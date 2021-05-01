#!/usr/bin/env python3

# Created by: Hussein Mansour
# Created on: Sat/May1/2021
# This program is a Number Guessing Game


import constants


def main():
    # this function checks if the number guessed is true
    print("hey,guess the number if you can!\n")

    # input
    number_guessed = int(input("Enter the number between 0 - 9:"))

    # process & output
    if constants.NUMBER == number_guessed:
        print("You guessed correct!")

    if constants.NUMBER != number_guessed:
        print("You guessed wrong!")

    print("\nDone.")


if __name__ == "__main__":
    main()
