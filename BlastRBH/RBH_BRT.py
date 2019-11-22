#!/usr/bin/env python3

#this script takes two lists of Blast hits (A vs. B and B vs. A) sorted by best hits and writes a new text file of each reciprocal blast hit. 

Usage = 'Please provide: Blast_Results_1 Blast_Results_2 RBH_name_out, be sure Blast hits are sorted best hit -> worst hit'

import sys
import re

if len(sys.argv) < 3:
	print(Usage)
 
debug = 2

blast1 = sys.argv[1]
blast2 = sys.argv[2]
outfile = sys.argv[3]

#parse first BLAST results
blasto1 = open(blast1, 'r')
blastdict1 = {} #dictionary for BLAST file ONE
for Line in blasto1:
	if ( Line[0] != '#' ):
		Line.strip()
		Elements = re.split('\t', Line)
		queryId = Elements[0]
		subjectId = Elements[1]
		if ( not ( queryId in blastdict1.keys() ) ):
			blastdict1[queryId] = subjectId  #pick the first hit

if (debug): blastdict1.keys() 

#parse second BLAST results
blasto2 = open(blast2, 'r')
blastdict2 = {}
for Line in blasto2:
	if ( Line[0] != '#' ):
		Line.strip()
		Elements = re.split('\t', Line)
		queryId = Elements[0]
		subjectId = Elements[1]
		if ( not ( queryId in blastdict2.keys() ) ):
			blastdict2[queryId] = subjectId  #pick the first hit

if (debug): blastdict2.keys() 

#Identifying shared pairs

RBhits={}
for id1 in blastdict1.keys():
	value1 = blastdict1[id1]
	if ( value1 in blastdict2.keys() ):
		if ( id1 == blastdict2[value1] ) : #if true, it is a reciprocal pair
			RBhits[value1] = id1

if (debug): RBhits 


outfl = open( outfile, 'w')

for hits in RBhits.keys():
	line = hits + '\t' + RBhits[hits] + '\n'
	outfl.write(line) #writed reciprocal hits to output RBH file
	
outfl.close()

print("Done. RBH from", sys.argv[1], "and", sys.argv[2], "are in", sys.argv[3])
