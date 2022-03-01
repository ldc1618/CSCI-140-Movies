"""
This reads from given files, it can be used for both the basics and the ratings files based on parameters
given in the read_f function. It also ignores any adult movies and ratings that have no movie to go along
with them.

Author: Luke Chelius
"""
from Movies import Movie
from Ratings import Rating
from timeit import default_timer as timer


def read_f(file: str, is_movies: bool, movies={}) -> dict:
    """
    Reads from a dataset file and puts the data into a dictionary where the tconst values are the key and either
    Movie or Rating objects are the values based on what dataset is being read.
    :param file: The name of the dataset file to be read
    :param is_movies: A boolean value, True if the dataset is to be made into Movie objects, False for Rating objects
    :param movies: The movies dictionary, necessary when reading the ratings dataset to ensure no ratings without
                    a corresponding movie are put in the dictionary
    :return: A dictionary relating the tconst as the keys to either Movie or Rating objects as the values
    """
    print("reading", file, "into dict...")
    start = timer()  # Starts timing
    imdb = {}  # Dictionary to store the Movie or Rating objects
    with open(file, encoding='utf-8') as imdb_f:
        imdb_f.readline()
        for line in imdb_f:
            line = line.strip()  # Gets rid of whitespace at the end of each line
            title = line.split("\t")  # Separates the line from the tsv file which are separated by tabs

            # Checks if the movie is an adult movie and skips it if it is
            if is_movies and int(title[4]) == 1:
                continue

            # Replaces the "\\N" values with 0 or None depending on which field it's in
            for i in range(len(title)):
                if title[i] == "\\N" and (i == 5 or i == 6 or i == 7):
                    title[i] = "0"
                elif title[i] == "\\N" and i == 8:
                    title[i] = "None"

            # If it's a movie it adds a Movie object with the info to the dictionary
            if is_movies:
                imdb[title[0]] = Movie(title[0], title[1], title[2], title[3], int(title[5]), int(title[6]),
                                       int(title[7]), title[8])

            # Otherwise it's a rating and it adds a Rating object with the info to the dictionary
            else:
                if title[0] in movies:
                    imdb[title[0]] = Rating(title[0], float(title[1]), int(title[2]))

    elapsed = timer() - start  # Finds the elapsed time
    print("elapsed time (s):", elapsed)
    return imdb
