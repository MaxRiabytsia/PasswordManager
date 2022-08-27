function showPassword(event, password) {
    console.log(event.target.innerHTML)
    if (event.target.innerHTML.trim() === 'Show') {
        event.target.closest('#password_row').querySelector('#password').innerHTML = password;
        event.target.innerHTML = 'Hide';
    }
    else {
        event.target.closest('#password_row').querySelector('#password').innerHTML = "•••••••••••";
        event.target.innerHTML = 'Show';
    }
}


function copy(text) {
    navigator.clipboard.writeText(text);
}