import re
string  = 'From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008'
answer = 'uct.ac.za'
listRe = ['@(\S+)','F.+:','..@\S+..','@\S+']
for x,val in enumerate(listRe):
	if re.findall(val,string)[0]==answer:
		print 'correct Answer is: ',str(x+1)
