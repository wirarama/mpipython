from bs4 import BeautifulSoup
import requests as req

def cariingan(link,katakunci,tag):
    try:
        resp = req.get(link)
        soup = BeautifulSoup(resp.text,'lxml')
        for y in soup.find_all(tag):
            if any(x in y.text for x in katakunci):
                print(y.text)
    except:
        print("[gagal] %s " % link)
            
def cariinsemua(daftarlink,katakunci,tag):
    for x in daftarlink:
        cariingan(x,katakunci,tag)

def cariinganlog(link,katakunci,tag,file):
    try:
        resp = req.get(link)
        soup = BeautifulSoup(resp.text,'lxml')
        f = open(file,'a')
        for y in soup.find_all(tag):
            if any(x in y.text for x in katakunci):
                f.write(y.text+"\n\n")
        f.close()
    except:
        print("[gagal] %s " % link)
            
def cariinsemualog(daftarlink,katakunci,tag,file):
    for x in daftarlink:
        cariinganlog(x,katakunci,tag,file)