# -*- coding: utf-8 -*-
"""
Created on Thu Jul 27 12:56:02 2017

@author: MacKenzie Harnett
"""
class CornellGrades(object):
    def __init__(self, grades):
        self.grades = grades
        
    def addGrades(self, grade):
        self.grades.append(grade)
        
    def getGrades(self):
        return self.grades
    
    def getPercentage(self):
        percentage = float(sum(self.grades))/len(self.grades)
        return round(percentage, 2)
    

gradeList = []
print (' ab '.strip())
