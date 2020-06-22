from mpi4py import MPI
from time import sleep

comm = MPI.COMM_WORLD
rank = comm.Get_rank()

if rank == 0:
    data = 45
elif rank == 1:
    data = 17
else:
    data = None
    
if rank%2==0:
    data = comm.bcast(data,0)
    sleep(10)
else:
    data = comm.bcast(data,1)
    sleep(10)
print("rank %d data : " % (rank),data)
