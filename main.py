###założenia###
# pokazuje które litery były w wyrazie, które na dobrym miejscu i których nie ma w wyrazie
def ContainsANumber(string):
    return any(char.isdigit() for char in string)

import random
import time

while 1:
    error = True

    anwser = []
    correctLetters = []
    incorrectLetters = []

    tries = 1

    # choosing word length (4-8)
    while error:
        try:
            wordLength = int(input("set word length(4-8): "))
            if 4 <= wordLength <= 8:
                error = False
            else:
                print("pick a number between 4 and 8")
        except ValueError:
            print("please write a number")

    error = True

    for i in range(wordLength):
        anwser.append("_")

    # choosing number of tries
    while error:
        try:
            maxtries = int(input("set number of tries: "))
            if maxtries > 0:
                error = False
            else:
                print("set a number greater than 0")
        except ValueError:
            print("please write a number")

    # picking random word
    wordBase = open(f"wordBase/stripped_base{wordLength}.txt")
    wordList = wordBase.readlines()
    wordBase.close()

    rand = random.randint(0, len(wordList))
    word = wordList[rand]
    word = word.strip()

    while tries <= maxtries:
        error = True
        # getting user guess
        while error:
            guess = input("let's guess: ")
            if not ContainsANumber(guess) and len(guess) == wordLength and guess + "\n" in wordList:
                error = False
            elif ContainsANumber(guess) and len(guess) != wordLength:
                print("words don't have digits and this word is too long or too short!!!")
            elif ContainsANumber(guess):
                print("words don't have digits!!!")
            elif len(guess) != wordLength:
                print("this word is too long or too short!!!")
            elif guess not in wordList:
                print("that's not a real word!!!")

        guess = guess.lower()

        #tu nie dokończyłeś
        #przemyśl potencjalne błędy dopisz warunek zakończenia pętli i zrób pętle przed guessem
        for i in range(wordLength):
            if guess[i] in word:
                if word[i] == guess[i]:
                    anwser[i] = guess[i]
                else:
                    if guess[i] not in correctLetters:
                        correctLetters.append(guess[i])
            elif guess[i] not in incorrectLetters:
                incorrectLetters.append(guess[i])
        print(f'⬛⬛⬛⬛⬛⬛⬛⬛\n'
              f'correctly placed letters: {anwser}')
        time.sleep(1)
        print(f'⬛⬛⬛⬛⬛⬛⬛⬛\n'
              f'correct but misplaced letters: {correctLetters}')
        time.sleep(1)
        print(f'⬛⬛⬛⬛⬛⬛⬛⬛\n'
              f'incorrect letters: {incorrectLetters}\n')
        time.sleep(1)
        if guess == word:
            break
        tries += 1

    if guess == word:
        print(f"Congrats you guessed anwser {guess} in {tries} tries!!!")
    else:
        print("You lost but that's ok, you can try again with more tries.\n"
              f"The anwser was {word}")
    print("Do you want to play again?\ny = yes\nn = no")

    error = True
    while error:
        again = input()
        if again == "y" or again == "n":
            error = False
        else:
            print("write 'y' or 'n'")
    if again == "n":
        print("Have a great day, bye!")
        break