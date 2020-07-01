import pytest


def test_noun_chunks_is_parsed_nb(nb_tokenizer):
    """Test that noun_chunks raises Value Error for 'nb' language if Doc is not parsed.
    To check this test, we're constructing a Doc
    with a new Vocab here and forcing is_parsed to 'False'
    to make sure the noun chunks don't run.
    """
    doc = nb_tokenizer("Smørsausen brukes bl.a. til")
    doc.is_parsed = False
    with pytest.raises(ValueError):
        list(doc.noun_chunks)