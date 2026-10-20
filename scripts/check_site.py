"""Check built pages, local assets and archive isolation after a Jekyll build."""
import sys
from pathlib import Path
from html.parser import HTMLParser
from urllib.parse import urlsplit, unquote, urljoin
root = Path(sys.argv[1]).resolve()
class Page(HTMLParser):
    def __init__(self):
        super().__init__(); self.links = []
    def handle_starttag(self, tag, attrs):
        for key, value in attrs:
            if key in ('href', 'src') and value:
                self.links.append(value.strip())
errors = []
files = list(root.rglob('*.html'))
for path in files:
    relative = path.relative_to(root).as_posix()
    text = path.read_text()
    if '{{' in text or '{%' in text:
        errors.append(f'{relative}: unrendered Liquid')
    parser = Page(); parser.feed(text)
    for link in parser.links:
        url = urlsplit(link)
        if url.scheme or url.netloc or not url.path:
            continue
        resolved = unquote(urlsplit(urljoin('/' + relative, link)).path)
        target = root / resolved.lstrip('/')
        if not target.is_file() and not (target / 'index.html').is_file():
            errors.append(f'{relative}: missing {link}')
        if relative.startswith('2025/') and resolved not in ('/', '/2025') and not resolved.startswith('/2025/'):
            errors.append(f'{relative}: escapes archive: {link}')
for route in ('index.html', 'program/index.html', 'speakers/index.html', 'organizers/index.html', 'cfp/index.html', 'submission/index.html', 'previous-workshops/index.html', '2025/index.html'):
    if not (root / route).is_file(): errors.append(f'Missing page: {route}')
organizers = (root / 'organizers/index.html').read_text()
assert organizers.count('class="organizer-photo"') == 6, 'Expected six organizer portraits'
assert '<fieldset disabled>' in (root / '2025/submission/index.html').read_text()
assert '<form' not in (root / 'submission/index.html').read_text()
if errors:
    print('\n'.join(errors)); sys.exit(1)
print(f'PASS: {len(files)} HTML pages; local links/assets resolve; archive links stay within 2025; six organizer portraits; submissions closed.')
