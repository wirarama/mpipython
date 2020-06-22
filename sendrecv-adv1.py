from mpi4py import MPI

comm = MPI.COMM_WORLD
rank = comm.rank

print("rank %d " % rank,end=" ")
if rank==0:
    data1 = 10
    data2 = 100
    comm.send(data1,dest=1,tag=1)
    comm.send(data2,dest=2,tag=1)
    print("Mengirim")
    data10 = comm.recv(source=3,tag=14)
    data9 = comm.recv(source=4,tag=69)*2
    dataHasil = data10 + data9
    print(dataHasil)
elif rank==1:
    data11 = comm.recv(source=0,tag=1)
    data11 += 45
    print("Hasil Sementara : %d " % (data11))
    comm.send(data11,dest=3,tag=1)
elif rank==2:
    data12 = comm.recv(source=0,tag=1)
    data12 -= 45
    comm.send(data12,dest=4,tag=1)
    print("Hasil Sementara : %d " % (data12))
elif rank==3:
    data13 = comm.recv(source=1,tag=1)
    data13 **= 2
    print("Hasil Akhir : %d " % (data13))
    comm.send(data13,dest=0,tag=14)
elif rank==4:
    data14 = comm.recv(source=2,tag=1)
    data14 **= 2
    print("Hasil Akhir : %d " % (data14))
    comm.send(data14,dest=0,tag=69)
    
    