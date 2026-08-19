name = str(input("Enter name: "))
age = int(input("Enter age: "))
while True:
    if age<12:
        print("ikä on lian pieni")
        break
    else:
        print("Tervetuloa")
        print(f"{name}, {age}")
        command = str(input("Syötä komento: "))
        if command == "lopeta":
            break
        elif command == "meow":
            print("bark")
            continue