# tia-tandy-rugby

Website for Tia Tandy, an 18-year-old dual-code rugby prop from
Dartford. No build step, no dependencies. Two versions live side by
side, linked by a tab strip at the top of every page:

- **Version 1** — the original one-pager, `public/index.html`.
  **Frozen by owner instruction**: do not change it beyond the version
  tab strip that links the two versions, unless the owner explicitly
  asks.
- **Version 2** — a multi-page site with dropdown navigation under
  `public/v2/` (front page, bio, one page per club, pictures,
  sponsors, My Rugby Life, videos), styled black-and-gold to the
  client's mock. Pages share `public/v2/style.css`; photo/video/stat
  placeholders are filled in as the client supplies material. All
  ongoing site work happens here.

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
