from fastapi import FastAPI
from app.routers import person #importa os routers criados

# Criação da aplicação principal
app = FastAPI(
    title="TMDB_API"
)

# Inclusão dos routers 
app.include_router(person.router, prefix="/person", tags=["Person"])

