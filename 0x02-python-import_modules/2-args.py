#!/usr/bin/python3
import sys
if __name__ == "__main__":
    _len = len(sys.argv)
    i = 1
    if (_len == 1):
        print("0 arguments.")
    elif (_len == 2):
        print("1 argument:")
        print("{}: {}".format(i, sys.argv[i]))
    elif (_len > 2):
        print("{} arguments:".format(_len - 1))
        while (i < _len):
            print("{}: {}".format(i, sys.argv[i]))
            i = i + 1
