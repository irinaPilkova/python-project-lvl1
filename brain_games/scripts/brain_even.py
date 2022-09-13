#!/usr/bin/env python3


from brain_games.games_engine import run_game
from brain_games.games import even_game


def play_game():
    run_game(even_game)


def main():
    play_game()
    if __name__ == '__main__':
        main()
