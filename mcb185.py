import random
import sys

def read_fasta(filename):
	name = None
	seq = []
	
	with open(filename) as fp:
		while True:
			line = fp.readline()
			if line == '': break
			elif line.startswith('>'):
				if len(seq) > 0: # now is the time to return name, seq
					yield name, ''.join(seq)
				words = line.split()
				name = words[0][1:]
				seq = []
			else:
				line = line.rstrip()
				seq.append(line)
	yield name, ''.join(seq)

def gc(dna):
	g = dna.count('G')
	c = dna.count('C')
	return (g+c)/len(dna)

def n50(seq):
	length.sort()
	runningsum = 0
	total = sum(length)
	while runningsum < total/2:
		runningsum += length[i]
		i += 1
	return length[i]
	
def randseq(length, gc):
	seq = ''
	for i in range(length):
		if random.random() < gc:
			seq += random.choice('GC')
		else: seq += random.choice('AT')
	return seq

gcode = {
		'AAA' : 'K',	'AAC' : 'N',	'AAG' : 'K',	'AAT' : 'N',
		'ACA' : 'T',	'ACC' : 'T',	'ACG' : 'T',	'ACT' : 'T',
		'AGA' : 'R',	'AGC' : 'S',	'AGG' : 'R',	'AGT' : 'S',
		'ATA' : 'I',	'ATC' : 'I',	'ATG' : 'M',	'ATT' : 'I',
		'CAA' : 'Q',	'CAC' : 'H',	'CAG' : 'Q',	'CAT' : 'H',
		'CCA' : 'P',	'CCC' : 'P',	'CCG' : 'P',	'CCT' : 'P',
		'CGA' : 'R',	'CGC' : 'R',	'CGG' : 'R',	'CGT' : 'R',
		'CTA' : 'L',	'CTC' : 'L',	'CTG' : 'L',	'CTT' : 'L',
		'GAA' : 'E',	'GAC' : 'D',	'GAG' : 'E',	'GAT' : 'D',
		'GCA' : 'A',	'GCC' : 'A',	'GCG' : 'A',	'GCT' : 'A',
		'GGA' : 'G',	'GGC' : 'G',	'GGG' : 'G',	'GGT' : 'G',
		'GTA' : 'V',	'GTC' : 'V',	'GTG' : 'V',	'GTT' : 'V',
		'TAA' : '*',	'TAC' : 'Y',	'TAG' : '*',	'TAT' : 'Y',
		'TCA' : 'S',	'TCC' : 'S',	'TCG' : 'S',	'TCT' : 'S',
		'TGA' : '*',	'TGC' : 'C',	'TGG' : 'W',	'TGT' : 'C',
		'TTA' : 'L',	'TTC' : 'F',	'TTG' : 'L',	'TTT' : 'F',
	}

def translate(seq):
		prot = ''
		seq = seq.upper()
		for i in range(0, len(seq)-2, 3):
			codon = seq[i:i+3]
			if codon in gcode:
				prot += gcode[codon]
			else:
				prot = 'X'
		return prot

def anti(dna):
	seq = ''
	for c in dna[::-1]:
		if   c == 'A': seq += 'T'
		elif c == 'C': seq += 'G'
		elif c == 'G': seq += 'C'
		elif c == 'T': seq += 'A'
		else: seq += 'N'
	return seq

def longestorf(seq):
	longestorf = ''
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
		if stop != None:
			if len(longestorf) < len(seq[i:j+3]):
				longestorf = seq[i:j+3]
	return longestorf
