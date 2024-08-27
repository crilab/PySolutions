import os
import json


def clear():
    if os.name == 'nt':
        os.system('cls')
    elif os.name == 'posix':
        os.system('clear')


def line():
    print('---------------')


def header(notes):
    clear()
    print('.:  ALWAYSNOTE  :.')
    print('-- gold edition --')
    print('******************')
    for note in notes:
        print('-', note)
    line()
    print('view | view note')
    print('add  | add note')
    print('rm   | remove note')
    print('exit | exit program')
    line()


def load_notes():
    with open('notes.json') as f:
        return json.loads(f.read())


def save_notes(notes):
    with open('notes.json', 'w') as f:
        f.write(json.dumps(notes))


def main():
    notes = load_notes()
    while True:
        header(notes)

        operation = input('menu > ').lower()

        if operation == 'view':
            note = input('note > ')
            line()
            try:
                print(notes[note])
            except KeyError:
                print('ERROR: Note not found')
        
        elif operation == 'add':
            note = input('note > ')
            text = input('Text > ')
            notes[note] = text
            continue
        
        elif operation == 'rm':
            note = input('note > ')
            line()
            try:
                del notes[note]
                continue
            except KeyError:
                print('ERROR: note not found')
        
        elif operation == 'exit':
            save_notes(notes)
            exit(0)
        
        line()
        input('Press enter to continue...')


if __name__ == '__main__':
    main()
