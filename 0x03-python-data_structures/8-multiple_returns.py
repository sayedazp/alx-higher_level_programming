#!/usr/bin/python3
def multiple_returns(sentence):
    len1 = len(sentence)
    f_char = sentence[0] if len1 else None
    return len1, f_char
