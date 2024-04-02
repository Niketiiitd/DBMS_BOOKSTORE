// Function to validate the vendor registration form
function validateVendorRegistrationForm() {
    var form = document.getElementById('vendor-registration-form');
    var password = form.elements['password'].value;
    var confirmPassword = form.elements['confirm_password'].value;

    // Check if password and confirm password match
    if (password !== confirmPassword) {
        alert('Passwords do not match. Please re-enter your password.');
        return false; // Prevent form submission
    }

    // Check password strength
    var strengthMessage = checkPasswordStrength(password);
    if (strengthMessage !== "Strong password.") {
        alert(strengthMessage);
        return false; // Prevent form submission
    }

    // If password is strong, proceed with form submission
    alert("Vendor registration done!"); // Display success message
    saveVendorRegistrationData(); // Save data to the database
    return true; // Allow form submission
}

// Event listener to validate form on submission
document.getElementById('vendor-registration-form').addEventListener('submit', function(event) {
    if (!validateVendorRegistrationForm()) {
        event.preventDefault(); // Prevent form submission if validation fails
    }
});

function checkPasswordStrength(password) {
    // Check length
    if (password.length < 8) {
        return "Password must be at least 8 characters long.";
    }

    // Check for uppercase letters
    if (!/[A-Z]/.test(password)) {
        return "Password must contain at least one uppercase letter.";
    }

    // Check for lowercase letters
    if (!/[a-z]/.test(password)) {
        return "Password must contain at least one lowercase letter.";
    }

    // Check for numbers
    if (!/\d/.test(password)) {
        return "Password must contain at least one number.";
    }

    // Check for special characters
    if (!/[!@#$%^&*()_+{}\[\]:;<>,.?/~\-]/.test(password)) {
        return "Password must contain at least one special character.";
    }

    // Check for common patterns
    if (/password|123456|qwerty|letmein/i.test(password)) {
        return "Password is too common and easily guessable.";
    }

    // Check for personal information
    if (/john|doe|birthdate|address/i.test(password)) {
        return "Password should not contain personal information.";
    }

    // Password meets all criteria
    return "Strong password.";
}

// Function to save vendor registration data to the database
function saveVendorRegistrationData() {
    // Implement saving data to the database here
    // This function is a placeholder and should be replaced with actual database logic
    console.log("Saving vendor registration data to the database...");
}
