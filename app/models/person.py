from pydantic import BaseModel
from typing import Optional, List

# Modelo de uma pessoa individual
class Person(BaseModel):
    id: int
    name: str
    biography: Optional[str]
    birthday: Optional[str]
    place_of_birth: Optional[str]
    profile_path: Optional[str]

# Modelo de resposta de busca/listagem de pessoas
class PersonResponse(BaseModel):
    page: int
    results: List[Person]
    total_pages: int
    total_results: int

# Modelo de créditos de filmes de uma pessoa
class MovieCredit(BaseModel):
    id: int
    title: str
    character: Optional[str]
    job: Optional[str]
    release_date: Optional[str]

class MovieCreditsResponse(BaseModel):
    cast: List[MovieCredit]
    crew: List[MovieCredit]