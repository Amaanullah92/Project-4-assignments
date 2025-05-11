# <!-- Problem: High Low
# We want you to gain more experience working with control flow and Booleans in Python. To do this, we are going to have you develop a game! The game is called High-Low and the way it's played goes as follows:

# Two numbers are generated from 1 to 100 (inclusive on both ends): one for you and one for a computer, who will be your opponent. You can see your number, but not the computer's!

# You make a guess, saying your number is either higher than or lower than the computer's number

# If your guess matches the truth (ex. you guess your number is higher, and then your number is actually higher than the computer's), you get a point!

# These steps make up one round of the game. The game is over after all rounds have been played.

# We've provided a sample run below.

# Welcome to the High-Low Game!
# --------------------------------
# Round 1
# Your number is 8
# Do you think your number is higher or lower than the computer's?: lower
# You were right! The computer's number was 35
# Your score is now 1

# Round 2
# Your number is 88
# Do you think your number is higher or lower than the computer's?: higher
# Aww, that's incorrect. The computer's number was 100
# Your score is now 1

# Round 3
# Your number is 63
# Do you think your number is higher or lower than the computer's?: higher
# You were right! The computer's number was 5
# Your score is now 2

# Round 4
# Your number is 57
# Do you think your number is higher or lower than the computer's?: lower
# Aww, that's incorrect. The computer's number was 57
# Your score is now 2

# Round 5
# Your number is 22
# Do you think your number is higher or lower than the computer's?: lower
# Aww, that's incorrect. The computer's number was 1
# Your score is now 2

# Thanks for playing! -->


import random

NUM_ROUNDS = 5

def main():
    print("Welcome to the High-Low Game!")
    print('--------------------------------')

    # Milestone 5: keep track of your score
    your_score = 0

    # Milestone 4: Play multiple rounds
    for i in range(NUM_ROUNDS):
        print("Round", i + 1)
        # Milestone 1: Generate the random numbers and print them out
        computer_num: int = random.randint(1, 100)
        your_num: int = random.randint(1, 100)
        print("Your number is", your_num)

        # Milestone 2: Get user input for their choice
        choice: str = input("Do you think your number is higher or lower than the computer's?: ")

        # Milestone 3: Map out all the ways to win the round
        higher_and_correct: bool = choice == "higher" and your_num > computer_num
        lower_and_correct: bool = choice == "lower" and your_num < computer_num

        if higher_and_correct or lower_and_correct:
            print("You were right! The computer's number was", computer_num)
            # Milestone 5: keep track of your score
            your_score += 1 
        else: 
            print("Aww, that's incorrect. The computer's number was", computer_num)

        # Milestone 5: keep track of your score
        print("Your score is now", your_score)
        print()

    print("Thanks for playing!")

if __name__ == "__main__":
    main()

