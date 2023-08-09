document.addEventListener("DOMContentLoaded", function() {
    const form = document.getElementById("registrationForm");
    const errorText = document.getElementById("errorText");

    form.addEventListener("submit", function(event) {
        event.preventDefault();

        errorText.style.display = "none";
        errorText.innerHTML = "";

        const password = document.getElementById("password").value;
        const confirmPassword = document.getElementById("confirm_password").value;
        const photoInput = document.getElementById("photo");
        const birthdayInput = document.getElementById("birthday");
        const nameInput = document.getElementById("name");
        const emailInput = document.getElementById("email");

        let errors = [];

        if (password !== confirmPassword) {
            errors.push("Passwords do not match.");
        }

        if (photoInput.files.length > 0 && photoInput.files[0].size > 5 * 1024 * 1024) {
            errors.push("File size should be less than 5MB.");
        }

        const today = new Date();
        const birthday = new Date(birthdayInput.value);
        const age = today.getFullYear() - birthday.getFullYear();
        if (age < 16) {
            errors.push("You must be at least 16 years old to register.");
        }

        if (nameInput.value.trim() === "") {
            errors.push("Name is required.");
        }
        if (emailInput.value.trim() === "") {
            errors.push("Email is required.");
        }

        if (errors.length > 0) {
            errorText.style.display = "block";
            errorText.innerHTML = errors.map(error => `<p>${error}</p>`).join("");
        } else {
            window.location.href = "thankyou.html";
        }
    });
});
