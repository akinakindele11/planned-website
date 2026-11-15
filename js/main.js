// Planned Limited - Main JavaScript (loaded on every page)

document.addEventListener('DOMContentLoaded', function () {

    // =========================================
    // MOBILE MENU TOGGLE
    // =========================================
    var hamburgers = document.querySelectorAll('.hamburger, .mobile-menu-toggle');
    var navMenu = document.querySelector('.nav-menu') || document.getElementById('navMenu');
    var dropdowns = document.querySelectorAll('.dropdown, .nav-dropdown');

    function setMenu(open) {
        if (!navMenu) return;
        navMenu.classList.toggle('active', open);
        hamburgers.forEach(function (h) { h.setAttribute('aria-expanded', open ? 'true' : 'false'); });
    }

    function closeDropdowns(except) {
        dropdowns.forEach(function (d) {
            if (d === except) return;
            d.classList.remove('active');
            var t = d.querySelector('.dropdown-toggle');
            if (t) t.setAttribute('aria-expanded', 'false');
        });
    }

    hamburgers.forEach(function (hamburger) {
        hamburger.addEventListener('click', function () {
            setMenu(!(navMenu && navMenu.classList.contains('active')));
        });
    });

    // Close the mobile menu when a real link is followed. Dropdown toggles are
    // buttons, and any legacy href="#" toggles are excluded, so opening a
    // sub-menu never closes the whole menu.
    if (navMenu) {
        navMenu.querySelectorAll('a[href]:not(.dropdown-toggle):not([href="#"])').forEach(function (link) {
            link.addEventListener('click', function () {
                setMenu(false);
                closeDropdowns(null);
            });
        });
    }

    // =========================================
    // DROPDOWN MENUS (click / tap / keyboard)
    // =========================================
    dropdowns.forEach(function (dropdown) {
        var toggle = dropdown.querySelector('.dropdown-toggle');
        if (!toggle) return;
        toggle.addEventListener('click', function (e) {
            e.preventDefault();
            e.stopPropagation();
            var open = !dropdown.classList.contains('active');
            closeDropdowns(dropdown);
            dropdown.classList.toggle('active', open);
            toggle.setAttribute('aria-expanded', open ? 'true' : 'false');
        });
    });

    document.addEventListener('click', function (e) {
        if (!e.target.closest('.dropdown, .nav-dropdown')) closeDropdowns(null);
    });

    document.addEventListener('keydown', function (e) {
        if (e.key === 'Escape') { closeDropdowns(null); setMenu(false); }
    });

    // =========================================
    // FAQ TOGGLE (div-based, subpages)
    // =========================================
    document.querySelectorAll('.faq-header').forEach(function (header) {
        header.addEventListener('click', function () {
            var faqItem = this.closest('.faq-item');
            if (!faqItem) return;
            document.querySelectorAll('.faq-item.active').forEach(function (item) {
                if (item !== faqItem) item.classList.remove('active');
            });
            faqItem.classList.toggle('active');
        });
    });

    // =========================================
    // REVEAL ON SCROLL
    // =========================================
    var revealElements = document.querySelectorAll('.reveal');
    if (revealElements.length > 0 && 'IntersectionObserver' in window) {
        var revealObserver = new IntersectionObserver(function (entries) {
            entries.forEach(function (entry) {
                if (entry.isIntersecting) {
                    entry.target.classList.add('visible');
                    revealObserver.unobserve(entry.target);
                }
            });
        }, { threshold: 0.1 });
        revealElements.forEach(function (el) { revealObserver.observe(el); });
    } else {
        revealElements.forEach(function (el) { el.classList.add('visible'); });
    }

    // =========================================
    // SMOOTH SCROLL FOR IN-PAGE ANCHORS
    // =========================================
    document.querySelectorAll('a[href^="#"]').forEach(function (anchor) {
        anchor.addEventListener('click', function (e) {
            var href = this.getAttribute('href');
            if (!href || href === '#' || href.length < 2) return;
            var target = null;
            try { target = document.querySelector(href); } catch (err) { return; }
            if (target) {
                e.preventDefault();
                target.scrollIntoView({ behavior: 'smooth', block: 'start' });
            }
        });
    });

    // =========================================
    // ENQUIRY ATTRIBUTION (every page)
    // Remembers the first page of the visit, the referrer and any UTM tags,
    // then fills the hidden fields on the contact form so each Netlify
    // submission carries its source.
    // =========================================
    try {
        var params = new URLSearchParams(location.search);
        if (!sessionStorage.getItem('pl_landing')) {
            sessionStorage.setItem('pl_landing', location.pathname + location.search);
            sessionStorage.setItem('pl_referrer', document.referrer || '(direct)');
            ['utm_source', 'utm_medium', 'utm_campaign'].forEach(function (k) {
                if (params.get(k)) sessionStorage.setItem('pl_' + k, params.get(k));
            });
        }
        var form = document.querySelector('form[name="contact"]');
        if (form) {
            var setField = function (name, val) {
                var el = form.querySelector('[name="' + name + '"]');
                if (el) el.value = val || '';
            };
            setField('referrer', sessionStorage.getItem('pl_referrer'));
            setField('landing_page', sessionStorage.getItem('pl_landing'));
            setField('utm_source', sessionStorage.getItem('pl_utm_source'));
            setField('utm_medium', sessionStorage.getItem('pl_utm_medium'));
            setField('utm_campaign', sessionStorage.getItem('pl_utm_campaign'));

            // Preselect the service from ?service= (e.g. /contact?service=tender-programme)
            var wanted = params.get('service');
            var select = form.querySelector('select[name="service"]');
            if (wanted && select) {
                for (var i = 0; i < select.options.length; i++) {
                    if (select.options[i].value === wanted) { select.selectedIndex = i; break; }
                }
            }

            form.addEventListener('submit', function () {
                if (window.gtag) gtag('event', 'generate_lead', { method: 'contact_form' });
            });
        }
    } catch (err) { /* storage blocked: form still submits without attribution */ }
});

// =========================================
// FAQ TOGGLE (button-based, used on homepage)
// =========================================
function toggleFaq(element) {
    var faqItem = element.closest('.faq-item');
    if (!faqItem) return;
    document.querySelectorAll('.faq-item.active').forEach(function (item) {
        if (item !== faqItem) {
            item.classList.remove('active');
            var b = item.querySelector('.faq-question');
            if (b) b.setAttribute('aria-expanded', 'false');
        }
    });
    var open = faqItem.classList.toggle('active');
    if (element.classList.contains('faq-question')) element.setAttribute('aria-expanded', open ? 'true' : 'false');
}
