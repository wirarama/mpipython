from mpi4py import MPI
comm = MPI.COMM_WORLD

data = comm.rank
out = comm.allreduce(data,op=MPI.SUM)
print("rank %d data : " % (comm.rank),out)