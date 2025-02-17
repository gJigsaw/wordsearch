"""
Create a random wordsearch grid and identify words included
"""
import argparse
import random
import string
import numpy as np

class WordSearch:
    """Create a matrix of characters and find all the words included"""

    def __init__(self, matrix_size, words_to_find):
        self.matrix_size = matrix_size
        self.matrix = self.new_matrix()
        self.words_to_find = words_to_find
        self.words_found = self.find_words()

    def __repr__(self):
        matrix_strings = []
        self_string = "\n"

        for _, row in enumerate(self.matrix):
            matrix_strings.append(" ".join(row))

        self_string += "\n".join(matrix_strings)
        self_string += "\n\n"
        self_string += " ".join(sorted(self.words_found))

        return self_string

    def new_matrix(self):
        """Return a matrix of uppercase characters of height and width self.matrix_size"""

        uppercase_letters = string.ascii_uppercase

        # create a matrix with populated values of '0'
        wordsearch_matrix = np.full((self.matrix_size, self.matrix_size), '0')

        # replace the '0's with random characters from uppercase_letters
        for row_idx, row in enumerate(wordsearch_matrix):
            for col_idx, _ in enumerate(row):
                row[col_idx] = random.choice(uppercase_letters)
            wordsearch_matrix[row_idx] = row

        return wordsearch_matrix

    def find_words(self):
        """Return a list of words found in the matrix"""

        found_words = set()
        found_words.update(self._find_words_in_row())
        found_words.update(self._find_words_in_column())
        found_words.update(self._find_words_in_diagonal())

        return found_words

    def _find_words_in_row(self):
        """Return a set of words found in a row of the matrix"""

        words_found = set()
        for _, row in enumerate(self.matrix):
            search_string = "".join(row)
            words_found.update(self._find_words_in_string(search_string))

        return words_found

    def _find_words_in_column(self):
        """Return a set of words found in a column of the matrix"""

        words_found = set()
        for col in range(self.matrix_size):
            search_string = "".join(self.matrix[:, col])
            words_found.update(self._find_words_in_string(search_string))

        return words_found

    def _find_words_in_diagonal(self):
        """Return a set of words found in the diagonals of the matrix"""

        words_found = set()
        for diag in range(self.matrix_size):
            search_string = "".join(np.diagonal(self.matrix, diag))
            words_found.update(self._find_words_in_string(search_string))

        for diag in range(-1, 0-self.matrix_size, -1):
            search_string = "".join(np.diagonal(self.matrix, diag))
            words_found.update(self._find_words_in_string(search_string))

        flip_matrix = np.fliplr(self.matrix)
        for diag in range(self.matrix_size):
            search_string = "".join(np.diagonal(flip_matrix, diag))
            words_found.update(self._find_words_in_string(search_string))

        for diag in range(-1, 0-self.matrix_size, -1):
            search_string = "".join(np.diagonal(flip_matrix, diag))
            words_found.update(self._find_words_in_string(search_string))

        return words_found

    def _find_words_in_string(self, search_string):
        """Return a list of words found in a given string"""

        words_found = []

        for word in self.words_to_find:
            if (word in search_string) or (word in search_string[::-1]):
                words_found.append(word)

        return words_found

def grid_size_type(size):
    """Create a new argparse type to validate grid size is an integer greater than 2"""

    size = int(size)
    if size <= 2:
        raise argparse.ArgumentTypeError("Minimum grid size is 3 x 3")
    return size

def create_word_list_from_file(filehandle, grid_size):
    """Return a list of words to search for"""

    word_list = set(line.strip().upper() for line in filehandle if len(line) <= grid_size)

    return word_list

def main():
    """Create a wordsearch with provided size and word list file"""

    parser = argparse.ArgumentParser(description='Create a new Wordsearch')
    parser.add_argument('size', type=grid_size_type,
                        help="height and width of our wordsearch grid (min: 3)")
    parser.add_argument('wordfile', type=argparse.FileType('r'),
                        help="file including words to search for")
    parser_args = parser.parse_args()

    words_to_find = create_word_list_from_file(parser_args.wordfile, parser_args.size)
    parser_args.wordfile.close()
    new_wordsearch = WordSearch(parser_args.size, words_to_find)
    print(new_wordsearch)

if __name__ == "__main__":
    main()
