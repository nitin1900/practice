const shareBtn = document.getElementById('special');
const shareBox = document.getElementById('shareBox');

shareBtn.addEventListener('click', (e) => {
    e.stopPropagation();
    shareBox.classList.toggle('hidden');
});

// Optional: close the tooltip when clicking outside anywhere on the page
document.addEventListener('click', (e) => {
    if (!shareBox.contains(e.target) && e.target !== shareBtn) {
        shareBox.classList.add('hidden');
    }
});