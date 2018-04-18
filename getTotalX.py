# -*- coding: utf-8 -*-
"""
Created on Thu Jul 27 12:14:50 2017

@author: MacKenzie Harnett
"""
import sys
def getTotalX(a, b):
    ''' returns list of common factors of list b.
    '''
    if min(a)>max(b):
        return []
    factors = []
    if len(b) != 1:
        for i in range(len(b)-1):
            for j in range(1, min(b)+1):
                if b[i]%j == 0:
                    if j not in factors:
                        factors.append(j)
        
    else:
        for i in range(len(b)):
            for j in range(1, min(b)+1):
                if b[i]%j == 0:
                    if j not in factors:
                        factors.append(j)
    for item in a:
        for value in factors:
            if value%item != 0:
                factors.remove(value)
    for number in b:
        for stupid in factors:
            if number%stupid != 0:
                factors.remove(stupid)
    return factors             

    

n, m = input().strip().split(' ')
n, m = [int(n), int(m)]
a = list(map(int, input().strip().split(' ')))
b = list(map(int, input().strip().split(' ')))
total = getTotalX(a, b)
if len(total) !=0:
    for item in a:
        for value in total:
            if value%item != 0:
                total.remove(value)
print(len(total))