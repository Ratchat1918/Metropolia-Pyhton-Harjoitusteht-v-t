import random
random_number = random.randint(1, 10)
while True:
    guess = int(input("Enter your guess of number between 1 and 10: "))
    if guess == random_number:
        print("Oikein")
        break
    elif guess>random_number:
        print("Liian suuri arvaus")
        continue
    elif guess<random_number:
        print("Liian pieni arvaus")
        continue 