#! /usr/bin/env python

import sys
count = 0
mydict = {}
for line in sys.stdin:
	
	line = line.strip()
	title, votes = line.split("\t")
	if count < 20:
		mydict[title] = int(votes)
		#print("\t".join(str(v) for v in result))
	else:
		min_value_title = min(mydict,key=mydict.get)
		min_val = mydict[min_value_title]
		#check if the min value is less than the present iteration votes
		# if yes, continue
		
		#else replace the min value with the present iter entry
		if min_val < int(votes):
			del mydict[min_value_title]
			#add this entry to the dictionry
			mydict[title] = int(votes)
		else: 
			continue
	count += 1

for k,v in mydict.items():
		print "%s\t%s"%(k,v)

