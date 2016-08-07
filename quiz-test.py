import re
tstring = "From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008"
reg = '\S+?@\S+'
print re.findall(reg,tstring)
