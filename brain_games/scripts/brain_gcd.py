#!/usr/bin/env python3


from brain_games.logic.games_logic import brain_gcd
from brain_games.scripts.brain_games import greet


def game_gcd():
    brain_gcd()


def main():
    greet()
    brain_gcd()
    if __name__ == '__main__':
        main()
