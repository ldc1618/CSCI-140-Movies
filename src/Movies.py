"""
This is the Movie dataclass that allows the user to create Movie objects that hold all the attributes that a movie
can have.

Author: Luke Chelius
"""
from dataclasses import dataclass


@dataclass(frozen=True)
class Movie:
    """
    Dataclass to represent a movie.
    """
    movie_id: str
    title_type: str
    primary_title: str
    original_title: str
    start_year: int
    end_year: int
    run_time_mins: int
    genres: str
