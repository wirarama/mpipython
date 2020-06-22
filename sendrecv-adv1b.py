from mpi4py import MPI

comm = MPI.COMM_WORLD
rank = comm.rank

print("rank %d " % rank,end=" ")
if rank==0:
    data1 = 10
    data2 = 100
    comm.send(data1,dest=1,tag=1)
    comm.send(data2,dest=2,tag=1)
    print("mengirim ",data1,data2)
    data7 = comm.recv(source=3,tag=1)
    data8 = comm.recv(source=4,tag=1)
    print("Hasil beneran akhir",data7+2*data8)
elif rank==1:
    data3 = comm.recv(source=0,tag=1)
    print("menerima ",data3)
    data3+=45
    comm.send(data3,dest=3,tag=1)
    print("mengirim ",data3)
elif rank==2:
    data4 = comm.recv(source=0,tag=1)
    print("menerima ",data4)
    data4-=45
    comm.send(data4,dest=4,tag=1)
    print("mengirim ",data4)
elif rank==3:
    data5 = comm.recv(source=1,tag=1)
    print("menerima ",data5)
    data5 **= 2
    print("menghitung hasil akhir ",data5)
    comm.send(data5,dest=0,tag=1)
elif rank==4:
    data6 = comm.recv(source=2,tag=1)
    print("menerima ",data6)
    data6 **= 2
    print("menghitung hasil akhir ",data6)
    comm.send(data6,dest=0,tag=1)