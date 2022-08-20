#!/usr/bin/env python3


from brain_games.scripts.brain_games import greet
from brain_games.cli import welcome_user
from brain_games.logic.games_logic import gcd_question
import prompt


def game_gcd():
    name = welcome_user()
    counter = 0
    winscore = 2
    print("Find the greatest common divisor of given numbers.")
    gcd_question()


num_1 = 10
num_2 = 20


def gcd_question():
    Question = f'Question: {num_1}  {num_2}' + "\n"
    print(Question, end='')
    gcd_question.user_answer = prompt.string('Your answer: ')
    if num_1 == 0:
        return num_1
    if num_2 == 1 or num_2 == 1:
        return 1
    correct_answer = (num_2, num_1 % num_2)
    if gcd_question.user_answer == correct_answer:
        print(True)
    else:
        print(False)


def main():
    greet()
    game_gcd()
    if __name__ == '__main__':
        main()
