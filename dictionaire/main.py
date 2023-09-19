# d = {
#     "nom" : "Guillaume",
#     "age" : 25,
#     "ville" : "Bruxelles"
# }

# print(d.keys())

# d = {
#     "orange" : 12,
#     "bannane" : 3,
#     "mandarine" : 7
# }

# print(sum(d.values()))

# classe1 = {
#     "eleve1" : {
#         "nom" : "eve",
#         "age" : 16,
#         "moyenne" : 19
#     }
# }

# classe2 = {
#     "eleve2" : {
#         "nom" : "leonard",
#         "age" : 17,
#         "moyenne" : 11
#     },
#     "eleve3" : {
#         "nom" : "hamid",
#         "age" : 16,
#         "moyenne" : 17
#     }

# }

# classe1.update(classe2)
# print(classe1)

log = {
    "login" : "Guillaume",
    "password" : "password"
}

user_log = {
    "login" : "",
    "password" : ""
}

while user_log["login"] != log["login"] or user_log["password"] != log["password"]:
    user_log["login"] = str(input("\nusername : "))
    user_log["password"] = str(input("mot de passe : "))
print("Bienvenu " + user_log["login"] + " vous etes connecte")