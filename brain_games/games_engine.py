#!/usr/bin/env python3


import prompt
from brain_games.cli import welcome_user


counter = 0
winscore = 3


def greet():
    """This function welcomes User to the Game."""
    print('Welcome to the Brain Games!')


def run_game(game):
    greet()
    name = welcome_user()
    print(game.DESCRIPTION)
    global counter
    while counter < winscore:
        question, correct_answer = game.generate_question_answer()
        print(question, end='')
        user_answer = prompt.string('Your answer: ')
        if user_answer != correct_answer:
            print(f"'{user_answer}' is wrong answer ;(.")
            print(f"Correct answer was '{correct_answer}'.")
            print(f"Let's try again, {name}!")
            break
        elif user_answer == correct_answer:
            print('Correct!')
        counter += 1
        if counter == 3:
            print(f"Congratulations, {name}!")
