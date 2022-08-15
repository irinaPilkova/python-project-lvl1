#!/usr/bin/env python3
from brain_games.scripts.brain_games import greet
from brain_games.cli import welcome_user
from brain_games.logic.games_logic import gcd_question

def game_gcd():
    name = welcome_user()
    counter = 0
    winscore = 2
    print("Find the greatest common divisor of given numbers.")
    gcd_question()



def main():
    greet()
    game_gcd()
    
    if __name__ == '__main__':
        main()
