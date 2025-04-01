#!/bin/python
#https://www.codewars.com/kata/530e15517bc88ac656000716/solutions/python

def rot13(message): return "".join([((((chr((ord(c)+13)%122)), "z")[c == "m"]), c)[not (c in "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz")] if c.lower() == c and (ord(c)+13) >= 97 and (ord(c)+13) <= 122 else ((((chr(((ord(c)+13)%90, (ord(c)+13)%90+64) [(ord(c)+13)%90 < 65])), "Z")[c=="M"]), c)[not (c in "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz")] for c in message])

print(rot13("M"))
print(rot13("N"))
print(rot13("m"))
print(rot13("n"))
print(rot13("A"))
print(rot13("test"))
print(rot13("Test"))
print(rot13("aA bB zZ 1234 *!?%"))
print(rot13("!@#$%^&*+?~()_-+=:;"))
print(rot13("grfg"))
