![All brushes](contact.png)

# Brush Lab — 100 brushes · 9 Nov 2026 at 06:34

Every sheet: 1500 × 600, ten strokes in a 5 × 2 grid — 1. light line · 2. heavy line · 3. pressure swell · 4. fast wave · 5. slow wave · 6. spiral · 7. loop · 8. tilted · 9. over the wet one · 10. long, no reload (cell 8 holds «tilted» and «over the wet one» crossed). The CPU reference of Mamay's paint engine; the wet layer settles 20 s at the end.

Columns: **covered** = share of the cell with paint right after the stroke → after settling; **width** = painted area of the stroke ÷ its length (px); **dark** = mean darkness of the painted pixels above the paper's own grain (0 = paper, 1 = black); **spread** = how far wet paint went beyond the stroke (1.0 = stayed); **ms** = the stroke on the CPU; long stroke: paint in each quarter of its length (it should run out: wet → streaks → dry tail).

## Refs v3 · #01 HW peach cloud
Gouache 1.00 + turpentine 30 % · 104 px · 70.4 s

![Refs v3 · #01 HW peach cloud](Refs-v3-01-HW-peach-cloud.png)

A light paint: laid on a grey sheet (on white it cannot be seen); **dark** = how far it is from the grey either way.

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 31 % → 29 % | 90.3 px | 0.31 | 0.94 | 480 |
| heavy line | 32 % → 29 % | 93.7 px | 0.31 | 0.90 | 555 |
| pressure swell | 25 % → 24 % | 92.8 px | 0.29 | 0.98 | 410 |
| fast wave | 68 % → 33 % | 78.2 px | 0.24 | 0.49 | 2133 |
| slow wave | 66 % → 31 % | 76.5 px | 0.29 | 0.47 | 2635 |
| spiral | 79 % → 35 % | 52.4 px | 0.25 | 0.44 | 3660 |
| loop | 60 % → 39 % | 77.9 px | 0.29 | 0.65 | 1302 |
| tilted | 25 % → 25 % | 68.9 px | 0.28 | 1.00 | 986 |
| over the wet one | 51 % → 46 % | 73.0 px | 0.28 | 0.90 | 593 |
| long, no reload | 95 % → 35 % | 42.8 px | 0.30 | 0.37 | 4277 | quarters: 0.00 → 0.00 → 0.00 → 0.00

Numbers say: light vs heavy: width 90.3 → 93.7 px, dark 0.31 → 0.31; pressure barely changes the width; the long stroke does not run out of paint.

## Refs v3 · #02 HW cream strokes
Gouache 1.00 + turpentine 30 % · 51 px · 50.9 s

![Refs v3 · #02 HW cream strokes](Refs-v3-02-HW-cream-strokes.png)

A light paint: laid on a grey sheet (on white it cannot be seen); **dark** = how far it is from the grey either way.

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 16 % → 15 % | 46.3 px | 0.37 | 0.92 | 268 |
| heavy line | 17 % → 15 % | 48.1 px | 0.34 | 0.89 | 364 |
| pressure swell | 13 % → 12 % | 47.2 px | 0.35 | 0.95 | 198 |
| fast wave | 39 % → 16 % | 45.1 px | 0.29 | 0.42 | 602 |
| slow wave | 40 % → 18 % | 46.1 px | 0.33 | 0.45 | 1310 |
| spiral | 59 % → 21 % | 38.7 px | 0.32 | 0.35 | 1223 |
| loop | 34 % → 18 % | 44.5 px | 0.35 | 0.52 | 543 |
| tilted | 14 % → 14 % | 39.9 px | 0.31 | 1.01 | 314 |
| over the wet one | 30 % → 26 % | 42.8 px | 0.31 | 0.87 | 408 |
| long, no reload | 72 % → 17 % | 32.3 px | 0.31 | 0.24 | 1801 | quarters: 0.00 → 0.01 → 0.01 → 0.01

Numbers say: light vs heavy: width 46.3 → 48.1 px, dark 0.37 → 0.34; pressure barely changes the width; the long stroke does not run out of paint.

## Refs v3 · #03 HW navy contours
Gouache 1.00 + turpentine 30 % · 80 px · 60.3 s

![Refs v3 · #03 HW navy contours](Refs-v3-03-HW-navy-contours.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 24 % → 23 % | 69.4 px | 0.27 | 0.96 | 388 |
| heavy line | 26 % → 23 % | 74.2 px | 0.28 | 0.92 | 388 |
| pressure swell | 19 % → 19 % | 71.9 px | 0.30 | 0.97 | 262 |
| fast wave | 57 % → 26 % | 65.5 px | 0.32 | 0.45 | 1238 |
| slow wave | 56 % → 27 % | 64.8 px | 0.30 | 0.48 | 2481 |
| spiral | 70 % → 28 % | 46.4 px | 0.33 | 0.40 | 2011 |
| loop | 50 % → 30 % | 64.5 px | 0.30 | 0.60 | 1481 |
| tilted | 20 % → 20 % | 55.2 px | 0.33 | 1.01 | 653 |
| over the wet one | 42 % → 37 % | 61.0 px | 0.33 | 0.88 | 397 |
| long, no reload | 90 % → 28 % | 40.3 px | 0.33 | 0.31 | 2675 | quarters: 0.31 → 0.22 → 0.09 → 0.01

Numbers say: light vs heavy: width 69.4 → 74.2 px, dark 0.27 → 0.28; pressure barely changes the width.

## Refs v3 · #04 HW grey cloud
Gouache 1.00 + turpentine 30 % · 93 px · 67.0 s

![Refs v3 · #04 HW grey cloud](Refs-v3-04-HW-grey-cloud.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 28 % → 27 % | 81.5 px | 0.13 | 0.95 | 462 |
| heavy line | 29 % → 26 % | 84.5 px | 0.14 | 0.90 | 534 |
| pressure swell | 22 % → 21 % | 83.2 px | 0.17 | 0.97 | 361 |
| fast wave | 63 % → 30 % | 73.0 px | 0.22 | 0.47 | 2178 |
| slow wave | 62 % → 31 % | 71.7 px | 0.17 | 0.49 | 2172 |
| spiral | 71 % → 33 % | 46.7 px | 0.21 | 0.46 | 2806 |
| loop | 56 % → 35 % | 72.4 px | 0.12 | 0.62 | 1411 |
| tilted | 23 % → 23 % | 63.4 px | 0.19 | 1.00 | 591 |
| over the wet one | 47 % → 42 % | 68.6 px | 0.19 | 0.88 | 540 |
| long, no reload | 94 % → 31 % | 41.9 px | 0.19 | 0.33 | 3783 | quarters: 0.18 → 0.12 → 0.05 → 0.01

Numbers say: light vs heavy: width 81.5 → 84.5 px, dark 0.13 → 0.14; pressure barely changes the width.

## Refs v3 · #05 HW green in rust loops
Gouache 1.00 + turpentine 30 % · 104 px · 70.7 s

![Refs v3 · #05 HW green in rust loops](Refs-v3-05-HW-green-in-rust-loops.png)

A light paint: laid on a grey sheet (on white it cannot be seen); **dark** = how far it is from the grey either way.

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 31 % → 29 % | 90.3 px | 0.36 | 0.94 | 529 |
| heavy line | 32 % → 29 % | 93.7 px | 0.37 | 0.90 | 488 |
| pressure swell | 25 % → 24 % | 92.8 px | 0.35 | 0.98 | 395 |
| fast wave | 68 % → 33 % | 78.2 px | 0.30 | 0.49 | 2233 |
| slow wave | 66 % → 31 % | 76.5 px | 0.34 | 0.47 | 2611 |
| spiral | 79 % → 35 % | 52.4 px | 0.31 | 0.44 | 3544 |
| loop | 60 % → 39 % | 77.9 px | 0.35 | 0.65 | 1336 |
| tilted | 25 % → 25 % | 68.9 px | 0.33 | 1.00 | 971 |
| over the wet one | 51 % → 46 % | 73.0 px | 0.33 | 0.90 | 569 |
| long, no reload | 95 % → 35 % | 42.8 px | 0.35 | 0.37 | 4204 | quarters: 0.00 → 0.00 → 0.00 → 0.00

Numbers say: light vs heavy: width 90.3 → 93.7 px, dark 0.36 → 0.37; pressure barely changes the width; the long stroke does not run out of paint.

## Refs v3 · #06 HW scrubbed grey
Gouache 1.00 + turpentine 30 % · 93 px · 66.6 s

![Refs v3 · #06 HW scrubbed grey](Refs-v3-06-HW-scrubbed-grey.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 28 % → 27 % | 81.5 px | 0.13 | 0.95 | 462 |
| heavy line | 29 % → 26 % | 84.5 px | 0.14 | 0.90 | 465 |
| pressure swell | 22 % → 21 % | 83.2 px | 0.17 | 0.97 | 310 |
| fast wave | 63 % → 30 % | 73.0 px | 0.22 | 0.47 | 2064 |
| slow wave | 62 % → 31 % | 71.7 px | 0.17 | 0.49 | 2433 |
| spiral | 71 % → 33 % | 46.7 px | 0.21 | 0.46 | 2871 |
| loop | 56 % → 35 % | 72.4 px | 0.12 | 0.62 | 1352 |
| tilted | 23 % → 23 % | 63.4 px | 0.19 | 1.00 | 642 |
| over the wet one | 47 % → 42 % | 68.6 px | 0.19 | 0.88 | 553 |
| long, no reload | 94 % → 31 % | 41.9 px | 0.19 | 0.33 | 3888 | quarters: 0.18 → 0.12 → 0.05 → 0.01

Numbers say: light vs heavy: width 81.5 → 84.5 px, dark 0.13 → 0.14; pressure barely changes the width.

## Refs v3 · #07 HW blue L and zigzag
Gouache 1.00 + turpentine 30 % · 104 px · 70.3 s

![Refs v3 · #07 HW blue L and zigzag](Refs-v3-07-HW-blue-L-and-zigzag.png)

A light paint: laid on a grey sheet (on white it cannot be seen); **dark** = how far it is from the grey either way.

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 31 % → 29 % | 90.3 px | 0.39 | 0.94 | 456 |
| heavy line | 32 % → 29 % | 93.7 px | 0.40 | 0.90 | 550 |
| pressure swell | 25 % → 24 % | 92.8 px | 0.37 | 0.98 | 374 |
| fast wave | 68 % → 33 % | 78.2 px | 0.34 | 0.49 | 2250 |
| slow wave | 66 % → 31 % | 76.5 px | 0.37 | 0.47 | 2712 |
| spiral | 79 % → 35 % | 52.4 px | 0.34 | 0.44 | 3910 |
| loop | 60 % → 39 % | 77.9 px | 0.37 | 0.65 | 1270 |
| tilted | 25 % → 25 % | 68.9 px | 0.36 | 1.00 | 1049 |
| over the wet one | 51 % → 46 % | 73.0 px | 0.36 | 0.90 | 687 |
| long, no reload | 95 % → 35 % | 42.8 px | 0.37 | 0.37 | 4159 | quarters: 0.00 → 0.00 → 0.00 → 0.00

Numbers say: light vs heavy: width 90.3 → 93.7 px, dark 0.39 → 0.40; pressure barely changes the width; the long stroke does not run out of paint.

## Refs v3 · #08 HW lilac crown basket
Gouache 1.00 + turpentine 30 % · 36 px · 45.5 s

![Refs v3 · #08 HW lilac crown basket](Refs-v3-08-HW-lilac-crown-basket.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 11 % → 11 % | 32.8 px | 0.13 | 1.00 | 224 |
| heavy line | 12 % → 12 % | 34.6 px | 0.14 | 0.98 | 159 |
| pressure swell | 9 % → 9 % | 35.0 px | 0.16 | 0.98 | 100 |
| fast wave | 30 % → 11 % | 34.7 px | 0.22 | 0.37 | 429 |
| slow wave | 29 % → 13 % | 33.7 px | 0.17 | 0.44 | 1487 |
| spiral | 48 % → 14 % | 31.8 px | 0.16 | 0.29 | 1475 |
| loop | 26 % → 12 % | 33.4 px | 0.14 | 0.47 | 403 |
| tilted | 12 % → 12 % | 32.9 px | 0.18 | 1.01 | 216 |
| over the wet one | 23 % → 20 % | 32.4 px | 0.18 | 0.86 | 184 |
| long, no reload | 53 % → 12 % | 23.6 px | 0.15 | 0.23 | 1355 | quarters: 0.09 → 0.03 → 0.00 → 0.00

Numbers say: light vs heavy: width 32.8 → 34.6 px, dark 0.13 → 0.14; pressure barely changes the width.

## Refs v3 · #09 HW white loops
Gouache 1.00 + turpentine 30 % · 104 px · 70.4 s

![Refs v3 · #09 HW white loops](Refs-v3-09-HW-white-loops.png)

A light paint: laid on a grey sheet (on white it cannot be seen); **dark** = how far it is from the grey either way.

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 31 % → 29 % | 90.3 px | 0.38 | 0.94 | 530 |
| heavy line | 32 % → 29 % | 93.7 px | 0.39 | 0.90 | 534 |
| pressure swell | 25 % → 24 % | 92.8 px | 0.37 | 0.98 | 411 |
| fast wave | 68 % → 33 % | 78.2 px | 0.33 | 0.49 | 2304 |
| slow wave | 66 % → 31 % | 76.5 px | 0.36 | 0.47 | 2649 |
| spiral | 79 % → 35 % | 52.4 px | 0.33 | 0.44 | 3888 |
| loop | 60 % → 39 % | 77.9 px | 0.37 | 0.65 | 1135 |
| tilted | 25 % → 25 % | 68.9 px | 0.35 | 1.00 | 1071 |
| over the wet one | 51 % → 46 % | 73.0 px | 0.35 | 0.90 | 684 |
| long, no reload | 95 % → 35 % | 42.8 px | 0.36 | 0.37 | 4157 | quarters: 0.00 → 0.00 → 0.00 → 0.00

Numbers say: light vs heavy: width 90.3 → 93.7 px, dark 0.38 → 0.39; pressure barely changes the width; the long stroke does not run out of paint.

## Refs v3 · #10 HW maroon loops
Gouache 1.00 + turpentine 30 % · 104 px · 70.6 s

![Refs v3 · #10 HW maroon loops](Refs-v3-10-HW-maroon-loops.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 31 % → 29 % | 90.3 px | 0.26 | 0.94 | 518 |
| heavy line | 32 % → 29 % | 93.7 px | 0.25 | 0.90 | 581 |
| pressure swell | 25 % → 24 % | 92.8 px | 0.27 | 0.98 | 370 |
| fast wave | 68 % → 33 % | 78.2 px | 0.32 | 0.49 | 2300 |
| slow wave | 66 % → 31 % | 76.5 px | 0.27 | 0.47 | 2716 |
| spiral | 79 % → 35 % | 52.4 px | 0.31 | 0.44 | 4079 |
| loop | 60 % → 39 % | 77.9 px | 0.25 | 0.65 | 1192 |
| tilted | 25 % → 25 % | 68.9 px | 0.28 | 1.00 | 1150 |
| over the wet one | 51 % → 46 % | 73.0 px | 0.28 | 0.90 | 710 |
| long, no reload | 95 % → 35 % | 42.8 px | 0.24 | 0.37 | 4264 | quarters: 0.23 → 0.19 → 0.09 → 0.02

Numbers say: light vs heavy: width 90.3 → 93.7 px, dark 0.26 → 0.25; pressure barely changes the width.

## Refs v3 · #11 HW purple balls
Gouache 1.00 + turpentine 30 % · 104 px · 66.6 s

![Refs v3 · #11 HW purple balls](Refs-v3-11-HW-purple-balls.png)

A light paint: laid on a grey sheet (on white it cannot be seen); **dark** = how far it is from the grey either way.

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 31 % → 29 % | 90.3 px | 0.30 | 0.94 | 487 |
| heavy line | 32 % → 29 % | 93.7 px | 0.31 | 0.90 | 526 |
| pressure swell | 25 % → 24 % | 92.8 px | 0.28 | 0.98 | 381 |
| fast wave | 68 % → 33 % | 78.2 px | 0.24 | 0.49 | 1452 |
| slow wave | 66 % → 31 % | 76.5 px | 0.28 | 0.47 | 2102 |
| spiral | 79 % → 35 % | 52.4 px | 0.24 | 0.44 | 2656 |
| loop | 60 % → 39 % | 77.9 px | 0.29 | 0.65 | 1403 |
| tilted | 25 % → 25 % | 68.9 px | 0.27 | 1.00 | 896 |
| over the wet one | 51 % → 46 % | 73.0 px | 0.27 | 0.90 | 699 |
| long, no reload | 95 % → 35 % | 42.8 px | 0.29 | 0.37 | 4316 | quarters: 0.00 → 0.00 → 0.00 → 0.00

Numbers say: light vs heavy: width 90.3 → 93.7 px, dark 0.30 → 0.31; pressure barely changes the width; the long stroke does not run out of paint.

## Refs v3 · #12 HW black-olive cage
Gouache 1.00 + turpentine 30 % · 36 px · 41.1 s

![Refs v3 · #12 HW black-olive cage](Refs-v3-12-HW-black-olive-cage.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 11 % → 11 % | 32.8 px | 0.13 | 1.00 | 144 |
| heavy line | 12 % → 12 % | 34.6 px | 0.14 | 0.98 | 144 |
| pressure swell | 9 % → 9 % | 35.0 px | 0.16 | 0.98 | 101 |
| fast wave | 30 % → 11 % | 34.7 px | 0.22 | 0.37 | 439 |
| slow wave | 29 % → 13 % | 33.7 px | 0.17 | 0.44 | 586 |
| spiral | 48 % → 14 % | 31.8 px | 0.16 | 0.29 | 836 |
| loop | 26 % → 12 % | 33.4 px | 0.14 | 0.47 | 561 |
| tilted | 12 % → 12 % | 32.9 px | 0.18 | 1.01 | 223 |
| over the wet one | 23 % → 20 % | 32.4 px | 0.18 | 0.86 | 200 |
| long, no reload | 53 % → 12 % | 23.6 px | 0.15 | 0.23 | 922 | quarters: 0.09 → 0.03 → 0.00 → 0.00

Numbers say: light vs heavy: width 32.8 → 34.6 px, dark 0.13 → 0.14; pressure barely changes the width.

## Refs v3 · #13 HW blue streaky form
Gouache 1.00 + turpentine 30 % · 104 px · 66.2 s

![Refs v3 · #13 HW blue streaky form](Refs-v3-13-HW-blue-streaky-form.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 31 % → 29 % | 90.3 px | 0.16 | 0.94 | 745 |
| heavy line | 32 % → 29 % | 93.7 px | 0.15 | 0.90 | 619 |
| pressure swell | 25 % → 24 % | 92.8 px | 0.18 | 0.98 | 407 |
| fast wave | 68 % → 33 % | 78.2 px | 0.23 | 0.49 | 1706 |
| slow wave | 66 % → 31 % | 76.5 px | 0.17 | 0.47 | 3142 |
| spiral | 79 % → 35 % | 52.4 px | 0.22 | 0.44 | 2647 |
| loop | 60 % → 39 % | 77.9 px | 0.16 | 0.65 | 1510 |
| tilted | 25 % → 25 % | 68.9 px | 0.18 | 1.00 | 1090 |
| over the wet one | 51 % → 46 % | 73.0 px | 0.18 | 0.90 | 624 |
| long, no reload | 95 % → 35 % | 42.8 px | 0.15 | 0.37 | 3813 | quarters: 0.14 → 0.11 → 0.05 → 0.01

Numbers say: light vs heavy: width 90.3 → 93.7 px, dark 0.16 → 0.15; pressure barely changes the width.

## Refs v3 · #14 HW olive totem
Gouache 1.00 + turpentine 30 % · 57 px · 49.1 s

![Refs v3 · #14 HW olive totem](Refs-v3-14-HW-olive-totem.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 18 % → 16 % | 51.2 px | 0.31 | 0.93 | 209 |
| heavy line | 18 % → 17 % | 53.4 px | 0.30 | 0.94 | 271 |
| pressure swell | 14 % → 14 % | 52.0 px | 0.32 | 0.98 | 235 |
| fast wave | 44 % → 17 % | 51.0 px | 0.34 | 0.38 | 842 |
| slow wave | 43 % → 20 % | 49.9 px | 0.33 | 0.46 | 1316 |
| spiral | 63 % → 23 % | 41.5 px | 0.34 | 0.37 | 1314 |
| loop | 38 % → 21 % | 48.9 px | 0.31 | 0.57 | 605 |
| tilted | 15 % → 15 % | 42.9 px | 0.34 | 1.01 | 380 |
| over the wet one | 32 % → 28 % | 46.4 px | 0.34 | 0.87 | 310 |
| long, no reload | 78 % → 21 % | 35.0 px | 0.33 | 0.27 | 1444 | quarters: 0.28 → 0.16 → 0.04 → 0.01

Numbers say: light vs heavy: width 51.2 → 53.4 px, dark 0.31 → 0.30; pressure barely changes the width.

## Refs v3 · #15 Ultramarine script
Ink 0.98 · 39 px · 39.4 s

![Refs v3 · #15 Ultramarine script](Refs-v3-15-Ultramarine-script.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 4 % → 7 % | 10.6 px | 0.60 | 2.03 | 50 |
| heavy line | 14 % → 15 % | 40.2 px | 0.68 | 1.11 | 176 |
| pressure swell | 8 % → 9 % | 28.6 px | 0.68 | 1.23 | 252 |
| fast wave | 28 % → 31 % | 31.8 px | 0.69 | 1.13 | 345 |
| slow wave | 23 % → 28 % | 26.9 px | 0.67 | 1.20 | 591 |
| spiral | 39 % → 45 % | 25.8 px | 0.66 | 1.15 | 512 |
| loop | 21 % → 25 % | 27.0 px | 0.66 | 1.19 | 246 |
| tilted | 14 % → 14 % | 39.2 px | 0.70 | 1.00 | 123 |
| over the wet one | 24 % → 26 % | 27.2 px | 0.70 | 1.09 | 175 |
| long, no reload | 54 % → 59 % | 24.3 px | 0.66 | 1.09 | 783 | quarters: 0.47 → 0.45 → 0.42 → 0.37

Numbers say: light vs heavy: width 10.6 → 40.2 px, dark 0.60 → 0.68; wet paint spreads well beyond the stroke.

## Refs v3 · #16 Shrigley strokes
Watercolour 1.00 + water 30 % · 64 px · 42.2 s

![Refs v3 · #16 Shrigley strokes](Refs-v3-16-Shrigley-strokes.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 8 % → 17 % | 24.6 px | 0.29 | 1.98 | 98 |
| heavy line | 17 % → 22 % | 49.0 px | 0.29 | 1.28 | 321 |
| pressure swell | 10 % → 15 % | 38.6 px | 0.34 | 1.45 | 158 |
| fast wave | 36 % → 43 % | 42.1 px | 0.32 | 1.17 | 600 |
| slow wave | 33 % → 40 % | 38.5 px | 0.28 | 1.21 | 618 |
| spiral | 57 % → 60 % | 37.9 px | 0.21 | 1.04 | 711 |
| loop | 29 % → 35 % | 37.6 px | 0.28 | 1.19 | 489 |
| tilted | 19 % → 19 % | 52.1 px | 0.30 | 1.00 | 258 |
| over the wet one | 31 % → 36 % | 35.0 px | 0.30 | 1.15 | 187 |
| long, no reload | 71 % → 75 % | 31.9 px | 0.20 | 1.06 | 1378 | quarters: 0.26 → 0.17 → 0.13 → 0.09

Numbers say: light vs heavy: width 24.6 → 49.0 px, dark 0.29 → 0.29; wet paint spreads well beyond the stroke.

## Refs v3 · #17 Krovostok dry brush
Ink 0.93 · Gouache 0.07 · 53 px · 58.3 s

![Refs v3 · #17 Krovostok dry brush](Refs-v3-17-Krovostok-dry-brush.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 16 % → 18 % | 47.0 px | 0.74 | 1.09 | 176 |
| heavy line | 18 % → 20 % | 52.5 px | 0.75 | 1.08 | 332 |
| pressure swell | 13 % → 14 % | 50.0 px | 0.76 | 1.09 | 274 |
| fast wave | 42 % → 43 % | 48.1 px | 0.77 | 1.03 | 590 |
| slow wave | 41 % → 43 % | 46.9 px | 0.74 | 1.06 | 940 |
| spiral | 60 % → 61 % | 39.7 px | 0.76 | 1.01 | 1385 |
| loop | 35 % → 38 % | 45.7 px | 0.75 | 1.07 | 637 |
| tilted | 15 % → 15 % | 42.8 px | 0.75 | 1.00 | 228 |
| over the wet one | 31 % → 33 % | 43.4 px | 0.75 | 1.06 | 251 |
| long, no reload | 71 % → 76 % | 31.9 px | 0.74 | 1.06 | 1306 | quarters: 0.68 → 0.65 → 0.58 → 0.50

Numbers say: light vs heavy: width 47.0 → 52.5 px, dark 0.74 → 0.75.

## Refs v3 · #18 Twombly blue sticks
Wax 1.00 · 19 px · 12.5 s

![Refs v3 · #18 Twombly blue sticks](Refs-v3-18-Twombly-blue-sticks.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 4 % → 4 % | 11.8 px | 0.23 | 1.00 | 53 |
| heavy line | 6 % → 6 % | 16.5 px | 0.25 | 1.00 | 41 |
| pressure swell | 4 % → 4 % | 15.4 px | 0.23 | 1.00 | 48 |
| fast wave | 14 % → 14 % | 16.1 px | 0.24 | 1.00 | 119 |
| slow wave | 13 % → 13 % | 15.3 px | 0.25 | 1.00 | 192 |
| spiral | 21 % → 21 % | 14.2 px | 0.24 | 1.00 | 205 |
| loop | 11 % → 11 % | 13.6 px | 0.24 | 1.00 | 135 |
| tilted | 4 % → 4 % | 12.4 px | 0.23 | 1.00 | 50 |
| over the wet one | 10 % → 10 % | 15.0 px | 0.23 | 1.00 | 54 |
| long, no reload | 27 % → 27 % | 12.2 px | 0.24 | 1.00 | 251 | quarters: 0.07 → 0.07 → 0.07 → 0.07

Numbers say: light vs heavy: width 11.8 → 16.5 px, dark 0.23 → 0.25; the long stroke does not run out of paint.

## Refs v3 · #19 Guston charcoal hand
Charcoal 1.00 · 60 px · 17.3 s

![Refs v3 · #19 Guston charcoal hand](Refs-v3-19-Guston-charcoal-hand.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 10 % → 10 % | 28.0 px | 0.62 | 1.00 | 174 |
| heavy line | 18 % → 18 % | 51.7 px | 0.61 | 1.00 | 322 |
| pressure swell | 12 % → 12 % | 46.2 px | 0.62 | 1.00 | 198 |
| fast wave | 39 % → 39 % | 44.8 px | 0.62 | 1.00 | 702 |
| slow wave | 36 % → 36 % | 41.9 px | 0.62 | 1.00 | 1036 |
| spiral | 57 % → 57 % | 37.8 px | 0.62 | 1.00 | 950 |
| loop | 29 % → 29 % | 37.6 px | 0.62 | 1.00 | 479 |
| tilted | 10 % → 10 % | 26.7 px | 0.61 | 1.00 | 307 |
| over the wet one | 24 % → 24 % | 40.7 px | 0.61 | 1.00 | 258 |
| long, no reload | 67 % → 67 % | 29.9 px | 0.62 | 1.00 | 1921 | quarters: 0.45 → 0.44 → 0.44 → 0.45

Numbers say: light vs heavy: width 28.0 → 51.7 px, dark 0.62 → 0.61; the long stroke does not run out of paint.

## Refs v3 · #20 Orange crayon
Wax 1.00 · 48 px · 15.9 s

![Refs v3 · #20 Orange crayon](Refs-v3-20-Orange-crayon.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 9 % → 9 % | 25.1 px | 0.52 | 1.00 | 197 |
| heavy line | 14 % → 14 % | 41.0 px | 0.52 | 1.00 | 248 |
| pressure swell | 10 % → 10 % | 37.4 px | 0.52 | 1.00 | 151 |
| fast wave | 31 % → 31 % | 36.3 px | 0.52 | 1.00 | 510 |
| slow wave | 30 % → 30 % | 34.4 px | 0.52 | 1.00 | 772 |
| spiral | 48 % → 48 % | 31.8 px | 0.52 | 1.00 | 613 |
| loop | 24 % → 24 % | 30.8 px | 0.52 | 1.00 | 513 |
| tilted | 7 % → 7 % | 20.5 px | 0.52 | 1.00 | 227 |
| over the wet one | 19 % → 19 % | 33.1 px | 0.52 | 1.00 | 152 |
| long, no reload | 55 % → 55 % | 24.8 px | 0.52 | 1.00 | 1096 | quarters: 0.32 → 0.31 → 0.32 → 0.32

Numbers say: light vs heavy: width 25.1 → 41.0 px, dark 0.52 → 0.52; the long stroke does not run out of paint.

## Refs v3 · #21 Gritty dog contours
Gouache 1.00 + water 15 % · 77 px · 57.5 s

![Refs v3 · #21 Gritty dog contours](Refs-v3-21-Gritty-dog-contours.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 23 % → 23 % | 67.5 px | 0.36 | 0.98 | 320 |
| heavy line | 24 % → 23 % | 70.8 px | 0.37 | 0.95 | 341 |
| pressure swell | 19 % → 19 % | 70.7 px | 0.37 | 1.00 | 355 |
| fast wave | 51 % → 40 % | 58.4 px | 0.38 | 0.79 | 879 |
| slow wave | 54 % → 41 % | 62.1 px | 0.36 | 0.76 | 1286 |
| spiral | 63 % → 40 % | 41.4 px | 0.33 | 0.63 | 1732 |
| loop | 48 % → 42 % | 61.6 px | 0.36 | 0.88 | 1417 |
| tilted | 19 % → 19 % | 52.5 px | 0.37 | 1.01 | 471 |
| over the wet one | 40 % → 39 % | 60.0 px | 0.37 | 0.97 | 389 |
| long, no reload | 75 % → 48 % | 33.7 px | 0.36 | 0.63 | 2044 | quarters: 0.35 → 0.32 → 0.27 → 0.20

Numbers say: light vs heavy: width 67.5 → 70.8 px, dark 0.36 → 0.37; pressure barely changes the width.

## Refs v3 · #22 Wasilewski brush poster
Ink 0.98 · 64 px · 50.2 s

![Refs v3 · #22 Wasilewski brush poster](Refs-v3-22-Wasilewski-brush-poster.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 19 % → 21 % | 55.5 px | 0.88 | 1.08 | 113 |
| heavy line | 22 % → 23 % | 64.9 px | 0.89 | 1.01 | 267 |
| pressure swell | 16 % → 17 % | 58.6 px | 0.88 | 1.09 | 250 |
| fast wave | 51 % → 53 % | 59.3 px | 0.84 | 1.03 | 553 |
| slow wave | 48 % → 50 % | 55.3 px | 0.87 | 1.04 | 778 |
| spiral | 68 % → 68 % | 44.5 px | 0.85 | 1.01 | 1535 |
| loop | 43 % → 44 % | 56.0 px | 0.87 | 1.02 | 718 |
| tilted | 18 % → 18 % | 50.1 px | 0.87 | 1.01 | 344 |
| over the wet one | 37 % → 38 % | 52.5 px | 0.87 | 1.04 | 247 |
| long, no reload | 81 % → 86 % | 36.4 px | 0.87 | 1.06 | 1622 | quarters: 0.84 → 0.84 → 0.81 → 0.70

Numbers say: light vs heavy: width 55.5 → 64.9 px, dark 0.88 → 0.89.

## Refs v3 · #23 Report dry white mask
Ink 0.93 · Gouache 0.07 · 89 px · 68.5 s

![Refs v3 · #23 Report dry white mask](Refs-v3-23-Report-dry-white-mask.png)

A light paint: laid on a grey sheet (on white it cannot be seen); **dark** = how far it is from the grey either way.

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 26 % → 27 % | 76.3 px | 0.36 | 1.03 | 249 |
| heavy line | 27 % → 28 % | 78.7 px | 0.40 | 1.03 | 455 |
| pressure swell | 21 % → 23 % | 79.9 px | 0.36 | 1.08 | 257 |
| fast wave | 60 % → 63 % | 69.2 px | 0.33 | 1.04 | 1094 |
| slow wave | 60 % → 60 % | 69.2 px | 0.37 | 1.01 | 2553 |
| spiral | 75 % → 71 % | 49.3 px | 0.38 | 0.95 | 1811 |
| loop | 55 % → 56 % | 71.3 px | 0.40 | 1.02 | 836 |
| tilted | 22 % → 22 % | 60.2 px | 0.35 | 1.01 | 795 |
| over the wet one | 46 % → 48 % | 68.2 px | 0.35 | 1.04 | 510 |
| long, no reload | 89 % → 89 % | 39.7 px | 0.35 | 1.01 | 3099 | quarters: 0.00 → 0.00 → 0.00 → 0.00

Numbers say: light vs heavy: width 76.3 → 78.7 px, dark 0.36 → 0.40; pressure barely changes the width.

## Refs v3 · #24 Picasso flat oil
Gouache 1.00 + turpentine 20 % · 74 px · 54.2 s

![Refs v3 · #24 Picasso flat oil](Refs-v3-24-Picasso-flat-oil.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 24 % → 22 % | 68.6 px | 0.11 | 0.92 | 498 |
| heavy line | 25 % → 22 % | 72.2 px | 0.12 | 0.87 | 420 |
| pressure swell | 19 % → 18 % | 70.3 px | 0.13 | 0.96 | 305 |
| fast wave | 54 % → 24 % | 62.3 px | 0.18 | 0.45 | 1291 |
| slow wave | 55 % → 26 % | 63.5 px | 0.15 | 0.47 | 1673 |
| spiral | 70 % → 27 % | 46.1 px | 0.17 | 0.39 | 1522 |
| loop | 48 % → 29 % | 61.9 px | 0.12 | 0.60 | 1016 |
| tilted | 18 % → 18 % | 51.4 px | 0.16 | 1.00 | 507 |
| over the wet one | 40 % → 36 % | 61.1 px | 0.16 | 0.89 | 470 |
| long, no reload | 90 % → 26 % | 40.2 px | 0.15 | 0.29 | 2067 | quarters: 0.14 → 0.08 → 0.02 → 0.00

Numbers say: light vs heavy: width 68.6 → 72.2 px, dark 0.11 → 0.12; pressure barely changes the width.

## Refs v3 · #25 Yellow heavy stroke
Impasto 1.00 · 272 px · 90.0 s

![Refs v3 · #25 Yellow heavy stroke](Refs-v3-25-Yellow-heavy-stroke.png)

A light paint: laid on a grey sheet (on white it cannot be seen); **dark** = how far it is from the grey either way.

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 71 % → 67 % | 205.2 px | 0.23 | 0.95 | 2544 |
| heavy line | 71 % → 48 % | 204.8 px | 0.22 | 0.68 | 2720 |
| pressure swell | 63 % → 67 % | 234.4 px | 0.20 | 1.08 | 1471 |
| fast wave | 99 % → 63 % | 114.5 px | 0.18 | 0.64 | 5506 |
| slow wave | 99 % → 52 % | 114.9 px | 0.19 | 0.53 | 12743 |
| spiral | 100 % → 64 % | 65.7 px | 0.17 | 0.65 | 10379 |
| loop | 100 % → 64 % | 129.5 px | 0.20 | 0.64 | 4825 |
| tilted | 54 % → 54 % | 149.5 px | 0.18 | 1.00 | 3995 |
| over the wet one | 89 % → 82 % | 98.2 px | 0.18 | 0.92 | 2990 |
| long, no reload | 100 % → 67 % | 44.8 px | 0.18 | 0.67 | 15629 | quarters: 0.00 → 0.00 → 0.00 → 0.00

Numbers say: light vs heavy: width 205.2 → 204.8 px, dark 0.23 → 0.22; pressure barely changes the width.

## Refs v3 · #26 Ink caricature
Ink 0.98 · 64 px · 41.1 s

![Refs v3 · #26 Ink caricature](Refs-v3-26-Ink-caricature.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 6 % → 9 % | 17.6 px | 0.77 | 1.52 | 79 |
| heavy line | 20 % → 21 % | 58.8 px | 0.82 | 1.06 | 253 |
| pressure swell | 11 % → 13 % | 42.1 px | 0.82 | 1.13 | 132 |
| fast wave | 41 % → 43 % | 46.9 px | 0.84 | 1.06 | 490 |
| slow wave | 36 % → 40 % | 41.4 px | 0.82 | 1.11 | 664 |
| spiral | 59 % → 61 % | 39.2 px | 0.80 | 1.02 | 621 |
| loop | 31 % → 34 % | 40.0 px | 0.82 | 1.10 | 357 |
| tilted | 19 % → 19 % | 53.9 px | 0.82 | 1.00 | 253 |
| over the wet one | 33 % → 35 % | 38.9 px | 0.82 | 1.06 | 227 |
| long, no reload | 78 % → 80 % | 35.1 px | 0.81 | 1.02 | 1198 | quarters: 0.72 → 0.71 → 0.70 → 0.66

Numbers say: light vs heavy: width 17.6 → 58.8 px, dark 0.77 → 0.82; the long stroke does not run out of paint; wet paint spreads well beyond the stroke.

## Refs v3 · #27 Orange impasto swatch
Impasto 1.00 · 80 px · 25.6 s

![Refs v3 · #27 Orange impasto swatch](Refs-v3-27-Orange-impasto-swatch.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 24 % → 20 % | 69.4 px | 0.32 | 0.82 | 278 |
| heavy line | 25 % → 15 % | 72.2 px | 0.34 | 0.62 | 460 |
| pressure swell | 19 % → 15 % | 70.4 px | 0.36 | 0.82 | 232 |
| fast wave | 53 % → 17 % | 61.4 px | 0.39 | 0.31 | 940 |
| slow wave | 54 % → 17 % | 62.2 px | 0.35 | 0.32 | 1676 |
| spiral | 60 % → 19 % | 39.7 px | 0.39 | 0.31 | 1355 |
| loop | 48 % → 22 % | 62.3 px | 0.34 | 0.45 | 787 |
| tilted | 18 % → 18 % | 51.5 px | 0.38 | 1.00 | 543 |
| over the wet one | 40 % → 31 % | 60.3 px | 0.38 | 0.77 | 380 |
| long, no reload | 73 % → 20 % | 32.7 px | 0.37 | 0.27 | 1926 | quarters: 0.32 → 0.13 → 0.03 → 0.00

Numbers say: light vs heavy: width 69.4 → 72.2 px, dark 0.32 → 0.34; pressure barely changes the width.

## Refs v3 · #28 Miles Davis lines
Ink 0.98 · 18 px · 31.3 s

![Refs v3 · #28 Miles Davis lines](Refs-v3-28-Miles-Davis-lines.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 2 % → 6 % | 4.8 px | 0.33 | 3.61 | 34 |
| heavy line | 8 % → 10 % | 24.6 px | 0.42 | 1.24 | 156 |
| pressure swell | 4 % → 7 % | 16.1 px | 0.41 | 1.58 | 56 |
| fast wave | 15 % → 20 % | 16.8 px | 0.47 | 1.40 | 162 |
| slow wave | 12 % → 19 % | 14.1 px | 0.40 | 1.53 | 206 |
| spiral | 20 % → 26 % | 12.9 px | 0.36 | 1.35 | 251 |
| loop | 12 % → 17 % | 15.4 px | 0.40 | 1.40 | 152 |
| tilted | 8 % → 8 % | 21.7 px | 0.45 | 1.04 | 89 |
| over the wet one | 14 % → 17 % | 16.9 px | 0.45 | 1.25 | 80 |
| long, no reload | 30 % → 37 % | 13.6 px | 0.40 | 1.21 | 566 | quarters: 0.22 → 0.18 → 0.15 → 0.12

Numbers say: light vs heavy: width 4.8 → 24.6 px, dark 0.33 → 0.42; wet paint spreads well beyond the stroke.

## Refs v3 · #29 Shrigley asterisk
Watercolour 1.00 + water 50 % · 64 px · 50.0 s

![Refs v3 · #29 Shrigley asterisk](Refs-v3-29-Shrigley-asterisk.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 18 % → 21 % | 51.8 px | 0.58 | 1.19 | 192 |
| heavy line | 35 % → 35 % | 103.0 px | 0.57 | 1.00 | 1032 |
| pressure swell | 22 % → 24 % | 82.6 px | 0.59 | 1.08 | 209 |
| fast wave | 64 % → 68 % | 74.2 px | 0.59 | 1.05 | 1329 |
| slow wave | 61 % → 61 % | 69.9 px | 0.57 | 1.01 | 1358 |
| spiral | 73 % → 73 % | 48.1 px | 0.56 | 1.01 | 1384 |
| loop | 54 % → 54 % | 69.6 px | 0.57 | 1.01 | 526 |
| tilted | 22 % → 22 % | 61.3 px | 0.59 | 1.00 | 345 |
| over the wet one | 48 % → 51 % | 72.8 px | 0.59 | 1.07 | 260 |
| long, no reload | 91 % → 93 % | 40.9 px | 0.56 | 1.01 | 2056 | quarters: 0.57 → 0.57 → 0.54 → 0.45

Numbers say: light vs heavy: width 51.8 → 103.0 px, dark 0.58 → 0.57.

## Refs v3 · #30 Red gouache face
Gouache 1.00 + water 15 % · 76 px · 54.4 s

![Refs v3 · #30 Red gouache face](Refs-v3-30-Red-gouache-face.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 23 % → 22 % | 66.6 px | 0.48 | 0.98 | 337 |
| heavy line | 24 % → 23 % | 70.3 px | 0.48 | 0.94 | 510 |
| pressure swell | 18 % → 18 % | 68.6 px | 0.49 | 1.00 | 240 |
| fast wave | 51 % → 38 % | 58.4 px | 0.50 | 0.76 | 1011 |
| slow wave | 51 % → 40 % | 59.4 px | 0.48 | 0.77 | 1562 |
| spiral | 63 % → 41 % | 41.7 px | 0.44 | 0.65 | 1369 |
| loop | 45 % → 40 % | 58.7 px | 0.48 | 0.88 | 738 |
| tilted | 18 % → 18 % | 49.7 px | 0.48 | 1.01 | 455 |
| over the wet one | 39 % → 38 % | 60.1 px | 0.48 | 0.97 | 554 |
| long, no reload | 74 % → 47 % | 33.1 px | 0.47 | 0.63 | 1899 | quarters: 0.45 → 0.41 → 0.34 → 0.26

Numbers say: light vs heavy: width 66.6 → 70.3 px, dark 0.48 → 0.48; pressure barely changes the width.

## Refs v3 · #31 Warhol blotted line
Ink 0.98 · 25 px · 32.2 s

![Refs v3 · #31 Warhol blotted line](Refs-v3-31-Warhol-blotted-line.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 3 % → 7 % | 9.4 px | 0.53 | 2.04 | 42 |
| heavy line | 9 % → 11 % | 27.6 px | 0.61 | 1.20 | 90 |
| pressure swell | 5 % → 7 % | 19.8 px | 0.59 | 1.37 | 57 |
| fast wave | 19 % → 23 % | 21.8 px | 0.63 | 1.20 | 167 |
| slow wave | 17 % → 22 % | 19.3 px | 0.60 | 1.32 | 281 |
| spiral | 26 % → 32 % | 17.3 px | 0.56 | 1.23 | 245 |
| loop | 14 % → 19 % | 18.7 px | 0.60 | 1.28 | 183 |
| tilted | 10 % → 10 % | 26.9 px | 0.61 | 1.02 | 100 |
| over the wet one | 17 % → 20 % | 19.9 px | 0.61 | 1.17 | 75 |
| long, no reload | 39 % → 45 % | 17.5 px | 0.61 | 1.15 | 566 | quarters: 0.36 → 0.33 → 0.28 → 0.25

Numbers say: light vs heavy: width 9.4 → 27.6 px, dark 0.53 → 0.61; wet paint spreads well beyond the stroke.

## Refs v3 · #32 Thick orange swipes
Impasto 1.00 · 76 px · 23.3 s

![Refs v3 · #32 Thick orange swipes](Refs-v3-32-Thick-orange-swipes.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 23 % → 18 % | 67.2 px | 0.22 | 0.79 | 263 |
| heavy line | 24 % → 14 % | 68.8 px | 0.23 | 0.59 | 313 |
| pressure swell | 18 % → 15 % | 67.9 px | 0.26 | 0.82 | 301 |
| fast wave | 52 % → 15 % | 60.2 px | 0.29 | 0.30 | 734 |
| slow wave | 52 % → 16 % | 59.6 px | 0.25 | 0.31 | 1781 |
| spiral | 59 % → 18 % | 38.8 px | 0.28 | 0.31 | 1537 |
| loop | 47 % → 20 % | 60.9 px | 0.23 | 0.43 | 840 |
| tilted | 18 % → 18 % | 49.9 px | 0.28 | 1.00 | 430 |
| over the wet one | 39 % → 29 % | 59.0 px | 0.28 | 0.74 | 365 |
| long, no reload | 72 % → 19 % | 32.4 px | 0.26 | 0.27 | 1699 | quarters: 0.20 → 0.04 → 0.00 → 0.00

Numbers say: light vs heavy: width 67.2 → 68.8 px, dark 0.22 → 0.23; pressure barely changes the width.

## Refs v3 · #33 Red wet-in-wet flames
Watercolour 1.00 + water 60 % · 96 px · 64.4 s

![Refs v3 · #33 Red wet-in-wet flames](Refs-v3-33-Red-wet-in-wet-flames.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 30 % → 53 % | 87.2 px | 0.47 | 1.78 | 183 |
| heavy line | 49 % → 59 % | 141.8 px | 0.53 | 1.21 | 438 |
| pressure swell | 30 % → 48 % | 110.9 px | 0.49 | 1.62 | 360 |
| fast wave | 75 % → 87 % | 87.1 px | 0.61 | 1.16 | 1307 |
| slow wave | 78 % → 87 % | 89.8 px | 0.58 | 1.12 | 1598 |
| spiral | 88 % → 98 % | 58.1 px | 0.57 | 1.11 | 1634 |
| loop | 68 % → 83 % | 88.7 px | 0.57 | 1.21 | 968 |
| tilted | 40 % → 42 % | 112.1 px | 0.55 | 1.05 | 766 |
| over the wet one | 72 % → 92 % | 87.8 px | 0.55 | 1.28 | 615 |
| long, no reload | 96 % → 100 % | 42.9 px | 0.61 | 1.04 | 2954 | quarters: 0.67 → 0.65 → 0.63 → 0.53

Numbers say: light vs heavy: width 87.2 → 141.8 px, dark 0.47 → 0.53; wet paint spreads well beyond the stroke.

## Refs v3 · #34 Magenta oil patches
Gouache 1.00 + turpentine 20 % · 90 px · 55.1 s

![Refs v3 · #34 Magenta oil patches](Refs-v3-34-Magenta-oil-patches.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 29 % → 26 % | 82.9 px | 0.29 | 0.93 | 381 |
| heavy line | 30 % → 27 % | 87.9 px | 0.29 | 0.88 | 405 |
| pressure swell | 23 % → 22 % | 85.0 px | 0.29 | 0.96 | 360 |
| fast wave | 63 % → 29 % | 72.3 px | 0.36 | 0.47 | 1123 |
| slow wave | 63 % → 30 % | 72.5 px | 0.31 | 0.48 | 2650 |
| spiral | 75 % → 32 % | 49.6 px | 0.35 | 0.43 | 2655 |
| loop | 56 % → 34 % | 72.4 px | 0.29 | 0.60 | 1189 |
| tilted | 22 % → 22 % | 61.2 px | 0.32 | 1.00 | 636 |
| over the wet one | 47 % → 41 % | 71.1 px | 0.32 | 0.87 | 577 |
| long, no reload | 94 % → 30 % | 42.0 px | 0.31 | 0.32 | 3402 | quarters: 0.30 → 0.26 → 0.14 → 0.05

Numbers say: light vs heavy: width 82.9 → 87.9 px, dark 0.29 → 0.29; pressure barely changes the width.

## Refs v3 · #35 Red band with runs
Watercolour 1.00 + water 70 % · 176 px · 99.2 s

![Refs v3 · #35 Red band with runs](Refs-v3-35-Red-band-with-runs.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 52 % → 68 % | 149.7 px | 0.33 | 1.31 | 601 |
| heavy line | 81 % → 78 % | 236.4 px | 0.45 | 0.96 | 1192 |
| pressure swell | 59 % → 76 % | 221.4 px | 0.35 | 1.28 | 1207 |
| fast wave | 92 % → 96 % | 106.3 px | 0.53 | 1.04 | 4174 |
| slow wave | 93 % → 96 % | 107.5 px | 0.51 | 1.03 | 6190 |
| spiral | 98 % → 100 % | 65.0 px | 0.40 | 1.02 | 4908 |
| loop | 100 % → 100 % | 129.5 px | 0.53 | 1.00 | 2461 |
| tilted | 90 % → 90 % | 250.3 px | 0.47 | 1.00 | 1745 |
| over the wet one | 95 % → 100 % | 14.7 px | 0.47 | 1.05 | 1400 |
| long, no reload | 98 % → 100 % | 44.1 px | 0.47 | 1.02 | 7416 | quarters: 0.54 → 0.54 → 0.51 → 0.33

Numbers say: light vs heavy: width 149.7 → 236.4 px, dark 0.33 → 0.45.

## Refs v3 · #36 Magenta letters flat
Gouache 1.00 + water 15 % · 64 px · 47.6 s

![Refs v3 · #36 Magenta letters flat](Refs-v3-36-Magenta-letters-flat.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 18 % → 18 % | 52.0 px | 0.39 | 0.99 | 170 |
| heavy line | 21 % → 19 % | 60.8 px | 0.39 | 0.92 | 351 |
| pressure swell | 16 % → 16 % | 58.9 px | 0.39 | 1.00 | 254 |
| fast wave | 42 % → 33 % | 48.9 px | 0.39 | 0.77 | 842 |
| slow wave | 46 % → 36 % | 53.1 px | 0.38 | 0.79 | 1092 |
| spiral | 55 % → 36 % | 36.1 px | 0.39 | 0.65 | 1377 |
| loop | 39 % → 34 % | 51.0 px | 0.39 | 0.85 | 695 |
| tilted | 16 % → 16 % | 44.8 px | 0.40 | 1.01 | 805 |
| over the wet one | 35 % → 33 % | 52.4 px | 0.40 | 0.96 | 247 |
| long, no reload | 66 % → 40 % | 29.5 px | 0.37 | 0.61 | 1547 | quarters: 0.33 → 0.29 → 0.24 → 0.18

Numbers say: light vs heavy: width 52.0 → 60.8 px, dark 0.39 → 0.39.

## Refs v3 · #37 Oil still life
Gouache 1.00 + turpentine 20 % · 28 px · 36.1 s

![Refs v3 · #37 Oil still life](Refs-v3-37-Oil-still-life.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 9 % → 9 % | 26.9 px | 0.31 | 1.00 | 164 |
| heavy line | 10 % → 10 % | 29.2 px | 0.31 | 0.96 | 179 |
| pressure swell | 8 % → 8 % | 28.5 px | 0.35 | 1.02 | 76 |
| fast wave | 25 % → 10 % | 28.8 px | 0.39 | 0.41 | 323 |
| slow wave | 25 % → 10 % | 29.0 px | 0.34 | 0.39 | 789 |
| spiral | 39 % → 10 % | 25.5 px | 0.36 | 0.26 | 609 |
| loop | 21 % → 9 % | 26.7 px | 0.33 | 0.44 | 415 |
| tilted | 10 % → 10 % | 26.9 px | 0.36 | 1.02 | 326 |
| over the wet one | 20 % → 17 % | 27.9 px | 0.36 | 0.88 | 363 |
| long, no reload | 43 % → 10 % | 19.5 px | 0.33 | 0.24 | 640 | quarters: 0.19 → 0.06 → 0.01 → 0.00

Numbers say: light vs heavy: width 26.9 → 29.2 px, dark 0.31 → 0.31; pressure barely changes the width.

## Refs v3 · #38 Sanguine drawing
Charcoal 0.50 · Pastel 0.50 · 12 px · 11.3 s

![Refs v3 · #38 Sanguine drawing](Refs-v3-38-Sanguine-drawing.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 3 % → 3 % | 9.0 px | 0.31 | 1.00 | 34 |
| heavy line | 4 % → 4 % | 12.2 px | 0.31 | 1.00 | 36 |
| pressure swell | 3 % → 3 % | 9.5 px | 0.27 | 1.00 | 21 |
| fast wave | 10 % → 10 % | 11.4 px | 0.31 | 1.00 | 76 |
| slow wave | 10 % → 10 % | 11.4 px | 0.30 | 1.00 | 61 |
| spiral | 15 % → 15 % | 10.2 px | 0.30 | 1.00 | 136 |
| loop | 8 % → 8 % | 10.0 px | 0.31 | 1.00 | 124 |
| tilted | 4 % → 4 % | 10.8 px | 0.31 | 1.00 | 31 |
| over the wet one | 8 % → 8 % | 10.8 px | 0.31 | 1.00 | 47 |
| long, no reload | 18 % → 18 % | 8.1 px | 0.30 | 1.00 | 227 | quarters: 0.06 → 0.06 → 0.06 → 0.06

Numbers say: light vs heavy: width 9.0 → 12.2 px, dark 0.31 → 0.31; the long stroke does not run out of paint.

## Refs v3 · #39 Thick impasto weave
Impasto 1.00 · 96 px · 26.5 s

![Refs v3 · #39 Thick impasto weave](Refs-v3-39-Thick-impasto-weave.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 28 % → 24 % | 81.9 px | 0.47 | 0.84 | 330 |
| heavy line | 30 % → 18 % | 85.7 px | 0.46 | 0.62 | 462 |
| pressure swell | 23 % → 19 % | 84.5 px | 0.47 | 0.85 | 290 |
| fast wave | 60 % → 22 % | 69.9 px | 0.49 | 0.36 | 1174 |
| slow wave | 61 % → 20 % | 70.7 px | 0.47 | 0.33 | 1727 |
| spiral | 64 % → 21 % | 42.2 px | 0.50 | 0.33 | 2088 |
| loop | 56 % → 26 % | 72.0 px | 0.46 | 0.47 | 1037 |
| tilted | 21 % → 21 % | 59.2 px | 0.48 | 1.00 | 723 |
| over the wet one | 46 % → 36 % | 69.6 px | 0.48 | 0.77 | 547 |
| long, no reload | 83 % → 25 % | 37.0 px | 0.48 | 0.31 | 3357 | quarters: 0.45 → 0.37 → 0.32 → 0.25

Numbers say: light vs heavy: width 81.9 → 85.7 px, dark 0.47 → 0.46; pressure barely changes the width.

## Refs v3 · #40 Watercolour blooms
Watercolour 1.00 + water 55 % · 112 px · 68.3 s

![Refs v3 · #40 Watercolour blooms](Refs-v3-40-Watercolour-blooms.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 26 % → 47 % | 76.1 px | 0.07 | 1.78 | 338 |
| heavy line | 47 % → 57 % | 136.8 px | 0.08 | 1.21 | 523 |
| pressure swell | 30 % → 46 % | 113.5 px | 0.08 | 1.52 | 673 |
| fast wave | 78 % → 92 % | 90.4 px | 0.10 | 1.18 | 1393 |
| slow wave | 78 % → 87 % | 89.6 px | 0.09 | 1.13 | 2507 |
| spiral | 86 % → 91 % | 56.4 px | 0.08 | 1.07 | 3004 |
| loop | 67 % → 77 % | 86.2 px | 0.09 | 1.16 | 1417 |
| tilted | 35 % → 36 % | 97.0 px | 0.09 | 1.03 | 679 |
| over the wet one | 68 % → 87 % | 94.1 px | 0.09 | 1.27 | 444 |
| long, no reload | 97 % → 100 % | 43.6 px | 0.08 | 1.03 | 3143 | quarters: 0.11 → 0.09 → 0.08 → 0.06

Numbers say: light vs heavy: width 76.1 → 136.8 px, dark 0.07 → 0.08; wet paint spreads well beyond the stroke.

## Refs v3 · #41 Coloured pencil
Charcoal 0.50 · Pastel 0.50 · 12 px · 10.8 s

![Refs v3 · #41 Coloured pencil](Refs-v3-41-Coloured-pencil.png)

A light paint: laid on a grey sheet (on white it cannot be seen); **dark** = how far it is from the grey either way.

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 3 % → 3 % | 9.0 px | 0.39 | 1.00 | 25 |
| heavy line | 4 % → 4 % | 12.2 px | 0.39 | 1.00 | 25 |
| pressure swell | 3 % → 3 % | 9.5 px | 0.34 | 1.00 | 29 |
| fast wave | 10 % → 10 % | 11.4 px | 0.38 | 1.00 | 61 |
| slow wave | 10 % → 10 % | 11.4 px | 0.38 | 1.00 | 60 |
| spiral | 15 % → 15 % | 10.2 px | 0.39 | 1.00 | 140 |
| loop | 8 % → 8 % | 10.0 px | 0.39 | 1.00 | 59 |
| tilted | 4 % → 4 % | 10.8 px | 0.39 | 1.00 | 46 |
| over the wet one | 8 % → 8 % | 10.8 px | 0.39 | 1.00 | 33 |
| long, no reload | 18 % → 18 % | 8.1 px | 0.37 | 1.00 | 195 | quarters: 0.00 → 0.00 → 0.00 → 0.00

Numbers say: light vs heavy: width 9.0 → 12.2 px, dark 0.39 → 0.39; the long stroke does not run out of paint.

## Refs v3 · #42 Pink shaggy pastel
Pastel 1.00 · 38 px · 12.2 s

![Refs v3 · #42 Pink shaggy pastel](Refs-v3-42-Pink-shaggy-pastel.png)

A light paint: laid on a grey sheet (on white it cannot be seen); **dark** = how far it is from the grey either way.

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 7 % → 7 % | 20.5 px | 0.32 | 1.00 | 101 |
| heavy line | 11 % → 11 % | 33.0 px | 0.32 | 1.00 | 111 |
| pressure swell | 8 % → 8 % | 29.8 px | 0.32 | 1.00 | 112 |
| fast wave | 26 % → 26 % | 29.6 px | 0.32 | 1.00 | 339 |
| slow wave | 24 % → 24 % | 27.8 px | 0.32 | 1.00 | 555 |
| spiral | 39 % → 39 % | 25.6 px | 0.32 | 1.00 | 381 |
| loop | 20 % → 20 % | 25.3 px | 0.32 | 1.00 | 194 |
| tilted | 6 % → 6 % | 17.4 px | 0.31 | 1.00 | 135 |
| over the wet one | 16 % → 16 % | 26.8 px | 0.31 | 1.00 | 127 |
| long, no reload | 47 % → 47 % | 20.9 px | 0.32 | 1.00 | 764 | quarters: 0.00 → 0.00 → 0.00 → 0.00

Numbers say: light vs heavy: width 20.5 → 33.0 px, dark 0.32 → 0.32; the long stroke does not run out of paint.

## Refs v3 · #43 Dragged black blocks
Ink 0.93 · Gouache 0.07 · 112 px · 78.8 s

![Refs v3 · #43 Dragged black blocks](Refs-v3-43-Dragged-black-blocks.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 33 % → 36 % | 96.1 px | 0.85 | 1.08 | 400 |
| heavy line | 36 % → 37 % | 105.9 px | 0.85 | 1.02 | 619 |
| pressure swell | 27 % → 30 % | 101.1 px | 0.85 | 1.11 | 378 |
| fast wave | 73 % → 76 % | 84.0 px | 0.86 | 1.05 | 1367 |
| slow wave | 70 % → 70 % | 80.8 px | 0.86 | 1.00 | 2030 |
| spiral | 82 % → 81 % | 54.1 px | 0.84 | 0.99 | 2020 |
| loop | 63 % → 65 % | 82.2 px | 0.85 | 1.02 | 1066 |
| tilted | 27 % → 27 % | 75.9 px | 0.85 | 1.01 | 1101 |
| over the wet one | 56 % → 58 % | 80.4 px | 0.85 | 1.03 | 726 |
| long, no reload | 94 % → 96 % | 42.0 px | 0.85 | 1.02 | 3916 | quarters: 0.85 → 0.85 → 0.84 → 0.77

Numbers say: light vs heavy: width 96.1 → 105.9 px, dark 0.85 → 0.85; pressure barely changes the width; the long stroke does not run out of paint.

## Refs v3 · #44 Blue looping ribbon
Oil 0.52 · Gouache 0.48 + turpentine 10 % · 64 px · 47.9 s

![Refs v3 · #44 Blue looping ribbon](Refs-v3-44-Blue-looping-ribbon.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 20 % → 19 % | 57.0 px | 0.41 | 0.96 | 238 |
| heavy line | 20 % → 20 % | 59.5 px | 0.41 | 0.96 | 248 |
| pressure swell | 16 % → 16 % | 59.4 px | 0.44 | 0.98 | 173 |
| fast wave | 49 % → 26 % | 56.2 px | 0.48 | 0.53 | 683 |
| slow wave | 48 % → 29 % | 55.1 px | 0.45 | 0.61 | 1100 |
| spiral | 66 % → 29 % | 43.4 px | 0.43 | 0.45 | 1080 |
| loop | 42 % → 28 % | 54.5 px | 0.43 | 0.67 | 669 |
| tilted | 17 % → 17 % | 47.9 px | 0.45 | 1.00 | 408 |
| over the wet one | 36 % → 32 % | 51.6 px | 0.45 | 0.90 | 484 |
| long, no reload | 83 % → 28 % | 37.2 px | 0.43 | 0.33 | 2882 | quarters: 0.39 → 0.32 → 0.16 → 0.06

Numbers say: light vs heavy: width 57.0 → 59.5 px, dark 0.41 → 0.41; pressure barely changes the width.

## Refs v3 · #45 Pastel pepper
Pastel 1.00 · 64 px · 17.3 s

![Refs v3 · #45 Pastel pepper](Refs-v3-45-Pastel-pepper.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 11 % → 11 % | 33.1 px | 0.56 | 1.00 | 192 |
| heavy line | 19 % → 19 % | 55.0 px | 0.56 | 1.00 | 221 |
| pressure swell | 13 % → 13 % | 49.5 px | 0.56 | 1.00 | 155 |
| fast wave | 40 % → 40 % | 46.4 px | 0.56 | 1.00 | 507 |
| slow wave | 38 % → 38 % | 44.2 px | 0.56 | 1.00 | 1053 |
| spiral | 61 % → 61 % | 40.0 px | 0.56 | 1.00 | 851 |
| loop | 31 % → 31 % | 40.0 px | 0.56 | 1.00 | 457 |
| tilted | 9 % → 9 % | 24.0 px | 0.56 | 1.00 | 288 |
| over the wet one | 24 % → 24 % | 43.7 px | 0.56 | 1.00 | 209 |
| long, no reload | 69 % → 69 % | 31.0 px | 0.56 | 1.00 | 1653 | quarters: 0.42 → 0.41 → 0.42 → 0.42

Numbers say: light vs heavy: width 33.1 → 55.0 px, dark 0.56 → 0.56; the long stroke does not run out of paint.

## Refs v3 · #46 Ink lips on wet paper
Watercolour 1.00 + water 65 % · 56 px · 52.2 s

![Refs v3 · #46 Ink lips on wet paper](Refs-v3-46-Ink-lips-on-wet-paper.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 12 % → 29 % | 34.6 px | 0.62 | 2.45 | 123 |
| heavy line | 24 % → 37 % | 69.7 px | 0.64 | 1.55 | 182 |
| pressure swell | 14 % → 27 % | 53.7 px | 0.64 | 1.87 | 120 |
| fast wave | 48 % → 71 % | 55.0 px | 0.65 | 1.50 | 513 |
| slow wave | 45 % → 66 % | 52.1 px | 0.66 | 1.47 | 685 |
| spiral | 67 % → 78 % | 44.0 px | 0.67 | 1.17 | 849 |
| loop | 41 % → 58 % | 52.6 px | 0.66 | 1.43 | 511 |
| tilted | 19 % → 20 % | 54.1 px | 0.62 | 1.05 | 358 |
| over the wet one | 39 % → 62 % | 54.5 px | 0.62 | 1.58 | 254 |
| long, no reload | 81 % → 96 % | 36.5 px | 0.67 | 1.18 | 1463 | quarters: 0.72 → 0.72 → 0.68 → 0.59

Numbers say: light vs heavy: width 34.6 → 69.7 px, dark 0.62 → 0.64; wet paint spreads well beyond the stroke.

## Refs v3 · #47 Pink knife slabs
Gouache 1.00 + water 15 % · 240 px · 130.2 s

![Refs v3 · #47 Pink knife slabs](Refs-v3-47-Pink-knife-slabs.png)

A light paint: laid on a grey sheet (on white it cannot be seen); **dark** = how far it is from the grey either way.

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 65 % → 67 % | 189.7 px | 0.34 | 1.02 | 1030 |
| heavy line | 68 % → 64 % | 196.0 px | 0.34 | 0.94 | 1627 |
| pressure swell | 58 % → 67 % | 215.7 px | 0.31 | 1.16 | 1216 |
| fast wave | 94 % → 91 % | 108.4 px | 0.29 | 0.97 | 6561 |
| slow wave | 97 % → 85 % | 111.8 px | 0.33 | 0.88 | 7616 |
| spiral | 96 % → 82 % | 63.5 px | 0.32 | 0.85 | 7842 |
| loop | 98 % → 93 % | 126.4 px | 0.33 | 0.95 | 6197 |
| tilted | 49 % → 49 % | 136.5 px | 0.30 | 1.00 | 2191 |
| over the wet one | 85 % → 85 % | 100.9 px | 0.30 | 1.00 | 2005 |
| long, no reload | 99 % → 94 % | 44.2 px | 0.32 | 0.96 | 15534 | quarters: 0.00 → 0.00 → 0.00 → 0.00

Numbers say: light vs heavy: width 189.7 → 196.0 px, dark 0.34 → 0.34; pressure barely changes the width.

## Refs v3 · #48 Black bands with drips
Watercolour 1.00 + water 35 % · 112 px · 62.9 s

![Refs v3 · #48 Black bands with drips](Refs-v3-48-Black-bands-with-drips.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 32 % → 38 % | 93.4 px | 0.75 | 1.17 | 286 |
| heavy line | 34 % → 38 % | 97.8 px | 0.76 | 1.12 | 458 |
| pressure swell | 25 % → 32 % | 93.5 px | 0.75 | 1.29 | 344 |
| fast wave | 67 % → 77 % | 77.3 px | 0.72 | 1.15 | 1964 |
| slow wave | 66 % → 71 % | 76.8 px | 0.70 | 1.07 | 2815 |
| spiral | 75 % → 80 % | 49.3 px | 0.65 | 1.06 | 1944 |
| loop | 61 % → 65 % | 79.3 px | 0.76 | 1.06 | 1213 |
| tilted | 26 % → 27 % | 72.5 px | 0.75 | 1.05 | 658 |
| over the wet one | 54 % → 60 % | 77.3 px | 0.75 | 1.11 | 495 |
| long, no reload | 81 % → 91 % | 36.1 px | 0.61 | 1.13 | 3140 | quarters: 0.76 → 0.69 → 0.49 → 0.35

Numbers say: light vs heavy: width 93.4 → 97.8 px, dark 0.75 → 0.76; pressure barely changes the width.

## Refs v3 · #49 Magenta letters round
Ink 0.98 · 64 px · 43.1 s

![Refs v3 · #49 Magenta letters round](Refs-v3-49-Magenta-letters-round.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 7 % → 10 % | 21.3 px | 0.46 | 1.36 | 92 |
| heavy line | 20 % → 21 % | 57.2 px | 0.49 | 1.07 | 302 |
| pressure swell | 11 % → 13 % | 42.1 px | 0.51 | 1.13 | 169 |
| fast wave | 40 % → 43 % | 46.7 px | 0.53 | 1.06 | 670 |
| slow wave | 36 % → 40 % | 41.7 px | 0.49 | 1.11 | 813 |
| spiral | 60 % → 61 % | 39.5 px | 0.47 | 1.02 | 1365 |
| loop | 31 % → 34 % | 40.1 px | 0.49 | 1.10 | 575 |
| tilted | 19 % → 19 % | 53.9 px | 0.51 | 1.01 | 237 |
| over the wet one | 33 % → 35 % | 38.9 px | 0.51 | 1.06 | 174 |
| long, no reload | 78 % → 80 % | 35.0 px | 0.47 | 1.02 | 1342 | quarters: 0.42 → 0.42 → 0.40 → 0.38

Numbers say: light vs heavy: width 21.3 → 57.2 px, dark 0.46 → 0.49; the long stroke does not run out of paint.

## Refs v3 · #50 Swipes on seaside
Gouache 1.00 + water 15 % · 80 px · 59.8 s

![Refs v3 · #50 Swipes on seaside](Refs-v3-50-Swipes-on-seaside.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 24 % → 24 % | 69.8 px | 0.30 | 0.98 | 390 |
| heavy line | 25 % → 24 % | 73.0 px | 0.31 | 0.95 | 636 |
| pressure swell | 19 % → 19 % | 72.4 px | 0.32 | 1.00 | 315 |
| fast wave | 52 % → 42 % | 60.0 px | 0.32 | 0.81 | 1316 |
| slow wave | 54 % → 41 % | 62.1 px | 0.29 | 0.77 | 1416 |
| spiral | 62 % → 40 % | 41.0 px | 0.27 | 0.64 | 1651 |
| loop | 48 % → 43 % | 62.7 px | 0.29 | 0.88 | 850 |
| tilted | 20 % → 20 % | 54.5 px | 0.33 | 1.01 | 440 |
| over the wet one | 42 % → 40 % | 62.2 px | 0.33 | 0.96 | 325 |
| long, no reload | 76 % → 49 % | 34.0 px | 0.27 | 0.64 | 2548 | quarters: 0.26 → 0.24 → 0.19 → 0.13

Numbers say: light vs heavy: width 69.8 → 73.0 px, dark 0.30 → 0.31; pressure barely changes the width.

## Refs v3 · #01 HW peach cloud — own sheet
own sheet 800 × 1095 · Gouache 1.00 + turpentine 30 % · 104 px · 94.8 s

![Refs v3 · #01 HW peach cloud — own sheet](Refs-v3-01-HW-peach-cloud-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 7 % → 0 % | 100.7 px | 0.00 | 0.00 | 155 |
| stroke 2 | 4 % → 2 % | 102.1 px | 0.33 | 0.49 | 118 |
| stroke 3 | 14 % → 2 % | 145.3 px | 0.32 | 0.13 | 464 |
| stroke 4 | 18 % → 3 % | 233.6 px | 0.32 | 0.16 | 481 |
| stroke 5 | 26 % → 1 % | 544.8 px | 0.33 | 0.05 | 186 |
| stroke 6 | 20 % → 3 % | 295.8 px | 0.31 | 0.14 | 371 |
| stroke 7 | 23 % → 2 % | 310.9 px | 0.32 | 0.10 | 462 |
| stroke 8 | 23 % → 2 % | 302.1 px | 0.32 | 0.10 | 463 |
| stroke 9 | 26 % → 2 % | 322.4 px | 0.32 | 0.07 | 488 |
| stroke 10 | 29 % → 2 % | 288.1 px | 0.31 | 0.05 | 602 |
| stroke 11 | 38 % → 2 % | 313.3 px | 0.32 | 0.05 | 847 |
| stroke 12 | 45 % → 1 % | 391.0 px | 0.32 | 0.01 | 514 |
| stroke 13 | 54 % → 1 % | 616.1 px | 0.33 | 0.01 | 323 |
| stroke 14 | 52 % → 1 % | 1040.4 px | 0.33 | 0.01 | 143 |
| stroke 15 | 59 % → 0 % | 1313.5 px | 0.00 | 0.00 | 89 |
| stroke 16 | 63 % → 1 % | 871.5 px | 0.33 | 0.01 | 236 |
| stroke 17 | 2 % → 2 % | 25.3 px | 0.30 | 1.02 | 57 |
| stroke 18 | 5 % → 0 % | 36.4 px | 0.00 | 0.00 | 61 |
| stroke 19 | 7 % → 0 % | 50.7 px | 0.00 | 0.00 | 69 |
| stroke 20 | 8 % → 0 % | 88.5 px | 0.00 | 0.00 | 46 |
| stroke 21 | 9 % → 0 % | 145.0 px | 0.00 | 0.00 | 58 |
| stroke 22 | 10 % → 0 % | 227.5 px | 0.00 | 0.00 | 30 |
| stroke 23 | 10 % → 0 % | 295.7 px | 0.00 | 0.00 | 28 |
| stroke 24 | 11 % → 0 % | 621.7 px | 0.32 | 0.02 | 8 |
| stroke 25 | 2 % → 0 % | 37.8 px | 0.00 | 0.00 | 43 |
| stroke 26 | 4 % → 0 % | 42.5 px | 0.00 | 0.00 | 63 |
| stroke 27 | 5 % → 0 % | 117.8 px | 0.00 | 0.00 | 25 |
| stroke 28 | 3 % → 2 % | 184.6 px | 0.33 | 0.74 | 13 |
| stroke 29 | 5 % → 1 % | 148.4 px | 0.33 | 0.23 | 47 |
| stroke 30 | 6 % → 1 % | 238.9 px | 0.34 | 0.12 | 30 |
| stroke 31 | 7 % → 0 % | 270.7 px | 0.34 | 0.05 | 17 |
| stroke 32 | 7 % → 0 % | 290.7 px | 0.34 | 0.03 | 17 |
| stroke 33 | 7 % → 1 % | 154.9 px | 0.34 | 0.11 | 47 |
| stroke 34 | 8 % → 1 % | 147.2 px | 0.33 | 0.10 | 60 |
| stroke 35 | 11 % → 0 % | 561.7 px | 0.00 | 0.00 | 16 |
| stroke 36 | 8 % → 1 % | 189.1 px | 0.34 | 0.14 | 50 |
| stroke 37 | 10 % → 1 % | 150.7 px | 0.33 | 0.09 | 70 |
| stroke 38 | 12 % → 0 % | 197.5 px | 0.34 | 0.02 | 55 |
| stroke 39 | 13 % → 0 % | 229.9 px | 0.00 | 0.00 | 52 |
| stroke 40 | 13 % → 0 % | 223.0 px | 0.34 | 0.01 | 64 |
| stroke 41 | 15 % → 0 % | 355.0 px | 0.00 | 0.00 | 40 |
| stroke 42 | 17 % → 0 % | 480.0 px | 0.00 | 0.00 | 38 |
| stroke 43 | 18 % → 0 % | 391.2 px | 0.00 | 0.00 | 46 |
| stroke 44 | 18 % → 0 % | 457.6 px | 0.00 | 0.00 | 31 |
| stroke 45 | 19 % → 0 % | 686.5 px | 0.00 | 0.00 | 20 |
| stroke 46 | 19 % → 0 % | 820.0 px | 0.00 | 0.00 | 15 |
| stroke 47 | 19 % → 0 % | 1368.0 px | 0.00 | 0.00 | 14 |
| stroke 48 | 32 % → 0 % | 526.9 px | 0.00 | 0.00 | 38 |
| stroke 49 | 31 % → 0 % | 507.2 px | 0.00 | 0.00 | 44 |
| stroke 50 | 36 % → 0 % | 1936.3 px | 0.00 | 0.00 | 17 |
| stroke 51 | 1 % → 2 % | 39.4 px | 0.31 | 3.30 | 8 |
| stroke 52 | 1 % → 2 % | 49.9 px | 0.31 | 1.75 | 23 |
| stroke 53 | 2 % → 3 % | 96.3 px | 0.31 | 1.63 | 23 |
| stroke 54 | 15 % → 3 % | 1133.3 px | 0.33 | 0.20 | 13 |
| stroke 55 | 14 % → 3 % | 1033.2 px | 0.33 | 0.21 | 16 |
| stroke 56 | 12 % → 3 % | 951.3 px | 0.33 | 0.24 | 11 |
| stroke 57 | 11 % → 3 % | 857.6 px | 0.33 | 0.25 | 18 |
| stroke 58 | 10 % → 3 % | 795.4 px | 0.33 | 0.28 | 8 |
| stroke 59 | 9 % → 3 % | 541.1 px | 0.33 | 0.28 | 25 |
| stroke 60 | 8 % → 3 % | 454.4 px | 0.33 | 0.33 | 17 |
| stroke 61 | 3 % → 5 % | 138.0 px | 0.31 | 1.71 | 26 |
| stroke 62 | 4 % → 4 % | 74.2 px | 0.31 | 1.02 | 132 |
| stroke 63 | 5 % → 5 % | 368.0 px | 0.31 | 0.87 | 4 |
| stroke 64 | 6 % → 3 % | 202.1 px | 0.31 | 0.56 | 28 |
| stroke 65 | 7 % → 3 % | 94.3 px | 0.31 | 0.35 | 204 |
| stroke 66 | 10 % → 2 % | 333.0 px | 0.31 | 0.15 | 30 |
| stroke 67 | 10 % → 1 % | 75.3 px | 0.32 | 0.09 | 164 |
| stroke 68 | 13 % → 1 % | 289.5 px | 0.33 | 0.07 | 42 |
| stroke 69 | 14 % → 1 % | 84.7 px | 0.33 | 0.05 | 224 |
| stroke 70 | 18 % → 1 % | 105.5 px | 0.33 | 0.04 | 202 |
| stroke 71 | 10 % → 3 % | 254.3 px | 0.31 | 0.32 | 70 |
| stroke 72 | 10 % → 3 % | 366.0 px | 0.31 | 0.31 | 27 |
| stroke 73 | 7 % → 3 % | 91.7 px | 0.33 | 0.35 | 42 |
| stroke 74 | 10 % → 2 % | 54.4 px | 0.33 | 0.19 | 221 |
| stroke 75 | 14 % → 2 % | 94.8 px | 0.33 | 0.15 | 171 |
| stroke 76 | 11 % → 0 % | 456.7 px | 0.00 | 0.00 | 8 |
| stroke 77 | 14 % → 3 % | 909.1 px | 0.30 | 0.24 | 14 |
| stroke 78 | 17 % → 3 % | 297.6 px | 0.31 | 0.17 | 80 |
| stroke 79 | 20 % → 3 % | 498.8 px | 0.31 | 0.17 | 38 |
| stroke 80 | 1 % → 0 % | 42.8 px | 0.00 | 0.00 | 8 |
| stroke 81 | 1 % → 0 % | 57.5 px | 0.00 | 0.00 | 11 |
| stroke 82 | 8 % → 0 % | 137.4 px | 0.00 | 0.00 | 22 |
| stroke 83 | 9 % → 0 % | 315.3 px | 0.00 | 0.00 | 12 |
| stroke 84 | 10 % → 0 % | 499.6 px | 0.00 | 0.00 | 5 |
| stroke 85 | 8 % → 0 % | 103.5 px | 0.00 | 0.00 | 75 |
| stroke 86 | 10 % → 0 % | 118.8 px | 0.00 | 0.00 | 70 |
| stroke 87 | 14 % → 0 % | 343.8 px | 0.00 | 0.00 | 22 |
| stroke 88 | 12 % → 0 % | 214.6 px | 0.00 | 0.00 | 47 |
| stroke 89 | 15 % → 0 % | 1052.6 px | 0.00 | 0.00 | 5 |
| stroke 90 | 17 % → 0 % | 1021.6 px | 0.00 | 0.00 | 8 |
| stroke 91 | 9 % → 0 % | 495.0 px | 0.00 | 0.00 | 23 |
| stroke 92 | 1 % → 0 % | 29.6 px | 0.33 | 0.88 | 8 |
| stroke 93 | 3 % → 1 % | 33.9 px | 0.33 | 0.31 | 36 |
| stroke 94 | 1 % → 1 % | 30.9 px | 0.33 | 1.39 | 27 |
| stroke 95 | 2 % → 4 % | 46.7 px | 0.31 | 2.28 | 34 |
| stroke 96 | 2 % → 4 % | 81.1 px | 0.30 | 1.96 | 17 |
| stroke 97 | 2 % → 3 % | 106.5 px | 0.33 | 1.58 | 5 |
| stroke 98 | 3 % → 3 % | 54.3 px | 0.33 | 0.82 | 30 |
| stroke 99 | 2 % → 2 % | 118.2 px | 0.33 | 0.84 | 10 |
| stroke 100 | 1 % → 4 % | 60.5 px | 0.30 | 3.67 | 6 |
| stroke 101 | 4 % → 1 % | 52.6 px | 0.32 | 0.20 | 52 |
| stroke 102 | 7 % → 1 % | 81.0 px | 0.31 | 0.09 | 72 |
| stroke 103 | 2 % → 2 % | 33.8 px | 0.30 | 1.02 | 45 |
| stroke 104 | 3 % → 0 % | 162.5 px | 0.31 | 0.06 | 5 |
| stroke 105 | 4 % → 0 % | 91.6 px | 0.00 | 0.00 | 19 |
| stroke 106 | 4 % → 0 % | 184.7 px | 0.31 | 0.01 | 14 |
| stroke 107 | 7 % → 0 % | 179.5 px | 0.00 | 0.00 | 8 |
| stroke 108 | 1 % → 1 % | 39.3 px | 0.33 | 0.65 | 18 |
| stroke 109 | 2 % → 1 % | 139.8 px | 0.33 | 0.43 | 12 |
| stroke 110 | 4 % → 1 % | 64.4 px | 0.33 | 0.24 | 43 |
| stroke 111 | 6 % → 1 % | 88.5 px | 0.33 | 0.18 | 94 |
| stroke 112 | 7 % → 1 % | 106.8 px | 0.33 | 0.15 | 74 |
| stroke 113 | 10 % → 1 % | 172.9 px | 0.33 | 0.08 | 42 |
| stroke 114 | 12 % → 0 % | 507.8 px | 0.00 | 0.00 | 14 |
| stroke 115 | 14 % → 0 % | 607.3 px | 0.00 | 0.00 | 7 |
| stroke 116 | 1 % → 2 % | 49.2 px | 0.33 | 4.24 | 8 |
| stroke 117 | 1 % → 3 % | 88.8 px | 0.33 | 2.68 | 9 |
| stroke 118 | 2 % → 4 % | 73.7 px | 0.32 | 2.36 | 31 |
| stroke 119 | 3 % → 4 % | 65.3 px | 0.32 | 1.63 | 44 |
| stroke 120 | 4 % → 4 % | 60.6 px | 0.31 | 1.02 | 116 |
| stroke 121 | 6 % → 5 % | 194.4 px | 0.31 | 0.82 | 23 |
| stroke 122 | 7 % → 3 % | 567.4 px | 0.30 | 0.50 | 12 |
| stroke 123 | 7 % → 4 % | 292.1 px | 0.30 | 0.54 | 37 |
| stroke 124 | 8 % → 4 % | 272.3 px | 0.30 | 0.48 | 103 |
| stroke 125 | 8 % → 3 % | 124.7 px | 0.30 | 0.37 | 169 |
| stroke 126 | 4 % → 3 % | 286.2 px | 0.30 | 0.61 | 18 |
| stroke 127 | 10 % → 3 % | 148.1 px | 0.30 | 0.31 | 136 |
| stroke 128 | 4 % → 2 % | 147.7 px | 0.30 | 0.40 | 50 |
| stroke 129 | 11 % → 3 % | 120.9 px | 0.30 | 0.23 | 240 |
| stroke 130 | 9 % → 3 % | 177.3 px | 0.30 | 0.29 | 108 |
| stroke 131 | 15 % → 3 % | 251.5 px | 0.30 | 0.20 | 101 |
| stroke 132 | 16 % → 3 % | 399.1 px | 0.30 | 0.19 | 75 |
| stroke 133 | 8 % → 1 % | 268.0 px | 0.30 | 0.18 | 29 |
| stroke 134 | 7 % → 0 % | 659.0 px | 0.31 | 0.07 | 8 |
| stroke 135 | 9 % → 2 % | 196.5 px | 0.33 | 0.28 | 55 |
| stroke 136 | 9 % → 2 % | 218.6 px | 0.33 | 0.26 | 45 |
| stroke 137 | 10 % → 2 % | 303.1 px | 0.33 | 0.24 | 72 |
| stroke 138 | 10 % → 3 % | 115.0 px | 0.33 | 0.26 | 128 |
| stroke 139 | 11 % → 1 % | 150.7 px | 0.31 | 0.10 | 72 |
| stroke 140 | 13 % → 2 % | 98.2 px | 0.33 | 0.15 | 336 |
| stroke 141 | 16 % → 3 % | 235.4 px | 0.31 | 0.21 | 105 |
| stroke 142 | 17 % → 3 % | 612.8 px | 0.30 | 0.19 | 55 |
| stroke 143 | 16 % → 3 % | 176.8 px | 0.31 | 0.20 | 261 |
| stroke 144 | 18 % → 4 % | 574.5 px | 0.30 | 0.21 | 48 |
| stroke 145 | 18 % → 1 % | 1695.1 px | 0.31 | 0.04 | 11 |
| stroke 146 | 16 % → 0 % | 1597.2 px | 0.31 | 0.02 | 7 |
| stroke 147 | 16 % → 0 % | 1516.7 px | 0.30 | 0.01 | 8 |
| stroke 148 | 15 % → 0 % | 1002.6 px | 0.31 | 0.00 | 13 |
| stroke 149 | 13 % → 0 % | 512.7 px | 0.00 | 0.00 | 19 |
| stroke 150 | 13 % → 0 % | 1301.8 px | 0.00 | 0.00 | 5 |
| stroke 151 | 12 % → 0 % | 737.1 px | 0.00 | 0.00 | 6 |
| stroke 152 | 12 % → 0 % | 735.9 px | 0.00 | 0.00 | 7 |
| stroke 153 | 11 % → 0 % | 1018.9 px | 0.00 | 0.00 | 10 |
| stroke 154 | 10 % → 0 % | 919.9 px | 0.00 | 0.00 | 8 |
| stroke 155 | 12 % → 0 % | 609.8 px | 0.00 | 0.00 | 28 |
| stroke 156 | 15 % → 0 % | 185.0 px | 0.00 | 0.00 | 135 |
| stroke 157 | 17 % → 0 % | 215.9 px | 0.31 | 0.01 | 165 |
| stroke 158 | 18 % → 0 % | 218.8 px | 0.31 | 0.00 | 101 |
| stroke 159 | 18 % → 0 % | 247.4 px | 0.31 | 0.00 | 136 |
| stroke 160 | 19 % → 0 % | 431.1 px | 0.00 | 0.00 | 76 |
| stroke 161 | 19 % → 0 % | 389.1 px | 0.00 | 0.00 | 51 |
| stroke 162 | 25 % → 0 % | 499.7 px | 0.00 | 0.00 | 42 |
| stroke 163 | 26 % → 0 % | 763.1 px | 0.00 | 0.00 | 21 |
| stroke 164 | 26 % → 0 % | 636.3 px | 0.00 | 0.00 | 46 |
| stroke 165 | 2 % → 4 % | 24.2 px | 0.31 | 2.34 | 42 |
| stroke 166 | 1 % → 4 % | 30.2 px | 0.30 | 7.69 | 11 |
| stroke 167 | 2 % → 4 % | 151.7 px | 0.31 | 1.81 | 3 |
| stroke 168 | 4 % → 5 % | 79.4 px | 0.31 | 1.25 | 19 |
| stroke 169 | 2 % → 2 % | 35.6 px | 0.33 | 1.09 | 38 |
| stroke 170 | 2 % → 2 % | 136.9 px | 0.32 | 0.87 | 3 |
| stroke 171 | 3 % → 0 % | 33.2 px | 0.28 | 0.15 | 58 |
| stroke 172 | 2 % → 0 % | 26.2 px | 0.00 | 0.00 | 17 |
| stroke 173 | 1 % → 2 % | 28.2 px | 0.33 | 1.45 | 38 |
| stroke 174 | 2 % → 2 % | 38.0 px | 0.33 | 0.79 | 75 |
| stroke 175 | 3 % → 2 % | 68.2 px | 0.33 | 0.65 | 55 |
| stroke 176 | 4 % → 2 % | 365.8 px | 0.33 | 0.62 | 14 |
| stroke 177 | 4 % → 3 % | 378.1 px | 0.32 | 0.63 | 9 |
| stroke 178 | 5 % → 3 % | 416.1 px | 0.33 | 0.55 | 4 |
| stroke 179 | 5 % → 2 % | 170.5 px | 0.33 | 0.44 | 33 |
| stroke 180 | 6 % → 3 % | 122.8 px | 0.32 | 0.51 | 45 |
| stroke 181 | 7 % → 4 % | 300.0 px | 0.32 | 0.63 | 18 |
| stroke 182 | 7 % → 5 % | 473.1 px | 0.31 | 0.73 | 7 |
| stroke 183 | 7 % → 4 % | 107.2 px | 0.31 | 0.58 | 55 |
| stroke 184 | 8 % → 3 % | 81.0 px | 0.31 | 0.43 | 114 |
| stroke 185 | 12 % → 4 % | 738.1 px | 0.31 | 0.38 | 8 |
| stroke 186 | 10 % → 3 % | 141.4 px | 0.31 | 0.33 | 79 |
| stroke 187 | 14 % → 4 % | 577.3 px | 0.30 | 0.27 | 17 |
| stroke 188 | 11 % → 2 % | 225.2 px | 0.30 | 0.19 | 38 |
| stroke 189 | 13 % → 3 % | 156.7 px | 0.30 | 0.22 | 102 |
| stroke 190 | 13 % → 3 % | 158.5 px | 0.30 | 0.20 | 112 |
| stroke 191 | 16 % → 3 % | 231.4 px | 0.30 | 0.19 | 68 |
| stroke 192 | 20 % → 4 % | 1274.8 px | 0.30 | 0.20 | 12 |
| stroke 193 | 15 % → 1 % | 449.6 px | 0.30 | 0.10 | 36 |
| stroke 194 | 14 % → 1 % | 1274.2 px | 0.31 | 0.04 | 3 |
| stroke 195 | 6 % → 0 % | 155.1 px | 0.00 | 0.00 | 14 |
| stroke 196 | 7 % → 0 % | 113.1 px | 0.00 | 0.00 | 30 |
| stroke 197 | 8 % → 0 % | 119.0 px | 0.00 | 0.00 | 62 |
| stroke 198 | 14 % → 0 % | 152.0 px | 0.00 | 0.00 | 196 |
| stroke 199 | 15 % → 0 % | 145.6 px | 0.00 | 0.00 | 79 |
| stroke 200 | 17 % → 0 % | 164.1 px | 0.00 | 0.00 | 102 |
| stroke 201 | 15 % → 0 % | 195.2 px | 0.00 | 0.00 | 62 |
| stroke 202 | 16 % → 0 % | 255.5 px | 0.00 | 0.00 | 44 |
| stroke 203 | 18 % → 0 % | 423.6 px | 0.00 | 0.00 | 19 |
| stroke 204 | 19 % → 0 % | 548.6 px | 0.00 | 0.00 | 9 |
| stroke 205 | 21 % → 0 % | 535.9 px | 0.00 | 0.00 | 12 |
| stroke 206 | 22 % → 0 % | 582.5 px | 0.00 | 0.00 | 6 |
| stroke 207 | 2 % → 0 % | 25.0 px | 0.00 | 0.00 | 114 |
| stroke 208 | 4 % → 1 % | 67.1 px | 0.33 | 0.22 | 90 |
| stroke 209 | 4 % → 1 % | 66.0 px | 0.33 | 0.18 | 65 |
| stroke 210 | 1 % → 3 % | 31.4 px | 0.33 | 3.42 | 15 |
| stroke 211 | 1 % → 4 % | 27.4 px | 0.31 | 5.04 | 18 |
| stroke 212 | 2 % → 3 % | 109.3 px | 0.33 | 1.12 | 11 |
| stroke 213 | 1 % → 4 % | 25.6 px | 0.30 | 3.49 | 13 |
| stroke 214 | 3 % → 3 % | 88.1 px | 0.33 | 0.99 | 32 |
| stroke 215 | 3 % → 2 % | 52.5 px | 0.33 | 0.53 | 98 |
| stroke 216 | 1 % → 2 % | 63.0 px | 0.30 | 2.28 | 5 |
| stroke 217 | 4 % → 0 % | 125.0 px | 0.00 | 0.00 | 26 |
| stroke 218 | 5 % → 0 % | 150.2 px | 0.00 | 0.00 | 42 |
| stroke 219 | 2 % → 1 % | 88.7 px | 0.30 | 0.51 | 13 |
| stroke 220 | 3 % → 1 % | 70.0 px | 0.31 | 0.25 | 48 |
| stroke 221 | 3 % → 0 % | 200.4 px | 0.31 | 0.08 | 17 |
| stroke 222 | 5 % → 0 % | 120.2 px | 0.00 | 0.00 | 26 |
| stroke 223 | 5 % → 0 % | 202.8 px | 0.00 | 0.00 | 28 |
| stroke 224 | 2 % → 0 % | 42.0 px | 0.00 | 0.00 | 59 |
| stroke 225 | 3 % → 0 % | 58.0 px | 0.00 | 0.00 | 42 |
| stroke 226 | 3 % → 0 % | 137.5 px | 0.00 | 0.00 | 11 |
| stroke 227 | 2 % → 0 % | 43.3 px | 0.34 | 0.18 | 30 |
| stroke 228 | 4 % → 1 % | 50.9 px | 0.34 | 0.26 | 62 |
| stroke 229 | 5 % → 0 % | 156.4 px | 0.00 | 0.00 | 22 |
| stroke 230 | 5 % → 1 % | 106.9 px | 0.33 | 0.27 | 46 |
| stroke 231 | 2 % → 4 % | 40.5 px | 0.31 | 1.58 | 144 |
| stroke 232 | 5 % → 2 % | 45.7 px | 0.30 | 0.42 | 260 |
| stroke 233 | 7 % → 2 % | 60.6 px | 0.30 | 0.29 | 281 |
| stroke 234 | 9 % → 2 % | 76.0 px | 0.30 | 0.23 | 269 |
| stroke 235 | 15 % → 4 % | 1006.8 px | 0.30 | 0.26 | 15 |
| stroke 236 | 9 % → 2 % | 107.6 px | 0.30 | 0.24 | 171 |
| stroke 237 | 9 % → 2 % | 80.6 px | 0.31 | 0.26 | 304 |
| stroke 238 | 9 % → 2 % | 79.1 px | 0.31 | 0.24 | 525 |
| stroke 239 | 11 % → 3 % | 149.4 px | 0.31 | 0.27 | 119 |
| stroke 240 | 16 % → 2 % | 229.5 px | 0.33 | 0.11 | 111 |
| stroke 241 | 17 % → 1 % | 236.7 px | 0.32 | 0.07 | 99 |
| stroke 242 | 18 % → 2 % | 196.0 px | 0.32 | 0.12 | 188 |
| stroke 243 | 20 % → 3 % | 228.9 px | 0.32 | 0.16 | 217 |
| stroke 244 | 23 % → 2 % | 1390.0 px | 0.30 | 0.07 | 30 |
| stroke 245 | 14 % → 0 % | 805.2 px | 0.00 | 0.00 | 11 |
| stroke 246 | 22 % → 0 % | 1214.8 px | 0.00 | 0.00 | 13 |
| stroke 247 | 16 % → 0 % | 630.1 px | 0.00 | 0.00 | 30 |
| stroke 248 | 16 % → 0 % | 434.1 px | 0.00 | 0.00 | 47 |
| stroke 249 | 23 % → 0 % | 800.9 px | 0.00 | 0.00 | 112 |
| stroke 250 | 18 % → 0 % | 608.2 px | 0.00 | 0.00 | 94 |
| stroke 251 | 18 % → 0 % | 327.2 px | 0.00 | 0.00 | 53 |
| stroke 252 | 10 % → 0 % | 452.9 px | 0.00 | 0.00 | 18 |
| stroke 253 | 26 % → 0 % | 1309.6 px | 0.00 | 0.00 | 26 |
| stroke 254 | 22 % → 0 % | 1094.1 px | 0.00 | 0.00 | 15 |
| stroke 255 | 21 % → 0 % | 352.6 px | 0.00 | 0.00 | 40 |
| stroke 256 | 11 % → 0 % | 372.8 px | 0.00 | 0.00 | 25 |
| stroke 257 | 26 % → 0 % | 538.5 px | 0.00 | 0.00 | 41 |
| stroke 258 | 23 % → 0 % | 311.4 px | 0.00 | 0.00 | 57 |
| stroke 259 | 12 % → 0 % | 475.2 px | 0.00 | 0.00 | 80 |
| stroke 260 | 27 % → 0 % | 671.8 px | 0.00 | 0.00 | 50 |
| stroke 261 | 25 % → 0 % | 276.0 px | 0.00 | 0.00 | 91 |
| stroke 262 | 28 % → 0 % | 798.0 px | 0.00 | 0.00 | 34 |
| stroke 263 | 29 % → 0 % | 230.6 px | 0.00 | 0.00 | 98 |
| stroke 264 | 31 % → 0 % | 323.7 px | 0.00 | 0.00 | 69 |
| stroke 265 | 11 % → 0 % | 350.3 px | 0.00 | 0.00 | 14 |
| stroke 266 | 33 % → 0 % | 387.1 px | 0.00 | 0.00 | 58 |
| stroke 267 | 35 % → 0 % | 191.9 px | 0.00 | 0.00 | 150 |
| stroke 268 | 32 % → 0 % | 218.6 px | 0.00 | 0.00 | 122 |
| stroke 269 | 27 % → 0 % | 298.9 px | 0.00 | 0.00 | 64 |
| stroke 270 | 1 % → 1 % | 19.4 px | 0.31 | 2.65 | 5 |
| stroke 271 | 1 % → 3 % | 28.4 px | 0.33 | 2.19 | 27 |
| stroke 272 | 2 % → 2 % | 29.5 px | 0.30 | 1.13 | 81 |
| stroke 273 | 2 % → 2 % | 84.4 px | 0.33 | 1.32 | 10 |

Numbers say: wet paint spreads well beyond the stroke.

## Refs v3 · #02 HW cream strokes — own sheet
own sheet 800 × 650 · Gouache 1.00 + turpentine 30 % · 51 px · 39.0 s

![Refs v3 · #02 HW cream strokes — own sheet](Refs-v3-02-HW-cream-strokes-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 10 % → 0 % | 50.2 px | 0.00 | 0.00 | 69 |
| stroke 2 | 14 % → 0 % | 101.8 px | 0.00 | 0.00 | 43 |
| stroke 3 | 8 % → 0 % | 50.4 px | 0.00 | 0.00 | 42 |
| stroke 4 | 10 % → 0 % | 93.5 px | 0.00 | 0.00 | 41 |
| stroke 5 | 13 % → 0 % | 150.0 px | 0.00 | 0.00 | 19 |
| stroke 6 | 16 % → 0 % | 177.1 px | 0.00 | 0.00 | 31 |
| stroke 7 | 20 % → 0 % | 181.2 px | 0.00 | 0.00 | 45 |
| stroke 8 | 21 % → 0 % | 282.8 px | 0.00 | 0.00 | 30 |
| stroke 9 | 22 % → 0 % | 220.3 px | 0.00 | 0.00 | 29 |
| stroke 10 | 21 % → 0 % | 211.2 px | 0.00 | 0.00 | 20 |
| stroke 11 | 20 % → 0 % | 93.8 px | 0.00 | 0.00 | 90 |
| stroke 12 | 28 % → 0 % | 230.8 px | 0.00 | 0.00 | 32 |
| stroke 13 | 15 % → 0 % | 267.6 px | 0.00 | 0.00 | 16 |
| stroke 14 | 33 % → 0 % | 406.9 px | 0.00 | 0.00 | 15 |
| stroke 15 | 8 % → 0 % | 72.9 px | 0.00 | 0.00 | 29 |
| stroke 16 | 21 % → 0 % | 70.5 px | 0.00 | 0.00 | 210 |
| stroke 17 | 21 % → 0 % | 228.2 px | 0.00 | 0.00 | 36 |
| stroke 18 | 16 % → 0 % | 56.9 px | 0.00 | 0.00 | 458 |
| stroke 19 | 21 % → 0 % | 63.5 px | 0.00 | 0.00 | 225 |
| stroke 20 | 32 % → 0 % | 149.2 px | 0.00 | 0.00 | 103 |
| stroke 21 | 38 % → 1 % | 212.2 px | 0.58 | 0.01 | 95 |
| stroke 22 | 13 % → 1 % | 50.5 px | 0.59 | 0.10 | 130 |
| stroke 23 | 24 % → 8 % | 80.3 px | 0.59 | 0.33 | 181 |
| stroke 24 | 32 % → 13 % | 91.7 px | 0.59 | 0.41 | 264 |
| stroke 25 | 36 % → 17 % | 104.6 px | 0.59 | 0.48 | 303 |
| stroke 26 | 45 % → 21 % | 388.4 px | 0.59 | 0.46 | 37 |
| stroke 27 | 26 % → 47 % | 444.6 px | 0.59 | 1.84 | 23 |
| stroke 28 | 28 % → 17 % | 176.4 px | 0.59 | 0.62 | 103 |
| stroke 29 | 25 % → 22 % | 132.8 px | 0.59 | 0.89 | 109 |
| stroke 30 | 11 % → 0 % | 143.8 px | 0.00 | 0.00 | 17 |
| stroke 31 | 28 % → 12 % | 122.7 px | 0.59 | 0.43 | 93 |
| stroke 32 | 30 % → 14 % | 134.8 px | 0.59 | 0.47 | 129 |
| stroke 33 | 1 % → 0 % | 18.3 px | 0.00 | 0.00 | 3 |
| stroke 34 | 5 % → 18 % | 27.0 px | 0.58 | 3.46 | 92 |
| stroke 35 | 2 % → 0 % | 42.0 px | 0.00 | 0.00 | 11 |
| stroke 36 | 5 % → 0 % | 65.6 px | 0.00 | 0.00 | 19 |
| stroke 37 | 7 % → 0 % | 109.5 px | 0.00 | 0.00 | 15 |
| stroke 38 | 3 % → 0 % | 37.5 px | 0.00 | 0.00 | 15 |
| stroke 39 | 2 % → 0 % | 47.7 px | 0.00 | 0.00 | 12 |
| stroke 40 | 15 % → 0 % | 43.7 px | 0.00 | 0.00 | 509 |
| stroke 41 | 20 % → 0 % | 84.0 px | 0.00 | 0.00 | 166 |
| stroke 42 | 23 % → 0 % | 212.5 px | 0.00 | 0.00 | 36 |
| stroke 43 | 16 % → 0 % | 98.6 px | 0.00 | 0.00 | 96 |
| stroke 44 | 21 % → 0 % | 120.5 px | 0.00 | 0.00 | 97 |
| stroke 45 | 29 % → 0 % | 388.9 px | 0.00 | 0.00 | 34 |
| stroke 46 | 24 % → 0 % | 427.7 px | 0.00 | 0.00 | 16 |
| stroke 47 | 16 % → 0 % | 135.4 px | 0.00 | 0.00 | 47 |
| stroke 48 | 27 % → 0 % | 120.2 px | 0.00 | 0.00 | 240 |
| stroke 49 | 30 % → 0 % | 214.2 px | 0.00 | 0.00 | 78 |
| stroke 50 | 30 % → 0 % | 379.7 px | 0.00 | 0.00 | 41 |
| stroke 51 | 31 % → 0 % | 262.1 px | 0.00 | 0.00 | 64 |
| stroke 52 | 29 % → 0 % | 164.9 px | 0.00 | 0.00 | 114 |
| stroke 53 | 34 % → 0 % | 591.0 px | 0.00 | 0.00 | 10 |
| stroke 54 | 25 % → 0 % | 284.3 px | 0.00 | 0.00 | 29 |
| stroke 55 | 22 % → 0 % | 289.2 px | 0.00 | 0.00 | 17 |
| stroke 56 | 17 % → 0 % | 189.1 px | 0.00 | 0.00 | 28 |
| stroke 57 | 29 % → 0 % | 709.8 px | 0.00 | 0.00 | 12 |
| stroke 58 | 19 % → 0 % | 117.0 px | 0.00 | 0.00 | 54 |
| stroke 59 | 15 % → 0 % | 346.0 px | 0.00 | 0.00 | 18 |
| stroke 60 | 27 % → 0 % | 368.1 px | 0.00 | 0.00 | 38 |
| stroke 61 | 21 % → 0 % | 172.3 px | 0.00 | 0.00 | 46 |
| stroke 62 | 29 % → 0 % | 385.2 px | 0.00 | 0.00 | 22 |
| stroke 63 | 26 % → 0 % | 203.6 px | 0.00 | 0.00 | 43 |
| stroke 64 | 30 % → 0 % | 712.5 px | 0.00 | 0.00 | 13 |
| stroke 65 | 4 % → 0 % | 40.4 px | 0.00 | 0.00 | 14 |
| stroke 66 | 14 % → 0 % | 62.3 px | 0.00 | 0.00 | 134 |
| stroke 67 | 16 % → 0 % | 186.7 px | 0.00 | 0.00 | 23 |
| stroke 68 | 18 % → 0 % | 98.4 px | 0.00 | 0.00 | 92 |
| stroke 69 | 19 % → 0 % | 92.7 px | 0.00 | 0.00 | 233 |
| stroke 70 | 15 % → 0 % | 366.4 px | 0.00 | 0.00 | 14 |
| stroke 71 | 12 % → 0 % | 186.2 px | 0.00 | 0.00 | 35 |
| stroke 72 | 6 % → 0 % | 92.6 px | 0.00 | 0.00 | 24 |
| stroke 73 | 11 % → 0 % | 52.4 px | 0.00 | 0.00 | 192 |
| stroke 74 | 13 % → 0 % | 98.1 px | 0.58 | 0.00 | 59 |
| stroke 75 | 14 % → 1 % | 140.0 px | 0.59 | 0.07 | 38 |
| stroke 76 | 17 % → 1 % | 302.1 px | 0.59 | 0.04 | 22 |
| stroke 77 | 18 % → 10 % | 71.9 px | 0.59 | 0.57 | 128 |
| stroke 78 | 31 % → 0 % | 594.2 px | 0.00 | 0.00 | 6 |
| stroke 79 | 24 % → 14 % | 76.9 px | 0.59 | 0.60 | 171 |
| stroke 80 | 17 % → 31 % | 194.1 px | 0.59 | 1.80 | 22 |
| stroke 81 | 35 % → 5 % | 231.4 px | 0.59 | 0.14 | 61 |
| stroke 82 | 18 % → 39 % | 233.6 px | 0.59 | 2.18 | 16 |
| stroke 83 | 35 % → 6 % | 248.0 px | 0.59 | 0.16 | 43 |
| stroke 84 | 23 % → 42 % | 251.7 px | 0.59 | 1.85 | 37 |
| stroke 85 | 3 % → 0 % | 24.1 px | 0.00 | 0.00 | 32 |
| stroke 86 | 5 % → 0 % | 27.5 px | 0.58 | 0.00 | 92 |
| stroke 87 | 5 % → 33 % | 38.7 px | 0.59 | 6.18 | 52 |
| stroke 88 | 1 % → 0 % | 22.4 px | 0.00 | 0.00 | 20 |
| stroke 89 | 4 % → 0 % | 40.0 px | 0.00 | 0.00 | 44 |
| stroke 90 | 9 % → 0 % | 47.9 px | 0.00 | 0.00 | 51 |
| stroke 91 | 10 % → 0 % | 90.4 px | 0.00 | 0.00 | 27 |
| stroke 92 | 8 % → 0 % | 200.7 px | 0.00 | 0.00 | 6 |
| stroke 93 | 15 % → 0 % | 53.6 px | 0.00 | 0.00 | 237 |
| stroke 94 | 20 % → 0 % | 76.1 px | 0.00 | 0.00 | 203 |
| stroke 95 | 34 % → 0 % | 197.8 px | 0.00 | 0.00 | 85 |
| stroke 96 | 30 % → 0 % | 103.2 px | 0.00 | 0.00 | 201 |
| stroke 97 | 30 % → 0 % | 121.0 px | 0.00 | 0.00 | 101 |
| stroke 98 | 32 % → 0 % | 109.5 px | 0.00 | 0.00 | 127 |
| stroke 99 | 33 % → 0 % | 113.6 px | 0.00 | 0.00 | 112 |
| stroke 100 | 35 % → 0 % | 203.4 px | 0.00 | 0.00 | 40 |
| stroke 101 | 37 % → 0 % | 330.4 px | 0.00 | 0.00 | 27 |
| stroke 102 | 5 % → 0 % | 43.9 px | 0.00 | 0.00 | 33 |
| stroke 103 | 7 % → 0 % | 62.5 px | 0.00 | 0.00 | 35 |
| stroke 104 | 9 % → 0 % | 223.2 px | 0.00 | 0.00 | 10 |
| stroke 105 | 2 % → 0 % | 23.0 px | 0.00 | 0.00 | 9 |
| stroke 106 | 3 % → 0 % | 50.5 px | 0.00 | 0.00 | 7 |
| stroke 107 | 5 % → 0 % | 47.3 px | 0.00 | 0.00 | 11 |
| stroke 108 | 3 % → 0 % | 30.1 px | 0.00 | 0.00 | 22 |
| stroke 109 | 5 % → 0 % | 96.9 px | 0.00 | 0.00 | 5 |
| stroke 110 | 6 % → 2 % | 32.3 px | 0.58 | 0.26 | 50 |
| stroke 111 | 5 % → 0 % | 27.4 px | 0.00 | 0.00 | 35 |
| stroke 112 | 9 % → 7 % | 53.3 px | 0.59 | 0.85 | 44 |
| stroke 113 | 13 % → 34 % | 19.9 px | 0.58 | 2.55 | 279 |
| stroke 114 | 5 % → 0 % | 42.2 px | 0.00 | 0.00 | 53 |
| stroke 115 | 8 % → 0 % | 57.7 px | 0.00 | 0.00 | 45 |
| stroke 116 | 12 % → 0 % | 76.6 px | 0.00 | 0.00 | 51 |
| stroke 117 | 16 % → 0 % | 175.5 px | 0.00 | 0.00 | 16 |
| stroke 118 | 15 % → 0 % | 171.2 px | 0.00 | 0.00 | 20 |
| stroke 119 | 17 % → 0 % | 73.5 px | 0.00 | 0.00 | 113 |
| stroke 120 | 19 % → 0 % | 80.0 px | 0.00 | 0.00 | 130 |
| stroke 121 | 25 % → 0 % | 128.0 px | 0.00 | 0.00 | 77 |
| stroke 122 | 26 % → 0 % | 449.8 px | 0.00 | 0.00 | 13 |
| stroke 123 | 24 % → 0 % | 97.4 px | 0.00 | 0.00 | 130 |
| stroke 124 | 28 % → 0 % | 108.4 px | 0.00 | 0.00 | 105 |
| stroke 125 | 31 % → 0 % | 111.6 px | 0.00 | 0.00 | 149 |
| stroke 126 | 32 % → 1 % | 119.3 px | 0.58 | 0.02 | 125 |
| stroke 127 | 30 % → 4 % | 124.2 px | 0.59 | 0.15 | 125 |
| stroke 128 | 25 % → 10 % | 133.8 px | 0.59 | 0.39 | 94 |
| stroke 129 | 7 % → 0 % | 26.7 px | 0.00 | 0.00 | 54 |
| stroke 130 | 7 % → 0 % | 55.1 px | 0.00 | 0.00 | 20 |
| stroke 131 | 3 % → 0 % | 24.6 px | 0.00 | 0.00 | 32 |
| stroke 132 | 4 % → 0 % | 28.6 px | 0.00 | 0.00 | 18 |
| stroke 133 | 22 % → 47 % | 95.0 px | 0.58 | 2.14 | 247 |
| stroke 134 | 34 % → 49 % | 129.2 px | 0.58 | 1.43 | 367 |
| stroke 135 | 51 % → 51 % | 146.7 px | 0.58 | 0.99 | 746 |

Numbers say: wet paint spreads well beyond the stroke.

## Refs v3 · #03 HW navy contours — own sheet
own sheet 800 × 600 · Gouache 1.00 + turpentine 30 % · 80 px · 36.3 s

![Refs v3 · #03 HW navy contours — own sheet](Refs-v3-03-HW-navy-contours-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 4 % → 0 % | 79.6 px | 0.00 | 0.00 | 86 |
| stroke 2 | 12 % → 0 % | 96.3 px | 0.00 | 0.00 | 239 |
| stroke 3 | 16 % → 0 % | 131.7 px | 0.00 | 0.00 | 231 |
| stroke 4 | 21 % → 0 % | 168.0 px | 0.00 | 0.00 | 239 |
| stroke 5 | 26 % → 0 % | 227.9 px | 0.00 | 0.00 | 198 |
| stroke 6 | 30 % → 0 % | 244.1 px | 0.37 | 0.00 | 358 |
| stroke 7 | 33 % → 0 % | 303.9 px | 0.38 | 0.01 | 325 |
| stroke 8 | 19 % → 0 % | 386.2 px | 0.00 | 0.00 | 58 |
| stroke 9 | 29 % → 0 % | 291.4 px | 0.00 | 0.00 | 114 |
| stroke 10 | 31 % → 0 % | 649.8 px | 0.00 | 0.00 | 56 |
| stroke 11 | 30 % → 2 % | 379.1 px | 0.38 | 0.07 | 93 |
| stroke 12 | 2 % → 0 % | 28.9 px | 0.00 | 0.00 | 9 |
| stroke 13 | 3 % → 0 % | 51.8 px | 0.00 | 0.00 | 7 |
| stroke 14 | 4 % → 0 % | 80.0 px | 0.00 | 0.00 | 4 |
| stroke 15 | 5 % → 0 % | 79.9 px | 0.00 | 0.00 | 6 |
| stroke 16 | 6 % → 0 % | 150.6 px | 0.00 | 0.00 | 6 |
| stroke 17 | 6 % → 0 % | 156.6 px | 0.00 | 0.00 | 21 |
| stroke 18 | 7 % → 0 % | 189.3 px | 0.00 | 0.00 | 4 |
| stroke 19 | 7 % → 0 % | 154.0 px | 0.00 | 0.00 | 8 |
| stroke 20 | 8 % → 0 % | 173.5 px | 0.00 | 0.00 | 16 |
| stroke 21 | 9 % → 0 % | 275.0 px | 0.00 | 0.00 | 8 |
| stroke 22 | 10 % → 0 % | 253.6 px | 0.00 | 0.00 | 12 |
| stroke 23 | 10 % → 0 % | 299.3 px | 0.00 | 0.00 | 11 |
| stroke 24 | 10 % → 0 % | 308.7 px | 0.00 | 0.00 | 7 |
| stroke 25 | 11 % → 0 % | 317.1 px | 0.00 | 0.00 | 14 |
| stroke 26 | 11 % → 0 % | 345.8 px | 0.00 | 0.00 | 6 |
| stroke 27 | 11 % → 0 % | 290.1 px | 0.00 | 0.00 | 9 |
| stroke 28 | 11 % → 0 % | 333.0 px | 0.00 | 0.00 | 7 |
| stroke 29 | 10 % → 0 % | 312.5 px | 0.00 | 0.00 | 4 |
| stroke 30 | 8 % → 0 % | 240.7 px | 0.00 | 0.00 | 11 |
| stroke 31 | 8 % → 0 % | 166.9 px | 0.00 | 0.00 | 17 |
| stroke 32 | 8 % → 0 % | 248.5 px | 0.00 | 0.00 | 4 |
| stroke 33 | 8 % → 0 % | 249.7 px | 0.00 | 0.00 | 8 |
| stroke 34 | 8 % → 0 % | 236.8 px | 0.00 | 0.00 | 14 |
| stroke 35 | 8 % → 0 % | 226.3 px | 0.00 | 0.00 | 5 |
| stroke 36 | 8 % → 0 % | 250.4 px | 0.00 | 0.00 | 10 |
| stroke 37 | 8 % → 0 % | 246.6 px | 0.00 | 0.00 | 6 |
| stroke 38 | 8 % → 0 % | 250.3 px | 0.00 | 0.00 | 6 |
| stroke 39 | 8 % → 0 % | 241.0 px | 0.00 | 0.00 | 8 |
| stroke 40 | 8 % → 0 % | 190.3 px | 0.00 | 0.00 | 10 |
| stroke 41 | 9 % → 0 % | 281.6 px | 0.00 | 0.00 | 7 |
| stroke 42 | 10 % → 0 % | 294.0 px | 0.00 | 0.00 | 14 |
| stroke 43 | 11 % → 0 % | 217.5 px | 0.00 | 0.00 | 13 |
| stroke 44 | 12 % → 0 % | 243.7 px | 0.00 | 0.00 | 11 |
| stroke 45 | 13 % → 0 % | 238.2 px | 0.00 | 0.00 | 14 |
| stroke 46 | 14 % → 0 % | 363.0 px | 0.00 | 0.00 | 9 |
| stroke 47 | 14 % → 0 % | 352.7 px | 0.00 | 0.00 | 5 |
| stroke 48 | 15 % → 0 % | 372.3 px | 0.00 | 0.00 | 9 |
| stroke 49 | 15 % → 0 % | 377.7 px | 0.00 | 0.00 | 8 |
| stroke 50 | 16 % → 0 % | 331.4 px | 0.00 | 0.00 | 8 |
| stroke 51 | 17 % → 0 % | 355.0 px | 0.00 | 0.00 | 3 |
| stroke 52 | 17 % → 0 % | 124.2 px | 0.00 | 0.00 | 26 |
| stroke 53 | 14 % → 0 % | 439.3 px | 0.00 | 0.00 | 12 |
| stroke 54 | 17 % → 1 % | 37.7 px | 0.38 | 0.09 | 620 |
| stroke 55 | 23 % → 2 % | 49.5 px | 0.38 | 0.07 | 385 |
| stroke 56 | 18 % → 4 % | 117.5 px | 0.38 | 0.20 | 49 |
| stroke 57 | 1 % → 0 % | 35.8 px | 0.00 | 0.00 | 15 |
| stroke 58 | 5 % → 0 % | 46.4 px | 0.00 | 0.00 | 94 |
| stroke 59 | 9 % → 0 % | 56.6 px | 0.00 | 0.00 | 179 |
| stroke 60 | 12 % → 0 % | 73.1 px | 0.00 | 0.00 | 360 |
| stroke 61 | 14 % → 0 % | 93.8 px | 0.00 | 0.00 | 231 |
| stroke 62 | 14 % → 0 % | 530.0 px | 0.00 | 0.00 | 39 |
| stroke 63 | 14 % → 0 % | 567.0 px | 0.00 | 0.00 | 24 |
| stroke 64 | 15 % → 0 % | 597.8 px | 0.00 | 0.00 | 17 |
| stroke 65 | 15 % → 0 % | 612.4 px | 0.00 | 0.00 | 27 |
| stroke 66 | 16 % → 0 % | 640.1 px | 0.00 | 0.00 | 19 |
| stroke 67 | 16 % → 0 % | 639.2 px | 0.00 | 0.00 | 21 |
| stroke 68 | 15 % → 0 % | 618.6 px | 0.00 | 0.00 | 17 |
| stroke 69 | 14 % → 0 % | 552.1 px | 0.00 | 0.00 | 15 |
| stroke 70 | 12 % → 0 % | 503.0 px | 0.00 | 0.00 | 20 |
| stroke 71 | 11 % → 0 % | 422.7 px | 0.00 | 0.00 | 30 |
| stroke 72 | 9 % → 0 % | 290.9 px | 0.00 | 0.00 | 29 |
| stroke 73 | 9 % → 0 % | 289.2 px | 0.00 | 0.00 | 23 |
| stroke 74 | 9 % → 0 % | 283.9 px | 0.00 | 0.00 | 32 |
| stroke 75 | 7 % → 0 % | 284.5 px | 0.00 | 0.00 | 17 |
| stroke 76 | 5 % → 0 % | 43.7 px | 0.00 | 0.00 | 128 |
| stroke 77 | 7 % → 0 % | 63.7 px | 0.00 | 0.00 | 161 |
| stroke 78 | 10 % → 0 % | 239.6 px | 0.00 | 0.00 | 55 |
| stroke 79 | 11 % → 0 % | 269.3 px | 0.00 | 0.00 | 40 |
| stroke 80 | 12 % → 0 % | 297.2 px | 0.00 | 0.00 | 56 |
| stroke 81 | 16 % → 0 % | 579.3 px | 0.00 | 0.00 | 32 |
| stroke 82 | 15 % → 0 % | 426.8 px | 0.00 | 0.00 | 37 |
| stroke 83 | 16 % → 0 % | 615.3 px | 0.00 | 0.00 | 81 |
| stroke 84 | 17 % → 0 % | 671.1 px | 0.00 | 0.00 | 47 |
| stroke 85 | 18 % → 0 % | 482.0 px | 0.00 | 0.00 | 51 |
| stroke 86 | 18 % → 0 % | 692.7 px | 0.00 | 0.00 | 45 |
| stroke 87 | 26 % → 0 % | 324.9 px | 0.00 | 0.00 | 147 |
| stroke 88 | 20 % → 0 % | 616.4 px | 0.38 | 0.02 | 23 |
| stroke 89 | 25 % → 0 % | 543.8 px | 0.38 | 0.02 | 58 |
| stroke 90 | 25 % → 0 % | 519.4 px | 0.38 | 0.02 | 22 |
| stroke 91 | 19 % → 1 % | 484.7 px | 0.38 | 0.06 | 25 |
| stroke 92 | 18 % → 2 % | 389.3 px | 0.38 | 0.10 | 44 |
| stroke 93 | 17 % → 2 % | 444.0 px | 0.38 | 0.11 | 27 |
| stroke 94 | 19 % → 3 % | 502.6 px | 0.38 | 0.15 | 11 |
| stroke 95 | 19 % → 2 % | 484.4 px | 0.38 | 0.10 | 24 |
| stroke 96 | 28 % → 2 % | 315.9 px | 0.38 | 0.08 | 47 |
| stroke 97 | 23 % → 2 % | 151.2 px | 0.38 | 0.07 | 114 |
| stroke 98 | 25 % → 2 % | 168.4 px | 0.38 | 0.07 | 139 |
| stroke 99 | 26 % → 2 % | 546.2 px | 0.38 | 0.07 | 34 |
| stroke 100 | 34 % → 2 % | 348.8 px | 0.38 | 0.07 | 59 |
| stroke 101 | 28 % → 2 % | 1130.3 px | 0.38 | 0.07 | 22 |
| stroke 102 | 36 % → 2 % | 435.5 px | 0.38 | 0.07 | 86 |
| stroke 103 | 36 % → 3 % | 733.9 px | 0.38 | 0.08 | 35 |
| stroke 104 | 36 % → 3 % | 879.3 px | 0.38 | 0.09 | 29 |
| stroke 105 | 37 % → 3 % | 348.6 px | 0.38 | 0.08 | 48 |
| stroke 106 | 41 % → 3 % | 502.8 px | 0.38 | 0.08 | 29 |
| stroke 107 | 36 % → 0 % | 1054.4 px | 0.00 | 0.00 | 21 |
| stroke 108 | 33 % → 0 % | 387.7 px | 0.00 | 0.00 | 72 |
| stroke 109 | 32 % → 0 % | 293.9 px | 0.00 | 0.00 | 102 |
| stroke 110 | 35 % → 0 % | 711.9 px | 0.00 | 0.00 | 45 |
| stroke 111 | 24 % → 0 % | 701.7 px | 0.00 | 0.00 | 11 |
| stroke 112 | 23 % → 0 % | 364.4 px | 0.00 | 0.00 | 36 |
| stroke 113 | 22 % → 0 % | 399.3 px | 0.00 | 0.00 | 29 |
| stroke 114 | 18 % → 0 % | 473.8 px | 0.00 | 0.00 | 12 |
| stroke 115 | 15 % → 0 % | 134.6 px | 0.00 | 0.00 | 45 |
| stroke 116 | 6 % → 0 % | 41.8 px | 0.00 | 0.00 | 98 |
| stroke 117 | 8 % → 0 % | 184.7 px | 0.00 | 0.00 | 17 |
| stroke 118 | 7 % → 0 % | 148.5 px | 0.00 | 0.00 | 36 |
| stroke 119 | 10 % → 0 % | 321.9 px | 0.00 | 0.00 | 12 |
| stroke 120 | 11 % → 0 % | 346.5 px | 0.00 | 0.00 | 10 |
| stroke 121 | 11 % → 0 % | 238.9 px | 0.00 | 0.00 | 24 |
| stroke 122 | 13 % → 0 % | 183.6 px | 0.00 | 0.00 | 48 |
| stroke 123 | 13 % → 0 % | 268.9 px | 0.00 | 0.00 | 28 |
| stroke 124 | 14 % → 0 % | 346.9 px | 0.00 | 0.00 | 28 |
| stroke 125 | 15 % → 0 % | 313.2 px | 0.00 | 0.00 | 32 |
| stroke 126 | 18 % → 0 % | 155.7 px | 0.00 | 0.00 | 106 |
| stroke 127 | 20 % → 0 % | 159.9 px | 0.00 | 0.00 | 108 |
| stroke 128 | 20 % → 0 % | 159.8 px | 0.00 | 0.00 | 90 |
| stroke 129 | 21 % → 0 % | 173.0 px | 0.00 | 0.00 | 79 |
| stroke 130 | 21 % → 0 % | 186.3 px | 0.00 | 0.00 | 89 |
| stroke 131 | 25 % → 0 % | 322.1 px | 0.00 | 0.00 | 48 |
| stroke 132 | 26 % → 0 % | 597.4 px | 0.00 | 0.00 | 29 |
| stroke 133 | 24 % → 0 % | 985.8 px | 0.00 | 0.00 | 12 |
| stroke 134 | 22 % → 0 % | 556.2 px | 0.00 | 0.00 | 24 |
| stroke 135 | 19 % → 0 % | 194.7 px | 0.00 | 0.00 | 83 |
| stroke 136 | 6 % → 1 % | 210.1 px | 0.38 | 0.15 | 17 |
| stroke 137 | 19 % → 1 % | 148.7 px | 0.38 | 0.04 | 166 |
| stroke 138 | 1 % → 0 % | 27.2 px | 0.00 | 0.00 | 10 |
| stroke 139 | 2 % → 0 % | 39.3 px | 0.00 | 0.00 | 34 |
| stroke 140 | 1 % → 0 % | 55.4 px | 0.00 | 0.00 | 9 |
| stroke 141 | 3 % → 0 % | 133.8 px | 0.00 | 0.00 | 10 |
| stroke 142 | 3 % → 0 % | 63.8 px | 0.00 | 0.00 | 9 |
| stroke 143 | 3 % → 0 % | 98.4 px | 0.00 | 0.00 | 18 |
| stroke 144 | 4 % → 0 % | 89.8 px | 0.38 | 0.01 | 33 |
| stroke 145 | 5 % → 2 % | 82.9 px | 0.38 | 0.42 | 21 |
| stroke 146 | 5 % → 2 % | 228.1 px | 0.38 | 0.36 | 7 |
| stroke 147 | 21 % → 0 % | 77.8 px | 0.00 | 0.00 | 405 |
| stroke 148 | 27 % → 0 % | 136.3 px | 0.00 | 0.00 | 321 |
| stroke 149 | 30 % → 0 % | 178.9 px | 0.00 | 0.00 | 383 |
| stroke 150 | 34 % → 0 % | 240.0 px | 0.00 | 0.00 | 410 |
| stroke 151 | 8 % → 0 % | 90.4 px | 0.00 | 0.00 | 161 |
| stroke 152 | 12 % → 0 % | 125.9 px | 0.00 | 0.00 | 293 |
| stroke 153 | 2 % → 3 % | 31.3 px | 0.38 | 1.40 | 32 |

## Refs v3 · #04 HW grey cloud — own sheet
own sheet 800 × 635 · Gouache 1.00 + turpentine 30 % · 93 px · 38.6 s

![Refs v3 · #04 HW grey cloud — own sheet](Refs-v3-04-HW-grey-cloud-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 13 % → 1 % | 66.0 px | 0.21 | 0.08 | 263 |
| stroke 2 | 17 % → 1 % | 103.0 px | 0.21 | 0.05 | 324 |
| stroke 3 | 23 % → 1 % | 157.5 px | 0.21 | 0.03 | 363 |
| stroke 4 | 28 % → 0 % | 303.3 px | 0.00 | 0.00 | 132 |
| stroke 5 | 16 % → 1 % | 305.8 px | 0.21 | 0.07 | 96 |
| stroke 6 | 31 % → 1 % | 208.3 px | 0.21 | 0.02 | 569 |
| stroke 7 | 37 % → 0 % | 334.0 px | 0.00 | 0.00 | 225 |
| stroke 8 | 38 % → 1 % | 207.3 px | 0.21 | 0.01 | 787 |
| stroke 9 | 32 % → 0 % | 511.3 px | 0.00 | 0.00 | 108 |
| stroke 10 | 42 % → 0 % | 239.6 px | 0.21 | 0.01 | 1150 |
| stroke 11 | 34 % → 0 % | 505.0 px | 0.00 | 0.00 | 146 |
| stroke 12 | 38 % → 0 % | 471.5 px | 0.00 | 0.00 | 134 |
| stroke 13 | 45 % → 0 % | 1119.4 px | 0.00 | 0.00 | 130 |
| stroke 14 | 44 % → 0 % | 431.1 px | 0.00 | 0.00 | 325 |
| stroke 15 | 49 % → 0 % | 887.1 px | 0.00 | 0.00 | 265 |
| stroke 16 | 42 % → 0 % | 394.1 px | 0.00 | 0.00 | 461 |
| stroke 17 | 46 % → 0 % | 653.2 px | 0.00 | 0.00 | 199 |
| stroke 18 | 1 % → 0 % | 26.1 px | 0.00 | 0.00 | 20 |
| stroke 19 | 2 % → 0 % | 46.8 px | 0.00 | 0.00 | 12 |
| stroke 20 | 4 % → 0 % | 60.6 px | 0.00 | 0.00 | 14 |
| stroke 21 | 3 % → 0 % | 80.4 px | 0.00 | 0.00 | 88 |
| stroke 22 | 7 % → 0 % | 107.4 px | 0.00 | 0.00 | 176 |
| stroke 23 | 8 % → 0 % | 161.6 px | 0.00 | 0.00 | 109 |
| stroke 24 | 11 % → 0 % | 128.5 px | 0.00 | 0.00 | 235 |
| stroke 25 | 13 % → 0 % | 171.8 px | 0.00 | 0.00 | 384 |
| stroke 26 | 18 % → 0 % | 134.8 px | 0.00 | 0.00 | 375 |
| stroke 27 | 20 % → 0 % | 285.8 px | 0.00 | 0.00 | 182 |
| stroke 28 | 28 % → 0 % | 664.7 px | 0.00 | 0.00 | 154 |
| stroke 29 | 22 % → 0 % | 244.3 px | 0.00 | 0.00 | 461 |
| stroke 30 | 22 % → 0 % | 177.9 px | 0.00 | 0.00 | 579 |
| stroke 31 | 28 % → 0 % | 416.7 px | 0.00 | 0.00 | 129 |
| stroke 32 | 33 % → 0 % | 543.0 px | 0.00 | 0.00 | 106 |
| stroke 33 | 33 % → 0 % | 627.7 px | 0.00 | 0.00 | 79 |
| stroke 34 | 32 % → 0 % | 196.7 px | 0.00 | 0.00 | 356 |
| stroke 35 | 33 % → 0 % | 193.7 px | 0.00 | 0.00 | 411 |
| stroke 36 | 37 % → 0 % | 203.4 px | 0.00 | 0.00 | 640 |
| stroke 37 | 21 % → 0 % | 295.9 px | 0.19 | 0.00 | 258 |
| stroke 38 | 14 % → 0 % | 360.5 px | 0.00 | 0.00 | 43 |
| stroke 39 | 17 % → 0 % | 303.8 px | 0.00 | 0.00 | 122 |
| stroke 40 | 15 % → 0 % | 275.5 px | 0.00 | 0.00 | 52 |
| stroke 41 | 21 % → 0 % | 355.4 px | 0.00 | 0.00 | 105 |
| stroke 42 | 24 % → 0 % | 269.2 px | 0.00 | 0.00 | 135 |
| stroke 43 | 1 % → 1 % | 31.9 px | 0.21 | 1.02 | 20 |
| stroke 44 | 1 % → 0 % | 26.4 px | 0.00 | 0.00 | 23 |
| stroke 45 | 10 % → 2 % | 47.5 px | 0.21 | 0.19 | 103 |
| stroke 46 | 11 % → 1 % | 113.8 px | 0.21 | 0.12 | 52 |
| stroke 47 | 19 % → 1 % | 71.6 px | 0.21 | 0.06 | 247 |
| stroke 48 | 23 % → 1 % | 100.3 px | 0.21 | 0.05 | 225 |
| stroke 49 | 35 % → 2 % | 485.2 px | 0.21 | 0.05 | 39 |
| stroke 50 | 35 % → 2 % | 449.7 px | 0.21 | 0.05 | 46 |
| stroke 51 | 34 % → 2 % | 641.7 px | 0.21 | 0.05 | 40 |
| stroke 52 | 11 % → 0 % | 47.9 px | 0.00 | 0.00 | 122 |
| stroke 53 | 11 % → 0 % | 241.5 px | 0.00 | 0.00 | 25 |
| stroke 54 | 18 % → 0 % | 127.1 px | 0.00 | 0.00 | 111 |
| stroke 55 | 16 % → 0 % | 296.2 px | 0.00 | 0.00 | 50 |
| stroke 56 | 24 % → 0 % | 241.7 px | 0.00 | 0.00 | 65 |
| stroke 57 | 26 % → 0 % | 307.9 px | 0.00 | 0.00 | 45 |
| stroke 58 | 27 % → 0 % | 406.5 px | 0.00 | 0.00 | 31 |
| stroke 59 | 7 % → 0 % | 76.2 px | 0.00 | 0.00 | 114 |
| stroke 60 | 9 % → 0 % | 91.2 px | 0.00 | 0.00 | 110 |
| stroke 61 | 12 % → 0 % | 118.4 px | 0.00 | 0.00 | 89 |
| stroke 62 | 18 % → 0 % | 346.7 px | 0.00 | 0.00 | 33 |
| stroke 63 | 7 % → 0 % | 60.2 px | 0.00 | 0.00 | 94 |
| stroke 64 | 11 % → 0 % | 251.2 px | 0.00 | 0.00 | 19 |
| stroke 65 | 11 % → 0 % | 88.1 px | 0.00 | 0.00 | 195 |
| stroke 66 | 14 % → 0 % | 101.9 px | 0.00 | 0.00 | 214 |
| stroke 67 | 19 % → 0 % | 134.0 px | 0.00 | 0.00 | 248 |
| stroke 68 | 31 % → 0 % | 515.4 px | 0.00 | 0.00 | 59 |
| stroke 69 | 23 % → 0 % | 266.7 px | 0.00 | 0.00 | 130 |
| stroke 70 | 45 % → 0 % | 557.9 px | 0.00 | 0.00 | 41 |
| stroke 71 | 16 % → 0 % | 212.4 px | 0.00 | 0.00 | 54 |
| stroke 72 | 20 % → 0 % | 352.3 px | 0.00 | 0.00 | 21 |
| stroke 73 | 15 % → 0 % | 94.4 px | 0.00 | 0.00 | 689 |
| stroke 74 | 26 % → 0 % | 121.1 px | 0.00 | 0.00 | 1439 |
| stroke 75 | 26 % → 0 % | 199.1 px | 0.00 | 0.00 | 268 |
| stroke 76 | 50 % → 0 % | 144.3 px | 0.00 | 0.00 | 1586 |
| stroke 77 | 73 % → 0 % | 182.9 px | 0.00 | 0.00 | 1476 |
| stroke 78 | 1 % → 2 % | 24.0 px | 0.21 | 1.36 | 55 |

## Refs v3 · #05 HW green in rust loops — own sheet
own sheet 800 × 1045 · Gouache 1.00 + turpentine 30 % · 104 px · 78.8 s

![Refs v3 · #05 HW green in rust loops — own sheet](Refs-v3-05-HW-green-in-rust-loops-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 11 % → 36 % | 94.0 px | 0.36 | 3.31 | 564 |
| stroke 2 | 20 % → 26 % | 113.5 px | 0.37 | 1.30 | 973 |
| stroke 3 | 28 % → 21 % | 151.6 px | 0.36 | 0.77 | 1572 |
| stroke 4 | 36 % → 16 % | 191.3 px | 0.37 | 0.45 | 1959 |
| stroke 5 | 44 % → 11 % | 233.0 px | 0.38 | 0.25 | 1350 |
| stroke 6 | 49 % → 5 % | 265.5 px | 0.39 | 0.10 | 1372 |
| stroke 7 | 50 % → 0 % | 275.8 px | 0.34 | 0.00 | 2056 |
| stroke 8 | 51 % → 0 % | 269.5 px | 0.00 | 0.00 | 990 |
| stroke 9 | 50 % → 0 % | 302.1 px | 0.00 | 0.00 | 1150 |
| stroke 10 | 54 % → 0 % | 869.4 px | 0.00 | 0.00 | 223 |
| stroke 11 | 52 % → 0 % | 778.4 px | 0.00 | 0.00 | 270 |
| stroke 12 | 3 % → 41 % | 66.2 px | 0.36 | 15.29 | 54 |
| stroke 13 | 5 % → 46 % | 86.9 px | 0.36 | 9.98 | 61 |
| stroke 14 | 7 % → 43 % | 202.3 px | 0.37 | 6.67 | 29 |
| stroke 15 | 2 % → 76 % | 65.5 px | 0.37 | 43.74 | 35 |
| stroke 16 | 2 % → 72 % | 97.1 px | 0.37 | 28.87 | 34 |
| stroke 17 | 10 % → 56 % | 255.3 px | 0.37 | 5.77 | 46 |
| stroke 18 | 11 % → 55 % | 197.2 px | 0.37 | 4.90 | 77 |
| stroke 19 | 13 % → 52 % | 190.6 px | 0.37 | 3.96 | 94 |
| stroke 20 | 16 % → 51 % | 180.4 px | 0.37 | 3.19 | 149 |
| stroke 21 | 19 % → 46 % | 240.1 px | 0.37 | 2.49 | 113 |
| stroke 22 | 21 % → 43 % | 245.4 px | 0.37 | 1.99 | 132 |
| stroke 23 | 23 % → 38 % | 288.5 px | 0.37 | 1.66 | 133 |
| stroke 24 | 24 % → 32 % | 571.3 px | 0.37 | 1.32 | 67 |
| stroke 25 | 1 % → 0 % | 59.2 px | 0.00 | 0.00 | 33 |
| stroke 26 | 1 % → 0 % | 28.3 px | 0.00 | 0.00 | 14 |
| stroke 27 | 2 % → 0 % | 55.1 px | 0.00 | 0.00 | 12 |
| stroke 28 | 4 % → 0 % | 41.2 px | 0.00 | 0.00 | 41 |
| stroke 29 | 1 % → 0 % | 22.7 px | 0.00 | 0.00 | 7 |
| stroke 30 | 3 % → 0 % | 129.0 px | 0.00 | 0.00 | 13 |
| stroke 31 | 3 % → 0 % | 126.2 px | 0.00 | 0.00 | 4 |
| stroke 32 | 3 % → 52 % | 51.2 px | 0.37 | 17.97 | 18 |
| stroke 33 | 3 % → 48 % | 118.6 px | 0.36 | 15.51 | 11 |
| stroke 34 | 4 % → 47 % | 128.7 px | 0.36 | 11.33 | 19 |
| stroke 35 | 5 % → 48 % | 131.2 px | 0.36 | 9.60 | 27 |
| stroke 36 | 5 % → 46 % | 165.5 px | 0.36 | 8.57 | 19 |
| stroke 37 | 6 % → 43 % | 176.1 px | 0.36 | 7.78 | 16 |
| stroke 38 | 6 % → 41 % | 196.9 px | 0.36 | 6.75 | 20 |
| stroke 39 | 7 % → 38 % | 296.8 px | 0.36 | 5.33 | 13 |
| stroke 40 | 8 % → 36 % | 333.0 px | 0.36 | 4.51 | 10 |
| stroke 41 | 9 % → 34 % | 359.1 px | 0.36 | 3.89 | 12 |
| stroke 42 | 10 % → 32 % | 392.0 px | 0.36 | 3.32 | 11 |
| stroke 43 | 11 % → 30 % | 435.8 px | 0.36 | 2.87 | 10 |
| stroke 44 | 11 % → 28 % | 471.9 px | 0.36 | 2.47 | 10 |
| stroke 45 | 10 % → 20 % | 417.8 px | 0.35 | 1.91 | 10 |
| stroke 46 | 2 % → 19 % | 44.6 px | 0.38 | 8.65 | 25 |
| stroke 47 | 4 % → 19 % | 70.1 px | 0.38 | 5.01 | 64 |
| stroke 48 | 5 % → 18 % | 106.5 px | 0.38 | 3.42 | 48 |
| stroke 49 | 6 % → 16 % | 148.3 px | 0.38 | 2.64 | 27 |
| stroke 50 | 7 % → 16 % | 218.0 px | 0.38 | 2.09 | 15 |
| stroke 51 | 8 % → 15 % | 328.8 px | 0.38 | 1.77 | 17 |
| stroke 52 | 2 % → 0 % | 46.8 px | 0.00 | 0.00 | 24 |
| stroke 53 | 4 % → 0 % | 59.4 px | 0.00 | 0.00 | 147 |
| stroke 54 | 5 % → 0 % | 91.4 px | 0.00 | 0.00 | 64 |
| stroke 55 | 7 % → 0 % | 123.1 px | 0.00 | 0.00 | 80 |
| stroke 56 | 8 % → 0 % | 171.4 px | 0.00 | 0.00 | 36 |
| stroke 57 | 10 % → 0 % | 359.7 px | 0.00 | 0.00 | 24 |
| stroke 58 | 2 % → 0 % | 46.5 px | 0.00 | 0.00 | 47 |
| stroke 59 | 3 % → 0 % | 75.7 px | 0.00 | 0.00 | 29 |
| stroke 60 | 4 % → 0 % | 101.2 px | 0.00 | 0.00 | 33 |
| stroke 61 | 5 % → 0 % | 108.3 px | 0.00 | 0.00 | 34 |
| stroke 62 | 6 % → 0 % | 112.1 px | 0.00 | 0.00 | 48 |
| stroke 63 | 8 % → 0 % | 152.5 px | 0.00 | 0.00 | 134 |
| stroke 64 | 9 % → 0 % | 238.5 px | 0.00 | 0.00 | 35 |
| stroke 65 | 11 % → 0 % | 303.3 px | 0.00 | 0.00 | 16 |
| stroke 66 | 12 % → 0 % | 348.9 px | 0.00 | 0.00 | 24 |
| stroke 67 | 14 % → 0 % | 356.2 px | 0.00 | 0.00 | 33 |
| stroke 68 | 16 % → 0 % | 539.9 px | 0.00 | 0.00 | 19 |
| stroke 69 | 17 % → 0 % | 532.5 px | 0.00 | 0.00 | 22 |
| stroke 70 | 19 % → 0 % | 591.0 px | 0.00 | 0.00 | 16 |
| stroke 71 | 19 % → 0 % | 551.6 px | 0.00 | 0.00 | 19 |
| stroke 72 | 2 % → 34 % | 26.1 px | 0.36 | 19.63 | 25 |
| stroke 73 | 1 % → 67 % | 23.5 px | 0.36 | 83.45 | 12 |
| stroke 74 | 1 % → 0 % | 24.9 px | 0.00 | 0.00 | 12 |
| stroke 75 | 1 % → 17 % | 31.1 px | 0.38 | 28.75 | 40 |
| stroke 76 | 1 % → 16 % | 58.8 px | 0.38 | 17.10 | 8 |
| stroke 77 | 1 % → 16 % | 87.1 px | 0.38 | 10.41 | 3 |
| stroke 78 | 2 % → 16 % | 92.4 px | 0.38 | 7.11 | 13 |
| stroke 79 | 3 % → 15 % | 88.2 px | 0.38 | 5.31 | 20 |
| stroke 80 | 3 % → 15 % | 107.6 px | 0.38 | 4.38 | 21 |
| stroke 81 | 4 % → 14 % | 125.9 px | 0.39 | 3.34 | 26 |
| stroke 82 | 5 % → 11 % | 138.2 px | 0.40 | 2.51 | 15 |
| stroke 83 | 5 % → 9 % | 214.8 px | 0.39 | 1.84 | 26 |
| stroke 84 | 5 % → 7 % | 172.8 px | 0.39 | 1.34 | 34 |
| stroke 85 | 6 % → 5 % | 191.6 px | 0.39 | 0.79 | 9 |
| stroke 86 | 7 % → 3 % | 213.9 px | 0.40 | 0.37 | 12 |
| stroke 87 | 7 % → 0 % | 315.2 px | 0.34 | 0.03 | 14 |
| stroke 88 | 8 % → 0 % | 312.4 px | 0.00 | 0.00 | 18 |
| stroke 89 | 8 % → 0 % | 360.2 px | 0.00 | 0.00 | 18 |
| stroke 90 | 9 % → 0 % | 275.2 px | 0.00 | 0.00 | 15 |
| stroke 91 | 10 % → 0 % | 386.7 px | 0.00 | 0.00 | 12 |
| stroke 92 | 10 % → 0 % | 419.4 px | 0.00 | 0.00 | 8 |
| stroke 93 | 10 % → 0 % | 327.6 px | 0.00 | 0.00 | 17 |
| stroke 94 | 11 % → 0 % | 344.2 px | 0.00 | 0.00 | 52 |
| stroke 95 | 11 % → 0 % | 455.4 px | 0.00 | 0.00 | 24 |
| stroke 96 | 11 % → 0 % | 632.0 px | 0.00 | 0.00 | 22 |
| stroke 97 | 10 % → 0 % | 696.7 px | 0.00 | 0.00 | 10 |
| stroke 98 | 10 % → 0 % | 211.7 px | 0.00 | 0.00 | 106 |
| stroke 99 | 9 % → 0 % | 104.9 px | 0.00 | 0.00 | 191 |
| stroke 100 | 6 % → 0 % | 259.4 px | 0.00 | 0.00 | 46 |
| stroke 101 | 5 % → 0 % | 243.2 px | 0.00 | 0.00 | 15 |
| stroke 102 | 4 % → 0 % | 194.4 px | 0.00 | 0.00 | 20 |
| stroke 103 | 5 % → 0 % | 184.9 px | 0.00 | 0.00 | 21 |
| stroke 104 | 6 % → 0 % | 275.6 px | 0.00 | 0.00 | 22 |
| stroke 105 | 6 % → 0 % | 387.9 px | 0.00 | 0.00 | 8 |
| stroke 106 | 6 % → 0 % | 590.5 px | 0.00 | 0.00 | 4 |
| stroke 107 | 6 % → 0 % | 630.9 px | 0.00 | 0.00 | 8 |
| stroke 108 | 1 % → 42 % | 22.7 px | 0.36 | 33.03 | 16 |
| stroke 109 | 3 % → 0 % | 27.3 px | 0.00 | 0.00 | 152 |
| stroke 110 | 4 % → 0 % | 153.9 px | 0.00 | 0.00 | 25 |
| stroke 111 | 8 % → 0 % | 97.7 px | 0.00 | 0.00 | 366 |
| stroke 112 | 13 % → 0 % | 129.0 px | 0.00 | 0.00 | 571 |
| stroke 113 | 15 % → 0 % | 203.9 px | 0.00 | 0.00 | 713 |
| stroke 114 | 25 % → 0 % | 212.2 px | 0.00 | 0.00 | 699 |
| stroke 115 | 23 % → 0 % | 228.2 px | 0.00 | 0.00 | 521 |
| stroke 116 | 33 % → 0 % | 424.7 px | 0.00 | 0.00 | 246 |
| stroke 117 | 34 % → 0 % | 245.7 px | 0.00 | 0.00 | 737 |
| stroke 118 | 47 % → 0 % | 419.6 px | 0.00 | 0.00 | 607 |
| stroke 119 | 47 % → 0 % | 297.0 px | 0.00 | 0.00 | 660 |
| stroke 120 | 60 % → 0 % | 240.0 px | 0.00 | 0.00 | 1223 |
| stroke 121 | 1 % → 59 % | 17.1 px | 0.36 | 90.71 | 11 |
| stroke 122 | 9 % → 53 % | 76.4 px | 0.36 | 5.69 | 212 |
| stroke 123 | 17 % → 61 % | 103.9 px | 0.36 | 3.55 | 285 |
| stroke 124 | 21 % → 48 % | 149.9 px | 0.36 | 2.32 | 228 |
| stroke 125 | 24 % → 73 % | 377.5 px | 0.36 | 2.97 | 111 |
| stroke 126 | 19 % → 67 % | 192.9 px | 0.36 | 3.47 | 165 |
| stroke 127 | 23 % → 51 % | 597.7 px | 0.36 | 2.20 | 81 |
| stroke 128 | 31 % → 71 % | 445.1 px | 0.36 | 2.31 | 212 |
| stroke 129 | 24 % → 68 % | 282.7 px | 0.36 | 2.80 | 420 |
| stroke 130 | 33 % → 69 % | 451.6 px | 0.36 | 2.09 | 194 |
| stroke 131 | 27 % → 67 % | 710.2 px | 0.36 | 2.52 | 99 |
| stroke 132 | 34 % → 70 % | 556.7 px | 0.37 | 2.08 | 186 |
| stroke 133 | 30 % → 65 % | 484.9 px | 0.36 | 2.15 | 144 |
| stroke 134 | 37 % → 67 % | 807.5 px | 0.37 | 1.80 | 146 |
| stroke 135 | 32 % → 60 % | 554.0 px | 0.36 | 1.89 | 199 |
| stroke 136 | 31 % → 53 % | 789.3 px | 0.36 | 1.74 | 218 |
| stroke 137 | 39 % → 65 % | 876.4 px | 0.37 | 1.64 | 133 |
| stroke 138 | 37 % → 58 % | 637.4 px | 0.36 | 1.56 | 141 |
| stroke 139 | 36 % → 53 % | 973.9 px | 0.36 | 1.46 | 51 |
| stroke 140 | 36 % → 50 % | 266.6 px | 0.37 | 1.38 | 559 |
| stroke 141 | 35 % → 44 % | 263.9 px | 0.37 | 1.26 | 520 |
| stroke 142 | 34 % → 40 % | 330.9 px | 0.37 | 1.17 | 669 |
| stroke 143 | 36 % → 36 % | 271.2 px | 0.37 | 0.99 | 745 |

Numbers say: wet paint spreads well beyond the stroke.

## Refs v3 · #06 HW scrubbed grey — own sheet
own sheet 800 × 635 · Gouache 1.00 + turpentine 30 % · 93 px · 40.9 s

![Refs v3 · #06 HW scrubbed grey — own sheet](Refs-v3-06-HW-scrubbed-grey-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 13 % → 1 % | 66.0 px | 0.21 | 0.08 | 370 |
| stroke 2 | 17 % → 1 % | 103.0 px | 0.21 | 0.05 | 418 |
| stroke 3 | 23 % → 1 % | 157.4 px | 0.21 | 0.03 | 826 |
| stroke 4 | 28 % → 0 % | 302.3 px | 0.00 | 0.00 | 234 |
| stroke 5 | 16 % → 1 % | 305.9 px | 0.21 | 0.07 | 76 |
| stroke 6 | 31 % → 1 % | 208.3 px | 0.21 | 0.02 | 746 |
| stroke 7 | 37 % → 0 % | 334.0 px | 0.00 | 0.00 | 423 |
| stroke 8 | 38 % → 1 % | 206.8 px | 0.21 | 0.01 | 889 |
| stroke 9 | 32 % → 0 % | 510.6 px | 0.00 | 0.00 | 117 |
| stroke 10 | 42 % → 0 % | 239.4 px | 0.21 | 0.01 | 965 |
| stroke 11 | 34 % → 0 % | 504.5 px | 0.00 | 0.00 | 106 |
| stroke 12 | 38 % → 0 % | 470.8 px | 0.00 | 0.00 | 206 |
| stroke 13 | 45 % → 0 % | 1119.0 px | 0.00 | 0.00 | 117 |
| stroke 14 | 44 % → 0 % | 430.6 px | 0.00 | 0.00 | 238 |
| stroke 15 | 49 % → 0 % | 886.4 px | 0.00 | 0.00 | 253 |
| stroke 16 | 42 % → 0 % | 393.8 px | 0.00 | 0.00 | 562 |
| stroke 17 | 46 % → 0 % | 652.6 px | 0.00 | 0.00 | 187 |
| stroke 18 | 1 % → 0 % | 26.1 px | 0.00 | 0.00 | 12 |
| stroke 19 | 2 % → 0 % | 46.8 px | 0.00 | 0.00 | 13 |
| stroke 20 | 4 % → 0 % | 60.5 px | 0.00 | 0.00 | 12 |
| stroke 21 | 3 % → 0 % | 80.9 px | 0.00 | 0.00 | 43 |
| stroke 22 | 7 % → 0 % | 107.6 px | 0.00 | 0.00 | 101 |
| stroke 23 | 8 % → 0 % | 161.8 px | 0.00 | 0.00 | 88 |
| stroke 24 | 11 % → 0 % | 128.4 px | 0.00 | 0.00 | 146 |
| stroke 25 | 13 % → 0 % | 172.2 px | 0.00 | 0.00 | 168 |
| stroke 26 | 18 % → 0 % | 134.8 px | 0.00 | 0.00 | 369 |
| stroke 27 | 20 % → 0 % | 285.6 px | 0.00 | 0.00 | 236 |
| stroke 28 | 28 % → 0 % | 663.6 px | 0.00 | 0.00 | 124 |
| stroke 29 | 22 % → 0 % | 244.1 px | 0.00 | 0.00 | 188 |
| stroke 30 | 22 % → 0 % | 177.8 px | 0.00 | 0.00 | 441 |
| stroke 31 | 28 % → 0 % | 416.1 px | 0.00 | 0.00 | 155 |
| stroke 32 | 33 % → 0 % | 542.9 px | 0.00 | 0.00 | 225 |
| stroke 33 | 33 % → 0 % | 628.2 px | 0.00 | 0.00 | 84 |
| stroke 34 | 32 % → 0 % | 196.4 px | 0.00 | 0.00 | 406 |
| stroke 35 | 33 % → 0 % | 193.5 px | 0.00 | 0.00 | 388 |
| stroke 36 | 37 % → 0 % | 203.4 px | 0.00 | 0.00 | 359 |
| stroke 37 | 21 % → 0 % | 295.5 px | 0.19 | 0.00 | 127 |
| stroke 38 | 14 % → 0 % | 359.6 px | 0.00 | 0.00 | 56 |
| stroke 39 | 17 % → 0 % | 304.1 px | 0.00 | 0.00 | 122 |
| stroke 40 | 15 % → 0 % | 277.6 px | 0.00 | 0.00 | 41 |
| stroke 41 | 21 % → 0 % | 356.0 px | 0.00 | 0.00 | 71 |
| stroke 42 | 24 % → 0 % | 270.2 px | 0.00 | 0.00 | 144 |
| stroke 43 | 1 % → 1 % | 33.3 px | 0.21 | 0.98 | 13 |
| stroke 44 | 1 % → 0 % | 26.0 px | 0.00 | 0.00 | 24 |
| stroke 45 | 10 % → 2 % | 47.8 px | 0.21 | 0.19 | 92 |
| stroke 46 | 11 % → 1 % | 113.9 px | 0.21 | 0.12 | 55 |
| stroke 47 | 19 % → 1 % | 71.7 px | 0.21 | 0.06 | 256 |
| stroke 48 | 23 % → 1 % | 100.5 px | 0.21 | 0.05 | 238 |
| stroke 49 | 35 % → 2 % | 486.0 px | 0.21 | 0.05 | 46 |
| stroke 50 | 35 % → 2 % | 450.3 px | 0.21 | 0.05 | 43 |
| stroke 51 | 34 % → 2 % | 642.6 px | 0.21 | 0.05 | 38 |
| stroke 52 | 11 % → 0 % | 48.0 px | 0.00 | 0.00 | 132 |
| stroke 53 | 11 % → 0 % | 241.7 px | 0.00 | 0.00 | 18 |
| stroke 54 | 18 % → 0 % | 127.1 px | 0.00 | 0.00 | 86 |
| stroke 55 | 16 % → 0 % | 296.5 px | 0.00 | 0.00 | 42 |
| stroke 56 | 24 % → 0 % | 242.3 px | 0.00 | 0.00 | 59 |
| stroke 57 | 26 % → 0 % | 307.9 px | 0.00 | 0.00 | 76 |
| stroke 58 | 27 % → 0 % | 406.7 px | 0.00 | 0.00 | 48 |
| stroke 59 | 7 % → 0 % | 76.5 px | 0.00 | 0.00 | 91 |
| stroke 60 | 9 % → 0 % | 91.1 px | 0.00 | 0.00 | 124 |
| stroke 61 | 12 % → 0 % | 118.5 px | 0.00 | 0.00 | 199 |
| stroke 62 | 18 % → 0 % | 347.1 px | 0.00 | 0.00 | 108 |
| stroke 63 | 7 % → 0 % | 60.6 px | 0.00 | 0.00 | 122 |
| stroke 64 | 11 % → 0 % | 253.3 px | 0.00 | 0.00 | 43 |
| stroke 65 | 11 % → 0 % | 88.7 px | 0.00 | 0.00 | 286 |
| stroke 66 | 14 % → 0 % | 102.2 px | 0.00 | 0.00 | 378 |
| stroke 67 | 19 % → 0 % | 134.0 px | 0.00 | 0.00 | 307 |
| stroke 68 | 31 % → 0 % | 515.9 px | 0.00 | 0.00 | 60 |
| stroke 69 | 23 % → 0 % | 267.0 px | 0.00 | 0.00 | 331 |
| stroke 70 | 46 % → 0 % | 559.1 px | 0.00 | 0.00 | 58 |
| stroke 71 | 16 % → 0 % | 213.0 px | 0.00 | 0.00 | 72 |
| stroke 72 | 20 % → 0 % | 354.2 px | 0.00 | 0.00 | 29 |
| stroke 73 | 15 % → 0 % | 94.6 px | 0.00 | 0.00 | 647 |
| stroke 74 | 26 % → 0 % | 120.5 px | 0.00 | 0.00 | 1771 |
| stroke 75 | 26 % → 0 % | 198.8 px | 0.00 | 0.00 | 340 |
| stroke 76 | 50 % → 0 % | 144.6 px | 0.00 | 0.00 | 1484 |
| stroke 77 | 73 % → 0 % | 182.9 px | 0.00 | 0.00 | 1413 |
| stroke 78 | 1 % → 2 % | 23.9 px | 0.21 | 1.37 | 27 |

## Refs v3 · #07 HW blue L and zigzag — own sheet
own sheet 800 × 1065 · Gouache 1.00 + turpentine 30 % · 104 px · 54.2 s

![Refs v3 · #07 HW blue L and zigzag — own sheet](Refs-v3-07-HW-blue-L-and-zigzag-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 5 % → 1 % | 103.4 px | 0.39 | 0.27 | 93 |
| stroke 2 | 9 % → 1 % | 192.7 px | 0.39 | 0.13 | 101 |
| stroke 3 | 10 % → 0 % | 93.7 px | 0.00 | 0.00 | 240 |
| stroke 4 | 13 % → 1 % | 161.2 px | 0.39 | 0.06 | 426 |
| stroke 5 | 15 % → 3 % | 141.6 px | 0.38 | 0.17 | 254 |
| stroke 6 | 31 % → 1 % | 170.4 px | 0.38 | 0.05 | 750 |
| stroke 7 | 31 % → 4 % | 427.5 px | 0.38 | 0.13 | 113 |
| stroke 8 | 45 % → 0 % | 442.8 px | 0.00 | 0.00 | 166 |
| stroke 9 | 43 % → 2 % | 294.1 px | 0.38 | 0.04 | 544 |
| stroke 10 | 60 % → 0 % | 726.6 px | 0.00 | 0.00 | 110 |
| stroke 11 | 57 % → 2 % | 337.1 px | 0.38 | 0.03 | 640 |
| stroke 12 | 76 % → 2 % | 261.6 px | 0.38 | 0.03 | 1790 |
| stroke 13 | 84 % → 3 % | 315.5 px | 0.38 | 0.03 | 817 |
| stroke 14 | 1 % → 2 % | 20.9 px | 0.39 | 3.32 | 20 |
| stroke 15 | 5 % → 0 % | 84.7 px | 0.00 | 0.00 | 199 |
| stroke 16 | 11 % → 0 % | 117.7 px | 0.00 | 0.00 | 296 |
| stroke 17 | 15 % → 0 % | 155.4 px | 0.00 | 0.00 | 233 |
| stroke 18 | 20 % → 0 % | 214.5 px | 0.00 | 0.00 | 277 |
| stroke 19 | 23 % → 0 % | 243.0 px | 0.39 | 0.01 | 523 |
| stroke 20 | 27 % → 1 % | 297.3 px | 0.39 | 0.05 | 558 |
| stroke 21 | 28 % → 1 % | 320.3 px | 0.39 | 0.05 | 232 |
| stroke 22 | 29 % → 2 % | 391.5 px | 0.39 | 0.06 | 243 |
| stroke 23 | 3 % → 2 % | 69.0 px | 0.39 | 0.66 | 38 |
| stroke 24 | 6 % → 2 % | 83.2 px | 0.39 | 0.29 | 80 |
| stroke 25 | 8 % → 1 % | 82.2 px | 0.39 | 0.17 | 305 |
| stroke 26 | 11 % → 1 % | 113.2 px | 0.39 | 0.12 | 161 |
| stroke 27 | 3 % → 0 % | 70.2 px | 0.40 | 0.01 | 67 |
| stroke 28 | 6 % → 1 % | 74.2 px | 0.39 | 0.21 | 245 |
| stroke 29 | 8 % → 2 % | 102.4 px | 0.38 | 0.24 | 235 |
| stroke 30 | 1 % → 0 % | 45.0 px | 0.00 | 0.00 | 13 |
| stroke 31 | 1 % → 0 % | 56.4 px | 0.00 | 0.00 | 29 |
| stroke 32 | 2 % → 0 % | 90.2 px | 0.00 | 0.00 | 41 |
| stroke 33 | 3 % → 0 % | 114.6 px | 0.00 | 0.00 | 27 |
| stroke 34 | 3 % → 0 % | 192.1 px | 0.00 | 0.00 | 15 |
| stroke 35 | 4 % → 0 % | 242.1 px | 0.00 | 0.00 | 11 |
| stroke 36 | 4 % → 0 % | 197.4 px | 0.00 | 0.00 | 86 |
| stroke 37 | 5 % → 0 % | 232.7 px | 0.00 | 0.00 | 44 |
| stroke 38 | 6 % → 0 % | 251.9 px | 0.00 | 0.00 | 41 |
| stroke 39 | 6 % → 0 % | 233.8 px | 0.00 | 0.00 | 22 |
| stroke 40 | 7 % → 0 % | 261.5 px | 0.00 | 0.00 | 28 |
| stroke 41 | 8 % → 0 % | 235.4 px | 0.00 | 0.00 | 32 |
| stroke 42 | 8 % → 0 % | 247.7 px | 0.00 | 0.00 | 29 |
| stroke 43 | 8 % → 0 % | 259.8 px | 0.00 | 0.00 | 31 |
| stroke 44 | 8 % → 0 % | 255.2 px | 0.00 | 0.00 | 34 |
| stroke 45 | 9 % → 0 % | 185.1 px | 0.00 | 0.00 | 63 |
| stroke 46 | 10 % → 0 % | 219.3 px | 0.00 | 0.00 | 64 |
| stroke 47 | 5 % → 0 % | 61.9 px | 0.00 | 0.00 | 244 |
| stroke 48 | 5 % → 0 % | 191.1 px | 0.00 | 0.00 | 59 |
| stroke 49 | 8 % → 0 % | 221.7 px | 0.00 | 0.00 | 36 |
| stroke 50 | 7 % → 0 % | 330.3 px | 0.00 | 0.00 | 45 |
| stroke 51 | 11 % → 0 % | 228.0 px | 0.00 | 0.00 | 67 |
| stroke 52 | 13 % → 0 % | 230.8 px | 0.00 | 0.00 | 103 |
| stroke 53 | 15 % → 0 % | 222.1 px | 0.00 | 0.00 | 131 |
| stroke 54 | 16 % → 0 % | 182.9 px | 0.00 | 0.00 | 452 |
| stroke 55 | 19 % → 0 % | 226.4 px | 0.00 | 0.00 | 168 |
| stroke 56 | 22 % → 0 % | 274.0 px | 0.00 | 0.00 | 149 |
| stroke 57 | 24 % → 0 % | 296.3 px | 0.00 | 0.00 | 164 |
| stroke 58 | 25 % → 0 % | 353.5 px | 0.00 | 0.00 | 105 |
| stroke 59 | 25 % → 0 % | 319.2 px | 0.00 | 0.00 | 142 |
| stroke 60 | 24 % → 0 % | 306.5 px | 0.00 | 0.00 | 109 |
| stroke 61 | 25 % → 0 % | 287.9 px | 0.00 | 0.00 | 131 |
| stroke 62 | 19 % → 0 % | 645.5 px | 0.00 | 0.00 | 67 |
| stroke 63 | 20 % → 0 % | 244.9 px | 0.00 | 0.00 | 489 |
| stroke 64 | 21 % → 0 % | 237.9 px | 0.00 | 0.00 | 204 |
| stroke 65 | 3 % → 0 % | 132.0 px | 0.00 | 0.00 | 29 |
| stroke 66 | 5 % → 0 % | 165.9 px | 0.00 | 0.00 | 36 |
| stroke 67 | 7 % → 0 % | 194.0 px | 0.00 | 0.00 | 54 |
| stroke 68 | 8 % → 0 % | 222.7 px | 0.00 | 0.00 | 49 |
| stroke 69 | 11 % → 0 % | 428.1 px | 0.00 | 0.00 | 41 |
| stroke 70 | 13 % → 0 % | 504.0 px | 0.00 | 0.00 | 29 |
| stroke 71 | 13 % → 0 % | 528.1 px | 0.00 | 0.00 | 33 |
| stroke 72 | 16 % → 0 % | 434.7 px | 0.00 | 0.00 | 57 |
| stroke 73 | 16 % → 0 % | 539.4 px | 0.00 | 0.00 | 78 |
| stroke 74 | 17 % → 0 % | 406.2 px | 0.00 | 0.00 | 88 |
| stroke 75 | 16 % → 0 % | 365.6 px | 0.00 | 0.00 | 100 |
| stroke 76 | 16 % → 0 % | 741.6 px | 0.00 | 0.00 | 31 |
| stroke 77 | 16 % → 0 % | 435.9 px | 0.00 | 0.00 | 78 |
| stroke 78 | 16 % → 0 % | 755.6 px | 0.00 | 0.00 | 32 |
| stroke 79 | 2 % → 0 % | 56.3 px | 0.00 | 0.00 | 41 |
| stroke 80 | 4 % → 0 % | 76.0 px | 0.00 | 0.00 | 46 |
| stroke 81 | 5 % → 0 % | 116.7 px | 0.00 | 0.00 | 52 |
| stroke 82 | 6 % → 0 % | 146.3 px | 0.00 | 0.00 | 58 |
| stroke 83 | 7 % → 0 % | 175.6 px | 0.00 | 0.00 | 81 |
| stroke 84 | 8 % → 0 % | 204.1 px | 0.00 | 0.00 | 99 |
| stroke 85 | 9 % → 0 % | 237.2 px | 0.00 | 0.00 | 115 |
| stroke 86 | 11 % → 0 % | 269.0 px | 0.00 | 0.00 | 79 |
| stroke 87 | 11 % → 0 % | 404.6 px | 0.00 | 0.00 | 42 |
| stroke 88 | 12 % → 0 % | 424.9 px | 0.00 | 0.00 | 48 |
| stroke 89 | 12 % → 0 % | 451.5 px | 0.00 | 0.00 | 37 |
| stroke 90 | 12 % → 0 % | 548.1 px | 0.00 | 0.00 | 28 |
| stroke 91 | 7 % → 1 % | 318.9 px | 0.39 | 0.17 | 14 |
| stroke 92 | 7 % → 1 % | 309.9 px | 0.39 | 0.18 | 24 |
| stroke 93 | 7 % → 1 % | 259.1 px | 0.39 | 0.18 | 23 |
| stroke 94 | 7 % → 1 % | 181.5 px | 0.39 | 0.17 | 65 |
| stroke 95 | 8 % → 1 % | 190.3 px | 0.39 | 0.16 | 82 |
| stroke 96 | 8 % → 1 % | 224.8 px | 0.39 | 0.16 | 53 |
| stroke 97 | 8 % → 1 % | 341.4 px | 0.39 | 0.16 | 44 |
| stroke 98 | 9 % → 1 % | 362.8 px | 0.39 | 0.15 | 36 |
| stroke 99 | 10 % → 1 % | 377.2 px | 0.39 | 0.14 | 23 |
| stroke 100 | 11 % → 1 % | 436.0 px | 0.39 | 0.13 | 21 |
| stroke 101 | 11 % → 1 % | 372.2 px | 0.39 | 0.12 | 28 |
| stroke 102 | 11 % → 1 % | 369.0 px | 0.39 | 0.12 | 36 |
| stroke 103 | 11 % → 1 % | 367.0 px | 0.39 | 0.12 | 42 |
| stroke 104 | 11 % → 1 % | 275.5 px | 0.39 | 0.11 | 44 |
| stroke 105 | 10 % → 1 % | 248.5 px | 0.39 | 0.11 | 77 |
| stroke 106 | 10 % → 1 % | 220.4 px | 0.39 | 0.10 | 105 |
| stroke 107 | 10 % → 1 % | 251.3 px | 0.39 | 0.09 | 69 |
| stroke 108 | 11 % → 0 % | 570.5 px | 0.37 | 0.00 | 64 |
| stroke 109 | 1 % → 0 % | 19.4 px | 0.00 | 0.00 | 69 |
| stroke 110 | 1 % → 0 % | 77.0 px | 0.00 | 0.00 | 29 |
| stroke 111 | 7 % → 3 % | 66.9 px | 0.38 | 0.47 | 264 |
| stroke 112 | 10 % → 3 % | 95.4 px | 0.38 | 0.31 | 192 |
| stroke 113 | 15 % → 4 % | 134.0 px | 0.38 | 0.23 | 326 |
| stroke 114 | 20 % → 4 % | 156.4 px | 0.38 | 0.19 | 292 |
| stroke 115 | 4 % → 0 % | 70.8 px | 0.00 | 0.00 | 35 |
| stroke 116 | 7 % → 0 % | 87.6 px | 0.00 | 0.00 | 60 |
| stroke 117 | 1 % → 2 % | 21.9 px | 0.39 | 1.70 | 47 |
| stroke 118 | 4 % → 5 % | 19.6 px | 0.38 | 1.50 | 103 |

Numbers say: wet paint spreads well beyond the stroke.

## Refs v3 · #08 HW lilac crown basket — own sheet
own sheet 800 × 1150 · Gouache 1.00 + turpentine 30 % · 36 px · 122.1 s

![Refs v3 · #08 HW lilac crown basket — own sheet](Refs-v3-08-HW-lilac-crown-basket-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 11 % → 11 % | 34.7 px | 0.30 | 0.93 | 44 |
| stroke 2 | 22 % → 9 % | 38.9 px | 0.30 | 0.40 | 112 |
| stroke 3 | 28 % → 6 % | 47.2 px | 0.30 | 0.23 | 162 |
| stroke 4 | 7 % → 1 % | 36.8 px | 0.30 | 0.10 | 50 |
| stroke 5 | 11 % → 0 % | 52.5 px | 0.30 | 0.03 | 47 |
| stroke 6 | 13 % → 1 % | 60.8 px | 0.30 | 0.08 | 62 |
| stroke 7 | 20 % → 2 % | 105.3 px | 0.29 | 0.12 | 37 |
| stroke 8 | 28 % → 0 % | 280.9 px | 0.00 | 0.00 | 10 |
| stroke 9 | 23 % → 1 % | 112.6 px | 0.30 | 0.05 | 53 |
| stroke 10 | 23 % → 1 % | 102.1 px | 0.30 | 0.05 | 71 |
| stroke 11 | 23 % → 3 % | 120.7 px | 0.29 | 0.11 | 49 |
| stroke 12 | 22 % → 1 % | 172.3 px | 0.30 | 0.07 | 20 |
| stroke 13 | 7 % → 3 % | 38.4 px | 0.28 | 0.47 | 16 |
| stroke 14 | 10 % → 6 % | 56.3 px | 0.29 | 0.59 | 18 |
| stroke 15 | 9 % → 3 % | 37.2 px | 0.30 | 0.29 | 20 |
| stroke 16 | 4 % → 0 % | 40.3 px | 0.00 | 0.00 | 6 |
| stroke 17 | 18 % → 15 % | 40.5 px | 0.31 | 0.84 | 65 |
| stroke 18 | 15 % → 22 % | 92.2 px | 0.31 | 1.48 | 12 |
| stroke 19 | 26 % → 10 % | 90.1 px | 0.31 | 0.40 | 36 |
| stroke 20 | 36 % → 19 % | 102.9 px | 0.31 | 0.52 | 31 |
| stroke 21 | 42 % → 19 % | 77.2 px | 0.31 | 0.45 | 61 |
| stroke 22 | 51 % → 15 % | 360.5 px | 0.30 | 0.29 | 9 |
| stroke 23 | 13 % → 0 % | 35.1 px | 0.00 | 0.00 | 134 |
| stroke 24 | 19 % → 0 % | 43.9 px | 0.00 | 0.00 | 305 |
| stroke 25 | 28 % → 0 % | 68.8 px | 0.00 | 0.00 | 234 |
| stroke 26 | 6 % → 0 % | 35.9 px | 0.00 | 0.00 | 42 |
| stroke 27 | 10 % → 0 % | 41.2 px | 0.00 | 0.00 | 173 |
| stroke 28 | 16 % → 0 % | 103.3 px | 0.00 | 0.00 | 20 |
| stroke 29 | 20 % → 0 % | 101.8 px | 0.00 | 0.00 | 57 |
| stroke 30 | 14 % → 0 % | 116.7 px | 0.00 | 0.00 | 21 |
| stroke 31 | 14 % → 0 % | 151.5 px | 0.00 | 0.00 | 19 |
| stroke 32 | 4 % → 0 % | 37.5 px | 0.00 | 0.00 | 14 |
| stroke 33 | 8 % → 0 % | 48.3 px | 0.00 | 0.00 | 27 |
| stroke 34 | 11 % → 0 % | 60.5 px | 0.00 | 0.00 | 30 |
| stroke 35 | 15 % → 0 % | 112.5 px | 0.00 | 0.00 | 26 |
| stroke 36 | 19 % → 0 % | 179.5 px | 0.00 | 0.00 | 17 |
| stroke 37 | 21 % → 0 % | 146.4 px | 0.00 | 0.00 | 28 |
| stroke 38 | 22 % → 0 % | 141.0 px | 0.00 | 0.00 | 33 |
| stroke 39 | 25 % → 0 % | 102.9 px | 0.00 | 0.00 | 102 |
| stroke 40 | 25 % → 0 % | 111.6 px | 0.00 | 0.00 | 86 |
| stroke 41 | 32 % → 0 % | 112.4 px | 0.00 | 0.00 | 69 |
| stroke 42 | 30 % → 0 % | 75.6 px | 0.00 | 0.00 | 211 |
| stroke 43 | 36 % → 0 % | 79.4 px | 0.00 | 0.00 | 175 |
| stroke 44 | 46 % → 0 % | 93.2 px | 0.00 | 0.00 | 206 |
| stroke 45 | 67 % → 0 % | 142.6 px | 0.00 | 0.00 | 84 |
| stroke 46 | 88 % → 0 % | 387.3 px | 0.00 | 0.00 | 23 |
| stroke 47 | 4 % → 0 % | 41.9 px | 0.00 | 0.00 | 24 |
| stroke 48 | 8 % → 0 % | 65.4 px | 0.00 | 0.00 | 13 |
| stroke 49 | 4 % → 0 % | 42.3 px | 0.00 | 0.00 | 13 |
| stroke 50 | 8 % → 0 % | 59.1 px | 0.00 | 0.00 | 8 |
| stroke 51 | 20 % → 0 % | 46.8 px | 0.00 | 0.00 | 57 |
| stroke 52 | 33 % → 0 % | 63.3 px | 0.00 | 0.00 | 156 |
| stroke 53 | 5 % → 0 % | 15.6 px | 0.00 | 0.00 | 27 |
| stroke 54 | 6 % → 0 % | 16.9 px | 0.00 | 0.00 | 8 |
| stroke 55 | 4 % → 0 % | 21.0 px | 0.28 | 0.09 | 16 |
| stroke 56 | 3 % → 17 % | 16.6 px | 0.32 | 5.87 | 5 |
| stroke 57 | 4 % → 2 % | 20.5 px | 0.28 | 0.49 | 20 |
| stroke 58 | 4 % → 4 % | 23.3 px | 0.33 | 1.21 | 19 |
| stroke 59 | 7 % → 4 % | 65.0 px | 0.33 | 0.49 | 20 |
| stroke 60 | 4 % → 0 % | 17.5 px | 0.00 | 0.00 | 13 |
| stroke 61 | 10 % → 0 % | 42.5 px | 0.00 | 0.00 | 19 |
| stroke 62 | 16 % → 0 % | 46.6 px | 0.00 | 0.00 | 25 |
| stroke 63 | 7 % → 0 % | 30.1 px | 0.00 | 0.00 | 51 |
| stroke 64 | 5 % → 0 % | 25.9 px | 0.00 | 0.00 | 23 |
| stroke 65 | 6 % → 0 % | 34.8 px | 0.00 | 0.00 | 58 |
| stroke 66 | 10 % → 0 % | 71.4 px | 0.00 | 0.00 | 16 |
| stroke 67 | 15 % → 0 % | 51.6 px | 0.00 | 0.00 | 37 |
| stroke 68 | 6 % → 0 % | 35.7 px | 0.00 | 0.00 | 23 |
| stroke 69 | 9 % → 0 % | 51.6 px | 0.00 | 0.00 | 27 |
| stroke 70 | 12 % → 0 % | 63.5 px | 0.00 | 0.00 | 39 |
| stroke 71 | 10 % → 0 % | 33.1 px | 0.00 | 0.00 | 72 |
| stroke 72 | 3 % → 5 % | 30.2 px | 0.30 | 1.99 | 8 |
| stroke 73 | 9 % → 10 % | 31.7 px | 0.30 | 1.16 | 71 |
| stroke 74 | 4 % → 1 % | 28.9 px | 0.27 | 0.24 | 7 |
| stroke 75 | 16 % → 7 % | 42.9 px | 0.30 | 0.41 | 312 |
| stroke 76 | 19 % → 7 % | 52.1 px | 0.30 | 0.35 | 181 |
| stroke 77 | 27 % → 13 % | 376.2 px | 0.30 | 0.49 | 7 |
| stroke 78 | 27 % → 10 % | 194.2 px | 0.30 | 0.37 | 20 |
| stroke 79 | 29 % → 7 % | 174.5 px | 0.29 | 0.25 | 18 |
| stroke 80 | 28 % → 3 % | 125.1 px | 0.29 | 0.12 | 89 |
| stroke 81 | 24 % → 0 % | 149.6 px | 0.30 | 0.00 | 50 |
| stroke 82 | 23 % → 0 % | 100.9 px | 0.00 | 0.00 | 35 |
| stroke 83 | 21 % → 0 % | 152.0 px | 0.00 | 0.00 | 12 |
| stroke 84 | 21 % → 0 % | 196.1 px | 0.00 | 0.00 | 16 |
| stroke 85 | 22 % → 0 % | 203.7 px | 0.00 | 0.00 | 11 |
| stroke 86 | 22 % → 0 % | 165.8 px | 0.00 | 0.00 | 15 |
| stroke 87 | 22 % → 0 % | 209.9 px | 0.00 | 0.00 | 17 |
| stroke 88 | 21 % → 0 % | 198.6 px | 0.00 | 0.00 | 47 |
| stroke 89 | 20 % → 0 % | 252.0 px | 0.00 | 0.00 | 19 |
| stroke 90 | 17 % → 0 % | 161.3 px | 0.00 | 0.00 | 27 |
| stroke 91 | 3 % → 0 % | 30.2 px | 0.00 | 0.00 | 14 |
| stroke 92 | 7 % → 0 % | 34.4 px | 0.00 | 0.00 | 25 |
| stroke 93 | 10 % → 0 % | 53.2 px | 0.00 | 0.00 | 20 |
| stroke 94 | 2 % → 0 % | 29.7 px | 0.27 | 0.02 | 7 |
| stroke 95 | 5 % → 0 % | 50.9 px | 0.27 | 0.06 | 6 |
| stroke 96 | 9 % → 0 % | 70.5 px | 0.00 | 0.00 | 9 |
| stroke 97 | 10 % → 0 % | 72.0 px | 0.00 | 0.00 | 12 |
| stroke 98 | 13 % → 0 % | 104.4 px | 0.00 | 0.00 | 9 |
| stroke 99 | 13 % → 0 % | 92.0 px | 0.31 | 0.01 | 15 |
| stroke 100 | 6 % → 14 % | 51.3 px | 0.31 | 2.13 | 7 |
| stroke 101 | 19 % → 0 % | 150.0 px | 0.32 | 0.02 | 10 |
| stroke 102 | 19 % → 10 % | 117.1 px | 0.31 | 0.54 | 55 |
| stroke 103 | 22 % → 5 % | 96.8 px | 0.31 | 0.22 | 60 |
| stroke 104 | 29 % → 1 % | 235.9 px | 0.32 | 0.02 | 15 |
| stroke 105 | 11 % → 0 % | 76.2 px | 0.00 | 0.00 | 16 |
| stroke 106 | 12 % → 0 % | 60.8 px | 0.00 | 0.00 | 20 |
| stroke 107 | 12 % → 0 % | 122.1 px | 0.00 | 0.00 | 6 |
| stroke 108 | 19 % → 0 % | 183.5 px | 0.00 | 0.00 | 12 |
| stroke 109 | 3 % → 0 % | 31.3 px | 0.00 | 0.00 | 11 |
| stroke 110 | 9 % → 0 % | 56.9 px | 0.00 | 0.00 | 25 |
| stroke 111 | 16 % → 0 % | 112.8 px | 0.00 | 0.00 | 16 |
| stroke 112 | 21 % → 0 % | 120.3 px | 0.00 | 0.00 | 34 |
| stroke 113 | 29 % → 0 % | 353.1 px | 0.00 | 0.00 | 9 |
| stroke 114 | 9 % → 0 % | 29.2 px | 0.00 | 0.00 | 113 |
| stroke 115 | 14 % → 0 % | 35.4 px | 0.00 | 0.00 | 316 |
| stroke 116 | 18 % → 0 % | 40.8 px | 0.00 | 0.00 | 179 |
| stroke 117 | 20 % → 0 % | 79.2 px | 0.00 | 0.00 | 69 |
| stroke 118 | 33 % → 0 % | 135.9 px | 0.00 | 0.00 | 40 |
| stroke 119 | 21 % → 0 % | 63.7 px | 0.00 | 0.00 | 64 |
| stroke 120 | 18 % → 0 % | 127.4 px | 0.00 | 0.00 | 14 |
| stroke 121 | 19 % → 0 % | 69.4 px | 0.00 | 0.00 | 62 |
| stroke 122 | 15 % → 0 % | 210.6 px | 0.00 | 0.00 | 15 |
| stroke 123 | 17 % → 0 % | 76.8 px | 0.00 | 0.00 | 41 |
| stroke 124 | 21 % → 0 % | 76.5 px | 0.00 | 0.00 | 80 |
| stroke 125 | 15 % → 0 % | 181.0 px | 0.00 | 0.00 | 8 |
| stroke 126 | 25 % → 0 % | 75.4 px | 0.00 | 0.00 | 103 |
| stroke 127 | 15 % → 0 % | 190.9 px | 0.00 | 0.00 | 4 |
| stroke 128 | 37 % → 0 % | 277.9 px | 0.00 | 0.00 | 16 |
| stroke 129 | 25 % → 0 % | 117.2 px | 0.00 | 0.00 | 21 |
| stroke 130 | 25 % → 0 % | 158.4 px | 0.00 | 0.00 | 20 |
| stroke 131 | 12 % → 0 % | 165.4 px | 0.00 | 0.00 | 8 |
| stroke 132 | 13 % → 0 % | 173.9 px | 0.00 | 0.00 | 8 |
| stroke 133 | 13 % → 0 % | 116.6 px | 0.00 | 0.00 | 13 |
| stroke 134 | 13 % → 0 % | 123.3 px | 0.00 | 0.00 | 12 |
| stroke 135 | 13 % → 0 % | 165.6 px | 0.00 | 0.00 | 10 |
| stroke 136 | 14 % → 0 % | 124.3 px | 0.00 | 0.00 | 12 |
| stroke 137 | 16 % → 0 % | 197.9 px | 0.00 | 0.00 | 8 |
| stroke 138 | 18 % → 0 % | 152.2 px | 0.00 | 0.00 | 12 |
| stroke 139 | 18 % → 0 % | 194.5 px | 0.00 | 0.00 | 22 |
| stroke 140 | 20 % → 0 % | 153.5 px | 0.00 | 0.00 | 22 |
| stroke 141 | 20 % → 0 % | 156.2 px | 0.00 | 0.00 | 12 |
| stroke 142 | 20 % → 0 % | 198.6 px | 0.00 | 0.00 | 5 |
| stroke 143 | 20 % → 0 % | 148.0 px | 0.00 | 0.00 | 23 |
| stroke 144 | 22 % → 0 % | 223.4 px | 0.00 | 0.00 | 6 |
| stroke 145 | 22 % → 0 % | 180.6 px | 0.00 | 0.00 | 7 |
| stroke 146 | 23 % → 0 % | 203.9 px | 0.00 | 0.00 | 6 |
| stroke 147 | 22 % → 0 % | 191.1 px | 0.00 | 0.00 | 7 |
| stroke 148 | 9 % → 0 % | 70.8 px | 0.00 | 0.00 | 9 |
| stroke 149 | 9 % → 0 % | 78.1 px | 0.00 | 0.00 | 7 |
| stroke 150 | 10 % → 0 % | 89.7 px | 0.00 | 0.00 | 5 |
| stroke 151 | 13 % → 0 % | 96.1 px | 0.00 | 0.00 | 7 |
| stroke 152 | 9 % → 12 % | 44.4 px | 0.31 | 1.30 | 37 |
| stroke 153 | 13 % → 11 % | 65.1 px | 0.31 | 0.86 | 36 |
| stroke 154 | 18 % → 16 % | 182.8 px | 0.31 | 0.85 | 14 |
| stroke 155 | 22 % → 15 % | 214.3 px | 0.31 | 0.66 | 20 |
| stroke 156 | 3 % → 1 % | 28.5 px | 0.28 | 0.45 | 5 |
| stroke 157 | 4 % → 0 % | 27.0 px | 0.00 | 0.00 | 20 |
| stroke 158 | 4 % → 0 % | 42.6 px | 0.00 | 0.00 | 8 |
| stroke 159 | 3 % → 5 % | 22.3 px | 0.31 | 1.60 | 44 |
| stroke 160 | 4 % → 0 % | 23.4 px | 0.00 | 0.00 | 20 |
| stroke 161 | 10 % → 0 % | 43.1 px | 0.00 | 0.00 | 47 |
| stroke 162 | 6 % → 17 % | 23.4 px | 0.31 | 2.96 | 18 |
| stroke 163 | 11 % → 3 % | 43.5 px | 0.31 | 0.31 | 52 |
| stroke 164 | 4 % → 0 % | 24.3 px | 0.00 | 0.00 | 13 |
| stroke 165 | 4 % → 0 % | 22.7 px | 0.00 | 0.00 | 16 |
| stroke 166 | 8 % → 0 % | 48.8 px | 0.00 | 0.00 | 21 |
| stroke 167 | 3 % → 0 % | 24.4 px | 0.00 | 0.00 | 16 |
| stroke 168 | 16 % → 0 % | 63.7 px | 0.00 | 0.00 | 66 |
| stroke 169 | 23 % → 0 % | 76.8 px | 0.00 | 0.00 | 107 |
| stroke 170 | 29 % → 0 % | 91.8 px | 0.00 | 0.00 | 160 |
| stroke 171 | 31 % → 0 % | 105.8 px | 0.00 | 0.00 | 278 |
| stroke 172 | 31 % → 0 % | 191.4 px | 0.00 | 0.00 | 143 |
| stroke 173 | 27 % → 0 % | 171.1 px | 0.00 | 0.00 | 83 |
| stroke 174 | 25 % → 0 % | 142.3 px | 0.00 | 0.00 | 73 |
| stroke 175 | 27 % → 0 % | 173.3 px | 0.00 | 0.00 | 68 |
| stroke 176 | 26 % → 0 % | 182.8 px | 0.00 | 0.00 | 50 |
| stroke 177 | 17 % → 0 % | 64.3 px | 0.35 | 0.01 | 68 |
| stroke 178 | 26 % → 0 % | 147.7 px | 0.00 | 0.00 | 66 |
| stroke 179 | 23 % → 5 % | 77.5 px | 0.33 | 0.22 | 124 |
| stroke 180 | 24 % → 0 % | 111.7 px | 0.00 | 0.00 | 113 |
| stroke 181 | 29 % → 7 % | 89.4 px | 0.31 | 0.25 | 206 |
| stroke 182 | 29 % → 0 % | 135.6 px | 0.00 | 0.00 | 159 |
| stroke 183 | 33 % → 7 % | 106.9 px | 0.31 | 0.22 | 340 |
| stroke 184 | 37 % → 0 % | 294.7 px | 0.00 | 0.00 | 47 |
| stroke 185 | 33 % → 9 % | 114.1 px | 0.30 | 0.27 | 278 |
| stroke 186 | 34 % → 2 % | 152.9 px | 0.30 | 0.07 | 139 |
| stroke 187 | 29 % → 4 % | 129.8 px | 0.30 | 0.13 | 502 |
| stroke 188 | 35 % → 5 % | 148.5 px | 0.30 | 0.15 | 714 |
| stroke 189 | 42 % → 6 % | 196.9 px | 0.30 | 0.15 | 193 |
| stroke 190 | 44 % → 4 % | 240.5 px | 0.29 | 0.08 | 72 |
| stroke 191 | 42 % → 1 % | 331.4 px | 0.28 | 0.02 | 51 |
| stroke 192 | 16 % → 2 % | 64.3 px | 0.29 | 0.16 | 55 |
| stroke 193 | 26 % → 1 % | 89.6 px | 0.28 | 0.05 | 82 |
| stroke 194 | 44 % → 0 % | 206.9 px | 0.00 | 0.00 | 25 |
| stroke 195 | 14 % → 3 % | 67.0 px | 0.30 | 0.18 | 47 |
| stroke 196 | 20 % → 4 % | 90.6 px | 0.30 | 0.19 | 66 |
| stroke 197 | 28 % → 3 % | 127.3 px | 0.30 | 0.13 | 66 |
| stroke 198 | 5 % → 13 % | 38.5 px | 0.31 | 2.48 | 44 |
| stroke 199 | 10 % → 11 % | 68.8 px | 0.31 | 1.12 | 24 |
| stroke 200 | 13 % → 12 % | 99.1 px | 0.30 | 0.91 | 30 |
| stroke 201 | 4 % → 0 % | 38.6 px | 0.00 | 0.00 | 18 |
| stroke 202 | 7 % → 0 % | 47.6 px | 0.00 | 0.00 | 23 |
| stroke 203 | 12 % → 4 % | 67.3 px | 0.30 | 0.31 | 38 |
| stroke 204 | 12 % → 5 % | 51.0 px | 0.30 | 0.45 | 100 |
| stroke 205 | 17 % → 13 % | 140.0 px | 0.30 | 0.77 | 27 |
| stroke 206 | 29 % → 9 % | 351.8 px | 0.32 | 0.32 | 6 |
| stroke 207 | 28 % → 9 % | 359.5 px | 0.32 | 0.32 | 8 |
| stroke 208 | 6 % → 0 % | 37.5 px | 0.00 | 0.00 | 35 |
| stroke 209 | 12 % → 0 % | 49.4 px | 0.00 | 0.00 | 66 |
| stroke 210 | 16 % → 0 % | 60.0 px | 0.00 | 0.00 | 93 |
| stroke 211 | 17 % → 7 % | 67.9 px | 0.32 | 0.44 | 70 |
| stroke 212 | 11 % → 13 % | 82.6 px | 0.31 | 1.25 | 22 |
| stroke 213 | 3 % → 0 % | 39.0 px | 0.00 | 0.00 | 8 |
| stroke 214 | 20 % → 9 % | 72.4 px | 0.31 | 0.46 | 83 |
| stroke 215 | 12 % → 0 % | 45.9 px | 0.00 | 0.00 | 62 |
| stroke 216 | 32 % → 6 % | 123.0 px | 0.32 | 0.18 | 72 |
| stroke 217 | 22 % → 18 % | 293.6 px | 0.31 | 0.82 | 14 |
| stroke 218 | 18 % → 0 % | 140.4 px | 0.00 | 0.00 | 26 |
| stroke 219 | 22 % → 0 % | 105.5 px | 0.00 | 0.00 | 86 |
| stroke 220 | 41 % → 0 % | 218.4 px | 0.00 | 0.00 | 44 |
| stroke 221 | 27 % → 0 % | 258.4 px | 0.00 | 0.00 | 16 |
| stroke 222 | 20 % → 0 % | 156.4 px | 0.00 | 0.00 | 13 |
| stroke 223 | 42 % → 0 % | 227.8 px | 0.00 | 0.00 | 39 |
| stroke 224 | 28 % → 16 % | 272.3 px | 0.31 | 0.58 | 23 |
| stroke 225 | 21 % → 0 % | 164.2 px | 0.00 | 0.00 | 26 |
| stroke 226 | 39 % → 0 % | 251.2 px | 0.00 | 0.00 | 40 |
| stroke 227 | 22 % → 0 % | 205.9 px | 0.00 | 0.00 | 7 |
| stroke 228 | 22 % → 0 % | 212.5 px | 0.00 | 0.00 | 14 |
| stroke 229 | 20 % → 13 % | 234.6 px | 0.31 | 0.64 | 15 |
| stroke 230 | 25 % → 0 % | 123.0 px | 0.00 | 0.00 | 254 |
| stroke 231 | 24 % → 0 % | 128.1 px | 0.00 | 0.00 | 33 |
| stroke 232 | 23 % → 9 % | 153.1 px | 0.31 | 0.41 | 38 |
| stroke 233 | 25 % → 14 % | 269.7 px | 0.31 | 0.57 | 11 |
| stroke 234 | 29 % → 0 % | 99.0 px | 0.00 | 0.00 | 148 |
| stroke 235 | 29 % → 7 % | 119.1 px | 0.31 | 0.25 | 74 |
| stroke 236 | 36 % → 0 % | 146.4 px | 0.00 | 0.00 | 102 |
| stroke 237 | 35 % → 4 % | 121.4 px | 0.31 | 0.11 | 267 |
| stroke 238 | 42 % → 0 % | 272.5 px | 0.00 | 0.00 | 32 |
| stroke 239 | 41 % → 4 % | 239.4 px | 0.31 | 0.10 | 38 |
| stroke 240 | 35 % → 8 % | 310.6 px | 0.31 | 0.22 | 11 |
| stroke 241 | 42 % → 0 % | 395.2 px | 0.00 | 0.00 | 14 |
| stroke 242 | 38 % → 0 % | 519.1 px | 0.00 | 0.00 | 17 |
| stroke 243 | 37 % → 4 % | 151.9 px | 0.31 | 0.10 | 56 |
| stroke 244 | 43 % → 0 % | 176.2 px | 0.00 | 0.00 | 92 |
| stroke 245 | 42 % → 2 % | 199.6 px | 0.32 | 0.05 | 62 |
| stroke 246 | 44 % → 0 % | 590.4 px | 0.00 | 0.00 | 8 |
| stroke 247 | 49 % → 0 % | 215.4 px | 0.31 | 0.00 | 52 |
| stroke 248 | 51 % → 0 % | 488.2 px | 0.00 | 0.00 | 7 |
| stroke 249 | 6 % → 0 % | 86.9 px | 0.00 | 0.00 | 4 |
| stroke 250 | 8 % → 0 % | 59.7 px | 0.00 | 0.00 | 27 |
| stroke 251 | 11 % → 0 % | 60.7 px | 0.00 | 0.00 | 47 |
| stroke 252 | 14 % → 0 % | 79.7 px | 0.00 | 0.00 | 77 |
| stroke 253 | 18 % → 0 % | 111.7 px | 0.00 | 0.00 | 42 |
| stroke 254 | 3 % → 0 % | 39.2 px | 0.00 | 0.00 | 5 |
| stroke 255 | 16 % → 7 % | 217.0 px | 0.31 | 0.47 | 7 |
| stroke 256 | 8 % → 1 % | 105.2 px | 0.31 | 0.09 | 4 |
| stroke 257 | 18 % → 4 % | 80.3 px | 0.31 | 0.23 | 53 |
| stroke 258 | 6 % → 0 % | 55.6 px | 0.00 | 0.00 | 36 |
| stroke 259 | 23 % → 5 % | 127.0 px | 0.31 | 0.20 | 24 |
| stroke 260 | 20 % → 0 % | 90.3 px | 0.00 | 0.00 | 64 |
| stroke 261 | 34 % → 6 % | 225.7 px | 0.31 | 0.18 | 19 |
| stroke 262 | 29 % → 0 % | 149.7 px | 0.00 | 0.00 | 47 |
| stroke 263 | 36 % → 0 % | 213.4 px | 0.00 | 0.00 | 34 |
| stroke 264 | 39 % → 0 % | 198.7 px | 0.00 | 0.00 | 42 |
| stroke 265 | 45 % → 0 % | 541.1 px | 0.00 | 0.00 | 5 |
| stroke 266 | 3 % → 0 % | 42.9 px | 0.00 | 0.00 | 9 |
| stroke 267 | 10 % → 0 % | 42.0 px | 0.00 | 0.00 | 108 |
| stroke 268 | 16 % → 0 % | 86.9 px | 0.00 | 0.00 | 50 |
| stroke 269 | 20 % → 0 % | 153.8 px | 0.00 | 0.00 | 20 |
| stroke 270 | 12 % → 0 % | 36.8 px | 0.00 | 0.00 | 71 |
| stroke 271 | 8 % → 0 % | 51.8 px | 0.00 | 0.00 | 27 |
| stroke 272 | 18 % → 0 % | 43.4 px | 0.00 | 0.00 | 214 |
| stroke 273 | 26 % → 0 % | 60.9 px | 0.00 | 0.00 | 479 |
| stroke 274 | 28 % → 0 % | 128.8 px | 0.00 | 0.00 | 59 |
| stroke 275 | 41 % → 0 % | 303.8 px | 0.00 | 0.00 | 17 |
| stroke 276 | 41 % → 0 % | 224.9 px | 0.00 | 0.00 | 30 |
| stroke 277 | 28 % → 0 % | 174.7 px | 0.00 | 0.00 | 29 |
| stroke 278 | 26 % → 0 % | 189.9 px | 0.00 | 0.00 | 36 |
| stroke 279 | 43 % → 0 % | 565.5 px | 0.00 | 0.00 | 11 |
| stroke 280 | 32 % → 0 % | 400.3 px | 0.00 | 0.00 | 5 |
| stroke 281 | 28 % → 0 % | 210.1 px | 0.00 | 0.00 | 21 |
| stroke 282 | 37 % → 0 % | 230.9 px | 0.00 | 0.00 | 74 |
| stroke 283 | 26 % → 0 % | 352.8 px | 0.00 | 0.00 | 16 |
| stroke 284 | 36 % → 0 % | 223.6 px | 0.00 | 0.00 | 38 |
| stroke 285 | 36 % → 0 % | 199.6 px | 0.00 | 0.00 | 29 |
| stroke 286 | 35 % → 0 % | 436.9 px | 0.00 | 0.00 | 11 |
| stroke 287 | 40 % → 0 % | 377.3 px | 0.00 | 0.00 | 7 |
| stroke 288 | 50 % → 0 % | 270.1 px | 0.00 | 0.00 | 25 |
| stroke 289 | 26 % → 0 % | 195.0 px | 0.00 | 0.00 | 22 |
| stroke 290 | 49 % → 0 % | 181.2 px | 0.00 | 0.00 | 87 |
| stroke 291 | 28 % → 0 % | 121.2 px | 0.00 | 0.00 | 45 |
| stroke 292 | 38 % → 0 % | 189.8 px | 0.00 | 0.00 | 29 |
| stroke 293 | 28 % → 0 % | 388.7 px | 0.00 | 0.00 | 12 |
| stroke 294 | 41 % → 0 % | 185.9 px | 0.00 | 0.00 | 25 |
| stroke 295 | 38 % → 0 % | 271.4 px | 0.00 | 0.00 | 25 |
| stroke 296 | 8 % → 17 % | 21.8 px | 0.32 | 2.20 | 18 |
| stroke 297 | 4 % → 0 % | 16.9 px | 0.00 | 0.00 | 9 |
| stroke 298 | 6 % → 1 % | 53.1 px | 0.26 | 0.12 | 10 |
| stroke 299 | 6 % → 8 % | 26.9 px | 0.29 | 1.37 | 22 |
| stroke 300 | 12 % → 7 % | 100.6 px | 0.29 | 0.55 | 5 |
| stroke 301 | 4 % → 11 % | 30.6 px | 0.28 | 2.91 | 15 |
| stroke 302 | 5 % → 0 % | 29.7 px | 0.00 | 0.00 | 20 |
| stroke 303 | 3 % → 13 % | 34.2 px | 0.30 | 3.99 | 4 |
| stroke 304 | 3 % → 5 % | 24.2 px | 0.30 | 1.37 | 7 |
| stroke 305 | 4 % → 0 % | 23.5 px | 0.00 | 0.00 | 18 |
| stroke 306 | 5 % → 0 % | 31.8 px | 0.00 | 0.00 | 17 |
| stroke 307 | 2 % → 0 % | 23.0 px | 0.00 | 0.00 | 6 |
| stroke 308 | 9 % → 0 % | 49.2 px | 0.00 | 0.00 | 29 |
| stroke 309 | 2 % → 0 % | 23.0 px | 0.00 | 0.00 | 11 |
| stroke 310 | 11 % → 0 % | 54.4 px | 0.00 | 0.00 | 32 |
| stroke 311 | 18 % → 0 % | 85.4 px | 0.00 | 0.00 | 58 |
| stroke 312 | 14 % → 0 % | 67.0 px | 0.00 | 0.00 | 58 |
| stroke 313 | 18 % → 0 % | 67.4 px | 0.00 | 0.00 | 77 |
| stroke 314 | 9 % → 0 % | 68.3 px | 0.00 | 0.00 | 22 |
| stroke 315 | 12 % → 0 % | 66.8 px | 0.00 | 0.00 | 54 |
| stroke 316 | 40 % → 0 % | 94.8 px | 0.00 | 0.00 | 270 |
| stroke 317 | 18 % → 0 % | 109.2 px | 0.00 | 0.00 | 71 |
| stroke 318 | 28 % → 0 % | 201.7 px | 0.00 | 0.00 | 37 |
| stroke 319 | 54 % → 0 % | 258.3 px | 0.00 | 0.00 | 90 |
| stroke 320 | 25 % → 0 % | 182.4 px | 0.00 | 0.00 | 44 |
| stroke 321 | 42 % → 0 % | 202.7 px | 0.00 | 0.00 | 52 |
| stroke 322 | 53 % → 2 % | 109.4 px | 0.31 | 0.04 | 365 |
| stroke 323 | 33 % → 0 % | 164.9 px | 0.00 | 0.00 | 45 |
| stroke 324 | 61 % → 0 % | 123.5 px | 0.00 | 0.00 | 557 |
| stroke 325 | 54 % → 0 % | 173.8 px | 0.00 | 0.00 | 154 |
| stroke 326 | 53 % → 0 % | 161.4 px | 0.00 | 0.00 | 109 |
| stroke 327 | 51 % → 0 % | 137.8 px | 0.00 | 0.00 | 137 |
| stroke 328 | 48 % → 0 % | 127.8 px | 0.00 | 0.00 | 168 |
| stroke 329 | 38 % → 0 % | 111.1 px | 0.00 | 0.00 | 294 |
| stroke 330 | 51 % → 0 % | 110.4 px | 0.00 | 0.00 | 401 |
| stroke 331 | 26 % → 0 % | 106.3 px | 0.00 | 0.00 | 71 |
| stroke 332 | 53 % → 0 % | 104.8 px | 0.00 | 0.00 | 610 |
| stroke 333 | 59 % → 0 % | 142.4 px | 0.00 | 0.00 | 235 |
| stroke 334 | 46 % → 0 % | 152.2 px | 0.00 | 0.00 | 176 |
| stroke 335 | 56 % → 0 % | 150.7 px | 0.00 | 0.00 | 490 |
| stroke 336 | 48 % → 0 % | 200.4 px | 0.00 | 0.00 | 100 |
| stroke 337 | 53 % → 0 % | 127.7 px | 0.00 | 0.00 | 228 |
| stroke 338 | 46 % → 0 % | 246.4 px | 0.00 | 0.00 | 54 |
| stroke 339 | 46 % → 0 % | 116.1 px | 0.00 | 0.00 | 609 |
| stroke 340 | 35 % → 0 % | 257.4 px | 0.00 | 0.00 | 94 |
| stroke 341 | 37 % → 0 % | 111.9 px | 0.00 | 0.00 | 223 |
| stroke 342 | 53 % → 0 % | 248.4 px | 0.00 | 0.00 | 61 |
| stroke 343 | 7 % → 13 % | 27.9 px | 0.31 | 1.80 | 25 |
| stroke 344 | 9 % → 10 % | 25.4 px | 0.30 | 1.12 | 61 |
| stroke 345 | 7 % → 11 % | 68.8 px | 0.30 | 1.68 | 9 |
| stroke 346 | 5 % → 11 % | 31.1 px | 0.30 | 2.11 | 25 |
| stroke 347 | 10 % → 14 % | 65.5 px | 0.30 | 1.47 | 21 |
| stroke 348 | 9 % → 11 % | 27.6 px | 0.31 | 1.16 | 65 |

Numbers say: wet paint spreads well beyond the stroke.

## Refs v3 · #09 HW white loops — own sheet
own sheet 800 × 640 · Gouache 1.00 + turpentine 30 % · 104 px · 36.6 s

![Refs v3 · #09 HW white loops — own sheet](Refs-v3-09-HW-white-loops-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 11 % → 0 % | 72.7 px | 0.00 | 0.00 | 235 |
| stroke 2 | 7 % → 0 % | 103.2 px | 0.00 | 0.00 | 74 |
| stroke 3 | 21 % → 0 % | 116.9 px | 0.00 | 0.00 | 504 |
| stroke 4 | 21 % → 0 % | 159.6 px | 0.00 | 0.00 | 263 |
| stroke 5 | 30 % → 0 % | 168.8 px | 0.00 | 0.00 | 541 |
| stroke 6 | 39 % → 0 % | 151.2 px | 0.00 | 0.00 | 1305 |
| stroke 7 | 44 % → 0 % | 192.1 px | 0.00 | 0.00 | 1949 |
| stroke 8 | 50 % → 0 % | 232.2 px | 0.00 | 0.00 | 1611 |
| stroke 9 | 54 % → 0 % | 249.6 px | 0.00 | 0.00 | 1615 |
| stroke 10 | 57 % → 0 % | 265.9 px | 0.00 | 0.00 | 1751 |
| stroke 11 | 58 % → 1 % | 274.1 px | 0.75 | 0.01 | 1469 |
| stroke 12 | 57 % → 3 % | 275.7 px | 0.75 | 0.05 | 1292 |
| stroke 13 | 57 % → 7 % | 277.4 px | 0.75 | 0.12 | 1409 |
| stroke 14 | 60 % → 7 % | 287.5 px | 0.75 | 0.12 | 1449 |
| stroke 15 | 64 % → 10 % | 844.9 px | 0.75 | 0.15 | 452 |
| stroke 16 | 62 % → 15 % | 631.6 px | 0.75 | 0.24 | 550 |
| stroke 17 | 67 % → 12 % | 729.7 px | 0.75 | 0.17 | 396 |
| stroke 18 | 1 % → 0 % | 15.7 px | 0.00 | 0.00 | 20 |
| stroke 19 | 1 % → 0 % | 26.0 px | 0.00 | 0.00 | 27 |
| stroke 20 | 2 % → 0 % | 35.9 px | 0.00 | 0.00 | 52 |
| stroke 21 | 3 % → 0 % | 47.0 px | 0.00 | 0.00 | 35 |
| stroke 22 | 4 % → 0 % | 54.6 px | 0.00 | 0.00 | 61 |
| stroke 23 | 4 % → 0 % | 62.5 px | 0.00 | 0.00 | 64 |
| stroke 24 | 5 % → 0 % | 89.9 px | 0.00 | 0.00 | 74 |
| stroke 25 | 6 % → 0 % | 115.1 px | 0.00 | 0.00 | 34 |
| stroke 26 | 6 % → 0 % | 143.3 px | 0.00 | 0.00 | 34 |
| stroke 27 | 1 % → 15 % | 29.6 px | 0.75 | 26.52 | 12 |
| stroke 28 | 1 % → 15 % | 53.6 px | 0.75 | 13.73 | 13 |
| stroke 29 | 2 % → 16 % | 57.5 px | 0.75 | 10.03 | 19 |
| stroke 30 | 2 % → 16 % | 95.4 px | 0.75 | 7.84 | 12 |
| stroke 31 | 4 % → 4 % | 16.7 px | 0.75 | 0.84 | 511 |
| stroke 32 | 10 % → 2 % | 247.5 px | 0.74 | 0.17 | 44 |
| stroke 33 | 6 % → 4 % | 258.0 px | 0.74 | 0.65 | 21 |
| stroke 34 | 2 % → 15 % | 89.9 px | 0.75 | 6.16 | 33 |
| stroke 35 | 4 % → 14 % | 229.8 px | 0.75 | 4.04 | 9 |
| stroke 36 | 8 % → 18 % | 71.0 px | 0.75 | 2.30 | 45 |
| stroke 37 | 6 % → 22 % | 65.1 px | 0.75 | 3.89 | 22 |
| stroke 38 | 1 % → 0 % | 39.2 px | 0.00 | 0.00 | 9 |
| stroke 39 | 2 % → 0 % | 78.0 px | 0.00 | 0.00 | 9 |
| stroke 40 | 2 % → 0 % | 104.9 px | 0.00 | 0.00 | 8 |
| stroke 41 | 3 % → 0 % | 145.8 px | 0.00 | 0.00 | 5 |
| stroke 42 | 3 % → 0 % | 173.4 px | 0.00 | 0.00 | 14 |
| stroke 43 | 4 % → 0 % | 198.8 px | 0.00 | 0.00 | 7 |
| stroke 44 | 5 % → 0 % | 251.1 px | 0.00 | 0.00 | 6 |
| stroke 45 | 5 % → 0 % | 272.2 px | 0.00 | 0.00 | 5 |
| stroke 46 | 6 % → 0 % | 211.8 px | 0.00 | 0.00 | 92 |
| stroke 47 | 7 % → 0 % | 235.7 px | 0.73 | 0.06 | 15 |
| stroke 48 | 7 % → 1 % | 264.7 px | 0.75 | 0.17 | 12 |
| stroke 49 | 8 % → 2 % | 293.9 px | 0.75 | 0.30 | 14 |
| stroke 50 | 9 % → 4 % | 325.3 px | 0.75 | 0.46 | 12 |
| stroke 51 | 9 % → 6 % | 355.5 px | 0.75 | 0.64 | 11 |
| stroke 52 | 10 % → 8 % | 351.5 px | 0.75 | 0.79 | 12 |
| stroke 53 | 10 % → 10 % | 287.5 px | 0.74 | 0.96 | 18 |
| stroke 54 | 11 % → 12 % | 279.5 px | 0.75 | 1.10 | 20 |
| stroke 55 | 11 % → 13 % | 571.5 px | 0.75 | 1.10 | 8 |
| stroke 56 | 1 % → 17 % | 47.7 px | 0.75 | 15.92 | 30 |
| stroke 57 | 3 % → 18 % | 69.8 px | 0.75 | 6.78 | 25 |
| stroke 58 | 5 % → 19 % | 64.0 px | 0.75 | 3.60 | 89 |
| stroke 59 | 8 % → 20 % | 75.3 px | 0.75 | 2.38 | 101 |
| stroke 60 | 11 % → 21 % | 97.0 px | 0.75 | 1.85 | 110 |
| stroke 61 | 13 % → 15 % | 128.2 px | 0.75 | 1.21 | 86 |
| stroke 62 | 16 % → 16 % | 149.8 px | 0.75 | 1.03 | 106 |

Numbers say: wet paint spreads well beyond the stroke.

## Refs v3 · #10 HW maroon loops — own sheet
own sheet 800 × 1070 · Gouache 1.00 + turpentine 30 % · 104 px · 48.9 s

![Refs v3 · #10 HW maroon loops — own sheet](Refs-v3-10-HW-maroon-loops-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 6 % → 0 % | 96.5 px | 0.00 | 0.00 | 386 |
| stroke 2 | 13 % → 0 % | 110.7 px | 0.00 | 0.00 | 543 |
| stroke 3 | 18 % → 0 % | 171.9 px | 0.21 | 0.00 | 596 |
| stroke 4 | 22 % → 1 % | 219.3 px | 0.22 | 0.06 | 814 |
| stroke 5 | 27 % → 1 % | 273.8 px | 0.22 | 0.06 | 1309 |
| stroke 6 | 30 % → 2 % | 321.8 px | 0.22 | 0.05 | 456 |
| stroke 7 | 31 % → 2 % | 354.0 px | 0.22 | 0.05 | 441 |
| stroke 8 | 30 % → 1 % | 369.4 px | 0.22 | 0.04 | 673 |
| stroke 9 | 4 % → 4 % | 81.9 px | 0.22 | 0.82 | 84 |
| stroke 10 | 7 % → 1 % | 123.3 px | 0.22 | 0.18 | 63 |
| stroke 11 | 9 % → 0 % | 156.9 px | 0.21 | 0.02 | 146 |
| stroke 12 | 13 % → 1 % | 118.1 px | 0.20 | 0.05 | 381 |
| stroke 13 | 17 % → 1 % | 153.9 px | 0.20 | 0.05 | 809 |
| stroke 14 | 23 % → 1 % | 189.0 px | 0.20 | 0.04 | 352 |
| stroke 15 | 30 % → 1 % | 243.4 px | 0.20 | 0.03 | 254 |
| stroke 16 | 45 % → 1 % | 598.6 px | 0.20 | 0.03 | 123 |
| stroke 17 | 53 % → 2 % | 820.7 px | 0.20 | 0.03 | 79 |
| stroke 18 | 56 % → 2 % | 602.4 px | 0.20 | 0.03 | 135 |
| stroke 19 | 54 % → 2 % | 435.8 px | 0.20 | 0.04 | 147 |
| stroke 20 | 3 % → 2 % | 80.0 px | 0.22 | 0.58 | 89 |
| stroke 21 | 5 % → 2 % | 127.4 px | 0.22 | 0.37 | 116 |
| stroke 22 | 6 % → 2 % | 188.4 px | 0.22 | 0.29 | 113 |
| stroke 23 | 10 % → 2 % | 171.6 px | 0.22 | 0.18 | 200 |
| stroke 24 | 12 % → 2 % | 207.5 px | 0.22 | 0.15 | 117 |
| stroke 25 | 15 % → 2 % | 357.4 px | 0.22 | 0.13 | 71 |
| stroke 26 | 2 % → 1 % | 19.3 px | 0.22 | 0.55 | 51 |
| stroke 27 | 0 % → 3 % | 23.3 px | 0.22 | 6.60 | 8 |
| stroke 28 | 9 % → 0 % | 69.6 px | 0.00 | 0.00 | 203 |
| stroke 29 | 13 % → 0 % | 94.4 px | 0.00 | 0.00 | 305 |
| stroke 30 | 16 % → 0 % | 128.6 px | 0.00 | 0.00 | 472 |
| stroke 31 | 22 % → 0 % | 303.7 px | 0.00 | 0.00 | 232 |
| stroke 32 | 25 % → 0 % | 721.1 px | 0.00 | 0.00 | 59 |
| stroke 33 | 9 % → 2 % | 282.6 px | 0.22 | 0.26 | 58 |
| stroke 34 | 7 % → 2 % | 193.9 px | 0.22 | 0.34 | 63 |
| stroke 35 | 7 % → 2 % | 149.8 px | 0.22 | 0.34 | 97 |
| stroke 36 | 9 % → 2 % | 152.4 px | 0.22 | 0.25 | 127 |
| stroke 37 | 10 % → 0 % | 343.9 px | 0.00 | 0.00 | 71 |
| stroke 38 | 9 % → 2 % | 94.5 px | 0.22 | 0.20 | 576 |
| stroke 39 | 16 % → 2 % | 117.5 px | 0.22 | 0.13 | 901 |
| stroke 40 | 21 % → 3 % | 159.9 px | 0.22 | 0.12 | 700 |
| stroke 41 | 26 % → 3 % | 196.3 px | 0.22 | 0.10 | 904 |
| stroke 42 | 32 % → 3 % | 249.2 px | 0.22 | 0.09 | 720 |
| stroke 43 | 36 % → 3 % | 292.7 px | 0.22 | 0.07 | 662 |
| stroke 44 | 38 % → 1 % | 322.5 px | 0.22 | 0.04 | 560 |
| stroke 45 | 37 % → 2 % | 481.1 px | 0.21 | 0.05 | 518 |
| stroke 46 | 34 % → 2 % | 384.4 px | 0.21 | 0.06 | 526 |
| stroke 47 | 35 % → 2 % | 364.7 px | 0.21 | 0.06 | 641 |
| stroke 48 | 39 % → 2 % | 295.2 px | 0.21 | 0.06 | 809 |
| stroke 49 | 43 % → 2 % | 234.9 px | 0.21 | 0.05 | 872 |
| stroke 50 | 49 % → 2 % | 240.2 px | 0.21 | 0.04 | 771 |
| stroke 51 | 4 % → 0 % | 104.9 px | 0.00 | 0.00 | 122 |
| stroke 52 | 11 % → 0 % | 112.5 px | 0.22 | 0.03 | 348 |
| stroke 53 | 16 % → 1 % | 151.5 px | 0.22 | 0.07 | 403 |
| stroke 54 | 21 % → 2 % | 224.4 px | 0.22 | 0.08 | 521 |
| stroke 55 | 26 % → 2 % | 249.0 px | 0.22 | 0.07 | 424 |
| stroke 56 | 32 % → 2 % | 546.3 px | 0.22 | 0.06 | 157 |
| stroke 57 | 32 % → 2 % | 520.6 px | 0.22 | 0.07 | 200 |
| stroke 58 | 16 % → 2 % | 253.6 px | 0.22 | 0.14 | 229 |
| stroke 59 | 17 % → 2 % | 191.4 px | 0.22 | 0.14 | 347 |
| stroke 60 | 22 % → 2 % | 220.9 px | 0.22 | 0.10 | 319 |
| stroke 61 | 26 % → 1 % | 327.0 px | 0.21 | 0.05 | 132 |
| stroke 62 | 2 % → 2 % | 26.2 px | 0.22 | 1.21 | 53 |
| stroke 63 | 1 % → 2 % | 34.9 px | 0.22 | 1.11 | 64 |
| stroke 64 | 1 % → 2 % | 27.5 px | 0.20 | 1.45 | 11 |

Numbers say: wet paint spreads well beyond the stroke.

## Refs v3 · #11 HW purple balls — own sheet
own sheet 800 × 985 · Gouache 1.00 + turpentine 30 % · 104 px · 58.9 s

![Refs v3 · #11 HW purple balls — own sheet](Refs-v3-11-HW-purple-balls-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 13 % → 0 % | 72.7 px | 0.00 | 0.00 | 392 |
| stroke 2 | 20 % → 0 % | 107.9 px | 0.00 | 0.00 | 731 |
| stroke 3 | 26 % → 0 % | 128.3 px | 0.00 | 0.00 | 1065 |
| stroke 4 | 31 % → 0 % | 158.8 px | 0.00 | 0.00 | 1023 |
| stroke 5 | 37 % → 0 % | 193.5 px | 0.00 | 0.00 | 1400 |
| stroke 6 | 41 % → 0 % | 229.9 px | 0.00 | 0.00 | 1953 |
| stroke 7 | 46 % → 0 % | 241.9 px | 0.00 | 0.00 | 1446 |
| stroke 8 | 49 % → 0 % | 251.3 px | 0.00 | 0.00 | 1756 |
| stroke 9 | 52 % → 0 % | 247.4 px | 0.00 | 0.00 | 1131 |
| stroke 10 | 54 % → 0 % | 246.3 px | 0.00 | 0.00 | 1388 |
| stroke 11 | 56 % → 0 % | 251.5 px | 0.00 | 0.00 | 1276 |
| stroke 12 | 56 % → 0 % | 294.4 px | 0.00 | 0.00 | 1482 |
| stroke 13 | 56 % → 1 % | 296.3 px | 0.68 | 0.01 | 1264 |
| stroke 14 | 55 % → 3 % | 290.5 px | 0.67 | 0.05 | 1201 |
| stroke 15 | 53 % → 6 % | 400.3 px | 0.67 | 0.12 | 766 |
| stroke 16 | 50 % → 12 % | 334.4 px | 0.67 | 0.23 | 1190 |
| stroke 17 | 48 % → 23 % | 410.3 px | 0.67 | 0.48 | 693 |
| stroke 18 | 54 % → 19 % | 511.7 px | 0.67 | 0.35 | 792 |
| stroke 19 | 48 % → 31 % | 409.5 px | 0.67 | 0.65 | 790 |
| stroke 20 | 55 % → 25 % | 472.2 px | 0.67 | 0.47 | 446 |
| stroke 21 | 43 % → 41 % | 630.6 px | 0.67 | 0.95 | 201 |
| stroke 22 | 49 % → 30 % | 427.6 px | 0.67 | 0.61 | 445 |
| stroke 23 | 45 % → 33 % | 458.6 px | 0.67 | 0.73 | 435 |
| stroke 24 | 0 % → 24 % | 28.6 px | 0.67 | 75.13 | 4 |
| stroke 25 | 1 % → 26 % | 46.1 px | 0.67 | 35.40 | 9 |
| stroke 26 | 1 % → 28 % | 67.3 px | 0.67 | 27.59 | 8 |
| stroke 27 | 1 % → 29 % | 64.8 px | 0.67 | 21.76 | 17 |
| stroke 28 | 2 % → 31 % | 79.4 px | 0.67 | 19.24 | 28 |
| stroke 29 | 2 % → 32 % | 81.4 px | 0.67 | 15.83 | 36 |
| stroke 30 | 2 % → 34 % | 118.8 px | 0.67 | 14.28 | 27 |
| stroke 31 | 3 % → 38 % | 174.9 px | 0.67 | 13.92 | 9 |
| stroke 32 | 3 % → 39 % | 189.7 px | 0.67 | 13.34 | 49 |
| stroke 33 | 3 % → 42 % | 209.6 px | 0.67 | 12.96 | 12 |
| stroke 34 | 4 % → 44 % | 301.9 px | 0.67 | 12.54 | 4 |
| stroke 35 | 1 % → 0 % | 26.1 px | 0.00 | 0.00 | 16 |
| stroke 36 | 1 % → 13 % | 28.2 px | 0.66 | 9.14 | 33 |
| stroke 37 | 1 % → 44 % | 45.6 px | 0.67 | 33.08 | 8 |
| stroke 38 | 1 % → 36 % | 19.6 px | 0.67 | 51.36 | 13 |
| stroke 39 | 2 % → 48 % | 44.9 px | 0.67 | 28.29 | 5 |
| stroke 40 | 3 % → 79 % | 18.3 px | 0.67 | 22.57 | 45 |
| stroke 41 | 4 % → 90 % | 82.5 px | 0.67 | 23.95 | 10 |
| stroke 42 | 6 % → 45 % | 100.0 px | 0.67 | 7.72 | 236 |
| stroke 43 | 10 % → 47 % | 128.9 px | 0.67 | 4.85 | 351 |
| stroke 44 | 18 % → 44 % | 128.8 px | 0.67 | 2.38 | 1038 |
| stroke 45 | 28 % → 45 % | 154.8 px | 0.67 | 1.60 | 1100 |
| stroke 46 | 42 % → 51 % | 186.3 px | 0.67 | 1.23 | 1310 |
| stroke 47 | 56 % → 56 % | 221.4 px | 0.67 | 1.00 | 1083 |
| stroke 48 | 89 % → 88 % | 1289.7 px | 0.67 | 0.99 | 105 |
| stroke 49 | 65 % → 65 % | 491.6 px | 0.67 | 0.99 | 252 |

Numbers say: wet paint spreads well beyond the stroke.

## Refs v3 · #12 HW black-olive cage — own sheet
own sheet 800 × 1150 · Gouache 1.00 + turpentine 30 % · 36 px · 120.3 s

![Refs v3 · #12 HW black-olive cage — own sheet](Refs-v3-12-HW-black-olive-cage-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 12 % → 11 % | 34.9 px | 0.30 | 0.93 | 36 |
| stroke 2 | 22 % → 9 % | 39.0 px | 0.30 | 0.40 | 139 |
| stroke 3 | 28 % → 6 % | 47.2 px | 0.30 | 0.23 | 265 |
| stroke 4 | 7 % → 1 % | 36.7 px | 0.30 | 0.10 | 58 |
| stroke 5 | 11 % → 0 % | 52.4 px | 0.30 | 0.03 | 66 |
| stroke 6 | 13 % → 1 % | 60.8 px | 0.30 | 0.08 | 82 |
| stroke 7 | 20 % → 2 % | 105.5 px | 0.29 | 0.12 | 85 |
| stroke 8 | 28 % → 0 % | 281.4 px | 0.00 | 0.00 | 28 |
| stroke 9 | 23 % → 1 % | 112.8 px | 0.30 | 0.05 | 68 |
| stroke 10 | 23 % → 1 % | 101.9 px | 0.30 | 0.05 | 190 |
| stroke 11 | 23 % → 3 % | 120.5 px | 0.29 | 0.11 | 68 |
| stroke 12 | 22 % → 1 % | 173.0 px | 0.30 | 0.07 | 16 |
| stroke 13 | 7 % → 3 % | 36.1 px | 0.28 | 0.49 | 25 |
| stroke 14 | 10 % → 6 % | 56.5 px | 0.29 | 0.59 | 18 |
| stroke 15 | 9 % → 3 % | 36.9 px | 0.30 | 0.29 | 20 |
| stroke 16 | 4 % → 0 % | 40.6 px | 0.00 | 0.00 | 7 |
| stroke 17 | 18 % → 15 % | 39.9 px | 0.31 | 0.85 | 76 |
| stroke 18 | 15 % → 22 % | 92.6 px | 0.31 | 1.47 | 10 |
| stroke 19 | 26 % → 10 % | 90.1 px | 0.31 | 0.40 | 32 |
| stroke 20 | 35 % → 18 % | 102.2 px | 0.31 | 0.52 | 44 |
| stroke 21 | 42 % → 19 % | 77.1 px | 0.31 | 0.45 | 91 |
| stroke 22 | 51 % → 15 % | 358.2 px | 0.30 | 0.29 | 9 |
| stroke 23 | 13 % → 0 % | 35.1 px | 0.00 | 0.00 | 181 |
| stroke 24 | 19 % → 0 % | 43.8 px | 0.00 | 0.00 | 226 |
| stroke 25 | 28 % → 0 % | 69.0 px | 0.00 | 0.00 | 127 |
| stroke 26 | 6 % → 0 % | 35.8 px | 0.00 | 0.00 | 24 |
| stroke 27 | 10 % → 0 % | 41.3 px | 0.00 | 0.00 | 96 |
| stroke 28 | 16 % → 0 % | 103.1 px | 0.00 | 0.00 | 25 |
| stroke 29 | 20 % → 0 % | 101.9 px | 0.00 | 0.00 | 36 |
| stroke 30 | 14 % → 0 % | 116.1 px | 0.00 | 0.00 | 11 |
| stroke 31 | 14 % → 0 % | 151.7 px | 0.00 | 0.00 | 6 |
| stroke 32 | 4 % → 0 % | 38.3 px | 0.00 | 0.00 | 8 |
| stroke 33 | 8 % → 0 % | 48.8 px | 0.00 | 0.00 | 30 |
| stroke 34 | 11 % → 0 % | 60.7 px | 0.00 | 0.00 | 35 |
| stroke 35 | 15 % → 0 % | 112.1 px | 0.00 | 0.00 | 22 |
| stroke 36 | 19 % → 0 % | 178.4 px | 0.00 | 0.00 | 13 |
| stroke 37 | 20 % → 0 % | 145.4 px | 0.00 | 0.00 | 21 |
| stroke 38 | 22 % → 0 % | 140.5 px | 0.00 | 0.00 | 24 |
| stroke 39 | 25 % → 0 % | 102.9 px | 0.00 | 0.00 | 60 |
| stroke 40 | 25 % → 0 % | 111.0 px | 0.00 | 0.00 | 33 |
| stroke 41 | 32 % → 0 % | 112.3 px | 0.00 | 0.00 | 69 |
| stroke 42 | 30 % → 0 % | 75.5 px | 0.00 | 0.00 | 238 |
| stroke 43 | 36 % → 0 % | 79.3 px | 0.00 | 0.00 | 376 |
| stroke 44 | 45 % → 0 % | 93.0 px | 0.00 | 0.00 | 151 |
| stroke 45 | 67 % → 0 % | 142.5 px | 0.00 | 0.00 | 94 |
| stroke 46 | 88 % → 0 % | 387.5 px | 0.00 | 0.00 | 20 |
| stroke 47 | 4 % → 0 % | 41.6 px | 0.00 | 0.00 | 6 |
| stroke 48 | 8 % → 0 % | 65.3 px | 0.00 | 0.00 | 17 |
| stroke 49 | 4 % → 0 % | 42.4 px | 0.00 | 0.00 | 6 |
| stroke 50 | 8 % → 0 % | 58.8 px | 0.00 | 0.00 | 11 |
| stroke 51 | 20 % → 0 % | 46.9 px | 0.00 | 0.00 | 102 |
| stroke 52 | 33 % → 0 % | 63.4 px | 0.00 | 0.00 | 41 |
| stroke 53 | 5 % → 0 % | 15.5 px | 0.00 | 0.00 | 19 |
| stroke 54 | 6 % → 0 % | 16.9 px | 0.00 | 0.00 | 9 |
| stroke 55 | 4 % → 0 % | 20.7 px | 0.27 | 0.09 | 9 |
| stroke 56 | 3 % → 17 % | 16.3 px | 0.32 | 6.02 | 17 |
| stroke 57 | 4 % → 2 % | 20.4 px | 0.29 | 0.50 | 26 |
| stroke 58 | 4 % → 4 % | 24.7 px | 0.33 | 1.14 | 11 |
| stroke 59 | 7 % → 4 % | 66.3 px | 0.33 | 0.48 | 13 |
| stroke 60 | 4 % → 0 % | 17.3 px | 0.00 | 0.00 | 10 |
| stroke 61 | 10 % → 0 % | 42.4 px | 0.00 | 0.00 | 27 |
| stroke 62 | 16 % → 0 % | 46.5 px | 0.00 | 0.00 | 24 |
| stroke 63 | 7 % → 0 % | 29.1 px | 0.00 | 0.00 | 64 |
| stroke 64 | 5 % → 0 % | 26.1 px | 0.00 | 0.00 | 24 |
| stroke 65 | 6 % → 0 % | 34.3 px | 0.00 | 0.00 | 23 |
| stroke 66 | 9 % → 0 % | 70.7 px | 0.00 | 0.00 | 19 |
| stroke 67 | 14 % → 0 % | 50.7 px | 0.00 | 0.00 | 43 |
| stroke 68 | 6 % → 0 % | 35.4 px | 0.00 | 0.00 | 34 |
| stroke 69 | 9 % → 0 % | 51.2 px | 0.00 | 0.00 | 31 |
| stroke 70 | 12 % → 0 % | 63.4 px | 0.00 | 0.00 | 49 |
| stroke 71 | 10 % → 0 % | 33.1 px | 0.00 | 0.00 | 74 |
| stroke 72 | 3 % → 5 % | 30.8 px | 0.30 | 2.00 | 7 |
| stroke 73 | 9 % → 10 % | 31.8 px | 0.30 | 1.16 | 61 |
| stroke 74 | 4 % → 1 % | 29.0 px | 0.27 | 0.23 | 19 |
| stroke 75 | 16 % → 7 % | 43.0 px | 0.30 | 0.42 | 129 |
| stroke 76 | 19 % → 7 % | 52.1 px | 0.30 | 0.35 | 148 |
| stroke 77 | 27 % → 13 % | 375.7 px | 0.30 | 0.49 | 7 |
| stroke 78 | 27 % → 10 % | 194.3 px | 0.30 | 0.37 | 35 |
| stroke 79 | 29 % → 7 % | 174.5 px | 0.29 | 0.26 | 34 |
| stroke 80 | 28 % → 3 % | 125.2 px | 0.29 | 0.12 | 82 |
| stroke 81 | 24 % → 0 % | 149.8 px | 0.30 | 0.00 | 46 |
| stroke 82 | 23 % → 0 % | 100.9 px | 0.00 | 0.00 | 28 |
| stroke 83 | 21 % → 0 % | 151.7 px | 0.00 | 0.00 | 16 |
| stroke 84 | 21 % → 0 % | 195.8 px | 0.00 | 0.00 | 48 |
| stroke 85 | 22 % → 0 % | 203.7 px | 0.00 | 0.00 | 20 |
| stroke 86 | 23 % → 0 % | 166.8 px | 0.00 | 0.00 | 46 |
| stroke 87 | 22 % → 0 % | 210.6 px | 0.00 | 0.00 | 13 |
| stroke 88 | 21 % → 0 % | 199.2 px | 0.00 | 0.00 | 11 |
| stroke 89 | 20 % → 0 % | 253.5 px | 0.00 | 0.00 | 7 |
| stroke 90 | 17 % → 0 % | 162.7 px | 0.00 | 0.00 | 12 |
| stroke 91 | 3 % → 0 % | 30.2 px | 0.00 | 0.00 | 16 |
| stroke 92 | 7 % → 0 % | 34.6 px | 0.00 | 0.00 | 27 |
| stroke 93 | 10 % → 0 % | 53.1 px | 0.00 | 0.00 | 32 |
| stroke 94 | 2 % → 0 % | 30.2 px | 0.27 | 0.01 | 4 |
| stroke 95 | 5 % → 0 % | 51.1 px | 0.27 | 0.06 | 15 |
| stroke 96 | 9 % → 0 % | 70.6 px | 0.00 | 0.00 | 15 |
| stroke 97 | 10 % → 0 % | 72.1 px | 0.00 | 0.00 | 24 |
| stroke 98 | 13 % → 0 % | 103.9 px | 0.00 | 0.00 | 48 |
| stroke 99 | 13 % → 0 % | 91.8 px | 0.31 | 0.01 | 38 |
| stroke 100 | 6 % → 13 % | 51.1 px | 0.31 | 2.14 | 14 |
| stroke 101 | 19 % → 0 % | 150.3 px | 0.32 | 0.02 | 13 |
| stroke 102 | 19 % → 10 % | 117.5 px | 0.31 | 0.53 | 29 |
| stroke 103 | 22 % → 5 % | 96.8 px | 0.31 | 0.22 | 44 |
| stroke 104 | 29 % → 1 % | 235.8 px | 0.32 | 0.02 | 11 |
| stroke 105 | 11 % → 0 % | 76.0 px | 0.00 | 0.00 | 10 |
| stroke 106 | 12 % → 0 % | 61.0 px | 0.00 | 0.00 | 19 |
| stroke 107 | 12 % → 0 % | 122.7 px | 0.00 | 0.00 | 6 |
| stroke 108 | 20 % → 0 % | 184.3 px | 0.00 | 0.00 | 31 |
| stroke 109 | 3 % → 0 % | 31.2 px | 0.00 | 0.00 | 5 |
| stroke 110 | 9 % → 0 % | 56.4 px | 0.00 | 0.00 | 48 |
| stroke 111 | 16 % → 0 % | 112.6 px | 0.00 | 0.00 | 29 |
| stroke 112 | 21 % → 0 % | 119.9 px | 0.00 | 0.00 | 40 |
| stroke 113 | 29 % → 0 % | 352.5 px | 0.00 | 0.00 | 10 |
| stroke 114 | 9 % → 0 % | 29.0 px | 0.00 | 0.00 | 71 |
| stroke 115 | 14 % → 0 % | 35.4 px | 0.00 | 0.00 | 113 |
| stroke 116 | 18 % → 0 % | 40.9 px | 0.00 | 0.00 | 163 |
| stroke 117 | 20 % → 0 % | 79.3 px | 0.00 | 0.00 | 61 |
| stroke 118 | 33 % → 0 % | 136.4 px | 0.00 | 0.00 | 56 |
| stroke 119 | 21 % → 0 % | 63.7 px | 0.00 | 0.00 | 59 |
| stroke 120 | 18 % → 0 % | 127.4 px | 0.00 | 0.00 | 26 |
| stroke 121 | 19 % → 0 % | 69.4 px | 0.00 | 0.00 | 119 |
| stroke 122 | 15 % → 0 % | 211.0 px | 0.00 | 0.00 | 18 |
| stroke 123 | 17 % → 0 % | 76.5 px | 0.00 | 0.00 | 29 |
| stroke 124 | 20 % → 0 % | 76.3 px | 0.00 | 0.00 | 63 |
| stroke 125 | 15 % → 0 % | 181.1 px | 0.00 | 0.00 | 4 |
| stroke 126 | 25 % → 0 % | 75.4 px | 0.00 | 0.00 | 52 |
| stroke 127 | 15 % → 0 % | 192.0 px | 0.00 | 0.00 | 11 |
| stroke 128 | 37 % → 0 % | 278.2 px | 0.00 | 0.00 | 25 |
| stroke 129 | 25 % → 0 % | 117.3 px | 0.00 | 0.00 | 45 |
| stroke 130 | 25 % → 0 % | 159.1 px | 0.00 | 0.00 | 46 |
| stroke 131 | 12 % → 0 % | 164.0 px | 0.00 | 0.00 | 9 |
| stroke 132 | 13 % → 0 % | 173.7 px | 0.00 | 0.00 | 7 |
| stroke 133 | 13 % → 0 % | 115.7 px | 0.00 | 0.00 | 11 |
| stroke 134 | 13 % → 0 % | 123.3 px | 0.00 | 0.00 | 13 |
| stroke 135 | 13 % → 0 % | 165.4 px | 0.00 | 0.00 | 7 |
| stroke 136 | 14 % → 0 % | 124.0 px | 0.00 | 0.00 | 16 |
| stroke 137 | 16 % → 0 % | 197.5 px | 0.00 | 0.00 | 5 |
| stroke 138 | 18 % → 0 % | 151.9 px | 0.00 | 0.00 | 9 |
| stroke 139 | 18 % → 0 % | 192.8 px | 0.00 | 0.00 | 7 |
| stroke 140 | 19 % → 0 % | 151.8 px | 0.00 | 0.00 | 9 |
| stroke 141 | 20 % → 0 % | 155.3 px | 0.00 | 0.00 | 7 |
| stroke 142 | 20 % → 0 % | 197.7 px | 0.00 | 0.00 | 6 |
| stroke 143 | 20 % → 0 % | 147.1 px | 0.00 | 0.00 | 7 |
| stroke 144 | 22 % → 0 % | 222.6 px | 0.00 | 0.00 | 7 |
| stroke 145 | 22 % → 0 % | 180.0 px | 0.00 | 0.00 | 13 |
| stroke 146 | 23 % → 0 % | 202.6 px | 0.00 | 0.00 | 11 |
| stroke 147 | 22 % → 0 % | 189.7 px | 0.00 | 0.00 | 8 |
| stroke 148 | 9 % → 0 % | 70.5 px | 0.00 | 0.00 | 8 |
| stroke 149 | 9 % → 0 % | 77.7 px | 0.00 | 0.00 | 6 |
| stroke 150 | 10 % → 0 % | 90.6 px | 0.00 | 0.00 | 5 |
| stroke 151 | 13 % → 0 % | 96.9 px | 0.00 | 0.00 | 7 |
| stroke 152 | 9 % → 12 % | 44.7 px | 0.31 | 1.29 | 21 |
| stroke 153 | 13 % → 11 % | 65.2 px | 0.31 | 0.85 | 46 |
| stroke 154 | 18 % → 16 % | 183.4 px | 0.31 | 0.84 | 15 |
| stroke 155 | 22 % → 15 % | 214.7 px | 0.31 | 0.66 | 11 |
| stroke 156 | 3 % → 1 % | 28.7 px | 0.28 | 0.44 | 7 |
| stroke 157 | 4 % → 0 % | 27.0 px | 0.00 | 0.00 | 21 |
| stroke 158 | 4 % → 0 % | 46.0 px | 0.00 | 0.00 | 6 |
| stroke 159 | 3 % → 5 % | 22.2 px | 0.31 | 1.64 | 14 |
| stroke 160 | 4 % → 0 % | 23.4 px | 0.00 | 0.00 | 22 |
| stroke 161 | 10 % → 0 % | 43.1 px | 0.00 | 0.00 | 36 |
| stroke 162 | 6 % → 17 % | 23.3 px | 0.31 | 2.97 | 13 |
| stroke 163 | 11 % → 3 % | 44.0 px | 0.31 | 0.31 | 64 |
| stroke 164 | 4 % → 0 % | 24.6 px | 0.00 | 0.00 | 22 |
| stroke 165 | 4 % → 0 % | 23.5 px | 0.00 | 0.00 | 20 |
| stroke 166 | 8 % → 0 % | 49.5 px | 0.00 | 0.00 | 26 |
| stroke 167 | 3 % → 0 % | 23.3 px | 0.00 | 0.00 | 16 |
| stroke 168 | 15 % → 0 % | 63.0 px | 0.00 | 0.00 | 73 |
| stroke 169 | 23 % → 0 % | 76.8 px | 0.00 | 0.00 | 102 |
| stroke 170 | 29 % → 0 % | 91.8 px | 0.00 | 0.00 | 138 |
| stroke 171 | 31 % → 0 % | 105.8 px | 0.00 | 0.00 | 264 |
| stroke 172 | 31 % → 0 % | 191.7 px | 0.00 | 0.00 | 107 |
| stroke 173 | 27 % → 0 % | 171.6 px | 0.00 | 0.00 | 52 |
| stroke 174 | 25 % → 0 % | 142.9 px | 0.00 | 0.00 | 82 |
| stroke 175 | 28 % → 0 % | 174.7 px | 0.00 | 0.00 | 112 |
| stroke 176 | 26 % → 0 % | 184.3 px | 0.00 | 0.00 | 123 |
| stroke 177 | 16 % → 0 % | 62.6 px | 0.35 | 0.01 | 114 |
| stroke 178 | 26 % → 0 % | 148.2 px | 0.00 | 0.00 | 60 |
| stroke 179 | 23 % → 5 % | 76.8 px | 0.33 | 0.22 | 72 |
| stroke 180 | 24 % → 0 % | 112.3 px | 0.00 | 0.00 | 141 |
| stroke 181 | 29 % → 7 % | 89.0 px | 0.31 | 0.25 | 239 |
| stroke 182 | 29 % → 0 % | 135.5 px | 0.00 | 0.00 | 450 |
| stroke 183 | 33 % → 7 % | 106.5 px | 0.31 | 0.22 | 486 |
| stroke 184 | 37 % → 0 % | 294.6 px | 0.00 | 0.00 | 51 |
| stroke 185 | 33 % → 9 % | 114.0 px | 0.31 | 0.27 | 339 |
| stroke 186 | 34 % → 2 % | 153.0 px | 0.30 | 0.07 | 155 |
| stroke 187 | 29 % → 4 % | 130.3 px | 0.30 | 0.13 | 457 |
| stroke 188 | 35 % → 5 % | 148.4 px | 0.30 | 0.15 | 239 |
| stroke 189 | 42 % → 6 % | 197.0 px | 0.30 | 0.15 | 96 |
| stroke 190 | 44 % → 4 % | 240.9 px | 0.29 | 0.08 | 64 |
| stroke 191 | 42 % → 1 % | 331.0 px | 0.28 | 0.01 | 29 |
| stroke 192 | 16 % → 2 % | 64.1 px | 0.29 | 0.16 | 55 |
| stroke 193 | 26 % → 1 % | 89.6 px | 0.28 | 0.05 | 102 |
| stroke 194 | 44 % → 0 % | 207.0 px | 0.00 | 0.00 | 27 |
| stroke 195 | 14 % → 3 % | 66.5 px | 0.30 | 0.19 | 52 |
| stroke 196 | 20 % → 4 % | 90.5 px | 0.30 | 0.19 | 104 |
| stroke 197 | 28 % → 4 % | 127.3 px | 0.30 | 0.13 | 95 |
| stroke 198 | 5 % → 13 % | 39.3 px | 0.31 | 2.43 | 18 |
| stroke 199 | 10 % → 11 % | 69.2 px | 0.31 | 1.11 | 27 |
| stroke 200 | 13 % → 11 % | 99.8 px | 0.30 | 0.89 | 18 |
| stroke 201 | 4 % → 0 % | 38.3 px | 0.00 | 0.00 | 21 |
| stroke 202 | 7 % → 0 % | 46.9 px | 0.00 | 0.00 | 31 |
| stroke 203 | 11 % → 4 % | 66.5 px | 0.30 | 0.32 | 46 |
| stroke 204 | 12 % → 5 % | 50.9 px | 0.30 | 0.45 | 149 |
| stroke 205 | 17 % → 13 % | 140.2 px | 0.30 | 0.77 | 25 |
| stroke 206 | 29 % → 9 % | 353.3 px | 0.32 | 0.32 | 11 |
| stroke 207 | 28 % → 9 % | 360.1 px | 0.32 | 0.33 | 8 |
| stroke 208 | 6 % → 0 % | 37.2 px | 0.00 | 0.00 | 25 |
| stroke 209 | 12 % → 0 % | 49.5 px | 0.00 | 0.00 | 62 |
| stroke 210 | 16 % → 0 % | 59.9 px | 0.00 | 0.00 | 62 |
| stroke 211 | 17 % → 7 % | 67.8 px | 0.32 | 0.45 | 117 |
| stroke 212 | 11 % → 13 % | 81.6 px | 0.31 | 1.27 | 23 |
| stroke 213 | 3 % → 0 % | 38.9 px | 0.00 | 0.00 | 10 |
| stroke 214 | 20 % → 9 % | 72.4 px | 0.31 | 0.46 | 114 |
| stroke 215 | 12 % → 0 % | 46.1 px | 0.00 | 0.00 | 68 |
| stroke 216 | 32 % → 6 % | 123.0 px | 0.32 | 0.18 | 72 |
| stroke 217 | 22 % → 18 % | 293.4 px | 0.31 | 0.82 | 6 |
| stroke 218 | 18 % → 0 % | 141.0 px | 0.00 | 0.00 | 20 |
| stroke 219 | 22 % → 0 % | 104.9 px | 0.00 | 0.00 | 158 |
| stroke 220 | 41 % → 0 % | 218.5 px | 0.00 | 0.00 | 42 |
| stroke 221 | 27 % → 0 % | 257.3 px | 0.00 | 0.00 | 11 |
| stroke 222 | 20 % → 0 % | 155.6 px | 0.00 | 0.00 | 23 |
| stroke 223 | 42 % → 0 % | 227.9 px | 0.00 | 0.00 | 29 |
| stroke 224 | 28 % → 16 % | 271.7 px | 0.31 | 0.58 | 9 |
| stroke 225 | 21 % → 0 % | 163.4 px | 0.00 | 0.00 | 28 |
| stroke 226 | 38 % → 0 % | 250.8 px | 0.00 | 0.00 | 32 |
| stroke 227 | 22 % → 0 % | 204.6 px | 0.00 | 0.00 | 12 |
| stroke 228 | 22 % → 0 % | 212.5 px | 0.00 | 0.00 | 11 |
| stroke 229 | 20 % → 13 % | 234.1 px | 0.31 | 0.64 | 16 |
| stroke 230 | 25 % → 0 % | 122.7 px | 0.00 | 0.00 | 29 |
| stroke 231 | 24 % → 0 % | 127.9 px | 0.00 | 0.00 | 21 |
| stroke 232 | 23 % → 9 % | 153.2 px | 0.31 | 0.40 | 18 |
| stroke 233 | 25 % → 14 % | 269.5 px | 0.31 | 0.57 | 14 |
| stroke 234 | 29 % → 0 % | 98.7 px | 0.00 | 0.00 | 154 |
| stroke 235 | 29 % → 7 % | 119.2 px | 0.31 | 0.25 | 59 |
| stroke 236 | 36 % → 0 % | 146.0 px | 0.00 | 0.00 | 69 |
| stroke 237 | 35 % → 4 % | 121.2 px | 0.31 | 0.11 | 97 |
| stroke 238 | 42 % → 0 % | 272.1 px | 0.00 | 0.00 | 24 |
| stroke 239 | 41 % → 4 % | 239.5 px | 0.31 | 0.10 | 22 |
| stroke 240 | 35 % → 7 % | 310.9 px | 0.31 | 0.22 | 18 |
| stroke 241 | 42 % → 0 % | 394.7 px | 0.00 | 0.00 | 19 |
| stroke 242 | 38 % → 0 % | 518.1 px | 0.00 | 0.00 | 8 |
| stroke 243 | 37 % → 4 % | 152.1 px | 0.31 | 0.10 | 55 |
| stroke 244 | 43 % → 0 % | 176.4 px | 0.00 | 0.00 | 59 |
| stroke 245 | 42 % → 2 % | 199.5 px | 0.32 | 0.05 | 40 |
| stroke 246 | 44 % → 0 % | 593.0 px | 0.00 | 0.00 | 7 |
| stroke 247 | 49 % → 0 % | 215.6 px | 0.00 | 0.00 | 46 |
| stroke 248 | 51 % → 0 % | 487.7 px | 0.00 | 0.00 | 12 |
| stroke 249 | 6 % → 0 % | 86.9 px | 0.00 | 0.00 | 7 |
| stroke 250 | 8 % → 0 % | 59.8 px | 0.00 | 0.00 | 22 |
| stroke 251 | 11 % → 0 % | 61.0 px | 0.00 | 0.00 | 35 |
| stroke 252 | 14 % → 0 % | 80.1 px | 0.00 | 0.00 | 36 |
| stroke 253 | 18 % → 0 % | 112.4 px | 0.00 | 0.00 | 25 |
| stroke 254 | 3 % → 0 % | 39.2 px | 0.00 | 0.00 | 4 |
| stroke 255 | 16 % → 7 % | 217.3 px | 0.31 | 0.47 | 6 |
| stroke 256 | 8 % → 1 % | 106.1 px | 0.31 | 0.09 | 13 |
| stroke 257 | 18 % → 4 % | 80.1 px | 0.31 | 0.23 | 75 |
| stroke 258 | 6 % → 0 % | 55.1 px | 0.00 | 0.00 | 17 |
| stroke 259 | 23 % → 5 % | 127.3 px | 0.31 | 0.20 | 29 |
| stroke 260 | 20 % → 0 % | 90.6 px | 0.00 | 0.00 | 54 |
| stroke 261 | 34 % → 6 % | 226.1 px | 0.31 | 0.18 | 15 |
| stroke 262 | 29 % → 0 % | 149.9 px | 0.00 | 0.00 | 51 |
| stroke 263 | 36 % → 0 % | 213.8 px | 0.00 | 0.00 | 38 |
| stroke 264 | 39 % → 0 % | 199.2 px | 0.00 | 0.00 | 39 |
| stroke 265 | 45 % → 0 % | 541.9 px | 0.00 | 0.00 | 6 |
| stroke 266 | 3 % → 0 % | 43.1 px | 0.00 | 0.00 | 8 |
| stroke 267 | 10 % → 0 % | 41.9 px | 0.00 | 0.00 | 48 |
| stroke 268 | 15 % → 0 % | 86.5 px | 0.00 | 0.00 | 29 |
| stroke 269 | 20 % → 0 % | 153.3 px | 0.00 | 0.00 | 20 |
| stroke 270 | 11 % → 0 % | 36.3 px | 0.00 | 0.00 | 84 |
| stroke 271 | 8 % → 0 % | 52.3 px | 0.00 | 0.00 | 30 |
| stroke 272 | 18 % → 0 % | 43.5 px | 0.00 | 0.00 | 203 |
| stroke 273 | 26 % → 0 % | 61.0 px | 0.00 | 0.00 | 212 |
| stroke 274 | 28 % → 0 % | 128.5 px | 0.00 | 0.00 | 34 |
| stroke 275 | 41 % → 0 % | 302.4 px | 0.00 | 0.00 | 19 |
| stroke 276 | 41 % → 0 % | 225.0 px | 0.00 | 0.00 | 46 |
| stroke 277 | 28 % → 0 % | 175.5 px | 0.00 | 0.00 | 44 |
| stroke 278 | 26 % → 0 % | 190.2 px | 0.00 | 0.00 | 21 |
| stroke 279 | 43 % → 0 % | 564.9 px | 0.00 | 0.00 | 5 |
| stroke 280 | 32 % → 0 % | 402.0 px | 0.00 | 0.00 | 15 |
| stroke 281 | 28 % → 0 % | 210.4 px | 0.00 | 0.00 | 26 |
| stroke 282 | 37 % → 0 % | 231.2 px | 0.00 | 0.00 | 32 |
| stroke 283 | 26 % → 0 % | 352.2 px | 0.00 | 0.00 | 5 |
| stroke 284 | 36 % → 0 % | 222.8 px | 0.00 | 0.00 | 51 |
| stroke 285 | 36 % → 0 % | 200.2 px | 0.00 | 0.00 | 53 |
| stroke 286 | 35 % → 0 % | 435.0 px | 0.00 | 0.00 | 14 |
| stroke 287 | 40 % → 0 % | 377.3 px | 0.00 | 0.00 | 11 |
| stroke 288 | 50 % → 0 % | 270.1 px | 0.00 | 0.00 | 40 |
| stroke 289 | 26 % → 0 % | 194.9 px | 0.00 | 0.00 | 19 |
| stroke 290 | 49 % → 0 % | 181.5 px | 0.00 | 0.00 | 90 |
| stroke 291 | 28 % → 0 % | 120.6 px | 0.00 | 0.00 | 81 |
| stroke 292 | 38 % → 0 % | 190.0 px | 0.00 | 0.00 | 171 |
| stroke 293 | 28 % → 0 % | 387.1 px | 0.00 | 0.00 | 14 |
| stroke 294 | 41 % → 0 % | 186.3 px | 0.00 | 0.00 | 36 |
| stroke 295 | 38 % → 0 % | 272.1 px | 0.00 | 0.00 | 16 |
| stroke 296 | 8 % → 18 % | 21.9 px | 0.32 | 2.20 | 17 |
| stroke 297 | 4 % → 0 % | 16.9 px | 0.00 | 0.00 | 8 |
| stroke 298 | 6 % → 1 % | 55.1 px | 0.26 | 0.11 | 11 |
| stroke 299 | 6 % → 8 % | 26.7 px | 0.29 | 1.39 | 30 |
| stroke 300 | 12 % → 7 % | 99.6 px | 0.29 | 0.56 | 7 |
| stroke 301 | 4 % → 11 % | 30.1 px | 0.28 | 2.89 | 12 |
| stroke 302 | 5 % → 0 % | 30.4 px | 0.00 | 0.00 | 18 |
| stroke 303 | 3 % → 13 % | 34.1 px | 0.30 | 3.94 | 4 |
| stroke 304 | 3 % → 5 % | 24.8 px | 0.30 | 1.37 | 11 |
| stroke 305 | 4 % → 0 % | 23.5 px | 0.00 | 0.00 | 7 |
| stroke 306 | 5 % → 0 % | 31.3 px | 0.00 | 0.00 | 19 |
| stroke 307 | 2 % → 0 % | 22.3 px | 0.00 | 0.00 | 7 |
| stroke 308 | 9 % → 0 % | 48.9 px | 0.00 | 0.00 | 43 |
| stroke 309 | 2 % → 0 % | 23.0 px | 0.00 | 0.00 | 8 |
| stroke 310 | 11 % → 0 % | 54.2 px | 0.00 | 0.00 | 84 |
| stroke 311 | 19 % → 0 % | 86.5 px | 0.00 | 0.00 | 79 |
| stroke 312 | 14 % → 0 % | 66.6 px | 0.00 | 0.00 | 93 |
| stroke 313 | 18 % → 0 % | 67.1 px | 0.00 | 0.00 | 154 |
| stroke 314 | 9 % → 0 % | 69.0 px | 0.00 | 0.00 | 38 |
| stroke 315 | 12 % → 0 % | 66.3 px | 0.00 | 0.00 | 37 |
| stroke 316 | 40 % → 0 % | 94.9 px | 0.00 | 0.00 | 283 |
| stroke 317 | 18 % → 0 % | 109.7 px | 0.00 | 0.00 | 68 |
| stroke 318 | 28 % → 0 % | 202.0 px | 0.00 | 0.00 | 33 |
| stroke 319 | 54 % → 0 % | 258.3 px | 0.00 | 0.00 | 80 |
| stroke 320 | 25 % → 0 % | 183.5 px | 0.00 | 0.00 | 43 |
| stroke 321 | 42 % → 0 % | 202.6 px | 0.00 | 0.00 | 55 |
| stroke 322 | 53 % → 2 % | 109.1 px | 0.31 | 0.04 | 438 |
| stroke 323 | 33 % → 0 % | 165.2 px | 0.00 | 0.00 | 69 |
| stroke 324 | 61 % → 0 % | 123.6 px | 0.00 | 0.00 | 578 |
| stroke 325 | 54 % → 0 % | 173.6 px | 0.00 | 0.00 | 163 |
| stroke 326 | 53 % → 0 % | 161.2 px | 0.00 | 0.00 | 103 |
| stroke 327 | 51 % → 0 % | 137.5 px | 0.00 | 0.00 | 199 |
| stroke 328 | 48 % → 0 % | 127.5 px | 0.00 | 0.00 | 268 |
| stroke 329 | 38 % → 0 % | 111.0 px | 0.00 | 0.00 | 203 |
| stroke 330 | 51 % → 0 % | 110.5 px | 0.00 | 0.00 | 588 |
| stroke 331 | 26 % → 0 % | 106.9 px | 0.00 | 0.00 | 78 |
| stroke 332 | 53 % → 0 % | 104.8 px | 0.00 | 0.00 | 509 |
| stroke 333 | 59 % → 0 % | 142.1 px | 0.00 | 0.00 | 558 |
| stroke 334 | 46 % → 0 % | 152.7 px | 0.00 | 0.00 | 430 |
| stroke 335 | 56 % → 0 % | 150.8 px | 0.00 | 0.00 | 177 |
| stroke 336 | 48 % → 0 % | 200.6 px | 0.00 | 0.00 | 80 |
| stroke 337 | 53 % → 0 % | 127.6 px | 0.00 | 0.00 | 431 |
| stroke 338 | 46 % → 0 % | 246.2 px | 0.00 | 0.00 | 86 |
| stroke 339 | 47 % → 0 % | 116.3 px | 0.00 | 0.00 | 282 |
| stroke 340 | 35 % → 0 % | 256.9 px | 0.00 | 0.00 | 33 |
| stroke 341 | 36 % → 0 % | 111.5 px | 0.00 | 0.00 | 410 |
| stroke 342 | 53 % → 0 % | 247.4 px | 0.00 | 0.00 | 138 |
| stroke 343 | 7 % → 13 % | 27.9 px | 0.31 | 1.79 | 46 |
| stroke 344 | 9 % → 10 % | 25.7 px | 0.30 | 1.12 | 54 |
| stroke 345 | 7 % → 11 % | 68.6 px | 0.30 | 1.66 | 7 |
| stroke 346 | 5 % → 11 % | 31.4 px | 0.30 | 2.10 | 25 |
| stroke 347 | 9 % → 14 % | 64.3 px | 0.30 | 1.47 | 22 |
| stroke 348 | 9 % → 11 % | 27.6 px | 0.31 | 1.16 | 60 |

Numbers say: wet paint spreads well beyond the stroke.

## Refs v3 · #13 HW blue streaky form — own sheet
own sheet 800 × 1020 · Gouache 1.00 + turpentine 30 % · 104 px · 104.4 s

![Refs v3 · #13 HW blue streaky form — own sheet](Refs-v3-13-HW-blue-streaky-form-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 7 % → 33 % | 101.7 px | 0.47 | 4.47 | 225 |
| stroke 2 | 11 % → 37 % | 169.7 px | 0.47 | 3.21 | 202 |
| stroke 3 | 16 % → 29 % | 226.9 px | 0.47 | 1.77 | 255 |
| stroke 4 | 18 % → 33 % | 217.6 px | 0.47 | 1.89 | 819 |
| stroke 5 | 13 % → 25 % | 276.7 px | 0.47 | 1.90 | 156 |
| stroke 6 | 26 % → 22 % | 693.1 px | 0.47 | 0.87 | 114 |
| stroke 7 | 24 % → 22 % | 222.2 px | 0.47 | 0.92 | 547 |
| stroke 8 | 33 % → 18 % | 443.8 px | 0.47 | 0.53 | 271 |
| stroke 9 | 32 % → 15 % | 323.8 px | 0.46 | 0.47 | 394 |
| stroke 10 | 41 % → 12 % | 678.1 px | 0.47 | 0.30 | 137 |
| stroke 11 | 39 % → 11 % | 322.3 px | 0.46 | 0.29 | 698 |
| stroke 12 | 42 % → 5 % | 359.1 px | 0.47 | 0.13 | 508 |
| stroke 13 | 42 % → 0 % | 316.4 px | 0.46 | 0.00 | 953 |
| stroke 14 | 39 % → 0 % | 789.1 px | 0.00 | 0.00 | 146 |
| stroke 15 | 42 % → 0 % | 335.0 px | 0.00 | 0.00 | 752 |
| stroke 16 | 45 % → 0 % | 810.6 px | 0.00 | 0.00 | 176 |
| stroke 17 | 44 % → 0 % | 461.0 px | 0.00 | 0.00 | 955 |
| stroke 18 | 43 % → 0 % | 863.8 px | 0.00 | 0.00 | 173 |
| stroke 19 | 39 % → 0 % | 733.2 px | 0.00 | 0.00 | 106 |
| stroke 20 | 47 % → 0 % | 722.4 px | 0.00 | 0.00 | 321 |
| stroke 21 | 39 % → 0 % | 410.6 px | 0.00 | 0.00 | 483 |
| stroke 22 | 31 % → 0 % | 679.0 px | 0.00 | 0.00 | 153 |
| stroke 23 | 34 % → 0 % | 468.9 px | 0.00 | 0.00 | 573 |
| stroke 24 | 34 % → 0 % | 681.9 px | 0.00 | 0.00 | 168 |
| stroke 25 | 2 % → 19 % | 23.9 px | 0.47 | 11.79 | 58 |
| stroke 26 | 3 % → 3 % | 75.2 px | 0.45 | 1.30 | 25 |
| stroke 27 | 0 % → 0 % | 20.5 px | 0.00 | 0.00 | 8 |
| stroke 28 | 1 % → 33 % | 41.2 px | 0.47 | 23.52 | 24 |
| stroke 29 | 3 % → 34 % | 47.2 px | 0.47 | 12.96 | 71 |
| stroke 30 | 3 % → 33 % | 150.2 px | 0.47 | 9.61 | 35 |
| stroke 31 | 5 % → 26 % | 242.4 px | 0.47 | 4.84 | 21 |
| stroke 32 | 7 % → 10 % | 289.1 px | 0.46 | 1.50 | 24 |
| stroke 33 | 8 % → 9 % | 308.9 px | 0.45 | 1.20 | 15 |
| stroke 34 | 9 % → 8 % | 361.0 px | 0.45 | 0.94 | 17 |
| stroke 35 | 9 % → 7 % | 289.0 px | 0.45 | 0.72 | 17 |
| stroke 36 | 9 % → 5 % | 368.5 px | 0.45 | 0.49 | 29 |
| stroke 37 | 6 % → 0 % | 240.7 px | 0.46 | 0.06 | 19 |
| stroke 38 | 6 % → 0 % | 191.1 px | 0.00 | 0.00 | 25 |
| stroke 39 | 7 % → 0 % | 312.0 px | 0.00 | 0.00 | 20 |
| stroke 40 | 8 % → 0 % | 323.4 px | 0.00 | 0.00 | 11 |
| stroke 41 | 9 % → 0 % | 351.4 px | 0.00 | 0.00 | 19 |
| stroke 42 | 10 % → 0 % | 242.6 px | 0.00 | 0.00 | 22 |
| stroke 43 | 10 % → 0 % | 316.9 px | 0.00 | 0.00 | 16 |
| stroke 44 | 9 % → 0 % | 284.3 px | 0.00 | 0.00 | 17 |
| stroke 45 | 12 % → 0 % | 299.7 px | 0.00 | 0.00 | 29 |
| stroke 46 | 4 % → 0 % | 100.1 px | 0.00 | 0.00 | 35 |
| stroke 47 | 11 % → 0 % | 307.2 px | 0.00 | 0.00 | 25 |
| stroke 48 | 15 % → 0 % | 607.7 px | 0.00 | 0.00 | 19 |
| stroke 49 | 7 % → 0 % | 178.0 px | 0.00 | 0.00 | 55 |
| stroke 50 | 13 % → 0 % | 189.3 px | 0.00 | 0.00 | 87 |
| stroke 51 | 7 % → 0 % | 351.2 px | 0.00 | 0.00 | 45 |
| stroke 52 | 14 % → 0 % | 243.9 px | 0.00 | 0.00 | 76 |
| stroke 53 | 19 % → 0 % | 551.7 px | 0.00 | 0.00 | 41 |
| stroke 54 | 14 % → 0 % | 380.9 px | 0.00 | 0.00 | 49 |
| stroke 55 | 21 % → 0 % | 898.0 px | 0.00 | 0.00 | 13 |
| stroke 56 | 7 % → 29 % | 479.6 px | 0.47 | 3.87 | 10 |
| stroke 57 | 8 % → 26 % | 408.3 px | 0.47 | 3.19 | 15 |
| stroke 58 | 10 % → 22 % | 500.4 px | 0.47 | 2.18 | 24 |
| stroke 59 | 1 % → 32 % | 49.0 px | 0.47 | 42.67 | 12 |
| stroke 60 | 1 % → 27 % | 55.2 px | 0.47 | 19.82 | 32 |
| stroke 61 | 2 % → 26 % | 110.7 px | 0.47 | 14.70 | 36 |
| stroke 62 | 3 % → 24 % | 129.7 px | 0.47 | 8.89 | 32 |
| stroke 63 | 6 % → 0 % | 288.9 px | 0.00 | 0.00 | 49 |
| stroke 64 | 4 % → 0 % | 273.6 px | 0.00 | 0.00 | 23 |
| stroke 65 | 4 % → 0 % | 123.2 px | 0.00 | 0.00 | 38 |
| stroke 66 | 5 % → 0 % | 155.8 px | 0.00 | 0.00 | 41 |
| stroke 67 | 7 % → 0 % | 163.1 px | 0.00 | 0.00 | 33 |
| stroke 68 | 7 % → 0 % | 165.4 px | 0.00 | 0.00 | 40 |
| stroke 69 | 12 % → 0 % | 137.5 px | 0.00 | 0.00 | 149 |
| stroke 70 | 17 % → 0 % | 840.5 px | 0.00 | 0.00 | 38 |
| stroke 71 | 15 % → 0 % | 166.2 px | 0.00 | 0.00 | 163 |
| stroke 72 | 20 % → 0 % | 680.9 px | 0.00 | 0.00 | 43 |
| stroke 73 | 20 % → 0 % | 995.7 px | 0.00 | 0.00 | 16 |
| stroke 74 | 17 % → 0 % | 212.4 px | 0.00 | 0.00 | 363 |
| stroke 75 | 21 % → 0 % | 740.2 px | 0.00 | 0.00 | 25 |
| stroke 76 | 19 % → 0 % | 242.9 px | 0.00 | 0.00 | 159 |
| stroke 77 | 25 % → 0 % | 1491.8 px | 0.00 | 0.00 | 15 |
| stroke 78 | 23 % → 0 % | 757.9 px | 0.00 | 0.00 | 20 |
| stroke 79 | 22 % → 0 % | 481.5 px | 0.00 | 0.00 | 48 |
| stroke 80 | 29 % → 0 % | 515.0 px | 0.00 | 0.00 | 94 |
| stroke 81 | 25 % → 0 % | 583.7 px | 0.00 | 0.00 | 46 |
| stroke 82 | 23 % → 0 % | 1281.7 px | 0.00 | 0.00 | 34 |
| stroke 83 | 32 % → 0 % | 629.7 px | 0.00 | 0.00 | 237 |
| stroke 84 | 28 % → 0 % | 493.5 px | 0.00 | 0.00 | 35 |
| stroke 85 | 24 % → 0 % | 950.3 px | 0.00 | 0.00 | 17 |
| stroke 86 | 34 % → 0 % | 1838.6 px | 0.00 | 0.00 | 24 |
| stroke 87 | 27 % → 0 % | 593.1 px | 0.00 | 0.00 | 40 |
| stroke 88 | 28 % → 0 % | 462.1 px | 0.00 | 0.00 | 58 |
| stroke 89 | 26 % → 0 % | 637.2 px | 0.00 | 0.00 | 32 |
| stroke 90 | 30 % → 0 % | 457.4 px | 0.00 | 0.00 | 50 |
| stroke 91 | 25 % → 0 % | 593.0 px | 0.00 | 0.00 | 20 |
| stroke 92 | 31 % → 0 % | 518.2 px | 0.00 | 0.00 | 36 |
| stroke 93 | 35 % → 0 % | 754.7 px | 0.00 | 0.00 | 25 |
| stroke 94 | 27 % → 0 % | 643.9 px | 0.00 | 0.00 | 31 |
| stroke 95 | 35 % → 0 % | 345.7 px | 0.00 | 0.00 | 116 |
| stroke 96 | 40 % → 0 % | 381.7 px | 0.00 | 0.00 | 107 |
| stroke 97 | 29 % → 0 % | 593.3 px | 0.00 | 0.00 | 35 |
| stroke 98 | 38 % → 0 % | 224.2 px | 0.00 | 0.00 | 155 |
| stroke 99 | 43 % → 0 % | 1350.9 px | 0.00 | 0.00 | 14 |
| stroke 100 | 35 % → 0 % | 491.4 px | 0.00 | 0.00 | 61 |
| stroke 101 | 44 % → 0 % | 283.6 px | 0.00 | 0.00 | 137 |
| stroke 102 | 45 % → 0 % | 844.4 px | 0.00 | 0.00 | 44 |
| stroke 103 | 51 % → 0 % | 470.7 px | 0.00 | 0.00 | 86 |
| stroke 104 | 49 % → 0 % | 1437.9 px | 0.00 | 0.00 | 18 |
| stroke 105 | 26 % → 0 % | 1158.0 px | 0.00 | 0.00 | 13 |
| stroke 106 | 31 % → 0 % | 583.9 px | 0.00 | 0.00 | 23 |
| stroke 107 | 34 % → 0 % | 671.4 px | 0.00 | 0.00 | 58 |
| stroke 108 | 35 % → 0 % | 1123.3 px | 0.00 | 0.00 | 26 |
| stroke 109 | 1 % → 23 % | 28.1 px | 0.47 | 22.89 | 41 |
| stroke 110 | 1 % → 24 % | 31.0 px | 0.47 | 26.37 | 30 |
| stroke 111 | 1 % → 20 % | 54.3 px | 0.47 | 13.89 | 21 |
| stroke 112 | 2 % → 15 % | 96.2 px | 0.47 | 6.49 | 14 |
| stroke 113 | 3 % → 9 % | 64.7 px | 0.47 | 2.54 | 37 |
| stroke 114 | 2 % → 0 % | 105.1 px | 0.00 | 0.00 | 11 |
| stroke 115 | 4 % → 0 % | 114.5 px | 0.00 | 0.00 | 27 |
| stroke 116 | 4 % → 0 % | 135.7 px | 0.00 | 0.00 | 11 |
| stroke 117 | 4 % → 0 % | 210.5 px | 0.00 | 0.00 | 6 |
| stroke 118 | 5 % → 51 % | 65.3 px | 0.47 | 11.25 | 40 |
| stroke 119 | 7 % → 50 % | 103.2 px | 0.47 | 7.50 | 61 |
| stroke 120 | 9 % → 51 % | 129.6 px | 0.47 | 5.62 | 59 |
| stroke 121 | 10 % → 52 % | 143.8 px | 0.47 | 5.10 | 68 |
| stroke 122 | 12 % → 52 % | 162.9 px | 0.47 | 4.31 | 77 |
| stroke 123 | 13 % → 51 % | 164.6 px | 0.47 | 3.81 | 138 |
| stroke 124 | 15 % → 48 % | 188.0 px | 0.47 | 3.22 | 227 |
| stroke 125 | 16 % → 47 % | 188.2 px | 0.47 | 2.92 | 124 |
| stroke 126 | 18 % → 44 % | 228.5 px | 0.47 | 2.49 | 107 |
| stroke 127 | 20 % → 39 % | 319.5 px | 0.47 | 1.95 | 145 |
| stroke 128 | 21 % → 35 % | 336.8 px | 0.47 | 1.69 | 156 |
| stroke 129 | 3 % → 47 % | 66.2 px | 0.47 | 15.52 | 55 |
| stroke 130 | 5 % → 46 % | 80.0 px | 0.48 | 9.17 | 294 |
| stroke 131 | 6 % → 40 % | 182.0 px | 0.47 | 6.33 | 85 |
| stroke 132 | 8 % → 39 % | 225.0 px | 0.47 | 5.17 | 40 |
| stroke 133 | 9 % → 37 % | 269.3 px | 0.47 | 4.13 | 34 |
| stroke 134 | 10 % → 34 % | 309.8 px | 0.47 | 3.28 | 41 |
| stroke 135 | 2 % → 62 % | 64.5 px | 0.47 | 34.89 | 60 |
| stroke 136 | 3 % → 58 % | 80.2 px | 0.47 | 16.98 | 91 |
| stroke 137 | 5 % → 56 % | 105.2 px | 0.47 | 10.99 | 109 |
| stroke 138 | 6 % → 54 % | 166.5 px | 0.47 | 8.45 | 93 |
| stroke 139 | 8 % → 50 % | 205.9 px | 0.47 | 6.60 | 90 |
| stroke 140 | 9 % → 46 % | 239.2 px | 0.47 | 5.19 | 94 |
| stroke 141 | 15 % → 21 % | 434.8 px | 0.47 | 1.40 | 33 |
| stroke 142 | 14 % → 18 % | 355.6 px | 0.46 | 1.28 | 46 |
| stroke 143 | 13 % → 15 % | 335.7 px | 0.46 | 1.14 | 45 |
| stroke 144 | 12 % → 12 % | 369.6 px | 0.46 | 0.95 | 33 |
| stroke 145 | 11 % → 10 % | 278.8 px | 0.45 | 0.87 | 74 |
| stroke 146 | 11 % → 7 % | 277.9 px | 0.45 | 0.60 | 56 |
| stroke 147 | 11 % → 3 % | 335.2 px | 0.45 | 0.31 | 52 |
| stroke 148 | 12 % → 1 % | 320.4 px | 0.46 | 0.07 | 58 |
| stroke 149 | 14 % → 0 % | 356.9 px | 0.00 | 0.00 | 65 |
| stroke 150 | 14 % → 0 % | 322.8 px | 0.00 | 0.00 | 47 |
| stroke 151 | 14 % → 0 % | 316.6 px | 0.00 | 0.00 | 64 |
| stroke 152 | 10 % → 0 % | 255.3 px | 0.00 | 0.00 | 58 |
| stroke 153 | 10 % → 0 % | 209.2 px | 0.00 | 0.00 | 86 |
| stroke 154 | 10 % → 0 % | 281.2 px | 0.00 | 0.00 | 51 |
| stroke 155 | 11 % → 0 % | 246.2 px | 0.00 | 0.00 | 53 |
| stroke 156 | 14 % → 0 % | 170.1 px | 0.00 | 0.00 | 112 |
| stroke 157 | 18 % → 0 % | 165.9 px | 0.00 | 0.00 | 108 |
| stroke 158 | 20 % → 0 % | 165.1 px | 0.00 | 0.00 | 121 |
| stroke 159 | 17 % → 0 % | 584.2 px | 0.00 | 0.00 | 26 |
| stroke 160 | 17 % → 0 % | 345.3 px | 0.00 | 0.00 | 70 |
| stroke 161 | 5 % → 0 % | 61.9 px | 0.00 | 0.00 | 95 |
| stroke 162 | 9 % → 0 % | 95.4 px | 0.00 | 0.00 | 153 |
| stroke 163 | 12 % → 0 % | 118.2 px | 0.00 | 0.00 | 156 |
| stroke 164 | 17 % → 0 % | 177.8 px | 0.00 | 0.00 | 74 |
| stroke 165 | 22 % → 0 % | 273.7 px | 0.00 | 0.00 | 55 |
| stroke 166 | 27 % → 0 % | 302.5 px | 0.00 | 0.00 | 83 |
| stroke 167 | 31 % → 0 % | 274.2 px | 0.00 | 0.00 | 208 |
| stroke 168 | 6 % → 52 % | 37.7 px | 0.48 | 8.11 | 94 |
| stroke 169 | 10 % → 44 % | 246.4 px | 0.47 | 4.31 | 16 |
| stroke 170 | 8 % → 52 % | 114.0 px | 0.48 | 6.52 | 23 |
| stroke 171 | 12 % → 50 % | 176.4 px | 0.48 | 4.05 | 41 |
| stroke 172 | 10 % → 54 % | 136.3 px | 0.48 | 5.59 | 41 |
| stroke 173 | 15 % → 52 % | 227.4 px | 0.48 | 3.52 | 27 |
| stroke 174 | 12 % → 58 % | 122.7 px | 0.48 | 4.86 | 65 |
| stroke 175 | 19 % → 53 % | 302.9 px | 0.48 | 2.81 | 45 |
| stroke 176 | 16 % → 52 % | 628.2 px | 0.48 | 3.29 | 15 |
| stroke 177 | 15 % → 59 % | 523.3 px | 0.48 | 4.03 | 22 |
| stroke 178 | 20 % → 53 % | 346.6 px | 0.48 | 2.67 | 53 |
| stroke 179 | 17 % → 52 % | 752.0 px | 0.48 | 3.04 | 10 |
| stroke 180 | 16 % → 60 % | 777.3 px | 0.48 | 3.72 | 8 |
| stroke 181 | 22 % → 54 % | 469.8 px | 0.48 | 2.49 | 34 |
| stroke 182 | 18 % → 53 % | 1176.3 px | 0.48 | 2.96 | 8 |
| stroke 183 | 17 % → 63 % | 633.8 px | 0.48 | 3.78 | 19 |
| stroke 184 | 22 % → 52 % | 456.0 px | 0.48 | 2.33 | 36 |
| stroke 185 | 19 % → 53 % | 1332.1 px | 0.48 | 2.75 | 10 |
| stroke 186 | 18 % → 65 % | 482.0 px | 0.47 | 3.63 | 44 |
| stroke 187 | 24 % → 49 % | 617.6 px | 0.48 | 2.02 | 32 |
| stroke 188 | 20 % → 51 % | 1613.7 px | 0.48 | 2.50 | 8 |
| stroke 189 | 19 % → 63 % | 736.9 px | 0.47 | 3.35 | 19 |
| stroke 190 | 25 % → 48 % | 1643.3 px | 0.48 | 1.89 | 5 |
| stroke 191 | 19 % → 68 % | 169.3 px | 0.48 | 3.50 | 82 |
| stroke 192 | 22 % → 70 % | 321.4 px | 0.48 | 3.23 | 51 |
| stroke 193 | 13 % → 73 % | 720.1 px | 0.48 | 5.62 | 11 |
| stroke 194 | 24 % → 70 % | 344.5 px | 0.48 | 2.89 | 72 |
| stroke 195 | 27 % → 69 % | 1193.2 px | 0.48 | 2.55 | 17 |
| stroke 196 | 25 % → 70 % | 1661.4 px | 0.47 | 2.73 | 5 |
| stroke 197 | 19 % → 73 % | 1241.7 px | 0.47 | 3.93 | 6 |
| stroke 198 | 17 % → 73 % | 809.4 px | 0.47 | 4.25 | 14 |
| stroke 199 | 15 % → 73 % | 1098.1 px | 0.47 | 4.76 | 6 |
| stroke 200 | 9 % → 58 % | 249.1 px | 0.47 | 6.68 | 18 |
| stroke 201 | 9 % → 58 % | 226.8 px | 0.47 | 6.13 | 20 |
| stroke 202 | 10 % → 58 % | 262.0 px | 0.47 | 5.55 | 22 |
| stroke 203 | 11 % → 58 % | 357.7 px | 0.47 | 5.49 | 18 |
| stroke 204 | 11 % → 57 % | 493.3 px | 0.47 | 5.31 | 17 |
| stroke 205 | 12 % → 47 % | 470.0 px | 0.47 | 3.97 | 23 |
| stroke 206 | 13 % → 46 % | 371.5 px | 0.47 | 3.65 | 44 |
| stroke 207 | 12 % → 43 % | 290.0 px | 0.47 | 3.60 | 58 |
| stroke 208 | 12 % → 41 % | 247.4 px | 0.47 | 3.38 | 52 |
| stroke 209 | 12 % → 40 % | 265.4 px | 0.47 | 3.31 | 50 |
| stroke 210 | 25 % → 46 % | 2396.0 px | 0.48 | 1.82 | 5 |
| stroke 211 | 24 % → 44 % | 446.3 px | 0.48 | 1.82 | 57 |
| stroke 212 | 23 % → 43 % | 456.6 px | 0.48 | 1.84 | 64 |
| stroke 213 | 21 % → 41 % | 421.9 px | 0.48 | 1.91 | 56 |
| stroke 214 | 20 % → 39 % | 477.5 px | 0.47 | 1.97 | 62 |
| stroke 215 | 2 % → 55 % | 25.7 px | 0.47 | 32.57 | 25 |
| stroke 216 | 3 % → 53 % | 52.2 px | 0.47 | 18.18 | 20 |
| stroke 217 | 2 % → 60 % | 42.4 px | 0.47 | 38.65 | 29 |
| stroke 218 | 2 % → 35 % | 81.5 px | 0.47 | 20.15 | 17 |
| stroke 219 | 4 % → 62 % | 52.6 px | 0.48 | 15.39 | 52 |
| stroke 220 | 8 % → 58 % | 59.1 px | 0.48 | 7.18 | 118 |
| stroke 221 | 6 % → 64 % | 163.3 px | 0.48 | 9.97 | 34 |
| stroke 222 | 13 % → 59 % | 129.0 px | 0.48 | 4.61 | 117 |
| stroke 223 | 15 % → 58 % | 225.1 px | 0.47 | 3.83 | 39 |
| stroke 224 | 14 % → 70 % | 597.3 px | 0.48 | 4.83 | 21 |
| stroke 225 | 18 % → 66 % | 296.9 px | 0.48 | 3.64 | 108 |
| stroke 226 | 18 % → 57 % | 648.0 px | 0.47 | 3.16 | 23 |
| stroke 227 | 13 % → 68 % | 372.3 px | 0.47 | 5.24 | 34 |
| stroke 228 | 18 % → 71 % | 529.1 px | 0.47 | 3.97 | 34 |
| stroke 229 | 21 % → 65 % | 378.4 px | 0.47 | 3.03 | 56 |
| stroke 230 | 20 % → 57 % | 765.2 px | 0.47 | 2.90 | 15 |
| stroke 231 | 18 % → 72 % | 255.4 px | 0.47 | 3.90 | 86 |
| stroke 232 | 23 % → 59 % | 372.9 px | 0.47 | 2.56 | 131 |
| stroke 233 | 22 % → 57 % | 954.0 px | 0.47 | 2.58 | 19 |
| stroke 234 | 23 % → 70 % | 396.9 px | 0.47 | 2.97 | 131 |
| stroke 235 | 26 % → 56 % | 525.7 px | 0.47 | 2.14 | 92 |
| stroke 236 | 25 % → 56 % | 692.5 px | 0.47 | 2.20 | 35 |
| stroke 237 | 24 % → 65 % | 1012.8 px | 0.47 | 2.67 | 27 |
| stroke 238 | 28 % → 53 % | 274.6 px | 0.47 | 1.93 | 147 |
| stroke 239 | 28 % → 62 % | 1628.9 px | 0.47 | 2.21 | 19 |
| stroke 240 | 29 % → 50 % | 379.6 px | 0.47 | 1.73 | 125 |
| stroke 241 | 28 % → 48 % | 322.8 px | 0.47 | 1.73 | 269 |
| stroke 242 | 33 % → 54 % | 1118.6 px | 0.47 | 1.62 | 85 |
| stroke 243 | 32 % → 44 % | 1008.3 px | 0.47 | 1.39 | 41 |
| stroke 244 | 34 % → 53 % | 1007.3 px | 0.47 | 1.58 | 32 |
| stroke 245 | 33 % → 44 % | 989.5 px | 0.47 | 1.33 | 39 |
| stroke 246 | 32 % → 51 % | 937.8 px | 0.47 | 1.59 | 83 |
| stroke 247 | 33 % → 42 % | 1133.7 px | 0.47 | 1.27 | 51 |
| stroke 248 | 31 % → 48 % | 1051.3 px | 0.47 | 1.56 | 64 |
| stroke 249 | 32 % → 39 % | 843.3 px | 0.47 | 1.19 | 55 |
| stroke 250 | 26 % → 36 % | 318.1 px | 0.47 | 1.38 | 188 |
| stroke 251 | 26 % → 34 % | 417.9 px | 0.47 | 1.33 | 164 |
| stroke 252 | 19 % → 49 % | 226.1 px | 0.48 | 2.62 | 184 |
| stroke 253 | 17 % → 52 % | 714.3 px | 0.48 | 3.00 | 23 |
| stroke 254 | 18 % → 51 % | 845.4 px | 0.48 | 2.75 | 25 |
| stroke 255 | 20 % → 48 % | 721.8 px | 0.48 | 2.41 | 31 |
| stroke 256 | 31 % → 56 % | 1832.8 px | 0.48 | 1.79 | 11 |
| stroke 257 | 35 % → 52 % | 358.1 px | 0.48 | 1.49 | 271 |
| stroke 258 | 35 % → 49 % | 397.2 px | 0.48 | 1.40 | 221 |
| stroke 259 | 30 % → 43 % | 372.3 px | 0.48 | 1.44 | 265 |
| stroke 260 | 40 % → 52 % | 1947.4 px | 0.48 | 1.30 | 42 |
| stroke 261 | 27 % → 41 % | 660.0 px | 0.48 | 1.55 | 40 |
| stroke 262 | 41 % → 52 % | 2643.4 px | 0.48 | 1.26 | 21 |
| stroke 263 | 27 % → 39 % | 594.6 px | 0.48 | 1.45 | 66 |
| stroke 264 | 42 % → 51 % | 2018.9 px | 0.47 | 1.21 | 37 |
| stroke 265 | 27 % → 37 % | 587.0 px | 0.48 | 1.36 | 79 |
| stroke 266 | 40 % → 47 % | 1632.7 px | 0.47 | 1.17 | 31 |
| stroke 267 | 37 % → 40 % | 361.2 px | 0.47 | 1.07 | 276 |
| stroke 268 | 37 % → 37 % | 399.7 px | 0.47 | 1.01 | 484 |

Numbers say: wet paint spreads well beyond the stroke.

## Refs v3 · #14 HW olive totem — own sheet
own sheet 800 × 1040 · Gouache 1.00 + turpentine 30 % · 57 px · 71.3 s

![Refs v3 · #14 HW olive totem — own sheet](Refs-v3-14-HW-olive-totem-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 4 % → 0 % | 59.1 px | 0.00 | 0.00 | 84 |
| stroke 2 | 7 % → 0 % | 55.2 px | 0.00 | 0.00 | 106 |
| stroke 3 | 10 % → 0 % | 109.4 px | 0.00 | 0.00 | 83 |
| stroke 4 | 16 % → 0 % | 143.7 px | 0.00 | 0.00 | 124 |
| stroke 5 | 5 % → 0 % | 60.5 px | 0.00 | 0.00 | 29 |
| stroke 6 | 9 % → 0 % | 73.6 px | 0.00 | 0.00 | 48 |
| stroke 7 | 15 % → 0 % | 83.5 px | 0.00 | 0.00 | 154 |
| stroke 8 | 22 % → 1 % | 118.5 px | 0.23 | 0.05 | 136 |
| stroke 9 | 29 % → 4 % | 172.3 px | 0.21 | 0.15 | 110 |
| stroke 10 | 31 % → 5 % | 190.1 px | 0.21 | 0.15 | 65 |
| stroke 11 | 32 % → 4 % | 180.3 px | 0.21 | 0.14 | 91 |
| stroke 12 | 29 % → 3 % | 120.6 px | 0.21 | 0.12 | 205 |
| stroke 13 | 28 % → 3 % | 159.5 px | 0.21 | 0.11 | 149 |
| stroke 14 | 20 % → 0 % | 177.3 px | 0.00 | 0.00 | 60 |
| stroke 15 | 20 % → 0 % | 190.4 px | 0.00 | 0.00 | 50 |
| stroke 16 | 15 % → 1 % | 117.2 px | 0.22 | 0.04 | 108 |
| stroke 17 | 20 % → 1 % | 170.3 px | 0.22 | 0.05 | 105 |
| stroke 18 | 16 % → 0 % | 128.0 px | 0.00 | 0.00 | 123 |
| stroke 19 | 27 % → 1 % | 364.0 px | 0.22 | 0.04 | 32 |
| stroke 20 | 21 % → 0 % | 197.6 px | 0.00 | 0.00 | 63 |
| stroke 21 | 30 % → 0 % | 462.9 px | 0.00 | 0.00 | 24 |
| stroke 22 | 33 % → 0 % | 442.0 px | 0.00 | 0.00 | 38 |
| stroke 23 | 32 % → 0 % | 435.8 px | 0.00 | 0.00 | 41 |
| stroke 24 | 32 % → 0 % | 200.8 px | 0.00 | 0.00 | 121 |
| stroke 25 | 35 % → 0 % | 404.1 px | 0.00 | 0.00 | 49 |
| stroke 26 | 35 % → 0 % | 557.9 px | 0.00 | 0.00 | 36 |
| stroke 27 | 31 % → 0 % | 359.4 px | 0.00 | 0.00 | 113 |
| stroke 28 | 20 % → 0 % | 187.4 px | 0.00 | 0.00 | 79 |
| stroke 29 | 18 % → 0 % | 128.9 px | 0.00 | 0.00 | 128 |
| stroke 30 | 18 % → 0 % | 164.2 px | 0.00 | 0.00 | 77 |
| stroke 31 | 19 % → 3 % | 145.3 px | 0.25 | 0.14 | 49 |
| stroke 32 | 13 % → 3 % | 178.4 px | 0.25 | 0.24 | 34 |
| stroke 33 | 12 % → 3 % | 143.4 px | 0.25 | 0.25 | 37 |
| stroke 34 | 25 % → 0 % | 154.1 px | 0.25 | 0.00 | 135 |
| stroke 35 | 23 % → 2 % | 147.9 px | 0.25 | 0.10 | 153 |
| stroke 36 | 16 % → 3 % | 212.7 px | 0.25 | 0.20 | 85 |
| stroke 37 | 27 % → 0 % | 125.1 px | 0.25 | 0.00 | 250 |
| stroke 38 | 26 % → 2 % | 132.2 px | 0.25 | 0.08 | 191 |
| stroke 39 | 33 % → 0 % | 203.4 px | 0.00 | 0.00 | 140 |
| stroke 40 | 32 % → 2 % | 155.7 px | 0.25 | 0.06 | 228 |
| stroke 41 | 45 % → 3 % | 520.7 px | 0.25 | 0.07 | 65 |
| stroke 42 | 35 % → 3 % | 247.9 px | 0.25 | 0.07 | 127 |
| stroke 43 | 33 % → 0 % | 390.0 px | 0.00 | 0.00 | 64 |
| stroke 44 | 46 % → 3 % | 472.7 px | 0.25 | 0.06 | 107 |
| stroke 45 | 38 % → 3 % | 263.0 px | 0.25 | 0.07 | 115 |
| stroke 46 | 30 % → 0 % | 238.8 px | 0.00 | 0.00 | 97 |
| stroke 47 | 39 % → 2 % | 205.7 px | 0.25 | 0.06 | 147 |
| stroke 48 | 41 % → 1 % | 127.3 px | 0.25 | 0.03 | 634 |
| stroke 49 | 46 % → 2 % | 191.1 px | 0.25 | 0.04 | 667 |
| stroke 50 | 50 % → 3 % | 200.3 px | 0.25 | 0.05 | 158 |
| stroke 51 | 43 % → 2 % | 208.5 px | 0.25 | 0.04 | 263 |
| stroke 52 | 51 % → 2 % | 194.4 px | 0.25 | 0.04 | 192 |
| stroke 53 | 34 % → 0 % | 353.0 px | 0.00 | 0.00 | 48 |
| stroke 54 | 50 % → 1 % | 394.8 px | 0.26 | 0.01 | 68 |
| stroke 55 | 47 % → 0 % | 392.5 px | 0.26 | 0.00 | 60 |
| stroke 56 | 49 % → 0 % | 457.3 px | 0.00 | 0.00 | 81 |
| stroke 57 | 43 % → 0 % | 468.6 px | 0.00 | 0.00 | 41 |
| stroke 58 | 5 % → 0 % | 23.2 px | 0.00 | 0.00 | 56 |
| stroke 59 | 1 % → 0 % | 22.9 px | 0.00 | 0.00 | 15 |
| stroke 60 | 6 % → 0 % | 64.7 px | 0.00 | 0.00 | 19 |
| stroke 61 | 4 % → 0 % | 74.3 px | 0.00 | 0.00 | 6 |
| stroke 62 | 5 % → 3 % | 54.2 px | 0.21 | 0.61 | 23 |
| stroke 63 | 1 % → 0 % | 24.9 px | 0.00 | 0.00 | 10 |
| stroke 64 | 4 % → 0 % | 32.4 px | 0.00 | 0.00 | 22 |
| stroke 65 | 1 % → 0 % | 20.6 px | 0.00 | 0.00 | 10 |
| stroke 66 | 2 % → 0 % | 26.6 px | 0.00 | 0.00 | 16 |
| stroke 67 | 2 % → 0 % | 23.2 px | 0.00 | 0.00 | 4 |
| stroke 68 | 16 % → 0 % | 57.3 px | 0.00 | 0.00 | 171 |
| stroke 69 | 20 % → 0 % | 190.8 px | 0.00 | 0.00 | 54 |
| stroke 70 | 26 % → 0 % | 173.9 px | 0.00 | 0.00 | 88 |
| stroke 71 | 28 % → 0 % | 200.9 px | 0.00 | 0.00 | 91 |
| stroke 72 | 27 % → 0 % | 262.0 px | 0.00 | 0.00 | 74 |
| stroke 73 | 28 % → 0 % | 197.9 px | 0.00 | 0.00 | 121 |
| stroke 74 | 35 % → 0 % | 335.6 px | 0.00 | 0.00 | 76 |
| stroke 75 | 29 % → 0 % | 150.9 px | 0.00 | 0.00 | 151 |
| stroke 76 | 35 % → 0 % | 149.2 px | 0.00 | 0.00 | 411 |
| stroke 77 | 32 % → 0 % | 172.9 px | 0.00 | 0.00 | 334 |
| stroke 78 | 39 % → 0 % | 157.0 px | 0.00 | 0.00 | 415 |
| stroke 79 | 47 % → 0 % | 179.0 px | 0.00 | 0.00 | 686 |
| stroke 80 | 47 % → 0 % | 158.1 px | 0.00 | 0.00 | 973 |
| stroke 81 | 38 % → 0 % | 436.3 px | 0.23 | 0.00 | 111 |
| stroke 82 | 54 % → 0 % | 198.8 px | 0.23 | 0.00 | 599 |
| stroke 83 | 37 % → 3 % | 322.7 px | 0.21 | 0.08 | 152 |
| stroke 84 | 57 % → 2 % | 487.7 px | 0.22 | 0.04 | 231 |
| stroke 85 | 53 % → 0 % | 232.2 px | 0.00 | 0.00 | 695 |
| stroke 86 | 47 % → 2 % | 240.4 px | 0.21 | 0.05 | 300 |
| stroke 87 | 60 % → 0 % | 395.7 px | 0.00 | 0.00 | 179 |
| stroke 88 | 52 % → 0 % | 482.2 px | 0.00 | 0.00 | 183 |
| stroke 89 | 47 % → 3 % | 546.8 px | 0.21 | 0.07 | 75 |
| stroke 90 | 53 % → 0 % | 506.4 px | 0.00 | 0.00 | 128 |
| stroke 91 | 32 % → 3 % | 428.4 px | 0.21 | 0.10 | 43 |
| stroke 92 | 37 % → 0 % | 317.5 px | 0.00 | 0.00 | 96 |
| stroke 93 | 22 % → 0 % | 226.8 px | 0.00 | 0.00 | 66 |
| stroke 94 | 21 % → 0 % | 193.2 px | 0.00 | 0.00 | 100 |
| stroke 95 | 21 % → 0 % | 247.9 px | 0.00 | 0.00 | 90 |
| stroke 96 | 21 % → 0 % | 153.7 px | 0.00 | 0.00 | 125 |
| stroke 97 | 9 % → 0 % | 74.6 px | 0.25 | 0.01 | 128 |
| stroke 98 | 18 % → 2 % | 96.0 px | 0.25 | 0.12 | 264 |
| stroke 99 | 29 % → 0 % | 333.8 px | 0.00 | 0.00 | 104 |
| stroke 100 | 21 % → 3 % | 247.3 px | 0.25 | 0.14 | 109 |
| stroke 101 | 4 % → 0 % | 28.5 px | 0.00 | 0.00 | 46 |
| stroke 102 | 4 % → 5 % | 33.7 px | 0.21 | 1.44 | 26 |
| stroke 103 | 3 % → 0 % | 29.9 px | 0.00 | 0.00 | 26 |
| stroke 104 | 15 % → 0 % | 87.6 px | 0.00 | 0.00 | 109 |
| stroke 105 | 27 % → 0 % | 161.1 px | 0.00 | 0.00 | 97 |
| stroke 106 | 21 % → 4 % | 92.6 px | 0.21 | 0.17 | 213 |
| stroke 107 | 33 % → 3 % | 133.8 px | 0.21 | 0.10 | 356 |
| stroke 108 | 41 % → 3 % | 162.7 px | 0.21 | 0.08 | 384 |
| stroke 109 | 45 % → 0 % | 179.6 px | 0.00 | 0.00 | 303 |
| stroke 110 | 45 % → 0 % | 179.0 px | 0.00 | 0.00 | 246 |
| stroke 111 | 46 % → 0 % | 185.2 px | 0.00 | 0.00 | 754 |
| stroke 112 | 51 % → 0 % | 224.1 px | 0.00 | 0.00 | 244 |
| stroke 113 | 55 % → 0 % | 368.5 px | 0.00 | 0.00 | 90 |
| stroke 114 | 21 % → 0 % | 88.2 px | 0.00 | 0.00 | 225 |
| stroke 115 | 38 % → 0 % | 137.7 px | 0.00 | 0.00 | 308 |
| stroke 116 | 56 % → 0 % | 153.9 px | 0.00 | 0.00 | 547 |
| stroke 117 | 66 % → 0 % | 135.3 px | 0.00 | 0.00 | 327 |
| stroke 118 | 15 % → 0 % | 96.3 px | 0.00 | 0.00 | 194 |
| stroke 119 | 2 % → 0 % | 24.1 px | 0.00 | 0.00 | 14 |
| stroke 120 | 4 % → 0 % | 58.4 px | 0.00 | 0.00 | 24 |
| stroke 121 | 6 % → 0 % | 119.0 px | 0.00 | 0.00 | 16 |
| stroke 122 | 6 % → 0 % | 50.1 px | 0.00 | 0.00 | 28 |
| stroke 123 | 9 % → 0 % | 134.5 px | 0.00 | 0.00 | 18 |
| stroke 124 | 12 % → 0 % | 162.1 px | 0.00 | 0.00 | 18 |
| stroke 125 | 3 % → 0 % | 58.3 px | 0.22 | 0.14 | 12 |
| stroke 126 | 4 % → 0 % | 88.6 px | 0.22 | 0.01 | 11 |
| stroke 127 | 7 % → 0 % | 147.8 px | 0.00 | 0.00 | 17 |
| stroke 128 | 9 % → 0 % | 139.1 px | 0.00 | 0.00 | 28 |
| stroke 129 | 13 % → 0 % | 80.2 px | 0.00 | 0.00 | 142 |
| stroke 130 | 19 % → 0 % | 116.4 px | 0.00 | 0.00 | 148 |
| stroke 131 | 19 % → 1 % | 117.2 px | 0.24 | 0.03 | 269 |
| stroke 132 | 18 % → 0 % | 156.1 px | 0.00 | 0.00 | 63 |
| stroke 133 | 33 % → 0 % | 539.1 px | 0.00 | 0.00 | 20 |
| stroke 134 | 25 % → 2 % | 185.5 px | 0.25 | 0.08 | 73 |
| stroke 135 | 19 % → 2 % | 218.7 px | 0.25 | 0.13 | 34 |
| stroke 136 | 20 % → 0 % | 207.9 px | 0.00 | 0.00 | 68 |
| stroke 137 | 20 % → 0 % | 185.1 px | 0.00 | 0.00 | 74 |
| stroke 138 | 19 % → 0 % | 274.8 px | 0.00 | 0.00 | 37 |
| stroke 139 | 18 % → 0 % | 221.2 px | 0.00 | 0.00 | 25 |
| stroke 140 | 28 % → 0 % | 442.0 px | 0.00 | 0.00 | 30 |
| stroke 141 | 23 % → 0 % | 220.2 px | 0.00 | 0.00 | 30 |
| stroke 142 | 28 % → 0 % | 222.7 px | 0.00 | 0.00 | 64 |
| stroke 143 | 32 % → 0 % | 117.9 px | 0.00 | 0.00 | 187 |
| stroke 144 | 35 % → 0 % | 134.6 px | 0.00 | 0.00 | 191 |
| stroke 145 | 40 % → 0 % | 167.2 px | 0.00 | 0.00 | 152 |
| stroke 146 | 48 % → 0 % | 409.7 px | 0.00 | 0.00 | 32 |
| stroke 147 | 35 % → 0 % | 251.5 px | 0.00 | 0.00 | 72 |
| stroke 148 | 39 % → 0 % | 148.6 px | 0.00 | 0.00 | 132 |
| stroke 149 | 36 % → 0 % | 127.1 px | 0.00 | 0.00 | 198 |
| stroke 150 | 34 % → 0 % | 297.8 px | 0.00 | 0.00 | 104 |
| stroke 151 | 28 % → 0 % | 461.8 px | 0.00 | 0.00 | 38 |
| stroke 152 | 13 % → 0 % | 178.0 px | 0.00 | 0.00 | 33 |
| stroke 153 | 25 % → 0 % | 167.8 px | 0.00 | 0.00 | 91 |
| stroke 154 | 26 % → 0 % | 118.3 px | 0.00 | 0.00 | 146 |
| stroke 155 | 32 % → 0 % | 143.3 px | 0.00 | 0.00 | 126 |
| stroke 156 | 37 % → 0 % | 156.1 px | 0.00 | 0.00 | 153 |
| stroke 157 | 47 % → 0 % | 214.6 px | 0.00 | 0.00 | 119 |
| stroke 158 | 34 % → 3 % | 451.6 px | 0.25 | 0.08 | 39 |
| stroke 159 | 33 % → 3 % | 450.4 px | 0.25 | 0.09 | 34 |
| stroke 160 | 13 % → 1 % | 81.8 px | 0.26 | 0.11 | 117 |
| stroke 161 | 19 % → 0 % | 99.5 px | 0.26 | 0.01 | 141 |
| stroke 162 | 3 % → 4 % | 26.0 px | 0.21 | 1.41 | 38 |
| stroke 163 | 2 % → 3 % | 28.8 px | 0.25 | 1.56 | 36 |

Numbers say: wet paint spreads well beyond the stroke.

## Refs v3 · #15 Ultramarine script — own sheet
own sheet 800 × 1422 · Ink 0.98 · 39 px · 151.8 s

![Refs v3 · #15 Ultramarine script — own sheet](Refs-v3-15-Ultramarine-script-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 3 % → 43 % | 15.6 px | 0.64 | 16.54 | 35 |
| stroke 2 | 4 % → 45 % | 22.3 px | 0.65 | 11.11 | 9 |
| stroke 3 | 11 % → 47 % | 24.7 px | 0.65 | 4.16 | 29 |
| stroke 4 | 15 % → 45 % | 82.2 px | 0.64 | 2.96 | 6 |
| stroke 5 | 18 % → 41 % | 223.9 px | 0.64 | 2.27 | 7 |
| stroke 6 | 19 % → 40 % | 247.8 px | 0.65 | 2.07 | 4 |
| stroke 7 | 19 % → 39 % | 104.0 px | 0.63 | 2.05 | 9 |
| stroke 8 | 29 % → 45 % | 265.3 px | 0.65 | 1.54 | 8 |
| stroke 9 | 3 % → 35 % | 16.0 px | 0.64 | 12.66 | 5 |
| stroke 10 | 5 % → 45 % | 29.3 px | 0.63 | 8.33 | 12 |
| stroke 11 | 5 % → 34 % | 60.6 px | 0.64 | 7.51 | 5 |
| stroke 12 | 9 % → 35 % | 32.2 px | 0.64 | 3.77 | 20 |
| stroke 13 | 14 % → 36 % | 98.7 px | 0.63 | 2.59 | 18 |
| stroke 14 | 19 % → 37 % | 121.7 px | 0.63 | 1.94 | 15 |
| stroke 15 | 21 % → 39 % | 105.0 px | 0.63 | 1.91 | 23 |
| stroke 16 | 12 % → 45 % | 100.6 px | 0.63 | 3.88 | 6 |
| stroke 17 | 5 % → 51 % | 23.8 px | 0.65 | 10.65 | 8 |
| stroke 18 | 12 % → 49 % | 53.9 px | 0.65 | 4.09 | 10 |
| stroke 19 | 17 % → 42 % | 99.5 px | 0.63 | 2.49 | 6 |
| stroke 20 | 19 % → 47 % | 246.3 px | 0.64 | 2.50 | 2 |
| stroke 21 | 20 % → 45 % | 256.0 px | 0.63 | 2.18 | 5 |
| stroke 22 | 24 % → 49 % | 67.7 px | 0.63 | 2.02 | 43 |
| stroke 23 | 38 % → 51 % | 399.9 px | 0.64 | 1.33 | 19 |
| stroke 24 | 2 % → 36 % | 18.5 px | 0.63 | 19.39 | 6 |
| stroke 25 | 2 % → 52 % | 39.1 px | 0.65 | 21.98 | 13 |
| stroke 26 | 4 % → 65 % | 19.5 px | 0.65 | 15.50 | 13 |
| stroke 27 | 3 % → 48 % | 37.9 px | 0.64 | 14.71 | 7 |
| stroke 28 | 28 % → 62 % | 77.1 px | 0.65 | 2.17 | 31 |
| stroke 29 | 4 % → 54 % | 31.8 px | 0.64 | 13.47 | 4 |
| stroke 30 | 8 % → 43 % | 41.6 px | 0.63 | 5.67 | 18 |
| stroke 31 | 11 % → 50 % | 102.0 px | 0.63 | 4.41 | 8 |
| stroke 32 | 17 % → 43 % | 141.6 px | 0.64 | 2.62 | 14 |
| stroke 33 | 11 % → 38 % | 87.3 px | 0.64 | 3.40 | 7 |
| stroke 34 | 9 % → 40 % | 59.2 px | 0.64 | 4.66 | 13 |
| stroke 35 | 15 % → 45 % | 147.9 px | 0.63 | 2.98 | 8 |
| stroke 36 | 10 % → 40 % | 51.8 px | 0.64 | 3.88 | 13 |
| stroke 37 | 19 % → 62 % | 103.2 px | 0.65 | 3.33 | 12 |
| stroke 38 | 17 % → 39 % | 82.1 px | 0.63 | 2.28 | 18 |
| stroke 39 | 27 % → 54 % | 150.1 px | 0.64 | 1.98 | 13 |
| stroke 40 | 30 % → 56 % | 216.4 px | 0.64 | 1.83 | 8 |
| stroke 41 | 33 % → 55 % | 528.8 px | 0.64 | 1.69 | 28 |
| stroke 42 | 29 % → 50 % | 564.5 px | 0.64 | 1.68 | 3 |
| stroke 43 | 25 % → 50 % | 145.1 px | 0.64 | 1.96 | 17 |
| stroke 44 | 26 % → 52 % | 150.8 px | 0.64 | 1.98 | 61 |
| stroke 45 | 21 % → 42 % | 259.4 px | 0.65 | 2.00 | 5 |
| stroke 46 | 28 % → 60 % | 257.3 px | 0.65 | 2.13 | 19 |
| stroke 47 | 37 % → 56 % | 121.3 px | 0.65 | 1.51 | 42 |
| stroke 48 | 29 % → 46 % | 377.2 px | 0.64 | 1.57 | 4 |
| stroke 49 | 30 % → 46 % | 336.4 px | 0.65 | 1.50 | 6 |
| stroke 50 | 31 % → 43 % | 377.2 px | 0.64 | 1.36 | 7 |
| stroke 51 | 37 % → 50 % | 200.7 px | 0.65 | 1.36 | 11 |
| stroke 52 | 20 % → 54 % | 256.0 px | 0.65 | 2.77 | 3 |
| stroke 53 | 11 % → 50 % | 202.7 px | 0.62 | 4.76 | 2 |
| stroke 54 | 5 % → 55 % | 29.9 px | 0.64 | 10.96 | 28 |
| stroke 55 | 5 % → 56 % | 35.2 px | 0.66 | 11.79 | 10 |
| stroke 56 | 10 % → 49 % | 46.9 px | 0.63 | 5.01 | 7 |
| stroke 57 | 15 % → 45 % | 111.6 px | 0.65 | 3.13 | 16 |
| stroke 58 | 11 % → 62 % | 83.9 px | 0.65 | 5.63 | 11 |
| stroke 59 | 29 % → 60 % | 260.5 px | 0.66 | 2.10 | 4 |
| stroke 60 | 11 % → 47 % | 85.4 px | 0.66 | 4.18 | 5 |
| stroke 61 | 10 % → 40 % | 66.2 px | 0.66 | 3.93 | 10 |
| stroke 62 | 34 % → 60 % | 396.8 px | 0.65 | 1.76 | 5 |
| stroke 63 | 14 % → 53 % | 164.9 px | 0.65 | 3.67 | 3 |
| stroke 64 | 15 % → 57 % | 110.7 px | 0.65 | 3.74 | 12 |
| stroke 65 | 28 % → 57 % | 117.7 px | 0.65 | 2.03 | 31 |
| stroke 66 | 12 % → 55 % | 151.6 px | 0.65 | 4.74 | 14 |
| stroke 67 | 20 % → 53 % | 119.7 px | 0.65 | 2.66 | 41 |
| stroke 68 | 32 % → 54 % | 263.4 px | 0.65 | 1.68 | 17 |
| stroke 69 | 38 % → 50 % | 305.7 px | 0.65 | 1.30 | 27 |
| stroke 70 | 18 % → 53 % | 278.4 px | 0.63 | 2.98 | 2 |
| stroke 71 | 31 % → 51 % | 410.6 px | 0.64 | 1.64 | 6 |
| stroke 72 | 20 % → 56 % | 117.5 px | 0.64 | 2.76 | 8 |
| stroke 73 | 29 % → 50 % | 447.4 px | 0.64 | 1.74 | 7 |
| stroke 74 | 25 % → 58 % | 123.7 px | 0.64 | 2.35 | 17 |
| stroke 75 | 25 % → 59 % | 222.7 px | 0.65 | 2.37 | 11 |
| stroke 76 | 40 % → 55 % | 141.9 px | 0.63 | 1.37 | 24 |
| stroke 77 | 38 % → 49 % | 202.6 px | 0.65 | 1.30 | 24 |
| stroke 78 | 29 % → 44 % | 130.5 px | 0.64 | 1.52 | 36 |
| stroke 79 | 35 % → 53 % | 197.4 px | 0.64 | 1.49 | 19 |
| stroke 80 | 31 % → 52 % | 281.8 px | 0.65 | 1.71 | 4 |
| stroke 81 | 33 % → 49 % | 182.0 px | 0.66 | 1.47 | 19 |
| stroke 82 | 28 % → 58 % | 101.6 px | 0.66 | 2.10 | 225 |
| stroke 83 | 41 % → 51 % | 398.6 px | 0.64 | 1.23 | 9 |
| stroke 84 | 42 % → 51 % | 753.5 px | 0.63 | 1.23 | 11 |
| stroke 85 | 33 % → 67 % | 250.6 px | 0.66 | 2.00 | 8 |
| stroke 86 | 38 % → 61 % | 270.5 px | 0.65 | 1.61 | 8 |
| stroke 87 | 21 % → 56 % | 114.3 px | 0.64 | 2.64 | 20 |
| stroke 88 | 21 % → 55 % | 309.1 px | 0.64 | 2.64 | 4 |
| stroke 89 | 27 % → 54 % | 99.9 px | 0.65 | 2.03 | 38 |
| stroke 90 | 29 % → 55 % | 231.5 px | 0.65 | 1.87 | 5 |
| stroke 91 | 42 % → 56 % | 376.4 px | 0.64 | 1.34 | 13 |
| stroke 92 | 33 % → 68 % | 270.2 px | 0.65 | 2.08 | 5 |
| stroke 93 | 7 % → 64 % | 42.5 px | 0.65 | 8.78 | 11 |
| stroke 94 | 26 % → 64 % | 158.0 px | 0.66 | 2.52 | 18 |
| stroke 95 | 36 % → 68 % | 256.2 px | 0.66 | 1.90 | 3 |
| stroke 96 | 28 % → 61 % | 435.2 px | 0.66 | 2.16 | 2 |
| stroke 97 | 18 % → 54 % | 123.5 px | 0.65 | 2.95 | 4 |
| stroke 98 | 30 % → 59 % | 329.0 px | 0.66 | 1.94 | 3 |
| stroke 99 | 29 % → 56 % | 155.8 px | 0.65 | 1.93 | 9 |
| stroke 100 | 48 % → 65 % | 260.2 px | 0.65 | 1.34 | 10 |
| stroke 101 | 15 % → 49 % | 130.0 px | 0.66 | 3.24 | 10 |
| stroke 102 | 13 % → 49 % | 99.3 px | 0.64 | 3.73 | 22 |
| stroke 103 | 17 % → 46 % | 202.7 px | 0.64 | 2.77 | 7 |
| stroke 104 | 34 % → 57 % | 242.6 px | 0.66 | 1.67 | 12 |
| stroke 105 | 24 % → 56 % | 262.4 px | 0.66 | 2.31 | 5 |
| stroke 106 | 17 % → 61 % | 185.3 px | 0.66 | 3.57 | 7 |
| stroke 107 | 19 % → 46 % | 107.2 px | 0.64 | 2.35 | 15 |
| stroke 108 | 34 % → 55 % | 293.4 px | 0.66 | 1.59 | 4 |
| stroke 109 | 29 % → 51 % | 133.6 px | 0.65 | 1.77 | 11 |
| stroke 110 | 29 % → 58 % | 410.5 px | 0.66 | 1.99 | 2 |
| stroke 111 | 34 % → 51 % | 530.1 px | 0.65 | 1.48 | 3 |
| stroke 112 | 39 % → 53 % | 670.8 px | 0.65 | 1.36 | 2 |
| stroke 113 | 34 % → 50 % | 449.4 px | 0.66 | 1.49 | 8 |
| stroke 114 | 41 % → 49 % | 639.5 px | 0.65 | 1.18 | 5 |
| stroke 115 | 35 % → 47 % | 324.3 px | 0.66 | 1.31 | 9 |
| stroke 116 | 4 % → 61 % | 22.0 px | 0.64 | 17.06 | 20 |
| stroke 117 | 31 % → 63 % | 184.5 px | 0.65 | 2.03 | 14 |
| stroke 118 | 33 % → 61 % | 566.6 px | 0.64 | 1.86 | 2 |
| stroke 119 | 29 % → 68 % | 396.6 px | 0.67 | 2.35 | 8 |
| stroke 120 | 6 % → 50 % | 104.8 px | 0.65 | 7.83 | 3 |
| stroke 121 | 7 % → 62 % | 35.5 px | 0.65 | 8.63 | 28 |
| stroke 122 | 14 % → 39 % | 46.9 px | 0.64 | 2.86 | 20 |
| stroke 123 | 18 % → 63 % | 117.1 px | 0.65 | 3.52 | 10 |
| stroke 124 | 16 % → 60 % | 116.1 px | 0.64 | 3.79 | 14 |
| stroke 125 | 4 % → 57 % | 33.0 px | 0.63 | 13.76 | 10 |
| stroke 126 | 11 % → 57 % | 71.2 px | 0.64 | 5.17 | 21 |
| stroke 127 | 18 % → 66 % | 77.9 px | 0.64 | 3.62 | 32 |
| stroke 128 | 12 % → 62 % | 87.4 px | 0.63 | 4.99 | 13 |
| stroke 129 | 31 % → 66 % | 338.9 px | 0.65 | 2.12 | 10 |
| stroke 130 | 20 % → 55 % | 129.0 px | 0.65 | 2.77 | 20 |
| stroke 131 | 26 % → 64 % | 147.5 px | 0.64 | 2.50 | 19 |
| stroke 132 | 33 % → 60 % | 256.6 px | 0.64 | 1.80 | 13 |
| stroke 133 | 25 % → 59 % | 101.6 px | 0.63 | 2.38 | 25 |
| stroke 134 | 24 % → 53 % | 144.9 px | 0.65 | 2.20 | 8 |
| stroke 135 | 20 % → 59 % | 323.9 px | 0.64 | 2.94 | 4 |
| stroke 136 | 35 % → 61 % | 178.8 px | 0.65 | 1.76 | 21 |
| stroke 137 | 44 % → 63 % | 802.3 px | 0.65 | 1.42 | 2 |
| stroke 138 | 33 % → 61 % | 275.6 px | 0.63 | 1.88 | 10 |
| stroke 139 | 39 % → 61 % | 286.8 px | 0.65 | 1.57 | 34 |
| stroke 140 | 37 % → 63 % | 494.8 px | 0.65 | 1.68 | 5 |
| stroke 141 | 38 % → 66 % | 420.4 px | 0.64 | 1.74 | 12 |
| stroke 142 | 36 % → 53 % | 190.6 px | 0.65 | 1.49 | 32 |
| stroke 143 | 41 % → 63 % | 555.9 px | 0.66 | 1.54 | 5 |
| stroke 144 | 45 % → 62 % | 317.5 px | 0.66 | 1.37 | 10 |
| stroke 145 | 49 % → 62 % | 354.4 px | 0.66 | 1.26 | 14 |
| stroke 146 | 48 % → 61 % | 371.9 px | 0.65 | 1.27 | 19 |
| stroke 147 | 53 % → 58 % | 221.3 px | 0.66 | 1.10 | 44 |
| stroke 148 | 39 % → 49 % | 742.3 px | 0.65 | 1.26 | 3 |
| stroke 149 | 7 % → 46 % | 73.4 px | 0.64 | 6.61 | 8 |
| stroke 150 | 16 % → 50 % | 113.2 px | 0.65 | 3.19 | 24 |
| stroke 151 | 7 % → 54 % | 40.3 px | 0.65 | 7.49 | 18 |
| stroke 152 | 23 % → 53 % | 143.4 px | 0.64 | 2.33 | 7 |
| stroke 153 | 48 % → 62 % | 278.5 px | 0.65 | 1.30 | 35 |
| stroke 154 | 34 % → 56 % | 83.9 px | 0.66 | 1.67 | 38 |
| stroke 155 | 50 % → 65 % | 596.2 px | 0.66 | 1.30 | 5 |
| stroke 156 | 23 % → 49 % | 202.5 px | 0.65 | 2.13 | 11 |
| stroke 157 | 21 % → 51 % | 131.7 px | 0.65 | 2.38 | 23 |
| stroke 158 | 22 % → 50 % | 176.6 px | 0.65 | 2.27 | 11 |
| stroke 159 | 39 % → 52 % | 172.4 px | 0.65 | 1.34 | 29 |
| stroke 160 | 30 % → 49 % | 160.6 px | 0.65 | 1.64 | 22 |
| stroke 161 | 35 % → 51 % | 160.5 px | 0.64 | 1.45 | 23 |
| stroke 162 | 10 % → 54 % | 82.5 px | 0.64 | 5.56 | 5 |
| stroke 163 | 1 % → 59 % | 15.3 px | 0.64 | 41.61 | 5 |
| stroke 164 | 19 % → 58 % | 163.6 px | 0.64 | 3.02 | 9 |
| stroke 165 | 20 % → 57 % | 170.4 px | 0.64 | 2.85 | 5 |
| stroke 166 | 52 % → 65 % | 326.6 px | 0.65 | 1.25 | 10 |
| stroke 167 | 25 % → 61 % | 335.1 px | 0.64 | 2.48 | 6 |
| stroke 168 | 3 % → 68 % | 44.1 px | 0.65 | 23.21 | 4 |
| stroke 169 | 3 % → 75 % | 14.4 px | 0.66 | 27.11 | 14 |
| stroke 170 | 3 % → 62 % | 32.1 px | 0.64 | 17.97 | 13 |
| stroke 171 | 8 % → 61 % | 61.7 px | 0.64 | 7.37 | 11 |
| stroke 172 | 51 % → 63 % | 479.4 px | 0.65 | 1.24 | 7 |
| stroke 173 | 8 % → 64 % | 37.3 px | 0.65 | 8.01 | 15 |
| stroke 174 | 17 % → 70 % | 82.6 px | 0.65 | 4.22 | 8 |
| stroke 175 | 6 % → 56 % | 54.6 px | 0.64 | 9.85 | 10 |
| stroke 176 | 8 % → 57 % | 63.0 px | 0.64 | 7.09 | 6 |
| stroke 177 | 13 % → 59 % | 91.9 px | 0.64 | 4.64 | 9 |
| stroke 178 | 32 % → 60 % | 106.7 px | 0.64 | 1.89 | 32 |
| stroke 179 | 17 % → 60 % | 129.1 px | 0.64 | 3.50 | 58 |
| stroke 180 | 19 % → 55 % | 182.4 px | 0.64 | 2.85 | 20 |
| stroke 181 | 31 % → 53 % | 312.7 px | 0.63 | 1.68 | 9 |
| stroke 182 | 27 % → 55 % | 224.1 px | 0.64 | 2.00 | 16 |
| stroke 183 | 16 % → 68 % | 231.4 px | 0.65 | 4.31 | 8 |
| stroke 184 | 21 % → 62 % | 177.6 px | 0.65 | 3.01 | 6 |
| stroke 185 | 29 % → 53 % | 345.1 px | 0.64 | 1.86 | 8 |
| stroke 186 | 34 % → 70 % | 90.6 px | 0.65 | 2.09 | 11 |
| stroke 187 | 20 % → 54 % | 228.1 px | 0.64 | 2.71 | 5 |
| stroke 188 | 42 % → 57 % | 180.3 px | 0.64 | 1.38 | 22 |
| stroke 189 | 27 % → 68 % | 54.8 px | 0.66 | 2.49 | 35 |
| stroke 190 | 41 % → 58 % | 305.4 px | 0.64 | 1.39 | 15 |
| stroke 191 | 29 % → 57 % | 217.6 px | 0.64 | 1.96 | 6 |
| stroke 192 | 35 % → 61 % | 267.1 px | 0.64 | 1.73 | 26 |
| stroke 193 | 48 % → 58 % | 452.7 px | 0.64 | 1.23 | 5 |
| stroke 194 | 34 % → 63 % | 210.8 px | 0.64 | 1.87 | 15 |
| stroke 195 | 42 % → 61 % | 310.5 px | 0.64 | 1.45 | 15 |
| stroke 196 | 44 % → 61 % | 188.5 px | 0.64 | 1.39 | 11 |
| stroke 197 | 37 % → 50 % | 71.8 px | 0.63 | 1.37 | 34 |
| stroke 198 | 25 % → 55 % | 118.0 px | 0.64 | 2.24 | 5 |
| stroke 199 | 30 % → 50 % | 380.9 px | 0.64 | 1.69 | 3 |
| stroke 200 | 39 % → 53 % | 195.5 px | 0.63 | 1.35 | 161 |
| stroke 201 | 36 % → 50 % | 263.4 px | 0.63 | 1.40 | 17 |
| stroke 202 | 39 % → 53 % | 285.5 px | 0.64 | 1.35 | 5 |
| stroke 203 | 38 % → 50 % | 445.1 px | 0.64 | 1.30 | 2 |
| stroke 204 | 45 % → 54 % | 231.8 px | 0.64 | 1.19 | 9 |
| stroke 205 | 2 % → 49 % | 25.7 px | 0.63 | 24.96 | 3 |
| stroke 206 | 28 % → 62 % | 131.9 px | 0.63 | 2.22 | 16 |
| stroke 207 | 19 % → 59 % | 149.0 px | 0.64 | 3.02 | 13 |
| stroke 208 | 2 % → 67 % | 14.1 px | 0.64 | 33.97 | 5 |
| stroke 209 | 13 % → 48 % | 53.4 px | 0.64 | 3.76 | 15 |
| stroke 210 | 11 % → 59 % | 65.7 px | 0.63 | 5.59 | 8 |
| stroke 211 | 8 % → 59 % | 80.8 px | 0.64 | 7.35 | 7 |
| stroke 212 | 16 % → 63 % | 41.3 px | 0.64 | 4.07 | 32 |
| stroke 213 | 25 % → 66 % | 98.7 px | 0.64 | 2.67 | 19 |
| stroke 214 | 23 % → 59 % | 363.0 px | 0.62 | 2.62 | 2 |
| stroke 215 | 29 % → 62 % | 412.4 px | 0.63 | 2.17 | 5 |
| stroke 216 | 23 % → 60 % | 143.9 px | 0.64 | 2.63 | 16 |
| stroke 217 | 34 % → 65 % | 301.3 px | 0.64 | 1.90 | 6 |
| stroke 218 | 42 % → 61 % | 189.2 px | 0.64 | 1.47 | 21 |
| stroke 219 | 36 % → 60 % | 304.0 px | 0.63 | 1.70 | 10 |
| stroke 220 | 42 % → 59 % | 654.2 px | 0.64 | 1.41 | 3 |
| stroke 221 | 38 % → 61 % | 267.1 px | 0.64 | 1.58 | 8 |
| stroke 222 | 48 % → 58 % | 375.9 px | 0.64 | 1.21 | 11 |
| stroke 223 | 47 % → 67 % | 373.8 px | 0.64 | 1.41 | 5 |
| stroke 224 | 17 % → 47 % | 123.6 px | 0.64 | 2.76 | 13 |
| stroke 225 | 20 % → 52 % | 163.2 px | 0.65 | 2.56 | 10 |
| stroke 226 | 36 % → 55 % | 159.5 px | 0.64 | 1.54 | 31 |
| stroke 227 | 29 % → 54 % | 255.6 px | 0.64 | 1.83 | 20 |
| stroke 228 | 13 % → 47 % | 166.7 px | 0.64 | 3.57 | 3 |
| stroke 229 | 29 % → 48 % | 163.8 px | 0.64 | 1.64 | 19 |
| stroke 230 | 31 % → 57 % | 111.6 px | 0.65 | 1.85 | 19 |
| stroke 231 | 25 % → 54 % | 205.1 px | 0.63 | 2.19 | 6 |
| stroke 232 | 33 % → 57 % | 393.1 px | 0.64 | 1.76 | 6 |
| stroke 233 | 37 % → 57 % | 166.6 px | 0.64 | 1.54 | 26 |
| stroke 234 | 26 % → 63 % | 297.5 px | 0.66 | 2.40 | 7 |
| stroke 235 | 12 % → 44 % | 80.9 px | 0.65 | 3.63 | 11 |
| stroke 236 | 30 % → 59 % | 232.3 px | 0.66 | 1.97 | 11 |
| stroke 237 | 32 % → 55 % | 139.1 px | 0.65 | 1.75 | 25 |
| stroke 238 | 26 % → 48 % | 95.8 px | 0.64 | 1.85 | 17 |
| stroke 239 | 30 % → 51 % | 279.1 px | 0.65 | 1.72 | 18 |
| stroke 240 | 23 % → 47 % | 191.4 px | 0.65 | 2.04 | 8 |
| stroke 241 | 35 % → 52 % | 135.5 px | 0.65 | 1.47 | 23 |
| stroke 242 | 2 % → 51 % | 15.6 px | 0.63 | 27.27 | 6 |
| stroke 243 | 8 % → 58 % | 30.6 px | 0.64 | 7.57 | 25 |
| stroke 244 | 23 % → 63 % | 278.8 px | 0.65 | 2.78 | 8 |
| stroke 245 | 1 % → 35 % | 16.1 px | 0.63 | 28.57 | 3 |
| stroke 246 | 4 % → 44 % | 25.4 px | 0.64 | 10.51 | 11 |
| stroke 247 | 11 % → 42 % | 58.1 px | 0.63 | 3.78 | 12 |
| stroke 248 | 10 % → 33 % | 93.7 px | 0.63 | 3.20 | 7 |
| stroke 249 | 8 % → 38 % | 67.4 px | 0.61 | 4.73 | 12 |
| stroke 250 | 18 % → 64 % | 174.0 px | 0.64 | 3.51 | 8 |
| stroke 251 | 9 % → 49 % | 83.3 px | 0.62 | 5.37 | 6 |
| stroke 252 | 12 % → 63 % | 149.0 px | 0.64 | 5.14 | 4 |
| stroke 253 | 9 % → 66 % | 139.8 px | 0.64 | 7.39 | 4 |
| stroke 254 | 12 % → 56 % | 84.9 px | 0.64 | 4.54 | 5 |
| stroke 255 | 30 % → 58 % | 357.3 px | 0.64 | 1.94 | 3 |
| stroke 256 | 23 % → 54 % | 237.5 px | 0.65 | 2.38 | 6 |
| stroke 257 | 27 % → 55 % | 394.5 px | 0.65 | 2.07 | 2 |
| stroke 258 | 46 % → 64 % | 306.5 px | 0.66 | 1.39 | 16 |
| stroke 259 | 17 % → 65 % | 225.1 px | 0.64 | 3.79 | 5 |
| stroke 260 | 36 % → 62 % | 150.2 px | 0.65 | 1.70 | 22 |
| stroke 261 | 20 % → 57 % | 96.4 px | 0.64 | 2.83 | 16 |
| stroke 262 | 20 % → 54 % | 309.7 px | 0.64 | 2.74 | 5 |
| stroke 263 | 20 % → 52 % | 171.1 px | 0.64 | 2.64 | 11 |
| stroke 264 | 28 % → 56 % | 353.0 px | 0.65 | 2.02 | 2 |
| stroke 265 | 23 % → 48 % | 364.4 px | 0.62 | 2.07 | 3 |
| stroke 266 | 17 % → 31 % | 233.7 px | 0.63 | 1.78 | 5 |
| stroke 267 | 16 % → 34 % | 99.5 px | 0.62 | 2.06 | 20 |
| stroke 268 | 22 % → 50 % | 202.3 px | 0.64 | 2.34 | 6 |
| stroke 269 | 32 % → 61 % | 165.4 px | 0.64 | 1.87 | 35 |
| stroke 270 | 21 % → 34 % | 314.6 px | 0.62 | 1.58 | 2 |
| stroke 271 | 33 % → 54 % | 245.5 px | 0.63 | 1.62 | 7 |
| stroke 272 | 45 % → 64 % | 453.6 px | 0.65 | 1.41 | 9 |
| stroke 273 | 26 % → 48 % | 156.1 px | 0.63 | 1.81 | 13 |
| stroke 274 | 33 % → 39 % | 281.9 px | 0.62 | 1.18 | 11 |
| stroke 275 | 44 % → 59 % | 248.1 px | 0.65 | 1.35 | 13 |
| stroke 276 | 39 % → 55 % | 646.8 px | 0.63 | 1.39 | 12 |
| stroke 277 | 33 % → 48 % | 281.5 px | 0.63 | 1.44 | 5 |
| stroke 278 | 49 % → 61 % | 335.0 px | 0.64 | 1.24 | 57 |
| stroke 279 | 32 % → 51 % | 362.2 px | 0.63 | 1.61 | 5 |
| stroke 280 | 37 % → 53 % | 609.6 px | 0.63 | 1.41 | 6 |
| stroke 281 | 46 % → 54 % | 408.0 px | 0.63 | 1.18 | 8 |
| stroke 282 | 51 % → 55 % | 194.6 px | 0.64 | 1.08 | 13 |
| stroke 283 | 34 % → 56 % | 101.0 px | 0.63 | 1.63 | 29 |
| stroke 284 | 12 % → 43 % | 59.3 px | 0.61 | 3.57 | 10 |
| stroke 285 | 11 % → 38 % | 62.2 px | 0.62 | 3.56 | 11 |
| stroke 286 | 17 % → 36 % | 117.0 px | 0.61 | 2.07 | 11 |
| stroke 287 | 38 % → 51 % | 174.1 px | 0.62 | 1.33 | 21 |
| stroke 288 | 39 % → 51 % | 263.6 px | 0.61 | 1.31 | 9 |
| stroke 289 | 32 % → 55 % | 281.6 px | 0.64 | 1.72 | 9 |
| stroke 290 | 21 % → 58 % | 116.2 px | 0.65 | 2.83 | 7 |
| stroke 291 | 45 % → 67 % | 209.4 px | 0.66 | 1.49 | 17 |
| stroke 292 | 29 % → 62 % | 213.0 px | 0.67 | 2.14 | 2 |
| stroke 293 | 44 % → 64 % | 118.7 px | 0.65 | 1.46 | 15 |
| stroke 294 | 35 % → 56 % | 236.5 px | 0.66 | 1.60 | 17 |
| stroke 295 | 10 % → 35 % | 95.1 px | 0.63 | 3.43 | 6 |
| stroke 296 | 31 % → 39 % | 86.1 px | 0.64 | 1.28 | 69 |
| stroke 297 | 28 % → 73 % | 106.4 px | 0.66 | 2.57 | 16 |
| stroke 298 | 4 % → 41 % | 35.1 px | 0.63 | 9.21 | 18 |
| stroke 299 | 2 % → 29 % | 13.3 px | 0.62 | 13.62 | 7 |
| stroke 300 | 7 % → 33 % | 72.0 px | 0.62 | 4.75 | 14 |
| stroke 301 | 9 % → 30 % | 48.4 px | 0.62 | 3.46 | 8 |
| stroke 302 | 18 % → 47 % | 56.6 px | 0.64 | 2.54 | 27 |
| stroke 303 | 19 % → 42 % | 146.9 px | 0.63 | 2.24 | 9 |
| stroke 304 | 14 % → 36 % | 122.5 px | 0.62 | 2.62 | 8 |
| stroke 305 | 22 % → 47 % | 216.4 px | 0.63 | 2.20 | 9 |
| stroke 306 | 22 % → 45 % | 182.5 px | 0.63 | 2.07 | 10 |
| stroke 307 | 12 % → 31 % | 95.9 px | 0.62 | 2.55 | 10 |
| stroke 308 | 19 % → 39 % | 181.0 px | 0.62 | 2.01 | 4 |
| stroke 309 | 20 % → 38 % | 164.8 px | 0.62 | 1.91 | 6 |
| stroke 310 | 20 % → 29 % | 107.3 px | 0.61 | 1.47 | 12 |
| stroke 311 | 16 % → 44 % | 86.2 px | 0.63 | 2.83 | 14 |
| stroke 312 | 2 % → 34 % | 19.1 px | 0.63 | 20.06 | 8 |
| stroke 313 | 18 % → 45 % | 143.2 px | 0.63 | 2.51 | 10 |
| stroke 314 | 28 % → 46 % | 341.9 px | 0.63 | 1.61 | 3 |
| stroke 315 | 14 % → 44 % | 174.8 px | 0.63 | 3.11 | 3 |
| stroke 316 | 27 % → 44 % | 194.5 px | 0.63 | 1.60 | 20 |
| stroke 317 | 30 % → 45 % | 516.8 px | 0.64 | 1.53 | 2 |
| stroke 318 | 22 % → 41 % | 175.1 px | 0.63 | 1.86 | 19 |
| stroke 319 | 30 % → 42 % | 568.1 px | 0.63 | 1.39 | 2 |
| stroke 320 | 22 % → 40 % | 190.6 px | 0.63 | 1.84 | 15 |
| stroke 321 | 8 % → 42 % | 64.6 px | 0.63 | 5.21 | 7 |
| stroke 322 | 21 % → 61 % | 187.7 px | 0.64 | 2.95 | 11 |
| stroke 323 | 7 % → 56 % | 48.3 px | 0.64 | 7.66 | 20 |
| stroke 324 | 29 % → 59 % | 58.1 px | 0.65 | 2.06 | 35 |
| stroke 325 | 34 % → 60 % | 225.7 px | 0.65 | 1.79 | 34 |
| stroke 326 | 32 % → 54 % | 248.7 px | 0.65 | 1.69 | 7 |
| stroke 327 | 20 % → 51 % | 82.6 px | 0.63 | 2.48 | 70 |
| stroke 328 | 26 % → 48 % | 98.5 px | 0.63 | 1.82 | 17 |
| stroke 329 | 32 % → 53 % | 187.2 px | 0.65 | 1.66 | 11 |
| stroke 330 | 20 % → 52 % | 58.3 px | 0.63 | 2.61 | 38 |
| stroke 331 | 42 % → 56 % | 445.6 px | 0.65 | 1.34 | 7 |
| stroke 332 | 40 % → 53 % | 256.4 px | 0.64 | 1.34 | 11 |
| stroke 333 | 7 % → 54 % | 49.1 px | 0.64 | 8.10 | 17 |
| stroke 334 | 7 % → 56 % | 56.9 px | 0.64 | 8.47 | 5 |
| stroke 335 | 9 % → 62 % | 69.1 px | 0.65 | 7.16 | 14 |
| stroke 336 | 3 % → 48 % | 17.1 px | 0.64 | 18.40 | 8 |
| stroke 337 | 7 % → 55 % | 42.7 px | 0.65 | 8.46 | 16 |
| stroke 338 | 12 % → 53 % | 151.2 px | 0.65 | 4.52 | 2 |
| stroke 339 | 28 % → 57 % | 235.3 px | 0.65 | 2.05 | 8 |
| stroke 340 | 13 % → 70 % | 104.1 px | 0.66 | 5.35 | 6 |
| stroke 341 | 32 % → 56 % | 187.3 px | 0.65 | 1.76 | 20 |
| stroke 342 | 9 % → 66 % | 99.0 px | 0.64 | 7.20 | 3 |
| stroke 343 | 20 % → 63 % | 166.6 px | 0.64 | 3.11 | 10 |
| stroke 344 | 24 % → 66 % | 397.0 px | 0.65 | 2.70 | 3 |
| stroke 345 | 21 % → 65 % | 185.1 px | 0.64 | 3.05 | 4 |
| stroke 346 | 30 % → 64 % | 424.5 px | 0.65 | 2.12 | 10 |
| stroke 347 | 34 % → 59 % | 112.2 px | 0.63 | 1.73 | 33 |
| stroke 348 | 41 % → 56 % | 258.4 px | 0.65 | 1.37 | 14 |
| stroke 349 | 43 % → 56 % | 266.5 px | 0.65 | 1.30 | 20 |
| stroke 350 | 39 % → 59 % | 351.4 px | 0.65 | 1.51 | 14 |
| stroke 351 | 37 % → 57 % | 317.7 px | 0.64 | 1.55 | 8 |
| stroke 352 | 39 % → 64 % | 661.1 px | 0.64 | 1.65 | 3 |
| stroke 353 | 32 % → 49 % | 282.4 px | 0.64 | 1.54 | 8 |
| stroke 354 | 13 % → 49 % | 80.6 px | 0.64 | 3.84 | 10 |
| stroke 355 | 27 % → 53 % | 229.4 px | 0.64 | 1.95 | 7 |
| stroke 356 | 6 % → 34 % | 29.1 px | 0.64 | 5.51 | 7 |
| stroke 357 | 21 % → 51 % | 88.5 px | 0.64 | 2.40 | 17 |
| stroke 358 | 9 % → 42 % | 43.0 px | 0.64 | 4.91 | 12 |
| stroke 359 | 15 % → 39 % | 110.8 px | 0.64 | 2.58 | 19 |
| stroke 360 | 19 % → 50 % | 223.7 px | 0.64 | 2.66 | 3 |
| stroke 361 | 22 % → 49 % | 396.3 px | 0.64 | 2.24 | 15 |
| stroke 362 | 22 % → 47 % | 151.0 px | 0.64 | 2.18 | 10 |
| stroke 363 | 21 % → 44 % | 320.9 px | 0.64 | 2.12 | 5 |
| stroke 364 | 27 % → 51 % | 211.5 px | 0.64 | 1.88 | 20 |
| stroke 365 | 26 % → 38 % | 310.9 px | 0.65 | 1.43 | 3 |
| stroke 366 | 34 % → 45 % | 250.3 px | 0.64 | 1.31 | 15 |
| stroke 367 | 19 % → 63 % | 56.8 px | 0.66 | 3.35 | 13 |
| stroke 368 | 5 % → 72 % | 18.4 px | 0.66 | 15.46 | 10 |
| stroke 369 | 20 % → 55 % | 108.5 px | 0.64 | 2.74 | 16 |
| stroke 370 | 10 % → 56 % | 89.4 px | 0.64 | 5.68 | 11 |
| stroke 371 | 13 % → 50 % | 228.0 px | 0.63 | 3.86 | 11 |
| stroke 372 | 14 % → 56 % | 131.3 px | 0.64 | 4.13 | 9 |
| stroke 373 | 22 % → 51 % | 88.8 px | 0.63 | 2.36 | 28 |
| stroke 374 | 27 % → 57 % | 152.5 px | 0.64 | 2.11 | 5 |
| stroke 375 | 22 % → 51 % | 189.7 px | 0.62 | 2.34 | 4 |
| stroke 376 | 36 % → 58 % | 326.1 px | 0.64 | 1.61 | 17 |
| stroke 377 | 31 % → 52 % | 105.0 px | 0.62 | 1.66 | 29 |
| stroke 378 | 9 % → 50 % | 50.2 px | 0.63 | 5.58 | 12 |
| stroke 379 | 28 % → 56 % | 116.0 px | 0.64 | 1.98 | 26 |
| stroke 380 | 13 % → 55 % | 79.5 px | 0.63 | 4.21 | 12 |
| stroke 381 | 13 % → 49 % | 53.5 px | 0.63 | 3.72 | 17 |
| stroke 382 | 31 % → 52 % | 107.0 px | 0.63 | 1.68 | 20 |
| stroke 383 | 26 % → 52 % | 165.2 px | 0.63 | 2.03 | 44 |
| stroke 384 | 32 % → 53 % | 203.0 px | 0.63 | 1.68 | 10 |
| stroke 385 | 7 % → 67 % | 30.8 px | 0.66 | 9.47 | 7 |
| stroke 386 | 17 % → 50 % | 70.9 px | 0.64 | 2.94 | 26 |
| stroke 387 | 4 % → 55 % | 31.5 px | 0.65 | 13.32 | 4 |
| stroke 388 | 38 % → 67 % | 75.7 px | 0.65 | 1.75 | 38 |
| stroke 389 | 22 % → 57 % | 91.6 px | 0.65 | 2.59 | 10 |
| stroke 390 | 10 % → 62 % | 164.2 px | 0.65 | 6.11 | 5 |
| stroke 391 | 31 % → 61 % | 108.4 px | 0.65 | 1.95 | 23 |
| stroke 392 | 26 % → 58 % | 82.7 px | 0.64 | 2.26 | 21 |
| stroke 393 | 30 % → 56 % | 159.3 px | 0.65 | 1.85 | 71 |
| stroke 394 | 36 % → 63 % | 199.1 px | 0.65 | 1.75 | 13 |
| stroke 395 | 23 % → 50 % | 73.0 px | 0.64 | 2.23 | 24 |
| stroke 396 | 39 % → 61 % | 319.0 px | 0.65 | 1.58 | 19 |
| stroke 397 | 45 % → 57 % | 818.5 px | 0.66 | 1.28 | 2 |
| stroke 398 | 25 % → 49 % | 483.3 px | 0.64 | 1.92 | 5 |
| stroke 399 | 32 % → 57 % | 276.6 px | 0.66 | 1.78 | 14 |
| stroke 400 | 51 % → 64 % | 215.1 px | 0.65 | 1.24 | 20 |
| stroke 401 | 45 % → 59 % | 132.6 px | 0.65 | 1.30 | 22 |
| stroke 402 | 42 % → 57 % | 374.0 px | 0.66 | 1.35 | 25 |
| stroke 403 | 47 % → 56 % | 289.2 px | 0.66 | 1.18 | 20 |
| stroke 404 | 66 % → 73 % | 1256.3 px | 0.65 | 1.12 | 2 |
| stroke 405 | 14 % → 46 % | 118.2 px | 0.63 | 3.24 | 9 |
| stroke 406 | 32 % → 48 % | 97.9 px | 0.63 | 1.53 | 33 |
| stroke 407 | 36 % → 53 % | 174.3 px | 0.64 | 1.47 | 13 |
| stroke 408 | 36 % → 53 % | 91.7 px | 0.63 | 1.48 | 54 |
| stroke 409 | 39 % → 51 % | 113.0 px | 0.65 | 1.30 | 12 |
| stroke 410 | 52 % → 63 % | 337.9 px | 0.66 | 1.23 | 2 |
| stroke 411 | 26 % → 49 % | 166.2 px | 0.63 | 1.93 | 3 |
| stroke 412 | 31 % → 51 % | 216.4 px | 0.63 | 1.68 | 5 |
| stroke 413 | 35 % → 49 % | 242.1 px | 0.63 | 1.42 | 7 |
| stroke 414 | 34 % → 47 % | 235.0 px | 0.63 | 1.40 | 3 |
| stroke 415 | 37 % → 47 % | 371.6 px | 0.64 | 1.27 | 2 |
| stroke 416 | 37 % → 46 % | 264.0 px | 0.64 | 1.23 | 7 |
| stroke 417 | 40 % → 51 % | 243.0 px | 0.63 | 1.26 | 5 |
| stroke 418 | 41 % → 47 % | 228.7 px | 0.64 | 1.14 | 9 |
| stroke 419 | 49 % → 57 % | 387.4 px | 0.64 | 1.16 | 4 |
| stroke 420 | 38 % → 44 % | 126.1 px | 0.64 | 1.17 | 9 |

Numbers say: wet paint spreads well beyond the stroke.

## Refs v3 · #16 Shrigley strokes — own sheet
own sheet 800 × 1000 · Watercolour 1.00 + water 30 % · 64 px · 27.5 s

![Refs v3 · #16 Shrigley strokes — own sheet](Refs-v3-16-Shrigley-strokes-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 6 % → 19 % | 33.2 px | 0.33 | 3.20 | 59 |
| stroke 2 | 4 % → 5 % | 45.8 px | 0.34 | 1.37 | 15 |
| stroke 3 | 7 % → 8 % | 80.8 px | 0.31 | 1.17 | 26 |
| stroke 4 | 10 % → 16 % | 44.9 px | 0.35 | 1.62 | 125 |
| stroke 5 | 3 % → 4 % | 28.0 px | 0.30 | 1.72 | 13 |
| stroke 6 | 7 % → 15 % | 121.8 px | 0.33 | 2.00 | 14 |
| stroke 7 | 8 % → 7 % | 54.6 px | 0.32 | 0.95 | 171 |
| stroke 8 | 14 % → 12 % | 113.8 px | 0.31 | 0.85 | 55 |
| stroke 9 | 18 % → 9 % | 324.6 px | 0.30 | 0.49 | 28 |
| stroke 10 | 14 % → 12 % | 73.5 px | 0.29 | 0.89 | 214 |
| stroke 11 | 10 % → 20 % | 83.0 px | 0.28 | 2.06 | 81 |
| stroke 12 | 15 % → 5 % | 75.2 px | 0.27 | 0.31 | 184 |
| stroke 13 | 8 % → 7 % | 39.9 px | 0.23 | 0.84 | 582 |
| stroke 14 | 8 % → 15 % | 78.7 px | 0.28 | 1.85 | 97 |
| stroke 15 | 24 % → 8 % | 121.0 px | 0.23 | 0.33 | 148 |
| stroke 16 | 12 % → 14 % | 87.2 px | 0.27 | 1.20 | 80 |
| stroke 17 | 27 % → 14 % | 246.2 px | 0.28 | 0.50 | 50 |
| stroke 18 | 11 % → 12 % | 132.9 px | 0.32 | 1.08 | 29 |
| stroke 19 | 10 % → 15 % | 44.9 px | 0.30 | 1.49 | 260 |
| stroke 20 | 15 % → 18 % | 155.3 px | 0.30 | 1.23 | 71 |
| stroke 21 | 16 % → 21 % | 193.0 px | 0.29 | 1.34 | 20 |
| stroke 22 | 14 % → 13 % | 71.3 px | 0.27 | 0.96 | 175 |
| stroke 23 | 22 % → 18 % | 118.8 px | 0.28 | 0.83 | 125 |
| stroke 24 | 17 % → 10 % | 104.1 px | 0.34 | 0.57 | 36 |
| stroke 25 | 7 % → 15 % | 29.5 px | 0.34 | 2.02 | 74 |
| stroke 26 | 14 % → 16 % | 77.3 px | 0.35 | 1.17 | 40 |
| stroke 27 | 8 % → 9 % | 44.8 px | 0.31 | 1.12 | 137 |
| stroke 28 | 14 % → 7 % | 111.6 px | 0.31 | 0.51 | 21 |
| stroke 29 | 19 % → 8 % | 171.3 px | 0.31 | 0.44 | 18 |
| stroke 30 | 6 % → 18 % | 194.3 px | 0.31 | 2.94 | 10 |
| stroke 31 | 9 % → 11 % | 97.9 px | 0.32 | 1.30 | 33 |
| stroke 32 | 7 % → 9 % | 162.5 px | 0.32 | 1.43 | 7 |
| stroke 33 | 10 % → 8 % | 79.5 px | 0.32 | 0.73 | 70 |
| stroke 34 | 10 % → 7 % | 82.1 px | 0.31 | 0.68 | 34 |
| stroke 35 | 24 % → 6 % | 162.0 px | 0.31 | 0.26 | 52 |
| stroke 36 | 15 % → 8 % | 170.6 px | 0.30 | 0.55 | 58 |
| stroke 37 | 13 % → 4 % | 90.2 px | 0.27 | 0.30 | 61 |
| stroke 38 | 19 % → 3 % | 105.5 px | 0.27 | 0.17 | 46 |
| stroke 39 | 24 % → 11 % | 221.2 px | 0.25 | 0.44 | 31 |
| stroke 40 | 17 % → 11 % | 195.9 px | 0.28 | 0.61 | 24 |
| stroke 41 | 10 % → 16 % | 93.1 px | 0.30 | 1.53 | 58 |
| stroke 42 | 11 % → 16 % | 157.0 px | 0.28 | 1.51 | 22 |
| stroke 43 | 7 % → 12 % | 42.2 px | 0.29 | 1.61 | 73 |
| stroke 44 | 6 % → 14 % | 47.0 px | 0.27 | 2.34 | 31 |
| stroke 45 | 15 % → 11 % | 194.8 px | 0.28 | 0.77 | 19 |
| stroke 46 | 11 % → 12 % | 109.3 px | 0.29 | 1.17 | 32 |
| stroke 47 | 15 % → 8 % | 370.3 px | 0.34 | 0.51 | 8 |
| stroke 48 | 12 % → 9 % | 146.3 px | 0.32 | 0.72 | 23 |
| stroke 49 | 19 % → 7 % | 200.5 px | 0.33 | 0.38 | 55 |
| stroke 50 | 20 % → 9 % | 162.6 px | 0.30 | 0.46 | 109 |
| stroke 51 | 5 % → 12 % | 73.8 px | 0.26 | 2.12 | 22 |
| stroke 52 | 5 % → 0 % | 64.0 px | 0.19 | 0.01 | 42 |
| stroke 53 | 7 % → 0 % | 197.3 px | 0.18 | 0.01 | 10 |
| stroke 54 | 4 % → 11 % | 40.7 px | 0.28 | 2.90 | 31 |
| stroke 55 | 5 % → 18 % | 128.1 px | 0.28 | 3.99 | 8 |
| stroke 56 | 11 % → 6 % | 61.5 px | 0.36 | 0.53 | 86 |
| stroke 57 | 18 % → 12 % | 104.3 px | 0.34 | 0.64 | 28 |
| stroke 58 | 6 % → 12 % | 103.6 px | 0.29 | 1.98 | 6 |
| stroke 59 | 3 % → 23 % | 50.5 px | 0.24 | 7.99 | 6 |
| stroke 60 | 16 % → 13 % | 56.2 px | 0.31 | 0.81 | 42 |
| stroke 61 | 1 % → 8 % | 46.2 px | 0.29 | 6.06 | 6 |
| stroke 62 | 9 % → 11 % | 49.0 px | 0.33 | 1.26 | 313 |
| stroke 63 | 13 % → 6 % | 49.3 px | 0.33 | 0.45 | 275 |
| stroke 64 | 17 % → 11 % | 154.7 px | 0.30 | 0.65 | 53 |
| stroke 65 | 20 % → 10 % | 85.0 px | 0.34 | 0.50 | 221 |
| stroke 66 | 4 % → 2 % | 147.1 px | 0.29 | 0.53 | 7 |
| stroke 67 | 10 % → 3 % | 69.6 px | 0.32 | 0.31 | 90 |
| stroke 68 | 16 % → 1 % | 354.0 px | 0.29 | 0.09 | 14 |
| stroke 69 | 13 % → 10 % | 80.7 px | 0.31 | 0.76 | 52 |
| stroke 70 | 8 % → 8 % | 41.3 px | 0.25 | 1.02 | 95 |
| stroke 71 | 14 % → 5 % | 62.1 px | 0.30 | 0.38 | 307 |
| stroke 72 | 11 % → 9 % | 234.0 px | 0.31 | 0.82 | 38 |
| stroke 73 | 13 % → 11 % | 185.3 px | 0.29 | 0.88 | 32 |
| stroke 74 | 20 % → 9 % | 161.3 px | 0.26 | 0.42 | 144 |
| stroke 75 | 5 % → 21 % | 42.9 px | 0.30 | 4.35 | 88 |
| stroke 76 | 9 % → 21 % | 60.8 px | 0.30 | 2.24 | 65 |
| stroke 77 | 13 % → 22 % | 88.1 px | 0.27 | 1.65 | 105 |
| stroke 78 | 9 % → 14 % | 36.1 px | 0.34 | 1.59 | 281 |
| stroke 79 | 2 % → 10 % | 28.5 px | 0.31 | 4.86 | 34 |
| stroke 80 | 5 % → 11 % | 59.3 px | 0.31 | 2.12 | 31 |
| stroke 81 | 2 % → 10 % | 29.2 px | 0.31 | 4.07 | 11 |
| stroke 82 | 8 % → 12 % | 111.4 px | 0.31 | 1.39 | 26 |
| stroke 83 | 6 % → 8 % | 51.3 px | 0.31 | 1.46 | 23 |
| stroke 84 | 2 % → 3 % | 37.4 px | 0.27 | 1.60 | 14 |
| stroke 85 | 5 % → 13 % | 41.8 px | 0.28 | 2.48 | 100 |
| stroke 86 | 3 % → 13 % | 91.2 px | 0.23 | 4.24 | 5 |
| stroke 87 | 10 % → 17 % | 201.7 px | 0.27 | 1.74 | 24 |
| stroke 88 | 12 % → 14 % | 124.6 px | 0.27 | 1.16 | 69 |
| stroke 89 | 6 % → 11 % | 40.7 px | 0.29 | 1.72 | 159 |
| stroke 90 | 4 % → 16 % | 142.6 px | 0.28 | 3.56 | 22 |
| stroke 91 | 3 % → 14 % | 96.3 px | 0.28 | 4.17 | 13 |
| stroke 92 | 10 % → 12 % | 50.8 px | 0.26 | 1.19 | 461 |
| stroke 93 | 12 % → 15 % | 53.6 px | 0.30 | 1.28 | 107 |
| stroke 94 | 10 % → 11 % | 37.0 px | 0.31 | 1.19 | 107 |

Numbers say: wet paint spreads well beyond the stroke.

## Refs v3 · #17 Krovostok dry brush — own sheet
own sheet 800 × 720 · Ink 0.93 · Gouache 0.07 · 53 px · 31.9 s

![Refs v3 · #17 Krovostok dry brush — own sheet](Refs-v3-17-Krovostok-dry-brush-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 9 % → 51 % | 53.8 px | 0.81 | 5.39 | 87 |
| stroke 2 | 14 % → 46 % | 68.2 px | 0.80 | 3.30 | 123 |
| stroke 3 | 19 % → 50 % | 87.9 px | 0.80 | 2.56 | 144 |
| stroke 4 | 25 % → 55 % | 107.5 px | 0.80 | 2.23 | 172 |
| stroke 5 | 37 % → 71 % | 233.7 px | 0.81 | 1.90 | 106 |
| stroke 6 | 36 % → 72 % | 261.9 px | 0.80 | 1.97 | 71 |
| stroke 7 | 34 % → 64 % | 157.2 px | 0.80 | 1.90 | 185 |
| stroke 8 | 40 % → 66 % | 337.3 px | 0.80 | 1.66 | 62 |
| stroke 9 | 44 % → 80 % | 284.1 px | 0.80 | 1.82 | 90 |
| stroke 10 | 37 % → 57 % | 474.4 px | 0.80 | 1.55 | 25 |
| stroke 11 | 45 % → 77 % | 261.0 px | 0.80 | 1.72 | 105 |
| stroke 12 | 37 % → 56 % | 182.9 px | 0.80 | 1.52 | 143 |
| stroke 13 | 24 % → 62 % | 194.3 px | 0.80 | 2.60 | 52 |
| stroke 14 | 28 % → 30 % | 377.2 px | 0.78 | 1.09 | 28 |
| stroke 15 | 46 % → 69 % | 360.6 px | 0.80 | 1.49 | 75 |
| stroke 16 | 4 % → 33 % | 56.3 px | 0.79 | 8.76 | 21 |
| stroke 17 | 39 % → 72 % | 495.1 px | 0.80 | 1.85 | 54 |
| stroke 18 | 32 % → 72 % | 202.4 px | 0.80 | 2.26 | 100 |
| stroke 19 | 12 % → 42 % | 126.7 px | 0.79 | 3.40 | 48 |
| stroke 20 | 39 % → 75 % | 307.5 px | 0.80 | 1.92 | 58 |
| stroke 21 | 35 % → 76 % | 270.4 px | 0.79 | 2.20 | 60 |
| stroke 22 | 24 % → 51 % | 216.8 px | 0.80 | 2.14 | 95 |
| stroke 23 | 38 % → 68 % | 166.9 px | 0.80 | 1.79 | 343 |
| stroke 24 | 41 % → 73 % | 182.6 px | 0.80 | 1.78 | 172 |
| stroke 25 | 4 % → 33 % | 69.9 px | 0.79 | 7.52 | 13 |
| stroke 26 | 42 % → 77 % | 207.0 px | 0.80 | 1.84 | 281 |
| stroke 27 | 8 % → 41 % | 71.6 px | 0.80 | 5.11 | 85 |
| stroke 28 | 37 % → 66 % | 170.7 px | 0.80 | 1.79 | 221 |
| stroke 29 | 12 % → 52 % | 92.6 px | 0.80 | 4.38 | 71 |
| stroke 30 | 35 % → 65 % | 176.9 px | 0.80 | 1.87 | 216 |
| stroke 31 | 49 % → 67 % | 245.6 px | 0.80 | 1.37 | 179 |
| stroke 32 | 32 % → 62 % | 161.1 px | 0.79 | 1.95 | 409 |
| stroke 33 | 46 % → 59 % | 217.8 px | 0.80 | 1.27 | 275 |
| stroke 34 | 32 % → 62 % | 167.1 px | 0.80 | 1.90 | 210 |
| stroke 35 | 48 % → 60 % | 621.1 px | 0.80 | 1.25 | 27 |
| stroke 36 | 40 % → 48 % | 433.9 px | 0.80 | 1.19 | 32 |
| stroke 37 | 36 % → 63 % | 164.8 px | 0.80 | 1.75 | 312 |
| stroke 38 | 47 % → 55 % | 427.7 px | 0.79 | 1.18 | 51 |
| stroke 39 | 38 % → 40 % | 442.8 px | 0.79 | 1.04 | 31 |
| stroke 40 | 38 % → 61 % | 170.9 px | 0.80 | 1.59 | 203 |
| stroke 41 | 43 % → 76 % | 556.8 px | 0.80 | 1.76 | 22 |
| stroke 42 | 44 % → 69 % | 330.8 px | 0.81 | 1.56 | 54 |
| stroke 43 | 39 % → 61 % | 287.8 px | 0.80 | 1.58 | 83 |
| stroke 44 | 41 % → 61 % | 322.8 px | 0.80 | 1.48 | 127 |
| stroke 45 | 35 % → 42 % | 167.2 px | 0.80 | 1.21 | 229 |
| stroke 46 | 40 % → 44 % | 194.1 px | 0.80 | 1.09 | 121 |
| stroke 47 | 52 % → 53 % | 382.3 px | 0.80 | 1.03 | 66 |

Numbers say: wet paint spreads well beyond the stroke.

## Refs v3 · #18 Twombly blue sticks — own sheet
own sheet 800 × 789 · Wax 1.00 · 19 px · 18.9 s

![Refs v3 · #18 Twombly blue sticks — own sheet](Refs-v3-18-Twombly-blue-sticks-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 4 % → 28 % | 20.9 px | 0.34 | 7.76 | 3 |
| stroke 2 | 6 % → 8 % | 34.1 px | 0.32 | 1.43 | 0 |
| stroke 3 | 6 % → 22 % | 16.0 px | 0.34 | 3.76 | 2 |
| stroke 4 | 11 % → 6 % | 26.1 px | 0.31 | 0.55 | 3 |
| stroke 5 | 10 % → 14 % | 40.8 px | 0.34 | 1.40 | 2 |
| stroke 6 | 13 % → 15 % | 75.2 px | 0.33 | 1.15 | 0 |
| stroke 7 | 14 % → 23 % | 47.0 px | 0.34 | 1.61 | 5 |
| stroke 8 | 18 % → 10 % | 75.2 px | 0.34 | 0.60 | 1 |
| stroke 9 | 11 % → 34 % | 45.3 px | 0.34 | 3.08 | 1 |
| stroke 10 | 14 % → 41 % | 82.9 px | 0.35 | 2.88 | 0 |
| stroke 11 | 18 % → 41 % | 50.3 px | 0.34 | 2.34 | 3 |
| stroke 12 | 16 % → 31 % | 28.0 px | 0.34 | 1.94 | 6 |
| stroke 13 | 5 % → 0 % | 19.0 px | 0.00 | 0.00 | 3 |
| stroke 14 | 24 % → 32 % | 130.9 px | 0.34 | 1.35 | 0 |
| stroke 15 | 19 % → 15 % | 83.3 px | 0.34 | 0.81 | 2 |
| stroke 16 | 18 % → 48 % | 103.1 px | 0.34 | 2.61 | 0 |
| stroke 17 | 28 % → 19 % | 118.5 px | 0.34 | 0.68 | 2 |
| stroke 18 | 9 % → 0 % | 31.7 px | 0.00 | 0.00 | 3 |
| stroke 19 | 4 % → 0 % | 23.8 px | 0.00 | 0.00 | 1 |
| stroke 20 | 21 % → 22 % | 48.5 px | 0.34 | 1.08 | 6 |
| stroke 21 | 18 % → 0 % | 50.8 px | 0.24 | 0.00 | 5 |
| stroke 22 | 9 % → 0 % | 22.4 px | 0.00 | 0.00 | 2 |
| stroke 23 | 12 % → 38 % | 67.8 px | 0.34 | 3.24 | 1 |
| stroke 24 | 25 % → 20 % | 148.0 px | 0.34 | 0.79 | 0 |
| stroke 25 | 28 % → 5 % | 112.9 px | 0.34 | 0.18 | 1 |
| stroke 26 | 14 % → 0 % | 82.8 px | 0.00 | 0.00 | 0 |
| stroke 27 | 15 % → 1 % | 38.7 px | 0.29 | 0.05 | 6 |
| stroke 28 | 23 % → 19 % | 65.5 px | 0.34 | 0.81 | 2 |
| stroke 29 | 10 % → 4 % | 32.9 px | 0.33 | 0.41 | 1 |
| stroke 30 | 15 % → 0 % | 47.1 px | 0.00 | 0.00 | 3 |
| stroke 31 | 9 % → 0 % | 47.1 px | 0.00 | 0.00 | 1 |
| stroke 32 | 18 % → 0 % | 38.3 px | 0.00 | 0.00 | 3 |
| stroke 33 | 8 % → 0 % | 43.8 px | 0.00 | 0.00 | 0 |
| stroke 34 | 20 % → 6 % | 36.9 px | 0.33 | 0.28 | 5 |
| stroke 35 | 20 % → 0 % | 66.1 px | 0.00 | 0.00 | 3 |
| stroke 36 | 11 % → 0 % | 53.5 px | 0.00 | 0.00 | 1 |
| stroke 37 | 25 % → 7 % | 54.2 px | 0.33 | 0.26 | 4 |
| stroke 38 | 26 % → 0 % | 150.1 px | 0.00 | 0.00 | 2 |
| stroke 39 | 18 % → 0 % | 105.4 px | 0.00 | 0.00 | 1 |
| stroke 40 | 12 % → 0 % | 60.2 px | 0.00 | 0.00 | 0 |
| stroke 41 | 22 % → 7 % | 46.5 px | 0.33 | 0.31 | 7 |
| stroke 42 | 36 % → 0 % | 147.7 px | 0.00 | 0.00 | 8 |
| stroke 43 | 25 % → 0 % | 56.4 px | 0.00 | 0.00 | 5 |
| stroke 44 | 12 % → 0 % | 68.8 px | 0.00 | 0.00 | 0 |
| stroke 45 | 28 % → 0 % | 161.5 px | 0.28 | 0.02 | 8 |
| stroke 46 | 19 % → 0 % | 106.1 px | 0.00 | 0.00 | 0 |
| stroke 47 | 12 % → 1 % | 63.4 px | 0.32 | 0.11 | 1 |
| stroke 48 | 18 % → 2 % | 39.1 px | 0.33 | 0.11 | 13 |
| stroke 49 | 23 % → 0 % | 74.9 px | 0.00 | 0.00 | 3 |
| stroke 50 | 12 % → 8 % | 64.9 px | 0.34 | 0.73 | 1 |
| stroke 51 | 4 % → 0 % | 20.3 px | 0.00 | 0.00 | 7 |
| stroke 52 | 14 % → 0 % | 32.6 px | 0.00 | 0.00 | 14 |
| stroke 53 | 12 % → 6 % | 16.3 px | 0.34 | 0.52 | 29 |
| stroke 54 | 15 % → 9 % | 27.0 px | 0.34 | 0.62 | 16 |
| stroke 55 | 11 % → 0 % | 27.5 px | 0.00 | 0.00 | 8 |
| stroke 56 | 17 % → 0 % | 43.3 px | 0.00 | 0.00 | 6 |
| stroke 57 | 22 % → 5 % | 29.3 px | 0.34 | 0.24 | 45 |
| stroke 58 | 22 % → 10 % | 56.2 px | 0.34 | 0.47 | 2 |
| stroke 59 | 25 % → 3 % | 35.3 px | 0.34 | 0.11 | 68 |
| stroke 60 | 33 % → 3 % | 46.2 px | 0.34 | 0.09 | 76 |
| stroke 61 | 42 % → 2 % | 56.4 px | 0.34 | 0.04 | 52 |
| stroke 62 | 42 % → 0 % | 56.2 px | 0.00 | 0.00 | 39 |
| stroke 63 | 20 % → 0 % | 11.9 px | 0.00 | 0.00 | 42 |
| stroke 64 | 31 % → 0 % | 39.3 px | 0.00 | 0.00 | 8 |
| stroke 65 | 35 % → 0 % | 156.8 px | 0.00 | 0.00 | 1 |
| stroke 66 | 33 % → 0 % | 22.8 px | 0.00 | 0.00 | 79 |
| stroke 67 | 11 % → 0 % | 20.5 px | 0.00 | 0.00 | 11 |
| stroke 68 | 7 % → 4 % | 24.0 px | 0.33 | 0.57 | 3 |
| stroke 69 | 5 % → 49 % | 23.4 px | 0.34 | 9.67 | 4 |
| stroke 70 | 6 % → 22 % | 28.1 px | 0.34 | 3.47 | 5 |
| stroke 71 | 10 % → 48 % | 28.8 px | 0.34 | 4.67 | 5 |
| stroke 72 | 5 % → 0 % | 23.0 px | 0.00 | 0.00 | 1 |
| stroke 73 | 7 % → 7 % | 30.7 px | 0.34 | 0.96 | 5 |
| stroke 74 | 7 % → 6 % | 25.8 px | 0.34 | 0.80 | 8 |
| stroke 75 | 8 % → 8 % | 23.2 px | 0.33 | 1.02 | 13 |
| stroke 76 | 18 % → 0 % | 84.0 px | 0.00 | 0.00 | 2 |
| stroke 77 | 19 % → 41 % | 59.7 px | 0.34 | 2.12 | 9 |
| stroke 78 | 17 % → 46 % | 43.9 px | 0.34 | 2.76 | 12 |
| stroke 79 | 6 % → 30 % | 20.8 px | 0.34 | 5.13 | 6 |
| stroke 80 | 9 % → 18 % | 43.4 px | 0.34 | 1.96 | 1 |
| stroke 81 | 12 % → 0 % | 52.3 px | 0.00 | 0.00 | 5 |
| stroke 82 | 9 % → 15 % | 28.4 px | 0.35 | 1.74 | 3 |
| stroke 83 | 17 % → 29 % | 76.9 px | 0.35 | 1.73 | 1 |
| stroke 84 | 12 % → 37 % | 34.4 px | 0.34 | 3.02 | 3 |
| stroke 85 | 18 % → 0 % | 70.3 px | 0.00 | 0.00 | 12 |
| stroke 86 | 28 % → 48 % | 106.3 px | 0.34 | 1.73 | 6 |
| stroke 87 | 17 % → 34 % | 77.3 px | 0.34 | 1.95 | 19 |
| stroke 88 | 19 % → 11 % | 62.2 px | 0.34 | 0.57 | 7 |
| stroke 89 | 17 % → 33 % | 55.9 px | 0.34 | 1.98 | 4 |
| stroke 90 | 23 % → 18 % | 107.3 px | 0.34 | 0.80 | 4 |
| stroke 91 | 25 % → 0 % | 71.3 px | 0.00 | 0.00 | 9 |
| stroke 92 | 25 % → 11 % | 58.0 px | 0.34 | 0.44 | 15 |
| stroke 93 | 6 % → 0 % | 22.8 px | 0.00 | 0.00 | 8 |
| stroke 94 | 20 % → 28 % | 57.3 px | 0.34 | 1.37 | 7 |
| stroke 95 | 16 % → 16 % | 55.2 px | 0.34 | 1.02 | 6 |
| stroke 96 | 26 % → 22 % | 107.5 px | 0.35 | 0.84 | 14 |
| stroke 97 | 21 % → 12 % | 98.6 px | 0.33 | 0.57 | 2 |
| stroke 98 | 25 % → 22 % | 72.2 px | 0.34 | 0.88 | 4 |
| stroke 99 | 14 % → 13 % | 63.6 px | 0.34 | 0.99 | 10 |
| stroke 100 | 41 % → 28 % | 192.9 px | 0.34 | 0.69 | 3 |
| stroke 101 | 37 % → 23 % | 158.0 px | 0.34 | 0.63 | 4 |
| stroke 102 | 38 % → 30 % | 145.1 px | 0.34 | 0.77 | 17 |
| stroke 103 | 29 % → 19 % | 97.5 px | 0.34 | 0.66 | 28 |
| stroke 104 | 39 % → 37 % | 101.8 px | 0.34 | 0.94 | 6 |
| stroke 105 | 37 % → 29 % | 140.8 px | 0.35 | 0.77 | 3 |
| stroke 106 | 38 % → 40 % | 145.0 px | 0.34 | 1.05 | 13 |
| stroke 107 | 16 % → 12 % | 72.8 px | 0.34 | 0.75 | 14 |
| stroke 108 | 31 % → 17 % | 137.9 px | 0.34 | 0.56 | 2 |
| stroke 109 | 37 % → 8 % | 158.8 px | 0.34 | 0.23 | 9 |
| stroke 110 | 43 % → 24 % | 130.0 px | 0.34 | 0.54 | 3 |
| stroke 111 | 31 % → 15 % | 108.9 px | 0.33 | 0.50 | 9 |
| stroke 112 | 13 % → 37 % | 46.2 px | 0.34 | 2.86 | 5 |
| stroke 113 | 37 % → 4 % | 164.9 px | 0.32 | 0.12 | 5 |
| stroke 114 | 34 % → 6 % | 85.6 px | 0.33 | 0.19 | 9 |
| stroke 115 | 38 % → 16 % | 178.8 px | 0.34 | 0.43 | 2 |
| stroke 116 | 48 % → 41 % | 223.5 px | 0.35 | 0.85 | 4 |
| stroke 117 | 54 % → 35 % | 189.9 px | 0.35 | 0.65 | 5 |
| stroke 118 | 47 % → 13 % | 201.2 px | 0.34 | 0.28 | 5 |
| stroke 119 | 30 % → 29 % | 116.7 px | 0.34 | 0.98 | 4 |
| stroke 120 | 31 % → 31 % | 98.0 px | 0.34 | 0.99 | 12 |
| stroke 121 | 55 % → 45 % | 220.3 px | 0.35 | 0.81 | 11 |
| stroke 122 | 11 % → 0 % | 18.7 px | 0.00 | 0.00 | 51 |
| stroke 123 | 7 % → 0 % | 26.4 px | 0.00 | 0.00 | 17 |
| stroke 124 | 17 % → 0 % | 56.2 px | 0.00 | 0.00 | 12 |
| stroke 125 | 15 % → 0 % | 40.9 px | 0.00 | 0.00 | 14 |
| stroke 126 | 8 % → 0 % | 27.0 px | 0.00 | 0.00 | 7 |
| stroke 127 | 29 % → 0 % | 103.9 px | 0.00 | 0.00 | 5 |
| stroke 128 | 11 % → 18 % | 21.2 px | 0.34 | 1.71 | 13 |
| stroke 129 | 12 % → 41 % | 16.2 px | 0.35 | 3.34 | 44 |
| stroke 130 | 21 % → 34 % | 55.6 px | 0.34 | 1.59 | 17 |
| stroke 131 | 13 % → 55 % | 47.1 px | 0.34 | 4.12 | 14 |
| stroke 132 | 22 % → 59 % | 91.8 px | 0.35 | 2.70 | 6 |
| stroke 133 | 15 % → 61 % | 72.8 px | 0.35 | 3.95 | 2 |
| stroke 134 | 29 % → 77 % | 124.6 px | 0.35 | 2.60 | 5 |
| stroke 135 | 24 % → 27 % | 54.6 px | 0.35 | 1.11 | 19 |
| stroke 136 | 31 % → 52 % | 132.9 px | 0.35 | 1.70 | 8 |
| stroke 137 | 35 % → 36 % | 154.9 px | 0.35 | 1.02 | 14 |
| stroke 138 | 16 % → 34 % | 53.5 px | 0.34 | 2.18 | 7 |
| stroke 139 | 27 % → 33 % | 124.1 px | 0.34 | 1.25 | 1 |
| stroke 140 | 31 % → 32 % | 82.0 px | 0.34 | 1.02 | 5 |
| stroke 141 | 31 % → 1 % | 125.0 px | 0.31 | 0.02 | 4 |
| stroke 142 | 18 % → 55 % | 83.7 px | 0.34 | 3.02 | 2 |
| stroke 143 | 24 % → 61 % | 93.9 px | 0.34 | 2.55 | 25 |
| stroke 144 | 35 % → 0 % | 88.7 px | 0.00 | 0.00 | 23 |
| stroke 145 | 33 % → 0 % | 100.7 px | 0.00 | 0.00 | 6 |
| stroke 146 | 37 % → 0 % | 137.5 px | 0.31 | 0.00 | 3 |
| stroke 147 | 22 % → 27 % | 95.6 px | 0.34 | 1.23 | 5 |
| stroke 148 | 44 % → 24 % | 116.5 px | 0.35 | 0.55 | 12 |
| stroke 149 | 57 % → 32 % | 262.5 px | 0.35 | 0.56 | 4 |
| stroke 150 | 60 % → 33 % | 207.0 px | 0.34 | 0.55 | 28 |
| stroke 151 | 28 % → 0 % | 82.7 px | 0.00 | 0.00 | 19 |
| stroke 152 | 25 % → 0 % | 53.3 px | 0.00 | 0.00 | 20 |
| stroke 153 | 14 % → 6 % | 34.4 px | 0.34 | 0.44 | 8 |
| stroke 154 | 18 % → 0 % | 67.1 px | 0.22 | 0.01 | 3 |
| stroke 155 | 34 % → 0 % | 130.7 px | 0.00 | 0.00 | 9 |
| stroke 156 | 40 % → 0 % | 100.3 px | 0.00 | 0.00 | 14 |
| stroke 157 | 19 % → 0 % | 49.7 px | 0.00 | 0.00 | 15 |
| stroke 158 | 8 % → 0 % | 31.6 px | 0.00 | 0.00 | 12 |
| stroke 159 | 11 % → 0 % | 44.2 px | 0.00 | 0.00 | 11 |
| stroke 160 | 7 % → 3 % | 20.6 px | 0.33 | 0.42 | 3 |
| stroke 161 | 5 % → 14 % | 14.6 px | 0.35 | 2.82 | 2 |
| stroke 162 | 9 % → 12 % | 26.2 px | 0.34 | 1.29 | 6 |
| stroke 163 | 13 % → 10 % | 48.8 px | 0.33 | 0.76 | 3 |
| stroke 164 | 21 % → 4 % | 120.8 px | 0.34 | 0.17 | 1 |
| stroke 165 | 10 % → 17 % | 61.2 px | 0.34 | 1.68 | 1 |
| stroke 166 | 20 % → 1 % | 73.3 px | 0.32 | 0.05 | 3 |
| stroke 167 | 3 % → 13 % | 17.0 px | 0.34 | 4.67 | 1 |
| stroke 168 | 5 % → 22 % | 13.8 px | 0.35 | 4.61 | 4 |
| stroke 169 | 10 % → 14 % | 25.9 px | 0.34 | 1.47 | 9 |
| stroke 170 | 22 % → 0 % | 96.9 px | 0.00 | 0.00 | 1 |
| stroke 171 | 5 % → 9 % | 23.5 px | 0.34 | 1.75 | 2 |
| stroke 172 | 11 % → 16 % | 47.7 px | 0.34 | 1.47 | 5 |
| stroke 173 | 17 % → 14 % | 47.2 px | 0.35 | 0.85 | 8 |
| stroke 174 | 23 % → 0 % | 106.5 px | 0.00 | 0.00 | 3 |
| stroke 175 | 21 % → 0 % | 93.9 px | 0.00 | 0.00 | 1 |
| stroke 176 | 17 % → 4 % | 52.0 px | 0.33 | 0.25 | 5 |
| stroke 177 | 21 % → 0 % | 51.3 px | 0.33 | 0.01 | 12 |
| stroke 178 | 9 % → 1 % | 28.5 px | 0.33 | 0.12 | 8 |
| stroke 179 | 18 % → 11 % | 42.2 px | 0.34 | 0.59 | 11 |
| stroke 180 | 22 % → 0 % | 60.8 px | 0.00 | 0.00 | 2 |
| stroke 181 | 23 % → 0 % | 106.0 px | 0.00 | 0.00 | 1 |
| stroke 182 | 9 % → 0 % | 55.0 px | 0.00 | 0.00 | 0 |
| stroke 183 | 19 % → 1 % | 73.5 px | 0.34 | 0.05 | 1 |
| stroke 184 | 22 % → 0 % | 130.6 px | 0.00 | 0.00 | 7 |
| stroke 185 | 30 % → 0 % | 176.1 px | 0.00 | 0.00 | 1 |
| stroke 186 | 21 % → 3 % | 53.0 px | 0.33 | 0.14 | 8 |
| stroke 187 | 34 % → 0 % | 114.5 px | 0.00 | 0.00 | 1 |
| stroke 188 | 16 % → 0 % | 38.3 px | 0.27 | 0.00 | 16 |
| stroke 189 | 26 % → 0 % | 155.7 px | 0.00 | 0.00 | 1 |
| stroke 190 | 24 % → 2 % | 57.3 px | 0.33 | 0.09 | 10 |
| stroke 191 | 19 % → 0 % | 55.6 px | 0.00 | 0.00 | 5 |
| stroke 192 | 32 % → 0 % | 91.6 px | 0.00 | 0.00 | 13 |
| stroke 193 | 25 % → 0 % | 85.2 px | 0.00 | 0.00 | 2 |
| stroke 194 | 27 % → 0 % | 63.6 px | 0.00 | 0.00 | 15 |
| stroke 195 | 23 % → 0 % | 54.6 px | 0.00 | 0.00 | 14 |
| stroke 196 | 30 % → 3 % | 69.7 px | 0.35 | 0.09 | 20 |
| stroke 197 | 30 % → 0 % | 112.6 px | 0.00 | 0.00 | 3 |
| stroke 198 | 25 % → 0 % | 149.1 px | 0.00 | 0.00 | 1 |
| stroke 199 | 32 % → 0 % | 77.0 px | 0.00 | 0.00 | 9 |
| stroke 200 | 33 % → 0 % | 107.8 px | 0.00 | 0.00 | 5 |
| stroke 201 | 25 % → 0 % | 147.9 px | 0.00 | 0.00 | 3 |
| stroke 202 | 28 % → 0 % | 127.4 px | 0.00 | 0.00 | 2 |
| stroke 203 | 30 % → 0 % | 136.7 px | 0.00 | 0.00 | 1 |
| stroke 204 | 31 % → 0 % | 194.9 px | 0.00 | 0.00 | 0 |
| stroke 205 | 31 % → 0 % | 140.0 px | 0.00 | 0.00 | 1 |
| stroke 206 | 29 % → 0 % | 73.6 px | 0.00 | 0.00 | 6 |
| stroke 207 | 30 % → 0 % | 183.4 px | 0.00 | 0.00 | 0 |
| stroke 208 | 29 % → 0 % | 110.2 px | 0.00 | 0.00 | 1 |
| stroke 209 | 27 % → 0 % | 157.6 px | 0.00 | 0.00 | 0 |
| stroke 210 | 26 % → 0 % | 120.4 px | 0.00 | 0.00 | 2 |
| stroke 211 | 26 % → 0 % | 154.7 px | 0.00 | 0.00 | 1 |
| stroke 212 | 20 % → 0 % | 88.0 px | 0.00 | 0.00 | 1 |
| stroke 213 | 27 % → 0 % | 66.4 px | 0.00 | 0.00 | 9 |
| stroke 214 | 31 % → 0 % | 111.6 px | 0.00 | 0.00 | 1 |
| stroke 215 | 16 % → 4 % | 44.1 px | 0.33 | 0.23 | 3 |
| stroke 216 | 31 % → 0 % | 92.3 px | 0.00 | 0.00 | 3 |
| stroke 217 | 27 % → 0 % | 118.1 px | 0.00 | 0.00 | 5 |
| stroke 218 | 31 % → 0 % | 175.6 px | 0.00 | 0.00 | 1 |
| stroke 219 | 22 % → 0 % | 84.2 px | 0.00 | 0.00 | 2 |
| stroke 220 | 29 % → 0 % | 94.7 px | 0.00 | 0.00 | 2 |
| stroke 221 | 27 % → 3 % | 122.0 px | 0.32 | 0.10 | 5 |
| stroke 222 | 28 % → 0 % | 78.1 px | 0.00 | 0.00 | 2 |
| stroke 223 | 32 % → 1 % | 78.6 px | 0.30 | 0.02 | 10 |
| stroke 224 | 26 % → 0 % | 117.8 px | 0.00 | 0.00 | 2 |
| stroke 225 | 34 % → 0 % | 102.2 px | 0.00 | 0.00 | 2 |
| stroke 226 | 32 % → 4 % | 103.4 px | 0.33 | 0.14 | 15 |
| stroke 227 | 25 % → 0 % | 112.7 px | 0.00 | 0.00 | 1 |
| stroke 228 | 31 % → 3 % | 72.9 px | 0.33 | 0.09 | 6 |
| stroke 229 | 12 % → 9 % | 55.1 px | 0.33 | 0.69 | 1 |
| stroke 230 | 33 % → 1 % | 76.7 px | 0.33 | 0.04 | 29 |
| stroke 231 | 17 % → 9 % | 79.2 px | 0.33 | 0.51 | 2 |
| stroke 232 | 38 % → 0 % | 98.1 px | 0.00 | 0.00 | 9 |
| stroke 233 | 22 % → 5 % | 57.3 px | 0.33 | 0.22 | 10 |
| stroke 234 | 39 % → 0 % | 94.9 px | 0.23 | 0.00 | 15 |
| stroke 235 | 39 % → 0 % | 96.7 px | 0.00 | 0.00 | 6 |
| stroke 236 | 21 % → 5 % | 54.5 px | 0.33 | 0.24 | 5 |
| stroke 237 | 29 % → 2 % | 68.4 px | 0.33 | 0.07 | 18 |
| stroke 238 | 40 % → 0 % | 93.8 px | 0.00 | 0.00 | 24 |
| stroke 239 | 40 % → 0 % | 96.8 px | 0.00 | 0.00 | 8 |
| stroke 240 | 39 % → 0 % | 108.3 px | 0.00 | 0.00 | 2 |
| stroke 241 | 36 % → 0 % | 159.9 px | 0.00 | 0.00 | 1 |
| stroke 242 | 13 % → 37 % | 40.8 px | 0.34 | 2.88 | 7 |
| stroke 243 | 24 % → 32 % | 93.3 px | 0.34 | 1.34 | 7 |
| stroke 244 | 10 % → 31 % | 38.8 px | 0.35 | 3.03 | 7 |
| stroke 245 | 16 % → 29 % | 52.4 px | 0.34 | 1.78 | 9 |
| stroke 246 | 40 % → 44 % | 106.7 px | 0.34 | 1.11 | 24 |
| stroke 247 | 43 % → 43 % | 170.8 px | 0.34 | 1.00 | 7 |
| stroke 248 | 11 % → 58 % | 34.2 px | 0.34 | 5.42 | 13 |
| stroke 249 | 13 % → 28 % | 36.1 px | 0.34 | 2.23 | 9 |
| stroke 250 | 26 % → 32 % | 65.7 px | 0.34 | 1.22 | 23 |
| stroke 251 | 17 % → 73 % | 64.1 px | 0.35 | 4.40 | 14 |
| stroke 252 | 27 % → 48 % | 73.7 px | 0.34 | 1.77 | 24 |
| stroke 253 | 31 % → 48 % | 100.8 px | 0.34 | 1.52 | 8 |
| stroke 254 | 15 % → 41 % | 62.9 px | 0.34 | 2.66 | 7 |
| stroke 255 | 22 % → 57 % | 56.8 px | 0.35 | 2.62 | 19 |
| stroke 256 | 23 % → 43 % | 59.4 px | 0.34 | 1.88 | 10 |
| stroke 257 | 35 % → 35 % | 117.6 px | 0.34 | 1.03 | 16 |
| stroke 258 | 48 % → 60 % | 203.3 px | 0.35 | 1.24 | 9 |
| stroke 259 | 16 % → 53 % | 66.3 px | 0.35 | 3.21 | 5 |
| stroke 260 | 48 % → 54 % | 165.8 px | 0.35 | 1.13 | 12 |
| stroke 261 | 24 % → 47 % | 94.3 px | 0.35 | 1.92 | 8 |
| stroke 262 | 34 % → 64 % | 148.6 px | 0.35 | 1.87 | 5 |
| stroke 263 | 43 % → 64 % | 172.9 px | 0.35 | 1.48 | 14 |
| stroke 264 | 55 % → 60 % | 191.3 px | 0.34 | 1.09 | 14 |
| stroke 265 | 47 % → 65 % | 164.7 px | 0.35 | 1.38 | 15 |
| stroke 266 | 41 % → 52 % | 182.0 px | 0.35 | 1.25 | 9 |
| stroke 267 | 75 % → 84 % | 330.2 px | 0.35 | 1.12 | 8 |
| stroke 268 | 65 % → 67 % | 214.4 px | 0.35 | 1.03 | 6 |
| stroke 269 | 54 % → 55 % | 212.5 px | 0.35 | 1.02 | 5 |
| stroke 270 | 57 % → 57 % | 172.1 px | 0.35 | 1.00 | 16 |
| stroke 271 | 22 % → 22 % | 47.3 px | 0.34 | 1.00 | 39 |
| stroke 272 | 13 % → 22 % | 61.3 px | 0.34 | 1.70 | 7 |
| stroke 273 | 17 % → 17 % | 67.2 px | 0.34 | 1.01 | 7 |
| stroke 274 | 11 % → 38 % | 36.0 px | 0.34 | 3.49 | 18 |
| stroke 275 | 20 % → 46 % | 75.1 px | 0.34 | 2.32 | 7 |
| stroke 276 | 26 % → 37 % | 98.5 px | 0.34 | 1.43 | 13 |
| stroke 277 | 29 % → 34 % | 99.8 px | 0.34 | 1.17 | 11 |
| stroke 278 | 40 % → 42 % | 142.0 px | 0.34 | 1.04 | 15 |
| stroke 279 | 9 % → 36 % | 42.0 px | 0.34 | 3.93 | 9 |
| stroke 280 | 16 % → 27 % | 51.1 px | 0.34 | 1.68 | 14 |
| stroke 281 | 21 % → 28 % | 84.4 px | 0.34 | 1.31 | 8 |
| stroke 282 | 24 % → 50 % | 73.9 px | 0.34 | 2.11 | 10 |
| stroke 283 | 26 % → 48 % | 70.4 px | 0.34 | 1.83 | 17 |
| stroke 284 | 12 % → 27 % | 51.7 px | 0.33 | 2.19 | 7 |
| stroke 285 | 17 % → 21 % | 74.3 px | 0.34 | 1.24 | 6 |
| stroke 286 | 28 % → 45 % | 110.6 px | 0.34 | 1.59 | 6 |
| stroke 287 | 38 % → 56 % | 159.4 px | 0.34 | 1.46 | 5 |
| stroke 288 | 45 % → 53 % | 149.4 px | 0.34 | 1.19 | 28 |
| stroke 289 | 34 % → 34 % | 117.9 px | 0.34 | 1.00 | 17 |
| stroke 290 | 9 % → 9 % | 36.0 px | 0.33 | 1.00 | 10 |
| stroke 291 | 11 % → 11 % | 28.0 px | 0.34 | 1.00 | 24 |
| stroke 292 | 10 % → 10 % | 26.8 px | 0.34 | 1.00 | 15 |

Numbers say: wet paint spreads well beyond the stroke.

## Refs v3 · #19 Guston charcoal hand — own sheet
own sheet 800 × 800 · Charcoal 1.00 · 60 px · 12.7 s

![Refs v3 · #19 Guston charcoal hand — own sheet](Refs-v3-19-Guston-charcoal-hand-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 4 % → 26 % | 36.3 px | 0.59 | 6.51 | 23 |
| stroke 2 | 7 % → 27 % | 75.6 px | 0.59 | 3.72 | 29 |
| stroke 3 | 8 % → 25 % | 187.6 px | 0.59 | 3.09 | 9 |
| stroke 4 | 10 % → 28 % | 105.9 px | 0.59 | 2.75 | 27 |
| stroke 5 | 9 % → 28 % | 120.3 px | 0.59 | 3.06 | 35 |
| stroke 6 | 16 % → 33 % | 405.0 px | 0.59 | 2.02 | 10 |
| stroke 7 | 17 % → 30 % | 450.6 px | 0.59 | 1.81 | 7 |
| stroke 8 | 16 % → 32 % | 206.5 px | 0.59 | 2.03 | 26 |
| stroke 9 | 2 % → 64 % | 35.0 px | 0.60 | 29.08 | 21 |
| stroke 10 | 4 % → 65 % | 78.1 px | 0.60 | 14.80 | 16 |
| stroke 11 | 3 % → 39 % | 43.5 px | 0.60 | 11.28 | 10 |
| stroke 12 | 6 % → 45 % | 77.2 px | 0.60 | 7.99 | 24 |
| stroke 13 | 3 % → 46 % | 52.9 px | 0.59 | 16.73 | 8 |
| stroke 14 | 4 % → 65 % | 140.7 px | 0.60 | 16.58 | 5 |
| stroke 15 | 15 % → 47 % | 190.0 px | 0.59 | 3.20 | 26 |
| stroke 16 | 8 % → 70 % | 151.7 px | 0.60 | 8.57 | 12 |
| stroke 17 | 10 % → 33 % | 292.8 px | 0.59 | 3.20 | 13 |
| stroke 18 | 2 % → 48 % | 55.8 px | 0.60 | 30.16 | 5 |
| stroke 19 | 5 % → 56 % | 107.9 px | 0.60 | 10.76 | 20 |
| stroke 20 | 4 % → 37 % | 113.1 px | 0.60 | 10.36 | 11 |
| stroke 21 | 9 % → 52 % | 168.6 px | 0.60 | 5.54 | 15 |
| stroke 22 | 13 % → 67 % | 366.2 px | 0.60 | 5.40 | 9 |
| stroke 23 | 20 % → 45 % | 162.4 px | 0.60 | 2.22 | 51 |
| stroke 24 | 15 % → 34 % | 107.6 px | 0.60 | 2.23 | 69 |
| stroke 25 | 9 % → 52 % | 168.0 px | 0.60 | 6.00 | 26 |
| stroke 26 | 15 % → 73 % | 315.3 px | 0.60 | 5.02 | 13 |
| stroke 27 | 14 % → 67 % | 313.4 px | 0.60 | 4.84 | 26 |
| stroke 28 | 17 % → 68 % | 169.4 px | 0.60 | 3.96 | 62 |
| stroke 29 | 19 % → 70 % | 402.9 px | 0.60 | 3.76 | 25 |
| stroke 30 | 22 % → 52 % | 166.3 px | 0.60 | 2.38 | 78 |
| stroke 31 | 9 % → 46 % | 263.0 px | 0.60 | 5.12 | 16 |
| stroke 32 | 11 % → 48 % | 340.0 px | 0.60 | 4.52 | 26 |
| stroke 33 | 10 % → 43 % | 269.0 px | 0.60 | 4.10 | 23 |
| stroke 34 | 21 % → 61 % | 326.6 px | 0.60 | 2.97 | 30 |
| stroke 35 | 21 % → 57 % | 533.4 px | 0.60 | 2.78 | 20 |
| stroke 36 | 19 % → 38 % | 116.6 px | 0.60 | 1.99 | 153 |
| stroke 37 | 26 % → 57 % | 521.7 px | 0.60 | 2.17 | 23 |
| stroke 38 | 17 % → 41 % | 233.8 px | 0.60 | 2.38 | 45 |
| stroke 39 | 22 % → 64 % | 568.9 px | 0.60 | 2.97 | 18 |
| stroke 40 | 24 % → 51 % | 375.9 px | 0.60 | 2.15 | 22 |
| stroke 41 | 25 % → 43 % | 444.1 px | 0.60 | 1.70 | 41 |
| stroke 42 | 25 % → 66 % | 455.6 px | 0.60 | 2.65 | 28 |
| stroke 43 | 13 % → 39 % | 215.7 px | 0.60 | 2.97 | 24 |
| stroke 44 | 25 % → 51 % | 184.6 px | 0.60 | 2.08 | 105 |
| stroke 45 | 18 % → 29 % | 128.5 px | 0.60 | 1.65 | 70 |
| stroke 46 | 27 % → 66 % | 635.4 px | 0.60 | 2.44 | 15 |
| stroke 47 | 32 % → 64 % | 973.9 px | 0.60 | 2.04 | 5 |
| stroke 48 | 31 % → 62 % | 581.3 px | 0.60 | 2.01 | 26 |
| stroke 49 | 11 % → 32 % | 151.5 px | 0.60 | 2.94 | 34 |
| stroke 50 | 35 % → 63 % | 740.5 px | 0.60 | 1.79 | 34 |
| stroke 51 | 38 % → 66 % | 584.8 px | 0.60 | 1.74 | 18 |
| stroke 52 | 17 % → 43 % | 312.7 px | 0.60 | 2.48 | 27 |
| stroke 53 | 17 % → 44 % | 279.7 px | 0.60 | 2.64 | 23 |
| stroke 54 | 18 % → 40 % | 452.0 px | 0.60 | 2.28 | 31 |
| stroke 55 | 30 % → 47 % | 567.4 px | 0.60 | 1.58 | 43 |
| stroke 56 | 35 % → 66 % | 1059.4 px | 0.60 | 1.92 | 15 |
| stroke 57 | 26 % → 53 % | 731.4 px | 0.60 | 2.04 | 19 |
| stroke 58 | 19 % → 39 % | 387.4 px | 0.60 | 1.98 | 20 |
| stroke 59 | 39 % → 68 % | 864.8 px | 0.60 | 1.73 | 23 |
| stroke 60 | 41 % → 62 % | 638.2 px | 0.60 | 1.50 | 61 |
| stroke 61 | 23 % → 47 % | 629.9 px | 0.60 | 2.07 | 19 |
| stroke 62 | 31 % → 42 % | 498.3 px | 0.60 | 1.35 | 68 |
| stroke 63 | 44 % → 69 % | 762.6 px | 0.60 | 1.58 | 45 |
| stroke 64 | 26 % → 44 % | 125.7 px | 0.60 | 1.68 | 149 |
| stroke 65 | 37 % → 58 % | 301.5 px | 0.60 | 1.57 | 78 |
| stroke 66 | 22 % → 40 % | 408.8 px | 0.60 | 1.79 | 64 |
| stroke 67 | 36 % → 51 % | 304.3 px | 0.60 | 1.41 | 87 |
| stroke 68 | 50 % → 67 % | 575.9 px | 0.60 | 1.35 | 49 |
| stroke 69 | 40 % → 63 % | 944.3 px | 0.60 | 1.58 | 31 |
| stroke 70 | 31 % → 44 % | 738.0 px | 0.60 | 1.41 | 24 |
| stroke 71 | 25 % → 38 % | 759.1 px | 0.60 | 1.53 | 15 |
| stroke 72 | 43 % → 63 % | 521.5 px | 0.60 | 1.46 | 47 |
| stroke 73 | 50 % → 69 % | 1476.0 px | 0.60 | 1.37 | 21 |
| stroke 74 | 38 % → 43 % | 148.6 px | 0.59 | 1.12 | 439 |
| stroke 75 | 38 % → 51 % | 841.0 px | 0.60 | 1.34 | 19 |
| stroke 76 | 55 % → 71 % | 1167.0 px | 0.60 | 1.28 | 36 |
| stroke 77 | 57 % → 66 % | 804.1 px | 0.60 | 1.15 | 28 |
| stroke 78 | 49 % → 61 % | 1175.9 px | 0.60 | 1.26 | 16 |
| stroke 79 | 43 % → 56 % | 1639.2 px | 0.60 | 1.29 | 23 |
| stroke 80 | 48 % → 60 % | 1246.5 px | 0.60 | 1.24 | 19 |
| stroke 81 | 39 % → 45 % | 340.4 px | 0.60 | 1.14 | 73 |
| stroke 82 | 42 % → 54 % | 747.3 px | 0.60 | 1.29 | 27 |
| stroke 83 | 50 % → 53 % | 1607.2 px | 0.60 | 1.08 | 17 |
| stroke 84 | 54 % → 66 % | 835.1 px | 0.60 | 1.23 | 37 |
| stroke 85 | 36 % → 38 % | 460.7 px | 0.60 | 1.06 | 33 |
| stroke 86 | 31 % → 38 % | 523.5 px | 0.60 | 1.25 | 20 |
| stroke 87 | 41 % → 47 % | 524.3 px | 0.60 | 1.15 | 48 |
| stroke 88 | 45 % → 54 % | 569.1 px | 0.60 | 1.19 | 82 |
| stroke 89 | 46 % → 57 % | 1306.7 px | 0.60 | 1.22 | 12 |
| stroke 90 | 30 % → 33 % | 687.1 px | 0.60 | 1.12 | 23 |
| stroke 91 | 38 % → 41 % | 705.9 px | 0.60 | 1.07 | 28 |
| stroke 92 | 58 % → 63 % | 1004.0 px | 0.60 | 1.08 | 29 |
| stroke 93 | 49 % → 55 % | 1446.0 px | 0.60 | 1.13 | 25 |
| stroke 94 | 38 % → 44 % | 448.1 px | 0.60 | 1.18 | 51 |
| stroke 95 | 59 % → 64 % | 1079.7 px | 0.60 | 1.09 | 26 |
| stroke 96 | 32 % → 35 % | 1010.9 px | 0.60 | 1.11 | 14 |
| stroke 97 | 41 % → 43 % | 308.0 px | 0.60 | 1.05 | 66 |
| stroke 98 | 60 % → 64 % | 2166.3 px | 0.60 | 1.05 | 13 |
| stroke 99 | 63 % → 68 % | 2283.5 px | 0.60 | 1.08 | 14 |
| stroke 100 | 45 % → 46 % | 803.9 px | 0.60 | 1.02 | 33 |
| stroke 101 | 56 % → 60 % | 1012.6 px | 0.60 | 1.07 | 122 |
| stroke 102 | 64 % → 68 % | 1264.6 px | 0.60 | 1.05 | 124 |
| stroke 103 | 29 % → 32 % | 1173.1 px | 0.60 | 1.09 | 12 |
| stroke 104 | 59 % → 65 % | 2242.1 px | 0.60 | 1.11 | 20 |
| stroke 105 | 56 % → 57 % | 1310.8 px | 0.60 | 1.03 | 74 |
| stroke 106 | 61 % → 65 % | 1264.7 px | 0.60 | 1.08 | 63 |
| stroke 107 | 60 % → 61 % | 1286.5 px | 0.60 | 1.02 | 121 |
| stroke 108 | 66 % → 67 % | 651.3 px | 0.60 | 1.02 | 119 |
| stroke 109 | 63 % → 63 % | 2119.2 px | 0.60 | 1.00 | 43 |
| stroke 110 | 40 % → 40 % | 709.6 px | 0.60 | 1.00 | 48 |
| stroke 111 | 62 % → 63 % | 1038.6 px | 0.60 | 1.02 | 67 |
| stroke 112 | 53 % → 55 % | 710.0 px | 0.60 | 1.03 | 55 |
| stroke 113 | 67 % → 67 % | 1463.4 px | 0.60 | 1.00 | 32 |
| stroke 114 | 38 % → 38 % | 664.2 px | 0.60 | 1.00 | 41 |
| stroke 115 | 31 % → 31 % | 609.0 px | 0.59 | 1.00 | 15 |

Numbers say: wet paint spreads well beyond the stroke.

## Refs v3 · #20 Orange crayon — own sheet
own sheet 800 × 1245 · Wax 1.00 · 48 px · 28.9 s

![Refs v3 · #20 Orange crayon — own sheet](Refs-v3-20-Orange-crayon-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 8 % → 68 % | 45.2 px | 0.55 | 8.07 | 33 |
| stroke 2 | 16 % → 79 % | 52.4 px | 0.55 | 4.99 | 74 |
| stroke 3 | 6 % → 46 % | 50.6 px | 0.55 | 7.82 | 25 |
| stroke 4 | 6 % → 30 % | 47.6 px | 0.55 | 5.27 | 29 |
| stroke 5 | 21 % → 85 % | 63.4 px | 0.55 | 4.03 | 151 |
| stroke 6 | 10 % → 54 % | 70.9 px | 0.55 | 5.67 | 64 |
| stroke 7 | 14 % → 41 % | 84.2 px | 0.55 | 2.92 | 55 |
| stroke 8 | 4 % → 12 % | 63.6 px | 0.55 | 2.78 | 29 |
| stroke 9 | 24 % → 88 % | 74.3 px | 0.55 | 3.61 | 256 |
| stroke 10 | 18 % → 52 % | 80.9 px | 0.55 | 2.90 | 154 |
| stroke 11 | 24 % → 77 % | 87.5 px | 0.55 | 3.27 | 457 |
| stroke 12 | 8 % → 20 % | 120.4 px | 0.55 | 2.55 | 20 |
| stroke 13 | 30 % → 81 % | 106.9 px | 0.55 | 2.69 | 543 |
| stroke 14 | 11 % → 30 % | 132.0 px | 0.55 | 2.71 | 45 |
| stroke 15 | 37 % → 84 % | 137.3 px | 0.55 | 2.28 | 477 |
| stroke 16 | 16 % → 43 % | 164.2 px | 0.55 | 2.73 | 36 |
| stroke 17 | 40 % → 86 % | 162.7 px | 0.55 | 2.11 | 559 |
| stroke 18 | 22 % → 57 % | 153.1 px | 0.55 | 2.64 | 47 |
| stroke 19 | 44 % → 86 % | 185.9 px | 0.55 | 1.98 | 465 |
| stroke 20 | 31 % → 71 % | 174.9 px | 0.55 | 2.28 | 61 |
| stroke 21 | 53 % → 94 % | 206.5 px | 0.55 | 1.78 | 265 |
| stroke 22 | 39 % → 82 % | 176.0 px | 0.55 | 2.09 | 116 |
| stroke 23 | 25 % → 44 % | 307.8 px | 0.55 | 1.77 | 31 |
| stroke 24 | 53 % → 95 % | 207.7 px | 0.55 | 1.79 | 429 |
| stroke 25 | 35 % → 73 % | 151.8 px | 0.55 | 2.07 | 220 |
| stroke 26 | 44 % → 85 % | 204.9 px | 0.55 | 1.96 | 475 |
| stroke 27 | 47 % → 89 % | 218.5 px | 0.55 | 1.89 | 1017 |
| stroke 28 | 49 % → 92 % | 227.3 px | 0.55 | 1.87 | 613 |
| stroke 29 | 41 % → 83 % | 203.0 px | 0.55 | 2.04 | 673 |
| stroke 30 | 56 % → 98 % | 232.9 px | 0.55 | 1.76 | 452 |
| stroke 31 | 39 % → 82 % | 173.5 px | 0.55 | 2.08 | 247 |
| stroke 32 | 17 % → 46 % | 214.3 px | 0.55 | 2.63 | 23 |
| stroke 33 | 57 % → 98 % | 228.5 px | 0.55 | 1.74 | 341 |
| stroke 34 | 52 % → 96 % | 235.6 px | 0.55 | 1.84 | 120 |
| stroke 35 | 25 % → 61 % | 158.8 px | 0.55 | 2.38 | 74 |
| stroke 36 | 56 % → 98 % | 225.7 px | 0.55 | 1.74 | 461 |
| stroke 37 | 46 % → 91 % | 206.1 px | 0.55 | 1.98 | 165 |
| stroke 38 | 35 % → 70 % | 248.5 px | 0.55 | 2.00 | 57 |
| stroke 39 | 43 % → 86 % | 217.2 px | 0.55 | 1.98 | 553 |
| stroke 40 | 44 % → 86 % | 221.6 px | 0.55 | 1.95 | 693 |
| stroke 41 | 45 % → 87 % | 227.5 px | 0.55 | 1.92 | 726 |
| stroke 42 | 47 % → 88 % | 231.7 px | 0.55 | 1.90 | 526 |
| stroke 43 | 48 % → 88 % | 235.1 px | 0.55 | 1.83 | 584 |
| stroke 44 | 50 % → 87 % | 234.4 px | 0.55 | 1.73 | 659 |
| stroke 45 | 54 % → 86 % | 231.4 px | 0.55 | 1.60 | 573 |
| stroke 46 | 61 % → 95 % | 254.3 px | 0.55 | 1.55 | 613 |
| stroke 47 | 46 % → 46 % | 228.1 px | 0.55 | 1.00 | 50 |
| stroke 48 | 65 % → 96 % | 253.6 px | 0.55 | 1.47 | 538 |
| stroke 49 | 62 % → 97 % | 235.7 px | 0.55 | 1.55 | 345 |
| stroke 50 | 75 % → 82 % | 307.0 px | 0.55 | 1.09 | 38 |
| stroke 51 | 66 % → 97 % | 231.6 px | 0.55 | 1.47 | 379 |
| stroke 52 | 79 % → 86 % | 479.2 px | 0.55 | 1.09 | 20 |
| stroke 53 | 73 % → 97 % | 232.6 px | 0.55 | 1.32 | 523 |
| stroke 54 | 72 % → 98 % | 221.2 px | 0.55 | 1.35 | 274 |
| stroke 55 | 89 % → 95 % | 392.8 px | 0.55 | 1.06 | 37 |
| stroke 56 | 79 % → 98 % | 219.1 px | 0.55 | 1.24 | 283 |
| stroke 57 | 83 % → 97 % | 214.5 px | 0.55 | 1.17 | 199 |
| stroke 58 | 86 % → 97 % | 206.6 px | 0.55 | 1.13 | 200 |
| stroke 59 | 91 % → 96 % | 215.4 px | 0.55 | 1.06 | 125 |
| stroke 60 | 95 % → 95 % | 251.2 px | 0.55 | 1.00 | 97 |

Numbers say: wet paint spreads well beyond the stroke.

## Refs v3 · #21 Gritty dog contours — own sheet
own sheet 800 × 1132 · Gouache 1.00 + water 15 % · 77 px · 47.0 s

![Refs v3 · #21 Gritty dog contours — own sheet](Refs-v3-21-Gritty-dog-contours-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 4 % → 0 % | 81.2 px | 0.00 | 0.00 | 102 |
| stroke 2 | 8 % → 2 % | 149.8 px | 0.37 | 0.23 | 48 |
| stroke 3 | 12 % → 2 % | 99.2 px | 0.37 | 0.15 | 248 |
| stroke 4 | 16 % → 2 % | 119.2 px | 0.38 | 0.12 | 429 |
| stroke 5 | 21 % → 0 % | 387.5 px | 0.00 | 0.00 | 83 |
| stroke 6 | 25 % → 3 % | 268.0 px | 0.38 | 0.13 | 186 |
| stroke 7 | 32 % → 0 % | 650.6 px | 0.00 | 0.00 | 53 |
| stroke 8 | 31 % → 4 % | 509.2 px | 0.38 | 0.13 | 110 |
| stroke 9 | 27 % → 4 % | 414.6 px | 0.38 | 0.14 | 129 |
| stroke 10 | 22 % → 4 % | 320.4 px | 0.38 | 0.16 | 115 |
| stroke 11 | 20 % → 2 % | 207.9 px | 0.38 | 0.12 | 184 |
| stroke 12 | 19 % → 2 % | 281.5 px | 0.39 | 0.09 | 83 |
| stroke 13 | 7 % → 0 % | 147.4 px | 0.00 | 0.00 | 59 |
| stroke 14 | 27 % → 0 % | 357.7 px | 0.00 | 0.00 | 197 |
| stroke 15 | 24 % → 1 % | 254.2 px | 0.40 | 0.04 | 184 |
| stroke 16 | 18 % → 0 % | 249.5 px | 0.00 | 0.00 | 118 |
| stroke 17 | 25 % → 1 % | 187.1 px | 0.40 | 0.06 | 283 |
| stroke 18 | 19 % → 0 % | 344.9 px | 0.00 | 0.00 | 82 |
| stroke 19 | 34 % → 2 % | 304.3 px | 0.40 | 0.06 | 431 |
| stroke 20 | 32 % → 2 % | 232.2 px | 0.39 | 0.06 | 337 |
| stroke 21 | 31 % → 0 % | 424.6 px | 0.00 | 0.00 | 79 |
| stroke 22 | 33 % → 3 % | 220.4 px | 0.38 | 0.09 | 518 |
| stroke 23 | 34 % → 4 % | 651.9 px | 0.39 | 0.12 | 118 |
| stroke 24 | 48 % → 5 % | 497.0 px | 0.38 | 0.10 | 168 |
| stroke 25 | 50 % → 2 % | 1090.8 px | 0.39 | 0.03 | 45 |
| stroke 26 | 34 % → 1 % | 650.4 px | 0.39 | 0.03 | 77 |
| stroke 27 | 30 % → 6 % | 577.7 px | 0.38 | 0.20 | 76 |
| stroke 28 | 47 % → 6 % | 465.4 px | 0.38 | 0.13 | 190 |
| stroke 29 | 51 % → 4 % | 1016.1 px | 0.39 | 0.07 | 48 |
| stroke 30 | 36 % → 2 % | 598.9 px | 0.39 | 0.04 | 89 |
| stroke 31 | 31 % → 8 % | 676.8 px | 0.38 | 0.26 | 84 |
| stroke 32 | 39 % → 5 % | 276.4 px | 0.38 | 0.12 | 510 |
| stroke 33 | 49 % → 9 % | 810.1 px | 0.39 | 0.17 | 75 |
| stroke 34 | 40 % → 10 % | 850.8 px | 0.38 | 0.25 | 41 |
| stroke 35 | 2 % → 0 % | 21.0 px | 0.31 | 0.02 | 38 |
| stroke 36 | 3 % → 0 % | 59.6 px | 0.00 | 0.00 | 25 |
| stroke 37 | 4 % → 1 % | 58.4 px | 0.39 | 0.23 | 48 |
| stroke 38 | 5 % → 1 % | 219.6 px | 0.39 | 0.19 | 13 |
| stroke 39 | 5 % → 1 % | 191.0 px | 0.39 | 0.19 | 12 |
| stroke 40 | 6 % → 0 % | 133.8 px | 0.22 | 0.00 | 28 |
| stroke 41 | 7 % → 0 % | 179.6 px | 0.00 | 0.00 | 22 |
| stroke 42 | 8 % → 0 % | 173.9 px | 0.00 | 0.00 | 22 |
| stroke 43 | 4 % → 1 % | 181.1 px | 0.39 | 0.28 | 7 |
| stroke 44 | 6 % → 2 % | 130.0 px | 0.39 | 0.26 | 10 |
| stroke 45 | 6 % → 2 % | 175.8 px | 0.40 | 0.30 | 8 |
| stroke 46 | 6 % → 2 % | 247.4 px | 0.39 | 0.34 | 6 |
| stroke 47 | 7 % → 2 % | 381.1 px | 0.39 | 0.32 | 3 |
| stroke 48 | 1 % → 0 % | 18.6 px | 0.00 | 0.00 | 22 |
| stroke 49 | 2 % → 0 % | 46.5 px | 0.00 | 0.00 | 3 |
| stroke 50 | 2 % → 0 % | 46.7 px | 0.00 | 0.00 | 12 |
| stroke 51 | 3 % → 0 % | 145.6 px | 0.00 | 0.00 | 5 |
| stroke 52 | 4 % → 0 % | 107.3 px | 0.00 | 0.00 | 11 |
| stroke 53 | 5 % → 0 % | 98.8 px | 0.00 | 0.00 | 17 |
| stroke 54 | 7 % → 0 % | 165.5 px | 0.00 | 0.00 | 16 |
| stroke 55 | 7 % → 0 % | 252.3 px | 0.00 | 0.00 | 9 |
| stroke 56 | 7 % → 2 % | 130.1 px | 0.37 | 0.24 | 22 |
| stroke 57 | 8 % → 0 % | 157.9 px | 0.00 | 0.00 | 21 |
| stroke 58 | 9 % → 2 % | 112.2 px | 0.37 | 0.26 | 31 |
| stroke 59 | 14 % → 0 % | 600.5 px | 0.00 | 0.00 | 8 |
| stroke 60 | 5 % → 0 % | 143.6 px | 0.00 | 0.00 | 15 |
| stroke 61 | 7 % → 0 % | 115.4 px | 0.00 | 0.00 | 17 |
| stroke 62 | 7 % → 0 % | 193.0 px | 0.00 | 0.00 | 7 |
| stroke 63 | 6 % → 0 % | 143.4 px | 0.00 | 0.00 | 16 |
| stroke 64 | 5 % → 0 % | 165.8 px | 0.00 | 0.00 | 8 |
| stroke 65 | 4 % → 1 % | 166.2 px | 0.35 | 0.32 | 10 |
| stroke 66 | 1 % → 4 % | 41.9 px | 0.38 | 4.04 | 4 |
| stroke 67 | 5 % → 0 % | 115.9 px | 0.00 | 0.00 | 19 |
| stroke 68 | 5 % → 1 % | 137.0 px | 0.38 | 0.20 | 17 |
| stroke 69 | 4 % → 0 % | 81.4 px | 0.00 | 0.00 | 23 |
| stroke 70 | 5 % → 3 % | 81.3 px | 0.40 | 0.58 | 26 |
| stroke 71 | 3 % → 1 % | 161.9 px | 0.39 | 0.37 | 4 |
| stroke 72 | 6 % → 3 % | 86.1 px | 0.39 | 0.55 | 23 |
| stroke 73 | 6 % → 7 % | 186.2 px | 0.38 | 1.05 | 13 |
| stroke 74 | 3 % → 1 % | 62.4 px | 0.39 | 0.52 | 16 |
| stroke 75 | 7 % → 6 % | 105.1 px | 0.39 | 0.85 | 26 |
| stroke 76 | 4 % → 5 % | 152.2 px | 0.39 | 1.13 | 6 |
| stroke 77 | 5 % → 2 % | 227.0 px | 0.39 | 0.41 | 5 |
| stroke 78 | 3 % → 5 % | 99.2 px | 0.40 | 1.54 | 3 |
| stroke 79 | 3 % → 13 % | 82.1 px | 0.39 | 5.22 | 6 |
| stroke 80 | 2 % → 0 % | 32.2 px | 0.00 | 0.00 | 34 |
| stroke 81 | 3 % → 0 % | 47.1 px | 0.00 | 0.00 | 62 |
| stroke 82 | 4 % → 0 % | 92.0 px | 0.00 | 0.00 | 29 |
| stroke 83 | 4 % → 4 % | 251.7 px | 0.38 | 1.05 | 3 |
| stroke 84 | 5 % → 2 % | 345.7 px | 0.36 | 0.43 | 7 |
| stroke 85 | 7 % → 1 % | 234.2 px | 0.35 | 0.17 | 25 |
| stroke 86 | 8 % → 0 % | 267.3 px | 0.32 | 0.05 | 7 |
| stroke 87 | 8 % → 0 % | 243.1 px | 0.25 | 0.00 | 14 |
| stroke 88 | 9 % → 0 % | 172.8 px | 0.00 | 0.00 | 22 |
| stroke 89 | 10 % → 0 % | 179.3 px | 0.00 | 0.00 | 24 |
| stroke 90 | 8 % → 0 % | 364.8 px | 0.00 | 0.00 | 6 |
| stroke 91 | 8 % → 0 % | 107.1 px | 0.00 | 0.00 | 36 |
| stroke 92 | 11 % → 0 % | 734.9 px | 0.00 | 0.00 | 6 |
| stroke 93 | 10 % → 0 % | 483.5 px | 0.00 | 0.00 | 9 |
| stroke 94 | 11 % → 0 % | 721.2 px | 0.00 | 0.00 | 3 |
| stroke 95 | 11 % → 0 % | 496.0 px | 0.00 | 0.00 | 17 |
| stroke 96 | 5 % → 3 % | 59.1 px | 0.38 | 0.62 | 89 |
| stroke 97 | 8 % → 3 % | 66.8 px | 0.38 | 0.34 | 107 |
| stroke 98 | 12 % → 3 % | 127.2 px | 0.38 | 0.29 | 101 |
| stroke 99 | 18 % → 5 % | 821.6 px | 0.38 | 0.27 | 31 |
| stroke 100 | 22 % → 0 % | 1345.7 px | 0.32 | 0.02 | 8 |
| stroke 101 | 20 % → 0 % | 486.6 px | 0.24 | 0.00 | 21 |
| stroke 102 | 7 % → 0 % | 504.6 px | 0.00 | 0.00 | 11 |
| stroke 103 | 19 % → 0 % | 217.6 px | 0.00 | 0.00 | 60 |
| stroke 104 | 21 % → 0 % | 305.1 px | 0.00 | 0.00 | 46 |
| stroke 105 | 23 % → 0 % | 451.4 px | 0.00 | 0.00 | 33 |
| stroke 106 | 27 % → 0 % | 1221.3 px | 0.00 | 0.00 | 47 |
| stroke 107 | 25 % → 0 % | 1173.4 px | 0.00 | 0.00 | 5 |
| stroke 108 | 25 % → 0 % | 895.6 px | 0.00 | 0.00 | 7 |
| stroke 109 | 30 % → 0 % | 2000.8 px | 0.00 | 0.00 | 5 |
| stroke 110 | 25 % → 0 % | 499.2 px | 0.00 | 0.00 | 23 |
| stroke 111 | 26 % → 0 % | 400.3 px | 0.00 | 0.00 | 42 |
| stroke 112 | 24 % → 0 % | 1505.5 px | 0.00 | 0.00 | 13 |
| stroke 113 | 25 % → 0 % | 1747.7 px | 0.00 | 0.00 | 2 |
| stroke 114 | 19 % → 0 % | 1236.8 px | 0.00 | 0.00 | 5 |
| stroke 115 | 17 % → 0 % | 599.1 px | 0.00 | 0.00 | 67 |
| stroke 116 | 17 % → 0 % | 257.0 px | 0.00 | 0.00 | 95 |
| stroke 117 | 16 % → 0 % | 360.2 px | 0.00 | 0.00 | 24 |
| stroke 118 | 7 % → 4 % | 158.1 px | 0.39 | 0.52 | 27 |
| stroke 119 | 7 % → 4 % | 155.7 px | 0.39 | 0.54 | 20 |
| stroke 120 | 7 % → 4 % | 141.2 px | 0.39 | 0.56 | 26 |
| stroke 121 | 2 % → 3 % | 21.0 px | 0.38 | 1.94 | 48 |
| stroke 122 | 3 % → 5 % | 118.1 px | 0.38 | 1.45 | 9 |
| stroke 123 | 2 % → 9 % | 32.5 px | 0.37 | 5.36 | 30 |
| stroke 124 | 3 % → 9 % | 65.5 px | 0.37 | 3.31 | 10 |
| stroke 125 | 5 % → 10 % | 56.6 px | 0.37 | 2.05 | 23 |
| stroke 126 | 6 % → 8 % | 187.4 px | 0.37 | 1.46 | 14 |
| stroke 127 | 7 % → 11 % | 116.3 px | 0.39 | 1.72 | 8 |
| stroke 128 | 3 % → 5 % | 56.6 px | 0.39 | 1.59 | 14 |

Numbers say: wet paint spreads well beyond the stroke.

## Refs v3 · #22 Wasilewski brush poster — own sheet
own sheet 800 × 1633 · Ink 0.98 · 64 px · 53.5 s

![Refs v3 · #22 Wasilewski brush poster — own sheet](Refs-v3-22-Wasilewski-brush-poster-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 2 % → 41 % | 90.3 px | 0.91 | 16.66 | 12 |
| stroke 2 | 4 % → 72 % | 94.9 px | 0.92 | 19.43 | 5 |
| stroke 3 | 10 % → 80 % | 41.6 px | 0.92 | 7.76 | 58 |
| stroke 4 | 2 % → 49 % | 92.2 px | 0.92 | 22.60 | 14 |
| stroke 5 | 4 % → 56 % | 61.1 px | 0.91 | 13.90 | 29 |
| stroke 6 | 3 % → 35 % | 84.7 px | 0.91 | 11.58 | 50 |
| stroke 7 | 2 % → 40 % | 67.6 px | 0.90 | 19.24 | 26 |
| stroke 8 | 6 % → 61 % | 226.9 px | 0.91 | 10.14 | 19 |
| stroke 9 | 6 % → 29 % | 208.7 px | 0.91 | 4.54 | 8 |
| stroke 10 | 6 % → 40 % | 165.4 px | 0.91 | 7.06 | 17 |
| stroke 11 | 9 % → 31 % | 125.0 px | 0.91 | 3.38 | 34 |
| stroke 12 | 7 % → 58 % | 166.0 px | 0.91 | 8.57 | 15 |
| stroke 13 | 8 % → 46 % | 306.5 px | 0.91 | 5.95 | 5 |
| stroke 14 | 10 % → 36 % | 307.8 px | 0.91 | 3.72 | 5 |
| stroke 15 | 3 % → 15 % | 88.1 px | 0.91 | 5.19 | 6 |
| stroke 16 | 6 % → 36 % | 285.3 px | 0.91 | 5.63 | 8 |
| stroke 17 | 14 % → 50 % | 126.7 px | 0.91 | 3.46 | 28 |
| stroke 18 | 3 % → 45 % | 80.4 px | 0.92 | 14.87 | 20 |
| stroke 19 | 1 % → 40 % | 59.9 px | 0.92 | 30.18 | 4 |
| stroke 20 | 9 % → 36 % | 109.4 px | 0.90 | 3.98 | 52 |
| stroke 21 | 16 % → 54 % | 321.8 px | 0.91 | 3.36 | 22 |
| stroke 22 | 4 % → 36 % | 140.3 px | 0.92 | 8.10 | 20 |
| stroke 23 | 17 % → 31 % | 95.0 px | 0.90 | 1.88 | 148 |
| stroke 24 | 19 % → 72 % | 741.9 px | 0.92 | 3.78 | 4 |
| stroke 25 | 6 % → 27 % | 201.5 px | 0.91 | 4.35 | 10 |
| stroke 26 | 4 % → 14 % | 143.7 px | 0.91 | 3.74 | 3 |
| stroke 27 | 2 % → 25 % | 69.0 px | 0.91 | 13.53 | 6 |
| stroke 28 | 9 % → 42 % | 233.7 px | 0.92 | 4.61 | 10 |
| stroke 29 | 12 % → 46 % | 442.1 px | 0.91 | 3.94 | 8 |
| stroke 30 | 6 % → 27 % | 71.7 px | 0.91 | 4.55 | 62 |
| stroke 31 | 7 % → 24 % | 178.4 px | 0.91 | 3.43 | 16 |
| stroke 32 | 13 % → 44 % | 236.8 px | 0.91 | 3.32 | 36 |
| stroke 33 | 28 % → 85 % | 438.8 px | 0.92 | 3.08 | 17 |
| stroke 34 | 9 % → 26 % | 160.5 px | 0.91 | 2.96 | 23 |
| stroke 35 | 10 % → 23 % | 223.9 px | 0.91 | 2.34 | 17 |
| stroke 36 | 7 % → 31 % | 111.3 px | 0.91 | 4.39 | 28 |
| stroke 37 | 10 % → 28 % | 112.9 px | 0.91 | 2.85 | 70 |
| stroke 38 | 16 % → 24 % | 106.2 px | 0.91 | 1.48 | 212 |
| stroke 39 | 18 % → 45 % | 193.5 px | 0.91 | 2.48 | 62 |
| stroke 40 | 12 % → 26 % | 476.9 px | 0.91 | 2.17 | 10 |
| stroke 41 | 23 % → 40 % | 252.6 px | 0.91 | 1.73 | 64 |
| stroke 42 | 13 % → 25 % | 226.6 px | 0.91 | 1.98 | 25 |
| stroke 43 | 20 % → 41 % | 286.5 px | 0.91 | 2.02 | 36 |
| stroke 44 | 17 % → 17 % | 179.7 px | 0.91 | 1.04 | 38 |
| stroke 45 | 22 % → 43 % | 239.1 px | 0.91 | 1.97 | 80 |
| stroke 46 | 30 % → 75 % | 771.2 px | 0.91 | 2.52 | 10 |
| stroke 47 | 25 % → 47 % | 1121.3 px | 0.91 | 1.89 | 10 |
| stroke 48 | 15 % → 26 % | 420.8 px | 0.91 | 1.69 | 31 |
| stroke 49 | 19 % → 49 % | 306.4 px | 0.91 | 2.65 | 22 |
| stroke 50 | 26 % → 54 % | 1079.2 px | 0.91 | 2.08 | 15 |
| stroke 51 | 41 % → 79 % | 898.0 px | 0.91 | 1.94 | 28 |
| stroke 52 | 12 % → 30 % | 158.9 px | 0.92 | 2.48 | 38 |
| stroke 53 | 39 % → 75 % | 698.3 px | 0.91 | 1.94 | 24 |
| stroke 54 | 42 % → 75 % | 673.0 px | 0.92 | 1.80 | 17 |
| stroke 55 | 31 % → 48 % | 270.9 px | 0.90 | 1.56 | 61 |
| stroke 56 | 26 % → 54 % | 577.6 px | 0.92 | 2.09 | 24 |
| stroke 57 | 33 % → 58 % | 554.6 px | 0.91 | 1.77 | 24 |
| stroke 58 | 20 % → 25 % | 327.8 px | 0.91 | 1.27 | 47 |
| stroke 59 | 13 % → 55 % | 158.1 px | 0.92 | 4.24 | 27 |
| stroke 60 | 19 % → 25 % | 285.5 px | 0.91 | 1.32 | 44 |
| stroke 61 | 29 % → 42 % | 383.9 px | 0.91 | 1.44 | 54 |
| stroke 62 | 19 % → 32 % | 255.2 px | 0.90 | 1.64 | 35 |
| stroke 63 | 47 % → 81 % | 724.4 px | 0.92 | 1.74 | 16 |
| stroke 64 | 32 % → 48 % | 196.4 px | 0.92 | 1.51 | 179 |
| stroke 65 | 20 % → 28 % | 665.5 px | 0.91 | 1.37 | 7 |
| stroke 66 | 28 % → 39 % | 481.1 px | 0.91 | 1.41 | 50 |
| stroke 67 | 19 % → 25 % | 621.0 px | 0.92 | 1.30 | 11 |
| stroke 68 | 24 % → 30 % | 469.7 px | 0.91 | 1.27 | 31 |
| stroke 69 | 6 % → 17 % | 240.9 px | 0.91 | 2.79 | 39 |
| stroke 70 | 37 % → 38 % | 435.3 px | 0.92 | 1.05 | 47 |
| stroke 71 | 25 % → 39 % | 1127.6 px | 0.92 | 1.53 | 8 |
| stroke 72 | 55 % → 75 % | 1063.7 px | 0.92 | 1.37 | 23 |
| stroke 73 | 46 % → 58 % | 539.0 px | 0.92 | 1.25 | 57 |
| stroke 74 | 61 % → 74 % | 1569.7 px | 0.92 | 1.21 | 20 |
| stroke 75 | 67 % → 84 % | 799.8 px | 0.92 | 1.24 | 22 |
| stroke 76 | 48 % → 61 % | 634.6 px | 0.91 | 1.27 | 69 |
| stroke 77 | 18 % → 25 % | 578.0 px | 0.91 | 1.39 | 12 |
| stroke 78 | 31 % → 47 % | 332.6 px | 0.91 | 1.52 | 87 |
| stroke 79 | 53 % → 68 % | 833.4 px | 0.92 | 1.27 | 40 |
| stroke 80 | 77 % → 88 % | 731.5 px | 0.92 | 1.14 | 32 |
| stroke 81 | 68 % → 75 % | 400.8 px | 0.92 | 1.11 | 46 |
| stroke 82 | 39 % → 59 % | 1104.2 px | 0.91 | 1.53 | 8 |
| stroke 83 | 38 % → 49 % | 666.8 px | 0.91 | 1.28 | 22 |
| stroke 84 | 32 % → 36 % | 462.8 px | 0.91 | 1.10 | 75 |
| stroke 85 | 6 % → 16 % | 146.6 px | 0.91 | 2.85 | 14 |
| stroke 86 | 40 % → 42 % | 334.3 px | 0.91 | 1.05 | 110 |
| stroke 87 | 50 % → 63 % | 1014.7 px | 0.91 | 1.26 | 17 |
| stroke 88 | 25 % → 29 % | 429.4 px | 0.91 | 1.15 | 23 |
| stroke 89 | 37 % → 38 % | 597.4 px | 0.91 | 1.04 | 64 |
| stroke 90 | 19 % → 24 % | 505.5 px | 0.90 | 1.27 | 13 |
| stroke 91 | 31 % → 37 % | 442.6 px | 0.91 | 1.20 | 58 |
| stroke 92 | 21 % → 25 % | 591.3 px | 0.91 | 1.19 | 30 |
| stroke 93 | 20 % → 23 % | 705.0 px | 0.91 | 1.15 | 14 |
| stroke 94 | 45 % → 49 % | 342.3 px | 0.91 | 1.08 | 87 |
| stroke 95 | 39 % → 40 % | 909.2 px | 0.91 | 1.01 | 27 |
| stroke 96 | 68 % → 72 % | 855.3 px | 0.91 | 1.06 | 138 |
| stroke 97 | 25 % → 28 % | 925.0 px | 0.91 | 1.12 | 8 |
| stroke 98 | 23 % → 24 % | 556.9 px | 0.91 | 1.06 | 18 |
| stroke 99 | 51 % → 52 % | 881.9 px | 0.91 | 1.02 | 28 |
| stroke 100 | 17 % → 20 % | 254.7 px | 0.91 | 1.20 | 56 |
| stroke 101 | 39 % → 41 % | 485.2 px | 0.92 | 1.06 | 33 |
| stroke 102 | 17 % → 18 % | 278.6 px | 0.91 | 1.06 | 33 |
| stroke 103 | 23 % → 23 % | 767.0 px | 0.90 | 1.02 | 13 |
| stroke 104 | 35 % → 35 % | 299.6 px | 0.91 | 1.01 | 130 |
| stroke 105 | 42 % → 42 % | 1875.9 px | 0.92 | 1.01 | 31 |
| stroke 106 | 49 % → 49 % | 1745.0 px | 0.91 | 1.01 | 24 |
| stroke 107 | 25 % → 25 % | 841.5 px | 0.91 | 1.01 | 14 |
| stroke 108 | 34 % → 34 % | 250.7 px | 0.91 | 1.02 | 107 |
| stroke 109 | 8 % → 28 % | 49.9 px | 0.92 | 3.51 | 51 |
| stroke 110 | 6 % → 30 % | 38.2 px | 0.90 | 4.84 | 26 |
| stroke 111 | 12 % → 36 % | 277.0 px | 0.92 | 3.04 | 5 |
| stroke 112 | 16 % → 28 % | 131.0 px | 0.91 | 1.80 | 70 |
| stroke 113 | 21 % → 22 % | 86.5 px | 0.91 | 1.08 | 235 |

Numbers say: wet paint spreads well beyond the stroke.

## Refs v3 · #23 Report dry white mask — own sheet
own sheet 800 × 804 · Ink 0.93 · Gouache 0.07 · 89 px · 43.0 s

![Refs v3 · #23 Report dry white mask — own sheet](Refs-v3-23-Report-dry-white-mask-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 9 % → 21 % | 83.8 px | 0.48 | 2.23 | 163 |
| stroke 2 | 12 % → 18 % | 93.9 px | 0.49 | 1.49 | 875 |
| stroke 3 | 16 % → 21 % | 138.9 px | 0.49 | 1.27 | 495 |
| stroke 4 | 20 % → 27 % | 253.0 px | 0.49 | 1.33 | 301 |
| stroke 5 | 37 % → 18 % | 487.8 px | 0.48 | 0.48 | 193 |
| stroke 6 | 22 % → 28 % | 259.3 px | 0.49 | 1.28 | 404 |
| stroke 7 | 36 % → 20 % | 838.1 px | 0.48 | 0.54 | 93 |
| stroke 8 | 23 % → 26 % | 248.1 px | 0.49 | 1.13 | 507 |
| stroke 9 | 23 % → 22 % | 260.4 px | 0.50 | 0.96 | 434 |
| stroke 10 | 44 % → 34 % | 750.7 px | 0.49 | 0.78 | 171 |
| stroke 11 | 22 % → 19 % | 393.4 px | 0.50 | 0.90 | 130 |
| stroke 12 | 37 % → 33 % | 593.9 px | 0.49 | 0.90 | 186 |
| stroke 13 | 23 % → 20 % | 287.7 px | 0.50 | 0.87 | 194 |
| stroke 14 | 34 % → 37 % | 513.7 px | 0.49 | 1.08 | 170 |
| stroke 15 | 24 % → 19 % | 274.9 px | 0.50 | 0.79 | 215 |
| stroke 16 | 35 % → 30 % | 453.4 px | 0.50 | 0.86 | 235 |
| stroke 17 | 30 % → 20 % | 303.2 px | 0.50 | 0.66 | 197 |
| stroke 18 | 42 % → 27 % | 871.6 px | 0.50 | 0.64 | 96 |
| stroke 19 | 34 % → 32 % | 909.0 px | 0.50 | 0.94 | 70 |
| stroke 20 | 44 % → 22 % | 368.2 px | 0.50 | 0.50 | 364 |
| stroke 21 | 48 % → 22 % | 408.2 px | 0.50 | 0.47 | 335 |
| stroke 22 | 45 % → 23 % | 399.0 px | 0.50 | 0.52 | 383 |
| stroke 23 | 39 % → 18 % | 558.2 px | 0.50 | 0.46 | 168 |
| stroke 24 | 83 % → 28 % | 2190.6 px | 0.50 | 0.33 | 86 |
| stroke 25 | 53 % → 27 % | 1113.1 px | 0.50 | 0.51 | 95 |
| stroke 26 | 59 % → 18 % | 708.6 px | 0.48 | 0.31 | 181 |
| stroke 27 | 1 % → 22 % | 38.2 px | 0.50 | 19.01 | 34 |
| stroke 28 | 2 % → 21 % | 46.7 px | 0.50 | 9.80 | 42 |
| stroke 29 | 3 % → 22 % | 184.9 px | 0.50 | 6.84 | 25 |
| stroke 30 | 4 % → 29 % | 52.7 px | 0.49 | 6.95 | 186 |
| stroke 31 | 8 % → 22 % | 472.1 px | 0.50 | 2.87 | 10 |
| stroke 32 | 6 % → 29 % | 77.5 px | 0.50 | 4.74 | 113 |
| stroke 33 | 10 % → 22 % | 579.7 px | 0.50 | 2.30 | 9 |
| stroke 34 | 10 % → 38 % | 237.4 px | 0.50 | 3.81 | 43 |
| stroke 35 | 11 % → 23 % | 655.3 px | 0.50 | 2.10 | 10 |
| stroke 36 | 12 % → 37 % | 338.9 px | 0.50 | 3.17 | 27 |
| stroke 37 | 12 % → 24 % | 556.6 px | 0.50 | 1.98 | 7 |
| stroke 38 | 13 % → 34 % | 340.2 px | 0.50 | 2.63 | 27 |
| stroke 39 | 14 % → 24 % | 838.8 px | 0.50 | 1.75 | 5 |
| stroke 40 | 13 % → 26 % | 256.8 px | 0.50 | 1.96 | 62 |
| stroke 41 | 14 % → 22 % | 230.4 px | 0.50 | 1.61 | 73 |
| stroke 42 | 1 % → 29 % | 33.2 px | 0.50 | 29.63 | 7 |
| stroke 43 | 16 % → 33 % | 981.6 px | 0.50 | 2.00 | 18 |
| stroke 44 | 5 % → 29 % | 76.4 px | 0.50 | 5.98 | 34 |
| stroke 45 | 16 % → 28 % | 166.6 px | 0.50 | 1.77 | 133 |
| stroke 46 | 9 % → 26 % | 366.8 px | 0.50 | 2.98 | 7 |
| stroke 47 | 22 % → 32 % | 1333.8 px | 0.50 | 1.45 | 16 |
| stroke 48 | 17 % → 27 % | 458.8 px | 0.50 | 1.60 | 20 |
| stroke 49 | 12 % → 25 % | 447.6 px | 0.50 | 2.09 | 14 |
| stroke 50 | 11 % → 24 % | 711.2 px | 0.50 | 2.18 | 3 |
| stroke 51 | 24 % → 32 % | 1496.2 px | 0.50 | 1.32 | 7 |
| stroke 52 | 13 % → 23 % | 279.6 px | 0.50 | 1.79 | 31 |
| stroke 53 | 25 % → 32 % | 1181.0 px | 0.50 | 1.25 | 16 |
| stroke 54 | 14 % → 22 % | 625.0 px | 0.50 | 1.54 | 14 |
| stroke 55 | 26 % → 31 % | 992.5 px | 0.50 | 1.21 | 39 |
| stroke 56 | 18 % → 23 % | 476.8 px | 0.50 | 1.28 | 38 |
| stroke 57 | 25 % → 28 % | 730.3 px | 0.50 | 1.11 | 37 |
| stroke 58 | 21 % → 24 % | 706.6 px | 0.50 | 1.13 | 11 |
| stroke 59 | 25 % → 26 % | 500.1 px | 0.50 | 1.04 | 57 |
| stroke 60 | 2 % → 14 % | 35.2 px | 0.50 | 7.36 | 34 |
| stroke 61 | 5 % → 12 % | 50.3 px | 0.50 | 2.18 | 82 |
| stroke 62 | 8 % → 13 % | 70.7 px | 0.50 | 1.60 | 103 |
| stroke 63 | 12 % → 16 % | 492.3 px | 0.50 | 1.33 | 17 |
| stroke 64 | 12 % → 21 % | 192.9 px | 0.50 | 1.84 | 15 |
| stroke 65 | 15 % → 17 % | 647.7 px | 0.50 | 1.13 | 10 |
| stroke 66 | 16 % → 18 % | 737.0 px | 0.50 | 1.08 | 43 |
| stroke 67 | 4 % → 15 % | 39.7 px | 0.48 | 3.66 | 179 |
| stroke 68 | 7 % → 19 % | 263.0 px | 0.48 | 2.71 | 103 |
| stroke 69 | 8 % → 17 % | 87.3 px | 0.48 | 2.20 | 84 |
| stroke 70 | 9 % → 20 % | 538.0 px | 0.48 | 2.07 | 13 |
| stroke 71 | 11 % → 19 % | 179.6 px | 0.49 | 1.83 | 44 |
| stroke 72 | 12 % → 21 % | 1009.2 px | 0.48 | 1.81 | 11 |
| stroke 73 | 13 % → 21 % | 301.2 px | 0.49 | 1.56 | 22 |
| stroke 74 | 13 % → 22 % | 803.9 px | 0.48 | 1.67 | 23 |
| stroke 75 | 16 % → 23 % | 471.2 px | 0.49 | 1.41 | 37 |
| stroke 76 | 17 % → 24 % | 545.3 px | 0.49 | 1.41 | 22 |
| stroke 77 | 20 % → 25 % | 742.8 px | 0.49 | 1.25 | 92 |
| stroke 78 | 22 % → 24 % | 249.2 px | 0.49 | 1.10 | 209 |
| stroke 79 | 3 % → 15 % | 62.6 px | 0.50 | 5.36 | 25 |
| stroke 80 | 3 % → 21 % | 144.0 px | 0.50 | 6.71 | 4 |
| stroke 81 | 7 % → 14 % | 49.6 px | 0.50 | 2.12 | 63 |
| stroke 82 | 7 % → 15 % | 574.6 px | 0.50 | 2.01 | 4 |
| stroke 83 | 10 % → 17 % | 69.2 px | 0.50 | 1.69 | 102 |
| stroke 84 | 9 % → 14 % | 703.8 px | 0.49 | 1.54 | 4 |
| stroke 85 | 22 % → 27 % | 346.0 px | 0.50 | 1.25 | 18 |
| stroke 86 | 10 % → 14 % | 901.5 px | 0.49 | 1.35 | 2 |
| stroke 87 | 10 % → 13 % | 880.4 px | 0.49 | 1.27 | 4 |
| stroke 88 | 11 % → 13 % | 676.5 px | 0.49 | 1.19 | 5 |
| stroke 89 | 12 % → 14 % | 1032.4 px | 0.49 | 1.13 | 15 |
| stroke 90 | 13 % → 14 % | 828.7 px | 0.49 | 1.08 | 9 |

Numbers say: wet paint spreads well beyond the stroke.

## Refs v3 · #24 Picasso flat oil — own sheet
own sheet 800 × 1155 · Gouache 1.00 + turpentine 20 % · 74 px · 97.6 s

![Refs v3 · #24 Picasso flat oil — own sheet](Refs-v3-24-Picasso-flat-oil-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 4 % → 2 % | 88.6 px | 0.01 | 0.50 | 63 |
| stroke 2 | 10 % → 2 % | 107.0 px | 0.01 | 0.16 | 115 |
| stroke 3 | 13 % → 2 % | 110.5 px | 0.01 | 0.13 | 228 |
| stroke 4 | 20 % → 2 % | 228.8 px | 0.01 | 0.08 | 190 |
| stroke 5 | 21 % → 1 % | 189.1 px | 0.01 | 0.06 | 360 |
| stroke 6 | 33 % → 2 % | 747.4 px | 0.01 | 0.06 | 56 |
| stroke 7 | 24 % → 1 % | 260.4 px | 0.01 | 0.03 | 135 |
| stroke 8 | 26 % → 0 % | 339.8 px | 0.00 | 0.00 | 165 |
| stroke 9 | 33 % → 2 % | 411.1 px | 0.01 | 0.05 | 106 |
| stroke 10 | 39 % → 3 % | 309.6 px | 0.01 | 0.09 | 286 |
| stroke 11 | 7 % → 2 % | 88.6 px | 0.05 | 0.25 | 205 |
| stroke 12 | 15 % → 1 % | 102.9 px | 0.05 | 0.07 | 250 |
| stroke 13 | 19 % → 1 % | 121.0 px | 0.05 | 0.06 | 191 |
| stroke 14 | 25 % → 1 % | 147.7 px | 0.05 | 0.05 | 226 |
| stroke 15 | 32 % → 0 % | 165.0 px | 0.07 | 0.01 | 407 |
| stroke 16 | 44 % → 0 % | 200.7 px | 0.00 | 0.00 | 317 |
| stroke 17 | 64 % → 0 % | 321.7 px | 0.00 | 0.00 | 142 |
| stroke 18 | 84 % → 0 % | 498.0 px | 0.00 | 0.00 | 147 |
| stroke 19 | 7 % → 0 % | 90.1 px | 0.00 | 0.00 | 79 |
| stroke 20 | 19 % → 0 % | 88.9 px | 0.00 | 0.00 | 256 |
| stroke 21 | 6 % → 2 % | 55.0 px | 0.02 | 0.39 | 166 |
| stroke 22 | 11 % → 1 % | 58.4 px | 0.02 | 0.11 | 1079 |
| stroke 23 | 16 % → 1 % | 98.9 px | 0.02 | 0.08 | 363 |
| stroke 24 | 19 % → 1 % | 116.4 px | 0.02 | 0.07 | 410 |
| stroke 25 | 21 % → 2 % | 184.7 px | 0.01 | 0.09 | 386 |
| stroke 26 | 20 % → 0 % | 387.0 px | 0.00 | 0.00 | 140 |
| stroke 27 | 22 % → 0 % | 309.6 px | 0.00 | 0.00 | 92 |
| stroke 28 | 8 % → 3 % | 126.4 px | 0.02 | 0.35 | 73 |
| stroke 29 | 44 % → 2 % | 398.4 px | 0.02 | 0.05 | 88 |
| stroke 30 | 46 % → 3 % | 846.7 px | 0.02 | 0.07 | 47 |
| stroke 31 | 34 % → 3 % | 917.7 px | 0.02 | 0.09 | 32 |
| stroke 32 | 3 % → 1 % | 67.9 px | 0.05 | 0.48 | 32 |
| stroke 33 | 5 % → 1 % | 79.3 px | 0.05 | 0.29 | 95 |
| stroke 34 | 1 % → 0 % | 23.1 px | 0.00 | 0.00 | 15 |
| stroke 35 | 3 % → 3 % | 30.1 px | 0.03 | 0.94 | 51 |
| stroke 36 | 7 % → 1 % | 64.8 px | 0.05 | 0.17 | 37 |
| stroke 37 | 9 % → 2 % | 101.2 px | 0.05 | 0.20 | 33 |
| stroke 38 | 9 % → 1 % | 200.1 px | 0.05 | 0.10 | 13 |
| stroke 39 | 1 % → 1 % | 29.1 px | 0.01 | 0.61 | 14 |
| stroke 40 | 2 % → 1 % | 33.9 px | 0.01 | 0.50 | 48 |
| stroke 41 | 4 % → 2 % | 37.3 px | 0.01 | 0.50 | 110 |
| stroke 42 | 5 % → 0 % | 185.9 px | 0.00 | 0.00 | 11 |
| stroke 43 | 6 % → 3 % | 91.7 px | 0.02 | 0.45 | 69 |
| stroke 44 | 7 % → 0 % | 251.4 px | 0.00 | 0.00 | 21 |
| stroke 45 | 7 % → 3 % | 103.0 px | 0.02 | 0.37 | 67 |
| stroke 46 | 8 % → 3 % | 173.4 px | 0.02 | 0.39 | 13 |
| stroke 47 | 7 % → 3 % | 155.7 px | 0.02 | 0.43 | 19 |
| stroke 48 | 7 % → 3 % | 107.8 px | 0.02 | 0.39 | 35 |
| stroke 49 | 7 % → 3 % | 138.3 px | 0.02 | 0.39 | 38 |
| stroke 50 | 10 % → 0 % | 236.3 px | 0.00 | 0.00 | 25 |
| stroke 51 | 11 % → 0 % | 243.6 px | 0.00 | 0.00 | 24 |
| stroke 52 | 11 % → 0 % | 230.0 px | 0.00 | 0.00 | 23 |
| stroke 53 | 16 % → 3 % | 186.6 px | 0.02 | 0.17 | 25 |
| stroke 54 | 16 % → 2 % | 167.0 px | 0.02 | 0.15 | 52 |
| stroke 55 | 22 % → 3 % | 584.8 px | 0.01 | 0.13 | 13 |
| stroke 56 | 23 % → 3 % | 1156.8 px | 0.01 | 0.13 | 4 |
| stroke 57 | 4 % → 3 % | 203.9 px | 0.02 | 0.85 | 12 |
| stroke 58 | 3 % → 3 % | 139.2 px | 0.02 | 1.20 | 8 |
| stroke 59 | 5 % → 3 % | 72.2 px | 0.02 | 0.52 | 43 |
| stroke 60 | 5 % → 3 % | 83.6 px | 0.02 | 0.58 | 39 |
| stroke 61 | 5 % → 3 % | 134.3 px | 0.02 | 0.52 | 19 |
| stroke 62 | 5 % → 2 % | 190.7 px | 0.02 | 0.32 | 7 |
| stroke 63 | 5 % → 4 % | 223.8 px | 0.01 | 0.83 | 14 |
| stroke 64 | 7 % → 1 % | 112.6 px | 0.02 | 0.20 | 27 |
| stroke 65 | 8 % → 2 % | 85.8 px | 0.02 | 0.21 | 86 |
| stroke 66 | 22 % → 3 % | 482.1 px | 0.02 | 0.14 | 18 |
| stroke 67 | 20 % → 3 % | 662.0 px | 0.02 | 0.17 | 18 |
| stroke 68 | 20 % → 3 % | 964.6 px | 0.02 | 0.17 | 14 |
| stroke 69 | 19 % → 3 % | 239.9 px | 0.02 | 0.14 | 84 |
| stroke 70 | 20 % → 3 % | 375.2 px | 0.02 | 0.15 | 38 |
| stroke 71 | 8 % → 0 % | 273.6 px | 0.01 | 0.01 | 13 |
| stroke 72 | 6 % → 2 % | 89.4 px | 0.02 | 0.28 | 58 |
| stroke 73 | 10 % → 2 % | 81.2 px | 0.02 | 0.20 | 89 |
| stroke 74 | 14 % → 2 % | 100.2 px | 0.02 | 0.12 | 178 |
| stroke 75 | 17 % → 2 % | 140.4 px | 0.02 | 0.11 | 115 |
| stroke 76 | 25 % → 2 % | 1187.4 px | 0.01 | 0.07 | 12 |
| stroke 77 | 9 % → 0 % | 98.7 px | 0.05 | 0.00 | 81 |
| stroke 78 | 11 % → 0 % | 100.7 px | 0.04 | 0.02 | 86 |
| stroke 79 | 12 % → 1 % | 121.6 px | 0.05 | 0.12 | 131 |
| stroke 80 | 14 % → 0 % | 364.2 px | 0.05 | 0.01 | 20 |
| stroke 81 | 13 % → 2 % | 355.7 px | 0.05 | 0.17 | 8 |
| stroke 82 | 15 % → 0 % | 424.6 px | 0.04 | 0.02 | 11 |
| stroke 83 | 2 % → 0 % | 23.1 px | 0.00 | 0.00 | 41 |
| stroke 84 | 1 % → 3 % | 24.6 px | 0.02 | 3.16 | 24 |
| stroke 85 | 3 % → 2 % | 32.7 px | 0.02 | 0.84 | 72 |
| stroke 86 | 3 % → 1 % | 127.7 px | 0.06 | 0.40 | 13 |
| stroke 87 | 5 % → 2 % | 55.7 px | 0.01 | 0.37 | 67 |
| stroke 88 | 12 % → 1 % | 71.5 px | 0.01 | 0.09 | 278 |
| stroke 89 | 15 % → 1 % | 87.7 px | 0.01 | 0.07 | 330 |
| stroke 90 | 20 % → 1 % | 152.9 px | 0.01 | 0.07 | 183 |
| stroke 91 | 21 % → 0 % | 558.4 px | 0.00 | 0.00 | 34 |
| stroke 92 | 18 % → 1 % | 139.1 px | 0.05 | 0.05 | 259 |
| stroke 93 | 24 % → 1 % | 138.7 px | 0.05 | 0.03 | 316 |
| stroke 94 | 27 % → 1 % | 152.8 px | 0.05 | 0.03 | 299 |
| stroke 95 | 28 % → 1 % | 270.8 px | 0.05 | 0.05 | 95 |
| stroke 96 | 16 % → 2 % | 131.4 px | 0.04 | 0.11 | 99 |
| stroke 97 | 25 % → 3 % | 136.1 px | 0.03 | 0.11 | 215 |
| stroke 98 | 33 % → 3 % | 184.3 px | 0.03 | 0.08 | 318 |
| stroke 99 | 46 % → 3 % | 362.4 px | 0.03 | 0.06 | 128 |
| stroke 100 | 27 % → 1 % | 427.9 px | 0.02 | 0.04 | 57 |
| stroke 101 | 32 % → 0 % | 1122.4 px | 0.00 | 0.00 | 17 |
| stroke 102 | 2 % → 0 % | 32.8 px | 0.00 | 0.00 | 23 |
| stroke 103 | 4 % → 0 % | 43.0 px | 0.00 | 0.00 | 30 |
| stroke 104 | 5 % → 0 % | 63.1 px | 0.00 | 0.00 | 26 |
| stroke 105 | 7 % → 0 % | 139.9 px | 0.00 | 0.00 | 11 |
| stroke 106 | 11 % → 0 % | 116.4 px | 0.00 | 0.00 | 17 |
| stroke 107 | 12 % → 0 % | 111.6 px | 0.00 | 0.00 | 26 |
| stroke 108 | 17 % → 0 % | 275.1 px | 0.00 | 0.00 | 6 |
| stroke 109 | 19 % → 0 % | 337.4 px | 0.00 | 0.00 | 8 |
| stroke 110 | 8 % → 0 % | 154.8 px | 0.00 | 0.00 | 13 |
| stroke 111 | 13 % → 0 % | 140.9 px | 0.00 | 0.00 | 20 |
| stroke 112 | 18 % → 0 % | 107.7 px | 0.00 | 0.00 | 71 |
| stroke 113 | 20 % → 0 % | 129.5 px | 0.00 | 0.00 | 48 |
| stroke 114 | 21 % → 0 % | 145.8 px | 0.00 | 0.00 | 78 |
| stroke 115 | 23 % → 0 % | 193.2 px | 0.00 | 0.00 | 48 |
| stroke 116 | 1 % → 2 % | 34.8 px | 0.01 | 3.11 | 18 |
| stroke 117 | 1 % → 2 % | 52.0 px | 0.01 | 1.50 | 15 |
| stroke 118 | 2 % → 2 % | 59.0 px | 0.01 | 0.91 | 25 |
| stroke 119 | 3 % → 2 % | 156.0 px | 0.01 | 0.70 | 5 |
| stroke 120 | 4 % → 2 % | 90.2 px | 0.01 | 0.50 | 17 |
| stroke 121 | 5 % → 2 % | 119.1 px | 0.01 | 0.43 | 15 |
| stroke 122 | 5 % → 2 % | 188.7 px | 0.01 | 0.38 | 22 |
| stroke 123 | 6 % → 1 % | 70.2 px | 0.01 | 0.25 | 108 |
| stroke 124 | 7 % → 1 % | 81.2 px | 0.01 | 0.20 | 94 |
| stroke 125 | 11 % → 2 % | 279.8 px | 0.01 | 0.18 | 15 |
| stroke 126 | 12 % → 2 % | 402.9 px | 0.01 | 0.18 | 25 |
| stroke 127 | 12 % → 2 % | 325.0 px | 0.01 | 0.17 | 27 |
| stroke 128 | 12 % → 2 % | 575.0 px | 0.01 | 0.19 | 6 |
| stroke 129 | 8 % → 1 % | 413.3 px | 0.01 | 0.15 | 4 |
| stroke 130 | 12 % → 2 % | 214.6 px | 0.01 | 0.14 | 87 |
| stroke 131 | 4 % → 0 % | 139.9 px | 0.01 | 0.02 | 16 |
| stroke 132 | 5 % → 0 % | 118.9 px | 0.01 | 0.08 | 34 |
| stroke 133 | 5 % → 0 % | 277.2 px | 0.01 | 0.05 | 13 |
| stroke 134 | 7 % → 1 % | 181.3 px | 0.01 | 0.10 | 20 |
| stroke 135 | 7 % → 1 % | 334.7 px | 0.01 | 0.18 | 10 |
| stroke 136 | 8 % → 2 % | 185.9 px | 0.01 | 0.25 | 19 |
| stroke 137 | 9 % → 3 % | 247.1 px | 0.01 | 0.28 | 29 |
| stroke 138 | 10 % → 3 % | 520.3 px | 0.01 | 0.28 | 7 |
| stroke 139 | 11 % → 3 % | 395.8 px | 0.01 | 0.30 | 23 |
| stroke 140 | 12 % → 4 % | 584.9 px | 0.02 | 0.30 | 10 |
| stroke 141 | 11 % → 3 % | 531.4 px | 0.02 | 0.31 | 8 |
| stroke 142 | 5 % → 0 % | 31.2 px | 0.00 | 0.00 | 40 |
| stroke 143 | 12 % → 0 % | 80.1 px | 0.00 | 0.00 | 39 |
| stroke 144 | 1 % → 2 % | 30.1 px | 0.01 | 2.05 | 17 |
| stroke 145 | 1 % → 2 % | 27.6 px | 0.05 | 1.12 | 16 |
| stroke 146 | 1 % → 0 % | 26.5 px | 0.00 | 0.00 | 58 |
| stroke 147 | 3 % → 2 % | 56.6 px | 0.05 | 0.63 | 10 |
| stroke 148 | 8 % → 0 % | 82.9 px | 0.00 | 0.00 | 145 |
| stroke 149 | 11 % → 0 % | 143.7 px | 0.00 | 0.00 | 104 |
| stroke 150 | 14 % → 0 % | 207.8 px | 0.00 | 0.00 | 83 |
| stroke 151 | 16 % → 0 % | 260.6 px | 0.00 | 0.00 | 175 |
| stroke 152 | 18 % → 0 % | 319.5 px | 0.00 | 0.00 | 97 |
| stroke 153 | 17 % → 0 % | 115.4 px | 0.00 | 0.00 | 302 |
| stroke 154 | 21 % → 0 % | 465.0 px | 0.00 | 0.00 | 76 |
| stroke 155 | 24 % → 0 % | 131.5 px | 0.00 | 0.00 | 353 |
| stroke 156 | 28 % → 0 % | 275.0 px | 0.00 | 0.00 | 279 |
| stroke 157 | 59 % → 0 % | 444.1 px | 0.00 | 0.00 | 271 |
| stroke 158 | 26 % → 0 % | 251.1 px | 0.00 | 0.00 | 183 |
| stroke 159 | 30 % → 0 % | 203.9 px | 0.02 | 0.00 | 263 |
| stroke 160 | 31 % → 0 % | 246.3 px | 0.00 | 0.00 | 419 |
| stroke 161 | 29 % → 0 % | 420.9 px | 0.00 | 0.00 | 117 |
| stroke 162 | 10 % → 0 % | 88.7 px | 0.00 | 0.00 | 136 |
| stroke 163 | 14 % → 0 % | 102.0 px | 0.00 | 0.00 | 382 |
| stroke 164 | 29 % → 2 % | 178.6 px | 0.02 | 0.06 | 580 |
| stroke 165 | 26 % → 0 % | 168.3 px | 0.02 | 0.00 | 376 |
| stroke 166 | 34 % → 0 % | 224.5 px | 0.00 | 0.00 | 387 |
| stroke 167 | 33 % → 0 % | 227.4 px | 0.00 | 0.00 | 333 |
| stroke 168 | 32 % → 0 % | 212.2 px | 0.00 | 0.00 | 429 |
| stroke 169 | 31 % → 0 % | 205.7 px | 0.00 | 0.00 | 345 |
| stroke 170 | 35 % → 0 % | 216.1 px | 0.00 | 0.00 | 501 |
| stroke 171 | 40 % → 0 % | 204.6 px | 0.00 | 0.00 | 288 |
| stroke 172 | 44 % → 0 % | 250.3 px | 0.00 | 0.00 | 492 |
| stroke 173 | 45 % → 0 % | 375.0 px | 0.00 | 0.00 | 168 |
| stroke 174 | 45 % → 0 % | 620.0 px | 0.00 | 0.00 | 132 |
| stroke 175 | 6 % → 2 % | 86.5 px | 0.01 | 0.37 | 67 |
| stroke 176 | 12 % → 0 % | 92.4 px | 0.06 | 0.02 | 327 |
| stroke 177 | 21 % → 1 % | 106.4 px | 0.01 | 0.06 | 490 |
| stroke 178 | 30 % → 1 % | 137.0 px | 0.01 | 0.04 | 631 |
| stroke 179 | 43 % → 0 % | 170.0 px | 0.01 | 0.00 | 585 |
| stroke 180 | 60 % → 0 % | 229.2 px | 0.00 | 0.00 | 394 |
| stroke 181 | 1 % → 0 % | 19.6 px | 0.01 | 0.11 | 29 |
| stroke 182 | 3 % → 2 % | 76.1 px | 0.01 | 0.67 | 13 |
| stroke 183 | 2 % → 0 % | 52.4 px | 0.00 | 0.00 | 9 |
| stroke 184 | 3 % → 0 % | 85.7 px | 0.00 | 0.00 | 21 |
| stroke 185 | 9 % → 0 % | 80.5 px | 0.00 | 0.00 | 24 |
| stroke 186 | 7 % → 0 % | 97.3 px | 0.00 | 0.00 | 54 |
| stroke 187 | 11 % → 0 % | 67.9 px | 0.00 | 0.00 | 76 |
| stroke 188 | 14 % → 0 % | 109.3 px | 0.00 | 0.00 | 75 |
| stroke 189 | 24 % → 0 % | 365.9 px | 0.00 | 0.00 | 40 |
| stroke 190 | 18 % → 0 % | 294.0 px | 0.00 | 0.00 | 26 |
| stroke 191 | 19 % → 0 % | 429.3 px | 0.00 | 0.00 | 17 |
| stroke 192 | 20 % → 0 % | 335.2 px | 0.00 | 0.00 | 13 |
| stroke 193 | 21 % → 0 % | 753.1 px | 0.00 | 0.00 | 27 |
| stroke 194 | 22 % → 0 % | 304.1 px | 0.00 | 0.00 | 37 |
| stroke 195 | 24 % → 0 % | 276.0 px | 0.00 | 0.00 | 66 |
| stroke 196 | 2 % → 2 % | 40.2 px | 0.01 | 0.79 | 64 |
| stroke 197 | 3 % → 2 % | 149.9 px | 0.01 | 0.72 | 9 |
| stroke 198 | 5 % → 1 % | 190.2 px | 0.01 | 0.27 | 24 |
| stroke 199 | 6 % → 1 % | 120.3 px | 0.01 | 0.15 | 30 |
| stroke 200 | 8 % → 1 % | 289.3 px | 0.01 | 0.15 | 11 |
| stroke 201 | 9 % → 2 % | 302.2 px | 0.01 | 0.20 | 13 |
| stroke 202 | 9 % → 1 % | 80.6 px | 0.01 | 0.09 | 94 |
| stroke 203 | 11 % → 0 % | 102.1 px | 0.01 | 0.04 | 113 |
| stroke 204 | 13 % → 0 % | 132.1 px | 0.01 | 0.01 | 113 |
| stroke 205 | 15 % → 0 % | 156.8 px | 0.02 | 0.00 | 88 |
| stroke 206 | 17 % → 0 % | 186.9 px | 0.00 | 0.00 | 94 |
| stroke 207 | 19 % → 0 % | 206.8 px | 0.00 | 0.00 | 89 |
| stroke 208 | 21 % → 0 % | 273.4 px | 0.00 | 0.00 | 114 |
| stroke 209 | 22 % → 0 % | 343.5 px | 0.00 | 0.00 | 63 |
| stroke 210 | 26 % → 0 % | 902.9 px | 0.00 | 0.00 | 15 |
| stroke 211 | 4 % → 0 % | 40.5 px | 0.00 | 0.00 | 69 |
| stroke 212 | 6 % → 0 % | 64.0 px | 0.02 | 0.00 | 128 |
| stroke 213 | 8 % → 1 % | 72.0 px | 0.01 | 0.10 | 119 |
| stroke 214 | 10 % → 0 % | 322.5 px | 0.00 | 0.00 | 14 |
| stroke 215 | 11 % → 2 % | 115.8 px | 0.02 | 0.19 | 98 |
| stroke 216 | 12 % → 3 % | 516.0 px | 0.02 | 0.23 | 12 |
| stroke 217 | 10 % → 3 % | 471.5 px | 0.02 | 0.27 | 15 |
| stroke 218 | 15 % → 2 % | 140.2 px | 0.02 | 0.16 | 150 |
| stroke 219 | 14 % → 3 % | 719.9 px | 0.02 | 0.24 | 7 |
| stroke 220 | 14 % → 3 % | 509.6 px | 0.02 | 0.23 | 26 |
| stroke 221 | 15 % → 3 % | 409.4 px | 0.01 | 0.17 | 25 |
| stroke 222 | 14 % → 2 % | 252.2 px | 0.01 | 0.15 | 64 |
| stroke 223 | 13 % → 2 % | 253.3 px | 0.01 | 0.16 | 48 |
| stroke 224 | 10 % → 2 % | 353.8 px | 0.01 | 0.15 | 25 |
| stroke 225 | 4 % → 0 % | 54.2 px | 0.03 | 0.04 | 66 |
| stroke 226 | 8 % → 0 % | 212.1 px | 0.01 | 0.06 | 36 |
| stroke 227 | 8 % → 0 % | 315.4 px | 0.00 | 0.00 | 18 |
| stroke 228 | 12 % → 0 % | 213.5 px | 0.00 | 0.00 | 23 |
| stroke 229 | 13 % → 0 % | 450.7 px | 0.01 | 0.02 | 14 |
| stroke 230 | 12 % → 0 % | 107.4 px | 0.00 | 0.00 | 116 |
| stroke 231 | 17 % → 0 % | 602.6 px | 0.01 | 0.01 | 22 |
| stroke 232 | 20 % → 0 % | 936.2 px | 0.00 | 0.00 | 15 |
| stroke 233 | 22 % → 0 % | 989.8 px | 0.01 | 0.00 | 14 |
| stroke 234 | 2 % → 1 % | 50.4 px | 0.05 | 0.67 | 19 |
| stroke 235 | 5 % → 3 % | 43.9 px | 0.03 | 0.52 | 102 |
| stroke 236 | 7 % → 3 % | 94.0 px | 0.03 | 0.45 | 102 |
| stroke 237 | 9 % → 2 % | 169.4 px | 0.02 | 0.20 | 54 |
| stroke 238 | 10 % → 1 % | 262.0 px | 0.01 | 0.07 | 39 |
| stroke 239 | 21 % → 2 % | 214.5 px | 0.02 | 0.11 | 113 |
| stroke 240 | 22 % → 2 % | 286.8 px | 0.02 | 0.09 | 106 |
| stroke 241 | 2 % → 2 % | 26.5 px | 0.01 | 1.24 | 48 |
| stroke 242 | 2 % → 3 % | 25.2 px | 0.02 | 1.34 | 54 |
| stroke 243 | 1 % → 2 % | 24.4 px | 0.05 | 1.94 | 6 |

Numbers say: wet paint spreads well beyond the stroke.

## Refs v3 · #25 Yellow heavy stroke — own sheet
own sheet 800 × 1198 · Impasto 1.00 · 272 px · 21.7 s

![Refs v3 · #25 Yellow heavy stroke — own sheet](Refs-v3-25-Yellow-heavy-stroke-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 23 % → 9 % | 222.1 px | 0.14 | 0.39 | 12513 |

## Refs v3 · #26 Ink caricature — own sheet
own sheet 800 × 1065 · Ink 0.98 · 64 px · 25.5 s

![Refs v3 · #26 Ink caricature — own sheet](Refs-v3-26-Ink-caricature-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 8 % → 23 % | 21.7 px | 0.73 | 2.95 | 99 |
| stroke 2 | 3 % → 47 % | 65.4 px | 0.76 | 14.41 | 43 |
| stroke 3 | 9 % → 34 % | 52.6 px | 0.76 | 3.80 | 203 |
| stroke 4 | 5 % → 54 % | 160.6 px | 0.76 | 11.57 | 3 |
| stroke 5 | 6 % → 37 % | 32.0 px | 0.75 | 5.78 | 196 |
| stroke 6 | 10 % → 40 % | 325.0 px | 0.76 | 3.94 | 7 |
| stroke 7 | 8 % → 45 % | 79.7 px | 0.76 | 5.34 | 31 |
| stroke 8 | 17 % → 38 % | 118.3 px | 0.75 | 2.29 | 177 |
| stroke 9 | 15 % → 31 % | 102.5 px | 0.77 | 2.15 | 145 |
| stroke 10 | 1 % → 28 % | 29.9 px | 0.74 | 21.79 | 5 |
| stroke 11 | 19 % → 48 % | 135.6 px | 0.76 | 2.52 | 60 |
| stroke 12 | 16 % → 52 % | 288.4 px | 0.76 | 3.19 | 15 |
| stroke 13 | 19 % → 45 % | 130.7 px | 0.75 | 2.33 | 78 |
| stroke 14 | 28 % → 51 % | 362.4 px | 0.76 | 1.85 | 26 |
| stroke 15 | 34 % → 48 % | 546.7 px | 0.76 | 1.41 | 37 |
| stroke 16 | 25 % → 45 % | 503.7 px | 0.76 | 1.81 | 38 |
| stroke 17 | 36 % → 48 % | 301.4 px | 0.76 | 1.35 | 93 |
| stroke 18 | 45 % → 50 % | 802.3 px | 0.76 | 1.12 | 44 |
| stroke 19 | 22 % → 31 % | 129.3 px | 0.75 | 1.40 | 331 |
| stroke 20 | 37 % → 42 % | 657.4 px | 0.76 | 1.12 | 29 |
| stroke 21 | 22 % → 40 % | 591.5 px | 0.74 | 1.79 | 11 |
| stroke 22 | 37 % → 43 % | 319.7 px | 0.75 | 1.16 | 122 |
| stroke 23 | 20 % → 26 % | 241.0 px | 0.73 | 1.27 | 6 |
| stroke 24 | 34 % → 38 % | 160.4 px | 0.76 | 1.11 | 202 |
| stroke 25 | 38 % → 42 % | 412.4 px | 0.75 | 1.09 | 25 |
| stroke 26 | 56 % → 60 % | 990.0 px | 0.76 | 1.07 | 17 |
| stroke 27 | 10 % → 28 % | 78.9 px | 0.74 | 2.91 | 81 |
| stroke 28 | 9 % → 23 % | 76.9 px | 0.73 | 2.75 | 60 |
| stroke 29 | 19 % → 34 % | 170.4 px | 0.73 | 1.83 | 45 |
| stroke 30 | 26 % → 33 % | 812.1 px | 0.74 | 1.29 | 21 |
| stroke 31 | 14 % → 27 % | 116.8 px | 0.74 | 2.01 | 79 |
| stroke 32 | 13 % → 21 % | 96.2 px | 0.74 | 1.65 | 102 |
| stroke 33 | 19 % → 31 % | 348.6 px | 0.73 | 1.64 | 14 |
| stroke 34 | 7 % → 16 % | 61.2 px | 0.73 | 2.24 | 47 |
| stroke 35 | 18 % → 33 % | 242.7 px | 0.73 | 1.80 | 33 |
| stroke 36 | 15 % → 26 % | 121.8 px | 0.73 | 1.79 | 130 |
| stroke 37 | 13 % → 25 % | 140.7 px | 0.73 | 1.89 | 19 |
| stroke 38 | 13 % → 25 % | 125.2 px | 0.72 | 1.86 | 25 |
| stroke 39 | 15 % → 23 % | 136.1 px | 0.73 | 1.50 | 23 |
| stroke 40 | 19 % → 24 % | 201.6 px | 0.72 | 1.29 | 27 |
| stroke 41 | 13 % → 17 % | 76.3 px | 0.73 | 1.23 | 57 |
| stroke 42 | 4 % → 6 % | 11.8 px | 0.75 | 1.65 | 44 |

Numbers say: wet paint spreads well beyond the stroke.

## Refs v3 · #27 Orange impasto swatch — own sheet
own sheet 800 × 1000 · Impasto 1.00 · 80 px · 14.9 s

![Refs v3 · #27 Orange impasto swatch — own sheet](Refs-v3-27-Orange-impasto-swatch-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 6 % → 1 % | 76.3 px | 0.25 | 0.18 | 188 |
| stroke 2 | 10 % → 1 % | 93.5 px | 0.25 | 0.08 | 304 |
| stroke 3 | 14 % → 1 % | 122.4 px | 0.25 | 0.05 | 336 |
| stroke 4 | 17 % → 1 % | 154.5 px | 0.25 | 0.04 | 339 |
| stroke 5 | 19 % → 0 % | 490.4 px | 0.00 | 0.00 | 42 |
| stroke 6 | 19 % → 1 % | 150.8 px | 0.25 | 0.03 | 854 |
| stroke 7 | 23 % → 1 % | 179.5 px | 0.25 | 0.02 | 641 |
| stroke 8 | 33 % → 1 % | 276.1 px | 0.26 | 0.02 | 384 |
| stroke 9 | 36 % → 0 % | 325.4 px | 0.27 | 0.01 | 293 |
| stroke 10 | 38 % → 0 % | 451.7 px | 0.27 | 0.01 | 148 |
| stroke 11 | 35 % → 0 % | 425.8 px | 0.00 | 0.00 | 151 |
| stroke 12 | 33 % → 0 % | 476.1 px | 0.00 | 0.00 | 136 |
| stroke 13 | 31 % → 0 % | 312.4 px | 0.00 | 0.00 | 224 |
| stroke 14 | 29 % → 0 % | 270.7 px | 0.00 | 0.00 | 312 |
| stroke 15 | 29 % → 0 % | 268.2 px | 0.00 | 0.00 | 310 |
| stroke 16 | 31 % → 0 % | 374.1 px | 0.00 | 0.00 | 244 |
| stroke 17 | 32 % → 0 % | 515.6 px | 0.00 | 0.00 | 93 |
| stroke 18 | 3 % → 0 % | 72.0 px | 0.00 | 0.00 | 52 |
| stroke 19 | 4 % → 0 % | 59.9 px | 0.15 | 0.00 | 105 |
| stroke 20 | 6 % → 0 % | 91.1 px | 0.28 | 0.06 | 106 |
| stroke 21 | 8 % → 1 % | 128.6 px | 0.27 | 0.08 | 90 |
| stroke 22 | 11 % → 1 % | 171.6 px | 0.27 | 0.07 | 132 |
| stroke 23 | 14 % → 1 % | 332.8 px | 0.27 | 0.06 | 49 |
| stroke 24 | 1 % → 1 % | 22.4 px | 0.25 | 0.93 | 42 |
| stroke 25 | 1 % → 1 % | 25.0 px | 0.27 | 0.95 | 19 |

## Refs v3 · #28 Miles Davis lines — own sheet
own sheet 800 × 753 · Ink 0.98 · 18 px · 33.9 s

![Refs v3 · #28 Miles Davis lines — own sheet](Refs-v3-28-Miles-Davis-lines-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 6 % → 0 % | 8.1 px | 0.00 | 0.00 | 4 |
| stroke 2 | 3 % → 0 % | 8.8 px | 0.00 | 0.00 | 1 |
| stroke 3 | 9 % → 0 % | 20.3 px | 0.00 | 0.00 | 2 |
| stroke 4 | 15 % → 0 % | 19.4 px | 0.00 | 0.00 | 12 |
| stroke 5 | 8 % → 0 % | 11.8 px | 0.00 | 0.00 | 8 |
| stroke 6 | 8 % → 0 % | 9.8 px | 0.00 | 0.00 | 6 |
| stroke 7 | 7 % → 0 % | 14.3 px | 0.00 | 0.00 | 2 |
| stroke 8 | 5 % → 36 % | 11.2 px | 0.81 | 6.51 | 4 |
| stroke 9 | 3 % → 69 % | 7.1 px | 0.86 | 23.40 | 3 |
| stroke 10 | 4 % → 88 % | 8.7 px | 0.89 | 24.39 | 11 |
| stroke 11 | 2 % → 82 % | 6.4 px | 0.88 | 45.49 | 3 |
| stroke 12 | 4 % → 30 % | 10.9 px | 0.85 | 7.79 | 5 |
| stroke 13 | 5 % → 91 % | 9.1 px | 0.89 | 19.22 | 5 |
| stroke 14 | 12 % → 91 % | 20.8 px | 0.87 | 7.39 | 7 |
| stroke 15 | 6 % → 70 % | 15.7 px | 0.86 | 11.45 | 6 |
| stroke 16 | 4 % → 80 % | 13.1 px | 0.87 | 19.07 | 5 |
| stroke 17 | 23 % → 37 % | 31.6 px | 0.88 | 1.58 | 48 |
| stroke 18 | 9 % → 28 % | 19.0 px | 0.86 | 3.12 | 16 |
| stroke 19 | 9 % → 42 % | 16.3 px | 0.86 | 4.81 | 11 |
| stroke 20 | 8 % → 56 % | 15.5 px | 0.86 | 6.78 | 29 |
| stroke 21 | 21 % → 84 % | 31.0 px | 0.89 | 3.93 | 67 |
| stroke 22 | 15 % → 52 % | 46.5 px | 0.89 | 3.51 | 9 |
| stroke 23 | 8 % → 74 % | 15.0 px | 0.85 | 9.47 | 20 |
| stroke 24 | 16 % → 68 % | 28.1 px | 0.85 | 4.26 | 10 |
| stroke 25 | 23 % → 49 % | 27.0 px | 0.85 | 2.11 | 72 |
| stroke 26 | 10 % → 17 % | 21.8 px | 0.87 | 1.64 | 121 |
| stroke 27 | 20 % → 46 % | 28.8 px | 0.88 | 2.30 | 140 |
| stroke 28 | 11 % → 77 % | 50.3 px | 0.88 | 6.77 | 8 |
| stroke 29 | 30 % → 56 % | 48.6 px | 0.89 | 1.88 | 24 |
| stroke 30 | 15 % → 63 % | 19.8 px | 0.86 | 4.21 | 19 |
| stroke 31 | 26 % → 84 % | 33.9 px | 0.87 | 3.24 | 23 |
| stroke 32 | 61 % → 89 % | 75.8 px | 0.88 | 1.45 | 47 |
| stroke 33 | 25 % → 41 % | 30.9 px | 0.87 | 1.65 | 72 |
| stroke 34 | 21 % → 33 % | 41.5 px | 0.87 | 1.53 | 168 |
| stroke 35 | 14 % → 19 % | 30.8 px | 0.88 | 1.34 | 106 |
| stroke 36 | 17 % → 55 % | 71.5 px | 0.85 | 3.21 | 2 |
| stroke 37 | 21 % → 91 % | 57.7 px | 0.89 | 4.32 | 14 |
| stroke 38 | 26 % → 67 % | 55.8 px | 0.88 | 2.52 | 14 |
| stroke 39 | 9 % → 77 % | 30.7 px | 0.89 | 8.53 | 4 |
| stroke 40 | 5 % → 81 % | 21.6 px | 0.88 | 17.45 | 2 |
| stroke 41 | 11 % → 68 % | 21.3 px | 0.85 | 6.00 | 10 |
| stroke 42 | 28 % → 64 % | 50.5 px | 0.88 | 2.29 | 18 |
| stroke 43 | 9 % → 69 % | 27.9 px | 0.86 | 7.78 | 7 |
| stroke 44 | 8 % → 73 % | 32.7 px | 0.88 | 8.75 | 5 |
| stroke 45 | 13 % → 73 % | 29.3 px | 0.88 | 5.73 | 14 |
| stroke 46 | 22 % → 72 % | 49.9 px | 0.87 | 3.30 | 21 |
| stroke 47 | 11 % → 81 % | 29.8 px | 0.88 | 7.13 | 21 |
| stroke 48 | 29 % → 74 % | 73.4 px | 0.87 | 2.56 | 12 |
| stroke 49 | 26 % → 74 % | 90.2 px | 0.88 | 2.87 | 4 |
| stroke 50 | 32 % → 74 % | 81.9 px | 0.88 | 2.28 | 5 |
| stroke 51 | 28 % → 79 % | 47.3 px | 0.88 | 2.79 | 30 |
| stroke 52 | 22 % → 65 % | 40.1 px | 0.87 | 2.88 | 49 |
| stroke 53 | 23 % → 73 % | 73.2 px | 0.88 | 3.15 | 12 |
| stroke 54 | 25 % → 70 % | 38.6 px | 0.86 | 2.78 | 33 |
| stroke 55 | 41 % → 83 % | 90.3 px | 0.88 | 2.01 | 9 |
| stroke 56 | 49 % → 89 % | 166.1 px | 0.89 | 1.83 | 8 |
| stroke 57 | 25 % → 64 % | 51.0 px | 0.88 | 2.57 | 8 |
| stroke 58 | 50 % → 83 % | 146.9 px | 0.89 | 1.67 | 5 |
| stroke 59 | 55 % → 75 % | 159.8 px | 0.88 | 1.37 | 12 |
| stroke 60 | 21 % → 68 % | 56.5 px | 0.88 | 3.28 | 9 |
| stroke 61 | 30 % → 77 % | 77.1 px | 0.88 | 2.57 | 12 |
| stroke 62 | 29 % → 71 % | 85.9 px | 0.89 | 2.41 | 14 |
| stroke 63 | 23 % → 66 % | 105.2 px | 0.88 | 2.82 | 2 |
| stroke 64 | 22 % → 66 % | 46.9 px | 0.86 | 2.99 | 20 |
| stroke 65 | 21 % → 58 % | 48.1 px | 0.87 | 2.69 | 9 |
| stroke 66 | 39 % → 59 % | 115.5 px | 0.86 | 1.52 | 13 |
| stroke 67 | 42 % → 84 % | 166.8 px | 0.87 | 1.99 | 2 |
| stroke 68 | 11 % → 49 % | 36.7 px | 0.85 | 4.24 | 6 |
| stroke 69 | 16 % → 58 % | 44.1 px | 0.85 | 3.70 | 8 |
| stroke 70 | 41 % → 76 % | 100.5 px | 0.87 | 1.86 | 19 |
| stroke 71 | 68 % → 88 % | 272.1 px | 0.89 | 1.30 | 8 |
| stroke 72 | 59 % → 75 % | 155.3 px | 0.86 | 1.28 | 15 |
| stroke 73 | 50 % → 88 % | 80.8 px | 0.88 | 1.78 | 19 |
| stroke 74 | 37 % → 73 % | 86.3 px | 0.88 | 1.97 | 14 |
| stroke 75 | 61 % → 74 % | 160.3 px | 0.87 | 1.21 | 8 |
| stroke 76 | 68 % → 76 % | 138.7 px | 0.88 | 1.12 | 23 |
| stroke 77 | 34 % → 69 % | 125.2 px | 0.87 | 2.01 | 6 |
| stroke 78 | 22 % → 49 % | 32.6 px | 0.86 | 2.22 | 71 |
| stroke 79 | 48 % → 66 % | 79.3 px | 0.87 | 1.37 | 33 |
| stroke 80 | 60 % → 77 % | 95.4 px | 0.87 | 1.28 | 43 |
| stroke 81 | 48 % → 79 % | 129.0 px | 0.87 | 1.66 | 11 |
| stroke 82 | 56 % → 72 % | 117.4 px | 0.88 | 1.29 | 19 |
| stroke 83 | 22 % → 55 % | 92.6 px | 0.87 | 2.53 | 4 |
| stroke 84 | 38 % → 53 % | 65.8 px | 0.86 | 1.39 | 76 |
| stroke 85 | 59 % → 74 % | 128.0 px | 0.88 | 1.26 | 16 |
| stroke 86 | 59 % → 85 % | 173.2 px | 0.88 | 1.44 | 7 |
| stroke 87 | 72 % → 80 % | 229.4 px | 0.88 | 1.10 | 30 |
| stroke 88 | 62 % → 75 % | 146.6 px | 0.86 | 1.21 | 18 |
| stroke 89 | 23 % → 40 % | 64.2 px | 0.88 | 1.70 | 8 |
| stroke 90 | 21 % → 46 % | 55.9 px | 0.87 | 2.14 | 6 |
| stroke 91 | 7 % → 55 % | 26.0 px | 0.88 | 8.24 | 3 |
| stroke 92 | 44 % → 64 % | 89.6 px | 0.89 | 1.45 | 56 |
| stroke 93 | 53 % → 69 % | 136.2 px | 0.87 | 1.30 | 15 |
| stroke 94 | 59 % → 67 % | 156.3 px | 0.88 | 1.12 | 7 |
| stroke 95 | 29 % → 58 % | 53.3 px | 0.87 | 2.02 | 20 |
| stroke 96 | 26 % → 63 % | 63.0 px | 0.87 | 2.40 | 10 |
| stroke 97 | 43 % → 69 % | 112.7 px | 0.87 | 1.59 | 13 |
| stroke 98 | 76 % → 89 % | 200.5 px | 0.89 | 1.17 | 31 |
| stroke 99 | 36 % → 59 % | 68.8 px | 0.87 | 1.61 | 11 |
| stroke 100 | 64 % → 77 % | 247.4 px | 0.86 | 1.21 | 9 |
| stroke 101 | 67 % → 80 % | 308.2 px | 0.89 | 1.18 | 18 |
| stroke 102 | 21 % → 54 % | 34.5 px | 0.88 | 2.54 | 20 |
| stroke 103 | 30 % → 38 % | 77.5 px | 0.88 | 1.25 | 10 |
| stroke 104 | 27 % → 42 % | 44.2 px | 0.88 | 1.55 | 60 |
| stroke 105 | 74 % → 82 % | 234.4 px | 0.88 | 1.12 | 9 |
| stroke 106 | 77 % → 79 % | 217.1 px | 0.89 | 1.03 | 8 |
| stroke 107 | 39 % → 53 % | 121.9 px | 0.87 | 1.37 | 10 |
| stroke 108 | 47 % → 66 % | 100.5 px | 0.88 | 1.39 | 21 |
| stroke 109 | 68 % → 76 % | 160.5 px | 0.89 | 1.12 | 14 |
| stroke 110 | 50 % → 59 % | 218.7 px | 0.87 | 1.18 | 5 |
| stroke 111 | 28 % → 53 % | 58.9 px | 0.88 | 1.89 | 26 |
| stroke 112 | 52 % → 60 % | 83.6 px | 0.88 | 1.15 | 29 |
| stroke 113 | 61 % → 67 % | 184.2 px | 0.87 | 1.10 | 5 |
| stroke 114 | 54 % → 65 % | 68.2 px | 0.87 | 1.21 | 51 |
| stroke 115 | 66 % → 76 % | 174.3 px | 0.88 | 1.16 | 9 |
| stroke 116 | 72 % → 74 % | 229.7 px | 0.85 | 1.02 | 8 |
| stroke 117 | 78 % → 82 % | 226.6 px | 0.88 | 1.05 | 16 |
| stroke 118 | 31 % → 61 % | 78.1 px | 0.86 | 2.01 | 25 |
| stroke 119 | 82 % → 85 % | 257.1 px | 0.89 | 1.04 | 9 |
| stroke 120 | 50 % → 53 % | 90.2 px | 0.88 | 1.05 | 46 |
| stroke 121 | 79 % → 81 % | 367.1 px | 0.88 | 1.03 | 5 |
| stroke 122 | 48 % → 55 % | 127.1 px | 0.86 | 1.16 | 35 |
| stroke 123 | 40 % → 46 % | 139.2 px | 0.86 | 1.16 | 7 |
| stroke 124 | 90 % → 91 % | 236.5 px | 0.89 | 1.01 | 12 |
| stroke 125 | 64 % → 67 % | 255.6 px | 0.86 | 1.05 | 11 |
| stroke 126 | 82 % → 85 % | 306.1 px | 0.88 | 1.03 | 3 |
| stroke 127 | 46 % → 48 % | 178.8 px | 0.87 | 1.05 | 8 |
| stroke 128 | 70 % → 76 % | 297.5 px | 0.86 | 1.08 | 6 |
| stroke 129 | 39 % → 61 % | 50.8 px | 0.86 | 1.58 | 40 |
| stroke 130 | 41 % → 67 % | 51.6 px | 0.86 | 1.63 | 60 |
| stroke 131 | 43 % → 63 % | 58.6 px | 0.86 | 1.44 | 50 |
| stroke 132 | 61 % → 72 % | 156.8 px | 0.87 | 1.17 | 24 |

Numbers say: wet paint spreads well beyond the stroke.

## Refs v3 · #29 Shrigley asterisk — own sheet
own sheet 800 × 1028 · Watercolour 1.00 + water 50 % · 64 px · 21.4 s

![Refs v3 · #29 Shrigley asterisk — own sheet](Refs-v3-29-Shrigley-asterisk-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 15 % → 46 % | 70.2 px | 0.57 | 3.16 | 428 |
| stroke 2 | 24 % → 55 % | 104.0 px | 0.57 | 2.34 | 290 |
| stroke 3 | 8 % → 29 % | 78.1 px | 0.57 | 3.62 | 37 |
| stroke 4 | 22 % → 38 % | 111.1 px | 0.58 | 1.72 | 541 |
| stroke 5 | 30 % → 48 % | 148.6 px | 0.57 | 1.59 | 227 |
| stroke 6 | 30 % → 38 % | 138.3 px | 0.57 | 1.28 | 278 |
| stroke 7 | 33 % → 38 % | 183.5 px | 0.57 | 1.14 | 395 |
| stroke 8 | 31 % → 33 % | 175.6 px | 0.57 | 1.08 | 587 |
| stroke 9 | 62 % → 69 % | 813.4 px | 0.57 | 1.12 | 79 |
| stroke 10 | 72 % → 83 % | 1328.8 px | 0.57 | 1.15 | 43 |
| stroke 11 | 58 % → 71 % | 796.9 px | 0.57 | 1.21 | 77 |
| stroke 12 | 66 % → 72 % | 967.8 px | 0.57 | 1.10 | 63 |
| stroke 13 | 41 % → 42 % | 272.7 px | 0.57 | 1.02 | 229 |

Numbers say: wet paint spreads well beyond the stroke.

## Refs v3 · #30 Red gouache face — own sheet
own sheet 800 × 1084 · Gouache 1.00 + water 15 % · 76 px · 52.0 s

![Refs v3 · #30 Red gouache face — own sheet](Refs-v3-30-Red-gouache-face-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 7 % → 0 % | 73.6 px | 0.00 | 0.00 | 186 |
| stroke 2 | 10 % → 1 % | 115.8 px | 0.40 | 0.06 | 135 |
| stroke 3 | 14 % → 1 % | 115.5 px | 0.37 | 0.06 | 247 |
| stroke 4 | 13 % → 1 % | 149.8 px | 0.40 | 0.11 | 118 |
| stroke 5 | 18 % → 2 % | 136.5 px | 0.37 | 0.12 | 262 |
| stroke 6 | 19 % → 2 % | 201.6 px | 0.40 | 0.13 | 124 |
| stroke 7 | 25 % → 3 % | 207.9 px | 0.38 | 0.13 | 298 |
| stroke 8 | 20 % → 5 % | 283.2 px | 0.37 | 0.26 | 108 |
| stroke 9 | 25 % → 3 % | 279.1 px | 0.40 | 0.14 | 168 |
| stroke 10 | 36 % → 0 % | 400.9 px | 0.33 | 0.01 | 140 |
| stroke 11 | 17 % → 6 % | 309.6 px | 0.37 | 0.35 | 82 |
| stroke 12 | 31 % → 4 % | 246.2 px | 0.40 | 0.12 | 209 |
| stroke 13 | 42 % → 0 % | 678.5 px | 0.00 | 0.00 | 92 |
| stroke 14 | 18 % → 6 % | 378.1 px | 0.37 | 0.35 | 49 |
| stroke 15 | 33 % → 5 % | 264.5 px | 0.40 | 0.14 | 336 |
| stroke 16 | 34 % → 3 % | 448.0 px | 0.37 | 0.10 | 162 |
| stroke 17 | 17 % → 6 % | 361.7 px | 0.37 | 0.36 | 52 |
| stroke 18 | 38 % → 5 % | 261.7 px | 0.40 | 0.12 | 501 |
| stroke 19 | 16 % → 6 % | 264.5 px | 0.37 | 0.34 | 111 |
| stroke 20 | 37 % → 6 % | 228.8 px | 0.39 | 0.17 | 685 |
| stroke 21 | 23 % → 5 % | 272.5 px | 0.37 | 0.22 | 171 |
| stroke 22 | 41 % → 7 % | 335.7 px | 0.40 | 0.17 | 287 |
| stroke 23 | 35 % → 3 % | 245.3 px | 0.37 | 0.08 | 500 |
| stroke 24 | 40 % → 8 % | 343.3 px | 0.40 | 0.20 | 320 |
| stroke 25 | 40 % → 3 % | 284.9 px | 0.37 | 0.07 | 430 |
| stroke 26 | 40 % → 8 % | 360.0 px | 0.39 | 0.19 | 353 |
| stroke 27 | 42 % → 2 % | 316.0 px | 0.38 | 0.05 | 526 |
| stroke 28 | 38 % → 7 % | 339.6 px | 0.39 | 0.18 | 198 |
| stroke 29 | 44 % → 1 % | 339.8 px | 0.37 | 0.03 | 378 |
| stroke 30 | 42 % → 4 % | 273.7 px | 0.39 | 0.10 | 730 |
| stroke 31 | 45 % → 3 % | 284.9 px | 0.39 | 0.08 | 583 |
| stroke 32 | 36 % → 5 % | 354.9 px | 0.39 | 0.13 | 172 |
| stroke 33 | 54 % → 0 % | 969.1 px | 0.00 | 0.00 | 44 |
| stroke 34 | 43 % → 0 % | 566.0 px | 0.00 | 0.00 | 90 |
| stroke 35 | 44 % → 1 % | 557.2 px | 0.37 | 0.02 | 176 |
| stroke 36 | 2 % → 0 % | 27.0 px | 0.00 | 0.00 | 26 |
| stroke 37 | 3 % → 0 % | 81.6 px | 0.00 | 0.00 | 8 |
| stroke 38 | 0 % → 7 % | 15.9 px | 0.37 | 19.09 | 4 |
| stroke 39 | 1 % → 6 % | 32.9 px | 0.37 | 6.44 | 6 |
| stroke 40 | 1 % → 8 % | 23.2 px | 0.39 | 8.89 | 8 |
| stroke 41 | 3 % → 8 % | 41.7 px | 0.39 | 2.38 | 9 |
| stroke 42 | 5 % → 6 % | 76.4 px | 0.39 | 1.15 | 21 |
| stroke 43 | 6 % → 7 % | 184.8 px | 0.39 | 1.21 | 19 |
| stroke 44 | 2 % → 4 % | 29.8 px | 0.40 | 2.00 | 40 |
| stroke 45 | 1 % → 0 % | 46.7 px | 0.37 | 0.00 | 8 |
| stroke 46 | 1 % → 0 % | 12.4 px | 0.00 | 0.00 | 14 |
| stroke 47 | 1 % → 0 % | 25.8 px | 0.00 | 0.00 | 7 |
| stroke 48 | 2 % → 0 % | 42.0 px | 0.00 | 0.00 | 7 |
| stroke 49 | 2 % → 0 % | 44.1 px | 0.00 | 0.00 | 3 |
| stroke 50 | 2 % → 0 % | 37.1 px | 0.00 | 0.00 | 7 |
| stroke 51 | 1 % → 6 % | 28.5 px | 0.37 | 6.32 | 9 |
| stroke 52 | 2 % → 5 % | 53.9 px | 0.37 | 2.31 | 10 |
| stroke 53 | 4 % → 4 % | 61.1 px | 0.37 | 1.19 | 30 |
| stroke 54 | 1 % → 6 % | 17.3 px | 0.37 | 11.75 | 4 |
| stroke 55 | 6 % → 5 % | 127.0 px | 0.38 | 0.76 | 20 |
| stroke 56 | 5 % → 0 % | 50.5 px | 0.00 | 0.00 | 103 |
| stroke 57 | 6 % → 0 % | 66.2 px | 0.00 | 0.00 | 55 |
| stroke 58 | 8 % → 0 % | 91.9 px | 0.37 | 0.00 | 62 |
| stroke 59 | 16 % → 0 % | 201.5 px | 0.00 | 0.00 | 55 |
| stroke 60 | 16 % → 0 % | 470.0 px | 0.00 | 0.00 | 59 |
| stroke 61 | 16 % → 1 % | 132.5 px | 0.40 | 0.05 | 99 |
| stroke 62 | 17 % → 0 % | 118.6 px | 0.00 | 0.00 | 203 |
| stroke 63 | 19 % → 2 % | 151.8 px | 0.40 | 0.08 | 113 |
| stroke 64 | 23 % → 0 % | 357.4 px | 0.00 | 0.00 | 107 |
| stroke 65 | 17 % → 0 % | 433.5 px | 0.00 | 0.00 | 28 |
| stroke 66 | 23 % → 3 % | 219.2 px | 0.40 | 0.13 | 85 |
| stroke 67 | 26 % → 0 % | 322.3 px | 0.00 | 0.00 | 77 |
| stroke 68 | 30 % → 0 % | 844.2 px | 0.00 | 0.00 | 47 |
| stroke 69 | 29 % → 0 % | 830.8 px | 0.00 | 0.00 | 41 |
| stroke 70 | 31 % → 0 % | 579.4 px | 0.00 | 0.00 | 38 |
| stroke 71 | 6 % → 1 % | 207.2 px | 0.37 | 0.14 | 32 |
| stroke 72 | 29 % → 0 % | 552.9 px | 0.00 | 0.00 | 45 |
| stroke 73 | 24 % → 0 % | 311.9 px | 0.00 | 0.00 | 204 |
| stroke 74 | 6 % → 3 % | 115.9 px | 0.37 | 0.47 | 47 |
| stroke 75 | 20 % → 0 % | 347.3 px | 0.00 | 0.00 | 66 |
| stroke 76 | 8 % → 3 % | 84.5 px | 0.37 | 0.40 | 65 |
| stroke 77 | 19 % → 0 % | 627.6 px | 0.00 | 0.00 | 29 |
| stroke 78 | 11 % → 5 % | 316.4 px | 0.38 | 0.45 | 84 |
| stroke 79 | 10 % → 5 % | 286.2 px | 0.38 | 0.46 | 20 |
| stroke 80 | 18 % → 0 % | 224.9 px | 0.00 | 0.00 | 103 |
| stroke 81 | 18 % → 5 % | 242.7 px | 0.37 | 0.31 | 72 |
| stroke 82 | 23 % → 0 % | 229.3 px | 0.32 | 0.01 | 183 |
| stroke 83 | 21 % → 5 % | 266.8 px | 0.37 | 0.26 | 81 |
| stroke 84 | 8 % → 0 % | 193.7 px | 0.00 | 0.00 | 20 |
| stroke 85 | 21 % → 6 % | 317.5 px | 0.37 | 0.26 | 113 |
| stroke 86 | 22 % → 5 % | 303.4 px | 0.37 | 0.24 | 72 |
| stroke 87 | 22 % → 6 % | 618.6 px | 0.37 | 0.29 | 19 |
| stroke 88 | 22 % → 6 % | 507.5 px | 0.37 | 0.29 | 41 |
| stroke 89 | 12 % → 4 % | 356.7 px | 0.38 | 0.36 | 10 |
| stroke 90 | 20 % → 7 % | 651.2 px | 0.37 | 0.33 | 18 |
| stroke 91 | 16 % → 6 % | 130.2 px | 0.37 | 0.39 | 84 |
| stroke 92 | 17 % → 5 % | 160.9 px | 0.38 | 0.27 | 117 |
| stroke 93 | 17 % → 7 % | 599.0 px | 0.37 | 0.39 | 20 |
| stroke 94 | 19 % → 2 % | 222.8 px | 0.37 | 0.12 | 81 |
| stroke 95 | 18 % → 4 % | 514.1 px | 0.38 | 0.24 | 27 |
| stroke 96 | 16 % → 3 % | 269.2 px | 0.37 | 0.18 | 49 |
| stroke 97 | 14 % → 1 % | 156.9 px | 0.37 | 0.10 | 83 |
| stroke 98 | 13 % → 0 % | 134.0 px | 0.35 | 0.04 | 86 |
| stroke 99 | 13 % → 0 % | 91.8 px | 0.00 | 0.00 | 247 |
| stroke 100 | 19 % → 0 % | 111.4 px | 0.00 | 0.00 | 250 |
| stroke 101 | 25 % → 0 % | 497.3 px | 0.00 | 0.00 | 33 |
| stroke 102 | 9 % → 0 % | 125.7 px | 0.33 | 0.00 | 72 |
| stroke 103 | 13 % → 3 % | 121.8 px | 0.40 | 0.21 | 80 |
| stroke 104 | 15 % → 4 % | 125.8 px | 0.39 | 0.26 | 148 |
| stroke 105 | 17 % → 3 % | 99.2 px | 0.39 | 0.21 | 281 |
| stroke 106 | 24 % → 4 % | 175.3 px | 0.39 | 0.16 | 215 |
| stroke 107 | 30 % → 3 % | 277.3 px | 0.38 | 0.11 | 75 |
| stroke 108 | 32 % → 3 % | 321.4 px | 0.38 | 0.10 | 66 |
| stroke 109 | 18 % → 0 % | 285.0 px | 0.00 | 0.00 | 71 |
| stroke 110 | 27 % → 0 % | 377.3 px | 0.00 | 0.00 | 72 |
| stroke 111 | 27 % → 0 % | 492.4 px | 0.00 | 0.00 | 41 |
| stroke 112 | 24 % → 0 % | 695.5 px | 0.00 | 0.00 | 20 |
| stroke 113 | 34 % → 0 % | 420.7 px | 0.00 | 0.00 | 165 |
| stroke 114 | 34 % → 0 % | 666.9 px | 0.00 | 0.00 | 76 |
| stroke 115 | 6 % → 7 % | 36.0 px | 0.40 | 1.13 | 169 |
| stroke 116 | 4 % → 5 % | 44.2 px | 0.37 | 1.12 | 108 |

Numbers say: wet paint spreads well beyond the stroke.

## Refs v3 · #31 Warhol blotted line — own sheet
own sheet 800 × 708 · Ink 0.98 · 25 px · 24.8 s

![Refs v3 · #31 Warhol blotted line — own sheet](Refs-v3-31-Warhol-blotted-line-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 1 % → 23 % | 8.5 px | 0.52 | 20.94 | 2 |
| stroke 2 | 2 % → 60 % | 12.0 px | 0.51 | 28.06 | 7 |
| stroke 3 | 2 % → 49 % | 12.8 px | 0.53 | 23.05 | 4 |
| stroke 4 | 1 % → 66 % | 11.5 px | 0.51 | 44.52 | 4 |
| stroke 5 | 1 % → 70 % | 8.8 px | 0.51 | 49.64 | 2 |
| stroke 6 | 6 % → 69 % | 35.1 px | 0.51 | 12.17 | 2 |
| stroke 7 | 4 % → 73 % | 23.7 px | 0.52 | 18.39 | 3 |
| stroke 8 | 2 % → 53 % | 11.5 px | 0.53 | 23.62 | 5 |
| stroke 9 | 5 % → 31 % | 14.5 px | 0.53 | 6.06 | 23 |
| stroke 10 | 3 % → 43 % | 17.0 px | 0.51 | 13.44 | 6 |
| stroke 11 | 4 % → 50 % | 27.0 px | 0.53 | 11.73 | 3 |
| stroke 12 | 6 % → 60 % | 33.4 px | 0.52 | 9.61 | 2 |
| stroke 13 | 9 % → 51 % | 44.6 px | 0.54 | 5.88 | 2 |
| stroke 14 | 7 % → 41 % | 20.2 px | 0.52 | 5.92 | 24 |
| stroke 15 | 7 % → 17 % | 20.5 px | 0.51 | 2.35 | 14 |
| stroke 16 | 2 % → 29 % | 13.4 px | 0.50 | 12.18 | 3 |
| stroke 17 | 8 % → 73 % | 64.4 px | 0.54 | 9.46 | 2 |
| stroke 18 | 20 % → 57 % | 63.2 px | 0.53 | 2.88 | 11 |
| stroke 19 | 11 % → 42 % | 49.8 px | 0.50 | 3.82 | 4 |
| stroke 20 | 12 % → 55 % | 87.7 px | 0.52 | 4.53 | 4 |
| stroke 21 | 1 % → 49 % | 9.7 px | 0.52 | 43.41 | 1 |
| stroke 22 | 5 % → 29 % | 12.6 px | 0.52 | 6.11 | 27 |
| stroke 23 | 3 % → 37 % | 10.7 px | 0.50 | 12.00 | 10 |
| stroke 24 | 4 % → 43 % | 12.4 px | 0.53 | 10.96 | 7 |
| stroke 25 | 15 % → 42 % | 65.4 px | 0.53 | 2.87 | 7 |
| stroke 26 | 15 % → 38 % | 63.1 px | 0.49 | 2.58 | 6 |
| stroke 27 | 12 % → 73 % | 55.4 px | 0.52 | 5.99 | 3 |
| stroke 28 | 10 % → 57 % | 79.9 px | 0.51 | 5.94 | 4 |
| stroke 29 | 14 % → 75 % | 72.5 px | 0.53 | 5.32 | 2 |
| stroke 30 | 3 % → 45 % | 13.2 px | 0.51 | 13.01 | 5 |
| stroke 31 | 14 % → 63 % | 47.5 px | 0.53 | 4.60 | 6 |
| stroke 32 | 4 % → 44 % | 15.9 px | 0.52 | 12.51 | 4 |
| stroke 33 | 12 % → 40 % | 55.4 px | 0.52 | 3.32 | 5 |
| stroke 34 | 12 % → 45 % | 91.3 px | 0.52 | 3.82 | 3 |
| stroke 35 | 15 % → 31 % | 40.3 px | 0.52 | 2.08 | 39 |
| stroke 36 | 9 % → 60 % | 30.8 px | 0.52 | 6.33 | 11 |
| stroke 37 | 18 % → 64 % | 79.2 px | 0.51 | 3.51 | 6 |
| stroke 38 | 17 % → 60 % | 119.3 px | 0.52 | 3.49 | 11 |
| stroke 39 | 7 % → 45 % | 27.1 px | 0.51 | 6.25 | 10 |
| stroke 40 | 16 % → 56 % | 89.7 px | 0.52 | 3.57 | 2 |
| stroke 41 | 5 % → 48 % | 19.2 px | 0.52 | 9.06 | 5 |
| stroke 42 | 8 % → 50 % | 34.6 px | 0.53 | 6.09 | 9 |
| stroke 43 | 22 % → 63 % | 76.6 px | 0.52 | 2.86 | 17 |
| stroke 44 | 19 % → 53 % | 59.9 px | 0.52 | 2.76 | 11 |
| stroke 45 | 29 % → 76 % | 159.2 px | 0.53 | 2.62 | 9 |
| stroke 46 | 9 % → 48 % | 70.8 px | 0.52 | 5.20 | 1 |
| stroke 47 | 18 % → 46 % | 78.3 px | 0.50 | 2.52 | 8 |
| stroke 48 | 24 % → 42 % | 93.6 px | 0.51 | 1.74 | 10 |
| stroke 49 | 34 % → 57 % | 191.9 px | 0.53 | 1.71 | 6 |
| stroke 50 | 35 % → 74 % | 233.4 px | 0.54 | 2.13 | 2 |
| stroke 51 | 26 % → 59 % | 88.6 px | 0.53 | 2.26 | 11 |
| stroke 52 | 17 % → 43 % | 59.8 px | 0.51 | 2.50 | 10 |
| stroke 53 | 11 % → 21 % | 31.1 px | 0.51 | 1.83 | 20 |
| stroke 54 | 25 % → 67 % | 102.8 px | 0.53 | 2.65 | 11 |
| stroke 55 | 4 % → 46 % | 27.0 px | 0.52 | 11.85 | 6 |
| stroke 56 | 41 % → 59 % | 153.1 px | 0.53 | 1.42 | 12 |
| stroke 57 | 17 % → 30 % | 40.2 px | 0.52 | 1.74 | 69 |
| stroke 58 | 29 % → 70 % | 202.0 px | 0.52 | 2.41 | 3 |
| stroke 59 | 40 % → 57 % | 156.7 px | 0.53 | 1.42 | 7 |
| stroke 60 | 43 % → 61 % | 161.6 px | 0.50 | 1.42 | 9 |
| stroke 61 | 14 % → 49 % | 59.6 px | 0.52 | 3.43 | 8 |
| stroke 62 | 31 % → 62 % | 141.3 px | 0.52 | 1.98 | 9 |
| stroke 63 | 36 % → 62 % | 227.3 px | 0.53 | 1.74 | 3 |
| stroke 64 | 27 % → 62 % | 114.0 px | 0.54 | 2.27 | 7 |
| stroke 65 | 26 % → 45 % | 97.0 px | 0.53 | 1.74 | 10 |
| stroke 66 | 26 % → 47 % | 145.1 px | 0.51 | 1.77 | 3 |
| stroke 67 | 25 % → 46 % | 114.9 px | 0.53 | 1.81 | 5 |
| stroke 68 | 13 % → 44 % | 47.1 px | 0.53 | 3.31 | 15 |
| stroke 69 | 22 % → 46 % | 87.0 px | 0.53 | 2.12 | 13 |
| stroke 70 | 38 % → 58 % | 218.3 px | 0.52 | 1.51 | 5 |
| stroke 71 | 31 % → 63 % | 230.0 px | 0.52 | 2.06 | 2 |
| stroke 72 | 35 % → 54 % | 281.5 px | 0.52 | 1.55 | 1 |
| stroke 73 | 37 % → 54 % | 290.1 px | 0.52 | 1.49 | 16 |
| stroke 74 | 41 % → 70 % | 147.1 px | 0.51 | 1.68 | 8 |
| stroke 75 | 18 % → 38 % | 75.3 px | 0.51 | 2.16 | 9 |
| stroke 76 | 45 % → 70 % | 210.8 px | 0.53 | 1.55 | 9 |
| stroke 77 | 21 % → 28 % | 57.7 px | 0.53 | 1.32 | 15 |
| stroke 78 | 31 % → 48 % | 219.2 px | 0.53 | 1.58 | 5 |
| stroke 79 | 23 % → 46 % | 49.8 px | 0.52 | 1.99 | 32 |
| stroke 80 | 36 % → 54 % | 251.1 px | 0.52 | 1.49 | 8 |
| stroke 81 | 41 % → 66 % | 336.1 px | 0.51 | 1.63 | 14 |
| stroke 82 | 20 % → 45 % | 84.3 px | 0.52 | 2.26 | 31 |
| stroke 83 | 32 % → 47 % | 101.9 px | 0.51 | 1.47 | 7 |
| stroke 84 | 42 % → 57 % | 344.4 px | 0.50 | 1.38 | 3 |
| stroke 85 | 45 % → 62 % | 167.8 px | 0.52 | 1.37 | 13 |
| stroke 86 | 47 % → 61 % | 301.6 px | 0.52 | 1.30 | 2 |
| stroke 87 | 25 % → 49 % | 212.8 px | 0.52 | 2.00 | 1 |
| stroke 88 | 42 % → 53 % | 219.7 px | 0.53 | 1.25 | 3 |
| stroke 89 | 51 % → 65 % | 228.2 px | 0.51 | 1.27 | 4 |
| stroke 90 | 57 % → 72 % | 319.2 px | 0.51 | 1.27 | 4 |
| stroke 91 | 31 % → 49 % | 129.2 px | 0.52 | 1.58 | 4 |
| stroke 92 | 28 % → 45 % | 97.1 px | 0.52 | 1.62 | 10 |
| stroke 93 | 31 % → 40 % | 92.0 px | 0.53 | 1.29 | 30 |
| stroke 94 | 39 % → 51 % | 316.4 px | 0.51 | 1.32 | 2 |
| stroke 95 | 33 % → 40 % | 106.0 px | 0.52 | 1.24 | 5 |
| stroke 96 | 31 % → 48 % | 232.7 px | 0.52 | 1.55 | 3 |
| stroke 97 | 51 % → 63 % | 230.7 px | 0.54 | 1.23 | 13 |
| stroke 98 | 58 % → 63 % | 195.1 px | 0.53 | 1.07 | 15 |
| stroke 99 | 18 % → 20 % | 67.9 px | 0.52 | 1.16 | 98 |
| stroke 100 | 34 % → 37 % | 251.5 px | 0.51 | 1.09 | 2 |
| stroke 101 | 11 % → 33 % | 45.4 px | 0.52 | 2.88 | 6 |
| stroke 102 | 49 % → 58 % | 183.3 px | 0.52 | 1.19 | 7 |
| stroke 103 | 31 % → 50 % | 120.1 px | 0.51 | 1.61 | 12 |
| stroke 104 | 49 % → 51 % | 373.6 px | 0.52 | 1.05 | 9 |
| stroke 105 | 48 % → 50 % | 166.3 px | 0.53 | 1.05 | 19 |
| stroke 106 | 42 % → 55 % | 174.7 px | 0.52 | 1.31 | 12 |
| stroke 107 | 28 % → 48 % | 218.2 px | 0.53 | 1.70 | 3 |
| stroke 108 | 44 % → 48 % | 144.3 px | 0.52 | 1.09 | 9 |
| stroke 109 | 43 % → 48 % | 279.5 px | 0.52 | 1.12 | 4 |
| stroke 110 | 34 % → 41 % | 129.5 px | 0.52 | 1.19 | 10 |
| stroke 111 | 27 % → 36 % | 69.5 px | 0.51 | 1.37 | 29 |
| stroke 112 | 62 % → 65 % | 313.0 px | 0.52 | 1.06 | 8 |
| stroke 113 | 79 % → 82 % | 537.7 px | 0.53 | 1.03 | 4 |
| stroke 114 | 45 % → 50 % | 285.4 px | 0.51 | 1.10 | 2 |
| stroke 115 | 23 % → 33 % | 84.9 px | 0.52 | 1.45 | 12 |
| stroke 116 | 54 % → 65 % | 201.0 px | 0.52 | 1.22 | 11 |
| stroke 117 | 43 % → 53 % | 180.3 px | 0.51 | 1.24 | 5 |
| stroke 118 | 41 % → 44 % | 234.2 px | 0.52 | 1.08 | 2 |
| stroke 119 | 49 % → 51 % | 194.2 px | 0.52 | 1.04 | 24 |
| stroke 120 | 40 % → 44 % | 168.1 px | 0.51 | 1.11 | 10 |
| stroke 121 | 38 % → 52 % | 188.3 px | 0.52 | 1.39 | 25 |
| stroke 122 | 47 % → 58 % | 211.2 px | 0.52 | 1.23 | 17 |
| stroke 123 | 40 % → 49 % | 194.9 px | 0.52 | 1.21 | 21 |
| stroke 124 | 56 % → 62 % | 299.7 px | 0.51 | 1.10 | 5 |

Numbers say: wet paint spreads well beyond the stroke.

## Refs v3 · #32 Thick orange swipes — own sheet
own sheet 800 × 800 · Impasto 1.00 · 76 px · 24.2 s

![Refs v3 · #32 Thick orange swipes — own sheet](Refs-v3-32-Thick-orange-swipes-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 13 % → 22 % | 68.2 px | 0.32 | 1.66 | 703 |
| stroke 2 | 19 % → 33 % | 155.3 px | 0.32 | 1.70 | 361 |
| stroke 3 | 15 % → 30 % | 277.7 px | 0.32 | 2.03 | 146 |
| stroke 4 | 23 % → 34 % | 219.9 px | 0.33 | 1.51 | 252 |
| stroke 5 | 16 % → 34 % | 370.2 px | 0.33 | 2.11 | 86 |
| stroke 6 | 25 % → 33 % | 351.7 px | 0.33 | 1.33 | 122 |
| stroke 7 | 18 % → 39 % | 418.1 px | 0.33 | 2.15 | 42 |
| stroke 8 | 27 % → 32 % | 463.9 px | 0.33 | 1.18 | 91 |
| stroke 9 | 25 % → 33 % | 492.4 px | 0.33 | 1.29 | 95 |
| stroke 10 | 22 % → 35 % | 442.4 px | 0.33 | 1.55 | 75 |
| stroke 11 | 13 % → 49 % | 301.1 px | 0.33 | 3.74 | 188 |
| stroke 12 | 19 % → 38 % | 371.1 px | 0.34 | 1.97 | 149 |
| stroke 13 | 16 % → 62 % | 137.2 px | 0.33 | 3.74 | 297 |
| stroke 14 | 16 % → 41 % | 286.2 px | 0.34 | 2.51 | 184 |
| stroke 15 | 16 % → 45 % | 213.4 px | 0.34 | 2.81 | 131 |
| stroke 16 | 18 % → 50 % | 180.6 px | 0.33 | 2.79 | 201 |
| stroke 17 | 19 % → 47 % | 213.3 px | 0.34 | 2.49 | 254 |
| stroke 18 | 20 % → 44 % | 240.5 px | 0.33 | 2.26 | 213 |
| stroke 19 | 21 % → 36 % | 356.1 px | 0.34 | 1.74 | 122 |
| stroke 20 | 20 % → 33 % | 386.7 px | 0.34 | 1.62 | 155 |
| stroke 21 | 19 % → 29 % | 324.4 px | 0.33 | 1.52 | 76 |
| stroke 22 | 6 % → 44 % | 102.0 px | 0.33 | 7.36 | 136 |
| stroke 23 | 17 % → 28 % | 295.5 px | 0.34 | 1.60 | 109 |
| stroke 24 | 12 % → 32 % | 101.1 px | 0.33 | 2.60 | 353 |
| stroke 25 | 17 % → 24 % | 293.6 px | 0.34 | 1.44 | 76 |
| stroke 26 | 25 % → 23 % | 160.1 px | 0.34 | 0.94 | 389 |
| stroke 27 | 26 % → 15 % | 140.0 px | 0.33 | 0.60 | 433 |
| stroke 28 | 34 % → 13 % | 174.6 px | 0.33 | 0.38 | 499 |
| stroke 29 | 11 % → 41 % | 107.0 px | 0.33 | 3.87 | 536 |
| stroke 30 | 18 % → 42 % | 127.7 px | 0.33 | 2.34 | 464 |
| stroke 31 | 26 % → 45 % | 162.4 px | 0.33 | 1.76 | 954 |
| stroke 32 | 32 % → 49 % | 199.1 px | 0.33 | 1.54 | 836 |
| stroke 33 | 41 % → 67 % | 371.8 px | 0.33 | 1.62 | 458 |
| stroke 34 | 37 % → 54 % | 239.6 px | 0.33 | 1.47 | 899 |
| stroke 35 | 38 % → 57 % | 273.0 px | 0.33 | 1.50 | 475 |
| stroke 36 | 36 % → 52 % | 252.6 px | 0.34 | 1.44 | 859 |
| stroke 37 | 34 % → 42 % | 217.5 px | 0.34 | 1.22 | 766 |
| stroke 38 | 38 % → 41 % | 302.8 px | 0.33 | 1.10 | 516 |
| stroke 39 | 39 % → 37 % | 389.9 px | 0.33 | 0.96 | 274 |

Numbers say: wet paint spreads well beyond the stroke.

## Refs v3 · #33 Red wet-in-wet flames — own sheet
own sheet 800 × 1083 · Watercolour 1.00 + water 60 % · 96 px · 39.4 s

![Refs v3 · #33 Red wet-in-wet flames — own sheet](Refs-v3-33-Red-wet-in-wet-flames-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 25 % → 59 % | 102.5 px | 0.38 | 2.34 | 2157 |
| stroke 2 | 29 % → 58 % | 142.0 px | 0.28 | 2.01 | 538 |
| stroke 3 | 31 % → 58 % | 260.5 px | 0.28 | 1.87 | 274 |
| stroke 4 | 37 % → 61 % | 256.7 px | 0.27 | 1.66 | 773 |
| stroke 5 | 38 % → 60 % | 361.1 px | 0.27 | 1.56 | 499 |
| stroke 6 | 37 % → 58 % | 325.2 px | 0.26 | 1.56 | 400 |
| stroke 7 | 35 % → 56 % | 205.9 px | 0.24 | 1.58 | 672 |
| stroke 8 | 41 % → 53 % | 206.3 px | 0.25 | 1.28 | 632 |

Numbers say: wet paint spreads well beyond the stroke.

## Refs v3 · #34 Magenta oil patches — own sheet
own sheet 800 × 1420 · Gouache 1.00 + turpentine 20 % · 90 px · 98.9 s

![Refs v3 · #34 Magenta oil patches — own sheet](Refs-v3-34-Magenta-oil-patches-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 23 % → 17 % | 70.7 px | 0.23 | 0.76 | 1204 |
| stroke 2 | 37 % → 21 % | 97.9 px | 0.24 | 0.56 | 1336 |
| stroke 3 | 40 % → 23 % | 183.4 px | 0.24 | 0.58 | 1080 |
| stroke 4 | 43 % → 25 % | 265.5 px | 0.24 | 0.58 | 713 |
| stroke 5 | 48 % → 30 % | 638.9 px | 0.24 | 0.63 | 147 |
| stroke 6 | 6 % → 21 % | 100.3 px | 0.24 | 3.68 | 229 |
| stroke 7 | 9 % → 20 % | 124.1 px | 0.24 | 2.16 | 247 |
| stroke 8 | 5 % → 23 % | 100.5 px | 0.24 | 4.39 | 150 |
| stroke 9 | 7 % → 27 % | 187.1 px | 0.24 | 3.84 | 85 |
| stroke 10 | 19 % → 21 % | 104.1 px | 0.24 | 1.11 | 916 |
| stroke 11 | 22 % → 18 % | 323.3 px | 0.24 | 0.82 | 207 |
| stroke 12 | 26 % → 22 % | 336.5 px | 0.23 | 0.86 | 316 |
| stroke 13 | 20 % → 23 % | 251.1 px | 0.23 | 1.15 | 189 |
| stroke 14 | 17 % → 24 % | 195.0 px | 0.23 | 1.39 | 343 |
| stroke 15 | 21 % → 21 % | 227.3 px | 0.23 | 1.04 | 173 |
| stroke 16 | 28 % → 18 % | 314.8 px | 0.23 | 0.64 | 248 |
| stroke 17 | 31 % → 20 % | 615.2 px | 0.22 | 0.64 | 82 |
| stroke 18 | 2 % → 54 % | 24.1 px | 0.24 | 29.91 | 36 |
| stroke 19 | 16 % → 0 % | 72.7 px | 0.00 | 0.00 | 313 |
| stroke 20 | 21 % → 0 % | 182.6 px | 0.19 | 0.00 | 179 |
| stroke 21 | 22 % → 2 % | 341.5 px | 0.23 | 0.08 | 274 |
| stroke 22 | 23 % → 16 % | 209.8 px | 0.24 | 0.71 | 388 |
| stroke 23 | 24 % → 20 % | 221.8 px | 0.24 | 0.83 | 605 |
| stroke 24 | 26 % → 20 % | 238.3 px | 0.24 | 0.78 | 378 |
| stroke 25 | 28 % → 20 % | 255.8 px | 0.24 | 0.72 | 550 |
| stroke 26 | 30 % → 20 % | 272.5 px | 0.24 | 0.67 | 430 |
| stroke 27 | 33 % → 14 % | 372.6 px | 0.24 | 0.41 | 402 |
| stroke 28 | 33 % → 11 % | 432.6 px | 0.23 | 0.35 | 227 |
| stroke 29 | 31 % → 12 % | 436.7 px | 0.23 | 0.38 | 332 |
| stroke 30 | 29 % → 13 % | 344.7 px | 0.24 | 0.45 | 225 |
| stroke 31 | 27 % → 11 % | 340.8 px | 0.23 | 0.38 | 196 |
| stroke 32 | 25 % → 9 % | 339.7 px | 0.23 | 0.35 | 208 |
| stroke 33 | 25 % → 8 % | 352.5 px | 0.23 | 0.31 | 214 |
| stroke 34 | 24 % → 7 % | 309.0 px | 0.24 | 0.29 | 207 |
| stroke 35 | 24 % → 6 % | 241.4 px | 0.24 | 0.27 | 329 |
| stroke 36 | 25 % → 7 % | 258.2 px | 0.24 | 0.27 | 275 |
| stroke 37 | 32 % → 8 % | 646.6 px | 0.24 | 0.25 | 95 |
| stroke 38 | 8 % → 0 % | 115.1 px | 0.00 | 0.00 | 89 |
| stroke 39 | 12 % → 0 % | 140.3 px | 0.00 | 0.00 | 131 |
| stroke 40 | 17 % → 0 % | 198.6 px | 0.23 | 0.01 | 240 |
| stroke 41 | 20 % → 0 % | 272.4 px | 0.23 | 0.01 | 159 |
| stroke 42 | 21 % → 0 % | 324.9 px | 0.23 | 0.01 | 126 |
| stroke 43 | 24 % → 0 % | 328.7 px | 0.23 | 0.01 | 97 |
| stroke 44 | 26 % → 2 % | 268.3 px | 0.22 | 0.08 | 158 |
| stroke 45 | 30 % → 4 % | 253.6 px | 0.22 | 0.12 | 239 |
| stroke 46 | 11 % → 35 % | 99.6 px | 0.22 | 3.29 | 187 |
| stroke 47 | 41 % → 7 % | 260.3 px | 0.22 | 0.18 | 377 |
| stroke 48 | 14 % → 46 % | 95.5 px | 0.24 | 3.39 | 239 |
| stroke 49 | 15 % → 45 % | 332.7 px | 0.24 | 2.93 | 99 |
| stroke 50 | 5 % → 6 % | 109.5 px | 0.24 | 1.38 | 88 |
| stroke 51 | 17 % → 4 % | 102.8 px | 0.24 | 0.24 | 545 |
| stroke 52 | 23 % → 2 % | 136.5 px | 0.24 | 0.09 | 502 |
| stroke 53 | 30 % → 6 % | 180.5 px | 0.26 | 0.18 | 522 |
| stroke 54 | 36 % → 11 % | 212.4 px | 0.25 | 0.30 | 517 |
| stroke 55 | 10 % → 0 % | 98.5 px | 0.23 | 0.04 | 149 |
| stroke 56 | 56 % → 14 % | 495.7 px | 0.24 | 0.25 | 242 |
| stroke 57 | 39 % → 12 % | 203.9 px | 0.25 | 0.30 | 1032 |
| stroke 58 | 54 % → 18 % | 469.1 px | 0.24 | 0.33 | 316 |
| stroke 59 | 44 % → 19 % | 449.0 px | 0.24 | 0.43 | 502 |
| stroke 60 | 32 % → 1 % | 309.5 px | 0.24 | 0.04 | 647 |
| stroke 61 | 55 % → 22 % | 474.0 px | 0.24 | 0.40 | 345 |
| stroke 62 | 47 % → 28 % | 755.1 px | 0.24 | 0.59 | 178 |
| stroke 63 | 51 % → 32 % | 313.9 px | 0.24 | 0.63 | 895 |
| stroke 64 | 2 % → 9 % | 25.1 px | 0.24 | 5.53 | 63 |
| stroke 65 | 9 % → 35 % | 98.2 px | 0.24 | 3.87 | 300 |
| stroke 66 | 21 % → 30 % | 121.5 px | 0.24 | 1.40 | 589 |
| stroke 67 | 29 % → 26 % | 170.5 px | 0.23 | 0.91 | 841 |
| stroke 68 | 33 % → 16 % | 177.0 px | 0.23 | 0.50 | 837 |
| stroke 69 | 40 % → 10 % | 214.4 px | 0.23 | 0.26 | 687 |
| stroke 70 | 44 % → 5 % | 234.5 px | 0.21 | 0.11 | 907 |
| stroke 71 | 45 % → 0 % | 247.4 px | 0.23 | 0.00 | 841 |
| stroke 72 | 5 % → 25 % | 106.1 px | 0.24 | 4.60 | 202 |
| stroke 73 | 11 % → 24 % | 135.0 px | 0.24 | 2.13 | 458 |
| stroke 74 | 16 % → 29 % | 171.7 px | 0.24 | 1.84 | 324 |
| stroke 75 | 20 % → 34 % | 303.0 px | 0.23 | 1.72 | 332 |
| stroke 76 | 24 % → 38 % | 552.0 px | 0.23 | 1.62 | 147 |
| stroke 77 | 18 % → 32 % | 289.8 px | 0.23 | 1.82 | 181 |
| stroke 78 | 21 % → 40 % | 308.3 px | 0.22 | 1.90 | 225 |
| stroke 79 | 1 % → 0 % | 25.2 px | 0.00 | 0.00 | 30 |
| stroke 80 | 11 % → 0 % | 91.9 px | 0.00 | 0.00 | 533 |
| stroke 81 | 21 % → 0 % | 114.2 px | 0.23 | 0.01 | 941 |
| stroke 82 | 28 % → 0 % | 154.4 px | 0.24 | 0.01 | 701 |
| stroke 83 | 36 % → 0 % | 196.6 px | 0.23 | 0.00 | 898 |
| stroke 84 | 44 % → 0 % | 237.4 px | 0.26 | 0.00 | 689 |
| stroke 85 | 47 % → 2 % | 262.7 px | 0.26 | 0.04 | 687 |
| stroke 86 | 46 % → 6 % | 318.2 px | 0.26 | 0.14 | 565 |
| stroke 87 | 1 % → 0 % | 13.2 px | 0.00 | 0.00 | 9 |
| stroke 88 | 7 % → 44 % | 20.7 px | 0.23 | 6.76 | 147 |
| stroke 89 | 5 % → 0 % | 24.3 px | 0.00 | 0.00 | 131 |
| stroke 90 | 7 % → 11 % | 116.2 px | 0.24 | 1.54 | 164 |
| stroke 91 | 11 % → 11 % | 182.0 px | 0.24 | 0.96 | 132 |
| stroke 92 | 14 % → 51 % | 99.4 px | 0.24 | 3.61 | 370 |
| stroke 93 | 19 % → 48 % | 120.7 px | 0.24 | 2.55 | 1686 |
| stroke 94 | 24 % → 50 % | 206.9 px | 0.24 | 2.12 | 425 |
| stroke 95 | 28 % → 49 % | 240.8 px | 0.24 | 1.76 | 721 |
| stroke 96 | 37 % → 49 % | 220.3 px | 0.24 | 1.33 | 733 |
| stroke 97 | 39 % → 44 % | 231.6 px | 0.24 | 1.13 | 773 |
| stroke 98 | 43 % → 42 % | 270.8 px | 0.24 | 0.98 | 652 |
| stroke 99 | 11 % → 27 % | 97.5 px | 0.24 | 2.52 | 391 |
| stroke 100 | 16 % → 31 % | 154.7 px | 0.24 | 1.97 | 637 |
| stroke 101 | 21 % → 39 % | 241.6 px | 0.24 | 1.82 | 280 |
| stroke 102 | 26 % → 47 % | 338.1 px | 0.23 | 1.79 | 265 |
| stroke 103 | 28 % → 42 % | 277.6 px | 0.23 | 1.52 | 374 |
| stroke 104 | 28 % → 39 % | 288.9 px | 0.23 | 1.38 | 273 |
| stroke 105 | 28 % → 35 % | 278.1 px | 0.23 | 1.25 | 653 |
| stroke 106 | 30 % → 32 % | 254.0 px | 0.23 | 1.06 | 352 |
| stroke 107 | 43 % → 43 % | 775.6 px | 0.23 | 0.99 | 146 |

Numbers say: wet paint spreads well beyond the stroke.

## Refs v3 · #35 Red band with runs — own sheet
own sheet 800 × 1191 · Watercolour 1.00 + water 70 % · 176 px · 32.2 s

![Refs v3 · #35 Red band with runs — own sheet](Refs-v3-35-Red-band-with-runs-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 40 % → 46 % | 297.4 px | 0.35 | 1.15 | 5198 |

## Refs v3 · #36 Magenta letters flat — own sheet
own sheet 800 × 1000 · Gouache 1.00 + water 15 % · 64 px · 37.6 s

![Refs v3 · #36 Magenta letters flat — own sheet](Refs-v3-36-Magenta-letters-flat-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 3 % → 37 % | 75.3 px | 0.40 | 10.99 | 27 |
| stroke 2 | 6 % → 35 % | 200.8 px | 0.40 | 5.81 | 23 |
| stroke 3 | 7 % → 26 % | 98.4 px | 0.40 | 3.84 | 17 |
| stroke 4 | 12 % → 31 % | 149.7 px | 0.40 | 2.58 | 31 |
| stroke 5 | 21 % → 35 % | 126.6 px | 0.41 | 1.69 | 162 |
| stroke 6 | 9 % → 31 % | 62.9 px | 0.40 | 3.38 | 118 |
| stroke 7 | 26 % → 39 % | 183.9 px | 0.40 | 1.51 | 107 |
| stroke 8 | 5 % → 43 % | 77.6 px | 0.40 | 7.92 | 68 |
| stroke 9 | 9 % → 42 % | 143.4 px | 0.40 | 4.57 | 51 |
| stroke 10 | 14 % → 33 % | 176.5 px | 0.40 | 2.33 | 68 |
| stroke 11 | 19 % → 37 % | 227.8 px | 0.40 | 1.95 | 65 |
| stroke 12 | 22 % → 38 % | 326.9 px | 0.40 | 1.69 | 121 |
| stroke 13 | 39 % → 42 % | 200.3 px | 0.40 | 1.08 | 212 |
| stroke 14 | 26 % → 33 % | 76.3 px | 0.41 | 1.26 | 430 |
| stroke 15 | 11 % → 41 % | 242.3 px | 0.41 | 3.60 | 70 |
| stroke 16 | 18 % → 42 % | 135.6 px | 0.40 | 2.30 | 184 |
| stroke 17 | 29 % → 42 % | 284.3 px | 0.40 | 1.46 | 151 |
| stroke 18 | 29 % → 43 % | 456.5 px | 0.40 | 1.51 | 47 |
| stroke 19 | 30 % → 43 % | 310.3 px | 0.40 | 1.43 | 140 |
| stroke 20 | 16 % → 40 % | 584.4 px | 0.41 | 2.55 | 21 |
| stroke 21 | 27 % → 45 % | 125.2 px | 0.41 | 1.65 | 363 |
| stroke 22 | 23 % → 45 % | 181.3 px | 0.41 | 1.93 | 127 |
| stroke 23 | 17 % → 48 % | 199.9 px | 0.41 | 2.79 | 113 |
| stroke 24 | 11 % → 50 % | 107.5 px | 0.41 | 4.59 | 179 |
| stroke 25 | 27 % → 37 % | 330.0 px | 0.40 | 1.38 | 79 |
| stroke 26 | 37 % → 40 % | 450.6 px | 0.41 | 1.10 | 61 |
| stroke 27 | 36 % → 40 % | 445.3 px | 0.41 | 1.11 | 95 |
| stroke 28 | 6 % → 52 % | 65.5 px | 0.41 | 8.25 | 127 |
| stroke 29 | 31 % → 41 % | 157.6 px | 0.40 | 1.33 | 283 |
| stroke 30 | 41 % → 47 % | 257.9 px | 0.41 | 1.15 | 154 |
| stroke 31 | 31 % → 43 % | 94.5 px | 0.41 | 1.36 | 692 |
| stroke 32 | 31 % → 45 % | 115.2 px | 0.41 | 1.43 | 343 |
| stroke 33 | 21 % → 45 % | 340.4 px | 0.41 | 2.14 | 109 |
| stroke 34 | 12 % → 46 % | 151.6 px | 0.41 | 3.72 | 60 |
| stroke 35 | 36 % → 43 % | 244.8 px | 0.41 | 1.20 | 177 |
| stroke 36 | 33 % → 40 % | 377.7 px | 0.41 | 1.19 | 117 |
| stroke 37 | 13 % → 35 % | 108.0 px | 0.42 | 2.74 | 79 |
| stroke 38 | 28 % → 44 % | 321.6 px | 0.41 | 1.56 | 56 |
| stroke 39 | 26 % → 37 % | 220.8 px | 0.42 | 1.43 | 103 |
| stroke 40 | 11 % → 28 % | 197.9 px | 0.42 | 2.53 | 35 |
| stroke 41 | 23 % → 35 % | 301.4 px | 0.42 | 1.53 | 58 |
| stroke 42 | 34 % → 36 % | 256.2 px | 0.42 | 1.05 | 152 |
| stroke 43 | 31 % → 31 % | 709.4 px | 0.42 | 1.00 | 26 |
| stroke 44 | 40 % → 40 % | 320.5 px | 0.41 | 1.01 | 68 |

Numbers say: wet paint spreads well beyond the stroke.

## Refs v3 · #37 Oil still life — own sheet
own sheet 800 × 810 · Gouache 1.00 + turpentine 20 % · 28 px · 62.9 s

![Refs v3 · #37 Oil still life — own sheet](Refs-v3-37-Oil-still-life-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 4 % → 0 % | 35.5 px | 0.00 | 0.00 | 14 |
| stroke 2 | 8 % → 0 % | 55.5 px | 0.00 | 0.00 | 9 |
| stroke 3 | 10 % → 0 % | 46.0 px | 0.00 | 0.00 | 48 |
| stroke 4 | 18 % → 0 % | 168.1 px | 0.00 | 0.00 | 6 |
| stroke 5 | 21 % → 0 % | 191.8 px | 0.00 | 0.00 | 4 |
| stroke 6 | 20 % → 0 % | 86.7 px | 0.00 | 0.00 | 28 |
| stroke 7 | 20 % → 0 % | 72.2 px | 0.00 | 0.00 | 76 |
| stroke 8 | 25 % → 0 % | 90.2 px | 0.00 | 0.00 | 67 |
| stroke 9 | 28 % → 0 % | 101.5 px | 0.00 | 0.00 | 101 |
| stroke 10 | 30 % → 0 % | 105.9 px | 0.00 | 0.00 | 45 |
| stroke 11 | 20 % → 0 % | 98.6 px | 0.00 | 0.00 | 30 |
| stroke 12 | 19 % → 0 % | 79.8 px | 0.00 | 0.00 | 40 |
| stroke 13 | 16 % → 0 % | 112.6 px | 0.00 | 0.00 | 12 |
| stroke 14 | 40 % → 0 % | 164.3 px | 0.00 | 0.00 | 71 |
| stroke 15 | 20 % → 0 % | 166.8 px | 0.00 | 0.00 | 11 |
| stroke 16 | 37 % → 0 % | 140.5 px | 0.00 | 0.00 | 36 |
| stroke 17 | 8 % → 0 % | 35.4 px | 0.00 | 0.00 | 16 |
| stroke 18 | 22 % → 0 % | 55.0 px | 0.00 | 0.00 | 66 |
| stroke 19 | 36 % → 0 % | 96.0 px | 0.00 | 0.00 | 57 |
| stroke 20 | 8 % → 11 % | 30.9 px | 0.15 | 1.30 | 37 |
| stroke 21 | 13 % → 12 % | 52.9 px | 0.15 | 0.89 | 24 |
| stroke 22 | 19 % → 13 % | 96.5 px | 0.15 | 0.72 | 16 |
| stroke 23 | 4 % → 7 % | 21.3 px | 0.15 | 1.68 | 11 |
| stroke 24 | 15 % → 0 % | 50.0 px | 0.00 | 0.00 | 45 |
| stroke 25 | 27 % → 0 % | 57.3 px | 0.00 | 0.00 | 132 |
| stroke 26 | 37 % → 0 % | 82.8 px | 0.00 | 0.00 | 103 |
| stroke 27 | 47 % → 0 % | 114.2 px | 0.00 | 0.00 | 138 |
| stroke 28 | 12 % → 0 % | 51.8 px | 0.00 | 0.00 | 68 |
| stroke 29 | 19 % → 0 % | 81.0 px | 0.00 | 0.00 | 38 |
| stroke 30 | 25 % → 0 % | 107.3 px | 0.00 | 0.00 | 47 |
| stroke 31 | 19 % → 0 % | 109.8 px | 0.00 | 0.00 | 26 |
| stroke 32 | 23 % → 0 % | 86.5 px | 0.00 | 0.00 | 76 |
| stroke 33 | 30 % → 0 % | 195.1 px | 0.00 | 0.00 | 13 |
| stroke 34 | 11 % → 0 % | 53.3 px | 0.00 | 0.00 | 31 |
| stroke 35 | 17 % → 0 % | 69.5 px | 0.00 | 0.00 | 41 |
| stroke 36 | 26 % → 0 % | 111.4 px | 0.00 | 0.00 | 30 |
| stroke 37 | 34 % → 0 % | 223.2 px | 0.00 | 0.00 | 12 |
| stroke 38 | 11 % → 0 % | 52.8 px | 0.00 | 0.00 | 17 |
| stroke 39 | 17 % → 2 % | 59.1 px | 0.15 | 0.09 | 62 |
| stroke 40 | 25 % → 1 % | 102.2 px | 0.15 | 0.04 | 79 |
| stroke 41 | 12 % → 0 % | 39.2 px | 0.00 | 0.00 | 42 |
| stroke 42 | 17 % → 0 % | 48.6 px | 0.00 | 0.00 | 112 |
| stroke 43 | 22 % → 0 % | 58.3 px | 0.00 | 0.00 | 168 |
| stroke 44 | 29 % → 0 % | 108.9 px | 0.00 | 0.00 | 39 |
| stroke 45 | 30 % → 0 % | 112.6 px | 0.00 | 0.00 | 42 |
| stroke 46 | 49 % → 0 % | 153.0 px | 0.00 | 0.00 | 57 |
| stroke 47 | 30 % → 0 % | 192.9 px | 0.00 | 0.00 | 14 |
| stroke 48 | 44 % → 0 % | 124.4 px | 0.00 | 0.00 | 124 |
| stroke 49 | 28 % → 0 % | 247.6 px | 0.00 | 0.00 | 8 |
| stroke 50 | 38 % → 0 % | 158.0 px | 0.00 | 0.00 | 88 |
| stroke 51 | 54 % → 0 % | 181.9 px | 0.00 | 0.00 | 51 |
| stroke 52 | 36 % → 0 % | 236.5 px | 0.00 | 0.00 | 21 |
| stroke 53 | 46 % → 0 % | 209.8 px | 0.00 | 0.00 | 82 |
| stroke 54 | 4 % → 0 % | 28.9 px | 0.00 | 0.00 | 12 |
| stroke 55 | 5 % → 0 % | 48.9 px | 0.00 | 0.00 | 10 |
| stroke 56 | 12 % → 0 % | 46.5 px | 0.00 | 0.00 | 27 |
| stroke 57 | 19 % → 0 % | 89.0 px | 0.00 | 0.00 | 18 |
| stroke 58 | 25 % → 0 % | 142.2 px | 0.00 | 0.00 | 20 |
| stroke 59 | 14 % → 0 % | 59.8 px | 0.00 | 0.00 | 42 |
| stroke 60 | 21 % → 0 % | 101.0 px | 0.00 | 0.00 | 25 |
| stroke 61 | 29 % → 0 % | 64.3 px | 0.00 | 0.00 | 133 |
| stroke 62 | 41 % → 0 % | 65.2 px | 0.00 | 0.00 | 320 |
| stroke 63 | 10 % → 0 % | 62.8 px | 0.00 | 0.00 | 15 |
| stroke 64 | 60 % → 0 % | 81.3 px | 0.00 | 0.00 | 335 |
| stroke 65 | 75 % → 0 % | 86.0 px | 0.00 | 0.00 | 388 |
| stroke 66 | 66 % → 0 % | 75.0 px | 0.00 | 0.00 | 544 |
| stroke 67 | 69 % → 0 % | 76.5 px | 0.00 | 0.00 | 124 |
| stroke 68 | 14 % → 5 % | 57.2 px | 0.13 | 0.35 | 48 |
| stroke 69 | 27 % → 4 % | 90.3 px | 0.13 | 0.15 | 57 |
| stroke 70 | 31 % → 3 % | 91.9 px | 0.13 | 0.10 | 89 |
| stroke 71 | 40 % → 4 % | 136.1 px | 0.13 | 0.10 | 135 |
| stroke 72 | 40 % → 3 % | 135.9 px | 0.12 | 0.07 | 59 |
| stroke 73 | 40 % → 1 % | 121.1 px | 0.11 | 0.02 | 107 |
| stroke 74 | 47 % → 0 % | 179.6 px | 0.00 | 0.00 | 57 |
| stroke 75 | 49 % → 0 % | 258.1 px | 0.00 | 0.00 | 52 |
| stroke 76 | 11 % → 0 % | 59.3 px | 0.00 | 0.00 | 34 |
| stroke 77 | 22 % → 0 % | 86.0 px | 0.00 | 0.00 | 77 |
| stroke 78 | 23 % → 0 % | 78.9 px | 0.00 | 0.00 | 111 |
| stroke 79 | 36 % → 0 % | 250.4 px | 0.00 | 0.00 | 24 |
| stroke 80 | 37 % → 0 % | 139.2 px | 0.00 | 0.00 | 81 |
| stroke 81 | 37 % → 0 % | 185.2 px | 0.00 | 0.00 | 51 |
| stroke 82 | 45 % → 0 % | 167.3 px | 0.00 | 0.00 | 97 |
| stroke 83 | 26 % → 0 % | 96.5 px | 0.00 | 0.00 | 283 |
| stroke 84 | 34 % → 0 % | 143.7 px | 0.00 | 0.00 | 49 |
| stroke 85 | 59 % → 0 % | 404.4 px | 0.00 | 0.00 | 18 |
| stroke 86 | 45 % → 0 % | 171.2 px | 0.00 | 0.00 | 98 |
| stroke 87 | 37 % → 0 % | 179.0 px | 0.00 | 0.00 | 54 |
| stroke 88 | 37 % → 0 % | 139.8 px | 0.00 | 0.00 | 160 |
| stroke 89 | 31 % → 0 % | 113.0 px | 0.00 | 0.00 | 131 |
| stroke 90 | 48 % → 0 % | 329.9 px | 0.00 | 0.00 | 22 |
| stroke 91 | 33 % → 0 % | 185.9 px | 0.00 | 0.00 | 44 |
| stroke 92 | 42 % → 0 % | 237.7 px | 0.00 | 0.00 | 31 |
| stroke 93 | 22 % → 0 % | 152.4 px | 0.00 | 0.00 | 33 |
| stroke 94 | 35 % → 0 % | 241.1 px | 0.00 | 0.00 | 16 |
| stroke 95 | 33 % → 0 % | 182.9 px | 0.00 | 0.00 | 45 |
| stroke 96 | 31 % → 0 % | 168.9 px | 0.00 | 0.00 | 47 |
| stroke 97 | 15 % → 0 % | 60.7 px | 0.00 | 0.00 | 21 |
| stroke 98 | 33 % → 0 % | 131.3 px | 0.00 | 0.00 | 222 |
| stroke 99 | 29 % → 0 % | 83.2 px | 0.00 | 0.00 | 84 |
| stroke 100 | 33 % → 0 % | 119.0 px | 0.00 | 0.00 | 128 |
| stroke 101 | 37 % → 0 % | 111.6 px | 0.00 | 0.00 | 56 |
| stroke 102 | 39 % → 0 % | 147.8 px | 0.00 | 0.00 | 133 |
| stroke 103 | 46 % → 0 % | 203.1 px | 0.00 | 0.00 | 25 |
| stroke 104 | 50 % → 0 % | 243.7 px | 0.00 | 0.00 | 67 |
| stroke 105 | 15 % → 0 % | 104.7 px | 0.00 | 0.00 | 21 |
| stroke 106 | 39 % → 0 % | 144.5 px | 0.00 | 0.00 | 47 |
| stroke 107 | 17 % → 0 % | 86.9 px | 0.00 | 0.00 | 37 |
| stroke 108 | 39 % → 0 % | 146.6 px | 0.00 | 0.00 | 30 |
| stroke 109 | 23 % → 0 % | 86.5 px | 0.00 | 0.00 | 50 |
| stroke 110 | 28 % → 0 % | 73.6 px | 0.00 | 0.00 | 107 |
| stroke 111 | 27 % → 0 % | 184.2 px | 0.00 | 0.00 | 17 |
| stroke 112 | 29 % → 0 % | 112.8 px | 0.00 | 0.00 | 82 |
| stroke 113 | 34 % → 0 % | 91.4 px | 0.00 | 0.00 | 114 |
| stroke 114 | 45 % → 0 % | 156.3 px | 0.00 | 0.00 | 103 |
| stroke 115 | 42 % → 0 % | 124.8 px | 0.00 | 0.00 | 218 |
| stroke 116 | 49 % → 0 % | 138.8 px | 0.00 | 0.00 | 222 |
| stroke 117 | 71 % → 0 % | 208.7 px | 0.00 | 0.00 | 44 |
| stroke 118 | 50 % → 0 % | 223.3 px | 0.00 | 0.00 | 44 |
| stroke 119 | 73 % → 0 % | 330.9 px | 0.00 | 0.00 | 14 |
| stroke 120 | 47 % → 0 % | 324.2 px | 0.00 | 0.00 | 24 |
| stroke 121 | 60 % → 0 % | 172.4 px | 0.00 | 0.00 | 88 |
| stroke 122 | 56 % → 0 % | 205.2 px | 0.00 | 0.00 | 29 |
| stroke 123 | 13 % → 9 % | 58.8 px | 0.15 | 0.65 | 54 |
| stroke 124 | 24 % → 16 % | 161.8 px | 0.15 | 0.66 | 26 |
| stroke 125 | 13 % → 0 % | 89.1 px | 0.00 | 0.00 | 16 |
| stroke 126 | 20 % → 4 % | 114.9 px | 0.15 | 0.21 | 30 |
| stroke 127 | 19 % → 9 % | 128.8 px | 0.15 | 0.47 | 49 |
| stroke 128 | 14 % → 8 % | 59.2 px | 0.15 | 0.61 | 35 |
| stroke 129 | 22 % → 0 % | 77.5 px | 0.00 | 0.00 | 47 |
| stroke 130 | 30 % → 4 % | 88.0 px | 0.15 | 0.14 | 104 |
| stroke 131 | 40 % → 9 % | 99.5 px | 0.15 | 0.22 | 200 |
| stroke 132 | 40 % → 13 % | 127.2 px | 0.15 | 0.32 | 80 |
| stroke 133 | 7 % → 13 % | 25.8 px | 0.15 | 1.71 | 58 |
| stroke 134 | 11 % → 0 % | 55.7 px | 0.00 | 0.00 | 42 |
| stroke 135 | 18 % → 0 % | 60.7 px | 0.00 | 0.00 | 114 |
| stroke 136 | 23 % → 0 % | 81.5 px | 0.00 | 0.00 | 170 |
| stroke 137 | 27 % → 0 % | 90.0 px | 0.00 | 0.00 | 124 |
| stroke 138 | 35 % → 0 % | 118.7 px | 0.00 | 0.00 | 114 |
| stroke 139 | 42 % → 0 % | 141.3 px | 0.00 | 0.00 | 102 |
| stroke 140 | 50 % → 0 % | 241.8 px | 0.00 | 0.00 | 45 |
| stroke 141 | 53 % → 0 % | 284.6 px | 0.00 | 0.00 | 22 |
| stroke 142 | 48 % → 0 % | 231.4 px | 0.00 | 0.00 | 29 |
| stroke 143 | 55 % → 0 % | 363.0 px | 0.00 | 0.00 | 29 |
| stroke 144 | 43 % → 0 % | 232.2 px | 0.00 | 0.00 | 73 |
| stroke 145 | 21 % → 0 % | 139.3 px | 0.00 | 0.00 | 41 |
| stroke 146 | 37 % → 0 % | 231.7 px | 0.00 | 0.00 | 19 |
| stroke 147 | 42 % → 0 % | 269.9 px | 0.00 | 0.00 | 16 |
| stroke 148 | 10 % → 0 % | 56.8 px | 0.00 | 0.00 | 25 |
| stroke 149 | 9 % → 7 % | 60.5 px | 0.16 | 0.84 | 12 |
| stroke 150 | 16 % → 8 % | 60.8 px | 0.15 | 0.51 | 52 |
| stroke 151 | 25 % → 4 % | 111.0 px | 0.16 | 0.17 | 36 |
| stroke 152 | 29 % → 6 % | 107.9 px | 0.16 | 0.20 | 60 |
| stroke 153 | 27 % → 0 % | 177.3 px | 0.00 | 0.00 | 13 |
| stroke 154 | 33 % → 0 % | 139.5 px | 0.00 | 0.00 | 69 |
| stroke 155 | 47 % → 0 % | 313.4 px | 0.00 | 0.00 | 19 |
| stroke 156 | 26 % → 0 % | 144.9 px | 0.18 | 0.01 | 43 |
| stroke 157 | 45 % → 0 % | 166.6 px | 0.00 | 0.00 | 82 |
| stroke 158 | 39 % → 0 % | 269.0 px | 0.00 | 0.00 | 19 |
| stroke 159 | 44 % → 0 % | 178.1 px | 0.00 | 0.00 | 44 |
| stroke 160 | 22 % → 9 % | 148.6 px | 0.16 | 0.41 | 16 |
| stroke 161 | 47 % → 0 % | 193.5 px | 0.00 | 0.00 | 56 |
| stroke 162 | 30 % → 4 % | 164.3 px | 0.16 | 0.15 | 22 |
| stroke 163 | 38 % → 0 % | 138.5 px | 0.18 | 0.00 | 86 |
| stroke 164 | 44 % → 0 % | 168.3 px | 0.00 | 0.00 | 56 |
| stroke 165 | 41 % → 0 % | 168.8 px | 0.00 | 0.00 | 45 |
| stroke 166 | 54 % → 0 % | 298.4 px | 0.00 | 0.00 | 33 |
| stroke 167 | 19 % → 0 % | 127.8 px | 0.00 | 0.00 | 15 |
| stroke 168 | 50 % → 0 % | 203.0 px | 0.00 | 0.00 | 55 |
| stroke 169 | 49 % → 0 % | 234.7 px | 0.00 | 0.00 | 38 |
| stroke 170 | 49 % → 0 % | 241.5 px | 0.13 | 0.01 | 25 |
| stroke 171 | 7 % → 0 % | 29.2 px | 0.00 | 0.00 | 24 |
| stroke 172 | 9 % → 0 % | 30.5 px | 0.13 | 0.01 | 94 |
| stroke 173 | 22 % → 0 % | 187.1 px | 0.00 | 0.00 | 13 |
| stroke 174 | 16 % → 0 % | 146.3 px | 0.00 | 0.00 | 19 |
| stroke 175 | 10 % → 0 % | 93.2 px | 0.00 | 0.00 | 7 |
| stroke 176 | 10 % → 0 % | 91.6 px | 0.00 | 0.00 | 22 |
| stroke 177 | 9 % → 0 % | 81.2 px | 0.00 | 0.00 | 10 |
| stroke 178 | 11 % → 0 % | 95.2 px | 0.00 | 0.00 | 14 |
| stroke 179 | 9 % → 0 % | 84.9 px | 0.00 | 0.00 | 11 |
| stroke 180 | 13 % → 0 % | 122.2 px | 0.00 | 0.00 | 6 |
| stroke 181 | 15 % → 0 % | 141.0 px | 0.00 | 0.00 | 8 |
| stroke 182 | 17 % → 0 % | 158.5 px | 0.00 | 0.00 | 9 |
| stroke 183 | 17 % → 0 % | 84.3 px | 0.00 | 0.00 | 18 |
| stroke 184 | 19 % → 0 % | 87.3 px | 0.00 | 0.00 | 28 |
| stroke 185 | 23 % → 0 % | 104.8 px | 0.00 | 0.00 | 50 |
| stroke 186 | 25 % → 0 % | 104.2 px | 0.00 | 0.00 | 41 |
| stroke 187 | 26 % → 0 % | 153.3 px | 0.00 | 0.00 | 59 |
| stroke 188 | 15 % → 0 % | 106.7 px | 0.00 | 0.00 | 30 |
| stroke 189 | 18 % → 0 % | 97.9 px | 0.00 | 0.00 | 35 |
| stroke 190 | 19 % → 0 % | 108.9 px | 0.00 | 0.00 | 24 |
| stroke 191 | 21 % → 0 % | 116.3 px | 0.00 | 0.00 | 22 |
| stroke 192 | 24 % → 0 % | 201.2 px | 0.00 | 0.00 | 7 |
| stroke 193 | 23 % → 0 % | 142.3 px | 0.00 | 0.00 | 17 |
| stroke 194 | 10 % → 0 % | 53.6 px | 0.00 | 0.00 | 13 |
| stroke 195 | 16 % → 0 % | 64.1 px | 0.00 | 0.00 | 129 |
| stroke 196 | 24 % → 0 % | 161.0 px | 0.00 | 0.00 | 25 |
| stroke 197 | 18 % → 0 % | 71.7 px | 0.00 | 0.00 | 69 |
| stroke 198 | 21 % → 0 % | 117.6 px | 0.00 | 0.00 | 23 |
| stroke 199 | 24 % → 0 % | 101.6 px | 0.00 | 0.00 | 49 |
| stroke 200 | 34 % → 0 % | 237.6 px | 0.00 | 0.00 | 44 |
| stroke 201 | 29 % → 0 % | 254.0 px | 0.00 | 0.00 | 8 |
| stroke 202 | 37 % → 0 % | 331.4 px | 0.00 | 0.00 | 10 |
| stroke 203 | 4 % → 0 % | 29.7 px | 0.00 | 0.00 | 11 |
| stroke 204 | 9 % → 0 % | 79.7 px | 0.00 | 0.00 | 6 |
| stroke 205 | 4 % → 0 % | 40.6 px | 0.00 | 0.00 | 9 |
| stroke 206 | 9 % → 0 % | 76.4 px | 0.00 | 0.00 | 6 |
| stroke 207 | 13 % → 0 % | 86.7 px | 0.00 | 0.00 | 23 |
| stroke 208 | 12 % → 0 % | 80.1 px | 0.00 | 0.00 | 7 |
| stroke 209 | 14 % → 0 % | 99.3 px | 0.00 | 0.00 | 20 |
| stroke 210 | 13 % → 0 % | 65.3 px | 0.00 | 0.00 | 26 |
| stroke 211 | 14 % → 0 % | 76.7 px | 0.00 | 0.00 | 14 |
| stroke 212 | 4 % → 15 % | 35.0 px | 0.15 | 3.98 | 5 |
| stroke 213 | 8 % → 12 % | 41.1 px | 0.15 | 1.44 | 13 |
| stroke 214 | 11 % → 9 % | 48.9 px | 0.15 | 0.77 | 28 |
| stroke 215 | 5 % → 7 % | 33.0 px | 0.13 | 1.39 | 8 |
| stroke 216 | 8 % → 12 % | 27.7 px | 0.15 | 1.39 | 53 |
| stroke 217 | 8 % → 10 % | 24.6 px | 0.15 | 1.20 | 44 |

Numbers say: wet paint spreads well beyond the stroke.

## Refs v3 · #38 Sanguine drawing — own sheet
own sheet 800 × 1092 · Charcoal 0.50 · Pastel 0.50 · 12 px · 43.0 s

![Refs v3 · #38 Sanguine drawing — own sheet](Refs-v3-38-Sanguine-drawing-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 7 % → 29 % | 13.6 px | 0.53 | 4.07 | 5 |
| stroke 2 | 11 % → 32 % | 17.3 px | 0.53 | 2.89 | 4 |
| stroke 3 | 21 % → 27 % | 33.7 px | 0.53 | 1.27 | 3 |
| stroke 4 | 28 % → 23 % | 62.1 px | 0.53 | 0.80 | 1 |
| stroke 5 | 12 % → 19 % | 20.0 px | 0.53 | 1.55 | 4 |
| stroke 6 | 14 % → 24 % | 22.4 px | 0.53 | 1.69 | 11 |
| stroke 7 | 16 % → 37 % | 26.3 px | 0.53 | 2.28 | 17 |
| stroke 8 | 14 % → 36 % | 23.1 px | 0.53 | 2.62 | 4 |
| stroke 9 | 13 % → 44 % | 23.7 px | 0.53 | 3.35 | 7 |
| stroke 10 | 9 % → 28 % | 12.3 px | 0.54 | 3.25 | 6 |
| stroke 11 | 8 % → 59 % | 10.5 px | 0.54 | 7.87 | 3 |
| stroke 12 | 6 % → 40 % | 10.5 px | 0.53 | 6.58 | 1 |
| stroke 13 | 7 % → 36 % | 11.1 px | 0.53 | 5.10 | 9 |
| stroke 14 | 13 % → 30 % | 36.2 px | 0.53 | 2.23 | 0 |
| stroke 15 | 17 % → 33 % | 23.2 px | 0.53 | 1.95 | 3 |
| stroke 16 | 31 % → 25 % | 55.0 px | 0.53 | 0.82 | 4 |
| stroke 17 | 5 % → 5 % | 14.2 px | 0.53 | 0.92 | 1 |
| stroke 18 | 11 % → 15 % | 18.7 px | 0.53 | 1.28 | 3 |
| stroke 19 | 16 % → 28 % | 34.3 px | 0.53 | 1.76 | 2 |
| stroke 20 | 10 % → 43 % | 30.1 px | 0.54 | 4.11 | 0 |
| stroke 21 | 16 % → 53 % | 41.4 px | 0.54 | 3.26 | 1 |
| stroke 22 | 5 % → 60 % | 14.7 px | 0.54 | 11.14 | 0 |
| stroke 23 | 7 % → 40 % | 11.9 px | 0.53 | 5.56 | 3 |
| stroke 24 | 13 % → 35 % | 19.1 px | 0.53 | 2.75 | 3 |
| stroke 25 | 7 % → 8 % | 17.8 px | 0.53 | 1.12 | 0 |
| stroke 26 | 21 % → 24 % | 34.3 px | 0.53 | 1.14 | 1 |
| stroke 27 | 10 % → 0 % | 27.0 px | 0.00 | 0.00 | 1 |
| stroke 28 | 10 % → 14 % | 20.9 px | 0.53 | 1.37 | 1 |
| stroke 29 | 7 % → 24 % | 12.0 px | 0.53 | 3.36 | 4 |
| stroke 30 | 16 % → 27 % | 25.6 px | 0.53 | 1.68 | 6 |
| stroke 31 | 12 % → 22 % | 26.3 px | 0.53 | 1.77 | 1 |
| stroke 32 | 7 % → 46 % | 17.4 px | 0.53 | 7.04 | 0 |
| stroke 33 | 13 % → 28 % | 25.0 px | 0.53 | 2.16 | 4 |
| stroke 34 | 6 % → 23 % | 14.9 px | 0.53 | 3.94 | 1 |
| stroke 35 | 9 % → 18 % | 10.6 px | 0.53 | 1.94 | 3 |
| stroke 36 | 20 % → 11 % | 19.3 px | 0.53 | 0.52 | 13 |
| stroke 37 | 9 % → 13 % | 23.7 px | 0.54 | 1.42 | 1 |
| stroke 38 | 24 % → 1 % | 46.3 px | 0.52 | 0.06 | 1 |
| stroke 39 | 19 % → 22 % | 36.0 px | 0.53 | 1.17 | 3 |
| stroke 40 | 7 % → 29 % | 13.5 px | 0.53 | 4.25 | 1 |
| stroke 41 | 16 % → 13 % | 23.0 px | 0.54 | 0.79 | 1 |
| stroke 42 | 14 % → 34 % | 19.4 px | 0.53 | 2.44 | 2 |
| stroke 43 | 17 % → 22 % | 20.8 px | 0.53 | 1.29 | 4 |
| stroke 44 | 7 % → 23 % | 13.2 px | 0.53 | 3.43 | 1 |
| stroke 45 | 18 % → 19 % | 25.4 px | 0.53 | 1.08 | 3 |
| stroke 46 | 18 % → 32 % | 20.3 px | 0.53 | 1.75 | 4 |
| stroke 47 | 20 % → 5 % | 38.7 px | 0.53 | 0.25 | 1 |
| stroke 48 | 21 % → 38 % | 26.2 px | 0.53 | 1.86 | 2 |
| stroke 49 | 14 % → 17 % | 16.4 px | 0.53 | 1.17 | 3 |
| stroke 50 | 20 % → 24 % | 17.6 px | 0.53 | 1.19 | 10 |
| stroke 51 | 23 % → 32 % | 26.6 px | 0.53 | 1.38 | 5 |
| stroke 52 | 28 % → 18 % | 35.8 px | 0.53 | 0.65 | 2 |
| stroke 53 | 21 % → 35 % | 29.0 px | 0.53 | 1.70 | 3 |
| stroke 54 | 8 % → 38 % | 12.0 px | 0.53 | 4.69 | 1 |
| stroke 55 | 17 % → 39 % | 45.4 px | 0.53 | 2.25 | 1 |
| stroke 56 | 15 % → 39 % | 39.6 px | 0.53 | 2.58 | 0 |
| stroke 57 | 10 % → 42 % | 16.0 px | 0.53 | 4.37 | 5 |
| stroke 58 | 10 % → 33 % | 16.0 px | 0.53 | 3.24 | 3 |
| stroke 59 | 17 % → 35 % | 27.1 px | 0.53 | 2.10 | 5 |
| stroke 60 | 25 % → 33 % | 49.5 px | 0.53 | 1.31 | 2 |
| stroke 61 | 21 % → 39 % | 63.3 px | 0.53 | 1.83 | 5 |
| stroke 62 | 9 % → 46 % | 27.0 px | 0.53 | 4.94 | 0 |
| stroke 63 | 7 % → 27 % | 11.7 px | 0.53 | 3.76 | 2 |
| stroke 64 | 8 % → 55 % | 17.1 px | 0.54 | 6.94 | 1 |
| stroke 65 | 5 % → 5 % | 13.7 px | 0.53 | 0.99 | 0 |
| stroke 66 | 11 % → 11 % | 28.2 px | 0.53 | 1.07 | 1 |
| stroke 67 | 11 % → 25 % | 27.2 px | 0.53 | 2.36 | 0 |
| stroke 68 | 5 % → 32 % | 13.2 px | 0.53 | 6.10 | 0 |
| stroke 69 | 10 % → 40 % | 15.0 px | 0.54 | 3.88 | 2 |
| stroke 70 | 7 % → 37 % | 13.2 px | 0.54 | 5.51 | 4 |
| stroke 71 | 9 % → 36 % | 13.1 px | 0.53 | 3.84 | 3 |
| stroke 72 | 13 % → 36 % | 15.2 px | 0.53 | 2.80 | 8 |
| stroke 73 | 13 % → 27 % | 16.7 px | 0.53 | 2.14 | 6 |
| stroke 74 | 17 % → 20 % | 20.2 px | 0.53 | 1.17 | 7 |
| stroke 75 | 19 % → 23 % | 31.3 px | 0.53 | 1.24 | 3 |
| stroke 76 | 11 % → 28 % | 18.0 px | 0.53 | 2.43 | 5 |
| stroke 77 | 9 % → 31 % | 25.6 px | 0.53 | 3.48 | 0 |
| stroke 78 | 21 % → 25 % | 36.6 px | 0.53 | 1.18 | 3 |
| stroke 79 | 13 % → 43 % | 35.5 px | 0.53 | 3.34 | 0 |
| stroke 80 | 7 % → 23 % | 12.3 px | 0.53 | 3.07 | 3 |
| stroke 81 | 20 % → 25 % | 31.1 px | 0.53 | 1.28 | 5 |
| stroke 82 | 16 % → 23 % | 35.2 px | 0.53 | 1.44 | 2 |
| stroke 83 | 15 % → 22 % | 24.2 px | 0.53 | 1.50 | 6 |
| stroke 84 | 21 % → 18 % | 45.8 px | 0.53 | 0.87 | 2 |
| stroke 85 | 11 % → 31 % | 31.3 px | 0.53 | 2.84 | 0 |
| stroke 86 | 18 % → 16 % | 28.1 px | 0.53 | 0.90 | 3 |
| stroke 87 | 10 % → 43 % | 21.2 px | 0.54 | 4.53 | 2 |
| stroke 88 | 19 % → 19 % | 42.6 px | 0.53 | 1.00 | 1 |
| stroke 89 | 11 % → 31 % | 24.0 px | 0.53 | 2.88 | 2 |
| stroke 90 | 9 % → 36 % | 25.0 px | 0.53 | 4.00 | 0 |
| stroke 91 | 23 % → 7 % | 36.5 px | 0.53 | 0.31 | 4 |
| stroke 92 | 14 % → 24 % | 21.5 px | 0.53 | 1.75 | 9 |
| stroke 93 | 13 % → 34 % | 22.3 px | 0.54 | 2.62 | 11 |
| stroke 94 | 18 % → 19 % | 34.6 px | 0.53 | 1.06 | 3 |
| stroke 95 | 18 % → 27 % | 28.8 px | 0.53 | 1.49 | 3 |
| stroke 96 | 14 % → 34 % | 24.7 px | 0.53 | 2.34 | 2 |
| stroke 97 | 28 % → 3 % | 44.3 px | 0.53 | 0.12 | 3 |
| stroke 98 | 20 % → 17 % | 57.9 px | 0.53 | 0.87 | 1 |
| stroke 99 | 16 % → 32 % | 25.3 px | 0.54 | 2.02 | 10 |
| stroke 100 | 22 % → 25 % | 36.5 px | 0.53 | 1.12 | 7 |
| stroke 101 | 21 % → 31 % | 45.5 px | 0.53 | 1.49 | 2 |
| stroke 102 | 24 % → 18 % | 41.5 px | 0.53 | 0.76 | 14 |
| stroke 103 | 18 % → 12 % | 49.0 px | 0.53 | 0.65 | 1 |
| stroke 104 | 7 % → 44 % | 12.5 px | 0.54 | 6.24 | 2 |
| stroke 105 | 23 % → 26 % | 36.9 px | 0.53 | 1.14 | 20 |
| stroke 106 | 23 % → 34 % | 38.1 px | 0.53 | 1.49 | 15 |
| stroke 107 | 31 % → 12 % | 50.6 px | 0.53 | 0.40 | 10 |
| stroke 108 | 17 % → 10 % | 27.8 px | 0.53 | 0.57 | 12 |
| stroke 109 | 7 % → 24 % | 20.8 px | 0.53 | 3.28 | 1 |
| stroke 110 | 4 % → 38 % | 12.5 px | 0.53 | 8.66 | 1 |
| stroke 111 | 16 % → 40 % | 25.6 px | 0.54 | 2.45 | 7 |
| stroke 112 | 16 % → 27 % | 33.9 px | 0.53 | 1.76 | 1 |
| stroke 113 | 19 % → 35 % | 33.8 px | 0.53 | 1.84 | 3 |
| stroke 114 | 21 % → 6 % | 62.5 px | 0.54 | 0.27 | 0 |
| stroke 115 | 21 % → 7 % | 34.0 px | 0.53 | 0.33 | 13 |
| stroke 116 | 11 % → 23 % | 17.9 px | 0.53 | 2.01 | 10 |
| stroke 117 | 14 % → 24 % | 30.9 px | 0.53 | 1.74 | 2 |
| stroke 118 | 22 % → 9 % | 38.9 px | 0.53 | 0.43 | 4 |
| stroke 119 | 13 % → 28 % | 27.1 px | 0.54 | 2.20 | 1 |
| stroke 120 | 16 % → 17 % | 28.2 px | 0.53 | 1.06 | 4 |
| stroke 121 | 14 % → 24 % | 22.0 px | 0.53 | 1.76 | 8 |
| stroke 122 | 9 % → 2 % | 20.6 px | 0.53 | 0.17 | 1 |
| stroke 123 | 14 % → 28 % | 30.7 px | 0.53 | 1.99 | 1 |
| stroke 124 | 18 % → 25 % | 29.5 px | 0.53 | 1.42 | 18 |
| stroke 125 | 7 % → 8 % | 15.3 px | 0.53 | 1.15 | 2 |
| stroke 126 | 18 % → 7 % | 28.3 px | 0.53 | 0.39 | 14 |
| stroke 127 | 14 % → 40 % | 24.8 px | 0.54 | 2.89 | 3 |
| stroke 128 | 20 % → 24 % | 31.8 px | 0.53 | 1.23 | 4 |
| stroke 129 | 28 % → 22 % | 62.9 px | 0.53 | 0.79 | 1 |
| stroke 130 | 6 % → 36 % | 14.0 px | 0.54 | 5.85 | 1 |
| stroke 131 | 11 % → 13 % | 18.1 px | 0.52 | 1.19 | 3 |
| stroke 132 | 18 % → 6 % | 48.6 px | 0.53 | 0.36 | 0 |
| stroke 133 | 13 % → 17 % | 36.9 px | 0.54 | 1.30 | 0 |
| stroke 134 | 18 % → 31 % | 40.1 px | 0.53 | 1.72 | 1 |
| stroke 135 | 26 % → 23 % | 56.8 px | 0.53 | 0.88 | 4 |
| stroke 136 | 21 % → 23 % | 47.9 px | 0.53 | 1.08 | 3 |
| stroke 137 | 11 % → 31 % | 32.2 px | 0.53 | 2.74 | 0 |
| stroke 138 | 17 % → 24 % | 26.0 px | 0.52 | 1.46 | 6 |
| stroke 139 | 14 % → 8 % | 24.8 px | 0.53 | 0.56 | 2 |
| stroke 140 | 16 % → 34 % | 30.9 px | 0.53 | 2.11 | 3 |
| stroke 141 | 17 % → 18 % | 32.5 px | 0.53 | 1.07 | 2 |
| stroke 142 | 11 % → 16 % | 23.9 px | 0.54 | 1.55 | 2 |
| stroke 143 | 16 % → 27 % | 27.2 px | 0.52 | 1.70 | 16 |
| stroke 144 | 22 % → 8 % | 38.6 px | 0.53 | 0.36 | 30 |
| stroke 145 | 17 % → 20 % | 32.0 px | 0.53 | 1.22 | 1 |
| stroke 146 | 15 % → 18 % | 23.5 px | 0.52 | 1.25 | 7 |
| stroke 147 | 18 % → 36 % | 39.0 px | 0.53 | 1.96 | 5 |
| stroke 148 | 22 % → 7 % | 35.2 px | 0.53 | 0.33 | 3 |
| stroke 149 | 8 % → 36 % | 12.7 px | 0.53 | 4.79 | 3 |
| stroke 150 | 14 % → 22 % | 28.7 px | 0.53 | 1.51 | 23 |
| stroke 151 | 21 % → 5 % | 28.4 px | 0.53 | 0.25 | 15 |
| stroke 152 | 16 % → 24 % | 27.6 px | 0.53 | 1.52 | 3 |
| stroke 153 | 19 % → 22 % | 53.7 px | 0.54 | 1.18 | 2 |
| stroke 154 | 26 % → 18 % | 50.5 px | 0.51 | 0.69 | 3 |
| stroke 155 | 20 % → 11 % | 57.3 px | 0.50 | 0.55 | 1 |
| stroke 156 | 35 % → 0 % | 58.6 px | 0.00 | 0.00 | 5 |
| stroke 157 | 18 % → 16 % | 35.6 px | 0.53 | 0.92 | 1 |
| stroke 158 | 20 % → 20 % | 38.2 px | 0.52 | 1.04 | 1 |
| stroke 159 | 17 % → 17 % | 27.2 px | 0.53 | 0.99 | 11 |
| stroke 160 | 9 % → 19 % | 21.2 px | 0.54 | 1.97 | 2 |
| stroke 161 | 16 % → 17 % | 46.0 px | 0.53 | 1.08 | 0 |
| stroke 162 | 8 % → 32 % | 24.3 px | 0.53 | 4.06 | 1 |
| stroke 163 | 16 % → 19 % | 28.2 px | 0.53 | 1.21 | 9 |
| stroke 164 | 23 % → 13 % | 36.1 px | 0.53 | 0.57 | 8 |
| stroke 165 | 10 % → 4 % | 22.4 px | 0.51 | 0.42 | 2 |
| stroke 166 | 26 % → 21 % | 41.0 px | 0.53 | 0.84 | 8 |
| stroke 167 | 12 % → 4 % | 25.7 px | 0.51 | 0.30 | 1 |
| stroke 168 | 32 % → 19 % | 42.2 px | 0.53 | 0.58 | 9 |
| stroke 169 | 15 % → 2 % | 23.2 px | 0.50 | 0.11 | 16 |
| stroke 170 | 37 % → 16 % | 58.5 px | 0.53 | 0.45 | 2 |
| stroke 171 | 16 % → 3 % | 28.4 px | 0.51 | 0.16 | 4 |
| stroke 172 | 7 % → 21 % | 13.2 px | 0.53 | 3.11 | 2 |
| stroke 173 | 13 % → 15 % | 22.0 px | 0.53 | 1.15 | 6 |
| stroke 174 | 20 % → 9 % | 35.2 px | 0.53 | 0.45 | 4 |
| stroke 175 | 19 % → 12 % | 41.3 px | 0.53 | 0.62 | 1 |
| stroke 176 | 7 % → 56 % | 13.3 px | 0.54 | 8.07 | 2 |
| stroke 177 | 7 % → 43 % | 14.5 px | 0.53 | 5.87 | 1 |
| stroke 178 | 8 % → 35 % | 12.3 px | 0.53 | 4.25 | 2 |
| stroke 179 | 6 % → 17 % | 12.3 px | 0.53 | 3.14 | 2 |
| stroke 180 | 13 % → 23 % | 26.2 px | 0.53 | 1.86 | 1 |
| stroke 181 | 9 % → 15 % | 23.8 px | 0.53 | 1.71 | 0 |
| stroke 182 | 9 % → 1 % | 15.3 px | 0.53 | 0.11 | 10 |
| stroke 183 | 12 % → 28 % | 19.7 px | 0.54 | 2.30 | 8 |
| stroke 184 | 9 % → 50 % | 12.7 px | 0.54 | 5.73 | 6 |
| stroke 185 | 10 % → 27 % | 18.4 px | 0.53 | 2.62 | 6 |
| stroke 186 | 11 % → 60 % | 20.2 px | 0.54 | 5.34 | 3 |
| stroke 187 | 11 % → 46 % | 17.6 px | 0.53 | 4.16 | 2 |
| stroke 188 | 12 % → 59 % | 17.3 px | 0.54 | 4.74 | 7 |
| stroke 189 | 5 % → 31 % | 14.0 px | 0.51 | 6.48 | 1 |
| stroke 190 | 11 % → 22 % | 22.4 px | 0.51 | 2.12 | 1 |
| stroke 191 | 12 % → 16 % | 25.0 px | 0.51 | 1.37 | 1 |
| stroke 192 | 16 % → 9 % | 29.3 px | 0.51 | 0.55 | 3 |
| stroke 193 | 16 % → 9 % | 24.3 px | 0.51 | 0.55 | 3 |
| stroke 194 | 10 % → 0 % | 18.4 px | 0.00 | 0.00 | 1 |
| stroke 195 | 24 % → 17 % | 58.5 px | 0.51 | 0.69 | 2 |
| stroke 196 | 21 % → 1 % | 46.5 px | 0.48 | 0.03 | 2 |
| stroke 197 | 12 % → 1 % | 21.3 px | 0.50 | 0.07 | 3 |
| stroke 198 | 17 % → 3 % | 26.7 px | 0.53 | 0.20 | 4 |
| stroke 199 | 25 % → 4 % | 42.9 px | 0.53 | 0.18 | 2 |
| stroke 200 | 25 % → 7 % | 54.3 px | 0.53 | 0.30 | 2 |
| stroke 201 | 21 % → 6 % | 34.2 px | 0.53 | 0.28 | 2 |
| stroke 202 | 19 % → 8 % | 29.2 px | 0.53 | 0.40 | 5 |
| stroke 203 | 11 % → 10 % | 24.1 px | 0.53 | 0.87 | 2 |
| stroke 204 | 14 % → 6 % | 23.3 px | 0.51 | 0.46 | 10 |
| stroke 205 | 8 % → 29 % | 19.2 px | 0.51 | 3.79 | 0 |
| stroke 206 | 5 % → 15 % | 12.6 px | 0.50 | 2.93 | 6 |
| stroke 207 | 10 % → 31 % | 20.5 px | 0.51 | 2.97 | 2 |
| stroke 208 | 15 % → 21 % | 39.3 px | 0.52 | 1.44 | 0 |
| stroke 209 | 14 % → 34 % | 27.4 px | 0.51 | 2.42 | 2 |
| stroke 210 | 10 % → 51 % | 27.6 px | 0.53 | 5.14 | 1 |
| stroke 211 | 8 % → 4 % | 13.2 px | 0.52 | 0.48 | 5 |
| stroke 212 | 10 % → 42 % | 11.6 px | 0.54 | 4.21 | 2 |
| stroke 213 | 15 % → 46 % | 16.6 px | 0.54 | 3.01 | 5 |
| stroke 214 | 17 % → 41 % | 21.1 px | 0.54 | 2.41 | 18 |
| stroke 215 | 19 % → 38 % | 26.5 px | 0.54 | 2.07 | 29 |
| stroke 216 | 21 % → 37 % | 33.4 px | 0.54 | 1.77 | 42 |
| stroke 217 | 26 % → 46 % | 33.7 px | 0.54 | 1.75 | 7 |
| stroke 218 | 26 % → 46 % | 37.2 px | 0.54 | 1.78 | 7 |
| stroke 219 | 25 % → 46 % | 33.2 px | 0.54 | 1.88 | 9 |
| stroke 220 | 24 % → 46 % | 34.6 px | 0.54 | 1.94 | 7 |
| stroke 221 | 26 % → 49 % | 35.7 px | 0.54 | 1.90 | 7 |
| stroke 222 | 19 % → 44 % | 29.1 px | 0.54 | 2.32 | 10 |
| stroke 223 | 8 % → 21 % | 20.3 px | 0.53 | 2.71 | 1 |
| stroke 224 | 27 % → 50 % | 39.2 px | 0.54 | 1.84 | 24 |
| stroke 225 | 17 % → 39 % | 28.7 px | 0.54 | 2.36 | 31 |
| stroke 226 | 28 % → 51 % | 40.4 px | 0.54 | 1.83 | 10 |
| stroke 227 | 24 % → 48 % | 38.4 px | 0.54 | 2.01 | 14 |
| stroke 228 | 18 % → 24 % | 39.1 px | 0.53 | 1.34 | 2 |
| stroke 229 | 30 % → 52 % | 43.5 px | 0.54 | 1.76 | 13 |
| stroke 230 | 26 % → 46 % | 42.3 px | 0.54 | 1.80 | 18 |
| stroke 231 | 17 % → 17 % | 35.6 px | 0.53 | 1.04 | 1 |
| stroke 232 | 30 % → 52 % | 43.9 px | 0.54 | 1.73 | 38 |
| stroke 233 | 25 % → 42 % | 44.9 px | 0.54 | 1.68 | 48 |
| stroke 234 | 31 % → 51 % | 44.6 px | 0.54 | 1.66 | 29 |
| stroke 235 | 28 % → 43 % | 49.3 px | 0.54 | 1.53 | 29 |
| stroke 236 | 23 % → 25 % | 62.7 px | 0.53 | 1.05 | 1 |
| stroke 237 | 31 % → 50 % | 43.8 px | 0.54 | 1.63 | 16 |
| stroke 238 | 28 % → 41 % | 46.5 px | 0.54 | 1.46 | 21 |
| stroke 239 | 27 % → 41 % | 57.0 px | 0.53 | 1.53 | 2 |
| stroke 240 | 30 % → 51 % | 42.9 px | 0.54 | 1.67 | 9 |
| stroke 241 | 14 % → 26 % | 29.7 px | 0.53 | 1.91 | 2 |
| stroke 242 | 33 % → 42 % | 49.3 px | 0.54 | 1.25 | 23 |
| stroke 243 | 20 % → 38 % | 33.3 px | 0.53 | 1.85 | 6 |
| stroke 244 | 29 % → 51 % | 40.5 px | 0.54 | 1.76 | 5 |
| stroke 245 | 15 % → 22 % | 29.8 px | 0.53 | 1.52 | 1 |
| stroke 246 | 31 % → 46 % | 49.4 px | 0.54 | 1.47 | 5 |
| stroke 247 | 14 % → 27 % | 20.3 px | 0.53 | 1.86 | 16 |
| stroke 248 | 26 % → 48 % | 38.7 px | 0.54 | 1.86 | 25 |
| stroke 249 | 24 % → 34 % | 37.4 px | 0.53 | 1.43 | 9 |
| stroke 250 | 18 % → 29 % | 25.5 px | 0.53 | 1.61 | 16 |
| stroke 251 | 27 % → 51 % | 39.4 px | 0.54 | 1.88 | 17 |
| stroke 252 | 21 % → 26 % | 30.2 px | 0.53 | 1.22 | 7 |
| stroke 253 | 25 % → 43 % | 37.5 px | 0.53 | 1.71 | 6 |
| stroke 254 | 28 % → 50 % | 40.8 px | 0.54 | 1.81 | 14 |
| stroke 255 | 11 % → 24 % | 22.0 px | 0.53 | 2.26 | 1 |
| stroke 256 | 6 % → 23 % | 16.2 px | 0.53 | 4.01 | 1 |
| stroke 257 | 21 % → 42 % | 29.8 px | 0.53 | 1.98 | 4 |
| stroke 258 | 23 % → 42 % | 38.0 px | 0.53 | 1.80 | 21 |
| stroke 259 | 7 % → 23 % | 12.6 px | 0.53 | 3.34 | 3 |
| stroke 260 | 12 % → 29 % | 17.9 px | 0.53 | 2.46 | 6 |
| stroke 261 | 22 % → 43 % | 31.2 px | 0.53 | 1.93 | 4 |
| stroke 262 | 28 % → 45 % | 42.6 px | 0.53 | 1.62 | 14 |
| stroke 263 | 12 % → 30 % | 17.0 px | 0.53 | 2.53 | 9 |
| stroke 264 | 15 % → 40 % | 22.2 px | 0.53 | 2.57 | 11 |
| stroke 265 | 26 % → 49 % | 36.6 px | 0.53 | 1.86 | 18 |
| stroke 266 | 33 % → 49 % | 46.2 px | 0.54 | 1.48 | 81 |
| stroke 267 | 24 % → 26 % | 34.0 px | 0.53 | 1.10 | 10 |
| stroke 268 | 20 % → 40 % | 30.0 px | 0.53 | 1.98 | 15 |
| stroke 269 | 21 % → 42 % | 33.7 px | 0.53 | 2.00 | 44 |
| stroke 270 | 31 % → 46 % | 42.6 px | 0.53 | 1.50 | 16 |
| stroke 271 | 25 % → 42 % | 34.9 px | 0.53 | 1.71 | 9 |
| stroke 272 | 24 % → 46 % | 34.4 px | 0.53 | 1.88 | 21 |
| stroke 273 | 17 % → 41 % | 25.4 px | 0.54 | 2.35 | 32 |
| stroke 274 | 28 % → 44 % | 39.7 px | 0.53 | 1.55 | 22 |
| stroke 275 | 25 % → 41 % | 39.1 px | 0.53 | 1.64 | 24 |
| stroke 276 | 22 % → 45 % | 33.5 px | 0.54 | 2.05 | 25 |
| stroke 277 | 23 % → 34 % | 48.0 px | 0.53 | 1.48 | 2 |
| stroke 278 | 21 % → 36 % | 30.3 px | 0.53 | 1.71 | 10 |
| stroke 279 | 27 % → 39 % | 41.5 px | 0.53 | 1.43 | 27 |
| stroke 280 | 25 % → 48 % | 37.0 px | 0.54 | 1.95 | 16 |
| stroke 281 | 17 % → 29 % | 45.4 px | 0.53 | 1.70 | 1 |
| stroke 282 | 20 % → 35 % | 28.7 px | 0.53 | 1.77 | 3 |
| stroke 283 | 29 % → 37 % | 43.2 px | 0.53 | 1.26 | 18 |
| stroke 284 | 30 % → 51 % | 43.5 px | 0.54 | 1.74 | 26 |
| stroke 285 | 14 % → 34 % | 17.6 px | 0.54 | 2.54 | 34 |
| stroke 286 | 14 % → 34 % | 38.0 px | 0.53 | 2.40 | 1 |
| stroke 287 | 26 % → 43 % | 48.1 px | 0.53 | 1.64 | 3 |
| stroke 288 | 14 % → 25 % | 23.1 px | 0.53 | 1.77 | 11 |
| stroke 289 | 24 % → 32 % | 52.0 px | 0.53 | 1.36 | 1 |
| stroke 290 | 28 % → 28 % | 59.6 px | 0.53 | 1.00 | 18 |
| stroke 291 | 30 % → 45 % | 43.8 px | 0.54 | 1.51 | 12 |
| stroke 292 | 18 % → 39 % | 23.0 px | 0.53 | 2.20 | 27 |
| stroke 293 | 22 % → 41 % | 31.3 px | 0.53 | 1.91 | 3 |
| stroke 294 | 14 % → 24 % | 21.7 px | 0.53 | 1.67 | 15 |
| stroke 295 | 19 % → 25 % | 32.1 px | 0.53 | 1.32 | 6 |
| stroke 296 | 31 % → 44 % | 43.5 px | 0.54 | 1.42 | 22 |
| stroke 297 | 24 % → 44 % | 31.6 px | 0.54 | 1.87 | 13 |
| stroke 298 | 22 % → 43 % | 30.9 px | 0.53 | 1.97 | 17 |
| stroke 299 | 16 % → 16 % | 22.9 px | 0.53 | 1.05 | 15 |
| stroke 300 | 14 % → 23 % | 26.2 px | 0.53 | 1.61 | 12 |
| stroke 301 | 29 % → 42 % | 41.2 px | 0.53 | 1.42 | 11 |
| stroke 302 | 27 % → 47 % | 36.5 px | 0.54 | 1.72 | 14 |
| stroke 303 | 22 % → 44 % | 31.0 px | 0.54 | 2.00 | 5 |
| stroke 304 | 14 % → 24 % | 30.2 px | 0.53 | 1.72 | 2 |
| stroke 305 | 25 % → 34 % | 35.7 px | 0.53 | 1.35 | 11 |
| stroke 306 | 12 % → 34 % | 17.9 px | 0.53 | 2.73 | 9 |
| stroke 307 | 29 % → 48 % | 38.3 px | 0.53 | 1.68 | 8 |
| stroke 308 | 21 % → 41 % | 29.5 px | 0.54 | 1.98 | 6 |
| stroke 309 | 12 % → 17 % | 17.3 px | 0.53 | 1.40 | 5 |
| stroke 310 | 14 % → 25 % | 23.5 px | 0.53 | 1.73 | 2 |
| stroke 311 | 27 % → 32 % | 40.3 px | 0.53 | 1.18 | 4 |
| stroke 312 | 17 % → 34 % | 23.7 px | 0.53 | 2.04 | 7 |
| stroke 313 | 30 % → 47 % | 39.1 px | 0.54 | 1.59 | 15 |
| stroke 314 | 27 % → 47 % | 37.9 px | 0.54 | 1.72 | 11 |
| stroke 315 | 19 % → 19 % | 51.9 px | 0.53 | 1.00 | 1 |
| stroke 316 | 15 % → 29 % | 22.1 px | 0.53 | 1.92 | 9 |
| stroke 317 | 21 % → 37 % | 29.1 px | 0.53 | 1.81 | 20 |
| stroke 318 | 28 % → 47 % | 36.4 px | 0.54 | 1.67 | 11 |
| stroke 319 | 29 % → 48 % | 40.5 px | 0.54 | 1.65 | 11 |
| stroke 320 | 20 % → 34 % | 28.7 px | 0.53 | 1.71 | 12 |
| stroke 321 | 10 % → 30 % | 28.1 px | 0.53 | 2.83 | 0 |
| stroke 322 | 28 % → 39 % | 41.8 px | 0.53 | 1.40 | 28 |
| stroke 323 | 28 % → 47 % | 36.2 px | 0.53 | 1.67 | 29 |
| stroke 324 | 26 % → 44 % | 37.2 px | 0.54 | 1.72 | 14 |
| stroke 325 | 4 % → 15 % | 11.7 px | 0.53 | 3.60 | 1 |
| stroke 326 | 22 % → 35 % | 31.3 px | 0.53 | 1.54 | 9 |
| stroke 327 | 17 % → 37 % | 25.1 px | 0.53 | 2.17 | 4 |
| stroke 328 | 25 % → 30 % | 36.9 px | 0.53 | 1.19 | 5 |
| stroke 329 | 27 % → 45 % | 36.1 px | 0.53 | 1.62 | 11 |
| stroke 330 | 26 % → 46 % | 38.4 px | 0.54 | 1.75 | 17 |
| stroke 331 | 10 % → 29 % | 18.0 px | 0.53 | 2.91 | 6 |
| stroke 332 | 6 % → 29 % | 15.0 px | 0.54 | 5.09 | 1 |
| stroke 333 | 18 % → 26 % | 26.2 px | 0.53 | 1.41 | 4 |
| stroke 334 | 26 % → 37 % | 37.1 px | 0.53 | 1.44 | 11 |
| stroke 335 | 28 % → 46 % | 35.3 px | 0.53 | 1.67 | 13 |
| stroke 336 | 23 % → 48 % | 33.3 px | 0.54 | 2.09 | 13 |
| stroke 337 | 17 % → 34 % | 25.4 px | 0.53 | 1.97 | 15 |
| stroke 338 | 26 % → 41 % | 40.3 px | 0.53 | 1.57 | 4 |
| stroke 339 | 28 % → 46 % | 35.1 px | 0.53 | 1.66 | 13 |
| stroke 340 | 19 % → 41 % | 37.4 px | 0.54 | 2.14 | 28 |
| stroke 341 | 23 % → 36 % | 33.0 px | 0.53 | 1.55 | 7 |
| stroke 342 | 28 % → 46 % | 36.7 px | 0.53 | 1.65 | 5 |
| stroke 343 | 23 % → 45 % | 39.6 px | 0.54 | 1.95 | 31 |
| stroke 344 | 25 % → 33 % | 41.5 px | 0.54 | 1.33 | 3 |
| stroke 345 | 22 % → 32 % | 60.9 px | 0.53 | 1.47 | 0 |
| stroke 346 | 19 % → 40 % | 30.7 px | 0.53 | 2.05 | 4 |
| stroke 347 | 27 % → 47 % | 35.9 px | 0.53 | 1.72 | 9 |
| stroke 348 | 30 % → 55 % | 44.0 px | 0.54 | 1.83 | 13 |
| stroke 349 | 29 % → 34 % | 82.1 px | 0.54 | 1.18 | 0 |
| stroke 350 | 23 % → 24 % | 35.7 px | 0.53 | 1.06 | 3 |
| stroke 351 | 7 % → 18 % | 14.5 px | 0.53 | 2.62 | 3 |
| stroke 352 | 15 % → 33 % | 20.8 px | 0.53 | 2.23 | 10 |
| stroke 353 | 27 % → 46 % | 34.9 px | 0.53 | 1.73 | 10 |
| stroke 354 | 31 % → 53 % | 45.3 px | 0.54 | 1.75 | 23 |
| stroke 355 | 20 % → 33 % | 31.0 px | 0.53 | 1.60 | 11 |
| stroke 356 | 13 % → 19 % | 18.9 px | 0.53 | 1.46 | 4 |
| stroke 357 | 27 % → 43 % | 35.7 px | 0.53 | 1.58 | 8 |
| stroke 358 | 28 % → 46 % | 47.4 px | 0.54 | 1.65 | 26 |
| stroke 359 | 29 % → 39 % | 40.7 px | 0.53 | 1.34 | 18 |
| stroke 360 | 17 % → 25 % | 24.9 px | 0.53 | 1.52 | 6 |
| stroke 361 | 27 % → 41 % | 34.7 px | 0.53 | 1.52 | 10 |
| stroke 362 | 33 % → 49 % | 48.2 px | 0.54 | 1.48 | 22 |
| stroke 363 | 17 % → 26 % | 31.9 px | 0.53 | 1.50 | 3 |
| stroke 364 | 14 % → 20 % | 21.8 px | 0.53 | 1.44 | 6 |
| stroke 365 | 16 % → 28 % | 22.8 px | 0.53 | 1.73 | 9 |
| stroke 366 | 22 % → 34 % | 60.4 px | 0.53 | 1.57 | 1 |
| stroke 367 | 25 % → 26 % | 38.7 px | 0.53 | 1.04 | 2 |
| stroke 368 | 17 % → 30 % | 26.6 px | 0.53 | 1.75 | 3 |
| stroke 369 | 22 % → 37 % | 48.5 px | 0.53 | 1.65 | 1 |
| stroke 370 | 26 % → 43 % | 34.0 px | 0.53 | 1.65 | 4 |
| stroke 371 | 36 % → 52 % | 47.1 px | 0.54 | 1.44 | 23 |
| stroke 372 | 20 % → 29 % | 33.5 px | 0.53 | 1.45 | 7 |
| stroke 373 | 20 % → 32 % | 55.5 px | 0.53 | 1.59 | 5 |
| stroke 374 | 21 % → 34 % | 30.2 px | 0.53 | 1.59 | 13 |
| stroke 375 | 22 % → 41 % | 28.1 px | 0.53 | 1.89 | 7 |
| stroke 376 | 33 % → 47 % | 41.9 px | 0.53 | 1.41 | 4 |
| stroke 377 | 29 % → 53 % | 42.1 px | 0.54 | 1.81 | 13 |
| stroke 378 | 13 % → 19 % | 20.4 px | 0.53 | 1.44 | 2 |
| stroke 379 | 20 % → 27 % | 33.6 px | 0.53 | 1.33 | 2 |
| stroke 380 | 16 % → 37 % | 33.0 px | 0.53 | 2.36 | 2 |
| stroke 381 | 23 % → 34 % | 31.9 px | 0.53 | 1.51 | 5 |
| stroke 382 | 23 % → 46 % | 29.3 px | 0.53 | 1.95 | 13 |
| stroke 383 | 26 % → 44 % | 38.9 px | 0.54 | 1.68 | 23 |
| stroke 384 | 19 % → 34 % | 28.0 px | 0.53 | 1.79 | 14 |
| stroke 385 | 27 % → 38 % | 41.4 px | 0.53 | 1.39 | 3 |
| stroke 386 | 16 % → 34 % | 26.0 px | 0.53 | 2.15 | 8 |
| stroke 387 | 25 % → 49 % | 30.6 px | 0.54 | 1.93 | 19 |
| stroke 388 | 25 % → 45 % | 37.2 px | 0.54 | 1.79 | 19 |
| stroke 389 | 21 % → 38 % | 29.1 px | 0.53 | 1.84 | 17 |
| stroke 390 | 24 % → 45 % | 48.3 px | 0.54 | 1.92 | 7 |
| stroke 391 | 25 % → 50 % | 32.6 px | 0.54 | 2.01 | 41 |
| stroke 392 | 22 % → 38 % | 33.7 px | 0.53 | 1.74 | 32 |
| stroke 393 | 10 % → 20 % | 14.2 px | 0.53 | 2.11 | 14 |
| stroke 394 | 17 % → 27 % | 25.2 px | 0.54 | 1.56 | 20 |
| stroke 395 | 23 % → 39 % | 35.4 px | 0.53 | 1.71 | 31 |
| stroke 396 | 30 % → 48 % | 42.8 px | 0.54 | 1.58 | 4 |
| stroke 397 | 17 % → 31 % | 26.8 px | 0.53 | 1.77 | 2 |
| stroke 398 | 8 % → 20 % | 16.4 px | 0.53 | 2.56 | 2 |
| stroke 399 | 30 % → 37 % | 41.8 px | 0.54 | 1.26 | 9 |
| stroke 400 | 25 % → 37 % | 39.3 px | 0.53 | 1.47 | 15 |
| stroke 401 | 31 % → 43 % | 39.3 px | 0.54 | 1.38 | 6 |
| stroke 402 | 15 % → 24 % | 21.8 px | 0.53 | 1.54 | 16 |
| stroke 403 | 25 % → 28 % | 35.6 px | 0.53 | 1.12 | 8 |
| stroke 404 | 26 % → 29 % | 55.5 px | 0.53 | 1.13 | 2 |
| stroke 405 | 29 % → 44 % | 39.7 px | 0.53 | 1.51 | 15 |
| stroke 406 | 30 % → 41 % | 42.0 px | 0.53 | 1.36 | 2 |
| stroke 407 | 22 % → 22 % | 34.0 px | 0.53 | 1.00 | 17 |
| stroke 408 | 22 % → 26 % | 62.5 px | 0.53 | 1.17 | 0 |
| stroke 409 | 20 % → 22 % | 30.5 px | 0.53 | 1.11 | 2 |
| stroke 410 | 31 % → 42 % | 44.4 px | 0.54 | 1.34 | 25 |
| stroke 411 | 26 % → 37 % | 43.9 px | 0.53 | 1.42 | 2 |
| stroke 412 | 29 % → 36 % | 39.0 px | 0.53 | 1.24 | 10 |
| stroke 413 | 30 % → 38 % | 42.1 px | 0.53 | 1.27 | 20 |
| stroke 414 | 18 % → 34 % | 30.8 px | 0.53 | 1.83 | 1 |
| stroke 415 | 25 % → 25 % | 38.3 px | 0.53 | 1.00 | 8 |
| stroke 416 | 11 % → 25 % | 17.7 px | 0.53 | 2.21 | 2 |
| stroke 417 | 27 % → 39 % | 41.2 px | 0.53 | 1.41 | 8 |
| stroke 418 | 20 % → 36 % | 29.9 px | 0.53 | 1.80 | 6 |
| stroke 419 | 14 % → 15 % | 20.0 px | 0.53 | 1.10 | 18 |
| stroke 420 | 23 % → 33 % | 37.9 px | 0.53 | 1.48 | 13 |
| stroke 421 | 22 % → 40 % | 30.2 px | 0.53 | 1.80 | 5 |
| stroke 422 | 17 % → 27 % | 31.2 px | 0.53 | 1.55 | 9 |
| stroke 423 | 20 % → 37 % | 33.9 px | 0.53 | 1.84 | 3 |
| stroke 424 | 25 % → 36 % | 35.3 px | 0.53 | 1.46 | 2 |
| stroke 425 | 13 % → 26 % | 20.1 px | 0.53 | 1.98 | 4 |
| stroke 426 | 27 % → 35 % | 32.3 px | 0.53 | 1.28 | 15 |
| stroke 427 | 14 % → 21 % | 17.6 px | 0.53 | 1.53 | 6 |
| stroke 428 | 28 % → 32 % | 34.1 px | 0.53 | 1.12 | 3 |
| stroke 429 | 23 % → 28 % | 28.9 px | 0.53 | 1.18 | 13 |
| stroke 430 | 27 % → 27 % | 57.0 px | 0.53 | 1.00 | 0 |
| stroke 431 | 29 % → 29 % | 42.3 px | 0.53 | 1.00 | 2 |
| stroke 432 | 5 % → 5 % | 13.5 px | 0.51 | 1.00 | 0 |
| stroke 433 | 7 % → 9 % | 13.5 px | 0.53 | 1.25 | 1 |
| stroke 434 | 7 % → 14 % | 13.7 px | 0.52 | 1.95 | 1 |
| stroke 435 | 14 % → 14 % | 28.2 px | 0.52 | 1.00 | 0 |
| stroke 436 | 8 % → 32 % | 23.2 px | 0.53 | 3.91 | 1 |
| stroke 437 | 9 % → 23 % | 13.1 px | 0.53 | 2.56 | 23 |
| stroke 438 | 13 % → 21 % | 20.2 px | 0.53 | 1.61 | 14 |
| stroke 439 | 26 % → 32 % | 38.3 px | 0.53 | 1.23 | 7 |
| stroke 440 | 14 % → 29 % | 8.3 px | 0.51 | 2.05 | 16 |
| stroke 441 | 24 % → 33 % | 18.1 px | 0.51 | 1.38 | 15 |
| stroke 442 | 26 % → 34 % | 20.8 px | 0.51 | 1.31 | 9 |
| stroke 443 | 22 % → 29 % | 19.8 px | 0.51 | 1.32 | 7 |
| stroke 444 | 17 % → 25 % | 42.3 px | 0.51 | 1.46 | 0 |
| stroke 445 | 6 % → 17 % | 11.0 px | 0.52 | 2.88 | 2 |
| stroke 446 | 19 % → 28 % | 20.0 px | 0.52 | 1.49 | 6 |
| stroke 447 | 11 % → 19 % | 17.0 px | 0.51 | 1.76 | 3 |
| stroke 448 | 19 % → 27 % | 19.3 px | 0.51 | 1.41 | 17 |
| stroke 449 | 6 % → 15 % | 12.0 px | 0.50 | 2.34 | 5 |
| stroke 450 | 14 % → 24 % | 18.7 px | 0.51 | 1.73 | 23 |
| stroke 451 | 18 % → 29 % | 22.4 px | 0.51 | 1.62 | 3 |
| stroke 452 | 17 % → 23 % | 15.8 px | 0.51 | 1.40 | 12 |
| stroke 453 | 20 % → 30 % | 18.7 px | 0.51 | 1.47 | 15 |
| stroke 454 | 12 % → 12 % | 28.6 px | 0.52 | 1.00 | 0 |
| stroke 455 | 21 % → 29 % | 20.3 px | 0.51 | 1.34 | 8 |
| stroke 456 | 20 % → 24 % | 22.3 px | 0.51 | 1.19 | 4 |
| stroke 457 | 12 % → 19 % | 18.3 px | 0.50 | 1.67 | 3 |
| stroke 458 | 12 % → 21 % | 17.5 px | 0.50 | 1.66 | 4 |
| stroke 459 | 13 % → 13 % | 12.3 px | 0.50 | 1.00 | 9 |
| stroke 460 | 8 % → 12 % | 13.7 px | 0.53 | 1.62 | 4 |
| stroke 461 | 12 % → 15 % | 24.8 px | 0.53 | 1.21 | 1 |
| stroke 462 | 9 % → 10 % | 17.6 px | 0.53 | 1.02 | 8 |
| stroke 463 | 7 % → 7 % | 12.7 px | 0.53 | 1.00 | 1 |
| stroke 464 | 8 % → 8 % | 11.9 px | 0.54 | 1.00 | 19 |

Numbers say: wet paint spreads well beyond the stroke.

## Refs v3 · #39 Thick impasto weave — own sheet
own sheet 800 × 1065 · Impasto 1.00 · 96 px · 44.9 s

![Refs v3 · #39 Thick impasto weave — own sheet](Refs-v3-39-Thick-impasto-weave-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 6 % → 1 % | 77.4 px | 0.17 | 0.13 | 113 |
| stroke 2 | 15 % → 0 % | 88.8 px | 0.17 | 0.02 | 616 |
| stroke 3 | 19 % → 1 % | 117.9 px | 0.18 | 0.03 | 751 |
| stroke 4 | 22 % → 1 % | 141.7 px | 0.17 | 0.03 | 986 |
| stroke 5 | 28 % → 1 % | 196.7 px | 0.16 | 0.05 | 885 |
| stroke 6 | 38 % → 1 % | 486.9 px | 0.18 | 0.02 | 507 |
| stroke 7 | 38 % → 1 % | 564.8 px | 0.18 | 0.01 | 396 |
| stroke 8 | 38 % → 1 % | 557.8 px | 0.16 | 0.02 | 247 |
| stroke 9 | 36 % → 1 % | 528.7 px | 0.16 | 0.04 | 302 |
| stroke 10 | 34 % → 1 % | 500.0 px | 0.16 | 0.04 | 320 |
| stroke 11 | 31 % → 1 % | 434.3 px | 0.16 | 0.04 | 342 |
| stroke 12 | 28 % → 1 % | 431.5 px | 0.16 | 0.04 | 285 |
| stroke 13 | 26 % → 1 % | 598.5 px | 0.16 | 0.05 | 134 |
| stroke 14 | 12 % → 1 % | 84.3 px | 0.17 | 0.05 | 798 |
| stroke 15 | 15 % → 1 % | 276.3 px | 0.17 | 0.08 | 95 |
| stroke 16 | 20 % → 1 % | 114.1 px | 0.17 | 0.03 | 909 |
| stroke 17 | 28 % → 1 % | 151.3 px | 0.17 | 0.02 | 997 |
| stroke 18 | 42 % → 1 % | 242.5 px | 0.17 | 0.02 | 634 |
| stroke 19 | 54 % → 1 % | 321.7 px | 0.17 | 0.02 | 388 |
| stroke 20 | 62 % → 1 % | 293.1 px | 0.17 | 0.01 | 681 |
| stroke 21 | 65 % → 1 % | 258.8 px | 0.17 | 0.01 | 1023 |
| stroke 22 | 68 % → 1 % | 235.1 px | 0.17 | 0.01 | 1076 |
| stroke 23 | 10 % → 0 % | 89.2 px | 0.17 | 0.03 | 307 |
| stroke 24 | 14 % → 0 % | 133.4 px | 0.00 | 0.00 | 330 |
| stroke 25 | 19 % → 0 % | 181.3 px | 0.00 | 0.00 | 315 |
| stroke 26 | 23 % → 1 % | 219.3 px | 0.17 | 0.05 | 259 |
| stroke 27 | 28 % → 2 % | 268.7 px | 0.17 | 0.07 | 551 |
| stroke 28 | 34 % → 2 % | 308.3 px | 0.17 | 0.07 | 371 |
| stroke 29 | 37 % → 2 % | 305.2 px | 0.17 | 0.07 | 283 |
| stroke 30 | 41 % → 3 % | 286.0 px | 0.17 | 0.07 | 318 |
| stroke 31 | 48 % → 3 % | 339.9 px | 0.17 | 0.07 | 224 |
| stroke 32 | 10 % → 1 % | 165.9 px | 0.17 | 0.12 | 339 |
| stroke 33 | 6 % → 1 % | 90.6 px | 0.16 | 0.21 | 357 |
| stroke 34 | 2 % → 0 % | 22.0 px | 0.00 | 0.00 | 31 |
| stroke 35 | 4 % → 1 % | 99.4 px | 0.16 | 0.34 | 205 |
| stroke 36 | 8 % → 1 % | 110.5 px | 0.16 | 0.12 | 471 |
| stroke 37 | 13 % → 1 % | 122.2 px | 0.16 | 0.09 | 444 |
| stroke 38 | 18 % → 1 % | 145.1 px | 0.16 | 0.06 | 667 |
| stroke 39 | 23 % → 1 % | 181.7 px | 0.16 | 0.05 | 840 |
| stroke 40 | 28 % → 1 % | 223.3 px | 0.16 | 0.04 | 740 |
| stroke 41 | 35 % → 0 % | 486.8 px | 0.17 | 0.01 | 344 |
| stroke 42 | 53 % → 0 % | 692.2 px | 0.00 | 0.00 | 168 |
| stroke 43 | 35 % → 1 % | 497.1 px | 0.17 | 0.04 | 293 |
| stroke 44 | 33 % → 2 % | 459.9 px | 0.17 | 0.05 | 536 |
| stroke 45 | 32 % → 2 % | 406.7 px | 0.17 | 0.05 | 457 |
| stroke 46 | 33 % → 2 % | 364.4 px | 0.17 | 0.06 | 404 |
| stroke 47 | 35 % → 2 % | 401.0 px | 0.17 | 0.07 | 244 |
| stroke 48 | 38 % → 3 % | 452.1 px | 0.17 | 0.07 | 202 |
| stroke 49 | 44 % → 3 % | 709.9 px | 0.17 | 0.08 | 135 |
| stroke 50 | 9 % → 0 % | 88.9 px | 0.16 | 0.00 | 873 |
| stroke 51 | 15 % → 1 % | 124.4 px | 0.17 | 0.04 | 480 |
| stroke 52 | 24 % → 0 % | 230.0 px | 0.00 | 0.00 | 309 |
| stroke 53 | 2 % → 2 % | 31.5 px | 0.17 | 0.87 | 72 |
| stroke 54 | 4 % → 2 % | 45.7 px | 0.17 | 0.61 | 80 |
| stroke 55 | 4 % → 2 % | 143.9 px | 0.17 | 0.47 | 58 |
| stroke 56 | 6 % → 3 % | 201.0 px | 0.17 | 0.44 | 34 |
| stroke 57 | 5 % → 2 % | 220.6 px | 0.17 | 0.36 | 44 |
| stroke 58 | 5 % → 2 % | 198.2 px | 0.17 | 0.30 | 34 |
| stroke 59 | 5 % → 1 % | 380.8 px | 0.18 | 0.25 | 12 |
| stroke 60 | 2 % → 0 % | 34.8 px | 0.00 | 0.00 | 57 |
| stroke 61 | 7 % → 1 % | 38.9 px | 0.17 | 0.08 | 289 |
| stroke 62 | 8 % → 1 % | 50.8 px | 0.17 | 0.06 | 270 |
| stroke 63 | 10 % → 1 % | 61.5 px | 0.17 | 0.05 | 147 |
| stroke 64 | 13 % → 0 % | 197.0 px | 0.00 | 0.00 | 39 |
| stroke 65 | 9 % → 1 % | 475.2 px | 0.17 | 0.06 | 15 |
| stroke 66 | 9 % → 0 % | 288.2 px | 0.17 | 0.05 | 33 |
| stroke 67 | 9 % → 0 % | 240.5 px | 0.17 | 0.05 | 48 |
| stroke 68 | 8 % → 0 % | 635.6 px | 0.00 | 0.00 | 6 |
| stroke 69 | 10 % → 1 % | 129.6 px | 0.16 | 0.10 | 58 |
| stroke 70 | 10 % → 0 % | 366.9 px | 0.17 | 0.05 | 27 |
| stroke 71 | 10 % → 1 % | 155.3 px | 0.15 | 0.06 | 47 |
| stroke 72 | 11 % → 0 % | 589.5 px | 0.00 | 0.00 | 14 |
| stroke 73 | 11 % → 0 % | 179.1 px | 0.00 | 0.00 | 35 |
| stroke 74 | 11 % → 0 % | 272.3 px | 0.00 | 0.00 | 45 |
| stroke 75 | 8 % → 1 % | 432.5 px | 0.16 | 0.15 | 11 |
| stroke 76 | 8 % → 1 % | 332.4 px | 0.16 | 0.15 | 29 |
| stroke 77 | 1 % → 0 % | 29.8 px | 0.16 | 0.10 | 23 |
| stroke 78 | 3 % → 1 % | 32.8 px | 0.16 | 0.34 | 95 |
| stroke 79 | 4 % → 1 % | 62.6 px | 0.16 | 0.28 | 84 |
| stroke 80 | 8 % → 0 % | 112.0 px | 0.00 | 0.00 | 43 |
| stroke 81 | 6 % → 1 % | 197.3 px | 0.17 | 0.10 | 30 |
| stroke 82 | 10 % → 0 % | 326.4 px | 0.00 | 0.00 | 12 |
| stroke 83 | 6 % → 1 % | 227.4 px | 0.15 | 0.16 | 10 |
| stroke 84 | 6 % → 1 % | 153.2 px | 0.16 | 0.23 | 26 |
| stroke 85 | 6 % → 1 % | 165.5 px | 0.16 | 0.23 | 49 |
| stroke 86 | 6 % → 2 % | 488.0 px | 0.16 | 0.27 | 22 |
| stroke 87 | 11 % → 0 % | 471.9 px | 0.00 | 0.00 | 9 |
| stroke 88 | 11 % → 0 % | 293.0 px | 0.00 | 0.00 | 31 |
| stroke 89 | 6 % → 2 % | 212.1 px | 0.16 | 0.25 | 15 |
| stroke 90 | 6 % → 2 % | 253.1 px | 0.16 | 0.26 | 16 |
| stroke 91 | 10 % → 0 % | 727.7 px | 0.00 | 0.00 | 6 |
| stroke 92 | 8 % → 1 % | 112.8 px | 0.16 | 0.16 | 65 |
| stroke 93 | 14 % → 0 % | 141.6 px | 0.16 | 0.01 | 59 |
| stroke 94 | 10 % → 1 % | 165.7 px | 0.16 | 0.13 | 54 |
| stroke 95 | 18 % → 0 % | 280.0 px | 0.00 | 0.00 | 33 |
| stroke 96 | 14 % → 1 % | 281.2 px | 0.17 | 0.05 | 41 |
| stroke 97 | 11 % → 1 % | 258.0 px | 0.16 | 0.13 | 42 |
| stroke 98 | 6 % → 1 % | 354.7 px | 0.17 | 0.24 | 12 |
| stroke 99 | 8 % → 2 % | 288.1 px | 0.16 | 0.21 | 16 |
| stroke 100 | 10 % → 2 % | 299.6 px | 0.16 | 0.15 | 29 |
| stroke 101 | 11 % → 1 % | 268.3 px | 0.16 | 0.13 | 57 |
| stroke 102 | 4 % → 1 % | 101.3 px | 0.17 | 0.33 | 46 |
| stroke 103 | 5 % → 1 % | 401.8 px | 0.17 | 0.22 | 7 |
| stroke 104 | 2 % → 4 % | 23.9 px | 0.17 | 1.91 | 53 |
| stroke 105 | 5 % → 5 % | 67.3 px | 0.17 | 0.92 | 32 |
| stroke 106 | 1 % → 1 % | 56.0 px | 0.18 | 0.94 | 24 |
| stroke 107 | 1 % → 1 % | 21.7 px | 0.16 | 0.92 | 43 |
| stroke 108 | 1 % → 1 % | 22.1 px | 0.17 | 0.94 | 27 |

Numbers say: wet paint spreads well beyond the stroke.

## Refs v3 · #40 Watercolour blooms — own sheet
own sheet 800 × 1170 · Watercolour 1.00 + water 55 % · 112 px · 58.5 s

![Refs v3 · #40 Watercolour blooms — own sheet](Refs-v3-40-Watercolour-blooms-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 10 % → 29 % | 114.6 px | 0.36 | 2.95 | 208 |
| stroke 2 | 13 % → 31 % | 196.4 px | 0.37 | 2.36 | 142 |
| stroke 3 | 15 % → 31 % | 318.0 px | 0.37 | 2.05 | 156 |
| stroke 4 | 16 % → 29 % | 430.6 px | 0.37 | 1.81 | 190 |
| stroke 5 | 20 % → 33 % | 239.3 px | 0.38 | 1.70 | 507 |
| stroke 6 | 22 % → 35 % | 263.0 px | 0.38 | 1.57 | 664 |
| stroke 7 | 26 % → 37 % | 259.1 px | 0.38 | 1.43 | 826 |
| stroke 8 | 30 % → 35 % | 269.8 px | 0.38 | 1.20 | 1024 |
| stroke 9 | 34 % → 32 % | 276.1 px | 0.38 | 0.95 | 1251 |
| stroke 10 | 37 % → 28 % | 308.5 px | 0.38 | 0.75 | 895 |
| stroke 11 | 39 % → 23 % | 331.3 px | 0.37 | 0.58 | 949 |
| stroke 12 | 41 % → 17 % | 336.3 px | 0.37 | 0.42 | 717 |
| stroke 13 | 49 % → 6 % | 506.6 px | 0.35 | 0.13 | 557 |
| stroke 14 | 30 % → 14 % | 914.6 px | 0.36 | 0.48 | 155 |
| stroke 15 | 51 % → 4 % | 655.6 px | 0.34 | 0.08 | 358 |
| stroke 16 | 26 % → 2 % | 450.8 px | 0.20 | 0.06 | 428 |
| stroke 17 | 24 % → 0 % | 317.3 px | 0.00 | 0.00 | 623 |
| stroke 18 | 23 % → 0 % | 330.7 px | 0.00 | 0.00 | 923 |
| stroke 19 | 1 % → 0 % | 29.5 px | 0.00 | 0.00 | 9 |
| stroke 20 | 3 % → 0 % | 47.9 px | 0.00 | 0.00 | 40 |
| stroke 21 | 2 % → 26 % | 95.4 px | 0.38 | 10.47 | 38 |
| stroke 22 | 7 % → 25 % | 111.7 px | 0.38 | 3.39 | 121 |
| stroke 23 | 8 % → 24 % | 363.5 px | 0.37 | 3.17 | 31 |
| stroke 24 | 12 % → 21 % | 200.0 px | 0.37 | 1.81 | 127 |
| stroke 25 | 15 % → 18 % | 270.6 px | 0.36 | 1.20 | 104 |
| stroke 26 | 16 % → 17 % | 307.0 px | 0.37 | 1.02 | 91 |
| stroke 27 | 13 % → 30 % | 233.0 px | 0.38 | 2.37 | 188 |
| stroke 28 | 24 % → 17 % | 924.1 px | 0.39 | 0.69 | 51 |
| stroke 29 | 4 % → 53 % | 73.8 px | 0.37 | 12.95 | 24 |
| stroke 30 | 12 % → 44 % | 100.2 px | 0.36 | 3.68 | 180 |
| stroke 31 | 20 % → 33 % | 132.7 px | 0.36 | 1.69 | 230 |
| stroke 32 | 38 % → 36 % | 709.0 px | 0.37 | 0.93 | 56 |
| stroke 33 | 38 % → 34 % | 976.5 px | 0.37 | 0.89 | 54 |
| stroke 34 | 9 % → 23 % | 148.0 px | 0.37 | 2.63 | 65 |
| stroke 35 | 38 % → 31 % | 1356.3 px | 0.36 | 0.82 | 25 |
| stroke 36 | 16 % → 21 % | 230.0 px | 0.37 | 1.34 | 165 |
| stroke 37 | 35 % → 21 % | 378.4 px | 0.35 | 0.59 | 271 |
| stroke 38 | 2 % → 2 % | 78.9 px | 0.21 | 0.77 | 58 |
| stroke 39 | 4 % → 5 % | 93.6 px | 0.32 | 1.17 | 120 |
| stroke 40 | 7 % → 24 % | 398.2 px | 0.37 | 3.65 | 34 |
| stroke 41 | 8 % → 10 % | 124.8 px | 0.36 | 1.21 | 157 |
| stroke 42 | 12 % → 17 % | 238.9 px | 0.37 | 1.39 | 145 |
| stroke 43 | 16 % → 23 % | 645.3 px | 0.37 | 1.43 | 83 |
| stroke 44 | 4 % → 0 % | 78.0 px | 0.00 | 0.00 | 110 |
| stroke 45 | 7 % → 0 % | 91.0 px | 0.00 | 0.00 | 133 |
| stroke 46 | 10 % → 0 % | 115.4 px | 0.00 | 0.00 | 179 |
| stroke 47 | 13 % → 0 % | 151.3 px | 0.10 | 0.00 | 206 |
| stroke 48 | 15 % → 1 % | 158.9 px | 0.19 | 0.05 | 211 |
| stroke 49 | 25 % → 0 % | 666.6 px | 0.00 | 0.00 | 65 |
| stroke 50 | 20 % → 0 % | 426.1 px | 0.20 | 0.02 | 109 |
| stroke 51 | 23 % → 1 % | 447.2 px | 0.31 | 0.06 | 117 |
| stroke 52 | 26 % → 3 % | 456.8 px | 0.34 | 0.11 | 129 |
| stroke 53 | 28 % → 4 % | 518.8 px | 0.36 | 0.15 | 195 |
| stroke 54 | 2 % → 9 % | 25.9 px | 0.36 | 4.11 | 40 |
| stroke 55 | 1 % → 30 % | 50.2 px | 0.38 | 53.30 | 10 |
| stroke 56 | 11 % → 15 % | 116.1 px | 0.38 | 1.42 | 337 |
| stroke 57 | 19 % → 20 % | 135.0 px | 0.38 | 1.06 | 1167 |
| stroke 58 | 26 % → 23 % | 172.3 px | 0.38 | 0.87 | 1000 |
| stroke 59 | 32 % → 26 % | 232.9 px | 0.38 | 0.80 | 1094 |
| stroke 60 | 20 % → 38 % | 370.4 px | 0.37 | 1.93 | 361 |
| stroke 61 | 34 % → 33 % | 786.2 px | 0.37 | 0.98 | 215 |
| stroke 62 | 14 % → 12 % | 256.7 px | 0.35 | 0.86 | 181 |
| stroke 63 | 7 % → 29 % | 103.8 px | 0.38 | 4.11 | 316 |
| stroke 64 | 12 % → 31 % | 149.5 px | 0.39 | 2.59 | 362 |
| stroke 65 | 18 % → 30 % | 160.0 px | 0.39 | 1.67 | 392 |
| stroke 66 | 24 % → 29 % | 196.2 px | 0.38 | 1.21 | 483 |
| stroke 67 | 33 % → 31 % | 241.2 px | 0.39 | 0.92 | 696 |
| stroke 68 | 51 % → 32 % | 1129.5 px | 0.37 | 0.63 | 72 |
| stroke 69 | 41 % → 32 % | 459.0 px | 0.38 | 0.80 | 164 |
| stroke 70 | 6 % → 25 % | 155.6 px | 0.39 | 3.97 | 126 |
| stroke 71 | 24 % → 16 % | 509.0 px | 0.37 | 0.66 | 432 |
| stroke 72 | 1 % → 15 % | 24.9 px | 0.36 | 13.05 | 14 |
| stroke 73 | 10 % → 31 % | 88.7 px | 0.36 | 3.14 | 161 |
| stroke 74 | 15 % → 32 % | 265.6 px | 0.36 | 2.10 | 83 |
| stroke 75 | 16 % → 23 % | 130.0 px | 0.36 | 1.39 | 282 |
| stroke 76 | 19 % → 22 % | 198.4 px | 0.36 | 1.14 | 367 |
| stroke 77 | 4 % → 30 % | 91.2 px | 0.38 | 7.09 | 259 |
| stroke 78 | 7 % → 22 % | 102.7 px | 0.37 | 2.93 | 399 |
| stroke 79 | 14 % → 33 % | 574.6 px | 0.38 | 2.27 | 58 |
| stroke 80 | 13 % → 28 % | 233.0 px | 0.37 | 2.10 | 290 |
| stroke 81 | 19 % → 36 % | 707.4 px | 0.38 | 1.86 | 59 |
| stroke 82 | 18 % → 30 % | 358.7 px | 0.37 | 1.72 | 177 |
| stroke 83 | 24 % → 38 % | 713.3 px | 0.39 | 1.56 | 80 |
| stroke 84 | 20 % → 25 % | 266.8 px | 0.37 | 1.24 | 305 |
| stroke 85 | 30 % → 33 % | 398.4 px | 0.37 | 1.11 | 283 |

Numbers say: wet paint spreads well beyond the stroke.

## Refs v3 · #41 Coloured pencil — own sheet
own sheet 800 × 1108 · Charcoal 0.50 · Pastel 0.50 · 12 px · 42.0 s

![Refs v3 · #41 Coloured pencil — own sheet](Refs-v3-41-Coloured-pencil-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 6 % → 0 % | 15.3 px | 0.00 | 0.00 | 14 |
| stroke 2 | 11 % → 2 % | 20.7 px | 0.17 | 0.21 | 3 |
| stroke 3 | 13 % → 4 % | 20.4 px | 0.18 | 0.34 | 11 |
| stroke 4 | 18 % → 2 % | 28.7 px | 0.17 | 0.13 | 10 |
| stroke 5 | 8 % → 0 % | 12.8 px | 0.00 | 0.00 | 4 |
| stroke 6 | 18 % → 1 % | 31.1 px | 0.17 | 0.03 | 13 |
| stroke 7 | 10 % → 0 % | 23.9 px | 0.00 | 0.00 | 46 |
| stroke 8 | 13 % → 0 % | 30.1 px | 0.00 | 0.00 | 28 |
| stroke 9 | 19 % → 0 % | 40.4 px | 0.00 | 0.00 | 41 |
| stroke 10 | 24 % → 0 % | 48.5 px | 0.00 | 0.00 | 30 |
| stroke 11 | 29 % → 0 % | 56.3 px | 0.00 | 0.00 | 25 |
| stroke 12 | 34 % → 0 % | 62.3 px | 0.00 | 0.00 | 25 |
| stroke 13 | 37 % → 0 % | 66.3 px | 0.00 | 0.00 | 28 |
| stroke 14 | 39 % → 0 % | 64.8 px | 0.00 | 0.00 | 38 |
| stroke 15 | 36 % → 0 % | 57.0 px | 0.00 | 0.00 | 8 |
| stroke 16 | 10 % → 0 % | 12.7 px | 0.00 | 0.00 | 47 |
| stroke 17 | 15 % → 0 % | 19.6 px | 0.16 | 0.00 | 34 |
| stroke 18 | 19 % → 0 % | 26.5 px | 0.00 | 0.00 | 21 |
| stroke 19 | 24 % → 0 % | 34.0 px | 0.00 | 0.00 | 44 |
| stroke 20 | 29 % → 0 % | 42.8 px | 0.00 | 0.00 | 38 |
| stroke 21 | 36 % → 0 % | 50.4 px | 0.00 | 0.00 | 25 |
| stroke 22 | 37 % → 0 % | 50.8 px | 0.00 | 0.00 | 49 |
| stroke 23 | 37 % → 0 % | 51.7 px | 0.00 | 0.00 | 38 |
| stroke 24 | 37 % → 0 % | 47.1 px | 0.00 | 0.00 | 21 |
| stroke 25 | 30 % → 0 % | 62.4 px | 0.00 | 0.00 | 1 |
| stroke 26 | 36 % → 0 % | 44.5 px | 0.00 | 0.00 | 19 |
| stroke 27 | 34 % → 0 % | 43.2 px | 0.00 | 0.00 | 12 |
| stroke 28 | 35 % → 0 % | 45.0 px | 0.00 | 0.00 | 7 |
| stroke 29 | 33 % → 0 % | 43.7 px | 0.00 | 0.00 | 6 |
| stroke 30 | 7 % → 0 % | 11.6 px | 0.00 | 0.00 | 5 |
| stroke 31 | 13 % → 0 % | 18.3 px | 0.00 | 0.00 | 5 |
| stroke 32 | 20 % → 0 % | 28.8 px | 0.00 | 0.00 | 8 |
| stroke 33 | 22 % → 0 % | 33.7 px | 0.00 | 0.00 | 13 |
| stroke 34 | 28 % → 0 % | 42.5 px | 0.00 | 0.00 | 15 |
| stroke 35 | 32 % → 0 % | 47.7 px | 0.00 | 0.00 | 19 |
| stroke 36 | 31 % → 0 % | 46.2 px | 0.00 | 0.00 | 17 |
| stroke 37 | 31 % → 0 % | 45.9 px | 0.00 | 0.00 | 13 |
| stroke 38 | 29 % → 0 % | 44.2 px | 0.00 | 0.00 | 5 |
| stroke 39 | 11 % → 0 % | 27.8 px | 0.00 | 0.00 | 1 |
| stroke 40 | 27 % → 0 % | 40.5 px | 0.00 | 0.00 | 6 |
| stroke 41 | 10 % → 0 % | 26.1 px | 0.00 | 0.00 | 1 |
| stroke 42 | 17 % → 2 % | 25.9 px | 0.18 | 0.12 | 15 |
| stroke 43 | 22 % → 3 % | 32.9 px | 0.18 | 0.12 | 18 |
| stroke 44 | 11 % → 0 % | 18.1 px | 0.00 | 0.00 | 2 |
| stroke 45 | 19 % → 4 % | 32.4 px | 0.18 | 0.21 | 131 |
| stroke 46 | 24 % → 6 % | 39.3 px | 0.18 | 0.25 | 40 |
| stroke 47 | 30 % → 11 % | 46.5 px | 0.18 | 0.36 | 31 |
| stroke 48 | 31 % → 18 % | 46.7 px | 0.18 | 0.57 | 13 |
| stroke 49 | 7 % → 0 % | 14.2 px | 0.00 | 0.00 | 3 |
| stroke 50 | 8 % → 8 % | 12.8 px | 0.17 | 0.89 | 5 |
| stroke 51 | 14 % → 0 % | 27.5 px | 0.00 | 0.00 | 8 |
| stroke 52 | 12 % → 7 % | 18.3 px | 0.17 | 0.63 | 32 |
| stroke 53 | 13 % → 0 % | 28.6 px | 0.00 | 0.00 | 1 |
| stroke 54 | 18 % → 6 % | 28.4 px | 0.17 | 0.34 | 12 |
| stroke 55 | 15 % → 6 % | 31.5 px | 0.17 | 0.40 | 20 |
| stroke 56 | 21 % → 6 % | 44.9 px | 0.18 | 0.28 | 23 |
| stroke 57 | 26 % → 5 % | 55.8 px | 0.18 | 0.20 | 23 |
| stroke 58 | 33 % → 4 % | 70.3 px | 0.17 | 0.12 | 27 |
| stroke 59 | 39 % → 0 % | 60.8 px | 0.00 | 0.00 | 13 |
| stroke 60 | 30 % → 1 % | 51.2 px | 0.17 | 0.03 | 2 |
| stroke 61 | 41 % → 0 % | 62.7 px | 0.00 | 0.00 | 11 |
| stroke 62 | 44 % → 0 % | 65.3 px | 0.00 | 0.00 | 9 |
| stroke 63 | 47 % → 0 % | 72.6 px | 0.00 | 0.00 | 7 |
| stroke 64 | 12 % → 0 % | 18.1 px | 0.00 | 0.00 | 6 |
| stroke 65 | 8 % → 0 % | 12.8 px | 0.00 | 0.00 | 3 |
| stroke 66 | 5 % → 2 % | 13.9 px | 0.18 | 0.33 | 1 |
| stroke 67 | 9 % → 0 % | 21.1 px | 0.00 | 0.00 | 2 |
| stroke 68 | 9 % → 9 % | 15.3 px | 0.18 | 0.97 | 22 |
| stroke 69 | 7 % → 0 % | 11.8 px | 0.00 | 0.00 | 8 |
| stroke 70 | 13 % → 6 % | 23.3 px | 0.18 | 0.49 | 22 |
| stroke 71 | 24 % → 9 % | 38.7 px | 0.18 | 0.37 | 19 |
| stroke 72 | 34 % → 16 % | 54.4 px | 0.18 | 0.47 | 5 |
| stroke 73 | 9 % → 17 % | 9.1 px | 0.18 | 2.00 | 33 |
| stroke 74 | 16 % → 7 % | 20.2 px | 0.17 | 0.41 | 6 |
| stroke 75 | 17 % → 0 % | 32.6 px | 0.17 | 0.02 | 1 |
| stroke 76 | 13 % → 0 % | 25.0 px | 0.00 | 0.00 | 1 |
| stroke 77 | 21 % → 0 % | 41.7 px | 0.00 | 0.00 | 2 |
| stroke 78 | 16 % → 0 % | 18.3 px | 0.00 | 0.00 | 7 |
| stroke 79 | 24 % → 0 % | 38.9 px | 0.00 | 0.00 | 10 |
| stroke 80 | 5 % → 0 % | 11.9 px | 0.00 | 0.00 | 0 |
| stroke 81 | 9 % → 0 % | 18.4 px | 0.00 | 0.00 | 1 |
| stroke 82 | 12 % → 0 % | 15.1 px | 0.00 | 0.00 | 4 |
| stroke 83 | 16 % → 0 % | 15.4 px | 0.00 | 0.00 | 14 |
| stroke 84 | 22 % → 0 % | 23.4 px | 0.00 | 0.00 | 8 |
| stroke 85 | 18 % → 0 % | 28.2 px | 0.00 | 0.00 | 1 |
| stroke 86 | 13 % → 0 % | 15.7 px | 0.00 | 0.00 | 3 |
| stroke 87 | 9 % → 0 % | 15.1 px | 0.00 | 0.00 | 5 |
| stroke 88 | 6 % → 0 % | 12.3 px | 0.00 | 0.00 | 2 |
| stroke 89 | 17 % → 0 % | 29.4 px | 0.00 | 0.00 | 4 |
| stroke 90 | 8 % → 0 % | 16.1 px | 0.00 | 0.00 | 3 |
| stroke 91 | 11 % → 0 % | 18.2 px | 0.00 | 0.00 | 2 |
| stroke 92 | 22 % → 0 % | 34.9 px | 0.00 | 0.00 | 5 |
| stroke 93 | 16 % → 0 % | 25.7 px | 0.00 | 0.00 | 6 |
| stroke 94 | 15 % → 0 % | 27.5 px | 0.00 | 0.00 | 13 |
| stroke 95 | 20 % → 0 % | 33.0 px | 0.00 | 0.00 | 10 |
| stroke 96 | 8 % → 0 % | 12.8 px | 0.00 | 0.00 | 1 |
| stroke 97 | 14 % → 0 % | 17.8 px | 0.00 | 0.00 | 6 |
| stroke 98 | 6 % → 0 % | 13.5 px | 0.00 | 0.00 | 1 |
| stroke 99 | 16 % → 0 % | 29.9 px | 0.00 | 0.00 | 4 |
| stroke 100 | 6 % → 0 % | 9.9 px | 0.00 | 0.00 | 1 |
| stroke 101 | 8 % → 0 % | 12.7 px | 0.00 | 0.00 | 3 |
| stroke 102 | 15 % → 0 % | 21.4 px | 0.00 | 0.00 | 4 |
| stroke 103 | 17 % → 0 % | 43.7 px | 0.00 | 0.00 | 5 |
| stroke 104 | 13 % → 0 % | 34.4 px | 0.00 | 0.00 | 1 |
| stroke 105 | 8 % → 0 % | 10.6 px | 0.00 | 0.00 | 2 |
| stroke 106 | 15 % → 0 % | 20.8 px | 0.00 | 0.00 | 2 |
| stroke 107 | 16 % → 0 % | 19.9 px | 0.00 | 0.00 | 5 |
| stroke 108 | 16 % → 0 % | 15.4 px | 0.00 | 0.00 | 9 |
| stroke 109 | 22 % → 0 % | 21.3 px | 0.00 | 0.00 | 18 |
| stroke 110 | 23 % → 0 % | 24.3 px | 0.00 | 0.00 | 3 |
| stroke 111 | 6 % → 0 % | 13.8 px | 0.00 | 0.00 | 2 |
| stroke 112 | 12 % → 0 % | 30.3 px | 0.00 | 0.00 | 0 |
| stroke 113 | 15 % → 0 % | 22.3 px | 0.00 | 0.00 | 6 |
| stroke 114 | 19 % → 0 % | 33.4 px | 0.00 | 0.00 | 1 |
| stroke 115 | 11 % → 0 % | 16.4 px | 0.00 | 0.00 | 6 |
| stroke 116 | 16 % → 0 % | 24.4 px | 0.00 | 0.00 | 16 |
| stroke 117 | 23 % → 0 % | 37.2 px | 0.00 | 0.00 | 9 |
| stroke 118 | 25 % → 0 % | 38.7 px | 0.00 | 0.00 | 9 |
| stroke 119 | 5 % → 0 % | 14.6 px | 0.00 | 0.00 | 1 |
| stroke 120 | 23 % → 0 % | 35.2 px | 0.00 | 0.00 | 6 |
| stroke 121 | 13 % → 0 % | 20.2 px | 0.00 | 0.00 | 1 |
| stroke 122 | 20 % → 0 % | 30.4 px | 0.00 | 0.00 | 7 |
| stroke 123 | 22 % → 0 % | 33.3 px | 0.00 | 0.00 | 3 |
| stroke 124 | 14 % → 0 % | 22.1 px | 0.00 | 0.00 | 21 |
| stroke 125 | 21 % → 0 % | 32.0 px | 0.00 | 0.00 | 17 |
| stroke 126 | 32 % → 0 % | 42.4 px | 0.00 | 0.00 | 19 |
| stroke 127 | 36 % → 0 % | 53.9 px | 0.00 | 0.00 | 6 |
| stroke 128 | 39 % → 0 % | 49.7 px | 0.00 | 0.00 | 6 |
| stroke 129 | 7 % → 0 % | 15.5 px | 0.00 | 0.00 | 0 |
| stroke 130 | 6 % → 0 % | 14.2 px | 0.00 | 0.00 | 1 |
| stroke 131 | 8 % → 0 % | 12.7 px | 0.00 | 0.00 | 3 |
| stroke 132 | 8 % → 0 % | 15.9 px | 0.00 | 0.00 | 3 |
| stroke 133 | 13 % → 0 % | 11.6 px | 0.00 | 0.00 | 6 |
| stroke 134 | 23 % → 0 % | 31.1 px | 0.00 | 0.00 | 3 |
| stroke 135 | 20 % → 0 % | 27.9 px | 0.00 | 0.00 | 2 |
| stroke 136 | 19 % → 0 % | 28.4 px | 0.00 | 0.00 | 1 |
| stroke 137 | 23 % → 0 % | 43.1 px | 0.00 | 0.00 | 2 |
| stroke 138 | 5 % → 0 % | 15.0 px | 0.00 | 0.00 | 0 |
| stroke 139 | 14 % → 1 % | 11.8 px | 0.17 | 0.10 | 11 |
| stroke 140 | 33 % → 0 % | 50.6 px | 0.00 | 0.00 | 1 |
| stroke 141 | 8 % → 2 % | 11.8 px | 0.18 | 0.24 | 6 |
| stroke 142 | 6 % → 0 % | 13.6 px | 0.00 | 0.00 | 1 |
| stroke 143 | 12 % → 1 % | 22.6 px | 0.17 | 0.06 | 4 |
| stroke 144 | 17 % → 8 % | 28.8 px | 0.18 | 0.45 | 3 |
| stroke 145 | 21 % → 13 % | 39.3 px | 0.18 | 0.63 | 9 |
| stroke 146 | 21 % → 13 % | 55.1 px | 0.18 | 0.61 | 1 |
| stroke 147 | 6 % → 7 % | 15.3 px | 0.17 | 1.13 | 2 |
| stroke 148 | 13 % → 2 % | 20.7 px | 0.17 | 0.13 | 4 |
| stroke 149 | 7 % → 22 % | 12.4 px | 0.17 | 2.91 | 14 |
| stroke 150 | 8 % → 0 % | 14.5 px | 0.00 | 0.00 | 0 |
| stroke 151 | 10 % → 32 % | 16.4 px | 0.17 | 3.15 | 3 |
| stroke 152 | 8 % → 0 % | 15.5 px | 0.00 | 0.00 | 2 |
| stroke 153 | 20 % → 0 % | 30.3 px | 0.00 | 0.00 | 1 |
| stroke 154 | 12 % → 0 % | 12.8 px | 0.00 | 0.00 | 2 |
| stroke 155 | 6 % → 0 % | 14.0 px | 0.00 | 0.00 | 2 |
| stroke 156 | 5 % → 0 % | 12.3 px | 0.00 | 0.00 | 3 |
| stroke 157 | 8 % → 0 % | 11.5 px | 0.00 | 0.00 | 8 |
| stroke 158 | 6 % → 0 % | 11.4 px | 0.00 | 0.00 | 7 |
| stroke 159 | 11 % → 0 % | 16.8 px | 0.00 | 0.00 | 25 |
| stroke 160 | 15 % → 0 % | 25.3 px | 0.00 | 0.00 | 29 |
| stroke 161 | 11 % → 0 % | 23.2 px | 0.00 | 0.00 | 2 |
| stroke 162 | 9 % → 0 % | 13.5 px | 0.00 | 0.00 | 12 |
| stroke 163 | 24 % → 0 % | 34.3 px | 0.00 | 0.00 | 21 |
| stroke 164 | 10 % → 0 % | 17.5 px | 0.00 | 0.00 | 27 |
| stroke 165 | 23 % → 0 % | 33.9 px | 0.00 | 0.00 | 30 |
| stroke 166 | 24 % → 0 % | 39.6 px | 0.00 | 0.00 | 2 |
| stroke 167 | 26 % → 0 % | 41.2 px | 0.00 | 0.00 | 2 |
| stroke 168 | 25 % → 0 % | 34.9 px | 0.00 | 0.00 | 11 |
| stroke 169 | 23 % → 0 % | 32.8 px | 0.00 | 0.00 | 13 |
| stroke 170 | 28 % → 0 % | 39.3 px | 0.00 | 0.00 | 17 |
| stroke 171 | 22 % → 0 % | 49.0 px | 0.00 | 0.00 | 1 |
| stroke 172 | 26 % → 0 % | 36.3 px | 0.00 | 0.00 | 7 |
| stroke 173 | 11 % → 0 % | 16.4 px | 0.00 | 0.00 | 2 |
| stroke 174 | 27 % → 0 % | 42.7 px | 0.00 | 0.00 | 2 |
| stroke 175 | 29 % → 0 % | 40.0 px | 0.00 | 0.00 | 17 |
| stroke 176 | 14 % → 0 % | 19.1 px | 0.00 | 0.00 | 12 |
| stroke 177 | 28 % → 0 % | 39.4 px | 0.00 | 0.00 | 8 |
| stroke 178 | 26 % → 0 % | 42.8 px | 0.00 | 0.00 | 6 |
| stroke 179 | 26 % → 0 % | 41.6 px | 0.00 | 0.00 | 22 |
| stroke 180 | 30 % → 0 % | 45.6 px | 0.00 | 0.00 | 38 |
| stroke 181 | 32 % → 0 % | 46.0 px | 0.00 | 0.00 | 14 |
| stroke 182 | 31 % → 0 % | 43.3 px | 0.00 | 0.00 | 15 |
| stroke 183 | 6 % → 0 % | 11.4 px | 0.00 | 0.00 | 2 |
| stroke 184 | 10 % → 0 % | 15.8 px | 0.00 | 0.00 | 43 |
| stroke 185 | 12 % → 0 % | 19.1 px | 0.00 | 0.00 | 23 |
| stroke 186 | 17 % → 0 % | 26.7 px | 0.00 | 0.00 | 7 |
| stroke 187 | 15 % → 0 % | 24.5 px | 0.00 | 0.00 | 13 |
| stroke 188 | 7 % → 0 % | 12.3 px | 0.00 | 0.00 | 3 |
| stroke 189 | 8 % → 0 % | 15.4 px | 0.00 | 0.00 | 2 |
| stroke 190 | 13 % → 0 % | 28.1 px | 0.00 | 0.00 | 5 |
| stroke 191 | 15 % → 0 % | 22.9 px | 0.00 | 0.00 | 4 |
| stroke 192 | 17 % → 0 % | 21.0 px | 0.00 | 0.00 | 6 |
| stroke 193 | 9 % → 0 % | 12.8 px | 0.00 | 0.00 | 3 |
| stroke 194 | 5 % → 0 % | 13.5 px | 0.00 | 0.00 | 2 |
| stroke 195 | 19 % → 0 % | 10.4 px | 0.00 | 0.00 | 21 |
| stroke 196 | 11 % → 0 % | 20.7 px | 0.00 | 0.00 | 2 |
| stroke 197 | 17 % → 0 % | 31.7 px | 0.00 | 0.00 | 3 |
| stroke 198 | 19 % → 0 % | 32.8 px | 0.00 | 0.00 | 2 |
| stroke 199 | 7 % → 0 % | 10.2 px | 0.00 | 0.00 | 3 |
| stroke 200 | 9 % → 0 % | 13.3 px | 0.00 | 0.00 | 12 |
| stroke 201 | 13 % → 0 % | 20.4 px | 0.00 | 0.00 | 27 |
| stroke 202 | 19 % → 0 % | 24.7 px | 0.00 | 0.00 | 5 |
| stroke 203 | 34 % → 0 % | 59.8 px | 0.00 | 0.00 | 3 |
| stroke 204 | 29 % → 0 % | 39.1 px | 0.00 | 0.00 | 5 |
| stroke 205 | 22 % → 0 % | 29.3 px | 0.00 | 0.00 | 19 |
| stroke 206 | 25 % → 0 % | 50.1 px | 0.00 | 0.00 | 3 |
| stroke 207 | 30 % → 0 % | 40.8 px | 0.00 | 0.00 | 13 |
| stroke 208 | 21 % → 0 % | 28.8 px | 0.00 | 0.00 | 7 |
| stroke 209 | 28 % → 0 % | 76.4 px | 0.00 | 0.00 | 0 |
| stroke 210 | 23 % → 0 % | 34.9 px | 0.00 | 0.00 | 2 |
| stroke 211 | 13 % → 0 % | 27.5 px | 0.00 | 0.00 | 2 |
| stroke 212 | 29 % → 0 % | 52.1 px | 0.00 | 0.00 | 1 |
| stroke 213 | 20 % → 0 % | 29.6 px | 0.00 | 0.00 | 7 |
| stroke 214 | 23 % → 0 % | 32.8 px | 0.00 | 0.00 | 4 |
| stroke 215 | 16 % → 0 % | 25.4 px | 0.00 | 0.00 | 8 |
| stroke 216 | 24 % → 0 % | 31.8 px | 0.00 | 0.00 | 7 |
| stroke 217 | 19 % → 0 % | 27.6 px | 0.00 | 0.00 | 3 |
| stroke 218 | 26 % → 0 % | 37.5 px | 0.00 | 0.00 | 4 |
| stroke 219 | 27 % → 0 % | 35.1 px | 0.00 | 0.00 | 10 |
| stroke 220 | 24 % → 0 % | 33.6 px | 0.00 | 0.00 | 5 |
| stroke 221 | 22 % → 0 % | 59.7 px | 0.00 | 0.00 | 1 |
| stroke 222 | 8 % → 0 % | 12.8 px | 0.00 | 0.00 | 3 |
| stroke 223 | 6 % → 0 % | 14.6 px | 0.00 | 0.00 | 2 |
| stroke 224 | 16 % → 0 % | 19.0 px | 0.00 | 0.00 | 11 |
| stroke 225 | 14 % → 0 % | 26.2 px | 0.00 | 0.00 | 1 |
| stroke 226 | 20 % → 0 % | 20.6 px | 0.00 | 0.00 | 4 |
| stroke 227 | 6 % → 0 % | 16.7 px | 0.00 | 0.00 | 1 |
| stroke 228 | 23 % → 0 % | 18.7 px | 0.00 | 0.00 | 12 |
| stroke 229 | 28 % → 0 % | 25.0 px | 0.00 | 0.00 | 11 |
| stroke 230 | 13 % → 0 % | 16.6 px | 0.00 | 0.00 | 7 |
| stroke 231 | 7 % → 0 % | 11.5 px | 0.00 | 0.00 | 5 |
| stroke 232 | 13 % → 0 % | 37.9 px | 0.00 | 0.00 | 0 |
| stroke 233 | 7 % → 0 % | 11.4 px | 0.00 | 0.00 | 3 |
| stroke 234 | 13 % → 0 % | 11.5 px | 0.00 | 0.00 | 9 |
| stroke 235 | 24 % → 0 % | 22.5 px | 0.00 | 0.00 | 9 |
| stroke 236 | 27 % → 0 % | 33.2 px | 0.00 | 0.00 | 3 |
| stroke 237 | 11 % → 0 % | 10.9 px | 0.00 | 0.00 | 8 |
| stroke 238 | 11 % → 0 % | 10.6 px | 0.00 | 0.00 | 10 |
| stroke 239 | 21 % → 0 % | 41.9 px | 0.00 | 0.00 | 1 |
| stroke 240 | 19 % → 0 % | 27.1 px | 0.00 | 0.00 | 4 |
| stroke 241 | 18 % → 0 % | 44.5 px | 0.00 | 0.00 | 1 |
| stroke 242 | 13 % → 0 % | 25.2 px | 0.00 | 0.00 | 1 |
| stroke 243 | 10 % → 0 % | 10.6 px | 0.00 | 0.00 | 11 |
| stroke 244 | 7 % → 0 % | 11.9 px | 0.00 | 0.00 | 1 |
| stroke 245 | 13 % → 0 % | 33.0 px | 0.00 | 0.00 | 0 |
| stroke 246 | 15 % → 0 % | 16.3 px | 0.00 | 0.00 | 9 |
| stroke 247 | 20 % → 0 % | 25.3 px | 0.00 | 0.00 | 4 |
| stroke 248 | 19 % → 0 % | 22.7 px | 0.00 | 0.00 | 4 |
| stroke 249 | 5 % → 0 % | 12.5 px | 0.00 | 0.00 | 1 |
| stroke 250 | 8 % → 0 % | 12.8 px | 0.00 | 0.00 | 3 |
| stroke 251 | 7 % → 0 % | 13.4 px | 0.00 | 0.00 | 2 |
| stroke 252 | 8 % → 0 % | 11.5 px | 0.00 | 0.00 | 1 |
| stroke 253 | 10 % → 0 % | 21.0 px | 0.00 | 0.00 | 0 |
| stroke 254 | 14 % → 0 % | 12.4 px | 0.00 | 0.00 | 4 |
| stroke 255 | 18 % → 0 % | 14.1 px | 0.00 | 0.00 | 15 |
| stroke 256 | 33 % → 0 % | 28.4 px | 0.00 | 0.00 | 2 |
| stroke 257 | 10 % → 0 % | 7.8 px | 0.00 | 0.00 | 9 |
| stroke 258 | 8 % → 0 % | 13.1 px | 0.00 | 0.00 | 4 |
| stroke 259 | 11 % → 0 % | 15.9 px | 0.00 | 0.00 | 11 |
| stroke 260 | 15 % → 0 % | 23.9 px | 0.00 | 0.00 | 14 |
| stroke 261 | 16 % → 0 % | 34.6 px | 0.00 | 0.00 | 2 |
| stroke 262 | 32 % → 0 % | 61.4 px | 0.00 | 0.00 | 1 |
| stroke 263 | 11 % → 0 % | 17.7 px | 0.00 | 0.00 | 5 |
| stroke 264 | 7 % → 0 % | 12.6 px | 0.00 | 0.00 | 6 |
| stroke 265 | 13 % → 0 % | 18.1 px | 0.00 | 0.00 | 9 |
| stroke 266 | 6 % → 9 % | 13.4 px | 0.18 | 1.38 | 2 |
| stroke 267 | 18 % → 0 % | 25.2 px | 0.00 | 0.00 | 13 |
| stroke 268 | 12 % → 1 % | 16.7 px | 0.18 | 0.07 | 5 |
| stroke 269 | 21 % → 0 % | 30.7 px | 0.00 | 0.00 | 11 |
| stroke 270 | 34 % → 0 % | 50.2 px | 0.00 | 0.00 | 3 |
| stroke 271 | 20 % → 0 % | 36.6 px | 0.00 | 0.00 | 3 |
| stroke 272 | 31 % → 0 % | 44.5 px | 0.00 | 0.00 | 7 |
| stroke 273 | 24 % → 0 % | 52.6 px | 0.00 | 0.00 | 6 |
| stroke 274 | 31 % → 0 % | 44.1 px | 0.00 | 0.00 | 12 |
| stroke 275 | 33 % → 0 % | 55.1 px | 0.00 | 0.00 | 3 |
| stroke 276 | 26 % → 0 % | 54.9 px | 0.00 | 0.00 | 3 |
| stroke 277 | 26 % → 0 % | 54.6 px | 0.00 | 0.00 | 1 |
| stroke 278 | 21 % → 0 % | 58.1 px | 0.00 | 0.00 | 0 |
| stroke 279 | 12 % → 0 % | 34.7 px | 0.00 | 0.00 | 0 |
| stroke 280 | 17 % → 0 % | 20.0 px | 0.00 | 0.00 | 5 |
| stroke 281 | 24 % → 0 % | 28.4 px | 0.00 | 0.00 | 5 |
| stroke 282 | 8 % → 0 % | 20.9 px | 0.00 | 0.00 | 1 |
| stroke 283 | 24 % → 0 % | 27.7 px | 0.00 | 0.00 | 12 |
| stroke 284 | 25 % → 0 % | 29.8 px | 0.00 | 0.00 | 9 |
| stroke 285 | 8 % → 0 % | 14.1 px | 0.00 | 0.00 | 6 |
| stroke 286 | 14 % → 0 % | 20.6 px | 0.00 | 0.00 | 3 |
| stroke 287 | 11 % → 0 % | 12.1 px | 0.00 | 0.00 | 10 |
| stroke 288 | 18 % → 0 % | 18.2 px | 0.00 | 0.00 | 22 |
| stroke 289 | 30 % → 0 % | 31.3 px | 0.00 | 0.00 | 22 |
| stroke 290 | 9 % → 7 % | 12.5 px | 0.17 | 0.81 | 12 |
| stroke 291 | 16 % → 5 % | 24.1 px | 0.17 | 0.31 | 12 |
| stroke 292 | 15 % → 11 % | 31.4 px | 0.17 | 0.69 | 3 |
| stroke 293 | 18 % → 0 % | 28.4 px | 0.00 | 0.00 | 5 |
| stroke 294 | 20 % → 0 % | 39.9 px | 0.00 | 0.00 | 6 |
| stroke 295 | 8 % → 22 % | 12.6 px | 0.17 | 2.87 | 7 |
| stroke 296 | 16 % → 16 % | 27.9 px | 0.17 | 1.04 | 16 |
| stroke 297 | 24 % → 8 % | 45.5 px | 0.17 | 0.35 | 2 |
| stroke 298 | 22 % → 4 % | 64.2 px | 0.18 | 0.17 | 0 |
| stroke 299 | 7 % → 25 % | 18.5 px | 0.17 | 3.74 | 0 |
| stroke 300 | 11 % → 20 % | 21.7 px | 0.17 | 1.75 | 3 |
| stroke 301 | 9 % → 22 % | 17.1 px | 0.18 | 2.40 | 2 |
| stroke 302 | 7 % → 0 % | 11.4 px | 0.00 | 0.00 | 5 |
| stroke 303 | 10 % → 0 % | 16.8 px | 0.00 | 0.00 | 15 |
| stroke 304 | 19 % → 0 % | 30.0 px | 0.00 | 0.00 | 5 |
| stroke 305 | 5 % → 0 % | 13.6 px | 0.00 | 0.00 | 1 |
| stroke 306 | 14 % → 0 % | 22.3 px | 0.00 | 0.00 | 9 |
| stroke 307 | 15 % → 0 % | 24.4 px | 0.00 | 0.00 | 17 |
| stroke 308 | 23 % → 0 % | 36.4 px | 0.00 | 0.00 | 12 |
| stroke 309 | 32 % → 0 % | 50.2 px | 0.00 | 0.00 | 9 |
| stroke 310 | 21 % → 0 % | 60.3 px | 0.00 | 0.00 | 0 |
| stroke 311 | 23 % → 0 % | 36.9 px | 0.00 | 0.00 | 4 |
| stroke 312 | 16 % → 0 % | 27.2 px | 0.00 | 0.00 | 2 |
| stroke 313 | 8 % → 0 % | 10.4 px | 0.00 | 0.00 | 15 |
| stroke 314 | 15 % → 0 % | 18.1 px | 0.00 | 0.00 | 3 |
| stroke 315 | 17 % → 0 % | 18.5 px | 0.00 | 0.00 | 24 |
| stroke 316 | 7 % → 0 % | 12.8 px | 0.00 | 0.00 | 1 |
| stroke 317 | 19 % → 0 % | 20.3 px | 0.00 | 0.00 | 10 |
| stroke 318 | 12 % → 0 % | 18.8 px | 0.00 | 0.00 | 2 |
| stroke 319 | 14 % → 0 % | 37.7 px | 0.00 | 0.00 | 0 |
| stroke 320 | 14 % → 0 % | 18.5 px | 0.00 | 0.00 | 7 |
| stroke 321 | 15 % → 0 % | 18.6 px | 0.00 | 0.00 | 2 |
| stroke 322 | 16 % → 0 % | 15.7 px | 0.00 | 0.00 | 13 |
| stroke 323 | 20 % → 0 % | 21.5 px | 0.00 | 0.00 | 6 |
| stroke 324 | 20 % → 0 % | 25.4 px | 0.00 | 0.00 | 4 |
| stroke 325 | 4 % → 0 % | 11.1 px | 0.00 | 0.00 | 0 |
| stroke 326 | 9 % → 0 % | 11.2 px | 0.00 | 0.00 | 6 |
| stroke 327 | 17 % → 1 % | 18.5 px | 0.17 | 0.07 | 11 |
| stroke 328 | 7 % → 0 % | 16.3 px | 0.00 | 0.00 | 7 |
| stroke 329 | 6 % → 0 % | 12.4 px | 0.00 | 0.00 | 8 |
| stroke 330 | 12 % → 0 % | 31.5 px | 0.00 | 0.00 | 1 |
| stroke 331 | 16 % → 0 % | 40.9 px | 0.00 | 0.00 | 1 |
| stroke 332 | 6 % → 0 % | 17.0 px | 0.00 | 0.00 | 1 |
| stroke 333 | 11 % → 0 % | 10.1 px | 0.00 | 0.00 | 5 |
| stroke 334 | 16 % → 0 % | 9.6 px | 0.00 | 0.00 | 25 |
| stroke 335 | 26 % → 0 % | 28.2 px | 0.00 | 0.00 | 8 |
| stroke 336 | 29 % → 0 % | 29.4 px | 0.00 | 0.00 | 15 |
| stroke 337 | 27 % → 0 % | 49.3 px | 0.00 | 0.00 | 1 |
| stroke 338 | 28 % → 0 % | 29.6 px | 0.00 | 0.00 | 6 |
| stroke 339 | 25 % → 0 % | 25.3 px | 0.00 | 0.00 | 3 |
| stroke 340 | 5 % → 0 % | 15.0 px | 0.00 | 0.00 | 0 |
| stroke 341 | 6 % → 0 % | 12.3 px | 0.00 | 0.00 | 8 |
| stroke 342 | 11 % → 0 % | 25.3 px | 0.00 | 0.00 | 13 |
| stroke 343 | 11 % → 0 % | 32.9 px | 0.00 | 0.00 | 0 |
| stroke 344 | 8 % → 7 % | 12.7 px | 0.17 | 0.85 | 9 |
| stroke 345 | 14 % → 0 % | 12.5 px | 0.00 | 0.00 | 3 |
| stroke 346 | 5 % → 0 % | 14.4 px | 0.00 | 0.00 | 1 |
| stroke 347 | 9 % → 0 % | 9.2 px | 0.00 | 0.00 | 12 |
| stroke 348 | 18 % → 2 % | 16.5 px | 0.17 | 0.09 | 16 |
| stroke 349 | 25 % → 3 % | 23.6 px | 0.17 | 0.14 | 20 |
| stroke 350 | 26 % → 8 % | 24.1 px | 0.17 | 0.30 | 16 |
| stroke 351 | 26 % → 10 % | 25.1 px | 0.18 | 0.38 | 12 |
| stroke 352 | 28 % → 11 % | 27.5 px | 0.17 | 0.40 | 9 |
| stroke 353 | 28 % → 8 % | 29.6 px | 0.17 | 0.30 | 10 |
| stroke 354 | 26 % → 8 % | 28.6 px | 0.17 | 0.32 | 13 |
| stroke 355 | 22 % → 7 % | 26.9 px | 0.17 | 0.32 | 11 |
| stroke 356 | 21 % → 7 % | 33.8 px | 0.17 | 0.32 | 1 |
| stroke 357 | 5 % → 0 % | 13.8 px | 0.00 | 0.00 | 4 |
| stroke 358 | 10 % → 0 % | 19.0 px | 0.00 | 0.00 | 11 |
| stroke 359 | 15 % → 0 % | 24.0 px | 0.00 | 0.00 | 6 |
| stroke 360 | 19 % → 0 % | 28.7 px | 0.19 | 0.02 | 4 |
| stroke 361 | 20 % → 5 % | 28.3 px | 0.18 | 0.25 | 4 |
| stroke 362 | 22 % → 13 % | 32.3 px | 0.18 | 0.57 | 10 |
| stroke 363 | 26 % → 19 % | 37.4 px | 0.18 | 0.73 | 8 |
| stroke 364 | 25 % → 17 % | 42.2 px | 0.18 | 0.67 | 4 |
| stroke 365 | 17 % → 15 % | 37.6 px | 0.17 | 0.84 | 1 |
| stroke 366 | 6 % → 0 % | 13.6 px | 0.00 | 0.00 | 7 |
| stroke 367 | 6 % → 0 % | 15.8 px | 0.00 | 0.00 | 1 |
| stroke 368 | 5 % → 0 % | 12.3 px | 0.00 | 0.00 | 0 |
| stroke 369 | 8 % → 0 % | 9.4 px | 0.00 | 0.00 | 15 |
| stroke 370 | 11 % → 0 % | 14.4 px | 0.00 | 0.00 | 22 |
| stroke 371 | 18 % → 0 % | 23.5 px | 0.00 | 0.00 | 14 |
| stroke 372 | 11 % → 0 % | 23.5 px | 0.00 | 0.00 | 1 |
| stroke 373 | 8 % → 0 % | 22.4 px | 0.00 | 0.00 | 2 |
| stroke 374 | 23 % → 0 % | 27.6 px | 0.00 | 0.00 | 5 |
| stroke 375 | 27 % → 0 % | 40.9 px | 0.00 | 0.00 | 2 |
| stroke 376 | 26 % → 0 % | 34.6 px | 0.00 | 0.00 | 3 |
| stroke 377 | 19 % → 0 % | 49.6 px | 0.00 | 0.00 | 1 |
| stroke 378 | 10 % → 0 % | 27.6 px | 0.00 | 0.00 | 0 |
| stroke 379 | 5 % → 0 % | 14.8 px | 0.00 | 0.00 | 1 |
| stroke 380 | 11 % → 0 % | 23.0 px | 0.00 | 0.00 | 6 |
| stroke 381 | 16 % → 0 % | 29.0 px | 0.00 | 0.00 | 5 |
| stroke 382 | 18 % → 0 % | 28.3 px | 0.00 | 0.00 | 7 |
| stroke 383 | 23 % → 0 % | 35.7 px | 0.00 | 0.00 | 3 |
| stroke 384 | 18 % → 0 % | 50.0 px | 0.00 | 0.00 | 0 |
| stroke 385 | 5 % → 0 % | 14.6 px | 0.00 | 0.00 | 1 |
| stroke 386 | 11 % → 0 % | 16.9 px | 0.00 | 0.00 | 4 |
| stroke 387 | 10 % → 0 % | 14.7 px | 0.00 | 0.00 | 6 |
| stroke 388 | 6 % → 0 % | 12.6 px | 0.00 | 0.00 | 1 |
| stroke 389 | 11 % → 0 % | 21.4 px | 0.00 | 0.00 | 6 |
| stroke 390 | 12 % → 0 % | 20.1 px | 0.00 | 0.00 | 2 |
| stroke 391 | 16 % → 0 % | 45.3 px | 0.00 | 0.00 | 0 |
| stroke 392 | 5 % → 0 % | 14.2 px | 0.00 | 0.00 | 0 |
| stroke 393 | 7 % → 0 % | 11.1 px | 0.00 | 0.00 | 25 |
| stroke 394 | 10 % → 0 % | 17.8 px | 0.00 | 0.00 | 44 |
| stroke 395 | 14 % → 0 % | 26.4 px | 0.00 | 0.00 | 24 |
| stroke 396 | 24 % → 0 % | 39.2 px | 0.00 | 0.00 | 27 |
| stroke 397 | 15 % → 0 % | 25.2 px | 0.00 | 0.00 | 2 |
| stroke 398 | 31 % → 0 % | 43.1 px | 0.00 | 0.00 | 10 |
| stroke 399 | 29 % → 0 % | 54.8 px | 0.00 | 0.00 | 3 |
| stroke 400 | 7 % → 0 % | 11.0 px | 0.00 | 0.00 | 2 |
| stroke 401 | 12 % → 0 % | 32.0 px | 0.00 | 0.00 | 1 |
| stroke 402 | 7 % → 29 % | 9.6 px | 0.18 | 4.40 | 6 |
| stroke 403 | 11 % → 35 % | 13.9 px | 0.18 | 3.24 | 7 |
| stroke 404 | 15 % → 31 % | 19.7 px | 0.18 | 2.01 | 16 |
| stroke 405 | 21 % → 30 % | 28.0 px | 0.18 | 1.41 | 19 |
| stroke 406 | 9 % → 23 % | 14.0 px | 0.17 | 2.59 | 3 |
| stroke 407 | 20 % → 24 % | 24.8 px | 0.18 | 1.24 | 9 |
| stroke 408 | 31 % → 34 % | 39.3 px | 0.18 | 1.07 | 23 |
| stroke 409 | 13 % → 25 % | 20.2 px | 0.17 | 1.92 | 11 |
| stroke 410 | 12 % → 12 % | 25.0 px | 0.17 | 1.00 | 4 |
| stroke 411 | 25 % → 25 % | 50.9 px | 0.18 | 1.00 | 6 |
| stroke 412 | 18 % → 27 % | 26.8 px | 0.17 | 1.49 | 5 |
| stroke 413 | 18 % → 19 % | 48.8 px | 0.17 | 1.03 | 18 |
| stroke 414 | 14 % → 22 % | 35.3 px | 0.17 | 1.61 | 0 |
| stroke 415 | 5 % → 11 % | 14.0 px | 0.17 | 2.06 | 2 |
| stroke 416 | 15 % → 25 % | 39.3 px | 0.17 | 1.71 | 0 |
| stroke 417 | 11 % → 16 % | 25.5 px | 0.17 | 1.47 | 3 |
| stroke 418 | 12 % → 22 % | 25.6 px | 0.17 | 1.83 | 1 |
| stroke 419 | 12 % → 12 % | 27.4 px | 0.17 | 1.00 | 0 |
| stroke 420 | 13 % → 18 % | 23.4 px | 0.17 | 1.39 | 2 |
| stroke 421 | 16 % → 16 % | 31.7 px | 0.17 | 1.00 | 1 |
| stroke 422 | 7 % → 20 % | 13.7 px | 0.18 | 2.90 | 1 |
| stroke 423 | 13 % → 20 % | 25.9 px | 0.18 | 1.48 | 1 |
| stroke 424 | 20 % → 20 % | 38.8 px | 0.18 | 1.00 | 1 |
| stroke 425 | 5 % → 16 % | 15.0 px | 0.17 | 2.98 | 0 |
| stroke 426 | 11 % → 21 % | 23.3 px | 0.18 | 1.94 | 2 |
| stroke 427 | 14 % → 24 % | 27.8 px | 0.18 | 1.67 | 1 |
| stroke 428 | 7 % → 12 % | 11.9 px | 0.18 | 1.77 | 2 |
| stroke 429 | 13 % → 21 % | 20.9 px | 0.18 | 1.66 | 4 |
| stroke 430 | 14 % → 14 % | 22.2 px | 0.18 | 1.00 | 6 |

Numbers say: wet paint spreads well beyond the stroke.

## Refs v3 · #42 Pink shaggy pastel — own sheet
own sheet 800 × 976 · Pastel 1.00 · 38 px · 38.9 s

![Refs v3 · #42 Pink shaggy pastel — own sheet](Refs-v3-42-Pink-shaggy-pastel-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 4 % → 18 % | 44.1 px | 0.34 | 4.11 | 19 |
| stroke 2 | 4 % → 46 % | 48.3 px | 0.34 | 12.50 | 14 |
| stroke 3 | 9 % → 41 % | 74.9 px | 0.34 | 4.60 | 34 |
| stroke 4 | 13 % → 40 % | 128.4 px | 0.34 | 3.14 | 14 |
| stroke 5 | 7 % → 0 % | 36.3 px | 0.00 | 0.00 | 40 |
| stroke 6 | 11 % → 0 % | 46.8 px | 0.00 | 0.00 | 63 |
| stroke 7 | 18 % → 0 % | 100.5 px | 0.00 | 0.00 | 28 |
| stroke 8 | 21 % → 0 % | 95.5 px | 0.21 | 0.00 | 43 |
| stroke 9 | 29 % → 0 % | 368.5 px | 0.00 | 0.00 | 8 |
| stroke 10 | 25 % → 0 % | 112.9 px | 0.00 | 0.00 | 34 |
| stroke 11 | 31 % → 0 % | 385.2 px | 0.00 | 0.00 | 4 |
| stroke 12 | 26 % → 0 % | 95.3 px | 0.00 | 0.00 | 106 |
| stroke 13 | 18 % → 8 % | 182.7 px | 0.34 | 0.43 | 15 |
| stroke 14 | 26 % → 0 % | 90.3 px | 0.00 | 0.00 | 203 |
| stroke 15 | 35 % → 8 % | 128.1 px | 0.34 | 0.23 | 156 |
| stroke 16 | 27 % → 0 % | 108.7 px | 0.00 | 0.00 | 106 |
| stroke 17 | 36 % → 20 % | 139.0 px | 0.34 | 0.55 | 111 |
| stroke 18 | 48 % → 0 % | 362.1 px | 0.00 | 0.00 | 30 |
| stroke 19 | 31 % → 0 % | 117.6 px | 0.00 | 0.00 | 90 |
| stroke 20 | 31 % → 9 % | 111.6 px | 0.34 | 0.29 | 445 |
| stroke 21 | 45 % → 16 % | 162.5 px | 0.34 | 0.35 | 143 |
| stroke 22 | 36 % → 0 % | 133.1 px | 0.00 | 0.00 | 138 |
| stroke 23 | 46 % → 21 % | 192.9 px | 0.34 | 0.46 | 79 |
| stroke 24 | 55 % → 0 % | 309.0 px | 0.00 | 0.00 | 23 |
| stroke 25 | 43 % → 0 % | 166.4 px | 0.00 | 0.00 | 50 |
| stroke 26 | 47 % → 24 % | 186.9 px | 0.34 | 0.52 | 57 |
| stroke 27 | 53 % → 0 % | 268.4 px | 0.00 | 0.00 | 30 |
| stroke 28 | 47 % → 0 % | 240.9 px | 0.00 | 0.00 | 33 |
| stroke 29 | 51 % → 18 % | 198.3 px | 0.35 | 0.36 | 58 |
| stroke 30 | 50 % → 0 % | 419.7 px | 0.00 | 0.00 | 13 |
| stroke 31 | 41 % → 0 % | 210.2 px | 0.00 | 0.00 | 29 |
| stroke 32 | 51 % → 22 % | 286.9 px | 0.35 | 0.44 | 40 |
| stroke 33 | 54 % → 0 % | 402.8 px | 0.34 | 0.00 | 28 |
| stroke 34 | 46 % → 0 % | 447.9 px | 0.00 | 0.00 | 14 |
| stroke 35 | 35 % → 0 % | 167.9 px | 0.00 | 0.00 | 35 |
| stroke 36 | 51 % → 21 % | 335.2 px | 0.35 | 0.41 | 20 |
| stroke 37 | 53 % → 0 % | 446.7 px | 0.33 | 0.00 | 19 |
| stroke 38 | 41 % → 0 % | 549.1 px | 0.00 | 0.00 | 8 |
| stroke 39 | 33 % → 0 % | 166.7 px | 0.36 | 0.01 | 47 |
| stroke 40 | 50 % → 11 % | 206.6 px | 0.35 | 0.22 | 114 |
| stroke 41 | 38 % → 0 % | 468.2 px | 0.00 | 0.00 | 5 |
| stroke 42 | 32 % → 0 % | 168.8 px | 0.00 | 0.00 | 44 |
| stroke 43 | 42 % → 8 % | 161.2 px | 0.35 | 0.18 | 98 |
| stroke 44 | 29 % → 0 % | 153.2 px | 0.00 | 0.00 | 48 |
| stroke 45 | 44 % → 16 % | 571.8 px | 0.35 | 0.37 | 8 |
| stroke 46 | 40 % → 2 % | 142.8 px | 0.34 | 0.06 | 150 |
| stroke 47 | 41 % → 18 % | 248.5 px | 0.34 | 0.44 | 19 |
| stroke 48 | 41 % → 3 % | 153.8 px | 0.35 | 0.08 | 96 |
| stroke 49 | 31 % → 0 % | 140.8 px | 0.33 | 0.00 | 45 |
| stroke 50 | 42 % → 14 % | 423.8 px | 0.35 | 0.33 | 7 |
| stroke 51 | 42 % → 2 % | 154.8 px | 0.35 | 0.06 | 98 |
| stroke 52 | 36 % → 0 % | 173.9 px | 0.00 | 0.00 | 50 |
| stroke 53 | 49 % → 1 % | 626.2 px | 0.35 | 0.03 | 8 |
| stroke 54 | 44 % → 0 % | 177.7 px | 0.00 | 0.00 | 98 |
| stroke 55 | 35 % → 0 % | 198.5 px | 0.00 | 0.00 | 34 |
| stroke 56 | 33 % → 10 % | 409.5 px | 0.35 | 0.31 | 10 |
| stroke 57 | 45 % → 0 % | 176.1 px | 0.00 | 0.00 | 72 |
| stroke 58 | 32 % → 0 % | 208.4 px | 0.00 | 0.00 | 19 |
| stroke 59 | 40 % → 3 % | 174.8 px | 0.34 | 0.07 | 43 |
| stroke 60 | 49 % → 0 % | 179.1 px | 0.00 | 0.00 | 78 |
| stroke 61 | 27 % → 1 % | 200.5 px | 0.34 | 0.02 | 10 |
| stroke 62 | 29 % → 0 % | 363.8 px | 0.33 | 0.01 | 5 |
| stroke 63 | 47 % → 0 % | 166.1 px | 0.00 | 0.00 | 129 |
| stroke 64 | 30 % → 0 % | 202.6 px | 0.00 | 0.00 | 19 |
| stroke 65 | 48 % → 0 % | 169.3 px | 0.00 | 0.00 | 142 |
| stroke 66 | 34 % → 0 % | 225.5 px | 0.00 | 0.00 | 19 |
| stroke 67 | 39 % → 0 % | 518.2 px | 0.00 | 0.00 | 4 |
| stroke 68 | 49 % → 0 % | 178.8 px | 0.00 | 0.00 | 91 |
| stroke 69 | 46 % → 0 % | 167.6 px | 0.00 | 0.00 | 112 |
| stroke 70 | 32 % → 0 % | 268.4 px | 0.00 | 0.00 | 20 |
| stroke 71 | 49 % → 0 % | 412.5 px | 0.00 | 0.00 | 20 |
| stroke 72 | 53 % → 0 % | 446.0 px | 0.00 | 0.00 | 24 |
| stroke 73 | 48 % → 0 % | 244.9 px | 0.00 | 0.00 | 51 |
| stroke 74 | 40 % → 0 % | 212.2 px | 0.00 | 0.00 | 42 |
| stroke 75 | 54 % → 0 % | 457.0 px | 0.00 | 0.00 | 12 |
| stroke 76 | 12 % → 0 % | 23.7 px | 0.00 | 0.00 | 171 |
| stroke 77 | 19 % → 0 % | 48.1 px | 0.00 | 0.00 | 125 |
| stroke 78 | 26 % → 0 % | 67.6 px | 0.00 | 0.00 | 158 |
| stroke 79 | 33 % → 0 % | 85.2 px | 0.00 | 0.00 | 128 |
| stroke 80 | 40 % → 0 % | 103.6 px | 0.00 | 0.00 | 98 |
| stroke 81 | 40 % → 0 % | 105.1 px | 0.00 | 0.00 | 91 |
| stroke 82 | 39 % → 0 % | 99.2 px | 0.20 | 0.00 | 149 |
| stroke 83 | 42 % → 1 % | 134.7 px | 0.35 | 0.02 | 107 |
| stroke 84 | 37 % → 1 % | 233.0 px | 0.35 | 0.03 | 21 |
| stroke 85 | 6 % → 0 % | 30.2 px | 0.00 | 0.00 | 24 |
| stroke 86 | 40 % → 0 % | 151.2 px | 0.36 | 0.01 | 276 |
| stroke 87 | 30 % → 0 % | 73.4 px | 0.36 | 0.01 | 207 |
| stroke 88 | 35 % → 0 % | 97.5 px | 0.00 | 0.00 | 99 |
| stroke 89 | 47 % → 2 % | 299.2 px | 0.34 | 0.04 | 22 |
| stroke 90 | 33 % → 2 % | 133.7 px | 0.34 | 0.05 | 34 |
| stroke 91 | 41 % → 0 % | 113.4 px | 0.00 | 0.00 | 81 |
| stroke 92 | 49 % → 1 % | 595.4 px | 0.36 | 0.01 | 13 |
| stroke 93 | 47 % → 0 % | 149.3 px | 0.00 | 0.00 | 65 |
| stroke 94 | 46 % → 1 % | 570.8 px | 0.35 | 0.03 | 18 |
| stroke 95 | 51 % → 0 % | 187.5 px | 0.00 | 0.00 | 62 |
| stroke 96 | 45 % → 2 % | 177.5 px | 0.34 | 0.03 | 54 |
| stroke 97 | 50 % → 0 % | 194.8 px | 0.00 | 0.00 | 60 |
| stroke 98 | 54 % → 0 % | 280.1 px | 0.00 | 0.00 | 41 |
| stroke 99 | 57 % → 2 % | 682.1 px | 0.34 | 0.04 | 10 |
| stroke 100 | 49 % → 0 % | 334.8 px | 0.00 | 0.00 | 29 |
| stroke 101 | 57 % → 2 % | 440.1 px | 0.34 | 0.03 | 34 |
| stroke 102 | 54 % → 2 % | 502.7 px | 0.34 | 0.04 | 24 |
| stroke 103 | 1 % → 0 % | 19.4 px | 0.00 | 0.00 | 1 |
| stroke 104 | 3 % → 2 % | 22.8 px | 0.34 | 0.48 | 13 |
| stroke 105 | 12 % → 11 % | 32.4 px | 0.34 | 0.89 | 100 |
| stroke 106 | 20 % → 16 % | 83.0 px | 0.34 | 0.82 | 45 |
| stroke 107 | 16 % → 6 % | 38.5 px | 0.34 | 0.37 | 246 |
| stroke 108 | 25 % → 16 % | 115.9 px | 0.34 | 0.63 | 39 |
| stroke 109 | 24 % → 5 % | 58.6 px | 0.34 | 0.23 | 363 |
| stroke 110 | 29 % → 17 % | 140.0 px | 0.34 | 0.60 | 46 |
| stroke 111 | 31 % → 15 % | 176.6 px | 0.34 | 0.47 | 21 |
| stroke 112 | 29 % → 0 % | 100.6 px | 0.00 | 0.00 | 79 |
| stroke 113 | 31 % → 23 % | 142.0 px | 0.34 | 0.74 | 38 |
| stroke 114 | 35 % → 16 % | 219.9 px | 0.34 | 0.46 | 19 |
| stroke 115 | 41 % → 0 % | 231.9 px | 0.00 | 0.00 | 28 |
| stroke 116 | 32 % → 0 % | 306.4 px | 0.00 | 0.00 | 17 |
| stroke 117 | 28 % → 28 % | 111.5 px | 0.34 | 1.01 | 29 |
| stroke 118 | 33 % → 23 % | 202.9 px | 0.34 | 0.70 | 22 |
| stroke 119 | 45 % → 0 % | 193.5 px | 0.00 | 0.00 | 44 |
| stroke 120 | 28 % → 26 % | 134.9 px | 0.34 | 0.95 | 34 |
| stroke 121 | 27 % → 32 % | 190.5 px | 0.34 | 1.21 | 18 |
| stroke 122 | 40 % → 0 % | 174.0 px | 0.00 | 0.00 | 34 |
| stroke 123 | 28 % → 27 % | 146.6 px | 0.34 | 0.96 | 18 |
| stroke 124 | 38 % → 0 % | 357.7 px | 0.00 | 0.00 | 11 |
| stroke 125 | 27 % → 31 % | 129.9 px | 0.34 | 1.15 | 27 |
| stroke 126 | 28 % → 0 % | 352.0 px | 0.00 | 0.00 | 14 |
| stroke 127 | 26 % → 29 % | 117.1 px | 0.34 | 1.14 | 46 |
| stroke 128 | 25 % → 28 % | 126.0 px | 0.34 | 1.11 | 40 |
| stroke 129 | 27 % → 22 % | 169.1 px | 0.34 | 0.82 | 45 |
| stroke 130 | 28 % → 22 % | 231.9 px | 0.34 | 0.78 | 15 |
| stroke 131 | 25 % → 18 % | 276.3 px | 0.34 | 0.73 | 11 |
| stroke 132 | 22 % → 18 % | 244.5 px | 0.34 | 0.80 | 9 |
| stroke 133 | 19 % → 16 % | 217.1 px | 0.34 | 0.88 | 8 |
| stroke 134 | 17 % → 13 % | 190.3 px | 0.34 | 0.79 | 9 |
| stroke 135 | 16 % → 16 % | 76.9 px | 0.34 | 0.96 | 22 |
| stroke 136 | 18 % → 14 % | 89.2 px | 0.34 | 0.74 | 26 |
| stroke 137 | 21 % → 14 % | 94.9 px | 0.34 | 0.66 | 26 |
| stroke 138 | 23 % → 10 % | 100.2 px | 0.35 | 0.41 | 32 |
| stroke 139 | 27 % → 3 % | 118.5 px | 0.34 | 0.13 | 33 |
| stroke 140 | 30 % → 0 % | 186.5 px | 0.00 | 0.00 | 19 |
| stroke 141 | 32 % → 0 % | 403.9 px | 0.33 | 0.01 | 8 |
| stroke 142 | 32 % → 0 % | 229.7 px | 0.00 | 0.00 | 16 |
| stroke 143 | 26 % → 0 % | 93.0 px | 0.00 | 0.00 | 49 |
| stroke 144 | 32 % → 0 % | 182.5 px | 0.00 | 0.00 | 20 |
| stroke 145 | 31 % → 0 % | 196.4 px | 0.00 | 0.00 | 17 |
| stroke 146 | 26 % → 0 % | 84.1 px | 0.00 | 0.00 | 52 |
| stroke 147 | 32 % → 0 % | 353.0 px | 0.00 | 0.00 | 8 |
| stroke 148 | 33 % → 0 % | 159.7 px | 0.00 | 0.00 | 22 |
| stroke 149 | 31 % → 0 % | 154.1 px | 0.00 | 0.00 | 27 |
| stroke 150 | 30 % → 0 % | 147.3 px | 0.00 | 0.00 | 33 |
| stroke 151 | 30 % → 0 % | 335.1 px | 0.00 | 0.00 | 10 |
| stroke 152 | 35 % → 0 % | 169.2 px | 0.00 | 0.00 | 63 |
| stroke 153 | 29 % → 0 % | 239.1 px | 0.00 | 0.00 | 7 |
| stroke 154 | 35 % → 0 % | 218.6 px | 0.00 | 0.00 | 23 |
| stroke 155 | 31 % → 0 % | 194.3 px | 0.00 | 0.00 | 37 |
| stroke 156 | 31 % → 0 % | 138.1 px | 0.00 | 0.00 | 22 |
| stroke 157 | 43 % → 41 % | 417.6 px | 0.34 | 0.94 | 10 |
| stroke 158 | 53 % → 34 % | 644.4 px | 0.34 | 0.64 | 13 |
| stroke 159 | 6 % → 2 % | 37.7 px | 0.34 | 0.32 | 49 |
| stroke 160 | 10 % → 1 % | 51.9 px | 0.34 | 0.15 | 36 |
| stroke 161 | 14 % → 1 % | 55.3 px | 0.34 | 0.07 | 47 |
| stroke 162 | 15 % → 0 % | 93.2 px | 0.00 | 0.00 | 21 |
| stroke 163 | 17 % → 1 % | 52.8 px | 0.34 | 0.03 | 77 |
| stroke 164 | 26 % → 0 % | 215.0 px | 0.36 | 0.00 | 12 |
| stroke 165 | 22 % → 0 % | 76.5 px | 0.00 | 0.00 | 53 |
| stroke 166 | 25 % → 0 % | 79.2 px | 0.00 | 0.00 | 69 |
| stroke 167 | 36 % → 0 % | 335.0 px | 0.00 | 0.00 | 14 |
| stroke 168 | 29 % → 0 % | 102.3 px | 0.00 | 0.00 | 42 |
| stroke 169 | 24 % → 0 % | 150.4 px | 0.00 | 0.00 | 15 |
| stroke 170 | 33 % → 0 % | 76.9 px | 0.00 | 0.00 | 153 |
| stroke 171 | 23 % → 0 % | 90.6 px | 0.00 | 0.00 | 46 |
| stroke 172 | 37 % → 0 % | 87.3 px | 0.00 | 0.00 | 201 |
| stroke 173 | 28 % → 0 % | 98.7 px | 0.00 | 0.00 | 46 |
| stroke 174 | 46 % → 0 % | 118.5 px | 0.00 | 0.00 | 164 |
| stroke 175 | 43 % → 0 % | 113.5 px | 0.00 | 0.00 | 167 |
| stroke 176 | 4 % → 12 % | 44.2 px | 0.35 | 2.63 | 15 |
| stroke 177 | 37 % → 0 % | 354.9 px | 0.00 | 0.00 | 15 |
| stroke 178 | 4 % → 0 % | 46.4 px | 0.00 | 0.00 | 8 |
| stroke 179 | 8 % → 0 % | 48.8 px | 0.00 | 0.00 | 25 |
| stroke 180 | 12 % → 0 % | 158.1 px | 0.00 | 0.00 | 10 |
| stroke 181 | 2 % → 0 % | 19.8 px | 0.00 | 0.00 | 3 |
| stroke 182 | 2 % → 0 % | 24.0 px | 0.00 | 0.00 | 2 |
| stroke 183 | 1 % → 0 % | 19.2 px | 0.00 | 0.00 | 6 |
| stroke 184 | 4 % → 0 % | 19.6 px | 0.00 | 0.00 | 16 |
| stroke 185 | 2 % → 0 % | 43.5 px | 0.00 | 0.00 | 4 |
| stroke 186 | 5 % → 0 % | 47.0 px | 0.00 | 0.00 | 6 |
| stroke 187 | 7 % → 0 % | 129.3 px | 0.00 | 0.00 | 2 |
| stroke 188 | 3 % → 0 % | 46.3 px | 0.00 | 0.00 | 4 |
| stroke 189 | 9 % → 0 % | 152.0 px | 0.00 | 0.00 | 5 |
| stroke 190 | 5 % → 0 % | 59.7 px | 0.00 | 0.00 | 6 |
| stroke 191 | 12 % → 0 % | 207.0 px | 0.00 | 0.00 | 2 |
| stroke 192 | 15 % → 0 % | 78.1 px | 0.00 | 0.00 | 18 |
| stroke 193 | 19 % → 0 % | 194.2 px | 0.00 | 0.00 | 10 |
| stroke 194 | 3 % → 0 % | 42.7 px | 0.33 | 0.05 | 2 |
| stroke 195 | 4 % → 0 % | 69.3 px | 0.00 | 0.00 | 2 |
| stroke 196 | 5 % → 0 % | 79.9 px | 0.32 | 0.00 | 4 |
| stroke 197 | 10 % → 0 % | 60.5 px | 0.00 | 0.00 | 18 |
| stroke 198 | 14 % → 0 % | 131.7 px | 0.00 | 0.00 | 18 |
| stroke 199 | 18 % → 0 % | 144.7 px | 0.00 | 0.00 | 12 |
| stroke 200 | 21 % → 0 % | 85.3 px | 0.00 | 0.00 | 25 |
| stroke 201 | 23 % → 0 % | 375.4 px | 0.00 | 0.00 | 3 |
| stroke 202 | 31 % → 0 % | 369.5 px | 0.00 | 0.00 | 7 |
| stroke 203 | 25 % → 0 % | 297.0 px | 0.00 | 0.00 | 9 |
| stroke 204 | 26 % → 0 % | 486.8 px | 0.00 | 0.00 | 3 |
| stroke 205 | 13 % → 15 % | 69.5 px | 0.34 | 1.17 | 24 |
| stroke 206 | 20 % → 8 % | 80.1 px | 0.34 | 0.42 | 62 |
| stroke 207 | 31 % → 16 % | 391.3 px | 0.35 | 0.51 | 12 |
| stroke 208 | 31 % → 4 % | 147.8 px | 0.35 | 0.14 | 44 |
| stroke 209 | 38 % → 12 % | 746.6 px | 0.35 | 0.31 | 3 |
| stroke 210 | 28 % → 0 % | 364.0 px | 0.00 | 0.00 | 5 |
| stroke 211 | 3 % → 0 % | 37.7 px | 0.00 | 0.00 | 7 |
| stroke 212 | 5 % → 0 % | 62.6 px | 0.00 | 0.00 | 5 |
| stroke 213 | 10 % → 0 % | 135.8 px | 0.00 | 0.00 | 5 |
| stroke 214 | 10 % → 0 % | 105.0 px | 0.00 | 0.00 | 5 |
| stroke 215 | 14 % → 0 % | 76.3 px | 0.00 | 0.00 | 28 |
| stroke 216 | 25 % → 0 % | 139.6 px | 0.00 | 0.00 | 27 |
| stroke 217 | 23 % → 0 % | 295.6 px | 0.00 | 0.00 | 11 |
| stroke 218 | 3 % → 1 % | 61.6 px | 0.34 | 0.15 | 4 |
| stroke 219 | 4 % → 1 % | 29.8 px | 0.32 | 0.26 | 6 |
| stroke 220 | 6 % → 0 % | 54.1 px | 0.24 | 0.02 | 25 |
| stroke 221 | 10 % → 3 % | 74.9 px | 0.34 | 0.29 | 33 |
| stroke 222 | 9 % → 0 % | 81.9 px | 0.00 | 0.00 | 17 |
| stroke 223 | 9 % → 0 % | 154.4 px | 0.00 | 0.00 | 4 |
| stroke 224 | 13 % → 0 % | 71.8 px | 0.00 | 0.00 | 58 |
| stroke 225 | 3 % → 0 % | 55.8 px | 0.00 | 0.00 | 16 |
| stroke 226 | 13 % → 0 % | 68.8 px | 0.00 | 0.00 | 73 |
| stroke 227 | 24 % → 0 % | 413.3 px | 0.00 | 0.00 | 11 |
| stroke 228 | 15 % → 0 % | 131.0 px | 0.00 | 0.00 | 20 |
| stroke 229 | 4 % → 0 % | 33.1 px | 0.00 | 0.00 | 35 |
| stroke 230 | 7 % → 0 % | 45.2 px | 0.00 | 0.00 | 28 |
| stroke 231 | 10 % → 0 % | 61.2 px | 0.00 | 0.00 | 25 |
| stroke 232 | 13 % → 0 % | 93.4 px | 0.00 | 0.00 | 12 |
| stroke 233 | 18 % → 0 % | 179.3 px | 0.00 | 0.00 | 27 |
| stroke 234 | 3 % → 0 % | 44.6 px | 0.00 | 0.00 | 6 |
| stroke 235 | 9 % → 0 % | 86.9 px | 0.00 | 0.00 | 7 |
| stroke 236 | 13 % → 0 % | 132.3 px | 0.00 | 0.00 | 6 |
| stroke 237 | 13 % → 0 % | 112.1 px | 0.00 | 0.00 | 16 |
| stroke 238 | 14 % → 0 % | 246.3 px | 0.00 | 0.00 | 2 |
| stroke 239 | 13 % → 0 % | 229.0 px | 0.00 | 0.00 | 2 |
| stroke 240 | 4 % → 0 % | 28.8 px | 0.00 | 0.00 | 9 |
| stroke 241 | 7 % → 0 % | 35.0 px | 0.00 | 0.00 | 25 |
| stroke 242 | 11 % → 0 % | 48.9 px | 0.00 | 0.00 | 78 |
| stroke 243 | 21 % → 0 % | 110.4 px | 0.00 | 0.00 | 49 |
| stroke 244 | 18 % → 0 % | 96.9 px | 0.00 | 0.00 | 50 |
| stroke 245 | 18 % → 0 % | 161.0 px | 0.00 | 0.00 | 9 |
| stroke 246 | 15 % → 0 % | 84.8 px | 0.00 | 0.00 | 30 |
| stroke 247 | 15 % → 0 % | 62.3 px | 0.00 | 0.00 | 43 |
| stroke 248 | 19 % → 0 % | 96.6 px | 0.00 | 0.00 | 48 |
| stroke 249 | 23 % → 0 % | 166.2 px | 0.00 | 0.00 | 18 |
| stroke 250 | 24 % → 1 % | 234.8 px | 0.36 | 0.02 | 9 |
| stroke 251 | 23 % → 1 % | 148.5 px | 0.35 | 0.06 | 17 |
| stroke 252 | 28 % → 0 % | 272.4 px | 0.00 | 0.00 | 13 |
| stroke 253 | 21 % → 2 % | 200.3 px | 0.34 | 0.10 | 15 |
| stroke 254 | 23 % → 2 % | 396.3 px | 0.34 | 0.10 | 20 |
| stroke 255 | 20 % → 2 % | 161.8 px | 0.34 | 0.10 | 9 |
| stroke 256 | 20 % → 2 % | 141.1 px | 0.34 | 0.10 | 7 |
| stroke 257 | 19 % → 2 % | 188.7 px | 0.34 | 0.11 | 10 |
| stroke 258 | 16 % → 2 % | 117.2 px | 0.34 | 0.12 | 15 |
| stroke 259 | 24 % → 1 % | 312.8 px | 0.35 | 0.05 | 5 |
| stroke 260 | 14 % → 1 % | 224.3 px | 0.35 | 0.09 | 5 |
| stroke 261 | 35 % → 2 % | 617.2 px | 0.34 | 0.07 | 4 |
| stroke 262 | 20 % → 2 % | 196.7 px | 0.34 | 0.10 | 10 |
| stroke 263 | 27 % → 2 % | 214.4 px | 0.34 | 0.08 | 6 |
| stroke 264 | 46 % → 2 % | 584.4 px | 0.34 | 0.05 | 6 |
| stroke 265 | 25 % → 2 % | 304.2 px | 0.34 | 0.09 | 6 |
| stroke 266 | 25 % → 2 % | 205.6 px | 0.34 | 0.08 | 6 |
| stroke 267 | 45 % → 2 % | 530.3 px | 0.34 | 0.05 | 4 |
| stroke 268 | 28 % → 2 % | 330.1 px | 0.34 | 0.08 | 38 |
| stroke 269 | 29 % → 2 % | 340.6 px | 0.34 | 0.08 | 19 |
| stroke 270 | 28 % → 2 % | 227.5 px | 0.34 | 0.08 | 14 |
| stroke 271 | 28 % → 2 % | 270.1 px | 0.34 | 0.08 | 24 |
| stroke 272 | 22 % → 2 % | 272.4 px | 0.34 | 0.10 | 5 |
| stroke 273 | 6 % → 0 % | 25.7 px | 0.00 | 0.00 | 44 |
| stroke 274 | 10 % → 0 % | 39.4 px | 0.00 | 0.00 | 30 |
| stroke 275 | 15 % → 0 % | 179.2 px | 0.00 | 0.00 | 4 |
| stroke 276 | 15 % → 0 % | 190.7 px | 0.00 | 0.00 | 14 |
| stroke 277 | 17 % → 0 % | 291.4 px | 0.00 | 0.00 | 7 |
| stroke 278 | 17 % → 0 % | 281.1 px | 0.00 | 0.00 | 4 |
| stroke 279 | 19 % → 0 % | 245.9 px | 0.00 | 0.00 | 11 |
| stroke 280 | 17 % → 0 % | 271.8 px | 0.00 | 0.00 | 3 |
| stroke 281 | 21 % → 0 % | 273.1 px | 0.00 | 0.00 | 9 |
| stroke 282 | 21 % → 0 % | 238.6 px | 0.00 | 0.00 | 7 |
| stroke 283 | 19 % → 0 % | 231.9 px | 0.00 | 0.00 | 5 |
| stroke 284 | 20 % → 0 % | 320.1 px | 0.00 | 0.00 | 2 |
| stroke 285 | 17 % → 0 % | 279.8 px | 0.00 | 0.00 | 2 |
| stroke 286 | 16 % → 0 % | 283.9 px | 0.00 | 0.00 | 2 |
| stroke 287 | 15 % → 0 % | 252.0 px | 0.00 | 0.00 | 4 |
| stroke 288 | 13 % → 0 % | 203.0 px | 0.00 | 0.00 | 2 |
| stroke 289 | 19 % → 0 % | 186.1 px | 0.00 | 0.00 | 4 |
| stroke 290 | 15 % → 0 % | 185.9 px | 0.00 | 0.00 | 6 |
| stroke 291 | 24 % → 0 % | 84.7 px | 0.00 | 0.00 | 22 |
| stroke 292 | 27 % → 0 % | 97.3 px | 0.00 | 0.00 | 36 |
| stroke 293 | 30 % → 0 % | 108.8 px | 0.00 | 0.00 | 53 |
| stroke 294 | 33 % → 0 % | 117.4 px | 0.00 | 0.00 | 31 |
| stroke 295 | 32 % → 0 % | 165.9 px | 0.00 | 0.00 | 62 |
| stroke 296 | 3 % → 0 % | 16.6 px | 0.00 | 0.00 | 25 |
| stroke 297 | 5 % → 0 % | 36.8 px | 0.00 | 0.00 | 70 |
| stroke 298 | 4 % → 0 % | 47.4 px | 0.00 | 0.00 | 8 |
| stroke 299 | 8 % → 0 % | 38.7 px | 0.00 | 0.00 | 58 |
| stroke 300 | 13 % → 0 % | 129.4 px | 0.00 | 0.00 | 22 |
| stroke 301 | 6 % → 0 % | 40.1 px | 0.00 | 0.00 | 20 |
| stroke 302 | 10 % → 0 % | 49.9 px | 0.00 | 0.00 | 33 |
| stroke 303 | 14 % → 0 % | 77.7 px | 0.00 | 0.00 | 33 |
| stroke 304 | 19 % → 0 % | 108.1 px | 0.00 | 0.00 | 31 |
| stroke 305 | 22 % → 0 % | 110.0 px | 0.00 | 0.00 | 29 |
| stroke 306 | 24 % → 0 % | 128.2 px | 0.00 | 0.00 | 34 |
| stroke 307 | 25 % → 0 % | 204.7 px | 0.00 | 0.00 | 25 |
| stroke 308 | 1 % → 0 % | 13.0 px | 0.00 | 0.00 | 4 |
| stroke 309 | 3 % → 25 % | 29.5 px | 0.34 | 7.31 | 10 |
| stroke 310 | 6 % → 22 % | 35.4 px | 0.34 | 3.74 | 21 |
| stroke 311 | 8 % → 20 % | 42.2 px | 0.34 | 2.41 | 29 |
| stroke 312 | 16 % → 35 % | 279.3 px | 0.34 | 2.16 | 6 |
| stroke 313 | 18 % → 38 % | 319.6 px | 0.34 | 2.12 | 2 |
| stroke 314 | 19 % → 37 % | 239.7 px | 0.34 | 2.02 | 7 |
| stroke 315 | 17 % → 30 % | 100.4 px | 0.34 | 1.76 | 19 |
| stroke 316 | 20 % → 36 % | 119.9 px | 0.34 | 1.78 | 9 |
| stroke 317 | 27 % → 42 % | 482.4 px | 0.34 | 1.59 | 2 |
| stroke 318 | 21 % → 42 % | 272.0 px | 0.34 | 1.94 | 7 |
| stroke 319 | 18 % → 38 % | 180.9 px | 0.34 | 2.10 | 15 |
| stroke 320 | 20 % → 33 % | 127.2 px | 0.34 | 1.69 | 22 |
| stroke 321 | 18 % → 36 % | 137.4 px | 0.34 | 2.04 | 19 |
| stroke 322 | 17 % → 38 % | 107.7 px | 0.34 | 2.27 | 61 |
| stroke 323 | 22 % → 41 % | 188.2 px | 0.34 | 1.92 | 10 |
| stroke 324 | 19 % → 39 % | 194.9 px | 0.34 | 2.01 | 10 |
| stroke 325 | 26 % → 41 % | 454.5 px | 0.34 | 1.60 | 7 |
| stroke 326 | 19 % → 34 % | 292.3 px | 0.35 | 1.81 | 2 |
| stroke 327 | 22 % → 36 % | 403.1 px | 0.34 | 1.66 | 4 |
| stroke 328 | 16 % → 28 % | 205.7 px | 0.35 | 1.77 | 6 |
| stroke 329 | 20 % → 34 % | 374.7 px | 0.34 | 1.69 | 3 |
| stroke 330 | 15 % → 26 % | 158.2 px | 0.35 | 1.68 | 7 |
| stroke 331 | 19 % → 28 % | 148.0 px | 0.34 | 1.45 | 11 |
| stroke 332 | 21 % → 27 % | 143.6 px | 0.34 | 1.29 | 15 |
| stroke 333 | 24 % → 27 % | 164.5 px | 0.34 | 1.12 | 9 |
| stroke 334 | 24 % → 24 % | 169.4 px | 0.34 | 1.00 | 29 |
| stroke 335 | 2 % → 2 % | 40.7 px | 0.34 | 1.00 | 2 |

Numbers say: wet paint spreads well beyond the stroke.

## Refs v3 · #43 Dragged black blocks — own sheet
own sheet 800 × 1115 · Ink 0.93 · Gouache 0.07 · 112 px · 77.6 s

![Refs v3 · #43 Dragged black blocks — own sheet](Refs-v3-43-Dragged-black-blocks-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 11 % → 68 % | 102.1 px | 0.51 | 6.08 | 186 |
| stroke 2 | 16 % → 73 % | 160.9 px | 0.51 | 4.59 | 204 |
| stroke 3 | 18 % → 76 % | 212.6 px | 0.51 | 4.16 | 241 |
| stroke 4 | 21 % → 79 % | 266.3 px | 0.51 | 3.71 | 332 |
| stroke 5 | 22 % → 82 % | 223.4 px | 0.51 | 3.68 | 671 |
| stroke 6 | 26 % → 87 % | 337.4 px | 0.51 | 3.29 | 385 |
| stroke 7 | 26 % → 88 % | 269.1 px | 0.51 | 3.42 | 490 |
| stroke 8 | 23 % → 54 % | 528.0 px | 0.51 | 2.32 | 197 |
| stroke 9 | 27 % → 78 % | 233.0 px | 0.51 | 2.94 | 1473 |
| stroke 10 | 28 % → 78 % | 263.6 px | 0.51 | 2.75 | 1792 |
| stroke 11 | 31 % → 78 % | 307.2 px | 0.51 | 2.48 | 976 |
| stroke 12 | 35 % → 82 % | 341.0 px | 0.51 | 2.35 | 1399 |
| stroke 13 | 41 % → 92 % | 418.4 px | 0.51 | 2.27 | 869 |
| stroke 14 | 44 % → 85 % | 787.0 px | 0.51 | 1.92 | 342 |
| stroke 15 | 37 % → 86 % | 378.1 px | 0.51 | 2.36 | 1317 |
| stroke 16 | 17 % → 54 % | 161.9 px | 0.50 | 3.12 | 274 |
| stroke 17 | 38 % → 88 % | 406.5 px | 0.51 | 2.31 | 1642 |
| stroke 18 | 34 % → 65 % | 288.9 px | 0.50 | 1.90 | 1705 |
| stroke 19 | 43 % → 82 % | 377.4 px | 0.51 | 1.91 | 2461 |
| stroke 20 | 46 % → 82 % | 434.6 px | 0.51 | 1.80 | 2201 |
| stroke 21 | 51 % → 92 % | 448.0 px | 0.50 | 1.81 | 2014 |
| stroke 22 | 56 % → 78 % | 626.4 px | 0.50 | 1.41 | 355 |
| stroke 23 | 59 % → 91 % | 468.2 px | 0.51 | 1.53 | 2525 |
| stroke 24 | 58 % → 89 % | 448.3 px | 0.50 | 1.54 | 769 |
| stroke 25 | 66 % → 86 % | 642.8 px | 0.50 | 1.30 | 1160 |
| stroke 26 | 59 % → 86 % | 498.0 px | 0.50 | 1.46 | 928 |
| stroke 27 | 67 % → 88 % | 653.3 px | 0.50 | 1.31 | 903 |
| stroke 28 | 61 % → 85 % | 597.7 px | 0.50 | 1.40 | 961 |
| stroke 29 | 67 % → 89 % | 669.7 px | 0.50 | 1.32 | 771 |
| stroke 30 | 63 % → 89 % | 634.7 px | 0.50 | 1.42 | 577 |
| stroke 31 | 67 % → 89 % | 684.4 px | 0.50 | 1.33 | 547 |
| stroke 32 | 65 % → 91 % | 651.4 px | 0.50 | 1.40 | 531 |
| stroke 33 | 66 % → 88 % | 721.1 px | 0.50 | 1.33 | 501 |
| stroke 34 | 63 % → 89 % | 628.9 px | 0.51 | 1.41 | 580 |
| stroke 35 | 66 % → 87 % | 751.7 px | 0.51 | 1.32 | 327 |
| stroke 36 | 69 % → 88 % | 644.3 px | 0.51 | 1.28 | 519 |
| stroke 37 | 67 % → 86 % | 876.0 px | 0.51 | 1.28 | 192 |
| stroke 38 | 71 % → 86 % | 615.5 px | 0.51 | 1.21 | 412 |
| stroke 39 | 76 % → 85 % | 574.4 px | 0.51 | 1.12 | 429 |
| stroke 40 | 77 % → 82 % | 526.0 px | 0.51 | 1.07 | 412 |
| stroke 41 | 78 % → 81 % | 603.1 px | 0.51 | 1.03 | 253 |
| stroke 42 | 84 % → 85 % | 893.3 px | 0.51 | 1.01 | 94 |

Numbers say: wet paint spreads well beyond the stroke.

## Refs v3 · #44 Blue looping ribbon — own sheet
own sheet 800 × 1204 · Oil 0.52 · Gouache 0.48 + turpentine 10 % · 64 px · 59.8 s

![Refs v3 · #44 Blue looping ribbon — own sheet](Refs-v3-44-Blue-looping-ribbon-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 2 % → 53 % | 72.0 px | 0.61 | 22.12 | 84 |
| stroke 2 | 11 % → 27 % | 66.1 px | 0.61 | 2.48 | 291 |
| stroke 3 | 11 % → 34 % | 73.6 px | 0.61 | 3.13 | 272 |
| stroke 4 | 20 % → 45 % | 170.2 px | 0.61 | 2.25 | 211 |
| stroke 5 | 18 % → 42 % | 145.0 px | 0.61 | 2.39 | 140 |
| stroke 6 | 34 % → 45 % | 863.6 px | 0.61 | 1.33 | 33 |
| stroke 7 | 38 % → 41 % | 345.1 px | 0.61 | 1.06 | 118 |
| stroke 8 | 9 % → 34 % | 177.9 px | 0.62 | 4.03 | 20 |
| stroke 9 | 16 % → 43 % | 208.9 px | 0.62 | 2.78 | 48 |
| stroke 10 | 14 % → 34 % | 70.3 px | 0.62 | 2.52 | 148 |
| stroke 11 | 22 % → 22 % | 358.9 px | 0.62 | 1.02 | 48 |
| stroke 12 | 24 % → 34 % | 292.7 px | 0.62 | 1.40 | 137 |
| stroke 13 | 29 % → 24 % | 507.9 px | 0.62 | 0.80 | 79 |
| stroke 14 | 32 % → 48 % | 259.0 px | 0.62 | 1.50 | 99 |
| stroke 15 | 2 % → 67 % | 71.1 px | 0.62 | 26.98 | 21 |
| stroke 16 | 9 % → 64 % | 99.4 px | 0.62 | 7.12 | 88 |
| stroke 17 | 11 % → 67 % | 254.0 px | 0.62 | 6.30 | 27 |
| stroke 18 | 18 % → 63 % | 161.8 px | 0.62 | 3.40 | 108 |
| stroke 19 | 22 % → 61 % | 334.2 px | 0.61 | 2.75 | 35 |
| stroke 20 | 26 % → 62 % | 576.2 px | 0.61 | 2.37 | 35 |
| stroke 21 | 33 % → 62 % | 435.5 px | 0.61 | 1.91 | 96 |
| stroke 22 | 29 % → 66 % | 348.7 px | 0.62 | 2.31 | 125 |
| stroke 23 | 33 % → 69 % | 862.6 px | 0.62 | 2.13 | 32 |
| stroke 24 | 24 % → 56 % | 564.1 px | 0.62 | 2.33 | 27 |
| stroke 25 | 20 % → 65 % | 332.1 px | 0.62 | 3.17 | 42 |
| stroke 26 | 18 % → 62 % | 460.9 px | 0.62 | 3.38 | 33 |
| stroke 27 | 17 % → 64 % | 191.1 px | 0.62 | 3.74 | 74 |
| stroke 28 | 28 % → 60 % | 246.9 px | 0.62 | 2.10 | 130 |
| stroke 29 | 19 % → 53 % | 145.5 px | 0.62 | 2.74 | 34 |
| stroke 30 | 12 % → 68 % | 134.5 px | 0.62 | 5.81 | 72 |
| stroke 31 | 7 % → 69 % | 217.2 px | 0.63 | 10.64 | 24 |
| stroke 32 | 8 % → 51 % | 112.0 px | 0.61 | 5.99 | 35 |
| stroke 33 | 14 % → 48 % | 134.8 px | 0.61 | 3.50 | 53 |
| stroke 34 | 23 % → 48 % | 84.7 px | 0.61 | 2.12 | 370 |
| stroke 35 | 8 % → 35 % | 75.9 px | 0.63 | 4.32 | 68 |
| stroke 36 | 3 % → 77 % | 90.3 px | 0.61 | 22.62 | 29 |
| stroke 37 | 6 % → 75 % | 185.2 px | 0.61 | 13.42 | 22 |
| stroke 38 | 12 % → 54 % | 114.8 px | 0.62 | 4.54 | 189 |
| stroke 39 | 19 % → 50 % | 212.5 px | 0.61 | 2.62 | 84 |
| stroke 40 | 19 % → 65 % | 184.7 px | 0.61 | 3.35 | 131 |
| stroke 41 | 21 % → 36 % | 472.5 px | 0.62 | 1.74 | 19 |
| stroke 42 | 34 % → 38 % | 218.3 px | 0.62 | 1.12 | 206 |
| stroke 43 | 29 % → 34 % | 377.5 px | 0.62 | 1.18 | 128 |
| stroke 44 | 3 % → 61 % | 89.4 px | 0.61 | 21.59 | 23 |
| stroke 45 | 4 % → 44 % | 72.9 px | 0.61 | 10.80 | 89 |
| stroke 46 | 4 % → 32 % | 88.2 px | 0.61 | 8.59 | 45 |
| stroke 47 | 4 % → 41 % | 67.0 px | 0.62 | 9.67 | 72 |
| stroke 48 | 4 % → 61 % | 76.2 px | 0.62 | 13.95 | 56 |
| stroke 49 | 4 % → 41 % | 68.4 px | 0.62 | 10.18 | 26 |
| stroke 50 | 6 % → 36 % | 137.3 px | 0.61 | 5.95 | 52 |
| stroke 51 | 7 % → 60 % | 68.7 px | 0.62 | 8.97 | 166 |
| stroke 52 | 12 % → 56 % | 112.6 px | 0.62 | 4.75 | 100 |
| stroke 53 | 9 % → 53 % | 140.7 px | 0.61 | 5.83 | 50 |
| stroke 54 | 15 % → 61 % | 133.2 px | 0.62 | 3.94 | 88 |
| stroke 55 | 7 % → 63 % | 257.3 px | 0.61 | 9.12 | 23 |
| stroke 56 | 13 % → 36 % | 99.2 px | 0.61 | 2.76 | 194 |
| stroke 57 | 10 % → 59 % | 126.5 px | 0.61 | 6.10 | 52 |
| stroke 58 | 14 % → 40 % | 151.6 px | 0.62 | 2.84 | 50 |
| stroke 59 | 6 % → 62 % | 83.5 px | 0.62 | 10.91 | 65 |
| stroke 60 | 13 % → 53 % | 116.8 px | 0.61 | 4.13 | 162 |
| stroke 61 | 6 % → 71 % | 63.0 px | 0.62 | 11.80 | 124 |
| stroke 62 | 16 % → 61 % | 252.7 px | 0.61 | 3.95 | 65 |
| stroke 63 | 11 % → 73 % | 190.3 px | 0.62 | 6.58 | 70 |
| stroke 64 | 17 % → 63 % | 219.5 px | 0.62 | 3.80 | 55 |
| stroke 65 | 18 % → 68 % | 179.3 px | 0.62 | 3.79 | 105 |
| stroke 66 | 12 % → 64 % | 258.9 px | 0.62 | 5.20 | 35 |
| stroke 67 | 18 % → 64 % | 255.8 px | 0.62 | 3.49 | 64 |
| stroke 68 | 11 % → 56 % | 108.3 px | 0.62 | 5.08 | 135 |
| stroke 69 | 14 % → 50 % | 236.2 px | 0.61 | 3.49 | 70 |
| stroke 70 | 16 % → 59 % | 127.2 px | 0.62 | 3.75 | 73 |
| stroke 71 | 27 % → 61 % | 310.0 px | 0.61 | 2.30 | 93 |
| stroke 72 | 21 % → 51 % | 281.7 px | 0.62 | 2.37 | 52 |
| stroke 73 | 27 % → 71 % | 229.4 px | 0.62 | 2.64 | 189 |
| stroke 74 | 28 % → 59 % | 193.1 px | 0.63 | 2.07 | 170 |
| stroke 75 | 23 % → 67 % | 344.8 px | 0.61 | 2.91 | 157 |
| stroke 76 | 23 % → 59 % | 317.1 px | 0.61 | 2.53 | 56 |
| stroke 77 | 29 % → 60 % | 333.4 px | 0.61 | 2.07 | 86 |
| stroke 78 | 27 % → 65 % | 895.6 px | 0.61 | 2.42 | 15 |
| stroke 79 | 27 % → 61 % | 534.2 px | 0.62 | 2.28 | 47 |
| stroke 80 | 33 % → 47 % | 290.4 px | 0.62 | 1.42 | 72 |
| stroke 81 | 25 % → 56 % | 427.3 px | 0.61 | 2.24 | 79 |
| stroke 82 | 45 % → 74 % | 442.0 px | 0.61 | 1.65 | 254 |
| stroke 83 | 37 % → 72 % | 904.6 px | 0.62 | 1.94 | 44 |
| stroke 84 | 46 % → 56 % | 537.5 px | 0.62 | 1.22 | 76 |
| stroke 85 | 33 % → 56 % | 240.6 px | 0.62 | 1.69 | 94 |
| stroke 86 | 39 % → 69 % | 789.5 px | 0.62 | 1.76 | 31 |
| stroke 87 | 46 % → 74 % | 416.2 px | 0.62 | 1.63 | 202 |
| stroke 88 | 30 % → 60 % | 732.9 px | 0.61 | 2.00 | 22 |
| stroke 89 | 31 % → 57 % | 413.3 px | 0.62 | 1.84 | 102 |
| stroke 90 | 35 % → 46 % | 259.6 px | 0.61 | 1.33 | 132 |
| stroke 91 | 32 % → 64 % | 258.9 px | 0.62 | 2.02 | 182 |
| stroke 92 | 22 % → 55 % | 227.9 px | 0.62 | 2.49 | 67 |
| stroke 93 | 28 % → 53 % | 205.7 px | 0.62 | 1.88 | 256 |
| stroke 94 | 31 % → 45 % | 268.0 px | 0.62 | 1.45 | 278 |
| stroke 95 | 41 % → 64 % | 824.0 px | 0.62 | 1.54 | 56 |
| stroke 96 | 42 % → 64 % | 381.1 px | 0.62 | 1.53 | 172 |
| stroke 97 | 51 % → 63 % | 766.8 px | 0.62 | 1.24 | 70 |
| stroke 98 | 45 % → 71 % | 612.4 px | 0.62 | 1.57 | 85 |
| stroke 99 | 34 % → 53 % | 298.5 px | 0.62 | 1.55 | 159 |
| stroke 100 | 60 % → 68 % | 861.1 px | 0.61 | 1.12 | 114 |
| stroke 101 | 43 % → 51 % | 360.0 px | 0.61 | 1.19 | 286 |
| stroke 102 | 47 % → 66 % | 696.5 px | 0.62 | 1.39 | 138 |
| stroke 103 | 53 % → 68 % | 823.5 px | 0.62 | 1.28 | 101 |
| stroke 104 | 41 % → 58 % | 395.7 px | 0.61 | 1.43 | 151 |
| stroke 105 | 42 % → 53 % | 759.3 px | 0.61 | 1.28 | 77 |
| stroke 106 | 46 % → 50 % | 359.0 px | 0.62 | 1.09 | 426 |
| stroke 107 | 46 % → 60 % | 471.4 px | 0.61 | 1.32 | 182 |
| stroke 108 | 49 % → 65 % | 989.6 px | 0.61 | 1.34 | 71 |
| stroke 109 | 45 % → 58 % | 485.3 px | 0.63 | 1.30 | 136 |
| stroke 110 | 39 % → 60 % | 1473.7 px | 0.61 | 1.52 | 8 |
| stroke 111 | 58 % → 70 % | 1250.9 px | 0.62 | 1.20 | 40 |
| stroke 112 | 41 % → 61 % | 337.7 px | 0.62 | 1.51 | 100 |
| stroke 113 | 42 % → 48 % | 394.1 px | 0.63 | 1.13 | 110 |
| stroke 114 | 60 % → 64 % | 986.2 px | 0.61 | 1.07 | 57 |
| stroke 115 | 44 % → 54 % | 552.3 px | 0.61 | 1.21 | 85 |
| stroke 116 | 52 % → 54 % | 1408.9 px | 0.63 | 1.03 | 21 |
| stroke 117 | 55 % → 57 % | 890.0 px | 0.62 | 1.04 | 34 |
| stroke 118 | 53 % → 59 % | 579.1 px | 0.62 | 1.12 | 146 |
| stroke 119 | 61 % → 66 % | 572.2 px | 0.62 | 1.08 | 123 |
| stroke 120 | 45 % → 57 % | 402.4 px | 0.62 | 1.25 | 139 |
| stroke 121 | 52 % → 60 % | 587.2 px | 0.62 | 1.14 | 39 |
| stroke 122 | 50 % → 51 % | 817.2 px | 0.61 | 1.02 | 50 |
| stroke 123 | 53 % → 63 % | 911.6 px | 0.62 | 1.19 | 28 |
| stroke 124 | 68 % → 68 % | 756.5 px | 0.62 | 1.00 | 157 |
| stroke 125 | 70 % → 73 % | 1596.2 px | 0.61 | 1.04 | 28 |
| stroke 126 | 52 % → 52 % | 517.7 px | 0.62 | 1.00 | 86 |
| stroke 127 | 69 % → 69 % | 914.5 px | 0.61 | 1.00 | 72 |
| stroke 128 | 61 % → 62 % | 580.9 px | 0.62 | 1.02 | 119 |
| stroke 129 | 69 % → 70 % | 1291.5 px | 0.62 | 1.00 | 35 |
| stroke 130 | 27 % → 27 % | 365.5 px | 0.61 | 1.00 | 77 |

Numbers say: wet paint spreads well beyond the stroke.

## Refs v3 · #45 Pastel pepper — own sheet
own sheet 800 × 800 · Pastel 1.00 · 64 px · 27.9 s

![Refs v3 · #45 Pastel pepper — own sheet](Refs-v3-45-Pastel-pepper-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 4 % → 3 % | 55.7 px | 0.16 | 0.81 | 104 |
| stroke 2 | 5 % → 0 % | 63.7 px | 0.00 | 0.00 | 53 |
| stroke 3 | 13 % → 2 % | 58.2 px | 0.16 | 0.17 | 506 |
| stroke 4 | 18 % → 4 % | 124.3 px | 0.16 | 0.25 | 156 |
| stroke 5 | 20 % → 1 % | 130.7 px | 0.16 | 0.04 | 154 |
| stroke 6 | 19 % → 5 % | 195.6 px | 0.16 | 0.26 | 77 |
| stroke 7 | 26 % → 0 % | 290.9 px | 0.00 | 0.00 | 67 |
| stroke 8 | 20 % → 4 % | 305.1 px | 0.16 | 0.21 | 53 |
| stroke 9 | 23 % → 4 % | 386.5 px | 0.16 | 0.18 | 40 |
| stroke 10 | 16 % → 0 % | 132.5 px | 0.00 | 0.00 | 77 |
| stroke 11 | 15 % → 0 % | 157.9 px | 0.00 | 0.00 | 40 |
| stroke 12 | 19 % → 0 % | 198.1 px | 0.00 | 0.00 | 46 |
| stroke 13 | 20 % → 0 % | 164.1 px | 0.00 | 0.00 | 90 |
| stroke 14 | 21 % → 0 % | 162.5 px | 0.00 | 0.00 | 95 |
| stroke 15 | 22 % → 0 % | 154.9 px | 0.00 | 0.00 | 110 |
| stroke 16 | 24 % → 0 % | 148.7 px | 0.00 | 0.00 | 161 |
| stroke 17 | 25 % → 0 % | 152.6 px | 0.00 | 0.00 | 211 |
| stroke 18 | 25 % → 1 % | 159.1 px | 0.16 | 0.03 | 261 |
| stroke 19 | 25 % → 1 % | 159.1 px | 0.16 | 0.03 | 337 |
| stroke 20 | 27 % → 1 % | 180.4 px | 0.16 | 0.02 | 296 |
| stroke 21 | 21 % → 2 % | 154.1 px | 0.16 | 0.08 | 264 |
| stroke 22 | 44 % → 0 % | 562.6 px | 0.00 | 0.00 | 57 |
| stroke 23 | 20 % → 2 % | 145.7 px | 0.16 | 0.09 | 407 |
| stroke 24 | 27 % → 2 % | 219.1 px | 0.16 | 0.09 | 228 |
| stroke 25 | 33 % → 2 % | 287.6 px | 0.16 | 0.08 | 168 |
| stroke 26 | 35 % → 3 % | 329.5 px | 0.16 | 0.07 | 141 |
| stroke 27 | 37 % → 2 % | 431.7 px | 0.16 | 0.06 | 65 |
| stroke 28 | 33 % → 1 % | 585.9 px | 0.16 | 0.03 | 46 |
| stroke 29 | 26 % → 2 % | 500.2 px | 0.16 | 0.08 | 31 |
| stroke 30 | 25 % → 3 % | 440.9 px | 0.16 | 0.13 | 37 |
| stroke 31 | 24 % → 3 % | 411.0 px | 0.16 | 0.13 | 45 |
| stroke 32 | 33 % → 3 % | 535.2 px | 0.16 | 0.09 | 64 |
| stroke 33 | 35 % → 2 % | 222.9 px | 0.16 | 0.05 | 206 |
| stroke 34 | 38 % → 2 % | 250.1 px | 0.16 | 0.06 | 977 |
| stroke 35 | 44 % → 2 % | 345.1 px | 0.16 | 0.04 | 160 |
| stroke 36 | 3 % → 3 % | 20.4 px | 0.16 | 1.03 | 39 |
| stroke 37 | 5 % → 1 % | 33.3 px | 0.15 | 0.20 | 34 |
| stroke 38 | 7 % → 1 % | 44.0 px | 0.16 | 0.18 | 65 |
| stroke 39 | 10 % → 2 % | 54.6 px | 0.16 | 0.20 | 104 |
| stroke 40 | 15 % → 2 % | 301.9 px | 0.16 | 0.17 | 12 |
| stroke 41 | 15 % → 1 % | 191.6 px | 0.16 | 0.08 | 16 |
| stroke 42 | 14 % → 3 % | 228.8 px | 0.16 | 0.22 | 14 |
| stroke 43 | 16 % → 1 % | 295.9 px | 0.16 | 0.07 | 20 |
| stroke 44 | 13 % → 3 % | 185.7 px | 0.16 | 0.25 | 24 |
| stroke 45 | 16 % → 4 % | 245.3 px | 0.16 | 0.22 | 24 |
| stroke 46 | 20 % → 4 % | 539.8 px | 0.16 | 0.17 | 10 |
| stroke 47 | 12 % → 1 % | 245.2 px | 0.16 | 0.09 | 7 |
| stroke 48 | 11 % → 1 % | 235.7 px | 0.16 | 0.10 | 26 |
| stroke 49 | 7 % → 0 % | 66.8 px | 0.18 | 0.00 | 170 |
| stroke 50 | 10 % → 0 % | 110.5 px | 0.19 | 0.00 | 126 |
| stroke 51 | 5 % → 4 % | 76.5 px | 0.16 | 0.71 | 66 |
| stroke 52 | 12 % → 3 % | 122.2 px | 0.16 | 0.27 | 115 |
| stroke 53 | 15 % → 3 % | 127.5 px | 0.16 | 0.18 | 195 |
| stroke 54 | 18 % → 2 % | 136.8 px | 0.16 | 0.11 | 306 |
| stroke 55 | 31 % → 2 % | 297.8 px | 0.16 | 0.07 | 147 |
| stroke 56 | 21 % → 3 % | 289.3 px | 0.16 | 0.14 | 55 |
| stroke 57 | 36 % → 3 % | 565.5 px | 0.16 | 0.08 | 31 |
| stroke 58 | 22 % → 3 % | 438.4 px | 0.16 | 0.14 | 40 |
| stroke 59 | 15 % → 2 % | 114.7 px | 0.16 | 0.12 | 110 |
| stroke 60 | 7 % → 0 % | 54.2 px | 0.00 | 0.00 | 77 |
| stroke 61 | 12 % → 0 % | 63.3 px | 0.00 | 0.00 | 176 |
| stroke 62 | 20 % → 0 % | 151.1 px | 0.00 | 0.00 | 87 |
| stroke 63 | 23 % → 0 % | 260.4 px | 0.00 | 0.00 | 54 |
| stroke 64 | 24 % → 0 % | 303.9 px | 0.00 | 0.00 | 110 |
| stroke 65 | 26 % → 0 % | 393.0 px | 0.00 | 0.00 | 80 |
| stroke 66 | 24 % → 0 % | 319.3 px | 0.00 | 0.00 | 56 |
| stroke 67 | 20 % → 0 % | 195.5 px | 0.00 | 0.00 | 127 |
| stroke 68 | 18 % → 0 % | 165.8 px | 0.16 | 0.03 | 125 |
| stroke 69 | 18 % → 1 % | 174.4 px | 0.16 | 0.05 | 98 |
| stroke 70 | 19 % → 1 % | 176.3 px | 0.16 | 0.08 | 76 |
| stroke 71 | 21 % → 2 % | 197.9 px | 0.16 | 0.10 | 92 |
| stroke 72 | 22 % → 3 % | 205.3 px | 0.16 | 0.13 | 80 |
| stroke 73 | 22 % → 4 % | 220.6 px | 0.16 | 0.16 | 77 |
| stroke 74 | 22 % → 5 % | 302.5 px | 0.16 | 0.22 | 59 |
| stroke 75 | 21 % → 5 % | 321.6 px | 0.16 | 0.24 | 57 |
| stroke 76 | 21 % → 5 % | 370.6 px | 0.16 | 0.25 | 44 |
| stroke 77 | 26 % → 5 % | 530.6 px | 0.16 | 0.21 | 46 |
| stroke 78 | 29 % → 5 % | 496.6 px | 0.16 | 0.17 | 50 |
| stroke 79 | 33 % → 4 % | 676.0 px | 0.16 | 0.13 | 50 |
| stroke 80 | 35 % → 4 % | 735.2 px | 0.16 | 0.11 | 95 |
| stroke 81 | 37 % → 4 % | 151.5 px | 0.16 | 0.12 | 279 |
| stroke 82 | 53 % → 4 % | 467.9 px | 0.16 | 0.07 | 139 |
| stroke 83 | 46 % → 2 % | 670.2 px | 0.16 | 0.05 | 44 |
| stroke 84 | 46 % → 2 % | 322.8 px | 0.16 | 0.04 | 186 |
| stroke 85 | 41 % → 0 % | 689.0 px | 0.00 | 0.00 | 39 |
| stroke 86 | 48 % → 1 % | 264.6 px | 0.16 | 0.02 | 309 |
| stroke 87 | 50 % → 1 % | 288.4 px | 0.16 | 0.02 | 331 |
| stroke 88 | 52 % → 1 % | 298.0 px | 0.16 | 0.02 | 674 |
| stroke 89 | 51 % → 1 % | 322.8 px | 0.16 | 0.02 | 223 |
| stroke 90 | 11 % → 0 % | 101.2 px | 0.00 | 0.00 | 101 |
| stroke 91 | 19 % → 0 % | 125.6 px | 0.00 | 0.00 | 152 |
| stroke 92 | 27 % → 0 % | 149.4 px | 0.16 | 0.01 | 200 |
| stroke 93 | 37 % → 1 % | 212.2 px | 0.16 | 0.02 | 185 |
| stroke 94 | 31 % → 0 % | 318.8 px | 0.00 | 0.00 | 40 |
| stroke 95 | 2 % → 4 % | 30.2 px | 0.16 | 2.61 | 7 |
| stroke 96 | 2 % → 4 % | 38.9 px | 0.16 | 1.71 | 8 |
| stroke 97 | 3 % → 4 % | 48.6 px | 0.16 | 1.18 | 27 |
| stroke 98 | 5 % → 4 % | 39.4 px | 0.16 | 0.78 | 80 |
| stroke 99 | 7 % → 3 % | 267.1 px | 0.16 | 0.45 | 5 |
| stroke 100 | 11 % → 7 % | 185.1 px | 0.16 | 0.62 | 8 |
| stroke 101 | 2 % → 0 % | 29.7 px | 0.00 | 0.00 | 23 |
| stroke 102 | 3 % → 0 % | 102.0 px | 0.00 | 0.00 | 6 |
| stroke 103 | 4 % → 0 % | 69.7 px | 0.00 | 0.00 | 8 |
| stroke 104 | 5 % → 0 % | 94.8 px | 0.00 | 0.00 | 7 |
| stroke 105 | 7 % → 0 % | 209.5 px | 0.00 | 0.00 | 7 |
| stroke 106 | 6 % → 1 % | 103.4 px | 0.16 | 0.09 | 8 |
| stroke 107 | 9 % → 0 % | 190.6 px | 0.00 | 0.00 | 4 |
| stroke 108 | 7 % → 2 % | 90.7 px | 0.16 | 0.22 | 23 |
| stroke 109 | 10 % → 0 % | 177.2 px | 0.00 | 0.00 | 12 |
| stroke 110 | 6 % → 3 % | 45.8 px | 0.16 | 0.57 | 74 |
| stroke 111 | 11 % → 0 % | 198.8 px | 0.00 | 0.00 | 10 |
| stroke 112 | 6 % → 4 % | 114.3 px | 0.16 | 0.62 | 10 |
| stroke 113 | 12 % → 0 % | 212.9 px | 0.00 | 0.00 | 7 |
| stroke 114 | 8 % → 3 % | 94.8 px | 0.16 | 0.45 | 17 |
| stroke 115 | 13 % → 0 % | 200.2 px | 0.00 | 0.00 | 10 |
| stroke 116 | 8 % → 4 % | 116.3 px | 0.16 | 0.44 | 12 |
| stroke 117 | 14 % → 0 % | 228.0 px | 0.00 | 0.00 | 7 |
| stroke 118 | 9 % → 3 % | 110.3 px | 0.16 | 0.39 | 33 |
| stroke 119 | 14 % → 0 % | 292.8 px | 0.00 | 0.00 | 17 |
| stroke 120 | 10 % → 3 % | 120.9 px | 0.16 | 0.33 | 23 |
| stroke 121 | 15 % → 0 % | 266.9 px | 0.00 | 0.00 | 33 |
| stroke 122 | 10 % → 3 % | 140.9 px | 0.16 | 0.26 | 27 |
| stroke 123 | 16 % → 0 % | 427.1 px | 0.00 | 0.00 | 9 |
| stroke 124 | 11 % → 3 % | 139.4 px | 0.16 | 0.24 | 32 |
| stroke 125 | 15 % → 0 % | 309.0 px | 0.00 | 0.00 | 9 |
| stroke 126 | 13 % → 2 % | 443.3 px | 0.16 | 0.14 | 3 |
| stroke 127 | 15 % → 2 % | 398.7 px | 0.16 | 0.15 | 8 |
| stroke 128 | 15 % → 0 % | 308.4 px | 0.16 | 0.02 | 16 |
| stroke 129 | 14 % → 1 % | 523.6 px | 0.16 | 0.09 | 3 |
| stroke 130 | 17 % → 2 % | 603.1 px | 0.16 | 0.11 | 3 |
| stroke 131 | 17 % → 1 % | 261.8 px | 0.16 | 0.08 | 22 |
| stroke 132 | 15 % → 1 % | 528.2 px | 0.16 | 0.06 | 2 |
| stroke 133 | 17 % → 1 % | 622.2 px | 0.16 | 0.08 | 6 |
| stroke 134 | 16 % → 0 % | 617.3 px | 0.16 | 0.03 | 3 |
| stroke 135 | 18 % → 1 % | 711.7 px | 0.16 | 0.07 | 5 |
| stroke 136 | 17 % → 0 % | 635.5 px | 0.16 | 0.01 | 5 |
| stroke 137 | 19 % → 1 % | 519.3 px | 0.16 | 0.05 | 8 |
| stroke 138 | 18 % → 0 % | 667.7 px | 0.00 | 0.00 | 4 |
| stroke 139 | 18 % → 2 % | 271.3 px | 0.16 | 0.13 | 28 |
| stroke 140 | 20 % → 0 % | 723.5 px | 0.00 | 0.00 | 5 |
| stroke 141 | 19 % → 1 % | 731.1 px | 0.16 | 0.07 | 9 |
| stroke 142 | 20 % → 0 % | 706.6 px | 0.16 | 0.01 | 3 |
| stroke 143 | 15 % → 1 % | 226.1 px | 0.16 | 0.10 | 18 |
| stroke 144 | 13 % → 2 % | 196.2 px | 0.16 | 0.14 | 15 |
| stroke 145 | 2 % → 3 % | 23.9 px | 0.16 | 1.63 | 11 |
| stroke 146 | 3 % → 3 % | 42.2 px | 0.16 | 0.99 | 12 |
| stroke 147 | 4 % → 2 % | 78.0 px | 0.16 | 0.63 | 6 |
| stroke 148 | 5 % → 2 % | 77.8 px | 0.16 | 0.46 | 9 |
| stroke 149 | 5 % → 0 % | 196.3 px | 0.15 | 0.06 | 4 |
| stroke 150 | 9 % → 0 % | 93.0 px | 0.15 | 0.04 | 22 |
| stroke 151 | 10 % → 0 % | 85.9 px | 0.00 | 0.00 | 44 |
| stroke 152 | 11 % → 0 % | 82.2 px | 0.00 | 0.00 | 86 |
| stroke 153 | 14 % → 0 % | 205.2 px | 0.16 | 0.02 | 12 |
| stroke 154 | 12 % → 0 % | 157.4 px | 0.00 | 0.00 | 29 |
| stroke 155 | 16 % → 0 % | 263.8 px | 0.16 | 0.03 | 17 |
| stroke 156 | 12 % → 0 % | 170.6 px | 0.00 | 0.00 | 21 |
| stroke 157 | 17 % → 0 % | 561.3 px | 0.16 | 0.02 | 8 |
| stroke 158 | 11 % → 0 % | 295.1 px | 0.00 | 0.00 | 31 |
| stroke 159 | 11 % → 0 % | 295.7 px | 0.00 | 0.00 | 11 |
| stroke 160 | 18 % → 1 % | 557.2 px | 0.16 | 0.07 | 9 |
| stroke 161 | 12 % → 0 % | 306.6 px | 0.00 | 0.00 | 10 |
| stroke 162 | 18 % → 1 % | 529.4 px | 0.16 | 0.08 | 19 |
| stroke 163 | 12 % → 0 % | 248.8 px | 0.00 | 0.00 | 12 |
| stroke 164 | 12 % → 0 % | 329.3 px | 0.00 | 0.00 | 13 |
| stroke 165 | 13 % → 0 % | 331.5 px | 0.00 | 0.00 | 5 |
| stroke 166 | 13 % → 0 % | 318.0 px | 0.00 | 0.00 | 6 |
| stroke 167 | 15 % → 0 % | 332.5 px | 0.00 | 0.00 | 7 |
| stroke 168 | 2 % → 0 % | 28.1 px | 0.00 | 0.00 | 18 |
| stroke 169 | 4 % → 0 % | 55.5 px | 0.00 | 0.00 | 14 |
| stroke 170 | 5 % → 0 % | 174.3 px | 0.00 | 0.00 | 7 |
| stroke 171 | 6 % → 0 % | 79.0 px | 0.16 | 0.06 | 19 |
| stroke 172 | 7 % → 1 % | 96.6 px | 0.16 | 0.19 | 19 |
| stroke 173 | 8 % → 3 % | 105.2 px | 0.16 | 0.37 | 19 |
| stroke 174 | 8 % → 4 % | 176.2 px | 0.16 | 0.48 | 15 |
| stroke 175 | 15 % → 2 % | 138.2 px | 0.16 | 0.13 | 48 |
| stroke 176 | 14 % → 0 % | 463.3 px | 0.00 | 0.00 | 7 |
| stroke 177 | 19 % → 4 % | 254.3 px | 0.16 | 0.21 | 19 |
| stroke 178 | 19 % → 2 % | 289.1 px | 0.16 | 0.09 | 25 |
| stroke 179 | 22 % → 0 % | 170.1 px | 0.17 | 0.00 | 67 |
| stroke 180 | 26 % → 0 % | 446.5 px | 0.00 | 0.00 | 16 |
| stroke 181 | 1 % → 3 % | 26.7 px | 0.16 | 3.16 | 8 |
| stroke 182 | 3 % → 3 % | 27.0 px | 0.16 | 1.00 | 17 |
| stroke 183 | 3 % → 3 % | 20.6 px | 0.16 | 1.31 | 35 |
| stroke 184 | 6 % → 6 % | 74.9 px | 0.16 | 1.00 | 20 |
| stroke 185 | 2 % → 2 % | 21.6 px | 0.16 | 1.00 | 19 |

Numbers say: wet paint spreads well beyond the stroke.

## Refs v3 · #46 Ink lips on wet paper — own sheet
own sheet 800 × 1047 · Watercolour 1.00 + water 65 % · 56 px · 24.7 s

![Refs v3 · #46 Ink lips on wet paper — own sheet](Refs-v3-46-Ink-lips-on-wet-paper-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 14 % → 22 % | 61.2 px | 0.59 | 1.54 | 463 |
| stroke 2 | 13 % → 21 % | 59.9 px | 0.60 | 1.57 | 267 |

Numbers say: wet paint spreads well beyond the stroke.

## Refs v3 · #47 Pink knife slabs — own sheet
own sheet 800 × 1014 · Gouache 1.00 + water 15 % · 240 px · 43.0 s

![Refs v3 · #47 Pink knife slabs — own sheet](Refs-v3-47-Pink-knife-slabs-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 26 % → 38 % | 127.5 px | 0.08 | 1.49 | 5522 |
| stroke 2 | 45 % → 40 % | 315.5 px | 0.08 | 0.90 | 6419 |
| stroke 3 | 54 % → 41 % | 481.6 px | 0.08 | 0.76 | 8125 |
| stroke 4 | 64 % → 42 % | 451.0 px | 0.08 | 0.66 | 5693 |
| stroke 5 | 82 % → 41 % | 422.8 px | 0.08 | 0.50 | 3616 |
| stroke 6 | 27 % → 39 % | 239.2 px | 0.08 | 1.43 | 340 |
| stroke 7 | 38 % → 41 % | 441.2 px | 0.08 | 1.09 | 313 |
| stroke 8 | 50 % → 42 % | 591.2 px | 0.08 | 0.83 | 304 |
| stroke 9 | 66 % → 41 % | 589.4 px | 0.08 | 0.62 | 593 |

## Refs v3 · #48 Black bands with drips — own sheet
own sheet 800 × 1045 · Watercolour 1.00 + water 35 % · 112 px · 35.7 s

![Refs v3 · #48 Black bands with drips — own sheet](Refs-v3-48-Black-bands-with-drips-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 13 % → 97 % | 77.7 px | 0.31 | 7.55 | 175 |
| stroke 2 | 16 % → 96 % | 125.6 px | 0.31 | 6.06 | 302 |
| stroke 3 | 34 % → 94 % | 105.5 px | 0.31 | 2.81 | 1422 |
| stroke 4 | 43 % → 95 % | 151.9 px | 0.31 | 2.23 | 1668 |
| stroke 5 | 47 % → 95 % | 229.1 px | 0.30 | 2.04 | 1457 |
| stroke 6 | 51 % → 95 % | 259.0 px | 0.31 | 1.87 | 1507 |
| stroke 7 | 56 % → 96 % | 265.3 px | 0.30 | 1.73 | 1182 |
| stroke 8 | 57 % → 97 % | 271.9 px | 0.30 | 1.70 | 1210 |
| stroke 9 | 58 % → 97 % | 278.5 px | 0.30 | 1.68 | 1235 |
| stroke 10 | 56 % → 97 % | 348.6 px | 0.30 | 1.73 | 898 |
| stroke 11 | 56 % → 98 % | 355.8 px | 0.30 | 1.74 | 827 |
| stroke 12 | 57 % → 97 % | 296.5 px | 0.30 | 1.69 | 920 |
| stroke 13 | 58 % → 93 % | 274.9 px | 0.30 | 1.62 | 1126 |
| stroke 14 | 58 % → 85 % | 274.3 px | 0.29 | 1.48 | 1006 |
| stroke 15 | 56 % → 76 % | 299.1 px | 0.29 | 1.35 | 785 |
| stroke 16 | 58 % → 67 % | 274.9 px | 0.30 | 1.16 | 1064 |
| stroke 17 | 56 % → 59 % | 355.2 px | 0.29 | 1.04 | 809 |
| stroke 18 | 54 % → 55 % | 823.5 px | 0.29 | 1.02 | 130 |

Numbers say: wet paint spreads well beyond the stroke.

## Refs v3 · #49 Magenta letters round — own sheet
own sheet 800 × 1000 · Ink 0.98 · 64 px · 23.3 s

![Refs v3 · #49 Magenta letters round — own sheet](Refs-v3-49-Magenta-letters-round-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 2 % → 31 % | 49.2 px | 0.47 | 14.24 | 15 |
| stroke 2 | 4 % → 28 % | 123.4 px | 0.47 | 7.67 | 17 |
| stroke 3 | 4 % → 22 % | 59.9 px | 0.48 | 5.38 | 17 |
| stroke 4 | 8 % → 26 % | 103.5 px | 0.48 | 3.11 | 18 |
| stroke 5 | 16 % → 29 % | 97.4 px | 0.47 | 1.81 | 131 |
| stroke 6 | 8 % → 27 % | 51.8 px | 0.45 | 3.50 | 63 |
| stroke 7 | 19 % → 33 % | 134.3 px | 0.46 | 1.74 | 46 |
| stroke 8 | 4 % → 38 % | 65.8 px | 0.47 | 8.43 | 37 |
| stroke 9 | 8 % → 39 % | 127.7 px | 0.47 | 4.76 | 37 |
| stroke 10 | 12 % → 29 % | 148.1 px | 0.47 | 2.44 | 41 |
| stroke 11 | 16 % → 34 % | 275.5 px | 0.48 | 2.10 | 22 |
| stroke 12 | 18 % → 32 % | 211.2 px | 0.48 | 1.83 | 81 |
| stroke 13 | 31 % → 37 % | 159.8 px | 0.47 | 1.19 | 156 |
| stroke 14 | 20 % → 29 % | 58.6 px | 0.49 | 1.45 | 514 |
| stroke 15 | 9 % → 37 % | 203.1 px | 0.47 | 3.86 | 22 |
| stroke 16 | 16 % → 37 % | 116.4 px | 0.47 | 2.36 | 118 |
| stroke 17 | 25 % → 37 % | 240.2 px | 0.47 | 1.52 | 181 |
| stroke 18 | 25 % → 39 % | 393.4 px | 0.47 | 1.55 | 52 |
| stroke 19 | 26 % → 39 % | 262.6 px | 0.47 | 1.52 | 106 |
| stroke 20 | 14 % → 37 % | 507.2 px | 0.48 | 2.72 | 13 |
| stroke 21 | 23 % → 40 % | 105.0 px | 0.47 | 1.77 | 325 |
| stroke 22 | 19 % → 40 % | 144.3 px | 0.47 | 2.14 | 91 |
| stroke 23 | 14 % → 43 % | 160.0 px | 0.47 | 3.09 | 52 |
| stroke 24 | 9 % → 44 % | 89.1 px | 0.47 | 4.85 | 76 |
| stroke 25 | 22 % → 32 % | 267.4 px | 0.47 | 1.48 | 53 |
| stroke 26 | 30 % → 35 % | 363.8 px | 0.47 | 1.18 | 191 |
| stroke 27 | 29 % → 34 % | 354.6 px | 0.46 | 1.19 | 52 |
| stroke 28 | 6 % → 48 % | 62.3 px | 0.48 | 7.99 | 43 |
| stroke 29 | 27 % → 38 % | 137.3 px | 0.47 | 1.39 | 205 |
| stroke 30 | 33 % → 41 % | 209.7 px | 0.47 | 1.24 | 107 |
| stroke 31 | 25 % → 38 % | 74.5 px | 0.47 | 1.54 | 342 |
| stroke 32 | 26 % → 42 % | 95.6 px | 0.48 | 1.62 | 243 |
| stroke 33 | 18 % → 40 % | 291.2 px | 0.48 | 2.27 | 42 |
| stroke 34 | 11 % → 40 % | 128.6 px | 0.48 | 3.82 | 63 |
| stroke 35 | 29 % → 37 % | 198.3 px | 0.47 | 1.29 | 93 |
| stroke 36 | 28 % → 36 % | 312.0 px | 0.47 | 1.29 | 50 |
| stroke 37 | 11 % → 32 % | 92.7 px | 0.48 | 2.84 | 49 |
| stroke 38 | 23 % → 38 % | 266.0 px | 0.47 | 1.62 | 55 |
| stroke 39 | 21 % → 32 % | 178.6 px | 0.47 | 1.52 | 43 |
| stroke 40 | 9 % → 24 % | 162.4 px | 0.49 | 2.70 | 20 |
| stroke 41 | 20 % → 32 % | 257.4 px | 0.48 | 1.63 | 26 |
| stroke 42 | 27 % → 31 % | 203.2 px | 0.47 | 1.14 | 133 |
| stroke 43 | 25 % → 27 % | 575.8 px | 0.48 | 1.09 | 16 |
| stroke 44 | 36 % → 38 % | 285.4 px | 0.48 | 1.07 | 49 |

Numbers say: wet paint spreads well beyond the stroke.

## Refs v3 · #50 Swipes on seaside — own sheet
own sheet 800 × 1160 · Gouache 1.00 + water 15 % · 80 px · 42.1 s

![Refs v3 · #50 Swipes on seaside — own sheet](Refs-v3-50-Swipes-on-seaside-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 10 % → 0 % | 75.6 px | 0.00 | 0.00 | 324 |
| stroke 2 | 13 % → 0 % | 184.6 px | 0.00 | 0.00 | 119 |
| stroke 3 | 11 % → 0 % | 74.9 px | 0.00 | 0.00 | 212 |
| stroke 4 | 21 % → 0 % | 281.7 px | 0.00 | 0.00 | 98 |
| stroke 5 | 8 % → 0 % | 112.0 px | 0.00 | 0.00 | 114 |
| stroke 6 | 15 % → 0 % | 116.3 px | 0.00 | 0.00 | 332 |
| stroke 7 | 27 % → 0 % | 121.6 px | 0.00 | 0.00 | 1177 |
| stroke 8 | 39 % → 0 % | 341.6 px | 0.00 | 0.00 | 205 |
| stroke 9 | 35 % → 0 % | 176.8 px | 0.00 | 0.00 | 611 |
| stroke 10 | 46 % → 4 % | 269.9 px | 0.43 | 0.08 | 445 |
| stroke 11 | 39 % → 3 % | 306.5 px | 0.44 | 0.07 | 221 |
| stroke 12 | 48 % → 11 % | 264.1 px | 0.43 | 0.23 | 338 |
| stroke 13 | 45 % → 13 % | 285.4 px | 0.43 | 0.28 | 245 |
| stroke 14 | 50 % → 20 % | 259.4 px | 0.44 | 0.41 | 375 |
| stroke 15 | 51 % → 23 % | 290.0 px | 0.43 | 0.45 | 311 |
| stroke 16 | 52 % → 32 % | 244.3 px | 0.43 | 0.62 | 617 |
| stroke 17 | 50 % → 31 % | 453.0 px | 0.43 | 0.62 | 114 |
| stroke 18 | 50 % → 44 % | 342.2 px | 0.43 | 0.87 | 305 |
| stroke 19 | 48 % → 42 % | 400.6 px | 0.44 | 0.87 | 154 |
| stroke 20 | 17 % → 70 % | 372.8 px | 0.43 | 4.04 | 53 |
| stroke 21 | 1 % → 75 % | 26.4 px | 0.43 | 67.27 | 18 |
| stroke 22 | 10 % → 0 % | 67.4 px | 0.00 | 0.00 | 311 |
| stroke 23 | 6 % → 0 % | 109.5 px | 0.00 | 0.00 | 44 |
| stroke 24 | 20 % → 0 % | 91.8 px | 0.00 | 0.00 | 446 |
| stroke 25 | 26 % → 0 % | 217.9 px | 0.00 | 0.00 | 125 |
| stroke 26 | 29 % → 0 % | 187.0 px | 0.00 | 0.00 | 312 |
| stroke 27 | 24 % → 0 % | 207.3 px | 0.00 | 0.00 | 141 |
| stroke 28 | 39 % → 0 % | 154.7 px | 0.00 | 0.00 | 697 |
| stroke 29 | 39 % → 0 % | 915.5 px | 0.00 | 0.00 | 49 |
| stroke 30 | 50 % → 0 % | 844.6 px | 0.00 | 0.00 | 61 |
| stroke 31 | 34 % → 0 % | 571.4 px | 0.00 | 0.00 | 36 |
| stroke 32 | 38 % → 0 % | 357.8 px | 0.00 | 0.00 | 88 |
| stroke 33 | 40 % → 0 % | 438.3 px | 0.00 | 0.00 | 143 |
| stroke 34 | 7 % → 35 % | 81.4 px | 0.43 | 4.87 | 99 |
| stroke 35 | 9 % → 49 % | 168.4 px | 0.44 | 5.47 | 46 |
| stroke 36 | 11 % → 56 % | 281.3 px | 0.44 | 4.99 | 33 |
| stroke 37 | 3 % → 77 % | 76.5 px | 0.43 | 24.83 | 39 |
| stroke 38 | 1 % → 0 % | 24.4 px | 0.00 | 0.00 | 14 |
| stroke 39 | 1 % → 1 % | 24.2 px | 0.41 | 1.39 | 5 |
| stroke 40 | 8 % → 0 % | 39.7 px | 0.00 | 0.00 | 78 |
| stroke 41 | 11 % → 0 % | 60.2 px | 0.00 | 0.00 | 94 |
| stroke 42 | 4 % → 0 % | 41.1 px | 0.00 | 0.00 | 41 |
| stroke 43 | 5 % → 0 % | 183.5 px | 0.00 | 0.00 | 11 |
| stroke 44 | 8 % → 0 % | 57.4 px | 0.00 | 0.00 | 80 |
| stroke 45 | 9 % → 0 % | 136.3 px | 0.00 | 0.00 | 40 |
| stroke 46 | 2 % → 0 % | 41.4 px | 0.00 | 0.00 | 22 |
| stroke 47 | 12 % → 0 % | 66.0 px | 0.00 | 0.00 | 246 |
| stroke 48 | 20 % → 0 % | 107.5 px | 0.00 | 0.00 | 171 |
| stroke 49 | 4 % → 3 % | 40.3 px | 0.44 | 0.62 | 95 |
| stroke 50 | 7 % → 7 % | 55.9 px | 0.43 | 0.94 | 146 |
| stroke 51 | 10 % → 12 % | 94.6 px | 0.42 | 1.22 | 68 |
| stroke 52 | 13 % → 16 % | 167.3 px | 0.43 | 1.28 | 54 |
| stroke 53 | 5 % → 76 % | 40.1 px | 0.44 | 15.59 | 71 |
| stroke 54 | 7 % → 77 % | 69.1 px | 0.44 | 10.99 | 68 |
| stroke 55 | 10 % → 81 % | 137.1 px | 0.44 | 7.86 | 105 |
| stroke 56 | 13 % → 77 % | 426.8 px | 0.44 | 5.89 | 19 |
| stroke 57 | 5 % → 0 % | 46.7 px | 0.00 | 0.00 | 48 |
| stroke 58 | 7 % → 0 % | 76.2 px | 0.00 | 0.00 | 42 |
| stroke 59 | 2 % → 0 % | 50.2 px | 0.00 | 0.00 | 27 |
| stroke 60 | 4 % → 0 % | 95.9 px | 0.00 | 0.00 | 19 |
| stroke 61 | 5 % → 0 % | 100.6 px | 0.00 | 0.00 | 35 |
| stroke 62 | 7 % → 0 % | 77.1 px | 0.00 | 0.00 | 62 |
| stroke 63 | 10 % → 0 % | 203.7 px | 0.00 | 0.00 | 44 |
| stroke 64 | 5 % → 0 % | 64.4 px | 0.00 | 0.00 | 38 |
| stroke 65 | 9 % → 0 % | 63.5 px | 0.00 | 0.00 | 112 |
| stroke 66 | 12 % → 0 % | 78.7 px | 0.00 | 0.00 | 130 |
| stroke 67 | 13 % → 0 % | 220.8 px | 0.00 | 0.00 | 36 |
| stroke 68 | 5 % → 37 % | 47.2 px | 0.43 | 8.14 | 66 |
| stroke 69 | 5 % → 79 % | 45.8 px | 0.43 | 16.01 | 53 |
| stroke 70 | 8 % → 75 % | 107.8 px | 0.43 | 9.54 | 21 |
| stroke 71 | 5 % → 47 % | 80.5 px | 0.43 | 9.76 | 70 |
| stroke 72 | 10 % → 52 % | 106.1 px | 0.43 | 5.45 | 119 |
| stroke 73 | 6 % → 44 % | 91.3 px | 0.44 | 8.01 | 41 |
| stroke 74 | 18 % → 59 % | 121.8 px | 0.44 | 3.35 | 271 |
| stroke 75 | 25 % → 56 % | 165.4 px | 0.44 | 2.30 | 172 |
| stroke 76 | 31 % → 65 % | 117.3 px | 0.44 | 2.07 | 538 |
| stroke 77 | 31 % → 70 % | 455.1 px | 0.43 | 2.24 | 49 |
| stroke 78 | 43 % → 77 % | 202.6 px | 0.43 | 1.78 | 435 |
| stroke 79 | 37 % → 75 % | 361.9 px | 0.43 | 2.06 | 82 |
| stroke 80 | 50 % → 82 % | 331.3 px | 0.43 | 1.62 | 292 |
| stroke 81 | 44 % → 75 % | 583.9 px | 0.43 | 1.70 | 56 |
| stroke 82 | 57 % → 79 % | 243.6 px | 0.43 | 1.39 | 360 |
| stroke 83 | 50 % → 76 % | 459.2 px | 0.44 | 1.53 | 69 |
| stroke 84 | 68 % → 79 % | 287.6 px | 0.43 | 1.17 | 230 |
| stroke 85 | 62 % → 73 % | 310.2 px | 0.44 | 1.18 | 165 |
| stroke 86 | 76 % → 76 % | 268.9 px | 0.43 | 1.00 | 205 |
| stroke 87 | 71 % → 71 % | 293.7 px | 0.44 | 1.00 | 155 |

Numbers say: wet paint spreads well beyond the stroke.

