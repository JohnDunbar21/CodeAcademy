def get_daily_movie():
    print('Retrieving the movie set to play on today\'s flight...')
    return 'Parasite'


def get_licensed_movies():
    print('Retrieving the list of licensed movies from the database...')
    licensed_movies = ['Parasite', 'Nomadland', 'Roma']
    return licensed_movies


def get_wifi_status():
    print('Checking WiFi signal...')
    print('WiFi is inactive')
    return False