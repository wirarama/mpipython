from mpi4py import MPI
comm = MPI.COMM_WORLD
if comm.rank==0:
    print("Rank %d Kumpulin data" % (comm.rank))
    comm.Barrier()
    comm.Barrier()
else:
    comm.Barrier()
    print("Session 1 Rank %d dari %d" % (comm.rank, comm.size))
    comm.Barrier()
    print("Session 2 Rank %d dari %d" % (comm.rank, comm.size))