from classes.Review import Review


class Movie:
    def __init__(self, title):
        self.title = title
        

    def get_title(self):
        return self._title
        
    def set_title(self, title):
        if isinstance(title, str) and 0 < len(title):
            self._title = title

    title = property(get_title, set_title)

    # title property goes here!

    def reviews(self):
        movie_reviews = []
        for review in Review.all:
            if review.movie == self:
                movie_reviews.append(review)
        return movie_reviews

    def reviewers(self):
        movie_viewers = []
        for review in self.reviews():
            movie_viewers.append(review.viewer)
        return movie_viewers

    def average_rating(self):
        ratings = []
        for review in self.reviews():
            ratings.append(review.rating)
        average = sum(ratings) / len(ratings)
        return average
      

   
    @classmethod
    def highest_rated(cls):
        pass
