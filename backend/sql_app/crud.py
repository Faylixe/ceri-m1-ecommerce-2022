from sqlalchemy.orm import Session

from . import models, schemas


def get_artists(db: Session):
    """
    Returns all artists in the database
    """
    return db.query(models.Artist).all()


def get_artist_by_id(db: Session, artist_id: int):
    """
    Returns an artist by id
    """
    return db.query(models.Artist).filter(models.Artist.id == artist_id).first()


def get_artist_by_name(db: Session, artist_name: str):
    """
    Returns an artist by name
    """
    return db.query(models.Artist).filter(models.Artist.name.like(artist_name)).first()


def get_albums(db: Session):
    """
    Returns all albums in the database
    """
    return db.query(models.Album).all()


def get_album_by_id(db: Session, album_id: int):
    """
    Returns an album by id
    """
    return db.query(models.Album).filter(models.Album.id == album_id).first()


def get_album_by_name(db: Session, album_name: str):
    """
    Returns an album by name
    """
    return db.query(models.Album).filter(models.Album.name.like(album_name)).first()


def get_album_by_artist_id(db: Session, artist_id: int):
    """
    Returns an album by artist id
    """
    return db.query(models.Album).filter(models.Album.artists_id == artist_id).first()


def get_songs(db: Session):
    """
    Returns all songs in the database
    """
    return db.query(models.Song).all()


def get_song_by_id(db: Session, song_id: int):
    """
    Returns a song by id
    """
    return db.query(models.Song).filter(models.Song.id == song_id).first()


def get_song_by_name(db: Session, song_name: str):
    """
    Returns a song by name
    """
    return db.query(models.Song).filter(models.Song.name.like(song_name)).first()


def get_song_by_album_id(db: Session, album_id: int):
    """
    Returns a song by album id
    """
    return db.query(models.Song).filter(models.Song.albums_id == album_id).first()

