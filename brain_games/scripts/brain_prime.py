#!/usr/bin/env python3


from brain_games.scripts.brain_games import greet
from brain_games.cli import welcome_user
from brain_games.logic.games_logic import prime_question


def game_prime():
    name = welcome_user()
    counter = 0
    winscore = 2
    print('Answer "yes" if given number is prime. Otherwise answer "no".')
    while counter <= winscore:
        if prime_question() is False:
            print(f" '{prime_question.user_answer}' is wrong answer ;(. Correct answer was '{prime_question.correct_answer}'.\n Let's try again, {name}!")
            break
        elif prime_question() is True:
            print('Correct!')
            counter += 1
    if counter == 3:
        print(f"Congratulations,{name}!")


def main():
    greet()
    game_prime()
    if __name__ == '__main__':
        main()
