#!/usr/bin/env python3

# Write a program that computes typical stats
# Count, Min, Max, Mean, Std. Dev, Median
# No, you cannot import the stats library!

# Did with Maribel A. 

import sys
import math

p = []
sum2 = 0.0000
sigsq = 0
for i in sys.argv[1:]:
	p.append(float(i))

print('Count: ', len(p)) #count
p.sort()
print('Minimum: ', p[0]) #min
print('Maximum: ', p[-1]) #max

for j in range(len(p)):
	sum2 = sum2 + p[j]
mean = sum2/len(p)
print('Mean: ', f'{mean:.3f}') #mean

for k in range(len(p)):
	sigsq = sigsq + ((p[k] - mean) ** 2)
before = sigsq / len(p)
print('Standard Deviation: ', f'{math.sqrt(before):.3f}') #stdev

med_def = len(p) // 2 #median
med_even = 0
if len(p) % 2 == 1: print('Median: ', f'{p[med_def]:.3f}')
if len(p) % 2 == 0: 
	med_even = (p[med_def-1] + p[med_def])/2
	print('Median: ', f'{med_even:.3f}') 

"""
python3 stats.py 3 1 4 1 5
Count: 5
Minimum: 1.0
Maximum: 5.0
Mean: 2.800
Std. dev: 1.600
Median 3.000
"""
