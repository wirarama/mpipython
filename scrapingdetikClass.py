from bs4 import BeautifulSoup
import requests as req
import pathlib

class scrDetik:
    page = []
    konten = []
    root = 'detik/'
    kategori = 'kategori/'
    berita = 'berita/'
    def __init__(self,katakunci):
        pathlib.Path(self.root+self.kategori).mkdir(parents=True, exist_ok=True)
        pathlib.Path(self.root+self.berita).mkdir(parents=True, exist_ok=True)
        url = "https://www.detik.com/search/searchall?query="+katakunci.replace(' ','+')
        self.caridetik(url)
        self.semuapage()
        self.savepages()
        self.savekonten()
        self.perkonten()
    def caridetik(self,url):
        resp = req.get(url)
        soup = BeautifulSoup(resp.text,'lxml')
        for a in soup.find_all('a',href=True):
            if("detik.com" in a['href']):
                suburl = a['href'].split('/')
                if len(suburl)>4:
                    if suburl[3]=='search' and '&page=' in a['href']:
                        if(a['href'] not in self.page):
                            self.page.append(a['href'])
                    elif len(suburl)>5:
                        if((a['href'],suburl[3]) not in self.konten):
                            self.konten.append((a['href'],suburl[3]))
    def semuapage(self):
        for pp in self.page:
            self.caridetik(pp)
    def savepages(self):
        pagefile = open(self.root+'page.txt','w')
        for x in self.page:
            pagefile.write(x.replace(' ','+')+"\n")
        pagefile.close()
    def savekonten(self):
        kontenfile = open(self.root+'konten.txt','w')
        for x in self.konten:
            kontenfile.write(x[0].replace(' ','+')+","+x[1]+"\n")
        kontenfile.close()
    def perkonten(self):
        for x in self.konten:
            f = open(self.root+self.kategori+x[1]+'.txt','a')
            f.write(x[0].replace(' ','+')+"\n")
            f.close()
    def detailberitadetik(self,url):
        resp = req.get(url)
        soup = BeautifulSoup(resp.text,'lxml')
        out = ""
        for judul in soup.find_all('h1',{"class":"detail__title"}):
            out += judul.text
        for isi in soup.find_all('div',{"class":"detail__body-text"}):
            out += isi.text
        return out
    def downloadberita(self,topik):
        sumber = open(self.root+self.kategori+topik,'r')
        judultopik,ekstensi = topik.split('.')
        pathlib.Path(os.getcwd()+self.root+self.berita+judultopik).mkdir(parents=True, exist_ok=True)
        for url in sumber.readlines():
            suburl = url.split('/')
            print(suburl[-1])
            f = open(self.root+self.berita+judultopik+'/'+suburl[-1]+'.txt','w')
            f.write(self.detailberitadetik(url))
            f.close()