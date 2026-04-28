
DAFTAR_PILIHAN = ["gunting", "batu", "kertas", "batu", "gunting", "kertas", "gunting", "batu"]

# === BAGIAN A ===

def tentukan_pemenang(pilihan_pemain, pilihan_komputer):
    pilihan = 0
    pilihan["gunting" : "batu", 
    "kertas" : "batu",
    "gunting" : "kertas"]

    
    while pilihan < pilihan_komputer:
        tebakan = input(str("pilihan pemain: "))
        tebakan = tebakan + 1
        
        if tebakan < pilihan_pemain:
            print("pemain")
        elif tebakan > pilihan_pemain:
            print("komputer")
        else:
            print("seri")
          
              
        sisa = pilihan_komputer - tebakan
        return True, sisa

    return False, 0 

def main_satu_giliran(nomor_giliran):
    pilihan_komputer = DAFTAR_PILIHAN[nomor_giliran % len(DAFTAR_PILIHAN)]
    while True:
        tebakan = input("batu/gunting/kertas").lower
        if tebakan in DAFTAR_PILIHAN:
            break
           

def main_satu_ronde(nama, nomor_ronde):
    nomor_giliran = 0
    pilihan_komputer = DAFTAR_PILIHAN[nomor_giliran % len(DAFTAR_PILIHAN)]
    nomor_ronde
    hitung_skor = 0

    menang, kalah = str(pilihan_komputer(nama, 5))
    skor = hitung_skor(menang, kalah)



# === BAGIAN B ===
def tampilkan_riwayat(riwayat):
    if len(riwayat) == 0:
        print("belum ada riwayat")
    else:
        print("+---------------------------+")
        print("Nomor Nama Skor")
        for i in range(len(riwayat)):
            print(i+1, riwayat[i][0], riwayat[i][1])
            


# === BAGIAN C ===
def bubble_sort_riwayat(riwayat):
    data = riwayat.copy()

    for i in range(len(data)):
        max_index = i

        for j in range(i+1, len(data)):
            if data[j][1] < data[max_index][1]:
                max_index = j

        # tukar
        temp = data[i]
        data[i] = data[max_index]
        data[max_index] = temp

    return data


# === LEADERBOARD ===
def tampilkan_leaderboard(riwayat):
    data = bubble_sort_riwayat(riwayat)

    print("Leaderboard:")
    for i in range(len(data)):
        if i == 0:
            print(i+1, data[i][0], data[i][1], "*")
        else:
            print(i+1, data[i][0], data[i][1])



nama = input("Masukkan nama: ")
riwayat = []
ronde = 0

while True:
    hasil = main_satu_ronde(nama, ronde)
    riwayat.append(hasil)
    ronde = ronde + 1

    ulang = input("Main lagi? (y/n): ")
    if ulang != "y":
        break

tampilkan_riwayat(riwayat)
tampilkan_leaderboard(riwayat)











