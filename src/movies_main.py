"""
Project 1: Movies

This takes input as to whether the big or small dataset should be used, converts the data in the dataset into
dictionaries for the movies and ratings. It then reads a file containing different queries that specify particular
types or categories of movies to find and finds them based on the input for each query.

Author: Luke Chelius
"""
import read_files  # read_f
import sys  # argv
import Queries  # get_queries


def main(args=sys.argv):
    # Determines whether to use the big or small datasets
    if len(args) > 1:
        files = ("data/small.basics.tsv", "data/small.ratings.tsv")
    else:
        files = ("data/title.basics.tsv", "data/title.ratings.tsv")

    movies = read_files.read_f(files[0], True)  # Reads the data from the movie file to a dict
    print()
    ratings = read_files.read_f(files[1], False, movies)  # Reads the data from the ratings file to a dict
    print("\nTotal movies:", len(movies))
    print("Total ratings:", len(ratings))

    Queries.get_queries(movies, ratings)  # Reads the queries from a file and performs them


if __name__ == '__main__':
    main()
