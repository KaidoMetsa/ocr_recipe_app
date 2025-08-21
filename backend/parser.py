import re
from typing import Dict

SECTION_RE = re.compile(r"(?im)^(nimi|title)\s*[:=-]\s*(.*)$")
ING_RE = re.compile(r"(?is)^(koostisosad|ingredients)\s*[:=-]?\s*(.*?)^(valmistamine|steps|juhend)\s*[:=-]?", re.M)
STEPS_RE = re.compile(r"(?is)^(valmistamine|steps|juhend)\s*[:=-]?\s*(.*)$")

# Fallback kui pealkirja eraldi pole
FIRST_LINE_TITLE_RE = re.compile(r"^(.{3,80})$")

def parse_recipe(text: str) -> Dict[str, str]:
    out = {"title": "", "ingredients": "", "steps": ""}

    # title
    m_title = SECTION_RE.search(text)
    if m_title:
        out["title"] = m_title.group(2).strip()
    else:
        # võta esimene mitte-tühi rida pealkirjaks
        for line in text.splitlines():
            line = line.strip()
            if line:
                out["title"] = line[:80]
                break

    m_ing = ING_RE.search(text + "\nvalmistamine:")
    if m_ing:
        out["ingredients"] = re.sub(r"\n{2,}", "\n", m_ing.group(2).strip())
    m_steps = STEPS_RE.search(text)
    if m_steps:
        out["steps"] = re.sub(r"\n{2,}", "\n", m_steps.group(2).strip())

    return out
