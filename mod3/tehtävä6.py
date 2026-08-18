import random
komlee_numero_koodi = ""
nelja_numero_koodi = ""
for x in range(3):
    random_numero = random.randint(0,9)
    komlee_numero_koodi+=str(random_numero)
for x in range(4):
    random_numero = random.randint(1,6)
    nelja_numero_koodi+=str(random_numero)
print(f"kolmenumeroinen koodi: {komlee_numero_koodi} elinumeroinen koodi: {nelja_numero_koodi}")