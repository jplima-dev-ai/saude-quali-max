(function () {
  "use strict";

  var ROOT = window.location.pathname.includes("/products/") ? "../" : "./";
  var ACK_KEY = "qualimax-privacy-notice-v363";

  function safeText(value, fallback) {
    return String(value == null ? fallback || "" : value).replace(/[\u0000-\u001f\u007f]/g, " ").trim().slice(0, 500);
  }

  async function config() {
    if (window.QualimaxConfig) return window.QualimaxConfig;
    try {
      var response = await fetch(ROOT + "data/config.json", { cache: "no-cache" });
      return response.ok ? response.json() : {};
    } catch (_) { return {}; }
  }

  function policyPath() {
    return ROOT + "privacy.html";
  }

  function populate(cfg) {
    var privacy = cfg.privacidade || {};
    var company = cfg.empresa || {};
    var contact = cfg.contato || {};
    var values = {
      nomeLoja: company.nome || "a loja",
      razaoSocial: privacy.razaoSocial || company.nome || "Preencha a razão social",
      cnpj: privacy.cnpj || "Preencha o CNPJ ou CPF do controlador",
      endereco: privacy.enderecoControlador || contact.endereco || "Preencha o endereço do controlador",
      emailPrivacidade: privacy.emailPrivacidade || contact.email || "Preencha o canal de privacidade",
      encarregado: privacy.encarregado || "Canal de privacidade da loja",
      atualizadaEm: privacy.atualizadaEm || "22 de agosto de 2026"
    };
    Object.keys(values).forEach(function (key) {
      document.querySelectorAll("[data-privacy-" + key.replace(/[A-Z]/g, function (x) { return "-" + x.toLowerCase(); }) + "]").forEach(function (el) {
        el.textContent = safeText(values[key]);
        if (el.tagName === "A" && key === "emailPrivacidade" && /^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(values[key])) el.href = "mailto:" + values[key];
      });
    });
  }

  function banner(cfg) {
    var privacy = cfg.privacidade || {};
    if (privacy.avisoAtivo === false || document.body.dataset.page === "privacy") return;
    try { if (localStorage.getItem(ACK_KEY) === "ok") return; } catch (_) {}
    var region = document.createElement("aside");
    region.className = "privacy-v363-banner";
    region.setAttribute("aria-labelledby", "privacy-v363-banner-title");
    region.innerHTML = '<div><strong id="privacy-v363-banner-title">Sua privacidade, sem letras miúdas</strong><p>Este site guarda preferências e listas neste aparelho. Ao abrir o WhatsApp ou consultar um CEP, os dados passam a ser tratados pelos respectivos serviços.</p></div><div class="privacy-v363-banner-actions"><a class="botao botao-secundario" href="' + policyPath() + '">Ler a política</a><button class="botao botao-principal" type="button" data-privacy-ack>Entendi</button></div>';
    document.body.append(region);
    region.querySelector("[data-privacy-ack]").addEventListener("click", function () {
      try { localStorage.setItem(ACK_KEY, "ok"); } catch (_) {}
      region.remove();
    });
  }

  function describeExternalTransfers() {
    var note = document.createElement("p");
    note.id = "privacy-v363-external-note";
    note.className = "sr-only";
    note.textContent = "Este link abre um serviço externo, que tratará os dados enviados conforme a própria política de privacidade.";
    document.body.append(note);
    document.querySelectorAll('a[href*="wa.me"], a[href*="whatsapp"], [data-configurable-whatsapp], [data-produto-whatsapp]').forEach(function (link) {
      var current = (link.getAttribute("aria-describedby") || "").split(/\s+/).filter(Boolean);
      if (!current.includes(note.id)) current.push(note.id);
      link.setAttribute("aria-describedby", current.join(" "));
    });
  }

  async function init() {
    var cfg = await config();
    populate(cfg);
    describeExternalTransfers();
    banner(cfg);
  }

  if (document.readyState === "loading") document.addEventListener("DOMContentLoaded", init, { once: true });
  else init();
}());
