import re
import unittest
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import urlparse


ROOT = Path(__file__).resolve().parents[1]
PAGES = [ROOT / name for name in ("index.html", "programs.html", "about.html")]
REGISTRATION = "https://docs.google.com/forms/d/14PnXpYQUP97Et9Dmm6wtJTy2VGmZW26QRzHvjv-3hZg/viewform"
CONTACTS = {
    "mailto:info@minhaajlearningcenter.com",
    "tel:+15713103119",
    "https://maps.google.com/?q=5531+Hempstead+Way+Springfield+VA+22151",
}
VOID_ELEMENTS = {"area", "base", "br", "col", "embed", "hr", "img", "input", "link", "meta", "param", "source", "track", "wbr"}


class Element:
    def __init__(self, tag, attrs=None, parent=None):
        self.tag = tag
        self.attrs = dict(attrs or [])
        self.parent = parent
        self.children = []
        self.text = []

    def descendants(self, tag=None):
        for child in self.children:
            if tag is None or child.tag == tag:
                yield child
            yield from child.descendants(tag)

    def content(self):
        return " ".join(self.text + [child.content() for child in self.children]).strip()


class Document(HTMLParser):
    def __init__(self):
        super().__init__()
        self.root = Element("document")
        self.current = self.root

    def handle_starttag(self, tag, attrs):
        element = Element(tag, attrs, self.current)
        self.current.children.append(element)
        if tag not in VOID_ELEMENTS:
            self.current = element

    def handle_startendtag(self, tag, attrs):
        self.handle_starttag(tag, attrs)

    def handle_endtag(self, tag):
        cursor = self.current
        while cursor is not self.root and cursor.tag != tag:
            cursor = cursor.parent
        if cursor is not self.root:
            self.current = cursor.parent

    def handle_data(self, data):
        if data.strip():
            self.current.text.append(data.strip())


def parse(path):
    document = Document()
    document.feed(path.read_text(encoding="utf-8"))
    return document.root


def elements_with(root, attribute):
    return [element for element in root.descendants() if attribute in element.attrs]


class StaticSiteMatrixTests(unittest.TestCase):
    def test_home_hero_contains_registration_action(self):
        root = parse(ROOT / "index.html")
        main = next(root.descendants("main"))
        hero = next(child for child in main.children if child.tag == "section")
        hero_links = [link.attrs.get("href") for link in hero.descendants("a")]
        self.assertIn(REGISTRATION, hero_links, "index.html: hero registration action missing")

    def test_mobile_navigation_is_scoped_and_progressive(self):
        for page in PAGES:
            root = parse(page)
            menus = [element for element in elements_with(root, "data-mobile-menu") if element.tag == "details"]
            self.assertEqual(len(menus), 1, f"{page.name}: expected one details mobile menu")
            menu = menus[0]
            summaries = list(menu.descendants("summary"))
            self.assertEqual(len(summaries), 1, f"{page.name}: mobile menu trigger missing")
            self.assertEqual(summaries[0].attrs.get("aria-label"), "Open navigation menu", page.name)
            self.assertEqual(summaries[0].attrs.get("aria-expanded"), "false", page.name)
            mobile_navs = [nav for nav in menu.descendants("nav") if nav.attrs.get("aria-label") == "Mobile navigation"]
            self.assertEqual(len(mobile_navs), 1, f"{page.name}: mobile navigation not inside details")
            destinations = [link.attrs.get("href") for link in mobile_navs[0].descendants("a")]
            self.assertEqual(destinations[:3], ["./index.html", "./programs.html", "./about.html"], page.name)
            self.assertIn(REGISTRATION, destinations, page.name)

    def test_shared_chrome_and_contact_contracts(self):
        for page in PAGES:
            root = parse(page)
            favicon = [link for link in root.descendants("link") if link.attrs.get("rel") == "icon"]
            self.assertEqual(len(favicon), 1, f"{page.name}: favicon metadata missing")
            self.assertEqual(favicon[0].attrs.get("href"), "./assets/icon.png", page.name)
            footer = next(root.descendants("footer"))
            footer_links = {link.attrs.get("href") for link in footer.descendants("a")}
            self.assertTrue(CONTACTS.issubset(footer_links), f"{page.name}: canonical footer contacts missing")
            years = [element for element in elements_with(footer, "data-current-year")]
            self.assertEqual(len(years), 1, f"{page.name}: current-year hook missing")
            self.assertEqual(years[0].content(), "2026", f"{page.name}: static fallback year missing")
            blank_links = [link for link in root.descendants("a") if link.attrs.get("target") == "_blank"]
            self.assertTrue(blank_links, f"{page.name}: expected external links")
            for link in blank_links:
                rel_tokens = set(link.attrs.get("rel", "").split())
                self.assertTrue({"noopener", "noreferrer"}.issubset(rel_tokens), f"{page.name}: unsafe new tab")
                self.assertIn("opens in a new tab", link.content(), f"{page.name}: new-tab disclosure missing")

    def test_every_registration_action_uses_canonical_destination(self):
        for page in PAGES:
            root = parse(page)
            registration_links = [
                link for link in root.descendants("a")
                if "register" in link.content().casefold() or "registration" in link.content().casefold()
            ]
            self.assertTrue(registration_links, f"{page.name}: registration action missing")
            for link in registration_links:
                self.assertEqual(link.attrs.get("href"), REGISTRATION, f"{page.name}: incorrect registration destination")

    def test_inventory_content_is_preserved(self):
        required = {
            "index.html": [
                "affordable education without compromising quality", "Qur'an recitation and memorization",
                "low teacher-to-student ratios", "multi-ethnic Muslim community", "pride in Muslim identity",
            ],
            "programs.html": [
                "Three-hour sessions", "seven levels", "juzu' Amma", "Knowledge Retreats", "Creed of at-Tahawiyy",
                "Islamic Manners", "Tafseer", "Islamic History", "Hadith", "Balaghah",
            ],
            "about.html": [
                "“Minhaaj” means “clear path", "traditional, authentic knowledge", "مَنْ سَلَكَ طَرِيْقًا",
                "path to Paradise", "face-to-face education", "Muslims of all ages",
            ],
        }
        for name, phrases in required.items():
            html = (ROOT / name).read_text(encoding="utf-8")
            for phrase in phrases:
                self.assertIn(phrase.casefold(), html.casefold(), f"{name}: required inventory content missing: {phrase}")

    def test_arabic_is_isolated_as_rtl_content(self):
        root = parse(ROOT / "about.html")
        arabic = [element for element in root.descendants() if element.attrs.get("lang") == "ar"]
        self.assertTrue(any(element.attrs.get("dir") == "rtl" for element in arabic))

    def test_all_static_local_references_resolve(self):
        for page in PAGES:
            root = parse(page)
            tags = {element.tag for element in root.descendants()}
            self.assertTrue({"header", "main", "footer", "nav"}.issubset(tags), page.name)
            references = [element.attrs.get("href") for element in root.descendants() if element.tag in {"a", "link"}]
            references += [element.attrs.get("src") for element in root.descendants("img")]
            references += [element.attrs.get("src") for element in root.descendants("script")]
            for reference in filter(None, references):
                parsed = urlparse(reference)
                if parsed.scheme or reference.startswith(("#", "mailto:", "tel:")):
                    continue
                target = (page.parent / parsed.path).resolve()
                self.assertTrue(target.is_file(), f"{page.name}: missing local asset {reference}")

    def test_compiled_css_contains_scoped_accessibility_rules(self):
        css = (ROOT / "assets/css/styles.css").read_text(encoding="utf-8")
        self.assertRegex(css, r"--color-gold-600:#76500f", "functional gold contrast token missing")
        reduced = re.search(r"@media\s*\(prefers-reduced-motion:reduce\)\s*\{(.+)\}\s*@property", css)
        self.assertIsNotNone(reduced, "compiled reduced-motion media query missing")
        rules = reduced.group(1)
        self.assertRegex(rules, r"html\{scroll-behavior:auto\}", "reduced-motion html rule missing")
        self.assertRegex(rules, r"\*,:before,:after\{[^}]*transition-duration:.01ms!important", "transition override is not scoped to elements")
        self.assertRegex(rules, r"\*,:before,:after\{[^}]*animation-duration:.01ms!important", "animation override is not scoped to elements")
        for page in PAGES:
            html = page.read_text(encoding="utf-8")
            self.assertNotIn("cdn.tailwindcss.com", html)
            self.assertNotIn("@tailwindcss/browser", html)


if __name__ == "__main__":
    unittest.main()
