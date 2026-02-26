#latihan praktikum 5
stok_barang = [15, 40, 30,10,25]

#soal 1
stok = stok_barang.index(10)
stok_barang[stok]= 50
print(stok_barang)

#soal 2
stok_barang.append(5)
stok_barang.sort(reverse=True)
print(stok_barang)

#soal 3
print (sum(stok_barang))

#soal 4
print("stok aman") if sum(stok_barang)/len(stok_barang) >= 20 else print("stok tidak aman")
    
    



