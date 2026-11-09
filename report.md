![All brushes](contact.png)

# Brush Lab — 2 brushes · 9 Nov 2026 at 21:21

Every sheet: 1500 × 600, ten strokes in a 5 × 2 grid — 1. light line · 2. heavy line · 3. pressure swell · 4. fast wave · 5. slow wave · 6. spiral · 7. loop · 8. tilted · 9. over the wet one · 10. long, no reload (cell 8 holds «tilted» and «over the wet one» crossed). The CPU reference of Mamay's paint engine; the wet layer settles 20 s at the end.

Columns: **covered** = share of the cell with paint right after the stroke → after settling; **width** = painted area of the stroke ÷ its length (px); **dark** = mean darkness of the painted pixels above the paper's own grain (0 = paper, 1 = black); **spread** = how far wet paint went beyond the stroke (1.0 = stayed); **ms** = the stroke on the CPU; long stroke: paint in each quarter of its length (it should run out: wet → streaks → dry tail).

## Oil focus · A best filbert — own sheet
own sheet 2000 × 1320 · Gouache 1.00 + turpentine 15 % · 260 px · 345.9 s

![Oil focus · A best filbert — own sheet](Oil-focus-A-best-filbert-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 14 % → 33 % | 176.8 px | 0.50 | 2.28 | 32154 |
| stroke 2 | 27 % → 15 % | 333.3 px | 0.35 | 0.55 | 31523 |
| stroke 3 | 32 % → 23 % | 299.3 px | 0.45 | 0.71 | 63355 |
| stroke 4 | 35 % → 20 % | 481.1 px | 0.51 | 0.57 | 52692 |
| stroke 5 | 43 % → 19 % | 694.0 px | 0.56 | 0.44 | 29008 |

Numbers say: wet paint spreads well beyond the stroke.

## Oil focus · D worn — own sheet
own sheet 2000 × 1320 · Gouache 1.00 + turpentine 15 % · 260 px · 352.3 s

![Oil focus · D worn — own sheet](Oil-focus-D-worn-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 13 % → 31 % | 165.9 px | 0.50 | 2.30 | 31496 |
| stroke 2 | 24 % → 15 % | 301.8 px | 0.36 | 0.60 | 32001 |
| stroke 3 | 29 % → 22 % | 270.7 px | 0.46 | 0.76 | 67504 |
| stroke 4 | 31 % → 18 % | 430.1 px | 0.52 | 0.59 | 56700 |
| stroke 5 | 37 % → 17 % | 610.2 px | 0.58 | 0.46 | 30791 |

Numbers say: wet paint spreads well beyond the stroke.



## Measures of the own sheets (v4 §9)

| sheet | fine lines (across ÷ along) | gaps | edge steps |
|---|---|---|---|
| Oil focus · A best filbert — own sheet | 1.18 | 1.6 % | 20.1 % |
| Oil focus · D worn — own sheet | 1.28 | 2.9 % | 20.4 % |
