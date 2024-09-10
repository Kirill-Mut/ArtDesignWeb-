$(document).ready(function() {
    // Добавление комнаты
    $('#add-room').click(function() {
        var formset = $('#room-section');
        var totalForms = formset.find('input[name$=TOTAL_FORMS]');
        var currentFormCount = parseInt(totalForms.val());
        var newForm = formset.find('.room-form:first').clone();
        newForm.find('input').each(function() {
            var name = $(this).attr('name').replace(/-\d+-/, '-' + currentFormCount + '-');
            $(this).attr('name', name).val('');
        });
        formset.append(newForm);
        totalForms.val(currentFormCount + 1);
    });

    // Удаление комнаты
    $(document).on('click', '.remove-roomBtn', function() {
        $(this).closest('.room-form').remove();
    });

    // Добавление внешней фотографии
    $('#add-exterior-photo').click(function() {
        var formset = $('#exterior-photo-section');
        var totalForms = formset.find('input[name$=TOTAL_FORMS]');
        var currentFormCount = parseInt(totalForms.val());
        var newForm = formset.find('.exterior-photo-form:first').clone();
        newForm.find('input').each(function() {
            var name = $(this).attr('name').replace(/-\d+-/, '-' + currentFormCount + '-');
            $(this).attr('name', name).val('');
        });
        formset.append(newForm);
        totalForms.val(currentFormCount + 1);
    });

    // Удаление внешней фотографии
    $(document).on('click', '.remove-exterior-photoBtn', function() {
        $(this).closest('.exterior-photo-form').remove();
    });

    // Добавление внутренней фотографии
    $('#add-interior-photo').click(function() {
        var formset = $('#interior-photo-section');
        var totalForms = formset.find('input[name$=TOTAL_FORMS]');
        var currentFormCount = parseInt(totalForms.val());
        var newForm = formset.find('.interior-photo-form:first').clone();
        newForm.find('input').each(function() {
            var name = $(this).attr('name').replace(/-\d+-/, '-' + currentFormCount + '-');
            $(this).attr('name', name).val('');
        });
        formset.append(newForm);
        totalForms.val(currentFormCount + 1);
    });

    // Удаление внутренней фотографии
    $(document).on('click', '.remove-interior-photoBtn', function() {
        $(this).closest('.interior-photo-form').remove();
    });
});