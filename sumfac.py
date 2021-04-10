#!/usr/bin/env python3

# Write a program that computes the running sum from 1..n
# Also, have it compute the factorial of n while you're at it
# No, you may not use math.factorial()
# Use the same loop for both calculations

n = 5
n_sum = 0
n_fac = 1
for i in range(1, n+1):
	n_sum = n_sum + i
	n_fac = n_fac * i
print (n, n_sum, n_fac)
# your code goes here

"""
python3 sumfac.py
5 15 120
"""
