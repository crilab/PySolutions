print('COMPANY LOOKUP')
print('--------------')

country = input('Country: ')
sector = input('Sector: ')

match = ''

if country == 'sweden':
    if sector == 'food':
        match = 'Ica Gruppen AB'
    elif sector == 'construction':
        match = 'Skanska AB'
elif country == 'usa':
    if sector == 'food':
        match = 'Walmart Inc'
    elif sector == 'construction':
        match = 'Bechtel Group Inc'

if match == '':
    print('ERROR: No match found!')
else:
    print('MATCH:', match)
