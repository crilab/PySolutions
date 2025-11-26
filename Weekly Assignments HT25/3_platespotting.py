"""
I will consider adding a requirement to check for valid plates in the future, but it isn't required at the moment.
"""

looking_for = 1

while looking_for <= 999:
    current_plate = input('> ')
    current_plate_num = int(current_plate[-3:])
    if current_plate_num == looking_for:
        print(f'Progress [{current_plate}]')
        looking_for += 1

print('The End!')
