from pydantic import BaseModel

class CategoriaCreate(BaseModel):
    nome: str

class Categoria(BaseModel):
    id: int
    nome: str