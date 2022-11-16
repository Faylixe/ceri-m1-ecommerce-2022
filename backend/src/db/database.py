# from paths import MODELS_PATH
# from src.models import *
from src.models.all_class import *
# from src.models.artist import Artist, create_table_artist
# from src.models.song import Song, create_table_song

from typing import Optional
from sqlmodel import Field, SQLModel, create_engine, Session, select

sqlite_file_name = "database.db"
sqlite_url = f"sqlite:///{sqlite_file_name}"
engine = create_engine(sqlite_url, echo=True)
class Database:
    # sqlite_file_name = "db/database.db"
    # sqlite_url = f"sqlite:///{sqlite_file_name}"
    # database_engine = create_engine(sqlite_url, echo=True)
    # def __init__(self):

    def create_all_tab():
        create_table(engine)
        # create_table_album(engine)
        # create_table_song(engine)
        # create_table_artist(engine)

    def get_all_songs():
        with Session(engine) as session:
            statement = select(Song)
            results = session.exec(statement).all()
            for song in results:
                print(song)
            return(results)

    def get_all_albums():
        with Session(engine) as session:
            statement = select(Album)
            results = session.exec(statement).all()
            for album in results:
                print(album)
            return(results)

    def get_all_artists():
        with Session(engine) as session:
            statement = select(Artist)
            results = session.exec(statement).all()
            for artist in results:
                print(artist)
            return(results)

    def insert_song(new_name, new_id_artist, new_id_album):
        new_song = Song(id_album=new_id_album, id_artist=new_id_artist, name=new_name)
        session = Session(engine)
        session.add(new_song)
        session.commit()
        session.refresh(new_song)

    def insert_album(new_name, new_id_artist, new_image, new_release_date, new_type, new_price):
        new_album = Album(name=new_name, id_artist=new_id_artist, image=new_image, release_date=new_release_date, type=new_type, price=new_price)
        session = Session(engine)
        session.add(new_album)
        session.commit()
        session.refresh(new_album)

    def insert_artist(new_firstname, new_secondname, new_nationality):
        new_artist = Artist(firstname=new_firstname, secondname=new_secondname, nationality=new_nationality)
        session = Session(engine)
        session.add(new_artist)
        session.commit()
        session.refresh(new_artist)

    def get_songs_from_album(id_to_search):
        with Session(engine) as session:
            statement = select(Album).where(Album.id == id_to_search)
            result = session.exec(statement).one()
            print(result.songs)
            # for song in results.songs:
            #     print(song)
            return(result.songs)

# def main():
#     Database.create_all_tab()

# main()