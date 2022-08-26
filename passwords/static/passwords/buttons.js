function showPassword(event, password) {
    if (event.target.innerHTML === "Show") {
        event.target.closest('#password_row').querySelector('#password').innerHTML = password;
        event.target.innerHTML = "Hide";
    }
    else {
        event.target.closest('#password_row').querySelector('#password').innerHTML = "•••••••••••";
        event.target.innerHTML = "Show";
    }
}


function copy(text) {
    navigator.clipboard.writeText(text);
}