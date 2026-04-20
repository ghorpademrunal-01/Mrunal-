# -*- coding: utf-8 -*-
"""
Created on Mon Apr 20 10:36:44 2026

@author: User mrunal ghorpade
"""

class BankAccount:
    def __init__(self):
        self.balance = 0

    def deposit(self, amount):
        self.balance = self.balance + amount

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient balance")
        else:
            self.balance = self.balance - amount

    def show(self):
        print("Balance:", self.balance)


# Main program
acc = BankAccount()

acc.deposit(1000)
acc.withdraw(400)
acc.show()
        
    