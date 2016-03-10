#!/usr/bin/python
import sys
import collections 


arr = [] 
count = 0
user=0
for line in sys.stdin:
	data = line.strip()
 	arr.append(data);
	user +=1
	

for i in arr:
	arr.sort()
	i=collections.Counter(arr).most_common(10)	
print "Total Number of Type-A Users :",user
print "Top-Rated Users,who Uses our Service often via Phone :",i


	
