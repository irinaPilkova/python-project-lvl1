from random import randint


DESCRIPTION = 'What number is missing in the progression?'


def generate_question_answer():
    """This function defines the question for the game."""
    num = randint(2, 6)
    i_replace = randint(2, 9)
    progression = [(i * num) for i in range(1, 11)]
    correct_answer = progression[i_replace]
    progression[i_replace] = '..'
    progression = [str(a) for a in progression]
    progression = " ".join(progression)
    question = f'Question: {progression}' + "\n"
    return question, str(correct_answer)
