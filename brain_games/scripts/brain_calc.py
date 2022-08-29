#!/usr/bin/env python3


from brain_games.scripts.brain_games import greet
from brain_games.logic.games_logic import calculation_question


def game_calc():
    calculation_question()


def main():
    greet()
    calculation_question()
    if __name__ == '__main__':
        main()
