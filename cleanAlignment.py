#! /usr/bin/env python

import sys
import optparse
import Bio
from Bio import AlignIO

parser = optparse.OptionParser()

parser.add_option('-f', '--fasta_file', action="store", dest="fastaIn", type="string")

(options, args) = parser.parse_args()
namefile = options.fastaIn
fp = open(namefile)

align = AlignIO.read(namefile, "fasta")
outal = align[:,0:0]

for i in range(0, len(align[0])):
    if "N" not in align[:, i]:
        outal=outal+align[:, i:i+1]

for record in outal:
   print(">"+record.id)
   print(record.seq)




