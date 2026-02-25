# Contoh match case

hari = 3

match hari:
    case 1:
        print("Senin")
    case 2:
        print("Selasa")
    case 3:
        print("Rabu")
    case _:
        print("Hari tidak valid")
