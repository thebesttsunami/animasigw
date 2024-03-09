class Data:
    
def __init__(self): 
    pass

def daftar(self):
    
nama_lengkap = input("Masukan Nama: ")
Email = input("Masukan Email: ")
Gender = input("Masukan Kelami n: ")
ttl = input("Masukan Tanggal: ")
bln = input("Masukan Bulan: ")
thn = input("Masukan Tahun: ")
pw = input("Masukan pw: ")

Main(nama_lengkap, Email, Gende r,ttl,bln,thn,pw)


class Main:

def__init__(self,nama_lengkap, Em ail, Gender,ttl,bln,thn,pw):

self.nama_lengkap = nama_lengkap
self.Email = Email
self.Gender = Gender
self.ttl = ttl
self.bin = bin
self.thn = thn
self.pw = pw
self.r = requests. Session()
self.url = "https://mbasic.facebook.com/reg/?cid=103&refid=8&rtime =1708262799&hrc=1&wtsid=rdr_0s 7CabjzO6IVZRPXc&refsrc=deprecated&_rdr"

self.Create(self.url, self.nama_lengkap, self. Email, self. Gender, self.ttl, self.bln, self.thn, self.pw)
