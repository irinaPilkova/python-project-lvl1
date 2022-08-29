#!/usr/bin/env python3


from random import randint


def progres_question():
    """This function defines the question for the game."""
    num = randint(2, 6)
    i_replace = randint(1, 10)
    progression = [(i * num) for i in range(1, 11)]
    correct_answer = progression[i_replace]
    progression[i_replace] = '..'
    question = f'Question: {progression}' + "\n"
    print(correct_answer)
    return question, str(correct_answer)


def progres_answer(i_replace, progression):
    """This function defines the correct answer for the game."""
    i_replace = progres_question(i_replace)
    progression = progres_question(progression)
    correct_answer = progression[i_replace]
    
    return correct_answer