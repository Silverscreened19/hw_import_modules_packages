from spotify_recommender_api.recommender import start_api
import pandas as pd
from pprint import pprint


class Spotify:
    def __init__(self):
        self.playlist_url = 'https://open.spotify.com/playlist/2cecCJBniq9b428qiF0lJt?si=3c6c2e11eb4c4750'
        self.playlist_id = '2cecCJBniq9b428qiF0lJt'
        self.user_id = 'smedjan'

    def csv_info(self):
        api = start_api(playlist_url=self.playlist_url, user_id=self.user_id)
        return api.playlist_to_csv()

    def playlist(self):
        api = start_api(playlist_url=self.playlist_url, user_id=self.user_id)
        pprint(api.get_playlist())

    def most_listened_songs(self, time_range, K):
        api = start_api(playlist_url=self.playlist_url, user_id=self.user_id)
        pprint(api.get_most_listened(time_range=time_range, K=K))

    def trending_genres(self, time_range):
        api = start_api(playlist_url=self.playlist_url, user_id=self.user_id)
        pprint(api.get_playlist_trending_genres(time_range=time_range))


if __name__ == '__main__':
    spotify = Spotify()
    spotify.csv_info()
    spotify.playlist()
    spotify.most_listened_songs('long', 15)
    spotify.trending_genres('month')
