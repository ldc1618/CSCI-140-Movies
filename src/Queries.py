"""
Contains functions for all query operations that could be performed on the dictionaries of movies and ratings. It
takes the queries as input until none is given and stops.

Author: Luke Chelius
"""
import operator
import sys
from timeit import default_timer as timer


def lookup(tconst: str, movies: dict, ratings: dict) -> None:
    """
    Takes a tconst value and searches the movies and ratings dictionaries for that specific tconst. It prints info
    on the movie and its rating if it is found and says it wasn't found otherwise.
    :param tconst: The 'serial number' of a certain movie/show on IMDB
    :param movies: The dictionary with the tconst values as the key for each Movie object
    :param ratings: A dictionary with the tconst values as the key for each Rating object
    :return: None
    """
    print("\nprocessing: LOOKUP", tconst)
    start = timer()  # Starts timing

    # If both the movie and rating are found prints the info
    if tconst in movies and tconst in ratings:
        print("\tMOVIE: Identifier:", tconst + ", Title:", movies[tconst].primary_title + ", Type:",
              movies[tconst].title_type + ", Year:", str(movies[tconst].start_year) + ", Runtime:",
              str(movies[tconst].run_time_mins) + ", Genres:", ", ".join(movies[tconst].genres.split(",")))
        print("\tRATING: Identifier:", tconst + ", Rating:", str(ratings[tconst].average_rating) + ", Votes:",
              str(ratings[tconst].num_votes))

    # Prints if the movie or rating isn't found
    else:
        print("\tMovie not found!")
        print("\tRating not found!")

    elapsed = timer() - start  # Finds elapsed time from when the start variable was made until now
    print("elapsed time (s):", elapsed)


def contains(movie_type: str, words: str, movies: dict) -> None:
    """
    Takes a type of movie and a series of words or characters and finds any titles in the dataset of movies that
    are of that type and contain those words or series of characters in the primary title.
    :param movie_type: The type of the movie i.e. short, movie, tvEpisode, videoGame, etc.
    :param words: The series of words or characters that is to be looked for in the primary title of movies of the
                    specified type
    :param movies: The dictionary containing all the titles from the movie dataset
    :return: None
    """
    print("\nprocessing: CONTAINS", movie_type, words)
    start = timer()  # Starts timing
    results = []  # Empty list to store Movie objects (could be multiple found)

    # Iterates through all keys in the dictionary
    for movie in movies:
        # If the title_type equals the specified one and the sequence of words appears in the title it appends it
        if movies[movie].title_type == movie_type and words in movies[movie].primary_title:
            results.append(movies[movie])

    # Prints info on each movie by iterating through the list of Movie objects
    if len(results) > 0:
        for item in results:
            print("\tIdentifier:", item.movie_id + ", Title:", item.primary_title + ", Type:", item.title_type +
                  ", Year:", str(item.start_year) + ", Runtime:", str(item.run_time_mins) + ", Genres:",
                  ", ".join(item.genres.split(",")))

    # Prints if there were no Movie objects found
    else:
        print("\tNo match found!")

    elapsed = timer() - start  # Finds elapsed time from when the start variable was made until now
    print("elapsed time (s):", elapsed)


def year_and_genre(movie_type: str, year: int, genre: str, movies: dict) -> None:
    """
    Takes a type of movie, the release year, and a genre and searches through the dictionary of Movie objects to
    find every movie in it that has the same type, release year, and genre.
    :param movie_type: The type of the movie i.e. short, movie, tvEpisode, videoGame, etc.
    :param year: The start year of the movies being searched for
    :param genre: The genre of the movies being searched for
    :param movies: The dictionary containing all the titles from the movie dataset
    :return: None
    """
    print("\nprocessing: YEAR_AND_GENRE", movie_type, year, genre)
    start = timer()  # Starts timing
    results = []  # Empty list to store Movie objects (could be multiple found)

    # Iterates through all keys in the dictionary
    for movie in movies:
        # If the movie's type, release year, and genre match it adds the Movie to results
        if movies[movie].title_type == movie_type and movies[movie].start_year == year and \
                genre in movies[movie].genres:
            results.append(movies[movie])

    # Prints the info for each Movie in results
    if len(results) > 0:
        results.sort(key=operator.attrgetter("primary_title"))  # Sorts the Movies alphabetically by title
        for item in results:
            print("\tIdentifier:", item.movie_id + ", Title:", item.primary_title + ", Type:", item.title_type +
                  ", Year:", str(item.start_year) + ", Runtime:", str(item.run_time_mins) +
                  ", Genres:", ", ".join(item.genres.split(",")))

    # Prints if no movies were found
    else:
        print("\tNo match found!")

    elapsed = timer() - start  # Finds elapsed time from when the start variable was made until now
    print("elapsed time (s):", elapsed)


def runtime(movie_type: str, min_mins: int, max_mins: int, movies: dict) -> None:
    """
    Finds all movies of a certain type between a minimum and maximum runtime (inclusive), and prints info on the
    found movies.
    :param movie_type: The type of the movie i.e. short, movie, tvEpisode, videoGame, etc.
    :param min_mins: The minimum runtime for the movie
    :param max_mins: The maximum runtime for the movie
    :param movies: The dictionary containing all the titles from the movie dataset
    :return: None
    """
    print("\nprocessing: RUNTIME", movie_type, min_mins, max_mins)
    start = timer()  # Starts timing
    results = []  # Blank list to store results

    # Iterates through each key in the dictionary
    for movie in movies:
        # If the movie is the right type and within the min and max runtimes (inclusive) it's appended to results
        if movies[movie].title_type == movie_type and min_mins <= movies[movie].run_time_mins <= max_mins:
            results.append(movies[movie])

    # Prints info on the movies in the results list
    if len(results) > 0:
        results.sort(key=operator.attrgetter("primary_title"))  # Sorts movies alphabetically by title
        results.sort(key=operator.attrgetter("run_time_mins"), reverse=True)  # Sorts movies short to long by runtime
        for item in results:
            print("\tIdentifier:", item.movie_id + ", Title:", item.primary_title + ", Type:", item.title_type +
                  ", Year:", str(item.start_year) + ", Runtime:", str(item.run_time_mins) +
                  ", Genres:", ", ".join(item.genres.split(",")))

    # Prints if no movies were found with the given parameters
    else:
        print("\tNo match found!")

    elapsed = timer() - start  # Finds elapsed time from when the start variable was made until now
    print("elapsed time (s):", elapsed)


def most_votes(movie_type: str, num: int, movies: dict, ratings: dict) -> None:
    """
    Finds a certain number of movies of a certain type with the most votes out of all the movies of that type.
    :param movie_type: The type of the movie i.e. short, movie, tvEpisode, videoGame, etc.
    :param num: The number of movies with the most votes to find
    :param movies: The dictionary containing all the titles from the movie dataset
    :param ratings: The dictionary containing all the ratings from the rating dataset
    :return: None
    """
    print("\nprocessing: MOST_VOTES", movie_type, num)
    start = timer()  # Starts timing
    results = []  # A blank list to store the results

    # Iterates through each key in the dictionary
    for movie in movies:
        # If the movie is the correct type and has a rating, it will compare its votes
        if movies[movie].title_type == movie_type and movie in ratings:
            # If there are less that the specified number of movies in the list it automatically is added
            if len(results) < num:
                results.append(ratings[movie])
                results.sort(key=lambda rating: movies[rating.movie_id].primary_title)  # Sorts by title
                results.sort(key=operator.attrgetter("num_votes"), reverse=True)  # Sorts the list by most votes
            # If the movie has more votes than the movie with the least number of votes in the list it replaces it
            elif ratings[movie].num_votes > results[-1].num_votes:
                results[-1] = ratings[movie]
                results.sort(key=lambda rating: movies[rating.movie_id].primary_title)  # Sorts by title
                results.sort(key=operator.attrgetter("num_votes"), reverse=True)  # Sorts the list by most votes

    # If movies were found it prints info on each one
    if len(results) > 0:
        # Prints the movies in order of most votes to least votes in the results
        for i, item in enumerate(results):
            print("\t" + str(i + 1) + ". VOTES:", str(item.num_votes) + ", MOVIE: Identifier:",
                  item.movie_id + ", Title:", movies[item.movie_id].primary_title + ", Type:",
                  movies[item.movie_id].title_type + ", Year:", str(movies[item.movie_id].start_year) + ", Runtime:",
                  str(movies[item.movie_id].run_time_mins) + ", Genres:",
                  ", ".join(movies[item.movie_id].genres.split(",")))

    # Prints if no movies were found with the given parameters
    else:
        print("\tNo match found!")

    elapsed = timer() - start  # Finds elapsed time from when the start variable was made until now
    print("elapsed time (s):", elapsed)


def top(movie_type: str, num: int, begin_year: int, stop_year: int, movies: dict, ratings: dict) -> None:
    """
    Searches movies of a type that fall between a start and end year (inclusive) and finds the a certain number of
    the top rated movies from every year between the start and end years (inclusive). It prints them out in order
    of decreasing rating, if the same then decreasing number of votes, and if that is tied then alphabetically
    by title.
    :param movie_type: The type of the movie i.e. short, movie, tvEpisode, videoGame, etc.
    :param num: The number of movies with the most votes to find
    :param begin_year: The year to begin finding movies at (inclusive)
    :param stop_year: The year to stop finding movies at (inclusive)
    :param movies:The dictionary containing all the titles from the movie dataset
    :param ratings: The dictionary containing all the ratings from the rating dataset
    :return: None
    """
    print("\nprocessing: TOP", movie_type, num, begin_year, stop_year)
    start = timer()  # Starts timing
    results = []  # A blank list to store the results
    # Makes results into a 2D list with one list inside results for each year movies are being searched for
    for k in range(stop_year - begin_year + 1):
        results.append([])

    # Iterates through each key in the dictionary
    for movie in movies:
        # If the type matches, the movie has a rating, its votes are >= 1000 and it falls between the years (inclusive)
        # then it will compare its rating
        if movies[movie].title_type == movie_type and movie in ratings and ratings[movie].num_votes >= 1000 and \
                begin_year <= movies[movie].start_year <= stop_year:
            year = stop_year - movies[movie].start_year  # Finds the index in result for the correct list for the year
            # If there are less than the specified number of movies needed its automatically appended
            if len(results[year]) < num:
                results[year].append(ratings[movie])
                results[year].sort(key=lambda rating: movies[rating.movie_id].primary_title)  # Sorts by title
                results[year].sort(key=operator.attrgetter("num_votes"), reverse=True)  # Sorts the list by most votes
                results[year].sort(key=operator.attrgetter("average_rating"), reverse=True)  # Sorts the list by rating
            # If the movie has a higher rating than the lowest in the list it replaces the lowest
            # if they are tied for rating, if it has more votes it replaces the lowest
            elif ratings[movie].average_rating > results[year][-1].average_rating or (ratings[movie].average_rating ==
                                                                                      results[year][-1].average_rating
                                                                                      and ratings[movie].num_votes >
                                                                                      results[year][-1].num_votes):
                results[year][-1] = ratings[movie]
                results[year].sort(key=lambda rating: movies[rating.movie_id].primary_title)  # Sorts by title
                results[year].sort(key=operator.attrgetter("num_votes"), reverse=True)  # Sorts the list by most votes
                results[year].sort(key=operator.attrgetter("average_rating"), reverse=True)  # Sorts the list by rating

    results.reverse()  # Reverses results because they are in descending year order to begin
    # Iterates through the lists for each year
    for i, result in enumerate(results):
        # If the list has movies in it it prints them
        if len(result) > 0:
            print("\tYEAR:", begin_year + i)  # Prints the year the movies are from
            # Prints each movie in the list ranked in the specified order
            for j, item in enumerate(result):
                print("\t\t" + str(j + 1) + ". RATING:", str(item.average_rating) + ", VOTES:", str(item.num_votes) +
                      ", MOVIE: Identifier:", item.movie_id + ", Title:", movies[item.movie_id].primary_title +
                      ", Type:", movies[item.movie_id].title_type + ", Year:", str(movies[item.movie_id].start_year) +
                      ", Runtime:", str(movies[item.movie_id].run_time_mins) + ", Genres:",
                      ", ".join(movies[item.movie_id].genres.split(",")))

        # Prints if no movies from the given year were found
        else:
            print("\tYEAR:", begin_year + i)
            print("\t\tNo match found!")

    elapsed = timer() - start  # Finds elapsed time from when the start variable was made until now
    print("elapsed time (s):", elapsed)


def get_queries(movies: dict, ratings: dict) -> None:
    for query in sys.stdin:
        query = query.strip().split(" ")
        if query[0] == "LOOKUP":
            lookup(query[1], movies, ratings)
        elif query[0] == "CONTAINS":
            contains(query[1], " ".join(query[2:]), movies)
        elif query[0] == "YEAR_AND_GENRE":
            year_and_genre(query[1], int(query[2]), query[3], movies)
        elif query[0] == "RUNTIME":
            runtime(query[1], int(query[2]), int(query[3]), movies)
        elif query[0] == "MOST_VOTES":
            most_votes(query[1], int(query[2]), movies, ratings)
        elif query[0] == "TOP":
            top(query[1], int(query[2]), int(query[3]), int(query[4]), movies, ratings)
