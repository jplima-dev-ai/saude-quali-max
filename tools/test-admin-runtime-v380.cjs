const fs = require("node:fs");
const vm = require("node:vm");

const document = {
  addEventListener() {},
  querySelector() { return null; },
  querySelectorAll() { return []; },
};
const context = {
  window: { addEventListener() {} },
  document,
  indexedDB: {},
  console,
  Blob,
  URL,
  setTimeout,
  clearTimeout,
  structuredClone,
  confirm: () => true,
};
context.window.window = context.window;
vm.createContext(context);
vm.runInContext(fs.readFileSync("assets/scripts/admin.js", "utf8"), context, {
  filename: "assets/scripts/admin.js",
});

if (typeof context.window.QualimaxAdminAPI?.auditar !== "function") {
  throw new Error("QualimaxAdminAPI.auditar não foi inicializada.");
}
console.log("ADMIN_RUNTIME_V380_OK");
