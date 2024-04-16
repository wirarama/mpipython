from mpi4py import MPI
import numpy
comm = MPI.COMM_WORLD
size = comm.Get_size()
rank = comm.Get_rank()

senddata = (rank+1)*numpy.arange(size,dtype=numpy.float64)
print("rank %d senddata : " % (rank),senddata)
recvdata = numpy.empty(size,dtype=numpy.float64)
comm.Alltoall(senddata,recvdata)
print("rank %d recvdata : " % (rank),recvdata)