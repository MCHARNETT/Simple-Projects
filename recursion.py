# -*- coding: utf-8 -*-
"""
Created on Fri Jul 28 11:26:39 2017

@author: MacKenzie Harnett
"""

def main():
    print (sum(10))

def sum(x):
    if x==1:
        return 1
    elif x>1:
        return sum(x-1)+x

print (main())

def fibbonaci(n):
    ''' returns the value of a fibbonaci
    sequence at index n
    '''
    if n<=1:
        return n
    else:
        return fibbonaci(n-1) + fibbonaci(n-2)
'result = input("Enter the value of the index of the fibbonaci number you want to find ")    '
'print (fibbonaci(int(result)))'

def digits(n):
    if n<10:
        return 1
    else:
        return digits(n/10) + 1
print (digits(15105))

def is_max(A):
    '''returns the maximum of integers in list n. 
    '''
    if len(A) == 1:
        return A[0]
    else:
        B = is_max(A[1:])
        return B if B>A[0] else A[0]

A = [1, 4, 5, 2, 10, 2]
print (is_max(A))

def multiply(a, b):
    if b == 0:
        return 0
    else:
        return a + multiply(a, b-1)

print (multiply(3, 50))

def exponential(base, exp):
    if exp == 1:
        return base
    else:
        return base*exponential(base, exp-1)
print (exponential(2, 4))

def print_from_n(n):
    if n == 0:
        print (0)
    else:
        print (print_from_n(n-1))
        print (n)
        
print_from_n(10)

def reverse(word):
    if len(word)==1:
        return word[0]
    else:
        return word[len(word)-1] + reverse(word[0:len(word)-1])
print (reverse("hello"))

def is_prime(n, value=2):
    if n < value**2:
        return True
    elif(n%value != 0):
        return is_prime(n, value + 1) 
    return False

print(is_prime(11))

def max_val(t): 
    """ t, tuple 
        Each element of t is either an int, a tuple, or a list
        No tuple or list is empty
        Returns the maximum int in t or (recursively) in an element of t """ 
    list_max = []
    if type(t) == int:
        return t

    else:
        for item in t:
            list_max.append(max_val(item))
    return max(list_max)   
print(max_val((5, (1,2), [[1],[9]])))


