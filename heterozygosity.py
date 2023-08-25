#! /usr/bin/env python

import sys
import optparse

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

def isTransition(s1, s2):
	if (s1 == "A" and s2 == "G") or (s1 == "G" and s2 == "A"):
		return(1)
	if (s1 == "C" and s2 == "T") or (s1 == "T" and s2 == "C"):
		return(1)

parser = optparse.OptionParser()

parser.add_option('-f', '--fasta_file',action="store", dest="fastaIn", type="string")
parser.add_option('-w', '--window_size',action="store", dest="windSize", type="int")

(options, args) = parser.parse_args()
namefile = options.fastaIn
wind_Size = options.windSize

fp = open(namefile)

seq1 = ""
seq2 = ""

count = 0
for name, seq in read_fasta(fp):
	if count == 0:
		seq1 = seq.upper()
		count = count + 1
	else:
		seq2 = seq.upper()


Num_Het = 0
Num_N = 0
Num_good_site = 0
Num_site = 0
Num_transition = 0
count_window = 0
print("name\tPosition\tTs\tTs/Tv\tS\tNum_site\tHet")

for i in range(0, len(seq1)):

	Num_site = Num_site + 1
	count_window = count_window + 1
	
	if count_window >= wind_Size:
		
		if Num_transition == 0 or Num_Het == 0 or Num_Het == Num_transition:
			print(namefile+"\t"+str(Num_site)+"\t"+str(Num_transition)+"\tNA\t"+str(Num_Het)+"\t"+str(Num_good_site)+"\tNA")
		else:
			print(namefile+"\t"+str(Num_site)+"\t"+str(Num_transition)+"\t"+str(float(Num_transition)/float(Num_Het-Num_transition))+"\t"+str(Num_Het)+"\t"+str(Num_good_site)+"\t"+str(float(Num_Het)/float(Num_good_site)))
		count_window = 0
		Num_Het = 0
		Num_N = 0
		Num_good_site = 0
		Num_transition = 0


	if seq1[i] == "N" or seq1[i] == "-" or seq2[i] == "N" or seq2[i] == "-":
		Num_N = Num_N + 1
		continue
	
	Num_good_site = Num_good_site + 1
	if seq1[i] != seq2[i]:
		Num_Het = Num_Het + 1
		if isTransition(seq1[i] , seq2[i]):
			Num_transition = Num_transition + 1

if Num_transition == 0 or Num_Het == 0 or Num_Het == Num_transition:
	print(namefile+"\t"+str(Num_site)+"\t"+str(Num_transition)+"\tNA\t"+str(Num_Het)+"\t"+str(Num_good_site)+"\tNA")
else:
	print(namefile+"\t"+str(Num_site)+"\t"+str(Num_transition)+"\t"+str(float(Num_transition)/float(Num_Het-Num_transition))+"\t"+str(Num_Het)+"\t"+str(Num_good_site)+"\t"+str(float(Num_Het)/float(Num_good_site)))

fp.close()

