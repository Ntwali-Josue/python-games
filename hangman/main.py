import random
from words import words
import string

def get_valid_word(words):
    word = random.choice(words)
    while '-' in word or ' ' in word:
        word = random.choice(words)

    return word


def hangman():
    word = get_valid_word(words)
    words_letters = set(word)
    alphabet = set(string.ascii_uppercase)
    used_letters = set()

    user_letter = input('Guess a letter: ').upper()
    if user_letter in alphabet - used_letters:
        used_letters.add(user_letter)
        if user_letter in words_letters:
            words_letters.remove(user_letter)
    
    elif user_letter in used_letters:
        print('You have already used that character. Please try again.')
    
    else:
        print('Invalid character. Please try again.')