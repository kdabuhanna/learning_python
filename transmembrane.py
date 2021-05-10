#!/usr/bin/env python3

import sys
import math

# Write a program that predicts if a protein is trans-membrane
# Trans-membrane proteins have the following properties
#	Signal peptide: https://en.wikipedia.org/wiki/Signal_peptide
#	Hydrophobic regions(s): https://en.wikipedia.org/wiki/Transmembrane_protein
#	No prolines in hydrophobic regions (alpha helix)
# Hydrophobicity is measued via Kyte-Dolittle
#	https://en.wikipedia.org/wiki/Hydrophilicity_plot
# For our purposes:
#	Signal peptide is 8 aa long, KD > 2.5, first 30 aa
#	Hydrophobic region is 11 aa long, KD > 2.0, after 30 aa

ids = []
proteins = []

with open(sys.argv[1]) as fp:
	seq = []
	for line in fp.readlines():
		line = line.rstrip() #strips line of spaces
		if line.startswith('>'): 
			words = line.split() #splits the line by spaces
			ids.append(words[0][1:]) #gets the ids of proteins and puts them in a list
			if len(seq) > 0: proteins.append(''.join(seq)) #gets aa seqs and adds them to proteins as str
			seq =[] #resets seq list
		else: 
			seq.append(line) #adds 
	proteins.append(''.join(seq))		

def kytedo(sequence):
	kdcount = 0
	for j in sequence: #window within the amino seq
		if j == 'P': kdcount -= 1.6
		if j == 'I': kdcount += 4.5 
		if j == 'V': kdcount += 4.2 
		if j == 'L': kdcount += 3.8 
		if j == 'F': kdcount += 2.8
		if j == 'C': kdcount += 2.5 
		if j == 'M': kdcount += 1.9 
		if j == 'A': kdcount += 1.8 
		if j == 'G': kdcount -= 0.4 
		if j == 'T': kdcount -= 0.7 
		if j == 'S': kdcount -= 0.8 
		if j == 'W': kdcount -= 0.9 
		if j == 'Y': kdcount -= 1.3 
		if j == 'H': kdcount -= 3.2 
		if j == 'E': kdcount -= 3.5 
		if j == 'Q': kdcount -= 3.5 
		if j == 'D': kdcount -= 3.5 
		if j == 'N': kdcount -= 3.5 
		if j == 'K': kdcount -= 3.9
		if j == 'R': kdcount -= 4.5 
	return kdcount

def noprolines(seq):
	for aa in seq:
		if aa == 'P': return True
	return False

def windowmaker(seq, win, kd):
	for i in range(len(seq)-win+1):
		frame = seq[i:i+win]
		kdcount = kytedo(frame)/win
		if kdcount >= kd and not noprolines(frame): 
			return True, i, frame, kdcount
	return False

for id, protein in zip(ids, proteins):
	nterm = protein[0:30]
	cterm = protein[30:]
	if windowmaker(nterm, 8, 2.5) and windowmaker(cterm, 11, 2.0):
		print(id)

"""
python3 Programs/transmembrane.py Data/at_prots.fa
AT1G75120.1
AT1G10950.1
AT1G75110.1
AT1G74790.1
AT1G12660.1
AT1G75130.1
"""
