buku = [
    ["Algoritma", 2000],
    ["Basis Data", 2500],
    ["struktur data", 3000],
    ["python", 3500],
    ["sejarah", 4000]
]# Diasumsikan buku yang dipinjam adalah buku pertama (Algoritma)
denda_per_hari = 2000 

while True:
    hari = int(input("Masukkan hari keterlambatan: "))
    if hari < 0:
        print("Error: Hari tidak boleh kurang dari 0!")
    else:
        break

if hari == 0:
    print("Tidak ada denda")
else:
    total = hari * denda_per_hari
    print(f"Total denda Anda: Rp{total}")