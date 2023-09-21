import random

def create_word():
    L = ["avion", "train", "camion", "bateau", "voiture", "arbre", "facade", "humain", "virus", "pandue"]
    word = random.choice(L)
    return (word)

def create_indice(word):
    indice = []
    for i in range(len(word)):
        indice.append('-')
    return (indice)

def count_dash(indice):
    counter = 0
    for e in indice:
        if e == '-':
            counter += 1
    return (counter)

def ask(word, indice, counter):
    print("\nMot en " + str(len(word)) + " lettre, il vous en reste " + str(count_dash(indice)) + " a trouver\nIl vous rest " + str(counter) + " chances sur 9")
    user_char = str(input(str("".join(indice)) + " >>> "))
    return (user_char)

def update_indice(word, indice, user_char):
    for i in range(len(word)):
        if user_char == word[i]:
            indice[i] = user_char

def valid_char(user_char):
    alpha = "abcdefghijklmnopqrstuvwxyz"
    if 0 < len(user_char) < 2 and user_char in alpha:
        return (True)
    return (False)

def game(word, indice, counter):
    user_char = ""
    while "".join(indice) != word:
        user_char = ask(word, indice, counter).lower()
        update_indice(word, indice, user_char)
        if not valid_char(user_char):
            return (game(word, indice, counter))
        counter -= 1
        if user_char not in word:
            print("La lettre (" + user_char + ") n'est pes dans le mot a trouver")
        if "".join(indice) == word:
            return (True)
        if counter < 1:
            return (False)

def win(word):
    for i in range(50):
        print("\n")
    print("vous avez trouver le mot (" + word + ")\nvous avez gagnez")

def lose(word):
    for i in range(50):
        print("\n")
    print("vous avez perdue\nle mot etait (" + word + ")")

def start():
    for i in range(50):
        print("\n")
    word = create_word()
    indice = create_indice(word)
    counter = 9
    played = game(word, indice, counter)
    if played:
        win(word)
    else:
        lose(word)
        

start()
