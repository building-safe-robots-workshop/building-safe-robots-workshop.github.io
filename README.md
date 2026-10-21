# Building Safe Robots workshops

GitHub Pages source for https://building-safe-robots-workshop.github.io/.
Repository: building-safe-robots-workshop/building-safe-robots-workshop.github.io.

The root site is the proposed ICRA 2027 2nd workshop. Acceptance, date, speakers,
schedule, submission details and sponsorship remain pending. Update these only
when confirmed by the organizers.

## Editing the website

Start with [the manual editing guide](docs/editing.md). It maps visible sections
to their source files and shows how to edit dates, agenda sessions, speakers,
organizers, images and styles. The HTML contains searchable section comments.
Each speaker and agenda session has its own editable block.

Most content changes need only a text editor: open the relevant HTML file, find
the visible text, and edit it. No new tools or dependencies are needed.

## Local preview and checks

```sh
bundle install
bundle exec jekyll serve --disable-disk-cache
```

```sh
bundle exec jekyll build --destination /tmp/building-safe-robots-check --disable-disk-cache
python3 scripts/check_site.py /tmp/building-safe-robots-check
```

The existing GitHub Pages publishing configuration uses the master branch.
Push only to the workshop repository; verify `git remote -v` before publishing.

## First edition archive

`2025/` is a frozen static build of revision
`32296a9a3ad447920c09dce2ef6297529e951777`, generated before the second-edition edits.
It carries its own images, CSS and JavaScript so changes to the main site do not
restyle the archive. Local links were rewritten to `/2025/`; a current-edition
link and archive notice were added. The old submission form and upload links are
inactive. Original program, speakers, organizers and sponsor content are retained.

Keep archive content independent of the current layouts and configuration.
The original 2025 working folder has also been left unchanged.

## Organizer portraits

Existing Luis Figueredo and Robin Kirschner portraits were retained. Additional
portraits were sourced on 20 October 2026 from:

- Marta Lagomarsino: https://www.iit.it/people-details/-/people/marta-lagomarsino
- Eugene Kim: https://kim3957.github.io/ (`images/kim.png`)
- Yue Hu: https://uwaterloo.ca/mechanical-mechatronics-engineering/profile/y526hu
- Karol Janik: https://www.engineeringdesignshow.co.uk/2026-conference-programme

Affiliations and short biographies follow the organizer-supplied proposal; Marta's
IIT affiliation was checked against her institutional profile. Profile links on
the organizers page provide contact details.

## 2027 design

Current pages use `public/css/edition-2027.css`; the 2025 snapshot keeps its
original layout and assets. Shared dates, contacts and institution logos live
in `_includes/`. Nine speaker placeholders are grouped into three domain blocks.
The conference logo links directly to the official ICRA 2027 website.

Content and asset provenance, including the generated Seoul illustration prompt,
are recorded in [docs/design-sources.md](docs/design-sources.md).
