# tia-tandy-rugby

Website for Tia Tandy, an 18-year-old dual-code rugby hooker from
Dartford (tiatandyrugby.com). No build step, no dependencies. Two
versions are maintained, with no links between them:

- **The public site** — multi-page, black-and-gold, served at the
  domain root: `public/index.html`, `bio.html`, `union/`, `league/`,
  `achievements`, `pictures`, `sponsors`, `my-rugby-life`, `videos`,
  plus the hosted partnership pack (`partnership-pack.html` and
  `files/Tia_Tandy_Partnership_Pack.pdf`). Pages are generated from a
  shared template script; `public/style.css` holds the look. The
  homepage carries a Next Match band (TBA until the owner supplies
  fixture details — set NEXT_MATCH in the generator).
- **The one-pager** — the original navy/chalk/red match-programme
  page, unlisted at `/v2/` (`public/v2/index.html`) by owner
  instruction. Keep its facts in step, condensed to suit the
  single-page format — never paste long-form copy into it, and never
  change its design language.

Shared photos and sponsor logos live in `public/img/`.

## Deployment

Cloudflare Workers static assets: every push deploys via
`npx wrangler deploy`, which serves the `public/` directory as
configured in `wrangler.jsonc`. Anything that should ship must live
under `public/`.

## Release workflow

Every push to the default branch is a release. Work in small, complete
batches: implement, verify, then commit and push — never leave pushed
work unverified or half-finished.

### Versioning

A simple ascending vMAJOR.MINOR sequence (v1.0, v1.1, v1.2 …). Every
push increments the minor by one, regardless of size. Reserve a major
bump for a ground-up overhaul of the project.

### Release tags

With every push, provide release-tag text in the reply, in exactly this
shape — the repo owner creates the GitHub release manually from it, so
never push tags:

    Tag: v<next>  —  Title: <five to nine words, plain and evocative>
    Description: <one to three sentences of editorial prose describing
    what changed from the user's point of view — outcomes, not
    implementation. No bullet lists, no jargon, no file names.>

### Commits

A descriptive imperative first line (what the change does, not
"update X"), then a short prose body — dash bullets are fine there —
explaining what changed and why it matters. Never include model names
or tooling identifiers in commits, titles, or code.

One commit per coherent piece of work; multiple commits may share a
push, but each push gets exactly one version tag entry covering all of
them.
