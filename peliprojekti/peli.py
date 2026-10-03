import json
from pelaaja import Pelaaja
from huone import Huone
from esine import Esine
mop = Esine("Mop", "Your trusty mop, the extension of your very soul")
storage_key = Esine("Storage Key", "A small metalic key meant for opening a storage room with your stuff")
bucket = Esine("Bucket", "Wooden bucket you use to keep your mop wet and floors human remains free")
water_bucket = Esine("Water Bucket", "same bucket but now actually usable")
trash = Esine("Trash", "A bunch of trash, maps, bented daggers, used up potion bottles")
item_list = [mop, bucket, storage_key, water_bucket]

entrance_room = Huone("Entrance", [trash], "Before you are two strong double gates, beyond them are the stairs leading into the dungeone")
staircase =Huone("Staircase", [], "The stairs are somewhat slippery and it smells of moss in here, pretty much up to code")
fountain_room = Huone("Fountain Room", [], "You see a functional fountain before you, beyond it you see a way into the storage room where your cleaning supplies usually are")
storage_room = Huone("Storage Room", [bucket],"Before you is a door into the storage room, you try to open it, but it does not even latch")
exit_room = Huone("Exit", [], "It's an exit, it looks like an unremarkable wooden door")
room_list = [entrance_room, staircase, fountain_room, storage_room, exit_room]

def print_instruction():
    try:
        with open("ohjeet.txt", "r") as instructuion_file:
            instructuion_text = instructuion_file.readlines()
            for line in instructuion_text:
                print(line)
    except FileNotFoundError:
        print("file ohjeet.txt does not exist")

def find_current_room(player_obj):#used to find current room in order to move player into next or previous room
    current_room = ""
    for room in room_list:
        if player_obj.sijainti == room.nimi:
            current_room = room
            break
    return current_room

def find_item(player_item):#used to find current room in order to move player into next or previous room
    current_item = ""
    for item in item_list:
        if player_item == item.nimi:
            current_item = item
            break
    return current_item

def examine_room(player_obj):#hoooly repeating code
    player_location = player_obj.sijainti
    match player_location:
        case "Entrance":
            print("You notice there's quite a bit of rubish around the gates of the dungeon.")
            print("1. Pick up the trash\n2. Go back to previous option")
            choice = int(input("Enter your choice: "))
            if choice == 1:
                print("You go around the area meticulously picking up trash")
                player_obj.keraa_esine("Trash")
            elif choice == 2:
                pass
            else:
                print("Unknown option, choose a valid option")
        case "Staircase":
            print("You notice a small halflings body laying upon the bottom of the stairs, poor bastard must have triggered a trap")
            print("1. Examine the body\n2. Go back to previous option")
            choice = int(input("Enter your choice: "))
            if choice == 1:
                print("You turn over the body and see the halfling clutching something in his hand")
                player_obj.keraa_esine("Storage Key")
            elif choice == 2:
                pass
            else:
                print("Unknown option, choose a valid option")
        case "Fountain Room":
            print("You notice besides the fountain there's a pool of blood and trash cans, conveniently marked for different trash types")
            if "Trash" in player_obj.inventaario and "Bucket" in player_obj.inventaario:
                print("1. Throw away the trash\n2. Pour some water into the bucket\n3. Go back to previous option")
                choice = int(input("Enter your choice: "))
                if choice == 1:
                    print("You throw away the trash into the correct trash types, you feel great!")
                    player_obj.inventaario.remove("Trash")
                    player_obj.entranceObjective = True
                elif choice == 2:
                    print("You put you bucket under the ")
                    player_obj.inventaario.remove("Bucket")
                    player_obj.keraa_esine("Water Bucket")
                    player_obj.fountainRoomObjective = True
                elif choice == 3:
                    pass
                else:
                    print("Unknown option, choose a valid option")
            elif "Trash" in player_obj.inventaario and "Bucket" not in player_obj.inventaario:
                print("1. Throw away the trash\n2. Go back to previous option")
                choice = int(input("Enter your choice: "))
                if choice == 1:
                    print("You throw away the trash into the correct trash types, you feel great!")
                    player_obj.inventaario.remove("Trash")
                    player_obj.entranceObjective = True
                elif choice == 2:
                    pass
                else:
                    print("Unknown option, choose a valid option")
            elif "Bucket" in player_obj.inventaario and "Trash" not in player_obj.inventaario:
                print("1. Pour some water into the bucket\n2. Go back to previous option")
                choice = int(input("Enter your choice: "))
                if choice == 1:
                    print("You put you bucket under the ")
                    player_obj.inventaario.remove("Bucket")
                    player_obj.keraa_esine("Water Bucket")
                elif choice == 2:
                    pass
                else:
                    print("Unknown option, choose a valid option")
            elif "Water Bucket" in player_obj.inventaario and "Trash" not in player_obj.inventaario:
                print("1. Clean up the blood\n2. Go back to previous option")
                choice = int(input("Enter your choice: "))
                if choice == 1:
                    print("You take your time cleaning the blood of the floor")
                    player_obj.fountainRoomObjective = True
                elif choice == 2:
                    pass
                else:
                    print("Unknown option, choose a valid option")
            elif "Water Bucket" in player_obj.inventaario and "Trash" in player_obj.inventaario:
                print("1. Throw away the trash\n2. Clean up the blood\n3. Go back to previous option")
                choice = int(input("Enter your choice: "))
                if choice == 1:
                    print("You throw away the trash into the correct trash types, you feel great!")
                    player_obj.inventaario.remove("Trash")
                    player_obj.entranceObjective = True
                elif choice == 2:
                    print("You take your time cleaning the blood of the floor")
                    player_obj.fountainRoomObjective = True
                elif choice == 3:
                    pass
                else:
                    print("Unknown option, choose a valid option")
        case "Storage Room":
            print("The storage is cramped but, you see your bucket as well as an exit")
            if "Storage Key" in player_obj.inventaario:
                print("1. Open the storage room with your key\n2. Go back to previous option")
                choice = int(input("Enter your choice: "))
                if choice == 1:
                    print("You put you bucket under the ")
                    player_obj.inventaario.remove("Storage Key")
                    player_obj.keraa_esine("Bucket")
                    storage_room.kuvaus = "The storage is cramped but, you see your bucket as well as an exit"
                elif choice == 2:
                    pass
                else:
                    print("Unknown option, choose a valid option")
        case "Exit":
            print("It's an exit, it looks like an unremarkable wooden door")
        case _:
            print("Unkown room")

def save_game(player_obj):
    player_save_data_object = {
            "name": player_obj.nimi,
            "age": player_obj.ika,
            "location": player_obj.sijainti,
            "iventory": player_obj.inventaario,
            "entranceObjective": player_obj.entranceObjective,
            "fountainRoomObjective": player_obj.fountainRoomObjective
        }
    with open("game_state.txt", "w") as game_state_file:
        json.dump(player_save_data_object, game_state_file)

def print_ending(player_obj):
    if player_obj.entranceObjective == False and player_obj.fountainRoomObjective == False:
        print("Ending 1")
    elif player_obj.entranceObjective == True and player_obj.fountainRoomObjective == False:
        print("Ending 2")
    elif player_obj.entranceObjective == False and player_obj.fountainRoomObjective == True:
        print("Ending 3")

while True:
    print("Enter number according to your choice")
    print("1. New game\n2. Continue Game")
    start_choice = (input("Enter choice: "))
    if int(start_choice) == 1:
        with open("game_state.txt", "w") as game_state_file:
            json.dump({}, game_state_file)
        with open("game_state.txt", "r") as game_state_file:
            game_state_info = json.load(game_state_file)
        break
    elif int(start_choice) == 2:
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
    player_obj = Pelaaja(name_input, age_input, "Entrance", ["Mop"], False, False)
    player_save_data_object = {
        "name": name_input,
        "age": age_input,
        "location": entrance_room.nimi,
        "iventory": ["Mop"],
        "entranceObjective": False,
        "fountainRoomObjective": False
    }
    with open("game_state.txt", "w") as game_state_file:
        json.dump(player_save_data_object, game_state_file)#creates player object and saves it in a text file
else:
    name = game_state_info["name"]
    age = game_state_info["age"]
    location = game_state_info["location"]
    inventory = game_state_info["iventory"]
    entranceObjective = game_state_info["entranceObjective"]
    fountainRoomObjective = game_state_info["fountainRoomObjective"]
    player_obj = Pelaaja(name, age, location, inventory, entranceObjective, fountainRoomObjective)
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
    match player_obj.sijainti:
        case "Entrance":
            print(entrance_room.kuvaus)
        case "Staircase":
            print(staircase.kuvaus)
        case "Fountain Room":
            print(fountain_room.kuvaus)
        case "Storage Room":
            print(storage_room.kuvaus)
        case "Exit":
            print(exit_room.kuvaus)
    print_instruction()
    choice = int(input("Enter choice: "))
    match choice:
        case 0:
            print("Stoping and saving the game")
            save_game(player_obj)
            game_on = False
        case 1:
            examine_room(player_obj)
        case 2:
            current_room = find_current_room(player_obj)
            current_room_index = room_list.index(current_room)
            if current_room.nimi == "Exit":
                print("Do you wish to leave now?")
                print("1. Leave now\n 2. Go to previous room")
                choice = int(input("Enter choice: "))
                if choice == 2:
                    player_obj.liikua(room_list[current_room_index-1].nimi)
                elif choice == 1:
                    print_ending(player_obj)
                    game_on = False
                else:
                    print("Unkown command please choose a valid command")
            else:
                player_obj.liikua(room_list[current_room_index+1].nimi)
        case 3:
            current_room = find_current_room(player_obj)
            current_room_index = room_list.index(current_room)
            if current_room.nimi == "Entrance":
                print("There's nowhere to go, but forward")
            else:
                print("You decided to check previous room once more")
                player_obj.liikua(room_list[current_room_index-1].nimi)
        case 4:
            print("You take a look in your bag")
            for item in player_obj.inventaario:
                print(item)
        case _:
            print("Unkown command please choose a valid command")