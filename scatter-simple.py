from mpi4py import MPI
comm = MPI.COMM_WORLD
size = comm.Get_size()
rank = comm.Get_rank()

if rank == 0:
    data = [4,5,6,7] #its a array
else:
    data = None
data = comm.scatter(data, root=0) #its not a bcast but scatter
print("rank %d data : " % (rank),data)