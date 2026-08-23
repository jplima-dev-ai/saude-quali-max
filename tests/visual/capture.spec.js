const path = require("node:path");
const { test, expect } = require("@playwright/test");

const output = path.resolve(__dirname, "../../docs/assets/screenshots");

const captures = [
  ["home-desktop", "index.html", { width: 1440, height: 1000 }],
  ["catalog-desktop", "catalog.html", { width: 1440, height: 1000 }],
  ["wellness-desktop", "wellness-hub.html", { width: 1440, height: 1000 }],
  ["admin-desktop", "admin.html", { width: 1440, height: 1000 }],
  ["home-mobile", "index.html", { width: 390, height: 844 }],
];

for (const [name, route, viewport] of captures) {
  test(`captura ${name}`, async ({ page }) => {
    await page.setViewportSize(viewport);
    await page.goto(`/${route}`);
    await page.emulateMedia({ reducedMotion: "reduce" });
    await expect(page.locator("main")).toBeVisible();
    await page.screenshot({ path: path.join(output, `${name}.png`), fullPage: true });
  });
}
