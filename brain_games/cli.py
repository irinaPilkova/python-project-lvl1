import prompt

def welcome_user():
        name = prompt.string('May I have your name?')
        welcome = 'Hello,' + ' ' + name + '!'
        print(welcome)
        return name
