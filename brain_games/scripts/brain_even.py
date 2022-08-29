#!/usr/bin/env python3


from brain_games.scripts.brain_games import greet
from brain_games.logic.games_logic import brain_even


def game_result():
    brain_even()


def main():
    greet()
    game_result()
    if __name__ == '__main__':
        main()
