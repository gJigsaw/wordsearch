# WordSearch

A wordsearch program that allows for the creation and automated searching of a grid of letters.

Create a grid of random letters.
Find words within the grid's rows, columns, and diagonals - both forwards and backwards.

## Getting Started

Clone this repository

Create a Virtual Environment using [pipenv](https://docs.pipenv.org/en/latest/install/)
```
pipenv --three
```

Install the PyTest requirement
```
pipenv install --ignore-pipfile
```

Enter the Virtual Environment
```
pipenv shell
```

To create your own 15 x 15 matrix and print the words found
```
python3 wordsearch/wordsearch.py 15 ./words.txt
```

For help with the command-line arguments
```
python3 wordsearch/wordsearch.py -h
```

To execute the tests
```
pipenv install --dev --ignore-pipfile
python3 -m pytest tests
```
