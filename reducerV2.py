#! /usr/bin/env python

import sys
count = 0
for line in sys.stdin:
	count+=1
	print line.strip()
	if count >= 20:
		break