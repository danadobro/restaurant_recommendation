document.addEventListener('DOMContentLoaded', () => {
    const navToggle = document.querySelector('.nav-toggle');
    navToggle.addEventListener('click', () => {
        const nav = document.querySelector('nav ul');
        nav.classList.toggle('active');
    });
});
document.getElementById('foodSelectionForm').addEventListener('submit', function(event) {
    event.preventDefault(); // Prevent the form from submitting the traditional way

    const cuisine = document.getElementById('cuisine').value;
    const budget = document.getElementById('budget').value;
    const vibe = document.getElementById('vibe').value;

    console.log(`Cuisine: ${cuisine}, Budget: ${budget}, Vibe: ${vibe}`);
    // TODO
});

document.addEventListener('DOMContentLoaded', function() {
    const form = document.querySelector('form');
    form.style.opacity = 0;

    setTimeout(() => {
        form.style.opacity = 1;
        form.style.transform = 'translateY(0)';
    }, 100);

    document.getElementById('foodSelectionForm').addEventListener('submit', function(event) {
        event.preventDefault(); // Prevent the form from submitting the traditional way

        const cuisine = document.getElementById('cuisine').value;
        const budget = document.getElementById('budget').value;
        const vibe = document.getElementById('vibe').value;

        console.log(`Cuisine: ${cuisine}, Budget: ${budget}, Vibe: ${vibe}`);
        // TODO post-submission logic
    });
});