# Editing the workshop website

Open the website folder in your usual text editor. Use its Find command to search
for the visible text or the capitalized section comments described below. Save
the file and preview the page. Content is ordinary HTML; the existing Jekyll
includes reuse dates, contacts, institution logos and session descriptions.

## Where to make each change

| What you want to change | File | Search for |
| --- | --- | --- |
| Header logo and official conference link | [_layouts/default.html](../_layouts/default.html) | `CONFERENCE LOGO` |
| Visible workshop title and subtitle | [_layouts/default.html](../_layouts/default.html) | `WORKSHOP TITLE / SUBTITLE` |
| Navigation labels and destinations | [_layouts/default.html](../_layouts/default.html) | `NAVIGATION` |
| Browser-tab title and search description | [_config.yml](../_config.yml) | `SITE METADATA` |
| Home illustration, venue, date and time | [index.html](../index.html) | `HOME` or `EVENT DETAILS` |
| Home introduction and application domains | [index.html](../index.html) | `INTRODUCTION` or `DOMAIN 01` |
| Important Dates on Home and Call for Papers | [_includes/dates.html](../_includes/dates.html) | The date's visible label |
| Program introduction, date and time | [program.html](../program.html) | `PROGRAM INTRODUCTION` |
| Agenda order, times and session titles | [program.html](../program.html) | `AGENDA`, `OPENING`, `DOMAIN 01`, `LUNCH`, etc. |
| Repeated academic/practitioner/debate descriptions | [_includes/session-format.html](../_includes/session-format.html) | `SESSION FORMAT` |
| Individual speaker names, affiliations and talks | [speakers.html](../speakers.html) | `SPEAKER 1.1` through `SPEAKER 3.3` |
| Organizer portraits, biographies and profile links | [organizers.html](../organizers.html) | `ORGANIZER:` followed by the name |
| Awards, abstract requirements, topics and submission link | [cfp.html](../cfp.html) | `AWARDS`, `SUBMISSION INSTRUCTIONS` or `TOPICS` |
| Submission status and link on the Submissions page | [submission.html](../submission.html) | `SUBMISSION STATUS` |
| Contact names and email addresses | [_includes/contact.html](../_includes/contact.html) | `CONTACTS` |
| Footer institution logos and links | [_includes/institutions.html](../_includes/institutions.html) | `FOOTER INSTITUTIONS` |
| Summary and links for the first edition | [previous-workshops.html](../previous-workshops.html) | `FIRST EDITION` |
| Colors, fonts, spacing and responsive layout | [public/css/edition-2027.css](../public/css/edition-2027.css) | Numbered section headings |

## Editing text and links

Change the text between HTML tags. Keep the surrounding tags and `class` values
when you want to preserve the appearance. For a link, `href` is the destination
and the text between `<a>` and `</a>` is what visitors see.

The small block between `---` lines at the top of each page is its Jekyll setup:

- `layout` selects the shared page layout.
- `title` supplies the page's browser-tab title.
- `permalink` sets its public address. Keep it unchanged unless moving the page.

Lines such as `{% include dates.html %}` insert a shared file from `_includes/`.
Edit that shared file to update every page using it. Image paths and internal
links use `{{ '/path/' | relative_url }}`; change the quoted path and keep the
surrounding syntax.

HTML comments (`<!-- ... -->`) are editing notes and do not appear on the page.
Use `&amp;` when writing an ampersand in HTML text.

## Dates and submission status

In `_includes/dates.html`, each `<dt>` is a label and the following `<dd>` is its
date. For example, replace `<dd>TBD</dd>` with the confirmed date. This updates
both Home and Call for Papers.

The workshop's own event date and time are separate from the submission dates.
Update them in both `index.html` and `program.html`. When opening submissions,
also update the status and link in `cfp.html` and `submission.html`. Search for
`TBD` and `pending` to find other details awaiting confirmation.

## Agenda sessions

Each session is a complete `<section class="agenda-row ...">` block in
`program.html`, introduced by a comment naming the session. Blocks appear in
the same order as the agenda.

- Change `<div class="agenda-time">TBD</div>` to set a session's time.
- Edit the `eyebrow` text for its category and the `<h2>` for its title.
- Move or copy the entire section, including its closing `</section>`, to
  reorder sessions or add one.
- Keep `agenda-break` on coffee/lunch rows to retain their background.
- The three domain sessions include `_includes/session-format.html`. Editing
  that file changes the common format text in all three sessions.

## Speakers and organizers

Each speaker now has an independent HTML block in `speakers.html`. Search for
its domain and role, such as `SPEAKER 2.1: Academic perspective`. Edit the name
in `<h3>`, the affiliation, the talk title and the abstract within that block.
There is no speaker-generation loop to change.

The portrait placeholder is the `speaker-placeholder` div containing an SVG.
When adding a portrait, replace that entire div with an image, for example:

```html
<img class="speaker-placeholder" src="{{ '/images/speaker-name.jpg' | relative_url }}" alt="Speaker Name" width="126" height="140" loading="lazy" style="object-fit: cover;">
```

Put the actual image in `images/` and update the filename and name. This example
keeps the existing responsive portrait dimensions and crops the image to fit.

Organizer blocks in `organizers.html` follow the same pattern. Update the
portrait's `src` and `alt`, the name, affiliation, biography and profile link
together. For contact addresses, edit both the displayed email and the `mailto:`
link in `_includes/contact.html`.

## Appearance

`public/css/edition-2027.css` is the stylesheet for the current workshop. Its
numbered sections follow the main components: header, navigation, Home, dates,
contacts, footer, Call for Papers, previous workshops, program, speakers and
organizers. The final sections cover screen widths and reduced motion.

- The `:root` block at the top defines shared colors and the sans-serif font.
- `--paper` is the warm background used by Important Dates and the domain rows.
- Header logo widths are in `.conference-logo img`; its grid column is in
  `.masthead`. Check their tablet and phone rules too when changing the size.
- `h1, .agenda-title` controls the shared Workshop Program / Agenda heading style.
- Rules inside `@media` apply only under the stated screen-width condition.
  Check desktop and mobile after changing layout or font sizes.

After a visual CSS change, increase the `v=` value on the stylesheet link in
`_layouts/default.html` so returning visitors load the updated styling.

## Preview and publish

Run these existing project commands from the website folder. The first installs
the dependencies; you only need it when setting up the project or changing them.

```sh
bundle install
bundle exec jekyll serve --disable-disk-cache
```

Open the local address printed by Jekyll. Stop the preview with Ctrl+C.
For the existing build and local-link checks:

```sh
bundle exec jekyll build --destination /tmp/building-safe-robots-check --disable-disk-cache
python3 scripts/check_site.py /tmp/building-safe-robots-check
```

Review the changes in your usual Git application, commit them, and push to this
repository's `master` branch to publish through GitHub Pages. Check the Pages
deployment and the live site after publishing.

## Older files

`2025/` is the frozen first-edition website with its own assets. It does not use
the current workshop's layout or stylesheet.

The files named `index (copy 1).html`, `_layouts/default (copy 1).html`, the old
`_includes/head.html` / `sidebar.html`, and the older `poole.css`, `lanyon.css`
and `syntax.css` are legacy sources. The current pages use
`_layouts/default.html` and `public/css/edition-2027.css`; start there for current
header and styling changes. Historical files have been retained.
