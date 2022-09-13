#!/usr/bin/env python3


from random import randint
from random import choice


DESCRIPTION = 'What is the result of the expression?'


lower_limit = 1
upper_limit = 100
operand_list = ['+', '-', '*']


def generate_question_answer():
    """This function defines the question for the game."""
    num_1 = randint(lower_limit, upper_limit)
    num_2 = randint(lower_limit, upper_limit)
    operand = choice(operand_list)
    question = f'Question: {num_1} {operand} {num_2}' + "\n"
    if operand == '+':
        correct_answer = num_1 + num_2
    elif operand == '-':
        correct_answer = num_1 - num_2
    elif operand == '*':
        correct_answer = num_1 * num_2
    return question, str(correct_answer)
