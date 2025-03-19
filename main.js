document.addEventListener('DOMContentLoaded', function() {
    const protectedLinks = document.querySelectorAll('.protected');

    protectedLinks.forEach(link => {
        link.addEventListener('click', function(e) {
            const loggedInEmail = localStorage.getItem('loggedIn');
            if (!loggedInEmail) {
                e.preventDefault();
                alert('You must be logged in to access this page');
                window.location.href = 'login.html';
            }
        });
    });
});
