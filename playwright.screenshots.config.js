const { defineConfig } = require("@playwright/test");

module.exports = defineConfig({
  testDir: "./tests/visual",
  workers: 1,
  reporter: "list",
  use: {
    baseURL: "http://127.0.0.1:4173",
    colorScheme: "light",
    reducedMotion: "reduce",
  },
  webServer: {
    command: "python tools/serve.py --port 4173",
    url: "http://127.0.0.1:4173/index.html",
    reuseExistingServer: true,
  },
});
