# Brush Artist packs

One JSON file per pack: `{"id": "...", "version": N, "folder": "...", "brushes": [{"name": "...", "recipe": {...}}]}` — the recipe
fields are those of Mamay's Brush Lab (Path · Tool · Material · Surface · Time · Form · Counterform · steps · erase); a missing
field keeps its default. A push here paints every brush (Actions › Brush Lab) and publishes the sheets on the branch
`brush-lab-out` — https://github.com/m0k1mo/mamay/blob/brush-lab-out/report.md. Mamay installs the packs too (Application
Support/Mamay/Brushes/Packs), once per version: raise `version` for every new release of a pack.
