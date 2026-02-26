ukm_coding = {"Andi", "Budi", "Caca", "Deni"}  
ukm_robotik = {"Caca", "Deni", "Euis", "Fafa"} 
#soal 1
ukm_coding_saja = ukm_coding - ukm_robotik
print(ukm_coding_saja)

#soal 2
mahasiswa_unik = ukm_coding | ukm_robotik
print(mahasiswa_unik)

#soal 3
print("Andi" in ukm_robotik)
