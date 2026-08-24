prev_nimi = ""
nyky_nimi = ""
nimi_lista = []
while True:
    nimi_input = str(input("Syötä nimen:"))
    if nimi_input == "" or nimi_input == " ":
        break
    nimi_lista.append(nimi_input)
    prev_nimi = nyky_nimi
    nyky_nimi = nimi_input
    if prev_nimi=="" or prev_nimi== " ":
        print(nyky_nimi)
    else:
        print(f"Aiemmin syötetty nimi: {prev_nimi}, Uusi nimi: {nyky_nimi}")
nimi_lista.sort()
for nimi in nimi_lista:
    print(nimi)