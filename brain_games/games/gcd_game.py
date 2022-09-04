#!/usr/bin/env python3


from brain_games.logic.games_logic import create_number


def gcd_question():
    """This function defines the question for the game."""
    num_1 = create_number()
    num_2 = create_number()
    question = f'Question: {num_1} {num_2}' + "\n"
    return question, num_1, num_2


def gcd_answer(num_1, num_2):
    """This function defines the correct answer for the game."""
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
    print(correct_answer)
    return str(correct_answer)
