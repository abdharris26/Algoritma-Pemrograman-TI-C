
struktur = {
    "Skripsi_Aqil": {
        "Bab_1": {
            "pendahuluan.docx": 45,
            "latar_belakang.docx": 62
        },
        "Bab_2": {
            "landasan_teori.docx": 118,
            "referensi": {
                "paper_A.pdf": 340,
                "paper_B.pdf": 210
            }
        },
        "Bab_3": {
            "metodologi.docx": 89,
            "diagram": {
                "flowchart.png": 512,
                "erd.png": 278,
                "arsitektur": {
                    "sistem.png": 430
                }
            }
        },
        "sidang": {
            "presentasi.pptx": 2048,
            "catatan_revisi.txt": 15
        },
        "README.txt": 8
    }
}

# Tugas A 
def total_ukuran(folder):
    total = 0
    for item in folder.values():
        if isinstance(item, dict):
            total += total_ukuran(item)
        else:
            total += item
    return total



# Tugas B 
def hitung_file(folder):
    jumlah = 0
    for item in folder.values():
        if isinstance(item, dict):
            jumlah += hitung_file(item)
        else:
            jumlah += 1
    return jumlah


# tugas c
def cari_terbesar(folder):
    terbesar_nama = ""
    terbesar_ukuran = 0

    for nama, item in folder.items():
        if isinstance(item, dict):
            nama_file, ukuran = cari_terbesar(item)
            if ukuran > terbesar_ukuran:
                terbesar_nama = nama_file
                terbesar_ukuran = ukuran
        else:
            if item > terbesar_ukuran:
                terbesar_nama = nama
                terbesar_ukuran = item

    return terbesar_nama, terbesar_ukuran

# tugas D
def tampilkan_tree(folder, nama="root", level=0):
    indent = " " * (level * 2)
    print(f"{indent}📁 {nama}")

    for key, value in folder.items():
        if isinstance(value, dict):
            tampilkan_tree(value, key, level + 1)
        else:
            print(f"{indent}  📄 {key} ({value} KB)")


root = struktur["Skripsi_Aqil"]

print("=== HASIL ===")

# Total ukuran
print("Total ukuran:", total_ukuran(root), "KB")

# Jumlah file
print("Jumlah file:", hitung_file(root), "file")

# File terbesar
nama, ukuran = cari_terbesar(root)
print(f"File terbesar: {nama} ({ukuran} KB)")

# Tampilkan struktur
print("\nStruktur folder:")
tampilkan_tree(root, "Skripsi_Aqil")