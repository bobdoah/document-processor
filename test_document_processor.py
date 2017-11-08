import string

import pytest

from document_processor import DocumentProcessor

@pytest.fixture(scope="function")
def document_processor():
    d = DocumentProcessor()
    yield d

def test_single_letters(document_processor):
    document = "a b c d e f g a b c d e"
    document_processor.process_document(document)
    assert not(document_processor.most_common_words())
    most_common_letters = document_processor.most_common_letters() 
    for most_common_letter in ('a', 'b', 'c', 'd', 'e'): 
        assert (most_common_letter, 2) in most_common_letters

@pytest.mark.parametrize("document", 
        ("'hello' hello", "\"hello\" hello", "(hello) hello", "[hello] hello", "{hello} hello",
            "<hello> hello", "hello? hello", "hello! hello", "hello, hello", "hello; hello", "hello. hello"),
        ids=("single_quotes", "double_quotes", "parenthesis", "brackets", "braces", "chevrons", 
            "question_marks", "exclamation_marks", "commas", "semi_colons", "full_stops"))
def test_ignore_punctuation(document_processor, document):
    document_processor.process_document(document)
    assert ("hello", 2) in document_processor.most_common_words()

def test_whitespace(document_processor):
    document_processor.process_document(string.whitespace + "hello")
    most_common_words = dict(document_processor.most_common_words()).keys()
    most_common_letters = dict(document_processor.most_common_letters()).keys()
    for whitespace_char in string.whitespace:
        assert whitespace_char not in most_common_words
        assert whitespace_char not in most_common_letters

def test_hyphen(document_processor):
    document_processor.process_document("sugar-free sugar-rush sugar-high")
    most_common_words = document_processor.most_common_words()
    assert ("sugar", 3) in most_common_words
    assert ("rush", 1) in most_common_words
    assert ("free", 1) in most_common_words
    assert ("high", 1) in most_common_words

