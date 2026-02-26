gudang_pc = [ 
{"item": "Monitor", "harga": 1500000, "stok": 5}, 
{"item": "Keyboard", "harga": 400000, "stok": 12}, 
{"item": "Mouse", "harga": 250000, "stok": 20} 
] 
#soal 1
for x in gudang_pc:
    if x["item"]== "keyboard":
        x["kategori"] == "aksesoris"
        
print(gudang_pc)

#soal 2
gudang_pc.append({
    "item" : "Headset", "harga": 350000, "stok": 8 
})

#soal 3
for x in gudang_pc:
    print(f"Item: {x["item"]} | Total Aset: Rp {x["harga"] * x["stok"]}")