// Planned Limited - Main JavaScript

document.addEventListener('DOMContentLoaded', function() {

    // =========================================
    // MOBILE MENU TOGGLE
    // =========================================
    const hamburgers = document.querySelectorAll('.hamburger, .mobile-menu-toggle');
    const navMenu = document.querySelector('.nav-menu') || document.getElementById('navMenu');

    hamburgers.forEach(function(hamburger) {
        hamburger.addEventListener('click', function() {
            if (navMenu) {
                navMenu.classList.toggle('active');
                // Update aria-expanded
                const expanded = navMenu.classList.contains('active');
                this.setAttribute('aria-expanded', expanded);
            }
        });
    });

    // Close mobile menu when clicking a nav link
    if (navMenu) {
        navMenu.querySelectorAll('a').forEach(function(link) {
            link.addEventListener('click', function() {
                navMenu.classList.remove('active');
                hamburgers.forEach(function(h) {
                    h.setAttribute('aria-expanded', 'false');
                });
            });
        });
    }

    // =========================================
    // DROPDOWN MENUS (Mobile)
    // =========================================
    const dropdowns = document.querySelectorAll('.dropdown, .nav-dropdown');
    dropdowns.forEach(function(dropdown) {
        const toggle = dropdown.querySelector('a, .dropdown-toggle');
        if (toggle) {
            toggle.addEventListener('click', function(e) {
                if (window.innerWidth <= 768) {
                    e.preventDefault();
                    dropdown.classList.toggle('active');
                }
            });
        }
    });

    // =========================================
    // FAQ TOGGLE
    // =========================================
    // For FAQ items with .faq-header (div-based toggle on subpages)
    document.querySelectorAll('.faq-header').forEach(function(header) {
        header.addEventListener('click', function() {
            const faqItem = this.closest('.faq-item');
            if (!faqItem) return;

            // Close other open FAQs
            document.querySelectorAll('.faq-item.active').forEach(function(item) {
                if (item !== faqItem) {
                    item.classList.remove('active');
                }
            });

            faqItem.classList.toggle('active');
        });
    });

    // =========================================
    // CONTACT FORM (handled by Netlify Forms)
    // =========================================
    // Form submits natively to Netlify — no JavaScript interception needed

    // =========================================
    // REVEAL ON SCROLL ANIMATION
    // =========================================
    const revealElements = document.querySelectorAll('.reveal');
    if (revealElements.length > 0) {
        const revealObserver = new IntersectionObserver(function(entries) {
            entries.forEach(function(entry) {
                if (entry.isIntersecting) {
                    entry.target.classList.add('visible');
                    revealObserver.unobserve(entry.target);
                }
            });
        }, { threshold: 0.1 });

        revealElements.forEach(function(el) {
            revealObserver.observe(el);
        });
    }

    // =========================================
    // SMOOTH SCROLL FOR ANCHOR LINKS
    // =========================================
    document.querySelectorAll('a[href^="#"]').forEach(function(anchor) {
        anchor.addEventListener('click', function(e) {
            const target = document.querySelector(this.getAttribute('href'));
            if (target) {
                e.preventDefault();
                target.scrollIntoView({ behavior: 'smooth', block: 'start' });
            }
        });
    });
});

// =========================================
// FAQ TOGGLE (button-based, used on homepage)
// =========================================
function toggleFaq(element) {
    const faqItem = element.closest('.faq-item');
    if (!faqItem) return;

    // Close other open FAQs
    document.querySelectorAll('.faq-item.active').forEach(function(item) {
        if (item !== faqItem) {
            item.classList.remove('active');
        }
    });

    faqItem.classList.toggle('active');
}
