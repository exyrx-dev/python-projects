
menu ={
    "Nescafe": 12,
    "Nesnes": 12,
    "Tea": 13,
    "Soda": 12
}
product = input("Hello sir \nWhat Would you like to drink ? We have (Nescafe/Tea/Nesnes/Soda):  ")

product = product.capitalize()

price = menu[product]

quantity = int(input("How much do you want ? "))

total = price * quantity

print(f"total is {total} DH \nHappy Good Day.")