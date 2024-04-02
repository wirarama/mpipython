from mpi4py import MPI
from math import ceil

comm = MPI.COMM_WORLD
size = comm.Get_size()
rank = comm.Get_rank()

status = 1
if rank == 0:
    data1 = [i for i in range(100)]
    i = ceil(len(data1)/size)
    data = []
    for x in range(0,len(data1),i):
        if (x+i)<=len(data1):
            data.append(data1[x:(x+i)])
        else:
            data.append(data1[x:len(data1)])
    if len(data)!=size:
        status = 0
        print("pembaginya terlalu besar boss")
else:
    data = None
status = comm.bcast(status,root=0)
if status==1:
    data = comm.scatter(data, root=0)
    print("rank %d memiliki %d data yaitu %s " % (rank,len(data),data))
