import pytest
from lib.track import *

"""
Given a title and artist strings
It creates a `Track` object with those attributes and returns nothing
"""
def test_title_and_artist_attributes_exist():
    track = Track(title="", artist="")
    assert hasattr(track, "title") and hasattr(track, "artist")

"""
Given a title and artist strings
It creates a `Track` object with the correct values and returns nothing
"""
def test_title_and_artist_attributes_set_correctly():
    desired_title = "Hello"
    desired_artist = "World"
    track = Track(desired_title, desired_artist)
    assert track.title == desired_title and track.artist == desired_artist

"""
Given a keyword to search which matches the title
It returns True
"""
def test_return_true_if_keyword_matches_title():
    track = Track("Foo", "Bar")
    result = track.matches("Foo")
    assert result == True

"""
Given a keyword to search which matches neither title nor artist
It returns False
"""
def test_return_false_if_keyword_matches_neither_title_nor_artist():
    track = Track("Foo", "Bar")
    result = track.matches("Baz")
    assert result == False

"""
Given keyword to search which matches the artist
It returns True
"""
def test_return_true_if_keyword_matches_artist():
    track = Track("Foo", "Bar")
    result = track.matches("Bar")
    assert result == True