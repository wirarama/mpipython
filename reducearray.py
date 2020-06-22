from mpi4py import MPI
comm = MPI.COMM_WORLD

data = []
for x in range(comm.size): data.append(comm.rank)
outsum = comm.reduce(data,op=MPI.SUM,root=0)
outmin = comm.reduce(data,op=MPI.MIN,root=0)
outmax = comm.reduce(data,op=MPI.MAX,root=0)
if comm.rank == 0:
    print("rank %d SUM : " % (comm.rank),outsum)
    print("rank %d MIN : " % (comm.rank),outmin)
    print("rank %d MAX : " % (comm.rank),outmax)