#!/usr/bin/env python3

import argparse
import mcb185
import random

# In prokaryotic genomes, genes are often predicted based on length
# Long ORFs are not expected to occur by chance
# Write a program that creates a histogram of ORF lengths in random DNA
# Your library should contain new functions for the following
#    1. generating random sequence
#    2. generating ORFs from sequence
# Your program should have command line options for the following:
#    + amount of sequence to generate
#    + GC fraction of sequence
# Thought questions
#    a. how does GC fraction affect the histogram?
#    b. what is a good length threshold for a gene?

parser = argparse.ArgumentParser(description='explore open reading frame length')
#no required arguments needed
parser.add_argument('--size', required = False, type = int, default = 450000, metavar='<str>', 
	help = 'genome size [(default)i]')
parser.add_argument('--orfmin', required = False, type = int, default = 1, metavar='<int>', 
	help = 'minimum open reading frame [(default)i]')
parser.add_argument('--gc', required = False, type = float, default = 0.5, metavar='<float>', 
	help = 'gc fraction [@(default).3f]')
parser.add_argument('--info', action='store_true',
	help='additional info')
parser.add_argument('--seed', action='store_true',
	help='fix random seed')
arg = parser.parse_args()

if arg.info: print(arg.size, arg.orfmin, arg.gc)
if arg.seed: random.seed(1)

seq = mcb185.randseq(arg.size, arg.gc)
#print(seq)

lengths = []
for i in range(len(seq)-2):
	start = None
	stop = None
	if seq[i:i+3] == 'ATG': 
		start = i
		for j in range(i, len(seq)-2, 3):
			codon = seq[j:j+3]
			if codon == 'TAA' or codon == 'TAG' or codon == 'TGA':
				stop = j
				break
	if stop != None: lengths.append(int((stop - start)/3))
lengths.sort()
count = 0
for n in lengths:
	if n > arg.orfmin: count += 1
#print(lengths)
#print(count)

histogram = []
histogram = [0] * int(lengths[-1]+1)
"""
n = 1
for i in range(len(lengths)):
	if int(lengths[i]) == n:
		histogram[n] += 1
	else: 
		if lengths[i] != lengths[-1]: n = int(lengths[i+1])
		else: 
			break


count2 = 0
for i in range(len(histogram)):
	count2 += histogram[i]

print(histogram)
print(lengths[-1], len(histogram), count2)
"""

for v in lengths:
	histogram[v] += 1
print(histogram)
#for v in histogram:
	#print(v)
