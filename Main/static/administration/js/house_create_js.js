// Добавление новых полей для внутренних фотографий
document.querySelector('.add-internal-photo').addEventListener('click', function() {
    const container = document.getElementById('internal-photo-container');
    const newInput = document.createElement('div');
    newInput.classList.add('internal-photo');
    newInput.innerHTML = `
        <input type="file" name="internal_photos[]" multiple>
        <button type="button" class="remove-internal-photo">Удалить</button>
    `;
    container.appendChild(newInput);
});

// Удаление полей для внутренних фотографий
document.getElementById('internal-photo-container').addEventListener('click', function(event) {
    if (event.target.classList.contains('remove-internal-photo')) {
        event.target.closest('.internal-photo').remove();
    }
});

// Добавление новых полей для внешних фотографий
document.querySelector('.add-external-photo').addEventListener('click', function() {
    const container = document.getElementById('external-photo-container');
    const newInput = document.createElement('div');
    newInput.classList.add('external-photo');
    newInput.innerHTML = `
        <input type="file" name="external_photos[]" multiple>
        <button type="button" class="remove-external-photo">Удалить</button>
    `;
    container.appendChild(newInput);
});

// Удаление полей для внешних фотографий
document.getElementById('external-photo-container').addEventListener('click', function(event) {
    if (event.target.classList.contains('remove-external-photo')) {
        event.target.closest('.external-photo').remove();
    }
});

// Добавление новых полей для комнат
document.getElementById('add-room').addEventListener('click', function() {
    const container = document.getElementById('room-container');
    const newRoom = document.createElement('div');
    newRoom.classList.add('room');
    newRoom.innerHTML = `
        <input type="text" name="room_names[]" placeholder="Название комнаты">
        <input type="number" name="room_areas[]" placeholder="Площадь комнаты (м²)">
        <button type="button" class="remove-room">Удалить</button>
    `;
    container.appendChild(newRoom);
});

// Удаление полей для комнат
document.getElementById('room-container').addEventListener('click', function(event) {
    if (event.target.classList.contains('remove-room')) {
        event.target.closest('.room').remove();
    }
});