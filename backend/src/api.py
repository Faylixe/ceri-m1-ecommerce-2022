from typing import Union

from fastapi import FastAPI, status
from src.db.database import *

tags_metadata = [
    {
        "name": "Database",
        "description": "Operations with database"
    },
    {
        "name": "Album",
        "description": "Operations with albums.",
    },
    {
        "name": "Song",
        "description": "Operations with songs.",
    },
    {
        "name": "Artist",
        "description": "Operations with artists.",
    },
    {
        "name": "User",
        "description": "Operations with users"
    }
]

app = FastAPI(title="Jean Cloud Vinil backend", version=1.0, openapi_tags=tags_metadata)

@app.get("/", tags=["Database"], status_code=status.HTTP_200_OK)
def read_root():
    return {'message': 'Jean Cloud Vinyl back is running'}

@app.get('/create/database', tags=["Database"], status_code=status.HTTP_200_OK)
def create_database():
    '''Root to create database'''
    Database.create_all_tab()

@app.get('/drop/database', tags=["Database"], status_code=status.HTTP_200_OK)
def drop_database():
    '''Root to create database'''
    Database.remove_all_tab()

@app.post("/create/song", tags=["Song"], status_code=status.HTTP_201_CREATED)
def create_song(song: Song):
    '''Root to create a song'''
    Database.insert_song(song.name, song.id_artist, song.id_album)
    return({'message': song})

@app.get("/get/songs", tags=["Song"], status_code=status.HTTP_200_OK)
def read_songs():
    '''Root to get all songs'''
    songs = Database.get_all_songs()
    return({'message': songs})

@app.post("/create/album", tags=["Album"], status_code=status.HTTP_201_CREATED)
def create_album(album: Album):
    '''Root to create an album'''
    Database.insert_album(album.name, album.id_artist, album.image, album.release_date, album.type, album.price)
    return({'message': album})

@app.get("/get/albums", tags=["Album"], status_code=status.HTTP_200_OK)
def read_albums():
    '''Root to get albums'''
    albums = Database.get_all_albums()
    return({'message': albums})

@app.post("/create/artist", tags=["Artist"], status_code=status.HTTP_201_CREATED)
def create_artist(artist: Artist):
    '''Root to create an artist'''
    Database.insert_artist(artist.firstname, artist.secondname, artist.nationality)
    return({'message': artist})

@app.get("/get/artists", tags=["Artist"], status_code=status.HTTP_200_OK)
def read_artists():
    '''Root to get all artists'''
    artists = Database.get_all_artists()
    return({'message': artists})

@app.get("/get/albumsongs/{album_id}", tags=["Song"])
def read_songs_in_album(album_id: int):
    '''Root to get all songs from an album, use the id of the album (work in progress: need to make with the name)'''
    songs = Database.get_songs_from_album(album_id)
    return({'message': songs})