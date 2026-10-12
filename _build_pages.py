#!/usr/bin/env python3
"""Generate 4 destination sub-pages for the Marvel Travel site."""
import os

SITE = r"C:\Users\Marco Yacoub\Desktop\marvel-landing"

# shared CSS/design tokens (reuse the landing page aesthetic)
HEAD = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{title} — Marvel Travel</title>
<link rel="icon" href="assets/logo.png">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Cinzel:wght@400;600;700;900&family=Playfair+Display:ital,wght@0,400;0,600;0,700;1,400&family=Montserrat:wght@300;400;500;600;700&display=swap" rel="stylesheet">
<style>
:root{{--gold:#c69c4a;--gold-l:#e2be6e;--gold-d:#9a7638;--cream:#f5f1e9;--ink:#101622;--paper:#faf7f0;--line:rgba(198,156,74,.25)}}
*{{margin:0;padding:0;box-sizing:border-box}}
html{{scroll-behavior:smooth}}
body{{font-family:'Montserrat',sans-serif;background:var(--paper);color:var(--ink);line-height:1.6;overflow-x:hidden}}
img{{max-width:100%;display:block}}
a{{color:inherit;text-decoration:none}}
.wrap{{max-width:1180px;margin:0 auto;padding:0 28px}}
.eyebrow{{font-weight:600;font-size:13px;letter-spacing:.35em;text-transform:uppercase;color:var(--gold-d)}}
nav{{position:fixed;top:0;left:0;right:0;z-index:100;transition:.4s;padding:22px 0}}
nav.scrolled{{background:rgba(16,22,34,.92);backdrop-filter:blur(14px);padding:14px 0;box-shadow:0 4px 30px rgba(0,0,0,.25)}}
nav .wrap{{display:flex;align-items:center;justify-content:space-between}}
.logo{{display:flex;align-items:center;gap:12px}}
.logo img{{height:44px;width:auto}}
.logo span{{font-family:'Cinzel';font-weight:700;font-size:20px;letter-spacing:.12em;color:var(--cream)}}
.nav-links{{display:flex;gap:30px;align-items:center;flex-wrap:wrap}}
.nav-links a{{font-size:12px;font-weight:600;letter-spacing:.12em;text-transform:uppercase;color:var(--cream);opacity:.85;transition:.3s}}
.nav-links a:hover,.nav-links a.active{{opacity:1;color:var(--gold-l)}}
.nav-cta{{background:var(--gold);color:var(--ink)!important;padding:10px 22px;border-radius:40px;opacity:1!important;font-weight:700}}
.nav-cta:hover{{background:var(--gold-l)}}
.hero{{position:relative;min-height:78vh;display:flex;align-items:flex-end;color:var(--cream);overflow:hidden}}
.hero-bg{{position:absolute;inset:0;z-index:-2}}
.hero-bg img{{width:100%;height:100%;object-fit:cover}}
.hero-bg::after{{content:'';position:absolute;inset:0;background:linear-gradient(180deg,rgba(16,22,34,.35),rgba(16,22,34,.75))}}
.hero-content{{padding:140px 0 70px;width:100%}}
.hero h1{{font-family:'Playfair Display',serif;font-size:clamp(44px,7vw,78px);font-weight:700;line-height:1.03;margin:16px 0 10px}}
.hero h1 em{{font-style:italic;color:var(--gold-l)}}
.hero p{{font-size:clamp(16px,2vw,20px);font-weight:300;max-width:640px;opacity:.92}}
.section{{padding:90px 0}}
.about h2{{font-family:'Playfair Display',serif;font-size:clamp(30px,4vw,44px);font-weight:700;margin:14px 0 20px;line-height:1.15}}
.about h2 em{{font-style:italic;color:var(--gold-d)}}
.about p{{color:#4a5163;font-size:17px;margin-bottom:16px;max-width:760px}}
.cards{{display:grid;grid-template-columns:repeat(3,1fr);gap:26px;margin-top:44px}}
.card{{background:#fff;border:1px solid #eee;border-radius:6px;padding:30px;transition:.3s}}
.card:hover{{border-color:var(--gold);transform:translateY(-4px);box-shadow:0 18px 40px rgba(16,22,34,.08)}}
.card .ico{{font-size:30px;margin-bottom:14px}}
.card h3{{font-family:'Cinzel';font-weight:700;font-size:18px;color:var(--gold-d);margin-bottom:10px}}
.card p{{font-size:15px;color:#5a6070}}
.itin{{margin-top:44px;border-left:3px solid var(--gold);padding-left:0}}
.day{{display:grid;grid-template-columns:110px 1fr;gap:22px;padding:24px 0;border-bottom:1px solid #eee}}
.day:last-child{{border-bottom:none}}
.day .d{{font-family:'Cinzel';font-weight:700;color:var(--gold-d);font-size:15px;letter-spacing:.08em}}
.day .t h4{{font-family:'Playfair Display';font-size:20px;font-weight:700;margin-bottom:6px}}
.day .t p{{color:#5a6070;font-size:15px}}
.cta-band{{background:var(--ink);color:var(--cream);text-align:center}}
.cta-band h2{{font-family:'Playfair Display',serif;font-size:clamp(30px,4.5vw,48px);font-weight:700;margin-bottom:14px}}
.cta-band h2 em{{font-style:italic;color:var(--gold-l)}}
.cta-band p{{opacity:.85;max-width:560px;margin:0 auto 34px;font-weight:300}}
.btn{{display:inline-block;font-weight:700;font-size:14px;letter-spacing:.16em;text-transform:uppercase;padding:18px 44px;border-radius:44px;transition:.3s;border:none;cursor:pointer}}
.btn-gold{{background:var(--gold);color:var(--ink)}}
.btn-gold:hover{{background:var(--gold-l);transform:translateY(-2px)}}
.info{{display:grid;grid-template-columns:repeat(4,1fr);gap:20px;margin-top:40px}}
.info div{{text-align:center}}
.info .k{{font-family:'Cinzel';font-weight:700;font-size:26px;color:var(--gold-d)}}
.info .v{{font-size:13px;color:#8a8f9c;letter-spacing:.06em;text-transform:uppercase;margin-top:4px}}
footer{{background:#0b101c;color:var(--cream);padding:60px 0 28px}}
.foot-grid{{display:grid;grid-template-columns:2fr 1fr 1.4fr;gap:40px;margin-bottom:40px}}
.foot-brand img{{height:52px;margin-bottom:16px}}
.foot-brand p{{font-size:14px;opacity:.6;max-width:280px}}
footer h4{{font-family:'Cinzel';font-size:15px;color:var(--gold-l);margin-bottom:16px}}
.foot-links a{{display:block;font-size:14px;opacity:.6;margin-bottom:9px;transition:.3s}}
.foot-links a:hover{{opacity:1;color:var(--gold-l)}}
.socials{{display:flex;gap:12px}}
.socials a{{width:42px;height:42px;border-radius:50%;border:1px solid rgba(198,156,74,.4);display:flex;align-items:center;justify-content:center;transition:.3s}}
.socials a:hover{{background:var(--gold);color:var(--ink)}}
.foot-bottom{{border-top:1px solid rgba(255,255,255,.1);padding-top:24px;display:flex;justify-content:space-between;font-size:13px;opacity:.5;flex-wrap:wrap;gap:10px}}
.rv{{opacity:0;transform:translateY(30px);transition:.8s cubic-bezier(.2,.7,.3,1)}}
.rv.in{{opacity:1;transform:none}}
@media(max-width:900px){{.nav-links{{display:none}}.cards{{grid-template-columns:1fr}}.info{{grid-template-columns:repeat(2,1fr)}}.day{{grid-template-columns:1fr;gap:6px}}.foot-grid{{grid-template-columns:1fr}}}}
</style>
</head>
<body>
<nav id="nav"><div class="wrap">
<a class="logo" href="index.html"><img src="assets/logo.png" alt="Marvel Travel"><span>MARVEL TRAVEL</span></a>
<div class="nav-links">
<a href="index.html#about">About</a>
<a href="cairo.html" class="{active}">Cairo</a>
<a href="siwa.html" class="{active}">Siwa</a>
<a href="sharm.html" class="{active}">Sharm</a>
<a href="luxor.html" class="{active}">Luxor</a>
<a href="index.html#contact" class="nav-cta">Plan Your Trip</a>
</div>
</div></nav>
"""

FOOT = """
<footer><div class="wrap">
<div class="foot-grid">
<div class="foot-brand"><img src="assets/logo.png" alt="Marvel Travel"><p>Premium, locally-crafted travel experiences across Egypt. Travel deeply, travel marvelously.</p></div>
<div class="foot-links"><h4>Destinations</h4><a href="cairo.html">Cairo</a><a href="siwa.html">Siwa</a><a href="sharm.html">Sharm El Sheikh</a><a href="luxor.html">Luxor</a><a href="index.html#tours">All Journeys</a></div>
<div><h4>Contact</h4><p style="font-size:14px;opacity:.6;margin-bottom:6px">+20 1029 216 650<br>+20 1096 766 482</p>
<div class="socials"><a href="https://www.instagram.com/TravelMarvel_/" title="Instagram">◉</a><a href="https://www.facebook.com/TravelMarvel_" title="Facebook">f</a><a href="https://wa.me/201029216650" title="WhatsApp">✆</a></div></div>
</div>
<div class="foot-bottom"><span>© 2026 Marvel Travel. All rights reserved.</span><span>Crafted with care in Cairo 🇪🇬</span></div>
</div></footer>
<script>
addEventListener('scroll',()=>document.getElementById('nav').classList.toggle('scrolled',scrollY>40));
const io=new IntersectionObserver(es=>es.forEach(e=>{if(e.isIntersecting){e.target.classList.add('in');io.unobserve(e.target)}}),{threshold:.12});
document.querySelectorAll('.rv').forEach(el=>io.observe(el));
</script>
</body></html>
"""

os.makedirs(SITE, exist_ok=True)
PAGES = {}

def page(slug, title, tagline, lead, photo, stats, cards, itinerary, cta_head, cta_sub, cards_intro):
    active = slug
    cards_html = "\n".join(
        f'<div class="card rv"><div class="ico">{i}</div><h3>{h}</h3><p>{p}</p></div>'
        for i, h, p in cards)
    stats_html = "\n".join(
        f'<div><div class="k">{k}</div><div class="v">{v}</div></div>' for k, v in stats)
    days_html = "\n".join(
        f'<div class="day rv"><div class="d">{d}</div><div class="t"><h4>{h}</h4><p>{p}</p></div></div>'
        for d, h, p in itinerary)
    body = HEAD.format(title=title, active=active) + f"""
<header class="hero">
<div class="hero-bg"><img src="assets/{photo}" alt="{title}"></div>
<div class="hero-content"><div class="wrap">
<div class="eyebrow" style="color:var(--gold-l)">Destination</div>
<h1>{title}<br><em>{tagline}</em></h1>
<p>{lead}</p>
</div></div>
</header>

<section class="section about"><div class="wrap">
<div class="eyebrow">Why {title}</div>
<h2>{title}, <em>experienced properly</em></h2>
<p>{cards_intro}</p>
<div class="cards">{cards_html}</div>
</div></section>

<section class="section" style="background:var(--cream)"><div class="wrap">
<div class="eyebrow">Sample Itinerary</div>
<h2 class="serif" style="font-size:clamp(30px,4vw,44px);font-weight:700;margin:14px 0 10px">A few days in {title}</h2>
<div class="info">{stats_html}</div>
<div class="itin">{days_html}</div>
</div></section>

<section class="section cta-band"><div class="wrap">
<div class="eyebrow" style="color:var(--gold-l)">Ready?</div>
<h2>{cta_head}</h2>
<p>{cta_sub}</p>
<a class="btn btn-gold" href="https://wa.me/201029216650">Message Us on WhatsApp</a>
</div></section>
""" + FOOT
    PAGES[slug] = body

# ---------- CAIRO ----------
page("cairo", "Cairo", "where history begins",
    "Stand before the last of the Seven Wonders of the ancient world, wander the treasures of the National Museum, and get beautifully lost in the lanes of Khan el-Khalili.",
    "pyramids.jpg",
    [("3–4", "Recommended days"), ("Giza", "Pyramids & Sphinx"), ("Oct–Apr", "Best season"), ("Private", "Guided tours")],
    [("🏛️", "Pyramids & Sphinx", "The Giza plateau at its most magical — sunrise or golden hour, away from the midday crowds."),
     ("🏺", "Museum of Egyptian Civilization", "The royal mummies and 50,000 artifacts, from prehistory to today."),
     ("🕌", "Islamic & Coptic Cairo", "Khan el-Khalili's spice lanes, Al-Azhar, and the Hanging Church."),
     ("🚢", "Nile Dinner Cruise", "Drift past the lit-up corniche with tanoura and a belly-dance show."),
     ("🍽️", "Real Cairo Food", "Koshary, hawawshi, and the rooftop cafes locals actually go to."),
     ("🛍️", "Bazaars & Craft", "Papyrus, perfumes, and copper — with honest prices we negotiate for you.")],
    [("Day 1", "Arrival & Old Cairo", "Airport meet, hotel check-in, then an evening walk through Coptic Cairo and the citadel area."),
     ("Day 2", "Giza Pyramids & Sphinx", "Half-day at the plateau — inside a pyramid, the Sphinx, and the panoramic viewpoint."),
     ("Day 3", "Museums & Bazaar", "The Egyptian Museum or NMEC in the morning, Khan el-Khalili souk and a Nile dinner cruise in the evening."),
     ("Day 4", "Free & Depart", "Morning at leisure, transfer to the airport.")],
    "Your Cairo story starts here",
    "Tell us your dates and we'll design the perfect Cairo escape around you.",
    "Cairo is not a city you tick off — it's one you sink into. We keep the groups small, the pace human, and the guides genuinely great, so you get the monuments without the chaos.")

# ---------- SIWA ----------
page("siwa", "Siwa", "the untouched oasis",
    "Salt lakes you float in, palm-spring springs, mud-brick fortress ruins, and a silence you can hear. Egypt's most magical, least-visited hideaway.",
    "siwa.jpg",
    [("2–3", "Recommended days"), ("Salt lakes", "Signature swim"), ("Oct–Apr", "Best season"), ("Small", "Group tours")],
    [("🧂", "Salt Lakes", "Float weightlessly in the famous turquoise salt pools of the Western Desert."),
     ("🌴", "Fatnas Island", "Sunset over the lake with a Bedouin tea — the shot everyone comes for."),
     ("🏰", "Shali Fortress", "The mud-brick citadel at the heart of old Siwa, glowing gold at dusk."),
     ("♨️", "Cleopatra's Spring", "A natural spring where legend says the queen herself bathed."),
     ("🚙", "Desert Safari", "4x4 across the Great Sand Sea to hot springs and fossil fields."),
     ("🌙", "Desert Stargazing", "Zero light pollution — the Milky Way, clear as day.")],
    [("Day 1", "Cairo → Siwa", "Overnight bus or morning flight to Marsa Matruh, then transfer to the oasis and an evening in town."),
     ("Day 2", "Lakes & Springs", "Salt lake swims, Cleopatra's spring, and the Fatnas Island sunset."),
     ("Day 3", "Desert & Depart", "Morning 4x4 desert safari, then return towards Cairo.")],
    "Find your oasis",
    "Siwa is best in small groups. Tell us when you're free and we'll handle everything else.",
    "Siwa moves slowly, and that's the point. No mega-buses, no rushed stops — just the oasis, the lakes, and a Bedouin way of doing things we know how to unlock.")

# ---------- SHARM ----------
page("sharm", "Sharm El Sheikh", "where the desert meets the sea",
    "World-class reefs, golden beaches, and all-inclusive luxury on the Red Sea — Ras Mohammed, Naama Bay, and some of the best diving on the planet.",
    "sharm.jpg",
    [("4–6", "Recommended days"), ("Red Sea", "Reef diving"), ("Year-round", "Warm climate"), ("5★", "Beachfront stays")],
    [("🤿", "Ras Mohammed", "The crown jewel of Red Sea diving — a national park at the Sinai tip."),
     ("🏖️", "Naama Bay", "The heart of Sharm: beach clubs, promenade, and nightlife."),
     ("🚤", "Boat & Snorkel", "Full-day boats to Tiran Island and the coral gardens."),
     ("🏨", "All-Inclusive Resorts", "Handpicked beachfront hotels from family-friendly to adults-only."),
     ("🪂", "Water Sports", "Windsurfing, kite-surfing, and the famous Sharm lagoon."),
     ("🐪", "Desert Excursions", "Colored Canyon, Blue Hole, and a Bedouin dinner under the stars.")],
    [("Day 1", "Arrival & Beach", "Airport transfer, hotel check-in, and an evening on the Naama Bay promenade."),
     ("Day 2", "Ras Mohammed", "Boat trip to the national park — snorkeling the coral walls and the observatory."),
     ("Day 3", "Tiran & Lagoon", "Full-day cruise to Tiran Island, then water sports in the afternoon."),
     ("Day 4", "Desert Safari", "Colored Canyon by day, a Bedouin dinner and stars by night.")],
    "Your Red Sea escape awaits",
    "Beach, reef, and relaxation — message us and we'll find your perfect stay.",
    "Sharm is where Egypt goes to relax. We match you to the right resort — not just the cheapest — so the holiday actually feels like a holiday.")

# ---------- LUXOR ----------
page("luxor", "Luxor", "the world's greatest open-air museum",
    "Karnak's towering columns, the Valley of the Kings, and sunsets from a felucca on the Nile — the heart of ancient Thebes.",
    "luxor.jpg",
    [("3–4", "Recommended days"), ("Nile", "Felucca sunsets"), ("Oct–Apr", "Best season"), ("Hot air", "Balloon at dawn")],
    [("🏛️", "Karnak Temple", "The largest religious complex ever built — the hypostyle hall has to be seen to be believed."),
     ("👑", "Valley of the Kings", "Tutankhamun's tomb and dozens more cut into the Theban hills."),
     ("🎈", "Sunrise Balloon", "Float over the west bank at dawn — Luxor's signature experience."),
     ("⛵", "Felucca Sail", "A private sunset sail on the Nile, just you and the river."),
     ("🏛️", "Luxor Temple", "Lit up at night, right in the middle of the modern city."),
     ("🛕", "Hatshepsut & Colossi", "The queen's terraced temple and the Memnon colossi on the west bank.")],
    [("Day 1", "East Bank", "Karnak at golden hour, then Luxor Temple after dark."),
     ("Day 2", "West Bank", "Valley of the Kings, Hatshepsut's temple, and the Colossi of Memnon."),
     ("Day 3", "Balloon & Sail", "Sunrise hot-air balloon, then a felucca sunset and a Nubian dinner."),
     ("Day 4", "Dendera & Depart", "Optional Dendera day-trip, then onward travel.")],
    "Walk with the pharaohs",
    "Luxor rewards slow travel. Tell us your dates and we'll build it right.",
    "Luxor is best done unhurried — early mornings on the west bank, afternoons in the shade, and evenings on the water. That's how we pace it.")

os.makedirs(SITE, exist_ok=True)
for slug, body in PAGES.items():
    with open(os.path.join(SITE, slug + ".html"), "w", encoding="utf-8") as f:
        f.write(body)
    print("wrote:", slug + ".html", len(body), "bytes")
print("ALL DESTINATION PAGES BUILT")
