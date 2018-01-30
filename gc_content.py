#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 13 17:43:06 2016

@author: James
"""
"""This program computes the GC content of a DNA sequence"""
#get DNA sequence:
dna_sequence='atgagatgatgacctcgccgtagcctcggtac'
no_c=dna_sequence.count('c')

#count number of G's in DNA sequence

no_g=dna_sequence.count('g')

#determine length of DNA seq.

dna_length=len(dna_sequence)

#compute GC%

gc_percent=(no_c+no_g)*100/dna_length

#print GC%
print("The DNA sequence's GC content is",gc_percent,"%")
