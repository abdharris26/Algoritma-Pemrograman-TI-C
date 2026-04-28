# === VARIABEL GLOBAL ===
DAFTAR_PILIHAN = ["gunting", "batu", "kertas", "batu", "gunting", "kertas", "gunting", "batu"]

# === BAGIAN A: FUNGSI INTI GAME ===

def tentukan_pemenang(pilihan_pemain, pilihan_komputer):
    """Menentukan pemenang antara pemain dan komputer berdasarkan aturan suit."""
    if pilihan_pemain == pilihan_komputer:
        return "seri"
    elif (pilihan_pemain == "gunting" and pilihan_komputer == "kertas") or \
         (pilihan_pemain == "batu" and pilihan_komputer == "gunting") or \
         (pilihan_pemain == "kertas" and pilihan_komputer == "batu"):
        return "pemain"
    else:
        return "komputer"

def main_satu_giliran(nomor_giliran):
    """Menjalankan satu giliran permainan dan mengembalikan hasil pemenang."""
    pilihan_komputer = DAFTAR_PILIHAN[nomor_giliran % len(DAFTAR_PILIHAN)]
    
    while True:
        pilihan_pemain = input("Masukkan pilihan (gunting/batu/kertas): ").lower()
        if pilihan_pemain == "gunting" or pilihan_pemain == "batu" or pilihan_pemain == "kertas":
            break
        print("Input tidak valid. Silakan coba lagi.")
    
    hasil = tentukan_pemenang(pilihan_pemain, pilihan_komputer)
    print("Komputer memilih: " + pilihan_komputer)
    print("Hasil giliran: " + hasil)
    return hasil

def main_satu_ronde(nama, nomor_ronde):
    """Menjalankan satu ronde hingga salah satu mencapai 3 kemenangan."""
    skor_pemain = 0
    skor_komputer = 0
    giliran = 0
    
    print("\n--- Ronde " + str(nomor_ronde) + " ---")
    while skor_pemain < 3 and skor_komputer < 3:
        hasil = main_satu_giliran(giliran)
        if hasil == "pemain":
            skor_pemain = skor_pemain + 1
        elif hasil == "komputer":
            skor_komputer = skor_komputer + 1
        giliran = giliran + 1
        print("Skor Sementara -> Pemain: " + str(skor_pemain) + ", Komputer: " + str(skor_komputer))
    
    if skor_pemain == 3:
        print("Selamat! Anda memenangkan ronde ini.")
        skor_akhir = skor_pemain * 10
    else:
        print("Komputer memenangkan ronde ini.")
        skor_akhir = 0
        
    return [nama, skor_akhir]

# === BAGIAN B: RIWAYAT SKOR ===

def tampilkan_riwayat(riwayat):
    """Mencetak riwayat permainan dalam bentuk tabel."""
    if len(riwayat) == 0:
        print("Belum ada riwayat.")
    else:
        print("\n--- Riwayat Permainan ---")
        print("No | Nama | Skor")
        # Menggunakan loop range untuk menggantikan enumerate
        for i in range(len(riwayat)):
            data = riwayat[i]
            print(str(i + 1) + " | " + data[0] + " | " + str(data[1]))

# === BAGIAN C: LEADERBOARD BUBBLE SORT ===

def bubble_sort_riwayat(riwayat):
    """Mengurutkan riwayat berdasarkan skor tertinggi menggunakan Bubble Sort."""
    # Membuat salinan list secara manual
    data_urut = []
    for item in riwayat:
        data_urut.append(item)
        
    n = len(data_urut)
    for i in range(n):
        for j in range(0, n - i - 1):
            if data_urut[j][1] < data_urut[j + 1][1]:
                # Tukar posisi
                temp = data_urut[j]
                data_urut[j] = data_urut[j + 1]
                data_urut[j + 1] = temp
    return data_urut

def tampilkan_leaderboard(riwayat):
    """Menampilkan peringkat skor akhir."""
    data_sorted = bubble_sort_riwayat(riwayat)
    print("\n--- Leaderboard ---")
    for i in range(len(data_sorted)):
        data = data_sorted[i]
        tanda = ""
        if i == 0:
            tanda = " *"
        print(str(i + 1) + ". " + data[0] + " - Skor: " + str(data[1]) + tanda)

# === PROGRAM UTAMA ===

def main():
    nama_pemain = input("Masukkan nama pemain: ")
    riwayat = []
    ronde = 1
    
    bermain = True
    while bermain == True:
        hasil_ronde = main_satu_ronde(nama_pemain, ronde)
        riwayat.append(hasil_ronde)
        
        lagi = input("\nIngin bermain lagi? (ya/tidak): ").lower()
        if lagi != "ya":
            bermain = False
        else:
            ronde = ronde + 1
        
    tampilkan_riwayat(riwayat)
    tampilkan_leaderboard(riwayat)

main()