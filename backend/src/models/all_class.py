from typing import Optional, List

from sqlmodel import Field, Relationship, SQLModel
from datetime import datetime

class Artist(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    firstname: str
    secondname: Optional[str] = None
    nationality: Optional[str] = None

class Album(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str
    id_artist: int = Field(nullable=False)
    image: Optional[str] = None
    release_date:Optional[datetime] = None
    type: str
    price: int
    
    songs: List["Song"]  = Relationship(back_populates="album")

class Song(SQLModel, table=True):
    id: Optional[int] = Field(nullable=False, primary_key=True)
    name: str
    id_album: int = Field(default=None, foreign_key="album.id")
    album: Optional[Album] = Relationship(back_populates="songs")
    id_artist: int = Field(default=None, foreign_key="artist.id")

class User(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    username: str
    password: str
    is_connected: Optional[int] = Field(default=0, nullable=False)
    image: Optional[str] = None
    firstname: str
    id_cart: int = Field(default=None, foreign_key="cart.id")

class Cart(SQLModel, table=True):
    id: Optional[int] = Field(nullable=False, primary_key=True)
    price: int
    

def remove_table(engine):
    SQLModel.metadata.drop_all(engine)

def create_all_table(engine):
    SQLModel.metadata.create_all(engine)