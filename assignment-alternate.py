#This is 2 line solution for assignment1
import re
print sum( [ int(i) for i in re.findall('[0-9]+',open('regex_sum_42.txt').read()) ] )
# print re.findall('[0-9]+',open('regex_sum_42.txt').read())
