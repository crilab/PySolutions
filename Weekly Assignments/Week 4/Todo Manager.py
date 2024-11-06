import os
import json

todos = []

while True:
    os.system('clear')

    print('.: Todo Manger :.')
    print('-----------------')

    for i, todo in enumerate(todos):
        print(i, '|', todo)
    
    print('-----------------')
    print('A | Add todo')
    print('C | Check todo')
    print('D | Delete todo')
    print('S | Save to file')
    print('L | Load from file')
    print('X | Exit program')
    print('-----------------')

    command = input('> ').upper()

    if command == 'A':
        todo = input('Todo > ')
        todos.append('[ ] ' + todo)

    elif command == 'C':
        try:
            index = int(input('Index > '))
            todos[index] = '[X]' + todos[index][3:]
        except (ValueError, IndexError):
            input('ERROR: invalid index')

    elif command == 'D':
        try:
            index = int(input('Index > '))
            del todos[index]
        except (ValueError, IndexError):
            input('ERROR: invalid index')

    elif command == 'S':
        f = open('todos.json', 'w')
        f.write(json.dumps(todos))
        f.close()

    elif command == 'L':
        f = open('todos.json')
        todos = json.loads(f.read())
        f.close()

    elif command == 'X':
        break

    else:
        input('ERROR: unknown command')
