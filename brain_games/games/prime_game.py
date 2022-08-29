#!/usr/bin/env python3

def prime_question(random_number):
    """This function defines the question for the game."""
    question = f'Question: {random_number}' + "\n"
    return question


def is_prime(random_number):
    """This function returns if the random number is prime or not."""
    for i in range(2, random_number):
        if random_number % i == 0:
            correct_answer = "no"
            break
    else:
        correct_answer = "yes"
    return correct_answer
