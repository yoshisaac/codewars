#!/bin/python
#https://www.codewars.com/kata/5264d2b162488dc400000001/python

def spin_words(sentence:str):
    words:str = sentence.split()
    for word in words:
        if len(word) >= 5:
            words[words.index(word)] = words[words.index(word)][::-1]
    return " ".join(words)

print(spin_words("awdawd dba aaaad"))
