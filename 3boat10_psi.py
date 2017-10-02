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

def calc_Psi(freq, total):
        psi=0
        for letter,count in freq.items():
                m=count/total
                psi= (psi + (m*m))
        return psi

in_file = getInput()
print ("\n")
freq = frequency(in_file)
total = totalCharacters(in_file)
psi = calc_Psi(freq, total)
print 'Psi Value: ', psi
print ("\n")

