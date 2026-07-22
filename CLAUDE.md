# tia-tandy-rugby

Single-page website for Tia Tandy, an 18-year-old dual-code rugby prop
from Dartford. The whole site lives in `index.html` — no build step, no
dependencies.

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
