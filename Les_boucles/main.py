# ex01
def ingredient():
    L = ["tomate", "patate", "carotte", "oeuf", "boeuf"]
    for e in L:
        print(e)

# ingredient()
# ex02


def print_nbr():
    nbr = int(input("\nEntrez un chiffre >>> "))
    for i in range(nbr + 1):
        print(i)

# print_nbr()
# ex03


def print_lettre():
    strg = "Wellcome"
    for e in strg:
        print(e, end="")
    print("\n")

# print_lettre()
# ex04


def hamid_break():
    L = ["Jean", "Stephane", "Hamid", "Christine", "Marie"]
    for e in L:
        if e == "Hamid":
            break
        print(e)

# hamid_break()
# ex05


def hamid_continue():
    L = ["Jean", "Stephane", "Hamid", "Christine", "Marie"]
    for e in L:
        if e == "Hamid":
            continue
        print(e)

# hamid_continue()
# ex06


def incremante():
    i = 8
    while i < 18:
        i += 1
        print(i)


# incremante()
# ex07


def decremante():
    i = 18
    while i > 0:
        i -= 1
        print(i)


# decremante()
# bonus01


def ask_login():
    user_login = str(input("\nNom d'utilisateur : "))
    return (user_login)


def ask_password():
    user_password = str(input("Mot de passe : "))
    return (user_password)


def singin():
    login = "Guillaume"
    password = "password"
    user_login = ask_login()
    user_password = ask_password()
    while user_login != login and user_password != password:
        user_login = ask_login()
        user_password = ask_password()
    print("Bienvenu " + user_login + " vous êtes connecté")

# singin()
# bonus02


def add_word(lst):
    ask = str(
        input("\nVoulez vous ajouter un mot dans la liste ? (y/n) >>> ")).lower()
    if len(ask) < 0 or len(ask) > 1 or 'n' != ask != 'y':
        print("Caratere invalide")
        return (add_word(lst))
    elif ask == 'y':
        lst.append(str(input("Entrez le mot a ajouter >>> ")))
        return (add_word(lst))
    else:
        print(lst)


# L = []
# add_word(L)
