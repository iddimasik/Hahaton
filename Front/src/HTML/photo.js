const photoBig2 = document.getElementById('photoBig2');
let isBig = false; // Переменная для хранения состояния фотографии (увеличена или нет)

photoBig2.addEventListener('click', function() {
    if (!isBig) { // Если фотография не увеличена
        // Увеличиваем размер фотографии в photoBig2
        photoBig2.style.transform = 'scale(2)'; // Увеличение в 2 раза
        isBig = true; // Устанавливаем флаг, что фотография увеличена
    } else { // Если фотография уже увеличена
        // Сбрасываем увеличение размера фотографии в photoBig2
        photoBig2.style.transform = 'scale(1)'; // Возвращаем исходный размер
        isBig = false; // Сбрасываем флаг
    }
});
