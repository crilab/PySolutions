import os


def width():
    return 28


def clear():
    if os.name == 'nt':
        os.system('cls')
    elif os.name == 'posix':
        os.system('clear')


def echo(text):
    print(text)


def line():
    print('-' * width())


def center(text):
    print(text.center(width()))
