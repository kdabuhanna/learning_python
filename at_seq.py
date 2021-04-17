#!/usr/bin/env python3

import random
random.seed(1) # comment-out this line to change sequence each time

# Write a program that stores random DNA sequence in a string
# The sequence should be 30 nt long
# On average, the sequence should be 60% AT
# Calculate the actual AT fraction while generating the sequence
# Report the length, AT fraction, and sequence


bp = 30
seq = ''
at = 0
for i in range(bp):
	r = random.random()
	if r < 0.3:
		seq += 'A'
		at += 1
	elif r < 0.6:
		seq += 'T'
	elif r < 0.8:
		seq += 'C'
		at += 1
	elif r < 1:
		seq += 'G'
print(bp, at/bp, seq)



"""
python3 at_seq.py
30 0.6666666666666666 ATTACCGTAATCTACTATTAAGTCACAACC
"""
