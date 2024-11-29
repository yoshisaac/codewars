#!/bin/python
#https://www.codewars.com/kata/57cff961eca260b71900008f/train/python

def is_vow(inp):
    return [c if str(c) == "a" or str(c) == "e" or str(c) == "i" or str(c) == "o" or str(c) == "u" else ord(c) for c in [chr(c) if type(c) != str else c for c in inp]]

print(is_vow([100,100,116,105,117,121 ]))
