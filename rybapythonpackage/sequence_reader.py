import dendropy
import os.path

def sequence_reader("../data/full_plethodon_alignment.phy"):
    assert os.path.exists("../data/full_plethodon_alignment.phy")
    sequence_set = dendropy.DnaCharacterMatrix.get(
        path="../data/full_plethodon_alignment.phy",
        schema="phylip"
)
    assert type(sequence_set) == dendropy.datamodel.charmatrixmodel.DnaCharacterMatrix
    return(sequence_set)

    #Pre:  check that the file exists or that its in the right format
    #post: check that the returned type is correct - should be dna character matrix