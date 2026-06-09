from fastapi import APIRouter, HTTPException
from schemas.categoria import Categoria, CategoriaCreate
from services.categoria_service import (
    get_all_categorias,
    get_categoria_by_id,
    create_categoria,
    delete_categoria
)

router = APIRouter(prefix="/categorias", tags=["Categorias"])


@router.get("/", response_model=list[Categoria])
async def listar_categorias():
    return await get_all_categorias()


@router.get("/{id}", response_model=Categoria)
async def buscar_categoria(id: int):
    categoria = await get_categoria_by_id(id)
    if not categoria:
        raise HTTPException(status_code=404, detail="Categoria não encontrada")
    return categoria


@router.post("/", response_model=Categoria, status_code=201)
async def criar_categoria(dados: CategoriaCreate):
    return await create_categoria(dados.nome)


@router.delete("/{id}", status_code=204)
async def deletar_categoria(id: int):
    deletado = await delete_categoria(id)
    if not deletado:
        raise HTTPException(status_code=404, detail="Categoria não encontrada")