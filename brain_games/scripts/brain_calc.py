from brain_games.scripts.brain_games import greet
from brain_games.logic.games_logic import calc_question
from brain_games.cli import welcome_user
import prompt


def game_calc():
    name = welcome_user()
    counter = 0
    winscore = 2
    print("What is the result of the expression?")
    while counter <= winscore:
        calc_question()
        if str(calc_question.correct_answer) != calc_question.user_answer:
            print(f" '{calc_question.user_answer}' is wrong answer ;(. Correct answer was '{calc_question.correct_answer}'.\n Let's try again, {name}!")
            break
        elif str(calc_question.correct_answer) == calc_question.user_answer:
            print('Correct!')
            counter += 1
    if counter == 3:
        print(f"Congratulations,{name}!")

def main():
    greet()
    game_calc()
    
    if __name__ == '__main__':
        main()