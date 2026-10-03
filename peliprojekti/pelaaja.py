class Pelaaja:
    def __init__(self, nimi, ika, sijainti, inventaario, entranceObjective, fountainRoomObjective):
        self.nimi = nimi
        self.ika = int(ika)
        self.inventaario = inventaario
        self.sijainti = sijainti
        self.entranceObjective = entranceObjective
        self.fountainRoomObjective = fountainRoomObjective
    def liikua(self, kohde):
        self.sijainti = kohde
    def keraa_esine(self, item):
        if item is not None:
            self.inventaario.append(item)
            print(f"Picked up: {item}")