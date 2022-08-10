from random import choice
stop = None

#TODO:

answers = ["Undoubtedly", "I think so", "It's not clear yet, try again", "Don't even think about it",
           "It's a foregone conclusion", "Most likely", "Ask me later", "My answer is no",
           "No doubt about it", "Good prospects", "It's better not to tell", "According to my data, no",
           "You can be sure of that", "Yes", "Concentrate and ask again", "Very doubtful"]

hi = ['What\'s up', 'I haven\'t seen you in a while', 'Long time no see', 'Wagwan'
      'Hiya!', 'Hey! There you are!']

def hello():
    console.print(Panel('''Hello World, I am a magic ball, and
I know the answer to any of your questions.
Just write your question!''', title='[yellow]Guessing number'), justify='center')


def name():
    global user_name
    user_name = input('By the way, what\'s your name?: ')
    print(f'{choice(hi)}, {user_name}!\n')

def playing():
    global user_name
    ask = input('[?] What do you want to ask me? >> ')
    if not is_valid(ask):
        print('[!] Such a short question? From five characters. \n')
        ask_continue()
    else:
        print(f'{choice(answers)}, {user_name}!')
        ask_continue()

def is_valid(value):
    return len(value) >= 5

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
name()
playing()