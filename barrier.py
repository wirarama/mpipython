from mpi4py import MPI

comm = MPI.COMM_WORLD
if comm.rank==0:
    print("Rank %d Kumpulin data" % (comm.rank))
    comm.Barrier()
    print("Rank %d Menganggur" % (comm.rank))
    comm.Barrier()
    print("Rank %d Menganggur" % (comm.rank))
    comm.Barrier()
else:
    comm.Barrier()
    print("Session 1 Rank %d dari %d" % (comm.rank, comm.size))
    comm.Barrier()
    print("Session 2 Rank %d dari %d" % (comm.rank, comm.size))
    comm.Barrier()
    if comm.rank==2:
        print("Rank %d Upload data" % (comm.rank))
    else:
        print("Rank %d Menganggur" % (comm.rank))