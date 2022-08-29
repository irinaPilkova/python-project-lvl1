#!/usr/bin/env python3


def calc_question(num_1, num_2, operand):
    """This function defines the question for the game."""
    if operand == '+':
        question = f'Question: {num_1} + {num_2}' + "\n"
    elif operand == '-':
        question = f'Question: {num_1} - {num_2}' + "\n"
    elif operand == '*':
        question = f'Question: {num_1} * {num_2}' + "\n"
    return question


def calc_answer(operand, num_1, num_2):
    """This function defines the correct answer for the game."""
    if operand == '+':
        correct_answer = num_1 + num_2
    elif operand == '-':
        correct_answer = num_1 - num_2
    elif operand == '*':
        correct_answer = num_1 * num_2
    return str(correct_answer)
