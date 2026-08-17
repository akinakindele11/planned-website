/*!
 * Planned Limited — cookie consent + Google Consent Mode v2
 * Self-hosted. No third-party CMP, no account, no cost.
 *
 * Load order in <head> matters and is enforced by the page template:
 *   1. inline: define dataLayer + gtag, set Consent Mode defaults to DENIED
 *   2. this file (synchronous)  — applies a stored choice before any tag fires
 *   3. gtag.js (async)
 *
 * Behaviour required by UK PECR / ICO guidance:
 *   - nothing non-essential is set before a choice is made
 *   - rejecting is exactly as easy as accepting (same size, same prominence)
 *   - the choice can be changed later, from any page
 */
(function () {
  "use strict";

  var COOKIE = "planned_consent";
  var MONTHS = 6;                       // re-ask twice a year
  var VERSION = 1;                      // bump to re-prompt everyone

  function read() {
    var m = document.cookie.match(/(?:^|;\s*)planned_consent=([^;]*)/);
    if (!m) return null;
    try {
      var v = JSON.parse(decodeURIComponent(m[1]));
      return (v && v.v === VERSION) ? v : null;
    } catch (e) { return null; }
  }

  function write(granted) {
    var val = encodeURIComponent(JSON.stringify({ v: VERSION, a: granted ? 1 : 0 }));
    var d = new Date();
    d.setMonth(d.getMonth() + MONTHS);
    document.cookie = COOKIE + "=" + val + ";expires=" + d.toUTCString() +
                      ";path=/;SameSite=Lax" + (location.protocol === "https:" ? ";Secure" : "");
  }

  function apply(granted) {
    var state = granted ? "granted" : "denied";
    if (typeof window.gtag === "function") {
      window.gtag("consent", "update", {
        ad_storage: state,
        ad_user_data: state,
        ad_personalization: state,
        analytics_storage: state
      });
    }
  }

  // ---- apply any stored choice immediately, before tags fire ----
  var stored = read();
  if (stored) apply(stored.a === 1);

  // ---- banner ----
  var CSS =
  '#pc-banner{position:fixed;left:0;right:0;bottom:0;z-index:2147483000;background:#fff;' +
  'border-top:3px solid #2C7DA0;box-shadow:0 -4px 24px rgba(0,0,0,.14);padding:20px 24px;' +
  'font-family:"Segoe UI",system-ui,-apple-system,Roboto,Arial,sans-serif;color:#4A4A5A;' +
  'font-size:.95rem;line-height:1.55}' +
  '#pc-banner .pc-in{max-width:1100px;margin:0 auto;display:flex;gap:24px;align-items:center;flex-wrap:wrap}' +
  '#pc-banner p{margin:0;flex:1;min-width:280px}' +
  '#pc-banner strong{color:#1A1A2E;display:block;margin-bottom:4px;font-size:1rem}' +
  '#pc-banner a{color:#21607C}' +
  '#pc-banner .pc-btns{display:flex;gap:10px;flex-wrap:wrap}' +
  '#pc-banner button{font:inherit;font-weight:600;font-size:.9rem;padding:11px 24px;border-radius:6px;' +
  'cursor:pointer;border:1px solid #2C7DA0;background:#fff;color:#21607C;min-width:132px}' +
  '#pc-banner button.pc-accept{background:#2C7DA0;border-color:#2C7DA0;color:#fff}' +
  '#pc-banner button:hover{opacity:.88}' +
  '@media (max-width:640px){#pc-banner{padding:16px}#pc-banner .pc-btns{width:100%}' +
  '#pc-banner button{flex:1}}';

  function banner() {
    if (document.getElementById("pc-banner")) return;

    var s = document.createElement("style");
    s.textContent = CSS;
    document.head.appendChild(s);

    var el = document.createElement("div");
    el.id = "pc-banner";
    el.setAttribute("role", "dialog");
    el.setAttribute("aria-live", "polite");
    el.setAttribute("aria-label", "Cookie choices");
    el.innerHTML =
      '<div class="pc-in">' +
        '<p><strong>Cookies on this site</strong>' +
        'We use Google Analytics to understand how the site is used, which sets cookies on your device. ' +
        'It is not needed for the site to work, so it is off until you say otherwise. ' +
        'See our <a href="/privacy">privacy policy</a>.</p>' +
        '<div class="pc-btns">' +
          '<button type="button" class="pc-reject">Reject</button>' +
          '<button type="button" class="pc-accept">Accept</button>' +
        '</div>' +
      '</div>';
    document.body.appendChild(el);

    function choose(granted) {
      write(granted);
      apply(granted);
      el.parentNode && el.parentNode.removeChild(el);
    }
    el.querySelector(".pc-accept").addEventListener("click", function () { choose(true); });
    el.querySelector(".pc-reject").addEventListener("click", function () { choose(false); });
  }

  if (!stored) {
    if (document.readyState === "loading") {
      document.addEventListener("DOMContentLoaded", banner);
    } else {
      banner();
    }
  }

  // ---- let any page reopen the choice: <a href="#" onclick="PlannedConsent.open()"> ----
  window.PlannedConsent = {
    open: function () {
      document.cookie = COOKIE + "=;expires=Thu, 01 Jan 1970 00:00:00 GMT;path=/";
      banner();
      return false;
    },
    state: function () { var c = read(); return c ? (c.a === 1 ? "granted" : "denied") : "unset"; }
  };
})();
