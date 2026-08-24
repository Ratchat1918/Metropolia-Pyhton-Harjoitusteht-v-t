class Pelaaja:
    def __init__(self, nimi, ika, sijainti):
        self.nimi = nimi
        self.ika = ika
        self.esineet = []
        self.sijainti = sijainti
    def liikua(self, kohde):
        self.sijainti = kohde
        print(f"Nykyinen sijainti: {self.sijainti}")
    def keraa_esine(self, item):
        if item is not None:
            self.esineet.append(item)
            print(f"Kerättiin: {item.nimi}")