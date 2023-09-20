# ex01
def parite(nbr):
    if nbr % 2 == 0:
        return (True)
    return (False)

# print(parite(0))
# ex02

def factorielle(nbr):
    tmp = nbr
    if nbr > 0:
        i = nbr - 1
        while i > 1:
            nbr *= i
            i -= 1
    else:
        nbr = 1
    print(str(tmp)+ "! = " + str(nbr))

# factorielle(3)
# ex04

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
                tmp =  (False)
                break
            else:
                tmp = (True)
    return (tmp)

def print_prime(borne_inf, borne_sup):
    for i in range(borne_inf, borne_sup):
        if premier(i):
            print(i)

# print_prime(50, 70)