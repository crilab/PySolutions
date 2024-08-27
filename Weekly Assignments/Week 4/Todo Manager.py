'''
Please be aware that students are no longer required to define their own functions, but it's good if they do.
'''

import os
import json


def clear_screen():
    if os.name == 'nt':
        os.system('cls')
    elif os.name == 'posix':
        os.system('clear')


def line():
    print('------------------')


def load_todos():
    with open('todos.json') as f:
        return json.loads(f.read())


def save_todos(todos):
    with open('todos.json', 'w') as f:
        f.write(json.dumps(todos))


def get_index(todos):
    while True:
        try:
            index = int(input('Index: '))
            todos[index]
            return index
        except ValueError:
            print('ERROR: invalid integer')
        except IndexError:
            print('ERROR: invalid index')


def main():
    todos = load_todos()
    operation = ''

    while True:
        clear_screen()
        
        print('.: Todo Manager :.')
        line()
        for i, todo in enumerate(todos):
            print(i, '|', todo)
        line()
        print('A | Add todo')
        print('C | Check todo')
        print('D | Delete todo')
        print('X | Exit program')
        line()

        operation = input('> ').upper()
        line()

        if operation == 'A':
            todo = input('Todo: ')
            todos.append('[ ] ' + todo)
            continue

        elif operation == 'C':
            '''
            This operation (and delete) gets stuck if the todos list is empty. Many students may encounter this issue without realising it.

            We should not penalize the students for this, but we should still recommend that they fix it.
            '''
            index = get_index(todos)
            todos[index] = '[X]' + todos[index][3:]
        
        elif operation == 'D':
            index = get_index(todos)
            del todos[index]
        
        elif operation == 'X':
            save_todos(todos)
            exit(0)
        
        else:
            print('ERROR: invalid operation')
            line()
            input('Press enter to continue...')


if __name__ == '__main__':
    main()
