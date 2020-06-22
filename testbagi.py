from math import ceil
d = [i for i in range(10)]
n = ceil(len(d)/3)
out = []
for x in range(0,len(d),n):
    if (x+n) < len(d):
        out.append([i for i in range(x,x+n)])
    else:
        out.append([i for i in range(x,len(d))])
print(out)