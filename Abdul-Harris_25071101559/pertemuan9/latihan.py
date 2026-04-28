# Buatlah sebuah program Python yang berjalan di terminal dengan ketentuan sebagai berikut:

# Program meminta pengguna untuk memasukkan jumlah elemen yang akan dimasukkan ke dalam array.
# Selanjutnya, pengguna memasukkan sejumlah bilangan bulat non-negatif sesuai jumlah yang telah ditentukan, satu per satu.
# Setelah semua elemen dimasukkan, program akan mengurutkan array tersebut menggunakan tiga algoritma pengurutan, yaitu 
# Insertion Sort, Quick Sort dan Counting Sort secara terpisah.
# Program menampilkan hasil pengurutan dari masing-masing algoritma ke layar terminal.
# Input yang diterima hanya bilangan bulat non-negatif (≥ 0). Program harus menangani input yang tidak valid.
# Implementasikan fungsi terpisah untuk Insertion Sort , Quick Sort dan Counting Sort.
# Tampilkan array sebelum dan sesudah diurutkan untuk setiap algoritma.
# 1. Fungsi Insertion Sort (Sesuai Screenshot 1)
jumlah = int(input("masukan jumlah bilangan: "))
array = []
while len(array) < jumlah:
    input_bilangan = int(input("masukan bilangan non negatif: "))
    if input_bilangan < 0:
        print("bilangan tidak boleh negatif")
    else:
        array.append(input_bilangan)
        
print("sebelum")

def insertion_sort(arr):
    n = len(arr)
    for i in range(1, n):
        insert_index = i
        current_value = arr[i]
        for j in range(i - 1, -1, -1):
            if arr[j] > current_value:
                arr[j + 1] = arr[j]
                insert_index = j
            else:
                break
        arr[insert_index] = current_value
    return arr


def partition(array, low, high):
    pivot = array[high]
    i = low - 1
    for j in range(low, high):
        if array[j] <= pivot:
            i += 1
            array[i], array[j] = array[j], array[i]
    array[i+1], array[high] = array[high], array[i+1]
    return i + 1

def quicksort(array, low=0, high=None):
    if high is None:
        high = len(array) - 1
    if low < high:
        pivot_index = partition(array, low, high)
        quicksort(array, low, pivot_index - 1)
        quicksort(array, pivot_index + 1, high)
    return array

# 3. Fungsi Counting Sort
def countingSort(arr):
    if not arr: return arr
    max_val = max(arr)
    count = [0] * (max_val + 1)
    
    while len(arr) > 0:
        num = arr.pop(0)
        count[num] += 1
        
    for i in range(len(count)):
        while count[i] > 0:
            arr.append(i)
            count[i] -= 1
    return arr



# --- FUNGSI UTAMA UNTUK TERMINAL ---

def main():
    print("=== Latihan Pertemuan 9 - Praktikum Alpro ===")
    
    # Validasi Input Jumlah Elemen
    while True:
        try:
            n = int(input("\nMasukkan jumlah elemen yang akan dimasukkan: "))
            if n <= 0:
                print("Masukkan jumlah lebih dari 0.")
                continue
            break
        except ValueError:
            print("Input tidak valid! Harap masukkan angka bulat.")

    # Input Elemen Array
    original_list = []
    for i in range(n):
        while True:
            try:
                val = int(input(f"Masukkan elemen ke-{i+1} (bilangan >= 0): "))
                if val < 0:
                    print("Hanya menerima bilangan bulat non-negatif.")
                else:
                    original_list.append(val)
                    break
            except ValueError:
                print("Input tidak valid! Harap masukkan angka bulat.")

    # Menampilkan Hasil Pengurutan Secara Terpisah
    print("\n" + "="*40)
    print(f"ARRAY AWAL: {original_list}")
    print("="*40)

    # Eksekusi Insertion Sort
    arr_ins = list(original_list) # Copy agar array asli tidak hilang
    print("\n[Insertion Sort]")
    print(f"Sebelum: {original_list}")
    print(f"Sesudah: {insertion_sort(arr_ins)}")

    # Eksekusi Quick Sort
    arr_qui = list(original_list)
    print("\n[Quick Sort]")
    print(f"Sebelum: {original_list}")
    print(f"Sesudah: {quicksort(arr_qui)}")

    # Eksekusi Counting Sort
    arr_cou = list(original_list)
    print("\n[Counting Sort]")
    print(f"Sebelum: {original_list}")
    print(f"Sesudah: {countingSort(arr_cou)}")

if __name__ == "__main__":
    main()