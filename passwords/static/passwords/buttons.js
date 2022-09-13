function showPassword(event, password) {
    if (event.target.innerHTML.trim() === 'Show') {
        event.target.closest('#password_row').querySelector('#password').innerHTML = password;
        event.target.innerHTML = 'Hide';
    } else {
        event.target.closest('#password_row').querySelector('#password').innerHTML = "•••••••••••";
        event.target.innerHTML = 'Show';
    }
}


function copy(text) {
    document.getElementById("custom-tooltip").style.display = "inline";
    navigator.clipboard.writeText(text);
    setTimeout( function() {
        document.getElementById("custom-tooltip").style.display = "none";
    }, 1000);
}
