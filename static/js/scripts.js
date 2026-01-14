
// Убираем фокус с кнопки навбара при закрытии меню
const navbarToggler = document.querySelector('.navbar-toggler');
const navbarCollapse = document.querySelector('.navbar-collapse');

if (navbarToggler && navbarCollapse) {
    navbarCollapse.addEventListener('hidden.bs.collapse', function () {
        navbarToggler.blur();
    });
}

// Создаем новогоднюю атмосферу
const background = document.getElementById('christmasBackground');

// Эмодзи для украшений
const decorations = ['🎄', '⛄', '🎁', '🔔', '⭐', '🎅', '🦌', '🕯️', '🧦'];
const snowflakes = ['❄', '❅', '❆'];

// Создаем снежинки
function createSnowflakes() {
    const numSnowflakes = window.innerWidth > 768 ? 30 : 15;
    
    for (let i = 0; i < numSnowflakes; i++) {
        const snowflake = document.createElement('div');
        snowflake.className = 'snowflake';
        snowflake.innerHTML = snowflakes[Math.floor(Math.random() * snowflakes.length)];
        snowflake.style.left = Math.random() * 100 + '%';
        snowflake.style.animationDuration = (Math.random() * 3 + 5) + 's';
        snowflake.style.animationDelay = Math.random() * 5 + 's';
        snowflake.style.fontSize = (Math.random() * 0.8 + 0.8) + 'rem';
        background.appendChild(snowflake);
    }
}

// Создаем новогодние украшения
function createDecorations() {
    const numDecorations = window.innerWidth > 768 ? 15 : 8;
    
    for (let i = 0; i < numDecorations; i++) {
        const decoration = document.createElement('div');
        decoration.className = 'christmas-decoration';
        decoration.innerHTML = decorations[Math.floor(Math.random() * decorations.length)];
        decoration.style.left = Math.random() * 90 + '%';
        decoration.style.top = Math.random() * 90 + '%';
        decoration.style.animationDelay = Math.random() * 3 + 's';
        decoration.style.animationDuration = (Math.random() * 2 + 5) + 's';
        background.appendChild(decoration);
    }
}

// Инициализация
createSnowflakes();
createDecorations();

// Пересоздаем при изменении размера окна
let resizeTimer;
window.addEventListener('resize', function() {
    clearTimeout(resizeTimer);
    resizeTimer = setTimeout(function() {
        background.innerHTML = '';
        createSnowflakes();
        createDecorations();
    }, 250);
});

