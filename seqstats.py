#!/usr/bin/env python3

import argparse
import mcb185
import statistics

# Write a program that computes statistics about a fasta file
#   Number of sequences
#   Total length
#   Minimum and maximum lengths
#   Average and median lengths
#   N50 length
# Use argparse
# Make useful functions and add them to your libraryimport argparse

parser = argparse.ArgumentParser(description='stats about sequence')
#required arguments
parser.add_argument('--file', required = True, type = str, 
	metavar='<str>', help = 'required fasta file')
arg = parser.parse_args()

length = []
for name, seq in mcb185.read_fasta(arg.file):
	length.append(len(seq))
length.sort()

print('min is', min(length)) #min
print('max is', max(length)) #max
print('sum is', sum(length)) #sum
print('mean is', statistics.mean(length)) #mean
print('median is', statistics.median(length)) #median

#n50 - sum values, once it is greater than 1/2 total sum, that is n50

runningsum = 0
total = sum(length)
for value in length:
	runningsum += value
	if runningsum > value:
		print('N50 is', value)
		break

