vuoden_kaudet = ("joulukuu", "tammikuu", "helmikuu", "maaliskuu, huhtikuu", "toukukuu","kesäkuu", "heinäkuu", "elokuu", "syyskuu", "lokakuu", "marraskuu")
kausi_input = int(input("Kuukauden numero: "))
print(vuoden_kaudet[kausi_input-1])
if vuoden_kaudet[kausi_input-1]== "joulukuu" or vuoden_kaudet[kausi_input-1] == "tammikuu" or vuoden_kaudet[kausi_input-1]=="helmikuu":
    print("talvi")
elif vuoden_kaudet[kausi_input-1]== "maaliskuu" or vuoden_kaudet[kausi_input-1] == "huhtikuu" or vuoden_kaudet[kausi_input-1]=="toukukuu":
    print("kevät")
elif vuoden_kaudet[kausi_input-1]== "kesäkuu" or vuoden_kaudet[kausi_input-1] == "heinäkuu" or vuoden_kaudet[kausi_input-1]=="elokuu":
    print("kesä")
elif vuoden_kaudet[kausi_input-1]== "syyskuu" or vuoden_kaudet[kausi_input-1] == "lokakuu" or vuoden_kaudet[kausi_input-1]=="marraskuu":
    print("kevat")
else:
    print("nsvnjks")