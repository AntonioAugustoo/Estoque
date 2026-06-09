from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from contextlib import asynccontextmanager
from db.connection import get_connection
from routes.categorias import router as categorias_router
from routes.fornecedores import router as fornecedores_router
from routes.produtos import router as produtos_router


@asynccontextmanager
async def lifespan(app: FastAPI):
    conn = await get_connection()
    await conn.close()
    yield


app = FastAPI(
    title="Sistema de Controle de Estoque",
    description="API para gerenciamento de produtos, categorias e fornecedores",
    version="1.0.0",
    lifespan=lifespan
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(categorias_router)
app.include_router(fornecedores_router)
app.include_router(produtos_router)


@app.get("/")
async def healthcheck():
    return {"ok": True, "mensagem": "API de estoque no ar"}