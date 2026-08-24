import random
from pathlib import Path
from pelaaja import Pelaaja
from huone import Huone
from esine import Esine

key_to_next_room = Esine("Key to the next room", 18.6)
bag_of_holding = Esine("Bag of holding", 0)
starting_room = Huone("Starting room", key_to_next_room)
room2 = Huone("Room 2", bag_of_holding)
final_room = Huone("Final room", None)

rooms = {
    starting_room.nimi: starting_room,
    room2.nimi: room2,
    final_room.nimi: final_room,
}

game_state_path = Path(__file__).parent / "game_state.txt"
with open(game_state_path, "r", encoding="utf-8") as game_state_file:
    lines = game_state_file.readlines()

if len(lines) < 3:
    name = input("Enter name: ")
    age = int(input("Enter age: "))
    new_player = Pelaaja(name, age, starting_room)
else:
    name = lines[0].strip()
    age = int(lines[1].strip())
    sijainti = rooms[lines[2].strip()]
    new_player = Pelaaja(name, age, sijainti)

with open(game_state_path, "w",) as game_state_file:
    game_state_file.write(f"{name}\n{age}\n{new_player.sijainti.nimi}\n")

if new_player.ika < 12:
    print("Ikä on liian pieni")
else:
    intro = Path(__file__).parent / "intro.txt"
    with open(intro, "r") as file:
         for i in file:
            print(i.rstrip())
    while True:
        print(f"{name}, {age}")
        if new_player.sijainti == starting_room:
            print(f"You see a key to the next room")
        ohjeet = Path(__file__).parent / "ohjeet.txt"
        with open(ohjeet, "r") as file:
            for i in file:
                    print(i.rstrip())
        command = input("Syötä komento: ")
        if command == "lopeta":
            break
        elif command == "1":
            if new_player.sijainti.esine is not None:
                new_player.keraa_esine(new_player.sijainti.esine)
                new_player.sijainti.esine = None
            else:
                print("Huoneessa ei ole esinettä.")
        elif command == "2":
            for item in new_player.esineet:
                print(f"Items: \n{item.nimi}")
        elif command == "3":
            if new_player.esineet:
                item = random.choice(new_player.esineet)
                new_player.esineet.remove(item)
                print(f"Poistettiin: {item.nimi}")
        elif command == "4":
            if key_to_next_room in new_player.esineet and new_player.sijainti == starting_room:
                new_player.liikua(room2)
                print(new_player.sijainti)
                with open(game_state_path, "w",) as game_state_file:
                    game_state_file.write(f"{name}\n{age}\n{new_player.sijainti.nimi}\n")
            elif new_player.sijainti == room2:
                new_player.liikua(final_room)
                print(new_player.sijainti)
                with open(game_state_path, "w",) as game_state_file:
                    game_state_file.write(f"{name}\n{age}\n{new_player.sijainti.nimi}\n")
            else:
                print("The door is locked")
        else:
            print("Inventaario on tyhjä.")