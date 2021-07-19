class sekolah :
    def __init__(self, name, pelajaran, kelas):
        self.name       = name
        self.pelajaran  = pelajaran
        self.kelas      = kelas

class guru(sekolah) :
    def __init__(self, name, pelajaran, kelas):
        super().__init__(name, pelajaran, kelas)

class murid(sekolah) :
    def __init__(self, name):
        super().__init__(name, "matematika", 12)

kalimat1 = guru("budiono", "IPA", 11)
kalimat2 = murid("andika")


print(kalimat1.name, "mengajar pelajaran", kalimat1.pelajaran, "dikelas", kalimat1.kelas)
print(kalimat2.name, "menerima pelajaran", kalimat2.pelajaran, "dikelas", kalimat2.kelas)