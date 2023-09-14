// Function to submit the form and handle the response
function submitForm() {
    const userResponse = document.getElementById("user-response").value;
    if (userResponse.toLowerCase() === "no") {
        // Show the flash message for "No" response
        const flashMessage = document.getElementById("flash-message");
        flashMessage.style.display = "block";

        // Hide the flash message after 3 seconds (adjust as needed)
        setTimeout(function () {
            flashMessage.style.display = "none";
        }, 3000);
    } else if (userResponse.toLowerCase() === "yes") {
        // Redirect to the registration page for "Yes" response
        window.location.href = "/registration";
        return false; // Prevent form submission
    }
    return false; // Prevent form submission
}
