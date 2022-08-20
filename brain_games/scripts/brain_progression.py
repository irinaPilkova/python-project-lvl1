#!/usr/bin/env python3


from brain_games.logic.games_logic import progression_question
from brain_games.cli import welcome_user
from brain_games.scripts.brain_games import greet


def game_progression():
    name = welcome_user()
    counter = 0
    winscore = 2
    print("What number is missing in the progression?")
    while counter <= winscore:
        counter += 1
        if progression_question() is False:
            print(f" '{progression_question.user_answer}' is wrong answer ;(. Correct answer was '{progression_question.correct_answer}'.\n Let's try again, {name}!")
            break
        elif progression_question() is True:
            print("Correct")
    if counter == 3:
        print(f"Congratulations, {name}!")


def main():
    greet()
    game_progression()
    if __name__ == '__main__':
        main()
