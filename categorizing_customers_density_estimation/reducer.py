#!/usr/bin/python
import sys


count_a = 0;
count_b	= 0;
count_c = 0;
count = 0;


for line in sys.stdin:
	count += 1
	data = line.strip()
	if(data[1] == 'A'):
		count_a += 1
	elif(data[1] == 'B'):
		count_b += 1
	else: 
		count_c += 1			 
		

print "Total count={0}".format(count)
print "% of trip was dispatched from the central:{0:.2f}%".format(float(count_a)/float(count)*100) 
print "% of trip was demanded directly to a taxi driver at a specific stand:{0:.2f}%".format(float(count_b)/float(count)*100) 
print "% of trip demanded on random street:{0:.2f}%".format(float(count_c)/float(count)*100) 
