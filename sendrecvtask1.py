from mpi4py import MPI
comm = MPI.COMM_WORLD
rank = comm.rank

#print("rank %d " % rank,end=" ",flush=True)
if rank == 0:
    for x in range(1,(comm.size)):
        comm.send(45, dest=x)
    print("sends",flush=True)
else:
    if rank!=0:
        c = comm.recv(source=0)
    print("receive :",c,flush=True)