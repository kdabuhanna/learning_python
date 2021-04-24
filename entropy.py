#!/usr/bin/env python3

# Write a Shannon entropy calculator: H = -sum(pi * log(pi))
# The values should come from the command line
# E.g. python3 entropy.py 0.4 0.3 0.2 0.1
# Put the probabilities into a new list
# Don't forget to convert them to numbers
# sum = loop

import math
import sys

prob = []
for s in sys.argv[1:]:
	prob.append(float(s))

print(sum(prob))
assert(math.isclose(sum(prob), 1, abs_tol = 0.2) 

H = 0
for i in range(len(prob)):
	H -= prob[i] * math.log2(prob[i])
print(H)

"""
python3 entropy.py 0.1 0.2 0.3 0.4
1.846
"""
