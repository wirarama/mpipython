from mpi4py import MPI
from bagikerja import bagikerja,lihatisi

comm = MPI.COMM_WORLD
size = comm.Get_size()
rank = comm.Get_rank()

if rank==0:
    f = open('sharelinkgan.txt','r')
    data = bagikerja(f.readlines(),size)
    #print("Total bagian : %d" % len(data))
    #lihatisi(data)
else:
    data = None
data = comm.scatter(data, root=0)
print("rank %d mendapatkan : %d data " % (rank,len(data)))

#from mpiscraping import cariinsemua
#cariinsemua(data,['budaya','culture','people'],'p')

from mpiscraping import cariinsemualog
cariinsemualog(data,['budaya','culture','people'],'p',"hasiltemuan/rank"+str(rank)+".txt")