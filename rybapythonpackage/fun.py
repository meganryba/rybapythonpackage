import pandas as pd
from Bio.Blast import NCBIXML
import os

def fun(switch):

    print ("Reverse is",switch[::-1])
    
    """ this function will print the reverse of whatever you type in quotation marks because I needed something fun to do because nothing else will work for me """ 
    
def parse(filepath):
    """ this is my real function. It uses the BLAST results and parses them to tell you what organism matches it the closest. This result using the data file from the previous BLAST search should return the first result as Plethodon kentucki voucher specimen with the cytb gene."""
    assert os.path.exists(filepath)

    parsed = NCBIXML.read(open(filepath))
    alignment_set = parsed.alignments
    for individual_alignment in alignment_set:
        print(individual_alignment)
    
    
   