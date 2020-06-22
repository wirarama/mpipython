from mpi4py import MPI
import numpy
comm = MPI.COMM_WORLD
size = comm.Get_size()
rank = comm.Get_rank()

a_size = 1
senddata = (rank+1)*numpy.arange(size*a_size,dtype=numpy.float64)
recvdata = numpy.empty(size*a_size,dtype=numpy.float64)
comm.Alltoall(senddata,recvdata)
print("rank %d recvdata : " % (rank),recvdata)