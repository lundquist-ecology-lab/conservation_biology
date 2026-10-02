"""Build-time patch: give Streamlit's static index.html a real <title>, description,
link-preview (Open Graph) tags, a canonical URL, and a real <noscript> message, so
search results and link previews don't show "Streamlit" / "You need to enable JavaScript"."""
import html
import os
import pathlib

import streamlit

title = os.environ["SITE_TITLE"]
desc = os.environ["SITE_DESCRIPTION"]
url = os.environ["SITE_URL"]

index = pathlib.Path(streamlit.__file__).parent / "static" / "index.html"
page = index.read_text()
t, d, u = html.escape(title), html.escape(desc), html.escape(url)
head = (f"<title>{t}</title>"
        f'<meta name="description" content="{d}">'
        f'<link rel="canonical" href="{u}">'
        f'<meta property="og:title" content="{t}">'
        f'<meta property="og:description" content="{d}">'
        f'<meta property="og:url" content="{u}">'
        f'<meta property="og:type" content="website">')
assert "<title>Streamlit</title>" in page, "unexpected Streamlit index.html"
noscript_old = "<noscript>You need to enable JavaScript to run this app.</noscript>"
noscript_new = (f"<noscript><h1>{t}</h1><p>{d}</p>"
                "<p>This interactive site needs JavaScript enabled.</p></noscript>")
page = page.replace("<title>Streamlit</title>", head, 1).replace(noscript_old, noscript_new, 1)
index.write_text(page)
print("patched", index)
