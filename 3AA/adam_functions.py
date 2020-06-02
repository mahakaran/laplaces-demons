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

import matplotlib.pyplot as plt 
from mpl_toolkits.mplot3d import Axes3D
import mpl_toolkits.mplot3d.art3d as art3d

from gen_set import gen_set  
import traj

def plot_traj(ax,traj):
    xs, ys, zs = zip(*traj)
    ax.plot(xs,ys,zs)
    return None


if __name__ == "__main__":
    AA_set, coords = gen_set()
    x,y,z = zip(*coords)
    fig = plt.figure(figsize=(16,16))
    ax1 = fig.add_subplot(111,projection="3d")
    ax1.set_zlabel("Position 3")
    ax1.set_ylabel("Position 2")
    ax1.set_xlabel("Position 1")
    ax1.scatter(x,y,z,marker=".",color="k")
    
    import traj
    traject = traj.gen_traj((1,2,3),100)
    plot_traj(ax1,traject)
    plt.show()

