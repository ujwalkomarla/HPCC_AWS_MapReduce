#! /usr/bin/env python

import sys
import re
#count=0
pattern = re.compile(
	r'"(.+)","(.+)",(\d+),(\d+),(\w+),([0-9.]+),(\d+),'
	# number, title, year, length, budget, rating, votes
	r'([0-9.]+),([0-9.]+),([0-9.]+),([0-9.]+),([0-9.]+),([0-9.]+),([0-9.]+),([0-9.]+),([0-9.]+),([0-9.]+),'
	# Ratings[1-10]
	r'"(.*)",(\d),(\d),(\d),(\d),(\d),(\d),(\d)'
	# mpaa, Action, Anim, Comedy, Drama, Document, Romance, Short
)

for line in sys.stdin:
	line = line.strip()
	match = pattern.search(line)
	if match and float(match.group(6)) == 1:
		print "%s\t%s" %(match.group(2), match.group(7))