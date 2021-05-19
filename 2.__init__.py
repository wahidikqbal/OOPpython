class siswa:
    def __init__(self, inputNama, inputHobby):
        self.nama  = inputNama
        self.hobby = inputHobby


siswa = siswa("Homelander","ngeGame")

print(siswa.nama, "hobby nya adalah", siswa.hobby)

#-------> dictionary pada siswa
print(siswa.__dict__)