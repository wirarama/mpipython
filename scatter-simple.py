from mpi4py import MPI
comm = MPI.COMM_WORLD
size = comm.Get_size()
rank = comm.Get_rank()

if rank == 0:
    data = [3,[4,3,6],1.6379,"beda sendiri"] #ini array
else:
    data = None
data = comm.scatter(data, root=0) #its not a bcast but scatter
print("rank %d data : " % (rank),data)