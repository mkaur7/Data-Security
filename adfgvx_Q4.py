from __future__ import division
from sys import argv

def getInput():
	with open("permuted5.txt","r") as file:
		data= file.read()
		file.close()
		return data

def getPairs(in_file):
       import re
       num = re.findall('..?',in_file)
       return num

def countPairs(listPairs):
        count = 0
        pairDict={}
        pairDict= dict((x,listPairs.count(x)) for x in set(listPairs))
        return pairDict

def calc_Psi(freq, total):
        psi = 0
        for letter, count in freq.items():
                m = count/total
                psi = (psi + (m*m))
        return psi

in_file = getInput()
count=0
listPairs = getPairs(in_file)
freqPairs = countPairs(listPairs)
print (freqPairs)

totalPairs = len(in_file)/2
psi = calc_Psi(freqPairs, totalPairs)
print ('\n')
print 'Psi Value: ', psi
print ('\n')
