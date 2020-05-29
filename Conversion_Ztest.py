# -*- coding: utf-8 -*-
"""

@author: kpericak

"""
##Comparing two conversion rates (of versions A and B)
 

import math 

#input the below four numbers
a_converted = 90
a_total = 369

b_converted = 72
b_total = 362

#math
a = a_converted/a_total
b = b_converted/b_total
c = (a_converted + b_converted) / (a_total + b_total)

z_score_num = (a-b) 
z_score_dem = ((a*(1-a))/a_total) + ((b*(1-b))/b_total) 
#c * (1-c) * ( (1/a_total) + (1/b_total) ), #assumes equal variances
z_score_dem = math.sqrt(z_score_dem)
z_score = z_score_num / z_score_dem

lift = (a-b)/b

lift_perc = '{:.2%}'.format(lift)
a_perc = '{:.2%}'.format(a)
b_perc = '{:.2%}'.format(b)
z_score_3dig = '{:.3f}'.format(z_score)


#print results
print("Does A Create Lift Versus B?")
#alpha = 0.05, 1.96 z-score
print("Conversion for A is " + str(a_perc) + ".")
print("Conversion for B is " + str(b_perc) + ".")

if  z_score > 1.65:
    print(str(z_score_3dig) + " is the z-score. A is statistically greater than B. Reject the null hypothesis that A is less than or equal to B.")
    print("The lift of A versus B is " + str(lift_perc) + ".")
else:
    print(str(z_score_3dig)+ " is the z-score. A does not provide lift versus B.")



#using an example from this blog http://juangabrielgomila.com/en/how-to-properly-analyze-an-ab-testing/ to show proof of answer

