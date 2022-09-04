#!/usr/bin/env python3


from brain_games.logic.games_logic import create_number


def prime_question():
    """This function defines the question for the game."""
    random_number = create_number()
    question = f'Question: {random_number}' + "\n"
    return question, random_number


def is_prime(random_number):
    """This function returns if the random number is prime or not."""
    for i in range(2, random_number):
        if random_number % i == 0:
            correct_answer = "no"
            break
    else:
        correct_answer = "yes"
    if random_number == 1:
        correct_answer = "no"
    return correct_answer
