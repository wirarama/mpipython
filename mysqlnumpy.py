import pymysql as mdb
import numpy

DBconn = mdb.connect(host='localhost', user='konversiKurikulum', passwd='konversiKurikulum', db='konversiKurikulum')
cursor = DBconn.cursor()
cursor.execute("select * from matakuliah")
A = numpy.fromiter(cursor.fetchall(), count=-1,dtype=[('no',numpy.int32),('kode',numpy.unicode_,16),('namamk',numpy.unicode_,48),('sks',numpy.int32),('sifat',numpy.unicode_,2),('jenisMK',numpy.unicode_,2),('semester',numpy.int32),('kurikulum',numpy.int32)])
#A = numpy.fromiter(cursor.fetchall(), count=-1,dtype=[('', numpy.unicode_,32)]*8)
print(A)
