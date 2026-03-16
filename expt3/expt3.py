# -*- coding: utf-8 -*-
"""
Created on Mon Mar 16 04:36:04 2026

@author: User
"""

# simple interest
"""
Created on Mon Feb 16 05:00:03 2026

@author: priti
"""
def simple_interest(principal,rate,time):
  si = (principal *rate  *time) /100  
  return si 
 #taking input from the us
p=float(input ( "enter principal amount :"))
r=float(input ( "enter rate of interest :"))
t =float (input ( "enter time (in years ) :"))
 #function call
interest = simple_interest(p,r,t)
print ( "simple interest is :",interest)