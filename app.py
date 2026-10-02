import html

import streamlit as st

from unit1.page0 import page0_content as u10
from unit1.page1 import page1_content as u11
from unit1.page2 import page2_content as u12
from unit1.page3 import page3_content as u13
from unit1.page4 import page4_content as u14
from unit1.page5 import page5_content as u15
from unit1.page6 import page6_content as u16
from unit1.page7 import page7_content as u17
from unit1.page8 import page8_content as u18

from unit2.page0 import page0_content as u20
from unit2.page1 import page1_content as u21
from unit2.page2 import page2_content as u22
from unit2.page3 import page3_content as u23
from unit2.page4 import page4_content as u24
from unit2.page5 import page5_content as u25

from unit3.page0 import page0_content as u30
from unit3.page1 import page1_content as u31
from unit3.page2 import page2_content as u32

from paper_summary.page0 import page0_content as up0

from unit4.page0 import page0_content as u40
from unit4.page1 import page1_content as u41
from unit4.page2 import page2_content as u42
from unit4.page3 import page3_content as u43
from unit4.page4 import page4_content as u44
from unit4.page5 import page5_content as u45
from unit4.page6 import page6_content as u46

from unit5.page0 import page0_content as u50
from unit5.page1 import page1_content as u51
from unit5.page2 import page2_content as u52
from unit5.page3 import page3_content as u53
from unit5.page4 import page4_content as u54

from unit6.page0 import page0_content as u60
from unit6.page1 import page1_content as u61
from unit6.page2 import page2_content as u62
from unit6.page3 import page3_content as u63

from data_analysis_activity.page0 import page0_content as ud0

from unit7.page0 import page0_content as u70

from unit8.page0 import page0_content as u80
from unit8.page1 import page1_content as u81
from unit8.page2 import page2_content as u82

from unit9.page0 import page0_content as u90


# Course structure: (unit title, [(page title, page function), ...]) in teaching order
UNITS = [
    ("Introduction to Conservation Biology", [
        ("What is the most important environmental issue?", u10),
        ("Human Population Growth", u11),
        ("Population Clock", u12),
        ("Ecological Footprints", u13),
        ("Ecological Footprint by Land Type", u14),
        ("What is your Ecological Footprint?", u15),
        ("Key People in Early Conservation Biology", u16),
        ("Terms for Discussion", u17),
        ("Organizational Values", u18),
    ]),
    ("Biodiversity", [
        ("Introduction", u20),
        ("Patterns of Biodiversity", u21),
        ("Identifying Species", u22),
        ("Quantifying Biodiversity", u23),
        ("Genetic Diversity", u24),
        ("Trophic Dynamics", u25),
    ]),
    ("Valuing Biodiversity", [
        ("Ecosystem Services", u30),
        ("Valuation Activity", u31),
        ("Environmental Ethics", u32),
    ]),
    ("Paper Summary 1", [
        ("Discussion", up0),
    ]),
    ("Threats to Biodiversity", [
        ("Biomes", u40),
        ("Group Activity", u41),
        ("Threats to Species", u42),
        ("Habitat Fragmentation", u43),
        ("Biomagnification", u44),
        ("Effects of Climate Change (Phenology)", u45),
        ("Invasive Species", u46),
    ]),
    ("Extinction", [
        ("Major Terms", u50),
        ("Vulnerability", u51),
        ("Island Biogeography", u52),
        ("Species–Area Curve", u53),
        ("Small Populations", u54),
    ]),
    ("Protecting Species", [
        ("Applied Conservation", u60),
        ("IUCN Red List", u61),
        ("Conservation Priorities", u62),
        ("Conservation Laws", u63),
    ]),
    ("Data Analysis Activity", [
        ("Using GBIF", ud0),
    ]),
    ("New Populations and Ex Situ Conservation", [
        ("Establishing New Populations", u70),
    ]),
    ("Protected Areas", [
        ("Terrestrial and Marine Protected Areas", u80),
        ("Protected Area Management", u81),
        ("Design a Protected Area", u82),
    ]),
    ("Restoration", [
        ("Restoration Ecology", u90),
    ]),
]

HOME = "Home"
HERO_IMAGE = ("https://images.unsplash.com/photo-1525382455947-f319bc05fb35"
              "?q=80&w=1200&auto=format&fit=crop")

# One-line summary per unit, in the same order as UNITS
DESCRIPTIONS = [
    "Why conservation matters: human population growth, ecological footprints, and the field's founders and values.",
    "What biodiversity is, where it is found, and how it is measured, from genes to food webs.",
    "Ecosystem services, putting a value on nature, and environmental ethics.",
    "Class discussion of a research paper on aquatic insects in urban streams.",
    "Habitat loss and fragmentation, pollution, climate change, and invasive species.",
    "What makes species vulnerable, island biogeography, and the problems of small populations.",
    "The IUCN Red List, setting conservation priorities, and conservation law.",
    "Hands-on exploration of real species occurrence records from GBIF.",
    "Reintroductions, translocations, and other ways to establish new populations.",
    "How terrestrial and marine protected areas are designed and managed.",
    "Ecological succession and how degraded ecosystems are restored.",
]
# Paradise palette accents, cycled across unit cards
ACCENTS = ["#8c977d", "#8da3b9", "#d9bc8c", "#a988b0", "#8aa6a2", "#d18a8d"]

st.set_page_config(page_title="Conservation Biology", layout="wide", page_icon="assets/panda_icon.png")

st.markdown("""
    <style>
        #MainMenu {visibility: hidden;}
        .stDeployButton {visibility: hidden;}
        footer {visibility: hidden;}
        #stDecoration {display: none;}

        .cb-hero {display: grid; grid-template-columns: 1.5fr 1fr; gap: 2.5rem; align-items: center;
                  margin: 0.5rem 0 2.5rem;}
        .cb-eyebrow {color: #8c977d; font-size: 0.78rem; font-weight: 700; letter-spacing: 0.14em;
                     text-transform: uppercase; margin-bottom: 0.4rem;}
        .cb-hero h1 {font-size: 3rem; line-height: 1.05; margin: 0 0 0.8rem; padding: 0;}
        .cb-lede {color: #b8b0b0; font-size: 1.08rem; line-height: 1.6; margin-bottom: 1.4rem;}
        .cb-byline {color: #958d8d; font-size: 0.92rem; margin-bottom: 1.4rem;}
        .cb-byline a {color: #8da3b9;}
        .cb-btn {display: inline-block; background: #d9bc8c; color: #151515 !important; font-weight: 700;
                 padding: 0.7rem 1.4rem; border-radius: 999px; text-decoration: none !important;}
        .cb-btn:hover {background: #e6cfa6;}
        .cb-photo {width: 100%; aspect-ratio: 4 / 3; object-fit: cover; border-radius: 16px;
                   border: 1px solid #2e2e2e;}

        .cb-section {display: flex; align-items: baseline; justify-content: space-between;
                     margin: 0 0 1rem; border-bottom: 1px solid #2e2e2e; padding-bottom: 0.6rem;}
        .cb-section h2 {margin: 0; padding: 0; font-size: 1.6rem;}
        .cb-section span {color: #958d8d; font-size: 0.9rem;}

        .cb-grid {display: grid; grid-template-columns: repeat(auto-fill, minmax(260px, 1fr)); gap: 1rem;}
        a.cb-card {position: relative; display: flex; flex-direction: column; gap: 0.5rem;
                   background: #1d1d1d; border: 1px solid #2e2e2e; border-radius: 14px;
                   padding: 1.3rem 1.3rem 1.1rem; text-decoration: none !important; color: #e8e3e3 !important;
                   overflow: hidden; transition: transform 0.15s, border-color 0.15s, background 0.15s;}
        a.cb-card::before {content: ""; position: absolute; inset: 0 0 auto 0; height: 4px; background: var(--accent);}
        a.cb-card:hover {transform: translateY(-3px); border-color: var(--accent); background: #222222;}
        .cb-num {font-size: 2.2rem; font-weight: 800; line-height: 1; color: var(--accent);}
        .cb-title {font-size: 1.12rem; font-weight: 700; line-height: 1.3;}
        .cb-desc {color: #b8b0b0; font-size: 0.92rem; line-height: 1.5; flex: 1;}
        .cb-meta {display: flex; justify-content: space-between; align-items: center; margin-top: 0.4rem;
                  padding-top: 0.7rem; border-top: 1px solid #2a2a2a; font-size: 0.82rem; color: #958d8d;}
        .cb-open {color: var(--accent); font-weight: 700;}

        .cb-a0 {--accent: #8c977d;}
        .cb-a1 {--accent: #8da3b9;}
        .cb-a2 {--accent: #d9bc8c;}
        .cb-a3 {--accent: #a988b0;}
        .cb-a4 {--accent: #8aa6a2;}
        .cb-a5 {--accent: #d18a8d;}

        @media (max-width: 800px) {
            .cb-hero {grid-template-columns: 1fr;}
            .cb-hero h1 {font-size: 2.3rem;}
        }
    </style>
""", unsafe_allow_html=True)


def unit_label(index, title):
    return f"{index}. {title}"


def home():
    cards = []
    for i, ((title, pages), desc) in enumerate(zip(UNITS, DESCRIPTIONS), start=1):
        n = len(pages)
        cards.append(
            f'<a class="cb-card cb-a{(i - 1) % len(ACCENTS)}" href="?unit={i}" target="_self">'
            f'<div class="cb-num">{i:02d}</div>'
            f'<div class="cb-title">{html.escape(title)}</div>'
            f'<div class="cb-desc">{html.escape(desc)}</div>'
            f'<div class="cb-meta"><span>{n} {"page" if n == 1 else "pages"}</span>'
            f'<span class="cb-open">Open →</span></div></a>'
        )
    st.markdown(f"""
<div class="cb-hero">
  <div>
    <div class="cb-eyebrow">Interactive course site</div>
    <h1>Conservation Biology</h1>
    <div class="cb-lede">Lessons, class activities, data exercises, and simulations covering biodiversity,
      the threats it faces, and the tools used to protect and restore it.</div>
    <div class="cb-byline">Matthew J. Lundquist, Ph.D. · <a href="https://lundquistecology.com">lundquistecology.com</a></div>
    <a class="cb-btn" href="?unit=1" target="_self">Start with Unit 1 →</a>
  </div>
  <img class="cb-photo" src="{HERO_IMAGE}" alt="Giant panda eating bamboo">
</div>
<div class="cb-section"><h2>Units</h2><span>{len(UNITS)} units · {sum(len(p) for _, p in UNITS)} pages</span></div>
<div class="cb-grid">{''.join(cards)}</div>
""", unsafe_allow_html=True)


# ---------- Sidebar navigation ----------
st.sidebar.title("Conservation Biology")
labels = [HOME] + [unit_label(i, t) for i, (t, _) in enumerate(UNITS, start=1)]

# ?unit=N opens that unit (used by the home-page cards and for linking students to a unit)
try:
    start = int(st.query_params.get("unit", 0))
except ValueError:
    start = 0
if not 0 <= start <= len(UNITS):
    start = 0

choice = st.sidebar.selectbox("Unit", labels, index=start)
idx = labels.index(choice)
if idx:
    st.query_params["unit"] = str(idx)
elif "unit" in st.query_params:
    del st.query_params["unit"]

if choice == HOME:
    home()
else:
    title, pages = UNITS[idx - 1]
    if len(pages) == 1:
        page_title, page_fn = pages[0]
    else:
        page_title = st.sidebar.radio("Page", [p for p, _ in pages])
        page_fn = dict(pages)[page_title]
    page_fn()

st.sidebar.divider()
st.sidebar.caption("Matthew J. Lundquist, Ph.D. · [lundquistecology.com](https://lundquistecology.com)")
