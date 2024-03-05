class Song:

    count = 0
    genres= []
    artists = []
    genre_count ={}
    artist_count = {}
    
    def __init__(self, name, artist, genre):
        self.name = name
        self.artist = artist
        self.genre = genre
        Song.add_to_artists(artist)
        Song.add_to_genres(genre)
        Song.add_song_to_count()
        Song.add_to_genre_count(genre)
        Song.add_to_artist_count(artist)
        

    @classmethod
    def add_song_to_count(cls):
        cls.count+= 1

    @classmethod
    def add_to_genres(cls, genre):
        if genre not in Song.genres:
            cls.genres.append(genre)
        else:
            return None



    @classmethod
    def show_genres(cls):
        print ([genre for genre in cls.genres])

    @classmethod
    def add_to_artists(cls, artist):
        if artist not in Song.artists:
            cls.artists.append(artist)
        else:
            return None



    @classmethod
    def show_artists(cls):
        print ([artist for artist in cls.artists])

    @classmethod
    def add_to_genre_count(cls, genre):
        for genre_name in cls.genres:
            if genre_name == genre:
                if genre_name in cls.genre_count:
                    cls.genre_count[genre_name] += 1
                else:
                    cls.genre_count[genre_name] = 1

    @classmethod
    def add_to_artist_count(cls, artist):
        if cls.artist_count.get(artist):
            cls.artist_count[artist] += 1
        else:
            cls.artist_count[artist] = 1

    


love = Song("99 Problems", "Jay-Z", "Rap")
love = Song("99 Problems", "Jay-Z", "Rap")
love = Song("99 Problems", "Jay-Z", "Rap")
love = Song("99 Problems", "Jay-Z", "Rap")



Song.show_genres()

print(Song.count)
