from song import song

#still need to implement doubley-linked circle list aspect (maybe remove list base structure)

class playlist:
    def __init__(self,title): #add cover image to playlist??
        self.your_playlist=[]
        self.title=title

    def delete(self,song_title,artist_name):
        for song in self.your_playlist:
            if song.title==song_title and song.artist==artist_name:
                self.your_playlist.remove(song)

    def add(self,song_title,artist_name):
        new_song = song(song_title,artist_name,song_title+".jpg")
        self.your_playlist.append(new_song)

    def print(self):
        print("Playlist: "+self.title)
        for song in self.your_playlist:
            print(song.title+", "+song.artist)
