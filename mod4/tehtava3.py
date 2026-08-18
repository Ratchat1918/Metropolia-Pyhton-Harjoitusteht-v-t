sukupuoli = str(input("Sukupoli: "))
hm_arvo = int(input("hm arvo: "))
if sukupuoli=="mies":
    if hm_arvo>195:
        print("korkea")
    elif hm_arvo<134:
        print("alhainen")
    elif hm_arvo<=195 and hm_arvo>=134:
        print("normali")
elif sukupuoli=="nainen":
    if hm_arvo>175:
        print("korkea")
    elif hm_arvo<117:
        print("alhainen")
    elif hm_arvo<=175 and hm_arvo>=117:
        print("normali")