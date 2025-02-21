# popgen_python

This is a suite of program to perform basic task on fasta sequences. Program are written in python3.

This include :

- heterozygosity.py : compute heterozygosity from a fasta file with two sequences corresponding to the two chromosomes.

- cleanAlignment.py : exclude site with missing data "N" from a alignment 


*Author:* Benoit Nabholz

--------
## heterozygosity.py

###  Usage:

`heterozygosity.py -f fasta_seq.fasta -w window_size`

- f : name of the fasta file
- w : size of the window in base pair

### Output
- name : name window
- Position : Position in the alignment
- Ts : Number of transition
- Ts/Tv : ratio of transition over transversion in the window
- S :  number of SNP
- Num_site:  number of site in the window that are not "-" or "N"
- Het : Heterozygosity = S / N_site

--------
## cleanAlignment.py

###  Usage:

`cleanAlignment.py fasta_seq.fasta`

--------
## seqStats.py

###  Usage:

`seqStats.py fasta_seq.fasta`

Read fasta sequences and return statistics.

### Output
- GC content
- gap_data : number of '-'
- N_sites : numder of 'N'
- tot_missing : sum of gap_data + N_sites
