
$(document).ready(function () {
    $('button.request').click(function () {
        console.log($(this).attr('data-note'));
        $.ajax({
            url: `${window.location.origin}/notes/delete`,
            type: 'DELETE',
            method: 'DELETE',
            dataType: 'json',
            contentType: 'application/json; charset=utf-8',
            data: JSON.stringify({ note_id: $(this).attr('data-note')}),
            success: function () {
                window.location.href = '/home'
            }
        });
    });
});