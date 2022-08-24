#!/usr/bin/env python3


from random import randint
from random import choice
import prompt
import string
from brain_games.cli import welcome_user
from brain_games.games.even_game import even_question
from brain_games.games.even_game import is_even
from brain_games.games.prime_game import prime_question
from brain_games.games.prime_game import is_prime
from brain_games.games.calc_game import calc_question
from brain_games.games.calc_game import calc_answer
from brain_games.games.progression_game import progres_question
from brain_games.games.progression_game import progres_answer


def greet():
    """This function welcomes User to the Game."""
    print('Welcome to the Brain Games!')


lower_limit = 1
upper_limit = 100


def create_number():
    """This function creates random number."""
    random_number = randint(lower_limit, upper_limit)
    return random_number


def get_user_answer(question):
    print(question, end='')
    user_answer = prompt.string('Your answer: ')
    return user_answer


counter = 0
winscore = 3


def compare_answer(user_answer, correct_answer, name):
    """This function compares user and correct answer."""
    if user_answer != correct_answer:
        print(f" '{user_answer}' is wrong answer ;(. Correct answer was '{correct_answer}'.\n Let's try again, {name}!")

    elif user_answer == correct_answer:
        print('Correct!')
        print(f" '{user_answer}' is right answer ;(. Correct answer was '{correct_answer}'.\n Let's try again, {name}!")

        
def brain_even():
    """This function starts game for brain even."""
    name = welcome_user()
    print('Answer "yes" if the number is even, otherwise answer "no".')
    global counter
    while counter < winscore:
        random_number = create_number()
        question = even_question(random_number)
        user_answer = get_user_answer(question)
        correct_answer = is_even(random_number)
        compare_answer(user_answer, correct_answer, name, random_number)
        counter += 1
        if user_answer != correct_answer:
            break
        if counter == 3:
            print(f"Congratulations, {name}!")


def brain_prime():
    """This function starts game for brain prime."""
    name = welcome_user()
    print('Answer "yes" if given number is prime. Otherwise answer "no".')
    global counter
    while counter < winscore:
        random_number = create_number()
        question = prime_question(random_number)
        user_answer = get_user_answer(question)
        correct_answer = is_prime(random_number)
        compare_answer(user_answer, correct_answer, name, random_number)
        counter += 1
        if user_answer != correct_answer:
            break
        if counter == 3:
            print(f"Congratulations, {name}!")


operand_list = ['+']
operand = choice(operand_list)


def calculation_question():
    """This function starts game for brain calc."""
    name = welcome_user()
    print('What is the result of the expression?')
    global counter
    global operand_list
    while counter < winscore:
        num_1 = create_number()
        num_2 = create_number()
        operand = choice(operand_list)
        question = calc_question(num_1, num_2, operand)
        user_answer = get_user_answer(question)
        correct_answer = calc_answer(operand, num_1, num_2)
        compare_answer(user_answer, correct_answer, name)
        counter += 1
        if user_answer != correct_answer:
            break
        if counter == 3:
            print(f"Congratulations, {name}!")


def progression_question():
    """This function starts game for brain progression."""
    name = welcome_user()
    print('What number is missing in the progression?')
    global counter
    while counter < winscore:
        question = progres_question()
        user_answer = get_user_answer(question)
        
        correct_answer = progres_answer(i_replace, progression)
        compare_answer(user_answer, correct_answer, name)
        counter += 1
        if user_answer != correct_answer:
            break
        if counter == 3:
            print(f"Congratulations, {name}!")

     


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



 
