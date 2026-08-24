class Julkaisu:
    def __init__(self, nimi):
        self.nimi = nimi

class Kirja(Julkaisu):
    def __init__(self, nimi, kirjoittaja, sivumaara):
        self.kirjoittaja = kirjoittaja
        self.sivumaara = sivumaara
        super().__init__(nimi)
    def tulosta_tiedot(self):
        print(self.nimi, self.kirjoittaja,"Sivua:", self.sivumaara)
class Lehti(Julkaisu):
    def __init__(self, nimi, paatoimittaja):
        self.paatoimittaja = paatoimittaja
        super().__init__(nimi)
    def tulosta_tiedot(self):
            print(self.nimi, self.paatoimittaja)
new_magazine = Lehti("Aku Ankka", " Aki Hyyppä")
new_magazine.tulosta_tiedot()
new_book = Kirja("Hytti n:o 6", "Rosa Liksom", 200)
new_book.tulosta_tiedot()