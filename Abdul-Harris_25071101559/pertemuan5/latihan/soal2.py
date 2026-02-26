data_aktivitas = [("Diki", 88), ("Aqul", 45), ("Abid", 92), ("Rehan", 70)] 

for x in data_aktivitas:
    if x[1] > 80:
        print(x[0], "mendapatkan predikat gold")
    elif x[1] < 80 and x[1] > 50:
        print(x[0],"mendapatkan predikat silver")
    else:
        print(x[0],"mendapatkan bronze")
    