"""
Test the wordsearch module
"""
#pylint: disable=redefined-outer-name
import pytest
from wordsearch.wordsearch import WordSearch


@pytest.fixture
def testable_wordsearch():
    """Create a test matrix to be used in future tests"""

    word_list = ['YUM', 'BOA', 'YEP', 'YAM', 'CBM', 'GUY', 'MOM', 'UB', 'DAD']

    wordsearch = WordSearch(3, word_list)

    wordsearch.matrix[0] = ['Y', 'U', 'M']
    wordsearch.matrix[1] = ['A', 'O', 'B']
    wordsearch.matrix[2] = ['M', 'F', 'C']

    wordsearch.words_found = wordsearch.find_words()

    return wordsearch

def test_new_matrix():
    """Test creating a new matrix and confirm there are no default values remaining"""

    zeros_exist = False
    word_list = ['SOME', 'SMURFY', 'LIST']
    wordsearch = WordSearch(5, word_list)

    for _, row in enumerate(wordsearch.matrix):
        if '0' in row:
            zeros_exist = True

    assert wordsearch.matrix.shape == (5, 5)
    assert not zeros_exist

def test_finding_words_in_row(testable_wordsearch):
    """Test finding words in a row of a given matrix"""

    assert 'YUM' in testable_wordsearch.words_found
    assert 'BOA' in testable_wordsearch.words_found
    assert 'YEP' not in testable_wordsearch.words_found

def test_finding_words_in_column(testable_wordsearch):
    """Test finding words in a column of a given matrix"""

    assert 'YAM' in testable_wordsearch.words_found
    assert 'CBM' in testable_wordsearch.words_found
    assert 'GUY' not in testable_wordsearch.words_found

def test_finding_words_in_diagonals(testable_wordsearch):
    """Test finding words in the diagonals of a given matrix"""

    assert 'MOM' in testable_wordsearch.words_found
    assert 'UB' in testable_wordsearch.words_found
    assert 'DAD' not in testable_wordsearch.words_found

def test_printing_wordsearch(testable_wordsearch, capsys):
    """Test printing the WordSearch object"""

    testable_wordsearch.words_found = ['DAD', 'BROTHER', 'ZEBRA']
    print(testable_wordsearch)
    captured = capsys.readouterr()

    assert captured.out == "\nY U M\nA O B\nM F C\n\nBROTHER DAD ZEBRA\n"
    assert captured.err == ''
