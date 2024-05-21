#!/usr/bin/env python3

import sys
from Bio import SeqIO

####
# Mutations file must be tab-delimited with the following columns: position, gene name, alternate allele.
# This script pulls 50bp in either direction of a given position (also introducing an alternate allele)
# for use with blast or a COBS search.
####

if len(sys.argv) != 3:
    print("Usage: cobsSeqPull.py <mutations.txt> <ref.fasta>")
    sys.exit(0)

# read mutations into a dictionary
muts = {}
with open(sys.argv[1],"r") as f:
    next(f)
    for line in f:
        info = line.strip().split("\t")
        muts[info[0]] = [info[1],info[2]]

# read reference file, grab sequence for each mutation, write to output file
outseq = []
for seq in SeqIO.parse(sys.argv[2],"fasta"):
    with open("cobsSeq.fasta","w") as out:
        for pos,info in muts.items():
            name = info[0]+"_"+pos+"_"+info[1]
            s = list(str(seq.seq[int(pos)-51:int(pos)+50]))
            s[50] = info[1]
            out.write(">"+name+"\n")
            out.write("".join(s)+"\n")
