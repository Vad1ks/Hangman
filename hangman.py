# Write your code here
import random
words = ['python', 'java', 'kotlin', 'javascript', 'golang', 'ruby', 'assembler', 'function', 'loop']
guessed_letters = []
tried_letters = set()
counter = 0


def string_arranging(answer):
    string = ''
    for i in range(len(answer)):
        if answer[i] in guessed_letters:
            j = guessed_letters.index(answer[i])
            string += guessed_letters[j]
        else:
            string += '-'
    return string


def starting_string_arranging(answer):
    string = ''
    for _ in answer:
        string += '-'
    return string


def hangman_game(tries):
    answer = random.choice(words)
    string = starting_string_arranging(answer)
    print(string)
    guessed_letters.clear()
    tried_letters.clear()
    while tries:
        letter = input("Input a letter: ")
        if len(letter) > 1 and letter == 'exit':
            break
        elif len(letter) > 1:
            print("You should input a single letter\n")
            string = string_arranging(answer)
            print(string)
        elif not letter.isalpha() or not letter.islower():
            print("Please enter a lowercase English letter\n")
            string = string_arranging(answer)
            print(string)

        elif letter in tried_letters:
            print("You've already guessed this letter\n")
            string = string_arranging(answer)
            print(string)
            tried_letters.add(letter)
        else:
            tried_letters.add(letter)
            if letter in answer:
                guessed_letters.append(letter)
                string = string_arranging(answer)
                if string == answer:
                    print("You guessed the word %s with %d tries left!" % (answer, tries))
                    print("You survived!")
                    break
                print("\n" + string)
            else:
                if tries == 1:
                    print("That letter doesn't appear in the word")
                    print("You lost!")
                    print("The word was \"%s\". Good luck next time!" % answer)
                    tries -= 1
                else:
                    print("That letter doesn't appear in the word\n")
                    print(string)
                    tries -= 1


print("H A N G M A N\n")
choice = input("Type \"play\" to play the game, \"exit\" to quit:")

while choice != 'exit':
    while choice != 'play':
        choice = input("Type \"play\" to play the game, \"exit\" to quit:")
    tries = input("Input the amount of tries:")
    while not tries.isnumeric() or int(tries) < 1:
        tries = input("Input the amount of tries:")
    tries = int(tries)
    hangman_game(tries)
    choice = input("Type \"play\" to play the game, \"exit\" to quit:")

