![All brushes](contact.png)

# Brush Lab — 4 brushes · Nov 4, 2026 at 8:08 AM

Every sheet: 1500 × 600, ten strokes in a 5 × 2 grid — 1. light line · 2. heavy line · 3. pressure swell · 4. fast wave · 5. slow wave · 6. spiral · 7. loop · 8. tilted · 9. over the wet one · 10. long, no reload (cell 8 holds «tilted» and «over the wet one» crossed). The CPU reference of Mamay's paint engine; the wet layer settles 20 s at the end.

Columns: **covered** = share of the cell with paint right after the stroke → after settling; **width** = painted area of the stroke ÷ its length (px); **dark** = mean darkness of the painted pixels above the paper's own grain (0 = paper, 1 = black); **spread** = how far wet paint went beyond the stroke (1.0 = stayed); **ms** = the stroke on the CPU; long stroke: paint in each quarter of its length (it should run out: wet → streaks → dry tail).

## Brush Artist · Refs · #35 Red band with runs
Watercolor · 70 px · 45.7 s

![Brush Artist · Refs · #35 Red band with runs](Brush-Artist-Refs-35-Red-band-with-runs.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 17 % → 35 % | 48.3 px | 0.47 | 2.08 | 116 |
| heavy line | 25 % → 41 % | 73.9 px | 0.49 | 1.61 | 209 |
| pressure swell | 17 % → 25 % | 63.0 px | 0.53 | 1.50 | 139 |
| fast wave | 54 % → 73 % | 61.9 px | 0.51 | 1.37 | 424 |
| slow wave | 52 % → 71 % | 59.8 px | 0.54 | 1.38 | 968 |
| spiral | 72 % → 89 % | 47.4 px | 0.55 | 1.24 | 695 |
| loop | 47 % → 71 % | 61.4 px | 0.51 | 1.51 | 357 |
| tilted | 21 % → 22 % | 58.2 px | 0.50 | 1.06 | 258 |
| over the wet one | 43 % → 71 % | 62.1 px | 0.50 | 1.65 | 180 |
| long, no reload | 93 % → 98 % | 41.5 px | 0.58 | 1.06 | 1026 | quarters: 0.60 → 0.60 → 0.59 → 0.57

Numbers say: light vs heavy: width 48.3 → 73.9 px, dark 0.47 → 0.49; the long stroke does not run out of paint; wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #48 Black bands with drips
Gouache · 70 px · 39.6 s

![Brush Artist · Refs · #48 Black bands with drips](Brush-Artist-Refs-48-Black-bands-with-drips.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 19 % → 18 % | 54.7 px | 0.68 | 0.94 | 218 |
| heavy line | 29 % → 24 % | 83.1 px | 0.68 | 0.85 | 272 |
| pressure swell | 23 % → 21 % | 86.1 px | 0.68 | 0.92 | 173 |
| fast wave | 54 % → 37 % | 62.8 px | 0.68 | 0.67 | 538 |
| slow wave | 54 % → 36 % | 61.9 px | 0.68 | 0.67 | 1135 |
| spiral | 64 % → 35 % | 42.2 px | 0.68 | 0.54 | 884 |
| loop | 45 % → 37 % | 58.1 px | 0.68 | 0.82 | 451 |
| tilted | 19 % → 19 % | 52.5 px | 0.68 | 1.00 | 281 |
| over the wet one | 41 % → 38 % | 62.5 px | 0.68 | 0.92 | 210 |
| long, no reload | 74 % → 37 % | 33.4 px | 0.68 | 0.50 | 1254 | quarters: 0.64 → 0.61 → 0.54 → 0.44

Numbers say: light vs heavy: width 54.7 → 83.1 px, dark 0.68 → 0.68.

## Brush Artist · Refs · #35 Red band with runs — own sheet
own sheet 600 × 600 · Watercolor · 70 px · 5.6 s

![Brush Artist · Refs · #35 Red band with runs — own sheet](Brush-Artist-Refs-35-Red-band-with-runs-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 21 % → 33 % | 77.5 px | 0.50 | 1.59 | 292 |

Numbers say: wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #48 Black bands with drips — own sheet
own sheet 600 × 600 · Gouache · 70 px · 9.2 s

![Brush Artist · Refs · #48 Black bands with drips — own sheet](Brush-Artist-Refs-48-Black-bands-with-drips-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 23 % → 36 % | 59.0 px | 0.39 | 1.58 | 428 |
| stroke 2 | 34 % → 48 % | 108.7 px | 0.39 | 1.41 | 414 |
| stroke 3 | 36 % → 48 % | 112.8 px | 0.39 | 1.34 | 434 |
| stroke 4 | 38 % → 36 % | 111.8 px | 0.39 | 0.95 | 419 |

Numbers say: wet paint spreads well beyond the stroke.

