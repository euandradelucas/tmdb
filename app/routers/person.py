from fastapi import APIRouter
from app.models.person import Person, PersonResponse, MovieCreditsResponse
from app.services.tmdb_service import get_tmdb_data

# Criação do router específico para o "Person"
router = APIRouter()

# 1 - Encontra pessoa por ID
@router.get("/{person_id}", response_model=Person)
async def get_person(person_id: int):
    return await get_tmdb_data(f"/person/{person_id}")

# 2 - Encontra pessoa por nome (search)
@router.get("/search/", response_model=PersonResponse)
async def search_person(query: str):
    return await get_tmdb_data("/search/person", {"query": query})

# 3 - Pessoas populares
@router.get("/trending", response_model=PersonResponse)
async def trending_persons(time_window: str = "week"):
    return await get_tmdb_data("/trending/person/{time_window}")

# 4 - Todos os filmes de uma pessoa (artista)
@router.get("/{person_id}/movies", response_model=MovieCreditsResponse)
async def person_movies(person_id: int):
    return await get_tmdb_data(f"/person/{person_id}/movie_credits")

# 5 - Person trending (day/week)
@router.get("/trending/{time_window}", response_model=PersonResponse)
async def trending_persons(time_window: str = "week"):
    return await get_tmdb_data(f"/trending/person/{time_window}")
