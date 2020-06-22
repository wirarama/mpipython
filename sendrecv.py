from mpi4py import MPI

comm = MPI.COMM_WORLD
rank = comm.rank

print("test %d " % rank)
if rank == 0:
    c = 45
    data = {'a': 7, 'b': 3.14}
    comm.send(data, dest=1, tag=1)
    comm.send(7, dest=1, tag=2)
    comm.send(c, dest=2, tag=1)
elif rank == 1:
    data = comm.recv(source=0, tag=1)
    d2 = comm.recv(source=0, tag=2)
    print("Isi a: %d b: %s d2: %d " % (data['a'],data['b'],d2))
elif rank == 2:
    c = comm.recv(source=0,tag=1)
    print("Isi c: %d " % (c))
