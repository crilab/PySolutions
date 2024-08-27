import ui


def header(h1, h2, h3):
    ui.clear()
    ui.line()
    ui.center('The Calculator')
    ui.line()
    ui.center(h1)
    ui.center(h2)
    ui.center(h3)
    ui.line()
    ui.echo(' add | Add two number')
    ui.echo(' sub | Subtract two numbers')
    ui.echo(' mul | Multiply two numbers')
    ui.echo(' div | Divide two numbers')
    ui.line()


def error(msg):
    ui.center(f'ERROR: {msg}')
    ui.line()


def get_number(var_name):
    while True:
        value = input(var_name + ' = ')
        ui.line()
        try:
            return float(value)
        except ValueError:
            error('Invalid float ({value})')


def get_operation():
    while True:
        operation = input(' > ')
        ui.line()
        if operation == 'add':
            return '+'
        elif operation == 'sub':
            return '-'
        elif operation == 'mul':
            return '*'
        elif operation == 'div':
            return '/'
        else:
            error(f'Unknown operation ({operation})')
