async function sha256(message) {
    const msgBuffer = new TextEncoder().encode(message);
    const hashBuffer = await crypto.subtle.digest('SHA-256', msgBuffer);
    const hashArray = Array.from(new Uint8Array(hashBuffer));
    const hashHex = hashArray.map(b => b.toString(16).padStart(2, '0')).join('');
    return hashHex;
}


async function getUserKey(username, password) {
    let masterPassword = `${username}${password}`;
    console.log(masterPassword);
    for (let i = 0; i < 5; i++) {
        masterPassword = await sha256(masterPassword);
        console.log(masterPassword);
    }
    localStorage.setItem('masterPassword', masterPassword);
}
