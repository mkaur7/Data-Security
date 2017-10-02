def getInput():
	with open("ceaser2.txt","r") as file:
		textFile = file.read()
		file.close()
		return textFile

def getKey():
	key = 0
	while True:
		print "Enter any key between 1 and 26: "
		key = int(input())
		if (key >= 1 and key <= 26):
			return key

def encrypt(key, lowertext):
	cipher = ''
	for ch in lowertext:
		if ch.isalpha():
			asciiValue=ord(ch)
			asciiValue=asciiValue+key
			if asciiValue > ord('z'):
				asciiValue = asciiValue - 26
			cipher += chr(asciiValue)		    
		else:
			cipher += ch
	return cipher

def getSortedData(data):
	from string import ascii_lowercase
	text = data.strip()
	dictionary = {}
	for c in ascii_lowercase:
		dictionary[c] = text.count(c)

	import operator
	sorted_data = sorted(dictionary.items(),key = operator.itemgetter(1))

	return sorted_data

ciphertext = getInput()
key = getKey()
lowertext = ciphertext.lower()
sorted_list= getSortedData(lowertext)

largestElement = sorted_list[-1]
largestValue = largestElement[1]

for iteration in range(0,26):
	decryptedCipher = encrypt(key,lowertext)
	sorted_list= getSortedData(decryptedCipher)
	largestElement = sorted_list[-1]

	if (largestElement[0] == "e"):
		print ("\n")
		print 'Number of iterations performed: ', iteration
		print ("\n")
		print (decryptedCipher)
		break
	else:
		lowertext = decryptedCipher
