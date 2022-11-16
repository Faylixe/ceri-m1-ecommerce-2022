from typing import Optional, List

from sqlmodel import Field, Relationship, SQLModel
from datetime import datetime

# sqlite_file_name = "database.db"
# sqlite_url = f"sqlite:///{sqlite_file_name}"

# engine = create_engine(sqlite_url, echo=True)

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

def create_table(engine):
    SQLModel.metadata.create_all(engine)