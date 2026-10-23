# Сборка CV (RU/EN) в PDF: python3 cv/build.py
import base64, io, os
from PIL import Image
from playwright.sync_api import sync_playwright

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SITE = 'portfolio-two-steel-37.vercel.app'

def photo_b64():
    im = Image.open(os.path.join(ROOT, 'assets/photo.webp')).convert('RGBA')
    # кадр с лицом (правая часть фото), ч/б на светлом фоне
    w, h = im.size
    im = im.crop((int(w * .60), int(h * .14), int(w * .92), int(h * .62)))
    bg = Image.new('RGBA', im.size, (16, 16, 16, 255)); bg.alpha_composite(im)
    bg = bg.convert('L').resize((360, int(360 * bg.height / bg.width)))
    b = io.BytesIO(); bg.save(b, 'JPEG', quality=85); return base64.b64encode(b.getvalue()).decode()

def noise_b64():
    b = open(os.path.join(ROOT, 'assets/noise.png'), 'rb').read(); return base64.b64encode(b).decode()

RU = dict(
    lang='ru', file='Korotkevich_Nadezhda_CV_RU.pdf',
    name='Короткевич Надежда', role='Графический дизайн → Веб-дизайн → UI/UX → Иллюстрации → AI',
    about_t='Обо мне',
    about=['Дизайнер и иллюстратор. 17+ лет в профессии, 300+ реализованных проектов — от стартапов до международных компаний.',
           'Работаю на стыке системного мышления и визуальной выразительности: проектирую интерфейсы, создаю визуал для брендов, рисую иллюстрации. Для меня важно, чтобы дизайн был не просто красивым, а понятным и практичным.'],
    exp_t='Опыт',
    exp=[('LuckyGroup', 'RU', 'Декабрь 2024 — Май 2026', 'Дизайн сайтов и лендингов, верстка в Tilda. Айдентика, брендинг, логотипы. Полиграфия, презентации, соцсети. Дизайн выставочных стендов и сопровождение конференций. Иллюстрации, ретушь, работа с нейросетями.'),
         ('МойСклад', 'RU', 'Март 2024 — Декабрь 2024', 'Работа над порталом, участие в исследованиях, дизайн лендингов. Новая дизайн-концепция, соцсети, полиграфия, мерч, выставочные стенды, презентации.'),
         ('EFKO', 'RU', 'Январь 2023 — Март 2024', 'Проектная работа с одной из крупнейших продовольственных компаний России: дизайн-концепт подписного журнала для шеф-поваров и меню для нескольких ресторанов, все иллюстрации, подготовка к печати.'),
         ('Ants Games', 'UAE', 'Март 2022 — Декабрь 2022', 'Игровые интерфейсы, персонажи, фоны и элементы UI. Соцсети и рекламные материалы.'),
         ('EmiDAO', 'UAE', '2021 — 2022', 'Дизайн веб-сайтов и лендингов. Концепты и иллюстрации для NFT-проекта, стикеры, соцсети.'),
         ('Rip Technologies', 'USA', '2020 — 2021', 'Концепты и иллюстрации для постеров и открыток, подготовка макетов к печати.'),
         ('ТутМи', 'RU', '2014 — 2020', 'Корпоративные сайты, интернет-магазины, лендинги, мобильные приложения, прототипирование. Иллюстрации, ретушь, упаковка, принты, инфографика, презентации, полиграфия. 2 года руководила командой из пяти дизайнеров.'),
         ('Bloomex', 'CA', '2011 — 2014', 'Интернет-магазины и лендинги, ретушь, упаковка, инфографика, презентации, полиграфия. Офис канадской компании, англоязычная команда.')],
    skills_t='Навыки',
    skills=[('Дизайн от интерфейсов до полиграфии', 'UI/UX, сайты, брендинг, иллюстрации, печать. 200+ дизайн-концепций, сотни логотипов.'),
            ('Профильное образование', 'ТРТУ, сейчас ЮФУ. Инженер-дизайнер.'),
            ('6+ лет в IT-студии', 'Работа в связке с разработчиками — от идеи до реализации.'),
            ('Международный опыт', '3+ года в англоязычной команде канадской компании, удалённая работа с зарубежными клиентами.'),
            ('Руководство и наставничество', '2 года руководила командой из пяти дизайнеров.'),
            ('Самостоятельность и сроки', 'Большой опыт фриланса, планирую нагрузку и довожу до результата.'),
            ('Вайбкодинг', 'Сайты и интерактивные инструменты с помощью AI.'),
            ('AI и автоматизация', 'AI-ассистенты, автоматизация процессов, генерация изображений и видео.')],
    tools_t='Инструменты',
    tools=[('Основные', 'Figma, Photoshop, Illustrator, Lightroom, Acrobat, Tilda, Procreate'),
           ('AI', 'ChatGPT, Claude, Codex, Lovable, Midjourney, Higgsfield, Krea, Recraft, Kling, Runway, Nano Banana, Suno'),
           ('Другое', 'GitHub, Supabase, Vercel, Obsidian, Miro, InDesign, Fresco, CorelDRAW, Procreate Dreams, CapCut, WIX, Keynote, PowerPoint, Google Slides')],
    certs_t='Курсы и сертификаты',
    certs=['AI-Эксперт', 'Экспериментальная композиция', 'Прикладная типографика', 'Дизайн взаимодействия', 'Веб-дизайн', 'Tilda School', 'Креативная верстка и анимация', 'Работа с западными клиентами'],
    langs_t='Языки', langs='Русский — родной · Английский — рабочий · Турецкий — базовый',
    contacts_t='Контакты', site_l='Портфолио',
)

EN = dict(
    lang='en', file='Korotkevich_Nadezhda_CV_EN.pdf',
    name='Nadezhda Korotkevich', role='Graphic design → Web design → UI/UX → Illustration → AI',
    about_t='About',
    about=['Designer and illustrator with 17+ years of experience and 300+ delivered projects — from startups to international companies.',
           'I work where systems thinking meets visual expression: I design interfaces, build brand visuals and draw illustrations. Good design, to me, is not only beautiful but clear and practical.'],
    exp_t='Experience',
    exp=[('LuckyGroup', 'RU', 'Dec 2024 — May 2026', 'Websites and landing pages, Tilda development. Identity, branding, logos. Print, presentations, social media. Exhibition stands and full design support for conferences. Illustration, retouching, AI tools.'),
         ('MoySklad', 'RU', 'Mar 2024 — Dec 2024', 'Product portal work, user research, landing pages. New design concept, social media, print, merch, exhibition stands, presentations.'),
         ('EFKO', 'RU', 'Jan 2023 — Mar 2024', 'Project work for one of Russia’s largest food companies: design concept for a subscription magazine for professional chefs and menus for several restaurants; all illustrations and prepress.'),
         ('Ants Games', 'UAE', 'Mar 2022 — Dec 2022', 'Game interfaces, characters, backgrounds and UI elements. Social media and ad creatives.'),
         ('EmiDAO', 'UAE', '2021 — 2022', 'Websites and landing pages. Concepts and illustrations for an NFT project, stickers, social media.'),
         ('Rip Technologies', 'USA', '2020 — 2021', 'Concepts and illustrations for posters and greeting cards, prepress.'),
         ('TutMe', 'RU', '2014 — 2020', 'Corporate websites, e-commerce, landing pages, mobile apps, prototyping. Illustration, retouching, packaging, prints, infographics, presentations, print. Led a team of five designers for 2 years.'),
         ('Bloomex', 'CA', '2011 — 2014', 'E-commerce and landing pages, retouching, packaging, infographics, presentations, print. On-site in a Canadian company, English-speaking team.')],
    skills_t='Skills',
    skills=[('Design from UI to print', 'UI/UX, websites, branding, illustration, print. 200+ design concepts, hundreds of logos.'),
            ('Design education', 'Engineering degree in design (TRTU, now SFedU).'),
            ('6+ years in an IT studio', 'Close collaboration with developers, from idea to launch.'),
            ('International experience', '3+ years in an English-speaking Canadian team, long-term remote work with clients abroad.'),
            ('Leadership and mentoring', 'Led a team of five designers for 2 years.'),
            ('Ownership and deadlines', 'Extensive freelance experience; I plan my workload and deliver.'),
            ('Vibe coding', 'Websites and interactive tools built with AI.'),
            ('AI and automation', 'AI assistants, workflow automation, image and video generation.')],
    tools_t='Tools',
    tools=[('Core', 'Figma, Photoshop, Illustrator, Lightroom, Acrobat, Tilda, Procreate'),
           ('AI', 'ChatGPT, Claude, Codex, Lovable, Midjourney, Higgsfield, Krea, Recraft, Kling, Runway, Nano Banana, Suno'),
           ('Other', 'GitHub, Supabase, Vercel, Obsidian, Miro, InDesign, Fresco, CorelDRAW, Procreate Dreams, CapCut, WIX, Keynote, PowerPoint, Google Slides')],
    certs_t='Courses',
    certs=['AI Expert', 'Experimental composition', 'Applied typography', 'Interaction design', 'Web design', 'Tilda School', 'Creative layout and animation', 'Working with Western clients'],
    langs_t='Languages', langs='Russian — native · English — working · Turkish — basic',
    contacts_t='Contacts', site_l='Portfolio',
)

CSS = '''
@page { size: A4; margin: 0; }
* { box-sizing: border-box; }
html, body { margin: 0; }
body { font-family: "JetBrains Mono", monospace; color: #171717; font-size: 8.6pt; line-height: 1.38; letter-spacing: .01em; }
.page { position: relative; width: 210mm; height: 297mm; padding: 14mm 14mm 12mm; overflow: hidden; background: #F6F5F2; page-break-after: always; }
.page:last-child { page-break-after: auto; }
.page::before { content: ""; position: absolute; inset: 0; background: url(data:image/png;base64,NOISE) 0 0 / 120px 120px; opacity: .07; mix-blend-mode: multiply; pointer-events: none; }
.page > * { position: relative; }
h1, h2, .k { font-family: "Unbounded", sans-serif; font-weight: 800; letter-spacing: -0.02em; }
.head { display: grid; grid-template-columns: 1fr 44mm; gap: 8mm; align-items: end; padding-bottom: 7mm; border-bottom: 1px solid #171717; }
h1 { margin: 0; font-size: 30pt; line-height: .98; }
.role { margin-top: 4mm; text-transform: uppercase; font-size: 7.6pt; letter-spacing: .06em; color: #555; }
.photo { width: 44mm; height: 52mm; object-fit: cover; border-radius: 2px; display: block; }
.contacts { display: flex; flex-wrap: wrap; gap: 2mm 6mm; margin-top: 5mm; font-size: 8pt; }
.contacts a { color: inherit; text-decoration: none; border-bottom: 1px solid #bbb; }
h2 { margin: 0 0 3.5mm; font-size: 12pt; }
h2 span { font-family: "JetBrains Mono", monospace; font-weight: 400; font-size: 7.5pt; color: #777; letter-spacing: .05em; margin-left: 2mm; }
section { margin-top: 7mm; }
.about p { margin: 0 0 2mm; max-width: 165mm; }
.job { display: grid; grid-template-columns: 46mm 1fr; gap: 5mm; padding: 2.6mm 0; border-top: 1px solid #d8d6d0; break-inside: avoid; }
.job:first-of-type { border-top: 0; padding-top: 0; }
.job .k { font-size: 9pt; }
.job .c { color: #777; font-size: 7pt; letter-spacing: .05em; }
.job .d { color: #777; font-size: 7.4pt; margin-top: 1mm; }
.job p { margin: 0; }
.grid2 { display: grid; grid-template-columns: 1fr 1fr; gap: 3.5mm 8mm; }
.sk b { display: block; font-family: "Unbounded"; font-weight: 800; font-size: 8.4pt; letter-spacing: -0.01em; margin-bottom: .8mm; }
.sk i { font-style: normal; font-family: "Unbounded"; font-weight: 800; color: #aaa; margin-right: 2mm; }
.sk p { margin: 0; color: #444; }
.tools div { display: grid; grid-template-columns: 24mm 1fr; gap: 4mm; padding: 1.6mm 0; border-top: 1px solid #d8d6d0; }
.tools div:first-child { border-top: 0; }
.tools b { font-weight: 400; color: #777; text-transform: uppercase; font-size: 7.2pt; letter-spacing: .05em; }
.tags { display: flex; flex-wrap: wrap; gap: 2mm; }
.tags span { padding: .8mm 2.2mm 1mm; border: 1px solid #171717; border-radius: 2px; font-size: 7.6pt; }
.foot { position: absolute; left: 14mm; right: 14mm; bottom: 9mm; display: flex; justify-content: space-between; font-size: 7pt; color: #888; letter-spacing: .05em; text-transform: uppercase; }
'''

def esc(s): return s.replace('&', '&amp;').replace('<', '&lt;')

def html(d, photo, noise):
    contacts = (f'<a href="mailto:teyega@mail.ru">teyega@mail.ru</a>'
                f'<a href="https://t.me/nadenka_nadushca">Telegram @nadenka_nadushca</a>'
                f'<a href="https://wa.me/79821886114">+7 (982) 188-61-14</a>'
                f'<a href="https://{SITE}">{d["site_l"]}: {SITE}</a>')
    jobs = ''.join(f'<div class="job"><div><div class="k">{esc(c)}</div><div class="c">{cc}</div><div class="d">{esc(dt)}</div></div><p>{esc(t)}</p></div>' for c, cc, dt, t in d['exp'])
    skills = ''.join(f'<div class="sk"><b><i>{i+1:02d}</i>{esc(t)}</b><p>{esc(s)}</p></div>' for i, (t, s) in enumerate(d['skills']))
    tools = ''.join(f'<div><b>{esc(t)}</b><span>{esc(s)}</span></div>' for t, s in d['tools'])
    certs = ''.join(f'<span>{esc(c)}</span>' for c in d['certs'])
    foot = f'<div class="foot"><span>{esc(d["name"])} · CV</span><span>{SITE}</span></div>'
    return f'''<!doctype html><html lang="{d["lang"]}"><head><meta charset="utf-8"><style>{CSS.replace("NOISE", noise)}</style></head><body>
<div class="page">
  <div class="head"><div><h1>{esc(d["name"]).replace(" ", "<br>", 1)}</h1><div class="role">{esc(d["role"])}</div><div class="contacts">{contacts}</div></div>
  <img class="photo" src="data:image/jpeg;base64,{photo}" alt=""></div>
  <section class="about"><h2>{d["about_t"]}</h2>{''.join(f"<p>{esc(p)}</p>" for p in d["about"])}</section>
  <section><h2>{d["exp_t"]}<span>2011—2026</span></h2>{jobs}</section>
  {foot}
</div>
<div class="page">
  <section style="margin-top:0"><h2>{d["skills_t"]}</h2><div class="grid2">{skills}</div></section>
  <section class="tools"><h2>{d["tools_t"]}</h2>{tools}</section>
  <section><h2>{d["certs_t"]}</h2><div class="tags">{certs}</div></section>
  <section><h2>{d["langs_t"]}</h2><p style="margin:0">{esc(d["langs"])}</p></section>
  <section><h2>{d["contacts_t"]}</h2><div class="contacts" style="margin-top:0">{contacts}</div></section>
  {foot}
</div></body></html>'''

if __name__ == '__main__':
    photo, noise = photo_b64(), noise_b64()
    out = os.path.join(ROOT, 'cv')
    with sync_playwright() as p:
        b = p.chromium.launch(executable_path='/opt/pw-browsers/chromium-1194/chrome-linux/chrome')
        for d in (RU, EN):
            src = os.path.join(out, f'cv-{d["lang"]}.html')
            open(src, 'w').write(html(d, photo, noise))
            pg = b.new_page(); pg.goto('file://' + src); pg.wait_for_timeout(400)
            pg.pdf(path=os.path.join(out, d['file']), format='A4', print_background=True, prefer_css_page_size=True)
            print('ok', d['file'])
        b.close()
