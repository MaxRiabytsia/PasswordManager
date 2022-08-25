function showPassword(event, password) {
    event.target.closest('#row').querySelector('#password').innerHTML = password;
}


function copy(text) {
    navigator.clipboard.writeText(text);
}