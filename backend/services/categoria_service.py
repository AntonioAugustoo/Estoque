from db.connection import get_connection


async def get_all_categorias():
    conn = await get_connection()
    try:
        rows = await conn.fetch("SELECT * FROM categorias")
        return [dict(row) for row in rows]
    finally:
        await conn.close()


async def get_categoria_by_id(id: int):
    conn = await get_connection()
    try:
        row = await conn.fetchrow("SELECT * FROM categorias WHERE id = $1", id)
        return dict(row) if row else None
    finally:
        await conn.close()


async def create_categoria(nome: str):
    conn = await get_connection()
    try:
        row = await conn.fetchrow(
            "INSERT INTO categorias (nome) VALUES ($1) RETURNING *", nome
        )
        return dict(row)
    finally:
        await conn.close()


async def delete_categoria(id: int):
    conn = await get_connection()
    try:
        result = await conn.execute(
            "DELETE FROM categorias WHERE id = $1", id
        )
        return result == "DELETE 1"
    finally:
        await conn.close()