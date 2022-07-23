# -*- coding: utf-8 -*-
""" 
Created on Sun Sep 15 14:53:04 2019

@author: kevicc

"""
import math

group1= "G1"
group2 = "G2"

print("Are the means different?")
print("Null: U1 - U2 = 0 Alternative U1 - U2 != 0; Two tailed z test")
print("")

#Group 1
print(group1)
n1 = 40
x1 = 3.1
s1 = 1


#Group 2
print(group2)
n2 = 36
x2 = 3.8
s2 = 1.5

#Error
alpha_95 = 0.05
alpha_split = alpha_95/2
critical_value = 1.96
critical_value_neg = -1.96

#Calculation
top = (x1 - x2) - 0
bottom1 = s1**2/n1
bottom2 = s2**2/n2
bottom = math.sqrt(bottom1 + bottom2)
z = top/bottom
print("Top: ", top)
print("Bottom: ", bottom)
print("Z score: ", z)
print("")

print("Answer")
if z < critical_value_neg:
    print("Significant, reject")
elif z > critical_value:
    print("Significant, reject")
else: print("Not significant, do not reject")
