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

-- Dados iniciais para teste
INSERT INTO categorias (nome) VALUES
    ('Eletrônicos'),
    ('Ferramentas'),
    ('Papelaria');

INSERT INTO fornecedores (nome, contato, email) VALUES
    ('TechDistribuições', '(35) 98888-1111', 'contato@techdist.com'),
    ('FerramentasMax', '(35) 97777-2222', 'vendas@ferramentasmax.com');

INSERT INTO produtos (nome, descricao, preco, quantidade, categoria_id) VALUES
    ('Teclado Mecânico', 'Teclado switch blue', 250.00, 15, 1),
    ('Mouse Gamer', 'Mouse 12000 DPI', 180.00, 20, 1),
    ('Chave de Fenda', 'Chave philips número 2', 25.00, 50, 2);

INSERT INTO produto_fornecedor (produto_id, fornecedor_id) VALUES
    (1, 1),
    (2, 1),
    (3, 2);