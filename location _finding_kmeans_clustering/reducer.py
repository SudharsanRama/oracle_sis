#!/usr/bin/python
import sys
from math import sqrt

cluster = {}

cluster_size = int(file("value.txt").read())
for i in range(cluster_size):
	cluster[i] = []
geo_values = []
for line in sys.stdin:
	data = line.strip().replace("\"","").split(" ")
	geo_values.append(data)
previous_cluster = cluster
flag = True
centroid = geo_values[:cluster_size]
while flag:
	for i in range(len(geo_values)):
		diff = sys.float_info.max
		cluster_no = 0
		for j in range(len(centroid)):
			dis = sqrt(pow((float(centroid[j][0])-float(geo_values[i][0])),2)+pow((float(centroid[j][1])-float(geo_values[i][1])),2))
			if(diff>dis):
				diff = dis
				cluster_no = j	
		cluster[cluster_no].append(geo_values[i])
	for i in range(len(centroid)):
		val = cluster[i]
		x = 0
		y = 0
		for j in range(len(val)):
			x += float(val[j][0])
			y += float(val[j][1])
		
		centroid[i][0] = x/float(len(val))	
		centroid[i][1] = y/float(len(val))
	if(previous_cluster == cluster):
		flag = False
	else:
		previous_cluster = cluster
	break
print "The taxi stations can be located in the following locations"
for i in range(len(centroid)):
	print "Taxi station must be created at {0} and must have {1:.2f}% of taxi count".format(centroid[i],float(len(cluster[i]))/float(len(geo_values))*100)
'''for i in range(len(centroid)):
	for j in range(len(centroid)):
		dis = sqrt(pow((float(centroid[i][0])-float(centroid[j][0])),2)+pow((float(centroid[i][1])-float(centroid[j][1])),2))
		print dis,
			
	print "\n"'''
