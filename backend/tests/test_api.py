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
async def test_criar_e_listar_categoria(client):
    await client.post("/categorias/", json={"nome": "Cat Teste"})
    response = await client.get("/categorias/")
    assert response.status_code == 200
    nomes = [c["nome"] for c in response.json()]
    assert "Cat Teste" in nomes


@pytest.mark.anyio
async def test_criar_categoria(client):
    response = await client.post("/categorias/", json={"nome": "Nova Categoria"})
    assert response.status_code == 201
    assert response.json()["nome"] == "Nova Categoria"


@pytest.mark.anyio
async def test_criar_e_listar_produto(client):
    cat = await client.post("/categorias/", json={"nome": "Cat Produto"})
    cat_id = cat.json()["id"]
    await client.post("/produtos/", json={
        "nome": "Produto Lista",
        "preco": 10.00,
        "quantidade": 1,
        "categoria_id": cat_id
    })
    response = await client.get("/produtos/")
    assert response.status_code == 200
    nomes = [p["nome"] for p in response.json()]
    assert "Produto Lista" in nomes


@pytest.mark.anyio
async def test_criar_produto(client):
    cat = await client.post("/categorias/", json={"nome": "Cat Criar"})
    cat_id = cat.json()["id"]
    response = await client.post("/produtos/", json={
        "nome": "Produto Teste",
        "descricao": "Descrição teste",
        "preco": 99.90,
        "quantidade": 5,
        "categoria_id": cat_id
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
async def test_criar_e_listar_fornecedor(client):
    await client.post("/fornecedores/", json={"nome": "Forn Teste"})
    response = await client.get("/fornecedores/")
    assert response.status_code == 200
    nomes = [f["nome"] for f in response.json()]
    assert "Forn Teste" in nomes


@pytest.mark.anyio
async def test_criar_fornecedor(client):
    response = await client.post("/fornecedores/", json={
        "nome": "Fornecedor Teste",
        "contato": "(35) 99999-0000",
        "email": "teste@fornecedor.com"
    })
    assert response.status_code == 201
    assert response.json()["nome"] == "Fornecedor Teste"


@pytest.mark.anyio
async def test_atualizar_produto(client):
    cat = await client.post("/categorias/", json={"nome": "Cat Update"})
    cat_id = cat.json()["id"]
    criar = await client.post("/produtos/", json={
        "nome": "Produto Atualizar",
        "preco": 50.00,
        "quantidade": 3,
        "categoria_id": cat_id
    })
    id = criar.json()["id"]
    response = await client.put(f"/produtos/{id}", json={"preco": 75.00})
    assert response.status_code == 200
    assert response.json()["preco"] == 75.00