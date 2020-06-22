from mpi4py import MPI
import numpy as np

comm = MPI.COMM_WORLD
size = comm.Get_size()
rank = comm.Get_rank()

data = None
if rank == 0:
    src = np.arange(100)
    data = np.array_split(src,size)

data = comm.scatter(data, root=0)
print("rank %d data : " % (rank),data)