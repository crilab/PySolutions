import random

correct = random.randint(0, 99)
guesses = 0
guess = None

print('HIGHER LOWER')
print('------------')

while guess != correct:
    try:
        guess = int(input('> '))
    except ValueError:
        print('ERROR: invalid guess')
        continue
    
    guesses += 1
    
    if guess < correct:
        print('Higher!')
    elif correct < guess:
        print('Lower!')

print('------------')
print(guess, 'is correct!')
print('It took you', guesses, 'guesses.')
