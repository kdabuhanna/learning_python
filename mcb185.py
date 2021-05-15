import random

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


