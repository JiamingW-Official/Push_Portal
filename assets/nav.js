/* ============================================================
   Push Portal — unified nav behavior
   - toggleLang: 中/EN switcher w/ localStorage persistence
   - More ▾ dropdown
   - Mobile burger menu
   Safe to load on every page.
   ============================================================ */

// Language toggle — global so inline onclick= still works
window.toggleLang = function () {
  const html = document.documentElement;
  const next = html.lang === "zh" ? "en" : "zh";
  html.lang = next;
  document.querySelectorAll("[data-en][data-zh]").forEach((el) => {
    el.textContent = el.getAttribute("data-" + next);
  });
  try {
    localStorage.setItem("push-lang", next);
  } catch (_) {}
};

// Restore saved lang on load
(function () {
  try {
    const saved = localStorage.getItem("push-lang");
    if (saved === "zh" && document.documentElement.lang !== "zh") {
      window.toggleLang();
    }
  } catch (_) {}
})();

document.addEventListener("DOMContentLoaded", function () {
  // Lang button: bind explicit listener (more reliable than inline onclick for automation)
  const langBtn = document.querySelector(".site-nav .nav-lang");
  if (langBtn) {
    langBtn.addEventListener("click", function (e) {
      e.preventDefault();
      window.toggleLang();
    });
  }

  // More ▾ dropdown
  const more = document.querySelector(".site-nav .nav-more");
  if (more) {
    const btn = more.querySelector(".nav-more-btn");
    if (btn) {
      btn.addEventListener("click", function (e) {
        e.stopPropagation();
        const open = more.getAttribute("data-open") === "true";
        more.setAttribute("data-open", String(!open));
        btn.setAttribute("aria-expanded", String(!open));
      });
      document.addEventListener("click", function () {
        more.setAttribute("data-open", "false");
        btn.setAttribute("aria-expanded", "false");
      });
      // Don't close when clicking inside the panel
      const panel = more.querySelector(".nav-more-panel");
      if (panel) {
        panel.addEventListener("click", function (e) {
          e.stopPropagation();
        });
      }
    }
  }

  // Mobile burger
  const nav = document.querySelector(".site-nav");
  const burger = nav ? nav.querySelector(".nav-burger") : null;
  if (burger && nav) {
    burger.addEventListener("click", function () {
      const open = nav.getAttribute("data-menu-open") === "true";
      nav.setAttribute("data-menu-open", String(!open));
      burger.setAttribute("aria-expanded", String(!open));
    });
  }

  // Inject Darky Giant Wordmark into footer (v11) — decorative, aria-hidden
  const footer = document.querySelector(".site-footer");
  if (footer && !footer.querySelector(".footer-wordmark")) {
    const wm = document.createElement("div");
    wm.className = "footer-wordmark";
    wm.setAttribute("aria-hidden", "true");
    wm.textContent = "PUSH";
    footer.appendChild(wm);
  }
});
