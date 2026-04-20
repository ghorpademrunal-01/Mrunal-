# -*- coding: utf-8 -*-
"""
Created on Mon Apr 20 11:03:01 2026

@author: User mrunal ghorpade
"""

class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def calculate_grade(self):
        if self.marks >= 90:
            grade = "A"
        elif self.marks >= 75:
            grade = "B"
        elif self.marks >= 50:
            grade = "C"
        else:
            grade = "Fail"

        print("Name:", self.name)
        print("Grade:", grade)


# Run
s = Student("Mrunal", 85)
s.calculate_grade()

