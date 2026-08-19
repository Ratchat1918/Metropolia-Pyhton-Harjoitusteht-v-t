import random
kuutio_maara = int(input("Syötä arpakuutioiden määrä: "))
kuutia_summa = 0
for x in range(kuutio_maara):
    numero = random.randint(1,6)
    kuutia_summa+=numero
print(f"Kuutio summa: {kuutia_summa}")