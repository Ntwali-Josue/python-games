import random
from words import words
import string

def get_valid_word(words):
    word = random.choice(words)
    while '-' in word or ' ' in word:
        word = random.choice(words)

    return word

lives = 6

def hangman():
    word = get_valid_word(words)
    words_letters = set(word)
    alphabet = set(string.ascii_uppercase)
    used_letters = set()

    # get user input 
    while len(words_letters) > 0 and lives > 0:

        print("You have ", lives, " lives left and you have used these letters: ", ' '.join(used_letters))

        #show the current word i.e( W-SR- R)
        word_list = [
            letter if letter in used_letters else '-' for letter in word
        ]
        print('The current word is: ', ' '.join(word_list))
        user_letter = input('Guess a letter: ').upper()
        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            if user_letter in words_letters:
                words_letters.remove(user_letter)

            else:
                lives = lives - 1 #remove one lives if guessed the wrong letter
             
        
        elif user_letter in used_letters:
            print('You have already used that character. Please try again.')
        
        else:
            print('Invalid character. Please try again.')

    #when len word == 0 and lives == 0
    if lives == 0:
        print('You\ve run out of lives. The word was: ', word)
    
    else:
        print("Yeaaass You've won, the word is: ", word)