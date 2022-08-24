#!/usr/bin/env python3
from random import choice




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

def game_calc():
    name = welcome_user()
    counter = 0
    winscore = 2
    print("What is the result of the expression?")
    while counter <= winscore:
        calc_question()
        if str(calc_question.correct_answer) != calc_question.user_answer:
            print(f" '{calc_question.user_answer}' is wrong answer ;(. Correct answer was '{calc_question.correct_answer}'.\n Let's try again, {name}!")
            break
        elif str(calc_question.correct_answer) == calc_question.user_answer:
            print('Correct!')
            counter += 1
    if counter == 3:
        print(f"Congratulations,{name}!")

