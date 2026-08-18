leiviskat = float(input("Anna leiviskät: "))
naulat = float(input("Anna naulat: "))
luodit = float(input("Anna luodit "))

leiviskat_gramm = leiviskat*20*32*13.5
naulat_gramm = naulat*32*13.5
luodit_gramm = luodit*13.5
gramm_summa = leiviskat_gramm + naulat_gramm + luodit_gramm
kilogramit = gramm_summa/1000
kilogramit = int(kilogramit)
gramm_jaljella = gramm_summa - kilogramit*1000

print(f"Massa nykymittojen mukaan\n{kilogramit} kilogrammaa {gramm_jaljella} grammaa")