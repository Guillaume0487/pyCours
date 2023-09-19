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
