from mpi4py import MPI
comm = MPI.COMM_WORLD
rank = comm.Get_rank()

b = rank
if rank == 4:
    b = rank*8
c = comm.bcast(b,root=4)
b = comm.bcast(b,root=3)
if rank%2==0:
    print("rank %d data : " % (rank),c)
else:
    print("rank %d data : " % (rank),b)