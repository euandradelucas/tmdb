from pydantic import BaseModel
from typing import Optional, List, Any

# Modelo de uma pessoa individual
class Person(BaseModel):
    id: int
    name: str
    original_name: Optional[str] = None
    profile_path: Optional[str] = None
    popularity: Optional[float] = None
    known_for_department: Optional[str] = None
    known_for: Optional[List[Any]] = None
    adult: Optional[bool] = None
    gender: Optional[int] = None
    biography: Optional[str] = None
    birthday: Optional[str] = None
    place_of_birth: Optional[str] = None

# Modelo de resposta de busca/listagem de pessoas
class PersonResponse(BaseModel):
    page: int
    results: List[Person]
    total_pages: int
    total_results: int

# Modelo de créditos de filmes de uma pessoa
class MovieCredit(BaseModel):
    id: int
    title: Optional[str] = None
    original_title: Optional[str] = None
    release_date: Optional[str] = None
    character: Optional[str] = None   # só aparece em cast
    job: Optional[str] = None         # só aparece em crew
    department: Optional[str] = None  # só aparece em crew
    credit_id: Optional[str] = None
    order: Optional[int] = None
    popularity: Optional[float] = None
    poster_path: Optional[str] = None
    backdrop_path: Optional[str] = None
    overview: Optional[str] = None
    vote_average: Optional[float] = None
    vote_count: Optional[int] = None
    adult: Optional[bool] = None
    video: Optional[bool] = None
    genre_ids: Optional[List[int]] = None
    original_language: Optional[str] = None
    media_type: Optional[str] = None

class MovieCreditsResponse(BaseModel):
    cast: List[MovieCredit]
    crew: List[MovieCredit]

