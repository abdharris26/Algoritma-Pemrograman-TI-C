class Vehincle:
    def __init__(self, jenis, merk, tahun_rilis):
        self.jenis = jenis
        self.merk = merk
        self.tahun_rilis = tahun_rilis
        
    def sound(self):
        return "suara"
    
class Motor(Vehincle):
    def __init__(self, jenis, merk, tahun_rilis):
        self.jenis = jenis
        self.merk = merk
        self.__tahun_rilis = tahun_rilis
        
    def get_tahun_rilis(self):
        return self.__tahun_rilis   
        
class Mobil(Vehincle):
    def __init__(self, jenis, merk, tahun_rilis):
        self.__jenis = jenis
        self.merk = merk
        self.tahun_rilis = tahun_rilis
        
    def get_jenis(self):
        return self.__jenis   
        
       
#membuat objek 
a1 = Vehincle ("kendaraan","darat",2015)
print(a1.sound())

a2 = Motor("kopling","rxking",2017,)
print(a2.get_tahun_rilis())
a3 = Mobil("besar","bmw",2020)
print(a3.merk)

    