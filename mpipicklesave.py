import face_recognition
import pickle
from mpi4py import MPI
comm = MPI.COMM_WORLD
size = comm.Get_size()
rank = comm.Get_rank()

if rank==0:
    import os
    pics = []
    for filename in os.listdir(os.getcwd()+'/training/'):
        if any(x in filename for x in ['.jpg','.jpeg','.png','.gif']):
            pics.append(filename)
    from bagikerja import bagikerja
    data = bagikerja(pics,size)
else:
    data = None
data = comm.scatter(data,root=0)
all_face_encodings = {}
for pic in data:
    picname = pic.split(".")
    img = face_recognition.load_image_file("training/"+pic)
    all_face_encodings[picname[0]] = face_recognition.face_encodings(img)[0]
all_face_encodings = comm.gather(all_face_encodings, root=0)
if rank == 0:
    print("Sudah disimpan %d wajah yaitu : "%(len(all_face_encodings)),end=" ")
    for x in all_face_encodings:
        for y in x.keys():
            print(y,end=" ")
    with open('mpidataset_faces.dat', 'wb') as f:
        pickle.dump(all_face_encodings, f)