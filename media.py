class Movie:
    """Class to store information about one movie

    Attributes:
        title: a string containig the title of a movie
        overview: a string containing the overview of a movie
        poster_image_url: a string contaning the url to the poster of a movie
        trailer_youtube_url: a string containing the url to the youtube trailer
            of a movie
    """
    def __init__(self, title, overview, url_poster, url_trailer):
        self.title = title
        self.overview = overview
        self.poster_image_url = url_poster
        self.trailer_youtube_url = url_trailer
