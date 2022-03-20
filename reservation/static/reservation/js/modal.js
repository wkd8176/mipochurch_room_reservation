$('#editReservationModalBtn').click(function () {
    var eventId = $(this).data('id');
    var booker = $(this).data('booker');
    var participants = $(this).data('participants');
    var start = $(this).data('start');
    var end = $(this).data('end');
    var description = $(this).data('description');
    $('#editBooker').attr('value', booker);
    $('#editParticipants').attr('value', participants);
    $('#editStartTime').attr('value', start);
    $('#editEndTime').attr('value', end);
    document.getElementById('editDescription').innerHTML = description;
    $('#reservation_edit_form').attr('action', 'edit/' + eventId + '/');
});
$('#deleteReservationModalBtn').click(function () {
    var eventId = $(this).data('id');
    $('#reservation_delete_form').attr('action', 'delete/' + eventId + '/');
});
