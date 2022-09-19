import prompt
from brain_games.cli import welcome_user


ROUNDS = 3


def run_game(game):
    print('Welcome to the Brain Games!')
    name = welcome_user()
    print(game.DESCRIPTION)
    for _ in range(ROUNDS):
        question, correct_answer = game.generate_question_answer()
        print(question, end='')
        user_answer = prompt.string('Your answer: ')
        if user_answer != correct_answer:
            print(f"'{user_answer}' is wrong answer ;(.")
            print(f"Correct answer was '{correct_answer}'.")
            print(f"Let's try again, {name}!")
            break
        elif user_answer == correct_answer:
            print('Correct!')
        if ROUNDS == 3:
            print(f"Congratulations, {name}!")
