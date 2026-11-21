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
    c = 0
    while c < len(text) and text[c] == ' ':
        c += 1

    while c < len(text):
        print(text[c], end="")
        if text[c] == "\n" or text[c] in ".?:":
            if text[c] in ".?:":
                print("\n")
            c += 1
            while c < len(text) and text[c] == ' ':
                c += 1
            continue
        c += 1
