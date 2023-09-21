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
# je set i = 1 et j = -1 pour comparer le debut de la chaine (i)
# et la fin (j) si la taille de la chaine est
# impaire ca n'as pas d'importance, je ne compare
# pas le milleux de la chaine avec lui meme.
# ensuite je joue avec la variable (validation)
# True si le debut de la chaine == la fin de la chaine
# sinon False et je casse la boucle et retourne (validation)


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
# je suis partie sur un systeme de tri en (n²) par ce que 
# c'est celuis que je connais le mieux.
# en gros je compare liste index i avec liste index j qui est = a i + 1
# pour ne pas comparer i avec lui meme.
# si lst[j] est plus petit que lst[i] je stock la valeur de lst[i] dans tmp
# ensuite lst[i] prend la valeur de lst[j] et lst[j] celle de tmp (enciennement la valeur de lst[i])

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
# celuis la ma un peu casser la tete.
# je suis partie sur 2 fonction pour un souci de facilitee
# dans la fonction (prime) si nbr est parfaitement = a 2 je retourne True
# sinon je set tmp a False et fait une une boucle (for in range()) avec le nombre
# en parametre, si i est plus grand que 1 alors je rentre dans le if
# si i doit etre plus grand que 1 c'est pour eviter de faire nbr % 0 par ce qu'on peux pas le faire
# egalement pour eviter de fair nbr % 1 car ca na pas d'interet de verifier
# le reste d'une division par 1.
# apres je verifi si nombre modulo valeur de i est parfaitement = a 0
# si oui alors tmp passe en false (meme si tmp est deja en false) et casse la boucle
# sinon tmp passe en true mais ne casse pas la boucle c'est pour ca que je repasse
# tmp en false dans le (if nbr % i == 0:).
# si on ne passe jamais dans le if que passe tmp en false, la boucle s'arete au bout
# de nbr fois

def prime(nbr):
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
        if prime(i):
            print(i)

# print_prime(50, 70)
