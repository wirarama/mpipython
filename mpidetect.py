import numpy as np
import cv2
from mpi4py import MPI
comm = MPI.COMM_WORLD
size = comm.Get_size()
rank = comm.Get_rank()

def detectcore(pic,picout):
    picname = picout.split(".")
    img = cv2.imread(pic)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    fc = 0
    for (x,y,w,h) in faces:
        img = cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
        roi_gray = gray[y:y+h, x:x+w]
        roi_color = img[y:y+h, x:x+w]
        eyes = eye_cascade.detectMultiScale(roi_gray)
        for (ex,ey,ew,eh) in eyes:
            cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,255,0),2)
        cv2.imwrite('%s-%d.%s'%(picname[0],fc,picname[1]),img[y:y+h,x:x+w])
        fc+=1
    cv2.imwrite(picout,img)

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
print("rank %d memiliki %s gambar yaitu : %s"%(rank,len(data),str(data)))

face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_eye.xml')
for pic in data:
    detectcore('img/'+pic,'imgout/'+pic)