from application.salary import *
from application.db.people import *
from datetime import *
from spoti import *


if __name__ == '__main__':
    calculate_salary()
    get_employees()
    print(date.today())
    spotify = Spotify()
    spotify.csv_info()
    spotify.playlist()
    spotify.most_listened_songs('long', 15)
    spotify.trending_genres('month')
