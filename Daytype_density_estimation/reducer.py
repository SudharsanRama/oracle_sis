#!/usr/bin/python
import sys
import collections 
 
user=0
a=0
b=0
c=0
for line in sys.stdin:
	data = line.strip()
 	if(data=='"A"'):
		a+=1
	elif(data=='"B"'):
		b+=1
	else:
		c+=1
	user +=1

print "% of users hiring on a day of type A:{0:.2%}".format(float(a)/float(user))
print "% of users hiring on a day of type B:{0:.2%}".format(float(b)/float(user))
print "% of users hiring on a day of type C:{0:.2%}".format(float(c)/float(user))
