// Navbar fixa: adiciona sombra ao rolar
const navbar = document.querySelector('nav');

window.addEventListener('scroll', () => {
    if (window.scrollY > 10) {
        navbar.classList.add('nav-scrolled');
    } else {
        navbar.classList.remove('nav-scrolled');
    }
});

// Scroll suave com offset para compensar a navbar fixa
function scrollToElement(elementSelector, instance = 0) {
    const elements = document.querySelectorAll(elementSelector);
    if (elements.length > instance) {
        const navHeight = navbar.offsetHeight;
        const elementTop = elements[instance].getBoundingClientRect().top + window.scrollY;
        window.scrollTo({
            top: elementTop - navHeight - 16,
            behavior: 'smooth'
        });
    }
}

const linkInicio = document.querySelector('.nav-links li:first-child a');
const link1 = document.querySelector("#link1 a");
const link2 = document.querySelector("#link2 a");
const link3 = document.querySelector("#link3 a");

linkInicio.addEventListener('click', (e) => {
    e.preventDefault();
    window.scrollTo({ top: 0, behavior: 'smooth' });
});

link1.addEventListener('click', (e) => {
    e.preventDefault();
    scrollToElement('.features');
});
link2.addEventListener('click', (e) => {
    e.preventDefault();
    scrollToElement('.preços');
});
link3.addEventListener('click', (e) => {
    e.preventDefault();
    scrollToElement('footer');
});