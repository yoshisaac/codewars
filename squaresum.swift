#!/bin/swift
//https://www.codewars.com/kata/515e271a311df0350d00000f/train/swift

func squareSum(_ vals: [Int]) -> Int {
    var sum: Int = 0
    for i in vals {
        sum += (i*i)
    }
    return sum
}

print(squareSum([]))
print(squareSum([1, 2, 2]))
