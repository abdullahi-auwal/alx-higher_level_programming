#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    n_tuple_a = tuple_a
    n_tuple_b = tuple_b

    if (len(n_tuple_a) == 0):
        n_tuple_a = (0, 0)
    if (len(n_tuple_b) == 0):
        n_tuple_b = (0, 0)
    if (len(n_tuple_a) == 1):
        n_tuple_a = (n_tuple_a[0], 0)
    if (len(n_tuple_b) == 1):
        n_tuple_b = (n_tuple_b[0], 0)

    sum_tuple = (n_tuple_a[0] + n_tuple_b[0],
                 n_tuple_a[1] + n_tuple_b[1])
    return sum_tuple
