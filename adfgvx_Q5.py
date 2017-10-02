from __future__ import division
from sys import argv

def getInput(filename):
        with open(filename,"r") as file:
                data = file.read()
                file.close()
                return data

def kappa(file1, file2):
        count = 0.0
        combinedFile = zip(file1, file2)
        for a, b in combinedFile:
                if a == b:
                        count += 1.0;
        length = len(combinedFile)                
        return count/length

def getPairs(in_file):
       import re
       num = re.findall('..?',in_file)
       return num

def countPairs(listPairs):
        count = 0
        pairDict = {}
        pairDict = dict((x,listPairs.count(x)) for x in set(listPairs))
        return pairDict

def replace(file1):
        file1 = [w.replace("fa","A") for w in file1]
        file1 = [w.replace("xa","1") for w in file1]
        file1 = [w.replace("ga","K") for w in file1]
        file1 = [w.replace("aa","C") for w in file1]
        file1 = [w.replace("fg","E") for w in file1]
        file1 = [w.replace("gg","I") for w in file1]
        file1 = [w.replace("va","8") for w in file1]
        file1 = [w.replace("ag","P") for w in file1]
        file1 = [w.replace("xg","H") for w in file1]
        file1 = [w.replace("xv","N") for w in file1]
        file1 = [w.replace("gv","Z") for w in file1]
        file1 = [w.replace("da","D") for w in file1]
        file1 = [w.replace("fv","S") for w in file1]
        file1 = [w.replace("gf","F") for w in file1]
        file1 = [w.replace("fd","T") for w in file1]
        file1 = [w.replace("gd","W") for w in file1]
        file1 = [w.replace("ff","5") for w in file1]
        file1 = [w.replace("xf","M") for w in file1]
        file1 = [w.replace("ad","V") for w in file1]
        file1 = [w.replace("xd","7") for w in file1]
        file1 = [w.replace("av","2") for w in file1]
        file1 = [w.replace("vg","O") for w in file1]
        file1 = [w.replace("dv","3") for w in file1]
        file1 = [w.replace("dg","4") for w in file1]
        file1 = [w.replace("vv","0") for w in file1]
        file1 = [w.replace("vx","X") for w in file1]
        file1 = [w.replace("fx","Y") for w in file1]
        file1 = [w.replace("vd","G") for w in file1]
        file1 = [w.replace("vf","6") for w in file1]
        file1 = [w.replace("af","L") for w in file1]
        file1 = [w.replace("dd","B") for w in file1]
        file1 = [w.replace("gx","9") for w in file1]
        file1 = [w.replace("ax","Q") for w in file1]
        file1 = [w.replace("df","J") for w in file1]
        file1 = [w.replace("dx","R") for w in file1]
        file1 = [w.replace("xx","U") for w in file1]        
        textFile = ''.join(file1)
        return textFile


file1 = getInput("permuted5.txt")
file2 = getInput("alice_in_wonderland.txt")
pairsList = getPairs(file1)
file2 = ''.join(e for e in file2 if e.isalnum())
file2 = file2.upper()   
text = replace(pairsList)
print ("\n")
print (text)
print ("\n")
print (kappa(text,file2))
print ("\n")

