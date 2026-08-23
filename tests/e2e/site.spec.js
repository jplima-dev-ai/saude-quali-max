const { test, expect } = require("@playwright/test");
const AxeBuilder = require("@axe-core/playwright").default;

const coreRoutes = [
  "index.html",
  "catalog.html",
  "cart.html",
  "wellness-hub.html",
  "admin.html",
  "privacy.html",
];

for (const route of coreRoutes) {
  test(`${route} carrega sem erro e sem overflow horizontal`, async ({ page }) => {
    const response = await page.goto(`/${route}`);
    expect(response?.ok()).toBeTruthy();
    await expect(page.locator("main")).toHaveCount(1);
    const overflow = await page.evaluate(
      () => document.documentElement.scrollWidth > document.documentElement.clientWidth + 1,
    );
    expect(overflow).toBeFalsy();
  });
}

test("atalho de conteúdo recebe foco", async ({ page }) => {
  await page.goto("/index.html");
  await page.keyboard.press("Tab");
  await expect(page.locator(".skip-link")).toBeFocused();
  await page.keyboard.press("Enter");
  await expect(page.locator("main")).toBeFocused();
});

test("Max abre por teclado, fecha e devolve o foco", async ({ page }) => {
  await page.goto("/index.html");
  const opener = page.locator(".chatbot-abrir");
  await opener.focus();
  await page.keyboard.press("Enter");
  const dialog = page.locator('[data-chatbot] [role="dialog"]');
  await expect(dialog).toBeVisible();
  await expect(page.locator("[data-chat-fechar]")).toBeFocused();
  await page.keyboard.press("Escape");
  await expect(dialog).toBeHidden();
  await expect(opener).toBeFocused();
});

for (const route of coreRoutes) {
  test(`${route} sem violações Axe sérias ou críticas`, async ({ page }) => {
    await page.emulateMedia({ reducedMotion: "reduce" });
    await page.goto(`/${route}`, { waitUntil: "networkidle" });
    const result = await new AxeBuilder({ page })
      .withTags(["wcag2a", "wcag2aa", "wcag21a", "wcag21aa"])
      .analyze();
    const blockers = result.violations.filter((item) =>
      ["serious", "critical"].includes(item.impact),
    );
    if (blockers.length) {
      const resumo = blockers.map((item) => ({
        id: item.id,
        impact: item.impact,
        nodes: item.nodes.map((node) => ({
          target: node.target,
          failure: node.failureSummary,
        })),
      }));
      console.error(`AXE ${route}: ${JSON.stringify(resumo)}`);
    }
    expect(blockers).toEqual([]);
  });
}

test("carrinho demonstrativo mantém anúncio e controles acessíveis", async ({ page }) => {
  await page.goto("/catalog.html");
  const add = page.locator("[data-v333-add]").first();
  await expect(add).toBeEnabled();
  await add.click();
  await page.goto("/cart.html");
  await expect(page.locator("[data-cart-list] article")).toHaveCount(1);
  await expect(page.locator('[aria-label^="Aumentar quantidade"]')).toBeVisible();
  await expect(page.locator("[data-cart-summary]")).toContainText("Total estimado");
});
