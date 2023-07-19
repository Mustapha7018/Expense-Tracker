// Get the error messages div
const errorMessagesDiv = document.getElementById('error_messages');

// Function to show the error messages div
function showErrorMessages() {
  errorMessagesDiv.style.display = 'block';
}

// Function to hide the error messages div
function hideErrorMessages() {
  errorMessagesDiv.style.display = 'none';
}

// Attach form validation to form submission event
const form = document.querySelector('form');
form.addEventListener('submit', function(event) {
  const password = document.getElementsByName('password')[0].value;
  const confirm_password = document.getElementsByName('confirm_password')[0].value;

  if (password !== confirm_password) {
    event.preventDefault(); // Prevent form submission
    errorMessagesDiv.innerHTML = '<div>Password mismatch!</div>';
    showErrorMessages();
  } else {
    hideErrorMessages();
  }
});
