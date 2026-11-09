![All brushes](contact.png)

# Brush Lab — 2 brushes · Nov 9, 2026 at 7:05 PM

Every sheet: 1500 × 600, ten strokes in a 5 × 2 grid — 1. light line · 2. heavy line · 3. pressure swell · 4. fast wave · 5. slow wave · 6. spiral · 7. loop · 8. tilted · 9. over the wet one · 10. long, no reload (cell 8 holds «tilted» and «over the wet one» crossed). The CPU reference of Mamay's paint engine; the wet layer settles 20 s at the end.

Columns: **covered** = share of the cell with paint right after the stroke → after settling; **width** = painted area of the stroke ÷ its length (px); **dark** = mean darkness of the painted pixels above the paper's own grain (0 = paper, 1 = black); **spread** = how far wet paint went beyond the stroke (1.0 = stayed); **ms** = the stroke on the CPU; long stroke: paint in each quarter of its length (it should run out: wet → streaks → dry tail).

## Oil focus · A best filbert — own sheet
own sheet 2000 × 1320 · Gouache 1.00 + turpentine 15 % · 260 px · 500.2 s

![Oil focus · A best filbert — own sheet](Oil-focus-A-best-filbert-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 14 % → 33 % | 176.8 px | 0.50 | 2.28 | 46230 |
| stroke 2 | 27 % → 15 % | 333.3 px | 0.35 | 0.55 | 46549 |
| stroke 3 | 32 % → 23 % | 298.7 px | 0.45 | 0.72 | 94280 |
| stroke 4 | 35 % → 20 % | 480.6 px | 0.51 | 0.57 | 80753 |
| stroke 5 | 43 % → 19 % | 694.0 px | 0.56 | 0.44 | 41790 |

Numbers say: wet paint spreads well beyond the stroke.

## Watercolour · #40 Olive and sepia blooms — own sheet
own sheet 600 × 600 · Watercolour 1.00 + water 55 % · 90 px · 121.6 s

![Watercolour · #40 Olive and sepia blooms — own sheet](Watercolour-40-Olive-and-sepia-blooms-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 23 % → 43 % | 80.7 px | 0.13 | 1.86 | 6632 |
| stroke 2 | 41 % → 46 % | 131.4 px | 0.14 | 1.12 | 6667 |

Numbers say: wet paint spreads well beyond the stroke.



## Measures of the own sheets (v4 §9)

| sheet | fine lines (across ÷ along) | gaps | edge steps |
|---|---|---|---|
| Oil focus · A best filbert — own sheet | 1.17 | 1.6 % | 20.2 % |
| Watercolour · #40 Olive and sepia blooms — own sheet | 1.03 | 0.1 % | 47.4 % |
