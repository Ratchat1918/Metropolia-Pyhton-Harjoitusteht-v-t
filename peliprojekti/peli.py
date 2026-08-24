import random
name = str(input("Enter name: "))
age = int(input("Enter age: "))
inventaario = []
def lisa_inventarioon(item):
    inventaario.append(item)
def tulosta_inventaario(inventaario):
    for i in range(len(inventaario)):
        print(inventaario[i])
def syo_satunainen_item(inventaario):
    if len(inventaario)!=0:
        item_index = random.randint(0, len(inventaario))
        inventaario.remove(inventaario[item_index])
while True:
    if age<12:
        print("ikä on lian pieni")
        break
    else:
        print("Tervetuloa")
        print(f"{name}, {age}")
        print("Lisätä item inventarioon: 1 Tulostaa itemia: 2 Syö satunaisen item: 3, Lopeta: lopeta")
        command = str(input("Syötä komento: "))
        if command == "lopeta":
            break
        elif command == "1":
            item_input = str(input("Item: "))
            lisa_inventarioon(item_input)
            continue
        elif command == "2":
            tulosta_inventaario(inventaario)
        elif command == "3":
            syo_satunainen_item(inventaario)