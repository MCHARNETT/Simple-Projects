# -*- coding: utf-8 -*-
"""
Created on Fri Aug  4 15:50:13 2017

@author: harne
"""
def Caesar_cipher(word, x):
    new_word = ''
    for char in word:
        if char.isupper():
            start = ord('A')
        elif char.islower():
            start = ord('a')
        new_word += chr(((ord(char)-start+x)%26+start))

    return new_word


print(Caesar_cipher("Hello", 30))