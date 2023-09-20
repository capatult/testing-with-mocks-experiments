class MusicLibrary:
    # Public properties:
    #   tracks: a list of instances of Track

    def __init__(self):
        self.tracks = []

    def add(self, track):
        # track is an instance of Track
        # Track gets added to the library
        # Returns nothing
        if hasattr(track, "title") and hasattr(track, "artist"):
            if isinstance(track.title, str) and isinstance(track.artist, str):
                self.tracks.append(track)
                return
        raise Exception("Cannot add non-track object to library")

        

    def search(self, keyword):
        # keyword is a string
        # Returns a list of instances of track that match the keyword
        return [track for track in self.tracks if track.matches(keyword)]
 
