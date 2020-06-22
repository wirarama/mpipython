from mpi4py import MPI

comm = MPI.COMM_WORLD
rank = comm.Get_rank()

data0 = None
data1 = None
if rank == 0:
    data0 = 45
elif rank == 1:
    data1 = 17
data0 = comm.bcast(data0,0)
data1 = comm.bcast(data1,1)
if rank%2==0:
    print("rank %d data : " % (rank),data0)
else:
    print("rank %d data : " % (rank),data1)