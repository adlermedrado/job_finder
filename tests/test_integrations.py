from unittest.mock import MagicMock

import pytest

from jobs.integrations import GithubIntegration


@pytest.fixture
def github_integration():
    mock_client = MagicMock()
    github_integration = GithubIntegration(github_token='fake_token')
    github_integration.client = mock_client
    return github_integration, mock_client


def test_fetch_issues(github_integration):
    integration, mock_client = github_integration
    mock_repo = MagicMock()
    mock_issue = MagicMock(id=1, title='Test Issue', body='This is a test issue', url='http://example.com/issue/1')

    mock_repo.get_issues.return_value = [mock_issue]
    mock_client.get_repo.return_value = mock_repo

    issues = integration.fetch_issues('owner/repo_name')

    assert len(issues) == 1
    assert issues[0]['id'] == 1
    assert issues[0]['title'] == 'Test Issue'
    assert issues[0]['body'] == 'This is a test issue'
    assert issues[0]['url'] == 'http://example.com/issue/1'
