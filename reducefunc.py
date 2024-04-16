from mpi4py import MPI
comm = MPI.COMM_WORLD

def test(a,b):
    return [a[0]+b[0],a[1]+b[1],a[2]+b[2]]

data = [comm.rank+1,comm.rank+1*3,comm.rank+1*10]
data = comm.reduce(data,op=test,root=0)
if comm.rank == 0:
    print(data)