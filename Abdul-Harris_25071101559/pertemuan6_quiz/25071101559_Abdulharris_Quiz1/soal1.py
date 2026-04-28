buku = [
    ["Algoritma", 2000],
    ["Basis Data", 2500],
    ["struktur data", 3000],
    ["python", 3500],
    ["sejarah", 4000]
]

for i in range(len(buku)):
    print(i+1, buku[i][0], buku[i][1] )
    
pilih = int(input("pilihlah buku yang ingin dipilih: "))

if 1 <= pilih <= len(buku):
    print("buku yang dipilih: ", buku[pilih-1][0])
    print("denda yang harus dibayar: ", buku[pilih-1][1])
else:
    print("error")