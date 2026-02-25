def bilangan_prima(n):
    prima = []

    for x in range(2,n + 1):
        ini_prima = True

        for y in range(2, x):
            if x % y == 0:
                ini_prima = False
                break
        
        if ini_prima:
            prima.append(x)

    return prima
hasil = bilangan_prima(30)
print(hasil)
