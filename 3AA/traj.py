"""
Any given evolutionary trajectory is given by an order list of coordinates
In this case the coordinates correspond to amino acid sequences.
"""

import random
import matplotlib.pyplot as plt
import numpy as np 

def gen_traj(initial,iterations=10):
    """
    Takes initial sequence in numeric form (1,1,1) and stochastically evolves it.
    """
    seqs = [list(initial)]
    for i in range(iterations):
        seqs.append( mutate(seqs[-1])) # Mutates most recent sequence
    return seqs 

def mutate(seq,*args,num_AAs=20,concurrent_mutations=3):
    """
    Assumes that you're only using the 20 canonical amino acids

    concurrent_mutations : int 
        
        Enables multiple positions to be mutated simultaneously
    
    num_AAs              : int
        
        Lists total number of amino acid possibilities
    """
    seq2 = seq.copy() # If this step is removed then it runs into a mutable default error where you have copies of the same sequence list
    many_muts = random.randint(1,concurrent_mutations) # Determines how many mutations will be made randomly (n.b will always make one)
    for pos in random.sample(range(len(seq2)),many_muts):
        seq2[pos] = random.randint(1,num_AAs)
    return seq2 


if __name__ == "__main__":
    test_seq = (1,2,3)
    print(mutate(list(test_seq)))
    #print(test_seq)
    #print(gen_traj(test_seq))

