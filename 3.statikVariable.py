class kelas:
    #statik Variable
    jumlahSiswa = 0
    def __init__(self, inputNoAbsen, inputNama, inputHobby):
        self.nama  = inputNama
        self.hobby = inputHobby
        self.absen = inputNoAbsen
        kelas.jumlahSiswa += 1
        print(inputNama, "hadir!!!")
        print("no Absen", inputNoAbsen, ",", "nama", inputNama, ",", "hobby", inputHobby)
 
siswa1 = kelas(1, "Homelander", "ngeGame")
siswa2 = kelas(2, "aTrain", "lari-lari")
print("jumlah siswa adalah" , kelas.jumlahSiswa)