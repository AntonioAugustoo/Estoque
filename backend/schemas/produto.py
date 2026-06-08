from pydantic import BaseModel

class ProdutoCreate(BaseModel):
    nome: str
    descricao: str | None = None
    preco: float
    quantidade: int = 0
    categoria_id: int | None = None

class ProdutoPatch(BaseModel):
    nome: str | None = None
    descricao: str | None = None
    preco: float | None = None
    quantidade: int | None = None
    categoria_id: int | None = None

class Produto(BaseModel):
    id: int
    nome: str
    descricao: str | None = None
    preco: float
    quantidade: int
    categoria_id: int | None = None