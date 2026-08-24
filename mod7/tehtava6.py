def pizza_worth(diametr, price):
    import math
    pizza_radius= diametr/2
    pizza_area = math.pi * pizza_radius ** 2
    pizza_worth = price / pizza_area
    return pizza_worth
price_input1 = int(input("Enter price: "))
diametr_input1 = int(input("Enter diameter: "))
price_input2 = int(input("Enter price: "))
diametr_input2 = int(input("Enter diameter: "))

price_metre1 = pizza_worth(price_input1, diametr_input1)
price_metre2 = pizza_worth(price_input2, diametr_input2)
if price_metre1>price_metre2:
    print(f"First is a better value")
else:
    print("Sedcond is bettter value")