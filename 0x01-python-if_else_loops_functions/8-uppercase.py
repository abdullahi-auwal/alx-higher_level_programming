#!/usr/bin/python3
def uppercase(str):
    for i in str:
        int_equiv = ord(i)
        if ((int_equiv > 96) and (int_equiv < 123)):
            int_equiv = int_equiv - 32
        print("{:c}".format(int_equiv), end="")
    print()
