import dendropy
import os

def sequence_cleanup(sequence_set, out_file, taxon, gene): 
    #pre: do files include taxon and gene
    #check what type the data is (object, float, int)
    assert sequence_set[taxon]
    my_taxon_sequence = sequence_set[taxon].symbols_as_string()
    my_taxon_sequence[int(gene[0]) : int(gene[1])]
    ofile = open(out_file, "w")
    ofile.write(">" + taxon + "\n" + my_taxon_sequence + "\n")
    ofile.close()
   
    assert os.stat(out_file).st_size != 0 
    #post: check to make sure the files are not empty after they are saved. 
    #make sure the file was saved in the right place