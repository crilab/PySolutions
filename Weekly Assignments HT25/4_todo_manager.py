print('.: TODO MANAGER :.')
print('------------------')
print('list | List todos')
print('add  | Add todo')
print('rm   | Remove todo')
print('------------------')

todos = []

while True:
    operation = input('> ')

    if operation == 'list':
        for todo in todos:
            print('-', todo)

    elif operation == 'add':
        todo = input('todo > ')
        if todo not in todos:
            todos.append(todo)
            print('SUCCESS: todo added')
        else:
            print('ERROR: todo already exists')
    
    elif operation == 'rm':
        todo = input('todo > ')
        try:
            todos.remove(todo)
            print('SUCCESS: todo removed')
        except ValueError:
            print('ERROR: todo not found')
