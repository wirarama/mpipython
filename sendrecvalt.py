from mpi4py import MPI

comm = MPI.COMM_WORLD
rank = comm.Get_rank()

if rank == 0:
    data = {'a': 7, 'b': 3.14}
    data1 = {'c': 'hello', 'd': 'world'}
    comm.send(data, dest=1, tag=1)
    comm.send(data1, dest=1, tag=2)
    print("terkirim vroh")
elif rank == 1:
    data = comm.recv(source=0,tag=1)
    data1 = comm.recv(source=0,tag=2)
    print("Isi a: %d b: %s " % (data['a'],data['b']))
    print("Isi c: %s d: %s " % (data1['c'],data1['d']))


