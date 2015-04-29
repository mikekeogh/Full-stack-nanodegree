""" media.py

Class to hold movie information for a movie preview webpage

"""
import webbrowser

# define a Movie class to hold movie data for movie website
class Movie():

    # initialize the object and assign instance variables
    def __init__(self, movie_title, release_date, movie_storyline, poster_image, trailer_youtube):
        """ class Movie

            Simple class to hold data for a movie.
        """
        self.title = movie_title
        self.release_date = release_date
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

    def show_trailer(self):
        """ Movie.showtrailer()

            If the link exists, opens the youtube page to show the movie trailer associtate with the Movie
        """
        if len(self.trailer_youtube_url) > 0:
            webbrowser.open(self.trailer_youtube_url, new=1)

