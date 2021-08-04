function submitDecryptionForm(e) {
    // Prevent form submission
    e.preventDefault();
    form = e.currentTarget
    var targetElement = document.querySelector(`#${form.dataset.decryptionFormFor}`);
    var password = form.elements["decryptionPassword"].value
    attemptDecryptElement(targetElement,password);
    return false
}

function catob(s){
    return CryptoJS.enc.Base64.parse(s);
}

function attemptDecryptElement(e, password) {
    var content = decryptb64(e.dataset.encData, password, e.dataset.salt, e.dataset.iv)
    // If the data is successfully decrypted, add it to the page and return true, else return false.
    try {
        var decryptedContent = content.toString(CryptoJS.enc.Utf8);
        if (decryptedContent) {
            e.innerHTML = decryptedContent
            return true;
        } else {
            e.textContent = "Decryption unsuccessful."
            return false;
        }
    } catch  {
        e.textContent = "Decryption unsuccessful."
        return false;
    }
}

function decryptb64(ciphertext, password, salt, iv){
    // Pass all arguments in base64.
    var key = CryptoJS.PBKDF2(password, catob(salt), {
     keySize: 256 / 32, iterations: 13337
    });
    return CryptoJS.AES.decrypt({ciphertext: catob(ciphertext)}, key, {iv: catob(iv), padding: CryptoJS.pad.Pkcs7});
}