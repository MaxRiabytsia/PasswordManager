async function sha256(message) {
    const msgBuffer = new TextEncoder().encode(message);
    const hashBuffer = await crypto.subtle.digest('SHA-256', msgBuffer);
    const hashArray = Array.from(new Uint8Array(hashBuffer));
    const hashHex = hashArray.map(b => b.toString(16).padStart(2, '0')).join('');
    return hashHex;
}


async function getUserKey(username, password) {
    let masterPassword = `${username}${password}`;
    for (let i = 0; i < 10; i++) {
        masterPassword = await sha256(masterPassword);
    }
    document.cookie = `userKey=${masterPassword}`;
}
