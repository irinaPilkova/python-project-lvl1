from random import randint


LOWER_LIMIT = 1
UPPER_LIMIT = 100


DESCRIPTION = 'Answer "yes" if the number is even, otherwise answer "no".'


def generate_question_answer():
    """This function defines the question for the game."""
    random_number = randint(LOWER_LIMIT, UPPER_LIMIT)
    question = f'Question: {random_number}' + "\n"
    if random_number % 2 == 0:
        correct_answer = "yes"
    else:
        correct_answer = "no"
    return question, correct_answer
