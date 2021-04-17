#!/usr/bin/env python3

# Write a program that computes the GC% of a DNA sequence
# Format the output for 2 decimal places
# Use all three formatting methods

dna = 'ACAGAGCCAGCAGATATACAGCAGATACTAT'
gc_content = 0 # feel free to change
for i in range(len(dna)):
	if dna[i] == "G" or dna[i] == "C":
		gc_content += 1
gc_percent = gc_content/len(dna)
print('%.2f' % (gc_percent))
print('{:.2f}'.format(gc_percent))
print(f'{gc_percent:.2f}')

"""
python3 gc.py
0.42
0.42
0.42
"""
