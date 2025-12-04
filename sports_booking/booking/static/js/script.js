document.addEventListener('DOMContentLoaded', function () {
    const hallList = document.getElementById('hall-list');

    // Функция для получения данных о залах
    async function fetchHalls() {
        try {
            const response = await fetch('/api/sportshalls/');
            if (!response.ok) {
                throw new Error('Ошибка при загрузке данных');
            }
            const halls = await response.json();

            // Очищаем список
            hallList.innerHTML = '';

            // Добавляем залы в список
            halls.forEach(hall => {
                const li = document.createElement('li');
                li.textContent = `${hall.name} - ${hall.address}`;
                hallList.appendChild(li);
            });
        } catch (error) {
            console.error(error);
            hallList.innerHTML = '<li>Ошибка при загрузке данных</li>';
        }
    }

    // Загружаем данные при загрузке страницы
    fetchHalls();
});