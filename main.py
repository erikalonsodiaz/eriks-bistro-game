#!/usr/bin/python3
import sys

def main():
    print("*****************************")
    print("Welcome to Erik's Bistro game")
    print("*****************************")
    print("");

    # Get the user's information
    username = input("What is your name? ")
    print(f"Hello, {username}")

    bistroName = input("What is your Bistro called? ")
    print(f"Great, Welcome to {bistroName}, {username}!")

    # Now set up the game
    dayNumber = 1
    tables = 1

    while True:
        print("");
        print(f"Day: {dayNumber}, Tables: {tables}");

        while True:
            print("");
            action = input("? ")

            if action == 'quit':
                print(f"Goodbye, {username}")
                sys.exit()
            elif action == 'ready':
                dayNumber = dayNumber + 1
                break
            else:
                print(f"I don't know how to '{action}'")

if __name__ == '__main__':
    main()
