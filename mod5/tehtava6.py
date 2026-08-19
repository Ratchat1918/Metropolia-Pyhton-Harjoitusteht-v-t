import random
pisteiden_maara=int(input("Syötä piseteiden määrä "))
pisteet_sisala = 0
x= pisteiden_maara
while True:
    if x<=0:
        break
    x_piste = random.uniform(-1,1)
    y_piste = random.uniform(-1,1)
    print(x_piste,y_piste)
    if x_piste**2+y_piste**2<1:
        pisteet_sisala+=1
    x-=1
pi = pisteet_sisala*4/pisteiden_maara
print(f"Pisteet sisalla: {pisteet_sisala} Piin likiarvo: {pi}")