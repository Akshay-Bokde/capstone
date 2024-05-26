document.addEventListener('DOMContentLoaded', () => {
    const submitButton = document.querySelector('button');

    submitButton.addEventListener('mouseenter', () => {
        submitButton.style.boxShadow = '0 4px 15px rgba(0, 0, 0, 0.2)';
    });

    submitButton.addEventListener('mouseleave', () => {
        submitButton.style.boxShadow = 'none';
    });
});
