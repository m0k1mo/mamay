![All brushes](contact.png)

# Brush Lab — 126 brushes · 10 Nov 2026 at 00:54

Every sheet: 1500 × 600, ten strokes in a 5 × 2 grid — 1. light line · 2. heavy line · 3. pressure swell · 4. fast wave · 5. slow wave · 6. spiral · 7. loop · 8. tilted · 9. over the wet one · 10. long, no reload (cell 8 holds «tilted» and «over the wet one» crossed). The CPU reference of Mamay's paint engine; the wet layer settles 20 s at the end.

Columns: **covered** = share of the cell with paint right after the stroke → after settling; **width** = painted area of the stroke ÷ its length (px); **dark** = mean darkness of the painted pixels above the paper's own grain (0 = paper, 1 = black); **spread** = how far wet paint went beyond the stroke (1.0 = stayed); **ms** = the stroke on the CPU; long stroke: paint in each quarter of its length (it should run out: wet → streaks → dry tail).

## Oil focus · A best filbert
Gouache 1.00 + turpentine 15 % · 260 px · 304.7 s

![Oil focus · A best filbert](Oil-focus-A-best-filbert.png)

A light paint: laid on a grey sheet (on white it cannot be seen); **dark** = how far it is from the grey either way.

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 74 % → 71 % | 213.6 px | 0.28 | 0.96 | 2248 |
| heavy line | 76 % → 67 % | 219.4 px | 0.28 | 0.89 | 3010 |
| pressure swell | 67 % → 73 % | 250.3 px | 0.25 | 1.10 | 2365 |
| fast wave | 99 % → 84 % | 114.7 px | 0.25 | 0.85 | 11052 |
| slow wave | 100 % → 69 % | 115.0 px | 0.28 | 0.69 | 19783 |
| spiral | 100 % → 74 % | 65.9 px | 0.27 | 0.74 | 18137 |
| loop | 100 % → 86 % | 129.5 px | 0.28 | 0.86 | 33998 |
| tilted | 55 % → 55 % | 154.0 px | 0.24 | 1.00 | 3935 |
| over the wet one | 92 % → 86 % | 103.5 px | 0.24 | 0.93 | 4450 |
| long, no reload | 100 % → 61 % | 44.8 px | 0.28 | 0.61 | 29707 | quarters: 0.00 → 0.00 → 0.00 → 0.01

Numbers say: light vs heavy: width 213.6 → 219.4 px, dark 0.28 → 0.28; pressure barely changes the width.

## Oil focus · B flat
Gouache 1.00 + turpentine 15 % · 260 px · 286.2 s

![Oil focus · B flat](Oil-focus-B-flat.png)

A light paint: laid on a grey sheet (on white it cannot be seen); **dark** = how far it is from the grey either way.

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 69 % → 69 % | 200.8 px | 0.29 | 1.00 | 1867 |
| heavy line | 71 % → 65 % | 204.9 px | 0.30 | 0.92 | 2585 |
| pressure swell | 61 % → 69 % | 230.2 px | 0.26 | 1.12 | 1632 |
| fast wave | 99 % → 81 % | 114.1 px | 0.26 | 0.82 | 9383 |
| slow wave | 99 % → 69 % | 114.9 px | 0.29 | 0.70 | 16013 |
| spiral | 100 % → 76 % | 65.9 px | 0.29 | 0.76 | 14172 |
| loop | 100 % → 85 % | 129.3 px | 0.29 | 0.85 | 8663 |
| tilted | 52 % → 52 % | 145.5 px | 0.26 | 1.00 | 8459 |
| over the wet one | 89 % → 85 % | 102.0 px | 0.26 | 0.96 | 12104 |
| long, no reload | 100 % → 63 % | 44.8 px | 0.28 | 0.63 | 22324 | quarters: 0.00 → 0.00 → 0.00 → 0.01

Numbers say: light vs heavy: width 200.8 → 204.9 px, dark 0.29 → 0.30; pressure barely changes the width.

## Oil focus · C round
Gouache 1.00 + turpentine 15 % · 260 px · 250.1 s

![Oil focus · C round](Oil-focus-C-round.png)

A light paint: laid on a grey sheet (on white it cannot be seen); **dark** = how far it is from the grey either way.

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 44 % → 37 % | 126.8 px | 0.36 | 0.85 | 1051 |
| heavy line | 56 % → 51 % | 163.1 px | 0.35 | 0.91 | 2207 |
| pressure swell | 41 % → 42 % | 152.5 px | 0.31 | 1.02 | 1553 |
| fast wave | 89 % → 83 % | 103.2 px | 0.30 | 0.93 | 7368 |
| slow wave | 90 % → 71 % | 104.3 px | 0.35 | 0.78 | 10509 |
| spiral | 93 % → 76 % | 61.6 px | 0.35 | 0.81 | 10813 |
| loop | 78 % → 72 % | 100.6 px | 0.35 | 0.92 | 4837 |
| tilted | 48 % → 48 % | 133.3 px | 0.32 | 1.00 | 4297 |
| over the wet one | 83 % → 75 % | 97.5 px | 0.32 | 0.91 | 2755 |
| long, no reload | 100 % → 65 % | 44.8 px | 0.34 | 0.65 | 51979 | quarters: 0.00 → 0.00 → 0.00 → 0.00

Numbers say: light vs heavy: width 126.8 → 163.1 px, dark 0.36 → 0.35.

## Oil focus · D worn
Gouache 1.00 + turpentine 15 % · 260 px · 304.3 s

![Oil focus · D worn](Oil-focus-D-worn.png)

A light paint: laid on a grey sheet (on white it cannot be seen); **dark** = how far it is from the grey either way.

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 69 % → 68 % | 200.0 px | 0.29 | 0.99 | 2439 |
| heavy line | 80 % → 69 % | 231.1 px | 0.29 | 0.86 | 3710 |
| pressure swell | 74 % → 75 % | 278.5 px | 0.27 | 1.01 | 2962 |
| fast wave | 97 % → 90 % | 112.4 px | 0.27 | 0.92 | 10738 |
| slow wave | 96 % → 68 % | 110.8 px | 0.29 | 0.71 | 17491 |
| spiral | 97 % → 88 % | 64.3 px | 0.28 | 0.90 | 16254 |
| loop | 97 % → 83 % | 126.1 px | 0.29 | 0.85 | 33201 |
| tilted | 57 % → 57 % | 160.2 px | 0.27 | 1.00 | 4958 |
| over the wet one | 94 % → 88 % | 103.1 px | 0.27 | 0.93 | 5127 |
| long, no reload | 100 % → 61 % | 44.6 px | 0.28 | 0.61 | 26854 | quarters: 0.00 → 0.00 → 0.00 → 0.02

Numbers say: light vs heavy: width 200.0 → 231.1 px, dark 0.29 → 0.29.

## Oil focus · E swell
Gouache 1.00 + turpentine 15 % · 260 px · 305.7 s

![Oil focus · E swell](Oil-focus-E-swell.png)

A light paint: laid on a grey sheet (on white it cannot be seen); **dark** = how far it is from the grey either way.

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 73 % → 70 % | 212.6 px | 0.28 | 0.95 | 1968 |
| heavy line | 77 % → 68 % | 224.3 px | 0.28 | 0.87 | 4030 |
| pressure swell | 67 % → 74 % | 249.4 px | 0.25 | 1.11 | 2559 |
| fast wave | 99 % → 84 % | 114.7 px | 0.25 | 0.85 | 10804 |
| slow wave | 100 % → 69 % | 115.0 px | 0.28 | 0.69 | 19282 |
| spiral | 100 % → 73 % | 65.9 px | 0.27 | 0.73 | 18606 |
| loop | 100 % → 86 % | 129.5 px | 0.27 | 0.86 | 35381 |
| tilted | 55 % → 55 % | 154.4 px | 0.24 | 1.00 | 3846 |
| over the wet one | 92 % → 86 % | 103.1 px | 0.24 | 0.93 | 4505 |
| long, no reload | 100 % → 60 % | 44.8 px | 0.27 | 0.60 | 29801 | quarters: 0.00 → 0.00 → 0.00 → 0.01

Numbers say: light vs heavy: width 212.6 → 224.3 px, dark 0.28 → 0.28; pressure barely changes the width.

## Oil focus · F steady hand
Gouache 1.00 + turpentine 15 % · 260 px · 304.5 s

![Oil focus · F steady hand](Oil-focus-F-steady-hand.png)

A light paint: laid on a grey sheet (on white it cannot be seen); **dark** = how far it is from the grey either way.

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 73 % → 70 % | 212.8 px | 0.28 | 0.95 | 2228 |
| heavy line | 75 % → 67 % | 218.0 px | 0.28 | 0.89 | 3063 |
| pressure swell | 66 % → 73 % | 248.7 px | 0.25 | 1.10 | 2204 |
| fast wave | 99 % → 84 % | 114.7 px | 0.25 | 0.85 | 11342 |
| slow wave | 100 % → 69 % | 115.0 px | 0.28 | 0.70 | 20224 |
| spiral | 100 % → 73 % | 65.9 px | 0.27 | 0.73 | 18010 |
| loop | 100 % → 86 % | 129.5 px | 0.28 | 0.86 | 34715 |
| tilted | 55 % → 55 % | 153.5 px | 0.24 | 1.00 | 3849 |
| over the wet one | 92 % → 85 % | 103.7 px | 0.24 | 0.93 | 4440 |
| long, no reload | 100 % → 59 % | 44.8 px | 0.27 | 0.59 | 30691 | quarters: 0.00 → 0.00 → 0.00 → 0.02

Numbers say: light vs heavy: width 212.8 → 218.0 px, dark 0.28 → 0.28; pressure barely changes the width.

## Oil focus · G soft hairs
Gouache 1.00 + turpentine 15 % · 260 px · 295.7 s

![Oil focus · G soft hairs](Oil-focus-G-soft-hairs.png)

A light paint: laid on a grey sheet (on white it cannot be seen); **dark** = how far it is from the grey either way.

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 73 % → 72 % | 212.6 px | 0.27 | 0.98 | 2278 |
| heavy line | 75 % → 65 % | 216.9 px | 0.27 | 0.86 | 2952 |
| pressure swell | 66 % → 73 % | 246.8 px | 0.24 | 1.11 | 2104 |
| fast wave | 99 % → 75 % | 114.6 px | 0.24 | 0.75 | 10618 |
| slow wave | 100 % → 60 % | 115.0 px | 0.27 | 0.60 | 18170 |
| spiral | 100 % → 68 % | 65.9 px | 0.26 | 0.68 | 16428 |
| loop | 100 % → 73 % | 129.5 px | 0.27 | 0.73 | 14917 |
| tilted | 56 % → 56 % | 156.1 px | 0.23 | 1.00 | 8130 |
| over the wet one | 92 % → 85 % | 100.9 px | 0.23 | 0.92 | 3700 |
| long, no reload | 100 % → 61 % | 44.8 px | 0.26 | 0.61 | 27694 | quarters: 0.00 → 0.00 → 0.00 → 0.01

Numbers say: light vs heavy: width 212.6 → 216.9 px, dark 0.27 → 0.27; pressure barely changes the width.

## Oil focus · H narrow
Gouache 1.00 + turpentine 15 % · 200 px · 252.2 s

![Oil focus · H narrow](Oil-focus-H-narrow.png)

A light paint: laid on a grey sheet (on white it cannot be seen); **dark** = how far it is from the grey either way.

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 60 % → 54 % | 174.3 px | 0.31 | 0.90 | 1545 |
| heavy line | 62 % → 54 % | 179.4 px | 0.31 | 0.88 | 1870 |
| pressure swell | 50 % → 57 % | 188.4 px | 0.28 | 1.14 | 1513 |
| fast wave | 94 % → 69 % | 108.6 px | 0.27 | 0.73 | 7242 |
| slow wave | 96 % → 61 % | 110.5 px | 0.31 | 0.64 | 12346 |
| spiral | 99 % → 60 % | 65.0 px | 0.29 | 0.61 | 11297 |
| loop | 93 % → 70 % | 120.0 px | 0.31 | 0.76 | 4876 |
| tilted | 45 % → 45 % | 124.5 px | 0.27 | 1.00 | 3087 |
| over the wet one | 84 % → 77 % | 108.8 px | 0.27 | 0.92 | 2872 |
| long, no reload | 100 % → 52 % | 44.8 px | 0.29 | 0.52 | 49577 | quarters: 0.00 → 0.00 → 0.00 → 0.02

Numbers say: light vs heavy: width 174.3 → 179.4 px, dark 0.31 → 0.31; pressure barely changes the width.

## Refs v3 · #01 HW peach cloud
Gouache 1.00 + turpentine 30 % · 104 px · 172.2 s

![Refs v3 · #01 HW peach cloud](Refs-v3-01-HW-peach-cloud.png)

A light paint: laid on a grey sheet (on white it cannot be seen); **dark** = how far it is from the grey either way.

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 31 % → 29 % | 90.5 px | 0.32 | 0.94 | 725 |
| heavy line | 32 % → 30 % | 93.9 px | 0.33 | 0.92 | 698 |
| pressure swell | 25 % → 24 % | 93.1 px | 0.30 | 0.98 | 632 |
| fast wave | 68 % → 37 % | 78.5 px | 0.26 | 0.55 | 2332 |
| slow wave | 67 % → 38 % | 77.2 px | 0.30 | 0.57 | 3856 |
| spiral | 80 % → 39 % | 53.0 px | 0.27 | 0.49 | 3990 |
| loop | 60 % → 44 % | 77.9 px | 0.31 | 0.73 | 1740 |
| tilted | 25 % → 25 % | 68.8 px | 0.30 | 1.00 | 1274 |
| over the wet one | 51 % → 48 % | 73.4 px | 0.30 | 0.93 | 896 |
| long, no reload | 96 % → 47 % | 43.2 px | 0.31 | 0.48 | 5468 | quarters: 0.00 → 0.00 → 0.00 → 0.00

Numbers say: light vs heavy: width 90.5 → 93.9 px, dark 0.32 → 0.33; pressure barely changes the width; the long stroke does not run out of paint.

## Refs v3 · #02 HW cream strokes
Gouache 1.00 + turpentine 30 % · 51 px · 111.0 s

![Refs v3 · #02 HW cream strokes](Refs-v3-02-HW-cream-strokes.png)

A light paint: laid on a grey sheet (on white it cannot be seen); **dark** = how far it is from the grey either way.

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 16 % → 15 % | 46.3 px | 0.38 | 0.95 | 440 |
| heavy line | 17 % → 15 % | 48.2 px | 0.35 | 0.93 | 335 |
| pressure swell | 13 % → 12 % | 47.3 px | 0.36 | 0.95 | 259 |
| fast wave | 39 % → 18 % | 45.5 px | 0.30 | 0.47 | 970 |
| slow wave | 40 % → 21 % | 46.4 px | 0.34 | 0.52 | 1473 |
| spiral | 60 % → 23 % | 39.3 px | 0.33 | 0.39 | 1675 |
| loop | 34 % → 21 % | 44.5 px | 0.36 | 0.60 | 1140 |
| tilted | 14 % → 14 % | 40.2 px | 0.32 | 1.00 | 555 |
| over the wet one | 30 % → 26 % | 42.6 px | 0.32 | 0.89 | 416 |
| long, no reload | 75 % → 21 % | 33.5 px | 0.32 | 0.28 | 1738 | quarters: 0.01 → 0.01 → 0.01 → 0.01

Numbers say: light vs heavy: width 46.3 → 48.2 px, dark 0.38 → 0.35; pressure barely changes the width; the long stroke does not run out of paint.

## Refs v3 · #03 HW navy contours
Gouache 1.00 + turpentine 30 % · 80 px · 122.7 s

![Refs v3 · #03 HW navy contours](Refs-v3-03-HW-navy-contours.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 24 % → 23 % | 69.7 px | 0.26 | 0.96 | 1678 |
| heavy line | 26 % → 24 % | 74.3 px | 0.27 | 0.93 | 1146 |
| pressure swell | 19 % → 19 % | 72.1 px | 0.30 | 0.97 | 527 |
| fast wave | 57 % → 30 % | 66.2 px | 0.31 | 0.52 | 1837 |
| slow wave | 56 % → 33 % | 65.2 px | 0.29 | 0.59 | 2656 |
| spiral | 71 % → 34 % | 47.1 px | 0.32 | 0.47 | 2747 |
| loop | 50 % → 33 % | 64.7 px | 0.29 | 0.67 | 1428 |
| tilted | 20 % → 20 % | 55.6 px | 0.31 | 1.01 | 990 |
| over the wet one | 42 % → 39 % | 61.2 px | 0.31 | 0.92 | 731 |
| long, no reload | 91 % → 32 % | 40.8 px | 0.32 | 0.36 | 4038 | quarters: 0.30 → 0.27 → 0.16 → 0.06

Numbers say: light vs heavy: width 69.7 → 74.3 px, dark 0.26 → 0.27; pressure barely changes the width.

## Refs v3 · #04 HW grey cloud
Gouache 1.00 + turpentine 30 % · 93 px · 122.9 s

![Refs v3 · #04 HW grey cloud](Refs-v3-04-HW-grey-cloud.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 28 % → 27 % | 81.7 px | 0.13 | 0.95 | 495 |
| heavy line | 29 % → 27 % | 84.7 px | 0.13 | 0.92 | 620 |
| pressure swell | 22 % → 22 % | 83.4 px | 0.16 | 0.97 | 840 |
| fast wave | 64 % → 38 % | 73.8 px | 0.21 | 0.59 | 2581 |
| slow wave | 62 % → 36 % | 72.2 px | 0.16 | 0.57 | 4410 |
| spiral | 74 % → 37 % | 49.0 px | 0.20 | 0.50 | 3072 |
| loop | 56 % → 40 % | 72.4 px | 0.11 | 0.71 | 2291 |
| tilted | 23 % → 23 % | 63.6 px | 0.18 | 1.00 | 997 |
| over the wet one | 47 % → 43 % | 68.5 px | 0.18 | 0.92 | 730 |
| long, no reload | 95 % → 37 % | 42.5 px | 0.18 | 0.39 | 7101 | quarters: 0.18 → 0.14 → 0.07 → 0.03

Numbers say: light vs heavy: width 81.7 → 84.7 px, dark 0.13 → 0.13; pressure barely changes the width.

## Refs v3 · #05 HW green in rust loops
Gouache 1.00 + turpentine 30 % · 104 px · 113.0 s

![Refs v3 · #05 HW green in rust loops](Refs-v3-05-HW-green-in-rust-loops.png)

A light paint: laid on a grey sheet (on white it cannot be seen); **dark** = how far it is from the grey either way.

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 31 % → 29 % | 90.5 px | 0.36 | 0.94 | 451 |
| heavy line | 32 % → 30 % | 93.9 px | 0.37 | 0.92 | 577 |
| pressure swell | 25 % → 24 % | 93.1 px | 0.34 | 0.98 | 458 |
| fast wave | 68 % → 37 % | 78.5 px | 0.30 | 0.55 | 1908 |
| slow wave | 67 % → 38 % | 77.2 px | 0.34 | 0.57 | 2910 |
| spiral | 80 % → 39 % | 53.0 px | 0.30 | 0.49 | 2838 |
| loop | 60 % → 44 % | 77.9 px | 0.35 | 0.73 | 2000 |
| tilted | 25 % → 25 % | 68.8 px | 0.33 | 1.00 | 1440 |
| over the wet one | 51 % → 48 % | 73.4 px | 0.33 | 0.93 | 1106 |
| long, no reload | 96 % → 47 % | 43.2 px | 0.35 | 0.48 | 4387 | quarters: 0.00 → 0.00 → 0.00 → 0.00

Numbers say: light vs heavy: width 90.5 → 93.9 px, dark 0.36 → 0.37; pressure barely changes the width; the long stroke does not run out of paint.

## Refs v3 · #06 HW scrubbed grey
Gouache 1.00 + turpentine 30 % · 93 px · 108.0 s

![Refs v3 · #06 HW scrubbed grey](Refs-v3-06-HW-scrubbed-grey.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 28 % → 27 % | 81.7 px | 0.13 | 0.95 | 392 |
| heavy line | 29 % → 27 % | 84.7 px | 0.13 | 0.92 | 600 |
| pressure swell | 22 % → 22 % | 83.4 px | 0.16 | 0.97 | 578 |
| fast wave | 64 % → 38 % | 73.8 px | 0.21 | 0.59 | 2161 |
| slow wave | 62 % → 36 % | 72.2 px | 0.16 | 0.57 | 3791 |
| spiral | 74 % → 37 % | 49.0 px | 0.20 | 0.50 | 2681 |
| loop | 56 % → 40 % | 72.4 px | 0.11 | 0.71 | 1681 |
| tilted | 23 % → 23 % | 63.6 px | 0.18 | 1.00 | 966 |
| over the wet one | 47 % → 43 % | 68.5 px | 0.18 | 0.92 | 716 |
| long, no reload | 95 % → 37 % | 42.5 px | 0.18 | 0.39 | 4605 | quarters: 0.18 → 0.14 → 0.07 → 0.03

Numbers say: light vs heavy: width 81.7 → 84.7 px, dark 0.13 → 0.13; pressure barely changes the width.

## Refs v3 · #07 HW blue L and zigzag
Gouache 1.00 + turpentine 30 % · 104 px · 116.6 s

![Refs v3 · #07 HW blue L and zigzag](Refs-v3-07-HW-blue-L-and-zigzag.png)

A light paint: laid on a grey sheet (on white it cannot be seen); **dark** = how far it is from the grey either way.

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 31 % → 29 % | 90.5 px | 0.39 | 0.94 | 485 |
| heavy line | 32 % → 30 % | 93.9 px | 0.40 | 0.92 | 941 |
| pressure swell | 25 % → 24 % | 93.1 px | 0.37 | 0.98 | 669 |
| fast wave | 68 % → 37 % | 78.5 px | 0.35 | 0.55 | 2746 |
| slow wave | 67 % → 38 % | 77.2 px | 0.38 | 0.57 | 3611 |
| spiral | 80 % → 39 % | 53.0 px | 0.35 | 0.49 | 3444 |
| loop | 60 % → 44 % | 77.9 px | 0.38 | 0.73 | 1919 |
| tilted | 25 % → 25 % | 68.8 px | 0.37 | 1.00 | 979 |
| over the wet one | 51 % → 48 % | 73.4 px | 0.37 | 0.93 | 818 |
| long, no reload | 96 % → 47 % | 43.2 px | 0.37 | 0.48 | 5587 | quarters: 0.00 → 0.00 → 0.00 → 0.00

Numbers say: light vs heavy: width 90.5 → 93.9 px, dark 0.39 → 0.40; pressure barely changes the width; the long stroke does not run out of paint.

## Refs v3 · #08 HW lilac crown basket
Gouache 1.00 + turpentine 30 % · 36 px · 57.0 s

![Refs v3 · #08 HW lilac crown basket](Refs-v3-08-HW-lilac-crown-basket.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 11 % → 11 % | 32.8 px | 0.13 | 0.99 | 125 |
| heavy line | 12 % → 12 % | 34.7 px | 0.14 | 1.00 | 153 |
| pressure swell | 9 % → 9 % | 35.1 px | 0.16 | 0.97 | 131 |
| fast wave | 30 % → 12 % | 35.0 px | 0.22 | 0.40 | 569 |
| slow wave | 30 % → 15 % | 34.1 px | 0.17 | 0.52 | 872 |
| spiral | 49 % → 17 % | 32.3 px | 0.15 | 0.35 | 728 |
| loop | 26 % → 14 % | 33.6 px | 0.13 | 0.55 | 438 |
| tilted | 12 % → 12 % | 33.6 px | 0.17 | 1.00 | 259 |
| over the wet one | 23 % → 21 % | 32.0 px | 0.17 | 0.87 | 213 |
| long, no reload | 56 % → 15 % | 25.2 px | 0.15 | 0.26 | 991 | quarters: 0.10 → 0.04 → 0.01 → 0.00

Numbers say: light vs heavy: width 32.8 → 34.7 px, dark 0.13 → 0.14; pressure barely changes the width.

## Refs v3 · #09 HW white loops
Gouache 1.00 + turpentine 30 % · 104 px · 111.9 s

![Refs v3 · #09 HW white loops](Refs-v3-09-HW-white-loops.png)

A light paint: laid on a grey sheet (on white it cannot be seen); **dark** = how far it is from the grey either way.

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 31 % → 29 % | 90.5 px | 0.39 | 0.94 | 432 |
| heavy line | 32 % → 30 % | 93.9 px | 0.40 | 0.92 | 598 |
| pressure swell | 25 % → 24 % | 93.1 px | 0.37 | 0.98 | 465 |
| fast wave | 68 % → 37 % | 78.5 px | 0.34 | 0.55 | 1717 |
| slow wave | 67 % → 38 % | 77.1 px | 0.38 | 0.57 | 2789 |
| spiral | 80 % → 39 % | 53.0 px | 0.35 | 0.49 | 3781 |
| loop | 60 % → 44 % | 77.9 px | 0.38 | 0.73 | 1535 |
| tilted | 25 % → 25 % | 68.8 px | 0.37 | 1.00 | 1194 |
| over the wet one | 51 % → 48 % | 73.4 px | 0.37 | 0.93 | 762 |
| long, no reload | 96 % → 45 % | 43.2 px | 0.37 | 0.47 | 4151 | quarters: 0.00 → 0.00 → 0.00 → 0.01

Numbers say: light vs heavy: width 90.5 → 93.9 px, dark 0.39 → 0.40; pressure barely changes the width; the long stroke does not run out of paint.

## Refs v3 · #10 HW maroon loops
Gouache 1.00 + turpentine 30 % · 104 px · 113.1 s

![Refs v3 · #10 HW maroon loops](Refs-v3-10-HW-maroon-loops.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 31 % → 29 % | 90.5 px | 0.25 | 0.94 | 414 |
| heavy line | 32 % → 30 % | 93.9 px | 0.24 | 0.92 | 581 |
| pressure swell | 25 % → 24 % | 93.1 px | 0.26 | 0.98 | 451 |
| fast wave | 68 % → 37 % | 78.5 px | 0.31 | 0.55 | 1744 |
| slow wave | 67 % → 38 % | 77.2 px | 0.26 | 0.57 | 2807 |
| spiral | 80 % → 39 % | 53.0 px | 0.31 | 0.49 | 3733 |
| loop | 60 % → 44 % | 77.9 px | 0.24 | 0.73 | 1571 |
| tilted | 25 % → 25 % | 68.8 px | 0.27 | 1.00 | 1479 |
| over the wet one | 51 % → 48 % | 73.4 px | 0.27 | 0.93 | 795 |
| long, no reload | 96 % → 47 % | 43.2 px | 0.24 | 0.48 | 4904 | quarters: 0.23 → 0.23 → 0.16 → 0.08

Numbers say: light vs heavy: width 90.5 → 93.9 px, dark 0.25 → 0.24; pressure barely changes the width.

## Refs v3 · #11 HW purple balls
Gouache 1.00 + turpentine 30 % · 104 px · 134.7 s

![Refs v3 · #11 HW purple balls](Refs-v3-11-HW-purple-balls.png)

A light paint: laid on a grey sheet (on white it cannot be seen); **dark** = how far it is from the grey either way.

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 31 % → 29 % | 90.5 px | 0.31 | 0.94 | 420 |
| heavy line | 32 % → 30 % | 93.9 px | 0.31 | 0.92 | 537 |
| pressure swell | 25 % → 24 % | 93.1 px | 0.29 | 0.98 | 454 |
| fast wave | 68 % → 37 % | 78.5 px | 0.24 | 0.55 | 2051 |
| slow wave | 67 % → 38 % | 77.2 px | 0.29 | 0.57 | 2940 |
| spiral | 80 % → 39 % | 53.0 px | 0.25 | 0.49 | 4121 |
| loop | 60 % → 44 % | 77.9 px | 0.30 | 0.73 | 1653 |
| tilted | 25 % → 25 % | 68.8 px | 0.28 | 1.00 | 942 |
| over the wet one | 51 % → 48 % | 73.4 px | 0.28 | 0.93 | 775 |
| long, no reload | 96 % → 47 % | 43.2 px | 0.30 | 0.48 | 4703 | quarters: 0.00 → 0.00 → 0.00 → 0.00

Numbers say: light vs heavy: width 90.5 → 93.9 px, dark 0.31 → 0.31; pressure barely changes the width; the long stroke does not run out of paint.

## Refs v3 · #12 HW black-olive cage
Gouache 1.00 + turpentine 30 % · 36 px · 59.8 s

![Refs v3 · #12 HW black-olive cage](Refs-v3-12-HW-black-olive-cage.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 11 % → 11 % | 32.8 px | 0.13 | 0.99 | 132 |
| heavy line | 12 % → 12 % | 34.7 px | 0.14 | 1.00 | 156 |
| pressure swell | 9 % → 9 % | 35.1 px | 0.16 | 0.97 | 125 |
| fast wave | 30 % → 12 % | 35.0 px | 0.22 | 0.40 | 479 |
| slow wave | 30 % → 15 % | 34.1 px | 0.17 | 0.52 | 923 |
| spiral | 49 % → 17 % | 32.3 px | 0.15 | 0.35 | 837 |
| loop | 26 % → 14 % | 33.6 px | 0.13 | 0.55 | 442 |
| tilted | 12 % → 12 % | 33.6 px | 0.17 | 1.00 | 259 |
| over the wet one | 23 % → 21 % | 32.0 px | 0.17 | 0.87 | 226 |
| long, no reload | 56 % → 15 % | 25.2 px | 0.15 | 0.26 | 1709 | quarters: 0.10 → 0.04 → 0.01 → 0.00

Numbers say: light vs heavy: width 32.8 → 34.7 px, dark 0.13 → 0.14; pressure barely changes the width.

## Refs v3 · #13 HW blue streaky form
Gouache 1.00 + turpentine 30 % · 104 px · 133.7 s

![Refs v3 · #13 HW blue streaky form](Refs-v3-13-HW-blue-streaky-form.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 31 % → 29 % | 90.5 px | 0.16 | 0.94 | 427 |
| heavy line | 32 % → 30 % | 93.9 px | 0.15 | 0.92 | 540 |
| pressure swell | 25 % → 24 % | 93.1 px | 0.18 | 0.98 | 471 |
| fast wave | 68 % → 37 % | 78.5 px | 0.22 | 0.55 | 2235 |
| slow wave | 67 % → 38 % | 77.2 px | 0.17 | 0.57 | 3023 |
| spiral | 80 % → 39 % | 53.0 px | 0.22 | 0.49 | 4083 |
| loop | 60 % → 44 % | 77.9 px | 0.15 | 0.73 | 1407 |
| tilted | 25 % → 25 % | 68.8 px | 0.18 | 1.00 | 899 |
| over the wet one | 51 % → 48 % | 73.4 px | 0.18 | 0.93 | 830 |
| long, no reload | 96 % → 47 % | 43.2 px | 0.15 | 0.48 | 4659 | quarters: 0.14 → 0.14 → 0.08 → 0.03

Numbers say: light vs heavy: width 90.5 → 93.9 px, dark 0.16 → 0.15; pressure barely changes the width.

## Refs v3 · #14 HW olive totem
Gouache 1.00 + turpentine 30 % · 57 px · 77.4 s

![Refs v3 · #14 HW olive totem](Refs-v3-14-HW-olive-totem.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 18 % → 17 % | 51.3 px | 0.29 | 0.95 | 217 |
| heavy line | 18 % → 18 % | 53.5 px | 0.28 | 0.95 | 257 |
| pressure swell | 14 % → 14 % | 52.2 px | 0.30 | 0.98 | 277 |
| fast wave | 44 % → 19 % | 51.3 px | 0.32 | 0.43 | 854 |
| slow wave | 44 % → 24 % | 50.3 px | 0.30 | 0.54 | 1519 |
| spiral | 63 % → 27 % | 41.8 px | 0.31 | 0.43 | 1489 |
| loop | 38 % → 24 % | 49.0 px | 0.29 | 0.63 | 877 |
| tilted | 15 % → 16 % | 43.1 px | 0.32 | 1.01 | 414 |
| over the wet one | 32 % → 28 % | 46.5 px | 0.32 | 0.88 | 372 |
| long, no reload | 80 % → 24 % | 35.9 px | 0.31 | 0.30 | 2060 | quarters: 0.26 → 0.21 → 0.09 → 0.03

Numbers say: light vs heavy: width 51.3 → 53.5 px, dark 0.29 → 0.28; pressure barely changes the width.

## Refs v3 · #15 Ultramarine script
Ink 0.98 · 39 px · 58.1 s

![Refs v3 · #15 Ultramarine script](Refs-v3-15-Ultramarine-script.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 4 % → 7 % | 10.5 px | 0.60 | 1.93 | 42 |
| heavy line | 14 % → 14 % | 40.3 px | 0.71 | 1.02 | 217 |
| pressure swell | 8 % → 8 % | 28.6 px | 0.71 | 1.10 | 113 |
| fast wave | 28 % → 28 % | 32.0 px | 0.72 | 1.03 | 467 |
| slow wave | 24 % → 25 % | 27.2 px | 0.69 | 1.08 | 537 |
| spiral | 40 % → 41 % | 26.1 px | 0.68 | 1.04 | 551 |
| loop | 21 % → 22 % | 27.1 px | 0.68 | 1.07 | 318 |
| tilted | 14 % → 14 % | 39.6 px | 0.71 | 1.00 | 197 |
| over the wet one | 24 % → 24 % | 27.2 px | 0.71 | 1.01 | 172 |
| long, no reload | 55 % → 57 % | 24.8 px | 0.66 | 1.03 | 1274 | quarters: 0.45 → 0.43 → 0.41 → 0.37

Numbers say: light vs heavy: width 10.5 → 40.3 px, dark 0.60 → 0.71; wet paint spreads well beyond the stroke.

## Refs v3 · #16 Shrigley strokes
Watercolour 1.00 + water 30 % · 64 px · 64.8 s

![Refs v3 · #16 Shrigley strokes](Refs-v3-16-Shrigley-strokes.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 8 % → 15 % | 24.6 px | 0.23 | 1.79 | 87 |
| heavy line | 17 % → 17 % | 49.0 px | 0.21 | 0.98 | 276 |
| pressure swell | 10 % → 11 % | 38.6 px | 0.24 | 1.02 | 179 |
| fast wave | 36 % → 35 % | 42.2 px | 0.20 | 0.97 | 611 |
| slow wave | 34 % → 33 % | 38.8 px | 0.17 | 1.00 | 753 |
| spiral | 58 % → 56 % | 38.1 px | 0.10 | 0.97 | 876 |
| loop | 29 % → 29 % | 37.7 px | 0.16 | 0.99 | 468 |
| tilted | 19 % → 19 % | 52.4 px | 0.19 | 1.00 | 352 |
| over the wet one | 31 % → 30 % | 34.9 px | 0.19 | 0.97 | 245 |
| long, no reload | 72 % → 67 % | 32.2 px | 0.11 | 0.93 | 1584 | quarters: 0.15 → 0.08 → 0.05 → 0.04

Numbers say: light vs heavy: width 24.6 → 49.0 px, dark 0.23 → 0.21; wet paint spreads well beyond the stroke.

## Refs v3 · #17 Krovostok dry brush
Ink 0.93 · Gouache 0.07 · 16 px · 81.6 s

![Refs v3 · #17 Krovostok dry brush](Refs-v3-17-Krovostok-dry-brush.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 6 % → 8 % | 16.5 px | 0.24 | 1.42 | 81 |
| heavy line | 6 % → 8 % | 17.1 px | 0.24 | 1.35 | 132 |
| pressure swell | 4 % → 7 % | 16.8 px | 0.23 | 1.52 | 91 |
| fast wave | 15 % → 19 % | 16.8 px | 0.29 | 1.29 | 373 |
| slow wave | 13 % → 16 % | 15.2 px | 0.22 | 1.24 | 323 |
| spiral | 23 % → 27 % | 15.2 px | 0.19 | 1.16 | 811 |
| loop | 12 % → 15 % | 15.7 px | 0.26 | 1.24 | 236 |
| tilted | 7 % → 8 % | 20.5 px | 0.27 | 1.03 | 200 |
| over the wet one | 13 % → 16 % | 16.8 px | 0.27 | 1.23 | 237 |
| long, no reload | 27 % → 31 % | 12.1 px | 0.19 | 1.13 | 665 | quarters: 0.11 → 0.07 → 0.04 → 0.03

Numbers say: light vs heavy: width 16.5 → 17.1 px, dark 0.24 → 0.24; pressure barely changes the width; wet paint spreads well beyond the stroke.

## Refs v3 · #18 Twombly blue sticks
Wax 1.00 · 19 px · 15.6 s

![Refs v3 · #18 Twombly blue sticks](Refs-v3-18-Twombly-blue-sticks.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 4 % → 4 % | 11.8 px | 0.20 | 1.00 | 51 |
| heavy line | 6 % → 6 % | 16.5 px | 0.21 | 1.00 | 95 |
| pressure swell | 4 % → 4 % | 15.4 px | 0.20 | 1.00 | 48 |
| fast wave | 14 % → 14 % | 16.1 px | 0.20 | 1.00 | 107 |
| slow wave | 13 % → 13 % | 15.3 px | 0.21 | 1.00 | 155 |
| spiral | 21 % → 21 % | 14.2 px | 0.20 | 1.00 | 153 |
| loop | 11 % → 11 % | 13.6 px | 0.21 | 1.00 | 95 |
| tilted | 4 % → 4 % | 12.4 px | 0.20 | 1.00 | 78 |
| over the wet one | 10 % → 10 % | 15.0 px | 0.20 | 1.00 | 130 |
| long, no reload | 27 % → 27 % | 12.2 px | 0.20 | 1.00 | 503 | quarters: 0.06 → 0.06 → 0.06 → 0.06

Numbers say: light vs heavy: width 11.8 → 16.5 px, dark 0.20 → 0.21; the long stroke does not run out of paint.

## Refs v3 · #19 Guston charcoal hand
Charcoal 1.00 · 39 px · 16.8 s

![Refs v3 · #19 Guston charcoal hand](Refs-v3-19-Guston-charcoal-hand.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 6 % → 6 % | 18.2 px | 0.62 | 1.00 | 226 |
| heavy line | 11 % → 11 % | 32.3 px | 0.62 | 1.00 | 213 |
| pressure swell | 8 % → 8 % | 29.9 px | 0.62 | 1.00 | 118 |
| fast wave | 26 % → 26 % | 29.8 px | 0.62 | 1.00 | 386 |
| slow wave | 25 % → 25 % | 28.3 px | 0.62 | 1.00 | 664 |
| spiral | 39 % → 39 % | 25.8 px | 0.62 | 1.00 | 496 |
| loop | 20 % → 20 % | 25.3 px | 0.62 | 1.00 | 240 |
| tilted | 7 % → 7 % | 20.3 px | 0.61 | 1.00 | 227 |
| over the wet one | 17 % → 17 % | 27.3 px | 0.61 | 1.00 | 163 |
| long, no reload | 48 % → 48 % | 21.3 px | 0.62 | 1.00 | 897 | quarters: 0.33 → 0.32 → 0.32 → 0.32

Numbers say: light vs heavy: width 18.2 → 32.3 px, dark 0.62 → 0.62; the long stroke does not run out of paint.

## Refs v3 · #20 Orange crayon
Wax 1.00 · 48 px · 16.1 s

![Refs v3 · #20 Orange crayon](Refs-v3-20-Orange-crayon.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 9 % → 9 % | 25.1 px | 0.52 | 1.00 | 138 |
| heavy line | 14 % → 14 % | 41.0 px | 0.52 | 1.00 | 216 |
| pressure swell | 10 % → 10 % | 37.4 px | 0.52 | 1.00 | 114 |
| fast wave | 31 % → 31 % | 36.3 px | 0.52 | 1.00 | 596 |
| slow wave | 30 % → 30 % | 34.4 px | 0.52 | 1.00 | 798 |
| spiral | 48 % → 48 % | 31.8 px | 0.52 | 1.00 | 688 |
| loop | 24 % → 24 % | 30.8 px | 0.52 | 1.00 | 361 |
| tilted | 7 % → 7 % | 20.5 px | 0.52 | 1.00 | 252 |
| over the wet one | 19 % → 19 % | 33.1 px | 0.52 | 1.00 | 174 |
| long, no reload | 55 % → 55 % | 24.8 px | 0.52 | 1.00 | 1129 | quarters: 0.32 → 0.31 → 0.32 → 0.32

Numbers say: light vs heavy: width 25.1 → 41.0 px, dark 0.52 → 0.52; the long stroke does not run out of paint.

## Refs v3 · #21 Gritty dog contours
Gouache 1.00 + water 15 % · 53 px · 109.8 s

![Refs v3 · #21 Gritty dog contours](Refs-v3-21-Gritty-dog-contours.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 17 % → 16 % | 48.1 px | 0.38 | 0.98 | 176 |
| heavy line | 17 % → 17 % | 49.9 px | 0.38 | 0.98 | 236 |
| pressure swell | 13 % → 13 % | 50.1 px | 0.38 | 0.99 | 201 |
| fast wave | 38 % → 28 % | 44.1 px | 0.36 | 0.75 | 718 |
| slow wave | 39 % → 31 % | 45.2 px | 0.37 | 0.80 | 1160 |
| spiral | 55 % → 35 % | 36.2 px | 0.36 | 0.63 | 1205 |
| loop | 33 % → 30 % | 43.3 px | 0.37 | 0.91 | 561 |
| tilted | 15 % → 15 % | 40.5 px | 0.39 | 1.00 | 307 |
| over the wet one | 30 % → 29 % | 44.3 px | 0.39 | 0.96 | 366 |
| long, no reload | 65 % → 39 % | 29.2 px | 0.35 | 0.60 | 1843 | quarters: 0.30 → 0.27 → 0.23 → 0.19

Numbers say: light vs heavy: width 48.1 → 49.9 px, dark 0.38 → 0.38; pressure barely changes the width.

## Refs v3 · #22 Wasilewski brush poster
Ink 0.98 · 64 px · 115.8 s

![Refs v3 · #22 Wasilewski brush poster](Refs-v3-22-Wasilewski-brush-poster.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 19 % → 20 % | 55.6 px | 0.88 | 1.05 | 107 |
| heavy line | 22 % → 22 % | 65.0 px | 0.89 | 1.00 | 357 |
| pressure swell | 16 % → 16 % | 58.8 px | 0.89 | 1.03 | 315 |
| fast wave | 52 % → 53 % | 60.0 px | 0.84 | 1.01 | 868 |
| slow wave | 49 % → 49 % | 56.2 px | 0.88 | 1.01 | 1190 |
| spiral | 69 % → 69 % | 45.3 px | 0.86 | 1.00 | 1308 |
| loop | 44 % → 44 % | 56.5 px | 0.87 | 1.00 | 713 |
| tilted | 18 % → 18 % | 50.8 px | 0.88 | 1.00 | 394 |
| over the wet one | 37 % → 37 % | 52.2 px | 0.88 | 1.00 | 409 |
| long, no reload | 84 % → 86 % | 37.8 px | 0.87 | 1.02 | 2123 | quarters: 0.84 → 0.83 → 0.80 → 0.72

Numbers say: light vs heavy: width 55.6 → 65.0 px, dark 0.88 → 0.89; the long stroke does not run out of paint.

## Refs v3 · #23 Report dry white mask
Ink 0.93 · Gouache 0.07 · 89 px · 168.7 s

![Refs v3 · #23 Report dry white mask](Refs-v3-23-Report-dry-white-mask.png)

A light paint: laid on a grey sheet (on white it cannot be seen); **dark** = how far it is from the grey either way.

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 26 % → 27 % | 76.2 px | 0.36 | 1.02 | 255 |
| heavy line | 27 % → 27 % | 78.6 px | 0.40 | 1.00 | 638 |
| pressure swell | 21 % → 23 % | 80.2 px | 0.35 | 1.05 | 354 |
| fast wave | 60 % → 62 % | 69.9 px | 0.33 | 1.03 | 1311 |
| slow wave | 61 % → 61 % | 70.3 px | 0.37 | 1.00 | 1977 |
| spiral | 76 % → 71 % | 50.2 px | 0.38 | 0.93 | 3108 |
| loop | 55 % → 55 % | 71.7 px | 0.40 | 1.00 | 3214 |
| tilted | 22 % → 22 % | 61.2 px | 0.35 | 1.00 | 2151 |
| over the wet one | 46 % → 46 % | 67.8 px | 0.35 | 1.00 | 824 |
| long, no reload | 91 % → 91 % | 40.9 px | 0.34 | 0.99 | 5456 | quarters: 0.00 → 0.00 → 0.00 → 0.00

Numbers say: light vs heavy: width 76.2 → 78.6 px, dark 0.36 → 0.40; pressure barely changes the width; the long stroke does not run out of paint.

## Refs v3 · #24 Picasso flat oil
Gouache 1.00 + turpentine 20 % · 51 px · 106.9 s

![Refs v3 · #24 Picasso flat oil](Refs-v3-24-Picasso-flat-oil.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 16 % → 15 % | 47.3 px | 0.18 | 0.94 | 242 |
| heavy line | 17 % → 17 % | 50.6 px | 0.17 | 0.95 | 299 |
| pressure swell | 13 % → 13 % | 49.1 px | 0.20 | 0.97 | 220 |
| fast wave | 41 % → 17 % | 47.6 px | 0.25 | 0.42 | 769 |
| slow wave | 42 % → 23 % | 48.8 px | 0.19 | 0.55 | 1431 |
| spiral | 61 % → 24 % | 40.4 px | 0.21 | 0.39 | 1684 |
| loop | 35 % → 21 % | 45.6 px | 0.17 | 0.59 | 1225 |
| tilted | 14 % → 14 % | 39.7 px | 0.22 | 1.00 | 1088 |
| over the wet one | 30 % → 27 % | 43.7 px | 0.22 | 0.90 | 4376 |
| long, no reload | 75 % → 22 % | 33.7 px | 0.20 | 0.30 | 3070 | quarters: 0.16 → 0.11 → 0.04 → 0.01

Numbers say: light vs heavy: width 47.3 → 50.6 px, dark 0.18 → 0.17; pressure barely changes the width.

## Refs v3 · #25 Yellow heavy stroke
Impasto 1.00 · 272 px · 179.5 s

![Refs v3 · #25 Yellow heavy stroke](Refs-v3-25-Yellow-heavy-stroke.png)

A light paint: laid on a grey sheet (on white it cannot be seen); **dark** = how far it is from the grey either way.

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 71 % → 70 % | 205.9 px | 0.22 | 0.99 | 1763 |
| heavy line | 71 % → 54 % | 205.9 px | 0.22 | 0.77 | 4000 |
| pressure swell | 63 % → 69 % | 236.2 px | 0.19 | 1.10 | 4532 |
| fast wave | 99 % → 69 % | 114.6 px | 0.17 | 0.69 | 22393 |
| slow wave | 99 % → 58 % | 114.9 px | 0.20 | 0.58 | 23316 |
| spiral | 99 % → 69 % | 65.6 px | 0.17 | 0.70 | 18305 |
| loop | 100 % → 66 % | 129.5 px | 0.20 | 0.66 | 8625 |
| tilted | 54 % → 54 % | 150.3 px | 0.17 | 1.00 | 5189 |
| over the wet one | 89 % → 84 % | 98.3 px | 0.17 | 0.94 | 3671 |
| long, no reload | 100 % → 71 % | 44.8 px | 0.18 | 0.71 | 24992 | quarters: 0.00 → 0.00 → 0.00 → 0.00

Numbers say: light vs heavy: width 205.9 → 205.9 px, dark 0.22 → 0.22; pressure barely changes the width.

## Refs v3 · #26 Ink caricature
Ink 0.98 · 64 px · 105.6 s

![Refs v3 · #26 Ink caricature](Refs-v3-26-Ink-caricature.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 6 % → 9 % | 17.6 px | 0.78 | 1.44 | 138 |
| heavy line | 20 % → 20 % | 59.0 px | 0.84 | 1.01 | 397 |
| pressure swell | 11 % → 12 % | 42.0 px | 0.84 | 1.05 | 235 |
| fast wave | 41 % → 41 % | 47.1 px | 0.85 | 1.01 | 2576 |
| slow wave | 36 % → 37 % | 41.5 px | 0.83 | 1.04 | 1400 |
| spiral | 60 % → 60 % | 39.4 px | 0.80 | 1.01 | 4813 |
| loop | 31 % → 32 % | 40.1 px | 0.83 | 1.02 | 1204 |
| tilted | 19 % → 19 % | 54.2 px | 0.84 | 1.00 | 498 |
| over the wet one | 33 % → 34 % | 38.8 px | 0.84 | 1.01 | 388 |
| long, no reload | 79 % → 79 % | 35.4 px | 0.82 | 1.00 | 2668 | quarters: 0.70 → 0.71 → 0.70 → 0.68

Numbers say: light vs heavy: width 17.6 → 59.0 px, dark 0.78 → 0.84; the long stroke does not run out of paint.

## Refs v3 · #27 Orange impasto swatch
Impasto 1.00 · 80 px · 64.7 s

![Refs v3 · #27 Orange impasto swatch](Refs-v3-27-Orange-impasto-swatch.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 24 % → 21 % | 69.5 px | 0.30 | 0.89 | 559 |
| heavy line | 25 % → 18 % | 72.5 px | 0.31 | 0.72 | 1461 |
| pressure swell | 19 % → 17 % | 70.9 px | 0.33 | 0.89 | 846 |
| fast wave | 54 % → 19 % | 62.6 px | 0.37 | 0.35 | 2977 |
| slow wave | 55 % → 20 % | 63.1 px | 0.32 | 0.36 | 7611 |
| spiral | 63 % → 21 % | 41.4 px | 0.36 | 0.34 | 3994 |
| loop | 49 % → 23 % | 62.9 px | 0.31 | 0.47 | 1534 |
| tilted | 19 % → 19 % | 52.0 px | 0.35 | 1.00 | 1086 |
| over the wet one | 40 % → 33 % | 60.4 px | 0.35 | 0.81 | 730 |
| long, no reload | 79 % → 21 % | 35.2 px | 0.34 | 0.27 | 3928 | quarters: 0.31 → 0.21 → 0.10 → 0.03

Numbers say: light vs heavy: width 69.5 → 72.5 px, dark 0.30 → 0.31; pressure barely changes the width.

## Refs v3 · #28 Miles Davis lines
Ink 0.98 · 18 px · 60.4 s

![Refs v3 · #28 Miles Davis lines](Refs-v3-28-Miles-Davis-lines.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 2 % → 6 % | 4.8 px | 0.32 | 3.37 | 48 |
| heavy line | 8 % → 9 % | 24.6 px | 0.45 | 1.08 | 130 |
| pressure swell | 4 % → 6 % | 16.2 px | 0.43 | 1.34 | 108 |
| fast wave | 15 % → 17 % | 17.1 px | 0.49 | 1.17 | 335 |
| slow wave | 12 % → 16 % | 14.4 px | 0.41 | 1.29 | 318 |
| spiral | 20 % → 23 % | 13.4 px | 0.35 | 1.16 | 533 |
| loop | 12 % → 14 % | 15.5 px | 0.41 | 1.21 | 349 |
| tilted | 8 % → 8 % | 21.9 px | 0.46 | 1.02 | 218 |
| over the wet one | 14 % → 15 % | 16.6 px | 0.46 | 1.11 | 187 |
| long, no reload | 32 % → 35 % | 14.2 px | 0.38 | 1.10 | 839 | quarters: 0.19 → 0.16 → 0.13 → 0.10

Numbers say: light vs heavy: width 4.8 → 24.6 px, dark 0.32 → 0.45; wet paint spreads well beyond the stroke.

## Refs v3 · #29 Shrigley asterisk
Watercolour 1.00 + water 50 % · 64 px · 122.5 s

![Refs v3 · #29 Shrigley asterisk](Refs-v3-29-Shrigley-asterisk.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 18 % → 19 % | 52.0 px | 0.55 | 1.06 | 225 |
| heavy line | 36 % → 33 % | 103.9 px | 0.50 | 0.91 | 923 |
| pressure swell | 22 % → 22 % | 83.0 px | 0.46 | 1.00 | 641 |
| fast wave | 65 % → 63 % | 74.9 px | 0.46 | 0.97 | 2061 |
| slow wave | 62 % → 58 % | 71.4 px | 0.47 | 0.94 | 3317 |
| spiral | 75 % → 71 % | 49.3 px | 0.44 | 0.95 | 3308 |
| loop | 54 % → 52 % | 70.3 px | 0.46 | 0.96 | 1330 |
| tilted | 22 % → 22 % | 61.6 px | 0.49 | 1.00 | 1095 |
| over the wet one | 48 % → 46 % | 73.0 px | 0.49 | 0.95 | 949 |
| long, no reload | 94 % → 89 % | 42.1 px | 0.44 | 0.95 | 4830 | quarters: 0.48 → 0.45 → 0.39 → 0.32

Numbers say: light vs heavy: width 52.0 → 103.9 px, dark 0.55 → 0.50.

## Refs v3 · #30 Red gouache face
Gouache 1.00 + water 15 % · 76 px · 123.8 s

![Refs v3 · #30 Red gouache face](Refs-v3-30-Red-gouache-face.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 23 % → 23 % | 66.8 px | 0.49 | 0.98 | 504 |
| heavy line | 24 % → 23 % | 70.7 px | 0.49 | 0.94 | 494 |
| pressure swell | 18 % → 18 % | 69.0 px | 0.49 | 0.98 | 475 |
| fast wave | 53 % → 41 % | 61.3 px | 0.50 | 0.77 | 1851 |
| slow wave | 53 % → 42 % | 61.0 px | 0.48 | 0.80 | 2391 |
| spiral | 66 % → 44 % | 43.4 px | 0.45 | 0.66 | 3052 |
| loop | 46 % → 41 % | 59.8 px | 0.48 | 0.89 | 1471 |
| tilted | 18 % → 18 % | 51.0 px | 0.48 | 1.00 | 761 |
| over the wet one | 40 % → 38 % | 59.8 px | 0.48 | 0.96 | 1083 |
| long, no reload | 81 % → 55 % | 36.1 px | 0.48 | 0.68 | 4222 | quarters: 0.46 → 0.44 → 0.39 → 0.33

Numbers say: light vs heavy: width 66.8 → 70.7 px, dark 0.49 → 0.49; pressure barely changes the width.

## Refs v3 · #31 Warhol blotted line
Ink 0.98 · 25 px · 55.0 s

![Refs v3 · #31 Warhol blotted line](Refs-v3-31-Warhol-blotted-line.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 3 % → 6 % | 9.5 px | 0.53 | 1.91 | 99 |
| heavy line | 10 % → 10 % | 27.7 px | 0.64 | 1.05 | 133 |
| pressure swell | 5 % → 6 % | 19.8 px | 0.62 | 1.17 | 129 |
| fast wave | 19 % → 20 % | 22.0 px | 0.65 | 1.05 | 476 |
| slow wave | 17 % → 19 % | 19.6 px | 0.62 | 1.15 | 400 |
| spiral | 27 % → 29 % | 17.8 px | 0.57 | 1.08 | 503 |
| loop | 15 % → 16 % | 18.9 px | 0.63 | 1.12 | 197 |
| tilted | 10 % → 10 % | 26.9 px | 0.63 | 1.00 | 185 |
| over the wet one | 17 % → 17 % | 19.5 px | 0.63 | 1.05 | 126 |
| long, no reload | 40 % → 43 % | 18.0 px | 0.60 | 1.06 | 755 | quarters: 0.33 → 0.30 → 0.27 → 0.24

Numbers say: light vs heavy: width 9.5 → 27.7 px, dark 0.53 → 0.64; wet paint spreads well beyond the stroke.

## Refs v3 · #32 Thick orange swipes
Impasto 1.00 · 76 px · 37.9 s

![Refs v3 · #32 Thick orange swipes](Refs-v3-32-Thick-orange-swipes.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 23 % → 20 % | 67.3 px | 0.21 | 0.86 | 347 |
| heavy line | 24 % → 16 % | 69.2 px | 0.22 | 0.67 | 519 |
| pressure swell | 18 % → 16 % | 68.3 px | 0.24 | 0.88 | 407 |
| fast wave | 53 % → 18 % | 61.4 px | 0.28 | 0.34 | 1278 |
| slow wave | 52 % → 18 % | 60.3 px | 0.24 | 0.35 | 2713 |
| spiral | 64 % → 21 % | 42.1 px | 0.27 | 0.33 | 2436 |
| loop | 47 % → 22 % | 61.1 px | 0.23 | 0.46 | 1293 |
| tilted | 18 % → 18 % | 50.4 px | 0.27 | 1.00 | 756 |
| over the wet one | 39 % → 31 % | 59.1 px | 0.27 | 0.79 | 705 |
| long, no reload | 76 % → 21 % | 34.3 px | 0.25 | 0.27 | 2620 | quarters: 0.21 → 0.08 → 0.02 → 0.00

Numbers say: light vs heavy: width 67.3 → 69.2 px, dark 0.21 → 0.22; pressure barely changes the width.

## Refs v3 · #33 Red wet-in-wet flames
Watercolour 1.00 + water 60 % · 96 px · 181.3 s

![Refs v3 · #33 Red wet-in-wet flames](Refs-v3-33-Red-wet-in-wet-flames.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 30 % → 51 % | 87.0 px | 0.45 | 1.70 | 412 |
| heavy line | 49 % → 55 % | 141.2 px | 0.51 | 1.14 | 916 |
| pressure swell | 29 % → 36 % | 107.4 px | 0.40 | 1.25 | 795 |
| fast wave | 76 % → 81 % | 87.4 px | 0.43 | 1.08 | 2488 |
| slow wave | 78 % → 82 % | 89.6 px | 0.49 | 1.05 | 3413 |
| spiral | 87 % → 93 % | 57.6 px | 0.41 | 1.06 | 4074 |
| loop | 67 % → 74 % | 86.5 px | 0.43 | 1.11 | 2279 |
| tilted | 38 % → 39 % | 106.2 px | 0.42 | 1.01 | 1169 |
| over the wet one | 69 % → 78 % | 86.8 px | 0.42 | 1.13 | 1274 |
| long, no reload | 97 % → 99 % | 43.6 px | 0.43 | 1.02 | 6295 | quarters: 0.57 → 0.48 → 0.40 → 0.31

Numbers say: light vs heavy: width 87.0 → 141.2 px, dark 0.45 → 0.51; wet paint spreads well beyond the stroke.

## Refs v3 · #34 Magenta oil patches
Gouache 1.00 + turpentine 20 % · 90 px · 134.3 s

![Refs v3 · #34 Magenta oil patches](Refs-v3-34-Magenta-oil-patches.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 29 % → 26 % | 83.1 px | 0.29 | 0.92 | 475 |
| heavy line | 30 % → 28 % | 88.1 px | 0.29 | 0.91 | 683 |
| pressure swell | 23 % → 22 % | 85.3 px | 0.30 | 0.98 | 531 |
| fast wave | 63 % → 35 % | 73.3 px | 0.35 | 0.55 | 1793 |
| slow wave | 63 % → 36 % | 72.8 px | 0.31 | 0.58 | 3261 |
| spiral | 77 % → 37 % | 50.5 px | 0.34 | 0.48 | 3928 |
| loop | 56 % → 40 % | 72.5 px | 0.29 | 0.72 | 1755 |
| tilted | 22 % → 22 % | 61.6 px | 0.32 | 1.00 | 1052 |
| over the wet one | 48 % → 43 % | 71.0 px | 0.32 | 0.91 | 706 |
| long, no reload | 96 % → 40 % | 42.9 px | 0.31 | 0.42 | 5694 | quarters: 0.30 → 0.29 → 0.25 → 0.16

Numbers say: light vs heavy: width 83.1 → 88.1 px, dark 0.29 → 0.29; pressure barely changes the width.

## Refs v3 · #35 Red band with runs
Watercolour 1.00 + water 70 % · 176 px · 292.5 s

![Refs v3 · #35 Red band with runs](Refs-v3-35-Red-band-with-runs.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 51 % → 67 % | 148.3 px | 0.30 | 1.32 | 754 |
| heavy line | 81 % → 80 % | 236.4 px | 0.42 | 0.98 | 2369 |
| pressure swell | 53 % → 70 % | 197.1 px | 0.29 | 1.33 | 1905 |
| fast wave | 92 % → 95 % | 106.4 px | 0.36 | 1.03 | 6932 |
| slow wave | 93 % → 94 % | 107.0 px | 0.49 | 1.01 | 12212 |
| spiral | 98 % → 99 % | 65.0 px | 0.22 | 1.01 | 11663 |
| loop | 99 % → 99 % | 128.5 px | 0.36 | 1.00 | 4925 |
| tilted | 86 % → 85 % | 239.5 px | 0.40 | 1.00 | 4132 |
| over the wet one | 93 % → 95 % | 21.4 px | 0.40 | 1.01 | 5473 |
| long, no reload | 99 % → 100 % | 44.5 px | 0.42 | 1.01 | 21871 | quarters: 0.51 → 0.48 → 0.44 → 0.30

Numbers say: light vs heavy: width 148.3 → 236.4 px, dark 0.30 → 0.42.

## Refs v3 · #36 Magenta letters flat
Gouache 1.00 + water 15 % · 64 px · 103.9 s

![Refs v3 · #36 Magenta letters flat](Refs-v3-36-Magenta-letters-flat.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 18 % → 18 % | 52.3 px | 0.39 | 0.99 | 211 |
| heavy line | 21 % → 19 % | 61.3 px | 0.39 | 0.91 | 503 |
| pressure swell | 16 % → 15 % | 59.0 px | 0.39 | 0.98 | 283 |
| fast wave | 44 % → 34 % | 51.0 px | 0.39 | 0.78 | 1280 |
| slow wave | 47 % → 38 % | 54.3 px | 0.38 | 0.82 | 1780 |
| spiral | 57 % → 39 % | 37.8 px | 0.40 | 0.67 | 1715 |
| loop | 40 % → 35 % | 52.0 px | 0.39 | 0.86 | 816 |
| tilted | 16 % → 16 % | 45.9 px | 0.40 | 1.00 | 534 |
| over the wet one | 35 % → 34 % | 51.9 px | 0.40 | 0.96 | 649 |
| long, no reload | 71 % → 46 % | 32.0 px | 0.37 | 0.65 | 3141 | quarters: 0.34 → 0.31 → 0.27 → 0.21

Numbers say: light vs heavy: width 52.3 → 61.3 px, dark 0.39 → 0.39.

## Refs v3 · #37 Oil still life
Gouache 1.00 + turpentine 20 % · 28 px · 66.6 s

![Refs v3 · #37 Oil still life](Refs-v3-37-Oil-still-life.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 9 % → 9 % | 27.1 px | 0.27 | 0.99 | 123 |
| heavy line | 10 % → 10 % | 29.3 px | 0.28 | 0.99 | 152 |
| pressure swell | 8 % → 8 % | 28.6 px | 0.31 | 1.00 | 135 |
| fast wave | 25 % → 11 % | 29.1 px | 0.35 | 0.43 | 550 |
| slow wave | 25 % → 12 % | 29.2 px | 0.30 | 0.46 | 803 |
| spiral | 40 % → 12 % | 26.4 px | 0.32 | 0.31 | 916 |
| loop | 21 % → 11 % | 26.9 px | 0.29 | 0.53 | 505 |
| tilted | 10 % → 10 % | 27.2 px | 0.32 | 1.01 | 235 |
| over the wet one | 20 % → 18 % | 27.6 px | 0.32 | 0.90 | 179 |
| long, no reload | 48 % → 13 % | 21.5 px | 0.29 | 0.28 | 1345 | quarters: 0.17 → 0.10 → 0.03 → 0.02

Numbers say: light vs heavy: width 27.1 → 29.3 px, dark 0.27 → 0.28; pressure barely changes the width.

## Refs v3 · #38 Sanguine drawing
Charcoal 0.50 · Pastel 0.50 · 12 px · 15.6 s

![Refs v3 · #38 Sanguine drawing](Refs-v3-38-Sanguine-drawing.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 3 % → 3 % | 9.0 px | 0.41 | 1.00 | 30 |
| heavy line | 4 % → 4 % | 12.2 px | 0.41 | 1.00 | 68 |
| pressure swell | 3 % → 3 % | 9.5 px | 0.37 | 1.00 | 41 |
| fast wave | 10 % → 10 % | 11.4 px | 0.40 | 1.00 | 95 |
| slow wave | 10 % → 10 % | 11.4 px | 0.40 | 1.00 | 81 |
| spiral | 15 % → 15 % | 10.2 px | 0.40 | 1.00 | 166 |
| loop | 8 % → 8 % | 10.0 px | 0.40 | 1.00 | 92 |
| tilted | 4 % → 4 % | 10.8 px | 0.41 | 1.00 | 39 |
| over the wet one | 8 % → 8 % | 10.8 px | 0.41 | 1.00 | 42 |
| long, no reload | 18 % → 18 % | 8.1 px | 0.40 | 1.00 | 227 | quarters: 0.08 → 0.08 → 0.08 → 0.08

Numbers say: light vs heavy: width 9.0 → 12.2 px, dark 0.41 → 0.41; the long stroke does not run out of paint.

## Refs v3 · #39 Thick impasto weave
Impasto 1.00 · 96 px · 51.8 s

![Refs v3 · #39 Thick impasto weave](Refs-v3-39-Thick-impasto-weave.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 28 % → 25 % | 82.2 px | 0.47 | 0.90 | 587 |
| heavy line | 30 % → 21 % | 86.1 px | 0.47 | 0.71 | 835 |
| pressure swell | 23 % → 21 % | 84.9 px | 0.47 | 0.91 | 572 |
| fast wave | 62 % → 24 % | 71.4 px | 0.50 | 0.39 | 1710 |
| slow wave | 62 % → 23 % | 71.8 px | 0.48 | 0.37 | 3383 |
| spiral | 67 % → 24 % | 44.2 px | 0.50 | 0.36 | 3301 |
| loop | 56 % → 27 % | 72.4 px | 0.46 | 0.49 | 1805 |
| tilted | 21 % → 21 % | 60.0 px | 0.48 | 1.00 | 1064 |
| over the wet one | 46 % → 38 % | 69.7 px | 0.48 | 0.82 | 731 |
| long, no reload | 85 % → 28 % | 38.2 px | 0.48 | 0.33 | 3865 | quarters: 0.46 → 0.41 → 0.35 → 0.31

Numbers say: light vs heavy: width 82.2 → 86.1 px, dark 0.47 → 0.47; pressure barely changes the width.

## Refs v3 · #40 Watercolour blooms
Watercolour 1.00 + water 55 % · 112 px · 218.2 s

![Refs v3 · #40 Watercolour blooms](Refs-v3-40-Watercolour-blooms.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 26 % → 44 % | 76.2 px | 0.02 | 1.67 | 384 |
| heavy line | 47 % → 51 % | 137.1 px | 0.02 | 1.07 | 1119 |
| pressure swell | 30 % → 35 % | 113.3 px | 0.03 | 1.16 | 676 |
| fast wave | 78 % → 85 % | 90.7 px | 0.04 | 1.08 | 2530 |
| slow wave | 78 % → 81 % | 90.2 px | 0.03 | 1.04 | 5894 |
| spiral | 86 % → 88 % | 56.8 px | 0.02 | 1.02 | 7372 |
| loop | 66 % → 69 % | 85.9 px | 0.03 | 1.04 | 2526 |
| tilted | 35 % → 35 % | 96.9 px | 0.04 | 1.01 | 1049 |
| over the wet one | 68 % → 76 % | 92.9 px | 0.04 | 1.12 | 1515 |
| long, no reload | 98 % → 100 % | 44.0 px | 0.02 | 1.01 | 7810 | quarters: 0.04 → 0.03 → 0.02 → 0.01

Numbers say: light vs heavy: width 76.2 → 137.1 px, dark 0.02 → 0.02; wet paint spreads well beyond the stroke.

## Refs v3 · #41 Coloured pencil
Charcoal 0.50 · Pastel 0.50 · 12 px · 16.2 s

![Refs v3 · #41 Coloured pencil](Refs-v3-41-Coloured-pencil.png)

A light paint: laid on a grey sheet (on white it cannot be seen); **dark** = how far it is from the grey either way.

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 3 % → 3 % | 9.0 px | 0.39 | 1.00 | 52 |
| heavy line | 4 % → 4 % | 12.2 px | 0.39 | 1.00 | 38 |
| pressure swell | 3 % → 3 % | 9.5 px | 0.34 | 1.00 | 28 |
| fast wave | 10 % → 10 % | 11.4 px | 0.38 | 1.00 | 84 |
| slow wave | 10 % → 10 % | 11.4 px | 0.38 | 1.00 | 74 |
| spiral | 15 % → 15 % | 10.2 px | 0.38 | 1.00 | 170 |
| loop | 8 % → 8 % | 10.0 px | 0.39 | 1.00 | 76 |
| tilted | 4 % → 4 % | 10.8 px | 0.39 | 1.00 | 49 |
| over the wet one | 8 % → 8 % | 10.8 px | 0.39 | 1.00 | 46 |
| long, no reload | 18 % → 18 % | 8.1 px | 0.37 | 1.00 | 260 | quarters: 0.00 → 0.00 → 0.00 → 0.00

Numbers say: light vs heavy: width 9.0 → 12.2 px, dark 0.39 → 0.39; the long stroke does not run out of paint.

## Refs v3 · #42 Pink shaggy pastel
Pastel 1.00 · 38 px · 21.5 s

![Refs v3 · #42 Pink shaggy pastel](Refs-v3-42-Pink-shaggy-pastel.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 7 % → 7 % | 20.5 px | 0.19 | 1.00 | 104 |
| heavy line | 11 % → 11 % | 33.0 px | 0.19 | 1.00 | 156 |
| pressure swell | 8 % → 8 % | 29.8 px | 0.19 | 1.00 | 109 |
| fast wave | 26 % → 26 % | 29.6 px | 0.19 | 1.00 | 350 |
| slow wave | 24 % → 24 % | 27.8 px | 0.19 | 1.00 | 664 |
| spiral | 39 % → 39 % | 25.6 px | 0.19 | 1.00 | 554 |
| loop | 20 % → 20 % | 25.3 px | 0.19 | 1.00 | 269 |
| tilted | 6 % → 6 % | 17.4 px | 0.19 | 1.00 | 201 |
| over the wet one | 16 % → 16 % | 26.8 px | 0.19 | 1.00 | 205 |
| long, no reload | 47 % → 47 % | 20.9 px | 0.19 | 1.00 | 832 | quarters: 0.10 → 0.10 → 0.10 → 0.10

Numbers say: light vs heavy: width 20.5 → 33.0 px, dark 0.19 → 0.19; the long stroke does not run out of paint.

## Refs v3 · #43 Dragged black blocks
Ink 0.93 · Gouache 0.07 · 112 px · 237.4 s

![Refs v3 · #43 Dragged black blocks](Refs-v3-43-Dragged-black-blocks.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 33 % → 35 % | 96.1 px | 0.87 | 1.06 | 463 |
| heavy line | 37 % → 37 % | 106.2 px | 0.87 | 1.00 | 1747 |
| pressure swell | 27 % → 29 % | 101.3 px | 0.87 | 1.08 | 870 |
| fast wave | 73 % → 76 % | 84.8 px | 0.86 | 1.03 | 2604 |
| slow wave | 71 % → 70 % | 82.3 px | 0.87 | 0.99 | 4241 |
| spiral | 83 % → 82 % | 55.1 px | 0.85 | 0.98 | 5375 |
| loop | 64 % → 64 % | 82.9 px | 0.87 | 1.00 | 2098 |
| tilted | 27 % → 28 % | 76.7 px | 0.86 | 1.00 | 1327 |
| over the wet one | 56 % → 57 % | 80.0 px | 0.86 | 1.01 | 1302 |
| long, no reload | 96 % → 96 % | 42.9 px | 0.86 | 1.00 | 10565 | quarters: 0.86 → 0.86 → 0.85 → 0.79

Numbers say: light vs heavy: width 96.1 → 106.2 px, dark 0.87 → 0.87; pressure barely changes the width; the long stroke does not run out of paint.

## Refs v3 · #44 Blue looping ribbon
Oil 0.52 · Gouache 0.48 + turpentine 10 % · 51 px · 141.5 s

![Refs v3 · #44 Blue looping ribbon](Refs-v3-44-Blue-looping-ribbon.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 16 % → 16 % | 46.1 px | 0.43 | 0.98 | 304 |
| heavy line | 17 % → 16 % | 49.1 px | 0.42 | 0.96 | 295 |
| pressure swell | 13 % → 12 % | 48.4 px | 0.44 | 0.97 | 262 |
| fast wave | 42 % → 22 % | 48.2 px | 0.48 | 0.53 | 878 |
| slow wave | 41 % → 28 % | 47.0 px | 0.44 | 0.68 | 1999 |
| spiral | 61 % → 27 % | 40.3 px | 0.44 | 0.44 | 1400 |
| loop | 34 % → 23 % | 44.0 px | 0.43 | 0.69 | 603 |
| tilted | 15 % → 15 % | 41.1 px | 0.46 | 1.00 | 380 |
| over the wet one | 30 % → 27 % | 42.6 px | 0.46 | 0.89 | 357 |
| long, no reload | 75 % → 25 % | 33.7 px | 0.46 | 0.33 | 2303 | quarters: 0.38 → 0.34 → 0.22 → 0.12

Numbers say: light vs heavy: width 46.1 → 49.1 px, dark 0.43 → 0.42; pressure barely changes the width.

## Refs v3 · #45 Pastel pepper
Pastel 1.00 · 64 px · 26.0 s

![Refs v3 · #45 Pastel pepper](Refs-v3-45-Pastel-pepper.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 11 % → 11 % | 33.1 px | 0.57 | 1.00 | 329 |
| heavy line | 19 % → 19 % | 55.0 px | 0.57 | 1.00 | 295 |
| pressure swell | 13 % → 13 % | 49.5 px | 0.57 | 1.00 | 212 |
| fast wave | 40 % → 40 % | 46.4 px | 0.57 | 1.00 | 954 |
| slow wave | 38 % → 38 % | 44.2 px | 0.57 | 1.00 | 1597 |
| spiral | 61 % → 61 % | 40.0 px | 0.57 | 1.00 | 1472 |
| loop | 31 % → 31 % | 40.0 px | 0.57 | 1.00 | 958 |
| tilted | 9 % → 9 % | 24.0 px | 0.57 | 1.00 | 549 |
| over the wet one | 24 % → 24 % | 43.7 px | 0.57 | 1.00 | 369 |
| long, no reload | 69 % → 69 % | 31.0 px | 0.57 | 1.00 | 2156 | quarters: 0.43 → 0.42 → 0.42 → 0.42

Numbers say: light vs heavy: width 33.1 → 55.0 px, dark 0.57 → 0.57; the long stroke does not run out of paint.

## Refs v3 · #46 Ink lips on wet paper
Watercolour 1.00 + water 65 % · 56 px · 170.1 s

![Refs v3 · #46 Ink lips on wet paper](Refs-v3-46-Ink-lips-on-wet-paper.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 12 % → 28 % | 34.7 px | 0.59 | 2.31 | 110 |
| heavy line | 24 % → 29 % | 69.9 px | 0.64 | 1.22 | 333 |
| pressure swell | 14 % → 17 % | 53.8 px | 0.62 | 1.16 | 229 |
| fast wave | 48 % → 53 % | 55.3 px | 0.55 | 1.12 | 931 |
| slow wave | 45 % → 52 % | 52.4 px | 0.58 | 1.14 | 2158 |
| spiral | 67 % → 70 % | 44.4 px | 0.50 | 1.04 | 2884 |
| loop | 41 % → 45 % | 52.7 px | 0.61 | 1.10 | 681 |
| tilted | 19 % → 20 % | 54.3 px | 0.55 | 1.02 | 483 |
| over the wet one | 39 % → 43 % | 53.2 px | 0.55 | 1.11 | 578 |
| long, no reload | 84 % → 92 % | 37.5 px | 0.59 | 1.10 | 2567 | quarters: 0.61 → 0.62 → 0.59 → 0.47

Numbers say: light vs heavy: width 34.7 → 69.9 px, dark 0.59 → 0.64; wet paint spreads well beyond the stroke.

## Refs v3 · #47 Pink knife slabs
Impasto 1.00 · 112 px · 59.6 s

![Refs v3 · #47 Pink knife slabs](Refs-v3-47-Pink-knife-slabs.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 38 % → 35 % | 111.8 px | 0.18 | 0.92 | 261 |
| heavy line | 38 % → 31 % | 110.8 px | 0.18 | 0.81 | 219 |
| pressure swell | 28 % → 28 % | 105.7 px | 0.18 | 1.00 | 83 |
| fast wave | 71 % → 61 % | 82.3 px | 0.17 | 0.86 | 312 |
| slow wave | 72 % → 49 % | 83.6 px | 0.18 | 0.67 | 914 |
| spiral | 70 % → 42 % | 46.4 px | 0.18 | 0.60 | 657 |
| loop | 64 % → 44 % | 82.5 px | 0.18 | 0.68 | 286 |
| tilted | 24 % → 24 % | 68.0 px | 0.18 | 1.00 | 88 |
| over the wet one | 56 % → 54 % | 89.6 px | 0.18 | 0.95 | 166 |
| long, no reload | 92 % → 82 % | 41.1 px | 0.17 | 0.89 | 723 | quarters: 0.17 → 0.16 → 0.14 → 0.12

Numbers say: light vs heavy: width 111.8 → 110.8 px, dark 0.18 → 0.18; pressure barely changes the width.

## Refs v3 · #48 Black bands with drips
Watercolour 1.00 + water 35 % · 112 px · 189.0 s

![Refs v3 · #48 Black bands with drips](Refs-v3-48-Black-bands-with-drips.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 32 % → 35 % | 93.3 px | 0.77 | 1.09 | 441 |
| heavy line | 34 % → 35 % | 97.8 px | 0.78 | 1.03 | 659 |
| pressure swell | 25 % → 28 % | 93.8 px | 0.77 | 1.13 | 598 |
| fast wave | 69 % → 72 % | 80.1 px | 0.59 | 1.04 | 2716 |
| slow wave | 69 % → 68 % | 79.6 px | 0.61 | 0.99 | 3774 |
| spiral | 77 % → 76 % | 51.1 px | 0.55 | 0.99 | 6887 |
| loop | 62 % → 62 % | 80.7 px | 0.64 | 1.00 | 3510 |
| tilted | 27 % → 27 % | 74.1 px | 0.66 | 1.00 | 1425 |
| over the wet one | 53 % → 52 % | 74.3 px | 0.66 | 0.98 | 855 |
| long, no reload | 86 % → 89 % | 38.8 px | 0.51 | 1.03 | 5506 | quarters: 0.72 → 0.53 → 0.35 → 0.29

Numbers say: light vs heavy: width 93.3 → 97.8 px, dark 0.77 → 0.78; pressure barely changes the width.

## Refs v3 · #49 Magenta letters round
Ink 0.98 · 64 px · 142.8 s

![Refs v3 · #49 Magenta letters round](Refs-v3-49-Magenta-letters-round.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 7 % → 10 % | 21.3 px | 0.46 | 1.31 | 105 |
| heavy line | 20 % → 20 % | 57.2 px | 0.50 | 1.01 | 560 |
| pressure swell | 11 % → 12 % | 42.1 px | 0.52 | 1.05 | 334 |
| fast wave | 41 % → 41 % | 46.8 px | 0.54 | 1.01 | 1034 |
| slow wave | 36 % → 38 % | 41.9 px | 0.49 | 1.04 | 1109 |
| spiral | 60 % → 60 % | 39.7 px | 0.46 | 1.01 | 2834 |
| loop | 31 % → 32 % | 40.1 px | 0.49 | 1.02 | 1040 |
| tilted | 19 % → 19 % | 54.1 px | 0.52 | 1.00 | 537 |
| over the wet one | 33 % → 34 % | 38.7 px | 0.52 | 1.01 | 1020 |
| long, no reload | 79 % → 79 % | 35.3 px | 0.47 | 1.01 | 3073 | quarters: 0.41 → 0.41 → 0.40 → 0.38

Numbers say: light vs heavy: width 21.3 → 57.2 px, dark 0.46 → 0.50; the long stroke does not run out of paint.

## Refs v3 · #50 Swipes on seaside
Gouache 1.00 + water 15 % · 80 px · 166.8 s

![Refs v3 · #50 Swipes on seaside](Refs-v3-50-Swipes-on-seaside.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 24 % → 24 % | 69.8 px | 0.29 | 0.98 | 805 |
| heavy line | 25 % → 24 % | 73.4 px | 0.29 | 0.95 | 819 |
| pressure swell | 19 % → 19 % | 72.7 px | 0.31 | 0.99 | 656 |
| fast wave | 54 % → 44 % | 61.8 px | 0.30 | 0.82 | 2608 |
| slow wave | 55 % → 44 % | 63.2 px | 0.28 | 0.80 | 2883 |
| spiral | 64 % → 42 % | 42.4 px | 0.26 | 0.65 | 2308 |
| loop | 49 % → 44 % | 63.5 px | 0.27 | 0.89 | 1248 |
| tilted | 20 % → 20 % | 56.1 px | 0.32 | 1.00 | 862 |
| over the wet one | 42 % → 40 % | 61.6 px | 0.32 | 0.96 | 800 |
| long, no reload | 81 % → 55 % | 36.4 px | 0.26 | 0.67 | 10932 | quarters: 0.25 → 0.24 → 0.20 → 0.15

Numbers say: light vs heavy: width 69.8 → 73.4 px, dark 0.29 → 0.29; pressure barely changes the width.

## Watercolour · #16 Shrigley strokes
Watercolour 1.00 + water 30 % · 46 px · 112.9 s

![Watercolour · #16 Shrigley strokes](Watercolour-16-Shrigley-strokes.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 6 % → 11 % | 18.7 px | 0.33 | 1.77 | 87 |
| heavy line | 13 % → 13 % | 37.9 px | 0.24 | 0.98 | 168 |
| pressure swell | 8 % → 8 % | 29.8 px | 0.27 | 1.00 | 115 |
| fast wave | 29 % → 28 % | 33.1 px | 0.27 | 0.98 | 535 |
| slow wave | 26 % → 26 % | 30.3 px | 0.23 | 0.98 | 692 |
| spiral | 44 % → 43 % | 29.2 px | 0.15 | 0.97 | 921 |
| loop | 23 % → 22 % | 29.3 px | 0.26 | 0.99 | 534 |
| tilted | 15 % → 15 % | 42.2 px | 0.22 | 1.00 | 262 |
| over the wet one | 25 % → 24 % | 27.7 px | 0.22 | 0.96 | 405 |
| long, no reload | 59 % → 56 % | 26.6 px | 0.15 | 0.95 | 2093 | quarters: 0.14 → 0.10 → 0.07 → 0.05

Numbers say: light vs heavy: width 18.7 → 37.9 px, dark 0.33 → 0.24; wet paint spreads well beyond the stroke.

## Watercolour · #29 Shrigley asterisk
Watercolour 1.00 + water 50 % · 70 px · 164.7 s

![Watercolour · #29 Shrigley asterisk](Watercolour-29-Shrigley-asterisk.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 20 % → 21 % | 57.8 px | 0.58 | 1.05 | 575 |
| heavy line | 39 % → 36 % | 113.3 px | 0.54 | 0.91 | 5713 |
| pressure swell | 24 % → 24 % | 89.0 px | 0.57 | 1.02 | 2432 |
| fast wave | 69 % → 67 % | 79.2 px | 0.48 | 0.98 | 9324 |
| slow wave | 65 % → 61 % | 75.4 px | 0.50 | 0.94 | 5435 |
| spiral | 78 % → 74 % | 51.4 px | 0.45 | 0.96 | 5618 |
| loop | 58 % → 56 % | 74.7 px | 0.48 | 0.96 | 2683 |
| tilted | 24 % → 24 % | 68.2 px | 0.57 | 1.00 | 658 |
| over the wet one | 53 % → 53 % | 78.8 px | 0.57 | 1.01 | 821 |
| long, no reload | 95 % → 95 % | 42.6 px | 0.53 | 1.00 | 5942 | quarters: 0.55 → 0.54 → 0.52 → 0.46

Numbers say: light vs heavy: width 57.8 → 113.3 px, dark 0.58 → 0.54.

## Watercolour · #35 Red band with runs
Watercolour 1.00 + water 75 % · 80 px · 188.4 s

![Watercolour · #35 Red band with runs](Watercolour-35-Red-band-with-runs.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 37 % → 50 % | 107.2 px | 0.14 | 1.35 | 229 |
| heavy line | 50 % → 55 % | 144.1 px | 0.29 | 1.12 | 1148 |
| pressure swell | 20 % → 23 % | 75.9 px | 0.17 | 1.13 | 1729 |
| fast wave | 69 % → 68 % | 79.8 px | 0.24 | 0.99 | 2696 |
| slow wave | 70 % → 70 % | 80.7 px | 0.40 | 1.00 | 3435 |
| spiral | 88 % → 93 % | 57.8 px | 0.13 | 1.06 | 2852 |
| loop | 70 % → 79 % | 90.5 px | 0.26 | 1.13 | 1187 |
| tilted | 45 % → 44 % | 124.4 px | 0.29 | 1.00 | 697 |
| over the wet one | 71 % → 75 % | 72.8 px | 0.29 | 1.06 | 577 |
| long, no reload | 95 % → 98 % | 42.5 px | 0.19 | 1.03 | 4228 | quarters: 0.27 → 0.18 → 0.18 → 0.13

Numbers say: light vs heavy: width 107.2 → 144.1 px, dark 0.14 → 0.29.

## Watercolour · #40 Olive and sepia blooms
Watercolour 1.00 + water 55 % · 90 px · 163.3 s

![Watercolour · #40 Olive and sepia blooms](Watercolour-40-Olive-and-sepia-blooms.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 20 % → 36 % | 59.4 px | 0.13 | 1.76 | 183 |
| heavy line | 37 % → 41 % | 107.9 px | 0.13 | 1.09 | 580 |
| pressure swell | 23 % → 26 % | 87.3 px | 0.14 | 1.14 | 417 |
| fast wave | 67 % → 74 % | 78.0 px | 0.15 | 1.10 | 1462 |
| slow wave | 66 % → 70 % | 76.2 px | 0.14 | 1.06 | 2341 |
| spiral | 80 % → 82 % | 52.5 px | 0.11 | 1.03 | 2503 |
| loop | 58 % → 61 % | 74.7 px | 0.15 | 1.06 | 1032 |
| tilted | 29 % → 30 % | 80.9 px | 0.14 | 1.02 | 728 |
| over the wet one | 56 % → 63 % | 76.5 px | 0.14 | 1.12 | 619 |
| long, no reload | 97 % → 99 % | 43.4 px | 0.12 | 1.02 | 4495 | quarters: 0.20 → 0.14 → 0.11 → 0.07

Numbers say: light vs heavy: width 59.4 → 107.9 px, dark 0.13 → 0.13; wet paint spreads well beyond the stroke.

## Watercolour · #46 Lips on wet paper
Watercolour 1.00 + water 65 % · 50 px · 128.1 s

![Watercolour · #46 Lips on wet paper](Watercolour-46-Lips-on-wet-paper.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 11 % → 27 % | 32.3 px | 0.58 | 2.38 | 85 |
| heavy line | 22 % → 27 % | 64.9 px | 0.64 | 1.21 | 230 |
| pressure swell | 13 % → 16 % | 50.0 px | 0.61 | 1.16 | 175 |
| fast wave | 44 % → 49 % | 50.7 px | 0.53 | 1.13 | 708 |
| slow wave | 42 % → 49 % | 48.0 px | 0.57 | 1.18 | 975 |
| spiral | 64 % → 68 % | 42.5 px | 0.49 | 1.05 | 1032 |
| loop | 37 % → 43 % | 47.8 px | 0.59 | 1.16 | 396 |
| tilted | 18 % → 19 % | 50.5 px | 0.52 | 1.03 | 343 |
| over the wet one | 36 % → 40 % | 49.6 px | 0.52 | 1.11 | 271 |
| long, no reload | 80 % → 90 % | 36.1 px | 0.57 | 1.12 | 1810 | quarters: 0.58 → 0.60 → 0.56 → 0.44

Numbers say: light vs heavy: width 32.3 → 64.9 px, dark 0.58 → 0.64; wet paint spreads well beyond the stroke.

## Oil focus · A best filbert — own sheet
own sheet 2000 × 1320 · Gouache 1.00 + turpentine 15 % · 260 px · 190.8 s

![Oil focus · A best filbert — own sheet](Oil-focus-A-best-filbert-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 15 % → 51 % | 190.7 px | 0.52 | 3.33 | 6900 |
| stroke 2 | 29 % → 32 % | 353.1 px | 0.45 | 1.13 | 8389 |
| stroke 3 | 36 % → 33 % | 334.4 px | 0.49 | 0.93 | 20787 |
| stroke 4 | 42 % → 32 % | 580.3 px | 0.53 | 0.76 | 21257 |
| stroke 5 | 50 % → 36 % | 807.8 px | 0.54 | 0.72 | 28122 |

Numbers say: wet paint spreads well beyond the stroke.

## Oil focus · B flat — own sheet
own sheet 2000 × 1320 · Gouache 1.00 + turpentine 15 % · 260 px · 178.6 s

![Oil focus · B flat — own sheet](Oil-focus-B-flat-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 15 % → 50 % | 188.0 px | 0.52 | 3.27 | 6480 |
| stroke 2 | 28 % → 32 % | 343.7 px | 0.45 | 1.14 | 7955 |
| stroke 3 | 35 % → 32 % | 324.4 px | 0.50 | 0.92 | 15272 |
| stroke 4 | 41 % → 31 % | 566.1 px | 0.53 | 0.76 | 15401 |
| stroke 5 | 48 % → 35 % | 776.3 px | 0.53 | 0.73 | 30702 |

Numbers say: wet paint spreads well beyond the stroke.

## Oil focus · C round — own sheet
own sheet 2000 × 1320 · Gouache 1.00 + turpentine 15 % · 260 px · 159.3 s

![Oil focus · C round — own sheet](Oil-focus-C-round-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 11 % → 41 % | 130.2 px | 0.54 | 3.88 | 5050 |
| stroke 2 | 20 % → 30 % | 252.7 px | 0.48 | 1.45 | 5526 |
| stroke 3 | 24 % → 26 % | 222.8 px | 0.54 | 1.08 | 14605 |
| stroke 4 | 29 % → 26 % | 396.5 px | 0.55 | 0.89 | 42834 |
| stroke 5 | 34 % → 29 % | 550.7 px | 0.53 | 0.84 | 11530 |

Numbers say: wet paint spreads well beyond the stroke.

## Oil focus · D worn — own sheet
own sheet 2000 × 1320 · Gouache 1.00 + turpentine 15 % · 260 px · 212.2 s

![Oil focus · D worn — own sheet](Oil-focus-D-worn-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 16 % → 49 % | 193.8 px | 0.52 | 3.12 | 7964 |
| stroke 2 | 29 % → 31 % | 353.2 px | 0.45 | 1.10 | 8610 |
| stroke 3 | 34 % → 34 % | 319.6 px | 0.50 | 0.99 | 51462 |
| stroke 4 | 37 % → 30 % | 514.9 px | 0.54 | 0.82 | 30822 |
| stroke 5 | 44 % → 32 % | 709.0 px | 0.54 | 0.74 | 11707 |

Numbers say: wet paint spreads well beyond the stroke.

## Oil focus · E swell — own sheet
own sheet 2000 × 1320 · Gouache 1.00 + turpentine 15 % · 260 px · 221.5 s

![Oil focus · E swell — own sheet](Oil-focus-E-swell-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 16 % → 52 % | 192.2 px | 0.53 | 3.32 | 10047 |
| stroke 2 | 29 % → 32 % | 356.8 px | 0.46 | 1.12 | 11086 |
| stroke 3 | 36 % → 34 % | 335.5 px | 0.50 | 0.95 | 56124 |
| stroke 4 | 42 % → 32 % | 581.2 px | 0.54 | 0.76 | 27858 |
| stroke 5 | 50 % → 35 % | 807.1 px | 0.55 | 0.71 | 11984 |

Numbers say: wet paint spreads well beyond the stroke.

## Oil focus · F steady hand — own sheet
own sheet 2000 × 1320 · Gouache 1.00 + turpentine 15 % · 260 px · 211.6 s

![Oil focus · F steady hand — own sheet](Oil-focus-F-steady-hand-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 15 % → 51 % | 190.7 px | 0.52 | 3.33 | 8074 |
| stroke 2 | 29 % → 32 % | 353.1 px | 0.45 | 1.13 | 17195 |
| stroke 3 | 36 % → 33 % | 334.1 px | 0.49 | 0.93 | 42238 |
| stroke 4 | 42 % → 32 % | 579.7 px | 0.53 | 0.76 | 24415 |
| stroke 5 | 50 % → 36 % | 807.7 px | 0.54 | 0.72 | 9128 |

Numbers say: wet paint spreads well beyond the stroke.

## Oil focus · G soft hairs — own sheet
own sheet 2000 × 1320 · Gouache 1.00 + turpentine 15 % · 260 px · 200.3 s

![Oil focus · G soft hairs — own sheet](Oil-focus-G-soft-hairs-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 15 % → 44 % | 187.9 px | 0.51 | 2.92 | 25571 |
| stroke 2 | 28 % → 25 % | 349.5 px | 0.42 | 0.89 | 15949 |
| stroke 3 | 35 % → 30 % | 328.0 px | 0.47 | 0.86 | 25558 |
| stroke 4 | 40 % → 27 % | 557.5 px | 0.52 | 0.68 | 18205 |
| stroke 5 | 48 % → 29 % | 788.6 px | 0.54 | 0.61 | 8964 |

Numbers say: wet paint spreads well beyond the stroke.

## Oil focus · H narrow — own sheet
own sheet 2000 × 1320 · Gouache 1.00 + turpentine 15 % · 200 px · 156.1 s

![Oil focus · H narrow — own sheet](Oil-focus-H-narrow-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 20 % → 43 % | 190.7 px | 0.54 | 2.18 | 9286 |
| stroke 2 | 24 % → 26 % | 230.0 px | 0.42 | 1.09 | 12435 |
| stroke 3 | 34 % → 28 % | 273.6 px | 0.45 | 0.81 | 12103 |
| stroke 4 | 36 % → 30 % | 398.3 px | 0.50 | 0.81 | 12489 |
| stroke 5 | 47 % → 33 % | 608.6 px | 0.55 | 0.70 | 8436 |

Numbers say: wet paint spreads well beyond the stroke.

## Refs v3 · #01 HW peach cloud — own sheet
own sheet 800 × 1095 · Gouache 1.00 + turpentine 30 % · 104 px · 823.0 s

![Refs v3 · #01 HW peach cloud — own sheet](Refs-v3-01-HW-peach-cloud-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 9 % → 75 % | 103.6 px | 0.14 | 7.96 | 176 |
| stroke 2 | 14 % → 79 % | 175.7 px | 0.13 | 5.51 | 221 |
| stroke 3 | 20 % → 80 % | 300.1 px | 0.14 | 3.97 | 216 |
| stroke 4 | 21 % → 80 % | 362.0 px | 0.13 | 3.75 | 300 |
| stroke 5 | 12 % → 87 % | 123.9 px | 0.24 | 7.55 | 680 |
| stroke 6 | 24 % → 86 % | 267.8 px | 0.14 | 3.58 | 593 |
| stroke 7 | 41 % → 88 % | 805.7 px | 0.15 | 2.13 | 251 |
| stroke 8 | 27 % → 82 % | 189.7 px | 0.14 | 3.05 | 1558 |
| stroke 9 | 44 % → 81 % | 400.2 px | 0.18 | 1.84 | 498 |
| stroke 10 | 39 % → 80 % | 431.7 px | 0.12 | 2.04 | 631 |
| stroke 11 | 60 % → 84 % | 945.8 px | 0.12 | 1.38 | 305 |
| stroke 12 | 20 % → 83 % | 180.8 px | 0.16 | 4.17 | 554 |
| stroke 13 | 64 % → 86 % | 990.7 px | 0.14 | 1.34 | 250 |
| stroke 14 | 52 % → 89 % | 684.6 px | 0.13 | 1.72 | 894 |
| stroke 15 | 54 % → 93 % | 764.0 px | 0.16 | 1.72 | 538 |
| stroke 16 | 43 % → 80 % | 884.3 px | 0.12 | 1.84 | 266 |
| stroke 17 | 49 % → 88 % | 696.6 px | 0.15 | 1.79 | 522 |
| stroke 18 | 49 % → 77 % | 676.2 px | 0.12 | 1.57 | 378 |
| stroke 19 | 58 % → 93 % | 1309.4 px | 0.15 | 1.60 | 378 |
| stroke 20 | 59 % → 78 % | 518.9 px | 0.12 | 1.31 | 826 |
| stroke 21 | 58 % → 75 % | 811.2 px | 0.12 | 1.28 | 337 |
| stroke 22 | 45 % → 90 % | 891.9 px | 0.19 | 1.97 | 254 |
| stroke 23 | 61 % → 85 % | 924.5 px | 0.14 | 1.39 | 429 |
| stroke 24 | 73 % → 85 % | 1422.3 px | 0.12 | 1.16 | 459 |
| stroke 25 | 63 % → 88 % | 981.5 px | 0.15 | 1.38 | 347 |
| stroke 26 | 59 % → 91 % | 1359.7 px | 0.18 | 1.55 | 223 |
| stroke 27 | 60 % → 87 % | 1148.4 px | 0.18 | 1.45 | 428 |
| stroke 28 | 73 % → 89 % | 1652.7 px | 0.15 | 1.22 | 269 |
| stroke 29 | 82 % → 85 % | 1256.7 px | 0.11 | 1.04 | 475 |
| stroke 30 | 64 % → 94 % | 1296.9 px | 0.19 | 1.46 | 321 |
| stroke 31 | 78 % → 93 % | 1654.0 px | 0.14 | 1.20 | 334 |
| stroke 32 | 23 % → 89 % | 307.7 px | 0.26 | 3.94 | 619 |
| stroke 33 | 27 % → 90 % | 445.0 px | 0.27 | 3.27 | 681 |
| stroke 34 | 26 % → 76 % | 272.0 px | 0.24 | 2.95 | 105 |
| stroke 35 | 44 % → 69 % | 1079.6 px | 0.13 | 1.57 | 17 |
| stroke 36 | 61 % → 70 % | 466.6 px | 0.12 | 1.15 | 200 |
| stroke 37 | 69 % → 75 % | 835.0 px | 0.12 | 1.10 | 113 |
| stroke 38 | 66 % → 71 % | 556.8 px | 0.12 | 1.07 | 113 |
| stroke 39 | 69 % → 74 % | 1011.9 px | 0.12 | 1.08 | 129 |
| stroke 40 | 67 % → 72 % | 835.0 px | 0.12 | 1.08 | 82 |
| stroke 41 | 67 % → 74 % | 1937.3 px | 0.12 | 1.10 | 36 |
| stroke 42 | 69 % → 75 % | 2655.1 px | 0.12 | 1.09 | 52 |
| stroke 43 | 67 % → 73 % | 1914.0 px | 0.12 | 1.09 | 166 |
| stroke 44 | 64 % → 76 % | 1012.0 px | 0.14 | 1.19 | 98 |
| stroke 45 | 65 % → 76 % | 684.7 px | 0.14 | 1.17 | 135 |
| stroke 46 | 68 % → 76 % | 2781.7 px | 0.14 | 1.13 | 37 |
| stroke 47 | 63 % → 75 % | 2109.0 px | 0.15 | 1.20 | 46 |
| stroke 48 | 76 % → 80 % | 1472.5 px | 0.13 | 1.05 | 65 |
| stroke 49 | 76 % → 82 % | 1347.7 px | 0.13 | 1.09 | 161 |
| stroke 50 | 75 % → 80 % | 2124.8 px | 0.13 | 1.07 | 177 |
| stroke 51 | 82 % → 85 % | 2887.9 px | 0.12 | 1.04 | 331 |
| stroke 52 | 77 % → 85 % | 2680.7 px | 0.14 | 1.10 | 74 |
| stroke 53 | 78 % → 79 % | 1543.5 px | 0.12 | 1.02 | 98 |
| stroke 54 | 77 % → 81 % | 1430.0 px | 0.13 | 1.05 | 492 |
| stroke 55 | 82 % → 84 % | 1809.6 px | 0.12 | 1.03 | 70 |
| stroke 56 | 78 % → 81 % | 2122.6 px | 0.13 | 1.04 | 54 |
| stroke 57 | 76 % → 81 % | 2163.7 px | 0.14 | 1.06 | 71 |
| stroke 58 | 84 % → 85 % | 1414.8 px | 0.12 | 1.01 | 134 |
| stroke 59 | 79 % → 86 % | 1625.4 px | 0.14 | 1.09 | 230 |
| stroke 60 | 80 % → 80 % | 2077.3 px | 0.13 | 1.00 | 101 |
| stroke 61 | 87 % → 86 % | 2560.7 px | 0.11 | 1.00 | 119 |
| stroke 62 | 79 % → 81 % | 3920.3 px | 0.13 | 1.02 | 30 |
| stroke 63 | 80 % → 81 % | 3574.6 px | 0.13 | 1.02 | 40 |
| stroke 64 | 79 % → 82 % | 2507.2 px | 0.13 | 1.04 | 37 |
| stroke 65 | 86 % → 86 % | 5460.3 px | 0.12 | 1.00 | 23 |
| stroke 66 | 87 % → 86 % | 4194.9 px | 0.12 | 0.99 | 24 |
| stroke 67 | 79 % → 81 % | 2797.5 px | 0.13 | 1.02 | 37 |
| stroke 68 | 83 % → 88 % | 3350.6 px | 0.13 | 1.06 | 68 |
| stroke 69 | 78 % → 80 % | 3104.5 px | 0.13 | 1.02 | 38 |
| stroke 70 | 85 % → 84 % | 3990.0 px | 0.12 | 0.99 | 70 |
| stroke 71 | 80 % → 83 % | 5093.3 px | 0.13 | 1.03 | 20 |
| stroke 72 | 82 % → 82 % | 3753.2 px | 0.13 | 1.00 | 31 |
| stroke 73 | 88 % → 87 % | 4622.0 px | 0.11 | 0.99 | 41 |
| stroke 74 | 75 % → 75 % | 1626.4 px | 0.13 | 0.99 | 22 |
| stroke 75 | 74 % → 74 % | 2458.8 px | 0.14 | 1.00 | 14 |
| stroke 76 | 77 % → 76 % | 1326.7 px | 0.13 | 0.98 | 77 |
| stroke 77 | 76 % → 76 % | 2804.4 px | 0.14 | 0.99 | 15 |
| stroke 78 | 76 % → 75 % | 2339.7 px | 0.14 | 0.99 | 32 |
| stroke 79 | 63 % → 84 % | 3097.6 px | 0.14 | 1.34 | 54 |
| stroke 80 | 59 % → 85 % | 3643.5 px | 0.15 | 1.44 | 35 |
| stroke 81 | 60 % → 84 % | 3348.9 px | 0.14 | 1.39 | 35 |
| stroke 82 | 61 % → 84 % | 2705.5 px | 0.14 | 1.37 | 49 |
| stroke 83 | 70 % → 85 % | 3543.5 px | 0.16 | 1.20 | 34 |
| stroke 84 | 60 % → 86 % | 1310.0 px | 0.20 | 1.43 | 99 |
| stroke 85 | 66 % → 85 % | 3055.9 px | 0.17 | 1.28 | 41 |
| stroke 86 | 62 % → 86 % | 2452.6 px | 0.20 | 1.38 | 27 |
| stroke 87 | 33 % → 76 % | 338.7 px | 0.23 | 2.27 | 102 |
| stroke 88 | 58 % → 82 % | 682.4 px | 0.15 | 1.42 | 92 |
| stroke 89 | 44 % → 80 % | 541.2 px | 0.19 | 1.81 | 386 |
| stroke 90 | 60 % → 85 % | 2379.4 px | 0.15 | 1.41 | 32 |
| stroke 91 | 36 % → 76 % | 395.7 px | 0.23 | 2.13 | 109 |
| stroke 92 | 59 % → 80 % | 580.9 px | 0.17 | 1.37 | 117 |
| stroke 93 | 65 % → 80 % | 588.0 px | 0.15 | 1.24 | 456 |
| stroke 94 | 67 % → 82 % | 1557.2 px | 0.15 | 1.22 | 92 |
| stroke 95 | 68 % → 85 % | 1624.2 px | 0.15 | 1.25 | 86 |
| stroke 96 | 70 % → 81 % | 1293.4 px | 0.15 | 1.17 | 62 |
| stroke 97 | 62 % → 81 % | 1067.0 px | 0.17 | 1.31 | 98 |
| stroke 98 | 70 % → 83 % | 2650.2 px | 0.15 | 1.19 | 41 |
| stroke 99 | 59 % → 81 % | 859.1 px | 0.18 | 1.37 | 110 |
| stroke 100 | 70 % → 84 % | 2572.1 px | 0.15 | 1.21 | 46 |
| stroke 101 | 66 % → 79 % | 1555.2 px | 0.16 | 1.19 | 37 |
| stroke 102 | 70 % → 85 % | 2957.8 px | 0.15 | 1.20 | 29 |
| stroke 103 | 72 % → 82 % | 2661.4 px | 0.15 | 1.14 | 18 |
| stroke 104 | 69 % → 81 % | 1126.5 px | 0.16 | 1.17 | 117 |
| stroke 105 | 72 % → 82 % | 2049.2 px | 0.15 | 1.14 | 50 |
| stroke 106 | 68 % → 82 % | 1320.8 px | 0.16 | 1.21 | 70 |
| stroke 107 | 72 % → 82 % | 2812.2 px | 0.15 | 1.13 | 18 |
| stroke 108 | 70 % → 83 % | 3189.9 px | 0.15 | 1.19 | 31 |
| stroke 109 | 66 % → 94 % | 1602.2 px | 0.19 | 1.41 | 180 |
| stroke 110 | 68 % → 94 % | 3939.0 px | 0.18 | 1.37 | 77 |
| stroke 111 | 65 % → 94 % | 3701.5 px | 0.20 | 1.45 | 36 |
| stroke 112 | 69 % → 93 % | 3990.3 px | 0.18 | 1.35 | 41 |
| stroke 113 | 69 % → 93 % | 4456.4 px | 0.18 | 1.35 | 20 |
| stroke 114 | 43 % → 82 % | 463.6 px | 0.21 | 1.89 | 100 |
| stroke 115 | 34 % → 81 % | 341.2 px | 0.20 | 2.38 | 132 |
| stroke 116 | 25 % → 81 % | 523.1 px | 0.24 | 3.20 | 46 |
| stroke 117 | 9 % → 76 % | 103.0 px | 0.32 | 8.07 | 71 |
| stroke 118 | 10 % → 78 % | 246.3 px | 0.33 | 7.76 | 63 |
| stroke 119 | 31 % → 80 % | 313.3 px | 0.24 | 2.59 | 139 |
| stroke 120 | 22 % → 82 % | 355.6 px | 0.29 | 3.74 | 107 |
| stroke 121 | 54 % → 82 % | 869.9 px | 0.20 | 1.52 | 196 |
| stroke 122 | 53 % → 80 % | 753.0 px | 0.18 | 1.52 | 105 |
| stroke 123 | 34 % → 81 % | 686.8 px | 0.23 | 2.36 | 107 |
| stroke 124 | 24 % → 82 % | 868.6 px | 0.26 | 3.39 | 25 |
| stroke 125 | 12 % → 76 % | 469.5 px | 0.34 | 6.29 | 18 |
| stroke 126 | 53 % → 91 % | 1195.1 px | 0.23 | 1.72 | 61 |
| stroke 127 | 60 % → 90 % | 1198.2 px | 0.20 | 1.49 | 119 |
| stroke 128 | 53 % → 92 % | 3439.9 px | 0.24 | 1.73 | 42 |
| stroke 129 | 64 % → 92 % | 2412.4 px | 0.20 | 1.44 | 49 |
| stroke 130 | 9 % → 82 % | 511.9 px | 0.36 | 9.06 | 21 |
| stroke 131 | 10 % → 83 % | 551.7 px | 0.36 | 8.60 | 47 |
| stroke 132 | 10 % → 83 % | 580.4 px | 0.36 | 8.39 | 39 |
| stroke 133 | 25 % → 64 % | 358.2 px | 0.28 | 2.54 | 66 |
| stroke 134 | 27 % → 65 % | 791.5 px | 0.28 | 2.44 | 151 |
| stroke 135 | 28 % → 66 % | 829.7 px | 0.27 | 2.33 | 30 |
| stroke 136 | 26 % → 64 % | 793.9 px | 0.28 | 2.49 | 18 |
| stroke 137 | 13 % → 79 % | 284.1 px | 0.35 | 6.13 | 58 |
| stroke 138 | 18 % → 72 % | 361.2 px | 0.34 | 4.03 | 55 |
| stroke 139 | 21 % → 71 % | 216.0 px | 0.34 | 3.37 | 76 |
| stroke 140 | 17 % → 77 % | 467.4 px | 0.36 | 4.43 | 38 |
| stroke 141 | 18 % → 78 % | 740.4 px | 0.36 | 4.24 | 23 |
| stroke 142 | 24 % → 70 % | 1114.0 px | 0.34 | 2.99 | 34 |
| stroke 143 | 16 % → 79 % | 719.4 px | 0.36 | 4.85 | 21 |
| stroke 144 | 77 % → 81 % | 4314.1 px | 0.12 | 1.05 | 12 |
| stroke 145 | 72 % → 75 % | 822.5 px | 0.14 | 1.04 | 53 |
| stroke 146 | 84 % → 90 % | 2844.4 px | 0.13 | 1.07 | 43 |
| stroke 147 | 69 % → 94 % | 1772.3 px | 0.18 | 1.37 | 45 |
| stroke 148 | 59 % → 96 % | 2462.5 px | 0.23 | 1.63 | 36 |
| stroke 149 | 54 % → 85 % | 3179.1 px | 0.23 | 1.58 | 22 |
| stroke 150 | 37 % → 84 % | 630.0 px | 0.25 | 2.29 | 183 |
| stroke 151 | 26 % → 86 % | 1283.8 px | 0.33 | 3.25 | 21 |
| stroke 152 | 26 % → 94 % | 1453.0 px | 0.32 | 3.61 | 8 |
| stroke 153 | 20 % → 83 % | 264.2 px | 0.36 | 4.18 | 432 |
| stroke 154 | 23 % → 81 % | 265.6 px | 0.34 | 3.44 | 179 |
| stroke 155 | 45 % → 76 % | 718.2 px | 0.24 | 1.70 | 157 |
| stroke 156 | 36 % → 78 % | 2072.4 px | 0.30 | 2.19 | 15 |
| stroke 157 | 34 % → 73 % | 827.8 px | 0.31 | 2.13 | 109 |
| stroke 158 | 27 % → 82 % | 1137.7 px | 0.36 | 3.07 | 13 |
| stroke 159 | 15 % → 76 % | 372.6 px | 0.39 | 4.99 | 76 |
| stroke 160 | 72 % → 74 % | 1156.5 px | 0.13 | 1.03 | 135 |
| stroke 161 | 71 % → 73 % | 996.4 px | 0.13 | 1.02 | 113 |
| stroke 162 | 73 % → 74 % | 856.0 px | 0.13 | 1.01 | 195 |
| stroke 163 | 74 % → 75 % | 2573.8 px | 0.13 | 1.01 | 26 |
| stroke 164 | 74 % → 74 % | 1636.5 px | 0.12 | 1.01 | 49 |
| stroke 165 | 72 % → 71 % | 581.9 px | 0.13 | 0.99 | 158 |
| stroke 166 | 58 % → 95 % | 1235.4 px | 0.24 | 1.63 | 97 |
| stroke 167 | 58 % → 95 % | 1487.6 px | 0.24 | 1.65 | 62 |
| stroke 168 | 65 % → 95 % | 3715.6 px | 0.21 | 1.45 | 24 |
| stroke 169 | 65 % → 95 % | 2656.5 px | 0.21 | 1.46 | 69 |
| stroke 170 | 61 % → 95 % | 1334.2 px | 0.23 | 1.56 | 339 |
| stroke 171 | 48 % → 94 % | 1548.0 px | 0.28 | 1.99 | 225 |
| stroke 172 | 75 % → 95 % | 4317.6 px | 0.18 | 1.26 | 49 |
| stroke 173 | 61 % → 96 % | 949.5 px | 0.24 | 1.56 | 187 |
| stroke 174 | 55 % → 95 % | 912.0 px | 0.27 | 1.71 | 151 |
| stroke 175 | 30 % → 89 % | 866.3 px | 0.36 | 3.00 | 162 |
| stroke 176 | 70 % → 95 % | 3476.0 px | 0.22 | 1.36 | 83 |
| stroke 177 | 41 % → 91 % | 893.7 px | 0.32 | 2.22 | 150 |
| stroke 178 | 54 % → 96 % | 1856.0 px | 0.29 | 1.79 | 46 |
| stroke 179 | 32 % → 84 % | 1225.8 px | 0.36 | 2.63 | 94 |
| stroke 180 | 33 % → 92 % | 795.6 px | 0.35 | 2.77 | 110 |
| stroke 181 | 56 % → 96 % | 1695.5 px | 0.28 | 1.72 | 86 |
| stroke 182 | 60 % → 94 % | 1601.1 px | 0.28 | 1.58 | 109 |
| stroke 183 | 49 % → 95 % | 2420.7 px | 0.32 | 1.94 | 218 |
| stroke 184 | 67 % → 96 % | 1943.8 px | 0.25 | 1.44 | 330 |
| stroke 185 | 79 % → 95 % | 3871.5 px | 0.20 | 1.21 | 87 |
| stroke 186 | 63 % → 96 % | 2049.0 px | 0.27 | 1.52 | 211 |
| stroke 187 | 50 % → 92 % | 1292.3 px | 0.31 | 1.84 | 512 |
| stroke 188 | 71 % → 95 % | 1798.8 px | 0.24 | 1.34 | 771 |
| stroke 189 | 37 % → 89 % | 1661.0 px | 0.36 | 2.42 | 128 |
| stroke 190 | 39 % → 91 % | 1930.4 px | 0.34 | 2.33 | 61 |
| stroke 191 | 59 % → 96 % | 2166.9 px | 0.29 | 1.64 | 139 |
| stroke 192 | 80 % → 94 % | 4463.1 px | 0.19 | 1.18 | 63 |
| stroke 193 | 78 % → 95 % | 3889.0 px | 0.20 | 1.21 | 40 |
| stroke 194 | 72 % → 96 % | 4046.6 px | 0.23 | 1.34 | 72 |
| stroke 195 | 55 % → 86 % | 1284.2 px | 0.27 | 1.56 | 108 |
| stroke 196 | 48 % → 85 % | 2132.8 px | 0.30 | 1.75 | 58 |
| stroke 197 | 54 % → 85 % | 1473.5 px | 0.27 | 1.58 | 68 |
| stroke 198 | 56 % → 86 % | 2043.3 px | 0.27 | 1.53 | 49 |
| stroke 199 | 42 % → 83 % | 446.7 px | 0.28 | 1.96 | 167 |
| stroke 200 | 47 % → 83 % | 512.6 px | 0.26 | 1.79 | 167 |
| stroke 201 | 63 % → 83 % | 1857.2 px | 0.22 | 1.33 | 35 |
| stroke 202 | 59 % → 82 % | 1678.8 px | 0.23 | 1.39 | 38 |
| stroke 203 | 30 % → 83 % | 596.0 px | 0.34 | 2.77 | 71 |
| stroke 204 | 63 % → 84 % | 1947.7 px | 0.23 | 1.34 | 49 |
| stroke 205 | 29 % → 82 % | 833.6 px | 0.34 | 2.84 | 131 |
| stroke 206 | 34 % → 83 % | 847.5 px | 0.31 | 2.47 | 229 |
| stroke 207 | 42 % → 82 % | 1604.9 px | 0.27 | 1.98 | 39 |
| stroke 208 | 71 % → 83 % | 1784.1 px | 0.19 | 1.18 | 75 |
| stroke 209 | 69 % → 82 % | 1563.3 px | 0.20 | 1.20 | 107 |
| stroke 210 | 75 % → 84 % | 1389.5 px | 0.17 | 1.12 | 204 |
| stroke 211 | 67 % → 82 % | 2198.1 px | 0.21 | 1.22 | 33 |
| stroke 212 | 79 % → 85 % | 3048.8 px | 0.17 | 1.08 | 42 |
| stroke 213 | 75 % → 86 % | 3303.2 px | 0.18 | 1.14 | 74 |
| stroke 214 | 33 % → 89 % | 562.3 px | 0.36 | 2.66 | 128 |
| stroke 215 | 33 % → 87 % | 923.9 px | 0.35 | 2.68 | 72 |
| stroke 216 | 32 % → 79 % | 425.1 px | 0.36 | 2.51 | 184 |
| stroke 217 | 30 % → 82 % | 597.1 px | 0.38 | 2.69 | 72 |
| stroke 218 | 34 % → 78 % | 1253.0 px | 0.35 | 2.28 | 75 |
| stroke 219 | 30 % → 80 % | 533.5 px | 0.38 | 2.70 | 322 |
| stroke 220 | 34 % → 86 % | 1233.1 px | 0.37 | 2.52 | 221 |
| stroke 221 | 30 % → 80 % | 873.0 px | 0.38 | 2.64 | 89 |
| stroke 222 | 34 % → 86 % | 1291.7 px | 0.38 | 2.55 | 90 |
| stroke 223 | 30 % → 81 % | 673.8 px | 0.39 | 2.69 | 102 |
| stroke 224 | 37 % → 83 % | 1386.6 px | 0.36 | 2.24 | 76 |
| stroke 225 | 41 % → 77 % | 1443.6 px | 0.35 | 1.88 | 126 |
| stroke 226 | 38 % → 83 % | 1013.0 px | 0.37 | 2.21 | 82 |
| stroke 227 | 40 % → 84 % | 862.5 px | 0.37 | 2.09 | 91 |
| stroke 228 | 39 % → 83 % | 1526.8 px | 0.36 | 2.12 | 96 |
| stroke 229 | 34 % → 81 % | 1180.6 px | 0.38 | 2.40 | 68 |
| stroke 230 | 46 % → 91 % | 920.7 px | 0.35 | 1.99 | 226 |
| stroke 231 | 35 % → 81 % | 833.7 px | 0.38 | 2.32 | 223 |
| stroke 232 | 39 % → 84 % | 1334.6 px | 0.38 | 2.15 | 68 |
| stroke 233 | 40 % → 83 % | 2161.1 px | 0.37 | 2.09 | 35 |
| stroke 234 | 37 % → 80 % | 1696.7 px | 0.38 | 2.18 | 42 |
| stroke 235 | 39 % → 90 % | 1945.1 px | 0.39 | 2.31 | 60 |
| stroke 236 | 41 % → 80 % | 529.6 px | 0.37 | 1.94 | 104 |
| stroke 237 | 40 % → 82 % | 1044.9 px | 0.39 | 2.03 | 37 |
| stroke 238 | 40 % → 83 % | 1499.3 px | 0.40 | 2.08 | 32 |
| stroke 239 | 41 % → 83 % | 1776.4 px | 0.38 | 2.00 | 42 |
| stroke 240 | 82 % → 85 % | 1112.9 px | 0.15 | 1.03 | 142 |
| stroke 241 | 77 % → 96 % | 4449.9 px | 0.21 | 1.26 | 17 |
| stroke 242 | 83 % → 87 % | 5269.6 px | 0.15 | 1.05 | 9 |
| stroke 243 | 78 % → 83 % | 1696.6 px | 0.16 | 1.06 | 43 |
| stroke 244 | 57 % → 87 % | 1149.5 px | 0.29 | 1.53 | 66 |
| stroke 245 | 58 % → 83 % | 3352.6 px | 0.28 | 1.45 | 15 |
| stroke 246 | 57 % → 74 % | 578.6 px | 0.23 | 1.29 | 111 |
| stroke 247 | 43 % → 76 % | 642.5 px | 0.36 | 1.76 | 30 |
| stroke 248 | 67 % → 92 % | 1564.9 px | 0.26 | 1.38 | 64 |
| stroke 249 | 68 % → 95 % | 1524.7 px | 0.27 | 1.40 | 63 |
| stroke 250 | 72 % → 94 % | 1550.5 px | 0.25 | 1.31 | 79 |
| stroke 251 | 56 % → 92 % | 1021.1 px | 0.34 | 1.64 | 75 |
| stroke 252 | 75 % → 95 % | 1855.9 px | 0.25 | 1.26 | 62 |
| stroke 253 | 58 % → 92 % | 1063.9 px | 0.34 | 1.57 | 112 |
| stroke 254 | 67 % → 93 % | 1824.1 px | 0.30 | 1.40 | 71 |
| stroke 255 | 78 % → 91 % | 5062.9 px | 0.22 | 1.17 | 16 |
| stroke 256 | 71 % → 90 % | 3476.9 px | 0.27 | 1.28 | 32 |
| stroke 257 | 72 % → 95 % | 2325.2 px | 0.28 | 1.32 | 54 |
| stroke 258 | 66 % → 94 % | 3264.7 px | 0.32 | 1.43 | 18 |
| stroke 259 | 50 % → 90 % | 2021.2 px | 0.38 | 1.80 | 41 |
| stroke 260 | 49 % → 88 % | 1829.5 px | 0.39 | 1.82 | 22 |
| stroke 261 | 60 % → 93 % | 3376.0 px | 0.35 | 1.54 | 13 |
| stroke 262 | 71 % → 94 % | 3573.6 px | 0.29 | 1.32 | 49 |
| stroke 263 | 65 % → 93 % | 4193.8 px | 0.33 | 1.43 | 13 |
| stroke 264 | 75 % → 95 % | 3086.3 px | 0.27 | 1.26 | 43 |
| stroke 265 | 82 % → 96 % | 5282.7 px | 0.23 | 1.16 | 17 |
| stroke 266 | 82 % → 93 % | 5341.9 px | 0.22 | 1.14 | 24 |
| stroke 267 | 57 % → 91 % | 1394.0 px | 0.36 | 1.58 | 42 |
| stroke 268 | 68 % → 94 % | 1954.4 px | 0.31 | 1.38 | 53 |
| stroke 269 | 57 % → 89 % | 1094.9 px | 0.35 | 1.55 | 69 |
| stroke 270 | 68 % → 93 % | 1535.9 px | 0.32 | 1.37 | 41 |
| stroke 271 | 55 % → 87 % | 2811.7 px | 0.36 | 1.58 | 31 |
| stroke 272 | 66 % → 93 % | 1234.9 px | 0.33 | 1.41 | 81 |
| stroke 273 | 65 % → 93 % | 1312.9 px | 0.34 | 1.43 | 82 |
| stroke 274 | 72 % → 96 % | 3211.3 px | 0.32 | 1.34 | 96 |
| stroke 275 | 57 % → 87 % | 3224.2 px | 0.37 | 1.54 | 18 |
| stroke 276 | 73 % → 95 % | 2969.5 px | 0.31 | 1.30 | 39 |
| stroke 277 | 60 % → 92 % | 3404.3 px | 0.36 | 1.52 | 68 |
| stroke 278 | 66 % → 92 % | 3674.9 px | 0.34 | 1.40 | 44 |
| stroke 279 | 50 % → 80 % | 498.8 px | 0.37 | 1.60 | 58 |
| stroke 280 | 51 % → 79 % | 1149.3 px | 0.37 | 1.54 | 19 |
| stroke 281 | 53 % → 80 % | 1217.8 px | 0.38 | 1.53 | 36 |
| stroke 282 | 54 % → 81 % | 696.9 px | 0.38 | 1.49 | 174 |
| stroke 283 | 55 % → 79 % | 714.2 px | 0.38 | 1.44 | 54 |
| stroke 284 | 58 % → 79 % | 1094.9 px | 0.36 | 1.36 | 40 |
| stroke 285 | 57 % → 80 % | 2275.7 px | 0.37 | 1.39 | 24 |
| stroke 286 | 56 % → 78 % | 2585.5 px | 0.36 | 1.38 | 19 |
| stroke 287 | 55 % → 77 % | 1248.8 px | 0.40 | 1.39 | 8 |
| stroke 288 | 58 % → 80 % | 886.7 px | 0.37 | 1.39 | 41 |
| stroke 289 | 57 % → 77 % | 2631.0 px | 0.35 | 1.35 | 18 |
| stroke 290 | 58 % → 79 % | 1171.8 px | 0.37 | 1.35 | 27 |
| stroke 291 | 57 % → 77 % | 2050.7 px | 0.38 | 1.35 | 9 |
| stroke 292 | 58 % → 81 % | 3202.2 px | 0.38 | 1.39 | 9 |
| stroke 293 | 59 % → 82 % | 2176.6 px | 0.38 | 1.40 | 39 |
| stroke 294 | 58 % → 78 % | 2326.5 px | 0.38 | 1.35 | 15 |
| stroke 295 | 78 % → 79 % | 1024.5 px | 0.12 | 1.00 | 74 |
| stroke 296 | 77 % → 76 % | 1406.7 px | 0.12 | 0.98 | 71 |
| stroke 297 | 76 % → 75 % | 1152.9 px | 0.13 | 0.98 | 72 |
| stroke 298 | 82 % → 84 % | 2841.7 px | 0.17 | 1.02 | 23 |
| stroke 299 | 85 % → 96 % | 3013.4 px | 0.22 | 1.12 | 29 |
| stroke 300 | 76 % → 86 % | 3571.3 px | 0.24 | 1.13 | 26 |
| stroke 301 | 74 % → 83 % | 1794.8 px | 0.17 | 1.12 | 25 |
| stroke 302 | 70 % → 84 % | 2374.8 px | 0.30 | 1.20 | 33 |
| stroke 303 | 71 % → 87 % | 1147.4 px | 0.32 | 1.22 | 147 |
| stroke 304 | 68 % → 89 % | 4364.6 px | 0.31 | 1.32 | 9 |
| stroke 305 | 64 % → 82 % | 1781.1 px | 0.37 | 1.28 | 105 |
| stroke 306 | 62 % → 84 % | 2014.0 px | 0.39 | 1.35 | 32 |
| stroke 307 | 58 % → 74 % | 2091.8 px | 0.25 | 1.29 | 24 |
| stroke 308 | 58 % → 75 % | 1289.7 px | 0.29 | 1.31 | 72 |
| stroke 309 | 61 % → 83 % | 3724.5 px | 0.33 | 1.36 | 7 |
| stroke 310 | 62 % → 86 % | 1489.4 px | 0.38 | 1.38 | 96 |
| stroke 311 | 61 % → 86 % | 2615.9 px | 0.39 | 1.40 | 10 |
| stroke 312 | 80 % → 78 % | 1125.8 px | 0.12 | 0.97 | 96 |
| stroke 313 | 83 % → 80 % | 1894.8 px | 0.12 | 0.97 | 88 |
| stroke 314 | 79 % → 79 % | 941.7 px | 0.14 | 1.00 | 232 |
| stroke 315 | 79 % → 78 % | 1468.8 px | 0.13 | 0.98 | 56 |
| stroke 316 | 79 % → 77 % | 1852.7 px | 0.13 | 0.97 | 83 |
| stroke 317 | 77 % → 93 % | 4283.1 px | 0.32 | 1.21 | 66 |
| stroke 318 | 78 % → 93 % | 1145.8 px | 0.30 | 1.18 | 160 |
| stroke 319 | 90 % → 96 % | 1295.5 px | 0.23 | 1.07 | 268 |
| stroke 320 | 87 % → 94 % | 2295.9 px | 0.28 | 1.08 | 78 |
| stroke 321 | 81 % → 92 % | 1976.7 px | 0.32 | 1.14 | 109 |
| stroke 322 | 72 % → 89 % | 1138.9 px | 0.36 | 1.23 | 284 |
| stroke 323 | 86 % → 94 % | 4856.4 px | 0.32 | 1.09 | 44 |
| stroke 324 | 70 % → 89 % | 2621.4 px | 0.36 | 1.27 | 72 |
| stroke 325 | 85 % → 92 % | 4240.1 px | 0.32 | 1.08 | 27 |
| stroke 326 | 89 % → 96 % | 4402.0 px | 0.28 | 1.08 | 71 |
| stroke 327 | 86 % → 95 % | 4257.6 px | 0.30 | 1.10 | 39 |
| stroke 328 | 92 % → 96 % | 2110.1 px | 0.22 | 1.03 | 167 |
| stroke 329 | 72 % → 91 % | 3210.8 px | 0.37 | 1.26 | 28 |
| stroke 330 | 91 % → 97 % | 2603.4 px | 0.24 | 1.06 | 65 |
| stroke 331 | 82 % → 93 % | 4057.1 px | 0.33 | 1.13 | 35 |
| stroke 332 | 84 % → 87 % | 1751.5 px | 0.16 | 1.03 | 81 |
| stroke 333 | 85 % → 87 % | 1228.4 px | 0.19 | 1.03 | 168 |
| stroke 334 | 78 % → 83 % | 1068.0 px | 0.21 | 1.06 | 153 |
| stroke 335 | 81 % → 83 % | 1088.2 px | 0.18 | 1.02 | 194 |
| stroke 336 | 74 % → 84 % | 1199.9 px | 0.25 | 1.13 | 151 |
| stroke 337 | 65 % → 78 % | 1992.1 px | 0.27 | 1.20 | 100 |
| stroke 338 | 72 % → 82 % | 1484.0 px | 0.24 | 1.14 | 110 |
| stroke 339 | 86 % → 92 % | 2934.5 px | 0.33 | 1.08 | 59 |
| stroke 340 | 89 % → 94 % | 2716.4 px | 0.30 | 1.06 | 69 |
| stroke 341 | 77 % → 92 % | 1415.0 px | 0.38 | 1.20 | 94 |
| stroke 342 | 89 % → 93 % | 3053.9 px | 0.32 | 1.05 | 38 |
| stroke 343 | 91 % → 94 % | 2460.8 px | 0.29 | 1.03 | 113 |
| stroke 344 | 76 % → 91 % | 3220.0 px | 0.38 | 1.20 | 47 |
| stroke 345 | 90 % → 94 % | 1606.6 px | 0.32 | 1.04 | 99 |
| stroke 346 | 84 % → 94 % | 3122.2 px | 0.38 | 1.13 | 45 |
| stroke 347 | 94 % → 94 % | 5205.2 px | 0.29 | 1.01 | 38 |
| stroke 348 | 86 % → 94 % | 2152.1 px | 0.36 | 1.09 | 66 |
| stroke 349 | 67 % → 82 % | 1085.5 px | 0.37 | 1.22 | 124 |
| stroke 350 | 61 % → 78 % | 976.3 px | 0.37 | 1.29 | 87 |
| stroke 351 | 69 % → 79 % | 617.4 px | 0.39 | 1.14 | 114 |
| stroke 352 | 55 % → 67 % | 367.3 px | 0.35 | 1.23 | 122 |
| stroke 353 | 73 % → 85 % | 2620.1 px | 0.39 | 1.16 | 28 |
| stroke 354 | 64 % → 76 % | 778.9 px | 0.38 | 1.18 | 126 |
| stroke 355 | 76 % → 81 % | 899.6 px | 0.38 | 1.06 | 98 |
| stroke 356 | 76 % → 81 % | 1498.8 px | 0.36 | 1.07 | 85 |
| stroke 357 | 73 % → 78 % | 2076.4 px | 0.37 | 1.07 | 81 |
| stroke 358 | 68 % → 69 % | 739.1 px | 0.30 | 1.03 | 107 |
| stroke 359 | 78 % → 81 % | 1267.5 px | 0.37 | 1.03 | 140 |
| stroke 360 | 62 % → 65 % | 884.7 px | 0.32 | 1.04 | 40 |
| stroke 361 | 77 % → 81 % | 1877.3 px | 0.40 | 1.05 | 27 |
| stroke 362 | 73 % → 74 % | 1199.9 px | 0.35 | 1.01 | 42 |
| stroke 363 | 78 % → 80 % | 1727.3 px | 0.38 | 1.03 | 34 |
| stroke 364 | 78 % → 78 % | 744.3 px | 0.39 | 1.01 | 80 |
| stroke 365 | 82 % → 82 % | 1838.6 px | 0.36 | 1.00 | 66 |
| stroke 366 | 67 % → 67 % | 1235.3 px | 0.35 | 1.01 | 36 |
| stroke 367 | 79 % → 80 % | 3788.7 px | 0.36 | 1.01 | 19 |
| stroke 368 | 69 % → 69 % | 1363.8 px | 0.29 | 0.99 | 58 |
| stroke 369 | 64 % → 63 % | 1808.5 px | 0.29 | 0.99 | 20 |
| stroke 370 | 87 % → 87 % | 3843.8 px | 0.38 | 1.00 | 31 |
| stroke 371 | 82 % → 82 % | 2980.4 px | 0.35 | 1.00 | 65 |
| stroke 372 | 81 % → 80 % | 3121.5 px | 0.14 | 0.99 | 8 |
| stroke 373 | 85 % → 84 % | 1894.1 px | 0.20 | 0.99 | 36 |
| stroke 374 | 94 % → 93 % | 1318.1 px | 0.24 | 0.99 | 164 |
| stroke 375 | 96 % → 95 % | 4537.1 px | 0.26 | 1.00 | 53 |

Numbers say: wet paint spreads well beyond the stroke.

## Refs v3 · #02 HW cream strokes — own sheet
own sheet 800 × 650 · Gouache 1.00 + turpentine 30 % · 51 px · 243.2 s

![Refs v3 · #02 HW cream strokes — own sheet](Refs-v3-02-HW-cream-strokes-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 6 % → 58 % | 50.4 px | 0.13 | 9.04 | 79 |
| stroke 2 | 10 % → 55 % | 60.0 px | 0.13 | 5.30 | 95 |
| stroke 3 | 17 % → 46 % | 172.0 px | 0.12 | 2.75 | 26 |
| stroke 4 | 4 % → 98 % | 53.5 px | 0.24 | 23.29 | 21 |
| stroke 5 | 13 % → 86 % | 67.5 px | 0.19 | 6.67 | 111 |
| stroke 6 | 23 % → 75 % | 119.1 px | 0.14 | 3.30 | 108 |
| stroke 7 | 28 % → 80 % | 207.4 px | 0.10 | 2.81 | 80 |
| stroke 8 | 29 % → 67 % | 166.2 px | 0.10 | 2.29 | 90 |
| stroke 9 | 32 % → 82 % | 201.9 px | 0.19 | 2.53 | 95 |
| stroke 10 | 23 % → 63 % | 134.4 px | 0.11 | 2.72 | 225 |
| stroke 11 | 34 % → 88 % | 218.3 px | 0.16 | 2.57 | 98 |
| stroke 12 | 6 % → 96 % | 65.2 px | 0.16 | 17.15 | 33 |
| stroke 13 | 16 % → 77 % | 71.7 px | 0.16 | 4.85 | 154 |
| stroke 14 | 25 % → 80 % | 185.6 px | 0.16 | 3.22 | 128 |
| stroke 15 | 28 % → 97 % | 146.1 px | 0.17 | 3.44 | 132 |
| stroke 16 | 20 % → 97 % | 106.9 px | 0.17 | 4.86 | 227 |
| stroke 17 | 34 % → 97 % | 293.9 px | 0.18 | 2.86 | 78 |
| stroke 18 | 8 % → 96 % | 49.1 px | 0.10 | 11.88 | 91 |
| stroke 19 | 15 % → 96 % | 76.9 px | 0.14 | 6.32 | 140 |
| stroke 20 | 26 % → 95 % | 151.6 px | 0.16 | 3.62 | 135 |
| stroke 21 | 17 % → 94 % | 150.5 px | 0.22 | 5.72 | 55 |
| stroke 22 | 30 % → 90 % | 162.8 px | 0.13 | 2.98 | 120 |
| stroke 23 | 32 % → 88 % | 136.1 px | 0.11 | 2.75 | 156 |
| stroke 24 | 34 % → 89 % | 170.5 px | 0.12 | 2.58 | 184 |
| stroke 25 | 39 % → 95 % | 325.2 px | 0.13 | 2.43 | 90 |
| stroke 26 | 33 % → 87 % | 299.5 px | 0.14 | 2.61 | 50 |
| stroke 27 | 8 % → 56 % | 50.0 px | 0.15 | 7.29 | 52 |
| stroke 28 | 15 % → 70 % | 65.4 px | 0.19 | 4.72 | 127 |
| stroke 29 | 23 % → 81 % | 92.2 px | 0.20 | 3.45 | 248 |
| stroke 30 | 16 % → 91 % | 109.2 px | 0.27 | 5.73 | 131 |
| stroke 31 | 29 % → 80 % | 198.5 px | 0.20 | 2.78 | 137 |
| stroke 32 | 33 % → 87 % | 197.9 px | 0.20 | 2.64 | 202 |
| stroke 33 | 30 % → 93 % | 203.2 px | 0.23 | 3.09 | 142 |
| stroke 34 | 40 % → 85 % | 157.8 px | 0.20 | 2.13 | 269 |
| stroke 35 | 44 % → 94 % | 321.1 px | 0.18 | 2.12 | 99 |
| stroke 36 | 43 % → 64 % | 399.7 px | 0.13 | 1.48 | 61 |
| stroke 37 | 38 % → 96 % | 487.5 px | 0.21 | 2.49 | 32 |
| stroke 38 | 48 % → 92 % | 596.6 px | 0.19 | 1.93 | 81 |
| stroke 39 | 25 % → 74 % | 112.1 px | 0.20 | 2.97 | 222 |
| stroke 40 | 38 % → 86 % | 246.3 px | 0.15 | 2.25 | 118 |
| stroke 41 | 26 % → 59 % | 121.5 px | 0.19 | 2.21 | 172 |
| stroke 42 | 33 % → 84 % | 315.3 px | 0.24 | 2.51 | 57 |
| stroke 43 | 20 % → 98 % | 361.8 px | 0.15 | 4.93 | 5 |
| stroke 44 | 42 % → 60 % | 216.7 px | 0.19 | 1.43 | 85 |
| stroke 45 | 32 % → 89 % | 246.6 px | 0.13 | 2.75 | 75 |
| stroke 46 | 38 % → 78 % | 175.1 px | 0.14 | 2.08 | 88 |
| stroke 47 | 34 % → 63 % | 204.2 px | 0.16 | 1.88 | 115 |
| stroke 48 | 39 % → 77 % | 208.7 px | 0.17 | 1.98 | 88 |
| stroke 49 | 51 % → 80 % | 502.2 px | 0.11 | 1.56 | 58 |
| stroke 50 | 42 % → 78 % | 235.5 px | 0.17 | 1.85 | 92 |
| stroke 51 | 50 % → 75 % | 626.3 px | 0.16 | 1.49 | 23 |
| stroke 52 | 44 % → 81 % | 457.6 px | 0.17 | 1.83 | 31 |
| stroke 53 | 51 % → 84 % | 341.2 px | 0.12 | 1.67 | 74 |
| stroke 54 | 48 % → 76 % | 291.3 px | 0.12 | 1.59 | 100 |
| stroke 55 | 55 % → 78 % | 402.0 px | 0.16 | 1.41 | 67 |
| stroke 56 | 52 % → 72 % | 512.5 px | 0.11 | 1.40 | 26 |
| stroke 57 | 56 % → 76 % | 814.6 px | 0.17 | 1.36 | 35 |
| stroke 58 | 45 % → 84 % | 465.5 px | 0.16 | 1.88 | 35 |
| stroke 59 | 50 % → 69 % | 720.7 px | 0.12 | 1.37 | 33 |
| stroke 60 | 56 % → 70 % | 645.8 px | 0.15 | 1.24 | 40 |
| stroke 61 | 52 % → 77 % | 794.4 px | 0.18 | 1.48 | 24 |
| stroke 62 | 65 % → 90 % | 914.7 px | 0.10 | 1.38 | 58 |
| stroke 63 | 56 % → 70 % | 482.4 px | 0.15 | 1.25 | 59 |
| stroke 64 | 56 % → 92 % | 514.3 px | 0.13 | 1.65 | 51 |
| stroke 65 | 56 % → 77 % | 474.3 px | 0.14 | 1.36 | 51 |
| stroke 66 | 55 % → 72 % | 641.2 px | 0.11 | 1.31 | 43 |
| stroke 67 | 60 % → 74 % | 763.5 px | 0.11 | 1.23 | 36 |
| stroke 68 | 50 % → 90 % | 788.3 px | 0.16 | 1.79 | 38 |
| stroke 69 | 51 % → 97 % | 399.2 px | 0.19 | 1.92 | 68 |
| stroke 70 | 52 % → 97 % | 543.7 px | 0.19 | 1.87 | 35 |
| stroke 71 | 40 % → 88 % | 226.2 px | 0.24 | 2.23 | 123 |
| stroke 72 | 50 % → 85 % | 399.8 px | 0.21 | 1.71 | 66 |
| stroke 73 | 46 % → 88 % | 398.2 px | 0.23 | 1.90 | 75 |
| stroke 74 | 53 % → 97 % | 658.7 px | 0.19 | 1.84 | 74 |
| stroke 75 | 49 % → 98 % | 555.9 px | 0.25 | 2.03 | 38 |
| stroke 76 | 63 % → 97 % | 516.1 px | 0.17 | 1.54 | 193 |
| stroke 77 | 49 % → 98 % | 579.5 px | 0.24 | 2.01 | 89 |
| stroke 78 | 57 % → 97 % | 525.0 px | 0.20 | 1.69 | 170 |
| stroke 79 | 50 % → 98 % | 534.4 px | 0.25 | 1.98 | 87 |
| stroke 80 | 52 % → 83 % | 682.8 px | 0.21 | 1.59 | 48 |
| stroke 81 | 62 % → 97 % | 670.4 px | 0.18 | 1.57 | 87 |
| stroke 82 | 55 % → 96 % | 778.7 px | 0.21 | 1.76 | 98 |
| stroke 83 | 39 % → 76 % | 387.0 px | 0.16 | 1.95 | 70 |
| stroke 84 | 45 % → 70 % | 260.0 px | 0.14 | 1.56 | 150 |
| stroke 85 | 33 % → 56 % | 306.4 px | 0.17 | 1.69 | 34 |
| stroke 86 | 45 % → 75 % | 605.9 px | 0.16 | 1.66 | 29 |
| stroke 87 | 45 % → 69 % | 539.0 px | 0.16 | 1.54 | 19 |
| stroke 88 | 63 % → 97 % | 951.4 px | 0.13 | 1.55 | 25 |
| stroke 89 | 63 % → 97 % | 340.8 px | 0.17 | 1.53 | 239 |
| stroke 90 | 64 % → 96 % | 415.3 px | 0.18 | 1.50 | 481 |
| stroke 91 | 67 % → 96 % | 696.6 px | 0.18 | 1.43 | 98 |
| stroke 92 | 72 % → 96 % | 979.3 px | 0.16 | 1.33 | 48 |
| stroke 93 | 63 % → 79 % | 308.0 px | 0.07 | 1.27 | 122 |
| stroke 94 | 58 % → 91 % | 313.3 px | 0.15 | 1.55 | 145 |
| stroke 95 | 81 % → 98 % | 910.4 px | 0.07 | 1.20 | 151 |
| stroke 96 | 54 % → 66 % | 380.2 px | 0.09 | 1.23 | 75 |
| stroke 97 | 62 % → 73 % | 435.3 px | 0.07 | 1.17 | 64 |
| stroke 98 | 66 % → 86 % | 334.7 px | 0.10 | 1.30 | 84 |
| stroke 99 | 45 % → 91 % | 509.9 px | 0.25 | 2.01 | 36 |
| stroke 100 | 64 % → 87 % | 428.6 px | 0.11 | 1.36 | 131 |
| stroke 101 | 45 % → 89 % | 413.2 px | 0.29 | 1.98 | 43 |
| stroke 102 | 70 % → 85 % | 659.0 px | 0.09 | 1.22 | 99 |
| stroke 103 | 84 % → 93 % | 1026.5 px | 0.08 | 1.10 | 31 |
| stroke 104 | 79 % → 94 % | 477.5 px | 0.11 | 1.20 | 89 |
| stroke 105 | 73 % → 79 % | 982.3 px | 0.08 | 1.09 | 84 |
| stroke 106 | 58 % → 91 % | 784.1 px | 0.21 | 1.56 | 48 |
| stroke 107 | 63 % → 68 % | 627.5 px | 0.06 | 1.07 | 40 |
| stroke 108 | 57 % → 81 % | 531.2 px | 0.14 | 1.44 | 42 |
| stroke 109 | 67 % → 93 % | 831.2 px | 0.16 | 1.40 | 41 |
| stroke 110 | 75 % → 78 % | 876.8 px | 0.06 | 1.04 | 38 |
| stroke 111 | 91 % → 95 % | 1363.6 px | 0.07 | 1.05 | 31 |
| stroke 112 | 91 % → 98 % | 1380.2 px | 0.08 | 1.09 | 36 |
| stroke 113 | 59 % → 86 % | 501.8 px | 0.17 | 1.47 | 51 |
| stroke 114 | 68 % → 96 % | 340.2 px | 0.18 | 1.41 | 172 |
| stroke 115 | 47 % → 87 % | 345.4 px | 0.26 | 1.85 | 57 |
| stroke 116 | 48 % → 52 % | 823.5 px | 0.06 | 1.08 | 9 |
| stroke 117 | 75 % → 94 % | 365.7 px | 0.16 | 1.26 | 131 |
| stroke 118 | 72 % → 89 % | 685.4 px | 0.17 | 1.24 | 124 |
| stroke 119 | 64 % → 77 % | 426.7 px | 0.16 | 1.21 | 80 |
| stroke 120 | 67 % → 80 % | 378.1 px | 0.17 | 1.18 | 194 |
| stroke 121 | 70 % → 83 % | 623.4 px | 0.17 | 1.19 | 102 |
| stroke 122 | 71 % → 82 % | 415.4 px | 0.17 | 1.16 | 141 |
| stroke 123 | 66 % → 83 % | 890.1 px | 0.15 | 1.25 | 32 |
| stroke 124 | 60 % → 70 % | 922.2 px | 0.15 | 1.17 | 34 |
| stroke 125 | 79 % → 91 % | 722.9 px | 0.17 | 1.15 | 48 |
| stroke 126 | 67 % → 75 % | 455.5 px | 0.16 | 1.12 | 95 |
| stroke 127 | 66 % → 78 % | 879.2 px | 0.17 | 1.18 | 37 |
| stroke 128 | 74 % → 84 % | 672.6 px | 0.17 | 1.13 | 93 |
| stroke 129 | 64 % → 80 % | 306.8 px | 0.13 | 1.24 | 160 |
| stroke 130 | 79 % → 91 % | 410.4 px | 0.12 | 1.14 | 199 |
| stroke 131 | 82 % → 88 % | 433.6 px | 0.14 | 1.07 | 149 |
| stroke 132 | 90 % → 97 % | 780.5 px | 0.17 | 1.08 | 90 |
| stroke 133 | 84 % → 89 % | 523.7 px | 0.15 | 1.06 | 142 |
| stroke 134 | 84 % → 89 % | 506.6 px | 0.13 | 1.06 | 120 |
| stroke 135 | 91 % → 94 % | 800.2 px | 0.13 | 1.03 | 111 |
| stroke 136 | 85 % → 96 % | 792.5 px | 0.18 | 1.14 | 87 |
| stroke 137 | 83 % → 84 % | 565.3 px | 0.12 | 1.01 | 72 |
| stroke 138 | 88 % → 89 % | 1323.4 px | 0.14 | 1.01 | 28 |
| stroke 139 | 91 % → 92 % | 510.9 px | 0.13 | 1.02 | 105 |
| stroke 140 | 81 % → 81 % | 516.6 px | 0.13 | 1.00 | 70 |
| stroke 141 | 92 % → 98 % | 1384.7 px | 0.17 | 1.06 | 37 |
| stroke 142 | 76 % → 77 % | 532.3 px | 0.15 | 1.00 | 151 |
| stroke 143 | 85 % → 85 % | 1284.9 px | 0.16 | 1.01 | 29 |
| stroke 144 | 86 % → 88 % | 802.0 px | 0.13 | 1.02 | 34 |
| stroke 145 | 84 % → 96 % | 934.2 px | 0.19 | 1.15 | 52 |
| stroke 146 | 53 % → 88 % | 433.9 px | 0.24 | 1.64 | 126 |
| stroke 147 | 63 % → 96 % | 842.8 px | 0.24 | 1.53 | 37 |
| stroke 148 | 62 % → 96 % | 938.1 px | 0.24 | 1.56 | 73 |
| stroke 149 | 54 % → 88 % | 468.7 px | 0.24 | 1.62 | 193 |
| stroke 150 | 60 % → 75 % | 612.8 px | 0.19 | 1.26 | 26 |
| stroke 151 | 67 % → 72 % | 1116.0 px | 0.18 | 1.08 | 9 |
| stroke 152 | 65 % → 79 % | 643.6 px | 0.17 | 1.22 | 20 |
| stroke 153 | 69 % → 97 % | 629.5 px | 0.21 | 1.41 | 88 |
| stroke 154 | 62 % → 98 % | 1119.7 px | 0.25 | 1.59 | 11 |
| stroke 155 | 72 % → 96 % | 393.5 px | 0.18 | 1.34 | 109 |
| stroke 156 | 82 % → 83 % | 446.5 px | 0.08 | 1.02 | 217 |
| stroke 157 | 89 % → 96 % | 534.2 px | 0.09 | 1.08 | 106 |
| stroke 158 | 14 % → 44 % | 21.3 px | 0.52 | 3.08 | 302 |
| stroke 159 | 80 % → 89 % | 531.2 px | 0.12 | 1.10 | 169 |
| stroke 160 | 80 % → 87 % | 557.6 px | 0.12 | 1.09 | 110 |
| stroke 161 | 86 % → 97 % | 854.6 px | 0.14 | 1.12 | 67 |
| stroke 162 | 90 % → 98 % | 1074.1 px | 0.13 | 1.09 | 42 |
| stroke 163 | 67 % → 87 % | 300.2 px | 0.21 | 1.30 | 176 |
| stroke 164 | 82 % → 97 % | 453.0 px | 0.21 | 1.18 | 153 |
| stroke 165 | 75 % → 87 % | 384.8 px | 0.21 | 1.16 | 146 |
| stroke 166 | 81 % → 95 % | 476.2 px | 0.16 | 1.17 | 153 |
| stroke 167 | 86 % → 92 % | 448.3 px | 0.20 | 1.08 | 204 |
| stroke 168 | 91 % → 96 % | 489.1 px | 0.20 | 1.05 | 314 |
| stroke 169 | 94 % → 95 % | 809.2 px | 0.15 | 1.02 | 102 |
| stroke 170 | 94 % → 97 % | 764.2 px | 0.22 | 1.03 | 202 |
| stroke 171 | 86 % → 89 % | 417.1 px | 0.22 | 1.03 | 151 |
| stroke 172 | 95 % → 97 % | 1004.3 px | 0.22 | 1.02 | 22 |
| stroke 173 | 93 % → 94 % | 1135.5 px | 0.16 | 1.01 | 65 |
| stroke 174 | 87 % → 96 % | 594.7 px | 0.16 | 1.09 | 139 |
| stroke 175 | 97 % → 99 % | 1488.0 px | 0.23 | 1.02 | 22 |
| stroke 176 | 95 % → 97 % | 811.0 px | 0.24 | 1.02 | 82 |
| stroke 177 | 94 % → 96 % | 1445.6 px | 0.19 | 1.02 | 19 |
| stroke 178 | 69 % → 73 % | 279.7 px | 0.17 | 1.06 | 71 |
| stroke 179 | 70 % → 72 % | 530.2 px | 0.19 | 1.02 | 32 |
| stroke 180 | 96 % → 96 % | 682.2 px | 0.12 | 1.00 | 39 |
| stroke 181 | 80 % → 80 % | 597.2 px | 0.07 | 1.00 | 34 |
| stroke 182 | 58 % → 82 % | 259.9 px | 0.33 | 1.40 | 524 |
| stroke 183 | 65 % → 75 % | 334.5 px | 0.36 | 1.15 | 417 |
| stroke 184 | 73 % → 77 % | 273.8 px | 0.43 | 1.06 | 682 |
| stroke 185 | 68 % → 68 % | 181.4 px | 0.57 | 1.00 | 772 |
| stroke 186 | 88 % → 87 % | 466.3 px | 0.38 | 0.99 | 345 |
| stroke 187 | 86 % → 85 % | 391.5 px | 0.54 | 0.99 | 202 |

Numbers say: wet paint spreads well beyond the stroke.

## Refs v3 · #03 HW navy contours — own sheet
own sheet 800 × 600 · Gouache 1.00 + turpentine 30 % · 80 px · 186.9 s

![Refs v3 · #03 HW navy contours — own sheet](Refs-v3-03-HW-navy-contours-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 6 % → 90 % | 76.9 px | 0.49 | 14.96 | 362 |
| stroke 2 | 13 % → 84 % | 109.3 px | 0.48 | 6.59 | 473 |
| stroke 3 | 23 % → 88 % | 187.1 px | 0.50 | 3.81 | 424 |
| stroke 4 | 24 % → 78 % | 225.1 px | 0.48 | 3.30 | 839 |
| stroke 5 | 28 % → 86 % | 280.3 px | 0.50 | 3.06 | 742 |
| stroke 6 | 36 % → 93 % | 441.1 px | 0.50 | 2.60 | 343 |
| stroke 7 | 31 % → 89 % | 324.7 px | 0.49 | 2.87 | 787 |
| stroke 8 | 41 % → 77 % | 669.1 px | 0.43 | 1.91 | 376 |
| stroke 9 | 22 % → 68 % | 188.4 px | 0.54 | 3.05 | 951 |
| stroke 10 | 30 % → 70 % | 357.8 px | 0.53 | 2.32 | 486 |
| stroke 11 | 36 % → 66 % | 553.4 px | 0.51 | 1.85 | 332 |
| stroke 12 | 36 % → 68 % | 445.5 px | 0.54 | 1.92 | 200 |
| stroke 13 | 19 % → 81 % | 326.5 px | 0.47 | 4.34 | 182 |
| stroke 14 | 10 % → 95 % | 89.8 px | 0.47 | 9.78 | 67 |
| stroke 15 | 3 % → 32 % | 28.4 px | 0.22 | 9.68 | 55 |
| stroke 16 | 16 % → 94 % | 119.4 px | 0.48 | 5.98 | 110 |
| stroke 17 | 9 % → 71 % | 82.3 px | 0.43 | 7.96 | 103 |
| stroke 18 | 11 % → 38 % | 72.2 px | 0.31 | 3.57 | 405 |
| stroke 19 | 15 % → 58 % | 104.1 px | 0.39 | 3.92 | 226 |
| stroke 20 | 17 % → 55 % | 184.5 px | 0.43 | 3.29 | 124 |
| stroke 21 | 15 % → 77 % | 198.1 px | 0.48 | 5.07 | 15 |
| stroke 22 | 19 % → 90 % | 149.0 px | 0.46 | 4.81 | 28 |
| stroke 23 | 20 % → 95 % | 457.0 px | 0.47 | 4.75 | 13 |
| stroke 24 | 9 % → 37 % | 54.0 px | 0.39 | 4.00 | 72 |
| stroke 25 | 11 % → 38 % | 82.6 px | 0.41 | 3.51 | 67 |
| stroke 26 | 26 % → 93 % | 165.8 px | 0.44 | 3.51 | 38 |
| stroke 27 | 17 % → 34 % | 130.0 px | 0.27 | 2.00 | 419 |
| stroke 28 | 25 % → 94 % | 270.9 px | 0.45 | 3.76 | 48 |
| stroke 29 | 22 % → 40 % | 192.5 px | 0.34 | 1.85 | 120 |
| stroke 30 | 17 % → 83 % | 151.4 px | 0.46 | 5.00 | 128 |
| stroke 31 | 14 % → 40 % | 192.4 px | 0.43 | 2.81 | 51 |
| stroke 32 | 32 % → 93 % | 385.0 px | 0.46 | 2.94 | 95 |
| stroke 33 | 32 % → 85 % | 587.5 px | 0.46 | 2.69 | 23 |
| stroke 34 | 31 % → 93 % | 288.9 px | 0.44 | 3.03 | 52 |
| stroke 35 | 19 % → 79 % | 218.7 px | 0.49 | 4.07 | 25 |
| stroke 36 | 29 % → 94 % | 231.3 px | 0.45 | 3.28 | 48 |
| stroke 37 | 20 % → 83 % | 211.3 px | 0.49 | 4.15 | 89 |
| stroke 38 | 35 % → 87 % | 446.2 px | 0.46 | 2.48 | 130 |
| stroke 39 | 22 % → 83 % | 176.9 px | 0.49 | 3.79 | 59 |
| stroke 40 | 28 % → 96 % | 442.3 px | 0.49 | 3.47 | 22 |
| stroke 41 | 23 % → 84 % | 392.2 px | 0.47 | 3.68 | 24 |
| stroke 42 | 20 % → 27 % | 318.0 px | 0.20 | 1.34 | 25 |
| stroke 43 | 30 % → 96 % | 357.1 px | 0.48 | 3.13 | 35 |
| stroke 44 | 17 % → 36 % | 110.1 px | 0.38 | 2.09 | 56 |
| stroke 45 | 30 % → 65 % | 789.2 px | 0.42 | 2.20 | 19 |
| stroke 46 | 14 % → 43 % | 167.1 px | 0.49 | 2.98 | 25 |
| stroke 47 | 34 % → 94 % | 751.0 px | 0.44 | 2.72 | 21 |
| stroke 48 | 31 % → 96 % | 682.9 px | 0.47 | 3.12 | 18 |
| stroke 49 | 33 % → 72 % | 649.7 px | 0.43 | 2.20 | 16 |
| stroke 50 | 34 % → 94 % | 805.5 px | 0.45 | 2.77 | 26 |
| stroke 51 | 39 % → 93 % | 801.9 px | 0.44 | 2.37 | 17 |
| stroke 52 | 31 % → 80 % | 1312.1 px | 0.45 | 2.56 | 15 |
| stroke 53 | 35 % → 75 % | 514.1 px | 0.46 | 2.14 | 73 |
| stroke 54 | 32 % → 80 % | 297.3 px | 0.53 | 2.53 | 306 |
| stroke 55 | 41 % → 88 % | 232.8 px | 0.51 | 2.14 | 504 |
| stroke 56 | 34 % → 81 % | 289.5 px | 0.54 | 2.35 | 287 |
| stroke 57 | 46 % → 88 % | 324.9 px | 0.51 | 1.92 | 175 |
| stroke 58 | 48 % → 87 % | 346.1 px | 0.51 | 1.80 | 94 |
| stroke 59 | 36 % → 75 % | 1103.1 px | 0.48 | 2.11 | 51 |
| stroke 60 | 47 % → 84 % | 679.0 px | 0.53 | 1.78 | 60 |
| stroke 61 | 34 % → 65 % | 310.3 px | 0.54 | 1.94 | 216 |
| stroke 62 | 39 % → 61 % | 542.4 px | 0.56 | 1.56 | 56 |
| stroke 63 | 42 % → 62 % | 313.0 px | 0.54 | 1.49 | 198 |
| stroke 64 | 54 % → 81 % | 1100.2 px | 0.48 | 1.50 | 63 |
| stroke 65 | 45 % → 56 % | 770.1 px | 0.53 | 1.25 | 77 |
| stroke 66 | 41 % → 61 % | 747.5 px | 0.52 | 1.49 | 56 |
| stroke 67 | 49 % → 64 % | 350.5 px | 0.53 | 1.29 | 126 |
| stroke 68 | 48 % → 59 % | 1248.9 px | 0.54 | 1.23 | 39 |
| stroke 69 | 53 % → 74 % | 1545.9 px | 0.50 | 1.39 | 57 |
| stroke 70 | 48 % → 66 % | 574.7 px | 0.51 | 1.38 | 166 |
| stroke 71 | 49 % → 64 % | 683.9 px | 0.58 | 1.32 | 83 |
| stroke 72 | 56 % → 67 % | 1206.3 px | 0.51 | 1.20 | 42 |
| stroke 73 | 54 % → 62 % | 748.9 px | 0.45 | 1.16 | 153 |
| stroke 74 | 54 % → 73 % | 616.2 px | 0.51 | 1.35 | 177 |
| stroke 75 | 60 % → 64 % | 366.2 px | 0.51 | 1.07 | 174 |
| stroke 76 | 55 % → 61 % | 1326.6 px | 0.55 | 1.11 | 51 |
| stroke 77 | 70 % → 74 % | 1620.9 px | 0.58 | 1.06 | 39 |
| stroke 78 | 55 % → 60 % | 730.9 px | 0.45 | 1.09 | 153 |
| stroke 79 | 74 % → 76 % | 1221.5 px | 0.58 | 1.03 | 64 |
| stroke 80 | 60 % → 65 % | 1910.6 px | 0.45 | 1.10 | 31 |
| stroke 81 | 59 % → 62 % | 1499.0 px | 0.54 | 1.04 | 47 |
| stroke 82 | 62 % → 65 % | 755.3 px | 0.52 | 1.04 | 111 |
| stroke 83 | 58 % → 63 % | 1866.7 px | 0.45 | 1.08 | 65 |
| stroke 84 | 50 % → 90 % | 296.0 px | 0.47 | 1.82 | 171 |
| stroke 85 | 58 % → 89 % | 467.6 px | 0.51 | 1.54 | 269 |
| stroke 86 | 57 % → 93 % | 1034.2 px | 0.51 | 1.64 | 84 |
| stroke 87 | 58 % → 87 % | 811.1 px | 0.50 | 1.50 | 68 |
| stroke 88 | 54 % → 72 % | 425.7 px | 0.43 | 1.33 | 91 |
| stroke 89 | 63 % → 92 % | 866.1 px | 0.46 | 1.47 | 96 |
| stroke 90 | 68 % → 92 % | 914.6 px | 0.48 | 1.36 | 132 |
| stroke 91 | 71 % → 95 % | 1259.5 px | 0.49 | 1.34 | 250 |
| stroke 92 | 65 % → 87 % | 1144.9 px | 0.48 | 1.35 | 86 |
| stroke 93 | 65 % → 86 % | 591.7 px | 0.50 | 1.33 | 144 |
| stroke 94 | 69 % → 88 % | 639.3 px | 0.49 | 1.28 | 139 |
| stroke 95 | 72 % → 86 % | 1118.9 px | 0.50 | 1.21 | 53 |
| stroke 96 | 68 % → 88 % | 746.9 px | 0.51 | 1.29 | 156 |
| stroke 97 | 73 % → 92 % | 2101.5 px | 0.49 | 1.27 | 39 |
| stroke 98 | 64 % → 83 % | 810.8 px | 0.53 | 1.29 | 161 |
| stroke 99 | 77 % → 92 % | 1562.0 px | 0.48 | 1.19 | 47 |
| stroke 100 | 74 % → 86 % | 1588.2 px | 0.49 | 1.16 | 59 |
| stroke 101 | 77 % → 89 % | 1957.7 px | 0.52 | 1.15 | 60 |
| stroke 102 | 66 % → 89 % | 1146.5 px | 0.50 | 1.35 | 97 |
| stroke 103 | 65 % → 89 % | 1865.6 px | 0.52 | 1.38 | 58 |
| stroke 104 | 74 % → 84 % | 1535.6 px | 0.48 | 1.14 | 110 |
| stroke 105 | 66 % → 87 % | 811.5 px | 0.52 | 1.33 | 158 |
| stroke 106 | 86 % → 92 % | 1459.2 px | 0.49 | 1.08 | 76 |
| stroke 107 | 76 % → 92 % | 1739.1 px | 0.50 | 1.21 | 45 |
| stroke 108 | 81 % → 89 % | 2487.3 px | 0.48 | 1.10 | 33 |
| stroke 109 | 88 % → 94 % | 2177.8 px | 0.49 | 1.07 | 32 |
| stroke 110 | 72 % → 87 % | 2054.6 px | 0.52 | 1.21 | 161 |
| stroke 111 | 52 % → 57 % | 1576.1 px | 0.43 | 1.10 | 25 |
| stroke 112 | 69 % → 76 % | 728.8 px | 0.46 | 1.10 | 176 |
| stroke 113 | 61 % → 64 % | 1731.7 px | 0.42 | 1.05 | 55 |
| stroke 114 | 61 % → 67 % | 881.9 px | 0.45 | 1.10 | 69 |
| stroke 115 | 71 % → 78 % | 2444.0 px | 0.46 | 1.10 | 31 |
| stroke 116 | 63 % → 63 % | 1060.2 px | 0.45 | 1.01 | 209 |
| stroke 117 | 59 % → 96 % | 1732.6 px | 0.50 | 1.62 | 37 |
| stroke 118 | 57 % → 86 % | 917.2 px | 0.48 | 1.50 | 107 |
| stroke 119 | 49 % → 55 % | 2084.1 px | 0.53 | 1.13 | 11 |
| stroke 120 | 55 % → 66 % | 2431.1 px | 0.51 | 1.20 | 16 |
| stroke 121 | 64 % → 64 % | 1637.4 px | 0.56 | 1.00 | 23 |
| stroke 122 | 78 % → 90 % | 2817.6 px | 0.46 | 1.16 | 17 |
| stroke 123 | 71 % → 72 % | 1497.8 px | 0.56 | 1.02 | 31 |
| stroke 124 | 68 % → 70 % | 1047.8 px | 0.59 | 1.03 | 56 |
| stroke 125 | 71 % → 73 % | 2968.0 px | 0.51 | 1.02 | 49 |
| stroke 126 | 69 % → 86 % | 466.3 px | 0.52 | 1.25 | 566 |
| stroke 127 | 77 % → 89 % | 679.8 px | 0.51 | 1.15 | 448 |
| stroke 128 | 75 % → 79 % | 350.7 px | 0.56 | 1.05 | 330 |
| stroke 129 | 84 % → 87 % | 621.6 px | 0.52 | 1.03 | 519 |
| stroke 130 | 80 % → 80 % | 357.2 px | 0.58 | 1.01 | 381 |
| stroke 131 | 92 % → 93 % | 900.1 px | 0.53 | 1.01 | 165 |
| stroke 132 | 85 % → 85 % | 754.0 px | 0.55 | 1.00 | 89 |
| stroke 133 | 86 % → 86 % | 986.1 px | 0.54 | 1.00 | 109 |
| stroke 134 | 73 % → 75 % | 647.9 px | 0.43 | 1.04 | 302 |
| stroke 135 | 81 % → 81 % | 933.0 px | 0.45 | 1.00 | 245 |
| stroke 136 | 56 % → 56 % | 947.8 px | 0.52 | 1.01 | 21 |

Numbers say: wet paint spreads well beyond the stroke.

## Refs v3 · #04 HW grey cloud — own sheet
own sheet 800 × 635 · Gouache 1.00 + turpentine 30 % · 93 px · 309.8 s

![Refs v3 · #04 HW grey cloud — own sheet](Refs-v3-04-HW-grey-cloud-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 14 % → 98 % | 85.1 px | 0.21 | 7.14 | 560 |
| stroke 2 | 12 % → 98 % | 81.9 px | 0.19 | 7.91 | 1374 |
| stroke 3 | 25 % → 99 % | 248.3 px | 0.22 | 3.87 | 733 |
| stroke 4 | 37 % → 98 % | 200.0 px | 0.21 | 2.65 | 1877 |
| stroke 5 | 33 % → 98 % | 330.1 px | 0.20 | 2.97 | 1208 |
| stroke 6 | 50 % → 97 % | 652.1 px | 0.19 | 1.96 | 451 |
| stroke 7 | 40 % → 97 % | 602.1 px | 0.18 | 2.45 | 371 |
| stroke 8 | 55 % → 99 % | 456.6 px | 0.23 | 1.79 | 479 |
| stroke 9 | 65 % → 99 % | 535.5 px | 0.21 | 1.53 | 1222 |
| stroke 10 | 53 % → 97 % | 667.2 px | 0.18 | 1.82 | 1573 |
| stroke 11 | 35 % → 99 % | 440.9 px | 0.21 | 2.78 | 714 |
| stroke 12 | 61 % → 98 % | 1014.1 px | 0.21 | 1.60 | 228 |
| stroke 13 | 62 % → 98 % | 774.4 px | 0.23 | 1.60 | 454 |
| stroke 14 | 68 % → 99 % | 714.9 px | 0.23 | 1.46 | 282 |
| stroke 15 | 54 % → 99 % | 1000.4 px | 0.20 | 1.83 | 691 |
| stroke 16 | 59 % → 99 % | 701.2 px | 0.22 | 1.68 | 1444 |
| stroke 17 | 64 % → 98 % | 759.9 px | 0.22 | 1.54 | 2093 |
| stroke 18 | 42 % → 97 % | 372.9 px | 0.20 | 2.34 | 414 |
| stroke 19 | 57 % → 98 % | 729.6 px | 0.21 | 1.74 | 318 |
| stroke 20 | 76 % → 98 % | 817.4 px | 0.23 | 1.30 | 611 |
| stroke 21 | 73 % → 99 % | 928.4 px | 0.22 | 1.35 | 609 |
| stroke 22 | 58 % → 99 % | 1011.5 px | 0.22 | 1.71 | 228 |
| stroke 23 | 40 % → 98 % | 825.5 px | 0.17 | 2.45 | 158 |
| stroke 24 | 68 % → 98 % | 1112.2 px | 0.20 | 1.44 | 214 |
| stroke 25 | 31 % → 99 % | 653.4 px | 0.17 | 3.25 | 194 |
| stroke 26 | 18 % → 97 % | 585.2 px | 0.17 | 5.41 | 19 |
| stroke 27 | 17 % → 95 % | 340.7 px | 0.16 | 5.49 | 17 |
| stroke 28 | 4 % → 94 % | 65.5 px | 0.14 | 21.12 | 17 |
| stroke 29 | 62 % → 98 % | 670.7 px | 0.21 | 1.58 | 757 |
| stroke 30 | 51 % → 99 % | 471.7 px | 0.19 | 1.94 | 500 |
| stroke 31 | 38 % → 98 % | 266.8 px | 0.16 | 2.58 | 1082 |
| stroke 32 | 36 % → 97 % | 314.8 px | 0.15 | 2.69 | 402 |
| stroke 33 | 74 % → 98 % | 782.6 px | 0.21 | 1.34 | 332 |
| stroke 34 | 80 % → 99 % | 983.8 px | 0.21 | 1.23 | 333 |
| stroke 35 | 64 % → 99 % | 1554.4 px | 0.19 | 1.55 | 124 |
| stroke 36 | 77 % → 99 % | 1115.2 px | 0.21 | 1.29 | 243 |
| stroke 37 | 41 % → 94 % | 431.1 px | 0.15 | 2.28 | 98 |
| stroke 38 | 88 % → 99 % | 1980.7 px | 0.23 | 1.13 | 115 |
| stroke 39 | 67 % → 99 % | 871.9 px | 0.19 | 1.49 | 295 |
| stroke 40 | 55 % → 99 % | 960.9 px | 0.16 | 1.80 | 181 |
| stroke 41 | 68 % → 98 % | 1126.8 px | 0.18 | 1.44 | 292 |
| stroke 42 | 48 % → 97 % | 1142.0 px | 0.15 | 2.02 | 120 |
| stroke 43 | 88 % → 99 % | 1595.3 px | 0.23 | 1.12 | 222 |
| stroke 44 | 91 % → 99 % | 2427.8 px | 0.22 | 1.10 | 148 |
| stroke 45 | 55 % → 97 % | 477.5 px | 0.16 | 1.77 | 403 |
| stroke 46 | 50 % → 99 % | 1070.5 px | 0.14 | 2.00 | 123 |
| stroke 47 | 71 % → 99 % | 1932.7 px | 0.18 | 1.39 | 123 |
| stroke 48 | 58 % → 99 % | 1546.3 px | 0.16 | 1.70 | 111 |
| stroke 49 | 65 % → 97 % | 1018.4 px | 0.17 | 1.48 | 224 |
| stroke 50 | 80 % → 98 % | 1816.0 px | 0.21 | 1.23 | 148 |
| stroke 51 | 50 % → 99 % | 1204.3 px | 0.14 | 1.99 | 180 |
| stroke 52 | 77 % → 98 % | 1678.4 px | 0.21 | 1.26 | 148 |
| stroke 53 | 74 % → 98 % | 826.6 px | 0.20 | 1.32 | 519 |
| stroke 54 | 62 % → 96 % | 554.0 px | 0.18 | 1.56 | 420 |
| stroke 55 | 79 % → 98 % | 796.7 px | 0.20 | 1.24 | 472 |
| stroke 56 | 51 % → 95 % | 541.3 px | 0.15 | 1.87 | 220 |
| stroke 57 | 66 % → 96 % | 901.3 px | 0.18 | 1.46 | 475 |
| stroke 58 | 75 % → 97 % | 2198.8 px | 0.20 | 1.30 | 19 |
| stroke 59 | 58 % → 97 % | 1348.1 px | 0.16 | 1.66 | 39 |
| stroke 60 | 82 % → 97 % | 425.6 px | 0.19 | 1.19 | 236 |
| stroke 61 | 91 % → 99 % | 1477.1 px | 0.21 | 1.08 | 115 |
| stroke 62 | 93 % → 98 % | 446.5 px | 0.20 | 1.05 | 687 |
| stroke 63 | 92 % → 96 % | 925.7 px | 0.19 | 1.05 | 136 |
| stroke 64 | 96 % → 98 % | 925.8 px | 0.20 | 1.03 | 479 |
| stroke 65 | 92 % → 96 % | 1330.4 px | 0.18 | 1.04 | 153 |
| stroke 66 | 95 % → 97 % | 1496.2 px | 0.19 | 1.03 | 196 |
| stroke 67 | 95 % → 96 % | 772.3 px | 0.16 | 1.01 | 167 |
| stroke 68 | 96 % → 96 % | 924.9 px | 0.17 | 1.00 | 372 |
| stroke 69 | 96 % → 96 % | 1133.6 px | 0.16 | 1.00 | 102 |
| stroke 70 | 99 % → 99 % | 1593.7 px | 0.19 | 1.00 | 84 |
| stroke 71 | 75 % → 97 % | 809.0 px | 0.18 | 1.29 | 285 |
| stroke 72 | 84 % → 98 % | 496.3 px | 0.20 | 1.17 | 360 |
| stroke 73 | 86 % → 98 % | 911.6 px | 0.19 | 1.15 | 237 |
| stroke 74 | 90 % → 99 % | 925.0 px | 0.22 | 1.09 | 373 |
| stroke 75 | 93 % → 98 % | 583.1 px | 0.21 | 1.05 | 106 |
| stroke 76 | 84 % → 97 % | 575.1 px | 0.18 | 1.16 | 218 |
| stroke 77 | 98 % → 98 % | 782.8 px | 0.21 | 1.00 | 261 |
| stroke 78 | 98 % → 98 % | 533.5 px | 0.21 | 1.00 | 198 |
| stroke 79 | 81 % → 97 % | 1517.4 px | 0.18 | 1.20 | 155 |
| stroke 80 | 96 % → 98 % | 1109.0 px | 0.20 | 1.02 | 181 |
| stroke 81 | 97 % → 97 % | 1173.5 px | 0.19 | 1.00 | 98 |
| stroke 82 | 50 % → 96 % | 387.6 px | 0.14 | 1.94 | 761 |
| stroke 83 | 64 % → 97 % | 664.0 px | 0.16 | 1.53 | 545 |
| stroke 84 | 54 % → 96 % | 512.4 px | 0.14 | 1.76 | 390 |
| stroke 85 | 61 % → 94 % | 558.1 px | 0.15 | 1.54 | 187 |
| stroke 86 | 62 % → 97 % | 798.4 px | 0.15 | 1.57 | 481 |
| stroke 87 | 55 % → 95 % | 1355.1 px | 0.13 | 1.74 | 87 |
| stroke 88 | 71 % → 96 % | 1142.0 px | 0.15 | 1.35 | 128 |
| stroke 89 | 59 % → 92 % | 536.1 px | 0.12 | 1.57 | 112 |
| stroke 90 | 75 % → 94 % | 1324.4 px | 0.15 | 1.25 | 90 |
| stroke 91 | 75 % → 95 % | 1613.4 px | 0.15 | 1.28 | 72 |
| stroke 92 | 65 % → 98 % | 1971.9 px | 0.14 | 1.52 | 94 |
| stroke 93 | 67 % → 95 % | 1150.1 px | 0.14 | 1.41 | 253 |
| stroke 94 | 72 % → 94 % | 1129.6 px | 0.15 | 1.32 | 184 |
| stroke 95 | 63 % → 97 % | 784.3 px | 0.15 | 1.54 | 466 |
| stroke 96 | 65 % → 95 % | 867.6 px | 0.14 | 1.48 | 109 |
| stroke 97 | 76 % → 98 % | 335.1 px | 0.13 | 1.28 | 1053 |
| stroke 98 | 73 % → 96 % | 356.0 px | 0.10 | 1.31 | 675 |
| stroke 99 | 92 % → 97 % | 593.7 px | 0.14 | 1.06 | 1034 |
| stroke 100 | 87 % → 96 % | 517.3 px | 0.12 | 1.11 | 944 |
| stroke 101 | 96 % → 100 % | 1039.3 px | 0.11 | 1.03 | 278 |
| stroke 102 | 88 % → 94 % | 444.1 px | 0.08 | 1.06 | 632 |
| stroke 103 | 97 % → 96 % | 1027.9 px | 0.14 | 1.00 | 266 |
| stroke 104 | 95 % → 96 % | 770.8 px | 0.12 | 1.01 | 734 |
| stroke 105 | 96 % → 96 % | 774.6 px | 0.13 | 1.00 | 792 |
| stroke 106 | 97 % → 97 % | 600.8 px | 0.12 | 1.00 | 280 |
| stroke 107 | 100 % → 100 % | 1053.8 px | 0.14 | 1.00 | 719 |
| stroke 108 | 96 % → 96 % | 1230.2 px | 0.09 | 1.00 | 274 |
| stroke 109 | 96 % → 96 % | 1956.6 px | 0.17 | 1.00 | 36 |

Numbers say: wet paint spreads well beyond the stroke.

## Refs v3 · #05 HW green in rust loops — own sheet
own sheet 800 × 1045 · Gouache 1.00 + turpentine 30 % · 104 px · 496.8 s

![Refs v3 · #05 HW green in rust loops — own sheet](Refs-v3-05-HW-green-in-rust-loops-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 11 % → 97 % | 81.5 px | 0.22 | 9.19 | 1709 |
| stroke 2 | 18 % → 94 % | 194.1 px | 0.23 | 5.11 | 2071 |
| stroke 3 | 23 % → 94 % | 268.3 px | 0.29 | 4.11 | 805 |
| stroke 4 | 24 % → 97 % | 200.1 px | 0.29 | 3.98 | 1333 |
| stroke 5 | 29 % → 94 % | 278.0 px | 0.19 | 3.24 | 3774 |
| stroke 6 | 35 % → 90 % | 223.7 px | 0.22 | 2.53 | 1729 |
| stroke 7 | 50 % → 93 % | 686.2 px | 0.08 | 1.84 | 657 |
| stroke 8 | 40 % → 93 % | 472.5 px | 0.22 | 2.33 | 4674 |
| stroke 9 | 44 % → 93 % | 400.1 px | 0.25 | 2.14 | 3769 |
| stroke 10 | 51 % → 99 % | 781.0 px | 0.30 | 1.96 | 467 |
| stroke 11 | 60 % → 99 % | 1074.9 px | 0.20 | 1.65 | 931 |
| stroke 12 | 75 % → 99 % | 1637.2 px | 0.12 | 1.32 | 219 |
| stroke 13 | 42 % → 95 % | 521.5 px | 0.25 | 2.26 | 342 |
| stroke 14 | 63 % → 92 % | 1016.8 px | 0.16 | 1.45 | 518 |
| stroke 15 | 76 % → 99 % | 1540.6 px | 0.14 | 1.30 | 370 |
| stroke 16 | 62 % → 99 % | 1330.9 px | 0.26 | 1.61 | 382 |
| stroke 17 | 54 % → 99 % | 1124.4 px | 0.29 | 1.83 | 302 |
| stroke 18 | 58 % → 96 % | 1115.0 px | 0.20 | 1.65 | 638 |
| stroke 19 | 71 % → 99 % | 1618.4 px | 0.21 | 1.39 | 554 |
| stroke 20 | 80 % → 93 % | 1647.5 px | 0.08 | 1.16 | 339 |
| stroke 21 | 66 % → 88 % | 977.1 px | 0.12 | 1.33 | 212 |
| stroke 22 | 60 % → 93 % | 1253.2 px | 0.21 | 1.56 | 277 |
| stroke 23 | 59 % → 99 % | 931.9 px | 0.24 | 1.66 | 428 |
| stroke 24 | 60 % → 96 % | 929.6 px | 0.20 | 1.59 | 393 |
| stroke 25 | 53 % → 97 % | 852.4 px | 0.28 | 1.83 | 341 |
| stroke 26 | 88 % → 99 % | 2072.5 px | 0.11 | 1.12 | 264 |
| stroke 27 | 51 % → 96 % | 996.6 px | 0.27 | 1.89 | 285 |
| stroke 28 | 68 % → 96 % | 1459.1 px | 0.17 | 1.40 | 221 |
| stroke 29 | 22 % → 83 % | 263.3 px | 0.46 | 3.74 | 119 |
| stroke 30 | 18 % → 80 % | 290.5 px | 0.49 | 4.42 | 103 |
| stroke 31 | 4 % → 89 % | 62.3 px | 0.59 | 22.46 | 117 |
| stroke 32 | 7 % → 89 % | 125.6 px | 0.57 | 13.62 | 84 |
| stroke 33 | 11 % → 89 % | 161.8 px | 0.55 | 8.28 | 150 |
| stroke 34 | 23 % → 92 % | 788.0 px | 0.52 | 4.04 | 73 |
| stroke 35 | 29 % → 91 % | 563.3 px | 0.49 | 3.08 | 141 |
| stroke 36 | 33 % → 91 % | 803.4 px | 0.47 | 2.75 | 162 |
| stroke 37 | 30 % → 92 % | 394.4 px | 0.47 | 3.06 | 243 |
| stroke 38 | 53 % → 97 % | 554.7 px | 0.37 | 1.82 | 394 |
| stroke 39 | 42 % → 95 % | 806.6 px | 0.45 | 2.27 | 270 |
| stroke 40 | 40 % → 91 % | 1105.1 px | 0.49 | 2.26 | 128 |
| stroke 41 | 48 % → 96 % | 1058.6 px | 0.42 | 2.01 | 150 |
| stroke 42 | 54 % → 97 % | 1026.9 px | 0.39 | 1.79 | 211 |
| stroke 43 | 48 % → 96 % | 585.1 px | 0.43 | 1.99 | 642 |
| stroke 44 | 39 % → 90 % | 708.7 px | 0.51 | 2.30 | 134 |
| stroke 45 | 44 % → 91 % | 848.2 px | 0.47 | 2.05 | 175 |
| stroke 46 | 62 % → 97 % | 1258.7 px | 0.36 | 1.58 | 112 |
| stroke 47 | 44 % → 91 % | 1604.3 px | 0.48 | 2.09 | 295 |
| stroke 48 | 37 % → 89 % | 1042.6 px | 0.54 | 2.43 | 131 |
| stroke 49 | 25 % → 83 % | 644.2 px | 0.45 | 3.30 | 72 |
| stroke 50 | 27 % → 84 % | 998.7 px | 0.42 | 3.13 | 26 |
| stroke 51 | 7 % → 76 % | 173.6 px | 0.61 | 11.16 | 35 |
| stroke 52 | 7 % → 77 % | 81.7 px | 0.62 | 10.63 | 267 |
| stroke 53 | 1 % → 79 % | 41.1 px | 0.55 | 58.91 | 25 |
| stroke 54 | 7 % → 79 % | 270.3 px | 0.66 | 11.25 | 31 |
| stroke 55 | 4 % → 80 % | 176.6 px | 0.63 | 20.04 | 29 |
| stroke 56 | 21 % → 79 % | 174.4 px | 0.50 | 3.84 | 327 |
| stroke 57 | 67 % → 88 % | 1446.8 px | 0.14 | 1.33 | 73 |
| stroke 58 | 35 % → 83 % | 426.8 px | 0.40 | 2.38 | 108 |
| stroke 59 | 48 % → 82 % | 465.4 px | 0.32 | 1.71 | 168 |
| stroke 60 | 22 % → 78 % | 450.8 px | 0.60 | 3.54 | 53 |
| stroke 61 | 68 % → 87 % | 671.9 px | 0.19 | 1.28 | 162 |
| stroke 62 | 61 % → 90 % | 1830.1 px | 0.28 | 1.48 | 56 |
| stroke 63 | 53 % → 88 % | 1321.8 px | 0.34 | 1.64 | 46 |
| stroke 64 | 67 % → 89 % | 1181.0 px | 0.23 | 1.33 | 137 |
| stroke 65 | 60 % → 89 % | 1866.2 px | 0.30 | 1.49 | 67 |
| stroke 66 | 72 % → 94 % | 1687.0 px | 0.24 | 1.30 | 110 |
| stroke 67 | 70 % → 93 % | 605.2 px | 0.26 | 1.34 | 193 |
| stroke 68 | 76 % → 95 % | 1620.1 px | 0.29 | 1.24 | 60 |
| stroke 69 | 78 % → 94 % | 2503.2 px | 0.27 | 1.21 | 72 |
| stroke 70 | 78 % → 93 % | 2333.4 px | 0.19 | 1.19 | 85 |
| stroke 71 | 44 % → 84 % | 454.1 px | 0.36 | 1.93 | 223 |
| stroke 72 | 57 % → 94 % | 683.6 px | 0.33 | 1.67 | 132 |
| stroke 73 | 52 % → 86 % | 493.8 px | 0.34 | 1.67 | 138 |
| stroke 74 | 56 % → 95 % | 1549.7 px | 0.35 | 1.70 | 46 |
| stroke 75 | 53 % → 93 % | 1169.9 px | 0.37 | 1.77 | 75 |
| stroke 76 | 34 % → 76 % | 258.8 px | 0.30 | 2.22 | 125 |
| stroke 77 | 39 % → 79 % | 390.0 px | 0.33 | 2.01 | 140 |
| stroke 78 | 54 % → 87 % | 1144.5 px | 0.27 | 1.62 | 57 |
| stroke 79 | 44 % → 80 % | 1319.7 px | 0.31 | 1.81 | 48 |
| stroke 80 | 51 % → 80 % | 1182.3 px | 0.27 | 1.59 | 53 |
| stroke 81 | 33 % → 75 % | 547.1 px | 0.40 | 2.29 | 78 |
| stroke 82 | 42 % → 76 % | 1356.8 px | 0.33 | 1.82 | 57 |
| stroke 83 | 61 % → 88 % | 1243.7 px | 0.24 | 1.43 | 128 |
| stroke 84 | 41 % → 89 % | 614.4 px | 0.59 | 2.19 | 33 |
| stroke 85 | 32 % → 87 % | 921.2 px | 0.62 | 2.77 | 20 |
| stroke 86 | 75 % → 85 % | 2579.8 px | 0.13 | 1.13 | 20 |
| stroke 87 | 78 % → 94 % | 1122.7 px | 0.22 | 1.20 | 88 |
| stroke 88 | 66 % → 94 % | 3103.2 px | 0.28 | 1.43 | 24 |
| stroke 89 | 78 % → 94 % | 1110.2 px | 0.22 | 1.20 | 62 |
| stroke 90 | 74 % → 94 % | 1081.0 px | 0.23 | 1.27 | 54 |
| stroke 91 | 69 % → 95 % | 1280.0 px | 0.27 | 1.36 | 75 |
| stroke 92 | 81 % → 94 % | 2278.5 px | 0.19 | 1.16 | 59 |
| stroke 93 | 76 % → 94 % | 1444.3 px | 0.22 | 1.23 | 60 |
| stroke 94 | 72 % → 94 % | 1007.2 px | 0.25 | 1.31 | 102 |
| stroke 95 | 82 % → 93 % | 4006.3 px | 0.17 | 1.13 | 20 |
| stroke 96 | 67 % → 95 % | 2517.6 px | 0.29 | 1.43 | 36 |
| stroke 97 | 82 % → 92 % | 2722.8 px | 0.18 | 1.12 | 56 |
| stroke 98 | 80 % → 95 % | 4396.8 px | 0.19 | 1.19 | 20 |
| stroke 99 | 62 % → 97 % | 1065.9 px | 0.31 | 1.57 | 125 |
| stroke 100 | 59 % → 99 % | 4561.7 px | 0.33 | 1.70 | 14 |
| stroke 101 | 63 % → 96 % | 2048.0 px | 0.31 | 1.53 | 26 |
| stroke 102 | 51 % → 92 % | 1242.8 px | 0.37 | 1.82 | 49 |
| stroke 103 | 53 % → 98 % | 3458.8 px | 0.38 | 1.84 | 20 |
| stroke 104 | 62 % → 99 % | 4832.6 px | 0.32 | 1.60 | 18 |
| stroke 105 | 56 % → 99 % | 2374.0 px | 0.36 | 1.75 | 35 |
| stroke 106 | 54 % → 98 % | 3083.3 px | 0.38 | 1.83 | 18 |
| stroke 107 | 67 % → 96 % | 2721.9 px | 0.29 | 1.43 | 29 |
| stroke 108 | 56 % → 99 % | 4353.1 px | 0.36 | 1.77 | 9 |
| stroke 109 | 57 % → 99 % | 4423.2 px | 0.36 | 1.75 | 16 |
| stroke 110 | 55 % → 99 % | 4265.9 px | 0.35 | 1.78 | 9 |
| stroke 111 | 36 % → 86 % | 633.9 px | 0.59 | 2.40 | 22 |
| stroke 112 | 62 % → 90 % | 657.0 px | 0.26 | 1.45 | 218 |
| stroke 113 | 62 % → 95 % | 2663.2 px | 0.29 | 1.54 | 103 |
| stroke 114 | 50 % → 86 % | 861.0 px | 0.43 | 1.70 | 225 |
| stroke 115 | 42 % → 89 % | 574.7 px | 0.55 | 2.15 | 1236 |
| stroke 116 | 59 % → 93 % | 1210.2 px | 0.43 | 1.58 | 755 |
| stroke 117 | 59 % → 85 % | 363.7 px | 0.38 | 1.45 | 2637 |
| stroke 118 | 51 % → 80 % | 298.9 px | 0.58 | 1.57 | 1580 |
| stroke 119 | 72 % → 88 % | 732.6 px | 0.35 | 1.22 | 1497 |
| stroke 120 | 69 % → 81 % | 529.7 px | 0.37 | 1.17 | 864 |
| stroke 121 | 66 % → 78 % | 519.4 px | 0.45 | 1.18 | 941 |
| stroke 122 | 76 % → 82 % | 930.5 px | 0.35 | 1.08 | 620 |
| stroke 123 | 73 % → 78 % | 673.0 px | 0.52 | 1.06 | 774 |
| stroke 124 | 77 % → 80 % | 1108.5 px | 0.37 | 1.04 | 584 |
| stroke 125 | 77 % → 80 % | 861.0 px | 0.58 | 1.04 | 463 |
| stroke 126 | 82 % → 83 % | 864.1 px | 0.41 | 1.02 | 784 |
| stroke 127 | 81 % → 82 % | 748.2 px | 0.51 | 1.01 | 682 |
| stroke 128 | 94 % → 94 % | 1764.6 px | 0.40 | 1.00 | 477 |
| stroke 129 | 76 % → 76 % | 979.9 px | 0.54 | 1.00 | 405 |
| stroke 130 | 84 % → 84 % | 1739.0 px | 0.52 | 0.99 | 623 |
| stroke 131 | 90 % → 90 % | 1879.4 px | 0.37 | 0.99 | 517 |
| stroke 132 | 98 % → 98 % | 1784.3 px | 0.34 | 0.99 | 504 |
| stroke 133 | 96 % → 95 % | 1828.7 px | 0.35 | 1.00 | 452 |
| stroke 134 | 33 % → 80 % | 867.7 px | 0.62 | 2.43 | 22 |
| stroke 135 | 56 % → 87 % | 642.1 px | 0.40 | 1.55 | 458 |
| stroke 136 | 71 % → 94 % | 729.1 px | 0.39 | 1.32 | 2763 |
| stroke 137 | 75 % → 97 % | 1509.7 px | 0.40 | 1.30 | 2619 |
| stroke 138 | 66 % → 91 % | 815.2 px | 0.45 | 1.37 | 1907 |
| stroke 139 | 69 % → 90 % | 1212.9 px | 0.44 | 1.30 | 851 |
| stroke 140 | 81 % → 93 % | 783.1 px | 0.36 | 1.15 | 2641 |
| stroke 141 | 75 % → 85 % | 606.8 px | 0.40 | 1.14 | 707 |
| stroke 142 | 78 % → 91 % | 410.3 px | 0.38 | 1.17 | 869 |
| stroke 143 | 67 % → 81 % | 459.2 px | 0.61 | 1.21 | 311 |
| stroke 144 | 81 % → 88 % | 1573.6 px | 0.42 | 1.08 | 197 |
| stroke 145 | 91 % → 94 % | 2225.9 px | 0.31 | 1.03 | 402 |
| stroke 146 | 88 % → 98 % | 2345.7 px | 0.39 | 1.11 | 203 |
| stroke 147 | 88 % → 92 % | 2091.2 px | 0.39 | 1.04 | 148 |
| stroke 148 | 91 % → 92 % | 1702.1 px | 0.32 | 1.01 | 171 |
| stroke 149 | 82 % → 85 % | 1526.2 px | 0.54 | 1.03 | 93 |
| stroke 150 | 94 % → 99 % | 2681.3 px | 0.30 | 1.06 | 198 |
| stroke 151 | 86 % → 93 % | 894.1 px | 0.45 | 1.08 | 475 |
| stroke 152 | 95 % → 97 % | 1120.9 px | 0.31 | 1.02 | 594 |
| stroke 153 | 99 % → 98 % | 2309.7 px | 0.28 | 1.00 | 875 |
| stroke 154 | 79 % → 88 % | 1400.7 px | 0.60 | 1.11 | 549 |
| stroke 155 | 83 % → 89 % | 740.6 px | 0.59 | 1.08 | 400 |
| stroke 156 | 95 % → 97 % | 2238.3 px | 0.29 | 1.01 | 237 |
| stroke 157 | 98 % → 99 % | 2665.0 px | 0.34 | 1.01 | 184 |
| stroke 158 | 81 % → 87 % | 1002.4 px | 0.59 | 1.07 | 229 |
| stroke 159 | 86 % → 86 % | 1151.4 px | 0.42 | 1.00 | 641 |
| stroke 160 | 92 % → 92 % | 486.6 px | 0.39 | 1.00 | 1575 |
| stroke 161 | 91 % → 91 % | 1243.4 px | 0.58 | 1.00 | 415 |
| stroke 162 | 93 % → 93 % | 1865.9 px | 0.45 | 1.00 | 232 |
| stroke 163 | 85 % → 85 % | 1560.8 px | 0.63 | 1.00 | 966 |
| stroke 164 | 98 % → 98 % | 2885.8 px | 0.36 | 1.00 | 313 |
| stroke 165 | 90 % → 89 % | 1719.9 px | 0.63 | 1.00 | 483 |
| stroke 166 | 93 % → 93 % | 2530.0 px | 0.47 | 1.00 | 472 |

Numbers say: wet paint spreads well beyond the stroke.

## Refs v3 · #06 HW scrubbed grey — own sheet
own sheet 800 × 635 · Gouache 1.00 + turpentine 30 % · 93 px · 322.5 s

![Refs v3 · #06 HW scrubbed grey — own sheet](Refs-v3-06-HW-scrubbed-grey-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 14 % → 98 % | 85.2 px | 0.21 | 7.13 | 578 |
| stroke 2 | 12 % → 98 % | 81.6 px | 0.19 | 7.93 | 520 |
| stroke 3 | 25 % → 99 % | 248.2 px | 0.22 | 3.87 | 429 |
| stroke 4 | 37 % → 98 % | 199.6 px | 0.21 | 2.65 | 1034 |
| stroke 5 | 33 % → 98 % | 329.7 px | 0.20 | 2.98 | 381 |
| stroke 6 | 50 % → 97 % | 651.7 px | 0.19 | 1.96 | 243 |
| stroke 7 | 40 % → 97 % | 602.3 px | 0.18 | 2.45 | 371 |
| stroke 8 | 55 % → 99 % | 456.0 px | 0.23 | 1.79 | 503 |
| stroke 9 | 65 % → 99 % | 534.6 px | 0.21 | 1.53 | 745 |
| stroke 10 | 53 % → 97 % | 666.8 px | 0.18 | 1.82 | 404 |
| stroke 11 | 36 % → 99 % | 441.3 px | 0.21 | 2.77 | 419 |
| stroke 12 | 61 % → 98 % | 1013.0 px | 0.21 | 1.60 | 297 |
| stroke 13 | 62 % → 98 % | 773.3 px | 0.23 | 1.60 | 463 |
| stroke 14 | 68 % → 99 % | 714.8 px | 0.23 | 1.46 | 304 |
| stroke 15 | 54 % → 99 % | 999.8 px | 0.20 | 1.83 | 186 |
| stroke 16 | 59 % → 99 % | 700.6 px | 0.22 | 1.68 | 672 |
| stroke 17 | 64 % → 98 % | 759.1 px | 0.22 | 1.54 | 947 |
| stroke 18 | 42 % → 97 % | 372.5 px | 0.20 | 2.34 | 422 |
| stroke 19 | 57 % → 98 % | 728.8 px | 0.21 | 1.74 | 348 |
| stroke 20 | 76 % → 98 % | 816.3 px | 0.23 | 1.30 | 324 |
| stroke 21 | 73 % → 99 % | 927.3 px | 0.22 | 1.35 | 294 |
| stroke 22 | 58 % → 99 % | 1011.0 px | 0.22 | 1.71 | 369 |
| stroke 23 | 40 % → 98 % | 825.9 px | 0.17 | 2.45 | 337 |
| stroke 24 | 68 % → 98 % | 1111.8 px | 0.20 | 1.44 | 342 |
| stroke 25 | 31 % → 99 % | 653.9 px | 0.17 | 3.25 | 105 |
| stroke 26 | 18 % → 97 % | 586.6 px | 0.17 | 5.40 | 26 |
| stroke 27 | 17 % → 95 % | 341.7 px | 0.16 | 5.47 | 19 |
| stroke 28 | 4 % → 94 % | 65.7 px | 0.14 | 21.01 | 9 |
| stroke 29 | 62 % → 98 % | 670.8 px | 0.21 | 1.57 | 626 |
| stroke 30 | 51 % → 99 % | 472.2 px | 0.19 | 1.94 | 807 |
| stroke 31 | 38 % → 98 % | 266.8 px | 0.16 | 2.58 | 1059 |
| stroke 32 | 36 % → 97 % | 315.3 px | 0.15 | 2.68 | 783 |
| stroke 33 | 74 % → 98 % | 782.6 px | 0.21 | 1.34 | 329 |
| stroke 34 | 80 % → 99 % | 984.2 px | 0.21 | 1.23 | 414 |
| stroke 35 | 64 % → 99 % | 1556.8 px | 0.19 | 1.55 | 168 |
| stroke 36 | 77 % → 99 % | 1116.1 px | 0.21 | 1.29 | 536 |
| stroke 37 | 41 % → 94 % | 431.1 px | 0.15 | 2.28 | 126 |
| stroke 38 | 87 % → 99 % | 1979.5 px | 0.23 | 1.13 | 133 |
| stroke 39 | 67 % → 99 % | 872.5 px | 0.19 | 1.49 | 407 |
| stroke 40 | 55 % → 99 % | 961.2 px | 0.16 | 1.80 | 139 |
| stroke 41 | 68 % → 98 % | 1128.4 px | 0.18 | 1.44 | 293 |
| stroke 42 | 48 % → 97 % | 1143.4 px | 0.15 | 2.01 | 147 |
| stroke 43 | 88 % → 99 % | 1594.7 px | 0.23 | 1.12 | 211 |
| stroke 44 | 91 % → 99 % | 2427.9 px | 0.22 | 1.10 | 163 |
| stroke 45 | 55 % → 97 % | 477.8 px | 0.16 | 1.77 | 427 |
| stroke 46 | 50 % → 99 % | 1071.4 px | 0.14 | 1.99 | 166 |
| stroke 47 | 71 % → 99 % | 1932.8 px | 0.18 | 1.39 | 221 |
| stroke 48 | 58 % → 99 % | 1545.8 px | 0.16 | 1.70 | 184 |
| stroke 49 | 65 % → 97 % | 1018.6 px | 0.17 | 1.48 | 253 |
| stroke 50 | 80 % → 98 % | 1815.5 px | 0.21 | 1.23 | 132 |
| stroke 51 | 50 % → 99 % | 1203.0 px | 0.14 | 1.99 | 78 |
| stroke 52 | 77 % → 98 % | 1677.6 px | 0.21 | 1.26 | 144 |
| stroke 53 | 74 % → 98 % | 826.4 px | 0.20 | 1.32 | 374 |
| stroke 54 | 62 % → 96 % | 553.8 px | 0.18 | 1.56 | 375 |
| stroke 55 | 79 % → 98 % | 796.3 px | 0.20 | 1.24 | 357 |
| stroke 56 | 51 % → 95 % | 540.8 px | 0.15 | 1.87 | 113 |
| stroke 57 | 66 % → 96 % | 900.7 px | 0.18 | 1.46 | 236 |
| stroke 58 | 75 % → 97 % | 2196.0 px | 0.20 | 1.30 | 24 |
| stroke 59 | 58 % → 97 % | 1347.4 px | 0.17 | 1.66 | 35 |
| stroke 60 | 81 % → 97 % | 424.7 px | 0.19 | 1.19 | 190 |
| stroke 61 | 91 % → 99 % | 1475.8 px | 0.21 | 1.08 | 110 |
| stroke 62 | 93 % → 98 % | 446.0 px | 0.20 | 1.05 | 466 |
| stroke 63 | 92 % → 96 % | 924.3 px | 0.19 | 1.05 | 178 |
| stroke 64 | 96 % → 98 % | 925.0 px | 0.20 | 1.03 | 612 |
| stroke 65 | 92 % → 96 % | 1328.7 px | 0.18 | 1.04 | 100 |
| stroke 66 | 94 % → 97 % | 1494.8 px | 0.19 | 1.03 | 93 |
| stroke 67 | 95 % → 96 % | 771.2 px | 0.15 | 1.01 | 88 |
| stroke 68 | 96 % → 96 % | 923.9 px | 0.17 | 1.00 | 88 |
| stroke 69 | 96 % → 96 % | 1132.4 px | 0.16 | 1.00 | 56 |
| stroke 70 | 98 % → 99 % | 1593.2 px | 0.19 | 1.00 | 56 |
| stroke 71 | 75 % → 97 % | 809.4 px | 0.18 | 1.29 | 193 |
| stroke 72 | 84 % → 98 % | 496.4 px | 0.21 | 1.17 | 322 |
| stroke 73 | 86 % → 98 % | 912.1 px | 0.19 | 1.15 | 305 |
| stroke 74 | 90 % → 99 % | 925.3 px | 0.22 | 1.09 | 268 |
| stroke 75 | 93 % → 98 % | 583.4 px | 0.21 | 1.05 | 98 |
| stroke 76 | 84 % → 97 % | 575.3 px | 0.18 | 1.16 | 318 |
| stroke 77 | 98 % → 98 % | 782.8 px | 0.21 | 1.00 | 108 |
| stroke 78 | 98 % → 98 % | 533.5 px | 0.21 | 1.00 | 155 |
| stroke 79 | 81 % → 97 % | 1517.8 px | 0.18 | 1.20 | 87 |
| stroke 80 | 96 % → 98 % | 1108.9 px | 0.21 | 1.02 | 178 |
| stroke 81 | 97 % → 97 % | 1173.5 px | 0.19 | 1.00 | 151 |
| stroke 82 | 50 % → 96 % | 387.2 px | 0.14 | 1.94 | 407 |
| stroke 83 | 64 % → 97 % | 663.5 px | 0.16 | 1.53 | 325 |
| stroke 84 | 54 % → 96 % | 512.4 px | 0.14 | 1.76 | 376 |
| stroke 85 | 61 % → 94 % | 557.7 px | 0.15 | 1.54 | 203 |
| stroke 86 | 62 % → 98 % | 797.9 px | 0.15 | 1.57 | 298 |
| stroke 87 | 55 % → 95 % | 1353.9 px | 0.13 | 1.74 | 70 |
| stroke 88 | 71 % → 96 % | 1141.2 px | 0.15 | 1.35 | 98 |
| stroke 89 | 59 % → 92 % | 535.7 px | 0.12 | 1.57 | 111 |
| stroke 90 | 75 % → 94 % | 1324.0 px | 0.15 | 1.25 | 69 |
| stroke 91 | 75 % → 95 % | 1612.8 px | 0.15 | 1.28 | 77 |
| stroke 92 | 65 % → 98 % | 1971.5 px | 0.14 | 1.52 | 79 |
| stroke 93 | 67 % → 95 % | 1149.8 px | 0.14 | 1.41 | 174 |
| stroke 94 | 72 % → 94 % | 1129.4 px | 0.15 | 1.32 | 235 |
| stroke 95 | 62 % → 96 % | 783.9 px | 0.15 | 1.54 | 237 |
| stroke 96 | 64 % → 95 % | 867.5 px | 0.14 | 1.48 | 115 |
| stroke 97 | 76 % → 98 % | 335.2 px | 0.13 | 1.28 | 3166 |
| stroke 98 | 73 % → 96 % | 355.9 px | 0.10 | 1.31 | 1322 |
| stroke 99 | 92 % → 97 % | 593.9 px | 0.14 | 1.06 | 2264 |
| stroke 100 | 87 % → 96 % | 517.8 px | 0.12 | 1.10 | 1300 |
| stroke 101 | 97 % → 100 % | 1040.0 px | 0.11 | 1.03 | 331 |
| stroke 102 | 88 % → 94 % | 444.0 px | 0.08 | 1.06 | 800 |
| stroke 103 | 97 % → 96 % | 1027.9 px | 0.14 | 1.00 | 367 |
| stroke 104 | 95 % → 96 % | 770.7 px | 0.12 | 1.01 | 624 |
| stroke 105 | 96 % → 96 % | 774.5 px | 0.13 | 1.00 | 807 |
| stroke 106 | 97 % → 96 % | 600.7 px | 0.12 | 1.00 | 375 |
| stroke 107 | 100 % → 100 % | 1053.9 px | 0.14 | 1.00 | 979 |
| stroke 108 | 96 % → 96 % | 1229.7 px | 0.09 | 1.00 | 535 |
| stroke 109 | 96 % → 96 % | 1955.3 px | 0.17 | 1.00 | 31 |

Numbers say: wet paint spreads well beyond the stroke.

## Refs v3 · #07 HW blue L and zigzag — own sheet
own sheet 800 × 1065 · Gouache 1.00 + turpentine 30 % · 104 px · 362.9 s

![Refs v3 · #07 HW blue L and zigzag — own sheet](Refs-v3-07-HW-blue-L-and-zigzag-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 13 % → 90 % | 93.2 px | 0.24 | 7.15 | 901 |
| stroke 2 | 31 % → 80 % | 123.4 px | 0.26 | 2.60 | 996 |
| stroke 3 | 36 % → 85 % | 409.4 px | 0.25 | 2.32 | 461 |
| stroke 4 | 61 % → 99 % | 662.6 px | 0.15 | 1.63 | 437 |
| stroke 5 | 20 % → 86 % | 160.1 px | 0.32 | 4.37 | 1241 |
| stroke 6 | 65 % → 99 % | 516.3 px | 0.13 | 1.53 | 432 |
| stroke 7 | 32 % → 87 % | 246.7 px | 0.23 | 2.71 | 642 |
| stroke 8 | 74 % → 99 % | 909.3 px | 0.15 | 1.34 | 290 |
| stroke 9 | 42 % → 88 % | 275.6 px | 0.20 | 2.09 | 1344 |
| stroke 10 | 38 % → 84 % | 446.9 px | 0.28 | 2.20 | 768 |
| stroke 11 | 76 % → 98 % | 937.4 px | 0.12 | 1.29 | 231 |
| stroke 12 | 59 % → 90 % | 696.5 px | 0.20 | 1.54 | 320 |
| stroke 13 | 66 % → 94 % | 1102.7 px | 0.22 | 1.41 | 387 |
| stroke 14 | 73 % → 96 % | 1075.1 px | 0.20 | 1.32 | 1061 |
| stroke 15 | 62 % → 91 % | 704.5 px | 0.24 | 1.48 | 926 |
| stroke 16 | 58 % → 87 % | 771.1 px | 0.18 | 1.51 | 327 |
| stroke 17 | 41 % → 72 % | 412.7 px | 0.30 | 1.75 | 937 |
| stroke 18 | 66 % → 91 % | 885.0 px | 0.17 | 1.38 | 264 |
| stroke 19 | 67 % → 90 % | 589.3 px | 0.18 | 1.34 | 373 |
| stroke 20 | 64 % → 86 % | 688.0 px | 0.22 | 1.34 | 296 |
| stroke 21 | 53 % → 85 % | 845.7 px | 0.25 | 1.62 | 283 |
| stroke 22 | 88 % → 100 % | 966.1 px | 0.12 | 1.13 | 461 |
| stroke 23 | 49 % → 84 % | 1635.5 px | 0.22 | 1.70 | 11 |
| stroke 24 | 23 % → 64 % | 161.3 px | 0.36 | 2.85 | 1280 |
| stroke 25 | 24 % → 63 % | 270.0 px | 0.39 | 2.66 | 556 |
| stroke 26 | 25 % → 42 % | 217.3 px | 0.36 | 1.70 | 451 |
| stroke 27 | 35 % → 58 % | 393.6 px | 0.36 | 1.66 | 580 |
| stroke 28 | 37 % → 65 % | 613.4 px | 0.37 | 1.78 | 325 |
| stroke 29 | 35 % → 62 % | 548.8 px | 0.38 | 1.76 | 459 |
| stroke 30 | 48 % → 73 % | 684.2 px | 0.29 | 1.53 | 343 |
| stroke 31 | 67 % → 88 % | 685.7 px | 0.21 | 1.30 | 433 |
| stroke 32 | 66 % → 87 % | 675.7 px | 0.23 | 1.33 | 378 |
| stroke 33 | 65 % → 85 % | 816.9 px | 0.23 | 1.30 | 275 |
| stroke 34 | 68 % → 84 % | 1246.1 px | 0.20 | 1.23 | 230 |
| stroke 35 | 70 % → 88 % | 678.6 px | 0.21 | 1.25 | 313 |
| stroke 36 | 69 % → 85 % | 1147.4 px | 0.19 | 1.23 | 143 |
| stroke 37 | 64 % → 82 % | 1387.3 px | 0.21 | 1.27 | 104 |
| stroke 38 | 58 % → 84 % | 834.6 px | 0.28 | 1.46 | 366 |
| stroke 39 | 64 % → 86 % | 913.6 px | 0.25 | 1.34 | 251 |
| stroke 40 | 66 % → 89 % | 1327.3 px | 0.25 | 1.35 | 182 |
| stroke 41 | 55 % → 83 % | 1898.8 px | 0.30 | 1.51 | 62 |
| stroke 42 | 51 % → 81 % | 1532.9 px | 0.33 | 1.60 | 115 |
| stroke 43 | 55 % → 86 % | 2086.8 px | 0.32 | 1.56 | 87 |
| stroke 44 | 62 % → 87 % | 2306.6 px | 0.28 | 1.42 | 120 |
| stroke 45 | 59 % → 81 % | 2203.6 px | 0.27 | 1.38 | 69 |
| stroke 46 | 2 % → 43 % | 38.2 px | 0.58 | 24.13 | 84 |
| stroke 47 | 3 % → 41 % | 81.9 px | 0.57 | 13.14 | 57 |
| stroke 48 | 4 % → 46 % | 146.6 px | 0.57 | 13.04 | 58 |
| stroke 49 | 8 % → 64 % | 75.4 px | 0.59 | 8.03 | 308 |
| stroke 50 | 12 % → 78 % | 194.2 px | 0.61 | 6.52 | 31 |
| stroke 51 | 12 % → 75 % | 197.4 px | 0.60 | 6.11 | 81 |
| stroke 52 | 14 % → 82 % | 442.8 px | 0.59 | 5.92 | 20 |
| stroke 53 | 14 % → 67 % | 456.4 px | 0.57 | 4.83 | 23 |
| stroke 54 | 9 % → 44 % | 127.7 px | 0.61 | 4.78 | 134 |
| stroke 55 | 11 % → 46 % | 157.6 px | 0.61 | 4.25 | 94 |
| stroke 56 | 11 % → 48 % | 375.0 px | 0.61 | 4.23 | 33 |
| stroke 57 | 14 % → 49 % | 359.4 px | 0.61 | 3.56 | 67 |
| stroke 58 | 16 % → 38 % | 545.7 px | 0.57 | 2.41 | 83 |
| stroke 59 | 15 % → 37 % | 290.5 px | 0.59 | 2.45 | 101 |
| stroke 60 | 17 % → 49 % | 863.2 px | 0.60 | 2.78 | 37 |
| stroke 61 | 19 % → 51 % | 892.5 px | 0.60 | 2.75 | 78 |
| stroke 62 | 25 % → 51 % | 189.1 px | 0.60 | 2.03 | 501 |
| stroke 63 | 42 % → 69 % | 524.8 px | 0.39 | 1.66 | 379 |
| stroke 64 | 26 % → 49 % | 331.4 px | 0.63 | 1.90 | 206 |
| stroke 65 | 52 % → 66 % | 633.9 px | 0.39 | 1.27 | 410 |
| stroke 66 | 55 % → 74 % | 1600.1 px | 0.38 | 1.35 | 157 |
| stroke 67 | 31 % → 43 % | 337.0 px | 0.61 | 1.36 | 388 |
| stroke 68 | 39 % → 52 % | 462.9 px | 0.60 | 1.34 | 261 |
| stroke 69 | 58 % → 78 % | 1871.9 px | 0.37 | 1.34 | 142 |
| stroke 70 | 53 % → 64 % | 781.7 px | 0.60 | 1.21 | 168 |
| stroke 71 | 52 % → 62 % | 536.7 px | 0.60 | 1.21 | 246 |
| stroke 72 | 49 % → 66 % | 721.5 px | 0.38 | 1.35 | 328 |
| stroke 73 | 53 % → 62 % | 457.9 px | 0.60 | 1.18 | 380 |
| stroke 74 | 59 % → 71 % | 1463.7 px | 0.42 | 1.21 | 115 |
| stroke 75 | 58 % → 71 % | 889.2 px | 0.32 | 1.23 | 207 |
| stroke 76 | 51 % → 56 % | 1144.8 px | 0.57 | 1.10 | 143 |
| stroke 77 | 47 % → 50 % | 731.2 px | 0.62 | 1.06 | 218 |
| stroke 78 | 52 % → 55 % | 900.8 px | 0.61 | 1.04 | 268 |
| stroke 79 | 34 % → 35 % | 333.6 px | 0.58 | 1.02 | 536 |
| stroke 80 | 53 % → 55 % | 964.4 px | 0.57 | 1.04 | 699 |
| stroke 81 | 72 % → 77 % | 1428.9 px | 0.31 | 1.07 | 726 |
| stroke 82 | 44 % → 45 % | 537.4 px | 0.59 | 1.02 | 366 |
| stroke 83 | 37 % → 38 % | 1185.2 px | 0.57 | 1.02 | 224 |
| stroke 84 | 65 % → 69 % | 1076.8 px | 0.38 | 1.06 | 697 |
| stroke 85 | 44 % → 57 % | 1321.0 px | 0.50 | 1.31 | 193 |
| stroke 86 | 44 % → 45 % | 1093.7 px | 0.59 | 1.02 | 307 |
| stroke 87 | 71 % → 77 % | 2585.7 px | 0.37 | 1.08 | 120 |
| stroke 88 | 45 % → 58 % | 1527.2 px | 0.49 | 1.29 | 140 |
| stroke 89 | 54 % → 66 % | 1295.7 px | 0.36 | 1.21 | 160 |
| stroke 90 | 62 % → 63 % | 1781.3 px | 0.60 | 1.01 | 119 |
| stroke 91 | 64 % → 64 % | 1153.7 px | 0.60 | 1.00 | 122 |
| stroke 92 | 55 % → 55 % | 1460.6 px | 0.60 | 1.01 | 97 |
| stroke 93 | 60 % → 61 % | 1245.1 px | 0.58 | 1.00 | 97 |
| stroke 94 | 48 % → 48 % | 745.7 px | 0.62 | 1.00 | 310 |
| stroke 95 | 74 % → 78 % | 2849.3 px | 0.36 | 1.05 | 185 |
| stroke 96 | 33 % → 48 % | 351.0 px | 0.41 | 1.46 | 446 |
| stroke 97 | 42 % → 55 % | 477.9 px | 0.42 | 1.33 | 612 |
| stroke 98 | 35 % → 42 % | 472.2 px | 0.37 | 1.20 | 128 |
| stroke 99 | 63 % → 71 % | 1046.6 px | 0.32 | 1.14 | 379 |
| stroke 100 | 73 % → 77 % | 1026.2 px | 0.27 | 1.07 | 384 |
| stroke 101 | 30 % → 33 % | 417.9 px | 0.38 | 1.11 | 575 |
| stroke 102 | 80 % → 84 % | 1565.2 px | 0.27 | 1.06 | 526 |
| stroke 103 | 62 % → 67 % | 1089.2 px | 0.35 | 1.08 | 420 |
| stroke 104 | 35 % → 37 % | 506.8 px | 0.36 | 1.05 | 333 |
| stroke 105 | 35 % → 36 % | 522.7 px | 0.36 | 1.02 | 250 |
| stroke 106 | 69 % → 72 % | 1043.3 px | 0.30 | 1.04 | 221 |
| stroke 107 | 75 % → 76 % | 1175.6 px | 0.28 | 1.01 | 257 |
| stroke 108 | 81 % → 82 % | 3081.7 px | 0.28 | 1.01 | 182 |
| stroke 109 | 29 % → 29 % | 721.9 px | 0.45 | 0.99 | 453 |
| stroke 110 | 61 % → 61 % | 1075.4 px | 0.40 | 1.01 | 672 |
| stroke 111 | 72 % → 72 % | 2255.7 px | 0.32 | 1.00 | 266 |
| stroke 112 | 38 % → 38 % | 929.8 px | 0.40 | 1.00 | 223 |
| stroke 113 | 79 % → 80 % | 3075.5 px | 0.29 | 1.00 | 162 |
| stroke 114 | 62 % → 62 % | 1580.7 px | 0.46 | 1.00 | 949 |
| stroke 115 | 71 % → 74 % | 4065.0 px | 0.41 | 1.04 | 61 |
| stroke 116 | 85 % → 87 % | 1189.3 px | 0.24 | 1.03 | 782 |
| stroke 117 | 86 % → 89 % | 968.4 px | 0.24 | 1.03 | 477 |
| stroke 118 | 88 % → 91 % | 1109.8 px | 0.22 | 1.03 | 228 |
| stroke 119 | 96 % → 96 % | 1088.3 px | 0.19 | 1.00 | 538 |
| stroke 120 | 98 % → 99 % | 1231.0 px | 0.16 | 1.00 | 217 |
| stroke 121 | 93 % → 93 % | 1098.1 px | 0.22 | 1.00 | 391 |
| stroke 122 | 89 % → 91 % | 720.3 px | 0.17 | 1.03 | 490 |
| stroke 123 | 95 % → 97 % | 1252.8 px | 0.13 | 1.02 | 196 |
| stroke 124 | 95 % → 97 % | 1070.1 px | 0.13 | 1.01 | 82 |
| stroke 125 | 96 % → 96 % | 1045.1 px | 0.13 | 1.00 | 59 |
| stroke 126 | 78 % → 78 % | 1626.5 px | 0.26 | 1.00 | 43 |
| stroke 127 | 99 % → 99 % | 536.2 px | 0.13 | 1.00 | 84 |

Numbers say: wet paint spreads well beyond the stroke.

## Refs v3 · #08 HW lilac crown basket — own sheet
own sheet 800 × 1150 · Gouache 1.00 + turpentine 30 % · 36 px · 746.4 s

![Refs v3 · #08 HW lilac crown basket — own sheet](Refs-v3-08-HW-lilac-crown-basket-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 17 % → 88 % | 35.1 px | 0.12 | 5.16 | 194 |
| stroke 2 | 28 % → 78 % | 92.3 px | 0.11 | 2.80 | 32 |
| stroke 3 | 25 % → 95 % | 69.9 px | 0.14 | 3.73 | 121 |
| stroke 4 | 22 % → 96 % | 51.2 px | 0.25 | 4.33 | 63 |
| stroke 5 | 38 % → 94 % | 99.5 px | 0.12 | 2.50 | 45 |
| stroke 6 | 30 % → 84 % | 83.6 px | 0.13 | 2.84 | 85 |
| stroke 7 | 39 % → 96 % | 187.6 px | 0.13 | 2.42 | 22 |
| stroke 8 | 52 % → 96 % | 289.8 px | 0.12 | 1.83 | 12 |
| stroke 9 | 35 % → 78 % | 109.1 px | 0.12 | 2.23 | 38 |
| stroke 10 | 10 % → 73 % | 34.3 px | 0.11 | 6.99 | 70 |
| stroke 11 | 18 % → 88 % | 131.3 px | 0.08 | 4.96 | 28 |
| stroke 12 | 21 % → 82 % | 108.3 px | 0.07 | 3.86 | 39 |
| stroke 13 | 27 % → 78 % | 97.0 px | 0.12 | 2.87 | 78 |
| stroke 14 | 25 % → 94 % | 142.9 px | 0.09 | 3.75 | 45 |
| stroke 15 | 37 % → 90 % | 177.9 px | 0.09 | 2.42 | 55 |
| stroke 16 | 41 % → 77 % | 340.0 px | 0.11 | 1.86 | 49 |
| stroke 17 | 31 % → 92 % | 169.9 px | 0.09 | 2.99 | 124 |
| stroke 18 | 46 % → 79 % | 355.3 px | 0.08 | 1.71 | 51 |
| stroke 19 | 32 % → 95 % | 239.2 px | 0.09 | 2.96 | 42 |
| stroke 20 | 26 % → 97 % | 187.3 px | 0.14 | 3.77 | 33 |
| stroke 21 | 35 % → 96 % | 315.0 px | 0.11 | 2.72 | 21 |
| stroke 22 | 43 % → 92 % | 268.3 px | 0.07 | 2.16 | 18 |
| stroke 23 | 51 % → 80 % | 442.7 px | 0.07 | 1.57 | 18 |
| stroke 24 | 37 % → 63 % | 324.6 px | 0.11 | 1.70 | 20 |
| stroke 25 | 51 % → 96 % | 481.3 px | 0.10 | 1.87 | 22 |
| stroke 26 | 7 % → 32 % | 36.9 px | 0.15 | 4.25 | 18 |
| stroke 27 | 9 % → 33 % | 50.8 px | 0.18 | 3.74 | 21 |
| stroke 28 | 13 % → 28 % | 79.9 px | 0.16 | 2.21 | 18 |
| stroke 29 | 13 % → 90 % | 34.7 px | 0.18 | 6.93 | 86 |
| stroke 30 | 12 % → 58 % | 46.6 px | 0.19 | 4.74 | 145 |
| stroke 31 | 30 % → 86 % | 64.1 px | 0.17 | 2.88 | 580 |
| stroke 32 | 12 % → 77 % | 32.0 px | 0.20 | 6.24 | 107 |
| stroke 33 | 38 % → 94 % | 100.5 px | 0.17 | 2.46 | 148 |
| stroke 34 | 39 % → 92 % | 94.1 px | 0.19 | 2.36 | 153 |
| stroke 35 | 41 % → 92 % | 180.9 px | 0.18 | 2.28 | 60 |
| stroke 36 | 33 % → 70 % | 223.9 px | 0.15 | 2.11 | 63 |
| stroke 37 | 9 % → 96 % | 35.1 px | 0.30 | 10.42 | 223 |
| stroke 38 | 17 % → 100 % | 58.0 px | 0.26 | 5.90 | 102 |
| stroke 39 | 24 % → 99 % | 73.3 px | 0.29 | 4.08 | 110 |
| stroke 40 | 23 % → 100 % | 107.1 px | 0.33 | 4.41 | 47 |
| stroke 41 | 29 % → 100 % | 100.9 px | 0.32 | 3.49 | 87 |
| stroke 42 | 32 % → 99 % | 106.3 px | 0.25 | 3.10 | 151 |
| stroke 43 | 41 % → 100 % | 271.9 px | 0.24 | 2.46 | 36 |
| stroke 44 | 20 % → 94 % | 112.3 px | 0.29 | 4.82 | 48 |
| stroke 45 | 34 % → 98 % | 161.2 px | 0.25 | 2.86 | 53 |
| stroke 46 | 41 % → 100 % | 304.8 px | 0.26 | 2.43 | 31 |
| stroke 47 | 8 % → 76 % | 35.4 px | 0.17 | 9.41 | 99 |
| stroke 48 | 8 % → 54 % | 36.2 px | 0.15 | 7.04 | 79 |
| stroke 49 | 17 % → 63 % | 124.2 px | 0.14 | 3.77 | 26 |
| stroke 50 | 17 % → 65 % | 72.1 px | 0.15 | 3.89 | 78 |
| stroke 51 | 19 % → 71 % | 91.2 px | 0.17 | 3.75 | 163 |
| stroke 52 | 19 % → 48 % | 88.3 px | 0.15 | 2.47 | 75 |
| stroke 53 | 31 % → 69 % | 202.4 px | 0.15 | 2.18 | 54 |
| stroke 54 | 20 % → 81 % | 172.6 px | 0.18 | 4.13 | 23 |
| stroke 55 | 34 % → 67 % | 345.5 px | 0.15 | 1.94 | 31 |
| stroke 56 | 10 % → 65 % | 35.1 px | 0.03 | 6.83 | 75 |
| stroke 57 | 24 % → 95 % | 64.9 px | 0.04 | 3.88 | 153 |
| stroke 58 | 8 % → 56 % | 58.6 px | 0.03 | 7.10 | 153 |
| stroke 59 | 21 % → 57 % | 76.4 px | 0.04 | 2.68 | 70 |
| stroke 60 | 33 % → 71 % | 95.5 px | 0.03 | 2.14 | 168 |
| stroke 61 | 49 % → 79 % | 116.7 px | 0.03 | 1.63 | 188 |
| stroke 62 | 35 % → 73 % | 170.2 px | 0.03 | 2.12 | 70 |
| stroke 63 | 36 % → 50 % | 175.6 px | 0.03 | 1.41 | 41 |
| stroke 64 | 39 % → 57 % | 159.3 px | 0.03 | 1.49 | 78 |
| stroke 65 | 34 % → 49 % | 227.2 px | 0.04 | 1.46 | 32 |
| stroke 66 | 59 % → 68 % | 183.2 px | 0.03 | 1.16 | 99 |
| stroke 67 | 30 % → 84 % | 170.1 px | 0.06 | 2.81 | 179 |
| stroke 68 | 49 % → 75 % | 458.2 px | 0.03 | 1.53 | 21 |
| stroke 69 | 59 % → 75 % | 251.3 px | 0.03 | 1.28 | 106 |
| stroke 70 | 42 % → 47 % | 197.3 px | 0.04 | 1.12 | 162 |
| stroke 71 | 54 % → 82 % | 311.9 px | 0.03 | 1.51 | 60 |
| stroke 72 | 87 % → 94 % | 255.9 px | 0.03 | 1.09 | 69 |
| stroke 73 | 55 % → 64 % | 219.6 px | 0.03 | 1.18 | 92 |
| stroke 74 | 77 % → 88 % | 270.8 px | 0.03 | 1.13 | 73 |
| stroke 75 | 59 % → 76 % | 319.9 px | 0.03 | 1.30 | 62 |
| stroke 76 | 55 % → 82 % | 318.3 px | 0.03 | 1.49 | 43 |
| stroke 77 | 50 % → 83 % | 337.7 px | 0.04 | 1.65 | 47 |
| stroke 78 | 75 % → 78 % | 432.9 px | 0.03 | 1.05 | 31 |
| stroke 79 | 34 % → 84 % | 289.3 px | 0.08 | 2.49 | 20 |
| stroke 80 | 66 % → 72 % | 468.0 px | 0.03 | 1.09 | 32 |
| stroke 81 | 73 % → 77 % | 491.3 px | 0.03 | 1.06 | 39 |
| stroke 82 | 49 % → 84 % | 414.8 px | 0.05 | 1.72 | 36 |
| stroke 83 | 5 % → 11 % | 38.3 px | 0.03 | 2.24 | 16 |
| stroke 84 | 11 % → 11 % | 89.7 px | 0.02 | 1.09 | 11 |
| stroke 85 | 18 % → 36 % | 36.7 px | 0.03 | 1.99 | 58 |
| stroke 86 | 23 % → 34 % | 52.1 px | 0.03 | 1.52 | 72 |
| stroke 87 | 33 % → 40 % | 75.3 px | 0.03 | 1.21 | 66 |
| stroke 88 | 30 % → 33 % | 187.4 px | 0.03 | 1.08 | 23 |
| stroke 89 | 5 % → 49 % | 15.7 px | 0.23 | 8.98 | 31 |
| stroke 90 | 7 % → 57 % | 19.2 px | 0.07 | 8.77 | 8 |
| stroke 91 | 7 % → 47 % | 35.6 px | 0.14 | 6.93 | 16 |
| stroke 92 | 9 % → 70 % | 52.7 px | 0.11 | 7.71 | 16 |
| stroke 93 | 4 % → 72 % | 20.3 px | 0.16 | 16.63 | 30 |
| stroke 94 | 4 % → 94 % | 23.9 px | 0.26 | 25.58 | 21 |
| stroke 95 | 7 % → 93 % | 65.6 px | 0.26 | 12.70 | 18 |
| stroke 96 | 4 % → 92 % | 18.1 px | 0.26 | 21.46 | 34 |
| stroke 97 | 20 % → 90 % | 84.4 px | 0.22 | 4.45 | 62 |
| stroke 98 | 37 % → 68 % | 108.6 px | 0.11 | 1.83 | 173 |
| stroke 99 | 7 % → 89 % | 29.9 px | 0.42 | 12.06 | 85 |
| stroke 100 | 6 % → 90 % | 33.0 px | 0.34 | 15.08 | 31 |
| stroke 101 | 6 % → 97 % | 34.6 px | 0.28 | 15.86 | 32 |
| stroke 102 | 10 % → 76 % | 77.3 px | 0.23 | 7.32 | 22 |
| stroke 103 | 33 % → 36 % | 117.9 px | 0.06 | 1.09 | 47 |
| stroke 104 | 15 % → 70 % | 83.0 px | 0.14 | 4.79 | 34 |
| stroke 105 | 25 % → 82 % | 134.6 px | 0.14 | 3.32 | 27 |
| stroke 106 | 42 % → 68 % | 219.0 px | 0.09 | 1.61 | 49 |
| stroke 107 | 28 % → 74 % | 96.2 px | 0.15 | 2.62 | 63 |
| stroke 108 | 49 % → 89 % | 531.5 px | 0.14 | 1.82 | 15 |
| stroke 109 | 31 % → 97 % | 125.4 px | 0.17 | 3.17 | 91 |
| stroke 110 | 48 % → 82 % | 206.5 px | 0.12 | 1.71 | 36 |
| stroke 111 | 24 % → 98 % | 92.0 px | 0.24 | 4.15 | 95 |
| stroke 112 | 50 % → 80 % | 245.1 px | 0.13 | 1.60 | 51 |
| stroke 113 | 63 % → 93 % | 242.9 px | 0.13 | 1.48 | 79 |
| stroke 114 | 57 % → 98 % | 318.5 px | 0.12 | 1.73 | 41 |
| stroke 115 | 59 % → 97 % | 556.1 px | 0.12 | 1.64 | 12 |
| stroke 116 | 50 % → 95 % | 342.9 px | 0.12 | 1.89 | 21 |
| stroke 117 | 74 % → 95 % | 311.2 px | 0.12 | 1.28 | 64 |
| stroke 118 | 31 % → 97 % | 283.2 px | 0.26 | 3.18 | 34 |
| stroke 119 | 68 % → 97 % | 642.1 px | 0.12 | 1.43 | 18 |
| stroke 120 | 71 % → 98 % | 810.8 px | 0.10 | 1.38 | 24 |
| stroke 121 | 50 % → 97 % | 431.7 px | 0.17 | 1.94 | 18 |
| stroke 122 | 78 % → 97 % | 645.0 px | 0.12 | 1.23 | 16 |
| stroke 123 | 58 % → 100 % | 563.1 px | 0.17 | 1.73 | 29 |
| stroke 124 | 42 % → 75 % | 280.6 px | 0.12 | 1.79 | 19 |
| stroke 125 | 39 % → 97 % | 390.8 px | 0.20 | 2.48 | 24 |
| stroke 126 | 80 % → 97 % | 649.6 px | 0.11 | 1.22 | 32 |
| stroke 127 | 10 % → 84 % | 60.9 px | 0.12 | 8.20 | 71 |
| stroke 128 | 14 % → 76 % | 105.1 px | 0.13 | 5.32 | 30 |
| stroke 129 | 16 % → 89 % | 179.6 px | 0.12 | 5.46 | 9 |
| stroke 130 | 18 % → 80 % | 175.7 px | 0.13 | 4.56 | 33 |
| stroke 131 | 19 % → 83 % | 215.2 px | 0.13 | 4.48 | 24 |
| stroke 132 | 40 % → 82 % | 146.0 px | 0.17 | 2.04 | 101 |
| stroke 133 | 24 % → 70 % | 108.7 px | 0.18 | 2.99 | 66 |
| stroke 134 | 29 % → 64 % | 133.8 px | 0.18 | 2.17 | 70 |
| stroke 135 | 16 % → 80 % | 186.6 px | 0.17 | 4.90 | 13 |
| stroke 136 | 43 % → 78 % | 278.8 px | 0.19 | 1.84 | 47 |
| stroke 137 | 48 % → 76 % | 354.2 px | 0.18 | 1.58 | 25 |
| stroke 138 | 51 % → 89 % | 220.1 px | 0.19 | 1.73 | 42 |
| stroke 139 | 27 % → 70 % | 307.5 px | 0.16 | 2.60 | 12 |
| stroke 140 | 47 % → 65 % | 480.2 px | 0.17 | 1.39 | 9 |
| stroke 141 | 35 % → 97 % | 148.7 px | 0.22 | 2.78 | 29 |
| stroke 142 | 35 % → 97 % | 181.2 px | 0.26 | 2.77 | 25 |
| stroke 143 | 47 % → 96 % | 320.3 px | 0.18 | 2.06 | 16 |
| stroke 144 | 17 % → 94 % | 76.1 px | 0.23 | 5.43 | 45 |
| stroke 145 | 36 % → 95 % | 390.3 px | 0.22 | 2.65 | 12 |
| stroke 146 | 25 % → 95 % | 202.1 px | 0.23 | 3.88 | 38 |
| stroke 147 | 23 % → 95 % | 253.8 px | 0.20 | 4.06 | 18 |
| stroke 148 | 16 % → 99 % | 145.7 px | 0.20 | 6.27 | 37 |
| stroke 149 | 39 % → 94 % | 428.7 px | 0.23 | 2.40 | 14 |
| stroke 150 | 19 % → 57 % | 79.9 px | 0.24 | 3.05 | 160 |
| stroke 151 | 31 % → 78 % | 131.4 px | 0.16 | 2.49 | 213 |
| stroke 152 | 24 % → 62 % | 102.9 px | 0.23 | 2.60 | 217 |
| stroke 153 | 34 % → 71 % | 138.3 px | 0.17 | 2.09 | 138 |
| stroke 154 | 37 % → 64 % | 205.6 px | 0.17 | 1.71 | 60 |
| stroke 155 | 34 % → 84 % | 128.1 px | 0.25 | 2.47 | 122 |
| stroke 156 | 34 % → 86 % | 153.2 px | 0.26 | 2.51 | 150 |
| stroke 157 | 40 % → 79 % | 168.4 px | 0.18 | 1.97 | 103 |
| stroke 158 | 43 % → 92 % | 470.0 px | 0.18 | 2.11 | 13 |
| stroke 159 | 36 % → 84 % | 123.1 px | 0.19 | 2.33 | 127 |
| stroke 160 | 28 % → 94 % | 72.0 px | 0.32 | 3.30 | 202 |
| stroke 161 | 31 % → 98 % | 97.7 px | 0.35 | 3.18 | 55 |
| stroke 162 | 26 % → 49 % | 186.4 px | 0.22 | 1.89 | 18 |
| stroke 163 | 42 % → 77 % | 367.1 px | 0.21 | 1.85 | 22 |
| stroke 164 | 43 % → 96 % | 131.2 px | 0.30 | 2.24 | 49 |
| stroke 165 | 48 % → 85 % | 521.9 px | 0.17 | 1.79 | 17 |
| stroke 166 | 45 % → 74 % | 313.3 px | 0.16 | 1.64 | 33 |
| stroke 167 | 43 % → 84 % | 169.2 px | 0.23 | 1.95 | 87 |
| stroke 168 | 47 % → 84 % | 296.5 px | 0.20 | 1.79 | 30 |
| stroke 169 | 47 % → 86 % | 336.9 px | 0.22 | 1.82 | 23 |
| stroke 170 | 40 % → 85 % | 221.9 px | 0.20 | 2.15 | 39 |
| stroke 171 | 42 % → 96 % | 181.4 px | 0.31 | 2.29 | 34 |
| stroke 172 | 45 % → 77 % | 298.1 px | 0.18 | 1.71 | 72 |
| stroke 173 | 49 % → 92 % | 339.1 px | 0.23 | 1.87 | 22 |
| stroke 174 | 38 % → 93 % | 183.1 px | 0.31 | 2.42 | 26 |
| stroke 175 | 44 % → 74 % | 476.0 px | 0.16 | 1.68 | 26 |
| stroke 176 | 41 % → 78 % | 234.1 px | 0.19 | 1.88 | 53 |
| stroke 177 | 52 % → 84 % | 493.4 px | 0.16 | 1.62 | 27 |
| stroke 178 | 45 % → 90 % | 208.2 px | 0.20 | 2.00 | 67 |
| stroke 179 | 45 % → 91 % | 352.9 px | 0.28 | 2.03 | 72 |
| stroke 180 | 50 % → 89 % | 345.5 px | 0.19 | 1.76 | 39 |
| stroke 181 | 49 % → 86 % | 338.0 px | 0.18 | 1.74 | 48 |
| stroke 182 | 41 % → 97 % | 174.6 px | 0.33 | 2.40 | 82 |
| stroke 183 | 44 % → 98 % | 193.5 px | 0.32 | 2.23 | 96 |
| stroke 184 | 46 % → 70 % | 241.9 px | 0.18 | 1.53 | 148 |
| stroke 185 | 49 % → 73 % | 396.6 px | 0.17 | 1.50 | 51 |
| stroke 186 | 42 % → 50 % | 304.4 px | 0.17 | 1.20 | 60 |
| stroke 187 | 50 % → 81 % | 310.5 px | 0.18 | 1.63 | 58 |
| stroke 188 | 40 % → 60 % | 323.5 px | 0.20 | 1.47 | 61 |
| stroke 189 | 53 % → 80 % | 526.7 px | 0.17 | 1.49 | 20 |
| stroke 190 | 20 % → 89 % | 195.1 px | 0.26 | 4.51 | 12 |
| stroke 191 | 22 % → 90 % | 116.4 px | 0.26 | 4.09 | 70 |
| stroke 192 | 27 % → 86 % | 134.2 px | 0.25 | 3.12 | 77 |
| stroke 193 | 31 % → 59 % | 295.6 px | 0.14 | 1.87 | 15 |
| stroke 194 | 18 % → 74 % | 107.5 px | 0.10 | 4.20 | 331 |
| stroke 195 | 30 % → 75 % | 321.7 px | 0.07 | 2.51 | 455 |
| stroke 196 | 13 % → 68 % | 88.4 px | 0.18 | 5.28 | 219 |
| stroke 197 | 10 % → 98 % | 56.2 px | 0.21 | 9.34 | 246 |
| stroke 198 | 12 % → 99 % | 51.3 px | 0.33 | 8.45 | 244 |
| stroke 199 | 39 % → 92 % | 155.1 px | 0.21 | 2.39 | 74 |
| stroke 200 | 25 % → 77 % | 101.7 px | 0.29 | 3.09 | 809 |
| stroke 201 | 22 % → 88 % | 127.5 px | 0.35 | 3.92 | 142 |
| stroke 202 | 7 % → 97 % | 40.6 px | 0.40 | 13.95 | 167 |
| stroke 203 | 24 % → 97 % | 153.2 px | 0.31 | 4.03 | 117 |
| stroke 204 | 35 % → 95 % | 292.4 px | 0.32 | 2.74 | 66 |
| stroke 205 | 26 % → 68 % | 105.0 px | 0.16 | 2.61 | 2249 |
| stroke 206 | 35 % → 87 % | 69.6 px | 0.18 | 2.45 | 1946 |
| stroke 207 | 36 % → 67 % | 111.1 px | 0.11 | 1.86 | 2251 |
| stroke 208 | 40 % → 54 % | 113.7 px | 0.09 | 1.34 | 376 |
| stroke 209 | 49 % → 54 % | 177.6 px | 0.09 | 1.09 | 246 |
| stroke 210 | 54 % → 83 % | 288.8 px | 0.15 | 1.54 | 263 |
| stroke 211 | 37 % → 81 % | 143.2 px | 0.21 | 2.16 | 226 |
| stroke 212 | 62 % → 74 % | 193.5 px | 0.09 | 1.18 | 477 |
| stroke 213 | 56 % → 83 % | 191.2 px | 0.15 | 1.49 | 824 |
| stroke 214 | 54 % → 96 % | 212.1 px | 0.17 | 1.79 | 192 |
| stroke 215 | 63 % → 86 % | 205.1 px | 0.13 | 1.37 | 359 |
| stroke 216 | 63 % → 99 % | 202.3 px | 0.14 | 1.56 | 256 |
| stroke 217 | 61 % → 100 % | 314.1 px | 0.19 | 1.64 | 87 |
| stroke 218 | 70 % → 96 % | 293.9 px | 0.14 | 1.38 | 131 |
| stroke 219 | 61 % → 83 % | 259.4 px | 0.14 | 1.37 | 204 |
| stroke 220 | 72 % → 100 % | 276.8 px | 0.17 | 1.40 | 179 |
| stroke 221 | 58 % → 60 % | 187.6 px | 0.10 | 1.02 | 113 |
| stroke 222 | 76 % → 92 % | 360.8 px | 0.13 | 1.21 | 137 |
| stroke 223 | 75 % → 95 % | 377.1 px | 0.15 | 1.26 | 112 |
| stroke 224 | 71 % → 93 % | 260.8 px | 0.17 | 1.31 | 436 |
| stroke 225 | 69 % → 85 % | 271.9 px | 0.11 | 1.25 | 441 |
| stroke 226 | 53 % → 72 % | 227.3 px | 0.16 | 1.36 | 1105 |
| stroke 227 | 69 % → 98 % | 279.9 px | 0.20 | 1.41 | 278 |
| stroke 228 | 73 % → 74 % | 277.6 px | 0.10 | 1.02 | 364 |
| stroke 229 | 60 % → 75 % | 288.7 px | 0.14 | 1.24 | 215 |
| stroke 230 | 57 % → 72 % | 340.6 px | 0.15 | 1.27 | 191 |
| stroke 231 | 83 % → 90 % | 442.8 px | 0.10 | 1.09 | 115 |
| stroke 232 | 41 % → 54 % | 162.9 px | 0.10 | 1.31 | 63 |
| stroke 233 | 51 % → 59 % | 189.9 px | 0.13 | 1.16 | 154 |
| stroke 234 | 68 % → 73 % | 290.4 px | 0.12 | 1.08 | 133 |
| stroke 235 | 75 % → 96 % | 267.7 px | 0.17 | 1.27 | 905 |
| stroke 236 | 72 % → 99 % | 398.4 px | 0.20 | 1.37 | 179 |
| stroke 237 | 84 % → 96 % | 462.5 px | 0.16 | 1.15 | 129 |
| stroke 238 | 70 % → 77 % | 367.1 px | 0.11 | 1.11 | 63 |
| stroke 239 | 66 % → 73 % | 585.3 px | 0.12 | 1.11 | 106 |
| stroke 240 | 77 % → 84 % | 781.3 px | 0.11 | 1.08 | 159 |
| stroke 241 | 72 % → 79 % | 631.0 px | 0.12 | 1.10 | 92 |
| stroke 242 | 86 % → 97 % | 586.6 px | 0.15 | 1.13 | 255 |
| stroke 243 | 73 % → 80 % | 273.5 px | 0.14 | 1.09 | 520 |
| stroke 244 | 82 % → 87 % | 316.1 px | 0.14 | 1.05 | 326 |
| stroke 245 | 81 % → 85 % | 408.5 px | 0.15 | 1.05 | 137 |
| stroke 246 | 53 % → 63 % | 237.8 px | 0.18 | 1.18 | 227 |
| stroke 247 | 59 % → 71 % | 326.9 px | 0.18 | 1.20 | 170 |
| stroke 248 | 46 % → 91 % | 141.0 px | 0.24 | 1.97 | 162 |
| stroke 249 | 48 % → 95 % | 207.8 px | 0.28 | 1.98 | 158 |
| stroke 250 | 65 % → 91 % | 230.9 px | 0.20 | 1.41 | 222 |
| stroke 251 | 49 % → 97 % | 316.0 px | 0.29 | 1.99 | 57 |
| stroke 252 | 45 % → 85 % | 198.0 px | 0.25 | 1.91 | 145 |
| stroke 253 | 20 % → 100 % | 70.1 px | 0.41 | 5.04 | 193 |
| stroke 254 | 59 % → 94 % | 216.2 px | 0.27 | 1.59 | 128 |
| stroke 255 | 64 % → 100 % | 334.0 px | 0.26 | 1.56 | 66 |
| stroke 256 | 27 % → 100 % | 126.0 px | 0.43 | 3.73 | 75 |
| stroke 257 | 50 % → 99 % | 319.8 px | 0.34 | 1.99 | 40 |
| stroke 258 | 66 % → 87 % | 293.9 px | 0.19 | 1.32 | 90 |
| stroke 259 | 45 % → 85 % | 204.0 px | 0.26 | 1.90 | 81 |
| stroke 260 | 52 % → 88 % | 251.4 px | 0.25 | 1.69 | 46 |
| stroke 261 | 72 % → 91 % | 324.3 px | 0.23 | 1.26 | 92 |
| stroke 262 | 80 % → 100 % | 318.6 px | 0.21 | 1.25 | 49 |
| stroke 263 | 54 % → 87 % | 307.6 px | 0.27 | 1.62 | 57 |
| stroke 264 | 83 % → 95 % | 441.4 px | 0.22 | 1.15 | 64 |
| stroke 265 | 66 % → 100 % | 496.5 px | 0.29 | 1.51 | 37 |
| stroke 266 | 56 % → 89 % | 181.2 px | 0.28 | 1.58 | 172 |
| stroke 267 | 67 % → 93 % | 407.0 px | 0.28 | 1.37 | 32 |
| stroke 268 | 80 % → 90 % | 780.3 px | 0.26 | 1.12 | 56 |
| stroke 269 | 79 % → 99 % | 366.2 px | 0.24 | 1.26 | 63 |
| stroke 270 | 77 % → 96 % | 323.2 px | 0.25 | 1.24 | 79 |
| stroke 271 | 78 % → 88 % | 276.0 px | 0.19 | 1.13 | 107 |
| stroke 272 | 71 % → 90 % | 512.6 px | 0.26 | 1.27 | 77 |
| stroke 273 | 85 % → 90 % | 571.1 px | 0.19 | 1.06 | 120 |
| stroke 274 | 61 % → 97 % | 412.0 px | 0.26 | 1.59 | 49 |
| stroke 275 | 73 % → 95 % | 339.2 px | 0.23 | 1.29 | 61 |
| stroke 276 | 56 % → 99 % | 248.4 px | 0.27 | 1.78 | 67 |
| stroke 277 | 54 % → 100 % | 461.3 px | 0.37 | 1.86 | 70 |
| stroke 278 | 89 % → 94 % | 587.3 px | 0.22 | 1.06 | 52 |
| stroke 279 | 75 % → 89 % | 707.2 px | 0.23 | 1.18 | 27 |
| stroke 280 | 89 % → 94 % | 459.1 px | 0.19 | 1.05 | 71 |
| stroke 281 | 89 % → 100 % | 351.6 px | 0.20 | 1.12 | 109 |
| stroke 282 | 88 % → 92 % | 362.9 px | 0.21 | 1.04 | 117 |
| stroke 283 | 93 % → 93 % | 747.6 px | 0.21 | 1.01 | 65 |
| stroke 284 | 93 % → 93 % | 922.6 px | 0.20 | 1.00 | 30 |
| stroke 285 | 46 % → 100 % | 449.7 px | 0.37 | 2.16 | 19 |
| stroke 286 | 59 % → 100 % | 362.9 px | 0.29 | 1.71 | 53 |
| stroke 287 | 48 % → 100 % | 445.4 px | 0.39 | 2.10 | 22 |
| stroke 288 | 50 % → 100 % | 359.0 px | 0.38 | 1.99 | 29 |
| stroke 289 | 75 % → 90 % | 708.5 px | 0.25 | 1.20 | 27 |
| stroke 290 | 44 % → 100 % | 195.6 px | 0.41 | 2.29 | 58 |
| stroke 291 | 93 % → 94 % | 595.4 px | 0.21 | 1.01 | 33 |
| stroke 292 | 91 % → 94 % | 847.1 px | 0.21 | 1.03 | 33 |
| stroke 293 | 70 % → 84 % | 684.8 px | 0.23 | 1.19 | 19 |
| stroke 294 | 79 % → 100 % | 648.7 px | 0.27 | 1.26 | 38 |
| stroke 295 | 30 % → 100 % | 246.8 px | 0.45 | 3.37 | 40 |
| stroke 296 | 85 % → 85 % | 842.9 px | 0.20 | 1.00 | 29 |
| stroke 297 | 89 % → 94 % | 827.6 px | 0.23 | 1.05 | 27 |
| stroke 298 | 94 % → 97 % | 891.0 px | 0.23 | 1.03 | 17 |
| stroke 299 | 85 % → 85 % | 630.4 px | 0.18 | 1.00 | 92 |
| stroke 300 | 75 % → 94 % | 724.5 px | 0.27 | 1.26 | 25 |
| stroke 301 | 49 % → 100 % | 471.1 px | 0.40 | 2.02 | 23 |
| stroke 302 | 68 % → 100 % | 686.5 px | 0.32 | 1.46 | 50 |
| stroke 303 | 17 % → 100 % | 134.9 px | 0.43 | 5.85 | 67 |
| stroke 304 | 17 % → 100 % | 104.6 px | 0.48 | 5.99 | 83 |
| stroke 305 | 21 % → 100 % | 131.3 px | 0.47 | 4.76 | 34 |
| stroke 306 | 23 % → 100 % | 175.2 px | 0.49 | 4.28 | 36 |
| stroke 307 | 30 % → 100 % | 157.7 px | 0.43 | 3.32 | 65 |
| stroke 308 | 39 % → 78 % | 228.5 px | 0.24 | 1.98 | 93 |
| stroke 309 | 43 % → 78 % | 187.8 px | 0.29 | 1.79 | 93 |
| stroke 310 | 50 % → 78 % | 263.6 px | 0.28 | 1.56 | 60 |
| stroke 311 | 57 % → 78 % | 382.6 px | 0.25 | 1.36 | 32 |
| stroke 312 | 70 % → 84 % | 562.9 px | 0.24 | 1.20 | 28 |
| stroke 313 | 39 % → 90 % | 389.4 px | 0.39 | 2.29 | 24 |
| stroke 314 | 58 % → 85 % | 360.6 px | 0.29 | 1.45 | 60 |
| stroke 315 | 61 % → 89 % | 384.3 px | 0.27 | 1.47 | 44 |
| stroke 316 | 68 % → 73 % | 502.7 px | 0.23 | 1.07 | 38 |
| stroke 317 | 63 % → 85 % | 395.0 px | 0.25 | 1.36 | 53 |
| stroke 318 | 72 % → 77 % | 501.8 px | 0.22 | 1.07 | 30 |
| stroke 319 | 63 % → 88 % | 618.1 px | 0.30 | 1.40 | 30 |
| stroke 320 | 54 % → 88 % | 530.1 px | 0.36 | 1.64 | 23 |
| stroke 321 | 56 % → 79 % | 496.7 px | 0.31 | 1.41 | 25 |
| stroke 322 | 18 % → 86 % | 86.4 px | 0.42 | 4.66 | 44 |
| stroke 323 | 32 % → 90 % | 120.4 px | 0.38 | 2.81 | 81 |
| stroke 324 | 29 % → 83 % | 242.8 px | 0.39 | 2.84 | 29 |
| stroke 325 | 48 % → 90 % | 450.1 px | 0.32 | 1.88 | 16 |
| stroke 326 | 30 % → 93 % | 171.8 px | 0.39 | 3.11 | 48 |
| stroke 327 | 55 % → 85 % | 234.9 px | 0.23 | 1.54 | 124 |
| stroke 328 | 28 % → 93 % | 151.5 px | 0.46 | 3.30 | 33 |
| stroke 329 | 63 % → 97 % | 200.9 px | 0.25 | 1.55 | 153 |
| stroke 330 | 35 % → 93 % | 153.8 px | 0.43 | 2.68 | 77 |
| stroke 331 | 60 % → 86 % | 244.7 px | 0.23 | 1.43 | 114 |
| stroke 332 | 66 % → 91 % | 269.0 px | 0.22 | 1.39 | 169 |
| stroke 333 | 72 % → 97 % | 259.5 px | 0.23 | 1.34 | 119 |
| stroke 334 | 37 % → 97 % | 185.9 px | 0.38 | 2.65 | 136 |
| stroke 335 | 59 % → 79 % | 253.7 px | 0.22 | 1.35 | 176 |
| stroke 336 | 51 % → 98 % | 389.2 px | 0.32 | 1.90 | 30 |
| stroke 337 | 68 % → 97 % | 678.1 px | 0.24 | 1.43 | 16 |
| stroke 338 | 68 % → 98 % | 559.7 px | 0.23 | 1.44 | 33 |
| stroke 339 | 71 % → 94 % | 333.4 px | 0.33 | 1.34 | 86 |
| stroke 340 | 45 % → 98 % | 362.3 px | 0.36 | 2.18 | 28 |
| stroke 341 | 74 % → 98 % | 426.0 px | 0.28 | 1.31 | 62 |
| stroke 342 | 68 % → 96 % | 571.4 px | 0.27 | 1.41 | 24 |
| stroke 343 | 62 % → 95 % | 325.7 px | 0.30 | 1.53 | 75 |
| stroke 344 | 76 % → 98 % | 755.2 px | 0.26 | 1.28 | 173 |
| stroke 345 | 66 % → 97 % | 238.5 px | 0.28 | 1.47 | 282 |
| stroke 346 | 82 % → 95 % | 433.8 px | 0.32 | 1.15 | 64 |
| stroke 347 | 81 % → 93 % | 333.7 px | 0.20 | 1.14 | 182 |
| stroke 348 | 81 % → 94 % | 503.1 px | 0.21 | 1.15 | 565 |
| stroke 349 | 39 % → 100 % | 351.8 px | 0.41 | 2.52 | 42 |
| stroke 350 | 71 % → 96 % | 658.5 px | 0.28 | 1.34 | 25 |
| stroke 351 | 77 % → 95 % | 434.9 px | 0.25 | 1.24 | 61 |
| stroke 352 | 80 % → 97 % | 544.5 px | 0.30 | 1.21 | 54 |
| stroke 353 | 78 % → 96 % | 375.5 px | 0.24 | 1.23 | 380 |
| stroke 354 | 76 % → 97 % | 588.7 px | 0.28 | 1.27 | 39 |
| stroke 355 | 78 % → 82 % | 630.7 px | 0.18 | 1.05 | 42 |
| stroke 356 | 75 % → 97 % | 668.5 px | 0.30 | 1.29 | 39 |
| stroke 357 | 79 % → 90 % | 455.4 px | 0.24 | 1.13 | 66 |
| stroke 358 | 71 % → 92 % | 682.0 px | 0.38 | 1.28 | 18 |
| stroke 359 | 81 % → 88 % | 680.8 px | 0.22 | 1.09 | 25 |
| stroke 360 | 87 % → 93 % | 657.3 px | 0.23 | 1.07 | 29 |
| stroke 361 | 57 % → 93 % | 435.4 px | 0.41 | 1.63 | 23 |
| stroke 362 | 73 % → 97 % | 729.7 px | 0.31 | 1.34 | 25 |
| stroke 363 | 87 % → 93 % | 237.9 px | 0.08 | 1.08 | 19 |
| stroke 364 | 35 % → 68 % | 133.7 px | 0.33 | 1.93 | 8 |
| stroke 365 | 56 % → 80 % | 538.0 px | 0.25 | 1.42 | 38 |
| stroke 366 | 69 % → 74 % | 306.0 px | 0.14 | 1.06 | 59 |
| stroke 367 | 77 % → 80 % | 637.9 px | 0.13 | 1.04 | 13 |
| stroke 368 | 60 % → 65 % | 489.0 px | 0.17 | 1.09 | 39 |
| stroke 369 | 89 % → 90 % | 566.1 px | 0.08 | 1.01 | 37 |
| stroke 370 | 68 % → 73 % | 706.3 px | 0.12 | 1.06 | 13 |
| stroke 371 | 91 % → 96 % | 654.8 px | 0.13 | 1.05 | 16 |
| stroke 372 | 60 % → 100 % | 402.4 px | 0.34 | 1.65 | 14 |
| stroke 373 | 35 % → 100 % | 214.0 px | 0.43 | 2.87 | 24 |
| stroke 374 | 30 % → 95 % | 276.8 px | 0.41 | 3.16 | 7 |
| stroke 375 | 68 % → 92 % | 382.3 px | 0.29 | 1.36 | 38 |
| stroke 376 | 41 % → 86 % | 420.9 px | 0.39 | 2.10 | 10 |
| stroke 377 | 75 % → 78 % | 204.8 px | 0.22 | 1.05 | 277 |
| stroke 378 | 63 % → 63 % | 221.0 px | 0.29 | 1.00 | 105 |
| stroke 379 | 69 % → 97 % | 204.1 px | 0.30 | 1.41 | 254 |
| stroke 380 | 63 % → 97 % | 185.0 px | 0.36 | 1.55 | 386 |
| stroke 381 | 75 % → 97 % | 204.9 px | 0.38 | 1.30 | 383 |
| stroke 382 | 65 % → 99 % | 189.3 px | 0.41 | 1.52 | 416 |
| stroke 383 | 73 % → 97 % | 176.0 px | 0.34 | 1.32 | 296 |
| stroke 384 | 77 % → 99 % | 219.1 px | 0.46 | 1.29 | 295 |
| stroke 385 | 58 % → 90 % | 198.3 px | 0.46 | 1.54 | 322 |
| stroke 386 | 88 % → 96 % | 366.3 px | 0.34 | 1.10 | 223 |
| stroke 387 | 94 % → 97 % | 271.2 px | 0.34 | 1.04 | 394 |
| stroke 388 | 91 % → 98 % | 284.6 px | 0.32 | 1.07 | 388 |
| stroke 389 | 84 % → 99 % | 255.2 px | 0.38 | 1.18 | 386 |
| stroke 390 | 84 % → 99 % | 268.7 px | 0.29 | 1.18 | 256 |
| stroke 391 | 65 % → 88 % | 206.7 px | 0.36 | 1.36 | 172 |
| stroke 392 | 74 % → 90 % | 226.6 px | 0.48 | 1.22 | 178 |
| stroke 393 | 87 % → 97 % | 392.1 px | 0.35 | 1.11 | 194 |
| stroke 394 | 84 % → 91 % | 347.4 px | 0.31 | 1.09 | 265 |
| stroke 395 | 96 % → 100 % | 331.4 px | 0.49 | 1.04 | 208 |
| stroke 396 | 96 % → 97 % | 463.6 px | 0.37 | 1.01 | 82 |
| stroke 397 | 96 % → 100 % | 529.9 px | 0.36 | 1.04 | 64 |
| stroke 398 | 96 % → 99 % | 469.2 px | 0.37 | 1.03 | 124 |
| stroke 399 | 81 % → 89 % | 252.0 px | 0.43 | 1.10 | 123 |
| stroke 400 | 96 % → 98 % | 326.3 px | 0.31 | 1.02 | 219 |
| stroke 401 | 98 % → 98 % | 556.2 px | 0.25 | 1.00 | 98 |
| stroke 402 | 98 % → 98 % | 381.5 px | 0.39 | 1.01 | 231 |
| stroke 403 | 100 % → 100 % | 439.5 px | 0.38 | 1.00 | 117 |
| stroke 404 | 100 % → 100 % | 454.8 px | 0.48 | 1.00 | 141 |
| stroke 405 | 99 % → 100 % | 539.9 px | 0.50 | 1.01 | 105 |
| stroke 406 | 80 % → 83 % | 362.3 px | 0.38 | 1.03 | 126 |
| stroke 407 | 91 % → 91 % | 456.7 px | 0.36 | 1.01 | 188 |
| stroke 408 | 97 % → 97 % | 474.2 px | 0.46 | 1.00 | 141 |
| stroke 409 | 94 % → 95 % | 510.4 px | 0.37 | 1.01 | 104 |
| stroke 410 | 100 % → 100 % | 479.6 px | 0.42 | 1.00 | 143 |
| stroke 411 | 91 % → 99 % | 466.2 px | 0.44 | 1.09 | 100 |
| stroke 412 | 82 % → 93 % | 321.4 px | 0.40 | 1.13 | 196 |
| stroke 413 | 88 % → 90 % | 336.0 px | 0.43 | 1.03 | 137 |
| stroke 414 | 100 % → 100 % | 439.5 px | 0.46 | 1.00 | 204 |
| stroke 415 | 85 % → 85 % | 376.1 px | 0.43 | 1.00 | 116 |
| stroke 416 | 93 % → 97 % | 520.2 px | 0.42 | 1.04 | 113 |
| stroke 417 | 99 % → 99 % | 555.4 px | 0.40 | 1.00 | 112 |
| stroke 418 | 100 % → 100 % | 621.8 px | 0.50 | 1.00 | 106 |
| stroke 419 | 100 % → 100 % | 495.7 px | 0.40 | 1.00 | 107 |
| stroke 420 | 99 % → 99 % | 543.6 px | 0.48 | 1.00 | 89 |
| stroke 421 | 85 % → 91 % | 264.9 px | 0.35 | 1.07 | 335 |
| stroke 422 | 87 % → 94 % | 531.9 px | 0.34 | 1.08 | 77 |
| stroke 423 | 87 % → 90 % | 385.6 px | 0.37 | 1.02 | 135 |
| stroke 424 | 95 % → 95 % | 601.1 px | 0.24 | 1.00 | 68 |
| stroke 425 | 85 % → 84 % | 449.1 px | 0.39 | 1.00 | 112 |
| stroke 426 | 76 % → 78 % | 304.6 px | 0.12 | 1.02 | 46 |
| stroke 427 | 94 % → 93 % | 271.3 px | 0.13 | 1.00 | 66 |
| stroke 428 | 64 % → 67 % | 664.2 px | 0.15 | 1.04 | 13 |
| stroke 429 | 73 % → 74 % | 455.8 px | 0.16 | 1.01 | 29 |
| stroke 430 | 61 % → 62 % | 418.5 px | 0.14 | 1.01 | 23 |
| stroke 431 | 87 % → 87 % | 255.2 px | 0.24 | 1.00 | 104 |

Numbers say: wet paint spreads well beyond the stroke.

## Refs v3 · #09 HW white loops — own sheet
own sheet 800 × 640 · Gouache 1.00 + turpentine 30 % · 104 px · 247.1 s

![Refs v3 · #09 HW white loops — own sheet](Refs-v3-09-HW-white-loops-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 14 % → 93 % | 91.4 px | 0.09 | 6.84 | 914 |
| stroke 2 | 29 % → 87 % | 248.0 px | 0.10 | 2.97 | 373 |
| stroke 3 | 24 % → 90 % | 132.3 px | 0.10 | 3.76 | 855 |
| stroke 4 | 22 % → 85 % | 171.1 px | 0.14 | 3.85 | 1573 |
| stroke 5 | 40 % → 95 % | 362.4 px | 0.09 | 2.35 | 1058 |
| stroke 6 | 49 % → 94 % | 354.0 px | 0.11 | 1.91 | 1062 |
| stroke 7 | 41 % → 89 % | 687.3 px | 0.10 | 2.20 | 384 |
| stroke 8 | 45 % → 81 % | 405.5 px | 0.11 | 1.82 | 644 |
| stroke 9 | 57 % → 90 % | 397.6 px | 0.10 | 1.58 | 2045 |
| stroke 10 | 47 % → 87 % | 401.1 px | 0.17 | 1.84 | 878 |
| stroke 11 | 49 % → 86 % | 658.6 px | 0.14 | 1.76 | 445 |
| stroke 12 | 58 % → 89 % | 717.6 px | 0.10 | 1.54 | 697 |
| stroke 13 | 63 % → 90 % | 511.3 px | 0.12 | 1.42 | 2009 |
| stroke 14 | 62 % → 89 % | 755.9 px | 0.15 | 1.42 | 1113 |
| stroke 15 | 72 % → 83 % | 1068.2 px | 0.10 | 1.14 | 381 |
| stroke 16 | 77 % → 94 % | 742.3 px | 0.09 | 1.22 | 838 |
| stroke 17 | 79 % → 87 % | 542.9 px | 0.10 | 1.10 | 748 |
| stroke 18 | 81 % → 94 % | 1232.0 px | 0.09 | 1.17 | 323 |
| stroke 19 | 68 % → 88 % | 1138.1 px | 0.14 | 1.28 | 455 |
| stroke 20 | 65 % → 80 % | 1110.1 px | 0.12 | 1.24 | 357 |
| stroke 21 | 64 % → 89 % | 743.4 px | 0.16 | 1.38 | 540 |
| stroke 22 | 81 % → 93 % | 578.9 px | 0.11 | 1.15 | 811 |
| stroke 23 | 85 % → 97 % | 1443.9 px | 0.10 | 1.14 | 595 |
| stroke 24 | 80 % → 87 % | 947.8 px | 0.10 | 1.09 | 890 |
| stroke 25 | 75 % → 92 % | 1520.4 px | 0.14 | 1.22 | 576 |
| stroke 26 | 70 % → 84 % | 397.9 px | 0.16 | 1.19 | 978 |
| stroke 27 | 86 % → 92 % | 1299.3 px | 0.09 | 1.07 | 287 |
| stroke 28 | 86 % → 91 % | 1287.1 px | 0.10 | 1.05 | 262 |
| stroke 29 | 93 % → 96 % | 1461.4 px | 0.09 | 1.04 | 415 |
| stroke 30 | 90 % → 94 % | 1624.6 px | 0.09 | 1.03 | 385 |
| stroke 31 | 70 % → 83 % | 940.6 px | 0.13 | 1.19 | 514 |
| stroke 32 | 90 % → 93 % | 1315.5 px | 0.11 | 1.03 | 408 |
| stroke 33 | 73 % → 77 % | 1182.7 px | 0.10 | 1.05 | 339 |
| stroke 34 | 83 % → 85 % | 1556.9 px | 0.11 | 1.03 | 470 |
| stroke 35 | 69 % → 86 % | 1111.3 px | 0.18 | 1.24 | 267 |
| stroke 36 | 91 % → 94 % | 1186.0 px | 0.12 | 1.03 | 339 |
| stroke 37 | 81 % → 85 % | 1130.5 px | 0.10 | 1.06 | 418 |
| stroke 38 | 93 % → 94 % | 1421.6 px | 0.10 | 1.01 | 611 |
| stroke 39 | 30 % → 43 % | 424.1 px | 0.08 | 1.40 | 18 |
| stroke 40 | 87 % → 89 % | 1469.3 px | 0.09 | 1.03 | 22 |
| stroke 41 | 88 % → 89 % | 1238.1 px | 0.09 | 1.01 | 42 |
| stroke 42 | 90 % → 90 % | 1602.8 px | 0.09 | 1.00 | 60 |
| stroke 43 | 89 % → 89 % | 2729.2 px | 0.09 | 1.00 | 30 |
| stroke 44 | 91 % → 91 % | 6658.0 px | 0.09 | 1.00 | 21 |
| stroke 45 | 87 % → 87 % | 5333.0 px | 0.09 | 1.00 | 9 |
| stroke 46 | 90 % → 90 % | 2382.9 px | 0.10 | 1.00 | 31 |
| stroke 47 | 88 % → 88 % | 5353.6 px | 0.09 | 0.99 | 11 |
| stroke 48 | 88 % → 87 % | 4840.5 px | 0.10 | 0.99 | 19 |
| stroke 49 | 90 % → 90 % | 3211.2 px | 0.09 | 1.00 | 22 |
| stroke 50 | 68 % → 85 % | 2508.3 px | 0.20 | 1.25 | 31 |
| stroke 51 | 67 % → 84 % | 3169.7 px | 0.20 | 1.25 | 18 |
| stroke 52 | 70 % → 85 % | 2410.6 px | 0.19 | 1.23 | 22 |
| stroke 53 | 81 % → 83 % | 316.6 px | 0.11 | 1.02 | 592 |
| stroke 54 | 76 % → 75 % | 1958.7 px | 0.10 | 0.99 | 46 |
| stroke 55 | 78 % → 80 % | 3151.8 px | 0.12 | 1.03 | 44 |
| stroke 56 | 79 % → 92 % | 2843.2 px | 0.17 | 1.16 | 32 |
| stroke 57 | 80 % → 92 % | 5109.5 px | 0.17 | 1.15 | 14 |
| stroke 58 | 65 % → 79 % | 581.9 px | 0.20 | 1.23 | 39 |
| stroke 59 | 49 % → 70 % | 556.1 px | 0.27 | 1.44 | 39 |
| stroke 60 | 88 % → 92 % | 915.4 px | 0.12 | 1.04 | 245 |
| stroke 61 | 72 % → 84 % | 894.1 px | 0.19 | 1.17 | 151 |
| stroke 62 | 86 % → 89 % | 1075.9 px | 0.13 | 1.03 | 84 |
| stroke 63 | 81 % → 88 % | 1150.7 px | 0.16 | 1.09 | 166 |
| stroke 64 | 74 % → 84 % | 1160.6 px | 0.19 | 1.14 | 260 |
| stroke 65 | 74 % → 85 % | 2389.4 px | 0.20 | 1.15 | 45 |
| stroke 66 | 91 % → 91 % | 2287.6 px | 0.13 | 1.01 | 43 |
| stroke 67 | 94 % → 94 % | 3035.0 px | 0.12 | 1.01 | 52 |
| stroke 68 | 92 % → 92 % | 2349.3 px | 0.13 | 1.00 | 30 |
| stroke 69 | 81 % → 87 % | 2734.1 px | 0.16 | 1.08 | 33 |
| stroke 70 | 69 % → 79 % | 633.3 px | 0.24 | 1.14 | 116 |
| stroke 71 | 74 % → 81 % | 887.5 px | 0.22 | 1.09 | 90 |
| stroke 72 | 81 % → 85 % | 1750.6 px | 0.20 | 1.05 | 54 |
| stroke 73 | 81 % → 83 % | 917.0 px | 0.21 | 1.03 | 117 |
| stroke 74 | 80 % → 82 % | 2075.9 px | 0.21 | 1.03 | 35 |
| stroke 75 | 82 % → 82 % | 842.9 px | 0.19 | 1.01 | 133 |
| stroke 76 | 82 % → 82 % | 843.7 px | 0.18 | 1.00 | 162 |

Numbers say: wet paint spreads well beyond the stroke.

## Refs v3 · #10 HW maroon loops — own sheet
own sheet 800 × 1070 · Gouache 1.00 + turpentine 30 % · 104 px · 319.9 s

![Refs v3 · #10 HW maroon loops — own sheet](Refs-v3-10-HW-maroon-loops-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 8 % → 76 % | 95.0 px | 0.42 | 9.48 | 704 |
| stroke 2 | 15 % → 67 % | 152.2 px | 0.38 | 4.52 | 1014 |
| stroke 3 | 28 % → 77 % | 556.7 px | 0.25 | 2.76 | 297 |
| stroke 4 | 28 % → 48 % | 653.0 px | 0.23 | 1.74 | 255 |
| stroke 5 | 25 % → 89 % | 439.7 px | 0.46 | 3.59 | 630 |
| stroke 6 | 26 % → 56 % | 354.7 px | 0.21 | 2.14 | 943 |
| stroke 7 | 38 % → 80 % | 550.8 px | 0.37 | 2.13 | 635 |
| stroke 8 | 34 % → 68 % | 470.0 px | 0.30 | 2.00 | 722 |
| stroke 9 | 35 % → 76 % | 743.5 px | 0.35 | 2.18 | 375 |
| stroke 10 | 46 % → 78 % | 799.3 px | 0.29 | 1.71 | 1346 |
| stroke 11 | 48 % → 87 % | 1129.6 px | 0.40 | 1.81 | 338 |
| stroke 12 | 39 % → 60 % | 626.9 px | 0.32 | 1.54 | 795 |
| stroke 13 | 46 % → 87 % | 1058.4 px | 0.42 | 1.88 | 502 |
| stroke 14 | 9 % → 88 % | 69.4 px | 0.37 | 9.85 | 265 |
| stroke 15 | 19 % → 94 % | 105.4 px | 0.49 | 4.92 | 722 |
| stroke 16 | 25 % → 94 % | 185.0 px | 0.50 | 3.85 | 492 |
| stroke 17 | 44 % → 92 % | 597.6 px | 0.37 | 2.11 | 174 |
| stroke 18 | 28 % → 94 % | 387.1 px | 0.49 | 3.32 | 277 |
| stroke 19 | 32 % → 96 % | 343.8 px | 0.49 | 3.02 | 310 |
| stroke 20 | 40 % → 90 % | 432.2 px | 0.44 | 2.24 | 436 |
| stroke 21 | 60 % → 90 % | 612.6 px | 0.35 | 1.51 | 111 |
| stroke 22 | 50 % → 94 % | 757.4 px | 0.43 | 1.89 | 158 |
| stroke 23 | 34 % → 77 % | 567.1 px | 0.42 | 2.25 | 154 |
| stroke 24 | 8 % → 71 % | 144.8 px | 0.42 | 9.06 | 119 |
| stroke 25 | 9 % → 81 % | 118.9 px | 0.55 | 9.17 | 374 |
| stroke 26 | 22 % → 68 % | 270.2 px | 0.36 | 3.03 | 122 |
| stroke 27 | 16 % → 82 % | 389.5 px | 0.52 | 5.26 | 328 |
| stroke 28 | 21 % → 76 % | 317.7 px | 0.47 | 3.65 | 317 |
| stroke 29 | 23 % → 83 % | 530.0 px | 0.52 | 3.68 | 510 |
| stroke 30 | 19 % → 82 % | 484.0 px | 0.53 | 4.24 | 331 |
| stroke 31 | 23 % → 91 % | 520.1 px | 0.55 | 3.91 | 225 |
| stroke 32 | 35 % → 71 % | 432.5 px | 0.44 | 2.02 | 109 |
| stroke 33 | 35 % → 78 % | 1794.7 px | 0.45 | 2.23 | 7 |
| stroke 34 | 36 % → 50 % | 411.7 px | 0.20 | 1.39 | 402 |
| stroke 35 | 44 % → 54 % | 390.0 px | 0.21 | 1.24 | 628 |
| stroke 36 | 43 % → 53 % | 670.9 px | 0.20 | 1.22 | 241 |
| stroke 37 | 47 % → 55 % | 907.3 px | 0.21 | 1.18 | 285 |
| stroke 38 | 47 % → 73 % | 547.4 px | 0.37 | 1.56 | 535 |
| stroke 39 | 53 % → 78 % | 870.5 px | 0.41 | 1.48 | 347 |
| stroke 40 | 49 % → 52 % | 624.0 px | 0.20 | 1.06 | 321 |
| stroke 41 | 59 % → 64 % | 1659.0 px | 0.20 | 1.09 | 216 |
| stroke 42 | 47 % → 48 % | 505.9 px | 0.20 | 1.02 | 595 |
| stroke 43 | 49 % → 47 % | 916.9 px | 0.18 | 0.96 | 102 |
| stroke 44 | 51 % → 73 % | 1398.0 px | 0.40 | 1.43 | 141 |
| stroke 45 | 54 % → 76 % | 1465.2 px | 0.40 | 1.42 | 176 |
| stroke 46 | 42 % → 66 % | 555.7 px | 0.40 | 1.60 | 802 |
| stroke 47 | 43 % → 45 % | 818.9 px | 0.26 | 1.06 | 269 |
| stroke 48 | 44 % → 65 % | 931.7 px | 0.40 | 1.50 | 204 |
| stroke 49 | 54 % → 86 % | 440.9 px | 0.45 | 1.58 | 1209 |
| stroke 50 | 55 % → 93 % | 540.1 px | 0.49 | 1.70 | 1141 |
| stroke 51 | 52 % → 89 % | 503.8 px | 0.54 | 1.71 | 799 |
| stroke 52 | 66 % → 86 % | 437.1 px | 0.45 | 1.31 | 638 |
| stroke 53 | 77 % → 91 % | 1166.4 px | 0.48 | 1.18 | 352 |
| stroke 54 | 67 % → 90 % | 1207.5 px | 0.51 | 1.33 | 229 |
| stroke 55 | 81 % → 94 % | 960.2 px | 0.51 | 1.16 | 600 |
| stroke 56 | 69 % → 85 % | 838.8 px | 0.45 | 1.23 | 1852 |
| stroke 57 | 83 % → 93 % | 1235.5 px | 0.49 | 1.12 | 480 |
| stroke 58 | 82 % → 99 % | 1961.5 px | 0.58 | 1.21 | 641 |
| stroke 59 | 80 % → 96 % | 1310.4 px | 0.49 | 1.19 | 579 |
| stroke 60 | 75 % → 95 % | 1109.0 px | 0.59 | 1.27 | 642 |
| stroke 61 | 79 % → 93 % | 1512.4 px | 0.49 | 1.18 | 871 |
| stroke 62 | 87 % → 94 % | 1226.7 px | 0.57 | 1.08 | 610 |
| stroke 63 | 76 % → 94 % | 1385.7 px | 0.50 | 1.23 | 572 |
| stroke 64 | 89 % → 97 % | 876.0 px | 0.51 | 1.08 | 1195 |
| stroke 65 | 93 % → 93 % | 959.0 px | 0.46 | 1.00 | 507 |
| stroke 66 | 87 % → 89 % | 1610.4 px | 0.48 | 1.02 | 336 |
| stroke 67 | 95 % → 98 % | 1456.7 px | 0.52 | 1.03 | 467 |
| stroke 68 | 83 % → 83 % | 1285.9 px | 0.47 | 1.00 | 402 |
| stroke 69 | 93 % → 93 % | 1335.3 px | 0.45 | 1.00 | 418 |
| stroke 70 | 83 % → 94 % | 1675.1 px | 0.60 | 1.14 | 440 |
| stroke 71 | 72 % → 91 % | 1277.2 px | 0.56 | 1.28 | 785 |
| stroke 72 | 61 % → 73 % | 718.2 px | 0.45 | 1.20 | 609 |
| stroke 73 | 69 % → 80 % | 1634.3 px | 0.48 | 1.15 | 393 |
| stroke 74 | 67 % → 75 % | 661.5 px | 0.47 | 1.13 | 1753 |
| stroke 75 | 66 % → 72 % | 1277.1 px | 0.45 | 1.09 | 693 |
| stroke 76 | 78 % → 80 % | 1031.7 px | 0.50 | 1.03 | 904 |
| stroke 77 | 78 % → 79 % | 1271.4 px | 0.50 | 1.01 | 479 |
| stroke 78 | 79 % → 79 % | 1433.5 px | 0.49 | 1.00 | 355 |
| stroke 79 | 76 % → 81 % | 1264.0 px | 0.51 | 1.06 | 513 |
| stroke 80 | 75 % → 76 % | 594.3 px | 0.47 | 1.01 | 4939 |
| stroke 81 | 77 % → 77 % | 1233.8 px | 0.48 | 1.00 | 1580 |
| stroke 82 | 78 % → 78 % | 980.0 px | 0.50 | 1.00 | 2314 |
| stroke 83 | 83 % → 83 % | 1051.3 px | 0.46 | 1.00 | 762 |
| stroke 84 | 95 % → 95 % | 2271.0 px | 0.56 | 1.00 | 923 |
| stroke 85 | 92 % → 91 % | 2180.6 px | 0.39 | 0.99 | 256 |

Numbers say: wet paint spreads well beyond the stroke.

## Refs v3 · #11 HW purple balls — own sheet
own sheet 800 × 985 · Gouache 1.00 + turpentine 30 % · 104 px · 341.9 s

![Refs v3 · #11 HW purple balls — own sheet](Refs-v3-11-HW-purple-balls-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 7 % → 87 % | 95.5 px | 0.31 | 12.04 | 521 |
| stroke 2 | 17 % → 88 % | 140.7 px | 0.16 | 5.23 | 985 |
| stroke 3 | 23 % → 88 % | 258.6 px | 0.21 | 3.78 | 852 |
| stroke 4 | 20 % → 67 % | 194.5 px | 0.04 | 3.31 | 381 |
| stroke 5 | 16 % → 86 % | 84.8 px | 0.04 | 5.37 | 937 |
| stroke 6 | 24 % → 71 % | 251.0 px | 0.04 | 2.91 | 668 |
| stroke 7 | 23 % → 90 % | 186.9 px | 0.05 | 3.89 | 678 |
| stroke 8 | 32 % → 77 % | 265.5 px | 0.04 | 2.45 | 979 |
| stroke 9 | 38 % → 86 % | 293.3 px | 0.04 | 2.28 | 2618 |
| stroke 10 | 52 % → 87 % | 481.4 px | 0.06 | 1.67 | 1292 |
| stroke 11 | 49 % → 92 % | 292.8 px | 0.04 | 1.88 | 2091 |
| stroke 12 | 65 % → 88 % | 355.0 px | 0.04 | 1.36 | 3271 |
| stroke 13 | 58 % → 92 % | 553.4 px | 0.09 | 1.58 | 2065 |
| stroke 14 | 68 % → 98 % | 1569.3 px | 0.09 | 1.45 | 553 |
| stroke 15 | 46 % → 85 % | 459.4 px | 0.22 | 1.84 | 1106 |
| stroke 16 | 53 % → 89 % | 783.0 px | 0.18 | 1.69 | 856 |
| stroke 17 | 71 % → 83 % | 849.8 px | 0.04 | 1.17 | 640 |
| stroke 18 | 70 % → 89 % | 518.3 px | 0.04 | 1.28 | 1214 |
| stroke 19 | 73 % → 89 % | 884.0 px | 0.04 | 1.22 | 3120 |
| stroke 20 | 84 % → 98 % | 1966.3 px | 0.04 | 1.17 | 1840 |
| stroke 21 | 72 % → 81 % | 864.5 px | 0.04 | 1.14 | 6331 |
| stroke 22 | 48 % → 86 % | 608.0 px | 0.25 | 1.78 | 4204 |
| stroke 23 | 71 % → 75 % | 863.3 px | 0.04 | 1.06 | 2768 |
| stroke 24 | 85 % → 95 % | 1118.5 px | 0.04 | 1.12 | 4705 |
| stroke 25 | 85 % → 91 % | 1280.3 px | 0.04 | 1.07 | 2459 |
| stroke 26 | 81 % → 85 % | 711.4 px | 0.04 | 1.06 | 716 |
| stroke 27 | 79 % → 82 % | 1805.0 px | 0.04 | 1.03 | 473 |
| stroke 28 | 88 % → 91 % | 1494.0 px | 0.04 | 1.03 | 725 |
| stroke 29 | 89 % → 96 % | 1809.2 px | 0.05 | 1.09 | 531 |
| stroke 30 | 67 % → 88 % | 1193.7 px | 0.15 | 1.30 | 866 |
| stroke 31 | 71 % → 97 % | 1619.0 px | 0.19 | 1.36 | 600 |
| stroke 32 | 64 % → 78 % | 1049.6 px | 0.13 | 1.22 | 413 |
| stroke 33 | 79 % → 82 % | 1033.0 px | 0.04 | 1.03 | 517 |
| stroke 34 | 86 % → 87 % | 1491.9 px | 0.04 | 1.01 | 318 |
| stroke 35 | 95 % → 97 % | 2299.9 px | 0.04 | 1.02 | 259 |
| stroke 36 | 79 % → 80 % | 801.4 px | 0.04 | 1.02 | 824 |
| stroke 37 | 52 % → 77 % | 513.3 px | 0.26 | 1.49 | 586 |
| stroke 38 | 88 % → 90 % | 1517.3 px | 0.04 | 1.03 | 359 |
| stroke 39 | 42 % → 79 % | 611.5 px | 0.34 | 1.87 | 448 |
| stroke 40 | 76 % → 90 % | 1735.9 px | 0.13 | 1.17 | 595 |
| stroke 41 | 96 % → 98 % | 2265.9 px | 0.05 | 1.02 | 1313 |
| stroke 42 | 94 % → 93 % | 2028.4 px | 0.04 | 0.99 | 458 |
| stroke 43 | 66 % → 79 % | 534.8 px | 0.16 | 1.21 | 2200 |
| stroke 44 | 88 % → 88 % | 2073.6 px | 0.04 | 0.99 | 359 |
| stroke 45 | 53 % → 92 % | 1144.6 px | 0.33 | 1.72 | 278 |
| stroke 46 | 69 % → 96 % | 1099.0 px | 0.24 | 1.39 | 727 |
| stroke 47 | 92 % → 91 % | 1811.7 px | 0.04 | 0.99 | 647 |
| stroke 48 | 80 % → 79 % | 1387.9 px | 0.04 | 0.99 | 413 |
| stroke 49 | 89 % → 88 % | 1705.7 px | 0.06 | 0.99 | 881 |
| stroke 50 | 90 % → 89 % | 1454.9 px | 0.04 | 1.00 | 418 |
| stroke 51 | 70 % → 98 % | 1926.9 px | 0.25 | 1.39 | 54 |
| stroke 52 | 71 % → 99 % | 2942.9 px | 0.25 | 1.39 | 47 |
| stroke 53 | 61 % → 97 % | 3432.5 px | 0.31 | 1.58 | 36 |
| stroke 54 | 65 % → 99 % | 6199.9 px | 0.30 | 1.53 | 14 |
| stroke 55 | 68 % → 96 % | 6479.1 px | 0.27 | 1.42 | 14 |
| stroke 56 | 59 % → 98 % | 4498.8 px | 0.33 | 1.67 | 17 |
| stroke 57 | 68 % → 98 % | 2047.0 px | 0.27 | 1.44 | 237 |
| stroke 58 | 74 % → 98 % | 2696.6 px | 0.23 | 1.31 | 116 |
| stroke 59 | 64 % → 98 % | 6168.9 px | 0.30 | 1.52 | 22 |
| stroke 60 | 82 % → 81 % | 2517.8 px | 0.04 | 0.98 | 33 |
| stroke 61 | 64 % → 76 % | 1257.2 px | 0.16 | 1.18 | 263 |
| stroke 62 | 29 % → 76 % | 981.0 px | 0.46 | 2.66 | 28 |
| stroke 63 | 37 % → 70 % | 1036.1 px | 0.36 | 1.90 | 35 |
| stroke 64 | 20 % → 65 % | 544.3 px | 0.49 | 3.16 | 16 |
| stroke 65 | 4 % → 87 % | 19.0 px | 0.65 | 23.94 | 80 |
| stroke 66 | 10 % → 99 % | 226.9 px | 0.62 | 9.53 | 19 |
| stroke 67 | 54 % → 85 % | 258.0 px | 0.44 | 1.57 | 1594 |
| stroke 68 | 69 % → 92 % | 647.0 px | 0.40 | 1.33 | 1392 |
| stroke 69 | 69 % → 80 % | 325.9 px | 0.49 | 1.16 | 1834 |
| stroke 70 | 83 % → 89 % | 944.3 px | 0.35 | 1.08 | 883 |
| stroke 71 | 76 % → 79 % | 892.7 px | 0.41 | 1.04 | 537 |
| stroke 72 | 72 % → 83 % | 1022.9 px | 0.55 | 1.15 | 298 |
| stroke 73 | 76 % → 78 % | 1205.0 px | 0.38 | 1.03 | 498 |
| stroke 74 | 78 % → 83 % | 1087.3 px | 0.44 | 1.07 | 495 |
| stroke 75 | 91 % → 95 % | 794.5 px | 0.61 | 1.04 | 358 |
| stroke 76 | 96 % → 96 % | 2149.3 px | 0.40 | 1.00 | 302 |
| stroke 77 | 76 % → 76 % | 571.1 px | 0.46 | 1.00 | 587 |
| stroke 78 | 80 % → 80 % | 1159.8 px | 0.52 | 1.00 | 228 |
| stroke 79 | 97 % → 97 % | 1507.8 px | 0.43 | 1.00 | 634 |
| stroke 80 | 85 % → 85 % | 817.8 px | 0.60 | 1.00 | 434 |

Numbers say: wet paint spreads well beyond the stroke.

## Refs v3 · #12 HW black-olive cage — own sheet
own sheet 800 × 1150 · Gouache 1.00 + turpentine 30 % · 36 px · 690.2 s

![Refs v3 · #12 HW black-olive cage — own sheet](Refs-v3-12-HW-black-olive-cage-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 17 % → 88 % | 35.0 px | 0.12 | 5.18 | 543 |
| stroke 2 | 28 % → 78 % | 92.5 px | 0.12 | 2.79 | 75 |
| stroke 3 | 25 % → 95 % | 69.6 px | 0.14 | 3.75 | 99 |
| stroke 4 | 22 % → 96 % | 51.1 px | 0.25 | 4.34 | 71 |
| stroke 5 | 38 % → 94 % | 99.2 px | 0.12 | 2.51 | 74 |
| stroke 6 | 30 % → 84 % | 83.6 px | 0.13 | 2.83 | 349 |
| stroke 7 | 40 % → 96 % | 187.8 px | 0.13 | 2.42 | 43 |
| stroke 8 | 53 % → 96 % | 290.3 px | 0.12 | 1.82 | 35 |
| stroke 9 | 35 % → 78 % | 109.4 px | 0.12 | 2.23 | 115 |
| stroke 10 | 10 % → 73 % | 34.0 px | 0.11 | 7.06 | 165 |
| stroke 11 | 18 % → 88 % | 130.3 px | 0.08 | 5.00 | 45 |
| stroke 12 | 21 % → 82 % | 107.7 px | 0.07 | 3.88 | 65 |
| stroke 13 | 27 % → 78 % | 97.1 px | 0.12 | 2.87 | 130 |
| stroke 14 | 25 % → 94 % | 143.2 px | 0.09 | 3.74 | 57 |
| stroke 15 | 37 % → 90 % | 178.2 px | 0.09 | 2.41 | 92 |
| stroke 16 | 41 % → 77 % | 340.1 px | 0.11 | 1.85 | 28 |
| stroke 17 | 31 % → 92 % | 169.9 px | 0.09 | 2.99 | 124 |
| stroke 18 | 46 % → 79 % | 355.1 px | 0.08 | 1.71 | 78 |
| stroke 19 | 32 % → 94 % | 239.5 px | 0.09 | 2.96 | 41 |
| stroke 20 | 26 % → 97 % | 187.0 px | 0.14 | 3.77 | 31 |
| stroke 21 | 35 % → 96 % | 314.8 px | 0.10 | 2.71 | 63 |
| stroke 22 | 43 % → 92 % | 268.3 px | 0.07 | 2.16 | 75 |
| stroke 23 | 51 % → 80 % | 442.9 px | 0.07 | 1.57 | 33 |
| stroke 24 | 37 % → 63 % | 324.8 px | 0.11 | 1.70 | 24 |
| stroke 25 | 51 % → 96 % | 481.1 px | 0.10 | 1.87 | 30 |
| stroke 26 | 7 % → 32 % | 36.7 px | 0.14 | 4.28 | 31 |
| stroke 27 | 9 % → 33 % | 51.0 px | 0.18 | 3.74 | 39 |
| stroke 28 | 13 % → 28 % | 79.9 px | 0.17 | 2.22 | 27 |
| stroke 29 | 13 % → 91 % | 34.8 px | 0.19 | 6.92 | 122 |
| stroke 30 | 12 % → 58 % | 46.4 px | 0.18 | 4.75 | 91 |
| stroke 31 | 30 % → 86 % | 64.2 px | 0.18 | 2.88 | 177 |
| stroke 32 | 13 % → 77 % | 32.4 px | 0.19 | 6.17 | 82 |
| stroke 33 | 38 % → 94 % | 101.1 px | 0.18 | 2.45 | 91 |
| stroke 34 | 39 % → 92 % | 94.3 px | 0.19 | 2.36 | 161 |
| stroke 35 | 41 % → 92 % | 181.1 px | 0.19 | 2.28 | 691 |
| stroke 36 | 33 % → 70 % | 223.7 px | 0.15 | 2.11 | 85 |
| stroke 37 | 9 % → 96 % | 34.9 px | 0.29 | 10.46 | 229 |
| stroke 38 | 17 % → 100 % | 58.3 px | 0.26 | 5.87 | 905 |
| stroke 39 | 24 % → 99 % | 73.8 px | 0.29 | 4.06 | 487 |
| stroke 40 | 23 % → 100 % | 107.8 px | 0.34 | 4.38 | 180 |
| stroke 41 | 29 % → 100 % | 101.5 px | 0.33 | 3.47 | 486 |
| stroke 42 | 32 % → 99 % | 106.9 px | 0.25 | 3.08 | 707 |
| stroke 43 | 41 % → 100 % | 272.9 px | 0.24 | 2.45 | 259 |
| stroke 44 | 19 % → 94 % | 112.1 px | 0.28 | 4.83 | 244 |
| stroke 45 | 34 % → 98 % | 161.4 px | 0.25 | 2.86 | 300 |
| stroke 46 | 41 % → 100 % | 305.7 px | 0.27 | 2.42 | 134 |
| stroke 47 | 8 % → 76 % | 35.4 px | 0.18 | 9.40 | 139 |
| stroke 48 | 8 % → 54 % | 35.9 px | 0.15 | 7.11 | 303 |
| stroke 49 | 17 % → 63 % | 124.0 px | 0.15 | 3.78 | 260 |
| stroke 50 | 17 % → 65 % | 71.7 px | 0.15 | 3.91 | 218 |
| stroke 51 | 19 % → 71 % | 91.4 px | 0.18 | 3.74 | 499 |
| stroke 52 | 19 % → 48 % | 88.2 px | 0.15 | 2.48 | 949 |
| stroke 53 | 31 % → 69 % | 202.5 px | 0.15 | 2.18 | 436 |
| stroke 54 | 20 % → 80 % | 173.2 px | 0.20 | 4.10 | 216 |
| stroke 55 | 34 % → 67 % | 345.8 px | 0.15 | 1.94 | 80 |
| stroke 56 | 10 % → 65 % | 35.0 px | 0.03 | 6.84 | 149 |
| stroke 57 | 24 % → 95 % | 65.0 px | 0.04 | 3.88 | 183 |
| stroke 58 | 8 % → 56 % | 58.8 px | 0.03 | 7.09 | 209 |
| stroke 59 | 22 % → 58 % | 77.0 px | 0.04 | 2.66 | 266 |
| stroke 60 | 33 % → 71 % | 95.7 px | 0.03 | 2.13 | 421 |
| stroke 61 | 49 % → 79 % | 116.8 px | 0.03 | 1.63 | 187 |
| stroke 62 | 35 % → 73 % | 170.2 px | 0.03 | 2.13 | 100 |
| stroke 63 | 36 % → 50 % | 175.5 px | 0.03 | 1.41 | 45 |
| stroke 64 | 39 % → 57 % | 159.3 px | 0.03 | 1.49 | 104 |
| stroke 65 | 34 % → 49 % | 227.6 px | 0.04 | 1.46 | 58 |
| stroke 66 | 59 % → 68 % | 183.2 px | 0.03 | 1.16 | 164 |
| stroke 67 | 30 % → 84 % | 170.4 px | 0.06 | 2.81 | 63 |
| stroke 68 | 49 % → 75 % | 459.1 px | 0.03 | 1.53 | 23 |
| stroke 69 | 59 % → 75 % | 251.5 px | 0.03 | 1.27 | 151 |
| stroke 70 | 42 % → 48 % | 197.4 px | 0.04 | 1.12 | 80 |
| stroke 71 | 54 % → 81 % | 312.7 px | 0.03 | 1.51 | 50 |
| stroke 72 | 87 % → 94 % | 256.0 px | 0.03 | 1.09 | 210 |
| stroke 73 | 55 % → 65 % | 219.5 px | 0.03 | 1.18 | 214 |
| stroke 74 | 78 % → 88 % | 270.9 px | 0.03 | 1.13 | 139 |
| stroke 75 | 59 % → 76 % | 320.2 px | 0.03 | 1.29 | 122 |
| stroke 76 | 55 % → 82 % | 317.9 px | 0.03 | 1.49 | 132 |
| stroke 77 | 50 % → 83 % | 337.5 px | 0.04 | 1.65 | 38 |
| stroke 78 | 75 % → 78 % | 432.8 px | 0.03 | 1.05 | 43 |
| stroke 79 | 34 % → 84 % | 289.1 px | 0.08 | 2.49 | 24 |
| stroke 80 | 66 % → 72 % | 468.1 px | 0.03 | 1.09 | 22 |
| stroke 81 | 73 % → 78 % | 491.0 px | 0.03 | 1.06 | 33 |
| stroke 82 | 49 % → 84 % | 414.4 px | 0.05 | 1.72 | 17 |
| stroke 83 | 5 % → 11 % | 39.2 px | 0.03 | 2.20 | 11 |
| stroke 84 | 11 % → 11 % | 90.1 px | 0.02 | 1.08 | 18 |
| stroke 85 | 18 % → 36 % | 36.6 px | 0.03 | 1.98 | 56 |
| stroke 86 | 23 % → 34 % | 52.2 px | 0.03 | 1.50 | 70 |
| stroke 87 | 33 % → 40 % | 75.4 px | 0.03 | 1.20 | 61 |
| stroke 88 | 30 % → 33 % | 187.6 px | 0.03 | 1.07 | 22 |
| stroke 89 | 6 % → 49 % | 15.9 px | 0.23 | 8.92 | 31 |
| stroke 90 | 7 % → 57 % | 19.4 px | 0.08 | 8.65 | 5 |
| stroke 91 | 7 % → 47 % | 35.8 px | 0.14 | 6.89 | 13 |
| stroke 92 | 9 % → 70 % | 51.9 px | 0.09 | 7.84 | 4 |
| stroke 93 | 4 % → 72 % | 20.2 px | 0.16 | 16.69 | 25 |
| stroke 94 | 4 % → 94 % | 23.5 px | 0.25 | 25.96 | 23 |
| stroke 95 | 7 % → 93 % | 64.6 px | 0.25 | 12.87 | 8 |
| stroke 96 | 4 % → 92 % | 17.0 px | 0.28 | 22.76 | 7 |
| stroke 97 | 20 % → 90 % | 83.2 px | 0.24 | 4.49 | 30 |
| stroke 98 | 37 % → 68 % | 108.1 px | 0.11 | 1.83 | 27 |
| stroke 99 | 7 % → 88 % | 29.9 px | 0.43 | 12.04 | 41 |
| stroke 100 | 6 % → 90 % | 33.2 px | 0.35 | 14.99 | 31 |
| stroke 101 | 6 % → 97 % | 35.1 px | 0.29 | 15.64 | 49 |
| stroke 102 | 10 % → 76 % | 78.1 px | 0.23 | 7.25 | 70 |
| stroke 103 | 33 % → 36 % | 117.0 px | 0.06 | 1.09 | 80 |
| stroke 104 | 15 % → 69 % | 83.0 px | 0.14 | 4.78 | 55 |
| stroke 105 | 25 % → 82 % | 134.5 px | 0.14 | 3.31 | 48 |
| stroke 106 | 42 % → 68 % | 218.6 px | 0.09 | 1.61 | 128 |
| stroke 107 | 28 % → 74 % | 95.9 px | 0.14 | 2.63 | 198 |
| stroke 108 | 49 % → 89 % | 531.6 px | 0.14 | 1.82 | 34 |
| stroke 109 | 31 % → 97 % | 125.2 px | 0.18 | 3.17 | 472 |
| stroke 110 | 48 % → 82 % | 206.5 px | 0.12 | 1.71 | 87 |
| stroke 111 | 24 % → 98 % | 92.0 px | 0.24 | 4.16 | 104 |
| stroke 112 | 50 % → 80 % | 245.1 px | 0.13 | 1.60 | 59 |
| stroke 113 | 63 % → 93 % | 242.6 px | 0.13 | 1.48 | 102 |
| stroke 114 | 57 % → 98 % | 318.2 px | 0.12 | 1.73 | 76 |
| stroke 115 | 59 % → 97 % | 555.1 px | 0.12 | 1.65 | 15 |
| stroke 116 | 50 % → 95 % | 342.7 px | 0.12 | 1.89 | 38 |
| stroke 117 | 74 % → 95 % | 311.1 px | 0.12 | 1.28 | 48 |
| stroke 118 | 31 % → 97 % | 283.6 px | 0.27 | 3.17 | 25 |
| stroke 119 | 68 % → 97 % | 641.2 px | 0.12 | 1.43 | 13 |
| stroke 120 | 71 % → 98 % | 809.1 px | 0.10 | 1.38 | 19 |
| stroke 121 | 50 % → 97 % | 431.9 px | 0.17 | 1.94 | 25 |
| stroke 122 | 78 % → 97 % | 645.5 px | 0.12 | 1.23 | 31 |
| stroke 123 | 57 % → 100 % | 563.0 px | 0.17 | 1.73 | 12 |
| stroke 124 | 42 % → 75 % | 280.6 px | 0.12 | 1.79 | 34 |
| stroke 125 | 39 % → 97 % | 391.0 px | 0.20 | 2.48 | 50 |
| stroke 126 | 80 % → 97 % | 649.8 px | 0.11 | 1.21 | 56 |
| stroke 127 | 10 % → 84 % | 61.2 px | 0.12 | 8.15 | 67 |
| stroke 128 | 14 % → 76 % | 105.5 px | 0.13 | 5.29 | 42 |
| stroke 129 | 16 % → 89 % | 180.2 px | 0.12 | 5.44 | 24 |
| stroke 130 | 18 % → 80 % | 175.9 px | 0.13 | 4.55 | 19 |
| stroke 131 | 19 % → 83 % | 216.3 px | 0.13 | 4.45 | 13 |
| stroke 132 | 40 % → 82 % | 145.9 px | 0.17 | 2.05 | 164 |
| stroke 133 | 24 % → 70 % | 108.7 px | 0.17 | 2.99 | 78 |
| stroke 134 | 29 % → 63 % | 133.9 px | 0.18 | 2.17 | 202 |
| stroke 135 | 16 % → 79 % | 187.1 px | 0.16 | 4.88 | 85 |
| stroke 136 | 42 % → 78 % | 278.0 px | 0.18 | 1.84 | 90 |
| stroke 137 | 48 % → 76 % | 353.5 px | 0.18 | 1.58 | 64 |
| stroke 138 | 51 % → 89 % | 220.1 px | 0.19 | 1.73 | 413 |
| stroke 139 | 27 % → 70 % | 306.1 px | 0.16 | 2.61 | 24 |
| stroke 140 | 47 % → 65 % | 480.0 px | 0.16 | 1.39 | 32 |
| stroke 141 | 35 % → 97 % | 149.2 px | 0.23 | 2.78 | 166 |
| stroke 142 | 35 % → 97 % | 181.3 px | 0.26 | 2.77 | 38 |
| stroke 143 | 47 % → 96 % | 321.5 px | 0.18 | 2.05 | 28 |
| stroke 144 | 17 % → 94 % | 75.7 px | 0.23 | 5.46 | 59 |
| stroke 145 | 36 % → 95 % | 387.8 px | 0.22 | 2.66 | 12 |
| stroke 146 | 24 % → 95 % | 200.9 px | 0.23 | 3.90 | 27 |
| stroke 147 | 23 % → 95 % | 252.6 px | 0.19 | 4.08 | 29 |
| stroke 148 | 16 % → 99 % | 145.1 px | 0.20 | 6.29 | 23 |
| stroke 149 | 39 % → 94 % | 426.6 px | 0.22 | 2.40 | 26 |
| stroke 150 | 19 % → 58 % | 80.1 px | 0.24 | 3.05 | 74 |
| stroke 151 | 31 % → 78 % | 131.4 px | 0.15 | 2.49 | 71 |
| stroke 152 | 24 % → 62 % | 103.2 px | 0.24 | 2.60 | 86 |
| stroke 153 | 34 % → 71 % | 138.3 px | 0.18 | 2.09 | 134 |
| stroke 154 | 37 % → 64 % | 205.9 px | 0.17 | 1.71 | 56 |
| stroke 155 | 34 % → 84 % | 127.7 px | 0.26 | 2.47 | 91 |
| stroke 156 | 34 % → 86 % | 152.7 px | 0.28 | 2.51 | 84 |
| stroke 157 | 40 % → 79 % | 168.4 px | 0.18 | 1.97 | 88 |
| stroke 158 | 43 % → 92 % | 469.2 px | 0.18 | 2.11 | 14 |
| stroke 159 | 36 % → 84 % | 122.8 px | 0.19 | 2.34 | 125 |
| stroke 160 | 28 % → 94 % | 71.7 px | 0.34 | 3.31 | 100 |
| stroke 161 | 31 % → 98 % | 97.3 px | 0.36 | 3.18 | 99 |
| stroke 162 | 26 % → 49 % | 186.8 px | 0.21 | 1.89 | 18 |
| stroke 163 | 42 % → 77 % | 368.2 px | 0.21 | 1.85 | 25 |
| stroke 164 | 43 % → 96 % | 131.5 px | 0.30 | 2.24 | 53 |
| stroke 165 | 48 % → 85 % | 522.2 px | 0.17 | 1.79 | 18 |
| stroke 166 | 45 % → 74 % | 312.7 px | 0.17 | 1.64 | 37 |
| stroke 167 | 43 % → 83 % | 168.7 px | 0.25 | 1.95 | 79 |
| stroke 168 | 47 % → 84 % | 296.8 px | 0.21 | 1.78 | 27 |
| stroke 169 | 47 % → 86 % | 337.6 px | 0.22 | 1.81 | 26 |
| stroke 170 | 40 % → 85 % | 221.8 px | 0.20 | 2.15 | 19 |
| stroke 171 | 42 % → 96 % | 181.8 px | 0.32 | 2.28 | 32 |
| stroke 172 | 45 % → 77 % | 297.8 px | 0.18 | 1.71 | 43 |
| stroke 173 | 49 % → 92 % | 341.0 px | 0.23 | 1.86 | 25 |
| stroke 174 | 38 % → 93 % | 182.2 px | 0.34 | 2.43 | 28 |
| stroke 175 | 44 % → 74 % | 474.8 px | 0.16 | 1.68 | 12 |
| stroke 176 | 41 % → 78 % | 233.9 px | 0.19 | 1.88 | 40 |
| stroke 177 | 52 % → 84 % | 493.1 px | 0.16 | 1.62 | 15 |
| stroke 178 | 45 % → 90 % | 208.3 px | 0.20 | 2.00 | 46 |
| stroke 179 | 45 % → 91 % | 351.4 px | 0.31 | 2.03 | 17 |
| stroke 180 | 50 % → 89 % | 345.3 px | 0.20 | 1.76 | 30 |
| stroke 181 | 49 % → 86 % | 337.3 px | 0.19 | 1.75 | 31 |
| stroke 182 | 40 % → 97 % | 173.7 px | 0.35 | 2.40 | 21 |
| stroke 183 | 44 % → 98 % | 192.4 px | 0.34 | 2.24 | 25 |
| stroke 184 | 46 % → 70 % | 241.8 px | 0.17 | 1.53 | 124 |
| stroke 185 | 48 % → 73 % | 396.0 px | 0.16 | 1.50 | 24 |
| stroke 186 | 42 % → 51 % | 305.2 px | 0.17 | 1.20 | 24 |
| stroke 187 | 50 % → 81 % | 310.7 px | 0.18 | 1.63 | 39 |
| stroke 188 | 41 % → 60 % | 324.7 px | 0.20 | 1.47 | 32 |
| stroke 189 | 53 % → 80 % | 524.6 px | 0.18 | 1.49 | 24 |
| stroke 190 | 20 % → 89 % | 194.0 px | 0.26 | 4.53 | 21 |
| stroke 191 | 22 % → 90 % | 115.3 px | 0.26 | 4.13 | 62 |
| stroke 192 | 27 % → 86 % | 133.6 px | 0.24 | 3.13 | 73 |
| stroke 193 | 31 % → 59 % | 294.4 px | 0.14 | 1.87 | 17 |
| stroke 194 | 18 % → 74 % | 107.0 px | 0.10 | 4.21 | 54 |
| stroke 195 | 30 % → 75 % | 324.6 px | 0.08 | 2.49 | 9 |
| stroke 196 | 13 % → 68 % | 89.4 px | 0.18 | 5.21 | 63 |
| stroke 197 | 11 % → 98 % | 56.9 px | 0.21 | 9.22 | 48 |
| stroke 198 | 12 % → 99 % | 51.7 px | 0.33 | 8.38 | 129 |
| stroke 199 | 39 % → 92 % | 155.6 px | 0.21 | 2.39 | 39 |
| stroke 200 | 25 % → 78 % | 102.1 px | 0.29 | 3.09 | 58 |
| stroke 201 | 22 % → 88 % | 127.4 px | 0.36 | 3.92 | 35 |
| stroke 202 | 7 % → 97 % | 39.9 px | 0.43 | 14.19 | 25 |
| stroke 203 | 24 % → 97 % | 152.2 px | 0.32 | 4.05 | 23 |
| stroke 204 | 35 % → 95 % | 292.8 px | 0.32 | 2.74 | 19 |
| stroke 205 | 26 % → 68 % | 105.2 px | 0.16 | 2.60 | 454 |
| stroke 206 | 35 % → 86 % | 69.6 px | 0.18 | 2.45 | 353 |
| stroke 207 | 36 % → 67 % | 111.9 px | 0.11 | 1.85 | 436 |
| stroke 208 | 40 % → 54 % | 113.9 px | 0.09 | 1.34 | 241 |
| stroke 209 | 49 % → 54 % | 177.7 px | 0.09 | 1.09 | 239 |
| stroke 210 | 54 % → 82 % | 289.3 px | 0.15 | 1.54 | 90 |
| stroke 211 | 37 % → 80 % | 142.5 px | 0.20 | 2.17 | 222 |
| stroke 212 | 62 % → 73 % | 193.4 px | 0.10 | 1.18 | 315 |
| stroke 213 | 56 % → 83 % | 191.0 px | 0.15 | 1.49 | 332 |
| stroke 214 | 53 % → 96 % | 210.9 px | 0.17 | 1.80 | 122 |
| stroke 215 | 63 % → 86 % | 205.0 px | 0.12 | 1.37 | 205 |
| stroke 216 | 64 % → 99 % | 203.2 px | 0.14 | 1.55 | 250 |
| stroke 217 | 61 % → 100 % | 314.8 px | 0.19 | 1.63 | 83 |
| stroke 218 | 70 % → 96 % | 293.5 px | 0.13 | 1.39 | 111 |
| stroke 219 | 61 % → 83 % | 259.8 px | 0.13 | 1.36 | 209 |
| stroke 220 | 72 % → 100 % | 277.7 px | 0.16 | 1.39 | 228 |
| stroke 221 | 58 % → 60 % | 187.7 px | 0.10 | 1.02 | 132 |
| stroke 222 | 76 % → 92 % | 361.6 px | 0.13 | 1.21 | 199 |
| stroke 223 | 75 % → 95 % | 377.7 px | 0.15 | 1.26 | 160 |
| stroke 224 | 71 % → 93 % | 261.2 px | 0.16 | 1.31 | 275 |
| stroke 225 | 69 % → 85 % | 272.1 px | 0.11 | 1.24 | 174 |
| stroke 226 | 53 % → 72 % | 227.0 px | 0.16 | 1.35 | 310 |
| stroke 227 | 69 % → 98 % | 280.3 px | 0.20 | 1.41 | 134 |
| stroke 228 | 73 % → 74 % | 277.8 px | 0.10 | 1.02 | 273 |
| stroke 229 | 60 % → 74 % | 288.3 px | 0.13 | 1.24 | 227 |
| stroke 230 | 57 % → 72 % | 340.2 px | 0.14 | 1.27 | 131 |
| stroke 231 | 83 % → 90 % | 443.2 px | 0.09 | 1.09 | 311 |
| stroke 232 | 41 % → 54 % | 162.8 px | 0.10 | 1.31 | 70 |
| stroke 233 | 51 % → 59 % | 189.3 px | 0.13 | 1.16 | 180 |
| stroke 234 | 68 % → 73 % | 290.7 px | 0.12 | 1.08 | 95 |
| stroke 235 | 75 % → 96 % | 267.6 px | 0.17 | 1.27 | 267 |
| stroke 236 | 72 % → 99 % | 398.8 px | 0.20 | 1.38 | 105 |
| stroke 237 | 84 % → 96 % | 462.8 px | 0.16 | 1.15 | 116 |
| stroke 238 | 69 % → 77 % | 366.6 px | 0.11 | 1.11 | 117 |
| stroke 239 | 66 % → 73 % | 584.2 px | 0.12 | 1.12 | 28 |
| stroke 240 | 77 % → 84 % | 781.0 px | 0.11 | 1.09 | 21 |
| stroke 241 | 72 % → 79 % | 630.4 px | 0.11 | 1.10 | 69 |
| stroke 242 | 86 % → 97 % | 587.3 px | 0.14 | 1.13 | 45 |
| stroke 243 | 73 % → 80 % | 273.3 px | 0.14 | 1.09 | 113 |
| stroke 244 | 82 % → 87 % | 316.0 px | 0.14 | 1.05 | 148 |
| stroke 245 | 81 % → 85 % | 408.3 px | 0.14 | 1.05 | 86 |
| stroke 246 | 53 % → 63 % | 237.4 px | 0.18 | 1.18 | 146 |
| stroke 247 | 59 % → 70 % | 326.3 px | 0.18 | 1.19 | 64 |
| stroke 248 | 46 % → 91 % | 141.1 px | 0.24 | 1.97 | 115 |
| stroke 249 | 48 % → 95 % | 207.5 px | 0.28 | 1.98 | 101 |
| stroke 250 | 65 % → 91 % | 230.6 px | 0.20 | 1.41 | 102 |
| stroke 251 | 49 % → 97 % | 316.1 px | 0.28 | 1.99 | 31 |
| stroke 252 | 45 % → 86 % | 197.7 px | 0.25 | 1.92 | 88 |
| stroke 253 | 20 % → 100 % | 70.1 px | 0.42 | 5.04 | 77 |
| stroke 254 | 59 % → 94 % | 215.6 px | 0.26 | 1.59 | 100 |
| stroke 255 | 64 % → 100 % | 334.3 px | 0.26 | 1.56 | 52 |
| stroke 256 | 27 % → 100 % | 126.1 px | 0.43 | 3.73 | 52 |
| stroke 257 | 50 % → 99 % | 319.4 px | 0.34 | 1.99 | 50 |
| stroke 258 | 66 % → 87 % | 293.6 px | 0.19 | 1.32 | 77 |
| stroke 259 | 45 % → 85 % | 203.9 px | 0.25 | 1.91 | 84 |
| stroke 260 | 52 % → 88 % | 251.2 px | 0.25 | 1.69 | 68 |
| stroke 261 | 72 % → 91 % | 324.1 px | 0.23 | 1.26 | 104 |
| stroke 262 | 80 % → 100 % | 318.6 px | 0.21 | 1.25 | 71 |
| stroke 263 | 54 % → 87 % | 308.1 px | 0.27 | 1.62 | 76 |
| stroke 264 | 83 % → 95 % | 441.3 px | 0.22 | 1.15 | 90 |
| stroke 265 | 66 % → 100 % | 496.7 px | 0.29 | 1.51 | 27 |
| stroke 266 | 57 % → 89 % | 181.5 px | 0.28 | 1.58 | 265 |
| stroke 267 | 67 % → 93 % | 406.4 px | 0.28 | 1.37 | 51 |
| stroke 268 | 80 % → 90 % | 778.3 px | 0.26 | 1.13 | 21 |
| stroke 269 | 79 % → 99 % | 366.2 px | 0.24 | 1.26 | 65 |
| stroke 270 | 77 % → 96 % | 322.8 px | 0.26 | 1.24 | 100 |
| stroke 271 | 78 % → 88 % | 276.3 px | 0.19 | 1.13 | 110 |
| stroke 272 | 71 % → 90 % | 511.5 px | 0.26 | 1.27 | 42 |
| stroke 273 | 85 % → 90 % | 570.3 px | 0.19 | 1.06 | 43 |
| stroke 274 | 61 % → 97 % | 411.7 px | 0.26 | 1.59 | 67 |
| stroke 275 | 73 % → 95 % | 338.7 px | 0.23 | 1.29 | 108 |
| stroke 276 | 56 % → 99 % | 248.6 px | 0.27 | 1.78 | 70 |
| stroke 277 | 54 % → 100 % | 461.2 px | 0.37 | 1.86 | 28 |
| stroke 278 | 89 % → 94 % | 586.7 px | 0.22 | 1.06 | 48 |
| stroke 279 | 75 % → 89 % | 705.5 px | 0.22 | 1.18 | 37 |
| stroke 280 | 89 % → 93 % | 458.7 px | 0.19 | 1.05 | 79 |
| stroke 281 | 89 % → 100 % | 351.4 px | 0.19 | 1.12 | 100 |
| stroke 282 | 88 % → 92 % | 362.9 px | 0.20 | 1.04 | 152 |
| stroke 283 | 93 % → 93 % | 746.8 px | 0.21 | 1.00 | 35 |
| stroke 284 | 92 % → 93 % | 922.0 px | 0.20 | 1.00 | 36 |
| stroke 285 | 46 % → 100 % | 450.0 px | 0.37 | 2.15 | 33 |
| stroke 286 | 59 % → 100 % | 363.0 px | 0.29 | 1.71 | 50 |
| stroke 287 | 48 % → 100 % | 445.2 px | 0.39 | 2.10 | 31 |
| stroke 288 | 50 % → 100 % | 359.0 px | 0.38 | 1.99 | 59 |
| stroke 289 | 74 % → 90 % | 706.6 px | 0.24 | 1.20 | 32 |
| stroke 290 | 44 % → 100 % | 195.3 px | 0.42 | 2.29 | 58 |
| stroke 291 | 93 % → 94 % | 594.7 px | 0.21 | 1.01 | 33 |
| stroke 292 | 91 % → 94 % | 848.0 px | 0.21 | 1.03 | 26 |
| stroke 293 | 70 % → 84 % | 686.2 px | 0.24 | 1.19 | 27 |
| stroke 294 | 79 % → 100 % | 648.1 px | 0.27 | 1.26 | 21 |
| stroke 295 | 30 % → 100 % | 245.7 px | 0.45 | 3.39 | 21 |
| stroke 296 | 85 % → 84 % | 842.1 px | 0.20 | 1.00 | 25 |
| stroke 297 | 89 % → 93 % | 826.2 px | 0.23 | 1.05 | 27 |
| stroke 298 | 94 % → 97 % | 891.1 px | 0.23 | 1.03 | 23 |
| stroke 299 | 85 % → 85 % | 629.9 px | 0.18 | 1.00 | 35 |
| stroke 300 | 75 % → 94 % | 723.3 px | 0.27 | 1.26 | 32 |
| stroke 301 | 49 % → 100 % | 470.4 px | 0.41 | 2.03 | 12 |
| stroke 302 | 68 % → 100 % | 685.3 px | 0.32 | 1.46 | 29 |
| stroke 303 | 17 % → 100 % | 134.7 px | 0.45 | 5.86 | 27 |
| stroke 304 | 17 % → 100 % | 105.1 px | 0.50 | 5.96 | 50 |
| stroke 305 | 21 % → 100 % | 131.2 px | 0.49 | 4.77 | 35 |
| stroke 306 | 23 % → 100 % | 174.8 px | 0.50 | 4.29 | 27 |
| stroke 307 | 30 % → 100 % | 157.3 px | 0.44 | 3.33 | 68 |
| stroke 308 | 39 % → 78 % | 228.3 px | 0.23 | 1.99 | 89 |
| stroke 309 | 43 % → 78 % | 188.1 px | 0.29 | 1.79 | 78 |
| stroke 310 | 50 % → 78 % | 263.6 px | 0.28 | 1.56 | 44 |
| stroke 311 | 57 % → 78 % | 383.0 px | 0.25 | 1.37 | 32 |
| stroke 312 | 70 % → 84 % | 562.8 px | 0.24 | 1.21 | 20 |
| stroke 313 | 39 % → 90 % | 389.4 px | 0.40 | 2.29 | 15 |
| stroke 314 | 58 % → 85 % | 360.9 px | 0.29 | 1.46 | 51 |
| stroke 315 | 61 % → 89 % | 385.1 px | 0.27 | 1.46 | 50 |
| stroke 316 | 68 % → 74 % | 503.0 px | 0.22 | 1.08 | 46 |
| stroke 317 | 63 % → 85 % | 396.1 px | 0.26 | 1.36 | 65 |
| stroke 318 | 72 % → 77 % | 501.2 px | 0.22 | 1.07 | 40 |
| stroke 319 | 63 % → 88 % | 618.0 px | 0.30 | 1.40 | 33 |
| stroke 320 | 53 % → 88 % | 529.9 px | 0.36 | 1.64 | 36 |
| stroke 321 | 56 % → 80 % | 496.9 px | 0.31 | 1.42 | 26 |
| stroke 322 | 18 % → 85 % | 86.9 px | 0.43 | 4.63 | 82 |
| stroke 323 | 32 % → 89 % | 120.1 px | 0.39 | 2.81 | 82 |
| stroke 324 | 29 % → 83 % | 243.3 px | 0.41 | 2.83 | 37 |
| stroke 325 | 48 % → 90 % | 450.6 px | 0.33 | 1.88 | 19 |
| stroke 326 | 30 % → 93 % | 171.9 px | 0.40 | 3.11 | 81 |
| stroke 327 | 55 % → 85 % | 234.8 px | 0.24 | 1.55 | 106 |
| stroke 328 | 28 % → 93 % | 151.3 px | 0.47 | 3.30 | 24 |
| stroke 329 | 63 % → 97 % | 201.3 px | 0.26 | 1.55 | 136 |
| stroke 330 | 35 % → 93 % | 153.7 px | 0.45 | 2.68 | 43 |
| stroke 331 | 60 % → 86 % | 244.9 px | 0.23 | 1.43 | 116 |
| stroke 332 | 66 % → 91 % | 269.0 px | 0.22 | 1.39 | 83 |
| stroke 333 | 72 % → 97 % | 260.0 px | 0.23 | 1.34 | 80 |
| stroke 334 | 36 % → 97 % | 185.4 px | 0.40 | 2.66 | 48 |
| stroke 335 | 59 % → 79 % | 253.8 px | 0.22 | 1.35 | 120 |
| stroke 336 | 51 % → 98 % | 387.9 px | 0.34 | 1.91 | 23 |
| stroke 337 | 68 % → 97 % | 679.3 px | 0.25 | 1.43 | 14 |
| stroke 338 | 68 % → 98 % | 561.1 px | 0.24 | 1.44 | 22 |
| stroke 339 | 70 % → 94 % | 333.2 px | 0.34 | 1.34 | 52 |
| stroke 340 | 45 % → 98 % | 361.2 px | 0.38 | 2.19 | 25 |
| stroke 341 | 74 % → 98 % | 426.0 px | 0.29 | 1.31 | 63 |
| stroke 342 | 68 % → 96 % | 571.9 px | 0.28 | 1.41 | 15 |
| stroke 343 | 62 % → 95 % | 325.6 px | 0.31 | 1.53 | 80 |
| stroke 344 | 76 % → 98 % | 755.5 px | 0.27 | 1.28 | 17 |
| stroke 345 | 66 % → 97 % | 238.7 px | 0.28 | 1.46 | 126 |
| stroke 346 | 82 % → 95 % | 433.7 px | 0.33 | 1.15 | 67 |
| stroke 347 | 81 % → 93 % | 334.2 px | 0.20 | 1.14 | 112 |
| stroke 348 | 82 % → 94 % | 503.9 px | 0.21 | 1.15 | 38 |
| stroke 349 | 39 % → 100 % | 350.1 px | 0.44 | 2.53 | 33 |
| stroke 350 | 72 % → 96 % | 660.1 px | 0.29 | 1.34 | 40 |
| stroke 351 | 77 % → 95 % | 434.8 px | 0.26 | 1.23 | 67 |
| stroke 352 | 80 % → 97 % | 544.4 px | 0.32 | 1.21 | 64 |
| stroke 353 | 78 % → 96 % | 375.4 px | 0.25 | 1.23 | 161 |
| stroke 354 | 76 % → 97 % | 589.1 px | 0.29 | 1.27 | 32 |
| stroke 355 | 78 % → 82 % | 630.6 px | 0.18 | 1.05 | 69 |
| stroke 356 | 75 % → 97 % | 668.1 px | 0.31 | 1.29 | 40 |
| stroke 357 | 79 % → 90 % | 455.5 px | 0.24 | 1.13 | 91 |
| stroke 358 | 71 % → 92 % | 680.9 px | 0.40 | 1.28 | 45 |
| stroke 359 | 81 % → 88 % | 680.1 px | 0.23 | 1.09 | 32 |
| stroke 360 | 88 % → 93 % | 658.4 px | 0.24 | 1.07 | 33 |
| stroke 361 | 57 % → 93 % | 434.8 px | 0.43 | 1.63 | 23 |
| stroke 362 | 73 % → 97 % | 729.1 px | 0.33 | 1.34 | 20 |
| stroke 363 | 87 % → 93 % | 237.8 px | 0.08 | 1.07 | 18 |
| stroke 364 | 35 % → 68 % | 134.3 px | 0.33 | 1.92 | 12 |
| stroke 365 | 56 % → 80 % | 536.5 px | 0.25 | 1.42 | 12 |
| stroke 366 | 69 % → 74 % | 305.7 px | 0.14 | 1.07 | 38 |
| stroke 367 | 77 % → 80 % | 639.0 px | 0.13 | 1.04 | 7 |
| stroke 368 | 60 % → 65 % | 488.5 px | 0.16 | 1.09 | 16 |
| stroke 369 | 89 % → 90 % | 567.0 px | 0.08 | 1.01 | 28 |
| stroke 370 | 68 % → 72 % | 705.0 px | 0.12 | 1.06 | 14 |
| stroke 371 | 91 % → 95 % | 654.3 px | 0.13 | 1.05 | 12 |
| stroke 372 | 61 % → 100 % | 402.9 px | 0.34 | 1.65 | 16 |
| stroke 373 | 35 % → 100 % | 212.9 px | 0.46 | 2.88 | 13 |
| stroke 374 | 30 % → 95 % | 275.3 px | 0.41 | 3.17 | 14 |
| stroke 375 | 67 % → 92 % | 380.4 px | 0.31 | 1.36 | 24 |
| stroke 376 | 41 % → 85 % | 422.6 px | 0.39 | 2.09 | 4 |
| stroke 377 | 74 % → 78 % | 204.6 px | 0.22 | 1.05 | 207 |
| stroke 378 | 63 % → 63 % | 220.5 px | 0.30 | 1.00 | 88 |
| stroke 379 | 69 % → 97 % | 204.4 px | 0.30 | 1.40 | 242 |
| stroke 380 | 63 % → 97 % | 184.8 px | 0.37 | 1.55 | 326 |
| stroke 381 | 75 % → 97 % | 205.3 px | 0.38 | 1.30 | 333 |
| stroke 382 | 65 % → 99 % | 189.0 px | 0.42 | 1.53 | 311 |
| stroke 383 | 73 % → 97 % | 175.4 px | 0.36 | 1.32 | 253 |
| stroke 384 | 77 % → 99 % | 218.6 px | 0.47 | 1.29 | 227 |
| stroke 385 | 58 % → 90 % | 198.0 px | 0.47 | 1.54 | 190 |
| stroke 386 | 88 % → 96 % | 366.3 px | 0.33 | 1.10 | 208 |
| stroke 387 | 94 % → 97 % | 271.3 px | 0.34 | 1.04 | 339 |
| stroke 388 | 91 % → 98 % | 284.5 px | 0.32 | 1.07 | 399 |
| stroke 389 | 84 % → 99 % | 255.1 px | 0.41 | 1.18 | 354 |
| stroke 390 | 84 % → 99 % | 268.8 px | 0.29 | 1.18 | 235 |
| stroke 391 | 65 % → 89 % | 206.9 px | 0.36 | 1.36 | 191 |
| stroke 392 | 74 % → 89 % | 227.0 px | 0.49 | 1.22 | 170 |
| stroke 393 | 87 % → 96 % | 391.1 px | 0.37 | 1.11 | 172 |
| stroke 394 | 83 % → 91 % | 346.7 px | 0.32 | 1.09 | 275 |
| stroke 395 | 96 % → 100 % | 331.3 px | 0.49 | 1.04 | 185 |
| stroke 396 | 96 % → 97 % | 463.9 px | 0.38 | 1.01 | 97 |
| stroke 397 | 96 % → 100 % | 530.0 px | 0.36 | 1.04 | 62 |
| stroke 398 | 96 % → 99 % | 468.9 px | 0.37 | 1.04 | 164 |
| stroke 399 | 81 % → 89 % | 251.9 px | 0.43 | 1.11 | 113 |
| stroke 400 | 96 % → 98 % | 326.5 px | 0.31 | 1.02 | 216 |
| stroke 401 | 98 % → 98 % | 556.1 px | 0.25 | 1.00 | 89 |
| stroke 402 | 98 % → 98 % | 381.5 px | 0.40 | 1.01 | 230 |
| stroke 403 | 100 % → 100 % | 439.4 px | 0.39 | 1.00 | 113 |
| stroke 404 | 100 % → 100 % | 454.7 px | 0.49 | 1.00 | 121 |
| stroke 405 | 99 % → 100 % | 539.8 px | 0.52 | 1.01 | 86 |
| stroke 406 | 80 % → 83 % | 362.6 px | 0.38 | 1.03 | 107 |
| stroke 407 | 91 % → 91 % | 456.5 px | 0.37 | 1.01 | 127 |
| stroke 408 | 97 % → 97 % | 473.9 px | 0.46 | 1.00 | 67 |
| stroke 409 | 94 % → 95 % | 509.3 px | 0.40 | 1.01 | 99 |
| stroke 410 | 100 % → 100 % | 479.6 px | 0.43 | 1.00 | 105 |
| stroke 411 | 91 % → 99 % | 465.6 px | 0.46 | 1.09 | 78 |
| stroke 412 | 82 % → 93 % | 321.5 px | 0.42 | 1.13 | 150 |
| stroke 413 | 88 % → 90 % | 336.0 px | 0.44 | 1.03 | 103 |
| stroke 414 | 100 % → 100 % | 439.6 px | 0.48 | 1.00 | 106 |
| stroke 415 | 85 % → 85 % | 376.4 px | 0.43 | 1.00 | 80 |
| stroke 416 | 93 % → 97 % | 520.3 px | 0.44 | 1.04 | 152 |
| stroke 417 | 99 % → 99 % | 555.2 px | 0.40 | 1.00 | 89 |
| stroke 418 | 100 % → 100 % | 621.8 px | 0.51 | 1.00 | 67 |
| stroke 419 | 100 % → 100 % | 495.7 px | 0.42 | 1.00 | 150 |
| stroke 420 | 99 % → 99 % | 543.9 px | 0.50 | 1.00 | 72 |
| stroke 421 | 85 % → 91 % | 264.6 px | 0.36 | 1.07 | 324 |
| stroke 422 | 87 % → 94 % | 531.6 px | 0.35 | 1.08 | 83 |
| stroke 423 | 87 % → 90 % | 385.3 px | 0.38 | 1.02 | 142 |
| stroke 424 | 95 % → 95 % | 601.7 px | 0.25 | 1.00 | 77 |
| stroke 425 | 85 % → 84 % | 449.0 px | 0.40 | 0.99 | 77 |
| stroke 426 | 76 % → 78 % | 304.2 px | 0.11 | 1.03 | 41 |
| stroke 427 | 94 % → 93 % | 271.5 px | 0.13 | 1.00 | 68 |
| stroke 428 | 64 % → 67 % | 664.1 px | 0.15 | 1.04 | 8 |
| stroke 429 | 73 % → 74 % | 455.1 px | 0.15 | 1.01 | 33 |
| stroke 430 | 61 % → 62 % | 416.6 px | 0.14 | 1.01 | 22 |
| stroke 431 | 87 % → 87 % | 255.5 px | 0.24 | 1.00 | 118 |

Numbers say: wet paint spreads well beyond the stroke.

## Refs v3 · #13 HW blue streaky form — own sheet
own sheet 800 × 1020 · Gouache 1.00 + turpentine 30 % · 104 px · 585.8 s

![Refs v3 · #13 HW blue streaky form — own sheet](Refs-v3-13-HW-blue-streaky-form-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 9 % → 96 % | 95.1 px | 0.18 | 11.24 | 557 |
| stroke 2 | 13 % → 87 % | 94.1 px | 0.20 | 6.57 | 537 |
| stroke 3 | 18 % → 96 % | 192.7 px | 0.20 | 5.22 | 717 |
| stroke 4 | 29 % → 92 % | 265.9 px | 0.13 | 3.14 | 2435 |
| stroke 5 | 31 % → 94 % | 312.4 px | 0.25 | 3.06 | 1665 |
| stroke 6 | 49 % → 94 % | 466.4 px | 0.22 | 1.90 | 2874 |
| stroke 7 | 56 % → 96 % | 817.1 px | 0.20 | 1.71 | 915 |
| stroke 8 | 43 % → 94 % | 472.7 px | 0.14 | 2.18 | 1511 |
| stroke 9 | 47 % → 92 % | 1045.5 px | 0.14 | 1.94 | 821 |
| stroke 10 | 52 % → 98 % | 913.6 px | 0.17 | 1.90 | 523 |
| stroke 11 | 36 % → 93 % | 484.3 px | 0.13 | 2.55 | 542 |
| stroke 12 | 35 % → 97 % | 713.7 px | 0.20 | 2.79 | 197 |
| stroke 13 | 46 % → 99 % | 705.8 px | 0.25 | 2.17 | 411 |
| stroke 14 | 43 % → 92 % | 875.3 px | 0.12 | 2.13 | 264 |
| stroke 15 | 79 % → 98 % | 1476.9 px | 0.18 | 1.24 | 432 |
| stroke 16 | 48 % → 94 % | 708.2 px | 0.14 | 1.95 | 1125 |
| stroke 17 | 69 % → 97 % | 967.6 px | 0.15 | 1.41 | 737 |
| stroke 18 | 50 % → 93 % | 1037.4 px | 0.15 | 1.87 | 1096 |
| stroke 19 | 66 % → 89 % | 862.2 px | 0.17 | 1.36 | 1322 |
| stroke 20 | 39 % → 87 % | 434.3 px | 0.12 | 2.25 | 946 |
| stroke 21 | 60 % → 99 % | 973.4 px | 0.25 | 1.64 | 451 |
| stroke 22 | 71 % → 92 % | 930.3 px | 0.20 | 1.29 | 1289 |
| stroke 23 | 48 % → 90 % | 963.0 px | 0.12 | 1.87 | 484 |
| stroke 24 | 75 % → 95 % | 1625.3 px | 0.14 | 1.26 | 1119 |
| stroke 25 | 57 % → 90 % | 839.1 px | 0.13 | 1.57 | 2205 |
| stroke 26 | 71 % → 94 % | 1160.0 px | 0.13 | 1.32 | 1135 |
| stroke 27 | 68 % → 88 % | 1072.7 px | 0.22 | 1.29 | 967 |
| stroke 28 | 66 % → 94 % | 1538.6 px | 0.14 | 1.43 | 445 |
| stroke 29 | 62 % → 92 % | 1201.4 px | 0.22 | 1.50 | 505 |
| stroke 30 | 42 % → 85 % | 599.3 px | 0.11 | 2.03 | 695 |
| stroke 31 | 41 % → 84 % | 744.8 px | 0.10 | 2.04 | 501 |
| stroke 32 | 32 % → 94 % | 474.3 px | 0.18 | 2.97 | 178 |
| stroke 33 | 49 % → 90 % | 1403.2 px | 0.12 | 1.85 | 88 |
| stroke 34 | 34 % → 82 % | 1470.8 px | 0.09 | 2.43 | 10 |
| stroke 35 | 43 % → 88 % | 734.4 px | 0.11 | 2.03 | 93 |
| stroke 36 | 59 % → 91 % | 758.0 px | 0.11 | 1.54 | 144 |
| stroke 37 | 67 % → 91 % | 1342.1 px | 0.12 | 1.37 | 137 |
| stroke 38 | 46 % → 93 % | 561.5 px | 0.17 | 2.03 | 140 |
| stroke 39 | 55 % → 91 % | 864.6 px | 0.13 | 1.64 | 80 |
| stroke 40 | 67 % → 91 % | 1398.1 px | 0.12 | 1.37 | 213 |
| stroke 41 | 54 % → 91 % | 730.5 px | 0.14 | 1.68 | 195 |
| stroke 42 | 38 % → 97 % | 948.1 px | 0.24 | 2.53 | 44 |
| stroke 43 | 66 % → 90 % | 1114.5 px | 0.11 | 1.37 | 63 |
| stroke 44 | 68 % → 90 % | 1276.8 px | 0.12 | 1.33 | 190 |
| stroke 45 | 34 % → 96 % | 1121.6 px | 0.24 | 2.80 | 37 |
| stroke 46 | 77 % → 95 % | 1761.2 px | 0.13 | 1.24 | 100 |
| stroke 47 | 76 % → 94 % | 2061.6 px | 0.13 | 1.24 | 84 |
| stroke 48 | 70 % → 93 % | 3179.2 px | 0.12 | 1.33 | 30 |
| stroke 49 | 41 % → 97 % | 1116.4 px | 0.24 | 2.34 | 55 |
| stroke 50 | 55 % → 93 % | 1558.4 px | 0.16 | 1.70 | 40 |
| stroke 51 | 58 % → 89 % | 2056.1 px | 0.11 | 1.55 | 58 |
| stroke 52 | 44 % → 96 % | 1512.2 px | 0.21 | 2.17 | 61 |
| stroke 53 | 66 % → 90 % | 1081.4 px | 0.11 | 1.35 | 94 |
| stroke 54 | 72 % → 92 % | 2983.9 px | 0.12 | 1.27 | 50 |
| stroke 55 | 77 % → 93 % | 3152.4 px | 0.13 | 1.21 | 56 |
| stroke 56 | 63 % → 90 % | 2860.5 px | 0.11 | 1.43 | 41 |
| stroke 57 | 56 % → 87 % | 2122.5 px | 0.11 | 1.57 | 25 |
| stroke 58 | 61 % → 88 % | 2106.4 px | 0.11 | 1.45 | 52 |
| stroke 59 | 56 % → 99 % | 2290.4 px | 0.21 | 1.78 | 30 |
| stroke 60 | 60 % → 98 % | 2430.9 px | 0.19 | 1.63 | 38 |
| stroke 61 | 74 % → 97 % | 2654.3 px | 0.21 | 1.31 | 41 |
| stroke 62 | 69 % → 97 % | 2662.8 px | 0.22 | 1.41 | 44 |
| stroke 63 | 67 % → 97 % | 3829.5 px | 0.23 | 1.46 | 50 |
| stroke 64 | 37 % → 85 % | 1040.8 px | 0.10 | 2.32 | 43 |
| stroke 65 | 49 % → 84 % | 587.5 px | 0.10 | 1.73 | 120 |
| stroke 66 | 54 % → 84 % | 1651.9 px | 0.10 | 1.55 | 46 |
| stroke 67 | 23 % → 83 % | 461.2 px | 0.09 | 3.67 | 19 |
| stroke 68 | 57 % → 87 % | 804.7 px | 0.12 | 1.51 | 216 |
| stroke 69 | 66 % → 89 % | 1693.6 px | 0.12 | 1.35 | 127 |
| stroke 70 | 67 % → 89 % | 2128.1 px | 0.13 | 1.33 | 109 |
| stroke 71 | 46 % → 83 % | 530.5 px | 0.10 | 1.79 | 183 |
| stroke 72 | 42 % → 82 % | 407.7 px | 0.09 | 1.97 | 94 |
| stroke 73 | 52 % → 85 % | 1500.8 px | 0.10 | 1.62 | 101 |
| stroke 74 | 65 % → 90 % | 1661.5 px | 0.13 | 1.38 | 63 |
| stroke 75 | 51 % → 84 % | 766.3 px | 0.10 | 1.65 | 72 |
| stroke 76 | 39 % → 84 % | 591.0 px | 0.09 | 2.18 | 76 |
| stroke 77 | 49 % → 84 % | 555.3 px | 0.10 | 1.72 | 131 |
| stroke 78 | 68 % → 88 % | 1194.5 px | 0.12 | 1.28 | 116 |
| stroke 79 | 69 % → 89 % | 1309.4 px | 0.12 | 1.29 | 123 |
| stroke 80 | 66 % → 86 % | 1198.5 px | 0.12 | 1.30 | 103 |
| stroke 81 | 60 % → 83 % | 587.1 px | 0.10 | 1.39 | 181 |
| stroke 82 | 56 % → 83 % | 600.2 px | 0.10 | 1.48 | 180 |
| stroke 83 | 71 % → 83 % | 1498.4 px | 0.10 | 1.16 | 53 |
| stroke 84 | 68 % → 86 % | 2042.6 px | 0.12 | 1.27 | 52 |
| stroke 85 | 78 % → 87 % | 3537.2 px | 0.12 | 1.12 | 42 |
| stroke 86 | 76 % → 91 % | 2040.7 px | 0.12 | 1.20 | 67 |
| stroke 87 | 76 % → 86 % | 1253.7 px | 0.11 | 1.12 | 141 |
| stroke 88 | 85 % → 91 % | 2666.1 px | 0.13 | 1.07 | 53 |
| stroke 89 | 76 % → 86 % | 3444.9 px | 0.11 | 1.14 | 51 |
| stroke 90 | 58 % → 83 % | 1299.6 px | 0.09 | 1.42 | 40 |
| stroke 91 | 74 % → 84 % | 1400.9 px | 0.10 | 1.14 | 66 |
| stroke 92 | 59 % → 84 % | 738.1 px | 0.10 | 1.41 | 92 |
| stroke 93 | 79 % → 86 % | 1698.8 px | 0.11 | 1.09 | 106 |
| stroke 94 | 72 % → 84 % | 1318.0 px | 0.10 | 1.17 | 75 |
| stroke 95 | 62 % → 87 % | 2286.4 px | 0.10 | 1.40 | 42 |
| stroke 96 | 84 % → 94 % | 2210.5 px | 0.14 | 1.12 | 100 |
| stroke 97 | 94 % → 97 % | 4338.7 px | 0.15 | 1.03 | 45 |
| stroke 98 | 66 % → 82 % | 887.6 px | 0.10 | 1.25 | 105 |
| stroke 99 | 81 % → 85 % | 3189.5 px | 0.11 | 1.05 | 59 |
| stroke 100 | 54 % → 85 % | 1365.1 px | 0.09 | 1.57 | 31 |
| stroke 101 | 60 % → 84 % | 913.3 px | 0.10 | 1.39 | 81 |
| stroke 102 | 60 % → 84 % | 2336.3 px | 0.10 | 1.40 | 77 |
| stroke 103 | 71 % → 88 % | 3327.8 px | 0.12 | 1.24 | 43 |
| stroke 104 | 66 % → 87 % | 3058.7 px | 0.10 | 1.32 | 42 |
| stroke 105 | 64 % → 86 % | 2550.2 px | 0.11 | 1.33 | 176 |
| stroke 106 | 67 % → 87 % | 1286.8 px | 0.12 | 1.29 | 67 |
| stroke 107 | 70 % → 87 % | 1205.8 px | 0.12 | 1.24 | 124 |
| stroke 108 | 78 % → 88 % | 1531.4 px | 0.13 | 1.13 | 166 |
| stroke 109 | 69 % → 88 % | 1720.8 px | 0.12 | 1.27 | 55 |
| stroke 110 | 55 % → 96 % | 1508.1 px | 0.21 | 1.75 | 64 |
| stroke 111 | 64 % → 90 % | 2156.4 px | 0.22 | 1.41 | 36 |
| stroke 112 | 79 % → 99 % | 2898.8 px | 0.22 | 1.26 | 71 |
| stroke 113 | 76 % → 88 % | 3262.9 px | 0.20 | 1.16 | 24 |
| stroke 114 | 85 % → 87 % | 1614.7 px | 0.18 | 1.03 | 91 |
| stroke 115 | 82 % → 92 % | 5350.7 px | 0.13 | 1.12 | 17 |
| stroke 116 | 84 % → 88 % | 2265.5 px | 0.15 | 1.04 | 50 |
| stroke 117 | 71 % → 85 % | 2257.6 px | 0.13 | 1.20 | 35 |
| stroke 118 | 73 % → 86 % | 3526.0 px | 0.13 | 1.18 | 15 |
| stroke 119 | 48 % → 94 % | 240.6 px | 0.20 | 1.95 | 687 |
| stroke 120 | 44 % → 96 % | 770.5 px | 0.27 | 2.18 | 158 |
| stroke 121 | 46 % → 96 % | 289.6 px | 0.30 | 2.10 | 367 |
| stroke 122 | 41 % → 96 % | 526.3 px | 0.31 | 2.30 | 100 |
| stroke 123 | 47 % → 96 % | 417.3 px | 0.31 | 2.03 | 216 |
| stroke 124 | 58 % → 95 % | 686.6 px | 0.26 | 1.63 | 287 |
| stroke 125 | 56 % → 95 % | 1617.9 px | 0.27 | 1.70 | 87 |
| stroke 126 | 59 % → 95 % | 708.0 px | 0.25 | 1.60 | 214 |
| stroke 127 | 62 % → 95 % | 428.8 px | 0.23 | 1.52 | 308 |
| stroke 128 | 72 % → 94 % | 1608.7 px | 0.18 | 1.32 | 91 |
| stroke 129 | 43 % → 90 % | 422.6 px | 0.31 | 2.12 | 222 |
| stroke 130 | 42 % → 90 % | 739.7 px | 0.33 | 2.16 | 126 |
| stroke 131 | 32 % → 90 % | 403.8 px | 0.37 | 2.79 | 96 |
| stroke 132 | 51 % → 88 % | 393.2 px | 0.30 | 1.75 | 274 |
| stroke 133 | 36 % → 98 % | 549.7 px | 0.37 | 2.74 | 161 |
| stroke 134 | 48 % → 98 % | 964.0 px | 0.33 | 2.05 | 158 |
| stroke 135 | 50 % → 99 % | 1369.7 px | 0.32 | 1.98 | 123 |
| stroke 136 | 52 % → 99 % | 1500.2 px | 0.32 | 1.91 | 143 |
| stroke 137 | 49 % → 98 % | 866.6 px | 0.33 | 1.98 | 233 |
| stroke 138 | 38 % → 97 % | 763.9 px | 0.38 | 2.57 | 185 |
| stroke 139 | 50 % → 98 % | 1151.5 px | 0.33 | 1.95 | 234 |
| stroke 140 | 39 % → 97 % | 1286.6 px | 0.37 | 2.51 | 149 |
| stroke 141 | 70 % → 95 % | 1487.9 px | 0.21 | 1.36 | 176 |
| stroke 142 | 78 % → 93 % | 868.4 px | 0.15 | 1.20 | 591 |
| stroke 143 | 78 % → 94 % | 1084.2 px | 0.18 | 1.21 | 260 |
| stroke 144 | 80 % → 92 % | 830.8 px | 0.13 | 1.15 | 297 |
| stroke 145 | 84 % → 92 % | 1246.9 px | 0.12 | 1.09 | 203 |
| stroke 146 | 81 % → 94 % | 1325.8 px | 0.17 | 1.16 | 218 |
| stroke 147 | 74 % → 96 % | 2165.5 px | 0.21 | 1.29 | 112 |
| stroke 148 | 85 % → 91 % | 2318.0 px | 0.12 | 1.07 | 124 |
| stroke 149 | 82 % → 93 % | 2129.2 px | 0.16 | 1.15 | 175 |
| stroke 150 | 62 % → 83 % | 556.3 px | 0.09 | 1.34 | 253 |
| stroke 151 | 75 % → 86 % | 553.3 px | 0.10 | 1.15 | 297 |
| stroke 152 | 71 % → 84 % | 914.6 px | 0.09 | 1.19 | 199 |
| stroke 153 | 71 % → 82 % | 560.8 px | 0.09 | 1.15 | 527 |
| stroke 154 | 79 % → 86 % | 1238.9 px | 0.09 | 1.09 | 131 |
| stroke 155 | 76 % → 84 % | 748.9 px | 0.09 | 1.10 | 194 |
| stroke 156 | 79 % → 86 % | 1347.1 px | 0.09 | 1.09 | 248 |
| stroke 157 | 80 % → 85 % | 1740.3 px | 0.10 | 1.06 | 163 |
| stroke 158 | 78 % → 82 % | 529.1 px | 0.09 | 1.05 | 254 |
| stroke 159 | 84 % → 85 % | 2651.9 px | 0.10 | 1.01 | 140 |
| stroke 160 | 84 % → 84 % | 2185.2 px | 0.10 | 1.00 | 99 |
| stroke 161 | 86 % → 85 % | 1734.3 px | 0.11 | 1.00 | 394 |
| stroke 162 | 84 % → 84 % | 2271.5 px | 0.10 | 0.99 | 128 |
| stroke 163 | 55 % → 83 % | 879.9 px | 0.10 | 1.52 | 65 |
| stroke 164 | 66 % → 84 % | 562.6 px | 0.09 | 1.27 | 163 |
| stroke 165 | 81 % → 86 % | 815.6 px | 0.11 | 1.06 | 233 |
| stroke 166 | 81 % → 85 % | 882.3 px | 0.10 | 1.05 | 213 |
| stroke 167 | 84 % → 86 % | 1203.3 px | 0.11 | 1.03 | 183 |
| stroke 168 | 82 % → 85 % | 1152.6 px | 0.10 | 1.04 | 130 |
| stroke 169 | 85 % → 86 % | 1625.2 px | 0.11 | 1.01 | 103 |
| stroke 170 | 83 % → 84 % | 1043.2 px | 0.09 | 1.02 | 149 |
| stroke 171 | 83 % → 83 % | 1131.4 px | 0.08 | 1.01 | 153 |
| stroke 172 | 86 % → 86 % | 1801.4 px | 0.10 | 1.00 | 156 |
| stroke 173 | 85 % → 85 % | 1829.0 px | 0.10 | 1.00 | 107 |
| stroke 174 | 40 % → 91 % | 622.8 px | 0.35 | 2.26 | 61 |
| stroke 175 | 30 % → 95 % | 511.5 px | 0.39 | 3.12 | 51 |
| stroke 176 | 43 % → 91 % | 501.9 px | 0.36 | 2.13 | 74 |
| stroke 177 | 39 % → 94 % | 380.3 px | 0.39 | 2.41 | 54 |
| stroke 178 | 52 % → 92 % | 717.3 px | 0.34 | 1.75 | 68 |
| stroke 179 | 51 % → 92 % | 848.2 px | 0.35 | 1.83 | 76 |
| stroke 180 | 47 % → 93 % | 541.4 px | 0.39 | 2.00 | 82 |
| stroke 181 | 46 % → 95 % | 667.3 px | 0.39 | 2.08 | 87 |
| stroke 182 | 46 % → 96 % | 1635.1 px | 0.39 | 2.07 | 33 |
| stroke 183 | 59 % → 91 % | 664.6 px | 0.36 | 1.54 | 87 |
| stroke 184 | 51 % → 93 % | 710.3 px | 0.39 | 1.84 | 69 |
| stroke 185 | 54 % → 93 % | 665.4 px | 0.35 | 1.71 | 147 |
| stroke 186 | 59 % → 93 % | 1002.4 px | 0.40 | 1.57 | 37 |
| stroke 187 | 58 % → 94 % | 1019.7 px | 0.40 | 1.61 | 81 |
| stroke 188 | 57 % → 93 % | 1133.2 px | 0.39 | 1.62 | 54 |
| stroke 189 | 56 % → 93 % | 613.2 px | 0.39 | 1.67 | 119 |
| stroke 190 | 59 % → 93 % | 1540.9 px | 0.39 | 1.59 | 39 |
| stroke 191 | 61 % → 94 % | 915.4 px | 0.41 | 1.54 | 51 |
| stroke 192 | 62 % → 91 % | 2089.6 px | 0.37 | 1.48 | 24 |
| stroke 193 | 49 % → 97 % | 2310.8 px | 0.39 | 1.96 | 31 |
| stroke 194 | 60 % → 92 % | 2221.4 px | 0.36 | 1.53 | 26 |
| stroke 195 | 60 % → 93 % | 1697.7 px | 0.39 | 1.57 | 30 |
| stroke 196 | 33 % → 97 % | 498.7 px | 0.46 | 2.95 | 53 |
| stroke 197 | 42 % → 96 % | 372.3 px | 0.44 | 2.30 | 135 |
| stroke 198 | 48 % → 96 % | 849.4 px | 0.39 | 2.01 | 67 |
| stroke 199 | 40 % → 96 % | 540.2 px | 0.47 | 2.40 | 79 |
| stroke 200 | 46 % → 96 % | 955.4 px | 0.39 | 2.08 | 72 |
| stroke 201 | 46 % → 96 % | 1675.1 px | 0.46 | 2.10 | 18 |
| stroke 202 | 46 % → 97 % | 1751.1 px | 0.45 | 2.11 | 18 |
| stroke 203 | 44 % → 96 % | 1280.3 px | 0.43 | 2.20 | 31 |
| stroke 204 | 45 % → 96 % | 1958.3 px | 0.41 | 2.14 | 21 |
| stroke 205 | 50 % → 96 % | 1094.9 px | 0.36 | 1.91 | 31 |
| stroke 206 | 56 % → 96 % | 1525.2 px | 0.33 | 1.70 | 31 |
| stroke 207 | 59 % → 96 % | 1110.2 px | 0.32 | 1.64 | 74 |
| stroke 208 | 54 % → 96 % | 2045.1 px | 0.35 | 1.78 | 33 |
| stroke 209 | 56 % → 96 % | 1359.1 px | 0.34 | 1.73 | 65 |
| stroke 210 | 55 % → 96 % | 1414.1 px | 0.36 | 1.74 | 31 |
| stroke 211 | 74 % → 97 % | 3380.3 px | 0.25 | 1.31 | 31 |
| stroke 212 | 74 % → 97 % | 1526.5 px | 0.27 | 1.30 | 90 |
| stroke 213 | 73 % → 96 % | 1719.6 px | 0.27 | 1.31 | 236 |
| stroke 214 | 74 % → 99 % | 3441.4 px | 0.29 | 1.33 | 60 |
| stroke 215 | 79 % → 99 % | 3939.6 px | 0.26 | 1.25 | 22 |
| stroke 216 | 80 % → 98 % | 2594.1 px | 0.25 | 1.24 | 107 |
| stroke 217 | 78 % → 99 % | 3518.0 px | 0.27 | 1.27 | 69 |
| stroke 218 | 74 % → 97 % | 3684.7 px | 0.28 | 1.31 | 56 |
| stroke 219 | 78 % → 99 % | 3934.4 px | 0.27 | 1.27 | 40 |
| stroke 220 | 75 % → 92 % | 1254.8 px | 0.30 | 1.23 | 96 |
| stroke 221 | 78 % → 94 % | 1597.4 px | 0.29 | 1.20 | 108 |
| stroke 222 | 78 % → 92 % | 1951.9 px | 0.30 | 1.19 | 49 |
| stroke 223 | 78 % → 94 % | 1934.3 px | 0.30 | 1.19 | 90 |
| stroke 224 | 78 % → 93 % | 3908.2 px | 0.31 | 1.20 | 27 |
| stroke 225 | 81 % → 94 % | 1764.0 px | 0.27 | 1.16 | 67 |
| stroke 226 | 80 % → 93 % | 2638.1 px | 0.30 | 1.16 | 46 |
| stroke 227 | 63 % → 96 % | 946.3 px | 0.36 | 1.53 | 20 |
| stroke 228 | 66 % → 96 % | 1174.0 px | 0.33 | 1.46 | 34 |
| stroke 229 | 68 % → 96 % | 1851.1 px | 0.37 | 1.42 | 16 |
| stroke 230 | 85 % → 99 % | 4017.1 px | 0.23 | 1.17 | 12 |
| stroke 231 | 79 % → 99 % | 2038.6 px | 0.31 | 1.25 | 102 |
| stroke 232 | 71 % → 95 % | 596.5 px | 0.36 | 1.33 | 132 |
| stroke 233 | 80 % → 99 % | 2149.7 px | 0.30 | 1.23 | 107 |
| stroke 234 | 81 % → 96 % | 903.5 px | 0.31 | 1.18 | 305 |
| stroke 235 | 79 % → 97 % | 1077.9 px | 0.36 | 1.22 | 161 |
| stroke 236 | 87 % → 96 % | 1102.5 px | 0.27 | 1.10 | 156 |
| stroke 237 | 82 % → 97 % | 1155.5 px | 0.35 | 1.17 | 166 |
| stroke 238 | 80 % → 96 % | 1192.0 px | 0.43 | 1.20 | 68 |
| stroke 239 | 92 % → 97 % | 1792.1 px | 0.24 | 1.06 | 123 |
| stroke 240 | 88 % → 96 % | 1086.6 px | 0.34 | 1.09 | 120 |
| stroke 241 | 90 % → 96 % | 1931.3 px | 0.27 | 1.06 | 111 |
| stroke 242 | 82 % → 97 % | 1338.7 px | 0.40 | 1.18 | 114 |
| stroke 243 | 82 % → 97 % | 1515.5 px | 0.43 | 1.18 | 59 |
| stroke 244 | 88 % → 96 % | 1160.9 px | 0.39 | 1.09 | 188 |
| stroke 245 | 92 % → 97 % | 1328.7 px | 0.25 | 1.06 | 308 |
| stroke 246 | 90 % → 96 % | 1092.7 px | 0.35 | 1.06 | 138 |
| stroke 247 | 92 % → 96 % | 2037.8 px | 0.30 | 1.04 | 71 |
| stroke 248 | 92 % → 96 % | 3070.3 px | 0.31 | 1.04 | 48 |
| stroke 249 | 95 % → 97 % | 1480.9 px | 0.31 | 1.02 | 77 |
| stroke 250 | 91 % → 96 % | 2045.5 px | 0.41 | 1.05 | 76 |
| stroke 251 | 89 % → 97 % | 1903.0 px | 0.40 | 1.08 | 89 |
| stroke 252 | 94 % → 97 % | 1528.0 px | 0.33 | 1.03 | 137 |
| stroke 253 | 95 % → 98 % | 4361.6 px | 0.33 | 1.04 | 42 |
| stroke 254 | 91 % → 97 % | 2031.1 px | 0.40 | 1.06 | 96 |
| stroke 255 | 97 % → 99 % | 2742.1 px | 0.25 | 1.03 | 90 |
| stroke 256 | 85 % → 97 % | 2239.6 px | 0.43 | 1.14 | 60 |
| stroke 257 | 94 % → 96 % | 1824.7 px | 0.33 | 1.02 | 129 |
| stroke 258 | 95 % → 96 % | 3977.9 px | 0.28 | 1.00 | 39 |
| stroke 259 | 97 % → 97 % | 2247.9 px | 0.33 | 1.00 | 76 |
| stroke 260 | 96 % → 96 % | 2146.6 px | 0.35 | 1.00 | 49 |
| stroke 261 | 97 % → 97 % | 2336.9 px | 0.33 | 1.00 | 62 |
| stroke 262 | 96 % → 96 % | 2555.3 px | 0.34 | 1.00 | 58 |
| stroke 263 | 95 % → 97 % | 4303.9 px | 0.31 | 1.02 | 60 |
| stroke 264 | 87 % → 92 % | 905.0 px | 0.29 | 1.06 | 273 |
| stroke 265 | 86 % → 91 % | 869.2 px | 0.33 | 1.06 | 200 |
| stroke 266 | 92 % → 94 % | 973.2 px | 0.30 | 1.02 | 293 |
| stroke 267 | 90 % → 92 % | 1342.9 px | 0.34 | 1.02 | 125 |
| stroke 268 | 90 % → 91 % | 679.2 px | 0.33 | 1.01 | 251 |
| stroke 269 | 91 % → 92 % | 2052.5 px | 0.34 | 1.01 | 86 |
| stroke 270 | 97 % → 98 % | 1756.1 px | 0.33 | 1.00 | 131 |
| stroke 271 | 95 % → 94 % | 1508.5 px | 0.27 | 1.00 | 151 |
| stroke 272 | 91 % → 90 % | 2173.7 px | 0.33 | 1.00 | 52 |
| stroke 273 | 91 % → 90 % | 1889.9 px | 0.32 | 1.00 | 73 |
| stroke 274 | 92 % → 92 % | 2061.1 px | 0.36 | 1.00 | 60 |
| stroke 275 | 93 % → 94 % | 1744.8 px | 0.40 | 1.00 | 43 |
| stroke 276 | 97 % → 97 % | 3191.7 px | 0.33 | 1.00 | 67 |
| stroke 277 | 91 % → 91 % | 2862.6 px | 0.34 | 1.00 | 44 |
| stroke 278 | 91 % → 91 % | 2851.1 px | 0.34 | 1.00 | 44 |
| stroke 279 | 95 % → 95 % | 2209.9 px | 0.35 | 1.00 | 82 |
| stroke 280 | 98 % → 98 % | 4544.7 px | 0.30 | 1.00 | 44 |
| stroke 281 | 93 % → 92 % | 3284.7 px | 0.29 | 0.99 | 44 |

Numbers say: wet paint spreads well beyond the stroke.

## Refs v3 · #14 HW olive totem — own sheet
own sheet 800 × 1040 · Gouache 1.00 + turpentine 30 % · 57 px · 404.4 s

![Refs v3 · #14 HW olive totem — own sheet](Refs-v3-14-HW-olive-totem-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 7 % → 88 % | 57.3 px | 0.21 | 13.36 | 77 |
| stroke 2 | 10 % → 88 % | 125.4 px | 0.20 | 8.43 | 46 |
| stroke 3 | 6 % → 76 % | 55.8 px | 0.22 | 11.82 | 75 |
| stroke 4 | 10 % → 71 % | 85.6 px | 0.22 | 7.24 | 94 |
| stroke 5 | 16 % → 63 % | 99.2 px | 0.23 | 3.86 | 145 |
| stroke 6 | 21 % → 79 % | 166.5 px | 0.23 | 3.82 | 114 |
| stroke 7 | 8 % → 96 % | 55.5 px | 0.19 | 12.70 | 91 |
| stroke 8 | 12 % → 97 % | 87.8 px | 0.20 | 8.41 | 74 |
| stroke 9 | 24 % → 97 % | 111.8 px | 0.20 | 4.09 | 209 |
| stroke 10 | 20 % → 96 % | 183.0 px | 0.20 | 4.80 | 197 |
| stroke 11 | 28 % → 96 % | 156.9 px | 0.21 | 3.45 | 295 |
| stroke 12 | 30 % → 98 % | 330.7 px | 0.21 | 3.27 | 64 |
| stroke 13 | 47 % → 97 % | 305.2 px | 0.21 | 2.05 | 110 |
| stroke 14 | 51 % → 98 % | 509.1 px | 0.23 | 1.93 | 71 |
| stroke 15 | 42 % → 97 % | 239.5 px | 0.18 | 2.30 | 158 |
| stroke 16 | 44 % → 99 % | 321.4 px | 0.22 | 2.27 | 669 |
| stroke 17 | 32 % → 90 % | 318.0 px | 0.19 | 2.83 | 214 |
| stroke 18 | 53 % → 97 % | 558.7 px | 0.21 | 1.83 | 97 |
| stroke 19 | 28 % → 84 % | 303.6 px | 0.19 | 2.97 | 150 |
| stroke 20 | 23 % → 70 % | 157.7 px | 0.23 | 3.05 | 303 |
| stroke 21 | 29 % → 64 % | 306.0 px | 0.24 | 2.23 | 116 |
| stroke 22 | 43 % → 63 % | 402.1 px | 0.26 | 1.47 | 73 |
| stroke 23 | 17 % → 98 % | 86.4 px | 0.21 | 5.72 | 303 |
| stroke 24 | 10 % → 96 % | 114.6 px | 0.21 | 10.13 | 90 |
| stroke 25 | 22 % → 97 % | 234.1 px | 0.22 | 4.44 | 68 |
| stroke 26 | 17 % → 99 % | 197.6 px | 0.25 | 5.69 | 68 |
| stroke 27 | 27 % → 99 % | 344.6 px | 0.26 | 3.65 | 91 |
| stroke 28 | 23 % → 97 % | 291.4 px | 0.22 | 4.23 | 167 |
| stroke 29 | 38 % → 97 % | 286.3 px | 0.22 | 2.53 | 286 |
| stroke 30 | 31 % → 91 % | 270.4 px | 0.22 | 2.89 | 858 |
| stroke 31 | 22 % → 99 % | 202.1 px | 0.23 | 4.49 | 114 |
| stroke 32 | 37 % → 97 % | 330.8 px | 0.25 | 2.60 | 417 |
| stroke 33 | 55 % → 97 % | 570.9 px | 0.26 | 1.78 | 525 |
| stroke 34 | 54 % → 97 % | 399.5 px | 0.23 | 1.80 | 322 |
| stroke 35 | 47 % → 97 % | 590.2 px | 0.22 | 2.08 | 410 |
| stroke 36 | 37 % → 99 % | 496.7 px | 0.24 | 2.69 | 398 |
| stroke 37 | 63 % → 98 % | 854.9 px | 0.23 | 1.54 | 194 |
| stroke 38 | 67 % → 97 % | 986.3 px | 0.22 | 1.43 | 94 |
| stroke 39 | 11 % → 96 % | 53.5 px | 0.28 | 8.39 | 471 |
| stroke 40 | 13 % → 83 % | 92.0 px | 0.25 | 6.55 | 453 |
| stroke 41 | 19 % → 99 % | 134.9 px | 0.27 | 5.06 | 184 |
| stroke 42 | 32 % → 99 % | 360.0 px | 0.25 | 3.09 | 330 |
| stroke 43 | 18 % → 80 % | 120.9 px | 0.27 | 4.35 | 394 |
| stroke 44 | 31 % → 97 % | 253.1 px | 0.26 | 3.10 | 162 |
| stroke 45 | 31 % → 88 % | 193.9 px | 0.29 | 2.85 | 348 |
| stroke 46 | 24 % → 100 % | 181.9 px | 0.28 | 4.19 | 238 |
| stroke 47 | 34 % → 99 % | 224.0 px | 0.25 | 2.93 | 442 |
| stroke 48 | 27 % → 79 % | 201.6 px | 0.25 | 2.88 | 266 |
| stroke 49 | 33 % → 67 % | 189.2 px | 0.25 | 1.99 | 247 |
| stroke 50 | 48 % → 99 % | 275.4 px | 0.27 | 2.05 | 322 |
| stroke 51 | 52 % → 99 % | 559.2 px | 0.27 | 1.88 | 97 |
| stroke 52 | 33 % → 90 % | 243.1 px | 0.27 | 2.70 | 175 |
| stroke 53 | 37 % → 95 % | 217.4 px | 0.27 | 2.55 | 462 |
| stroke 54 | 39 % → 65 % | 301.2 px | 0.25 | 1.66 | 98 |
| stroke 55 | 46 % → 90 % | 343.7 px | 0.25 | 1.95 | 328 |
| stroke 56 | 58 % → 99 % | 393.3 px | 0.28 | 1.72 | 379 |
| stroke 57 | 57 % → 93 % | 482.1 px | 0.28 | 1.62 | 206 |
| stroke 58 | 51 % → 81 % | 429.3 px | 0.25 | 1.59 | 156 |
| stroke 59 | 63 % → 89 % | 682.4 px | 0.27 | 1.42 | 267 |
| stroke 60 | 41 % → 64 % | 394.8 px | 0.25 | 1.56 | 154 |
| stroke 61 | 54 % → 82 % | 344.5 px | 0.27 | 1.52 | 309 |
| stroke 62 | 77 % → 99 % | 650.8 px | 0.28 | 1.28 | 151 |
| stroke 63 | 65 % → 99 % | 453.4 px | 0.28 | 1.52 | 167 |
| stroke 64 | 71 % → 89 % | 667.4 px | 0.25 | 1.25 | 113 |
| stroke 65 | 50 % → 68 % | 680.9 px | 0.26 | 1.38 | 61 |
| stroke 66 | 39 % → 53 % | 421.5 px | 0.26 | 1.37 | 49 |
| stroke 67 | 47 % → 61 % | 473.6 px | 0.26 | 1.31 | 77 |
| stroke 68 | 62 % → 100 % | 758.0 px | 0.29 | 1.60 | 150 |
| stroke 69 | 59 % → 95 % | 523.1 px | 0.27 | 1.59 | 123 |
| stroke 70 | 67 % → 86 % | 826.0 px | 0.26 | 1.28 | 93 |
| stroke 71 | 45 % → 99 % | 564.9 px | 0.28 | 2.20 | 59 |
| stroke 72 | 61 % → 82 % | 718.2 px | 0.27 | 1.34 | 115 |
| stroke 73 | 54 % → 69 % | 453.9 px | 0.24 | 1.28 | 90 |
| stroke 74 | 78 % → 98 % | 888.2 px | 0.28 | 1.25 | 83 |
| stroke 75 | 58 % → 100 % | 546.2 px | 0.28 | 1.72 | 97 |
| stroke 76 | 38 % → 53 % | 545.8 px | 0.26 | 1.41 | 58 |
| stroke 77 | 45 % → 100 % | 623.4 px | 0.29 | 2.22 | 52 |
| stroke 78 | 55 % → 76 % | 787.2 px | 0.28 | 1.39 | 64 |
| stroke 79 | 53 % → 62 % | 476.5 px | 0.25 | 1.17 | 134 |
| stroke 80 | 49 % → 93 % | 501.1 px | 0.27 | 1.90 | 98 |
| stroke 81 | 74 % → 99 % | 733.6 px | 0.27 | 1.34 | 120 |
| stroke 82 | 58 % → 100 % | 787.0 px | 0.28 | 1.74 | 153 |
| stroke 83 | 75 % → 99 % | 982.7 px | 0.29 | 1.32 | 80 |
| stroke 84 | 52 % → 63 % | 456.2 px | 0.23 | 1.21 | 66 |
| stroke 85 | 13 % → 81 % | 64.6 px | 0.22 | 6.29 | 60 |
| stroke 86 | 11 % → 75 % | 175.8 px | 0.20 | 6.69 | 12 |
| stroke 87 | 14 % → 95 % | 160.2 px | 0.22 | 6.96 | 23 |
| stroke 88 | 21 % → 91 % | 440.3 px | 0.22 | 4.33 | 13 |
| stroke 89 | 46 % → 97 % | 545.3 px | 0.22 | 2.09 | 25 |
| stroke 90 | 17 % → 64 % | 298.6 px | 0.21 | 3.67 | 20 |
| stroke 91 | 20 % → 81 % | 172.7 px | 0.19 | 4.06 | 61 |
| stroke 92 | 53 % → 91 % | 942.4 px | 0.28 | 1.73 | 20 |
| stroke 93 | 17 % → 98 % | 188.9 px | 0.25 | 5.71 | 97 |
| stroke 94 | 28 % → 90 % | 428.5 px | 0.26 | 3.21 | 23 |
| stroke 95 | 28 % → 67 % | 197.7 px | 0.20 | 2.44 | 224 |
| stroke 96 | 51 % → 96 % | 298.3 px | 0.21 | 1.89 | 750 |
| stroke 97 | 58 % → 98 % | 343.5 px | 0.18 | 1.68 | 976 |
| stroke 98 | 43 % → 84 % | 209.8 px | 0.21 | 1.95 | 501 |
| stroke 99 | 71 % → 97 % | 394.3 px | 0.22 | 1.36 | 446 |
| stroke 100 | 45 % → 84 % | 236.0 px | 0.21 | 1.85 | 531 |
| stroke 101 | 41 % → 77 % | 160.0 px | 0.21 | 1.89 | 278 |
| stroke 102 | 51 % → 85 % | 320.5 px | 0.20 | 1.66 | 452 |
| stroke 103 | 62 % → 93 % | 286.0 px | 0.21 | 1.50 | 642 |
| stroke 104 | 64 % → 92 % | 529.3 px | 0.22 | 1.45 | 198 |
| stroke 105 | 69 % → 97 % | 642.0 px | 0.21 | 1.40 | 232 |
| stroke 106 | 75 % → 97 % | 744.4 px | 0.22 | 1.30 | 162 |
| stroke 107 | 84 % → 98 % | 505.6 px | 0.20 | 1.17 | 403 |
| stroke 108 | 62 % → 86 % | 443.3 px | 0.28 | 1.39 | 280 |
| stroke 109 | 67 % → 85 % | 315.1 px | 0.21 | 1.28 | 361 |
| stroke 110 | 70 % → 94 % | 466.5 px | 0.22 | 1.34 | 406 |
| stroke 111 | 65 % → 81 % | 375.2 px | 0.21 | 1.25 | 419 |
| stroke 112 | 68 % → 83 % | 411.9 px | 0.21 | 1.22 | 397 |
| stroke 113 | 57 % → 71 % | 341.6 px | 0.23 | 1.23 | 508 |
| stroke 114 | 77 % → 85 % | 443.2 px | 0.22 | 1.11 | 220 |
| stroke 115 | 75 % → 82 % | 543.6 px | 0.22 | 1.09 | 228 |
| stroke 116 | 71 % → 85 % | 479.3 px | 0.25 | 1.20 | 365 |
| stroke 117 | 90 % → 93 % | 576.1 px | 0.21 | 1.04 | 356 |
| stroke 118 | 74 % → 80 % | 630.9 px | 0.22 | 1.08 | 199 |
| stroke 119 | 64 % → 73 % | 431.6 px | 0.25 | 1.14 | 291 |
| stroke 120 | 88 % → 97 % | 834.1 px | 0.22 | 1.10 | 167 |
| stroke 121 | 69 % → 70 % | 485.1 px | 0.21 | 1.02 | 302 |
| stroke 122 | 79 % → 91 % | 772.9 px | 0.22 | 1.15 | 377 |
| stroke 123 | 57 % → 78 % | 521.9 px | 0.20 | 1.37 | 227 |
| stroke 124 | 95 % → 96 % | 809.5 px | 0.21 | 1.02 | 475 |
| stroke 125 | 96 % → 97 % | 1036.4 px | 0.22 | 1.01 | 206 |
| stroke 126 | 79 % → 86 % | 545.9 px | 0.22 | 1.08 | 439 |
| stroke 127 | 97 % → 97 % | 1001.1 px | 0.21 | 1.00 | 182 |
| stroke 128 | 93 % → 97 % | 955.5 px | 0.22 | 1.04 | 209 |
| stroke 129 | 73 % → 84 % | 564.4 px | 0.25 | 1.15 | 287 |
| stroke 130 | 71 % → 78 % | 803.7 px | 0.23 | 1.10 | 190 |
| stroke 131 | 53 % → 60 % | 314.3 px | 0.26 | 1.12 | 463 |
| stroke 132 | 84 % → 100 % | 804.5 px | 0.27 | 1.19 | 176 |
| stroke 133 | 78 % → 99 % | 427.5 px | 0.29 | 1.27 | 944 |
| stroke 134 | 86 % → 100 % | 631.0 px | 0.28 | 1.16 | 242 |
| stroke 135 | 59 % → 67 % | 417.2 px | 0.24 | 1.14 | 92 |
| stroke 136 | 56 % → 96 % | 505.7 px | 0.15 | 1.71 | 19 |
| stroke 137 | 30 % → 99 % | 286.2 px | 0.23 | 3.32 | 54 |
| stroke 138 | 66 % → 67 % | 313.6 px | 0.18 | 1.01 | 323 |
| stroke 139 | 79 % → 81 % | 412.8 px | 0.20 | 1.02 | 445 |
| stroke 140 | 62 % → 98 % | 232.5 px | 0.14 | 1.58 | 671 |
| stroke 141 | 76 % → 99 % | 402.4 px | 0.09 | 1.30 | 246 |
| stroke 142 | 83 % → 99 % | 519.9 px | 0.15 | 1.19 | 370 |
| stroke 143 | 76 % → 99 % | 380.0 px | 0.23 | 1.31 | 672 |
| stroke 144 | 80 % → 99 % | 482.9 px | 0.17 | 1.24 | 222 |
| stroke 145 | 85 % → 98 % | 439.8 px | 0.08 | 1.15 | 287 |
| stroke 146 | 95 % → 97 % | 454.6 px | 0.12 | 1.02 | 404 |
| stroke 147 | 97 % → 97 % | 462.0 px | 0.15 | 1.00 | 369 |
| stroke 148 | 55 % → 96 % | 138.0 px | 0.20 | 1.76 | 747 |
| stroke 149 | 64 % → 98 % | 265.3 px | 0.22 | 1.52 | 463 |
| stroke 150 | 83 % → 97 % | 340.0 px | 0.11 | 1.17 | 287 |
| stroke 151 | 71 % → 98 % | 429.0 px | 0.24 | 1.38 | 483 |
| stroke 152 | 84 % → 96 % | 188.2 px | 0.12 | 1.15 | 563 |
| stroke 153 | 39 % → 69 % | 212.5 px | 0.28 | 1.75 | 202 |
| stroke 154 | 64 % → 79 % | 937.9 px | 0.25 | 1.23 | 25 |
| stroke 155 | 72 % → 75 % | 546.2 px | 0.23 | 1.03 | 136 |
| stroke 156 | 71 % → 72 % | 746.3 px | 0.23 | 1.02 | 46 |
| stroke 157 | 69 % → 69 % | 902.1 px | 0.23 | 1.00 | 61 |
| stroke 158 | 55 % → 60 % | 345.6 px | 0.25 | 1.08 | 121 |
| stroke 159 | 52 % → 53 % | 472.7 px | 0.25 | 1.00 | 84 |
| stroke 160 | 75 % → 92 % | 402.4 px | 0.26 | 1.23 | 345 |
| stroke 161 | 68 % → 73 % | 454.0 px | 0.27 | 1.07 | 526 |
| stroke 162 | 92 % → 98 % | 677.1 px | 0.23 | 1.07 | 290 |
| stroke 163 | 90 % → 100 % | 804.2 px | 0.21 | 1.11 | 184 |
| stroke 164 | 78 % → 95 % | 468.5 px | 0.26 | 1.22 | 131 |
| stroke 165 | 82 % → 94 % | 504.5 px | 0.26 | 1.15 | 147 |
| stroke 166 | 83 % → 99 % | 484.8 px | 0.27 | 1.20 | 320 |
| stroke 167 | 81 % → 99 % | 425.7 px | 0.25 | 1.22 | 399 |
| stroke 168 | 80 % → 94 % | 544.0 px | 0.27 | 1.17 | 162 |
| stroke 169 | 84 % → 89 % | 905.6 px | 0.27 | 1.06 | 73 |
| stroke 170 | 90 % → 99 % | 668.4 px | 0.26 | 1.11 | 200 |
| stroke 171 | 90 % → 100 % | 614.1 px | 0.28 | 1.11 | 206 |
| stroke 172 | 88 % → 100 % | 523.7 px | 0.25 | 1.13 | 168 |
| stroke 173 | 87 % → 100 % | 677.9 px | 0.26 | 1.14 | 40 |
| stroke 174 | 94 % → 96 % | 1426.9 px | 0.28 | 1.03 | 61 |
| stroke 175 | 92 % → 99 % | 684.5 px | 0.24 | 1.08 | 147 |
| stroke 176 | 91 % → 100 % | 1288.7 px | 0.28 | 1.09 | 52 |
| stroke 177 | 95 % → 99 % | 837.3 px | 0.23 | 1.04 | 130 |
| stroke 178 | 94 % → 100 % | 714.9 px | 0.29 | 1.06 | 87 |
| stroke 179 | 97 % → 100 % | 515.9 px | 0.30 | 1.02 | 131 |
| stroke 180 | 95 % → 97 % | 776.7 px | 0.26 | 1.02 | 158 |
| stroke 181 | 94 % → 98 % | 838.3 px | 0.27 | 1.04 | 103 |
| stroke 182 | 99 % → 100 % | 878.8 px | 0.27 | 1.00 | 176 |
| stroke 183 | 83 % → 87 % | 647.4 px | 0.29 | 1.04 | 130 |
| stroke 184 | 98 % → 99 % | 591.2 px | 0.26 | 1.00 | 234 |
| stroke 185 | 86 % → 88 % | 752.9 px | 0.29 | 1.03 | 143 |
| stroke 186 | 97 % → 97 % | 940.9 px | 0.27 | 1.00 | 76 |
| stroke 187 | 93 % → 94 % | 1188.3 px | 0.29 | 1.02 | 65 |
| stroke 188 | 99 % → 99 % | 510.6 px | 0.27 | 1.00 | 251 |
| stroke 189 | 99 % → 99 % | 660.0 px | 0.25 | 1.00 | 99 |
| stroke 190 | 99 % → 99 % | 1075.7 px | 0.28 | 1.00 | 73 |
| stroke 191 | 100 % → 100 % | 1066.9 px | 0.20 | 1.00 | 122 |
| stroke 192 | 100 % → 100 % | 1583.1 px | 0.22 | 1.00 | 62 |
| stroke 193 | 100 % → 100 % | 1364.8 px | 0.29 | 1.00 | 51 |
| stroke 194 | 97 % → 97 % | 1520.1 px | 0.23 | 1.00 | 60 |
| stroke 195 | 97 % → 98 % | 1537.2 px | 0.28 | 1.02 | 52 |
| stroke 196 | 99 % → 99 % | 1426.0 px | 0.24 | 1.00 | 58 |
| stroke 197 | 97 % → 98 % | 1352.2 px | 0.29 | 1.01 | 59 |
| stroke 198 | 94 % → 95 % | 1182.3 px | 0.29 | 1.00 | 109 |
| stroke 199 | 70 % → 71 % | 389.4 px | 0.25 | 1.02 | 283 |
| stroke 200 | 76 % → 76 % | 630.6 px | 0.25 | 1.00 | 129 |
| stroke 201 | 68 % → 68 % | 688.2 px | 0.25 | 1.00 | 113 |
| stroke 202 | 97 % → 97 % | 984.5 px | 0.17 | 1.00 | 42 |
| stroke 203 | 97 % → 97 % | 1438.0 px | 0.27 | 1.00 | 29 |

Numbers say: wet paint spreads well beyond the stroke.

## Refs v3 · #15 Ultramarine script — own sheet
own sheet 800 × 1422 · Ink 0.98 · 39 px · 324.3 s

![Refs v3 · #15 Ultramarine script — own sheet](Refs-v3-15-Ultramarine-script-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 3 % → 39 % | 15.5 px | 0.67 | 15.05 | 70 |
| stroke 2 | 4 % → 41 % | 22.4 px | 0.69 | 9.95 | 17 |
| stroke 3 | 11 % → 43 % | 24.7 px | 0.68 | 3.74 | 58 |
| stroke 4 | 15 % → 40 % | 81.4 px | 0.68 | 2.69 | 21 |
| stroke 5 | 18 % → 37 % | 219.8 px | 0.67 | 2.08 | 15 |
| stroke 6 | 19 % → 36 % | 241.6 px | 0.68 | 1.93 | 9 |
| stroke 7 | 19 % → 35 % | 101.3 px | 0.67 | 1.88 | 46 |
| stroke 8 | 29 % → 41 % | 258.5 px | 0.69 | 1.43 | 6 |
| stroke 9 | 3 % → 31 % | 16.0 px | 0.68 | 11.21 | 22 |
| stroke 10 | 5 % → 40 % | 28.9 px | 0.67 | 7.57 | 65 |
| stroke 11 | 4 % → 30 % | 59.6 px | 0.67 | 6.78 | 4 |
| stroke 12 | 9 % → 32 % | 31.9 px | 0.67 | 3.40 | 40 |
| stroke 13 | 14 % → 32 % | 97.3 px | 0.67 | 2.32 | 19 |
| stroke 14 | 19 % → 33 % | 119.4 px | 0.66 | 1.75 | 23 |
| stroke 15 | 20 % → 35 % | 102.9 px | 0.66 | 1.73 | 43 |
| stroke 16 | 11 % → 40 % | 98.5 px | 0.67 | 3.56 | 14 |
| stroke 17 | 5 % → 47 % | 23.7 px | 0.68 | 9.88 | 15 |
| stroke 18 | 12 % → 45 % | 53.5 px | 0.68 | 3.80 | 15 |
| stroke 19 | 16 % → 38 % | 97.0 px | 0.67 | 2.31 | 12 |
| stroke 20 | 18 % → 43 % | 239.9 px | 0.67 | 2.34 | 6 |
| stroke 21 | 20 % → 40 % | 248.3 px | 0.66 | 2.03 | 8 |
| stroke 22 | 23 % → 44 % | 66.0 px | 0.66 | 1.87 | 43 |
| stroke 23 | 37 % → 46 % | 390.9 px | 0.67 | 1.24 | 7 |
| stroke 24 | 2 % → 32 % | 18.3 px | 0.66 | 17.57 | 8 |
| stroke 25 | 2 % → 47 % | 38.3 px | 0.68 | 20.42 | 7 |
| stroke 26 | 4 % → 59 % | 19.5 px | 0.68 | 14.11 | 37 |
| stroke 27 | 3 % → 43 % | 37.5 px | 0.68 | 13.35 | 9 |
| stroke 28 | 27 % → 56 % | 73.6 px | 0.68 | 2.05 | 25 |
| stroke 29 | 4 % → 49 % | 31.4 px | 0.67 | 12.40 | 8 |
| stroke 30 | 8 % → 39 % | 41.0 px | 0.67 | 5.18 | 19 |
| stroke 31 | 11 % → 45 % | 97.2 px | 0.67 | 4.15 | 9 |
| stroke 32 | 16 % → 39 % | 134.2 px | 0.67 | 2.48 | 10 |
| stroke 33 | 11 % → 34 % | 83.6 px | 0.67 | 3.20 | 22 |
| stroke 34 | 8 % → 36 % | 55.4 px | 0.67 | 4.47 | 58 |
| stroke 35 | 15 % → 41 % | 143.0 px | 0.67 | 2.77 | 12 |
| stroke 36 | 10 % → 36 % | 50.6 px | 0.67 | 3.58 | 20 |
| stroke 37 | 18 % → 56 % | 100.0 px | 0.68 | 3.12 | 19 |
| stroke 38 | 16 % → 35 % | 78.9 px | 0.66 | 2.13 | 24 |
| stroke 39 | 26 % → 49 % | 145.2 px | 0.67 | 1.87 | 26 |
| stroke 40 | 29 % → 51 % | 209.0 px | 0.67 | 1.73 | 23 |
| stroke 41 | 32 % → 51 % | 509.5 px | 0.67 | 1.60 | 10 |
| stroke 42 | 28 % → 45 % | 543.1 px | 0.67 | 1.58 | 13 |
| stroke 43 | 24 % → 45 % | 139.3 px | 0.67 | 1.85 | 28 |
| stroke 44 | 25 % → 47 % | 143.9 px | 0.67 | 1.86 | 22 |
| stroke 45 | 20 % → 38 % | 247.8 px | 0.68 | 1.89 | 6 |
| stroke 46 | 27 % → 55 % | 246.3 px | 0.68 | 2.02 | 13 |
| stroke 47 | 35 % → 50 % | 115.3 px | 0.68 | 1.43 | 48 |
| stroke 48 | 28 % → 41 % | 357.7 px | 0.67 | 1.48 | 16 |
| stroke 49 | 29 % → 41 % | 320.6 px | 0.68 | 1.43 | 9 |
| stroke 50 | 30 % → 38 % | 356.5 px | 0.67 | 1.29 | 8 |
| stroke 51 | 35 % → 45 % | 190.5 px | 0.68 | 1.30 | 26 |
| stroke 52 | 18 % → 50 % | 238.0 px | 0.68 | 2.72 | 41 |
| stroke 53 | 9 % → 45 % | 177.1 px | 0.65 | 4.90 | 6 |
| stroke 54 | 5 % → 50 % | 29.5 px | 0.67 | 10.11 | 41 |
| stroke 55 | 5 % → 51 % | 35.0 px | 0.68 | 10.93 | 15 |
| stroke 56 | 9 % → 44 % | 44.0 px | 0.66 | 4.83 | 31 |
| stroke 57 | 14 % → 41 % | 107.0 px | 0.69 | 2.96 | 24 |
| stroke 58 | 11 % → 56 % | 82.4 px | 0.67 | 5.26 | 20 |
| stroke 59 | 27 % → 55 % | 242.6 px | 0.69 | 2.08 | 94 |
| stroke 60 | 11 % → 43 % | 83.1 px | 0.68 | 3.94 | 8 |
| stroke 61 | 10 % → 37 % | 65.8 px | 0.68 | 3.66 | 11 |
| stroke 62 | 32 % → 55 % | 377.0 px | 0.68 | 1.70 | 4 |
| stroke 63 | 14 % → 49 % | 162.4 px | 0.68 | 3.43 | 5 |
| stroke 64 | 15 % → 53 % | 108.0 px | 0.68 | 3.54 | 9 |
| stroke 65 | 27 % → 52 % | 113.1 px | 0.68 | 1.94 | 32 |
| stroke 66 | 11 % → 51 % | 146.1 px | 0.68 | 4.51 | 4 |
| stroke 67 | 19 % → 48 % | 115.5 px | 0.68 | 2.51 | 17 |
| stroke 68 | 31 % → 49 % | 251.1 px | 0.68 | 1.61 | 24 |
| stroke 69 | 36 % → 45 % | 289.7 px | 0.68 | 1.25 | 13 |
| stroke 70 | 17 % → 48 % | 260.5 px | 0.66 | 2.88 | 2 |
| stroke 71 | 30 % → 47 % | 388.1 px | 0.67 | 1.57 | 6 |
| stroke 72 | 19 % → 51 % | 110.7 px | 0.67 | 2.67 | 34 |
| stroke 73 | 27 % → 45 % | 417.4 px | 0.67 | 1.69 | 7 |
| stroke 74 | 23 % → 53 % | 116.6 px | 0.67 | 2.27 | 29 |
| stroke 75 | 24 % → 55 % | 211.9 px | 0.67 | 2.30 | 20 |
| stroke 76 | 37 % → 50 % | 132.9 px | 0.66 | 1.33 | 30 |
| stroke 77 | 36 % → 44 % | 191.4 px | 0.68 | 1.24 | 33 |
| stroke 78 | 28 % → 41 % | 125.1 px | 0.67 | 1.46 | 31 |
| stroke 79 | 33 % → 48 % | 186.1 px | 0.67 | 1.43 | 18 |
| stroke 80 | 29 % → 48 % | 268.6 px | 0.67 | 1.65 | 5 |
| stroke 81 | 32 % → 45 % | 174.9 px | 0.68 | 1.42 | 11 |
| stroke 82 | 27 % → 54 % | 97.7 px | 0.68 | 2.03 | 38 |
| stroke 83 | 39 % → 46 % | 372.6 px | 0.68 | 1.19 | 10 |
| stroke 84 | 39 % → 46 % | 708.3 px | 0.66 | 1.19 | 3 |
| stroke 85 | 32 % → 61 % | 238.9 px | 0.69 | 1.92 | 9 |
| stroke 86 | 36 % → 55 % | 255.6 px | 0.68 | 1.54 | 17 |
| stroke 87 | 20 % → 50 % | 108.0 px | 0.68 | 2.49 | 19 |
| stroke 88 | 20 % → 49 % | 292.2 px | 0.68 | 2.51 | 5 |
| stroke 89 | 26 % → 49 % | 95.9 px | 0.68 | 1.90 | 47 |
| stroke 90 | 28 % → 49 % | 225.0 px | 0.68 | 1.74 | 11 |
| stroke 91 | 40 % → 50 % | 358.7 px | 0.68 | 1.26 | 24 |
| stroke 92 | 30 % → 62 % | 249.0 px | 0.68 | 2.05 | 3 |
| stroke 93 | 7 % → 58 % | 38.8 px | 0.68 | 8.68 | 37 |
| stroke 94 | 24 % → 59 % | 147.9 px | 0.69 | 2.47 | 24 |
| stroke 95 | 33 % → 62 % | 240.1 px | 0.68 | 1.85 | 5 |
| stroke 96 | 27 % → 55 % | 413.1 px | 0.69 | 2.07 | 8 |
| stroke 97 | 17 % → 48 % | 117.5 px | 0.68 | 2.76 | 9 |
| stroke 98 | 29 % → 53 % | 313.5 px | 0.69 | 1.84 | 4 |
| stroke 99 | 28 % → 50 % | 148.7 px | 0.68 | 1.82 | 35 |
| stroke 100 | 46 % → 59 % | 248.6 px | 0.68 | 1.28 | 9 |
| stroke 101 | 15 % → 45 % | 124.5 px | 0.69 | 3.08 | 20 |
| stroke 102 | 12 % → 44 % | 92.6 px | 0.68 | 3.60 | 35 |
| stroke 103 | 16 % → 42 % | 189.3 px | 0.68 | 2.68 | 5 |
| stroke 104 | 32 % → 52 % | 228.2 px | 0.69 | 1.64 | 10 |
| stroke 105 | 23 % → 52 % | 250.0 px | 0.69 | 2.25 | 6 |
| stroke 106 | 17 % → 56 % | 180.9 px | 0.69 | 3.40 | 8 |
| stroke 107 | 18 % → 41 % | 101.2 px | 0.68 | 2.26 | 21 |
| stroke 108 | 32 % → 50 % | 278.5 px | 0.69 | 1.55 | 12 |
| stroke 109 | 27 % → 46 % | 128.5 px | 0.68 | 1.68 | 21 |
| stroke 110 | 28 % → 53 % | 397.1 px | 0.69 | 1.90 | 4 |
| stroke 111 | 33 % → 47 % | 509.8 px | 0.69 | 1.42 | 12 |
| stroke 112 | 37 % → 48 % | 640.7 px | 0.69 | 1.30 | 6 |
| stroke 113 | 32 % → 46 % | 431.0 px | 0.69 | 1.43 | 13 |
| stroke 114 | 39 % → 45 % | 612.4 px | 0.68 | 1.13 | 8 |
| stroke 115 | 34 % → 42 % | 308.6 px | 0.69 | 1.26 | 15 |
| stroke 116 | 4 % → 55 % | 21.9 px | 0.67 | 15.49 | 13 |
| stroke 117 | 29 % → 58 % | 171.8 px | 0.68 | 1.98 | 27 |
| stroke 118 | 31 % → 55 % | 529.9 px | 0.68 | 1.79 | 3 |
| stroke 119 | 27 % → 63 % | 369.7 px | 0.69 | 2.35 | 11 |
| stroke 120 | 6 % → 46 % | 95.4 px | 0.68 | 7.93 | 5 |
| stroke 121 | 7 % → 57 % | 34.9 px | 0.68 | 7.97 | 36 |
| stroke 122 | 13 % → 35 % | 45.2 px | 0.67 | 2.70 | 34 |
| stroke 123 | 17 % → 57 % | 111.4 px | 0.68 | 3.38 | 16 |
| stroke 124 | 16 % → 55 % | 113.7 px | 0.67 | 3.51 | 18 |
| stroke 125 | 4 % → 51 % | 32.6 px | 0.66 | 12.69 | 11 |
| stroke 126 | 10 % → 51 % | 67.5 px | 0.67 | 4.88 | 39 |
| stroke 127 | 18 % → 60 % | 75.9 px | 0.67 | 3.39 | 26 |
| stroke 128 | 12 % → 56 % | 86.0 px | 0.67 | 4.62 | 11 |
| stroke 129 | 30 % → 60 % | 329.0 px | 0.68 | 2.00 | 9 |
| stroke 130 | 19 % → 51 % | 124.0 px | 0.68 | 2.64 | 20 |
| stroke 131 | 25 % → 58 % | 144.4 px | 0.67 | 2.33 | 18 |
| stroke 132 | 32 % → 54 % | 242.7 px | 0.68 | 1.70 | 18 |
| stroke 133 | 23 % → 52 % | 96.5 px | 0.67 | 2.23 | 47 |
| stroke 134 | 23 % → 49 % | 138.3 px | 0.68 | 2.12 | 12 |
| stroke 135 | 19 % → 53 % | 305.2 px | 0.68 | 2.80 | 12 |
| stroke 136 | 33 % → 55 % | 170.0 px | 0.68 | 1.67 | 27 |
| stroke 137 | 42 % → 57 % | 766.2 px | 0.68 | 1.33 | 7 |
| stroke 138 | 32 % → 55 % | 267.1 px | 0.67 | 1.76 | 15 |
| stroke 139 | 37 % → 55 % | 271.2 px | 0.68 | 1.49 | 12 |
| stroke 140 | 36 % → 58 % | 471.6 px | 0.68 | 1.63 | 5 |
| stroke 141 | 37 % → 61 % | 404.1 px | 0.67 | 1.66 | 10 |
| stroke 142 | 34 % → 49 % | 181.3 px | 0.68 | 1.45 | 20 |
| stroke 143 | 38 % → 58 % | 522.6 px | 0.69 | 1.52 | 6 |
| stroke 144 | 43 % → 58 % | 300.6 px | 0.69 | 1.34 | 17 |
| stroke 145 | 47 % → 57 % | 335.3 px | 0.69 | 1.23 | 21 |
| stroke 146 | 46 % → 55 % | 353.2 px | 0.68 | 1.20 | 18 |
| stroke 147 | 51 % → 54 % | 211.3 px | 0.68 | 1.07 | 28 |
| stroke 148 | 37 % → 45 % | 700.6 px | 0.68 | 1.23 | 3 |
| stroke 149 | 6 % → 41 % | 67.1 px | 0.67 | 6.54 | 11 |
| stroke 150 | 15 % → 46 % | 105.8 px | 0.68 | 3.11 | 14 |
| stroke 151 | 7 % → 49 % | 40.1 px | 0.68 | 6.75 | 11 |
| stroke 152 | 21 % → 48 % | 134.4 px | 0.67 | 2.25 | 21 |
| stroke 153 | 45 % → 57 % | 261.7 px | 0.68 | 1.27 | 20 |
| stroke 154 | 32 % → 51 % | 78.8 px | 0.68 | 1.61 | 65 |
| stroke 155 | 48 % → 60 % | 568.4 px | 0.68 | 1.26 | 5 |
| stroke 156 | 22 % → 44 % | 191.5 px | 0.68 | 2.03 | 5 |
| stroke 157 | 21 % → 46 % | 127.1 px | 0.68 | 2.24 | 52 |
| stroke 158 | 21 % → 46 % | 170.3 px | 0.68 | 2.14 | 17 |
| stroke 159 | 37 % → 47 % | 163.3 px | 0.68 | 1.28 | 17 |
| stroke 160 | 28 % → 44 % | 152.5 px | 0.67 | 1.56 | 30 |
| stroke 161 | 33 % → 46 % | 152.1 px | 0.67 | 1.38 | 28 |
| stroke 162 | 9 % → 49 % | 73.4 px | 0.67 | 5.63 | 25 |
| stroke 163 | 1 % → 53 % | 15.2 px | 0.67 | 37.76 | 8 |
| stroke 164 | 18 % → 53 % | 151.1 px | 0.68 | 2.96 | 11 |
| stroke 165 | 19 % → 52 % | 157.1 px | 0.68 | 2.80 | 11 |
| stroke 166 | 48 % → 59 % | 301.0 px | 0.68 | 1.22 | 40 |
| stroke 167 | 24 % → 56 % | 319.1 px | 0.67 | 2.38 | 22 |
| stroke 168 | 3 % → 62 % | 42.9 px | 0.68 | 21.70 | 2 |
| stroke 169 | 3 % → 69 % | 14.4 px | 0.69 | 25.09 | 9 |
| stroke 170 | 3 % → 56 % | 31.5 px | 0.67 | 16.50 | 4 |
| stroke 171 | 8 % → 55 % | 60.0 px | 0.67 | 6.82 | 8 |
| stroke 172 | 46 % → 56 % | 437.6 px | 0.68 | 1.21 | 12 |
| stroke 173 | 8 % → 58 % | 37.0 px | 0.68 | 7.31 | 33 |
| stroke 174 | 16 % → 64 % | 80.2 px | 0.68 | 3.98 | 8 |
| stroke 175 | 6 % → 51 % | 52.6 px | 0.67 | 9.17 | 6 |
| stroke 176 | 8 % → 51 % | 60.2 px | 0.67 | 6.68 | 8 |
| stroke 177 | 12 % → 54 % | 88.3 px | 0.68 | 4.35 | 10 |
| stroke 178 | 30 % → 55 % | 100.2 px | 0.68 | 1.83 | 27 |
| stroke 179 | 16 % → 54 % | 123.7 px | 0.67 | 3.27 | 27 |
| stroke 180 | 19 % → 50 % | 176.2 px | 0.68 | 2.64 | 9 |
| stroke 181 | 30 % → 47 % | 295.9 px | 0.67 | 1.60 | 12 |
| stroke 182 | 25 % → 49 % | 208.8 px | 0.67 | 1.94 | 6 |
| stroke 183 | 15 % → 62 % | 215.9 px | 0.68 | 4.18 | 2 |
| stroke 184 | 19 % → 56 % | 168.3 px | 0.68 | 2.88 | 13 |
| stroke 185 | 27 % → 48 % | 324.2 px | 0.67 | 1.79 | 3 |
| stroke 186 | 32 % → 64 % | 85.7 px | 0.68 | 2.02 | 17 |
| stroke 187 | 19 % → 48 % | 216.1 px | 0.68 | 2.54 | 12 |
| stroke 188 | 39 % → 52 % | 169.8 px | 0.67 | 1.32 | 25 |
| stroke 189 | 26 % → 63 % | 51.9 px | 0.69 | 2.41 | 41 |
| stroke 190 | 39 % → 52 % | 288.8 px | 0.68 | 1.34 | 17 |
| stroke 191 | 27 % → 51 % | 202.9 px | 0.67 | 1.87 | 13 |
| stroke 192 | 33 % → 55 % | 247.7 px | 0.67 | 1.67 | 20 |
| stroke 193 | 44 % → 52 % | 413.2 px | 0.68 | 1.20 | 16 |
| stroke 194 | 31 % → 56 % | 196.7 px | 0.68 | 1.80 | 18 |
| stroke 195 | 39 % → 55 % | 289.0 px | 0.67 | 1.40 | 24 |
| stroke 196 | 41 % → 55 % | 176.2 px | 0.67 | 1.34 | 14 |
| stroke 197 | 35 % → 46 % | 67.5 px | 0.66 | 1.32 | 62 |
| stroke 198 | 23 % → 50 % | 109.0 px | 0.67 | 2.17 | 13 |
| stroke 199 | 27 % → 45 % | 351.4 px | 0.67 | 1.64 | 22 |
| stroke 200 | 36 % → 47 % | 180.2 px | 0.67 | 1.30 | 18 |
| stroke 201 | 33 % → 44 % | 244.5 px | 0.67 | 1.33 | 16 |
| stroke 202 | 37 % → 47 % | 270.8 px | 0.67 | 1.28 | 4 |
| stroke 203 | 36 % → 44 % | 418.9 px | 0.67 | 1.23 | 4 |
| stroke 204 | 43 % → 48 % | 218.4 px | 0.67 | 1.12 | 5 |
| stroke 205 | 2 % → 44 % | 25.4 px | 0.67 | 22.50 | 4 |
| stroke 206 | 26 % → 56 % | 122.9 px | 0.67 | 2.15 | 19 |
| stroke 207 | 18 % → 53 % | 141.1 px | 0.67 | 2.90 | 13 |
| stroke 208 | 2 % → 61 % | 14.0 px | 0.67 | 31.07 | 7 |
| stroke 209 | 12 % → 43 % | 51.1 px | 0.67 | 3.59 | 12 |
| stroke 210 | 10 % → 53 % | 62.4 px | 0.66 | 5.29 | 10 |
| stroke 211 | 8 % → 54 % | 78.8 px | 0.67 | 6.82 | 13 |
| stroke 212 | 15 % → 57 % | 40.5 px | 0.67 | 3.75 | 35 |
| stroke 213 | 24 % → 60 % | 97.1 px | 0.67 | 2.46 | 32 |
| stroke 214 | 21 % → 53 % | 343.1 px | 0.66 | 2.48 | 3 |
| stroke 215 | 28 % → 56 % | 398.2 px | 0.66 | 2.04 | 3 |
| stroke 216 | 22 % → 54 % | 140.0 px | 0.67 | 2.45 | 11 |
| stroke 217 | 33 % → 59 % | 292.4 px | 0.67 | 1.78 | 9 |
| stroke 218 | 39 % → 56 % | 179.3 px | 0.67 | 1.41 | 21 |
| stroke 219 | 34 % → 55 % | 291.3 px | 0.66 | 1.60 | 27 |
| stroke 220 | 40 % → 54 % | 628.3 px | 0.67 | 1.34 | 3 |
| stroke 221 | 37 % → 55 % | 257.3 px | 0.67 | 1.49 | 17 |
| stroke 222 | 45 % → 53 % | 358.5 px | 0.67 | 1.16 | 8 |
| stroke 223 | 44 % → 60 % | 348.3 px | 0.67 | 1.37 | 20 |
| stroke 224 | 16 % → 43 % | 112.9 px | 0.67 | 2.75 | 17 |
| stroke 225 | 19 % → 48 % | 150.6 px | 0.67 | 2.56 | 18 |
| stroke 226 | 33 % → 50 % | 148.7 px | 0.67 | 1.51 | 38 |
| stroke 227 | 28 % → 50 % | 240.3 px | 0.67 | 1.79 | 7 |
| stroke 228 | 13 % → 44 % | 158.6 px | 0.67 | 3.47 | 7 |
| stroke 229 | 28 % → 44 % | 156.3 px | 0.67 | 1.58 | 17 |
| stroke 230 | 29 % → 52 % | 105.9 px | 0.68 | 1.80 | 24 |
| stroke 231 | 23 % → 49 % | 189.7 px | 0.66 | 2.14 | 15 |
| stroke 232 | 30 % → 52 % | 365.1 px | 0.67 | 1.72 | 6 |
| stroke 233 | 35 % → 52 % | 155.4 px | 0.67 | 1.50 | 21 |
| stroke 234 | 26 % → 59 % | 291.3 px | 0.68 | 2.28 | 6 |
| stroke 235 | 12 % → 40 % | 79.4 px | 0.67 | 3.38 | 16 |
| stroke 236 | 29 % → 54 % | 227.8 px | 0.68 | 1.86 | 14 |
| stroke 237 | 31 % → 51 % | 135.4 px | 0.68 | 1.65 | 33 |
| stroke 238 | 25 % → 43 % | 93.2 px | 0.67 | 1.73 | 27 |
| stroke 239 | 29 % → 46 % | 269.9 px | 0.68 | 1.62 | 17 |
| stroke 240 | 23 % → 43 % | 186.9 px | 0.68 | 1.90 | 8 |
| stroke 241 | 33 % → 47 % | 129.2 px | 0.68 | 1.40 | 24 |
| stroke 242 | 2 % → 46 % | 15.5 px | 0.66 | 24.86 | 30 |
| stroke 243 | 7 % → 53 % | 28.3 px | 0.68 | 7.43 | 69 |
| stroke 244 | 21 % → 58 % | 251.0 px | 0.68 | 2.84 | 8 |
| stroke 245 | 1 % → 31 % | 15.8 px | 0.66 | 25.94 | 5 |
| stroke 246 | 4 % → 40 % | 25.3 px | 0.68 | 9.55 | 22 |
| stroke 247 | 11 % → 38 % | 55.8 px | 0.66 | 3.55 | 31 |
| stroke 248 | 10 % → 29 % | 90.0 px | 0.66 | 2.94 | 8 |
| stroke 249 | 8 % → 34 % | 65.4 px | 0.65 | 4.34 | 15 |
| stroke 250 | 17 % → 58 % | 158.8 px | 0.68 | 3.48 | 19 |
| stroke 251 | 9 % → 44 % | 80.2 px | 0.66 | 5.01 | 60 |
| stroke 252 | 12 % → 57 % | 143.8 px | 0.67 | 4.87 | 4 |
| stroke 253 | 9 % → 60 % | 134.8 px | 0.67 | 6.98 | 5 |
| stroke 254 | 12 % → 51 % | 82.0 px | 0.67 | 4.29 | 21 |
| stroke 255 | 26 % → 52 % | 315.0 px | 0.68 | 1.98 | 3 |
| stroke 256 | 21 % → 49 % | 215.6 px | 0.68 | 2.38 | 21 |
| stroke 257 | 24 % → 50 % | 360.7 px | 0.68 | 2.05 | 8 |
| stroke 258 | 43 % → 59 % | 282.2 px | 0.69 | 1.38 | 16 |
| stroke 259 | 16 % → 59 % | 213.8 px | 0.67 | 3.63 | 3 |
| stroke 260 | 34 % → 57 % | 141.9 px | 0.68 | 1.65 | 20 |
| stroke 261 | 19 % → 52 % | 91.9 px | 0.67 | 2.70 | 20 |
| stroke 262 | 19 % → 49 % | 295.1 px | 0.67 | 2.62 | 5 |
| stroke 263 | 19 % → 48 % | 162.6 px | 0.67 | 2.53 | 11 |
| stroke 264 | 26 % → 51 % | 333.7 px | 0.68 | 1.95 | 5 |
| stroke 265 | 22 % → 43 % | 344.1 px | 0.66 | 1.96 | 2 |
| stroke 266 | 16 % → 28 % | 216.3 px | 0.66 | 1.73 | 3 |
| stroke 267 | 15 % → 30 % | 93.1 px | 0.65 | 1.97 | 21 |
| stroke 268 | 20 % → 46 % | 191.0 px | 0.67 | 2.25 | 26 |
| stroke 269 | 30 % → 55 % | 155.7 px | 0.67 | 1.82 | 16 |
| stroke 270 | 20 % → 30 % | 295.0 px | 0.66 | 1.51 | 4 |
| stroke 271 | 31 % → 49 % | 229.8 px | 0.67 | 1.57 | 35 |
| stroke 272 | 42 % → 58 % | 426.6 px | 0.68 | 1.38 | 8 |
| stroke 273 | 25 % → 44 % | 146.6 px | 0.66 | 1.75 | 27 |
| stroke 274 | 31 % → 35 % | 261.1 px | 0.65 | 1.14 | 15 |
| stroke 275 | 40 % → 53 % | 224.2 px | 0.68 | 1.35 | 26 |
| stroke 276 | 37 % → 50 % | 605.1 px | 0.67 | 1.34 | 2 |
| stroke 277 | 31 % → 43 % | 264.3 px | 0.66 | 1.38 | 11 |
| stroke 278 | 45 % → 55 % | 310.5 px | 0.67 | 1.22 | 9 |
| stroke 279 | 29 % → 46 % | 335.0 px | 0.67 | 1.57 | 5 |
| stroke 280 | 35 % → 47 % | 564.6 px | 0.67 | 1.37 | 7 |
| stroke 281 | 43 % → 49 % | 380.6 px | 0.66 | 1.15 | 14 |
| stroke 282 | 47 % → 50 % | 180.1 px | 0.67 | 1.07 | 27 |
| stroke 283 | 32 % → 51 % | 94.9 px | 0.66 | 1.57 | 53 |
| stroke 284 | 12 % → 38 % | 58.6 px | 0.65 | 3.20 | 10 |
| stroke 285 | 10 % → 33 % | 60.3 px | 0.65 | 3.23 | 15 |
| stroke 286 | 17 % → 32 % | 113.8 px | 0.64 | 1.88 | 5 |
| stroke 287 | 36 % → 45 % | 165.5 px | 0.65 | 1.25 | 38 |
| stroke 288 | 37 % → 45 % | 252.9 px | 0.65 | 1.21 | 5 |
| stroke 289 | 30 % → 50 % | 261.2 px | 0.67 | 1.67 | 12 |
| stroke 290 | 19 % → 53 % | 105.5 px | 0.68 | 2.83 | 9 |
| stroke 291 | 42 % → 61 % | 193.4 px | 0.69 | 1.47 | 26 |
| stroke 292 | 27 % → 56 % | 202.1 px | 0.70 | 2.07 | 6 |
| stroke 293 | 41 % → 59 % | 111.6 px | 0.69 | 1.41 | 26 |
| stroke 294 | 34 % → 51 % | 227.7 px | 0.69 | 1.51 | 19 |
| stroke 295 | 10 % → 31 % | 90.1 px | 0.67 | 3.16 | 8 |
| stroke 296 | 29 % → 34 % | 80.9 px | 0.68 | 1.20 | 60 |
| stroke 297 | 27 % → 68 % | 102.4 px | 0.69 | 2.48 | 9 |
| stroke 298 | 4 % → 36 % | 33.8 px | 0.67 | 8.43 | 16 |
| stroke 299 | 2 % → 26 % | 13.3 px | 0.66 | 11.93 | 7 |
| stroke 300 | 7 % → 28 % | 70.7 px | 0.67 | 4.23 | 7 |
| stroke 301 | 8 % → 26 % | 47.0 px | 0.66 | 3.10 | 6 |
| stroke 302 | 18 % → 42 % | 54.1 px | 0.67 | 2.39 | 29 |
| stroke 303 | 18 % → 37 % | 143.0 px | 0.67 | 2.04 | 11 |
| stroke 304 | 13 % → 31 % | 118.8 px | 0.67 | 2.36 | 6 |
| stroke 305 | 21 % → 42 % | 211.2 px | 0.67 | 1.99 | 10 |
| stroke 306 | 21 % → 40 % | 177.9 px | 0.67 | 1.88 | 18 |
| stroke 307 | 12 % → 27 % | 92.0 px | 0.66 | 2.30 | 7 |
| stroke 308 | 19 % → 34 % | 175.5 px | 0.66 | 1.82 | 11 |
| stroke 309 | 19 % → 33 % | 159.1 px | 0.66 | 1.73 | 8 |
| stroke 310 | 19 % → 25 % | 102.7 px | 0.66 | 1.32 | 17 |
| stroke 311 | 15 % → 40 % | 82.3 px | 0.66 | 2.66 | 14 |
| stroke 312 | 2 % → 31 % | 18.7 px | 0.66 | 18.54 | 7 |
| stroke 313 | 17 % → 41 % | 133.8 px | 0.67 | 2.44 | 11 |
| stroke 314 | 27 % → 41 % | 321.5 px | 0.66 | 1.55 | 3 |
| stroke 315 | 14 % → 40 % | 167.5 px | 0.66 | 2.94 | 3 |
| stroke 316 | 26 % → 40 % | 182.2 px | 0.66 | 1.55 | 18 |
| stroke 317 | 28 % → 41 % | 490.7 px | 0.67 | 1.46 | 7 |
| stroke 318 | 21 % → 37 % | 166.9 px | 0.66 | 1.75 | 6 |
| stroke 319 | 28 % → 37 % | 540.9 px | 0.66 | 1.32 | 3 |
| stroke 320 | 21 % → 36 % | 185.2 px | 0.66 | 1.73 | 14 |
| stroke 321 | 8 % → 39 % | 63.1 px | 0.66 | 4.92 | 36 |
| stroke 322 | 19 % → 56 % | 171.1 px | 0.67 | 2.97 | 9 |
| stroke 323 | 7 % → 52 % | 46.4 px | 0.67 | 7.34 | 18 |
| stroke 324 | 27 % → 54 % | 55.9 px | 0.68 | 1.98 | 48 |
| stroke 325 | 32 % → 56 % | 214.6 px | 0.68 | 1.75 | 11 |
| stroke 326 | 31 % → 50 % | 237.4 px | 0.67 | 1.63 | 11 |
| stroke 327 | 20 % → 47 % | 78.8 px | 0.67 | 2.40 | 23 |
| stroke 328 | 25 % → 44 % | 93.6 px | 0.66 | 1.77 | 24 |
| stroke 329 | 31 % → 49 % | 180.7 px | 0.67 | 1.59 | 21 |
| stroke 330 | 19 % → 47 % | 57.2 px | 0.66 | 2.44 | 60 |
| stroke 331 | 40 % → 51 % | 424.7 px | 0.68 | 1.29 | 9 |
| stroke 332 | 38 % → 48 % | 246.7 px | 0.66 | 1.27 | 13 |
| stroke 333 | 6 % → 49 % | 47.3 px | 0.67 | 7.62 | 24 |
| stroke 334 | 6 % → 51 % | 54.7 px | 0.68 | 8.05 | 10 |
| stroke 335 | 9 % → 58 % | 68.4 px | 0.68 | 6.67 | 29 |
| stroke 336 | 2 % → 44 % | 16.1 px | 0.67 | 17.62 | 7 |
| stroke 337 | 6 % → 51 % | 42.2 px | 0.68 | 7.82 | 24 |
| stroke 338 | 12 % → 49 % | 149.1 px | 0.68 | 4.19 | 10 |
| stroke 339 | 26 % → 52 % | 221.7 px | 0.68 | 1.99 | 10 |
| stroke 340 | 13 % → 66 % | 101.8 px | 0.69 | 5.09 | 25 |
| stroke 341 | 31 % → 51 % | 180.0 px | 0.68 | 1.67 | 32 |
| stroke 342 | 9 % → 60 % | 96.0 px | 0.67 | 6.77 | 14 |
| stroke 343 | 20 % → 58 % | 161.6 px | 0.68 | 2.93 | 9 |
| stroke 344 | 24 % → 60 % | 384.7 px | 0.68 | 2.56 | 4 |
| stroke 345 | 21 % → 59 % | 178.6 px | 0.67 | 2.87 | 20 |
| stroke 346 | 29 % → 59 % | 410.3 px | 0.68 | 2.03 | 12 |
| stroke 347 | 33 % → 53 % | 107.7 px | 0.66 | 1.63 | 24 |
| stroke 348 | 39 % → 52 % | 245.4 px | 0.68 | 1.32 | 26 |
| stroke 349 | 41 % → 51 % | 253.3 px | 0.68 | 1.25 | 31 |
| stroke 350 | 38 % → 54 % | 337.5 px | 0.67 | 1.43 | 16 |
| stroke 351 | 35 % → 52 % | 304.7 px | 0.67 | 1.47 | 17 |
| stroke 352 | 37 % → 58 % | 632.7 px | 0.67 | 1.56 | 16 |
| stroke 353 | 30 % → 44 % | 271.0 px | 0.67 | 1.46 | 31 |
| stroke 354 | 12 % → 44 % | 76.9 px | 0.67 | 3.64 | 27 |
| stroke 355 | 25 % → 48 % | 214.1 px | 0.67 | 1.89 | 7 |
| stroke 356 | 6 % → 31 % | 29.1 px | 0.68 | 4.96 | 16 |
| stroke 357 | 21 % → 46 % | 84.8 px | 0.67 | 2.26 | 39 |
| stroke 358 | 8 % → 38 % | 42.7 px | 0.67 | 4.48 | 19 |
| stroke 359 | 15 % → 35 % | 107.3 px | 0.67 | 2.42 | 15 |
| stroke 360 | 18 % → 45 % | 219.5 px | 0.68 | 2.47 | 7 |
| stroke 361 | 21 % → 45 % | 387.6 px | 0.68 | 2.08 | 8 |
| stroke 362 | 21 % → 43 % | 146.6 px | 0.67 | 2.03 | 16 |
| stroke 363 | 20 % → 40 % | 312.1 px | 0.67 | 1.98 | 14 |
| stroke 364 | 27 % → 46 % | 205.1 px | 0.68 | 1.75 | 16 |
| stroke 365 | 25 % → 35 % | 298.6 px | 0.68 | 1.36 | 9 |
| stroke 366 | 33 % → 41 % | 239.2 px | 0.67 | 1.24 | 19 |
| stroke 367 | 18 % → 59 % | 53.3 px | 0.68 | 3.32 | 11 |
| stroke 368 | 5 % → 68 % | 18.4 px | 0.69 | 14.54 | 11 |
| stroke 369 | 19 % → 51 % | 101.6 px | 0.67 | 2.69 | 12 |
| stroke 370 | 9 % → 52 % | 84.8 px | 0.67 | 5.52 | 21 |
| stroke 371 | 12 % → 46 % | 211.8 px | 0.66 | 3.81 | 7 |
| stroke 372 | 13 % → 52 % | 124.3 px | 0.67 | 4.00 | 11 |
| stroke 373 | 21 % → 47 % | 83.7 px | 0.67 | 2.30 | 28 |
| stroke 374 | 26 % → 52 % | 146.5 px | 0.67 | 2.02 | 5 |
| stroke 375 | 20 % → 46 % | 176.0 px | 0.66 | 2.29 | 8 |
| stroke 376 | 34 % → 53 % | 311.0 px | 0.67 | 1.55 | 2 |
| stroke 377 | 29 % → 46 % | 96.8 px | 0.66 | 1.62 | 26 |
| stroke 378 | 8 % → 45 % | 46.9 px | 0.67 | 5.36 | 10 |
| stroke 379 | 27 % → 51 % | 110.0 px | 0.68 | 1.89 | 37 |
| stroke 380 | 13 % → 49 % | 76.9 px | 0.67 | 3.91 | 10 |
| stroke 381 | 13 % → 44 % | 51.1 px | 0.66 | 3.49 | 12 |
| stroke 382 | 30 % → 47 % | 102.2 px | 0.67 | 1.58 | 33 |
| stroke 383 | 25 % → 47 % | 160.8 px | 0.66 | 1.87 | 15 |
| stroke 384 | 31 % → 48 % | 197.9 px | 0.66 | 1.54 | 11 |
| stroke 385 | 7 % → 62 % | 29.3 px | 0.69 | 9.24 | 10 |
| stroke 386 | 16 % → 45 % | 65.6 px | 0.67 | 2.88 | 42 |
| stroke 387 | 4 % → 50 % | 31.2 px | 0.68 | 12.35 | 5 |
| stroke 388 | 37 % → 62 % | 72.9 px | 0.68 | 1.68 | 27 |
| stroke 389 | 21 % → 52 % | 89.3 px | 0.68 | 2.44 | 9 |
| stroke 390 | 9 % → 57 % | 147.3 px | 0.69 | 6.25 | 3 |
| stroke 391 | 29 % → 56 % | 100.9 px | 0.68 | 1.92 | 31 |
| stroke 392 | 25 % → 53 % | 79.3 px | 0.67 | 2.16 | 42 |
| stroke 393 | 29 % → 51 % | 150.5 px | 0.68 | 1.80 | 48 |
| stroke 394 | 34 % → 58 % | 188.8 px | 0.68 | 1.69 | 24 |
| stroke 395 | 22 % → 46 % | 70.0 px | 0.67 | 2.12 | 35 |
| stroke 396 | 37 % → 56 % | 307.2 px | 0.68 | 1.51 | 18 |
| stroke 397 | 43 % → 53 % | 774.0 px | 0.69 | 1.24 | 9 |
| stroke 398 | 25 % → 45 % | 467.6 px | 0.67 | 1.82 | 2 |
| stroke 399 | 31 % → 53 % | 266.7 px | 0.68 | 1.71 | 6 |
| stroke 400 | 48 % → 58 % | 202.9 px | 0.68 | 1.21 | 40 |
| stroke 401 | 43 % → 54 % | 127.8 px | 0.68 | 1.25 | 25 |
| stroke 402 | 41 % → 53 % | 363.0 px | 0.68 | 1.29 | 22 |
| stroke 403 | 46 % → 52 % | 282.3 px | 0.69 | 1.12 | 13 |
| stroke 404 | 62 % → 67 % | 1191.3 px | 0.68 | 1.08 | 2 |
| stroke 405 | 13 % → 41 % | 106.6 px | 0.66 | 3.20 | 6 |
| stroke 406 | 29 % → 43 % | 91.4 px | 0.67 | 1.47 | 58 |
| stroke 407 | 33 % → 48 % | 160.8 px | 0.67 | 1.43 | 43 |
| stroke 408 | 34 % → 48 % | 87.4 px | 0.67 | 1.39 | 27 |
| stroke 409 | 38 % → 47 % | 107.8 px | 0.68 | 1.25 | 11 |
| stroke 410 | 50 % → 58 % | 323.9 px | 0.68 | 1.17 | 2 |
| stroke 411 | 25 % → 44 % | 160.2 px | 0.66 | 1.80 | 6 |
| stroke 412 | 30 % → 46 % | 209.0 px | 0.67 | 1.56 | 6 |
| stroke 413 | 33 % → 44 % | 232.6 px | 0.67 | 1.32 | 6 |
| stroke 414 | 31 % → 42 % | 219.5 px | 0.66 | 1.34 | 6 |
| stroke 415 | 34 % → 42 % | 341.2 px | 0.67 | 1.25 | 4 |
| stroke 416 | 34 % → 41 % | 242.2 px | 0.67 | 1.21 | 8 |
| stroke 417 | 38 % → 45 % | 228.3 px | 0.67 | 1.20 | 8 |
| stroke 418 | 39 % → 43 % | 215.1 px | 0.67 | 1.11 | 7 |
| stroke 419 | 47 % → 52 % | 366.1 px | 0.68 | 1.12 | 4 |
| stroke 420 | 35 % → 40 % | 117.2 px | 0.67 | 1.15 | 8 |

Numbers say: wet paint spreads well beyond the stroke.

## Refs v3 · #16 Shrigley strokes — own sheet
own sheet 800 × 1000 · Watercolour 1.00 + water 30 % · 64 px · 99.4 s

![Refs v3 · #16 Shrigley strokes — own sheet](Refs-v3-16-Shrigley-strokes-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 6 % → 65 % | 33.2 px | 0.25 | 11.17 | 37 |
| stroke 2 | 4 % → 49 % | 45.6 px | 0.20 | 13.64 | 18 |
| stroke 3 | 7 % → 55 % | 80.4 px | 0.20 | 8.33 | 30 |
| stroke 4 | 10 % → 72 % | 44.9 px | 0.25 | 7.05 | 165 |
| stroke 5 | 3 % → 52 % | 27.9 px | 0.18 | 20.34 | 17 |
| stroke 6 | 7 % → 69 % | 121.3 px | 0.23 | 9.33 | 24 |
| stroke 7 | 8 % → 59 % | 54.5 px | 0.20 | 7.60 | 256 |
| stroke 8 | 14 % → 64 % | 113.5 px | 0.21 | 4.40 | 85 |
| stroke 9 | 18 % → 57 % | 323.7 px | 0.19 | 3.12 | 37 |
| stroke 10 | 14 % → 62 % | 73.2 px | 0.22 | 4.56 | 337 |
| stroke 11 | 10 % → 61 % | 82.4 px | 0.22 | 6.18 | 119 |
| stroke 12 | 15 % → 53 % | 75.2 px | 0.19 | 3.57 | 241 |
| stroke 13 | 8 % → 59 % | 40.0 px | 0.21 | 7.50 | 350 |
| stroke 14 | 8 % → 61 % | 78.7 px | 0.23 | 7.62 | 149 |
| stroke 15 | 24 % → 54 % | 121.1 px | 0.20 | 2.27 | 148 |
| stroke 16 | 12 % → 49 % | 86.9 px | 0.23 | 4.10 | 108 |
| stroke 17 | 27 % → 52 % | 246.1 px | 0.23 | 1.90 | 88 |
| stroke 18 | 11 % → 51 % | 131.9 px | 0.23 | 4.70 | 34 |
| stroke 19 | 10 % → 50 % | 45.0 px | 0.23 | 5.01 | 254 |
| stroke 20 | 15 % → 52 % | 155.3 px | 0.23 | 3.53 | 102 |
| stroke 21 | 16 % → 54 % | 193.3 px | 0.23 | 3.40 | 26 |
| stroke 22 | 14 % → 57 % | 71.0 px | 0.23 | 4.21 | 222 |
| stroke 23 | 22 % → 53 % | 118.6 px | 0.23 | 2.44 | 310 |
| stroke 24 | 17 % → 56 % | 104.1 px | 0.24 | 3.33 | 70 |
| stroke 25 | 25 % → 72 % | 100.6 px | 0.24 | 2.91 | 124 |
| stroke 26 | 29 % → 74 % | 165.6 px | 0.25 | 2.52 | 69 |
| stroke 27 | 24 % → 54 % | 127.9 px | 0.20 | 2.28 | 330 |
| stroke 28 | 23 % → 60 % | 180.8 px | 0.19 | 2.56 | 45 |
| stroke 29 | 28 % → 61 % | 249.5 px | 0.19 | 2.19 | 45 |
| stroke 30 | 19 % → 62 % | 590.7 px | 0.24 | 3.30 | 10 |
| stroke 31 | 27 % → 71 % | 308.4 px | 0.21 | 2.61 | 44 |
| stroke 32 | 28 % → 70 % | 681.8 px | 0.20 | 2.51 | 11 |
| stroke 33 | 33 % → 67 % | 255.0 px | 0.20 | 2.02 | 128 |
| stroke 34 | 27 % → 57 % | 214.0 px | 0.19 | 2.08 | 166 |
| stroke 35 | 40 % → 61 % | 266.0 px | 0.18 | 1.52 | 77 |
| stroke 36 | 36 % → 54 % | 403.7 px | 0.20 | 1.48 | 101 |
| stroke 37 | 41 % → 63 % | 288.2 px | 0.19 | 1.54 | 148 |
| stroke 38 | 38 % → 60 % | 209.0 px | 0.19 | 1.57 | 103 |
| stroke 39 | 44 % → 56 % | 400.8 px | 0.20 | 1.28 | 82 |
| stroke 40 | 31 % → 58 % | 356.5 px | 0.20 | 1.85 | 44 |
| stroke 41 | 27 % → 56 % | 244.9 px | 0.22 | 2.07 | 147 |
| stroke 42 | 33 % → 58 % | 491.3 px | 0.23 | 1.72 | 30 |
| stroke 43 | 23 % → 58 % | 132.4 px | 0.20 | 2.47 | 501 |
| stroke 44 | 25 % → 49 % | 200.2 px | 0.23 | 1.94 | 184 |
| stroke 45 | 36 % → 57 % | 484.9 px | 0.22 | 1.58 | 45 |
| stroke 46 | 27 % → 60 % | 282.8 px | 0.20 | 2.18 | 32 |
| stroke 47 | 31 % → 49 % | 746.7 px | 0.22 | 1.61 | 14 |
| stroke 48 | 24 % → 47 % | 294.0 px | 0.22 | 1.95 | 40 |
| stroke 49 | 32 % → 51 % | 342.8 px | 0.21 | 1.59 | 45 |
| stroke 50 | 36 % → 53 % | 297.2 px | 0.21 | 1.46 | 170 |
| stroke 51 | 30 % → 64 % | 410.3 px | 0.21 | 2.13 | 28 |
| stroke 52 | 32 % → 64 % | 426.6 px | 0.19 | 2.01 | 50 |
| stroke 53 | 35 % → 62 % | 1043.1 px | 0.19 | 1.78 | 16 |
| stroke 54 | 26 % → 49 % | 271.4 px | 0.23 | 1.87 | 37 |
| stroke 55 | 21 % → 47 % | 587.0 px | 0.23 | 2.26 | 11 |
| stroke 56 | 33 % → 62 % | 178.3 px | 0.23 | 1.90 | 176 |
| stroke 57 | 27 % → 52 % | 154.9 px | 0.24 | 1.93 | 80 |
| stroke 58 | 27 % → 52 % | 479.2 px | 0.24 | 1.92 | 12 |
| stroke 59 | 19 % → 55 % | 335.6 px | 0.24 | 2.88 | 12 |
| stroke 60 | 37 % → 53 % | 127.3 px | 0.26 | 1.42 | 85 |
| stroke 61 | 32 % → 53 % | 1119.8 px | 0.19 | 1.66 | 7 |
| stroke 62 | 45 % → 60 % | 249.5 px | 0.22 | 1.33 | 478 |
| stroke 63 | 55 % → 58 % | 204.6 px | 0.19 | 1.05 | 256 |
| stroke 64 | 48 % → 57 % | 425.1 px | 0.22 | 1.20 | 72 |
| stroke 65 | 63 % → 70 % | 268.2 px | 0.23 | 1.12 | 272 |
| stroke 66 | 37 % → 48 % | 1235.2 px | 0.18 | 1.31 | 9 |
| stroke 67 | 48 % → 53 % | 341.7 px | 0.19 | 1.11 | 139 |
| stroke 68 | 52 % → 52 % | 1170.9 px | 0.17 | 1.00 | 26 |
| stroke 69 | 50 % → 59 % | 311.1 px | 0.20 | 1.17 | 95 |
| stroke 70 | 45 % → 57 % | 241.8 px | 0.21 | 1.28 | 95 |
| stroke 71 | 40 % → 52 % | 180.6 px | 0.21 | 1.28 | 513 |
| stroke 72 | 36 % → 50 % | 791.6 px | 0.21 | 1.36 | 25 |
| stroke 73 | 35 % → 52 % | 513.1 px | 0.21 | 1.49 | 35 |
| stroke 74 | 51 % → 58 % | 408.2 px | 0.22 | 1.14 | 140 |
| stroke 75 | 34 % → 58 % | 303.3 px | 0.24 | 1.71 | 101 |
| stroke 76 | 34 % → 51 % | 225.5 px | 0.25 | 1.49 | 81 |
| stroke 77 | 31 % → 52 % | 210.3 px | 0.25 | 1.65 | 146 |
| stroke 78 | 66 % → 70 % | 271.2 px | 0.24 | 1.06 | 295 |
| stroke 79 | 48 % → 54 % | 653.1 px | 0.21 | 1.14 | 43 |
| stroke 80 | 59 % → 63 % | 658.4 px | 0.21 | 1.07 | 56 |
| stroke 81 | 59 % → 63 % | 719.0 px | 0.19 | 1.06 | 13 |
| stroke 82 | 68 % → 70 % | 922.7 px | 0.21 | 1.03 | 46 |
| stroke 83 | 59 % → 60 % | 549.1 px | 0.19 | 1.01 | 40 |
| stroke 84 | 62 % → 62 % | 1204.0 px | 0.17 | 1.01 | 20 |
| stroke 85 | 46 % → 52 % | 374.4 px | 0.23 | 1.13 | 147 |
| stroke 86 | 44 % → 51 % | 1334.8 px | 0.20 | 1.16 | 9 |
| stroke 87 | 52 % → 57 % | 1067.0 px | 0.23 | 1.10 | 24 |
| stroke 88 | 52 % → 52 % | 542.8 px | 0.22 | 1.00 | 130 |
| stroke 89 | 52 % → 55 % | 348.4 px | 0.21 | 1.05 | 175 |
| stroke 90 | 35 % → 44 % | 1137.1 px | 0.23 | 1.25 | 8 |
| stroke 91 | 34 % → 42 % | 971.0 px | 0.24 | 1.26 | 10 |
| stroke 92 | 51 % → 53 % | 263.1 px | 0.22 | 1.02 | 472 |
| stroke 93 | 48 % → 49 % | 217.6 px | 0.24 | 1.01 | 110 |
| stroke 94 | 53 % → 54 % | 205.1 px | 0.24 | 1.01 | 165 |

Numbers say: wet paint spreads well beyond the stroke.

## Refs v3 · #17 Krovostok dry brush — own sheet
own sheet 800 × 720 · Ink 0.93 · Gouache 0.07 · 16 px · 101.9 s

![Refs v3 · #17 Krovostok dry brush — own sheet](Refs-v3-17-Krovostok-dry-brush-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 5 % → 17 % | 21.3 px | 0.37 | 3.77 | 49 |
| stroke 2 | 8 % → 8 % | 25.9 px | 0.35 | 1.10 | 7 |
| stroke 3 | 13 % → 34 % | 44.2 px | 0.38 | 2.60 | 14 |
| stroke 4 | 4 % → 43 % | 19.7 px | 0.42 | 10.47 | 5 |
| stroke 5 | 10 % → 59 % | 32.4 px | 0.42 | 6.13 | 13 |
| stroke 6 | 17 % → 9 % | 24.8 px | 0.38 | 0.54 | 53 |
| stroke 7 | 14 % → 55 % | 37.9 px | 0.42 | 4.06 | 11 |
| stroke 8 | 17 % → 0 % | 57.5 px | 0.00 | 0.00 | 5 |
| stroke 9 | 28 % → 7 % | 64.1 px | 0.37 | 0.26 | 75 |
| stroke 10 | 26 % → 34 % | 116.9 px | 0.41 | 1.31 | 6 |
| stroke 11 | 23 % → 55 % | 62.2 px | 0.42 | 2.41 | 6 |
| stroke 12 | 36 % → 26 % | 65.0 px | 0.41 | 0.72 | 55 |
| stroke 13 | 35 % → 52 % | 96.9 px | 0.42 | 1.49 | 12 |
| stroke 14 | 40 % → 32 % | 57.5 px | 0.43 | 0.81 | 63 |
| stroke 15 | 42 % → 56 % | 209.5 px | 0.43 | 1.34 | 6 |
| stroke 16 | 4 % → 12 % | 18.7 px | 0.40 | 3.21 | 10 |
| stroke 17 | 42 % → 45 % | 113.5 px | 0.44 | 1.06 | 18 |
| stroke 18 | 43 % → 37 % | 145.0 px | 0.44 | 0.87 | 5 |
| stroke 19 | 8 % → 3 % | 38.0 px | 0.37 | 0.35 | 2 |
| stroke 20 | 38 % → 33 % | 104.4 px | 0.44 | 0.87 | 33 |
| stroke 21 | 12 % → 0 % | 52.4 px | 0.20 | 0.01 | 8 |
| stroke 22 | 35 % → 31 % | 81.5 px | 0.44 | 0.89 | 24 |
| stroke 23 | 16 % → 0 % | 54.1 px | 0.20 | 0.00 | 12 |
| stroke 24 | 28 % → 27 % | 93.7 px | 0.44 | 0.98 | 7 |
| stroke 25 | 18 % → 0 % | 35.1 px | 0.00 | 0.00 | 43 |
| stroke 26 | 23 % → 0 % | 42.2 px | 0.00 | 0.00 | 23 |
| stroke 27 | 20 % → 1 % | 46.8 px | 0.46 | 0.07 | 10 |
| stroke 28 | 20 % → 9 % | 49.2 px | 0.43 | 0.45 | 30 |
| stroke 29 | 5 % → 2 % | 19.0 px | 0.47 | 0.45 | 6 |
| stroke 30 | 5 % → 29 % | 19.9 px | 0.43 | 6.20 | 7 |
| stroke 31 | 8 % → 27 % | 21.9 px | 0.43 | 3.28 | 12 |
| stroke 32 | 13 % → 27 % | 32.3 px | 0.43 | 2.16 | 18 |
| stroke 33 | 17 % → 33 % | 77.6 px | 0.43 | 1.95 | 3 |
| stroke 34 | 37 % → 1 % | 174.4 px | 0.47 | 0.03 | 6 |
| stroke 35 | 42 % → 0 % | 147.2 px | 0.00 | 0.00 | 5 |
| stroke 36 | 45 % → 0 % | 214.4 px | 0.00 | 0.00 | 3 |
| stroke 37 | 5 % → 13 % | 24.9 px | 0.44 | 2.32 | 7 |
| stroke 38 | 13 % → 13 % | 45.5 px | 0.44 | 1.01 | 6 |
| stroke 39 | 20 % → 15 % | 69.9 px | 0.44 | 0.74 | 7 |
| stroke 40 | 28 % → 18 % | 135.5 px | 0.43 | 0.63 | 2 |
| stroke 41 | 35 % → 23 % | 132.3 px | 0.43 | 0.66 | 4 |
| stroke 42 | 7 % → 11 % | 21.1 px | 0.41 | 1.58 | 11 |
| stroke 43 | 13 % → 12 % | 38.7 px | 0.41 | 0.88 | 8 |
| stroke 44 | 24 % → 14 % | 86.5 px | 0.42 | 0.57 | 11 |
| stroke 45 | 29 % → 10 % | 84.7 px | 0.43 | 0.36 | 6 |
| stroke 46 | 7 % → 15 % | 17.4 px | 0.44 | 2.24 | 11 |
| stroke 47 | 12 % → 17 % | 33.4 px | 0.43 | 1.39 | 6 |
| stroke 48 | 16 % → 23 % | 77.6 px | 0.43 | 1.43 | 5 |
| stroke 49 | 4 % → 15 % | 20.9 px | 0.40 | 3.28 | 2 |
| stroke 50 | 10 % → 15 % | 33.3 px | 0.40 | 1.48 | 9 |
| stroke 51 | 7 % → 29 % | 25.8 px | 0.41 | 3.94 | 7 |
| stroke 52 | 12 % → 29 % | 59.3 px | 0.41 | 2.44 | 5 |
| stroke 53 | 8 % → 0 % | 12.0 px | 0.00 | 0.00 | 5 |
| stroke 54 | 13 % → 0 % | 13.4 px | 0.00 | 0.00 | 7 |
| stroke 55 | 2 % → 0 % | 9.0 px | 0.00 | 0.00 | 2 |
| stroke 56 | 9 % → 0 % | 31.4 px | 0.00 | 0.00 | 11 |
| stroke 57 | 6 % → 24 % | 12.1 px | 0.41 | 4.01 | 26 |
| stroke 58 | 7 % → 1 % | 23.2 px | 0.51 | 0.11 | 3 |
| stroke 59 | 8 % → 0 % | 18.6 px | 0.00 | 0.00 | 6 |
| stroke 60 | 10 % → 25 % | 28.1 px | 0.43 | 2.64 | 7 |
| stroke 61 | 15 % → 26 % | 34.9 px | 0.43 | 1.75 | 4 |
| stroke 62 | 13 % → 18 % | 27.1 px | 0.43 | 1.35 | 5 |
| stroke 63 | 32 % → 21 % | 72.5 px | 0.42 | 0.65 | 12 |
| stroke 64 | 7 % → 9 % | 13.5 px | 0.39 | 1.16 | 34 |
| stroke 65 | 5 % → 22 % | 12.2 px | 0.41 | 4.06 | 4 |
| stroke 66 | 7 % → 22 % | 13.4 px | 0.41 | 3.07 | 6 |
| stroke 67 | 12 % → 10 % | 26.6 px | 0.40 | 0.85 | 10 |
| stroke 68 | 12 % → 13 % | 34.6 px | 0.43 | 1.05 | 13 |
| stroke 69 | 8 % → 22 % | 14.4 px | 0.40 | 2.93 | 6 |
| stroke 70 | 4 % → 12 % | 10.0 px | 0.42 | 2.88 | 7 |
| stroke 71 | 6 % → 6 % | 10.3 px | 0.45 | 1.00 | 13 |
| stroke 72 | 9 % → 0 % | 17.6 px | 0.00 | 0.00 | 5 |
| stroke 73 | 24 % → 19 % | 37.5 px | 0.39 | 0.76 | 34 |
| stroke 74 | 35 % → 22 % | 79.8 px | 0.40 | 0.62 | 16 |
| stroke 75 | 13 % → 17 % | 42.9 px | 0.42 | 1.34 | 10 |
| stroke 76 | 29 % → 12 % | 49.7 px | 0.42 | 0.43 | 52 |
| stroke 77 | 36 % → 25 % | 53.0 px | 0.42 | 0.69 | 61 |
| stroke 78 | 38 % → 3 % | 54.3 px | 0.41 | 0.08 | 50 |
| stroke 79 | 19 % → 12 % | 34.9 px | 0.40 | 0.64 | 19 |
| stroke 80 | 33 % → 25 % | 104.4 px | 0.43 | 0.78 | 12 |
| stroke 81 | 41 % → 3 % | 71.2 px | 0.38 | 0.08 | 43 |
| stroke 82 | 25 % → 17 % | 83.4 px | 0.42 | 0.70 | 8 |
| stroke 83 | 34 % → 12 % | 45.7 px | 0.42 | 0.36 | 64 |
| stroke 84 | 32 % → 24 % | 87.9 px | 0.42 | 0.73 | 20 |
| stroke 85 | 46 % → 8 % | 68.8 px | 0.41 | 0.16 | 114 |
| stroke 86 | 45 % → 10 % | 60.7 px | 0.42 | 0.22 | 55 |
| stroke 87 | 31 % → 23 % | 103.6 px | 0.41 | 0.75 | 8 |
| stroke 88 | 51 % → 6 % | 76.7 px | 0.40 | 0.11 | 55 |
| stroke 89 | 46 % → 6 % | 54.5 px | 0.42 | 0.13 | 117 |
| stroke 90 | 62 % → 8 % | 66.5 px | 0.43 | 0.12 | 177 |
| stroke 91 | 49 % → 10 % | 135.8 px | 0.44 | 0.20 | 11 |
| stroke 92 | 64 % → 6 % | 78.6 px | 0.43 | 0.09 | 137 |
| stroke 93 | 65 % → 8 % | 136.3 px | 0.44 | 0.12 | 34 |
| stroke 94 | 44 % → 19 % | 102.0 px | 0.41 | 0.43 | 15 |
| stroke 95 | 62 % → 10 % | 92.2 px | 0.44 | 0.16 | 64 |
| stroke 96 | 65 % → 11 % | 85.2 px | 0.42 | 0.17 | 71 |
| stroke 97 | 55 % → 15 % | 95.2 px | 0.44 | 0.27 | 39 |
| stroke 98 | 59 % → 0 % | 157.2 px | 0.00 | 0.00 | 24 |
| stroke 99 | 59 % → 14 % | 98.3 px | 0.42 | 0.23 | 67 |
| stroke 100 | 59 % → 16 % | 64.3 px | 0.44 | 0.27 | 130 |
| stroke 101 | 57 % → 17 % | 60.6 px | 0.43 | 0.31 | 163 |
| stroke 102 | 29 % → 24 % | 65.7 px | 0.41 | 0.81 | 26 |
| stroke 103 | 58 % → 20 % | 61.4 px | 0.43 | 0.34 | 252 |
| stroke 104 | 36 % → 22 % | 118.1 px | 0.41 | 0.62 | 8 |
| stroke 105 | 15 % → 7 % | 49.0 px | 0.38 | 0.50 | 5 |
| stroke 106 | 50 % → 37 % | 77.6 px | 0.44 | 0.73 | 50 |
| stroke 107 | 62 % → 7 % | 76.3 px | 0.41 | 0.11 | 128 |
| stroke 108 | 24 % → 3 % | 81.5 px | 0.34 | 0.14 | 18 |
| stroke 109 | 51 % → 32 % | 74.7 px | 0.44 | 0.63 | 77 |
| stroke 110 | 58 % → 8 % | 79.3 px | 0.39 | 0.14 | 55 |
| stroke 111 | 34 % → 0 % | 78.1 px | 0.14 | 0.00 | 18 |
| stroke 112 | 45 % → 27 % | 76.6 px | 0.44 | 0.61 | 51 |
| stroke 113 | 55 % → 7 % | 74.6 px | 0.39 | 0.13 | 71 |
| stroke 114 | 28 % → 18 % | 93.4 px | 0.39 | 0.66 | 13 |
| stroke 115 | 37 % → 0 % | 65.2 px | 0.00 | 0.00 | 65 |
| stroke 116 | 47 % → 24 % | 65.2 px | 0.43 | 0.51 | 103 |
| stroke 117 | 42 % → 6 % | 110.0 px | 0.40 | 0.14 | 8 |
| stroke 118 | 60 % → 1 % | 124.2 px | 0.41 | 0.02 | 24 |
| stroke 119 | 54 % → 9 % | 56.3 px | 0.44 | 0.18 | 164 |
| stroke 120 | 59 % → 9 % | 69.6 px | 0.44 | 0.15 | 82 |
| stroke 121 | 59 % → 14 % | 102.3 px | 0.44 | 0.24 | 34 |
| stroke 122 | 21 % → 13 % | 48.7 px | 0.39 | 0.61 | 14 |
| stroke 123 | 64 % → 4 % | 70.7 px | 0.44 | 0.07 | 102 |
| stroke 124 | 58 % → 3 % | 64.8 px | 0.44 | 0.05 | 112 |
| stroke 125 | 50 % → 1 % | 78.2 px | 0.45 | 0.01 | 62 |
| stroke 126 | 60 % → 5 % | 71.0 px | 0.43 | 0.09 | 110 |
| stroke 127 | 56 % → 7 % | 59.0 px | 0.44 | 0.12 | 145 |
| stroke 128 | 33 % → 0 % | 110.9 px | 0.00 | 0.00 | 17 |
| stroke 129 | 65 % → 12 % | 82.6 px | 0.44 | 0.18 | 150 |
| stroke 130 | 57 % → 11 % | 87.5 px | 0.42 | 0.19 | 48 |
| stroke 131 | 63 % → 15 % | 119.4 px | 0.43 | 0.25 | 53 |
| stroke 132 | 43 % → 12 % | 73.3 px | 0.42 | 0.28 | 34 |
| stroke 133 | 50 % → 17 % | 171.6 px | 0.43 | 0.34 | 8 |
| stroke 134 | 44 % → 14 % | 89.8 px | 0.42 | 0.31 | 24 |
| stroke 135 | 25 % → 0 % | 86.5 px | 0.00 | 0.00 | 6 |
| stroke 136 | 42 % → 13 % | 134.4 px | 0.43 | 0.31 | 5 |
| stroke 137 | 42 % → 12 % | 73.6 px | 0.42 | 0.28 | 32 |
| stroke 138 | 46 % → 12 % | 125.3 px | 0.43 | 0.26 | 8 |
| stroke 139 | 30 % → 11 % | 69.0 px | 0.42 | 0.37 | 10 |
| stroke 140 | 24 % → 14 % | 54.4 px | 0.42 | 0.57 | 29 |
| stroke 141 | 44 % → 5 % | 76.7 px | 0.44 | 0.11 | 35 |
| stroke 142 | 34 % → 0 % | 91.4 px | 0.43 | 0.00 | 18 |
| stroke 143 | 49 % → 15 % | 99.8 px | 0.43 | 0.31 | 32 |
| stroke 144 | 48 % → 4 % | 97.4 px | 0.43 | 0.08 | 20 |
| stroke 145 | 24 % → 0 % | 78.2 px | 0.00 | 0.00 | 8 |
| stroke 146 | 41 % → 4 % | 106.5 px | 0.45 | 0.10 | 22 |
| stroke 147 | 40 % → 0 % | 82.1 px | 0.49 | 0.01 | 24 |
| stroke 148 | 41 % → 0 % | 135.4 px | 0.00 | 0.00 | 8 |
| stroke 149 | 51 % → 21 % | 89.3 px | 0.43 | 0.42 | 24 |
| stroke 150 | 52 % → 12 % | 118.8 px | 0.42 | 0.23 | 43 |
| stroke 151 | 55 % → 12 % | 61.4 px | 0.42 | 0.22 | 164 |
| stroke 152 | 61 % → 17 % | 139.3 px | 0.43 | 0.27 | 28 |
| stroke 153 | 65 % → 32 % | 149.1 px | 0.42 | 0.50 | 36 |
| stroke 154 | 60 % → 18 % | 207.2 px | 0.42 | 0.30 | 13 |
| stroke 155 | 20 % → 2 % | 37.1 px | 0.37 | 0.08 | 57 |
| stroke 156 | 23 % → 4 % | 42.4 px | 0.39 | 0.15 | 136 |
| stroke 157 | 39 % → 5 % | 70.2 px | 0.39 | 0.12 | 78 |
| stroke 158 | 34 % → 0 % | 72.8 px | 0.42 | 0.01 | 52 |
| stroke 159 | 35 % → 0 % | 124.4 px | 0.00 | 0.00 | 48 |
| stroke 160 | 41 % → 3 % | 74.1 px | 0.39 | 0.08 | 355 |
| stroke 161 | 35 % → 0 % | 123.2 px | 0.00 | 0.00 | 28 |
| stroke 162 | 44 % → 4 % | 82.8 px | 0.39 | 0.08 | 393 |
| stroke 163 | 41 % → 0 % | 148.1 px | 0.00 | 0.00 | 11 |
| stroke 164 | 63 % → 10 % | 133.7 px | 0.40 | 0.16 | 33 |
| stroke 165 | 56 % → 5 % | 106.2 px | 0.40 | 0.10 | 119 |
| stroke 166 | 42 % → 11 % | 148.2 px | 0.39 | 0.27 | 15 |
| stroke 167 | 53 % → 12 % | 159.2 px | 0.40 | 0.23 | 8 |
| stroke 168 | 60 % → 10 % | 214.1 px | 0.39 | 0.16 | 9 |
| stroke 169 | 63 % → 0 % | 228.5 px | 0.00 | 0.00 | 10 |
| stroke 170 | 50 % → 10 % | 120.2 px | 0.37 | 0.19 | 16 |
| stroke 171 | 42 % → 11 % | 109.4 px | 0.37 | 0.25 | 16 |
| stroke 172 | 44 % → 0 % | 153.9 px | 0.43 | 0.00 | 20 |
| stroke 173 | 40 % → 10 % | 105.1 px | 0.37 | 0.25 | 23 |
| stroke 174 | 28 % → 9 % | 81.1 px | 0.44 | 0.34 | 12 |
| stroke 175 | 34 % → 0 % | 120.8 px | 0.00 | 0.00 | 10 |
| stroke 176 | 44 % → 8 % | 130.2 px | 0.35 | 0.18 | 38 |
| stroke 177 | 46 % → 8 % | 83.1 px | 0.42 | 0.17 | 116 |
| stroke 178 | 44 % → 4 % | 98.4 px | 0.36 | 0.09 | 37 |
| stroke 179 | 43 % → 24 % | 100.2 px | 0.43 | 0.56 | 19 |
| stroke 180 | 53 % → 6 % | 191.5 px | 0.45 | 0.11 | 9 |
| stroke 181 | 51 % → 4 % | 92.8 px | 0.43 | 0.08 | 97 |
| stroke 182 | 59 % → 30 % | 135.3 px | 0.43 | 0.52 | 30 |
| stroke 183 | 51 % → 4 % | 92.7 px | 0.44 | 0.08 | 148 |
| stroke 184 | 70 % → 28 % | 259.0 px | 0.43 | 0.40 | 15 |
| stroke 185 | 55 % → 0 % | 164.1 px | 0.00 | 0.00 | 23 |
| stroke 186 | 56 % → 6 % | 113.1 px | 0.44 | 0.11 | 38 |
| stroke 187 | 61 % → 5 % | 109.8 px | 0.42 | 0.08 | 89 |
| stroke 188 | 69 % → 3 % | 138.3 px | 0.46 | 0.04 | 50 |
| stroke 189 | 59 % → 11 % | 214.0 px | 0.42 | 0.18 | 6 |
| stroke 190 | 68 % → 7 % | 137.1 px | 0.40 | 0.10 | 58 |
| stroke 191 | 6 % → 48 % | 22.9 px | 0.41 | 7.81 | 6 |
| stroke 192 | 6 % → 10 % | 14.9 px | 0.45 | 1.66 | 7 |
| stroke 193 | 18 % → 17 % | 39.2 px | 0.43 | 0.91 | 9 |
| stroke 194 | 25 % → 14 % | 45.3 px | 0.42 | 0.57 | 20 |
| stroke 195 | 13 % → 3 % | 47.2 px | 0.36 | 0.23 | 4 |
| stroke 196 | 8 % → 0 % | 19.1 px | 0.00 | 0.00 | 17 |
| stroke 197 | 13 % → 0 % | 37.8 px | 0.00 | 0.00 | 8 |
| stroke 198 | 17 % → 0 % | 36.7 px | 0.00 | 0.00 | 22 |
| stroke 199 | 23 % → 0 % | 108.1 px | 0.00 | 0.00 | 7 |
| stroke 200 | 26 % → 0 % | 72.4 px | 0.00 | 0.00 | 18 |
| stroke 201 | 32 % → 0 % | 114.5 px | 0.00 | 0.00 | 15 |
| stroke 202 | 33 % → 0 % | 145.3 px | 0.00 | 0.00 | 10 |
| stroke 203 | 6 % → 20 % | 20.7 px | 0.41 | 3.55 | 9 |
| stroke 204 | 6 % → 27 % | 23.5 px | 0.43 | 4.25 | 43 |
| stroke 205 | 10 % → 17 % | 46.2 px | 0.41 | 1.76 | 9 |
| stroke 206 | 9 % → 32 % | 40.2 px | 0.43 | 3.70 | 16 |
| stroke 207 | 14 % → 12 % | 51.3 px | 0.40 | 0.84 | 6 |
| stroke 208 | 21 % → 9 % | 54.5 px | 0.41 | 0.43 | 10 |
| stroke 209 | 13 % → 0 % | 60.7 px | 0.41 | 0.01 | 33 |
| stroke 210 | 26 % → 3 % | 76.1 px | 0.42 | 0.13 | 19 |
| stroke 211 | 22 % → 0 % | 104.3 px | 0.00 | 0.00 | 14 |
| stroke 212 | 34 % → 3 % | 122.1 px | 0.41 | 0.08 | 14 |
| stroke 213 | 30 % → 0 % | 112.7 px | 0.00 | 0.00 | 21 |
| stroke 214 | 32 % → 1 % | 83.7 px | 0.41 | 0.02 | 28 |
| stroke 215 | 41 % → 0 % | 203.2 px | 0.00 | 0.00 | 10 |
| stroke 216 | 40 % → 0 % | 189.2 px | 0.00 | 0.00 | 3 |
| stroke 217 | 38 % → 0 % | 112.9 px | 0.00 | 0.00 | 14 |
| stroke 218 | 4 % → 15 % | 19.4 px | 0.41 | 3.76 | 5 |
| stroke 219 | 11 % → 25 % | 51.4 px | 0.42 | 2.21 | 17 |
| stroke 220 | 13 % → 6 % | 37.0 px | 0.42 | 0.46 | 20 |
| stroke 221 | 17 % → 1 % | 79.7 px | 0.40 | 0.05 | 10 |
| stroke 222 | 28 % → 10 % | 128.7 px | 0.43 | 0.35 | 5 |
| stroke 223 | 20 % → 2 % | 100.5 px | 0.45 | 0.11 | 5 |
| stroke 224 | 28 % → 4 % | 94.9 px | 0.43 | 0.16 | 17 |
| stroke 225 | 6 % → 2 % | 28.6 px | 0.46 | 0.29 | 10 |
| stroke 226 | 11 % → 3 % | 37.4 px | 0.46 | 0.28 | 13 |
| stroke 227 | 15 % → 7 % | 35.6 px | 0.43 | 0.48 | 16 |
| stroke 228 | 24 % → 6 % | 116.2 px | 0.43 | 0.24 | 6 |
| stroke 229 | 17 % → 13 % | 37.8 px | 0.44 | 0.72 | 27 |
| stroke 230 | 25 % → 12 % | 55.0 px | 0.42 | 0.48 | 33 |
| stroke 231 | 26 % → 8 % | 63.3 px | 0.44 | 0.31 | 25 |
| stroke 232 | 34 % → 18 % | 63.0 px | 0.43 | 0.52 | 55 |
| stroke 233 | 34 % → 12 % | 93.6 px | 0.44 | 0.34 | 20 |
| stroke 234 | 38 % → 21 % | 93.4 px | 0.44 | 0.56 | 22 |
| stroke 235 | 35 % → 15 % | 160.6 px | 0.43 | 0.43 | 15 |
| stroke 236 | 37 % → 16 % | 182.1 px | 0.43 | 0.42 | 5 |
| stroke 237 | 37 % → 18 % | 170.3 px | 0.43 | 0.49 | 9 |
| stroke 238 | 32 % → 0 % | 134.8 px | 0.00 | 0.00 | 3 |
| stroke 239 | 38 % → 0 % | 131.7 px | 0.00 | 0.00 | 5 |
| stroke 240 | 37 % → 0 % | 94.1 px | 0.62 | 0.00 | 18 |
| stroke 241 | 31 % → 1 % | 140.6 px | 0.51 | 0.03 | 6 |
| stroke 242 | 34 % → 2 % | 73.5 px | 0.46 | 0.07 | 18 |
| stroke 243 | 33 % → 5 % | 165.4 px | 0.46 | 0.15 | 9 |
| stroke 244 | 6 % → 0 % | 23.9 px | 0.61 | 0.01 | 10 |
| stroke 245 | 14 % → 1 % | 61.4 px | 0.39 | 0.08 | 8 |
| stroke 246 | 18 % → 3 % | 50.9 px | 0.40 | 0.15 | 11 |
| stroke 247 | 26 % → 5 % | 128.2 px | 0.38 | 0.20 | 3 |
| stroke 248 | 29 % → 7 % | 137.8 px | 0.38 | 0.25 | 10 |
| stroke 249 | 19 % → 0 % | 95.5 px | 0.63 | 0.00 | 6 |
| stroke 250 | 13 % → 0 % | 65.2 px | 0.63 | 0.00 | 6 |
| stroke 251 | 17 % → 2 % | 61.8 px | 0.47 | 0.12 | 6 |
| stroke 252 | 25 % → 9 % | 61.4 px | 0.44 | 0.38 | 33 |
| stroke 253 | 6 % → 0 % | 21.0 px | 0.39 | 0.03 | 4 |
| stroke 254 | 19 % → 0 % | 57.9 px | 0.57 | 0.01 | 17 |
| stroke 255 | 12 % → 2 % | 58.0 px | 0.26 | 0.16 | 7 |
| stroke 256 | 25 % → 0 % | 66.2 px | 0.61 | 0.00 | 13 |
| stroke 257 | 33 % → 4 % | 79.2 px | 0.43 | 0.12 | 20 |
| stroke 258 | 35 % → 13 % | 74.3 px | 0.43 | 0.38 | 51 |
| stroke 259 | 33 % → 7 % | 68.7 px | 0.43 | 0.20 | 51 |
| stroke 260 | 40 % → 4 % | 97.9 px | 0.41 | 0.11 | 47 |
| stroke 261 | 13 % → 10 % | 48.3 px | 0.40 | 0.74 | 9 |
| stroke 262 | 21 % → 9 % | 64.7 px | 0.40 | 0.42 | 11 |
| stroke 263 | 25 % → 7 % | 55.5 px | 0.39 | 0.28 | 71 |
| stroke 264 | 37 % → 4 % | 101.8 px | 0.40 | 0.12 | 34 |
| stroke 265 | 50 % → 1 % | 183.6 px | 0.45 | 0.01 | 14 |
| stroke 266 | 4 % → 19 % | 19.0 px | 0.40 | 5.09 | 7 |
| stroke 267 | 11 % → 12 % | 20.5 px | 0.41 | 1.04 | 32 |
| stroke 268 | 20 % → 5 % | 69.1 px | 0.40 | 0.26 | 12 |
| stroke 269 | 23 % → 3 % | 81.8 px | 0.40 | 0.14 | 7 |
| stroke 270 | 24 % → 1 % | 115.1 px | 0.42 | 0.04 | 2 |
| stroke 271 | 9 % → 25 % | 21.0 px | 0.41 | 2.68 | 31 |
| stroke 272 | 15 % → 26 % | 40.5 px | 0.41 | 1.69 | 22 |
| stroke 273 | 23 % → 21 % | 115.1 px | 0.41 | 0.92 | 12 |
| stroke 274 | 21 % → 0 % | 76.1 px | 0.00 | 0.00 | 4 |
| stroke 275 | 17 % → 0 % | 63.3 px | 0.00 | 0.00 | 8 |
| stroke 276 | 5 % → 21 % | 26.2 px | 0.41 | 3.95 | 4 |
| stroke 277 | 11 % → 29 % | 39.3 px | 0.41 | 2.60 | 6 |
| stroke 278 | 15 % → 25 % | 44.5 px | 0.41 | 1.66 | 8 |
| stroke 279 | 19 % → 21 % | 69.6 px | 0.40 | 1.10 | 9 |
| stroke 280 | 7 % → 7 % | 23.8 px | 0.42 | 1.02 | 9 |
| stroke 281 | 15 % → 13 % | 35.1 px | 0.40 | 0.90 | 23 |
| stroke 282 | 10 % → 17 % | 23.8 px | 0.43 | 1.69 | 17 |
| stroke 283 | 19 % → 11 % | 53.4 px | 0.38 | 0.59 | 22 |
| stroke 284 | 17 % → 14 % | 35.0 px | 0.43 | 0.81 | 20 |
| stroke 285 | 32 % → 12 % | 155.5 px | 0.45 | 0.36 | 8 |
| stroke 286 | 36 % → 3 % | 168.4 px | 0.46 | 0.09 | 5 |
| stroke 287 | 38 % → 1 % | 180.6 px | 0.36 | 0.02 | 5 |
| stroke 288 | 24 % → 15 % | 86.6 px | 0.42 | 0.62 | 8 |
| stroke 289 | 27 % → 13 % | 70.9 px | 0.42 | 0.48 | 24 |
| stroke 290 | 33 % → 6 % | 158.2 px | 0.42 | 0.18 | 6 |
| stroke 291 | 12 % → 20 % | 17.5 px | 0.40 | 1.63 | 24 |
| stroke 292 | 9 % → 22 % | 16.7 px | 0.43 | 2.37 | 31 |
| stroke 293 | 10 % → 21 % | 34.9 px | 0.43 | 2.04 | 8 |
| stroke 294 | 20 % → 27 % | 77.2 px | 0.43 | 1.35 | 6 |
| stroke 295 | 12 % → 13 % | 35.1 px | 0.39 | 1.05 | 16 |
| stroke 296 | 10 % → 19 % | 25.4 px | 0.43 | 1.95 | 28 |
| stroke 297 | 9 % → 21 % | 19.2 px | 0.43 | 2.48 | 18 |
| stroke 298 | 11 % → 23 % | 41.1 px | 0.43 | 2.00 | 5 |
| stroke 299 | 22 % → 24 % | 55.9 px | 0.43 | 1.12 | 7 |
| stroke 300 | 7 % → 12 % | 22.2 px | 0.44 | 1.64 | 16 |
| stroke 301 | 17 % → 34 % | 43.7 px | 0.42 | 2.08 | 6 |
| stroke 302 | 19 % → 22 % | 36.6 px | 0.42 | 1.16 | 30 |
| stroke 303 | 7 % → 8 % | 27.2 px | 0.44 | 1.16 | 7 |
| stroke 304 | 8 % → 17 % | 24.7 px | 0.44 | 2.24 | 10 |
| stroke 305 | 12 % → 29 % | 22.9 px | 0.42 | 2.48 | 67 |
| stroke 306 | 26 % → 34 % | 26.6 px | 0.41 | 1.31 | 47 |
| stroke 307 | 6 % → 10 % | 16.6 px | 0.37 | 1.56 | 13 |
| stroke 308 | 9 % → 14 % | 21.5 px | 0.42 | 1.60 | 23 |
| stroke 309 | 6 % → 11 % | 21.4 px | 0.44 | 1.85 | 8 |
| stroke 310 | 14 % → 24 % | 51.0 px | 0.43 | 1.74 | 12 |
| stroke 311 | 7 % → 14 % | 21.4 px | 0.43 | 2.06 | 5 |
| stroke 312 | 6 % → 17 % | 18.7 px | 0.40 | 2.88 | 7 |
| stroke 313 | 16 % → 23 % | 54.4 px | 0.41 | 1.42 | 9 |
| stroke 314 | 5 % → 23 % | 17.7 px | 0.41 | 4.21 | 8 |
| stroke 315 | 10 % → 24 % | 32.7 px | 0.41 | 2.45 | 4 |
| stroke 316 | 15 % → 21 % | 43.5 px | 0.41 | 1.38 | 18 |
| stroke 317 | 9 % → 20 % | 18.8 px | 0.40 | 2.12 | 20 |
| stroke 318 | 9 % → 14 % | 22.3 px | 0.39 | 1.60 | 6 |
| stroke 319 | 10 % → 13 % | 20.3 px | 0.39 | 1.32 | 20 |
| stroke 320 | 9 % → 16 % | 17.8 px | 0.42 | 1.85 | 14 |
| stroke 321 | 17 % → 25 % | 39.6 px | 0.41 | 1.50 | 25 |
| stroke 322 | 26 % → 31 % | 76.7 px | 0.41 | 1.17 | 6 |
| stroke 323 | 5 % → 19 % | 16.1 px | 0.43 | 3.98 | 8 |
| stroke 324 | 15 % → 18 % | 42.1 px | 0.43 | 1.19 | 19 |

Numbers say: wet paint spreads well beyond the stroke.

## Refs v3 · #18 Twombly blue sticks — own sheet
own sheet 800 × 789 · Wax 1.00 · 19 px · 21.6 s

![Refs v3 · #18 Twombly blue sticks — own sheet](Refs-v3-18-Twombly-blue-sticks-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 4 % → 28 % | 20.9 px | 0.35 | 7.76 | 2 |
| stroke 2 | 6 % → 8 % | 34.1 px | 0.34 | 1.43 | 1 |
| stroke 3 | 6 % → 22 % | 16.0 px | 0.35 | 3.76 | 3 |
| stroke 4 | 11 % → 6 % | 26.1 px | 0.33 | 0.55 | 10 |
| stroke 5 | 10 % → 14 % | 40.8 px | 0.34 | 1.40 | 3 |
| stroke 6 | 13 % → 15 % | 75.2 px | 0.34 | 1.15 | 1 |
| stroke 7 | 14 % → 23 % | 47.0 px | 0.34 | 1.61 | 12 |
| stroke 8 | 18 % → 10 % | 75.2 px | 0.34 | 0.60 | 6 |
| stroke 9 | 11 % → 34 % | 45.3 px | 0.34 | 3.08 | 3 |
| stroke 10 | 14 % → 41 % | 82.9 px | 0.35 | 2.88 | 1 |
| stroke 11 | 18 % → 41 % | 50.3 px | 0.35 | 2.34 | 7 |
| stroke 12 | 16 % → 31 % | 28.0 px | 0.35 | 1.94 | 6 |
| stroke 13 | 5 % → 0 % | 19.0 px | 0.00 | 0.00 | 2 |
| stroke 14 | 24 % → 32 % | 130.9 px | 0.34 | 1.35 | 1 |
| stroke 15 | 19 % → 15 % | 83.3 px | 0.34 | 0.81 | 4 |
| stroke 16 | 18 % → 48 % | 103.1 px | 0.35 | 2.61 | 1 |
| stroke 17 | 28 % → 19 % | 118.5 px | 0.34 | 0.68 | 1 |
| stroke 18 | 9 % → 0 % | 31.7 px | 0.00 | 0.00 | 2 |
| stroke 19 | 4 % → 0 % | 23.8 px | 0.00 | 0.00 | 2 |
| stroke 20 | 21 % → 22 % | 48.5 px | 0.35 | 1.08 | 4 |
| stroke 21 | 18 % → 0 % | 50.8 px | 0.29 | 0.00 | 5 |
| stroke 22 | 9 % → 0 % | 22.4 px | 0.00 | 0.00 | 6 |
| stroke 23 | 12 % → 38 % | 67.8 px | 0.35 | 3.24 | 1 |
| stroke 24 | 25 % → 20 % | 148.0 px | 0.35 | 0.79 | 13 |
| stroke 25 | 28 % → 5 % | 112.9 px | 0.34 | 0.18 | 2 |
| stroke 26 | 14 % → 0 % | 82.8 px | 0.00 | 0.00 | 2 |
| stroke 27 | 15 % → 1 % | 38.7 px | 0.32 | 0.05 | 3 |
| stroke 28 | 23 % → 19 % | 65.5 px | 0.35 | 0.81 | 7 |
| stroke 29 | 10 % → 4 % | 32.9 px | 0.34 | 0.41 | 5 |
| stroke 30 | 15 % → 0 % | 47.1 px | 0.00 | 0.00 | 2 |
| stroke 31 | 9 % → 0 % | 47.1 px | 0.00 | 0.00 | 1 |
| stroke 32 | 18 % → 0 % | 38.3 px | 0.00 | 0.00 | 14 |
| stroke 33 | 8 % → 0 % | 43.8 px | 0.00 | 0.00 | 20 |
| stroke 34 | 20 % → 6 % | 36.9 px | 0.34 | 0.28 | 6 |
| stroke 35 | 20 % → 0 % | 66.1 px | 0.00 | 0.00 | 3 |
| stroke 36 | 11 % → 0 % | 53.5 px | 0.00 | 0.00 | 2 |
| stroke 37 | 25 % → 7 % | 54.2 px | 0.34 | 0.26 | 10 |
| stroke 38 | 26 % → 0 % | 150.1 px | 0.00 | 0.00 | 1 |
| stroke 39 | 18 % → 0 % | 105.4 px | 0.00 | 0.00 | 2 |
| stroke 40 | 12 % → 0 % | 60.2 px | 0.00 | 0.00 | 1 |
| stroke 41 | 22 % → 7 % | 46.5 px | 0.34 | 0.31 | 7 |
| stroke 42 | 36 % → 0 % | 147.7 px | 0.00 | 0.00 | 3 |
| stroke 43 | 25 % → 0 % | 56.4 px | 0.00 | 0.00 | 4 |
| stroke 44 | 12 % → 0 % | 68.8 px | 0.00 | 0.00 | 1 |
| stroke 45 | 28 % → 0 % | 161.5 px | 0.31 | 0.02 | 3 |
| stroke 46 | 19 % → 0 % | 106.1 px | 0.00 | 0.00 | 2 |
| stroke 47 | 12 % → 1 % | 63.4 px | 0.34 | 0.11 | 2 |
| stroke 48 | 18 % → 2 % | 39.1 px | 0.34 | 0.11 | 10 |
| stroke 49 | 23 % → 0 % | 74.9 px | 0.00 | 0.00 | 13 |
| stroke 50 | 12 % → 8 % | 64.9 px | 0.34 | 0.73 | 12 |
| stroke 51 | 4 % → 0 % | 20.3 px | 0.00 | 0.00 | 1 |
| stroke 52 | 14 % → 0 % | 32.6 px | 0.00 | 0.00 | 5 |
| stroke 53 | 12 % → 6 % | 16.3 px | 0.35 | 0.52 | 31 |
| stroke 54 | 15 % → 9 % | 27.0 px | 0.34 | 0.62 | 7 |
| stroke 55 | 11 % → 0 % | 27.5 px | 0.00 | 0.00 | 9 |
| stroke 56 | 17 % → 0 % | 43.3 px | 0.00 | 0.00 | 6 |
| stroke 57 | 22 % → 5 % | 29.3 px | 0.34 | 0.24 | 37 |
| stroke 58 | 22 % → 10 % | 56.2 px | 0.34 | 0.47 | 5 |
| stroke 59 | 25 % → 3 % | 35.3 px | 0.34 | 0.11 | 70 |
| stroke 60 | 33 % → 3 % | 46.2 px | 0.34 | 0.09 | 72 |
| stroke 61 | 42 % → 2 % | 56.4 px | 0.35 | 0.04 | 80 |
| stroke 62 | 42 % → 0 % | 56.2 px | 0.00 | 0.00 | 31 |
| stroke 63 | 20 % → 0 % | 11.9 px | 0.00 | 0.00 | 53 |
| stroke 64 | 31 % → 0 % | 39.3 px | 0.00 | 0.00 | 6 |
| stroke 65 | 35 % → 0 % | 156.8 px | 0.00 | 0.00 | 2 |
| stroke 66 | 33 % → 0 % | 22.8 px | 0.00 | 0.00 | 65 |
| stroke 67 | 11 % → 0 % | 20.5 px | 0.00 | 0.00 | 7 |
| stroke 68 | 7 % → 4 % | 24.0 px | 0.34 | 0.57 | 6 |
| stroke 69 | 5 % → 49 % | 23.4 px | 0.35 | 9.67 | 2 |
| stroke 70 | 6 % → 22 % | 28.1 px | 0.34 | 3.47 | 6 |
| stroke 71 | 10 % → 48 % | 28.8 px | 0.35 | 4.67 | 12 |
| stroke 72 | 5 % → 0 % | 23.0 px | 0.00 | 0.00 | 4 |
| stroke 73 | 7 % → 7 % | 30.7 px | 0.34 | 0.96 | 3 |
| stroke 74 | 7 % → 6 % | 25.8 px | 0.34 | 0.80 | 6 |
| stroke 75 | 8 % → 8 % | 23.2 px | 0.34 | 1.02 | 11 |
| stroke 76 | 18 % → 0 % | 84.0 px | 0.00 | 0.00 | 2 |
| stroke 77 | 19 % → 41 % | 59.7 px | 0.35 | 2.12 | 11 |
| stroke 78 | 17 % → 46 % | 43.9 px | 0.35 | 2.76 | 9 |
| stroke 79 | 6 % → 30 % | 20.8 px | 0.35 | 5.13 | 2 |
| stroke 80 | 9 % → 18 % | 43.4 px | 0.34 | 1.96 | 3 |
| stroke 81 | 12 % → 0 % | 52.3 px | 0.00 | 0.00 | 5 |
| stroke 82 | 9 % → 15 % | 28.4 px | 0.35 | 1.74 | 5 |
| stroke 83 | 17 % → 29 % | 76.9 px | 0.35 | 1.73 | 5 |
| stroke 84 | 12 % → 37 % | 34.4 px | 0.35 | 3.02 | 16 |
| stroke 85 | 18 % → 0 % | 70.3 px | 0.00 | 0.00 | 8 |
| stroke 86 | 28 % → 48 % | 106.3 px | 0.35 | 1.73 | 8 |
| stroke 87 | 17 % → 34 % | 77.3 px | 0.35 | 1.95 | 2 |
| stroke 88 | 19 % → 11 % | 62.2 px | 0.35 | 0.57 | 8 |
| stroke 89 | 17 % → 33 % | 55.9 px | 0.35 | 1.98 | 13 |
| stroke 90 | 23 % → 18 % | 107.3 px | 0.35 | 0.80 | 4 |
| stroke 91 | 25 % → 0 % | 71.3 px | 0.00 | 0.00 | 14 |
| stroke 92 | 25 % → 11 % | 58.0 px | 0.35 | 0.44 | 17 |
| stroke 93 | 6 % → 0 % | 22.8 px | 0.00 | 0.00 | 9 |
| stroke 94 | 20 % → 28 % | 57.3 px | 0.34 | 1.37 | 7 |
| stroke 95 | 16 % → 16 % | 55.2 px | 0.34 | 1.02 | 3 |
| stroke 96 | 26 % → 22 % | 107.5 px | 0.35 | 0.84 | 2 |
| stroke 97 | 21 % → 12 % | 98.6 px | 0.34 | 0.57 | 2 |
| stroke 98 | 25 % → 22 % | 72.2 px | 0.34 | 0.88 | 5 |
| stroke 99 | 14 % → 13 % | 63.6 px | 0.35 | 0.99 | 5 |
| stroke 100 | 41 % → 28 % | 192.9 px | 0.35 | 0.69 | 3 |
| stroke 101 | 37 % → 23 % | 158.0 px | 0.35 | 0.63 | 3 |
| stroke 102 | 38 % → 30 % | 145.1 px | 0.35 | 0.77 | 10 |
| stroke 103 | 29 % → 19 % | 97.5 px | 0.34 | 0.66 | 4 |
| stroke 104 | 39 % → 37 % | 101.8 px | 0.34 | 0.94 | 19 |
| stroke 105 | 37 % → 29 % | 140.8 px | 0.35 | 0.77 | 6 |
| stroke 106 | 38 % → 40 % | 145.0 px | 0.35 | 1.05 | 4 |
| stroke 107 | 16 % → 12 % | 72.8 px | 0.35 | 0.75 | 3 |
| stroke 108 | 31 % → 17 % | 137.9 px | 0.35 | 0.56 | 3 |
| stroke 109 | 37 % → 8 % | 158.8 px | 0.35 | 0.23 | 7 |
| stroke 110 | 43 % → 24 % | 130.0 px | 0.34 | 0.54 | 13 |
| stroke 111 | 31 % → 15 % | 108.9 px | 0.34 | 0.50 | 8 |
| stroke 112 | 13 % → 37 % | 46.2 px | 0.35 | 2.86 | 8 |
| stroke 113 | 37 % → 4 % | 164.9 px | 0.33 | 0.12 | 5 |
| stroke 114 | 34 % → 6 % | 85.6 px | 0.34 | 0.19 | 6 |
| stroke 115 | 38 % → 16 % | 178.8 px | 0.35 | 0.43 | 4 |
| stroke 116 | 48 % → 41 % | 223.5 px | 0.35 | 0.85 | 6 |
| stroke 117 | 54 % → 35 % | 189.9 px | 0.35 | 0.65 | 4 |
| stroke 118 | 47 % → 13 % | 201.2 px | 0.34 | 0.28 | 8 |
| stroke 119 | 30 % → 29 % | 116.7 px | 0.34 | 0.98 | 3 |
| stroke 120 | 31 % → 31 % | 98.0 px | 0.35 | 0.99 | 9 |
| stroke 121 | 55 % → 45 % | 220.3 px | 0.35 | 0.81 | 5 |
| stroke 122 | 11 % → 0 % | 18.7 px | 0.00 | 0.00 | 16 |
| stroke 123 | 7 % → 0 % | 26.4 px | 0.00 | 0.00 | 5 |
| stroke 124 | 17 % → 0 % | 56.2 px | 0.00 | 0.00 | 3 |
| stroke 125 | 15 % → 0 % | 40.9 px | 0.00 | 0.00 | 12 |
| stroke 126 | 8 % → 0 % | 27.0 px | 0.00 | 0.00 | 6 |
| stroke 127 | 29 % → 0 % | 103.9 px | 0.00 | 0.00 | 4 |
| stroke 128 | 11 % → 18 % | 21.2 px | 0.34 | 1.71 | 10 |
| stroke 129 | 12 % → 41 % | 16.2 px | 0.35 | 3.34 | 40 |
| stroke 130 | 21 % → 34 % | 55.6 px | 0.35 | 1.59 | 9 |
| stroke 131 | 13 % → 55 % | 47.1 px | 0.35 | 4.12 | 7 |
| stroke 132 | 22 % → 59 % | 91.8 px | 0.35 | 2.70 | 3 |
| stroke 133 | 15 % → 61 % | 72.8 px | 0.35 | 3.95 | 2 |
| stroke 134 | 29 % → 77 % | 124.6 px | 0.35 | 2.60 | 3 |
| stroke 135 | 24 % → 27 % | 54.6 px | 0.35 | 1.11 | 19 |
| stroke 136 | 31 % → 52 % | 132.9 px | 0.35 | 1.70 | 3 |
| stroke 137 | 35 % → 36 % | 154.9 px | 0.35 | 1.02 | 7 |
| stroke 138 | 16 % → 34 % | 53.5 px | 0.34 | 2.18 | 4 |
| stroke 139 | 27 % → 33 % | 124.1 px | 0.34 | 1.25 | 6 |
| stroke 140 | 31 % → 32 % | 82.0 px | 0.34 | 1.02 | 8 |
| stroke 141 | 31 % → 1 % | 125.0 px | 0.33 | 0.02 | 6 |
| stroke 142 | 18 % → 55 % | 83.7 px | 0.35 | 3.02 | 2 |
| stroke 143 | 24 % → 61 % | 93.9 px | 0.35 | 2.55 | 4 |
| stroke 144 | 35 % → 0 % | 88.7 px | 0.00 | 0.00 | 6 |
| stroke 145 | 33 % → 0 % | 100.7 px | 0.00 | 0.00 | 4 |
| stroke 146 | 37 % → 0 % | 137.5 px | 0.32 | 0.00 | 5 |
| stroke 147 | 22 % → 27 % | 95.6 px | 0.35 | 1.23 | 19 |
| stroke 148 | 44 % → 24 % | 116.5 px | 0.35 | 0.55 | 13 |
| stroke 149 | 57 % → 32 % | 262.5 px | 0.35 | 0.56 | 4 |
| stroke 150 | 60 % → 33 % | 207.0 px | 0.35 | 0.55 | 13 |
| stroke 151 | 28 % → 0 % | 82.7 px | 0.00 | 0.00 | 8 |
| stroke 152 | 25 % → 0 % | 53.3 px | 0.00 | 0.00 | 9 |
| stroke 153 | 14 % → 6 % | 34.4 px | 0.34 | 0.44 | 8 |
| stroke 154 | 18 % → 0 % | 67.1 px | 0.31 | 0.01 | 12 |
| stroke 155 | 34 % → 0 % | 130.7 px | 0.00 | 0.00 | 6 |
| stroke 156 | 40 % → 0 % | 100.3 px | 0.00 | 0.00 | 10 |
| stroke 157 | 19 % → 0 % | 49.7 px | 0.00 | 0.00 | 11 |
| stroke 158 | 8 % → 0 % | 31.6 px | 0.00 | 0.00 | 10 |
| stroke 159 | 11 % → 0 % | 44.2 px | 0.00 | 0.00 | 6 |
| stroke 160 | 7 % → 3 % | 20.6 px | 0.34 | 0.42 | 9 |
| stroke 161 | 5 % → 14 % | 14.6 px | 0.35 | 2.82 | 3 |
| stroke 162 | 9 % → 12 % | 26.2 px | 0.34 | 1.29 | 4 |
| stroke 163 | 13 % → 10 % | 48.8 px | 0.34 | 0.76 | 5 |
| stroke 164 | 21 % → 4 % | 120.8 px | 0.34 | 0.17 | 2 |
| stroke 165 | 10 % → 17 % | 61.2 px | 0.34 | 1.68 | 1 |
| stroke 166 | 20 % → 1 % | 73.3 px | 0.33 | 0.05 | 5 |
| stroke 167 | 3 % → 13 % | 17.0 px | 0.35 | 4.67 | 1 |
| stroke 168 | 5 % → 22 % | 13.8 px | 0.35 | 4.61 | 4 |
| stroke 169 | 10 % → 14 % | 25.9 px | 0.34 | 1.47 | 7 |
| stroke 170 | 22 % → 0 % | 96.9 px | 0.00 | 0.00 | 7 |
| stroke 171 | 5 % → 9 % | 23.5 px | 0.35 | 1.75 | 4 |
| stroke 172 | 11 % → 16 % | 47.7 px | 0.35 | 1.47 | 4 |
| stroke 173 | 17 % → 14 % | 47.2 px | 0.35 | 0.85 | 5 |
| stroke 174 | 23 % → 0 % | 106.5 px | 0.00 | 0.00 | 1 |
| stroke 175 | 21 % → 0 % | 93.9 px | 0.00 | 0.00 | 4 |
| stroke 176 | 17 % → 4 % | 52.0 px | 0.34 | 0.25 | 6 |
| stroke 177 | 21 % → 0 % | 51.3 px | 0.34 | 0.01 | 9 |
| stroke 178 | 9 % → 1 % | 28.5 px | 0.34 | 0.12 | 5 |
| stroke 179 | 18 % → 11 % | 42.2 px | 0.35 | 0.59 | 8 |
| stroke 180 | 22 % → 0 % | 60.8 px | 0.00 | 0.00 | 6 |
| stroke 181 | 23 % → 0 % | 106.0 px | 0.00 | 0.00 | 1 |
| stroke 182 | 9 % → 0 % | 55.0 px | 0.00 | 0.00 | 1 |
| stroke 183 | 19 % → 1 % | 73.5 px | 0.34 | 0.05 | 2 |
| stroke 184 | 22 % → 0 % | 130.6 px | 0.00 | 0.00 | 1 |
| stroke 185 | 30 % → 0 % | 176.1 px | 0.00 | 0.00 | 1 |
| stroke 186 | 21 % → 3 % | 53.0 px | 0.34 | 0.14 | 17 |
| stroke 187 | 34 % → 0 % | 114.5 px | 0.00 | 0.00 | 2 |
| stroke 188 | 16 % → 0 % | 38.3 px | 0.29 | 0.00 | 9 |
| stroke 189 | 26 % → 0 % | 155.7 px | 0.00 | 0.00 | 2 |
| stroke 190 | 24 % → 2 % | 57.3 px | 0.34 | 0.09 | 19 |
| stroke 191 | 19 % → 0 % | 55.6 px | 0.00 | 0.00 | 7 |
| stroke 192 | 32 % → 0 % | 91.6 px | 0.00 | 0.00 | 3 |
| stroke 193 | 25 % → 0 % | 85.2 px | 0.00 | 0.00 | 2 |
| stroke 194 | 27 % → 0 % | 63.6 px | 0.00 | 0.00 | 10 |
| stroke 195 | 23 % → 0 % | 54.6 px | 0.00 | 0.00 | 6 |
| stroke 196 | 30 % → 3 % | 69.7 px | 0.35 | 0.09 | 13 |
| stroke 197 | 30 % → 0 % | 112.6 px | 0.00 | 0.00 | 3 |
| stroke 198 | 25 % → 0 % | 149.1 px | 0.00 | 0.00 | 1 |
| stroke 199 | 32 % → 0 % | 77.0 px | 0.00 | 0.00 | 7 |
| stroke 200 | 33 % → 0 % | 107.8 px | 0.00 | 0.00 | 3 |
| stroke 201 | 25 % → 0 % | 147.9 px | 0.00 | 0.00 | 1 |
| stroke 202 | 28 % → 0 % | 127.4 px | 0.00 | 0.00 | 1 |
| stroke 203 | 30 % → 0 % | 136.7 px | 0.00 | 0.00 | 2 |
| stroke 204 | 31 % → 0 % | 194.9 px | 0.00 | 0.00 | 0 |
| stroke 205 | 31 % → 0 % | 140.0 px | 0.00 | 0.00 | 3 |
| stroke 206 | 29 % → 0 % | 73.6 px | 0.00 | 0.00 | 9 |
| stroke 207 | 30 % → 0 % | 183.4 px | 0.00 | 0.00 | 1 |
| stroke 208 | 29 % → 0 % | 110.2 px | 0.00 | 0.00 | 2 |
| stroke 209 | 27 % → 0 % | 157.6 px | 0.00 | 0.00 | 3 |
| stroke 210 | 26 % → 0 % | 120.4 px | 0.00 | 0.00 | 1 |
| stroke 211 | 26 % → 0 % | 154.7 px | 0.00 | 0.00 | 1 |
| stroke 212 | 20 % → 0 % | 88.0 px | 0.00 | 0.00 | 1 |
| stroke 213 | 27 % → 0 % | 66.4 px | 0.00 | 0.00 | 7 |
| stroke 214 | 31 % → 0 % | 111.6 px | 0.00 | 0.00 | 3 |
| stroke 215 | 16 % → 4 % | 44.1 px | 0.34 | 0.23 | 5 |
| stroke 216 | 31 % → 0 % | 92.3 px | 0.00 | 0.00 | 8 |
| stroke 217 | 27 % → 0 % | 118.1 px | 0.00 | 0.00 | 1 |
| stroke 218 | 31 % → 0 % | 175.6 px | 0.00 | 0.00 | 1 |
| stroke 219 | 22 % → 0 % | 84.2 px | 0.00 | 0.00 | 3 |
| stroke 220 | 29 % → 0 % | 94.7 px | 0.00 | 0.00 | 4 |
| stroke 221 | 27 % → 3 % | 122.0 px | 0.33 | 0.10 | 5 |
| stroke 222 | 28 % → 0 % | 78.1 px | 0.00 | 0.00 | 3 |
| stroke 223 | 32 % → 1 % | 78.6 px | 0.32 | 0.02 | 9 |
| stroke 224 | 26 % → 0 % | 117.8 px | 0.00 | 0.00 | 3 |
| stroke 225 | 34 % → 0 % | 102.2 px | 0.00 | 0.00 | 3 |
| stroke 226 | 32 % → 4 % | 103.4 px | 0.34 | 0.14 | 3 |
| stroke 227 | 25 % → 0 % | 112.7 px | 0.00 | 0.00 | 2 |
| stroke 228 | 31 % → 3 % | 72.9 px | 0.34 | 0.09 | 10 |
| stroke 229 | 12 % → 9 % | 55.1 px | 0.34 | 0.69 | 9 |
| stroke 230 | 33 % → 1 % | 76.7 px | 0.34 | 0.04 | 14 |
| stroke 231 | 17 % → 9 % | 79.2 px | 0.34 | 0.51 | 1 |
| stroke 232 | 38 % → 0 % | 98.1 px | 0.00 | 0.00 | 12 |
| stroke 233 | 22 % → 5 % | 57.3 px | 0.34 | 0.22 | 5 |
| stroke 234 | 39 % → 0 % | 94.9 px | 0.29 | 0.00 | 6 |
| stroke 235 | 39 % → 0 % | 96.7 px | 0.00 | 0.00 | 10 |
| stroke 236 | 21 % → 5 % | 54.5 px | 0.34 | 0.24 | 6 |
| stroke 237 | 29 % → 2 % | 68.4 px | 0.34 | 0.07 | 18 |
| stroke 238 | 40 % → 0 % | 93.8 px | 0.00 | 0.00 | 9 |
| stroke 239 | 40 % → 0 % | 96.8 px | 0.00 | 0.00 | 10 |
| stroke 240 | 39 % → 0 % | 108.3 px | 0.00 | 0.00 | 3 |
| stroke 241 | 36 % → 0 % | 159.9 px | 0.00 | 0.00 | 1 |
| stroke 242 | 13 % → 37 % | 40.8 px | 0.35 | 2.88 | 8 |
| stroke 243 | 24 % → 32 % | 93.3 px | 0.35 | 1.34 | 11 |
| stroke 244 | 10 % → 31 % | 38.8 px | 0.35 | 3.03 | 17 |
| stroke 245 | 16 % → 29 % | 52.4 px | 0.35 | 1.78 | 20 |
| stroke 246 | 40 % → 44 % | 106.7 px | 0.35 | 1.11 | 27 |
| stroke 247 | 43 % → 43 % | 170.8 px | 0.35 | 1.00 | 14 |
| stroke 248 | 11 % → 58 % | 34.2 px | 0.35 | 5.42 | 12 |
| stroke 249 | 13 % → 28 % | 36.1 px | 0.35 | 2.23 | 18 |
| stroke 250 | 26 % → 32 % | 65.7 px | 0.35 | 1.22 | 13 |
| stroke 251 | 17 % → 73 % | 64.1 px | 0.35 | 4.40 | 6 |
| stroke 252 | 27 % → 48 % | 73.7 px | 0.35 | 1.77 | 23 |
| stroke 253 | 31 % → 48 % | 100.8 px | 0.35 | 1.52 | 15 |
| stroke 254 | 15 % → 41 % | 62.9 px | 0.35 | 2.66 | 7 |
| stroke 255 | 22 % → 57 % | 56.8 px | 0.35 | 2.62 | 18 |
| stroke 256 | 23 % → 43 % | 59.4 px | 0.35 | 1.88 | 29 |
| stroke 257 | 35 % → 35 % | 117.6 px | 0.35 | 1.03 | 14 |
| stroke 258 | 48 % → 60 % | 203.3 px | 0.35 | 1.24 | 9 |
| stroke 259 | 16 % → 53 % | 66.3 px | 0.35 | 3.21 | 8 |
| stroke 260 | 48 % → 54 % | 165.8 px | 0.35 | 1.13 | 12 |
| stroke 261 | 24 % → 47 % | 94.3 px | 0.35 | 1.92 | 8 |
| stroke 262 | 34 % → 64 % | 148.6 px | 0.35 | 1.87 | 12 |
| stroke 263 | 43 % → 64 % | 172.9 px | 0.35 | 1.48 | 12 |
| stroke 264 | 55 % → 60 % | 191.3 px | 0.35 | 1.09 | 13 |
| stroke 265 | 47 % → 65 % | 164.7 px | 0.35 | 1.38 | 16 |
| stroke 266 | 41 % → 52 % | 182.0 px | 0.35 | 1.25 | 10 |
| stroke 267 | 75 % → 84 % | 330.2 px | 0.35 | 1.12 | 5 |
| stroke 268 | 65 % → 67 % | 214.4 px | 0.35 | 1.03 | 15 |
| stroke 269 | 54 % → 55 % | 212.5 px | 0.35 | 1.02 | 10 |
| stroke 270 | 57 % → 57 % | 172.1 px | 0.35 | 1.00 | 30 |
| stroke 271 | 22 % → 22 % | 47.3 px | 0.34 | 1.00 | 53 |
| stroke 272 | 13 % → 22 % | 61.3 px | 0.34 | 1.70 | 4 |
| stroke 273 | 17 % → 17 % | 67.2 px | 0.34 | 1.01 | 12 |
| stroke 274 | 11 % → 38 % | 36.0 px | 0.35 | 3.49 | 12 |
| stroke 275 | 20 % → 46 % | 75.1 px | 0.35 | 2.32 | 15 |
| stroke 276 | 26 % → 37 % | 98.5 px | 0.35 | 1.43 | 8 |
| stroke 277 | 29 % → 34 % | 99.8 px | 0.35 | 1.17 | 17 |
| stroke 278 | 40 % → 42 % | 142.0 px | 0.35 | 1.04 | 16 |
| stroke 279 | 9 % → 36 % | 42.0 px | 0.34 | 3.93 | 11 |
| stroke 280 | 16 % → 27 % | 51.1 px | 0.34 | 1.68 | 14 |
| stroke 281 | 21 % → 28 % | 84.4 px | 0.34 | 1.31 | 14 |
| stroke 282 | 24 % → 50 % | 73.9 px | 0.35 | 2.11 | 13 |
| stroke 283 | 26 % → 48 % | 70.4 px | 0.35 | 1.83 | 12 |
| stroke 284 | 12 % → 27 % | 51.7 px | 0.34 | 2.19 | 9 |
| stroke 285 | 17 % → 21 % | 74.3 px | 0.34 | 1.24 | 11 |
| stroke 286 | 28 % → 45 % | 110.6 px | 0.35 | 1.59 | 13 |
| stroke 287 | 38 % → 56 % | 159.4 px | 0.35 | 1.46 | 11 |
| stroke 288 | 45 % → 53 % | 149.4 px | 0.35 | 1.19 | 13 |
| stroke 289 | 34 % → 34 % | 117.9 px | 0.35 | 1.00 | 11 |
| stroke 290 | 9 % → 9 % | 36.0 px | 0.34 | 1.00 | 7 |
| stroke 291 | 11 % → 11 % | 28.0 px | 0.35 | 1.00 | 23 |
| stroke 292 | 10 % → 10 % | 26.8 px | 0.34 | 1.00 | 17 |

Numbers say: wet paint spreads well beyond the stroke.

## Refs v3 · #19 Guston charcoal hand — own sheet
own sheet 800 × 800 · Charcoal 1.00 · 39 px · 11.2 s

![Refs v3 · #19 Guston charcoal hand — own sheet](Refs-v3-19-Guston-charcoal-hand-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 5 % → 22 % | 21.6 px | 0.59 | 4.73 | 15 |
| stroke 2 | 9 % → 23 % | 46.5 px | 0.59 | 2.62 | 13 |
| stroke 3 | 8 % → 22 % | 105.3 px | 0.59 | 2.62 | 7 |
| stroke 4 | 12 % → 22 % | 67.9 px | 0.59 | 1.76 | 22 |
| stroke 5 | 7 % → 20 % | 42.9 px | 0.59 | 2.94 | 16 |
| stroke 6 | 18 % → 24 % | 240.6 px | 0.59 | 1.37 | 4 |
| stroke 7 | 19 % → 23 % | 273.8 px | 0.59 | 1.20 | 7 |
| stroke 8 | 18 % → 22 % | 132.8 px | 0.59 | 1.23 | 20 |
| stroke 9 | 3 % → 40 % | 21.2 px | 0.59 | 14.04 | 10 |
| stroke 10 | 6 % → 44 % | 47.1 px | 0.60 | 7.85 | 6 |
| stroke 11 | 4 % → 27 % | 25.7 px | 0.59 | 6.56 | 8 |
| stroke 12 | 4 % → 38 % | 25.2 px | 0.60 | 10.18 | 11 |
| stroke 13 | 3 % → 36 % | 29.1 px | 0.59 | 11.46 | 4 |
| stroke 14 | 2 % → 41 % | 29.9 px | 0.60 | 22.55 | 11 |
| stroke 15 | 8 % → 43 % | 52.9 px | 0.60 | 5.11 | 21 |
| stroke 16 | 7 % → 52 % | 64.0 px | 0.60 | 7.07 | 12 |
| stroke 17 | 7 % → 28 % | 93.7 px | 0.59 | 3.84 | 7 |
| stroke 18 | 2 % → 39 % | 30.4 px | 0.60 | 20.52 | 4 |
| stroke 19 | 2 % → 52 % | 22.6 px | 0.59 | 21.99 | 10 |
| stroke 20 | 2 % → 35 % | 30.5 px | 0.60 | 16.43 | 4 |
| stroke 21 | 11 % → 44 % | 89.9 px | 0.60 | 4.10 | 13 |
| stroke 22 | 6 % → 42 % | 73.7 px | 0.60 | 7.55 | 9 |
| stroke 23 | 15 % → 28 % | 63.1 px | 0.59 | 1.87 | 51 |
| stroke 24 | 11 % → 20 % | 42.3 px | 0.60 | 1.83 | 47 |
| stroke 25 | 4 % → 45 % | 31.3 px | 0.60 | 12.81 | 9 |
| stroke 26 | 10 % → 60 % | 103.1 px | 0.60 | 5.95 | 7 |
| stroke 27 | 14 % → 61 % | 142.2 px | 0.60 | 4.51 | 14 |
| stroke 28 | 15 % → 58 % | 74.7 px | 0.60 | 3.88 | 32 |
| stroke 29 | 10 % → 48 % | 96.6 px | 0.60 | 4.98 | 11 |
| stroke 30 | 17 % → 42 % | 74.6 px | 0.59 | 2.47 | 37 |
| stroke 31 | 5 % → 38 % | 71.0 px | 0.60 | 7.21 | 5 |
| stroke 32 | 7 % → 41 % | 108.2 px | 0.60 | 5.51 | 5 |
| stroke 33 | 7 % → 34 % | 84.0 px | 0.60 | 4.84 | 8 |
| stroke 34 | 22 % → 61 % | 159.9 px | 0.60 | 2.84 | 17 |
| stroke 35 | 17 % → 56 % | 206.1 px | 0.60 | 3.22 | 9 |
| stroke 36 | 16 % → 25 % | 52.9 px | 0.59 | 1.61 | 25 |
| stroke 37 | 20 % → 42 % | 189.2 px | 0.60 | 2.04 | 13 |
| stroke 38 | 10 % → 32 % | 62.0 px | 0.60 | 3.32 | 38 |
| stroke 39 | 16 % → 51 % | 191.7 px | 0.60 | 3.23 | 11 |
| stroke 40 | 19 % → 46 % | 139.7 px | 0.60 | 2.45 | 12 |
| stroke 41 | 17 % → 33 % | 143.8 px | 0.59 | 1.91 | 14 |
| stroke 42 | 13 % → 46 % | 115.1 px | 0.60 | 3.43 | 13 |
| stroke 43 | 11 % → 35 % | 97.8 px | 0.60 | 3.10 | 9 |
| stroke 44 | 18 % → 39 % | 72.6 px | 0.60 | 2.16 | 63 |
| stroke 45 | 16 % → 28 % | 60.0 px | 0.60 | 1.78 | 42 |
| stroke 46 | 20 % → 54 % | 218.3 px | 0.60 | 2.74 | 12 |
| stroke 47 | 19 % → 53 % | 266.4 px | 0.60 | 2.77 | 6 |
| stroke 48 | 21 % → 49 % | 179.8 px | 0.60 | 2.35 | 7 |
| stroke 49 | 5 % → 23 % | 32.7 px | 0.60 | 4.65 | 22 |
| stroke 50 | 31 % → 56 % | 300.2 px | 0.60 | 1.81 | 20 |
| stroke 51 | 30 % → 53 % | 218.3 px | 0.60 | 1.76 | 14 |
| stroke 52 | 13 % → 33 % | 114.2 px | 0.60 | 2.48 | 12 |
| stroke 53 | 14 % → 38 % | 116.2 px | 0.60 | 2.83 | 52 |
| stroke 54 | 14 % → 34 % | 177.1 px | 0.60 | 2.39 | 9 |
| stroke 55 | 30 % → 49 % | 266.0 px | 0.60 | 1.62 | 13 |
| stroke 56 | 25 % → 52 % | 350.9 px | 0.60 | 2.08 | 9 |
| stroke 57 | 20 % → 48 % | 249.0 px | 0.60 | 2.44 | 23 |
| stroke 58 | 10 % → 29 % | 96.6 px | 0.60 | 2.76 | 14 |
| stroke 59 | 35 % → 56 % | 351.6 px | 0.60 | 1.63 | 6 |
| stroke 60 | 30 % → 55 % | 223.0 px | 0.60 | 1.81 | 14 |
| stroke 61 | 20 % → 33 % | 293.0 px | 0.59 | 1.62 | 3 |
| stroke 62 | 24 % → 30 % | 190.7 px | 0.60 | 1.24 | 31 |
| stroke 63 | 41 % → 58 % | 330.8 px | 0.60 | 1.43 | 13 |
| stroke 64 | 23 % → 39 % | 71.7 px | 0.59 | 1.67 | 58 |
| stroke 65 | 25 % → 43 % | 111.9 px | 0.60 | 1.71 | 39 |
| stroke 66 | 20 % → 31 % | 173.8 px | 0.60 | 1.53 | 9 |
| stroke 67 | 29 % → 45 % | 128.4 px | 0.60 | 1.56 | 38 |
| stroke 68 | 40 % → 57 % | 226.3 px | 0.60 | 1.41 | 26 |
| stroke 69 | 30 % → 53 % | 329.2 px | 0.60 | 1.76 | 8 |
| stroke 70 | 28 % → 33 % | 340.3 px | 0.59 | 1.15 | 4 |
| stroke 71 | 14 % → 27 % | 196.4 px | 0.60 | 1.94 | 4 |
| stroke 72 | 38 % → 57 % | 223.5 px | 0.60 | 1.49 | 20 |
| stroke 73 | 31 % → 48 % | 405.5 px | 0.60 | 1.54 | 8 |
| stroke 74 | 30 % → 34 % | 72.7 px | 0.59 | 1.11 | 59 |
| stroke 75 | 29 % → 42 % | 298.3 px | 0.60 | 1.44 | 6 |
| stroke 76 | 49 % → 59 % | 473.4 px | 0.60 | 1.21 | 15 |
| stroke 77 | 38 % → 46 % | 251.6 px | 0.60 | 1.22 | 16 |
| stroke 78 | 37 % → 52 % | 414.7 px | 0.60 | 1.40 | 14 |
| stroke 79 | 34 % → 49 % | 570.7 px | 0.60 | 1.45 | 6 |
| stroke 80 | 38 % → 51 % | 455.9 px | 0.60 | 1.34 | 29 |
| stroke 81 | 30 % → 34 % | 139.7 px | 0.60 | 1.16 | 39 |
| stroke 82 | 35 % → 50 % | 299.8 px | 0.60 | 1.42 | 10 |
| stroke 83 | 33 % → 42 % | 476.7 px | 0.60 | 1.28 | 7 |
| stroke 84 | 35 % → 42 % | 262.3 px | 0.60 | 1.19 | 14 |
| stroke 85 | 31 % → 34 % | 192.3 px | 0.60 | 1.11 | 13 |
| stroke 86 | 18 % → 26 % | 149.4 px | 0.60 | 1.41 | 15 |
| stroke 87 | 33 % → 39 % | 205.6 px | 0.60 | 1.17 | 30 |
| stroke 88 | 43 % → 52 % | 267.0 px | 0.60 | 1.20 | 20 |
| stroke 89 | 35 % → 48 % | 446.7 px | 0.60 | 1.38 | 5 |
| stroke 90 | 18 % → 23 % | 195.1 px | 0.60 | 1.26 | 9 |
| stroke 91 | 31 % → 33 % | 264.8 px | 0.60 | 1.07 | 9 |
| stroke 92 | 46 % → 53 % | 379.0 px | 0.59 | 1.14 | 10 |
| stroke 93 | 46 % → 53 % | 603.9 px | 0.60 | 1.17 | 6 |
| stroke 94 | 31 % → 39 % | 186.0 px | 0.60 | 1.25 | 17 |
| stroke 95 | 50 % → 56 % | 428.5 px | 0.60 | 1.14 | 11 |
| stroke 96 | 19 % → 23 % | 281.1 px | 0.60 | 1.17 | 6 |
| stroke 97 | 31 % → 33 % | 121.4 px | 0.60 | 1.08 | 24 |
| stroke 98 | 45 % → 48 % | 722.9 px | 0.60 | 1.08 | 4 |
| stroke 99 | 46 % → 52 % | 753.7 px | 0.60 | 1.12 | 8 |
| stroke 100 | 37 % → 38 % | 307.9 px | 0.60 | 1.01 | 8 |
| stroke 101 | 42 % → 47 % | 351.5 px | 0.60 | 1.11 | 12 |
| stroke 102 | 55 % → 58 % | 502.3 px | 0.60 | 1.06 | 12 |
| stroke 103 | 20 % → 23 % | 358.2 px | 0.60 | 1.13 | 3 |
| stroke 104 | 42 % → 47 % | 706.1 px | 0.60 | 1.13 | 4 |
| stroke 105 | 49 % → 50 % | 539.8 px | 0.60 | 1.03 | 14 |
| stroke 106 | 30 % → 37 % | 287.9 px | 0.60 | 1.23 | 16 |
| stroke 107 | 57 % → 59 % | 580.7 px | 0.60 | 1.02 | 10 |
| stroke 108 | 49 % → 49 % | 256.8 px | 0.60 | 1.00 | 35 |
| stroke 109 | 60 % → 61 % | 911.8 px | 0.60 | 1.01 | 8 |
| stroke 110 | 34 % → 34 % | 282.4 px | 0.60 | 1.00 | 9 |
| stroke 111 | 42 % → 44 % | 332.3 px | 0.60 | 1.05 | 14 |
| stroke 112 | 40 % → 40 % | 255.1 px | 0.60 | 1.00 | 22 |
| stroke 113 | 56 % → 56 % | 558.3 px | 0.60 | 1.00 | 15 |
| stroke 114 | 32 % → 32 % | 268.1 px | 0.60 | 1.00 | 18 |
| stroke 115 | 24 % → 24 % | 221.2 px | 0.59 | 1.00 | 10 |

Numbers say: wet paint spreads well beyond the stroke.

## Refs v3 · #20 Orange crayon — own sheet
own sheet 800 × 1245 · Wax 1.00 · 48 px · 50.0 s

![Refs v3 · #20 Orange crayon — own sheet](Refs-v3-20-Orange-crayon-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 8 % → 68 % | 45.2 px | 0.55 | 8.07 | 74 |
| stroke 2 | 16 % → 79 % | 52.4 px | 0.55 | 4.99 | 118 |
| stroke 3 | 6 % → 46 % | 50.6 px | 0.54 | 7.82 | 51 |
| stroke 4 | 6 % → 30 % | 47.6 px | 0.55 | 5.27 | 48 |
| stroke 5 | 21 % → 85 % | 63.4 px | 0.55 | 4.03 | 310 |
| stroke 6 | 10 % → 54 % | 70.9 px | 0.54 | 5.67 | 161 |
| stroke 7 | 14 % → 41 % | 84.2 px | 0.54 | 2.92 | 113 |
| stroke 8 | 4 % → 12 % | 63.6 px | 0.50 | 2.78 | 32 |
| stroke 9 | 24 % → 88 % | 74.3 px | 0.55 | 3.61 | 313 |
| stroke 10 | 18 % → 52 % | 80.9 px | 0.55 | 2.90 | 243 |
| stroke 11 | 24 % → 77 % | 87.5 px | 0.55 | 3.27 | 862 |
| stroke 12 | 8 % → 20 % | 120.4 px | 0.51 | 2.55 | 21 |
| stroke 13 | 30 % → 81 % | 106.9 px | 0.55 | 2.69 | 866 |
| stroke 14 | 11 % → 30 % | 132.0 px | 0.52 | 2.71 | 63 |
| stroke 15 | 37 % → 84 % | 137.3 px | 0.55 | 2.28 | 697 |
| stroke 16 | 16 % → 43 % | 164.2 px | 0.54 | 2.73 | 28 |
| stroke 17 | 40 % → 86 % | 162.7 px | 0.55 | 2.11 | 638 |
| stroke 18 | 22 % → 57 % | 153.1 px | 0.54 | 2.64 | 66 |
| stroke 19 | 44 % → 86 % | 185.9 px | 0.55 | 1.98 | 574 |
| stroke 20 | 31 % → 71 % | 174.9 px | 0.54 | 2.28 | 146 |
| stroke 21 | 53 % → 94 % | 206.5 px | 0.55 | 1.78 | 708 |
| stroke 22 | 39 % → 82 % | 176.0 px | 0.55 | 2.09 | 312 |
| stroke 23 | 25 % → 44 % | 307.8 px | 0.54 | 1.77 | 32 |
| stroke 24 | 53 % → 95 % | 207.7 px | 0.55 | 1.79 | 389 |
| stroke 25 | 35 % → 73 % | 151.8 px | 0.54 | 2.07 | 350 |
| stroke 26 | 44 % → 85 % | 204.9 px | 0.55 | 1.96 | 854 |
| stroke 27 | 47 % → 89 % | 218.5 px | 0.55 | 1.89 | 719 |
| stroke 28 | 49 % → 92 % | 227.3 px | 0.55 | 1.87 | 703 |
| stroke 29 | 41 % → 83 % | 203.0 px | 0.55 | 2.04 | 850 |
| stroke 30 | 56 % → 98 % | 232.9 px | 0.55 | 1.76 | 943 |
| stroke 31 | 39 % → 82 % | 173.5 px | 0.54 | 2.08 | 307 |
| stroke 32 | 17 % → 46 % | 214.3 px | 0.54 | 2.63 | 24 |
| stroke 33 | 57 % → 98 % | 228.5 px | 0.55 | 1.74 | 600 |
| stroke 34 | 52 % → 96 % | 235.6 px | 0.54 | 1.84 | 309 |
| stroke 35 | 25 % → 61 % | 158.8 px | 0.54 | 2.38 | 128 |
| stroke 36 | 56 % → 98 % | 225.7 px | 0.55 | 1.74 | 521 |
| stroke 37 | 46 % → 91 % | 206.1 px | 0.54 | 1.98 | 252 |
| stroke 38 | 35 % → 70 % | 248.5 px | 0.54 | 2.00 | 59 |
| stroke 39 | 43 % → 86 % | 217.2 px | 0.55 | 1.98 | 1382 |
| stroke 40 | 44 % → 86 % | 221.6 px | 0.55 | 1.95 | 950 |
| stroke 41 | 45 % → 87 % | 227.5 px | 0.55 | 1.92 | 1244 |
| stroke 42 | 47 % → 88 % | 231.7 px | 0.55 | 1.90 | 1486 |
| stroke 43 | 48 % → 88 % | 235.1 px | 0.55 | 1.83 | 939 |
| stroke 44 | 50 % → 87 % | 234.4 px | 0.55 | 1.73 | 937 |
| stroke 45 | 54 % → 86 % | 231.4 px | 0.55 | 1.60 | 1190 |
| stroke 46 | 61 % → 95 % | 254.3 px | 0.55 | 1.55 | 1815 |
| stroke 47 | 46 % → 46 % | 228.1 px | 0.53 | 1.00 | 61 |
| stroke 48 | 65 % → 96 % | 253.6 px | 0.55 | 1.47 | 858 |
| stroke 49 | 62 % → 97 % | 235.7 px | 0.55 | 1.55 | 985 |
| stroke 50 | 75 % → 82 % | 307.0 px | 0.55 | 1.09 | 109 |
| stroke 51 | 66 % → 97 % | 231.6 px | 0.55 | 1.47 | 743 |
| stroke 52 | 79 % → 86 % | 479.2 px | 0.55 | 1.09 | 82 |
| stroke 53 | 73 % → 97 % | 232.6 px | 0.55 | 1.32 | 534 |
| stroke 54 | 72 % → 98 % | 221.2 px | 0.55 | 1.35 | 490 |
| stroke 55 | 89 % → 95 % | 392.8 px | 0.55 | 1.06 | 78 |
| stroke 56 | 79 % → 98 % | 219.1 px | 0.55 | 1.24 | 535 |
| stroke 57 | 83 % → 97 % | 214.5 px | 0.55 | 1.17 | 308 |
| stroke 58 | 86 % → 97 % | 206.6 px | 0.55 | 1.13 | 320 |
| stroke 59 | 91 % → 96 % | 215.4 px | 0.55 | 1.06 | 305 |
| stroke 60 | 95 % → 95 % | 251.2 px | 0.55 | 1.00 | 111 |

Numbers say: wet paint spreads well beyond the stroke.

## Refs v3 · #21 Gritty dog contours — own sheet
own sheet 800 × 1130 · Gouache 1.00 + water 15 % · 53 px · 126.6 s

![Refs v3 · #21 Gritty dog contours — own sheet](Refs-v3-21-Gritty-dog-contours-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 5 % → 3 % | 55.1 px | 0.40 | 0.54 | 144 |
| stroke 2 | 8 % → 3 % | 115.8 px | 0.40 | 0.33 | 51 |
| stroke 3 | 10 % → 2 % | 77.0 px | 0.40 | 0.18 | 154 |
| stroke 4 | 16 % → 3 % | 150.5 px | 0.41 | 0.19 | 125 |
| stroke 5 | 25 % → 3 % | 453.3 px | 0.40 | 0.11 | 33 |
| stroke 6 | 18 % → 4 % | 145.8 px | 0.42 | 0.21 | 193 |
| stroke 7 | 21 % → 3 % | 160.6 px | 0.41 | 0.14 | 212 |
| stroke 8 | 20 % → 4 % | 168.2 px | 0.42 | 0.19 | 112 |
| stroke 9 | 18 % → 5 % | 111.1 px | 0.42 | 0.26 | 473 |
| stroke 10 | 34 % → 2 % | 359.6 px | 0.41 | 0.05 | 108 |
| stroke 11 | 41 % → 2 % | 751.1 px | 0.41 | 0.04 | 28 |
| stroke 12 | 23 % → 4 % | 151.2 px | 0.42 | 0.16 | 222 |
| stroke 13 | 35 % → 3 % | 293.8 px | 0.41 | 0.08 | 125 |
| stroke 14 | 31 % → 5 % | 209.7 px | 0.42 | 0.15 | 167 |
| stroke 15 | 23 % → 7 % | 307.6 px | 0.42 | 0.32 | 42 |
| stroke 16 | 41 % → 2 % | 741.5 px | 0.41 | 0.05 | 23 |
| stroke 17 | 34 % → 6 % | 226.2 px | 0.42 | 0.17 | 353 |
| stroke 18 | 34 % → 2 % | 601.3 px | 0.41 | 0.05 | 58 |
| stroke 19 | 33 % → 5 % | 206.8 px | 0.42 | 0.15 | 312 |
| stroke 20 | 46 % → 6 % | 520.8 px | 0.40 | 0.12 | 69 |
| stroke 21 | 37 % → 7 % | 457.0 px | 0.42 | 0.19 | 61 |
| stroke 22 | 39 % → 5 % | 306.7 px | 0.40 | 0.13 | 114 |
| stroke 23 | 33 % → 7 % | 352.7 px | 0.42 | 0.20 | 60 |
| stroke 24 | 33 % → 5 % | 328.0 px | 0.40 | 0.16 | 114 |
| stroke 25 | 29 % → 6 % | 257.1 px | 0.42 | 0.19 | 96 |
| stroke 26 | 6 % → 3 % | 80.2 px | 0.42 | 0.45 | 28 |
| stroke 27 | 31 % → 6 % | 313.3 px | 0.40 | 0.19 | 67 |
| stroke 28 | 45 % → 6 % | 694.4 px | 0.40 | 0.13 | 35 |
| stroke 29 | 29 % → 6 % | 226.1 px | 0.42 | 0.19 | 108 |
| stroke 30 | 7 % → 2 % | 83.2 px | 0.42 | 0.28 | 51 |
| stroke 31 | 33 % → 6 % | 347.6 px | 0.40 | 0.20 | 105 |
| stroke 32 | 47 % → 7 % | 585.8 px | 0.40 | 0.14 | 61 |
| stroke 33 | 31 % → 7 % | 222.4 px | 0.42 | 0.21 | 170 |
| stroke 34 | 13 % → 1 % | 146.2 px | 0.41 | 0.10 | 80 |
| stroke 35 | 35 % → 7 % | 428.5 px | 0.40 | 0.21 | 81 |
| stroke 36 | 44 % → 8 % | 536.7 px | 0.41 | 0.19 | 62 |
| stroke 37 | 30 % → 6 % | 206.9 px | 0.43 | 0.19 | 240 |
| stroke 38 | 14 % → 1 % | 164.7 px | 0.41 | 0.07 | 66 |
| stroke 39 | 37 % → 9 % | 666.7 px | 0.41 | 0.25 | 60 |
| stroke 40 | 41 % → 9 % | 558.7 px | 0.41 | 0.21 | 62 |
| stroke 41 | 30 % → 5 % | 202.7 px | 0.43 | 0.15 | 223 |
| stroke 42 | 21 % → 0 % | 197.7 px | 0.42 | 0.02 | 126 |
| stroke 43 | 38 % → 10 % | 665.0 px | 0.41 | 0.26 | 42 |
| stroke 44 | 44 % → 6 % | 552.8 px | 0.42 | 0.14 | 118 |
| stroke 45 | 32 % → 4 % | 212.5 px | 0.42 | 0.12 | 247 |
| stroke 46 | 32 % → 0 % | 443.1 px | 0.42 | 0.01 | 47 |
| stroke 47 | 23 % → 0 % | 346.8 px | 0.40 | 0.01 | 43 |
| stroke 48 | 36 % → 9 % | 406.9 px | 0.41 | 0.25 | 58 |
| stroke 49 | 29 % → 4 % | 178.8 px | 0.42 | 0.13 | 638 |
| stroke 50 | 26 % → 1 % | 362.3 px | 0.42 | 0.03 | 141 |
| stroke 51 | 31 % → 11 % | 548.4 px | 0.41 | 0.35 | 49 |
| stroke 52 | 44 % → 5 % | 470.0 px | 0.43 | 0.12 | 70 |
| stroke 53 | 36 % → 3 % | 229.2 px | 0.42 | 0.07 | 685 |
| stroke 54 | 29 % → 1 % | 357.2 px | 0.42 | 0.04 | 79 |
| stroke 55 | 29 % → 10 % | 352.3 px | 0.41 | 0.33 | 79 |
| stroke 56 | 41 % → 4 % | 265.2 px | 0.42 | 0.09 | 255 |
| stroke 57 | 45 % → 1 % | 788.9 px | 0.41 | 0.01 | 30 |
| stroke 58 | 30 % → 1 % | 421.0 px | 0.42 | 0.04 | 53 |
| stroke 59 | 44 % → 7 % | 774.3 px | 0.43 | 0.15 | 33 |
| stroke 60 | 45 % → 4 % | 295.4 px | 0.42 | 0.08 | 350 |
| stroke 61 | 33 % → 1 % | 270.0 px | 0.42 | 0.02 | 315 |
| stroke 62 | 25 % → 9 % | 340.8 px | 0.41 | 0.37 | 64 |
| stroke 63 | 42 % → 6 % | 355.6 px | 0.42 | 0.15 | 155 |
| stroke 64 | 49 % → 4 % | 322.7 px | 0.42 | 0.08 | 373 |
| stroke 65 | 50 % → 2 % | 904.7 px | 0.41 | 0.03 | 57 |
| stroke 66 | 33 % → 1 % | 417.2 px | 0.42 | 0.03 | 78 |
| stroke 67 | 39 % → 7 % | 419.5 px | 0.43 | 0.17 | 131 |
| stroke 68 | 50 % → 5 % | 322.1 px | 0.42 | 0.10 | 498 |
| stroke 69 | 32 % → 1 % | 372.9 px | 0.42 | 0.03 | 65 |
| stroke 70 | 31 % → 9 % | 557.2 px | 0.42 | 0.30 | 26 |
| stroke 71 | 48 % → 5 % | 302.7 px | 0.42 | 0.10 | 330 |
| stroke 72 | 36 % → 1 % | 379.2 px | 0.42 | 0.03 | 194 |
| stroke 73 | 25 % → 8 % | 265.2 px | 0.42 | 0.32 | 94 |
| stroke 74 | 50 % → 5 % | 314.5 px | 0.42 | 0.11 | 402 |
| stroke 75 | 30 % → 1 % | 254.6 px | 0.42 | 0.04 | 106 |
| stroke 76 | 41 % → 7 % | 255.9 px | 0.42 | 0.16 | 474 |
| stroke 77 | 58 % → 2 % | 782.0 px | 0.41 | 0.03 | 46 |
| stroke 78 | 30 % → 2 % | 228.6 px | 0.41 | 0.05 | 144 |
| stroke 79 | 31 % → 8 % | 283.0 px | 0.42 | 0.27 | 79 |
| stroke 80 | 53 % → 8 % | 347.7 px | 0.42 | 0.14 | 217 |
| stroke 81 | 56 % → 1 % | 567.0 px | 0.41 | 0.03 | 94 |
| stroke 82 | 34 % → 2 % | 268.2 px | 0.41 | 0.06 | 114 |
| stroke 83 | 32 % → 8 % | 337.1 px | 0.42 | 0.26 | 58 |
| stroke 84 | 51 % → 9 % | 323.0 px | 0.42 | 0.17 | 260 |
| stroke 85 | 57 % → 1 % | 544.3 px | 0.41 | 0.03 | 81 |
| stroke 86 | 37 % → 2 % | 313.4 px | 0.41 | 0.05 | 151 |
| stroke 87 | 47 % → 7 % | 287.7 px | 0.42 | 0.15 | 349 |
| stroke 88 | 55 % → 2 % | 524.7 px | 0.41 | 0.03 | 78 |
| stroke 89 | 40 % → 2 % | 374.4 px | 0.41 | 0.05 | 88 |
| stroke 90 | 48 % → 8 % | 295.3 px | 0.42 | 0.16 | 334 |
| stroke 91 | 57 % → 3 % | 1021.9 px | 0.42 | 0.05 | 49 |
| stroke 92 | 56 % → 3 % | 556.0 px | 0.41 | 0.05 | 142 |
| stroke 93 | 45 % → 9 % | 429.3 px | 0.42 | 0.21 | 114 |
| stroke 94 | 54 % → 12 % | 408.8 px | 0.42 | 0.23 | 195 |
| stroke 95 | 56 % → 4 % | 509.6 px | 0.42 | 0.07 | 114 |
| stroke 96 | 52 % → 3 % | 489.0 px | 0.41 | 0.06 | 236 |
| stroke 97 | 49 % → 13 % | 521.3 px | 0.42 | 0.26 | 82 |
| stroke 98 | 53 % → 6 % | 326.0 px | 0.42 | 0.11 | 529 |
| stroke 99 | 51 % → 9 % | 317.4 px | 0.42 | 0.18 | 327 |
| stroke 100 | 48 % → 3 % | 726.6 px | 0.41 | 0.06 | 44 |
| stroke 101 | 47 % → 13 % | 586.5 px | 0.42 | 0.28 | 56 |
| stroke 102 | 53 % → 10 % | 348.4 px | 0.42 | 0.18 | 253 |
| stroke 103 | 44 % → 12 % | 423.9 px | 0.42 | 0.26 | 83 |
| stroke 104 | 55 % → 11 % | 555.5 px | 0.43 | 0.20 | 137 |
| stroke 105 | 53 % → 7 % | 789.4 px | 0.42 | 0.14 | 28 |
| stroke 106 | 44 % → 12 % | 437.5 px | 0.42 | 0.27 | 62 |
| stroke 107 | 49 % → 11 % | 755.8 px | 0.42 | 0.23 | 44 |
| stroke 108 | 41 % → 13 % | 434.3 px | 0.42 | 0.31 | 73 |
| stroke 109 | 46 % → 11 % | 528.6 px | 0.42 | 0.25 | 45 |
| stroke 110 | 40 % → 13 % | 498.0 px | 0.42 | 0.33 | 42 |
| stroke 111 | 45 % → 11 % | 368.2 px | 0.42 | 0.23 | 110 |
| stroke 112 | 42 % → 13 % | 473.7 px | 0.42 | 0.30 | 61 |
| stroke 113 | 34 % → 10 % | 593.5 px | 0.43 | 0.29 | 24 |
| stroke 114 | 39 % → 13 % | 490.0 px | 0.43 | 0.33 | 45 |
| stroke 115 | 35 % → 12 % | 402.3 px | 0.43 | 0.35 | 55 |
| stroke 116 | 32 % → 12 % | 408.8 px | 0.43 | 0.38 | 48 |
| stroke 117 | 29 % → 11 % | 328.0 px | 0.43 | 0.38 | 60 |
| stroke 118 | 25 % → 11 % | 378.3 px | 0.43 | 0.43 | 39 |
| stroke 119 | 1 % → 4 % | 20.3 px | 0.42 | 4.34 | 7 |
| stroke 120 | 2 % → 3 % | 15.0 px | 0.42 | 1.58 | 21 |
| stroke 121 | 2 % → 3 % | 13.1 px | 0.40 | 1.53 | 33 |
| stroke 122 | 2 % → 2 % | 21.0 px | 0.41 | 0.83 | 15 |
| stroke 123 | 3 % → 1 % | 31.0 px | 0.42 | 0.41 | 18 |
| stroke 124 | 7 % → 3 % | 105.4 px | 0.40 | 0.38 | 6 |
| stroke 125 | 8 % → 3 % | 200.5 px | 0.40 | 0.35 | 8 |
| stroke 126 | 8 % → 2 % | 90.8 px | 0.40 | 0.31 | 34 |
| stroke 127 | 10 % → 2 % | 152.3 px | 0.41 | 0.23 | 9 |
| stroke 128 | 12 % → 3 % | 170.7 px | 0.40 | 0.22 | 11 |
| stroke 129 | 10 % → 3 % | 76.4 px | 0.42 | 0.32 | 40 |
| stroke 130 | 16 % → 3 % | 288.0 px | 0.40 | 0.17 | 12 |
| stroke 131 | 15 % → 1 % | 259.2 px | 0.42 | 0.09 | 18 |
| stroke 132 | 11 % → 3 % | 159.2 px | 0.41 | 0.26 | 14 |
| stroke 133 | 7 % → 4 % | 72.1 px | 0.42 | 0.58 | 26 |
| stroke 134 | 5 % → 8 % | 68.7 px | 0.40 | 1.70 | 16 |
| stroke 135 | 10 % → 5 % | 217.6 px | 0.41 | 0.47 | 9 |
| stroke 136 | 5 % → 9 % | 50.2 px | 0.41 | 1.75 | 29 |
| stroke 137 | 4 % → 10 % | 46.1 px | 0.41 | 2.31 | 12 |
| stroke 138 | 2 % → 1 % | 27.1 px | 0.40 | 0.35 | 11 |
| stroke 139 | 6 % → 12 % | 190.4 px | 0.41 | 1.82 | 3 |
| stroke 140 | 7 % → 8 % | 55.1 px | 0.41 | 1.10 | 37 |
| stroke 141 | 8 % → 5 % | 182.2 px | 0.41 | 0.64 | 8 |
| stroke 142 | 9 % → 5 % | 235.0 px | 0.41 | 0.54 | 5 |
| stroke 143 | 9 % → 8 % | 174.7 px | 0.41 | 0.86 | 12 |
| stroke 144 | 11 % → 7 % | 166.6 px | 0.40 | 0.65 | 11 |
| stroke 145 | 9 % → 11 % | 123.0 px | 0.41 | 1.17 | 17 |
| stroke 146 | 7 % → 5 % | 104.0 px | 0.43 | 0.65 | 13 |
| stroke 147 | 1 % → 4 % | 15.9 px | 0.42 | 5.36 | 4 |
| stroke 148 | 6 % → 9 % | 77.4 px | 0.43 | 1.38 | 28 |
| stroke 149 | 4 % → 5 % | 57.7 px | 0.43 | 1.30 | 6 |
| stroke 150 | 3 % → 6 % | 30.2 px | 0.42 | 1.77 | 33 |
| stroke 151 | 2 % → 14 % | 43.1 px | 0.42 | 5.80 | 20 |
| stroke 152 | 4 % → 13 % | 35.2 px | 0.42 | 2.93 | 48 |
| stroke 153 | 5 % → 10 % | 50.4 px | 0.42 | 1.94 | 15 |
| stroke 154 | 1 % → 2 % | 17.1 px | 0.41 | 1.74 | 10 |
| stroke 155 | 3 % → 1 % | 22.2 px | 0.41 | 0.44 | 58 |
| stroke 156 | 7 % → 2 % | 78.2 px | 0.41 | 0.24 | 27 |
| stroke 157 | 6 % → 4 % | 49.2 px | 0.42 | 0.77 | 30 |
| stroke 158 | 6 % → 4 % | 120.9 px | 0.42 | 0.71 | 8 |
| stroke 159 | 1 % → 1 % | 23.5 px | 0.42 | 1.63 | 6 |
| stroke 160 | 1 % → 1 % | 32.6 px | 0.42 | 1.19 | 2 |
| stroke 161 | 3 % → 1 % | 42.0 px | 0.42 | 0.26 | 18 |
| stroke 162 | 1 % → 5 % | 33.3 px | 0.43 | 4.29 | 2 |
| stroke 163 | 1 % → 9 % | 13.9 px | 0.42 | 14.19 | 2 |
| stroke 164 | 2 % → 5 % | 27.1 px | 0.42 | 2.27 | 6 |
| stroke 165 | 2 % → 1 % | 33.3 px | 0.41 | 0.74 | 13 |
| stroke 166 | 3 % → 1 % | 76.5 px | 0.41 | 0.22 | 5 |
| stroke 167 | 4 % → 0 % | 91.2 px | 0.40 | 0.10 | 5 |
| stroke 168 | 5 % → 1 % | 76.4 px | 0.40 | 0.21 | 20 |
| stroke 169 | 5 % → 2 % | 87.9 px | 0.41 | 0.37 | 32 |
| stroke 170 | 6 % → 3 % | 93.6 px | 0.42 | 0.51 | 32 |
| stroke 171 | 8 % → 4 % | 79.8 px | 0.41 | 0.54 | 47 |
| stroke 172 | 9 % → 4 % | 79.4 px | 0.41 | 0.44 | 47 |
| stroke 173 | 10 % → 4 % | 81.0 px | 0.41 | 0.37 | 54 |
| stroke 174 | 13 % → 4 % | 171.3 px | 0.41 | 0.33 | 23 |
| stroke 175 | 4 % → 7 % | 36.4 px | 0.42 | 1.90 | 35 |
| stroke 176 | 7 % → 5 % | 38.8 px | 0.42 | 0.69 | 124 |
| stroke 177 | 9 % → 4 % | 47.1 px | 0.42 | 0.47 | 152 |
| stroke 178 | 12 % → 5 % | 66.5 px | 0.42 | 0.38 | 153 |
| stroke 179 | 19 % → 5 % | 132.3 px | 0.42 | 0.29 | 83 |
| stroke 180 | 26 % → 7 % | 689.5 px | 0.42 | 0.28 | 16 |
| stroke 181 | 15 % → 1 % | 418.7 px | 0.40 | 0.09 | 6 |
| stroke 182 | 16 % → 3 % | 182.0 px | 0.41 | 0.20 | 20 |
| stroke 183 | 17 % → 4 % | 220.1 px | 0.41 | 0.25 | 25 |
| stroke 184 | 18 % → 5 % | 173.4 px | 0.41 | 0.25 | 37 |
| stroke 185 | 8 % → 7 % | 136.0 px | 0.43 | 0.86 | 10 |
| stroke 186 | 17 % → 8 % | 110.2 px | 0.42 | 0.46 | 75 |
| stroke 187 | 18 % → 8 % | 154.4 px | 0.42 | 0.44 | 40 |
| stroke 188 | 20 % → 8 % | 168.1 px | 0.42 | 0.41 | 56 |
| stroke 189 | 28 % → 4 % | 571.5 px | 0.41 | 0.16 | 16 |
| stroke 190 | 20 % → 8 % | 289.9 px | 0.42 | 0.40 | 59 |
| stroke 191 | 21 % → 8 % | 571.7 px | 0.41 | 0.36 | 10 |
| stroke 192 | 23 % → 8 % | 615.0 px | 0.41 | 0.35 | 8 |
| stroke 193 | 22 % → 11 % | 454.8 px | 0.42 | 0.49 | 16 |
| stroke 194 | 22 % → 12 % | 327.7 px | 0.42 | 0.54 | 15 |
| stroke 195 | 22 % → 13 % | 181.8 px | 0.42 | 0.59 | 57 |
| stroke 196 | 22 % → 13 % | 189.0 px | 0.42 | 0.58 | 53 |
| stroke 197 | 22 % → 11 % | 312.6 px | 0.42 | 0.51 | 29 |
| stroke 198 | 1 % → 3 % | 10.8 px | 0.40 | 4.67 | 4 |
| stroke 199 | 1 % → 3 % | 18.6 px | 0.40 | 1.80 | 6 |
| stroke 200 | 1 % → 4 % | 11.8 px | 0.42 | 4.06 | 9 |
| stroke 201 | 3 % → 4 % | 15.3 px | 0.42 | 1.48 | 45 |
| stroke 202 | 3 % → 8 % | 26.1 px | 0.41 | 2.57 | 33 |
| stroke 203 | 6 % → 8 % | 38.7 px | 0.41 | 1.40 | 42 |
| stroke 204 | 8 % → 10 % | 217.0 px | 0.41 | 1.26 | 7 |
| stroke 205 | 3 % → 6 % | 73.4 px | 0.41 | 1.77 | 6 |
| stroke 206 | 4 % → 8 % | 23.0 px | 0.42 | 2.02 | 81 |
| stroke 207 | 1 % → 9 % | 21.9 px | 0.42 | 6.35 | 11 |
| stroke 208 | 4 % → 11 % | 67.1 px | 0.42 | 2.81 | 9 |
| stroke 209 | 5 % → 8 % | 55.4 px | 0.42 | 1.67 | 21 |
| stroke 210 | 6 % → 12 % | 69.9 px | 0.42 | 2.19 | 10 |
| stroke 211 | 0 % → 2 % | 11.5 px | 0.41 | 5.37 | 2 |
| stroke 212 | 4 % → 11 % | 35.5 px | 0.42 | 3.02 | 41 |
| stroke 213 | 9 % → 15 % | 177.8 px | 0.42 | 1.71 | 10 |
| stroke 214 | 6 % → 11 % | 35.5 px | 0.42 | 1.86 | 43 |
| stroke 215 | 10 % → 15 % | 137.9 px | 0.42 | 1.54 | 7 |
| stroke 216 | 1 % → 2 % | 25.1 px | 0.41 | 1.62 | 8 |
| stroke 217 | 7 % → 9 % | 65.0 px | 0.43 | 1.37 | 15 |
| stroke 218 | 5 % → 7 % | 134.4 px | 0.42 | 1.31 | 4 |
| stroke 219 | 1 % → 1 % | 10.3 px | 0.41 | 2.56 | 2 |
| stroke 220 | 1 % → 2 % | 32.4 px | 0.41 | 1.55 | 2 |

Numbers say: wet paint spreads well beyond the stroke.

## Refs v3 · #22 Wasilewski brush poster — own sheet
own sheet 800 × 1633 · Ink 0.98 · 64 px · 99.8 s

![Refs v3 · #22 Wasilewski brush poster — own sheet](Refs-v3-22-Wasilewski-brush-poster-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 2 % → 39 % | 90.3 px | 0.92 | 15.99 | 48 |
| stroke 2 | 4 % → 70 % | 94.6 px | 0.92 | 18.95 | 5 |
| stroke 3 | 10 % → 78 % | 41.5 px | 0.92 | 7.58 | 94 |
| stroke 4 | 2 % → 48 % | 92.1 px | 0.92 | 22.03 | 10 |
| stroke 5 | 4 % → 54 % | 61.1 px | 0.92 | 13.45 | 37 |
| stroke 6 | 3 % → 34 % | 84.7 px | 0.92 | 11.14 | 19 |
| stroke 7 | 2 % → 38 % | 67.6 px | 0.91 | 18.34 | 9 |
| stroke 8 | 6 % → 59 % | 225.7 px | 0.92 | 9.85 | 7 |
| stroke 9 | 6 % → 28 % | 207.2 px | 0.91 | 4.35 | 12 |
| stroke 10 | 6 % → 38 % | 164.4 px | 0.92 | 6.79 | 17 |
| stroke 11 | 9 % → 30 % | 123.9 px | 0.91 | 3.28 | 32 |
| stroke 12 | 7 % → 56 % | 161.8 px | 0.91 | 8.49 | 27 |
| stroke 13 | 8 % → 44 % | 301.2 px | 0.91 | 5.84 | 24 |
| stroke 14 | 10 % → 35 % | 300.8 px | 0.91 | 3.65 | 24 |
| stroke 15 | 3 % → 14 % | 88.1 px | 0.91 | 4.86 | 17 |
| stroke 16 | 6 % → 35 % | 280.3 px | 0.92 | 5.49 | 8 |
| stroke 17 | 14 % → 48 % | 124.0 px | 0.92 | 3.44 | 33 |
| stroke 18 | 3 % → 43 % | 80.1 px | 0.93 | 14.47 | 22 |
| stroke 19 | 1 % → 39 % | 59.9 px | 0.92 | 29.22 | 5 |
| stroke 20 | 9 % → 34 % | 107.6 px | 0.91 | 3.88 | 78 |
| stroke 21 | 16 % → 52 % | 313.2 px | 0.92 | 3.33 | 27 |
| stroke 22 | 4 % → 35 % | 138.2 px | 0.92 | 7.86 | 15 |
| stroke 23 | 17 % → 30 % | 94.2 px | 0.91 | 1.80 | 200 |
| stroke 24 | 18 % → 70 % | 707.2 px | 0.92 | 3.88 | 6 |
| stroke 25 | 6 % → 26 % | 188.0 px | 0.91 | 4.42 | 12 |
| stroke 26 | 4 % → 13 % | 136.9 px | 0.91 | 3.68 | 16 |
| stroke 27 | 2 % → 24 % | 68.7 px | 0.91 | 12.95 | 7 |
| stroke 28 | 9 % → 40 % | 226.7 px | 0.92 | 4.56 | 16 |
| stroke 29 | 11 % → 45 % | 427.0 px | 0.92 | 3.91 | 7 |
| stroke 30 | 6 % → 26 % | 71.4 px | 0.92 | 4.34 | 62 |
| stroke 31 | 7 % → 23 % | 173.4 px | 0.92 | 3.34 | 20 |
| stroke 32 | 13 % → 43 % | 230.0 px | 0.92 | 3.29 | 44 |
| stroke 33 | 26 % → 83 % | 419.6 px | 0.93 | 3.16 | 21 |
| stroke 34 | 9 % → 25 % | 152.7 px | 0.91 | 2.96 | 38 |
| stroke 35 | 10 % → 22 % | 221.0 px | 0.92 | 2.24 | 28 |
| stroke 36 | 7 % → 30 % | 108.0 px | 0.92 | 4.34 | 45 |
| stroke 37 | 10 % → 27 % | 111.6 px | 0.92 | 2.75 | 82 |
| stroke 38 | 16 % → 23 % | 104.4 px | 0.91 | 1.44 | 328 |
| stroke 39 | 17 % → 43 % | 186.2 px | 0.91 | 2.46 | 122 |
| stroke 40 | 12 % → 25 % | 467.6 px | 0.92 | 2.11 | 17 |
| stroke 41 | 23 % → 39 % | 245.9 px | 0.92 | 1.70 | 95 |
| stroke 42 | 12 % → 24 % | 217.4 px | 0.91 | 1.95 | 55 |
| stroke 43 | 19 % → 39 % | 271.6 px | 0.92 | 2.04 | 80 |
| stroke 44 | 16 % → 16 % | 175.5 px | 0.91 | 1.00 | 76 |
| stroke 45 | 22 % → 42 % | 233.7 px | 0.92 | 1.94 | 161 |
| stroke 46 | 28 % → 72 % | 721.8 px | 0.92 | 2.61 | 20 |
| stroke 47 | 24 % → 46 % | 1062.8 px | 0.92 | 1.92 | 18 |
| stroke 48 | 15 % → 24 % | 408.0 px | 0.92 | 1.66 | 27 |
| stroke 49 | 18 % → 48 % | 287.8 px | 0.92 | 2.73 | 158 |
| stroke 50 | 25 % → 52 % | 1022.3 px | 0.92 | 2.11 | 24 |
| stroke 51 | 39 % → 77 % | 854.4 px | 0.92 | 1.98 | 41 |
| stroke 52 | 12 % → 29 % | 153.0 px | 0.92 | 2.48 | 43 |
| stroke 53 | 37 % → 73 % | 665.4 px | 0.92 | 1.99 | 51 |
| stroke 54 | 40 % → 73 % | 647.0 px | 0.92 | 1.83 | 18 |
| stroke 55 | 30 % → 46 % | 260.9 px | 0.91 | 1.55 | 161 |
| stroke 56 | 25 % → 53 % | 556.0 px | 0.92 | 2.12 | 58 |
| stroke 57 | 31 % → 56 % | 530.1 px | 0.92 | 1.79 | 62 |
| stroke 58 | 19 % → 24 % | 315.6 px | 0.92 | 1.25 | 60 |
| stroke 59 | 12 % → 53 % | 151.6 px | 0.93 | 4.28 | 29 |
| stroke 60 | 18 % → 24 % | 278.8 px | 0.92 | 1.28 | 88 |
| stroke 61 | 28 % → 41 % | 370.4 px | 0.92 | 1.44 | 76 |
| stroke 62 | 18 % → 30 % | 236.2 px | 0.91 | 1.68 | 71 |
| stroke 63 | 45 % → 80 % | 702.3 px | 0.92 | 1.76 | 26 |
| stroke 64 | 31 % → 47 % | 191.4 px | 0.92 | 1.51 | 262 |
| stroke 65 | 19 % → 27 % | 621.2 px | 0.91 | 1.39 | 21 |
| stroke 66 | 27 % → 37 % | 465.4 px | 0.92 | 1.40 | 96 |
| stroke 67 | 19 % → 24 % | 604.4 px | 0.92 | 1.29 | 41 |
| stroke 68 | 22 % → 28 % | 441.8 px | 0.91 | 1.28 | 59 |
| stroke 69 | 6 % → 16 % | 233.2 px | 0.92 | 2.73 | 29 |
| stroke 70 | 36 % → 37 % | 422.4 px | 0.92 | 1.04 | 76 |
| stroke 71 | 24 % → 37 % | 1062.8 px | 0.92 | 1.55 | 23 |
| stroke 72 | 52 % → 73 % | 1019.1 px | 0.92 | 1.40 | 82 |
| stroke 73 | 45 % → 56 % | 518.7 px | 0.92 | 1.26 | 170 |
| stroke 74 | 59 % → 72 % | 1518.5 px | 0.92 | 1.22 | 36 |
| stroke 75 | 65 % → 82 % | 772.9 px | 0.92 | 1.26 | 44 |
| stroke 76 | 46 % → 59 % | 612.3 px | 0.92 | 1.28 | 95 |
| stroke 77 | 17 % → 23 % | 543.9 px | 0.92 | 1.40 | 16 |
| stroke 78 | 29 % → 45 % | 317.8 px | 0.92 | 1.53 | 123 |
| stroke 79 | 52 % → 66 % | 807.8 px | 0.92 | 1.27 | 46 |
| stroke 80 | 75 % → 86 % | 715.4 px | 0.93 | 1.14 | 43 |
| stroke 81 | 67 % → 73 % | 395.9 px | 0.92 | 1.09 | 114 |
| stroke 82 | 37 % → 57 % | 1051.5 px | 0.92 | 1.56 | 18 |
| stroke 83 | 36 % → 47 % | 632.7 px | 0.92 | 1.29 | 330 |
| stroke 84 | 31 % → 34 % | 444.5 px | 0.92 | 1.09 | 209 |
| stroke 85 | 5 % → 15 % | 143.2 px | 0.92 | 2.76 | 33 |
| stroke 86 | 39 % → 41 % | 323.6 px | 0.92 | 1.05 | 160 |
| stroke 87 | 49 % → 61 % | 982.9 px | 0.91 | 1.26 | 41 |
| stroke 88 | 24 % → 27 % | 408.1 px | 0.91 | 1.15 | 84 |
| stroke 89 | 36 % → 36 % | 579.0 px | 0.92 | 1.02 | 119 |
| stroke 90 | 18 % → 23 % | 481.2 px | 0.91 | 1.26 | 28 |
| stroke 91 | 30 % → 36 % | 422.9 px | 0.91 | 1.20 | 102 |
| stroke 92 | 20 % → 23 % | 565.0 px | 0.92 | 1.18 | 22 |
| stroke 93 | 19 % → 22 % | 675.3 px | 0.92 | 1.14 | 22 |
| stroke 94 | 44 % → 47 % | 332.3 px | 0.91 | 1.07 | 136 |
| stroke 95 | 38 % → 38 % | 880.7 px | 0.92 | 1.00 | 54 |
| stroke 96 | 66 % → 70 % | 833.8 px | 0.91 | 1.06 | 57 |
| stroke 97 | 24 % → 26 % | 884.4 px | 0.91 | 1.11 | 8 |
| stroke 98 | 22 % → 23 % | 534.5 px | 0.92 | 1.04 | 28 |
| stroke 99 | 50 % → 50 % | 857.9 px | 0.91 | 1.01 | 35 |
| stroke 100 | 16 % → 19 % | 245.2 px | 0.92 | 1.18 | 125 |
| stroke 101 | 37 % → 39 % | 468.1 px | 0.92 | 1.04 | 71 |
| stroke 102 | 16 % → 17 % | 270.7 px | 0.92 | 1.04 | 130 |
| stroke 103 | 22 % → 22 % | 737.3 px | 0.91 | 1.00 | 19 |
| stroke 104 | 34 % → 34 % | 288.7 px | 0.92 | 1.00 | 237 |
| stroke 105 | 41 % → 41 % | 1819.5 px | 0.92 | 1.00 | 10 |
| stroke 106 | 48 % → 48 % | 1695.3 px | 0.91 | 1.00 | 36 |
| stroke 107 | 24 % → 24 % | 811.3 px | 0.92 | 1.00 | 11 |
| stroke 108 | 33 % → 33 % | 242.6 px | 0.92 | 1.00 | 174 |
| stroke 109 | 8 % → 26 % | 49.8 px | 0.92 | 3.33 | 55 |
| stroke 110 | 6 % → 29 % | 38.3 px | 0.92 | 4.60 | 32 |
| stroke 111 | 12 % → 34 % | 276.4 px | 0.92 | 2.89 | 8 |
| stroke 112 | 15 % → 26 % | 129.8 px | 0.92 | 1.72 | 80 |
| stroke 113 | 21 % → 21 % | 86.6 px | 0.92 | 1.02 | 365 |

Numbers say: wet paint spreads well beyond the stroke.

## Refs v3 · #23 Report dry white mask — own sheet
own sheet 800 × 804 · Ink 0.93 · Gouache 0.07 · 89 px · 79.7 s

![Refs v3 · #23 Report dry white mask — own sheet](Refs-v3-23-Report-dry-white-mask-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 9 % → 19 % | 83.9 px | 0.46 | 2.08 | 299 |
| stroke 2 | 12 % → 17 % | 93.9 px | 0.47 | 1.40 | 932 |
| stroke 3 | 16 % → 20 % | 139.2 px | 0.48 | 1.20 | 665 |
| stroke 4 | 20 % → 26 % | 253.8 px | 0.48 | 1.26 | 626 |
| stroke 5 | 37 % → 17 % | 488.4 px | 0.47 | 0.45 | 291 |
| stroke 6 | 22 % → 27 % | 259.3 px | 0.48 | 1.22 | 554 |
| stroke 7 | 36 % → 18 % | 838.4 px | 0.47 | 0.51 | 89 |
| stroke 8 | 23 % → 25 % | 248.2 px | 0.48 | 1.08 | 859 |
| stroke 9 | 23 % → 21 % | 260.6 px | 0.47 | 0.91 | 621 |
| stroke 10 | 44 % → 33 % | 750.5 px | 0.47 | 0.74 | 398 |
| stroke 11 | 22 % → 19 % | 393.9 px | 0.48 | 0.86 | 223 |
| stroke 12 | 37 % → 32 % | 593.3 px | 0.47 | 0.86 | 350 |
| stroke 13 | 23 % → 19 % | 287.9 px | 0.48 | 0.83 | 337 |
| stroke 14 | 34 % → 35 % | 512.7 px | 0.47 | 1.03 | 303 |
| stroke 15 | 24 % → 18 % | 275.0 px | 0.47 | 0.75 | 676 |
| stroke 16 | 35 % → 29 % | 452.4 px | 0.47 | 0.82 | 503 |
| stroke 17 | 30 % → 19 % | 303.2 px | 0.47 | 0.63 | 506 |
| stroke 18 | 42 % → 26 % | 871.0 px | 0.47 | 0.61 | 292 |
| stroke 19 | 34 % → 30 % | 906.5 px | 0.47 | 0.90 | 140 |
| stroke 20 | 44 % → 21 % | 367.7 px | 0.47 | 0.48 | 779 |
| stroke 21 | 48 % → 22 % | 407.9 px | 0.47 | 0.45 | 634 |
| stroke 22 | 45 % → 22 % | 398.7 px | 0.47 | 0.50 | 1925 |
| stroke 23 | 39 % → 17 % | 558.0 px | 0.47 | 0.45 | 275 |
| stroke 24 | 83 % → 26 % | 2184.4 px | 0.46 | 0.32 | 383 |
| stroke 25 | 53 % → 26 % | 1110.7 px | 0.47 | 0.49 | 200 |
| stroke 26 | 59 % → 17 % | 705.5 px | 0.47 | 0.29 | 371 |
| stroke 27 | 1 % → 21 % | 37.7 px | 0.47 | 18.46 | 49 |
| stroke 28 | 2 % → 20 % | 45.9 px | 0.47 | 9.55 | 92 |
| stroke 29 | 3 % → 21 % | 184.4 px | 0.47 | 6.58 | 19 |
| stroke 30 | 4 % → 28 % | 52.4 px | 0.47 | 6.65 | 261 |
| stroke 31 | 8 % → 21 % | 467.2 px | 0.47 | 2.77 | 14 |
| stroke 32 | 6 % → 27 % | 76.5 px | 0.47 | 4.56 | 174 |
| stroke 33 | 10 % → 21 % | 573.6 px | 0.47 | 2.22 | 15 |
| stroke 34 | 10 % → 36 % | 233.9 px | 0.47 | 3.68 | 91 |
| stroke 35 | 11 % → 22 % | 647.7 px | 0.47 | 2.03 | 8 |
| stroke 36 | 11 % → 35 % | 333.2 px | 0.47 | 3.08 | 50 |
| stroke 37 | 12 % → 23 % | 548.3 px | 0.46 | 1.93 | 22 |
| stroke 38 | 13 % → 32 % | 333.4 px | 0.47 | 2.56 | 84 |
| stroke 39 | 14 % → 23 % | 824.6 px | 0.46 | 1.71 | 12 |
| stroke 40 | 13 % → 25 % | 252.0 px | 0.47 | 1.92 | 119 |
| stroke 41 | 13 % → 21 % | 226.3 px | 0.47 | 1.58 | 155 |
| stroke 42 | 1 % → 28 % | 33.1 px | 0.49 | 28.29 | 16 |
| stroke 43 | 16 % → 31 % | 963.6 px | 0.47 | 1.96 | 28 |
| stroke 44 | 5 % → 27 % | 74.5 px | 0.48 | 5.81 | 60 |
| stroke 45 | 15 % → 27 % | 163.3 px | 0.47 | 1.72 | 194 |
| stroke 46 | 9 % → 24 % | 364.1 px | 0.48 | 2.86 | 8 |
| stroke 47 | 22 % → 31 % | 1300.8 px | 0.47 | 1.43 | 26 |
| stroke 48 | 16 % → 26 % | 447.6 px | 0.47 | 1.57 | 38 |
| stroke 49 | 12 % → 24 % | 434.7 px | 0.48 | 2.05 | 25 |
| stroke 50 | 11 % → 23 % | 696.7 px | 0.49 | 2.12 | 4 |
| stroke 51 | 24 % → 31 % | 1450.7 px | 0.47 | 1.31 | 6 |
| stroke 52 | 13 % → 22 % | 272.2 px | 0.48 | 1.75 | 48 |
| stroke 53 | 25 % → 31 % | 1144.5 px | 0.47 | 1.24 | 32 |
| stroke 54 | 14 % → 21 % | 610.9 px | 0.49 | 1.51 | 12 |
| stroke 55 | 25 % → 30 % | 962.0 px | 0.47 | 1.20 | 67 |
| stroke 56 | 17 % → 22 % | 458.7 px | 0.48 | 1.27 | 61 |
| stroke 57 | 25 % → 27 % | 707.1 px | 0.47 | 1.11 | 61 |
| stroke 58 | 21 % → 23 % | 680.5 px | 0.48 | 1.12 | 23 |
| stroke 59 | 24 % → 25 % | 483.4 px | 0.47 | 1.04 | 63 |
| stroke 60 | 2 % → 13 % | 34.7 px | 0.52 | 7.09 | 22 |
| stroke 61 | 5 % → 11 % | 50.1 px | 0.51 | 2.09 | 99 |
| stroke 62 | 8 % → 13 % | 69.9 px | 0.51 | 1.54 | 155 |
| stroke 63 | 12 % → 15 % | 482.3 px | 0.50 | 1.29 | 17 |
| stroke 64 | 12 % → 20 % | 191.9 px | 0.51 | 1.76 | 23 |
| stroke 65 | 15 % → 16 % | 632.4 px | 0.50 | 1.10 | 14 |
| stroke 66 | 16 % → 17 % | 716.4 px | 0.50 | 1.06 | 42 |
| stroke 67 | 4 % → 14 % | 39.0 px | 0.47 | 3.49 | 296 |
| stroke 68 | 7 % → 18 % | 257.5 px | 0.46 | 2.58 | 83 |
| stroke 69 | 8 % → 16 % | 86.0 px | 0.47 | 2.10 | 196 |
| stroke 70 | 9 % → 18 % | 524.2 px | 0.46 | 1.98 | 46 |
| stroke 71 | 10 % → 19 % | 175.8 px | 0.47 | 1.77 | 82 |
| stroke 72 | 11 % → 20 % | 974.7 px | 0.46 | 1.75 | 27 |
| stroke 73 | 13 % → 20 % | 291.9 px | 0.47 | 1.53 | 46 |
| stroke 74 | 13 % → 21 % | 775.0 px | 0.46 | 1.62 | 23 |
| stroke 75 | 15 % → 21 % | 455.7 px | 0.47 | 1.39 | 25 |
| stroke 76 | 16 % → 23 % | 526.5 px | 0.47 | 1.37 | 29 |
| stroke 77 | 19 % → 24 % | 717.6 px | 0.48 | 1.23 | 32 |
| stroke 78 | 21 % → 22 % | 239.9 px | 0.47 | 1.08 | 130 |
| stroke 79 | 3 % → 15 % | 61.4 px | 0.50 | 5.18 | 16 |
| stroke 80 | 3 % → 20 % | 143.3 px | 0.51 | 6.42 | 4 |
| stroke 81 | 7 % → 13 % | 48.9 px | 0.50 | 2.03 | 95 |
| stroke 82 | 7 % → 14 % | 564.5 px | 0.50 | 1.94 | 4 |
| stroke 83 | 10 % → 16 % | 68.7 px | 0.50 | 1.61 | 102 |
| stroke 84 | 9 % → 13 % | 686.4 px | 0.50 | 1.48 | 10 |
| stroke 85 | 21 % → 26 % | 340.3 px | 0.51 | 1.21 | 15 |
| stroke 86 | 10 % → 13 % | 868.7 px | 0.50 | 1.31 | 4 |
| stroke 87 | 10 % → 12 % | 844.3 px | 0.49 | 1.23 | 3 |
| stroke 88 | 11 % → 12 % | 647.0 px | 0.48 | 1.17 | 11 |
| stroke 89 | 12 % → 13 % | 984.1 px | 0.48 | 1.10 | 7 |
| stroke 90 | 13 % → 13 % | 788.8 px | 0.48 | 1.06 | 15 |

Numbers say: wet paint spreads well beyond the stroke.

## Refs v3 · #24 Picasso flat oil — own sheet
own sheet 800 × 1156 · Gouache 1.00 + turpentine 20 % · 51 px · 662.6 s

![Refs v3 · #24 Picasso flat oil — own sheet](Refs-v3-24-Picasso-flat-oil-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 8 % → 78 % | 51.0 px | 0.16 | 9.88 | 122 |
| stroke 2 | 8 % → 97 % | 53.1 px | 0.43 | 11.57 | 288 |
| stroke 3 | 16 % → 93 % | 90.7 px | 0.41 | 5.68 | 281 |
| stroke 4 | 19 % → 98 % | 121.6 px | 0.45 | 5.26 | 285 |
| stroke 5 | 19 % → 97 % | 221.3 px | 0.23 | 5.24 | 88 |
| stroke 6 | 23 % → 97 % | 169.1 px | 0.53 | 4.19 | 243 |
| stroke 7 | 36 % → 96 % | 429.3 px | 0.53 | 2.64 | 42 |
| stroke 8 | 43 % → 95 % | 512.2 px | 0.45 | 2.23 | 63 |
| stroke 9 | 20 % → 91 % | 100.3 px | 0.51 | 4.47 | 187 |
| stroke 10 | 40 % → 99 % | 502.9 px | 0.54 | 2.46 | 58 |
| stroke 11 | 28 % → 96 % | 130.7 px | 0.52 | 3.41 | 291 |
| stroke 12 | 38 % → 93 % | 285.0 px | 0.37 | 2.43 | 109 |
| stroke 13 | 41 % → 100 % | 255.7 px | 0.54 | 2.43 | 214 |
| stroke 14 | 43 % → 94 % | 367.1 px | 0.47 | 2.16 | 107 |
| stroke 15 | 36 % → 100 % | 213.3 px | 0.52 | 2.76 | 166 |
| stroke 16 | 39 % → 99 % | 242.7 px | 0.53 | 2.51 | 164 |
| stroke 17 | 48 % → 95 % | 622.3 px | 0.49 | 1.99 | 48 |
| stroke 18 | 56 % → 95 % | 562.9 px | 0.51 | 1.68 | 85 |
| stroke 19 | 55 % → 99 % | 478.6 px | 0.50 | 1.80 | 90 |
| stroke 20 | 30 % → 88 % | 230.4 px | 0.24 | 2.92 | 85 |
| stroke 21 | 39 % → 100 % | 275.1 px | 0.52 | 2.56 | 126 |
| stroke 22 | 61 % → 100 % | 720.0 px | 0.55 | 1.62 | 78 |
| stroke 23 | 57 % → 97 % | 592.1 px | 0.42 | 1.70 | 94 |
| stroke 24 | 54 % → 94 % | 481.4 px | 0.48 | 1.72 | 109 |
| stroke 25 | 43 % → 97 % | 359.8 px | 0.52 | 2.29 | 122 |
| stroke 26 | 60 % → 95 % | 748.6 px | 0.53 | 1.59 | 60 |
| stroke 27 | 48 % → 97 % | 253.7 px | 0.49 | 2.04 | 259 |
| stroke 28 | 39 % → 100 % | 203.2 px | 0.47 | 2.53 | 258 |
| stroke 29 | 48 % → 98 % | 450.4 px | 0.48 | 2.03 | 110 |
| stroke 30 | 67 % → 99 % | 582.1 px | 0.52 | 1.48 | 94 |
| stroke 31 | 42 % → 96 % | 389.5 px | 0.43 | 2.27 | 97 |
| stroke 32 | 41 % → 95 % | 426.9 px | 0.42 | 2.34 | 69 |
| stroke 33 | 58 % → 100 % | 515.4 px | 0.48 | 1.71 | 121 |
| stroke 34 | 14 % → 82 % | 51.1 px | 0.55 | 5.83 | 238 |
| stroke 35 | 26 % → 83 % | 122.9 px | 0.56 | 3.20 | 182 |
| stroke 36 | 32 % → 96 % | 102.9 px | 0.49 | 2.98 | 311 |
| stroke 37 | 37 % → 79 % | 184.6 px | 0.58 | 2.11 | 187 |
| stroke 38 | 57 % → 94 % | 198.1 px | 0.57 | 1.64 | 264 |
| stroke 39 | 67 % → 97 % | 464.6 px | 0.55 | 1.44 | 249 |
| stroke 40 | 63 % → 93 % | 426.6 px | 0.58 | 1.48 | 157 |
| stroke 41 | 39 % → 75 % | 145.7 px | 0.54 | 1.93 | 295 |
| stroke 42 | 60 % → 72 % | 315.0 px | 0.60 | 1.19 | 118 |
| stroke 43 | 63 % → 80 % | 431.6 px | 0.58 | 1.27 | 142 |
| stroke 44 | 21 % → 95 % | 159.0 px | 0.42 | 4.41 | 65 |
| stroke 45 | 87 % → 97 % | 403.8 px | 0.59 | 1.11 | 86 |
| stroke 46 | 51 % → 84 % | 415.9 px | 0.54 | 1.64 | 110 |
| stroke 47 | 82 % → 97 % | 288.0 px | 0.58 | 1.17 | 153 |
| stroke 48 | 83 % → 93 % | 375.6 px | 0.59 | 1.12 | 177 |
| stroke 49 | 97 % → 97 % | 270.0 px | 0.60 | 1.00 | 144 |
| stroke 50 | 49 % → 88 % | 297.6 px | 0.52 | 1.77 | 158 |
| stroke 51 | 67 % → 98 % | 462.3 px | 0.53 | 1.45 | 72 |
| stroke 52 | 78 % → 83 % | 745.4 px | 0.59 | 1.07 | 88 |
| stroke 53 | 66 % → 87 % | 489.4 px | 0.55 | 1.31 | 128 |
| stroke 54 | 80 % → 98 % | 794.6 px | 0.56 | 1.22 | 86 |
| stroke 55 | 95 % → 97 % | 816.8 px | 0.59 | 1.01 | 82 |
| stroke 56 | 97 % → 97 % | 335.3 px | 0.59 | 1.00 | 115 |
| stroke 57 | 97 % → 97 % | 604.4 px | 0.59 | 1.00 | 101 |
| stroke 58 | 80 % → 79 % | 656.8 px | 0.59 | 0.99 | 84 |
| stroke 59 | 34 % → 95 % | 279.2 px | 0.45 | 2.78 | 49 |
| stroke 60 | 14 % → 58 % | 47.6 px | 0.49 | 4.06 | 134 |
| stroke 61 | 15 % → 86 % | 71.0 px | 0.41 | 5.74 | 127 |
| stroke 62 | 30 % → 71 % | 87.9 px | 0.44 | 2.33 | 237 |
| stroke 63 | 35 % → 73 % | 253.3 px | 0.43 | 2.07 | 109 |
| stroke 64 | 46 % → 77 % | 246.7 px | 0.45 | 1.68 | 84 |
| stroke 65 | 39 % → 45 % | 191.4 px | 0.55 | 1.16 | 48 |
| stroke 66 | 41 % → 50 % | 287.6 px | 0.50 | 1.23 | 56 |
| stroke 67 | 39 % → 74 % | 224.7 px | 0.43 | 1.89 | 120 |
| stroke 68 | 9 % → 79 % | 52.3 px | 0.18 | 8.96 | 36 |
| stroke 69 | 11 % → 79 % | 68.4 px | 0.13 | 7.30 | 31 |
| stroke 70 | 11 % → 78 % | 184.9 px | 0.15 | 6.98 | 19 |
| stroke 71 | 15 % → 77 % | 231.2 px | 0.24 | 5.08 | 7 |
| stroke 72 | 13 % → 78 % | 94.5 px | 0.12 | 6.08 | 31 |
| stroke 73 | 15 % → 94 % | 82.6 px | 0.26 | 6.45 | 20 |
| stroke 74 | 12 % → 92 % | 68.7 px | 0.28 | 7.45 | 15 |
| stroke 75 | 21 % → 92 % | 236.1 px | 0.28 | 4.49 | 16 |
| stroke 76 | 24 % → 94 % | 150.2 px | 0.26 | 3.93 | 32 |
| stroke 77 | 20 % → 92 % | 140.1 px | 0.28 | 4.63 | 15 |
| stroke 78 | 22 % → 92 % | 148.3 px | 0.28 | 4.22 | 23 |
| stroke 79 | 23 % → 94 % | 367.9 px | 0.25 | 4.04 | 8 |
| stroke 80 | 24 % → 94 % | 419.5 px | 0.24 | 3.90 | 14 |
| stroke 81 | 28 % → 92 % | 285.6 px | 0.30 | 3.33 | 10 |
| stroke 82 | 33 % → 92 % | 295.0 px | 0.31 | 2.80 | 27 |
| stroke 83 | 32 % → 93 % | 411.3 px | 0.28 | 2.90 | 13 |
| stroke 84 | 20 % → 94 % | 94.1 px | 0.18 | 4.72 | 69 |
| stroke 85 | 20 % → 95 % | 139.5 px | 0.20 | 4.71 | 32 |
| stroke 86 | 27 % → 93 % | 112.1 px | 0.20 | 3.47 | 90 |
| stroke 87 | 17 % → 95 % | 113.8 px | 0.12 | 5.68 | 19 |
| stroke 88 | 29 % → 96 % | 195.8 px | 0.17 | 3.31 | 45 |
| stroke 89 | 42 % → 93 % | 528.7 px | 0.25 | 2.23 | 14 |
| stroke 90 | 39 % → 95 % | 449.4 px | 0.23 | 2.44 | 19 |
| stroke 91 | 23 % → 95 % | 201.7 px | 0.14 | 4.08 | 27 |
| stroke 92 | 27 % → 95 % | 484.4 px | 0.17 | 3.50 | 12 |
| stroke 93 | 37 % → 95 % | 555.1 px | 0.22 | 2.55 | 9 |
| stroke 94 | 49 % → 92 % | 617.4 px | 0.27 | 1.89 | 11 |
| stroke 95 | 38 % → 97 % | 358.3 px | 0.26 | 2.56 | 38 |
| stroke 96 | 40 % → 96 % | 325.3 px | 0.29 | 2.37 | 63 |
| stroke 97 | 44 % → 97 % | 504.0 px | 0.29 | 2.21 | 35 |
| stroke 98 | 45 % → 98 % | 837.5 px | 0.31 | 2.19 | 21 |
| stroke 99 | 57 % → 95 % | 1189.1 px | 0.39 | 1.67 | 43 |
| stroke 100 | 39 % → 88 % | 726.5 px | 0.29 | 2.26 | 13 |
| stroke 101 | 40 % → 88 % | 721.1 px | 0.30 | 2.23 | 10 |
| stroke 102 | 60 % → 98 % | 826.9 px | 0.43 | 1.63 | 32 |
| stroke 103 | 64 % → 98 % | 1216.6 px | 0.47 | 1.53 | 17 |
| stroke 104 | 52 % → 98 % | 1320.7 px | 0.41 | 1.88 | 13 |
| stroke 105 | 51 % → 97 % | 773.5 px | 0.44 | 1.88 | 27 |
| stroke 106 | 57 % → 99 % | 832.0 px | 0.48 | 1.75 | 34 |
| stroke 107 | 63 % → 98 % | 719.1 px | 0.44 | 1.56 | 35 |
| stroke 108 | 4 % → 91 % | 26.5 px | 0.34 | 23.92 | 48 |
| stroke 109 | 7 % → 86 % | 45.0 px | 0.27 | 12.72 | 57 |
| stroke 110 | 8 % → 90 % | 53.6 px | 0.26 | 11.11 | 49 |
| stroke 111 | 10 % → 95 % | 107.4 px | 0.21 | 9.47 | 23 |
| stroke 112 | 14 % → 89 % | 208.1 px | 0.32 | 6.30 | 18 |
| stroke 113 | 9 % → 95 % | 222.0 px | 0.20 | 10.94 | 12 |
| stroke 114 | 16 % → 92 % | 143.0 px | 0.31 | 5.93 | 43 |
| stroke 115 | 11 % → 97 % | 186.1 px | 0.34 | 8.61 | 22 |
| stroke 116 | 16 % → 83 % | 393.0 px | 0.26 | 5.24 | 6 |
| stroke 117 | 17 % → 84 % | 310.9 px | 0.33 | 5.08 | 13 |
| stroke 118 | 18 % → 91 % | 434.2 px | 0.29 | 5.20 | 8 |
| stroke 119 | 18 % → 86 % | 222.1 px | 0.30 | 4.82 | 22 |
| stroke 120 | 9 % → 93 % | 195.9 px | 0.34 | 10.06 | 8 |
| stroke 121 | 13 % → 90 % | 317.5 px | 0.33 | 7.04 | 9 |
| stroke 122 | 8 % → 93 % | 119.2 px | 0.34 | 11.56 | 11 |
| stroke 123 | 12 % → 95 % | 313.3 px | 0.23 | 7.73 | 7 |
| stroke 124 | 17 % → 93 % | 421.6 px | 0.33 | 5.47 | 10 |
| stroke 125 | 14 % → 90 % | 310.3 px | 0.22 | 6.27 | 14 |
| stroke 126 | 17 % → 92 % | 358.7 px | 0.27 | 5.35 | 10 |
| stroke 127 | 79 % → 94 % | 1508.8 px | 0.50 | 1.18 | 19 |
| stroke 128 | 80 % → 94 % | 1016.0 px | 0.51 | 1.17 | 28 |
| stroke 129 | 32 % → 96 % | 309.3 px | 0.34 | 3.00 | 21 |
| stroke 130 | 48 % → 100 % | 344.2 px | 0.45 | 2.09 | 79 |
| stroke 131 | 37 % → 96 % | 483.8 px | 0.37 | 2.62 | 28 |
| stroke 132 | 55 % → 99 % | 1045.6 px | 0.46 | 1.81 | 12 |
| stroke 133 | 40 % → 100 % | 277.4 px | 0.44 | 2.50 | 60 |
| stroke 134 | 59 % → 99 % | 664.0 px | 0.47 | 1.68 | 34 |
| stroke 135 | 53 % → 100 % | 412.9 px | 0.46 | 1.88 | 61 |
| stroke 136 | 42 % → 97 % | 891.5 px | 0.42 | 2.30 | 14 |
| stroke 137 | 27 % → 100 % | 572.6 px | 0.41 | 3.75 | 11 |
| stroke 138 | 60 % → 100 % | 1502.0 px | 0.46 | 1.65 | 11 |
| stroke 139 | 55 % → 100 % | 779.8 px | 0.46 | 1.80 | 25 |
| stroke 140 | 50 % → 100 % | 1272.3 px | 0.44 | 2.00 | 10 |
| stroke 141 | 40 % → 96 % | 539.6 px | 0.35 | 2.37 | 24 |
| stroke 142 | 52 % → 95 % | 1304.9 px | 0.44 | 1.82 | 14 |
| stroke 143 | 69 % → 100 % | 1270.2 px | 0.48 | 1.46 | 19 |
| stroke 144 | 63 % → 100 % | 1555.0 px | 0.47 | 1.58 | 29 |
| stroke 145 | 49 % → 96 % | 1058.9 px | 0.43 | 1.96 | 19 |
| stroke 146 | 58 % → 100 % | 1469.3 px | 0.46 | 1.71 | 8 |
| stroke 147 | 69 % → 100 % | 1744.7 px | 0.48 | 1.44 | 14 |
| stroke 148 | 77 % → 95 % | 1101.6 px | 0.50 | 1.24 | 27 |
| stroke 149 | 74 % → 95 % | 1064.8 px | 0.49 | 1.29 | 69 |
| stroke 150 | 43 % → 100 % | 278.7 px | 0.41 | 2.35 | 81 |
| stroke 151 | 49 % → 100 % | 341.5 px | 0.40 | 2.03 | 141 |
| stroke 152 | 31 % → 100 % | 416.5 px | 0.39 | 3.23 | 11 |
| stroke 153 | 40 % → 100 % | 511.1 px | 0.39 | 2.47 | 42 |
| stroke 154 | 36 % → 100 % | 332.8 px | 0.45 | 2.78 | 37 |
| stroke 155 | 29 % → 100 % | 272.8 px | 0.44 | 3.38 | 62 |
| stroke 156 | 60 % → 100 % | 996.2 px | 0.48 | 1.66 | 14 |
| stroke 157 | 33 % → 100 % | 334.6 px | 0.44 | 3.04 | 68 |
| stroke 158 | 60 % → 100 % | 619.8 px | 0.50 | 1.67 | 37 |
| stroke 159 | 93 % → 100 % | 1437.3 px | 0.55 | 1.07 | 17 |
| stroke 160 | 89 % → 100 % | 1661.5 px | 0.55 | 1.12 | 17 |
| stroke 161 | 47 % → 100 % | 516.1 px | 0.46 | 2.14 | 36 |
| stroke 162 | 84 % → 100 % | 733.1 px | 0.53 | 1.19 | 66 |
| stroke 163 | 33 % → 99 % | 689.3 px | 0.44 | 3.04 | 20 |
| stroke 164 | 65 % → 100 % | 1068.9 px | 0.48 | 1.53 | 16 |
| stroke 165 | 24 % → 99 % | 616.4 px | 0.43 | 4.07 | 12 |
| stroke 166 | 46 % → 100 % | 1146.1 px | 0.46 | 2.17 | 13 |
| stroke 167 | 62 % → 100 % | 1326.1 px | 0.50 | 1.60 | 17 |
| stroke 168 | 54 % → 100 % | 1342.9 px | 0.46 | 1.85 | 10 |
| stroke 169 | 86 % → 100 % | 1266.6 px | 0.52 | 1.16 | 27 |
| stroke 170 | 9 % → 72 % | 61.5 px | 0.33 | 8.31 | 49 |
| stroke 171 | 20 % → 67 % | 137.7 px | 0.32 | 3.33 | 45 |
| stroke 172 | 26 % → 77 % | 229.2 px | 0.39 | 2.96 | 33 |
| stroke 173 | 12 % → 72 % | 312.4 px | 0.33 | 5.74 | 7 |
| stroke 174 | 21 % → 65 % | 199.2 px | 0.32 | 3.07 | 26 |
| stroke 175 | 15 % → 63 % | 108.9 px | 0.33 | 4.29 | 48 |
| stroke 176 | 20 % → 75 % | 197.3 px | 0.35 | 3.81 | 36 |
| stroke 177 | 30 % → 82 % | 426.3 px | 0.37 | 2.71 | 17 |
| stroke 178 | 28 % → 65 % | 511.5 px | 0.32 | 2.33 | 10 |
| stroke 179 | 24 % → 66 % | 277.0 px | 0.32 | 2.75 | 22 |
| stroke 180 | 23 % → 77 % | 486.2 px | 0.34 | 3.38 | 8 |
| stroke 181 | 26 % → 74 % | 653.3 px | 0.33 | 2.81 | 12 |
| stroke 182 | 18 % → 76 % | 337.8 px | 0.33 | 4.13 | 9 |
| stroke 183 | 23 % → 68 % | 348.5 px | 0.33 | 2.94 | 19 |
| stroke 184 | 34 % → 77 % | 488.1 px | 0.39 | 2.25 | 26 |
| stroke 185 | 27 % → 73 % | 288.3 px | 0.33 | 2.68 | 44 |
| stroke 186 | 23 % → 78 % | 328.4 px | 0.34 | 3.31 | 18 |
| stroke 187 | 21 % → 69 % | 322.6 px | 0.32 | 3.21 | 19 |
| stroke 188 | 31 % → 71 % | 766.4 px | 0.32 | 2.29 | 13 |
| stroke 189 | 19 % → 96 % | 340.7 px | 0.42 | 5.13 | 19 |
| stroke 190 | 20 % → 96 % | 301.5 px | 0.42 | 4.79 | 16 |
| stroke 191 | 20 % → 96 % | 141.9 px | 0.41 | 4.82 | 55 |
| stroke 192 | 33 % → 95 % | 446.1 px | 0.41 | 2.89 | 14 |
| stroke 193 | 30 % → 95 % | 318.6 px | 0.41 | 3.14 | 18 |
| stroke 194 | 46 % → 96 % | 266.6 px | 0.41 | 2.07 | 37 |
| stroke 195 | 48 % → 95 % | 577.3 px | 0.41 | 1.99 | 7 |
| stroke 196 | 37 % → 98 % | 434.4 px | 0.40 | 2.68 | 13 |
| stroke 197 | 42 % → 96 % | 476.9 px | 0.40 | 2.29 | 28 |
| stroke 198 | 35 % → 99 % | 624.6 px | 0.40 | 2.79 | 8 |
| stroke 199 | 42 % → 97 % | 372.0 px | 0.40 | 2.28 | 30 |
| stroke 200 | 35 % → 99 % | 436.2 px | 0.40 | 2.80 | 13 |
| stroke 201 | 42 % → 90 % | 984.5 px | 0.32 | 2.12 | 4 |
| stroke 202 | 68 % → 92 % | 1424.2 px | 0.45 | 1.35 | 12 |
| stroke 203 | 57 % → 94 % | 1002.3 px | 0.41 | 1.65 | 17 |
| stroke 204 | 86 % → 98 % | 1827.6 px | 0.55 | 1.14 | 7 |
| stroke 205 | 16 % → 100 % | 302.9 px | 0.40 | 6.29 | 10 |
| stroke 206 | 25 % → 79 % | 207.1 px | 0.48 | 3.22 | 33 |
| stroke 207 | 32 % → 90 % | 192.7 px | 0.35 | 2.78 | 89 |
| stroke 208 | 27 % → 85 % | 434.7 px | 0.48 | 3.14 | 7 |
| stroke 209 | 48 % → 85 % | 612.7 px | 0.53 | 1.76 | 22 |
| stroke 210 | 49 % → 95 % | 1072.4 px | 0.38 | 1.95 | 3 |
| stroke 211 | 59 % → 94 % | 377.7 px | 0.50 | 1.59 | 53 |
| stroke 212 | 47 % → 60 % | 318.9 px | 0.45 | 1.26 | 33 |
| stroke 213 | 42 % → 44 % | 497.8 px | 0.53 | 1.04 | 8 |
| stroke 214 | 52 % → 99 % | 264.2 px | 0.36 | 1.91 | 247 |
| stroke 215 | 49 % → 94 % | 285.2 px | 0.30 | 1.93 | 243 |
| stroke 216 | 47 % → 95 % | 258.1 px | 0.38 | 2.00 | 338 |
| stroke 217 | 57 % → 100 % | 253.6 px | 0.38 | 1.75 | 361 |
| stroke 218 | 56 % → 97 % | 272.7 px | 0.29 | 1.72 | 362 |
| stroke 219 | 63 % → 95 % | 532.5 px | 0.37 | 1.49 | 123 |
| stroke 220 | 61 % → 95 % | 723.2 px | 0.34 | 1.57 | 91 |
| stroke 221 | 39 % → 100 % | 399.6 px | 0.38 | 2.55 | 65 |
| stroke 222 | 63 % → 98 % | 288.7 px | 0.34 | 1.54 | 350 |
| stroke 223 | 62 % → 99 % | 393.8 px | 0.35 | 1.60 | 163 |
| stroke 224 | 65 % → 97 % | 546.0 px | 0.33 | 1.48 | 112 |
| stroke 225 | 50 % → 100 % | 373.0 px | 0.39 | 2.01 | 145 |
| stroke 226 | 52 % → 93 % | 446.1 px | 0.26 | 1.80 | 138 |
| stroke 227 | 62 % → 99 % | 343.6 px | 0.37 | 1.60 | 191 |
| stroke 228 | 76 % → 100 % | 389.0 px | 0.37 | 1.31 | 233 |
| stroke 229 | 67 % → 98 % | 475.8 px | 0.31 | 1.46 | 160 |
| stroke 230 | 84 % → 100 % | 550.4 px | 0.39 | 1.18 | 151 |
| stroke 231 | 67 % → 98 % | 420.7 px | 0.31 | 1.45 | 207 |
| stroke 232 | 76 % → 99 % | 908.1 px | 0.34 | 1.31 | 56 |
| stroke 233 | 64 % → 97 % | 828.4 px | 0.35 | 1.51 | 51 |
| stroke 234 | 50 % → 92 % | 417.5 px | 0.25 | 1.83 | 131 |
| stroke 235 | 58 % → 98 % | 590.1 px | 0.40 | 1.71 | 69 |
| stroke 236 | 79 % → 97 % | 861.9 px | 0.35 | 1.23 | 83 |
| stroke 237 | 66 % → 100 % | 679.4 px | 0.39 | 1.51 | 88 |
| stroke 238 | 76 % → 100 % | 947.0 px | 0.37 | 1.32 | 68 |
| stroke 239 | 76 % → 98 % | 925.8 px | 0.33 | 1.29 | 54 |
| stroke 240 | 58 % → 100 % | 726.0 px | 0.37 | 1.72 | 44 |
| stroke 241 | 73 % → 100 % | 385.8 px | 0.50 | 1.36 | 234 |
| stroke 242 | 90 % → 100 % | 1063.9 px | 0.52 | 1.11 | 60 |
| stroke 243 | 85 % → 100 % | 694.8 px | 0.43 | 1.17 | 99 |
| stroke 244 | 80 % → 100 % | 427.9 px | 0.41 | 1.25 | 169 |
| stroke 245 | 87 % → 100 % | 564.6 px | 0.42 | 1.14 | 151 |
| stroke 246 | 81 % → 100 % | 887.2 px | 0.43 | 1.23 | 75 |
| stroke 247 | 40 % → 96 % | 346.0 px | 0.41 | 2.39 | 66 |
| stroke 248 | 63 % → 99 % | 391.1 px | 0.38 | 1.57 | 116 |
| stroke 249 | 60 % → 100 % | 426.0 px | 0.38 | 1.65 | 124 |
| stroke 250 | 70 % → 98 % | 343.4 px | 0.40 | 1.40 | 160 |
| stroke 251 | 70 % → 96 % | 554.6 px | 0.41 | 1.38 | 72 |
| stroke 252 | 46 % → 88 % | 266.0 px | 0.48 | 1.90 | 148 |
| stroke 253 | 59 % → 89 % | 629.4 px | 0.51 | 1.51 | 75 |
| stroke 254 | 55 % → 96 % | 274.1 px | 0.45 | 1.76 | 142 |
| stroke 255 | 44 % → 99 % | 591.8 px | 0.30 | 2.25 | 13 |
| stroke 256 | 21 % → 55 % | 409.5 px | 0.52 | 2.56 | 9 |
| stroke 257 | 56 % → 100 % | 289.8 px | 0.46 | 1.78 | 57 |
| stroke 258 | 32 % → 66 % | 797.9 px | 0.51 | 2.04 | 4 |
| stroke 259 | 47 % → 78 % | 209.0 px | 0.46 | 1.67 | 193 |
| stroke 260 | 47 % → 73 % | 249.7 px | 0.45 | 1.56 | 174 |
| stroke 261 | 45 % → 61 % | 220.3 px | 0.50 | 1.37 | 263 |
| stroke 262 | 63 % → 93 % | 384.0 px | 0.38 | 1.49 | 134 |
| stroke 263 | 73 % → 85 % | 448.0 px | 0.49 | 1.16 | 155 |
| stroke 264 | 63 % → 78 % | 340.7 px | 0.51 | 1.25 | 170 |
| stroke 265 | 70 % → 78 % | 861.7 px | 0.54 | 1.12 | 47 |
| stroke 266 | 55 % → 89 % | 451.7 px | 0.33 | 1.61 | 90 |
| stroke 267 | 58 % → 70 % | 451.8 px | 0.52 | 1.22 | 103 |
| stroke 268 | 57 % → 77 % | 549.2 px | 0.38 | 1.36 | 64 |
| stroke 269 | 70 % → 96 % | 630.2 px | 0.39 | 1.36 | 109 |
| stroke 270 | 71 % → 78 % | 882.5 px | 0.49 | 1.10 | 59 |
| stroke 271 | 70 % → 89 % | 327.5 px | 0.47 | 1.27 | 267 |
| stroke 272 | 82 % → 90 % | 347.3 px | 0.47 | 1.09 | 231 |
| stroke 273 | 80 % → 95 % | 654.3 px | 0.45 | 1.19 | 86 |
| stroke 274 | 82 % → 98 % | 446.1 px | 0.47 | 1.19 | 168 |
| stroke 275 | 86 % → 95 % | 458.7 px | 0.46 | 1.11 | 167 |
| stroke 276 | 78 % → 97 % | 420.7 px | 0.45 | 1.24 | 204 |
| stroke 277 | 87 % → 93 % | 925.0 px | 0.47 | 1.06 | 64 |
| stroke 278 | 81 % → 84 % | 837.2 px | 0.48 | 1.04 | 63 |
| stroke 279 | 77 % → 98 % | 312.4 px | 0.39 | 1.27 | 264 |
| stroke 280 | 79 % → 100 % | 766.7 px | 0.41 | 1.26 | 42 |
| stroke 281 | 87 % → 98 % | 386.9 px | 0.40 | 1.12 | 303 |
| stroke 282 | 89 % → 97 % | 452.7 px | 0.40 | 1.09 | 177 |
| stroke 283 | 93 % → 100 % | 675.9 px | 0.42 | 1.08 | 115 |
| stroke 284 | 95 % → 100 % | 993.3 px | 0.39 | 1.05 | 57 |
| stroke 285 | 93 % → 100 % | 740.5 px | 0.39 | 1.07 | 123 |
| stroke 286 | 88 % → 97 % | 560.6 px | 0.39 | 1.11 | 95 |
| stroke 287 | 90 % → 98 % | 551.3 px | 0.39 | 1.09 | 172 |
| stroke 288 | 90 % → 97 % | 917.9 px | 0.40 | 1.09 | 33 |
| stroke 289 | 88 % → 97 % | 869.4 px | 0.40 | 1.09 | 64 |
| stroke 290 | 95 % → 100 % | 698.0 px | 0.39 | 1.04 | 100 |
| stroke 291 | 95 % → 99 % | 877.5 px | 0.38 | 1.05 | 79 |
| stroke 292 | 13 % → 100 % | 52.1 px | 0.00 | 7.70 | 77 |
| stroke 293 | 16 % → 77 % | 75.1 px | 0.04 | 4.76 | 154 |
| stroke 294 | 36 % → 79 % | 151.8 px | 0.04 | 2.18 | 89 |
| stroke 295 | 32 % → 82 % | 179.8 px | 0.12 | 2.58 | 152 |
| stroke 296 | 22 % → 100 % | 60.6 px | 0.00 | 4.48 | 141 |
| stroke 297 | 28 % → 80 % | 141.4 px | 0.05 | 2.84 | 140 |
| stroke 298 | 25 % → 100 % | 106.8 px | 0.02 | 3.96 | 123 |
| stroke 299 | 34 % → 74 % | 210.2 px | 0.05 | 2.22 | 87 |
| stroke 300 | 36 % → 93 % | 141.7 px | 0.00 | 2.57 | 145 |
| stroke 301 | 39 % → 99 % | 185.3 px | 0.11 | 2.53 | 169 |
| stroke 302 | 49 % → 86 % | 188.9 px | 0.14 | 1.74 | 206 |
| stroke 303 | 41 % → 75 % | 187.6 px | 0.06 | 1.84 | 94 |
| stroke 304 | 62 % → 100 % | 206.5 px | 0.00 | 1.61 | 64 |
| stroke 305 | 48 % → 98 % | 266.3 px | 0.11 | 2.03 | 142 |
| stroke 306 | 62 % → 99 % | 244.9 px | 0.03 | 1.59 | 178 |
| stroke 307 | 74 % → 99 % | 338.4 px | 0.03 | 1.34 | 170 |
| stroke 308 | 39 % → 92 % | 168.2 px | 0.00 | 2.36 | 243 |
| stroke 309 | 54 % → 97 % | 292.6 px | 0.00 | 1.78 | 145 |
| stroke 310 | 44 % → 74 % | 212.9 px | 0.01 | 1.69 | 100 |
| stroke 311 | 59 % → 96 % | 310.0 px | 0.00 | 1.63 | 151 |
| stroke 312 | 74 % → 93 % | 326.6 px | 0.00 | 1.25 | 88 |
| stroke 313 | 75 % → 91 % | 319.1 px | 0.12 | 1.22 | 198 |
| stroke 314 | 61 % → 83 % | 256.8 px | 0.12 | 1.35 | 111 |
| stroke 315 | 74 % → 100 % | 682.0 px | 0.00 | 1.34 | 32 |
| stroke 316 | 59 % → 78 % | 323.9 px | 0.02 | 1.32 | 73 |
| stroke 317 | 75 % → 99 % | 473.3 px | 0.08 | 1.32 | 113 |
| stroke 318 | 80 % → 99 % | 367.3 px | 0.01 | 1.24 | 132 |
| stroke 319 | 61 % → 94 % | 454.2 px | 0.00 | 1.53 | 83 |
| stroke 320 | 83 % → 99 % | 764.6 px | 0.00 | 1.20 | 36 |
| stroke 321 | 86 % → 100 % | 294.3 px | 0.00 | 1.16 | 107 |
| stroke 322 | 72 % → 100 % | 704.9 px | 0.00 | 1.38 | 40 |
| stroke 323 | 80 % → 99 % | 320.3 px | 0.00 | 1.24 | 45 |
| stroke 324 | 73 % → 81 % | 364.2 px | 0.15 | 1.11 | 111 |
| stroke 325 | 63 % → 81 % | 515.8 px | 0.10 | 1.27 | 101 |
| stroke 326 | 77 % → 100 % | 471.5 px | 0.00 | 1.30 | 68 |
| stroke 327 | 54 % → 83 % | 285.3 px | 0.12 | 1.55 | 171 |
| stroke 328 | 78 % → 100 % | 398.0 px | 0.00 | 1.28 | 64 |
| stroke 329 | 57 % → 79 % | 278.7 px | 0.03 | 1.38 | 95 |
| stroke 330 | 55 % → 81 % | 212.9 px | 0.04 | 1.49 | 134 |
| stroke 331 | 55 % → 84 % | 341.9 px | 0.00 | 1.53 | 91 |
| stroke 332 | 79 % → 99 % | 531.6 px | 0.00 | 1.26 | 62 |
| stroke 333 | 76 % → 100 % | 506.3 px | 0.01 | 1.31 | 122 |
| stroke 334 | 92 % → 99 % | 501.7 px | 0.00 | 1.08 | 84 |
| stroke 335 | 95 % → 100 % | 555.5 px | 0.00 | 1.05 | 91 |
| stroke 336 | 55 % → 79 % | 339.9 px | 0.02 | 1.44 | 92 |
| stroke 337 | 70 % → 80 % | 529.2 px | 0.12 | 1.14 | 91 |
| stroke 338 | 73 % → 76 % | 481.2 px | 0.23 | 1.05 | 50 |
| stroke 339 | 59 % → 78 % | 247.7 px | 0.02 | 1.32 | 128 |
| stroke 340 | 85 % → 92 % | 371.6 px | 0.00 | 1.08 | 101 |
| stroke 341 | 92 % → 98 % | 1134.1 px | 0.15 | 1.07 | 34 |
| stroke 342 | 90 % → 99 % | 850.8 px | 0.01 | 1.10 | 46 |
| stroke 343 | 86 % → 100 % | 794.6 px | 0.00 | 1.17 | 38 |
| stroke 344 | 98 % → 100 % | 817.9 px | 0.00 | 1.02 | 32 |
| stroke 345 | 87 % → 94 % | 441.0 px | 0.00 | 1.09 | 86 |
| stroke 346 | 85 % → 88 % | 401.2 px | 0.00 | 1.04 | 37 |
| stroke 347 | 92 % → 100 % | 465.0 px | 0.00 | 1.08 | 44 |
| stroke 348 | 63 % → 89 % | 500.5 px | 0.00 | 1.41 | 125 |
| stroke 349 | 51 % → 73 % | 352.3 px | 0.04 | 1.45 | 78 |
| stroke 350 | 69 % → 81 % | 366.0 px | 0.06 | 1.18 | 72 |
| stroke 351 | 87 % → 94 % | 645.3 px | 0.00 | 1.08 | 44 |
| stroke 352 | 98 % → 99 % | 474.3 px | 0.00 | 1.01 | 48 |
| stroke 353 | 69 % → 82 % | 438.0 px | 0.09 | 1.19 | 110 |
| stroke 354 | 69 % → 84 % | 756.2 px | 0.21 | 1.21 | 30 |
| stroke 355 | 97 % → 100 % | 333.0 px | 0.00 | 1.03 | 83 |
| stroke 356 | 74 % → 88 % | 676.3 px | 0.00 | 1.19 | 48 |
| stroke 357 | 98 % → 100 % | 562.1 px | 0.00 | 1.02 | 77 |
| stroke 358 | 97 % → 99 % | 881.2 px | 0.00 | 1.02 | 41 |
| stroke 359 | 99 % → 99 % | 830.9 px | 0.00 | 1.01 | 49 |
| stroke 360 | 77 % → 81 % | 618.1 px | 0.02 | 1.05 | 43 |
| stroke 361 | 99 % → 100 % | 742.2 px | 0.00 | 1.01 | 44 |
| stroke 362 | 59 % → 77 % | 305.4 px | 0.01 | 1.30 | 71 |
| stroke 363 | 89 % → 99 % | 1138.9 px | 0.07 | 1.11 | 32 |
| stroke 364 | 87 % → 89 % | 884.7 px | 0.12 | 1.03 | 61 |
| stroke 365 | 70 % → 77 % | 456.4 px | 0.05 | 1.10 | 65 |
| stroke 366 | 99 % → 100 % | 616.8 px | 0.00 | 1.01 | 74 |
| stroke 367 | 66 % → 75 % | 665.0 px | 0.03 | 1.14 | 35 |
| stroke 368 | 62 % → 76 % | 556.0 px | 0.02 | 1.23 | 43 |
| stroke 369 | 93 % → 100 % | 1084.1 px | 0.00 | 1.08 | 39 |
| stroke 370 | 83 % → 87 % | 720.1 px | 0.14 | 1.05 | 78 |
| stroke 371 | 91 % → 93 % | 592.1 px | 0.00 | 1.02 | 66 |
| stroke 372 | 60 % → 79 % | 511.2 px | 0.03 | 1.32 | 55 |
| stroke 373 | 87 % → 89 % | 965.4 px | 0.23 | 1.02 | 67 |
| stroke 374 | 81 % → 100 % | 963.5 px | 0.00 | 1.23 | 34 |
| stroke 375 | 75 % → 75 % | 427.4 px | 0.15 | 1.00 | 64 |
| stroke 376 | 95 % → 97 % | 750.9 px | 0.00 | 1.02 | 35 |
| stroke 377 | 100 % → 100 % | 425.9 px | 0.00 | 1.00 | 42 |
| stroke 378 | 88 % → 99 % | 818.2 px | 0.19 | 1.13 | 51 |
| stroke 379 | 91 % → 100 % | 1070.3 px | 0.03 | 1.10 | 36 |
| stroke 380 | 91 % → 90 % | 674.0 px | 0.09 | 1.00 | 67 |
| stroke 381 | 51 % → 70 % | 543.2 px | 0.04 | 1.36 | 42 |
| stroke 382 | 87 % → 99 % | 738.7 px | 0.06 | 1.14 | 73 |
| stroke 383 | 63 % → 79 % | 653.6 px | 0.12 | 1.24 | 43 |
| stroke 384 | 91 % → 93 % | 844.1 px | 0.00 | 1.02 | 33 |
| stroke 385 | 92 % → 93 % | 1219.7 px | 0.19 | 1.01 | 59 |
| stroke 386 | 57 % → 74 % | 505.8 px | 0.07 | 1.29 | 49 |
| stroke 387 | 67 % → 76 % | 756.5 px | 0.12 | 1.12 | 28 |
| stroke 388 | 79 % → 86 % | 899.4 px | 0.22 | 1.10 | 46 |
| stroke 389 | 100 % → 99 % | 965.6 px | 0.04 | 1.00 | 45 |
| stroke 390 | 64 % → 73 % | 835.1 px | 0.01 | 1.14 | 34 |
| stroke 391 | 97 % → 99 % | 704.5 px | 0.00 | 1.01 | 24 |
| stroke 392 | 92 % → 100 % | 1005.2 px | 0.00 | 1.09 | 50 |
| stroke 393 | 72 % → 76 % | 699.5 px | 0.02 | 1.05 | 32 |
| stroke 394 | 100 % → 100 % | 1147.7 px | 0.00 | 1.00 | 31 |
| stroke 395 | 78 % → 84 % | 822.2 px | 0.07 | 1.07 | 53 |
| stroke 396 | 97 % → 99 % | 1125.8 px | 0.00 | 1.03 | 78 |
| stroke 397 | 99 % → 99 % | 850.3 px | 0.02 | 1.00 | 61 |
| stroke 398 | 78 % → 82 % | 709.4 px | 0.04 | 1.04 | 38 |
| stroke 399 | 100 % → 100 % | 910.4 px | 0.00 | 1.00 | 26 |
| stroke 400 | 97 % → 98 % | 602.6 px | 0.00 | 1.02 | 70 |
| stroke 401 | 75 % → 84 % | 946.2 px | 0.08 | 1.11 | 34 |
| stroke 402 | 61 % → 78 % | 586.0 px | 0.04 | 1.27 | 51 |
| stroke 403 | 95 % → 98 % | 1192.9 px | 0.00 | 1.03 | 35 |
| stroke 404 | 93 % → 99 % | 1225.7 px | 0.05 | 1.07 | 26 |
| stroke 405 | 92 % → 95 % | 913.8 px | 0.00 | 1.03 | 42 |
| stroke 406 | 86 % → 88 % | 1031.6 px | 0.00 | 1.02 | 32 |
| stroke 407 | 69 % → 80 % | 899.7 px | 0.05 | 1.16 | 26 |
| stroke 408 | 59 % → 67 % | 445.5 px | 0.03 | 1.13 | 28 |
| stroke 409 | 100 % → 100 % | 781.2 px | 0.00 | 1.00 | 30 |
| stroke 410 | 83 % → 87 % | 1054.9 px | 0.11 | 1.04 | 29 |
| stroke 411 | 90 % → 91 % | 921.1 px | 0.00 | 1.01 | 30 |
| stroke 412 | 74 % → 74 % | 564.8 px | 0.00 | 1.00 | 31 |
| stroke 413 | 92 % → 92 % | 1127.0 px | 0.12 | 1.00 | 35 |
| stroke 414 | 82 % → 99 % | 1051.1 px | 0.12 | 1.21 | 51 |
| stroke 415 | 100 % → 100 % | 764.1 px | 0.00 | 1.00 | 59 |
| stroke 416 | 95 % → 99 % | 1161.5 px | 0.10 | 1.05 | 31 |
| stroke 417 | 84 % → 88 % | 997.2 px | 0.00 | 1.04 | 31 |
| stroke 418 | 79 % → 100 % | 905.3 px | 0.07 | 1.26 | 38 |
| stroke 419 | 25 % → 82 % | 169.2 px | 0.09 | 3.33 | 27 |
| stroke 420 | 50 % → 75 % | 275.2 px | 0.03 | 1.50 | 76 |
| stroke 421 | 48 % → 73 % | 356.3 px | 0.04 | 1.52 | 32 |
| stroke 422 | 58 % → 77 % | 264.5 px | 0.09 | 1.34 | 137 |
| stroke 423 | 59 % → 77 % | 390.5 px | 0.09 | 1.31 | 85 |
| stroke 424 | 62 % → 83 % | 391.1 px | 0.18 | 1.34 | 93 |
| stroke 425 | 62 % → 76 % | 640.0 px | 0.05 | 1.22 | 54 |
| stroke 426 | 64 % → 76 % | 304.6 px | 0.05 | 1.18 | 91 |
| stroke 427 | 73 % → 81 % | 435.2 px | 0.08 | 1.11 | 66 |
| stroke 428 | 83 % → 92 % | 483.5 px | 0.10 | 1.11 | 54 |
| stroke 429 | 74 % → 77 % | 756.7 px | 0.01 | 1.04 | 31 |
| stroke 430 | 69 % → 72 % | 550.2 px | 0.06 | 1.03 | 68 |
| stroke 431 | 77 % → 88 % | 482.5 px | 0.25 | 1.14 | 55 |
| stroke 432 | 75 % → 75 % | 408.6 px | 0.05 | 1.01 | 130 |
| stroke 433 | 74 % → 77 % | 360.3 px | 0.10 | 1.05 | 255 |
| stroke 434 | 74 % → 77 % | 573.7 px | 0.07 | 1.04 | 50 |
| stroke 435 | 76 % → 83 % | 780.2 px | 0.11 | 1.08 | 52 |
| stroke 436 | 74 % → 80 % | 665.6 px | 0.17 | 1.08 | 67 |
| stroke 437 | 87 % → 93 % | 442.1 px | 0.22 | 1.07 | 64 |
| stroke 438 | 84 % → 93 % | 679.8 px | 0.26 | 1.10 | 24 |
| stroke 439 | 93 % → 95 % | 603.0 px | 0.18 | 1.02 | 49 |
| stroke 440 | 94 % → 96 % | 1335.3 px | 0.18 | 1.03 | 25 |
| stroke 441 | 89 % → 93 % | 503.3 px | 0.26 | 1.04 | 43 |
| stroke 442 | 90 % → 93 % | 629.3 px | 0.23 | 1.03 | 38 |
| stroke 443 | 93 % → 96 % | 1443.9 px | 0.16 | 1.03 | 14 |
| stroke 444 | 95 % → 97 % | 879.6 px | 0.17 | 1.01 | 42 |
| stroke 445 | 92 % → 94 % | 961.0 px | 0.23 | 1.01 | 56 |
| stroke 446 | 91 % → 92 % | 855.5 px | 0.24 | 1.01 | 47 |
| stroke 447 | 91 % → 92 % | 875.0 px | 0.28 | 1.01 | 12 |
| stroke 448 | 92 % → 93 % | 877.5 px | 0.26 | 1.01 | 30 |
| stroke 449 | 80 % → 80 % | 795.6 px | 0.22 | 1.00 | 24 |
| stroke 450 | 80 % → 79 % | 1015.7 px | 0.22 | 0.99 | 21 |
| stroke 451 | 79 % → 78 % | 1071.1 px | 0.21 | 0.99 | 14 |
| stroke 452 | 67 % → 91 % | 379.3 px | 0.13 | 1.35 | 51 |
| stroke 453 | 69 % → 87 % | 505.1 px | 0.11 | 1.26 | 32 |
| stroke 454 | 76 % → 87 % | 473.1 px | 0.08 | 1.15 | 42 |
| stroke 455 | 75 % → 89 % | 498.2 px | 0.18 | 1.18 | 37 |
| stroke 456 | 83 % → 94 % | 706.7 px | 0.12 | 1.13 | 32 |
| stroke 457 | 70 % → 80 % | 1218.7 px | 0.06 | 1.14 | 8 |
| stroke 458 | 77 % → 84 % | 671.2 px | 0.01 | 1.09 | 29 |
| stroke 459 | 83 % → 90 % | 1110.3 px | 0.01 | 1.09 | 14 |
| stroke 460 | 96 % → 99 % | 1070.4 px | 0.17 | 1.03 | 19 |
| stroke 461 | 90 % → 97 % | 954.4 px | 0.16 | 1.08 | 21 |
| stroke 462 | 81 % → 89 % | 556.2 px | 0.11 | 1.10 | 71 |
| stroke 463 | 78 % → 85 % | 631.5 px | 0.13 | 1.09 | 39 |
| stroke 464 | 96 % → 98 % | 1632.5 px | 0.05 | 1.02 | 19 |
| stroke 465 | 78 % → 84 % | 1337.2 px | 0.12 | 1.08 | 14 |
| stroke 466 | 82 % → 89 % | 727.5 px | 0.17 | 1.08 | 53 |
| stroke 467 | 79 % → 84 % | 795.8 px | 0.15 | 1.07 | 34 |
| stroke 468 | 77 % → 80 % | 1314.1 px | 0.10 | 1.04 | 19 |
| stroke 469 | 85 % → 89 % | 817.4 px | 0.13 | 1.05 | 37 |
| stroke 470 | 84 % → 86 % | 725.5 px | 0.07 | 1.03 | 41 |
| stroke 471 | 98 % → 99 % | 1077.8 px | 0.22 | 1.01 | 58 |
| stroke 472 | 79 % → 83 % | 1218.2 px | 0.15 | 1.05 | 20 |
| stroke 473 | 99 % → 99 % | 1519.7 px | 0.20 | 1.00 | 51 |
| stroke 474 | 92 % → 97 % | 1531.2 px | 0.19 | 1.04 | 24 |
| stroke 475 | 83 % → 88 % | 1425.7 px | 0.16 | 1.06 | 24 |
| stroke 476 | 88 % → 90 % | 1082.3 px | 0.04 | 1.02 | 34 |
| stroke 477 | 79 % → 83 % | 1346.4 px | 0.16 | 1.05 | 14 |
| stroke 478 | 85 % → 92 % | 1579.9 px | 0.20 | 1.09 | 11 |
| stroke 479 | 78 % → 81 % | 1220.8 px | 0.11 | 1.03 | 15 |
| stroke 480 | 79 % → 86 % | 1453.4 px | 0.22 | 1.09 | 12 |
| stroke 481 | 80 % → 86 % | 1530.3 px | 0.15 | 1.07 | 7 |
| stroke 482 | 79 % → 81 % | 1451.0 px | 0.01 | 1.02 | 15 |
| stroke 483 | 79 % → 84 % | 1148.9 px | 0.13 | 1.06 | 13 |
| stroke 484 | 88 % → 91 % | 822.6 px | 0.35 | 1.04 | 27 |
| stroke 485 | 86 % → 89 % | 1460.0 px | 0.35 | 1.04 | 15 |
| stroke 486 | 89 % → 91 % | 771.0 px | 0.33 | 1.03 | 39 |
| stroke 487 | 84 % → 87 % | 1455.6 px | 0.22 | 1.03 | 14 |
| stroke 488 | 81 % → 88 % | 540.4 px | 0.20 | 1.08 | 84 |
| stroke 489 | 86 % → 88 % | 717.7 px | 0.23 | 1.02 | 38 |
| stroke 490 | 64 % → 74 % | 433.3 px | 0.30 | 1.16 | 44 |
| stroke 491 | 86 % → 92 % | 481.7 px | 0.39 | 1.07 | 75 |
| stroke 492 | 68 % → 74 % | 768.4 px | 0.40 | 1.08 | 42 |
| stroke 493 | 73 % → 81 % | 422.1 px | 0.32 | 1.12 | 77 |
| stroke 494 | 69 % → 81 % | 654.7 px | 0.34 | 1.16 | 39 |
| stroke 495 | 71 % → 79 % | 453.1 px | 0.35 | 1.11 | 66 |
| stroke 496 | 76 % → 85 % | 528.0 px | 0.34 | 1.12 | 63 |
| stroke 497 | 82 % → 89 % | 723.6 px | 0.36 | 1.08 | 41 |
| stroke 498 | 55 % → 60 % | 498.5 px | 0.34 | 1.09 | 28 |
| stroke 499 | 55 % → 60 % | 604.9 px | 0.32 | 1.10 | 19 |
| stroke 500 | 63 % → 68 % | 448.4 px | 0.26 | 1.07 | 40 |
| stroke 501 | 53 % → 58 % | 407.1 px | 0.30 | 1.09 | 38 |
| stroke 502 | 79 % → 82 % | 640.7 px | 0.33 | 1.05 | 40 |
| stroke 503 | 80 % → 82 % | 1079.3 px | 0.26 | 1.02 | 18 |
| stroke 504 | 73 % → 75 % | 728.8 px | 0.32 | 1.03 | 30 |
| stroke 505 | 58 % → 61 % | 421.7 px | 0.32 | 1.06 | 45 |
| stroke 506 | 66 % → 68 % | 475.9 px | 0.29 | 1.03 | 54 |
| stroke 507 | 85 % → 87 % | 1081.6 px | 0.38 | 1.02 | 22 |
| stroke 508 | 94 % → 95 % | 730.8 px | 0.41 | 1.01 | 33 |
| stroke 509 | 91 % → 93 % | 780.2 px | 0.39 | 1.02 | 37 |
| stroke 510 | 87 % → 90 % | 764.1 px | 0.34 | 1.03 | 39 |
| stroke 511 | 76 % → 79 % | 1136.3 px | 0.34 | 1.04 | 30 |
| stroke 512 | 64 % → 65 % | 1034.0 px | 0.32 | 1.03 | 32 |
| stroke 513 | 55 % → 56 % | 452.6 px | 0.31 | 1.03 | 51 |
| stroke 514 | 60 % → 62 % | 703.3 px | 0.31 | 1.03 | 25 |
| stroke 515 | 67 % → 69 % | 958.3 px | 0.37 | 1.02 | 25 |
| stroke 516 | 84 % → 86 % | 1138.7 px | 0.34 | 1.02 | 37 |
| stroke 517 | 58 % → 59 % | 801.0 px | 0.32 | 1.03 | 21 |
| stroke 518 | 75 % → 77 % | 1126.9 px | 0.33 | 1.02 | 33 |
| stroke 519 | 83 % → 84 % | 1364.3 px | 0.34 | 1.02 | 17 |
| stroke 520 | 99 % → 100 % | 546.9 px | 0.40 | 1.01 | 112 |
| stroke 521 | 99 % → 100 % | 1448.1 px | 0.41 | 1.01 | 26 |
| stroke 522 | 99 % → 100 % | 726.7 px | 0.41 | 1.01 | 56 |
| stroke 523 | 99 % → 100 % | 806.9 px | 0.43 | 1.01 | 53 |
| stroke 524 | 99 % → 100 % | 1668.0 px | 0.45 | 1.00 | 15 |
| stroke 525 | 100 % → 100 % | 1125.6 px | 0.43 | 1.00 | 37 |
| stroke 526 | 100 % → 100 % | 871.0 px | 0.45 | 1.00 | 52 |
| stroke 527 | 100 % → 100 % | 1851.0 px | 0.46 | 1.00 | 12 |
| stroke 528 | 100 % → 100 % | 1293.3 px | 0.43 | 1.00 | 21 |
| stroke 529 | 97 % → 100 % | 1346.4 px | 0.38 | 1.03 | 15 |
| stroke 530 | 100 % → 100 % | 864.8 px | 0.40 | 1.00 | 39 |
| stroke 531 | 100 % → 100 % | 733.7 px | 0.42 | 1.00 | 44 |
| stroke 532 | 98 % → 100 % | 1360.3 px | 0.39 | 1.02 | 20 |
| stroke 533 | 95 % → 97 % | 476.2 px | 0.43 | 1.02 | 62 |
| stroke 534 | 96 % → 95 % | 670.3 px | 0.48 | 1.00 | 30 |
| stroke 535 | 99 % → 100 % | 559.9 px | 0.45 | 1.01 | 55 |
| stroke 536 | 98 % → 98 % | 637.5 px | 0.42 | 1.01 | 39 |
| stroke 537 | 99 % → 100 % | 858.1 px | 0.43 | 1.00 | 28 |
| stroke 538 | 98 % → 98 % | 1597.9 px | 0.42 | 1.00 | 12 |
| stroke 539 | 99 % → 100 % | 1349.9 px | 0.44 | 1.00 | 18 |
| stroke 540 | 96 % → 96 % | 1691.5 px | 0.43 | 1.00 | 11 |
| stroke 541 | 99 % → 100 % | 1814.5 px | 0.42 | 1.00 | 11 |
| stroke 542 | 74 % → 74 % | 968.9 px | 0.03 | 1.00 | 5 |
| stroke 543 | 98 % → 98 % | 676.5 px | 0.40 | 1.00 | 50 |
| stroke 544 | 90 % → 91 % | 1890.9 px | 0.36 | 1.01 | 5 |
| stroke 545 | 93 % → 93 % | 865.5 px | 0.43 | 1.01 | 24 |
| stroke 546 | 100 % → 100 % | 2455.4 px | 0.41 | 1.00 | 4 |
| stroke 547 | 99 % → 99 % | 705.6 px | 0.39 | 1.00 | 72 |
| stroke 548 | 99 % → 99 % | 1289.1 px | 0.40 | 1.00 | 33 |

Numbers say: wet paint spreads well beyond the stroke.

## Refs v3 · #25 Yellow heavy stroke — own sheet
own sheet 800 × 1198 · Impasto 1.00 · 272 px · 57.6 s

![Refs v3 · #25 Yellow heavy stroke — own sheet](Refs-v3-25-Yellow-heavy-stroke-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 21 % → 21 % | 226.0 px | 0.15 | 0.97 | 9770 |
| stroke 2 | 28 % → 26 % | 66.5 px | 0.15 | 0.95 | 16290 |
| stroke 3 | 29 % → 18 % | 11.3 px | 0.15 | 0.63 | 17350 |

## Refs v3 · #26 Ink caricature — own sheet
own sheet 800 × 1065 · Ink 0.98 · 64 px · 35.4 s

![Refs v3 · #26 Ink caricature — own sheet](Refs-v3-26-Ink-caricature-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 8 % → 22 % | 21.7 px | 0.74 | 2.78 | 62 |
| stroke 2 | 3 % → 44 % | 64.7 px | 0.77 | 13.79 | 24 |
| stroke 3 | 9 % → 32 % | 52.5 px | 0.77 | 3.60 | 246 |
| stroke 4 | 5 % → 51 % | 159.1 px | 0.77 | 11.12 | 11 |
| stroke 5 | 6 % → 35 % | 32.0 px | 0.76 | 5.39 | 187 |
| stroke 6 | 10 % → 38 % | 322.8 px | 0.77 | 3.76 | 5 |
| stroke 7 | 8 % → 42 % | 79.0 px | 0.77 | 5.06 | 37 |
| stroke 8 | 16 % → 36 % | 117.5 px | 0.77 | 2.18 | 203 |
| stroke 9 | 15 % → 30 % | 101.9 px | 0.78 | 2.05 | 138 |
| stroke 10 | 1 % → 26 % | 29.7 px | 0.75 | 20.42 | 12 |
| stroke 11 | 19 % → 45 % | 134.8 px | 0.77 | 2.39 | 91 |
| stroke 12 | 16 % → 50 % | 286.2 px | 0.77 | 3.08 | 16 |
| stroke 13 | 19 % → 43 % | 129.5 px | 0.77 | 2.21 | 165 |
| stroke 14 | 27 % → 49 % | 359.8 px | 0.77 | 1.78 | 36 |
| stroke 15 | 34 % → 45 % | 540.5 px | 0.77 | 1.35 | 54 |
| stroke 16 | 25 % → 43 % | 495.0 px | 0.77 | 1.75 | 54 |
| stroke 17 | 35 % → 46 % | 297.8 px | 0.77 | 1.31 | 165 |
| stroke 18 | 44 % → 47 % | 791.8 px | 0.77 | 1.08 | 31 |
| stroke 19 | 22 % → 29 % | 127.5 px | 0.76 | 1.34 | 468 |
| stroke 20 | 37 % → 40 % | 644.6 px | 0.77 | 1.08 | 40 |
| stroke 21 | 22 % → 37 % | 576.2 px | 0.76 | 1.72 | 13 |
| stroke 22 | 36 % → 41 % | 314.1 px | 0.76 | 1.11 | 239 |
| stroke 23 | 20 % → 24 % | 235.7 px | 0.74 | 1.22 | 15 |
| stroke 24 | 34 % → 36 % | 156.9 px | 0.77 | 1.06 | 301 |
| stroke 25 | 38 % → 40 % | 406.1 px | 0.76 | 1.05 | 24 |
| stroke 26 | 54 % → 56 % | 964.1 px | 0.77 | 1.03 | 19 |
| stroke 27 | 9 % → 25 % | 73.9 px | 0.75 | 2.82 | 52 |
| stroke 28 | 8 % → 21 % | 72.4 px | 0.75 | 2.64 | 36 |
| stroke 29 | 18 % → 31 % | 160.5 px | 0.75 | 1.75 | 31 |
| stroke 30 | 24 % → 30 % | 763.7 px | 0.75 | 1.24 | 11 |
| stroke 31 | 13 % → 25 % | 111.6 px | 0.75 | 1.91 | 56 |
| stroke 32 | 12 % → 19 % | 93.1 px | 0.75 | 1.55 | 86 |
| stroke 33 | 18 % → 28 % | 330.6 px | 0.75 | 1.56 | 19 |
| stroke 34 | 7 % → 15 % | 59.5 px | 0.74 | 2.08 | 70 |
| stroke 35 | 18 % → 30 % | 235.6 px | 0.74 | 1.69 | 25 |
| stroke 36 | 14 % → 24 % | 119.7 px | 0.75 | 1.65 | 56 |
| stroke 37 | 13 % → 23 % | 138.4 px | 0.74 | 1.75 | 32 |
| stroke 38 | 13 % → 23 % | 122.8 px | 0.74 | 1.73 | 29 |
| stroke 39 | 15 % → 21 % | 133.6 px | 0.74 | 1.39 | 41 |
| stroke 40 | 19 % → 22 % | 197.6 px | 0.73 | 1.19 | 27 |
| stroke 41 | 13 % → 15 % | 74.6 px | 0.75 | 1.14 | 65 |
| stroke 42 | 4 % → 6 % | 11.6 px | 0.76 | 1.46 | 31 |

Numbers say: wet paint spreads well beyond the stroke.

## Refs v3 · #27 Orange impasto swatch — own sheet
own sheet 800 × 1000 · Impasto 1.00 · 80 px · 18.4 s

![Refs v3 · #27 Orange impasto swatch — own sheet](Refs-v3-27-Orange-impasto-swatch-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 6 % → 1 % | 76.6 px | 0.21 | 0.18 | 132 |
| stroke 2 | 10 % → 1 % | 93.6 px | 0.21 | 0.08 | 317 |
| stroke 3 | 14 % → 1 % | 122.6 px | 0.21 | 0.05 | 367 |
| stroke 4 | 17 % → 1 % | 154.6 px | 0.21 | 0.04 | 394 |
| stroke 5 | 19 % → 0 % | 490.7 px | 0.00 | 0.00 | 55 |
| stroke 6 | 19 % → 1 % | 151.0 px | 0.21 | 0.03 | 656 |
| stroke 7 | 23 % → 1 % | 179.8 px | 0.21 | 0.02 | 606 |
| stroke 8 | 33 % → 1 % | 276.3 px | 0.21 | 0.02 | 450 |
| stroke 9 | 36 % → 0 % | 325.8 px | 0.21 | 0.01 | 441 |
| stroke 10 | 38 % → 0 % | 451.8 px | 0.20 | 0.01 | 267 |
| stroke 11 | 35 % → 0 % | 426.0 px | 0.00 | 0.00 | 326 |
| stroke 12 | 33 % → 0 % | 476.1 px | 0.00 | 0.00 | 263 |
| stroke 13 | 31 % → 0 % | 312.6 px | 0.00 | 0.00 | 342 |
| stroke 14 | 29 % → 0 % | 270.8 px | 0.00 | 0.00 | 390 |
| stroke 15 | 29 % → 0 % | 268.4 px | 0.00 | 0.00 | 396 |
| stroke 16 | 31 % → 0 % | 374.0 px | 0.00 | 0.00 | 261 |
| stroke 17 | 32 % → 0 % | 515.5 px | 0.00 | 0.00 | 158 |
| stroke 18 | 3 % → 0 % | 70.7 px | 0.00 | 0.00 | 42 |
| stroke 19 | 4 % → 0 % | 59.8 px | 0.00 | 0.00 | 96 |
| stroke 20 | 6 % → 0 % | 91.0 px | 0.22 | 0.06 | 145 |
| stroke 21 | 8 % → 1 % | 128.2 px | 0.23 | 0.08 | 166 |
| stroke 22 | 11 % → 1 % | 171.1 px | 0.23 | 0.07 | 210 |
| stroke 23 | 14 % → 1 % | 331.5 px | 0.23 | 0.06 | 68 |
| stroke 24 | 1 % → 1 % | 22.5 px | 0.21 | 0.93 | 41 |
| stroke 25 | 1 % → 1 % | 25.1 px | 0.23 | 0.94 | 22 |

## Refs v3 · #28 Miles Davis lines — own sheet
own sheet 800 × 753 · Ink 0.98 · 18 px · 58.1 s

![Refs v3 · #28 Miles Davis lines — own sheet](Refs-v3-28-Miles-Davis-lines-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 6 % → 0 % | 8.1 px | 0.00 | 0.00 | 5 |
| stroke 2 | 3 % → 0 % | 8.8 px | 0.00 | 0.00 | 1 |
| stroke 3 | 9 % → 0 % | 20.2 px | 0.00 | 0.00 | 2 |
| stroke 4 | 15 % → 0 % | 19.3 px | 0.00 | 0.00 | 10 |
| stroke 5 | 8 % → 0 % | 11.9 px | 0.00 | 0.00 | 5 |
| stroke 6 | 8 % → 0 % | 9.8 px | 0.00 | 0.00 | 15 |
| stroke 7 | 7 % → 0 % | 14.3 px | 0.00 | 0.00 | 7 |
| stroke 8 | 5 % → 31 % | 11.2 px | 0.83 | 5.73 | 8 |
| stroke 9 | 3 % → 63 % | 7.0 px | 0.88 | 21.50 | 7 |
| stroke 10 | 4 % → 83 % | 8.6 px | 0.89 | 23.28 | 4 |
| stroke 11 | 2 % → 77 % | 6.5 px | 0.89 | 42.20 | 2 |
| stroke 12 | 4 % → 27 % | 10.9 px | 0.87 | 6.92 | 3 |
| stroke 13 | 5 % → 87 % | 9.0 px | 0.89 | 18.73 | 5 |
| stroke 14 | 12 % → 87 % | 20.4 px | 0.88 | 7.19 | 11 |
| stroke 15 | 6 % → 63 % | 15.5 px | 0.88 | 10.48 | 12 |
| stroke 16 | 4 % → 75 % | 12.9 px | 0.88 | 18.24 | 4 |
| stroke 17 | 23 % → 34 % | 31.6 px | 0.89 | 1.45 | 58 |
| stroke 18 | 9 % → 25 % | 19.0 px | 0.88 | 2.81 | 25 |
| stroke 19 | 9 % → 39 % | 16.0 px | 0.88 | 4.45 | 43 |
| stroke 20 | 8 % → 51 % | 15.4 px | 0.88 | 6.26 | 15 |
| stroke 21 | 22 % → 81 % | 31.1 px | 0.90 | 3.76 | 69 |
| stroke 22 | 15 % → 49 % | 47.0 px | 0.90 | 3.26 | 25 |
| stroke 23 | 8 % → 69 % | 15.0 px | 0.87 | 8.88 | 23 |
| stroke 24 | 16 % → 63 % | 27.7 px | 0.87 | 3.99 | 25 |
| stroke 25 | 23 % → 44 % | 26.9 px | 0.87 | 1.92 | 88 |
| stroke 26 | 10 % → 15 % | 21.8 px | 0.89 | 1.50 | 154 |
| stroke 27 | 20 % → 41 % | 28.9 px | 0.89 | 2.09 | 290 |
| stroke 28 | 11 % → 71 % | 46.7 px | 0.89 | 6.73 | 5 |
| stroke 29 | 29 % → 53 % | 47.8 px | 0.90 | 1.80 | 78 |
| stroke 30 | 15 % → 58 % | 19.7 px | 0.88 | 3.92 | 38 |
| stroke 31 | 26 % → 79 % | 33.4 px | 0.88 | 3.05 | 39 |
| stroke 32 | 60 % → 84 % | 74.7 px | 0.89 | 1.40 | 77 |
| stroke 33 | 25 % → 37 % | 30.5 px | 0.88 | 1.48 | 176 |
| stroke 34 | 22 % → 31 % | 41.7 px | 0.89 | 1.42 | 341 |
| stroke 35 | 14 % → 17 % | 30.7 px | 0.90 | 1.21 | 123 |
| stroke 36 | 17 % → 50 % | 70.5 px | 0.87 | 2.99 | 2 |
| stroke 37 | 21 % → 88 % | 56.9 px | 0.90 | 4.24 | 19 |
| stroke 38 | 26 % → 63 % | 55.4 px | 0.89 | 2.42 | 36 |
| stroke 39 | 9 % → 73 % | 29.7 px | 0.90 | 8.42 | 9 |
| stroke 40 | 5 % → 76 % | 21.6 px | 0.90 | 16.37 | 9 |
| stroke 41 | 11 % → 62 % | 21.1 px | 0.87 | 5.58 | 23 |
| stroke 42 | 27 % → 58 % | 49.9 px | 0.89 | 2.11 | 30 |
| stroke 43 | 8 % → 63 % | 25.9 px | 0.87 | 7.65 | 15 |
| stroke 44 | 8 % → 68 % | 31.1 px | 0.89 | 8.60 | 12 |
| stroke 45 | 12 % → 68 % | 28.8 px | 0.90 | 5.46 | 32 |
| stroke 46 | 21 % → 67 % | 48.5 px | 0.89 | 3.15 | 21 |
| stroke 47 | 11 % → 75 % | 29.5 px | 0.89 | 6.73 | 13 |
| stroke 48 | 28 % → 69 % | 71.4 px | 0.88 | 2.45 | 17 |
| stroke 49 | 25 % → 69 % | 86.2 px | 0.89 | 2.79 | 12 |
| stroke 50 | 31 % → 68 % | 77.2 px | 0.89 | 2.22 | 8 |
| stroke 51 | 27 % → 73 % | 45.8 px | 0.89 | 2.69 | 73 |
| stroke 52 | 22 % → 59 % | 39.3 px | 0.88 | 2.66 | 95 |
| stroke 53 | 23 % → 68 % | 72.1 px | 0.90 | 3.00 | 19 |
| stroke 54 | 24 % → 63 % | 36.7 px | 0.88 | 2.66 | 53 |
| stroke 55 | 39 % → 79 % | 86.1 px | 0.89 | 2.01 | 22 |
| stroke 56 | 47 % → 85 % | 159.1 px | 0.90 | 1.83 | 5 |
| stroke 57 | 23 % → 59 % | 46.9 px | 0.89 | 2.60 | 20 |
| stroke 58 | 49 % → 80 % | 144.5 px | 0.90 | 1.63 | 6 |
| stroke 59 | 53 % → 71 % | 156.1 px | 0.89 | 1.33 | 26 |
| stroke 60 | 20 % → 63 % | 55.1 px | 0.89 | 3.12 | 7 |
| stroke 61 | 28 % → 71 % | 72.8 px | 0.89 | 2.52 | 26 |
| stroke 62 | 29 % → 67 % | 85.0 px | 0.89 | 2.30 | 45 |
| stroke 63 | 22 % → 60 % | 99.6 px | 0.89 | 2.72 | 4 |
| stroke 64 | 21 % → 61 % | 44.1 px | 0.87 | 2.94 | 26 |
| stroke 65 | 21 % → 53 % | 47.6 px | 0.89 | 2.50 | 44 |
| stroke 66 | 38 % → 54 % | 112.8 px | 0.88 | 1.42 | 41 |
| stroke 67 | 38 % → 79 % | 151.0 px | 0.88 | 2.05 | 9 |
| stroke 68 | 10 % → 44 % | 33.4 px | 0.87 | 4.24 | 4 |
| stroke 69 | 15 % → 53 % | 41.0 px | 0.87 | 3.63 | 4 |
| stroke 70 | 39 % → 71 % | 94.8 px | 0.88 | 1.85 | 27 |
| stroke 71 | 65 % → 84 % | 258.3 px | 0.89 | 1.31 | 7 |
| stroke 72 | 57 % → 71 % | 149.6 px | 0.88 | 1.24 | 17 |
| stroke 73 | 47 % → 84 % | 76.7 px | 0.89 | 1.78 | 22 |
| stroke 74 | 36 % → 69 % | 82.8 px | 0.89 | 1.93 | 12 |
| stroke 75 | 58 % → 70 % | 151.0 px | 0.88 | 1.21 | 13 |
| stroke 76 | 63 % → 71 % | 129.9 px | 0.89 | 1.13 | 34 |
| stroke 77 | 31 % → 64 % | 114.3 px | 0.88 | 2.04 | 15 |
| stroke 78 | 21 % → 44 % | 31.7 px | 0.88 | 2.06 | 134 |
| stroke 79 | 45 % → 59 % | 73.7 px | 0.88 | 1.33 | 21 |
| stroke 80 | 57 % → 71 % | 90.5 px | 0.88 | 1.24 | 45 |
| stroke 81 | 44 % → 72 % | 119.3 px | 0.88 | 1.63 | 18 |
| stroke 82 | 52 % → 68 % | 110.1 px | 0.89 | 1.30 | 16 |
| stroke 83 | 21 % → 50 % | 91.7 px | 0.89 | 2.35 | 8 |
| stroke 84 | 37 % → 49 % | 63.7 px | 0.88 | 1.30 | 57 |
| stroke 85 | 55 % → 69 % | 120.0 px | 0.89 | 1.25 | 30 |
| stroke 86 | 54 % → 81 % | 161.0 px | 0.88 | 1.48 | 7 |
| stroke 87 | 67 % → 74 % | 213.7 px | 0.89 | 1.10 | 14 |
| stroke 88 | 58 % → 69 % | 136.5 px | 0.87 | 1.20 | 26 |
| stroke 89 | 22 % → 37 % | 61.5 px | 0.90 | 1.64 | 5 |
| stroke 90 | 20 % → 42 % | 53.4 px | 0.89 | 2.05 | 19 |
| stroke 91 | 7 % → 51 % | 26.0 px | 0.89 | 7.53 | 8 |
| stroke 92 | 43 % → 62 % | 88.4 px | 0.90 | 1.42 | 75 |
| stroke 93 | 49 % → 63 % | 125.6 px | 0.88 | 1.30 | 11 |
| stroke 94 | 55 % → 62 % | 143.8 px | 0.89 | 1.13 | 12 |
| stroke 95 | 27 % → 52 % | 50.1 px | 0.88 | 1.93 | 11 |
| stroke 96 | 25 % → 57 % | 59.2 px | 0.88 | 2.32 | 16 |
| stroke 97 | 40 % → 64 % | 103.7 px | 0.88 | 1.60 | 10 |
| stroke 98 | 73 % → 86 % | 191.2 px | 0.90 | 1.19 | 46 |
| stroke 99 | 34 % → 54 % | 64.2 px | 0.88 | 1.58 | 41 |
| stroke 100 | 59 % → 73 % | 229.4 px | 0.88 | 1.23 | 11 |
| stroke 101 | 65 % → 76 % | 296.9 px | 0.90 | 1.18 | 12 |
| stroke 102 | 20 % → 49 % | 33.1 px | 0.89 | 2.40 | 32 |
| stroke 103 | 29 % → 35 % | 73.3 px | 0.90 | 1.22 | 15 |
| stroke 104 | 26 % → 38 % | 42.9 px | 0.89 | 1.46 | 44 |
| stroke 105 | 69 % → 79 % | 219.8 px | 0.89 | 1.14 | 12 |
| stroke 106 | 73 % → 75 % | 206.0 px | 0.90 | 1.02 | 5 |
| stroke 107 | 36 % → 48 % | 114.1 px | 0.89 | 1.32 | 10 |
| stroke 108 | 45 % → 61 % | 95.3 px | 0.89 | 1.36 | 31 |
| stroke 109 | 65 % → 73 % | 153.6 px | 0.90 | 1.12 | 15 |
| stroke 110 | 46 % → 54 % | 200.7 px | 0.89 | 1.18 | 10 |
| stroke 111 | 27 % → 49 % | 56.8 px | 0.90 | 1.81 | 11 |
| stroke 112 | 50 % → 55 % | 80.4 px | 0.89 | 1.11 | 41 |
| stroke 113 | 57 % → 62 % | 173.1 px | 0.89 | 1.09 | 7 |
| stroke 114 | 50 % → 59 % | 63.7 px | 0.89 | 1.17 | 60 |
| stroke 115 | 62 % → 72 % | 165.7 px | 0.89 | 1.15 | 13 |
| stroke 116 | 67 % → 68 % | 214.8 px | 0.87 | 1.02 | 11 |
| stroke 117 | 73 % → 77 % | 211.3 px | 0.89 | 1.06 | 6 |
| stroke 118 | 29 % → 56 % | 73.0 px | 0.88 | 1.96 | 5 |
| stroke 119 | 78 % → 80 % | 244.6 px | 0.89 | 1.04 | 8 |
| stroke 120 | 49 % → 50 % | 87.9 px | 0.89 | 1.02 | 40 |
| stroke 121 | 75 % → 76 % | 350.8 px | 0.90 | 1.01 | 6 |
| stroke 122 | 44 % → 50 % | 116.8 px | 0.88 | 1.13 | 19 |
| stroke 123 | 38 % → 42 % | 133.6 px | 0.88 | 1.10 | 12 |
| stroke 124 | 88 % → 88 % | 229.6 px | 0.90 | 1.01 | 14 |
| stroke 125 | 58 % → 61 % | 232.8 px | 0.87 | 1.04 | 4 |
| stroke 126 | 78 % → 79 % | 288.5 px | 0.89 | 1.02 | 7 |
| stroke 127 | 42 % → 44 % | 164.2 px | 0.89 | 1.05 | 9 |
| stroke 128 | 65 % → 69 % | 277.1 px | 0.88 | 1.06 | 6 |
| stroke 129 | 37 % → 57 % | 48.2 px | 0.88 | 1.54 | 46 |
| stroke 130 | 38 % → 60 % | 48.2 px | 0.87 | 1.59 | 38 |
| stroke 131 | 42 % → 57 % | 56.6 px | 0.88 | 1.37 | 32 |
| stroke 132 | 59 % → 65 % | 150.3 px | 0.88 | 1.10 | 18 |

Numbers say: wet paint spreads well beyond the stroke.

## Refs v3 · #29 Shrigley asterisk — own sheet
own sheet 800 × 1028 · Watercolour 1.00 + water 50 % · 64 px · 39.5 s

![Refs v3 · #29 Shrigley asterisk — own sheet](Refs-v3-29-Shrigley-asterisk-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 15 % → 46 % | 70.8 px | 0.49 | 3.09 | 403 |
| stroke 2 | 24 % → 54 % | 104.9 px | 0.47 | 2.26 | 494 |
| stroke 3 | 8 % → 27 % | 78.2 px | 0.49 | 3.46 | 53 |
| stroke 4 | 22 % → 37 % | 111.8 px | 0.47 | 1.66 | 1420 |
| stroke 5 | 30 % → 47 % | 149.3 px | 0.47 | 1.55 | 594 |
| stroke 6 | 30 % → 38 % | 138.8 px | 0.46 | 1.25 | 1117 |
| stroke 7 | 33 % → 37 % | 184.0 px | 0.49 | 1.11 | 1087 |
| stroke 8 | 31 % → 32 % | 176.2 px | 0.48 | 1.05 | 1386 |
| stroke 9 | 62 % → 68 % | 815.1 px | 0.47 | 1.10 | 163 |
| stroke 10 | 72 % → 82 % | 1330.0 px | 0.46 | 1.14 | 102 |
| stroke 11 | 58 % → 69 % | 797.7 px | 0.47 | 1.19 | 208 |
| stroke 12 | 66 % → 71 % | 970.0 px | 0.47 | 1.08 | 239 |
| stroke 13 | 41 % → 40 % | 273.1 px | 0.47 | 0.98 | 664 |

Numbers say: wet paint spreads well beyond the stroke.

## Refs v3 · #30 Red gouache face — own sheet
own sheet 800 × 1084 · Gouache 1.00 + water 15 % · 76 px · 233.6 s

![Refs v3 · #30 Red gouache face — own sheet](Refs-v3-30-Red-gouache-face-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 10 % → 79 % | 71.0 px | 0.50 | 8.05 | 364 |
| stroke 2 | 16 % → 94 % | 107.9 px | 0.50 | 6.04 | 526 |
| stroke 3 | 20 % → 99 % | 148.1 px | 0.51 | 4.94 | 866 |
| stroke 4 | 13 % → 68 % | 127.5 px | 0.51 | 5.08 | 468 |
| stroke 5 | 24 % → 80 % | 176.0 px | 0.52 | 3.27 | 640 |
| stroke 6 | 21 % → 62 % | 159.9 px | 0.49 | 2.98 | 548 |
| stroke 7 | 38 % → 96 % | 333.6 px | 0.50 | 2.50 | 464 |
| stroke 8 | 18 % → 73 % | 144.3 px | 0.50 | 3.97 | 761 |
| stroke 9 | 43 % → 82 % | 279.3 px | 0.50 | 1.93 | 833 |
| stroke 10 | 23 % → 80 % | 211.2 px | 0.51 | 3.57 | 447 |
| stroke 11 | 51 % → 80 % | 479.5 px | 0.49 | 1.55 | 442 |
| stroke 12 | 48 % → 97 % | 382.1 px | 0.52 | 2.01 | 402 |
| stroke 13 | 50 % → 91 % | 572.0 px | 0.50 | 1.81 | 337 |
| stroke 14 | 43 % → 81 % | 379.8 px | 0.50 | 1.89 | 291 |
| stroke 15 | 50 % → 88 % | 520.5 px | 0.51 | 1.76 | 436 |
| stroke 16 | 46 % → 78 % | 336.5 px | 0.50 | 1.68 | 685 |
| stroke 17 | 62 % → 84 % | 1171.0 px | 0.49 | 1.35 | 216 |
| stroke 18 | 71 % → 98 % | 837.7 px | 0.49 | 1.38 | 246 |
| stroke 19 | 55 % → 95 % | 430.5 px | 0.50 | 1.73 | 516 |
| stroke 20 | 33 % → 83 % | 438.1 px | 0.53 | 2.54 | 230 |
| stroke 21 | 49 % → 80 % | 368.6 px | 0.51 | 1.62 | 452 |
| stroke 22 | 70 % → 97 % | 748.7 px | 0.50 | 1.39 | 345 |
| stroke 23 | 64 % → 88 % | 785.6 px | 0.51 | 1.38 | 215 |
| stroke 24 | 35 % → 76 % | 311.1 px | 0.51 | 2.15 | 382 |
| stroke 25 | 34 % → 77 % | 446.6 px | 0.53 | 2.27 | 192 |
| stroke 26 | 76 % → 99 % | 1378.8 px | 0.49 | 1.30 | 122 |
| stroke 27 | 40 % → 77 % | 408.3 px | 0.51 | 1.92 | 427 |
| stroke 28 | 46 % → 89 % | 819.0 px | 0.53 | 1.94 | 122 |
| stroke 29 | 48 % → 81 % | 463.7 px | 0.50 | 1.70 | 330 |
| stroke 30 | 51 % → 81 % | 770.1 px | 0.50 | 1.60 | 147 |
| stroke 31 | 34 % → 65 % | 368.2 px | 0.52 | 1.92 | 180 |
| stroke 32 | 78 % → 98 % | 1075.7 px | 0.51 | 1.26 | 163 |
| stroke 33 | 59 % → 94 % | 1047.7 px | 0.52 | 1.59 | 114 |
| stroke 34 | 53 % → 82 % | 870.5 px | 0.51 | 1.54 | 134 |
| stroke 35 | 56 % → 86 % | 1037.4 px | 0.51 | 1.54 | 128 |
| stroke 36 | 59 % → 85 % | 706.1 px | 0.51 | 1.44 | 201 |
| stroke 37 | 84 % → 97 % | 1538.1 px | 0.49 | 1.16 | 118 |
| stroke 38 | 66 % → 76 % | 889.8 px | 0.49 | 1.15 | 207 |
| stroke 39 | 66 % → 92 % | 689.0 px | 0.51 | 1.40 | 277 |
| stroke 40 | 70 % → 90 % | 822.3 px | 0.51 | 1.29 | 271 |
| stroke 41 | 50 % → 82 % | 586.2 px | 0.50 | 1.65 | 269 |
| stroke 42 | 67 % → 75 % | 1222.1 px | 0.49 | 1.12 | 94 |
| stroke 43 | 45 % → 72 % | 693.0 px | 0.50 | 1.62 | 153 |
| stroke 44 | 77 % → 99 % | 897.4 px | 0.50 | 1.28 | 179 |
| stroke 45 | 82 % → 99 % | 1293.1 px | 0.50 | 1.20 | 129 |
| stroke 46 | 38 % → 68 % | 613.0 px | 0.52 | 1.78 | 125 |
| stroke 47 | 84 % → 99 % | 1194.1 px | 0.51 | 1.18 | 158 |
| stroke 48 | 92 % → 99 % | 1665.8 px | 0.49 | 1.07 | 100 |
| stroke 49 | 85 % → 98 % | 1437.1 px | 0.51 | 1.16 | 105 |
| stroke 50 | 77 % → 94 % | 1344.4 px | 0.51 | 1.22 | 137 |
| stroke 51 | 85 % → 98 % | 1489.2 px | 0.50 | 1.16 | 133 |
| stroke 52 | 47 % → 64 % | 445.2 px | 0.49 | 1.35 | 273 |
| stroke 53 | 52 % → 61 % | 681.6 px | 0.48 | 1.18 | 122 |
| stroke 54 | 74 % → 93 % | 975.7 px | 0.50 | 1.26 | 41 |
| stroke 55 | 51 % → 73 % | 1204.6 px | 0.51 | 1.42 | 5 |
| stroke 56 | 84 % → 96 % | 3697.2 px | 0.51 | 1.15 | 4 |
| stroke 57 | 34 % → 69 % | 1120.8 px | 0.53 | 2.02 | 6 |
| stroke 58 | 34 % → 56 % | 865.2 px | 0.49 | 1.65 | 14 |
| stroke 59 | 31 % → 54 % | 393.9 px | 0.49 | 1.72 | 12 |
| stroke 60 | 36 % → 58 % | 524.8 px | 0.50 | 1.63 | 47 |
| stroke 61 | 38 % → 58 % | 1260.4 px | 0.49 | 1.51 | 16 |
| stroke 62 | 42 % → 61 % | 603.8 px | 0.50 | 1.45 | 50 |
| stroke 63 | 45 % → 70 % | 1810.0 px | 0.52 | 1.55 | 9 |
| stroke 64 | 45 % → 85 % | 852.1 px | 0.52 | 1.87 | 7 |
| stroke 65 | 56 % → 87 % | 1236.9 px | 0.51 | 1.54 | 10 |
| stroke 66 | 49 % → 72 % | 1163.8 px | 0.52 | 1.48 | 14 |
| stroke 67 | 58 % → 72 % | 1678.0 px | 0.49 | 1.23 | 9 |
| stroke 68 | 54 % → 78 % | 1196.1 px | 0.51 | 1.43 | 8 |
| stroke 69 | 35 % → 73 % | 999.5 px | 0.54 | 2.11 | 19 |
| stroke 70 | 32 % → 68 % | 834.7 px | 0.54 | 2.11 | 22 |
| stroke 71 | 27 % → 58 % | 449.2 px | 0.54 | 2.13 | 21 |
| stroke 72 | 34 % → 64 % | 1090.3 px | 0.54 | 1.87 | 4 |
| stroke 73 | 29 % → 62 % | 622.3 px | 0.55 | 2.12 | 14 |
| stroke 74 | 47 % → 65 % | 304.1 px | 0.52 | 1.40 | 227 |
| stroke 75 | 87 % → 99 % | 732.4 px | 0.51 | 1.14 | 243 |
| stroke 76 | 44 % → 51 % | 344.0 px | 0.50 | 1.15 | 131 |
| stroke 77 | 39 % → 67 % | 399.1 px | 0.54 | 1.72 | 198 |
| stroke 78 | 45 % → 60 % | 555.1 px | 0.51 | 1.34 | 73 |
| stroke 79 | 53 % → 76 % | 403.0 px | 0.52 | 1.43 | 237 |
| stroke 80 | 54 % → 69 % | 519.2 px | 0.51 | 1.29 | 280 |
| stroke 81 | 39 % → 55 % | 269.6 px | 0.54 | 1.41 | 171 |
| stroke 82 | 48 % → 68 % | 662.9 px | 0.55 | 1.41 | 58 |
| stroke 83 | 79 % → 85 % | 641.9 px | 0.50 | 1.08 | 271 |
| stroke 84 | 96 % → 99 % | 1207.4 px | 0.50 | 1.03 | 138 |
| stroke 85 | 46 % → 59 % | 533.1 px | 0.53 | 1.27 | 123 |
| stroke 86 | 52 % → 62 % | 420.1 px | 0.52 | 1.19 | 227 |
| stroke 87 | 50 % → 54 % | 484.9 px | 0.50 | 1.07 | 143 |
| stroke 88 | 80 % → 87 % | 916.3 px | 0.51 | 1.08 | 147 |
| stroke 89 | 60 % → 68 % | 760.8 px | 0.53 | 1.15 | 140 |
| stroke 90 | 66 % → 72 % | 631.7 px | 0.50 | 1.10 | 151 |
| stroke 91 | 94 % → 97 % | 1451.0 px | 0.50 | 1.04 | 114 |
| stroke 92 | 96 % → 99 % | 1117.8 px | 0.51 | 1.04 | 136 |
| stroke 93 | 48 % → 54 % | 1123.7 px | 0.53 | 1.13 | 46 |
| stroke 94 | 86 % → 90 % | 1230.5 px | 0.50 | 1.05 | 116 |
| stroke 95 | 83 % → 87 % | 1355.5 px | 0.50 | 1.05 | 103 |
| stroke 96 | 46 % → 58 % | 1050.6 px | 0.55 | 1.25 | 55 |
| stroke 97 | 87 % → 89 % | 1088.1 px | 0.50 | 1.03 | 118 |
| stroke 98 | 66 % → 69 % | 1080.5 px | 0.49 | 1.04 | 105 |
| stroke 99 | 75 % → 80 % | 1938.9 px | 0.51 | 1.06 | 53 |
| stroke 100 | 71 % → 72 % | 524.2 px | 0.50 | 1.00 | 167 |
| stroke 101 | 50 % → 66 % | 692.8 px | 0.55 | 1.32 | 50 |
| stroke 102 | 97 % → 99 % | 1052.1 px | 0.51 | 1.02 | 207 |
| stroke 103 | 58 % → 61 % | 1090.3 px | 0.52 | 1.05 | 71 |
| stroke 104 | 94 % → 95 % | 1558.2 px | 0.50 | 1.01 | 73 |
| stroke 105 | 57 % → 78 % | 426.7 px | 0.52 | 1.38 | 88 |
| stroke 106 | 63 % → 72 % | 778.4 px | 0.54 | 1.14 | 92 |
| stroke 107 | 52 % → 81 % | 709.1 px | 0.53 | 1.56 | 21 |
| stroke 108 | 44 % → 49 % | 846.1 px | 0.54 | 1.12 | 67 |
| stroke 109 | 66 % → 73 % | 1010.5 px | 0.54 | 1.10 | 104 |
| stroke 110 | 62 % → 66 % | 1001.6 px | 0.53 | 1.06 | 86 |
| stroke 111 | 75 % → 75 % | 850.6 px | 0.50 | 1.00 | 109 |
| stroke 112 | 53 % → 56 % | 585.6 px | 0.50 | 1.05 | 120 |
| stroke 113 | 74 % → 74 % | 1456.6 px | 0.51 | 0.99 | 65 |
| stroke 114 | 69 % → 76 % | 829.7 px | 0.51 | 1.09 | 70 |
| stroke 115 | 47 % → 49 % | 501.7 px | 0.55 | 1.05 | 80 |
| stroke 116 | 49 % → 51 % | 833.7 px | 0.53 | 1.03 | 53 |
| stroke 117 | 77 % → 78 % | 1890.8 px | 0.51 | 1.00 | 40 |
| stroke 118 | 44 % → 45 % | 1195.8 px | 0.54 | 1.02 | 37 |
| stroke 119 | 54 % → 54 % | 610.4 px | 0.55 | 1.01 | 66 |
| stroke 120 | 74 % → 74 % | 1053.7 px | 0.51 | 1.00 | 88 |
| stroke 121 | 99 % → 100 % | 2660.5 px | 0.49 | 1.01 | 41 |
| stroke 122 | 50 % → 50 % | 398.2 px | 0.50 | 1.00 | 117 |
| stroke 123 | 94 % → 95 % | 2100.8 px | 0.51 | 1.01 | 47 |
| stroke 124 | 70 % → 77 % | 1522.8 px | 0.51 | 1.10 | 50 |
| stroke 125 | 69 % → 82 % | 1115.8 px | 0.51 | 1.19 | 76 |
| stroke 126 | 95 % → 96 % | 1987.2 px | 0.51 | 1.01 | 63 |
| stroke 127 | 94 % → 95 % | 2325.2 px | 0.51 | 1.01 | 51 |
| stroke 128 | 98 % → 98 % | 2046.3 px | 0.50 | 1.00 | 64 |
| stroke 129 | 68 % → 69 % | 1010.8 px | 0.55 | 1.02 | 73 |
| stroke 130 | 76 % → 78 % | 2050.9 px | 0.54 | 1.02 | 43 |
| stroke 131 | 63 % → 64 % | 1346.9 px | 0.53 | 1.02 | 38 |
| stroke 132 | 71 % → 71 % | 1602.4 px | 0.52 | 1.00 | 38 |
| stroke 133 | 48 % → 67 % | 356.2 px | 0.50 | 1.38 | 124 |
| stroke 134 | 60 % → 74 % | 404.0 px | 0.51 | 1.23 | 132 |
| stroke 135 | 80 % → 89 % | 750.4 px | 0.51 | 1.12 | 116 |
| stroke 136 | 59 % → 63 % | 388.8 px | 0.50 | 1.07 | 114 |
| stroke 137 | 84 % → 88 % | 874.7 px | 0.51 | 1.05 | 86 |
| stroke 138 | 65 % → 70 % | 595.8 px | 0.50 | 1.08 | 126 |
| stroke 139 | 85 % → 88 % | 1310.2 px | 0.51 | 1.04 | 72 |
| stroke 140 | 85 % → 89 % | 1143.1 px | 0.51 | 1.05 | 68 |
| stroke 141 | 64 % → 66 % | 1508.8 px | 0.50 | 1.03 | 49 |
| stroke 142 | 58 % → 60 % | 829.5 px | 0.50 | 1.04 | 111 |
| stroke 143 | 60 % → 60 % | 723.7 px | 0.50 | 1.00 | 52 |
| stroke 144 | 84 % → 87 % | 1372.1 px | 0.51 | 1.03 | 63 |
| stroke 145 | 96 % → 98 % | 928.4 px | 0.50 | 1.02 | 198 |
| stroke 146 | 97 % → 99 % | 1106.2 px | 0.50 | 1.02 | 125 |
| stroke 147 | 97 % → 99 % | 1525.5 px | 0.51 | 1.02 | 100 |
| stroke 148 | 99 % → 99 % | 1711.9 px | 0.50 | 1.01 | 67 |
| stroke 149 | 97 % → 98 % | 997.6 px | 0.50 | 1.00 | 184 |
| stroke 150 | 99 % → 99 % | 2017.9 px | 0.49 | 1.00 | 71 |
| stroke 151 | 97 % → 97 % | 2241.9 px | 0.51 | 1.00 | 48 |
| stroke 152 | 99 % → 99 % | 2175.0 px | 0.49 | 1.00 | 65 |
| stroke 153 | 62 % → 62 % | 365.2 px | 0.49 | 1.00 | 319 |
| stroke 154 | 88 % → 88 % | 909.5 px | 0.52 | 1.00 | 161 |

Numbers say: wet paint spreads well beyond the stroke.

## Refs v3 · #31 Warhol blotted line — own sheet
own sheet 800 × 708 · Ink 0.98 · 25 px · 33.9 s

![Refs v3 · #31 Warhol blotted line — own sheet](Refs-v3-31-Warhol-blotted-line-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 1 % → 20 % | 8.2 px | 0.53 | 18.92 | 4 |
| stroke 2 | 2 % → 54 % | 11.8 px | 0.52 | 25.50 | 2 |
| stroke 3 | 2 % → 44 % | 12.6 px | 0.54 | 21.03 | 5 |
| stroke 4 | 1 % → 59 % | 11.2 px | 0.52 | 41.21 | 3 |
| stroke 5 | 1 % → 61 % | 8.7 px | 0.53 | 43.94 | 2 |
| stroke 6 | 6 % → 62 % | 34.4 px | 0.52 | 11.08 | 2 |
| stroke 7 | 4 % → 66 % | 23.2 px | 0.53 | 16.88 | 4 |
| stroke 8 | 2 % → 46 % | 11.4 px | 0.55 | 20.58 | 4 |
| stroke 9 | 5 % → 27 % | 14.5 px | 0.55 | 5.28 | 24 |
| stroke 10 | 3 % → 37 % | 16.5 px | 0.53 | 11.88 | 3 |
| stroke 11 | 4 % → 46 % | 26.0 px | 0.55 | 11.08 | 2 |
| stroke 12 | 6 % → 53 % | 32.3 px | 0.53 | 8.74 | 3 |
| stroke 13 | 8 % → 46 % | 43.4 px | 0.55 | 5.44 | 5 |
| stroke 14 | 7 % → 35 % | 19.7 px | 0.54 | 5.23 | 24 |
| stroke 15 | 7 % → 14 % | 20.1 px | 0.52 | 2.06 | 10 |
| stroke 16 | 2 % → 25 % | 13.4 px | 0.52 | 10.37 | 5 |
| stroke 17 | 7 % → 66 % | 60.5 px | 0.54 | 9.12 | 4 |
| stroke 18 | 19 % → 50 % | 60.4 px | 0.55 | 2.64 | 11 |
| stroke 19 | 10 % → 36 % | 47.0 px | 0.52 | 3.42 | 6 |
| stroke 20 | 11 % → 48 % | 82.6 px | 0.54 | 4.22 | 3 |
| stroke 21 | 1 % → 42 % | 9.5 px | 0.54 | 37.70 | 1 |
| stroke 22 | 5 % → 25 % | 12.6 px | 0.55 | 5.24 | 24 |
| stroke 23 | 3 % → 33 % | 10.7 px | 0.52 | 10.61 | 5 |
| stroke 24 | 4 % → 38 % | 12.4 px | 0.55 | 9.65 | 12 |
| stroke 25 | 13 % → 37 % | 60.0 px | 0.55 | 2.77 | 6 |
| stroke 26 | 14 % → 32 % | 59.1 px | 0.51 | 2.29 | 9 |
| stroke 27 | 11 % → 65 % | 50.3 px | 0.53 | 5.87 | 7 |
| stroke 28 | 9 % → 49 % | 76.8 px | 0.52 | 5.39 | 3 |
| stroke 29 | 13 % → 67 % | 65.7 px | 0.54 | 5.27 | 4 |
| stroke 30 | 3 % → 39 % | 13.2 px | 0.53 | 11.23 | 5 |
| stroke 31 | 13 % → 56 % | 45.1 px | 0.55 | 4.30 | 5 |
| stroke 32 | 3 % → 39 % | 15.4 px | 0.54 | 11.26 | 5 |
| stroke 33 | 12 % → 35 % | 53.1 px | 0.54 | 3.01 | 6 |
| stroke 34 | 11 % → 39 % | 82.1 px | 0.54 | 3.69 | 3 |
| stroke 35 | 14 % → 27 % | 38.0 px | 0.54 | 1.93 | 35 |
| stroke 36 | 9 % → 54 % | 27.8 px | 0.53 | 6.30 | 9 |
| stroke 37 | 17 % → 56 % | 71.2 px | 0.53 | 3.39 | 6 |
| stroke 38 | 16 % → 53 % | 112.1 px | 0.54 | 3.29 | 2 |
| stroke 39 | 7 % → 39 % | 25.7 px | 0.53 | 5.79 | 8 |
| stroke 40 | 15 % → 49 % | 83.9 px | 0.54 | 3.33 | 2 |
| stroke 41 | 5 % → 42 % | 18.3 px | 0.54 | 8.34 | 5 |
| stroke 42 | 8 % → 44 % | 33.9 px | 0.55 | 5.46 | 4 |
| stroke 43 | 20 % → 56 % | 68.1 px | 0.53 | 2.85 | 6 |
| stroke 44 | 17 % → 46 % | 53.2 px | 0.53 | 2.73 | 18 |
| stroke 45 | 26 % → 68 % | 143.5 px | 0.54 | 2.62 | 5 |
| stroke 46 | 9 % → 43 % | 65.9 px | 0.54 | 4.97 | 3 |
| stroke 47 | 16 % → 41 % | 69.3 px | 0.52 | 2.49 | 4 |
| stroke 48 | 22 % → 37 % | 84.6 px | 0.52 | 1.69 | 6 |
| stroke 49 | 30 % → 50 % | 170.5 px | 0.55 | 1.68 | 50 |
| stroke 50 | 31 % → 67 % | 208.7 px | 0.55 | 2.15 | 4 |
| stroke 51 | 23 % → 51 % | 80.0 px | 0.55 | 2.19 | 17 |
| stroke 52 | 16 % → 37 % | 56.3 px | 0.53 | 2.29 | 14 |
| stroke 53 | 11 % → 18 % | 29.8 px | 0.53 | 1.64 | 39 |
| stroke 54 | 23 % → 60 % | 94.7 px | 0.55 | 2.58 | 11 |
| stroke 55 | 3 % → 40 % | 23.3 px | 0.54 | 12.01 | 2 |
| stroke 56 | 37 % → 52 % | 136.3 px | 0.54 | 1.40 | 17 |
| stroke 57 | 17 % → 26 % | 38.0 px | 0.54 | 1.58 | 69 |
| stroke 58 | 26 % → 63 % | 182.3 px | 0.54 | 2.43 | 2 |
| stroke 59 | 37 % → 50 % | 142.2 px | 0.55 | 1.37 | 4 |
| stroke 60 | 37 % → 54 % | 141.1 px | 0.52 | 1.44 | 7 |
| stroke 61 | 13 % → 43 % | 53.0 px | 0.54 | 3.41 | 7 |
| stroke 62 | 28 % → 55 % | 127.4 px | 0.53 | 1.95 | 7 |
| stroke 63 | 32 % → 55 % | 203.7 px | 0.55 | 1.73 | 6 |
| stroke 64 | 25 % → 55 % | 103.5 px | 0.56 | 2.22 | 3 |
| stroke 65 | 23 % → 39 % | 88.4 px | 0.55 | 1.65 | 7 |
| stroke 66 | 24 % → 42 % | 130.6 px | 0.52 | 1.76 | 5 |
| stroke 67 | 24 % → 41 % | 108.1 px | 0.55 | 1.70 | 8 |
| stroke 68 | 12 % → 40 % | 42.6 px | 0.55 | 3.28 | 11 |
| stroke 69 | 20 % → 42 % | 80.3 px | 0.55 | 2.09 | 6 |
| stroke 70 | 33 % → 50 % | 190.8 px | 0.54 | 1.51 | 10 |
| stroke 71 | 26 % → 55 % | 196.1 px | 0.53 | 2.11 | 2 |
| stroke 72 | 31 % → 49 % | 252.6 px | 0.53 | 1.57 | 1 |
| stroke 73 | 33 % → 49 % | 260.1 px | 0.53 | 1.51 | 2 |
| stroke 74 | 37 % → 61 % | 132.7 px | 0.53 | 1.65 | 14 |
| stroke 75 | 15 % → 33 % | 65.3 px | 0.53 | 2.16 | 3 |
| stroke 76 | 40 % → 62 % | 186.2 px | 0.55 | 1.56 | 7 |
| stroke 77 | 19 % → 24 % | 51.4 px | 0.55 | 1.26 | 25 |
| stroke 78 | 27 % → 43 % | 194.9 px | 0.54 | 1.58 | 2 |
| stroke 79 | 21 % → 41 % | 44.3 px | 0.54 | 1.97 | 13 |
| stroke 80 | 31 % → 47 % | 217.4 px | 0.54 | 1.49 | 4 |
| stroke 81 | 36 % → 58 % | 301.7 px | 0.52 | 1.59 | 5 |
| stroke 82 | 17 % → 39 % | 72.8 px | 0.54 | 2.27 | 13 |
| stroke 83 | 29 % → 41 % | 93.1 px | 0.52 | 1.42 | 5 |
| stroke 84 | 38 % → 50 % | 312.1 px | 0.52 | 1.32 | 2 |
| stroke 85 | 40 % → 55 % | 149.6 px | 0.53 | 1.37 | 8 |
| stroke 86 | 42 % → 55 % | 267.0 px | 0.53 | 1.32 | 2 |
| stroke 87 | 21 % → 43 % | 182.5 px | 0.54 | 2.02 | 1 |
| stroke 88 | 36 % → 46 % | 189.7 px | 0.55 | 1.27 | 4 |
| stroke 89 | 46 % → 57 % | 205.8 px | 0.52 | 1.23 | 4 |
| stroke 90 | 52 % → 64 % | 291.1 px | 0.52 | 1.24 | 2 |
| stroke 91 | 27 % → 42 % | 113.1 px | 0.54 | 1.56 | 6 |
| stroke 92 | 24 % → 40 % | 85.1 px | 0.54 | 1.62 | 5 |
| stroke 93 | 28 % → 36 % | 82.1 px | 0.55 | 1.28 | 12 |
| stroke 94 | 33 % → 44 % | 269.7 px | 0.53 | 1.33 | 4 |
| stroke 95 | 29 % → 35 % | 92.8 px | 0.54 | 1.22 | 12 |
| stroke 96 | 27 % → 41 % | 203.4 px | 0.54 | 1.52 | 3 |
| stroke 97 | 46 % → 57 % | 208.4 px | 0.54 | 1.24 | 4 |
| stroke 98 | 52 % → 55 % | 175.1 px | 0.55 | 1.06 | 20 |
| stroke 99 | 16 % → 18 % | 60.9 px | 0.55 | 1.11 | 84 |
| stroke 100 | 30 % → 32 % | 221.8 px | 0.53 | 1.06 | 2 |
| stroke 101 | 10 % → 29 % | 41.3 px | 0.54 | 2.81 | 4 |
| stroke 102 | 44 % → 52 % | 163.9 px | 0.54 | 1.17 | 7 |
| stroke 103 | 27 % → 44 % | 103.2 px | 0.53 | 1.64 | 4 |
| stroke 104 | 44 % → 45 % | 334.9 px | 0.54 | 1.04 | 2 |
| stroke 105 | 43 % → 44 % | 146.9 px | 0.54 | 1.04 | 16 |
| stroke 106 | 37 % → 49 % | 157.4 px | 0.54 | 1.31 | 5 |
| stroke 107 | 25 % → 42 % | 191.2 px | 0.54 | 1.69 | 1 |
| stroke 108 | 40 % → 43 % | 130.0 px | 0.53 | 1.08 | 8 |
| stroke 109 | 38 % → 42 % | 245.0 px | 0.54 | 1.12 | 2 |
| stroke 110 | 30 % → 35 % | 112.9 px | 0.54 | 1.18 | 6 |
| stroke 111 | 24 % → 32 % | 62.4 px | 0.54 | 1.33 | 21 |
| stroke 112 | 54 % → 57 % | 276.2 px | 0.53 | 1.05 | 6 |
| stroke 113 | 72 % → 74 % | 489.6 px | 0.54 | 1.03 | 5 |
| stroke 114 | 39 % → 43 % | 246.8 px | 0.53 | 1.10 | 7 |
| stroke 115 | 21 % → 29 % | 79.5 px | 0.54 | 1.38 | 5 |
| stroke 116 | 47 % → 58 % | 176.5 px | 0.53 | 1.24 | 8 |
| stroke 117 | 38 % → 47 % | 159.1 px | 0.52 | 1.25 | 6 |
| stroke 118 | 36 % → 39 % | 208.7 px | 0.53 | 1.06 | 2 |
| stroke 119 | 43 % → 44 % | 171.3 px | 0.54 | 1.03 | 11 |
| stroke 120 | 36 % → 39 % | 152.4 px | 0.53 | 1.09 | 7 |
| stroke 121 | 33 % → 46 % | 167.5 px | 0.54 | 1.37 | 8 |
| stroke 122 | 44 % → 51 % | 196.2 px | 0.54 | 1.18 | 4 |
| stroke 123 | 36 % → 43 % | 177.0 px | 0.53 | 1.18 | 6 |
| stroke 124 | 50 % → 55 % | 268.4 px | 0.52 | 1.08 | 6 |

Numbers say: wet paint spreads well beyond the stroke.

## Refs v3 · #32 Thick orange swipes — own sheet
own sheet 800 × 800 · Impasto 1.00 · 76 px · 27.0 s

![Refs v3 · #32 Thick orange swipes — own sheet](Refs-v3-32-Thick-orange-swipes-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 14 % → 22 % | 68.5 px | 0.32 | 1.65 | 531 |
| stroke 2 | 19 % → 33 % | 155.7 px | 0.32 | 1.70 | 319 |
| stroke 3 | 15 % → 30 % | 278.6 px | 0.32 | 2.02 | 116 |
| stroke 4 | 23 % → 34 % | 220.3 px | 0.32 | 1.51 | 208 |
| stroke 5 | 16 % → 34 % | 370.8 px | 0.32 | 2.10 | 86 |
| stroke 6 | 25 % → 33 % | 352.0 px | 0.32 | 1.33 | 158 |
| stroke 7 | 18 % → 38 % | 420.4 px | 0.32 | 2.14 | 53 |
| stroke 8 | 27 % → 32 % | 464.1 px | 0.32 | 1.17 | 109 |
| stroke 9 | 25 % → 33 % | 492.3 px | 0.32 | 1.29 | 87 |
| stroke 10 | 22 % → 35 % | 442.2 px | 0.32 | 1.55 | 69 |
| stroke 11 | 13 % → 49 % | 301.0 px | 0.32 | 3.73 | 59 |
| stroke 12 | 19 % → 38 % | 371.0 px | 0.32 | 1.97 | 91 |
| stroke 13 | 16 % → 62 % | 137.3 px | 0.32 | 3.74 | 287 |
| stroke 14 | 16 % → 41 % | 286.0 px | 0.32 | 2.50 | 96 |
| stroke 15 | 16 % → 45 % | 213.4 px | 0.32 | 2.80 | 118 |
| stroke 16 | 18 % → 50 % | 180.9 px | 0.32 | 2.78 | 212 |
| stroke 17 | 19 % → 47 % | 213.9 px | 0.33 | 2.48 | 227 |
| stroke 18 | 20 % → 44 % | 240.7 px | 0.33 | 2.25 | 148 |
| stroke 19 | 21 % → 36 % | 355.8 px | 0.33 | 1.74 | 79 |
| stroke 20 | 20 % → 33 % | 386.7 px | 0.33 | 1.61 | 97 |
| stroke 21 | 19 % → 29 % | 324.2 px | 0.33 | 1.52 | 103 |
| stroke 22 | 6 % → 44 % | 101.9 px | 0.33 | 7.41 | 94 |
| stroke 23 | 17 % → 27 % | 295.2 px | 0.34 | 1.59 | 109 |
| stroke 24 | 12 % → 32 % | 101.3 px | 0.33 | 2.61 | 334 |
| stroke 25 | 17 % → 24 % | 293.1 px | 0.34 | 1.44 | 88 |
| stroke 26 | 25 % → 23 % | 160.2 px | 0.33 | 0.94 | 488 |
| stroke 27 | 26 % → 16 % | 140.3 px | 0.33 | 0.60 | 683 |
| stroke 28 | 34 % → 13 % | 174.9 px | 0.33 | 0.38 | 560 |
| stroke 29 | 11 % → 41 % | 107.3 px | 0.32 | 3.86 | 256 |
| stroke 30 | 18 % → 42 % | 128.3 px | 0.32 | 2.33 | 688 |
| stroke 31 | 26 % → 45 % | 162.4 px | 0.32 | 1.76 | 685 |
| stroke 32 | 32 % → 49 % | 199.0 px | 0.32 | 1.54 | 826 |
| stroke 33 | 41 % → 67 % | 371.3 px | 0.32 | 1.62 | 450 |
| stroke 34 | 37 % → 54 % | 239.2 px | 0.32 | 1.47 | 789 |
| stroke 35 | 38 % → 57 % | 272.4 px | 0.33 | 1.50 | 631 |
| stroke 36 | 36 % → 52 % | 252.3 px | 0.33 | 1.45 | 726 |
| stroke 37 | 34 % → 42 % | 217.5 px | 0.33 | 1.22 | 898 |
| stroke 38 | 38 % → 42 % | 302.9 px | 0.33 | 1.10 | 650 |
| stroke 39 | 38 % → 37 % | 389.1 px | 0.33 | 0.97 | 354 |

Numbers say: wet paint spreads well beyond the stroke.

## Refs v3 · #33 Red wet-in-wet flames — own sheet
own sheet 800 × 1083 · Watercolour 1.00 + water 60 % · 96 px · 54.9 s

![Refs v3 · #33 Red wet-in-wet flames — own sheet](Refs-v3-33-Red-wet-in-wet-flames-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 25 % → 55 % | 103.3 px | 0.36 | 2.15 | 1742 |
| stroke 2 | 28 % → 49 % | 141.4 px | 0.27 | 1.71 | 582 |
| stroke 3 | 29 % → 50 % | 242.2 px | 0.27 | 1.71 | 536 |
| stroke 4 | 36 % → 53 % | 249.2 px | 0.26 | 1.47 | 723 |
| stroke 5 | 38 % → 52 % | 353.8 px | 0.27 | 1.38 | 396 |
| stroke 6 | 36 % → 50 % | 316.4 px | 0.25 | 1.38 | 466 |
| stroke 7 | 34 % → 47 % | 200.5 px | 0.24 | 1.38 | 622 |
| stroke 8 | 40 % → 45 % | 199.2 px | 0.25 | 1.13 | 605 |

Numbers say: wet paint spreads well beyond the stroke.

## Refs v3 · #34 Magenta oil patches — own sheet
own sheet 800 × 1420 · Gouache 1.00 + turpentine 20 % · 90 px · 381.3 s

![Refs v3 · #34 Magenta oil patches — own sheet](Refs-v3-34-Magenta-oil-patches-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 15 % → 97 % | 84.7 px | 0.30 | 6.51 | 570 |
| stroke 2 | 30 % → 96 % | 188.6 px | 0.27 | 3.16 | 239 |
| stroke 3 | 21 % → 99 % | 232.4 px | 0.31 | 4.80 | 451 |
| stroke 4 | 49 % → 96 % | 207.0 px | 0.34 | 1.97 | 511 |
| stroke 5 | 55 % → 98 % | 301.3 px | 0.29 | 1.79 | 462 |
| stroke 6 | 37 % → 99 % | 385.0 px | 0.31 | 2.70 | 517 |
| stroke 7 | 44 % → 100 % | 721.4 px | 0.29 | 2.25 | 279 |
| stroke 8 | 53 % → 97 % | 425.4 px | 0.33 | 1.82 | 454 |
| stroke 9 | 62 % → 99 % | 628.5 px | 0.30 | 1.60 | 316 |
| stroke 10 | 45 % → 96 % | 383.3 px | 0.25 | 2.14 | 494 |
| stroke 11 | 75 % → 100 % | 940.0 px | 0.34 | 1.32 | 146 |
| stroke 12 | 58 % → 98 % | 388.7 px | 0.29 | 1.68 | 222 |
| stroke 13 | 74 % → 99 % | 572.0 px | 0.31 | 1.33 | 230 |
| stroke 14 | 75 % → 99 % | 651.5 px | 0.31 | 1.32 | 364 |
| stroke 15 | 62 % → 97 % | 796.3 px | 0.27 | 1.56 | 201 |
| stroke 16 | 53 % → 95 % | 448.3 px | 0.26 | 1.78 | 202 |
| stroke 17 | 61 % → 99 % | 739.3 px | 0.29 | 1.62 | 315 |
| stroke 18 | 67 % → 100 % | 698.0 px | 0.34 | 1.49 | 322 |
| stroke 19 | 7 % → 99 % | 92.3 px | 0.25 | 14.16 | 326 |
| stroke 20 | 13 % → 99 % | 160.8 px | 0.28 | 7.71 | 399 |
| stroke 21 | 18 % → 100 % | 375.5 px | 0.26 | 5.64 | 213 |
| stroke 22 | 21 % → 99 % | 479.3 px | 0.30 | 4.70 | 175 |
| stroke 23 | 6 % → 92 % | 99.6 px | 0.21 | 15.97 | 159 |
| stroke 24 | 9 % → 86 % | 173.9 px | 0.20 | 9.58 | 177 |
| stroke 25 | 12 % → 97 % | 108.8 px | 0.22 | 8.02 | 557 |
| stroke 26 | 22 % → 99 % | 157.0 px | 0.21 | 4.58 | 595 |
| stroke 27 | 31 % → 95 % | 212.1 px | 0.32 | 3.07 | 669 |
| stroke 28 | 30 % → 95 % | 394.3 px | 0.28 | 3.19 | 331 |
| stroke 29 | 41 % → 98 % | 616.9 px | 0.27 | 2.40 | 329 |
| stroke 30 | 28 % → 94 % | 479.1 px | 0.30 | 3.33 | 211 |
| stroke 31 | 47 % → 93 % | 630.1 px | 0.34 | 1.98 | 248 |
| stroke 32 | 28 % → 100 % | 576.0 px | 0.19 | 3.56 | 175 |
| stroke 33 | 31 % → 94 % | 395.3 px | 0.30 | 2.99 | 266 |
| stroke 34 | 37 % → 99 % | 650.4 px | 0.23 | 2.67 | 240 |
| stroke 35 | 32 % → 95 % | 640.1 px | 0.29 | 2.97 | 216 |
| stroke 36 | 41 % → 93 % | 539.9 px | 0.22 | 2.29 | 31 |
| stroke 37 | 63 % → 95 % | 291.3 px | 0.34 | 1.53 | 434 |
| stroke 38 | 50 % → 93 % | 508.5 px | 0.24 | 1.88 | 238 |
| stroke 39 | 20 % → 99 % | 212.3 px | 0.24 | 4.86 | 579 |
| stroke 40 | 52 % → 95 % | 390.5 px | 0.31 | 1.84 | 1038 |
| stroke 41 | 57 % → 96 % | 514.8 px | 0.30 | 1.68 | 863 |
| stroke 42 | 48 % → 94 % | 318.7 px | 0.31 | 1.96 | 833 |
| stroke 43 | 73 % → 99 % | 1107.5 px | 0.33 | 1.36 | 493 |
| stroke 44 | 43 % → 99 % | 492.2 px | 0.25 | 2.32 | 604 |
| stroke 45 | 66 % → 94 % | 930.0 px | 0.32 | 1.42 | 398 |
| stroke 46 | 26 % → 96 % | 329.3 px | 0.22 | 3.74 | 346 |
| stroke 47 | 70 % → 93 % | 1052.8 px | 0.35 | 1.32 | 233 |
| stroke 48 | 78 % → 99 % | 1121.4 px | 0.33 | 1.27 | 343 |
| stroke 49 | 65 % → 94 % | 673.3 px | 0.32 | 1.45 | 609 |
| stroke 50 | 76 % → 99 % | 1556.4 px | 0.33 | 1.30 | 233 |
| stroke 51 | 82 % → 96 % | 747.9 px | 0.35 | 1.16 | 311 |
| stroke 52 | 66 % → 99 % | 1123.0 px | 0.31 | 1.49 | 339 |
| stroke 53 | 77 % → 99 % | 1122.1 px | 0.32 | 1.30 | 353 |
| stroke 54 | 45 % → 95 % | 934.5 px | 0.28 | 2.10 | 212 |
| stroke 55 | 47 % → 99 % | 418.3 px | 0.27 | 2.10 | 480 |
| stroke 56 | 33 % → 70 % | 178.5 px | 0.25 | 2.13 | 473 |
| stroke 57 | 65 % → 95 % | 332.9 px | 0.34 | 1.47 | 736 |
| stroke 58 | 64 % → 94 % | 695.0 px | 0.35 | 1.45 | 290 |
| stroke 59 | 79 % → 95 % | 385.8 px | 0.38 | 1.20 | 503 |
| stroke 60 | 66 % → 93 % | 427.3 px | 0.30 | 1.41 | 429 |
| stroke 61 | 77 % → 98 % | 1036.3 px | 0.33 | 1.27 | 324 |
| stroke 62 | 88 % → 97 % | 941.9 px | 0.36 | 1.10 | 251 |
| stroke 63 | 59 % → 96 % | 464.2 px | 0.24 | 1.64 | 585 |
| stroke 64 | 70 % → 100 % | 1001.4 px | 0.27 | 1.41 | 403 |
| stroke 65 | 69 % → 98 % | 1198.6 px | 0.24 | 1.42 | 218 |
| stroke 66 | 74 % → 92 % | 647.7 px | 0.34 | 1.24 | 354 |
| stroke 67 | 41 % → 98 % | 313.9 px | 0.18 | 2.42 | 374 |
| stroke 68 | 30 % → 94 % | 323.2 px | 0.19 | 3.12 | 532 |
| stroke 69 | 43 % → 98 % | 409.3 px | 0.20 | 2.30 | 838 |
| stroke 70 | 54 % → 97 % | 353.8 px | 0.23 | 1.78 | 561 |
| stroke 71 | 56 % → 96 % | 490.5 px | 0.24 | 1.72 | 527 |
| stroke 72 | 45 % → 84 % | 411.5 px | 0.22 | 1.87 | 233 |
| stroke 73 | 66 % → 94 % | 513.2 px | 0.24 | 1.42 | 409 |
| stroke 74 | 48 % → 90 % | 727.9 px | 0.19 | 1.89 | 313 |
| stroke 75 | 57 % → 99 % | 452.9 px | 0.20 | 1.72 | 394 |
| stroke 76 | 59 % → 100 % | 931.7 px | 0.19 | 1.70 | 243 |
| stroke 77 | 63 % → 87 % | 702.1 px | 0.22 | 1.37 | 199 |
| stroke 78 | 67 % → 97 % | 1181.0 px | 0.21 | 1.44 | 265 |
| stroke 79 | 54 % → 78 % | 399.4 px | 0.19 | 1.44 | 498 |
| stroke 80 | 88 % → 96 % | 799.6 px | 0.27 | 1.09 | 334 |
| stroke 81 | 69 % → 95 % | 1260.6 px | 0.20 | 1.38 | 279 |
| stroke 82 | 82 % → 95 % | 899.9 px | 0.28 | 1.16 | 357 |
| stroke 83 | 74 % → 96 % | 953.8 px | 0.23 | 1.29 | 570 |
| stroke 84 | 78 % → 98 % | 976.3 px | 0.26 | 1.26 | 239 |
| stroke 85 | 63 % → 98 % | 755.1 px | 0.21 | 1.56 | 223 |
| stroke 86 | 89 % → 96 % | 865.6 px | 0.26 | 1.08 | 505 |
| stroke 87 | 66 % → 81 % | 549.0 px | 0.21 | 1.22 | 524 |
| stroke 88 | 60 % → 89 % | 733.3 px | 0.19 | 1.47 | 524 |
| stroke 89 | 27 % → 63 % | 300.9 px | 0.19 | 2.31 | 273 |
| stroke 90 | 72 % → 93 % | 937.5 px | 0.32 | 1.29 | 259 |
| stroke 91 | 63 % → 91 % | 1020.4 px | 0.33 | 1.44 | 54 |
| stroke 92 | 43 % → 99 % | 381.4 px | 0.20 | 2.29 | 941 |
| stroke 93 | 44 % → 99 % | 248.0 px | 0.14 | 2.25 | 1115 |
| stroke 94 | 47 % → 99 % | 322.7 px | 0.10 | 2.11 | 746 |
| stroke 95 | 60 % → 100 % | 1028.7 px | 0.20 | 1.66 | 377 |
| stroke 96 | 48 % → 99 % | 596.0 px | 0.08 | 2.06 | 549 |
| stroke 97 | 55 % → 98 % | 454.6 px | 0.16 | 1.76 | 1110 |
| stroke 98 | 67 % → 100 % | 617.4 px | 0.20 | 1.48 | 970 |
| stroke 99 | 60 % → 99 % | 471.7 px | 0.07 | 1.65 | 604 |
| stroke 100 | 70 % → 97 % | 437.5 px | 0.14 | 1.39 | 959 |
| stroke 101 | 68 % → 99 % | 1018.9 px | 0.07 | 1.44 | 257 |
| stroke 102 | 82 % → 99 % | 1615.4 px | 0.23 | 1.21 | 388 |
| stroke 103 | 55 % → 99 % | 706.0 px | 0.07 | 1.79 | 204 |
| stroke 104 | 76 % → 99 % | 863.9 px | 0.24 | 1.30 | 560 |
| stroke 105 | 79 % → 97 % | 660.0 px | 0.28 | 1.23 | 797 |
| stroke 106 | 64 % → 93 % | 717.9 px | 0.23 | 1.46 | 420 |
| stroke 107 | 80 % → 98 % | 1036.2 px | 0.23 | 1.23 | 455 |
| stroke 108 | 80 % → 100 % | 1092.7 px | 0.22 | 1.25 | 390 |
| stroke 109 | 75 % → 92 % | 1392.5 px | 0.35 | 1.23 | 41 |
| stroke 110 | 71 % → 99 % | 559.9 px | 0.15 | 1.40 | 814 |
| stroke 111 | 84 % → 99 % | 646.6 px | 0.18 | 1.18 | 980 |
| stroke 112 | 85 % → 100 % | 1128.3 px | 0.14 | 1.17 | 333 |
| stroke 113 | 81 % → 99 % | 724.1 px | 0.15 | 1.22 | 267 |
| stroke 114 | 91 % → 100 % | 1267.3 px | 0.15 | 1.10 | 340 |
| stroke 115 | 96 % → 99 % | 721.1 px | 0.13 | 1.03 | 374 |
| stroke 116 | 96 % → 99 % | 1110.1 px | 0.11 | 1.04 | 129 |
| stroke 117 | 97 % → 99 % | 1110.4 px | 0.08 | 1.02 | 258 |
| stroke 118 | 97 % → 99 % | 1802.9 px | 0.21 | 1.02 | 332 |
| stroke 119 | 97 % → 99 % | 1596.5 px | 0.16 | 1.02 | 315 |
| stroke 120 | 99 % → 99 % | 1925.2 px | 0.23 | 1.00 | 265 |
| stroke 121 | 100 % → 100 % | 1137.4 px | 0.13 | 1.00 | 554 |
| stroke 122 | 100 % → 99 % | 1548.6 px | 0.21 | 1.00 | 334 |
| stroke 123 | 99 % → 99 % | 1139.0 px | 0.13 | 1.00 | 279 |
| stroke 124 | 98 % → 99 % | 898.7 px | 0.17 | 1.01 | 514 |
| stroke 125 | 99 % → 99 % | 1714.5 px | 0.08 | 1.00 | 228 |
| stroke 126 | 99 % → 100 % | 1803.9 px | 0.19 | 1.01 | 290 |
| stroke 127 | 99 % → 99 % | 1264.6 px | 0.07 | 1.00 | 247 |
| stroke 128 | 91 % → 96 % | 2002.7 px | 0.34 | 1.05 | 19 |
| stroke 129 | 66 % → 94 % | 211.3 px | 0.15 | 1.42 | 214 |
| stroke 130 | 94 % → 94 % | 421.4 px | 0.40 | 0.99 | 122 |
| stroke 131 | 80 % → 93 % | 483.9 px | 0.31 | 1.16 | 1028 |
| stroke 132 | 83 % → 91 % | 414.5 px | 0.33 | 1.09 | 627 |
| stroke 133 | 85 % → 91 % | 586.6 px | 0.30 | 1.07 | 550 |
| stroke 134 | 89 % → 92 % | 837.2 px | 0.32 | 1.03 | 611 |
| stroke 135 | 88 % → 90 % | 1180.0 px | 0.29 | 1.02 | 191 |
| stroke 136 | 90 % → 89 % | 1183.4 px | 0.30 | 0.99 | 184 |
| stroke 137 | 80 % → 97 % | 547.6 px | 0.17 | 1.22 | 799 |
| stroke 138 | 92 % → 98 % | 823.1 px | 0.21 | 1.07 | 868 |
| stroke 139 | 91 % → 98 % | 1045.3 px | 0.23 | 1.07 | 640 |
| stroke 140 | 92 % → 97 % | 702.9 px | 0.17 | 1.05 | 756 |
| stroke 141 | 95 % → 96 % | 668.3 px | 0.19 | 1.01 | 935 |
| stroke 142 | 97 % → 99 % | 1892.3 px | 0.21 | 1.01 | 264 |
| stroke 143 | 97 % → 97 % | 1014.5 px | 0.19 | 1.00 | 587 |
| stroke 144 | 96 % → 97 % | 805.7 px | 0.08 | 1.01 | 631 |
| stroke 145 | 100 % → 100 % | 2016.4 px | 0.26 | 1.00 | 220 |
| stroke 146 | 96 % → 96 % | 1141.6 px | 0.11 | 1.00 | 267 |
| stroke 147 | 95 % → 95 % | 1377.3 px | 0.22 | 1.00 | 242 |
| stroke 148 | 77 % → 98 % | 1175.0 px | 0.21 | 1.27 | 348 |
| stroke 149 | 56 % → 72 % | 603.6 px | 0.19 | 1.28 | 621 |
| stroke 150 | 61 % → 73 % | 513.4 px | 0.20 | 1.20 | 768 |
| stroke 151 | 80 % → 84 % | 843.4 px | 0.20 | 1.05 | 434 |
| stroke 152 | 76 % → 77 % | 837.3 px | 0.18 | 1.01 | 408 |
| stroke 153 | 87 % → 88 % | 901.2 px | 0.20 | 1.01 | 629 |
| stroke 154 | 93 % → 93 % | 1613.1 px | 0.18 | 1.00 | 232 |
| stroke 155 | 83 % → 83 % | 1509.8 px | 0.17 | 1.00 | 222 |
| stroke 156 | 69 % → 69 % | 1430.5 px | 0.14 | 1.00 | 291 |
| stroke 157 | 77 % → 77 % | 1233.9 px | 0.18 | 0.99 | 339 |

Numbers say: wet paint spreads well beyond the stroke.

## Refs v3 · #35 Red band with runs — own sheet
own sheet 800 × 1191 · Watercolour 1.00 + water 70 % · 176 px · 60.8 s

![Refs v3 · #35 Red band with runs — own sheet](Refs-v3-35-Red-band-with-runs-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 40 % → 51 % | 297.4 px | 0.33 | 1.27 | 4141 |
| stroke 2 | 50 % → 52 % | 370.0 px | 0.32 | 1.03 | 6233 |
| stroke 3 | 49 % → 52 % | 357.7 px | 0.32 | 1.07 | 7116 |

## Refs v3 · #36 Magenta letters flat — own sheet
own sheet 800 × 1000 · Gouache 1.00 + water 15 % · 64 px · 56.2 s

![Refs v3 · #36 Magenta letters flat — own sheet](Refs-v3-36-Magenta-letters-flat-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 3 % → 36 % | 75.2 px | 0.40 | 10.65 | 36 |
| stroke 2 | 6 % → 34 % | 199.8 px | 0.40 | 5.63 | 16 |
| stroke 3 | 7 % → 25 % | 97.7 px | 0.40 | 3.77 | 24 |
| stroke 4 | 12 % → 30 % | 148.5 px | 0.40 | 2.54 | 31 |
| stroke 5 | 21 % → 34 % | 126.0 px | 0.40 | 1.63 | 151 |
| stroke 6 | 9 % → 31 % | 62.9 px | 0.40 | 3.35 | 109 |
| stroke 7 | 26 % → 38 % | 183.4 px | 0.40 | 1.49 | 73 |
| stroke 8 | 5 % → 42 % | 77.2 px | 0.40 | 7.80 | 81 |
| stroke 9 | 9 % → 42 % | 142.9 px | 0.40 | 4.56 | 66 |
| stroke 10 | 14 % → 33 % | 176.1 px | 0.40 | 2.31 | 94 |
| stroke 11 | 19 % → 36 % | 226.8 px | 0.40 | 1.93 | 99 |
| stroke 12 | 22 % → 37 % | 326.1 px | 0.40 | 1.67 | 76 |
| stroke 13 | 39 % → 42 % | 199.9 px | 0.40 | 1.07 | 233 |
| stroke 14 | 26 % → 33 % | 77.5 px | 0.41 | 1.24 | 612 |
| stroke 15 | 11 % → 40 % | 236.7 px | 0.40 | 3.57 | 32 |
| stroke 16 | 18 % → 41 % | 134.2 px | 0.40 | 2.27 | 153 |
| stroke 17 | 29 % → 41 % | 282.0 px | 0.40 | 1.43 | 177 |
| stroke 18 | 29 % → 42 % | 453.6 px | 0.40 | 1.48 | 64 |
| stroke 19 | 30 % → 42 % | 308.6 px | 0.40 | 1.41 | 132 |
| stroke 20 | 16 % → 40 % | 591.1 px | 0.41 | 2.53 | 11 |
| stroke 21 | 27 % → 45 % | 126.7 px | 0.41 | 1.63 | 392 |
| stroke 22 | 23 % → 45 % | 183.2 px | 0.41 | 1.91 | 156 |
| stroke 23 | 17 % → 48 % | 200.2 px | 0.41 | 2.75 | 100 |
| stroke 24 | 11 % → 49 % | 107.4 px | 0.40 | 4.53 | 141 |
| stroke 25 | 27 % → 36 % | 328.6 px | 0.40 | 1.36 | 101 |
| stroke 26 | 36 % → 40 % | 448.4 px | 0.40 | 1.09 | 82 |
| stroke 27 | 36 % → 39 % | 443.2 px | 0.40 | 1.09 | 70 |
| stroke 28 | 6 % → 52 % | 65.2 px | 0.41 | 8.22 | 71 |
| stroke 29 | 31 % → 41 % | 157.1 px | 0.40 | 1.31 | 373 |
| stroke 30 | 40 % → 46 % | 257.7 px | 0.40 | 1.13 | 216 |
| stroke 31 | 32 % → 42 % | 95.0 px | 0.41 | 1.35 | 543 |
| stroke 32 | 32 % → 45 % | 116.4 px | 0.41 | 1.41 | 442 |
| stroke 33 | 21 % → 44 % | 340.4 px | 0.41 | 2.12 | 84 |
| stroke 34 | 12 % → 46 % | 151.2 px | 0.41 | 3.68 | 90 |
| stroke 35 | 36 % → 42 % | 244.1 px | 0.41 | 1.19 | 193 |
| stroke 36 | 33 % → 39 % | 376.6 px | 0.41 | 1.18 | 119 |
| stroke 37 | 13 % → 35 % | 107.7 px | 0.42 | 2.70 | 68 |
| stroke 38 | 28 % → 43 % | 319.9 px | 0.41 | 1.54 | 92 |
| stroke 39 | 26 % → 36 % | 219.5 px | 0.41 | 1.41 | 107 |
| stroke 40 | 11 % → 27 % | 196.7 px | 0.42 | 2.50 | 43 |
| stroke 41 | 23 % → 34 % | 299.8 px | 0.42 | 1.51 | 54 |
| stroke 42 | 34 % → 36 % | 254.9 px | 0.41 | 1.04 | 225 |
| stroke 43 | 31 % → 30 % | 705.4 px | 0.42 | 0.99 | 33 |
| stroke 44 | 40 % → 40 % | 319.4 px | 0.41 | 0.99 | 110 |

Numbers say: wet paint spreads well beyond the stroke.

## Refs v3 · #37 Oil still life — own sheet
own sheet 800 × 810 · Gouache 1.00 + turpentine 20 % · 28 px · 184.4 s

![Refs v3 · #37 Oil still life — own sheet](Refs-v3-37-Oil-still-life-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 7 % → 90 % | 31.0 px | 0.23 | 12.05 | 21 |
| stroke 2 | 16 % → 98 % | 63.1 px | 0.30 | 6.02 | 30 |
| stroke 3 | 17 % → 99 % | 122.8 px | 0.32 | 5.93 | 6 |
| stroke 4 | 24 % → 99 % | 62.9 px | 0.35 | 4.20 | 62 |
| stroke 5 | 31 % → 99 % | 115.1 px | 0.33 | 3.14 | 36 |
| stroke 6 | 32 % → 89 % | 190.6 px | 0.23 | 2.82 | 14 |
| stroke 7 | 36 % → 100 % | 261.2 px | 0.33 | 2.81 | 11 |
| stroke 8 | 28 % → 99 % | 146.3 px | 0.23 | 3.51 | 34 |
| stroke 9 | 31 % → 99 % | 153.4 px | 0.26 | 3.21 | 17 |
| stroke 10 | 28 % → 96 % | 95.1 px | 0.21 | 3.44 | 27 |
| stroke 11 | 56 % → 94 % | 269.6 px | 0.29 | 1.66 | 23 |
| stroke 12 | 50 % → 99 % | 318.7 px | 0.34 | 2.00 | 15 |
| stroke 13 | 10 % → 87 % | 76.7 px | 0.27 | 8.79 | 6 |
| stroke 14 | 64 % → 99 % | 255.8 px | 0.35 | 1.54 | 46 |
| stroke 15 | 35 % → 77 % | 275.1 px | 0.22 | 2.21 | 14 |
| stroke 16 | 23 % → 88 % | 93.4 px | 0.32 | 3.76 | 42 |
| stroke 17 | 61 % → 99 % | 452.0 px | 0.29 | 1.60 | 9 |
| stroke 18 | 68 % → 97 % | 522.0 px | 0.33 | 1.43 | 19 |
| stroke 19 | 36 % → 79 % | 191.5 px | 0.21 | 2.18 | 27 |
| stroke 20 | 45 % → 98 % | 308.3 px | 0.23 | 2.18 | 14 |
| stroke 21 | 17 % → 93 % | 57.7 px | 0.28 | 5.44 | 44 |
| stroke 22 | 17 % → 98 % | 54.6 px | 0.31 | 5.84 | 30 |
| stroke 23 | 31 % → 97 % | 85.7 px | 0.31 | 3.11 | 68 |
| stroke 24 | 21 % → 98 % | 99.2 px | 0.26 | 4.62 | 22 |
| stroke 25 | 32 % → 90 % | 130.0 px | 0.31 | 2.77 | 35 |
| stroke 26 | 6 % → 77 % | 32.7 px | 0.19 | 13.39 | 14 |
| stroke 27 | 11 % → 70 % | 71.3 px | 0.20 | 6.15 | 12 |
| stroke 28 | 17 % → 83 % | 105.6 px | 0.23 | 5.04 | 16 |
| stroke 29 | 15 % → 74 % | 58.9 px | 0.19 | 4.76 | 33 |
| stroke 30 | 13 % → 85 % | 73.1 px | 0.27 | 6.34 | 11 |
| stroke 31 | 64 % → 98 % | 249.1 px | 0.33 | 1.52 | 63 |
| stroke 32 | 71 % → 91 % | 164.8 px | 0.36 | 1.29 | 170 |
| stroke 33 | 69 % → 93 % | 160.5 px | 0.35 | 1.34 | 222 |
| stroke 34 | 80 % → 98 % | 209.3 px | 0.37 | 1.23 | 136 |
| stroke 35 | 10 % → 89 % | 54.8 px | 0.29 | 8.66 | 29 |
| stroke 36 | 19 % → 94 % | 79.0 px | 0.32 | 4.88 | 56 |
| stroke 37 | 26 % → 97 % | 115.6 px | 0.32 | 3.76 | 45 |
| stroke 38 | 34 % → 91 % | 192.7 px | 0.35 | 2.65 | 40 |
| stroke 39 | 22 % → 98 % | 90.8 px | 0.30 | 4.37 | 58 |
| stroke 40 | 28 % → 92 % | 135.7 px | 0.26 | 3.28 | 42 |
| stroke 41 | 31 % → 92 % | 113.2 px | 0.28 | 2.96 | 103 |
| stroke 42 | 13 % → 77 % | 52.3 px | 0.24 | 6.06 | 43 |
| stroke 43 | 19 % → 75 % | 88.7 px | 0.23 | 3.99 | 53 |
| stroke 44 | 24 % → 85 % | 106.3 px | 0.20 | 3.53 | 58 |
| stroke 45 | 19 % → 84 % | 57.2 px | 0.24 | 4.39 | 105 |
| stroke 46 | 29 % → 82 % | 159.9 px | 0.27 | 2.87 | 37 |
| stroke 47 | 39 % → 96 % | 195.4 px | 0.32 | 2.50 | 30 |
| stroke 48 | 33 % → 87 % | 160.8 px | 0.25 | 2.63 | 30 |
| stroke 49 | 43 % → 99 % | 149.0 px | 0.39 | 2.28 | 66 |
| stroke 50 | 22 % → 88 % | 54.7 px | 0.23 | 3.98 | 89 |
| stroke 51 | 34 % → 95 % | 95.1 px | 0.23 | 2.79 | 115 |
| stroke 52 | 34 % → 96 % | 205.5 px | 0.26 | 2.87 | 16 |
| stroke 53 | 66 % → 100 % | 302.1 px | 0.42 | 1.51 | 47 |
| stroke 54 | 67 % → 99 % | 262.2 px | 0.38 | 1.48 | 54 |
| stroke 55 | 59 % → 97 % | 193.7 px | 0.30 | 1.66 | 95 |
| stroke 56 | 46 % → 91 % | 156.8 px | 0.26 | 1.97 | 64 |
| stroke 57 | 49 % → 96 % | 301.4 px | 0.23 | 1.97 | 18 |
| stroke 58 | 64 % → 94 % | 166.7 px | 0.28 | 1.47 | 119 |
| stroke 59 | 68 % → 97 % | 297.1 px | 0.29 | 1.42 | 56 |
| stroke 60 | 55 % → 96 % | 287.0 px | 0.28 | 1.74 | 28 |
| stroke 61 | 65 % → 89 % | 350.4 px | 0.32 | 1.37 | 37 |
| stroke 62 | 93 % → 100 % | 563.4 px | 0.43 | 1.08 | 26 |
| stroke 63 | 46 % → 97 % | 248.2 px | 0.19 | 2.13 | 27 |
| stroke 64 | 93 % → 99 % | 496.6 px | 0.40 | 1.07 | 40 |
| stroke 65 | 67 % → 97 % | 353.6 px | 0.28 | 1.44 | 44 |
| stroke 66 | 50 % → 83 % | 297.0 px | 0.26 | 1.68 | 27 |
| stroke 67 | 66 % → 89 % | 365.8 px | 0.30 | 1.33 | 34 |
| stroke 68 | 16 % → 76 % | 105.5 px | 0.14 | 4.72 | 14 |
| stroke 69 | 11 % → 88 % | 41.1 px | 0.27 | 8.34 | 27 |
| stroke 70 | 14 % → 86 % | 55.8 px | 0.30 | 6.19 | 39 |
| stroke 71 | 23 % → 91 % | 93.7 px | 0.30 | 3.97 | 24 |
| stroke 72 | 21 % → 91 % | 143.9 px | 0.28 | 4.25 | 18 |
| stroke 73 | 35 % → 93 % | 46.5 px | 0.10 | 2.63 | 164 |
| stroke 74 | 49 % → 98 % | 110.2 px | 0.12 | 1.99 | 92 |
| stroke 75 | 47 % → 86 % | 67.3 px | 0.10 | 1.83 | 199 |
| stroke 76 | 60 % → 88 % | 183.3 px | 0.12 | 1.47 | 81 |
| stroke 77 | 90 % → 97 % | 122.3 px | 0.10 | 1.07 | 129 |
| stroke 78 | 34 % → 69 % | 64.1 px | 0.09 | 1.99 | 113 |
| stroke 79 | 57 % → 67 % | 76.8 px | 0.10 | 1.19 | 130 |
| stroke 80 | 73 % → 97 % | 246.4 px | 0.16 | 1.32 | 78 |
| stroke 81 | 81 % → 92 % | 306.7 px | 0.10 | 1.13 | 49 |
| stroke 82 | 77 % → 91 % | 143.8 px | 0.12 | 1.18 | 41 |
| stroke 83 | 40 % → 43 % | 204.1 px | 0.08 | 1.09 | 25 |
| stroke 84 | 84 % → 97 % | 238.7 px | 0.11 | 1.15 | 52 |
| stroke 85 | 72 % → 83 % | 215.7 px | 0.11 | 1.16 | 38 |
| stroke 86 | 88 % → 100 % | 339.1 px | 0.12 | 1.13 | 65 |
| stroke 87 | 69 % → 83 % | 118.1 px | 0.11 | 1.20 | 88 |
| stroke 88 | 69 % → 79 % | 313.5 px | 0.10 | 1.14 | 33 |
| stroke 89 | 63 % → 90 % | 118.0 px | 0.09 | 1.43 | 138 |
| stroke 90 | 69 % → 67 % | 170.4 px | 0.09 | 0.98 | 37 |
| stroke 91 | 94 % → 96 % | 187.7 px | 0.11 | 1.03 | 53 |
| stroke 92 | 83 % → 81 % | 126.9 px | 0.11 | 0.98 | 56 |
| stroke 93 | 73 % → 97 % | 309.9 px | 0.19 | 1.33 | 62 |
| stroke 94 | 88 % → 96 % | 218.2 px | 0.11 | 1.09 | 38 |
| stroke 95 | 63 % → 64 % | 223.5 px | 0.11 | 1.01 | 57 |
| stroke 96 | 71 % → 89 % | 303.6 px | 0.14 | 1.26 | 53 |
| stroke 97 | 76 % → 97 % | 368.0 px | 0.14 | 1.27 | 40 |
| stroke 98 | 15 % → 45 % | 57.7 px | 0.02 | 3.12 | 57 |
| stroke 99 | 31 % → 66 % | 98.6 px | 0.09 | 2.12 | 68 |
| stroke 100 | 44 % → 72 % | 135.5 px | 0.08 | 1.64 | 74 |
| stroke 101 | 38 % → 64 % | 161.9 px | 0.19 | 1.70 | 31 |
| stroke 102 | 71 % → 84 % | 242.9 px | 0.18 | 1.20 | 54 |
| stroke 103 | 73 % → 82 % | 205.4 px | 0.21 | 1.12 | 76 |
| stroke 104 | 74 % → 79 % | 265.7 px | 0.12 | 1.07 | 49 |
| stroke 105 | 49 % → 62 % | 150.0 px | 0.05 | 1.28 | 74 |
| stroke 106 | 69 % → 74 % | 283.4 px | 0.06 | 1.07 | 40 |
| stroke 107 | 63 % → 63 % | 306.4 px | 0.03 | 0.99 | 32 |
| stroke 108 | 45 % → 81 % | 120.2 px | 0.18 | 1.80 | 80 |
| stroke 109 | 31 % → 97 % | 144.7 px | 0.12 | 3.09 | 33 |
| stroke 110 | 31 % → 45 % | 137.1 px | 0.28 | 1.46 | 36 |
| stroke 111 | 27 % → 78 % | 71.7 px | 0.05 | 2.92 | 88 |
| stroke 112 | 53 % → 80 % | 192.0 px | 0.12 | 1.51 | 40 |
| stroke 113 | 43 % → 91 % | 121.6 px | 0.12 | 2.09 | 135 |
| stroke 114 | 42 % → 64 % | 100.9 px | 0.19 | 1.54 | 58 |
| stroke 115 | 85 % → 98 % | 295.6 px | 0.25 | 1.15 | 105 |
| stroke 116 | 34 % → 60 % | 89.0 px | 0.17 | 1.80 | 144 |
| stroke 117 | 56 % → 81 % | 174.8 px | 0.22 | 1.45 | 98 |
| stroke 118 | 48 % → 69 % | 149.8 px | 0.22 | 1.42 | 59 |
| stroke 119 | 69 % → 80 % | 155.8 px | 0.20 | 1.16 | 60 |
| stroke 120 | 60 % → 67 % | 126.1 px | 0.22 | 1.12 | 174 |
| stroke 121 | 78 % → 92 % | 164.9 px | 0.21 | 1.18 | 94 |
| stroke 122 | 50 % → 88 % | 194.7 px | 0.16 | 1.76 | 78 |
| stroke 123 | 66 % → 70 % | 255.3 px | 0.24 | 1.06 | 55 |
| stroke 124 | 35 % → 73 % | 83.3 px | 0.05 | 2.11 | 80 |
| stroke 125 | 69 % → 78 % | 286.1 px | 0.28 | 1.13 | 57 |
| stroke 126 | 68 % → 82 % | 193.0 px | 0.15 | 1.21 | 117 |
| stroke 127 | 75 % → 88 % | 260.7 px | 0.21 | 1.17 | 34 |
| stroke 128 | 60 % → 69 % | 185.1 px | 0.14 | 1.15 | 65 |
| stroke 129 | 81 % → 83 % | 230.0 px | 0.14 | 1.03 | 57 |
| stroke 130 | 88 % → 96 % | 224.0 px | 0.22 | 1.09 | 84 |
| stroke 131 | 40 % → 51 % | 165.8 px | 0.12 | 1.28 | 49 |
| stroke 132 | 63 % → 88 % | 205.7 px | 0.06 | 1.38 | 71 |
| stroke 133 | 79 % → 87 % | 207.9 px | 0.27 | 1.10 | 84 |
| stroke 134 | 82 % → 85 % | 331.3 px | 0.24 | 1.04 | 89 |
| stroke 135 | 72 % → 71 % | 216.1 px | 0.10 | 0.99 | 24 |
| stroke 136 | 78 % → 88 % | 263.8 px | 0.16 | 1.14 | 114 |
| stroke 137 | 74 % → 84 % | 256.3 px | 0.20 | 1.14 | 153 |
| stroke 138 | 70 % → 72 % | 310.6 px | 0.15 | 1.02 | 41 |
| stroke 139 | 84 % → 84 % | 231.5 px | 0.19 | 1.00 | 163 |
| stroke 140 | 34 % → 33 % | 142.1 px | 0.20 | 0.98 | 35 |
| stroke 141 | 79 % → 79 % | 260.4 px | 0.18 | 1.00 | 107 |
| stroke 142 | 93 % → 95 % | 258.2 px | 0.15 | 1.02 | 45 |
| stroke 143 | 96 % → 96 % | 452.6 px | 0.18 | 1.00 | 56 |
| stroke 144 | 64 % → 69 % | 208.3 px | 0.19 | 1.08 | 83 |
| stroke 145 | 78 % → 76 % | 226.3 px | 0.33 | 0.98 | 97 |
| stroke 146 | 43 % → 51 % | 226.2 px | 0.07 | 1.19 | 37 |
| stroke 147 | 69 % → 86 % | 328.7 px | 0.11 | 1.25 | 51 |
| stroke 148 | 80 % → 87 % | 389.3 px | 0.21 | 1.09 | 56 |
| stroke 149 | 86 % → 86 % | 378.0 px | 0.22 | 1.00 | 45 |
| stroke 150 | 94 % → 93 % | 489.0 px | 0.10 | 0.99 | 44 |
| stroke 151 | 38 % → 75 % | 96.7 px | 0.22 | 1.95 | 226 |
| stroke 152 | 39 % → 82 % | 189.0 px | 0.13 | 2.07 | 26 |
| stroke 153 | 41 % → 67 % | 187.7 px | 0.12 | 1.63 | 62 |
| stroke 154 | 29 % → 58 % | 124.6 px | 0.14 | 1.98 | 45 |
| stroke 155 | 49 % → 65 % | 112.1 px | 0.24 | 1.33 | 143 |
| stroke 156 | 63 % → 77 % | 224.6 px | 0.24 | 1.21 | 94 |
| stroke 157 | 61 % → 67 % | 173.8 px | 0.24 | 1.09 | 168 |
| stroke 158 | 65 % → 65 % | 173.6 px | 0.18 | 1.00 | 76 |
| stroke 159 | 51 % → 52 % | 201.9 px | 0.19 | 1.02 | 40 |
| stroke 160 | 38 % → 42 % | 133.5 px | 0.10 | 1.10 | 25 |
| stroke 161 | 34 % → 85 % | 138.1 px | 0.13 | 2.48 | 32 |
| stroke 162 | 70 % → 96 % | 247.7 px | 0.14 | 1.37 | 60 |
| stroke 163 | 23 % → 58 % | 98.3 px | 0.03 | 2.58 | 31 |
| stroke 164 | 65 % → 82 % | 201.8 px | 0.09 | 1.26 | 120 |
| stroke 165 | 62 % → 68 % | 348.4 px | 0.11 | 1.08 | 30 |
| stroke 166 | 89 % → 97 % | 413.5 px | 0.16 | 1.09 | 51 |
| stroke 167 | 78 % → 86 % | 241.3 px | 0.07 | 1.11 | 80 |
| stroke 168 | 88 % → 90 % | 400.8 px | 0.06 | 1.03 | 80 |
| stroke 169 | 79 % → 81 % | 399.2 px | 0.13 | 1.03 | 56 |
| stroke 170 | 63 % → 71 % | 325.4 px | 0.04 | 1.13 | 68 |
| stroke 171 | 30 % → 34 % | 145.3 px | 0.02 | 1.15 | 32 |
| stroke 172 | 43 % → 41 % | 227.1 px | 0.02 | 0.96 | 35 |
| stroke 173 | 58 % → 62 % | 272.4 px | 0.12 | 1.06 | 41 |
| stroke 174 | 52 % → 81 % | 146.1 px | 0.08 | 1.56 | 68 |
| stroke 175 | 59 % → 87 % | 153.4 px | 0.09 | 1.49 | 110 |
| stroke 176 | 45 % → 96 % | 202.6 px | 0.02 | 2.13 | 44 |
| stroke 177 | 59 % → 89 % | 310.1 px | 0.12 | 1.51 | 23 |
| stroke 178 | 53 % → 88 % | 219.0 px | 0.02 | 1.66 | 39 |
| stroke 179 | 61 % → 85 % | 201.4 px | 0.14 | 1.38 | 47 |
| stroke 180 | 71 % → 84 % | 214.3 px | 0.12 | 1.19 | 112 |
| stroke 181 | 67 % → 95 % | 249.8 px | 0.02 | 1.41 | 62 |
| stroke 182 | 45 % → 81 % | 216.6 px | 0.05 | 1.77 | 36 |
| stroke 183 | 61 % → 94 % | 260.3 px | 0.02 | 1.53 | 39 |
| stroke 184 | 72 % → 94 % | 407.0 px | 0.02 | 1.30 | 25 |
| stroke 185 | 70 % → 85 % | 292.8 px | 0.02 | 1.21 | 49 |
| stroke 186 | 57 % → 79 % | 269.1 px | 0.08 | 1.40 | 33 |
| stroke 187 | 82 % → 89 % | 456.7 px | 0.02 | 1.09 | 28 |
| stroke 188 | 80 % → 86 % | 369.2 px | 0.03 | 1.08 | 33 |
| stroke 189 | 84 % → 95 % | 393.5 px | 0.02 | 1.13 | 61 |
| stroke 190 | 91 % → 92 % | 425.2 px | 0.13 | 1.01 | 43 |
| stroke 191 | 93 % → 92 % | 471.8 px | 0.07 | 0.99 | 25 |
| stroke 192 | 80 % → 82 % | 430.0 px | 0.11 | 1.03 | 32 |
| stroke 193 | 68 % → 76 % | 354.3 px | 0.02 | 1.13 | 33 |
| stroke 194 | 76 % → 78 % | 377.1 px | 0.02 | 1.02 | 25 |
| stroke 195 | 89 % → 95 % | 265.6 px | 0.23 | 1.07 | 50 |
| stroke 196 | 86 % → 93 % | 235.9 px | 0.27 | 1.09 | 60 |
| stroke 197 | 89 % → 99 % | 788.1 px | 0.26 | 1.11 | 11 |
| stroke 198 | 94 % → 97 % | 457.6 px | 0.18 | 1.04 | 22 |
| stroke 199 | 92 % → 99 % | 281.6 px | 0.27 | 1.07 | 50 |
| stroke 200 | 89 % → 94 % | 597.0 px | 0.20 | 1.05 | 21 |
| stroke 201 | 80 % → 85 % | 736.6 px | 0.24 | 1.06 | 8 |
| stroke 202 | 81 % → 86 % | 322.7 px | 0.21 | 1.07 | 42 |
| stroke 203 | 95 % → 97 % | 591.4 px | 0.17 | 1.02 | 18 |
| stroke 204 | 87 % → 90 % | 318.3 px | 0.27 | 1.03 | 33 |
| stroke 205 | 75 % → 80 % | 505.0 px | 0.17 | 1.07 | 9 |
| stroke 206 | 86 % → 89 % | 436.9 px | 0.22 | 1.03 | 18 |
| stroke 207 | 86 % → 87 % | 308.9 px | 0.25 | 1.02 | 30 |
| stroke 208 | 95 % → 97 % | 635.2 px | 0.21 | 1.02 | 17 |
| stroke 209 | 92 % → 95 % | 846.0 px | 0.18 | 1.03 | 10 |
| stroke 210 | 81 % → 81 % | 385.5 px | 0.24 | 1.00 | 25 |
| stroke 211 | 81 % → 83 % | 630.7 px | 0.21 | 1.03 | 10 |
| stroke 212 | 98 % → 99 % | 852.0 px | 0.27 | 1.01 | 6 |
| stroke 213 | 86 % → 88 % | 589.3 px | 0.26 | 1.02 | 21 |
| stroke 214 | 91 % → 92 % | 667.9 px | 0.19 | 1.01 | 12 |
| stroke 215 | 97 % → 99 % | 612.6 px | 0.20 | 1.02 | 19 |
| stroke 216 | 97 % → 99 % | 707.8 px | 0.22 | 1.02 | 14 |
| stroke 217 | 85 % → 90 % | 353.6 px | 0.24 | 1.06 | 41 |
| stroke 218 | 85 % → 92 % | 535.5 px | 0.28 | 1.08 | 18 |
| stroke 219 | 93 % → 95 % | 391.8 px | 0.28 | 1.02 | 35 |
| stroke 220 | 95 % → 96 % | 739.0 px | 0.25 | 1.01 | 16 |
| stroke 221 | 91 % → 93 % | 403.3 px | 0.29 | 1.02 | 42 |
| stroke 222 | 85 % → 86 % | 782.9 px | 0.18 | 1.01 | 6 |
| stroke 223 | 87 % → 89 % | 655.6 px | 0.22 | 1.02 | 12 |
| stroke 224 | 84 % → 86 % | 772.1 px | 0.23 | 1.02 | 8 |
| stroke 225 | 89 % → 89 % | 692.3 px | 0.20 | 1.00 | 9 |
| stroke 226 | 92 % → 92 % | 853.6 px | 0.22 | 1.00 | 8 |
| stroke 227 | 88 % → 89 % | 807.9 px | 0.27 | 1.01 | 11 |
| stroke 228 | 84 % → 86 % | 335.1 px | 0.36 | 1.03 | 31 |
| stroke 229 | 92 % → 95 % | 616.1 px | 0.38 | 1.03 | 17 |
| stroke 230 | 97 % → 99 % | 545.1 px | 0.34 | 1.02 | 20 |
| stroke 231 | 96 % → 97 % | 436.0 px | 0.35 | 1.01 | 36 |
| stroke 232 | 92 % → 93 % | 587.5 px | 0.36 | 1.01 | 24 |
| stroke 233 | 98 % → 99 % | 686.4 px | 0.31 | 1.01 | 13 |
| stroke 234 | 76 % → 80 % | 425.4 px | 0.02 | 1.06 | 10 |
| stroke 235 | 91 % → 93 % | 470.6 px | 0.03 | 1.02 | 15 |
| stroke 236 | 85 % → 88 % | 769.0 px | 0.03 | 1.03 | 4 |
| stroke 237 | 92 % → 93 % | 513.1 px | 0.04 | 1.01 | 10 |
| stroke 238 | 81 % → 82 % | 497.7 px | 0.02 | 1.01 | 8 |
| stroke 239 | 88 % → 88 % | 406.4 px | 0.03 | 1.01 | 18 |
| stroke 240 | 66 % → 71 % | 508.8 px | 0.19 | 1.08 | 13 |
| stroke 241 | 73 % → 77 % | 638.1 px | 0.17 | 1.06 | 10 |
| stroke 242 | 60 % → 64 % | 451.5 px | 0.19 | 1.07 | 11 |
| stroke 243 | 70 % → 72 % | 313.2 px | 0.13 | 1.02 | 21 |
| stroke 244 | 56 % → 56 % | 392.2 px | 0.02 | 0.99 | 5 |
| stroke 245 | 57 % → 58 % | 190.8 px | 0.15 | 1.01 | 59 |
| stroke 246 | 70 % → 71 % | 211.4 px | 0.21 | 1.00 | 58 |

Numbers say: wet paint spreads well beyond the stroke.

## Refs v3 · #38 Sanguine drawing — own sheet
own sheet 800 × 1092 · Charcoal 0.50 · Pastel 0.50 · 12 px · 85.1 s

![Refs v3 · #38 Sanguine drawing — own sheet](Refs-v3-38-Sanguine-drawing-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 6 % → 43 % | 11.5 px | 0.48 | 6.68 | 4 |
| stroke 2 | 7 % → 30 % | 9.5 px | 0.53 | 4.54 | 4 |
| stroke 3 | 10 % → 39 % | 15.2 px | 0.47 | 4.10 | 3 |
| stroke 4 | 8 % → 27 % | 11.5 px | 0.50 | 3.35 | 4 |
| stroke 5 | 19 % → 29 % | 26.2 px | 0.49 | 1.51 | 5 |
| stroke 6 | 13 % → 42 % | 18.2 px | 0.50 | 3.20 | 6 |
| stroke 7 | 15 % → 36 % | 21.5 px | 0.51 | 2.33 | 2 |
| stroke 8 | 19 % → 27 % | 33.2 px | 0.51 | 1.43 | 2 |
| stroke 9 | 27 % → 24 % | 58.0 px | 0.51 | 0.91 | 1 |
| stroke 10 | 37 % → 23 % | 61.7 px | 0.49 | 0.63 | 4 |
| stroke 11 | 37 % → 20 % | 102.5 px | 0.44 | 0.55 | 1 |
| stroke 12 | 26 % → 35 % | 52.9 px | 0.52 | 1.38 | 2 |
| stroke 13 | 39 % → 12 % | 95.5 px | 0.53 | 0.30 | 2 |
| stroke 14 | 28 % → 29 % | 59.6 px | 0.49 | 1.06 | 1 |
| stroke 15 | 15 % → 50 % | 42.5 px | 0.46 | 3.27 | 0 |
| stroke 16 | 8 % → 29 % | 11.9 px | 0.52 | 3.47 | 5 |
| stroke 17 | 25 % → 41 % | 50.4 px | 0.53 | 1.65 | 1 |
| stroke 18 | 8 % → 54 % | 10.2 px | 0.49 | 6.46 | 3 |
| stroke 19 | 6 % → 30 % | 9.7 px | 0.48 | 5.29 | 1 |
| stroke 20 | 7 % → 35 % | 11.4 px | 0.52 | 4.81 | 2 |
| stroke 21 | 15 % → 32 % | 24.9 px | 0.52 | 2.09 | 3 |
| stroke 22 | 14 % → 41 % | 18.6 px | 0.48 | 2.85 | 4 |
| stroke 23 | 26 % → 36 % | 41.1 px | 0.52 | 1.37 | 6 |
| stroke 24 | 26 % → 34 % | 46.4 px | 0.51 | 1.29 | 2 |
| stroke 25 | 10 % → 56 % | 11.1 px | 0.49 | 5.93 | 7 |
| stroke 26 | 10 % → 40 % | 16.2 px | 0.47 | 3.88 | 2 |
| stroke 27 | 9 % → 10 % | 21.4 px | 0.49 | 1.10 | 1 |
| stroke 28 | 16 % → 52 % | 35.8 px | 0.47 | 3.21 | 1 |
| stroke 29 | 23 % → 31 % | 52.7 px | 0.49 | 1.34 | 1 |
| stroke 30 | 22 % → 21 % | 42.0 px | 0.50 | 0.97 | 3 |
| stroke 31 | 9 % → 24 % | 10.8 px | 0.53 | 2.58 | 10 |
| stroke 32 | 8 % → 37 % | 12.2 px | 0.50 | 4.95 | 3 |
| stroke 33 | 7 % → 30 % | 9.9 px | 0.53 | 4.19 | 3 |
| stroke 34 | 29 % → 34 % | 56.1 px | 0.53 | 1.18 | 1 |
| stroke 35 | 15 % → 39 % | 34.4 px | 0.50 | 2.69 | 2 |
| stroke 36 | 19 % → 24 % | 34.4 px | 0.51 | 1.25 | 1 |
| stroke 37 | 17 % → 26 % | 26.6 px | 0.51 | 1.56 | 8 |
| stroke 38 | 34 % → 9 % | 94.1 px | 0.54 | 0.26 | 1 |
| stroke 39 | 19 % → 28 % | 49.5 px | 0.52 | 1.44 | 0 |
| stroke 40 | 31 % → 32 % | 87.7 px | 0.49 | 1.01 | 0 |
| stroke 41 | 31 % → 32 % | 74.0 px | 0.51 | 1.03 | 1 |
| stroke 42 | 25 % → 18 % | 49.8 px | 0.52 | 0.71 | 1 |
| stroke 43 | 36 % → 30 % | 79.0 px | 0.50 | 0.84 | 1 |
| stroke 44 | 24 % → 30 % | 56.4 px | 0.52 | 1.25 | 1 |
| stroke 45 | 5 % → 49 % | 14.9 px | 0.51 | 9.39 | 0 |
| stroke 46 | 11 % → 53 % | 19.1 px | 0.51 | 4.91 | 2 |
| stroke 47 | 15 % → 36 % | 33.2 px | 0.53 | 2.40 | 1 |
| stroke 48 | 8 % → 28 % | 11.9 px | 0.50 | 3.58 | 6 |
| stroke 49 | 7 % → 27 % | 17.3 px | 0.50 | 3.89 | 1 |
| stroke 50 | 8 % → 39 % | 12.3 px | 0.50 | 4.95 | 3 |
| stroke 51 | 11 % → 35 % | 16.4 px | 0.51 | 3.24 | 5 |
| stroke 52 | 16 % → 23 % | 22.1 px | 0.46 | 1.43 | 7 |
| stroke 53 | 11 % → 12 % | 11.8 px | 0.48 | 1.09 | 4 |
| stroke 54 | 10 % → 39 % | 15.3 px | 0.43 | 3.76 | 3 |
| stroke 55 | 12 % → 31 % | 25.8 px | 0.50 | 2.48 | 2 |
| stroke 56 | 12 % → 44 % | 15.8 px | 0.47 | 3.59 | 3 |
| stroke 57 | 7 % → 20 % | 17.4 px | 0.47 | 2.97 | 0 |
| stroke 58 | 23 % → 43 % | 34.4 px | 0.47 | 1.86 | 2 |
| stroke 59 | 24 % → 37 % | 31.1 px | 0.41 | 1.56 | 3 |
| stroke 60 | 20 % → 29 % | 45.9 px | 0.52 | 1.44 | 1 |
| stroke 61 | 21 % → 55 % | 36.8 px | 0.47 | 2.55 | 3 |
| stroke 62 | 34 % → 37 % | 78.2 px | 0.48 | 1.09 | 2 |
| stroke 63 | 32 % → 28 % | 53.1 px | 0.52 | 0.88 | 3 |
| stroke 64 | 23 % → 28 % | 28.2 px | 0.51 | 1.23 | 2 |
| stroke 65 | 23 % → 18 % | 35.6 px | 0.52 | 0.79 | 2 |
| stroke 66 | 20 % → 27 % | 41.0 px | 0.50 | 1.34 | 1 |
| stroke 67 | 30 % → 32 % | 47.9 px | 0.52 | 1.07 | 6 |
| stroke 68 | 31 % → 19 % | 38.5 px | 0.48 | 0.59 | 4 |
| stroke 69 | 26 % → 51 % | 65.5 px | 0.42 | 1.99 | 1 |
| stroke 70 | 22 % → 41 % | 63.2 px | 0.49 | 1.82 | 0 |
| stroke 71 | 33 % → 6 % | 41.3 px | 0.51 | 0.17 | 2 |
| stroke 72 | 14 % → 35 % | 35.7 px | 0.53 | 2.55 | 1 |
| stroke 73 | 48 % → 22 % | 82.5 px | 0.51 | 0.45 | 3 |
| stroke 74 | 11 % → 32 % | 21.8 px | 0.50 | 2.85 | 1 |
| stroke 75 | 19 % → 19 % | 35.4 px | 0.48 | 0.97 | 2 |
| stroke 76 | 42 % → 30 % | 97.7 px | 0.48 | 0.71 | 2 |
| stroke 77 | 38 % → 45 % | 56.4 px | 0.43 | 1.18 | 2 |
| stroke 78 | 35 % → 34 % | 96.9 px | 0.52 | 0.98 | 1 |
| stroke 79 | 36 % → 33 % | 70.2 px | 0.46 | 0.92 | 2 |
| stroke 80 | 24 % → 43 % | 52.5 px | 0.50 | 1.74 | 2 |
| stroke 81 | 38 % → 20 % | 82.3 px | 0.50 | 0.54 | 1 |
| stroke 82 | 32 % → 29 % | 86.6 px | 0.52 | 0.90 | 0 |
| stroke 83 | 32 % → 27 % | 89.0 px | 0.52 | 0.83 | 1 |
| stroke 84 | 8 % → 44 % | 10.8 px | 0.51 | 5.20 | 2 |
| stroke 85 | 19 % → 46 % | 48.7 px | 0.50 | 2.38 | 1 |
| stroke 86 | 26 % → 52 % | 58.7 px | 0.53 | 2.00 | 1 |
| stroke 87 | 10 % → 53 % | 15.8 px | 0.51 | 5.57 | 3 |
| stroke 88 | 20 % → 58 % | 49.5 px | 0.52 | 2.85 | 2 |
| stroke 89 | 21 % → 56 % | 51.8 px | 0.50 | 2.63 | 2 |
| stroke 90 | 7 % → 44 % | 12.6 px | 0.52 | 6.05 | 5 |
| stroke 91 | 15 % → 40 % | 23.7 px | 0.51 | 2.67 | 6 |
| stroke 92 | 18 % → 36 % | 49.1 px | 0.50 | 1.95 | 0 |
| stroke 93 | 25 % → 41 % | 40.4 px | 0.52 | 1.63 | 6 |
| stroke 94 | 31 % → 43 % | 64.0 px | 0.51 | 1.35 | 3 |
| stroke 95 | 27 % → 45 % | 60.7 px | 0.51 | 1.71 | 1 |
| stroke 96 | 9 % → 56 % | 25.0 px | 0.50 | 6.22 | 0 |
| stroke 97 | 6 % → 38 % | 13.4 px | 0.53 | 6.28 | 2 |
| stroke 98 | 10 % → 47 % | 15.1 px | 0.53 | 4.97 | 4 |
| stroke 99 | 13 % → 26 % | 22.4 px | 0.53 | 1.97 | 3 |
| stroke 100 | 18 % → 43 % | 51.5 px | 0.53 | 2.38 | 0 |
| stroke 101 | 15 % → 42 % | 37.1 px | 0.53 | 2.83 | 2 |
| stroke 102 | 19 % → 39 % | 45.9 px | 0.53 | 2.09 | 1 |
| stroke 103 | 8 % → 55 % | 18.1 px | 0.48 | 6.78 | 1 |
| stroke 104 | 6 % → 15 % | 13.9 px | 0.48 | 2.42 | 1 |
| stroke 105 | 12 % → 14 % | 26.3 px | 0.47 | 1.15 | 2 |
| stroke 106 | 17 % → 30 % | 47.1 px | 0.50 | 1.76 | 1 |
| stroke 107 | 9 % → 19 % | 24.1 px | 0.53 | 2.23 | 0 |
| stroke 108 | 13 % → 24 % | 35.5 px | 0.54 | 1.85 | 0 |
| stroke 109 | 17 % → 27 % | 39.1 px | 0.53 | 1.57 | 1 |
| stroke 110 | 7 % → 45 % | 12.5 px | 0.51 | 6.38 | 2 |
| stroke 111 | 14 % → 38 % | 24.3 px | 0.51 | 2.80 | 2 |
| stroke 112 | 10 % → 32 % | 18.3 px | 0.49 | 3.16 | 2 |
| stroke 113 | 17 % → 18 % | 46.5 px | 0.47 | 1.11 | 0 |
| stroke 114 | 8 % → 21 % | 11.1 px | 0.51 | 2.80 | 2 |
| stroke 115 | 13 % → 34 % | 24.1 px | 0.52 | 2.57 | 2 |
| stroke 116 | 13 % → 26 % | 17.3 px | 0.51 | 1.91 | 3 |
| stroke 117 | 14 % → 41 % | 16.0 px | 0.51 | 2.87 | 4 |
| stroke 118 | 27 % → 33 % | 32.3 px | 0.53 | 1.22 | 3 |
| stroke 119 | 18 % → 35 % | 47.3 px | 0.47 | 1.91 | 0 |
| stroke 120 | 22 % → 38 % | 30.1 px | 0.51 | 1.71 | 3 |
| stroke 121 | 30 % → 39 % | 76.2 px | 0.52 | 1.29 | 0 |
| stroke 122 | 34 % → 20 % | 74.2 px | 0.49 | 0.59 | 1 |
| stroke 123 | 8 % → 34 % | 12.6 px | 0.49 | 4.23 | 9 |
| stroke 124 | 8 % → 16 % | 11.7 px | 0.49 | 1.88 | 4 |
| stroke 125 | 12 % → 22 % | 22.1 px | 0.47 | 1.81 | 3 |
| stroke 126 | 8 % → 16 % | 12.5 px | 0.50 | 1.97 | 9 |
| stroke 127 | 8 % → 16 % | 12.9 px | 0.46 | 2.04 | 2 |
| stroke 128 | 11 % → 39 % | 16.9 px | 0.51 | 3.66 | 3 |
| stroke 129 | 16 % → 14 % | 25.3 px | 0.50 | 0.89 | 5 |
| stroke 130 | 15 % → 37 % | 20.5 px | 0.49 | 2.45 | 3 |
| stroke 131 | 7 % → 32 % | 13.3 px | 0.52 | 4.80 | 1 |
| stroke 132 | 7 % → 16 % | 12.7 px | 0.50 | 2.29 | 4 |
| stroke 133 | 8 % → 0 % | 14.4 px | 0.00 | 0.00 | 1 |
| stroke 134 | 16 % → 36 % | 26.2 px | 0.49 | 2.31 | 7 |
| stroke 135 | 7 % → 15 % | 12.3 px | 0.51 | 2.01 | 5 |
| stroke 136 | 7 % → 21 % | 12.3 px | 0.54 | 2.87 | 3 |
| stroke 137 | 7 % → 42 % | 10.7 px | 0.49 | 6.10 | 6 |
| stroke 138 | 17 % → 10 % | 23.2 px | 0.51 | 0.60 | 7 |
| stroke 139 | 10 % → 22 % | 25.2 px | 0.50 | 2.10 | 2 |
| stroke 140 | 12 % → 46 % | 19.9 px | 0.48 | 3.89 | 5 |
| stroke 141 | 16 % → 42 % | 26.4 px | 0.50 | 2.59 | 4 |
| stroke 142 | 21 % → 13 % | 30.0 px | 0.50 | 0.61 | 4 |
| stroke 143 | 8 % → 32 % | 14.9 px | 0.48 | 4.15 | 2 |
| stroke 144 | 6 % → 33 % | 11.5 px | 0.51 | 5.14 | 2 |
| stroke 145 | 15 % → 35 % | 17.2 px | 0.50 | 2.30 | 10 |
| stroke 146 | 30 % → 5 % | 58.8 px | 0.54 | 0.16 | 2 |
| stroke 147 | 13 % → 21 % | 20.4 px | 0.53 | 1.65 | 3 |
| stroke 148 | 13 % → 26 % | 19.6 px | 0.51 | 2.07 | 5 |
| stroke 149 | 16 % → 18 % | 26.3 px | 0.51 | 1.14 | 3 |
| stroke 150 | 8 % → 30 % | 12.7 px | 0.47 | 3.86 | 2 |
| stroke 151 | 8 % → 36 % | 12.0 px | 0.49 | 4.71 | 9 |
| stroke 152 | 15 % → 39 % | 24.7 px | 0.49 | 2.58 | 3 |
| stroke 153 | 8 % → 14 % | 10.9 px | 0.51 | 1.80 | 2 |
| stroke 154 | 20 % → 34 % | 33.8 px | 0.50 | 1.72 | 3 |
| stroke 155 | 14 % → 35 % | 19.3 px | 0.50 | 2.50 | 5 |
| stroke 156 | 15 % → 33 % | 23.5 px | 0.46 | 2.22 | 5 |
| stroke 157 | 15 % → 34 % | 23.4 px | 0.48 | 2.24 | 8 |
| stroke 158 | 15 % → 35 % | 18.2 px | 0.50 | 2.37 | 4 |
| stroke 159 | 30 % → 24 % | 69.1 px | 0.54 | 0.79 | 1 |
| stroke 160 | 10 % → 24 % | 15.7 px | 0.50 | 2.41 | 6 |
| stroke 161 | 32 % → 18 % | 40.1 px | 0.51 | 0.56 | 6 |
| stroke 162 | 16 % → 17 % | 22.9 px | 0.49 | 1.08 | 11 |
| stroke 163 | 26 % → 32 % | 50.4 px | 0.48 | 1.23 | 3 |
| stroke 164 | 13 % → 26 % | 22.6 px | 0.54 | 1.95 | 4 |
| stroke 165 | 13 % → 10 % | 21.2 px | 0.54 | 0.78 | 4 |
| stroke 166 | 15 % → 35 % | 30.2 px | 0.54 | 2.29 | 1 |
| stroke 167 | 14 % → 20 % | 31.7 px | 0.53 | 1.38 | 1 |
| stroke 168 | 28 % → 30 % | 49.4 px | 0.48 | 1.09 | 2 |
| stroke 169 | 18 % → 13 % | 28.7 px | 0.51 | 0.75 | 6 |
| stroke 170 | 22 % → 38 % | 34.5 px | 0.49 | 1.76 | 6 |
| stroke 171 | 8 % → 19 % | 8.9 px | 0.51 | 2.32 | 7 |
| stroke 172 | 15 % → 40 % | 25.9 px | 0.49 | 2.62 | 3 |
| stroke 173 | 15 % → 43 % | 24.2 px | 0.51 | 2.80 | 7 |
| stroke 174 | 28 % → 28 % | 44.4 px | 0.46 | 1.00 | 6 |
| stroke 175 | 22 % → 38 % | 37.3 px | 0.50 | 1.73 | 2 |
| stroke 176 | 34 % → 29 % | 71.6 px | 0.53 | 0.84 | 4 |
| stroke 177 | 37 % → 20 % | 55.4 px | 0.46 | 0.52 | 4 |
| stroke 178 | 15 % → 24 % | 34.5 px | 0.50 | 1.68 | 1 |
| stroke 179 | 17 % → 28 % | 25.7 px | 0.52 | 1.60 | 5 |
| stroke 180 | 10 % → 34 % | 27.4 px | 0.52 | 3.59 | 0 |
| stroke 181 | 19 % → 39 % | 26.3 px | 0.51 | 2.09 | 6 |
| stroke 182 | 19 % → 26 % | 31.8 px | 0.48 | 1.36 | 2 |
| stroke 183 | 18 % → 20 % | 23.2 px | 0.52 | 1.13 | 5 |
| stroke 184 | 15 % → 25 % | 23.7 px | 0.50 | 1.67 | 6 |
| stroke 185 | 11 % → 52 % | 28.1 px | 0.51 | 4.75 | 0 |
| stroke 186 | 18 % → 44 % | 30.0 px | 0.51 | 2.46 | 5 |
| stroke 187 | 17 % → 8 % | 31.6 px | 0.46 | 0.45 | 2 |
| stroke 188 | 11 % → 41 % | 21.0 px | 0.49 | 3.57 | 1 |
| stroke 189 | 16 % → 52 % | 37.7 px | 0.50 | 3.32 | 1 |
| stroke 190 | 33 % → 9 % | 81.6 px | 0.53 | 0.27 | 1 |
| stroke 191 | 24 % → 34 % | 67.0 px | 0.50 | 1.43 | 1 |
| stroke 192 | 34 % → 34 % | 75.9 px | 0.43 | 0.99 | 1 |
| stroke 193 | 19 % → 13 % | 35.5 px | 0.53 | 0.70 | 2 |
| stroke 194 | 24 % → 40 % | 49.5 px | 0.51 | 1.65 | 1 |
| stroke 195 | 14 % → 45 % | 23.1 px | 0.49 | 3.16 | 7 |
| stroke 196 | 29 % → 18 % | 43.4 px | 0.49 | 0.60 | 5 |
| stroke 197 | 51 % → 18 % | 88.5 px | 0.49 | 0.35 | 5 |
| stroke 198 | 20 % → 18 % | 31.9 px | 0.51 | 0.92 | 2 |
| stroke 199 | 27 % → 3 % | 32.5 px | 0.52 | 0.11 | 7 |
| stroke 200 | 19 % → 29 % | 38.4 px | 0.50 | 1.51 | 2 |
| stroke 201 | 23 % → 18 % | 56.6 px | 0.54 | 0.75 | 1 |
| stroke 202 | 27 % → 49 % | 45.9 px | 0.51 | 1.77 | 4 |
| stroke 203 | 28 % → 27 % | 50.2 px | 0.46 | 0.97 | 4 |
| stroke 204 | 19 % → 43 % | 40.6 px | 0.50 | 2.25 | 1 |
| stroke 205 | 26 % → 10 % | 45.0 px | 0.47 | 0.39 | 2 |
| stroke 206 | 31 % → 37 % | 52.2 px | 0.50 | 1.21 | 3 |
| stroke 207 | 27 % → 11 % | 57.7 px | 0.50 | 0.43 | 3 |
| stroke 208 | 10 % → 6 % | 20.1 px | 0.50 | 0.65 | 3 |
| stroke 209 | 37 % → 0 % | 102.4 px | 0.00 | 0.00 | 1 |
| stroke 210 | 27 % → 42 % | 50.6 px | 0.50 | 1.54 | 4 |
| stroke 211 | 33 % → 54 % | 93.0 px | 0.51 | 1.62 | 1 |
| stroke 212 | 21 % → 16 % | 58.4 px | 0.50 | 0.78 | 0 |
| stroke 213 | 27 % → 33 % | 40.1 px | 0.53 | 1.22 | 5 |
| stroke 214 | 42 % → 40 % | 81.0 px | 0.48 | 0.97 | 2 |
| stroke 215 | 27 % → 43 % | 44.2 px | 0.51 | 1.60 | 6 |
| stroke 216 | 23 % → 26 % | 34.5 px | 0.51 | 1.17 | 6 |
| stroke 217 | 14 % → 54 % | 28.8 px | 0.48 | 3.83 | 1 |
| stroke 218 | 33 % → 34 % | 47.9 px | 0.48 | 1.03 | 3 |
| stroke 219 | 21 % → 29 % | 33.2 px | 0.47 | 1.38 | 4 |
| stroke 220 | 35 % → 12 % | 57.6 px | 0.53 | 0.34 | 3 |
| stroke 221 | 20 % → 12 % | 41.0 px | 0.49 | 0.62 | 1 |
| stroke 222 | 38 % → 39 % | 63.0 px | 0.50 | 1.01 | 3 |
| stroke 223 | 20 % → 46 % | 49.4 px | 0.51 | 2.30 | 1 |
| stroke 224 | 21 % → 45 % | 34.5 px | 0.49 | 2.19 | 5 |
| stroke 225 | 23 % → 29 % | 37.9 px | 0.54 | 1.26 | 2 |
| stroke 226 | 29 % → 13 % | 47.7 px | 0.54 | 0.45 | 4 |
| stroke 227 | 17 % → 38 % | 37.8 px | 0.50 | 2.22 | 1 |
| stroke 228 | 18 % → 14 % | 50.7 px | 0.53 | 0.79 | 1 |
| stroke 229 | 24 % → 40 % | 59.3 px | 0.52 | 1.65 | 1 |
| stroke 230 | 10 % → 16 % | 28.9 px | 0.51 | 1.57 | 1 |
| stroke 231 | 26 % → 43 % | 64.4 px | 0.46 | 1.66 | 1 |
| stroke 232 | 43 % → 9 % | 94.8 px | 0.54 | 0.20 | 1 |
| stroke 233 | 48 % → 0 % | 79.3 px | 0.54 | 0.00 | 1 |
| stroke 234 | 47 % → 13 % | 88.5 px | 0.49 | 0.28 | 0 |
| stroke 235 | 42 % → 35 % | 122.9 px | 0.47 | 0.83 | 0 |
| stroke 236 | 41 % → 13 % | 101.3 px | 0.54 | 0.31 | 1 |
| stroke 237 | 20 % → 33 % | 35.5 px | 0.52 | 1.63 | 4 |
| stroke 238 | 43 % → 41 % | 105.9 px | 0.47 | 0.95 | 1 |
| stroke 239 | 21 % → 7 % | 35.7 px | 0.54 | 0.30 | 2 |
| stroke 240 | 24 % → 46 % | 43.6 px | 0.51 | 1.96 | 2 |
| stroke 241 | 49 % → 33 % | 101.4 px | 0.48 | 0.68 | 1 |
| stroke 242 | 22 % → 38 % | 57.1 px | 0.51 | 1.71 | 0 |
| stroke 243 | 15 % → 49 % | 36.9 px | 0.47 | 3.20 | 1 |
| stroke 244 | 33 % → 23 % | 54.5 px | 0.50 | 0.69 | 5 |
| stroke 245 | 52 % → 12 % | 106.2 px | 0.54 | 0.24 | 1 |
| stroke 246 | 30 % → 40 % | 50.3 px | 0.49 | 1.34 | 4 |
| stroke 247 | 33 % → 37 % | 80.0 px | 0.50 | 1.11 | 2 |
| stroke 248 | 47 % → 18 % | 102.6 px | 0.44 | 0.39 | 1 |
| stroke 249 | 29 % → 2 % | 48.6 px | 0.54 | 0.07 | 4 |
| stroke 250 | 36 % → 34 % | 79.3 px | 0.47 | 0.96 | 1 |
| stroke 251 | 38 % → 0 % | 83.6 px | 0.00 | 0.00 | 1 |
| stroke 252 | 24 % → 43 % | 52.4 px | 0.49 | 1.79 | 1 |
| stroke 253 | 31 % → 10 % | 69.8 px | 0.49 | 0.33 | 1 |
| stroke 254 | 25 % → 1 % | 50.7 px | 0.51 | 0.04 | 3 |
| stroke 255 | 39 % → 17 % | 83.0 px | 0.50 | 0.44 | 1 |
| stroke 256 | 31 % → 11 % | 61.1 px | 0.47 | 0.37 | 1 |
| stroke 257 | 35 % → 14 % | 82.2 px | 0.51 | 0.40 | 1 |
| stroke 258 | 59 % → 17 % | 108.2 px | 0.54 | 0.29 | 4 |
| stroke 259 | 35 % → 38 % | 78.1 px | 0.46 | 1.10 | 1 |
| stroke 260 | 25 % → 26 % | 63.4 px | 0.53 | 1.06 | 0 |
| stroke 261 | 36 % → 33 % | 80.0 px | 0.50 | 0.90 | 1 |
| stroke 262 | 54 % → 10 % | 152.2 px | 0.51 | 0.19 | 0 |
| stroke 263 | 52 % → 19 % | 151.8 px | 0.51 | 0.37 | 0 |
| stroke 264 | 24 % → 21 % | 26.7 px | 0.53 | 0.89 | 4 |
| stroke 265 | 42 % → 39 % | 105.1 px | 0.45 | 0.91 | 2 |
| stroke 266 | 37 % → 8 % | 107.2 px | 0.46 | 0.23 | 1 |
| stroke 267 | 40 % → 40 % | 112.4 px | 0.45 | 0.99 | 0 |
| stroke 268 | 29 % → 31 % | 82.9 px | 0.51 | 1.05 | 0 |
| stroke 269 | 36 % → 38 % | 88.1 px | 0.49 | 1.07 | 2 |
| stroke 270 | 32 % → 35 % | 77.2 px | 0.54 | 1.11 | 2 |
| stroke 271 | 46 % → 24 % | 107.2 px | 0.51 | 0.51 | 2 |
| stroke 272 | 49 % → 19 % | 132.5 px | 0.49 | 0.38 | 0 |
| stroke 273 | 48 % → 28 % | 138.7 px | 0.54 | 0.59 | 0 |
| stroke 274 | 32 % → 24 % | 75.0 px | 0.49 | 0.75 | 1 |
| stroke 275 | 39 % → 15 % | 81.5 px | 0.49 | 0.40 | 1 |
| stroke 276 | 40 % → 35 % | 109.6 px | 0.49 | 0.89 | 1 |
| stroke 277 | 51 % → 19 % | 120.4 px | 0.42 | 0.37 | 1 |
| stroke 278 | 33 % → 43 % | 93.9 px | 0.50 | 1.31 | 2 |
| stroke 279 | 49 % → 34 % | 104.7 px | 0.49 | 0.69 | 2 |
| stroke 280 | 40 % → 11 % | 64.8 px | 0.53 | 0.27 | 3 |
| stroke 281 | 37 % → 20 % | 100.5 px | 0.51 | 0.53 | 1 |
| stroke 282 | 40 % → 29 % | 108.6 px | 0.49 | 0.73 | 0 |
| stroke 283 | 54 % → 19 % | 154.3 px | 0.52 | 0.35 | 1 |
| stroke 284 | 48 % → 29 % | 106.7 px | 0.50 | 0.60 | 1 |
| stroke 285 | 48 % → 29 % | 105.5 px | 0.48 | 0.61 | 2 |
| stroke 286 | 35 % → 43 % | 96.6 px | 0.50 | 1.24 | 0 |
| stroke 287 | 39 % → 24 % | 103.0 px | 0.49 | 0.61 | 0 |
| stroke 288 | 49 % → 17 % | 120.6 px | 0.50 | 0.35 | 2 |
| stroke 289 | 59 % → 5 % | 124.5 px | 0.40 | 0.08 | 1 |
| stroke 290 | 30 % → 34 % | 62.0 px | 0.53 | 1.10 | 2 |
| stroke 291 | 30 % → 1 % | 65.3 px | 0.46 | 0.04 | 2 |
| stroke 292 | 41 % → 8 % | 116.3 px | 0.46 | 0.20 | 1 |
| stroke 293 | 18 % → 51 % | 49.7 px | 0.49 | 2.91 | 0 |
| stroke 294 | 7 % → 69 % | 13.8 px | 0.51 | 9.62 | 2 |
| stroke 295 | 6 % → 57 % | 12.3 px | 0.50 | 9.13 | 1 |
| stroke 296 | 10 % → 52 % | 17.1 px | 0.49 | 5.35 | 1 |
| stroke 297 | 16 % → 56 % | 35.6 px | 0.49 | 3.52 | 2 |
| stroke 298 | 9 % → 51 % | 14.8 px | 0.49 | 5.46 | 2 |
| stroke 299 | 7 % → 53 % | 18.9 px | 0.48 | 7.87 | 0 |
| stroke 300 | 9 % → 32 % | 14.2 px | 0.50 | 3.57 | 1 |
| stroke 301 | 12 % → 26 % | 32.1 px | 0.49 | 2.20 | 1 |
| stroke 302 | 18 % → 21 % | 46.3 px | 0.51 | 1.17 | 0 |
| stroke 303 | 12 % → 26 % | 28.4 px | 0.50 | 2.20 | 1 |
| stroke 304 | 9 % → 7 % | 16.6 px | 0.54 | 0.81 | 2 |
| stroke 305 | 12 % → 5 % | 19.6 px | 0.54 | 0.44 | 2 |
| stroke 306 | 17 % → 36 % | 33.4 px | 0.47 | 2.12 | 1 |
| stroke 307 | 9 % → 29 % | 21.2 px | 0.52 | 3.37 | 2 |
| stroke 308 | 12 % → 32 % | 24.6 px | 0.54 | 2.63 | 1 |
| stroke 309 | 23 % → 27 % | 64.3 px | 0.52 | 1.19 | 1 |
| stroke 310 | 7 % → 67 % | 11.6 px | 0.46 | 9.75 | 3 |
| stroke 311 | 7 % → 38 % | 11.6 px | 0.53 | 5.41 | 4 |
| stroke 312 | 15 % → 46 % | 25.8 px | 0.49 | 3.16 | 2 |
| stroke 313 | 12 % → 56 % | 18.1 px | 0.50 | 4.49 | 3 |
| stroke 314 | 20 % → 56 % | 40.4 px | 0.47 | 2.74 | 2 |
| stroke 315 | 13 % → 58 % | 23.4 px | 0.53 | 4.41 | 2 |
| stroke 316 | 28 % → 66 % | 36.3 px | 0.48 | 2.35 | 2 |
| stroke 317 | 18 % → 37 % | 52.6 px | 0.50 | 2.03 | 0 |
| stroke 318 | 8 % → 73 % | 12.7 px | 0.49 | 8.94 | 2 |
| stroke 319 | 8 % → 28 % | 13.6 px | 0.53 | 3.51 | 3 |
| stroke 320 | 15 % → 22 % | 29.1 px | 0.54 | 1.43 | 4 |
| stroke 321 | 17 % → 33 % | 30.7 px | 0.52 | 1.88 | 2 |
| stroke 322 | 22 % → 14 % | 40.7 px | 0.54 | 0.61 | 2 |
| stroke 323 | 18 % → 2 % | 29.1 px | 0.52 | 0.11 | 8 |
| stroke 324 | 29 % → 32 % | 59.9 px | 0.53 | 1.09 | 3 |
| stroke 325 | 25 % → 40 % | 42.7 px | 0.52 | 1.57 | 2 |
| stroke 326 | 33 % → 8 % | 72.0 px | 0.54 | 0.25 | 2 |
| stroke 327 | 34 % → 1 % | 95.6 px | 0.53 | 0.03 | 1 |
| stroke 328 | 25 % → 0 % | 71.1 px | 0.00 | 0.00 | 1 |
| stroke 329 | 8 % → 13 % | 10.8 px | 0.50 | 1.59 | 8 |
| stroke 330 | 18 % → 11 % | 29.1 px | 0.50 | 0.64 | 5 |
| stroke 331 | 6 % → 41 % | 13.0 px | 0.52 | 6.44 | 2 |
| stroke 332 | 12 % → 22 % | 18.4 px | 0.51 | 1.89 | 8 |
| stroke 333 | 26 % → 15 % | 40.6 px | 0.51 | 0.59 | 5 |
| stroke 334 | 23 % → 10 % | 38.2 px | 0.51 | 0.42 | 3 |
| stroke 335 | 34 % → 12 % | 55.2 px | 0.50 | 0.35 | 5 |
| stroke 336 | 28 % → 1 % | 77.3 px | 0.45 | 0.02 | 0 |
| stroke 337 | 21 % → 4 % | 60.8 px | 0.54 | 0.17 | 2 |
| stroke 338 | 50 % → 13 % | 86.3 px | 0.49 | 0.26 | 2 |
| stroke 339 | 26 % → 27 % | 49.1 px | 0.51 | 1.03 | 1 |
| stroke 340 | 8 % → 3 % | 12.8 px | 0.51 | 0.40 | 3 |
| stroke 341 | 11 % → 0 % | 22.6 px | 0.00 | 0.00 | 1 |
| stroke 342 | 21 % → 7 % | 32.6 px | 0.51 | 0.34 | 11 |
| stroke 343 | 7 % → 20 % | 15.9 px | 0.52 | 2.92 | 1 |
| stroke 344 | 14 % → 18 % | 34.8 px | 0.50 | 1.24 | 2 |
| stroke 345 | 24 % → 0 % | 52.6 px | 0.00 | 0.00 | 2 |
| stroke 346 | 22 % → 19 % | 51.2 px | 0.50 | 0.86 | 1 |
| stroke 347 | 17 % → 0 % | 34.3 px | 0.00 | 0.00 | 1 |
| stroke 348 | 9 % → 30 % | 22.3 px | 0.50 | 3.46 | 0 |
| stroke 349 | 9 % → 32 % | 19.8 px | 0.52 | 3.49 | 1 |
| stroke 350 | 18 % → 40 % | 49.7 px | 0.49 | 2.16 | 1 |
| stroke 351 | 14 % → 43 % | 18.0 px | 0.52 | 3.05 | 4 |
| stroke 352 | 21 % → 42 % | 51.8 px | 0.50 | 1.97 | 1 |
| stroke 353 | 18 % → 41 % | 46.7 px | 0.52 | 2.27 | 2 |
| stroke 354 | 15 % → 52 % | 39.4 px | 0.52 | 3.59 | 0 |
| stroke 355 | 6 % → 15 % | 11.8 px | 0.50 | 2.37 | 4 |
| stroke 356 | 10 % → 52 % | 11.3 px | 0.52 | 5.25 | 6 |
| stroke 357 | 9 % → 54 % | 9.6 px | 0.49 | 6.08 | 5 |
| stroke 358 | 11 % → 57 % | 10.4 px | 0.53 | 5.37 | 7 |
| stroke 359 | 5 % → 34 % | 12.1 px | 0.51 | 7.40 | 1 |
| stroke 360 | 9 % → 59 % | 9.7 px | 0.52 | 6.27 | 8 |
| stroke 361 | 8 % → 64 % | 9.7 px | 0.50 | 7.87 | 6 |
| stroke 362 | 8 % → 36 % | 10.1 px | 0.53 | 4.67 | 9 |
| stroke 363 | 9 % → 53 % | 12.4 px | 0.51 | 5.75 | 5 |
| stroke 364 | 8 % → 36 % | 11.8 px | 0.49 | 4.84 | 9 |
| stroke 365 | 7 % → 39 % | 10.8 px | 0.49 | 5.27 | 3 |
| stroke 366 | 18 % → 54 % | 19.0 px | 0.50 | 3.02 | 5 |
| stroke 367 | 6 % → 41 % | 9.2 px | 0.47 | 6.42 | 2 |
| stroke 368 | 10 % → 54 % | 11.2 px | 0.52 | 5.66 | 10 |
| stroke 369 | 20 % → 53 % | 48.1 px | 0.53 | 2.67 | 1 |
| stroke 370 | 9 % → 60 % | 12.9 px | 0.52 | 6.92 | 5 |
| stroke 371 | 7 % → 25 % | 16.3 px | 0.49 | 3.71 | 1 |
| stroke 372 | 8 % → 52 % | 11.6 px | 0.49 | 6.88 | 4 |
| stroke 373 | 11 % → 60 % | 13.8 px | 0.53 | 5.44 | 5 |
| stroke 374 | 8 % → 48 % | 11.8 px | 0.50 | 6.40 | 9 |
| stroke 375 | 8 % → 70 % | 10.2 px | 0.53 | 8.72 | 5 |
| stroke 376 | 8 % → 49 % | 11.0 px | 0.44 | 5.89 | 3 |
| stroke 377 | 15 % → 60 % | 23.5 px | 0.52 | 4.01 | 10 |
| stroke 378 | 12 % → 48 % | 17.1 px | 0.54 | 4.04 | 5 |
| stroke 379 | 7 % → 40 % | 11.8 px | 0.53 | 5.32 | 5 |
| stroke 380 | 11 % → 40 % | 16.8 px | 0.52 | 3.79 | 10 |
| stroke 381 | 8 % → 34 % | 11.7 px | 0.53 | 3.99 | 5 |
| stroke 382 | 9 % → 45 % | 12.5 px | 0.51 | 5.24 | 7 |
| stroke 383 | 17 % → 48 % | 23.8 px | 0.53 | 2.81 | 7 |
| stroke 384 | 12 % → 28 % | 27.3 px | 0.48 | 2.35 | 2 |
| stroke 385 | 10 % → 41 % | 11.3 px | 0.53 | 3.96 | 11 |
| stroke 386 | 15 % → 58 % | 24.1 px | 0.52 | 3.82 | 8 |
| stroke 387 | 12 % → 51 % | 18.6 px | 0.48 | 4.19 | 7 |
| stroke 388 | 16 % → 55 % | 15.0 px | 0.50 | 3.51 | 5 |
| stroke 389 | 7 % → 61 % | 10.5 px | 0.51 | 8.22 | 5 |
| stroke 390 | 10 % → 45 % | 15.9 px | 0.49 | 4.71 | 4 |
| stroke 391 | 19 % → 34 % | 29.4 px | 0.54 | 1.77 | 4 |
| stroke 392 | 7 % → 14 % | 13.4 px | 0.50 | 1.84 | 3 |
| stroke 393 | 8 % → 45 % | 11.7 px | 0.52 | 5.42 | 6 |
| stroke 394 | 15 % → 48 % | 20.8 px | 0.50 | 3.13 | 2 |
| stroke 395 | 15 % → 50 % | 18.7 px | 0.53 | 3.46 | 5 |
| stroke 396 | 10 % → 31 % | 11.1 px | 0.53 | 3.28 | 6 |
| stroke 397 | 8 % → 38 % | 10.4 px | 0.49 | 4.62 | 4 |
| stroke 398 | 13 % → 38 % | 16.3 px | 0.52 | 3.01 | 10 |
| stroke 399 | 8 % → 57 % | 11.6 px | 0.50 | 7.18 | 7 |
| stroke 400 | 11 % → 41 % | 14.5 px | 0.49 | 3.85 | 7 |
| stroke 401 | 13 % → 40 % | 21.0 px | 0.51 | 3.02 | 10 |
| stroke 402 | 12 % → 46 % | 10.3 px | 0.53 | 3.84 | 6 |
| stroke 403 | 27 % → 46 % | 42.0 px | 0.52 | 1.68 | 3 |
| stroke 404 | 5 % → 43 % | 10.5 px | 0.45 | 8.09 | 2 |
| stroke 405 | 30 % → 55 % | 78.0 px | 0.50 | 1.83 | 2 |
| stroke 406 | 13 % → 55 % | 21.1 px | 0.51 | 4.04 | 8 |
| stroke 407 | 16 % → 46 % | 20.7 px | 0.45 | 2.83 | 6 |
| stroke 408 | 8 % → 56 % | 10.4 px | 0.52 | 6.94 | 6 |
| stroke 409 | 13 % → 42 % | 17.3 px | 0.50 | 3.19 | 7 |
| stroke 410 | 11 % → 39 % | 17.0 px | 0.52 | 3.40 | 6 |
| stroke 411 | 7 % → 19 % | 11.1 px | 0.48 | 2.57 | 5 |
| stroke 412 | 17 % → 51 % | 21.9 px | 0.49 | 3.05 | 7 |
| stroke 413 | 18 % → 51 % | 27.2 px | 0.52 | 2.77 | 4 |
| stroke 414 | 10 % → 60 % | 10.7 px | 0.48 | 5.98 | 4 |
| stroke 415 | 11 % → 43 % | 10.3 px | 0.50 | 4.03 | 8 |
| stroke 416 | 8 % → 30 % | 10.1 px | 0.53 | 3.53 | 8 |
| stroke 417 | 22 % → 54 % | 24.4 px | 0.49 | 2.45 | 5 |
| stroke 418 | 17 % → 51 % | 24.3 px | 0.50 | 2.98 | 5 |
| stroke 419 | 12 % → 55 % | 11.5 px | 0.53 | 4.40 | 5 |
| stroke 420 | 16 % → 45 % | 22.5 px | 0.53 | 2.72 | 2 |
| stroke 421 | 12 % → 27 % | 18.9 px | 0.44 | 2.31 | 5 |
| stroke 422 | 27 % → 55 % | 43.5 px | 0.53 | 2.02 | 8 |
| stroke 423 | 14 % → 62 % | 22.9 px | 0.51 | 4.33 | 3 |
| stroke 424 | 18 % → 56 % | 25.0 px | 0.51 | 3.08 | 4 |
| stroke 425 | 19 % → 53 % | 25.6 px | 0.51 | 2.86 | 7 |
| stroke 426 | 18 % → 62 % | 27.6 px | 0.53 | 3.54 | 3 |
| stroke 427 | 7 % → 46 % | 10.1 px | 0.51 | 6.26 | 7 |
| stroke 428 | 15 % → 54 % | 25.4 px | 0.48 | 3.62 | 4 |
| stroke 429 | 7 % → 54 % | 9.2 px | 0.49 | 7.51 | 7 |
| stroke 430 | 25 % → 50 % | 37.4 px | 0.51 | 2.03 | 10 |
| stroke 431 | 10 % → 31 % | 12.0 px | 0.51 | 3.11 | 5 |
| stroke 432 | 9 % → 39 % | 10.9 px | 0.53 | 4.40 | 2 |
| stroke 433 | 13 % → 40 % | 20.7 px | 0.50 | 3.15 | 3 |
| stroke 434 | 23 % → 49 % | 27.7 px | 0.47 | 2.13 | 3 |
| stroke 435 | 17 % → 60 % | 25.3 px | 0.50 | 3.51 | 2 |
| stroke 436 | 8 % → 28 % | 11.3 px | 0.50 | 3.68 | 9 |
| stroke 437 | 22 % → 41 % | 32.2 px | 0.51 | 1.86 | 5 |
| stroke 438 | 14 % → 48 % | 21.6 px | 0.48 | 3.34 | 4 |
| stroke 439 | 13 % → 64 % | 19.2 px | 0.53 | 5.00 | 6 |
| stroke 440 | 16 % → 31 % | 24.7 px | 0.51 | 1.94 | 6 |
| stroke 441 | 19 % → 45 % | 11.3 px | 0.51 | 2.41 | 7 |
| stroke 442 | 18 % → 61 % | 22.5 px | 0.53 | 3.49 | 11 |
| stroke 443 | 14 % → 37 % | 14.9 px | 0.52 | 2.67 | 6 |
| stroke 444 | 14 % → 38 % | 18.7 px | 0.51 | 2.74 | 5 |
| stroke 445 | 5 % → 45 % | 11.4 px | 0.52 | 8.63 | 2 |
| stroke 446 | 21 % → 46 % | 27.5 px | 0.52 | 2.17 | 6 |
| stroke 447 | 12 % → 54 % | 16.1 px | 0.52 | 4.35 | 5 |
| stroke 448 | 20 % → 30 % | 39.2 px | 0.51 | 1.52 | 3 |
| stroke 449 | 11 % → 41 % | 12.9 px | 0.53 | 3.83 | 3 |
| stroke 450 | 14 % → 47 % | 22.3 px | 0.49 | 3.33 | 6 |
| stroke 451 | 19 % → 49 % | 20.5 px | 0.49 | 2.54 | 5 |
| stroke 452 | 25 % → 40 % | 40.5 px | 0.51 | 1.57 | 4 |
| stroke 453 | 26 % → 37 % | 23.9 px | 0.53 | 1.42 | 5 |
| stroke 454 | 20 % → 54 % | 19.5 px | 0.53 | 2.77 | 10 |
| stroke 455 | 38 % → 61 % | 60.2 px | 0.53 | 1.61 | 4 |
| stroke 456 | 13 % → 49 % | 19.6 px | 0.50 | 3.61 | 10 |
| stroke 457 | 29 % → 61 % | 78.7 px | 0.53 | 2.09 | 0 |
| stroke 458 | 25 % → 58 % | 33.4 px | 0.53 | 2.29 | 5 |
| stroke 459 | 15 % → 53 % | 22.0 px | 0.52 | 3.52 | 6 |
| stroke 460 | 26 % → 64 % | 25.0 px | 0.49 | 2.47 | 5 |
| stroke 461 | 18 % → 61 % | 20.5 px | 0.49 | 3.38 | 9 |
| stroke 462 | 16 % → 44 % | 41.3 px | 0.48 | 2.72 | 0 |
| stroke 463 | 24 % → 56 % | 57.7 px | 0.49 | 2.35 | 2 |
| stroke 464 | 24 % → 51 % | 33.7 px | 0.46 | 2.18 | 2 |
| stroke 465 | 24 % → 66 % | 35.3 px | 0.53 | 2.73 | 5 |
| stroke 466 | 23 % → 51 % | 26.1 px | 0.54 | 2.21 | 2 |
| stroke 467 | 20 % → 34 % | 20.8 px | 0.52 | 1.65 | 7 |
| stroke 468 | 34 % → 39 % | 50.8 px | 0.54 | 1.13 | 3 |
| stroke 469 | 19 % → 48 % | 29.5 px | 0.49 | 2.49 | 3 |
| stroke 470 | 16 % → 39 % | 24.9 px | 0.51 | 2.49 | 4 |
| stroke 471 | 31 % → 46 % | 37.5 px | 0.52 | 1.51 | 6 |
| stroke 472 | 29 % → 65 % | 45.4 px | 0.52 | 2.21 | 6 |
| stroke 473 | 28 % → 50 % | 36.8 px | 0.51 | 1.77 | 4 |
| stroke 474 | 18 % → 43 % | 34.1 px | 0.46 | 2.43 | 1 |
| stroke 475 | 21 % → 44 % | 31.3 px | 0.52 | 2.07 | 2 |
| stroke 476 | 11 % → 23 % | 16.3 px | 0.48 | 2.03 | 3 |
| stroke 477 | 20 % → 41 % | 56.4 px | 0.51 | 2.07 | 0 |
| stroke 478 | 18 % → 39 % | 21.4 px | 0.54 | 2.17 | 7 |
| stroke 479 | 20 % → 38 % | 31.1 px | 0.53 | 1.85 | 5 |
| stroke 480 | 7 % → 21 % | 18.4 px | 0.39 | 3.00 | 0 |
| stroke 481 | 14 % → 43 % | 17.8 px | 0.48 | 3.08 | 3 |
| stroke 482 | 15 % → 50 % | 22.0 px | 0.51 | 3.27 | 7 |
| stroke 483 | 25 % → 51 % | 25.8 px | 0.51 | 2.03 | 6 |
| stroke 484 | 24 % → 46 % | 35.6 px | 0.52 | 1.97 | 18 |
| stroke 485 | 34 % → 52 % | 44.7 px | 0.54 | 1.51 | 7 |
| stroke 486 | 15 % → 47 % | 23.6 px | 0.53 | 3.16 | 8 |
| stroke 487 | 10 % → 51 % | 13.5 px | 0.51 | 5.14 | 9 |
| stroke 488 | 26 % → 47 % | 31.8 px | 0.53 | 1.78 | 5 |
| stroke 489 | 27 % → 44 % | 48.0 px | 0.47 | 1.62 | 4 |
| stroke 490 | 19 % → 56 % | 32.0 px | 0.49 | 2.95 | 2 |
| stroke 491 | 33 % → 59 % | 35.1 px | 0.53 | 1.77 | 8 |
| stroke 492 | 24 % → 59 % | 43.3 px | 0.52 | 2.47 | 3 |
| stroke 493 | 21 % → 67 % | 34.0 px | 0.52 | 3.11 | 5 |
| stroke 494 | 20 % → 43 % | 22.1 px | 0.51 | 2.15 | 10 |
| stroke 495 | 34 % → 59 % | 55.5 px | 0.50 | 1.70 | 3 |
| stroke 496 | 24 % → 44 % | 36.4 px | 0.51 | 1.84 | 7 |
| stroke 497 | 4 % → 32 % | 10.7 px | 0.46 | 7.38 | 1 |
| stroke 498 | 34 % → 44 % | 53.0 px | 0.54 | 1.30 | 4 |
| stroke 499 | 18 % → 51 % | 30.8 px | 0.51 | 2.77 | 5 |
| stroke 500 | 22 % → 49 % | 33.7 px | 0.52 | 2.20 | 7 |
| stroke 501 | 23 % → 40 % | 42.2 px | 0.53 | 1.77 | 4 |
| stroke 502 | 26 % → 51 % | 41.6 px | 0.53 | 1.95 | 3 |
| stroke 503 | 23 % → 48 % | 37.3 px | 0.51 | 2.09 | 6 |
| stroke 504 | 8 % → 40 % | 10.6 px | 0.50 | 5.22 | 2 |
| stroke 505 | 35 % → 61 % | 47.7 px | 0.52 | 1.73 | 7 |
| stroke 506 | 27 % → 64 % | 37.0 px | 0.51 | 2.40 | 6 |
| stroke 507 | 31 % → 62 % | 48.9 px | 0.53 | 2.00 | 4 |
| stroke 508 | 16 % → 47 % | 19.7 px | 0.51 | 2.95 | 4 |
| stroke 509 | 11 % → 46 % | 29.8 px | 0.48 | 4.07 | 0 |
| stroke 510 | 24 % → 58 % | 29.3 px | 0.51 | 2.39 | 4 |
| stroke 511 | 35 % → 44 % | 52.3 px | 0.50 | 1.25 | 2 |
| stroke 512 | 24 % → 50 % | 38.5 px | 0.50 | 2.12 | 3 |
| stroke 513 | 24 % → 48 % | 36.7 px | 0.52 | 2.02 | 5 |
| stroke 514 | 21 % → 51 % | 15.1 px | 0.53 | 2.48 | 7 |
| stroke 515 | 17 % → 34 % | 48.0 px | 0.50 | 1.99 | 0 |
| stroke 516 | 34 % → 53 % | 61.5 px | 0.49 | 1.55 | 2 |
| stroke 517 | 15 % → 31 % | 29.6 px | 0.48 | 2.13 | 1 |
| stroke 518 | 36 % → 47 % | 62.6 px | 0.50 | 1.32 | 3 |
| stroke 519 | 17 % → 39 % | 29.9 px | 0.52 | 2.25 | 2 |
| stroke 520 | 25 % → 45 % | 25.3 px | 0.53 | 1.83 | 8 |
| stroke 521 | 26 % → 52 % | 42.3 px | 0.52 | 1.97 | 5 |
| stroke 522 | 23 % → 50 % | 55.3 px | 0.51 | 2.19 | 1 |
| stroke 523 | 39 % → 56 % | 52.1 px | 0.49 | 1.44 | 3 |
| stroke 524 | 12 % → 32 % | 16.7 px | 0.53 | 2.65 | 9 |
| stroke 525 | 42 % → 71 % | 72.9 px | 0.53 | 1.69 | 3 |
| stroke 526 | 10 % → 30 % | 13.0 px | 0.53 | 2.96 | 3 |
| stroke 527 | 18 % → 40 % | 28.9 px | 0.49 | 2.17 | 9 |
| stroke 528 | 20 % → 48 % | 29.7 px | 0.51 | 2.48 | 7 |
| stroke 529 | 33 % → 51 % | 38.9 px | 0.53 | 1.56 | 3 |
| stroke 530 | 18 % → 40 % | 26.3 px | 0.50 | 2.15 | 10 |
| stroke 531 | 36 % → 52 % | 47.1 px | 0.47 | 1.44 | 3 |
| stroke 532 | 20 % → 40 % | 24.1 px | 0.51 | 1.97 | 7 |
| stroke 533 | 32 % → 45 % | 56.0 px | 0.52 | 1.39 | 4 |
| stroke 534 | 18 % → 32 % | 37.1 px | 0.54 | 1.80 | 3 |
| stroke 535 | 17 % → 51 % | 28.7 px | 0.52 | 3.01 | 4 |
| stroke 536 | 15 % → 29 % | 26.4 px | 0.50 | 1.90 | 3 |
| stroke 537 | 20 % → 40 % | 32.3 px | 0.52 | 2.01 | 3 |
| stroke 538 | 28 % → 68 % | 42.3 px | 0.52 | 2.42 | 7 |
| stroke 539 | 36 % → 64 % | 57.0 px | 0.51 | 1.76 | 5 |
| stroke 540 | 18 % → 62 % | 23.1 px | 0.53 | 3.39 | 4 |
| stroke 541 | 30 % → 52 % | 45.8 px | 0.53 | 1.70 | 7 |
| stroke 542 | 26 % → 56 % | 43.9 px | 0.50 | 2.12 | 5 |
| stroke 543 | 45 % → 47 % | 28.7 px | 0.53 | 1.04 | 4 |
| stroke 544 | 38 % → 62 % | 57.8 px | 0.49 | 1.63 | 4 |
| stroke 545 | 42 % → 66 % | 65.7 px | 0.52 | 1.57 | 8 |
| stroke 546 | 35 % → 42 % | 54.7 px | 0.51 | 1.21 | 5 |
| stroke 547 | 16 % → 31 % | 22.0 px | 0.52 | 1.92 | 6 |
| stroke 548 | 30 % → 59 % | 22.5 px | 0.52 | 1.96 | 4 |
| stroke 549 | 11 % → 39 % | 21.0 px | 0.50 | 3.49 | 4 |
| stroke 550 | 25 % → 41 % | 45.4 px | 0.48 | 1.60 | 5 |
| stroke 551 | 12 % → 35 % | 19.8 px | 0.50 | 2.81 | 4 |
| stroke 552 | 33 % → 49 % | 41.3 px | 0.54 | 1.46 | 8 |
| stroke 553 | 42 % → 64 % | 76.0 px | 0.54 | 1.52 | 2 |
| stroke 554 | 32 % → 49 % | 41.1 px | 0.52 | 1.54 | 5 |
| stroke 555 | 31 % → 47 % | 44.7 px | 0.50 | 1.52 | 7 |
| stroke 556 | 15 % → 34 % | 33.5 px | 0.47 | 2.32 | 1 |
| stroke 557 | 24 % → 52 % | 32.8 px | 0.52 | 2.22 | 6 |
| stroke 558 | 20 % → 25 % | 30.8 px | 0.53 | 1.22 | 1 |
| stroke 559 | 33 % → 50 % | 50.5 px | 0.52 | 1.53 | 8 |
| stroke 560 | 35 % → 67 % | 90.3 px | 0.53 | 1.91 | 2 |
| stroke 561 | 42 % → 61 % | 80.2 px | 0.53 | 1.46 | 1 |
| stroke 562 | 26 % → 46 % | 48.4 px | 0.51 | 1.76 | 3 |
| stroke 563 | 15 % → 28 % | 10.8 px | 0.53 | 1.84 | 10 |
| stroke 564 | 30 % → 57 % | 32.5 px | 0.53 | 1.87 | 6 |
| stroke 565 | 36 % → 55 % | 69.7 px | 0.53 | 1.51 | 2 |
| stroke 566 | 25 % → 57 % | 33.9 px | 0.49 | 2.25 | 4 |
| stroke 567 | 45 % → 69 % | 74.7 px | 0.53 | 1.53 | 2 |
| stroke 568 | 17 % → 37 % | 41.4 px | 0.50 | 2.16 | 2 |
| stroke 569 | 26 % → 52 % | 38.9 px | 0.49 | 1.99 | 6 |
| stroke 570 | 12 % → 30 % | 22.3 px | 0.46 | 2.39 | 2 |
| stroke 571 | 41 % → 57 % | 92.1 px | 0.52 | 1.39 | 1 |
| stroke 572 | 49 % → 58 % | 136.4 px | 0.52 | 1.20 | 0 |
| stroke 573 | 25 % → 34 % | 34.4 px | 0.50 | 1.35 | 6 |
| stroke 574 | 42 % → 57 % | 62.6 px | 0.52 | 1.37 | 5 |
| stroke 575 | 21 % → 35 % | 34.0 px | 0.49 | 1.67 | 4 |
| stroke 576 | 39 % → 54 % | 71.4 px | 0.52 | 1.39 | 2 |
| stroke 577 | 38 % → 64 % | 107.7 px | 0.52 | 1.66 | 1 |
| stroke 578 | 35 % → 42 % | 59.8 px | 0.52 | 1.21 | 2 |
| stroke 579 | 48 % → 68 % | 78.9 px | 0.51 | 1.41 | 4 |
| stroke 580 | 26 % → 42 % | 31.2 px | 0.53 | 1.63 | 5 |
| stroke 581 | 38 % → 59 % | 38.7 px | 0.48 | 1.58 | 6 |
| stroke 582 | 35 % → 54 % | 44.4 px | 0.53 | 1.55 | 2 |
| stroke 583 | 43 % → 58 % | 60.2 px | 0.50 | 1.34 | 4 |
| stroke 584 | 15 % → 36 % | 21.0 px | 0.50 | 2.37 | 7 |
| stroke 585 | 33 % → 53 % | 90.9 px | 0.48 | 1.62 | 2 |
| stroke 586 | 19 % → 39 % | 41.2 px | 0.52 | 2.06 | 1 |
| stroke 587 | 29 % → 45 % | 52.8 px | 0.49 | 1.55 | 1 |
| stroke 588 | 32 % → 59 % | 57.4 px | 0.52 | 1.83 | 1 |
| stroke 589 | 21 % → 48 % | 49.7 px | 0.48 | 2.27 | 1 |
| stroke 590 | 9 % → 29 % | 17.3 px | 0.48 | 3.42 | 3 |
| stroke 591 | 22 % → 27 % | 61.3 px | 0.49 | 1.23 | 1 |
| stroke 592 | 20 % → 30 % | 50.7 px | 0.52 | 1.50 | 1 |
| stroke 593 | 53 % → 58 % | 91.7 px | 0.54 | 1.11 | 1 |
| stroke 594 | 36 % → 49 % | 55.5 px | 0.49 | 1.35 | 4 |
| stroke 595 | 27 % → 47 % | 36.6 px | 0.48 | 1.78 | 14 |
| stroke 596 | 18 % → 56 % | 19.4 px | 0.50 | 3.06 | 7 |
| stroke 597 | 51 % → 51 % | 68.7 px | 0.53 | 1.01 | 1 |
| stroke 598 | 36 % → 45 % | 69.6 px | 0.54 | 1.26 | 1 |
| stroke 599 | 44 % → 53 % | 46.2 px | 0.51 | 1.22 | 11 |
| stroke 600 | 29 % → 37 % | 42.4 px | 0.53 | 1.30 | 5 |
| stroke 601 | 30 % → 50 % | 73.6 px | 0.50 | 1.66 | 2 |
| stroke 602 | 52 % → 61 % | 74.5 px | 0.54 | 1.17 | 6 |
| stroke 603 | 35 % → 51 % | 46.7 px | 0.50 | 1.48 | 6 |
| stroke 604 | 42 % → 51 % | 76.1 px | 0.44 | 1.21 | 4 |
| stroke 605 | 39 % → 52 % | 72.4 px | 0.47 | 1.31 | 3 |
| stroke 606 | 32 % → 40 % | 40.2 px | 0.52 | 1.24 | 5 |
| stroke 607 | 24 % → 38 % | 63.6 px | 0.51 | 1.58 | 2 |
| stroke 608 | 23 % → 57 % | 49.2 px | 0.50 | 2.53 | 2 |
| stroke 609 | 46 % → 65 % | 85.5 px | 0.53 | 1.42 | 3 |
| stroke 610 | 61 % → 62 % | 115.8 px | 0.53 | 1.02 | 1 |
| stroke 611 | 28 % → 41 % | 56.6 px | 0.48 | 1.47 | 3 |
| stroke 612 | 51 % → 59 % | 101.1 px | 0.52 | 1.15 | 1 |
| stroke 613 | 50 % → 55 % | 123.0 px | 0.49 | 1.11 | 1 |
| stroke 614 | 29 % → 41 % | 30.1 px | 0.53 | 1.38 | 15 |
| stroke 615 | 41 % → 55 % | 65.3 px | 0.50 | 1.35 | 9 |
| stroke 616 | 54 % → 65 % | 105.0 px | 0.53 | 1.19 | 7 |
| stroke 617 | 48 % → 53 % | 60.7 px | 0.52 | 1.10 | 4 |
| stroke 618 | 48 % → 61 % | 95.3 px | 0.54 | 1.26 | 4 |
| stroke 619 | 45 % → 61 % | 47.6 px | 0.53 | 1.36 | 10 |
| stroke 620 | 37 % → 46 % | 53.5 px | 0.47 | 1.24 | 11 |
| stroke 621 | 38 % → 59 % | 49.4 px | 0.53 | 1.55 | 6 |
| stroke 622 | 42 % → 54 % | 47.5 px | 0.52 | 1.28 | 5 |
| stroke 623 | 23 % → 31 % | 47.1 px | 0.49 | 1.33 | 3 |
| stroke 624 | 33 % → 40 % | 72.6 px | 0.48 | 1.22 | 6 |
| stroke 625 | 56 % → 68 % | 60.1 px | 0.48 | 1.20 | 6 |
| stroke 626 | 45 % → 58 % | 75.3 px | 0.49 | 1.27 | 7 |
| stroke 627 | 42 % → 62 % | 108.6 px | 0.48 | 1.46 | 2 |
| stroke 628 | 32 % → 52 % | 52.6 px | 0.50 | 1.61 | 2 |
| stroke 629 | 28 % → 55 % | 36.9 px | 0.48 | 1.94 | 3 |
| stroke 630 | 34 % → 42 % | 45.8 px | 0.52 | 1.24 | 9 |
| stroke 631 | 27 % → 47 % | 49.2 px | 0.53 | 1.76 | 2 |
| stroke 632 | 10 % → 30 % | 16.4 px | 0.47 | 3.08 | 4 |
| stroke 633 | 25 % → 41 % | 44.3 px | 0.46 | 1.60 | 2 |
| stroke 634 | 40 % → 47 % | 57.7 px | 0.50 | 1.17 | 3 |
| stroke 635 | 33 % → 43 % | 43.5 px | 0.53 | 1.32 | 4 |
| stroke 636 | 30 % → 40 % | 42.2 px | 0.52 | 1.35 | 3 |
| stroke 637 | 21 % → 38 % | 33.9 px | 0.48 | 1.82 | 13 |
| stroke 638 | 41 % → 53 % | 83.4 px | 0.53 | 1.30 | 1 |
| stroke 639 | 34 % → 44 % | 46.4 px | 0.49 | 1.31 | 2 |
| stroke 640 | 50 % → 57 % | 68.1 px | 0.50 | 1.13 | 5 |
| stroke 641 | 59 % → 64 % | 94.9 px | 0.53 | 1.09 | 2 |
| stroke 642 | 34 % → 36 % | 50.6 px | 0.51 | 1.05 | 7 |
| stroke 643 | 45 % → 50 % | 127.7 px | 0.54 | 1.12 | 2 |
| stroke 644 | 45 % → 57 % | 85.5 px | 0.50 | 1.28 | 1 |
| stroke 645 | 28 % → 46 % | 25.7 px | 0.52 | 1.66 | 4 |
| stroke 646 | 35 % → 62 % | 69.6 px | 0.51 | 1.79 | 0 |
| stroke 647 | 38 % → 43 % | 60.7 px | 0.51 | 1.15 | 3 |
| stroke 648 | 43 % → 50 % | 100.8 px | 0.51 | 1.18 | 1 |
| stroke 649 | 44 % → 64 % | 65.4 px | 0.52 | 1.47 | 9 |
| stroke 650 | 27 % → 36 % | 44.1 px | 0.52 | 1.35 | 8 |
| stroke 651 | 25 % → 35 % | 43.4 px | 0.51 | 1.38 | 3 |
| stroke 652 | 37 % → 37 % | 78.7 px | 0.52 | 1.01 | 2 |
| stroke 653 | 19 % → 35 % | 35.9 px | 0.48 | 1.87 | 3 |
| stroke 654 | 44 % → 59 % | 85.5 px | 0.52 | 1.32 | 1 |
| stroke 655 | 51 % → 55 % | 65.7 px | 0.53 | 1.07 | 5 |
| stroke 656 | 39 % → 47 % | 87.0 px | 0.48 | 1.18 | 1 |
| stroke 657 | 33 % → 38 % | 63.0 px | 0.44 | 1.17 | 2 |
| stroke 658 | 51 % → 65 % | 96.5 px | 0.52 | 1.27 | 1 |
| stroke 659 | 30 % → 31 % | 50.0 px | 0.53 | 1.03 | 0 |
| stroke 660 | 42 % → 53 % | 48.5 px | 0.51 | 1.25 | 10 |
| stroke 661 | 33 % → 53 % | 79.0 px | 0.49 | 1.63 | 1 |
| stroke 662 | 46 % → 57 % | 85.2 px | 0.52 | 1.23 | 2 |
| stroke 663 | 29 % → 42 % | 62.2 px | 0.50 | 1.44 | 1 |
| stroke 664 | 23 % → 29 % | 32.8 px | 0.52 | 1.24 | 7 |
| stroke 665 | 33 % → 48 % | 52.1 px | 0.53 | 1.43 | 11 |
| stroke 666 | 18 % → 33 % | 27.1 px | 0.49 | 1.78 | 7 |
| stroke 667 | 27 % → 40 % | 68.7 px | 0.47 | 1.50 | 0 |
| stroke 668 | 45 % → 51 % | 68.6 px | 0.50 | 1.15 | 2 |
| stroke 669 | 43 % → 60 % | 77.8 px | 0.49 | 1.41 | 6 |
| stroke 670 | 45 % → 49 % | 67.9 px | 0.50 | 1.09 | 4 |
| stroke 671 | 41 % → 42 % | 51.3 px | 0.52 | 1.02 | 3 |
| stroke 672 | 10 % → 17 % | 27.0 px | 0.46 | 1.72 | 1 |
| stroke 673 | 40 % → 53 % | 80.3 px | 0.50 | 1.32 | 1 |
| stroke 674 | 31 % → 39 % | 49.5 px | 0.52 | 1.29 | 2 |
| stroke 675 | 24 % → 34 % | 37.9 px | 0.49 | 1.41 | 3 |
| stroke 676 | 45 % → 62 % | 121.2 px | 0.53 | 1.37 | 0 |
| stroke 677 | 39 % → 48 % | 80.5 px | 0.52 | 1.25 | 4 |
| stroke 678 | 20 % → 31 % | 32.7 px | 0.51 | 1.59 | 4 |
| stroke 679 | 36 % → 42 % | 101.2 px | 0.44 | 1.15 | 1 |
| stroke 680 | 23 % → 25 % | 37.1 px | 0.49 | 1.09 | 3 |
| stroke 681 | 37 % → 53 % | 66.3 px | 0.53 | 1.43 | 5 |
| stroke 682 | 43 % → 43 % | 61.3 px | 0.53 | 1.00 | 2 |
| stroke 683 | 16 % → 21 % | 37.7 px | 0.49 | 1.28 | 1 |
| stroke 684 | 31 % → 40 % | 52.3 px | 0.49 | 1.30 | 1 |
| stroke 685 | 11 % → 30 % | 22.0 px | 0.49 | 2.63 | 1 |
| stroke 686 | 37 % → 48 % | 66.1 px | 0.53 | 1.30 | 6 |
| stroke 687 | 49 % → 50 % | 104.4 px | 0.50 | 1.02 | 2 |
| stroke 688 | 29 % → 29 % | 79.1 px | 0.43 | 1.02 | 0 |
| stroke 689 | 42 % → 64 % | 64.4 px | 0.52 | 1.52 | 6 |
| stroke 690 | 51 % → 61 % | 74.9 px | 0.53 | 1.18 | 1 |
| stroke 691 | 57 % → 61 % | 75.6 px | 0.50 | 1.08 | 4 |
| stroke 692 | 26 % → 33 % | 69.5 px | 0.51 | 1.27 | 1 |
| stroke 693 | 61 % → 68 % | 164.1 px | 0.54 | 1.12 | 1 |
| stroke 694 | 35 % → 47 % | 63.2 px | 0.49 | 1.35 | 1 |
| stroke 695 | 39 % → 62 % | 63.9 px | 0.52 | 1.59 | 3 |
| stroke 696 | 30 % → 39 % | 53.1 px | 0.54 | 1.28 | 7 |
| stroke 697 | 43 % → 53 % | 57.3 px | 0.48 | 1.22 | 5 |
| stroke 698 | 55 % → 72 % | 93.9 px | 0.52 | 1.32 | 9 |
| stroke 699 | 49 % → 57 % | 107.8 px | 0.51 | 1.16 | 1 |
| stroke 700 | 31 % → 36 % | 68.4 px | 0.53 | 1.15 | 1 |
| stroke 701 | 37 % → 43 % | 70.8 px | 0.50 | 1.16 | 2 |
| stroke 702 | 50 % → 66 % | 79.8 px | 0.53 | 1.32 | 6 |
| stroke 703 | 51 % → 54 % | 144.1 px | 0.51 | 1.05 | 0 |
| stroke 704 | 26 % → 35 % | 35.8 px | 0.51 | 1.31 | 2 |
| stroke 705 | 31 % → 34 % | 48.3 px | 0.49 | 1.09 | 8 |
| stroke 706 | 26 % → 42 % | 71.4 px | 0.49 | 1.60 | 0 |
| stroke 707 | 46 % → 52 % | 72.6 px | 0.53 | 1.13 | 3 |
| stroke 708 | 46 % → 52 % | 53.5 px | 0.53 | 1.13 | 5 |
| stroke 709 | 33 % → 41 % | 46.6 px | 0.52 | 1.23 | 8 |
| stroke 710 | 50 % → 53 % | 88.8 px | 0.52 | 1.06 | 2 |
| stroke 711 | 34 % → 44 % | 58.1 px | 0.53 | 1.29 | 4 |
| stroke 712 | 26 % → 45 % | 62.2 px | 0.51 | 1.74 | 2 |
| stroke 713 | 34 % → 51 % | 53.3 px | 0.54 | 1.49 | 1 |
| stroke 714 | 45 % → 52 % | 125.1 px | 0.52 | 1.17 | 0 |
| stroke 715 | 61 % → 63 % | 128.5 px | 0.53 | 1.02 | 1 |
| stroke 716 | 16 % → 24 % | 40.1 px | 0.52 | 1.44 | 1 |
| stroke 717 | 28 % → 33 % | 53.0 px | 0.53 | 1.16 | 1 |
| stroke 718 | 53 % → 67 % | 92.3 px | 0.53 | 1.27 | 4 |
| stroke 719 | 30 % → 37 % | 67.1 px | 0.50 | 1.21 | 2 |
| stroke 720 | 52 % → 52 % | 144.3 px | 0.51 | 1.00 | 2 |
| stroke 721 | 46 % → 57 % | 88.0 px | 0.51 | 1.22 | 1 |
| stroke 722 | 44 % → 58 % | 81.8 px | 0.52 | 1.31 | 2 |
| stroke 723 | 25 % → 33 % | 47.0 px | 0.48 | 1.29 | 5 |
| stroke 724 | 39 % → 39 % | 85.4 px | 0.53 | 1.00 | 3 |
| stroke 725 | 31 % → 35 % | 49.5 px | 0.50 | 1.14 | 2 |
| stroke 726 | 66 % → 72 % | 128.8 px | 0.52 | 1.08 | 5 |
| stroke 727 | 24 % → 35 % | 41.2 px | 0.51 | 1.47 | 2 |
| stroke 728 | 42 % → 51 % | 93.2 px | 0.53 | 1.22 | 9 |
| stroke 729 | 40 % → 45 % | 70.4 px | 0.52 | 1.12 | 4 |
| stroke 730 | 52 % → 62 % | 95.2 px | 0.54 | 1.19 | 2 |
| stroke 731 | 43 % → 56 % | 98.4 px | 0.52 | 1.31 | 1 |
| stroke 732 | 28 % → 29 % | 80.1 px | 0.53 | 1.03 | 1 |
| stroke 733 | 56 % → 69 % | 113.9 px | 0.53 | 1.24 | 2 |
| stroke 734 | 46 % → 46 % | 107.9 px | 0.53 | 1.00 | 1 |
| stroke 735 | 43 % → 54 % | 87.4 px | 0.54 | 1.26 | 3 |
| stroke 736 | 27 % → 27 % | 73.8 px | 0.50 | 1.00 | 1 |
| stroke 737 | 37 % → 48 % | 41.6 px | 0.47 | 1.29 | 2 |
| stroke 738 | 49 % → 54 % | 75.9 px | 0.48 | 1.09 | 2 |
| stroke 739 | 35 % → 35 % | 52.8 px | 0.52 | 1.02 | 2 |
| stroke 740 | 31 % → 33 % | 47.5 px | 0.51 | 1.08 | 6 |
| stroke 741 | 26 % → 39 % | 46.1 px | 0.48 | 1.53 | 4 |
| stroke 742 | 34 % → 47 % | 87.4 px | 0.49 | 1.37 | 0 |
| stroke 743 | 35 % → 49 % | 97.7 px | 0.49 | 1.38 | 1 |
| stroke 744 | 26 % → 31 % | 58.4 px | 0.47 | 1.18 | 4 |
| stroke 745 | 33 % → 33 % | 48.1 px | 0.51 | 1.00 | 1 |
| stroke 746 | 38 % → 48 % | 99.1 px | 0.47 | 1.27 | 3 |
| stroke 747 | 54 % → 56 % | 87.7 px | 0.53 | 1.03 | 3 |
| stroke 748 | 21 % → 22 % | 45.2 px | 0.42 | 1.06 | 1 |
| stroke 749 | 37 % → 46 % | 57.8 px | 0.51 | 1.26 | 7 |
| stroke 750 | 31 % → 36 % | 59.4 px | 0.51 | 1.14 | 2 |
| stroke 751 | 53 % → 57 % | 78.3 px | 0.53 | 1.08 | 3 |
| stroke 752 | 39 % → 39 % | 77.2 px | 0.51 | 1.00 | 2 |
| stroke 753 | 37 % → 42 % | 81.4 px | 0.52 | 1.12 | 1 |
| stroke 754 | 43 % → 43 % | 112.2 px | 0.52 | 1.00 | 0 |
| stroke 755 | 31 % → 40 % | 50.7 px | 0.49 | 1.30 | 4 |
| stroke 756 | 54 % → 64 % | 75.0 px | 0.53 | 1.19 | 5 |
| stroke 757 | 47 % → 56 % | 89.9 px | 0.48 | 1.20 | 3 |
| stroke 758 | 55 % → 63 % | 92.9 px | 0.53 | 1.15 | 4 |
| stroke 759 | 17 % → 23 % | 42.4 px | 0.51 | 1.32 | 2 |
| stroke 760 | 54 % → 57 % | 148.1 px | 0.52 | 1.07 | 1 |
| stroke 761 | 30 % → 30 % | 72.2 px | 0.49 | 1.00 | 1 |
| stroke 762 | 40 % → 46 % | 89.5 px | 0.52 | 1.16 | 1 |
| stroke 763 | 32 % → 37 % | 58.9 px | 0.50 | 1.16 | 4 |
| stroke 764 | 50 % → 50 % | 74.7 px | 0.50 | 1.00 | 6 |
| stroke 765 | 39 % → 43 % | 78.8 px | 0.52 | 1.09 | 1 |
| stroke 766 | 58 % → 64 % | 139.3 px | 0.49 | 1.10 | 2 |
| stroke 767 | 58 % → 62 % | 118.0 px | 0.49 | 1.06 | 3 |
| stroke 768 | 64 % → 69 % | 100.2 px | 0.52 | 1.08 | 5 |
| stroke 769 | 44 % → 44 % | 78.4 px | 0.52 | 1.00 | 1 |
| stroke 770 | 45 % → 53 % | 44.2 px | 0.52 | 1.18 | 7 |
| stroke 771 | 38 % → 46 % | 83.3 px | 0.48 | 1.21 | 4 |
| stroke 772 | 30 % → 35 % | 86.8 px | 0.48 | 1.15 | 0 |
| stroke 773 | 57 % → 57 % | 113.7 px | 0.51 | 1.00 | 2 |
| stroke 774 | 18 % → 27 % | 47.2 px | 0.48 | 1.45 | 1 |
| stroke 775 | 26 % → 30 % | 51.9 px | 0.49 | 1.18 | 1 |
| stroke 776 | 45 % → 47 % | 115.1 px | 0.50 | 1.05 | 1 |
| stroke 777 | 49 % → 49 % | 114.8 px | 0.48 | 1.00 | 2 |
| stroke 778 | 50 % → 54 % | 135.5 px | 0.49 | 1.09 | 0 |
| stroke 779 | 36 % → 44 % | 80.5 px | 0.53 | 1.21 | 3 |
| stroke 780 | 46 % → 49 % | 87.7 px | 0.50 | 1.06 | 2 |
| stroke 781 | 49 % → 59 % | 133.7 px | 0.46 | 1.21 | 0 |
| stroke 782 | 38 % → 41 % | 108.1 px | 0.50 | 1.08 | 0 |
| stroke 783 | 72 % → 72 % | 198.3 px | 0.53 | 1.00 | 0 |
| stroke 784 | 40 % → 52 % | 110.2 px | 0.50 | 1.31 | 4 |
| stroke 785 | 39 % → 40 % | 83.2 px | 0.50 | 1.04 | 2 |
| stroke 786 | 55 % → 57 % | 129.5 px | 0.53 | 1.03 | 1 |
| stroke 787 | 44 % → 44 % | 79.9 px | 0.49 | 1.00 | 3 |
| stroke 788 | 59 % → 67 % | 132.1 px | 0.54 | 1.13 | 1 |
| stroke 789 | 53 % → 56 % | 130.3 px | 0.53 | 1.05 | 2 |
| stroke 790 | 30 % → 33 % | 56.1 px | 0.51 | 1.10 | 2 |
| stroke 791 | 61 % → 61 % | 171.0 px | 0.51 | 1.00 | 1 |
| stroke 792 | 60 % → 63 % | 110.9 px | 0.51 | 1.05 | 1 |
| stroke 793 | 7 % → 7 % | 13.4 px | 0.51 | 1.09 | 2 |
| stroke 794 | 30 % → 35 % | 83.8 px | 0.49 | 1.17 | 1 |
| stroke 795 | 58 % → 58 % | 146.6 px | 0.48 | 1.00 | 0 |
| stroke 796 | 67 % → 73 % | 146.9 px | 0.52 | 1.09 | 1 |
| stroke 797 | 33 % → 33 % | 55.3 px | 0.48 | 1.00 | 7 |
| stroke 798 | 23 % → 28 % | 64.2 px | 0.53 | 1.22 | 4 |
| stroke 799 | 55 % → 55 % | 121.2 px | 0.50 | 1.00 | 3 |
| stroke 800 | 51 % → 58 % | 99.5 px | 0.50 | 1.14 | 1 |
| stroke 801 | 53 % → 62 % | 109.3 px | 0.53 | 1.16 | 4 |
| stroke 802 | 57 % → 59 % | 125.8 px | 0.50 | 1.03 | 2 |
| stroke 803 | 30 % → 30 % | 63.8 px | 0.51 | 1.01 | 1 |
| stroke 804 | 21 % → 21 % | 40.3 px | 0.51 | 1.00 | 6 |
| stroke 805 | 48 % → 48 % | 104.2 px | 0.53 | 1.00 | 2 |
| stroke 806 | 38 % → 41 % | 67.3 px | 0.51 | 1.09 | 2 |
| stroke 807 | 49 % → 53 % | 125.3 px | 0.50 | 1.09 | 0 |
| stroke 808 | 59 % → 59 % | 112.6 px | 0.52 | 1.00 | 3 |
| stroke 809 | 42 % → 48 % | 78.3 px | 0.50 | 1.14 | 5 |
| stroke 810 | 52 % → 60 % | 124.4 px | 0.51 | 1.16 | 1 |
| stroke 811 | 18 % → 19 % | 49.1 px | 0.54 | 1.08 | 0 |
| stroke 812 | 16 % → 18 % | 40.6 px | 0.43 | 1.12 | 5 |
| stroke 813 | 50 % → 55 % | 140.9 px | 0.50 | 1.10 | 2 |
| stroke 814 | 51 % → 51 % | 102.9 px | 0.48 | 1.00 | 1 |
| stroke 815 | 48 % → 48 % | 89.6 px | 0.51 | 1.00 | 1 |
| stroke 816 | 35 % → 38 % | 94.4 px | 0.47 | 1.07 | 1 |
| stroke 817 | 61 % → 61 % | 126.6 px | 0.54 | 1.00 | 1 |
| stroke 818 | 41 % → 48 % | 91.8 px | 0.52 | 1.17 | 4 |
| stroke 819 | 55 % → 60 % | 117.2 px | 0.51 | 1.08 | 1 |
| stroke 820 | 65 % → 66 % | 141.0 px | 0.52 | 1.01 | 2 |
| stroke 821 | 49 % → 50 % | 139.7 px | 0.52 | 1.03 | 0 |
| stroke 822 | 46 % → 51 % | 94.2 px | 0.49 | 1.11 | 1 |
| stroke 823 | 36 % → 40 % | 43.6 px | 0.52 | 1.11 | 2 |
| stroke 824 | 36 % → 36 % | 73.8 px | 0.51 | 1.00 | 3 |
| stroke 825 | 25 % → 30 % | 71.2 px | 0.50 | 1.17 | 2 |
| stroke 826 | 42 % → 42 % | 104.0 px | 0.49 | 1.00 | 1 |
| stroke 827 | 50 % → 50 % | 68.7 px | 0.48 | 1.00 | 1 |
| stroke 828 | 37 % → 43 % | 69.5 px | 0.50 | 1.17 | 3 |
| stroke 829 | 19 % → 19 % | 56.2 px | 0.54 | 1.00 | 0 |
| stroke 830 | 38 % → 43 % | 94.4 px | 0.54 | 1.12 | 1 |
| stroke 831 | 28 % → 28 % | 55.2 px | 0.51 | 1.00 | 1 |
| stroke 832 | 29 % → 29 % | 82.0 px | 0.48 | 1.00 | 1 |
| stroke 833 | 34 % → 34 % | 94.4 px | 0.51 | 1.00 | 1 |
| stroke 834 | 48 % → 48 % | 112.4 px | 0.54 | 1.00 | 2 |
| stroke 835 | 45 % → 45 % | 111.0 px | 0.45 | 1.00 | 1 |
| stroke 836 | 69 % → 72 % | 109.6 px | 0.53 | 1.05 | 2 |
| stroke 837 | 34 % → 34 % | 76.9 px | 0.47 | 1.00 | 2 |
| stroke 838 | 41 % → 41 % | 75.3 px | 0.53 | 1.00 | 2 |
| stroke 839 | 33 % → 33 % | 88.2 px | 0.47 | 1.00 | 2 |
| stroke 840 | 32 % → 32 % | 79.2 px | 0.46 | 1.00 | 2 |
| stroke 841 | 60 % → 60 % | 96.5 px | 0.53 | 1.00 | 2 |
| stroke 842 | 45 % → 45 % | 102.1 px | 0.42 | 1.00 | 3 |
| stroke 843 | 61 % → 66 % | 95.9 px | 0.48 | 1.08 | 5 |
| stroke 844 | 60 % → 60 % | 114.9 px | 0.52 | 1.00 | 2 |
| stroke 845 | 53 % → 53 % | 108.7 px | 0.47 | 1.00 | 2 |
| stroke 846 | 44 % → 44 % | 82.6 px | 0.52 | 1.00 | 3 |
| stroke 847 | 61 % → 61 % | 163.5 px | 0.49 | 1.00 | 0 |
| stroke 848 | 59 % → 61 % | 168.8 px | 0.54 | 1.03 | 0 |
| stroke 849 | 71 % → 71 % | 195.6 px | 0.53 | 1.00 | 1 |
| stroke 850 | 51 % → 51 % | 39.6 px | 0.53 | 1.00 | 2 |
| stroke 851 | 34 % → 34 % | 94.4 px | 0.53 | 1.00 | 2 |
| stroke 852 | 45 % → 45 % | 82.5 px | 0.54 | 1.00 | 4 |
| stroke 853 | 67 % → 67 % | 171.9 px | 0.53 | 1.00 | 0 |
| stroke 854 | 56 % → 56 % | 128.7 px | 0.52 | 1.00 | 4 |
| stroke 855 | 67 % → 67 % | 188.0 px | 0.53 | 1.00 | 1 |
| stroke 856 | 54 % → 54 % | 146.3 px | 0.50 | 1.00 | 1 |
| stroke 857 | 35 % → 35 % | 47.7 px | 0.44 | 1.00 | 3 |
| stroke 858 | 20 % → 20 % | 42.9 px | 0.52 | 1.00 | 1 |
| stroke 859 | 38 % → 38 % | 102.2 px | 0.53 | 1.00 | 0 |
| stroke 860 | 57 % → 57 % | 132.6 px | 0.52 | 1.00 | 2 |
| stroke 861 | 44 % → 46 % | 107.1 px | 0.51 | 1.05 | 2 |
| stroke 862 | 48 % → 53 % | 75.1 px | 0.49 | 1.12 | 1 |
| stroke 863 | 49 % → 49 % | 95.1 px | 0.48 | 1.00 | 3 |
| stroke 864 | 44 % → 44 % | 102.9 px | 0.50 | 1.00 | 2 |
| stroke 865 | 56 % → 59 % | 104.6 px | 0.53 | 1.05 | 5 |
| stroke 866 | 45 % → 45 % | 91.4 px | 0.50 | 1.00 | 1 |
| stroke 867 | 37 % → 37 % | 93.6 px | 0.50 | 1.00 | 1 |
| stroke 868 | 60 % → 60 % | 153.2 px | 0.53 | 1.00 | 1 |
| stroke 869 | 24 % → 24 % | 66.0 px | 0.50 | 1.00 | 1 |
| stroke 870 | 58 % → 58 % | 166.0 px | 0.54 | 1.00 | 1 |
| stroke 871 | 50 % → 50 % | 113.2 px | 0.51 | 1.00 | 1 |
| stroke 872 | 67 % → 67 % | 148.2 px | 0.53 | 1.00 | 1 |
| stroke 873 | 21 % → 21 % | 59.0 px | 0.50 | 1.00 | 1 |
| stroke 874 | 33 % → 40 % | 79.6 px | 0.50 | 1.22 | 1 |
| stroke 875 | 67 % → 67 % | 164.8 px | 0.51 | 1.00 | 1 |
| stroke 876 | 42 % → 42 % | 88.2 px | 0.54 | 1.00 | 0 |
| stroke 877 | 44 % → 44 % | 89.0 px | 0.50 | 1.00 | 1 |
| stroke 878 | 53 % → 53 % | 70.9 px | 0.51 | 1.00 | 2 |
| stroke 879 | 33 % → 33 % | 63.6 px | 0.52 | 1.00 | 3 |
| stroke 880 | 33 % → 33 % | 71.7 px | 0.51 | 1.00 | 1 |
| stroke 881 | 76 % → 76 % | 184.1 px | 0.53 | 1.00 | 2 |
| stroke 882 | 46 % → 46 % | 99.9 px | 0.52 | 1.00 | 4 |
| stroke 883 | 11 % → 29 % | 15.0 px | 0.51 | 2.70 | 10 |
| stroke 884 | 12 % → 22 % | 29.9 px | 0.50 | 1.80 | 1 |
| stroke 885 | 18 % → 32 % | 24.1 px | 0.51 | 1.74 | 11 |
| stroke 886 | 25 % → 37 % | 38.0 px | 0.51 | 1.48 | 3 |
| stroke 887 | 16 % → 25 % | 33.2 px | 0.53 | 1.61 | 2 |
| stroke 888 | 32 % → 34 % | 72.2 px | 0.50 | 1.07 | 4 |
| stroke 889 | 15 % → 19 % | 35.2 px | 0.54 | 1.27 | 2 |
| stroke 890 | 32 % → 32 % | 88.3 px | 0.54 | 1.00 | 0 |
| stroke 891 | 8 % → 11 % | 16.9 px | 0.54 | 1.40 | 3 |
| stroke 892 | 6 % → 32 % | 10.7 px | 0.50 | 5.08 | 4 |
| stroke 893 | 9 % → 22 % | 10.5 px | 0.52 | 2.48 | 7 |
| stroke 894 | 11 % → 42 % | 14.5 px | 0.53 | 3.97 | 31 |
| stroke 895 | 15 % → 35 % | 17.5 px | 0.50 | 2.40 | 14 |
| stroke 896 | 13 % → 27 % | 20.4 px | 0.53 | 2.09 | 11 |
| stroke 897 | 11 % → 48 % | 14.8 px | 0.53 | 4.51 | 10 |
| stroke 898 | 15 % → 30 % | 20.8 px | 0.50 | 2.07 | 7 |
| stroke 899 | 16 % → 50 % | 23.1 px | 0.53 | 3.22 | 14 |
| stroke 900 | 6 % → 21 % | 12.8 px | 0.48 | 3.53 | 5 |
| stroke 901 | 17 % → 39 % | 48.1 px | 0.51 | 2.21 | 2 |
| stroke 902 | 19 % → 39 % | 18.2 px | 0.53 | 2.10 | 8 |
| stroke 903 | 19 % → 49 % | 21.6 px | 0.54 | 2.55 | 5 |
| stroke 904 | 13 % → 19 % | 30.6 px | 0.49 | 1.41 | 1 |
| stroke 905 | 18 % → 21 % | 26.3 px | 0.53 | 1.18 | 7 |
| stroke 906 | 12 % → 38 % | 17.9 px | 0.54 | 3.09 | 6 |
| stroke 907 | 17 % → 41 % | 15.4 px | 0.54 | 2.34 | 12 |
| stroke 908 | 29 % → 42 % | 39.5 px | 0.53 | 1.46 | 4 |
| stroke 909 | 22 % → 36 % | 31.9 px | 0.53 | 1.61 | 3 |
| stroke 910 | 20 % → 29 % | 32.5 px | 0.50 | 1.49 | 16 |
| stroke 911 | 39 % → 48 % | 51.2 px | 0.54 | 1.23 | 5 |
| stroke 912 | 21 % → 36 % | 27.4 px | 0.54 | 1.72 | 3 |
| stroke 913 | 25 % → 31 % | 63.1 px | 0.51 | 1.24 | 1 |
| stroke 914 | 36 % → 54 % | 40.4 px | 0.53 | 1.50 | 2 |
| stroke 915 | 25 % → 32 % | 39.7 px | 0.53 | 1.29 | 5 |
| stroke 916 | 36 % → 39 % | 70.0 px | 0.52 | 1.08 | 2 |
| stroke 917 | 42 % → 53 % | 61.8 px | 0.54 | 1.29 | 1 |
| stroke 918 | 29 % → 41 % | 44.0 px | 0.52 | 1.41 | 1 |
| stroke 919 | 38 % → 48 % | 68.8 px | 0.53 | 1.26 | 5 |
| stroke 920 | 48 % → 56 % | 120.3 px | 0.53 | 1.19 | 0 |
| stroke 921 | 40 % → 49 % | 59.0 px | 0.54 | 1.21 | 7 |
| stroke 922 | 35 % → 40 % | 86.5 px | 0.51 | 1.15 | 3 |
| stroke 923 | 41 % → 41 % | 107.6 px | 0.52 | 1.00 | 1 |
| stroke 924 | 19 % → 19 % | 35.8 px | 0.48 | 1.00 | 1 |
| stroke 925 | 51 % → 53 % | 110.6 px | 0.54 | 1.05 | 4 |
| stroke 926 | 30 % → 30 % | 65.5 px | 0.50 | 1.00 | 1 |
| stroke 927 | 15 % → 15 % | 34.9 px | 0.52 | 1.00 | 1 |
| stroke 928 | 41 % → 43 % | 58.5 px | 0.54 | 1.03 | 1 |
| stroke 929 | 26 % → 26 % | 62.6 px | 0.52 | 1.00 | 5 |
| stroke 930 | 46 % → 46 % | 128.0 px | 0.53 | 1.00 | 1 |
| stroke 931 | 30 % → 30 % | 70.1 px | 0.50 | 1.00 | 2 |
| stroke 932 | 53 % → 58 % | 136.3 px | 0.54 | 1.08 | 0 |
| stroke 933 | 64 % → 64 % | 155.0 px | 0.54 | 1.00 | 1 |
| stroke 934 | 9 % → 16 % | 12.0 px | 0.48 | 1.79 | 2 |
| stroke 935 | 13 % → 21 % | 21.3 px | 0.52 | 1.63 | 7 |
| stroke 936 | 26 % → 26 % | 33.3 px | 0.50 | 1.02 | 5 |
| stroke 937 | 27 % → 27 % | 75.5 px | 0.52 | 1.00 | 0 |
| stroke 938 | 5 % → 15 % | 13.8 px | 0.48 | 2.80 | 2 |
| stroke 939 | 10 % → 17 % | 18.9 px | 0.50 | 1.78 | 3 |
| stroke 940 | 15 % → 20 % | 42.1 px | 0.51 | 1.30 | 1 |
| stroke 941 | 23 % → 23 % | 59.2 px | 0.50 | 1.00 | 1 |
| stroke 942 | 9 % → 17 % | 12.4 px | 0.50 | 1.86 | 12 |
| stroke 943 | 13 % → 18 % | 26.8 px | 0.51 | 1.43 | 1 |
| stroke 944 | 21 % → 21 % | 35.8 px | 0.50 | 1.00 | 2 |

Numbers say: wet paint spreads well beyond the stroke.

## Refs v3 · #39 Thick impasto weave — own sheet
own sheet 800 × 1065 · Impasto 1.00 · 96 px · 47.2 s

![Refs v3 · #39 Thick impasto weave — own sheet](Refs-v3-39-Thick-impasto-weave-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 6 % → 1 % | 77.4 px | 0.13 | 0.13 | 113 |
| stroke 2 | 15 % → 0 % | 89.1 px | 0.13 | 0.02 | 708 |
| stroke 3 | 19 % → 1 % | 118.1 px | 0.15 | 0.03 | 949 |
| stroke 4 | 23 % → 1 % | 142.1 px | 0.15 | 0.03 | 1162 |
| stroke 5 | 28 % → 1 % | 197.3 px | 0.16 | 0.05 | 1034 |
| stroke 6 | 39 % → 1 % | 488.4 px | 0.15 | 0.02 | 466 |
| stroke 7 | 38 % → 1 % | 566.7 px | 0.15 | 0.01 | 379 |
| stroke 8 | 38 % → 1 % | 559.5 px | 0.14 | 0.02 | 393 |
| stroke 9 | 36 % → 1 % | 530.5 px | 0.15 | 0.04 | 379 |
| stroke 10 | 34 % → 1 % | 502.0 px | 0.15 | 0.04 | 356 |
| stroke 11 | 31 % → 1 % | 436.4 px | 0.15 | 0.04 | 365 |
| stroke 12 | 28 % → 1 % | 433.7 px | 0.16 | 0.04 | 272 |
| stroke 13 | 26 % → 1 % | 601.0 px | 0.16 | 0.05 | 173 |
| stroke 14 | 12 % → 1 % | 85.0 px | 0.16 | 0.05 | 782 |
| stroke 15 | 15 % → 1 % | 276.8 px | 0.16 | 0.08 | 109 |
| stroke 16 | 21 % → 1 % | 114.9 px | 0.16 | 0.03 | 1331 |
| stroke 17 | 28 % → 1 % | 152.0 px | 0.16 | 0.02 | 1266 |
| stroke 18 | 42 % → 1 % | 243.6 px | 0.16 | 0.02 | 745 |
| stroke 19 | 55 % → 1 % | 322.2 px | 0.16 | 0.02 | 584 |
| stroke 20 | 62 % → 1 % | 293.7 px | 0.16 | 0.01 | 839 |
| stroke 21 | 65 % → 1 % | 259.8 px | 0.16 | 0.01 | 1045 |
| stroke 22 | 69 % → 1 % | 236.3 px | 0.16 | 0.01 | 983 |
| stroke 23 | 10 % → 0 % | 89.3 px | 0.16 | 0.03 | 248 |
| stroke 24 | 14 % → 0 % | 133.5 px | 0.00 | 0.00 | 326 |
| stroke 25 | 19 % → 0 % | 181.5 px | 0.00 | 0.00 | 327 |
| stroke 26 | 23 % → 1 % | 219.4 px | 0.17 | 0.05 | 296 |
| stroke 27 | 28 % → 2 % | 269.0 px | 0.17 | 0.07 | 318 |
| stroke 28 | 34 % → 2 % | 308.4 px | 0.17 | 0.07 | 275 |
| stroke 29 | 37 % → 2 % | 305.2 px | 0.17 | 0.07 | 310 |
| stroke 30 | 41 % → 3 % | 286.1 px | 0.17 | 0.07 | 308 |
| stroke 31 | 48 % → 3 % | 339.9 px | 0.17 | 0.07 | 254 |
| stroke 32 | 10 % → 1 % | 166.1 px | 0.15 | 0.12 | 217 |
| stroke 33 | 6 % → 1 % | 91.2 px | 0.16 | 0.22 | 246 |
| stroke 34 | 2 % → 0 % | 22.1 px | 0.00 | 0.00 | 22 |
| stroke 35 | 4 % → 1 % | 98.6 px | 0.16 | 0.35 | 108 |
| stroke 36 | 8 % → 1 % | 110.3 px | 0.16 | 0.12 | 395 |
| stroke 37 | 13 % → 1 % | 122.1 px | 0.15 | 0.09 | 615 |
| stroke 38 | 18 % → 1 % | 145.2 px | 0.15 | 0.06 | 719 |
| stroke 39 | 23 % → 1 % | 181.4 px | 0.15 | 0.05 | 771 |
| stroke 40 | 28 % → 1 % | 223.1 px | 0.15 | 0.04 | 883 |
| stroke 41 | 35 % → 0 % | 486.3 px | 0.13 | 0.01 | 395 |
| stroke 42 | 53 % → 0 % | 693.1 px | 0.00 | 0.00 | 242 |
| stroke 43 | 35 % → 1 % | 496.4 px | 0.16 | 0.04 | 390 |
| stroke 44 | 33 % → 2 % | 459.0 px | 0.16 | 0.05 | 409 |
| stroke 45 | 32 % → 2 % | 405.5 px | 0.16 | 0.05 | 377 |
| stroke 46 | 33 % → 2 % | 363.0 px | 0.16 | 0.06 | 420 |
| stroke 47 | 34 % → 2 % | 398.9 px | 0.16 | 0.07 | 292 |
| stroke 48 | 38 % → 3 % | 449.8 px | 0.16 | 0.07 | 211 |
| stroke 49 | 44 % → 3 % | 705.5 px | 0.16 | 0.08 | 153 |
| stroke 50 | 9 % → 0 % | 89.1 px | 0.16 | 0.00 | 344 |
| stroke 51 | 15 % → 1 % | 124.7 px | 0.16 | 0.04 | 584 |
| stroke 52 | 24 % → 0 % | 230.5 px | 0.00 | 0.00 | 286 |
| stroke 53 | 2 % → 2 % | 31.1 px | 0.15 | 0.88 | 53 |
| stroke 54 | 4 % → 2 % | 45.6 px | 0.15 | 0.61 | 62 |
| stroke 55 | 4 % → 2 % | 142.6 px | 0.15 | 0.47 | 57 |
| stroke 56 | 6 % → 3 % | 199.2 px | 0.15 | 0.44 | 21 |
| stroke 57 | 5 % → 2 % | 219.0 px | 0.15 | 0.36 | 52 |
| stroke 58 | 5 % → 2 % | 195.9 px | 0.15 | 0.30 | 63 |
| stroke 59 | 5 % → 1 % | 377.0 px | 0.15 | 0.25 | 43 |
| stroke 60 | 2 % → 0 % | 34.6 px | 0.00 | 0.00 | 22 |
| stroke 61 | 7 % → 1 % | 39.0 px | 0.13 | 0.08 | 232 |
| stroke 62 | 8 % → 0 % | 50.7 px | 0.13 | 0.06 | 195 |
| stroke 63 | 10 % → 0 % | 61.4 px | 0.13 | 0.05 | 179 |
| stroke 64 | 13 % → 0 % | 197.5 px | 0.00 | 0.00 | 69 |
| stroke 65 | 9 % → 1 % | 472.1 px | 0.13 | 0.06 | 20 |
| stroke 66 | 9 % → 0 % | 286.6 px | 0.13 | 0.05 | 50 |
| stroke 67 | 9 % → 0 % | 238.8 px | 0.13 | 0.05 | 85 |
| stroke 68 | 8 % → 0 % | 631.0 px | 0.00 | 0.00 | 9 |
| stroke 69 | 10 % → 1 % | 128.9 px | 0.14 | 0.10 | 105 |
| stroke 70 | 10 % → 0 % | 364.6 px | 0.13 | 0.05 | 48 |
| stroke 71 | 10 % → 1 % | 154.6 px | 0.16 | 0.06 | 79 |
| stroke 72 | 11 % → 0 % | 585.4 px | 0.00 | 0.00 | 5 |
| stroke 73 | 11 % → 0 % | 178.4 px | 0.00 | 0.00 | 44 |
| stroke 74 | 11 % → 0 % | 270.6 px | 0.00 | 0.00 | 27 |
| stroke 75 | 8 % → 1 % | 431.0 px | 0.16 | 0.16 | 12 |
| stroke 76 | 8 % → 1 % | 329.6 px | 0.16 | 0.16 | 29 |
| stroke 77 | 1 % → 0 % | 30.0 px | 0.15 | 0.10 | 38 |
| stroke 78 | 3 % → 1 % | 33.1 px | 0.16 | 0.34 | 119 |
| stroke 79 | 4 % → 1 % | 62.6 px | 0.16 | 0.28 | 93 |
| stroke 80 | 8 % → 0 % | 112.2 px | 0.00 | 0.00 | 68 |
| stroke 81 | 6 % → 1 % | 197.4 px | 0.16 | 0.10 | 35 |
| stroke 82 | 10 % → 0 % | 326.2 px | 0.00 | 0.00 | 16 |
| stroke 83 | 6 % → 1 % | 225.5 px | 0.16 | 0.17 | 17 |
| stroke 84 | 6 % → 1 % | 152.2 px | 0.16 | 0.24 | 42 |
| stroke 85 | 6 % → 1 % | 164.4 px | 0.16 | 0.24 | 32 |
| stroke 86 | 6 % → 2 % | 485.1 px | 0.16 | 0.28 | 15 |
| stroke 87 | 11 % → 0 % | 469.9 px | 0.00 | 0.00 | 6 |
| stroke 88 | 11 % → 0 % | 291.0 px | 0.00 | 0.00 | 23 |
| stroke 89 | 6 % → 2 % | 211.6 px | 0.16 | 0.25 | 18 |
| stroke 90 | 6 % → 2 % | 252.4 px | 0.16 | 0.26 | 26 |
| stroke 91 | 10 % → 0 % | 726.5 px | 0.00 | 0.00 | 8 |
| stroke 92 | 8 % → 1 % | 112.7 px | 0.16 | 0.16 | 123 |
| stroke 93 | 14 % → 0 % | 141.4 px | 0.15 | 0.01 | 66 |
| stroke 94 | 10 % → 1 % | 165.4 px | 0.16 | 0.13 | 143 |
| stroke 95 | 18 % → 0 % | 279.5 px | 0.00 | 0.00 | 45 |
| stroke 96 | 14 % → 1 % | 280.7 px | 0.16 | 0.05 | 39 |
| stroke 97 | 11 % → 1 % | 257.8 px | 0.16 | 0.13 | 54 |
| stroke 98 | 6 % → 2 % | 354.9 px | 0.16 | 0.24 | 13 |
| stroke 99 | 8 % → 2 % | 287.9 px | 0.16 | 0.22 | 30 |
| stroke 100 | 10 % → 2 % | 299.4 px | 0.16 | 0.16 | 36 |
| stroke 101 | 11 % → 1 % | 267.7 px | 0.16 | 0.13 | 65 |
| stroke 102 | 4 % → 1 % | 101.2 px | 0.17 | 0.33 | 61 |
| stroke 103 | 5 % → 1 % | 400.4 px | 0.16 | 0.22 | 13 |
| stroke 104 | 2 % → 4 % | 23.8 px | 0.16 | 1.91 | 51 |
| stroke 105 | 5 % → 5 % | 67.2 px | 0.17 | 0.93 | 23 |
| stroke 106 | 1 % → 1 % | 54.8 px | 0.15 | 0.94 | 21 |
| stroke 107 | 1 % → 1 % | 22.0 px | 0.16 | 0.92 | 62 |
| stroke 108 | 1 % → 1 % | 22.3 px | 0.16 | 0.94 | 35 |

Numbers say: wet paint spreads well beyond the stroke.

## Refs v3 · #40 Watercolour blooms — own sheet
own sheet 800 × 1170 · Watercolour 1.00 + water 55 % · 112 px · 210.0 s

![Refs v3 · #40 Watercolour blooms — own sheet](Refs-v3-40-Watercolour-blooms-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 11 % → 99 % | 116.5 px | 0.12 | 8.79 | 799 |
| stroke 2 | 18 % → 93 % | 266.0 px | 0.10 | 5.07 | 598 |
| stroke 3 | 16 % → 55 % | 237.8 px | 0.05 | 3.43 | 701 |
| stroke 4 | 25 % → 100 % | 146.9 px | 0.17 | 3.98 | 1358 |
| stroke 5 | 45 % → 93 % | 304.5 px | 0.06 | 2.08 | 1118 |
| stroke 6 | 52 % → 97 % | 680.9 px | 0.06 | 1.85 | 716 |
| stroke 7 | 43 % → 79 % | 525.6 px | 0.06 | 1.82 | 803 |
| stroke 8 | 62 % → 99 % | 684.0 px | 0.08 | 1.59 | 822 |
| stroke 9 | 70 % → 98 % | 711.1 px | 0.05 | 1.40 | 945 |
| stroke 10 | 54 % → 99 % | 863.7 px | 0.14 | 1.82 | 527 |
| stroke 11 | 39 % → 68 % | 552.0 px | 0.05 | 1.75 | 821 |
| stroke 12 | 54 % → 95 % | 1419.3 px | 0.11 | 1.74 | 203 |
| stroke 13 | 79 % → 99 % | 895.4 px | 0.07 | 1.25 | 951 |
| stroke 14 | 45 % → 100 % | 693.2 px | 0.14 | 2.24 | 276 |
| stroke 15 | 56 % → 98 % | 718.7 px | 0.14 | 1.76 | 686 |
| stroke 16 | 80 % → 99 % | 1619.1 px | 0.08 | 1.23 | 375 |
| stroke 17 | 59 % → 100 % | 1104.5 px | 0.15 | 1.69 | 577 |
| stroke 18 | 66 % → 100 % | 1199.0 px | 0.14 | 1.52 | 413 |
| stroke 19 | 80 % → 99 % | 1643.1 px | 0.09 | 1.24 | 434 |
| stroke 20 | 32 % → 50 % | 480.6 px | 0.05 | 1.56 | 707 |
| stroke 21 | 50 % → 66 % | 1081.4 px | 0.05 | 1.33 | 281 |
| stroke 22 | 84 % → 100 % | 1005.3 px | 0.07 | 1.19 | 317 |
| stroke 23 | 89 % → 98 % | 2232.1 px | 0.08 | 1.11 | 308 |
| stroke 24 | 11 % → 100 % | 130.9 px | 0.24 | 9.23 | 353 |
| stroke 25 | 38 % → 56 % | 1825.1 px | 0.05 | 1.48 | 17 |
| stroke 26 | 34 % → 54 % | 529.8 px | 0.06 | 1.59 | 38 |
| stroke 27 | 53 % → 100 % | 1770.2 px | 0.17 | 1.89 | 97 |
| stroke 28 | 61 % → 100 % | 662.9 px | 0.13 | 1.64 | 349 |
| stroke 29 | 54 % → 100 % | 783.2 px | 0.16 | 1.86 | 154 |
| stroke 30 | 52 % → 100 % | 1049.7 px | 0.18 | 1.90 | 272 |
| stroke 31 | 58 % → 100 % | 1397.3 px | 0.15 | 1.74 | 111 |
| stroke 32 | 53 % → 100 % | 947.1 px | 0.16 | 1.88 | 111 |
| stroke 33 | 62 % → 100 % | 1152.1 px | 0.13 | 1.60 | 161 |
| stroke 34 | 64 % → 100 % | 1839.8 px | 0.14 | 1.56 | 109 |
| stroke 35 | 64 % → 100 % | 548.0 px | 0.14 | 1.57 | 114 |
| stroke 36 | 84 % → 100 % | 734.0 px | 0.09 | 1.19 | 510 |
| stroke 37 | 81 % → 100 % | 576.0 px | 0.12 | 1.23 | 289 |
| stroke 38 | 84 % → 100 % | 1030.3 px | 0.12 | 1.19 | 228 |
| stroke 39 | 89 % → 100 % | 1242.8 px | 0.09 | 1.12 | 266 |
| stroke 40 | 82 % → 100 % | 1708.1 px | 0.14 | 1.22 | 108 |
| stroke 41 | 80 % → 100 % | 1155.0 px | 0.16 | 1.25 | 72 |
| stroke 42 | 86 % → 100 % | 1729.2 px | 0.13 | 1.16 | 79 |
| stroke 43 | 55 % → 87 % | 912.3 px | 0.11 | 1.57 | 401 |
| stroke 44 | 42 % → 65 % | 1042.2 px | 0.08 | 1.58 | 137 |
| stroke 45 | 46 % → 68 % | 1757.0 px | 0.06 | 1.49 | 96 |
| stroke 46 | 52 % → 86 % | 2263.9 px | 0.11 | 1.66 | 95 |
| stroke 47 | 55 % → 93 % | 2140.2 px | 0.13 | 1.68 | 81 |
| stroke 48 | 73 % → 98 % | 3141.8 px | 0.12 | 1.34 | 75 |
| stroke 49 | 45 % → 62 % | 1606.4 px | 0.06 | 1.38 | 110 |
| stroke 50 | 65 % → 92 % | 2819.0 px | 0.11 | 1.41 | 81 |
| stroke 51 | 74 % → 83 % | 687.5 px | 0.05 | 1.11 | 406 |
| stroke 52 | 76 % → 85 % | 932.0 px | 0.04 | 1.12 | 495 |
| stroke 53 | 66 % → 76 % | 1199.0 px | 0.05 | 1.15 | 110 |
| stroke 54 | 77 % → 84 % | 2148.6 px | 0.05 | 1.09 | 157 |
| stroke 55 | 61 % → 65 % | 911.5 px | 0.04 | 1.07 | 316 |
| stroke 56 | 66 % → 70 % | 845.6 px | 0.04 | 1.06 | 226 |
| stroke 57 | 60 % → 64 % | 879.8 px | 0.05 | 1.06 | 187 |
| stroke 58 | 75 % → 78 % | 1993.5 px | 0.04 | 1.03 | 138 |
| stroke 59 | 55 % → 58 % | 1844.2 px | 0.05 | 1.04 | 111 |
| stroke 60 | 90 % → 93 % | 2155.8 px | 0.04 | 1.03 | 115 |
| stroke 61 | 82 % → 84 % | 2491.7 px | 0.04 | 1.03 | 120 |
| stroke 62 | 67 % → 69 % | 2119.3 px | 0.04 | 1.03 | 129 |
| stroke 63 | 54 % → 55 % | 946.0 px | 0.06 | 1.04 | 141 |
| stroke 64 | 93 % → 100 % | 1090.9 px | 0.07 | 1.07 | 73 |
| stroke 65 | 70 % → 98 % | 6135.4 px | 0.14 | 1.40 | 14 |
| stroke 66 | 67 % → 100 % | 341.0 px | 0.17 | 1.49 | 2092 |
| stroke 67 | 76 % → 100 % | 714.0 px | 0.17 | 1.31 | 799 |
| stroke 68 | 88 % → 100 % | 613.8 px | 0.21 | 1.13 | 325 |
| stroke 69 | 81 % → 100 % | 712.9 px | 0.18 | 1.24 | 782 |
| stroke 70 | 71 % → 100 % | 827.4 px | 0.24 | 1.41 | 326 |
| stroke 71 | 76 % → 100 % | 1284.3 px | 0.18 | 1.31 | 455 |
| stroke 72 | 64 % → 99 % | 651.2 px | 0.20 | 1.54 | 906 |
| stroke 73 | 76 % → 100 % | 1176.3 px | 0.19 | 1.31 | 706 |
| stroke 74 | 43 % → 79 % | 696.0 px | 0.13 | 1.83 | 234 |
| stroke 75 | 74 % → 96 % | 570.4 px | 0.20 | 1.30 | 1031 |
| stroke 76 | 69 % → 89 % | 718.1 px | 0.18 | 1.30 | 544 |
| stroke 77 | 94 % → 100 % | 2021.0 px | 0.23 | 1.06 | 214 |
| stroke 78 | 74 % → 91 % | 717.5 px | 0.19 | 1.23 | 550 |
| stroke 79 | 89 % → 99 % | 749.6 px | 0.19 | 1.12 | 406 |
| stroke 80 | 98 % → 100 % | 1219.9 px | 0.24 | 1.02 | 263 |
| stroke 81 | 78 % → 87 % | 1000.5 px | 0.17 | 1.12 | 540 |
| stroke 82 | 98 % → 100 % | 1096.7 px | 0.23 | 1.02 | 325 |
| stroke 83 | 90 % → 100 % | 1851.8 px | 0.23 | 1.12 | 258 |
| stroke 84 | 93 % → 100 % | 1449.7 px | 0.22 | 1.08 | 288 |
| stroke 85 | 68 % → 82 % | 1224.9 px | 0.14 | 1.20 | 180 |
| stroke 86 | 99 % → 100 % | 2363.2 px | 0.17 | 1.01 | 245 |
| stroke 87 | 78 % → 84 % | 1523.2 px | 0.12 | 1.07 | 435 |
| stroke 88 | 75 % → 81 % | 2213.0 px | 0.11 | 1.08 | 260 |
| stroke 89 | 83 % → 88 % | 1744.3 px | 0.13 | 1.05 | 384 |
| stroke 90 | 86 % → 86 % | 1406.5 px | 0.05 | 1.00 | 272 |
| stroke 91 | 100 % → 100 % | 2162.0 px | 0.21 | 1.00 | 15 |
| stroke 92 | 97 % → 100 % | 670.3 px | 0.09 | 1.03 | 711 |
| stroke 93 | 100 % → 100 % | 694.1 px | 0.11 | 1.00 | 549 |
| stroke 94 | 100 % → 100 % | 757.2 px | 0.10 | 1.00 | 564 |
| stroke 95 | 100 % → 100 % | 2318.1 px | 0.10 | 1.00 | 183 |
| stroke 96 | 94 % → 97 % | 1242.0 px | 0.14 | 1.03 | 687 |
| stroke 97 | 96 % → 97 % | 1096.1 px | 0.17 | 1.01 | 868 |
| stroke 98 | 96 % → 97 % | 1734.1 px | 0.16 | 1.01 | 394 |
| stroke 99 | 99 % → 100 % | 1409.2 px | 0.20 | 1.01 | 462 |
| stroke 100 | 100 % → 100 % | 1421.2 px | 0.19 | 1.00 | 576 |
| stroke 101 | 99 % → 99 % | 3020.2 px | 0.18 | 1.00 | 202 |
| stroke 102 | 96 % → 96 % | 2739.4 px | 0.16 | 1.00 | 244 |
| stroke 103 | 100 % → 100 % | 2180.2 px | 0.18 | 1.00 | 370 |
| stroke 104 | 97 % → 98 % | 3182.7 px | 0.17 | 1.00 | 134 |
| stroke 105 | 100 % → 100 % | 2067.8 px | 0.21 | 1.00 | 247 |
| stroke 106 | 100 % → 100 % | 3129.8 px | 0.21 | 1.00 | 162 |

Numbers say: wet paint spreads well beyond the stroke.

## Refs v3 · #41 Coloured pencil — own sheet
own sheet 800 × 1108 · Charcoal 0.50 · Pastel 0.50 · 12 px · 74.3 s

![Refs v3 · #41 Coloured pencil — own sheet](Refs-v3-41-Coloured-pencil-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 8 % → 0 % | 11.9 px | 0.00 | 0.00 | 11 |
| stroke 2 | 8 % → 0 % | 10.5 px | 0.00 | 0.00 | 8 |
| stroke 3 | 11 % → 0 % | 17.4 px | 0.00 | 0.00 | 5 |
| stroke 4 | 11 % → 0 % | 14.9 px | 0.00 | 0.00 | 5 |
| stroke 5 | 15 % → 0 % | 26.1 px | 0.00 | 0.00 | 6 |
| stroke 6 | 11 % → 0 % | 11.8 px | 0.00 | 0.00 | 5 |
| stroke 7 | 28 % → 0 % | 38.2 px | 0.00 | 0.00 | 8 |
| stroke 8 | 18 % → 0 % | 25.7 px | 0.00 | 0.00 | 3 |
| stroke 9 | 33 % → 0 % | 51.1 px | 0.00 | 0.00 | 2 |
| stroke 10 | 19 % → 0 % | 21.6 px | 0.13 | 0.02 | 7 |
| stroke 11 | 24 % → 0 % | 38.2 px | 0.00 | 0.00 | 7 |
| stroke 12 | 23 % → 0 % | 30.9 px | 0.00 | 0.00 | 4 |
| stroke 13 | 14 % → 0 % | 24.0 px | 0.00 | 0.00 | 2 |
| stroke 14 | 29 % → 0 % | 42.1 px | 0.00 | 0.00 | 5 |
| stroke 15 | 22 % → 0 % | 31.7 px | 0.13 | 0.01 | 5 |
| stroke 16 | 43 % → 0 % | 63.7 px | 0.00 | 0.00 | 6 |
| stroke 17 | 29 % → 0 % | 52.3 px | 0.00 | 0.00 | 2 |
| stroke 18 | 28 % → 0 % | 30.5 px | 0.00 | 0.00 | 6 |
| stroke 19 | 22 % → 0 % | 34.0 px | 0.00 | 0.00 | 4 |
| stroke 20 | 34 % → 0 % | 53.6 px | 0.00 | 0.00 | 3 |
| stroke 21 | 20 % → 11 % | 27.7 px | 0.14 | 0.51 | 7 |
| stroke 22 | 38 % → 0 % | 52.7 px | 0.00 | 0.00 | 6 |
| stroke 23 | 50 % → 0 % | 78.8 px | 0.00 | 0.00 | 6 |
| stroke 24 | 41 % → 0 % | 76.1 px | 0.00 | 0.00 | 2 |
| stroke 25 | 18 % → 9 % | 27.0 px | 0.13 | 0.47 | 2 |
| stroke 26 | 56 % → 0 % | 67.2 px | 0.00 | 0.00 | 3 |
| stroke 27 | 34 % → 0 % | 93.1 px | 0.00 | 0.00 | 0 |
| stroke 28 | 46 % → 0 % | 67.6 px | 0.00 | 0.00 | 2 |
| stroke 29 | 57 % → 0 % | 99.6 px | 0.00 | 0.00 | 2 |
| stroke 30 | 53 % → 0 % | 147.2 px | 0.00 | 0.00 | 1 |
| stroke 31 | 26 % → 0 % | 39.5 px | 0.00 | 0.00 | 3 |
| stroke 32 | 38 % → 0 % | 61.9 px | 0.00 | 0.00 | 2 |
| stroke 33 | 65 % → 0 % | 185.5 px | 0.00 | 0.00 | 0 |
| stroke 34 | 33 % → 0 % | 53.2 px | 0.00 | 0.00 | 3 |
| stroke 35 | 38 % → 0 % | 89.3 px | 0.00 | 0.00 | 1 |
| stroke 36 | 34 % → 0 % | 59.1 px | 0.00 | 0.00 | 2 |
| stroke 37 | 36 % → 0 % | 99.3 px | 0.00 | 0.00 | 1 |
| stroke 38 | 40 % → 0 % | 75.4 px | 0.00 | 0.00 | 2 |
| stroke 39 | 21 % → 23 % | 59.8 px | 0.15 | 1.10 | 0 |
| stroke 40 | 54 % → 1 % | 131.6 px | 0.13 | 0.01 | 1 |
| stroke 41 | 29 % → 0 % | 67.2 px | 0.00 | 0.00 | 1 |
| stroke 42 | 53 % → 0 % | 105.8 px | 0.00 | 0.00 | 3 |
| stroke 43 | 64 % → 0 % | 141.8 px | 0.00 | 0.00 | 1 |
| stroke 44 | 51 % → 0 % | 142.3 px | 0.00 | 0.00 | 0 |
| stroke 45 | 52 % → 0 % | 134.2 px | 0.00 | 0.00 | 1 |
| stroke 46 | 34 % → 0 % | 96.3 px | 0.00 | 0.00 | 0 |
| stroke 47 | 57 % → 0 % | 94.3 px | 0.00 | 0.00 | 4 |
| stroke 48 | 56 % → 0 % | 159.9 px | 0.00 | 0.00 | 0 |
| stroke 49 | 24 % → 0 % | 66.3 px | 0.00 | 0.00 | 1 |
| stroke 50 | 38 % → 0 % | 88.6 px | 0.00 | 0.00 | 1 |
| stroke 51 | 67 % → 0 % | 187.5 px | 0.00 | 0.00 | 0 |
| stroke 52 | 10 % → 0 % | 11.0 px | 0.00 | 0.00 | 6 |
| stroke 53 | 11 % → 0 % | 15.1 px | 0.00 | 0.00 | 6 |
| stroke 54 | 21 % → 0 % | 23.4 px | 0.00 | 0.00 | 5 |
| stroke 55 | 12 % → 0 % | 18.3 px | 0.00 | 0.00 | 10 |
| stroke 56 | 8 % → 0 % | 12.4 px | 0.00 | 0.00 | 10 |
| stroke 57 | 17 % → 0 % | 23.8 px | 0.00 | 0.00 | 6 |
| stroke 58 | 21 % → 0 % | 35.6 px | 0.00 | 0.00 | 5 |
| stroke 59 | 7 % → 0 % | 18.7 px | 0.00 | 0.00 | 1 |
| stroke 60 | 36 % → 0 % | 58.5 px | 0.00 | 0.00 | 3 |
| stroke 61 | 24 % → 0 % | 38.8 px | 0.00 | 0.00 | 3 |
| stroke 62 | 8 % → 0 % | 11.1 px | 0.19 | 0.04 | 7 |
| stroke 63 | 22 % → 0 % | 29.3 px | 0.00 | 0.00 | 6 |
| stroke 64 | 25 % → 0 % | 35.4 px | 0.00 | 0.00 | 7 |
| stroke 65 | 21 % → 0 % | 35.1 px | 0.00 | 0.00 | 2 |
| stroke 66 | 23 % → 1 % | 34.3 px | 0.14 | 0.06 | 7 |
| stroke 67 | 41 % → 0 % | 69.5 px | 0.00 | 0.00 | 2 |
| stroke 68 | 30 % → 0 % | 35.4 px | 0.00 | 0.00 | 4 |
| stroke 69 | 30 % → 0 % | 66.2 px | 0.00 | 0.00 | 1 |
| stroke 70 | 26 % → 0 % | 33.4 px | 0.00 | 0.00 | 10 |
| stroke 71 | 23 % → 0 % | 35.0 px | 0.00 | 0.00 | 5 |
| stroke 72 | 38 % → 0 % | 61.3 px | 0.00 | 0.00 | 3 |
| stroke 73 | 49 % → 0 % | 71.0 px | 0.00 | 0.00 | 8 |
| stroke 74 | 37 % → 0 % | 69.8 px | 0.00 | 0.00 | 2 |
| stroke 75 | 52 % → 0 % | 73.7 px | 0.00 | 0.00 | 5 |
| stroke 76 | 28 % → 0 % | 41.6 px | 0.00 | 0.00 | 9 |
| stroke 77 | 61 % → 0 % | 124.5 px | 0.00 | 0.00 | 1 |
| stroke 78 | 46 % → 0 % | 111.5 px | 0.00 | 0.00 | 1 |
| stroke 79 | 62 % → 0 % | 119.6 px | 0.00 | 0.00 | 3 |
| stroke 80 | 42 % → 0 % | 69.2 px | 0.00 | 0.00 | 3 |
| stroke 81 | 44 % → 0 % | 69.7 px | 0.00 | 0.00 | 8 |
| stroke 82 | 60 % → 0 % | 115.6 px | 0.00 | 0.00 | 1 |
| stroke 83 | 49 % → 0 % | 135.7 px | 0.00 | 0.00 | 1 |
| stroke 84 | 60 % → 0 % | 72.4 px | 0.00 | 0.00 | 3 |
| stroke 85 | 51 % → 0 % | 93.4 px | 0.00 | 0.00 | 3 |
| stroke 86 | 47 % → 0 % | 133.8 px | 0.00 | 0.00 | 0 |
| stroke 87 | 66 % → 0 % | 105.8 px | 0.00 | 0.00 | 6 |
| stroke 88 | 71 % → 0 % | 156.1 px | 0.00 | 0.00 | 1 |
| stroke 89 | 21 % → 0 % | 41.7 px | 0.00 | 0.00 | 2 |
| stroke 90 | 48 % → 0 % | 93.6 px | 0.00 | 0.00 | 1 |
| stroke 91 | 65 % → 0 % | 147.3 px | 0.00 | 0.00 | 2 |
| stroke 92 | 39 % → 0 % | 104.6 px | 0.00 | 0.00 | 0 |
| stroke 93 | 34 % → 0 % | 60.2 px | 0.00 | 0.00 | 2 |
| stroke 94 | 29 % → 0 % | 82.3 px | 0.00 | 0.00 | 1 |
| stroke 95 | 39 % → 0 % | 75.8 px | 0.00 | 0.00 | 3 |
| stroke 96 | 25 % → 0 % | 68.5 px | 0.00 | 0.00 | 1 |
| stroke 97 | 69 % → 0 % | 195.1 px | 0.00 | 0.00 | 1 |
| stroke 98 | 65 % → 0 % | 161.8 px | 0.00 | 0.00 | 1 |
| stroke 99 | 8 % → 6 % | 11.7 px | 0.17 | 0.72 | 11 |
| stroke 100 | 10 % → 0 % | 10.0 px | 0.00 | 0.00 | 9 |
| stroke 101 | 16 % → 0 % | 19.8 px | 0.00 | 0.00 | 5 |
| stroke 102 | 11 % → 6 % | 12.5 px | 0.16 | 0.56 | 7 |
| stroke 103 | 9 % → 0 % | 14.4 px | 0.00 | 0.00 | 5 |
| stroke 104 | 13 % → 13 % | 20.0 px | 0.17 | 0.97 | 6 |
| stroke 105 | 21 % → 0 % | 25.1 px | 0.00 | 0.00 | 10 |
| stroke 106 | 16 % → 0 % | 26.6 px | 0.00 | 0.00 | 3 |
| stroke 107 | 7 % → 0 % | 19.4 px | 0.00 | 0.00 | 1 |
| stroke 108 | 28 % → 0 % | 41.6 px | 0.00 | 0.00 | 6 |
| stroke 109 | 14 % → 0 % | 21.9 px | 0.00 | 0.00 | 7 |
| stroke 110 | 18 % → 27 % | 25.3 px | 0.17 | 1.51 | 5 |
| stroke 111 | 21 % → 0 % | 29.1 px | 0.00 | 0.00 | 9 |
| stroke 112 | 22 % → 0 % | 37.2 px | 0.00 | 0.00 | 6 |
| stroke 113 | 22 % → 0 % | 35.5 px | 0.00 | 0.00 | 3 |
| stroke 114 | 36 % → 1 % | 62.1 px | 0.13 | 0.03 | 2 |
| stroke 115 | 42 % → 1 % | 66.9 px | 0.12 | 0.02 | 5 |
| stroke 116 | 34 % → 0 % | 61.4 px | 0.00 | 0.00 | 2 |
| stroke 117 | 43 % → 0 % | 58.2 px | 0.00 | 0.00 | 3 |
| stroke 118 | 34 % → 0 % | 55.0 px | 0.00 | 0.00 | 3 |
| stroke 119 | 23 % → 0 % | 44.4 px | 0.00 | 0.00 | 2 |
| stroke 120 | 46 % → 0 % | 64.7 px | 0.00 | 0.00 | 2 |
| stroke 121 | 27 % → 0 % | 57.7 px | 0.00 | 0.00 | 1 |
| stroke 122 | 37 % → 13 % | 55.8 px | 0.17 | 0.34 | 4 |
| stroke 123 | 27 % → 0 % | 57.1 px | 0.00 | 0.00 | 1 |
| stroke 124 | 24 % → 0 % | 60.6 px | 0.00 | 0.00 | 0 |
| stroke 125 | 34 % → 19 % | 54.2 px | 0.17 | 0.56 | 4 |
| stroke 126 | 51 % → 0 % | 130.4 px | 0.00 | 0.00 | 0 |
| stroke 127 | 30 % → 0 % | 43.5 px | 0.00 | 0.00 | 4 |
| stroke 128 | 57 % → 0 % | 85.0 px | 0.00 | 0.00 | 3 |
| stroke 129 | 47 % → 0 % | 83.1 px | 0.00 | 0.00 | 2 |
| stroke 130 | 55 % → 17 % | 152.6 px | 0.17 | 0.31 | 0 |
| stroke 131 | 52 % → 0 % | 132.2 px | 0.00 | 0.00 | 0 |
| stroke 132 | 57 % → 15 % | 140.7 px | 0.14 | 0.27 | 1 |
| stroke 133 | 41 % → 0 % | 69.9 px | 0.00 | 0.00 | 6 |
| stroke 134 | 30 % → 4 % | 44.1 px | 0.19 | 0.13 | 2 |
| stroke 135 | 31 % → 0 % | 83.3 px | 0.00 | 0.00 | 1 |
| stroke 136 | 55 % → 0 % | 122.0 px | 0.00 | 0.00 | 2 |
| stroke 137 | 61 % → 0 % | 130.6 px | 0.00 | 0.00 | 6 |
| stroke 138 | 58 % → 0 % | 129.2 px | 0.00 | 0.00 | 3 |
| stroke 139 | 49 % → 0 % | 89.8 px | 0.00 | 0.00 | 7 |
| stroke 140 | 51 % → 12 % | 74.9 px | 0.19 | 0.23 | 4 |
| stroke 141 | 52 % → 0 % | 132.9 px | 0.00 | 0.00 | 1 |
| stroke 142 | 48 % → 0 % | 136.0 px | 0.00 | 0.00 | 0 |
| stroke 143 | 60 % → 0 % | 138.4 px | 0.00 | 0.00 | 2 |
| stroke 144 | 61 % → 14 % | 164.8 px | 0.19 | 0.23 | 2 |
| stroke 145 | 8 % → 2 % | 12.2 px | 0.19 | 0.22 | 8 |
| stroke 146 | 16 % → 5 % | 25.6 px | 0.19 | 0.28 | 6 |
| stroke 147 | 11 % → 0 % | 19.3 px | 0.00 | 0.00 | 5 |
| stroke 148 | 13 % → 0 % | 13.6 px | 0.00 | 0.00 | 9 |
| stroke 149 | 26 % → 1 % | 38.4 px | 0.19 | 0.02 | 4 |
| stroke 150 | 14 % → 0 % | 16.8 px | 0.00 | 0.00 | 5 |
| stroke 151 | 13 % → 0 % | 14.5 px | 0.00 | 0.00 | 8 |
| stroke 152 | 25 % → 0 % | 33.8 px | 0.00 | 0.00 | 6 |
| stroke 153 | 34 % → 0 % | 41.5 px | 0.00 | 0.00 | 5 |
| stroke 154 | 25 % → 11 % | 38.6 px | 0.19 | 0.43 | 45 |
| stroke 155 | 14 % → 10 % | 17.6 px | 0.17 | 0.73 | 4 |
| stroke 156 | 16 % → 0 % | 27.1 px | 0.00 | 0.00 | 6 |
| stroke 157 | 41 % → 0 % | 66.6 px | 0.00 | 0.00 | 5 |
| stroke 158 | 11 % → 0 % | 11.5 px | 0.00 | 0.00 | 11 |
| stroke 159 | 34 % → 0 % | 53.2 px | 0.00 | 0.00 | 3 |
| stroke 160 | 17 % → 0 % | 27.8 px | 0.00 | 0.00 | 3 |
| stroke 161 | 14 % → 26 % | 26.2 px | 0.17 | 1.77 | 3 |
| stroke 162 | 24 % → 6 % | 67.5 px | 0.18 | 0.26 | 0 |
| stroke 163 | 40 % → 0 % | 61.3 px | 0.00 | 0.00 | 5 |
| stroke 164 | 30 % → 0 % | 50.5 px | 0.00 | 0.00 | 1 |
| stroke 165 | 29 % → 0 % | 71.1 px | 0.00 | 0.00 | 2 |
| stroke 166 | 35 % → 0 % | 46.9 px | 0.00 | 0.00 | 8 |
| stroke 167 | 30 % → 9 % | 48.3 px | 0.19 | 0.32 | 4 |
| stroke 168 | 34 % → 0 % | 54.1 px | 0.00 | 0.00 | 1 |
| stroke 169 | 49 % → 0 % | 113.7 px | 0.00 | 0.00 | 1 |
| stroke 170 | 43 % → 0 % | 68.2 px | 0.00 | 0.00 | 4 |
| stroke 171 | 47 % → 0 % | 73.0 px | 0.00 | 0.00 | 8 |
| stroke 172 | 41 % → 6 % | 107.3 px | 0.19 | 0.15 | 0 |
| stroke 173 | 60 % → 0 % | 168.8 px | 0.00 | 0.00 | 1 |
| stroke 174 | 46 % → 0 % | 101.3 px | 0.00 | 0.00 | 2 |
| stroke 175 | 57 % → 0 % | 89.6 px | 0.00 | 0.00 | 4 |
| stroke 176 | 29 % → 0 % | 50.4 px | 0.00 | 0.00 | 2 |
| stroke 177 | 34 % → 0 % | 42.4 px | 0.00 | 0.00 | 7 |
| stroke 178 | 37 % → 0 % | 78.2 px | 0.00 | 0.00 | 2 |
| stroke 179 | 49 % → 0 % | 128.7 px | 0.00 | 0.00 | 0 |
| stroke 180 | 49 % → 0 % | 127.5 px | 0.00 | 0.00 | 0 |
| stroke 181 | 62 % → 0 % | 146.8 px | 0.00 | 0.00 | 1 |
| stroke 182 | 64 % → 0 % | 166.6 px | 0.00 | 0.00 | 3 |
| stroke 183 | 48 % → 0 % | 90.7 px | 0.00 | 0.00 | 1 |
| stroke 184 | 27 % → 0 % | 73.2 px | 0.00 | 0.00 | 1 |
| stroke 185 | 48 % → 0 % | 136.1 px | 0.00 | 0.00 | 0 |
| stroke 186 | 59 % → 0 % | 91.1 px | 0.00 | 0.00 | 4 |
| stroke 187 | 35 % → 15 % | 96.4 px | 0.19 | 0.45 | 5 |
| stroke 188 | 64 % → 0 % | 176.3 px | 0.00 | 0.00 | 0 |
| stroke 189 | 40 % → 0 % | 98.5 px | 0.00 | 0.00 | 1 |
| stroke 190 | 58 % → 0 % | 136.6 px | 0.00 | 0.00 | 1 |
| stroke 191 | 32 % → 26 % | 83.6 px | 0.18 | 0.84 | 1 |
| stroke 192 | 12 % → 0 % | 20.4 px | 0.00 | 0.00 | 4 |
| stroke 193 | 10 % → 0 % | 27.7 px | 0.00 | 0.00 | 0 |
| stroke 194 | 19 % → 0 % | 44.4 px | 0.00 | 0.00 | 1 |
| stroke 195 | 22 % → 0 % | 49.2 px | 0.00 | 0.00 | 1 |
| stroke 196 | 9 % → 0 % | 16.6 px | 0.00 | 0.00 | 2 |
| stroke 197 | 16 % → 0 % | 37.3 px | 0.00 | 0.00 | 2 |
| stroke 198 | 6 % → 27 % | 11.6 px | 0.17 | 4.39 | 1 |
| stroke 199 | 9 % → 4 % | 13.4 px | 0.14 | 0.39 | 16 |
| stroke 200 | 11 % → 0 % | 16.7 px | 0.13 | 0.01 | 11 |
| stroke 201 | 17 % → 23 % | 25.6 px | 0.17 | 1.39 | 9 |
| stroke 202 | 30 % → 8 % | 40.4 px | 0.15 | 0.27 | 3 |
| stroke 203 | 24 % → 22 % | 34.6 px | 0.16 | 0.93 | 2 |
| stroke 204 | 29 % → 0 % | 69.9 px | 0.00 | 0.00 | 1 |
| stroke 205 | 30 % → 5 % | 58.3 px | 0.13 | 0.16 | 2 |
| stroke 206 | 33 % → 0 % | 48.9 px | 0.13 | 0.01 | 10 |
| stroke 207 | 7 % → 0 % | 12.3 px | 0.00 | 0.00 | 2 |
| stroke 208 | 17 % → 0 % | 34.1 px | 0.00 | 0.00 | 2 |
| stroke 209 | 28 % → 1 % | 77.8 px | 0.19 | 0.04 | 1 |
| stroke 210 | 34 % → 0 % | 94.7 px | 0.00 | 0.00 | 0 |
| stroke 211 | 38 % → 0 % | 110.2 px | 0.00 | 0.00 | 0 |
| stroke 212 | 38 % → 0 % | 91.9 px | 0.00 | 0.00 | 1 |
| stroke 213 | 31 % → 6 % | 87.9 px | 0.13 | 0.18 | 1 |
| stroke 214 | 43 % → 0 % | 93.5 px | 0.00 | 0.00 | 1 |
| stroke 215 | 27 % → 0 % | 65.3 px | 0.00 | 0.00 | 2 |
| stroke 216 | 37 % → 0 % | 106.2 px | 0.00 | 0.00 | 1 |
| stroke 217 | 7 % → 8 % | 11.2 px | 0.19 | 1.18 | 4 |
| stroke 218 | 8 % → 0 % | 10.8 px | 0.00 | 0.00 | 5 |
| stroke 219 | 12 % → 12 % | 16.0 px | 0.19 | 1.01 | 3 |
| stroke 220 | 10 % → 8 % | 13.4 px | 0.16 | 0.86 | 5 |
| stroke 221 | 24 % → 0 % | 38.4 px | 0.00 | 0.00 | 3 |
| stroke 222 | 15 % → 0 % | 27.6 px | 0.00 | 0.00 | 5 |
| stroke 223 | 33 % → 0 % | 72.4 px | 0.00 | 0.00 | 1 |
| stroke 224 | 22 % → 21 % | 41.3 px | 0.19 | 0.98 | 3 |
| stroke 225 | 21 % → 1 % | 33.1 px | 0.12 | 0.03 | 1 |
| stroke 226 | 33 % → 0 % | 70.3 px | 0.00 | 0.00 | 1 |
| stroke 227 | 22 % → 25 % | 56.7 px | 0.17 | 1.14 | 0 |
| stroke 228 | 20 % → 11 % | 53.3 px | 0.16 | 0.53 | 0 |
| stroke 229 | 7 % → 0 % | 11.0 px | 0.00 | 0.00 | 2 |
| stroke 230 | 14 % → 0 % | 28.5 px | 0.00 | 0.00 | 3 |
| stroke 231 | 19 % → 0 % | 27.2 px | 0.00 | 0.00 | 6 |
| stroke 232 | 11 % → 0 % | 15.9 px | 0.00 | 0.00 | 6 |
| stroke 233 | 10 % → 0 % | 18.3 px | 0.00 | 0.00 | 1 |
| stroke 234 | 14 % → 0 % | 23.4 px | 0.00 | 0.00 | 1 |
| stroke 235 | 26 % → 0 % | 50.9 px | 0.00 | 0.00 | 4 |
| stroke 236 | 25 % → 0 % | 65.2 px | 0.00 | 0.00 | 2 |
| stroke 237 | 24 % → 0 % | 63.3 px | 0.00 | 0.00 | 0 |
| stroke 238 | 29 % → 0 % | 70.7 px | 0.00 | 0.00 | 1 |
| stroke 239 | 41 % → 0 % | 111.5 px | 0.00 | 0.00 | 0 |
| stroke 240 | 17 % → 0 % | 48.6 px | 0.00 | 0.00 | 1 |
| stroke 241 | 9 % → 0 % | 13.6 px | 0.00 | 0.00 | 6 |
| stroke 242 | 10 % → 0 % | 15.3 px | 0.00 | 0.00 | 16 |
| stroke 243 | 20 % → 0 % | 29.8 px | 0.00 | 0.00 | 15 |
| stroke 244 | 9 % → 0 % | 12.7 px | 0.00 | 0.00 | 6 |
| stroke 245 | 20 % → 0 % | 32.8 px | 0.00 | 0.00 | 8 |
| stroke 246 | 21 % → 0 % | 39.7 px | 0.00 | 0.00 | 1 |
| stroke 247 | 26 % → 0 % | 44.0 px | 0.00 | 0.00 | 7 |
| stroke 248 | 18 % → 0 % | 45.1 px | 0.00 | 0.00 | 1 |
| stroke 249 | 35 % → 0 % | 53.8 px | 0.00 | 0.00 | 5 |
| stroke 250 | 19 % → 0 % | 43.1 px | 0.00 | 0.00 | 1 |
| stroke 251 | 28 % → 0 % | 38.0 px | 0.00 | 0.00 | 4 |
| stroke 252 | 32 % → 0 % | 50.9 px | 0.00 | 0.00 | 3 |
| stroke 253 | 53 % → 0 % | 102.2 px | 0.00 | 0.00 | 2 |
| stroke 254 | 47 % → 0 % | 134.1 px | 0.00 | 0.00 | 0 |
| stroke 255 | 41 % → 0 % | 93.9 px | 0.00 | 0.00 | 3 |
| stroke 256 | 29 % → 0 % | 70.7 px | 0.00 | 0.00 | 1 |
| stroke 257 | 46 % → 0 % | 121.0 px | 0.00 | 0.00 | 0 |
| stroke 258 | 62 % → 0 % | 176.2 px | 0.00 | 0.00 | 0 |
| stroke 259 | 9 % → 0 % | 12.5 px | 0.00 | 0.00 | 5 |
| stroke 260 | 21 % → 0 % | 25.5 px | 0.00 | 0.00 | 5 |
| stroke 261 | 20 % → 0 % | 54.8 px | 0.00 | 0.00 | 1 |
| stroke 262 | 7 % → 0 % | 14.7 px | 0.00 | 0.00 | 2 |
| stroke 263 | 13 % → 0 % | 35.8 px | 0.00 | 0.00 | 0 |
| stroke 264 | 20 % → 0 % | 37.8 px | 0.00 | 0.00 | 2 |
| stroke 265 | 6 % → 0 % | 10.8 px | 0.00 | 0.00 | 5 |
| stroke 266 | 15 % → 0 % | 40.5 px | 0.00 | 0.00 | 0 |
| stroke 267 | 9 % → 0 % | 13.3 px | 0.00 | 0.00 | 7 |
| stroke 268 | 9 % → 0 % | 22.7 px | 0.00 | 0.00 | 1 |
| stroke 269 | 21 % → 0 % | 36.8 px | 0.00 | 0.00 | 5 |
| stroke 270 | 22 % → 0 % | 49.2 px | 0.00 | 0.00 | 1 |
| stroke 271 | 9 % → 0 % | 10.5 px | 0.00 | 0.00 | 12 |
| stroke 272 | 14 % → 0 % | 34.2 px | 0.00 | 0.00 | 3 |
| stroke 273 | 22 % → 0 % | 24.4 px | 0.00 | 0.00 | 10 |
| stroke 274 | 15 % → 0 % | 22.4 px | 0.00 | 0.00 | 5 |
| stroke 275 | 32 % → 0 % | 64.4 px | 0.00 | 0.00 | 3 |
| stroke 276 | 25 % → 0 % | 55.3 px | 0.00 | 0.00 | 1 |
| stroke 277 | 34 % → 0 % | 79.7 px | 0.00 | 0.00 | 2 |
| stroke 278 | 49 % → 0 % | 75.4 px | 0.00 | 0.00 | 3 |
| stroke 279 | 50 % → 0 % | 94.3 px | 0.00 | 0.00 | 1 |
| stroke 280 | 30 % → 0 % | 55.5 px | 0.00 | 0.00 | 1 |
| stroke 281 | 10 % → 0 % | 10.4 px | 0.00 | 0.00 | 10 |
| stroke 282 | 15 % → 0 % | 16.0 px | 0.00 | 0.00 | 8 |
| stroke 283 | 10 % → 0 % | 9.0 px | 0.00 | 0.00 | 10 |
| stroke 284 | 21 % → 0 % | 36.7 px | 0.00 | 0.00 | 3 |
| stroke 285 | 14 % → 0 % | 15.6 px | 0.00 | 0.00 | 3 |
| stroke 286 | 19 % → 0 % | 14.8 px | 0.00 | 0.00 | 10 |
| stroke 287 | 26 % → 0 % | 26.1 px | 0.00 | 0.00 | 13 |
| stroke 288 | 7 % → 0 % | 11.1 px | 0.00 | 0.00 | 5 |
| stroke 289 | 8 % → 0 % | 11.7 px | 0.00 | 0.00 | 1 |
| stroke 290 | 19 % → 0 % | 25.1 px | 0.00 | 0.00 | 5 |
| stroke 291 | 31 % → 0 % | 68.4 px | 0.00 | 0.00 | 2 |
| stroke 292 | 27 % → 0 % | 45.2 px | 0.00 | 0.00 | 2 |
| stroke 293 | 20 % → 0 % | 28.4 px | 0.00 | 0.00 | 3 |
| stroke 294 | 25 % → 0 % | 38.9 px | 0.00 | 0.00 | 2 |
| stroke 295 | 20 % → 0 % | 48.4 px | 0.00 | 0.00 | 1 |
| stroke 296 | 31 % → 0 % | 61.7 px | 0.00 | 0.00 | 2 |
| stroke 297 | 29 % → 0 % | 69.8 px | 0.00 | 0.00 | 1 |
| stroke 298 | 24 % → 0 % | 43.0 px | 0.00 | 0.00 | 3 |
| stroke 299 | 38 % → 0 % | 57.7 px | 0.00 | 0.00 | 9 |
| stroke 300 | 23 % → 0 % | 46.8 px | 0.00 | 0.00 | 1 |
| stroke 301 | 28 % → 0 % | 61.7 px | 0.00 | 0.00 | 2 |
| stroke 302 | 58 % → 0 % | 120.8 px | 0.00 | 0.00 | 2 |
| stroke 303 | 53 % → 0 % | 85.5 px | 0.00 | 0.00 | 1 |
| stroke 304 | 40 % → 0 % | 101.5 px | 0.00 | 0.00 | 0 |
| stroke 305 | 52 % → 0 % | 87.7 px | 0.00 | 0.00 | 2 |
| stroke 306 | 47 % → 0 % | 130.0 px | 0.00 | 0.00 | 2 |
| stroke 307 | 7 % → 0 % | 12.2 px | 0.00 | 0.00 | 2 |
| stroke 308 | 12 % → 0 % | 27.0 px | 0.00 | 0.00 | 0 |
| stroke 309 | 8 % → 0 % | 12.9 px | 0.00 | 0.00 | 2 |
| stroke 310 | 12 % → 0 % | 19.3 px | 0.00 | 0.00 | 7 |
| stroke 311 | 6 % → 0 % | 11.8 px | 0.00 | 0.00 | 1 |
| stroke 312 | 9 % → 0 % | 12.5 px | 0.00 | 0.00 | 7 |
| stroke 313 | 22 % → 0 % | 34.5 px | 0.00 | 0.00 | 6 |
| stroke 314 | 26 % → 0 % | 39.0 px | 0.00 | 0.00 | 2 |
| stroke 315 | 33 % → 0 % | 73.0 px | 0.00 | 0.00 | 2 |
| stroke 316 | 38 % → 0 % | 60.3 px | 0.00 | 0.00 | 3 |
| stroke 317 | 40 % → 0 % | 110.8 px | 0.00 | 0.00 | 1 |
| stroke 318 | 35 % → 0 % | 100.3 px | 0.00 | 0.00 | 1 |
| stroke 319 | 5 % → 0 % | 15.2 px | 0.00 | 0.00 | 1 |
| stroke 320 | 12 % → 1 % | 14.2 px | 0.19 | 0.12 | 2 |
| stroke 321 | 19 % → 1 % | 15.4 px | 0.19 | 0.03 | 4 |
| stroke 322 | 28 % → 3 % | 59.6 px | 0.19 | 0.10 | 0 |
| stroke 323 | 6 % → 11 % | 14.0 px | 0.19 | 1.76 | 5 |
| stroke 324 | 11 % → 0 % | 17.9 px | 0.17 | 0.02 | 3 |
| stroke 325 | 15 % → 0 % | 43.1 px | 0.00 | 0.00 | 0 |
| stroke 326 | 17 % → 17 % | 38.3 px | 0.19 | 0.98 | 1 |
| stroke 327 | 27 % → 0 % | 61.1 px | 0.00 | 0.00 | 5 |
| stroke 328 | 6 % → 2 % | 11.3 px | 0.19 | 0.25 | 2 |
| stroke 329 | 13 % → 11 % | 18.8 px | 0.17 | 0.86 | 10 |
| stroke 330 | 21 % → 21 % | 40.1 px | 0.18 | 1.00 | 1 |
| stroke 331 | 25 % → 2 % | 54.6 px | 0.14 | 0.06 | 1 |
| stroke 332 | 21 % → 25 % | 40.9 px | 0.17 | 1.18 | 2 |
| stroke 333 | 35 % → 7 % | 84.8 px | 0.19 | 0.20 | 2 |
| stroke 334 | 5 % → 0 % | 14.7 px | 0.00 | 0.00 | 0 |
| stroke 335 | 12 % → 0 % | 22.8 px | 0.00 | 0.00 | 1 |
| stroke 336 | 19 % → 5 % | 36.7 px | 0.16 | 0.25 | 1 |
| stroke 337 | 17 % → 0 % | 47.8 px | 0.00 | 0.00 | 0 |
| stroke 338 | 10 % → 29 % | 16.1 px | 0.15 | 2.93 | 4 |
| stroke 339 | 11 % → 0 % | 15.0 px | 0.00 | 0.00 | 1 |
| stroke 340 | 6 % → 45 % | 11.0 px | 0.16 | 7.21 | 1 |
| stroke 341 | 12 % → 0 % | 17.0 px | 0.00 | 0.00 | 1 |
| stroke 342 | 15 % → 0 % | 27.0 px | 0.00 | 0.00 | 4 |
| stroke 343 | 28 % → 0 % | 23.5 px | 0.00 | 0.00 | 2 |
| stroke 344 | 6 % → 0 % | 13.1 px | 0.00 | 0.00 | 2 |
| stroke 345 | 13 % → 0 % | 35.8 px | 0.00 | 0.00 | 0 |
| stroke 346 | 5 % → 0 % | 14.5 px | 0.00 | 0.00 | 0 |
| stroke 347 | 5 % → 0 % | 13.2 px | 0.00 | 0.00 | 2 |
| stroke 348 | 10 % → 0 % | 12.2 px | 0.00 | 0.00 | 10 |
| stroke 349 | 7 % → 0 % | 11.0 px | 0.00 | 0.00 | 16 |
| stroke 350 | 8 % → 0 % | 11.5 px | 0.00 | 0.00 | 14 |
| stroke 351 | 15 % → 0 % | 18.5 px | 0.00 | 0.00 | 8 |
| stroke 352 | 13 % → 0 % | 20.3 px | 0.00 | 0.00 | 13 |
| stroke 353 | 17 % → 0 % | 25.9 px | 0.00 | 0.00 | 9 |
| stroke 354 | 7 % → 0 % | 9.5 px | 0.00 | 0.00 | 7 |
| stroke 355 | 8 % → 0 % | 14.2 px | 0.00 | 0.00 | 4 |
| stroke 356 | 16 % → 0 % | 23.4 px | 0.00 | 0.00 | 5 |
| stroke 357 | 25 % → 0 % | 50.7 px | 0.00 | 0.00 | 1 |
| stroke 358 | 9 % → 0 % | 15.5 px | 0.00 | 0.00 | 3 |
| stroke 359 | 7 % → 0 % | 12.1 px | 0.00 | 0.00 | 12 |
| stroke 360 | 20 % → 0 % | 30.3 px | 0.00 | 0.00 | 4 |
| stroke 361 | 9 % → 0 % | 9.6 px | 0.00 | 0.00 | 10 |
| stroke 362 | 36 % → 0 % | 69.6 px | 0.00 | 0.00 | 4 |
| stroke 363 | 33 % → 0 % | 52.7 px | 0.00 | 0.00 | 12 |
| stroke 364 | 14 % → 0 % | 21.2 px | 0.00 | 0.00 | 8 |
| stroke 365 | 28 % → 0 % | 43.9 px | 0.00 | 0.00 | 14 |
| stroke 366 | 34 % → 0 % | 58.7 px | 0.00 | 0.00 | 3 |
| stroke 367 | 26 % → 0 % | 32.0 px | 0.00 | 0.00 | 10 |
| stroke 368 | 34 % → 0 % | 60.1 px | 0.00 | 0.00 | 1 |
| stroke 369 | 40 % → 0 % | 65.5 px | 0.00 | 0.00 | 5 |
| stroke 370 | 36 % → 0 % | 54.0 px | 0.00 | 0.00 | 7 |
| stroke 371 | 25 % → 0 % | 37.6 px | 0.00 | 0.00 | 5 |
| stroke 372 | 17 % → 0 % | 28.8 px | 0.00 | 0.00 | 2 |
| stroke 373 | 28 % → 0 % | 57.3 px | 0.00 | 0.00 | 1 |
| stroke 374 | 16 % → 0 % | 21.2 px | 0.00 | 0.00 | 5 |
| stroke 375 | 18 % → 0 % | 27.2 px | 0.00 | 0.00 | 8 |
| stroke 376 | 42 % → 0 % | 66.3 px | 0.00 | 0.00 | 3 |
| stroke 377 | 36 % → 0 % | 57.2 px | 0.00 | 0.00 | 2 |
| stroke 378 | 21 % → 0 % | 30.6 px | 0.00 | 0.00 | 4 |
| stroke 379 | 27 % → 0 % | 48.7 px | 0.00 | 0.00 | 4 |
| stroke 380 | 20 % → 0 % | 27.6 px | 0.00 | 0.00 | 9 |
| stroke 381 | 42 % → 0 % | 102.5 px | 0.00 | 0.00 | 2 |
| stroke 382 | 53 % → 0 % | 87.1 px | 0.00 | 0.00 | 6 |
| stroke 383 | 51 % → 0 % | 104.8 px | 0.00 | 0.00 | 7 |
| stroke 384 | 34 % → 0 % | 54.2 px | 0.00 | 0.00 | 2 |
| stroke 385 | 32 % → 0 % | 74.1 px | 0.00 | 0.00 | 2 |
| stroke 386 | 52 % → 0 % | 97.7 px | 0.00 | 0.00 | 2 |
| stroke 387 | 34 % → 0 % | 52.6 px | 0.00 | 0.00 | 13 |
| stroke 388 | 22 % → 0 % | 36.9 px | 0.00 | 0.00 | 2 |
| stroke 389 | 38 % → 0 % | 77.8 px | 0.00 | 0.00 | 1 |
| stroke 390 | 45 % → 0 % | 91.9 px | 0.00 | 0.00 | 2 |
| stroke 391 | 49 % → 0 % | 94.5 px | 0.00 | 0.00 | 4 |
| stroke 392 | 14 % → 0 % | 32.0 px | 0.00 | 0.00 | 1 |
| stroke 393 | 16 % → 0 % | 34.6 px | 0.00 | 0.00 | 2 |
| stroke 394 | 58 % → 0 % | 154.0 px | 0.00 | 0.00 | 0 |
| stroke 395 | 47 % → 0 % | 86.3 px | 0.00 | 0.00 | 1 |
| stroke 396 | 27 % → 0 % | 75.5 px | 0.00 | 0.00 | 0 |
| stroke 397 | 39 % → 0 % | 93.5 px | 0.00 | 0.00 | 1 |
| stroke 398 | 17 % → 0 % | 37.0 px | 0.00 | 0.00 | 1 |
| stroke 399 | 21 % → 0 % | 61.8 px | 0.00 | 0.00 | 0 |
| stroke 400 | 47 % → 0 % | 132.8 px | 0.00 | 0.00 | 1 |
| stroke 401 | 68 % → 0 % | 193.6 px | 0.00 | 0.00 | 0 |
| stroke 402 | 37 % → 0 % | 99.7 px | 0.00 | 0.00 | 0 |
| stroke 403 | 74 % → 0 % | 163.6 px | 0.00 | 0.00 | 1 |
| stroke 404 | 46 % → 0 % | 102.2 px | 0.00 | 0.00 | 1 |
| stroke 405 | 32 % → 0 % | 77.9 px | 0.00 | 0.00 | 1 |
| stroke 406 | 38 % → 0 % | 82.7 px | 0.00 | 0.00 | 1 |
| stroke 407 | 52 % → 0 % | 148.5 px | 0.00 | 0.00 | 1 |
| stroke 408 | 43 % → 0 % | 106.2 px | 0.00 | 0.00 | 1 |
| stroke 409 | 45 % → 0 % | 125.0 px | 0.00 | 0.00 | 1 |
| stroke 410 | 51 % → 0 % | 143.0 px | 0.00 | 0.00 | 1 |
| stroke 411 | 4 % → 0 % | 10.7 px | 0.00 | 0.00 | 0 |
| stroke 412 | 7 % → 0 % | 11.3 px | 0.00 | 0.00 | 5 |
| stroke 413 | 9 % → 0 % | 14.5 px | 0.00 | 0.00 | 3 |
| stroke 414 | 13 % → 0 % | 20.3 px | 0.00 | 0.00 | 8 |
| stroke 415 | 20 % → 0 % | 40.7 px | 0.00 | 0.00 | 2 |
| stroke 416 | 13 % → 0 % | 23.4 px | 0.00 | 0.00 | 2 |
| stroke 417 | 26 % → 0 % | 53.2 px | 0.00 | 0.00 | 1 |
| stroke 418 | 31 % → 0 % | 49.4 px | 0.00 | 0.00 | 3 |
| stroke 419 | 33 % → 0 % | 57.7 px | 0.00 | 0.00 | 3 |
| stroke 420 | 31 % → 0 % | 56.7 px | 0.00 | 0.00 | 2 |
| stroke 421 | 44 % → 0 % | 80.3 px | 0.00 | 0.00 | 2 |
| stroke 422 | 22 % → 0 % | 53.1 px | 0.00 | 0.00 | 1 |
| stroke 423 | 51 % → 0 % | 105.8 px | 0.00 | 0.00 | 3 |
| stroke 424 | 41 % → 0 % | 110.7 px | 0.00 | 0.00 | 2 |
| stroke 425 | 39 % → 0 % | 79.8 px | 0.00 | 0.00 | 1 |
| stroke 426 | 28 % → 0 % | 79.2 px | 0.00 | 0.00 | 1 |
| stroke 427 | 30 % → 0 % | 80.9 px | 0.00 | 0.00 | 0 |
| stroke 428 | 28 % → 0 % | 77.9 px | 0.00 | 0.00 | 0 |
| stroke 429 | 45 % → 0 % | 122.1 px | 0.00 | 0.00 | 0 |
| stroke 430 | 6 % → 0 % | 12.9 px | 0.00 | 0.00 | 3 |
| stroke 431 | 12 % → 0 % | 25.5 px | 0.00 | 0.00 | 1 |
| stroke 432 | 8 % → 0 % | 11.9 px | 0.00 | 0.00 | 2 |
| stroke 433 | 16 % → 0 % | 32.9 px | 0.00 | 0.00 | 3 |
| stroke 434 | 20 % → 0 % | 35.0 px | 0.00 | 0.00 | 3 |
| stroke 435 | 12 % → 0 % | 12.8 px | 0.00 | 0.00 | 6 |
| stroke 436 | 29 % → 0 % | 39.4 px | 0.00 | 0.00 | 6 |
| stroke 437 | 22 % → 0 % | 51.8 px | 0.00 | 0.00 | 3 |
| stroke 438 | 10 % → 0 % | 13.4 px | 0.00 | 0.00 | 15 |
| stroke 439 | 10 % → 0 % | 12.2 px | 0.00 | 0.00 | 2 |
| stroke 440 | 19 % → 0 % | 20.1 px | 0.00 | 0.00 | 3 |
| stroke 441 | 14 % → 0 % | 11.7 px | 0.00 | 0.00 | 3 |
| stroke 442 | 20 % → 0 % | 41.3 px | 0.00 | 0.00 | 0 |
| stroke 443 | 16 % → 0 % | 34.8 px | 0.00 | 0.00 | 1 |
| stroke 444 | 40 % → 0 % | 37.3 px | 0.00 | 0.00 | 2 |
| stroke 445 | 23 % → 0 % | 49.5 px | 0.00 | 0.00 | 1 |
| stroke 446 | 15 % → 0 % | 30.3 px | 0.00 | 0.00 | 1 |
| stroke 447 | 13 % → 0 % | 21.7 px | 0.00 | 0.00 | 3 |
| stroke 448 | 25 % → 0 % | 71.3 px | 0.00 | 0.00 | 0 |
| stroke 449 | 10 % → 0 % | 15.0 px | 0.00 | 0.00 | 14 |
| stroke 450 | 8 % → 0 % | 10.8 px | 0.00 | 0.00 | 7 |
| stroke 451 | 14 % → 0 % | 21.7 px | 0.00 | 0.00 | 10 |
| stroke 452 | 7 % → 0 % | 11.7 px | 0.00 | 0.00 | 5 |
| stroke 453 | 7 % → 0 % | 10.0 px | 0.00 | 0.00 | 6 |
| stroke 454 | 20 % → 0 % | 35.5 px | 0.00 | 0.00 | 1 |
| stroke 455 | 10 % → 0 % | 15.2 px | 0.00 | 0.00 | 2 |
| stroke 456 | 29 % → 0 % | 48.0 px | 0.00 | 0.00 | 3 |
| stroke 457 | 14 % → 0 % | 18.5 px | 0.00 | 0.00 | 3 |
| stroke 458 | 22 % → 0 % | 27.3 px | 0.00 | 0.00 | 5 |
| stroke 459 | 7 % → 0 % | 9.5 px | 0.00 | 0.00 | 10 |
| stroke 460 | 21 % → 0 % | 29.9 px | 0.00 | 0.00 | 21 |
| stroke 461 | 35 % → 0 % | 78.7 px | 0.00 | 0.00 | 2 |
| stroke 462 | 18 % → 0 % | 22.1 px | 0.00 | 0.00 | 19 |
| stroke 463 | 16 % → 0 % | 40.1 px | 0.00 | 0.00 | 2 |
| stroke 464 | 23 % → 0 % | 28.8 px | 0.00 | 0.00 | 10 |
| stroke 465 | 28 % → 0 % | 35.1 px | 0.00 | 0.00 | 10 |
| stroke 466 | 21 % → 0 % | 26.0 px | 0.00 | 0.00 | 5 |
| stroke 467 | 22 % → 0 % | 31.1 px | 0.00 | 0.00 | 6 |
| stroke 468 | 34 % → 0 % | 54.3 px | 0.00 | 0.00 | 5 |
| stroke 469 | 40 % → 0 % | 64.6 px | 0.00 | 0.00 | 22 |
| stroke 470 | 33 % → 0 % | 53.7 px | 0.00 | 0.00 | 4 |
| stroke 471 | 37 % → 0 % | 46.4 px | 0.00 | 0.00 | 8 |
| stroke 472 | 34 % → 0 % | 46.9 px | 0.00 | 0.00 | 5 |
| stroke 473 | 32 % → 0 % | 36.4 px | 0.00 | 0.00 | 15 |
| stroke 474 | 25 % → 0 % | 38.2 px | 0.00 | 0.00 | 4 |
| stroke 475 | 21 % → 0 % | 47.4 px | 0.00 | 0.00 | 1 |
| stroke 476 | 29 % → 0 % | 77.3 px | 0.00 | 0.00 | 16 |
| stroke 477 | 24 % → 0 % | 63.1 px | 0.00 | 0.00 | 7 |
| stroke 478 | 30 % → 0 % | 43.9 px | 0.00 | 0.00 | 2 |
| stroke 479 | 37 % → 0 % | 89.4 px | 0.00 | 0.00 | 1 |
| stroke 480 | 31 % → 0 % | 58.5 px | 0.00 | 0.00 | 1 |
| stroke 481 | 21 % → 0 % | 60.4 px | 0.00 | 0.00 | 1 |
| stroke 482 | 52 % → 0 % | 124.8 px | 0.00 | 0.00 | 1 |
| stroke 483 | 42 % → 0 % | 68.0 px | 0.00 | 0.00 | 4 |
| stroke 484 | 50 % → 0 % | 121.6 px | 0.00 | 0.00 | 2 |
| stroke 485 | 56 % → 0 % | 93.6 px | 0.00 | 0.00 | 1 |
| stroke 486 | 21 % → 0 % | 45.6 px | 0.00 | 0.00 | 1 |
| stroke 487 | 56 % → 0 % | 150.4 px | 0.00 | 0.00 | 0 |
| stroke 488 | 35 % → 0 % | 71.7 px | 0.00 | 0.00 | 8 |
| stroke 489 | 26 % → 0 % | 57.2 px | 0.00 | 0.00 | 1 |
| stroke 490 | 41 % → 0 % | 96.2 px | 0.00 | 0.00 | 2 |
| stroke 491 | 34 % → 0 % | 95.6 px | 0.00 | 0.00 | 0 |
| stroke 492 | 43 % → 0 % | 115.9 px | 0.00 | 0.00 | 0 |
| stroke 493 | 10 % → 0 % | 13.4 px | 0.00 | 0.00 | 3 |
| stroke 494 | 11 % → 0 % | 11.6 px | 0.00 | 0.00 | 13 |
| stroke 495 | 14 % → 0 % | 17.8 px | 0.00 | 0.00 | 9 |
| stroke 496 | 25 % → 0 % | 25.9 px | 0.00 | 0.00 | 4 |
| stroke 497 | 25 % → 0 % | 49.1 px | 0.00 | 0.00 | 1 |
| stroke 498 | 17 % → 0 % | 19.6 px | 0.00 | 0.00 | 4 |
| stroke 499 | 26 % → 0 % | 68.2 px | 0.00 | 0.00 | 1 |
| stroke 500 | 13 % → 0 % | 24.0 px | 0.00 | 0.00 | 2 |
| stroke 501 | 17 % → 0 % | 42.7 px | 0.00 | 0.00 | 0 |
| stroke 502 | 25 % → 0 % | 39.1 px | 0.00 | 0.00 | 1 |
| stroke 503 | 22 % → 0 % | 42.6 px | 0.00 | 0.00 | 1 |
| stroke 504 | 50 % → 0 % | 74.2 px | 0.00 | 0.00 | 8 |
| stroke 505 | 30 % → 0 % | 78.1 px | 0.00 | 0.00 | 1 |
| stroke 506 | 43 % → 0 % | 101.9 px | 0.00 | 0.00 | 1 |
| stroke 507 | 6 % → 0 % | 13.5 px | 0.00 | 0.00 | 1 |
| stroke 508 | 7 % → 0 % | 12.3 px | 0.00 | 0.00 | 6 |
| stroke 509 | 13 % → 0 % | 22.5 px | 0.00 | 0.00 | 8 |
| stroke 510 | 26 % → 0 % | 71.7 px | 0.00 | 0.00 | 1 |
| stroke 511 | 9 % → 0 % | 21.3 px | 0.00 | 0.00 | 1 |
| stroke 512 | 6 % → 0 % | 13.3 px | 0.00 | 0.00 | 1 |
| stroke 513 | 12 % → 0 % | 21.2 px | 0.00 | 0.00 | 1 |
| stroke 514 | 5 % → 0 % | 11.9 px | 0.00 | 0.00 | 2 |
| stroke 515 | 14 % → 0 % | 38.5 px | 0.00 | 0.00 | 3 |
| stroke 516 | 10 % → 0 % | 12.0 px | 0.00 | 0.00 | 6 |
| stroke 517 | 7 % → 0 % | 12.0 px | 0.00 | 0.00 | 2 |
| stroke 518 | 20 % → 0 % | 19.2 px | 0.00 | 0.00 | 5 |
| stroke 519 | 16 % → 0 % | 35.6 px | 0.00 | 0.00 | 2 |
| stroke 520 | 35 % → 0 % | 40.5 px | 0.00 | 0.00 | 3 |
| stroke 521 | 13 % → 0 % | 33.5 px | 0.00 | 0.00 | 1 |
| stroke 522 | 9 % → 0 % | 11.4 px | 0.00 | 0.00 | 11 |
| stroke 523 | 22 % → 0 % | 49.4 px | 0.00 | 0.00 | 3 |
| stroke 524 | 14 % → 0 % | 36.4 px | 0.00 | 0.00 | 0 |
| stroke 525 | 10 % → 0 % | 11.8 px | 0.00 | 0.00 | 2 |
| stroke 526 | 11 % → 0 % | 16.5 px | 0.00 | 0.00 | 4 |
| stroke 527 | 21 % → 0 % | 32.7 px | 0.00 | 0.00 | 3 |
| stroke 528 | 25 % → 0 % | 39.7 px | 0.00 | 0.00 | 2 |
| stroke 529 | 29 % → 0 % | 38.3 px | 0.00 | 0.00 | 7 |
| stroke 530 | 18 % → 0 % | 35.7 px | 0.00 | 0.00 | 1 |
| stroke 531 | 5 % → 0 % | 12.8 px | 0.00 | 0.00 | 2 |
| stroke 532 | 11 % → 0 % | 16.2 px | 0.00 | 0.00 | 4 |
| stroke 533 | 21 % → 0 % | 46.4 px | 0.00 | 0.00 | 3 |
| stroke 534 | 23 % → 0 % | 60.5 px | 0.00 | 0.00 | 0 |
| stroke 535 | 8 % → 0 % | 12.1 px | 0.00 | 0.00 | 3 |
| stroke 536 | 13 % → 0 % | 17.9 px | 0.00 | 0.00 | 5 |
| stroke 537 | 23 % → 0 % | 46.8 px | 0.00 | 0.00 | 1 |
| stroke 538 | 15 % → 0 % | 39.0 px | 0.00 | 0.00 | 2 |
| stroke 539 | 36 % → 0 % | 94.9 px | 0.00 | 0.00 | 0 |
| stroke 540 | 31 % → 0 % | 82.9 px | 0.00 | 0.00 | 0 |
| stroke 541 | 8 % → 0 % | 21.4 px | 0.00 | 0.00 | 0 |
| stroke 542 | 8 % → 0 % | 19.7 px | 0.00 | 0.00 | 3 |
| stroke 543 | 5 % → 0 % | 13.5 px | 0.00 | 0.00 | 0 |
| stroke 544 | 12 % → 0 % | 27.1 px | 0.00 | 0.00 | 2 |
| stroke 545 | 16 % → 0 % | 40.6 px | 0.00 | 0.00 | 0 |
| stroke 546 | 7 % → 0 % | 13.5 px | 0.00 | 0.00 | 2 |
| stroke 547 | 15 % → 0 % | 9.5 px | 0.00 | 0.00 | 5 |
| stroke 548 | 12 % → 0 % | 10.1 px | 0.00 | 0.00 | 11 |
| stroke 549 | 30 % → 0 % | 18.4 px | 0.00 | 0.00 | 10 |
| stroke 550 | 22 % → 0 % | 51.6 px | 0.00 | 0.00 | 0 |
| stroke 551 | 29 % → 0 % | 36.0 px | 0.00 | 0.00 | 0 |
| stroke 552 | 24 % → 0 % | 54.9 px | 0.00 | 0.00 | 1 |
| stroke 553 | 28 % → 0 % | 32.8 px | 0.00 | 0.00 | 4 |
| stroke 554 | 13 % → 0 % | 19.6 px | 0.00 | 0.00 | 1 |
| stroke 555 | 35 % → 0 % | 60.3 px | 0.00 | 0.00 | 1 |
| stroke 556 | 9 % → 0 % | 12.5 px | 0.00 | 0.00 | 3 |
| stroke 557 | 16 % → 0 % | 15.6 px | 0.00 | 0.00 | 2 |
| stroke 558 | 8 % → 0 % | 11.2 px | 0.00 | 0.00 | 16 |
| stroke 559 | 12 % → 0 % | 19.2 px | 0.00 | 0.00 | 9 |
| stroke 560 | 16 % → 0 % | 33.9 px | 0.00 | 0.00 | 1 |
| stroke 561 | 11 % → 0 % | 18.7 px | 0.00 | 0.00 | 2 |
| stroke 562 | 29 % → 0 % | 53.5 px | 0.00 | 0.00 | 2 |
| stroke 563 | 12 % → 0 % | 21.4 px | 0.00 | 0.00 | 2 |
| stroke 564 | 12 % → 0 % | 19.1 px | 0.00 | 0.00 | 3 |
| stroke 565 | 21 % → 0 % | 29.3 px | 0.00 | 0.00 | 3 |
| stroke 566 | 35 % → 0 % | 55.9 px | 0.00 | 0.00 | 6 |
| stroke 567 | 30 % → 0 % | 82.0 px | 0.00 | 0.00 | 1 |
| stroke 568 | 15 % → 0 % | 41.0 px | 0.00 | 0.00 | 1 |
| stroke 569 | 52 % → 0 % | 132.7 px | 0.00 | 0.00 | 3 |
| stroke 570 | 27 % → 0 % | 77.1 px | 0.00 | 0.00 | 0 |
| stroke 571 | 10 % → 0 % | 12.1 px | 0.00 | 0.00 | 12 |
| stroke 572 | 8 % → 0 % | 11.2 px | 0.00 | 0.00 | 3 |
| stroke 573 | 7 % → 7 % | 10.8 px | 0.19 | 1.00 | 6 |
| stroke 574 | 17 % → 0 % | 29.5 px | 0.00 | 0.00 | 3 |
| stroke 575 | 10 % → 0 % | 16.0 px | 0.00 | 0.00 | 13 |
| stroke 576 | 25 % → 0 % | 33.0 px | 0.00 | 0.00 | 8 |
| stroke 577 | 32 % → 0 % | 52.7 px | 0.00 | 0.00 | 2 |
| stroke 578 | 17 % → 0 % | 23.0 px | 0.00 | 0.00 | 12 |
| stroke 579 | 13 % → 0 % | 18.8 px | 0.00 | 0.00 | 5 |
| stroke 580 | 22 % → 0 % | 34.8 px | 0.00 | 0.00 | 3 |
| stroke 581 | 16 % → 0 % | 35.8 px | 0.00 | 0.00 | 1 |
| stroke 582 | 48 % → 0 % | 105.8 px | 0.00 | 0.00 | 1 |
| stroke 583 | 13 % → 0 % | 20.1 px | 0.00 | 0.00 | 2 |
| stroke 584 | 18 % → 0 % | 42.6 px | 0.00 | 0.00 | 1 |
| stroke 585 | 39 % → 0 % | 62.4 px | 0.00 | 0.00 | 7 |
| stroke 586 | 18 % → 0 % | 51.2 px | 0.00 | 0.00 | 2 |
| stroke 587 | 41 % → 0 % | 80.9 px | 0.00 | 0.00 | 1 |
| stroke 588 | 21 % → 2 % | 55.2 px | 0.19 | 0.11 | 1 |
| stroke 589 | 48 % → 0 % | 53.8 px | 0.00 | 0.00 | 8 |
| stroke 590 | 27 % → 0 % | 41.6 px | 0.00 | 0.00 | 2 |
| stroke 591 | 37 % → 0 % | 103.4 px | 0.00 | 0.00 | 0 |
| stroke 592 | 41 % → 0 % | 110.2 px | 0.00 | 0.00 | 0 |
| stroke 593 | 13 % → 0 % | 16.8 px | 0.00 | 0.00 | 7 |
| stroke 594 | 13 % → 0 % | 21.3 px | 0.00 | 0.00 | 2 |
| stroke 595 | 15 % → 0 % | 24.9 px | 0.00 | 0.00 | 2 |
| stroke 596 | 25 % → 0 % | 30.6 px | 0.00 | 0.00 | 7 |
| stroke 597 | 31 % → 0 % | 41.5 px | 0.00 | 0.00 | 11 |
| stroke 598 | 41 % → 0 % | 68.9 px | 0.00 | 0.00 | 2 |
| stroke 599 | 34 % → 0 % | 86.3 px | 0.00 | 0.00 | 0 |
| stroke 600 | 27 % → 0 % | 43.5 px | 0.00 | 0.00 | 2 |
| stroke 601 | 22 % → 0 % | 53.0 px | 0.00 | 0.00 | 2 |
| stroke 602 | 53 % → 0 % | 149.3 px | 0.00 | 0.00 | 2 |
| stroke 603 | 45 % → 0 % | 126.7 px | 0.00 | 0.00 | 1 |
| stroke 604 | 34 % → 0 % | 95.7 px | 0.00 | 0.00 | 1 |
| stroke 605 | 7 % → 0 % | 11.6 px | 0.00 | 0.00 | 3 |
| stroke 606 | 13 % → 0 % | 18.8 px | 0.00 | 0.00 | 2 |
| stroke 607 | 20 % → 0 % | 37.5 px | 0.00 | 0.00 | 3 |
| stroke 608 | 9 % → 0 % | 12.0 px | 0.00 | 0.00 | 5 |
| stroke 609 | 20 % → 0 % | 20.3 px | 0.00 | 0.00 | 5 |
| stroke 610 | 10 % → 5 % | 18.0 px | 0.13 | 0.54 | 1 |
| stroke 611 | 27 % → 0 % | 30.5 px | 0.00 | 0.00 | 4 |
| stroke 612 | 30 % → 0 % | 39.2 px | 0.12 | 0.01 | 2 |
| stroke 613 | 8 % → 16 % | 12.4 px | 0.19 | 1.87 | 9 |
| stroke 614 | 13 % → 9 % | 24.5 px | 0.19 | 0.71 | 2 |
| stroke 615 | 17 % → 2 % | 19.3 px | 0.19 | 0.13 | 6 |
| stroke 616 | 27 % → 0 % | 35.5 px | 0.00 | 0.00 | 5 |
| stroke 617 | 20 % → 13 % | 37.4 px | 0.19 | 0.62 | 2 |
| stroke 618 | 9 % → 16 % | 10.4 px | 0.15 | 1.83 | 3 |
| stroke 619 | 9 % → 11 % | 14.3 px | 0.13 | 1.16 | 3 |
| stroke 620 | 13 % → 30 % | 21.8 px | 0.14 | 2.24 | 2 |
| stroke 621 | 23 % → 36 % | 54.0 px | 0.15 | 1.57 | 4 |
| stroke 622 | 14 % → 23 % | 25.4 px | 0.15 | 1.63 | 3 |
| stroke 623 | 29 % → 7 % | 77.8 px | 0.14 | 0.26 | 1 |
| stroke 624 | 27 % → 0 % | 66.0 px | 0.12 | 0.02 | 2 |
| stroke 625 | 33 % → 11 % | 72.9 px | 0.13 | 0.34 | 2 |
| stroke 626 | 27 % → 34 % | 65.7 px | 0.16 | 1.25 | 1 |
| stroke 627 | 10 % → 23 % | 17.9 px | 0.19 | 2.22 | 6 |
| stroke 628 | 7 % → 0 % | 11.3 px | 0.00 | 0.00 | 5 |
| stroke 629 | 8 % → 0 % | 11.8 px | 0.00 | 0.00 | 6 |
| stroke 630 | 15 % → 0 % | 33.8 px | 0.00 | 0.00 | 1 |
| stroke 631 | 10 % → 0 % | 16.0 px | 0.00 | 0.00 | 10 |
| stroke 632 | 14 % → 0 % | 21.2 px | 0.00 | 0.00 | 8 |
| stroke 633 | 14 % → 0 % | 24.3 px | 0.00 | 0.00 | 2 |
| stroke 634 | 25 % → 0 % | 37.9 px | 0.00 | 0.00 | 4 |
| stroke 635 | 14 % → 0 % | 21.5 px | 0.00 | 0.00 | 5 |
| stroke 636 | 19 % → 0 % | 53.3 px | 0.00 | 0.00 | 1 |
| stroke 637 | 38 % → 0 % | 76.5 px | 0.00 | 0.00 | 1 |
| stroke 638 | 22 % → 0 % | 36.2 px | 0.00 | 0.00 | 3 |
| stroke 639 | 31 % → 0 % | 55.0 px | 0.00 | 0.00 | 4 |
| stroke 640 | 26 % → 0 % | 54.2 px | 0.00 | 0.00 | 1 |
| stroke 641 | 31 % → 0 % | 51.5 px | 0.00 | 0.00 | 6 |
| stroke 642 | 42 % → 0 % | 119.1 px | 0.00 | 0.00 | 0 |
| stroke 643 | 33 % → 0 % | 67.3 px | 0.00 | 0.00 | 1 |
| stroke 644 | 54 % → 0 % | 91.0 px | 0.00 | 0.00 | 3 |
| stroke 645 | 36 % → 0 % | 87.0 px | 0.00 | 0.00 | 1 |
| stroke 646 | 34 % → 0 % | 75.9 px | 0.00 | 0.00 | 2 |
| stroke 647 | 48 % → 0 % | 116.4 px | 0.00 | 0.00 | 2 |
| stroke 648 | 37 % → 0 % | 76.9 px | 0.00 | 0.00 | 3 |
| stroke 649 | 16 % → 0 % | 26.8 px | 0.00 | 0.00 | 2 |
| stroke 650 | 7 % → 0 % | 12.5 px | 0.00 | 0.00 | 7 |
| stroke 651 | 8 % → 0 % | 10.6 px | 0.00 | 0.00 | 14 |
| stroke 652 | 17 % → 0 % | 27.7 px | 0.00 | 0.00 | 3 |
| stroke 653 | 10 % → 0 % | 16.5 px | 0.00 | 0.00 | 10 |
| stroke 654 | 11 % → 0 % | 16.2 px | 0.00 | 0.00 | 7 |
| stroke 655 | 17 % → 3 % | 28.9 px | 0.12 | 0.17 | 7 |
| stroke 656 | 14 % → 0 % | 22.5 px | 0.00 | 0.00 | 9 |
| stroke 657 | 23 % → 0 % | 50.1 px | 0.00 | 0.00 | 2 |
| stroke 658 | 24 % → 0 % | 41.2 px | 0.00 | 0.00 | 7 |
| stroke 659 | 22 % → 0 % | 57.4 px | 0.00 | 0.00 | 2 |
| stroke 660 | 34 % → 0 % | 82.9 px | 0.00 | 0.00 | 8 |
| stroke 661 | 42 % → 0 % | 73.6 px | 0.00 | 0.00 | 7 |
| stroke 662 | 21 % → 0 % | 44.4 px | 0.00 | 0.00 | 6 |
| stroke 663 | 26 % → 0 % | 63.0 px | 0.00 | 0.00 | 5 |
| stroke 664 | 26 % → 0 % | 42.9 px | 0.00 | 0.00 | 9 |
| stroke 665 | 53 % → 0 % | 129.7 px | 0.00 | 0.00 | 3 |
| stroke 666 | 22 % → 0 % | 61.9 px | 0.00 | 0.00 | 0 |
| stroke 667 | 44 % → 0 % | 122.2 px | 0.00 | 0.00 | 1 |
| stroke 668 | 8 % → 0 % | 10.1 px | 0.00 | 0.00 | 4 |
| stroke 669 | 11 % → 0 % | 16.1 px | 0.00 | 0.00 | 3 |
| stroke 670 | 18 % → 0 % | 23.8 px | 0.19 | 0.03 | 5 |
| stroke 671 | 15 % → 0 % | 37.2 px | 0.00 | 0.00 | 1 |
| stroke 672 | 24 % → 3 % | 66.4 px | 0.19 | 0.11 | 1 |
| stroke 673 | 9 % → 0 % | 18.2 px | 0.00 | 0.00 | 3 |
| stroke 674 | 5 % → 0 % | 13.7 px | 0.00 | 0.00 | 2 |
| stroke 675 | 10 % → 0 % | 22.8 px | 0.00 | 0.00 | 1 |
| stroke 676 | 16 % → 0 % | 40.0 px | 0.00 | 0.00 | 0 |
| stroke 677 | 13 % → 0 % | 38.0 px | 0.00 | 0.00 | 0 |
| stroke 678 | 7 % → 0 % | 11.3 px | 0.00 | 0.00 | 4 |
| stroke 679 | 8 % → 0 % | 14.8 px | 0.00 | 0.00 | 4 |
| stroke 680 | 7 % → 0 % | 12.8 px | 0.00 | 0.00 | 6 |
| stroke 681 | 15 % → 0 % | 10.0 px | 0.00 | 0.00 | 15 |
| stroke 682 | 15 % → 0 % | 12.5 px | 0.00 | 0.00 | 15 |
| stroke 683 | 27 % → 0 % | 26.6 px | 0.00 | 0.00 | 8 |
| stroke 684 | 35 % → 0 % | 41.7 px | 0.00 | 0.00 | 4 |
| stroke 685 | 18 % → 0 % | 25.2 px | 0.00 | 0.00 | 3 |
| stroke 686 | 25 % → 0 % | 59.9 px | 0.00 | 0.00 | 1 |
| stroke 687 | 12 % → 0 % | 10.5 px | 0.00 | 0.00 | 13 |
| stroke 688 | 25 % → 0 % | 40.4 px | 0.00 | 0.00 | 3 |
| stroke 689 | 37 % → 0 % | 65.3 px | 0.00 | 0.00 | 1 |
| stroke 690 | 36 % → 0 % | 94.8 px | 0.00 | 0.00 | 3 |
| stroke 691 | 46 % → 0 % | 116.2 px | 0.00 | 0.00 | 0 |
| stroke 692 | 44 % → 0 % | 81.4 px | 0.00 | 0.00 | 0 |
| stroke 693 | 39 % → 0 % | 106.5 px | 0.00 | 0.00 | 0 |
| stroke 694 | 7 % → 0 % | 16.1 px | 0.00 | 0.00 | 2 |
| stroke 695 | 12 % → 0 % | 25.4 px | 0.00 | 0.00 | 1 |
| stroke 696 | 7 % → 0 % | 8.9 px | 0.00 | 0.00 | 2 |
| stroke 697 | 8 % → 0 % | 15.4 px | 0.00 | 0.00 | 4 |
| stroke 698 | 18 % → 0 % | 34.9 px | 0.00 | 0.00 | 1 |
| stroke 699 | 15 % → 0 % | 30.8 px | 0.00 | 0.00 | 1 |
| stroke 700 | 18 % → 0 % | 49.6 px | 0.00 | 0.00 | 1 |
| stroke 701 | 6 % → 0 % | 12.8 px | 0.00 | 0.00 | 1 |
| stroke 702 | 8 % → 12 % | 13.0 px | 0.16 | 1.46 | 5 |
| stroke 703 | 15 % → 0 % | 13.1 px | 0.00 | 0.00 | 3 |
| stroke 704 | 5 % → 0 % | 14.8 px | 0.00 | 0.00 | 0 |
| stroke 705 | 5 % → 0 % | 11.7 px | 0.00 | 0.00 | 1 |
| stroke 706 | 9 % → 13 % | 10.8 px | 0.16 | 1.50 | 6 |
| stroke 707 | 13 % → 10 % | 12.9 px | 0.19 | 0.79 | 11 |
| stroke 708 | 11 % → 0 % | 11.6 px | 0.00 | 0.00 | 5 |
| stroke 709 | 22 % → 2 % | 43.3 px | 0.19 | 0.08 | 2 |
| stroke 710 | 25 % → 0 % | 29.0 px | 0.00 | 0.00 | 3 |
| stroke 711 | 8 % → 8 % | 12.6 px | 0.19 | 0.95 | 5 |
| stroke 712 | 30 % → 4 % | 46.3 px | 0.18 | 0.13 | 3 |
| stroke 713 | 21 % → 5 % | 33.8 px | 0.19 | 0.23 | 3 |
| stroke 714 | 43 % → 0 % | 72.5 px | 0.00 | 0.00 | 1 |
| stroke 715 | 28 % → 0 % | 56.4 px | 0.19 | 0.01 | 1 |
| stroke 716 | 24 % → 0 % | 25.4 px | 0.00 | 0.00 | 7 |
| stroke 717 | 32 % → 14 % | 35.3 px | 0.17 | 0.45 | 8 |
| stroke 718 | 16 % → 8 % | 24.2 px | 0.17 | 0.48 | 6 |
| stroke 719 | 43 % → 5 % | 57.2 px | 0.19 | 0.12 | 3 |
| stroke 720 | 25 % → 27 % | 42.6 px | 0.16 | 1.09 | 2 |
| stroke 721 | 36 % → 5 % | 69.1 px | 0.19 | 0.13 | 4 |
| stroke 722 | 39 % → 14 % | 65.5 px | 0.18 | 0.37 | 2 |
| stroke 723 | 49 % → 0 % | 125.9 px | 0.00 | 0.00 | 1 |
| stroke 724 | 30 % → 23 % | 78.1 px | 0.17 | 0.77 | 0 |
| stroke 725 | 57 % → 6 % | 104.1 px | 0.19 | 0.11 | 2 |
| stroke 726 | 34 % → 4 % | 65.2 px | 0.19 | 0.11 | 3 |
| stroke 727 | 51 % → 11 % | 127.6 px | 0.19 | 0.21 | 1 |
| stroke 728 | 30 % → 6 % | 85.2 px | 0.19 | 0.19 | 0 |
| stroke 729 | 58 % → 0 % | 133.5 px | 0.00 | 0.00 | 1 |
| stroke 730 | 54 % → 0 % | 150.9 px | 0.00 | 0.00 | 2 |
| stroke 731 | 8 % → 6 % | 10.6 px | 0.19 | 0.79 | 5 |
| stroke 732 | 12 % → 20 % | 17.7 px | 0.19 | 1.71 | 4 |
| stroke 733 | 12 % → 0 % | 17.6 px | 0.00 | 0.00 | 4 |
| stroke 734 | 12 % → 7 % | 18.6 px | 0.17 | 0.57 | 4 |
| stroke 735 | 25 % → 0 % | 48.9 px | 0.00 | 0.00 | 2 |
| stroke 736 | 25 % → 0 % | 41.8 px | 0.00 | 0.00 | 4 |
| stroke 737 | 29 % → 14 % | 40.6 px | 0.19 | 0.46 | 3 |
| stroke 738 | 36 % → 4 % | 84.4 px | 0.18 | 0.10 | 3 |
| stroke 739 | 36 % → 14 % | 88.7 px | 0.19 | 0.39 | 1 |
| stroke 740 | 28 % → 9 % | 76.0 px | 0.19 | 0.31 | 1 |
| stroke 741 | 48 % → 0 % | 114.8 px | 0.19 | 0.00 | 2 |
| stroke 742 | 59 % → 2 % | 130.5 px | 0.19 | 0.04 | 2 |
| stroke 743 | 42 % → 0 % | 116.4 px | 0.00 | 0.00 | 1 |
| stroke 744 | 23 % → 0 % | 62.4 px | 0.00 | 0.00 | 0 |
| stroke 745 | 35 % → 0 % | 92.7 px | 0.00 | 0.00 | 1 |
| stroke 746 | 6 % → 0 % | 13.0 px | 0.00 | 0.00 | 1 |
| stroke 747 | 7 % → 0 % | 15.4 px | 0.00 | 0.00 | 1 |
| stroke 748 | 5 % → 0 % | 12.6 px | 0.00 | 0.00 | 1 |
| stroke 749 | 9 % → 0 % | 11.9 px | 0.00 | 0.00 | 10 |
| stroke 750 | 20 % → 0 % | 30.1 px | 0.00 | 0.00 | 3 |
| stroke 751 | 8 % → 0 % | 10.0 px | 0.00 | 0.00 | 3 |
| stroke 752 | 20 % → 0 % | 31.5 px | 0.00 | 0.00 | 3 |
| stroke 753 | 11 % → 0 % | 14.6 px | 0.00 | 0.00 | 9 |
| stroke 754 | 31 % → 0 % | 53.7 px | 0.00 | 0.00 | 2 |
| stroke 755 | 19 % → 0 % | 26.5 px | 0.00 | 0.00 | 3 |
| stroke 756 | 17 % → 0 % | 21.1 px | 0.00 | 0.00 | 11 |
| stroke 757 | 21 % → 0 % | 24.9 px | 0.00 | 0.00 | 5 |
| stroke 758 | 12 % → 0 % | 22.4 px | 0.00 | 0.00 | 1 |
| stroke 759 | 28 % → 0 % | 43.0 px | 0.00 | 0.00 | 6 |
| stroke 760 | 46 % → 0 % | 78.5 px | 0.00 | 0.00 | 3 |
| stroke 761 | 27 % → 0 % | 49.0 px | 0.00 | 0.00 | 1 |
| stroke 762 | 32 % → 0 % | 50.0 px | 0.00 | 0.00 | 3 |
| stroke 763 | 35 % → 0 % | 63.6 px | 0.00 | 0.00 | 2 |
| stroke 764 | 32 % → 0 % | 70.1 px | 0.00 | 0.00 | 1 |
| stroke 765 | 33 % → 0 % | 83.6 px | 0.00 | 0.00 | 1 |
| stroke 766 | 42 % → 0 % | 91.9 px | 0.00 | 0.00 | 1 |
| stroke 767 | 8 % → 0 % | 21.9 px | 0.00 | 0.00 | 0 |
| stroke 768 | 6 % → 0 % | 12.2 px | 0.00 | 0.00 | 1 |
| stroke 769 | 9 % → 0 % | 11.2 px | 0.00 | 0.00 | 9 |
| stroke 770 | 22 % → 0 % | 34.4 px | 0.00 | 0.00 | 2 |
| stroke 771 | 27 % → 0 % | 60.3 px | 0.00 | 0.00 | 1 |
| stroke 772 | 27 % → 0 % | 49.6 px | 0.00 | 0.00 | 4 |
| stroke 773 | 33 % → 0 % | 93.6 px | 0.00 | 0.00 | 1 |
| stroke 774 | 8 % → 0 % | 12.3 px | 0.00 | 0.00 | 3 |
| stroke 775 | 10 % → 0 % | 22.1 px | 0.00 | 0.00 | 2 |
| stroke 776 | 23 % → 0 % | 56.4 px | 0.00 | 0.00 | 2 |
| stroke 777 | 26 % → 0 % | 72.9 px | 0.00 | 0.00 | 0 |
| stroke 778 | 13 % → 0 % | 19.5 px | 0.00 | 0.00 | 8 |
| stroke 779 | 12 % → 0 % | 34.2 px | 0.00 | 0.00 | 1 |
| stroke 780 | 7 % → 0 % | 9.6 px | 0.00 | 0.00 | 2 |
| stroke 781 | 7 % → 0 % | 16.6 px | 0.00 | 0.00 | 1 |
| stroke 782 | 15 % → 0 % | 21.7 px | 0.00 | 0.00 | 3 |
| stroke 783 | 17 % → 0 % | 47.1 px | 0.00 | 0.00 | 0 |
| stroke 784 | 22 % → 0 % | 58.9 px | 0.00 | 0.00 | 0 |
| stroke 785 | 19 % → 0 % | 49.4 px | 0.00 | 0.00 | 0 |
| stroke 786 | 5 % → 0 % | 11.9 px | 0.00 | 0.00 | 1 |
| stroke 787 | 8 % → 0 % | 11.5 px | 0.00 | 0.00 | 5 |
| stroke 788 | 11 % → 0 % | 16.8 px | 0.00 | 0.00 | 3 |
| stroke 789 | 16 % → 0 % | 16.9 px | 0.00 | 0.00 | 9 |
| stroke 790 | 16 % → 0 % | 24.4 px | 0.00 | 0.00 | 1 |
| stroke 791 | 24 % → 0 % | 36.3 px | 0.00 | 0.00 | 5 |
| stroke 792 | 17 % → 0 % | 25.8 px | 0.00 | 0.00 | 13 |
| stroke 793 | 11 % → 0 % | 15.1 px | 0.00 | 0.00 | 10 |
| stroke 794 | 15 % → 0 % | 16.6 px | 0.00 | 0.00 | 7 |
| stroke 795 | 24 % → 0 % | 36.8 px | 0.00 | 0.00 | 3 |
| stroke 796 | 40 % → 0 % | 65.5 px | 0.00 | 0.00 | 6 |
| stroke 797 | 38 % → 0 % | 65.1 px | 0.00 | 0.00 | 2 |
| stroke 798 | 26 % → 0 % | 41.1 px | 0.00 | 0.00 | 3 |
| stroke 799 | 31 % → 0 % | 87.8 px | 0.00 | 0.00 | 0 |
| stroke 800 | 27 % → 0 % | 41.5 px | 0.00 | 0.00 | 2 |
| stroke 801 | 35 % → 0 % | 60.6 px | 0.00 | 0.00 | 1 |
| stroke 802 | 47 % → 0 % | 76.6 px | 0.00 | 0.00 | 6 |
| stroke 803 | 47 % → 0 % | 73.0 px | 0.00 | 0.00 | 5 |
| stroke 804 | 34 % → 0 % | 55.1 px | 0.00 | 0.00 | 3 |
| stroke 805 | 59 % → 0 % | 126.9 px | 0.00 | 0.00 | 1 |
| stroke 806 | 58 % → 0 % | 142.5 px | 0.00 | 0.00 | 1 |
| stroke 807 | 32 % → 0 % | 87.0 px | 0.00 | 0.00 | 0 |
| stroke 808 | 39 % → 0 % | 82.7 px | 0.00 | 0.00 | 2 |
| stroke 809 | 37 % → 0 % | 89.4 px | 0.00 | 0.00 | 2 |
| stroke 810 | 25 % → 0 % | 66.0 px | 0.00 | 0.00 | 0 |
| stroke 811 | 47 % → 0 % | 124.2 px | 0.00 | 0.00 | 0 |
| stroke 812 | 54 % → 0 % | 146.6 px | 0.00 | 0.00 | 1 |
| stroke 813 | 8 % → 0 % | 17.7 px | 0.00 | 0.00 | 3 |
| stroke 814 | 6 % → 0 % | 8.9 px | 0.00 | 0.00 | 2 |
| stroke 815 | 17 % → 0 % | 39.5 px | 0.00 | 0.00 | 1 |
| stroke 816 | 8 % → 36 % | 9.8 px | 0.17 | 4.46 | 4 |
| stroke 817 | 8 % → 31 % | 11.7 px | 0.18 | 3.75 | 4 |
| stroke 818 | 16 % → 43 % | 25.3 px | 0.17 | 2.76 | 2 |
| stroke 819 | 21 % → 37 % | 27.9 px | 0.18 | 1.77 | 2 |
| stroke 820 | 9 % → 17 % | 12.1 px | 0.19 | 1.83 | 5 |
| stroke 821 | 11 % → 36 % | 12.4 px | 0.17 | 3.30 | 4 |
| stroke 822 | 9 % → 27 % | 16.4 px | 0.16 | 3.03 | 3 |
| stroke 823 | 14 % → 22 % | 21.7 px | 0.19 | 1.56 | 8 |
| stroke 824 | 7 % → 18 % | 11.6 px | 0.15 | 2.53 | 3 |
| stroke 825 | 27 % → 47 % | 40.2 px | 0.19 | 1.70 | 6 |
| stroke 826 | 22 % → 31 % | 33.9 px | 0.16 | 1.40 | 7 |
| stroke 827 | 21 % → 32 % | 23.7 px | 0.17 | 1.54 | 5 |
| stroke 828 | 27 % → 30 % | 41.2 px | 0.19 | 1.10 | 3 |
| stroke 829 | 26 % → 30 % | 52.7 px | 0.15 | 1.17 | 1 |
| stroke 830 | 20 % → 31 % | 40.7 px | 0.17 | 1.55 | 1 |
| stroke 831 | 29 % → 34 % | 70.0 px | 0.16 | 1.17 | 1 |
| stroke 832 | 29 % → 29 % | 83.7 px | 0.19 | 1.00 | 0 |
| stroke 833 | 24 % → 30 % | 34.6 px | 0.18 | 1.22 | 3 |
| stroke 834 | 27 % → 27 % | 71.9 px | 0.17 | 1.01 | 0 |
| stroke 835 | 19 % → 25 % | 45.5 px | 0.15 | 1.34 | 2 |
| stroke 836 | 38 % → 46 % | 83.6 px | 0.18 | 1.21 | 1 |
| stroke 837 | 38 % → 38 % | 64.7 px | 0.16 | 1.00 | 1 |
| stroke 838 | 55 % → 55 % | 89.0 px | 0.17 | 1.00 | 2 |
| stroke 839 | 26 % → 26 % | 37.0 px | 0.19 | 1.00 | 2 |
| stroke 840 | 36 % → 36 % | 89.3 px | 0.16 | 1.00 | 1 |
| stroke 841 | 10 % → 35 % | 9.7 px | 0.17 | 3.72 | 9 |
| stroke 842 | 6 % → 25 % | 11.8 px | 0.19 | 3.96 | 2 |
| stroke 843 | 14 % → 24 % | 30.0 px | 0.19 | 1.78 | 1 |
| stroke 844 | 12 % → 25 % | 18.1 px | 0.17 | 2.05 | 2 |
| stroke 845 | 19 % → 33 % | 30.1 px | 0.17 | 1.75 | 3 |
| stroke 846 | 10 % → 31 % | 16.5 px | 0.17 | 3.22 | 4 |
| stroke 847 | 12 % → 23 % | 20.5 px | 0.18 | 1.82 | 5 |
| stroke 848 | 19 % → 26 % | 38.9 px | 0.19 | 1.35 | 1 |
| stroke 849 | 25 % → 25 % | 43.4 px | 0.18 | 1.00 | 2 |
| stroke 850 | 18 % → 23 % | 27.5 px | 0.18 | 1.26 | 4 |
| stroke 851 | 26 % → 34 % | 32.4 px | 0.17 | 1.31 | 4 |
| stroke 852 | 20 % → 30 % | 50.7 px | 0.17 | 1.47 | 2 |
| stroke 853 | 34 % → 38 % | 85.0 px | 0.17 | 1.13 | 1 |
| stroke 854 | 34 % → 34 % | 97.4 px | 0.17 | 1.00 | 0 |
| stroke 855 | 26 % → 26 % | 56.3 px | 0.17 | 1.00 | 1 |

Numbers say: wet paint spreads well beyond the stroke.

## Refs v3 · #42 Pink shaggy pastel — own sheet
own sheet 800 × 976 · Pastel 1.00 · 38 px · 40.0 s

![Refs v3 · #42 Pink shaggy pastel — own sheet](Refs-v3-42-Pink-shaggy-pastel-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 4 % → 18 % | 44.1 px | 0.35 | 4.11 | 19 |
| stroke 2 | 4 % → 46 % | 48.3 px | 0.34 | 12.50 | 5 |
| stroke 3 | 9 % → 41 % | 74.9 px | 0.34 | 4.60 | 17 |
| stroke 4 | 13 % → 40 % | 128.4 px | 0.34 | 3.14 | 12 |
| stroke 5 | 7 % → 0 % | 36.3 px | 0.00 | 0.00 | 25 |
| stroke 6 | 11 % → 0 % | 46.8 px | 0.00 | 0.00 | 68 |
| stroke 7 | 18 % → 0 % | 100.5 px | 0.00 | 0.00 | 27 |
| stroke 8 | 21 % → 0 % | 95.5 px | 0.21 | 0.00 | 42 |
| stroke 9 | 29 % → 0 % | 368.5 px | 0.00 | 0.00 | 6 |
| stroke 10 | 25 % → 0 % | 112.9 px | 0.00 | 0.00 | 45 |
| stroke 11 | 31 % → 0 % | 385.2 px | 0.00 | 0.00 | 7 |
| stroke 12 | 26 % → 0 % | 95.3 px | 0.00 | 0.00 | 95 |
| stroke 13 | 18 % → 8 % | 182.7 px | 0.34 | 0.43 | 8 |
| stroke 14 | 26 % → 0 % | 90.3 px | 0.00 | 0.00 | 148 |
| stroke 15 | 35 % → 8 % | 128.1 px | 0.34 | 0.23 | 106 |
| stroke 16 | 27 % → 0 % | 108.7 px | 0.00 | 0.00 | 75 |
| stroke 17 | 36 % → 20 % | 139.0 px | 0.34 | 0.55 | 69 |
| stroke 18 | 48 % → 0 % | 362.1 px | 0.00 | 0.00 | 25 |
| stroke 19 | 31 % → 0 % | 117.6 px | 0.00 | 0.00 | 108 |
| stroke 20 | 31 % → 9 % | 111.6 px | 0.34 | 0.29 | 343 |
| stroke 21 | 45 % → 16 % | 162.5 px | 0.34 | 0.35 | 135 |
| stroke 22 | 36 % → 0 % | 133.1 px | 0.00 | 0.00 | 135 |
| stroke 23 | 46 % → 21 % | 192.9 px | 0.34 | 0.46 | 81 |
| stroke 24 | 55 % → 0 % | 309.0 px | 0.00 | 0.00 | 37 |
| stroke 25 | 43 % → 0 % | 166.4 px | 0.00 | 0.00 | 98 |
| stroke 26 | 47 % → 24 % | 186.9 px | 0.34 | 0.52 | 83 |
| stroke 27 | 53 % → 0 % | 268.4 px | 0.00 | 0.00 | 46 |
| stroke 28 | 47 % → 0 % | 240.9 px | 0.00 | 0.00 | 36 |
| stroke 29 | 51 % → 18 % | 198.3 px | 0.34 | 0.36 | 89 |
| stroke 30 | 50 % → 0 % | 419.7 px | 0.00 | 0.00 | 10 |
| stroke 31 | 41 % → 0 % | 210.2 px | 0.00 | 0.00 | 36 |
| stroke 32 | 51 % → 22 % | 286.9 px | 0.34 | 0.44 | 29 |
| stroke 33 | 54 % → 0 % | 402.8 px | 0.34 | 0.00 | 22 |
| stroke 34 | 46 % → 0 % | 447.9 px | 0.00 | 0.00 | 12 |
| stroke 35 | 35 % → 0 % | 167.9 px | 0.00 | 0.00 | 50 |
| stroke 36 | 51 % → 21 % | 335.2 px | 0.34 | 0.41 | 24 |
| stroke 37 | 53 % → 0 % | 446.7 px | 0.33 | 0.00 | 16 |
| stroke 38 | 41 % → 0 % | 549.1 px | 0.00 | 0.00 | 11 |
| stroke 39 | 33 % → 0 % | 166.7 px | 0.33 | 0.01 | 51 |
| stroke 40 | 50 % → 11 % | 206.6 px | 0.35 | 0.22 | 84 |
| stroke 41 | 38 % → 0 % | 468.2 px | 0.00 | 0.00 | 9 |
| stroke 42 | 32 % → 0 % | 168.8 px | 0.00 | 0.00 | 35 |
| stroke 43 | 42 % → 8 % | 161.2 px | 0.35 | 0.18 | 77 |
| stroke 44 | 29 % → 0 % | 153.2 px | 0.00 | 0.00 | 51 |
| stroke 45 | 44 % → 16 % | 571.8 px | 0.35 | 0.37 | 13 |
| stroke 46 | 40 % → 2 % | 142.8 px | 0.35 | 0.06 | 154 |
| stroke 47 | 41 % → 18 % | 248.5 px | 0.34 | 0.44 | 27 |
| stroke 48 | 41 % → 3 % | 153.8 px | 0.35 | 0.08 | 104 |
| stroke 49 | 31 % → 0 % | 140.8 px | 0.31 | 0.00 | 49 |
| stroke 50 | 42 % → 14 % | 423.8 px | 0.35 | 0.33 | 14 |
| stroke 51 | 42 % → 2 % | 154.8 px | 0.35 | 0.06 | 113 |
| stroke 52 | 36 % → 0 % | 173.9 px | 0.00 | 0.00 | 44 |
| stroke 53 | 49 % → 1 % | 626.2 px | 0.35 | 0.03 | 10 |
| stroke 54 | 44 % → 0 % | 177.7 px | 0.00 | 0.00 | 89 |
| stroke 55 | 35 % → 0 % | 198.5 px | 0.00 | 0.00 | 30 |
| stroke 56 | 33 % → 10 % | 409.5 px | 0.35 | 0.31 | 16 |
| stroke 57 | 45 % → 0 % | 176.1 px | 0.00 | 0.00 | 68 |
| stroke 58 | 32 % → 0 % | 208.4 px | 0.00 | 0.00 | 25 |
| stroke 59 | 40 % → 3 % | 174.8 px | 0.35 | 0.07 | 40 |
| stroke 60 | 49 % → 0 % | 179.1 px | 0.00 | 0.00 | 99 |
| stroke 61 | 27 % → 1 % | 200.5 px | 0.32 | 0.02 | 20 |
| stroke 62 | 29 % → 0 % | 363.8 px | 0.34 | 0.01 | 10 |
| stroke 63 | 47 % → 0 % | 166.1 px | 0.00 | 0.00 | 150 |
| stroke 64 | 30 % → 0 % | 202.6 px | 0.00 | 0.00 | 23 |
| stroke 65 | 48 % → 0 % | 169.3 px | 0.00 | 0.00 | 135 |
| stroke 66 | 34 % → 0 % | 225.5 px | 0.00 | 0.00 | 27 |
| stroke 67 | 39 % → 0 % | 518.2 px | 0.00 | 0.00 | 6 |
| stroke 68 | 49 % → 0 % | 178.8 px | 0.00 | 0.00 | 111 |
| stroke 69 | 46 % → 0 % | 167.6 px | 0.00 | 0.00 | 97 |
| stroke 70 | 32 % → 0 % | 268.4 px | 0.00 | 0.00 | 17 |
| stroke 71 | 49 % → 0 % | 412.5 px | 0.00 | 0.00 | 10 |
| stroke 72 | 53 % → 0 % | 446.0 px | 0.00 | 0.00 | 18 |
| stroke 73 | 48 % → 0 % | 244.9 px | 0.00 | 0.00 | 36 |
| stroke 74 | 40 % → 0 % | 212.2 px | 0.00 | 0.00 | 38 |
| stroke 75 | 54 % → 0 % | 457.0 px | 0.00 | 0.00 | 17 |
| stroke 76 | 12 % → 0 % | 23.7 px | 0.00 | 0.00 | 158 |
| stroke 77 | 19 % → 0 % | 48.1 px | 0.00 | 0.00 | 121 |
| stroke 78 | 26 % → 0 % | 67.6 px | 0.00 | 0.00 | 107 |
| stroke 79 | 33 % → 0 % | 85.2 px | 0.00 | 0.00 | 102 |
| stroke 80 | 40 % → 0 % | 103.6 px | 0.00 | 0.00 | 125 |
| stroke 81 | 40 % → 0 % | 105.1 px | 0.00 | 0.00 | 111 |
| stroke 82 | 39 % → 0 % | 99.2 px | 0.22 | 0.00 | 105 |
| stroke 83 | 42 % → 1 % | 134.7 px | 0.32 | 0.02 | 70 |
| stroke 84 | 37 % → 1 % | 233.0 px | 0.32 | 0.03 | 20 |
| stroke 85 | 6 % → 0 % | 30.2 px | 0.00 | 0.00 | 31 |
| stroke 86 | 40 % → 0 % | 151.2 px | 0.33 | 0.01 | 39 |
| stroke 87 | 30 % → 0 % | 73.4 px | 0.33 | 0.01 | 272 |
| stroke 88 | 35 % → 0 % | 97.5 px | 0.00 | 0.00 | 195 |
| stroke 89 | 47 % → 2 % | 299.2 px | 0.32 | 0.04 | 38 |
| stroke 90 | 33 % → 2 % | 133.7 px | 0.32 | 0.05 | 77 |
| stroke 91 | 41 % → 0 % | 113.4 px | 0.00 | 0.00 | 147 |
| stroke 92 | 49 % → 1 % | 595.4 px | 0.33 | 0.01 | 20 |
| stroke 93 | 47 % → 0 % | 149.3 px | 0.00 | 0.00 | 111 |
| stroke 94 | 46 % → 1 % | 570.8 px | 0.32 | 0.03 | 17 |
| stroke 95 | 51 % → 0 % | 187.5 px | 0.00 | 0.00 | 81 |
| stroke 96 | 45 % → 2 % | 177.5 px | 0.32 | 0.03 | 49 |
| stroke 97 | 50 % → 0 % | 194.8 px | 0.00 | 0.00 | 41 |
| stroke 98 | 54 % → 0 % | 280.1 px | 0.00 | 0.00 | 42 |
| stroke 99 | 57 % → 2 % | 682.1 px | 0.32 | 0.04 | 7 |
| stroke 100 | 49 % → 0 % | 334.8 px | 0.00 | 0.00 | 45 |
| stroke 101 | 57 % → 2 % | 440.1 px | 0.32 | 0.03 | 22 |
| stroke 102 | 54 % → 2 % | 502.7 px | 0.32 | 0.04 | 18 |
| stroke 103 | 1 % → 0 % | 19.4 px | 0.00 | 0.00 | 3 |
| stroke 104 | 3 % → 2 % | 22.8 px | 0.32 | 0.48 | 4 |
| stroke 105 | 12 % → 11 % | 32.4 px | 0.33 | 0.89 | 79 |
| stroke 106 | 20 % → 16 % | 83.0 px | 0.33 | 0.82 | 40 |
| stroke 107 | 16 % → 6 % | 38.5 px | 0.34 | 0.37 | 166 |
| stroke 108 | 25 % → 16 % | 115.9 px | 0.33 | 0.63 | 45 |
| stroke 109 | 24 % → 5 % | 58.6 px | 0.34 | 0.23 | 216 |
| stroke 110 | 29 % → 17 % | 140.0 px | 0.33 | 0.60 | 40 |
| stroke 111 | 31 % → 15 % | 176.6 px | 0.34 | 0.47 | 34 |
| stroke 112 | 29 % → 0 % | 100.6 px | 0.00 | 0.00 | 76 |
| stroke 113 | 31 % → 23 % | 142.0 px | 0.33 | 0.74 | 39 |
| stroke 114 | 35 % → 16 % | 219.9 px | 0.34 | 0.46 | 25 |
| stroke 115 | 41 % → 0 % | 231.9 px | 0.00 | 0.00 | 31 |
| stroke 116 | 32 % → 0 % | 306.4 px | 0.00 | 0.00 | 32 |
| stroke 117 | 28 % → 28 % | 111.5 px | 0.33 | 1.01 | 43 |
| stroke 118 | 33 % → 23 % | 202.9 px | 0.34 | 0.70 | 28 |
| stroke 119 | 45 % → 0 % | 193.5 px | 0.00 | 0.00 | 49 |
| stroke 120 | 28 % → 26 % | 134.9 px | 0.33 | 0.95 | 27 |
| stroke 121 | 27 % → 32 % | 190.5 px | 0.34 | 1.21 | 21 |
| stroke 122 | 40 % → 0 % | 174.0 px | 0.00 | 0.00 | 39 |
| stroke 123 | 28 % → 27 % | 146.6 px | 0.33 | 0.96 | 28 |
| stroke 124 | 38 % → 0 % | 357.7 px | 0.00 | 0.00 | 8 |
| stroke 125 | 27 % → 31 % | 129.9 px | 0.33 | 1.15 | 28 |
| stroke 126 | 28 % → 0 % | 352.0 px | 0.00 | 0.00 | 9 |
| stroke 127 | 26 % → 29 % | 117.1 px | 0.33 | 1.14 | 34 |
| stroke 128 | 25 % → 28 % | 126.0 px | 0.34 | 1.11 | 31 |
| stroke 129 | 27 % → 22 % | 169.1 px | 0.34 | 0.82 | 24 |
| stroke 130 | 28 % → 22 % | 231.9 px | 0.34 | 0.78 | 11 |
| stroke 131 | 25 % → 18 % | 276.3 px | 0.34 | 0.73 | 12 |
| stroke 132 | 22 % → 18 % | 244.5 px | 0.34 | 0.80 | 12 |
| stroke 133 | 19 % → 16 % | 217.1 px | 0.34 | 0.88 | 6 |
| stroke 134 | 17 % → 13 % | 190.3 px | 0.34 | 0.79 | 9 |
| stroke 135 | 16 % → 16 % | 76.9 px | 0.34 | 0.96 | 31 |
| stroke 136 | 18 % → 14 % | 89.2 px | 0.34 | 0.74 | 26 |
| stroke 137 | 21 % → 14 % | 94.9 px | 0.35 | 0.66 | 35 |
| stroke 138 | 23 % → 10 % | 100.2 px | 0.35 | 0.41 | 47 |
| stroke 139 | 27 % → 3 % | 118.5 px | 0.34 | 0.13 | 38 |
| stroke 140 | 30 % → 0 % | 186.5 px | 0.00 | 0.00 | 16 |
| stroke 141 | 32 % → 0 % | 403.9 px | 0.34 | 0.01 | 6 |
| stroke 142 | 32 % → 0 % | 229.7 px | 0.00 | 0.00 | 14 |
| stroke 143 | 26 % → 0 % | 93.0 px | 0.00 | 0.00 | 45 |
| stroke 144 | 32 % → 0 % | 182.5 px | 0.00 | 0.00 | 31 |
| stroke 145 | 31 % → 0 % | 196.4 px | 0.00 | 0.00 | 21 |
| stroke 146 | 26 % → 0 % | 84.1 px | 0.00 | 0.00 | 52 |
| stroke 147 | 32 % → 0 % | 353.0 px | 0.00 | 0.00 | 15 |
| stroke 148 | 33 % → 0 % | 159.7 px | 0.00 | 0.00 | 54 |
| stroke 149 | 31 % → 0 % | 154.1 px | 0.00 | 0.00 | 36 |
| stroke 150 | 30 % → 0 % | 147.3 px | 0.00 | 0.00 | 37 |
| stroke 151 | 30 % → 0 % | 335.1 px | 0.00 | 0.00 | 14 |
| stroke 152 | 35 % → 0 % | 169.2 px | 0.00 | 0.00 | 31 |
| stroke 153 | 29 % → 0 % | 239.1 px | 0.00 | 0.00 | 9 |
| stroke 154 | 35 % → 0 % | 218.6 px | 0.00 | 0.00 | 25 |
| stroke 155 | 31 % → 0 % | 194.3 px | 0.00 | 0.00 | 31 |
| stroke 156 | 31 % → 0 % | 138.1 px | 0.00 | 0.00 | 48 |
| stroke 157 | 43 % → 41 % | 417.6 px | 0.34 | 0.94 | 17 |
| stroke 158 | 53 % → 34 % | 644.4 px | 0.34 | 0.64 | 13 |
| stroke 159 | 6 % → 2 % | 37.7 px | 0.32 | 0.32 | 39 |
| stroke 160 | 10 % → 1 % | 51.9 px | 0.32 | 0.15 | 43 |
| stroke 161 | 14 % → 1 % | 55.3 px | 0.32 | 0.07 | 44 |
| stroke 162 | 15 % → 0 % | 93.2 px | 0.00 | 0.00 | 24 |
| stroke 163 | 17 % → 1 % | 52.8 px | 0.31 | 0.03 | 111 |
| stroke 164 | 26 % → 0 % | 215.0 px | 0.33 | 0.00 | 20 |
| stroke 165 | 22 % → 0 % | 76.5 px | 0.00 | 0.00 | 74 |
| stroke 166 | 25 % → 0 % | 79.2 px | 0.00 | 0.00 | 101 |
| stroke 167 | 36 % → 0 % | 335.0 px | 0.00 | 0.00 | 18 |
| stroke 168 | 29 % → 0 % | 102.3 px | 0.00 | 0.00 | 52 |
| stroke 169 | 24 % → 0 % | 150.4 px | 0.00 | 0.00 | 21 |
| stroke 170 | 33 % → 0 % | 76.9 px | 0.00 | 0.00 | 215 |
| stroke 171 | 23 % → 0 % | 90.6 px | 0.00 | 0.00 | 50 |
| stroke 172 | 37 % → 0 % | 87.3 px | 0.00 | 0.00 | 269 |
| stroke 173 | 28 % → 0 % | 98.7 px | 0.00 | 0.00 | 77 |
| stroke 174 | 46 % → 0 % | 118.5 px | 0.00 | 0.00 | 184 |
| stroke 175 | 43 % → 0 % | 113.5 px | 0.00 | 0.00 | 170 |
| stroke 176 | 4 % → 12 % | 44.2 px | 0.35 | 2.63 | 10 |
| stroke 177 | 37 % → 0 % | 354.9 px | 0.00 | 0.00 | 18 |
| stroke 178 | 4 % → 0 % | 46.4 px | 0.00 | 0.00 | 12 |
| stroke 179 | 8 % → 0 % | 48.8 px | 0.00 | 0.00 | 30 |
| stroke 180 | 12 % → 0 % | 158.1 px | 0.00 | 0.00 | 9 |
| stroke 181 | 2 % → 0 % | 19.8 px | 0.00 | 0.00 | 4 |
| stroke 182 | 2 % → 0 % | 24.0 px | 0.00 | 0.00 | 4 |
| stroke 183 | 1 % → 0 % | 19.2 px | 0.00 | 0.00 | 4 |
| stroke 184 | 4 % → 0 % | 19.6 px | 0.00 | 0.00 | 23 |
| stroke 185 | 2 % → 0 % | 43.5 px | 0.00 | 0.00 | 4 |
| stroke 186 | 5 % → 0 % | 47.0 px | 0.00 | 0.00 | 9 |
| stroke 187 | 7 % → 0 % | 129.3 px | 0.00 | 0.00 | 3 |
| stroke 188 | 3 % → 0 % | 46.3 px | 0.00 | 0.00 | 5 |
| stroke 189 | 9 % → 0 % | 152.0 px | 0.00 | 0.00 | 3 |
| stroke 190 | 5 % → 0 % | 59.7 px | 0.00 | 0.00 | 4 |
| stroke 191 | 12 % → 0 % | 207.0 px | 0.00 | 0.00 | 3 |
| stroke 192 | 15 % → 0 % | 78.1 px | 0.00 | 0.00 | 23 |
| stroke 193 | 19 % → 0 % | 194.2 px | 0.00 | 0.00 | 17 |
| stroke 194 | 3 % → 0 % | 42.7 px | 0.34 | 0.05 | 5 |
| stroke 195 | 4 % → 0 % | 69.3 px | 0.00 | 0.00 | 6 |
| stroke 196 | 5 % → 0 % | 79.9 px | 0.33 | 0.00 | 5 |
| stroke 197 | 10 % → 0 % | 60.5 px | 0.00 | 0.00 | 30 |
| stroke 198 | 14 % → 0 % | 131.7 px | 0.00 | 0.00 | 8 |
| stroke 199 | 18 % → 0 % | 144.7 px | 0.00 | 0.00 | 10 |
| stroke 200 | 21 % → 0 % | 85.3 px | 0.00 | 0.00 | 25 |
| stroke 201 | 23 % → 0 % | 375.4 px | 0.00 | 0.00 | 8 |
| stroke 202 | 31 % → 0 % | 369.5 px | 0.00 | 0.00 | 6 |
| stroke 203 | 25 % → 0 % | 297.0 px | 0.00 | 0.00 | 6 |
| stroke 204 | 26 % → 0 % | 486.8 px | 0.00 | 0.00 | 3 |
| stroke 205 | 13 % → 15 % | 69.5 px | 0.34 | 1.17 | 25 |
| stroke 206 | 20 % → 8 % | 80.1 px | 0.35 | 0.42 | 82 |
| stroke 207 | 31 % → 16 % | 391.3 px | 0.35 | 0.51 | 14 |
| stroke 208 | 31 % → 4 % | 147.8 px | 0.35 | 0.14 | 34 |
| stroke 209 | 38 % → 12 % | 746.6 px | 0.35 | 0.31 | 5 |
| stroke 210 | 28 % → 0 % | 363.9 px | 0.00 | 0.00 | 8 |
| stroke 211 | 3 % → 0 % | 37.7 px | 0.00 | 0.00 | 4 |
| stroke 212 | 5 % → 0 % | 62.6 px | 0.00 | 0.00 | 9 |
| stroke 213 | 10 % → 0 % | 135.8 px | 0.00 | 0.00 | 8 |
| stroke 214 | 10 % → 0 % | 105.0 px | 0.00 | 0.00 | 7 |
| stroke 215 | 14 % → 0 % | 76.3 px | 0.00 | 0.00 | 32 |
| stroke 216 | 25 % → 0 % | 139.6 px | 0.00 | 0.00 | 29 |
| stroke 217 | 23 % → 0 % | 295.6 px | 0.00 | 0.00 | 6 |
| stroke 218 | 3 % → 1 % | 61.6 px | 0.34 | 0.15 | 2 |
| stroke 219 | 4 % → 1 % | 29.8 px | 0.32 | 0.26 | 11 |
| stroke 220 | 6 % → 0 % | 54.1 px | 0.24 | 0.02 | 11 |
| stroke 221 | 10 % → 3 % | 74.9 px | 0.33 | 0.29 | 22 |
| stroke 222 | 9 % → 0 % | 81.9 px | 0.00 | 0.00 | 11 |
| stroke 223 | 9 % → 0 % | 154.4 px | 0.00 | 0.00 | 4 |
| stroke 224 | 13 % → 0 % | 71.8 px | 0.00 | 0.00 | 23 |
| stroke 225 | 3 % → 0 % | 55.8 px | 0.00 | 0.00 | 6 |
| stroke 226 | 13 % → 0 % | 68.8 px | 0.00 | 0.00 | 34 |
| stroke 227 | 24 % → 0 % | 413.2 px | 0.00 | 0.00 | 4 |
| stroke 228 | 15 % → 0 % | 131.0 px | 0.00 | 0.00 | 12 |
| stroke 229 | 4 % → 0 % | 33.1 px | 0.00 | 0.00 | 13 |
| stroke 230 | 7 % → 0 % | 45.2 px | 0.00 | 0.00 | 26 |
| stroke 231 | 10 % → 0 % | 61.2 px | 0.00 | 0.00 | 22 |
| stroke 232 | 13 % → 0 % | 93.4 px | 0.00 | 0.00 | 17 |
| stroke 233 | 18 % → 0 % | 179.3 px | 0.00 | 0.00 | 10 |
| stroke 234 | 3 % → 0 % | 44.6 px | 0.00 | 0.00 | 9 |
| stroke 235 | 9 % → 0 % | 86.9 px | 0.00 | 0.00 | 7 |
| stroke 236 | 13 % → 0 % | 132.3 px | 0.00 | 0.00 | 12 |
| stroke 237 | 13 % → 0 % | 112.1 px | 0.00 | 0.00 | 18 |
| stroke 238 | 14 % → 0 % | 246.3 px | 0.00 | 0.00 | 2 |
| stroke 239 | 13 % → 0 % | 229.0 px | 0.00 | 0.00 | 4 |
| stroke 240 | 4 % → 0 % | 28.8 px | 0.00 | 0.00 | 20 |
| stroke 241 | 7 % → 0 % | 35.0 px | 0.00 | 0.00 | 35 |
| stroke 242 | 11 % → 0 % | 48.9 px | 0.00 | 0.00 | 109 |
| stroke 243 | 21 % → 0 % | 110.4 px | 0.00 | 0.00 | 79 |
| stroke 244 | 18 % → 0 % | 96.9 px | 0.00 | 0.00 | 47 |
| stroke 245 | 18 % → 0 % | 161.0 px | 0.00 | 0.00 | 16 |
| stroke 246 | 15 % → 0 % | 84.8 px | 0.00 | 0.00 | 26 |
| stroke 247 | 15 % → 0 % | 62.3 px | 0.00 | 0.00 | 58 |
| stroke 248 | 19 % → 0 % | 96.6 px | 0.00 | 0.00 | 34 |
| stroke 249 | 23 % → 0 % | 166.2 px | 0.00 | 0.00 | 20 |
| stroke 250 | 24 % → 1 % | 234.8 px | 0.33 | 0.02 | 14 |
| stroke 251 | 23 % → 1 % | 148.5 px | 0.32 | 0.06 | 31 |
| stroke 252 | 28 % → 0 % | 272.4 px | 0.00 | 0.00 | 11 |
| stroke 253 | 21 % → 2 % | 200.3 px | 0.32 | 0.10 | 17 |
| stroke 254 | 23 % → 2 % | 396.3 px | 0.32 | 0.10 | 14 |
| stroke 255 | 20 % → 2 % | 161.8 px | 0.32 | 0.10 | 22 |
| stroke 256 | 20 % → 2 % | 141.1 px | 0.32 | 0.10 | 20 |
| stroke 257 | 19 % → 2 % | 188.7 px | 0.32 | 0.11 | 14 |
| stroke 258 | 16 % → 2 % | 117.2 px | 0.32 | 0.12 | 17 |
| stroke 259 | 24 % → 1 % | 312.8 px | 0.32 | 0.05 | 15 |
| stroke 260 | 14 % → 1 % | 224.3 px | 0.32 | 0.09 | 4 |
| stroke 261 | 35 % → 2 % | 617.2 px | 0.32 | 0.07 | 3 |
| stroke 262 | 20 % → 2 % | 196.7 px | 0.32 | 0.10 | 9 |
| stroke 263 | 27 % → 2 % | 214.4 px | 0.32 | 0.08 | 18 |
| stroke 264 | 46 % → 2 % | 584.4 px | 0.32 | 0.05 | 8 |
| stroke 265 | 25 % → 2 % | 304.2 px | 0.32 | 0.09 | 4 |
| stroke 266 | 25 % → 2 % | 205.6 px | 0.32 | 0.08 | 10 |
| stroke 267 | 45 % → 2 % | 530.3 px | 0.32 | 0.05 | 4 |
| stroke 268 | 28 % → 2 % | 330.1 px | 0.32 | 0.08 | 9 |
| stroke 269 | 29 % → 2 % | 340.6 px | 0.32 | 0.08 | 10 |
| stroke 270 | 28 % → 2 % | 227.5 px | 0.32 | 0.08 | 20 |
| stroke 271 | 28 % → 2 % | 270.1 px | 0.32 | 0.08 | 10 |
| stroke 272 | 22 % → 2 % | 272.4 px | 0.32 | 0.10 | 3 |
| stroke 273 | 6 % → 0 % | 25.7 px | 0.00 | 0.00 | 24 |
| stroke 274 | 10 % → 0 % | 39.4 px | 0.00 | 0.00 | 37 |
| stroke 275 | 15 % → 0 % | 179.2 px | 0.00 | 0.00 | 8 |
| stroke 276 | 15 % → 0 % | 190.7 px | 0.00 | 0.00 | 8 |
| stroke 277 | 17 % → 0 % | 291.4 px | 0.00 | 0.00 | 8 |
| stroke 278 | 17 % → 0 % | 281.1 px | 0.00 | 0.00 | 3 |
| stroke 279 | 19 % → 0 % | 245.9 px | 0.00 | 0.00 | 7 |
| stroke 280 | 17 % → 0 % | 271.8 px | 0.00 | 0.00 | 3 |
| stroke 281 | 21 % → 0 % | 273.1 px | 0.00 | 0.00 | 4 |
| stroke 282 | 21 % → 0 % | 238.6 px | 0.00 | 0.00 | 6 |
| stroke 283 | 19 % → 0 % | 231.9 px | 0.00 | 0.00 | 5 |
| stroke 284 | 20 % → 0 % | 320.1 px | 0.00 | 0.00 | 9 |
| stroke 285 | 17 % → 0 % | 279.8 px | 0.00 | 0.00 | 3 |
| stroke 286 | 16 % → 0 % | 283.9 px | 0.00 | 0.00 | 8 |
| stroke 287 | 15 % → 0 % | 252.0 px | 0.00 | 0.00 | 3 |
| stroke 288 | 13 % → 0 % | 203.0 px | 0.00 | 0.00 | 3 |
| stroke 289 | 19 % → 0 % | 186.1 px | 0.00 | 0.00 | 6 |
| stroke 290 | 15 % → 0 % | 185.9 px | 0.00 | 0.00 | 5 |
| stroke 291 | 24 % → 0 % | 84.7 px | 0.00 | 0.00 | 32 |
| stroke 292 | 27 % → 0 % | 97.3 px | 0.00 | 0.00 | 37 |
| stroke 293 | 30 % → 0 % | 108.8 px | 0.00 | 0.00 | 48 |
| stroke 294 | 33 % → 0 % | 117.4 px | 0.00 | 0.00 | 45 |
| stroke 295 | 32 % → 0 % | 165.9 px | 0.00 | 0.00 | 30 |
| stroke 296 | 3 % → 0 % | 16.6 px | 0.00 | 0.00 | 12 |
| stroke 297 | 5 % → 0 % | 36.8 px | 0.00 | 0.00 | 10 |
| stroke 298 | 4 % → 0 % | 47.4 px | 0.00 | 0.00 | 9 |
| stroke 299 | 8 % → 0 % | 38.7 px | 0.00 | 0.00 | 37 |
| stroke 300 | 13 % → 0 % | 129.4 px | 0.00 | 0.00 | 13 |
| stroke 301 | 6 % → 0 % | 40.1 px | 0.00 | 0.00 | 27 |
| stroke 302 | 10 % → 0 % | 49.9 px | 0.00 | 0.00 | 27 |
| stroke 303 | 14 % → 0 % | 77.7 px | 0.00 | 0.00 | 30 |
| stroke 304 | 19 % → 0 % | 108.1 px | 0.00 | 0.00 | 26 |
| stroke 305 | 22 % → 0 % | 110.0 px | 0.00 | 0.00 | 33 |
| stroke 306 | 24 % → 0 % | 128.2 px | 0.00 | 0.00 | 33 |
| stroke 307 | 25 % → 0 % | 204.7 px | 0.00 | 0.00 | 25 |
| stroke 308 | 1 % → 0 % | 13.0 px | 0.00 | 0.00 | 3 |
| stroke 309 | 3 % → 25 % | 29.5 px | 0.33 | 7.31 | 9 |
| stroke 310 | 6 % → 22 % | 35.4 px | 0.33 | 3.74 | 22 |
| stroke 311 | 8 % → 20 % | 42.2 px | 0.33 | 2.41 | 26 |
| stroke 312 | 16 % → 35 % | 279.3 px | 0.33 | 2.16 | 3 |
| stroke 313 | 18 % → 38 % | 319.6 px | 0.33 | 2.12 | 2 |
| stroke 314 | 19 % → 37 % | 239.7 px | 0.33 | 2.02 | 4 |
| stroke 315 | 17 % → 30 % | 100.4 px | 0.33 | 1.76 | 18 |
| stroke 316 | 20 % → 36 % | 119.9 px | 0.34 | 1.78 | 15 |
| stroke 317 | 27 % → 42 % | 482.4 px | 0.33 | 1.59 | 2 |
| stroke 318 | 21 % → 42 % | 272.0 px | 0.33 | 1.94 | 5 |
| stroke 319 | 18 % → 38 % | 180.9 px | 0.33 | 2.10 | 6 |
| stroke 320 | 20 % → 33 % | 127.2 px | 0.33 | 1.69 | 15 |
| stroke 321 | 18 % → 36 % | 137.4 px | 0.34 | 2.04 | 12 |
| stroke 322 | 17 % → 38 % | 107.7 px | 0.34 | 2.27 | 17 |
| stroke 323 | 22 % → 41 % | 188.2 px | 0.34 | 1.92 | 12 |
| stroke 324 | 19 % → 39 % | 194.9 px | 0.34 | 2.01 | 9 |
| stroke 325 | 26 % → 41 % | 454.5 px | 0.34 | 1.60 | 4 |
| stroke 326 | 19 % → 34 % | 292.3 px | 0.34 | 1.81 | 2 |
| stroke 327 | 22 % → 36 % | 403.1 px | 0.34 | 1.66 | 2 |
| stroke 328 | 16 % → 28 % | 205.7 px | 0.35 | 1.77 | 5 |
| stroke 329 | 20 % → 34 % | 374.7 px | 0.34 | 1.69 | 3 |
| stroke 330 | 15 % → 26 % | 158.2 px | 0.35 | 1.68 | 10 |
| stroke 331 | 19 % → 28 % | 148.0 px | 0.34 | 1.45 | 7 |
| stroke 332 | 21 % → 27 % | 143.6 px | 0.34 | 1.29 | 19 |
| stroke 333 | 24 % → 27 % | 164.5 px | 0.34 | 1.12 | 18 |
| stroke 334 | 24 % → 24 % | 169.4 px | 0.34 | 1.00 | 13 |
| stroke 335 | 2 % → 2 % | 40.7 px | 0.32 | 1.00 | 4 |

Numbers say: wet paint spreads well beyond the stroke.

## Refs v3 · #43 Dragged black blocks — own sheet
own sheet 800 × 1115 · Ink 0.93 · Gouache 0.07 · 112 px · 166.5 s

![Refs v3 · #43 Dragged black blocks — own sheet](Refs-v3-43-Dragged-black-blocks-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 11 % → 68 % | 102.2 px | 0.51 | 6.06 | 193 |
| stroke 2 | 16 % → 73 % | 161.0 px | 0.50 | 4.58 | 244 |
| stroke 3 | 18 % → 76 % | 212.6 px | 0.50 | 4.15 | 329 |
| stroke 4 | 21 % → 79 % | 266.5 px | 0.50 | 3.70 | 420 |
| stroke 5 | 22 % → 82 % | 223.5 px | 0.50 | 3.67 | 704 |
| stroke 6 | 26 % → 87 % | 337.4 px | 0.50 | 3.28 | 495 |
| stroke 7 | 26 % → 88 % | 269.2 px | 0.50 | 3.41 | 568 |
| stroke 8 | 23 % → 54 % | 527.7 px | 0.50 | 2.31 | 191 |
| stroke 9 | 27 % → 78 % | 233.3 px | 0.50 | 2.93 | 2008 |
| stroke 10 | 28 % → 78 % | 264.0 px | 0.50 | 2.74 | 1749 |
| stroke 11 | 31 % → 78 % | 307.7 px | 0.50 | 2.47 | 1268 |
| stroke 12 | 35 % → 82 % | 341.6 px | 0.50 | 2.34 | 1291 |
| stroke 13 | 41 % → 92 % | 418.6 px | 0.50 | 2.26 | 975 |
| stroke 14 | 44 % → 85 % | 788.1 px | 0.50 | 1.91 | 442 |
| stroke 15 | 37 % → 86 % | 378.6 px | 0.50 | 2.35 | 1584 |
| stroke 16 | 17 % → 53 % | 161.8 px | 0.50 | 3.09 | 323 |
| stroke 17 | 38 % → 88 % | 406.9 px | 0.50 | 2.30 | 1724 |
| stroke 18 | 34 % → 65 % | 289.0 px | 0.50 | 1.88 | 527 |
| stroke 19 | 43 % → 81 % | 378.1 px | 0.50 | 1.90 | 2398 |
| stroke 20 | 46 % → 82 % | 435.2 px | 0.50 | 1.79 | 2288 |
| stroke 21 | 51 % → 91 % | 449.1 px | 0.50 | 1.80 | 1950 |
| stroke 22 | 56 % → 78 % | 626.2 px | 0.50 | 1.40 | 510 |
| stroke 23 | 59 % → 90 % | 468.7 px | 0.50 | 1.52 | 2744 |
| stroke 24 | 58 % → 89 % | 448.8 px | 0.50 | 1.53 | 1383 |
| stroke 25 | 66 % → 86 % | 642.9 px | 0.50 | 1.30 | 1148 |
| stroke 26 | 59 % → 86 % | 498.4 px | 0.50 | 1.45 | 1020 |
| stroke 27 | 67 % → 87 % | 653.4 px | 0.50 | 1.30 | 1012 |
| stroke 28 | 61 % → 85 % | 597.8 px | 0.50 | 1.39 | 887 |
| stroke 29 | 67 % → 89 % | 669.5 px | 0.50 | 1.32 | 973 |
| stroke 30 | 63 % → 89 % | 634.9 px | 0.50 | 1.41 | 1005 |
| stroke 31 | 67 % → 89 % | 684.6 px | 0.50 | 1.33 | 655 |
| stroke 32 | 65 % → 90 % | 651.3 px | 0.50 | 1.40 | 936 |
| stroke 33 | 66 % → 88 % | 721.1 px | 0.50 | 1.32 | 541 |
| stroke 34 | 63 % → 89 % | 628.8 px | 0.50 | 1.40 | 936 |
| stroke 35 | 66 % → 87 % | 751.6 px | 0.50 | 1.32 | 475 |
| stroke 36 | 69 % → 88 % | 643.9 px | 0.50 | 1.28 | 686 |
| stroke 37 | 67 % → 86 % | 875.5 px | 0.50 | 1.28 | 365 |
| stroke 38 | 71 % → 86 % | 614.9 px | 0.50 | 1.21 | 652 |
| stroke 39 | 75 % → 84 % | 573.7 px | 0.50 | 1.11 | 808 |
| stroke 40 | 77 % → 82 % | 525.3 px | 0.50 | 1.06 | 679 |
| stroke 41 | 78 % → 80 % | 602.5 px | 0.50 | 1.03 | 386 |
| stroke 42 | 84 % → 85 % | 891.9 px | 0.50 | 1.01 | 193 |

Numbers say: wet paint spreads well beyond the stroke.

## Refs v3 · #44 Blue looping ribbon — own sheet
own sheet 800 × 1204 · Oil 0.52 · Gouache 0.48 + turpentine 10 % · 51 px · 149.8 s

![Refs v3 · #44 Blue looping ribbon — own sheet](Refs-v3-44-Blue-looping-ribbon-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 7 % → 1 % | 50.1 px | 0.29 | 0.15 | 102 |
| stroke 2 | 10 % → 1 % | 59.2 px | 0.29 | 0.07 | 188 |
| stroke 3 | 11 % → 0 % | 72.0 px | 0.29 | 0.02 | 127 |
| stroke 4 | 17 % → 1 % | 101.4 px | 0.29 | 0.04 | 273 |
| stroke 5 | 22 % → 0 % | 155.0 px | 0.00 | 0.00 | 49 |
| stroke 6 | 14 % → 0 % | 85.4 px | 0.29 | 0.02 | 477 |
| stroke 7 | 22 % → 0 % | 170.1 px | 0.00 | 0.00 | 49 |
| stroke 8 | 19 % → 0 % | 126.6 px | 0.00 | 0.00 | 188 |
| stroke 9 | 39 % → 2 % | 693.1 px | 0.29 | 0.04 | 29 |
| stroke 10 | 39 % → 1 % | 403.7 px | 0.29 | 0.03 | 58 |
| stroke 11 | 21 % → 0 % | 180.6 px | 0.00 | 0.00 | 24 |
| stroke 12 | 20 % → 0 % | 145.5 px | 0.00 | 0.00 | 128 |
| stroke 13 | 21 % → 0 % | 210.6 px | 0.00 | 0.00 | 24 |
| stroke 14 | 20 % → 0 % | 174.7 px | 0.00 | 0.00 | 99 |
| stroke 15 | 20 % → 0 % | 195.3 px | 0.00 | 0.00 | 73 |
| stroke 16 | 20 % → 0 % | 185.2 px | 0.00 | 0.00 | 66 |
| stroke 17 | 20 % → 0 % | 209.5 px | 0.00 | 0.00 | 67 |
| stroke 18 | 20 % → 0 % | 178.8 px | 0.00 | 0.00 | 75 |
| stroke 19 | 21 % → 0 % | 160.0 px | 0.00 | 0.00 | 98 |
| stroke 20 | 24 % → 0 % | 394.8 px | 0.00 | 0.00 | 42 |
| stroke 21 | 32 % → 0 % | 358.0 px | 0.00 | 0.00 | 46 |
| stroke 22 | 31 % → 0 % | 342.8 px | 0.00 | 0.00 | 57 |
| stroke 23 | 30 % → 0 % | 427.1 px | 0.00 | 0.00 | 34 |
| stroke 24 | 26 % → 0 % | 442.9 px | 0.00 | 0.00 | 29 |
| stroke 25 | 23 % → 0 % | 328.8 px | 0.00 | 0.00 | 26 |
| stroke 26 | 20 % → 0 % | 355.2 px | 0.00 | 0.00 | 22 |
| stroke 27 | 39 % → 0 % | 346.0 px | 0.00 | 0.00 | 66 |
| stroke 28 | 25 % → 0 % | 141.1 px | 0.00 | 0.00 | 80 |
| stroke 29 | 28 % → 0 % | 152.0 px | 0.00 | 0.00 | 99 |
| stroke 30 | 13 % → 0 % | 103.9 px | 0.00 | 0.00 | 74 |
| stroke 31 | 20 % → 0 % | 117.5 px | 0.00 | 0.00 | 170 |
| stroke 32 | 23 % → 0 % | 126.2 px | 0.00 | 0.00 | 225 |
| stroke 33 | 23 % → 0 % | 132.4 px | 0.00 | 0.00 | 230 |
| stroke 34 | 26 % → 0 % | 149.3 px | 0.00 | 0.00 | 201 |
| stroke 35 | 26 % → 0 % | 145.0 px | 0.00 | 0.00 | 210 |
| stroke 36 | 31 % → 0 % | 186.6 px | 0.00 | 0.00 | 179 |
| stroke 37 | 37 % → 0 % | 238.8 px | 0.00 | 0.00 | 158 |
| stroke 38 | 34 % → 0 % | 216.0 px | 0.00 | 0.00 | 124 |
| stroke 39 | 35 % → 0 % | 199.8 px | 0.00 | 0.00 | 204 |
| stroke 40 | 37 % → 0 % | 251.0 px | 0.00 | 0.00 | 150 |
| stroke 41 | 39 % → 0 % | 667.1 px | 0.00 | 0.00 | 27 |
| stroke 42 | 16 % → 0 % | 151.3 px | 0.00 | 0.00 | 57 |
| stroke 43 | 22 % → 0 % | 107.6 px | 0.00 | 0.00 | 178 |
| stroke 44 | 28 % → 0 % | 162.7 px | 0.00 | 0.00 | 180 |
| stroke 45 | 20 % → 0 % | 152.5 px | 0.00 | 0.00 | 85 |
| stroke 46 | 15 % → 0 % | 200.6 px | 0.00 | 0.00 | 39 |
| stroke 47 | 41 % → 0 % | 663.1 px | 0.00 | 0.00 | 30 |
| stroke 48 | 15 % → 0 % | 246.6 px | 0.00 | 0.00 | 19 |
| stroke 49 | 49 % → 0 % | 572.2 px | 0.00 | 0.00 | 50 |
| stroke 50 | 55 % → 0 % | 742.1 px | 0.00 | 0.00 | 27 |
| stroke 51 | 23 % → 0 % | 334.8 px | 0.00 | 0.00 | 26 |
| stroke 52 | 33 % → 0 % | 343.3 px | 0.00 | 0.00 | 72 |
| stroke 53 | 15 % → 0 % | 256.9 px | 0.00 | 0.00 | 28 |
| stroke 54 | 17 % → 0 % | 47.7 px | 0.00 | 0.00 | 271 |
| stroke 55 | 21 % → 0 % | 62.7 px | 0.00 | 0.00 | 393 |
| stroke 56 | 27 % → 0 % | 80.7 px | 0.00 | 0.00 | 475 |
| stroke 57 | 32 % → 0 % | 105.3 px | 0.00 | 0.00 | 440 |
| stroke 58 | 4 % → 0 % | 61.9 px | 0.00 | 0.00 | 27 |
| stroke 59 | 7 % → 0 % | 88.0 px | 0.00 | 0.00 | 53 |
| stroke 60 | 9 % → 0 % | 124.2 px | 0.00 | 0.00 | 45 |
| stroke 61 | 10 % → 0 % | 112.6 px | 0.00 | 0.00 | 57 |
| stroke 62 | 12 % → 0 % | 125.4 px | 0.00 | 0.00 | 80 |
| stroke 63 | 16 % → 0 % | 196.9 px | 0.00 | 0.00 | 48 |
| stroke 64 | 7 % → 0 % | 97.9 px | 0.00 | 0.00 | 24 |
| stroke 65 | 21 % → 0 % | 119.4 px | 0.00 | 0.00 | 162 |
| stroke 66 | 23 % → 0 % | 132.9 px | 0.00 | 0.00 | 178 |
| stroke 67 | 31 % → 0 % | 440.7 px | 0.00 | 0.00 | 35 |
| stroke 68 | 40 % → 0 % | 322.7 px | 0.00 | 0.00 | 84 |
| stroke 69 | 2 % → 0 % | 12.5 px | 0.00 | 0.00 | 44 |
| stroke 70 | 1 % → 0 % | 13.5 px | 0.00 | 0.00 | 11 |
| stroke 71 | 2 % → 0 % | 13.1 px | 0.00 | 0.00 | 19 |
| stroke 72 | 2 % → 0 % | 33.0 px | 0.00 | 0.00 | 4 |
| stroke 73 | 1 % → 0 % | 17.3 px | 0.00 | 0.00 | 9 |
| stroke 74 | 1 % → 0 % | 15.0 px | 0.00 | 0.00 | 11 |
| stroke 75 | 2 % → 0 % | 40.2 px | 0.00 | 0.00 | 7 |
| stroke 76 | 1 % → 0 % | 15.0 px | 0.00 | 0.00 | 12 |
| stroke 77 | 4 % → 0 % | 34.5 px | 0.00 | 0.00 | 41 |
| stroke 78 | 1 % → 0 % | 19.8 px | 0.00 | 0.00 | 20 |
| stroke 79 | 3 % → 0 % | 39.4 px | 0.00 | 0.00 | 20 |
| stroke 80 | 7 % → 0 % | 60.1 px | 0.00 | 0.00 | 80 |
| stroke 81 | 10 % → 0 % | 69.8 px | 0.28 | 0.05 | 165 |
| stroke 82 | 13 % → 1 % | 81.3 px | 0.29 | 0.06 | 275 |
| stroke 83 | 15 % → 1 % | 92.9 px | 0.29 | 0.04 | 300 |
| stroke 84 | 17 % → 1 % | 104.7 px | 0.29 | 0.03 | 377 |
| stroke 85 | 13 % → 0 % | 55.0 px | 0.00 | 0.00 | 260 |
| stroke 86 | 17 % → 0 % | 68.5 px | 0.00 | 0.00 | 318 |
| stroke 87 | 20 % → 0 % | 82.6 px | 0.00 | 0.00 | 355 |
| stroke 88 | 26 % → 0 % | 154.6 px | 0.00 | 0.00 | 259 |
| stroke 89 | 36 % → 0 % | 213.3 px | 0.00 | 0.00 | 107 |
| stroke 90 | 25 % → 0 % | 112.4 px | 0.00 | 0.00 | 410 |
| stroke 91 | 32 % → 0 % | 178.8 px | 0.30 | 0.00 | 324 |
| stroke 92 | 38 % → 0 % | 242.3 px | 0.00 | 0.00 | 128 |
| stroke 93 | 32 % → 1 % | 172.7 px | 0.29 | 0.02 | 421 |
| stroke 94 | 39 % → 0 % | 522.3 px | 0.00 | 0.00 | 41 |
| stroke 95 | 27 % → 0 % | 344.8 px | 0.00 | 0.00 | 51 |
| stroke 96 | 32 % → 1 % | 201.7 px | 0.29 | 0.03 | 223 |
| stroke 97 | 54 % → 0 % | 335.2 px | 0.00 | 0.00 | 163 |
| stroke 98 | 39 % → 0 % | 233.4 px | 0.00 | 0.00 | 191 |
| stroke 99 | 34 % → 1 % | 202.0 px | 0.29 | 0.02 | 238 |
| stroke 100 | 55 % → 0 % | 382.7 px | 0.00 | 0.00 | 143 |
| stroke 101 | 33 % → 0 % | 212.4 px | 0.00 | 0.00 | 180 |
| stroke 102 | 35 % → 1 % | 208.5 px | 0.29 | 0.02 | 266 |
| stroke 103 | 41 % → 0 % | 212.0 px | 0.00 | 0.00 | 511 |
| stroke 104 | 37 % → 1 % | 210.7 px | 0.29 | 0.02 | 265 |
| stroke 105 | 40 % → 0 % | 212.0 px | 0.00 | 0.00 | 467 |
| stroke 106 | 44 % → 0 % | 612.4 px | 0.00 | 0.00 | 43 |
| stroke 107 | 44 % → 0 % | 335.3 px | 0.00 | 0.00 | 151 |
| stroke 108 | 48 % → 0 % | 480.3 px | 0.00 | 0.00 | 97 |
| stroke 109 | 43 % → 0 % | 228.2 px | 0.00 | 0.00 | 416 |
| stroke 110 | 42 % → 0 % | 590.6 px | 0.00 | 0.00 | 51 |
| stroke 111 | 48 % → 0 % | 676.5 px | 0.00 | 0.00 | 38 |
| stroke 112 | 50 % → 0 % | 288.6 px | 0.00 | 0.00 | 229 |
| stroke 113 | 39 % → 0 % | 211.0 px | 0.00 | 0.00 | 391 |
| stroke 114 | 47 % → 0 % | 335.9 px | 0.00 | 0.00 | 155 |
| stroke 115 | 52 % → 0 % | 297.0 px | 0.00 | 0.00 | 488 |
| stroke 116 | 57 % → 0 % | 445.0 px | 0.00 | 0.00 | 197 |
| stroke 117 | 33 % → 0 % | 214.4 px | 0.00 | 0.00 | 211 |
| stroke 118 | 44 % → 0 % | 317.2 px | 0.00 | 0.00 | 121 |
| stroke 119 | 51 % → 0 % | 285.0 px | 0.00 | 0.00 | 312 |
| stroke 120 | 44 % → 0 % | 223.2 px | 0.00 | 0.00 | 571 |
| stroke 121 | 40 % → 0 % | 237.4 px | 0.00 | 0.00 | 266 |
| stroke 122 | 49 % → 0 % | 318.3 px | 0.00 | 0.00 | 196 |
| stroke 123 | 56 % → 0 % | 459.2 px | 0.00 | 0.00 | 93 |
| stroke 124 | 57 % → 0 % | 442.2 px | 0.00 | 0.00 | 130 |
| stroke 125 | 40 % → 0 % | 213.6 px | 0.00 | 0.00 | 180 |
| stroke 126 | 38 % → 0 % | 225.1 px | 0.00 | 0.00 | 216 |
| stroke 127 | 51 % → 0 % | 706.0 px | 0.00 | 0.00 | 72 |
| stroke 128 | 51 % → 0 % | 473.2 px | 0.00 | 0.00 | 86 |
| stroke 129 | 55 % → 0 % | 473.3 px | 0.00 | 0.00 | 99 |
| stroke 130 | 54 % → 0 % | 403.7 px | 0.00 | 0.00 | 133 |
| stroke 131 | 43 % → 0 % | 210.2 px | 0.00 | 0.00 | 178 |
| stroke 132 | 37 % → 0 % | 221.1 px | 0.00 | 0.00 | 246 |
| stroke 133 | 49 % → 0 % | 275.5 px | 0.00 | 0.00 | 305 |
| stroke 134 | 57 % → 0 % | 364.7 px | 0.00 | 0.00 | 204 |
| stroke 135 | 53 % → 0 % | 260.4 px | 0.00 | 0.00 | 339 |
| stroke 136 | 34 % → 0 % | 235.1 px | 0.00 | 0.00 | 245 |
| stroke 137 | 50 % → 0 % | 276.8 px | 0.00 | 0.00 | 437 |
| stroke 138 | 56 % → 0 % | 298.0 px | 0.00 | 0.00 | 318 |
| stroke 139 | 36 % → 0 % | 311.1 px | 0.00 | 0.00 | 104 |
| stroke 140 | 53 % → 0 % | 275.2 px | 0.00 | 0.00 | 685 |
| stroke 141 | 36 % → 0 % | 357.4 px | 0.00 | 0.00 | 99 |
| stroke 142 | 50 % → 0 % | 276.1 px | 0.00 | 0.00 | 327 |
| stroke 143 | 55 % → 0 % | 316.2 px | 0.00 | 0.00 | 240 |
| stroke 144 | 35 % → 0 % | 349.7 px | 0.00 | 0.00 | 87 |
| stroke 145 | 35 % → 0 % | 330.6 px | 0.00 | 0.00 | 89 |
| stroke 146 | 54 % → 0 % | 296.9 px | 0.00 | 0.00 | 274 |
| stroke 147 | 53 % → 0 % | 323.3 px | 0.00 | 0.00 | 196 |
| stroke 148 | 32 % → 0 % | 299.6 px | 0.00 | 0.00 | 87 |
| stroke 149 | 28 % → 0 % | 307.0 px | 0.00 | 0.00 | 68 |
| stroke 150 | 53 % → 0 % | 297.0 px | 0.00 | 0.00 | 269 |
| stroke 151 | 50 % → 0 % | 333.4 px | 0.00 | 0.00 | 156 |
| stroke 152 | 25 % → 0 % | 302.5 px | 0.00 | 0.00 | 51 |
| stroke 153 | 35 % → 0 % | 383.7 px | 0.00 | 0.00 | 80 |
| stroke 154 | 52 % → 0 % | 293.4 px | 0.00 | 0.00 | 219 |
| stroke 155 | 48 % → 0 % | 472.4 px | 0.00 | 0.00 | 77 |
| stroke 156 | 26 % → 0 % | 288.6 px | 0.00 | 0.00 | 68 |
| stroke 157 | 33 % → 0 % | 463.7 px | 0.00 | 0.00 | 43 |
| stroke 158 | 50 % → 0 % | 272.4 px | 0.00 | 0.00 | 276 |
| stroke 159 | 42 % → 0 % | 393.3 px | 0.00 | 0.00 | 84 |
| stroke 160 | 30 % → 0 % | 203.4 px | 0.00 | 0.00 | 298 |
| stroke 161 | 37 % → 0 % | 253.2 px | 0.00 | 0.00 | 148 |
| stroke 162 | 48 % → 0 % | 261.1 px | 0.00 | 0.00 | 317 |
| stroke 163 | 38 % → 0 % | 420.0 px | 0.00 | 0.00 | 66 |
| stroke 164 | 38 % → 0 % | 202.9 px | 0.00 | 0.00 | 222 |
| stroke 165 | 33 % → 0 % | 465.7 px | 0.00 | 0.00 | 50 |
| stroke 166 | 45 % → 0 % | 285.3 px | 0.00 | 0.00 | 154 |
| stroke 167 | 52 % → 0 % | 384.3 px | 0.00 | 0.00 | 113 |
| stroke 168 | 34 % → 0 % | 390.5 px | 0.00 | 0.00 | 59 |
| stroke 169 | 47 % → 0 % | 269.1 px | 0.00 | 0.00 | 169 |
| stroke 170 | 43 % → 0 % | 247.8 px | 0.00 | 0.00 | 256 |
| stroke 171 | 53 % → 0 % | 308.0 px | 0.00 | 0.00 | 243 |
| stroke 172 | 40 % → 0 % | 395.6 px | 0.00 | 0.00 | 113 |
| stroke 173 | 52 % → 0 % | 301.0 px | 0.00 | 0.00 | 172 |
| stroke 174 | 41 % → 0 % | 329.8 px | 0.00 | 0.00 | 123 |
| stroke 175 | 52 % → 0 % | 353.1 px | 0.00 | 0.00 | 175 |
| stroke 176 | 41 % → 0 % | 276.0 px | 0.00 | 0.00 | 122 |
| stroke 177 | 54 % → 0 % | 242.5 px | 0.00 | 0.00 | 269 |
| stroke 178 | 50 % → 0 % | 259.6 px | 0.00 | 0.00 | 545 |
| stroke 179 | 61 % → 0 % | 290.3 px | 0.00 | 0.00 | 240 |
| stroke 180 | 49 % → 0 % | 263.5 px | 0.00 | 0.00 | 572 |
| stroke 181 | 68 % → 0 % | 302.5 px | 0.00 | 0.00 | 238 |
| stroke 182 | 51 % → 0 % | 265.2 px | 0.00 | 0.00 | 647 |
| stroke 183 | 58 % → 0 % | 253.1 px | 0.00 | 0.00 | 745 |
| stroke 184 | 64 % → 0 % | 268.2 px | 0.00 | 0.00 | 413 |
| stroke 185 | 69 % → 0 % | 267.5 px | 0.00 | 0.00 | 301 |
| stroke 186 | 72 % → 0 % | 262.8 px | 0.00 | 0.00 | 294 |
| stroke 187 | 74 % → 0 % | 267.2 px | 0.00 | 0.00 | 212 |
| stroke 188 | 76 % → 0 % | 302.9 px | 0.00 | 0.00 | 125 |
| stroke 189 | 74 % → 0 % | 464.5 px | 0.00 | 0.00 | 48 |
| stroke 190 | 1 % → 2 % | 21.6 px | 0.29 | 1.65 | 12 |

Numbers say: wet paint spreads well beyond the stroke.

## Refs v3 · #45 Pastel pepper — own sheet
own sheet 800 × 800 · Pastel 1.00 · 64 px · 33.2 s

![Refs v3 · #45 Pastel pepper — own sheet](Refs-v3-45-Pastel-pepper-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 4 % → 63 % | 56.0 px | 0.62 | 17.60 | 35 |
| stroke 2 | 7 % → 73 % | 47.1 px | 0.67 | 10.42 | 161 |
| stroke 3 | 8 % → 73 % | 55.4 px | 0.68 | 8.86 | 149 |
| stroke 4 | 17 % → 81 % | 105.0 px | 0.67 | 4.84 | 221 |
| stroke 5 | 18 % → 73 % | 131.9 px | 0.65 | 4.05 | 121 |
| stroke 6 | 34 % → 88 % | 335.5 px | 0.65 | 2.61 | 65 |
| stroke 7 | 23 % → 62 % | 264.1 px | 0.67 | 2.75 | 71 |
| stroke 8 | 25 % → 66 % | 228.0 px | 0.63 | 2.70 | 90 |
| stroke 9 | 22 % → 58 % | 338.5 px | 0.62 | 2.65 | 47 |
| stroke 10 | 22 % → 75 % | 293.1 px | 0.68 | 3.35 | 97 |
| stroke 11 | 29 % → 79 % | 327.1 px | 0.65 | 2.70 | 103 |
| stroke 12 | 34 % → 83 % | 301.0 px | 0.67 | 2.39 | 147 |
| stroke 13 | 9 % → 93 % | 51.7 px | 0.60 | 10.62 | 218 |
| stroke 14 | 16 % → 92 % | 114.8 px | 0.65 | 5.72 | 216 |
| stroke 15 | 22 % → 98 % | 144.2 px | 0.61 | 4.42 | 216 |
| stroke 16 | 15 % → 94 % | 107.4 px | 0.70 | 6.09 | 111 |
| stroke 17 | 20 % → 75 % | 132.5 px | 0.60 | 3.67 | 129 |
| stroke 18 | 14 % → 72 % | 71.4 px | 0.56 | 4.97 | 155 |
| stroke 19 | 31 % → 87 % | 205.0 px | 0.58 | 2.78 | 225 |
| stroke 20 | 34 % → 73 % | 283.9 px | 0.56 | 2.12 | 151 |
| stroke 21 | 46 % → 92 % | 303.7 px | 0.55 | 2.02 | 116 |
| stroke 22 | 24 % → 67 % | 157.5 px | 0.60 | 2.84 | 109 |
| stroke 23 | 19 % → 98 % | 300.9 px | 0.72 | 5.18 | 35 |
| stroke 24 | 21 % → 94 % | 166.0 px | 0.71 | 4.40 | 129 |
| stroke 25 | 38 % → 98 % | 238.8 px | 0.63 | 2.58 | 220 |
| stroke 26 | 51 % → 93 % | 319.5 px | 0.58 | 1.81 | 112 |
| stroke 27 | 32 % → 75 % | 295.6 px | 0.61 | 2.38 | 71 |
| stroke 28 | 43 % → 88 % | 424.2 px | 0.62 | 2.03 | 48 |
| stroke 29 | 50 % → 98 % | 699.8 px | 0.61 | 1.95 | 56 |
| stroke 30 | 32 % → 60 % | 401.3 px | 0.55 | 1.84 | 59 |
| stroke 31 | 45 % → 88 % | 407.8 px | 0.61 | 1.98 | 99 |
| stroke 32 | 45 % → 89 % | 508.0 px | 0.63 | 1.99 | 49 |
| stroke 33 | 60 % → 83 % | 769.4 px | 0.53 | 1.39 | 48 |
| stroke 34 | 58 % → 99 % | 686.6 px | 0.58 | 1.71 | 99 |
| stroke 35 | 58 % → 91 % | 535.9 px | 0.56 | 1.56 | 105 |
| stroke 36 | 59 % → 99 % | 858.8 px | 0.58 | 1.67 | 87 |
| stroke 37 | 53 % → 74 % | 589.4 px | 0.54 | 1.40 | 101 |
| stroke 38 | 39 % → 66 % | 247.7 px | 0.60 | 1.69 | 99 |
| stroke 39 | 59 % → 99 % | 931.7 px | 0.59 | 1.67 | 42 |
| stroke 40 | 62 % → 92 % | 553.2 px | 0.58 | 1.48 | 121 |
| stroke 41 | 61 % → 67 % | 471.3 px | 0.50 | 1.09 | 68 |
| stroke 42 | 37 % → 68 % | 521.1 px | 0.60 | 1.86 | 40 |
| stroke 43 | 34 % → 94 % | 487.1 px | 0.65 | 2.79 | 63 |
| stroke 44 | 57 % → 98 % | 839.2 px | 0.60 | 1.71 | 72 |
| stroke 45 | 33 % → 96 % | 255.2 px | 0.67 | 2.91 | 34 |
| stroke 46 | 9 % → 53 % | 65.6 px | 0.62 | 6.19 | 33 |
| stroke 47 | 17 % → 48 % | 130.2 px | 0.58 | 2.82 | 37 |
| stroke 48 | 17 % → 66 % | 135.3 px | 0.65 | 3.95 | 39 |
| stroke 49 | 23 % → 57 % | 260.3 px | 0.61 | 2.44 | 24 |
| stroke 50 | 25 % → 79 % | 496.8 px | 0.66 | 3.11 | 15 |
| stroke 51 | 20 % → 59 % | 366.8 px | 0.66 | 3.01 | 14 |
| stroke 52 | 22 % → 49 % | 340.8 px | 0.63 | 2.23 | 16 |
| stroke 53 | 27 % → 55 % | 459.0 px | 0.60 | 2.04 | 13 |
| stroke 54 | 27 % → 51 % | 429.0 px | 0.60 | 1.90 | 23 |
| stroke 55 | 26 % → 65 % | 221.6 px | 0.65 | 2.48 | 51 |
| stroke 56 | 26 % → 80 % | 526.7 px | 0.67 | 3.08 | 25 |
| stroke 57 | 36 % → 52 % | 291.7 px | 0.58 | 1.45 | 42 |
| stroke 58 | 37 % → 61 % | 587.3 px | 0.61 | 1.64 | 17 |
| stroke 59 | 32 % → 67 % | 209.2 px | 0.64 | 2.09 | 147 |
| stroke 60 | 36 % → 65 % | 294.2 px | 0.64 | 1.82 | 129 |
| stroke 61 | 41 % → 63 % | 506.0 px | 0.61 | 1.55 | 60 |
| stroke 62 | 50 % → 73 % | 347.9 px | 0.63 | 1.46 | 154 |
| stroke 63 | 57 % → 86 % | 531.3 px | 0.64 | 1.52 | 122 |
| stroke 64 | 69 % → 90 % | 590.1 px | 0.61 | 1.29 | 91 |
| stroke 65 | 64 % → 76 % | 556.9 px | 0.60 | 1.18 | 202 |
| stroke 66 | 70 % → 86 % | 701.9 px | 0.63 | 1.23 | 154 |
| stroke 67 | 71 % → 76 % | 1018.0 px | 0.64 | 1.07 | 59 |
| stroke 68 | 78 % → 87 % | 1218.3 px | 0.63 | 1.11 | 68 |
| stroke 69 | 77 % → 85 % | 1019.2 px | 0.63 | 1.10 | 90 |
| stroke 70 | 34 % → 53 % | 286.7 px | 0.64 | 1.55 | 157 |
| stroke 71 | 32 % → 44 % | 488.5 px | 0.63 | 1.38 | 62 |
| stroke 72 | 44 % → 78 % | 234.8 px | 0.65 | 1.75 | 149 |
| stroke 73 | 45 % → 89 % | 294.5 px | 0.66 | 1.97 | 240 |
| stroke 74 | 47 % → 70 % | 239.7 px | 0.66 | 1.48 | 219 |
| stroke 75 | 66 % → 87 % | 514.8 px | 0.67 | 1.31 | 107 |
| stroke 76 | 57 % → 92 % | 367.2 px | 0.67 | 1.61 | 397 |
| stroke 77 | 70 % → 92 % | 970.0 px | 0.69 | 1.31 | 79 |
| stroke 78 | 53 % → 84 % | 620.2 px | 0.66 | 1.59 | 75 |
| stroke 79 | 66 % → 95 % | 688.3 px | 0.66 | 1.44 | 117 |
| stroke 80 | 63 % → 99 % | 850.0 px | 0.71 | 1.56 | 131 |
| stroke 81 | 66 % → 96 % | 553.8 px | 0.68 | 1.46 | 204 |
| stroke 82 | 57 % → 83 % | 494.1 px | 0.67 | 1.44 | 219 |
| stroke 83 | 71 % → 90 % | 777.0 px | 0.67 | 1.26 | 165 |
| stroke 84 | 60 % → 99 % | 809.4 px | 0.71 | 1.65 | 130 |
| stroke 85 | 68 % → 90 % | 1039.5 px | 0.65 | 1.33 | 92 |
| stroke 86 | 73 % → 77 % | 300.3 px | 0.63 | 1.06 | 282 |
| stroke 87 | 80 % → 82 % | 536.0 px | 0.66 | 1.03 | 215 |
| stroke 88 | 71 % → 97 % | 470.2 px | 0.68 | 1.37 | 209 |
| stroke 89 | 79 % → 98 % | 587.8 px | 0.66 | 1.24 | 198 |
| stroke 90 | 87 % → 97 % | 700.7 px | 0.66 | 1.11 | 179 |
| stroke 91 | 85 % → 99 % | 663.0 px | 0.64 | 1.16 | 114 |
| stroke 92 | 87 % → 99 % | 901.4 px | 0.60 | 1.14 | 96 |
| stroke 93 | 91 % → 98 % | 1361.4 px | 0.63 | 1.08 | 79 |
| stroke 94 | 88 % → 99 % | 657.9 px | 0.66 | 1.13 | 163 |
| stroke 95 | 85 % → 92 % | 1213.9 px | 0.68 | 1.09 | 72 |
| stroke 96 | 91 % → 97 % | 989.6 px | 0.68 | 1.07 | 113 |
| stroke 97 | 87 % → 97 % | 1349.1 px | 0.65 | 1.12 | 101 |
| stroke 98 | 94 % → 99 % | 1073.0 px | 0.71 | 1.05 | 121 |
| stroke 99 | 94 % → 98 % | 1559.3 px | 0.62 | 1.05 | 60 |
| stroke 100 | 62 % → 80 % | 318.1 px | 0.60 | 1.29 | 228 |
| stroke 101 | 72 % → 81 % | 423.5 px | 0.59 | 1.13 | 232 |
| stroke 102 | 68 % → 80 % | 515.2 px | 0.60 | 1.17 | 262 |
| stroke 103 | 60 % → 69 % | 446.0 px | 0.62 | 1.15 | 115 |
| stroke 104 | 75 % → 81 % | 461.0 px | 0.64 | 1.08 | 157 |
| stroke 105 | 54 % → 57 % | 696.9 px | 0.62 | 1.06 | 8 |
| stroke 106 | 65 % → 68 % | 744.3 px | 0.62 | 1.05 | 14 |
| stroke 107 | 56 % → 62 % | 445.3 px | 0.63 | 1.10 | 61 |
| stroke 108 | 51 % → 52 % | 1143.3 px | 0.60 | 1.02 | 5 |
| stroke 109 | 54 % → 55 % | 853.0 px | 0.61 | 1.01 | 15 |
| stroke 110 | 68 % → 68 % | 1299.7 px | 0.61 | 1.01 | 8 |
| stroke 111 | 87 % → 95 % | 1477.2 px | 0.67 | 1.10 | 16 |
| stroke 112 | 80 % → 87 % | 986.8 px | 0.68 | 1.09 | 24 |
| stroke 113 | 92 % → 99 % | 1138.0 px | 0.58 | 1.08 | 37 |
| stroke 114 | 94 % → 99 % | 1251.6 px | 0.72 | 1.04 | 44 |
| stroke 115 | 91 % → 93 % | 776.9 px | 0.63 | 1.02 | 67 |
| stroke 116 | 88 % → 94 % | 1211.0 px | 0.67 | 1.06 | 16 |
| stroke 117 | 91 % → 95 % | 1125.7 px | 0.63 | 1.05 | 47 |
| stroke 118 | 91 % → 94 % | 829.0 px | 0.70 | 1.03 | 58 |
| stroke 119 | 92 % → 97 % | 1337.5 px | 0.69 | 1.06 | 21 |
| stroke 120 | 82 % → 87 % | 1474.9 px | 0.66 | 1.06 | 23 |
| stroke 121 | 75 % → 80 % | 1461.5 px | 0.66 | 1.06 | 19 |
| stroke 122 | 90 % → 95 % | 1627.5 px | 0.67 | 1.06 | 18 |
| stroke 123 | 87 % → 90 % | 1209.9 px | 0.67 | 1.04 | 23 |
| stroke 124 | 88 % → 91 % | 994.1 px | 0.65 | 1.04 | 28 |
| stroke 125 | 80 % → 83 % | 1032.8 px | 0.66 | 1.04 | 24 |
| stroke 126 | 88 % → 91 % | 2100.0 px | 0.66 | 1.03 | 12 |
| stroke 127 | 91 % → 92 % | 886.7 px | 0.61 | 1.02 | 50 |
| stroke 128 | 95 % → 97 % | 2507.7 px | 0.60 | 1.02 | 12 |
| stroke 129 | 92 % → 94 % | 1426.6 px | 0.67 | 1.02 | 28 |
| stroke 130 | 96 % → 99 % | 1972.9 px | 0.58 | 1.03 | 18 |
| stroke 131 | 89 % → 91 % | 1899.5 px | 0.66 | 1.01 | 26 |
| stroke 132 | 90 % → 91 % | 1317.4 px | 0.58 | 1.01 | 28 |
| stroke 133 | 94 % → 96 % | 1683.4 px | 0.68 | 1.02 | 21 |
| stroke 134 | 98 % → 99 % | 1418.9 px | 0.72 | 1.01 | 33 |
| stroke 135 | 91 % → 92 % | 1141.4 px | 0.62 | 1.00 | 29 |
| stroke 136 | 92 % → 94 % | 1409.0 px | 0.68 | 1.01 | 12 |
| stroke 137 | 82 % → 82 % | 1583.7 px | 0.67 | 1.01 | 21 |
| stroke 138 | 91 % → 91 % | 2107.0 px | 0.62 | 1.00 | 15 |
| stroke 139 | 78 % → 79 % | 2470.4 px | 0.66 | 1.01 | 10 |
| stroke 140 | 98 % → 99 % | 2261.6 px | 0.61 | 1.01 | 17 |
| stroke 141 | 94 % → 94 % | 1782.5 px | 0.67 | 1.01 | 24 |
| stroke 142 | 92 % → 93 % | 1783.0 px | 0.67 | 1.01 | 18 |
| stroke 143 | 96 % → 97 % | 1718.5 px | 0.70 | 1.01 | 31 |
| stroke 144 | 98 % → 99 % | 2589.2 px | 0.71 | 1.01 | 9 |
| stroke 145 | 89 % → 89 % | 1874.9 px | 0.66 | 1.00 | 19 |
| stroke 146 | 98 % → 99 % | 2271.9 px | 0.59 | 1.01 | 16 |
| stroke 147 | 89 % → 89 % | 2828.3 px | 0.66 | 1.00 | 14 |
| stroke 148 | 83 % → 83 % | 1765.9 px | 0.67 | 1.00 | 29 |
| stroke 149 | 90 % → 90 % | 2852.4 px | 0.66 | 1.01 | 11 |
| stroke 150 | 90 % → 90 % | 2394.0 px | 0.65 | 1.00 | 14 |
| stroke 151 | 95 % → 95 % | 2548.7 px | 0.65 | 1.00 | 7 |
| stroke 152 | 90 % → 90 % | 2524.6 px | 0.60 | 1.00 | 13 |
| stroke 153 | 89 % → 89 % | 2390.3 px | 0.58 | 1.00 | 10 |
| stroke 154 | 98 % → 99 % | 2557.9 px | 0.69 | 1.01 | 17 |
| stroke 155 | 99 % → 99 % | 2652.6 px | 0.73 | 1.00 | 14 |
| stroke 156 | 78 % → 78 % | 2463.7 px | 0.66 | 1.00 | 11 |
| stroke 157 | 79 % → 81 % | 1221.3 px | 0.59 | 1.01 | 15 |
| stroke 158 | 82 % → 84 % | 727.5 px | 0.60 | 1.02 | 68 |
| stroke 159 | 96 % → 97 % | 2516.4 px | 0.60 | 1.02 | 14 |
| stroke 160 | 90 % → 91 % | 1237.9 px | 0.60 | 1.02 | 37 |
| stroke 161 | 88 % → 92 % | 734.2 px | 0.57 | 1.04 | 38 |
| stroke 162 | 57 % → 60 % | 1336.5 px | 0.58 | 1.06 | 5 |
| stroke 163 | 86 % → 89 % | 1001.1 px | 0.57 | 1.03 | 46 |
| stroke 164 | 69 % → 71 % | 1077.3 px | 0.56 | 1.02 | 14 |
| stroke 165 | 73 % → 75 % | 1559.6 px | 0.56 | 1.02 | 24 |
| stroke 166 | 96 % → 98 % | 1575.5 px | 0.58 | 1.02 | 25 |
| stroke 167 | 81 % → 83 % | 1048.3 px | 0.57 | 1.02 | 37 |
| stroke 168 | 85 % → 87 % | 1153.2 px | 0.61 | 1.02 | 27 |
| stroke 169 | 86 % → 87 % | 1078.8 px | 0.61 | 1.01 | 29 |
| stroke 170 | 57 % → 58 % | 1492.4 px | 0.58 | 1.02 | 5 |
| stroke 171 | 84 % → 86 % | 2244.7 px | 0.62 | 1.02 | 16 |
| stroke 172 | 96 % → 97 % | 1118.6 px | 0.57 | 1.01 | 43 |
| stroke 173 | 93 % → 93 % | 1661.8 px | 0.60 | 1.00 | 21 |
| stroke 174 | 87 % → 87 % | 2094.3 px | 0.62 | 1.00 | 23 |
| stroke 175 | 64 % → 64 % | 1380.0 px | 0.58 | 1.00 | 7 |
| stroke 176 | 93 % → 93 % | 2424.0 px | 0.60 | 1.00 | 14 |
| stroke 177 | 70 % → 70 % | 1485.9 px | 0.57 | 1.00 | 15 |
| stroke 178 | 88 % → 88 % | 2259.7 px | 0.61 | 1.01 | 12 |
| stroke 179 | 92 % → 92 % | 2178.5 px | 0.60 | 1.00 | 18 |
| stroke 180 | 88 % → 88 % | 2794.6 px | 0.62 | 1.00 | 8 |
| stroke 181 | 99 % → 99 % | 2574.1 px | 0.57 | 1.00 | 12 |
| stroke 182 | 56 % → 60 % | 724.2 px | 0.67 | 1.06 | 29 |
| stroke 183 | 69 % → 72 % | 675.2 px | 0.67 | 1.04 | 32 |
| stroke 184 | 71 % → 73 % | 560.9 px | 0.66 | 1.03 | 59 |
| stroke 185 | 86 % → 87 % | 888.0 px | 0.67 | 1.01 | 38 |
| stroke 186 | 56 % → 57 % | 667.8 px | 0.64 | 1.03 | 20 |
| stroke 187 | 87 % → 87 % | 987.8 px | 0.67 | 1.01 | 34 |
| stroke 188 | 66 % → 66 % | 1090.4 px | 0.64 | 1.00 | 16 |
| stroke 189 | 87 % → 87 % | 1028.4 px | 0.67 | 1.00 | 61 |
| stroke 190 | 90 % → 90 % | 1918.4 px | 0.67 | 1.00 | 18 |
| stroke 191 | 88 % → 88 % | 1837.8 px | 0.67 | 1.00 | 22 |
| stroke 192 | 83 % → 83 % | 1324.8 px | 0.68 | 1.01 | 24 |
| stroke 193 | 73 % → 73 % | 1489.3 px | 0.67 | 1.00 | 12 |
| stroke 194 | 79 % → 80 % | 2184.9 px | 0.67 | 1.01 | 15 |
| stroke 195 | 76 % → 76 % | 1880.8 px | 0.63 | 1.01 | 16 |
| stroke 196 | 72 % → 72 % | 750.8 px | 0.60 | 1.00 | 20 |
| stroke 197 | 78 % → 78 % | 619.9 px | 0.66 | 1.00 | 74 |
| stroke 198 | 88 % → 88 % | 1143.4 px | 0.67 | 1.00 | 28 |
| stroke 199 | 97 % → 97 % | 1233.3 px | 0.62 | 1.00 | 30 |

Numbers say: wet paint spreads well beyond the stroke.

## Refs v3 · #46 Ink lips on wet paper — own sheet
own sheet 800 × 1047 · Watercolour 1.00 + water 65 % · 56 px · 25.0 s

![Refs v3 · #46 Ink lips on wet paper — own sheet](Refs-v3-46-Ink-lips-on-wet-paper-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 14 % → 20 % | 61.3 px | 0.60 | 1.45 | 282 |
| stroke 2 | 13 % → 17 % | 60.1 px | 0.50 | 1.25 | 290 |

## Refs v3 · #47 Pink knife slabs — own sheet
own sheet 800 × 1190 · Impasto 1.00 · 112 px · 30.9 s

![Refs v3 · #47 Pink knife slabs — own sheet](Refs-v3-47-Pink-knife-slabs-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 12 % → 0 % | 114.8 px | 0.00 | 0.00 | 51 |
| stroke 2 | 26 % → 0 % | 138.9 px | 0.00 | 0.00 | 113 |
| stroke 3 | 33 % → 0 % | 135.0 px | 0.04 | 0.01 | 197 |
| stroke 4 | 40 % → 0 % | 178.1 px | 0.04 | 0.00 | 204 |
| stroke 5 | 43 % → 0 % | 307.1 px | 0.00 | 0.00 | 121 |
| stroke 6 | 44 % → 0 % | 477.1 px | 0.04 | 0.01 | 44 |
| stroke 7 | 51 % → 0 % | 355.3 px | 0.00 | 0.00 | 125 |
| stroke 8 | 52 % → 0 % | 537.2 px | 0.04 | 0.01 | 59 |
| stroke 9 | 51 % → 0 % | 735.1 px | 0.00 | 0.00 | 51 |
| stroke 10 | 52 % → 0 % | 647.9 px | 0.00 | 0.00 | 81 |
| stroke 11 | 51 % → 0 % | 540.2 px | 0.04 | 0.01 | 65 |
| stroke 12 | 50 % → 0 % | 407.2 px | 0.00 | 0.00 | 122 |
| stroke 13 | 47 % → 0 % | 618.2 px | 0.04 | 0.01 | 58 |
| stroke 14 | 52 % → 0 % | 824.8 px | 0.00 | 0.00 | 38 |
| stroke 15 | 41 % → 0 % | 516.4 px | 0.04 | 0.01 | 50 |
| stroke 16 | 44 % → 0 % | 368.8 px | 0.06 | 0.01 | 95 |
| stroke 17 | 36 % → 1 % | 582.7 px | 0.05 | 0.02 | 38 |
| stroke 18 | 43 % → 0 % | 366.2 px | 0.06 | 0.01 | 91 |
| stroke 19 | 34 % → 1 % | 393.2 px | 0.05 | 0.03 | 54 |
| stroke 20 | 43 % → 0 % | 305.7 px | 0.05 | 0.01 | 138 |
| stroke 21 | 41 % → 1 % | 395.4 px | 0.05 | 0.02 | 71 |
| stroke 22 | 45 % → 0 % | 310.2 px | 0.05 | 0.01 | 154 |
| stroke 23 | 45 % → 1 % | 401.4 px | 0.05 | 0.02 | 84 |
| stroke 24 | 50 % → 0 % | 329.9 px | 0.05 | 0.01 | 177 |
| stroke 25 | 45 % → 1 % | 603.5 px | 0.05 | 0.01 | 46 |
| stroke 26 | 51 % → 0 % | 393.1 px | 0.05 | 0.01 | 134 |
| stroke 27 | 47 % → 1 % | 623.8 px | 0.05 | 0.01 | 43 |
| stroke 28 | 53 % → 0 % | 741.3 px | 0.00 | 0.00 | 56 |
| stroke 29 | 55 % → 0 % | 445.4 px | 0.05 | 0.01 | 131 |
| stroke 30 | 50 % → 0 % | 1082.4 px | 0.00 | 0.00 | 19 |
| stroke 31 | 53 % → 0 % | 465.0 px | 0.05 | 0.01 | 108 |
| stroke 32 | 47 % → 0 % | 613.5 px | 0.00 | 0.00 | 48 |
| stroke 33 | 52 % → 0 % | 437.3 px | 0.05 | 0.01 | 99 |
| stroke 34 | 41 % → 0 % | 504.8 px | 0.00 | 0.00 | 50 |
| stroke 35 | 48 % → 0 % | 373.4 px | 0.05 | 0.01 | 117 |
| stroke 36 | 36 % → 0 % | 451.8 px | 0.00 | 0.00 | 47 |
| stroke 37 | 45 % → 0 % | 372.4 px | 0.05 | 0.01 | 115 |
| stroke 38 | 35 % → 0 % | 361.5 px | 0.00 | 0.00 | 64 |
| stroke 39 | 41 % → 0 % | 339.5 px | 0.04 | 0.00 | 116 |
| stroke 40 | 32 % → 0 % | 379.9 px | 0.00 | 0.00 | 48 |
| stroke 41 | 39 % → 0 % | 327.9 px | 0.00 | 0.00 | 97 |
| stroke 42 | 39 % → 0 % | 365.9 px | 0.00 | 0.00 | 79 |
| stroke 43 | 48 % → 0 % | 486.9 px | 0.00 | 0.00 | 63 |
| stroke 44 | 51 % → 0 % | 359.3 px | 0.00 | 0.00 | 121 |
| stroke 45 | 59 % → 0 % | 649.6 px | 0.00 | 0.00 | 56 |
| stroke 46 | 54 % → 0 % | 436.5 px | 0.00 | 0.00 | 81 |
| stroke 47 | 58 % → 0 % | 835.3 px | 0.00 | 0.00 | 26 |
| stroke 48 | 18 % → 0 % | 47.6 px | 0.00 | 0.00 | 137 |
| stroke 49 | 24 % → 0 % | 82.9 px | 0.00 | 0.00 | 124 |
| stroke 50 | 28 % → 0 % | 305.1 px | 0.00 | 0.00 | 20 |
| stroke 51 | 29 % → 0 % | 249.1 px | 0.00 | 0.00 | 40 |
| stroke 52 | 29 % → 0 % | 467.6 px | 0.00 | 0.00 | 9 |
| stroke 53 | 30 % → 0 % | 589.0 px | 0.00 | 0.00 | 15 |
| stroke 54 | 18 % → 0 % | 694.6 px | 0.04 | 0.01 | 5 |
| stroke 55 | 15 % → 0 % | 455.5 px | 0.04 | 0.02 | 13 |
| stroke 56 | 5 % → 0 % | 205.9 px | 0.04 | 0.05 | 5 |
| stroke 57 | 6 % → 0 % | 139.5 px | 0.04 | 0.04 | 23 |
| stroke 58 | 9 % → 0 % | 122.3 px | 0.04 | 0.02 | 59 |
| stroke 59 | 11 % → 0 % | 117.6 px | 0.04 | 0.02 | 72 |
| stroke 60 | 17 % → 0 % | 356.5 px | 0.05 | 0.02 | 24 |
| stroke 61 | 18 % → 1 % | 382.4 px | 0.05 | 0.04 | 22 |
| stroke 62 | 19 % → 0 % | 897.3 px | 0.05 | 0.03 | 14 |
| stroke 63 | 4 % → 0 % | 118.4 px | 0.00 | 0.00 | 4 |
| stroke 64 | 2 % → 0 % | 63.2 px | 0.00 | 0.00 | 2 |
| stroke 65 | 4 % → 0 % | 98.8 px | 0.00 | 0.00 | 18 |
| stroke 66 | 7 % → 0 % | 99.8 px | 0.06 | 0.05 | 44 |
| stroke 67 | 8 % → 0 % | 119.5 px | 0.05 | 0.05 | 32 |
| stroke 68 | 9 % → 0 % | 190.4 px | 0.05 | 0.04 | 20 |
| stroke 69 | 10 % → 0 % | 200.3 px | 0.05 | 0.04 | 21 |
| stroke 70 | 12 % → 0 % | 211.3 px | 0.05 | 0.03 | 28 |
| stroke 71 | 13 % → 0 % | 246.4 px | 0.05 | 0.03 | 23 |
| stroke 72 | 15 % → 0 % | 290.4 px | 0.05 | 0.02 | 20 |
| stroke 73 | 16 % → 0 % | 296.1 px | 0.03 | 0.00 | 17 |
| stroke 74 | 17 % → 0 % | 285.1 px | 0.00 | 0.00 | 28 |
| stroke 75 | 17 % → 0 % | 381.8 px | 0.00 | 0.00 | 18 |
| stroke 76 | 3 % → 0 % | 64.8 px | 0.00 | 0.00 | 8 |
| stroke 77 | 11 % → 0 % | 327.3 px | 0.00 | 0.00 | 3 |
| stroke 78 | 13 % → 0 % | 299.6 px | 0.00 | 0.00 | 9 |
| stroke 79 | 15 % → 0 % | 289.1 px | 0.00 | 0.00 | 8 |
| stroke 80 | 19 % → 0 % | 271.2 px | 0.00 | 0.00 | 16 |
| stroke 81 | 25 % → 0 % | 246.1 px | 0.00 | 0.00 | 15 |
| stroke 82 | 16 % → 0 % | 521.2 px | 0.00 | 0.00 | 10 |
| stroke 83 | 15 % → 0 % | 472.2 px | 0.00 | 0.00 | 13 |
| stroke 84 | 19 % → 0 % | 374.4 px | 0.00 | 0.00 | 17 |
| stroke 85 | 22 % → 0 % | 298.3 px | 0.00 | 0.00 | 31 |
| stroke 86 | 25 % → 0 % | 258.4 px | 0.00 | 0.00 | 32 |
| stroke 87 | 1 % → 1 % | 22.6 px | 0.04 | 0.99 | 3 |
| stroke 88 | 0 % → 0 % | 23.1 px | 0.05 | 0.98 | 4 |

## Refs v3 · #48 Black bands with drips — own sheet
own sheet 800 × 1045 · Watercolour 1.00 + water 35 % · 112 px · 82.4 s

![Refs v3 · #48 Black bands with drips — own sheet](Refs-v3-48-Black-bands-with-drips-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 13 % → 96 % | 77.6 px | 0.30 | 7.48 | 265 |
| stroke 2 | 16 % → 95 % | 125.3 px | 0.30 | 6.02 | 324 |
| stroke 3 | 34 % → 92 % | 107.3 px | 0.30 | 2.71 | 1565 |
| stroke 4 | 43 % → 93 % | 152.9 px | 0.30 | 2.18 | 1786 |
| stroke 5 | 47 % → 93 % | 229.2 px | 0.29 | 2.00 | 1484 |
| stroke 6 | 51 % → 93 % | 257.9 px | 0.29 | 1.84 | 1523 |
| stroke 7 | 56 % → 95 % | 264.9 px | 0.29 | 1.70 | 1604 |
| stroke 8 | 57 % → 96 % | 272.1 px | 0.29 | 1.68 | 1873 |
| stroke 9 | 58 % → 96 % | 278.2 px | 0.29 | 1.66 | 1813 |
| stroke 10 | 56 % → 96 % | 348.0 px | 0.29 | 1.71 | 1373 |
| stroke 11 | 56 % → 96 % | 355.5 px | 0.29 | 1.71 | 1336 |
| stroke 12 | 57 % → 95 % | 296.6 px | 0.29 | 1.66 | 1566 |
| stroke 13 | 58 % → 92 % | 275.5 px | 0.28 | 1.58 | 1784 |
| stroke 14 | 58 % → 83 % | 275.1 px | 0.28 | 1.44 | 1592 |
| stroke 15 | 56 % → 74 % | 299.8 px | 0.28 | 1.32 | 1336 |
| stroke 16 | 58 % → 66 % | 275.5 px | 0.28 | 1.13 | 1628 |
| stroke 17 | 56 % → 57 % | 354.8 px | 0.28 | 1.02 | 1521 |
| stroke 18 | 53 % → 53 % | 819.0 px | 0.28 | 1.00 | 201 |

Numbers say: wet paint spreads well beyond the stroke.

## Refs v3 · #49 Magenta letters round — own sheet
own sheet 800 × 1000 · Ink 0.98 · 64 px · 39.7 s

![Refs v3 · #49 Magenta letters round — own sheet](Refs-v3-49-Magenta-letters-round-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 2 % → 29 % | 49.1 px | 0.48 | 13.43 | 12 |
| stroke 2 | 4 % → 27 % | 122.7 px | 0.48 | 7.23 | 14 |
| stroke 3 | 4 % → 21 % | 59.7 px | 0.49 | 5.04 | 23 |
| stroke 4 | 8 % → 24 % | 103.1 px | 0.48 | 2.91 | 16 |
| stroke 5 | 16 % → 27 % | 97.0 px | 0.48 | 1.70 | 123 |
| stroke 6 | 8 % → 25 % | 51.8 px | 0.46 | 3.25 | 57 |
| stroke 7 | 19 % → 30 % | 133.6 px | 0.47 | 1.61 | 46 |
| stroke 8 | 4 % → 36 % | 65.6 px | 0.48 | 8.05 | 61 |
| stroke 9 | 8 % → 37 % | 127.4 px | 0.48 | 4.54 | 43 |
| stroke 10 | 12 % → 28 % | 147.7 px | 0.48 | 2.31 | 59 |
| stroke 11 | 16 % → 33 % | 274.7 px | 0.48 | 2.01 | 32 |
| stroke 12 | 17 % → 30 % | 210.5 px | 0.48 | 1.73 | 44 |
| stroke 13 | 31 % → 35 % | 158.8 px | 0.47 | 1.13 | 206 |
| stroke 14 | 20 % → 27 % | 58.6 px | 0.49 | 1.37 | 469 |
| stroke 15 | 9 % → 35 % | 200.3 px | 0.48 | 3.74 | 28 |
| stroke 16 | 16 % → 36 % | 115.5 px | 0.47 | 2.25 | 125 |
| stroke 17 | 24 % → 35 % | 237.4 px | 0.48 | 1.46 | 114 |
| stroke 18 | 25 % → 37 % | 390.4 px | 0.48 | 1.48 | 48 |
| stroke 19 | 25 % → 37 % | 261.3 px | 0.48 | 1.45 | 100 |
| stroke 20 | 13 % → 35 % | 501.6 px | 0.48 | 2.62 | 5 |
| stroke 21 | 23 % → 38 % | 104.5 px | 0.48 | 1.69 | 258 |
| stroke 22 | 18 % → 38 % | 143.5 px | 0.47 | 2.04 | 91 |
| stroke 23 | 14 % → 41 % | 159.6 px | 0.47 | 2.95 | 87 |
| stroke 24 | 9 % → 42 % | 89.1 px | 0.48 | 4.61 | 102 |
| stroke 25 | 21 % → 30 % | 264.7 px | 0.47 | 1.40 | 49 |
| stroke 26 | 29 % → 33 % | 359.7 px | 0.47 | 1.12 | 64 |
| stroke 27 | 29 % → 32 % | 352.6 px | 0.47 | 1.13 | 54 |
| stroke 28 | 6 % → 46 % | 62.1 px | 0.48 | 7.57 | 49 |
| stroke 29 | 27 % → 35 % | 136.1 px | 0.47 | 1.31 | 193 |
| stroke 30 | 33 % → 38 % | 208.7 px | 0.48 | 1.17 | 141 |
| stroke 31 | 25 % → 36 % | 74.0 px | 0.47 | 1.47 | 392 |
| stroke 32 | 26 % → 40 % | 95.9 px | 0.48 | 1.54 | 278 |
| stroke 33 | 18 % → 38 % | 290.2 px | 0.48 | 2.16 | 56 |
| stroke 34 | 10 % → 38 % | 127.0 px | 0.48 | 3.64 | 91 |
| stroke 35 | 29 % → 35 % | 195.2 px | 0.48 | 1.22 | 151 |
| stroke 36 | 27 % → 33 % | 309.0 px | 0.48 | 1.22 | 84 |
| stroke 37 | 11 % → 30 % | 92.5 px | 0.49 | 2.68 | 56 |
| stroke 38 | 23 % → 35 % | 259.2 px | 0.48 | 1.54 | 64 |
| stroke 39 | 21 % → 30 % | 175.1 px | 0.48 | 1.45 | 40 |
| stroke 40 | 9 % → 23 % | 161.2 px | 0.49 | 2.57 | 21 |
| stroke 41 | 19 % → 30 % | 254.7 px | 0.48 | 1.55 | 40 |
| stroke 42 | 27 % → 29 % | 199.4 px | 0.48 | 1.08 | 168 |
| stroke 43 | 25 % → 26 % | 570.6 px | 0.49 | 1.04 | 20 |
| stroke 44 | 35 % → 36 % | 280.8 px | 0.49 | 1.03 | 80 |

Numbers say: wet paint spreads well beyond the stroke.

## Refs v3 · #50 Swipes on seaside — own sheet
own sheet 800 × 1160 · Gouache 1.00 + water 15 % · 80 px · 76.8 s

![Refs v3 · #50 Swipes on seaside — own sheet](Refs-v3-50-Swipes-on-seaside-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 10 % → 0 % | 75.6 px | 0.00 | 0.00 | 203 |
| stroke 2 | 13 % → 0 % | 184.5 px | 0.00 | 0.00 | 117 |
| stroke 3 | 11 % → 0 % | 75.2 px | 0.00 | 0.00 | 277 |
| stroke 4 | 21 % → 0 % | 281.7 px | 0.00 | 0.00 | 94 |
| stroke 5 | 8 % → 0 % | 112.0 px | 0.00 | 0.00 | 125 |
| stroke 6 | 15 % → 0 % | 116.3 px | 0.00 | 0.00 | 281 |
| stroke 7 | 27 % → 0 % | 122.2 px | 0.00 | 0.00 | 834 |
| stroke 8 | 39 % → 0 % | 342.0 px | 0.00 | 0.00 | 169 |
| stroke 9 | 35 % → 0 % | 177.3 px | 0.00 | 0.00 | 628 |
| stroke 10 | 46 % → 4 % | 270.3 px | 0.36 | 0.08 | 417 |
| stroke 11 | 39 % → 3 % | 306.5 px | 0.37 | 0.07 | 224 |
| stroke 12 | 48 % → 11 % | 264.4 px | 0.39 | 0.23 | 450 |
| stroke 13 | 45 % → 12 % | 285.6 px | 0.38 | 0.28 | 364 |
| stroke 14 | 50 % → 20 % | 259.7 px | 0.41 | 0.40 | 625 |
| stroke 15 | 51 % → 23 % | 290.6 px | 0.40 | 0.45 | 416 |
| stroke 16 | 52 % → 32 % | 245.0 px | 0.41 | 0.62 | 779 |
| stroke 17 | 50 % → 31 % | 454.1 px | 0.41 | 0.61 | 168 |
| stroke 18 | 50 % → 44 % | 342.5 px | 0.42 | 0.87 | 502 |
| stroke 19 | 48 % → 42 % | 401.0 px | 0.41 | 0.87 | 178 |
| stroke 20 | 17 % → 70 % | 372.6 px | 0.44 | 4.04 | 65 |
| stroke 21 | 1 % → 75 % | 26.5 px | 0.44 | 66.89 | 22 |
| stroke 22 | 10 % → 0 % | 67.8 px | 0.00 | 0.00 | 306 |
| stroke 23 | 6 % → 0 % | 110.4 px | 0.00 | 0.00 | 220 |
| stroke 24 | 20 % → 0 % | 92.7 px | 0.00 | 0.00 | 1073 |
| stroke 25 | 26 % → 0 % | 218.9 px | 0.00 | 0.00 | 248 |
| stroke 26 | 29 % → 0 % | 187.8 px | 0.00 | 0.00 | 518 |
| stroke 27 | 24 % → 0 % | 208.0 px | 0.00 | 0.00 | 145 |
| stroke 28 | 39 % → 0 % | 155.5 px | 0.00 | 0.00 | 1029 |
| stroke 29 | 40 % → 0 % | 922.7 px | 0.00 | 0.00 | 58 |
| stroke 30 | 50 % → 0 % | 846.5 px | 0.00 | 0.00 | 110 |
| stroke 31 | 34 % → 0 % | 569.3 px | 0.00 | 0.00 | 67 |
| stroke 32 | 38 % → 0 % | 357.0 px | 0.00 | 0.00 | 149 |
| stroke 33 | 40 % → 0 % | 438.5 px | 0.00 | 0.00 | 208 |
| stroke 34 | 7 % → 35 % | 81.1 px | 0.41 | 4.87 | 158 |
| stroke 35 | 9 % → 49 % | 168.0 px | 0.41 | 5.48 | 66 |
| stroke 36 | 11 % → 55 % | 280.3 px | 0.42 | 5.00 | 57 |
| stroke 37 | 3 % → 76 % | 76.2 px | 0.44 | 24.89 | 51 |
| stroke 38 | 1 % → 0 % | 24.4 px | 0.00 | 0.00 | 13 |
| stroke 39 | 1 % → 1 % | 24.2 px | 0.34 | 1.38 | 12 |
| stroke 40 | 8 % → 0 % | 39.7 px | 0.00 | 0.00 | 89 |
| stroke 41 | 11 % → 0 % | 60.2 px | 0.00 | 0.00 | 110 |
| stroke 42 | 4 % → 0 % | 41.1 px | 0.00 | 0.00 | 52 |
| stroke 43 | 5 % → 0 % | 182.9 px | 0.00 | 0.00 | 16 |
| stroke 44 | 8 % → 0 % | 57.4 px | 0.00 | 0.00 | 122 |
| stroke 45 | 9 % → 0 % | 135.8 px | 0.00 | 0.00 | 50 |
| stroke 46 | 2 % → 0 % | 41.3 px | 0.00 | 0.00 | 31 |
| stroke 47 | 12 % → 0 % | 66.5 px | 0.00 | 0.00 | 278 |
| stroke 48 | 20 % → 0 % | 107.8 px | 0.00 | 0.00 | 257 |
| stroke 49 | 4 % → 3 % | 40.3 px | 0.37 | 0.62 | 130 |
| stroke 50 | 7 % → 7 % | 55.9 px | 0.36 | 0.94 | 142 |
| stroke 51 | 10 % → 12 % | 94.4 px | 0.38 | 1.21 | 105 |
| stroke 52 | 13 % → 16 % | 166.6 px | 0.40 | 1.28 | 82 |
| stroke 53 | 5 % → 76 % | 40.1 px | 0.43 | 15.54 | 98 |
| stroke 54 | 7 % → 77 % | 69.1 px | 0.43 | 10.95 | 97 |
| stroke 55 | 10 % → 81 % | 137.1 px | 0.44 | 7.86 | 48 |
| stroke 56 | 13 % → 77 % | 426.1 px | 0.44 | 5.90 | 20 |
| stroke 57 | 5 % → 0 % | 46.5 px | 0.00 | 0.00 | 61 |
| stroke 58 | 7 % → 0 % | 75.9 px | 0.00 | 0.00 | 57 |
| stroke 59 | 2 % → 0 % | 50.0 px | 0.00 | 0.00 | 46 |
| stroke 60 | 4 % → 0 % | 95.7 px | 0.00 | 0.00 | 28 |
| stroke 61 | 5 % → 0 % | 100.2 px | 0.00 | 0.00 | 55 |
| stroke 62 | 7 % → 0 % | 76.9 px | 0.00 | 0.00 | 134 |
| stroke 63 | 10 % → 0 % | 202.8 px | 0.00 | 0.00 | 56 |
| stroke 64 | 5 % → 0 % | 64.4 px | 0.00 | 0.00 | 38 |
| stroke 65 | 9 % → 0 % | 63.3 px | 0.00 | 0.00 | 153 |
| stroke 66 | 12 % → 0 % | 78.8 px | 0.00 | 0.00 | 237 |
| stroke 67 | 13 % → 0 % | 220.5 px | 0.00 | 0.00 | 80 |
| stroke 68 | 5 % → 37 % | 47.2 px | 0.42 | 8.11 | 134 |
| stroke 69 | 5 % → 79 % | 45.8 px | 0.44 | 15.99 | 134 |
| stroke 70 | 8 % → 75 % | 107.6 px | 0.45 | 9.55 | 81 |
| stroke 71 | 5 % → 47 % | 80.5 px | 0.43 | 9.74 | 144 |
| stroke 72 | 10 % → 52 % | 106.0 px | 0.42 | 5.45 | 222 |
| stroke 73 | 5 % → 44 % | 90.7 px | 0.41 | 8.01 | 62 |
| stroke 74 | 18 % → 59 % | 121.8 px | 0.43 | 3.35 | 664 |
| stroke 75 | 24 % → 56 % | 164.9 px | 0.42 | 2.30 | 287 |
| stroke 76 | 32 % → 65 % | 118.4 px | 0.43 | 2.05 | 1114 |
| stroke 77 | 31 % → 70 % | 454.5 px | 0.44 | 2.24 | 85 |
| stroke 78 | 43 % → 76 % | 203.1 px | 0.43 | 1.77 | 763 |
| stroke 79 | 37 % → 75 % | 362.6 px | 0.45 | 2.05 | 194 |
| stroke 80 | 50 % → 82 % | 331.8 px | 0.44 | 1.62 | 548 |
| stroke 81 | 44 % → 75 % | 582.4 px | 0.42 | 1.70 | 93 |
| stroke 82 | 57 % → 79 % | 244.2 px | 0.44 | 1.38 | 715 |
| stroke 83 | 50 % → 76 % | 458.8 px | 0.43 | 1.52 | 134 |
| stroke 84 | 68 % → 79 % | 287.9 px | 0.45 | 1.16 | 404 |
| stroke 85 | 62 % → 73 % | 310.5 px | 0.44 | 1.17 | 297 |
| stroke 86 | 76 % → 76 % | 269.1 px | 0.45 | 1.00 | 427 |
| stroke 87 | 71 % → 71 % | 293.6 px | 0.44 | 1.00 | 376 |

Numbers say: wet paint spreads well beyond the stroke.

## Watercolour · #16 Shrigley strokes — own sheet
own sheet 600 × 600 · Watercolour 1.00 + water 30 % · 46 px · 18.1 s

![Watercolour · #16 Shrigley strokes — own sheet](Watercolour-16-Shrigley-strokes-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| s0 | 7 % → 22 % | 33.9 px | 0.33 | 2.98 | 78 |
| s1 | 6 % → 28 % | 11.8 px | 0.44 | 4.73 | 89 |
| s2 | 12 % → 18 % | 59.6 px | 0.24 | 1.52 | 108 |
| s3 | 10 % → 17 % | 31.2 px | 0.43 | 1.62 | 114 |
| s4 | 15 % → 25 % | 44.1 px | 0.40 | 1.70 | 120 |
| s5 | 20 % → 25 % | 46.7 px | 0.42 | 1.20 | 156 |
| s6 | 19 % → 20 % | 58.7 px | 0.35 | 1.05 | 159 |
| s7 | 26 % → 31 % | 40.4 px | 0.44 | 1.20 | 94 |
| s8 | 22 % → 22 % | 97.5 px | 0.32 | 1.01 | 129 |

Numbers say: wet paint spreads well beyond the stroke.

## Watercolour · #29 Shrigley asterisk — own sheet
own sheet 600 × 600 · Watercolour 1.00 + water 50 % · 70 px · 30.4 s

![Watercolour · #29 Shrigley asterisk — own sheet](Watercolour-29-Shrigley-asterisk-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 28 % → 62 % | 99.0 px | 0.61 | 2.21 | 455 |
| stroke 2 | 24 % → 24 % | 172.0 px | 0.60 | 1.00 | 759 |
| stroke 3 | 51 % → 61 % | 180.3 px | 0.60 | 1.21 | 979 |
| stroke 4 | 42 % → 41 % | 300.0 px | 0.60 | 0.97 | 973 |

Numbers say: wet paint spreads well beyond the stroke.

## Watercolour · #35 Red band with runs — own sheet
own sheet 600 × 600 · Watercolour 1.00 + water 75 % · 80 px · 22.7 s

![Watercolour · #35 Red band with runs — own sheet](Watercolour-35-Red-band-with-runs-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 37 % → 46 % | 146.8 px | 0.20 | 1.22 | 770 |

## Watercolour · #40 Olive and sepia blooms — own sheet
own sheet 600 × 600 · Watercolour 1.00 + water 55 % · 90 px · 30.2 s

![Watercolour · #40 Olive and sepia blooms — own sheet](Watercolour-40-Olive-and-sepia-blooms-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 27 % → 52 % | 95.7 px | 0.15 | 1.91 | 1739 |
| stroke 2 | 47 % → 55 % | 150.6 px | 0.16 | 1.16 | 1443 |

Numbers say: wet paint spreads well beyond the stroke.

## Watercolour · #46 Lips on wet paper — own sheet
own sheet 600 × 600 · Watercolour 1.00 + water 65 % · 50 px · 19.7 s

![Watercolour · #46 Lips on wet paper — own sheet](Watercolour-46-Lips-on-wet-paper-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 13 % → 27 % | 56.1 px | 0.53 | 2.00 | 146 |
| stroke 2 | 14 % → 24 % | 63.2 px | 0.51 | 1.70 | 177 |

Numbers say: wet paint spreads well beyond the stroke.



## Measures of the own sheets (v4 §9)

| sheet | fine lines (across ÷ along) | gaps | edge steps |
|---|---|---|---|
| Oil focus · A best filbert — own sheet | 2.09 | 0.8 % | 14.7 % |
| Oil focus · B flat — own sheet | 1.99 | 1.7 % | 13.1 % |
| Oil focus · C round — own sheet | 1.36 | 0.2 % | 12.5 % |
| Oil focus · D worn — own sheet | 1.65 | 6.9 % | 16.4 % |
| Oil focus · E swell — own sheet | 2.06 | 0.9 % | 13.7 % |
| Oil focus · F steady hand — own sheet | 2.12 | 0.8 % | 15.0 % |
| Oil focus · G soft hairs — own sheet | 1.98 | 1.5 % | 13.1 % |
| Oil focus · H narrow — own sheet | 2.04 | 0.9 % | 13.9 % |
| Refs v3 · #01 HW peach cloud — own sheet | 1.37 | 0.8 % | 32.1 % |
| Refs v3 · #02 HW cream strokes — own sheet | 1.66 | 23.1 % | 31.8 % |
| Refs v3 · #03 HW navy contours — own sheet | 1.59 | 4.5 % | 34.7 % |
| Refs v3 · #04 HW grey cloud — own sheet | 1.54 | 8.6 % | 33.7 % |
| Refs v3 · #05 HW green in rust loops — own sheet | 1.38 | 2.4 % | 30.9 % |
| Refs v3 · #06 HW scrubbed grey — own sheet | 1.55 | 8.5 % | 32.6 % |
| Refs v3 · #07 HW blue L and zigzag — own sheet | 1.50 | 6.4 % | 32.7 % |
| Refs v3 · #08 HW lilac crown basket — own sheet | 1.42 | 15.5 % | 37.7 % |
| Refs v3 · #09 HW white loops — own sheet | 1.74 | 10.6 % | 30.6 % |
| Refs v3 · #10 HW maroon loops — own sheet | 1.40 | 2.1 % | 30.1 % |
| Refs v3 · #11 HW purple balls — own sheet | 1.48 | 43.2 % | 38.9 % |
| Refs v3 · #12 HW black-olive cage — own sheet | 1.46 | 15.7 % | 37.3 % |
| Refs v3 · #13 HW blue streaky form — own sheet | 1.35 | 3.0 % | 29.1 % |
| Refs v3 · #14 HW olive totem — own sheet | 1.38 | 8.9 % | 38.0 % |
| Refs v3 · #15 Ultramarine script — own sheet | 1.17 | 3.2 % | 42.2 % |
| Refs v3 · #16 Shrigley strokes — own sheet | 1.05 | 9.3 % | 49.3 % |
| Refs v3 · #17 Krovostok dry brush — own sheet | 1.33 | 0.6 % | 40.0 % |
| Refs v3 · #18 Twombly blue sticks — own sheet | 1.15 | 2.7 % | 20.0 % |
| Refs v3 · #19 Guston charcoal hand — own sheet | 1.02 | 1.3 % | 25.4 % |
| Refs v3 · #20 Orange crayon — own sheet | 0.96 | 0.4 % | 15.8 % |
| Refs v3 · #21 Gritty dog contours — own sheet | 1.34 | 47.5 % | 53.8 % |
| Refs v3 · #22 Wasilewski brush poster — own sheet | 1.26 | 6.5 % | 37.6 % |
| Refs v3 · #23 Report dry white mask — own sheet | 1.60 | 1.7 % | 45.7 % |
| Refs v3 · #24 Picasso flat oil — own sheet | 1.37 | 32.3 % | 37.4 % |
| Refs v3 · #25 Yellow heavy stroke — own sheet | 1.30 | 1.2 % | 14.7 % |
| Refs v3 · #26 Ink caricature — own sheet | 1.58 | 1.3 % | 40.9 % |
| Refs v3 · #27 Orange impasto swatch — own sheet | 1.68 | 0.2 % | 35.0 % |
| Refs v3 · #28 Miles Davis lines — own sheet | 1.26 | 2.1 % | 38.5 % |
| Refs v3 · #29 Shrigley asterisk — own sheet | 1.10 | 0.0 % | 37.8 % |
| Refs v3 · #30 Red gouache face — own sheet | 1.35 | 0.5 % | 41.5 % |
| Refs v3 · #31 Warhol blotted line — own sheet | 1.16 | 4.2 % | 39.0 % |
| Refs v3 · #32 Thick orange swipes — own sheet | 2.14 | 0.1 % | 18.1 % |
| Refs v3 · #33 Red wet-in-wet flames — own sheet | 1.46 | 6.7 % | 52.6 % |
| Refs v3 · #34 Magenta oil patches — own sheet | 1.49 | 14.6 % | 35.0 % |
| Refs v3 · #35 Red band with runs — own sheet | 0.98 | 0.0 % | 32.8 % |
| Refs v3 · #36 Magenta letters flat — own sheet | 1.26 | 3.0 % | 36.2 % |
| Refs v3 · #37 Oil still life — own sheet | 1.37 | 39.6 % | 38.7 % |
| Refs v3 · #38 Sanguine drawing — own sheet | 1.20 | 4.3 % | 32.7 % |
| Refs v3 · #39 Thick impasto weave — own sheet | 1.75 | 0.4 % | 29.2 % |
| Refs v3 · #40 Watercolour blooms — own sheet | 1.06 | 24.4 % | 74.4 % |
| Refs v3 · #41 Coloured pencil — own sheet | 1.22 | 20.4 % | 32.5 % |
| Refs v3 · #42 Pink shaggy pastel — own sheet | 1.09 | 0.4 % | 13.8 % |
| Refs v3 · #43 Dragged black blocks — own sheet | 1.58 | 0.0 % | 56.2 % |
| Refs v3 · #44 Blue looping ribbon — own sheet | 1.48 | 0.1 % | 47.8 % |
| Refs v3 · #45 Pastel pepper — own sheet | 1.24 | 0.1 % | 27.1 % |
| Refs v3 · #46 Ink lips on wet paper — own sheet | 1.35 | 0.0 % | 37.8 % |
| Refs v3 · #47 Pink knife slabs — own sheet | 0.69 | 58.4 % | 36.5 % |
| Refs v3 · #48 Black bands with drips — own sheet | 1.30 | 0.2 % | 30.7 % |
| Refs v3 · #49 Magenta letters round — own sheet | 1.51 | 0.1 % | 35.2 % |
| Refs v3 · #50 Swipes on seaside — own sheet | 2.19 | 4.3 % | 19.2 % |
| Watercolour · #16 Shrigley strokes — own sheet | 1.08 | 5.9 % | 40.4 % |
| Watercolour · #29 Shrigley asterisk — own sheet | 1.14 | 0.3 % | 34.2 % |
| Watercolour · #35 Red band with runs — own sheet | 1.38 | 1.6 % | 39.7 % |
| Watercolour · #40 Olive and sepia blooms — own sheet | 1.05 | 6.1 % | 44.0 % |
| Watercolour · #46 Lips on wet paper — own sheet | 1.58 | 0.0 % | 41.7 % |
