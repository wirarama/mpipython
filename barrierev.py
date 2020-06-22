from mpi4py import MPI

comm = MPI.COMM_WORLD
print("Rank %d session 1" % (comm.rank),flush=True)
comm.Barrier()
print("Rank %d session 2" % (comm.rank),flush=True)
comm.Barrier()
print("Rank %d session 3" % (comm.rank),flush=True)
comm.Barrier()
