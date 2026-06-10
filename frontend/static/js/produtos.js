const API = '/api'

async function carregarCategorias() {
  const categorias = await fetch(`${API}/categorias/`).then(r => r.json())
  const select = document.getElementById('categoria_id')
  categorias.forEach(c => {
    const option = document.createElement('option')
    option.value = c.id
    option.textContent = c.nome
    select.appendChild(option)
  })
}

async function carregarProdutos() {
  const produtos = await fetch(`${API}/produtos/`).then(r => r.json())
  const tbody = document.getElementById('tabela-produtos')
  tbody.innerHTML = produtos.map(p => `
    <tr>
      <td>${p.id}</td>
      <td>${p.nome}</td>
      <td>${p.categoria_nome ?? '—'}</td>
      <td>R$ ${Number(p.preco).toFixed(2)}</td>
      <td>${p.quantidade}</td>
      <td><button class="btn-delete" onclick="deletarProduto(${p.id})">deletar</button></td>
    </tr>
  `).join('')
}

async function criarProduto() {
  const nome = document.getElementById('nome').value.trim()
  const descricao = document.getElementById('descricao').value.trim()
  const preco = parseFloat(document.getElementById('preco').value)
  const quantidade = parseInt(document.getElementById('quantidade').value)
  const categoria_id = document.getElementById('categoria_id').value
  if (!nome || isNaN(preco) || isNaN(quantidade)) {
    alert('Preencha pelo menos nome, preco e quantidade.')
    return
  }
  await fetch(`${API}/produtos/`, {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ nome, descricao: descricao || null, preco, quantidade, categoria_id: categoria_id ? parseInt(categoria_id) : null })
  })
  document.getElementById('nome').value = ''
  document.getElementById('descricao').value = ''
  document.getElementById('preco').value = ''
  document.getElementById('quantidade').value = ''
  document.getElementById('categoria_id').value = ''
  await carregarProdutos()
}

async function deletarProduto(id) {
  if (!confirm(`Deseja deletar o produto #${id}?`)) return
  await fetch(`${API}/produtos/${id}`, { method: 'DELETE' })
  await carregarProdutos()
}

carregarCategorias()
carregarProdutos()
