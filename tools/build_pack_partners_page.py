#!/usr/bin/env python3
"""Rebuild page 6 (Current partners / The Bigger Picture) of the partnership
pack and splice it into public/files/Tia_Tandy_Partnership_Pack.pdf.

The original whole-pack builder was lost with a sandbox reset; this rebuilds
the one page that changes when the sponsor roster does, leaving every other
page of the shipped PDF untouched. Fonts are fetched from Google Fonts into
FONT_DIR as Anton-400 / Oswald-500,600,700 / Barlow-400 TTFs before running.

Usage: python3 tools/build_pack_partners_page.py <font_dir> <work_dir>
Then print <work_dir>/p6.html to PDF with headless Chromium
(--no-pdf-header-footer) and run this script again with --splice <page.pdf>.
"""
import base64, pathlib, sys

REPO = pathlib.Path(__file__).resolve().parent.parent
PACK = REPO / "public/files/Tia_Tandy_Partnership_Pack.pdf"
IMG = f"file://{REPO}/public/img"

PARTNERS = [
    ("logo-gilbert.jpg", "@gilbertrugby", "Boot sponsor"),
    ("logo-buddhabox.jpg", "@buddhabox", "Main partner"),
    ("logo-nutrabytes.png", "@nutrabytes", "nutrabytes.com"),
    ("logo-apexor.jpg", "@apexor.uk", "Silver-package partner"),
    ("logo-gelforce.jpg", "@gelforceofficial_", "Protective sports bras"),
    ("logo-apex-mouthguards.jpg", "@apex_mouthguards", "Laser-scanned gum shields"),
    ("logo-aurion.png", "@aurion.london", "Mayfair &middot; London"),
    ("logo-primova.png", "@primovaplus", ""),  # strapline lives in the logo itself
    ("logo-bodymasters.png", "@the_body_masters", "Sports injury &amp; physio"),
    ("logo-katesclothing.png", "@katesclothinghq", ""),
]
SUPPORTERS = [
    ("logo-jackvenom.jpg", "@jackvenomco"),
    ("logo-hipf.jpg", "@hipererformance_hipf"),
    ("logo-enduo.jpg", "@enduosports"),
    ("logo-b4sleep.jpg", "@b4sleep_"),
    ("logo-funkoff.jpg", "@funkoffpro"),
]


def build_html(font_dir: pathlib.Path) -> str:
    def face(fam, weight, fname):
        b64 = base64.b64encode((font_dir / fname).read_bytes()).decode()
        return ("@font-face{font-family:'%s';font-style:normal;font-weight:%s;"
                "src:url(data:font/truetype;base64,%s) format('truetype');}" % (fam, weight, b64))

    fonts = "".join([
        face("Anton", 400, "Anton-400.ttf"),
        face("Oswald", 500, "Oswald-500.ttf"),
        face("Oswald", 600, "Oswald-600.ttf"),
        face("Oswald", 700, "Oswald-700.ttf"),
        face("Barlow", 400, "Barlow-400.ttf"),
    ])

    css = fonts + """
*{margin:0;padding:0;box-sizing:border-box;-webkit-print-color-adjust:exact;print-color-adjust:exact}
@page{size:A4;margin:0}
:root{
  --coal:#0B0B0C;--panel:#131318;
  --gold:#D4AF37;--paper:#F5F2EA;--muted:#A29B8C;
  --line:#2B2B33;--goldline:rgba(212,175,55,.45);
}
body{background:#333;font-family:'Barlow';color:var(--paper)}
.page{width:210mm;height:297mm;background:var(--coal);position:relative;
  padding:15mm 14mm 20mm;overflow:hidden;page-break-after:always;}
.pfoot{position:absolute;left:14mm;right:14mm;bottom:9mm;
  display:flex;justify-content:space-between;border-top:1px solid var(--line);padding-top:3mm;
  font-family:'Oswald';font-weight:500;font-size:7.5pt;letter-spacing:.2em;color:var(--muted);
  text-transform:uppercase;}
.rule{font-family:'Anton';font-size:22pt;color:var(--gold);text-transform:uppercase;
  border-top:2px solid var(--gold);padding-top:5mm;margin-bottom:2.5mm;letter-spacing:.01em}
.sub{font-family:'Oswald';font-weight:600;font-size:10pt;letter-spacing:.24em;color:var(--paper);
  text-transform:uppercase;margin-bottom:6mm}
.lede{font-size:10.5pt;color:var(--muted);margin-bottom:6mm;max-width:150mm}
.numlab{font-family:'Oswald';font-weight:600;font-size:8.5pt;letter-spacing:.26em;color:var(--gold);
  text-transform:uppercase;margin:6mm 0 3mm}
.chips{display:flex;flex-wrap:wrap;gap:2.2mm}
.chip{font-family:'Oswald';font-weight:600;font-size:8pt;letter-spacing:.12em;text-transform:uppercase;
  color:var(--paper);border:1px solid var(--goldline);border-radius:99px;padding:1.6mm 3.5mm}
.card{border:1px solid var(--line);background:var(--panel);border-radius:2mm;padding:5mm 5.5mm}
.card h3{font-family:'Oswald';font-weight:700;font-size:9.5pt;letter-spacing:.14em;
  text-transform:uppercase;color:var(--gold);margin-bottom:1.8mm}
.card p{font-size:9.5pt;color:var(--muted);line-height:1.5}
.moment{display:grid;grid-template-columns:repeat(3,1fr);gap:4mm}
.prow{display:grid;grid-template-columns:repeat(5,1fr);gap:4mm}
.prow.main{grid-template-columns:repeat(5,1fr);gap:3mm}
.pcardx{border:1px solid var(--line);background:var(--panel);border-radius:2mm;padding:4mm 3mm;
  display:flex;flex-direction:column;align-items:center;gap:2mm;justify-content:center}
.pcardx img{max-height:12mm;max-width:85%;object-fit:contain}
.pcardx span{font-family:'Oswald';font-weight:500;font-size:7pt;letter-spacing:.08em;color:var(--gold)}
.pcardx i{font-style:normal;font-size:7pt;color:var(--muted);text-align:center;line-height:1.35}
.prow.main .pcardx{padding:4mm 2mm;gap:1.8mm}
.prow.main .pcardx img{max-height:11mm;max-width:88%}
.prow.main .pcardx span{font-size:6.5pt;letter-spacing:.04em}
.prow.main .pcardx i{font-size:6.5pt}
"""

    main_cards = "".join(
        f'<div class="pcardx"><img src="{IMG}/{f}"><span>{h}</span>' + (f'<i>{r}</i>' if r else '') + '</div>'
        for f, h, r in PARTNERS)
    supp_cards = "".join(
        f'<div class="pcardx"><img src="{IMG}/{f}"><span>{h}</span></div>'
        for f, h in SUPPORTERS)

    body = f"""
<div class="page">
  <div class="rule">The Bigger Picture</div>
  <div class="sub">Why women&rsquo;s rugby, why now</div>
  <p class="numlab" style="margin-top:2mm">Current partners</p>
  <div class="prow main">{main_cards}</div>
  <p class="numlab">Supporting partners</p>
  <div class="prow">{supp_cards}</div>
  <p class="numlab">The Moment</p>
  <div class="moment">
    <div class="card"><h3>The Red Roses are world champions</h3><p>England won the 2025 Rugby
    World Cup on home soil, and the women&rsquo;s game is growing faster than ever &mdash; on the
    pitch and online.</p></div>
    <div class="card"><h3>The game has gone professional</h3><p>England&rsquo;s top-flight players
    now earn full-time salaries &mdash; the Championship is where the next generation proves
    itself.</p></div>
    <div class="card"><h3>The Championship is watchable</h3><p>Matches stream live online, so
    partners get real, visible exposure &mdash; not just a logo on a shirt nobody sees.</p></div>
  </div>
  <p class="numlab">Where Your Support Goes</p>
  <p class="lede">Even at Championship level, the women&rsquo;s game is largely unpaid &mdash; clubs
  actively encourage players to secure sponsors. Training in Thurrock two to three nights a week
  plus weekend fixtures, alongside full-time education, comes with real costs.</p>
  <div class="chips">
    <span class="chip">Travel &amp; Transport</span><span class="chip">Kit &amp; Recovery</span>
    <span class="chip">Matchday Costs</span><span class="chip">Athlete Development</span>
  </div>
  <div class="pfoot"><span>Tia Tandy &mdash; Partnership Programme 2026/27</span><span>06 / 07</span></div>
</div>"""
    return f"<!DOCTYPE html><html><head><meta charset='utf-8'><style>{css}</style></head><body>{body}</body></html>"


def splice(page_pdf: pathlib.Path):
    from pypdf import PdfReader, PdfWriter
    pack = PdfReader(str(PACK))
    new_page = PdfReader(str(page_pdf))
    assert len(pack.pages) == 7 and len(new_page.pages) == 1
    out = PdfWriter()
    for i, pg in enumerate(pack.pages):
        out.add_page(new_page.pages[0] if i == 5 else pg)
    with open(PACK, "wb") as f:
        out.write(f)
    print(f"spliced page 6 into {PACK} ({PACK.stat().st_size} bytes)")


if __name__ == "__main__":
    if sys.argv[1] == "--splice":
        splice(pathlib.Path(sys.argv[2]))
    else:
        font_dir, work_dir = pathlib.Path(sys.argv[1]), pathlib.Path(sys.argv[2])
        html = build_html(font_dir)
        dest = work_dir / "p6.html"
        dest.write_text(html)
        print(f"wrote {dest} ({len(html)} bytes)")
