#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    _len = len(sys.argv)
    i = 1
    _sum = 0
    while (i < _len):
        _sum = _sum + int(sys.argv[i])
        i = i + 1
    print("{}".format(_sum))
