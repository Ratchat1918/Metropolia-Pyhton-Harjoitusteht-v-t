class Hissi:
    def __init__(self, alimman, ylimman):
        self.alimman = alimman
        self.ylimman = ylimman
        self.nyky_kerros = alimman
    def kerros_ylos(self,kerroksen_maara):
        for i in range(kerroksen_maara):
            self.nyky_kerros+=1
            print(self.nyky_kerros)
    def kerros_alas(self,kerroksen_maara):
            for i in range(kerroksen_maara):
                self.nyky_kerros-=1
                print(self.nyky_kerros)
    def siirry_kerokseen(self, kerros):
        if kerros>self.nyky_kerros:
            kerroksen_maara = kerros-self.nyky_kerros
            self.kerros_ylos(kerroksen_maara)
        elif kerros<self.nyky_kerros:
             kerroksen_maara = self.nyky_kerros-kerros
             self.kerros_alas(kerroksen_maara)
        print(self.nyky_kerros)

class Talo:
    def __init__(self, alimman, ylimman, hissien_maara):
        self.alimman = alimman
        self.ylimman = ylimman
        self.hissien_maara = hissien_maara
        self.hissien_lista = []
        for i in range(hissien_maara):
            new_elevator = Hissi(alimman, ylimman)
            self.hissien_lista.append(new_elevator)
    def aja_hissia(self,hissi_numero, kohdekerros):
        hissi = self.hissien_lista[hissi_numero]
        hissi.siirry_kerokseen(kohdekerros)
    def palohylatys(self):
        print("Palohylätys!")
        for i in range(self.hissien_maara):
            self.hissien_lista[i].siirry_kerokseen(0)
new_home = Talo(0, 10, 3)
new_home.aja_hissia(1, 9)
new_home.palohylatys()