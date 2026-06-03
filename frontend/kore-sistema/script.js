/* ============================================================
   KoreArmazen · script.js
   ============================================================ */

// ─────────────────────────────────────────────
// 0. AUTENTICAÇÃO E TOKEN
// ─────────────────────────────────────────────
function verificarAutenticacao() {
  const token = localStorage.getItem('token');
  if (!token) {
    window.location.href = '/';
    return false;
  }
  return true;
}

function obterHeadersAutenticados() {
  const token = localStorage.getItem('token');
  return {
    'Content-Type': 'application/json',
    'Authorization': `Bearer ${token}`
  };
}

function fazerLogout() {
  localStorage.removeItem('token');
  localStorage.removeItem('usuario');
  window.location.href = '/';
}

if (!verificarAutenticacao()) {
  return;
}

window.fazerLogout = fazerLogout;
window.showToast = (msg, type = 'ok') => console.log(`[${type}] ${msg}`);

// ─────────────────────────────────────────────
// INICIALIZAÇÃO
// ─────────────────────────────────────────────
document.addEventListener('DOMContentLoaded', function() {
  const sidebar = document.getElementById('sidebar');
  const toggleBtn = document.getElementById('toggleBtn');
  const mainWrap = document.getElementById('mainWrap');
  const navItems = document.querySelectorAll('.nav-item');
  const themeBtn = document.getElementById('themeBtn');
  const logoutBtn = document.querySelector('.logout-btn');
  
  // Sidebar Toggle
  if (toggleBtn && sidebar) {
    toggleBtn.addEventListener('click', () => {
      sidebar.classList.toggle('collapsed');
      if (mainWrap) mainWrap.classList.toggle('expanded');
    });
  }
  
  // Navigation
  navItems.forEach(item => {
    item.addEventListener('click', (e) => {
      e.preventDefault();
      const target = item.dataset.page;
      if (!target) return;
      
      navItems.forEach(n => n.classList.remove('active'));
      item.classList.add('active');
      
      const pages = document.querySelectorAll('.page');
      pages.forEach(p => p.classList.remove('active'));
      const targetPage = document.getElementById(`page-${target}`);
      if (targetPage) targetPage.classList.add('active');
      
      if (sidebar && sidebar.classList.contains('mobile-open')) {
        sidebar.classList.remove('mobile-open');
      }
    });
  });
  
  // Theme
  if (themeBtn) {
    themeBtn.addEventListener('click', () => {
      document.body.classList.toggle('dark');
    });
  }
  
  // Logout
  if (logoutBtn) {
    logoutBtn.addEventListener('click', fazerLogout);
  }
});

// ─────────────────────────────────────────────
// API - Funções para chamar o backend
// ─────────────────────────────────────────────
const API = {
  // Fornecedores
  listarFornecedores: async () => {
    try {
      const response = await fetch('/api/fornecedores', {
        method: 'GET',
        headers: obterHeadersAutenticados()
      });
      if (response.ok) return await response.json();
      if (response.status === 401) { fazerLogout(); return []; }
      return [];
    } catch (err) {
      showToast('Erro ao listar fornecedores', 'danger');
      return [];
    }
  },

  // Produtos
  listarProdutos: async () => {
    try {
      const response = await fetch('/api/produtos', {
        method: 'GET',
        headers: obterHeadersAutenticados()
      });
      if (response.ok) return await response.json();
      if (response.status === 401) { fazerLogout(); return []; }
      return [];
    } catch (err) {
      showToast('Erro ao listar produtos', 'danger');
      return [];
    }
  },

  // Entradas
  listarEntradas: async () => {
    try {
      const response = await fetch('/api/entradas', {
        method: 'GET',
        headers: obterHeadersAutenticados()
      });
      if (response.ok) return await response.json();
      if (response.status === 401) { fazerLogout(); return []; }
      return [];
    } catch (err) {
      showToast('Erro ao listar entradas', 'danger');
      return [];
    }
  },

  // Saídas
  listarSaidas: async () => {
    try {
      const response = await fetch('/api/saidas', {
        method: 'GET',
        headers: obterHeadersAutenticados()
      });
      if (response.ok) return await response.json();
      if (response.status === 401) { fazerLogout(); return []; }
      return [];
    } catch (err) {
      showToast('Erro ao listar saídas', 'danger');
      return [];
    }
  }
};

window.API = API;

// Aguardar o DOM estar pronto antes de inicializar
document.addEventListener('DOMContentLoaded', () => {

// ─────────────────────────────────────────────
// 1. SIDEBAR TOGGLE
// ─────────────────────────────────────────────
const sidebar  = document.getElementById('sidebar');
const mainWrap = document.getElementById('mainWrap');
const toggleBtn = document.getElementById('toggleBtn');
const logoutBtn = document.querySelector('.logout-btn');

// Evento do botão de logout
if (logoutBtn) {
  logoutBtn.addEventListener('click', fazerLogout);
}

let isMobile = () => window.innerWidth <= 768;

if (toggleBtn) {
  toggleBtn.addEventListener('click', () => {
    if (isMobile()) {
      sidebar.classList.toggle('mobile-open');
      sidebar.classList.remove('collapsed');
    } else {
      sidebar.classList.toggle('collapsed');
      mainWrap.classList.toggle('expanded');
    }
  });
}

// Fecha sidebar mobile ao clicar fora
if (sidebar) {
  document.addEventListener('click', (e) => {
    if (isMobile() && sidebar.classList.contains('mobile-open')) {
      if (!sidebar.contains(e.target) && (!toggleBtn || !toggleBtn.contains(e.target))) {
        sidebar.classList.remove('mobile-open');
      }
    }
  });
}

if (sidebar) {
  window.addEventListener('resize', () => {
    if (!isMobile()) {
      sidebar.classList.remove('mobile-open');
    }
  });
}

// ─────────────────────────────────────────────
// 2. NAVEGAÇÃO ENTRE PÁGINAS
// ─────────────────────────────────────────────
const navItems  = document.querySelectorAll('.nav-item');
const pages     = document.querySelectorAll('.page');
const pageLabel = document.getElementById('pageLabel');

navItems.forEach(item => {
  item.addEventListener('click', (e) => {
    e.preventDefault();
    const target = item.dataset.page;
    if (!target) return;

    // Atualiza menu ativo
    navItems.forEach(n => n.classList.remove('active'));
    item.classList.add('active');

    // Atualiza páginas
    pages.forEach(p => p.classList.remove('active'));
    const targetPage = document.getElementById(`page-${target}`);
    if (targetPage) targetPage.classList.add('active');

    // Atualiza label da topbar
    const label = item.querySelector('span');
    if (label) pageLabel.textContent = label.textContent;

    // Fecha sidebar mobile
    if (isMobile()) sidebar.classList.remove('mobile-open');
  });
});

// ─────────────────────────────────────────────
// 3. TEMA CLARO / ESCURO
// ─────────────────────────────────────────────
const themeBtn  = document.getElementById('themeBtn');
const darkToggle = document.getElementById('darkToggle');

function setDark(on) {
  document.body.classList.toggle('dark', on);
  if (themeBtn) {
    const icon = themeBtn.querySelector('i');
    if (icon) icon.className = on ? 'bx bx-sun' : 'bx bx-moon';
  }
  if (darkToggle) darkToggle.checked = on;
  localStorage.setItem('kore-dark', on ? '1' : '0');
}

// Restaurar preferência salva
const savedDark = localStorage.getItem('kore-dark');
if (savedDark === '1') setDark(true);

if (themeBtn) {
  themeBtn.addEventListener('click', () => {
    setDark(!document.body.classList.contains('dark'));
  });
}

// Sync toggle das configurações
if (darkToggle) {
  darkToggle.addEventListener('change', () => setDark(darkToggle.checked));
}

// ─────────────────────────────────────────────
// 4. MODAIS
// ─────────────────────────────────────────────
const overlay = document.getElementById('modalOverlay');

function openModal(id) {
  closeModal(); // fecha qualquer modal aberto
  const modal = document.getElementById(id);
  if (!modal) return;
  overlay.classList.add('open');
  modal.style.display = 'flex';
  // Pequeno delay para ativar transição CSS
  requestAnimationFrame(() => {
    requestAnimationFrame(() => modal.classList.add('open'));
  });
  document.body.style.overflow = 'hidden';
}

function closeModal() {
  const openM = document.querySelector('.modal.open');
  if (openM) {
    openM.classList.remove('open');
    setTimeout(() => { openM.style.display = 'none'; }, 250);
  }
  overlay.classList.remove('open');
  document.body.style.overflow = '';
}

// ESC fecha modal
document.addEventListener('keydown', (e) => {
  if (e.key === 'Escape') closeModal();
});

// Expor funções globalmente (chamadas inline nos botões HTML)
window.openModal  = openModal;
window.closeModal = closeModal;

// ─────────────────────────────────────────────
// 5. TOAST NOTIFICATIONS
// ─────────────────────────────────────────────
const toast    = document.getElementById('toast');
const toastMsg = document.getElementById('toastMsg');
let toastTimer;

function showToast(msg, type = 'ok') {
  clearTimeout(toastTimer);
  toastMsg.textContent = msg;
  toast.className = 'toast';
  if (type === 'warn')   toast.classList.add('toast-warn');
  if (type === 'danger') toast.classList.add('toast-danger');

  const icon = toast.querySelector('i');
  icon.className = type === 'ok'
    ? 'bx bx-check-circle'
    : type === 'warn'
    ? 'bx bx-error'
    : 'bx bx-x-circle';

  toast.classList.add('show');
  toastTimer = setTimeout(() => toast.classList.remove('show'), 3500);
}

window.showToast = showToast;

// ─────────────────────────────────────────────
// 6. DATA ATUAL
// ─────────────────────────────────────────────
const dateEl = document.getElementById('currentDate');
if (dateEl) {
  const now = new Date();
  dateEl.textContent = now.toLocaleDateString('pt-BR', {
    weekday: 'long', day: 'numeric', month: 'long', year: 'numeric'
  });
}

// ─────────────────────────────────────────────
// 7. GRÁFICO DE BARRAS (Dashboard)
// ─────────────────────────────────────────────
const barChartEl = document.getElementById('mainBarChart');

if (barChartEl) {
  const meses = ['Dez', 'Jan', 'Fev', 'Mar', 'Abr', 'Mai'];
  const entradas  = [420, 390, 510, 480, 560, 892];
  const saidas    = [350, 420, 390, 520, 610, 750];
  const maxVal = Math.max(...entradas, ...saidas);

  meses.forEach((mes, i) => {
    const hIn  = Math.round((entradas[i] / maxVal) * 130);
    const hOut = Math.round((saidas[i]   / maxVal) * 130);

    const group = document.createElement('div');
    group.className = 'bar-group';

    group.innerHTML = `
      <div class="bars">
        <div class="bar bar-in"  style="height:${hIn}px"  title="Entradas ${mes}: ${entradas[i]}"></div>
        <div class="bar bar-out" style="height:${hOut}px" title="Saídas ${mes}: ${saidas[i]}"></div>
      </div>
      <span class="bar-label">${mes}</span>
    `;

    barChartEl.appendChild(group);
  });
}

// ─────────────────────────────────────────────
// 8. FILTRO DE ABAS (ftab) — genérico
// ─────────────────────────────────────────────
document.querySelectorAll('.filter-tabs').forEach(group => {
  group.querySelectorAll('.ftab').forEach(btn => {
    btn.addEventListener('click', () => {
      group.querySelectorAll('.ftab').forEach(b => b.classList.remove('active'));
      btn.classList.add('active');
    });
  });
});

// ─────────────────────────────────────────────
// 9. VISUALIZAÇÃO TABELA / GRADE (Estoque)
// ─────────────────────────────────────────────
const viewTable   = document.getElementById('viewTable');
const viewGrid    = document.getElementById('viewGrid');
const btnTable    = document.getElementById('viewTable') && document.querySelector('#viewTable');
const vtabTable   = document.querySelector('#viewTable.vtab') || document.getElementById('viewTable');
const vtabGrid    = document.getElementById('viewGrid');
const tableView   = document.getElementById('tableView');
const gridViewEl  = document.getElementById('gridView');
const gridInner   = document.getElementById('productGridInner');

// Dados dos produtos para o grid
const produtos = [
  { icon: 'bx bx-chip',         cls: 'pi-blue',   name: 'Processador Intel i9',     sku: 'SKU-0021', cat: 'cat-elet', catLabel: 'Eletrônicos', qty: 240, status: 'ok',     statusLabel: 'Normal' },
  { icon: 'bx bx-wrench',       cls: 'pi-orange',  name: 'Chave Combinada 13mm',     sku: 'SKU-0048', cat: 'cat-ferr', catLabel: 'Ferramentas', qty: 85,  status: 'ok',     statusLabel: 'Normal' },
  { icon: 'bx bx-laptop',       cls: 'pi-violet',  name: 'Notebook Dell Vostro',     sku: 'SKU-0012', cat: 'cat-elet', catLabel: 'Eletrônicos', qty: 15,  status: 'warn',   statusLabel: 'Baixo' },
  { icon: 'bx bx-cable-car',    cls: 'pi-teal',    name: 'Cabo HDMI 2m',             sku: 'SKU-0093', cat: 'cat-elet', catLabel: 'Eletrônicos', qty: 420, status: 'ok',     statusLabel: 'Normal' },
  { icon: 'bx bx-battery',      cls: 'pi-rose',    name: 'Bateria 18650 3.7V',       sku: 'SKU-0156', cat: 'cat-elet', catLabel: 'Eletrônicos', qty: 8,   status: 'danger', statusLabel: 'Crítico' },
  { icon: 'bx bx-droplet',      cls: 'pi-orange',  name: 'Óleo Lubrificante 1L',     sku: 'SKU-0210', cat: 'cat-mat',  catLabel: 'Materiais',   qty: 63,  status: 'ok',     statusLabel: 'Normal' },
  { icon: 'bx bx-memory-card',  cls: 'pi-blue',    name: 'Memória RAM 16GB DDR5',    sku: 'SKU-0075', cat: 'cat-elet', catLabel: 'Eletrônicos', qty: 22,  status: 'warn',   statusLabel: 'Baixo' },
];

function renderGridCards() {
  if (!gridInner) return;
  gridInner.innerHTML = '';
  produtos.forEach(p => {
    const card = document.createElement('div');
    card.className = 'pgrid-card';
    card.innerHTML = `
      <div class="prod-icon pgrid-icon ${p.cls}"><i class='${p.icon}'></i></div>
      <div>
        <p class="pgrid-name">${p.name}</p>
        <p class="pgrid-sku">${p.sku}</p>
      </div>
      <p class="pgrid-qty">${p.qty} <span>unid.</span></p>
      <div style="display:flex;align-items:center;justify-content:space-between;gap:8px">
        <span class="cat-tag ${p.cat}">${p.catLabel}</span>
        <span class="pill ${p.status}">${p.statusLabel}</span>
      </div>
    `;
    gridInner.appendChild(card);
  });
}

const vtBtns = document.querySelectorAll('.view-toggle .vtab');
if (vtBtns.length) {
  vtBtns.forEach((btn, idx) => {
    btn.addEventListener('click', () => {
      vtBtns.forEach(b => b.classList.remove('active'));
      btn.classList.add('active');
      if (idx === 0) {
        // Tabela
        if (tableView)  tableView.style.display = '';
        if (gridViewEl) gridViewEl.classList.add('hidden');
      } else {
        // Grid
        if (tableView)  tableView.style.display = 'none';
        if (gridViewEl) gridViewEl.classList.remove('hidden');
        renderGridCards();
      }
    });
  });
}

// ─────────────────────────────────────────────
// 10. BUSCA NO ESTOQUE (filtro simples)
// ─────────────────────────────────────────────
const estoqueSearch = document.getElementById('estoque-search');
const estoqueTbody  = document.getElementById('estoque-tbody');

if (estoqueSearch && estoqueTbody) {
  estoqueSearch.addEventListener('input', () => {
    const q = estoqueSearch.value.toLowerCase().trim();
    estoqueTbody.querySelectorAll('tr').forEach(row => {
      row.style.display = row.textContent.toLowerCase().includes(q) ? '' : 'none';
    });
  });
}

// ─────────────────────────────────────────────
// 11. CONFIGURAÇÕES — ABAS INTERNAS
// ─────────────────────────────────────────────
const stabs  = document.querySelectorAll('.stab');
const panels = document.querySelectorAll('.stab-panel');

stabs.forEach(btn => {
  btn.addEventListener('click', () => {
    stabs.forEach(b => b.classList.remove('active'));
    panels.forEach(p => p.classList.remove('active'));
    btn.classList.add('active');
    const panelId = `stab-${btn.dataset.stab}`;
    const panel = document.getElementById(panelId);
    if (panel) panel.classList.add('active');
  });
});

// ─────────────────────────────────────────────
// 12. CHECKBOX "SELECIONAR TODOS" (tabelas)
// ─────────────────────────────────────────────
document.querySelectorAll('.check-all').forEach(chk => {
  chk.addEventListener('change', () => {
    const table = chk.closest('table');
    table.querySelectorAll('tbody input[type="checkbox"]')
      .forEach(c => c.checked = chk.checked);
  });
});

// ─────────────────────────────────────────────
// 13. BOTÃO LOGOUT
// ─────────────────────────────────────────────
document.querySelector('.logout-btn')?.addEventListener('click', () => {
  showToast('Saindo do sistema...', 'warn');
  setTimeout(() => {
    // Em produção: window.location.href = '/logout'
    showToast('Você foi desconectado.', 'ok');
  }, 1500);
});

// ─────────────────────────────────────────────
// 14. BOTÃO "SALVAR ALTERAÇÕES" (Configurações)
// ─────────────────────────────────────────────
document.querySelectorAll('.page-header .btn-primary').forEach(btn => {
  if (btn.textContent.trim().includes('Salvar')) {
    btn.addEventListener('click', () => {
      showToast('Configurações salvas com sucesso!', 'ok');
    });
  }
});

// ─────────────────────────────────────────────
// 15. ATALHO TECLADO ⌘K / Ctrl+K — foco busca
// ─────────────────────────────────────────────
document.addEventListener('keydown', (e) => {
  if ((e.metaKey || e.ctrlKey) && e.key === 'k') {
    e.preventDefault();
    const si = document.querySelector('.search-box input');
    if (si) si.focus();
  }
});

}); // Fecha DOMContentLoaded