![All brushes](contact.png)

# Brush Lab — 16 brushes · 9 Nov 2026 at 00:35

Every sheet: 1500 × 600, ten strokes in a 5 × 2 grid — 1. light line · 2. heavy line · 3. pressure swell · 4. fast wave · 5. slow wave · 6. spiral · 7. loop · 8. tilted · 9. over the wet one · 10. long, no reload (cell 8 holds «tilted» and «over the wet one» crossed). The CPU reference of Mamay's paint engine; the wet layer settles 20 s at the end.

Columns: **covered** = share of the cell with paint right after the stroke → after settling; **width** = painted area of the stroke ÷ its length (px); **dark** = mean darkness of the painted pixels above the paper's own grain (0 = paper, 1 = black); **spread** = how far wet paint went beyond the stroke (1.0 = stayed); **ms** = the stroke on the CPU; long stroke: paint in each quarter of its length (it should run out: wet → streaks → dry tail).

## Oil focus · A G x2
Gouache 1.00 + turpentine 15 % · 260 px · 101.5 s

![Oil focus · A G x2](Oil-focus-A-G-x2.png)

A light paint: laid on a grey sheet (on white it cannot be seen); **dark** = how far it is from the grey either way.

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 32 % → 14 % | 92.9 px | 0.28 | 0.45 | 1135 |
| heavy line | 59 % → 50 % | 170.1 px | 0.32 | 0.85 | 1517 |
| pressure swell | 51 % → 47 % | 191.1 px | 0.30 | 0.92 | 1121 |
| fast wave | 96 % → 91 % | 111.1 px | 0.27 | 0.94 | 4362 |
| slow wave | 95 % → 73 % | 109.7 px | 0.32 | 0.77 | 8692 |
| spiral | 100 % → 66 % | 66.0 px | 0.31 | 0.66 | 8798 |
| loop | 97 % → 69 % | 125.1 px | 0.29 | 0.71 | 3554 |
| tilted | 52 % → 52 % | 144.2 px | 0.27 | 1.00 | 2791 |
| over the wet one | 69 % → 66 % | 47.3 px | 0.27 | 0.97 | 1878 |
| long, no reload | 100 % → 90 % | 44.7 px | 0.31 | 0.90 | 10580 | quarters: 0.00 → 0.00 → 0.00 → 0.00

Numbers say: light vs heavy: width 92.9 → 170.1 px, dark 0.28 → 0.32.

## Oil focus · B G x2 soft
Gouache 1.00 + turpentine 15 % · 260 px · 100.6 s

![Oil focus · B G x2 soft](Oil-focus-B-G-x2-soft.png)

A light paint: laid on a grey sheet (on white it cannot be seen); **dark** = how far it is from the grey either way.

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 32 % → 14 % | 92.3 px | 0.28 | 0.44 | 1155 |
| heavy line | 58 % → 49 % | 169.4 px | 0.32 | 0.84 | 1540 |
| pressure swell | 51 % → 46 % | 190.2 px | 0.30 | 0.92 | 1213 |
| fast wave | 96 % → 91 % | 111.4 px | 0.27 | 0.94 | 4525 |
| slow wave | 95 % → 72 % | 109.2 px | 0.31 | 0.76 | 8712 |
| spiral | 100 % → 64 % | 66.0 px | 0.31 | 0.64 | 8774 |
| loop | 97 % → 67 % | 126.2 px | 0.28 | 0.69 | 3632 |
| tilted | 52 % → 52 % | 146.1 px | 0.27 | 1.00 | 2640 |
| over the wet one | 69 % → 65 % | 47.0 px | 0.27 | 0.94 | 1712 |
| long, no reload | 100 % → 91 % | 44.7 px | 0.31 | 0.91 | 10953 | quarters: 0.00 → 0.00 → 0.00 → 0.00

Numbers say: light vs heavy: width 92.3 → 169.4 px, dark 0.28 → 0.32.

## Oil focus · C G x2 mix low
Gouache 1.00 + turpentine 15 % · 260 px · 99.5 s

![Oil focus · C G x2 mix low](Oil-focus-C-G-x2-mix-low.png)

A light paint: laid on a grey sheet (on white it cannot be seen); **dark** = how far it is from the grey either way.

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 32 % → 14 % | 92.9 px | 0.22 | 0.45 | 1237 |
| heavy line | 59 % → 50 % | 170.1 px | 0.33 | 0.85 | 1514 |
| pressure swell | 51 % → 47 % | 191.1 px | 0.29 | 0.92 | 1170 |
| fast wave | 96 % → 91 % | 111.1 px | 0.19 | 0.94 | 4349 |
| slow wave | 95 % → 73 % | 109.7 px | 0.30 | 0.77 | 8447 |
| spiral | 100 % → 66 % | 66.0 px | 0.27 | 0.66 | 8617 |
| loop | 97 % → 69 % | 125.1 px | 0.29 | 0.71 | 3639 |
| tilted | 52 % → 52 % | 144.2 px | 0.20 | 1.00 | 2473 |
| over the wet one | 69 % → 66 % | 47.3 px | 0.20 | 0.97 | 1836 |
| long, no reload | 100 % → 90 % | 44.7 px | 0.28 | 0.90 | 10307 | quarters: 0.00 → 0.00 → 0.00 → 0.00

Numbers say: light vs heavy: width 92.9 → 170.1 px, dark 0.22 → 0.33.

## Oil focus · D G x2 no pickup
Gouache 1.00 + turpentine 15 % · 260 px · 100.2 s

![Oil focus · D G x2 no pickup](Oil-focus-D-G-x2-no-pickup.png)

A light paint: laid on a grey sheet (on white it cannot be seen); **dark** = how far it is from the grey either way.

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 32 % → 14 % | 92.9 px | 0.28 | 0.45 | 1183 |
| heavy line | 59 % → 50 % | 170.1 px | 0.32 | 0.85 | 1528 |
| pressure swell | 51 % → 47 % | 191.1 px | 0.30 | 0.93 | 1199 |
| fast wave | 96 % → 91 % | 111.1 px | 0.27 | 0.94 | 4481 |
| slow wave | 95 % → 73 % | 109.2 px | 0.32 | 0.77 | 8460 |
| spiral | 100 % → 65 % | 66.0 px | 0.31 | 0.65 | 9004 |
| loop | 97 % → 69 % | 125.1 px | 0.29 | 0.71 | 3583 |
| tilted | 52 % → 52 % | 144.2 px | 0.27 | 1.00 | 2797 |
| over the wet one | 69 % → 66 % | 47.2 px | 0.27 | 0.96 | 1889 |
| long, no reload | 100 % → 89 % | 44.7 px | 0.31 | 0.89 | 10700 | quarters: 0.00 → 0.00 → 0.00 → 0.00

Numbers say: light vs heavy: width 92.9 → 170.1 px, dark 0.28 → 0.32.

## Oil focus · E G x2 dilute 0.3
Gouache 1.00 + turpentine 30 % · 260 px · 100.0 s

![Oil focus · E G x2 dilute 0.3](Oil-focus-E-G-x2-dilute-0-3.png)

A light paint: laid on a grey sheet (on white it cannot be seen); **dark** = how far it is from the grey either way.

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 32 % → 13 % | 92.0 px | 0.28 | 0.42 | 1162 |
| heavy line | 58 % → 49 % | 169.8 px | 0.34 | 0.84 | 1577 |
| pressure swell | 51 % → 46 % | 190.3 px | 0.32 | 0.90 | 1234 |
| fast wave | 96 % → 90 % | 111.1 px | 0.29 | 0.93 | 4338 |
| slow wave | 94 % → 71 % | 109.0 px | 0.32 | 0.76 | 8431 |
| spiral | 100 % → 60 % | 66.0 px | 0.32 | 0.60 | 9030 |
| loop | 96 % → 62 % | 124.7 px | 0.27 | 0.65 | 3591 |
| tilted | 52 % → 52 % | 143.9 px | 0.28 | 1.00 | 2780 |
| over the wet one | 68 % → 65 % | 47.2 px | 0.28 | 0.95 | 1766 |
| long, no reload | 100 % → 89 % | 44.7 px | 0.31 | 0.89 | 10701 | quarters: 0.00 → 0.00 → 0.00 → 0.00

Numbers say: light vs heavy: width 92.0 → 169.8 px, dark 0.28 → 0.34.

## Oil focus · F G x2 wet load
Gouache 1.00 + turpentine 15 % · 260 px · 110.1 s

![Oil focus · F G x2 wet load](Oil-focus-F-G-x2-wet-load.png)

A light paint: laid on a grey sheet (on white it cannot be seen); **dark** = how far it is from the grey either way.

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 65 % → 53 % | 187.6 px | 0.30 | 0.81 | 1489 |
| heavy line | 68 % → 57 % | 197.2 px | 0.31 | 0.84 | 1669 |
| pressure swell | 64 % → 65 % | 240.9 px | 0.28 | 1.02 | 1226 |
| fast wave | 99 % → 91 % | 114.8 px | 0.26 | 0.92 | 4879 |
| slow wave | 100 % → 75 % | 115.1 px | 0.30 | 0.76 | 9396 |
| spiral | 100 % → 75 % | 65.9 px | 0.30 | 0.76 | 8878 |
| loop | 100 % → 96 % | 129.5 px | 0.30 | 0.96 | 4304 |
| tilted | 54 % → 54 % | 151.6 px | 0.27 | 1.00 | 2870 |
| over the wet one | 90 % → 80 % | 101.0 px | 0.27 | 0.88 | 2042 |
| long, no reload | 100 % → 90 % | 44.8 px | 0.29 | 0.90 | 12919 | quarters: 0.00 → 0.00 → 0.00 → 0.00

Numbers say: light vs heavy: width 187.6 → 197.2 px, dark 0.30 → 0.31; pressure barely changes the width.

## Oil focus · G G x2 fine hairs
Gouache 1.00 + turpentine 15 % · 260 px · 100.8 s

![Oil focus · G G x2 fine hairs](Oil-focus-G-G-x2-fine-hairs.png)

A light paint: laid on a grey sheet (on white it cannot be seen); **dark** = how far it is from the grey either way.

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 32 % → 14 % | 91.5 px | 0.28 | 0.44 | 1183 |
| heavy line | 58 % → 46 % | 167.4 px | 0.32 | 0.81 | 1496 |
| pressure swell | 50 % → 49 % | 187.8 px | 0.30 | 0.98 | 1226 |
| fast wave | 96 % → 89 % | 111.2 px | 0.27 | 0.92 | 4410 |
| slow wave | 93 % → 69 % | 107.1 px | 0.31 | 0.74 | 8628 |
| spiral | 100 % → 61 % | 66.0 px | 0.30 | 0.61 | 9016 |
| loop | 98 % → 73 % | 126.6 px | 0.29 | 0.75 | 3597 |
| tilted | 52 % → 52 % | 146.2 px | 0.26 | 1.00 | 2782 |
| over the wet one | 69 % → 62 % | 46.9 px | 0.26 | 0.89 | 1851 |
| long, no reload | 100 % → 91 % | 44.7 px | 0.30 | 0.91 | 10791 | quarters: 0.00 → 0.00 → 0.00 → 0.00

Numbers say: light vs heavy: width 91.5 → 167.4 px, dark 0.28 → 0.32.

## Oil focus · H flat x2 soft
Gouache 1.00 + turpentine 15 % · 260 px · 96.9 s

![Oil focus · H flat x2 soft](Oil-focus-H-flat-x2-soft.png)

A light paint: laid on a grey sheet (on white it cannot be seen); **dark** = how far it is from the grey either way.

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 26 % → 17 % | 75.7 px | 0.28 | 0.65 | 1027 |
| heavy line | 56 % → 48 % | 162.7 px | 0.34 | 0.86 | 1400 |
| pressure swell | 48 % → 45 % | 179.9 px | 0.32 | 0.94 | 1036 |
| fast wave | 94 % → 84 % | 108.2 px | 0.29 | 0.90 | 4132 |
| slow wave | 96 % → 70 % | 111.0 px | 0.33 | 0.73 | 8021 |
| spiral | 100 % → 86 % | 66.0 px | 0.32 | 0.86 | 8569 |
| loop | 95 % → 63 % | 123.6 px | 0.31 | 0.66 | 3755 |
| tilted | 50 % → 50 % | 139.4 px | 0.29 | 1.00 | 2434 |
| over the wet one | 67 % → 64 % | 46.5 px | 0.29 | 0.96 | 1443 |
| long, no reload | 100 % → 91 % | 44.7 px | 0.32 | 0.91 | 10397 | quarters: 0.00 → 0.00 → 0.00 → 0.00

Numbers say: light vs heavy: width 75.7 → 162.7 px, dark 0.28 → 0.34.

## Oil focus · A G x2 — own sheet
own sheet 2000 × 1320 · Gouache 1.00 + turpentine 15 % · 260 px · 74.7 s

![Oil focus · A G x2 — own sheet](Oil-focus-A-G-x2-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 15 % → 47 % | 190.7 px | 0.49 | 3.03 | 5681 |
| stroke 2 | 28 % → 38 % | 348.7 px | 0.43 | 1.36 | 5200 |
| stroke 3 | 29 % → 35 % | 275.0 px | 0.48 | 1.20 | 9315 |
| stroke 4 | 35 % → 33 % | 489.2 px | 0.50 | 0.95 | 9961 |
| stroke 5 | 44 % → 38 % | 715.4 px | 0.52 | 0.86 | 4880 |

Numbers say: wet paint spreads well beyond the stroke.

## Oil focus · B G x2 soft — own sheet
own sheet 2000 × 1320 · Gouache 1.00 + turpentine 15 % · 260 px · 74.4 s

![Oil focus · B G x2 soft — own sheet](Oil-focus-B-G-x2-soft-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 15 % → 46 % | 189.9 px | 0.49 | 3.01 | 5660 |
| stroke 2 | 28 % → 37 % | 347.0 px | 0.43 | 1.33 | 5203 |
| stroke 3 | 29 % → 35 % | 274.7 px | 0.47 | 1.18 | 9479 |
| stroke 4 | 35 % → 33 % | 486.8 px | 0.50 | 0.93 | 9752 |
| stroke 5 | 44 % → 37 % | 712.8 px | 0.52 | 0.85 | 4727 |

Numbers say: wet paint spreads well beyond the stroke.

## Oil focus · C G x2 mix low — own sheet
own sheet 2000 × 1320 · Gouache 1.00 + turpentine 15 % · 260 px · 64.2 s

![Oil focus · C G x2 mix low — own sheet](Oil-focus-C-G-x2-mix-low-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 15 % → 47 % | 190.7 px | 0.47 | 3.03 | 6480 |
| stroke 2 | 28 % → 38 % | 348.7 px | 0.43 | 1.36 | 6271 |
| stroke 3 | 29 % → 35 % | 275.0 px | 0.46 | 1.20 | 9761 |
| stroke 4 | 35 % → 33 % | 489.2 px | 0.49 | 0.95 | 8223 |
| stroke 5 | 44 % → 38 % | 715.4 px | 0.50 | 0.86 | 4252 |

Numbers say: wet paint spreads well beyond the stroke.

## Oil focus · D G x2 no pickup — own sheet
own sheet 2000 × 1320 · Gouache 1.00 + turpentine 15 % · 260 px · 63.0 s

![Oil focus · D G x2 no pickup — own sheet](Oil-focus-D-G-x2-no-pickup-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 15 % → 46 % | 190.6 px | 0.49 | 3.01 | 5974 |
| stroke 2 | 28 % → 38 % | 348.5 px | 0.43 | 1.34 | 6170 |
| stroke 3 | 29 % → 35 % | 274.9 px | 0.47 | 1.19 | 8864 |
| stroke 4 | 35 % → 33 % | 488.9 px | 0.50 | 0.94 | 8658 |
| stroke 5 | 44 % → 37 % | 714.7 px | 0.52 | 0.85 | 4033 |

Numbers say: wet paint spreads well beyond the stroke.

## Oil focus · E G x2 dilute 0.3 — own sheet
own sheet 2000 × 1320 · Gouache 1.00 + turpentine 30 % · 260 px · 56.6 s

![Oil focus · E G x2 dilute 0.3 — own sheet](Oil-focus-E-G-x2-dilute-0-3-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 15 % → 47 % | 190.7 px | 0.46 | 3.02 | 6446 |
| stroke 2 | 28 % → 38 % | 348.7 px | 0.40 | 1.33 | 4453 |
| stroke 3 | 29 % → 35 % | 274.5 px | 0.45 | 1.18 | 7339 |
| stroke 4 | 35 % → 33 % | 488.5 px | 0.47 | 0.93 | 7268 |
| stroke 5 | 44 % → 37 % | 714.1 px | 0.49 | 0.85 | 3637 |

Numbers say: wet paint spreads well beyond the stroke.

## Oil focus · F G x2 wet load — own sheet
own sheet 2000 × 1320 · Gouache 1.00 + turpentine 15 % · 260 px · 55.7 s

![Oil focus · F G x2 wet load — own sheet](Oil-focus-F-G-x2-wet-load-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 15 % → 52 % | 190.2 px | 0.49 | 3.35 | 5976 |
| stroke 2 | 28 % → 36 % | 348.2 px | 0.40 | 1.26 | 4414 |
| stroke 3 | 32 % → 35 % | 298.5 px | 0.46 | 1.08 | 7690 |
| stroke 4 | 38 % → 33 % | 531.4 px | 0.49 | 0.87 | 7396 |
| stroke 5 | 48 % → 38 % | 789.3 px | 0.51 | 0.78 | 3785 |

Numbers say: wet paint spreads well beyond the stroke.

## Oil focus · G G x2 fine hairs — own sheet
own sheet 2000 × 1320 · Gouache 1.00 + turpentine 15 % · 260 px · 53.2 s

![Oil focus · G G x2 fine hairs — own sheet](Oil-focus-G-G-x2-fine-hairs-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 15 % → 44 % | 187.7 px | 0.49 | 2.88 | 5685 |
| stroke 2 | 28 % → 33 % | 341.7 px | 0.42 | 1.20 | 4305 |
| stroke 3 | 29 % → 33 % | 272.4 px | 0.46 | 1.14 | 6814 |
| stroke 4 | 35 % → 30 % | 479.6 px | 0.50 | 0.86 | 6973 |
| stroke 5 | 43 % → 33 % | 701.9 px | 0.53 | 0.77 | 3381 |

Numbers say: wet paint spreads well beyond the stroke.

## Oil focus · H flat x2 soft — own sheet
own sheet 2000 × 1320 · Gouache 1.00 + turpentine 15 % · 260 px · 51.9 s

![Oil focus · H flat x2 soft — own sheet](Oil-focus-H-flat-x2-soft-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 15 % → 45 % | 188.1 px | 0.48 | 2.94 | 5238 |
| stroke 2 | 27 % → 36 % | 338.7 px | 0.43 | 1.31 | 4122 |
| stroke 3 | 29 % → 34 % | 268.3 px | 0.47 | 1.18 | 6537 |
| stroke 4 | 34 % → 31 % | 474.4 px | 0.49 | 0.92 | 6227 |
| stroke 5 | 42 % → 35 % | 689.0 px | 0.51 | 0.84 | 3451 |

Numbers say: wet paint spreads well beyond the stroke.

