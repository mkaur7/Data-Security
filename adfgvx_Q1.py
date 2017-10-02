from __future__ import division
from sys import argv

def getInput():
	print ("\n")
	inputFile = raw_input("Enter Input File: ")
	with open(inputFile, "r") as file:
		data = file.read()
		file.close()
		return data

def totalCharacters(in_file):
	char = 0
	for line in in_file:
		char += len(line)
	total = char
	return (total)

def refineData(in_file):
	newData = ''.join(e for e in in_file if e.isalnum())
	return newData

def frequency(in_file):
	countFreq = {}	
	freq = {}
	for line in in_file:
		for char in line:
			if char in freq:
				freq[char] = freq[char] + 1
			else:
				freq[char] = 1
	return freq

def getPairs(in_file):
	import re
	num = re.findall('..?',in_file)
	return num

def calc_Phi(freq,total):
	phi = 0
	for letter,count in freq.items():
		m = (count / total)
		phi = phi + m*(m-(1/26))
	return phi

def calc_Phi_Pairs(freq,total):
	phi = 0
	for letter,count in freq.items():
		m = (count / total)
		phi = phi + m*(m-(1/(26*25)))
	return phi

def countPairs(listPairs):
	count = 0
	pairDict = {}
	pairDict = dict((x,listPairs.count(x)) for x in set(listPairs))
	return pairDict

in_file = getInput()
print ("\n")
print (in_file)
newData = refineData(in_file)
newData = newData.lower()

#Single Letters
freq = frequency(newData)
total = totalCharacters(newData)
phi = calc_Phi(freq,total)
print 'Phi value for single letters: ', phi

#Pairs
listPairs = getPairs(newData)
freqPairs = countPairs(listPairs)
totalPairs = len(freqPairs)
phi = calc_Phi_Pairs(freqPairs, totalPairs)
print 'Phi value for pairs of letters: ', phi
print ("\n")
