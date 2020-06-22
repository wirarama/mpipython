from math import ceil
def bagikerja(d,size):
    i = ceil(len(d)/size)
    data = []
    for x in range(0,len(d),i):
        if (x+i)<=len(d):
            data.append(d[x:(x+i)])
        else:
            data.append(d[x:len(d)])
    return data
def lihatisi(d):
    i = 0
    for x in d:
        print("bagian %d berisi %d url:" % (i,len(x)))
        for y in x:
            print("\t%s"%y.replace("\n",""))
        i+=1
        