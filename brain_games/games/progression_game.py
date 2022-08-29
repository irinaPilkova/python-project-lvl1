#!/usr/bin/env python3


from random import randint


def progres_question():
    """This function defines the question for the game."""
    num = randint(2, 6)
    i_replace = randint(1, 10)
    progression = [(i * num) for i in range(1, 11)]
    correct_answer = progression[i_replace]
    progression[i_replace]= '..'
    progression = [str(a) for a in progression]
    progression = " ".join(progression)
    question = f'Question: {progression}' + "\n"
    return question, str(correct_answer)
