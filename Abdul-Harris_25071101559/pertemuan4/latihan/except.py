#studi kasus
class NilaiMahasiswa:
    def hitung_rata_rata(self):
        try:
            nilai1 = float(input("masukan nilai 1: "))
            nilai2 = float(input("masukan nilai kedua: "))
            nilai3 = float(input("masukan nilai ketiga: "))
            
            rata_rata = (nilai1 + nilai2 + nilai3)/3
            print("rata-rata nilainya: ",rata_rata)
            
        except ValueError:
            print("input harus berupa angka")
        
        finally:
            print("program telah selesai")
            
objek = NilaiMahasiswa()
objek.hitung_rata_rata()
        