#!/usr/bin/env python3


import sys
import prompt
from brain_games.cli import welcome_user
from brain_games.games.even_game import even_question
from brain_games.games.even_game import is_even
from brain_games.games.prime_game import prime_question
from brain_games.games.prime_game import is_prime
from brain_games.games.calc_game import calc_question
from brain_games.games.calc_game import calc_answer
from brain_games.games.progression_game import progres_question
from brain_games.games.gcd_game import gcd_question
from brain_games.games.gcd_game import gcd_answer


def greet():
    """This function welcomes User to the Game."""
    print('Welcome to the Brain Games!')


def get_user_answer(question):
    print(question, end='')
    user_answer = prompt.string('Your answer: ')
    return user_answer


counter = 0
winscore = 3


def compare_answer(user_answer, correct_answer, name):
    """This function compares user and correct answer."""
    if user_answer != correct_answer:
        print(f"'{user_answer}' is wrong answer ;(.")
        print(f"Correct answer was '{correct_answer}'.")
        print(f"Let's try again, {name}!")
    elif user_answer == correct_answer:
        print('Correct!')


def end_game(counter, user_answer, correct_answer, name):
    if user_answer != correct_answer:
        sys.exit()
    if counter == 3:
        print(f"Congratulations, {name}!")


def brain_even():
    """This function starts game for brain even."""
    name = welcome_user()
    print('Answer "yes" if the number is even, otherwise answer "no".')
    global counter
    while counter < winscore:
        question, random_number = even_question()
        user_answer = get_user_answer(question)
        correct_answer = is_even(random_number)
        compare_answer(user_answer, correct_answer, name)
        counter += 1
        end_game(counter, user_answer, correct_answer, name)


def brain_prime():
    """This function starts game for brain prime."""
    name = welcome_user()
    print('Answer "yes" if given number is prime. Otherwise answer "no".')
    global counter
    while counter < winscore:
        question, random_number = prime_question()
        user_answer = get_user_answer(question)
        correct_answer = is_prime(random_number)
        compare_answer(user_answer, correct_answer, name)
        counter += 1
        end_game(counter, user_answer, correct_answer, name)


def calculation_question():
    """This function starts game for brain calc."""
    name = welcome_user()
    print('What is the result of the expression?')
    global counter
    while counter < winscore:
        question, operand, num_1, num_2 = calc_question()
        user_answer = get_user_answer(question)
        correct_answer = calc_answer(operand, num_1, num_2)
        compare_answer(user_answer, correct_answer, name)
        counter += 1
        end_game(counter, user_answer, correct_answer, name)


def progression_question():
    """This function starts game for brain progression."""
    name = welcome_user()
    print('What number is missing in the progression?')
    global counter
    while counter < winscore:
        question, correct_answer = progres_question()
        user_answer = get_user_answer(question)
        compare_answer(user_answer, correct_answer, name)
        counter += 1
        end_game(counter, user_answer, correct_answer, name)


def brain_gcd():
    """This function starts game for gcd."""
    name = welcome_user()
    print('Find the greatest common divisor of given numbers.')
    global counter
    while counter < winscore:
        question, num_1, num_2 = gcd_question()
        user_answer = get_user_answer(question)
        correct_answer = gcd_answer(num_1, num_2)
        compare_answer(user_answer, correct_answer, name)
        counter += 1
        end_game(counter, user_answer, correct_answer, name)
