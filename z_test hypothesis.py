# -*- coding: utf-8 -*-
"""
Created on Sun Sep 15 11:56:35 2019

@author: kpericak
"""

#calculating if a result is statistically different that b result as well as the lift
#using example from https://www.statisticshowto.datasciencecentral.com/z-test/

import math 

#input the below four numbers
a_converted = 41
a_total = 195

b_converted = 351 
b_total = 605

#conversion ratio
a = a_converted/a_total
b = b_converted/b_total
c = (a_converted + b_converted) / (a_total + b_total)

z_score_num = (a-b) - 0  
z_score_dem = (c * (1-c)) * ( (1/a_total) + (1/b_total) )
z_score_dem = math.sqrt(z_score_dem)
z_score = z_score_num / z_score_dem

lift = (a-b)/b

lift_perc = '{:.1%}'.format(lift)
a_perc = '{:.1%}'.format(a)
b_perc = '{:.1%}'.format(b)
z_score_2dig = '{:.2f}'.format(z_score)

#alpha = 0.05, 1.96 z-score

#print results
print("Conversion for A is " + str(a_perc) + ".")
print("Conversion for B is " + str(b_perc) + ".")

if  abs(z_score) > 1.96:
    print(str(z_score_2dig) + " is the z-score. A is statistically different than B. Reject the null hypothesis that they are the same.")
    print("The lift of A versus B is " + str(lift_perc) + ".")
else:
    print(str(z_score_2dig)+ " is the z-score. A and B are not statistically different.")

 