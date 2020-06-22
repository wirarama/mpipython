from mpi4py import MPI

comm = MPI.COMM_WORLD
def printbarrier(session):
    if comm.rank != 0:
        data = "Rank "+str(comm.rank)+" session "+str(session)
        comm.send(data,dest=0,tag=session)
    else:
        print("Rank %d session %s" % (comm.rank,session))
        for i in range(1,comm.size):
            data = comm.recv(source=i,tag=session)
            print(data)

printbarrier(1)
comm.Barrier()
printbarrier(2)
comm.Barrier()
printbarrier(3)
comm.Barrier()