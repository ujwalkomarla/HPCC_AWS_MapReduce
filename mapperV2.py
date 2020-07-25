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

class TopN(object):
	def __init__(self,N):
		self.entry = {};
		self.size = N
	def insert(self,title,votes):
		self.entry[title] = int(votes)
		while len(self.entry) > self.size:
			self.entry.pop(min(self.entry, key=self.entry.get))
	def printItems(self):
		for title,votes in self.entry.items():
			print "%s\t%s" %(str(votes),title)
			
def read_input(file):
	for line in file:
		yield line.strip()
		
top20 = TopN(20)
data = read_input(sys.stdin)
for line in data:
	match = pattern.search(line)
	if match and float(match.group(6)) == 1:
		top20.insert(match.group(2), match.group(7))
#		print "%s\t%s" %(match.group(7),match.group(2))
top20.printItems()