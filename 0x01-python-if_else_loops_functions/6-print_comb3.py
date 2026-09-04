#!/usr/bin/python3
for i in range(1, 89):
    for j in [10, 11, 20, 21, 22, 30, 31, 32, 33, 40, 41, 42,
              43, 44, 50, 51, 52, 53, 54, 55, 60, 61, 62, 63,
              64, 65, 66, 70, 71, 72, 73, 74, 75, 76, 77]:
        if (i == j):
            break
    if (i == j):
        continue
    print("{:02},".format(i), end=" ")
print("89")
