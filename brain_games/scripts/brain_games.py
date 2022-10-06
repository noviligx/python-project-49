#!/usr/bin/env python3
from brain_games.cli import welcome_user
import prompt


def main():
    print("Welcome to the Brain Games!")
    name_user = prompt.string("May I have your name? ")
    welcome_user(name_user)


if __name__ == '__main__':
    main()
