line = '------------'

print('Fame Matcher')
print(line)
print()
gender = input('Gender: ')
hair_color = input('Hair color: ')
eye_color = input('Eye color: ')
print()
print(line)
print()

matching = ''

# STUDENTS MUST ADD FIVE ADDITIONAL PEOPLE
if gender == 'female':
    if hair_color == 'brown':
        if eye_color == 'brown':
            matching = 'Emma Watson, Selena Gomez'
elif gender == 'male':
    if hair_color == 'brown':
        if eye_color == 'brown':
            matching = 'Daniel Radcliffe'
    elif hair_color == 'red':
        if eye_color == 'blue':
            matching = 'Rupert Grint'

if not matching:
    print('ERROR: No match found')
else:
    print('MATCH:', matching)
