# -*- coding: utf-8 -*-
"""
Created on Mon Aug 14 14:35:27 2017

@author: harne
"""
#Hackerrank Max Sum

def maximumSum(a, m):
    mz = 0
    for i in range(len(a)):
        for j in range(i, len(a)):
            value = sum(a[i:j+1])%m
            if value>mz:
                mz = value
    return mz
result = maximumSum([3, 3, 9, 9, 5], 7)
print(result)