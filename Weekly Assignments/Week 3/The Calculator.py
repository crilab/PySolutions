import os

width = 28
line = '-' * width
h1 = ''
h2 = ''
h3 = ''

def get_number(var):
    '''
    Functions are not required for the assignment.
    '''
    while True:
        value = input(var + ' = ')
        print(line)
        try:
            return float(value)
        except ValueError:
            print(f'ERROR: Invalid float ({value})'.center(width))
            print(line)

while True:
    os.system('clear')

    print(line)
    print('The Calculator'.center(width))
    print(line)
    print(h1.center(width))
    print(h2.center(width))
    print(h3.center(width))
    print(line)
    print(' add | Add two number')
    print(' sub | Subtract two numbers')
    print(' mul | Multiply two numbers')
    print(' div | Divide two numbers')
    print(line)
    op = input(' > ')
    print(line)

    if op != 'add' and op != 'sub' and op != 'mul' and op != 'div':
        print(f'ERROR: Unknown operation ({op})'.center(width))
        print(line)
        input('Press enter to continue...')
        continue

    a = get_number('a')
    b = get_number('b')
    
    if op == 'add':
        op = '+'
        c = a + b
    elif op == 'sub':
        op = '-'
        c = a - b
    elif op == 'mul':
        op = '*'
        c = a * b
    elif op == 'div':
        op = '/'
        c = a / b
    
    h1 = h2
    h2 = h3
    h3 = f'{a} {op} {b} = {c}'
