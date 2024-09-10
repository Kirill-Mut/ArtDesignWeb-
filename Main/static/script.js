//____________________скрипт для главной_________________
const phrases = ["НОВАЯ ФИЛОСОФИЯ ЖИЛЬЯ", "НЕ СТРОИМ, А СОБИРАЕМ ДОМА", "ВЫСОКАЯ СКОРОСТЬ ВОЗВЕДЕНИЯ", "КОНЦЕПЦИЯ РАСТУЩЕГО ДОМА"];
const phrases2 = ["Идя в ногу со временем, мы создаем быстровозводимые современные модульные дома с различной конфигурацией. Технология BY home основана на принципах рациональности и оптимальности. Это проявляется в удачном сочетании экологичных материалов, энергоэффективности, функциональности и общей стоимости дома.",
    "Преимущество модульных домов в том, что их можно конфигурировать перед строительством и расширять дом путем добавления модулей в будущем. Модули производятся на заводе, где осуществляется должный контроль качества, а затем доставляются и собираются на участке под техническим надзором.",
    "Строительство модульного дома под ключ занимает от нескольких месяцев до полугода. Такие короткие сроки обусловлены тем, что все несущие элементы, инженерные коммуникации, материалы отделки фасада устанавливаются в модулях на производстве, а процесс монтажа представляет собой сборку дома как конструктор.", 
    "Главная идея нашей технологии - быстросборный дом из готовых заводских элементов высокого качества. Построив однажды модульный дом, вы не ограничены его текущими размерами. По мере роста семьи и потребностей, вы можете достроить модули и после нескольких лет проживания увеличить дом до нужных размеров."];
let currentIndex = 0;
let currentIndexDown = 0;
let intervalId;
function updatePhrase() {
    const phraseElement = document.getElementById("phrase");
    const phraseElementDown = document.getElementById("phraseDown");
    // Добавляем класс fade-out для исчезновения
    phraseElement.classList.add("fade-out");
    phraseElementDown.classList.add("fade-out");
    // Ждем завершения анимации перед изменением текста
    setTimeout(() => {
        currentIndex = (currentIndex + 1) % phrases.length;
        currentIndexDown = (currentIndexDown + 1) % phrases2.length;
        phraseElement.textContent = phrases[currentIndex];
        phraseElementDown.textContent = phrases2[currentIndex];
        // Убираем класс fade-out и добавляем fade для появления
        phraseElement.classList.remove("fade-out");
        phraseElementDown.classList.remove("fade-out");
        void phraseElement.offsetWidth; // Перезапускаем анимацию
        void phraseElementDown.offsetWidth;
        phraseElement.classList.add("fade");
        phraseElementDown.classList.add("fade");
    }, 500); // Время совпадает с временем анимации в CSS
}
function changePhrase(index) {
    currentIndex = index;
    currentIndexDown = index;
    updatePhrase();
    resetInterval();
}
function resetInterval() {
    clearInterval(intervalId);
    intervalId = setInterval(updatePhrase, 5000);
}
// Инициализация
updatePhrase();
resetInterval();
//____________________скрипт для слайдера_________________
const slides = document.querySelectorAll('.card-testimonial');
let currentSlide = 0;
function showSlide(index) {
    slides.forEach((slide, i) => {slide.style.transform = `translateX(${(i - index*40)}%)`; });
}
function nextSlide() {
    currentSlide = (currentSlide + 1) % slides.length; // Переход к следующему слайду
    showSlide(currentSlide);
}
// Автоматическое переключение слайдов каждые 3 секунды
setInterval(nextSlide, 5000);
// Обработка прокрутки мышкой
let isMouseDown = false;
document.querySelector('.marquee-wrapper').addEventListener('mousedown', (e) => {
    isMouseDown = true;
    startX = e.pageX - document.querySelector('.marquee-wrapper').offsetLeft;
});
document.querySelector('.marquee-wrapper').addEventListener('mouseup', () => {
    isMouseDown = false;
});
document.querySelector('.marquee-wrapper').addEventListener('mouseleave', () => {
    isMouseDown = false;
});
document.querySelector('.marquee-wrapper').addEventListener('mousemove', (e) => {
    if (!isMouseDown) return;
    const x = e.pageX - document.querySelector('.marquee-wrapper').offsetLeft;
    const walk = (x - startX); // Разница между начальной и текущей позицией мыши
    if (walk > 50) { // Если мышь переместилась вправо более чем на 50px
        currentSlide = (currentSlide - 2 + slides.length) % slides.length; // Назад на 2 слайда
        showSlide(currentSlide);
        isMouseDown = false; // Остановить движение
    } else if (walk < -50) { // Если мышь переместилась влево более чем на 50px
        currentSlide = (currentSlide + 2) % slides.length; // Вперед на 2 слайда
        showSlide(currentSlide);
        isMouseDown = false; // Остановить движение
    }
});
//____________________скрипт для FAQ_________________
const faqButtons = document.querySelectorAll('.faq-button');
faqButtons.forEach(button => {
    button.addEventListener('click', () => {
        const content = button.nextElementSibling;
        const icon = button.querySelector('.iconFaq');
        const circle = button.querySelector('.circle');
        const separator = content.nextElementSibling; // Получаем следующий элемент (separator)
        // Закрыть все остальные открытые блоки
        faqButtons.forEach(otherButton => {
            if (otherButton !== button) {
                const otherContent = otherButton.nextElementSibling;
                const otherIcon = otherButton.querySelector('.iconFaq');
                // Проверяем, открыт ли другой блок
                if (otherContent.classList.contains('show')) {
                    otherContent.classList.remove('show');
                    otherIcon.src = '../static/images/plus.svg'; // Меняем на "плюс"
                }
            }
        });
        content.classList.toggle('show');
        if (content.classList.contains('show')) {
            icon.src = '../static/images/cross.svg'; // Измените на изображение "крест"
            separator.style.opacity = "0"; // Прячем полосу
        } else {
            icon.src = '../static/images/plus.svg'; // Измените на изображение "плюс"
            separator.style.opacity = "1"; // Показываем полосу
        }
                // Показать круг
                circle.style.opacity = '1';
                circle.style.transform = 'translate(-50%, -50%) scale(1.5)';
                // Скрыть круг через короткое время
                setTimeout(() => {
                    circle.style.opacity = '0';
                    circle.style.transform = 'translate(-50%, -50%) scale(1)';
                }, 300); // Длительность анимации


                
    });
});