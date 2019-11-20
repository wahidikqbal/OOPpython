class polisi:
    def __init__(self, name, callSign, bidang):
        self.name = name
        self.callSign = callSign
        self.bidang = bidang

class sitipol(polisi):
    def __init__ (self, name):
        super().__init__(name, 12, "Informatika dan Komunikasi")

class sumda(polisi):
    def __init__ (self, name):
        super().__init__(name, 4, "Sumber Daya Manusia")

class reskrim(polisi):
    def __init__(self, name):
        super().__init__(name, 7, "Kriminal")

malang12 = sitipol("Telematika")
malang4  = sumda("Bag Sumda")
malang7  = reskrim("Sat Resrim")


print(malang12.name, "kode", malang12.callSign, "menangani bidang", malang12.bidang)
print(malang4.name, "kode", malang4.callSign, "memangani bidang", malang4.bidang)
print(malang7.name, "kode", malang7.callSign,"memangani bidang", malang7.bidang)
