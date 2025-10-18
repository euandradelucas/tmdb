import httpx
from app.config import TMDB_API_KEY, TMDB_BASE_URL

# Função genérica para buscar dados no TMDB
async def get_tmdb_data(endpoint: str, params: dict = None):
    if params is None:
        params = {}

    # Sempre adiciona a chave da API
    params["api_key"] = TMDB_API_KEY

    async with httpx.AsyncClient() as client:
        response = await client.get(f"{TMDB_BASE_URL}{endpoint}", params=params)
        response.raise_for_status()  
        return response.json()