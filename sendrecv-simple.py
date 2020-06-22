from mpi4py import MPI

comm = MPI.COMM_WORLD
rank = comm.rank

print("rank %d " % rank,end=" ")
if rank == 0:
    c = 45
    comm.send(c, dest=1, tag=1)
    comm.send([2,3,4], dest=1, tag=2)
    comm.send(c, dest=2, tag=1)
    print("mengirim")
elif rank == 1:
    c = comm.recv(source=0, tag=1)
    d = comm.recv(source=0, tag=2)
    print("menerima c: %d d: %s" % (c,d))
elif rank == 2:
    c = comm.recv(source=0,tag=1)
    print("menerima c: %d " % (c))
else:
    print("nganggur")
