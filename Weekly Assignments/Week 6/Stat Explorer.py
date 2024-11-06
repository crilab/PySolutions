import api


def main():
    print('STAT EXPLORER')
    print('*************')

    year = input('Year: ')

    if year not in api.list_seasons():
        print('ERROR: invalid season')
        exit(1)

    home_score = int(input('Home score: '))
    away_score = int(input('Away score: '))

    print('-------------')

    for gameday in api.list_gamedays(year):
        for game in api.list_games(year, gameday):
            home = game['score']['home']
            away = game['score']['away']
            if home_score == home['goals'] and away_score == away['goals']:
                print(f'[{gameday}/{year}] ({home["goals"]}) {home["team"].center(23)} - {away["team"].center(23)} ({away["goals"]})')

if __name__ == '__main__':
    main()
