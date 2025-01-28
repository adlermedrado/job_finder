from unittest.mock import MagicMock, patch

import pytest

from jobs.analyzers.openai import JobAnalyzer


@pytest.fixture
def mock_openai():
    with patch('jobs.analyzers.openai.OpenAI') as mock:
        yield mock

@pytest.fixture
def analyzer(mock_openai):
    api_key = 'test_api_key'
    return JobAnalyzer(api_key=api_key)

def test_analyze_job_description_fully_meets(analyzer, mock_openai):
    job_description = "We are looking for a Senior Python Developer for a fully remote position."
    mock_openai.return_value.chat.completions.create.return_value.choices = [MagicMock(message=MagicMock(content='Fully meets'))]

    result = analyzer.analyze_job_description(job_description)
    assert result == 'Fully meets'

def test_analyze_job_description_partially_meets(analyzer, mock_openai):
    job_description = "We are looking for a Developer for a remote position."
    mock_openai.return_value.chat.completions.create.return_value.choices = [MagicMock(message=MagicMock(content='Partially meets'))]

    result = analyzer.analyze_job_description(job_description)
    assert result == 'Partially meets'

def test_analyze_job_description_does_not_meet(analyzer, mock_openai):
    job_description = "We are looking for an intern."
    mock_openai.return_value.chat.completions.create.return_value.choices = [MagicMock(message=MagicMock(content='Does not meet'))]

    result = analyzer.analyze_job_description(job_description)
    assert result == 'Does not meet'

def test_analyze_job_description_api_error(analyzer, mock_openai):
    job_description = "We are looking for a Senior Developer."
    mock_openai.return_value.chat.completions.create.side_effect = Exception("API error")

    result = analyzer.analyze_job_description(job_description)
    assert result is None
