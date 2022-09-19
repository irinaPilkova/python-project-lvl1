from random import randint
from random import choice


DESCRIPTION = 'What is the result of the expression?'


LOWER_LIMIT = 1
UPPER_LIMIT = 100
OPPERAND_LIST = ['+', '-', '*']


def generate_question_answer():
    """This function defines the question for the game."""
    num_1 = randint(LOWER_LIMIT, UPPER_LIMIT)
    num_2 = randint(LOWER_LIMIT, UPPER_LIMIT)
    operand = choice(OPPERAND_LIST)
    question = f'Question: {num_1} {operand} {num_2}' + "\n"
    if operand == '+':
        correct_answer = num_1 + num_2
    elif operand == '-':
        correct_answer = num_1 - num_2
    elif operand == '*':
        correct_answer = num_1 * num_2
    return question, str(correct_answer)
