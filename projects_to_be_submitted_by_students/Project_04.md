<!-- Project 4: Rock, paper, scissors Python Project -->

import random
def isWin(player,opponent):
    if player == 'r' and opponent == 's':
        return True
    elif player == 's' and opponent == 'p':
        return True
    elif player == 'p' and opponent == 'r':
        return True
    return False

def main():
   computer = random.choice(['r','p','s'])
   user = input("Enter your choice (r/p/s): ")
   if isWin(user,computer):
       print("You won!")
   elif user == computer:
       print("It's a tie!")
   else:
       print("You lost!")

if __name__ == '__main__':
    main()
    