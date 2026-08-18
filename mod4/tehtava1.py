kuha_pituus = float(input("Syötä kuhan pituus: "))
if kuha_pituus<=37:
    puutut_sentit = 37-kuha_pituus 
    print(f"Laske kuhan takaisin, senttia puuttuu: {puutut_sentit}")
else:
    print("Kaikki ok")