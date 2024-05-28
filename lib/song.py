class Song:
    count= 0
    genres = []
    artists = []
    genres_count = {}
    artists_count = {}

    def __init__(self, name, artist, genre):
        self.name = name
        self.artist = artist
        self.genre = genre
        self.add_song_to_count()
        Song.add_to_genres(genre)
        Song.add_to_artists(artist)
        Song.add_to_genre_count(genre)
        Song.add_to_artists_count(artist)

    @classmethod
    def add_song_to_count(cls, increment=1):
        cls.count += increment

    @classmethod
    def add_to_genres(cls, genre):
        if genre not in cls.genres:
            cls.genres.append(genre)

    @classmethod
    def add_to_artists(cls, artist):
        if artist not in cls.artists:
            cls.artists.append(artist)

    @classmethod
    def add_to_genre_count(cls, genre):
        if cls.genres_count.get(genre, 0) == 0:
            cls.genres_count[genre] = 1
        else:
            cls.genres_count[genre] += 1

    @classmethod
    def add_to_artists_count(cls, artist):
        if cls.artists_count.get(artist):
            cls.artists_count[artist] += 1
        else:
            cls.artists_count[artist] = 1
