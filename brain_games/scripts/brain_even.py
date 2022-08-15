from random import randint
from brain_games.cli import welcome_user
from brain_games.scripts.brain_games import greet
import prompt
from brain_games.logic.games_logic import create_number
from brain_games.logic.games_logic import is_even
from brain_games.logic.games_logic import question_user


def game_quiz():
    counter = 0
    winscore = 2
    name = welcome_user()
    print('Answer "yes" if the number is even, otherwise answer "no".')
    while counter <= winscore:
        counter += 1
        if question_user() is False:
            print(f'Let\'s try again, {name}!')
            break
        elif question_user() is True:
            print("Correct") 
    if counter == 3:
        print(f"Congratulations, {name}!")

def main():
    greet()
    game_quiz()
    if __name__ == '__main__':
        main()

