# tia-tandy-rugby

The website of Tia Tandy — an 18-year-old front-row forward from
Dartford, Kent, playing senior rugby in both codes: union with Thurrock
T-Birds and league with London Broncos.

The site is a single self-contained page: open `public/index.html` in a
browser. Deployment is Cloudflare Workers static assets — every push
runs `npx wrangler deploy`, which serves the `public/` directory as
configured in `wrangler.jsonc`.

## Releases

Every push to the default branch is a release, versioned v1.0, v1.1,
v1.2 … — see `CLAUDE.md` for the full workflow.
