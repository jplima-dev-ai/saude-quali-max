(function () {
  "use strict";

  var root = document.documentElement;
  var frame = 0;
  var baselineHeight = window.innerHeight;

  function viewport() {
    return window.visualViewport || { width: window.innerWidth, height: window.innerHeight };
  }

  function classify(width) {
    if (width <= 390) return "compact";
    if (width <= 767) return "phone";
    if (width <= 1180) return "tablet";
    return "wide";
  }

  function markHorizontalRegions() {
    document.querySelectorAll("table, pre, .v340-compare, .admin-tabela-wrap").forEach(function (element) {
      var region = element.matches("table, pre") ? element.parentElement : element;
      if (!region) return;
      if (element.scrollWidth > region.clientWidth + 2) region.classList.add("v362-horizontal-scroll");
    });
  }

  function update() {
    var current = viewport();
    var width = Math.max(0, Math.round(current.width));
    var height = Math.max(0, Math.round(current.height));
    root.style.setProperty("--v362-vw", width + "px");
    root.style.setProperty("--v362-vh", height + "px");
    root.dataset.v362Layout = classify(width);
    root.dataset.v362Orientation = width > height ? "landscape" : "portrait";

    var active = document.activeElement;
    var editable = active && /^(INPUT|TEXTAREA|SELECT)$/.test(active.tagName);
    root.dataset.v362Keyboard = editable && baselineHeight - height > 140 ? "open" : "closed";
    markHorizontalRegions();
  }

  function schedule() {
    window.cancelAnimationFrame(frame);
    frame = window.requestAnimationFrame(update);
  }

  function init() {
    root.classList.add("v362-ready");
    update();
    window.addEventListener("resize", schedule, { passive: true });
    window.addEventListener("orientationchange", function () {
      baselineHeight = window.innerHeight;
      schedule();
    }, { passive: true });
    window.addEventListener("pageshow", schedule, { passive: true });
    document.addEventListener("focusin", schedule);
    document.addEventListener("focusout", schedule);
    if (window.visualViewport) {
      window.visualViewport.addEventListener("resize", schedule, { passive: true });
      window.visualViewport.addEventListener("scroll", schedule, { passive: true });
    }
    if ("ResizeObserver" in window) new ResizeObserver(schedule).observe(document.body);
  }

  if (document.readyState === "loading") document.addEventListener("DOMContentLoaded", init, { once: true });
  else init();
}());
