document.addEventListener('DOMContentLoaded', function () {
    const hallList = document.getElementById('hall-list');
    const bookingPopup = document.getElementById('booking-popup');
    const slotSelect = document.getElementById('slot-select');
    const confirmBookingButton = document.getElementById('confirm-booking');
    const cancelPopupButton = document.getElementById('cancel-popup');
    const bookingList = document.getElementById('booking-list');

    let halls = [];
    let selectedHallId = null;

    // Функция для получения данных о залах
    async function fetchHalls() {
        try {
            const response = await fetch('/api/sportshalls/');
            if (!response.ok) throw new Error('Ошибка при загрузке залов');
            halls = await response.json();

            // Очищаем список
            hallList.innerHTML = '';

            // Добавляем залы в список
            halls.forEach(hall => {
                const li = document.createElement('li');
                li.textContent = `${hall.name} - ${hall.address}`;

                const bookButton = document.createElement('button');
                bookButton.textContent = 'Забронировать';
                bookButton.addEventListener('click', () => openBookingPopup(hall.id));
                li.appendChild(bookButton);

                hallList.appendChild(li);
            });
        } catch (error) {
            console.error(error);
            hallList.innerHTML = '<li>Ошибка при загрузке данных</li>';
        }
    }

    // Функция для открытия попапа
    function openBookingPopup(hallId) {
        selectedHallId = hallId;
        fetchSlots(hallId);
        bookingPopup.style.display = 'block';
    }

    // Функция для загрузки доступных слотов
    async function fetchSlots(hallId) {
        try {
            const response = await fetch(`/api/availableslots/?hall=${hallId}`);
            if (!response.ok) throw new Error('Ошибка при загрузке слотов');
            const slots = await response.json();

            // Очищаем выпадающий список
            slotSelect.innerHTML = '';

            // Добавляем слоты в выпадающий список
            slots.forEach(slot => {
                const option = document.createElement('option');
                option.value = slot.id;
                option.textContent = `${slot.available_date} ${slot.start_time}-${slot.end_time}`;
                slotSelect.appendChild(option);
            });
        } catch (error) {
            console.error(error);
            slotSelect.innerHTML = '<option>Ошибка при загрузке слотов</option>';
        }
    }

    // Функция для подтверждения бронирования
    confirmBookingButton.addEventListener('click', async function () {
        const slotId = slotSelect.value;

        try {
            const response = await fetch('/api/bookings/', {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({ slot: slotId }),
            });

            if (!response.ok) throw new Error('Ошибка при создании бронирования');
            alert('Бронирование успешно создано!');
            bookingPopup.style.display = 'none'; // Скрываем попап
            fetchBookings(); // Обновляем список бронирований
        } catch (error) {
            console.error(error);
            alert('Ошибка при создании бронирования');
        }
    });

    // Функция для закрытия попапа
    cancelPopupButton.addEventListener('click', function () {
        bookingPopup.style.display = 'none';
    });

    // Функция для загрузки бронирований
    async function fetchBookings() {
        try {
            const response = await fetch('/api/bookings/');
            if (!response.ok) throw new Error('Ошибка при загрузке бронирований');
            const bookings = await response.data;

            // Очищаем список
            bookingList.innerHTML = '';

            // Добавляем бронирования в список
            bookings.forEach(booking => {
                const li = document.createElement('li');
                li.textContent = `${booking.slot.hall.name} - ${booking.slot.available_date} ${booking.slot.start_time}`;

                const deleteButton = document.createElement('button');
                deleteButton.textContent = 'Удалить';
                deleteButton.addEventListener('click', () => deleteBooking(booking.id));
                li.appendChild(deleteButton);

                bookingList.appendChild(li);
            });
        } catch (error) {
            console.error(error);
            bookingList.innerHTML = '<li>Ошибка при загрузке бронирований</li>';
        }
    }

    // Функция для удаления бронирования
    async function deleteBooking(bookingId) {
        try {
            const response = await fetch(`/api/bookings/${bookingId}/`, {
                method: 'DELETE',
            });

            if (!response.ok) throw new Error('Ошибка при удалении бронирования');
            alert('Бронирование успешно удалено!');
            fetchBookings(); // Обновляем список бронирований
        } catch (error) {
            console.error(error);
            alert('Ошибка при удалении бронирования');
        }
    }

    // Загружаем данные при загрузке страницы
    fetchHalls();
    fetchBookings();
});