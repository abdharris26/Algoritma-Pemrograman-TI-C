def pangkat_rekursi(a, b):
    if b == 0:
        return 1
    return a * pangkat_rekursi(a, b-1)
hasil = pangkat_rekursi(2,5)
print(hasil)
    