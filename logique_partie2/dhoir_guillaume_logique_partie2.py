# ex07
# dans la premiere fonction je retourne simplement un carre de nbr
# dans la deuxieme je dit d'afficher le carre de i si il se situee
# egale ou entre borne_inf et borne_sup

def carre(nbr):
    return (nbr * nbr)

def carre_parfait(borne_inf, borne_sup):
    for i in range(borne_sup):
        if borne_inf <= carre(i) <= borne_sup:
            print(carre(i))

# carre_parfait(50, 100)

# ex08
# comme les 2 liste sont dejat trier je vais prendre le premier
# ellement de la deuxieme et l'insert a l'index i de la liste 1
# si l'ellement de la liste 1 est plus grand que celui de la
# liste 2

def fusion(lst1, lst2):
    i = 0
    for e1 in lst1:
        for e2 in lst2:
            if e1 > e2:
                lst1.insert(i, e2)
                lst2.remove(e2)
        i += 1
    print(lst1)


# L1 = [1, 4, 6]
# L2 = [2, 3, 5]
# fusion(L1, L2)

# ex09
# j'insert dernier ellement de la liste au debut de celci
# esuite je suprime le dernier ellement pour ne pas avoir de doublon

def rotation_lst(lst, rot):
    i = 0
    while i < rot:
        lst.insert(0, lst[-1])
        lst.pop(-1)
        i += 1
    print(lst)

# L = [10, 20, 30, 40, 50]
# rotation_lst(L, 3)

# ex10

def anagrame(strg1, strg2):
    if len(strg1) != len(strg2):
        return (False)
    for e1 in strg1:
        for e2 in strg2:
            if e2 == e1:
                tmp = True
                break
            else:
                tmp = False
        if tmp == False:
            break
    return (tmp)

# print(anagrame("hello", "world"))

# ex11

def lst_prefix(lst):
    tmp = 0
    test = []
    for e in lst:
        if tmp == 0:
            tmp = len(e)
        elif len(e) < tmp:
            tmp = len(e)
    for i in range(len(lst) - 1):
        for j in range(tmp):
            if lst[i][j] == lst[i + 1][j]:
                test.append(lst[i][j])
            else:
                if len(test) > j:
                    test.pop(j)
                    break
    j = -1
    k = len(test) // 2 - 1
    for i in range(len(test) // 2):
        if test[k] != test[j]:
            return ([])
        test.pop(j)
        k -= 1

    return ("".join(test))

L = ["applei", "appetite", "appril"]
print(lst_prefix(L))