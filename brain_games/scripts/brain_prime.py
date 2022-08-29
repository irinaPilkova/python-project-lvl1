#!/usr/bin/env python3


from brain_games.scripts.brain_games import greet
from brain_games.logic.games_logic import brain_prime


def game_result():
    brain_prime()


def main():
    greet()
    brain_prime()
    if __name__ == '__main__':
        main()
