from fastapi import APIRouter, HTTPException
from schemas.fornecedor import Fornecedor, FornecedorCreate
from services.fornecedor_service import (
    get_all_fornecedores,
    get_fornecedor_by_id,
    create_fornecedor,
    delete_fornecedor
)

router = APIRouter(prefix="/fornecedores", tags=["Fornecedores"])


@router.get("/", response_model=list[Fornecedor])
async def listar_fornecedores():
    return await get_all_fornecedores()


@router.get("/{id}", response_model=Fornecedor)
async def buscar_fornecedor(id: int):
    fornecedor = await get_fornecedor_by_id(id)
    if not fornecedor:
        raise HTTPException(status_code=404, detail="Fornecedor não encontrado")
    return fornecedor


@router.post("/", response_model=Fornecedor, status_code=201)
async def criar_fornecedor(dados: FornecedorCreate):
    return await create_fornecedor(dados.nome, dados.contato, dados.email)


@router.delete("/{id}", status_code=204)
async def deletar_fornecedor(id: int):
    deletado = await delete_fornecedor(id)
    if not deletado:
        raise HTTPException(status_code=404, detail="Fornecedor não encontrado")