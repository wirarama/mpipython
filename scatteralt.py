from mpi4py import MPI

comm = MPI.COMM_WORLD
size = comm.Get_size()
rank = comm.Get_rank()

if rank == 0:
    data = [34,[34,45,65,76],56]
    #data = [i+1 for i in range(size)]
else:
    data = None
data = comm.scatter(data, root=0)
print("rank %i mendapat data %s" % (rank,data))
