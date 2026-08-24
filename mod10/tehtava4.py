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
auto_lista = [
    Auto("ABC-123", 142),
    Auto("ABC-124", 142),
    Auto("ABC-124", 142),
    Auto("ABC-125", 142),
    Auto("ABC-126", 142),
    Auto("ABC-127", 142),
    Auto("ABC-128", 142),
    Auto("ABC-129", 142),
    Auto("ABC-130", 142),
    Auto("ABC-131", 142),
    Auto("ABC-132", 142),
    Auto("ABC-132", 142)
]
class Suuri_romurali:
    def __init__(self, auto_lista, matka):
        self.auto_lista = auto_lista
        self.matka = matka
        self.tunnit = 0
    def tunti_kuulu(self):
        for auto in self.auto_lista:
            auto.kiihtya(random.randint(10,15))
            auto.kulje(1)
            self.tunnit+=1
    def tulosta_tilanne(self):
        if self.tunnit>=10:
            self.tunnit = 0
            for auto in self.auto_lista:
                print(auto.rekestritunnus, auto.nyky_nopeus, auto.kuljettu_matka)
    def kilpaiu_ohi(self):
        for auto in auto_lista:
            if auto.kuljettu_matka>=8000:
                print(f"Voittaja: {auto.rekestritunnus}")
                return True
new_race = Suuri_romurali(auto_lista, 8000)
while True:
    new_race.tunti_kuulu()
    new_race.tulosta_tilanne()
    if new_race.kilpaiu_ohi()==True:
        break