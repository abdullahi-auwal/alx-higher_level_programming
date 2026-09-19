#!/usr/bin/python3
def multiple_returns(sentence):
    ln = len(sentence)
    if ln == 0:
        tuple_s = (ln, None)
        return tuple_s
    else:
        tuple_s = (ln, sentence[0])
        return tuple_s
