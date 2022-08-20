#!/usr/bin/env python3

from random import randint
from random import choice
import prompt
import string


def greet():
    """This function welcomes User to the Game."""
    print('Welcome to the Brain Games!')


lower_limit = 1
upper_limit = 100


def create_number():
    """This function creates random number."""
    create_number.random_number = randint(lower_limit, upper_limit)
    return create_number.random_number


def is_even():
    """This function returns if the random number is even or not."""
    if create_number.random_number % 2 == 0:
        return True
    else:
        return False


def even_question():
    """This function asks if the number is even or not and returns correspodingly if he is correct or not."""
    create_number()
    Question = f'Question: {create_number.random_number}' + "\n"
    print(Question, end='')
    user_answer = prompt.string('Your answer: ')
    if (is_even() is True and user_answer == "yes") or (is_even() is False and user_answer == "no"):
        return True
    else:
        return False


num_1 = create_number()
num_2 = create_number()
operand_list = ['+', '-', '*']


def calc_question():
    operand = choice(operand_list)
    if operand == '+':
        Question = f'Question: {num_1} + {num_2}' + "\n"
        print(Question, end='')
        calc_question.user_answer = prompt.string('Your answer: ')
        calc_question.correct_answer = num_1 + num_2
        return calc_question.user_answer, calc_question.correct_answer
    elif operand == '-':
        Question = f'Question: {num_1} - {num_2}' + "\n"
        print(Question, end='')
        calc_question.user_answer = prompt.string('Your answer: ')
        calc_question.correct_answer = num_1 - num_2
        return calc_question.user_answer, calc_question.correct_answer
    elif operand == '*':
        Question = f'Question: {num_1} * {num_2}' + "\n"
        print(Question, end='')
        calc_question.user_answer = prompt.string('Your answer: ')
        calc_question.correct_answer = num_1 * num_2
        return calc_question.user_answer, calc_question.correct_answer


def gcd_question():
    Question = f'Question: {num_1}  {num_2}' + "\n"
    print(Question, end='')
    gcd_question.user_answer = prompt.string('Your answer: ')
    if num_1 == 0:
        return num_1
    if num_2 == 1 or num_2 == 1:
        return 1
    return gcd_question(num_2, num_1%num_2)
    if gcd_question.user_answer == gcd_question(num_2, num_1%num_2):
        print(True)
    else:
        print(False)


def progression_question():
    num = randint(2, 6)
    i_replace = randint(0, 10)
    progression = [(i * num) for i in range(1, 11)]
    progression_question.correct_answer = progression[i_replace]
    progression[i_replace] = '..'
    Question = f'Question: {progression}' + "\n"
    print(Question, end='')
    print(progression_question.correct_answer)
    progression_question.user_answer = prompt.string('Your answer: ')
    if str(progression_question.correct_answer) == progression_question.user_answer:
        print(True)
        return True
    else:
        print(False)
        return False


def is_prime():
    """This function returns if the random number is prime or not."""
    for i in range(2, create_number.random_number):
        if create_number.random_number % i == 0:
            return False
            break
    else:
        return True


def prime_question():
    create_number()
    Question = f'Question: {create_number.random_number}' + "\n"
    print(Question, end='')
    prime_question.user_answer = prompt.string('Your answer: ')
    if is_prime() is True and prime_question.user_answer == "yes": 
        prime_question.correct_answer = "yes"
        print(True)
        return True
    elif is_prime() is False and prime_question.user_answer == "no":
        prime_question.correct_answer = "no"
        print(True)
        return True
    else:
        prime_question.correct_answer = "no"
        print(False)
        return False
    
