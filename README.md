# لندینگ پشتوان (Poshtone) — Cloudflare Pages

## انتشار
1. `npx wrangler kv namespace create LEADS`
2. سه خط `kv_namespaces` در `wrangler.toml` را فعال کنید و id را بگذارید.
3. در همین پوشه: `npx wrangler pages deploy`

انتشار با کشیدن پوشهٔ `dist` در داشبورد فقط صفحه را بالا می‌برد و فرم کار نمی‌کند.

## دیدن درخواست‌ها
داشبورد Cloudflare ← KV ← LEADS (کلیدها با `lead:` شروع می‌شوند).

## تغییر محتوا
فایل `dist/index.html` را مستقیم ویرایش کنید.

## منابع
کامپوننت‌ها و آیکون‌ها: Kashi UI (MIT) · فونت: Vazirmatn (OFL)

> پوشهٔ `src` فقط برای ساخت دوباره است. اگر `dist` را دستی ویرایش می‌کنید، `build.mjs` را دوباره اجرا نکنید چون تغییرها را بازنویسی می‌کند.

## ساخت دوباره از `src`
مخزن Kashi را کلون و پکیج‌های tokens و icons را بسازید، سپس:
`python3 src/gen.py && KASHI_DIR=/path/to/kashi node src/build.mjs`
