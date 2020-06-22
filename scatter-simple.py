from mpi4py import MPI

comm = MPI.COMM_WORLD
size = comm.Get_size()
rank = comm.Get_rank()

if rank == 0:
    #data = [i for i in range(size)]
    data1 = [23,[56,78,90],56.7898,"test","kelebihan"]
    data = data1[0:size]
else:
    data = None
data = comm.scatter(data, root=0)
print("rank %d data : " % (rank),data)