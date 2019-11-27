#Bagaimana jika mempunyai method dalam kelas yang sama???

class kelas_A:
    def show(self):
        print(self.name, "ada di kelas A")

class kelas_B:
    def show(self):
        print(self.name, "ada di kelas B")

class kelas(kelas_A, kelas_B): #mengambil inherittance dari kelas_A dan kelas_B
    def __init__(self, name):
        self.name = name
        print(self.name, "adalah siswa")

siswa1 = kelas("ucok")
siswa2 = kelas("andi")


siswa1
siswa1.show()

#help(siswa1)  #untuk mengetahui method dari kelas manakah yg dipakai jika name methodnya sama

siswa2
siswa2.show() #siswa2 salah kelas, karena yg dipakai oleh class kelas adalah metod turunan dari kelas_A terlebih dahulu