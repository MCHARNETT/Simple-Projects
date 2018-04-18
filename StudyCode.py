# -*- coding: utf-8 -*-
"""
Created on Fri Jul 28 21:07:31 2017

@author: harne
"""
import string

def isPalindrome(x):
    if x == x[::-1]:
        return True
    return False
def isPalindrome2(x):
    x = x.lower()
    letter_list = list(string.ascii_lowercase)
    for char in x:
        if char not in letter_list:
            x = x.replace(char, '')
    if x == x[::-1]:
        return True
    return False
print (isPalindrome("madamimadam"))
print (isPalindrome2("Madam, I'm Adam."))

def calcMedian(x):
    x = sorted(x)
    mid = 0
    if len(x) == 1:
        return x[0]
    if len(x)%2 != 0:
        mid = int((len(x)-1)/2)
        return x[mid]
    else:
        mid = int((len(x))/2)
        return (x[mid] + x[mid-1])/2.0

print (calcMedian([1, 5, 6, 4]))

def count0s(x):
    val = str(x)
    Count = 0
    for char in val:
        if char == '0':
            Count += 1
    return Count

print (count0s(5000))

def countMatrix0s(x):
    zeroes = 0
    for item in x:
        for value in item:
            if value == 0:
                zeroes += 1
    return zeroes

print (countMatrix0s([[9,0, 1,2], [4, 5, 3, 0], [0, 0, 4, 5]]))

def balance(x):
    total = 0
    balance = 0
    count = 0
    for item in x:
        for value in item:
                total += value
                count +=1
    new_total = round(total/count)
    for item in x:
        for value in item:
            if value > new_total:
                balance += 1
    return balance

print(balance([[9,0, 1,2], [4, 5, 3, 0], [0, 0, 4, 5]]))
    
def binarySearch(array, x):
    low = 0   
    for item in array:
        if item<=x:
            low += 1
    return low

print (binarySearch([1, 2, 3, 4,4,4, 4,5,6, 7], 5))
            
                           