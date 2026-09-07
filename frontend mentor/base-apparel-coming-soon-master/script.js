document.addEventListener('DOMContentLoaded', () => {
  const form = document.getElementById('newsletter-form');
  const emailInput = document.getElementById('email');

  const validateEmail = (email) => {
    // Standard RFC-compliant email verification pattern
    const regex = /^[a-zA-Z0-9.!#$%&'*+/=?^_`{|}~-]+@[a-zA-Z0-9-]+(?:\.[a-zA-Z0-9-]+)+$/;
    return regex.test(String(email).trim());
  };

  form.addEventListener('submit', (e) => {
    e.preventDefault();
    const value = emailInput.value.trim();

    if (!value || !validateEmail(value)) {
      form.classList.remove('success');
      form.classList.add('error');
      emailInput.setAttribute('aria-invalid', 'true');
    } else {
      form.classList.remove('error');
      emailInput.removeAttribute('aria-invalid');
      
      // Feedback on submission
      emailInput.value = '';
      alert("Thank you! You've been subscribed for updates.");
    }
  });

  // Clear the error outline while user is re-typing
  emailInput.addEventListener('input', () => {
    if (form.classList.contains('error')) {
      form.classList.remove('error');
      emailInput.removeAttribute('aria-invalid');
    }
  });
});
