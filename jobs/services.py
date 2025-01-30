import logging
from typing import List, Optional

from django.db import transaction
from django.db.models import QuerySet
from django.utils import timezone

from job_finder import settings
from jobs.analyzers.openai import JobAnalyzer
from jobs.integrations import GithubIntegration
from jobs.models import GithubTask, JobDescription
from jobs.sanitizer import MultiLangSanitizer

logger = logging.getLogger(__name__)


class GithubService:
    def get_job_descriptions(self) -> None:
        logger.info('Starting to retrieve job descriptions from Github')

        tasks: List[GithubTask] = GithubTask.objects.all()
        existing_ids: set = set(JobDescription.objects.values_list('external_id', flat=True))
        logger.debug(f'Existing job description IDs: {existing_ids}')

        gh = GithubIntegration(settings.GITHUB_TOKEN)
        new_job_descriptions: List[JobDescription] = []

        for task in tasks:
            source_name: str = task.source.name
            logger.info(f'Fetching job descriptions for task: {source_name}')

            issues = self._fetch_github_issues(gh, source_name)
            if not issues:
                continue

            new_job_descriptions.extend(self._create_job_descriptions(issues, existing_ids, task.source))

        if new_job_descriptions:
            self._bulk_save_job_descriptions(new_job_descriptions)
        else:
            logger.info('No new job descriptions found.')

    def _fetch_github_issues(self, gh: GithubIntegration, source_name: str) -> Optional[List[dict]]:
        try:
            return gh.fetch_issues(source_name)
        except ConnectionError as e:
            logger.error(f'Connection error fetching issues for {source_name}: {e}')
        except Exception as e:
            logger.error(f'Unexpected error fetching issues for {source_name}: {e}')
        return None

    def _create_job_descriptions(self, issues: List[dict], existing_ids: set, source) -> List[JobDescription]:
        new_descriptions = []
        for issue in issues:
            issue_id: str = str(issue['id'])
            if issue_id not in existing_ids:
                logger.info(f'New issue found: {issue["title"]}. Saving...')
                new_descriptions.append(
                    JobDescription(
                        external_id=issue_id,
                        title=issue['title'],
                        description=issue['body'],
                        source=source,
                        url=issue['url'],
                    )
                )
        return new_descriptions

    def _bulk_save_job_descriptions(self, job_descriptions: List[JobDescription]) -> None:
        with transaction.atomic():
            JobDescription.objects.bulk_create(job_descriptions)
        logger.info(f'Created {len(job_descriptions)} new job descriptions.')


class JobAnalyzerService:
    def analyze(self) -> None:
        logger.info('Starting to analyze job descriptions')
        job_descriptions = JobDescription.objects.filter(is_analyzed=False, is_sanitized=True)
        logger.info(f'Found {len(job_descriptions)} job descriptions to analyze.')
        job_analyzer = JobAnalyzer(settings.OPENAI_API_KEY)

        for job_description in job_descriptions:
            self._analyze_job_description(job_analyzer, job_description)

    def _analyze_job_description(self, job_analyzer: JobAnalyzer, job_description: JobDescription) -> None:
        logger.info(f'Analyzing job description: {job_description.title}')
        try:
            result: Optional[str] = job_analyzer.analyze_job_description(job_description.description)
            if not result:
                raise ValueError('No result returned from JobAnalyzer')

            logger.info(f'Analysis result for {job_description.title}: {result}')
            self._update_job_description(job_description, criteria_status=result)
        except ValueError as e:
            logger.error(f'Value error analyzing job description {job_description.title}: {e}')
            self._update_job_description(job_description, criteria_status='Error')
        except Exception as e:
            logger.error(f'Unexpected error analyzing job description {job_description.title}: {e}')
            self._update_job_description(job_description, criteria_status='Error')

    def _update_job_description(self, job_description: JobDescription, criteria_status: str) -> None:
        job_description.criteria_status = criteria_status
        job_description.is_analyzed = True
        job_description.updated_at = timezone.now()
        job_description.save()
        logger.info(f'Job description updated: {job_description.title} with status: {criteria_status}')


class JobSanitizerService:
    def __init__(self):
        self.sanitizer = MultiLangSanitizer()

    def sanitize(self) -> None:
        updated_job_descriptions = []
        job_descriptions = self._fetch_job_descriptions()
        for job_description in job_descriptions:
            job_description.description = self.sanitizer.sanitize(job_description.description)
            job_description.updated_at = timezone.now()
            job_description.is_sanitized = True
            updated_job_descriptions.append(job_description)

        self._bulk_save_job_descriptions(updated_job_descriptions)

    def _fetch_job_descriptions(self):
        return JobDescription.objects.filter(is_analyzed=False, is_sanitized=False)

    def _bulk_save_job_descriptions(self, job_descriptions: List[JobDescription]) -> None:
        with transaction.atomic():
            JobDescription.objects.bulk_update(job_descriptions, ['description', 'updated_at', 'is_sanitized'])
        logger.info(f'Updated {len(job_descriptions)} sanitized job descriptions.')
