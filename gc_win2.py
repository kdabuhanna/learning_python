#!/usr/bin/env python3

# Write a program that computes the GC fraction of a DNA sequence in a window
# Window size is 11 nt
# Output with 4 significant figures using whichever method you prefer
# Use no nested loops. Instead, count only the first window
# Then 'move' the window by adding 1 letter on one side
# And subtracting 1 letter from the other side
# Describe the pros/cons of this algorith vs. nested loops

seq = 'ACGACGCAGGAGGAGAGTTTCAGAGATCACGAATACATCCATATTACCCAGAGAGAG'
w = 11
gc_count = 0
for j in range(len(seq)-int(w-1)): 
	if seq[0] == "C" or seq[0] == "G": gc_count += 1
	if seq[1] == "C" or seq[1] == "G": gc_count += 1
	if seq[2] == "C" or seq[2] == "G": gc_count += 1
	if seq[3] == "C" or seq[3] == "G": gc_count += 1
	if seq[4] == "C" or seq[4] == "G": gc_count += 1
	if seq[5] == "C" or seq[5] == "G": gc_count += 1
	if seq[6] == "C" or seq[6] == "G": gc_count += 1
	if seq[7] == "C" or seq[7] == "G": gc_count += 1
	if seq[8] == "C" or seq[8] == "G": gc_count += 1
	if seq[9] == "C" or seq[9] == "G": gc_count += 1
	if seq[10] == "C" or seq[10] == "G": gc_count += 1
	print(f'{j} {seq[0:10]} {gc_count/11:.4f}')
	gc_count = 0
	seq = seq[1:]+seq[0]
#pro: easier to read and troubleshoot because everything is right in front
#con: more lines of code to go through
#con: longer operation time because of these calculations
"""
python3 gc_win2.py
0 ACGACGCAGGA 0.6364
1 CGACGCAGGAG 0.7273
2 GACGCAGGAGG 0.7273
3 ACGCAGGAGGA 0.6364
4 CGCAGGAGGAG 0.7273
5 GCAGGAGGAGA 0.6364
6 CAGGAGGAGAG 0.6364
7 AGGAGGAGAGT 0.5455
8 GGAGGAGAGTT 0.5455
9 GAGGAGAGTTT 0.4545
10 AGGAGAGTTTC 0.4545
11 GGAGAGTTTCA 0.4545
12 GAGAGTTTCAG 0.4545
13 AGAGTTTCAGA 0.3636
14 GAGTTTCAGAG 0.4545
15 AGTTTCAGAGA 0.3636
16 GTTTCAGAGAT 0.3636
17 TTTCAGAGATC 0.3636
18 TTCAGAGATCA 0.3636
19 TCAGAGATCAC 0.4545
20 CAGAGATCACG 0.5455
21 AGAGATCACGA 0.4545
22 GAGATCACGAA 0.4545
23 AGATCACGAAT 0.3636
24 GATCACGAATA 0.3636
25 ATCACGAATAC 0.3636
26 TCACGAATACA 0.3636
27 CACGAATACAT 0.3636
28 ACGAATACATC 0.3636
29 CGAATACATCC 0.4545
30 GAATACATCCA 0.3636
31 AATACATCCAT 0.2727
32 ATACATCCATA 0.2727
33 TACATCCATAT 0.2727
34 ACATCCATATT 0.2727
35 CATCCATATTA 0.2727
36 ATCCATATTAC 0.2727
37 TCCATATTACC 0.3636
38 CCATATTACCC 0.4545
39 CATATTACCCA 0.3636
40 ATATTACCCAG 0.3636
41 TATTACCCAGA 0.3636
42 ATTACCCAGAG 0.4545
43 TTACCCAGAGA 0.4545
44 TACCCAGAGAG 0.5455
45 ACCCAGAGAGA 0.5455
46 CCCAGAGAGAG 0.6364
"""
