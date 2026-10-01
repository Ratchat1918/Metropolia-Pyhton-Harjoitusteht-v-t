import json
from pelaaja import Pelaaja
from huone import Huone
from esine import Esine

storage_key = Esine("Storage Key", "a small metalic key meant for opening a storage room with your stuff")
bucket = Esine("Bucket", "wooden bucket you use to keep your mop wet and floors human remains free")
water_bucket = Esine("Water Bucket", "same bucket but now actuallu usable")
corridor =Huone("Corridor", [], "There's a long ")
entrance_room = Huone("Entrance", [], "The entrance into the dungeone looks like always ")
storage_room = Huone("Storage Room", [], "The entrance into the dungeone looks like always ")
exit_room = Huone("Exit", [], "Small room ")
room_list = [entrance_room]

def print_instruction():
    try:
        with open("ohjeet.txt", "r") as instructuion_file:
            instructuion_text = instructuion_file.readlines()
            for line in intro_text:
                print(line)
    except FileNotFoundError:
        print("file ohjeet.txt does not exist")

while True:
    print("Enter number according to your choice")
    print("1. New game\n2. Continue Game")
    start_choice = int(input("Enter choice: "))
    if start_choice == 1:
        with open("game_state.txt", "w") as game_state_file:
            json.dump({}, game_state_file)
        with open("game_state.txt", "r") as game_state_file:
            game_state_info = json.load(game_state_file)
        break
    elif start_choice == 2:
        try:
            with open("game_state.txt", "r") as game_state_file:
                game_state_info = json.load(game_state_file)
        except FileNotFoundError:
            print("save not found, creating new game")
            with open("game_state.txt", "w") as game_state_file:
                json.dump({}, game_state_file)
            with open("game_state.txt", "r") as game_state_file:
                game_state_info = json.load(game_state_file)
        break
    else:
        print("Unknown option, choose a valid option")

if len(game_state_info) < 3:
    name_input = input("Enter name: ")
    age_input = int(input("Enter age: "))
    player_obj = Pelaaja(name_input, age_input, "Entrance", [])
    player_save_data_object = {
        "name": name_input,
        "age": age_input,
        "location": "Entrance",
        "iventory": [],
        "entranceObjective": False,
        "secondRoomObjective": False,
        "storageRoomObjective": False,
        'exitRoomObjective': False
    }
    with open("game_state.txt", "w") as game_state_file:
        json.dump(player_save_data_object, game_state_file)#creates player object and saves it in a text file
else:
    name = game_state_info["name"]
    age = game_state_info["age"]
    location = game_state_info["location"]
    inventory = game_state_info["iventory"]
    player_obj = Pelaaja(name, age, location, inventory )
if int(player_obj.ika) < 12:
    print("You are too young to play this.\nCome back when you're older")#loads player info and creates player object with it
else:
    with open("intro.txt", "r") as intro_file:
        intro_text = intro_file.readlines()
        for line in intro_text:
            print(line)
    print("Welcome!",player_obj.nimi)

game_on = True

while game_on:
    if player_obj.sijainti == "Entrance":
        print(entrance_room.kuvaus)
    print_instruction()
    choice = int(input("Enter choice: "))
    if 