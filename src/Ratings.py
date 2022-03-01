"""
This is the Rating dataclass, it allows the user to create Rating objects that store all the attributes that a rating
can have.

Author: Luke Chelius
"""
from dataclasses import dataclass


@dataclass(frozen=True)
class Rating:
    """
    Dataclass to represent a rating for a movie object.
    """
    movie_id: str
    average_rating: float
    num_votes: int
