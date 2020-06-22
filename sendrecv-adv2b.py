from mpi4py import MPI

comm = MPI.COMM_WORLD
rank = comm.rank
size = comm.size

print("rank %d " % rank,end=" ")
if rank == 0:
    for i in range(size):
        if i%2==0: 
            comm.send(2,dest=i,tag=1)
        else:
            comm.send(3,dest=i,tag=1)
elif rank%2==0: #genap
    data1 = comm.recv(source=0,tag=1)
    for i in range(size):
        if i%2==1:
            a = data1*rank
            comm.send(a,dest=i,tag=1)
            b = comm.recv(source=i,tag=1)
            print(b*rank)
else: #ganjil
    data2 = comm.recv(source=0,tag=1)
    for i in range(size):
        if i%2==0:
            a = data2*rank
            comm.send(a,dest=i,tag=1)
            b = comm.recv(source=i,tag=1)
            print(b*rank)