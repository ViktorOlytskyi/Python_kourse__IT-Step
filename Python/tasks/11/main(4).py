import random

words = ["apple", "mango", "grapes", "orange", "papaya"]
letter = ''
word = random.choice(words)
field = []
for i in range(len(word)):
    field.append(" _ ")
str1 = ""
str2 = ""
used = []


def show_field():
    global word
    global str1
    # global str2
    # global used
    for i in range(len(word)):
        if letter == word[i]:
            field[i] = letter
    print("\n\n"+str1.join(field), end="")

    # print("used letters: "+str2.join(used), end=", ")


isWin = False
try_counts = 10
while (isWin != True):
    show_field()

    if word == str1.join(field):
        try_counts += 2

        print(f"\n\nCongratulaions! You guessed the word {word}!\nTry to guessed other word\nYou have {try_counts} lives ")
        field = []
        word = random.choice(words)
        for i in range(len(word)):
            field.append(" _ ")

        show_field()
    else:
        print(f"\nYou have {try_counts} lives")
        print("used letters: " + str2.join(used), sep=", ")

    if (try_counts == 0):

        print("\n\nOh noo!! You lose!")
        exit()
    letter = input("\npleace, enter the letter ")
    used.append(letter)
    try_counts -= 1
