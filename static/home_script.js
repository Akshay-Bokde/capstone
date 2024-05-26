document.addEventListener('DOMContentLoaded', () => {
    const buttons = document.querySelectorAll('.button');
    buttons.forEach(button => {
        button.addEventListener('mouseenter', () => {
            button.style.boxShadow = '0 4px 15px rgba(0, 0, 0, 0.2)';
        });

        button.addEventListener('mouseleave', () => {
            button.style.boxShadow = 'none';
        });
    });
});
