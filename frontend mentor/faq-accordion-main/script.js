const faqItems = document.querySelectorAll('.faq-item');

faqItems.forEach(item => {
    const button = item.querySelector('.question-btn');
    const icon = item.querySelector('.toggle-icon');

    button.addEventListener('click', () => {
        const isActive = item.classList.toggle('active');

        // Update accessibility attributes
        button.setAttribute('aria-expanded', isActive);

        // Switch icons between plus and minus
        icon.src = isActive 
            ? 'assets/images/icon-minus.svg' 
            : 'assets/images/icon-plus.svg';
    });
});