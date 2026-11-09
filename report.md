![All brushes](contact.png)

# Brush Lab — 3 brushes · Nov 9, 2026 at 9:08 PM

Every sheet: 1500 × 600, ten strokes in a 5 × 2 grid — 1. light line · 2. heavy line · 3. pressure swell · 4. fast wave · 5. slow wave · 6. spiral · 7. loop · 8. tilted · 9. over the wet one · 10. long, no reload (cell 8 holds «tilted» and «over the wet one» crossed). The CPU reference of Mamay's paint engine; the wet layer settles 20 s at the end.

Columns: **covered** = share of the cell with paint right after the stroke → after settling; **width** = painted area of the stroke ÷ its length (px); **dark** = mean darkness of the painted pixels above the paper's own grain (0 = paper, 1 = black); **spread** = how far wet paint went beyond the stroke (1.0 = stayed); **ms** = the stroke on the CPU; long stroke: paint in each quarter of its length (it should run out: wet → streaks → dry tail).

## Oil focus · A best filbert — own sheet
own sheet 2000 × 1320 · Gouache 1.00 + turpentine 15 % · 260 px · 756.7 s

![Oil focus · A best filbert — own sheet](Oil-focus-A-best-filbert-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 15 % → 52 % | 190.2 px | 0.52 | 3.35 | 46509 |
| stroke 2 | 28 % → 33 % | 352.5 px | 0.44 | 1.15 | 48056 |
| stroke 3 | 36 % → 33 % | 333.6 px | 0.49 | 0.94 | 112399 |
| stroke 4 | 42 % → 32 % | 582.2 px | 0.53 | 0.77 | 105596 |
| stroke 5 | 50 % → 36 % | 807.2 px | 0.53 | 0.73 | 56519 |

Numbers say: wet paint spreads well beyond the stroke.

## Oil focus · B flat — own sheet
own sheet 2000 × 1320 · Gouache 1.00 + turpentine 15 % · 260 px · 599.7 s

![Oil focus · B flat — own sheet](Oil-focus-B-flat-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 15 % → 51 % | 186.4 px | 0.53 | 3.37 | 40044 |
| stroke 2 | 28 % → 33 % | 341.2 px | 0.46 | 1.20 | 38773 |
| stroke 3 | 35 % → 33 % | 324.6 px | 0.50 | 0.94 | 83601 |
| stroke 4 | 41 % → 32 % | 571.0 px | 0.53 | 0.77 | 74754 |
| stroke 5 | 48 % → 36 % | 779.4 px | 0.53 | 0.75 | 38629 |

Numbers say: wet paint spreads well beyond the stroke.

## Oil focus · D worn — own sheet
own sheet 2000 × 1320 · Gouache 1.00 + turpentine 15 % · 260 px · 646.4 s

![Oil focus · D worn — own sheet](Oil-focus-D-worn-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 17 % → 51 % | 204.9 px | 0.52 | 3.09 | 48698 |
| stroke 2 | 29 % → 33 % | 363.4 px | 0.44 | 1.12 | 50499 |
| stroke 3 | 35 % → 35 % | 324.3 px | 0.49 | 1.01 | 128750 |
| stroke 4 | 39 % → 32 % | 541.4 px | 0.53 | 0.82 | 103162 |
| stroke 5 | 46 % → 35 % | 755.7 px | 0.54 | 0.74 | 50813 |

Numbers say: wet paint spreads well beyond the stroke.



## Measures of the own sheets (v4 §9)

| sheet | fine lines (across ÷ along) | gaps | edge steps |
|---|---|---|---|
| Oil focus · A best filbert — own sheet | 1.12 | 0.8 % | 17.8 % |
| Oil focus · B flat — own sheet | 1.24 | 1.7 % | 15.5 % |
| Oil focus · D worn — own sheet | 1.32 | 1.1 % | 20.4 % |
