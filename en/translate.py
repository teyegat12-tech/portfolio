# Собирает en/index.html из index.html: python3 en/translate.py
import os, re
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

T = {
# meta / hero / nav
'Портфолио Надежды Короткевич: графический дизайн, веб-дизайн, UI/UX, иллюстрации и AI. 17+ лет в профессии.': 'Portfolio of Nadezhda Korotkevich: graphic design, web design, UI/UX, illustration and AI. 17+ years of experience.',
'Надежда Короткевич — графический дизайн, веб-дизайн, UI/UX, иллюстрации': 'Nadezhda Korotkevich — graphic design, web design, UI/UX, illustration',
'Надежда Короткевич, портрет': 'Nadezhda Korotkevich, portrait',
'Короткевич Надежда · ©2026': 'Nadezhda Korotkevich · ©2026',
'Графический дизайн → Веб-дизайн → UI/UX → иллюстрации → AI': 'Graphic design → Web design → UI/UX → Illustration → AI',
'Обо мне': 'About', 'Опыт': 'Experience', 'Скиллы': 'Skills', 'Клиенты': 'Clients', 'Кейсы': 'Cases',
'Иллюстрации': 'Illustrations', 'Логофолио': 'Logofolio', 'Контакты': 'Contacts', 'Разделы': 'Sections', 'Меню': 'Menu',
'Открыть меню': 'Open menu', 'Закрыть меню': 'Close menu',
# about
'Привет': 'Hello', 'Меня зовут Надежда.': 'My name is Nadezhda.', 'Я дизайнер и иллюстратор.': 'I’m a designer and illustrator.',
'17+ лет в профессии.': '17+ years in the profession.', '300+ реализованных проектов.': '300+ delivered projects.',
'От стартапов до международных компаний.': 'From startups to international companies.',
'Работаю на стыке системного мышления и визуальной выразительности.': 'I work where systems thinking meets visual expression.',
'Проектирую интерфейсы, создаю визуал для брендов, рисую иллюстрации.': 'I design interfaces, create brand visuals and draw illustrations.',
'Для меня важно, чтобы дизайн': 'What matters to me is that design',
'был не просто красивым, а&nbsp;понятным и&nbsp;практичным.': 'is not only beautiful, but clear and practical.',
# experience
'Декабрь 2024 — Май 2026': 'Dec 2024 — May 2026', 'Март 2024 — Декабрь 2024': 'Mar 2024 — Dec 2024',
'Январь 2023 — Март 2024': 'Jan 2023 — Mar 2024', 'Март 2022 — Декабрь 2022': 'Mar 2022 — Dec 2022',
'МойСклад': 'MoySklad', 'ТутМи': 'TutMe', 'Фриланс': 'Freelance', 'ЭФКО': 'EFKO',
'Дизайн сайтов и&nbsp;лендингов, верстка в&nbsp;Tilda. Айдентика и&nbsp;брендинг. Разработка логотипов. Графический дизайн и&nbsp;полиграфия. Презентации. Оформление соцсетей. Дизайн выставочных стендов, полное дизайн-сопровождение конференций. Отрисовка иллюстраций, художественная ретушь фото, работа с&nbsp;нейросетями и&nbsp;др.':
 'Websites and landing pages, Tilda development. Identity and branding. Logo design. Graphic design and print. Presentations. Social media. Exhibition stands, full design support for conferences. Illustration, art photo retouching, AI tools and more.',
'Работа над порталом, участие в&nbsp;исследованиях, дизайн лендингов. Оформление соцсетей, разработка новой дизайн-концепции, полиграфия, разработка мерча, дизайн выставочных стендов, оформление презентаций и&nbsp;др.':
 'Product portal work, user research, landing pages. Social media, a new design concept, print, merch, exhibition stands, presentations and more.',
'На проектной основе работала с&nbsp;одной из&nbsp;крупнейших продовольственных компаний в&nbsp;России.': 'Project-based work for one of the largest food companies in Russia.',
'Разработала дизайн-концепт под фирменный подписной журнал для профессиональных шеф-поваров и&nbsp;меню для нескольких разнонаправленных ресторанов. Отрисовала все иллюстрации и&nbsp;занималась подготовкой материалов к&nbsp;печати.':
 'Designed the concept of a branded subscription magazine for professional chefs and menus for several different restaurants. Drew all the illustrations and prepared materials for print.',
'Создание игровых интерфейсов, отрисовка персонажей, фонов и&nbsp;элементов интерфейсов. Оформление соцсетей и&nbsp;рекламных материалов.':
 'Game interfaces, characters, backgrounds and UI elements. Social media and ad creatives.',
'Дизайн веб-сайтов и&nbsp;целевых страниц. Создание концептов и&nbsp;отрисовка иллюстраций для проекта NFT. Отрисовка стикеров, оформление соцсетей.':
 'Websites and landing pages. Concepts and illustrations for an NFT project. Stickers and social media.',
'Разработка концептов и&nbsp;отрисовка иллюстраций для постеров и&nbsp;открыток. Подготовка макетов к&nbsp;печати.':
 'Concepts and illustrations for posters and greeting cards. Prepress.',
'Дизайн-концепции корпоративных сайтов, интернет-магазины и&nbsp;лендинги, мобильные приложения. Прототипирование. Отрисовка иллюстраций в&nbsp;разной стилистике. Художественная ретушь изображений. Дизайн и&nbsp;подготовка полиграфической и&nbsp;рекламной продукции к&nbsp;печати, дизайн упаковки, отрисовка принтов, стикеров. Обработка и&nbsp;ретушь изображений. Инфографика. Презентации. Оформление соцсетей и&nbsp;др.':
 'Design concepts for corporate websites, e-commerce and landing pages, mobile apps. Prototyping. Illustration in different styles. Art retouching. Print and advertising design and prepress, packaging, prints and stickers. Image editing and retouching. Infographics. Presentations. Social media and more.',
'Интернет-магазины и&nbsp;лендинги. Обработка и&nbsp;ретушь изображений. Дизайн упаковки. Инфографика. Презентации. Дизайн и&nbsp;подготовка полиграфической и&nbsp;рекламной продукции к&nbsp;печати.':
 'E-commerce and landing pages. Image editing and retouching. Packaging design. Infographics. Presentations. Print and advertising design and prepress.',
# soft
'Софт': 'Software', '{ Инструменты, с которыми я работаю }': '{ Tools I work with }', '{ Инструменты }': '{ Tools }',
'Основные': 'Core', 'Нейронки': 'AI tools', 'Другое': 'Other',
# skills
'{ Навыки }': '{ Skills }', 'Навыки, листаются вбок': 'Skills, scroll sideways',
'Предыдущий навык': 'Previous skill', 'Следующий навык': 'Next skill',
'Дизайн от&nbsp;интерфейсов до&nbsp;полиграфии': 'Design from&nbsp;UI to&nbsp;print',
'UI/UX, сайты, брендинг, иллюстрации и&nbsp;печатные материалы. За&nbsp;плечами&nbsp;— 200+': 'UI/UX, websites, branding, illustration and print. 200+',
'дизайн-концепций': 'design concepts', ', сотни логотипов и&nbsp;фирменных стилей.': ', hundreds of logos and brand identities.',
'Профильное образование': 'Design education',
'Окончила ТРТУ, сейчас ЮФУ. По&nbsp;специальности&nbsp;—': 'Graduated from TRTU (now SFedU). Degree:',
'инженер-дизайнер': 'design engineer',
'6+ лет в&nbsp;IT-студии': '6+ years in&nbsp;an IT studio',
'Знаю процессы изнутри и&nbsp;умею работать в&nbsp;связке с&nbsp;разработчиками&nbsp;— от&nbsp;идеи до&nbsp;реализации.': 'I know the process from the inside and work closely with developers&nbsp;— from idea to launch.',
'Международный опыт': 'International experience',
'3+ года в&nbsp;офисе канадской компании, в&nbsp;англоязычной команде. Долгосрочно сотрудничаю с&nbsp;зарубежными компаниями удалённо.': '3+ years on-site at a Canadian company in an English-speaking team. Long-term remote work with companies abroad.',
'Руководство и&nbsp;наставничество': 'Leadership and&nbsp;mentoring',
'2 года руководила командой из&nbsp;пяти дизайнеров: распределяла задачи, вела переговоры и&nbsp;сдавала проекты. Помогаю младшим специалистам расти.': 'For 2 years I led a team of five designers: assigned tasks, negotiated and delivered projects. I help junior designers grow.',
'Самостоятельность и&nbsp;сроки': 'Ownership and&nbsp;deadlines',
'Большой опыт фриланса. Быстро включаюсь в&nbsp;работу, планирую нагрузку и&nbsp;довожу проекты до&nbsp;результата.': 'Extensive freelance experience. I get up to speed fast, plan my workload and see projects through.',
'Вайбкодинг': 'Vibe coding',
'Создаю сайты и&nbsp;интерактивные инструменты с&nbsp;помощью AI. Соединяю дизайн и&nbsp;код, чтобы превращать идеи в&nbsp;работающие проекты.': 'I build websites and interactive tools with AI, combining design and code to turn ideas into working products.',
'AI и&nbsp;автоматизация': 'AI and&nbsp;automation', 'Собираю': 'I build', 'AI-ассистентов': 'AI assistants',
'и&nbsp;автоматизирую рабочие процессы. Использую нейросети для&nbsp;генерации изображений, видео и&nbsp;ретуши.': 'and automate workflows. I use neural networks for image and video generation and retouching.',
# upgrade
'Апгрейд': 'Upgrade', '{ Сертификаты и подтверждённая экспертиза }': '{ Certificates and proven expertise }', '{ Сертификаты }': '{ Certificates }',
'Сертификат: ': 'Certificate: ', 'Сертификаты': 'Certificates',
'AI-Эксперт': 'AI Expert', 'Экспериментальная композиция': 'Experimental composition', 'Прикладная типографика': 'Applied typography',
'Дизайн взаимодействия': 'Interaction design', 'Веб-дизайн': 'Web design', 'Креативная верстка и&nbsp;анимация': 'Creative layout and&nbsp;animation',
'Креативная верстка и анимация': 'Creative layout and animation', 'Работа с&nbsp;западными клиентами': 'Working with&nbsp;Western clients', 'Работа с западными клиентами': 'Working with Western clients',
'Генерация визуалов и&nbsp;видео, продвинутый промт-инжиниринг, внедрение AI в&nbsp;дизайн и&nbsp;маркетинг, создание GPT-ассистентов, разработка контент-стратегий и&nbsp;автоматизация рабочих процессов.': 'Visual and video generation, advanced prompt engineering, AI in design and marketing, building GPT assistants, content strategy and workflow automation.',
'Работа с&nbsp;динамикой и&nbsp;статикой, контраст и&nbsp;ритм, управление формой и&nbsp;форматом, группировка элементов, создание цельного образа и&nbsp;разработка концепций через визуальную метафору.': 'Dynamics and statics, contrast and rhythm, form and format, grouping, building a coherent image and developing concepts through visual metaphor.',
'Композиция и&nbsp;архитектура страницы, работа с&nbsp;форматом и&nbsp;визуальной иерархией, выстраивание структуры больших массивов текста, грамотная верстка текстовых элементов, подбор и&nbsp;сочетание шрифтов под характер проекта.': 'Page composition and architecture, format and visual hierarchy, structuring large amounts of text, careful typesetting, choosing and pairing typefaces to fit the project.',
'Проектирование микро- и&nbsp;макровзаимодействий, навигационные модели и&nbsp;архитектура интерфейса, сценарии пользователя, адаптивность и&nbsp;бесшовность взаимодействия, анимация как инструмент навигации и&nbsp;управления вниманием.': 'Micro- and macro-interactions, navigation models and information architecture, user scenarios, responsive and seamless interaction, animation as a tool for navigation and attention.',
'Аналитика и&nbsp;исследование ЦА, построение пользовательских сценариев, прототипирование, системная работа с&nbsp;композицией и&nbsp;типографикой, сетки и&nbsp;модульная структура, адаптив и&nbsp;интерактивная верстка.': 'Audience research, user scenarios, prototyping, systematic work with composition and typography, grids and modular structure, responsive and interactive layout.',
'Проектирование и&nbsp;сборка сайтов любой сложности, Zero Block и&nbsp;кастомные сетки, анимация и&nbsp;интерактив, адаптивность, интеграции и&nbsp;подготовка проекта к&nbsp;запуску.': 'Designing and building websites of any complexity, Zero Block and custom grids, animation and interactivity, responsiveness, integrations and launch preparation.',
'Деловая коммуникация и&nbsp;брифинг на&nbsp;международном уровне, соблюдение дедлайнов и&nbsp;стандартов качества, структурирование процессов, защита решений, работа по&nbsp;контрактам и&nbsp;в&nbsp;рамках четких бизнес-требований.': 'Business communication and briefing at an international level, meeting deadlines and quality standards, structuring processes, defending decisions, working under contracts and clear business requirements.',
'нажми на стопку, чтобы листать': 'tap the stack to flip through',
# cases
'Кейс #': 'Case #', 'Смотреть проект': 'View project', 'Показать ещё кейсы': 'Show more cases', 'Показать ещё': 'Show more', 'Скрыть': 'Hide',
'Новостное мини-приложение на&nbsp;основе ИИ.': 'AI-powered news mini app.',
'Работа с&nbsp;курса «NewLVL 180°» Сергея Гурова': 'Project from Sergey Gurov’s «NewLVL 180°» course',
'Аналитика, дизайн, адаптив,': 'Research, design, responsive,', 'AI-визуал': 'AI visuals', '3D-визуал': '3D visuals',
'{ Сайт, соцсети, мерч, оформление выставочной площадки }': '{ Website, social media, merch, venue design }',
'Полное дизайн-сопровождение организации фестиваля. Разработка концепции. Брендинг. Оформление соцсетей. Презентации для партнеров и&nbsp;участников. Мерч. Рекламная продукция. Карта площадки.': 'Full design support for a festival. Concept. Branding. Social media. Presentations for partners and participants. Merch. Advertising materials. Venue map.',
'{ Лонгрид, иллюстрации, дизайн }': '{ Longread, illustration, design }',
'Лонгрид о&nbsp;мультипликаторе Роберте Саакянце. Весь сайт нарисован вручную с&nbsp;нуля&nbsp;— каждый персонаж, фон и&nbsp;деталь. Сейчас в&nbsp;работе: анимация сцен и&nbsp;мобильная версия.': 'A longread about animator Robert Saakyants. The whole site is hand-drawn from scratch&nbsp;— every character, background and detail. In progress: scene animation and the mobile version.',
'{ Лого, сайт, айдентика, соцсети, мерч }': '{ Logo, website, identity, social media, merch }',
'Разработка логотипа и&nbsp;айдентики. Дизайн банковских карт. Оформление соцсетей.': 'Logo and identity design. Bank card design. Social media.',
'Оформление соцсетей. Презентации. Мерч. Рекламная продукция. Дизайн-сопровождение конференций, дизайн выставочных стендов.': 'Social media. Presentations. Merch. Advertising materials. Design support for conferences, exhibition stands.',
'{ Редизайн лендинга, UI/UX, адаптив,': '{ Landing page redesign, UI/UX, responsive,',
'Редизайн главной страницы МойСклад&nbsp;— облачного сервиса для&nbsp;торговли, склада и&nbsp;CRM. Новая структура и&nbsp;интерфейс, адаптив под все экраны,': 'Redesign of the MoySklad home page&nbsp;— a cloud service for retail, inventory and CRM. New structure and interface, responsive for all screens,',
'{ Лого, лендинг, UI/UX, адаптив }': '{ Logo, landing page, UI/UX, responsive }',
'Лендинг для&nbsp;компании «Лёгкий шаг»&nbsp;— проектирование, изготовление и&nbsp;установка лестниц. Разработка логотипа, структура и&nbsp;дизайн сайта, калькулятор стоимости, адаптив под планшет.': 'Landing page for «Legkiy Shag», a company that designs, builds and installs staircases. Logo, site structure and design, price calculator, tablet layout.',
# alts (cases)
'главный экран сайта': 'website home screen', 'главный экран лендинга': 'landing home screen', 'мобильная версия': 'mobile version',
'соцсети и носители': 'social media and print', 'макет ': 'layout ', 'экран ': 'screen ', 'адаптивная версия': 'responsive version',
'Лонгрид «Роберт Саакянц и его сказочные миры»: первый экран': 'Longread «Robert Saakyants and his fairy-tale worlds»: first screen',
'Лонгрид о Роберте Саакянце: нарисованные сцены': 'Longread about Robert Saakyants: hand-drawn scenes',
'Лонгрид: «Хиппи, который вырос в великого мультипликатора»': 'Longread: «The hippie who became a great animator»',
'Лонгрид: «В синем море, в белой пене…»': 'Longread: «In the blue sea, in the white foam…»',
'Лонгрид: «Иш ты, Масленица!»': 'Longread: «Oh my, Maslenitsa!»',
'блоки «Кому выгодно» и «Бесплатный тариф»': 'audiences and free plan sections', 'отзывы и преимущества': 'reviews and benefits',
'интеграции и мобильное приложение': 'integrations and mobile app',
'калькулятор стоимости лестницы': 'staircase price calculator', 'преимущества, о компании, услуги': 'benefits, about, services',
'вопросы и ответы': 'FAQ', 'форма, Instagram и контакты': 'form, Instagram and contacts',
'Лёгкий шаг': 'Legkiy Shag',
# illustrations alts
'Иллюстрация: ': 'Illustration: ', 'Краб среди листьев лотоса': 'Crab among lotus leaves', 'Девушка с цветами в волосах': 'Girl with flowers in her hair',
'Мужчина с катаной среди цветущей сакуры': 'Man with a katana among cherry blossoms', 'Пионы': 'Peonies', 'Баскетболистка с мячом': 'Basketball player with a ball',
'Ноги в окне машины на фоне облаков': 'Feet out of a car window against the clouds', 'Портрет мужчины в кепке': 'Portrait of a man in a cap',
'Неоновое лицо': 'Neon face', 'Девушка с лапшой и осьминогом': 'Girl with noodles and an octopus', 'Девушка в стиле граффити': 'Girl in graffiti style',
'Портрет с настольной игрой Funky Business': 'Portrait with the Funky Business board game', 'Скелет и дама: ретро-мультфильм': 'Skeleton and lady: retro cartoon',
'Сцена в стиле ретро-мультфильма': 'Retro cartoon scene', 'Бульдозер и полицейская машинка': 'Bulldozer and a police car',
# logos / clients
'Лого': 'Logo', '{ Логофолио }': '{ Logofolio }', '{ Клиенты }': '{ Clients }', 'Логотип «19»': '«19» logo', 'Логотип': 'Logo',
'Свой интерьер': 'Svoy Interior', 'Режь и ешь на дубовых досках': 'Rezh i Esh', 'Виона': 'Viona', 'Королевский кедр': 'Royal Cedar',
'Банка': 'Banka', 'Еврострой': 'Evrostroy', 'ДентTravel': 'DentTravel', 'МКШОР «Север»': 'Sever sports school', 'Монограмма': 'Monogram',
'Газпром': 'Gazprom', 'Лукойл': 'Lukoil', 'НЛМК': 'NLMK', 'Роснефть': 'Rosneft', 'Рокет Ворк': 'Rocket Work',
# contacts
'Благодарю за&nbsp;внимание': 'Thank you for&nbsp;your attention',
'Если вас заинтересовала моя кандидатура, всегда рада пообщаться и&nbsp;обсудить детали.': 'If you’re interested in working together, I’m always happy to talk and discuss the details.',
'Примеры актуальных работ вышлю по&nbsp;запросу.': 'Recent work samples are available on request.',
'Старые работы, находящиеся в&nbsp;свободном доступе, можете посмотреть тут:': 'Older public work can be found here:',
'Короткевич': 'Korotkevich', 'Надежда': 'Nadezhda',
# CV / language
'Скачать CV': 'Download CV', 'Korotkevich_Nadezhda_CV_RU.pdf': 'Korotkevich_Nadezhda_CV_EN.pdf',
}

def build():
    h = open(os.path.join(ROOT, 'index.html')).read()
    h = h.replace('<html lang="ru">', '<html lang="en">', 1)
    h = re.sub(r'(src|href)="(assets/|style\.css|cv/)', r'\1="../\2', h)
    h = h.replace("url(assets/", "url(../assets/")
    # hero: name order
    h = h.replace('Короткевич <br class="m-only">Надежда', 'Nadezhda <br class="m-only">Korotkevich')
    h = h.replace('<b>RU</b> / <a data-lang-switch href="en/" hreflang="en">EN</a>', '<a data-lang-switch href="../" hreflang="ru">RU</a> / <b>EN</b>')
    h = h.replace('<a data-lang-switch href="en/" hreflang="en">EN</a>', '<a data-lang-switch href="../" hreflang="ru">RU</a>')
    h = h.replace('<link rel="alternate" hreflang="en" href="en/">', '<link rel="alternate" hreflang="ru" href="../">')
    for ru in sorted(T, key=len, reverse=True):
        h = h.replace(ru, T[ru])
    os.makedirs(os.path.join(ROOT, 'en'), exist_ok=True)
    open(os.path.join(ROOT, 'en/index.html'), 'w').write(h)
    left = sorted(set(m.group(0).strip() for m in re.finditer(r'>[^<>]*[А-Яа-яЁё][^<>]*<|"[^"\n]*[А-Яа-яЁё][^"\n]*"', h)))
    return left

if __name__ == '__main__':
    for l in build(): print('RU LEFT:', l[:120])
