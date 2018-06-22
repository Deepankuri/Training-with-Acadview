#Question1
"""
-n enables us to read the file from the nth point,
working seems like a list, and prints line by line.
"""
def func(file,n):
	with open(file) as f1:
		for line in (f1.readlines() [-n]:):
			print(line /n)
p = 'testing1.txt'
q = int(input('enter last lines to read'))
func(p,q)
#Question2
"""
We use the wordcount dictionary which is pre defined amd stores
the words and their frequency ofoccureence in a given file.
"""
file = open("testing1.txt")
wordcount={}
for word in file.read():
	if word not in wordcount:
		wordcount[word]=1
    else:
    	wordcount[word]+=1
for key,value in wordcount.items():
	print("word and frequency are:")
    print(key, value)

#Question3
"""
We will create a blank file named testing 2 of text type.
We will import the os and coy testig 1 contents to testing 2 
through simple copy function.
"""
import os
os.system('copy testing1.txt testing2.txt')

#Question4
"""
Zip function in python combines the corresponding data i.e. 
here, the corresponding lines of the two files together.
The first line of testing1 will be combined with testing2, 
second with second, and so on.
"""
with open('testing1.txt','r') as f1, open('testing2.txt','r') as f2:
	for s,e in zip(l1,l2):
		print("{}{}".format(l1.rstrip(),l2.rstrip()))

#Question5
"""
We will generate a sequence of random numbers and write it
into testing1. Then we will sort this random sequence and then
store it in the testing2 file.
"""
import random
af = open('testing1.txt', 'w')
a = []
for i in range(10):
	a.append((random.randint(1,100)))
    s1 = str(a)
af.write(s1)
af.close()

af2 = open('test.txt','r')
while True:
	line = af2.readline()
	print(line)
	if not line:
		break
af2.close()

a.sort()
s2 = str(a)
bf = open('testing2.txt','w')
bf.write(s2)
bf.close()

bf2 = open('test2.txt','r')
while True:
	line = bf2.readline()
    print(line)
    if not line:
    	break
bf2.close()
