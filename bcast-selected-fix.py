from mpi4py import MPI
from math import ceil

comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()

data0 = None
data1 = None
data2 = None
if rank == 0:
    data0 = 45
elif rank == 1:
    data1 = 8
elif rank == 2:
    data2 = 17

n = int(ceil(size/3))
out = []
#size = 32
for x in range(0,size,n):
    if (x+n) < size:
        out.append([i for i in range(x,x+n)])
    else:
        out.append([i for i in range(x,size)])
if rank==0:
    print(n,out)
data0 = comm.bcast(data0,root=0)
data1 = comm.bcast(data1,root=1)
data2 = comm.bcast(data2,root=2)
if rank in out[0]:
    print("rank %d data : " % (rank),data0)
elif rank in out[1]:
    print("rank %d data : " % (rank),data1)
else:
    print("rank %d data : " % (rank),data2)