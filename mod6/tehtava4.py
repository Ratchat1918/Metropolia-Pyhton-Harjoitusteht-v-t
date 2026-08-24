kaupunki_lista = []
for i in range(5):
    input_kaupunki = str(input("Syötä kaupungin nimi: "))
    kaupunki_lista.append(input_kaupunki)
for i in range(len(kaupunki_lista)):
    print(kaupunki_lista[i])