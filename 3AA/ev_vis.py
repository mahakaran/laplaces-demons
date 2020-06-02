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
