// ساخت خروجی: node src/build.mjs  →  dist/ (برای Cloudflare Pages)
import { readFileSync as R, writeFileSync as W, mkdirSync, copyFileSync } from "node:fs";
const K = (process.env.KASHI_DIR || "../kashi") + "/packages";
const { iconSvg } = await import((await import("node:path")).resolve(K, "icons/dist/index.js"));
const here = new URL(".", import.meta.url).pathname, out = here + "../dist/";
mkdirSync(out + "assets", { recursive: true });

const icon = (name, size = 24, variant = "bulk") => {
  const s = iconSvg(name, { size, variant, idPrefix: "i" + (n++) });
  if (!s) throw new Error("icon " + name);
  return s;
};
let n = 0;
let html = R(here + "index.html", "utf8")
  .replace(/\{\{i:([\w-]+)(?::(\d+))?(?::([\w-]+))?\}\}/g, (_, a, b, c) => icon(a, +(b || 24), c || "bulk"));

const comps = ["button", "card", "badge", "navbar", "accordion", "input", "tabs", "chip", "alert"];
const base = R(K + "/css/src/base.css", "utf8");
const kashi = "@layer kashi.tokens, kashi.base, kashi.components;\n" +
  `@layer kashi.tokens{\n${R(K + "/tokens/dist/tokens.css", "utf8")}\n}\n@layer kashi.base{\n${base}\n}\n` +
  `@layer kashi.components{\n${comps.map((c) => R(`${K}/css/src/components/${c}.css`, "utf8")).join("\n")}\n}\n`;

W(out + "index.html", html);
W(out + "assets/kashi.css", "/* Kashi UI — MIT — github.com/Sepantapouya/Kashi */\n" + kashi);
copyFileSync(here + "site.css", out + "assets/site.css");
copyFileSync(here + "main.js", out + "assets/main.js");
copyFileSync(here + "Vazirmatn.woff2", out + "assets/Vazirmatn.woff2");
copyFileSync(here + "Vazirmatn-OFL.txt", out + "assets/Vazirmatn-OFL.txt");
copyFileSync(K + "/css/LICENSE", out + "assets/Kashi-LICENSE.txt");

// نسخهٔ تک‌فایل برای پیش‌نمایش
const b64 = (f) => R(here + f).toString("base64");
const css = (kashi + R(here + "site.css", "utf8")).replace('url("./Vazirmatn.woff2")', `url("data:font/woff2;base64,${b64("Vazirmatn.woff2")}")`);
const body = html.split("<!--BODY-->")[1].split("<!--/BODY-->")[0];
W(here + "../preview.html", `<title>پشتوان</title>
<style>${css}</style>
<script>for(const [k,v] of [["lang","fa"],["dir","rtl"],["data-theme","dark"]])document.documentElement.setAttribute(k,v);document.documentElement.classList.add("js","preview")</script>
${body}
<script>${R(here + "main.js", "utf8")}</script>
`);
console.log("ok");
