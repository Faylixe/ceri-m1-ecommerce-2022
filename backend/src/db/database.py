# from paths import MODELS_PATH
# from src.models import *
from src.models.all_class import *
import hashlib
# from src.models.artist import Artist, create_table_artist
# from src.models.song import Song, create_table_song

from typing import Optional
from sqlmodel import create_engine, Session, select
from google.cloud.sql.connector import Connector, IPTypes
from decouple import config
import pymysql
import sqlalchemy
import os

def connect_with_connector() -> sqlalchemy.engine.base.Engine:
    # Note: Saving credentials in environment variables is convenient, but not
    # secure - consider a more secure solution such as
    # Cloud Secret Manager (https://cloud.google.com/secret-manager) to help
    # keep secrets safe.
    db_address = os.environ.get("DATABASE_ADDRESS")  # e.g. 'project:region:instance'

    db_user = os.environ.get("DATABASE_USER")   # config('DATABASE_USER')  # e.g. 'my-db-user'
    db_pass = os.environ.get("PASSWORD") # config('PASSWORD') # os.environ["PASSWORD"]  # e.g. 'my-db-password'
    db_name = os.environ.get("DATABASE_NAME") # config('DATABASE_NAME') # os.environ["DATABASE_NAME"]  # e.g. 'my-database'
    ip_type = IPTypes.PRIVATE if os.environ.get("PRIVATE_IP") else IPTypes.PUBLIC

    connector = Connector(ip_type)

    def getconn() -> pymysql.connections.Connection:
        conn: pymysql.connections.Connection = connector.connect(
            db_address,
            "pymysql",
            user=db_user,
            password=db_pass,
            db=db_name,
        )
        return conn

    pool = sqlalchemy.create_engine(
        "mysql+pymysql://",
        creator=getconn,
        # ...
    )
    return pool


sqlite_file_name = "database.db"
sqlite_url = f"sqlite:///{sqlite_file_name}"
engine = connect_with_connector()# create_engine(sqlite_url, echo=True)
class Database:
    # sqlite_file_name = "db/database.db"
    # sqlite_url = f"sqlite:///{sqlite_file_name}"
    # database_engine = create_engine(sqlite_url, echo=True)
    # def __init__(self):

    def create_all_tab():
        create_all_table(engine)
        # create_table_album(engine)
        # create_table_song(engine)
        # create_table_artist(engine)

    def remove_all_tab():
        remove_table(engine)

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
            print(result)
            # for song in results.songs:
            #     print(song)
            return(result)
    
    def insert_user(new_username, new_password, new_firstname):
        new_user = User(username=new_username, password= hashlib.sha256(new_password.encode('utf-8')).hexdigest(), firstname=new_firstname)
        session = Session(engine)
        session.add(new_user)
        session.commit()
        session.refresh(new_user)

    def connect_user(username, password):
        resp = {'message': str, 'status': int}
        with Session(engine) as session:
            statement = select(User).where(User.username == username)
            result = session.exec(statement)
            print(result)
            if(len(result.all()) == 0):
                resp['message'] = "Nom d'utilisateur inexistant"
                resp['status'] = 404
            else:
                statement = select(User).where(User.username == username, User.password == hashlib.sha256(password.encode('utf-8')).hexdigest())
                result = session.exec(statement)
                print(result)
                if(len(result.all()) == 0):
                    resp['message'] = "Mot de passe incorrect"
                    resp['status'] = 404
                else:
                    user = result.one()
                    resp['message'] = "Bienvenue " + user.firstname
                    resp['status'] = 200
        return resp

    def user_is_connected():
        with Session(engine) as session:
            statement = select(User).where(User.is_connected == 1)
            result = session.exec(statement).all()
            if(len(result) == 0):
                return False
            else:
                return True
# def main():
#     Database.create_all_tab()

# main()