#!/usr/bin/python3

def main():
    print("*****************************")
    print("Welcome to Erik's Bistro game")
    print("*****************************")
    print("");

    username = input("What is your name? ")
    print(f"Hello, {username}")

    bistroName = input("What is your Bistro called? ")
    print(f"Great, Welcome to {bistroName}, {username}!")

if __name__ == '__main__':
    main()
