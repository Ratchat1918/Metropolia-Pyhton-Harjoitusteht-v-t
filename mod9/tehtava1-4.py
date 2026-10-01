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
    Auto("ABC-1", random.randint(100,200)),
    Auto("ABC-2", random.randint(100,200)),
    Auto("ABC-3", random.randint(100,200)),
    Auto("ABC-4", random.randint(100,200)),
    Auto("ABC-5", random.randint(100,200)),
    Auto("ABC-6", random.randint(100,200)),
    Auto("ABC-7", random.randint(100,200)),
    Auto("ABC-8", random.randint(100,200)),
    Auto("ABC-9", random.randint(100,200)),
    Auto("ABC-10", random.randint(100,200))
]
x = True
while x:
    for auto in auto_lista:
        auto.kiihtya(random.randint(10,15))
        auto.kulje(1)
        print(f"Reksestritunnus: {auto.rekestritunnus}, Auton matka: {auto.kuljettu_matka}, Nopeus: {auto.nyky_nopeus}")
        if auto.kuljettu_matka>=10000:
            x = False
            break