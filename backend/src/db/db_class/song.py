from typing import Optional

from sqlmodel import Field, SQLModel, create_engine


class Song(SQLModel, table=True):
    id: Optional[int] = Field(nullable=False, primary_key=True)
    name: str
    id_album: int = Field(nullable=False)
    id_artist: int = Field(nullable=False)

# def create_table_song():
#     sqlite_file_name = "database.db"

#     engine = create_engine(sqlite_file_name, echo=True)

#     SQLModel.metadata.create_all(engine)