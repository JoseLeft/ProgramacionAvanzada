from pydantic import BaseModel

class MovieSchema(BaseModel):
    title: str
    duration: int
    release_year: int
    director: str
    classification: str
    genre: str