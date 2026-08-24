import random

class Auto:
    def __init__(self, rekestritunnus, huippunopeus, nyky_nopeus=0, kuljettu_matka=0):
        self.rekestritunnus = rekestritunnus
        self.huippunopeus = huippunopeus
        self.nyky_nopeus = nyky_nopeus
        self.kuljettu_matka = kuljettu_matka
    def kiihtya(self, nopeus_muutos):
        if nopeus_muutos<=self.huippunopeus:
            if self.nyky_nopeus+nopeus_muutos<=0:
                self.nyky_nopeus = 0
            elif self.nyky_nopeus +nopeus_muutos>=self.huippunopeus:
                self.nyky_nopeus =self.huippunopeus
            else:
                self.nyky_nopeus = self.nyky_nopeus + nopeus_muutos
    def kulje(self, tunnit):
        uusi_matka = self.nyky_nopeus * tunnit
        self.kuljettu_matka+=uusi_matka

class Sahkoauto(Auto):
    def __init__(self, rekestritunnus, huippunopeus,akkukapasiteetti, nyky_nopeus=80, kuljettu_matka=0):
        self.akkukapasiteetti = akkukapasiteetti
        super().__init__(rekestritunnus, huippunopeus, nyky_nopeus, kuljettu_matka)
    def kiihtya(self, nopeus_muutos):
        return super().kiihtya(nopeus_muutos)
    def kulje(self, tunnit):
        return super().kulje(tunnit)

class Poltomootoriauto(Auto):
    def __init__(self, rekestritunnus, huippunopeus,bensatanki, nyky_nopeus=60, kuljettu_matka=0):
        self.bensatanki = bensatanki
        super().__init__(rekestritunnus, huippunopeus, nyky_nopeus, kuljettu_matka)
    def kiihtya(self, nopeus_muutos):
        return super().kiihtya(nopeus_muutos)
    def kulje(self, tunnit):
        return super().kulje(tunnit)

new_electric = Sahkoauto("ABC-15", 180, 52.5)
new_fuel = Poltomootoriauto("ACD-123", 165, 32.3)
for i in range(3):
    new_electric.kiihtya(random.randint(10,15))
    new_electric.kulje(1)
    new_fuel.kiihtya(random.randint(10,15))
    new_fuel.kulje(1)
print(new_electric.rekestritunnus, new_electric.kuljettu_matka, new_fuel.rekestritunnus, new_fuel.kuljettu_matka)