number_list = []
while True:
    x = input("Enter number: ")
    if x == "" or x == " ":
        break
    else:
        number_list.append(int(x))
        continue
if len(number_list)<5:
    number_list.sort(reverse=True)
    for x in range(len(number_list)):
        print(number_list[x])
else:
    number_list.sort(reverse=True)
    for x in range(5):
        print(number_list[x])