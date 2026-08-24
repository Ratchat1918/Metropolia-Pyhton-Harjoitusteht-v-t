input_luku = int(input("Syötä kokonaisluvun: "))
alkuluku_boolean = True
for i in range(input_luku):
    dived_by = int(i+1)
    if input_luku % dived_by == 0 and dived_by !=1 and dived_by !=input_luku:
        alkuluku_boolean = False
print(alkuluku_boolean)