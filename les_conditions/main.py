#ex01
def pos_neg_null():
    user_nbr = int(input("\nEntrez un chiffre >>> "))
    if user_nbr > 0:
        print(str(user_nbr) + " est positif")
    elif user_nbr < 0:
        print(str(user_nbr) + " est negatif")
    else:
        print(str(user_nbr) + " est NULL")

#pos_neg_null()
#ex02
def paire():
    user_nbr = int(input("\nEntrez un chiffre >>> "))
    if user_nbr % 2 == 0:
        print(str(user_nbr) + " est paire")
    else:
        print(str(user_nbr) + " est impaire")

#paire()
#ex03
def user_is_major():
    user_age = int(input("\nEntrez votre age >>> "))
    if user_age > 17:
        print("Vous etes majeur")
    else:
        print("Vous etes mineur")
    return (user_age)

#user_is_major()
#ex04
def valid_name(str):
    if str.lower() == "alice" or str.lower() == "bob":
        print("Bonjour " + str)
    else:
        print("Bonjour")

def wellcome():
    name = str(input("\nEntrez votre prenom >>> "))
    valid_name(name)

#wellcome()
#ex05
def operation():
    nbr1 = int(input("\nEntrez un chiffre >>> "))
    nbr2 = int(input("Entrez un 2eme chiffre >>> "))
    symbol = str(input("Choisissez l'une de ces operation (+, -, *, /) >>> "))
    if symbol == "+":
        print(nbr1 + nbr2)
    elif symbol == "-":
        print(nbr1 - nbr2)
    elif symbol == "*":
        print(nbr1 * nbr2)
    elif symbol == "/":
        print(nbr1 / nbr2)
    else:
        print("ERROR")
    
#operation()
#bonus01
def connected():
    user_age = user_is_major()
    if user_age < 18:
        print("Revennez dans " + str(18 - user_age) + " ans")
    else:
        print("Vous etes cennectee")

#connected()
#bonus02
def test():
    age = 2023 - int(input("\nEntrez votre annee de naissance >>> "))
    username = str(input("\nEntrez votre prenom >>> "))
    print("\nBonjour " + username + " vous avez " + str(age) + " ans")
    if age > 100:
        print("vous avez une longevite remarquable.")
    elif 66 < age:
        print("Vous etes pensionne.")
    elif 50 <= age < 67:
        print("On se rapproche de la pension, courage plus que " + str(67 - age) + " année avant la pension.")
    elif 18 <= age < 50:
        print("Tu est un adulte.")
    elif 15 < age < 18:
        print("Tu est un ado.")
    elif 13 <= age <= 15:
        print("Tu est un pre-ado.")
    else:
        print("bonjour... Tu est un enfant.")
    
test()