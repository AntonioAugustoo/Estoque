from db.connection import get_connection


async def get_all_produtos():
    conn = await get_connection()
    try:
        rows = await conn.fetch("""
            SELECT p.*, c.nome AS categoria_nome
            FROM produtos p
            LEFT JOIN categorias c ON p.categoria_id = c.id
        """)
        return [dict(row) for row in rows]
    finally:
        await conn.close()


async def get_produto_by_id(id: int):
    conn = await get_connection()
    try:
        row = await conn.fetchrow("""
            SELECT p.*, c.nome AS categoria_nome
            FROM produtos p
            LEFT JOIN categorias c ON p.categoria_id = c.id
            WHERE p.id = $1
        """, id)
        return dict(row) if row else None
    finally:
        await conn.close()


async def create_produto(nome: str, descricao: str | None, preco: float, quantidade: int, categoria_id: int | None):
    conn = await get_connection()
    try:
        row = await conn.fetchrow("""
            INSERT INTO produtos (nome, descricao, preco, quantidade, categoria_id)
            VALUES ($1, $2, $3, $4, $5)
            RETURNING *
        """, nome, descricao, preco, quantidade, categoria_id)
        return dict(row)
    finally:
        await conn.close()


async def update_produto(id: int, campos: dict):
    conn = await get_connection()
    try:
        campos_filtrados = {k: v for k, v in campos.items() if v is not None}

        if not campos_filtrados:
            return None

        set_clause = ", ".join(
            f"{campo} = ${i + 1}" for i, campo in enumerate(campos_filtrados)
        )
        valores = list(campos_filtrados.values())
        valores.append(id)

        row = await conn.fetchrow(
            f"UPDATE produtos SET {set_clause} WHERE id = ${len(valores)} RETURNING *",
            *valores
        )
        return dict(row) if row else None
    finally:
        await conn.close()


async def delete_produto(id: int):
    conn = await get_connection()
    try:
        result = await conn.execute(
            "DELETE FROM produtos WHERE id = $1", id
        )
        return result == "DELETE 1"
    finally:
        await conn.close()


async def vincular_fornecedor(produto_id: int, fornecedor_id: int):
    conn = await get_connection()
    try:
        await conn.execute("""
            INSERT INTO produto_fornecedor (produto_id, fornecedor_id)
            VALUES ($1, $2)
            ON CONFLICT DO NOTHING
        """, produto_id, fornecedor_id)
        return True
    finally:
        await conn.close()


async def get_fornecedores_do_produto(produto_id: int):
    conn = await get_connection()
    try:
        rows = await conn.fetch("""
            SELECT f.*
            FROM fornecedores f
            JOIN produto_fornecedor pf ON f.id = pf.fornecedor_id
            WHERE pf.produto_id = $1
        """, produto_id)
        return [dict(row) for row in rows]
    finally:
        await conn.close()