#!/usr/bin/env python3

from random import randint
from random import choice
import prompt

def greet():
    """This function welcomes User to the Game."""
    print('Welcome to the Brain Games!')

lower_limit = 1
upper_limit = 100

def create_number():
    """This function creates random number."""
    create_number.random_number=randint(lower_limit,upper_limit)
    return create_number.random_number



def is_even():
    """This function returns if the random number is even or not."""
    if create_number.random_number % 2 == 0:
        return True
    else:
        return False

def question_user():
    """This function asks for three times the user to say if the number is even or not and responds to him correspodingly if he is correct or not."""
    create_number()
    Question = f'Question: {create_number.random_number}' + "\n"
    print(Question, end='')
    user_answer = prompt.string('Your answer: ')
    if (is_even() == True and user_answer == "yes") or (is_even() == False and user_answer == "no"):
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