#!/usr/bin/python3
"""This module manipulate a text"""


def text_indentation(text):
    """
    Adds 2 lines after . ? and :

    Args:
        text (str): the string text to manipulate

    Raises:
        TypeError: if text isn't string
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    text = text.strip()
    c = 0

    while c < len(text):
        char = text[c]

        if char in ".?:":
            print(char, end="")
            print("\n")

            c += 1
            while c < len(text) and text[c] == ' ':
                c += 1

        elif char == "\n":
            print()
            c += 1
            while c < len(text) and text[c] == ' ':
                c += 1

        else:
            print(char, end="")
            c += 1
