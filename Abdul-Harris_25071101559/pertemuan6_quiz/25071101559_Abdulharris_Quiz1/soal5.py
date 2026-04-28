class Buku:
    def __init__(self, judul, denda_per_hari):
        self.judul = judul
        self.denda_per_hari = denda_per_hari
    def tampilkan(self):
        print(f"{self.judul} - Denda Rp{self.denda_per_hari}/hari")

class Peminjaman:
    def __init__(self):
        self.total_denda = 0
    def tambah(self, buku, hari):
        self.total_denda += (buku.denda_per_hari * hari)
    def ringkasan(self):
        print("Total denda akumulasi: Rp", self.total_denda)

# Program Utama
list_buku = [Buku("Sejarah", 2000), Buku("Pemrograman", 3000), Buku("Python", 4000)]
for b in list_buku:
    b.tampilkan()

pinjam = Peminjaman()
pinjam.tambah(list_buku[0], 2) # Contoh: buku 1 dipinjam 2 hari
pinjam.ringkasan()