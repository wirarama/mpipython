from mpi4py import MPI
comm = MPI.COMM_WORLD

data = (comm.rank>round(comm.size/2))
print("rank %d data : " % (comm.rank),data)
outland = comm.reduce(data,op=MPI.LAND,root=0)
outlor = comm.reduce(data,op=MPI.LOR,root=0)
outband = comm.reduce(data,op=MPI.BAND,root=0)
outbor = comm.reduce(data,op=MPI.BOR,root=0)
if comm.rank == 0:
    print("rank %d LAND : " % (comm.rank),outland)
    print("rank %d LOR : " % (comm.rank),outlor)
    print("rank %d BAND : " % (comm.rank),outband)
    print("rank %d BOR : " % (comm.rank),outbor)