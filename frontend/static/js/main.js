const API = '/api'

async function carregarTotais() {
  const [produtos, categorias, fornecedores] = await Promise.all([
    fetch(`${API}/produtos/`).then(r => r.json()),
    fetch(`${API}/categorias/`).then(r => r.json()),
    fetch(`${API}/fornecedores/`).then(r => r.json()),
  ])

  document.getElementById('total-produtos').textContent = produtos.length
  document.getElementById('total-categorias').textContent = categorias.length
  document.getElementById('total-fornecedores').textContent = fornecedores.length

  const tbody = document.getElementById('tabela-produtos')
  tbody.innerHTML = produtos.map(p => `
    <tr>
      <td>${p.id}</td>
      <td>${p.nome}</td>
      <td>${p.categoria_nome ?? '—'}</td>
      <td>R$ ${Number(p.preco).toFixed(2)}</td>
      <td>${p.quantidade}</td>
    </tr>
  `).join('')
}

carregarTotais()
