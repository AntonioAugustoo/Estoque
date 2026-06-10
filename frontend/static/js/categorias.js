const API = '/api'

async function carregarCategorias() {
  const categorias = await fetch(`${API}/categorias/`).then(r => r.json())
  const tbody = document.getElementById('tabela-categorias')
  tbody.innerHTML = categorias.map(c => `
    <tr>
      <td>${c.id}</td>
      <td>${c.nome}</td>
      <td><button class="btn-delete" onclick="deletarCategoria(${c.id})">deletar</button></td>
    </tr>
  `).join('')
}

async function carregarFornecedores() {
  const fornecedores = await fetch(`${API}/fornecedores/`).then(r => r.json())
  const tbody = document.getElementById('tabela-fornecedores')
  tbody.innerHTML = fornecedores.map(f => `
    <tr>
      <td>${f.id}</td>
      <td>${f.nome}</td>
      <td>${f.contato ?? '—'}</td>
      <td><button class="btn-delete" onclick="deletarFornecedor(${f.id})">deletar</button></td>
    </tr>
  `).join('')
}

async function criarCategoria() {
  const nome = document.getElementById('nome-categoria').value.trim()
  if (!nome) { alert('Preencha o nome da categoria.'); return }
  await fetch(`${API}/categorias/`, {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ nome })
  })
  document.getElementById('nome-categoria').value = ''
  await carregarCategorias()
}

async function criarFornecedor() {
  const nome = document.getElementById('nome-fornecedor').value.trim()
  const contato = document.getElementById('contato-fornecedor').value.trim()
  const email = document.getElementById('email-fornecedor').value.trim()
  if (!nome) { alert('Preencha o nome do fornecedor.'); return }
  await fetch(`${API}/fornecedores/`, {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ nome, contato: contato || null, email: email || null })
  })
  document.getElementById('nome-fornecedor').value = ''
  document.getElementById('contato-fornecedor').value = ''
  document.getElementById('email-fornecedor').value = ''
  await carregarFornecedores()
}

async function deletarCategoria(id) {
  if (!confirm(`Deseja deletar a categoria #${id}?`)) return
  await fetch(`${API}/categorias/${id}`, { method: 'DELETE' })
  await carregarCategorias()
}

async function deletarFornecedor(id) {
  if (!confirm(`Deseja deletar o fornecedor #${id}?`)) return
  await fetch(`${API}/fornecedores/${id}`, { method: 'DELETE' })
  await carregarFornecedores()
}

carregarCategorias()
carregarFornecedores()
