from typing import Optional

from sqlmodel import Field, SQLModel, create_engine


class Artist(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    firstname: str
    secondname: Optional[str] = None
    nationality: Optional[str] = None

# def create_table_artist():
#     sqlite_file_name = "database.db"

#     engine = create_engine(sqlite_file_name, echo=True)

#     SQLModel.metadata.create_all(engine)