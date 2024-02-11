// Получаем ссылки на элементы
const imagePopup = document.querySelector('.image-popup');
const modalContainer = document.querySelector('.modal-container');
const modalImage = document.getElementById('modal-image');
const closeModal = document.querySelector('.close-modal');

// Добавляем обработчик события клика на элемент image-popup
imagePopup.addEventListener('click', function() {
    const imgSrc = this.querySelector('source').srcset; // Получаем источник изображения из тега source
    const imgAlt = this.querySelector('img').alt; // Получаем атрибут alt изображения

    // Устанавливаем свойства изображения в модальном окне
    modalImage.src = imgSrc;
    modalImage.alt = imgAlt;

    // Показываем модальное окно
    modalContainer.style.display = 'block';
});

// Добавляем обработчик события клика на элемент закрытия модального окна
closeModal.addEventListener('click', function() {
    // Скрываем модальное окно
    modalContainer.style.display = 'none';
});
