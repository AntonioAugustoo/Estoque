import pytest
import httpx

BASE_URL = "http://api:8000"


@pytest.fixture
async def client():
    async with httpx.AsyncClient(base_url=BASE_URL, follow_redirects=True) as client:
        yield client


@pytest.mark.anyio
async def test_healthcheck(client):
    response = await client.get("/")
    assert response.status_code == 200
    assert response.json()["ok"] is True


@pytest.mark.anyio
async def test_listar_categorias(client):
    response = await client.get("/categorias")
    assert response.status_code == 200
    assert len(response.json()) > 0


@pytest.mark.anyio
async def test_criar_categoria(client):
    response = await client.post("/categorias", json={"nome": "Teste"})
    assert response.status_code == 201
    assert response.json()["nome"] == "Teste"


@pytest.mark.anyio
async def test_listar_produtos(client):
    response = await client.get("/produtos")
    assert response.status_code == 200
    assert len(response.json()) > 0


@pytest.mark.anyio
async def test_criar_produto(client):
    response = await client.post("/produtos", json={
        "nome": "Produto Teste",
        "descricao": "Descrição teste",
        "preco": 99.90,
        "quantidade": 5,
        "categoria_id": 1
    })
    assert response.status_code == 201
    assert response.json()["nome"] == "Produto Teste"


@pytest.mark.anyio
async def test_buscar_produto_inexistente(client):
    response = await client.get("/produtos/99999")
    assert response.status_code == 404


@pytest.mark.anyio
async def test_deletar_categoria_inexistente(client):
    response = await client.delete("/categorias/99999")
    assert response.status_code == 404


@pytest.mark.anyio
async def test_listar_fornecedores(client):
    response = await client.get("/fornecedores")
    assert response.status_code == 200
    assert len(response.json()) > 0


@pytest.mark.anyio
async def test_criar_fornecedor(client):
    response = await client.post("/fornecedores", json={
        "nome": "Fornecedor Teste",
        "contato": "(35) 99999-0000",
        "email": "teste@fornecedor.com"
    })
    assert response.status_code == 201
    assert response.json()["nome"] == "Fornecedor Teste"


@pytest.mark.anyio
async def test_atualizar_produto(client):
    criar = await client.post("/produtos", json={
        "nome": "Produto Atualizar",
        "preco": 50.00,
        "quantidade": 3,
        "categoria_id": 1
    })
    id = criar.json()["id"]

    response = await client.put(f"/produtos/{id}", json={"preco": 75.00})
    assert response.status_code == 200
    assert response.json()["preco"] == 75.00
