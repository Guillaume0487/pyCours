import random
import time


def create_word():
    L = ["voiture",
         "moto",
         "camion",
         "velo",
         "bus",
         "tramway",
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
    alpha = "abcdefghijklmnopqrstuvwxyz-"
    if 0 < len(user_char) < 2 and user_char in alpha:
        return (True)
    if len(user_char) > 1:
        print("(" + user_char + ") contiens trop de caractere")
    else:
        print("Le caractere (" + user_char + ") est invalide")
    return (False)


def game(word, indice, counter):
    user_char = ""
    while "".join(indice) != word:
        user_char = ask(word, indice, counter).lower()
        update_indice(word, indice, user_char)
        if not valid_char(user_char):
            return (game(word, indice, counter))
        if user_char not in word:
            counter -= 1
            if counter < 1:
                return (False)
            print("La lettre (" + user_char + ") n'est pes dans le mot a trouver")
        if "".join(indice) == word:
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
    time.sleep(0.2)


def start():
    for i in range(50):
        print("\n")
    print("Bienvenu dans le jeu du pendu\nLe theme est les vehicules")
    time.sleep(3)
    for i in range(50):
        print("\n")
    word = create_word()
    indice = create_indice(word)
    counter = 9
    played = game(word, indice, counter)
    if played:
        win()
    else:
        lose()
    for i in range(44):
        time.sleep(0.2)
        print("\n")


start()
