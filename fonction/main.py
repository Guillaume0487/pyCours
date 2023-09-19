# def addition(nbr1, nbr2):
#     return (nbr1 + nbr2)

# def soustraction(nbr1, nbr2):
#     return (nbr1 - nbr2)

# def multiplication(nbr1, nbr2):
#     return (nbr1 * nbr2)

# def division(nbr1, nbr2):
#     return (nbr1 / nbr2)

# print(addition(1, 9))
# print(soustraction(4, 2))
# print(multiplication(5, 2))
# print(division(10, 5))

# def calcul():
#     nbr1 = int(input("\nEntrez un chiffre >>> "))
#     symbol = str(input("Choisissez l'une de ces operation (+, -, *, /) >>> "))
#     nbr2 = int(input("Entrez un 2eme chiffre >>> "))
#     if symbol == "+":
#         print(str(nbr1) + " " + symbol + " " + str(nbr2) + " = " + str(nbr1 + nbr2))
#     elif symbol == "-":
#         print(str(nbr1) + " " + symbol + " " + str(nbr2) + " = " + str(nbr1 - nbr2))
#     elif symbol == "*":
#         print(str(nbr1) + " " + symbol + " " + str(nbr2) + " = " + str(nbr1 * nbr2))
#     elif symbol == "/":
#         print(str(nbr1) + " " + symbol + " " + str(nbr2) + " = " + str(nbr1 / nbr2))
#     else:
#         print("ERROR")
    
# calcul()

def capitalize_bis(strg):
    new_str = []
    new_str.append(strg[0].upper())
    
    for i in len(strg):
        new_str.append(strg[i + 1].lower())
    print(strg)
    return ("".join(new_str))

test = "test"
test = capitalize_bis(test)
print(test)