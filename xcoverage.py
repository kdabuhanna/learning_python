#!/usr/bin/env python3

# Write a program that simulates random read coverage over a chromosome
# Report min, max, and average coverage
# Make variables for genome size, read number, read length
# Input values from the command line
# Note that you will not sample the ends of a chromosome very well
# So don't count the first and last parts of a chromsome

# Did with Maribel A. 

import sys
import random
#make variables of input in order genome size, read number and read length
size = int(sys.argv[1])
read_no = int(sys.argv[2])
read_len = int(sys.argv[3])

# make random reads
genome = [0] * size
for i in range(read_no):
	r = random.randint(0, size - read_len)
	for j in range(read_len):
		genome[j + r] += 1

#min, max, mean reads
min1 = genome[0]
max1 = genome[0]
sum2 = 0.00000
#count = 0.00000 #count for places read
for i in range(1, len(genome)):
	if genome[i] < min1: min1 = genome[i]
	if genome[i] > max1: max1 = genome[i]
for j in range(len(genome)):
	sum2 += genome[j]
	#if genome[j] != 0: count += 1 
mean = float(sum2/len(genome)) 
#print(sum2, count, mean)
print(min1, max1, f'{mean:.5f}')

"""
python3 xcoverage.py 1000 100 100
5 20 10.82375
"""
