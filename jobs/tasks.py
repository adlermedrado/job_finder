from celery import shared_task
from .services import GithubService, JobAnalyzerService, JobSanitizerService


@shared_task()
def fetch_github_issues():
    service = GithubService()
    service.get_job_descriptions()


@shared_task(acks_late=True, reject_on_worker_lost=True)
def analyze_jobs_descriptions():
    service = JobAnalyzerService()
    service.analyze()


@shared_task(acks_late=True, reject_on_worker_lost=True)
def sanitize_jobs_descriptions():
    service = JobSanitizerService()
    service.sanitize()
