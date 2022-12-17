from application.salary import calculate_salary
from application.db.people import get_employees
from datetime import date
from spoti import Spotify


if __name__ == '__main__':
    calculate_salary()
    get_employees()
    print(date.today())
    spotify = Spotify()
    spotify.csv_info()
    spotify.playlist()
    spotify.most_listened_songs('long', 15)
    spotify.trending_genres('month')
