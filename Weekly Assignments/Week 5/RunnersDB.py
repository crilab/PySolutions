import json

with open('registrations.json') as f:
    registrations = f.read()
    registrations = json.loads(registrations)

with open('results.json') as f:
    results = f.read()
    results = json.loads(results)

print('RunnersDB')
print('---------')
print()
print('1) Lookup registration')
print('2) List results (based on filter)')
print()

operation = input('What to do? ')
print()

if operation == '1':
    number = int(input('Runner\'s number? '))
    print()

    for registration in registrations:
        if registration['number'] == number:
            print('---------------------------')
            print('       REGISTRATION')
            print('---------------------------')
            print('NAME:', registration['name'])
            print('CITY:', registration['city'])
            print('NUMBER:', registration['number'])
            print('---------------------------')
            break

elif operation == '2':
    time = int(input('List participants fasten than what (sec)? '))
    print()

    for result in results:
        if result['time'] < time:
            print()
            print('-----')
            print('NUMBER: ', result['number'])
            print('TIME:', result['time'], 'sec')
            for registration in registrations:
                if registration['number'] == result['number']:
                    print('NAME:', registration['name'])
                    print('CITY:', registration['city'])
            print('-----')
            print()
