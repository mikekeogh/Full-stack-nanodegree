""" entertainmentcenter.py

Short program to create content for an example movie preview website.
"""

import media
import fresh_tomatoes

# create movie objects with content and links for the movie page
red_october = media.Movie("The Hunt for Red October", "March 2, 1990",
                          "In 1984, the USSR's best submarine captain in their newest sub violates orders and heads for the USA. Is he trying to defect, or to start a war?",
                          "http://ia.media-imdb.com/images/M/MV5BNzk3OTE2NjQ0OV5BMl5BanBnXkFtZTgwMDg3ODYxMTE@._V1_SX214_AL_.jpg",
                          "https://www.youtube.com/watch?v=iGfk_IU3Wlo")

major_league = media.Movie("Major League", "April 7, 1989",
                           "The new owner of the Cleveland Indians puts together a purposely horrible team so they'll lose and she can move the team. But when the plot is uncovered, they start winning just to spite her.",
                           "http://ia.media-imdb.com/images/M/MV5BMTcyMDE5NzIxMV5BMl5BanBnXkFtZTcwNDUwNzE0MQ@@._V1_SY317_CR5,0,214,317_AL_.jpg",
                           "https://www.youtube.com/watch?v=K_ILz9bC-VU")

cars = media.Movie("CARS", "June 9, 2006",
                   "A hot-shot race-car named Lightning McQueen gets waylaid in Radiator Springs, where he finds the true meaning of friendship and family.",
                   "http://ia.media-imdb.com/images/M/MV5BMTg5NzY0MzA2MV5BMl5BanBnXkFtZTYwNDc3NTc2._V1_SX214_AL_.jpg",
                   "https://www.youtube.com/watch?v=WGByijP0Leo")

buckaroo_banzai = media.Movie("Buckaroo Banzai", "August 10, 1984",
                              "Adventurer/surgeon/rock musician Buckaroo Banzai and his band of men, the Hong Kong Cavaliers, take on evil alien invaders from the 8th dimension.",
                              "http://ia.media-imdb.com/images/M/MV5BMTk3OTAwNDQwOF5BMl5BanBnXkFtZTgwOTE0MzQxMDE@._V1_SY317_CR0,0,214,317_AL_.jpg",
                              "https://www.youtube.com/watch?v=ii9n8CMpLMk")

french_kiss = media.Movie("French Kiss", "May 5, 1995",
                          "A woman flies to France to confront her straying fiance, but gets into trouble when the charming crook seated next to her uses her for smuggling.",
                          "http://ia.media-imdb.com/images/M/MV5BMTkzMjg5MDQ3M15BMl5BanBnXkFtZTgwOTM5NTE0MDE@._V1_SX214_AL_.jpg",
                          "https://www.youtube.com/watch?v=TF9xsk3tmoA")

pacific_rim = media.Movie("Pacific Rim", "July 12, 2013",
                          "As a war between humankind and monstrous sea creatures wages on, a former pilot and a trainee are paired up to drive a seemingly obsolete special weapon in a desperate effort to save the world from the apocalypse.",
                          "http://ia.media-imdb.com/images/M/MV5BMTY3MTI5NjQ4Nl5BMl5BanBnXkFtZTcwOTU1OTU0OQ@@._V1_SY317_CR0,0,214,317_AL_.jpg",
                          "https://www.youtube.com/watch?v=rkOy1C8eX6o")

# fill an array with the movie objects
movies = [red_october, major_league, cars, buckaroo_banzai, french_kiss, pacific_rim]

# call the fress_tomatoes code to create and open the page
fresh_tomatoes.open_movies_page(movies)
