import os

import pytest


@pytest.fixture(autouse=True)
def set_django_settings_module():
    os.environ['DJANGO_SETTINGS_MODULE'] = 'job_finder.settings'


@pytest.fixture
def mock_github_task(mocker):
    return mocker.patch('jobs.models.GithubTask.objects.all')


@pytest.fixture
def mock_job_description(mocker):
    return mocker.patch('jobs.models.JobDescription.objects')
