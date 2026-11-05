# Backlog

Open items that need a human decision or an external account. Keep each entry
short: what, why, and where in the repo it lands.

## API keys and map providers

- [ ] **Review the UNCTAD API key.** The pipeline reads `UNCTAD_API_KEY` from the
  environment, falling back to the local `.env.txt` (`pipeline/sources/aux_unctad.py`).
  Check that the key is still valid, that `.env.txt` stays untracked, and whether it
  should be rotated.
- [ ] **Get a key for the map tiles.** The site maps (`public/assets/site.js`) pull
  CARTO `light_nolabels` / `dark_nolabels` basemaps from `basemaps.cartocdn.com`
  with no key. That free endpoint has no SLA and CARTO may rate-limit or retire it.
  Decide on a provider (CARTO account, MapTiler, or self-hosted tiles) and obtain a key.
- [ ] **Get a CARTO account key for the analytical layers.** If the overlays move
  from static `overlay.json` to CARTO-hosted data, the project needs its own CARTO
  API key, stored as an environment variable, not in `site.js`.

Added 2026-11-05.
