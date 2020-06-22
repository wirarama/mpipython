from mpi4py import MPI
comm = MPI.COMM_WORLD

if comm.rank == 0:
    data = "kata kunci"
    for i in range(1,comm.size):
        comm.send(data,dest=i,tag=1)
    comm.Barrier()
    data2 = "minyak goreng 2kg"
    for i in range(1,comm.size):
        comm.send(data2,dest=i,tag=2)
    comm.Barrier()
else:
    comm.Barrier()
    data = comm.recv(source=0,tag=1)
    print("Rank %d lapor : Isi %s " % (comm.rank,data))
    comm.Barrier()
    data2 = comm.recv(source=0,tag=2)
    print("Session 2 Rank %d lapor : Isi %s " % (comm.rank,data2))
