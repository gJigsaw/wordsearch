# A Python Wordsearch created in One Hour

A wordsearch program created in 61 minutes (plus documentation time). Create a grid of random characters, then find the words from the provided words.txt file in the rows, columns, and diagonals, forwards and backwards.

## Getting Started

Clone this repository

Create a Virtual Environment
`python3 -m venv build_env`
`source build_env/bin/activate`

Install the PyTest requirement
`pip install -r requirements.txt`

To create your own 15 x 15 matrix and print the words found
`python3 wordsearch/wordsearch.py 15 ./words.txt`

For help with the command-line arguments
`python3 wordsearch/wordsearch.py -h`

To execute the tests
`python3 -m pytest tests`
