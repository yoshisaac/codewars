#!/bin/python
#https://www.codewars.com/kata/525f50e3b73515a6db000b83/train/python
def create_phone_number(n): return '('+"".join(str(c) for c in n[0:3])+') '+"".join(str(c) for c in n[3:6])+'-'+"".join(str(c) for c in n[6:11])

print(create_phone_number([1, 2, 3, 4, 5, 6, 7, 8, 9, 0]))
