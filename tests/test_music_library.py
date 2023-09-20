from lib.music_library import *
from unittest.mock import Mock
import pytest

"""
Given no arguments, when music library is initialized it creates an attribute
Returns nothing
"""

def create_mock_track():
    track = Mock()
    track.title = ""
    track.artist = ""
    return track

def test_music_library_has_tracks_attribute():
    library = MusicLibrary()
    assert library.tracks == []

"""
Given track music library should add it to its library
It returns nothing
"""
def test_add_adds_track_to_library():
    track = create_mock_track()
    library = MusicLibrary()
    library.add(track)
    assert library.tracks[0] is track

def test_can_add_multiple_tracks_to_library():
    track1, track2 = create_mock_track(), create_mock_track()
    library = MusicLibrary()
    library.add(track1)
    library.add(track2)
    assert library.tracks == [track1, track2]
        
def test_cannot_add_non_track_objects_to_library():
    library = MusicLibrary()
    not_a_track = None
    with pytest.raises(Exception) as e:
        library.add(not_a_track)
    error_msg = str(e.value)
    assert error_msg == "Cannot add non-track object to library"

"""
Given any keyword to search an empty library 
It returns nothing
"""

def test_keyword_search_returns_emptylist_if_empty_library():
    library = MusicLibrary()
    keywords = ["", "hello", "world"]
    assert all(library.search(keyword) == [] for keyword in keywords)

"""
Given a keyword which matches a track in library  
It returns a list containing matching tracks
"""
def test_keyword_search_can_return_list_containing_track():
    library = MusicLibrary()
    track = create_mock_track()
    track.matches.return_value = True
    library.add(track)
    keyword = ""
    results = library.search(keyword)
    assert results == [track]

"""
Given a keyword which matches some of the tracks in the library
It returns a list only tracks containing keyword
"""
def test_keyword_search_only_returns_matching_tracks():
    library = MusicLibrary()
    tracks = [create_mock_track() for i in range(3)]
    matching = [True, False, True]
    for track, should_match in zip(tracks, matching):
        track.matches.return_value = should_match
        library.add(track)
    keyword = ""
    results = library.search(keyword)
    assert results == [tracks[0], tracks[2]]
    
    
    
    
