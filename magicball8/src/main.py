from random import choice
from rich.console import Console
from rich import print
from rich.panel import Panel
from rich.progress import track
from time import sleep

stop = None
console = Console()

answers = ["Undoubtedly", "I think so", "It's not clear yet, try again", "Don't even think about it",
           "It's a foregone conclusion", "Most likely", "Ask me later", "My answer is no",
           "No doubt about it", "Good prospects", "It's better not to tell", "According to my data, no",
           "You can be sure of that", "Yes", "Concentrate and ask again", "Very doubtful"]

hi = ['What\'s up!', 'I haven\'t seen you in a while!', 'Long time no see!', 'Wagwan!',
      'Hiya!', 'Hey. There you are!']


def hello():
    console.print(Panel('''Hello World, I am a magic ball, and
I know the answer to any of your questions.
Just write your question!''', title='[yellow]Magic ball 8'), justify='center')
    name()


def name():
    global user_name
    console.print(
        '[yellow] -- [i]We would like to know your name[/i] -- [/yellow]')
    user_name = input('your name: ')
    console.print(Panel(f'{choice(hi)}[red] {user_name}[/red].'))
    playing()


def playing():
    console.print(
        '[yellow] -- [i]What do you want to ask me?[/i] -- [/yellow]')
    ask = input('your question: ')
    if not is_valid(ask):
        console.print(
            Panel('Such a short question? From five characters', title='[red]Error'))
        playing()
    else:
        for _ in track(range(50), description='[green]Processing...'):
            sleep(0.03)
        console.print(Panel(
            f'{choice(answers)}, [red]{user_name}[/red]!', title='[yellow]Magic ball 8'))
        ask_continue()


def is_valid(value):
    return len(value) >= 5


def ask_continue():
    match console.input('[red]don\'t you want to continue? (+/-) [/red]'):
        case '+':
            playing()
        case '-':
            console.print(
                '[blue](͡° ͜ʖ ͡°) Come back if you have any questions! (͡° ͜ʖ ͡°)', justify='center')
        case _:
            console.print(
                Panel('Something\'s wrong. Don\'t enter it.', title='[red]Error'))
            ask_continue()


if __name__ == '__main__':
    hello()
