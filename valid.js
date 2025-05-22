function myfunction() {
    var x = document.getElementById("password");

    if (x.type == 'password') {
        x.type = "text";
    } else {
        x.type = "password";
    }
}

function validate(event) {
    event.preventDefault(); // Prevent the default form submission behavior
    console.log("Validation function triggered");

    var password = document.getElementById("password").value;
    console.log("Password entered:", password);

    if (password.length >= 8) {
        alert('Password is valid');
        window.location.href = "homepage.html"; // Redirect to homepage.html
    } else {
        alert('Password is invalid');
        console.log("Password is too short.");
    }

    return false; // Explicitly return false to prevent form submission
}