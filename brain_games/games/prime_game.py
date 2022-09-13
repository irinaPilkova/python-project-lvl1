#!/usr/bin/env python3


from random import randint

lower_limit = 1
upper_limit = 100


DESCRIPTION = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def generate_question_answer():
    """This function defines the question for the game."""
    random_number = randint(lower_limit, upper_limit)
    question = f'Question: {random_number}' + "\n"
    for i in range(2, random_number):
        if random_number % i == 0:
            correct_answer = "no"
            break
    else:
        correct_answer = "yes"
    if random_number == 1:
        correct_answer = "no"
    return question, correct_answer
