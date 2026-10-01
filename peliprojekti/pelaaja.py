class Pelaaja:
    def __init__(self, nimi, ika, sijainti, inventaario):
        self.nimi = nimi
        self.ika = int(ika)
        self.inventaario = inventaario
        self.sijainti = sijainti
    def liikua(self, kohde):
        self.sijainti = kohde
        print(f"Nykyinen sijainti: {self.sijainti}")
    def keraa_esine(self, item):
        if item is not None:
            self.esineet.append(item)
            print(f"Kerättiin: {item.nimi}")