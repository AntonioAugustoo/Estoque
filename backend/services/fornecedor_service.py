from db.connection import get_connection


async def get_all_fornecedores():
    conn = await get_connection()
    try:
        rows = await conn.fetch("SELECT * FROM fornecedores")
        return [dict(row) for row in rows]
    finally:
        await conn.close()


async def get_fornecedor_by_id(id: int):
    conn = await get_connection()
    try:
        row = await conn.fetchrow("SELECT * FROM fornecedores WHERE id = $1", id)
        return dict(row) if row else None
    finally:
        await conn.close()


async def create_fornecedor(nome: str, contato: str | None, email: str | None):
    conn = await get_connection()
    try:
        row = await conn.fetchrow(
            "INSERT INTO fornecedores (nome, contato, email) VALUES ($1, $2, $3) RETURNING *",
            nome, contato, email
        )
        return dict(row)
    finally:
        await conn.close()


async def delete_fornecedor(id: int):
    conn = await get_connection()
    try:
        result = await conn.execute(
            "DELETE FROM fornecedores WHERE id = $1", id
        )
        return result == "DELETE 1"
    finally:
        await conn.close()