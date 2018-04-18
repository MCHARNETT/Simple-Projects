# -*- coding: utf-8 -*-
"""
Created on Wed Jul 26 11:07:59 2017

@author: harne
"""
import sys
def fibonacciSeries(n):
    ''' n is the range of values that the program will calculate
    the series up to.
    returns a list of the fibbonaci numbers in that range.
    '''
    fibbonaci_numbers = [1, 1]
    for i in range(n):
        if i>1:
            fibbonaci_numbers.append(fibbonaci_numbers[i-1]+fibbonaci_numbers[i-2])
            
    return fibbonaci_numbers


result = int(input("enter the value you want to calculate the fibbonacci sequence up to: "))

print (fibonacciSeries(result))