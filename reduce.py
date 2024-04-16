from mpi4py import MPI
import random as rd
comm = MPI.COMM_WORLD

data = comm.rank+1
#data2 = [comm.rank,data*rd.randint(0,comm.size)]
data2 = ["f21"+str(comm.rank),comm.rank+1]
outsum = comm.reduce(data,op=MPI.SUM,root=0)
outmin = comm.reduce(data,op=MPI.MIN,root=0)
outmax = comm.reduce(data,op=MPI.MAX,root=0)
outprod = comm.reduce(data,op=MPI.PROD,root=0)
outmaxloc = comm.reduce(data2,op=MPI.MAXLOC,root=0)
outminloc = comm.reduce(data2,op=MPI.MINLOC,root=0)
if comm.rank == 0:
    print("rank %d SUM : " % (comm.rank),outsum)
    print("rank %d MEAN : " % (comm.rank),outsum/comm.size)
    print("rank %d MIN : " % (comm.rank),outmin)
    print("rank %d MAX : " % (comm.rank),outmax)
    print("rank %d PROD : " % (comm.rank),outprod)
    print("rank %d MAXLOC : " % (comm.rank),outmaxloc)
    print("rank %d MINLOC : " % (comm.rank),outminloc)