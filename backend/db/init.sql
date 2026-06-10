CREATE TABLE IF NOT EXISTS categorias (
    id SERIAL PRIMARY KEY,
    nome VARCHAR(100) NOT NULL
);

CREATE TABLE IF NOT EXISTS fornecedores (
    id SERIAL PRIMARY KEY,
    nome VARCHAR(100) NOT NULL,
    contato VARCHAR(100),
    email VARCHAR(150)
);

CREATE TABLE IF NOT EXISTS produtos (
    id SERIAL PRIMARY KEY,
    nome VARCHAR(150) NOT NULL,
    descricao TEXT,
    preco NUMERIC(10, 2) NOT NULL,
    quantidade INTEGER NOT NULL DEFAULT 0,
    categoria_id INTEGER REFERENCES categorias(id) ON DELETE SET NULL
);

CREATE TABLE IF NOT EXISTS produto_fornecedor (
    produto_id INTEGER REFERENCES produtos(id) ON DELETE CASCADE,
    fornecedor_id INTEGER REFERENCES fornecedores(id) ON DELETE CASCADE,
    PRIMARY KEY (produto_id, fornecedor_id)
);

