from mpi4py import MPI
comm = MPI.COMM_WORLD
rank = comm.Get_rank()

data = [rank+1,(rank+1)*10]
data = comm.gather(data, root=0)
if rank == 0:
    print(type(data))
    print(data)