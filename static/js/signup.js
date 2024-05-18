function validatePassword() {
    var password = document.getElementById("password").value;
    var repeatPassword = document.getElementById("repeatpsw").value;
    if (password !== repeatPassword) {
        alert("Passwords don't match, check for syntax errors");
        return false;
    }
    return true
}