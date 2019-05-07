"""
Test the wordsearch module
"""
import pytest
from wordsearch.wordsearch import WordSearch

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
