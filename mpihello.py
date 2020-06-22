from mpi4py import MPI
comm = MPI.COMM_WORLD
if comm.rank==0:
    print("saya boss")
elif comm.rank==4:
    print("saya anak istimewa")
else:
    print("saya anak buah no",comm.rank,"dari total",comm.size)