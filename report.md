![All brushes](contact.png)

# Brush Lab — 16 brushes · 9 Nov 2026 at 04:25

Every sheet: 1500 × 600, ten strokes in a 5 × 2 grid — 1. light line · 2. heavy line · 3. pressure swell · 4. fast wave · 5. slow wave · 6. spiral · 7. loop · 8. tilted · 9. over the wet one · 10. long, no reload (cell 8 holds «tilted» and «over the wet one» crossed). The CPU reference of Mamay's paint engine; the wet layer settles 20 s at the end.

Columns: **covered** = share of the cell with paint right after the stroke → after settling; **width** = painted area of the stroke ÷ its length (px); **dark** = mean darkness of the painted pixels above the paper's own grain (0 = paper, 1 = black); **spread** = how far wet paint went beyond the stroke (1.0 = stayed); **ms** = the stroke on the CPU; long stroke: paint in each quarter of its length (it should run out: wet → streaks → dry tail).

## Oil focus · A best filbert
Gouache 1.00 + turpentine 15 % · 260 px · 110.0 s

![Oil focus · A best filbert](Oil-focus-A-best-filbert.png)

A light paint: laid on a grey sheet (on white it cannot be seen); **dark** = how far it is from the grey either way.

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 73 % → 71 % | 213.3 px | 0.29 | 0.97 | 1714 |
| heavy line | 75 % → 67 % | 218.7 px | 0.29 | 0.88 | 1892 |
| pressure swell | 66 % → 74 % | 249.3 px | 0.26 | 1.11 | 1430 |
| fast wave | 99 % → 85 % | 114.8 px | 0.24 | 0.85 | 5559 |
| slow wave | 100 % → 69 % | 115.0 px | 0.28 | 0.70 | 10420 |
| spiral | 100 % → 73 % | 65.9 px | 0.28 | 0.73 | 10211 |
| loop | 100 % → 86 % | 129.5 px | 0.28 | 0.86 | 4883 |
| tilted | 55 % → 55 % | 153.9 px | 0.25 | 1.00 | 2692 |
| over the wet one | 92 % → 87 % | 103.2 px | 0.25 | 0.95 | 2858 |
| long, no reload | 100 % → 73 % | 44.8 px | 0.27 | 0.73 | 12159 | quarters: 0.00 → 0.00 → 0.00 → 0.00

Numbers say: light vs heavy: width 213.3 → 218.7 px, dark 0.29 → 0.29; pressure barely changes the width.

## Oil focus · B flat
Gouache 1.00 + turpentine 15 % · 260 px · 102.9 s

![Oil focus · B flat](Oil-focus-B-flat.png)

A light paint: laid on a grey sheet (on white it cannot be seen); **dark** = how far it is from the grey either way.

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 69 % → 69 % | 200.7 px | 0.31 | 1.00 | 1384 |
| heavy line | 70 % → 65 % | 204.5 px | 0.31 | 0.92 | 1669 |
| pressure swell | 61 % → 69 % | 230.5 px | 0.28 | 1.12 | 1262 |
| fast wave | 99 % → 83 % | 114.2 px | 0.26 | 0.84 | 4895 |
| slow wave | 99 % → 70 % | 114.9 px | 0.30 | 0.70 | 8423 |
| spiral | 100 % → 75 % | 65.9 px | 0.29 | 0.75 | 9050 |
| loop | 100 % → 86 % | 129.3 px | 0.30 | 0.87 | 4310 |
| tilted | 52 % → 52 % | 145.4 px | 0.27 | 1.00 | 2477 |
| over the wet one | 89 % → 86 % | 101.8 px | 0.27 | 0.97 | 1983 |
| long, no reload | 100 % → 73 % | 44.8 px | 0.28 | 0.73 | 11638 | quarters: 0.00 → 0.00 → 0.00 → 0.00

Numbers say: light vs heavy: width 200.7 → 204.5 px, dark 0.31 → 0.31; pressure barely changes the width.

## Oil focus · C round
Gouache 1.00 + turpentine 15 % · 260 px · 86.4 s

![Oil focus · C round](Oil-focus-C-round.png)

A light paint: laid on a grey sheet (on white it cannot be seen); **dark** = how far it is from the grey either way.

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 44 % → 38 % | 126.9 px | 0.36 | 0.86 | 731 |
| heavy line | 56 % → 51 % | 163.1 px | 0.37 | 0.92 | 1399 |
| pressure swell | 41 % → 42 % | 152.8 px | 0.32 | 1.03 | 1103 |
| fast wave | 89 % → 83 % | 103.2 px | 0.31 | 0.93 | 3500 |
| slow wave | 90 % → 70 % | 104.3 px | 0.36 | 0.78 | 5383 |
| spiral | 93 % → 78 % | 61.7 px | 0.36 | 0.84 | 5800 |
| loop | 78 % → 73 % | 100.6 px | 0.35 | 0.94 | 3049 |
| tilted | 48 % → 48 % | 133.5 px | 0.32 | 1.00 | 2753 |
| over the wet one | 83 % → 76 % | 97.3 px | 0.32 | 0.92 | 1618 |
| long, no reload | 100 % → 68 % | 44.7 px | 0.35 | 0.68 | 9176 | quarters: 0.00 → 0.00 → 0.00 → 0.00

Numbers say: light vs heavy: width 126.9 → 163.1 px, dark 0.36 → 0.37.

## Oil focus · D worn
Gouache 1.00 + turpentine 15 % · 260 px · 112.2 s

![Oil focus · D worn](Oil-focus-D-worn.png)

A light paint: laid on a grey sheet (on white it cannot be seen); **dark** = how far it is from the grey either way.

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 67 % → 69 % | 195.9 px | 0.31 | 1.02 | 1952 |
| heavy line | 77 % → 67 % | 224.7 px | 0.31 | 0.87 | 2362 |
| pressure swell | 72 % → 75 % | 269.4 px | 0.29 | 1.04 | 1819 |
| fast wave | 97 % → 89 % | 112.1 px | 0.28 | 0.92 | 5834 |
| slow wave | 96 % → 66 % | 110.6 px | 0.30 | 0.69 | 11048 |
| spiral | 97 % → 89 % | 64.2 px | 0.30 | 0.91 | 10380 |
| loop | 97 % → 84 % | 125.0 px | 0.30 | 0.87 | 5489 |
| tilted | 57 % → 57 % | 158.4 px | 0.27 | 1.00 | 3610 |
| over the wet one | 93 % → 87 % | 102.5 px | 0.27 | 0.94 | 2425 |
| long, no reload | 100 % → 65 % | 44.6 px | 0.29 | 0.65 | 12694 | quarters: 0.00 → 0.00 → 0.00 → 0.00

Numbers say: light vs heavy: width 195.9 → 224.7 px, dark 0.31 → 0.31.

## Oil focus · E swell
Gouache 1.00 + turpentine 15 % · 260 px · 112.2 s

![Oil focus · E swell](Oil-focus-E-swell.png)

A light paint: laid on a grey sheet (on white it cannot be seen); **dark** = how far it is from the grey either way.

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 73 % → 71 % | 212.2 px | 0.29 | 0.97 | 1414 |
| heavy line | 77 % → 67 % | 223.3 px | 0.29 | 0.87 | 2939 |
| pressure swell | 66 % → 74 % | 247.8 px | 0.26 | 1.12 | 1798 |
| fast wave | 99 % → 85 % | 114.8 px | 0.24 | 0.85 | 5804 |
| slow wave | 100 % → 69 % | 115.0 px | 0.28 | 0.70 | 10415 |
| spiral | 100 % → 73 % | 65.9 px | 0.28 | 0.73 | 10143 |
| loop | 100 % → 86 % | 129.5 px | 0.28 | 0.86 | 5210 |
| tilted | 55 % → 55 % | 154.3 px | 0.25 | 1.00 | 2835 |
| over the wet one | 92 % → 87 % | 102.8 px | 0.25 | 0.95 | 2295 |
| long, no reload | 100 % → 73 % | 44.8 px | 0.27 | 0.73 | 12873 | quarters: 0.00 → 0.00 → 0.00 → 0.00

Numbers say: light vs heavy: width 212.2 → 223.3 px, dark 0.29 → 0.29; pressure barely changes the width.

## Oil focus · F steady hand
Gouache 1.00 + turpentine 15 % · 260 px · 109.9 s

![Oil focus · F steady hand](Oil-focus-F-steady-hand.png)

A light paint: laid on a grey sheet (on white it cannot be seen); **dark** = how far it is from the grey either way.

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 73 % → 71 % | 212.5 px | 0.29 | 0.97 | 1688 |
| heavy line | 75 % → 66 % | 217.3 px | 0.29 | 0.88 | 1928 |
| pressure swell | 66 % → 73 % | 247.7 px | 0.26 | 1.11 | 1405 |
| fast wave | 99 % → 85 % | 114.8 px | 0.24 | 0.85 | 5470 |
| slow wave | 100 % → 70 % | 115.0 px | 0.28 | 0.70 | 10281 |
| spiral | 100 % → 73 % | 65.9 px | 0.28 | 0.73 | 10066 |
| loop | 100 % → 86 % | 129.5 px | 0.28 | 0.86 | 4906 |
| tilted | 55 % → 55 % | 153.4 px | 0.25 | 1.00 | 2693 |
| over the wet one | 92 % → 88 % | 103.4 px | 0.25 | 0.95 | 2663 |
| long, no reload | 100 % → 71 % | 44.8 px | 0.27 | 0.71 | 12466 | quarters: 0.00 → 0.00 → 0.00 → 0.00

Numbers say: light vs heavy: width 212.5 → 217.3 px, dark 0.29 → 0.29; pressure barely changes the width.

## Oil focus · G soft hairs
Gouache 1.00 + turpentine 15 % · 260 px · 111.4 s

![Oil focus · G soft hairs](Oil-focus-G-soft-hairs.png)

A light paint: laid on a grey sheet (on white it cannot be seen); **dark** = how far it is from the grey either way.

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 73 % → 72 % | 212.1 px | 0.28 | 0.98 | 1744 |
| heavy line | 74 % → 62 % | 216.1 px | 0.28 | 0.84 | 1927 |
| pressure swell | 65 % → 73 % | 244.1 px | 0.25 | 1.12 | 1477 |
| fast wave | 99 % → 75 % | 114.7 px | 0.24 | 0.76 | 5963 |
| slow wave | 100 % → 62 % | 115.0 px | 0.27 | 0.63 | 10602 |
| spiral | 100 % → 69 % | 65.9 px | 0.26 | 0.69 | 10569 |
| loop | 100 % → 76 % | 129.5 px | 0.27 | 0.76 | 5264 |
| tilted | 56 % → 56 % | 155.8 px | 0.24 | 1.00 | 2884 |
| over the wet one | 92 % → 86 % | 100.8 px | 0.24 | 0.93 | 2338 |
| long, no reload | 100 % → 71 % | 44.8 px | 0.26 | 0.71 | 12678 | quarters: 0.00 → 0.00 → 0.00 → 0.00

Numbers say: light vs heavy: width 212.1 → 216.1 px, dark 0.28 → 0.28; pressure barely changes the width.

## Oil focus · H narrow
Gouache 1.00 + turpentine 15 % · 200 px · 88.4 s

![Oil focus · H narrow](Oil-focus-H-narrow.png)

A light paint: laid on a grey sheet (on white it cannot be seen); **dark** = how far it is from the grey either way.

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 60 % → 55 % | 174.0 px | 0.31 | 0.92 | 1158 |
| heavy line | 62 % → 54 % | 178.7 px | 0.31 | 0.88 | 1307 |
| pressure swell | 50 % → 58 % | 187.7 px | 0.28 | 1.15 | 852 |
| fast wave | 94 % → 69 % | 108.8 px | 0.26 | 0.73 | 3615 |
| slow wave | 96 % → 61 % | 111.3 px | 0.31 | 0.63 | 6079 |
| spiral | 98 % → 58 % | 64.9 px | 0.28 | 0.59 | 7069 |
| loop | 93 % → 70 % | 120.1 px | 0.31 | 0.75 | 3638 |
| tilted | 45 % → 45 % | 124.4 px | 0.27 | 1.00 | 2070 |
| over the wet one | 83 % → 77 % | 108.5 px | 0.27 | 0.93 | 1433 |
| long, no reload | 100 % → 60 % | 44.8 px | 0.29 | 0.60 | 9391 | quarters: 0.00 → 0.00 → 0.00 → 0.00

Numbers say: light vs heavy: width 174.0 → 178.7 px, dark 0.31 → 0.31; pressure barely changes the width.

## Oil focus · A best filbert — own sheet
own sheet 2000 × 1320 · Gouache 1.00 + turpentine 15 % · 260 px · 77.6 s

![Oil focus · A best filbert — own sheet](Oil-focus-A-best-filbert-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 15 % → 50 % | 189.5 px | 0.47 | 3.29 | 5996 |
| stroke 2 | 28 % → 32 % | 351.2 px | 0.37 | 1.11 | 5691 |
| stroke 3 | 36 % → 34 % | 335.8 px | 0.43 | 0.93 | 12350 |
| stroke 4 | 42 % → 31 % | 583.3 px | 0.48 | 0.75 | 11172 |
| stroke 5 | 50 % → 34 % | 809.0 px | 0.50 | 0.69 | 5256 |

Numbers say: wet paint spreads well beyond the stroke.

## Oil focus · B flat — own sheet
own sheet 2000 × 1320 · Gouache 1.00 + turpentine 15 % · 260 px · 72.3 s

![Oil focus · B flat — own sheet](Oil-focus-B-flat-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 15 % → 49 % | 187.3 px | 0.47 | 3.25 | 5400 |
| stroke 2 | 28 % → 32 % | 342.4 px | 0.38 | 1.14 | 4999 |
| stroke 3 | 35 % → 33 % | 326.3 px | 0.44 | 0.93 | 10016 |
| stroke 4 | 41 % → 31 % | 572.2 px | 0.48 | 0.75 | 10312 |
| stroke 5 | 48 % → 34 % | 780.3 px | 0.50 | 0.70 | 5179 |

Numbers say: wet paint spreads well beyond the stroke.

## Oil focus · C round — own sheet
own sheet 2000 × 1320 · Gouache 1.00 + turpentine 15 % · 260 px · 51.6 s

![Oil focus · C round — own sheet](Oil-focus-C-round-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 10 % → 41 % | 129.7 px | 0.51 | 3.91 | 3505 |
| stroke 2 | 20 % → 30 % | 251.9 px | 0.44 | 1.47 | 3821 |
| stroke 3 | 24 % → 26 % | 223.0 px | 0.50 | 1.09 | 7309 |
| stroke 4 | 29 % → 26 % | 396.5 px | 0.51 | 0.90 | 6450 |
| stroke 5 | 34 % → 28 % | 551.8 px | 0.52 | 0.84 | 3080 |

Numbers say: wet paint spreads well beyond the stroke.

## Oil focus · D worn — own sheet
own sheet 2000 × 1320 · Gouache 1.00 + turpentine 15 % · 260 px · 62.3 s

![Oil focus · D worn — own sheet](Oil-focus-D-worn-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 15 % → 48 % | 188.5 px | 0.48 | 3.18 | 6468 |
| stroke 2 | 28 % → 32 % | 343.8 px | 0.39 | 1.14 | 5549 |
| stroke 3 | 34 % → 34 % | 315.7 px | 0.45 | 1.00 | 11639 |
| stroke 4 | 37 % → 31 % | 508.8 px | 0.49 | 0.83 | 9003 |
| stroke 5 | 43 % → 32 % | 702.4 px | 0.52 | 0.75 | 3973 |

Numbers say: wet paint spreads well beyond the stroke.

## Oil focus · E swell — own sheet
own sheet 2000 × 1320 · Gouache 1.00 + turpentine 15 % · 260 px · 61.6 s

![Oil focus · E swell — own sheet](Oil-focus-E-swell-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 15 % → 51 % | 190.8 px | 0.48 | 3.29 | 7429 |
| stroke 2 | 29 % → 32 % | 354.7 px | 0.39 | 1.12 | 6862 |
| stroke 3 | 36 % → 35 % | 336.8 px | 0.44 | 0.96 | 11597 |
| stroke 4 | 42 % → 32 % | 584.3 px | 0.49 | 0.76 | 6914 |
| stroke 5 | 50 % → 34 % | 810.3 px | 0.52 | 0.68 | 4550 |

Numbers say: wet paint spreads well beyond the stroke.

## Oil focus · F steady hand — own sheet
own sheet 2000 × 1320 · Gouache 1.00 + turpentine 15 % · 260 px · 56.0 s

![Oil focus · F steady hand — own sheet](Oil-focus-F-steady-hand-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 15 % → 50 % | 189.6 px | 0.47 | 3.28 | 5471 |
| stroke 2 | 28 % → 32 % | 351.2 px | 0.37 | 1.11 | 5235 |
| stroke 3 | 36 % → 34 % | 335.4 px | 0.43 | 0.93 | 9844 |
| stroke 4 | 42 % → 31 % | 582.8 px | 0.48 | 0.75 | 6835 |
| stroke 5 | 50 % → 34 % | 808.9 px | 0.50 | 0.69 | 3620 |

Numbers say: wet paint spreads well beyond the stroke.

## Oil focus · G soft hairs — own sheet
own sheet 2000 × 1320 · Gouache 1.00 + turpentine 15 % · 260 px · 48.7 s

![Oil focus · G soft hairs — own sheet](Oil-focus-G-soft-hairs-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 15 % → 45 % | 186.2 px | 0.46 | 2.99 | 5347 |
| stroke 2 | 28 % → 26 % | 346.9 px | 0.34 | 0.92 | 4462 |
| stroke 3 | 36 % → 31 % | 332.5 px | 0.42 | 0.87 | 7616 |
| stroke 4 | 41 % → 28 % | 563.3 px | 0.47 | 0.68 | 6292 |
| stroke 5 | 49 % → 29 % | 794.8 px | 0.50 | 0.60 | 3149 |

Numbers say: wet paint spreads well beyond the stroke.

## Oil focus · H narrow — own sheet
own sheet 2000 × 1320 · Gouache 1.00 + turpentine 15 % · 200 px · 40.9 s

![Oil focus · H narrow — own sheet](Oil-focus-H-narrow-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 20 % → 44 % | 189.5 px | 0.49 | 2.23 | 4416 |
| stroke 2 | 24 % → 27 % | 228.5 px | 0.37 | 1.16 | 3857 |
| stroke 3 | 34 % → 28 % | 275.0 px | 0.41 | 0.82 | 4802 |
| stroke 4 | 37 % → 30 % | 400.5 px | 0.47 | 0.83 | 4267 |
| stroke 5 | 48 % → 34 % | 616.6 px | 0.51 | 0.71 | 2189 |

Numbers say: wet paint spreads well beyond the stroke.

