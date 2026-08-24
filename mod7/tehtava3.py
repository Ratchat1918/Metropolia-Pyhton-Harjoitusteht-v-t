def fuel_converter(gallons):
    liters = gallons * 3,785
    return liters
while True:
    gallons_input = int(input("Syötä gallonmäärä: "))
    if gallons_input<0:
        break
    liters_result = fuel_converter(gallons_input)
    print(liters_result)