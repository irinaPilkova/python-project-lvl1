#!/usr/bin/env python3


def even_question(random_number):
    """This function defines the question for the game."""
    question = f'Question: {random_number}' + "\n"
    return question


def is_even(random_number):
    """This function returns if the random number is even or not."""
    if random_number % 2 == 0:
        correct_answer = "yes"
    else:
        correct_answer = "no"
    return correct_answer
