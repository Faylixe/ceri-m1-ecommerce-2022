from typing import Optional
from datetime import datetime
from sqlmodel import Field, SQLModel, create_engine


class Album(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str
    id_artist: int = Field(nullable=False, primary_key=True)
    image: Optional[str] = None
    release_date:Optional[datetime] = None


# def create_table_album():
#     sqlite_file_name = "database.db"

#     engine = create_engine(sqlite_file_name, echo=True)

#     SQLModel.metadata.create_all(engine)