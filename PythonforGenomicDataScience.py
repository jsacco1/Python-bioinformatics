#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 13 17:06:47 2016

@author: James
"""

#!/usr/bin/python

"""dnautil module contains a few useful functions for dna sequence"""
'dnautil module contains a few useful functions for dna sequence'

def gc(dna):"this function computes the GC percentage of a dna sequence"
   ...:     nbases=dna.count('n')+dna.count('N')
   ...:     gcpercent=float(dna.count('c')+dna.count('C')+dna.count('g')+dna.count('G'))*100.0/(len(dna)-nbases)
   ...:     return gcpercent
   ...: 

def has_stop_codon(dna,frame) :
   ...:     #This function checks if a given DNA sequence has in frame stop codons."
   ...:     stop_codon_found=False
   ...:     stop_codons=['tga', 'tag', 'taa']
   ...:     for i in range(frame,len(dna),3) :
   ...:         codon=dna[i:i+3].lower()
   ...:         if codon in stop_codons :
   ...:             stop_codon_found=True
   ...:             break
   ...:     return stop_codon_found
   ...: 

def reversecomplement(seq):
   ...:     """Return the reverse complement of the dna string."""
   ...:     seq=reverse_string(seq)
   ...:     seq=complement(seq)
   ...:     return seq
