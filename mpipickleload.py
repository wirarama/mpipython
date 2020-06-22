import face_recognition
import pickle
import numpy as np
from mpi4py import MPI
comm = MPI.COMM_WORLD
size = comm.Get_size()
rank = comm.Get_rank()

def siapani(result):
    for x in result:
        if x[1] == True:
            return x[0]
    return "gakenal"

if rank == 0:
    with open('mpidataset_faces.dat', 'rb') as f:
        all_face_encodings = pickle.load(f)
    face_names = []
    face_encodings = []
    for x in all_face_encodings:
        for y in x.keys():
            face_names.append(y)
        for z in x.values():
            face_encodings.append(z)
    face_encodings = np.array(face_encodings)
else:
    face_names = None
    face_encodings = None
face_names = comm.bcast(face_names,root=0)
face_encodings = comm.bcast(face_encodings,root=0)

if rank==0:
    import os
    pics = []
    for filename in os.listdir(os.getcwd()+'/img/'):
        if any(x in filename for x in ['.jpg','.jpeg','.png','.gif']):
            pics.append(filename)
    from bagikerja import bagikerja
    data = bagikerja(pics,size)
else:
    data = None
data = comm.scatter(data, root=0)
gakenal = 0
kenal = 0
for pic in data:
    unknown_image = face_recognition.load_image_file("img/"+pic)
    unknown_face = face_recognition.face_encodings(unknown_image)
    print("Pada gambar %s ditemukan %d wajah : "%(pic,len(unknown_face)),end=" ")
    for face in unknown_face:
        result = face_recognition.compare_faces(face_encodings,face)
        names_with_result = list(zip(face_names, result))
        hasil = siapani(names_with_result)
        print(hasil,end=" ")
        if hasil=='gakenal':
            gakenal+=1
        else:
            kenal+=1
    print()
print("rank %d wajah dikenal %d dan wajah tidak dikenal %d dari total %d wajah akurasi %.2f"%(rank,kenal,gakenal,(kenal+gakenal),float(kenal/(kenal+gakenal))))