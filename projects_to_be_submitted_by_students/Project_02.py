
# <!-- Project 2: Guess the Number Game Python Project (computer) -->

import random
def guess(x):
    random_number = random.randint(1, x)
    guess = 0
    while guess != random_number:
        guess = int(input(f'Guess a number between 1 and {x}: '))
        if guess < random_number:
            print('Sorry, guess again. Too low.')
        elif guess > random_number:
            print('Sorry, guess again. Too high.')
    print(f'Yay, congrats. You have guessed the number {random_number} correctly!!')
def main():
    guess(10)

if __name__ == '__main__':
    main()
