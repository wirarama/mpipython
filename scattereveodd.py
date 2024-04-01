from mpi4py import MPI
from math import ceil

comm = MPI.COMM_WORLD
size = comm.Get_size()
rank = comm.Get_rank()

if rank == 0:
    data1 = [i for i in range(100)]
    i = ceil(len(data1)/size)
    data = []
    for x in range(0,len(data1),i):
        data2 = []
        if (x+i)<=len(data1):
            last = (x+i)
        else:
            last = len(data1)
        for y in range(x,last,2):
            data2.append(y)
        data.append(data2)
    print(len(data),data)
else:
    data = None
data = comm.scatter(data, root=0)
print("rank %d data : " % (rank),data)