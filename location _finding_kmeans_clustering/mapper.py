#!/usr/bin/python
import sys
for line in sys.stdin:
	data = line.strip().split(",")
	value = data[8]+data[9]
	value = value.replace("[","")
	value = value.replace("]","")
	
	print value[1:] 	 
		
