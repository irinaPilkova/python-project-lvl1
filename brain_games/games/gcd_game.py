#!/usr/bin/env python3


from random import randint


DESCRIPTION = 'Find the greatest common divisor of given numbers.'


lower_limit = 1
upper_limit = 100


def generate_question_answer():
    """This function defines the question for the game."""
    num_1 = randint(lower_limit, upper_limit)
    num_2 = randint(lower_limit, upper_limit)
    question = f'Question: {num_1} {num_2}' + "\n"
    if num_1 == 0:
        correct_answer = 0
    if num_1 == 1 or num_2 == 1:
        correct_answer = 1
    if num_1 > num_2:
        num = num_1
    else:
        num = num_2
    correct_answer = 1
    for i in range(1, num):
        if num_2 % i == 0 and num_1 % i == 0:
            correct_answer = i
    return question, str(correct_answer)
