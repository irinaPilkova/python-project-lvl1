#!/usr/bin/env python3


from random import randint


lower_limit = 1
upper_limit = 100


DESCRIPTION = 'Answer "yes" if the number is even, otherwise answer "no".'


def generate_question_answer():
    """This function defines the question for the game."""
    random_number = randint(lower_limit, upper_limit)
    question = f'Question: {random_number}' + "\n"
    if random_number % 2 == 0:
        correct_answer = "yes"
    else:
        correct_answer = "no"
    return question, correct_answer
