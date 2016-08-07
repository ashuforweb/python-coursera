#Assignment1 push
import re
fopen = open("regex_sum_307201.txt") #just change the file name to test this
reString = '[0-9]+'
numList = []
for line in fopen:
	numList = numList+re.findall(reString,line)
def listSum(a):
	fin = 0
	for x in range(0,len(a)):
		fin = fin+int(a[x])
	return fin
print listSum(numList)
