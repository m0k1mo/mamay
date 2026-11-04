![All brushes](contact.png)

# Brush Lab — 4 brushes · Nov 4, 2026 at 8:34 AM

Every sheet: 1500 × 600, ten strokes in a 5 × 2 grid — 1. light line · 2. heavy line · 3. pressure swell · 4. fast wave · 5. slow wave · 6. spiral · 7. loop · 8. tilted · 9. over the wet one · 10. long, no reload (cell 8 holds «tilted» and «over the wet one» crossed). The CPU reference of Mamay's paint engine; the wet layer settles 20 s at the end.

Columns: **covered** = share of the cell with paint right after the stroke → after settling; **width** = painted area of the stroke ÷ its length (px); **dark** = mean darkness of the painted pixels above the paper's own grain (0 = paper, 1 = black); **spread** = how far wet paint went beyond the stroke (1.0 = stayed); **ms** = the stroke on the CPU; long stroke: paint in each quarter of its length (it should run out: wet → streaks → dry tail).

## Brush Artist · Refs · #35 Red band with runs
Watercolor · 70 px · 61.6 s

![Brush Artist · Refs · #35 Red band with runs](Brush-Artist-Refs-35-Red-band-with-runs.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 21 % → 38 % | 60.0 px | 0.44 | 1.82 | 271 |
| heavy line | 30 % → 45 % | 86.8 px | 0.47 | 1.50 | 544 |
| pressure swell | 17 % → 25 % | 63.0 px | 0.53 | 1.50 | 250 |
| fast wave | 57 % → 74 % | 65.4 px | 0.50 | 1.31 | 676 |
| slow wave | 54 % → 72 % | 62.2 px | 0.54 | 1.33 | 1092 |
| spiral | 74 % → 90 % | 49.1 px | 0.55 | 1.20 | 1022 |
| loop | 55 % → 78 % | 71.8 px | 0.50 | 1.40 | 550 |
| tilted | 25 % → 29 % | 69.5 px | 0.49 | 1.17 | 366 |
| over the wet one | 50 % → 78 % | 70.4 px | 0.49 | 1.55 | 348 |
| long, no reload | 93 % → 99 % | 41.8 px | 0.58 | 1.06 | 1470 | quarters: 0.60 → 0.60 → 0.59 → 0.56

Numbers say: light vs heavy: width 60.0 → 86.8 px, dark 0.44 → 0.47; the long stroke does not run out of paint; wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #48 Black bands with drips
Gouache · 70 px · 57.2 s

![Brush Artist · Refs · #48 Black bands with drips](Brush-Artist-Refs-48-Black-bands-with-drips.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 20 % → 18 % | 58.7 px | 0.67 | 0.90 | 463 |
| heavy line | 30 % → 25 % | 87.8 px | 0.67 | 0.83 | 652 |
| pressure swell | 23 % → 21 % | 86.1 px | 0.67 | 0.92 | 363 |
| fast wave | 56 % → 37 % | 64.4 px | 0.67 | 0.66 | 892 |
| slow wave | 55 % → 36 % | 63.8 px | 0.67 | 0.66 | 1444 |
| spiral | 65 % → 35 % | 42.9 px | 0.67 | 0.53 | 1454 |
| loop | 47 % → 38 % | 60.7 px | 0.67 | 0.81 | 629 |
| tilted | 20 % → 20 % | 55.5 px | 0.67 | 1.01 | 565 |
| over the wet one | 43 % → 39 % | 64.5 px | 0.67 | 0.91 | 342 |
| long, no reload | 75 % → 37 % | 33.5 px | 0.67 | 0.50 | 1777 | quarters: 0.63 → 0.60 → 0.53 → 0.43

Numbers say: light vs heavy: width 58.7 → 87.8 px, dark 0.67 → 0.67.

## Brush Artist · Refs · #35 Red band with runs — own sheet
own sheet 600 × 600 · Watercolor · 70 px · 10.3 s

![Brush Artist · Refs · #35 Red band with runs — own sheet](Brush-Artist-Refs-35-Red-band-with-runs-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 26 % → 37 % | 96.0 px | 0.50 | 1.45 | 734 |

## Brush Artist · Refs · #48 Black bands with drips — own sheet
own sheet 600 × 600 · Gouache · 70 px · 16.7 s

![Brush Artist · Refs · #48 Black bands with drips — own sheet](Brush-Artist-Refs-48-Black-bands-with-drips-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 25 % → 38 % | 64.4 px | 0.38 | 1.54 | 631 |
| stroke 2 | 38 % → 51 % | 121.1 px | 0.38 | 1.36 | 756 |
| stroke 3 | 40 % → 52 % | 125.0 px | 0.38 | 1.30 | 687 |
| stroke 4 | 43 % → 40 % | 124.2 px | 0.38 | 0.95 | 641 |

Numbers say: wet paint spreads well beyond the stroke.

