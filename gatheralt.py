from mpi4py import MPI

comm = MPI.COMM_WORLD
size = comm.Get_size()
rank = comm.Get_rank()

if rank == 0:
    data = 78
elif rank == 1:
    data = "tulisan"
elif rank == 2:
    data = [23,56,34,56,45]
elif rank == 3:
    data = True
data = comm.gather(data, root=0)
print("rank %d menerima %s" % (rank,data))
