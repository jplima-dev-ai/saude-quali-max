const fs = require("node:fs");
const path = require("node:path");
const { test, expect } = require("@playwright/test");

const root = path.resolve(__dirname, "../..");
const routes = [
  ...fs.readdirSync(root).filter((name) => name.endsWith(".html")),
  ...fs
    .readdirSync(path.join(root, "products"))
    .filter((name) => name.endsWith(".html"))
    .map((name) => `products/${name}`),
].sort();

test("as 81 páginas públicas respondem com HTML", async ({ request }) => {
  expect(routes).toHaveLength(81);
  for (const route of routes) {
    const response = await request.get(`/${route}`);
    expect(response.ok(), route).toBeTruthy();
    expect(response.headers()["content-type"], route).toContain("text/html");
  }
});

test("menu móvel abre por teclado e devolve o foco com Escape", async ({ page }) => {
  await page.setViewportSize({ width: 375, height: 667 });
  await page.goto("/index.html");
  const button = page.locator(".botao-menu");
  await button.focus();
  await page.keyboard.press("Enter");
  await expect(button).toHaveAttribute("aria-expanded", "true");
  await expect(page.locator(".navegacao a").first()).toBeFocused();
  await page.keyboard.press("Escape");
  await expect(button).toHaveAttribute("aria-expanded", "false");
  await expect(button).toBeFocused();
});

test("preferências de acessibilidade persistem depois da recarga", async ({ page }) => {
  await page.goto("/index.html");
  await page.locator("[data-acessibilidade-toggle]").click();
  await page.locator("[data-alto-contraste]").click();
  await page.locator("[data-reduzir-movimento]").click();
  await page.reload();
  await expect(page.locator("html")).toHaveClass(/alto-contraste/);
  await expect(page.locator("html")).toHaveClass(/movimento-reduzido/);
  await expect(page.locator("[data-alto-contraste]")).toHaveAttribute("aria-pressed", "true");
});

test("manifesto e service worker ficam ativos", async ({ page, request }) => {
  const manifest = await request.get("/manifest.webmanifest");
  expect(manifest.ok()).toBeTruthy();
  const data = await manifest.json();
  expect(data.name).toBeTruthy();
  expect(data.start_url).toBeTruthy();
  await page.goto("/index.html");
  await page.evaluate(() => navigator.serviceWorker.ready);
  await page.reload();
  await expect
    .poll(() => page.evaluate(() => Boolean(navigator.serviceWorker.controller)))
    .toBeTruthy();
});

test("navegação sem rede apresenta a página offline", async ({ page, context }) => {
  await page.goto("/index.html");
  await page.evaluate(() => navigator.serviceWorker.ready);
  await page.reload();
  await expect
    .poll(() => page.evaluate(() => Boolean(navigator.serviceWorker.controller)))
    .toBeTruthy();
  await expect
    .poll(() =>
      page.evaluate(async () => {
        const registration = await navigator.serviceWorker.ready;
        const offlineUrl = new URL("offline.html", registration.scope).href;
        return Boolean(await caches.match(offlineUrl, { ignoreSearch: true }));
      }),
    )
    .toBeTruthy();
  await context.setOffline(true);
  try {
    await page.goto("/rota-indisponivel-no-cache.html");
    await expect(page.locator("h1")).toContainText("A internet deu uma pausa");
  } finally {
    await context.setOffline(false);
  }
});

test("jornadas principais não geram erros no console", async ({ page }) => {
  const errors = [];
  page.on("console", (message) => {
    if (message.type() === "error") errors.push(message.text());
  });
  for (const route of [
    "index.html",
    "catalog.html",
    "cart.html",
    "wellness-hub.html",
    "admin.html",
  ]) {
    await page.goto(`/${route}`);
  }
  expect(errors).toEqual([]);
});
