from app.main import normalize_question

def test_removes_surrounding_whitespaces():
    result = normalize_question(" What is RAG?  ")
    assert result == "What is RAG?"


def test_preserves_internal_spacing():
    result = normalize_question("Explain Apache  Spark")
    assert result == 'Explain Apache  Spark'


def test_whitespace_only_question_becomes_empty():
    result = normalize_question("   ")
    assert result == "" 