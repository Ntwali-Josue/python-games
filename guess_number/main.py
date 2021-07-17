import random

def guess(x,y):
    random_number = random.randint(x,y)
    guess = 0
    while guess != random_number:
        guess = int(input(f'Guess a number between{x} and {y}: '))
        print(guess)
        if guess < random_number:
            print ('Sorry guess again.Too low')
        elif guess > random_number:
            print('Sorry, guess again.Too high')
    print(f'yohoooo, congrats.You have guessed the right number which is {random_number}')
    
guess(1,10)