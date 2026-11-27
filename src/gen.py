# تولید src/index.html از داده‌های محصولات
def li(items): return "".join(f"<li>{{{{i:check:18:light}}}}<span>{x}</span></li>" for x in items)
SITES = {"حساب‌یار":"hesabyiar.ir","پیمان":"hesabyiar.ir","هما اس‌ام‌اس":"homasms.ir","منوتم":"menutam.ir"}
def demo_btn(name):
    if name in SITES:
        d = SITES[name]
        return f'<a class="k-btn k-btn--primary k-btn--sm site" href="https://{d}" target="_blank" rel="noopener" aria-label="ورود به سایت {name} (در زبانهٔ تازه)">ورود به سایت <bdi dir="ltr">{d}</bdi> {{{{i:arrow-up-left:16:light}}}}</a>'
    return f'<a class="k-btn k-btn--secondary k-btn--sm" href="#contact" data-product="{name}">درخواست دمو {{{{i:arrow-left:16:light}}}}</a>'

# ---------- تصویرهای متحرک محصولات ----------
erp = '<div class="v v-erp">' + "".join(f'<span style="--d:{i}">{{{{i:{ic}:26}}}}<b>{t}</b></span>' for i,(ic,t) in enumerate([("calculator","مالی"),("store","فروش"),("package","انبار"),("building-factory","تولید"),("users","منابع انسانی"),("chart-bar","گزارش‌ها")])) + '</div>'
hes = '<div class="v v-ledger"><div class="row head"><b>شرح سند</b><b>بدهکار</b><b>بستانکار</b></div>' + "".join(f'<div class="row" style="--d:{i}"><i style="--w:{w}%"></i><i class="a" style="--w:{a}%"></i><i class="b" style="--w:{b}%"></i></div>' for i,(w,a,b) in enumerate([(80,70,0),(65,0,70),(90,55,0),(55,0,55)])) + '<div class="stamp">{{i:check:16:light}} سند تراز است</div></div>'
pay = '<div class="v v-pay"><div class="track">' + "".join(f'<span style="--d:{i}">{n}</span>' for i,n in enumerate("۱۲۳۴۵۶")) + '</div><div class="toast">{{i:bell:20}}<div><b>یادآوری قسط</b><small>سررسید قسط شما نزدیک است</small></div></div></div>'
rav = '<div class="v v-att"><div class="finger">{{i:fingerprint:72:light}}<em></em></div><ul><li style="--d:0"><b>ورود</b><span>۰۸:۰۰</span></li><li style="--d:1"><b>مأموریت</b><span>۱۱:۳۰</span></li><li style="--d:2"><b>خروج</b><span>۱۷:۰۰</span></li></ul></div>'
crm = '<div class="v v-crm">' + "".join(f'<div class="col"><b>{t}</b><i></i>{"<i></i>" if k<2 else ""}</div>' for k,t in enumerate(["سرنخ","مذاکره","فروش"])) + '<div class="mover">{{i:user:16}}<span></span></div></div>'
men = '<div class="v v-menu"><div class="phone"><div class="title">{{i:coffee:18}} منوی کافه</div>' + "".join(f'<div class="item" style="--d:{i}"><i></i><span>{t}</span></div>' for i,t in enumerate(["اسپرسو","لاته","کیک روز"])) + '</div><div class="qr">{{i:qr-code:64:light}}<em></em></div></div>'

products = [
 ("erp","wide","buildings","ERP سازمانی پشتوان","سامانهٔ یکپارچه برای شرکت‌های بزرگ",
  "مالی، فروش، انبار، تولید و منابع انسانی روی یک پایگاه داده کار می‌کنند. اطلاعات یک بار ثبت می‌شود و همهٔ واحدها همان را می‌بینند.",
  ["ماژول‌های هماهنگ با گردش کار سازمان","سطح دسترسی جدا برای هر نقش","داشبورد و گزارش مدیریتی از کل مجموعه"], erp),
 ("hesabyar","","calculator","حساب‌یار","نرم‌افزار حسابداری بازرگانی و تولیدی",
  "حسابداری ویندوز با رابط فارسی و راست‌چین، ساخته‌شده برای کسب‌وکارهای بازرگانی و تولیدی.",
  ["اسناد حسابداری، خرید، فروش و انبار","پایگاه دادهٔ محلی SQLite","سبک و سریع، نوشته‌شده با Rust"], hes),
 ("payman","","calendar-check","پیمان","مدیریت فروش اقساطی",
  "فروش اقساطی را از فاکتور تا تسویه دنبال کنید و سررسیدها را پیش از دیر شدن ببینید.",
  ["فهرست اقساط سررسیدشده و پیش‌رو","مدیریت چک اقساط و چک ضمانت","یادآوری پیامکی و پروندهٔ کامل مشتری"], pay),
 ("ravand","","fingerprint","روند","نرم‌افزار حضور و غیاب",
  "ورود و خروج کارکنان را منظم ثبت کنید و کارکرد ماهانه را بدون محاسبهٔ دستی تحویل حسابداری بدهید.",
  ["تعریف شیفت و تقویم کاری","درخواست مرخصی و مأموریت","گزارش کارکرد، تأخیر و اضافه‌کار"], rav),
 ("crm","","users","CRM پشتوان","مدیریت ارتباط با مشتریان",
  "هیچ تماس و پیگیری‌ای گم نمی‌شود. تیم فروش می‌داند هر مشتری در کدام مرحله است و قدم بعدی چیست.",
  ["قیف فروش و مراحل پیگیری","تاریخچهٔ تماس‌ها و یادداشت‌ها","یادآور کارها و گزارش عملکرد تیم"], crm),
 ("menutam","wide","coffee","منوتم","منوساز دیجیتال کافه",
  "منوی کافه را خودتان بسازید و هر وقت خواستید تغییر دهید. مشتری با اسکن کد QR منوی به‌روز را روی گوشی می‌بیند.",
  ["دسته‌بندی، عکس، توضیح و قیمت هر محصول","تغییر قیمت بدون چاپ دوباره","اطلاعات کافه و شبکه‌های اجتماعی در یک صفحه"], men),
]
cards = ""
for pid,cls,ic,name,sub,desc,feats,vis in products:
    cards += f'''<article class="k-card product reveal {cls}" id="p-{pid}">
<div class="text"><div class="phead"><span class="tile">{{{{i:{ic}:28}}}}</span><div><h3>{name}</h3><p class="sub">{sub}</p></div></div>
<p>{desc}</p><ul class="checks">{li(feats)}</ul>{demo_btn(name)}</div>
<div class="visual" aria-hidden="true">{vis}</div></article>'''

orbit_items = [("buildings","ERP","p-erp",1),("calculator","حساب‌یار","p-hesabyar",1),("calendar-check","پیمان","p-payman",1),("fingerprint","روند","p-ravand",1),("users","CRM","p-crm",1),("coffee","منوتم","p-menutam",1),("shield-check","مرزگارد","p-marzgard",2),("wallet","Payto","p-payto",2),("chat","هما","homa",2)]
import math
orbit = ""; lines = ""
for i,(ic,t,href,ring) in enumerate(orbit_items):
    a = math.radians(-90 + i*40); r = 41
    x = 50 + r*math.cos(a); y = 50 + r*math.sin(a)
    orbit += f'<a class="node g{ring}" href="#{href}" style="--x:{x:.2f}%;--y:{y:.2f}%;--d:{i}"><span>{{{{i:{ic}:26}}}}</span><b>{t}</b></a>'
    lines += f'<path d="M50 50L{x:.2f} {y:.2f}"/><path class="pulse" style="--d:{i}" pathLength="100" d="M{x:.2f} {y:.2f}L50 50"/>'

logo = '<svg class="logo" viewBox="0 0 40 40" aria-hidden="true"><rect width="40" height="40" rx="11" fill="#1f30d9"/><path d="M9 29h22M12.5 23.5h15" stroke="#fff" stroke-width="3" stroke-linecap="round"/><path d="M20 7l7 7-7 7-7-7z" fill="#8ff0e4"/></svg>'

names = ["ERP سازمانی","حساب‌یار","پیمان","روند","CRM","منوتم","مرزگارد","Payto","هما اس‌ام‌اس"]
marq = "".join(f"<span>{x}</span>" for x in names)

bars = "".join(f'<span><i style="--h:{a}%;--d:{i}"></i><i class="o" style="--h:{b}%;--d:{i}"></i></span>' for i,(a,b) in enumerate([(45,30),(60,38),(52,44),(75,40),(68,50),(90,46)]))

faq = [("پشتوان چه محصولاتی دارد؟","شش نرم‌افزار (ERP سازمانی، حساب‌یار، پیمان، روند، CRM و منوتم)، دو افزونهٔ وردپرس (مرزگارد و Payto) و پنل پیامکی هما اس‌ام‌اس."),
 ("کدام محصول برای کسب‌وکار من مناسب است؟","برای سازمان چندواحدی ERP، برای بازرگانی و تولیدی حساب‌یار، برای فروش قسطی پیمان و برای کافه منوتم را ببینید. اگر مطمئن نیستید، در فرم تماس کارتان را توضیح دهید."),
 ("می‌توانم قبل از خرید دمو ببینم؟","حساب‌یار، پیمان، منوتم و هما اس‌ام‌اس از دکمهٔ «ورود به سایت» در دسترس‌اند. برای بقیهٔ محصولات «درخواست دمو» را بزنید."),
 ("افزونه‌ها روی چه سایتی نصب می‌شوند؟","مرزگارد و Payto افزونهٔ وردپرس هستند و روی سایت وردپرسی شما نصب می‌شوند.")]
faqh = "".join(f'<details class="k-accordion__item" name="faq"{" open" if i==0 else ""}><summary class="k-accordion__trigger">{q}</summary><div class="k-accordion__content">{a}</div></details>' for i,(q,a) in enumerate(faq))
options = "".join(f"<option>{x}</option>" for x in ["مشاوره / نمی‌دانم","ERP سازمانی پشتوان","حساب‌یار","پیمان","روند","CRM پشتوان","منوتم","مرزگارد","Payto","هما اس‌ام‌اس","ساخت نرم‌افزار سفارشی"])

t = open(__file__.replace("gen.py","template.html"),encoding="utf-8").read()
for k,v in dict(LOGO=logo,CARDS=cards,ORBIT=orbit,LINES=lines,MARQ=marq,FAQ=faqh,BARS=bars,OPTIONS=options).items():
    t = t.replace("%"+k+"%", v)
t = t.replace("%HOMA_BTN%", demo_btn("هما اس‌ام‌اس")).replace("%MG_BTN%", demo_btn("مرزگارد")).replace("%PT_BTN%", demo_btn("Payto"))
open(__file__.replace("gen.py","index.html"),"w",encoding="utf-8").write(t)
