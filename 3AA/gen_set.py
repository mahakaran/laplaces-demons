import numpy as np 
import itertools 

AAs = 'ACDEFGHIKLMNPQRSTVWY'
nums = np.arange(1,21,1)

mapping = {x[0] : x[1] for x in zip(AAs,nums)}

def AA_map(seq):
    """
    Uses provided mapping dictionary to generate 3D coords for a given amino acid sequence
    """
    return tuple([mapping[x] for x in seq])

def gen_set():
    """
    Generates the full 8000 amino acid set along with their coordinates determined by the 
    mapping provided above.
    """
    AA_set = [a for a in itertools.product(AAs,repeat=3)]
    coords = list(map(AA_map,AA_set))
    return AA_set, coords

if __name__ == "__main__":
    AA_set, coords = gen_set()
    print(AA_set[:10],coords[:10]) 
