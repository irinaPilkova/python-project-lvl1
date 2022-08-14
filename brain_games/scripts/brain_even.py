from random import randint
from brain_games.cli import welcome_user
import prompt

def game_explanation():
    print('Answer "yes" if the number is even, otherwise answer "no".')

lower_limit = 1
upper_limit = 100

def create_number():
    """This function creates random number."""
    random_number=randint(lower_limit,upper_limit)
    return random_number



def is_even():
    """This function returns if the random number is even or not."""
    random_number = create_number()
    if random_number % 2 == 0:
        return True
    else:
        return False


def question_user():
    """This function asks for three times the user to say if the number is even or not and responds to him correspodingly if he is correct or not."""
    
    random_number = create_number()
    Question = "Question: " + str(random_number) + "\n"
    print(Question, end='')
    user_answer = prompt.string('Your answer: ')
    if (is_even() == True and user_answer == "yes") or (is_even() == False and user_answer == "no"):
            print("Correct") 
            return True
    else:
            print(f'Let\'s try again!')
            return
    

def game_quiz():
    correct_answer = 0
    winscore = 3
    name = welcome_user()
    while correct_answer != winscore:
            if question_user() == True:
                question_user()
                correct_answer += 1
            else:
                return
    print(f"Congratulations,{name}!")

def main():
    game_explanation()
    game_quiz()
    if __name__ == '__main__':
        main()

