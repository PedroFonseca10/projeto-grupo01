const container = document.getElementById('container');
const registerBtn = document.getElementById('register');
const loginBtn = document.getElementById('login');
const registerForm = document.getElementById('registerForm');
const loginForm = document.getElementById('loginForm');
const messageElement = document.getElementById('message');

const showMessage = (text, success = true) => {
    messageElement.textContent = text;
    messageElement.style.color = success ? '#00a86b' : '#d8000c';
};

registerBtn.addEventListener('click', () => {
    container.classList.add('active');
    showMessage('');
});

loginBtn.addEventListener('click', () => {
    container.classList.remove('active');
    showMessage('');
});

registerForm.addEventListener('submit', async (event) => {
    event.preventDefault();

    const nome = document.getElementById('registerName').value.trim();
    const email = document.getElementById('registerEmail').value.trim();
    const senha = document.getElementById('registerPassword').value.trim();

    if (!nome || !email || !senha) {
        showMessage('Preencha todos os campos de cadastro.', false);
        return;
    }

    try {
        const response = await fetch('/api/auth/registrar', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ nome_completo: nome, email, senha })
        });
        const data = await response.json();

        if (response.ok) {
            showMessage('Cadastro realizado com sucesso. Faça login.', true);
            container.classList.remove('active');
        } else {
            showMessage(data.erro || 'Erro ao cadastrar usuário.', false);
        }
    } catch (error) {
        showMessage('Erro ao conectar com o backend.', false);
    }
});

loginForm.addEventListener('submit', async (event) => {
    event.preventDefault();

    const email = document.getElementById('loginEmail').value.trim();
    const senha = document.getElementById('loginPassword').value.trim();

    if (!email || !senha) {
        showMessage('Preencha email e senha.', false);
        return;
    }

    try {
        const response = await fetch('/api/auth/login', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ email, senha })
        });
        const data = await response.json();

        if (response.ok) {
            localStorage.setItem('token', data.token);
            localStorage.setItem('usuario', JSON.stringify(data.usuario));
            showMessage('Login realizado com sucesso.', true);
            // Redirecionar para o sistema após 1.5 segundos
            setTimeout(() => {
                window.location.href = '/sistema';
            }, 1500);
        } else {
            showMessage(data.erro || 'Email ou senha inválidos.', false);
        }
    } catch (error) {
        showMessage('Erro ao conectar com o backend.', false);
    }
});
