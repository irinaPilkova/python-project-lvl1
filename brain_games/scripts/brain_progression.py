#!/usr/bin/env python3


from brain_games.logic.games_engine import progression_question
from brain_games.scripts.brain_games import greet


def game_progression():
    progression_question()


def main():
    greet()
    progression_question()
    if __name__ == '__main__':
        main()
