class polisi:
    def __init__(self, name, callSign, bidang):
        self.name = name
        self.callSign = callSign
        self.bidang = bidang


class sitipol(polisi):
    def __init__(self, name):
        super().__init__(name, 12, "Informatika dan Komunikasi")

    def info (self):
        print(self.name, "kode", self.callSign,"menangani bidang", self.bidang)

class sumda(polisi):
    def __init__(self, name):
        super().__init__(name, 4, "Sumber Daya Manusia")

    def info(self):
        print("sedangkan", self.name, "kode", self.callSign,
              "menangani bidang", self.bidang)

class reskrim(polisi):
    def __init__(self, name):
        super().__init__(name, 7, "Kriminal")
    def info(self):
        print("kemudian", self.name, "kode", self.callSign,
              "menangani bidang", self.bidang)

malang12 = sitipol("Telematika,")
malang4 = sumda("Bag Sumda,")
malang7 = reskrim("Sat Resrim,")


malang12.info()
malang4.info()
malang7.info()