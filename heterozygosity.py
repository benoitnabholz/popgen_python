#! /usr/bin/env python

import sys
import optparse


def read_fasta(fp):
    name, seq = None, []
    for line in fp:
        line = line.strip()
        if line.startswith(">"):
            if name is not None:
                yield name, ''.join(seq)
            name, seq = line[1:], []
        elif line:
            seq.append(line)
    if name is not None:
        yield name, ''.join(seq)


def is_transition(a, b):
    return (a, b) in (("A", "G"), ("G", "A"),
                      ("C", "T"), ("T", "C"))


parser = optparse.OptionParser()
parser.add_option('-f', '--fasta_file', dest='fastaIn', type='string')
parser.add_option('-w', '--window_size', dest='windSize', type='int')

(options, args) = parser.parse_args()

if not options.fastaIn or not options.windSize or options.windSize <= 0:
    parser.error("Please provide a FASTA file and a positive window size")

# Read FASTA
with open(options.fastaIn) as fp:
    sequences = list(read_fasta(fp))

if len(sequences) != 2:
    sys.exit("ERROR: FASTA must contain exactly two sequences")

name1, seq1 = sequences[0]
name2, seq2 = sequences[1]

seq1 = seq1.upper()
seq2 = seq2.upper()

if len(seq1) != len(seq2):
    sys.exit("ERROR: sequences have different lengths")

window_size = options.windSize

print("Name\tStart\tEnd\tTs\tTs/Tv\tHet\tCallable_sites\tHeterozygosity")

# Process windows
for start in range(0, len(seq1), window_size):

    end = min(start + window_size, len(seq1))

    num_het = 0
    num_ts = 0
    num_callable = 0

    for i in range(start, end):

        a = seq1[i]
        b = seq2[i]

        # Only A, C, G and T are considered callable, excluding N, - and ambiguious sites
        if a not in "ACGT" or b not in "ACGT":
            continue

        num_callable += 1

        if a != b:
            num_het += 1

            if is_transition(a, b):
                num_ts += 1

    num_tv = num_het - num_ts

    # Ts/Tv
    ts_tv = num_ts / num_tv if num_tv > 0 else "NA"

    # Heterozygosity
    het = num_het / num_callable if num_callable > 0 else "NA"

    print(f"{options.fastaIn}\t{start+1}\t{end}\t"
          f"{num_ts}\t{ts_tv}\t{num_het}\t"
          f"{num_callable}\t{het}")


