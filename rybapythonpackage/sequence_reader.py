import dendropy
import os.path

def sequence_reader(filepath):
    assert os.path.exists(filepath)
    sequence_set = dendropy.DnaCharacterMatrix.get(
        path=filepath,
        schema="phylip"
)
    assert type(sequence_set) == dendropy.datamodel.charmatrixmodel.DnaCharacterMatrix
    return(sequence_set)

    #Pre:  check that the file exists or that its in the right format
    #post: check that the returned type is correct - should be dna character matrix