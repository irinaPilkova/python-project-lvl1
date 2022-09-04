#!/usr/bin/env python3


from brain_games.logic.games_logic import create_number


def even_question():
    """This function defines the question for the game."""
    random_number = create_number()
    question = f'Question: {random_number}' + "\n"
    return question, random_number


def is_even(random_number):
    """This function returns if the random number is even or not."""
    if random_number % 2 == 0:
        correct_answer = "yes"
    else:
        correct_answer = "no"
    return correct_answer
