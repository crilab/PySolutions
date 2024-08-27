import calc

def main():
    h1 = ''
    h2 = ''
    h3 = ''

    while True:
        calc.header(h1, h2, h3)
        o = calc.get_operation()
        a = calc.get_number('a')
        b = calc.get_number('b')

        if o == '+':
            c = a + b
        elif o == '-':
            c = a - b
        elif o == '*':
            c = a * b
        elif o == '/':
            c = a / b
        
        h1 = h2
        h2 = h3
        h3 = f'{a} {o} {b} = {c}'

if __name__ == '__main__':
    main()
