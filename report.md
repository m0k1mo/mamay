![All brushes](contact.png)

# Brush Lab — 16 brushes · 9 Nov 2026 at 12:56

Every sheet: 1500 × 600, ten strokes in a 5 × 2 grid — 1. light line · 2. heavy line · 3. pressure swell · 4. fast wave · 5. slow wave · 6. spiral · 7. loop · 8. tilted · 9. over the wet one · 10. long, no reload (cell 8 holds «tilted» and «over the wet one» crossed). The CPU reference of Mamay's paint engine; the wet layer settles 20 s at the end.

Columns: **covered** = share of the cell with paint right after the stroke → after settling; **width** = painted area of the stroke ÷ its length (px); **dark** = mean darkness of the painted pixels above the paper's own grain (0 = paper, 1 = black); **spread** = how far wet paint went beyond the stroke (1.0 = stayed); **ms** = the stroke on the CPU; long stroke: paint in each quarter of its length (it should run out: wet → streaks → dry tail).

## Oil focus · A best filbert
Gouache 1.00 + turpentine 15 % · 260 px · 224.6 s

![Oil focus · A best filbert](Oil-focus-A-best-filbert.png)

A light paint: laid on a grey sheet (on white it cannot be seen); **dark** = how far it is from the grey either way.

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 73 % → 71 % | 213.2 px | 0.29 | 0.97 | 3198 |
| heavy line | 75 % → 66 % | 218.6 px | 0.29 | 0.88 | 3792 |
| pressure swell | 66 % → 73 % | 249.2 px | 0.26 | 1.11 | 2343 |
| fast wave | 99 % → 78 % | 114.6 px | 0.25 | 0.78 | 10412 |
| slow wave | 99 % → 65 % | 115.0 px | 0.28 | 0.66 | 17534 |
| spiral | 100 % → 70 % | 65.9 px | 0.28 | 0.70 | 15417 |
| loop | 100 % → 78 % | 129.5 px | 0.28 | 0.78 | 8443 |
| tilted | 55 % → 55 % | 153.5 px | 0.26 | 1.00 | 3537 |
| over the wet one | 92 % → 85 % | 103.5 px | 0.26 | 0.92 | 3558 |
| long, no reload | 100 % → 55 % | 44.8 px | 0.28 | 0.55 | 20971 | quarters: 0.00 → 0.00 → 0.00 → 0.00

Numbers say: light vs heavy: width 213.2 → 218.6 px, dark 0.29 → 0.29; pressure barely changes the width.

## Oil focus · B flat
Gouache 1.00 + turpentine 15 % · 260 px · 199.9 s

![Oil focus · B flat](Oil-focus-B-flat.png)

A light paint: laid on a grey sheet (on white it cannot be seen); **dark** = how far it is from the grey either way.

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 69 % → 69 % | 200.7 px | 0.30 | 1.00 | 2483 |
| heavy line | 70 % → 64 % | 204.4 px | 0.30 | 0.91 | 3235 |
| pressure swell | 61 % → 69 % | 230.3 px | 0.27 | 1.12 | 1905 |
| fast wave | 99 % → 74 % | 114.0 px | 0.25 | 0.75 | 8253 |
| slow wave | 99 % → 65 % | 114.8 px | 0.29 | 0.66 | 14333 |
| spiral | 100 % → 72 % | 65.8 px | 0.28 | 0.73 | 13152 |
| loop | 100 % → 79 % | 129.3 px | 0.29 | 0.79 | 6687 |
| tilted | 52 % → 52 % | 144.7 px | 0.27 | 1.00 | 3734 |
| over the wet one | 88 % → 84 % | 102.3 px | 0.27 | 0.95 | 3428 |
| long, no reload | 100 % → 57 % | 44.8 px | 0.28 | 0.57 | 16250 | quarters: 0.00 → 0.00 → 0.00 → 0.00

Numbers say: light vs heavy: width 200.7 → 204.4 px, dark 0.30 → 0.30; pressure barely changes the width.

## Oil focus · C round
Gouache 1.00 + turpentine 15 % · 260 px · 187.6 s

![Oil focus · C round](Oil-focus-C-round.png)

A light paint: laid on a grey sheet (on white it cannot be seen); **dark** = how far it is from the grey either way.

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 44 % → 38 % | 126.9 px | 0.36 | 0.86 | 1518 |
| heavy line | 56 % → 51 % | 163.1 px | 0.36 | 0.92 | 2397 |
| pressure swell | 41 % → 42 % | 152.8 px | 0.32 | 1.03 | 1982 |
| fast wave | 89 % → 81 % | 103.2 px | 0.32 | 0.91 | 6788 |
| slow wave | 90 % → 67 % | 104.2 px | 0.35 | 0.75 | 10818 |
| spiral | 93 % → 71 % | 61.6 px | 0.36 | 0.76 | 11122 |
| loop | 78 % → 70 % | 100.5 px | 0.35 | 0.91 | 5296 |
| tilted | 48 % → 48 % | 133.4 px | 0.34 | 1.00 | 4206 |
| over the wet one | 83 % → 75 % | 97.4 px | 0.34 | 0.91 | 2863 |
| long, no reload | 100 % → 62 % | 44.7 px | 0.35 | 0.63 | 16583 | quarters: 0.00 → 0.00 → 0.00 → 0.00

Numbers say: light vs heavy: width 126.9 → 163.1 px, dark 0.36 → 0.36.

## Oil focus · D worn
Gouache 1.00 + turpentine 15 % · 260 px · 240.0 s

![Oil focus · D worn](Oil-focus-D-worn.png)

A light paint: laid on a grey sheet (on white it cannot be seen); **dark** = how far it is from the grey either way.

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 67 % → 68 % | 195.9 px | 0.30 | 1.00 | 3754 |
| heavy line | 77 % → 67 % | 224.6 px | 0.30 | 0.86 | 4668 |
| pressure swell | 72 % → 74 % | 269.3 px | 0.28 | 1.04 | 3170 |
| fast wave | 97 % → 87 % | 112.0 px | 0.28 | 0.89 | 10577 |
| slow wave | 96 % → 62 % | 110.5 px | 0.30 | 0.65 | 17421 |
| spiral | 97 % → 85 % | 64.2 px | 0.30 | 0.87 | 15947 |
| loop | 96 % → 77 % | 124.7 px | 0.30 | 0.80 | 8883 |
| tilted | 57 % → 57 % | 158.1 px | 0.28 | 1.00 | 4472 |
| over the wet one | 93 % → 86 % | 102.6 px | 0.28 | 0.92 | 4311 |
| long, no reload | 99 % → 56 % | 44.5 px | 0.29 | 0.57 | 21613 | quarters: 0.00 → 0.00 → 0.00 → 0.01

Numbers say: light vs heavy: width 195.9 → 224.6 px, dark 0.30 → 0.30.

## Oil focus · E swell
Gouache 1.00 + turpentine 15 % · 260 px · 224.3 s

![Oil focus · E swell](Oil-focus-E-swell.png)

A light paint: laid on a grey sheet (on white it cannot be seen); **dark** = how far it is from the grey either way.

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 73 % → 71 % | 212.2 px | 0.28 | 0.97 | 2670 |
| heavy line | 77 % → 66 % | 223.1 px | 0.29 | 0.86 | 5165 |
| pressure swell | 66 % → 74 % | 247.6 px | 0.26 | 1.12 | 2762 |
| fast wave | 99 % → 78 % | 114.7 px | 0.25 | 0.78 | 9795 |
| slow wave | 100 % → 65 % | 115.0 px | 0.28 | 0.65 | 15755 |
| spiral | 100 % → 70 % | 65.9 px | 0.27 | 0.70 | 15007 |
| loop | 100 % → 78 % | 129.5 px | 0.28 | 0.78 | 8281 |
| tilted | 55 % → 55 % | 153.9 px | 0.25 | 1.00 | 3593 |
| over the wet one | 92 % → 85 % | 103.1 px | 0.25 | 0.92 | 3512 |
| long, no reload | 100 % → 54 % | 44.8 px | 0.28 | 0.54 | 20792 | quarters: 0.00 → 0.00 → 0.00 → 0.00

Numbers say: light vs heavy: width 212.2 → 223.1 px, dark 0.28 → 0.29; pressure barely changes the width.

## Oil focus · F steady hand
Gouache 1.00 + turpentine 15 % · 260 px · 227.1 s

![Oil focus · F steady hand](Oil-focus-F-steady-hand.png)

A light paint: laid on a grey sheet (on white it cannot be seen); **dark** = how far it is from the grey either way.

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 73 % → 71 % | 212.5 px | 0.29 | 0.97 | 3075 |
| heavy line | 75 % → 66 % | 217.3 px | 0.29 | 0.88 | 3982 |
| pressure swell | 66 % → 73 % | 247.6 px | 0.26 | 1.11 | 2436 |
| fast wave | 99 % → 78 % | 114.7 px | 0.25 | 0.78 | 10564 |
| slow wave | 99 % → 66 % | 114.9 px | 0.28 | 0.66 | 17712 |
| spiral | 100 % → 70 % | 65.9 px | 0.28 | 0.70 | 15815 |
| loop | 100 % → 78 % | 129.5 px | 0.28 | 0.78 | 8596 |
| tilted | 55 % → 55 % | 153.0 px | 0.26 | 1.00 | 3655 |
| over the wet one | 92 % → 85 % | 103.7 px | 0.26 | 0.92 | 3611 |
| long, no reload | 100 % → 54 % | 44.8 px | 0.28 | 0.54 | 21532 | quarters: 0.00 → 0.00 → 0.00 → 0.00

Numbers say: light vs heavy: width 212.5 → 217.3 px, dark 0.29 → 0.29; pressure barely changes the width.

## Oil focus · G soft hairs
Gouache 1.00 + turpentine 15 % · 260 px · 226.1 s

![Oil focus · G soft hairs](Oil-focus-G-soft-hairs.png)

A light paint: laid on a grey sheet (on white it cannot be seen); **dark** = how far it is from the grey either way.

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 73 % → 72 % | 212.1 px | 0.28 | 0.98 | 3005 |
| heavy line | 74 % → 62 % | 216.0 px | 0.28 | 0.83 | 3899 |
| pressure swell | 65 % → 72 % | 243.9 px | 0.25 | 1.11 | 2275 |
| fast wave | 99 % → 69 % | 114.6 px | 0.24 | 0.70 | 10446 |
| slow wave | 99 % → 49 % | 114.9 px | 0.27 | 0.50 | 18069 |
| spiral | 100 % → 65 % | 65.8 px | 0.27 | 0.65 | 16227 |
| loop | 100 % → 67 % | 129.5 px | 0.28 | 0.67 | 8264 |
| tilted | 56 % → 56 % | 155.5 px | 0.25 | 1.00 | 3596 |
| over the wet one | 92 % → 84 % | 101.0 px | 0.25 | 0.91 | 3634 |
| long, no reload | 100 % → 56 % | 44.8 px | 0.27 | 0.56 | 21812 | quarters: 0.00 → 0.00 → 0.00 → 0.00

Numbers say: light vs heavy: width 212.1 → 216.0 px, dark 0.28 → 0.28; pressure barely changes the width.

## Oil focus · H narrow
Gouache 1.00 + turpentine 15 % · 200 px · 176.2 s

![Oil focus · H narrow](Oil-focus-H-narrow.png)

A light paint: laid on a grey sheet (on white it cannot be seen); **dark** = how far it is from the grey either way.

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 60 % → 55 % | 174.0 px | 0.31 | 0.92 | 2240 |
| heavy line | 62 % → 54 % | 178.6 px | 0.31 | 0.88 | 2083 |
| pressure swell | 50 % → 58 % | 187.6 px | 0.28 | 1.15 | 1678 |
| fast wave | 94 % → 63 % | 108.4 px | 0.27 | 0.67 | 6533 |
| slow wave | 96 % → 56 % | 110.7 px | 0.31 | 0.58 | 11660 |
| spiral | 98 % → 55 % | 64.9 px | 0.29 | 0.56 | 11225 |
| loop | 92 % → 64 % | 119.8 px | 0.30 | 0.69 | 5340 |
| tilted | 44 % → 44 % | 123.9 px | 0.28 | 1.00 | 2641 |
| over the wet one | 83 % → 76 % | 108.8 px | 0.28 | 0.91 | 2731 |
| long, no reload | 99 % → 48 % | 44.5 px | 0.30 | 0.49 | 15347 | quarters: 0.00 → 0.00 → 0.00 → 0.01

Numbers say: light vs heavy: width 174.0 → 178.6 px, dark 0.31 → 0.31; pressure barely changes the width.

## Oil focus · A best filbert — own sheet
own sheet 2000 × 1320 · Gouache 1.00 + turpentine 15 % · 260 px · 131.2 s

![Oil focus · A best filbert — own sheet](Oil-focus-A-best-filbert-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 15 % → 48 % | 189.4 px | 0.48 | 3.16 | 10555 |
| stroke 2 | 28 % → 29 % | 351.0 px | 0.38 | 1.04 | 9713 |
| stroke 3 | 35 % → 32 % | 328.8 px | 0.45 | 0.91 | 19579 |
| stroke 4 | 41 % → 30 % | 572.7 px | 0.49 | 0.73 | 19270 |
| stroke 5 | 50 % → 33 % | 806.7 px | 0.50 | 0.67 | 9996 |

Numbers say: wet paint spreads well beyond the stroke.

## Oil focus · B flat — own sheet
own sheet 2000 × 1320 · Gouache 1.00 + turpentine 15 % · 260 px · 113.2 s

![Oil focus · B flat — own sheet](Oil-focus-B-flat-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 15 % → 47 % | 187.3 px | 0.49 | 3.13 | 8946 |
| stroke 2 | 28 % → 29 % | 342.2 px | 0.40 | 1.06 | 7225 |
| stroke 3 | 34 % → 31 % | 321.2 px | 0.45 | 0.90 | 14695 |
| stroke 4 | 41 % → 29 % | 564.7 px | 0.49 | 0.72 | 14429 |
| stroke 5 | 48 % → 33 % | 779.3 px | 0.50 | 0.68 | 7824 |

Numbers say: wet paint spreads well beyond the stroke.

## Oil focus · C round — own sheet
own sheet 2000 × 1320 · Gouache 1.00 + turpentine 15 % · 260 px · 115.6 s

![Oil focus · C round — own sheet](Oil-focus-C-round-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 10 % → 41 % | 129.7 px | 0.52 | 3.90 | 5910 |
| stroke 2 | 20 % → 29 % | 252.1 px | 0.45 | 1.42 | 5394 |
| stroke 3 | 24 % → 25 % | 221.3 px | 0.52 | 1.06 | 14490 |
| stroke 4 | 28 % → 25 % | 394.8 px | 0.53 | 0.88 | 14545 |
| stroke 5 | 34 % → 28 % | 554.3 px | 0.52 | 0.84 | 6127 |

Numbers say: wet paint spreads well beyond the stroke.

## Oil focus · D worn — own sheet
own sheet 2000 × 1320 · Gouache 1.00 + turpentine 15 % · 260 px · 133.1 s

![Oil focus · D worn — own sheet](Oil-focus-D-worn-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 15 % → 46 % | 188.2 px | 0.49 | 3.06 | 12870 |
| stroke 2 | 28 % → 29 % | 343.5 px | 0.38 | 1.03 | 11377 |
| stroke 3 | 33 % → 32 % | 311.9 px | 0.46 | 0.96 | 23571 |
| stroke 4 | 36 % → 29 % | 503.7 px | 0.50 | 0.79 | 23703 |
| stroke 5 | 43 % → 30 % | 697.2 px | 0.51 | 0.71 | 10586 |

Numbers say: wet paint spreads well beyond the stroke.

## Oil focus · E swell — own sheet
own sheet 2000 × 1320 · Gouache 1.00 + turpentine 15 % · 260 px · 114.3 s

![Oil focus · E swell — own sheet](Oil-focus-E-swell-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 15 % → 49 % | 190.6 px | 0.49 | 3.20 | 15958 |
| stroke 2 | 29 % → 30 % | 354.5 px | 0.40 | 1.04 | 13523 |
| stroke 3 | 35 % → 33 % | 331.2 px | 0.46 | 0.92 | 22425 |
| stroke 4 | 41 % → 31 % | 574.8 px | 0.50 | 0.74 | 13073 |
| stroke 5 | 50 % → 33 % | 810.5 px | 0.51 | 0.67 | 8086 |

Numbers say: wet paint spreads well beyond the stroke.

## Oil focus · F steady hand — own sheet
own sheet 2000 × 1320 · Gouache 1.00 + turpentine 15 % · 260 px · 102.8 s

![Oil focus · F steady hand — own sheet](Oil-focus-F-steady-hand-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 15 % → 50 % | 189.4 px | 0.48 | 3.24 | 12991 |
| stroke 2 | 28 % → 31 % | 351.0 px | 0.38 | 1.08 | 11432 |
| stroke 3 | 35 % → 32 % | 328.9 px | 0.45 | 0.92 | 17274 |
| stroke 4 | 41 % → 31 % | 573.0 px | 0.49 | 0.75 | 12636 |
| stroke 5 | 50 % → 35 % | 808.4 px | 0.50 | 0.70 | 6331 |

Numbers say: wet paint spreads well beyond the stroke.

## Oil focus · G soft hairs — own sheet
own sheet 2000 × 1320 · Gouache 1.00 + turpentine 15 % · 260 px · 90.2 s

![Oil focus · G soft hairs — own sheet](Oil-focus-G-soft-hairs-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 15 % → 42 % | 186.0 px | 0.47 | 2.79 | 12199 |
| stroke 2 | 28 % → 23 % | 346.7 px | 0.34 | 0.80 | 9030 |
| stroke 3 | 34 % → 29 % | 317.5 px | 0.43 | 0.84 | 12730 |
| stroke 4 | 39 % → 26 % | 542.6 px | 0.48 | 0.66 | 11120 |
| stroke 5 | 48 % → 27 % | 788.1 px | 0.51 | 0.56 | 5791 |

Numbers say: wet paint spreads well beyond the stroke.

## Oil focus · H narrow — own sheet
own sheet 2000 × 1320 · Gouache 1.00 + turpentine 15 % · 200 px · 66.6 s

![Oil focus · H narrow — own sheet](Oil-focus-H-narrow-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 20 % → 41 % | 189.4 px | 0.50 | 2.09 | 7210 |
| stroke 2 | 24 % → 23 % | 228.4 px | 0.37 | 0.98 | 5864 |
| stroke 3 | 34 % → 27 % | 270.6 px | 0.41 | 0.80 | 7072 |
| stroke 4 | 36 % → 28 % | 395.5 px | 0.48 | 0.77 | 6967 |
| stroke 5 | 48 % → 31 % | 611.3 px | 0.52 | 0.64 | 3868 |

Numbers say: wet paint spreads well beyond the stroke.

