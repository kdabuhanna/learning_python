#!/usr/bin/env python3

# Write a program that prints the reverse-complement of a DNA sequence
# You must use a loop and conditional

dna = 'ACTGAAAAAAAAAAA'
revcomp_dna = ''

for i in range(len(dna) -1, -1, -1):
	nt = dna[i]
	if nt == 'A':
		revcomp_dna += 'T'
	elif nt == 'G':
		revcomp_dna += 'C'
	elif nt == 'C':
		revcomp_dna += 'G'
	elif nt == 'T':
		revcomp_dna += 'A'
	else:
		revcomp_dna += 'N'
print(revcomp_dna)

"""
python3 anti.py
TTTTTTTTTTTCAGT
"""
