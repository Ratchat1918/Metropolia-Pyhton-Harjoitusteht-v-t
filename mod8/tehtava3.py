icao_kodit = {
    "ADDE": "Thomas C Russel Field",
    "AGAF": "Afutara airport",
}
while True:
    print("Syöttää uuden lentoaseman: 1, hakea lentoaseman: 2, lopetta: 3 ") 
    choice_input = int(input("Vaihtoehto: "))
    if choice_input == 3:
        break
    elif choice_input == 1:
        icao_koodi_input= str(input("ICAO koodi: "))
        lentoasema_input = str(input("Lentoasemam nimi: "))
        icao_kodit[icao_koodi_input] = lentoasema_input
        print(icao_kodit)
    elif choice_input == 2:
        koodihaku_input = str(input("Syötä ICAO koodi: "))
        print(icao_kodit[koodihaku_input])