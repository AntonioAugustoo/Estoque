from fastapi import APIRouter, HTTPException
from schemas.produto import Produto, ProdutoCreate, ProdutoPatch
from schemas.fornecedor import Fornecedor
from services.produto_service import (
    get_all_produtos,
    get_produto_by_id,
    create_produto,
    update_produto,
    delete_produto,
    vincular_fornecedor,
    get_fornecedores_do_produto
)

router = APIRouter(prefix="/produtos", tags=["Produtos"])


@router.get("/", response_model=list[Produto])
async def listar_produtos():
    return await get_all_produtos()


@router.get("/{id}", response_model=Produto)
async def buscar_produto(id: int):
    produto = await get_produto_by_id(id)
    if not produto:
        raise HTTPException(status_code=404, detail="Produto não encontrado")
    return produto


@router.post("/", response_model=Produto, status_code=201)
async def criar_produto(dados: ProdutoCreate):
    return await create_produto(
        dados.nome,
        dados.descricao,
        dados.preco,
        dados.quantidade,
        dados.categoria_id
    )


@router.put("/{id}", response_model=Produto)
async def atualizar_produto(id: int, dados: ProdutoPatch):
    produto = await update_produto(id, dados.model_dump())
    if not produto:
        raise HTTPException(status_code=404, detail="Produto não encontrado")
    return produto


@router.delete("/{id}", status_code=204)
async def deletar_produto(id: int):
    deletado = await delete_produto(id)
    if not deletado:
        raise HTTPException(status_code=404, detail="Produto não encontrado")


@router.post("/{id}/fornecedores", status_code=201)
async def vincular_fornecedor_ao_produto(id: int, fornecedor_id: int):
    await vincular_fornecedor(id, fornecedor_id)
    return {"mensagem": "Fornecedor vinculado com sucesso"}


@router.get("/{id}/fornecedores", response_model=list[Fornecedor])
async def listar_fornecedores_do_produto(id: int):
    return await get_fornecedores_do_produto(id)