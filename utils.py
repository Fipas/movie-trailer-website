import urllib
import json
import media

"""
This module contains utilities to fetch information about movies.

The Movie Database API is used.
Please visit https://developers.themoviedb.org/3/getting-started/introduction
in order to obtain an API key. It is not possible to fetch information without
one. If you don't want to obtain an API key, you can use the information
from movie_list.json to populate the website
"""

# Your API key for The Movie Database here
API_KEY = ''
# URL to obtain a list of movies sorted by current most popular
URL_LIST = 'https://api.themoviedb.org/3/discover/movie?page=1&include_video=true&include_adult=true&sort_by=popularity.desc&language=en-US&api_key={}'
# URL to obtain a list of videos for a given movie
URL_VIDEO = 'https://api.themoviedb.org/3/movie/{}/videos?api_key={}&language=en-US'


def find_trailer(id_movie):
    """Find a youtube trailer url for a given movie.

    Args:
        id_movie: the id, from The Movie Database, of the movie to search
            for a trailer.

    Returns:
        A youtube url containing a trailer for the movie with id id_movie
    """

    url_trailer = 'https://www.youtube.com/watch?v={}'
    connection = urllib.urlopen(URL_VIDEO.format(id_movie, API_KEY))
    data_json = json.loads(connection.read())

    for video in data_json['results']:
        if video['type'] == 'Trailer':
            connection.close()
            return url_trailer.format(video['key'])

    # If no trailer was found

    connection.close()
    return None


def generate_movie_list():
    """Generate a list of the most popular current movies

    Returns:
        A list of media.Movie objects containg the tile, overview, poster url
        and youtube url for each of the top 20 current popular movies (or less,
        if a trailer cannot be found for a movie)
    """

    movie_list = []

    connection = urllib.urlopen(URL_LIST.format(API_KEY))
    file_json = open('movie_list.json', 'w')
    data_json = json.loads(connection.read())

    for movie in data_json['results']:
        title = movie['title']
        overview = movie['overview'].encode('utf-8')
        url_poster = 'http://image.tmdb.org/t/p/w342/{}'.format(movie['poster_path'])
        url_trailer = find_trailer(movie['id'])

        # If no trailer was found, don't add the current movie to the list
        if url_trailer is None:
            continue

        movie_list.append(media.Movie(title, overview, url_poster, url_trailer))

    # The movie data is stored in json format to give an alternative to users
    # that don't want to generate an API key at The Movie Database
    json.dump(movie_list, file_json, default=lambda o: o.__dict__, indent=2)
    connection.close()
    file_json.close()

generate_movie_list()
