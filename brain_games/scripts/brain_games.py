#!/usr/bin/env python3


from brain_games.logic.games_engine import greet
from brain_games.cli import welcome_user


def main():
    greet()
    welcome_user()
    if __name__ == '__main__':
        main()
