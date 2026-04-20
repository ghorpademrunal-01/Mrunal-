# -*- coding: utf-8 -*-
"""
Created on Mon Apr 20 11:05:56 2026

@author: User mrunal ghorpade
"""

class Vehicle:
    def __init__(self, name, distance, fuel):
        self.name = name
        self.distance = distance
        self.fuel = fuel

    def efficiency(self):
        eff = self.distance / self.fuel
        print("Vehicle:", self.name)
        print("Fuel Efficiency:", eff, "km/l")


# Run
v = Vehicle("Bike", 200, 5)
v.efficiency()

