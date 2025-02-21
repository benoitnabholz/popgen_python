#! /usr/bin/env python
# read fasta sequences and return statistiques

import sys

f = open(sys.argv[1])


def read_fasta(fp):
    name, seq = None, []
    for line in fp:
        line = line.rstrip()
        if line.startswith(">"):
            if name: yield (name, ''.join(seq))
            name, seq = line, []
        else:
            seq.append(line)
    if name: yield (name, ''.join(seq))
    
nameFile = str(sys.argv[1])

print("File\tname\tsize\tGC\tgap_data\tN_sites\ttot_missing")

GC=0
gap_data=0
N_sites=0
tot_missing=0
with f as fp:
    for name, seq in read_fasta(fp):
        seq = seq.upper()
        nseq = seq.replace("-","")
        mseq = seq.replace("N","")
        mseq = mseq.replace("?","")
        nomissing_seq = nseq.replace("N", "")
        nomissing_seq = nomissing_seq.replace("?", "")
        if len(nomissing_seq) > 0:
            GC = (nseq.count('G') + nseq.count('C')) / float(len(nomissing_seq))
            gap_data = 1.0- ( float(len(nseq)) /float(len(seq)))
            N_sites = 1.0- ( float(len(mseq)) /float(len(seq)))
            tot_missing = gap_data+N_sites
        else:
            GC = "NA"
            gap_data = 1.0
            N_sites = 1.0
            tot_missing = 1.0 
        name=name.lstrip(">")
        print(nameFile+"\t"+name+"\t"+ str(len(seq)) + "\t" + str(GC) + "\t" + str(gap_data) + "\t" + str(N_sites) + "\t" + str(tot_missing))
		
