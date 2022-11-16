from typing import Union

from fastapi import FastAPI, status
from src.db.database import *
# from src.models import *
# from models.album import Album
# from models.artist import Artist
# from models.song import Song

app = FastAPI()

@app.get("/", status_code=status.HTTP_200_OK)
def read_root():
    return {'message': 'Jean Cloud Vinyl back is running'}

@app.get('/create/database')
def create_database():
    # database = Database()
    Database.create_all_tab()

@app.post("/create/song/")
def create_song(song: Song):
    database = Database()
    Database.insert_song(song.name, song.id_artist, song.id_album)
    return({'message': song})

@app.get("/get/songs/")
def read_songs():
    database = Database()
    songs = Database.get_all_songs()
    return({'message': songs})

@app.post("/create/album/")
def create_album(album: Album):
    database = Database()
    Database.insert_album(album.name, album.id_artist, album.image, album.release_date, album.type, album.price)
    return({'message': album})

@app.get("/get/albums/")
def read_albums():
    database = Database()
    albums = Database.get_all_albums()
    return({'message': albums})

@app.post("/create/artist/")
def create_artist(artist: Artist):
    database = Database()
    Database.insert_artist(artist.firstname, artist.secondname, artist.nationality)
    return({'message': artist})

@app.get("/get/artists/")
def read_artists():
    database = Database()
    artists = Database.get_all_artists()
    return({'message': artists})

@app.get("/get/album/songs/{album_id}")
def read_songs_in_album(album_id: int):
    songs = Database.get_songs_from_album(album_id)
    return({'message': songs})