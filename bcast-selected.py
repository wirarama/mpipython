from mpi4py import MPI
from math import ceil

comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()

if rank == 0:
    data = 45
elif rank == 1:
    data = 8
elif rank == 2:
    data = 17
else:
    data = None

n = int(ceil(size/3))
out = []
for x in range(0,size,n):
    if (x+n) < size:
        out.append([i for i in range(x,x+n)])
    else:
        out.append([i for i in range(x,size)])

if rank in out[0]:
    data = comm.bcast(data,root=0)
elif rank in out[1]:
    data = comm.bcast(data,root=1)
else:
    data = comm.bcast(data,root=2)
print("rank %d data : " % (rank),data, flush=True)
