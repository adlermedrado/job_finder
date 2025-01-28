import pytest

from jobs.sanitizer import MultiLangSanitizer


@pytest.fixture
def sanitizer():
    return MultiLangSanitizer()


def test_sanitize_removes_person_entity(sanitizer):
    text = 'My name is John Doe and I live in New York.'
    sanitized_text = sanitizer.sanitize(text)
    assert 'John Doe' not in sanitized_text
    assert 'New York' not in sanitized_text
    assert 'My name is and I live in' in sanitized_text

def test_sanitize_removes_org_entity(sanitizer):
    text = 'I work at Mercadinho do João.'
    sanitized_text = sanitizer.sanitize(text)
    assert 'Mercadinho' not in sanitized_text
    assert 'João' not in sanitized_text


def test_sanitize_removes_email(sanitizer):
    text = 'Contact me at john.doe@example.com.'
    sanitized_text = sanitizer.sanitize(text)
    assert 'john.doe@example.com' not in sanitized_text


def test_sanitize_removes_phone_number(sanitizer):
    text = 'Call me at 123-456-7890.'
    sanitized_text = sanitizer.sanitize(text)
    assert '123-456-7890' not in sanitized_text


def test_sanitize_special_characters(sanitizer):
    text = 'Hello! This is a test with special characters: @#$%^&*()'
    sanitized_text = sanitizer.sanitize(text)
    assert 'Hello This is a test with special characters' in sanitized_text


def test_sanitize_multiple_entities(sanitizer):
    text = 'My name is Jane Doe, I work at Acme Corp, and my email is jane.doe@example.com.'
    sanitized_text = sanitizer.sanitize(text)
    assert 'Jane Doe' not in sanitized_text
    assert 'Acme Corp' not in sanitized_text
    assert 'jane.doe@example.com' not in sanitized_text


def test_sanitize_empty_string(sanitizer):
    text = ''
    sanitized_text = sanitizer.sanitize(text)
    assert sanitized_text == ''


def test_sanitize_no_entities(sanitizer):
    text = 'This is a clean text without any entities'
    sanitized_text = sanitizer.sanitize(text)
    assert sanitized_text == text
