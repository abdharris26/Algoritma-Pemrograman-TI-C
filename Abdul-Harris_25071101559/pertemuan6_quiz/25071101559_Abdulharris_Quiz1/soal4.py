minggu = int(input("Masukkan jumlah minggu: "))
kategori = int(input("Masukkan jumlah kategori buku: "))
matriks = []

for i in range(minggu):
    baris = []
    for j in range(kategori):
        val = int(input(f"Minggu {i+1}, Kategori {j+1}: "))
        baris.append(val)
    matriks.append(baris)

# Tampilkan Matriks
print("\nMatriks Peminjaman:")
for row in matriks:
    print(row)

# Hitung per minggu (baris)
for i in range(minggu):
    print(f"Total peminjaman minggu {i+1}: {sum(matriks[i])}")