![All brushes](contact.png)

# Brush Lab — 100 brushes · 9 Nov 2026 at 06:21

Every sheet: 1500 × 600, ten strokes in a 5 × 2 grid — 1. light line · 2. heavy line · 3. pressure swell · 4. fast wave · 5. slow wave · 6. spiral · 7. loop · 8. tilted · 9. over the wet one · 10. long, no reload (cell 8 holds «tilted» and «over the wet one» crossed). The CPU reference of Mamay's paint engine; the wet layer settles 20 s at the end.

Columns: **covered** = share of the cell with paint right after the stroke → after settling; **width** = painted area of the stroke ÷ its length (px); **dark** = mean darkness of the painted pixels above the paper's own grain (0 = paper, 1 = black); **spread** = how far wet paint went beyond the stroke (1.0 = stayed); **ms** = the stroke on the CPU; long stroke: paint in each quarter of its length (it should run out: wet → streaks → dry tail).

## Refs v3 · #01 HW peach cloud
Gouache 1.00 + turpentine 30 % · 74 px · 53.5 s

![Refs v3 · #01 HW peach cloud](Refs-v3-01-HW-peach-cloud.png)

A light paint: laid on a grey sheet (on white it cannot be seen); **dark** = how far it is from the grey either way.

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 23 % → 21 % | 66.6 px | 0.33 | 0.93 | 290 |
| heavy line | 23 % → 21 % | 67.9 px | 0.31 | 0.91 | 369 |
| pressure swell | 18 % → 17 % | 66.9 px | 0.32 | 0.97 | 209 |
| fast wave | 55 % → 23 % | 63.6 px | 0.26 | 0.42 | 970 |
| slow wave | 52 % → 26 % | 60.6 px | 0.31 | 0.49 | 1601 |
| spiral | 69 % → 29 % | 45.4 px | 0.27 | 0.42 | 2286 |
| loop | 47 % → 28 % | 60.3 px | 0.30 | 0.60 | 660 |
| tilted | 19 % → 19 % | 52.7 px | 0.28 | 1.00 | 449 |
| over the wet one | 40 % → 34 % | 57.7 px | 0.28 | 0.87 | 312 |
| long, no reload | 88 % → 26 % | 39.7 px | 0.29 | 0.29 | 2883 | quarters: 0.00 → 0.00 → 0.00 → 0.00

Numbers say: light vs heavy: width 66.6 → 67.9 px, dark 0.33 → 0.31; pressure barely changes the width; the long stroke does not run out of paint.

## Refs v3 · #02 HW cream strokes
Gouache 1.00 + turpentine 30 % · 36 px · 43.9 s

![Refs v3 · #02 HW cream strokes](Refs-v3-02-HW-cream-strokes.png)

A light paint: laid on a grey sheet (on white it cannot be seen); **dark** = how far it is from the grey either way.

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 12 % → 11 % | 34.0 px | 0.37 | 0.98 | 139 |
| heavy line | 12 % → 12 % | 36.1 px | 0.37 | 0.97 | 232 |
| pressure swell | 9 % → 9 % | 35.0 px | 0.36 | 1.00 | 130 |
| fast wave | 31 % → 12 % | 35.7 px | 0.31 | 0.38 | 410 |
| slow wave | 29 % → 13 % | 34.1 px | 0.34 | 0.45 | 775 |
| spiral | 47 % → 14 % | 31.0 px | 0.33 | 0.30 | 747 |
| loop | 26 % → 12 % | 33.2 px | 0.35 | 0.47 | 572 |
| tilted | 12 % → 12 % | 33.5 px | 0.32 | 1.00 | 511 |
| over the wet one | 23 % → 21 % | 31.1 px | 0.32 | 0.89 | 216 |
| long, no reload | 55 % → 13 % | 24.5 px | 0.33 | 0.24 | 860 | quarters: 0.01 → 0.01 → 0.01 → 0.01

Numbers say: light vs heavy: width 34.0 → 36.1 px, dark 0.37 → 0.37; pressure barely changes the width; the long stroke does not run out of paint.

## Refs v3 · #03 HW navy contours
Gouache 1.00 + turpentine 30 % · 58 px · 49.0 s

![Refs v3 · #03 HW navy contours](Refs-v3-03-HW-navy-contours.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 18 % → 17 % | 51.5 px | 0.28 | 0.95 | 220 |
| heavy line | 18 % → 17 % | 53.7 px | 0.30 | 0.93 | 388 |
| pressure swell | 14 % → 13 % | 53.7 px | 0.33 | 0.94 | 207 |
| fast wave | 45 % → 18 % | 51.8 px | 0.34 | 0.40 | 703 |
| slow wave | 43 % → 19 % | 50.0 px | 0.32 | 0.43 | 1202 |
| spiral | 62 % → 23 % | 40.8 px | 0.35 | 0.38 | 1486 |
| loop | 38 % → 21 % | 49.3 px | 0.31 | 0.55 | 907 |
| tilted | 16 % → 16 % | 43.4 px | 0.33 | 1.00 | 302 |
| over the wet one | 32 % → 28 % | 46.5 px | 0.33 | 0.88 | 260 |
| long, no reload | 78 % → 20 % | 34.8 px | 0.32 | 0.25 | 1386 | quarters: 0.27 → 0.15 → 0.04 → 0.01

Numbers say: light vs heavy: width 51.5 → 53.7 px, dark 0.28 → 0.30; pressure barely changes the width.

## Refs v3 · #04 HW grey cloud
Gouache 1.00 + turpentine 30 % · 66 px · 51.4 s

![Refs v3 · #04 HW grey cloud](Refs-v3-04-HW-grey-cloud.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 20 % → 20 % | 59.2 px | 0.14 | 0.97 | 259 |
| heavy line | 21 % → 20 % | 61.0 px | 0.14 | 0.94 | 344 |
| pressure swell | 16 % → 16 % | 59.0 px | 0.17 | 0.99 | 232 |
| fast wave | 49 % → 21 % | 57.1 px | 0.23 | 0.43 | 901 |
| slow wave | 50 % → 24 % | 57.8 px | 0.18 | 0.47 | 1350 |
| spiral | 66 % → 27 % | 43.5 px | 0.20 | 0.41 | 1975 |
| loop | 43 % → 23 % | 55.3 px | 0.14 | 0.54 | 642 |
| tilted | 17 % → 17 % | 48.3 px | 0.17 | 1.00 | 370 |
| over the wet one | 36 % → 31 % | 52.4 px | 0.17 | 0.86 | 322 |
| long, no reload | 84 % → 25 % | 37.5 px | 0.16 | 0.30 | 2282 | quarters: 0.14 → 0.08 → 0.02 → 0.00

Numbers say: light vs heavy: width 59.2 → 61.0 px, dark 0.14 → 0.14; pressure barely changes the width.

## Refs v3 · #05 HW green in rust loops
Gouache 1.00 + turpentine 30 % · 74 px · 54.0 s

![Refs v3 · #05 HW green in rust loops](Refs-v3-05-HW-green-in-rust-loops.png)

A light paint: laid on a grey sheet (on white it cannot be seen); **dark** = how far it is from the grey either way.

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 23 % → 21 % | 66.6 px | 0.38 | 0.93 | 302 |
| heavy line | 23 % → 21 % | 67.9 px | 0.38 | 0.91 | 331 |
| pressure swell | 18 % → 17 % | 66.9 px | 0.38 | 0.97 | 243 |
| fast wave | 55 % → 23 % | 63.6 px | 0.32 | 0.42 | 965 |
| slow wave | 52 % → 26 % | 60.6 px | 0.36 | 0.49 | 1820 |
| spiral | 69 % → 29 % | 45.4 px | 0.34 | 0.42 | 2327 |
| loop | 47 % → 28 % | 60.3 px | 0.36 | 0.60 | 687 |
| tilted | 19 % → 19 % | 52.7 px | 0.34 | 1.00 | 436 |
| over the wet one | 40 % → 34 % | 57.7 px | 0.34 | 0.87 | 337 |
| long, no reload | 88 % → 26 % | 39.7 px | 0.35 | 0.29 | 2969 | quarters: 0.00 → 0.00 → 0.00 → 0.00

Numbers say: light vs heavy: width 66.6 → 67.9 px, dark 0.38 → 0.38; pressure barely changes the width; the long stroke does not run out of paint.

## Refs v3 · #06 HW scrubbed grey
Gouache 1.00 + turpentine 30 % · 66 px · 51.5 s

![Refs v3 · #06 HW scrubbed grey](Refs-v3-06-HW-scrubbed-grey.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 20 % → 20 % | 59.2 px | 0.14 | 0.97 | 249 |
| heavy line | 21 % → 20 % | 61.0 px | 0.14 | 0.94 | 325 |
| pressure swell | 16 % → 16 % | 59.0 px | 0.17 | 0.99 | 216 |
| fast wave | 49 % → 21 % | 57.1 px | 0.23 | 0.43 | 867 |
| slow wave | 50 % → 24 % | 57.8 px | 0.18 | 0.47 | 1294 |
| spiral | 66 % → 27 % | 43.5 px | 0.20 | 0.41 | 1707 |
| loop | 43 % → 23 % | 55.3 px | 0.14 | 0.54 | 604 |
| tilted | 17 % → 17 % | 48.3 px | 0.17 | 1.00 | 345 |
| over the wet one | 36 % → 31 % | 52.4 px | 0.17 | 0.86 | 326 |
| long, no reload | 84 % → 25 % | 37.5 px | 0.16 | 0.30 | 2153 | quarters: 0.14 → 0.08 → 0.02 → 0.00

Numbers say: light vs heavy: width 59.2 → 61.0 px, dark 0.14 → 0.14; pressure barely changes the width.

## Refs v3 · #07 HW blue L and zigzag
Gouache 1.00 + turpentine 30 % · 74 px · 53.8 s

![Refs v3 · #07 HW blue L and zigzag](Refs-v3-07-HW-blue-L-and-zigzag.png)

A light paint: laid on a grey sheet (on white it cannot be seen); **dark** = how far it is from the grey either way.

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 23 % → 21 % | 66.6 px | 0.41 | 0.93 | 309 |
| heavy line | 23 % → 21 % | 67.9 px | 0.41 | 0.91 | 373 |
| pressure swell | 18 % → 17 % | 66.9 px | 0.40 | 0.97 | 231 |
| fast wave | 55 % → 23 % | 63.6 px | 0.36 | 0.42 | 1015 |
| slow wave | 52 % → 26 % | 60.6 px | 0.40 | 0.49 | 1749 |
| spiral | 69 % → 29 % | 45.4 px | 0.37 | 0.42 | 2264 |
| loop | 47 % → 28 % | 60.3 px | 0.38 | 0.60 | 677 |
| tilted | 19 % → 19 % | 52.7 px | 0.38 | 1.00 | 477 |
| over the wet one | 40 % → 34 % | 57.7 px | 0.38 | 0.87 | 328 |
| long, no reload | 88 % → 26 % | 39.7 px | 0.38 | 0.29 | 2799 | quarters: 0.00 → 0.00 → 0.00 → 0.01

Numbers say: light vs heavy: width 66.6 → 67.9 px, dark 0.41 → 0.41; pressure barely changes the width; the long stroke does not run out of paint.

## Refs v3 · #08 HW lilac crown basket
Gouache 1.00 + turpentine 30 % · 26 px · 39.6 s

![Refs v3 · #08 HW lilac crown basket](Refs-v3-08-HW-lilac-crown-basket.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 8 % → 9 % | 24.3 px | 0.13 | 1.02 | 111 |
| heavy line | 9 % → 8 % | 25.2 px | 0.14 | 0.96 | 180 |
| pressure swell | 7 % → 7 % | 26.3 px | 0.17 | 1.06 | 82 |
| fast wave | 21 % → 7 % | 24.3 px | 0.20 | 0.36 | 265 |
| slow wave | 21 % → 10 % | 24.6 px | 0.16 | 0.48 | 560 |
| spiral | 33 % → 8 % | 21.6 px | 0.18 | 0.25 | 473 |
| loop | 19 % → 9 % | 25.0 px | 0.16 | 0.45 | 413 |
| tilted | 9 % → 10 % | 26.5 px | 0.20 | 1.02 | 213 |
| over the wet one | 18 % → 16 % | 24.9 px | 0.20 | 0.89 | 220 |
| long, no reload | 38 % → 9 % | 17.2 px | 0.19 | 0.24 | 644 | quarters: 0.10 → 0.02 → 0.00 → 0.00

Numbers say: light vs heavy: width 24.3 → 25.2 px, dark 0.13 → 0.14; pressure barely changes the width.

## Refs v3 · #09 HW white loops
Gouache 1.00 + turpentine 30 % · 74 px · 53.7 s

![Refs v3 · #09 HW white loops](Refs-v3-09-HW-white-loops.png)

A light paint: laid on a grey sheet (on white it cannot be seen); **dark** = how far it is from the grey either way.

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 23 % → 21 % | 66.6 px | 0.40 | 0.93 | 281 |
| heavy line | 23 % → 21 % | 67.9 px | 0.40 | 0.91 | 395 |
| pressure swell | 18 % → 17 % | 66.9 px | 0.39 | 0.97 | 265 |
| fast wave | 55 % → 23 % | 63.6 px | 0.35 | 0.42 | 980 |
| slow wave | 52 % → 26 % | 60.6 px | 0.39 | 0.49 | 1723 |
| spiral | 69 % → 29 % | 45.4 px | 0.36 | 0.42 | 2231 |
| loop | 47 % → 28 % | 60.3 px | 0.38 | 0.60 | 698 |
| tilted | 19 % → 19 % | 52.7 px | 0.36 | 1.00 | 443 |
| over the wet one | 40 % → 34 % | 57.7 px | 0.36 | 0.87 | 333 |
| long, no reload | 88 % → 26 % | 39.7 px | 0.37 | 0.29 | 2889 | quarters: 0.00 → 0.00 → 0.00 → 0.01

Numbers say: light vs heavy: width 66.6 → 67.9 px, dark 0.40 → 0.40; pressure barely changes the width; the long stroke does not run out of paint.

## Refs v3 · #10 HW maroon loops
Gouache 1.00 + turpentine 30 % · 74 px · 54.0 s

![Refs v3 · #10 HW maroon loops](Refs-v3-10-HW-maroon-loops.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 23 % → 21 % | 66.6 px | 0.26 | 0.93 | 292 |
| heavy line | 23 % → 21 % | 67.9 px | 0.28 | 0.91 | 393 |
| pressure swell | 18 % → 17 % | 66.9 px | 0.27 | 0.97 | 236 |
| fast wave | 55 % → 23 % | 63.6 px | 0.33 | 0.42 | 971 |
| slow wave | 52 % → 26 % | 60.6 px | 0.28 | 0.49 | 1903 |
| spiral | 69 % → 29 % | 45.4 px | 0.31 | 0.42 | 2333 |
| loop | 47 % → 28 % | 60.3 px | 0.27 | 0.60 | 696 |
| tilted | 19 % → 19 % | 52.7 px | 0.30 | 1.00 | 426 |
| over the wet one | 40 % → 34 % | 57.7 px | 0.30 | 0.87 | 320 |
| long, no reload | 88 % → 26 % | 39.7 px | 0.28 | 0.29 | 2964 | quarters: 0.26 → 0.17 → 0.06 → 0.01

Numbers say: light vs heavy: width 66.6 → 67.9 px, dark 0.26 → 0.28; pressure barely changes the width.

## Refs v3 · #11 HW purple balls
Gouache 1.00 + turpentine 30 % · 74 px · 45.0 s

![Refs v3 · #11 HW purple balls](Refs-v3-11-HW-purple-balls.png)

A light paint: laid on a grey sheet (on white it cannot be seen); **dark** = how far it is from the grey either way.

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 23 % → 21 % | 66.6 px | 0.32 | 0.93 | 258 |
| heavy line | 23 % → 21 % | 67.9 px | 0.31 | 0.91 | 318 |
| pressure swell | 18 % → 17 % | 66.9 px | 0.32 | 0.97 | 219 |
| fast wave | 55 % → 23 % | 63.6 px | 0.25 | 0.42 | 895 |
| slow wave | 52 % → 26 % | 60.6 px | 0.30 | 0.49 | 1236 |
| spiral | 69 % → 29 % | 45.4 px | 0.27 | 0.42 | 1315 |
| loop | 47 % → 28 % | 60.3 px | 0.30 | 0.60 | 714 |
| tilted | 19 % → 19 % | 52.7 px | 0.28 | 1.00 | 435 |
| over the wet one | 40 % → 34 % | 57.7 px | 0.28 | 0.87 | 331 |
| long, no reload | 88 % → 26 % | 39.7 px | 0.29 | 0.29 | 1796 | quarters: 0.00 → 0.00 → 0.00 → 0.00

Numbers say: light vs heavy: width 66.6 → 67.9 px, dark 0.32 → 0.31; pressure barely changes the width; the long stroke does not run out of paint.

## Refs v3 · #12 HW black-olive cage
Gouache 1.00 + turpentine 30 % · 26 px · 30.6 s

![Refs v3 · #12 HW black-olive cage](Refs-v3-12-HW-black-olive-cage.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 8 % → 9 % | 24.3 px | 0.13 | 1.02 | 88 |
| heavy line | 9 % → 8 % | 25.2 px | 0.14 | 0.96 | 105 |
| pressure swell | 7 % → 7 % | 26.3 px | 0.17 | 1.06 | 79 |
| fast wave | 21 % → 7 % | 24.3 px | 0.20 | 0.36 | 263 |
| slow wave | 21 % → 10 % | 24.6 px | 0.16 | 0.48 | 422 |
| spiral | 33 % → 8 % | 21.6 px | 0.18 | 0.25 | 441 |
| loop | 19 % → 9 % | 25.0 px | 0.16 | 0.45 | 219 |
| tilted | 9 % → 10 % | 26.5 px | 0.20 | 1.02 | 124 |
| over the wet one | 18 % → 16 % | 24.9 px | 0.20 | 0.89 | 111 |
| long, no reload | 38 % → 9 % | 17.2 px | 0.19 | 0.24 | 596 | quarters: 0.10 → 0.02 → 0.00 → 0.00

Numbers say: light vs heavy: width 24.3 → 25.2 px, dark 0.13 → 0.14; pressure barely changes the width.

## Refs v3 · #13 HW blue streaky form
Gouache 1.00 + turpentine 30 % · 74 px · 46.5 s

![Refs v3 · #13 HW blue streaky form](Refs-v3-13-HW-blue-streaky-form.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 23 % → 21 % | 66.6 px | 0.16 | 0.93 | 287 |
| heavy line | 23 % → 21 % | 67.9 px | 0.17 | 0.91 | 298 |
| pressure swell | 18 % → 17 % | 66.9 px | 0.17 | 0.97 | 224 |
| fast wave | 55 % → 23 % | 63.6 px | 0.23 | 0.42 | 788 |
| slow wave | 52 % → 26 % | 60.6 px | 0.18 | 0.49 | 1259 |
| spiral | 69 % → 29 % | 45.4 px | 0.21 | 0.42 | 1345 |
| loop | 47 % → 28 % | 60.3 px | 0.17 | 0.60 | 733 |
| tilted | 19 % → 19 % | 52.7 px | 0.20 | 1.00 | 461 |
| over the wet one | 40 % → 34 % | 57.7 px | 0.20 | 0.87 | 325 |
| long, no reload | 88 % → 26 % | 39.7 px | 0.18 | 0.29 | 1933 | quarters: 0.17 → 0.10 → 0.03 → 0.00

Numbers say: light vs heavy: width 66.6 → 67.9 px, dark 0.16 → 0.17; pressure barely changes the width.

## Refs v3 · #14 HW olive totem
Gouache 1.00 + turpentine 30 % · 41 px · 35.8 s

![Refs v3 · #14 HW olive totem](Refs-v3-14-HW-olive-totem.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 13 % → 12 % | 37.6 px | 0.31 | 0.92 | 133 |
| heavy line | 13 % → 13 % | 38.8 px | 0.32 | 0.96 | 148 |
| pressure swell | 10 % → 10 % | 39.1 px | 0.35 | 0.97 | 114 |
| fast wave | 32 % → 13 % | 36.9 px | 0.37 | 0.40 | 354 |
| slow wave | 33 % → 16 % | 37.7 px | 0.34 | 0.48 | 633 |
| spiral | 56 % → 16 % | 36.8 px | 0.34 | 0.29 | 601 |
| loop | 28 % → 14 % | 35.8 px | 0.32 | 0.49 | 336 |
| tilted | 12 % → 12 % | 34.3 px | 0.35 | 1.00 | 205 |
| over the wet one | 25 % → 21 % | 34.9 px | 0.35 | 0.86 | 156 |
| long, no reload | 59 % → 16 % | 26.4 px | 0.33 | 0.28 | 912 | quarters: 0.24 → 0.12 → 0.03 → 0.00

Numbers say: light vs heavy: width 37.6 → 38.8 px, dark 0.31 → 0.32; pressure barely changes the width.

## Refs v3 · #15 Ultramarine script
Ink 0.98 · 39 px · 32.0 s

![Refs v3 · #15 Ultramarine script](Refs-v3-15-Ultramarine-script.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 4 % → 7 % | 10.6 px | 0.60 | 2.03 | 46 |
| heavy line | 14 % → 15 % | 40.2 px | 0.68 | 1.11 | 160 |
| pressure swell | 8 % → 9 % | 28.6 px | 0.68 | 1.23 | 85 |
| fast wave | 28 % → 31 % | 31.8 px | 0.69 | 1.13 | 301 |
| slow wave | 23 % → 28 % | 26.9 px | 0.67 | 1.20 | 361 |
| spiral | 39 % → 45 % | 25.8 px | 0.66 | 1.15 | 357 |
| loop | 21 % → 25 % | 27.0 px | 0.66 | 1.19 | 203 |
| tilted | 14 % → 14 % | 39.2 px | 0.70 | 1.00 | 127 |
| over the wet one | 24 % → 26 % | 27.2 px | 0.70 | 1.09 | 118 |
| long, no reload | 54 % → 59 % | 24.3 px | 0.66 | 1.09 | 699 | quarters: 0.47 → 0.45 → 0.42 → 0.37

Numbers say: light vs heavy: width 10.6 → 40.2 px, dark 0.60 → 0.68; wet paint spreads well beyond the stroke.

## Refs v3 · #16 Shrigley strokes
Watercolour 1.00 + water 30 % · 64 px · 33.4 s

![Refs v3 · #16 Shrigley strokes](Refs-v3-16-Shrigley-strokes.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 8 % → 17 % | 24.6 px | 0.29 | 1.98 | 75 |
| heavy line | 17 % → 22 % | 49.0 px | 0.29 | 1.28 | 172 |
| pressure swell | 10 % → 15 % | 38.6 px | 0.34 | 1.45 | 122 |
| fast wave | 36 % → 43 % | 42.1 px | 0.32 | 1.17 | 401 |
| slow wave | 33 % → 40 % | 38.5 px | 0.28 | 1.21 | 567 |
| spiral | 57 % → 60 % | 37.9 px | 0.21 | 1.04 | 621 |
| loop | 29 % → 35 % | 37.6 px | 0.28 | 1.19 | 313 |
| tilted | 19 % → 19 % | 52.1 px | 0.30 | 1.00 | 229 |
| over the wet one | 31 % → 36 % | 35.0 px | 0.30 | 1.15 | 178 |
| long, no reload | 71 % → 75 % | 31.9 px | 0.20 | 1.06 | 995 | quarters: 0.26 → 0.17 → 0.13 → 0.09

Numbers say: light vs heavy: width 24.6 → 49.0 px, dark 0.29 → 0.29; wet paint spreads well beyond the stroke.

## Refs v3 · #17 Krovostok dry brush
Ink 0.93 · Gouache 0.07 · 38 px · 46.2 s

![Refs v3 · #17 Krovostok dry brush](Refs-v3-17-Krovostok-dry-brush.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 12 % → 14 % | 34.7 px | 0.75 | 1.13 | 92 |
| heavy line | 13 % → 15 % | 38.6 px | 0.74 | 1.15 | 158 |
| pressure swell | 10 % → 11 % | 35.9 px | 0.75 | 1.18 | 107 |
| fast wave | 32 % → 35 % | 37.3 px | 0.75 | 1.09 | 336 |
| slow wave | 28 % → 32 % | 32.8 px | 0.74 | 1.13 | 520 |
| spiral | 52 % → 54 % | 34.1 px | 0.76 | 1.05 | 566 |
| loop | 27 % → 30 % | 35.1 px | 0.75 | 1.10 | 319 |
| tilted | 13 % → 13 % | 35.6 px | 0.76 | 1.00 | 164 |
| over the wet one | 25 % → 28 % | 33.7 px | 0.76 | 1.14 | 136 |
| long, no reload | 56 % → 60 % | 24.9 px | 0.74 | 1.08 | 839 | quarters: 0.58 → 0.55 → 0.49 → 0.34

Numbers say: light vs heavy: width 34.7 → 38.6 px, dark 0.75 → 0.74.

## Refs v3 · #18 Twombly blue sticks
Wax 1.00 · 20 px · 9.5 s

![Refs v3 · #18 Twombly blue sticks](Refs-v3-18-Twombly-blue-sticks.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 4 % → 4 % | 12.1 px | 0.23 | 1.00 | 30 |
| heavy line | 6 % → 6 % | 17.1 px | 0.25 | 1.00 | 37 |
| pressure swell | 4 % → 4 % | 16.1 px | 0.23 | 1.00 | 22 |
| fast wave | 14 % → 14 % | 16.7 px | 0.24 | 1.00 | 88 |
| slow wave | 14 % → 14 % | 15.9 px | 0.25 | 1.00 | 124 |
| spiral | 23 % → 23 % | 14.9 px | 0.24 | 1.00 | 139 |
| loop | 11 % → 11 % | 14.1 px | 0.24 | 1.00 | 71 |
| tilted | 4 % → 4 % | 12.6 px | 0.23 | 1.00 | 45 |
| over the wet one | 10 % → 10 % | 15.6 px | 0.23 | 1.00 | 36 |
| long, no reload | 28 % → 28 % | 12.6 px | 0.24 | 1.00 | 203 | quarters: 0.08 → 0.08 → 0.08 → 0.08

Numbers say: light vs heavy: width 12.1 → 17.1 px, dark 0.23 → 0.25; the long stroke does not run out of paint.

## Refs v3 · #19 Guston charcoal hand
Charcoal 1.00 · 64 px · 14.3 s

![Refs v3 · #19 Guston charcoal hand](Refs-v3-19-Guston-charcoal-hand.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 10 % → 10 % | 29.5 px | 0.62 | 1.00 | 301 |
| heavy line | 19 % → 19 % | 54.6 px | 0.61 | 1.00 | 214 |
| pressure swell | 13 % → 13 % | 48.8 px | 0.62 | 1.00 | 145 |
| fast wave | 41 % → 41 % | 46.9 px | 0.62 | 1.00 | 526 |
| slow wave | 38 % → 38 % | 43.9 px | 0.62 | 1.00 | 906 |
| spiral | 59 % → 59 % | 39.2 px | 0.62 | 1.00 | 781 |
| loop | 30 % → 30 % | 39.5 px | 0.62 | 1.00 | 439 |
| tilted | 10 % → 10 % | 27.7 px | 0.61 | 1.00 | 293 |
| over the wet one | 25 % → 25 % | 43.0 px | 0.61 | 1.00 | 274 |
| long, no reload | 70 % → 70 % | 31.2 px | 0.62 | 1.00 | 1460 | quarters: 0.47 → 0.46 → 0.46 → 0.46

Numbers say: light vs heavy: width 29.5 → 54.6 px, dark 0.62 → 0.61; the long stroke does not run out of paint.

## Refs v3 · #20 Orange crayon
Wax 1.00 · 34 px · 10.6 s

![Refs v3 · #20 Orange crayon](Refs-v3-20-Orange-crayon.png)

A light paint: laid on a grey sheet (on white it cannot be seen); **dark** = how far it is from the grey either way.

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 6 % → 6 % | 18.6 px | 0.47 | 1.00 | 68 |
| heavy line | 10 % → 10 % | 28.8 px | 0.48 | 1.00 | 80 |
| pressure swell | 7 % → 7 % | 27.0 px | 0.48 | 1.00 | 50 |
| fast wave | 23 % → 23 % | 26.9 px | 0.49 | 1.00 | 191 |
| slow wave | 22 % → 22 % | 25.4 px | 0.49 | 1.00 | 311 |
| spiral | 35 % → 35 % | 23.4 px | 0.49 | 1.00 | 306 |
| loop | 18 % → 18 % | 23.0 px | 0.48 | 1.00 | 157 |
| tilted | 6 % → 6 % | 16.7 px | 0.47 | 1.00 | 107 |
| over the wet one | 15 % → 15 % | 24.5 px | 0.47 | 1.00 | 74 |
| long, no reload | 43 % → 43 % | 19.3 px | 0.49 | 1.00 | 453 | quarters: 0.00 → 0.00 → 0.00 → 0.00

Numbers say: light vs heavy: width 18.6 → 28.8 px, dark 0.47 → 0.48; the long stroke does not run out of paint.

## Refs v3 · #21 Gritty dog contours
Gouache 1.00 + water 15 % · 56 px · 44.6 s

![Refs v3 · #21 Gritty dog contours](Refs-v3-21-Gritty-dog-contours.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 17 % → 17 % | 50.1 px | 0.38 | 0.99 | 161 |
| heavy line | 17 % → 17 % | 50.8 px | 0.38 | 0.98 | 214 |
| pressure swell | 14 % → 14 % | 52.0 px | 0.39 | 1.00 | 154 |
| fast wave | 40 % → 29 % | 46.1 px | 0.39 | 0.73 | 569 |
| slow wave | 37 % → 31 % | 43.2 px | 0.37 | 0.82 | 849 |
| spiral | 55 % → 33 % | 36.3 px | 0.37 | 0.59 | 900 |
| loop | 35 % → 31 % | 45.1 px | 0.37 | 0.89 | 461 |
| tilted | 15 % → 15 % | 41.1 px | 0.38 | 1.01 | 252 |
| over the wet one | 31 % → 30 % | 46.2 px | 0.38 | 0.97 | 254 |
| long, no reload | 62 % → 36 % | 27.9 px | 0.35 | 0.58 | 1309 | quarters: 0.30 → 0.26 → 0.21 → 0.16

Numbers say: light vs heavy: width 50.1 → 50.8 px, dark 0.38 → 0.38; pressure barely changes the width.

## Refs v3 · #22 Wasilewski brush poster
Ink 0.98 · 64 px · 44.2 s

![Refs v3 · #22 Wasilewski brush poster](Refs-v3-22-Wasilewski-brush-poster.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 19 % → 21 % | 55.5 px | 0.88 | 1.08 | 99 |
| heavy line | 22 % → 23 % | 64.9 px | 0.89 | 1.01 | 288 |
| pressure swell | 16 % → 17 % | 58.6 px | 0.88 | 1.09 | 191 |
| fast wave | 51 % → 53 % | 59.3 px | 0.84 | 1.03 | 579 |
| slow wave | 48 % → 50 % | 55.3 px | 0.87 | 1.04 | 828 |
| spiral | 68 % → 68 % | 44.5 px | 0.85 | 1.01 | 889 |
| loop | 43 % → 44 % | 56.0 px | 0.87 | 1.02 | 469 |
| tilted | 18 % → 18 % | 50.1 px | 0.87 | 1.01 | 273 |
| over the wet one | 37 % → 38 % | 52.5 px | 0.87 | 1.04 | 249 |
| long, no reload | 81 % → 86 % | 36.4 px | 0.87 | 1.06 | 1453 | quarters: 0.84 → 0.84 → 0.81 → 0.70

Numbers say: light vs heavy: width 55.5 → 64.9 px, dark 0.88 → 0.89.

## Refs v3 · #23 Report dry white mask
Ink 0.93 · Gouache 0.07 · 64 px · 60.2 s

![Refs v3 · #23 Report dry white mask](Refs-v3-23-Report-dry-white-mask.png)

A light paint: laid on a grey sheet (on white it cannot be seen); **dark** = how far it is from the grey either way.

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 20 % → 21 % | 56.8 px | 0.38 | 1.06 | 151 |
| heavy line | 21 % → 22 % | 62.4 px | 0.39 | 1.05 | 299 |
| pressure swell | 16 % → 17 % | 59.1 px | 0.37 | 1.08 | 186 |
| fast wave | 51 % → 51 % | 58.5 px | 0.30 | 1.01 | 615 |
| slow wave | 48 % → 49 % | 55.5 px | 0.38 | 1.02 | 997 |
| spiral | 66 % → 61 % | 43.8 px | 0.35 | 0.93 | 1002 |
| loop | 42 % → 44 % | 54.3 px | 0.39 | 1.04 | 635 |
| tilted | 17 % → 17 % | 48.0 px | 0.34 | 1.01 | 308 |
| over the wet one | 36 % → 38 % | 52.5 px | 0.34 | 1.07 | 412 |
| long, no reload | 79 % → 77 % | 35.5 px | 0.34 | 0.97 | 1628 | quarters: 0.00 → 0.00 → 0.00 → 0.00

Numbers say: light vs heavy: width 56.8 → 62.4 px, dark 0.38 → 0.39; pressure barely changes the width.

## Refs v3 · #24 Picasso flat oil
Gouache 1.00 + turpentine 20 % · 53 px · 43.3 s

![Refs v3 · #24 Picasso flat oil](Refs-v3-24-Picasso-flat-oil.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 17 % → 16 % | 49.6 px | 0.13 | 0.94 | 211 |
| heavy line | 18 % → 17 % | 53.4 px | 0.13 | 0.94 | 191 |
| pressure swell | 14 % → 13 % | 51.6 px | 0.18 | 0.96 | 170 |
| fast wave | 42 % → 16 % | 48.3 px | 0.21 | 0.39 | 589 |
| slow wave | 42 % → 19 % | 49.0 px | 0.15 | 0.44 | 1071 |
| spiral | 60 % → 22 % | 39.9 px | 0.18 | 0.36 | 1589 |
| loop | 36 % → 20 % | 47.1 px | 0.12 | 0.54 | 547 |
| tilted | 14 % → 15 % | 40.4 px | 0.16 | 1.00 | 301 |
| over the wet one | 31 % → 27 % | 45.8 px | 0.16 | 0.86 | 219 |
| long, no reload | 76 % → 18 % | 34.1 px | 0.15 | 0.23 | 1301 | quarters: 0.12 → 0.05 → 0.01 → 0.00

Numbers say: light vs heavy: width 49.6 → 53.4 px, dark 0.13 → 0.13; pressure barely changes the width.

## Refs v3 · #25 Yellow heavy stroke
Impasto 1.00 · 160 px · 48.4 s

![Refs v3 · #25 Yellow heavy stroke](Refs-v3-25-Yellow-heavy-stroke.png)

A light paint: laid on a grey sheet (on white it cannot be seen); **dark** = how far it is from the grey either way.

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 46 % → 43 % | 133.4 px | 0.26 | 0.93 | 701 |
| heavy line | 46 % → 30 % | 134.8 px | 0.25 | 0.65 | 1002 |
| pressure swell | 36 % → 35 % | 136.4 px | 0.24 | 0.97 | 599 |
| fast wave | 84 % → 39 % | 97.6 px | 0.21 | 0.46 | 2136 |
| slow wave | 85 % → 33 % | 98.4 px | 0.23 | 0.39 | 3712 |
| spiral | 89 % → 32 % | 58.7 px | 0.21 | 0.36 | 4108 |
| loop | 78 % → 39 % | 100.7 px | 0.24 | 0.50 | 2986 |
| tilted | 34 % → 34 % | 95.5 px | 0.23 | 1.00 | 1583 |
| over the wet one | 69 % → 55 % | 97.7 px | 0.23 | 0.79 | 1219 |
| long, no reload | 95 % → 41 % | 42.4 px | 0.23 | 0.44 | 5946 | quarters: 0.00 → 0.00 → 0.00 → 0.02

Numbers say: light vs heavy: width 133.4 → 134.8 px, dark 0.26 → 0.25; pressure barely changes the width; the long stroke does not run out of paint.

## Refs v3 · #26 Ink caricature
Ink 0.98 · 64 px · 41.3 s

![Refs v3 · #26 Ink caricature](Refs-v3-26-Ink-caricature.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 6 % → 9 % | 17.6 px | 0.77 | 1.52 | 71 |
| heavy line | 20 % → 21 % | 58.8 px | 0.82 | 1.06 | 337 |
| pressure swell | 11 % → 13 % | 42.1 px | 0.82 | 1.13 | 142 |
| fast wave | 41 % → 43 % | 46.9 px | 0.84 | 1.06 | 480 |
| slow wave | 36 % → 40 % | 41.4 px | 0.82 | 1.11 | 611 |
| spiral | 59 % → 61 % | 39.2 px | 0.80 | 1.02 | 628 |
| loop | 31 % → 34 % | 40.0 px | 0.82 | 1.10 | 383 |
| tilted | 19 % → 19 % | 53.9 px | 0.82 | 1.00 | 240 |
| over the wet one | 33 % → 35 % | 38.9 px | 0.82 | 1.06 | 204 |
| long, no reload | 78 % → 80 % | 35.1 px | 0.81 | 1.02 | 1159 | quarters: 0.72 → 0.71 → 0.70 → 0.66

Numbers say: light vs heavy: width 17.6 → 58.8 px, dark 0.77 → 0.82; the long stroke does not run out of paint; wet paint spreads well beyond the stroke.

## Refs v3 · #27 Orange impasto swatch
Impasto 1.00 · 57 px · 20.2 s

![Refs v3 · #27 Orange impasto swatch](Refs-v3-27-Orange-impasto-swatch.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 17 % → 12 % | 50.0 px | 0.35 | 0.71 | 202 |
| heavy line | 18 % → 11 % | 52.9 px | 0.34 | 0.58 | 231 |
| pressure swell | 14 % → 10 % | 51.7 px | 0.37 | 0.73 | 164 |
| fast wave | 39 % → 10 % | 45.3 px | 0.39 | 0.26 | 557 |
| slow wave | 41 % → 12 % | 47.4 px | 0.37 | 0.29 | 925 |
| spiral | 52 % → 14 % | 34.1 px | 0.38 | 0.28 | 849 |
| loop | 37 % → 15 % | 47.4 px | 0.37 | 0.41 | 554 |
| tilted | 15 % → 15 % | 40.5 px | 0.37 | 1.00 | 345 |
| over the wet one | 31 % → 22 % | 45.6 px | 0.37 | 0.72 | 301 |
| long, no reload | 57 % → 14 % | 25.5 px | 0.39 | 0.25 | 1291 | quarters: 0.29 → 0.09 → 0.02 → 0.00

Numbers say: light vs heavy: width 50.0 → 52.9 px, dark 0.35 → 0.34; pressure barely changes the width.

## Refs v3 · #28 Miles Davis lines
Ink 0.98 · 20 px · 30.5 s

![Refs v3 · #28 Miles Davis lines](Refs-v3-28-Miles-Davis-lines.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 2 % → 6 % | 5.4 px | 0.33 | 3.20 | 43 |
| heavy line | 9 % → 11 % | 25.9 px | 0.43 | 1.24 | 109 |
| pressure swell | 5 % → 7 % | 17.5 px | 0.43 | 1.49 | 62 |
| fast wave | 16 % → 21 % | 18.2 px | 0.46 | 1.34 | 173 |
| slow wave | 13 % → 19 % | 15.4 px | 0.40 | 1.45 | 203 |
| spiral | 22 % → 29 % | 14.5 px | 0.36 | 1.32 | 266 |
| loop | 13 % → 17 % | 16.4 px | 0.41 | 1.37 | 168 |
| tilted | 8 % → 8 % | 22.7 px | 0.45 | 1.03 | 82 |
| over the wet one | 14 % → 18 % | 17.4 px | 0.45 | 1.23 | 71 |
| long, no reload | 33 % → 39 % | 14.6 px | 0.41 | 1.19 | 485 | quarters: 0.23 → 0.19 → 0.16 → 0.13

Numbers say: light vs heavy: width 5.4 → 25.9 px, dark 0.33 → 0.43; wet paint spreads well beyond the stroke.

## Refs v3 · #29 Shrigley asterisk
Watercolour 1.00 + water 50 % · 64 px · 48.7 s

![Refs v3 · #29 Shrigley asterisk](Refs-v3-29-Shrigley-asterisk.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 18 % → 21 % | 51.8 px | 0.58 | 1.19 | 157 |
| heavy line | 35 % → 35 % | 103.0 px | 0.57 | 1.00 | 336 |
| pressure swell | 22 % → 24 % | 82.6 px | 0.59 | 1.08 | 248 |
| fast wave | 64 % → 68 % | 74.2 px | 0.59 | 1.05 | 1014 |
| slow wave | 61 % → 61 % | 69.9 px | 0.57 | 1.01 | 1345 |
| spiral | 73 % → 73 % | 48.1 px | 0.56 | 1.01 | 1256 |
| loop | 54 % → 54 % | 69.6 px | 0.57 | 1.01 | 697 |
| tilted | 22 % → 22 % | 61.3 px | 0.59 | 1.00 | 460 |
| over the wet one | 48 % → 51 % | 72.8 px | 0.59 | 1.07 | 322 |
| long, no reload | 91 % → 93 % | 40.9 px | 0.56 | 1.01 | 1702 | quarters: 0.57 → 0.57 → 0.54 → 0.45

Numbers say: light vs heavy: width 51.8 → 103.0 px, dark 0.58 → 0.57.

## Refs v3 · #30 Red gouache face
Gouache 1.00 + water 15 % · 55 px · 46.8 s

![Refs v3 · #30 Red gouache face](Refs-v3-30-Red-gouache-face.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 17 % → 16 % | 48.8 px | 0.49 | 0.98 | 201 |
| heavy line | 18 % → 17 % | 51.7 px | 0.50 | 0.98 | 239 |
| pressure swell | 13 % → 13 % | 49.4 px | 0.50 | 1.00 | 187 |
| fast wave | 36 % → 26 % | 41.7 px | 0.48 | 0.72 | 611 |
| slow wave | 41 % → 32 % | 47.2 px | 0.49 | 0.78 | 1414 |
| spiral | 54 % → 33 % | 35.6 px | 0.48 | 0.61 | 1280 |
| loop | 34 % → 30 % | 44.1 px | 0.50 | 0.88 | 421 |
| tilted | 14 % → 15 % | 40.1 px | 0.52 | 1.01 | 275 |
| over the wet one | 31 % → 29 % | 45.8 px | 0.52 | 0.95 | 218 |
| long, no reload | 61 % → 35 % | 27.2 px | 0.47 | 0.57 | 1233 | quarters: 0.41 → 0.35 → 0.27 → 0.21

Numbers say: light vs heavy: width 48.8 → 51.7 px, dark 0.49 → 0.50; pressure barely changes the width.

## Refs v3 · #31 Warhol blotted line
Ink 0.98 · 31 px · 33.4 s

![Refs v3 · #31 Warhol blotted line](Refs-v3-31-Warhol-blotted-line.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 4 % → 7 % | 12.3 px | 0.55 | 1.71 | 51 |
| heavy line | 11 % → 13 % | 32.7 px | 0.62 | 1.15 | 125 |
| pressure swell | 6 % → 8 % | 23.4 px | 0.61 | 1.31 | 102 |
| fast wave | 22 % → 26 % | 25.7 px | 0.65 | 1.18 | 231 |
| slow wave | 20 % → 25 % | 23.4 px | 0.61 | 1.23 | 301 |
| spiral | 32 % → 38 % | 21.1 px | 0.59 | 1.19 | 317 |
| loop | 18 % → 22 % | 22.9 px | 0.61 | 1.22 | 162 |
| tilted | 11 % → 11 % | 31.4 px | 0.63 | 1.00 | 109 |
| over the wet one | 19 % → 22 % | 22.3 px | 0.63 | 1.12 | 90 |
| long, no reload | 44 % → 48 % | 19.9 px | 0.60 | 1.08 | 598 | quarters: 0.37 → 0.34 → 0.30 → 0.27

Numbers say: light vs heavy: width 12.3 → 32.7 px, dark 0.55 → 0.62; wet paint spreads well beyond the stroke.

## Refs v3 · #32 Thick orange swipes
Impasto 1.00 · 55 px · 25.2 s

![Refs v3 · #32 Thick orange swipes](Refs-v3-32-Thick-orange-swipes.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 16 % → 11 % | 47.5 px | 0.24 | 0.69 | 301 |
| heavy line | 17 % → 11 % | 49.8 px | 0.25 | 0.61 | 279 |
| pressure swell | 13 % → 10 % | 49.8 px | 0.28 | 0.74 | 164 |
| fast wave | 40 % → 10 % | 46.5 px | 0.32 | 0.24 | 525 |
| slow wave | 40 % → 12 % | 45.9 px | 0.25 | 0.30 | 850 |
| spiral | 53 % → 14 % | 35.2 px | 0.27 | 0.27 | 846 |
| loop | 34 % → 14 % | 43.8 px | 0.24 | 0.41 | 501 |
| tilted | 14 % → 14 % | 39.4 px | 0.28 | 1.00 | 278 |
| over the wet one | 30 % → 22 % | 44.8 px | 0.28 | 0.74 | 271 |
| long, no reload | 54 % → 13 % | 24.4 px | 0.27 | 0.25 | 1199 | quarters: 0.16 → 0.02 → 0.00 → 0.00

Numbers say: light vs heavy: width 47.5 → 49.8 px, dark 0.24 → 0.25; pressure barely changes the width.

## Refs v3 · #33 Red wet-in-wet flames
Watercolour 1.00 + water 60 % · 96 px · 65.0 s

![Refs v3 · #33 Red wet-in-wet flames](Refs-v3-33-Red-wet-in-wet-flames.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 30 % → 53 % | 87.2 px | 0.47 | 1.78 | 253 |
| heavy line | 49 % → 59 % | 141.8 px | 0.53 | 1.21 | 467 |
| pressure swell | 30 % → 48 % | 110.9 px | 0.49 | 1.62 | 302 |
| fast wave | 75 % → 87 % | 87.1 px | 0.61 | 1.16 | 1073 |
| slow wave | 78 % → 87 % | 89.8 px | 0.58 | 1.12 | 1755 |
| spiral | 88 % → 98 % | 58.1 px | 0.57 | 1.11 | 2253 |
| loop | 68 % → 83 % | 88.7 px | 0.57 | 1.21 | 1174 |
| tilted | 40 % → 42 % | 112.1 px | 0.55 | 1.05 | 953 |
| over the wet one | 72 % → 92 % | 87.8 px | 0.55 | 1.28 | 592 |
| long, no reload | 96 % → 100 % | 42.9 px | 0.61 | 1.04 | 3141 | quarters: 0.67 → 0.65 → 0.63 → 0.53

Numbers say: light vs heavy: width 87.2 → 141.8 px, dark 0.47 → 0.53; wet paint spreads well beyond the stroke.

## Refs v3 · #34 Magenta oil patches
Gouache 1.00 + turpentine 20 % · 65 px · 47.9 s

![Refs v3 · #34 Magenta oil patches](Refs-v3-34-Magenta-oil-patches.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 21 % → 19 % | 59.5 px | 0.31 | 0.92 | 269 |
| heavy line | 22 % → 20 % | 64.0 px | 0.30 | 0.92 | 426 |
| pressure swell | 16 % → 16 % | 60.8 px | 0.34 | 0.97 | 225 |
| fast wave | 49 % → 20 % | 57.0 px | 0.34 | 0.41 | 971 |
| slow wave | 50 % → 24 % | 58.0 px | 0.33 | 0.48 | 1937 |
| spiral | 67 % → 24 % | 43.9 px | 0.36 | 0.36 | 1386 |
| loop | 43 % → 24 % | 55.5 px | 0.31 | 0.56 | 712 |
| tilted | 17 % → 17 % | 46.1 px | 0.33 | 1.01 | 387 |
| over the wet one | 36 % → 32 % | 53.6 px | 0.33 | 0.89 | 307 |
| long, no reload | 83 % → 22 % | 37.4 px | 0.33 | 0.27 | 1756 | quarters: 0.30 → 0.22 → 0.10 → 0.03

Numbers say: light vs heavy: width 59.5 → 64.0 px, dark 0.31 → 0.30; pressure barely changes the width.

## Refs v3 · #35 Red band with runs
Watercolour 1.00 + water 75 % · 88 px · 69.1 s

![Refs v3 · #35 Red band with runs](Refs-v3-35-Red-band-with-runs.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 40 % → 57 % | 117.2 px | 0.24 | 1.41 | 236 |
| heavy line | 59 % → 64 % | 170.6 px | 0.35 | 1.10 | 739 |
| pressure swell | 26 % → 40 % | 97.3 px | 0.32 | 1.54 | 327 |
| fast wave | 70 % → 82 % | 81.0 px | 0.43 | 1.17 | 1536 |
| slow wave | 72 % → 81 % | 83.4 px | 0.44 | 1.12 | 2224 |
| spiral | 94 % → 99 % | 62.2 px | 0.19 | 1.05 | 1983 |
| loop | 83 % → 92 % | 106.9 px | 0.39 | 1.12 | 798 |
| tilted | 45 % → 46 % | 125.8 px | 0.35 | 1.02 | 452 |
| over the wet one | 72 % → 88 % | 75.0 px | 0.35 | 1.23 | 410 |
| long, no reload | 95 % → 100 % | 42.4 px | 0.28 | 1.06 | 2527 | quarters: 0.41 → 0.34 → 0.25 → 0.13

Numbers say: light vs heavy: width 117.2 → 170.6 px, dark 0.24 → 0.35; wet paint spreads well beyond the stroke.

## Refs v3 · #36 Magenta letters flat
Gouache 1.00 + water 15 % · 64 px · 47.0 s

![Refs v3 · #36 Magenta letters flat](Refs-v3-36-Magenta-letters-flat.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 18 % → 18 % | 52.0 px | 0.39 | 0.99 | 315 |
| heavy line | 21 % → 19 % | 60.8 px | 0.39 | 0.92 | 341 |
| pressure swell | 16 % → 16 % | 58.9 px | 0.39 | 1.00 | 202 |
| fast wave | 42 % → 33 % | 48.9 px | 0.39 | 0.77 | 1021 |
| slow wave | 46 % → 36 % | 53.1 px | 0.38 | 0.79 | 1100 |
| spiral | 55 % → 36 % | 36.1 px | 0.39 | 0.65 | 1095 |
| loop | 39 % → 34 % | 51.0 px | 0.39 | 0.85 | 539 |
| tilted | 16 % → 16 % | 44.8 px | 0.40 | 1.01 | 288 |
| over the wet one | 35 % → 33 % | 52.4 px | 0.40 | 0.96 | 279 |
| long, no reload | 66 % → 40 % | 29.5 px | 0.37 | 0.61 | 1618 | quarters: 0.33 → 0.29 → 0.24 → 0.18

Numbers say: light vs heavy: width 52.0 → 60.8 px, dark 0.39 → 0.39.

## Refs v3 · #37 Oil still life
Gouache 1.00 + turpentine 20 % · 20 px · 32.2 s

![Refs v3 · #37 Oil still life](Refs-v3-37-Oil-still-life.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 7 % → 7 % | 20.8 px | 0.31 | 0.99 | 104 |
| heavy line | 8 % → 7 % | 23.0 px | 0.33 | 0.87 | 200 |
| pressure swell | 6 % → 6 % | 20.7 px | 0.37 | 1.15 | 83 |
| fast wave | 18 % → 6 % | 20.6 px | 0.38 | 0.33 | 274 |
| slow wave | 19 % → 7 % | 21.9 px | 0.35 | 0.38 | 408 |
| spiral | 28 % → 7 % | 18.3 px | 0.36 | 0.24 | 440 |
| loop | 15 % → 6 % | 19.3 px | 0.33 | 0.43 | 234 |
| tilted | 8 % → 8 % | 21.2 px | 0.36 | 1.05 | 132 |
| over the wet one | 15 % → 14 % | 21.2 px | 0.36 | 0.91 | 108 |
| long, no reload | 31 % → 8 % | 13.7 px | 0.33 | 0.25 | 569 | quarters: 0.15 → 0.04 → 0.01 → 0.00

Numbers say: light vs heavy: width 20.8 → 23.0 px, dark 0.31 → 0.33; pressure barely changes the width.

## Refs v3 · #38 Sanguine drawing
Charcoal 0.50 · Pastel 0.50 · 13 px · 9.5 s

![Refs v3 · #38 Sanguine drawing](Refs-v3-38-Sanguine-drawing.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 3 % → 3 % | 9.7 px | 0.31 | 1.00 | 32 |
| heavy line | 5 % → 5 % | 13.3 px | 0.31 | 1.00 | 29 |
| pressure swell | 3 % → 3 % | 10.1 px | 0.27 | 1.00 | 36 |
| fast wave | 10 % → 10 % | 11.3 px | 0.30 | 1.00 | 74 |
| slow wave | 10 % → 10 % | 11.8 px | 0.30 | 1.00 | 79 |
| spiral | 16 % → 16 % | 10.7 px | 0.30 | 1.00 | 128 |
| loop | 8 % → 8 % | 10.9 px | 0.30 | 1.00 | 69 |
| tilted | 4 % → 4 % | 11.6 px | 0.31 | 1.00 | 31 |
| over the wet one | 8 % → 8 % | 11.7 px | 0.31 | 1.00 | 33 |
| long, no reload | 20 % → 20 % | 8.9 px | 0.30 | 1.00 | 192 | quarters: 0.07 → 0.07 → 0.07 → 0.07

Numbers say: light vs heavy: width 9.7 → 13.3 px, dark 0.31 → 0.31; the long stroke does not run out of paint.

## Refs v3 · #39 Thick impasto weave
Impasto 1.00 · 69 px · 22.3 s

![Refs v3 · #39 Thick impasto weave](Refs-v3-39-Thick-impasto-weave.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 21 % → 16 % | 60.4 px | 0.50 | 0.76 | 255 |
| heavy line | 22 % → 13 % | 62.4 px | 0.49 | 0.59 | 272 |
| pressure swell | 17 % → 13 % | 62.3 px | 0.50 | 0.77 | 200 |
| fast wave | 46 % → 13 % | 53.2 px | 0.54 | 0.29 | 641 |
| slow wave | 48 % → 14 % | 55.6 px | 0.51 | 0.30 | 1174 |
| spiral | 58 % → 17 % | 38.1 px | 0.52 | 0.29 | 1195 |
| loop | 42 % → 18 % | 54.9 px | 0.51 | 0.43 | 640 |
| tilted | 17 % → 17 % | 46.2 px | 0.52 | 1.00 | 383 |
| over the wet one | 36 % → 27 % | 54.4 px | 0.52 | 0.75 | 303 |
| long, no reload | 67 % → 17 % | 30.1 px | 0.51 | 0.25 | 1590 | quarters: 0.45 → 0.35 → 0.31 → 0.21

Numbers say: light vs heavy: width 60.4 → 62.4 px, dark 0.50 → 0.49; pressure barely changes the width.

## Refs v3 · #40 Watercolour blooms
Watercolour 1.00 + water 55 % · 80 px · 55.1 s

![Refs v3 · #40 Watercolour blooms](Refs-v3-40-Watercolour-blooms.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 18 % → 37 % | 52.3 px | 0.07 | 2.05 | 162 |
| heavy line | 35 % → 46 % | 101.2 px | 0.07 | 1.33 | 352 |
| pressure swell | 22 % → 35 % | 80.8 px | 0.08 | 1.62 | 238 |
| fast wave | 64 % → 83 % | 74.0 px | 0.09 | 1.30 | 876 |
| slow wave | 62 % → 77 % | 71.2 px | 0.08 | 1.25 | 1615 |
| spiral | 76 % → 86 % | 50.1 px | 0.08 | 1.13 | 1582 |
| loop | 54 % → 67 % | 70.1 px | 0.08 | 1.24 | 667 |
| tilted | 26 % → 27 % | 71.7 px | 0.08 | 1.05 | 421 |
| over the wet one | 52 % → 75 % | 74.3 px | 0.08 | 1.44 | 324 |
| long, no reload | 94 % → 99 % | 42.2 px | 0.08 | 1.05 | 2023 | quarters: 0.11 → 0.09 → 0.07 → 0.06

Numbers say: light vs heavy: width 52.3 → 101.2 px, dark 0.07 → 0.07; wet paint spreads well beyond the stroke.

## Refs v3 · #41 Coloured pencil
Charcoal 0.50 · Pastel 0.50 · 13 px · 11.0 s

![Refs v3 · #41 Coloured pencil](Refs-v3-41-Coloured-pencil.png)

A light paint: laid on a grey sheet (on white it cannot be seen); **dark** = how far it is from the grey either way.

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 3 % → 3 % | 9.7 px | 0.39 | 1.00 | 31 |
| heavy line | 5 % → 5 % | 13.3 px | 0.39 | 1.00 | 32 |
| pressure swell | 3 % → 3 % | 10.1 px | 0.34 | 1.00 | 18 |
| fast wave | 10 % → 10 % | 11.3 px | 0.38 | 1.00 | 71 |
| slow wave | 10 % → 10 % | 11.8 px | 0.38 | 1.00 | 70 |
| spiral | 16 % → 16 % | 10.7 px | 0.38 | 1.00 | 154 |
| loop | 8 % → 8 % | 10.9 px | 0.38 | 1.00 | 72 |
| tilted | 4 % → 4 % | 11.6 px | 0.39 | 1.00 | 33 |
| over the wet one | 8 % → 8 % | 11.7 px | 0.39 | 1.00 | 30 |
| long, no reload | 20 % → 20 % | 8.9 px | 0.37 | 1.00 | 269 | quarters: 0.00 → 0.00 → 0.00 → 0.00

Numbers say: light vs heavy: width 9.7 → 13.3 px, dark 0.39 → 0.39; the long stroke does not run out of paint.

## Refs v3 · #42 Pink shaggy pastel
Pastel 1.00 · 27 px · 11.9 s

![Refs v3 · #42 Pink shaggy pastel](Refs-v3-42-Pink-shaggy-pastel.png)

A light paint: laid on a grey sheet (on white it cannot be seen); **dark** = how far it is from the grey either way.

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 5 % → 5 % | 15.5 px | 0.32 | 1.00 | 88 |
| heavy line | 8 % → 8 % | 22.6 px | 0.32 | 1.00 | 80 |
| pressure swell | 6 % → 6 % | 22.0 px | 0.31 | 1.00 | 78 |
| fast wave | 19 % → 19 % | 21.9 px | 0.32 | 1.00 | 237 |
| slow wave | 18 % → 18 % | 20.7 px | 0.32 | 1.00 | 309 |
| spiral | 29 % → 29 % | 19.3 px | 0.32 | 1.00 | 234 |
| loop | 15 % → 15 % | 19.0 px | 0.32 | 1.00 | 117 |
| tilted | 5 % → 5 % | 14.3 px | 0.31 | 1.00 | 93 |
| over the wet one | 12 % → 12 % | 20.2 px | 0.31 | 1.00 | 55 |
| long, no reload | 36 % → 36 % | 16.2 px | 0.32 | 1.00 | 399 | quarters: 0.00 → 0.00 → 0.00 → 0.00

Numbers say: light vs heavy: width 15.5 → 22.6 px, dark 0.32 → 0.32; the long stroke does not run out of paint.

## Refs v3 · #43 Dragged black blocks
Ink 0.93 · Gouache 0.07 · 80 px · 64.0 s

![Refs v3 · #43 Dragged black blocks](Refs-v3-43-Dragged-black-blocks.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 24 % → 26 % | 69.4 px | 0.33 | 1.07 | 244 |
| heavy line | 26 % → 27 % | 76.9 px | 0.33 | 1.02 | 496 |
| pressure swell | 20 % → 21 % | 73.1 px | 0.35 | 1.10 | 270 |
| fast wave | 59 % → 62 % | 67.7 px | 0.38 | 1.06 | 919 |
| slow wave | 56 % → 58 % | 64.9 px | 0.34 | 1.03 | 1479 |
| spiral | 71 % → 69 % | 46.9 px | 0.28 | 0.98 | 1428 |
| loop | 51 % → 53 % | 65.8 px | 0.31 | 1.04 | 690 |
| tilted | 20 % → 20 % | 56.1 px | 0.34 | 1.01 | 410 |
| over the wet one | 43 % → 45 % | 63.3 px | 0.34 | 1.06 | 349 |
| long, no reload | 87 % → 88 % | 38.8 px | 0.32 | 1.02 | 2483 | quarters: 0.33 → 0.32 → 0.30 → 0.23

Numbers say: light vs heavy: width 69.4 → 76.9 px, dark 0.33 → 0.33; pressure barely changes the width.

## Refs v3 · #44 Blue looping ribbon
Oil 0.52 · Gouache 0.48 + turpentine 10 % · 64 px · 44.4 s

![Refs v3 · #44 Blue looping ribbon](Refs-v3-44-Blue-looping-ribbon.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 20 % → 19 % | 57.0 px | 0.41 | 0.96 | 255 |
| heavy line | 20 % → 20 % | 59.5 px | 0.41 | 0.96 | 284 |
| pressure swell | 16 % → 16 % | 59.4 px | 0.44 | 0.98 | 195 |
| fast wave | 49 % → 26 % | 56.2 px | 0.48 | 0.53 | 704 |
| slow wave | 48 % → 29 % | 55.1 px | 0.45 | 0.61 | 1034 |
| spiral | 66 % → 29 % | 43.4 px | 0.43 | 0.45 | 1281 |
| loop | 42 % → 28 % | 54.5 px | 0.43 | 0.67 | 623 |
| tilted | 17 % → 17 % | 47.9 px | 0.45 | 1.00 | 506 |
| over the wet one | 36 % → 32 % | 51.6 px | 0.45 | 0.90 | 435 |
| long, no reload | 83 % → 28 % | 37.2 px | 0.43 | 0.33 | 2086 | quarters: 0.39 → 0.32 → 0.16 → 0.06

Numbers say: light vs heavy: width 57.0 → 59.5 px, dark 0.41 → 0.41; pressure barely changes the width.

## Refs v3 · #45 Pastel pepper
Pastel 1.00 · 46 px · 13.6 s

![Refs v3 · #45 Pastel pepper](Refs-v3-45-Pastel-pepper.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 8 % → 8 % | 24.2 px | 0.56 | 1.00 | 125 |
| heavy line | 14 % → 14 % | 39.4 px | 0.56 | 1.00 | 135 |
| pressure swell | 10 % → 10 % | 35.9 px | 0.56 | 1.00 | 102 |
| fast wave | 30 % → 30 % | 34.9 px | 0.56 | 1.00 | 340 |
| slow wave | 28 % → 28 % | 32.8 px | 0.56 | 1.00 | 639 |
| spiral | 46 % → 46 % | 30.5 px | 0.56 | 1.00 | 556 |
| loop | 23 % → 23 % | 29.7 px | 0.56 | 1.00 | 300 |
| tilted | 7 % → 7 % | 19.5 px | 0.56 | 1.00 | 202 |
| over the wet one | 18 % → 18 % | 32.0 px | 0.56 | 1.00 | 142 |
| long, no reload | 54 % → 54 % | 24.0 px | 0.56 | 1.00 | 954 | quarters: 0.33 → 0.33 → 0.33 → 0.33

Numbers say: light vs heavy: width 24.2 → 39.4 px, dark 0.56 → 0.56; the long stroke does not run out of paint.

## Refs v3 · #46 Ink lips on wet paper
Watercolour 1.00 + water 65 % · 56 px · 48.5 s

![Refs v3 · #46 Ink lips on wet paper](Refs-v3-46-Ink-lips-on-wet-paper.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 12 % → 29 % | 34.6 px | 0.62 | 2.45 | 89 |
| heavy line | 24 % → 37 % | 69.7 px | 0.64 | 1.55 | 199 |
| pressure swell | 14 % → 27 % | 53.7 px | 0.64 | 1.87 | 153 |
| fast wave | 48 % → 71 % | 55.0 px | 0.65 | 1.50 | 527 |
| slow wave | 45 % → 66 % | 52.1 px | 0.66 | 1.47 | 811 |
| spiral | 67 % → 78 % | 44.0 px | 0.67 | 1.17 | 937 |
| loop | 41 % → 58 % | 52.6 px | 0.66 | 1.43 | 664 |
| tilted | 19 % → 20 % | 54.1 px | 0.62 | 1.05 | 238 |
| over the wet one | 39 % → 62 % | 54.5 px | 0.62 | 1.58 | 220 |
| long, no reload | 81 % → 96 % | 36.5 px | 0.67 | 1.18 | 1220 | quarters: 0.72 → 0.72 → 0.68 → 0.59

Numbers say: light vs heavy: width 34.6 → 69.7 px, dark 0.62 → 0.64; wet paint spreads well beyond the stroke.

## Refs v3 · #47 Pink knife slabs
Gouache 1.00 + water 15 % · 240 px · 122.7 s

![Refs v3 · #47 Pink knife slabs](Refs-v3-47-Pink-knife-slabs.png)

A light paint: laid on a grey sheet (on white it cannot be seen); **dark** = how far it is from the grey either way.

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 65 % → 67 % | 189.7 px | 0.34 | 1.02 | 1164 |
| heavy line | 68 % → 64 % | 196.0 px | 0.34 | 0.94 | 2563 |
| pressure swell | 58 % → 67 % | 215.7 px | 0.31 | 1.16 | 1278 |
| fast wave | 94 % → 91 % | 108.4 px | 0.29 | 0.97 | 4251 |
| slow wave | 97 % → 85 % | 111.8 px | 0.33 | 0.88 | 8195 |
| spiral | 96 % → 82 % | 63.5 px | 0.32 | 0.85 | 7759 |
| loop | 98 % → 93 % | 126.4 px | 0.33 | 0.95 | 3783 |
| tilted | 49 % → 49 % | 136.5 px | 0.30 | 1.00 | 2608 |
| over the wet one | 85 % → 85 % | 100.9 px | 0.30 | 1.00 | 2157 |
| long, no reload | 99 % → 94 % | 44.2 px | 0.32 | 0.96 | 10439 | quarters: 0.00 → 0.00 → 0.00 → 0.00

Numbers say: light vs heavy: width 189.7 → 196.0 px, dark 0.34 → 0.34; pressure barely changes the width.

## Refs v3 · #48 Black bands with drips
Watercolour 1.00 + water 35 % · 80 px · 45.6 s

![Refs v3 · #48 Black bands with drips](Refs-v3-48-Black-bands-with-drips.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 24 % → 29 % | 68.3 px | 0.75 | 1.22 | 204 |
| heavy line | 24 % → 29 % | 70.8 px | 0.75 | 1.19 | 283 |
| pressure swell | 18 % → 24 % | 68.9 px | 0.77 | 1.29 | 215 |
| fast wave | 52 % → 60 % | 59.8 px | 0.71 | 1.17 | 812 |
| slow wave | 52 % → 57 % | 59.7 px | 0.66 | 1.10 | 1196 |
| spiral | 61 % → 66 % | 40.3 px | 0.69 | 1.08 | 1251 |
| loop | 48 % → 53 % | 61.6 px | 0.73 | 1.12 | 692 |
| tilted | 19 % → 20 % | 53.2 px | 0.77 | 1.05 | 418 |
| over the wet one | 41 % → 48 % | 60.4 px | 0.77 | 1.19 | 314 |
| long, no reload | 73 % → 83 % | 32.5 px | 0.54 | 1.14 | 2597 | quarters: 0.72 → 0.54 → 0.38 → 0.24

Numbers say: light vs heavy: width 68.3 → 70.8 px, dark 0.75 → 0.75; pressure barely changes the width.

## Refs v3 · #49 Magenta letters round
Ink 0.98 · 64 px · 40.0 s

![Refs v3 · #49 Magenta letters round](Refs-v3-49-Magenta-letters-round.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 7 % → 10 % | 21.3 px | 0.46 | 1.36 | 64 |
| heavy line | 20 % → 21 % | 57.2 px | 0.49 | 1.07 | 253 |
| pressure swell | 11 % → 13 % | 42.1 px | 0.51 | 1.13 | 171 |
| fast wave | 40 % → 43 % | 46.7 px | 0.53 | 1.06 | 436 |
| slow wave | 36 % → 40 % | 41.7 px | 0.49 | 1.11 | 588 |
| spiral | 60 % → 61 % | 39.5 px | 0.47 | 1.02 | 668 |
| loop | 31 % → 34 % | 40.1 px | 0.49 | 1.10 | 396 |
| tilted | 19 % → 19 % | 53.9 px | 0.51 | 1.01 | 242 |
| over the wet one | 33 % → 35 % | 38.9 px | 0.51 | 1.06 | 207 |
| long, no reload | 78 % → 80 % | 35.0 px | 0.47 | 1.02 | 1550 | quarters: 0.42 → 0.42 → 0.40 → 0.38

Numbers say: light vs heavy: width 21.3 → 57.2 px, dark 0.46 → 0.49; the long stroke does not run out of paint.

## Refs v3 · #50 Swipes on seaside
Gouache 1.00 + water 15 % · 57 px · 45.2 s

![Refs v3 · #50 Swipes on seaside](Refs-v3-50-Swipes-on-seaside.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 18 % → 18 % | 52.3 px | 0.31 | 0.97 | 154 |
| heavy line | 18 % → 18 % | 53.5 px | 0.32 | 0.98 | 224 |
| pressure swell | 14 % → 14 % | 53.4 px | 0.33 | 1.00 | 147 |
| fast wave | 38 % → 29 % | 43.9 px | 0.31 | 0.78 | 559 |
| slow wave | 41 % → 32 % | 47.3 px | 0.29 | 0.78 | 916 |
| spiral | 54 % → 34 % | 35.9 px | 0.28 | 0.62 | 1406 |
| loop | 35 % → 31 % | 45.7 px | 0.29 | 0.89 | 577 |
| tilted | 15 % → 15 % | 42.0 px | 0.35 | 1.01 | 270 |
| over the wet one | 32 % → 31 % | 47.0 px | 0.35 | 0.97 | 236 |
| long, no reload | 62 % → 37 % | 27.6 px | 0.24 | 0.60 | 1730 | quarters: 0.21 → 0.17 → 0.12 → 0.08

Numbers say: light vs heavy: width 52.3 → 53.5 px, dark 0.31 → 0.32; pressure barely changes the width.

## Refs v3 · #01 HW peach cloud — own sheet
own sheet 800 × 1095 · Gouache 1.00 + turpentine 30 % · 74 px · 70.7 s

![Refs v3 · #01 HW peach cloud — own sheet](Refs-v3-01-HW-peach-cloud-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 7 % → 0 % | 71.7 px | 0.00 | 0.00 | 87 |
| stroke 2 | 8 % → 3 % | 68.2 px | 0.30 | 0.31 | 179 |
| stroke 3 | 16 % → 2 % | 111.8 px | 0.30 | 0.13 | 297 |
| stroke 4 | 28 % → 1 % | 388.8 px | 0.31 | 0.04 | 93 |
| stroke 5 | 22 % → 3 % | 265.6 px | 0.30 | 0.14 | 144 |
| stroke 6 | 23 % → 2 % | 203.0 px | 0.31 | 0.10 | 302 |
| stroke 7 | 22 % → 1 % | 188.3 px | 0.30 | 0.07 | 327 |
| stroke 8 | 26 % → 1 % | 218.3 px | 0.31 | 0.04 | 329 |
| stroke 9 | 27 % → 1 % | 205.8 px | 0.31 | 0.04 | 457 |
| stroke 10 | 38 % → 0 % | 255.7 px | 0.33 | 0.01 | 490 |
| stroke 11 | 47 % → 0 % | 322.7 px | 0.33 | 0.01 | 497 |
| stroke 12 | 54 % → 1 % | 364.6 px | 0.33 | 0.01 | 404 |
| stroke 13 | 55 % → 0 % | 454.8 px | 0.00 | 0.00 | 367 |
| stroke 14 | 3 % → 0 % | 24.7 px | 0.34 | 0.05 | 97 |
| stroke 15 | 5 % → 0 % | 26.4 px | 0.00 | 0.00 | 54 |
| stroke 16 | 9 % → 0 % | 43.5 px | 0.00 | 0.00 | 70 |
| stroke 17 | 10 % → 0 % | 80.4 px | 0.00 | 0.00 | 32 |
| stroke 18 | 12 % → 0 % | 121.7 px | 0.00 | 0.00 | 26 |
| stroke 19 | 13 % → 0 % | 181.6 px | 0.00 | 0.00 | 19 |
| stroke 20 | 14 % → 0 % | 269.4 px | 0.00 | 0.00 | 17 |
| stroke 21 | 3 % → 0 % | 27.1 px | 0.00 | 0.00 | 19 |
| stroke 22 | 5 % → 0 % | 33.9 px | 0.00 | 0.00 | 61 |
| stroke 23 | 6 % → 0 % | 141.8 px | 0.00 | 0.00 | 12 |
| stroke 24 | 1 % → 1 % | 29.3 px | 0.31 | 0.67 | 14 |
| stroke 25 | 4 % → 0 % | 91.7 px | 0.00 | 0.00 | 14 |
| stroke 26 | 6 % → 0 % | 139.2 px | 0.00 | 0.00 | 23 |
| stroke 27 | 8 % → 0 % | 217.8 px | 0.00 | 0.00 | 12 |
| stroke 28 | 9 % → 0 % | 144.1 px | 0.00 | 0.00 | 24 |
| stroke 29 | 9 % → 0 % | 112.8 px | 0.00 | 0.00 | 37 |
| stroke 30 | 13 % → 0 % | 429.0 px | 0.00 | 0.00 | 27 |
| stroke 31 | 11 % → 0 % | 172.5 px | 0.32 | 0.00 | 64 |
| stroke 32 | 16 % → 0 % | 499.3 px | 0.00 | 0.00 | 18 |
| stroke 33 | 13 % → 0 % | 200.3 px | 0.32 | 0.00 | 32 |
| stroke 34 | 14 % → 0 % | 158.7 px | 0.00 | 0.00 | 49 |
| stroke 35 | 18 % → 0 % | 201.0 px | 0.00 | 0.00 | 38 |
| stroke 36 | 19 % → 0 % | 200.3 px | 0.00 | 0.00 | 52 |
| stroke 37 | 22 % → 0 % | 315.9 px | 0.00 | 0.00 | 33 |
| stroke 38 | 26 % → 0 % | 444.7 px | 0.00 | 0.00 | 23 |
| stroke 39 | 27 % → 0 % | 353.0 px | 0.00 | 0.00 | 31 |
| stroke 40 | 25 % → 0 % | 411.1 px | 0.00 | 0.00 | 22 |
| stroke 41 | 22 % → 0 % | 418.9 px | 0.00 | 0.00 | 23 |
| stroke 42 | 20 % → 0 % | 757.4 px | 0.00 | 0.00 | 8 |
| stroke 43 | 31 % → 0 % | 333.2 px | 0.00 | 0.00 | 54 |
| stroke 44 | 35 % → 0 % | 456.2 px | 0.00 | 0.00 | 23 |
| stroke 45 | 43 % → 0 % | 1091.3 px | 0.00 | 0.00 | 11 |
| stroke 46 | 1 % → 2 % | 28.0 px | 0.32 | 2.86 | 4 |
| stroke 47 | 1 % → 2 % | 41.5 px | 0.32 | 1.64 | 15 |
| stroke 48 | 2 % → 2 % | 49.3 px | 0.32 | 1.04 | 23 |
| stroke 49 | 10 % → 3 % | 399.3 px | 0.31 | 0.32 | 10 |
| stroke 50 | 8 % → 4 % | 375.7 px | 0.31 | 0.45 | 6 |
| stroke 51 | 5 % → 4 % | 217.4 px | 0.30 | 0.80 | 7 |
| stroke 52 | 5 % → 4 % | 173.5 px | 0.30 | 0.81 | 12 |
| stroke 53 | 4 % → 4 % | 165.3 px | 0.30 | 1.03 | 8 |
| stroke 54 | 4 % → 4 % | 185.7 px | 0.30 | 1.03 | 8 |
| stroke 55 | 4 % → 2 % | 170.5 px | 0.34 | 0.45 | 5 |
| stroke 56 | 5 % → 1 % | 92.3 px | 0.33 | 0.25 | 19 |
| stroke 57 | 7 % → 1 % | 56.3 px | 0.33 | 0.15 | 57 |
| stroke 58 | 11 % → 1 % | 218.8 px | 0.33 | 0.14 | 11 |
| stroke 59 | 11 % → 1 % | 77.1 px | 0.33 | 0.06 | 54 |
| stroke 60 | 16 % → 2 % | 237.5 px | 0.33 | 0.10 | 17 |
| stroke 61 | 14 % → 0 % | 54.5 px | 0.37 | 0.00 | 121 |
| stroke 62 | 20 % → 2 % | 256.7 px | 0.33 | 0.08 | 24 |
| stroke 63 | 21 % → 0 % | 85.3 px | 0.37 | 0.00 | 125 |
| stroke 64 | 28 % → 1 % | 124.9 px | 0.33 | 0.04 | 80 |
| stroke 65 | 7 % → 3 % | 91.1 px | 0.31 | 0.46 | 39 |
| stroke 66 | 7 % → 3 % | 162.0 px | 0.31 | 0.38 | 16 |
| stroke 67 | 8 % → 3 % | 57.5 px | 0.31 | 0.37 | 37 |
| stroke 68 | 11 % → 2 % | 41.3 px | 0.31 | 0.14 | 159 |
| stroke 69 | 16 % → 2 % | 79.9 px | 0.31 | 0.12 | 99 |
| stroke 70 | 5 % → 6 % | 208.0 px | 0.31 | 1.19 | 7 |
| stroke 71 | 13 % → 4 % | 127.6 px | 0.31 | 0.32 | 62 |
| stroke 72 | 12 % → 6 % | 313.0 px | 0.31 | 0.45 | 14 |
| stroke 73 | 1 % → 0 % | 27.8 px | 0.00 | 0.00 | 11 |
| stroke 74 | 1 % → 0 % | 52.0 px | 0.00 | 0.00 | 6 |
| stroke 75 | 6 % → 0 % | 92.8 px | 0.00 | 0.00 | 16 |
| stroke 76 | 7 % → 0 % | 168.7 px | 0.00 | 0.00 | 13 |
| stroke 77 | 6 % → 0 % | 49.0 px | 0.00 | 0.00 | 38 |
| stroke 78 | 9 % → 0 % | 68.1 px | 0.00 | 0.00 | 56 |
| stroke 79 | 10 % → 0 % | 286.3 px | 0.00 | 0.00 | 5 |
| stroke 80 | 10 % → 0 % | 122.8 px | 0.00 | 0.00 | 35 |
| stroke 81 | 12 % → 0 % | 468.6 px | 0.00 | 0.00 | 4 |
| stroke 82 | 12 % → 0 % | 506.4 px | 0.00 | 0.00 | 6 |
| stroke 83 | 1 % → 0 % | 26.2 px | 0.00 | 0.00 | 10 |
| stroke 84 | 4 % → 1 % | 27.3 px | 0.33 | 0.37 | 52 |
| stroke 85 | 2 % → 0 % | 29.7 px | 0.00 | 0.00 | 15 |
| stroke 86 | 2 % → 3 % | 33.1 px | 0.30 | 1.34 | 33 |
| stroke 87 | 3 % → 5 % | 61.9 px | 0.30 | 2.00 | 15 |
| stroke 88 | 2 % → 4 % | 55.9 px | 0.30 | 2.70 | 3 |
| stroke 89 | 3 % → 2 % | 33.1 px | 0.31 | 0.80 | 41 |
| stroke 90 | 4 % → 1 % | 115.6 px | 0.29 | 0.34 | 8 |
| stroke 91 | 1 % → 5 % | 24.3 px | 0.31 | 6.14 | 6 |
| stroke 92 | 6 % → 0 % | 49.0 px | 0.30 | 0.03 | 56 |
| stroke 93 | 10 % → 0 % | 77.2 px | 0.00 | 0.00 | 60 |
| stroke 94 | 2 % → 1 % | 26.2 px | 0.31 | 0.43 | 43 |
| stroke 95 | 4 % → 0 % | 134.7 px | 0.00 | 0.00 | 10 |
| stroke 96 | 5 % → 0 % | 85.0 px | 0.00 | 0.00 | 21 |
| stroke 97 | 7 % → 0 % | 158.1 px | 0.00 | 0.00 | 12 |
| stroke 98 | 5 % → 0 % | 69.8 px | 0.00 | 0.00 | 5 |
| stroke 99 | 2 % → 0 % | 28.2 px | 0.33 | 0.30 | 22 |
| stroke 100 | 3 % → 2 % | 87.5 px | 0.33 | 0.53 | 10 |
| stroke 101 | 5 % → 1 % | 49.4 px | 0.33 | 0.29 | 31 |
| stroke 102 | 7 % → 1 % | 74.0 px | 0.33 | 0.12 | 34 |
| stroke 103 | 10 % → 0 % | 105.5 px | 0.27 | 0.00 | 24 |
| stroke 104 | 13 % → 0 % | 163.2 px | 0.00 | 0.00 | 20 |
| stroke 105 | 17 % → 0 % | 279.3 px | 0.00 | 0.00 | 14 |
| stroke 106 | 1 % → 3 % | 32.5 px | 0.31 | 4.38 | 5 |
| stroke 107 | 1 % → 2 % | 47.0 px | 0.30 | 1.57 | 7 |
| stroke 108 | 2 % → 1 % | 54.1 px | 0.29 | 0.63 | 20 |
| stroke 109 | 4 % → 1 % | 43.6 px | 0.29 | 0.25 | 46 |
| stroke 110 | 6 % → 1 % | 55.6 px | 0.29 | 0.17 | 127 |
| stroke 111 | 8 % → 2 % | 177.1 px | 0.29 | 0.18 | 37 |
| stroke 112 | 10 % → 6 % | 163.8 px | 0.30 | 0.67 | 22 |
| stroke 113 | 10 % → 5 % | 131.1 px | 0.30 | 0.54 | 34 |
| stroke 114 | 10 % → 4 % | 85.3 px | 0.31 | 0.38 | 67 |
| stroke 115 | 3 % → 2 % | 67.6 px | 0.31 | 0.69 | 18 |
| stroke 116 | 12 % → 4 % | 95.0 px | 0.31 | 0.32 | 57 |
| stroke 117 | 3 % → 1 % | 71.5 px | 0.30 | 0.25 | 18 |
| stroke 118 | 12 % → 4 % | 93.1 px | 0.31 | 0.30 | 86 |
| stroke 119 | 16 % → 4 % | 167.8 px | 0.31 | 0.28 | 49 |
| stroke 120 | 8 % → 1 % | 107.9 px | 0.30 | 0.14 | 31 |
| stroke 121 | 15 % → 4 % | 374.7 px | 0.31 | 0.28 | 20 |
| stroke 122 | 17 % → 4 % | 485.5 px | 0.31 | 0.23 | 13 |
| stroke 123 | 9 % → 0 % | 161.5 px | 0.30 | 0.05 | 19 |
| stroke 124 | 9 % → 0 % | 366.9 px | 0.00 | 0.00 | 7 |
| stroke 125 | 6 % → 3 % | 82.4 px | 0.30 | 0.62 | 33 |
| stroke 126 | 9 % → 3 % | 131.1 px | 0.30 | 0.38 | 35 |
| stroke 127 | 11 % → 3 % | 188.0 px | 0.30 | 0.30 | 27 |
| stroke 128 | 9 % → 2 % | 45.7 px | 0.31 | 0.20 | 174 |
| stroke 129 | 12 % → 2 % | 60.8 px | 0.31 | 0.15 | 155 |
| stroke 130 | 5 % → 4 % | 50.8 px | 0.31 | 0.83 | 92 |
| stroke 131 | 7 % → 3 % | 175.0 px | 0.31 | 0.43 | 24 |
| stroke 132 | 6 % → 3 % | 100.1 px | 0.32 | 0.55 | 34 |
| stroke 133 | 8 % → 3 % | 108.1 px | 0.31 | 0.43 | 36 |
| stroke 134 | 9 % → 1 % | 224.2 px | 0.34 | 0.10 | 21 |
| stroke 135 | 15 % → 0 % | 670.9 px | 0.00 | 0.00 | 4 |
| stroke 136 | 13 % → 0 % | 448.9 px | 0.00 | 0.00 | 6 |
| stroke 137 | 13 % → 0 % | 583.7 px | 0.00 | 0.00 | 5 |
| stroke 138 | 12 % → 0 % | 392.8 px | 0.00 | 0.00 | 21 |
| stroke 139 | 12 % → 0 % | 333.3 px | 0.00 | 0.00 | 8 |
| stroke 140 | 12 % → 0 % | 537.3 px | 0.00 | 0.00 | 6 |
| stroke 141 | 14 % → 0 % | 466.9 px | 0.00 | 0.00 | 5 |
| stroke 142 | 13 % → 0 % | 347.5 px | 0.00 | 0.00 | 10 |
| stroke 143 | 12 % → 0 % | 508.2 px | 0.00 | 0.00 | 7 |
| stroke 144 | 13 % → 0 % | 380.7 px | 0.00 | 0.00 | 9 |
| stroke 145 | 12 % → 0 % | 108.0 px | 0.00 | 0.00 | 60 |
| stroke 146 | 16 % → 0 % | 149.0 px | 0.00 | 0.00 | 76 |
| stroke 147 | 19 % → 0 % | 170.9 px | 0.00 | 0.00 | 70 |
| stroke 148 | 21 % → 0 % | 203.9 px | 0.00 | 0.00 | 58 |
| stroke 149 | 21 % → 0 % | 271.2 px | 0.00 | 0.00 | 35 |
| stroke 150 | 21 % → 0 % | 736.8 px | 0.00 | 0.00 | 15 |
| stroke 151 | 23 % → 0 % | 277.1 px | 0.00 | 0.00 | 35 |
| stroke 152 | 26 % → 0 % | 483.8 px | 0.00 | 0.00 | 10 |
| stroke 153 | 27 % → 0 % | 550.0 px | 0.00 | 0.00 | 22 |
| stroke 154 | 3 % → 3 % | 24.9 px | 0.33 | 0.97 | 47 |
| stroke 155 | 1 % → 5 % | 29.8 px | 0.30 | 5.41 | 9 |
| stroke 156 | 4 % → 5 % | 148.0 px | 0.31 | 1.39 | 5 |
| stroke 157 | 6 % → 0 % | 81.5 px | 0.34 | 0.06 | 20 |
| stroke 158 | 2 % → 3 % | 26.2 px | 0.30 | 1.26 | 49 |
| stroke 159 | 4 % → 1 % | 137.2 px | 0.29 | 0.36 | 9 |
| stroke 160 | 4 % → 0 % | 26.6 px | 0.00 | 0.00 | 74 |
| stroke 161 | 3 % → 0 % | 27.4 px | 0.00 | 0.00 | 18 |
| stroke 162 | 2 % → 3 % | 21.0 px | 0.30 | 1.48 | 33 |
| stroke 163 | 3 % → 3 % | 32.2 px | 0.30 | 0.82 | 43 |
| stroke 164 | 5 % → 3 % | 63.3 px | 0.31 | 0.61 | 27 |
| stroke 165 | 7 % → 3 % | 365.3 px | 0.31 | 0.39 | 4 |
| stroke 166 | 7 % → 2 % | 267.1 px | 0.30 | 0.22 | 10 |
| stroke 167 | 8 % → 2 % | 81.6 px | 0.30 | 0.21 | 39 |
| stroke 168 | 10 % → 1 % | 188.9 px | 0.29 | 0.13 | 25 |
| stroke 169 | 12 % → 1 % | 491.3 px | 0.29 | 0.12 | 10 |
| stroke 170 | 12 % → 1 % | 216.0 px | 0.29 | 0.11 | 15 |
| stroke 171 | 5 % → 0 % | 153.4 px | 0.00 | 0.00 | 6 |
| stroke 172 | 11 % → 1 % | 85.3 px | 0.29 | 0.08 | 96 |
| stroke 173 | 4 % → 0 % | 120.2 px | 0.00 | 0.00 | 12 |
| stroke 174 | 17 % → 2 % | 450.8 px | 0.29 | 0.10 | 13 |
| stroke 175 | 12 % → 1 % | 94.4 px | 0.29 | 0.08 | 75 |
| stroke 176 | 7 % → 0 % | 282.2 px | 0.00 | 0.00 | 5 |
| stroke 177 | 16 % → 7 % | 363.9 px | 0.30 | 0.42 | 13 |
| stroke 178 | 12 % → 2 % | 133.1 px | 0.31 | 0.16 | 31 |
| stroke 179 | 15 % → 4 % | 106.3 px | 0.30 | 0.30 | 82 |
| stroke 180 | 16 % → 4 % | 123.8 px | 0.30 | 0.25 | 82 |
| stroke 181 | 18 % → 4 % | 150.1 px | 0.30 | 0.21 | 72 |
| stroke 182 | 18 % → 0 % | 323.4 px | 0.30 | 0.02 | 21 |
| stroke 183 | 17 % → 0 % | 689.5 px | 0.00 | 0.00 | 9 |
| stroke 184 | 2 % → 0 % | 25.2 px | 0.00 | 0.00 | 23 |
| stroke 185 | 4 % → 0 % | 41.0 px | 0.00 | 0.00 | 35 |
| stroke 186 | 7 % → 0 % | 238.5 px | 0.00 | 0.00 | 8 |
| stroke 187 | 6 % → 0 % | 65.1 px | 0.00 | 0.00 | 29 |
| stroke 188 | 11 % → 0 % | 81.8 px | 0.00 | 0.00 | 49 |
| stroke 189 | 13 % → 0 % | 82.3 px | 0.00 | 0.00 | 70 |
| stroke 190 | 15 % → 0 % | 564.6 px | 0.00 | 0.00 | 6 |
| stroke 191 | 15 % → 0 % | 142.1 px | 0.00 | 0.00 | 30 |
| stroke 192 | 17 % → 0 % | 162.2 px | 0.00 | 0.00 | 27 |
| stroke 193 | 21 % → 0 % | 314.4 px | 0.00 | 0.00 | 19 |
| stroke 194 | 25 % → 0 % | 428.2 px | 0.00 | 0.00 | 8 |
| stroke 195 | 29 % → 0 % | 492.9 px | 0.00 | 0.00 | 8 |
| stroke 196 | 31 % → 0 % | 452.3 px | 0.00 | 0.00 | 8 |
| stroke 197 | 3 % → 0 % | 24.4 px | 0.00 | 0.00 | 43 |
| stroke 198 | 4 % → 0 % | 49.9 px | 0.00 | 0.00 | 42 |
| stroke 199 | 5 % → 1 % | 50.1 px | 0.33 | 0.23 | 35 |
| stroke 200 | 1 % → 3 % | 29.8 px | 0.31 | 2.13 | 26 |
| stroke 201 | 1 % → 3 % | 27.4 px | 0.29 | 2.31 | 17 |
| stroke 202 | 2 % → 4 % | 61.8 px | 0.30 | 1.77 | 9 |
| stroke 203 | 2 % → 0 % | 25.9 px | 0.00 | 0.00 | 21 |
| stroke 204 | 2 % → 2 % | 52.4 px | 0.30 | 0.77 | 23 |
| stroke 205 | 5 % → 1 % | 45.5 px | 0.30 | 0.28 | 81 |
| stroke 206 | 1 % → 2 % | 23.3 px | 0.31 | 3.20 | 8 |
| stroke 207 | 6 % → 0 % | 105.4 px | 0.00 | 0.00 | 18 |
| stroke 208 | 6 % → 0 % | 120.0 px | 0.00 | 0.00 | 24 |
| stroke 209 | 1 % → 0 % | 31.0 px | 0.00 | 0.00 | 18 |
| stroke 210 | 4 % → 0 % | 50.8 px | 0.00 | 0.00 | 30 |
| stroke 211 | 5 % → 0 % | 171.9 px | 0.00 | 0.00 | 11 |
| stroke 212 | 5 % → 0 % | 79.9 px | 0.00 | 0.00 | 16 |
| stroke 213 | 4 % → 0 % | 88.9 px | 0.00 | 0.00 | 8 |
| stroke 214 | 2 % → 0 % | 29.2 px | 0.00 | 0.00 | 17 |
| stroke 215 | 4 % → 0 % | 45.0 px | 0.00 | 0.00 | 21 |
| stroke 216 | 5 % → 0 % | 122.8 px | 0.00 | 0.00 | 13 |
| stroke 217 | 2 % → 0 % | 31.8 px | 0.00 | 0.00 | 17 |
| stroke 218 | 4 % → 0 % | 39.7 px | 0.00 | 0.00 | 34 |
| stroke 219 | 6 % → 0 % | 117.6 px | 0.00 | 0.00 | 9 |
| stroke 220 | 4 % → 1 % | 28.9 px | 0.29 | 0.32 | 92 |
| stroke 221 | 7 % → 3 % | 39.7 px | 0.29 | 0.36 | 160 |
| stroke 222 | 10 % → 3 % | 54.4 px | 0.30 | 0.31 | 162 |
| stroke 223 | 14 % → 3 % | 73.6 px | 0.30 | 0.24 | 208 |
| stroke 224 | 4 % → 3 % | 29.6 px | 0.31 | 0.85 | 109 |
| stroke 225 | 7 % → 3 % | 40.3 px | 0.31 | 0.45 | 117 |
| stroke 226 | 10 % → 3 % | 59.9 px | 0.31 | 0.35 | 121 |
| stroke 227 | 14 % → 5 % | 165.8 px | 0.31 | 0.36 | 54 |
| stroke 228 | 24 % → 3 % | 205.1 px | 0.30 | 0.11 | 63 |
| stroke 229 | 24 % → 1 % | 196.6 px | 0.29 | 0.03 | 64 |
| stroke 230 | 26 % → 1 % | 175.9 px | 0.30 | 0.03 | 105 |
| stroke 231 | 30 % → 1 % | 222.6 px | 0.29 | 0.03 | 110 |
| stroke 232 | 13 % → 0 % | 463.2 px | 0.00 | 0.00 | 12 |
| stroke 233 | 15 % → 0 % | 497.8 px | 0.00 | 0.00 | 7 |
| stroke 234 | 14 % → 0 % | 472.0 px | 0.00 | 0.00 | 7 |
| stroke 235 | 13 % → 0 % | 187.9 px | 0.00 | 0.00 | 32 |
| stroke 236 | 16 % → 0 % | 318.8 px | 0.00 | 0.00 | 19 |
| stroke 237 | 18 % → 0 % | 358.3 px | 0.00 | 0.00 | 32 |
| stroke 238 | 15 % → 0 % | 152.7 px | 0.00 | 0.00 | 64 |
| stroke 239 | 5 % → 0 % | 176.5 px | 0.00 | 0.00 | 11 |
| stroke 240 | 20 % → 0 % | 428.7 px | 0.00 | 0.00 | 17 |
| stroke 241 | 14 % → 0 % | 162.0 px | 0.00 | 0.00 | 32 |
| stroke 242 | 6 % → 0 % | 117.3 px | 0.00 | 0.00 | 20 |
| stroke 243 | 20 % → 0 % | 300.8 px | 0.00 | 0.00 | 24 |
| stroke 244 | 16 % → 0 % | 127.9 px | 0.00 | 0.00 | 51 |
| stroke 245 | 20 % → 0 % | 330.9 px | 0.00 | 0.00 | 17 |
| stroke 246 | 21 % → 0 % | 130.6 px | 0.00 | 0.00 | 94 |
| stroke 247 | 21 % → 0 % | 282.5 px | 0.00 | 0.00 | 44 |
| stroke 248 | 32 % → 0 % | 372.0 px | 0.00 | 0.00 | 28 |
| stroke 249 | 28 % → 0 % | 333.4 px | 0.00 | 0.00 | 34 |
| stroke 250 | 24 % → 0 % | 185.3 px | 0.00 | 0.00 | 69 |
| stroke 251 | 26 % → 0 % | 99.9 px | 0.00 | 0.00 | 161 |
| stroke 252 | 25 % → 0 % | 110.8 px | 0.00 | 0.00 | 121 |
| stroke 253 | 25 % → 0 % | 149.1 px | 0.00 | 0.00 | 52 |
| stroke 254 | 1 % → 2 % | 17.4 px | 0.33 | 2.08 | 8 |
| stroke 255 | 2 % → 3 % | 28.6 px | 0.31 | 1.62 | 45 |
| stroke 256 | 4 % → 4 % | 29.3 px | 0.31 | 1.11 | 97 |
| stroke 257 | 2 % → 3 % | 57.4 px | 0.31 | 1.14 | 23 |

Numbers say: wet paint spreads well beyond the stroke.

## Refs v3 · #02 HW cream strokes — own sheet
own sheet 800 × 650 · Gouache 1.00 + turpentine 30 % · 36 px · 28.3 s

![Refs v3 · #02 HW cream strokes — own sheet](Refs-v3-02-HW-cream-strokes-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 11 % → 0 % | 37.8 px | 0.00 | 0.00 | 84 |
| stroke 2 | 18 % → 0 % | 78.5 px | 0.00 | 0.00 | 39 |
| stroke 3 | 8 % → 0 % | 37.1 px | 0.00 | 0.00 | 63 |
| stroke 4 | 13 % → 0 % | 77.7 px | 0.00 | 0.00 | 27 |
| stroke 5 | 17 % → 0 % | 122.1 px | 0.00 | 0.00 | 19 |
| stroke 6 | 22 % → 0 % | 121.0 px | 0.00 | 0.00 | 37 |
| stroke 7 | 23 % → 0 % | 139.3 px | 0.00 | 0.00 | 21 |
| stroke 8 | 22 % → 0 % | 120.8 px | 0.00 | 0.00 | 29 |
| stroke 9 | 22 % → 0 % | 132.9 px | 0.00 | 0.00 | 16 |
| stroke 10 | 22 % → 0 % | 76.2 px | 0.00 | 0.00 | 51 |
| stroke 11 | 28 % → 0 % | 130.6 px | 0.00 | 0.00 | 26 |
| stroke 12 | 31 % → 0 % | 218.1 px | 0.00 | 0.00 | 8 |
| stroke 13 | 7 % → 0 % | 38.1 px | 0.00 | 0.00 | 23 |
| stroke 14 | 19 % → 0 % | 42.2 px | 0.00 | 0.00 | 183 |
| stroke 15 | 20 % → 0 % | 128.1 px | 0.00 | 0.00 | 23 |
| stroke 16 | 15 % → 0 % | 35.5 px | 0.00 | 0.00 | 153 |
| stroke 17 | 25 % → 0 % | 52.8 px | 0.00 | 0.00 | 221 |
| stroke 18 | 41 % → 0 % | 120.4 px | 0.00 | 0.00 | 80 |
| stroke 19 | 50 % → 0 % | 177.1 px | 0.00 | 0.00 | 75 |
| stroke 20 | 13 % → 0 % | 35.2 px | 0.00 | 0.00 | 86 |
| stroke 21 | 24 % → 2 % | 53.4 px | 0.60 | 0.08 | 142 |
| stroke 22 | 32 % → 8 % | 66.1 px | 0.61 | 0.26 | 172 |
| stroke 23 | 45 % → 0 % | 210.9 px | 0.00 | 0.00 | 20 |
| stroke 24 | 52 % → 6 % | 166.8 px | 0.61 | 0.11 | 73 |
| stroke 25 | 26 % → 30 % | 127.5 px | 0.61 | 1.13 | 28 |
| stroke 26 | 24 % → 48 % | 248.1 px | 0.61 | 2.01 | 7 |
| stroke 27 | 19 % → 11 % | 69.5 px | 0.61 | 0.58 | 50 |
| stroke 28 | 19 % → 18 % | 63.6 px | 0.61 | 0.91 | 84 |
| stroke 29 | 6 % → 0 % | 48.6 px | 0.00 | 0.00 | 12 |
| stroke 30 | 26 % → 7 % | 77.3 px | 0.61 | 0.27 | 78 |
| stroke 31 | 30 % → 3 % | 120.2 px | 0.61 | 0.09 | 39 |
| stroke 32 | 2 % → 0 % | 19.6 px | 0.00 | 0.00 | 4 |
| stroke 33 | 8 % → 11 % | 27.1 px | 0.61 | 1.37 | 67 |
| stroke 34 | 3 % → 0 % | 31.2 px | 0.00 | 0.00 | 6 |
| stroke 35 | 8 % → 0 % | 32.8 px | 0.00 | 0.00 | 34 |
| stroke 36 | 8 % → 0 % | 28.5 px | 0.00 | 0.00 | 39 |
| stroke 37 | 6 % → 0 % | 39.5 px | 0.00 | 0.00 | 17 |
| stroke 38 | 19 % → 0 % | 44.5 px | 0.00 | 0.00 | 110 |
| stroke 39 | 15 % → 0 % | 68.9 px | 0.00 | 0.00 | 24 |
| stroke 40 | 26 % → 0 % | 71.7 px | 0.00 | 0.00 | 77 |
| stroke 41 | 22 % → 0 % | 63.8 px | 0.00 | 0.00 | 76 |
| stroke 42 | 30 % → 0 % | 105.5 px | 0.00 | 0.00 | 49 |
| stroke 43 | 36 % → 0 % | 267.0 px | 0.00 | 0.00 | 22 |
| stroke 44 | 12 % → 0 % | 112.5 px | 0.00 | 0.00 | 13 |
| stroke 45 | 38 % → 0 % | 108.9 px | 0.00 | 0.00 | 74 |
| stroke 46 | 35 % → 0 % | 218.0 px | 0.00 | 0.00 | 23 |
| stroke 47 | 24 % → 0 % | 93.3 px | 0.00 | 0.00 | 31 |
| stroke 48 | 29 % → 0 % | 204.3 px | 0.00 | 0.00 | 17 |
| stroke 49 | 22 % → 0 % | 116.3 px | 0.00 | 0.00 | 19 |
| stroke 50 | 23 % → 0 % | 353.1 px | 0.00 | 0.00 | 6 |
| stroke 51 | 22 % → 0 % | 138.5 px | 0.00 | 0.00 | 12 |
| stroke 52 | 19 % → 0 % | 266.7 px | 0.00 | 0.00 | 7 |
| stroke 53 | 23 % → 0 % | 213.0 px | 0.00 | 0.00 | 10 |
| stroke 54 | 12 % → 0 % | 63.2 px | 0.00 | 0.00 | 23 |
| stroke 55 | 11 % → 0 % | 57.4 px | 0.00 | 0.00 | 27 |
| stroke 56 | 22 % → 0 % | 238.4 px | 0.00 | 0.00 | 6 |
| stroke 57 | 22 % → 0 % | 163.5 px | 0.00 | 0.00 | 16 |
| stroke 58 | 20 % → 0 % | 92.0 px | 0.00 | 0.00 | 29 |
| stroke 59 | 27 % → 0 % | 188.7 px | 0.00 | 0.00 | 14 |
| stroke 60 | 6 % → 0 % | 28.5 px | 0.00 | 0.00 | 12 |
| stroke 61 | 13 % → 0 % | 35.6 px | 0.00 | 0.00 | 51 |
| stroke 62 | 22 % → 0 % | 150.0 px | 0.00 | 0.00 | 7 |
| stroke 63 | 16 % → 0 % | 104.4 px | 0.00 | 0.00 | 17 |
| stroke 64 | 18 % → 0 % | 58.2 px | 0.00 | 0.00 | 50 |
| stroke 65 | 19 % → 0 % | 132.0 px | 0.00 | 0.00 | 27 |
| stroke 66 | 15 % → 0 % | 112.9 px | 0.00 | 0.00 | 12 |
| stroke 67 | 9 % → 0 % | 28.9 px | 0.00 | 0.00 | 33 |
| stroke 68 | 13 % → 0 % | 41.1 px | 0.00 | 0.00 | 47 |
| stroke 69 | 18 % → 0 % | 92.9 px | 0.00 | 0.00 | 32 |
| stroke 70 | 18 % → 0 % | 133.0 px | 0.00 | 0.00 | 20 |
| stroke 71 | 10 % → 3 % | 50.2 px | 0.60 | 0.32 | 25 |
| stroke 72 | 25 % → 0 % | 181.9 px | 0.00 | 0.00 | 17 |
| stroke 73 | 24 % → 6 % | 53.5 px | 0.61 | 0.23 | 112 |
| stroke 74 | 17 % → 20 % | 115.7 px | 0.61 | 1.17 | 16 |
| stroke 75 | 31 % → 0 % | 134.8 px | 0.62 | 0.00 | 33 |
| stroke 76 | 20 % → 30 % | 139.9 px | 0.61 | 1.54 | 15 |
| stroke 77 | 30 % → 1 % | 130.4 px | 0.61 | 0.04 | 43 |
| stroke 78 | 24 % → 38 % | 159.7 px | 0.61 | 1.59 | 12 |
| stroke 79 | 5 % → 0 % | 23.2 px | 0.00 | 0.00 | 53 |
| stroke 80 | 8 % → 0 % | 27.2 px | 0.00 | 0.00 | 66 |
| stroke 81 | 6 % → 26 % | 26.2 px | 0.61 | 4.38 | 47 |
| stroke 82 | 3 % → 0 % | 26.0 px | 0.00 | 0.00 | 18 |
| stroke 83 | 6 % → 0 % | 29.4 px | 0.00 | 0.00 | 29 |
| stroke 84 | 14 % → 0 % | 34.1 px | 0.00 | 0.00 | 190 |
| stroke 85 | 21 % → 0 % | 50.5 px | 0.00 | 0.00 | 155 |
| stroke 86 | 30 % → 0 % | 75.8 px | 0.00 | 0.00 | 185 |
| stroke 87 | 33 % → 0 % | 100.3 px | 0.00 | 0.00 | 60 |
| stroke 88 | 27 % → 0 % | 67.8 px | 0.00 | 0.00 | 106 |
| stroke 89 | 27 % → 0 % | 63.7 px | 0.00 | 0.00 | 85 |
| stroke 90 | 31 % → 0 % | 71.5 px | 0.00 | 0.00 | 80 |
| stroke 91 | 37 % → 0 % | 88.5 px | 0.00 | 0.00 | 86 |
| stroke 92 | 44 % → 0 % | 175.2 px | 0.00 | 0.00 | 27 |
| stroke 93 | 6 % → 0 % | 30.7 px | 0.00 | 0.00 | 34 |
| stroke 94 | 10 % → 0 % | 71.2 px | 0.00 | 0.00 | 16 |
| stroke 95 | 13 % → 0 % | 95.3 px | 0.00 | 0.00 | 16 |
| stroke 96 | 4 % → 0 % | 23.1 px | 0.00 | 0.00 | 17 |
| stroke 97 | 2 % → 0 % | 24.0 px | 0.00 | 0.00 | 9 |
| stroke 98 | 7 % → 0 % | 48.0 px | 0.00 | 0.00 | 35 |
| stroke 99 | 6 % → 0 % | 30.6 px | 0.00 | 0.00 | 32 |
| stroke 100 | 7 % → 0 % | 73.7 px | 0.00 | 0.00 | 12 |
| stroke 101 | 9 % → 0 % | 31.2 px | 0.00 | 0.00 | 51 |
| stroke 102 | 7 % → 0 % | 27.0 px | 0.00 | 0.00 | 61 |
| stroke 103 | 10 % → 0 % | 37.9 px | 0.62 | 0.01 | 52 |
| stroke 104 | 16 % → 31 % | 18.7 px | 0.61 | 1.95 | 267 |
| stroke 105 | 6 % → 0 % | 30.9 px | 0.00 | 0.00 | 37 |
| stroke 106 | 10 % → 0 % | 44.9 px | 0.00 | 0.00 | 36 |
| stroke 107 | 15 % → 0 % | 61.7 px | 0.00 | 0.00 | 41 |
| stroke 108 | 24 % → 0 % | 232.0 px | 0.00 | 0.00 | 6 |
| stroke 109 | 13 % → 0 % | 83.4 px | 0.00 | 0.00 | 15 |
| stroke 110 | 16 % → 0 % | 43.8 px | 0.00 | 0.00 | 70 |
| stroke 111 | 21 % → 0 % | 54.5 px | 0.00 | 0.00 | 79 |
| stroke 112 | 25 % → 0 % | 189.6 px | 0.00 | 0.00 | 58 |
| stroke 113 | 36 % → 0 % | 341.2 px | 0.00 | 0.00 | 10 |
| stroke 114 | 28 % → 0 % | 189.6 px | 0.00 | 0.00 | 25 |
| stroke 115 | 24 % → 0 % | 62.7 px | 0.00 | 0.00 | 113 |
| stroke 116 | 27 % → 0 % | 70.7 px | 0.00 | 0.00 | 107 |
| stroke 117 | 31 % → 0 % | 76.7 px | 0.00 | 0.00 | 124 |
| stroke 118 | 28 % → 0 % | 72.9 px | 0.00 | 0.00 | 125 |
| stroke 119 | 24 % → 0 % | 71.6 px | 0.00 | 0.00 | 96 |
| stroke 120 | 10 % → 0 % | 26.7 px | 0.00 | 0.00 | 63 |
| stroke 121 | 9 % → 0 % | 42.1 px | 0.00 | 0.00 | 21 |
| stroke 122 | 6 % → 0 % | 24.4 px | 0.00 | 0.00 | 26 |
| stroke 123 | 5 % → 0 % | 24.6 px | 0.00 | 0.00 | 23 |
| stroke 124 | 26 % → 53 % | 71.1 px | 0.61 | 2.03 | 237 |
| stroke 125 | 43 % → 65 % | 107.2 px | 0.61 | 1.52 | 265 |
| stroke 126 | 54 % → 55 % | 108.8 px | 0.61 | 1.02 | 439 |

Numbers say: wet paint spreads well beyond the stroke.

## Refs v3 · #03 HW navy contours — own sheet
own sheet 800 × 600 · Gouache 1.00 + turpentine 30 % · 58 px · 25.2 s

![Refs v3 · #03 HW navy contours — own sheet](Refs-v3-03-HW-navy-contours-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 11 % → 0 % | 54.8 px | 0.00 | 0.00 | 155 |
| stroke 2 | 18 % → 0 % | 89.1 px | 0.00 | 0.00 | 183 |
| stroke 3 | 25 % → 0 % | 122.7 px | 0.00 | 0.00 | 181 |
| stroke 4 | 32 % → 0 % | 160.8 px | 0.00 | 0.00 | 207 |
| stroke 5 | 33 % → 0 % | 166.7 px | 0.00 | 0.00 | 171 |
| stroke 6 | 13 % → 0 % | 142.1 px | 0.00 | 0.00 | 68 |
| stroke 7 | 25 % → 0 % | 159.7 px | 0.00 | 0.00 | 98 |
| stroke 8 | 28 % → 0 % | 163.7 px | 0.00 | 0.00 | 97 |
| stroke 9 | 27 % → 1 % | 250.7 px | 0.39 | 0.05 | 61 |
| stroke 10 | 2 % → 0 % | 18.5 px | 0.00 | 0.00 | 9 |
| stroke 11 | 3 % → 0 % | 43.4 px | 0.00 | 0.00 | 10 |
| stroke 12 | 5 % → 0 % | 61.6 px | 0.00 | 0.00 | 7 |
| stroke 13 | 6 % → 0 % | 77.3 px | 0.00 | 0.00 | 5 |
| stroke 14 | 7 % → 0 % | 113.8 px | 0.00 | 0.00 | 4 |
| stroke 15 | 8 % → 0 % | 110.2 px | 0.00 | 0.00 | 6 |
| stroke 16 | 9 % → 0 % | 141.6 px | 0.00 | 0.00 | 7 |
| stroke 17 | 10 % → 0 % | 112.8 px | 0.00 | 0.00 | 10 |
| stroke 18 | 11 % → 0 % | 149.4 px | 0.00 | 0.00 | 11 |
| stroke 19 | 12 % → 0 % | 196.6 px | 0.00 | 0.00 | 3 |
| stroke 20 | 12 % → 0 % | 192.3 px | 0.00 | 0.00 | 9 |
| stroke 21 | 12 % → 0 % | 205.1 px | 0.00 | 0.00 | 7 |
| stroke 22 | 13 % → 0 % | 219.4 px | 0.00 | 0.00 | 9 |
| stroke 23 | 13 % → 0 % | 220.3 px | 0.00 | 0.00 | 4 |
| stroke 24 | 12 % → 0 % | 253.6 px | 0.00 | 0.00 | 6 |
| stroke 25 | 13 % → 0 % | 209.7 px | 0.00 | 0.00 | 4 |
| stroke 26 | 13 % → 0 % | 166.2 px | 0.00 | 0.00 | 8 |
| stroke 27 | 8 % → 0 % | 116.9 px | 0.00 | 0.00 | 4 |
| stroke 28 | 8 % → 0 % | 95.1 px | 0.00 | 0.00 | 6 |
| stroke 29 | 8 % → 0 % | 118.3 px | 0.00 | 0.00 | 6 |
| stroke 30 | 8 % → 0 % | 137.9 px | 0.00 | 0.00 | 6 |
| stroke 31 | 8 % → 0 % | 135.8 px | 0.00 | 0.00 | 5 |
| stroke 32 | 8 % → 0 % | 119.5 px | 0.00 | 0.00 | 8 |
| stroke 33 | 9 % → 0 % | 164.4 px | 0.00 | 0.00 | 5 |
| stroke 34 | 10 % → 0 % | 171.5 px | 0.00 | 0.00 | 7 |
| stroke 35 | 11 % → 0 % | 159.5 px | 0.00 | 0.00 | 11 |
| stroke 36 | 12 % → 0 % | 160.3 px | 0.00 | 0.00 | 6 |
| stroke 37 | 13 % → 0 % | 236.4 px | 0.00 | 0.00 | 8 |
| stroke 38 | 13 % → 0 % | 233.7 px | 0.00 | 0.00 | 9 |
| stroke 39 | 13 % → 0 % | 153.7 px | 0.00 | 0.00 | 13 |
| stroke 40 | 13 % → 0 % | 158.8 px | 0.00 | 0.00 | 11 |
| stroke 41 | 14 % → 0 % | 225.1 px | 0.00 | 0.00 | 7 |
| stroke 42 | 15 % → 0 % | 232.4 px | 0.00 | 0.00 | 6 |
| stroke 43 | 16 % → 0 % | 231.6 px | 0.00 | 0.00 | 8 |
| stroke 44 | 16 % → 0 % | 239.9 px | 0.00 | 0.00 | 4 |
| stroke 45 | 17 % → 0 % | 270.8 px | 0.00 | 0.00 | 12 |
| stroke 46 | 18 % → 0 % | 225.0 px | 0.00 | 0.00 | 4 |
| stroke 47 | 18 % → 0 % | 83.9 px | 0.00 | 0.00 | 18 |
| stroke 48 | 7 % → 0 % | 151.3 px | 0.00 | 0.00 | 4 |
| stroke 49 | 15 % → 1 % | 27.0 px | 0.38 | 0.10 | 230 |
| stroke 50 | 23 % → 2 % | 38.3 px | 0.38 | 0.07 | 229 |
| stroke 51 | 20 % → 3 % | 85.6 px | 0.38 | 0.15 | 28 |
| stroke 52 | 1 % → 0 % | 33.1 px | 0.00 | 0.00 | 5 |
| stroke 53 | 6 % → 0 % | 35.0 px | 0.00 | 0.00 | 34 |
| stroke 54 | 10 % → 0 % | 43.9 px | 0.00 | 0.00 | 103 |
| stroke 55 | 14 % → 0 % | 63.6 px | 0.00 | 0.00 | 66 |
| stroke 56 | 22 % → 0 % | 205.8 px | 0.00 | 0.00 | 26 |
| stroke 57 | 15 % → 0 % | 310.5 px | 0.00 | 0.00 | 16 |
| stroke 58 | 13 % → 0 % | 314.9 px | 0.00 | 0.00 | 27 |
| stroke 59 | 15 % → 0 % | 318.0 px | 0.00 | 0.00 | 21 |
| stroke 60 | 15 % → 0 % | 319.6 px | 0.00 | 0.00 | 7 |
| stroke 61 | 14 % → 0 % | 305.7 px | 0.00 | 0.00 | 17 |
| stroke 62 | 12 % → 0 % | 254.7 px | 0.00 | 0.00 | 7 |
| stroke 63 | 11 % → 0 % | 236.7 px | 0.00 | 0.00 | 16 |
| stroke 64 | 10 % → 0 % | 195.8 px | 0.00 | 0.00 | 10 |
| stroke 65 | 10 % → 0 % | 199.4 px | 0.00 | 0.00 | 8 |
| stroke 66 | 10 % → 0 % | 197.8 px | 0.00 | 0.00 | 10 |
| stroke 67 | 10 % → 0 % | 163.2 px | 0.00 | 0.00 | 28 |
| stroke 68 | 11 % → 0 % | 177.6 px | 0.00 | 0.00 | 32 |
| stroke 69 | 11 % → 0 % | 230.6 px | 0.00 | 0.00 | 9 |
| stroke 70 | 6 % → 0 % | 33.7 px | 0.00 | 0.00 | 97 |
| stroke 71 | 9 % → 0 % | 63.8 px | 0.00 | 0.00 | 63 |
| stroke 72 | 13 % → 0 % | 194.4 px | 0.00 | 0.00 | 19 |
| stroke 73 | 15 % → 0 % | 203.0 px | 0.00 | 0.00 | 25 |
| stroke 74 | 16 % → 0 % | 275.3 px | 0.00 | 0.00 | 37 |
| stroke 75 | 18 % → 0 % | 290.9 px | 0.00 | 0.00 | 19 |
| stroke 76 | 18 % → 0 % | 365.2 px | 0.00 | 0.00 | 19 |
| stroke 77 | 15 % → 0 % | 332.4 px | 0.00 | 0.00 | 6 |
| stroke 78 | 11 % → 0 % | 92.5 px | 0.00 | 0.00 | 46 |
| stroke 79 | 13 % → 0 % | 297.2 px | 0.00 | 0.00 | 10 |
| stroke 80 | 18 % → 0 % | 109.2 px | 0.00 | 0.00 | 58 |
| stroke 81 | 14 % → 0 % | 186.6 px | 0.00 | 0.00 | 40 |
| stroke 82 | 14 % → 0 % | 208.6 px | 0.00 | 0.00 | 20 |
| stroke 83 | 15 % → 1 % | 212.7 px | 0.39 | 0.06 | 21 |
| stroke 84 | 14 % → 1 % | 219.8 px | 0.38 | 0.10 | 10 |
| stroke 85 | 16 % → 2 % | 225.0 px | 0.38 | 0.14 | 23 |
| stroke 86 | 22 % → 3 % | 152.0 px | 0.38 | 0.12 | 79 |
| stroke 87 | 24 % → 2 % | 103.4 px | 0.38 | 0.09 | 120 |
| stroke 88 | 26 % → 2 % | 114.0 px | 0.38 | 0.08 | 108 |
| stroke 89 | 27 % → 3 % | 359.5 px | 0.38 | 0.10 | 19 |
| stroke 90 | 33 % → 3 % | 226.7 px | 0.38 | 0.09 | 28 |
| stroke 91 | 31 % → 3 % | 280.9 px | 0.38 | 0.11 | 22 |
| stroke 92 | 32 % → 4 % | 529.8 px | 0.38 | 0.12 | 15 |
| stroke 93 | 31 % → 4 % | 459.3 px | 0.38 | 0.13 | 10 |
| stroke 94 | 31 % → 3 % | 244.4 px | 0.38 | 0.11 | 37 |
| stroke 95 | 23 % → 0 % | 341.8 px | 0.00 | 0.00 | 10 |
| stroke 96 | 31 % → 0 % | 193.5 px | 0.00 | 0.00 | 41 |
| stroke 97 | 17 % → 0 % | 146.4 px | 0.00 | 0.00 | 32 |
| stroke 98 | 7 % → 0 % | 129.5 px | 0.00 | 0.00 | 8 |
| stroke 99 | 10 % → 0 % | 99.9 px | 0.00 | 0.00 | 17 |
| stroke 100 | 7 % → 0 % | 83.4 px | 0.00 | 0.00 | 22 |
| stroke 101 | 9 % → 0 % | 153.4 px | 0.00 | 0.00 | 13 |
| stroke 102 | 6 % → 0 % | 66.8 px | 0.00 | 0.00 | 17 |
| stroke 103 | 6 % → 0 % | 30.0 px | 0.00 | 0.00 | 80 |
| stroke 104 | 10 % → 0 % | 142.7 px | 0.00 | 0.00 | 10 |
| stroke 105 | 10 % → 0 % | 103.1 px | 0.00 | 0.00 | 29 |
| stroke 106 | 14 % → 0 % | 257.6 px | 0.00 | 0.00 | 9 |
| stroke 107 | 15 % → 0 % | 182.2 px | 0.00 | 0.00 | 15 |
| stroke 108 | 15 % → 0 % | 138.1 px | 0.00 | 0.00 | 31 |
| stroke 109 | 17 % → 0 % | 183.2 px | 0.00 | 0.00 | 23 |
| stroke 110 | 19 % → 0 % | 266.0 px | 0.00 | 0.00 | 18 |
| stroke 111 | 19 % → 0 % | 243.4 px | 0.00 | 0.00 | 17 |
| stroke 112 | 18 % → 0 % | 103.2 px | 0.00 | 0.00 | 66 |
| stroke 113 | 18 % → 0 % | 95.2 px | 0.00 | 0.00 | 66 |
| stroke 114 | 20 % → 0 % | 104.0 px | 0.00 | 0.00 | 74 |
| stroke 115 | 23 % → 0 % | 120.2 px | 0.00 | 0.00 | 48 |
| stroke 116 | 24 % → 0 % | 131.7 px | 0.00 | 0.00 | 71 |
| stroke 117 | 28 % → 0 % | 226.6 px | 0.00 | 0.00 | 33 |
| stroke 118 | 20 % → 0 % | 442.0 px | 0.00 | 0.00 | 9 |
| stroke 119 | 20 % → 0 % | 268.0 px | 0.00 | 0.00 | 37 |
| stroke 120 | 18 % → 0 % | 104.9 px | 0.00 | 0.00 | 72 |
| stroke 121 | 6 % → 0 % | 88.5 px | 0.00 | 0.00 | 22 |
| stroke 122 | 19 % → 0 % | 89.7 px | 0.00 | 0.00 | 88 |
| stroke 123 | 2 % → 0 % | 26.2 px | 0.00 | 0.00 | 12 |
| stroke 124 | 4 % → 0 % | 34.2 px | 0.00 | 0.00 | 25 |
| stroke 125 | 1 % → 0 % | 18.6 px | 0.00 | 0.00 | 4 |
| stroke 126 | 4 % → 0 % | 86.4 px | 0.00 | 0.00 | 12 |
| stroke 127 | 4 % → 0 % | 59.5 px | 0.00 | 0.00 | 9 |
| stroke 128 | 3 % → 0 % | 68.3 px | 0.00 | 0.00 | 15 |
| stroke 129 | 5 % → 0 % | 68.0 px | 0.00 | 0.00 | 22 |
| stroke 130 | 6 % → 2 % | 57.3 px | 0.39 | 0.30 | 23 |
| stroke 131 | 5 % → 1 % | 112.3 px | 0.39 | 0.26 | 9 |
| stroke 132 | 23 % → 0 % | 59.0 px | 0.00 | 0.00 | 359 |
| stroke 133 | 32 % → 0 % | 114.5 px | 0.00 | 0.00 | 233 |
| stroke 134 | 37 % → 0 % | 157.6 px | 0.00 | 0.00 | 231 |
| stroke 135 | 7 % → 0 % | 63.8 px | 0.00 | 0.00 | 52 |
| stroke 136 | 13 % → 0 % | 106.2 px | 0.00 | 0.00 | 67 |
| stroke 137 | 2 % → 3 % | 27.5 px | 0.38 | 1.28 | 20 |

## Refs v3 · #04 HW grey cloud — own sheet
own sheet 800 × 635 · Gouache 1.00 + turpentine 30 % · 66 px · 24.5 s

![Refs v3 · #04 HW grey cloud — own sheet](Refs-v3-04-HW-grey-cloud-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 17 % → 0 % | 56.4 px | 0.18 | 0.01 | 195 |
| stroke 2 | 23 % → 0 % | 94.1 px | 0.20 | 0.02 | 248 |
| stroke 3 | 29 % → 1 % | 135.8 px | 0.20 | 0.03 | 308 |
| stroke 4 | 27 % → 0 % | 196.0 px | 0.00 | 0.00 | 106 |
| stroke 5 | 35 % → 1 % | 148.6 px | 0.20 | 0.02 | 342 |
| stroke 6 | 35 % → 0 % | 218.5 px | 0.00 | 0.00 | 138 |
| stroke 7 | 41 % → 0 % | 155.7 px | 0.00 | 0.00 | 432 |
| stroke 8 | 29 % → 0 % | 265.7 px | 0.00 | 0.00 | 74 |
| stroke 9 | 35 % → 0 % | 305.4 px | 0.00 | 0.00 | 62 |
| stroke 10 | 44 % → 0 % | 437.3 px | 0.00 | 0.00 | 96 |
| stroke 11 | 46 % → 0 % | 373.8 px | 0.00 | 0.00 | 180 |
| stroke 12 | 35 % → 0 % | 221.3 px | 0.00 | 0.00 | 139 |
| stroke 13 | 46 % → 0 % | 283.1 px | 0.00 | 0.00 | 230 |
| stroke 14 | 48 % → 0 % | 314.8 px | 0.00 | 0.00 | 318 |
| stroke 15 | 42 % → 0 % | 238.8 px | 0.00 | 0.00 | 226 |
| stroke 16 | 44 % → 0 % | 351.0 px | 0.00 | 0.00 | 117 |
| stroke 17 | 1 % → 0 % | 26.0 px | 0.00 | 0.00 | 11 |
| stroke 18 | 4 % → 0 % | 41.0 px | 0.00 | 0.00 | 9 |
| stroke 19 | 6 % → 0 % | 54.9 px | 0.00 | 0.00 | 9 |
| stroke 20 | 4 % → 0 % | 53.1 px | 0.00 | 0.00 | 34 |
| stroke 21 | 8 % → 0 % | 76.9 px | 0.00 | 0.00 | 69 |
| stroke 22 | 11 % → 0 % | 112.7 px | 0.00 | 0.00 | 95 |
| stroke 23 | 15 % → 0 % | 108.1 px | 0.00 | 0.00 | 103 |
| stroke 24 | 19 % → 0 % | 90.5 px | 0.00 | 0.00 | 250 |
| stroke 25 | 25 % → 0 % | 186.8 px | 0.00 | 0.00 | 135 |
| stroke 26 | 32 % → 0 % | 346.4 px | 0.00 | 0.00 | 71 |
| stroke 27 | 31 % → 0 % | 222.9 px | 0.00 | 0.00 | 139 |
| stroke 28 | 29 % → 0 % | 154.0 px | 0.00 | 0.00 | 188 |
| stroke 29 | 32 % → 0 % | 243.1 px | 0.00 | 0.00 | 119 |
| stroke 30 | 42 % → 0 % | 381.4 px | 0.00 | 0.00 | 202 |
| stroke 31 | 37 % → 0 % | 416.2 px | 0.00 | 0.00 | 66 |
| stroke 32 | 33 % → 0 % | 137.5 px | 0.00 | 0.00 | 315 |
| stroke 33 | 36 % → 0 % | 136.8 px | 0.00 | 0.00 | 405 |
| stroke 34 | 37 % → 0 % | 144.5 px | 0.00 | 0.00 | 334 |
| stroke 35 | 19 % → 0 % | 137.4 px | 0.00 | 0.00 | 156 |
| stroke 36 | 13 % → 0 % | 150.1 px | 0.00 | 0.00 | 41 |
| stroke 37 | 15 % → 0 % | 138.6 px | 0.00 | 0.00 | 35 |
| stroke 38 | 20 % → 0 % | 212.9 px | 0.00 | 0.00 | 82 |
| stroke 39 | 23 % → 0 % | 215.7 px | 0.00 | 0.00 | 70 |
| stroke 40 | 2 % → 2 % | 32.5 px | 0.20 | 0.93 | 15 |
| stroke 41 | 2 % → 0 % | 24.4 px | 0.00 | 0.00 | 20 |
| stroke 42 | 13 % → 3 % | 38.2 px | 0.20 | 0.19 | 84 |
| stroke 43 | 12 % → 2 % | 78.5 px | 0.20 | 0.18 | 48 |
| stroke 44 | 24 % → 2 % | 64.7 px | 0.20 | 0.06 | 178 |
| stroke 45 | 30 % → 1 % | 93.8 px | 0.20 | 0.05 | 179 |
| stroke 46 | 40 % → 2 % | 369.0 px | 0.21 | 0.06 | 23 |
| stroke 47 | 40 % → 2 % | 352.8 px | 0.20 | 0.06 | 41 |
| stroke 48 | 12 % → 0 % | 41.5 px | 0.00 | 0.00 | 68 |
| stroke 49 | 12 % → 0 % | 170.7 px | 0.00 | 0.00 | 23 |
| stroke 50 | 23 % → 0 % | 110.9 px | 0.00 | 0.00 | 58 |
| stroke 51 | 26 % → 0 % | 171.9 px | 0.00 | 0.00 | 29 |
| stroke 52 | 29 % → 0 % | 235.7 px | 0.00 | 0.00 | 35 |
| stroke 53 | 7 % → 0 % | 45.4 px | 0.00 | 0.00 | 61 |
| stroke 54 | 12 % → 0 % | 74.1 px | 0.00 | 0.00 | 78 |
| stroke 55 | 17 % → 0 % | 101.9 px | 0.00 | 0.00 | 70 |
| stroke 56 | 4 % → 0 % | 46.8 px | 0.00 | 0.00 | 27 |
| stroke 57 | 10 % → 0 % | 56.6 px | 0.00 | 0.00 | 77 |
| stroke 58 | 20 % → 0 % | 234.3 px | 0.00 | 0.00 | 20 |
| stroke 59 | 15 % → 0 % | 73.7 px | 0.00 | 0.00 | 185 |
| stroke 60 | 21 % → 0 % | 98.0 px | 0.00 | 0.00 | 208 |
| stroke 61 | 27 % → 0 % | 124.1 px | 0.00 | 0.00 | 191 |
| stroke 62 | 10 % → 0 % | 66.7 px | 0.00 | 0.00 | 64 |
| stroke 63 | 15 % → 0 % | 68.4 px | 0.00 | 0.00 | 267 |
| stroke 64 | 29 % → 0 % | 85.5 px | 0.00 | 0.00 | 671 |
| stroke 65 | 56 % → 0 % | 122.6 px | 0.00 | 0.00 | 809 |
| stroke 66 | 86 % → 0 % | 182.6 px | 0.00 | 0.00 | 592 |
| stroke 67 | 83 % → 0 % | 248.9 px | 0.00 | 0.00 | 206 |
| stroke 68 | 2 % → 3 % | 22.9 px | 0.20 | 1.32 | 14 |

## Refs v3 · #05 HW green in rust loops — own sheet
own sheet 800 × 1045 · Gouache 1.00 + turpentine 30 % · 74 px · 54.6 s

![Refs v3 · #05 HW green in rust loops — own sheet](Refs-v3-05-HW-green-in-rust-loops-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 12 % → 34 % | 70.0 px | 0.39 | 2.85 | 288 |
| stroke 2 | 22 % → 21 % | 88.1 px | 0.39 | 0.96 | 821 |
| stroke 3 | 32 % → 13 % | 129.0 px | 0.38 | 0.42 | 1049 |
| stroke 4 | 44 % → 6 % | 168.9 px | 0.39 | 0.13 | 701 |
| stroke 5 | 49 % → 1 % | 189.6 px | 0.38 | 0.01 | 740 |
| stroke 6 | 50 % → 0 % | 199.8 px | 0.00 | 0.00 | 639 |
| stroke 7 | 50 % → 0 % | 196.2 px | 0.00 | 0.00 | 641 |
| stroke 8 | 50 % → 0 % | 199.1 px | 0.00 | 0.00 | 669 |
| stroke 9 | 50 % → 0 % | 272.6 px | 0.00 | 0.00 | 393 |
| stroke 10 | 3 % → 29 % | 46.5 px | 0.38 | 8.63 | 33 |
| stroke 11 | 6 % → 27 % | 66.5 px | 0.38 | 4.78 | 52 |
| stroke 12 | 2 % → 87 % | 49.1 px | 0.39 | 44.99 | 19 |
| stroke 13 | 4 % → 84 % | 76.9 px | 0.39 | 23.30 | 25 |
| stroke 14 | 8 % → 44 % | 118.7 px | 0.38 | 5.39 | 45 |
| stroke 15 | 10 % → 45 % | 111.3 px | 0.39 | 4.35 | 67 |
| stroke 16 | 14 % → 48 % | 128.0 px | 0.39 | 3.36 | 80 |
| stroke 17 | 18 % → 45 % | 131.2 px | 0.39 | 2.44 | 106 |
| stroke 18 | 22 % → 35 % | 171.0 px | 0.39 | 1.56 | 77 |
| stroke 19 | 23 % → 35 % | 176.8 px | 0.39 | 1.49 | 85 |
| stroke 20 | 26 % → 28 % | 236.3 px | 0.39 | 1.09 | 87 |
| stroke 21 | 2 % → 0 % | 47.8 px | 0.00 | 0.00 | 24 |
| stroke 22 | 4 % → 0 % | 99.7 px | 0.00 | 0.00 | 23 |
| stroke 23 | 1 % → 0 % | 27.8 px | 0.00 | 0.00 | 11 |
| stroke 24 | 2 % → 0 % | 40.2 px | 0.00 | 0.00 | 10 |
| stroke 25 | 5 % → 0 % | 36.5 px | 0.00 | 0.00 | 39 |
| stroke 26 | 1 % → 0 % | 22.3 px | 0.00 | 0.00 | 11 |
| stroke 27 | 4 % → 0 % | 81.1 px | 0.00 | 0.00 | 7 |
| stroke 28 | 3 % → 0 % | 89.7 px | 0.00 | 0.00 | 6 |
| stroke 29 | 4 % → 25 % | 36.1 px | 0.38 | 7.14 | 19 |
| stroke 30 | 2 % → 37 % | 34.4 px | 0.39 | 19.00 | 18 |
| stroke 31 | 4 % → 37 % | 55.5 px | 0.39 | 9.95 | 18 |
| stroke 32 | 5 % → 32 % | 93.2 px | 0.39 | 5.92 | 17 |
| stroke 33 | 7 % → 30 % | 124.3 px | 0.39 | 4.27 | 16 |
| stroke 34 | 8 % → 27 % | 141.4 px | 0.40 | 3.23 | 18 |
| stroke 35 | 10 % → 24 % | 239.7 px | 0.40 | 2.28 | 9 |
| stroke 36 | 12 % → 21 % | 311.1 px | 0.40 | 1.82 | 8 |
| stroke 37 | 13 % → 21 % | 227.2 px | 0.40 | 1.65 | 19 |
| stroke 38 | 14 % → 19 % | 306.2 px | 0.40 | 1.41 | 11 |
| stroke 39 | 13 % → 18 % | 320.9 px | 0.40 | 1.32 | 10 |
| stroke 40 | 13 % → 14 % | 296.7 px | 0.39 | 1.11 | 11 |
| stroke 41 | 11 % → 7 % | 261.8 px | 0.39 | 0.67 | 12 |
| stroke 42 | 11 % → 4 % | 258.6 px | 0.37 | 0.32 | 11 |
| stroke 43 | 3 % → 13 % | 34.4 px | 0.39 | 4.62 | 21 |
| stroke 44 | 5 % → 13 % | 60.5 px | 0.39 | 2.76 | 28 |
| stroke 45 | 7 % → 13 % | 87.0 px | 0.39 | 1.86 | 23 |
| stroke 46 | 9 % → 13 % | 126.5 px | 0.39 | 1.44 | 17 |
| stroke 47 | 11 % → 13 % | 180.8 px | 0.39 | 1.18 | 12 |
| stroke 48 | 3 % → 0 % | 37.5 px | 0.00 | 0.00 | 19 |
| stroke 49 | 5 % → 0 % | 45.4 px | 0.00 | 0.00 | 33 |
| stroke 50 | 8 % → 0 % | 73.2 px | 0.00 | 0.00 | 33 |
| stroke 51 | 10 % → 0 % | 125.1 px | 0.00 | 0.00 | 24 |
| stroke 52 | 13 % → 0 % | 203.9 px | 0.00 | 0.00 | 15 |
| stroke 53 | 1 % → 0 % | 34.5 px | 0.00 | 0.00 | 7 |
| stroke 54 | 3 % → 0 % | 51.0 px | 0.00 | 0.00 | 23 |
| stroke 55 | 5 % → 0 % | 75.1 px | 0.00 | 0.00 | 19 |
| stroke 56 | 6 % → 0 % | 94.5 px | 0.00 | 0.00 | 16 |
| stroke 57 | 8 % → 0 % | 82.2 px | 0.00 | 0.00 | 36 |
| stroke 58 | 11 % → 0 % | 116.0 px | 0.00 | 0.00 | 43 |
| stroke 59 | 13 % → 0 % | 178.0 px | 0.00 | 0.00 | 21 |
| stroke 60 | 15 % → 0 % | 234.3 px | 0.00 | 0.00 | 18 |
| stroke 61 | 17 % → 0 % | 281.7 px | 0.00 | 0.00 | 21 |
| stroke 62 | 17 % → 0 % | 307.1 px | 0.00 | 0.00 | 20 |
| stroke 63 | 18 % → 0 % | 416.3 px | 0.00 | 0.00 | 10 |
| stroke 64 | 19 % → 0 % | 385.6 px | 0.00 | 0.00 | 11 |
| stroke 65 | 19 % → 0 % | 367.3 px | 0.00 | 0.00 | 10 |
| stroke 66 | 19 % → 0 % | 365.6 px | 0.00 | 0.00 | 11 |
| stroke 67 | 3 % → 31 % | 26.3 px | 0.38 | 10.77 | 14 |
| stroke 68 | 1 % → 56 % | 22.7 px | 0.38 | 41.50 | 13 |
| stroke 69 | 1 % → 0 % | 25.1 px | 0.00 | 0.00 | 10 |
| stroke 70 | 1 % → 13 % | 22.5 px | 0.39 | 20.50 | 7 |
| stroke 71 | 2 % → 8 % | 44.7 px | 0.38 | 4.73 | 6 |
| stroke 72 | 3 % → 5 % | 45.8 px | 0.37 | 2.01 | 16 |
| stroke 73 | 4 % → 2 % | 60.5 px | 0.43 | 0.50 | 14 |
| stroke 74 | 5 % → 0 % | 72.2 px | 0.00 | 0.00 | 16 |
| stroke 75 | 6 % → 0 % | 99.5 px | 0.00 | 0.00 | 14 |
| stroke 76 | 7 % → 0 % | 136.9 px | 0.00 | 0.00 | 13 |
| stroke 77 | 8 % → 0 % | 136.9 px | 0.00 | 0.00 | 14 |
| stroke 78 | 8 % → 0 % | 132.1 px | 0.00 | 0.00 | 20 |
| stroke 79 | 10 % → 0 % | 175.1 px | 0.00 | 0.00 | 18 |
| stroke 80 | 10 % → 0 % | 247.2 px | 0.00 | 0.00 | 14 |
| stroke 81 | 11 % → 0 % | 264.8 px | 0.00 | 0.00 | 11 |
| stroke 82 | 12 % → 0 % | 213.5 px | 0.00 | 0.00 | 16 |
| stroke 83 | 13 % → 0 % | 229.1 px | 0.00 | 0.00 | 16 |
| stroke 84 | 13 % → 0 % | 316.1 px | 0.00 | 0.00 | 7 |
| stroke 85 | 13 % → 0 % | 232.9 px | 0.00 | 0.00 | 13 |
| stroke 86 | 13 % → 0 % | 243.5 px | 0.00 | 0.00 | 9 |
| stroke 87 | 13 % → 0 % | 300.0 px | 0.00 | 0.00 | 7 |
| stroke 88 | 13 % → 0 % | 370.7 px | 0.00 | 0.00 | 6 |
| stroke 89 | 12 % → 0 % | 432.6 px | 0.00 | 0.00 | 10 |
| stroke 90 | 11 % → 0 % | 151.0 px | 0.00 | 0.00 | 25 |
| stroke 91 | 14 % → 0 % | 508.6 px | 0.00 | 0.00 | 5 |
| stroke 92 | 10 % → 0 % | 106.7 px | 0.00 | 0.00 | 41 |
| stroke 93 | 5 % → 0 % | 121.5 px | 0.00 | 0.00 | 13 |
| stroke 94 | 5 % → 0 % | 131.0 px | 0.00 | 0.00 | 18 |
| stroke 95 | 4 % → 0 % | 110.0 px | 0.00 | 0.00 | 12 |
| stroke 96 | 6 % → 0 % | 119.3 px | 0.00 | 0.00 | 21 |
| stroke 97 | 7 % → 0 % | 252.3 px | 0.00 | 0.00 | 9 |
| stroke 98 | 8 % → 0 % | 255.9 px | 0.00 | 0.00 | 6 |
| stroke 99 | 8 % → 0 % | 329.7 px | 0.00 | 0.00 | 11 |
| stroke 100 | 9 % → 0 % | 340.9 px | 0.00 | 0.00 | 10 |
| stroke 101 | 2 % → 33 % | 23.2 px | 0.38 | 15.88 | 31 |
| stroke 102 | 4 % → 0 % | 27.7 px | 0.00 | 0.00 | 131 |
| stroke 103 | 5 % → 0 % | 115.2 px | 0.00 | 0.00 | 25 |
| stroke 104 | 10 % → 0 % | 74.0 px | 0.00 | 0.00 | 192 |
| stroke 105 | 17 % → 0 % | 104.7 px | 0.00 | 0.00 | 251 |
| stroke 106 | 17 % → 0 % | 129.3 px | 0.00 | 0.00 | 362 |
| stroke 107 | 30 % → 0 % | 164.9 px | 0.00 | 0.00 | 470 |
| stroke 108 | 25 % → 0 % | 166.1 px | 0.00 | 0.00 | 408 |
| stroke 109 | 42 % → 0 % | 293.8 px | 0.00 | 0.00 | 192 |
| stroke 110 | 46 % → 0 % | 620.7 px | 0.00 | 0.00 | 89 |
| stroke 111 | 38 % → 0 % | 210.7 px | 0.00 | 0.00 | 499 |
| stroke 112 | 48 % → 0 % | 175.7 px | 0.00 | 0.00 | 902 |
| stroke 113 | 60 % → 0 % | 183.9 px | 0.00 | 0.00 | 915 |
| stroke 114 | 1 % → 37 % | 17.6 px | 0.38 | 36.00 | 10 |
| stroke 115 | 10 % → 43 % | 56.5 px | 0.38 | 4.28 | 122 |
| stroke 116 | 16 % → 49 % | 68.3 px | 0.39 | 3.08 | 343 |
| stroke 117 | 20 % → 35 % | 97.8 px | 0.38 | 1.78 | 218 |
| stroke 118 | 24 % → 65 % | 231.2 px | 0.39 | 2.67 | 88 |
| stroke 119 | 23 % → 54 % | 167.6 px | 0.39 | 2.38 | 157 |
| stroke 120 | 28 % → 64 % | 299.2 px | 0.39 | 2.28 | 103 |
| stroke 121 | 31 % → 72 % | 503.1 px | 0.39 | 2.31 | 53 |
| stroke 122 | 26 % → 54 % | 407.1 px | 0.39 | 2.10 | 48 |
| stroke 123 | 32 % → 60 % | 311.3 px | 0.39 | 1.85 | 121 |
| stroke 124 | 31 % → 62 % | 297.7 px | 0.39 | 2.00 | 129 |
| stroke 125 | 36 % → 69 % | 452.0 px | 0.39 | 1.93 | 86 |
| stroke 126 | 37 % → 70 % | 354.8 px | 0.39 | 1.90 | 117 |
| stroke 127 | 34 % → 68 % | 389.3 px | 0.39 | 2.01 | 86 |
| stroke 128 | 38 % → 69 % | 362.7 px | 0.39 | 1.83 | 105 |
| stroke 129 | 32 % → 62 % | 340.6 px | 0.39 | 1.97 | 89 |
| stroke 130 | 39 % → 65 % | 342.5 px | 0.39 | 1.70 | 132 |
| stroke 131 | 31 % → 45 % | 407.6 px | 0.39 | 1.43 | 96 |
| stroke 132 | 31 % → 44 % | 153.2 px | 0.39 | 1.43 | 349 |
| stroke 133 | 34 % → 42 % | 203.5 px | 0.39 | 1.23 | 263 |
| stroke 134 | 26 % → 31 % | 146.3 px | 0.39 | 1.20 | 217 |
| stroke 135 | 40 % → 43 % | 430.8 px | 0.39 | 1.06 | 99 |
| stroke 136 | 39 % → 39 % | 610.7 px | 0.39 | 1.01 | 51 |

Numbers say: wet paint spreads well beyond the stroke.

## Refs v3 · #06 HW scrubbed grey — own sheet
own sheet 800 × 635 · Gouache 1.00 + turpentine 30 % · 66 px · 23.5 s

![Refs v3 · #06 HW scrubbed grey — own sheet](Refs-v3-06-HW-scrubbed-grey-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 17 % → 0 % | 56.4 px | 0.18 | 0.01 | 195 |
| stroke 2 | 23 % → 0 % | 94.0 px | 0.20 | 0.02 | 215 |
| stroke 3 | 29 % → 1 % | 135.8 px | 0.20 | 0.03 | 264 |
| stroke 4 | 27 % → 0 % | 195.3 px | 0.00 | 0.00 | 92 |
| stroke 5 | 35 % → 1 % | 148.5 px | 0.20 | 0.02 | 339 |
| stroke 6 | 35 % → 0 % | 218.2 px | 0.00 | 0.00 | 155 |
| stroke 7 | 41 % → 0 % | 155.7 px | 0.00 | 0.00 | 371 |
| stroke 8 | 29 % → 0 % | 265.2 px | 0.00 | 0.00 | 56 |
| stroke 9 | 35 % → 0 % | 306.4 px | 0.00 | 0.00 | 69 |
| stroke 10 | 44 % → 0 % | 437.0 px | 0.00 | 0.00 | 93 |
| stroke 11 | 46 % → 0 % | 373.1 px | 0.00 | 0.00 | 131 |
| stroke 12 | 35 % → 0 % | 220.8 px | 0.00 | 0.00 | 122 |
| stroke 13 | 46 % → 0 % | 283.6 px | 0.00 | 0.00 | 102 |
| stroke 14 | 48 % → 0 % | 314.7 px | 0.00 | 0.00 | 180 |
| stroke 15 | 42 % → 0 % | 238.6 px | 0.00 | 0.00 | 198 |
| stroke 16 | 44 % → 0 % | 350.7 px | 0.00 | 0.00 | 116 |
| stroke 17 | 1 % → 0 % | 25.9 px | 0.00 | 0.00 | 16 |
| stroke 18 | 4 % → 0 % | 40.9 px | 0.00 | 0.00 | 14 |
| stroke 19 | 6 % → 0 % | 54.9 px | 0.00 | 0.00 | 12 |
| stroke 20 | 4 % → 0 % | 52.7 px | 0.00 | 0.00 | 28 |
| stroke 21 | 8 % → 0 % | 76.7 px | 0.00 | 0.00 | 69 |
| stroke 22 | 11 % → 0 % | 112.4 px | 0.00 | 0.00 | 92 |
| stroke 23 | 14 % → 0 % | 107.7 px | 0.00 | 0.00 | 128 |
| stroke 24 | 19 % → 0 % | 90.3 px | 0.00 | 0.00 | 229 |
| stroke 25 | 25 % → 0 % | 186.5 px | 0.00 | 0.00 | 110 |
| stroke 26 | 32 % → 0 % | 345.9 px | 0.00 | 0.00 | 49 |
| stroke 27 | 31 % → 0 % | 222.9 px | 0.00 | 0.00 | 109 |
| stroke 28 | 29 % → 0 % | 154.3 px | 0.00 | 0.00 | 205 |
| stroke 29 | 32 % → 0 % | 243.4 px | 0.00 | 0.00 | 147 |
| stroke 30 | 42 % → 0 % | 381.4 px | 0.00 | 0.00 | 72 |
| stroke 31 | 37 % → 0 % | 415.9 px | 0.00 | 0.00 | 59 |
| stroke 32 | 33 % → 0 % | 137.4 px | 0.00 | 0.00 | 255 |
| stroke 33 | 36 % → 0 % | 136.8 px | 0.00 | 0.00 | 259 |
| stroke 34 | 37 % → 0 % | 144.3 px | 0.00 | 0.00 | 260 |
| stroke 35 | 19 % → 0 % | 137.8 px | 0.00 | 0.00 | 116 |
| stroke 36 | 13 % → 0 % | 150.4 px | 0.00 | 0.00 | 49 |
| stroke 37 | 15 % → 0 % | 138.8 px | 0.00 | 0.00 | 34 |
| stroke 38 | 20 % → 0 % | 213.4 px | 0.00 | 0.00 | 47 |
| stroke 39 | 23 % → 0 % | 216.3 px | 0.00 | 0.00 | 53 |
| stroke 40 | 2 % → 2 % | 33.1 px | 0.20 | 0.91 | 14 |
| stroke 41 | 2 % → 0 % | 24.5 px | 0.00 | 0.00 | 18 |
| stroke 42 | 13 % → 3 % | 38.1 px | 0.20 | 0.19 | 90 |
| stroke 43 | 12 % → 2 % | 77.9 px | 0.20 | 0.18 | 41 |
| stroke 44 | 24 % → 2 % | 64.7 px | 0.20 | 0.06 | 171 |
| stroke 45 | 30 % → 1 % | 94.0 px | 0.20 | 0.05 | 217 |
| stroke 46 | 41 % → 2 % | 369.6 px | 0.21 | 0.06 | 26 |
| stroke 47 | 40 % → 2 % | 354.0 px | 0.20 | 0.06 | 24 |
| stroke 48 | 12 % → 0 % | 41.5 px | 0.00 | 0.00 | 60 |
| stroke 49 | 12 % → 0 % | 171.4 px | 0.00 | 0.00 | 24 |
| stroke 50 | 23 % → 0 % | 111.0 px | 0.00 | 0.00 | 49 |
| stroke 51 | 26 % → 0 % | 172.0 px | 0.00 | 0.00 | 48 |
| stroke 52 | 29 % → 0 % | 236.0 px | 0.00 | 0.00 | 25 |
| stroke 53 | 7 % → 0 % | 45.4 px | 0.00 | 0.00 | 71 |
| stroke 54 | 12 % → 0 % | 74.1 px | 0.00 | 0.00 | 80 |
| stroke 55 | 17 % → 0 % | 101.7 px | 0.00 | 0.00 | 70 |
| stroke 56 | 4 % → 0 % | 47.1 px | 0.00 | 0.00 | 35 |
| stroke 57 | 10 % → 0 % | 56.6 px | 0.00 | 0.00 | 80 |
| stroke 58 | 20 % → 0 % | 234.0 px | 0.00 | 0.00 | 28 |
| stroke 59 | 15 % → 0 % | 74.0 px | 0.00 | 0.00 | 172 |
| stroke 60 | 21 % → 0 % | 97.9 px | 0.00 | 0.00 | 162 |
| stroke 61 | 27 % → 0 % | 123.8 px | 0.00 | 0.00 | 175 |
| stroke 62 | 10 % → 0 % | 67.0 px | 0.00 | 0.00 | 72 |
| stroke 63 | 15 % → 0 % | 68.7 px | 0.00 | 0.00 | 254 |
| stroke 64 | 29 % → 0 % | 85.8 px | 0.00 | 0.00 | 679 |
| stroke 65 | 56 % → 0 % | 122.7 px | 0.00 | 0.00 | 680 |
| stroke 66 | 87 % → 0 % | 182.9 px | 0.00 | 0.00 | 555 |
| stroke 67 | 83 % → 0 % | 248.3 px | 0.00 | 0.00 | 198 |
| stroke 68 | 2 % → 3 % | 22.7 px | 0.20 | 1.34 | 12 |

## Refs v3 · #07 HW blue L and zigzag — own sheet
own sheet 800 × 1065 · Gouache 1.00 + turpentine 30 % · 74 px · 36.5 s

![Refs v3 · #07 HW blue L and zigzag — own sheet](Refs-v3-07-HW-blue-L-and-zigzag-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 7 % → 2 % | 78.9 px | 0.39 | 0.34 | 83 |
| stroke 2 | 10 % → 0 % | 159.3 px | 0.41 | 0.05 | 61 |
| stroke 3 | 12 % → 0 % | 67.4 px | 0.00 | 0.00 | 178 |
| stroke 4 | 15 % → 0 % | 123.6 px | 0.00 | 0.00 | 191 |
| stroke 5 | 20 % → 0 % | 114.5 px | 0.00 | 0.00 | 188 |
| stroke 6 | 31 % → 1 % | 124.4 px | 0.41 | 0.03 | 591 |
| stroke 7 | 42 % → 0 % | 278.8 px | 0.00 | 0.00 | 112 |
| stroke 8 | 44 % → 1 % | 213.4 px | 0.40 | 0.03 | 420 |
| stroke 9 | 55 % → 0 % | 457.3 px | 0.00 | 0.00 | 73 |
| stroke 10 | 58 % → 2 % | 241.1 px | 0.40 | 0.03 | 415 |
| stroke 11 | 75 % → 3 % | 184.6 px | 0.40 | 0.04 | 635 |
| stroke 12 | 1 % → 4 % | 21.8 px | 0.39 | 3.10 | 9 |
| stroke 13 | 9 % → 0 % | 66.7 px | 0.00 | 0.00 | 91 |
| stroke 14 | 16 % → 0 % | 105.6 px | 0.00 | 0.00 | 213 |
| stroke 15 | 23 % → 0 % | 145.1 px | 0.00 | 0.00 | 135 |
| stroke 16 | 31 % → 0 % | 201.3 px | 0.00 | 0.00 | 159 |
| stroke 17 | 32 % → 0 % | 208.2 px | 0.00 | 0.00 | 135 |
| stroke 18 | 32 % → 1 % | 207.1 px | 0.38 | 0.02 | 139 |
| stroke 19 | 34 % → 3 % | 253.2 px | 0.39 | 0.08 | 107 |
| stroke 20 | 35 % → 3 % | 346.3 px | 0.39 | 0.09 | 58 |
| stroke 21 | 5 % → 3 % | 43.3 px | 0.39 | 0.67 | 46 |
| stroke 22 | 8 % → 2 % | 63.9 px | 0.40 | 0.23 | 68 |
| stroke 23 | 12 % → 0 % | 72.5 px | 0.41 | 0.02 | 95 |
| stroke 24 | 17 % → 0 % | 99.0 px | 0.00 | 0.00 | 107 |
| stroke 25 | 5 % → 0 % | 43.9 px | 0.00 | 0.00 | 73 |
| stroke 26 | 8 % → 0 % | 61.6 px | 0.00 | 0.00 | 98 |
| stroke 27 | 12 % → 0 % | 90.6 px | 0.00 | 0.00 | 132 |
| stroke 28 | 1 % → 0 % | 31.3 px | 0.00 | 0.00 | 8 |
| stroke 29 | 2 % → 0 % | 40.7 px | 0.00 | 0.00 | 22 |
| stroke 30 | 3 % → 0 % | 67.0 px | 0.00 | 0.00 | 16 |
| stroke 31 | 3 % → 0 % | 109.3 px | 0.00 | 0.00 | 11 |
| stroke 32 | 4 % → 0 % | 144.2 px | 0.00 | 0.00 | 9 |
| stroke 33 | 5 % → 0 % | 151.7 px | 0.00 | 0.00 | 12 |
| stroke 34 | 6 % → 0 % | 159.0 px | 0.00 | 0.00 | 10 |
| stroke 35 | 7 % → 0 % | 196.5 px | 0.00 | 0.00 | 23 |
| stroke 36 | 7 % → 0 % | 156.0 px | 0.00 | 0.00 | 24 |
| stroke 37 | 7 % → 0 % | 163.1 px | 0.00 | 0.00 | 19 |
| stroke 38 | 7 % → 0 % | 132.4 px | 0.00 | 0.00 | 24 |
| stroke 39 | 8 % → 0 % | 149.4 px | 0.00 | 0.00 | 21 |
| stroke 40 | 9 % → 0 % | 163.5 px | 0.00 | 0.00 | 38 |
| stroke 41 | 10 % → 0 % | 142.4 px | 0.00 | 0.00 | 31 |
| stroke 42 | 11 % → 0 % | 138.2 px | 0.00 | 0.00 | 36 |
| stroke 43 | 3 % → 0 % | 47.6 px | 0.00 | 0.00 | 22 |
| stroke 44 | 7 % → 0 % | 95.2 px | 0.00 | 0.00 | 27 |
| stroke 45 | 6 % → 0 % | 145.1 px | 0.00 | 0.00 | 26 |
| stroke 46 | 11 % → 0 % | 166.5 px | 0.00 | 0.00 | 25 |
| stroke 47 | 13 % → 0 % | 151.1 px | 0.00 | 0.00 | 42 |
| stroke 48 | 16 % → 0 % | 166.6 px | 0.00 | 0.00 | 54 |
| stroke 49 | 19 % → 0 % | 168.4 px | 0.00 | 0.00 | 62 |
| stroke 50 | 21 % → 0 % | 153.4 px | 0.00 | 0.00 | 85 |
| stroke 51 | 23 % → 0 % | 174.3 px | 0.00 | 0.00 | 67 |
| stroke 52 | 23 % → 0 % | 179.1 px | 0.00 | 0.00 | 68 |
| stroke 53 | 24 % → 0 % | 190.7 px | 0.00 | 0.00 | 62 |
| stroke 54 | 26 % → 0 % | 228.5 px | 0.00 | 0.00 | 54 |
| stroke 55 | 27 % → 0 % | 209.5 px | 0.00 | 0.00 | 57 |
| stroke 56 | 28 % → 0 % | 199.5 px | 0.00 | 0.00 | 74 |
| stroke 57 | 18 % → 0 % | 319.2 px | 0.00 | 0.00 | 33 |
| stroke 58 | 21 % → 0 % | 163.2 px | 0.00 | 0.00 | 84 |
| stroke 59 | 22 % → 0 % | 156.3 px | 0.00 | 0.00 | 114 |
| stroke 60 | 2 % → 0 % | 48.4 px | 0.00 | 0.00 | 23 |
| stroke 61 | 4 % → 0 % | 71.3 px | 0.00 | 0.00 | 29 |
| stroke 62 | 7 % → 0 % | 101.4 px | 0.00 | 0.00 | 44 |
| stroke 63 | 10 % → 0 % | 129.8 px | 0.00 | 0.00 | 49 |
| stroke 64 | 13 % → 0 % | 344.5 px | 0.00 | 0.00 | 14 |
| stroke 65 | 14 % → 0 % | 345.0 px | 0.00 | 0.00 | 22 |
| stroke 66 | 11 % → 0 % | 162.1 px | 0.00 | 0.00 | 39 |
| stroke 67 | 17 % → 0 % | 384.0 px | 0.00 | 0.00 | 39 |
| stroke 68 | 12 % → 0 % | 158.5 px | 0.00 | 0.00 | 78 |
| stroke 69 | 18 % → 0 % | 208.2 px | 0.00 | 0.00 | 85 |
| stroke 70 | 15 % → 0 % | 357.1 px | 0.00 | 0.00 | 29 |
| stroke 71 | 21 % → 0 % | 308.0 px | 0.00 | 0.00 | 47 |
| stroke 72 | 19 % → 0 % | 502.2 px | 0.00 | 0.00 | 22 |
| stroke 73 | 2 % → 0 % | 39.7 px | 0.00 | 0.00 | 26 |
| stroke 74 | 4 % → 0 % | 60.9 px | 0.00 | 0.00 | 52 |
| stroke 75 | 6 % → 0 % | 96.0 px | 0.00 | 0.00 | 49 |
| stroke 76 | 8 % → 0 % | 124.7 px | 0.00 | 0.00 | 45 |
| stroke 77 | 10 % → 0 % | 149.3 px | 0.00 | 0.00 | 63 |
| stroke 78 | 12 % → 0 % | 177.8 px | 0.00 | 0.00 | 67 |
| stroke 79 | 13 % → 0 % | 203.1 px | 0.00 | 0.00 | 63 |
| stroke 80 | 14 % → 0 % | 298.8 px | 0.00 | 0.00 | 28 |
| stroke 81 | 13 % → 0 % | 286.6 px | 0.00 | 0.00 | 30 |
| stroke 82 | 12 % → 0 % | 266.5 px | 0.00 | 0.00 | 30 |
| stroke 83 | 12 % → 0 % | 267.3 px | 0.00 | 0.00 | 43 |
| stroke 84 | 6 % → 0 % | 137.2 px | 0.37 | 0.01 | 19 |
| stroke 85 | 6 % → 1 % | 126.5 px | 0.39 | 0.17 | 38 |
| stroke 86 | 6 % → 2 % | 105.1 px | 0.39 | 0.33 | 38 |
| stroke 87 | 7 % → 2 % | 93.6 px | 0.39 | 0.28 | 43 |
| stroke 88 | 9 % → 2 % | 132.2 px | 0.39 | 0.22 | 48 |
| stroke 89 | 11 % → 2 % | 206.9 px | 0.39 | 0.19 | 22 |
| stroke 90 | 12 % → 2 % | 301.7 px | 0.39 | 0.17 | 26 |
| stroke 91 | 13 % → 2 % | 300.2 px | 0.39 | 0.16 | 29 |
| stroke 92 | 13 % → 2 % | 276.7 px | 0.39 | 0.17 | 32 |
| stroke 93 | 13 % → 2 % | 243.7 px | 0.39 | 0.16 | 40 |
| stroke 94 | 12 % → 2 % | 239.3 px | 0.39 | 0.18 | 23 |
| stroke 95 | 11 % → 2 % | 188.5 px | 0.39 | 0.18 | 40 |
| stroke 96 | 11 % → 2 % | 173.6 px | 0.39 | 0.18 | 41 |
| stroke 97 | 11 % → 2 % | 135.3 px | 0.39 | 0.15 | 58 |
| stroke 98 | 12 % → 0 % | 140.9 px | 0.41 | 0.02 | 82 |
| stroke 99 | 14 % → 0 % | 242.7 px | 0.00 | 0.00 | 30 |
| stroke 100 | 1 % → 0 % | 19.6 px | 0.00 | 0.00 | 44 |
| stroke 101 | 2 % → 0 % | 75.0 px | 0.00 | 0.00 | 20 |
| stroke 102 | 7 % → 3 % | 49.1 px | 0.40 | 0.37 | 151 |
| stroke 103 | 12 % → 4 % | 76.6 px | 0.40 | 0.35 | 151 |
| stroke 104 | 19 % → 5 % | 111.0 px | 0.40 | 0.25 | 127 |
| stroke 105 | 26 % → 5 % | 139.6 px | 0.40 | 0.20 | 140 |
| stroke 106 | 5 % → 0 % | 50.0 px | 0.00 | 0.00 | 25 |
| stroke 107 | 2 % → 3 % | 21.0 px | 0.39 | 1.72 | 21 |
| stroke 108 | 5 % → 8 % | 18.4 px | 0.40 | 1.49 | 54 |

Numbers say: wet paint spreads well beyond the stroke.

## Refs v3 · #08 HW lilac crown basket — own sheet
own sheet 800 × 1150 · Gouache 1.00 + turpentine 30 % · 26 px · 98.3 s

![Refs v3 · #08 HW lilac crown basket — own sheet](Refs-v3-08-HW-lilac-crown-basket-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 14 % → 12 % | 27.4 px | 0.34 | 0.86 | 29 |
| stroke 2 | 24 % → 11 % | 30.3 px | 0.34 | 0.46 | 85 |
| stroke 3 | 31 % → 8 % | 40.0 px | 0.34 | 0.26 | 119 |
| stroke 4 | 8 % → 0 % | 26.8 px | 0.00 | 0.00 | 28 |
| stroke 5 | 12 % → 0 % | 39.0 px | 0.00 | 0.00 | 41 |
| stroke 6 | 17 % → 0 % | 55.2 px | 0.00 | 0.00 | 42 |
| stroke 7 | 25 % → 0 % | 83.5 px | 0.00 | 0.00 | 33 |
| stroke 8 | 33 % → 0 % | 221.1 px | 0.00 | 0.00 | 9 |
| stroke 9 | 26 % → 0 % | 82.2 px | 0.00 | 0.00 | 47 |
| stroke 10 | 26 % → 0 % | 89.1 px | 0.00 | 0.00 | 29 |
| stroke 11 | 20 % → 0 % | 86.1 px | 0.00 | 0.00 | 18 |
| stroke 12 | 8 % → 0 % | 25.9 px | 0.21 | 0.02 | 13 |
| stroke 13 | 12 % → 0 % | 52.6 px | 0.00 | 0.00 | 12 |
| stroke 14 | 10 % → 0 % | 28.0 px | 0.00 | 0.00 | 16 |
| stroke 15 | 7 % → 29 % | 24.3 px | 0.30 | 3.91 | 16 |
| stroke 16 | 21 % → 6 % | 43.1 px | 0.30 | 0.27 | 25 |
| stroke 17 | 29 % → 13 % | 34.5 px | 0.30 | 0.46 | 135 |
| stroke 18 | 49 % → 11 % | 105.3 px | 0.31 | 0.22 | 12 |
| stroke 19 | 14 % → 0 % | 25.9 px | 0.00 | 0.00 | 68 |
| stroke 20 | 21 % → 0 % | 34.2 px | 0.00 | 0.00 | 115 |
| stroke 21 | 35 % → 0 % | 58.0 px | 0.00 | 0.00 | 103 |
| stroke 22 | 8 % → 0 % | 26.7 px | 0.00 | 0.00 | 20 |
| stroke 23 | 10 % → 0 % | 33.2 px | 0.00 | 0.00 | 70 |
| stroke 24 | 12 % → 0 % | 58.5 px | 0.00 | 0.00 | 10 |
| stroke 25 | 26 % → 0 % | 99.9 px | 0.00 | 0.00 | 20 |
| stroke 26 | 11 % → 0 % | 55.0 px | 0.00 | 0.00 | 12 |
| stroke 27 | 15 % → 0 % | 85.1 px | 0.00 | 0.00 | 5 |
| stroke 28 | 11 % → 0 % | 78.0 px | 0.00 | 0.00 | 5 |
| stroke 29 | 5 % → 0 % | 28.5 px | 0.00 | 0.00 | 9 |
| stroke 30 | 11 % → 0 % | 39.5 px | 0.00 | 0.00 | 16 |
| stroke 31 | 16 % → 0 % | 51.7 px | 0.00 | 0.00 | 23 |
| stroke 32 | 23 % → 0 % | 89.4 px | 0.00 | 0.00 | 13 |
| stroke 33 | 29 % → 0 % | 119.3 px | 0.00 | 0.00 | 15 |
| stroke 34 | 19 % → 0 % | 56.4 px | 0.00 | 0.00 | 20 |
| stroke 35 | 27 % → 0 % | 101.0 px | 0.00 | 0.00 | 20 |
| stroke 36 | 28 % → 0 % | 72.0 px | 0.00 | 0.00 | 34 |
| stroke 37 | 27 % → 0 % | 53.2 px | 0.00 | 0.00 | 82 |
| stroke 38 | 34 % → 0 % | 59.5 px | 0.00 | 0.00 | 95 |
| stroke 39 | 45 % → 0 % | 72.0 px | 0.00 | 0.00 | 97 |
| stroke 40 | 63 % → 0 % | 101.2 px | 0.00 | 0.00 | 82 |
| stroke 41 | 59 % → 0 % | 279.5 px | 0.00 | 0.00 | 5 |
| stroke 42 | 82 % → 0 % | 165.8 px | 0.00 | 0.00 | 21 |
| stroke 43 | 4 % → 0 % | 29.9 px | 0.00 | 0.00 | 14 |
| stroke 44 | 8 % → 0 % | 42.7 px | 0.00 | 0.00 | 13 |
| stroke 45 | 12 % → 0 % | 67.4 px | 0.00 | 0.00 | 6 |
| stroke 46 | 4 % → 0 % | 25.5 px | 0.00 | 0.00 | 4 |
| stroke 47 | 8 % → 0 % | 36.9 px | 0.00 | 0.00 | 7 |
| stroke 48 | 23 % → 0 % | 37.2 px | 0.00 | 0.00 | 25 |
| stroke 49 | 39 % → 0 % | 53.8 px | 0.00 | 0.00 | 31 |
| stroke 50 | 8 % → 0 % | 15.3 px | 0.00 | 0.00 | 22 |
| stroke 51 | 9 % → 0 % | 16.3 px | 0.00 | 0.00 | 7 |
| stroke 52 | 6 % → 0 % | 20.0 px | 0.00 | 0.00 | 11 |
| stroke 53 | 4 % → 32 % | 15.5 px | 0.31 | 7.20 | 3 |
| stroke 54 | 7 % → 0 % | 20.1 px | 0.33 | 0.04 | 23 |
| stroke 55 | 6 % → 1 % | 25.5 px | 0.29 | 0.08 | 15 |
| stroke 56 | 13 % → 0 % | 67.6 px | 0.29 | 0.00 | 9 |
| stroke 57 | 7 % → 0 % | 18.0 px | 0.00 | 0.00 | 8 |
| stroke 58 | 15 % → 0 % | 40.7 px | 0.00 | 0.00 | 18 |
| stroke 59 | 20 % → 0 % | 38.7 px | 0.00 | 0.00 | 23 |
| stroke 60 | 12 % → 0 % | 29.9 px | 0.00 | 0.00 | 39 |
| stroke 61 | 8 % → 0 % | 26.6 px | 0.00 | 0.00 | 25 |
| stroke 62 | 8 % → 0 % | 29.1 px | 0.00 | 0.00 | 29 |
| stroke 63 | 12 % → 0 % | 53.5 px | 0.00 | 0.00 | 20 |
| stroke 64 | 17 % → 0 % | 40.2 px | 0.00 | 0.00 | 23 |
| stroke 65 | 7 % → 0 % | 25.7 px | 0.00 | 0.00 | 14 |
| stroke 66 | 14 % → 0 % | 46.8 px | 0.00 | 0.00 | 16 |
| stroke 67 | 18 % → 0 % | 60.4 px | 0.00 | 0.00 | 34 |
| stroke 68 | 13 % → 0 % | 29.4 px | 0.00 | 0.00 | 37 |
| stroke 69 | 4 % → 4 % | 22.3 px | 0.34 | 1.20 | 6 |
| stroke 70 | 10 % → 13 % | 24.6 px | 0.34 | 1.28 | 31 |
| stroke 71 | 17 % → 10 % | 30.3 px | 0.34 | 0.59 | 78 |
| stroke 72 | 24 % → 10 % | 44.8 px | 0.34 | 0.41 | 72 |
| stroke 73 | 32 % → 16 % | 267.8 px | 0.34 | 0.51 | 3 |
| stroke 74 | 34 % → 4 % | 127.9 px | 0.33 | 0.11 | 14 |
| stroke 75 | 31 % → 0 % | 86.9 px | 0.33 | 0.01 | 28 |
| stroke 76 | 24 % → 0 % | 88.1 px | 0.00 | 0.00 | 13 |
| stroke 77 | 23 % → 0 % | 72.7 px | 0.00 | 0.00 | 23 |
| stroke 78 | 23 % → 0 % | 68.6 px | 0.00 | 0.00 | 22 |
| stroke 79 | 24 % → 0 % | 124.5 px | 0.00 | 0.00 | 8 |
| stroke 80 | 26 % → 0 % | 146.9 px | 0.00 | 0.00 | 6 |
| stroke 81 | 25 % → 0 % | 103.0 px | 0.00 | 0.00 | 13 |
| stroke 82 | 24 % → 0 % | 128.0 px | 0.00 | 0.00 | 11 |
| stroke 83 | 22 % → 0 % | 116.4 px | 0.00 | 0.00 | 9 |
| stroke 84 | 20 % → 0 % | 142.4 px | 0.00 | 0.00 | 4 |
| stroke 85 | 4 % → 0 % | 22.9 px | 0.00 | 0.00 | 5 |
| stroke 86 | 9 % → 0 % | 27.9 px | 0.00 | 0.00 | 26 |
| stroke 87 | 13 % → 0 % | 58.5 px | 0.00 | 0.00 | 9 |
| stroke 88 | 3 % → 0 % | 18.4 px | 0.00 | 0.00 | 9 |
| stroke 89 | 6 % → 0 % | 29.6 px | 0.00 | 0.00 | 12 |
| stroke 90 | 11 % → 0 % | 46.1 px | 0.00 | 0.00 | 27 |
| stroke 91 | 14 % → 0 % | 58.4 px | 0.00 | 0.00 | 27 |
| stroke 92 | 18 % → 0 % | 77.4 px | 0.00 | 0.00 | 23 |
| stroke 93 | 17 % → 0 % | 77.5 px | 0.00 | 0.00 | 23 |
| stroke 94 | 6 % → 13 % | 34.8 px | 0.29 | 2.29 | 4 |
| stroke 95 | 20 % → 4 % | 60.3 px | 0.29 | 0.18 | 36 |
| stroke 96 | 26 % → 0 % | 94.0 px | 0.28 | 0.01 | 26 |
| stroke 97 | 7 % → 0 % | 26.9 px | 0.00 | 0.00 | 12 |
| stroke 98 | 10 % → 0 % | 31.7 px | 0.00 | 0.00 | 23 |
| stroke 99 | 15 % → 0 % | 99.8 px | 0.00 | 0.00 | 9 |
| stroke 100 | 4 % → 0 % | 23.2 px | 0.00 | 0.00 | 8 |
| stroke 101 | 8 % → 0 % | 28.2 px | 0.00 | 0.00 | 55 |
| stroke 102 | 15 % → 0 % | 67.7 px | 0.00 | 0.00 | 18 |
| stroke 103 | 23 % → 0 % | 83.9 px | 0.00 | 0.00 | 22 |
| stroke 104 | 28 % → 0 % | 266.1 px | 0.00 | 0.00 | 5 |
| stroke 105 | 4 % → 0 % | 25.4 px | 0.00 | 0.00 | 14 |
| stroke 106 | 11 % → 0 % | 22.2 px | 0.00 | 0.00 | 49 |
| stroke 107 | 18 % → 0 % | 30.8 px | 0.00 | 0.00 | 113 |
| stroke 108 | 23 % → 0 % | 36.1 px | 0.00 | 0.00 | 196 |
| stroke 109 | 18 % → 0 % | 75.3 px | 0.00 | 0.00 | 22 |
| stroke 110 | 36 % → 0 % | 185.4 px | 0.00 | 0.00 | 33 |
| stroke 111 | 21 % → 0 % | 43.1 px | 0.00 | 0.00 | 60 |
| stroke 112 | 28 % → 0 % | 150.9 px | 0.00 | 0.00 | 6 |
| stroke 113 | 18 % → 0 % | 48.4 px | 0.00 | 0.00 | 40 |
| stroke 114 | 12 % → 0 % | 87.7 px | 0.00 | 0.00 | 14 |
| stroke 115 | 22 % → 0 % | 56.5 px | 0.00 | 0.00 | 37 |
| stroke 116 | 13 % → 0 % | 90.0 px | 0.00 | 0.00 | 10 |
| stroke 117 | 27 % → 0 % | 54.9 px | 0.00 | 0.00 | 65 |
| stroke 118 | 15 % → 0 % | 108.5 px | 0.00 | 0.00 | 4 |
| stroke 119 | 41 % → 0 % | 111.0 px | 0.00 | 0.00 | 29 |
| stroke 120 | 28 % → 0 % | 85.0 px | 0.00 | 0.00 | 31 |
| stroke 121 | 25 % → 0 % | 94.8 px | 0.00 | 0.00 | 17 |
| stroke 122 | 9 % → 0 % | 56.2 px | 0.00 | 0.00 | 9 |
| stroke 123 | 9 % → 0 % | 49.0 px | 0.00 | 0.00 | 16 |
| stroke 124 | 11 % → 0 % | 59.7 px | 0.00 | 0.00 | 7 |
| stroke 125 | 16 % → 0 % | 100.5 px | 0.00 | 0.00 | 8 |
| stroke 126 | 17 % → 0 % | 89.4 px | 0.00 | 0.00 | 9 |
| stroke 127 | 21 % → 0 % | 141.1 px | 0.00 | 0.00 | 7 |
| stroke 128 | 18 % → 0 % | 92.3 px | 0.00 | 0.00 | 11 |
| stroke 129 | 18 % → 0 % | 125.1 px | 0.00 | 0.00 | 7 |
| stroke 130 | 18 % → 0 % | 94.8 px | 0.00 | 0.00 | 5 |
| stroke 131 | 20 % → 0 % | 132.9 px | 0.00 | 0.00 | 8 |
| stroke 132 | 19 % → 0 % | 98.9 px | 0.00 | 0.00 | 6 |
| stroke 133 | 20 % → 0 % | 128.3 px | 0.00 | 0.00 | 3 |
| stroke 134 | 20 % → 0 % | 125.1 px | 0.00 | 0.00 | 7 |
| stroke 135 | 24 % → 0 % | 105.2 px | 0.00 | 0.00 | 12 |
| stroke 136 | 23 % → 0 % | 123.7 px | 0.00 | 0.00 | 9 |
| stroke 137 | 6 % → 0 % | 26.4 px | 0.00 | 0.00 | 19 |
| stroke 138 | 9 % → 0 % | 40.8 px | 0.00 | 0.00 | 13 |
| stroke 139 | 13 % → 0 % | 61.8 px | 0.00 | 0.00 | 4 |
| stroke 140 | 8 % → 0 % | 38.5 px | 0.00 | 0.00 | 8 |
| stroke 141 | 7 % → 15 % | 22.1 px | 0.29 | 2.13 | 28 |
| stroke 142 | 11 % → 14 % | 35.3 px | 0.29 | 1.28 | 33 |
| stroke 143 | 20 % → 20 % | 116.0 px | 0.29 | 1.00 | 11 |
| stroke 144 | 23 % → 20 % | 146.9 px | 0.29 | 0.86 | 6 |
| stroke 145 | 5 % → 0 % | 28.1 px | 0.00 | 0.00 | 9 |
| stroke 146 | 7 % → 0 % | 26.5 px | 0.00 | 0.00 | 11 |
| stroke 147 | 3 % → 0 % | 20.9 px | 0.00 | 0.00 | 6 |
| stroke 148 | 5 % → 3 % | 22.1 px | 0.32 | 0.55 | 8 |
| stroke 149 | 7 % → 0 % | 24.0 px | 0.00 | 0.00 | 17 |
| stroke 150 | 14 % → 0 % | 39.4 px | 0.00 | 0.00 | 28 |
| stroke 151 | 8 % → 22 % | 22.1 px | 0.30 | 2.63 | 16 |
| stroke 152 | 13 % → 3 % | 36.5 px | 0.30 | 0.21 | 39 |
| stroke 153 | 7 % → 0 % | 25.2 px | 0.00 | 0.00 | 22 |
| stroke 154 | 7 % → 0 % | 23.5 px | 0.00 | 0.00 | 11 |
| stroke 155 | 12 % → 0 % | 45.5 px | 0.00 | 0.00 | 18 |
| stroke 156 | 5 % → 0 % | 24.1 px | 0.00 | 0.00 | 6 |
| stroke 157 | 18 % → 0 % | 45.4 px | 0.00 | 0.00 | 44 |
| stroke 158 | 26 % → 0 % | 60.6 px | 0.00 | 0.00 | 83 |
| stroke 159 | 31 % → 0 % | 74.4 px | 0.00 | 0.00 | 96 |
| stroke 160 | 35 % → 0 % | 98.6 px | 0.00 | 0.00 | 114 |
| stroke 161 | 29 % → 0 % | 111.2 px | 0.00 | 0.00 | 35 |
| stroke 162 | 28 % → 0 % | 101.5 px | 0.00 | 0.00 | 56 |
| stroke 163 | 29 % → 0 % | 106.6 px | 0.00 | 0.00 | 49 |
| stroke 164 | 32 % → 0 % | 126.7 px | 0.00 | 0.00 | 34 |
| stroke 165 | 15 % → 0 % | 48.0 px | 0.00 | 0.00 | 22 |
| stroke 166 | 25 % → 0 % | 95.6 px | 0.00 | 0.00 | 38 |
| stroke 167 | 24 % → 1 % | 57.4 px | 0.31 | 0.03 | 64 |
| stroke 168 | 25 % → 0 % | 82.3 px | 0.00 | 0.00 | 80 |
| stroke 169 | 30 % → 7 % | 72.9 px | 0.32 | 0.23 | 117 |
| stroke 170 | 32 % → 0 % | 101.6 px | 0.00 | 0.00 | 90 |
| stroke 171 | 33 % → 8 % | 88.5 px | 0.32 | 0.24 | 147 |
| stroke 172 | 35 % → 0 % | 148.0 px | 0.00 | 0.00 | 43 |
| stroke 173 | 31 % → 10 % | 93.8 px | 0.32 | 0.33 | 230 |
| stroke 174 | 29 % → 1 % | 93.0 px | 0.32 | 0.02 | 130 |
| stroke 175 | 23 % → 5 % | 80.7 px | 0.33 | 0.24 | 281 |
| stroke 176 | 35 % → 8 % | 110.1 px | 0.33 | 0.22 | 167 |
| stroke 177 | 49 % → 4 % | 159.9 px | 0.34 | 0.07 | 80 |
| stroke 178 | 46 % → 0 % | 175.3 px | 0.35 | 0.01 | 52 |
| stroke 179 | 17 % → 1 % | 45.8 px | 0.33 | 0.07 | 51 |
| stroke 180 | 32 % → 0 % | 75.9 px | 0.00 | 0.00 | 87 |
| stroke 181 | 46 % → 0 % | 119.6 px | 0.00 | 0.00 | 40 |
| stroke 182 | 16 % → 1 % | 49.9 px | 0.34 | 0.08 | 54 |
| stroke 183 | 27 % → 6 % | 65.3 px | 0.34 | 0.22 | 103 |
| stroke 184 | 37 % → 0 % | 117.5 px | 0.33 | 0.01 | 59 |
| stroke 185 | 7 % → 18 % | 28.3 px | 0.31 | 2.63 | 16 |
| stroke 186 | 13 % → 14 % | 49.1 px | 0.32 | 1.06 | 19 |
| stroke 187 | 20 % → 13 % | 92.7 px | 0.32 | 0.64 | 18 |
| stroke 188 | 5 % → 0 % | 29.1 px | 0.00 | 0.00 | 5 |
| stroke 189 | 9 % → 0 % | 38.4 px | 0.00 | 0.00 | 26 |
| stroke 190 | 5 % → 1 % | 35.7 px | 0.31 | 0.23 | 16 |
| stroke 191 | 12 % → 6 % | 37.7 px | 0.32 | 0.52 | 59 |
| stroke 192 | 14 % → 12 % | 44.8 px | 0.33 | 0.82 | 47 |
| stroke 193 | 29 % → 8 % | 123.2 px | 0.32 | 0.28 | 19 |
| stroke 194 | 33 % → 11 % | 227.6 px | 0.32 | 0.32 | 5 |
| stroke 195 | 10 % → 0 % | 28.4 px | 0.00 | 0.00 | 52 |
| stroke 196 | 16 % → 0 % | 42.5 px | 0.00 | 0.00 | 50 |
| stroke 197 | 31 % → 0 % | 166.8 px | 0.00 | 0.00 | 10 |
| stroke 198 | 18 % → 0 % | 54.1 px | 0.00 | 0.00 | 34 |
| stroke 199 | 16 % → 11 % | 40.7 px | 0.30 | 0.67 | 86 |
| stroke 200 | 10 % → 0 % | 26.9 px | 0.00 | 0.00 | 104 |
| stroke 201 | 23 % → 12 % | 57.2 px | 0.30 | 0.53 | 147 |
| stroke 202 | 15 % → 0 % | 37.6 px | 0.00 | 0.00 | 61 |
| stroke 203 | 39 % → 0 % | 117.5 px | 0.00 | 0.00 | 44 |
| stroke 204 | 34 % → 0 % | 172.6 px | 0.00 | 0.00 | 9 |
| stroke 205 | 19 % → 0 % | 75.0 px | 0.00 | 0.00 | 28 |
| stroke 206 | 36 % → 0 % | 112.9 px | 0.00 | 0.00 | 46 |
| stroke 207 | 27 % → 23 % | 113.6 px | 0.30 | 0.86 | 16 |
| stroke 208 | 22 % → 0 % | 98.4 px | 0.00 | 0.00 | 11 |
| stroke 209 | 31 % → 0 % | 98.6 px | 0.00 | 0.00 | 43 |
| stroke 210 | 30 % → 26 % | 223.6 px | 0.30 | 0.87 | 3 |
| stroke 211 | 24 % → 0 % | 184.1 px | 0.00 | 0.00 | 3 |
| stroke 212 | 20 % → 0 % | 111.9 px | 0.00 | 0.00 | 12 |
| stroke 213 | 15 % → 19 % | 118.6 px | 0.29 | 1.27 | 11 |
| stroke 214 | 23 % → 0 % | 73.1 px | 0.00 | 0.00 | 50 |
| stroke 215 | 20 % → 0 % | 66.0 px | 0.00 | 0.00 | 37 |
| stroke 216 | 13 % → 13 % | 51.9 px | 0.29 | 0.95 | 19 |
| stroke 217 | 27 % → 0 % | 65.6 px | 0.00 | 0.00 | 117 |
| stroke 218 | 18 % → 8 % | 52.1 px | 0.29 | 0.44 | 67 |
| stroke 219 | 35 % → 0 % | 91.6 px | 0.00 | 0.00 | 77 |
| stroke 220 | 32 % → 4 % | 79.5 px | 0.29 | 0.12 | 178 |
| stroke 221 | 44 % → 0 % | 153.9 px | 0.00 | 0.00 | 39 |
| stroke 222 | 36 % → 2 % | 139.5 px | 0.29 | 0.05 | 30 |
| stroke 223 | 34 % → 6 % | 195.8 px | 0.29 | 0.17 | 15 |
| stroke 224 | 38 % → 0 % | 153.5 px | 0.00 | 0.00 | 32 |
| stroke 225 | 40 % → 1 % | 119.1 px | 0.29 | 0.03 | 38 |
| stroke 226 | 39 % → 0 % | 96.9 px | 0.28 | 0.00 | 114 |
| stroke 227 | 46 % → 0 % | 199.4 px | 0.00 | 0.00 | 36 |
| stroke 228 | 5 % → 0 % | 30.4 px | 0.00 | 0.00 | 13 |
| stroke 229 | 10 % → 0 % | 45.2 px | 0.00 | 0.00 | 14 |
| stroke 230 | 15 % → 0 % | 56.2 px | 0.00 | 0.00 | 35 |
| stroke 231 | 20 % → 0 % | 78.0 px | 0.00 | 0.00 | 25 |
| stroke 232 | 4 % → 0 % | 27.9 px | 0.00 | 0.00 | 8 |
| stroke 233 | 9 % → 7 % | 39.0 px | 0.30 | 0.70 | 14 |
| stroke 234 | 13 % → 0 % | 103.3 px | 0.00 | 0.00 | 5 |
| stroke 235 | 14 % → 4 % | 45.4 px | 0.30 | 0.29 | 47 |
| stroke 236 | 5 % → 0 % | 34.7 px | 0.00 | 0.00 | 16 |
| stroke 237 | 25 % → 4 % | 91.0 px | 0.30 | 0.18 | 24 |
| stroke 238 | 23 % → 0 % | 71.1 px | 0.00 | 0.00 | 62 |
| stroke 239 | 35 % → 6 % | 148.0 px | 0.30 | 0.18 | 34 |
| stroke 240 | 36 % → 0 % | 154.5 px | 0.00 | 0.00 | 21 |
| stroke 241 | 40 % → 0 % | 145.5 px | 0.00 | 0.00 | 27 |
| stroke 242 | 39 % → 0 % | 139.5 px | 0.00 | 0.00 | 37 |
| stroke 243 | 4 % → 0 % | 29.5 px | 0.00 | 0.00 | 4 |
| stroke 244 | 10 % → 0 % | 29.1 px | 0.00 | 0.00 | 82 |
| stroke 245 | 21 % → 0 % | 85.1 px | 0.00 | 0.00 | 26 |
| stroke 246 | 25 % → 0 % | 119.2 px | 0.00 | 0.00 | 17 |
| stroke 247 | 14 % → 0 % | 27.1 px | 0.00 | 0.00 | 96 |
| stroke 248 | 12 % → 0 % | 39.8 px | 0.00 | 0.00 | 21 |
| stroke 249 | 22 % → 0 % | 37.2 px | 0.00 | 0.00 | 198 |
| stroke 250 | 29 % → 0 % | 50.4 px | 0.00 | 0.00 | 204 |
| stroke 251 | 33 % → 0 % | 87.2 px | 0.00 | 0.00 | 52 |
| stroke 252 | 45 % → 0 % | 309.4 px | 0.00 | 0.00 | 6 |
| stroke 253 | 33 % → 0 % | 112.6 px | 0.00 | 0.00 | 55 |
| stroke 254 | 26 % → 0 % | 140.2 px | 0.00 | 0.00 | 14 |
| stroke 255 | 44 % → 0 % | 239.5 px | 0.00 | 0.00 | 10 |
| stroke 256 | 39 % → 0 % | 282.1 px | 0.00 | 0.00 | 17 |
| stroke 257 | 31 % → 0 % | 116.4 px | 0.00 | 0.00 | 32 |
| stroke 258 | 37 % → 0 % | 136.3 px | 0.00 | 0.00 | 40 |
| stroke 259 | 34 % → 0 % | 164.1 px | 0.00 | 0.00 | 20 |
| stroke 260 | 34 % → 0 % | 128.0 px | 0.00 | 0.00 | 15 |
| stroke 261 | 36 % → 0 % | 129.8 px | 0.00 | 0.00 | 20 |
| stroke 262 | 21 % → 0 % | 85.5 px | 0.00 | 0.00 | 19 |
| stroke 263 | 26 % → 0 % | 174.5 px | 0.00 | 0.00 | 4 |
| stroke 264 | 47 % → 0 % | 140.2 px | 0.00 | 0.00 | 51 |
| stroke 265 | 22 % → 0 % | 62.1 px | 0.00 | 0.00 | 37 |
| stroke 266 | 33 % → 0 % | 107.4 px | 0.00 | 0.00 | 50 |
| stroke 267 | 27 % → 0 % | 165.2 px | 0.00 | 0.00 | 13 |
| stroke 268 | 33 % → 0 % | 99.9 px | 0.00 | 0.00 | 55 |
| stroke 269 | 35 % → 0 % | 128.5 px | 0.00 | 0.00 | 22 |
| stroke 270 | 12 % → 19 % | 21.6 px | 0.31 | 1.65 | 13 |
| stroke 271 | 7 % → 0 % | 16.8 px | 0.00 | 0.00 | 7 |
| stroke 272 | 5 % → 0 % | 28.9 px | 0.00 | 0.00 | 7 |
| stroke 273 | 9 % → 3 % | 25.9 px | 0.33 | 0.31 | 30 |
| stroke 274 | 9 % → 7 % | 45.7 px | 0.34 | 0.79 | 6 |
| stroke 275 | 6 % → 14 % | 28.6 px | 0.34 | 2.39 | 16 |
| stroke 276 | 8 % → 0 % | 30.1 px | 0.00 | 0.00 | 22 |
| stroke 277 | 5 % → 15 % | 28.0 px | 0.35 | 3.20 | 4 |
| stroke 278 | 5 % → 3 % | 24.5 px | 0.34 | 0.61 | 8 |
| stroke 279 | 6 % → 0 % | 23.4 px | 0.00 | 0.00 | 16 |
| stroke 280 | 9 % → 0 % | 31.9 px | 0.00 | 0.00 | 15 |
| stroke 281 | 4 % → 0 % | 23.7 px | 0.00 | 0.00 | 15 |
| stroke 282 | 13 % → 0 % | 47.8 px | 0.00 | 0.00 | 29 |
| stroke 283 | 4 % → 0 % | 24.2 px | 0.00 | 0.00 | 10 |
| stroke 284 | 16 % → 0 % | 45.4 px | 0.00 | 0.00 | 33 |
| stroke 285 | 23 % → 0 % | 88.3 px | 0.00 | 0.00 | 15 |
| stroke 286 | 16 % → 0 % | 48.3 px | 0.00 | 0.00 | 86 |
| stroke 287 | 13 % → 0 % | 55.0 px | 0.00 | 0.00 | 42 |
| stroke 288 | 24 % → 0 % | 47.2 px | 0.00 | 0.00 | 184 |
| stroke 289 | 35 % → 0 % | 133.0 px | 0.00 | 0.00 | 35 |
| stroke 290 | 21 % → 0 % | 77.1 px | 0.00 | 0.00 | 36 |
| stroke 291 | 15 % → 0 % | 48.2 px | 0.00 | 0.00 | 44 |
| stroke 292 | 42 % → 0 % | 74.1 px | 0.00 | 0.00 | 230 |
| stroke 293 | 27 % → 0 % | 121.6 px | 0.00 | 0.00 | 27 |
| stroke 294 | 53 % → 0 % | 156.6 px | 0.00 | 0.00 | 56 |
| stroke 295 | 27 % → 0 % | 96.3 px | 0.00 | 0.00 | 34 |
| stroke 296 | 48 % → 1 % | 67.7 px | 0.29 | 0.03 | 422 |
| stroke 297 | 48 % → 0 % | 79.1 px | 0.00 | 0.00 | 165 |
| stroke 298 | 50 % → 0 % | 183.5 px | 0.00 | 0.00 | 41 |
| stroke 299 | 53 % → 0 % | 143.1 px | 0.00 | 0.00 | 46 |
| stroke 300 | 45 % → 0 % | 89.7 px | 0.00 | 0.00 | 69 |
| stroke 301 | 43 % → 0 % | 81.3 px | 0.00 | 0.00 | 90 |
| stroke 302 | 25 % → 0 % | 56.1 px | 0.00 | 0.00 | 87 |
| stroke 303 | 48 % → 0 % | 74.8 px | 0.00 | 0.00 | 211 |
| stroke 304 | 17 % → 0 % | 52.0 px | 0.00 | 0.00 | 29 |
| stroke 305 | 51 % → 0 % | 75.1 px | 0.00 | 0.00 | 347 |
| stroke 306 | 55 % → 0 % | 94.9 px | 0.00 | 0.00 | 184 |
| stroke 307 | 44 % → 0 % | 95.6 px | 0.00 | 0.00 | 109 |
| stroke 308 | 52 % → 0 % | 98.1 px | 0.00 | 0.00 | 118 |
| stroke 309 | 46 % → 0 % | 119.6 px | 0.00 | 0.00 | 62 |
| stroke 310 | 46 % → 0 % | 76.0 px | 0.00 | 0.00 | 168 |
| stroke 311 | 48 % → 0 % | 77.4 px | 0.00 | 0.00 | 227 |
| stroke 312 | 30 % → 0 % | 67.0 px | 0.00 | 0.00 | 382 |
| stroke 313 | 10 % → 16 % | 29.2 px | 0.31 | 1.55 | 30 |
| stroke 314 | 12 % → 13 % | 24.8 px | 0.34 | 1.12 | 47 |
| stroke 315 | 7 % → 9 % | 39.6 px | 0.32 | 1.41 | 15 |
| stroke 316 | 8 % → 13 % | 31.5 px | 0.32 | 1.63 | 44 |
| stroke 317 | 9 % → 15 % | 37.8 px | 0.35 | 1.68 | 30 |
| stroke 318 | 12 % → 14 % | 27.2 px | 0.30 | 1.19 | 73 |

Numbers say: wet paint spreads well beyond the stroke.

## Refs v3 · #09 HW white loops — own sheet
own sheet 800 × 640 · Gouache 1.00 + turpentine 30 % · 74 px · 23.2 s

![Refs v3 · #09 HW white loops — own sheet](Refs-v3-09-HW-white-loops-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 14 % → 0 % | 61.6 px | 0.00 | 0.00 | 191 |
| stroke 2 | 10 % → 0 % | 72.0 px | 0.00 | 0.00 | 94 |
| stroke 3 | 24 % → 0 % | 91.9 px | 0.00 | 0.00 | 396 |
| stroke 4 | 21 % → 0 % | 109.3 px | 0.00 | 0.00 | 233 |
| stroke 5 | 31 % → 0 % | 183.7 px | 0.00 | 0.00 | 215 |
| stroke 6 | 37 % → 0 % | 305.9 px | 0.00 | 0.00 | 92 |
| stroke 7 | 41 % → 0 % | 137.0 px | 0.00 | 0.00 | 677 |
| stroke 8 | 49 % → 0 % | 167.3 px | 0.00 | 0.00 | 747 |
| stroke 9 | 54 % → 0 % | 185.7 px | 0.00 | 0.00 | 733 |
| stroke 10 | 57 % → 0 % | 194.1 px | 0.00 | 0.00 | 718 |
| stroke 11 | 57 % → 0 % | 195.1 px | 0.00 | 0.00 | 825 |
| stroke 12 | 56 % → 0 % | 195.9 px | 0.00 | 0.00 | 678 |
| stroke 13 | 56 % → 1 % | 197.7 px | 0.74 | 0.02 | 657 |
| stroke 14 | 55 % → 6 % | 202.7 px | 0.74 | 0.10 | 689 |
| stroke 15 | 54 % → 10 % | 460.0 px | 0.74 | 0.18 | 145 |
| stroke 16 | 49 % → 16 % | 362.7 px | 0.74 | 0.33 | 144 |
| stroke 17 | 53 % → 11 % | 429.5 px | 0.74 | 0.20 | 135 |
| stroke 18 | 2 % → 0 % | 15.7 px | 0.00 | 0.00 | 10 |
| stroke 19 | 2 % → 0 % | 19.8 px | 0.00 | 0.00 | 18 |
| stroke 20 | 3 % → 0 % | 29.0 px | 0.00 | 0.00 | 22 |
| stroke 21 | 4 % → 0 % | 40.0 px | 0.00 | 0.00 | 32 |
| stroke 22 | 5 % → 0 % | 49.9 px | 0.00 | 0.00 | 35 |
| stroke 23 | 6 % → 0 % | 58.6 px | 0.00 | 0.00 | 28 |
| stroke 24 | 7 % → 0 % | 83.2 px | 0.00 | 0.00 | 39 |
| stroke 25 | 8 % → 0 % | 116.9 px | 0.00 | 0.00 | 26 |
| stroke 26 | 1 % → 19 % | 21.0 px | 0.74 | 28.38 | 6 |
| stroke 27 | 1 % → 19 % | 44.7 px | 0.74 | 14.18 | 8 |
| stroke 28 | 2 % → 19 % | 43.7 px | 0.74 | 9.62 | 16 |
| stroke 29 | 3 % → 20 % | 73.9 px | 0.74 | 7.28 | 11 |
| stroke 30 | 5 % → 2 % | 16.6 px | 0.74 | 0.51 | 234 |
| stroke 31 | 10 % → 0 % | 184.6 px | 0.00 | 0.00 | 22 |
| stroke 32 | 8 % → 3 % | 204.8 px | 0.74 | 0.30 | 11 |
| stroke 33 | 2 % → 20 % | 49.6 px | 0.74 | 8.73 | 13 |
| stroke 34 | 4 % → 18 % | 146.8 px | 0.74 | 4.84 | 19 |
| stroke 35 | 10 % → 28 % | 53.8 px | 0.74 | 2.74 | 32 |
| stroke 36 | 3 % → 29 % | 21.9 px | 0.74 | 9.06 | 13 |
| stroke 37 | 1 % → 0 % | 29.0 px | 0.00 | 0.00 | 28 |
| stroke 38 | 2 % → 0 % | 57.5 px | 0.00 | 0.00 | 10 |
| stroke 39 | 3 % → 0 % | 80.3 px | 0.00 | 0.00 | 5 |
| stroke 40 | 4 % → 0 % | 131.3 px | 0.00 | 0.00 | 6 |
| stroke 41 | 6 % → 0 % | 119.7 px | 0.00 | 0.00 | 12 |
| stroke 42 | 7 % → 0 % | 171.0 px | 0.00 | 0.00 | 4 |
| stroke 43 | 8 % → 0 % | 166.1 px | 0.00 | 0.00 | 12 |
| stroke 44 | 9 % → 0 % | 170.7 px | 0.00 | 0.00 | 11 |
| stroke 45 | 10 % → 0 % | 202.7 px | 0.00 | 0.00 | 11 |
| stroke 46 | 12 % → 0 % | 225.0 px | 0.00 | 0.00 | 10 |
| stroke 47 | 13 % → 0 % | 259.9 px | 0.00 | 0.00 | 14 |
| stroke 48 | 13 % → 0 % | 236.1 px | 0.00 | 0.00 | 6 |
| stroke 49 | 13 % → 0 % | 301.8 px | 0.00 | 0.00 | 5 |
| stroke 50 | 13 % → 0 % | 259.5 px | 0.74 | 0.03 | 16 |
| stroke 51 | 13 % → 2 % | 212.3 px | 0.74 | 0.18 | 13 |
| stroke 52 | 14 % → 3 % | 342.7 px | 0.74 | 0.23 | 4 |
| stroke 53 | 1 % → 22 % | 37.4 px | 0.74 | 15.97 | 15 |
| stroke 54 | 3 % → 21 % | 48.1 px | 0.74 | 6.14 | 24 |
| stroke 55 | 7 % → 22 % | 55.6 px | 0.74 | 3.21 | 42 |
| stroke 56 | 12 % → 24 % | 67.6 px | 0.74 | 2.12 | 71 |
| stroke 57 | 16 % → 27 % | 100.9 px | 0.74 | 1.64 | 50 |
| stroke 58 | 16 % → 21 % | 103.0 px | 0.74 | 1.29 | 87 |
| stroke 59 | 23 % → 24 % | 131.8 px | 0.74 | 1.04 | 73 |

Numbers say: wet paint spreads well beyond the stroke.

## Refs v3 · #10 HW maroon loops — own sheet
own sheet 800 × 1070 · Gouache 1.00 + turpentine 30 % · 74 px · 34.4 s

![Refs v3 · #10 HW maroon loops — own sheet](Refs-v3-10-HW-maroon-loops-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 8 % → 0 % | 72.6 px | 0.00 | 0.00 | 151 |
| stroke 2 | 16 % → 0 % | 88.1 px | 0.00 | 0.00 | 324 |
| stroke 3 | 24 % → 0 % | 145.3 px | 0.00 | 0.00 | 301 |
| stroke 4 | 32 % → 0 % | 195.7 px | 0.00 | 0.00 | 286 |
| stroke 5 | 35 % → 2 % | 223.5 px | 0.24 | 0.06 | 352 |
| stroke 6 | 34 % → 2 % | 228.0 px | 0.23 | 0.05 | 248 |
| stroke 7 | 35 % → 1 % | 264.8 px | 0.23 | 0.03 | 273 |
| stroke 8 | 31 % → 1 % | 217.7 px | 0.23 | 0.04 | 258 |
| stroke 9 | 5 % → 1 % | 62.5 px | 0.23 | 0.17 | 41 |
| stroke 10 | 9 % → 0 % | 98.0 px | 0.00 | 0.00 | 47 |
| stroke 11 | 13 % → 0 % | 123.9 px | 0.00 | 0.00 | 58 |
| stroke 12 | 17 % → 0 % | 95.2 px | 0.00 | 0.00 | 144 |
| stroke 13 | 22 % → 0 % | 124.9 px | 0.00 | 0.00 | 154 |
| stroke 14 | 27 % → 1 % | 149.0 px | 0.25 | 0.04 | 171 |
| stroke 15 | 32 % → 1 % | 181.2 px | 0.25 | 0.04 | 143 |
| stroke 16 | 51 % → 2 % | 476.4 px | 0.25 | 0.04 | 49 |
| stroke 17 | 52 % → 2 % | 481.3 px | 0.25 | 0.05 | 50 |
| stroke 18 | 51 % → 3 % | 341.0 px | 0.25 | 0.05 | 60 |
| stroke 19 | 48 % → 3 % | 277.8 px | 0.25 | 0.06 | 64 |
| stroke 20 | 4 % → 3 % | 55.7 px | 0.24 | 0.77 | 54 |
| stroke 21 | 7 % → 3 % | 100.2 px | 0.24 | 0.43 | 59 |
| stroke 22 | 10 % → 3 % | 157.5 px | 0.24 | 0.32 | 43 |
| stroke 23 | 13 % → 3 % | 135.6 px | 0.24 | 0.20 | 88 |
| stroke 24 | 17 % → 3 % | 206.1 px | 0.24 | 0.17 | 62 |
| stroke 25 | 18 % → 3 % | 329.0 px | 0.24 | 0.17 | 40 |
| stroke 26 | 2 % → 0 % | 19.3 px | 0.00 | 0.00 | 58 |
| stroke 27 | 1 % → 6 % | 23.3 px | 0.23 | 7.41 | 9 |
| stroke 28 | 9 % → 0 % | 51.6 px | 0.00 | 0.00 | 164 |
| stroke 29 | 13 % → 0 % | 75.6 px | 0.00 | 0.00 | 217 |
| stroke 30 | 19 % → 0 % | 107.4 px | 0.00 | 0.00 | 243 |
| stroke 31 | 28 % → 0 % | 293.7 px | 0.00 | 0.00 | 86 |
| stroke 32 | 19 % → 0 % | 410.7 px | 0.00 | 0.00 | 35 |
| stroke 33 | 31 % → 0 % | 693.8 px | 0.00 | 0.00 | 39 |
| stroke 34 | 4 % → 4 % | 76.8 px | 0.23 | 0.96 | 44 |
| stroke 35 | 5 % → 4 % | 90.5 px | 0.23 | 0.83 | 51 |
| stroke 36 | 8 % → 4 % | 112.7 px | 0.23 | 0.51 | 50 |
| stroke 37 | 11 % → 4 % | 119.8 px | 0.23 | 0.34 | 149 |
| stroke 38 | 10 % → 0 % | 217.9 px | 0.00 | 0.00 | 38 |
| stroke 39 | 10 % → 3 % | 70.2 px | 0.23 | 0.31 | 355 |
| stroke 40 | 19 % → 3 % | 95.0 px | 0.23 | 0.14 | 527 |
| stroke 41 | 27 % → 3 % | 136.4 px | 0.23 | 0.11 | 504 |
| stroke 42 | 35 % → 4 % | 181.6 px | 0.24 | 0.10 | 573 |
| stroke 43 | 38 % → 2 % | 197.0 px | 0.24 | 0.05 | 645 |
| stroke 44 | 39 % → 2 % | 212.1 px | 0.24 | 0.05 | 467 |
| stroke 45 | 40 % → 2 % | 291.9 px | 0.24 | 0.05 | 365 |
| stroke 46 | 36 % → 2 % | 265.4 px | 0.24 | 0.06 | 314 |
| stroke 47 | 31 % → 3 % | 214.4 px | 0.25 | 0.08 | 361 |
| stroke 48 | 29 % → 3 % | 173.9 px | 0.24 | 0.09 | 409 |
| stroke 49 | 35 % → 2 % | 148.1 px | 0.24 | 0.05 | 491 |
| stroke 50 | 47 % → 1 % | 167.8 px | 0.25 | 0.02 | 461 |
| stroke 51 | 5 % → 0 % | 73.6 px | 0.00 | 0.00 | 87 |
| stroke 52 | 13 % → 0 % | 88.8 px | 0.00 | 0.00 | 224 |
| stroke 53 | 20 % → 0 % | 126.2 px | 0.24 | 0.01 | 264 |
| stroke 54 | 28 % → 1 % | 183.7 px | 0.24 | 0.05 | 251 |
| stroke 55 | 32 % → 2 % | 214.2 px | 0.24 | 0.08 | 289 |
| stroke 56 | 34 % → 3 % | 355.6 px | 0.24 | 0.09 | 131 |
| stroke 57 | 30 % → 3 % | 354.3 px | 0.24 | 0.10 | 91 |
| stroke 58 | 12 % → 3 % | 115.0 px | 0.24 | 0.23 | 147 |
| stroke 59 | 16 % → 2 % | 121.6 px | 0.24 | 0.11 | 221 |
| stroke 60 | 26 % → 0 % | 204.8 px | 0.24 | 0.01 | 106 |
| stroke 61 | 3 % → 4 % | 26.5 px | 0.23 | 1.34 | 59 |
| stroke 62 | 2 % → 3 % | 33.4 px | 0.24 | 1.10 | 41 |
| stroke 63 | 1 % → 2 % | 23.1 px | 0.25 | 1.54 | 12 |

Numbers say: wet paint spreads well beyond the stroke.

## Refs v3 · #11 HW purple balls — own sheet
own sheet 800 × 985 · Gouache 1.00 + turpentine 30 % · 74 px · 39.8 s

![Refs v3 · #11 HW purple balls — own sheet](Refs-v3-11-HW-purple-balls-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 16 % → 0 % | 61.4 px | 0.00 | 0.00 | 218 |
| stroke 2 | 25 % → 0 % | 95.3 px | 0.00 | 0.00 | 349 |
| stroke 3 | 30 % → 0 % | 112.6 px | 0.00 | 0.00 | 520 |
| stroke 4 | 35 % → 0 % | 146.5 px | 0.00 | 0.00 | 580 |
| stroke 5 | 40 % → 0 % | 168.6 px | 0.00 | 0.00 | 564 |
| stroke 6 | 46 % → 0 % | 181.4 px | 0.00 | 0.00 | 697 |
| stroke 7 | 48 % → 0 % | 178.7 px | 0.00 | 0.00 | 635 |
| stroke 8 | 51 % → 0 % | 182.7 px | 0.00 | 0.00 | 664 |
| stroke 9 | 54 % → 0 % | 180.0 px | 0.00 | 0.00 | 713 |
| stroke 10 | 56 % → 0 % | 181.8 px | 0.00 | 0.00 | 893 |
| stroke 11 | 56 % → 0 % | 213.2 px | 0.00 | 0.00 | 967 |
| stroke 12 | 55 % → 0 % | 211.4 px | 0.00 | 0.00 | 1011 |
| stroke 13 | 53 % → 0 % | 204.2 px | 0.00 | 0.00 | 956 |
| stroke 14 | 49 % → 2 % | 248.1 px | 0.65 | 0.04 | 717 |
| stroke 15 | 46 % → 5 % | 212.7 px | 0.66 | 0.12 | 794 |
| stroke 16 | 45 % → 17 % | 256.1 px | 0.66 | 0.39 | 424 |
| stroke 17 | 48 % → 13 % | 289.0 px | 0.66 | 0.27 | 332 |
| stroke 18 | 45 % → 28 % | 250.2 px | 0.66 | 0.62 | 365 |
| stroke 19 | 46 % → 19 % | 237.8 px | 0.66 | 0.42 | 287 |
| stroke 20 | 42 % → 22 % | 246.0 px | 0.65 | 0.54 | 233 |
| stroke 21 | 39 % → 24 % | 542.4 px | 0.65 | 0.62 | 96 |
| stroke 22 | 0 % → 17 % | 22.6 px | 0.66 | 34.62 | 6 |
| stroke 23 | 1 % → 19 % | 35.6 px | 0.66 | 17.81 | 11 |
| stroke 24 | 2 % → 22 % | 54.5 px | 0.66 | 13.42 | 7 |
| stroke 25 | 2 % → 24 % | 61.3 px | 0.66 | 10.26 | 9 |
| stroke 26 | 3 % → 26 % | 72.2 px | 0.66 | 9.50 | 15 |
| stroke 27 | 4 % → 29 % | 77.1 px | 0.66 | 8.22 | 15 |
| stroke 28 | 4 % → 34 % | 151.8 px | 0.66 | 7.95 | 6 |
| stroke 29 | 5 % → 37 % | 169.6 px | 0.66 | 7.75 | 8 |
| stroke 30 | 5 % → 41 % | 194.3 px | 0.66 | 7.66 | 8 |
| stroke 31 | 6 % → 43 % | 289.3 px | 0.66 | 7.27 | 6 |
| stroke 32 | 1 % → 0 % | 29.2 px | 0.00 | 0.00 | 15 |
| stroke 33 | 2 % → 1 % | 27.3 px | 0.66 | 0.44 | 31 |
| stroke 34 | 1 % → 37 % | 18.2 px | 0.65 | 48.22 | 5 |
| stroke 35 | 1 % → 33 % | 19.3 px | 0.65 | 32.58 | 8 |
| stroke 36 | 3 % → 48 % | 45.2 px | 0.64 | 17.48 | 9 |
| stroke 37 | 5 % → 72 % | 16.3 px | 0.65 | 15.05 | 47 |
| stroke 38 | 3 % → 95 % | 36.9 px | 0.64 | 31.00 | 7 |
| stroke 39 | 8 % → 43 % | 75.7 px | 0.65 | 5.52 | 153 |
| stroke 40 | 14 % → 55 % | 103.0 px | 0.65 | 4.00 | 216 |
| stroke 41 | 21 % → 50 % | 104.5 px | 0.65 | 2.35 | 523 |
| stroke 42 | 34 % → 53 % | 133.3 px | 0.65 | 1.58 | 589 |
| stroke 43 | 48 % → 57 % | 157.2 px | 0.65 | 1.19 | 544 |
| stroke 44 | 68 % → 64 % | 185.2 px | 0.65 | 0.94 | 678 |

Numbers say: wet paint spreads well beyond the stroke.

## Refs v3 · #12 HW black-olive cage — own sheet
own sheet 800 × 1150 · Gouache 1.00 + turpentine 30 % · 26 px · 127.7 s

![Refs v3 · #12 HW black-olive cage — own sheet](Refs-v3-12-HW-black-olive-cage-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 14 % → 12 % | 27.4 px | 0.34 | 0.86 | 43 |
| stroke 2 | 24 % → 11 % | 30.3 px | 0.34 | 0.46 | 70 |
| stroke 3 | 31 % → 8 % | 39.9 px | 0.34 | 0.26 | 134 |
| stroke 4 | 8 % → 0 % | 26.8 px | 0.00 | 0.00 | 31 |
| stroke 5 | 12 % → 0 % | 39.0 px | 0.00 | 0.00 | 42 |
| stroke 6 | 17 % → 0 % | 55.2 px | 0.00 | 0.00 | 40 |
| stroke 7 | 25 % → 0 % | 83.7 px | 0.00 | 0.00 | 27 |
| stroke 8 | 33 % → 0 % | 221.1 px | 0.00 | 0.00 | 6 |
| stroke 9 | 26 % → 0 % | 82.2 px | 0.00 | 0.00 | 55 |
| stroke 10 | 26 % → 0 % | 89.0 px | 0.00 | 0.00 | 26 |
| stroke 11 | 20 % → 0 % | 86.2 px | 0.00 | 0.00 | 15 |
| stroke 12 | 8 % → 0 % | 26.0 px | 0.21 | 0.02 | 10 |
| stroke 13 | 12 % → 0 % | 53.6 px | 0.00 | 0.00 | 6 |
| stroke 14 | 10 % → 0 % | 28.4 px | 0.00 | 0.00 | 16 |
| stroke 15 | 7 % → 29 % | 24.1 px | 0.30 | 3.94 | 17 |
| stroke 16 | 21 % → 6 % | 43.0 px | 0.30 | 0.27 | 21 |
| stroke 17 | 28 % → 13 % | 34.1 px | 0.30 | 0.46 | 103 |
| stroke 18 | 49 % → 11 % | 105.1 px | 0.31 | 0.22 | 16 |
| stroke 19 | 14 % → 0 % | 26.0 px | 0.00 | 0.00 | 73 |
| stroke 20 | 21 % → 0 % | 34.2 px | 0.00 | 0.00 | 117 |
| stroke 21 | 35 % → 0 % | 58.3 px | 0.00 | 0.00 | 81 |
| stroke 22 | 8 % → 0 % | 27.0 px | 0.00 | 0.00 | 25 |
| stroke 23 | 10 % → 0 % | 33.2 px | 0.00 | 0.00 | 68 |
| stroke 24 | 12 % → 0 % | 57.7 px | 0.00 | 0.00 | 16 |
| stroke 25 | 26 % → 0 % | 100.2 px | 0.00 | 0.00 | 21 |
| stroke 26 | 10 % → 0 % | 54.4 px | 0.00 | 0.00 | 12 |
| stroke 27 | 15 % → 0 % | 85.2 px | 0.00 | 0.00 | 5 |
| stroke 28 | 11 % → 0 % | 78.5 px | 0.00 | 0.00 | 4 |
| stroke 29 | 5 % → 0 % | 28.7 px | 0.00 | 0.00 | 6 |
| stroke 30 | 11 % → 0 % | 39.8 px | 0.00 | 0.00 | 24 |
| stroke 31 | 16 % → 0 % | 52.0 px | 0.00 | 0.00 | 49 |
| stroke 32 | 23 % → 0 % | 90.0 px | 0.00 | 0.00 | 21 |
| stroke 33 | 29 % → 0 % | 120.5 px | 0.00 | 0.00 | 14 |
| stroke 34 | 19 % → 0 % | 56.9 px | 0.00 | 0.00 | 17 |
| stroke 35 | 27 % → 0 % | 101.0 px | 0.00 | 0.00 | 17 |
| stroke 36 | 28 % → 0 % | 71.9 px | 0.00 | 0.00 | 51 |
| stroke 37 | 27 % → 0 % | 53.2 px | 0.00 | 0.00 | 132 |
| stroke 38 | 34 % → 0 % | 60.0 px | 0.00 | 0.00 | 145 |
| stroke 39 | 45 % → 0 % | 72.2 px | 0.00 | 0.00 | 139 |
| stroke 40 | 63 % → 0 % | 101.3 px | 0.00 | 0.00 | 75 |
| stroke 41 | 59 % → 0 % | 280.2 px | 0.00 | 0.00 | 10 |
| stroke 42 | 82 % → 0 % | 165.9 px | 0.00 | 0.00 | 32 |
| stroke 43 | 4 % → 0 % | 29.8 px | 0.00 | 0.00 | 6 |
| stroke 44 | 8 % → 0 % | 42.2 px | 0.00 | 0.00 | 12 |
| stroke 45 | 12 % → 0 % | 67.3 px | 0.00 | 0.00 | 15 |
| stroke 46 | 4 % → 0 % | 24.9 px | 0.00 | 0.00 | 12 |
| stroke 47 | 8 % → 0 % | 37.0 px | 0.00 | 0.00 | 12 |
| stroke 48 | 23 % → 0 % | 37.0 px | 0.00 | 0.00 | 29 |
| stroke 49 | 39 % → 0 % | 53.9 px | 0.00 | 0.00 | 52 |
| stroke 50 | 8 % → 0 % | 15.2 px | 0.00 | 0.00 | 23 |
| stroke 51 | 9 % → 0 % | 16.7 px | 0.00 | 0.00 | 10 |
| stroke 52 | 6 % → 0 % | 19.9 px | 0.00 | 0.00 | 20 |
| stroke 53 | 5 % → 32 % | 15.9 px | 0.31 | 6.98 | 4 |
| stroke 54 | 7 % → 0 % | 20.2 px | 0.33 | 0.04 | 22 |
| stroke 55 | 6 % → 0 % | 23.6 px | 0.28 | 0.08 | 41 |
| stroke 56 | 13 % → 0 % | 65.5 px | 0.24 | 0.00 | 14 |
| stroke 57 | 7 % → 0 % | 18.0 px | 0.00 | 0.00 | 14 |
| stroke 58 | 15 % → 0 % | 39.8 px | 0.00 | 0.00 | 19 |
| stroke 59 | 21 % → 0 % | 38.8 px | 0.00 | 0.00 | 40 |
| stroke 60 | 12 % → 0 % | 30.0 px | 0.00 | 0.00 | 51 |
| stroke 61 | 8 % → 0 % | 26.6 px | 0.00 | 0.00 | 24 |
| stroke 62 | 8 % → 0 % | 29.7 px | 0.00 | 0.00 | 23 |
| stroke 63 | 12 % → 0 % | 53.4 px | 0.00 | 0.00 | 12 |
| stroke 64 | 18 % → 0 % | 41.2 px | 0.00 | 0.00 | 31 |
| stroke 65 | 7 % → 0 % | 25.6 px | 0.00 | 0.00 | 13 |
| stroke 66 | 14 % → 0 % | 46.8 px | 0.00 | 0.00 | 26 |
| stroke 67 | 18 % → 0 % | 59.9 px | 0.00 | 0.00 | 35 |
| stroke 68 | 13 % → 0 % | 29.3 px | 0.00 | 0.00 | 49 |
| stroke 69 | 4 % → 4 % | 21.9 px | 0.34 | 1.22 | 6 |
| stroke 70 | 10 % → 13 % | 24.5 px | 0.34 | 1.28 | 34 |
| stroke 71 | 17 % → 10 % | 30.4 px | 0.34 | 0.59 | 79 |
| stroke 72 | 24 % → 10 % | 45.0 px | 0.34 | 0.41 | 75 |
| stroke 73 | 32 % → 16 % | 268.5 px | 0.34 | 0.51 | 3 |
| stroke 74 | 34 % → 4 % | 128.2 px | 0.33 | 0.11 | 18 |
| stroke 75 | 31 % → 0 % | 86.9 px | 0.33 | 0.01 | 32 |
| stroke 76 | 24 % → 0 % | 88.0 px | 0.00 | 0.00 | 18 |
| stroke 77 | 23 % → 0 % | 72.8 px | 0.00 | 0.00 | 21 |
| stroke 78 | 23 % → 0 % | 68.3 px | 0.00 | 0.00 | 32 |
| stroke 79 | 24 % → 0 % | 124.5 px | 0.00 | 0.00 | 9 |
| stroke 80 | 26 % → 0 % | 147.2 px | 0.00 | 0.00 | 9 |
| stroke 81 | 25 % → 0 % | 103.0 px | 0.00 | 0.00 | 18 |
| stroke 82 | 24 % → 0 % | 127.6 px | 0.00 | 0.00 | 16 |
| stroke 83 | 22 % → 0 % | 116.6 px | 0.00 | 0.00 | 11 |
| stroke 84 | 20 % → 0 % | 142.2 px | 0.00 | 0.00 | 7 |
| stroke 85 | 4 % → 0 % | 23.1 px | 0.00 | 0.00 | 6 |
| stroke 86 | 9 % → 0 % | 28.3 px | 0.00 | 0.00 | 28 |
| stroke 87 | 13 % → 0 % | 59.2 px | 0.00 | 0.00 | 16 |
| stroke 88 | 3 % → 0 % | 18.8 px | 0.00 | 0.00 | 10 |
| stroke 89 | 6 % → 0 % | 29.7 px | 0.00 | 0.00 | 12 |
| stroke 90 | 11 % → 0 % | 46.5 px | 0.00 | 0.00 | 24 |
| stroke 91 | 14 % → 0 % | 58.8 px | 0.00 | 0.00 | 13 |
| stroke 92 | 18 % → 0 % | 77.7 px | 0.00 | 0.00 | 22 |
| stroke 93 | 17 % → 0 % | 77.6 px | 0.00 | 0.00 | 16 |
| stroke 94 | 6 % → 13 % | 34.7 px | 0.29 | 2.29 | 6 |
| stroke 95 | 20 % → 3 % | 60.4 px | 0.29 | 0.18 | 35 |
| stroke 96 | 25 % → 0 % | 93.8 px | 0.28 | 0.01 | 28 |
| stroke 97 | 6 % → 0 % | 26.4 px | 0.00 | 0.00 | 13 |
| stroke 98 | 9 % → 0 % | 31.4 px | 0.00 | 0.00 | 16 |
| stroke 99 | 15 % → 0 % | 99.7 px | 0.00 | 0.00 | 8 |
| stroke 100 | 4 % → 0 % | 23.0 px | 0.00 | 0.00 | 8 |
| stroke 101 | 8 % → 0 % | 28.3 px | 0.00 | 0.00 | 20 |
| stroke 102 | 15 % → 0 % | 68.2 px | 0.00 | 0.00 | 15 |
| stroke 103 | 23 % → 0 % | 83.9 px | 0.00 | 0.00 | 15 |
| stroke 104 | 28 % → 0 % | 266.4 px | 0.00 | 0.00 | 5 |
| stroke 105 | 4 % → 0 % | 25.4 px | 0.00 | 0.00 | 6 |
| stroke 106 | 11 % → 0 % | 22.3 px | 0.00 | 0.00 | 48 |
| stroke 107 | 19 % → 0 % | 31.2 px | 0.00 | 0.00 | 94 |
| stroke 108 | 23 % → 0 % | 36.3 px | 0.00 | 0.00 | 131 |
| stroke 109 | 18 % → 0 % | 75.6 px | 0.00 | 0.00 | 21 |
| stroke 110 | 36 % → 0 % | 186.4 px | 0.00 | 0.00 | 8 |
| stroke 111 | 21 % → 0 % | 43.2 px | 0.00 | 0.00 | 63 |
| stroke 112 | 28 % → 0 % | 150.0 px | 0.00 | 0.00 | 13 |
| stroke 113 | 18 % → 0 % | 48.2 px | 0.00 | 0.00 | 30 |
| stroke 114 | 12 % → 0 % | 87.5 px | 0.00 | 0.00 | 4 |
| stroke 115 | 22 % → 0 % | 56.3 px | 0.00 | 0.00 | 36 |
| stroke 116 | 13 % → 0 % | 89.8 px | 0.00 | 0.00 | 4 |
| stroke 117 | 27 % → 0 % | 54.7 px | 0.00 | 0.00 | 59 |
| stroke 118 | 15 % → 0 % | 108.8 px | 0.00 | 0.00 | 5 |
| stroke 119 | 41 % → 0 % | 111.0 px | 0.00 | 0.00 | 27 |
| stroke 120 | 28 % → 0 % | 85.0 px | 0.00 | 0.00 | 36 |
| stroke 121 | 26 % → 0 % | 95.1 px | 0.00 | 0.00 | 29 |
| stroke 122 | 9 % → 0 % | 56.3 px | 0.00 | 0.00 | 12 |
| stroke 123 | 9 % → 0 % | 48.9 px | 0.00 | 0.00 | 13 |
| stroke 124 | 11 % → 0 % | 59.7 px | 0.00 | 0.00 | 7 |
| stroke 125 | 16 % → 0 % | 100.3 px | 0.00 | 0.00 | 11 |
| stroke 126 | 17 % → 0 % | 89.6 px | 0.00 | 0.00 | 9 |
| stroke 127 | 21 % → 0 % | 141.5 px | 0.00 | 0.00 | 13 |
| stroke 128 | 18 % → 0 % | 92.3 px | 0.00 | 0.00 | 6 |
| stroke 129 | 18 % → 0 % | 125.1 px | 0.00 | 0.00 | 9 |
| stroke 130 | 18 % → 0 % | 95.0 px | 0.00 | 0.00 | 7 |
| stroke 131 | 20 % → 0 % | 133.7 px | 0.00 | 0.00 | 10 |
| stroke 132 | 19 % → 0 % | 99.7 px | 0.00 | 0.00 | 12 |
| stroke 133 | 20 % → 0 % | 128.8 px | 0.00 | 0.00 | 7 |
| stroke 134 | 20 % → 0 % | 125.8 px | 0.00 | 0.00 | 9 |
| stroke 135 | 24 % → 0 % | 105.3 px | 0.00 | 0.00 | 17 |
| stroke 136 | 23 % → 0 % | 123.3 px | 0.00 | 0.00 | 15 |
| stroke 137 | 6 % → 0 % | 25.8 px | 0.00 | 0.00 | 10 |
| stroke 138 | 9 % → 0 % | 40.8 px | 0.00 | 0.00 | 8 |
| stroke 139 | 14 % → 0 % | 62.0 px | 0.00 | 0.00 | 7 |
| stroke 140 | 8 % → 0 % | 38.1 px | 0.00 | 0.00 | 4 |
| stroke 141 | 7 % → 14 % | 22.1 px | 0.29 | 2.12 | 44 |
| stroke 142 | 11 % → 14 % | 35.2 px | 0.29 | 1.28 | 60 |
| stroke 143 | 20 % → 19 % | 115.6 px | 0.29 | 0.99 | 22 |
| stroke 144 | 23 % → 19 % | 146.4 px | 0.29 | 0.86 | 8 |
| stroke 145 | 4 % → 0 % | 26.6 px | 0.00 | 0.00 | 4 |
| stroke 146 | 7 % → 0 % | 26.1 px | 0.00 | 0.00 | 20 |
| stroke 147 | 3 % → 0 % | 20.8 px | 0.00 | 0.00 | 3 |
| stroke 148 | 5 % → 3 % | 22.0 px | 0.32 | 0.55 | 19 |
| stroke 149 | 7 % → 0 % | 23.1 px | 0.00 | 0.00 | 13 |
| stroke 150 | 14 % → 0 % | 38.8 px | 0.00 | 0.00 | 40 |
| stroke 151 | 8 % → 22 % | 22.2 px | 0.30 | 2.62 | 27 |
| stroke 152 | 13 % → 3 % | 37.2 px | 0.30 | 0.21 | 39 |
| stroke 153 | 7 % → 0 % | 25.3 px | 0.00 | 0.00 | 23 |
| stroke 154 | 7 % → 0 % | 23.7 px | 0.00 | 0.00 | 16 |
| stroke 155 | 12 % → 0 % | 46.6 px | 0.00 | 0.00 | 21 |
| stroke 156 | 5 % → 0 % | 24.2 px | 0.00 | 0.00 | 13 |
| stroke 157 | 18 % → 0 % | 45.8 px | 0.00 | 0.00 | 67 |
| stroke 158 | 26 % → 0 % | 60.8 px | 0.00 | 0.00 | 87 |
| stroke 159 | 31 % → 0 % | 74.5 px | 0.00 | 0.00 | 167 |
| stroke 160 | 35 % → 0 % | 98.9 px | 0.00 | 0.00 | 161 |
| stroke 161 | 29 % → 0 % | 112.2 px | 0.00 | 0.00 | 63 |
| stroke 162 | 28 % → 0 % | 102.2 px | 0.00 | 0.00 | 50 |
| stroke 163 | 29 % → 0 % | 107.2 px | 0.00 | 0.00 | 58 |
| stroke 164 | 32 % → 0 % | 126.7 px | 0.00 | 0.00 | 46 |
| stroke 165 | 15 % → 0 % | 47.8 px | 0.00 | 0.00 | 32 |
| stroke 166 | 25 % → 0 % | 95.5 px | 0.00 | 0.00 | 34 |
| stroke 167 | 23 % → 1 % | 56.7 px | 0.31 | 0.03 | 76 |
| stroke 168 | 25 % → 0 % | 82.2 px | 0.00 | 0.00 | 92 |
| stroke 169 | 30 % → 7 % | 72.6 px | 0.32 | 0.23 | 165 |
| stroke 170 | 32 % → 0 % | 101.6 px | 0.00 | 0.00 | 115 |
| stroke 171 | 33 % → 8 % | 88.4 px | 0.32 | 0.24 | 148 |
| stroke 172 | 35 % → 0 % | 148.2 px | 0.00 | 0.00 | 39 |
| stroke 173 | 31 % → 10 % | 93.7 px | 0.32 | 0.33 | 281 |
| stroke 174 | 29 % → 1 % | 93.0 px | 0.32 | 0.02 | 121 |
| stroke 175 | 23 % → 5 % | 80.8 px | 0.33 | 0.23 | 323 |
| stroke 176 | 35 % → 8 % | 110.4 px | 0.33 | 0.22 | 159 |
| stroke 177 | 49 % → 4 % | 160.1 px | 0.34 | 0.07 | 110 |
| stroke 178 | 46 % → 0 % | 175.2 px | 0.35 | 0.00 | 62 |
| stroke 179 | 17 % → 1 % | 45.5 px | 0.33 | 0.07 | 50 |
| stroke 180 | 32 % → 0 % | 76.1 px | 0.00 | 0.00 | 60 |
| stroke 181 | 46 % → 0 % | 119.7 px | 0.00 | 0.00 | 49 |
| stroke 182 | 16 % → 1 % | 50.1 px | 0.34 | 0.08 | 58 |
| stroke 183 | 26 % → 6 % | 64.7 px | 0.34 | 0.22 | 98 |
| stroke 184 | 37 % → 0 % | 116.0 px | 0.33 | 0.01 | 61 |
| stroke 185 | 7 % → 18 % | 28.5 px | 0.31 | 2.60 | 18 |
| stroke 186 | 13 % → 14 % | 49.3 px | 0.32 | 1.05 | 20 |
| stroke 187 | 20 % → 12 % | 93.3 px | 0.32 | 0.63 | 16 |
| stroke 188 | 5 % → 0 % | 29.2 px | 0.00 | 0.00 | 13 |
| stroke 189 | 9 % → 0 % | 37.9 px | 0.00 | 0.00 | 16 |
| stroke 190 | 5 % → 1 % | 35.4 px | 0.31 | 0.21 | 14 |
| stroke 191 | 12 % → 6 % | 37.3 px | 0.32 | 0.52 | 67 |
| stroke 192 | 14 % → 11 % | 44.5 px | 0.33 | 0.82 | 59 |
| stroke 193 | 29 % → 8 % | 123.0 px | 0.32 | 0.28 | 18 |
| stroke 194 | 33 % → 11 % | 227.2 px | 0.32 | 0.32 | 12 |
| stroke 195 | 10 % → 0 % | 28.4 px | 0.00 | 0.00 | 60 |
| stroke 196 | 16 % → 0 % | 42.3 px | 0.00 | 0.00 | 70 |
| stroke 197 | 31 % → 0 % | 166.3 px | 0.00 | 0.00 | 12 |
| stroke 198 | 18 % → 0 % | 54.5 px | 0.00 | 0.00 | 32 |
| stroke 199 | 16 % → 11 % | 40.6 px | 0.30 | 0.67 | 62 |
| stroke 200 | 10 % → 0 % | 27.1 px | 0.00 | 0.00 | 54 |
| stroke 201 | 23 % → 12 % | 57.0 px | 0.30 | 0.53 | 95 |
| stroke 202 | 15 % → 0 % | 37.6 px | 0.00 | 0.00 | 85 |
| stroke 203 | 39 % → 0 % | 117.1 px | 0.00 | 0.00 | 40 |
| stroke 204 | 35 % → 0 % | 173.4 px | 0.00 | 0.00 | 19 |
| stroke 205 | 20 % → 0 % | 75.3 px | 0.00 | 0.00 | 30 |
| stroke 206 | 36 % → 0 % | 112.7 px | 0.00 | 0.00 | 22 |
| stroke 207 | 26 % → 23 % | 112.4 px | 0.30 | 0.87 | 29 |
| stroke 208 | 22 % → 0 % | 98.4 px | 0.00 | 0.00 | 46 |
| stroke 209 | 31 % → 0 % | 98.6 px | 0.00 | 0.00 | 39 |
| stroke 210 | 30 % → 26 % | 221.1 px | 0.30 | 0.88 | 3 |
| stroke 211 | 24 % → 0 % | 183.9 px | 0.00 | 0.00 | 6 |
| stroke 212 | 20 % → 0 % | 111.9 px | 0.00 | 0.00 | 9 |
| stroke 213 | 15 % → 19 % | 117.8 px | 0.29 | 1.28 | 6 |
| stroke 214 | 23 % → 0 % | 73.0 px | 0.00 | 0.00 | 47 |
| stroke 215 | 20 % → 0 % | 66.4 px | 0.00 | 0.00 | 64 |
| stroke 216 | 13 % → 12 % | 52.1 px | 0.29 | 0.94 | 28 |
| stroke 217 | 27 % → 0 % | 65.6 px | 0.00 | 0.00 | 97 |
| stroke 218 | 18 % → 8 % | 52.4 px | 0.29 | 0.43 | 63 |
| stroke 219 | 35 % → 0 % | 91.6 px | 0.00 | 0.00 | 50 |
| stroke 220 | 32 % → 4 % | 79.7 px | 0.29 | 0.12 | 198 |
| stroke 221 | 44 % → 0 % | 154.3 px | 0.00 | 0.00 | 38 |
| stroke 222 | 36 % → 2 % | 140.4 px | 0.29 | 0.05 | 26 |
| stroke 223 | 34 % → 6 % | 196.4 px | 0.29 | 0.17 | 19 |
| stroke 224 | 39 % → 0 % | 154.2 px | 0.00 | 0.00 | 23 |
| stroke 225 | 40 % → 1 % | 119.2 px | 0.29 | 0.03 | 46 |
| stroke 226 | 39 % → 0 % | 97.0 px | 0.28 | 0.00 | 127 |
| stroke 227 | 46 % → 0 % | 199.0 px | 0.00 | 0.00 | 26 |
| stroke 228 | 5 % → 0 % | 30.5 px | 0.00 | 0.00 | 5 |
| stroke 229 | 10 % → 0 % | 45.6 px | 0.00 | 0.00 | 16 |
| stroke 230 | 15 % → 0 % | 56.4 px | 0.00 | 0.00 | 24 |
| stroke 231 | 20 % → 0 % | 78.2 px | 0.00 | 0.00 | 53 |
| stroke 232 | 4 % → 0 % | 28.2 px | 0.00 | 0.00 | 13 |
| stroke 233 | 9 % → 7 % | 39.1 px | 0.30 | 0.69 | 20 |
| stroke 234 | 13 % → 0 % | 104.1 px | 0.00 | 0.00 | 3 |
| stroke 235 | 14 % → 4 % | 45.2 px | 0.30 | 0.29 | 64 |
| stroke 236 | 5 % → 0 % | 35.3 px | 0.00 | 0.00 | 9 |
| stroke 237 | 24 % → 4 % | 90.8 px | 0.30 | 0.18 | 39 |
| stroke 238 | 23 % → 0 % | 70.9 px | 0.00 | 0.00 | 49 |
| stroke 239 | 35 % → 6 % | 147.9 px | 0.30 | 0.18 | 34 |
| stroke 240 | 36 % → 0 % | 154.2 px | 0.00 | 0.00 | 24 |
| stroke 241 | 40 % → 0 % | 145.4 px | 0.00 | 0.00 | 19 |
| stroke 242 | 39 % → 0 % | 139.6 px | 0.00 | 0.00 | 29 |
| stroke 243 | 4 % → 0 % | 29.2 px | 0.00 | 0.00 | 11 |
| stroke 244 | 10 % → 0 % | 28.9 px | 0.00 | 0.00 | 73 |
| stroke 245 | 21 % → 0 % | 84.6 px | 0.00 | 0.00 | 32 |
| stroke 246 | 25 % → 0 % | 118.7 px | 0.00 | 0.00 | 20 |
| stroke 247 | 14 % → 0 % | 27.2 px | 0.00 | 0.00 | 100 |
| stroke 248 | 12 % → 0 % | 40.0 px | 0.00 | 0.00 | 39 |
| stroke 249 | 22 % → 0 % | 37.1 px | 0.00 | 0.00 | 226 |
| stroke 250 | 29 % → 0 % | 50.5 px | 0.00 | 0.00 | 179 |
| stroke 251 | 33 % → 0 % | 87.6 px | 0.00 | 0.00 | 44 |
| stroke 252 | 45 % → 0 % | 308.8 px | 0.00 | 0.00 | 20 |
| stroke 253 | 33 % → 0 % | 112.6 px | 0.00 | 0.00 | 25 |
| stroke 254 | 26 % → 0 % | 140.4 px | 0.00 | 0.00 | 21 |
| stroke 255 | 44 % → 0 % | 239.9 px | 0.00 | 0.00 | 15 |
| stroke 256 | 39 % → 0 % | 280.4 px | 0.00 | 0.00 | 4 |
| stroke 257 | 31 % → 0 % | 116.3 px | 0.00 | 0.00 | 14 |
| stroke 258 | 37 % → 0 % | 135.5 px | 0.00 | 0.00 | 32 |
| stroke 259 | 34 % → 0 % | 163.5 px | 0.00 | 0.00 | 11 |
| stroke 260 | 34 % → 0 % | 127.9 px | 0.00 | 0.00 | 27 |
| stroke 261 | 36 % → 0 % | 130.0 px | 0.00 | 0.00 | 16 |
| stroke 262 | 21 % → 0 % | 85.6 px | 0.00 | 0.00 | 13 |
| stroke 263 | 26 % → 0 % | 174.4 px | 0.00 | 0.00 | 4 |
| stroke 264 | 47 % → 0 % | 140.2 px | 0.00 | 0.00 | 24 |
| stroke 265 | 22 % → 0 % | 61.8 px | 0.00 | 0.00 | 39 |
| stroke 266 | 33 % → 0 % | 107.8 px | 0.00 | 0.00 | 21 |
| stroke 267 | 27 % → 0 % | 164.6 px | 0.00 | 0.00 | 6 |
| stroke 268 | 33 % → 0 % | 100.1 px | 0.00 | 0.00 | 17 |
| stroke 269 | 35 % → 0 % | 128.6 px | 0.00 | 0.00 | 23 |
| stroke 270 | 12 % → 19 % | 22.0 px | 0.31 | 1.61 | 30 |
| stroke 271 | 7 % → 0 % | 17.4 px | 0.00 | 0.00 | 11 |
| stroke 272 | 5 % → 0 % | 28.0 px | 0.00 | 0.00 | 6 |
| stroke 273 | 10 % → 3 % | 26.1 px | 0.33 | 0.31 | 29 |
| stroke 274 | 9 % → 7 % | 46.3 px | 0.34 | 0.78 | 6 |
| stroke 275 | 6 % → 14 % | 29.3 px | 0.34 | 2.33 | 29 |
| stroke 276 | 8 % → 0 % | 29.8 px | 0.00 | 0.00 | 20 |
| stroke 277 | 5 % → 15 % | 27.9 px | 0.34 | 3.19 | 6 |
| stroke 278 | 5 % → 3 % | 24.3 px | 0.34 | 0.62 | 12 |
| stroke 279 | 6 % → 0 % | 23.3 px | 0.00 | 0.00 | 19 |
| stroke 280 | 8 % → 0 % | 31.1 px | 0.00 | 0.00 | 23 |
| stroke 281 | 4 % → 0 % | 22.8 px | 0.00 | 0.00 | 11 |
| stroke 282 | 13 % → 0 % | 47.8 px | 0.00 | 0.00 | 29 |
| stroke 283 | 4 % → 0 % | 23.9 px | 0.00 | 0.00 | 4 |
| stroke 284 | 16 % → 0 % | 45.6 px | 0.00 | 0.00 | 39 |
| stroke 285 | 23 % → 0 % | 88.7 px | 0.00 | 0.00 | 38 |
| stroke 286 | 16 % → 0 % | 48.2 px | 0.00 | 0.00 | 56 |
| stroke 287 | 13 % → 0 % | 55.2 px | 0.00 | 0.00 | 25 |
| stroke 288 | 24 % → 0 % | 47.4 px | 0.00 | 0.00 | 100 |
| stroke 289 | 35 % → 0 % | 132.6 px | 0.00 | 0.00 | 31 |
| stroke 290 | 21 % → 0 % | 77.4 px | 0.00 | 0.00 | 27 |
| stroke 291 | 15 % → 0 % | 47.9 px | 0.00 | 0.00 | 48 |
| stroke 292 | 42 % → 0 % | 74.1 px | 0.00 | 0.00 | 195 |
| stroke 293 | 27 % → 0 % | 122.2 px | 0.00 | 0.00 | 21 |
| stroke 294 | 53 % → 0 % | 156.1 px | 0.00 | 0.00 | 51 |
| stroke 295 | 26 % → 0 % | 95.9 px | 0.00 | 0.00 | 63 |
| stroke 296 | 48 % → 1 % | 68.0 px | 0.29 | 0.03 | 624 |
| stroke 297 | 49 % → 0 % | 79.8 px | 0.00 | 0.00 | 251 |
| stroke 298 | 49 % → 0 % | 182.7 px | 0.00 | 0.00 | 46 |
| stroke 299 | 54 % → 0 % | 143.8 px | 0.00 | 0.00 | 72 |
| stroke 300 | 45 % → 0 % | 90.1 px | 0.00 | 0.00 | 118 |
| stroke 301 | 43 % → 0 % | 82.0 px | 0.00 | 0.00 | 105 |
| stroke 302 | 25 % → 0 % | 55.3 px | 0.00 | 0.00 | 94 |
| stroke 303 | 48 % → 0 % | 74.6 px | 0.00 | 0.00 | 211 |
| stroke 304 | 17 % → 0 % | 52.0 px | 0.00 | 0.00 | 50 |
| stroke 305 | 51 % → 0 % | 74.9 px | 0.00 | 0.00 | 299 |
| stroke 306 | 55 % → 0 % | 94.7 px | 0.00 | 0.00 | 133 |
| stroke 307 | 44 % → 0 % | 95.8 px | 0.00 | 0.00 | 107 |
| stroke 308 | 52 % → 0 % | 98.1 px | 0.00 | 0.00 | 130 |
| stroke 309 | 46 % → 0 % | 119.8 px | 0.00 | 0.00 | 82 |
| stroke 310 | 46 % → 0 % | 76.1 px | 0.00 | 0.00 | 264 |
| stroke 311 | 48 % → 0 % | 77.9 px | 0.00 | 0.00 | 227 |
| stroke 312 | 30 % → 0 % | 66.8 px | 0.00 | 0.00 | 239 |
| stroke 313 | 10 % → 16 % | 29.0 px | 0.31 | 1.55 | 27 |
| stroke 314 | 12 % → 13 % | 24.8 px | 0.34 | 1.12 | 56 |
| stroke 315 | 7 % → 9 % | 38.9 px | 0.32 | 1.43 | 8 |
| stroke 316 | 8 % → 13 % | 31.5 px | 0.32 | 1.62 | 27 |
| stroke 317 | 9 % → 15 % | 37.6 px | 0.35 | 1.68 | 24 |
| stroke 318 | 12 % → 14 % | 27.3 px | 0.30 | 1.19 | 64 |

Numbers say: wet paint spreads well beyond the stroke.

## Refs v3 · #13 HW blue streaky form — own sheet
own sheet 800 × 1020 · Gouache 1.00 + turpentine 30 % · 74 px · 124.1 s

![Refs v3 · #13 HW blue streaky form — own sheet](Refs-v3-13-HW-blue-streaky-form-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 9 % → 32 % | 74.0 px | 0.46 | 3.71 | 172 |
| stroke 2 | 13 % → 31 % | 122.6 px | 0.47 | 2.40 | 189 |
| stroke 3 | 19 % → 20 % | 222.0 px | 0.46 | 1.06 | 162 |
| stroke 4 | 19 % → 26 % | 138.6 px | 0.47 | 1.38 | 320 |
| stroke 5 | 12 % → 19 % | 175.4 px | 0.49 | 1.67 | 106 |
| stroke 6 | 28 % → 13 % | 372.0 px | 0.47 | 0.45 | 130 |
| stroke 7 | 29 % → 14 % | 167.9 px | 0.48 | 0.49 | 469 |
| stroke 8 | 36 % → 6 % | 179.4 px | 0.48 | 0.17 | 665 |
| stroke 9 | 32 % → 0 % | 283.3 px | 0.46 | 0.00 | 126 |
| stroke 10 | 42 % → 0 % | 231.0 px | 0.51 | 0.01 | 433 |
| stroke 11 | 39 % → 0 % | 568.3 px | 0.00 | 0.00 | 91 |
| stroke 12 | 44 % → 0 % | 256.7 px | 0.00 | 0.00 | 370 |
| stroke 13 | 34 % → 0 % | 341.0 px | 0.00 | 0.00 | 82 |
| stroke 14 | 45 % → 0 % | 234.2 px | 0.00 | 0.00 | 485 |
| stroke 15 | 45 % → 0 % | 457.6 px | 0.00 | 0.00 | 177 |
| stroke 16 | 46 % → 0 % | 289.6 px | 0.00 | 0.00 | 296 |
| stroke 17 | 41 % → 0 % | 479.4 px | 0.00 | 0.00 | 113 |
| stroke 18 | 40 % → 0 % | 342.7 px | 0.00 | 0.00 | 194 |
| stroke 19 | 31 % → 0 % | 417.3 px | 0.00 | 0.00 | 90 |
| stroke 20 | 49 % → 0 % | 477.5 px | 0.00 | 0.00 | 147 |
| stroke 21 | 40 % → 0 % | 264.3 px | 0.00 | 0.00 | 325 |
| stroke 22 | 28 % → 0 % | 318.5 px | 0.00 | 0.00 | 121 |
| stroke 23 | 35 % → 0 % | 416.6 px | 0.00 | 0.00 | 93 |
| stroke 24 | 29 % → 0 % | 370.3 px | 0.00 | 0.00 | 81 |
| stroke 25 | 3 % → 11 % | 23.9 px | 0.48 | 3.99 | 33 |
| stroke 26 | 3 % → 0 % | 59.2 px | 0.00 | 0.00 | 11 |
| stroke 27 | 1 % → 0 % | 20.5 px | 0.00 | 0.00 | 8 |
| stroke 28 | 2 % → 26 % | 30.6 px | 0.49 | 15.15 | 13 |
| stroke 29 | 4 % → 26 % | 37.8 px | 0.48 | 7.48 | 48 |
| stroke 30 | 5 % → 26 % | 115.2 px | 0.48 | 5.77 | 19 |
| stroke 31 | 8 % → 3 % | 177.9 px | 0.49 | 0.44 | 8 |
| stroke 32 | 7 % → 1 % | 174.9 px | 0.50 | 0.16 | 9 |
| stroke 33 | 6 % → 0 % | 143.2 px | 0.50 | 0.07 | 12 |
| stroke 34 | 5 % → 0 % | 89.9 px | 0.48 | 0.00 | 19 |
| stroke 35 | 6 % → 0 % | 142.7 px | 0.00 | 0.00 | 15 |
| stroke 36 | 7 % → 0 % | 134.9 px | 0.00 | 0.00 | 17 |
| stroke 37 | 8 % → 0 % | 188.7 px | 0.00 | 0.00 | 16 |
| stroke 38 | 8 % → 0 % | 204.3 px | 0.00 | 0.00 | 13 |
| stroke 39 | 9 % → 0 % | 236.7 px | 0.00 | 0.00 | 5 |
| stroke 40 | 9 % → 0 % | 141.7 px | 0.00 | 0.00 | 22 |
| stroke 41 | 10 % → 0 % | 169.7 px | 0.00 | 0.00 | 14 |
| stroke 42 | 8 % → 0 % | 164.0 px | 0.00 | 0.00 | 18 |
| stroke 43 | 12 % → 0 % | 176.6 px | 0.00 | 0.00 | 26 |
| stroke 44 | 4 % → 0 % | 44.2 px | 0.00 | 0.00 | 62 |
| stroke 45 | 13 % → 0 % | 176.0 px | 0.00 | 0.00 | 48 |
| stroke 46 | 17 % → 0 % | 290.0 px | 0.00 | 0.00 | 12 |
| stroke 47 | 8 % → 0 % | 100.7 px | 0.00 | 0.00 | 52 |
| stroke 48 | 17 % → 0 % | 127.5 px | 0.00 | 0.00 | 69 |
| stroke 49 | 9 % → 0 % | 244.3 px | 0.00 | 0.00 | 22 |
| stroke 50 | 19 % → 0 % | 213.8 px | 0.00 | 0.00 | 69 |
| stroke 51 | 23 % → 0 % | 398.8 px | 0.00 | 0.00 | 27 |
| stroke 52 | 20 % → 0 % | 298.1 px | 0.00 | 0.00 | 57 |
| stroke 53 | 26 % → 0 % | 573.2 px | 0.00 | 0.00 | 7 |
| stroke 54 | 24 % → 0 % | 574.7 px | 0.00 | 0.00 | 31 |
| stroke 55 | 5 % → 28 % | 183.1 px | 0.48 | 5.45 | 24 |
| stroke 56 | 6 % → 24 % | 155.8 px | 0.48 | 3.91 | 27 |
| stroke 57 | 9 % → 21 % | 215.7 px | 0.48 | 2.40 | 29 |
| stroke 58 | 1 % → 24 % | 35.8 px | 0.46 | 22.88 | 19 |
| stroke 59 | 2 % → 20 % | 45.4 px | 0.47 | 9.83 | 39 |
| stroke 60 | 3 % → 17 % | 94.6 px | 0.47 | 6.26 | 24 |
| stroke 61 | 4 % → 15 % | 123.8 px | 0.47 | 3.92 | 10 |
| stroke 62 | 6 % → 0 % | 159.2 px | 0.00 | 0.00 | 27 |
| stroke 63 | 3 % → 0 % | 88.3 px | 0.00 | 0.00 | 13 |
| stroke 64 | 4 % → 0 % | 67.7 px | 0.00 | 0.00 | 32 |
| stroke 65 | 5 % → 0 % | 73.8 px | 0.00 | 0.00 | 28 |
| stroke 66 | 6 % → 0 % | 87.2 px | 0.00 | 0.00 | 65 |
| stroke 67 | 13 % → 0 % | 92.0 px | 0.00 | 0.00 | 145 |
| stroke 68 | 21 % → 0 % | 538.2 px | 0.00 | 0.00 | 14 |
| stroke 69 | 16 % → 0 % | 113.9 px | 0.00 | 0.00 | 110 |
| stroke 70 | 22 % → 0 % | 412.3 px | 0.00 | 0.00 | 43 |
| stroke 71 | 22 % → 0 % | 709.5 px | 0.00 | 0.00 | 12 |
| stroke 72 | 18 % → 0 % | 144.0 px | 0.00 | 0.00 | 84 |
| stroke 73 | 21 % → 0 % | 450.4 px | 0.00 | 0.00 | 17 |
| stroke 74 | 22 % → 0 % | 170.0 px | 0.00 | 0.00 | 105 |
| stroke 75 | 23 % → 0 % | 834.5 px | 0.00 | 0.00 | 13 |
| stroke 76 | 18 % → 0 % | 385.5 px | 0.00 | 0.00 | 21 |
| stroke 77 | 24 % → 0 % | 353.9 px | 0.00 | 0.00 | 52 |
| stroke 78 | 26 % → 0 % | 276.8 px | 0.00 | 0.00 | 137 |
| stroke 79 | 17 % → 0 % | 217.5 px | 0.00 | 0.00 | 21 |
| stroke 80 | 23 % → 0 % | 791.5 px | 0.00 | 0.00 | 25 |
| stroke 81 | 26 % → 0 % | 420.1 px | 0.00 | 0.00 | 50 |
| stroke 82 | 15 % → 0 % | 172.2 px | 0.00 | 0.00 | 58 |
| stroke 83 | 23 % → 0 % | 571.3 px | 0.00 | 0.00 | 16 |
| stroke 84 | 13 % → 0 % | 197.6 px | 0.00 | 0.00 | 22 |
| stroke 85 | 27 % → 0 % | 285.2 px | 0.00 | 0.00 | 48 |
| stroke 86 | 14 % → 0 % | 241.6 px | 0.00 | 0.00 | 13 |
| stroke 87 | 29 % → 0 % | 360.3 px | 0.00 | 0.00 | 25 |
| stroke 88 | 23 % → 0 % | 430.5 px | 0.00 | 0.00 | 21 |
| stroke 89 | 17 % → 0 % | 268.2 px | 0.00 | 0.00 | 37 |
| stroke 90 | 29 % → 0 % | 222.2 px | 0.00 | 0.00 | 54 |
| stroke 91 | 38 % → 0 % | 225.1 px | 0.00 | 0.00 | 109 |
| stroke 92 | 22 % → 0 % | 369.4 px | 0.00 | 0.00 | 29 |
| stroke 93 | 33 % → 0 % | 210.3 px | 0.00 | 0.00 | 65 |
| stroke 94 | 43 % → 0 % | 294.6 px | 0.00 | 0.00 | 71 |
| stroke 95 | 27 % → 0 % | 284.3 px | 0.00 | 0.00 | 44 |
| stroke 96 | 37 % → 0 % | 168.7 px | 0.00 | 0.00 | 170 |
| stroke 97 | 41 % → 0 % | 468.5 px | 0.00 | 0.00 | 78 |
| stroke 98 | 49 % → 0 % | 279.8 px | 0.00 | 0.00 | 90 |
| stroke 99 | 43 % → 0 % | 689.3 px | 0.00 | 0.00 | 19 |
| stroke 100 | 18 % → 0 % | 215.2 px | 0.00 | 0.00 | 21 |
| stroke 101 | 25 % → 0 % | 280.6 px | 0.00 | 0.00 | 36 |
| stroke 102 | 25 % → 0 % | 405.5 px | 0.00 | 0.00 | 24 |
| stroke 103 | 2 % → 14 % | 28.7 px | 0.48 | 8.56 | 46 |
| stroke 104 | 1 % → 17 % | 29.8 px | 0.46 | 12.35 | 26 |
| stroke 105 | 1 % → 13 % | 25.0 px | 0.48 | 10.49 | 50 |
| stroke 106 | 3 % → 7 % | 67.2 px | 0.45 | 2.75 | 15 |
| stroke 107 | 5 % → 0 % | 53.9 px | 0.46 | 0.01 | 48 |
| stroke 108 | 1 % → 0 % | 26.9 px | 0.00 | 0.00 | 4 |
| stroke 109 | 5 % → 0 % | 79.3 px | 0.00 | 0.00 | 25 |
| stroke 110 | 4 % → 0 % | 75.1 px | 0.00 | 0.00 | 13 |
| stroke 111 | 4 % → 0 % | 124.6 px | 0.00 | 0.00 | 4 |
| stroke 112 | 5 % → 39 % | 47.5 px | 0.48 | 7.19 | 25 |
| stroke 113 | 8 % → 39 % | 81.7 px | 0.48 | 4.82 | 37 |
| stroke 114 | 11 % → 41 % | 95.5 px | 0.48 | 3.86 | 43 |
| stroke 115 | 12 % → 41 % | 126.9 px | 0.48 | 3.27 | 57 |
| stroke 116 | 15 % → 43 % | 133.7 px | 0.48 | 2.93 | 81 |
| stroke 117 | 16 % → 45 % | 134.8 px | 0.48 | 2.75 | 90 |
| stroke 118 | 19 % → 45 % | 148.3 px | 0.48 | 2.42 | 100 |
| stroke 119 | 20 % → 41 % | 150.7 px | 0.48 | 2.02 | 129 |
| stroke 120 | 24 % → 32 % | 203.9 px | 0.48 | 1.37 | 86 |
| stroke 121 | 25 % → 29 % | 251.1 px | 0.48 | 1.15 | 57 |
| stroke 122 | 3 % → 38 % | 46.7 px | 0.47 | 13.95 | 17 |
| stroke 123 | 5 % → 42 % | 68.2 px | 0.47 | 7.71 | 75 |
| stroke 124 | 8 % → 43 % | 82.9 px | 0.47 | 5.20 | 54 |
| stroke 125 | 11 % → 37 % | 175.8 px | 0.47 | 3.26 | 31 |
| stroke 126 | 14 % → 36 % | 229.9 px | 0.47 | 2.64 | 18 |
| stroke 127 | 2 % → 66 % | 46.8 px | 0.48 | 29.73 | 49 |
| stroke 128 | 5 % → 64 % | 59.4 px | 0.48 | 13.39 | 111 |
| stroke 129 | 7 % → 59 % | 86.5 px | 0.48 | 8.07 | 81 |
| stroke 130 | 10 % → 53 % | 148.1 px | 0.48 | 5.19 | 56 |
| stroke 131 | 12 % → 47 % | 179.2 px | 0.48 | 3.84 | 80 |
| stroke 132 | 14 % → 40 % | 188.5 px | 0.48 | 2.81 | 71 |
| stroke 133 | 16 % → 15 % | 298.2 px | 0.48 | 0.96 | 28 |
| stroke 134 | 13 % → 12 % | 203.2 px | 0.48 | 0.93 | 45 |
| stroke 135 | 11 % → 9 % | 164.4 px | 0.49 | 0.82 | 42 |
| stroke 136 | 10 % → 7 % | 153.9 px | 0.49 | 0.67 | 44 |
| stroke 137 | 12 % → 3 % | 204.4 px | 0.51 | 0.27 | 49 |
| stroke 138 | 13 % → 1 % | 188.8 px | 0.51 | 0.05 | 64 |
| stroke 139 | 15 % → 0 % | 220.9 px | 0.00 | 0.00 | 74 |
| stroke 140 | 14 % → 0 % | 291.1 px | 0.00 | 0.00 | 42 |
| stroke 141 | 14 % → 0 % | 215.0 px | 0.00 | 0.00 | 63 |
| stroke 142 | 14 % → 0 % | 186.9 px | 0.00 | 0.00 | 60 |
| stroke 143 | 15 % → 0 % | 197.1 px | 0.00 | 0.00 | 57 |
| stroke 144 | 6 % → 0 % | 89.2 px | 0.00 | 0.00 | 54 |
| stroke 145 | 5 % → 0 % | 67.6 px | 0.00 | 0.00 | 42 |
| stroke 146 | 9 % → 0 % | 114.5 px | 0.00 | 0.00 | 39 |
| stroke 147 | 11 % → 0 % | 66.5 px | 0.00 | 0.00 | 81 |
| stroke 148 | 16 % → 0 % | 83.6 px | 0.00 | 0.00 | 101 |
| stroke 149 | 13 % → 0 % | 195.3 px | 0.00 | 0.00 | 50 |
| stroke 150 | 13 % → 0 % | 268.5 px | 0.00 | 0.00 | 45 |
| stroke 151 | 20 % → 0 % | 474.7 px | 0.00 | 0.00 | 26 |
| stroke 152 | 6 % → 0 % | 45.7 px | 0.00 | 0.00 | 87 |
| stroke 153 | 10 % → 0 % | 75.7 px | 0.00 | 0.00 | 111 |
| stroke 154 | 15 % → 0 % | 110.5 px | 0.00 | 0.00 | 98 |
| stroke 155 | 22 % → 0 % | 167.0 px | 0.00 | 0.00 | 81 |
| stroke 156 | 30 % → 0 % | 263.8 px | 0.00 | 0.00 | 85 |
| stroke 157 | 37 % → 0 % | 245.8 px | 0.00 | 0.00 | 77 |
| stroke 158 | 39 % → 0 % | 202.4 px | 0.00 | 0.00 | 83 |
| stroke 159 | 7 % → 41 % | 27.3 px | 0.48 | 5.60 | 102 |
| stroke 160 | 13 % → 29 % | 215.0 px | 0.48 | 2.25 | 11 |
| stroke 161 | 10 % → 45 % | 94.3 px | 0.48 | 4.58 | 50 |
| stroke 162 | 16 % → 38 % | 130.7 px | 0.47 | 2.39 | 27 |
| stroke 163 | 13 % → 47 % | 101.3 px | 0.48 | 3.71 | 70 |
| stroke 164 | 20 % → 40 % | 186.7 px | 0.47 | 1.98 | 34 |
| stroke 165 | 18 % → 47 % | 583.4 px | 0.47 | 2.62 | 13 |
| stroke 166 | 15 % → 55 % | 177.7 px | 0.48 | 3.69 | 33 |
| stroke 167 | 22 % → 41 % | 219.3 px | 0.47 | 1.84 | 30 |
| stroke 168 | 20 % → 47 % | 548.0 px | 0.47 | 2.28 | 32 |
| stroke 169 | 17 % → 55 % | 327.8 px | 0.48 | 3.18 | 22 |
| stroke 170 | 25 % → 41 % | 354.5 px | 0.47 | 1.64 | 25 |
| stroke 171 | 23 % → 48 % | 595.6 px | 0.47 | 2.12 | 29 |
| stroke 172 | 18 % → 56 % | 650.3 px | 0.48 | 3.14 | 5 |
| stroke 173 | 27 % → 44 % | 363.0 px | 0.47 | 1.61 | 20 |
| stroke 174 | 25 % → 50 % | 814.4 px | 0.47 | 2.04 | 24 |
| stroke 175 | 17 % → 60 % | 261.6 px | 0.48 | 3.47 | 32 |
| stroke 176 | 29 % → 47 % | 520.8 px | 0.47 | 1.62 | 24 |
| stroke 177 | 27 % → 54 % | 1307.1 px | 0.47 | 1.97 | 19 |
| stroke 178 | 19 % → 61 % | 368.1 px | 0.48 | 3.27 | 20 |
| stroke 179 | 29 % → 48 % | 1205.1 px | 0.47 | 1.64 | 10 |
| stroke 180 | 20 % → 67 % | 110.6 px | 0.48 | 3.43 | 75 |
| stroke 181 | 24 % → 67 % | 191.0 px | 0.48 | 2.82 | 42 |
| stroke 182 | 25 % → 67 % | 220.0 px | 0.48 | 2.64 | 54 |
| stroke 183 | 29 % → 62 % | 816.5 px | 0.48 | 2.11 | 13 |
| stroke 184 | 18 % → 69 % | 688.8 px | 0.48 | 3.87 | 3 |
| stroke 185 | 17 % → 69 % | 595.5 px | 0.48 | 4.11 | 10 |
| stroke 186 | 16 % → 68 % | 577.3 px | 0.48 | 4.36 | 4 |
| stroke 187 | 14 % → 66 % | 643.4 px | 0.48 | 4.67 | 5 |
| stroke 188 | 5 % → 56 % | 85.4 px | 0.48 | 11.74 | 18 |
| stroke 189 | 7 % → 55 % | 97.3 px | 0.48 | 7.98 | 25 |
| stroke 190 | 8 % → 55 % | 136.0 px | 0.48 | 6.89 | 22 |
| stroke 191 | 9 % → 55 % | 179.3 px | 0.48 | 6.37 | 19 |
| stroke 192 | 10 % → 59 % | 410.9 px | 0.48 | 6.18 | 19 |
| stroke 193 | 10 % → 60 % | 210.0 px | 0.49 | 6.12 | 16 |
| stroke 194 | 9 % → 54 % | 144.6 px | 0.49 | 6.25 | 25 |
| stroke 195 | 8 % → 47 % | 103.6 px | 0.49 | 6.21 | 62 |
| stroke 196 | 7 % → 42 % | 85.9 px | 0.49 | 5.70 | 54 |
| stroke 197 | 8 % → 41 % | 115.8 px | 0.49 | 5.21 | 36 |
| stroke 198 | 20 % → 48 % | 327.0 px | 0.47 | 2.32 | 42 |
| stroke 199 | 17 % → 40 % | 196.8 px | 0.47 | 2.44 | 46 |
| stroke 200 | 15 % → 39 % | 188.1 px | 0.47 | 2.59 | 49 |
| stroke 201 | 14 % → 37 % | 166.1 px | 0.47 | 2.72 | 48 |
| stroke 202 | 3 % → 49 % | 25.8 px | 0.48 | 18.44 | 18 |
| stroke 203 | 4 % → 43 % | 52.8 px | 0.48 | 10.02 | 26 |
| stroke 204 | 1 % → 65 % | 25.7 px | 0.48 | 44.29 | 35 |
| stroke 205 | 2 % → 31 % | 55.7 px | 0.48 | 14.51 | 15 |
| stroke 206 | 5 % → 57 % | 39.1 px | 0.48 | 11.06 | 60 |
| stroke 207 | 8 % → 56 % | 36.6 px | 0.49 | 7.41 | 117 |
| stroke 208 | 7 % → 59 % | 110.1 px | 0.48 | 8.18 | 31 |
| stroke 209 | 14 % → 62 % | 87.7 px | 0.48 | 4.54 | 121 |
| stroke 210 | 18 % → 53 % | 166.8 px | 0.48 | 3.00 | 66 |
| stroke 211 | 9 % → 59 % | 229.5 px | 0.48 | 6.52 | 32 |
| stroke 212 | 16 % → 66 % | 340.5 px | 0.48 | 4.04 | 20 |
| stroke 213 | 21 % → 69 % | 219.5 px | 0.48 | 3.26 | 50 |
| stroke 214 | 14 % → 61 % | 203.7 px | 0.48 | 4.29 | 44 |
| stroke 215 | 22 % → 66 % | 323.4 px | 0.48 | 2.95 | 63 |
| stroke 216 | 25 % → 66 % | 296.3 px | 0.48 | 2.64 | 55 |
| stroke 217 | 21 % → 49 % | 487.4 px | 0.48 | 2.37 | 36 |
| stroke 218 | 24 % → 63 % | 257.7 px | 0.48 | 2.67 | 59 |
| stroke 219 | 28 % → 59 % | 287.0 px | 0.48 | 2.15 | 58 |
| stroke 220 | 24 % → 49 % | 541.1 px | 0.48 | 2.02 | 26 |
| stroke 221 | 27 % → 65 % | 600.9 px | 0.48 | 2.41 | 21 |
| stroke 222 | 32 % → 68 % | 676.3 px | 0.48 | 2.14 | 25 |
| stroke 223 | 31 % → 60 % | 405.1 px | 0.48 | 1.93 | 44 |
| stroke 224 | 27 % → 51 % | 463.8 px | 0.48 | 1.86 | 30 |
| stroke 225 | 31 % → 68 % | 808.6 px | 0.48 | 2.17 | 26 |
| stroke 226 | 31 % → 53 % | 248.5 px | 0.48 | 1.71 | 129 |
| stroke 227 | 36 % → 69 % | 1143.5 px | 0.48 | 1.93 | 19 |
| stroke 228 | 34 % → 54 % | 330.2 px | 0.48 | 1.59 | 71 |
| stroke 229 | 38 % → 64 % | 548.8 px | 0.48 | 1.69 | 65 |
| stroke 230 | 34 % → 54 % | 568.1 px | 0.49 | 1.57 | 47 |
| stroke 231 | 36 % → 59 % | 702.8 px | 0.48 | 1.64 | 37 |
| stroke 232 | 30 % → 44 % | 537.7 px | 0.49 | 1.46 | 49 |
| stroke 233 | 32 % → 54 % | 520.5 px | 0.48 | 1.66 | 80 |
| stroke 234 | 27 % → 37 % | 533.8 px | 0.49 | 1.39 | 31 |
| stroke 235 | 29 % → 48 % | 554.3 px | 0.48 | 1.68 | 32 |
| stroke 236 | 27 % → 35 % | 434.8 px | 0.49 | 1.30 | 60 |
| stroke 237 | 25 % → 34 % | 190.1 px | 0.48 | 1.39 | 126 |
| stroke 238 | 28 % → 36 % | 628.6 px | 0.48 | 1.28 | 29 |
| stroke 239 | 32 % → 33 % | 701.2 px | 0.49 | 1.04 | 36 |
| stroke 240 | 14 % → 41 % | 111.3 px | 0.48 | 2.87 | 42 |
| stroke 241 | 15 % → 46 % | 299.5 px | 0.47 | 3.05 | 36 |
| stroke 242 | 15 % → 49 % | 540.4 px | 0.47 | 3.18 | 14 |
| stroke 243 | 25 % → 56 % | 825.2 px | 0.47 | 2.28 | 29 |
| stroke 244 | 19 % → 48 % | 198.2 px | 0.47 | 2.48 | 72 |
| stroke 245 | 35 % → 60 % | 654.6 px | 0.47 | 1.74 | 27 |
| stroke 246 | 31 % → 51 % | 243.1 px | 0.48 | 1.63 | 87 |
| stroke 247 | 32 % → 48 % | 214.4 px | 0.47 | 1.49 | 126 |
| stroke 248 | 25 % → 42 % | 240.4 px | 0.47 | 1.69 | 69 |
| stroke 249 | 41 % → 56 % | 1353.1 px | 0.48 | 1.36 | 35 |
| stroke 250 | 26 % → 41 % | 376.3 px | 0.47 | 1.53 | 57 |
| stroke 251 | 41 % → 53 % | 1057.5 px | 0.47 | 1.29 | 30 |
| stroke 252 | 28 % → 39 % | 422.2 px | 0.47 | 1.43 | 26 |
| stroke 253 | 39 % → 49 % | 868.9 px | 0.47 | 1.26 | 22 |
| stroke 254 | 34 % → 37 % | 211.3 px | 0.47 | 1.07 | 173 |
| stroke 255 | 30 % → 31 % | 449.5 px | 0.47 | 1.04 | 68 |

Numbers say: wet paint spreads well beyond the stroke.

## Refs v3 · #14 HW olive totem — own sheet
own sheet 800 × 1040 · Gouache 1.00 + turpentine 30 % · 41 px · 60.2 s

![Refs v3 · #14 HW olive totem — own sheet](Refs-v3-14-HW-olive-totem-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 5 % → 0 % | 43.1 px | 0.00 | 0.00 | 32 |
| stroke 2 | 11 % → 0 % | 60.0 px | 0.00 | 0.00 | 44 |
| stroke 3 | 17 % → 0 % | 144.0 px | 0.00 | 0.00 | 27 |
| stroke 4 | 8 % → 0 % | 41.7 px | 0.00 | 0.00 | 27 |
| stroke 5 | 16 % → 0 % | 65.0 px | 0.00 | 0.00 | 50 |
| stroke 6 | 24 % → 0 % | 82.6 px | 0.00 | 0.00 | 71 |
| stroke 7 | 35 % → 0 % | 129.1 px | 0.00 | 0.00 | 52 |
| stroke 8 | 37 % → 2 % | 133.9 px | 0.25 | 0.06 | 64 |
| stroke 9 | 34 % → 7 % | 119.1 px | 0.25 | 0.20 | 46 |
| stroke 10 | 30 % → 5 % | 85.2 px | 0.25 | 0.17 | 82 |
| stroke 11 | 29 % → 4 % | 101.8 px | 0.25 | 0.15 | 78 |
| stroke 12 | 23 % → 0 % | 167.8 px | 0.00 | 0.00 | 15 |
| stroke 13 | 18 % → 0 % | 122.7 px | 0.00 | 0.00 | 30 |
| stroke 14 | 8 % → 0 % | 68.2 px | 0.00 | 0.00 | 22 |
| stroke 15 | 15 % → 0 % | 72.9 px | 0.00 | 0.00 | 40 |
| stroke 16 | 11 % → 0 % | 106.6 px | 0.00 | 0.00 | 17 |
| stroke 17 | 23 % → 0 % | 126.9 px | 0.00 | 0.00 | 41 |
| stroke 18 | 21 % → 0 % | 106.2 px | 0.00 | 0.00 | 49 |
| stroke 19 | 31 % → 0 % | 243.2 px | 0.00 | 0.00 | 26 |
| stroke 20 | 30 % → 0 % | 221.8 px | 0.00 | 0.00 | 35 |
| stroke 21 | 35 % → 0 % | 271.8 px | 0.00 | 0.00 | 31 |
| stroke 22 | 32 % → 0 % | 149.4 px | 0.00 | 0.00 | 87 |
| stroke 23 | 28 % → 0 % | 119.3 px | 0.00 | 0.00 | 75 |
| stroke 24 | 30 % → 0 % | 231.8 px | 0.00 | 0.00 | 25 |
| stroke 25 | 15 % → 0 % | 78.3 px | 0.00 | 0.00 | 36 |
| stroke 26 | 15 % → 0 % | 69.2 px | 0.00 | 0.00 | 55 |
| stroke 27 | 19 % → 0 % | 96.9 px | 0.00 | 0.00 | 46 |
| stroke 28 | 20 % → 2 % | 57.9 px | 0.21 | 0.08 | 136 |
| stroke 29 | 14 % → 0 % | 102.9 px | 0.00 | 0.00 | 24 |
| stroke 30 | 29 % → 0 % | 108.4 px | 0.00 | 0.00 | 89 |
| stroke 31 | 27 % → 4 % | 106.0 px | 0.21 | 0.15 | 80 |
| stroke 32 | 22 % → 5 % | 166.6 px | 0.21 | 0.24 | 20 |
| stroke 33 | 28 % → 0 % | 84.3 px | 0.00 | 0.00 | 190 |
| stroke 34 | 34 % → 3 % | 107.1 px | 0.21 | 0.10 | 123 |
| stroke 35 | 44 % → 0 % | 299.5 px | 0.00 | 0.00 | 34 |
| stroke 36 | 42 % → 3 % | 123.9 px | 0.21 | 0.08 | 154 |
| stroke 37 | 39 % → 0 % | 313.7 px | 0.00 | 0.00 | 22 |
| stroke 38 | 45 % → 5 % | 274.1 px | 0.21 | 0.12 | 40 |
| stroke 39 | 40 % → 5 % | 177.4 px | 0.21 | 0.11 | 72 |
| stroke 40 | 32 % → 0 % | 162.3 px | 0.00 | 0.00 | 69 |
| stroke 41 | 40 % → 4 % | 135.4 px | 0.21 | 0.09 | 109 |
| stroke 42 | 37 % → 2 % | 79.4 px | 0.21 | 0.05 | 503 |
| stroke 43 | 43 % → 1 % | 90.1 px | 0.21 | 0.03 | 469 |
| stroke 44 | 50 % → 0 % | 108.5 px | 0.20 | 0.01 | 351 |
| stroke 45 | 44 % → 0 % | 270.3 px | 0.00 | 0.00 | 65 |
| stroke 46 | 55 % → 0 % | 254.4 px | 0.00 | 0.00 | 77 |
| stroke 47 | 47 % → 0 % | 241.3 px | 0.00 | 0.00 | 54 |
| stroke 48 | 46 % → 0 % | 236.9 px | 0.00 | 0.00 | 49 |
| stroke 49 | 41 % → 0 % | 321.8 px | 0.00 | 0.00 | 31 |
| stroke 50 | 7 % → 0 % | 23.7 px | 0.00 | 0.00 | 52 |
| stroke 51 | 2 % → 0 % | 21.6 px | 0.00 | 0.00 | 16 |
| stroke 52 | 7 % → 0 % | 45.9 px | 0.00 | 0.00 | 28 |
| stroke 53 | 3 % → 0 % | 38.0 px | 0.00 | 0.00 | 29 |
| stroke 54 | 6 % → 1 % | 41.6 px | 0.24 | 0.11 | 27 |
| stroke 55 | 3 % → 0 % | 24.9 px | 0.00 | 0.00 | 10 |
| stroke 56 | 5 % → 0 % | 23.6 px | 0.00 | 0.00 | 25 |
| stroke 57 | 2 % → 0 % | 20.8 px | 0.00 | 0.00 | 9 |
| stroke 58 | 4 % → 0 % | 26.3 px | 0.00 | 0.00 | 24 |
| stroke 59 | 3 % → 0 % | 23.6 px | 0.00 | 0.00 | 9 |
| stroke 60 | 20 % → 0 % | 48.4 px | 0.00 | 0.00 | 167 |
| stroke 61 | 26 % → 0 % | 164.3 px | 0.00 | 0.00 | 35 |
| stroke 62 | 33 % → 0 % | 140.0 px | 0.00 | 0.00 | 66 |
| stroke 63 | 35 % → 0 % | 159.4 px | 0.00 | 0.00 | 93 |
| stroke 64 | 28 % → 0 % | 144.8 px | 0.00 | 0.00 | 81 |
| stroke 65 | 29 % → 0 % | 74.0 px | 0.00 | 0.00 | 430 |
| stroke 66 | 31 % → 0 % | 101.1 px | 0.00 | 0.00 | 267 |
| stroke 67 | 40 % → 0 % | 106.1 px | 0.00 | 0.00 | 399 |
| stroke 68 | 24 % → 0 % | 145.6 px | 0.00 | 0.00 | 61 |
| stroke 69 | 54 % → 0 % | 136.6 px | 0.00 | 0.00 | 464 |
| stroke 70 | 50 % → 0 % | 117.6 px | 0.00 | 0.00 | 516 |
| stroke 71 | 43 % → 0 % | 217.9 px | 0.00 | 0.00 | 113 |
| stroke 72 | 59 % → 0 % | 176.6 px | 0.00 | 0.00 | 245 |
| stroke 73 | 47 % → 0 % | 156.8 px | 0.00 | 0.00 | 238 |
| stroke 74 | 34 % → 0 % | 175.3 px | 0.00 | 0.00 | 116 |
| stroke 75 | 58 % → 0 % | 315.3 px | 0.00 | 0.00 | 78 |
| stroke 76 | 59 % → 0 % | 162.1 px | 0.00 | 0.00 | 305 |
| stroke 77 | 44 % → 3 % | 147.1 px | 0.25 | 0.06 | 243 |
| stroke 78 | 56 % → 0 % | 225.0 px | 0.00 | 0.00 | 245 |
| stroke 79 | 55 % → 0 % | 285.8 px | 0.00 | 0.00 | 84 |
| stroke 80 | 47 % → 4 % | 313.6 px | 0.25 | 0.09 | 70 |
| stroke 81 | 47 % → 0 % | 252.4 px | 0.00 | 0.00 | 114 |
| stroke 82 | 23 % → 4 % | 168.4 px | 0.25 | 0.19 | 68 |
| stroke 83 | 27 % → 0 % | 140.6 px | 0.00 | 0.00 | 78 |
| stroke 84 | 20 % → 0 % | 123.6 px | 0.00 | 0.00 | 71 |
| stroke 85 | 20 % → 0 % | 127.7 px | 0.00 | 0.00 | 77 |
| stroke 86 | 23 % → 0 % | 84.0 px | 0.00 | 0.00 | 162 |
| stroke 87 | 33 % → 0 % | 256.3 px | 0.00 | 0.00 | 48 |
| stroke 88 | 12 % → 0 % | 56.5 px | 0.00 | 0.00 | 91 |
| stroke 89 | 21 % → 3 % | 72.3 px | 0.21 | 0.16 | 169 |
| stroke 90 | 6 % → 0 % | 28.5 px | 0.00 | 0.00 | 34 |
| stroke 91 | 6 % → 9 % | 33.2 px | 0.25 | 1.40 | 22 |
| stroke 92 | 5 % → 0 % | 30.7 px | 0.00 | 0.00 | 36 |
| stroke 93 | 23 % → 5 % | 66.9 px | 0.25 | 0.23 | 192 |
| stroke 94 | 39 % → 5 % | 105.8 px | 0.25 | 0.12 | 276 |
| stroke 95 | 46 % → 0 % | 121.7 px | 0.00 | 0.00 | 233 |
| stroke 96 | 48 % → 0 % | 124.0 px | 0.00 | 0.00 | 291 |
| stroke 97 | 49 % → 0 % | 127.8 px | 0.00 | 0.00 | 294 |
| stroke 98 | 50 % → 0 % | 139.0 px | 0.00 | 0.00 | 279 |
| stroke 99 | 53 % → 0 % | 166.9 px | 0.00 | 0.00 | 138 |
| stroke 100 | 25 % → 0 % | 68.8 px | 0.00 | 0.00 | 229 |
| stroke 101 | 43 % → 0 % | 112.3 px | 0.00 | 0.00 | 242 |
| stroke 102 | 61 % → 0 % | 116.3 px | 0.00 | 0.00 | 442 |
| stroke 103 | 20 % → 0 % | 72.4 px | 0.00 | 0.00 | 137 |
| stroke 104 | 3 % → 0 % | 23.9 px | 0.00 | 0.00 | 23 |
| stroke 105 | 4 % → 0 % | 43.9 px | 0.00 | 0.00 | 37 |
| stroke 106 | 7 % → 0 % | 84.1 px | 0.00 | 0.00 | 12 |
| stroke 107 | 7 % → 0 % | 38.1 px | 0.00 | 0.00 | 48 |
| stroke 108 | 12 % → 0 % | 77.7 px | 0.00 | 0.00 | 44 |
| stroke 109 | 5 % → 0 % | 38.9 px | 0.00 | 0.00 | 22 |
| stroke 110 | 9 % → 0 % | 91.7 px | 0.00 | 0.00 | 20 |
| stroke 111 | 12 % → 0 % | 50.4 px | 0.00 | 0.00 | 60 |
| stroke 112 | 18 % → 0 % | 65.9 px | 0.00 | 0.00 | 112 |
| stroke 113 | 20 % → 0 % | 76.8 px | 0.00 | 0.00 | 107 |
| stroke 114 | 19 % → 0 % | 96.3 px | 0.00 | 0.00 | 71 |
| stroke 115 | 30 % → 0 % | 278.6 px | 0.00 | 0.00 | 36 |
| stroke 116 | 29 % → 0 % | 126.9 px | 0.20 | 0.00 | 98 |
| stroke 117 | 18 % → 0 % | 119.9 px | 0.20 | 0.00 | 42 |
| stroke 118 | 21 % → 0 % | 123.6 px | 0.00 | 0.00 | 51 |
| stroke 119 | 24 % → 0 % | 129.8 px | 0.00 | 0.00 | 74 |
| stroke 120 | 18 % → 0 % | 160.2 px | 0.00 | 0.00 | 25 |
| stroke 121 | 18 % → 0 % | 125.5 px | 0.00 | 0.00 | 35 |
| stroke 122 | 28 % → 0 % | 250.1 px | 0.00 | 0.00 | 38 |
| stroke 123 | 23 % → 0 % | 124.2 px | 0.00 | 0.00 | 37 |
| stroke 124 | 29 % → 0 % | 129.4 px | 0.00 | 0.00 | 109 |
| stroke 125 | 33 % → 0 % | 128.9 px | 0.00 | 0.00 | 35 |
| stroke 126 | 34 % → 0 % | 180.6 px | 0.00 | 0.00 | 77 |
| stroke 127 | 40 % → 0 % | 107.8 px | 0.00 | 0.00 | 127 |
| stroke 128 | 45 % → 0 % | 129.9 px | 0.00 | 0.00 | 148 |
| stroke 129 | 50 % → 0 % | 232.7 px | 0.00 | 0.00 | 96 |
| stroke 130 | 39 % → 0 % | 180.5 px | 0.00 | 0.00 | 65 |
| stroke 131 | 36 % → 0 % | 84.2 px | 0.00 | 0.00 | 243 |
| stroke 132 | 51 % → 0 % | 353.0 px | 0.00 | 0.00 | 21 |
| stroke 133 | 52 % → 0 % | 367.6 px | 0.00 | 0.00 | 34 |
| stroke 134 | 35 % → 0 % | 159.8 px | 0.00 | 0.00 | 135 |
| stroke 135 | 31 % → 0 % | 261.6 px | 0.00 | 0.00 | 36 |
| stroke 136 | 12 % → 0 % | 89.8 px | 0.00 | 0.00 | 25 |
| stroke 137 | 27 % → 0 % | 112.7 px | 0.00 | 0.00 | 107 |
| stroke 138 | 26 % → 0 % | 81.3 px | 0.00 | 0.00 | 157 |
| stroke 139 | 32 % → 0 % | 100.8 px | 0.00 | 0.00 | 150 |
| stroke 140 | 40 % → 0 % | 123.5 px | 0.00 | 0.00 | 120 |
| stroke 141 | 58 % → 0 % | 217.5 px | 0.00 | 0.00 | 71 |
| stroke 142 | 32 % → 1 % | 252.7 px | 0.22 | 0.05 | 36 |
| stroke 143 | 25 % → 2 % | 217.2 px | 0.21 | 0.09 | 45 |
| stroke 144 | 13 % → 0 % | 48.2 px | 0.00 | 0.00 | 104 |
| stroke 145 | 20 % → 0 % | 66.9 px | 0.00 | 0.00 | 153 |
| stroke 146 | 4 % → 5 % | 24.1 px | 0.25 | 1.48 | 32 |
| stroke 147 | 3 % → 6 % | 28.4 px | 0.21 | 1.68 | 27 |

Numbers say: wet paint spreads well beyond the stroke.

## Refs v3 · #15 Ultramarine script — own sheet
own sheet 800 × 1422 · Ink 0.98 · 39 px · 201.5 s

![Refs v3 · #15 Ultramarine script — own sheet](Refs-v3-15-Ultramarine-script-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 3 % → 43 % | 15.6 px | 0.64 | 16.54 | 18 |
| stroke 2 | 4 % → 45 % | 22.3 px | 0.65 | 11.11 | 9 |
| stroke 3 | 11 % → 47 % | 24.7 px | 0.65 | 4.16 | 20 |
| stroke 4 | 15 % → 45 % | 82.2 px | 0.64 | 2.96 | 10 |
| stroke 5 | 18 % → 41 % | 223.9 px | 0.64 | 2.27 | 5 |
| stroke 6 | 19 % → 40 % | 247.8 px | 0.65 | 2.07 | 4 |
| stroke 7 | 19 % → 39 % | 104.0 px | 0.63 | 2.05 | 11 |
| stroke 8 | 29 % → 45 % | 265.3 px | 0.65 | 1.54 | 6 |
| stroke 9 | 3 % → 35 % | 16.0 px | 0.64 | 12.66 | 13 |
| stroke 10 | 5 % → 45 % | 29.3 px | 0.63 | 8.33 | 9 |
| stroke 11 | 5 % → 34 % | 60.6 px | 0.64 | 7.51 | 6 |
| stroke 12 | 9 % → 35 % | 32.2 px | 0.64 | 3.77 | 25 |
| stroke 13 | 14 % → 36 % | 98.7 px | 0.63 | 2.59 | 22 |
| stroke 14 | 19 % → 37 % | 121.7 px | 0.63 | 1.94 | 21 |
| stroke 15 | 21 % → 39 % | 105.0 px | 0.63 | 1.91 | 16 |
| stroke 16 | 12 % → 45 % | 100.6 px | 0.63 | 3.88 | 10 |
| stroke 17 | 5 % → 51 % | 23.8 px | 0.65 | 10.65 | 5 |
| stroke 18 | 12 % → 49 % | 53.9 px | 0.65 | 4.09 | 13 |
| stroke 19 | 17 % → 42 % | 99.5 px | 0.63 | 2.49 | 11 |
| stroke 20 | 19 % → 47 % | 246.3 px | 0.64 | 2.50 | 6 |
| stroke 21 | 20 % → 45 % | 256.0 px | 0.63 | 2.18 | 5 |
| stroke 22 | 24 % → 49 % | 67.7 px | 0.63 | 2.02 | 36 |
| stroke 23 | 38 % → 51 % | 399.9 px | 0.64 | 1.33 | 3 |
| stroke 24 | 2 % → 36 % | 18.5 px | 0.63 | 19.39 | 3 |
| stroke 25 | 2 % → 52 % | 39.1 px | 0.65 | 21.98 | 3 |
| stroke 26 | 4 % → 65 % | 19.5 px | 0.65 | 15.50 | 14 |
| stroke 27 | 3 % → 48 % | 37.9 px | 0.64 | 14.71 | 3 |
| stroke 28 | 28 % → 62 % | 77.1 px | 0.65 | 2.17 | 17 |
| stroke 29 | 4 % → 54 % | 31.8 px | 0.64 | 13.47 | 7 |
| stroke 30 | 8 % → 43 % | 41.6 px | 0.63 | 5.67 | 17 |
| stroke 31 | 11 % → 50 % | 102.0 px | 0.63 | 4.41 | 8 |
| stroke 32 | 17 % → 43 % | 141.6 px | 0.64 | 2.62 | 11 |
| stroke 33 | 11 % → 38 % | 87.3 px | 0.64 | 3.40 | 7 |
| stroke 34 | 9 % → 40 % | 59.2 px | 0.64 | 4.66 | 11 |
| stroke 35 | 15 % → 45 % | 147.9 px | 0.63 | 2.98 | 5 |
| stroke 36 | 10 % → 40 % | 51.8 px | 0.64 | 3.88 | 17 |
| stroke 37 | 19 % → 62 % | 103.2 px | 0.65 | 3.33 | 11 |
| stroke 38 | 17 % → 39 % | 82.1 px | 0.63 | 2.28 | 16 |
| stroke 39 | 27 % → 54 % | 150.1 px | 0.64 | 1.98 | 13 |
| stroke 40 | 30 % → 56 % | 216.4 px | 0.64 | 1.83 | 9 |
| stroke 41 | 33 % → 55 % | 528.8 px | 0.64 | 1.69 | 8 |
| stroke 42 | 29 % → 50 % | 564.5 px | 0.64 | 1.68 | 7 |
| stroke 43 | 25 % → 50 % | 145.1 px | 0.64 | 1.96 | 11 |
| stroke 44 | 26 % → 52 % | 150.8 px | 0.64 | 1.98 | 23 |
| stroke 45 | 21 % → 42 % | 259.4 px | 0.65 | 2.00 | 9 |
| stroke 46 | 28 % → 60 % | 257.3 px | 0.65 | 2.13 | 8 |
| stroke 47 | 37 % → 56 % | 121.3 px | 0.65 | 1.51 | 27 |
| stroke 48 | 29 % → 46 % | 377.2 px | 0.64 | 1.57 | 3 |
| stroke 49 | 30 % → 46 % | 336.4 px | 0.65 | 1.50 | 13 |
| stroke 50 | 31 % → 43 % | 377.2 px | 0.64 | 1.36 | 12 |
| stroke 51 | 37 % → 50 % | 200.7 px | 0.65 | 1.36 | 11 |
| stroke 52 | 20 % → 54 % | 256.0 px | 0.65 | 2.77 | 9 |
| stroke 53 | 11 % → 50 % | 202.7 px | 0.62 | 4.76 | 3 |
| stroke 54 | 5 % → 55 % | 29.9 px | 0.64 | 10.96 | 24 |
| stroke 55 | 5 % → 56 % | 35.2 px | 0.66 | 11.79 | 11 |
| stroke 56 | 10 % → 49 % | 46.9 px | 0.63 | 5.01 | 18 |
| stroke 57 | 15 % → 45 % | 111.6 px | 0.65 | 3.13 | 44 |
| stroke 58 | 11 % → 62 % | 83.9 px | 0.65 | 5.63 | 12 |
| stroke 59 | 29 % → 60 % | 260.5 px | 0.66 | 2.10 | 6 |
| stroke 60 | 11 % → 47 % | 85.4 px | 0.66 | 4.18 | 8 |
| stroke 61 | 10 % → 40 % | 66.2 px | 0.66 | 3.93 | 11 |
| stroke 62 | 34 % → 60 % | 396.8 px | 0.65 | 1.76 | 5 |
| stroke 63 | 14 % → 53 % | 164.9 px | 0.65 | 3.67 | 3 |
| stroke 64 | 15 % → 57 % | 110.7 px | 0.65 | 3.74 | 8 |
| stroke 65 | 28 % → 57 % | 117.7 px | 0.65 | 2.03 | 26 |
| stroke 66 | 12 % → 55 % | 151.6 px | 0.65 | 4.74 | 5 |
| stroke 67 | 20 % → 53 % | 119.7 px | 0.65 | 2.66 | 12 |
| stroke 68 | 32 % → 54 % | 263.4 px | 0.65 | 1.68 | 16 |
| stroke 69 | 38 % → 50 % | 305.7 px | 0.65 | 1.30 | 14 |
| stroke 70 | 18 % → 53 % | 278.4 px | 0.63 | 2.98 | 5 |
| stroke 71 | 31 % → 51 % | 410.6 px | 0.64 | 1.64 | 4 |
| stroke 72 | 20 % → 56 % | 117.5 px | 0.64 | 2.76 | 11 |
| stroke 73 | 29 % → 50 % | 447.4 px | 0.64 | 1.74 | 5 |
| stroke 74 | 25 % → 58 % | 123.7 px | 0.64 | 2.35 | 47 |
| stroke 75 | 25 % → 59 % | 222.7 px | 0.65 | 2.37 | 9 |
| stroke 76 | 40 % → 55 % | 141.9 px | 0.63 | 1.37 | 23 |
| stroke 77 | 38 % → 49 % | 202.6 px | 0.65 | 1.30 | 11 |
| stroke 78 | 29 % → 44 % | 130.5 px | 0.64 | 1.52 | 16 |
| stroke 79 | 35 % → 53 % | 197.4 px | 0.64 | 1.49 | 8 |
| stroke 80 | 31 % → 52 % | 281.8 px | 0.65 | 1.71 | 8 |
| stroke 81 | 33 % → 49 % | 182.0 px | 0.66 | 1.47 | 11 |
| stroke 82 | 28 % → 58 % | 101.6 px | 0.66 | 2.10 | 24 |
| stroke 83 | 41 % → 51 % | 398.6 px | 0.64 | 1.23 | 8 |
| stroke 84 | 42 % → 51 % | 753.5 px | 0.63 | 1.23 | 3 |
| stroke 85 | 33 % → 67 % | 250.6 px | 0.66 | 2.00 | 7 |
| stroke 86 | 38 % → 61 % | 270.5 px | 0.65 | 1.61 | 16 |
| stroke 87 | 21 % → 56 % | 114.3 px | 0.64 | 2.64 | 9 |
| stroke 88 | 21 % → 55 % | 309.1 px | 0.64 | 2.64 | 2 |
| stroke 89 | 27 % → 54 % | 99.9 px | 0.65 | 2.03 | 32 |
| stroke 90 | 29 % → 55 % | 231.5 px | 0.65 | 1.87 | 5 |
| stroke 91 | 42 % → 56 % | 376.4 px | 0.64 | 1.34 | 9 |
| stroke 92 | 33 % → 68 % | 270.2 px | 0.65 | 2.08 | 12 |
| stroke 93 | 7 % → 64 % | 42.5 px | 0.65 | 8.78 | 20 |
| stroke 94 | 26 % → 64 % | 158.0 px | 0.66 | 2.52 | 26 |
| stroke 95 | 36 % → 68 % | 256.2 px | 0.66 | 1.90 | 9 |
| stroke 96 | 28 % → 61 % | 435.2 px | 0.66 | 2.16 | 2 |
| stroke 97 | 18 % → 54 % | 123.5 px | 0.65 | 2.95 | 9 |
| stroke 98 | 30 % → 59 % | 329.0 px | 0.66 | 1.94 | 7 |
| stroke 99 | 29 % → 56 % | 155.8 px | 0.65 | 1.93 | 25 |
| stroke 100 | 48 % → 65 % | 260.2 px | 0.65 | 1.34 | 11 |
| stroke 101 | 15 % → 49 % | 130.0 px | 0.66 | 3.24 | 9 |
| stroke 102 | 13 % → 49 % | 99.3 px | 0.64 | 3.73 | 14 |
| stroke 103 | 17 % → 46 % | 202.7 px | 0.64 | 2.77 | 4 |
| stroke 104 | 34 % → 57 % | 242.6 px | 0.66 | 1.67 | 21 |
| stroke 105 | 24 % → 56 % | 262.4 px | 0.66 | 2.31 | 13 |
| stroke 106 | 17 % → 61 % | 185.3 px | 0.66 | 3.57 | 12 |
| stroke 107 | 19 % → 46 % | 107.2 px | 0.64 | 2.35 | 47 |
| stroke 108 | 34 % → 55 % | 293.4 px | 0.66 | 1.59 | 4 |
| stroke 109 | 29 % → 51 % | 133.6 px | 0.65 | 1.77 | 15 |
| stroke 110 | 29 % → 58 % | 410.5 px | 0.66 | 1.99 | 9 |
| stroke 111 | 34 % → 51 % | 530.1 px | 0.65 | 1.48 | 4 |
| stroke 112 | 39 % → 53 % | 670.8 px | 0.65 | 1.36 | 14 |
| stroke 113 | 34 % → 50 % | 449.4 px | 0.66 | 1.49 | 36 |
| stroke 114 | 41 % → 49 % | 639.5 px | 0.65 | 1.18 | 3 |
| stroke 115 | 35 % → 47 % | 324.3 px | 0.66 | 1.31 | 10 |
| stroke 116 | 4 % → 61 % | 22.0 px | 0.64 | 17.06 | 45 |
| stroke 117 | 31 % → 63 % | 184.5 px | 0.65 | 2.03 | 24 |
| stroke 118 | 33 % → 61 % | 566.6 px | 0.64 | 1.86 | 3 |
| stroke 119 | 29 % → 68 % | 396.6 px | 0.67 | 2.35 | 3 |
| stroke 120 | 6 % → 50 % | 104.8 px | 0.65 | 7.83 | 11 |
| stroke 121 | 7 % → 62 % | 35.5 px | 0.65 | 8.63 | 47 |
| stroke 122 | 14 % → 39 % | 46.9 px | 0.64 | 2.86 | 39 |
| stroke 123 | 18 % → 63 % | 117.1 px | 0.65 | 3.52 | 18 |
| stroke 124 | 16 % → 60 % | 116.1 px | 0.64 | 3.79 | 19 |
| stroke 125 | 4 % → 57 % | 33.0 px | 0.63 | 13.76 | 13 |
| stroke 126 | 11 % → 57 % | 71.2 px | 0.64 | 5.17 | 44 |
| stroke 127 | 18 % → 66 % | 77.9 px | 0.64 | 3.62 | 35 |
| stroke 128 | 12 % → 62 % | 87.4 px | 0.63 | 4.99 | 6 |
| stroke 129 | 31 % → 66 % | 338.9 px | 0.65 | 2.12 | 16 |
| stroke 130 | 20 % → 55 % | 129.0 px | 0.65 | 2.77 | 14 |
| stroke 131 | 26 % → 64 % | 147.5 px | 0.64 | 2.50 | 14 |
| stroke 132 | 33 % → 60 % | 256.6 px | 0.64 | 1.80 | 24 |
| stroke 133 | 25 % → 59 % | 101.6 px | 0.63 | 2.38 | 48 |
| stroke 134 | 24 % → 53 % | 144.9 px | 0.65 | 2.20 | 16 |
| stroke 135 | 20 % → 59 % | 323.9 px | 0.64 | 2.94 | 4 |
| stroke 136 | 35 % → 61 % | 178.8 px | 0.65 | 1.76 | 19 |
| stroke 137 | 44 % → 63 % | 802.3 px | 0.65 | 1.42 | 2 |
| stroke 138 | 33 % → 61 % | 275.6 px | 0.63 | 1.88 | 20 |
| stroke 139 | 39 % → 61 % | 286.8 px | 0.65 | 1.57 | 13 |
| stroke 140 | 37 % → 63 % | 494.8 px | 0.65 | 1.68 | 11 |
| stroke 141 | 38 % → 66 % | 420.4 px | 0.64 | 1.74 | 24 |
| stroke 142 | 36 % → 53 % | 190.6 px | 0.65 | 1.49 | 23 |
| stroke 143 | 41 % → 63 % | 555.9 px | 0.66 | 1.54 | 10 |
| stroke 144 | 45 % → 62 % | 317.5 px | 0.66 | 1.37 | 13 |
| stroke 145 | 49 % → 62 % | 354.4 px | 0.66 | 1.26 | 21 |
| stroke 146 | 48 % → 61 % | 371.9 px | 0.65 | 1.27 | 13 |
| stroke 147 | 53 % → 58 % | 221.3 px | 0.66 | 1.10 | 22 |
| stroke 148 | 39 % → 49 % | 742.3 px | 0.65 | 1.26 | 2 |
| stroke 149 | 7 % → 46 % | 73.4 px | 0.64 | 6.61 | 4 |
| stroke 150 | 16 % → 50 % | 113.2 px | 0.65 | 3.19 | 14 |
| stroke 151 | 7 % → 54 % | 40.3 px | 0.65 | 7.49 | 18 |
| stroke 152 | 23 % → 53 % | 143.4 px | 0.64 | 2.33 | 23 |
| stroke 153 | 48 % → 62 % | 278.5 px | 0.65 | 1.30 | 13 |
| stroke 154 | 34 % → 56 % | 83.9 px | 0.66 | 1.67 | 39 |
| stroke 155 | 50 % → 65 % | 596.2 px | 0.66 | 1.30 | 27 |
| stroke 156 | 23 % → 49 % | 202.5 px | 0.65 | 2.13 | 8 |
| stroke 157 | 21 % → 51 % | 131.7 px | 0.65 | 2.38 | 16 |
| stroke 158 | 22 % → 50 % | 176.6 px | 0.65 | 2.27 | 16 |
| stroke 159 | 39 % → 52 % | 172.4 px | 0.65 | 1.34 | 19 |
| stroke 160 | 30 % → 49 % | 160.6 px | 0.65 | 1.64 | 20 |
| stroke 161 | 35 % → 51 % | 160.5 px | 0.64 | 1.45 | 26 |
| stroke 162 | 10 % → 54 % | 82.5 px | 0.64 | 5.56 | 10 |
| stroke 163 | 1 % → 59 % | 15.3 px | 0.64 | 41.61 | 3 |
| stroke 164 | 19 % → 58 % | 163.6 px | 0.64 | 3.02 | 8 |
| stroke 165 | 20 % → 57 % | 170.4 px | 0.64 | 2.85 | 5 |
| stroke 166 | 52 % → 65 % | 326.6 px | 0.65 | 1.25 | 17 |
| stroke 167 | 25 % → 61 % | 335.1 px | 0.64 | 2.48 | 3 |
| stroke 168 | 3 % → 68 % | 44.1 px | 0.65 | 23.21 | 3 |
| stroke 169 | 3 % → 75 % | 14.4 px | 0.66 | 27.11 | 15 |
| stroke 170 | 3 % → 62 % | 32.1 px | 0.64 | 17.97 | 8 |
| stroke 171 | 8 % → 61 % | 61.7 px | 0.64 | 7.37 | 15 |
| stroke 172 | 51 % → 63 % | 479.4 px | 0.65 | 1.24 | 4 |
| stroke 173 | 8 % → 64 % | 37.3 px | 0.65 | 8.01 | 61 |
| stroke 174 | 17 % → 70 % | 82.6 px | 0.65 | 4.22 | 11 |
| stroke 175 | 6 % → 56 % | 54.6 px | 0.64 | 9.85 | 11 |
| stroke 176 | 8 % → 57 % | 63.0 px | 0.64 | 7.09 | 20 |
| stroke 177 | 13 % → 59 % | 91.9 px | 0.64 | 4.64 | 17 |
| stroke 178 | 32 % → 60 % | 106.7 px | 0.64 | 1.89 | 17 |
| stroke 179 | 17 % → 60 % | 129.1 px | 0.64 | 3.50 | 10 |
| stroke 180 | 19 % → 55 % | 182.4 px | 0.64 | 2.85 | 8 |
| stroke 181 | 31 % → 53 % | 312.7 px | 0.63 | 1.68 | 16 |
| stroke 182 | 27 % → 55 % | 224.1 px | 0.64 | 2.00 | 15 |
| stroke 183 | 16 % → 68 % | 231.4 px | 0.65 | 4.31 | 15 |
| stroke 184 | 21 % → 62 % | 177.6 px | 0.65 | 3.01 | 12 |
| stroke 185 | 29 % → 53 % | 345.1 px | 0.64 | 1.86 | 4 |
| stroke 186 | 34 % → 70 % | 90.6 px | 0.65 | 2.09 | 12 |
| stroke 187 | 20 % → 54 % | 228.1 px | 0.64 | 2.71 | 16 |
| stroke 188 | 42 % → 57 % | 180.3 px | 0.64 | 1.38 | 41 |
| stroke 189 | 27 % → 68 % | 54.8 px | 0.66 | 2.49 | 44 |
| stroke 190 | 41 % → 58 % | 305.4 px | 0.64 | 1.39 | 7 |
| stroke 191 | 29 % → 57 % | 217.6 px | 0.64 | 1.96 | 10 |
| stroke 192 | 35 % → 61 % | 267.1 px | 0.64 | 1.73 | 16 |
| stroke 193 | 48 % → 58 % | 452.7 px | 0.64 | 1.23 | 15 |
| stroke 194 | 34 % → 63 % | 210.8 px | 0.64 | 1.87 | 20 |
| stroke 195 | 42 % → 61 % | 310.5 px | 0.64 | 1.45 | 18 |
| stroke 196 | 44 % → 61 % | 188.5 px | 0.64 | 1.39 | 11 |
| stroke 197 | 37 % → 50 % | 71.8 px | 0.63 | 1.37 | 34 |
| stroke 198 | 25 % → 55 % | 118.0 px | 0.64 | 2.24 | 18 |
| stroke 199 | 30 % → 50 % | 380.9 px | 0.64 | 1.69 | 6 |
| stroke 200 | 39 % → 53 % | 195.5 px | 0.63 | 1.35 | 21 |
| stroke 201 | 36 % → 50 % | 263.4 px | 0.63 | 1.40 | 5 |
| stroke 202 | 39 % → 53 % | 285.5 px | 0.64 | 1.35 | 4 |
| stroke 203 | 38 % → 50 % | 445.1 px | 0.64 | 1.30 | 4 |
| stroke 204 | 45 % → 54 % | 231.8 px | 0.64 | 1.19 | 9 |
| stroke 205 | 2 % → 49 % | 25.7 px | 0.63 | 24.96 | 4 |
| stroke 206 | 28 % → 62 % | 131.9 px | 0.63 | 2.22 | 25 |
| stroke 207 | 19 % → 59 % | 149.0 px | 0.64 | 3.02 | 10 |
| stroke 208 | 2 % → 67 % | 14.1 px | 0.64 | 33.97 | 4 |
| stroke 209 | 13 % → 48 % | 53.4 px | 0.64 | 3.76 | 13 |
| stroke 210 | 11 % → 59 % | 65.7 px | 0.63 | 5.59 | 8 |
| stroke 211 | 8 % → 59 % | 80.8 px | 0.64 | 7.35 | 5 |
| stroke 212 | 16 % → 63 % | 41.3 px | 0.64 | 4.07 | 33 |
| stroke 213 | 25 % → 66 % | 98.7 px | 0.64 | 2.67 | 20 |
| stroke 214 | 23 % → 59 % | 363.0 px | 0.62 | 2.62 | 2 |
| stroke 215 | 29 % → 62 % | 412.4 px | 0.63 | 2.17 | 2 |
| stroke 216 | 23 % → 60 % | 143.9 px | 0.64 | 2.63 | 11 |
| stroke 217 | 34 % → 65 % | 301.3 px | 0.64 | 1.90 | 11 |
| stroke 218 | 42 % → 61 % | 189.2 px | 0.64 | 1.47 | 23 |
| stroke 219 | 36 % → 60 % | 304.0 px | 0.63 | 1.70 | 10 |
| stroke 220 | 42 % → 59 % | 654.2 px | 0.64 | 1.41 | 3 |
| stroke 221 | 38 % → 61 % | 267.1 px | 0.64 | 1.58 | 24 |
| stroke 222 | 48 % → 58 % | 375.9 px | 0.64 | 1.21 | 5 |
| stroke 223 | 47 % → 67 % | 373.8 px | 0.64 | 1.41 | 7 |
| stroke 224 | 17 % → 47 % | 123.6 px | 0.64 | 2.76 | 19 |
| stroke 225 | 20 % → 52 % | 163.2 px | 0.65 | 2.56 | 15 |
| stroke 226 | 36 % → 55 % | 159.5 px | 0.64 | 1.54 | 72 |
| stroke 227 | 29 % → 54 % | 255.6 px | 0.64 | 1.83 | 11 |
| stroke 228 | 13 % → 47 % | 166.7 px | 0.64 | 3.57 | 5 |
| stroke 229 | 29 % → 48 % | 163.8 px | 0.64 | 1.64 | 22 |
| stroke 230 | 31 % → 57 % | 111.6 px | 0.65 | 1.85 | 59 |
| stroke 231 | 25 % → 54 % | 205.1 px | 0.63 | 2.19 | 5 |
| stroke 232 | 33 % → 57 % | 393.1 px | 0.64 | 1.76 | 6 |
| stroke 233 | 37 % → 57 % | 166.6 px | 0.64 | 1.54 | 13 |
| stroke 234 | 26 % → 63 % | 297.5 px | 0.66 | 2.40 | 4 |
| stroke 235 | 12 % → 44 % | 80.9 px | 0.65 | 3.63 | 12 |
| stroke 236 | 30 % → 59 % | 232.3 px | 0.66 | 1.97 | 9 |
| stroke 237 | 32 % → 55 % | 139.1 px | 0.65 | 1.75 | 26 |
| stroke 238 | 26 % → 48 % | 95.8 px | 0.64 | 1.85 | 27 |
| stroke 239 | 30 % → 51 % | 279.1 px | 0.65 | 1.72 | 7 |
| stroke 240 | 23 % → 47 % | 191.4 px | 0.65 | 2.04 | 8 |
| stroke 241 | 35 % → 52 % | 135.5 px | 0.65 | 1.47 | 23 |
| stroke 242 | 2 % → 51 % | 15.6 px | 0.63 | 27.27 | 5 |
| stroke 243 | 8 % → 58 % | 30.6 px | 0.64 | 7.57 | 36 |
| stroke 244 | 23 % → 63 % | 278.8 px | 0.65 | 2.78 | 4 |
| stroke 245 | 1 % → 35 % | 16.1 px | 0.63 | 28.57 | 4 |
| stroke 246 | 4 % → 44 % | 25.4 px | 0.64 | 10.51 | 8 |
| stroke 247 | 11 % → 42 % | 58.1 px | 0.63 | 3.78 | 17 |
| stroke 248 | 10 % → 33 % | 93.7 px | 0.63 | 3.20 | 6 |
| stroke 249 | 8 % → 38 % | 67.4 px | 0.61 | 4.73 | 11 |
| stroke 250 | 18 % → 64 % | 174.0 px | 0.64 | 3.51 | 7 |
| stroke 251 | 9 % → 49 % | 83.3 px | 0.62 | 5.37 | 13 |
| stroke 252 | 12 % → 63 % | 149.0 px | 0.64 | 5.14 | 8 |
| stroke 253 | 9 % → 66 % | 139.8 px | 0.64 | 7.39 | 2 |
| stroke 254 | 12 % → 56 % | 84.9 px | 0.64 | 4.54 | 10 |
| stroke 255 | 30 % → 58 % | 357.3 px | 0.64 | 1.94 | 18 |
| stroke 256 | 23 % → 54 % | 237.5 px | 0.65 | 2.38 | 10 |
| stroke 257 | 27 % → 55 % | 394.5 px | 0.65 | 2.07 | 10 |
| stroke 258 | 46 % → 64 % | 306.5 px | 0.66 | 1.39 | 12 |
| stroke 259 | 17 % → 65 % | 225.1 px | 0.64 | 3.79 | 11 |
| stroke 260 | 36 % → 62 % | 150.2 px | 0.65 | 1.70 | 27 |
| stroke 261 | 20 % → 57 % | 96.4 px | 0.64 | 2.83 | 15 |
| stroke 262 | 20 % → 54 % | 309.7 px | 0.64 | 2.74 | 7 |
| stroke 263 | 20 % → 52 % | 171.1 px | 0.64 | 2.64 | 15 |
| stroke 264 | 28 % → 56 % | 353.0 px | 0.65 | 2.02 | 4 |
| stroke 265 | 23 % → 48 % | 364.4 px | 0.62 | 2.07 | 3 |
| stroke 266 | 17 % → 31 % | 233.7 px | 0.63 | 1.78 | 2 |
| stroke 267 | 16 % → 34 % | 99.5 px | 0.62 | 2.06 | 13 |
| stroke 268 | 22 % → 50 % | 202.3 px | 0.64 | 2.34 | 15 |
| stroke 269 | 32 % → 61 % | 165.4 px | 0.64 | 1.87 | 17 |
| stroke 270 | 21 % → 34 % | 314.6 px | 0.62 | 1.58 | 2 |
| stroke 271 | 33 % → 54 % | 245.5 px | 0.63 | 1.62 | 17 |
| stroke 272 | 45 % → 64 % | 453.6 px | 0.65 | 1.41 | 5 |
| stroke 273 | 26 % → 48 % | 156.1 px | 0.63 | 1.81 | 33 |
| stroke 274 | 33 % → 39 % | 281.9 px | 0.62 | 1.18 | 15 |
| stroke 275 | 44 % → 59 % | 248.1 px | 0.65 | 1.35 | 18 |
| stroke 276 | 39 % → 55 % | 646.8 px | 0.63 | 1.39 | 13 |
| stroke 277 | 33 % → 48 % | 281.5 px | 0.63 | 1.44 | 8 |
| stroke 278 | 49 % → 61 % | 335.0 px | 0.64 | 1.24 | 13 |
| stroke 279 | 32 % → 51 % | 362.2 px | 0.63 | 1.61 | 5 |
| stroke 280 | 37 % → 53 % | 609.6 px | 0.63 | 1.41 | 6 |
| stroke 281 | 46 % → 54 % | 408.0 px | 0.63 | 1.18 | 16 |
| stroke 282 | 51 % → 55 % | 194.6 px | 0.64 | 1.08 | 22 |
| stroke 283 | 34 % → 56 % | 101.0 px | 0.63 | 1.63 | 23 |
| stroke 284 | 12 % → 43 % | 59.3 px | 0.61 | 3.57 | 6 |
| stroke 285 | 11 % → 38 % | 62.2 px | 0.62 | 3.56 | 15 |
| stroke 286 | 17 % → 36 % | 117.0 px | 0.61 | 2.07 | 10 |
| stroke 287 | 38 % → 51 % | 174.1 px | 0.62 | 1.33 | 24 |
| stroke 288 | 39 % → 51 % | 263.6 px | 0.61 | 1.31 | 6 |
| stroke 289 | 32 % → 55 % | 281.6 px | 0.64 | 1.72 | 7 |
| stroke 290 | 21 % → 58 % | 116.2 px | 0.65 | 2.83 | 8 |
| stroke 291 | 45 % → 67 % | 209.4 px | 0.66 | 1.49 | 16 |
| stroke 292 | 29 % → 62 % | 213.0 px | 0.67 | 2.14 | 2 |
| stroke 293 | 44 % → 64 % | 118.7 px | 0.65 | 1.46 | 20 |
| stroke 294 | 35 % → 56 % | 236.5 px | 0.66 | 1.60 | 16 |
| stroke 295 | 10 % → 35 % | 95.1 px | 0.63 | 3.43 | 11 |
| stroke 296 | 31 % → 39 % | 86.1 px | 0.64 | 1.28 | 192 |
| stroke 297 | 28 % → 73 % | 106.4 px | 0.66 | 2.57 | 45 |
| stroke 298 | 4 % → 41 % | 35.1 px | 0.63 | 9.21 | 70 |
| stroke 299 | 2 % → 29 % | 13.3 px | 0.62 | 13.62 | 25 |
| stroke 300 | 7 % → 33 % | 72.0 px | 0.62 | 4.75 | 6 |
| stroke 301 | 9 % → 30 % | 48.4 px | 0.62 | 3.46 | 28 |
| stroke 302 | 18 % → 47 % | 56.6 px | 0.64 | 2.54 | 90 |
| stroke 303 | 19 % → 42 % | 146.9 px | 0.63 | 2.24 | 182 |
| stroke 304 | 14 % → 36 % | 122.5 px | 0.62 | 2.62 | 25 |
| stroke 305 | 22 % → 47 % | 216.4 px | 0.63 | 2.20 | 67 |
| stroke 306 | 22 % → 45 % | 182.5 px | 0.63 | 2.07 | 35 |
| stroke 307 | 12 % → 31 % | 95.9 px | 0.62 | 2.55 | 25 |
| stroke 308 | 19 % → 39 % | 181.0 px | 0.62 | 2.01 | 28 |
| stroke 309 | 20 % → 38 % | 164.8 px | 0.62 | 1.91 | 373 |
| stroke 310 | 20 % → 29 % | 107.3 px | 0.61 | 1.47 | 165 |
| stroke 311 | 16 % → 44 % | 86.2 px | 0.63 | 2.83 | 30 |
| stroke 312 | 2 % → 34 % | 19.1 px | 0.63 | 20.06 | 5 |
| stroke 313 | 18 % → 45 % | 143.2 px | 0.63 | 2.51 | 10 |
| stroke 314 | 28 % → 46 % | 341.9 px | 0.63 | 1.61 | 18 |
| stroke 315 | 14 % → 44 % | 174.8 px | 0.63 | 3.11 | 38 |
| stroke 316 | 27 % → 44 % | 194.5 px | 0.63 | 1.60 | 18 |
| stroke 317 | 30 % → 45 % | 516.8 px | 0.64 | 1.53 | 8 |
| stroke 318 | 22 % → 41 % | 175.1 px | 0.63 | 1.86 | 33 |
| stroke 319 | 30 % → 42 % | 568.1 px | 0.63 | 1.39 | 2 |
| stroke 320 | 22 % → 40 % | 190.6 px | 0.63 | 1.84 | 9 |
| stroke 321 | 8 % → 42 % | 64.6 px | 0.63 | 5.21 | 6 |
| stroke 322 | 21 % → 61 % | 187.7 px | 0.64 | 2.95 | 22 |
| stroke 323 | 7 % → 56 % | 48.3 px | 0.64 | 7.66 | 13 |
| stroke 324 | 29 % → 59 % | 58.1 px | 0.65 | 2.06 | 79 |
| stroke 325 | 34 % → 60 % | 225.7 px | 0.65 | 1.79 | 14 |
| stroke 326 | 32 % → 54 % | 248.7 px | 0.65 | 1.69 | 14 |
| stroke 327 | 20 % → 51 % | 82.6 px | 0.63 | 2.48 | 21 |
| stroke 328 | 26 % → 48 % | 98.5 px | 0.63 | 1.82 | 53 |
| stroke 329 | 32 % → 53 % | 187.2 px | 0.65 | 1.66 | 13 |
| stroke 330 | 20 % → 52 % | 58.3 px | 0.63 | 2.61 | 64 |
| stroke 331 | 42 % → 56 % | 445.6 px | 0.65 | 1.34 | 15 |
| stroke 332 | 40 % → 53 % | 256.4 px | 0.64 | 1.34 | 25 |
| stroke 333 | 7 % → 54 % | 49.1 px | 0.64 | 8.10 | 8 |
| stroke 334 | 7 % → 56 % | 56.9 px | 0.64 | 8.47 | 8 |
| stroke 335 | 9 % → 62 % | 69.1 px | 0.65 | 7.16 | 98 |
| stroke 336 | 3 % → 48 % | 17.1 px | 0.64 | 18.40 | 30 |
| stroke 337 | 7 % → 55 % | 42.7 px | 0.65 | 8.46 | 213 |
| stroke 338 | 12 % → 53 % | 151.2 px | 0.65 | 4.52 | 2 |
| stroke 339 | 28 % → 57 % | 235.3 px | 0.65 | 2.05 | 13 |
| stroke 340 | 13 % → 70 % | 104.1 px | 0.66 | 5.35 | 36 |
| stroke 341 | 32 % → 56 % | 187.3 px | 0.65 | 1.76 | 54 |
| stroke 342 | 9 % → 66 % | 99.0 px | 0.64 | 7.20 | 28 |
| stroke 343 | 20 % → 63 % | 166.6 px | 0.64 | 3.11 | 5 |
| stroke 344 | 24 % → 66 % | 397.0 px | 0.65 | 2.70 | 14 |
| stroke 345 | 21 % → 65 % | 185.1 px | 0.64 | 3.05 | 25 |
| stroke 346 | 30 % → 64 % | 424.5 px | 0.65 | 2.12 | 2 |
| stroke 347 | 34 % → 59 % | 112.2 px | 0.63 | 1.73 | 35 |
| stroke 348 | 41 % → 56 % | 258.4 px | 0.65 | 1.37 | 39 |
| stroke 349 | 43 % → 56 % | 266.5 px | 0.65 | 1.30 | 18 |
| stroke 350 | 39 % → 59 % | 351.4 px | 0.65 | 1.51 | 6 |
| stroke 351 | 37 % → 57 % | 317.7 px | 0.64 | 1.55 | 6 |
| stroke 352 | 39 % → 64 % | 661.1 px | 0.64 | 1.65 | 3 |
| stroke 353 | 32 % → 49 % | 282.4 px | 0.64 | 1.54 | 5 |
| stroke 354 | 13 % → 49 % | 80.6 px | 0.64 | 3.84 | 13 |
| stroke 355 | 27 % → 53 % | 229.4 px | 0.64 | 1.95 | 25 |
| stroke 356 | 6 % → 34 % | 29.1 px | 0.64 | 5.51 | 12 |
| stroke 357 | 21 % → 51 % | 88.5 px | 0.64 | 2.40 | 67 |
| stroke 358 | 9 % → 42 % | 43.0 px | 0.64 | 4.91 | 19 |
| stroke 359 | 15 % → 39 % | 110.8 px | 0.64 | 2.58 | 12 |
| stroke 360 | 19 % → 50 % | 223.7 px | 0.64 | 2.66 | 9 |
| stroke 361 | 22 % → 49 % | 396.3 px | 0.64 | 2.24 | 4 |
| stroke 362 | 22 % → 47 % | 151.0 px | 0.64 | 2.18 | 32 |
| stroke 363 | 21 % → 44 % | 320.9 px | 0.64 | 2.12 | 10 |
| stroke 364 | 27 % → 51 % | 211.5 px | 0.64 | 1.88 | 23 |
| stroke 365 | 26 % → 38 % | 310.9 px | 0.65 | 1.43 | 14 |
| stroke 366 | 34 % → 45 % | 250.3 px | 0.64 | 1.31 | 19 |
| stroke 367 | 19 % → 63 % | 56.8 px | 0.66 | 3.35 | 21 |
| stroke 368 | 5 % → 72 % | 18.4 px | 0.66 | 15.46 | 89 |
| stroke 369 | 20 % → 55 % | 108.5 px | 0.64 | 2.74 | 16 |
| stroke 370 | 10 % → 56 % | 89.4 px | 0.64 | 5.68 | 31 |
| stroke 371 | 13 % → 50 % | 228.0 px | 0.63 | 3.86 | 4 |
| stroke 372 | 14 % → 56 % | 131.3 px | 0.64 | 4.13 | 7 |
| stroke 373 | 22 % → 51 % | 88.8 px | 0.63 | 2.36 | 18 |
| stroke 374 | 27 % → 57 % | 152.5 px | 0.64 | 2.11 | 12 |
| stroke 375 | 22 % → 51 % | 189.7 px | 0.62 | 2.34 | 6 |
| stroke 376 | 36 % → 58 % | 326.1 px | 0.64 | 1.61 | 3 |
| stroke 377 | 31 % → 52 % | 105.0 px | 0.62 | 1.66 | 27 |
| stroke 378 | 9 % → 50 % | 50.2 px | 0.63 | 5.58 | 6 |
| stroke 379 | 28 % → 56 % | 116.0 px | 0.64 | 1.98 | 104 |
| stroke 380 | 13 % → 55 % | 79.5 px | 0.63 | 4.21 | 29 |
| stroke 381 | 13 % → 49 % | 53.5 px | 0.63 | 3.72 | 24 |
| stroke 382 | 31 % → 52 % | 107.0 px | 0.63 | 1.68 | 55 |
| stroke 383 | 26 % → 52 % | 165.2 px | 0.63 | 2.03 | 146 |
| stroke 384 | 32 % → 53 % | 203.0 px | 0.63 | 1.68 | 11 |
| stroke 385 | 7 % → 67 % | 30.8 px | 0.66 | 9.47 | 19 |
| stroke 386 | 17 % → 50 % | 70.9 px | 0.64 | 2.94 | 31 |
| stroke 387 | 4 % → 55 % | 31.5 px | 0.65 | 13.32 | 4 |
| stroke 388 | 38 % → 67 % | 75.7 px | 0.65 | 1.75 | 28 |
| stroke 389 | 22 % → 57 % | 91.6 px | 0.65 | 2.59 | 13 |
| stroke 390 | 10 % → 62 % | 164.2 px | 0.65 | 6.11 | 7 |
| stroke 391 | 31 % → 61 % | 108.4 px | 0.65 | 1.95 | 28 |
| stroke 392 | 26 % → 58 % | 82.7 px | 0.64 | 2.26 | 19 |
| stroke 393 | 30 % → 56 % | 159.3 px | 0.65 | 1.85 | 19 |
| stroke 394 | 36 % → 63 % | 199.1 px | 0.65 | 1.75 | 15 |
| stroke 395 | 23 % → 50 % | 73.0 px | 0.64 | 2.23 | 24 |
| stroke 396 | 39 % → 61 % | 319.0 px | 0.65 | 1.58 | 6 |
| stroke 397 | 45 % → 57 % | 818.5 px | 0.66 | 1.28 | 2 |
| stroke 398 | 25 % → 49 % | 483.3 px | 0.64 | 1.92 | 1 |
| stroke 399 | 32 % → 57 % | 276.6 px | 0.66 | 1.78 | 11 |
| stroke 400 | 51 % → 64 % | 215.1 px | 0.65 | 1.24 | 25 |
| stroke 401 | 45 % → 59 % | 132.6 px | 0.65 | 1.30 | 19 |
| stroke 402 | 42 % → 57 % | 374.0 px | 0.66 | 1.35 | 17 |
| stroke 403 | 47 % → 56 % | 289.2 px | 0.66 | 1.18 | 11 |
| stroke 404 | 66 % → 73 % | 1256.3 px | 0.65 | 1.12 | 6 |
| stroke 405 | 14 % → 46 % | 118.2 px | 0.63 | 3.24 | 5 |
| stroke 406 | 32 % → 48 % | 97.9 px | 0.63 | 1.53 | 42 |
| stroke 407 | 36 % → 53 % | 174.3 px | 0.64 | 1.47 | 11 |
| stroke 408 | 36 % → 53 % | 91.7 px | 0.63 | 1.48 | 16 |
| stroke 409 | 39 % → 51 % | 113.0 px | 0.65 | 1.30 | 8 |
| stroke 410 | 52 % → 63 % | 337.9 px | 0.66 | 1.23 | 4 |
| stroke 411 | 26 % → 49 % | 166.2 px | 0.63 | 1.93 | 4 |
| stroke 412 | 31 % → 51 % | 216.4 px | 0.63 | 1.68 | 5 |
| stroke 413 | 35 % → 49 % | 242.1 px | 0.63 | 1.42 | 43 |
| stroke 414 | 34 % → 47 % | 235.0 px | 0.63 | 1.40 | 3 |
| stroke 415 | 37 % → 47 % | 371.6 px | 0.64 | 1.27 | 9 |
| stroke 416 | 37 % → 46 % | 264.0 px | 0.64 | 1.23 | 4 |
| stroke 417 | 40 % → 51 % | 243.0 px | 0.63 | 1.26 | 10 |
| stroke 418 | 41 % → 47 % | 228.7 px | 0.64 | 1.14 | 11 |
| stroke 419 | 49 % → 57 % | 387.4 px | 0.64 | 1.16 | 7 |
| stroke 420 | 38 % → 44 % | 126.1 px | 0.64 | 1.17 | 15 |

Numbers say: wet paint spreads well beyond the stroke.

## Refs v3 · #16 Shrigley strokes — own sheet
own sheet 800 × 1000 · Watercolour 1.00 + water 30 % · 64 px · 30.2 s

![Refs v3 · #16 Shrigley strokes — own sheet](Refs-v3-16-Shrigley-strokes-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 6 % → 19 % | 33.2 px | 0.33 | 3.20 | 55 |
| stroke 2 | 4 % → 5 % | 45.8 px | 0.34 | 1.37 | 14 |
| stroke 3 | 7 % → 8 % | 80.8 px | 0.31 | 1.17 | 27 |
| stroke 4 | 10 % → 16 % | 44.9 px | 0.35 | 1.62 | 121 |
| stroke 5 | 3 % → 4 % | 28.0 px | 0.30 | 1.72 | 11 |
| stroke 6 | 7 % → 15 % | 121.8 px | 0.33 | 2.00 | 21 |
| stroke 7 | 8 % → 7 % | 54.6 px | 0.32 | 0.95 | 164 |
| stroke 8 | 14 % → 12 % | 113.8 px | 0.31 | 0.85 | 78 |
| stroke 9 | 18 % → 9 % | 324.6 px | 0.30 | 0.49 | 22 |
| stroke 10 | 14 % → 12 % | 73.5 px | 0.29 | 0.89 | 188 |
| stroke 11 | 10 % → 20 % | 83.0 px | 0.28 | 2.06 | 69 |
| stroke 12 | 15 % → 5 % | 75.2 px | 0.27 | 0.31 | 128 |
| stroke 13 | 8 % → 7 % | 39.9 px | 0.23 | 0.84 | 167 |
| stroke 14 | 8 % → 15 % | 78.7 px | 0.28 | 1.85 | 81 |
| stroke 15 | 24 % → 8 % | 121.0 px | 0.23 | 0.33 | 144 |
| stroke 16 | 12 % → 14 % | 87.2 px | 0.27 | 1.20 | 96 |
| stroke 17 | 27 % → 14 % | 246.2 px | 0.28 | 0.50 | 83 |
| stroke 18 | 11 % → 12 % | 132.9 px | 0.32 | 1.08 | 28 |
| stroke 19 | 10 % → 15 % | 44.9 px | 0.30 | 1.49 | 205 |
| stroke 20 | 15 % → 18 % | 155.3 px | 0.30 | 1.23 | 74 |
| stroke 21 | 16 % → 21 % | 193.0 px | 0.29 | 1.34 | 36 |
| stroke 22 | 14 % → 13 % | 71.3 px | 0.27 | 0.96 | 192 |
| stroke 23 | 22 % → 18 % | 118.8 px | 0.28 | 0.83 | 178 |
| stroke 24 | 17 % → 10 % | 104.1 px | 0.34 | 0.57 | 58 |
| stroke 25 | 7 % → 15 % | 29.5 px | 0.34 | 2.02 | 107 |
| stroke 26 | 14 % → 16 % | 77.3 px | 0.35 | 1.17 | 65 |
| stroke 27 | 8 % → 9 % | 44.8 px | 0.31 | 1.12 | 189 |
| stroke 28 | 14 % → 7 % | 111.6 px | 0.31 | 0.51 | 34 |
| stroke 29 | 19 % → 8 % | 171.3 px | 0.31 | 0.44 | 33 |
| stroke 30 | 6 % → 18 % | 194.3 px | 0.31 | 2.94 | 7 |
| stroke 31 | 9 % → 11 % | 97.9 px | 0.32 | 1.30 | 42 |
| stroke 32 | 7 % → 9 % | 162.5 px | 0.32 | 1.43 | 10 |
| stroke 33 | 10 % → 8 % | 79.5 px | 0.32 | 0.73 | 62 |
| stroke 34 | 10 % → 7 % | 82.1 px | 0.31 | 0.68 | 43 |
| stroke 35 | 24 % → 6 % | 162.0 px | 0.31 | 0.26 | 65 |
| stroke 36 | 15 % → 8 % | 170.6 px | 0.30 | 0.55 | 48 |
| stroke 37 | 13 % → 4 % | 90.2 px | 0.27 | 0.30 | 74 |
| stroke 38 | 19 % → 3 % | 105.5 px | 0.27 | 0.17 | 69 |
| stroke 39 | 24 % → 11 % | 221.2 px | 0.25 | 0.44 | 63 |
| stroke 40 | 17 % → 11 % | 195.9 px | 0.28 | 0.61 | 35 |
| stroke 41 | 10 % → 16 % | 93.1 px | 0.30 | 1.53 | 110 |
| stroke 42 | 11 % → 16 % | 157.0 px | 0.28 | 1.51 | 21 |
| stroke 43 | 7 % → 12 % | 42.2 px | 0.29 | 1.61 | 96 |
| stroke 44 | 6 % → 14 % | 47.0 px | 0.27 | 2.34 | 91 |
| stroke 45 | 15 % → 11 % | 194.8 px | 0.28 | 0.77 | 38 |
| stroke 46 | 11 % → 12 % | 109.3 px | 0.29 | 1.17 | 24 |
| stroke 47 | 15 % → 8 % | 370.3 px | 0.34 | 0.51 | 21 |
| stroke 48 | 12 % → 9 % | 146.3 px | 0.32 | 0.72 | 36 |
| stroke 49 | 19 % → 7 % | 200.5 px | 0.33 | 0.38 | 46 |
| stroke 50 | 20 % → 9 % | 162.6 px | 0.30 | 0.46 | 191 |
| stroke 51 | 5 % → 12 % | 73.8 px | 0.26 | 2.12 | 27 |
| stroke 52 | 5 % → 0 % | 64.0 px | 0.19 | 0.01 | 40 |
| stroke 53 | 7 % → 0 % | 197.3 px | 0.18 | 0.01 | 20 |
| stroke 54 | 4 % → 11 % | 40.7 px | 0.28 | 2.90 | 35 |
| stroke 55 | 5 % → 18 % | 128.1 px | 0.28 | 3.99 | 7 |
| stroke 56 | 11 % → 6 % | 61.5 px | 0.36 | 0.53 | 116 |
| stroke 57 | 18 % → 12 % | 104.3 px | 0.34 | 0.64 | 74 |
| stroke 58 | 6 % → 12 % | 103.6 px | 0.29 | 1.98 | 14 |
| stroke 59 | 3 % → 23 % | 50.5 px | 0.24 | 7.99 | 13 |
| stroke 60 | 16 % → 13 % | 56.2 px | 0.31 | 0.81 | 65 |
| stroke 61 | 1 % → 8 % | 46.2 px | 0.29 | 6.06 | 4 |
| stroke 62 | 9 % → 11 % | 49.0 px | 0.33 | 1.26 | 297 |
| stroke 63 | 13 % → 6 % | 49.3 px | 0.33 | 0.45 | 137 |
| stroke 64 | 17 % → 11 % | 154.7 px | 0.30 | 0.65 | 37 |
| stroke 65 | 20 % → 10 % | 85.0 px | 0.34 | 0.50 | 221 |
| stroke 66 | 4 % → 2 % | 147.1 px | 0.29 | 0.53 | 8 |
| stroke 67 | 10 % → 3 % | 69.6 px | 0.32 | 0.31 | 114 |
| stroke 68 | 16 % → 1 % | 354.0 px | 0.29 | 0.09 | 17 |
| stroke 69 | 13 % → 10 % | 80.7 px | 0.31 | 0.76 | 88 |
| stroke 70 | 8 % → 8 % | 41.3 px | 0.25 | 1.02 | 81 |
| stroke 71 | 14 % → 5 % | 62.1 px | 0.30 | 0.38 | 318 |
| stroke 72 | 11 % → 9 % | 234.0 px | 0.31 | 0.82 | 18 |
| stroke 73 | 13 % → 11 % | 185.3 px | 0.29 | 0.88 | 28 |
| stroke 74 | 20 % → 9 % | 161.3 px | 0.26 | 0.42 | 107 |
| stroke 75 | 5 % → 21 % | 42.9 px | 0.30 | 4.35 | 87 |
| stroke 76 | 9 % → 21 % | 60.8 px | 0.30 | 2.24 | 59 |
| stroke 77 | 13 % → 22 % | 88.1 px | 0.27 | 1.65 | 99 |
| stroke 78 | 9 % → 14 % | 36.1 px | 0.34 | 1.59 | 247 |
| stroke 79 | 2 % → 10 % | 28.5 px | 0.31 | 4.86 | 29 |
| stroke 80 | 5 % → 11 % | 59.3 px | 0.31 | 2.12 | 88 |
| stroke 81 | 2 % → 10 % | 29.2 px | 0.31 | 4.07 | 18 |
| stroke 82 | 8 % → 12 % | 111.4 px | 0.31 | 1.39 | 38 |
| stroke 83 | 6 % → 8 % | 51.3 px | 0.31 | 1.46 | 52 |
| stroke 84 | 2 % → 3 % | 37.4 px | 0.27 | 1.60 | 8 |
| stroke 85 | 5 % → 13 % | 41.8 px | 0.28 | 2.48 | 76 |
| stroke 86 | 3 % → 13 % | 91.2 px | 0.23 | 4.24 | 19 |
| stroke 87 | 10 % → 17 % | 201.7 px | 0.27 | 1.74 | 17 |
| stroke 88 | 12 % → 14 % | 124.6 px | 0.27 | 1.16 | 71 |
| stroke 89 | 6 % → 11 % | 40.7 px | 0.29 | 1.72 | 167 |
| stroke 90 | 4 % → 16 % | 142.6 px | 0.28 | 3.56 | 7 |
| stroke 91 | 3 % → 14 % | 96.3 px | 0.28 | 4.17 | 14 |
| stroke 92 | 10 % → 12 % | 50.8 px | 0.26 | 1.19 | 277 |
| stroke 93 | 12 % → 15 % | 53.6 px | 0.30 | 1.28 | 144 |
| stroke 94 | 10 % → 11 % | 37.0 px | 0.31 | 1.19 | 111 |

Numbers say: wet paint spreads well beyond the stroke.

## Refs v3 · #17 Krovostok dry brush — own sheet
own sheet 800 × 720 · Ink 0.93 · Gouache 0.07 · 38 px · 33.6 s

![Refs v3 · #17 Krovostok dry brush — own sheet](Refs-v3-17-Krovostok-dry-brush-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 10 % → 49 % | 39.6 px | 0.81 | 4.88 | 50 |
| stroke 2 | 16 % → 52 % | 53.3 px | 0.80 | 3.18 | 146 |
| stroke 3 | 23 % → 55 % | 73.3 px | 0.80 | 2.38 | 181 |
| stroke 4 | 30 % → 60 % | 94.4 px | 0.80 | 1.96 | 154 |
| stroke 5 | 38 % → 71 % | 154.9 px | 0.81 | 1.85 | 74 |
| stroke 6 | 41 % → 74 % | 174.2 px | 0.80 | 1.80 | 60 |
| stroke 7 | 38 % → 69 % | 121.7 px | 0.80 | 1.80 | 158 |
| stroke 8 | 41 % → 73 % | 194.0 px | 0.80 | 1.79 | 46 |
| stroke 9 | 46 % → 81 % | 186.1 px | 0.80 | 1.75 | 66 |
| stroke 10 | 37 % → 64 % | 265.5 px | 0.79 | 1.74 | 27 |
| stroke 11 | 47 % → 79 % | 175.5 px | 0.79 | 1.67 | 124 |
| stroke 12 | 39 % → 57 % | 128.7 px | 0.79 | 1.44 | 140 |
| stroke 13 | 21 % → 56 % | 101.1 px | 0.77 | 2.68 | 159 |
| stroke 14 | 24 % → 26 % | 197.4 px | 0.78 | 1.11 | 27 |
| stroke 15 | 44 % → 65 % | 202.8 px | 0.79 | 1.50 | 63 |
| stroke 16 | 5 % → 29 % | 43.8 px | 0.78 | 6.28 | 11 |
| stroke 17 | 37 % → 68 % | 262.2 px | 0.78 | 1.83 | 15 |
| stroke 18 | 30 % → 71 % | 116.9 px | 0.78 | 2.38 | 99 |
| stroke 19 | 11 % → 40 % | 71.7 px | 0.79 | 3.55 | 20 |
| stroke 20 | 40 % → 76 % | 187.3 px | 0.78 | 1.92 | 55 |
| stroke 21 | 38 % → 83 % | 172.8 px | 0.79 | 2.19 | 68 |
| stroke 22 | 24 % → 50 % | 134.1 px | 0.79 | 2.13 | 26 |
| stroke 23 | 38 % → 67 % | 118.0 px | 0.79 | 1.78 | 204 |
| stroke 24 | 40 % → 73 % | 127.7 px | 0.79 | 1.82 | 204 |
| stroke 25 | 4 % → 29 % | 42.8 px | 0.77 | 6.55 | 9 |
| stroke 26 | 43 % → 82 % | 142.6 px | 0.80 | 1.89 | 139 |
| stroke 27 | 11 % → 40 % | 56.3 px | 0.79 | 3.81 | 42 |
| stroke 28 | 37 % → 70 % | 115.3 px | 0.79 | 1.89 | 199 |
| stroke 29 | 16 % → 55 % | 73.9 px | 0.80 | 3.46 | 51 |
| stroke 30 | 32 % → 65 % | 107.5 px | 0.80 | 2.02 | 145 |
| stroke 31 | 46 % → 68 % | 160.7 px | 0.79 | 1.48 | 154 |
| stroke 32 | 35 % → 67 % | 115.4 px | 0.80 | 1.90 | 157 |
| stroke 33 | 45 % → 59 % | 147.8 px | 0.79 | 1.30 | 157 |
| stroke 34 | 37 % → 70 % | 124.1 px | 0.80 | 1.91 | 117 |
| stroke 35 | 49 % → 65 % | 355.4 px | 0.79 | 1.33 | 20 |
| stroke 36 | 39 % → 47 % | 259.4 px | 0.78 | 1.22 | 52 |
| stroke 37 | 36 % → 65 % | 115.5 px | 0.81 | 1.79 | 222 |
| stroke 38 | 39 % → 45 % | 207.6 px | 0.78 | 1.16 | 38 |
| stroke 39 | 33 % → 36 % | 239.5 px | 0.78 | 1.08 | 16 |
| stroke 40 | 35 % → 60 % | 111.4 px | 0.81 | 1.71 | 186 |
| stroke 41 | 47 % → 83 % | 347.0 px | 0.81 | 1.78 | 32 |
| stroke 42 | 40 % → 67 % | 182.3 px | 0.81 | 1.66 | 61 |
| stroke 43 | 39 % → 69 % | 177.9 px | 0.81 | 1.76 | 94 |
| stroke 44 | 38 % → 63 % | 181.7 px | 0.81 | 1.65 | 62 |
| stroke 45 | 37 % → 48 % | 116.8 px | 0.81 | 1.31 | 211 |
| stroke 46 | 40 % → 45 % | 135.2 px | 0.80 | 1.13 | 106 |
| stroke 47 | 48 % → 49 % | 232.8 px | 0.80 | 1.03 | 64 |

Numbers say: wet paint spreads well beyond the stroke.

## Refs v3 · #18 Twombly blue sticks — own sheet
own sheet 800 × 789 · Wax 1.00 · 20 px · 20.6 s

![Refs v3 · #18 Twombly blue sticks — own sheet](Refs-v3-18-Twombly-blue-sticks-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 3 % → 27 % | 21.5 px | 0.34 | 7.75 | 1 |
| stroke 2 | 6 % → 10 % | 39.9 px | 0.32 | 1.73 | 0 |
| stroke 3 | 6 % → 22 % | 16.8 px | 0.34 | 3.86 | 2 |
| stroke 4 | 11 % → 7 % | 27.4 px | 0.31 | 0.65 | 8 |
| stroke 5 | 11 % → 15 % | 46.0 px | 0.34 | 1.41 | 2 |
| stroke 6 | 13 % → 15 % | 65.2 px | 0.33 | 1.19 | 2 |
| stroke 7 | 14 % → 23 % | 49.8 px | 0.34 | 1.64 | 6 |
| stroke 8 | 18 % → 12 % | 85.6 px | 0.33 | 0.65 | 5 |
| stroke 9 | 13 % → 33 % | 57.6 px | 0.34 | 2.61 | 8 |
| stroke 10 | 15 % → 41 % | 93.1 px | 0.34 | 2.74 | 5 |
| stroke 11 | 18 % → 39 % | 56.1 px | 0.34 | 2.12 | 2 |
| stroke 12 | 16 % → 31 % | 30.3 px | 0.34 | 1.90 | 19 |
| stroke 13 | 5 % → 0 % | 20.5 px | 0.00 | 0.00 | 7 |
| stroke 14 | 25 % → 33 % | 127.4 px | 0.34 | 1.31 | 2 |
| stroke 15 | 20 % → 16 % | 106.3 px | 0.34 | 0.79 | 2 |
| stroke 16 | 21 % → 47 % | 117.1 px | 0.34 | 2.28 | 2 |
| stroke 17 | 29 % → 20 % | 135.8 px | 0.34 | 0.67 | 1 |
| stroke 18 | 9 % → 0 % | 34.5 px | 0.00 | 0.00 | 5 |
| stroke 19 | 5 % → 0 % | 27.7 px | 0.00 | 0.00 | 2 |
| stroke 20 | 23 % → 22 % | 56.7 px | 0.34 | 0.98 | 3 |
| stroke 21 | 20 % → 0 % | 60.1 px | 0.28 | 0.02 | 5 |
| stroke 22 | 9 % → 0 % | 24.1 px | 0.00 | 0.00 | 5 |
| stroke 23 | 13 % → 37 % | 76.1 px | 0.34 | 2.91 | 1 |
| stroke 24 | 27 % → 20 % | 169.8 px | 0.34 | 0.76 | 0 |
| stroke 25 | 30 % → 6 % | 125.8 px | 0.34 | 0.20 | 1 |
| stroke 26 | 15 % → 0 % | 97.2 px | 0.00 | 0.00 | 0 |
| stroke 27 | 15 % → 1 % | 41.1 px | 0.31 | 0.08 | 9 |
| stroke 28 | 25 % → 19 % | 73.4 px | 0.34 | 0.77 | 13 |
| stroke 29 | 11 % → 4 % | 39.0 px | 0.33 | 0.38 | 2 |
| stroke 30 | 16 % → 0 % | 51.2 px | 0.00 | 0.00 | 3 |
| stroke 31 | 9 % → 0 % | 52.1 px | 0.00 | 0.00 | 1 |
| stroke 32 | 19 % → 0 % | 43.0 px | 0.25 | 0.01 | 7 |
| stroke 33 | 9 % → 0 % | 52.4 px | 0.00 | 0.00 | 1 |
| stroke 34 | 21 % → 5 % | 41.9 px | 0.33 | 0.25 | 6 |
| stroke 35 | 20 % → 0 % | 72.2 px | 0.00 | 0.00 | 4 |
| stroke 36 | 11 % → 0 % | 48.1 px | 0.00 | 0.00 | 1 |
| stroke 37 | 27 % → 6 % | 59.5 px | 0.33 | 0.23 | 3 |
| stroke 38 | 28 % → 0 % | 153.9 px | 0.00 | 0.00 | 2 |
| stroke 39 | 19 % → 0 % | 123.2 px | 0.00 | 0.00 | 0 |
| stroke 40 | 14 % → 0 % | 63.0 px | 0.00 | 0.00 | 1 |
| stroke 41 | 23 % → 6 % | 51.2 px | 0.33 | 0.27 | 4 |
| stroke 42 | 38 % → 0 % | 164.6 px | 0.00 | 0.00 | 4 |
| stroke 43 | 26 % → 0 % | 62.6 px | 0.00 | 0.00 | 3 |
| stroke 44 | 13 % → 0 % | 81.7 px | 0.00 | 0.00 | 1 |
| stroke 45 | 32 % → 1 % | 199.8 px | 0.29 | 0.02 | 0 |
| stroke 46 | 20 % → 0 % | 112.1 px | 0.00 | 0.00 | 1 |
| stroke 47 | 13 % → 3 % | 66.3 px | 0.33 | 0.20 | 1 |
| stroke 48 | 19 % → 2 % | 43.4 px | 0.33 | 0.12 | 7 |
| stroke 49 | 25 % → 0 % | 84.8 px | 0.00 | 0.00 | 5 |
| stroke 50 | 13 % → 8 % | 72.4 px | 0.34 | 0.64 | 1 |
| stroke 51 | 3 % → 0 % | 20.6 px | 0.00 | 0.00 | 0 |
| stroke 52 | 16 % → 0 % | 38.2 px | 0.00 | 0.00 | 16 |
| stroke 53 | 12 % → 6 % | 17.5 px | 0.34 | 0.49 | 31 |
| stroke 54 | 16 % → 9 % | 30.1 px | 0.34 | 0.56 | 6 |
| stroke 55 | 11 % → 0 % | 29.5 px | 0.00 | 0.00 | 11 |
| stroke 56 | 18 % → 0 % | 47.5 px | 0.00 | 0.00 | 12 |
| stroke 57 | 23 % → 5 % | 31.1 px | 0.34 | 0.23 | 58 |
| stroke 58 | 22 % → 9 % | 62.7 px | 0.34 | 0.42 | 4 |
| stroke 59 | 26 % → 3 % | 37.2 px | 0.34 | 0.11 | 86 |
| stroke 60 | 33 % → 3 % | 48.3 px | 0.34 | 0.08 | 173 |
| stroke 61 | 42 % → 2 % | 60.2 px | 0.34 | 0.04 | 81 |
| stroke 62 | 44 % → 0 % | 60.9 px | 0.00 | 0.00 | 36 |
| stroke 63 | 21 % → 0 % | 13.3 px | 0.00 | 0.00 | 64 |
| stroke 64 | 33 % → 0 % | 44.6 px | 0.00 | 0.00 | 9 |
| stroke 65 | 40 % → 0 % | 195.5 px | 0.00 | 0.00 | 0 |
| stroke 66 | 36 % → 0 % | 25.3 px | 0.00 | 0.00 | 61 |
| stroke 67 | 10 % → 0 % | 20.5 px | 0.00 | 0.00 | 14 |
| stroke 68 | 6 % → 4 % | 24.0 px | 0.33 | 0.69 | 10 |
| stroke 69 | 5 % → 47 % | 23.4 px | 0.34 | 10.05 | 9 |
| stroke 70 | 6 % → 21 % | 28.1 px | 0.34 | 3.71 | 7 |
| stroke 71 | 10 % → 47 % | 30.2 px | 0.34 | 4.72 | 9 |
| stroke 72 | 5 % → 0 % | 23.0 px | 0.00 | 0.00 | 1 |
| stroke 73 | 7 % → 7 % | 30.7 px | 0.33 | 1.10 | 2 |
| stroke 74 | 7 % → 6 % | 25.9 px | 0.34 | 0.96 | 10 |
| stroke 75 | 8 % → 9 % | 23.2 px | 0.33 | 1.24 | 9 |
| stroke 76 | 17 % → 0 % | 87.7 px | 0.00 | 0.00 | 3 |
| stroke 77 | 18 % → 41 % | 60.5 px | 0.34 | 2.25 | 7 |
| stroke 78 | 16 % → 46 % | 44.9 px | 0.34 | 2.89 | 13 |
| stroke 79 | 5 % → 30 % | 20.8 px | 0.34 | 5.62 | 2 |
| stroke 80 | 9 % → 17 % | 46.4 px | 0.33 | 1.87 | 1 |
| stroke 81 | 11 % → 0 % | 53.3 px | 0.00 | 0.00 | 4 |
| stroke 82 | 8 % → 15 % | 30.0 px | 0.34 | 1.81 | 12 |
| stroke 83 | 16 % → 28 % | 80.0 px | 0.34 | 1.74 | 1 |
| stroke 84 | 11 % → 38 % | 34.4 px | 0.34 | 3.28 | 5 |
| stroke 85 | 17 % → 0 % | 72.0 px | 0.00 | 0.00 | 5 |
| stroke 86 | 27 % → 46 % | 111.5 px | 0.34 | 1.72 | 5 |
| stroke 87 | 17 % → 33 % | 80.3 px | 0.34 | 2.00 | 2 |
| stroke 88 | 18 % → 12 % | 63.7 px | 0.34 | 0.64 | 10 |
| stroke 89 | 16 % → 32 % | 58.7 px | 0.34 | 1.96 | 3 |
| stroke 90 | 21 % → 19 % | 108.2 px | 0.34 | 0.90 | 2 |
| stroke 91 | 24 % → 0 % | 72.5 px | 0.00 | 0.00 | 8 |
| stroke 92 | 24 % → 11 % | 59.4 px | 0.34 | 0.46 | 7 |
| stroke 93 | 5 % → 0 % | 22.8 px | 0.01 | 0.00 | 2 |
| stroke 94 | 20 % → 29 % | 61.1 px | 0.34 | 1.45 | 8 |
| stroke 95 | 16 % → 16 % | 59.6 px | 0.33 | 0.98 | 2 |
| stroke 96 | 24 % → 21 % | 110.2 px | 0.34 | 0.86 | 2 |
| stroke 97 | 22 % → 12 % | 111.0 px | 0.33 | 0.55 | 10 |
| stroke 98 | 25 % → 21 % | 79.8 px | 0.34 | 0.83 | 14 |
| stroke 99 | 14 % → 14 % | 69.0 px | 0.34 | 1.05 | 2 |
| stroke 100 | 40 % → 29 % | 207.4 px | 0.34 | 0.71 | 2 |
| stroke 101 | 35 % → 23 % | 161.9 px | 0.34 | 0.65 | 3 |
| stroke 102 | 38 % → 29 % | 153.0 px | 0.34 | 0.76 | 3 |
| stroke 103 | 27 % → 18 % | 100.1 px | 0.34 | 0.67 | 12 |
| stroke 104 | 38 % → 35 % | 106.0 px | 0.34 | 0.94 | 13 |
| stroke 105 | 37 % → 28 % | 151.3 px | 0.34 | 0.76 | 4 |
| stroke 106 | 38 % → 39 % | 156.5 px | 0.34 | 1.03 | 4 |
| stroke 107 | 16 % → 12 % | 75.2 px | 0.34 | 0.77 | 12 |
| stroke 108 | 31 % → 17 % | 147.2 px | 0.34 | 0.57 | 2 |
| stroke 109 | 36 % → 10 % | 167.1 px | 0.34 | 0.28 | 4 |
| stroke 110 | 43 % → 24 % | 138.3 px | 0.34 | 0.56 | 7 |
| stroke 111 | 32 % → 15 % | 121.2 px | 0.33 | 0.46 | 7 |
| stroke 112 | 14 % → 36 % | 51.7 px | 0.34 | 2.66 | 2 |
| stroke 113 | 36 % → 5 % | 174.7 px | 0.32 | 0.15 | 2 |
| stroke 114 | 34 % → 7 % | 91.1 px | 0.33 | 0.20 | 17 |
| stroke 115 | 38 % → 17 % | 191.7 px | 0.34 | 0.45 | 7 |
| stroke 116 | 49 % → 40 % | 247.5 px | 0.35 | 0.82 | 3 |
| stroke 117 | 53 % → 33 % | 201.4 px | 0.34 | 0.64 | 2 |
| stroke 118 | 46 % → 14 % | 212.6 px | 0.34 | 0.31 | 2 |
| stroke 119 | 28 % → 29 % | 121.9 px | 0.34 | 1.00 | 8 |
| stroke 120 | 31 % → 29 % | 105.3 px | 0.34 | 0.94 | 8 |
| stroke 121 | 55 % → 43 % | 240.8 px | 0.34 | 0.78 | 4 |
| stroke 122 | 10 % → 0 % | 19.0 px | 0.00 | 0.00 | 13 |
| stroke 123 | 7 % → 0 % | 26.4 px | 0.00 | 0.00 | 3 |
| stroke 124 | 17 % → 0 % | 58.9 px | 0.00 | 0.00 | 7 |
| stroke 125 | 14 % → 0 % | 41.7 px | 0.00 | 0.00 | 13 |
| stroke 126 | 9 % → 0 % | 30.0 px | 0.00 | 0.00 | 3 |
| stroke 127 | 27 % → 0 % | 106.8 px | 0.00 | 0.00 | 5 |
| stroke 128 | 10 % → 18 % | 21.2 px | 0.34 | 1.78 | 12 |
| stroke 129 | 12 % → 40 % | 16.4 px | 0.35 | 3.43 | 30 |
| stroke 130 | 21 % → 33 % | 60.1 px | 0.34 | 1.54 | 7 |
| stroke 131 | 14 % → 55 % | 53.3 px | 0.34 | 3.93 | 6 |
| stroke 132 | 21 % → 58 % | 95.5 px | 0.34 | 2.76 | 2 |
| stroke 133 | 14 % → 58 % | 74.4 px | 0.35 | 4.04 | 4 |
| stroke 134 | 28 % → 74 % | 128.7 px | 0.35 | 2.65 | 9 |
| stroke 135 | 24 % → 28 % | 57.8 px | 0.35 | 1.17 | 24 |
| stroke 136 | 31 % → 52 % | 145.8 px | 0.35 | 1.67 | 2 |
| stroke 137 | 34 % → 36 % | 160.9 px | 0.34 | 1.08 | 4 |
| stroke 138 | 16 % → 34 % | 58.0 px | 0.34 | 2.17 | 3 |
| stroke 139 | 25 % → 32 % | 125.6 px | 0.34 | 1.29 | 2 |
| stroke 140 | 29 % → 32 % | 82.0 px | 0.34 | 1.09 | 4 |
| stroke 141 | 30 % → 1 % | 132.8 px | 0.32 | 0.04 | 7 |
| stroke 142 | 18 % → 54 % | 87.8 px | 0.34 | 3.06 | 10 |
| stroke 143 | 24 % → 60 % | 101.0 px | 0.34 | 2.53 | 3 |
| stroke 144 | 34 % → 0 % | 92.4 px | 0.00 | 0.00 | 13 |
| stroke 145 | 32 % → 0 % | 106.5 px | 0.00 | 0.00 | 8 |
| stroke 146 | 37 % → 0 % | 149.4 px | 0.33 | 0.01 | 5 |
| stroke 147 | 24 % → 27 % | 113.7 px | 0.34 | 1.12 | 2 |
| stroke 148 | 44 % → 24 % | 124.4 px | 0.34 | 0.55 | 9 |
| stroke 149 | 55 % → 31 % | 278.1 px | 0.34 | 0.57 | 2 |
| stroke 150 | 58 % → 31 % | 218.3 px | 0.34 | 0.54 | 3 |
| stroke 151 | 28 % → 0 % | 88.1 px | 0.00 | 0.00 | 5 |
| stroke 152 | 24 % → 0 % | 54.7 px | 0.00 | 0.00 | 12 |
| stroke 153 | 14 % → 7 % | 36.3 px | 0.34 | 0.48 | 4 |
| stroke 154 | 18 % → 0 % | 73.7 px | 0.28 | 0.03 | 5 |
| stroke 155 | 35 % → 0 % | 145.0 px | 0.34 | 0.00 | 6 |
| stroke 156 | 39 % → 0 % | 107.5 px | 0.00 | 0.00 | 4 |
| stroke 157 | 18 % → 0 % | 52.4 px | 0.00 | 0.00 | 6 |
| stroke 158 | 8 % → 0 % | 33.8 px | 0.00 | 0.00 | 2 |
| stroke 159 | 11 % → 0 % | 46.0 px | 0.00 | 0.00 | 2 |
| stroke 160 | 6 % → 4 % | 20.6 px | 0.34 | 0.67 | 13 |
| stroke 161 | 5 % → 14 % | 15.0 px | 0.34 | 3.03 | 5 |
| stroke 162 | 9 % → 13 % | 26.6 px | 0.34 | 1.41 | 12 |
| stroke 163 | 13 % → 10 % | 49.0 px | 0.33 | 0.81 | 2 |
| stroke 164 | 20 % → 4 % | 113.5 px | 0.34 | 0.21 | 1 |
| stroke 165 | 10 % → 16 % | 59.9 px | 0.34 | 1.53 | 0 |
| stroke 166 | 19 % → 1 % | 74.6 px | 0.33 | 0.07 | 3 |
| stroke 167 | 3 % → 12 % | 17.1 px | 0.34 | 4.38 | 0 |
| stroke 168 | 5 % → 22 % | 14.2 px | 0.34 | 4.70 | 9 |
| stroke 169 | 10 % → 14 % | 26.8 px | 0.34 | 1.46 | 8 |
| stroke 170 | 21 % → 0 % | 102.6 px | 0.00 | 0.00 | 1 |
| stroke 171 | 5 % → 9 % | 24.2 px | 0.33 | 1.76 | 2 |
| stroke 172 | 10 % → 17 % | 48.1 px | 0.34 | 1.63 | 3 |
| stroke 173 | 17 % → 14 % | 48.3 px | 0.34 | 0.85 | 19 |
| stroke 174 | 23 % → 0 % | 116.5 px | 0.00 | 0.00 | 1 |
| stroke 175 | 21 % → 0 % | 95.1 px | 0.00 | 0.00 | 1 |
| stroke 176 | 18 % → 5 % | 55.7 px | 0.33 | 0.30 | 8 |
| stroke 177 | 21 % → 1 % | 53.7 px | 0.33 | 0.02 | 18 |
| stroke 178 | 8 % → 2 % | 29.5 px | 0.33 | 0.20 | 7 |
| stroke 179 | 18 % → 11 % | 45.5 px | 0.34 | 0.60 | 6 |
| stroke 180 | 23 % → 0 % | 68.5 px | 0.17 | 0.00 | 6 |
| stroke 181 | 23 % → 0 % | 114.2 px | 0.00 | 0.00 | 1 |
| stroke 182 | 9 % → 0 % | 51.2 px | 0.00 | 0.00 | 1 |
| stroke 183 | 19 % → 1 % | 77.6 px | 0.33 | 0.06 | 1 |
| stroke 184 | 22 % → 0 % | 125.4 px | 0.00 | 0.00 | 1 |
| stroke 185 | 32 % → 0 % | 179.1 px | 0.32 | 0.01 | 1 |
| stroke 186 | 22 % → 3 % | 56.2 px | 0.34 | 0.15 | 8 |
| stroke 187 | 36 % → 0 % | 128.7 px | 0.00 | 0.00 | 2 |
| stroke 188 | 16 % → 0 % | 39.4 px | 0.33 | 0.01 | 6 |
| stroke 189 | 26 % → 0 % | 163.6 px | 0.00 | 0.00 | 4 |
| stroke 190 | 25 % → 2 % | 61.7 px | 0.33 | 0.10 | 14 |
| stroke 191 | 19 % → 0 % | 60.2 px | 0.00 | 0.00 | 12 |
| stroke 192 | 32 % → 0 % | 94.3 px | 0.00 | 0.00 | 2 |
| stroke 193 | 26 % → 0 % | 95.8 px | 0.00 | 0.00 | 1 |
| stroke 194 | 28 % → 0 % | 68.2 px | 0.00 | 0.00 | 14 |
| stroke 195 | 22 % → 0 % | 57.0 px | 0.00 | 0.00 | 7 |
| stroke 196 | 30 % → 3 % | 73.9 px | 0.35 | 0.10 | 10 |
| stroke 197 | 29 % → 0 % | 120.0 px | 0.00 | 0.00 | 6 |
| stroke 198 | 26 % → 0 % | 138.7 px | 0.00 | 0.00 | 1 |
| stroke 199 | 33 % → 0 % | 83.0 px | 0.00 | 0.00 | 18 |
| stroke 200 | 33 % → 0 % | 112.6 px | 0.00 | 0.00 | 4 |
| stroke 201 | 27 % → 0 % | 173.8 px | 0.00 | 0.00 | 1 |
| stroke 202 | 29 % → 0 % | 141.2 px | 0.00 | 0.00 | 1 |
| stroke 203 | 30 % → 0 % | 138.4 px | 0.00 | 0.00 | 1 |
| stroke 204 | 31 % → 0 % | 210.3 px | 0.00 | 0.00 | 0 |
| stroke 205 | 31 % → 0 % | 153.8 px | 0.00 | 0.00 | 2 |
| stroke 206 | 30 % → 0 % | 81.8 px | 0.00 | 0.00 | 4 |
| stroke 207 | 29 % → 0 % | 177.1 px | 0.00 | 0.00 | 0 |
| stroke 208 | 30 % → 0 % | 117.1 px | 0.00 | 0.00 | 5 |
| stroke 209 | 28 % → 0 % | 159.2 px | 0.00 | 0.00 | 0 |
| stroke 210 | 27 % → 0 % | 142.1 px | 0.00 | 0.00 | 1 |
| stroke 211 | 26 % → 0 % | 167.4 px | 0.00 | 0.00 | 1 |
| stroke 212 | 21 % → 0 % | 99.8 px | 0.00 | 0.00 | 3 |
| stroke 213 | 28 % → 0 % | 72.1 px | 0.00 | 0.00 | 20 |
| stroke 214 | 31 % → 0 % | 116.1 px | 0.00 | 0.00 | 9 |
| stroke 215 | 16 % → 4 % | 49.3 px | 0.33 | 0.23 | 3 |
| stroke 216 | 31 % → 0 % | 100.2 px | 0.00 | 0.00 | 8 |
| stroke 217 | 28 % → 0 % | 123.7 px | 0.00 | 0.00 | 3 |
| stroke 218 | 32 % → 0 % | 174.0 px | 0.00 | 0.00 | 2 |
| stroke 219 | 23 % → 0 % | 95.9 px | 0.17 | 0.00 | 11 |
| stroke 220 | 29 % → 0 % | 103.4 px | 0.00 | 0.00 | 3 |
| stroke 221 | 27 % → 3 % | 130.7 px | 0.32 | 0.11 | 2 |
| stroke 222 | 27 % → 0 % | 82.9 px | 0.00 | 0.00 | 5 |
| stroke 223 | 32 % → 1 % | 83.4 px | 0.32 | 0.03 | 4 |
| stroke 224 | 28 % → 0 % | 136.0 px | 0.00 | 0.00 | 2 |
| stroke 225 | 34 % → 0 % | 105.4 px | 0.00 | 0.00 | 3 |
| stroke 226 | 33 % → 5 % | 111.9 px | 0.33 | 0.15 | 2 |
| stroke 227 | 26 % → 0 % | 121.1 px | 0.00 | 0.00 | 1 |
| stroke 228 | 31 % → 3 % | 76.5 px | 0.33 | 0.10 | 5 |
| stroke 229 | 13 % → 8 % | 59.8 px | 0.33 | 0.62 | 1 |
| stroke 230 | 33 % → 1 % | 78.7 px | 0.33 | 0.04 | 15 |
| stroke 231 | 17 % → 8 % | 91.8 px | 0.33 | 0.48 | 4 |
| stroke 232 | 39 % → 0 % | 103.8 px | 0.00 | 0.00 | 22 |
| stroke 233 | 24 % → 5 % | 62.9 px | 0.33 | 0.20 | 12 |
| stroke 234 | 39 % → 0 % | 98.4 px | 0.29 | 0.01 | 21 |
| stroke 235 | 40 % → 0 % | 101.9 px | 0.00 | 0.00 | 6 |
| stroke 236 | 21 % → 5 % | 57.3 px | 0.33 | 0.24 | 6 |
| stroke 237 | 29 % → 2 % | 71.6 px | 0.33 | 0.07 | 17 |
| stroke 238 | 39 % → 0 % | 97.0 px | 0.00 | 0.00 | 14 |
| stroke 239 | 39 % → 0 % | 98.4 px | 0.00 | 0.00 | 6 |
| stroke 240 | 38 % → 0 % | 110.9 px | 0.00 | 0.00 | 16 |
| stroke 241 | 35 % → 0 % | 165.0 px | 0.00 | 0.00 | 4 |
| stroke 242 | 12 % → 36 % | 40.8 px | 0.34 | 3.02 | 7 |
| stroke 243 | 23 % → 31 % | 96.1 px | 0.34 | 1.36 | 15 |
| stroke 244 | 9 % → 30 % | 38.8 px | 0.34 | 3.13 | 9 |
| stroke 245 | 15 % → 28 % | 53.5 px | 0.34 | 1.82 | 12 |
| stroke 246 | 38 % → 42 % | 108.5 px | 0.34 | 1.13 | 23 |
| stroke 247 | 40 % → 40 % | 173.5 px | 0.34 | 1.00 | 14 |
| stroke 248 | 10 % → 57 % | 34.2 px | 0.34 | 5.74 | 15 |
| stroke 249 | 12 % → 27 % | 36.1 px | 0.34 | 2.29 | 28 |
| stroke 250 | 25 % → 31 % | 69.7 px | 0.34 | 1.22 | 17 |
| stroke 251 | 16 % → 72 % | 66.3 px | 0.34 | 4.51 | 29 |
| stroke 252 | 26 % → 48 % | 75.2 px | 0.34 | 1.84 | 26 |
| stroke 253 | 30 % → 47 % | 105.0 px | 0.34 | 1.56 | 10 |
| stroke 254 | 15 % → 40 % | 69.1 px | 0.34 | 2.60 | 4 |
| stroke 255 | 20 % → 56 % | 56.9 px | 0.35 | 2.76 | 18 |
| stroke 256 | 23 % → 43 % | 63.9 px | 0.34 | 1.85 | 29 |
| stroke 257 | 33 % → 34 % | 121.4 px | 0.34 | 1.04 | 31 |
| stroke 258 | 47 % → 58 % | 214.0 px | 0.34 | 1.24 | 13 |
| stroke 259 | 16 % → 51 % | 70.6 px | 0.35 | 3.16 | 12 |
| stroke 260 | 45 % → 52 % | 168.8 px | 0.34 | 1.15 | 21 |
| stroke 261 | 23 % → 45 % | 95.8 px | 0.34 | 1.98 | 5 |
| stroke 262 | 33 % → 62 % | 156.0 px | 0.34 | 1.85 | 13 |
| stroke 263 | 42 % → 63 % | 182.2 px | 0.35 | 1.49 | 10 |
| stroke 264 | 54 % → 59 % | 201.5 px | 0.34 | 1.10 | 14 |
| stroke 265 | 46 % → 63 % | 174.7 px | 0.35 | 1.37 | 8 |
| stroke 266 | 40 % → 50 % | 189.9 px | 0.34 | 1.26 | 22 |
| stroke 267 | 74 % → 83 % | 355.4 px | 0.35 | 1.12 | 22 |
| stroke 268 | 64 % → 66 % | 228.8 px | 0.34 | 1.03 | 37 |
| stroke 269 | 52 % → 53 % | 225.5 px | 0.35 | 1.02 | 5 |
| stroke 270 | 56 % → 56 % | 181.0 px | 0.35 | 1.00 | 24 |
| stroke 271 | 21 % → 21 % | 49.6 px | 0.34 | 1.00 | 43 |
| stroke 272 | 13 % → 21 % | 66.0 px | 0.34 | 1.65 | 3 |
| stroke 273 | 16 % → 16 % | 69.3 px | 0.34 | 1.02 | 10 |
| stroke 274 | 10 % → 38 % | 36.0 px | 0.34 | 3.75 | 15 |
| stroke 275 | 18 % → 44 % | 75.1 px | 0.34 | 2.39 | 14 |
| stroke 276 | 25 % → 36 % | 103.4 px | 0.34 | 1.42 | 20 |
| stroke 277 | 28 % → 33 % | 105.9 px | 0.34 | 1.18 | 7 |
| stroke 278 | 38 % → 40 % | 144.5 px | 0.34 | 1.06 | 12 |
| stroke 279 | 8 % → 34 % | 42.3 px | 0.34 | 4.05 | 12 |
| stroke 280 | 15 % → 26 % | 51.2 px | 0.34 | 1.72 | 15 |
| stroke 281 | 20 % → 26 % | 84.5 px | 0.34 | 1.33 | 5 |
| stroke 282 | 23 % → 50 % | 77.9 px | 0.34 | 2.14 | 11 |
| stroke 283 | 26 % → 48 % | 75.0 px | 0.34 | 1.83 | 12 |
| stroke 284 | 12 % → 27 % | 55.8 px | 0.33 | 2.18 | 5 |
| stroke 285 | 16 % → 20 % | 74.3 px | 0.33 | 1.29 | 9 |
| stroke 286 | 28 % → 44 % | 118.3 px | 0.34 | 1.60 | 9 |
| stroke 287 | 38 % → 55 % | 168.9 px | 0.34 | 1.45 | 7 |
| stroke 288 | 44 % → 52 % | 156.5 px | 0.34 | 1.18 | 12 |
| stroke 289 | 34 % → 34 % | 125.9 px | 0.34 | 1.00 | 12 |
| stroke 290 | 8 % → 8 % | 35.9 px | 0.33 | 1.00 | 3 |
| stroke 291 | 10 % → 11 % | 28.0 px | 0.34 | 1.01 | 34 |
| stroke 292 | 10 % → 10 % | 27.0 px | 0.34 | 1.00 | 38 |

Numbers say: wet paint spreads well beyond the stroke.

## Refs v3 · #19 Guston charcoal hand — own sheet
own sheet 800 × 800 · Charcoal 1.00 · 64 px · 13.4 s

![Refs v3 · #19 Guston charcoal hand — own sheet](Refs-v3-19-Guston-charcoal-hand-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 4 % → 26 % | 38.6 px | 0.59 | 6.78 | 25 |
| stroke 2 | 7 % → 27 % | 80.0 px | 0.59 | 3.92 | 19 |
| stroke 3 | 8 % → 26 % | 199.4 px | 0.59 | 3.29 | 20 |
| stroke 4 | 10 % → 29 % | 111.3 px | 0.59 | 2.94 | 34 |
| stroke 5 | 9 % → 30 % | 126.8 px | 0.59 | 3.28 | 63 |
| stroke 6 | 16 % → 33 % | 427.2 px | 0.59 | 2.12 | 16 |
| stroke 7 | 16 % → 31 % | 474.7 px | 0.59 | 1.90 | 11 |
| stroke 8 | 16 % → 34 % | 217.1 px | 0.59 | 2.18 | 31 |
| stroke 9 | 2 % → 67 % | 37.2 px | 0.60 | 31.39 | 36 |
| stroke 10 | 4 % → 67 % | 83.2 px | 0.60 | 15.88 | 38 |
| stroke 11 | 3 % → 40 % | 47.1 px | 0.60 | 11.72 | 17 |
| stroke 12 | 6 % → 45 % | 97.3 px | 0.60 | 7.12 | 42 |
| stroke 13 | 3 % → 48 % | 57.3 px | 0.60 | 17.74 | 5 |
| stroke 14 | 4 % → 67 % | 150.9 px | 0.60 | 17.66 | 18 |
| stroke 15 | 15 % → 46 % | 207.8 px | 0.60 | 3.16 | 32 |
| stroke 16 | 8 % → 71 % | 162.3 px | 0.60 | 9.06 | 18 |
| stroke 17 | 10 % → 34 % | 324.7 px | 0.60 | 3.32 | 13 |
| stroke 18 | 2 % → 48 % | 60.1 px | 0.60 | 31.19 | 9 |
| stroke 19 | 5 % → 57 % | 122.7 px | 0.60 | 10.36 | 24 |
| stroke 20 | 4 % → 36 % | 140.3 px | 0.60 | 9.13 | 13 |
| stroke 21 | 10 % → 53 % | 193.7 px | 0.60 | 5.39 | 20 |
| stroke 22 | 13 % → 69 % | 432.5 px | 0.60 | 5.19 | 19 |
| stroke 23 | 21 % → 47 % | 179.6 px | 0.60 | 2.25 | 63 |
| stroke 24 | 15 % → 34 % | 114.5 px | 0.60 | 2.29 | 96 |
| stroke 25 | 9 % → 53 % | 184.0 px | 0.60 | 6.17 | 23 |
| stroke 26 | 14 % → 72 % | 343.7 px | 0.60 | 5.06 | 29 |
| stroke 27 | 15 % → 67 % | 371.2 px | 0.60 | 4.53 | 26 |
| stroke 28 | 17 % → 68 % | 186.9 px | 0.60 | 3.92 | 132 |
| stroke 29 | 19 % → 71 % | 462.8 px | 0.60 | 3.64 | 23 |
| stroke 30 | 22 % → 53 % | 183.0 px | 0.60 | 2.37 | 100 |
| stroke 31 | 10 % → 47 % | 311.8 px | 0.60 | 4.88 | 17 |
| stroke 32 | 11 % → 48 % | 397.8 px | 0.60 | 4.30 | 25 |
| stroke 33 | 11 % → 43 % | 311.5 px | 0.60 | 3.97 | 35 |
| stroke 34 | 21 % → 61 % | 368.2 px | 0.60 | 2.90 | 61 |
| stroke 35 | 21 % → 58 % | 595.3 px | 0.60 | 2.79 | 68 |
| stroke 36 | 19 % → 39 % | 130.1 px | 0.60 | 2.04 | 53 |
| stroke 37 | 27 % → 59 % | 603.2 px | 0.60 | 2.17 | 45 |
| stroke 38 | 18 % → 43 % | 277.2 px | 0.60 | 2.33 | 42 |
| stroke 39 | 23 % → 64 % | 668.8 px | 0.60 | 2.79 | 8 |
| stroke 40 | 24 % → 51 % | 422.2 px | 0.60 | 2.10 | 20 |
| stroke 41 | 26 % → 43 % | 502.6 px | 0.60 | 1.69 | 39 |
| stroke 42 | 27 % → 68 % | 537.1 px | 0.60 | 2.53 | 33 |
| stroke 43 | 13 % → 40 % | 234.6 px | 0.60 | 3.04 | 24 |
| stroke 44 | 25 % → 51 % | 203.7 px | 0.60 | 2.07 | 97 |
| stroke 45 | 18 % → 30 % | 144.6 px | 0.60 | 1.62 | 105 |
| stroke 46 | 29 % → 66 % | 744.0 px | 0.60 | 2.31 | 26 |
| stroke 47 | 33 % → 66 % | 1113.1 px | 0.60 | 2.04 | 8 |
| stroke 48 | 33 % → 65 % | 690.6 px | 0.60 | 1.96 | 30 |
| stroke 49 | 13 % → 34 % | 193.0 px | 0.60 | 2.66 | 55 |
| stroke 50 | 35 % → 63 % | 820.9 px | 0.60 | 1.81 | 47 |
| stroke 51 | 38 % → 68 % | 658.2 px | 0.60 | 1.77 | 44 |
| stroke 52 | 18 % → 44 % | 370.2 px | 0.60 | 2.40 | 35 |
| stroke 53 | 17 % → 45 % | 314.3 px | 0.60 | 2.59 | 51 |
| stroke 54 | 18 % → 41 % | 495.3 px | 0.60 | 2.31 | 21 |
| stroke 55 | 30 % → 47 % | 629.4 px | 0.60 | 1.57 | 33 |
| stroke 56 | 37 % → 69 % | 1251.8 px | 0.60 | 1.88 | 9 |
| stroke 57 | 28 % → 54 % | 889.6 px | 0.60 | 1.91 | 8 |
| stroke 58 | 21 % → 39 % | 451.3 px | 0.60 | 1.90 | 13 |
| stroke 59 | 40 % → 69 % | 980.9 px | 0.60 | 1.73 | 20 |
| stroke 60 | 42 % → 62 % | 715.7 px | 0.60 | 1.48 | 38 |
| stroke 61 | 24 % → 48 % | 712.0 px | 0.60 | 2.05 | 6 |
| stroke 62 | 32 % → 43 % | 572.2 px | 0.60 | 1.34 | 66 |
| stroke 63 | 44 % → 70 % | 845.5 px | 0.60 | 1.60 | 61 |
| stroke 64 | 27 % → 45 % | 138.7 px | 0.60 | 1.64 | 197 |
| stroke 65 | 39 % → 60 % | 351.4 px | 0.60 | 1.53 | 173 |
| stroke 66 | 23 % → 41 % | 471.0 px | 0.60 | 1.75 | 41 |
| stroke 67 | 37 % → 51 % | 339.6 px | 0.60 | 1.38 | 123 |
| stroke 68 | 50 % → 67 % | 638.6 px | 0.60 | 1.34 | 66 |
| stroke 69 | 41 % → 64 % | 1066.4 px | 0.60 | 1.56 | 25 |
| stroke 70 | 31 % → 46 % | 810.9 px | 0.60 | 1.47 | 8 |
| stroke 71 | 25 % → 38 % | 865.5 px | 0.60 | 1.51 | 13 |
| stroke 72 | 44 % → 65 % | 583.3 px | 0.60 | 1.47 | 43 |
| stroke 73 | 51 % → 69 % | 1655.1 px | 0.60 | 1.36 | 14 |
| stroke 74 | 39 % → 44 % | 161.1 px | 0.60 | 1.13 | 279 |
| stroke 75 | 40 % → 52 % | 978.5 px | 0.60 | 1.31 | 17 |
| stroke 76 | 56 % → 72 % | 1311.9 px | 0.60 | 1.28 | 24 |
| stroke 77 | 59 % → 67 % | 911.3 px | 0.60 | 1.14 | 29 |
| stroke 78 | 50 % → 62 % | 1348.3 px | 0.60 | 1.24 | 16 |
| stroke 79 | 44 % → 56 % | 1846.5 px | 0.60 | 1.27 | 11 |
| stroke 80 | 49 % → 60 % | 1408.3 px | 0.60 | 1.23 | 20 |
| stroke 81 | 40 % → 45 % | 376.4 px | 0.60 | 1.14 | 97 |
| stroke 82 | 43 % → 55 % | 840.8 px | 0.60 | 1.28 | 48 |
| stroke 83 | 51 % → 54 % | 1819.9 px | 0.60 | 1.07 | 17 |
| stroke 84 | 56 % → 69 % | 965.0 px | 0.60 | 1.22 | 34 |
| stroke 85 | 36 % → 38 % | 509.2 px | 0.60 | 1.06 | 35 |
| stroke 86 | 32 % → 40 % | 603.3 px | 0.60 | 1.25 | 23 |
| stroke 87 | 41 % → 48 % | 578.6 px | 0.60 | 1.16 | 37 |
| stroke 88 | 47 % → 56 % | 637.3 px | 0.60 | 1.18 | 52 |
| stroke 89 | 48 % → 58 % | 1493.6 px | 0.60 | 1.20 | 22 |
| stroke 90 | 31 % → 34 % | 780.5 px | 0.60 | 1.12 | 16 |
| stroke 91 | 39 % → 42 % | 800.3 px | 0.60 | 1.07 | 32 |
| stroke 92 | 60 % → 65 % | 1122.0 px | 0.60 | 1.09 | 36 |
| stroke 93 | 49 % → 55 % | 1611.3 px | 0.60 | 1.12 | 29 |
| stroke 94 | 38 % → 44 % | 496.5 px | 0.60 | 1.17 | 39 |
| stroke 95 | 60 % → 65 % | 1231.3 px | 0.60 | 1.08 | 27 |
| stroke 96 | 33 % → 37 % | 1162.8 px | 0.60 | 1.12 | 23 |
| stroke 97 | 42 % → 44 % | 344.3 px | 0.60 | 1.05 | 78 |
| stroke 98 | 63 % → 66 % | 2506.7 px | 0.60 | 1.05 | 7 |
| stroke 99 | 65 % → 70 % | 2602.2 px | 0.60 | 1.07 | 16 |
| stroke 100 | 46 % → 47 % | 906.0 px | 0.60 | 1.02 | 45 |
| stroke 101 | 58 % → 62 % | 1163.8 px | 0.60 | 1.06 | 53 |
| stroke 102 | 64 % → 67 % | 1385.9 px | 0.60 | 1.05 | 40 |
| stroke 103 | 31 % → 34 % | 1376.6 px | 0.60 | 1.10 | 8 |
| stroke 104 | 61 % → 67 % | 2566.1 px | 0.60 | 1.09 | 7 |
| stroke 105 | 56 % → 58 % | 1463.1 px | 0.60 | 1.03 | 46 |
| stroke 106 | 64 % → 68 % | 1469.6 px | 0.60 | 1.07 | 31 |
| stroke 107 | 59 % → 61 % | 1416.3 px | 0.60 | 1.03 | 28 |
| stroke 108 | 68 % → 69 % | 731.5 px | 0.60 | 1.02 | 70 |
| stroke 109 | 63 % → 63 % | 2357.4 px | 0.60 | 1.00 | 28 |
| stroke 110 | 42 % → 42 % | 820.5 px | 0.60 | 1.00 | 32 |
| stroke 111 | 64 % → 65 % | 1175.6 px | 0.60 | 1.03 | 41 |
| stroke 112 | 54 % → 55 % | 787.5 px | 0.60 | 1.03 | 65 |
| stroke 113 | 68 % → 68 % | 1639.1 px | 0.60 | 1.00 | 25 |
| stroke 114 | 38 % → 38 % | 737.7 px | 0.60 | 1.00 | 35 |
| stroke 115 | 32 % → 32 % | 703.7 px | 0.59 | 1.00 | 25 |

Numbers say: wet paint spreads well beyond the stroke.

## Refs v3 · #20 Orange crayon — own sheet
own sheet 800 × 1245 · Wax 1.00 · 34 px · 15.0 s

![Refs v3 · #20 Orange crayon — own sheet](Refs-v3-20-Orange-crayon-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 8 % → 56 % | 34.9 px | 0.54 | 6.83 | 32 |
| stroke 2 | 16 % → 59 % | 43.8 px | 0.53 | 3.67 | 53 |
| stroke 3 | 21 % → 59 % | 51.1 px | 0.53 | 2.85 | 68 |
| stroke 4 | 26 % → 59 % | 63.3 px | 0.53 | 2.30 | 137 |
| stroke 5 | 38 % → 45 % | 168.6 px | 0.53 | 1.18 | 53 |
| stroke 6 | 32 % → 77 % | 78.1 px | 0.54 | 2.44 | 84 |
| stroke 7 | 43 % → 43 % | 388.0 px | 0.53 | 1.00 | 12 |
| stroke 8 | 32 % → 77 % | 77.9 px | 0.54 | 2.44 | 115 |
| stroke 9 | 32 % → 76 % | 83.2 px | 0.54 | 2.36 | 121 |
| stroke 10 | 34 % → 76 % | 92.4 px | 0.54 | 2.24 | 147 |
| stroke 11 | 41 % → 80 % | 104.5 px | 0.54 | 1.94 | 107 |
| stroke 12 | 47 % → 85 % | 119.2 px | 0.54 | 1.83 | 101 |
| stroke 13 | 50 % → 85 % | 143.7 px | 0.54 | 1.72 | 109 |
| stroke 14 | 51 % → 88 % | 151.2 px | 0.54 | 1.72 | 107 |
| stroke 15 | 11 % → 34 % | 45.9 px | 0.54 | 3.04 | 84 |
| stroke 16 | 52 % → 85 % | 151.0 px | 0.54 | 1.65 | 160 |
| stroke 17 | 42 % → 68 % | 132.0 px | 0.54 | 1.62 | 170 |
| stroke 18 | 39 % → 68 % | 132.9 px | 0.54 | 1.73 | 118 |
| stroke 19 | 60 % → 85 % | 286.2 px | 0.54 | 1.42 | 7 |
| stroke 20 | 46 % → 77 % | 159.7 px | 0.54 | 1.66 | 72 |
| stroke 21 | 52 % → 83 % | 350.1 px | 0.54 | 1.60 | 7 |
| stroke 22 | 50 % → 84 % | 168.7 px | 0.54 | 1.68 | 45 |
| stroke 23 | 47 % → 81 % | 133.3 px | 0.54 | 1.71 | 83 |
| stroke 24 | 41 % → 70 % | 121.7 px | 0.54 | 1.70 | 107 |
| stroke 25 | 48 % → 81 % | 138.9 px | 0.54 | 1.69 | 70 |
| stroke 26 | 48 % → 84 % | 134.9 px | 0.54 | 1.75 | 63 |
| stroke 27 | 35 % → 62 % | 102.4 px | 0.54 | 1.77 | 89 |
| stroke 28 | 39 % → 64 % | 111.3 px | 0.54 | 1.65 | 125 |
| stroke 29 | 47 % → 70 % | 137.6 px | 0.54 | 1.49 | 134 |
| stroke 30 | 52 % → 74 % | 145.3 px | 0.54 | 1.44 | 60 |
| stroke 31 | 52 % → 75 % | 158.9 px | 0.54 | 1.42 | 39 |
| stroke 32 | 51 % → 76 % | 167.6 px | 0.54 | 1.47 | 39 |
| stroke 33 | 46 % → 72 % | 160.4 px | 0.54 | 1.56 | 45 |
| stroke 34 | 41 % → 65 % | 132.1 px | 0.54 | 1.59 | 46 |
| stroke 35 | 35 % → 56 % | 110.0 px | 0.54 | 1.63 | 40 |
| stroke 36 | 35 % → 59 % | 119.5 px | 0.54 | 1.70 | 40 |
| stroke 37 | 36 % → 62 % | 129.3 px | 0.54 | 1.71 | 43 |
| stroke 38 | 35 % → 62 % | 116.2 px | 0.54 | 1.80 | 35 |
| stroke 39 | 30 % → 57 % | 96.3 px | 0.53 | 1.88 | 93 |
| stroke 40 | 30 % → 58 % | 93.6 px | 0.53 | 1.95 | 53 |
| stroke 41 | 36 % → 62 % | 110.9 px | 0.53 | 1.73 | 88 |
| stroke 42 | 44 % → 64 % | 121.4 px | 0.53 | 1.46 | 30 |
| stroke 43 | 55 % → 67 % | 146.4 px | 0.53 | 1.22 | 15 |
| stroke 44 | 66 % → 69 % | 179.8 px | 0.53 | 1.04 | 15 |
| stroke 45 | 6 % → 12 % | 34.5 px | 0.53 | 1.88 | 37 |
| stroke 46 | 11 % → 11 % | 58.6 px | 0.53 | 1.00 | 24 |
| stroke 47 | 7 % → 11 % | 31.6 px | 0.52 | 1.55 | 37 |
| stroke 48 | 8 % → 21 % | 29.4 px | 0.53 | 2.60 | 32 |
| stroke 49 | 20 % → 20 % | 44.1 px | 0.53 | 1.00 | 67 |
| stroke 50 | 14 % → 14 % | 87.8 px | 0.52 | 1.00 | 13 |
| stroke 51 | 18 % → 18 % | 90.9 px | 0.53 | 1.00 | 21 |
| stroke 52 | 20 % → 38 % | 75.4 px | 0.53 | 1.91 | 27 |
| stroke 53 | 35 % → 38 % | 73.8 px | 0.53 | 1.10 | 52 |
| stroke 54 | 33 % → 33 % | 155.5 px | 0.53 | 1.00 | 7 |

Numbers say: wet paint spreads well beyond the stroke.

## Refs v3 · #21 Gritty dog contours — own sheet
own sheet 800 × 1132 · Gouache 1.00 + water 15 % · 56 px · 72.8 s

![Refs v3 · #21 Gritty dog contours — own sheet](Refs-v3-21-Gritty-dog-contours-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 5 % → 0 % | 59.6 px | 0.00 | 0.00 | 43 |
| stroke 2 | 8 % → 0 % | 88.5 px | 0.32 | 0.05 | 44 |
| stroke 3 | 13 % → 2 % | 68.0 px | 0.37 | 0.15 | 289 |
| stroke 4 | 18 % → 2 % | 91.9 px | 0.38 | 0.13 | 328 |
| stroke 5 | 23 % → 0 % | 240.2 px | 0.00 | 0.00 | 50 |
| stroke 6 | 29 % → 5 % | 191.1 px | 0.38 | 0.16 | 205 |
| stroke 7 | 28 % → 0 % | 317.0 px | 0.00 | 0.00 | 60 |
| stroke 8 | 29 % → 7 % | 269.9 px | 0.38 | 0.24 | 80 |
| stroke 9 | 23 % → 6 % | 208.3 px | 0.38 | 0.26 | 68 |
| stroke 10 | 21 % → 4 % | 170.5 px | 0.39 | 0.21 | 132 |
| stroke 11 | 20 % → 3 % | 127.8 px | 0.39 | 0.13 | 207 |
| stroke 12 | 23 % → 2 % | 195.4 px | 0.40 | 0.07 | 86 |
| stroke 13 | 5 % → 0 % | 56.3 px | 0.00 | 0.00 | 52 |
| stroke 14 | 27 % → 0 % | 212.3 px | 0.00 | 0.00 | 114 |
| stroke 15 | 28 % → 1 % | 180.7 px | 0.40 | 0.03 | 145 |
| stroke 16 | 17 % → 0 % | 137.1 px | 0.00 | 0.00 | 118 |
| stroke 17 | 25 % → 0 % | 129.9 px | 0.00 | 0.00 | 369 |
| stroke 18 | 20 % → 0 % | 210.1 px | 0.00 | 0.00 | 53 |
| stroke 19 | 37 % → 0 % | 210.3 px | 0.36 | 0.00 | 186 |
| stroke 20 | 36 % → 2 % | 179.0 px | 0.40 | 0.04 | 373 |
| stroke 21 | 29 % → 0 % | 252.2 px | 0.00 | 0.00 | 77 |
| stroke 22 | 34 % → 2 % | 165.0 px | 0.39 | 0.07 | 509 |
| stroke 23 | 30 % → 6 % | 324.0 px | 0.40 | 0.19 | 66 |
| stroke 24 | 49 % → 4 % | 314.8 px | 0.40 | 0.09 | 176 |
| stroke 25 | 50 % → 0 % | 628.1 px | 0.32 | 0.00 | 50 |
| stroke 26 | 32 % → 0 % | 360.9 px | 0.00 | 0.00 | 50 |
| stroke 27 | 30 % → 6 % | 321.0 px | 0.39 | 0.21 | 58 |
| stroke 28 | 49 % → 6 % | 302.1 px | 0.39 | 0.12 | 134 |
| stroke 29 | 50 % → 1 % | 564.1 px | 0.40 | 0.02 | 45 |
| stroke 30 | 36 % → 1 % | 341.7 px | 0.39 | 0.02 | 84 |
| stroke 31 | 30 % → 9 % | 358.4 px | 0.38 | 0.32 | 39 |
| stroke 32 | 40 % → 6 % | 197.6 px | 0.39 | 0.16 | 306 |
| stroke 33 | 45 % → 10 % | 426.3 px | 0.40 | 0.22 | 92 |
| stroke 34 | 36 % → 14 % | 436.6 px | 0.39 | 0.38 | 49 |
| stroke 35 | 2 % → 0 % | 16.1 px | 0.00 | 0.00 | 59 |
| stroke 36 | 4 % → 0 % | 49.6 px | 0.00 | 0.00 | 12 |
| stroke 37 | 5 % → 0 % | 49.5 px | 0.00 | 0.00 | 34 |
| stroke 38 | 7 % → 0 % | 169.2 px | 0.00 | 0.00 | 6 |
| stroke 39 | 8 % → 0 % | 159.0 px | 0.00 | 0.00 | 6 |
| stroke 40 | 9 % → 0 % | 113.9 px | 0.00 | 0.00 | 20 |
| stroke 41 | 10 % → 0 % | 161.2 px | 0.00 | 0.00 | 20 |
| stroke 42 | 12 % → 0 % | 149.1 px | 0.00 | 0.00 | 19 |
| stroke 43 | 1 % → 0 % | 28.3 px | 0.00 | 0.00 | 3 |
| stroke 44 | 4 % → 0 % | 52.9 px | 0.00 | 0.00 | 9 |
| stroke 45 | 4 % → 0 % | 79.2 px | 0.36 | 0.03 | 10 |
| stroke 46 | 5 % → 1 % | 121.0 px | 0.38 | 0.12 | 12 |
| stroke 47 | 6 % → 1 % | 187.1 px | 0.39 | 0.25 | 20 |
| stroke 48 | 1 % → 0 % | 18.6 px | 0.00 | 0.00 | 6 |
| stroke 49 | 1 % → 0 % | 17.6 px | 0.00 | 0.00 | 4 |
| stroke 50 | 4 % → 0 % | 46.7 px | 0.00 | 0.00 | 19 |
| stroke 51 | 6 % → 0 % | 145.2 px | 0.00 | 0.00 | 5 |
| stroke 52 | 7 % → 0 % | 106.3 px | 0.00 | 0.00 | 12 |
| stroke 53 | 8 % → 0 % | 98.0 px | 0.00 | 0.00 | 16 |
| stroke 54 | 11 % → 0 % | 164.2 px | 0.00 | 0.00 | 6 |
| stroke 55 | 12 % → 0 % | 251.1 px | 0.00 | 0.00 | 10 |
| stroke 56 | 11 % → 1 % | 117.7 px | 0.37 | 0.09 | 31 |
| stroke 57 | 9 % → 0 % | 101.8 px | 0.00 | 0.00 | 25 |
| stroke 58 | 11 % → 2 % | 79.3 px | 0.37 | 0.23 | 41 |
| stroke 59 | 22 % → 0 % | 516.4 px | 0.00 | 0.00 | 6 |
| stroke 60 | 4 % → 0 % | 57.5 px | 0.00 | 0.00 | 12 |
| stroke 61 | 8 % → 0 % | 77.5 px | 0.00 | 0.00 | 26 |
| stroke 62 | 6 % → 0 % | 98.3 px | 0.00 | 0.00 | 16 |
| stroke 63 | 8 % → 0 % | 103.7 px | 0.00 | 0.00 | 14 |
| stroke 64 | 8 % → 0 % | 127.7 px | 0.00 | 0.00 | 10 |
| stroke 65 | 3 % → 0 % | 77.1 px | 0.00 | 0.00 | 11 |
| stroke 66 | 1 % → 5 % | 29.0 px | 0.39 | 4.07 | 9 |
| stroke 67 | 6 % → 0 % | 75.4 px | 0.00 | 0.00 | 16 |
| stroke 68 | 5 % → 0 % | 71.6 px | 0.00 | 0.00 | 18 |
| stroke 69 | 5 % → 0 % | 48.5 px | 0.00 | 0.00 | 29 |
| stroke 70 | 7 % → 0 % | 70.6 px | 0.37 | 0.05 | 31 |
| stroke 71 | 4 % → 0 % | 99.4 px | 0.00 | 0.00 | 4 |
| stroke 72 | 7 % → 4 % | 64.4 px | 0.40 | 0.51 | 50 |
| stroke 73 | 8 % → 7 % | 129.2 px | 0.39 | 0.91 | 11 |
| stroke 74 | 4 % → 0 % | 55.7 px | 0.00 | 0.00 | 34 |
| stroke 75 | 9 % → 5 % | 76.6 px | 0.40 | 0.57 | 31 |
| stroke 76 | 7 % → 6 % | 142.8 px | 0.40 | 0.86 | 6 |
| stroke 77 | 6 % → 3 % | 164.5 px | 0.40 | 0.56 | 2 |
| stroke 78 | 4 % → 4 % | 78.6 px | 0.40 | 1.00 | 3 |
| stroke 79 | 3 % → 7 % | 56.0 px | 0.37 | 2.33 | 5 |
| stroke 80 | 2 % → 0 % | 23.6 px | 0.00 | 0.00 | 24 |
| stroke 81 | 4 % → 0 % | 38.8 px | 0.00 | 0.00 | 19 |
| stroke 82 | 6 % → 0 % | 78.8 px | 0.00 | 0.00 | 34 |
| stroke 83 | 1 % → 0 % | 25.1 px | 0.29 | 0.45 | 5 |
| stroke 84 | 2 % → 0 % | 73.4 px | 0.00 | 0.00 | 3 |
| stroke 85 | 5 % → 0 % | 96.4 px | 0.00 | 0.00 | 12 |
| stroke 86 | 9 % → 0 % | 168.8 px | 0.00 | 0.00 | 9 |
| stroke 87 | 11 % → 0 % | 188.8 px | 0.00 | 0.00 | 19 |
| stroke 88 | 13 % → 0 % | 141.9 px | 0.00 | 0.00 | 20 |
| stroke 89 | 15 % → 0 % | 152.7 px | 0.00 | 0.00 | 38 |
| stroke 90 | 9 % → 0 % | 191.4 px | 0.00 | 0.00 | 12 |
| stroke 91 | 9 % → 0 % | 69.5 px | 0.00 | 0.00 | 71 |
| stroke 92 | 14 % → 0 % | 482.1 px | 0.00 | 0.00 | 5 |
| stroke 93 | 15 % → 0 % | 369.7 px | 0.00 | 0.00 | 7 |
| stroke 94 | 12 % → 0 % | 423.3 px | 0.00 | 0.00 | 8 |
| stroke 95 | 14 % → 0 % | 344.8 px | 0.00 | 0.00 | 4 |
| stroke 96 | 5 % → 5 % | 30.2 px | 0.38 | 1.20 | 64 |
| stroke 97 | 7 % → 4 % | 41.4 px | 0.38 | 0.56 | 123 |
| stroke 98 | 12 % → 5 % | 80.4 px | 0.38 | 0.44 | 65 |
| stroke 99 | 20 % → 9 % | 516.8 px | 0.38 | 0.41 | 15 |
| stroke 100 | 17 % → 0 % | 473.7 px | 0.00 | 0.00 | 15 |
| stroke 101 | 19 % → 0 % | 264.6 px | 0.00 | 0.00 | 15 |
| stroke 102 | 4 % → 0 % | 134.6 px | 0.00 | 0.00 | 13 |
| stroke 103 | 17 % → 0 % | 122.3 px | 0.00 | 0.00 | 48 |
| stroke 104 | 20 % → 0 % | 174.1 px | 0.00 | 0.00 | 36 |
| stroke 105 | 23 % → 0 % | 265.0 px | 0.00 | 0.00 | 18 |
| stroke 106 | 33 % → 0 % | 823.1 px | 0.00 | 0.00 | 10 |
| stroke 107 | 25 % → 0 % | 655.9 px | 0.00 | 0.00 | 24 |
| stroke 108 | 28 % → 0 % | 529.1 px | 0.00 | 0.00 | 9 |
| stroke 109 | 39 % → 0 % | 1232.7 px | 0.00 | 0.00 | 18 |
| stroke 110 | 28 % → 0 % | 307.6 px | 0.00 | 0.00 | 31 |
| stroke 111 | 31 % → 0 % | 284.9 px | 0.00 | 0.00 | 59 |
| stroke 112 | 23 % → 0 % | 770.9 px | 0.00 | 0.00 | 4 |
| stroke 113 | 24 % → 0 % | 965.4 px | 0.00 | 0.00 | 14 |
| stroke 114 | 11 % → 0 % | 346.7 px | 0.00 | 0.00 | 9 |
| stroke 115 | 13 % → 0 % | 237.8 px | 0.00 | 0.00 | 29 |
| stroke 116 | 15 % → 0 % | 132.1 px | 0.00 | 0.00 | 40 |
| stroke 117 | 15 % → 0 % | 199.6 px | 0.00 | 0.00 | 25 |
| stroke 118 | 4 % → 2 % | 41.7 px | 0.39 | 0.61 | 17 |
| stroke 119 | 5 % → 2 % | 56.4 px | 0.39 | 0.52 | 22 |
| stroke 120 | 6 % → 3 % | 67.1 px | 0.40 | 0.53 | 20 |
| stroke 121 | 3 % → 6 % | 21.1 px | 0.38 | 1.96 | 20 |
| stroke 122 | 4 % → 6 % | 84.6 px | 0.39 | 1.49 | 10 |
| stroke 123 | 3 % → 13 % | 32.0 px | 0.38 | 4.57 | 33 |
| stroke 124 | 5 % → 15 % | 64.7 px | 0.38 | 3.16 | 15 |
| stroke 125 | 7 % → 13 % | 56.2 px | 0.37 | 1.77 | 19 |
| stroke 126 | 6 % → 10 % | 134.1 px | 0.36 | 1.56 | 7 |
| stroke 127 | 7 % → 11 % | 77.0 px | 0.39 | 1.54 | 10 |
| stroke 128 | 3 % → 5 % | 35.4 px | 0.40 | 1.58 | 16 |

Numbers say: wet paint spreads well beyond the stroke.

## Refs v3 · #22 Wasilewski brush poster — own sheet
own sheet 800 × 1633 · Ink 0.98 · 64 px · 90.0 s

![Refs v3 · #22 Wasilewski brush poster — own sheet](Refs-v3-22-Wasilewski-brush-poster-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 2 % → 41 % | 90.3 px | 0.91 | 16.66 | 32 |
| stroke 2 | 4 % → 72 % | 94.9 px | 0.92 | 19.43 | 8 |
| stroke 3 | 10 % → 80 % | 41.6 px | 0.92 | 7.76 | 97 |
| stroke 4 | 2 % → 49 % | 92.2 px | 0.92 | 22.60 | 4 |
| stroke 5 | 4 % → 56 % | 61.1 px | 0.91 | 13.90 | 34 |
| stroke 6 | 3 % → 35 % | 84.7 px | 0.91 | 11.58 | 14 |
| stroke 7 | 2 % → 40 % | 67.6 px | 0.90 | 19.24 | 5 |
| stroke 8 | 6 % → 61 % | 226.9 px | 0.91 | 10.14 | 10 |
| stroke 9 | 6 % → 29 % | 208.7 px | 0.91 | 4.54 | 15 |
| stroke 10 | 6 % → 40 % | 165.4 px | 0.91 | 7.06 | 14 |
| stroke 11 | 9 % → 31 % | 125.0 px | 0.91 | 3.38 | 40 |
| stroke 12 | 7 % → 58 % | 166.0 px | 0.91 | 8.57 | 33 |
| stroke 13 | 8 % → 46 % | 306.5 px | 0.91 | 5.95 | 6 |
| stroke 14 | 10 % → 36 % | 307.8 px | 0.91 | 3.72 | 13 |
| stroke 15 | 3 % → 15 % | 88.1 px | 0.91 | 5.19 | 11 |
| stroke 16 | 6 % → 36 % | 285.3 px | 0.91 | 5.63 | 12 |
| stroke 17 | 14 % → 50 % | 126.7 px | 0.91 | 3.46 | 57 |
| stroke 18 | 3 % → 45 % | 80.4 px | 0.92 | 14.87 | 20 |
| stroke 19 | 1 % → 40 % | 59.9 px | 0.92 | 30.18 | 3 |
| stroke 20 | 9 % → 36 % | 109.4 px | 0.90 | 3.98 | 65 |
| stroke 21 | 16 % → 54 % | 321.8 px | 0.91 | 3.36 | 23 |
| stroke 22 | 4 % → 36 % | 140.3 px | 0.92 | 8.10 | 20 |
| stroke 23 | 17 % → 31 % | 95.0 px | 0.90 | 1.88 | 202 |
| stroke 24 | 19 % → 72 % | 741.9 px | 0.92 | 3.78 | 11 |
| stroke 25 | 6 % → 27 % | 201.5 px | 0.91 | 4.35 | 11 |
| stroke 26 | 4 % → 14 % | 143.7 px | 0.91 | 3.74 | 5 |
| stroke 27 | 2 % → 25 % | 69.0 px | 0.91 | 13.53 | 4 |
| stroke 28 | 9 % → 42 % | 233.7 px | 0.92 | 4.61 | 36 |
| stroke 29 | 12 % → 46 % | 442.1 px | 0.91 | 3.94 | 7 |
| stroke 30 | 6 % → 27 % | 71.7 px | 0.91 | 4.55 | 62 |
| stroke 31 | 7 % → 24 % | 178.4 px | 0.91 | 3.43 | 25 |
| stroke 32 | 13 % → 44 % | 236.8 px | 0.91 | 3.32 | 62 |
| stroke 33 | 28 % → 85 % | 438.8 px | 0.92 | 3.08 | 13 |
| stroke 34 | 9 % → 26 % | 160.5 px | 0.91 | 2.96 | 41 |
| stroke 35 | 10 % → 23 % | 223.9 px | 0.91 | 2.34 | 19 |
| stroke 36 | 7 % → 31 % | 111.3 px | 0.91 | 4.39 | 41 |
| stroke 37 | 10 % → 28 % | 112.9 px | 0.91 | 2.85 | 97 |
| stroke 38 | 16 % → 24 % | 106.2 px | 0.91 | 1.48 | 200 |
| stroke 39 | 18 % → 45 % | 193.5 px | 0.91 | 2.48 | 51 |
| stroke 40 | 12 % → 26 % | 476.9 px | 0.91 | 2.17 | 9 |
| stroke 41 | 23 % → 40 % | 252.6 px | 0.91 | 1.73 | 68 |
| stroke 42 | 13 % → 25 % | 226.6 px | 0.91 | 1.98 | 38 |
| stroke 43 | 20 % → 41 % | 286.5 px | 0.91 | 2.02 | 55 |
| stroke 44 | 17 % → 17 % | 179.7 px | 0.91 | 1.04 | 35 |
| stroke 45 | 22 % → 43 % | 239.1 px | 0.91 | 1.97 | 112 |
| stroke 46 | 30 % → 75 % | 771.2 px | 0.91 | 2.52 | 21 |
| stroke 47 | 25 % → 47 % | 1121.3 px | 0.91 | 1.89 | 5 |
| stroke 48 | 15 % → 26 % | 420.8 px | 0.91 | 1.69 | 22 |
| stroke 49 | 19 % → 49 % | 306.4 px | 0.91 | 2.65 | 30 |
| stroke 50 | 26 % → 54 % | 1079.2 px | 0.91 | 2.08 | 16 |
| stroke 51 | 41 % → 79 % | 898.0 px | 0.91 | 1.94 | 27 |
| stroke 52 | 12 % → 30 % | 158.9 px | 0.92 | 2.48 | 64 |
| stroke 53 | 39 % → 75 % | 698.3 px | 0.91 | 1.94 | 27 |
| stroke 54 | 42 % → 75 % | 673.0 px | 0.92 | 1.80 | 39 |
| stroke 55 | 31 % → 48 % | 270.9 px | 0.90 | 1.56 | 82 |
| stroke 56 | 26 % → 54 % | 577.6 px | 0.92 | 2.09 | 31 |
| stroke 57 | 33 % → 58 % | 554.6 px | 0.91 | 1.77 | 47 |
| stroke 58 | 20 % → 25 % | 327.8 px | 0.91 | 1.27 | 37 |
| stroke 59 | 13 % → 55 % | 158.1 px | 0.92 | 4.24 | 27 |
| stroke 60 | 19 % → 25 % | 285.5 px | 0.91 | 1.32 | 31 |
| stroke 61 | 29 % → 42 % | 383.9 px | 0.91 | 1.44 | 44 |
| stroke 62 | 19 % → 32 % | 255.2 px | 0.90 | 1.64 | 48 |
| stroke 63 | 47 % → 81 % | 724.4 px | 0.92 | 1.74 | 17 |
| stroke 64 | 32 % → 48 % | 196.4 px | 0.92 | 1.51 | 276 |
| stroke 65 | 20 % → 28 % | 665.5 px | 0.91 | 1.37 | 6 |
| stroke 66 | 28 % → 39 % | 481.1 px | 0.91 | 1.41 | 39 |
| stroke 67 | 19 % → 25 % | 621.0 px | 0.92 | 1.30 | 9 |
| stroke 68 | 24 % → 30 % | 469.7 px | 0.91 | 1.27 | 37 |
| stroke 69 | 6 % → 17 % | 240.9 px | 0.91 | 2.79 | 24 |
| stroke 70 | 37 % → 38 % | 435.3 px | 0.92 | 1.05 | 59 |
| stroke 71 | 25 % → 39 % | 1127.6 px | 0.92 | 1.53 | 20 |
| stroke 72 | 55 % → 75 % | 1063.7 px | 0.92 | 1.37 | 38 |
| stroke 73 | 46 % → 58 % | 539.0 px | 0.92 | 1.25 | 63 |
| stroke 74 | 61 % → 74 % | 1569.7 px | 0.92 | 1.21 | 27 |
| stroke 75 | 67 % → 84 % | 799.8 px | 0.92 | 1.24 | 16 |
| stroke 76 | 48 % → 61 % | 634.6 px | 0.91 | 1.27 | 77 |
| stroke 77 | 18 % → 25 % | 578.0 px | 0.91 | 1.39 | 10 |
| stroke 78 | 31 % → 47 % | 332.6 px | 0.91 | 1.52 | 67 |
| stroke 79 | 53 % → 68 % | 833.4 px | 0.92 | 1.27 | 19 |
| stroke 80 | 77 % → 88 % | 731.5 px | 0.92 | 1.14 | 40 |
| stroke 81 | 68 % → 75 % | 400.8 px | 0.92 | 1.11 | 95 |
| stroke 82 | 39 % → 59 % | 1104.2 px | 0.91 | 1.53 | 15 |
| stroke 83 | 38 % → 49 % | 666.8 px | 0.91 | 1.28 | 37 |
| stroke 84 | 32 % → 36 % | 462.8 px | 0.91 | 1.10 | 35 |
| stroke 85 | 6 % → 16 % | 146.6 px | 0.91 | 2.85 | 19 |
| stroke 86 | 40 % → 42 % | 334.3 px | 0.91 | 1.05 | 145 |
| stroke 87 | 50 % → 63 % | 1014.7 px | 0.91 | 1.26 | 92 |
| stroke 88 | 25 % → 29 % | 429.4 px | 0.91 | 1.15 | 40 |
| stroke 89 | 37 % → 38 % | 597.4 px | 0.91 | 1.04 | 43 |
| stroke 90 | 19 % → 24 % | 505.5 px | 0.90 | 1.27 | 12 |
| stroke 91 | 31 % → 37 % | 442.6 px | 0.91 | 1.20 | 27 |
| stroke 92 | 21 % → 25 % | 591.3 px | 0.91 | 1.19 | 14 |
| stroke 93 | 20 % → 23 % | 705.0 px | 0.91 | 1.15 | 17 |
| stroke 94 | 45 % → 49 % | 342.3 px | 0.91 | 1.08 | 99 |
| stroke 95 | 39 % → 40 % | 909.2 px | 0.91 | 1.01 | 37 |
| stroke 96 | 68 % → 72 % | 855.3 px | 0.91 | 1.06 | 65 |
| stroke 97 | 25 % → 28 % | 925.0 px | 0.91 | 1.12 | 12 |
| stroke 98 | 23 % → 24 % | 556.9 px | 0.91 | 1.06 | 32 |
| stroke 99 | 51 % → 52 % | 881.9 px | 0.91 | 1.02 | 28 |
| stroke 100 | 17 % → 20 % | 254.7 px | 0.91 | 1.20 | 52 |
| stroke 101 | 39 % → 41 % | 485.2 px | 0.92 | 1.06 | 42 |
| stroke 102 | 17 % → 18 % | 278.6 px | 0.91 | 1.06 | 45 |
| stroke 103 | 23 % → 23 % | 767.0 px | 0.90 | 1.02 | 15 |
| stroke 104 | 35 % → 35 % | 299.6 px | 0.91 | 1.01 | 122 |
| stroke 105 | 42 % → 42 % | 1875.9 px | 0.92 | 1.01 | 4 |
| stroke 106 | 49 % → 49 % | 1745.0 px | 0.91 | 1.01 | 24 |
| stroke 107 | 25 % → 25 % | 841.5 px | 0.91 | 1.01 | 8 |
| stroke 108 | 34 % → 34 % | 250.7 px | 0.91 | 1.02 | 137 |
| stroke 109 | 8 % → 28 % | 49.9 px | 0.92 | 3.51 | 74 |
| stroke 110 | 6 % → 30 % | 38.2 px | 0.90 | 4.84 | 36 |
| stroke 111 | 12 % → 36 % | 277.0 px | 0.92 | 3.04 | 8 |
| stroke 112 | 16 % → 28 % | 131.0 px | 0.91 | 1.80 | 57 |
| stroke 113 | 21 % → 22 % | 86.5 px | 0.91 | 1.08 | 316 |

Numbers say: wet paint spreads well beyond the stroke.

## Refs v3 · #23 Report dry white mask — own sheet
own sheet 800 × 804 · Ink 0.93 · Gouache 0.07 · 64 px · 65.4 s

![Refs v3 · #23 Report dry white mask — own sheet](Refs-v3-23-Report-dry-white-mask-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 11 % → 12 % | 63.2 px | 0.48 | 1.16 | 222 |
| stroke 2 | 14 % → 14 % | 82.0 px | 0.48 | 0.99 | 340 |
| stroke 3 | 18 % → 15 % | 115.8 px | 0.48 | 0.81 | 444 |
| stroke 4 | 22 % → 20 % | 174.1 px | 0.48 | 0.93 | 335 |
| stroke 5 | 39 % → 21 % | 339.4 px | 0.48 | 0.53 | 169 |
| stroke 6 | 23 % → 27 % | 172.5 px | 0.48 | 1.19 | 231 |
| stroke 7 | 33 % → 24 % | 482.5 px | 0.48 | 0.73 | 85 |
| stroke 8 | 24 % → 25 % | 180.6 px | 0.48 | 1.03 | 565 |
| stroke 9 | 27 % → 19 % | 202.6 px | 0.48 | 0.72 | 455 |
| stroke 10 | 42 % → 33 % | 428.1 px | 0.48 | 0.79 | 96 |
| stroke 11 | 21 % → 18 % | 236.8 px | 0.48 | 0.82 | 107 |
| stroke 12 | 30 % → 37 % | 291.5 px | 0.48 | 1.21 | 124 |
| stroke 13 | 21 % → 17 % | 178.5 px | 0.48 | 0.79 | 176 |
| stroke 14 | 28 % → 39 % | 259.5 px | 0.48 | 1.39 | 125 |
| stroke 15 | 24 % → 14 % | 182.6 px | 0.48 | 0.60 | 179 |
| stroke 16 | 32 % → 31 % | 265.6 px | 0.48 | 0.97 | 233 |
| stroke 17 | 30 % → 12 % | 200.5 px | 0.48 | 0.41 | 187 |
| stroke 18 | 29 % → 30 % | 344.6 px | 0.48 | 1.03 | 79 |
| stroke 19 | 37 % → 33 % | 538.3 px | 0.48 | 0.89 | 58 |
| stroke 20 | 42 % → 19 % | 254.4 px | 0.48 | 0.45 | 391 |
| stroke 21 | 41 % → 21 % | 251.1 px | 0.48 | 0.52 | 318 |
| stroke 22 | 37 % → 20 % | 232.0 px | 0.48 | 0.54 | 247 |
| stroke 23 | 41 % → 9 % | 381.4 px | 0.48 | 0.23 | 119 |
| stroke 24 | 72 % → 33 % | 1062.0 px | 0.48 | 0.46 | 65 |
| stroke 25 | 50 % → 36 % | 569.8 px | 0.48 | 0.72 | 66 |
| stroke 26 | 64 % → 20 % | 446.0 px | 0.48 | 0.32 | 222 |
| stroke 27 | 1 % → 23 % | 26.1 px | 0.48 | 15.85 | 29 |
| stroke 28 | 3 % → 23 % | 34.5 px | 0.48 | 8.16 | 48 |
| stroke 29 | 5 % → 22 % | 130.1 px | 0.48 | 4.89 | 15 |
| stroke 30 | 5 % → 25 % | 38.4 px | 0.48 | 5.27 | 106 |
| stroke 31 | 9 % → 22 % | 296.1 px | 0.48 | 2.56 | 15 |
| stroke 32 | 7 % → 27 % | 61.1 px | 0.48 | 3.56 | 108 |
| stroke 33 | 11 % → 23 % | 342.8 px | 0.48 | 2.09 | 18 |
| stroke 34 | 11 % → 36 % | 146.1 px | 0.48 | 3.35 | 34 |
| stroke 35 | 12 % → 23 % | 385.8 px | 0.48 | 1.89 | 5 |
| stroke 36 | 13 % → 35 % | 209.8 px | 0.48 | 2.73 | 29 |
| stroke 37 | 13 % → 24 % | 332.3 px | 0.48 | 1.83 | 9 |
| stroke 38 | 16 % → 34 % | 226.8 px | 0.48 | 2.16 | 33 |
| stroke 39 | 16 % → 26 % | 510.6 px | 0.48 | 1.66 | 7 |
| stroke 40 | 18 % → 31 % | 206.4 px | 0.48 | 1.70 | 59 |
| stroke 41 | 19 % → 27 % | 188.6 px | 0.48 | 1.47 | 41 |
| stroke 42 | 1 % → 22 % | 25.5 px | 0.48 | 17.23 | 12 |
| stroke 43 | 18 % → 39 % | 579.7 px | 0.48 | 2.13 | 9 |
| stroke 44 | 4 % → 24 % | 38.0 px | 0.48 | 6.32 | 38 |
| stroke 45 | 16 % → 27 % | 116.7 px | 0.48 | 1.69 | 130 |
| stroke 46 | 9 % → 24 % | 224.7 px | 0.48 | 2.67 | 7 |
| stroke 47 | 25 % → 37 % | 792.3 px | 0.48 | 1.48 | 7 |
| stroke 48 | 16 % → 31 % | 250.2 px | 0.48 | 1.90 | 26 |
| stroke 49 | 12 % → 25 % | 266.9 px | 0.48 | 2.10 | 10 |
| stroke 50 | 13 % → 25 % | 506.2 px | 0.48 | 1.99 | 7 |
| stroke 51 | 27 % → 36 % | 880.1 px | 0.48 | 1.36 | 6 |
| stroke 52 | 13 % → 24 % | 179.8 px | 0.48 | 1.80 | 15 |
| stroke 53 | 26 % → 34 % | 644.2 px | 0.48 | 1.32 | 22 |
| stroke 54 | 15 % → 25 % | 366.1 px | 0.48 | 1.68 | 6 |
| stroke 55 | 25 % → 33 % | 522.2 px | 0.48 | 1.33 | 21 |
| stroke 56 | 18 % → 25 % | 276.6 px | 0.48 | 1.43 | 24 |
| stroke 57 | 27 % → 32 % | 423.8 px | 0.48 | 1.19 | 23 |
| stroke 58 | 21 % → 26 % | 442.2 px | 0.48 | 1.20 | 24 |
| stroke 59 | 24 % → 26 % | 293.1 px | 0.48 | 1.09 | 35 |
| stroke 60 | 2 % → 20 % | 24.2 px | 0.49 | 9.26 | 29 |
| stroke 61 | 5 % → 14 % | 28.4 px | 0.49 | 2.93 | 52 |
| stroke 62 | 7 % → 12 % | 40.0 px | 0.49 | 1.72 | 85 |
| stroke 63 | 11 % → 16 % | 272.7 px | 0.49 | 1.41 | 6 |
| stroke 64 | 17 % → 21 % | 159.7 px | 0.49 | 1.27 | 23 |
| stroke 65 | 14 % → 17 % | 365.3 px | 0.49 | 1.20 | 14 |
| stroke 66 | 16 % → 18 % | 388.2 px | 0.48 | 1.11 | 18 |
| stroke 67 | 4 % → 18 % | 25.3 px | 0.48 | 4.21 | 113 |
| stroke 68 | 6 % → 18 % | 127.2 px | 0.48 | 2.83 | 16 |
| stroke 69 | 8 % → 20 % | 58.5 px | 0.48 | 2.43 | 101 |
| stroke 70 | 8 % → 17 % | 218.5 px | 0.48 | 2.25 | 10 |
| stroke 71 | 9 % → 18 % | 94.8 px | 0.48 | 1.96 | 35 |
| stroke 72 | 10 % → 18 % | 446.0 px | 0.48 | 1.86 | 14 |
| stroke 73 | 11 % → 18 % | 143.0 px | 0.48 | 1.71 | 40 |
| stroke 74 | 12 % → 19 % | 368.5 px | 0.48 | 1.64 | 9 |
| stroke 75 | 13 % → 20 % | 214.4 px | 0.48 | 1.51 | 22 |
| stroke 76 | 15 % → 22 % | 263.7 px | 0.48 | 1.43 | 14 |
| stroke 77 | 17 % → 23 % | 332.9 px | 0.48 | 1.38 | 32 |
| stroke 78 | 22 % → 24 % | 148.3 px | 0.48 | 1.08 | 100 |
| stroke 79 | 2 % → 18 % | 22.9 px | 0.48 | 10.40 | 25 |
| stroke 80 | 4 % → 26 % | 114.6 px | 0.49 | 6.68 | 6 |
| stroke 81 | 6 % → 15 % | 30.9 px | 0.48 | 2.69 | 75 |
| stroke 82 | 8 % → 17 % | 306.9 px | 0.48 | 2.21 | 4 |
| stroke 83 | 12 % → 19 % | 58.3 px | 0.48 | 1.62 | 77 |
| stroke 84 | 10 % → 16 % | 363.7 px | 0.48 | 1.58 | 4 |
| stroke 85 | 23 % → 28 % | 203.1 px | 0.49 | 1.21 | 10 |
| stroke 86 | 10 % → 15 % | 415.4 px | 0.48 | 1.53 | 19 |
| stroke 87 | 8 % → 12 % | 348.4 px | 0.48 | 1.49 | 3 |
| stroke 88 | 7 % → 10 % | 238.9 px | 0.48 | 1.40 | 13 |
| stroke 89 | 8 % → 10 % | 298.7 px | 0.47 | 1.30 | 3 |
| stroke 90 | 9 % → 10 % | 310.0 px | 0.47 | 1.18 | 5 |

Numbers say: wet paint spreads well beyond the stroke.

## Refs v3 · #24 Picasso flat oil — own sheet
own sheet 800 × 1155 · Gouache 1.00 + turpentine 20 % · 53 px · 133.9 s

![Refs v3 · #24 Picasso flat oil — own sheet](Refs-v3-24-Picasso-flat-oil-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 5 % → 0 % | 61.4 px | 0.01 | 0.07 | 61 |
| stroke 2 | 12 % → 3 % | 80.5 px | 0.01 | 0.21 | 110 |
| stroke 3 | 16 % → 2 % | 86.8 px | 0.01 | 0.12 | 271 |
| stroke 4 | 25 % → 3 % | 174.6 px | 0.01 | 0.10 | 154 |
| stroke 5 | 25 % → 2 % | 139.4 px | 0.01 | 0.08 | 189 |
| stroke 6 | 38 % → 3 % | 489.7 px | 0.01 | 0.08 | 63 |
| stroke 7 | 27 % → 0 % | 178.4 px | 0.00 | 0.00 | 128 |
| stroke 8 | 30 % → 0 % | 233.9 px | 0.00 | 0.00 | 102 |
| stroke 9 | 28 % → 1 % | 194.8 px | 0.01 | 0.02 | 90 |
| stroke 10 | 41 % → 3 % | 202.7 px | 0.01 | 0.08 | 205 |
| stroke 11 | 8 % → 3 % | 60.1 px | 0.05 | 0.38 | 37 |
| stroke 12 | 13 % → 2 % | 62.3 px | 0.05 | 0.12 | 212 |
| stroke 13 | 17 % → 1 % | 81.3 px | 0.05 | 0.08 | 189 |
| stroke 14 | 27 % → 0 % | 118.3 px | 0.08 | 0.01 | 243 |
| stroke 15 | 37 % → 0 % | 140.0 px | 0.00 | 0.00 | 207 |
| stroke 16 | 49 % → 0 % | 162.7 px | 0.00 | 0.00 | 223 |
| stroke 17 | 71 % → 0 % | 245.1 px | 0.00 | 0.00 | 138 |
| stroke 18 | 93 % → 0 % | 349.2 px | 0.00 | 0.00 | 89 |
| stroke 19 | 7 % → 0 % | 59.4 px | 0.00 | 0.00 | 48 |
| stroke 20 | 19 % → 0 % | 63.2 px | 0.00 | 0.00 | 158 |
| stroke 21 | 7 % → 3 % | 40.6 px | 0.01 | 0.50 | 81 |
| stroke 22 | 11 % → 2 % | 45.6 px | 0.01 | 0.13 | 504 |
| stroke 23 | 18 % → 2 % | 75.4 px | 0.01 | 0.10 | 270 |
| stroke 24 | 22 % → 2 % | 92.6 px | 0.01 | 0.08 | 359 |
| stroke 25 | 25 % → 2 % | 134.4 px | 0.01 | 0.07 | 159 |
| stroke 26 | 25 % → 0 % | 271.1 px | 0.00 | 0.00 | 42 |
| stroke 27 | 27 % → 0 % | 211.7 px | 0.00 | 0.00 | 79 |
| stroke 28 | 5 % → 0 % | 44.2 px | 0.00 | 0.00 | 55 |
| stroke 29 | 43 % → 4 % | 231.9 px | 0.01 | 0.09 | 101 |
| stroke 30 | 40 % → 5 % | 383.0 px | 0.01 | 0.13 | 97 |
| stroke 31 | 26 % → 6 % | 383.8 px | 0.01 | 0.22 | 15 |
| stroke 32 | 3 % → 2 % | 44.3 px | 0.05 | 0.70 | 28 |
| stroke 33 | 6 % → 2 % | 58.4 px | 0.05 | 0.39 | 58 |
| stroke 34 | 2 % → 0 % | 23.1 px | 0.00 | 0.00 | 17 |
| stroke 35 | 4 % → 3 % | 24.5 px | 0.02 | 0.60 | 92 |
| stroke 36 | 5 % → 2 % | 26.8 px | 0.05 | 0.42 | 52 |
| stroke 37 | 11 % → 3 % | 79.1 px | 0.05 | 0.27 | 13 |
| stroke 38 | 10 % → 0 % | 126.0 px | 0.00 | 0.00 | 16 |
| stroke 39 | 2 % → 0 % | 23.0 px | 0.00 | 0.00 | 19 |
| stroke 40 | 3 % → 0 % | 26.6 px | 0.00 | 0.00 | 49 |
| stroke 41 | 5 % → 1 % | 29.7 px | 0.01 | 0.12 | 78 |
| stroke 42 | 8 % → 0 % | 147.4 px | 0.00 | 0.00 | 32 |
| stroke 43 | 9 % → 1 % | 78.3 px | 0.02 | 0.10 | 44 |
| stroke 44 | 10 % → 0 % | 183.8 px | 0.00 | 0.00 | 34 |
| stroke 45 | 10 % → 2 % | 79.5 px | 0.01 | 0.17 | 41 |
| stroke 46 | 9 % → 2 % | 114.3 px | 0.01 | 0.26 | 20 |
| stroke 47 | 8 % → 3 % | 97.6 px | 0.02 | 0.41 | 54 |
| stroke 48 | 8 % → 4 % | 68.8 px | 0.02 | 0.44 | 33 |
| stroke 49 | 9 % → 5 % | 88.1 px | 0.01 | 0.54 | 49 |
| stroke 50 | 14 % → 0 % | 180.6 px | 0.00 | 0.00 | 22 |
| stroke 51 | 14 % → 0 % | 172.5 px | 0.00 | 0.00 | 30 |
| stroke 52 | 13 % → 0 % | 152.5 px | 0.00 | 0.00 | 50 |
| stroke 53 | 17 % → 4 % | 121.0 px | 0.01 | 0.24 | 40 |
| stroke 54 | 21 % → 4 % | 130.0 px | 0.01 | 0.18 | 93 |
| stroke 55 | 23 % → 3 % | 335.6 px | 0.01 | 0.12 | 16 |
| stroke 56 | 15 % → 3 % | 398.8 px | 0.01 | 0.19 | 7 |
| stroke 57 | 1 % → 2 % | 22.3 px | 0.01 | 1.95 | 4 |
| stroke 58 | 2 % → 0 % | 50.3 px | 0.00 | 0.18 | 5 |
| stroke 59 | 3 % → 0 % | 26.8 px | 0.01 | 0.09 | 43 |
| stroke 60 | 5 % → 0 % | 48.3 px | 0.00 | 0.00 | 30 |
| stroke 61 | 6 % → 0 % | 90.6 px | 0.00 | 0.00 | 20 |
| stroke 62 | 8 % → 0 % | 159.0 px | 0.00 | 0.00 | 8 |
| stroke 63 | 1 % → 0 % | 22.3 px | 0.02 | 0.01 | 12 |
| stroke 64 | 10 % → 0 % | 91.9 px | 0.00 | 0.00 | 43 |
| stroke 65 | 10 % → 0 % | 69.0 px | 0.00 | 0.00 | 55 |
| stroke 66 | 19 % → 5 % | 235.9 px | 0.01 | 0.25 | 20 |
| stroke 67 | 22 % → 5 % | 380.2 px | 0.01 | 0.24 | 8 |
| stroke 68 | 20 % → 6 % | 489.5 px | 0.01 | 0.30 | 4 |
| stroke 69 | 26 % → 4 % | 189.0 px | 0.01 | 0.17 | 39 |
| stroke 70 | 29 % → 5 % | 302.5 px | 0.01 | 0.17 | 32 |
| stroke 71 | 9 % → 0 % | 165.3 px | 0.00 | 0.00 | 9 |
| stroke 72 | 7 % → 0 % | 54.1 px | 0.00 | 0.00 | 49 |
| stroke 73 | 10 % → 0 % | 55.4 px | 0.02 | 0.02 | 92 |
| stroke 74 | 15 % → 1 % | 73.3 px | 0.01 | 0.08 | 125 |
| stroke 75 | 21 % → 0 % | 108.9 px | 0.02 | 0.02 | 100 |
| stroke 76 | 25 % → 0 % | 531.5 px | 0.00 | 0.00 | 12 |
| stroke 77 | 8 % → 0 % | 54.3 px | 0.00 | 0.00 | 44 |
| stroke 78 | 12 % → 0 % | 68.6 px | 0.00 | 0.00 | 74 |
| stroke 79 | 12 % → 0 % | 74.6 px | 0.00 | 0.00 | 52 |
| stroke 80 | 13 % → 0 % | 214.7 px | 0.00 | 0.00 | 15 |
| stroke 81 | 16 % → 0 % | 235.4 px | 0.04 | 0.01 | 15 |
| stroke 82 | 14 % → 0 % | 249.3 px | 0.00 | 0.00 | 7 |
| stroke 83 | 3 % → 0 % | 23.1 px | 0.00 | 0.00 | 41 |
| stroke 84 | 2 % → 5 % | 24.0 px | 0.02 | 2.78 | 21 |
| stroke 85 | 5 % → 3 % | 32.2 px | 0.02 | 0.60 | 55 |
| stroke 86 | 4 % → 0 % | 95.5 px | 0.00 | 0.00 | 4 |
| stroke 87 | 6 % → 3 % | 38.4 px | 0.01 | 0.54 | 54 |
| stroke 88 | 12 % → 0 % | 46.7 px | 0.01 | 0.04 | 237 |
| stroke 89 | 19 % → 2 % | 69.3 px | 0.01 | 0.09 | 239 |
| stroke 90 | 25 % → 2 % | 117.1 px | 0.01 | 0.09 | 364 |
| stroke 91 | 24 % → 0 % | 332.7 px | 0.00 | 0.00 | 58 |
| stroke 92 | 18 % → 1 % | 90.0 px | 0.05 | 0.08 | 489 |
| stroke 93 | 25 % → 1 % | 100.9 px | 0.05 | 0.05 | 1542 |
| stroke 94 | 31 % → 1 % | 120.4 px | 0.05 | 0.04 | 784 |
| stroke 95 | 31 % → 2 % | 185.4 px | 0.05 | 0.07 | 244 |
| stroke 96 | 8 % → 0 % | 40.6 px | 0.04 | 0.04 | 1432 |
| stroke 97 | 20 % → 4 % | 74.5 px | 0.03 | 0.20 | 783 |
| stroke 98 | 30 % → 4 % | 118.7 px | 0.03 | 0.13 | 1672 |
| stroke 99 | 48 % → 3 % | 249.4 px | 0.04 | 0.05 | 482 |
| stroke 100 | 28 % → 0 % | 259.8 px | 0.04 | 0.01 | 239 |
| stroke 101 | 34 % → 0 % | 706.6 px | 0.00 | 0.00 | 138 |
| stroke 102 | 3 % → 0 % | 24.0 px | 0.00 | 0.00 | 57 |
| stroke 103 | 5 % → 0 % | 34.1 px | 0.00 | 0.00 | 105 |
| stroke 104 | 7 % → 0 % | 53.5 px | 0.00 | 0.00 | 69 |
| stroke 105 | 11 % → 0 % | 121.1 px | 0.00 | 0.00 | 46 |
| stroke 106 | 13 % → 0 % | 89.6 px | 0.00 | 0.00 | 26 |
| stroke 107 | 15 % → 0 % | 90.7 px | 0.00 | 0.00 | 93 |
| stroke 108 | 14 % → 0 % | 120.0 px | 0.00 | 0.00 | 30 |
| stroke 109 | 15 % → 0 % | 153.6 px | 0.00 | 0.00 | 16 |
| stroke 110 | 3 % → 0 % | 29.0 px | 0.00 | 0.00 | 57 |
| stroke 111 | 10 % → 0 % | 63.7 px | 0.00 | 0.00 | 68 |
| stroke 112 | 16 % → 0 % | 66.2 px | 0.00 | 0.00 | 169 |
| stroke 113 | 20 % → 0 % | 87.0 px | 0.00 | 0.00 | 159 |
| stroke 114 | 21 % → 0 % | 102.1 px | 0.00 | 0.00 | 65 |
| stroke 115 | 25 % → 0 % | 147.4 px | 0.00 | 0.00 | 46 |
| stroke 116 | 1 % → 3 % | 27.2 px | 0.01 | 3.15 | 60 |
| stroke 117 | 2 % → 4 % | 40.8 px | 0.01 | 1.92 | 10 |
| stroke 118 | 3 % → 4 % | 43.3 px | 0.01 | 1.10 | 43 |
| stroke 119 | 5 % → 3 % | 113.7 px | 0.01 | 0.54 | 44 |
| stroke 120 | 6 % → 4 % | 74.2 px | 0.01 | 0.61 | 104 |
| stroke 121 | 7 % → 4 % | 91.8 px | 0.01 | 0.51 | 86 |
| stroke 122 | 9 % → 4 % | 159.4 px | 0.01 | 0.44 | 44 |
| stroke 123 | 8 % → 2 % | 59.5 px | 0.01 | 0.30 | 190 |
| stroke 124 | 10 % → 2 % | 69.5 px | 0.01 | 0.23 | 235 |
| stroke 125 | 17 % → 4 % | 223.2 px | 0.01 | 0.21 | 30 |
| stroke 126 | 15 % → 4 % | 278.6 px | 0.01 | 0.25 | 7 |
| stroke 127 | 15 % → 4 % | 220.1 px | 0.01 | 0.24 | 25 |
| stroke 128 | 11 % → 4 % | 287.3 px | 0.01 | 0.36 | 68 |
| stroke 129 | 1 % → 0 % | 31.7 px | 0.00 | 0.00 | 5 |
| stroke 130 | 6 % → 0 % | 65.3 px | 0.01 | 0.02 | 39 |
| stroke 131 | 5 % → 0 % | 87.3 px | 0.00 | 0.00 | 38 |
| stroke 132 | 6 % → 0 % | 75.3 px | 0.00 | 0.00 | 19 |
| stroke 133 | 8 % → 0 % | 213.3 px | 0.00 | 0.00 | 12 |
| stroke 134 | 8 % → 0 % | 121.7 px | 0.00 | 0.00 | 28 |
| stroke 135 | 10 % → 0 % | 273.9 px | 0.00 | 0.00 | 5 |
| stroke 136 | 10 % → 1 % | 140.3 px | 0.01 | 0.11 | 36 |
| stroke 137 | 12 % → 2 % | 170.6 px | 0.01 | 0.18 | 93 |
| stroke 138 | 13 % → 3 % | 348.4 px | 0.01 | 0.19 | 34 |
| stroke 139 | 14 % → 3 % | 269.1 px | 0.01 | 0.23 | 78 |
| stroke 140 | 13 % → 4 % | 311.5 px | 0.01 | 0.31 | 25 |
| stroke 141 | 10 % → 5 % | 263.7 px | 0.01 | 0.50 | 27 |
| stroke 142 | 6 % → 0 % | 24.0 px | 0.00 | 0.00 | 134 |
| stroke 143 | 15 % → 0 % | 63.0 px | 0.00 | 0.00 | 30 |
| stroke 144 | 2 % → 4 % | 29.4 px | 0.01 | 2.13 | 16 |
| stroke 145 | 2 % → 3 % | 26.7 px | 0.05 | 1.22 | 38 |
| stroke 146 | 2 % → 0 % | 25.1 px | 0.00 | 0.00 | 46 |
| stroke 147 | 5 % → 3 % | 55.5 px | 0.05 | 0.68 | 13 |
| stroke 148 | 10 % → 0 % | 63.9 px | 0.00 | 0.00 | 105 |
| stroke 149 | 15 % → 0 % | 114.0 px | 0.00 | 0.00 | 88 |
| stroke 150 | 18 % → 0 % | 168.8 px | 0.00 | 0.00 | 73 |
| stroke 151 | 20 % → 0 % | 208.9 px | 0.00 | 0.00 | 118 |
| stroke 152 | 21 % → 0 % | 208.5 px | 0.00 | 0.00 | 89 |
| stroke 153 | 14 % → 0 % | 58.6 px | 0.00 | 0.00 | 296 |
| stroke 154 | 20 % → 0 % | 246.4 px | 0.00 | 0.00 | 41 |
| stroke 155 | 24 % → 0 % | 93.6 px | 0.00 | 0.00 | 531 |
| stroke 156 | 30 % → 0 % | 175.5 px | 0.00 | 0.00 | 272 |
| stroke 157 | 42 % → 0 % | 240.3 px | 0.00 | 0.00 | 156 |
| stroke 158 | 22 % → 0 % | 124.0 px | 0.00 | 0.00 | 188 |
| stroke 159 | 22 % → 0 % | 99.0 px | 0.00 | 0.00 | 272 |
| stroke 160 | 27 % → 0 % | 145.6 px | 0.00 | 0.00 | 341 |
| stroke 161 | 33 % → 0 % | 286.2 px | 0.00 | 0.00 | 60 |
| stroke 162 | 10 % → 0 % | 56.3 px | 0.00 | 0.00 | 171 |
| stroke 163 | 16 % → 0 % | 78.9 px | 0.00 | 0.00 | 162 |
| stroke 164 | 24 % → 0 % | 109.2 px | 0.02 | 0.02 | 643 |
| stroke 165 | 31 % → 0 % | 139.7 px | 0.00 | 0.00 | 684 |
| stroke 166 | 37 % → 0 % | 171.6 px | 0.00 | 0.00 | 680 |
| stroke 167 | 35 % → 0 % | 167.4 px | 0.00 | 0.00 | 685 |
| stroke 168 | 34 % → 0 % | 156.0 px | 0.00 | 0.00 | 623 |
| stroke 169 | 34 % → 0 % | 158.3 px | 0.00 | 0.00 | 379 |
| stroke 170 | 35 % → 0 % | 161.9 px | 0.00 | 0.00 | 490 |
| stroke 171 | 40 % → 0 % | 156.5 px | 0.00 | 0.00 | 1080 |
| stroke 172 | 44 % → 0 % | 188.5 px | 0.00 | 0.00 | 408 |
| stroke 173 | 47 % → 0 % | 283.4 px | 0.00 | 0.00 | 437 |
| stroke 174 | 44 % → 0 % | 402.8 px | 0.00 | 0.00 | 112 |
| stroke 175 | 6 % → 2 % | 62.0 px | 0.01 | 0.30 | 63 |
| stroke 176 | 12 % → 0 % | 59.9 px | 0.00 | 0.00 | 312 |
| stroke 177 | 22 % → 1 % | 83.0 px | 0.01 | 0.04 | 302 |
| stroke 178 | 35 % → 0 % | 114.7 px | 0.00 | 0.00 | 336 |
| stroke 179 | 51 % → 0 % | 144.1 px | 0.00 | 0.00 | 728 |
| stroke 180 | 72 % → 0 % | 185.3 px | 0.00 | 0.00 | 456 |
| stroke 181 | 2 % → 0 % | 19.6 px | 0.00 | 0.00 | 67 |
| stroke 182 | 4 % → 3 % | 61.2 px | 0.01 | 0.57 | 104 |
| stroke 183 | 3 % → 0 % | 34.7 px | 0.00 | 0.00 | 23 |
| stroke 184 | 4 % → 0 % | 66.5 px | 0.00 | 0.00 | 34 |
| stroke 185 | 10 % → 0 % | 59.2 px | 0.00 | 0.00 | 19 |
| stroke 186 | 8 % → 0 % | 72.8 px | 0.00 | 0.00 | 66 |
| stroke 187 | 12 % → 0 % | 53.8 px | 0.00 | 0.00 | 66 |
| stroke 188 | 17 % → 0 % | 90.0 px | 0.00 | 0.00 | 45 |
| stroke 189 | 27 % → 0 % | 267.8 px | 0.00 | 0.00 | 12 |
| stroke 190 | 21 % → 0 % | 248.9 px | 0.00 | 0.00 | 19 |
| stroke 191 | 23 % → 0 % | 373.1 px | 0.00 | 0.00 | 7 |
| stroke 192 | 24 % → 0 % | 277.5 px | 0.00 | 0.00 | 19 |
| stroke 193 | 26 % → 0 % | 553.3 px | 0.00 | 0.00 | 9 |
| stroke 194 | 27 % → 0 % | 236.0 px | 0.00 | 0.00 | 24 |
| stroke 195 | 31 % → 0 % | 215.9 px | 0.00 | 0.00 | 54 |
| stroke 196 | 3 % → 2 % | 30.4 px | 0.01 | 0.51 | 66 |
| stroke 197 | 2 % → 2 % | 48.8 px | 0.01 | 1.25 | 15 |
| stroke 198 | 6 % → 0 % | 120.0 px | 0.00 | 0.00 | 17 |
| stroke 199 | 8 % → 0 % | 82.7 px | 0.00 | 0.00 | 19 |
| stroke 200 | 12 % → 0 % | 220.8 px | 0.02 | 0.01 | 14 |
| stroke 201 | 7 % → 0 % | 143.4 px | 0.01 | 0.07 | 7 |
| stroke 202 | 12 % → 0 % | 65.3 px | 0.01 | 0.00 | 69 |
| stroke 203 | 15 % → 0 % | 85.9 px | 0.00 | 0.00 | 70 |
| stroke 204 | 19 % → 0 % | 110.6 px | 0.00 | 0.00 | 64 |
| stroke 205 | 21 % → 0 % | 126.8 px | 0.00 | 0.00 | 67 |
| stroke 206 | 22 % → 0 % | 145.0 px | 0.00 | 0.00 | 48 |
| stroke 207 | 25 % → 0 % | 162.3 px | 0.00 | 0.00 | 134 |
| stroke 208 | 29 % → 0 % | 221.5 px | 0.00 | 0.00 | 61 |
| stroke 209 | 30 % → 0 % | 271.6 px | 0.00 | 0.00 | 20 |
| stroke 210 | 31 % → 0 % | 600.4 px | 0.00 | 0.00 | 16 |
| stroke 211 | 5 % → 0 % | 29.3 px | 0.00 | 0.00 | 78 |
| stroke 212 | 8 % → 0 % | 48.4 px | 0.00 | 0.00 | 63 |
| stroke 213 | 11 % → 0 % | 55.5 px | 0.00 | 0.00 | 80 |
| stroke 214 | 10 % → 0 % | 180.8 px | 0.00 | 0.00 | 16 |
| stroke 215 | 16 % → 0 % | 96.0 px | 0.00 | 0.00 | 71 |
| stroke 216 | 13 % → 0 % | 267.8 px | 0.00 | 0.00 | 16 |
| stroke 217 | 9 % → 0 % | 214.2 px | 0.00 | 0.00 | 5 |
| stroke 218 | 19 % → 0 % | 107.9 px | 0.02 | 0.01 | 77 |
| stroke 219 | 4 % → 5 % | 98.4 px | 0.01 | 1.45 | 6 |
| stroke 220 | 5 % → 4 % | 94.0 px | 0.01 | 0.88 | 11 |
| stroke 221 | 7 % → 2 % | 99.6 px | 0.01 | 0.34 | 19 |
| stroke 222 | 8 % → 2 % | 81.8 px | 0.01 | 0.21 | 28 |
| stroke 223 | 8 % → 1 % | 92.5 px | 0.01 | 0.17 | 29 |
| stroke 224 | 11 % → 0 % | 193.1 px | 0.01 | 0.03 | 16 |
| stroke 225 | 4 % → 0 % | 30.8 px | 0.00 | 0.00 | 48 |
| stroke 226 | 8 % → 0 % | 119.7 px | 0.00 | 0.00 | 20 |
| stroke 227 | 10 % → 0 % | 214.2 px | 0.00 | 0.00 | 5 |
| stroke 228 | 12 % → 0 % | 127.7 px | 0.00 | 0.00 | 21 |
| stroke 229 | 13 % → 0 % | 234.2 px | 0.00 | 0.00 | 126 |
| stroke 230 | 13 % → 0 % | 75.8 px | 0.00 | 0.00 | 105 |
| stroke 231 | 14 % → 0 % | 332.1 px | 0.00 | 0.00 | 22 |
| stroke 232 | 20 % → 0 % | 499.6 px | 0.00 | 0.00 | 20 |
| stroke 233 | 24 % → 0 % | 494.6 px | 0.00 | 0.00 | 12 |
| stroke 234 | 2 % → 2 % | 32.9 px | 0.05 | 1.06 | 11 |
| stroke 235 | 6 % → 2 % | 33.8 px | 0.05 | 0.29 | 73 |
| stroke 236 | 10 % → 0 % | 74.1 px | 0.05 | 0.01 | 44 |
| stroke 237 | 11 % → 0 % | 111.2 px | 0.00 | 0.00 | 48 |
| stroke 238 | 11 % → 0 % | 156.8 px | 0.00 | 0.00 | 22 |
| stroke 239 | 23 % → 2 % | 143.4 px | 0.02 | 0.07 | 84 |
| stroke 240 | 26 % → 1 % | 198.4 px | 0.02 | 0.05 | 114 |
| stroke 241 | 3 % → 3 % | 25.9 px | 0.01 | 1.29 | 188 |
| stroke 242 | 3 % → 4 % | 24.9 px | 0.01 | 1.30 | 57 |
| stroke 243 | 2 % → 4 % | 24.2 px | 0.05 | 2.06 | 9 |

Numbers say: wet paint spreads well beyond the stroke.

## Refs v3 · #25 Yellow heavy stroke — own sheet
own sheet 800 × 1198 · Impasto 1.00 · 160 px · 11.1 s

![Refs v3 · #25 Yellow heavy stroke — own sheet](Refs-v3-25-Yellow-heavy-stroke-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 15 % → 6 % | 127.2 px | 0.14 | 0.39 | 4147 |

## Refs v3 · #26 Ink caricature — own sheet
own sheet 800 × 1065 · Ink 0.98 · 64 px · 53.6 s

![Refs v3 · #26 Ink caricature — own sheet](Refs-v3-26-Ink-caricature-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 8 % → 23 % | 21.7 px | 0.73 | 2.95 | 64 |
| stroke 2 | 3 % → 47 % | 65.4 px | 0.76 | 14.41 | 18 |
| stroke 3 | 9 % → 34 % | 52.6 px | 0.76 | 3.80 | 186 |
| stroke 4 | 5 % → 54 % | 160.6 px | 0.76 | 11.57 | 3 |
| stroke 5 | 6 % → 37 % | 32.0 px | 0.75 | 5.78 | 185 |
| stroke 6 | 10 % → 40 % | 325.0 px | 0.76 | 3.94 | 3 |
| stroke 7 | 8 % → 45 % | 79.7 px | 0.76 | 5.34 | 57 |
| stroke 8 | 17 % → 38 % | 118.3 px | 0.75 | 2.29 | 190 |
| stroke 9 | 15 % → 31 % | 102.5 px | 0.77 | 2.15 | 134 |
| stroke 10 | 1 % → 28 % | 29.9 px | 0.74 | 21.79 | 4 |
| stroke 11 | 19 % → 48 % | 135.6 px | 0.76 | 2.52 | 92 |
| stroke 12 | 16 % → 52 % | 288.4 px | 0.76 | 3.19 | 29 |
| stroke 13 | 19 % → 45 % | 130.7 px | 0.75 | 2.33 | 160 |
| stroke 14 | 28 % → 51 % | 362.4 px | 0.76 | 1.85 | 29 |
| stroke 15 | 34 % → 48 % | 546.7 px | 0.76 | 1.41 | 58 |
| stroke 16 | 25 % → 45 % | 503.7 px | 0.76 | 1.81 | 38 |
| stroke 17 | 36 % → 48 % | 301.4 px | 0.76 | 1.35 | 134 |
| stroke 18 | 45 % → 50 % | 802.3 px | 0.76 | 1.12 | 15 |
| stroke 19 | 22 % → 31 % | 129.3 px | 0.75 | 1.40 | 320 |
| stroke 20 | 37 % → 42 % | 657.4 px | 0.76 | 1.12 | 28 |
| stroke 21 | 22 % → 40 % | 591.5 px | 0.74 | 1.79 | 8 |
| stroke 22 | 37 % → 43 % | 319.7 px | 0.75 | 1.16 | 113 |
| stroke 23 | 20 % → 26 % | 241.0 px | 0.73 | 1.27 | 9 |
| stroke 24 | 34 % → 38 % | 160.4 px | 0.76 | 1.11 | 194 |
| stroke 25 | 38 % → 42 % | 412.4 px | 0.75 | 1.09 | 43 |
| stroke 26 | 56 % → 60 % | 990.0 px | 0.76 | 1.07 | 12 |
| stroke 27 | 10 % → 28 % | 78.9 px | 0.74 | 2.91 | 40 |
| stroke 28 | 9 % → 23 % | 76.9 px | 0.73 | 2.75 | 45 |
| stroke 29 | 19 % → 34 % | 170.4 px | 0.73 | 1.83 | 30 |
| stroke 30 | 26 % → 33 % | 812.1 px | 0.74 | 1.29 | 7 |
| stroke 31 | 14 % → 27 % | 116.8 px | 0.74 | 2.01 | 37 |
| stroke 32 | 13 % → 21 % | 96.2 px | 0.74 | 1.65 | 88 |
| stroke 33 | 19 % → 31 % | 348.6 px | 0.73 | 1.64 | 9 |
| stroke 34 | 7 % → 16 % | 61.2 px | 0.73 | 2.24 | 50 |
| stroke 35 | 18 % → 33 % | 242.7 px | 0.73 | 1.80 | 16 |
| stroke 36 | 15 % → 26 % | 121.8 px | 0.73 | 1.79 | 66 |
| stroke 37 | 13 % → 25 % | 140.7 px | 0.73 | 1.89 | 35 |
| stroke 38 | 13 % → 25 % | 125.2 px | 0.72 | 1.86 | 35 |
| stroke 39 | 15 % → 23 % | 136.1 px | 0.73 | 1.50 | 40 |
| stroke 40 | 19 % → 24 % | 201.6 px | 0.72 | 1.29 | 34 |
| stroke 41 | 13 % → 17 % | 76.3 px | 0.73 | 1.23 | 54 |
| stroke 42 | 4 % → 6 % | 11.8 px | 0.75 | 1.65 | 41 |

Numbers say: wet paint spreads well beyond the stroke.

## Refs v3 · #27 Orange impasto swatch — own sheet
own sheet 800 × 1000 · Impasto 1.00 · 57 px · 18.7 s

![Refs v3 · #27 Orange impasto swatch — own sheet](Refs-v3-27-Orange-impasto-swatch-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 7 % → 2 % | 55.4 px | 0.26 | 0.24 | 144 |
| stroke 2 | 12 % → 1 % | 71.6 px | 0.26 | 0.10 | 327 |
| stroke 3 | 17 % → 1 % | 100.8 px | 0.26 | 0.07 | 386 |
| stroke 4 | 23 % → 1 % | 130.2 px | 0.26 | 0.05 | 302 |
| stroke 5 | 19 % → 0 % | 276.2 px | 0.00 | 0.00 | 44 |
| stroke 6 | 24 % → 1 % | 126.3 px | 0.26 | 0.03 | 392 |
| stroke 7 | 28 % → 1 % | 147.8 px | 0.27 | 0.02 | 491 |
| stroke 8 | 39 % → 0 % | 221.1 px | 0.27 | 0.01 | 317 |
| stroke 9 | 41 % → 0 % | 239.0 px | 0.19 | 0.00 | 303 |
| stroke 10 | 41 % → 0 % | 292.8 px | 0.00 | 0.00 | 163 |
| stroke 11 | 37 % → 0 % | 269.5 px | 0.00 | 0.00 | 161 |
| stroke 12 | 34 % → 0 % | 288.1 px | 0.00 | 0.00 | 118 |
| stroke 13 | 32 % → 0 % | 201.1 px | 0.00 | 0.00 | 191 |
| stroke 14 | 30 % → 0 % | 178.0 px | 0.00 | 0.00 | 260 |
| stroke 15 | 30 % → 0 % | 175.1 px | 0.00 | 0.00 | 226 |
| stroke 16 | 36 % → 0 % | 268.1 px | 0.00 | 0.00 | 159 |
| stroke 17 | 35 % → 0 % | 324.3 px | 0.00 | 0.00 | 148 |
| stroke 18 | 3 % → 0 % | 50.0 px | 0.00 | 0.00 | 75 |
| stroke 19 | 4 % → 0 % | 42.3 px | 0.00 | 0.00 | 111 |
| stroke 20 | 8 % → 0 % | 69.5 px | 0.00 | 0.00 | 92 |
| stroke 21 | 11 % → 0 % | 99.1 px | 0.20 | 0.00 | 79 |
| stroke 22 | 15 % → 1 % | 139.5 px | 0.28 | 0.05 | 89 |
| stroke 23 | 19 % → 1 % | 270.9 px | 0.28 | 0.07 | 42 |
| stroke 24 | 2 % → 2 % | 22.3 px | 0.26 | 0.93 | 61 |
| stroke 25 | 2 % → 2 % | 25.0 px | 0.28 | 0.95 | 30 |

## Refs v3 · #28 Miles Davis lines — own sheet
own sheet 800 × 753 · Ink 0.98 · 20 px · 76.4 s

![Refs v3 · #28 Miles Davis lines — own sheet](Refs-v3-28-Miles-Davis-lines-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 5 % → 0 % | 9.0 px | 0.00 | 0.00 | 6 |
| stroke 2 | 3 % → 0 % | 9.3 px | 0.00 | 0.00 | 3 |
| stroke 3 | 8 % → 0 % | 20.9 px | 0.00 | 0.00 | 2 |
| stroke 4 | 14 % → 0 % | 20.1 px | 0.00 | 0.00 | 13 |
| stroke 5 | 8 % → 0 % | 12.5 px | 0.00 | 0.00 | 5 |
| stroke 6 | 7 % → 0 % | 10.6 px | 0.00 | 0.00 | 6 |
| stroke 7 | 6 % → 1 % | 16.4 px | 0.73 | 0.16 | 2 |
| stroke 8 | 5 % → 38 % | 12.4 px | 0.84 | 7.10 | 3 |
| stroke 9 | 3 % → 73 % | 7.7 px | 0.88 | 26.91 | 4 |
| stroke 10 | 3 % → 87 % | 9.0 px | 0.89 | 27.17 | 8 |
| stroke 11 | 2 % → 82 % | 6.6 px | 0.88 | 52.00 | 3 |
| stroke 12 | 3 % → 33 % | 11.4 px | 0.86 | 9.69 | 3 |
| stroke 13 | 4 % → 91 % | 9.5 px | 0.89 | 21.04 | 7 |
| stroke 14 | 11 % → 92 % | 21.4 px | 0.89 | 8.27 | 4 |
| stroke 15 | 6 % → 72 % | 17.2 px | 0.87 | 12.51 | 5 |
| stroke 16 | 4 % → 82 % | 14.9 px | 0.87 | 20.15 | 11 |
| stroke 17 | 23 % → 36 % | 34.2 px | 0.88 | 1.56 | 52 |
| stroke 18 | 9 % → 29 % | 21.1 px | 0.86 | 3.35 | 28 |
| stroke 19 | 8 % → 42 % | 17.8 px | 0.87 | 5.00 | 16 |
| stroke 20 | 8 % → 55 % | 17.7 px | 0.87 | 6.64 | 11 |
| stroke 21 | 21 % → 83 % | 34.0 px | 0.89 | 3.92 | 38 |
| stroke 22 | 16 % → 53 % | 58.0 px | 0.89 | 3.33 | 6 |
| stroke 23 | 8 % → 76 % | 16.7 px | 0.87 | 10.08 | 14 |
| stroke 24 | 15 % → 71 % | 30.4 px | 0.87 | 4.70 | 19 |
| stroke 25 | 24 % → 51 % | 29.6 px | 0.86 | 2.14 | 56 |
| stroke 26 | 11 % → 18 % | 23.9 px | 0.88 | 1.66 | 83 |
| stroke 27 | 20 % → 48 % | 31.8 px | 0.88 | 2.33 | 173 |
| stroke 28 | 10 % → 79 % | 55.2 px | 0.87 | 7.57 | 4 |
| stroke 29 | 30 % → 59 % | 52.8 px | 0.89 | 1.97 | 21 |
| stroke 30 | 15 % → 63 % | 22.5 px | 0.86 | 4.11 | 28 |
| stroke 31 | 29 % → 85 % | 42.2 px | 0.88 | 2.93 | 31 |
| stroke 32 | 60 % → 89 % | 83.3 px | 0.89 | 1.50 | 41 |
| stroke 33 | 28 % → 45 % | 38.2 px | 0.87 | 1.60 | 73 |
| stroke 34 | 22 % → 34 % | 44.8 px | 0.87 | 1.58 | 212 |
| stroke 35 | 16 % → 21 % | 36.0 px | 0.88 | 1.32 | 201 |
| stroke 36 | 17 % → 57 % | 83.7 px | 0.87 | 3.35 | 62 |
| stroke 37 | 25 % → 92 % | 77.9 px | 0.90 | 3.73 | 48 |
| stroke 38 | 26 % → 68 % | 64.4 px | 0.88 | 2.57 | 38 |
| stroke 39 | 8 % → 78 % | 33.6 px | 0.90 | 9.25 | 8 |
| stroke 40 | 4 % → 81 % | 24.7 px | 0.88 | 18.16 | 46 |
| stroke 41 | 12 % → 74 % | 26.0 px | 0.87 | 6.26 | 23 |
| stroke 42 | 31 % → 67 % | 63.7 px | 0.87 | 2.16 | 57 |
| stroke 43 | 10 % → 72 % | 36.2 px | 0.86 | 7.34 | 12 |
| stroke 44 | 10 % → 75 % | 47.6 px | 0.89 | 7.29 | 4 |
| stroke 45 | 14 % → 76 % | 36.4 px | 0.89 | 5.54 | 77 |
| stroke 46 | 25 % → 74 % | 64.6 px | 0.88 | 2.96 | 68 |
| stroke 47 | 12 % → 81 % | 36.8 px | 0.88 | 6.66 | 15 |
| stroke 48 | 29 % → 74 % | 84.2 px | 0.88 | 2.57 | 31 |
| stroke 49 | 27 % → 75 % | 110.6 px | 0.89 | 2.81 | 99 |
| stroke 50 | 37 % → 79 % | 109.2 px | 0.87 | 2.14 | 92 |
| stroke 51 | 29 % → 80 % | 54.2 px | 0.88 | 2.78 | 37 |
| stroke 52 | 23 % → 67 % | 45.9 px | 0.88 | 2.85 | 153 |
| stroke 53 | 26 % → 78 % | 97.0 px | 0.89 | 2.99 | 19 |
| stroke 54 | 27 % → 72 % | 47.2 px | 0.87 | 2.72 | 191 |
| stroke 55 | 42 % → 83 % | 107.3 px | 0.89 | 1.97 | 105 |
| stroke 56 | 50 % → 89 % | 201.8 px | 0.89 | 1.76 | 102 |
| stroke 57 | 26 % → 63 % | 60.8 px | 0.88 | 2.49 | 41 |
| stroke 58 | 50 % → 86 % | 172.7 px | 0.90 | 1.72 | 12 |
| stroke 59 | 53 % → 76 % | 181.3 px | 0.89 | 1.45 | 13 |
| stroke 60 | 20 % → 70 % | 64.0 px | 0.88 | 3.46 | 56 |
| stroke 61 | 31 % → 77 % | 92.7 px | 0.89 | 2.48 | 278 |
| stroke 62 | 28 % → 70 % | 95.5 px | 0.89 | 2.51 | 310 |
| stroke 63 | 27 % → 66 % | 145.6 px | 0.88 | 2.43 | 10 |
| stroke 64 | 25 % → 67 % | 61.5 px | 0.87 | 2.67 | 30 |
| stroke 65 | 23 % → 59 % | 59.0 px | 0.88 | 2.62 | 94 |
| stroke 66 | 40 % → 62 % | 138.6 px | 0.88 | 1.55 | 28 |
| stroke 67 | 45 % → 88 % | 210.9 px | 0.87 | 1.95 | 34 |
| stroke 68 | 13 % → 50 % | 49.8 px | 0.86 | 3.77 | 13 |
| stroke 69 | 15 % → 59 % | 49.4 px | 0.86 | 3.91 | 11 |
| stroke 70 | 44 % → 78 % | 124.6 px | 0.88 | 1.75 | 36 |
| stroke 71 | 67 % → 86 % | 319.1 px | 0.89 | 1.28 | 76 |
| stroke 72 | 59 % → 75 % | 179.8 px | 0.87 | 1.27 | 254 |
| stroke 73 | 51 % → 88 % | 95.8 px | 0.88 | 1.71 | 423 |
| stroke 74 | 40 % → 74 % | 105.4 px | 0.88 | 1.87 | 167 |
| stroke 75 | 64 % → 76 % | 191.6 px | 0.88 | 1.19 | 49 |
| stroke 76 | 70 % → 77 % | 163.1 px | 0.89 | 1.10 | 39 |
| stroke 77 | 36 % → 71 % | 151.1 px | 0.87 | 2.01 | 28 |
| stroke 78 | 23 % → 52 % | 37.3 px | 0.87 | 2.27 | 279 |
| stroke 79 | 49 % → 68 % | 92.8 px | 0.86 | 1.38 | 29 |
| stroke 80 | 62 % → 78 % | 108.9 px | 0.88 | 1.27 | 75 |
| stroke 81 | 48 % → 80 % | 152.7 px | 0.88 | 1.66 | 14 |
| stroke 82 | 56 % → 71 % | 135.3 px | 0.89 | 1.26 | 26 |
| stroke 83 | 23 % → 54 % | 115.1 px | 0.88 | 2.38 | 13 |
| stroke 84 | 39 % → 53 % | 73.0 px | 0.87 | 1.37 | 141 |
| stroke 85 | 59 % → 74 % | 150.9 px | 0.88 | 1.25 | 31 |
| stroke 86 | 66 % → 88 % | 227.1 px | 0.89 | 1.34 | 7 |
| stroke 87 | 71 % → 79 % | 266.6 px | 0.89 | 1.11 | 36 |
| stroke 88 | 66 % → 77 % | 178.9 px | 0.86 | 1.17 | 18 |
| stroke 89 | 23 % → 38 % | 75.0 px | 0.88 | 1.64 | 21 |
| stroke 90 | 22 % → 46 % | 66.5 px | 0.87 | 2.06 | 94 |
| stroke 91 | 6 % → 55 % | 28.8 px | 0.88 | 8.66 | 14 |
| stroke 92 | 47 % → 66 % | 107.1 px | 0.88 | 1.42 | 102 |
| stroke 93 | 55 % → 70 % | 161.3 px | 0.87 | 1.27 | 6 |
| stroke 94 | 63 % → 71 % | 191.2 px | 0.88 | 1.12 | 9 |
| stroke 95 | 34 % → 61 % | 73.6 px | 0.87 | 1.81 | 11 |
| stroke 96 | 30 % → 66 % | 84.0 px | 0.87 | 2.20 | 24 |
| stroke 97 | 46 % → 70 % | 135.8 px | 0.88 | 1.53 | 26 |
| stroke 98 | 77 % → 88 % | 233.3 px | 0.89 | 1.15 | 74 |
| stroke 99 | 40 % → 60 % | 85.8 px | 0.88 | 1.50 | 21 |
| stroke 100 | 69 % → 80 % | 317.2 px | 0.87 | 1.16 | 11 |
| stroke 101 | 69 % → 79 % | 374.7 px | 0.88 | 1.15 | 29 |
| stroke 102 | 20 % → 51 % | 38.4 px | 0.88 | 2.48 | 44 |
| stroke 103 | 31 % → 38 % | 87.8 px | 0.88 | 1.24 | 10 |
| stroke 104 | 26 % → 40 % | 48.9 px | 0.88 | 1.53 | 118 |
| stroke 105 | 79 % → 86 % | 295.2 px | 0.88 | 1.08 | 17 |
| stroke 106 | 76 % → 80 % | 250.3 px | 0.89 | 1.05 | 17 |
| stroke 107 | 40 % → 53 % | 148.1 px | 0.88 | 1.34 | 15 |
| stroke 108 | 48 % → 66 % | 116.0 px | 0.88 | 1.38 | 23 |
| stroke 109 | 70 % → 79 % | 186.8 px | 0.89 | 1.13 | 19 |
| stroke 110 | 52 % → 59 % | 267.4 px | 0.88 | 1.13 | 2 |
| stroke 111 | 29 % → 52 % | 70.3 px | 0.88 | 1.79 | 18 |
| stroke 112 | 55 % → 61 % | 98.7 px | 0.88 | 1.12 | 41 |
| stroke 113 | 63 % → 70 % | 223.8 px | 0.88 | 1.10 | 12 |
| stroke 114 | 56 % → 66 % | 77.8 px | 0.88 | 1.18 | 112 |
| stroke 115 | 64 % → 77 % | 197.0 px | 0.89 | 1.19 | 9 |
| stroke 116 | 74 % → 76 % | 280.2 px | 0.87 | 1.02 | 25 |
| stroke 117 | 79 % → 82 % | 264.4 px | 0.88 | 1.05 | 35 |
| stroke 118 | 32 % → 61 % | 96.8 px | 0.87 | 1.90 | 4 |
| stroke 119 | 80 % → 83 % | 295.1 px | 0.89 | 1.04 | 8 |
| stroke 120 | 52 % → 54 % | 105.6 px | 0.88 | 1.04 | 44 |
| stroke 121 | 79 % → 81 % | 434.6 px | 0.89 | 1.03 | 3 |
| stroke 122 | 50 % → 57 % | 151.2 px | 0.87 | 1.15 | 22 |
| stroke 123 | 41 % → 47 % | 165.3 px | 0.86 | 1.16 | 15 |
| stroke 124 | 91 % → 91 % | 274.4 px | 0.89 | 1.00 | 10 |
| stroke 125 | 70 % → 72 % | 330.9 px | 0.87 | 1.04 | 20 |
| stroke 126 | 83 % → 85 % | 362.7 px | 0.88 | 1.03 | 12 |
| stroke 127 | 46 % → 48 % | 211.3 px | 0.88 | 1.04 | 14 |
| stroke 128 | 75 % → 79 % | 374.2 px | 0.87 | 1.06 | 8 |
| stroke 129 | 41 % → 64 % | 59.1 px | 0.86 | 1.55 | 171 |
| stroke 130 | 45 % → 69 % | 61.7 px | 0.87 | 1.56 | 54 |
| stroke 131 | 48 % → 66 % | 73.4 px | 0.86 | 1.37 | 48 |
| stroke 132 | 67 % → 76 % | 199.1 px | 0.87 | 1.13 | 226 |

Numbers say: wet paint spreads well beyond the stroke.

## Refs v3 · #29 Shrigley asterisk — own sheet
own sheet 800 × 1028 · Watercolour 1.00 + water 50 % · 64 px · 55.5 s

![Refs v3 · #29 Shrigley asterisk — own sheet](Refs-v3-29-Shrigley-asterisk-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 15 % → 46 % | 70.2 px | 0.57 | 3.16 | 780 |
| stroke 2 | 24 % → 55 % | 104.0 px | 0.57 | 2.34 | 2989 |
| stroke 3 | 8 % → 29 % | 78.1 px | 0.57 | 3.62 | 268 |
| stroke 4 | 22 % → 38 % | 111.1 px | 0.58 | 1.72 | 5032 |
| stroke 5 | 30 % → 48 % | 148.6 px | 0.57 | 1.59 | 1122 |
| stroke 6 | 30 % → 38 % | 138.3 px | 0.57 | 1.28 | 5067 |
| stroke 7 | 33 % → 38 % | 183.5 px | 0.57 | 1.14 | 1501 |
| stroke 8 | 31 % → 33 % | 175.6 px | 0.57 | 1.08 | 1346 |
| stroke 9 | 62 % → 69 % | 813.4 px | 0.57 | 1.12 | 327 |
| stroke 10 | 72 % → 83 % | 1328.8 px | 0.57 | 1.15 | 178 |
| stroke 11 | 58 % → 71 % | 796.9 px | 0.57 | 1.21 | 210 |
| stroke 12 | 66 % → 72 % | 967.8 px | 0.57 | 1.10 | 127 |
| stroke 13 | 41 % → 42 % | 272.7 px | 0.57 | 1.02 | 787 |

Numbers say: wet paint spreads well beyond the stroke.

## Refs v3 · #30 Red gouache face — own sheet
own sheet 800 × 1084 · Gouache 1.00 + water 15 % · 55 px · 68.8 s

![Refs v3 · #30 Red gouache face — own sheet](Refs-v3-30-Red-gouache-face-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 8 % → 0 % | 54.3 px | 0.00 | 0.00 | 310 |
| stroke 2 | 9 % → 0 % | 64.4 px | 0.00 | 0.00 | 192 |
| stroke 3 | 15 % → 0 % | 76.1 px | 0.00 | 0.00 | 635 |
| stroke 4 | 14 % → 1 % | 94.5 px | 0.42 | 0.04 | 216 |
| stroke 5 | 21 % → 0 % | 103.7 px | 0.00 | 0.00 | 360 |
| stroke 6 | 20 % → 2 % | 128.4 px | 0.42 | 0.11 | 315 |
| stroke 7 | 29 % → 0 % | 150.4 px | 0.00 | 0.00 | 305 |
| stroke 8 | 22 % → 0 % | 177.4 px | 0.00 | 0.00 | 135 |
| stroke 9 | 27 % → 4 % | 176.6 px | 0.41 | 0.15 | 258 |
| stroke 10 | 38 % → 0 % | 261.2 px | 0.00 | 0.00 | 141 |
| stroke 11 | 17 % → 0 % | 169.2 px | 0.00 | 0.00 | 64 |
| stroke 12 | 28 % → 4 % | 144.4 px | 0.42 | 0.15 | 366 |
| stroke 13 | 38 % → 0 % | 347.5 px | 0.00 | 0.00 | 189 |
| stroke 14 | 19 % → 0 % | 231.0 px | 0.00 | 0.00 | 112 |
| stroke 15 | 33 % → 5 % | 167.3 px | 0.42 | 0.17 | 532 |
| stroke 16 | 31 % → 0 % | 237.4 px | 0.00 | 0.00 | 162 |
| stroke 17 | 17 % → 0 % | 208.5 px | 0.00 | 0.00 | 46 |
| stroke 18 | 39 % → 6 % | 180.4 px | 0.41 | 0.15 | 466 |
| stroke 19 | 16 % → 0 % | 139.8 px | 0.00 | 0.00 | 101 |
| stroke 20 | 35 % → 5 % | 151.6 px | 0.41 | 0.14 | 805 |
| stroke 21 | 21 % → 0 % | 148.9 px | 0.00 | 0.00 | 284 |
| stroke 22 | 42 % → 9 % | 216.8 px | 0.41 | 0.22 | 350 |
| stroke 23 | 34 % → 0 % | 160.1 px | 0.00 | 0.00 | 447 |
| stroke 24 | 40 % → 10 % | 211.1 px | 0.41 | 0.24 | 217 |
| stroke 25 | 39 % → 0 % | 184.3 px | 0.00 | 0.00 | 363 |
| stroke 26 | 39 % → 10 % | 216.1 px | 0.41 | 0.25 | 229 |
| stroke 27 | 43 % → 0 % | 209.1 px | 0.00 | 0.00 | 428 |
| stroke 28 | 35 % → 9 % | 191.8 px | 0.41 | 0.26 | 245 |
| stroke 29 | 43 % → 0 % | 213.9 px | 0.00 | 0.00 | 240 |
| stroke 30 | 43 % → 4 % | 190.0 px | 0.41 | 0.10 | 689 |
| stroke 31 | 42 % → 4 % | 191.9 px | 0.40 | 0.09 | 1093 |
| stroke 32 | 37 % → 6 % | 228.1 px | 0.40 | 0.15 | 578 |
| stroke 33 | 45 % → 0 % | 518.1 px | 0.00 | 0.00 | 190 |
| stroke 34 | 35 % → 0 % | 305.3 px | 0.00 | 0.00 | 152 |
| stroke 35 | 46 % → 0 % | 352.9 px | 0.00 | 0.00 | 277 |
| stroke 36 | 3 % → 0 % | 27.0 px | 0.00 | 0.00 | 271 |
| stroke 37 | 3 % → 0 % | 44.8 px | 0.00 | 0.00 | 5 |
| stroke 38 | 1 % → 0 % | 15.9 px | 0.00 | 0.00 | 5 |
| stroke 39 | 2 % → 0 % | 33.0 px | 0.00 | 0.00 | 17 |
| stroke 40 | 1 % → 9 % | 18.0 px | 0.40 | 15.96 | 40 |
| stroke 41 | 1 % → 8 % | 41.0 px | 0.40 | 7.01 | 14 |
| stroke 42 | 2 % → 8 % | 53.4 px | 0.40 | 4.31 | 17 |
| stroke 43 | 3 % → 9 % | 52.1 px | 0.40 | 3.52 | 22 |
| stroke 44 | 3 % → 8 % | 82.0 px | 0.40 | 2.47 | 24 |
| stroke 45 | 4 % → 8 % | 73.0 px | 0.40 | 1.83 | 21 |
| stroke 46 | 5 % → 7 % | 57.0 px | 0.40 | 1.44 | 69 |
| stroke 47 | 8 % → 4 % | 195.5 px | 0.39 | 0.52 | 19 |
| stroke 48 | 8 % → 6 % | 77.5 px | 0.40 | 0.79 | 27 |
| stroke 49 | 10 % → 7 % | 305.1 px | 0.40 | 0.67 | 4 |
| stroke 50 | 11 % → 9 % | 231.3 px | 0.40 | 0.77 | 9 |
| stroke 51 | 3 % → 4 % | 32.0 px | 0.41 | 1.15 | 20 |
| stroke 52 | 1 % → 0 % | 19.3 px | 0.00 | 0.00 | 4 |
| stroke 53 | 1 % → 0 % | 12.6 px | 0.00 | 0.00 | 6 |
| stroke 54 | 2 % → 0 % | 25.2 px | 0.00 | 0.00 | 4 |
| stroke 55 | 2 % → 0 % | 27.5 px | 0.00 | 0.00 | 8 |
| stroke 56 | 2 % → 0 % | 43.1 px | 0.00 | 0.00 | 4 |
| stroke 57 | 2 % → 0 % | 23.6 px | 0.00 | 0.00 | 7 |
| stroke 58 | 2 % → 0 % | 29.5 px | 0.00 | 0.00 | 14 |
| stroke 59 | 4 % → 0 % | 56.8 px | 0.00 | 0.00 | 43 |
| stroke 60 | 7 % → 0 % | 63.4 px | 0.00 | 0.00 | 31 |
| stroke 61 | 1 % → 0 % | 15.1 px | 0.00 | 0.00 | 5 |
| stroke 62 | 10 % → 0 % | 133.0 px | 0.00 | 0.00 | 12 |
| stroke 63 | 6 % → 0 % | 38.0 px | 0.00 | 0.00 | 45 |
| stroke 64 | 5 % → 0 % | 37.7 px | 0.00 | 0.00 | 36 |
| stroke 65 | 9 % → 0 % | 74.1 px | 0.00 | 0.00 | 43 |
| stroke 66 | 16 % → 0 % | 133.1 px | 0.00 | 0.00 | 59 |
| stroke 67 | 15 % → 0 % | 265.1 px | 0.00 | 0.00 | 46 |
| stroke 68 | 17 % → 0 % | 93.7 px | 0.00 | 0.00 | 166 |
| stroke 69 | 17 % → 0 % | 80.6 px | 0.00 | 0.00 | 200 |
| stroke 70 | 22 % → 0 % | 110.9 px | 0.42 | 0.02 | 182 |
| stroke 71 | 27 % → 0 % | 237.8 px | 0.00 | 0.00 | 309 |
| stroke 72 | 16 % → 0 % | 243.6 px | 0.00 | 0.00 | 26 |
| stroke 73 | 26 % → 2 % | 153.6 px | 0.42 | 0.08 | 101 |
| stroke 74 | 30 % → 0 % | 213.9 px | 0.00 | 0.00 | 142 |
| stroke 75 | 30 % → 0 % | 466.1 px | 0.00 | 0.00 | 32 |
| stroke 76 | 34 % → 0 % | 531.3 px | 0.00 | 0.00 | 27 |
| stroke 77 | 27 % → 0 % | 278.7 px | 0.00 | 0.00 | 65 |
| stroke 78 | 6 % → 0 % | 98.2 px | 0.00 | 0.00 | 33 |
| stroke 79 | 22 % → 0 % | 232.5 px | 0.00 | 0.00 | 44 |
| stroke 80 | 19 % → 0 % | 145.2 px | 0.00 | 0.00 | 128 |
| stroke 81 | 6 % → 0 % | 69.2 px | 0.00 | 0.00 | 139 |
| stroke 82 | 20 % → 0 % | 201.0 px | 0.00 | 0.00 | 87 |
| stroke 83 | 10 % → 0 % | 64.8 px | 0.00 | 0.00 | 65 |
| stroke 84 | 20 % → 0 % | 379.5 px | 0.00 | 0.00 | 12 |
| stroke 85 | 15 % → 0 % | 236.6 px | 0.00 | 0.00 | 16 |
| stroke 86 | 12 % → 0 % | 184.2 px | 0.00 | 0.00 | 16 |
| stroke 87 | 18 % → 0 % | 130.6 px | 0.00 | 0.00 | 68 |
| stroke 88 | 14 % → 0 % | 105.7 px | 0.00 | 0.00 | 51 |
| stroke 89 | 23 % → 0 % | 139.6 px | 0.00 | 0.00 | 79 |
| stroke 90 | 19 % → 0 % | 147.1 px | 0.00 | 0.00 | 52 |
| stroke 91 | 8 % → 0 % | 89.3 px | 0.00 | 0.00 | 13 |
| stroke 92 | 20 % → 0 % | 165.2 px | 0.00 | 0.00 | 126 |
| stroke 93 | 20 % → 0 % | 154.6 px | 0.00 | 0.00 | 86 |
| stroke 94 | 26 % → 0 % | 382.4 px | 0.00 | 0.00 | 38 |
| stroke 95 | 23 % → 0 % | 311.0 px | 0.00 | 0.00 | 19 |
| stroke 96 | 7 % → 0 % | 129.6 px | 0.00 | 0.00 | 11 |
| stroke 97 | 23 % → 0 % | 394.3 px | 0.00 | 0.00 | 14 |
| stroke 98 | 11 % → 0 % | 56.8 px | 0.00 | 0.00 | 70 |
| stroke 99 | 15 % → 0 % | 91.4 px | 0.00 | 0.00 | 48 |
| stroke 100 | 14 % → 0 % | 281.8 px | 0.00 | 0.00 | 24 |
| stroke 101 | 21 % → 0 % | 149.5 px | 0.00 | 0.00 | 33 |
| stroke 102 | 9 % → 0 % | 140.1 px | 0.00 | 0.00 | 22 |
| stroke 103 | 10 % → 0 % | 97.4 px | 0.00 | 0.00 | 30 |
| stroke 104 | 11 % → 0 % | 70.8 px | 0.00 | 0.00 | 61 |
| stroke 105 | 14 % → 0 % | 89.3 px | 0.00 | 0.00 | 59 |
| stroke 106 | 16 % → 0 % | 75.5 px | 0.00 | 0.00 | 134 |
| stroke 107 | 21 % → 0 % | 88.4 px | 0.00 | 0.00 | 159 |
| stroke 108 | 25 % → 0 % | 297.1 px | 0.00 | 0.00 | 19 |
| stroke 109 | 7 % → 0 % | 57.1 px | 0.00 | 0.00 | 36 |
| stroke 110 | 11 % → 0 % | 70.4 px | 0.00 | 0.00 | 83 |
| stroke 111 | 15 % → 2 % | 86.2 px | 0.41 | 0.14 | 403 |
| stroke 112 | 17 % → 3 % | 74.6 px | 0.40 | 0.19 | 146 |
| stroke 113 | 25 % → 3 % | 129.9 px | 0.40 | 0.13 | 145 |
| stroke 114 | 32 % → 2 % | 188.6 px | 0.38 | 0.07 | 72 |
| stroke 115 | 32 % → 1 % | 222.9 px | 0.37 | 0.04 | 37 |
| stroke 116 | 11 % → 0 % | 98.3 px | 0.00 | 0.00 | 67 |
| stroke 117 | 15 % → 0 % | 123.0 px | 0.00 | 0.00 | 70 |
| stroke 118 | 16 % → 0 % | 169.9 px | 0.00 | 0.00 | 76 |
| stroke 119 | 26 % → 0 % | 428.5 px | 0.00 | 0.00 | 36 |
| stroke 120 | 26 % → 0 % | 197.1 px | 0.00 | 0.00 | 219 |
| stroke 121 | 36 % → 0 % | 408.7 px | 0.00 | 0.00 | 55 |
| stroke 122 | 35 % → 0 % | 272.5 px | 0.00 | 0.00 | 91 |
| stroke 123 | 28 % → 0 % | 459.2 px | 0.00 | 0.00 | 27 |
| stroke 124 | 9 % → 10 % | 35.8 px | 0.41 | 1.14 | 378 |

Numbers say: wet paint spreads well beyond the stroke.

## Refs v3 · #31 Warhol blotted line — own sheet
own sheet 800 × 708 · Ink 0.98 · 31 px · 43.0 s

![Refs v3 · #31 Warhol blotted line — own sheet](Refs-v3-31-Warhol-blotted-line-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 1 % → 22 % | 11.0 px | 0.53 | 20.17 | 8 |
| stroke 2 | 2 % → 61 % | 15.6 px | 0.53 | 30.86 | 2 |
| stroke 3 | 2 % → 52 % | 15.8 px | 0.54 | 28.20 | 5 |
| stroke 4 | 2 % → 71 % | 23.5 px | 0.54 | 33.54 | 14 |
| stroke 5 | 1 % → 71 % | 11.8 px | 0.54 | 53.56 | 4 |
| stroke 6 | 5 % → 70 % | 45.3 px | 0.54 | 13.66 | 2 |
| stroke 7 | 3 % → 70 % | 29.2 px | 0.53 | 20.49 | 10 |
| stroke 8 | 2 % → 50 % | 14.3 px | 0.54 | 25.54 | 5 |
| stroke 9 | 5 % → 32 % | 17.3 px | 0.54 | 6.48 | 131 |
| stroke 10 | 4 % → 46 % | 27.9 px | 0.52 | 11.66 | 6 |
| stroke 11 | 4 % → 52 % | 31.3 px | 0.53 | 14.79 | 9 |
| stroke 12 | 5 % → 64 % | 41.0 px | 0.54 | 11.67 | 19 |
| stroke 13 | 9 % → 51 % | 65.7 px | 0.54 | 5.67 | 10 |
| stroke 14 | 8 % → 42 % | 28.0 px | 0.54 | 5.62 | 18 |
| stroke 15 | 7 % → 16 % | 23.9 px | 0.52 | 2.34 | 30 |
| stroke 16 | 2 % → 30 % | 15.4 px | 0.50 | 14.65 | 5 |
| stroke 17 | 6 % → 70 % | 75.9 px | 0.55 | 11.14 | 3 |
| stroke 18 | 18 % → 53 % | 78.5 px | 0.54 | 2.98 | 11 |
| stroke 19 | 11 % → 45 % | 64.5 px | 0.51 | 4.11 | 16 |
| stroke 20 | 12 % → 53 % | 124.9 px | 0.54 | 4.29 | 9 |
| stroke 21 | 1 % → 46 % | 13.1 px | 0.53 | 44.32 | 7 |
| stroke 22 | 5 % → 32 % | 16.3 px | 0.54 | 6.45 | 136 |
| stroke 23 | 3 % → 37 % | 13.5 px | 0.52 | 13.31 | 5 |
| stroke 24 | 3 % → 45 % | 15.1 px | 0.54 | 13.18 | 13 |
| stroke 25 | 18 % → 46 % | 109.4 px | 0.54 | 2.61 | 16 |
| stroke 26 | 15 % → 38 % | 89.5 px | 0.51 | 2.52 | 8 |
| stroke 27 | 13 % → 77 % | 82.3 px | 0.53 | 6.06 | 11 |
| stroke 28 | 12 % → 53 % | 140.3 px | 0.52 | 4.62 | 25 |
| stroke 29 | 13 % → 70 % | 99.0 px | 0.54 | 5.22 | 3 |
| stroke 30 | 5 % → 46 % | 29.3 px | 0.53 | 8.57 | 42 |
| stroke 31 | 12 % → 66 % | 59.7 px | 0.54 | 5.30 | 10 |
| stroke 32 | 7 % → 48 % | 40.5 px | 0.54 | 7.12 | 5 |
| stroke 33 | 11 % → 44 % | 68.9 px | 0.53 | 4.05 | 4 |
| stroke 34 | 11 % → 42 % | 122.5 px | 0.52 | 3.74 | 5 |
| stroke 35 | 15 % → 33 % | 50.3 px | 0.53 | 2.16 | 52 |
| stroke 36 | 11 % → 64 % | 46.6 px | 0.54 | 5.89 | 14 |
| stroke 37 | 19 % → 60 % | 115.0 px | 0.53 | 3.18 | 7 |
| stroke 38 | 16 % → 57 % | 164.6 px | 0.54 | 3.47 | 2 |
| stroke 39 | 12 % → 46 % | 63.8 px | 0.53 | 3.83 | 12 |
| stroke 40 | 14 % → 53 % | 110.8 px | 0.53 | 3.88 | 3 |
| stroke 41 | 6 % → 48 % | 31.7 px | 0.53 | 7.57 | 16 |
| stroke 42 | 9 % → 53 % | 52.1 px | 0.54 | 6.04 | 9 |
| stroke 43 | 25 % → 65 % | 123.9 px | 0.53 | 2.56 | 28 |
| stroke 44 | 23 % → 60 % | 97.9 px | 0.54 | 2.64 | 8 |
| stroke 45 | 29 % → 78 % | 228.7 px | 0.55 | 2.68 | 28 |
| stroke 46 | 8 % → 44 % | 84.0 px | 0.53 | 5.85 | 2 |
| stroke 47 | 21 % → 47 % | 128.9 px | 0.52 | 2.20 | 3 |
| stroke 48 | 21 % → 38 % | 115.3 px | 0.51 | 1.80 | 14 |
| stroke 49 | 33 % → 54 % | 269.1 px | 0.54 | 1.66 | 11 |
| stroke 50 | 32 % → 74 % | 315.2 px | 0.54 | 2.30 | 6 |
| stroke 51 | 31 % → 64 % | 142.3 px | 0.54 | 2.05 | 24 |
| stroke 52 | 19 % → 44 % | 92.0 px | 0.52 | 2.33 | 5 |
| stroke 53 | 11 % → 20 % | 38.5 px | 0.53 | 1.82 | 110 |
| stroke 54 | 25 % → 66 % | 138.0 px | 0.54 | 2.67 | 4 |
| stroke 55 | 7 % → 48 % | 68.1 px | 0.54 | 6.99 | 3 |
| stroke 56 | 40 % → 59 % | 201.5 px | 0.54 | 1.48 | 33 |
| stroke 57 | 18 % → 31 % | 50.8 px | 0.53 | 1.69 | 79 |
| stroke 58 | 33 % → 71 % | 335.6 px | 0.54 | 2.12 | 2 |
| stroke 59 | 42 % → 58 % | 228.0 px | 0.54 | 1.40 | 9 |
| stroke 60 | 39 % → 58 % | 207.5 px | 0.51 | 1.49 | 19 |
| stroke 61 | 15 % → 48 % | 90.6 px | 0.53 | 3.19 | 14 |
| stroke 62 | 28 % → 58 % | 182.3 px | 0.54 | 2.06 | 31 |
| stroke 63 | 33 % → 59 % | 300.6 px | 0.54 | 1.80 | 33 |
| stroke 64 | 26 % → 60 % | 156.3 px | 0.54 | 2.29 | 20 |
| stroke 65 | 25 % → 47 % | 132.6 px | 0.54 | 1.87 | 30 |
| stroke 66 | 29 % → 55 % | 226.1 px | 0.53 | 1.90 | 3 |
| stroke 67 | 26 % → 44 % | 168.6 px | 0.54 | 1.67 | 29 |
| stroke 68 | 18 % → 47 % | 85.6 px | 0.55 | 2.54 | 44 |
| stroke 69 | 25 % → 47 % | 136.0 px | 0.54 | 1.88 | 12 |
| stroke 70 | 39 % → 57 % | 317.4 px | 0.55 | 1.48 | 5 |
| stroke 71 | 26 % → 59 % | 284.8 px | 0.54 | 2.24 | 111 |
| stroke 72 | 36 % → 60 % | 422.0 px | 0.54 | 1.66 | 2 |
| stroke 73 | 37 % → 60 % | 426.9 px | 0.54 | 1.61 | 2 |
| stroke 74 | 40 % → 67 % | 198.1 px | 0.53 | 1.67 | 5 |
| stroke 75 | 17 % → 34 % | 99.2 px | 0.52 | 1.99 | 8 |
| stroke 76 | 43 % → 70 % | 286.1 px | 0.54 | 1.61 | 30 |
| stroke 77 | 21 % → 27 % | 73.5 px | 0.54 | 1.28 | 57 |
| stroke 78 | 35 % → 55 % | 359.3 px | 0.54 | 1.59 | 3 |
| stroke 79 | 27 % → 48 % | 70.4 px | 0.54 | 1.79 | 18 |
| stroke 80 | 36 % → 51 % | 355.0 px | 0.53 | 1.42 | 2 |
| stroke 81 | 42 % → 63 % | 501.2 px | 0.53 | 1.52 | 19 |
| stroke 82 | 21 % → 46 % | 123.4 px | 0.53 | 2.19 | 5 |
| stroke 83 | 34 % → 49 % | 152.2 px | 0.53 | 1.43 | 31 |
| stroke 84 | 40 % → 56 % | 476.7 px | 0.52 | 1.41 | 1 |
| stroke 85 | 49 % → 64 % | 252.2 px | 0.53 | 1.31 | 5 |
| stroke 86 | 45 % → 62 % | 407.3 px | 0.54 | 1.39 | 14 |
| stroke 87 | 26 % → 47 % | 323.6 px | 0.53 | 1.82 | 1 |
| stroke 88 | 46 % → 56 % | 343.9 px | 0.54 | 1.22 | 51 |
| stroke 89 | 49 % → 60 % | 305.3 px | 0.52 | 1.23 | 7 |
| stroke 90 | 61 % → 74 % | 489.9 px | 0.54 | 1.21 | 2 |
| stroke 91 | 29 % → 45 % | 172.9 px | 0.53 | 1.54 | 4 |
| stroke 92 | 32 % → 48 % | 157.3 px | 0.53 | 1.48 | 5 |
| stroke 93 | 35 % → 44 % | 131.2 px | 0.54 | 1.25 | 30 |
| stroke 94 | 38 % → 51 % | 457.2 px | 0.53 | 1.34 | 2 |
| stroke 95 | 36 % → 43 % | 162.8 px | 0.54 | 1.20 | 16 |
| stroke 96 | 29 % → 47 % | 312.9 px | 0.53 | 1.62 | 2 |
| stroke 97 | 53 % → 63 % | 338.9 px | 0.55 | 1.19 | 4 |
| stroke 98 | 62 % → 68 % | 287.7 px | 0.54 | 1.10 | 69 |
| stroke 99 | 20 % → 23 % | 83.0 px | 0.54 | 1.13 | 195 |
| stroke 100 | 31 % → 33 % | 332.6 px | 0.51 | 1.06 | 7 |
| stroke 101 | 11 % → 30 % | 55.2 px | 0.53 | 2.80 | 13 |
| stroke 102 | 52 % → 62 % | 260.1 px | 0.54 | 1.19 | 11 |
| stroke 103 | 33 % → 50 % | 175.0 px | 0.52 | 1.53 | 16 |
| stroke 104 | 56 % → 58 % | 618.5 px | 0.54 | 1.04 | 4 |
| stroke 105 | 50 % → 52 % | 234.5 px | 0.54 | 1.05 | 27 |
| stroke 106 | 41 % → 53 % | 246.4 px | 0.54 | 1.28 | 4 |
| stroke 107 | 26 % → 43 % | 292.3 px | 0.52 | 1.63 | 1 |
| stroke 108 | 45 % → 47 % | 201.1 px | 0.53 | 1.06 | 14 |
| stroke 109 | 41 % → 47 % | 390.6 px | 0.53 | 1.13 | 4 |
| stroke 110 | 36 % → 42 % | 195.1 px | 0.53 | 1.15 | 18 |
| stroke 111 | 27 % → 37 % | 87.4 px | 0.53 | 1.35 | 37 |
| stroke 112 | 61 % → 63 % | 436.3 px | 0.54 | 1.04 | 6 |
| stroke 113 | 73 % → 75 % | 708.0 px | 0.54 | 1.03 | 5 |
| stroke 114 | 46 % → 51 % | 418.4 px | 0.53 | 1.09 | 20 |
| stroke 115 | 21 % → 31 % | 102.1 px | 0.53 | 1.46 | 40 |
| stroke 116 | 57 % → 68 % | 302.3 px | 0.53 | 1.19 | 7 |
| stroke 117 | 46 % → 53 % | 274.3 px | 0.53 | 1.15 | 26 |
| stroke 118 | 39 % → 42 % | 323.5 px | 0.53 | 1.07 | 2 |
| stroke 119 | 45 % → 46 % | 246.2 px | 0.53 | 1.03 | 15 |
| stroke 120 | 45 % → 48 % | 269.4 px | 0.53 | 1.07 | 16 |
| stroke 121 | 36 % → 48 % | 256.8 px | 0.52 | 1.32 | 10 |
| stroke 122 | 50 % → 58 % | 317.8 px | 0.53 | 1.16 | 4 |
| stroke 123 | 48 % → 54 % | 328.4 px | 0.53 | 1.13 | 5 |
| stroke 124 | 58 % → 62 % | 435.6 px | 0.53 | 1.07 | 4 |

Numbers say: wet paint spreads well beyond the stroke.

## Refs v3 · #32 Thick orange swipes — own sheet
own sheet 800 × 800 · Impasto 1.00 · 55 px · 33.4 s

![Refs v3 · #32 Thick orange swipes — own sheet](Refs-v3-32-Thick-orange-swipes-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 13 % → 18 % | 48.1 px | 0.32 | 1.35 | 700 |
| stroke 2 | 22 % → 30 % | 109.5 px | 0.32 | 1.34 | 269 |
| stroke 3 | 15 % → 26 % | 152.0 px | 0.32 | 1.74 | 50 |
| stroke 4 | 28 % → 30 % | 164.0 px | 0.32 | 1.07 | 210 |
| stroke 5 | 18 % → 32 % | 224.8 px | 0.32 | 1.82 | 79 |
| stroke 6 | 33 % → 28 % | 266.2 px | 0.33 | 0.86 | 174 |
| stroke 7 | 20 % → 37 % | 266.2 px | 0.32 | 1.84 | 69 |
| stroke 8 | 29 % → 28 % | 279.0 px | 0.33 | 0.96 | 127 |
| stroke 9 | 25 % → 29 % | 273.2 px | 0.34 | 1.15 | 61 |
| stroke 10 | 21 % → 30 % | 238.7 px | 0.34 | 1.41 | 110 |
| stroke 11 | 10 % → 46 % | 128.6 px | 0.33 | 4.45 | 74 |
| stroke 12 | 18 % → 32 % | 193.1 px | 0.34 | 1.73 | 101 |
| stroke 13 | 14 % → 62 % | 68.9 px | 0.33 | 4.60 | 174 |
| stroke 14 | 17 % → 31 % | 167.1 px | 0.34 | 1.83 | 113 |
| stroke 15 | 18 % → 38 % | 135.0 px | 0.34 | 2.13 | 112 |
| stroke 16 | 19 % → 45 % | 111.3 px | 0.34 | 2.33 | 180 |
| stroke 17 | 22 % → 41 % | 144.9 px | 0.34 | 1.84 | 188 |
| stroke 18 | 25 % → 39 % | 178.9 px | 0.34 | 1.56 | 269 |
| stroke 19 | 26 % → 32 % | 258.5 px | 0.35 | 1.20 | 114 |
| stroke 20 | 24 % → 31 % | 250.2 px | 0.35 | 1.29 | 99 |
| stroke 21 | 20 % → 27 % | 197.4 px | 0.35 | 1.35 | 197 |
| stroke 22 | 6 % → 43 % | 54.4 px | 0.34 | 7.64 | 234 |
| stroke 23 | 18 % → 27 % | 171.3 px | 0.35 | 1.53 | 271 |
| stroke 24 | 13 % → 28 % | 64.7 px | 0.34 | 2.17 | 492 |
| stroke 25 | 17 % → 22 % | 171.4 px | 0.34 | 1.27 | 121 |
| stroke 26 | 25 % → 21 % | 103.1 px | 0.34 | 0.82 | 1050 |
| stroke 27 | 30 % → 12 % | 108.5 px | 0.34 | 0.39 | 711 |
| stroke 28 | 37 % → 8 % | 137.7 px | 0.33 | 0.21 | 549 |
| stroke 29 | 13 % → 42 % | 78.0 px | 0.32 | 3.18 | 331 |
| stroke 30 | 23 % → 47 % | 99.8 px | 0.32 | 2.10 | 664 |
| stroke 31 | 33 % → 52 % | 131.3 px | 0.33 | 1.60 | 518 |
| stroke 32 | 38 % → 55 % | 150.0 px | 0.33 | 1.46 | 793 |
| stroke 33 | 44 % → 66 % | 237.1 px | 0.33 | 1.51 | 365 |
| stroke 34 | 40 % → 57 % | 163.6 px | 0.33 | 1.42 | 686 |
| stroke 35 | 41 % → 62 % | 183.7 px | 0.34 | 1.49 | 516 |
| stroke 36 | 40 % → 58 % | 170.1 px | 0.34 | 1.46 | 547 |
| stroke 37 | 37 % → 48 % | 149.9 px | 0.34 | 1.27 | 534 |
| stroke 38 | 43 % → 48 % | 205.0 px | 0.34 | 1.13 | 477 |
| stroke 39 | 41 % → 40 % | 245.7 px | 0.35 | 0.97 | 235 |

Numbers say: wet paint spreads well beyond the stroke.

## Refs v3 · #33 Red wet-in-wet flames — own sheet
own sheet 800 × 1083 · Watercolour 1.00 + water 60 % · 96 px · 59.3 s

![Refs v3 · #33 Red wet-in-wet flames — own sheet](Refs-v3-33-Red-wet-in-wet-flames-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 25 % → 59 % | 102.5 px | 0.38 | 2.34 | 3215 |
| stroke 2 | 29 % → 58 % | 142.0 px | 0.28 | 2.01 | 755 |
| stroke 3 | 31 % → 58 % | 260.5 px | 0.28 | 1.87 | 675 |
| stroke 4 | 37 % → 61 % | 256.7 px | 0.27 | 1.66 | 617 |
| stroke 5 | 38 % → 60 % | 361.1 px | 0.27 | 1.56 | 433 |
| stroke 6 | 37 % → 58 % | 325.2 px | 0.26 | 1.56 | 543 |
| stroke 7 | 35 % → 56 % | 205.9 px | 0.24 | 1.58 | 943 |
| stroke 8 | 41 % → 53 % | 206.3 px | 0.25 | 1.28 | 1399 |

Numbers say: wet paint spreads well beyond the stroke.

## Refs v3 · #34 Magenta oil patches — own sheet
own sheet 800 × 1420 · Gouache 1.00 + turpentine 20 % · 65 px · 100.7 s

![Refs v3 · #34 Magenta oil patches — own sheet](Refs-v3-34-Magenta-oil-patches-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 27 % → 7 % | 58.6 px | 0.19 | 0.25 | 1918 |
| stroke 2 | 40 % → 12 % | 82.5 px | 0.20 | 0.29 | 1876 |
| stroke 3 | 45 % → 18 % | 156.2 px | 0.21 | 0.40 | 880 |
| stroke 4 | 48 % → 17 % | 222.7 px | 0.21 | 0.36 | 721 |
| stroke 5 | 52 % → 24 % | 428.6 px | 0.22 | 0.47 | 371 |
| stroke 6 | 7 % → 15 % | 70.3 px | 0.22 | 2.03 | 287 |
| stroke 7 | 13 % → 12 % | 96.3 px | 0.21 | 0.97 | 269 |
| stroke 8 | 6 % → 18 % | 67.2 px | 0.22 | 3.01 | 104 |
| stroke 9 | 9 % → 25 % | 129.5 px | 0.22 | 2.73 | 167 |
| stroke 10 | 17 % → 18 % | 65.4 px | 0.22 | 1.02 | 515 |
| stroke 11 | 26 % → 13 % | 224.9 px | 0.22 | 0.51 | 155 |
| stroke 12 | 12 % → 12 % | 101.6 px | 0.22 | 0.97 | 159 |
| stroke 13 | 13 % → 15 % | 105.2 px | 0.21 | 1.12 | 159 |
| stroke 14 | 19 % → 16 % | 136.7 px | 0.21 | 0.89 | 186 |
| stroke 15 | 24 % → 13 % | 181.2 px | 0.21 | 0.54 | 318 |
| stroke 16 | 28 % → 9 % | 229.8 px | 0.21 | 0.33 | 222 |
| stroke 17 | 33 % → 13 % | 410.1 px | 0.21 | 0.39 | 202 |
| stroke 18 | 3 % → 38 % | 24.1 px | 0.21 | 14.38 | 48 |
| stroke 19 | 21 % → 0 % | 60.9 px | 0.00 | 0.00 | 548 |
| stroke 20 | 25 % → 0 % | 159.5 px | 0.00 | 0.00 | 315 |
| stroke 21 | 23 % → 0 % | 248.9 px | 0.00 | 0.00 | 271 |
| stroke 22 | 21 % → 10 % | 128.4 px | 0.22 | 0.48 | 517 |
| stroke 23 | 24 % → 14 % | 147.2 px | 0.22 | 0.58 | 940 |
| stroke 24 | 28 % → 16 % | 171.0 px | 0.22 | 0.56 | 771 |
| stroke 25 | 32 % → 16 % | 189.1 px | 0.22 | 0.51 | 768 |
| stroke 26 | 31 % → 17 % | 184.7 px | 0.22 | 0.53 | 408 |
| stroke 27 | 35 % → 6 % | 250.0 px | 0.22 | 0.17 | 224 |
| stroke 28 | 35 % → 2 % | 287.1 px | 0.22 | 0.05 | 273 |
| stroke 29 | 32 % → 3 % | 274.8 px | 0.21 | 0.10 | 106 |
| stroke 30 | 28 % → 7 % | 213.0 px | 0.22 | 0.24 | 227 |
| stroke 31 | 26 % → 8 % | 204.6 px | 0.22 | 0.32 | 138 |
| stroke 32 | 27 % → 9 % | 222.4 px | 0.22 | 0.32 | 124 |
| stroke 33 | 27 % → 9 % | 228.7 px | 0.22 | 0.32 | 310 |
| stroke 34 | 26 % → 8 % | 199.2 px | 0.22 | 0.32 | 286 |
| stroke 35 | 25 % → 7 % | 162.9 px | 0.22 | 0.29 | 1595 |
| stroke 36 | 26 % → 7 % | 178.0 px | 0.22 | 0.25 | 481 |
| stroke 37 | 33 % → 5 % | 425.1 px | 0.22 | 0.15 | 112 |
| stroke 38 | 9 % → 0 % | 78.8 px | 0.00 | 0.00 | 96 |
| stroke 39 | 15 % → 0 % | 108.3 px | 0.00 | 0.00 | 92 |
| stroke 40 | 22 % → 0 % | 156.6 px | 0.00 | 0.00 | 218 |
| stroke 41 | 28 % → 0 % | 217.0 px | 0.00 | 0.00 | 183 |
| stroke 42 | 19 % → 0 % | 175.4 px | 0.00 | 0.00 | 72 |
| stroke 43 | 19 % → 0 % | 171.4 px | 0.00 | 0.00 | 57 |
| stroke 44 | 22 % → 0 % | 159.8 px | 0.00 | 0.00 | 83 |
| stroke 45 | 33 % → 0 % | 180.7 px | 0.00 | 0.00 | 112 |
| stroke 46 | 12 % → 32 % | 70.4 px | 0.21 | 2.59 | 76 |
| stroke 47 | 44 % → 0 % | 179.8 px | 0.24 | 0.00 | 314 |
| stroke 48 | 13 % → 37 % | 68.5 px | 0.21 | 2.83 | 382 |
| stroke 49 | 16 % → 43 % | 202.6 px | 0.21 | 2.70 | 71 |
| stroke 50 | 6 % → 2 % | 75.9 px | 0.22 | 0.33 | 61 |
| stroke 51 | 19 % → 1 % | 75.4 px | 0.20 | 0.04 | 309 |
| stroke 52 | 28 % → 0 % | 109.5 px | 0.00 | 0.00 | 396 |
| stroke 53 | 38 % → 0 % | 149.8 px | 0.00 | 0.00 | 289 |
| stroke 54 | 44 % → 3 % | 172.5 px | 0.22 | 0.07 | 310 |
| stroke 55 | 12 % → 0 % | 71.0 px | 0.00 | 0.00 | 104 |
| stroke 56 | 56 % → 8 % | 304.1 px | 0.23 | 0.13 | 157 |
| stroke 57 | 38 % → 8 % | 133.2 px | 0.22 | 0.21 | 526 |
| stroke 58 | 52 % → 11 % | 275.0 px | 0.22 | 0.22 | 344 |
| stroke 59 | 43 % → 19 % | 265.4 px | 0.22 | 0.45 | 417 |
| stroke 60 | 38 % → 0 % | 227.1 px | 0.00 | 0.00 | 204 |
| stroke 61 | 52 % → 16 % | 277.8 px | 0.22 | 0.30 | 191 |
| stroke 62 | 46 % → 32 % | 425.5 px | 0.22 | 0.70 | 152 |
| stroke 63 | 52 % → 31 % | 209.1 px | 0.21 | 0.60 | 411 |
| stroke 64 | 2 % → 6 % | 24.4 px | 0.21 | 2.62 | 93 |
| stroke 65 | 11 % → 35 % | 70.2 px | 0.22 | 3.22 | 291 |
| stroke 66 | 24 % → 29 % | 92.0 px | 0.22 | 1.20 | 731 |
| stroke 67 | 35 % → 21 % | 138.1 px | 0.22 | 0.60 | 642 |
| stroke 68 | 40 % → 9 % | 146.8 px | 0.22 | 0.21 | 694 |
| stroke 69 | 46 % → 1 % | 165.7 px | 0.18 | 0.02 | 488 |
| stroke 70 | 46 % → 0 % | 167.0 px | 0.00 | 0.00 | 430 |
| stroke 71 | 50 % → 0 % | 182.0 px | 0.00 | 0.00 | 450 |
| stroke 72 | 7 % → 23 % | 74.5 px | 0.22 | 3.40 | 120 |
| stroke 73 | 14 % → 20 % | 99.3 px | 0.22 | 1.48 | 138 |
| stroke 74 | 20 % → 26 % | 132.9 px | 0.21 | 1.30 | 224 |
| stroke 75 | 28 % → 32 % | 238.2 px | 0.22 | 1.18 | 158 |
| stroke 76 | 25 % → 38 % | 321.1 px | 0.21 | 1.54 | 55 |
| stroke 77 | 13 % → 25 % | 135.8 px | 0.21 | 1.94 | 53 |
| stroke 78 | 19 % → 40 % | 166.4 px | 0.21 | 2.11 | 73 |
| stroke 79 | 2 % → 0 % | 25.0 px | 0.00 | 0.00 | 42 |
| stroke 80 | 13 % → 0 % | 67.3 px | 0.00 | 0.00 | 286 |
| stroke 81 | 24 % → 0 % | 89.4 px | 0.00 | 0.00 | 623 |
| stroke 82 | 35 % → 0 % | 128.7 px | 0.00 | 0.00 | 564 |
| stroke 83 | 45 % → 0 % | 164.6 px | 0.00 | 0.00 | 853 |
| stroke 84 | 49 % → 0 % | 181.8 px | 0.00 | 0.00 | 1047 |
| stroke 85 | 50 % → 0 % | 187.2 px | 0.00 | 0.00 | 1002 |
| stroke 86 | 48 % → 0 % | 221.1 px | 0.24 | 0.00 | 583 |
| stroke 87 | 1 % → 0 % | 13.3 px | 0.00 | 0.00 | 14 |
| stroke 88 | 9 % → 38 % | 20.7 px | 0.21 | 4.04 | 310 |
| stroke 89 | 8 % → 0 % | 23.9 px | 0.00 | 0.00 | 109 |
| stroke 90 | 8 % → 13 % | 77.8 px | 0.22 | 1.69 | 84 |
| stroke 91 | 13 % → 13 % | 129.5 px | 0.22 | 0.97 | 92 |
| stroke 92 | 15 % → 47 % | 71.2 px | 0.21 | 3.16 | 302 |
| stroke 93 | 22 % → 50 % | 94.1 px | 0.21 | 2.27 | 310 |
| stroke 94 | 29 % → 57 % | 168.4 px | 0.21 | 1.95 | 258 |
| stroke 95 | 35 % → 64 % | 197.0 px | 0.22 | 1.84 | 390 |
| stroke 96 | 39 % → 57 % | 157.7 px | 0.22 | 1.44 | 350 |
| stroke 97 | 40 % → 48 % | 160.6 px | 0.22 | 1.18 | 436 |
| stroke 98 | 45 % → 44 % | 185.4 px | 0.22 | 0.98 | 362 |
| stroke 99 | 13 % → 30 % | 71.5 px | 0.21 | 2.39 | 243 |
| stroke 100 | 21 % → 38 % | 119.7 px | 0.21 | 1.84 | 239 |
| stroke 101 | 29 % → 49 % | 191.4 px | 0.21 | 1.67 | 170 |
| stroke 102 | 36 % → 60 % | 277.8 px | 0.21 | 1.66 | 140 |
| stroke 103 | 31 % → 50 % | 185.3 px | 0.21 | 1.62 | 217 |
| stroke 104 | 31 % → 46 % | 188.8 px | 0.21 | 1.51 | 203 |
| stroke 105 | 30 % → 40 % | 185.0 px | 0.21 | 1.33 | 327 |
| stroke 106 | 30 % → 33 % | 177.1 px | 0.21 | 1.08 | 328 |
| stroke 107 | 41 % → 41 % | 470.9 px | 0.21 | 0.99 | 98 |

Numbers say: wet paint spreads well beyond the stroke.

## Refs v3 · #35 Red band with runs — own sheet
own sheet 800 × 1191 · Watercolour 1.00 + water 75 % · 88 px · 39.4 s

![Refs v3 · #35 Red band with runs — own sheet](Refs-v3-35-Red-band-with-runs-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 39 % → 47 % | 148.5 px | 0.32 | 1.20 | 3830 |

## Refs v3 · #36 Magenta letters flat — own sheet
own sheet 800 × 1000 · Gouache 1.00 + water 15 % · 64 px · 48.1 s

![Refs v3 · #36 Magenta letters flat — own sheet](Refs-v3-36-Magenta-letters-flat-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 3 % → 37 % | 75.3 px | 0.40 | 10.99 | 96 |
| stroke 2 | 6 % → 35 % | 200.8 px | 0.40 | 5.81 | 28 |
| stroke 3 | 7 % → 26 % | 98.4 px | 0.40 | 3.84 | 68 |
| stroke 4 | 12 % → 31 % | 149.7 px | 0.40 | 2.58 | 51 |
| stroke 5 | 21 % → 35 % | 126.6 px | 0.41 | 1.69 | 332 |
| stroke 6 | 9 % → 31 % | 62.9 px | 0.40 | 3.38 | 214 |
| stroke 7 | 26 % → 39 % | 183.9 px | 0.40 | 1.51 | 126 |
| stroke 8 | 5 % → 43 % | 77.6 px | 0.40 | 7.92 | 132 |
| stroke 9 | 9 % → 42 % | 143.4 px | 0.40 | 4.57 | 154 |
| stroke 10 | 14 % → 33 % | 176.5 px | 0.40 | 2.33 | 181 |
| stroke 11 | 19 % → 37 % | 227.8 px | 0.40 | 1.95 | 209 |
| stroke 12 | 22 % → 38 % | 326.9 px | 0.40 | 1.69 | 644 |
| stroke 13 | 39 % → 42 % | 200.3 px | 0.40 | 1.08 | 532 |
| stroke 14 | 26 % → 33 % | 76.3 px | 0.41 | 1.26 | 1228 |
| stroke 15 | 11 % → 41 % | 242.3 px | 0.41 | 3.60 | 49 |
| stroke 16 | 18 % → 42 % | 135.6 px | 0.40 | 2.30 | 286 |
| stroke 17 | 29 % → 42 % | 284.3 px | 0.40 | 1.46 | 158 |
| stroke 18 | 29 % → 43 % | 456.5 px | 0.40 | 1.51 | 82 |
| stroke 19 | 30 % → 43 % | 310.3 px | 0.40 | 1.43 | 82 |
| stroke 20 | 16 % → 40 % | 584.4 px | 0.41 | 2.55 | 10 |
| stroke 21 | 27 % → 45 % | 125.2 px | 0.41 | 1.65 | 255 |
| stroke 22 | 23 % → 45 % | 181.3 px | 0.41 | 1.93 | 197 |
| stroke 23 | 17 % → 48 % | 199.9 px | 0.41 | 2.79 | 80 |
| stroke 24 | 11 % → 50 % | 107.5 px | 0.41 | 4.59 | 111 |
| stroke 25 | 27 % → 37 % | 330.0 px | 0.40 | 1.38 | 280 |
| stroke 26 | 37 % → 40 % | 450.6 px | 0.41 | 1.10 | 144 |
| stroke 27 | 36 % → 40 % | 445.3 px | 0.41 | 1.11 | 114 |
| stroke 28 | 6 % → 52 % | 65.5 px | 0.41 | 8.25 | 83 |
| stroke 29 | 31 % → 41 % | 157.6 px | 0.40 | 1.33 | 766 |
| stroke 30 | 41 % → 47 % | 257.9 px | 0.41 | 1.15 | 681 |
| stroke 31 | 31 % → 43 % | 94.5 px | 0.41 | 1.36 | 966 |
| stroke 32 | 31 % → 45 % | 115.2 px | 0.41 | 1.43 | 349 |
| stroke 33 | 21 % → 45 % | 340.4 px | 0.41 | 2.14 | 78 |
| stroke 34 | 12 % → 46 % | 151.6 px | 0.41 | 3.72 | 162 |
| stroke 35 | 36 % → 43 % | 244.8 px | 0.41 | 1.20 | 330 |
| stroke 36 | 33 % → 40 % | 377.7 px | 0.41 | 1.19 | 181 |
| stroke 37 | 13 % → 35 % | 108.0 px | 0.42 | 2.74 | 66 |
| stroke 38 | 28 % → 44 % | 321.6 px | 0.41 | 1.56 | 65 |
| stroke 39 | 26 % → 37 % | 220.8 px | 0.42 | 1.43 | 68 |
| stroke 40 | 11 % → 28 % | 197.9 px | 0.42 | 2.53 | 32 |
| stroke 41 | 23 % → 35 % | 301.4 px | 0.42 | 1.53 | 37 |
| stroke 42 | 34 % → 36 % | 256.2 px | 0.42 | 1.05 | 158 |
| stroke 43 | 31 % → 31 % | 709.4 px | 0.42 | 1.00 | 25 |
| stroke 44 | 40 % → 40 % | 320.5 px | 0.41 | 1.01 | 205 |

Numbers say: wet paint spreads well beyond the stroke.

## Refs v3 · #37 Oil still life — own sheet
own sheet 800 × 810 · Gouache 1.00 + turpentine 20 % · 20 px · 64.8 s

![Refs v3 · #37 Oil still life — own sheet](Refs-v3-37-Oil-still-life-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 6 % → 0 % | 27.4 px | 0.00 | 0.00 | 17 |
| stroke 2 | 10 % → 0 % | 45.0 px | 0.00 | 0.00 | 5 |
| stroke 3 | 14 % → 0 % | 38.0 px | 0.00 | 0.00 | 47 |
| stroke 4 | 24 % → 0 % | 118.6 px | 0.00 | 0.00 | 6 |
| stroke 5 | 26 % → 0 % | 138.3 px | 0.00 | 0.00 | 5 |
| stroke 6 | 27 % → 0 % | 72.8 px | 0.00 | 0.00 | 30 |
| stroke 7 | 25 % → 0 % | 61.7 px | 0.00 | 0.00 | 35 |
| stroke 8 | 30 % → 0 % | 75.4 px | 0.00 | 0.00 | 39 |
| stroke 9 | 33 % → 0 % | 79.9 px | 0.00 | 0.00 | 56 |
| stroke 10 | 34 % → 0 % | 83.8 px | 0.00 | 0.00 | 32 |
| stroke 11 | 22 % → 0 % | 66.2 px | 0.00 | 0.00 | 17 |
| stroke 12 | 20 % → 0 % | 53.7 px | 0.00 | 0.00 | 34 |
| stroke 13 | 18 % → 0 % | 78.8 px | 0.00 | 0.00 | 10 |
| stroke 14 | 35 % → 0 % | 93.9 px | 0.00 | 0.00 | 21 |
| stroke 15 | 21 % → 0 % | 87.3 px | 0.00 | 0.00 | 9 |
| stroke 16 | 32 % → 0 % | 81.3 px | 0.00 | 0.00 | 130 |
| stroke 17 | 9 % → 0 % | 23.6 px | 0.00 | 0.00 | 58 |
| stroke 18 | 18 % → 0 % | 31.0 px | 0.00 | 0.00 | 135 |
| stroke 19 | 32 % → 0 % | 58.1 px | 0.00 | 0.00 | 87 |
| stroke 20 | 10 % → 17 % | 22.6 px | 0.16 | 1.80 | 33 |
| stroke 21 | 16 % → 18 % | 40.1 px | 0.16 | 1.14 | 31 |
| stroke 22 | 25 % → 22 % | 77.4 px | 0.16 | 0.87 | 22 |
| stroke 23 | 7 % → 7 % | 21.3 px | 0.16 | 1.03 | 13 |
| stroke 24 | 17 % → 0 % | 36.4 px | 0.00 | 0.00 | 464 |
| stroke 25 | 30 % → 0 % | 44.0 px | 0.00 | 0.00 | 230 |
| stroke 26 | 45 % → 0 % | 67.2 px | 0.00 | 0.00 | 159 |
| stroke 27 | 51 % → 0 % | 80.4 px | 0.00 | 0.00 | 133 |
| stroke 28 | 14 % → 0 % | 37.8 px | 0.00 | 0.00 | 86 |
| stroke 29 | 22 % → 0 % | 59.1 px | 0.00 | 0.00 | 51 |
| stroke 30 | 30 % → 0 % | 84.3 px | 0.00 | 0.00 | 33 |
| stroke 31 | 14 % → 0 % | 51.0 px | 0.00 | 0.00 | 15 |
| stroke 32 | 21 % → 0 % | 54.0 px | 0.00 | 0.00 | 62 |
| stroke 33 | 36 % → 0 % | 140.8 px | 0.00 | 0.00 | 22 |
| stroke 34 | 13 % → 0 % | 37.9 px | 0.00 | 0.00 | 19 |
| stroke 35 | 20 % → 0 % | 52.2 px | 0.00 | 0.00 | 44 |
| stroke 36 | 31 % → 0 % | 83.8 px | 0.00 | 0.00 | 61 |
| stroke 37 | 36 % → 0 % | 133.9 px | 0.00 | 0.00 | 19 |
| stroke 38 | 12 % → 0 % | 37.6 px | 0.00 | 0.00 | 35 |
| stroke 39 | 18 % → 0 % | 43.9 px | 0.15 | 0.02 | 87 |
| stroke 40 | 27 % → 0 % | 70.3 px | 0.00 | 0.00 | 50 |
| stroke 41 | 13 % → 0 % | 27.6 px | 0.00 | 0.00 | 34 |
| stroke 42 | 18 % → 0 % | 36.2 px | 0.00 | 0.00 | 76 |
| stroke 43 | 25 % → 0 % | 48.3 px | 0.00 | 0.00 | 86 |
| stroke 44 | 32 % → 0 % | 77.1 px | 0.00 | 0.00 | 28 |
| stroke 45 | 34 % → 0 % | 82.5 px | 0.00 | 0.00 | 24 |
| stroke 46 | 45 % → 0 % | 92.9 px | 0.00 | 0.00 | 30 |
| stroke 47 | 30 % → 0 % | 114.4 px | 0.00 | 0.00 | 9 |
| stroke 48 | 41 % → 0 % | 82.8 px | 0.00 | 0.00 | 66 |
| stroke 49 | 28 % → 0 % | 135.8 px | 0.00 | 0.00 | 10 |
| stroke 50 | 33 % → 0 % | 87.9 px | 0.00 | 0.00 | 15 |
| stroke 51 | 46 % → 0 % | 101.6 px | 0.00 | 0.00 | 31 |
| stroke 52 | 39 % → 0 % | 152.2 px | 0.00 | 0.00 | 12 |
| stroke 53 | 42 % → 0 % | 116.5 px | 0.00 | 0.00 | 72 |
| stroke 54 | 7 % → 0 % | 28.9 px | 0.00 | 0.00 | 17 |
| stroke 55 | 6 % → 0 % | 32.8 px | 0.00 | 0.00 | 11 |
| stroke 56 | 12 % → 0 % | 33.8 px | 0.00 | 0.00 | 34 |
| stroke 57 | 22 % → 0 % | 63.7 px | 0.00 | 0.00 | 45 |
| stroke 58 | 29 % → 0 % | 105.8 px | 0.00 | 0.00 | 16 |
| stroke 59 | 16 % → 0 % | 41.9 px | 0.00 | 0.00 | 18 |
| stroke 60 | 20 % → 0 % | 51.5 px | 0.00 | 0.00 | 32 |
| stroke 61 | 33 % → 0 % | 50.2 px | 0.00 | 0.00 | 103 |
| stroke 62 | 39 % → 0 % | 50.6 px | 0.00 | 0.00 | 186 |
| stroke 63 | 12 % → 0 % | 43.8 px | 0.00 | 0.00 | 10 |
| stroke 64 | 58 % → 0 % | 65.4 px | 0.00 | 0.00 | 166 |
| stroke 65 | 73 % → 0 % | 68.8 px | 0.00 | 0.00 | 287 |
| stroke 66 | 62 % → 0 % | 57.3 px | 0.00 | 0.00 | 237 |
| stroke 67 | 73 % → 0 % | 61.1 px | 0.00 | 0.00 | 87 |
| stroke 68 | 16 % → 8 % | 39.7 px | 0.13 | 0.46 | 37 |
| stroke 69 | 31 % → 6 % | 69.4 px | 0.13 | 0.20 | 46 |
| stroke 70 | 35 % → 5 % | 72.8 px | 0.13 | 0.13 | 69 |
| stroke 71 | 43 % → 5 % | 98.7 px | 0.13 | 0.11 | 69 |
| stroke 72 | 42 % → 1 % | 94.1 px | 0.12 | 0.02 | 45 |
| stroke 73 | 42 % → 0 % | 87.9 px | 0.00 | 0.00 | 63 |
| stroke 74 | 51 % → 0 % | 122.7 px | 0.00 | 0.00 | 33 |
| stroke 75 | 47 % → 0 % | 147.9 px | 0.00 | 0.00 | 17 |
| stroke 76 | 13 % → 0 % | 41.7 px | 0.00 | 0.00 | 22 |
| stroke 77 | 24 % → 0 % | 61.4 px | 0.00 | 0.00 | 57 |
| stroke 78 | 25 % → 0 % | 62.0 px | 0.00 | 0.00 | 262 |
| stroke 79 | 40 % → 0 % | 166.0 px | 0.00 | 0.00 | 22 |
| stroke 80 | 41 % → 0 % | 103.5 px | 0.00 | 0.00 | 67 |
| stroke 81 | 38 % → 0 % | 120.8 px | 0.00 | 0.00 | 36 |
| stroke 82 | 47 % → 0 % | 119.1 px | 0.00 | 0.00 | 99 |
| stroke 83 | 27 % → 0 % | 79.1 px | 0.00 | 0.00 | 282 |
| stroke 84 | 35 % → 0 % | 97.9 px | 0.00 | 0.00 | 63 |
| stroke 85 | 52 % → 0 % | 219.0 px | 0.00 | 0.00 | 22 |
| stroke 86 | 44 % → 0 % | 115.0 px | 0.00 | 0.00 | 85 |
| stroke 87 | 39 % → 0 % | 117.8 px | 0.00 | 0.00 | 31 |
| stroke 88 | 34 % → 0 % | 89.9 px | 0.00 | 0.00 | 78 |
| stroke 89 | 30 % → 0 % | 76.9 px | 0.00 | 0.00 | 80 |
| stroke 90 | 43 % → 0 % | 185.5 px | 0.00 | 0.00 | 9 |
| stroke 91 | 31 % → 0 % | 110.6 px | 0.00 | 0.00 | 52 |
| stroke 92 | 36 % → 0 % | 121.5 px | 0.00 | 0.00 | 45 |
| stroke 93 | 23 % → 0 % | 91.2 px | 0.00 | 0.00 | 29 |
| stroke 94 | 35 % → 0 % | 143.8 px | 0.00 | 0.00 | 11 |
| stroke 95 | 34 % → 0 % | 110.2 px | 0.00 | 0.00 | 39 |
| stroke 96 | 34 % → 0 % | 108.8 px | 0.00 | 0.00 | 70 |
| stroke 97 | 16 % → 0 % | 40.6 px | 0.00 | 0.00 | 64 |
| stroke 98 | 35 % → 0 % | 91.9 px | 0.00 | 0.00 | 96 |
| stroke 99 | 31 % → 0 % | 61.6 px | 0.00 | 0.00 | 44 |
| stroke 100 | 35 % → 0 % | 90.2 px | 0.00 | 0.00 | 56 |
| stroke 101 | 40 % → 0 % | 82.4 px | 0.00 | 0.00 | 29 |
| stroke 102 | 43 % → 0 % | 109.4 px | 0.00 | 0.00 | 49 |
| stroke 103 | 51 % → 0 % | 138.1 px | 0.00 | 0.00 | 14 |
| stroke 104 | 51 % → 0 % | 155.6 px | 0.00 | 0.00 | 22 |
| stroke 105 | 12 % → 0 % | 49.9 px | 0.00 | 0.00 | 16 |
| stroke 106 | 39 % → 0 % | 96.6 px | 0.00 | 0.00 | 16 |
| stroke 107 | 19 % → 0 % | 59.0 px | 0.00 | 0.00 | 23 |
| stroke 108 | 37 % → 0 % | 91.4 px | 0.00 | 0.00 | 16 |
| stroke 109 | 24 % → 0 % | 60.2 px | 0.00 | 0.00 | 47 |
| stroke 110 | 26 % → 0 % | 51.1 px | 0.00 | 0.00 | 88 |
| stroke 111 | 23 % → 0 % | 93.7 px | 0.00 | 0.00 | 10 |
| stroke 112 | 34 % → 0 % | 88.8 px | 0.00 | 0.00 | 46 |
| stroke 113 | 30 % → 0 % | 62.3 px | 0.00 | 0.00 | 87 |
| stroke 114 | 35 % → 0 % | 87.0 px | 0.00 | 0.00 | 122 |
| stroke 115 | 36 % → 0 % | 90.1 px | 0.00 | 0.00 | 126 |
| stroke 116 | 44 % → 0 % | 100.9 px | 0.00 | 0.00 | 110 |
| stroke 117 | 67 % → 0 % | 140.2 px | 0.00 | 0.00 | 35 |
| stroke 118 | 50 % → 0 % | 142.2 px | 0.00 | 0.00 | 29 |
| stroke 119 | 63 % → 0 % | 186.4 px | 0.00 | 0.00 | 10 |
| stroke 120 | 44 % → 0 % | 181.7 px | 0.00 | 0.00 | 12 |
| stroke 121 | 45 % → 0 % | 91.1 px | 0.00 | 0.00 | 41 |
| stroke 122 | 44 % → 0 % | 106.3 px | 0.00 | 0.00 | 18 |
| stroke 123 | 15 % → 9 % | 43.0 px | 0.15 | 0.60 | 62 |
| stroke 124 | 22 % → 25 % | 88.9 px | 0.15 | 1.14 | 15 |
| stroke 125 | 11 % → 0 % | 45.5 px | 0.00 | 0.00 | 14 |
| stroke 126 | 20 % → 1 % | 69.7 px | 0.18 | 0.05 | 23 |
| stroke 127 | 21 % → 5 % | 84.9 px | 0.17 | 0.26 | 20 |
| stroke 128 | 16 % → 10 % | 42.1 px | 0.16 | 0.65 | 41 |
| stroke 129 | 19 % → 0 % | 43.1 px | 0.00 | 0.00 | 98 |
| stroke 130 | 32 % → 4 % | 59.6 px | 0.16 | 0.13 | 83 |
| stroke 131 | 37 % → 11 % | 68.6 px | 0.16 | 0.30 | 130 |
| stroke 132 | 34 % → 15 % | 75.3 px | 0.16 | 0.45 | 54 |
| stroke 133 | 12 % → 19 % | 25.7 px | 0.15 | 1.65 | 40 |
| stroke 134 | 13 % → 0 % | 38.7 px | 0.00 | 0.00 | 30 |
| stroke 135 | 19 % → 0 % | 46.4 px | 0.00 | 0.00 | 95 |
| stroke 136 | 27 % → 0 % | 67.2 px | 0.00 | 0.00 | 108 |
| stroke 137 | 31 % → 0 % | 74.9 px | 0.00 | 0.00 | 77 |
| stroke 138 | 40 % → 0 % | 96.7 px | 0.00 | 0.00 | 89 |
| stroke 139 | 49 % → 0 % | 116.3 px | 0.00 | 0.00 | 142 |
| stroke 140 | 51 % → 0 % | 155.9 px | 0.00 | 0.00 | 36 |
| stroke 141 | 52 % → 0 % | 166.8 px | 0.00 | 0.00 | 62 |
| stroke 142 | 49 % → 0 % | 148.1 px | 0.00 | 0.00 | 22 |
| stroke 143 | 56 % → 0 % | 216.8 px | 0.00 | 0.00 | 12 |
| stroke 144 | 42 % → 0 % | 133.1 px | 0.00 | 0.00 | 64 |
| stroke 145 | 15 % → 0 % | 58.0 px | 0.00 | 0.00 | 12 |
| stroke 146 | 33 % → 0 % | 115.8 px | 0.00 | 0.00 | 12 |
| stroke 147 | 38 % → 0 % | 143.3 px | 0.00 | 0.00 | 9 |
| stroke 148 | 12 % → 0 % | 39.3 px | 0.00 | 0.00 | 14 |
| stroke 149 | 10 % → 1 % | 39.8 px | 0.18 | 0.08 | 10 |
| stroke 150 | 18 % → 6 % | 44.6 px | 0.17 | 0.36 | 35 |
| stroke 151 | 30 % → 1 % | 83.5 px | 0.18 | 0.02 | 26 |
| stroke 152 | 32 % → 2 % | 81.3 px | 0.18 | 0.05 | 40 |
| stroke 153 | 23 % → 0 % | 88.8 px | 0.00 | 0.00 | 13 |
| stroke 154 | 30 % → 0 % | 78.6 px | 0.00 | 0.00 | 34 |
| stroke 155 | 44 % → 0 % | 174.4 px | 0.00 | 0.00 | 14 |
| stroke 156 | 25 % → 0 % | 85.5 px | 0.00 | 0.00 | 22 |
| stroke 157 | 41 % → 0 % | 101.8 px | 0.00 | 0.00 | 42 |
| stroke 158 | 43 % → 0 % | 177.4 px | 0.00 | 0.00 | 11 |
| stroke 159 | 49 % → 0 % | 131.3 px | 0.00 | 0.00 | 38 |
| stroke 160 | 23 % → 3 % | 87.3 px | 0.18 | 0.12 | 15 |
| stroke 161 | 47 % → 0 % | 124.2 px | 0.00 | 0.00 | 32 |
| stroke 162 | 28 % → 0 % | 93.7 px | 0.19 | 0.01 | 28 |
| stroke 163 | 40 % → 0 % | 99.3 px | 0.00 | 0.00 | 71 |
| stroke 164 | 45 % → 0 % | 116.1 px | 0.00 | 0.00 | 42 |
| stroke 165 | 36 % → 0 % | 96.3 px | 0.00 | 0.00 | 30 |
| stroke 166 | 50 % → 0 % | 169.4 px | 0.00 | 0.00 | 16 |
| stroke 167 | 18 % → 0 % | 73.1 px | 0.00 | 0.00 | 13 |
| stroke 168 | 48 % → 0 % | 126.4 px | 0.00 | 0.00 | 28 |
| stroke 169 | 46 % → 0 % | 138.9 px | 0.00 | 0.00 | 20 |
| stroke 170 | 32 % → 0 % | 99.0 px | 0.00 | 0.00 | 21 |
| stroke 171 | 8 % → 0 % | 21.9 px | 0.00 | 0.00 | 19 |
| stroke 172 | 10 % → 0 % | 24.5 px | 0.00 | 0.00 | 48 |
| stroke 173 | 28 % → 0 % | 130.9 px | 0.00 | 0.00 | 9 |
| stroke 174 | 16 % → 0 % | 76.9 px | 0.00 | 0.00 | 8 |
| stroke 175 | 10 % → 0 % | 51.2 px | 0.00 | 0.00 | 5 |
| stroke 176 | 11 % → 0 % | 54.5 px | 0.00 | 0.00 | 5 |
| stroke 177 | 12 % → 0 % | 54.5 px | 0.00 | 0.00 | 10 |
| stroke 178 | 11 % → 0 % | 49.0 px | 0.00 | 0.00 | 13 |
| stroke 179 | 14 % → 0 % | 66.2 px | 0.00 | 0.00 | 10 |
| stroke 180 | 16 % → 0 % | 80.6 px | 0.00 | 0.00 | 8 |
| stroke 181 | 17 % → 0 % | 81.9 px | 0.00 | 0.00 | 10 |
| stroke 182 | 19 % → 0 % | 108.7 px | 0.00 | 0.00 | 9 |
| stroke 183 | 19 % → 0 % | 58.2 px | 0.00 | 0.00 | 20 |
| stroke 184 | 23 % → 0 % | 64.3 px | 0.00 | 0.00 | 21 |
| stroke 185 | 28 % → 0 % | 79.2 px | 0.00 | 0.00 | 23 |
| stroke 186 | 30 % → 0 % | 81.0 px | 0.00 | 0.00 | 25 |
| stroke 187 | 24 % → 0 % | 87.0 px | 0.00 | 0.00 | 15 |
| stroke 188 | 13 % → 0 % | 60.7 px | 0.00 | 0.00 | 8 |
| stroke 189 | 16 % → 0 % | 55.1 px | 0.00 | 0.00 | 21 |
| stroke 190 | 18 % → 0 % | 62.8 px | 0.00 | 0.00 | 14 |
| stroke 191 | 20 % → 0 % | 68.5 px | 0.00 | 0.00 | 41 |
| stroke 192 | 24 % → 0 % | 108.8 px | 0.00 | 0.00 | 9 |
| stroke 193 | 22 % → 0 % | 81.3 px | 0.00 | 0.00 | 18 |
| stroke 194 | 7 % → 0 % | 23.1 px | 0.00 | 0.00 | 19 |
| stroke 195 | 15 % → 0 % | 37.2 px | 0.00 | 0.00 | 53 |
| stroke 196 | 26 % → 0 % | 97.5 px | 0.00 | 0.00 | 17 |
| stroke 197 | 18 % → 0 % | 46.2 px | 0.00 | 0.00 | 51 |
| stroke 198 | 20 % → 0 % | 66.2 px | 0.00 | 0.00 | 23 |
| stroke 199 | 23 % → 0 % | 63.2 px | 0.00 | 0.00 | 40 |
| stroke 200 | 38 % → 0 % | 163.7 px | 0.00 | 0.00 | 15 |
| stroke 201 | 29 % → 0 % | 126.5 px | 0.00 | 0.00 | 12 |
| stroke 202 | 39 % → 0 % | 196.3 px | 0.00 | 0.00 | 12 |
| stroke 203 | 5 % → 0 % | 21.6 px | 0.00 | 0.00 | 13 |
| stroke 204 | 10 % → 0 % | 47.6 px | 0.00 | 0.00 | 16 |
| stroke 205 | 6 % → 0 % | 31.1 px | 0.00 | 0.00 | 7 |
| stroke 206 | 11 % → 0 % | 49.5 px | 0.00 | 0.00 | 13 |
| stroke 207 | 15 % → 0 % | 59.2 px | 0.00 | 0.00 | 45 |
| stroke 208 | 10 % → 0 % | 42.5 px | 0.00 | 0.00 | 19 |
| stroke 209 | 13 % → 0 % | 55.8 px | 0.00 | 0.00 | 20 |
| stroke 210 | 11 % → 0 % | 32.6 px | 0.00 | 0.00 | 33 |
| stroke 211 | 12 % → 0 % | 40.3 px | 0.00 | 0.00 | 44 |
| stroke 212 | 5 % → 15 % | 27.3 px | 0.16 | 3.07 | 13 |
| stroke 213 | 11 % → 15 % | 31.4 px | 0.16 | 1.34 | 15 |
| stroke 214 | 16 % → 5 % | 41.1 px | 0.17 | 0.34 | 57 |
| stroke 215 | 8 % → 11 % | 32.2 px | 0.13 | 1.40 | 18 |
| stroke 216 | 13 % → 17 % | 27.3 px | 0.15 | 1.35 | 64 |
| stroke 217 | 12 % → 15 % | 24.2 px | 0.16 | 1.22 | 49 |

Numbers say: wet paint spreads well beyond the stroke.

## Refs v3 · #38 Sanguine drawing — own sheet
own sheet 800 × 1092 · Charcoal 0.50 · Pastel 0.50 · 13 px · 49.2 s

![Refs v3 · #38 Sanguine drawing — own sheet](Refs-v3-38-Sanguine-drawing-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 7 % → 33 % | 14.6 px | 0.52 | 4.71 | 11 |
| stroke 2 | 11 % → 35 % | 19.1 px | 0.52 | 3.14 | 8 |
| stroke 3 | 21 % → 29 % | 37.3 px | 0.52 | 1.40 | 34 |
| stroke 4 | 30 % → 25 % | 76.0 px | 0.52 | 0.81 | 37 |
| stroke 5 | 14 % → 21 % | 25.7 px | 0.52 | 1.53 | 9 |
| stroke 6 | 14 % → 27 % | 25.4 px | 0.52 | 1.90 | 16 |
| stroke 7 | 16 % → 39 % | 28.4 px | 0.52 | 2.42 | 25 |
| stroke 8 | 14 % → 39 % | 27.0 px | 0.52 | 2.72 | 13 |
| stroke 9 | 14 % → 47 % | 28.8 px | 0.52 | 3.36 | 11 |
| stroke 10 | 8 % → 31 % | 12.6 px | 0.53 | 3.89 | 13 |
| stroke 11 | 7 % → 61 % | 11.5 px | 0.53 | 8.29 | 16 |
| stroke 12 | 6 % → 43 % | 12.0 px | 0.53 | 7.18 | 3 |
| stroke 13 | 7 % → 38 % | 12.3 px | 0.52 | 5.39 | 14 |
| stroke 14 | 15 % → 34 % | 47.2 px | 0.52 | 2.29 | 2 |
| stroke 15 | 19 % → 36 % | 30.0 px | 0.52 | 1.91 | 24 |
| stroke 16 | 34 % → 27 % | 68.5 px | 0.52 | 0.79 | 77 |
| stroke 17 | 5 % → 6 % | 16.0 px | 0.52 | 1.16 | 3 |
| stroke 18 | 11 % → 18 % | 21.5 px | 0.52 | 1.62 | 4 |
| stroke 19 | 17 % → 33 % | 42.9 px | 0.53 | 1.95 | 3 |
| stroke 20 | 11 % → 50 % | 32.0 px | 0.53 | 4.51 | 1 |
| stroke 21 | 17 % → 56 % | 48.0 px | 0.53 | 3.30 | 3 |
| stroke 22 | 5 % → 67 % | 16.0 px | 0.53 | 12.56 | 20 |
| stroke 23 | 7 % → 44 % | 12.8 px | 0.53 | 6.61 | 53 |
| stroke 24 | 12 % → 40 % | 19.9 px | 0.52 | 3.31 | 6 |
| stroke 25 | 7 % → 8 % | 22.4 px | 0.52 | 1.12 | 1 |
| stroke 26 | 21 % → 25 % | 39.5 px | 0.52 | 1.22 | 17 |
| stroke 27 | 11 % → 1 % | 31.1 px | 0.50 | 0.08 | 24 |
| stroke 28 | 10 % → 17 % | 25.5 px | 0.53 | 1.65 | 3 |
| stroke 29 | 8 % → 26 % | 16.0 px | 0.52 | 3.16 | 3 |
| stroke 30 | 18 % → 30 % | 33.6 px | 0.53 | 1.61 | 3 |
| stroke 31 | 12 % → 27 % | 29.9 px | 0.52 | 2.26 | 4 |
| stroke 32 | 8 % → 50 % | 21.0 px | 0.53 | 6.65 | 1 |
| stroke 33 | 14 % → 31 % | 28.5 px | 0.52 | 2.24 | 13 |
| stroke 34 | 6 % → 28 % | 16.5 px | 0.52 | 4.66 | 1 |
| stroke 35 | 10 % → 20 % | 12.7 px | 0.52 | 2.03 | 21 |
| stroke 36 | 21 % → 14 % | 23.5 px | 0.52 | 0.65 | 10 |
| stroke 37 | 11 % → 14 % | 28.1 px | 0.53 | 1.29 | 7 |
| stroke 38 | 28 % → 3 % | 65.5 px | 0.52 | 0.12 | 1 |
| stroke 39 | 20 % → 24 % | 45.9 px | 0.52 | 1.17 | 2 |
| stroke 40 | 6 % → 31 % | 15.3 px | 0.52 | 4.78 | 1 |
| stroke 41 | 18 % → 16 % | 31.0 px | 0.53 | 0.85 | 4 |
| stroke 42 | 13 % → 38 % | 22.1 px | 0.53 | 2.88 | 3 |
| stroke 43 | 21 % → 28 % | 29.8 px | 0.53 | 1.32 | 3 |
| stroke 44 | 8 % → 25 % | 19.0 px | 0.52 | 3.01 | 1 |
| stroke 45 | 21 % → 22 % | 35.7 px | 0.52 | 1.03 | 4 |
| stroke 46 | 20 % → 37 % | 25.0 px | 0.52 | 1.83 | 8 |
| stroke 47 | 22 % → 7 % | 48.6 px | 0.51 | 0.32 | 2 |
| stroke 48 | 24 % → 42 % | 36.4 px | 0.52 | 1.73 | 5 |
| stroke 49 | 17 % → 20 % | 21.7 px | 0.52 | 1.14 | 4 |
| stroke 50 | 23 % → 30 % | 22.7 px | 0.52 | 1.28 | 14 |
| stroke 51 | 26 % → 36 % | 33.8 px | 0.52 | 1.41 | 3 |
| stroke 52 | 32 % → 23 % | 45.1 px | 0.52 | 0.73 | 6 |
| stroke 53 | 24 % → 39 % | 38.8 px | 0.52 | 1.63 | 6 |
| stroke 54 | 8 % → 43 % | 13.8 px | 0.53 | 5.32 | 12 |
| stroke 55 | 18 % → 44 % | 58.7 px | 0.53 | 2.42 | 0 |
| stroke 56 | 19 % → 37 % | 54.0 px | 0.52 | 1.97 | 7 |
| stroke 57 | 11 % → 44 % | 19.6 px | 0.52 | 4.09 | 37 |
| stroke 58 | 12 % → 36 % | 21.8 px | 0.52 | 2.90 | 5 |
| stroke 59 | 17 % → 39 % | 30.7 px | 0.53 | 2.34 | 12 |
| stroke 60 | 25 % → 38 % | 54.2 px | 0.52 | 1.50 | 3 |
| stroke 61 | 23 % → 42 % | 74.8 px | 0.53 | 1.81 | 1 |
| stroke 62 | 10 % → 47 % | 32.3 px | 0.53 | 4.63 | 2 |
| stroke 63 | 7 % → 30 % | 12.5 px | 0.52 | 4.52 | 4 |
| stroke 64 | 9 % → 57 % | 23.7 px | 0.53 | 6.13 | 2 |
| stroke 65 | 5 % → 7 % | 15.3 px | 0.52 | 1.35 | 1 |
| stroke 66 | 10 % → 13 % | 31.6 px | 0.53 | 1.32 | 2 |
| stroke 67 | 11 % → 27 % | 31.9 px | 0.52 | 2.48 | 1 |
| stroke 68 | 5 % → 38 % | 14.3 px | 0.53 | 7.32 | 6 |
| stroke 69 | 10 % → 44 % | 17.4 px | 0.53 | 4.25 | 3 |
| stroke 70 | 8 % → 38 % | 20.2 px | 0.53 | 4.63 | 2 |
| stroke 71 | 10 % → 41 % | 15.9 px | 0.52 | 4.07 | 4 |
| stroke 72 | 14 % → 41 % | 18.2 px | 0.52 | 2.95 | 8 |
| stroke 73 | 13 % → 31 % | 19.1 px | 0.52 | 2.40 | 3 |
| stroke 74 | 17 % → 23 % | 23.1 px | 0.52 | 1.35 | 7 |
| stroke 75 | 19 % → 27 % | 36.8 px | 0.52 | 1.40 | 3 |
| stroke 76 | 12 % → 30 % | 19.8 px | 0.52 | 2.61 | 6 |
| stroke 77 | 10 % → 33 % | 33.8 px | 0.52 | 3.35 | 0 |
| stroke 78 | 21 % → 28 % | 41.1 px | 0.52 | 1.37 | 4 |
| stroke 79 | 14 % → 45 % | 43.2 px | 0.53 | 3.22 | 1 |
| stroke 80 | 7 % → 24 % | 13.7 px | 0.52 | 3.24 | 4 |
| stroke 81 | 20 % → 27 % | 35.4 px | 0.52 | 1.36 | 7 |
| stroke 82 | 16 % → 25 % | 41.4 px | 0.52 | 1.57 | 1 |
| stroke 83 | 16 % → 23 % | 29.0 px | 0.52 | 1.46 | 4 |
| stroke 84 | 25 % → 20 % | 60.2 px | 0.52 | 0.81 | 2 |
| stroke 85 | 14 % → 34 % | 49.3 px | 0.53 | 2.34 | 1 |
| stroke 86 | 19 % → 18 % | 33.3 px | 0.52 | 0.94 | 6 |
| stroke 87 | 10 % → 44 % | 25.7 px | 0.53 | 4.35 | 2 |
| stroke 88 | 20 % → 21 % | 53.4 px | 0.52 | 1.04 | 1 |
| stroke 89 | 12 % → 33 % | 29.6 px | 0.53 | 2.82 | 3 |
| stroke 90 | 10 % → 38 % | 29.9 px | 0.52 | 4.01 | 2 |
| stroke 91 | 24 % → 10 % | 41.2 px | 0.52 | 0.42 | 3 |
| stroke 92 | 14 % → 25 % | 24.9 px | 0.52 | 1.74 | 11 |
| stroke 93 | 13 % → 35 % | 25.2 px | 0.53 | 2.80 | 3 |
| stroke 94 | 20 % → 23 % | 42.3 px | 0.52 | 1.19 | 1 |
| stroke 95 | 21 % → 28 % | 35.9 px | 0.53 | 1.38 | 3 |
| stroke 96 | 16 % → 37 % | 30.0 px | 0.52 | 2.26 | 5 |
| stroke 97 | 30 % → 4 % | 54.0 px | 0.52 | 0.14 | 3 |
| stroke 98 | 19 % → 20 % | 63.0 px | 0.52 | 1.03 | 0 |
| stroke 99 | 16 % → 35 % | 28.2 px | 0.53 | 2.19 | 7 |
| stroke 100 | 24 % → 27 % | 44.0 px | 0.52 | 1.14 | 6 |
| stroke 101 | 23 % → 34 % | 58.6 px | 0.52 | 1.48 | 1 |
| stroke 102 | 26 % → 21 % | 47.6 px | 0.52 | 0.82 | 17 |
| stroke 103 | 19 % → 12 % | 57.0 px | 0.52 | 0.63 | 1 |
| stroke 104 | 7 % → 47 % | 15.0 px | 0.53 | 6.35 | 4 |
| stroke 105 | 24 % → 29 % | 42.9 px | 0.53 | 1.22 | 14 |
| stroke 106 | 24 % → 37 % | 46.2 px | 0.53 | 1.56 | 7 |
| stroke 107 | 32 % → 14 % | 57.6 px | 0.52 | 0.43 | 37 |
| stroke 108 | 19 % → 10 % | 33.0 px | 0.52 | 0.55 | 9 |
| stroke 109 | 7 % → 26 % | 23.4 px | 0.52 | 3.49 | 5 |
| stroke 110 | 5 % → 41 % | 14.5 px | 0.53 | 8.42 | 1 |
| stroke 111 | 16 % → 42 % | 28.5 px | 0.53 | 2.60 | 5 |
| stroke 112 | 18 % → 27 % | 47.6 px | 0.53 | 1.51 | 2 |
| stroke 113 | 20 % → 37 % | 40.6 px | 0.53 | 1.85 | 2 |
| stroke 114 | 25 % → 6 % | 78.9 px | 0.53 | 0.24 | 1 |
| stroke 115 | 23 % → 8 % | 40.4 px | 0.52 | 0.34 | 9 |
| stroke 116 | 12 % → 25 % | 20.7 px | 0.53 | 2.15 | 5 |
| stroke 117 | 16 % → 24 % | 40.7 px | 0.53 | 1.45 | 6 |
| stroke 118 | 22 % → 12 % | 44.4 px | 0.52 | 0.56 | 4 |
| stroke 119 | 13 % → 31 % | 30.2 px | 0.53 | 2.51 | 1 |
| stroke 120 | 19 % → 17 % | 37.5 px | 0.52 | 0.93 | 4 |
| stroke 121 | 14 % → 27 % | 25.2 px | 0.52 | 1.86 | 5 |
| stroke 122 | 11 % → 2 % | 29.3 px | 0.52 | 0.17 | 2 |
| stroke 123 | 16 % → 33 % | 40.0 px | 0.53 | 2.10 | 1 |
| stroke 124 | 18 % → 27 % | 33.2 px | 0.52 | 1.48 | 14 |
| stroke 125 | 8 % → 9 % | 20.7 px | 0.52 | 1.13 | 2 |
| stroke 126 | 18 % → 7 % | 32.4 px | 0.52 | 0.41 | 5 |
| stroke 127 | 15 % → 44 % | 30.1 px | 0.53 | 3.04 | 2 |
| stroke 128 | 21 % → 27 % | 37.0 px | 0.53 | 1.28 | 6 |
| stroke 129 | 29 % → 25 % | 74.5 px | 0.52 | 0.87 | 3 |
| stroke 130 | 6 % → 40 % | 17.0 px | 0.53 | 6.47 | 1 |
| stroke 131 | 12 % → 15 % | 21.7 px | 0.52 | 1.28 | 4 |
| stroke 132 | 18 % → 7 % | 54.1 px | 0.52 | 0.37 | 0 |
| stroke 133 | 15 % → 16 % | 45.7 px | 0.53 | 1.03 | 1 |
| stroke 134 | 19 % → 35 % | 51.0 px | 0.52 | 1.87 | 2 |
| stroke 135 | 26 % → 25 % | 66.5 px | 0.53 | 0.96 | 3 |
| stroke 136 | 22 % → 25 % | 60.9 px | 0.52 | 1.13 | 2 |
| stroke 137 | 11 % → 33 % | 32.7 px | 0.53 | 3.06 | 1 |
| stroke 138 | 16 % → 26 % | 28.4 px | 0.52 | 1.62 | 4 |
| stroke 139 | 16 % → 9 % | 33.0 px | 0.52 | 0.58 | 2 |
| stroke 140 | 18 % → 34 % | 38.3 px | 0.53 | 1.85 | 2 |
| stroke 141 | 18 % → 19 % | 37.6 px | 0.52 | 1.06 | 2 |
| stroke 142 | 11 % → 19 % | 29.9 px | 0.53 | 1.76 | 2 |
| stroke 143 | 16 % → 29 % | 30.2 px | 0.52 | 1.78 | 16 |
| stroke 144 | 22 % → 9 % | 43.7 px | 0.52 | 0.41 | 2 |
| stroke 145 | 16 % → 23 % | 34.0 px | 0.52 | 1.43 | 3 |
| stroke 146 | 16 % → 22 % | 27.7 px | 0.52 | 1.40 | 8 |
| stroke 147 | 19 % → 37 % | 44.8 px | 0.52 | 1.96 | 2 |
| stroke 148 | 23 % → 9 % | 41.5 px | 0.51 | 0.39 | 5 |
| stroke 149 | 8 % → 38 % | 15.1 px | 0.52 | 4.75 | 5 |
| stroke 150 | 16 % → 24 % | 32.6 px | 0.52 | 1.53 | 19 |
| stroke 151 | 22 % → 8 % | 32.7 px | 0.51 | 0.37 | 8 |
| stroke 152 | 15 % → 26 % | 30.8 px | 0.52 | 1.68 | 2 |
| stroke 153 | 20 % → 23 % | 70.5 px | 0.53 | 1.14 | 1 |
| stroke 154 | 27 % → 20 % | 59.0 px | 0.51 | 0.73 | 3 |
| stroke 155 | 22 % → 14 % | 68.2 px | 0.50 | 0.65 | 1 |
| stroke 156 | 37 % → 0 % | 66.6 px | 0.00 | 0.00 | 3 |
| stroke 157 | 19 % → 19 % | 38.0 px | 0.52 | 1.02 | 2 |
| stroke 158 | 21 % → 21 % | 43.9 px | 0.52 | 1.03 | 3 |
| stroke 159 | 17 % → 20 % | 29.8 px | 0.53 | 1.17 | 6 |
| stroke 160 | 11 % → 21 % | 29.5 px | 0.52 | 1.93 | 1 |
| stroke 161 | 17 % → 20 % | 54.1 px | 0.53 | 1.13 | 0 |
| stroke 162 | 9 % → 33 % | 27.7 px | 0.53 | 3.74 | 0 |
| stroke 163 | 17 % → 21 % | 31.7 px | 0.52 | 1.23 | 14 |
| stroke 164 | 23 % → 16 % | 41.2 px | 0.52 | 0.68 | 7 |
| stroke 165 | 12 % → 5 % | 31.1 px | 0.51 | 0.38 | 2 |
| stroke 166 | 27 % → 23 % | 47.9 px | 0.52 | 0.85 | 12 |
| stroke 167 | 11 % → 4 % | 27.9 px | 0.51 | 0.32 | 1 |
| stroke 168 | 34 % → 21 % | 48.9 px | 0.52 | 0.62 | 9 |
| stroke 169 | 15 % → 3 % | 26.7 px | 0.51 | 0.18 | 7 |
| stroke 170 | 40 % → 18 % | 73.2 px | 0.53 | 0.44 | 1 |
| stroke 171 | 17 % → 3 % | 34.7 px | 0.52 | 0.16 | 2 |
| stroke 172 | 7 % → 25 % | 13.7 px | 0.52 | 3.82 | 7 |
| stroke 173 | 12 % → 19 % | 24.4 px | 0.52 | 1.51 | 3 |
| stroke 174 | 20 % → 12 % | 39.4 px | 0.52 | 0.62 | 4 |
| stroke 175 | 22 % → 14 % | 50.5 px | 0.52 | 0.62 | 1 |
| stroke 176 | 7 % → 58 % | 14.4 px | 0.53 | 8.50 | 3 |
| stroke 177 | 8 % → 44 % | 19.0 px | 0.52 | 5.65 | 2 |
| stroke 178 | 10 % → 36 % | 15.4 px | 0.52 | 3.70 | 4 |
| stroke 179 | 5 % → 20 % | 13.8 px | 0.53 | 3.75 | 2 |
| stroke 180 | 12 % → 25 % | 28.2 px | 0.53 | 2.04 | 1 |
| stroke 181 | 11 % → 18 % | 32.7 px | 0.52 | 1.67 | 1 |
| stroke 182 | 10 % → 2 % | 18.3 px | 0.51 | 0.25 | 3 |
| stroke 183 | 14 % → 32 % | 26.0 px | 0.53 | 2.24 | 15 |
| stroke 184 | 8 % → 52 % | 13.8 px | 0.53 | 6.25 | 11 |
| stroke 185 | 11 % → 31 % | 20.1 px | 0.52 | 2.84 | 5 |
| stroke 186 | 12 % → 62 % | 23.1 px | 0.53 | 5.33 | 1 |
| stroke 187 | 12 % → 48 % | 21.9 px | 0.52 | 4.10 | 2 |
| stroke 188 | 15 % → 58 % | 24.8 px | 0.53 | 3.93 | 4 |
| stroke 189 | 6 % → 38 % | 22.4 px | 0.51 | 5.96 | 12 |
| stroke 190 | 11 % → 29 % | 25.9 px | 0.51 | 2.64 | 28 |
| stroke 191 | 11 % → 22 % | 28.2 px | 0.51 | 1.92 | 3 |
| stroke 192 | 16 % → 14 % | 33.7 px | 0.51 | 0.90 | 3 |
| stroke 193 | 16 % → 12 % | 28.5 px | 0.51 | 0.76 | 7 |
| stroke 194 | 9 % → 0 % | 19.9 px | 0.00 | 0.00 | 6 |
| stroke 195 | 26 % → 21 % | 63.6 px | 0.51 | 0.81 | 1 |
| stroke 196 | 23 % → 1 % | 61.7 px | 0.49 | 0.06 | 1 |
| stroke 197 | 14 % → 2 % | 28.7 px | 0.50 | 0.11 | 2 |
| stroke 198 | 18 % → 4 % | 32.6 px | 0.52 | 0.21 | 6 |
| stroke 199 | 24 % → 5 % | 47.5 px | 0.52 | 0.20 | 2 |
| stroke 200 | 26 % → 8 % | 67.5 px | 0.52 | 0.30 | 2 |
| stroke 201 | 21 % → 8 % | 40.2 px | 0.52 | 0.36 | 9 |
| stroke 202 | 20 % → 8 % | 33.3 px | 0.52 | 0.42 | 19 |
| stroke 203 | 11 % → 10 % | 29.9 px | 0.52 | 0.90 | 1 |
| stroke 204 | 15 % → 9 % | 27.3 px | 0.52 | 0.61 | 16 |
| stroke 205 | 10 % → 33 % | 29.4 px | 0.51 | 3.26 | 0 |
| stroke 206 | 6 % → 27 % | 17.3 px | 0.51 | 4.34 | 4 |
| stroke 207 | 11 % → 37 % | 26.8 px | 0.51 | 3.46 | 1 |
| stroke 208 | 15 % → 31 % | 42.2 px | 0.51 | 2.09 | 1 |
| stroke 209 | 16 % → 40 % | 38.2 px | 0.51 | 2.50 | 2 |
| stroke 210 | 11 % → 54 % | 36.6 px | 0.52 | 4.82 | 1 |
| stroke 211 | 7 % → 4 % | 14.3 px | 0.51 | 0.62 | 3 |
| stroke 212 | 10 % → 45 % | 12.9 px | 0.53 | 4.39 | 6 |
| stroke 213 | 15 % → 45 % | 17.4 px | 0.53 | 3.08 | 7 |
| stroke 214 | 17 % → 41 % | 21.7 px | 0.53 | 2.46 | 26 |
| stroke 215 | 18 % → 39 % | 26.9 px | 0.53 | 2.10 | 29 |
| stroke 216 | 20 % → 37 % | 33.5 px | 0.53 | 1.85 | 92 |
| stroke 217 | 25 % → 47 % | 34.7 px | 0.53 | 1.83 | 70 |
| stroke 218 | 25 % → 46 % | 38.4 px | 0.53 | 1.84 | 40 |
| stroke 219 | 24 % → 47 % | 34.8 px | 0.53 | 1.96 | 6 |
| stroke 220 | 22 % → 47 % | 35.4 px | 0.53 | 2.08 | 14 |
| stroke 221 | 25 % → 49 % | 38.8 px | 0.53 | 1.92 | 20 |
| stroke 222 | 19 % → 47 % | 30.6 px | 0.53 | 2.50 | 27 |
| stroke 223 | 9 % → 23 % | 23.4 px | 0.52 | 2.61 | 2 |
| stroke 224 | 27 % → 50 % | 42.4 px | 0.53 | 1.84 | 13 |
| stroke 225 | 17 % → 41 % | 31.2 px | 0.53 | 2.38 | 45 |
| stroke 226 | 28 % → 51 % | 44.3 px | 0.53 | 1.82 | 28 |
| stroke 227 | 25 % → 49 % | 43.2 px | 0.53 | 1.99 | 30 |
| stroke 228 | 20 % → 26 % | 52.5 px | 0.52 | 1.28 | 6 |
| stroke 229 | 30 % → 53 % | 47.1 px | 0.53 | 1.79 | 7 |
| stroke 230 | 27 % → 48 % | 47.0 px | 0.53 | 1.79 | 20 |
| stroke 231 | 20 % → 21 % | 48.5 px | 0.52 | 1.08 | 3 |
| stroke 232 | 30 % → 53 % | 46.8 px | 0.53 | 1.77 | 27 |
| stroke 233 | 26 % → 43 % | 49.2 px | 0.53 | 1.68 | 43 |
| stroke 234 | 30 % → 52 % | 48.1 px | 0.53 | 1.71 | 27 |
| stroke 235 | 30 % → 45 % | 54.3 px | 0.53 | 1.53 | 47 |
| stroke 236 | 26 % → 28 % | 74.0 px | 0.52 | 1.11 | 2 |
| stroke 237 | 31 % → 51 % | 48.3 px | 0.53 | 1.64 | 21 |
| stroke 238 | 29 % → 43 % | 51.3 px | 0.53 | 1.47 | 24 |
| stroke 239 | 28 % → 43 % | 68.4 px | 0.52 | 1.56 | 2 |
| stroke 240 | 31 % → 52 % | 47.4 px | 0.53 | 1.69 | 10 |
| stroke 241 | 15 % → 28 % | 40.1 px | 0.52 | 1.85 | 6 |
| stroke 242 | 35 % → 43 % | 55.2 px | 0.53 | 1.25 | 35 |
| stroke 243 | 23 % → 40 % | 42.6 px | 0.52 | 1.79 | 7 |
| stroke 244 | 30 % → 52 % | 46.0 px | 0.53 | 1.76 | 15 |
| stroke 245 | 16 % → 24 % | 35.7 px | 0.52 | 1.53 | 3 |
| stroke 246 | 32 % → 47 % | 58.9 px | 0.53 | 1.47 | 4 |
| stroke 247 | 15 % → 29 % | 23.6 px | 0.52 | 1.88 | 10 |
| stroke 248 | 26 % → 49 % | 42.9 px | 0.53 | 1.87 | 13 |
| stroke 249 | 25 % → 34 % | 45.5 px | 0.53 | 1.39 | 9 |
| stroke 250 | 18 % → 31 % | 28.2 px | 0.52 | 1.69 | 17 |
| stroke 251 | 28 % → 52 % | 44.2 px | 0.53 | 1.86 | 11 |
| stroke 252 | 22 % → 27 % | 34.1 px | 0.52 | 1.24 | 4 |
| stroke 253 | 26 % → 44 % | 43.2 px | 0.53 | 1.71 | 9 |
| stroke 254 | 28 % → 51 % | 45.0 px | 0.53 | 1.80 | 8 |
| stroke 255 | 11 % → 24 % | 25.3 px | 0.52 | 2.26 | 2 |
| stroke 256 | 6 % → 24 % | 20.8 px | 0.52 | 3.77 | 1 |
| stroke 257 | 22 % → 43 % | 33.3 px | 0.53 | 2.00 | 8 |
| stroke 258 | 24 % → 42 % | 41.2 px | 0.52 | 1.80 | 20 |
| stroke 259 | 7 % → 24 % | 13.1 px | 0.52 | 3.65 | 3 |
| stroke 260 | 12 % → 30 % | 21.2 px | 0.52 | 2.57 | 2 |
| stroke 261 | 22 % → 44 % | 34.4 px | 0.52 | 1.99 | 5 |
| stroke 262 | 27 % → 45 % | 44.6 px | 0.53 | 1.65 | 10 |
| stroke 263 | 12 % → 30 % | 19.2 px | 0.52 | 2.56 | 13 |
| stroke 264 | 16 % → 41 % | 25.0 px | 0.53 | 2.64 | 8 |
| stroke 265 | 27 % → 51 % | 42.2 px | 0.53 | 1.89 | 5 |
| stroke 266 | 33 % → 49 % | 51.8 px | 0.53 | 1.48 | 9 |
| stroke 267 | 24 % → 28 % | 37.9 px | 0.52 | 1.16 | 7 |
| stroke 268 | 21 % → 41 % | 33.7 px | 0.52 | 1.96 | 4 |
| stroke 269 | 21 % → 44 % | 35.7 px | 0.53 | 2.07 | 19 |
| stroke 270 | 31 % → 46 % | 46.8 px | 0.52 | 1.51 | 6 |
| stroke 271 | 24 % → 42 % | 37.8 px | 0.52 | 1.75 | 8 |
| stroke 272 | 24 % → 47 % | 36.9 px | 0.53 | 1.97 | 21 |
| stroke 273 | 18 % → 43 % | 28.7 px | 0.53 | 2.36 | 12 |
| stroke 274 | 28 % → 45 % | 43.2 px | 0.52 | 1.63 | 7 |
| stroke 275 | 26 % → 42 % | 42.6 px | 0.52 | 1.63 | 19 |
| stroke 276 | 23 % → 47 % | 37.9 px | 0.53 | 2.06 | 14 |
| stroke 277 | 24 % → 38 % | 59.5 px | 0.52 | 1.57 | 2 |
| stroke 278 | 22 % → 38 % | 35.2 px | 0.52 | 1.71 | 4 |
| stroke 279 | 27 % → 39 % | 43.8 px | 0.52 | 1.45 | 12 |
| stroke 280 | 25 % → 50 % | 40.1 px | 0.53 | 2.00 | 12 |
| stroke 281 | 17 % → 32 % | 46.4 px | 0.52 | 1.90 | 2 |
| stroke 282 | 21 % → 38 % | 34.5 px | 0.52 | 1.80 | 14 |
| stroke 283 | 29 % → 37 % | 45.4 px | 0.52 | 1.30 | 14 |
| stroke 284 | 29 % → 52 % | 47.0 px | 0.53 | 1.76 | 21 |
| stroke 285 | 15 % → 38 % | 21.0 px | 0.53 | 2.44 | 16 |
| stroke 286 | 15 % → 37 % | 45.2 px | 0.52 | 2.45 | 1 |
| stroke 287 | 28 % → 46 % | 58.2 px | 0.52 | 1.64 | 9 |
| stroke 288 | 16 % → 28 % | 29.5 px | 0.52 | 1.77 | 2 |
| stroke 289 | 24 % → 33 % | 63.7 px | 0.52 | 1.38 | 2 |
| stroke 290 | 28 % → 28 % | 70.7 px | 0.52 | 1.00 | 1 |
| stroke 291 | 31 % → 47 % | 49.0 px | 0.53 | 1.52 | 13 |
| stroke 292 | 20 % → 42 % | 27.0 px | 0.53 | 2.17 | 9 |
| stroke 293 | 22 % → 44 % | 36.5 px | 0.52 | 1.96 | 8 |
| stroke 294 | 15 % → 24 % | 24.7 px | 0.52 | 1.65 | 3 |
| stroke 295 | 20 % → 27 % | 38.2 px | 0.52 | 1.32 | 2 |
| stroke 296 | 32 % → 46 % | 49.3 px | 0.53 | 1.43 | 13 |
| stroke 297 | 24 % → 46 % | 34.8 px | 0.53 | 1.94 | 14 |
| stroke 298 | 22 % → 45 % | 34.9 px | 0.53 | 2.04 | 11 |
| stroke 299 | 16 % → 18 % | 26.3 px | 0.52 | 1.14 | 6 |
| stroke 300 | 16 % → 25 % | 33.0 px | 0.52 | 1.61 | 1 |
| stroke 301 | 30 % → 44 % | 47.0 px | 0.53 | 1.46 | 11 |
| stroke 302 | 28 % → 49 % | 39.6 px | 0.53 | 1.79 | 18 |
| stroke 303 | 22 % → 46 % | 34.1 px | 0.53 | 2.07 | 7 |
| stroke 304 | 14 % → 25 % | 34.9 px | 0.52 | 1.82 | 2 |
| stroke 305 | 26 % → 36 % | 40.3 px | 0.52 | 1.39 | 12 |
| stroke 306 | 16 % → 39 % | 26.2 px | 0.52 | 2.44 | 6 |
| stroke 307 | 30 % → 51 % | 42.2 px | 0.53 | 1.70 | 14 |
| stroke 308 | 22 % → 43 % | 33.9 px | 0.53 | 1.95 | 6 |
| stroke 309 | 14 % → 19 % | 22.2 px | 0.52 | 1.41 | 4 |
| stroke 310 | 15 % → 26 % | 27.7 px | 0.52 | 1.76 | 2 |
| stroke 311 | 27 % → 34 % | 45.3 px | 0.52 | 1.23 | 3 |
| stroke 312 | 19 % → 38 % | 30.0 px | 0.52 | 2.00 | 7 |
| stroke 313 | 31 % → 49 % | 44.2 px | 0.53 | 1.60 | 11 |
| stroke 314 | 28 % → 48 % | 43.3 px | 0.53 | 1.69 | 16 |
| stroke 315 | 19 % → 19 % | 50.2 px | 0.52 | 1.00 | 1 |
| stroke 316 | 15 % → 30 % | 25.8 px | 0.52 | 1.93 | 2 |
| stroke 317 | 20 % → 37 % | 31.7 px | 0.52 | 1.85 | 11 |
| stroke 318 | 30 % → 49 % | 41.5 px | 0.53 | 1.66 | 9 |
| stroke 319 | 30 % → 48 % | 45.3 px | 0.53 | 1.62 | 8 |
| stroke 320 | 20 % → 35 % | 32.1 px | 0.52 | 1.76 | 7 |
| stroke 321 | 11 % → 31 % | 35.3 px | 0.52 | 2.75 | 1 |
| stroke 322 | 27 % → 39 % | 46.5 px | 0.52 | 1.43 | 5 |
| stroke 323 | 29 % → 49 % | 40.5 px | 0.53 | 1.67 | 12 |
| stroke 324 | 26 % → 45 % | 41.7 px | 0.53 | 1.70 | 11 |
| stroke 325 | 5 % → 17 % | 14.4 px | 0.52 | 3.68 | 1 |
| stroke 326 | 23 % → 36 % | 34.8 px | 0.52 | 1.58 | 8 |
| stroke 327 | 18 % → 39 % | 29.4 px | 0.52 | 2.15 | 8 |
| stroke 328 | 25 % → 30 % | 42.4 px | 0.52 | 1.19 | 3 |
| stroke 329 | 28 % → 46 % | 38.7 px | 0.53 | 1.65 | 7 |
| stroke 330 | 27 % → 48 % | 42.3 px | 0.53 | 1.78 | 9 |
| stroke 331 | 10 % → 31 % | 19.9 px | 0.52 | 3.18 | 2 |
| stroke 332 | 5 % → 30 % | 16.4 px | 0.53 | 5.60 | 0 |
| stroke 333 | 19 % → 28 % | 30.4 px | 0.52 | 1.48 | 7 |
| stroke 334 | 27 % → 39 % | 40.7 px | 0.53 | 1.46 | 10 |
| stroke 335 | 28 % → 48 % | 37.3 px | 0.53 | 1.72 | 7 |
| stroke 336 | 23 % → 49 % | 36.3 px | 0.53 | 2.13 | 9 |
| stroke 337 | 18 % → 35 % | 28.5 px | 0.53 | 1.94 | 12 |
| stroke 338 | 26 % → 41 % | 47.6 px | 0.52 | 1.53 | 2 |
| stroke 339 | 28 % → 48 % | 38.5 px | 0.52 | 1.73 | 11 |
| stroke 340 | 20 % → 42 % | 40.7 px | 0.53 | 2.14 | 27 |
| stroke 341 | 24 % → 38 % | 37.7 px | 0.52 | 1.60 | 5 |
| stroke 342 | 29 % → 48 % | 40.3 px | 0.53 | 1.69 | 15 |
| stroke 343 | 24 % → 48 % | 43.2 px | 0.53 | 1.98 | 31 |
| stroke 344 | 25 % → 32 % | 46.0 px | 0.53 | 1.32 | 9 |
| stroke 345 | 22 % → 35 % | 61.1 px | 0.53 | 1.62 | 1 |
| stroke 346 | 21 % → 43 % | 36.8 px | 0.53 | 2.04 | 10 |
| stroke 347 | 29 % → 50 % | 40.3 px | 0.52 | 1.71 | 15 |
| stroke 348 | 30 % → 56 % | 47.1 px | 0.53 | 1.88 | 13 |
| stroke 349 | 31 % → 37 % | 104.3 px | 0.53 | 1.21 | 1 |
| stroke 350 | 25 % → 27 % | 44.1 px | 0.53 | 1.11 | 5 |
| stroke 351 | 8 % → 19 % | 19.2 px | 0.52 | 2.38 | 1 |
| stroke 352 | 15 % → 34 % | 23.8 px | 0.53 | 2.20 | 5 |
| stroke 353 | 28 % → 48 % | 38.2 px | 0.53 | 1.72 | 14 |
| stroke 354 | 31 % → 56 % | 48.5 px | 0.53 | 1.80 | 78 |
| stroke 355 | 21 % → 34 % | 33.2 px | 0.53 | 1.66 | 28 |
| stroke 356 | 13 % → 20 % | 20.8 px | 0.52 | 1.49 | 13 |
| stroke 357 | 29 % → 46 % | 41.4 px | 0.52 | 1.58 | 12 |
| stroke 358 | 29 % → 48 % | 50.9 px | 0.53 | 1.67 | 39 |
| stroke 359 | 29 % → 40 % | 45.6 px | 0.52 | 1.38 | 9 |
| stroke 360 | 16 % → 25 % | 27.4 px | 0.52 | 1.60 | 10 |
| stroke 361 | 28 % → 44 % | 38.5 px | 0.52 | 1.58 | 13 |
| stroke 362 | 35 % → 52 % | 53.8 px | 0.53 | 1.47 | 78 |
| stroke 363 | 17 % → 27 % | 33.5 px | 0.53 | 1.62 | 5 |
| stroke 364 | 16 % → 24 % | 27.5 px | 0.52 | 1.51 | 2 |
| stroke 365 | 17 % → 30 % | 25.9 px | 0.53 | 1.80 | 18 |
| stroke 366 | 23 % → 37 % | 72.2 px | 0.52 | 1.58 | 0 |
| stroke 367 | 26 % → 29 % | 44.0 px | 0.52 | 1.12 | 6 |
| stroke 368 | 17 % → 30 % | 30.4 px | 0.52 | 1.79 | 5 |
| stroke 369 | 23 % → 38 % | 60.9 px | 0.52 | 1.64 | 2 |
| stroke 370 | 27 % → 45 % | 39.2 px | 0.53 | 1.66 | 4 |
| stroke 371 | 38 % → 55 % | 53.4 px | 0.53 | 1.44 | 21 |
| stroke 372 | 20 % → 30 % | 38.3 px | 0.52 | 1.50 | 2 |
| stroke 373 | 20 % → 34 % | 63.5 px | 0.52 | 1.70 | 1 |
| stroke 374 | 22 % → 35 % | 33.4 px | 0.52 | 1.62 | 12 |
| stroke 375 | 22 % → 44 % | 31.7 px | 0.53 | 1.98 | 4 |
| stroke 376 | 35 % → 51 % | 50.9 px | 0.53 | 1.44 | 6 |
| stroke 377 | 31 % → 56 % | 50.1 px | 0.53 | 1.81 | 14 |
| stroke 378 | 14 % → 21 % | 23.3 px | 0.52 | 1.56 | 15 |
| stroke 379 | 20 % → 28 % | 38.3 px | 0.52 | 1.44 | 27 |
| stroke 380 | 16 % → 40 % | 39.6 px | 0.52 | 2.55 | 1 |
| stroke 381 | 23 % → 36 % | 36.1 px | 0.52 | 1.55 | 10 |
| stroke 382 | 23 % → 48 % | 31.9 px | 0.53 | 2.06 | 23 |
| stroke 383 | 28 % → 46 % | 44.3 px | 0.53 | 1.62 | 26 |
| stroke 384 | 20 % → 36 % | 32.8 px | 0.52 | 1.78 | 64 |
| stroke 385 | 27 % → 40 % | 47.1 px | 0.52 | 1.45 | 7 |
| stroke 386 | 17 % → 38 % | 32.6 px | 0.52 | 2.22 | 4 |
| stroke 387 | 26 % → 52 % | 34.9 px | 0.53 | 1.96 | 17 |
| stroke 388 | 27 % → 46 % | 42.4 px | 0.53 | 1.73 | 17 |
| stroke 389 | 22 % → 40 % | 33.6 px | 0.52 | 1.82 | 14 |
| stroke 390 | 26 % → 48 % | 60.4 px | 0.52 | 1.87 | 4 |
| stroke 391 | 26 % → 52 % | 36.3 px | 0.53 | 2.02 | 19 |
| stroke 392 | 22 % → 39 % | 36.3 px | 0.53 | 1.74 | 44 |
| stroke 393 | 10 % → 23 % | 16.9 px | 0.53 | 2.22 | 19 |
| stroke 394 | 18 % → 29 % | 28.5 px | 0.52 | 1.58 | 57 |
| stroke 395 | 24 % → 40 % | 38.7 px | 0.53 | 1.71 | 59 |
| stroke 396 | 30 % → 48 % | 46.9 px | 0.53 | 1.61 | 9 |
| stroke 397 | 17 % → 31 % | 28.6 px | 0.52 | 1.78 | 15 |
| stroke 398 | 10 % → 23 % | 23.6 px | 0.52 | 2.36 | 2 |
| stroke 399 | 30 % → 39 % | 47.4 px | 0.52 | 1.28 | 8 |
| stroke 400 | 26 % → 38 % | 41.6 px | 0.53 | 1.49 | 27 |
| stroke 401 | 30 % → 42 % | 42.2 px | 0.53 | 1.38 | 10 |
| stroke 402 | 16 % → 25 % | 24.5 px | 0.52 | 1.59 | 16 |
| stroke 403 | 27 % → 30 % | 40.7 px | 0.52 | 1.14 | 21 |
| stroke 404 | 25 % → 29 % | 62.8 px | 0.52 | 1.20 | 2 |
| stroke 405 | 30 % → 45 % | 43.7 px | 0.53 | 1.50 | 23 |
| stroke 406 | 30 % → 42 % | 46.3 px | 0.52 | 1.37 | 10 |
| stroke 407 | 23 % → 23 % | 41.9 px | 0.53 | 1.00 | 17 |
| stroke 408 | 24 % → 29 % | 80.3 px | 0.52 | 1.22 | 0 |
| stroke 409 | 20 % → 24 % | 34.1 px | 0.52 | 1.24 | 2 |
| stroke 410 | 32 % → 43 % | 48.7 px | 0.53 | 1.38 | 13 |
| stroke 411 | 28 % → 42 % | 52.5 px | 0.52 | 1.50 | 6 |
| stroke 412 | 29 % → 36 % | 44.4 px | 0.52 | 1.23 | 1 |
| stroke 413 | 31 % → 40 % | 47.2 px | 0.53 | 1.28 | 5 |
| stroke 414 | 20 % → 38 % | 36.9 px | 0.52 | 1.87 | 1 |
| stroke 415 | 24 % → 24 % | 42.1 px | 0.52 | 1.00 | 1 |
| stroke 416 | 13 % → 28 % | 22.8 px | 0.52 | 2.13 | 4 |
| stroke 417 | 29 % → 42 % | 48.0 px | 0.52 | 1.43 | 3 |
| stroke 418 | 22 % → 39 % | 39.1 px | 0.52 | 1.78 | 6 |
| stroke 419 | 15 % → 17 % | 22.8 px | 0.52 | 1.13 | 14 |
| stroke 420 | 23 % → 35 % | 44.4 px | 0.52 | 1.56 | 4 |
| stroke 421 | 24 % → 43 % | 37.2 px | 0.52 | 1.78 | 2 |
| stroke 422 | 18 % → 28 % | 34.9 px | 0.52 | 1.57 | 2 |
| stroke 423 | 21 % → 39 % | 42.0 px | 0.52 | 1.83 | 4 |
| stroke 424 | 27 % → 40 % | 41.7 px | 0.52 | 1.47 | 4 |
| stroke 425 | 14 % → 27 % | 23.0 px | 0.52 | 1.96 | 4 |
| stroke 426 | 30 % → 38 % | 38.2 px | 0.52 | 1.27 | 5 |
| stroke 427 | 14 % → 22 % | 18.9 px | 0.52 | 1.54 | 22 |
| stroke 428 | 31 % → 35 % | 40.4 px | 0.52 | 1.12 | 10 |
| stroke 429 | 23 % → 28 % | 32.1 px | 0.52 | 1.20 | 3 |
| stroke 430 | 30 % → 30 % | 59.4 px | 0.52 | 1.00 | 1 |
| stroke 431 | 30 % → 30 % | 47.7 px | 0.53 | 1.00 | 2 |
| stroke 432 | 6 % → 6 % | 20.3 px | 0.51 | 1.00 | 0 |
| stroke 433 | 7 % → 11 % | 14.1 px | 0.52 | 1.48 | 0 |
| stroke 434 | 7 % → 13 % | 15.2 px | 0.51 | 1.87 | 2 |
| stroke 435 | 13 % → 13 % | 33.2 px | 0.51 | 1.00 | 1 |
| stroke 436 | 10 % → 35 % | 30.5 px | 0.53 | 3.38 | 0 |
| stroke 437 | 9 % → 24 % | 14.1 px | 0.53 | 2.68 | 7 |
| stroke 438 | 14 % → 23 % | 22.9 px | 0.52 | 1.70 | 9 |
| stroke 439 | 26 % → 34 % | 42.4 px | 0.52 | 1.29 | 4 |
| stroke 440 | 15 % → 34 % | 9.6 px | 0.51 | 2.20 | 16 |
| stroke 441 | 25 % → 35 % | 20.9 px | 0.51 | 1.44 | 24 |
| stroke 442 | 31 % → 42 % | 27.2 px | 0.51 | 1.38 | 13 |
| stroke 443 | 27 % → 39 % | 28.7 px | 0.51 | 1.45 | 11 |
| stroke 444 | 24 % → 35 % | 66.7 px | 0.51 | 1.43 | 2 |
| stroke 445 | 7 % → 22 % | 15.2 px | 0.51 | 3.10 | 3 |
| stroke 446 | 24 % → 36 % | 29.7 px | 0.51 | 1.49 | 3 |
| stroke 447 | 16 % → 29 % | 27.7 px | 0.51 | 1.77 | 5 |
| stroke 448 | 22 % → 32 % | 25.8 px | 0.51 | 1.48 | 11 |
| stroke 449 | 11 % → 25 % | 23.7 px | 0.51 | 2.34 | 1 |
| stroke 450 | 16 % → 28 % | 25.5 px | 0.51 | 1.77 | 3 |
| stroke 451 | 21 % → 35 % | 31.8 px | 0.51 | 1.64 | 5 |
| stroke 452 | 18 % → 27 % | 20.4 px | 0.51 | 1.48 | 11 |
| stroke 453 | 25 % → 36 % | 26.9 px | 0.51 | 1.44 | 13 |
| stroke 454 | 15 % → 15 % | 40.0 px | 0.51 | 1.00 | 0 |
| stroke 455 | 25 % → 32 % | 27.7 px | 0.51 | 1.30 | 7 |
| stroke 456 | 25 % → 30 % | 33.1 px | 0.51 | 1.19 | 5 |
| stroke 457 | 13 % → 23 % | 24.6 px | 0.51 | 1.75 | 1 |
| stroke 458 | 14 % → 22 % | 23.4 px | 0.50 | 1.64 | 3 |
| stroke 459 | 15 % → 15 % | 15.8 px | 0.51 | 1.00 | 10 |
| stroke 460 | 8 % → 13 % | 15.2 px | 0.52 | 1.62 | 3 |
| stroke 461 | 12 % → 16 % | 28.5 px | 0.52 | 1.29 | 2 |
| stroke 462 | 10 % → 11 % | 22.0 px | 0.52 | 1.07 | 6 |
| stroke 463 | 9 % → 9 % | 18.1 px | 0.52 | 1.00 | 8 |
| stroke 464 | 7 % → 7 % | 12.5 px | 0.53 | 1.00 | 4 |

Numbers say: wet paint spreads well beyond the stroke.

## Refs v3 · #39 Thick impasto weave — own sheet
own sheet 800 × 1065 · Impasto 1.00 · 69 px · 39.2 s

![Refs v3 · #39 Thick impasto weave — own sheet](Refs-v3-39-Thick-impasto-weave-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 7 % → 0 % | 59.2 px | 0.00 | 0.00 | 99 |
| stroke 2 | 15 % → 0 % | 68.3 px | 0.19 | 0.02 | 468 |
| stroke 3 | 20 % → 0 % | 97.1 px | 0.19 | 0.01 | 782 |
| stroke 4 | 23 % → 1 % | 118.8 px | 0.19 | 0.03 | 923 |
| stroke 5 | 29 % → 0 % | 172.6 px | 0.20 | 0.01 | 455 |
| stroke 6 | 42 % → 0 % | 365.3 px | 0.19 | 0.01 | 198 |
| stroke 7 | 41 % → 0 % | 373.8 px | 0.19 | 0.01 | 184 |
| stroke 8 | 40 % → 0 % | 360.4 px | 0.19 | 0.01 | 190 |
| stroke 9 | 36 % → 0 % | 325.5 px | 0.18 | 0.01 | 177 |
| stroke 10 | 33 % → 2 % | 300.0 px | 0.18 | 0.06 | 363 |
| stroke 11 | 29 % → 2 % | 256.6 px | 0.17 | 0.05 | 308 |
| stroke 12 | 27 % → 2 % | 259.5 px | 0.17 | 0.06 | 223 |
| stroke 13 | 30 % → 2 % | 397.3 px | 0.17 | 0.07 | 93 |
| stroke 14 | 13 % → 0 % | 63.0 px | 0.13 | 0.00 | 396 |
| stroke 15 | 13 % → 0 % | 159.3 px | 0.14 | 0.00 | 61 |
| stroke 16 | 23 % → 1 % | 92.2 px | 0.19 | 0.03 | 628 |
| stroke 17 | 32 % → 1 % | 127.4 px | 0.19 | 0.02 | 556 |
| stroke 18 | 48 % → 1 % | 193.0 px | 0.19 | 0.02 | 359 |
| stroke 19 | 51 % → 1 % | 225.7 px | 0.19 | 0.03 | 231 |
| stroke 20 | 55 % → 1 % | 196.7 px | 0.19 | 0.02 | 360 |
| stroke 21 | 57 % → 1 % | 167.5 px | 0.19 | 0.02 | 469 |
| stroke 22 | 61 % → 1 % | 156.1 px | 0.19 | 0.02 | 841 |
| stroke 23 | 11 % → 0 % | 65.1 px | 0.00 | 0.00 | 251 |
| stroke 24 | 18 % → 0 % | 108.0 px | 0.00 | 0.00 | 213 |
| stroke 25 | 25 % → 0 % | 147.9 px | 0.00 | 0.00 | 184 |
| stroke 26 | 31 % → 0 % | 185.9 px | 0.00 | 0.00 | 192 |
| stroke 27 | 35 % → 0 % | 212.7 px | 0.20 | 0.01 | 176 |
| stroke 28 | 34 % → 3 % | 214.6 px | 0.18 | 0.09 | 172 |
| stroke 29 | 36 % → 3 % | 208.9 px | 0.18 | 0.09 | 204 |
| stroke 30 | 40 % → 4 % | 197.6 px | 0.18 | 0.09 | 234 |
| stroke 31 | 50 % → 5 % | 233.9 px | 0.18 | 0.10 | 232 |
| stroke 32 | 7 % → 1 % | 66.2 px | 0.20 | 0.11 | 241 |
| stroke 33 | 8 % → 0 % | 66.0 px | 0.00 | 0.00 | 167 |
| stroke 34 | 3 % → 0 % | 22.0 px | 0.00 | 0.00 | 41 |
| stroke 35 | 5 % → 2 % | 69.3 px | 0.17 | 0.49 | 84 |
| stroke 36 | 10 % → 2 % | 82.5 px | 0.17 | 0.16 | 369 |
| stroke 37 | 14 % → 1 % | 98.7 px | 0.17 | 0.09 | 711 |
| stroke 38 | 20 % → 1 % | 118.9 px | 0.18 | 0.06 | 856 |
| stroke 39 | 27 % → 1 % | 154.3 px | 0.18 | 0.05 | 440 |
| stroke 40 | 34 % → 1 % | 194.8 px | 0.18 | 0.04 | 419 |
| stroke 41 | 36 % → 0 % | 312.2 px | 0.19 | 0.01 | 171 |
| stroke 42 | 59 % → 0 % | 469.2 px | 0.00 | 0.00 | 106 |
| stroke 43 | 36 % → 0 % | 321.1 px | 0.19 | 0.01 | 195 |
| stroke 44 | 33 % → 1 % | 290.3 px | 0.19 | 0.02 | 162 |
| stroke 45 | 28 % → 2 % | 248.9 px | 0.19 | 0.06 | 177 |
| stroke 46 | 29 % → 2 % | 231.9 px | 0.18 | 0.07 | 209 |
| stroke 47 | 34 % → 2 % | 272.3 px | 0.18 | 0.07 | 176 |
| stroke 48 | 38 % → 3 % | 300.2 px | 0.19 | 0.09 | 120 |
| stroke 49 | 46 % → 4 % | 470.3 px | 0.18 | 0.08 | 65 |
| stroke 50 | 10 % → 0 % | 65.9 px | 0.00 | 0.00 | 198 |
| stroke 51 | 17 % → 0 % | 99.4 px | 0.18 | 0.01 | 319 |
| stroke 52 | 29 % → 0 % | 187.7 px | 0.00 | 0.00 | 162 |
| stroke 53 | 3 % → 3 % | 22.2 px | 0.19 | 1.11 | 41 |
| stroke 54 | 5 % → 3 % | 35.4 px | 0.18 | 0.56 | 31 |
| stroke 55 | 6 % → 2 % | 112.1 px | 0.20 | 0.27 | 23 |
| stroke 56 | 8 % → 3 % | 155.6 px | 0.19 | 0.36 | 14 |
| stroke 57 | 6 % → 1 % | 175.5 px | 0.20 | 0.17 | 14 |
| stroke 58 | 7 % → 1 % | 158.6 px | 0.20 | 0.14 | 21 |
| stroke 59 | 7 % → 1 % | 270.9 px | 0.19 | 0.11 | 12 |
| stroke 60 | 2 % → 0 % | 26.4 px | 0.00 | 0.00 | 16 |
| stroke 61 | 5 % → 0 % | 20.1 px | 0.18 | 0.00 | 153 |
| stroke 62 | 7 % → 0 % | 31.7 px | 0.18 | 0.00 | 113 |
| stroke 63 | 9 % → 0 % | 44.7 px | 0.00 | 0.00 | 87 |
| stroke 64 | 16 % → 0 % | 148.3 px | 0.00 | 0.00 | 33 |
| stroke 65 | 4 % → 0 % | 125.7 px | 0.00 | 0.00 | 17 |
| stroke 66 | 5 % → 0 % | 88.3 px | 0.15 | 0.00 | 22 |
| stroke 67 | 6 % → 0 % | 89.3 px | 0.00 | 0.00 | 26 |
| stroke 68 | 6 % → 0 % | 271.2 px | 0.00 | 0.00 | 6 |
| stroke 69 | 7 % → 0 % | 65.9 px | 0.15 | 0.00 | 80 |
| stroke 70 | 7 % → 0 % | 140.7 px | 0.00 | 0.00 | 22 |
| stroke 71 | 9 % → 0 % | 86.7 px | 0.00 | 0.00 | 68 |
| stroke 72 | 9 % → 0 % | 229.5 px | 0.00 | 0.00 | 9 |
| stroke 73 | 12 % → 0 % | 120.0 px | 0.00 | 0.00 | 47 |
| stroke 74 | 13 % → 0 % | 197.2 px | 0.00 | 0.00 | 20 |
| stroke 75 | 8 % → 1 % | 246.6 px | 0.16 | 0.10 | 10 |
| stroke 76 | 10 % → 1 % | 223.9 px | 0.16 | 0.07 | 23 |
| stroke 77 | 2 % → 0 % | 22.3 px | 0.00 | 0.00 | 27 |
| stroke 78 | 4 % → 1 % | 27.3 px | 0.18 | 0.15 | 171 |
| stroke 79 | 5 % → 1 % | 51.3 px | 0.19 | 0.15 | 86 |
| stroke 80 | 10 % → 0 % | 82.2 px | 0.00 | 0.00 | 47 |
| stroke 81 | 8 % → 0 % | 166.2 px | 0.00 | 0.00 | 27 |
| stroke 82 | 12 % → 0 % | 212.4 px | 0.00 | 0.00 | 26 |
| stroke 83 | 4 % → 0 % | 104.1 px | 0.16 | 0.09 | 27 |
| stroke 84 | 5 % → 1 % | 74.8 px | 0.16 | 0.23 | 32 |
| stroke 85 | 5 % → 2 % | 77.3 px | 0.17 | 0.33 | 29 |
| stroke 86 | 5 % → 2 % | 200.6 px | 0.17 | 0.43 | 11 |
| stroke 87 | 4 % → 0 % | 85.7 px | 0.00 | 0.00 | 14 |
| stroke 88 | 6 % → 0 % | 83.2 px | 0.00 | 0.00 | 95 |
| stroke 89 | 3 % → 0 % | 54.3 px | 0.22 | 0.02 | 27 |
| stroke 90 | 3 % → 0 % | 57.0 px | 0.00 | 0.00 | 25 |
| stroke 91 | 5 % → 0 % | 219.2 px | 0.00 | 0.00 | 3 |
| stroke 92 | 4 % → 0 % | 38.0 px | 0.00 | 0.00 | 105 |
| stroke 93 | 9 % → 0 % | 58.1 px | 0.00 | 0.00 | 178 |
| stroke 94 | 7 % → 0 % | 69.3 px | 0.00 | 0.00 | 98 |
| stroke 95 | 9 % → 0 % | 83.1 px | 0.00 | 0.00 | 41 |
| stroke 96 | 11 % → 0 % | 130.0 px | 0.00 | 0.00 | 68 |
| stroke 97 | 9 % → 0 % | 117.4 px | 0.00 | 0.00 | 60 |
| stroke 98 | 6 % → 0 % | 186.2 px | 0.00 | 0.00 | 12 |
| stroke 99 | 8 % → 0 % | 143.6 px | 0.00 | 0.00 | 23 |
| stroke 100 | 8 % → 0 % | 133.4 px | 0.00 | 0.00 | 30 |
| stroke 101 | 9 % → 0 % | 118.9 px | 0.00 | 0.00 | 56 |
| stroke 102 | 3 % → 0 % | 45.4 px | 0.00 | 0.00 | 86 |
| stroke 103 | 5 % → 0 % | 209.7 px | 0.00 | 0.00 | 19 |
| stroke 104 | 3 % → 4 % | 23.6 px | 0.18 | 1.49 | 131 |
| stroke 105 | 7 % → 7 % | 56.8 px | 0.18 | 0.92 | 38 |
| stroke 106 | 1 % → 1 % | 28.7 px | 0.19 | 0.93 | 13 |
| stroke 107 | 2 % → 2 % | 21.7 px | 0.17 | 0.92 | 51 |
| stroke 108 | 2 % → 2 % | 21.9 px | 0.19 | 0.94 | 41 |

## Refs v3 · #40 Watercolour blooms — own sheet
own sheet 800 × 1170 · Watercolour 1.00 + water 55 % · 80 px · 46.7 s

![Refs v3 · #40 Watercolour blooms — own sheet](Refs-v3-40-Watercolour-blooms-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 11 % → 25 % | 87.8 px | 0.37 | 2.21 | 210 |
| stroke 2 | 16 % → 26 % | 159.2 px | 0.38 | 1.67 | 299 |
| stroke 3 | 19 % → 26 % | 262.0 px | 0.38 | 1.39 | 96 |
| stroke 4 | 20 % → 25 % | 337.0 px | 0.38 | 1.26 | 75 |
| stroke 5 | 20 % → 30 % | 166.4 px | 0.38 | 1.50 | 236 |
| stroke 6 | 24 % → 32 % | 187.9 px | 0.39 | 1.34 | 276 |
| stroke 7 | 29 % → 34 % | 193.1 px | 0.39 | 1.17 | 295 |
| stroke 8 | 33 % → 34 % | 205.0 px | 0.39 | 1.03 | 439 |
| stroke 9 | 38 % → 30 % | 207.1 px | 0.38 | 0.78 | 429 |
| stroke 10 | 41 % → 23 % | 229.6 px | 0.38 | 0.56 | 540 |
| stroke 11 | 43 % → 18 % | 241.8 px | 0.38 | 0.41 | 400 |
| stroke 12 | 44 % → 13 % | 246.0 px | 0.39 | 0.30 | 399 |
| stroke 13 | 52 % → 0 % | 343.1 px | 0.12 | 0.01 | 229 |
| stroke 14 | 25 % → 13 % | 429.9 px | 0.35 | 0.51 | 230 |
| stroke 15 | 49 % → 0 % | 396.2 px | 0.05 | 0.00 | 200 |
| stroke 16 | 21 % → 0 % | 209.8 px | 0.00 | 0.00 | 456 |
| stroke 17 | 20 % → 0 % | 161.2 px | 0.00 | 0.00 | 525 |
| stroke 18 | 23 % → 0 % | 202.4 px | 0.00 | 0.00 | 555 |
| stroke 19 | 1 % → 0 % | 29.5 px | 0.00 | 0.00 | 19 |
| stroke 20 | 5 % → 0 % | 47.9 px | 0.00 | 0.00 | 70 |
| stroke 21 | 3 % → 9 % | 64.4 px | 0.32 | 3.53 | 60 |
| stroke 22 | 9 % → 7 % | 85.8 px | 0.31 | 0.73 | 133 |
| stroke 23 | 10 % → 9 % | 279.5 px | 0.35 | 0.90 | 27 |
| stroke 24 | 16 % → 4 % | 159.9 px | 0.30 | 0.24 | 95 |
| stroke 25 | 21 % → 4 % | 224.4 px | 0.35 | 0.17 | 79 |
| stroke 26 | 23 % → 6 % | 257.6 px | 0.37 | 0.24 | 49 |
| stroke 27 | 13 % → 34 % | 142.5 px | 0.39 | 2.56 | 179 |
| stroke 28 | 30 % → 6 % | 659.1 px | 0.35 | 0.21 | 37 |
| stroke 29 | 5 % → 59 % | 53.9 px | 0.37 | 11.47 | 31 |
| stroke 30 | 11 % → 53 % | 58.4 px | 0.38 | 4.67 | 103 |
| stroke 31 | 17 % → 43 % | 78.2 px | 0.37 | 2.51 | 129 |
| stroke 32 | 36 % → 37 % | 429.5 px | 0.37 | 1.01 | 39 |
| stroke 33 | 37 % → 36 % | 665.1 px | 0.37 | 0.97 | 21 |
| stroke 34 | 6 % → 24 % | 61.9 px | 0.38 | 3.87 | 29 |
| stroke 35 | 37 % → 35 % | 885.1 px | 0.38 | 0.94 | 14 |
| stroke 36 | 11 % → 22 % | 98.9 px | 0.38 | 2.00 | 64 |
| stroke 37 | 34 % → 22 % | 275.7 px | 0.37 | 0.64 | 107 |
| stroke 38 | 3 % → 0 % | 57.8 px | 0.00 | 0.00 | 47 |
| stroke 39 | 6 % → 1 % | 74.9 px | 0.16 | 0.23 | 66 |
| stroke 40 | 3 % → 26 % | 93.9 px | 0.38 | 9.47 | 19 |
| stroke 41 | 9 % → 7 % | 98.1 px | 0.34 | 0.76 | 153 |
| stroke 42 | 15 % → 17 % | 182.1 px | 0.37 | 1.11 | 97 |
| stroke 43 | 17 % → 25 % | 365.4 px | 0.37 | 1.53 | 40 |
| stroke 44 | 5 % → 0 % | 55.0 px | 0.00 | 0.00 | 42 |
| stroke 45 | 9 % → 0 % | 72.6 px | 0.00 | 0.00 | 109 |
| stroke 46 | 12 % → 0 % | 95.1 px | 0.00 | 0.00 | 125 |
| stroke 47 | 15 % → 0 % | 121.4 px | 0.00 | 0.00 | 115 |
| stroke 48 | 18 % → 0 % | 128.4 px | 0.00 | 0.00 | 136 |
| stroke 49 | 31 % → 0 % | 467.2 px | 0.00 | 0.00 | 27 |
| stroke 50 | 26 % → 0 % | 353.4 px | 0.00 | 0.00 | 64 |
| stroke 51 | 26 % → 0 % | 334.0 px | 0.00 | 0.00 | 104 |
| stroke 52 | 27 % → 0 % | 323.2 px | 0.13 | 0.01 | 88 |
| stroke 53 | 30 % → 1 % | 365.1 px | 0.29 | 0.03 | 90 |
| stroke 54 | 4 % → 4 % | 25.8 px | 0.28 | 1.06 | 33 |
| stroke 55 | 1 % → 33 % | 49.8 px | 0.38 | 31.35 | 9 |
| stroke 56 | 13 % → 7 % | 89.2 px | 0.32 | 0.52 | 179 |
| stroke 57 | 22 % → 15 % | 112.6 px | 0.38 | 0.68 | 310 |
| stroke 58 | 30 % → 20 % | 147.4 px | 0.38 | 0.66 | 379 |
| stroke 59 | 38 % → 23 % | 210.1 px | 0.38 | 0.62 | 575 |
| stroke 60 | 11 % → 45 % | 143.0 px | 0.39 | 3.98 | 216 |
| stroke 61 | 33 % → 48 % | 438.0 px | 0.39 | 1.46 | 177 |
| stroke 62 | 10 % → 2 % | 116.2 px | 0.19 | 0.20 | 88 |
| stroke 63 | 8 % → 21 % | 75.6 px | 0.38 | 2.74 | 163 |
| stroke 64 | 14 % → 21 % | 119.4 px | 0.37 | 1.44 | 212 |
| stroke 65 | 22 % → 28 % | 129.9 px | 0.38 | 1.27 | 587 |
| stroke 66 | 31 % → 25 % | 170.6 px | 0.37 | 0.81 | 394 |
| stroke 67 | 37 % → 25 % | 200.2 px | 0.37 | 0.68 | 694 |
| stroke 68 | 63 % → 25 % | 797.9 px | 0.37 | 0.40 | 39 |
| stroke 69 | 43 % → 23 % | 310.7 px | 0.37 | 0.55 | 230 |
| stroke 70 | 6 % → 18 % | 82.3 px | 0.39 | 3.17 | 97 |
| stroke 71 | 24 % → 15 % | 300.2 px | 0.37 | 0.63 | 278 |
| stroke 72 | 2 % → 1 % | 24.6 px | 0.03 | 0.28 | 26 |
| stroke 73 | 11 % → 39 % | 65.4 px | 0.37 | 3.68 | 152 |
| stroke 74 | 18 % → 45 % | 185.9 px | 0.38 | 2.44 | 93 |
| stroke 75 | 19 % → 28 % | 107.0 px | 0.37 | 1.49 | 347 |
| stroke 76 | 22 % → 26 % | 165.7 px | 0.37 | 1.19 | 141 |
| stroke 77 | 5 % → 38 % | 66.4 px | 0.39 | 7.07 | 112 |
| stroke 78 | 9 % → 29 % | 80.4 px | 0.38 | 3.28 | 191 |
| stroke 79 | 18 % → 43 % | 407.3 px | 0.39 | 2.40 | 33 |
| stroke 80 | 17 % → 37 % | 185.9 px | 0.39 | 2.12 | 119 |
| stroke 81 | 21 % → 43 % | 480.7 px | 0.39 | 1.98 | 58 |
| stroke 82 | 21 % → 38 % | 250.7 px | 0.39 | 1.83 | 84 |
| stroke 83 | 21 % → 38 % | 381.6 px | 0.39 | 1.85 | 41 |
| stroke 84 | 24 % → 32 % | 223.3 px | 0.38 | 1.31 | 162 |
| stroke 85 | 35 % → 40 % | 321.8 px | 0.39 | 1.13 | 154 |

Numbers say: wet paint spreads well beyond the stroke.

## Refs v3 · #41 Coloured pencil — own sheet
own sheet 800 × 1108 · Charcoal 0.50 · Pastel 0.50 · 13 px · 42.1 s

![Refs v3 · #41 Coloured pencil — own sheet](Refs-v3-41-Coloured-pencil-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 5 % → 0 % | 16.7 px | 0.00 | 0.00 | 3 |
| stroke 2 | 10 % → 4 % | 21.9 px | 0.17 | 0.38 | 2 |
| stroke 3 | 13 % → 5 % | 22.7 px | 0.17 | 0.39 | 8 |
| stroke 4 | 18 % → 3 % | 31.3 px | 0.17 | 0.16 | 6 |
| stroke 5 | 8 % → 0 % | 14.1 px | 0.00 | 0.00 | 5 |
| stroke 6 | 18 % → 1 % | 34.1 px | 0.17 | 0.05 | 19 |
| stroke 7 | 11 % → 0 % | 27.1 px | 0.00 | 0.00 | 23 |
| stroke 8 | 15 % → 0 % | 34.4 px | 0.00 | 0.00 | 37 |
| stroke 9 | 20 % → 0 % | 45.2 px | 0.00 | 0.00 | 25 |
| stroke 10 | 26 % → 0 % | 53.9 px | 0.00 | 0.00 | 16 |
| stroke 11 | 31 % → 0 % | 62.5 px | 0.00 | 0.00 | 17 |
| stroke 12 | 37 % → 0 % | 69.2 px | 0.00 | 0.00 | 17 |
| stroke 13 | 40 % → 0 % | 73.5 px | 0.00 | 0.00 | 16 |
| stroke 14 | 42 % → 0 % | 73.6 px | 0.00 | 0.00 | 13 |
| stroke 15 | 39 % → 0 % | 68.7 px | 0.00 | 0.00 | 5 |
| stroke 16 | 11 % → 0 % | 14.4 px | 0.00 | 0.00 | 7 |
| stroke 17 | 16 % → 0 % | 22.1 px | 0.16 | 0.01 | 11 |
| stroke 18 | 20 % → 0 % | 29.6 px | 0.00 | 0.00 | 17 |
| stroke 19 | 24 % → 0 % | 37.1 px | 0.00 | 0.00 | 27 |
| stroke 20 | 30 % → 0 % | 46.3 px | 0.00 | 0.00 | 29 |
| stroke 21 | 37 % → 0 % | 55.1 px | 0.00 | 0.00 | 22 |
| stroke 22 | 39 % → 0 % | 56.1 px | 0.00 | 0.00 | 22 |
| stroke 23 | 38 % → 0 % | 56.9 px | 0.00 | 0.00 | 27 |
| stroke 24 | 37 % → 0 % | 52.3 px | 0.00 | 0.00 | 15 |
| stroke 25 | 31 % → 0 % | 78.1 px | 0.00 | 0.00 | 1 |
| stroke 26 | 36 % → 0 % | 47.9 px | 0.00 | 0.00 | 10 |
| stroke 27 | 36 % → 0 % | 49.8 px | 0.00 | 0.00 | 6 |
| stroke 28 | 38 % → 0 % | 53.2 px | 0.00 | 0.00 | 4 |
| stroke 29 | 35 % → 0 % | 52.8 px | 0.00 | 0.00 | 3 |
| stroke 30 | 7 % → 0 % | 12.9 px | 0.00 | 0.00 | 7 |
| stroke 31 | 13 % → 0 % | 20.9 px | 0.00 | 0.00 | 9 |
| stroke 32 | 20 % → 0 % | 31.4 px | 0.00 | 0.00 | 6 |
| stroke 33 | 22 % → 0 % | 35.9 px | 0.00 | 0.00 | 13 |
| stroke 34 | 27 % → 0 % | 44.8 px | 0.00 | 0.00 | 22 |
| stroke 35 | 31 % → 0 % | 50.7 px | 0.00 | 0.00 | 11 |
| stroke 36 | 32 % → 0 % | 51.1 px | 0.00 | 0.00 | 7 |
| stroke 37 | 34 % → 0 % | 54.9 px | 0.00 | 0.00 | 6 |
| stroke 38 | 31 % → 0 % | 53.3 px | 0.00 | 0.00 | 7 |
| stroke 39 | 14 % → 0 % | 39.5 px | 0.00 | 0.00 | 1 |
| stroke 40 | 28 % → 0 % | 47.0 px | 0.00 | 0.00 | 5 |
| stroke 41 | 10 % → 0 % | 29.9 px | 0.00 | 0.00 | 4 |
| stroke 42 | 18 % → 2 % | 30.2 px | 0.18 | 0.13 | 13 |
| stroke 43 | 23 % → 3 % | 37.6 px | 0.18 | 0.12 | 11 |
| stroke 44 | 13 % → 0 % | 25.3 px | 0.00 | 0.00 | 2 |
| stroke 45 | 21 % → 5 % | 36.3 px | 0.18 | 0.22 | 12 |
| stroke 46 | 25 % → 7 % | 44.9 px | 0.18 | 0.27 | 24 |
| stroke 47 | 32 % → 12 % | 53.4 px | 0.18 | 0.39 | 15 |
| stroke 48 | 33 % → 20 % | 53.4 px | 0.18 | 0.61 | 6 |
| stroke 49 | 7 % → 0 % | 14.9 px | 0.00 | 0.00 | 1 |
| stroke 50 | 8 % → 9 % | 13.6 px | 0.17 | 1.11 | 5 |
| stroke 51 | 14 % → 0 % | 31.1 px | 0.00 | 0.00 | 1 |
| stroke 52 | 12 % → 9 % | 19.8 px | 0.18 | 0.79 | 11 |
| stroke 53 | 14 % → 0 % | 33.3 px | 0.00 | 0.00 | 2 |
| stroke 54 | 17 % → 8 % | 29.8 px | 0.18 | 0.44 | 16 |
| stroke 55 | 16 % → 7 % | 33.4 px | 0.18 | 0.45 | 23 |
| stroke 56 | 22 % → 7 % | 48.0 px | 0.18 | 0.32 | 23 |
| stroke 57 | 28 % → 6 % | 61.5 px | 0.18 | 0.22 | 21 |
| stroke 58 | 34 % → 5 % | 76.4 px | 0.18 | 0.14 | 24 |
| stroke 59 | 42 % → 0 % | 69.2 px | 0.00 | 0.00 | 7 |
| stroke 60 | 30 % → 3 % | 57.5 px | 0.18 | 0.09 | 7 |
| stroke 61 | 44 % → 0 % | 72.0 px | 0.00 | 0.00 | 13 |
| stroke 62 | 47 % → 0 % | 77.0 px | 0.00 | 0.00 | 13 |
| stroke 63 | 49 % → 0 % | 84.7 px | 0.00 | 0.00 | 2 |
| stroke 64 | 14 % → 0 % | 23.8 px | 0.00 | 0.00 | 5 |
| stroke 65 | 8 % → 0 % | 14.6 px | 0.00 | 0.00 | 4 |
| stroke 66 | 5 % → 4 % | 13.5 px | 0.18 | 0.69 | 1 |
| stroke 67 | 9 % → 0 % | 25.6 px | 0.00 | 0.00 | 1 |
| stroke 68 | 9 % → 11 % | 16.7 px | 0.18 | 1.14 | 11 |
| stroke 69 | 6 % → 0 % | 11.8 px | 0.00 | 0.00 | 5 |
| stroke 70 | 13 % → 7 % | 25.6 px | 0.18 | 0.56 | 17 |
| stroke 71 | 24 % → 10 % | 42.1 px | 0.18 | 0.42 | 10 |
| stroke 72 | 35 % → 18 % | 62.5 px | 0.18 | 0.52 | 3 |
| stroke 73 | 9 % → 20 % | 10.3 px | 0.18 | 2.22 | 11 |
| stroke 74 | 17 % → 9 % | 23.5 px | 0.17 | 0.51 | 7 |
| stroke 75 | 16 % → 2 % | 39.1 px | 0.18 | 0.12 | 1 |
| stroke 76 | 14 % → 0 % | 32.3 px | 0.00 | 0.00 | 2 |
| stroke 77 | 25 % → 0 % | 63.2 px | 0.00 | 0.00 | 2 |
| stroke 78 | 18 % → 0 % | 21.9 px | 0.00 | 0.00 | 9 |
| stroke 79 | 23 % → 0 % | 42.8 px | 0.00 | 0.00 | 1 |
| stroke 80 | 5 % → 0 % | 13.8 px | 0.00 | 0.00 | 1 |
| stroke 81 | 10 % → 0 % | 25.2 px | 0.00 | 0.00 | 2 |
| stroke 82 | 12 % → 0 % | 18.1 px | 0.00 | 0.00 | 4 |
| stroke 83 | 17 % → 0 % | 18.7 px | 0.00 | 0.00 | 8 |
| stroke 84 | 25 % → 0 % | 29.5 px | 0.00 | 0.00 | 3 |
| stroke 85 | 22 % → 0 % | 41.8 px | 0.00 | 0.00 | 2 |
| stroke 86 | 16 % → 0 % | 23.8 px | 0.00 | 0.00 | 2 |
| stroke 87 | 10 % → 0 % | 17.8 px | 0.00 | 0.00 | 4 |
| stroke 88 | 5 % → 0 % | 14.0 px | 0.00 | 0.00 | 2 |
| stroke 89 | 17 % → 0 % | 33.2 px | 0.00 | 0.00 | 4 |
| stroke 90 | 9 % → 0 % | 18.4 px | 0.00 | 0.00 | 1 |
| stroke 91 | 10 % → 0 % | 19.2 px | 0.00 | 0.00 | 2 |
| stroke 92 | 21 % → 0 % | 39.2 px | 0.00 | 0.00 | 9 |
| stroke 93 | 16 % → 0 % | 27.1 px | 0.00 | 0.00 | 16 |
| stroke 94 | 16 % → 0 % | 32.3 px | 0.00 | 0.00 | 24 |
| stroke 95 | 23 % → 0 % | 39.5 px | 0.00 | 0.00 | 15 |
| stroke 96 | 8 % → 0 % | 14.9 px | 0.00 | 0.00 | 1 |
| stroke 97 | 14 % → 0 % | 19.7 px | 0.00 | 0.00 | 8 |
| stroke 98 | 6 % → 0 % | 14.3 px | 0.00 | 0.00 | 2 |
| stroke 99 | 21 % → 0 % | 42.9 px | 0.00 | 0.00 | 3 |
| stroke 100 | 6 % → 0 % | 11.1 px | 0.00 | 0.00 | 1 |
| stroke 101 | 8 % → 0 % | 15.8 px | 0.00 | 0.00 | 5 |
| stroke 102 | 15 % → 0 % | 26.0 px | 0.00 | 0.00 | 2 |
| stroke 103 | 20 % → 0 % | 55.5 px | 0.00 | 0.00 | 7 |
| stroke 104 | 15 % → 0 % | 51.1 px | 0.00 | 0.00 | 1 |
| stroke 105 | 7 % → 0 % | 11.9 px | 0.00 | 0.00 | 7 |
| stroke 106 | 15 % → 0 % | 24.3 px | 0.00 | 0.00 | 3 |
| stroke 107 | 18 % → 0 % | 25.9 px | 0.00 | 0.00 | 8 |
| stroke 108 | 18 % → 0 % | 20.5 px | 0.00 | 0.00 | 6 |
| stroke 109 | 24 % → 0 % | 26.5 px | 0.00 | 0.00 | 15 |
| stroke 110 | 27 % → 0 % | 34.3 px | 0.00 | 0.00 | 23 |
| stroke 111 | 6 % → 0 % | 15.3 px | 0.00 | 0.00 | 2 |
| stroke 112 | 12 % → 0 % | 30.5 px | 0.00 | 0.00 | 1 |
| stroke 113 | 15 % → 0 % | 26.2 px | 0.00 | 0.00 | 1 |
| stroke 114 | 19 % → 0 % | 39.3 px | 0.00 | 0.00 | 2 |
| stroke 115 | 12 % → 0 % | 17.4 px | 0.00 | 0.00 | 26 |
| stroke 116 | 16 % → 0 % | 26.3 px | 0.00 | 0.00 | 11 |
| stroke 117 | 23 % → 0 % | 41.5 px | 0.00 | 0.00 | 3 |
| stroke 118 | 26 % → 0 % | 45.0 px | 0.00 | 0.00 | 7 |
| stroke 119 | 5 % → 0 % | 15.2 px | 0.00 | 0.00 | 0 |
| stroke 120 | 24 % → 0 % | 39.7 px | 0.00 | 0.00 | 25 |
| stroke 121 | 13 % → 0 % | 22.0 px | 0.00 | 0.00 | 7 |
| stroke 122 | 19 % → 0 % | 33.4 px | 0.00 | 0.00 | 17 |
| stroke 123 | 23 % → 0 % | 35.4 px | 0.00 | 0.00 | 7 |
| stroke 124 | 15 % → 0 % | 24.3 px | 0.00 | 0.00 | 34 |
| stroke 125 | 23 % → 0 % | 35.5 px | 0.00 | 0.00 | 26 |
| stroke 126 | 33 % → 0 % | 48.1 px | 0.00 | 0.00 | 24 |
| stroke 127 | 38 % → 0 % | 61.0 px | 0.00 | 0.00 | 4 |
| stroke 128 | 43 % → 0 % | 60.6 px | 0.00 | 0.00 | 5 |
| stroke 129 | 7 % → 0 % | 16.2 px | 0.00 | 0.00 | 7 |
| stroke 130 | 8 % → 0 % | 17.8 px | 0.00 | 0.00 | 1 |
| stroke 131 | 8 % → 0 % | 13.7 px | 0.00 | 0.00 | 7 |
| stroke 132 | 8 % → 0 % | 19.5 px | 0.00 | 0.00 | 4 |
| stroke 133 | 14 % → 0 % | 13.3 px | 0.00 | 0.00 | 9 |
| stroke 134 | 23 % → 0 % | 35.9 px | 0.00 | 0.00 | 2 |
| stroke 135 | 24 % → 0 % | 38.2 px | 0.00 | 0.00 | 2 |
| stroke 136 | 22 % → 0 % | 36.9 px | 0.00 | 0.00 | 49 |
| stroke 137 | 26 % → 0 % | 61.3 px | 0.00 | 0.00 | 2 |
| stroke 138 | 5 % → 0 % | 15.6 px | 0.00 | 0.00 | 0 |
| stroke 139 | 16 % → 2 % | 14.1 px | 0.17 | 0.14 | 21 |
| stroke 140 | 32 % → 0 % | 53.2 px | 0.00 | 0.00 | 16 |
| stroke 141 | 8 % → 2 % | 13.1 px | 0.18 | 0.31 | 24 |
| stroke 142 | 5 % → 0 % | 14.5 px | 0.00 | 0.00 | 4 |
| stroke 143 | 11 % → 1 % | 23.4 px | 0.18 | 0.10 | 8 |
| stroke 144 | 16 % → 9 % | 30.7 px | 0.18 | 0.57 | 7 |
| stroke 145 | 21 % → 15 % | 42.8 px | 0.18 | 0.73 | 1 |
| stroke 146 | 22 % → 16 % | 59.2 px | 0.18 | 0.70 | 2 |
| stroke 147 | 6 % → 8 % | 15.7 px | 0.18 | 1.25 | 0 |
| stroke 148 | 13 % → 3 % | 24.0 px | 0.17 | 0.25 | 12 |
| stroke 149 | 8 % → 24 % | 14.9 px | 0.18 | 2.86 | 10 |
| stroke 150 | 10 % → 0 % | 19.9 px | 0.00 | 0.00 | 0 |
| stroke 151 | 10 % → 33 % | 19.4 px | 0.18 | 3.19 | 2 |
| stroke 152 | 8 % → 0 % | 18.5 px | 0.00 | 0.00 | 2 |
| stroke 153 | 20 % → 0 % | 36.4 px | 0.00 | 0.00 | 1 |
| stroke 154 | 12 % → 0 % | 14.5 px | 0.00 | 0.00 | 9 |
| stroke 155 | 6 % → 0 % | 15.1 px | 0.00 | 0.00 | 1 |
| stroke 156 | 5 % → 0 % | 13.7 px | 0.00 | 0.00 | 1 |
| stroke 157 | 8 % → 0 % | 11.8 px | 0.00 | 0.00 | 6 |
| stroke 158 | 6 % → 0 % | 12.7 px | 0.00 | 0.00 | 1 |
| stroke 159 | 10 % → 0 % | 17.2 px | 0.00 | 0.00 | 15 |
| stroke 160 | 15 % → 0 % | 25.9 px | 0.00 | 0.00 | 17 |
| stroke 161 | 11 % → 0 % | 25.6 px | 0.00 | 0.00 | 2 |
| stroke 162 | 9 % → 0 % | 14.9 px | 0.00 | 0.00 | 3 |
| stroke 163 | 24 % → 0 % | 37.7 px | 0.00 | 0.00 | 8 |
| stroke 164 | 10 % → 0 % | 19.1 px | 0.00 | 0.00 | 21 |
| stroke 165 | 23 % → 0 % | 35.8 px | 0.00 | 0.00 | 11 |
| stroke 166 | 24 % → 0 % | 45.6 px | 0.00 | 0.00 | 5 |
| stroke 167 | 27 % → 0 % | 48.8 px | 0.00 | 0.00 | 2 |
| stroke 168 | 26 % → 0 % | 39.1 px | 0.00 | 0.00 | 7 |
| stroke 169 | 24 % → 0 % | 37.8 px | 0.00 | 0.00 | 10 |
| stroke 170 | 29 % → 0 % | 44.6 px | 0.00 | 0.00 | 5 |
| stroke 171 | 23 % → 0 % | 60.2 px | 0.00 | 0.00 | 6 |
| stroke 172 | 28 % → 0 % | 42.6 px | 0.00 | 0.00 | 8 |
| stroke 173 | 12 % → 0 % | 21.6 px | 0.00 | 0.00 | 2 |
| stroke 174 | 29 % → 0 % | 50.5 px | 0.00 | 0.00 | 2 |
| stroke 175 | 30 % → 0 % | 45.4 px | 0.00 | 0.00 | 9 |
| stroke 176 | 14 % → 0 % | 22.6 px | 0.00 | 0.00 | 18 |
| stroke 177 | 29 % → 0 % | 44.2 px | 0.00 | 0.00 | 5 |
| stroke 178 | 27 % → 0 % | 52.7 px | 0.00 | 0.00 | 4 |
| stroke 179 | 27 % → 0 % | 45.4 px | 0.00 | 0.00 | 17 |
| stroke 180 | 31 % → 0 % | 50.1 px | 0.00 | 0.00 | 9 |
| stroke 181 | 32 % → 0 % | 50.3 px | 0.00 | 0.00 | 7 |
| stroke 182 | 32 % → 0 % | 49.4 px | 0.00 | 0.00 | 8 |
| stroke 183 | 6 % → 0 % | 12.6 px | 0.00 | 0.00 | 2 |
| stroke 184 | 11 % → 0 % | 17.4 px | 0.00 | 0.00 | 11 |
| stroke 185 | 13 % → 0 % | 21.8 px | 0.00 | 0.00 | 10 |
| stroke 186 | 18 % → 0 % | 31.3 px | 0.00 | 0.00 | 11 |
| stroke 187 | 16 % → 0 % | 28.6 px | 0.00 | 0.00 | 14 |
| stroke 188 | 6 % → 0 % | 13.1 px | 0.00 | 0.00 | 1 |
| stroke 189 | 8 % → 0 % | 19.8 px | 0.00 | 0.00 | 2 |
| stroke 190 | 12 % → 0 % | 32.2 px | 0.00 | 0.00 | 2 |
| stroke 191 | 15 % → 0 % | 27.9 px | 0.00 | 0.00 | 2 |
| stroke 192 | 17 % → 0 % | 23.6 px | 0.00 | 0.00 | 15 |
| stroke 193 | 9 % → 0 % | 14.1 px | 0.00 | 0.00 | 2 |
| stroke 194 | 6 % → 0 % | 16.7 px | 0.00 | 0.00 | 4 |
| stroke 195 | 23 % → 0 % | 13.8 px | 0.00 | 0.00 | 17 |
| stroke 196 | 10 % → 0 % | 24.2 px | 0.00 | 0.00 | 4 |
| stroke 197 | 15 % → 0 % | 33.7 px | 0.00 | 0.00 | 2 |
| stroke 198 | 19 % → 0 % | 36.8 px | 0.00 | 0.00 | 2 |
| stroke 199 | 7 % → 0 % | 11.4 px | 0.00 | 0.00 | 6 |
| stroke 200 | 9 % → 0 % | 13.8 px | 0.00 | 0.00 | 26 |
| stroke 201 | 12 % → 0 % | 21.2 px | 0.00 | 0.00 | 27 |
| stroke 202 | 18 % → 0 % | 26.9 px | 0.00 | 0.00 | 6 |
| stroke 203 | 33 % → 0 % | 66.7 px | 0.00 | 0.00 | 1 |
| stroke 204 | 28 % → 0 % | 42.0 px | 0.00 | 0.00 | 6 |
| stroke 205 | 22 % → 0 % | 32.4 px | 0.00 | 0.00 | 5 |
| stroke 206 | 27 % → 0 % | 61.4 px | 0.00 | 0.00 | 1 |
| stroke 207 | 31 % → 0 % | 45.6 px | 0.00 | 0.00 | 6 |
| stroke 208 | 22 % → 0 % | 33.8 px | 0.00 | 0.00 | 8 |
| stroke 209 | 27 % → 0 % | 75.1 px | 0.00 | 0.00 | 0 |
| stroke 210 | 23 % → 0 % | 41.1 px | 0.00 | 0.00 | 5 |
| stroke 211 | 15 % → 0 % | 36.8 px | 0.00 | 0.00 | 10 |
| stroke 212 | 32 % → 0 % | 63.9 px | 0.00 | 0.00 | 3 |
| stroke 213 | 22 % → 0 % | 38.2 px | 0.00 | 0.00 | 4 |
| stroke 214 | 24 % → 0 % | 38.4 px | 0.00 | 0.00 | 7 |
| stroke 215 | 17 % → 0 % | 29.4 px | 0.00 | 0.00 | 2 |
| stroke 216 | 25 % → 0 % | 35.8 px | 0.00 | 0.00 | 5 |
| stroke 217 | 20 % → 0 % | 32.2 px | 0.00 | 0.00 | 2 |
| stroke 218 | 26 % → 0 % | 42.1 px | 0.00 | 0.00 | 6 |
| stroke 219 | 27 % → 0 % | 38.8 px | 0.00 | 0.00 | 5 |
| stroke 220 | 24 % → 0 % | 37.7 px | 0.00 | 0.00 | 3 |
| stroke 221 | 24 % → 0 % | 71.1 px | 0.00 | 0.00 | 0 |
| stroke 222 | 8 % → 0 % | 14.7 px | 0.00 | 0.00 | 3 |
| stroke 223 | 6 % → 0 % | 17.5 px | 0.00 | 0.00 | 1 |
| stroke 224 | 16 % → 0 % | 22.3 px | 0.00 | 0.00 | 4 |
| stroke 225 | 14 % → 0 % | 32.9 px | 0.00 | 0.00 | 2 |
| stroke 226 | 22 % → 0 % | 25.2 px | 0.00 | 0.00 | 5 |
| stroke 227 | 6 % → 0 % | 22.5 px | 0.00 | 0.00 | 0 |
| stroke 228 | 25 % → 0 % | 23.7 px | 0.00 | 0.00 | 9 |
| stroke 229 | 34 % → 0 % | 35.0 px | 0.00 | 0.00 | 10 |
| stroke 230 | 22 % → 0 % | 31.4 px | 0.00 | 0.00 | 2 |
| stroke 231 | 6 % → 0 % | 11.9 px | 0.00 | 0.00 | 6 |
| stroke 232 | 13 % → 0 % | 44.1 px | 0.00 | 0.00 | 0 |
| stroke 233 | 6 % → 0 % | 12.5 px | 0.00 | 0.00 | 4 |
| stroke 234 | 12 % → 0 % | 13.1 px | 0.00 | 0.00 | 15 |
| stroke 235 | 25 % → 0 % | 27.2 px | 0.00 | 0.00 | 12 |
| stroke 236 | 35 % → 0 % | 49.2 px | 0.00 | 0.00 | 5 |
| stroke 237 | 11 % → 0 % | 13.2 px | 0.00 | 0.00 | 7 |
| stroke 238 | 11 % → 0 % | 12.4 px | 0.00 | 0.00 | 9 |
| stroke 239 | 21 % → 0 % | 50.4 px | 0.00 | 0.00 | 1 |
| stroke 240 | 20 % → 0 % | 33.5 px | 0.00 | 0.00 | 2 |
| stroke 241 | 22 % → 0 % | 65.3 px | 0.00 | 0.00 | 0 |
| stroke 242 | 15 % → 0 % | 33.4 px | 0.00 | 0.00 | 1 |
| stroke 243 | 10 % → 0 % | 12.4 px | 0.00 | 0.00 | 4 |
| stroke 244 | 7 % → 0 % | 14.7 px | 0.00 | 0.00 | 3 |
| stroke 245 | 12 % → 0 % | 38.9 px | 0.00 | 0.00 | 0 |
| stroke 246 | 16 % → 0 % | 20.6 px | 0.00 | 0.00 | 5 |
| stroke 247 | 22 % → 0 % | 30.4 px | 0.00 | 0.00 | 2 |
| stroke 248 | 22 % → 0 % | 31.7 px | 0.00 | 0.00 | 2 |
| stroke 249 | 6 % → 0 % | 15.2 px | 0.00 | 0.00 | 2 |
| stroke 250 | 9 % → 0 % | 13.9 px | 0.00 | 0.00 | 4 |
| stroke 251 | 6 % → 0 % | 13.4 px | 0.00 | 0.00 | 1 |
| stroke 252 | 8 % → 0 % | 14.3 px | 0.00 | 0.00 | 5 |
| stroke 253 | 11 % → 0 % | 24.1 px | 0.00 | 0.00 | 1 |
| stroke 254 | 14 % → 0 % | 13.9 px | 0.00 | 0.00 | 13 |
| stroke 255 | 18 % → 0 % | 15.2 px | 0.00 | 0.00 | 13 |
| stroke 256 | 33 % → 0 % | 30.8 px | 0.00 | 0.00 | 5 |
| stroke 257 | 11 % → 0 % | 10.0 px | 0.00 | 0.00 | 3 |
| stroke 258 | 7 % → 0 % | 14.2 px | 0.00 | 0.00 | 4 |
| stroke 259 | 10 % → 0 % | 16.5 px | 0.00 | 0.00 | 26 |
| stroke 260 | 14 % → 0 % | 24.5 px | 0.00 | 0.00 | 18 |
| stroke 261 | 16 % → 0 % | 38.9 px | 0.00 | 0.00 | 1 |
| stroke 262 | 31 % → 0 % | 69.7 px | 0.00 | 0.00 | 2 |
| stroke 263 | 12 % → 0 % | 20.7 px | 0.00 | 0.00 | 5 |
| stroke 264 | 7 % → 0 % | 13.9 px | 0.00 | 0.00 | 2 |
| stroke 265 | 12 % → 0 % | 19.1 px | 0.00 | 0.00 | 5 |
| stroke 266 | 5 % → 10 % | 14.0 px | 0.18 | 1.86 | 2 |
| stroke 267 | 17 % → 0 % | 26.8 px | 0.00 | 0.00 | 11 |
| stroke 268 | 11 % → 1 % | 17.2 px | 0.18 | 0.11 | 7 |
| stroke 269 | 21 % → 0 % | 33.3 px | 0.00 | 0.00 | 18 |
| stroke 270 | 35 % → 0 % | 58.6 px | 0.00 | 0.00 | 8 |
| stroke 271 | 20 % → 0 % | 42.7 px | 0.00 | 0.00 | 1 |
| stroke 272 | 34 % → 0 % | 52.9 px | 0.00 | 0.00 | 11 |
| stroke 273 | 25 % → 0 % | 65.0 px | 0.00 | 0.00 | 1 |
| stroke 274 | 32 % → 0 % | 49.4 px | 0.00 | 0.00 | 6 |
| stroke 275 | 34 % → 0 % | 67.1 px | 0.00 | 0.00 | 4 |
| stroke 276 | 27 % → 0 % | 66.3 px | 0.00 | 0.00 | 1 |
| stroke 277 | 27 % → 0 % | 67.2 px | 0.00 | 0.00 | 2 |
| stroke 278 | 23 % → 0 % | 72.3 px | 0.00 | 0.00 | 0 |
| stroke 279 | 14 % → 0 % | 43.4 px | 0.00 | 0.00 | 0 |
| stroke 280 | 18 % → 0 % | 24.0 px | 0.00 | 0.00 | 14 |
| stroke 281 | 25 % → 0 % | 32.8 px | 0.00 | 0.00 | 9 |
| stroke 282 | 11 % → 0 % | 35.8 px | 0.00 | 0.00 | 1 |
| stroke 283 | 26 % → 0 % | 33.3 px | 0.00 | 0.00 | 16 |
| stroke 284 | 26 % → 0 % | 34.1 px | 0.00 | 0.00 | 7 |
| stroke 285 | 8 % → 0 % | 15.5 px | 0.00 | 0.00 | 3 |
| stroke 286 | 14 % → 0 % | 23.4 px | 0.00 | 0.00 | 11 |
| stroke 287 | 11 % → 0 % | 13.4 px | 0.00 | 0.00 | 14 |
| stroke 288 | 18 % → 0 % | 20.1 px | 0.00 | 0.00 | 15 |
| stroke 289 | 31 % → 0 % | 35.6 px | 0.00 | 0.00 | 16 |
| stroke 290 | 8 % → 9 % | 12.6 px | 0.17 | 1.02 | 11 |
| stroke 291 | 15 % → 6 % | 24.1 px | 0.17 | 0.41 | 5 |
| stroke 292 | 15 % → 13 % | 35.6 px | 0.17 | 0.86 | 2 |
| stroke 293 | 17 % → 0 % | 29.8 px | 0.07 | 0.00 | 28 |
| stroke 294 | 19 % → 0 % | 44.3 px | 0.00 | 0.00 | 14 |
| stroke 295 | 7 % → 24 % | 13.2 px | 0.18 | 3.36 | 7 |
| stroke 296 | 15 % → 20 % | 29.8 px | 0.18 | 1.35 | 4 |
| stroke 297 | 23 % → 10 % | 49.3 px | 0.18 | 0.42 | 1 |
| stroke 298 | 23 % → 4 % | 70.6 px | 0.18 | 0.19 | 0 |
| stroke 299 | 8 % → 30 % | 23.9 px | 0.18 | 3.83 | 3 |
| stroke 300 | 12 % → 23 % | 27.2 px | 0.18 | 1.90 | 2 |
| stroke 301 | 9 % → 24 % | 21.0 px | 0.18 | 2.55 | 1 |
| stroke 302 | 6 % → 0 % | 12.0 px | 0.00 | 0.00 | 8 |
| stroke 303 | 10 % → 0 % | 17.9 px | 0.00 | 0.00 | 17 |
| stroke 304 | 19 % → 0 % | 32.8 px | 0.00 | 0.00 | 22 |
| stroke 305 | 5 % → 0 % | 15.9 px | 0.00 | 0.00 | 1 |
| stroke 306 | 15 % → 0 % | 25.3 px | 0.00 | 0.00 | 6 |
| stroke 307 | 16 % → 0 % | 27.6 px | 0.00 | 0.00 | 9 |
| stroke 308 | 24 % → 0 % | 40.5 px | 0.00 | 0.00 | 8 |
| stroke 309 | 34 % → 0 % | 58.3 px | 0.00 | 0.00 | 37 |
| stroke 310 | 24 % → 0 % | 78.8 px | 0.00 | 0.00 | 1 |
| stroke 311 | 24 % → 0 % | 44.1 px | 0.00 | 0.00 | 12 |
| stroke 312 | 16 % → 0 % | 31.1 px | 0.00 | 0.00 | 6 |
| stroke 313 | 7 % → 0 % | 11.3 px | 0.00 | 0.00 | 10 |
| stroke 314 | 14 % → 0 % | 20.2 px | 0.00 | 0.00 | 5 |
| stroke 315 | 19 % → 0 % | 23.7 px | 0.00 | 0.00 | 4 |
| stroke 316 | 9 % → 0 % | 21.3 px | 0.00 | 0.00 | 2 |
| stroke 317 | 20 % → 0 % | 24.9 px | 0.00 | 0.00 | 7 |
| stroke 318 | 11 % → 0 % | 22.1 px | 0.00 | 0.00 | 7 |
| stroke 319 | 17 % → 0 % | 52.5 px | 0.00 | 0.00 | 6 |
| stroke 320 | 14 % → 0 % | 23.8 px | 0.00 | 0.00 | 2 |
| stroke 321 | 17 % → 0 % | 24.8 px | 0.00 | 0.00 | 2 |
| stroke 322 | 19 % → 0 % | 21.4 px | 0.00 | 0.00 | 23 |
| stroke 323 | 22 % → 0 % | 27.4 px | 0.00 | 0.00 | 3 |
| stroke 324 | 26 % → 0 % | 38.3 px | 0.14 | 0.00 | 2 |
| stroke 325 | 5 % → 0 % | 13.6 px | 0.00 | 0.00 | 1 |
| stroke 326 | 9 % → 0 % | 13.3 px | 0.00 | 0.00 | 2 |
| stroke 327 | 16 % → 3 % | 20.8 px | 0.17 | 0.16 | 17 |
| stroke 328 | 9 % → 0 % | 23.9 px | 0.00 | 0.00 | 1 |
| stroke 329 | 6 % → 0 % | 14.1 px | 0.00 | 0.00 | 2 |
| stroke 330 | 11 % → 0 % | 27.8 px | 0.00 | 0.00 | 1 |
| stroke 331 | 16 % → 0 % | 45.8 px | 0.00 | 0.00 | 1 |
| stroke 332 | 6 % → 0 % | 17.5 px | 0.00 | 0.00 | 1 |
| stroke 333 | 12 % → 0 % | 12.9 px | 0.00 | 0.00 | 4 |
| stroke 334 | 17 % → 0 % | 11.6 px | 0.00 | 0.00 | 27 |
| stroke 335 | 27 % → 0 % | 33.1 px | 0.00 | 0.00 | 7 |
| stroke 336 | 30 % → 0 % | 35.6 px | 0.00 | 0.00 | 4 |
| stroke 337 | 31 % → 0 % | 67.4 px | 0.00 | 0.00 | 2 |
| stroke 338 | 33 % → 0 % | 40.0 px | 0.00 | 0.00 | 4 |
| stroke 339 | 29 % → 0 % | 35.0 px | 0.00 | 0.00 | 5 |
| stroke 340 | 5 % → 0 % | 17.4 px | 0.00 | 0.00 | 1 |
| stroke 341 | 6 % → 0 % | 13.9 px | 0.00 | 0.00 | 1 |
| stroke 342 | 11 % → 0 % | 28.5 px | 0.00 | 0.00 | 2 |
| stroke 343 | 12 % → 0 % | 41.7 px | 0.00 | 0.00 | 0 |
| stroke 344 | 7 % → 9 % | 12.7 px | 0.18 | 1.27 | 5 |
| stroke 345 | 13 % → 0 % | 12.5 px | 0.00 | 0.00 | 7 |
| stroke 346 | 5 % → 0 % | 15.3 px | 0.00 | 0.00 | 1 |
| stroke 347 | 9 % → 0 % | 10.2 px | 0.00 | 0.00 | 7 |
| stroke 348 | 17 % → 2 % | 18.2 px | 0.18 | 0.12 | 17 |
| stroke 349 | 26 % → 5 % | 27.3 px | 0.18 | 0.20 | 18 |
| stroke 350 | 28 % → 10 % | 29.1 px | 0.18 | 0.36 | 17 |
| stroke 351 | 30 % → 12 % | 32.4 px | 0.18 | 0.40 | 23 |
| stroke 352 | 30 % → 14 % | 33.1 px | 0.18 | 0.45 | 7 |
| stroke 353 | 32 % → 11 % | 36.8 px | 0.18 | 0.35 | 5 |
| stroke 354 | 27 % → 11 % | 33.6 px | 0.17 | 0.41 | 8 |
| stroke 355 | 24 % → 9 % | 35.1 px | 0.17 | 0.36 | 8 |
| stroke 356 | 25 % → 8 % | 49.0 px | 0.18 | 0.32 | 3 |
| stroke 357 | 6 % → 0 % | 13.8 px | 0.00 | 0.00 | 1 |
| stroke 358 | 10 % → 0 % | 20.9 px | 0.00 | 0.00 | 6 |
| stroke 359 | 15 % → 0 % | 26.4 px | 0.00 | 0.00 | 3 |
| stroke 360 | 19 % → 1 % | 32.0 px | 0.19 | 0.04 | 3 |
| stroke 361 | 20 % → 6 % | 31.0 px | 0.18 | 0.28 | 24 |
| stroke 362 | 23 % → 13 % | 35.5 px | 0.18 | 0.59 | 12 |
| stroke 363 | 26 % → 20 % | 40.9 px | 0.18 | 0.75 | 13 |
| stroke 364 | 27 % → 19 % | 53.3 px | 0.18 | 0.69 | 2 |
| stroke 365 | 17 % → 17 % | 44.8 px | 0.18 | 0.99 | 1 |
| stroke 366 | 6 % → 0 % | 15.3 px | 0.00 | 0.00 | 4 |
| stroke 367 | 6 % → 0 % | 16.2 px | 0.00 | 0.00 | 1 |
| stroke 368 | 5 % → 0 % | 13.6 px | 0.00 | 0.00 | 1 |
| stroke 369 | 7 % → 0 % | 9.7 px | 0.00 | 0.00 | 9 |
| stroke 370 | 11 % → 0 % | 15.0 px | 0.00 | 0.00 | 39 |
| stroke 371 | 18 % → 0 % | 24.7 px | 0.00 | 0.00 | 30 |
| stroke 372 | 12 % → 0 % | 28.4 px | 0.00 | 0.00 | 2 |
| stroke 373 | 9 % → 0 % | 27.3 px | 0.00 | 0.00 | 0 |
| stroke 374 | 24 % → 0 % | 31.7 px | 0.00 | 0.00 | 13 |
| stroke 375 | 28 % → 0 % | 48.6 px | 0.00 | 0.00 | 2 |
| stroke 376 | 26 % → 0 % | 40.6 px | 0.00 | 0.00 | 8 |
| stroke 377 | 21 % → 0 % | 55.4 px | 0.00 | 0.00 | 1 |
| stroke 378 | 12 % → 0 % | 37.1 px | 0.00 | 0.00 | 1 |
| stroke 379 | 5 % → 0 % | 16.4 px | 0.00 | 0.00 | 0 |
| stroke 380 | 10 % → 0 % | 25.2 px | 0.00 | 0.00 | 2 |
| stroke 381 | 15 % → 0 % | 32.1 px | 0.00 | 0.00 | 2 |
| stroke 382 | 18 % → 0 % | 31.3 px | 0.00 | 0.00 | 3 |
| stroke 383 | 23 % → 0 % | 41.1 px | 0.00 | 0.00 | 5 |
| stroke 384 | 19 % → 0 % | 57.9 px | 0.00 | 0.00 | 1 |
| stroke 385 | 5 % → 0 % | 15.3 px | 0.00 | 0.00 | 1 |
| stroke 386 | 10 % → 0 % | 19.0 px | 0.00 | 0.00 | 3 |
| stroke 387 | 10 % → 0 % | 16.9 px | 0.00 | 0.00 | 5 |
| stroke 388 | 5 % → 0 % | 14.0 px | 0.00 | 0.00 | 2 |
| stroke 389 | 11 % → 0 % | 23.2 px | 0.00 | 0.00 | 1 |
| stroke 390 | 12 % → 0 % | 22.9 px | 0.00 | 0.00 | 3 |
| stroke 391 | 16 % → 0 % | 53.5 px | 0.00 | 0.00 | 1 |
| stroke 392 | 5 % → 0 % | 14.9 px | 0.00 | 0.00 | 4 |
| stroke 393 | 7 % → 0 % | 11.7 px | 0.00 | 0.00 | 16 |
| stroke 394 | 10 % → 0 % | 18.4 px | 0.00 | 0.00 | 23 |
| stroke 395 | 14 % → 0 % | 27.2 px | 0.00 | 0.00 | 35 |
| stroke 396 | 24 % → 0 % | 41.5 px | 0.00 | 0.00 | 49 |
| stroke 397 | 15 % → 0 % | 29.0 px | 0.00 | 0.00 | 8 |
| stroke 398 | 30 % → 0 % | 45.7 px | 0.00 | 0.00 | 18 |
| stroke 399 | 29 % → 0 % | 59.4 px | 0.00 | 0.00 | 1 |
| stroke 400 | 7 % → 0 % | 11.9 px | 0.00 | 0.00 | 2 |
| stroke 401 | 14 % → 0 % | 41.3 px | 0.00 | 0.00 | 1 |
| stroke 402 | 6 % → 28 % | 10.3 px | 0.18 | 4.43 | 3 |
| stroke 403 | 10 % → 36 % | 14.5 px | 0.18 | 3.48 | 9 |
| stroke 404 | 15 % → 31 % | 20.5 px | 0.18 | 2.08 | 23 |
| stroke 405 | 20 % → 29 % | 28.8 px | 0.18 | 1.45 | 9 |
| stroke 406 | 9 % → 24 % | 16.9 px | 0.18 | 2.56 | 2 |
| stroke 407 | 21 % → 26 % | 28.5 px | 0.18 | 1.25 | 13 |
| stroke 408 | 32 % → 35 % | 44.3 px | 0.18 | 1.08 | 8 |
| stroke 409 | 12 % → 27 % | 21.8 px | 0.18 | 2.17 | 4 |
| stroke 410 | 13 % → 14 % | 29.7 px | 0.17 | 1.06 | 1 |
| stroke 411 | 25 % → 25 % | 56.8 px | 0.18 | 1.00 | 4 |
| stroke 412 | 18 % → 28 % | 27.8 px | 0.18 | 1.59 | 2 |
| stroke 413 | 20 % → 22 % | 64.7 px | 0.18 | 1.07 | 1 |
| stroke 414 | 15 % → 25 % | 42.9 px | 0.18 | 1.59 | 1 |
| stroke 415 | 7 % → 15 % | 17.9 px | 0.17 | 2.15 | 1 |
| stroke 416 | 16 % → 28 % | 47.7 px | 0.18 | 1.75 | 0 |
| stroke 417 | 12 % → 17 % | 26.8 px | 0.17 | 1.41 | 13 |
| stroke 418 | 14 % → 25 % | 33.7 px | 0.17 | 1.79 | 7 |
| stroke 419 | 15 % → 15 % | 38.1 px | 0.17 | 1.00 | 7 |
| stroke 420 | 15 % → 19 % | 27.7 px | 0.17 | 1.34 | 1 |
| stroke 421 | 16 % → 16 % | 39.0 px | 0.17 | 1.00 | 1 |
| stroke 422 | 7 % → 20 % | 14.7 px | 0.18 | 3.05 | 1 |
| stroke 423 | 13 % → 19 % | 26.9 px | 0.18 | 1.48 | 4 |
| stroke 424 | 19 % → 19 % | 39.8 px | 0.18 | 1.00 | 5 |
| stroke 425 | 5 % → 17 % | 15.5 px | 0.18 | 3.42 | 0 |
| stroke 426 | 10 % → 21 % | 24.7 px | 0.18 | 2.06 | 1 |
| stroke 427 | 15 % → 26 % | 32.8 px | 0.18 | 1.72 | 2 |
| stroke 428 | 7 % → 13 % | 13.3 px | 0.18 | 1.80 | 2 |
| stroke 429 | 14 % → 22 % | 24.8 px | 0.18 | 1.63 | 9 |
| stroke 430 | 14 % → 14 % | 25.5 px | 0.18 | 1.00 | 15 |

Numbers say: wet paint spreads well beyond the stroke.

## Refs v3 · #42 Pink shaggy pastel — own sheet
own sheet 800 × 976 · Pastel 1.00 · 27 px · 34.7 s

![Refs v3 · #42 Pink shaggy pastel — own sheet](Refs-v3-42-Pink-shaggy-pastel-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 5 % → 15 % | 28.9 px | 0.37 | 2.95 | 17 |
| stroke 2 | 4 % → 51 % | 28.8 px | 0.37 | 13.84 | 9 |
| stroke 3 | 8 % → 49 % | 38.8 px | 0.37 | 6.12 | 5 |
| stroke 4 | 13 % → 45 % | 72.1 px | 0.37 | 3.58 | 8 |
| stroke 5 | 8 % → 0 % | 25.9 px | 0.00 | 0.00 | 17 |
| stroke 6 | 13 % → 0 % | 37.1 px | 0.00 | 0.00 | 21 |
| stroke 7 | 19 % → 0 % | 68.5 px | 0.00 | 0.00 | 9 |
| stroke 8 | 23 % → 0 % | 69.6 px | 0.00 | 0.00 | 18 |
| stroke 9 | 29 % → 0 % | 216.1 px | 0.00 | 0.00 | 20 |
| stroke 10 | 22 % → 0 % | 65.6 px | 0.00 | 0.00 | 31 |
| stroke 11 | 31 % → 0 % | 210.0 px | 0.00 | 0.00 | 3 |
| stroke 12 | 24 % → 0 % | 62.8 px | 0.00 | 0.00 | 45 |
| stroke 13 | 15 % → 3 % | 87.6 px | 0.36 | 0.23 | 9 |
| stroke 14 | 24 % → 0 % | 61.1 px | 0.00 | 0.00 | 100 |
| stroke 15 | 34 % → 2 % | 89.1 px | 0.36 | 0.06 | 54 |
| stroke 16 | 28 % → 0 % | 76.1 px | 0.00 | 0.00 | 34 |
| stroke 17 | 32 % → 15 % | 85.6 px | 0.37 | 0.47 | 56 |
| stroke 18 | 47 % → 0 % | 205.1 px | 0.00 | 0.00 | 13 |
| stroke 19 | 32 % → 0 % | 83.5 px | 0.00 | 0.00 | 43 |
| stroke 20 | 30 % → 6 % | 85.7 px | 0.37 | 0.21 | 236 |
| stroke 21 | 46 % → 10 % | 119.8 px | 0.37 | 0.23 | 170 |
| stroke 22 | 37 % → 0 % | 94.8 px | 0.00 | 0.00 | 57 |
| stroke 23 | 47 % → 15 % | 134.8 px | 0.37 | 0.32 | 48 |
| stroke 24 | 50 % → 0 % | 174.1 px | 0.00 | 0.00 | 99 |
| stroke 25 | 45 % → 0 % | 121.0 px | 0.00 | 0.00 | 65 |
| stroke 26 | 47 % → 19 % | 125.5 px | 0.37 | 0.41 | 39 |
| stroke 27 | 49 % → 0 % | 154.8 px | 0.00 | 0.00 | 37 |
| stroke 28 | 50 % → 0 % | 159.6 px | 0.00 | 0.00 | 18 |
| stroke 29 | 50 % → 17 % | 132.8 px | 0.37 | 0.34 | 53 |
| stroke 30 | 45 % → 0 % | 226.3 px | 0.00 | 0.00 | 8 |
| stroke 31 | 44 % → 0 % | 141.6 px | 0.00 | 0.00 | 24 |
| stroke 32 | 50 % → 20 % | 175.2 px | 0.37 | 0.40 | 21 |
| stroke 33 | 51 % → 0 % | 233.1 px | 0.00 | 0.00 | 65 |
| stroke 34 | 40 % → 0 % | 217.9 px | 0.00 | 0.00 | 11 |
| stroke 35 | 35 % → 0 % | 107.9 px | 0.00 | 0.00 | 36 |
| stroke 36 | 47 % → 18 % | 185.5 px | 0.37 | 0.40 | 30 |
| stroke 37 | 48 % → 0 % | 240.9 px | 0.00 | 0.00 | 8 |
| stroke 38 | 35 % → 0 % | 275.6 px | 0.00 | 0.00 | 7 |
| stroke 39 | 33 % → 0 % | 105.5 px | 0.00 | 0.00 | 23 |
| stroke 40 | 45 % → 9 % | 123.6 px | 0.37 | 0.21 | 43 |
| stroke 41 | 31 % → 0 % | 209.1 px | 0.00 | 0.00 | 5 |
| stroke 42 | 32 % → 0 % | 105.5 px | 0.00 | 0.00 | 20 |
| stroke 43 | 38 % → 6 % | 101.6 px | 0.37 | 0.15 | 44 |
| stroke 44 | 30 % → 0 % | 98.2 px | 0.00 | 0.00 | 17 |
| stroke 45 | 35 % → 16 % | 268.5 px | 0.37 | 0.47 | 5 |
| stroke 46 | 38 % → 1 % | 102.1 px | 0.37 | 0.03 | 85 |
| stroke 47 | 36 % → 18 % | 134.7 px | 0.37 | 0.50 | 25 |
| stroke 48 | 38 % → 1 % | 98.0 px | 0.37 | 0.03 | 105 |
| stroke 49 | 33 % → 0 % | 96.8 px | 0.00 | 0.00 | 65 |
| stroke 50 | 36 % → 12 % | 209.4 px | 0.37 | 0.35 | 12 |
| stroke 51 | 39 % → 1 % | 99.3 px | 0.37 | 0.01 | 107 |
| stroke 52 | 36 % → 0 % | 111.7 px | 0.00 | 0.00 | 66 |
| stroke 53 | 43 % → 0 % | 319.1 px | 0.00 | 0.00 | 25 |
| stroke 54 | 41 % → 0 % | 113.3 px | 0.00 | 0.00 | 48 |
| stroke 55 | 32 % → 0 % | 114.3 px | 0.00 | 0.00 | 16 |
| stroke 56 | 28 % → 1 % | 199.7 px | 0.35 | 0.05 | 5 |
| stroke 57 | 44 % → 0 % | 114.9 px | 0.00 | 0.00 | 50 |
| stroke 58 | 31 % → 0 % | 124.9 px | 0.00 | 0.00 | 30 |
| stroke 59 | 35 % → 0 % | 99.1 px | 0.00 | 0.00 | 31 |
| stroke 60 | 46 % → 0 % | 117.6 px | 0.00 | 0.00 | 52 |
| stroke 61 | 25 % → 0 % | 107.8 px | 0.00 | 0.00 | 6 |
| stroke 62 | 26 % → 0 % | 178.2 px | 0.00 | 0.00 | 3 |
| stroke 63 | 44 % → 0 % | 116.2 px | 0.00 | 0.00 | 58 |
| stroke 64 | 27 % → 0 % | 111.0 px | 0.00 | 0.00 | 26 |
| stroke 65 | 44 % → 0 % | 114.4 px | 0.00 | 0.00 | 60 |
| stroke 66 | 33 % → 0 % | 130.7 px | 0.00 | 0.00 | 12 |
| stroke 67 | 37 % → 0 % | 303.3 px | 0.00 | 0.00 | 2 |
| stroke 68 | 47 % → 0 % | 119.5 px | 0.00 | 0.00 | 39 |
| stroke 69 | 44 % → 0 % | 112.8 px | 0.00 | 0.00 | 45 |
| stroke 70 | 26 % → 0 % | 129.1 px | 0.00 | 0.00 | 11 |
| stroke 71 | 46 % → 0 % | 225.4 px | 0.00 | 0.00 | 5 |
| stroke 72 | 53 % → 0 % | 268.1 px | 0.00 | 0.00 | 4 |
| stroke 73 | 49 % → 0 % | 158.0 px | 0.00 | 0.00 | 14 |
| stroke 74 | 38 % → 0 % | 128.8 px | 0.00 | 0.00 | 15 |
| stroke 75 | 51 % → 0 % | 252.8 px | 0.00 | 0.00 | 12 |
| stroke 76 | 11 % → 0 % | 17.7 px | 0.00 | 0.00 | 75 |
| stroke 77 | 22 % → 0 % | 38.3 px | 0.00 | 0.00 | 52 |
| stroke 78 | 32 % → 0 % | 56.2 px | 0.00 | 0.00 | 55 |
| stroke 79 | 42 % → 0 % | 73.0 px | 0.00 | 0.00 | 60 |
| stroke 80 | 41 % → 0 % | 72.0 px | 0.00 | 0.00 | 52 |
| stroke 81 | 41 % → 0 % | 71.5 px | 0.00 | 0.00 | 61 |
| stroke 82 | 40 % → 0 % | 69.6 px | 0.00 | 0.00 | 63 |
| stroke 83 | 42 % → 0 % | 87.1 px | 0.00 | 0.00 | 38 |
| stroke 84 | 36 % → 0 % | 133.9 px | 0.00 | 0.00 | 13 |
| stroke 85 | 7 % → 0 % | 21.7 px | 0.00 | 0.00 | 17 |
| stroke 86 | 40 % → 0 % | 96.9 px | 0.00 | 0.00 | 24 |
| stroke 87 | 29 % → 0 % | 48.2 px | 0.00 | 0.00 | 84 |
| stroke 88 | 35 % → 0 % | 63.8 px | 0.00 | 0.00 | 46 |
| stroke 89 | 36 % → 0 % | 143.6 px | 0.38 | 0.01 | 5 |
| stroke 90 | 23 % → 2 % | 59.2 px | 0.36 | 0.08 | 11 |
| stroke 91 | 42 % → 0 % | 77.6 px | 0.00 | 0.00 | 35 |
| stroke 92 | 35 % → 0 % | 233.6 px | 0.00 | 0.00 | 4 |
| stroke 93 | 47 % → 0 % | 97.3 px | 0.00 | 0.00 | 32 |
| stroke 94 | 32 % → 0 % | 228.7 px | 0.00 | 0.00 | 3 |
| stroke 95 | 47 % → 0 % | 107.7 px | 0.00 | 0.00 | 27 |
| stroke 96 | 31 % → 2 % | 75.6 px | 0.36 | 0.05 | 27 |
| stroke 97 | 44 % → 0 % | 107.7 px | 0.00 | 0.00 | 19 |
| stroke 98 | 47 % → 0 % | 151.1 px | 0.00 | 0.00 | 20 |
| stroke 99 | 44 % → 2 % | 289.4 px | 0.36 | 0.04 | 5 |
| stroke 100 | 40 % → 0 % | 160.7 px | 0.00 | 0.00 | 16 |
| stroke 101 | 45 % → 2 % | 205.9 px | 0.36 | 0.05 | 12 |
| stroke 102 | 53 % → 1 % | 261.5 px | 0.36 | 0.03 | 5 |
| stroke 103 | 2 % → 0 % | 19.4 px | 0.00 | 0.00 | 3 |
| stroke 104 | 5 % → 0 % | 22.8 px | 0.31 | 0.02 | 4 |
| stroke 105 | 13 % → 9 % | 23.9 px | 0.37 | 0.68 | 44 |
| stroke 106 | 21 % → 10 % | 61.0 px | 0.36 | 0.46 | 14 |
| stroke 107 | 16 % → 5 % | 27.7 px | 0.37 | 0.30 | 81 |
| stroke 108 | 28 % → 9 % | 85.9 px | 0.36 | 0.32 | 10 |
| stroke 109 | 27 % → 4 % | 47.4 px | 0.37 | 0.15 | 89 |
| stroke 110 | 32 % → 10 % | 103.1 px | 0.36 | 0.32 | 14 |
| stroke 111 | 38 % → 10 % | 126.0 px | 0.37 | 0.27 | 16 |
| stroke 112 | 36 % → 0 % | 79.1 px | 0.00 | 0.00 | 36 |
| stroke 113 | 27 % → 15 % | 83.3 px | 0.36 | 0.54 | 12 |
| stroke 114 | 37 % → 11 % | 137.6 px | 0.37 | 0.30 | 13 |
| stroke 115 | 47 % → 0 % | 163.0 px | 0.00 | 0.00 | 8 |
| stroke 116 | 38 % → 0 % | 198.9 px | 0.00 | 0.00 | 7 |
| stroke 117 | 25 % → 21 % | 68.1 px | 0.36 | 0.82 | 17 |
| stroke 118 | 29 % → 19 % | 106.1 px | 0.37 | 0.66 | 8 |
| stroke 119 | 42 % → 0 % | 113.2 px | 0.00 | 0.00 | 18 |
| stroke 120 | 29 % → 15 % | 92.5 px | 0.36 | 0.51 | 10 |
| stroke 121 | 26 % → 26 % | 108.2 px | 0.37 | 1.00 | 10 |
| stroke 122 | 37 % → 0 % | 100.0 px | 0.00 | 0.00 | 18 |
| stroke 123 | 29 % → 16 % | 99.4 px | 0.36 | 0.54 | 9 |
| stroke 124 | 33 % → 0 % | 182.9 px | 0.00 | 0.00 | 9 |
| stroke 125 | 28 % → 21 % | 89.4 px | 0.37 | 0.77 | 11 |
| stroke 126 | 22 % → 0 % | 159.0 px | 0.00 | 0.00 | 4 |
| stroke 127 | 25 % → 24 % | 73.4 px | 0.37 | 0.94 | 12 |
| stroke 128 | 26 % → 18 % | 86.0 px | 0.37 | 0.69 | 12 |
| stroke 129 | 28 % → 12 % | 111.4 px | 0.36 | 0.44 | 13 |
| stroke 130 | 27 % → 12 % | 143.5 px | 0.36 | 0.45 | 5 |
| stroke 131 | 23 % → 13 % | 160.5 px | 0.37 | 0.57 | 2 |
| stroke 132 | 19 % → 13 % | 142.1 px | 0.37 | 0.66 | 4 |
| stroke 133 | 16 % → 10 % | 129.6 px | 0.37 | 0.63 | 7 |
| stroke 134 | 15 % → 8 % | 109.2 px | 0.37 | 0.53 | 4 |
| stroke 135 | 16 % → 12 % | 47.2 px | 0.37 | 0.78 | 12 |
| stroke 136 | 19 % → 12 % | 61.2 px | 0.37 | 0.63 | 9 |
| stroke 137 | 23 % → 8 % | 67.5 px | 0.37 | 0.35 | 18 |
| stroke 138 | 27 % → 2 % | 76.7 px | 0.36 | 0.09 | 17 |
| stroke 139 | 28 % → 0 % | 82.6 px | 0.00 | 0.00 | 19 |
| stroke 140 | 31 % → 0 % | 126.5 px | 0.00 | 0.00 | 8 |
| stroke 141 | 31 % → 0 % | 226.8 px | 0.00 | 0.00 | 3 |
| stroke 142 | 31 % → 0 % | 146.7 px | 0.00 | 0.00 | 11 |
| stroke 143 | 25 % → 0 % | 62.3 px | 0.00 | 0.00 | 26 |
| stroke 144 | 30 % → 0 % | 114.5 px | 0.00 | 0.00 | 7 |
| stroke 145 | 28 % → 0 % | 108.5 px | 0.00 | 0.00 | 6 |
| stroke 146 | 25 % → 0 % | 57.6 px | 0.00 | 0.00 | 22 |
| stroke 147 | 27 % → 0 % | 179.4 px | 0.00 | 0.00 | 3 |
| stroke 148 | 35 % → 0 % | 103.7 px | 0.00 | 0.00 | 17 |
| stroke 149 | 35 % → 0 % | 102.9 px | 0.00 | 0.00 | 15 |
| stroke 150 | 35 % → 0 % | 101.6 px | 0.00 | 0.00 | 15 |
| stroke 151 | 22 % → 0 % | 151.1 px | 0.00 | 0.00 | 2 |
| stroke 152 | 34 % → 0 % | 102.5 px | 0.00 | 0.00 | 14 |
| stroke 153 | 19 % → 0 % | 97.4 px | 0.00 | 0.00 | 7 |
| stroke 154 | 34 % → 0 % | 121.9 px | 0.00 | 0.00 | 18 |
| stroke 155 | 25 % → 0 % | 101.7 px | 0.00 | 0.00 | 27 |
| stroke 156 | 29 % → 0 % | 83.5 px | 0.00 | 0.00 | 23 |
| stroke 157 | 31 % → 39 % | 165.5 px | 0.37 | 1.27 | 15 |
| stroke 158 | 48 % → 30 % | 328.1 px | 0.37 | 0.63 | 9 |
| stroke 159 | 7 % → 2 % | 26.3 px | 0.36 | 0.24 | 11 |
| stroke 160 | 12 % → 0 % | 41.2 px | 0.08 | 0.00 | 33 |
| stroke 161 | 13 % → 0 % | 32.2 px | 0.00 | 0.00 | 20 |
| stroke 162 | 13 % → 0 % | 53.2 px | 0.00 | 0.00 | 10 |
| stroke 163 | 19 % → 0 % | 38.6 px | 0.00 | 0.00 | 69 |
| stroke 164 | 26 % → 0 % | 128.4 px | 0.00 | 0.00 | 4 |
| stroke 165 | 24 % → 0 % | 57.7 px | 0.00 | 0.00 | 19 |
| stroke 166 | 30 % → 0 % | 60.5 px | 0.00 | 0.00 | 55 |
| stroke 167 | 36 % → 0 % | 185.0 px | 0.00 | 0.00 | 19 |
| stroke 168 | 35 % → 0 % | 81.9 px | 0.00 | 0.00 | 42 |
| stroke 169 | 19 % → 0 % | 73.1 px | 0.00 | 0.00 | 7 |
| stroke 170 | 37 % → 0 % | 63.7 px | 0.00 | 0.00 | 114 |
| stroke 171 | 21 % → 0 % | 51.5 px | 0.00 | 0.00 | 25 |
| stroke 172 | 41 % → 0 % | 71.7 px | 0.00 | 0.00 | 129 |
| stroke 173 | 28 % → 0 % | 63.1 px | 0.00 | 0.00 | 30 |
| stroke 174 | 47 % → 0 % | 84.2 px | 0.00 | 0.00 | 107 |
| stroke 175 | 42 % → 0 % | 79.2 px | 0.00 | 0.00 | 94 |
| stroke 176 | 5 % → 10 % | 26.7 px | 0.37 | 2.00 | 3 |
| stroke 177 | 28 % → 0 % | 150.6 px | 0.00 | 0.00 | 14 |
| stroke 178 | 4 % → 0 % | 29.4 px | 0.00 | 0.00 | 4 |
| stroke 179 | 8 % → 0 % | 36.6 px | 0.00 | 0.00 | 40 |
| stroke 180 | 15 % → 0 % | 109.3 px | 0.00 | 0.00 | 12 |
| stroke 181 | 3 % → 0 % | 19.5 px | 0.00 | 0.00 | 11 |
| stroke 182 | 3 % → 0 % | 23.8 px | 0.00 | 0.00 | 4 |
| stroke 183 | 3 % → 0 % | 19.1 px | 0.00 | 0.00 | 10 |
| stroke 184 | 6 % → 0 % | 17.1 px | 0.00 | 0.00 | 30 |
| stroke 185 | 3 % → 0 % | 25.3 px | 0.00 | 0.00 | 11 |
| stroke 186 | 6 % → 0 % | 33.4 px | 0.00 | 0.00 | 5 |
| stroke 187 | 9 % → 0 % | 107.8 px | 0.00 | 0.00 | 1 |
| stroke 188 | 3 % → 0 % | 29.5 px | 0.00 | 0.00 | 6 |
| stroke 189 | 9 % → 0 % | 77.2 px | 0.00 | 0.00 | 3 |
| stroke 190 | 5 % → 0 % | 34.9 px | 0.00 | 0.00 | 11 |
| stroke 191 | 9 % → 0 % | 86.5 px | 0.00 | 0.00 | 7 |
| stroke 192 | 16 % → 0 % | 50.4 px | 0.00 | 0.00 | 44 |
| stroke 193 | 20 % → 0 % | 117.6 px | 0.00 | 0.00 | 28 |
| stroke 194 | 3 % → 0 % | 21.9 px | 0.00 | 0.00 | 3 |
| stroke 195 | 5 % → 0 % | 40.5 px | 0.00 | 0.00 | 15 |
| stroke 196 | 3 % → 0 % | 25.4 px | 0.00 | 0.00 | 6 |
| stroke 197 | 12 % → 0 % | 42.3 px | 0.00 | 0.00 | 6 |
| stroke 198 | 12 % → 0 % | 68.9 px | 0.00 | 0.00 | 5 |
| stroke 199 | 17 % → 0 % | 82.4 px | 0.00 | 0.00 | 19 |
| stroke 200 | 23 % → 0 % | 59.0 px | 0.00 | 0.00 | 21 |
| stroke 201 | 22 % → 0 % | 182.0 px | 0.00 | 0.00 | 1 |
| stroke 202 | 25 % → 0 % | 158.3 px | 0.00 | 0.00 | 4 |
| stroke 203 | 25 % → 0 % | 164.5 px | 0.00 | 0.00 | 4 |
| stroke 204 | 26 % → 0 % | 271.8 px | 0.00 | 0.00 | 4 |
| stroke 205 | 10 % → 16 % | 35.0 px | 0.37 | 1.57 | 47 |
| stroke 206 | 19 % → 8 % | 51.9 px | 0.37 | 0.43 | 52 |
| stroke 207 | 33 % → 7 % | 235.4 px | 0.36 | 0.23 | 4 |
| stroke 208 | 34 % → 0 % | 106.8 px | 0.36 | 0.00 | 16 |
| stroke 209 | 41 % → 2 % | 499.8 px | 0.35 | 0.04 | 27 |
| stroke 210 | 26 % → 0 % | 207.9 px | 0.00 | 0.00 | 1 |
| stroke 211 | 3 % → 0 % | 24.2 px | 0.00 | 0.00 | 4 |
| stroke 212 | 6 % → 0 % | 44.7 px | 0.00 | 0.00 | 2 |
| stroke 213 | 8 % → 0 % | 63.5 px | 0.00 | 0.00 | 4 |
| stroke 214 | 12 % → 0 % | 68.1 px | 0.00 | 0.00 | 6 |
| stroke 215 | 14 % → 0 % | 48.9 px | 0.00 | 0.00 | 31 |
| stroke 216 | 20 % → 0 % | 73.0 px | 0.00 | 0.00 | 44 |
| stroke 217 | 27 % → 0 % | 199.7 px | 0.00 | 0.00 | 5 |
| stroke 218 | 3 % → 0 % | 24.9 px | 0.00 | 0.00 | 1 |
| stroke 219 | 5 % → 0 % | 21.2 px | 0.00 | 0.00 | 4 |
| stroke 220 | 8 % → 0 % | 41.3 px | 0.00 | 0.00 | 4 |
| stroke 221 | 12 % → 0 % | 56.8 px | 0.31 | 0.02 | 11 |
| stroke 222 | 8 % → 0 % | 40.2 px | 0.00 | 0.00 | 13 |
| stroke 223 | 10 % → 0 % | 93.4 px | 0.00 | 0.00 | 2 |
| stroke 224 | 11 % → 0 % | 34.8 px | 0.00 | 0.00 | 26 |
| stroke 225 | 3 % → 0 % | 24.9 px | 0.00 | 0.00 | 3 |
| stroke 226 | 12 % → 0 % | 41.3 px | 0.00 | 0.00 | 13 |
| stroke 227 | 24 % → 0 % | 238.9 px | 0.00 | 0.00 | 3 |
| stroke 228 | 17 % → 0 % | 85.2 px | 0.00 | 0.00 | 6 |
| stroke 229 | 5 % → 0 % | 21.8 px | 0.00 | 0.00 | 11 |
| stroke 230 | 8 % → 0 % | 33.1 px | 0.00 | 0.00 | 16 |
| stroke 231 | 12 % → 0 % | 50.0 px | 0.00 | 0.00 | 8 |
| stroke 232 | 17 % → 0 % | 74.1 px | 0.00 | 0.00 | 4 |
| stroke 233 | 20 % → 0 % | 111.7 px | 0.00 | 0.00 | 8 |
| stroke 234 | 3 % → 0 % | 26.0 px | 0.00 | 0.00 | 2 |
| stroke 235 | 6 % → 0 % | 30.5 px | 0.00 | 0.00 | 3 |
| stroke 236 | 9 % → 0 % | 53.7 px | 0.00 | 0.00 | 10 |
| stroke 237 | 12 % → 0 % | 65.8 px | 0.00 | 0.00 | 8 |
| stroke 238 | 14 % → 0 % | 125.2 px | 0.00 | 0.00 | 3 |
| stroke 239 | 13 % → 0 % | 115.0 px | 0.00 | 0.00 | 2 |
| stroke 240 | 5 % → 0 % | 20.1 px | 0.00 | 0.00 | 9 |
| stroke 241 | 7 % → 0 % | 24.9 px | 0.00 | 0.00 | 16 |
| stroke 242 | 11 % → 0 % | 35.8 px | 0.00 | 0.00 | 36 |
| stroke 243 | 22 % → 0 % | 76.0 px | 0.00 | 0.00 | 19 |
| stroke 244 | 19 % → 0 % | 66.9 px | 0.00 | 0.00 | 13 |
| stroke 245 | 19 % → 0 % | 97.8 px | 0.00 | 0.00 | 6 |
| stroke 246 | 15 % → 0 % | 51.0 px | 0.00 | 0.00 | 10 |
| stroke 247 | 16 % → 0 % | 42.9 px | 0.00 | 0.00 | 13 |
| stroke 248 | 22 % → 0 % | 65.2 px | 0.00 | 0.00 | 11 |
| stroke 249 | 25 % → 0 % | 100.9 px | 0.00 | 0.00 | 11 |
| stroke 250 | 28 % → 0 % | 153.9 px | 0.00 | 0.00 | 7 |
| stroke 251 | 26 % → 0 % | 98.5 px | 0.00 | 0.00 | 10 |
| stroke 252 | 22 % → 0 % | 125.1 px | 0.00 | 0.00 | 4 |
| stroke 253 | 17 % → 0 % | 89.5 px | 0.32 | 0.02 | 3 |
| stroke 254 | 19 % → 3 % | 171.9 px | 0.36 | 0.15 | 1 |
| stroke 255 | 19 % → 2 % | 91.9 px | 0.36 | 0.11 | 7 |
| stroke 256 | 17 % → 2 % | 69.9 px | 0.36 | 0.14 | 8 |
| stroke 257 | 19 % → 3 % | 108.6 px | 0.36 | 0.14 | 6 |
| stroke 258 | 17 % → 2 % | 72.9 px | 0.36 | 0.14 | 4 |
| stroke 259 | 19 % → 0 % | 137.5 px | 0.00 | 0.00 | 2 |
| stroke 260 | 10 % → 0 % | 75.9 px | 0.00 | 0.00 | 3 |
| stroke 261 | 24 % → 1 % | 223.4 px | 0.37 | 0.03 | 3 |
| stroke 262 | 14 % → 0 % | 73.7 px | 0.38 | 0.03 | 2 |
| stroke 263 | 14 % → 2 % | 68.8 px | 0.37 | 0.15 | 8 |
| stroke 264 | 36 % → 3 % | 281.5 px | 0.36 | 0.08 | 1 |
| stroke 265 | 20 % → 3 % | 140.1 px | 0.36 | 0.14 | 3 |
| stroke 266 | 24 % → 3 % | 119.6 px | 0.36 | 0.10 | 3 |
| stroke 267 | 42 % → 3 % | 268.4 px | 0.36 | 0.07 | 2 |
| stroke 268 | 29 % → 3 % | 177.6 px | 0.36 | 0.09 | 2 |
| stroke 269 | 27 % → 3 % | 170.9 px | 0.36 | 0.10 | 4 |
| stroke 270 | 25 % → 3 % | 120.6 px | 0.36 | 0.10 | 7 |
| stroke 271 | 24 % → 3 % | 136.4 px | 0.36 | 0.11 | 3 |
| stroke 272 | 17 % → 2 % | 123.7 px | 0.36 | 0.13 | 2 |
| stroke 273 | 7 % → 0 % | 18.7 px | 0.00 | 0.00 | 8 |
| stroke 274 | 12 % → 0 % | 30.0 px | 0.00 | 0.00 | 18 |
| stroke 275 | 18 % → 0 % | 114.7 px | 0.00 | 0.00 | 2 |
| stroke 276 | 17 % → 0 % | 122.0 px | 0.00 | 0.00 | 4 |
| stroke 277 | 19 % → 0 % | 183.4 px | 0.00 | 0.00 | 1 |
| stroke 278 | 18 % → 0 % | 160.6 px | 0.00 | 0.00 | 1 |
| stroke 279 | 21 % → 0 % | 158.5 px | 0.00 | 0.00 | 3 |
| stroke 280 | 19 % → 0 % | 166.4 px | 0.00 | 0.00 | 11 |
| stroke 281 | 17 % → 0 % | 132.8 px | 0.00 | 0.00 | 4 |
| stroke 282 | 17 % → 0 % | 121.5 px | 0.00 | 0.00 | 6 |
| stroke 283 | 13 % → 0 % | 86.7 px | 0.00 | 0.00 | 2 |
| stroke 284 | 14 % → 0 % | 120.8 px | 0.00 | 0.00 | 3 |
| stroke 285 | 13 % → 0 % | 109.8 px | 0.00 | 0.00 | 3 |
| stroke 286 | 12 % → 0 % | 135.4 px | 0.00 | 0.00 | 2 |
| stroke 287 | 13 % → 0 % | 110.3 px | 0.00 | 0.00 | 3 |
| stroke 288 | 12 % → 0 % | 102.9 px | 0.00 | 0.00 | 1 |
| stroke 289 | 13 % → 0 % | 71.2 px | 0.00 | 0.00 | 5 |
| stroke 290 | 12 % → 0 % | 95.7 px | 0.00 | 0.00 | 1 |
| stroke 291 | 19 % → 0 % | 45.4 px | 0.00 | 0.00 | 17 |
| stroke 292 | 23 % → 0 % | 53.2 px | 0.00 | 0.00 | 16 |
| stroke 293 | 28 % → 0 % | 66.3 px | 0.00 | 0.00 | 13 |
| stroke 294 | 33 % → 0 % | 76.8 px | 0.00 | 0.00 | 18 |
| stroke 295 | 39 % → 0 % | 123.5 px | 0.00 | 0.00 | 15 |
| stroke 296 | 4 % → 0 % | 16.5 px | 0.00 | 0.00 | 10 |
| stroke 297 | 5 % → 0 % | 24.1 px | 0.00 | 0.00 | 6 |
| stroke 298 | 4 % → 0 % | 30.3 px | 0.00 | 0.00 | 6 |
| stroke 299 | 9 % → 0 % | 28.4 px | 0.00 | 0.00 | 18 |
| stroke 300 | 18 % → 0 % | 92.0 px | 0.00 | 0.00 | 3 |
| stroke 301 | 7 % → 0 % | 27.3 px | 0.00 | 0.00 | 12 |
| stroke 302 | 12 % → 0 % | 36.3 px | 0.00 | 0.00 | 10 |
| stroke 303 | 19 % → 0 % | 63.1 px | 0.00 | 0.00 | 11 |
| stroke 304 | 25 % → 0 % | 85.6 px | 0.00 | 0.00 | 18 |
| stroke 305 | 25 % → 0 % | 75.9 px | 0.00 | 0.00 | 91 |
| stroke 306 | 27 % → 0 % | 90.4 px | 0.00 | 0.00 | 39 |
| stroke 307 | 29 % → 0 % | 134.0 px | 0.00 | 0.00 | 26 |
| stroke 308 | 2 % → 0 % | 13.0 px | 0.00 | 0.00 | 4 |
| stroke 309 | 4 % → 26 % | 21.1 px | 0.37 | 6.40 | 3 |
| stroke 310 | 7 % → 25 % | 26.9 px | 0.36 | 3.56 | 21 |
| stroke 311 | 10 % → 22 % | 33.5 px | 0.36 | 2.17 | 14 |
| stroke 312 | 22 % → 42 % | 203.1 px | 0.37 | 1.89 | 2 |
| stroke 313 | 25 % → 47 % | 251.1 px | 0.37 | 1.84 | 1 |
| stroke 314 | 25 % → 45 % | 188.8 px | 0.36 | 1.79 | 4 |
| stroke 315 | 21 % → 33 % | 78.3 px | 0.36 | 1.56 | 16 |
| stroke 316 | 21 % → 34 % | 78.1 px | 0.37 | 1.64 | 23 |
| stroke 317 | 26 % → 40 % | 216.5 px | 0.36 | 1.54 | 1 |
| stroke 318 | 23 % → 43 % | 163.0 px | 0.37 | 1.86 | 2 |
| stroke 319 | 16 % → 39 % | 93.3 px | 0.37 | 2.39 | 5 |
| stroke 320 | 18 % → 35 % | 72.8 px | 0.37 | 1.90 | 10 |
| stroke 321 | 19 % → 35 % | 87.6 px | 0.37 | 1.87 | 8 |
| stroke 322 | 17 % → 34 % | 69.1 px | 0.37 | 2.02 | 12 |
| stroke 323 | 24 % → 38 % | 125.5 px | 0.37 | 1.60 | 6 |
| stroke 324 | 21 % → 40 % | 123.2 px | 0.37 | 1.87 | 7 |
| stroke 325 | 24 % → 30 % | 226.7 px | 0.37 | 1.24 | 2 |
| stroke 326 | 17 % → 35 % | 124.3 px | 0.37 | 2.11 | 11 |
| stroke 327 | 20 % → 28 % | 210.5 px | 0.37 | 1.37 | 1 |
| stroke 328 | 14 % → 28 % | 98.0 px | 0.37 | 2.08 | 7 |
| stroke 329 | 18 % → 28 % | 151.5 px | 0.37 | 1.60 | 2 |
| stroke 330 | 12 % → 23 % | 72.0 px | 0.37 | 1.95 | 12 |
| stroke 331 | 16 % → 25 % | 74.7 px | 0.37 | 1.61 | 15 |
| stroke 332 | 20 % → 27 % | 85.6 px | 0.37 | 1.35 | 23 |
| stroke 333 | 23 % → 26 % | 96.6 px | 0.37 | 1.14 | 10 |
| stroke 334 | 18 % → 18 % | 75.7 px | 0.37 | 1.00 | 7 |
| stroke 335 | 3 % → 3 % | 27.3 px | 0.36 | 1.00 | 2 |

Numbers say: wet paint spreads well beyond the stroke.

## Refs v3 · #43 Dragged black blocks — own sheet
own sheet 800 × 1115 · Ink 0.93 · Gouache 0.07 · 80 px · 25.5 s

![Refs v3 · #43 Dragged black blocks — own sheet](Refs-v3-43-Dragged-black-blocks-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 19 % → 0 % | 63.8 px | 0.00 | 0.00 | 667 |
| stroke 2 | 22 % → 0 % | 200.7 px | 0.00 | 0.00 | 175 |
| stroke 3 | 5 % → 0 % | 81.7 px | 0.00 | 0.00 | 129 |
| stroke 4 | 10 % → 0 % | 95.4 px | 0.00 | 0.00 | 523 |
| stroke 5 | 18 % → 0 % | 117.8 px | 0.00 | 0.00 | 620 |
| stroke 6 | 26 % → 0 % | 258.7 px | 0.00 | 0.00 | 571 |
| stroke 7 | 34 % → 0 % | 430.9 px | 0.00 | 0.00 | 132 |
| stroke 8 | 8 % → 0 % | 79.6 px | 0.00 | 0.00 | 124 |
| stroke 9 | 13 % → 0 % | 79.4 px | 0.00 | 0.00 | 274 |
| stroke 10 | 18 % → 0 % | 139.2 px | 0.00 | 0.00 | 159 |
| stroke 11 | 24 % → 0 % | 142.5 px | 0.00 | 0.00 | 233 |
| stroke 12 | 36 % → 0 % | 244.5 px | 0.00 | 0.00 | 198 |
| stroke 13 | 37 % → 0 % | 250.8 px | 0.00 | 0.00 | 269 |
| stroke 14 | 15 % → 0 % | 231.8 px | 0.24 | 0.01 | 74 |
| stroke 15 | 27 % → 0 % | 306.9 px | 0.00 | 0.00 | 117 |
| stroke 16 | 25 % → 0 % | 137.3 px | 0.26 | 0.01 | 442 |
| stroke 17 | 27 % → 0 % | 151.1 px | 0.00 | 0.00 | 357 |
| stroke 18 | 36 % → 0 % | 193.0 px | 0.00 | 0.00 | 366 |
| stroke 19 | 46 % → 0 % | 261.4 px | 0.00 | 0.00 | 302 |
| stroke 20 | 52 % → 0 % | 302.3 px | 0.00 | 0.00 | 316 |
| stroke 21 | 59 % → 0 % | 498.1 px | 0.00 | 0.00 | 90 |
| stroke 22 | 1 % → 2 % | 19.4 px | 0.31 | 1.81 | 13 |
| stroke 23 | 1 % → 1 % | 27.6 px | 0.32 | 1.47 | 6 |

Numbers say: wet paint spreads well beyond the stroke.

## Refs v3 · #44 Blue looping ribbon — own sheet
own sheet 800 × 1204 · Oil 0.52 · Gouache 0.48 + turpentine 10 % · 64 px · 64.2 s

![Refs v3 · #44 Blue looping ribbon — own sheet](Refs-v3-44-Blue-looping-ribbon-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 2 % → 53 % | 72.0 px | 0.61 | 22.12 | 113 |
| stroke 2 | 11 % → 27 % | 66.1 px | 0.61 | 2.48 | 282 |
| stroke 3 | 11 % → 34 % | 73.6 px | 0.61 | 3.13 | 371 |
| stroke 4 | 20 % → 45 % | 170.2 px | 0.61 | 2.25 | 287 |
| stroke 5 | 18 % → 42 % | 145.0 px | 0.61 | 2.39 | 135 |
| stroke 6 | 34 % → 45 % | 863.6 px | 0.61 | 1.33 | 34 |
| stroke 7 | 38 % → 41 % | 345.1 px | 0.61 | 1.06 | 159 |
| stroke 8 | 9 % → 34 % | 177.9 px | 0.62 | 4.03 | 57 |
| stroke 9 | 16 % → 43 % | 208.9 px | 0.62 | 2.78 | 123 |
| stroke 10 | 14 % → 34 % | 70.3 px | 0.62 | 2.52 | 151 |
| stroke 11 | 22 % → 22 % | 358.9 px | 0.62 | 1.02 | 39 |
| stroke 12 | 24 % → 34 % | 292.7 px | 0.62 | 1.40 | 68 |
| stroke 13 | 29 % → 24 % | 507.9 px | 0.62 | 0.80 | 57 |
| stroke 14 | 32 % → 48 % | 259.0 px | 0.62 | 1.50 | 79 |
| stroke 15 | 2 % → 67 % | 71.1 px | 0.62 | 26.98 | 14 |
| stroke 16 | 9 % → 64 % | 99.4 px | 0.62 | 7.12 | 90 |
| stroke 17 | 11 % → 67 % | 254.0 px | 0.62 | 6.30 | 47 |
| stroke 18 | 18 % → 63 % | 161.8 px | 0.62 | 3.40 | 139 |
| stroke 19 | 22 % → 61 % | 334.2 px | 0.61 | 2.75 | 46 |
| stroke 20 | 26 % → 62 % | 576.2 px | 0.61 | 2.37 | 26 |
| stroke 21 | 33 % → 62 % | 435.5 px | 0.61 | 1.91 | 83 |
| stroke 22 | 29 % → 66 % | 348.7 px | 0.62 | 2.31 | 107 |
| stroke 23 | 33 % → 69 % | 862.6 px | 0.62 | 2.13 | 22 |
| stroke 24 | 24 % → 56 % | 564.1 px | 0.62 | 2.33 | 21 |
| stroke 25 | 20 % → 65 % | 332.1 px | 0.62 | 3.17 | 48 |
| stroke 26 | 18 % → 62 % | 460.9 px | 0.62 | 3.38 | 18 |
| stroke 27 | 17 % → 64 % | 191.1 px | 0.62 | 3.74 | 56 |
| stroke 28 | 28 % → 60 % | 246.9 px | 0.62 | 2.10 | 163 |
| stroke 29 | 19 % → 53 % | 145.5 px | 0.62 | 2.74 | 38 |
| stroke 30 | 12 % → 68 % | 134.5 px | 0.62 | 5.81 | 62 |
| stroke 31 | 7 % → 69 % | 217.2 px | 0.63 | 10.64 | 14 |
| stroke 32 | 8 % → 51 % | 112.0 px | 0.61 | 5.99 | 24 |
| stroke 33 | 14 % → 48 % | 134.8 px | 0.61 | 3.50 | 38 |
| stroke 34 | 23 % → 48 % | 84.7 px | 0.61 | 2.12 | 372 |
| stroke 35 | 8 % → 35 % | 75.9 px | 0.63 | 4.32 | 80 |
| stroke 36 | 3 % → 77 % | 90.3 px | 0.61 | 22.62 | 23 |
| stroke 37 | 6 % → 75 % | 185.2 px | 0.61 | 13.42 | 16 |
| stroke 38 | 12 % → 54 % | 114.8 px | 0.62 | 4.54 | 98 |
| stroke 39 | 19 % → 50 % | 212.5 px | 0.61 | 2.62 | 84 |
| stroke 40 | 19 % → 65 % | 184.7 px | 0.61 | 3.35 | 143 |
| stroke 41 | 21 % → 36 % | 472.5 px | 0.62 | 1.74 | 37 |
| stroke 42 | 34 % → 38 % | 218.3 px | 0.62 | 1.12 | 228 |
| stroke 43 | 29 % → 34 % | 377.5 px | 0.62 | 1.18 | 91 |
| stroke 44 | 3 % → 61 % | 89.4 px | 0.61 | 21.59 | 17 |
| stroke 45 | 4 % → 44 % | 72.9 px | 0.61 | 10.80 | 76 |
| stroke 46 | 4 % → 32 % | 88.2 px | 0.61 | 8.59 | 50 |
| stroke 47 | 4 % → 41 % | 67.0 px | 0.62 | 9.67 | 93 |
| stroke 48 | 4 % → 61 % | 76.2 px | 0.62 | 13.95 | 86 |
| stroke 49 | 4 % → 41 % | 68.4 px | 0.62 | 10.18 | 41 |
| stroke 50 | 6 % → 36 % | 137.3 px | 0.61 | 5.95 | 63 |
| stroke 51 | 7 % → 60 % | 68.7 px | 0.62 | 8.97 | 103 |
| stroke 52 | 12 % → 56 % | 112.6 px | 0.62 | 4.75 | 192 |
| stroke 53 | 9 % → 53 % | 140.7 px | 0.61 | 5.83 | 65 |
| stroke 54 | 15 % → 61 % | 133.2 px | 0.62 | 3.94 | 157 |
| stroke 55 | 7 % → 63 % | 257.3 px | 0.61 | 9.12 | 20 |
| stroke 56 | 13 % → 36 % | 99.2 px | 0.61 | 2.76 | 310 |
| stroke 57 | 10 % → 59 % | 126.5 px | 0.61 | 6.10 | 107 |
| stroke 58 | 14 % → 40 % | 151.6 px | 0.62 | 2.84 | 127 |
| stroke 59 | 6 % → 62 % | 83.5 px | 0.62 | 10.91 | 156 |
| stroke 60 | 13 % → 53 % | 116.8 px | 0.61 | 4.13 | 103 |
| stroke 61 | 6 % → 71 % | 63.0 px | 0.62 | 11.80 | 129 |
| stroke 62 | 16 % → 61 % | 252.7 px | 0.61 | 3.95 | 59 |
| stroke 63 | 11 % → 73 % | 190.3 px | 0.62 | 6.58 | 59 |
| stroke 64 | 17 % → 63 % | 219.5 px | 0.62 | 3.80 | 50 |
| stroke 65 | 18 % → 68 % | 179.3 px | 0.62 | 3.79 | 130 |
| stroke 66 | 12 % → 64 % | 258.9 px | 0.62 | 5.20 | 23 |
| stroke 67 | 18 % → 64 % | 255.8 px | 0.62 | 3.49 | 46 |
| stroke 68 | 11 % → 56 % | 108.3 px | 0.62 | 5.08 | 73 |
| stroke 69 | 14 % → 50 % | 236.2 px | 0.61 | 3.49 | 53 |
| stroke 70 | 16 % → 59 % | 127.2 px | 0.62 | 3.75 | 85 |
| stroke 71 | 27 % → 61 % | 310.0 px | 0.61 | 2.30 | 70 |
| stroke 72 | 21 % → 51 % | 281.7 px | 0.62 | 2.37 | 48 |
| stroke 73 | 27 % → 71 % | 229.4 px | 0.62 | 2.64 | 179 |
| stroke 74 | 28 % → 59 % | 193.1 px | 0.63 | 2.07 | 154 |
| stroke 75 | 23 % → 67 % | 344.8 px | 0.61 | 2.91 | 59 |
| stroke 76 | 23 % → 59 % | 317.1 px | 0.61 | 2.53 | 92 |
| stroke 77 | 29 % → 60 % | 333.4 px | 0.61 | 2.07 | 77 |
| stroke 78 | 27 % → 65 % | 895.6 px | 0.61 | 2.42 | 13 |
| stroke 79 | 27 % → 61 % | 534.2 px | 0.62 | 2.28 | 50 |
| stroke 80 | 33 % → 47 % | 290.4 px | 0.62 | 1.42 | 64 |
| stroke 81 | 25 % → 56 % | 427.3 px | 0.61 | 2.24 | 40 |
| stroke 82 | 45 % → 74 % | 442.0 px | 0.61 | 1.65 | 103 |
| stroke 83 | 37 % → 72 % | 904.6 px | 0.62 | 1.94 | 42 |
| stroke 84 | 46 % → 56 % | 537.5 px | 0.62 | 1.22 | 139 |
| stroke 85 | 33 % → 56 % | 240.6 px | 0.62 | 1.69 | 100 |
| stroke 86 | 39 % → 69 % | 789.5 px | 0.62 | 1.76 | 36 |
| stroke 87 | 46 % → 74 % | 416.2 px | 0.62 | 1.63 | 154 |
| stroke 88 | 30 % → 60 % | 732.9 px | 0.61 | 2.00 | 34 |
| stroke 89 | 31 % → 57 % | 413.3 px | 0.62 | 1.84 | 166 |
| stroke 90 | 35 % → 46 % | 259.6 px | 0.61 | 1.33 | 149 |
| stroke 91 | 32 % → 64 % | 258.9 px | 0.62 | 2.02 | 192 |
| stroke 92 | 22 % → 55 % | 227.9 px | 0.62 | 2.49 | 98 |
| stroke 93 | 28 % → 53 % | 205.7 px | 0.62 | 1.88 | 274 |
| stroke 94 | 31 % → 45 % | 268.0 px | 0.62 | 1.45 | 190 |
| stroke 95 | 41 % → 64 % | 824.0 px | 0.62 | 1.54 | 58 |
| stroke 96 | 42 % → 64 % | 381.1 px | 0.62 | 1.53 | 135 |
| stroke 97 | 51 % → 63 % | 766.8 px | 0.62 | 1.24 | 70 |
| stroke 98 | 45 % → 71 % | 612.4 px | 0.62 | 1.57 | 73 |
| stroke 99 | 34 % → 53 % | 298.5 px | 0.62 | 1.55 | 135 |
| stroke 100 | 60 % → 68 % | 861.1 px | 0.61 | 1.12 | 85 |
| stroke 101 | 43 % → 51 % | 360.0 px | 0.61 | 1.19 | 259 |
| stroke 102 | 47 % → 66 % | 696.5 px | 0.62 | 1.39 | 36 |
| stroke 103 | 53 % → 68 % | 823.5 px | 0.62 | 1.28 | 72 |
| stroke 104 | 41 % → 58 % | 395.7 px | 0.61 | 1.43 | 97 |
| stroke 105 | 42 % → 53 % | 759.3 px | 0.61 | 1.28 | 67 |
| stroke 106 | 46 % → 50 % | 359.0 px | 0.62 | 1.09 | 296 |
| stroke 107 | 46 % → 60 % | 471.4 px | 0.61 | 1.32 | 97 |
| stroke 108 | 49 % → 65 % | 989.6 px | 0.61 | 1.34 | 38 |
| stroke 109 | 45 % → 58 % | 485.3 px | 0.63 | 1.30 | 100 |
| stroke 110 | 39 % → 60 % | 1473.7 px | 0.61 | 1.52 | 7 |
| stroke 111 | 58 % → 70 % | 1250.9 px | 0.62 | 1.20 | 35 |
| stroke 112 | 41 % → 61 % | 337.7 px | 0.62 | 1.51 | 79 |
| stroke 113 | 42 % → 48 % | 394.1 px | 0.63 | 1.13 | 86 |
| stroke 114 | 60 % → 64 % | 986.2 px | 0.61 | 1.07 | 55 |
| stroke 115 | 44 % → 54 % | 552.3 px | 0.61 | 1.21 | 85 |
| stroke 116 | 52 % → 54 % | 1408.9 px | 0.63 | 1.03 | 13 |
| stroke 117 | 55 % → 57 % | 890.0 px | 0.62 | 1.04 | 46 |
| stroke 118 | 53 % → 59 % | 579.1 px | 0.62 | 1.12 | 99 |
| stroke 119 | 61 % → 66 % | 572.2 px | 0.62 | 1.08 | 120 |
| stroke 120 | 45 % → 57 % | 402.4 px | 0.62 | 1.25 | 115 |
| stroke 121 | 52 % → 60 % | 587.2 px | 0.62 | 1.14 | 43 |
| stroke 122 | 50 % → 51 % | 817.2 px | 0.61 | 1.02 | 45 |
| stroke 123 | 53 % → 63 % | 911.6 px | 0.62 | 1.19 | 37 |
| stroke 124 | 68 % → 68 % | 756.5 px | 0.62 | 1.00 | 118 |
| stroke 125 | 70 % → 73 % | 1596.2 px | 0.61 | 1.04 | 30 |
| stroke 126 | 52 % → 52 % | 517.7 px | 0.62 | 1.00 | 83 |
| stroke 127 | 69 % → 69 % | 914.5 px | 0.61 | 1.00 | 106 |
| stroke 128 | 61 % → 62 % | 580.9 px | 0.62 | 1.02 | 256 |
| stroke 129 | 69 % → 70 % | 1291.5 px | 0.62 | 1.00 | 56 |
| stroke 130 | 27 % → 27 % | 365.5 px | 0.61 | 1.00 | 61 |

Numbers say: wet paint spreads well beyond the stroke.

## Refs v3 · #45 Pastel pepper — own sheet
own sheet 800 × 800 · Pastel 1.00 · 46 px · 22.5 s

![Refs v3 · #45 Pastel pepper — own sheet](Refs-v3-45-Pastel-pepper-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 5 % → 5 % | 37.9 px | 0.19 | 1.11 | 27 |
| stroke 2 | 6 % → 0 % | 43.2 px | 0.00 | 0.00 | 25 |
| stroke 3 | 12 % → 3 % | 42.9 px | 0.19 | 0.23 | 299 |
| stroke 4 | 18 % → 6 % | 85.8 px | 0.19 | 0.35 | 73 |
| stroke 5 | 22 % → 0 % | 96.3 px | 0.20 | 0.01 | 81 |
| stroke 6 | 21 % → 6 % | 141.3 px | 0.19 | 0.29 | 41 |
| stroke 7 | 31 % → 0 % | 212.0 px | 0.00 | 0.00 | 35 |
| stroke 8 | 25 % → 6 % | 217.7 px | 0.19 | 0.23 | 25 |
| stroke 9 | 27 % → 6 % | 262.0 px | 0.19 | 0.21 | 22 |
| stroke 10 | 11 % → 0 % | 58.5 px | 0.00 | 0.00 | 51 |
| stroke 11 | 17 % → 0 % | 111.3 px | 0.00 | 0.00 | 25 |
| stroke 12 | 20 % → 0 % | 124.0 px | 0.00 | 0.00 | 23 |
| stroke 13 | 21 % → 0 % | 107.5 px | 0.00 | 0.00 | 37 |
| stroke 14 | 23 % → 0 % | 111.0 px | 0.00 | 0.00 | 59 |
| stroke 15 | 25 % → 0 % | 117.0 px | 0.00 | 0.00 | 105 |
| stroke 16 | 26 % → 0 % | 115.6 px | 0.00 | 0.00 | 91 |
| stroke 17 | 28 % → 0 % | 122.8 px | 0.00 | 0.00 | 120 |
| stroke 18 | 28 % → 0 % | 131.4 px | 0.19 | 0.01 | 154 |
| stroke 19 | 27 % → 1 % | 131.9 px | 0.19 | 0.03 | 261 |
| stroke 20 | 29 % → 1 % | 150.9 px | 0.19 | 0.03 | 317 |
| stroke 21 | 19 % → 1 % | 102.0 px | 0.19 | 0.07 | 216 |
| stroke 22 | 37 % → 0 % | 315.1 px | 0.00 | 0.00 | 39 |
| stroke 23 | 20 % → 2 % | 105.6 px | 0.19 | 0.12 | 198 |
| stroke 24 | 30 % → 3 % | 161.7 px | 0.19 | 0.09 | 138 |
| stroke 25 | 37 % → 2 % | 207.0 px | 0.19 | 0.06 | 103 |
| stroke 26 | 39 % → 2 % | 229.5 px | 0.19 | 0.05 | 84 |
| stroke 27 | 38 % → 1 % | 268.6 px | 0.19 | 0.02 | 52 |
| stroke 28 | 34 % → 0 % | 341.2 px | 0.18 | 0.00 | 30 |
| stroke 29 | 22 % → 1 % | 253.5 px | 0.19 | 0.04 | 29 |
| stroke 30 | 17 % → 5 % | 174.6 px | 0.19 | 0.28 | 59 |
| stroke 31 | 17 % → 4 % | 164.5 px | 0.19 | 0.22 | 37 |
| stroke 32 | 25 % → 1 % | 260.0 px | 0.19 | 0.03 | 74 |
| stroke 33 | 29 % → 3 % | 128.8 px | 0.19 | 0.09 | 111 |
| stroke 34 | 35 % → 2 % | 152.8 px | 0.19 | 0.05 | 107 |
| stroke 35 | 44 % → 1 % | 213.1 px | 0.19 | 0.02 | 63 |
| stroke 36 | 4 % → 4 % | 20.4 px | 0.19 | 0.87 | 45 |
| stroke 37 | 5 % → 0 % | 22.3 px | 0.00 | 0.00 | 57 |
| stroke 38 | 9 % → 0 % | 33.8 px | 0.17 | 0.03 | 30 |
| stroke 39 | 12 % → 1 % | 44.6 px | 0.19 | 0.08 | 161 |
| stroke 40 | 15 % → 1 % | 187.7 px | 0.18 | 0.07 | 9 |
| stroke 41 | 17 % → 1 % | 133.9 px | 0.19 | 0.08 | 13 |
| stroke 42 | 13 % → 2 % | 132.2 px | 0.19 | 0.14 | 13 |
| stroke 43 | 18 % → 0 % | 205.2 px | 0.19 | 0.01 | 15 |
| stroke 44 | 12 % → 2 % | 108.0 px | 0.19 | 0.20 | 10 |
| stroke 45 | 16 % → 4 % | 151.7 px | 0.19 | 0.25 | 12 |
| stroke 46 | 21 % → 5 % | 302.7 px | 0.19 | 0.25 | 14 |
| stroke 47 | 6 % → 0 % | 61.9 px | 0.19 | 0.09 | 19 |
| stroke 48 | 6 % → 2 % | 73.4 px | 0.19 | 0.24 | 4 |
| stroke 49 | 7 % → 0 % | 44.8 px | 0.00 | 0.00 | 82 |
| stroke 50 | 12 % → 0 % | 78.5 px | 0.00 | 0.00 | 106 |
| stroke 51 | 6 % → 3 % | 49.0 px | 0.19 | 0.58 | 38 |
| stroke 52 | 10 % → 3 % | 62.5 px | 0.19 | 0.34 | 89 |
| stroke 53 | 14 % → 3 % | 77.2 px | 0.19 | 0.24 | 155 |
| stroke 54 | 19 % → 2 % | 99.3 px | 0.19 | 0.13 | 254 |
| stroke 55 | 31 % → 4 % | 189.0 px | 0.19 | 0.11 | 162 |
| stroke 56 | 22 % → 4 % | 178.1 px | 0.19 | 0.18 | 145 |
| stroke 57 | 44 % → 5 % | 380.9 px | 0.19 | 0.12 | 45 |
| stroke 58 | 21 % → 4 % | 251.6 px | 0.19 | 0.19 | 30 |
| stroke 59 | 10 % → 1 % | 47.1 px | 0.19 | 0.15 | 49 |
| stroke 60 | 8 % → 0 % | 36.7 px | 0.00 | 0.00 | 49 |
| stroke 61 | 13 % → 0 % | 47.3 px | 0.00 | 0.00 | 133 |
| stroke 62 | 22 % → 0 % | 110.9 px | 0.00 | 0.00 | 109 |
| stroke 63 | 25 % → 0 % | 192.6 px | 0.00 | 0.00 | 40 |
| stroke 64 | 29 % → 0 % | 231.1 px | 0.00 | 0.00 | 95 |
| stroke 65 | 26 % → 0 % | 230.1 px | 0.00 | 0.00 | 37 |
| stroke 66 | 20 % → 0 % | 156.6 px | 0.00 | 0.00 | 28 |
| stroke 67 | 17 % → 0 % | 101.7 px | 0.00 | 0.00 | 45 |
| stroke 68 | 19 % → 0 % | 106.2 px | 0.00 | 0.00 | 48 |
| stroke 69 | 21 % → 0 % | 119.0 px | 0.19 | 0.01 | 47 |
| stroke 70 | 22 % → 1 % | 125.9 px | 0.19 | 0.06 | 64 |
| stroke 71 | 24 % → 2 % | 133.2 px | 0.19 | 0.09 | 58 |
| stroke 72 | 24 % → 3 % | 139.1 px | 0.19 | 0.13 | 49 |
| stroke 73 | 23 % → 4 % | 146.3 px | 0.19 | 0.19 | 50 |
| stroke 74 | 24 % → 6 % | 195.1 px | 0.19 | 0.26 | 27 |
| stroke 75 | 21 % → 8 % | 183.7 px | 0.19 | 0.39 | 27 |
| stroke 76 | 21 % → 9 % | 209.8 px | 0.19 | 0.43 | 20 |
| stroke 77 | 20 % → 8 % | 216.4 px | 0.19 | 0.39 | 17 |
| stroke 78 | 21 % → 7 % | 211.8 px | 0.19 | 0.33 | 17 |
| stroke 79 | 28 % → 6 % | 326.2 px | 0.19 | 0.22 | 16 |
| stroke 80 | 33 % → 5 % | 355.2 px | 0.19 | 0.14 | 16 |
| stroke 81 | 22 % → 5 % | 63.2 px | 0.19 | 0.22 | 223 |
| stroke 82 | 39 % → 4 % | 231.1 px | 0.19 | 0.10 | 63 |
| stroke 83 | 38 % → 0 % | 312.0 px | 0.21 | 0.00 | 33 |
| stroke 84 | 39 % → 0 % | 173.0 px | 0.20 | 0.01 | 112 |
| stroke 85 | 33 % → 0 % | 327.2 px | 0.00 | 0.00 | 18 |
| stroke 86 | 40 % → 1 % | 157.0 px | 0.19 | 0.03 | 176 |
| stroke 87 | 41 % → 1 % | 163.3 px | 0.19 | 0.03 | 194 |
| stroke 88 | 44 % → 1 % | 174.1 px | 0.19 | 0.03 | 174 |
| stroke 89 | 47 % → 2 % | 196.4 px | 0.19 | 0.03 | 137 |
| stroke 90 | 7 % → 0 % | 41.5 px | 0.00 | 0.00 | 50 |
| stroke 91 | 16 % → 0 % | 68.9 px | 0.00 | 0.00 | 120 |
| stroke 92 | 25 % → 0 % | 101.0 px | 0.00 | 0.00 | 149 |
| stroke 93 | 40 % → 0 % | 158.6 px | 0.00 | 0.00 | 80 |
| stroke 94 | 33 % → 0 % | 221.1 px | 0.00 | 0.00 | 40 |
| stroke 95 | 2 % → 2 % | 20.5 px | 0.19 | 1.21 | 7 |
| stroke 96 | 3 % → 3 % | 29.2 px | 0.19 | 1.15 | 3 |
| stroke 97 | 4 % → 4 % | 38.2 px | 0.19 | 1.00 | 7 |
| stroke 98 | 6 % → 5 % | 31.2 px | 0.19 | 0.76 | 15 |
| stroke 99 | 10 % → 4 % | 217.7 px | 0.19 | 0.36 | 1 |
| stroke 100 | 14 % → 6 % | 141.5 px | 0.19 | 0.39 | 3 |
| stroke 101 | 2 % → 0 % | 20.5 px | 0.00 | 0.00 | 13 |
| stroke 102 | 3 % → 0 % | 72.5 px | 0.00 | 0.00 | 1 |
| stroke 103 | 4 % → 0 % | 48.9 px | 0.00 | 0.00 | 5 |
| stroke 104 | 6 % → 0 % | 69.4 px | 0.00 | 0.00 | 4 |
| stroke 105 | 8 % → 0 % | 148.4 px | 0.00 | 0.00 | 3 |
| stroke 106 | 8 % → 0 % | 78.3 px | 0.00 | 0.00 | 5 |
| stroke 107 | 10 % → 0 % | 133.5 px | 0.00 | 0.00 | 4 |
| stroke 108 | 7 % → 1 % | 50.3 px | 0.20 | 0.10 | 8 |
| stroke 109 | 11 % → 0 % | 120.9 px | 0.00 | 0.00 | 4 |
| stroke 110 | 5 % → 2 % | 28.4 px | 0.19 | 0.37 | 27 |
| stroke 111 | 12 % → 0 % | 136.2 px | 0.00 | 0.00 | 6 |
| stroke 112 | 6 % → 4 % | 64.8 px | 0.19 | 0.59 | 9 |
| stroke 113 | 14 % → 0 % | 138.2 px | 0.00 | 0.00 | 10 |
| stroke 114 | 7 % → 4 % | 49.2 px | 0.19 | 0.55 | 15 |
| stroke 115 | 14 % → 0 % | 136.4 px | 0.00 | 0.00 | 8 |
| stroke 116 | 9 % → 3 % | 71.1 px | 0.19 | 0.34 | 10 |
| stroke 117 | 13 % → 0 % | 134.2 px | 0.00 | 0.00 | 4 |
| stroke 118 | 10 % → 3 % | 71.2 px | 0.19 | 0.26 | 16 |
| stroke 119 | 13 % → 0 % | 148.0 px | 0.00 | 0.00 | 6 |
| stroke 120 | 12 % → 2 % | 83.5 px | 0.19 | 0.16 | 10 |
| stroke 121 | 14 % → 0 % | 141.2 px | 0.00 | 0.00 | 51 |
| stroke 122 | 13 % → 1 % | 103.6 px | 0.19 | 0.10 | 28 |
| stroke 123 | 15 % → 0 % | 221.0 px | 0.00 | 0.00 | 13 |
| stroke 124 | 15 % → 1 % | 107.4 px | 0.19 | 0.06 | 16 |
| stroke 125 | 15 % → 0 % | 161.6 px | 0.00 | 0.00 | 10 |
| stroke 126 | 18 % → 1 % | 323.1 px | 0.19 | 0.04 | 9 |
| stroke 127 | 21 % → 0 % | 313.8 px | 0.20 | 0.01 | 2 |
| stroke 128 | 15 % → 0 % | 177.8 px | 0.00 | 0.00 | 6 |
| stroke 129 | 20 % → 0 % | 401.8 px | 0.19 | 0.01 | 2 |
| stroke 130 | 23 % → 1 % | 393.3 px | 0.20 | 0.03 | 2 |
| stroke 131 | 12 % → 1 % | 97.9 px | 0.19 | 0.09 | 14 |
| stroke 132 | 21 % → 0 % | 377.4 px | 0.00 | 0.00 | 6 |
| stroke 133 | 23 % → 1 % | 403.3 px | 0.19 | 0.04 | 5 |
| stroke 134 | 22 % → 0 % | 487.6 px | 0.00 | 0.00 | 3 |
| stroke 135 | 21 % → 1 % | 425.6 px | 0.20 | 0.03 | 4 |
| stroke 136 | 23 % → 0 % | 436.6 px | 0.00 | 0.00 | 2 |
| stroke 137 | 19 % → 0 % | 307.4 px | 0.19 | 0.01 | 3 |
| stroke 138 | 22 % → 0 % | 418.8 px | 0.00 | 0.00 | 3 |
| stroke 139 | 15 % → 1 % | 135.7 px | 0.19 | 0.09 | 13 |
| stroke 140 | 23 % → 0 % | 381.3 px | 0.00 | 0.00 | 3 |
| stroke 141 | 18 % → 0 % | 385.8 px | 0.00 | 0.00 | 6 |
| stroke 142 | 22 % → 0 % | 349.6 px | 0.00 | 0.00 | 4 |
| stroke 143 | 14 % → 1 % | 119.3 px | 0.19 | 0.07 | 16 |
| stroke 144 | 13 % → 2 % | 107.7 px | 0.19 | 0.13 | 22 |
| stroke 145 | 2 % → 4 % | 17.1 px | 0.19 | 2.16 | 8 |
| stroke 146 | 3 % → 3 % | 33.1 px | 0.19 | 0.80 | 16 |
| stroke 147 | 5 % → 1 % | 56.3 px | 0.19 | 0.29 | 12 |
| stroke 148 | 6 % → 1 % | 57.1 px | 0.19 | 0.19 | 11 |
| stroke 149 | 1 % → 0 % | 24.4 px | 0.00 | 0.00 | 9 |
| stroke 150 | 4 % → 0 % | 23.5 px | 0.00 | 0.00 | 15 |
| stroke 151 | 6 % → 0 % | 32.0 px | 0.00 | 0.00 | 29 |
| stroke 152 | 9 % → 0 % | 46.2 px | 0.00 | 0.00 | 37 |
| stroke 153 | 17 % → 0 % | 134.8 px | 0.00 | 0.00 | 8 |
| stroke 154 | 13 % → 0 % | 98.6 px | 0.00 | 0.00 | 18 |
| stroke 155 | 18 % → 0 % | 179.9 px | 0.00 | 0.00 | 7 |
| stroke 156 | 13 % → 0 % | 106.7 px | 0.00 | 0.00 | 13 |
| stroke 157 | 19 % → 0 % | 343.4 px | 0.00 | 0.00 | 2 |
| stroke 158 | 13 % → 0 % | 189.3 px | 0.00 | 0.00 | 10 |
| stroke 159 | 13 % → 0 % | 183.9 px | 0.00 | 0.00 | 3 |
| stroke 160 | 17 % → 0 % | 273.5 px | 0.00 | 0.00 | 4 |
| stroke 161 | 14 % → 0 % | 197.3 px | 0.00 | 0.00 | 2 |
| stroke 162 | 17 % → 0 % | 257.8 px | 0.00 | 0.00 | 1 |
| stroke 163 | 14 % → 0 % | 165.2 px | 0.00 | 0.00 | 3 |
| stroke 164 | 15 % → 0 % | 225.3 px | 0.00 | 0.00 | 2 |
| stroke 165 | 15 % → 0 % | 218.6 px | 0.00 | 0.00 | 13 |
| stroke 166 | 14 % → 0 % | 192.7 px | 0.00 | 0.00 | 4 |
| stroke 167 | 14 % → 0 % | 191.9 px | 0.00 | 0.00 | 10 |
| stroke 168 | 2 % → 0 % | 18.0 px | 0.00 | 0.00 | 13 |
| stroke 169 | 4 % → 0 % | 39.5 px | 0.00 | 0.00 | 5 |
| stroke 170 | 6 % → 0 % | 118.9 px | 0.00 | 0.00 | 1 |
| stroke 171 | 7 % → 0 % | 58.6 px | 0.00 | 0.00 | 8 |
| stroke 172 | 7 % → 1 % | 59.6 px | 0.20 | 0.10 | 12 |
| stroke 173 | 7 % → 3 % | 57.2 px | 0.19 | 0.44 | 18 |
| stroke 174 | 7 % → 4 % | 90.6 px | 0.19 | 0.61 | 13 |
| stroke 175 | 13 % → 2 % | 73.1 px | 0.19 | 0.16 | 34 |
| stroke 176 | 2 % → 0 % | 44.0 px | 0.00 | 0.00 | 7 |
| stroke 177 | 13 % → 5 % | 104.3 px | 0.19 | 0.38 | 7 |
| stroke 178 | 20 % → 2 % | 164.1 px | 0.19 | 0.08 | 14 |
| stroke 179 | 17 % → 0 % | 91.0 px | 0.00 | 0.00 | 35 |
| stroke 180 | 16 % → 0 % | 150.6 px | 0.00 | 0.00 | 13 |
| stroke 181 | 2 % → 5 % | 26.2 px | 0.19 | 2.57 | 8 |
| stroke 182 | 4 % → 4 % | 26.7 px | 0.19 | 1.00 | 17 |
| stroke 183 | 4 % → 5 % | 20.4 px | 0.19 | 1.31 | 29 |
| stroke 184 | 7 % → 7 % | 57.8 px | 0.19 | 1.00 | 9 |
| stroke 185 | 3 % → 3 % | 21.4 px | 0.19 | 1.00 | 16 |

Numbers say: wet paint spreads well beyond the stroke.

## Refs v3 · #46 Ink lips on wet paper — own sheet
own sheet 800 × 1047 · Watercolour 1.00 + water 65 % · 56 px · 22.4 s

![Refs v3 · #46 Ink lips on wet paper — own sheet](Refs-v3-46-Ink-lips-on-wet-paper-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 14 % → 22 % | 61.2 px | 0.59 | 1.54 | 396 |
| stroke 2 | 13 % → 21 % | 59.9 px | 0.60 | 1.57 | 300 |

Numbers say: wet paint spreads well beyond the stroke.

## Refs v3 · #47 Pink knife slabs — own sheet
own sheet 800 × 1014 · Gouache 1.00 + water 15 % · 240 px · 41.4 s

![Refs v3 · #47 Pink knife slabs — own sheet](Refs-v3-47-Pink-knife-slabs-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 26 % → 28 % | 127.5 px | 0.08 | 1.10 | 5655 |
| stroke 2 | 45 % → 30 % | 315.5 px | 0.08 | 0.67 | 5301 |
| stroke 3 | 54 % → 31 % | 481.6 px | 0.08 | 0.57 | 6783 |
| stroke 4 | 64 % → 30 % | 451.0 px | 0.08 | 0.47 | 5490 |
| stroke 5 | 82 % → 29 % | 422.8 px | 0.08 | 0.36 | 3703 |
| stroke 6 | 17 % → 31 % | 161.2 px | 0.08 | 1.79 | 133 |
| stroke 7 | 26 % → 32 % | 321.7 px | 0.08 | 1.25 | 294 |
| stroke 8 | 35 % → 32 % | 444.7 px | 0.08 | 0.91 | 287 |
| stroke 9 | 46 % → 31 % | 443.7 px | 0.08 | 0.68 | 211 |

Numbers say: wet paint spreads well beyond the stroke.

## Refs v3 · #48 Black bands with drips — own sheet
own sheet 800 × 1045 · Watercolour 1.00 + water 35 % · 80 px · 35.7 s

![Refs v3 · #48 Black bands with drips — own sheet](Refs-v3-48-Black-bands-with-drips-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 17 % → 95 % | 64.7 px | 0.32 | 5.72 | 138 |
| stroke 2 | 18 % → 93 % | 85.3 px | 0.31 | 5.29 | 245 |
| stroke 3 | 35 % → 89 % | 87.3 px | 0.31 | 2.56 | 1392 |
| stroke 4 | 45 % → 91 % | 131.1 px | 0.30 | 2.02 | 853 |
| stroke 5 | 50 % → 92 % | 203.2 px | 0.31 | 1.85 | 723 |
| stroke 6 | 55 % → 96 % | 218.2 px | 0.31 | 1.75 | 1109 |
| stroke 7 | 55 % → 95 % | 191.9 px | 0.30 | 1.73 | 728 |
| stroke 8 | 55 % → 95 % | 193.0 px | 0.30 | 1.72 | 910 |
| stroke 9 | 56 % → 95 % | 196.9 px | 0.30 | 1.69 | 828 |
| stroke 10 | 57 % → 99 % | 246.9 px | 0.30 | 1.74 | 556 |
| stroke 11 | 55 % → 97 % | 253.3 px | 0.30 | 1.75 | 525 |
| stroke 12 | 55 % → 97 % | 208.4 px | 0.30 | 1.75 | 658 |
| stroke 13 | 55 % → 96 % | 192.3 px | 0.30 | 1.73 | 754 |
| stroke 14 | 56 % → 92 % | 193.8 px | 0.30 | 1.65 | 690 |
| stroke 15 | 56 % → 82 % | 217.8 px | 0.30 | 1.47 | 864 |
| stroke 16 | 57 % → 71 % | 199.4 px | 0.30 | 1.23 | 886 |
| stroke 17 | 56 % → 60 % | 245.0 px | 0.30 | 1.07 | 889 |
| stroke 18 | 51 % → 53 % | 454.2 px | 0.29 | 1.05 | 111 |

Numbers say: wet paint spreads well beyond the stroke.

## Refs v3 · #49 Magenta letters round — own sheet
own sheet 800 × 1000 · Ink 0.98 · 64 px · 23.0 s

![Refs v3 · #49 Magenta letters round — own sheet](Refs-v3-49-Magenta-letters-round-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 2 % → 31 % | 49.2 px | 0.47 | 14.24 | 26 |
| stroke 2 | 4 % → 28 % | 123.4 px | 0.47 | 7.67 | 8 |
| stroke 3 | 4 % → 22 % | 59.9 px | 0.48 | 5.38 | 17 |
| stroke 4 | 8 % → 26 % | 103.5 px | 0.48 | 3.11 | 26 |
| stroke 5 | 16 % → 29 % | 97.4 px | 0.47 | 1.81 | 75 |
| stroke 6 | 8 % → 27 % | 51.8 px | 0.45 | 3.50 | 53 |
| stroke 7 | 19 % → 33 % | 134.3 px | 0.46 | 1.74 | 59 |
| stroke 8 | 4 % → 38 % | 65.8 px | 0.47 | 8.43 | 35 |
| stroke 9 | 8 % → 39 % | 127.7 px | 0.47 | 4.76 | 38 |
| stroke 10 | 12 % → 29 % | 148.1 px | 0.47 | 2.44 | 54 |
| stroke 11 | 16 % → 34 % | 275.5 px | 0.48 | 2.10 | 26 |
| stroke 12 | 18 % → 32 % | 211.2 px | 0.48 | 1.83 | 42 |
| stroke 13 | 31 % → 37 % | 159.8 px | 0.47 | 1.19 | 140 |
| stroke 14 | 20 % → 29 % | 58.6 px | 0.49 | 1.45 | 827 |
| stroke 15 | 9 % → 37 % | 203.1 px | 0.47 | 3.86 | 26 |
| stroke 16 | 16 % → 37 % | 116.4 px | 0.47 | 2.36 | 65 |
| stroke 17 | 25 % → 37 % | 240.2 px | 0.47 | 1.52 | 61 |
| stroke 18 | 25 % → 39 % | 393.4 px | 0.47 | 1.55 | 31 |
| stroke 19 | 26 % → 39 % | 262.6 px | 0.47 | 1.52 | 60 |
| stroke 20 | 14 % → 37 % | 507.2 px | 0.48 | 2.72 | 7 |
| stroke 21 | 23 % → 40 % | 105.0 px | 0.47 | 1.77 | 299 |
| stroke 22 | 19 % → 40 % | 144.3 px | 0.47 | 2.14 | 77 |
| stroke 23 | 14 % → 43 % | 160.0 px | 0.47 | 3.09 | 95 |
| stroke 24 | 9 % → 44 % | 89.1 px | 0.47 | 4.85 | 69 |
| stroke 25 | 22 % → 32 % | 267.4 px | 0.47 | 1.48 | 36 |
| stroke 26 | 30 % → 35 % | 363.8 px | 0.47 | 1.18 | 52 |
| stroke 27 | 29 % → 34 % | 354.6 px | 0.46 | 1.19 | 29 |
| stroke 28 | 6 % → 48 % | 62.3 px | 0.48 | 7.99 | 39 |
| stroke 29 | 27 % → 38 % | 137.3 px | 0.47 | 1.39 | 155 |
| stroke 30 | 33 % → 41 % | 209.7 px | 0.47 | 1.24 | 76 |
| stroke 31 | 25 % → 38 % | 74.5 px | 0.47 | 1.54 | 319 |
| stroke 32 | 26 % → 42 % | 95.6 px | 0.48 | 1.62 | 223 |
| stroke 33 | 18 % → 40 % | 291.2 px | 0.48 | 2.27 | 41 |
| stroke 34 | 11 % → 40 % | 128.6 px | 0.48 | 3.82 | 65 |
| stroke 35 | 29 % → 37 % | 198.3 px | 0.47 | 1.29 | 105 |
| stroke 36 | 28 % → 36 % | 312.0 px | 0.47 | 1.29 | 49 |
| stroke 37 | 11 % → 32 % | 92.7 px | 0.48 | 2.84 | 37 |
| stroke 38 | 23 % → 38 % | 266.0 px | 0.47 | 1.62 | 47 |
| stroke 39 | 21 % → 32 % | 178.6 px | 0.47 | 1.52 | 34 |
| stroke 40 | 9 % → 24 % | 162.4 px | 0.49 | 2.70 | 14 |
| stroke 41 | 20 % → 32 % | 257.4 px | 0.48 | 1.63 | 23 |
| stroke 42 | 27 % → 31 % | 203.2 px | 0.47 | 1.14 | 112 |
| stroke 43 | 25 % → 27 % | 575.8 px | 0.48 | 1.09 | 9 |
| stroke 44 | 36 % → 38 % | 285.4 px | 0.48 | 1.07 | 99 |

Numbers say: wet paint spreads well beyond the stroke.

## Refs v3 · #50 Swipes on seaside — own sheet
own sheet 800 × 1160 · Gouache 1.00 + water 15 % · 57 px · 46.4 s

![Refs v3 · #50 Swipes on seaside — own sheet](Refs-v3-50-Swipes-on-seaside-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 11 % → 0 % | 57.3 px | 0.00 | 0.00 | 137 |
| stroke 2 | 17 % → 0 % | 148.7 px | 0.00 | 0.00 | 60 |
| stroke 3 | 12 % → 0 % | 55.4 px | 0.00 | 0.00 | 140 |
| stroke 4 | 24 % → 0 % | 197.9 px | 0.00 | 0.00 | 54 |
| stroke 5 | 7 % → 0 % | 57.6 px | 0.00 | 0.00 | 58 |
| stroke 6 | 15 % → 0 % | 78.2 px | 0.00 | 0.00 | 154 |
| stroke 7 | 30 % → 0 % | 94.3 px | 0.00 | 0.00 | 484 |
| stroke 8 | 36 % → 0 % | 206.1 px | 0.00 | 0.00 | 70 |
| stroke 9 | 37 % → 0 % | 127.4 px | 0.00 | 0.00 | 314 |
| stroke 10 | 42 % → 0 % | 161.4 px | 0.00 | 0.00 | 203 |
| stroke 11 | 40 % → 0 % | 200.6 px | 0.00 | 0.00 | 101 |
| stroke 12 | 44 % → 2 % | 163.9 px | 0.40 | 0.05 | 192 |
| stroke 13 | 42 % → 2 % | 173.2 px | 0.44 | 0.04 | 150 |
| stroke 14 | 42 % → 11 % | 148.2 px | 0.44 | 0.25 | 327 |
| stroke 15 | 44 % → 12 % | 166.7 px | 0.44 | 0.27 | 194 |
| stroke 16 | 46 % → 21 % | 150.0 px | 0.45 | 0.46 | 352 |
| stroke 17 | 45 % → 22 % | 258.8 px | 0.44 | 0.47 | 98 |
| stroke 18 | 49 % → 38 % | 208.5 px | 0.44 | 0.78 | 247 |
| stroke 19 | 45 % → 33 % | 237.8 px | 0.44 | 0.74 | 191 |
| stroke 20 | 6 % → 65 % | 80.9 px | 0.44 | 10.88 | 39 |
| stroke 21 | 2 % → 74 % | 26.4 px | 0.44 | 37.50 | 19 |
| stroke 22 | 12 % → 0 % | 51.0 px | 0.00 | 0.00 | 211 |
| stroke 23 | 6 % → 0 % | 57.2 px | 0.00 | 0.00 | 32 |
| stroke 24 | 22 % → 0 % | 69.7 px | 0.00 | 0.00 | 619 |
| stroke 25 | 27 % → 0 % | 145.2 px | 0.00 | 0.00 | 121 |
| stroke 26 | 36 % → 0 % | 145.6 px | 0.00 | 0.00 | 227 |
| stroke 27 | 23 % → 0 % | 125.6 px | 0.00 | 0.00 | 90 |
| stroke 28 | 43 % → 0 % | 124.4 px | 0.00 | 0.00 | 634 |
| stroke 29 | 41 % → 0 % | 552.5 px | 0.00 | 0.00 | 32 |
| stroke 30 | 50 % → 0 % | 468.5 px | 0.00 | 0.00 | 50 |
| stroke 31 | 32 % → 0 % | 320.7 px | 0.00 | 0.00 | 30 |
| stroke 32 | 35 % → 0 % | 208.3 px | 0.00 | 0.00 | 66 |
| stroke 33 | 33 % → 0 % | 215.1 px | 0.00 | 0.00 | 102 |
| stroke 34 | 7 % → 27 % | 52.2 px | 0.44 | 3.63 | 80 |
| stroke 35 | 12 % → 44 % | 130.4 px | 0.44 | 3.52 | 48 |
| stroke 36 | 16 % → 56 % | 233.3 px | 0.45 | 3.46 | 37 |
| stroke 37 | 4 % → 79 % | 55.3 px | 0.44 | 19.71 | 22 |
| stroke 38 | 2 % → 0 % | 24.2 px | 0.00 | 0.00 | 16 |
| stroke 39 | 1 % → 0 % | 24.1 px | 0.00 | 0.00 | 8 |
| stroke 40 | 8 % → 0 % | 28.0 px | 0.00 | 0.00 | 61 |
| stroke 41 | 13 % → 0 % | 48.7 px | 0.00 | 0.00 | 67 |
| stroke 42 | 5 % → 0 % | 31.3 px | 0.00 | 0.00 | 30 |
| stroke 43 | 6 % → 0 % | 115.3 px | 0.00 | 0.00 | 8 |
| stroke 44 | 10 % → 0 % | 46.2 px | 0.00 | 0.00 | 54 |
| stroke 45 | 13 % → 0 % | 114.6 px | 0.00 | 0.00 | 20 |
| stroke 46 | 2 % → 0 % | 30.0 px | 0.00 | 0.00 | 14 |
| stroke 47 | 14 % → 0 % | 53.6 px | 0.00 | 0.00 | 213 |
| stroke 48 | 23 % → 0 % | 82.1 px | 0.00 | 0.00 | 179 |
| stroke 49 | 5 % → 0 % | 28.6 px | 0.00 | 0.00 | 92 |
| stroke 50 | 9 % → 0 % | 44.8 px | 0.00 | 0.00 | 68 |
| stroke 51 | 14 % → 1 % | 80.1 px | 0.41 | 0.08 | 47 |
| stroke 52 | 19 % → 5 % | 144.1 px | 0.42 | 0.25 | 45 |
| stroke 53 | 5 % → 74 % | 29.9 px | 0.44 | 13.71 | 61 |
| stroke 54 | 9 % → 74 % | 57.3 px | 0.44 | 8.42 | 51 |
| stroke 55 | 13 % → 65 % | 117.3 px | 0.44 | 4.99 | 24 |
| stroke 56 | 15 % → 59 % | 307.3 px | 0.45 | 4.01 | 6 |
| stroke 57 | 5 % → 0 % | 34.0 px | 0.00 | 0.00 | 35 |
| stroke 58 | 8 % → 0 % | 62.5 px | 0.00 | 0.00 | 37 |
| stroke 59 | 3 % → 0 % | 36.2 px | 0.00 | 0.00 | 16 |
| stroke 60 | 5 % → 0 % | 70.2 px | 0.00 | 0.00 | 22 |
| stroke 61 | 8 % → 0 % | 81.2 px | 0.00 | 0.00 | 21 |
| stroke 62 | 10 % → 0 % | 62.6 px | 0.00 | 0.00 | 42 |
| stroke 63 | 15 % → 0 % | 168.3 px | 0.00 | 0.00 | 19 |
| stroke 64 | 4 % → 0 % | 36.0 px | 0.00 | 0.00 | 20 |
| stroke 65 | 7 % → 0 % | 33.3 px | 0.00 | 0.00 | 100 |
| stroke 66 | 12 % → 0 % | 53.1 px | 0.00 | 0.00 | 88 |
| stroke 67 | 18 % → 0 % | 183.7 px | 0.00 | 0.00 | 50 |
| stroke 68 | 5 % → 30 % | 34.3 px | 0.44 | 5.72 | 30 |
| stroke 69 | 6 % → 64 % | 33.5 px | 0.44 | 11.49 | 34 |
| stroke 70 | 10 % → 57 % | 85.4 px | 0.44 | 5.49 | 22 |
| stroke 71 | 7 % → 41 % | 62.4 px | 0.44 | 6.17 | 38 |
| stroke 72 | 10 % → 49 % | 64.4 px | 0.44 | 4.98 | 77 |
| stroke 73 | 6 % → 40 % | 59.8 px | 0.44 | 6.76 | 29 |
| stroke 74 | 20 % → 57 % | 86.7 px | 0.44 | 2.87 | 160 |
| stroke 75 | 25 % → 55 % | 108.2 px | 0.44 | 2.20 | 110 |
| stroke 76 | 35 % → 65 % | 94.7 px | 0.44 | 1.87 | 504 |
| stroke 77 | 29 % → 61 % | 254.7 px | 0.44 | 2.13 | 30 |
| stroke 78 | 46 % → 77 % | 151.4 px | 0.44 | 1.66 | 260 |
| stroke 79 | 34 % → 73 % | 204.2 px | 0.43 | 2.18 | 47 |
| stroke 80 | 50 % → 81 % | 208.7 px | 0.44 | 1.62 | 382 |
| stroke 81 | 42 % → 74 % | 335.9 px | 0.44 | 1.75 | 62 |
| stroke 82 | 49 % → 72 % | 160.6 px | 0.44 | 1.47 | 588 |
| stroke 83 | 37 % → 68 % | 235.1 px | 0.44 | 1.85 | 65 |
| stroke 84 | 55 % → 68 % | 176.2 px | 0.43 | 1.25 | 237 |
| stroke 85 | 49 % → 61 % | 177.8 px | 0.44 | 1.25 | 224 |
| stroke 86 | 67 % → 67 % | 174.4 px | 0.43 | 1.00 | 283 |
| stroke 87 | 54 % → 55 % | 159.0 px | 0.44 | 1.02 | 311 |

Numbers say: wet paint spreads well beyond the stroke.

