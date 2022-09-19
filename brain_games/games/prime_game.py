from random import randint

LOWER_LIMIT = 1
UPPER_LIMIT = 100


DESCRIPTION = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def is_prime(random_number):
    for i in range(2, random_number):
        if random_number % i == 0:
            is_prime = False
            break
    else:
        is_prime = True
    if random_number == 1:
        is_prime = False
    return is_prime


def generate_question_answer():
    """This function defines the question for the game."""
    random_number = randint(LOWER_LIMIT, UPPER_LIMIT)
    question = f'Question: {random_number}' + "\n"
    correct_answer = "yes" if is_prime(random_number) is True else "no"
    return question, correct_answer
