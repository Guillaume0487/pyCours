#ex01
L1 = ["Guillaume", "Celine", "Artine"]

print(L1)
print(len(L1))
for e in L1:
    print(e)

#ex02
L2 = ["Guillaume", 25, 12.5, True]
print(L2)
L2.append("Celine")
print(L2)

#ex03
#def remplace(lst, str, str_update):
#    for i in range(len(lst)):
#        if lst[i] == str:
#            lst[i] = str_update
#    return (lst)

L3 = ["Voiture", "Moto", "Velo"]
print(L3)
#remplace(L3, "Moto", "Scooter")
L3.pop(1)
L3.insert(1, "Scooter")
print(L3)