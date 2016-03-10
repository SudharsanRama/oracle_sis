#!/usr/bin/python
import sys
for line in sys.stdin:
	data = line.strip().split(",")
	if(data[2] != 'NA'):
		print data[2]
		 
		
