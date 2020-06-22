from mpi4py import MPI
import numpy as np

comm = MPI.COMM_WORLD
size = comm.Get_size()
rank = comm.Get_rank()

n = 3
recvdata = np.zeros(n,dtype=np.int)
senddata = (rank+1)*np.arange(size*n,dtype=np.int)
print("rank %d senddata : " % (rank),senddata)
comm.Reduce_scatter_block(senddata,recvdata,op=MPI.SUM)
print("rank %d recvdata : " % (rank),recvdata)