#!/usr/bin/env python3

# You are probably well aware of the 'birthday paradox'
# https://en.wikipedia.org/wiki/Birthday_problem
# Let's try simulating it

# You will need a list for the 365 day calendar
# You will need a set number of people (e.g. 25)
# During each 'trial' you do the following
#	Choose a person
#	Git them a random birthday
#	Store it in the calendar
# Once you have stored all birthdays, check to see if any have the same day
# Do this for many trials to see what the probability of sharing a birthday is

import random
ppl = 25
days = 365
trials = 10000
duplicates = 0
for i in range(trials):
	calendar = [] #creating empty calendar
	calendar = [0 for j in range(days)] #creating filled calendar
	for k in range(ppl): #creating random calender
		birthday = random.randint(0, days-1)
		calendar[birthday] += 1
	for day in calendar: #counting duplicate birthdays
		if day > 1: 
			duplicates += 1
			break #only need to count 1 duplicate per calendar
print(duplicates, trials, duplicates/trials)
"""
repeat over amount of trials
	create empty calender
	fill calender with random birthdays (random function)
	check for duplicates (within a loop)
	record
print(duplicates/trials)
"""

"""
python3 birthday.py
0.571
"""

