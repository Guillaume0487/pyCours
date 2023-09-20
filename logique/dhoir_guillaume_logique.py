# ex01
# ici je verifie simplement si le nombre en parametre
# modulo 2 ne laisse pas de reste (=0), dans ce cas le chiffre est
# divisible par 2, il est donc paire et
# retourne True dans le cas contraire il retourne False
def parite(nbr):
    if nbr % 2 == 0:
        return (True)
    return (False)

# print(parite(0))

# ex02
# celui-la est asser simple aussi, si le nombre en parametre
# est plus grand que 0 alors on set i a la valeur de nbr -1 pour
# plus tard, ensuite on entre dans la boucle while si i est plus
# que 1 car il ne sera jamais utile de faire (nbr * 1)
# plus haut j'ai mis (i = nbr -1) pour pouvoir
# fair si (nbr = 5) 5 *= (i donc 4) apres je decremante i
# apres la boucle recommence avec (nbr = 20) et (i = 3).
# dans le (else: nbr = 1) c'est pour que si (nbr < 0)
# alors (nbr = 1)
# la variable tmp est la que pour le print et n'est pas reelement utile


def factorielle(nbr):
    tmp = nbr
    if nbr > 0:
        i = nbr - 1
        while i > 1:
            nbr *= i
            i -= 1
    else:
        nbr = 1
    print(str(tmp) + "! = " + str(nbr))

# factorielle(3)

# ex04
# ici je divise et arondie au nombre entier le plus bas
# la taille de la chaine de caractere en parametre par
# 2 et stock le resultat dans tmp
# je set i = 1 et j = -1 pour comparer le debut de la liste (i)
# et la fin (j) si la taille de la liste est
# impaire ca n'as pas d'importance, je ne compare
# pas le milleux de la liste avec lui meme


def palindrome(strg):
    tmp = len(strg) // 2
    i = 0
    j = -1
    validation = False
    while i < tmp:
        if strg[i] == strg[j]:
            validation = True
        else:
            validation = False
            break
        i += 1
        j -= 1
    return (validation)


# print(palindrome("level"))

# ex05


def tri(lst):
    for i in range(len(lst)):
        j = i + 1
        while j < len(lst):
            if lst[i] > lst[j]:
                tmp = lst[i]
                lst[i] = lst[j]
                lst[j] = tmp
            j += 1
        i += 1
    print(lst)

# L = [20, 10, 30, 40, 25]
# tri(L)

# ex06


def premier(nbr):
    if nbr == 2:
        return (True)
    tmp = (False)
    for i in range(nbr):
        if i > 1:
            if nbr % i == 0:
                tmp = (False)
                break
            else:
                tmp = (True)
    return (tmp)


def print_prime(borne_inf, borne_sup):
    for i in range(borne_inf, borne_sup):
        if premier(i):
            print(i)

# print_prime(50, 70)
