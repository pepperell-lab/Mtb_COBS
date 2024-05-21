#!/usr/bin/env python3

import sys
import cobs_index as cobs
from Bio import SeqIO

#####
#
#####

if len(sys.argv) != 3:
	print("Usage: cobs_search.py <cobs file> <query fasta>")
	sys.exit(0)

cobsFile = sys.argv[1]
fasta = sys.argv[2]

cobsData = cobs.Search(cobsFile)
seqDict = {}

for seq in SeqIO.parse(fasta,"fasta"):
	seqDict[seq.id] = seq.seq

for header,seq in seqDict.items():
	with open(header+"_cobsSearch.txt","w") as out:
		print(header, len(str(seq)))
		result = cobsData.search(str(seq),threshold=1)
		for x in result:
			x = x[1]
			out.write(str(x)+"\n")
