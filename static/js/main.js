// ============================================================
// NAVBAR TOGGLE (Hamburger Menu)
// ============================================================
function toggleMenu() {
    const navLinks = document.querySelector('.nav-links');
    navLinks.classList.toggle('active');
}

// Close menu when clicking outside
document.addEventListener('click', function(event) {
    const navLinks = document.querySelector('.nav-links');
    const hamburger = document.querySelector('.hamburger');
    
    if (navLinks && hamburger) {
        if (!navLinks.contains(event.target) && !hamburger.contains(event.target)) {
            navLinks.classList.remove('active');
        }
    }
});

// ============================================================
// TIPS CAROUSEL (Dashboard)
// ============================================================
document.addEventListener('DOMContentLoaded', function() {
    const tips = document.querySelectorAll('.tip-card');
    if (tips.length > 0) {
        let currentTip = 0;
        
        setInterval(() => {
            tips.forEach(tip => tip.classList.remove('active'));
            currentTip = (currentTip + 1) % tips.length;
            tips[currentTip].classList.add('active');
        }, 5000);
    }
});

// ============================================================
// SCROLL ANIMATIONS
// ============================================================
const animateOnScroll = () => {
    const elements = document.querySelectorAll('.animate-on-scroll');
    
    const observer = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.classList.add('visible');
            }
        });
    }, { threshold: 0.1 });
    
    elements.forEach(el => observer.observe(el));
};

document.addEventListener('DOMContentLoaded', animateOnScroll);

// ============================================================
// CONSOLE WELCOME
// ============================================================
console.log('%c PlacementPro v1.0 ', 'background: #6c5ce7; color: white; font-size: 20px; font-weight: bold; padding: 10px 20px; border-radius: 5px;');
console.log('%c Your AI-Powered Placement Preparation Partner ', 'color: #6c5ce7; font-size: 14px;');