(() => {
const $ = (s, r = document) => r.querySelector(s), $$ = (s, r = document) => [...r.querySelectorAll(s)];
const calm = matchMedia("(prefers-reduced-motion: reduce)").matches;
document.documentElement.classList.add("js");
const nav = $("#nav"), burger = $(".burger"), links = $("#links");
addEventListener("scroll", () => nav.toggleAttribute("data-scrolled", scrollY > 10), { passive: true });
const menu = (open) => { links.classList.toggle("open", open); burger.setAttribute("aria-expanded", open); };
burger.addEventListener("click", () => menu(!links.classList.contains("open")));
links.addEventListener("click", () => menu(false));
addEventListener("keydown", (e) => e.key === "Escape" && menu(false));
if (!calm && "IntersectionObserver" in window) {
const io = new IntersectionObserver((es) => es.forEach((e) => { if (e.isIntersecting) { e.target.classList.remove("wait"); io.unobserve(e.target); } }), { rootMargin: "0px 0px -8% 0px" });
const h = innerHeight;
$$(".reveal").filter((el) => el.getBoundingClientRect().top > h).forEach((el) => { el.classList.add("wait"); io.observe(el); });
}
if (!calm) {
const words = $$(".swap em"); let w = 0;
setInterval(() => { if (document.hidden) return; words[w].classList.remove("on"); w = (w + 1) % words.length; words[w].classList.add("on"); }, 2800);
$$("[data-count]").forEach((el) => { const end = +el.dataset.count; let t0;
const step = (t) => { t0 ??= t; const p = Math.min((t - t0) / 1200, 1); el.textContent = Math.round(end * p).toLocaleString("fa-IR"); if (p < 1) requestAnimationFrame(step); };
requestAnimationFrame(step); });
$$(".product,.plugin").forEach((c) => c.addEventListener("pointermove", (e) => { const r = c.getBoundingClientRect(); c.style.setProperty("--mx", e.clientX - r.left + "px"); c.style.setProperty("--my", e.clientY - r.top + "px"); }, { passive: true }));
}
const bubble = $("#bubble"), chips = $$("[data-sms]"); let timer, cur = 0;
const show = (i) => { cur = i; chips.forEach((c, k) => c.setAttribute("aria-pressed", k === i)); bubble.textContent = chips[i].dataset.sms; bubble.classList.remove("new"); void bubble.offsetWidth; bubble.classList.add("new"); };
chips.forEach((c, i) => c.addEventListener("click", () => { clearInterval(timer); show(i); }));
if (!calm) timer = setInterval(() => { if (!document.hidden) show((cur + 1) % chips.length); }, 3500);
$$("[data-product]").forEach((a) => a.addEventListener("click", () => { $("#f-product").value = a.dataset.product; }));
if (document.documentElement.classList.contains("preview"))
$$('a[href^="#"]').forEach((a) => a.addEventListener("click", (e) => { const t = $(a.getAttribute("href")); if (t) { e.preventDefault(); t.scrollIntoView(); } }));
const form = $("#form"), status = $("#status");
const say = (m, err) => { status.textContent = m; status.toggleAttribute("data-error", !!err); };
form.addEventListener("submit", async (e) => {
e.preventDefault();
const d = Object.fromEntries(new FormData(form));
d.phone = d.phone.replace(/[۰-۹]/g, (c) => c.charCodeAt(0) - 1776).replace(/[٠-٩]/g, (c) => c.charCodeAt(0) - 1632).replace(/[\s-]/g, "");
if (d.name.trim().length < 2) { $("#f-name").focus(); return say("نام خود را وارد کنید.", true); }
if (!/^(\+98|0098|0)9\d{9}$/.test(d.phone)) { $("#f-phone").focus(); return say("شمارهٔ موبایل را مانند 09123456789 وارد کنید.", true); }
if (document.documentElement.classList.contains("preview")) return say("این پیش‌نمایش است و درخواستی ارسال نشد.", true);
const btn = $("button[type=submit]", form); btn.disabled = true; say("در حال ارسال…");
try {
const r = await fetch("/api/contact", { method: "POST", headers: { "content-type": "application/json" }, body: JSON.stringify(d) });
if (!r.ok) throw new Error(r.status);
form.reset(); say("درخواست شما ثبت شد.");
} catch { say("ارسال انجام نشد. اتصال را بررسی کنید و دوباره بزنید.", true); }
finally { btn.disabled = false; }
});
})();