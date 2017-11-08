import pytest

from document_processor import DocumentProcessor

@pytest.fixture
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
    
