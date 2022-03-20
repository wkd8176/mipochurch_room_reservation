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

function setCookie(name, value, expiredays) {
    var today = new Date();
    today.setDate(today.getDate() + expiredays);
    document.cookie = name + '=' + escape(value) + '; expires=' + today.toGMTString();
}

function getCookie(name) {
    var cookie = document.cookie;
    if (document.cookie != '') {
        var cookie_array = cookie.split('; ');
        for (var index in cookie_array) {
            var cookie_name = cookie_array[index].split('=');
            if (cookie_name[0] == 'mycookie') {
                return cookie_name[1];
            }
        }
    }
    return;
}

$('#modal_today_close').click(function () {
    $('#noticeModal').modal('hide');
    setCookie('mycookie', 'popupEnd', 1);
});

var checkCookie = getCookie('mycookie');

document.addEventListener('DOMContentLoaded', function () {
    if (checkCookie == 'popupEnd') {
        $('#noticeModal').modal('hide');
    } else {
        $('#noticeModal').modal('show');
    }
});

var now = new Date();
var initialDate = sessionStorage.getItem('initialDate')
if (initialDate == null){
    initialDate = moment(now).format("YYYY[-]MM[-]DD");
    sessionStorage.setItem('initialDate',initialDate);
} else {
    console.log(sessionStorage.getItem('initialDate'));
}
$('#reservation_submit').click(function () {
    createDate = moment($('#start_time').val()).format("YYYY[-]MM[-]DD");
    console.log(createDate)
    sessionStorage.setItem('initialDate',createDate);
});
$('#editReservationBtn').click(function () {
    editDate = moment($('#editStartTime').val()).format("YYYY[-]MM[-]DD");
    sessionStorage.setItem('initialDate',editDate);
});