"""Retrieve and print words from a URL.

Usage:
    python modularity.py <URL>
"""
import sys
from urllib.request import urlopen

def fetch_words(url):
    """
    Fetch a list of words from a URL.

    Args:
        url: The URL of a UTF-8 text document.

    Return:
        A List of strings containing the words from the documemt.
    """
    example = urlopen(url)
    ex_words = []
    for line in example:
        line_word = line.decode('utf-8').split()
        for word in line_word:
            ex_words.append(word)
    example.close()
    return ex_words

    
def print_words(ex_words):
    """
    Print items one per line.

    Args:
        An iterable series of printable times.
    """
    for word in ex_words:
        print(word)

def main(url):
    """
    Print each word from a text document from at a URL

    Args:
        url: The URL of a UTF-8 text document
    """
    words = fetch_words(url)
    print_words(words)
    
if __name__ == '__main__':
    main(sys.argv[1])