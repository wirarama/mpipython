from mpi4py import MPI
comm = MPI.COMM_WORLD

if comm.rank == 0:
    data = 4
    for i in [1,2,4]:
        comm.send(data,dest=i,tag=1)
    print ("0 mengirim ke 1, 2, 4")
    comm.Barrier()
    comm.Barrier()
elif comm.rank in [1,2,4]:
    comm.Barrier()
    data = comm.recv(source=0,tag=1)
    print ("%d menerima dari 0" % (comm.rank))
    if comm.rank == 1:
        for i in [3,5]:
            comm.send(data,dest=i,tag=1)
        comm.Barrier()
        print ("1 mengirim ke 3 dan 5")
    elif comm.rank == 2:
        comm.send(data,dest=6,tag=1)
        comm.Barrier()
        print ("2 mengirim ke 6")
    else:
        comm.Barrier()
else:
    comm.Barrier()
    comm.Barrier()
    if comm.rank == 3:
        data = comm.recv(source=1,tag=1)
        print ("3 menerima dari 1")
        comm.send(data,dest=7,tag=1)
        print ("3 mengirim ke 7")
    elif comm.rank == 5:
        data = comm.recv(source=1,tag=1)
        print ("5 menerima dari 1")
    elif comm.rank == 6:
        data = comm.recv(source=2,tag=1)
        print ("6 menerima dari 2")
    elif comm.rank == 7:
        data = comm.recv(source=3,tag=1)
        print ("7 menerima dari 3")
