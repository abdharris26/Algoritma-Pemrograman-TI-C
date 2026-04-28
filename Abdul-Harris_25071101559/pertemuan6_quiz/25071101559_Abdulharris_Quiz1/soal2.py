buku = [["Algoritma", 2000], ["Basis Data", 2500], ["struktur data", 3000], ["python", 3500], ["sejarah", 4000]]
meminjam = []

while True:
    for i in range(len(buku)):
        print(f"{i+1}. {buku[i][0]} - Rp{buku[i][1]}")
    pilih = int(input("Pilih buku (0 untuk selesai): "))
    if pilih == 0: break
    if 1 <= pilih <= len(buku):
        # Menyimpan judul dan denda per hari
        meminjam.append(buku[pilih-1])
    else:
        print("Buku tidak valid")
        
print("\nDaftar Buku Dipinjam:")
total = 0
for item in meminjam:
    total += item[1] # Menambah denda per hari (simulasi 1 hari)
    print(f"{item[0]} - Rp{item[1]}")

print("Total denda (jika terlambat 1 hari): Rp", total)