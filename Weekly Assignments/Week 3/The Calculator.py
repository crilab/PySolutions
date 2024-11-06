import os

h1 = ''
h2 = ''
h3 = ''

while True:
    os.system('clear')

    print('----------------------------')
    print('The Calculator'.center(28))
    print('----------------------------')
    print(h1.center(28))
    print(h2.center(28))
    print(h3.center(28))
    print('----------------------------')
    print(' add | Add two numbers')
    print(' sub | Subtract two numbers')
    print(' mul | Multiply two numbers')
    print(' div | Divide two numbers')
    print('----------------------------')

    operation = input(' > ')

    if operation not in ('add', 'sub', 'mul', 'div'):
        input('ERROR: invalid operation')
        continue

    while True:
        try:
            a = float(input(' a = '))
            b = float(input(' b = '))
            break
        except ValueError:
            print('ERROR: invalid float')

    if operation == 'add':
        op = '+'
        c = a + b
    elif operation == 'sub':
        op = '-'
        c = a - b
    elif operation == 'mul':
        op = '*'
        c = a * b
    elif operation == 'div':
        op = '/'
        try:
            c = a / b
        except ZeroDivisionError:
            c = 'Infinity'
    
    h1 = h2
    h2 = h3
    h3 = f'{a} {op} {b} = {c}'
