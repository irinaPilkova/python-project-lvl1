#!/usr/bin/env python3


from brain_games.games_engine import run_game
from brain_games.games import progression_game


def play_game():
    run_game(progression_game)


def main():
    play_game()
    if __name__ == '__main__':
        main()
