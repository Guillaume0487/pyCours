import json
import random
import time

with open("score.json", "r") as file:
    scores = json.load(file)


def title():
    for i in range(50):
        print("\n")
    print("      :::::::::  :::::::::: ::::    ::: :::::::::  :::    ::: ")
    time.sleep(0.2)
    print("     :+:    :+: :+:        :+:+:   :+: :+:    :+: :+:    :+:  ")
    time.sleep(0.2)
    print("    +:+    +:+ +:+        :+:+:+  +:+ +:+    +:+ +:+    +:+   ")
    time.sleep(0.2)
    print("   +#++:++#+  +#++:++#   +#+ +:+ +#+ +#+    +:+ +#+    +:+    ")
    time.sleep(0.2)
    print("  +#+        +#+        +#+  +#+#+# +#+    +#+ +#+    +#+     ")
    time.sleep(0.2)
    print(" #+#        #+#        #+#   #+#+# #+#    #+# #+#    #+#      ")
    time.sleep(0.2)
    print("###        ########## ###    #### #########   ########        ")
    for i in range(5):
        time.sleep(0.2)
        print("\n")


def create_word():
    L = ["voiture",
         "moto",
         "camion",
         "velo",
         "bus",
         "tram",
         "train",
         "avion",
         "bateau",
         "helicoptere",
         "sous-marin",
         "fusee"
         ]

    word = random.choice(L)
    return (word)


def create_indice(word):
    indice = []
    for i in range(len(word)):
        if word[i] == '-':
            indice.append('-')
        else:
            indice.append('_')
    return (indice)


def count_dash(indice):
    counter = 0
    for e in indice:
        if e == '_':
            counter += 1
    return (counter)


def ask(word, indice, counter):
    len_word = len(word)
    for e in word:
        if e == '-':
            len_word -= 1
    print("Mot en " + str(len_word) + " lettre, il vous en reste " +
          str(count_dash(indice)) + " a trouver\nIl vous rest " + str(counter) + " chances sur 9")
    user_char = str(input(str("".join(indice)) + " >>> "))
    for i in range(50):
        print("\n")
    return (user_char)


def update_indice(word, indice, user_char):
    for i in range(len(word)):
        if user_char == word[i]:
            indice[i] = user_char


def valid_char(user_char):
    alpha = "abcdefghijklmnopqrstuvwxyz"
    if 0 < len(user_char) < 2 and user_char in alpha:
        return (True)
    if len(user_char) > 1:
        print("(" + user_char + ") contiens trop de caractere")
    else:
        print("Le caractere (" + user_char + ") est invalide")
    return (False)


def save(pseudo, counter):
    counter *= 10
    if pseudo in scores:
        if scores[pseudo] < counter:
            scores[pseudo] = counter
    else:
        scores[pseudo] = counter
    with open("score.json", "w+") as file:
        json.dump(scores, file)


def game(pseudo, word, indice, counter):
    user_char = ""
    while "".join(indice) != word:
        user_char = ask(word, indice, counter).lower()
        update_indice(word, indice, user_char)
        if not valid_char(user_char):
            return (game(pseudo, word, indice, counter))
        if user_char not in word:
            counter -= 1
            if counter < 1:
                save(pseudo, counter)
                return (False)
            print("La lettre (" + user_char + ") n'est pes dans le mot a trouver")
        if "".join(indice) == word:
            save(pseudo, counter)
            return (True)


def win():
    print("   :::   :::  ::::::::  :::    :::        :::       ::: ::::::::::: ::::    ::: ")
    time.sleep(0.2)
    print("  :+:   :+: :+:    :+: :+:    :+:        :+:       :+:     :+:     :+:+:   :+:  ")
    time.sleep(0.2)
    print("  +:+ +:+  +:+    +:+ +:+    +:+        +:+       +:+     +:+     :+:+:+  +:+   ")
    time.sleep(0.2)
    print("  +#++:   +#+    +:+ +#+    +:+        +#+  +:+  +#+     +#+     +#+ +:+ +#+    ")
    time.sleep(0.2)
    print("  +#+    +#+    +#+ +#+    +#+        +#+ +#+#+ +#+     +#+     +#+  +#+#+#     ")
    time.sleep(0.2)
    print(" #+#    #+#    #+# #+#    #+#         #+#+# #+#+#      #+#     #+#   #+#+#      ")
    time.sleep(0.2)
    print("###     ########   ########           ###   ###   ########### ###    ####       ")


def lose():
    print("   :::   :::  ::::::::  :::    :::          :::        ::::::::   ::::::::  :::::::::: ")
    time.sleep(0.2)
    print("  :+:   :+: :+:    :+: :+:    :+:          :+:       :+:    :+: :+:    :+: :+:         ")
    time.sleep(0.2)
    print("  +:+ +:+  +:+    +:+ +:+    +:+          +:+       +:+    +:+ +:+        +:+          ")
    time.sleep(0.2)
    print("  +#++:   +#+    +:+ +#+    +:+          +#+       +#+    +:+ +#++:++#++ +#++:++#      ")
    time.sleep(0.2)
    print("  +#+    +#+    +#+ +#+    +#+          +#+       +#+    +#+        +#+ +#+            ")
    time.sleep(0.2)
    print(" #+#    #+#    #+# #+#    #+#          #+#       #+#    #+# #+#    #+# #+#             ")
    time.sleep(0.2)
    print("###     ########   ########           ########## ########   ########  ##########       ")


def all_score(key):
    space = 20 - len(key)
    print(key, end="")
    for i in range(space):
        print(" ", end="")
    print(": Score (" + str(scores[key]) + ")")


def start():
    title()
    time.sleep(1)
    pseudo = str(input("Entrez un pseudo >>> "))
    for i in range(50):
        print("\n")
    word = create_word()
    indice = create_indice(word)
    counter = 9
    played = game(pseudo, word, indice, counter)
    if played:
        win()
    else:
        lose()
    for i in range(5):
        time.sleep(0.2)
        print("\n")
    for key in scores:
        all_score(key)


start()
