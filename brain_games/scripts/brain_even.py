from brain_games.cli import welcome_user
from brain_games.scripts.brain_games import greet
from brain_games.logic.games_logic import even_question


def game_even():
    counter = 0
    winscore = 2
    name = welcome_user()
    print('Answer "yes" if the number is even, otherwise answer "no".')
    while counter <= winscore:
        if even_question() is False:
            print(f'Let\'s try again, {name}!')
            break
        elif even_question() is True:
            print("Correct")
            counter += 1
    if counter == 3:
        print(f"Congratulations, {name}!")


def main():
    greet()
    game_even()
    if __name__ == '__main__':
        main()
