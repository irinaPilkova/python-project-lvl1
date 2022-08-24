#!/usr/bin/env python3

def prime_question(random_number):
    """This function defines the question for the game."""
    print('Answer "yes" if given number is prime. Otherwise answer "no".')
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
    print(random_number, correct_answer)
    return correct_answer
