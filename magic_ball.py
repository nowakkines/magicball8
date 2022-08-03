from random import choice
STOP_GAME = None

#FIXME:
#TODO: is_valid, ability to continue

answers = ["Undoubtedly", "I think so", "It's not clear yet, try again", "Don't even think about it",
           "It's a foregone conclusion", "Most likely", "Ask me later", "My answer is no",
           "No doubt about it", "Good prospects", "It's better not to tell", "According to my data, no",
           "You can be sure of that", "Yes", "Concentrate and ask again", "Very doubtful"]


def hello():
    global name
    print('''
*** Hello World, I am a magic ball, and
I know the answer to any of your questions.
Just write your question ***
    ''')
    match 'Max':
        case len(1):
            print('123')
    # name = '' #input('[?] Tell me your name >> ')'
    # print(f'Hello, {name}!\n')


def playing():
    global name
    ask = 'Am I stupid?' #input('[?] What do you want to ask me? >> ')
    print(f'{choice(answers)}, {name}!')
    ask_continue()

def ask_continue():
    match input('[?] Again? (+/-) '):
        case '+':
            playing()
        case '-':
            print('Come back if you have any questions!')
        case _:
            print('Something\'s wrong. Don\'t enter it.')
            ask_continue()


hello()
playing()