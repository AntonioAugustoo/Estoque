from pydantic import BaseModel

class FornecedorCreate(BaseModel):
    nome: str
    contato: str | None = None
    email: str | None = None

class Fornecedor(BaseModel):
    id: int
    nome: str
    contato: str | None = None
    email: str | None = None