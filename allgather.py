from mpi4py import MPI

comm = MPI.COMM_WORLD
rank = comm.Get_rank()

data = rank
data = comm.allgather(data)
print("rank %d data : " % (rank),data)