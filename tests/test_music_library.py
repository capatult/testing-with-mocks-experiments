from lib.music_library import *
from lib.track import *
from unittest.mock import Mock

"""
Given no arguments, when music library is initialized it creates an attribute
Returns nothing
"""
def test_music_library_has_tracks_attribute():
    library = MusicLibrary()
    assert library.tracks == []

"""
Given track music library should add it to its library
It returns nothing
"""
def test_add_adds_track_to_library():
    track = Mock()
    library = MusicLibrary()
    library.add(track)
    assert library.tracks[0] is track

def test_can_add_multiple_tracks_to_library():
    track1, track2 = Mock(), Mock()
    library = MusicLibrary()
    library.add(track1)
    library.add(track2)
    assert library.tracks == [track1, track2]
        
def test_cannot_add_non_track_objects_to_library():
    pass
    
    
