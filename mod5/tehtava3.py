suurin_numero = 0
pienin_numero = 0
while True:
    number = input("Syota numero: ")
    if number == "" or number == " ":
        break
    elif int(number) >= suurin_numero:
        suurin_numero=int(number)
    elif int(number) <= pienin_numero:
        pienin_numero = int(number)
print(f"Pienin: {pienin_numero} Suurin: {suurin_numero}")