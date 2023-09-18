#ex01
def pos_neg_null():
    user_nbr = int(input("\nEntrez un chiffre >>> "))
    if user_nbr > 0:
        print(str(user_nbr) + " est positif")
    elif user_nbr < 0:
        print(str(user_nbr) + " est negatif")
    else:
        print(str(user_nbr) + " est NULL")

pos_neg_null()
#ex02
def pair():
    user_nbr = int(input("\nEntrez un chiffre >>> "))
    if user_nbr % 2 == 0:
        print(str(user_nbr) + " est paire")
    else:
        print(str(user_nbr) + " est impaire")

pair()
#ex03
def user_is_major():
    user_age = int(input("\nEntrez votre age >>> "))
    if user_age > 17:
        print("Vous etes majeur")
    else:
        print("Vous etes mineur")

user_is_major()
#ex04
def valid_name(str):
    if str.lower() == "alice" or str.lower() == "bob":
        print("Bonjour " + str)
    else:
        print("Bonjour")

def wellcome():
    name = str(input("\nEntrez votre prenom >>> "))
    valid_name(name)

wellcome()
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
    
operation()