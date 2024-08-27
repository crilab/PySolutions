import requests

url = 'https://football-frenzy.s3.eu-north-1.amazonaws.com/api'

line = '-----------------'

print('.:STAT EXPLORER:.')
print(line)
print('1 | Exact score')
print('2 | Total goals')
print('3 | Goals under')
print(line)

selection = int(input('Selection: '))
if selection < 0 or 3 < selection:
    print('ERROR: selection is not in the range 0-3')
    exit(1)

year = int(input('Year: '))
if year < 1980 or 2018 < year:
    print('ERROR: year is not in the range 1980-2018')
    exit(1)

'''
I apply a predicate here to reuse the same loop for all selections.

However, we don't expect all students to fully understand this approach.

It is acceptable if the students copy and paste the loop into the different selections.

Just make sure the calculations are correct.
'''

if selection == 1:
    home_score = int(input('Home score: '))
    away_score = int(input('Away score: '))
    predicate = lambda game: game['score']['home']['goals'] == home_score and game['score']['away']['goals'] == away_score

elif selection == 2:
    total_goals = int(input('Total goals: '))
    predicate = lambda game: game['score']['home']['goals'] + game['score']['away']['goals'] == total_goals

elif selection == 3:
    goals_under = int(input('Goals under: '))
    predicate = lambda game: game['score']['home']['goals'] + game['score']['away']['goals'] < goals_under

games_matching = 0
games_total = 0
dates_printed = []
gamedays = requests.get(url + f'/{year}').json()['gamedays']
for gameday in gamedays:
    gameday_data = requests.get(url + f'/{year}/{gameday}').json()
    
    date = gameday_data['date']
    games = gameday_data['games']

    for game in games:
        games_total += 1
        if predicate(game):
            games_matching += 1

            if date not in dates_printed:
                print('\n')
                print(date.center(31))
                print('-' * 31)
                dates_printed.append(date)

            home_team = game['score']['home']['team'].split()[0]
            home_score = game['score']['home']['goals']
            away_team = game['score']['away']['team'].split()[0]
            away_score = game['score']['away']['goals']
            print(f'{home_score} - {away_score} [{home_team} - {away_team}]')

games_matching_percent = round(100 * games_matching / games_total, 1)
print('\n')
print(line)
print(f'Matching games: {games_matching} of {games_total} ({games_matching_percent}%)')
