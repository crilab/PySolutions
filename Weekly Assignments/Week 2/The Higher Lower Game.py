import random

line = '---------------------------'

print('.: The Higher Lower Game :.')
print(line)
print('Welcome to The Higher Lower')
print('Game. I  will  randomize  a')
print('number between  0  and  99.')
print('Can you guess it?')
print(line)

secret = random.randint(0, 99)
guesses = 0
guess = -1

while guess != secret:
    guess = int(input('Your guess > '))
    guesses += 1
    if guess < secret:
        print('Higher!')
    elif secret < guess:
        print('Lower!')

print(line)
print(guess, 'is correct!')
print('It took you', guesses, 'guesses.')
print('Good job!')
