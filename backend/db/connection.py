import asyncpg
import os

async def get_connection():
    return await asyncpg.connect(os.getenv("DATABASE_URL"))