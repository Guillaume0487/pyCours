# ex01
def addition(nbr1, nbr2):
    return (nbr1 + nbr2)

# print(addition(1, 9))
# ex02
def soustraction(nbr1, nbr2):
    return (nbr1 - nbr2)

# print(soustraction(4, 2))
# ex03
def multiplication(nbr1, nbr2):
    return (nbr1 * nbr2)

# print(multiplication(5, 2))
# ex04
def division(nbr1, nbr2):
    return (nbr1 / nbr2)

# print(division(10, 5))
# ex05
def calcul():
    nbr1 = int(input("\nEntrez un chiffre >>> "))
    symbol = str(input("Choisissez l'une de ces operation (+, -, *, /) >>> "))
    nbr2 = int(input("Entrez un 2eme chiffre >>> "))
    if symbol == "+":
        print(str(nbr1) + " " + symbol + " " + str(nbr2) + " = " + str(nbr1 + nbr2))
    elif symbol == "-":
        print(str(nbr1) + " " + symbol + " " + str(nbr2) + " = " + str(nbr1 - nbr2))
    elif symbol == "*":
        print(str(nbr1) + " " + symbol + " " + str(nbr2) + " = " + str(nbr1 * nbr2))
    elif symbol == "/":
        print(str(nbr1) + " " + symbol + " " + str(nbr2) + " = " + str(nbr1 / nbr2))
    else:
        print("ERROR")

# calcul()
# ex06
def capitalize_bis(strg):
    lst = []
    for e in strg:
        lst.append(e)
    for i in range(len(strg)):
        if i == 0:
            lst[i] = lst[i].upper()
        else:
            lst[i] = lst[i].lower()
    return ("".join(lst))


# print(capitalize_bis("gUILLAUME"))
# ex07
def password():
    user_password = str(input("\nMot de passe >>> "))
    if user_password != "password":
        print("Mot de passe incorrect")
        return (password())
    print("\n                 @@@@@@@@@@@@@@@@@@@@@@@@")
    print("                 @       Bienvenue      @")
    print("                 @@@@@@@@@@@@@@@@@@@@@@@@\n")


password()
