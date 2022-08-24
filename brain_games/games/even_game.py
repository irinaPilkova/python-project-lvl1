#!/usr/bin/env python3


def even_question(random_number):
    """This function defines the question for the game."""
    question = f'Question: {random_number}' + "\n"
    return question


def is_even(random_number):
    """This function returns if the random number is even or not."""
    if random_number % 2 == 0:
        correct_answer = "yes"
    else:
        correct_answer = "no"
    print(random_number, correct_answer)
    return correct_answer







def game_even():
    print('Answer "yes" if the number is even, otherwise answer "no".')
    while counter <= winscore:
        even_question()
        if compare_answers() is False:
            print(f'Let\'s try again, {name}!')
            break
        elif compare_answers() is True:
            print("Correct")
            counter += 1
    if counter == 3:
        print(f"Congratulations, {name}!")







def compare_answers():
    correct_answer = even_question
    user_answer = get_user_answer()
    if (correct_answer == "yes" and user_answer == "yes") or (correct_answer == "no" and user_answer == "no"):
        return True
    else:
        return False