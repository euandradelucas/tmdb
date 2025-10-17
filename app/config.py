import os
from dotenv import load_dotenv

# Carrega as variáveis do .env

load_dotenv()

# Chave da API do TMDB

TMDB_API_KEY =  os.getenv("TMDB_API_KEY")

# URL da API do TMDB

TMDB_BASE_URL = "https://api.themoviedb.org/3"
