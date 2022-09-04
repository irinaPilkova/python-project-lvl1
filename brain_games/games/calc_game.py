#!/usr/bin/env python3


from brain_games.logic.games_logic import create_number
from random import choice


def calc_question():
    """This function defines the question for the game."""
    num_1 = create_number()
    num_2 = create_number()
    operand_list = ['+', '-', '*']
    operand = choice(operand_list)
    if operand == '+':
        question = f'Question: {num_1} + {num_2}' + "\n"
    elif operand == '-':
        question = f'Question: {num_1} - {num_2}' + "\n"
    elif operand == '*':
        question = f'Question: {num_1} * {num_2}' + "\n"
    return question, num_1, num_2, operand


def calc_answer(operand, num_1, num_2):
    """This function defines the correct answer for the game."""
    if operand == '+':
        correct_answer = str(num_1 + num_2)
    elif operand == '-':
        correct_answer = num_1 - num_2
    elif operand == '*':
        correct_answer = num_1 * num_2
    return correct_answer
