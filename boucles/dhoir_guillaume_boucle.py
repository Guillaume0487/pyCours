# ex01
L = ["tomate", "patate", "carotte", "oeuf", "boeuf"]
for e in L:
    print(e)

# ex02
# nbr = int(input("\nEntrez un chiffre >>> "))
# for i in range(nbr + 1):
#     print(i)

# ex03
# strg = "Wellcome"
# for e in strg:
#     print(e, end="")
# print("\n")

# ex04
# L = ["Jean", "Stephane", "Hamid", "Christine", "Marie"]
# for e in L:
#     if e == "Hamid":
#         break
#     print(e)

# ex05
# L = ["Jean", "Stephane", "Hamid", "Christine", "Marie"]
# for e in L:
#     if e == "Hamid":
#         continue
#     print(e)

# ex06
# i = 8
# while i <= 18:
#     print(i)
#     i += 1

# ex07
# i = 18
# while i >= 0:
#     print(i)
#     i -= 1

# bonus01
# user_login = ""
# user_password = ""
# while user_login != "Guillaume" or user_password != "password":
#     user_login = str(input("\nNom d'utilisateur : "))
#     user_password = str(input("Mot de passe : "))
# print("Bienvenu " + user_login + " vous etes connecte")

# bonus02
# L = []
# active = True
# while active:
#     ask = str(input("\nVoulez vous ajouter un mot dans la liste ? (y/n) >>> ")).lower()
#     if len(ask) < 0 or len(ask) > 1 or 'n' != ask != 'y':
#         print("Caratere invalide")
#     elif ask == 'y':
#         L.append(str(input("Entrez le mot a ajouter >>> ")))
#     else:
#         print(L)
#         active = False
