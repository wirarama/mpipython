from mpi4py import MPI

comm = MPI.COMM_WORLD
rank = comm.Get_rank()

data = [rank+67,rank-89,rank*90,rank]
data = comm.gather(data, root=0)
if rank == 0:
    print(type(data))
    print(data)