password = "rules"
account = "python"
while True:
    entered_account = str(input("Enter account: "))
    entered_password = str(input("Enter password: "))
    if entered_account == account and entered_password == password:
        print('Tervetuloa')
        break
    else:
        print("Pääsy evätty")