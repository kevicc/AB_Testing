# -*- coding: utf-8 -*-
""" 
Created on Sun Sep 15 14:53:04 2019

@author: kpericak
"""

#Writing Answers to Questions in https://saylordotorg.github.io/text_introductory-statistics/s13-two-sample-problems.html with Python

import math

"""
To compare customer satisfaction levels of two competing cable television companies, 174 customers of Company 1 and 355 customers
of Company 2 were randomly selected and were asked to rate their cable companies on a
five-point scale, with 1 being least satisfied and 5 most satisfied. The survey results are summarized in the following table:
Construct a point estimate and a 99% confidence interval for μ1−μ2, the difference in average satisfaction levels of customers of the
"""

#Company 1	
n1 = 174	
x1 = 3.51	
s1 = 0.51	


#Company 2
n2 = 355
x2 = 3.24
s2 = 0.52

#Error
alpha_99 = 0.01
alpha_split = alpha_99/2
critical_value = 2.576 #this comes from a table

#Point estimate
point_estimate = x1- x2
print("The point estimate is " + str('{:.2f}'.format(point_estimate)) + ".\n")


#The difference in means lies between:
company1 = (s1**2)/n1
company2 = (s2**2)/n2
confidence =  math.sqrt((company1 + company2))
higher = point_estimate +  critical_value * confidence
lower = point_estimate -  critical_value * confidence
print("If this test is repeated, we are " + str('{:.0%}'.format(1-alpha_99)) 
      + " confident that the average level of customer satisfaction for company 1 will be between "
      + str('{:.2f}'.format(lower)) + " - " + str('{:.2f}'.format(higher))
      + " points higher, on the five-point scale, than that of company 2." )


#Z test
#Ho = x1-x1 > 0
z_score = point_estimate / confidence

if  z_score > 2.326:
    print(str('{:.3f}'.format(z_score)) + " is the z-score. At " +  str('{:.0%}'.format(1-alpha_99)) 
    + " confidence, Company 1's satisfaction score is statistically greater than Company 2's." +
    " Reject the null hypothesis.")
    
else:
    print(str('{:.3f}'.format(z_score)) + " is the z-score. Company 1's satisfaction score is not statistically higher than Company 2's.")

