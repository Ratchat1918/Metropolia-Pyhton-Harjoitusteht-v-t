class Elain:
    elain_maara = 0
    def __init__(self, nimi ,syntyaika, paino):
        Elain.elain_maara = Elain.elain_maara +1
        self.syntyaika = syntyaika
        self.nimi = nimi
        self.paino = paino
    def liikua(self):
        print(f"{self.nimi} liikkuu jonnekin")
    def tulosta_tietoa(self):
        print(f"{self.nimi}, {self.syntyaika}, {self.paino}")
class Ilves(Elain):
    def __init__(self, nimi, syntyaika, paino):
        super().__init__(nimi, syntyaika, paino)
    def kilja(self):
        print("AAAAAAAAAAAAAAAAAAAAAAAAA")
    def tulosta_tietoa(self):
        return super().tulosta_tietoa()
ilves = Ilves("kitty", 2026229, 30)
elain = Elain("saa", 12212, 12)
ilves.tulosta_tietoa()
ilves.liikua()
ilves.kilja()

print(Elain.elain_maara)
#ja hochu domoi ;-; 