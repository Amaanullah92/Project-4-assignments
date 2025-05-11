# <!-- Project 7: Password Generator Python Project -->

import random

print("=== Welcome to Your Password Generator! ===")
chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*1234567890"
number = input("Amount of passwords to generate: ")
number = int(number)
length = input("Input your password length: ")
length = int(length)

print("\nHere are your passwords:")
for i in range(number):
    password = ""
    for x in range(length):
        password += random.choice(chars)
    print(password)
