from classes.Review import Review
from classes.Movie import Movie


class Viewer:

    def __init__(self, username):
        self.username = username
        

    def get_username(self):
        return self._username

    def set_username(self, username):
        if isinstance(username, str) and 6 <= len(username) <= 16:
            self._username = username

    username = property(get_username, set_username)
    # username property goes here!

    def reviews(self):
        viewer_reviews = []
        for review in Review.all:
            if review.viewer == self:
                viewer_reviews.append(review)
        return viewer_reviews

    def reviewed_movies(self):
        viewer_movies = []
        for review in self.reviews():
            viewer_movies.append(review.movie)
        return viewer_movies
        

    def movie_reviewed(self, movie):
        pass

    def rate_movie(self, movie, rating):
        pass
