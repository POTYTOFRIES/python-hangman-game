import random
import time
from wordbank import word_list

# Getting a word in wordbank.py
def get_word():
    word = random.choice(word_list)
    return word.upper()

# function to print the letters one by one
def a_print(s):
    for char in s:
        print(char, end="", flush=True)
        time.sleep(0.07)

# function to print messages with a 3 seconds delay
def pp1(message):
    print(message)
    time.sleep(1)

# Welcomes the player
PlayerName = input("Enter your name: ").upper()
print("               \n")
print("Welcome", PlayerName,"!")
# Instruction
pp1("This is a Hangman game.")
pp1("You need to guess the word before the timer ends (30 secs),")
pp1("and you have '5' attempts only.")
pp1("\nHINT: The words are connected to Programming")
a_print("\nGood luck, Have fun!\n")
print("   ")

# function that turns the word into guess and this where the game restart.
def play(word):
    word_completion = "_" * len(word) #transforms the words into _
    guessed = False 
    guessed_letters = [] #player guess the letter
    guessed_words = [] #player guess the word
    tries = 6 
    start_time = time.time()
    a_print("TIMER STARTS NOW!\n")
    a_print("Let's play Hangman!")
    print(display_hangman(tries))
    print(word_completion)
    print("\n")

    while not guessed and tries > 0:  
        guess = input("Please guess a letter or word: ").upper()
        
        # Ends time
        if time.time() - start_time > 30 and guess != word:
            print("Time's up! You ran out of time.")
            print("The word was: ", word)
            a_print(" R.I.P \n")
            return main

      # Guessing the letters
      # .isalpha makes sure that the Guessed letter is a string.
        if len(guess) == 1 and guess.isalpha():
            # if the player re-input a letter.
            if guess in guessed_letters:
                print("You already guessed the letter", guess, "Go next!\n")

            # the letter is not part of the word.
            elif guess not in word:
                print(guess, "is not in the word.\n")
                tries -= 1
                guessed_letters.append(guess)

            # if the player guessed a letter correctly, 
            else:
                print("YAY!", guess, "is in the word! Keep Going", PlayerName, "\n")
                guessed_letters.append(guess)

                word_as_list = list(word_completion) # The Word that needs to be guessed
                indices = [i for i, letter in enumerate(word) if letter == guess] 

                # to check if the player's guess has correctly filled in all the blanks in the word.
                for index in indices:
                    word_as_list[index] = guess
                word_completion = "".join(word_as_list)
                
                # now if there's no _ in word then the player guessed the word.
                if "_" not in word_completion:
                    guessed = True
                    print("That's right the word is", word)


        # Guessing the word
        elif len(guess) == len(word) and guess.isalpha():
            
            if guess in guessed_words:
                print("You already guessed the word!! \nDon't repeat yourself bruh -_-", guess, "\n")

            elif guess != word:
                print(guess, "is not the word. Try again!\n")
                tries -= 1
                guessed_words.append(guess)

            else:
                guessed = True
                word_completion = word
                print("That's right the word is", word)

        else:
            print("Not a valid guess.\n") # means the guess is neither a string or the right word.

        print(display_hangman(tries))
        print(word_completion)
        print("\n")
    
    if guessed:
        print("CONGRATS!", PlayerName)
        a_print("YOU ESCAPED DEATH :D\n")

    else:
        print("You ran out of tries. \nThe word was " + word + ". \nMaybe next time!")
        a_print("\n R.I.P \n")



def display_hangman(tries):
    stages = [ 
      # final state: head, torso, both arms, and both legs
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / \\
                   -
                """,
                # head, torso, both arms, and one leg
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / 
                   -
                """,
                # head, torso, and both arms
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |      
                   -
                """,
                # head, torso, and one arm
                """
                   --------
                   |      |
                   |      O
                   |     \\|
                   |      |
                   |     
                   -
                """,
                # head and torso
                """
                   --------
                   |      |
                   |      O
                   |      |
                   |      |
                   |     
                   -
                """,
                # head
                """
                   --------
                   |      |
                   |      O
                   |    
                   |      
                   |     
                   -
                """,
                # initial empty state
                """
                   --------
                   |      |
                   |      
                   |    
                   |      
                   |     
                   -
                """
    ]
    return stages[tries]

# Main function that restarts or ends the game.
def main():
    word = get_word()
    start_time = time.time()
    play(word)
    while input("\nPlay Again? (Y/N) \n").upper() == "Y":
        word = get_word()
        start_time = time.time()
        play(word)

# for this whole code to run in the command line. 
#__name__ is a special variable stores the name of the currently running Python script or module. And it's value is always __main__.
if __name__ == "__main__":
    main()