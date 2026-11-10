![All brushes](contact.png)

# Brush Lab — 100 brushes · 10 Nov 2026 at 05:26

Every sheet: 1500 × 600, ten strokes in a 5 × 2 grid — 1. light line · 2. heavy line · 3. pressure swell · 4. fast wave · 5. slow wave · 6. spiral · 7. loop · 8. tilted · 9. over the wet one · 10. long, no reload (cell 8 holds «tilted» and «over the wet one» crossed). The CPU reference of Mamay's paint engine; the wet layer settles 20 s at the end.

Columns: **covered** = share of the cell with paint right after the stroke → after settling; **width** = painted area of the stroke ÷ its length (px); **dark** = mean darkness of the painted pixels above the paper's own grain (0 = paper, 1 = black); **spread** = how far wet paint went beyond the stroke (1.0 = stayed); **ms** = the stroke on the CPU; long stroke: paint in each quarter of its length (it should run out: wet → streaks → dry tail).

## Refs v3 · #01 HW peach cloud
Gouache 1.00 + turpentine 30 % · 104 px · 666.0 s

![Refs v3 · #01 HW peach cloud](Refs-v3-01-HW-peach-cloud.png)

A light paint: laid on a grey sheet (on white it cannot be seen); **dark** = how far it is from the grey either way.

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 31 % → 30 % | 89.5 px | 0.33 | 0.97 | 4091 |
| heavy line | 32 % → 30 % | 93.7 px | 0.32 | 0.92 | 5049 |
| pressure swell | 25 % → 25 % | 92.3 px | 0.31 | 1.00 | 3417 |
| fast wave | 68 % → 42 % | 78.5 px | 0.27 | 0.61 | 23436 |
| slow wave | 67 % → 41 % | 77.8 px | 0.30 | 0.61 | 14284 |
| spiral | 80 % → 41 % | 52.8 px | 0.29 | 0.51 | 28905 |
| loop | 61 % → 48 % | 78.4 px | 0.29 | 0.80 | 13197 |
| tilted | 25 % → 25 % | 69.2 px | 0.28 | 1.00 | 9683 |
| over the wet one | 51 % → 48 % | 74.0 px | 0.28 | 0.93 | 5048 |
| long, no reload | 97 % → 42 % | 43.4 px | 0.29 | 0.43 | 39177 | quarters: 0.00 → 0.00 → 0.00 → 0.00

Numbers say: light vs heavy: width 89.5 → 93.7 px, dark 0.33 → 0.32; pressure barely changes the width; the long stroke does not run out of paint.

## Refs v3 · #02 HW cream strokes
Gouache 1.00 + turpentine 30 % · 51 px · 404.1 s

![Refs v3 · #02 HW cream strokes](Refs-v3-02-HW-cream-strokes.png)

A light paint: laid on a grey sheet (on white it cannot be seen); **dark** = how far it is from the grey either way.

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 16 % → 15 % | 45.4 px | 0.37 | 0.95 | 1787 |
| heavy line | 17 % → 16 % | 48.6 px | 0.35 | 0.96 | 2146 |
| pressure swell | 13 % → 12 % | 46.9 px | 0.35 | 0.98 | 1622 |
| fast wave | 41 % → 19 % | 47.5 px | 0.31 | 0.46 | 4193 |
| slow wave | 39 % → 24 % | 45.4 px | 0.34 | 0.60 | 7951 |
| spiral | 62 % → 25 % | 40.7 px | 0.32 | 0.40 | 12264 |
| loop | 34 % → 22 % | 43.6 px | 0.34 | 0.65 | 6584 |
| tilted | 14 % → 14 % | 40.1 px | 0.34 | 1.00 | 2683 |
| over the wet one | 29 % → 26 % | 42.2 px | 0.34 | 0.89 | 2238 |
| long, no reload | 75 % → 24 % | 33.8 px | 0.33 | 0.31 | 15392 | quarters: 0.01 → 0.01 → 0.01 → 0.01

Numbers say: light vs heavy: width 45.4 → 48.6 px, dark 0.37 → 0.35; pressure barely changes the width; the long stroke does not run out of paint.

## Refs v3 · #03 HW navy contours
Gouache 1.00 + turpentine 30 % · 80 px · 575.3 s

![Refs v3 · #03 HW navy contours](Refs-v3-03-HW-navy-contours.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 24 % → 24 % | 70.3 px | 0.26 | 0.98 | 2844 |
| heavy line | 26 % → 24 % | 74.6 px | 0.27 | 0.92 | 4008 |
| pressure swell | 19 % → 18 % | 71.9 px | 0.30 | 0.96 | 2764 |
| fast wave | 58 % → 31 % | 66.4 px | 0.33 | 0.53 | 16174 |
| slow wave | 57 % → 33 % | 65.4 px | 0.29 | 0.58 | 13944 |
| spiral | 74 % → 35 % | 48.5 px | 0.31 | 0.47 | 21767 |
| loop | 51 % → 37 % | 65.6 px | 0.29 | 0.72 | 9098 |
| tilted | 20 % → 20 % | 55.0 px | 0.30 | 1.00 | 4535 |
| over the wet one | 42 % → 37 % | 60.9 px | 0.30 | 0.90 | 4448 |
| long, no reload | 93 % → 34 % | 41.5 px | 0.31 | 0.36 | 23554 | quarters: 0.29 → 0.26 → 0.17 → 0.06

Numbers say: light vs heavy: width 70.3 → 74.6 px, dark 0.26 → 0.27; pressure barely changes the width.

## Refs v3 · #04 HW grey cloud
Gouache 1.00 + turpentine 30 % · 93 px · 619.5 s

![Refs v3 · #04 HW grey cloud](Refs-v3-04-HW-grey-cloud.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 28 % → 27 % | 80.5 px | 0.13 | 0.96 | 3540 |
| heavy line | 29 % → 27 % | 85.0 px | 0.14 | 0.92 | 4582 |
| pressure swell | 22 % → 22 % | 82.2 px | 0.16 | 0.99 | 3254 |
| fast wave | 64 % → 38 % | 73.7 px | 0.19 | 0.60 | 19277 |
| slow wave | 62 % → 37 % | 72.1 px | 0.15 | 0.60 | 13226 |
| spiral | 77 % → 39 % | 50.5 px | 0.19 | 0.51 | 23910 |
| loop | 56 % → 43 % | 73.0 px | 0.13 | 0.77 | 10786 |
| tilted | 22 % → 22 % | 61.8 px | 0.19 | 1.00 | 6979 |
| over the wet one | 47 % → 43 % | 68.4 px | 0.19 | 0.93 | 5001 |
| long, no reload | 95 % → 41 % | 42.7 px | 0.16 | 0.43 | 24293 | quarters: 0.17 → 0.13 → 0.07 → 0.02

Numbers say: light vs heavy: width 80.5 → 85.0 px, dark 0.13 → 0.14; pressure barely changes the width.

## Refs v3 · #05 HW green in rust loops
Gouache 1.00 + turpentine 30 % · 104 px · 662.2 s

![Refs v3 · #05 HW green in rust loops](Refs-v3-05-HW-green-in-rust-loops.png)

A light paint: laid on a grey sheet (on white it cannot be seen); **dark** = how far it is from the grey either way.

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 31 % → 30 % | 89.5 px | 0.37 | 0.97 | 4396 |
| heavy line | 32 % → 30 % | 93.7 px | 0.36 | 0.92 | 5577 |
| pressure swell | 25 % → 25 % | 92.3 px | 0.34 | 1.00 | 3378 |
| fast wave | 68 % → 42 % | 78.5 px | 0.31 | 0.61 | 22893 |
| slow wave | 67 % → 41 % | 77.8 px | 0.34 | 0.61 | 14451 |
| spiral | 80 % → 41 % | 52.8 px | 0.32 | 0.51 | 29051 |
| loop | 61 % → 48 % | 78.4 px | 0.33 | 0.80 | 13157 |
| tilted | 25 % → 25 % | 69.2 px | 0.32 | 1.00 | 9663 |
| over the wet one | 51 % → 48 % | 74.0 px | 0.32 | 0.93 | 5159 |
| long, no reload | 97 % → 42 % | 43.4 px | 0.33 | 0.43 | 39278 | quarters: 0.00 → 0.00 → 0.00 → 0.00

Numbers say: light vs heavy: width 89.5 → 93.7 px, dark 0.37 → 0.36; pressure barely changes the width; the long stroke does not run out of paint.

## Refs v3 · #06 HW scrubbed grey
Gouache 1.00 + turpentine 30 % · 93 px · 617.9 s

![Refs v3 · #06 HW scrubbed grey](Refs-v3-06-HW-scrubbed-grey.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 28 % → 27 % | 80.5 px | 0.13 | 0.96 | 3279 |
| heavy line | 29 % → 27 % | 85.0 px | 0.14 | 0.92 | 4626 |
| pressure swell | 22 % → 22 % | 82.2 px | 0.16 | 0.99 | 3346 |
| fast wave | 64 % → 38 % | 73.7 px | 0.19 | 0.60 | 19274 |
| slow wave | 62 % → 37 % | 72.1 px | 0.15 | 0.60 | 13469 |
| spiral | 77 % → 39 % | 50.5 px | 0.19 | 0.51 | 24450 |
| loop | 56 % → 43 % | 73.0 px | 0.13 | 0.77 | 11270 |
| tilted | 22 % → 22 % | 61.8 px | 0.19 | 1.00 | 6759 |
| over the wet one | 47 % → 43 % | 68.4 px | 0.19 | 0.93 | 4911 |
| long, no reload | 95 % → 41 % | 42.7 px | 0.16 | 0.43 | 23829 | quarters: 0.17 → 0.13 → 0.07 → 0.02

Numbers say: light vs heavy: width 80.5 → 85.0 px, dark 0.13 → 0.14; pressure barely changes the width.

## Refs v3 · #07 HW blue L and zigzag
Gouache 1.00 + turpentine 30 % · 104 px · 662.3 s

![Refs v3 · #07 HW blue L and zigzag](Refs-v3-07-HW-blue-L-and-zigzag.png)

A light paint: laid on a grey sheet (on white it cannot be seen); **dark** = how far it is from the grey either way.

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 31 % → 30 % | 89.5 px | 0.40 | 0.97 | 4240 |
| heavy line | 32 % → 30 % | 93.7 px | 0.40 | 0.92 | 5620 |
| pressure swell | 25 % → 25 % | 92.3 px | 0.38 | 1.00 | 3364 |
| fast wave | 68 % → 42 % | 78.5 px | 0.35 | 0.61 | 23478 |
| slow wave | 67 % → 41 % | 77.8 px | 0.38 | 0.61 | 14839 |
| spiral | 80 % → 41 % | 52.8 px | 0.37 | 0.51 | 30305 |
| loop | 61 % → 48 % | 78.4 px | 0.37 | 0.80 | 13030 |
| tilted | 25 % → 25 % | 69.2 px | 0.36 | 1.00 | 9766 |
| over the wet one | 51 % → 48 % | 74.0 px | 0.36 | 0.93 | 5064 |
| long, no reload | 97 % → 42 % | 43.4 px | 0.37 | 0.43 | 39518 | quarters: 0.00 → 0.00 → 0.00 → 0.00

Numbers say: light vs heavy: width 89.5 → 93.7 px, dark 0.40 → 0.40; pressure barely changes the width; the long stroke does not run out of paint.

## Refs v3 · #08 HW lilac crown basket
Gouache 1.00 + turpentine 30 % · 36 px · 317.7 s

![Refs v3 · #08 HW lilac crown basket](Refs-v3-08-HW-lilac-crown-basket.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 11 % → 10 % | 33.0 px | 0.14 | 0.91 | 1518 |
| heavy line | 12 % → 12 % | 34.4 px | 0.13 | 0.98 | 1199 |
| pressure swell | 9 % → 9 % | 33.6 px | 0.17 | 1.01 | 875 |
| fast wave | 30 % → 14 % | 34.8 px | 0.19 | 0.46 | 3314 |
| slow wave | 29 % → 17 % | 33.6 px | 0.16 | 0.57 | 2950 |
| spiral | 49 % → 16 % | 32.5 px | 0.18 | 0.33 | 6755 |
| loop | 25 % → 16 % | 32.8 px | 0.14 | 0.64 | 3216 |
| tilted | 12 % → 12 % | 32.5 px | 0.18 | 1.00 | 1825 |
| over the wet one | 23 % → 20 % | 31.7 px | 0.18 | 0.88 | 2026 |
| long, no reload | 59 % → 18 % | 26.4 px | 0.16 | 0.30 | 7174 | quarters: 0.11 → 0.06 → 0.02 → 0.00

Numbers say: light vs heavy: width 33.0 → 34.4 px, dark 0.14 → 0.13; pressure barely changes the width.

## Refs v3 · #09 HW white loops
Gouache 1.00 + turpentine 30 % · 104 px · 650.6 s

![Refs v3 · #09 HW white loops](Refs-v3-09-HW-white-loops.png)

A light paint: laid on a grey sheet (on white it cannot be seen); **dark** = how far it is from the grey either way.

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 31 % → 30 % | 89.5 px | 0.40 | 0.97 | 4128 |
| heavy line | 32 % → 30 % | 93.7 px | 0.40 | 0.92 | 5398 |
| pressure swell | 25 % → 25 % | 92.3 px | 0.38 | 1.00 | 3399 |
| fast wave | 68 % → 41 % | 78.5 px | 0.35 | 0.61 | 22613 |
| slow wave | 67 % → 41 % | 77.6 px | 0.38 | 0.61 | 14770 |
| spiral | 80 % → 41 % | 52.8 px | 0.36 | 0.51 | 26724 |
| loop | 61 % → 48 % | 78.4 px | 0.37 | 0.80 | 13100 |
| tilted | 25 % → 25 % | 69.2 px | 0.36 | 1.00 | 6897 |
| over the wet one | 51 % → 48 % | 74.0 px | 0.36 | 0.93 | 5572 |
| long, no reload | 97 % → 40 % | 43.4 px | 0.36 | 0.42 | 31471 | quarters: 0.00 → 0.00 → 0.00 → 0.01

Numbers say: light vs heavy: width 89.5 → 93.7 px, dark 0.40 → 0.40; pressure barely changes the width; the long stroke does not run out of paint.

## Refs v3 · #10 HW maroon loops
Gouache 1.00 + turpentine 30 % · 104 px · 624.0 s

![Refs v3 · #10 HW maroon loops](Refs-v3-10-HW-maroon-loops.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 31 % → 30 % | 89.5 px | 0.24 | 0.97 | 4641 |
| heavy line | 32 % → 30 % | 93.7 px | 0.25 | 0.92 | 5805 |
| pressure swell | 25 % → 25 % | 92.3 px | 0.26 | 1.00 | 4310 |
| fast wave | 68 % → 42 % | 78.5 px | 0.29 | 0.61 | 22350 |
| slow wave | 67 % → 41 % | 77.8 px | 0.27 | 0.61 | 14424 |
| spiral | 80 % → 41 % | 52.8 px | 0.28 | 0.51 | 27476 |
| loop | 61 % → 48 % | 78.4 px | 0.27 | 0.80 | 15933 |
| tilted | 25 % → 25 % | 69.2 px | 0.28 | 1.00 | 7058 |
| over the wet one | 51 % → 48 % | 74.0 px | 0.28 | 0.93 | 6121 |
| long, no reload | 97 % → 42 % | 43.4 px | 0.27 | 0.43 | 33462 | quarters: 0.26 → 0.25 → 0.16 → 0.08

Numbers say: light vs heavy: width 89.5 → 93.7 px, dark 0.24 → 0.25; pressure barely changes the width.

## Refs v3 · #11 HW purple balls
Gouache 1.00 + turpentine 30 % · 104 px · 629.2 s

![Refs v3 · #11 HW purple balls](Refs-v3-11-HW-purple-balls.png)

A light paint: laid on a grey sheet (on white it cannot be seen); **dark** = how far it is from the grey either way.

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 31 % → 30 % | 89.5 px | 0.32 | 0.97 | 3133 |
| heavy line | 32 % → 30 % | 93.7 px | 0.31 | 0.92 | 8275 |
| pressure swell | 25 % → 25 % | 92.3 px | 0.29 | 1.00 | 2783 |
| fast wave | 68 % → 42 % | 78.5 px | 0.26 | 0.61 | 43087 |
| slow wave | 67 % → 41 % | 77.8 px | 0.29 | 0.61 | 25614 |
| spiral | 80 % → 41 % | 52.8 px | 0.27 | 0.51 | 22384 |
| loop | 61 % → 48 % | 78.4 px | 0.28 | 0.80 | 12399 |
| tilted | 25 % → 25 % | 69.2 px | 0.27 | 1.00 | 6993 |
| over the wet one | 51 % → 48 % | 74.0 px | 0.27 | 0.93 | 5362 |
| long, no reload | 97 % → 42 % | 43.4 px | 0.28 | 0.43 | 29041 | quarters: 0.00 → 0.00 → 0.00 → 0.00

Numbers say: light vs heavy: width 89.5 → 93.7 px, dark 0.32 → 0.31; pressure barely changes the width; the long stroke does not run out of paint.

## Refs v3 · #12 HW black-olive cage
Gouache 1.00 + turpentine 30 % · 36 px · 307.7 s

![Refs v3 · #12 HW black-olive cage](Refs-v3-12-HW-black-olive-cage.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 11 % → 10 % | 33.0 px | 0.14 | 0.91 | 650 |
| heavy line | 12 % → 12 % | 34.4 px | 0.13 | 0.98 | 1464 |
| pressure swell | 9 % → 9 % | 33.6 px | 0.17 | 1.01 | 868 |
| fast wave | 30 % → 14 % | 34.8 px | 0.19 | 0.46 | 2448 |
| slow wave | 29 % → 17 % | 33.6 px | 0.16 | 0.57 | 3087 |
| spiral | 49 % → 16 % | 32.5 px | 0.18 | 0.33 | 5144 |
| loop | 25 % → 16 % | 32.8 px | 0.14 | 0.64 | 2000 |
| tilted | 12 % → 12 % | 32.5 px | 0.18 | 1.00 | 1134 |
| over the wet one | 23 % → 20 % | 31.7 px | 0.18 | 0.88 | 918 |
| long, no reload | 59 % → 18 % | 26.4 px | 0.16 | 0.30 | 6753 | quarters: 0.11 → 0.06 → 0.02 → 0.00

Numbers say: light vs heavy: width 33.0 → 34.4 px, dark 0.14 → 0.13; pressure barely changes the width.

## Refs v3 · #13 HW blue streaky form
Gouache 1.00 + turpentine 30 % · 104 px · 572.2 s

![Refs v3 · #13 HW blue streaky form](Refs-v3-13-HW-blue-streaky-form.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 31 % → 30 % | 89.5 px | 0.16 | 0.97 | 2513 |
| heavy line | 32 % → 30 % | 93.7 px | 0.16 | 0.92 | 3493 |
| pressure swell | 25 % → 25 % | 92.3 px | 0.17 | 1.00 | 2560 |
| fast wave | 68 % → 42 % | 78.5 px | 0.21 | 0.61 | 12890 |
| slow wave | 67 % → 41 % | 77.8 px | 0.18 | 0.61 | 13662 |
| spiral | 80 % → 41 % | 52.8 px | 0.20 | 0.51 | 32821 |
| loop | 61 % → 48 % | 78.4 px | 0.19 | 0.80 | 10783 |
| tilted | 25 % → 25 % | 69.2 px | 0.20 | 1.00 | 6547 |
| over the wet one | 51 % → 48 % | 74.0 px | 0.20 | 0.93 | 5959 |
| long, no reload | 97 % → 42 % | 43.4 px | 0.18 | 0.43 | 48748 | quarters: 0.18 → 0.15 → 0.08 → 0.03

Numbers say: light vs heavy: width 89.5 → 93.7 px, dark 0.16 → 0.16; pressure barely changes the width.

## Refs v3 · #14 HW olive totem
Gouache 1.00 + turpentine 30 % · 57 px · 404.0 s

![Refs v3 · #14 HW olive totem](Refs-v3-14-HW-olive-totem.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 17 % → 16 % | 50.7 px | 0.26 | 0.94 | 1101 |
| heavy line | 18 % → 18 % | 53.7 px | 0.28 | 0.95 | 1447 |
| pressure swell | 14 % → 13 % | 52.2 px | 0.30 | 0.94 | 1148 |
| fast wave | 44 % → 22 % | 51.3 px | 0.33 | 0.50 | 5261 |
| slow wave | 43 % → 26 % | 49.9 px | 0.30 | 0.61 | 5471 |
| spiral | 65 % → 29 % | 42.9 px | 0.33 | 0.44 | 10381 |
| loop | 37 % → 23 % | 47.7 px | 0.28 | 0.62 | 12403 |
| tilted | 16 % → 16 % | 43.4 px | 0.33 | 1.00 | 3150 |
| over the wet one | 32 % → 29 % | 46.3 px | 0.33 | 0.91 | 2700 |
| long, no reload | 81 % → 26 % | 36.3 px | 0.29 | 0.32 | 11448 | quarters: 0.25 → 0.21 → 0.10 → 0.04

Numbers say: light vs heavy: width 50.7 → 53.7 px, dark 0.26 → 0.28; pressure barely changes the width.

## Refs v3 · #15 Ultramarine script
Ink 0.98 · 39 px · 278.2 s

![Refs v3 · #15 Ultramarine script](Refs-v3-15-Ultramarine-script.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 4 % → 5 % | 11.1 px | 0.62 | 1.39 | 186 |
| heavy line | 14 % → 14 % | 41.0 px | 0.71 | 1.00 | 1632 |
| pressure swell | 8 % → 8 % | 28.2 px | 0.72 | 1.05 | 771 |
| fast wave | 27 % → 27 % | 31.4 px | 0.74 | 1.01 | 3422 |
| slow wave | 24 % → 25 % | 27.6 px | 0.70 | 1.04 | 1337 |
| spiral | 39 % → 40 % | 25.8 px | 0.67 | 1.01 | 7277 |
| loop | 21 % → 21 % | 27.2 px | 0.70 | 1.02 | 2356 |
| tilted | 14 % → 14 % | 39.4 px | 0.74 | 1.00 | 1296 |
| over the wet one | 24 % → 24 % | 27.0 px | 0.74 | 1.00 | 888 |
| long, no reload | 57 % → 57 % | 25.7 px | 0.66 | 1.00 | 9179 | quarters: 0.44 → 0.44 → 0.42 → 0.38

Numbers say: light vs heavy: width 11.1 → 41.0 px, dark 0.62 → 0.71; the long stroke does not run out of paint.

## Refs v3 · #16 Shrigley strokes
Watercolour 1.00 + water 30 % · 64 px · 334.9 s

![Refs v3 · #16 Shrigley strokes](Refs-v3-16-Shrigley-strokes.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 8 % → 11 % | 23.4 px | 0.25 | 1.37 | 463 |
| heavy line | 17 % → 16 % | 49.5 px | 0.21 | 0.96 | 1915 |
| pressure swell | 10 % → 10 % | 37.9 px | 0.28 | 1.00 | 1176 |
| fast wave | 37 % → 35 % | 42.4 px | 0.21 | 0.96 | 7473 |
| slow wave | 34 % → 33 % | 39.0 px | 0.17 | 0.97 | 7827 |
| spiral | 57 % → 54 % | 37.5 px | 0.11 | 0.94 | 5609 |
| loop | 29 % → 29 % | 37.6 px | 0.18 | 0.98 | 4827 |
| tilted | 18 % → 18 % | 51.2 px | 0.19 | 1.00 | 1901 |
| over the wet one | 31 % → 30 % | 34.8 px | 0.19 | 0.96 | 1548 |
| long, no reload | 71 % → 64 % | 32.0 px | 0.12 | 0.90 | 10279 | quarters: 0.16 → 0.08 → 0.06 → 0.04

Numbers say: light vs heavy: width 23.4 → 49.5 px, dark 0.25 → 0.21.

## Refs v3 · #17 Krovostok dry brush
Ink 0.93 · Gouache 0.07 · 16 px · 274.5 s

![Refs v3 · #17 Krovostok dry brush](Refs-v3-17-Krovostok-dry-brush.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 5 % → 7 % | 15.4 px | 0.25 | 1.30 | 219 |
| heavy line | 6 % → 7 % | 18.1 px | 0.26 | 1.18 | 542 |
| pressure swell | 4 % → 5 % | 16.8 px | 0.29 | 1.11 | 419 |
| fast wave | 16 % → 17 % | 18.5 px | 0.31 | 1.05 | 972 |
| slow wave | 14 % → 16 % | 16.2 px | 0.25 | 1.13 | 3095 |
| spiral | 22 % → 23 % | 14.5 px | 0.24 | 1.03 | 2322 |
| loop | 13 % → 14 % | 17.0 px | 0.27 | 1.09 | 1091 |
| tilted | 7 % → 7 % | 20.8 px | 0.30 | 1.00 | 905 |
| over the wet one | 13 % → 15 % | 16.3 px | 0.30 | 1.11 | 722 |
| long, no reload | 30 % → 30 % | 13.3 px | 0.20 | 1.01 | 2248 | quarters: 0.10 → 0.08 → 0.06 → 0.04

Numbers say: light vs heavy: width 15.4 → 18.1 px, dark 0.25 → 0.26.

## Refs v3 · #18 Twombly blue sticks
Wax 1.00 · 19 px · 85.5 s

![Refs v3 · #18 Twombly blue sticks](Refs-v3-18-Twombly-blue-sticks.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 3 % → 3 % | 10.1 px | 0.20 | 1.00 | 345 |
| heavy line | 6 % → 6 % | 16.1 px | 0.21 | 1.00 | 343 |
| pressure swell | 4 % → 4 % | 14.7 px | 0.21 | 1.00 | 192 |
| fast wave | 13 % → 13 % | 14.9 px | 0.21 | 1.00 | 581 |
| slow wave | 12 % → 12 % | 14.1 px | 0.21 | 1.00 | 583 |
| spiral | 19 % → 19 % | 12.8 px | 0.21 | 1.00 | 1832 |
| loop | 10 % → 10 % | 13.0 px | 0.21 | 1.00 | 1007 |
| tilted | 4 % → 4 % | 10.1 px | 0.20 | 1.00 | 1295 |
| over the wet one | 8 % → 8 % | 13.5 px | 0.20 | 1.00 | 973 |
| long, no reload | 25 % → 25 % | 11.2 px | 0.21 | 1.00 | 6161 | quarters: 0.06 → 0.06 → 0.06 → 0.06

Numbers say: light vs heavy: width 10.1 → 16.1 px, dark 0.20 → 0.21; the long stroke does not run out of paint.

## Refs v3 · #19 Guston charcoal hand
Charcoal 1.00 · 39 px · 86.6 s

![Refs v3 · #19 Guston charcoal hand](Refs-v3-19-Guston-charcoal-hand.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 6 % → 6 % | 17.4 px | 0.62 | 1.00 | 455 |
| heavy line | 11 % → 11 % | 31.8 px | 0.62 | 1.00 | 815 |
| pressure swell | 8 % → 8 % | 29.2 px | 0.62 | 1.00 | 554 |
| fast wave | 25 % → 25 % | 29.2 px | 0.62 | 1.00 | 1599 |
| slow wave | 24 % → 24 % | 27.2 px | 0.62 | 1.00 | 1119 |
| spiral | 37 % → 37 % | 24.4 px | 0.62 | 1.00 | 2713 |
| loop | 19 % → 19 % | 24.4 px | 0.62 | 1.00 | 1559 |
| tilted | 7 % → 7 % | 18.2 px | 0.62 | 1.00 | 800 |
| over the wet one | 16 % → 16 % | 25.9 px | 0.62 | 1.00 | 569 |
| long, no reload | 46 % → 46 % | 20.4 px | 0.62 | 1.00 | 4874 | quarters: 0.31 → 0.31 → 0.31 → 0.31

Numbers say: light vs heavy: width 17.4 → 31.8 px, dark 0.62 → 0.62; the long stroke does not run out of paint.

## Refs v3 · #20 Orange crayon
Wax 1.00 · 48 px · 76.5 s

![Refs v3 · #20 Orange crayon](Refs-v3-20-Orange-crayon.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 8 % → 8 % | 23.9 px | 0.52 | 1.00 | 612 |
| heavy line | 14 % → 14 % | 39.7 px | 0.52 | 1.00 | 902 |
| pressure swell | 10 % → 10 % | 36.2 px | 0.52 | 1.00 | 1061 |
| fast wave | 30 % → 30 % | 35.0 px | 0.52 | 1.00 | 2778 |
| slow wave | 29 % → 29 % | 33.3 px | 0.52 | 1.00 | 3818 |
| spiral | 47 % → 47 % | 30.7 px | 0.52 | 1.00 | 7355 |
| loop | 23 % → 23 % | 29.9 px | 0.52 | 1.00 | 2145 |
| tilted | 7 % → 7 % | 18.8 px | 0.52 | 1.00 | 1290 |
| over the wet one | 18 % → 18 % | 31.9 px | 0.52 | 1.00 | 1018 |
| long, no reload | 54 % → 54 % | 24.1 px | 0.52 | 1.00 | 6023 | quarters: 0.31 → 0.31 → 0.31 → 0.31

Numbers say: light vs heavy: width 23.9 → 39.7 px, dark 0.52 → 0.52; the long stroke does not run out of paint.

## Refs v3 · #21 Gritty dog contours
Gouache 1.00 + water 15 % · 53 px · 360.5 s

![Refs v3 · #21 Gritty dog contours](Refs-v3-21-Gritty-dog-contours.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 16 % → 15 % | 46.3 px | 0.39 | 0.97 | 807 |
| heavy line | 17 % → 17 % | 50.4 px | 0.39 | 0.95 | 1763 |
| pressure swell | 13 % → 13 % | 49.1 px | 0.40 | 0.98 | 827 |
| fast wave | 37 % → 31 % | 42.8 px | 0.39 | 0.83 | 3253 |
| slow wave | 37 % → 32 % | 43.2 px | 0.39 | 0.86 | 2946 |
| spiral | 52 % → 39 % | 34.3 px | 0.38 | 0.74 | 5449 |
| loop | 32 % → 30 % | 42.0 px | 0.38 | 0.93 | 2602 |
| tilted | 14 % → 14 % | 39.4 px | 0.40 | 1.00 | 2108 |
| over the wet one | 30 % → 28 % | 43.2 px | 0.40 | 0.96 | 2455 |
| long, no reload | 60 % → 44 % | 27.1 px | 0.38 | 0.72 | 11330 | quarters: 0.32 → 0.26 → 0.21 → 0.18

Numbers say: light vs heavy: width 46.3 → 50.4 px, dark 0.39 → 0.39; pressure barely changes the width.

## Refs v3 · #22 Wasilewski brush poster
Ink 0.98 · 64 px · 377.8 s

![Refs v3 · #22 Wasilewski brush poster](Refs-v3-22-Wasilewski-brush-poster.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 19 % → 19 % | 54.1 px | 0.88 | 1.04 | 455 |
| heavy line | 22 % → 22 % | 65.1 px | 0.89 | 0.99 | 1940 |
| pressure swell | 16 % → 16 % | 59.0 px | 0.88 | 1.02 | 1199 |
| fast wave | 52 % → 52 % | 59.5 px | 0.87 | 1.01 | 4352 |
| slow wave | 49 % → 49 % | 56.1 px | 0.88 | 1.00 | 4583 |
| spiral | 68 % → 68 % | 45.0 px | 0.84 | 0.99 | 8932 |
| loop | 43 % → 42 % | 55.2 px | 0.88 | 1.00 | 7576 |
| tilted | 18 % → 18 % | 50.3 px | 0.87 | 1.00 | 2218 |
| over the wet one | 37 % → 36 % | 51.6 px | 0.87 | 1.00 | 2679 |
| long, no reload | 85 % → 84 % | 38.0 px | 0.88 | 0.99 | 17047 | quarters: 0.85 → 0.84 → 0.79 → 0.69

Numbers say: light vs heavy: width 54.1 → 65.1 px, dark 0.88 → 0.89.

## Refs v3 · #23 Report dry white mask
Ink 0.93 · Gouache 0.07 · 89 px · 613.6 s

![Refs v3 · #23 Report dry white mask](Refs-v3-23-Report-dry-white-mask.png)

A light paint: laid on a grey sheet (on white it cannot be seen); **dark** = how far it is from the grey either way.

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 26 % → 27 % | 76.9 px | 0.37 | 1.01 | 1334 |
| heavy line | 29 % → 28 % | 84.7 px | 0.38 | 0.96 | 5014 |
| pressure swell | 21 % → 22 % | 79.4 px | 0.37 | 1.06 | 3182 |
| fast wave | 62 % → 60 % | 71.2 px | 0.33 | 0.98 | 9552 |
| slow wave | 61 % → 60 % | 70.2 px | 0.38 | 0.99 | 19575 |
| spiral | 75 % → 68 % | 49.2 px | 0.37 | 0.91 | 28284 |
| loop | 55 % → 55 % | 70.9 px | 0.39 | 1.00 | 7849 |
| tilted | 22 % → 22 % | 61.3 px | 0.35 | 1.00 | 4026 |
| over the wet one | 46 % → 46 % | 67.5 px | 0.35 | 1.00 | 3200 |
| long, no reload | 89 % → 88 % | 39.8 px | 0.35 | 0.99 | 26383 | quarters: 0.00 → 0.00 → 0.00 → 0.00

Numbers say: light vs heavy: width 76.9 → 84.7 px, dark 0.37 → 0.38; pressure barely changes the width; the long stroke does not run out of paint.

## Refs v3 · #24 Picasso flat oil
Gouache 1.00 + turpentine 20 % · 51 px · 361.7 s

![Refs v3 · #24 Picasso flat oil](Refs-v3-24-Picasso-flat-oil.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 16 % → 15 % | 47.5 px | 0.17 | 0.91 | 1437 |
| heavy line | 17 % → 16 % | 50.6 px | 0.17 | 0.93 | 2058 |
| pressure swell | 13 % → 12 % | 48.1 px | 0.18 | 0.95 | 1377 |
| fast wave | 42 % → 20 % | 48.4 px | 0.24 | 0.47 | 5481 |
| slow wave | 41 % → 26 % | 47.6 px | 0.19 | 0.63 | 13001 |
| spiral | 63 % → 25 % | 41.9 px | 0.21 | 0.40 | 13312 |
| loop | 35 % → 22 % | 45.2 px | 0.17 | 0.62 | 7617 |
| tilted | 14 % → 14 % | 38.1 px | 0.20 | 1.00 | 3287 |
| over the wet one | 30 % → 27 % | 44.2 px | 0.20 | 0.91 | 2624 |
| long, no reload | 77 % → 27 % | 34.6 px | 0.20 | 0.34 | 11770 | quarters: 0.17 → 0.12 → 0.05 → 0.02

Numbers say: light vs heavy: width 47.5 → 50.6 px, dark 0.17 → 0.17; pressure barely changes the width.

## Refs v3 · #25 Yellow heavy stroke
Impasto 1.00 · 272 px · 905.1 s

![Refs v3 · #25 Yellow heavy stroke](Refs-v3-25-Yellow-heavy-stroke.png)

A light paint: laid on a grey sheet (on white it cannot be seen); **dark** = how far it is from the grey either way.

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 71 % → 71 % | 205.4 px | 0.21 | 1.00 | 15420 |
| heavy line | 71 % → 55 % | 207.1 px | 0.21 | 0.77 | 33268 |
| pressure swell | 63 % → 70 % | 235.5 px | 0.19 | 1.11 | 24127 |
| fast wave | 99 % → 68 % | 114.6 px | 0.17 | 0.69 | 62796 |
| slow wave | 100 % → 52 % | 115.0 px | 0.19 | 0.53 | 62678 |
| spiral | 100 % → 68 % | 66.0 px | 0.17 | 0.68 | 101767 |
| loop | 100 % → 67 % | 129.5 px | 0.20 | 0.67 | 44222 |
| tilted | 53 % → 53 % | 148.7 px | 0.17 | 1.00 | 48339 |
| over the wet one | 89 % → 84 % | 99.4 px | 0.17 | 0.95 | 35185 |
| long, no reload | 100 % → 68 % | 44.8 px | 0.18 | 0.68 | 168405 | quarters: 0.00 → 0.00 → 0.00 → 0.00

Numbers say: light vs heavy: width 205.4 → 207.1 px, dark 0.21 → 0.21; pressure barely changes the width.

## Refs v3 · #26 Ink caricature
Ink 0.98 · 64 px · 313.2 s

![Refs v3 · #26 Ink caricature](Refs-v3-26-Ink-caricature.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 6 % → 7 % | 17.6 px | 0.79 | 1.24 | 301 |
| heavy line | 21 % → 21 % | 60.0 px | 0.84 | 1.00 | 6671 |
| pressure swell | 11 % → 11 % | 41.9 px | 0.85 | 1.03 | 1617 |
| fast wave | 40 % → 40 % | 46.7 px | 0.85 | 1.00 | 8689 |
| slow wave | 35 % → 36 % | 40.8 px | 0.83 | 1.02 | 3117 |
| spiral | 59 % → 59 % | 39.1 px | 0.79 | 1.00 | 6355 |
| loop | 31 % → 31 % | 39.6 px | 0.83 | 1.01 | 3023 |
| tilted | 19 % → 19 % | 53.5 px | 0.83 | 1.00 | 2266 |
| over the wet one | 33 % → 33 % | 38.2 px | 0.83 | 1.01 | 1426 |
| long, no reload | 79 % → 79 % | 35.4 px | 0.83 | 0.99 | 11020 | quarters: 0.71 → 0.72 → 0.72 → 0.67

Numbers say: light vs heavy: width 17.6 → 60.0 px, dark 0.79 → 0.84; the long stroke does not run out of paint.

## Refs v3 · #27 Orange impasto swatch
Impasto 1.00 · 80 px · 168.0 s

![Refs v3 · #27 Orange impasto swatch](Refs-v3-27-Orange-impasto-swatch.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 24 % → 22 % | 68.7 px | 0.30 | 0.93 | 3576 |
| heavy line | 25 % → 18 % | 71.4 px | 0.30 | 0.73 | 2315 |
| pressure swell | 19 % → 17 % | 69.7 px | 0.32 | 0.91 | 3283 |
| fast wave | 54 % → 21 % | 62.9 px | 0.37 | 0.39 | 8685 |
| slow wave | 55 % → 21 % | 63.3 px | 0.32 | 0.39 | 8370 |
| spiral | 65 % → 23 % | 43.1 px | 0.36 | 0.34 | 11814 |
| loop | 49 % → 24 % | 63.6 px | 0.31 | 0.49 | 5828 |
| tilted | 19 % → 19 % | 51.8 px | 0.33 | 1.00 | 4032 |
| over the wet one | 40 % → 33 % | 59.6 px | 0.33 | 0.82 | 4523 |
| long, no reload | 80 % → 23 % | 35.8 px | 0.33 | 0.29 | 19626 | quarters: 0.31 → 0.22 → 0.10 → 0.03

Numbers say: light vs heavy: width 68.7 → 71.4 px, dark 0.30 → 0.30; pressure barely changes the width.

## Refs v3 · #28 Miles Davis lines
Ink 0.98 · 18 px · 184.0 s

![Refs v3 · #28 Miles Davis lines](Refs-v3-28-Miles-Davis-lines.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 2 % → 4 % | 4.6 px | 0.33 | 2.45 | 124 |
| heavy line | 8 % → 8 % | 24.3 px | 0.46 | 1.01 | 919 |
| pressure swell | 4 % → 5 % | 15.7 px | 0.46 | 1.16 | 300 |
| fast wave | 15 % → 16 % | 17.4 px | 0.47 | 1.05 | 1021 |
| slow wave | 13 % → 14 % | 14.6 px | 0.44 | 1.10 | 596 |
| spiral | 21 % → 22 % | 13.8 px | 0.37 | 1.05 | 1621 |
| loop | 12 % → 13 % | 15.1 px | 0.44 | 1.08 | 866 |
| tilted | 8 % → 8 % | 21.6 px | 0.45 | 1.00 | 520 |
| over the wet one | 13 % → 14 % | 15.8 px | 0.45 | 1.03 | 425 |
| long, no reload | 33 % → 34 % | 14.7 px | 0.38 | 1.03 | 2076 | quarters: 0.18 → 0.16 → 0.13 → 0.11

Numbers say: light vs heavy: width 4.6 → 24.3 px, dark 0.33 → 0.46; wet paint spreads well beyond the stroke.

## Refs v3 · #29 Shrigley asterisk
Watercolour 1.00 + water 50 % · 64 px · 516.1 s

![Refs v3 · #29 Shrigley asterisk](Refs-v3-29-Shrigley-asterisk.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 18 % → 19 % | 53.1 px | 0.55 | 1.02 | 828 |
| heavy line | 37 % → 34 % | 107.2 px | 0.52 | 0.91 | 2889 |
| pressure swell | 22 % → 22 % | 83.3 px | 0.50 | 0.99 | 2331 |
| fast wave | 65 % → 63 % | 75.3 px | 0.49 | 0.96 | 14337 |
| slow wave | 61 % → 57 % | 70.8 px | 0.51 | 0.93 | 6490 |
| spiral | 75 % → 70 % | 49.4 px | 0.48 | 0.94 | 15848 |
| loop | 55 % → 52 % | 71.5 px | 0.50 | 0.95 | 5621 |
| tilted | 22 % → 22 % | 61.2 px | 0.51 | 1.00 | 4361 |
| over the wet one | 49 % → 47 % | 75.7 px | 0.51 | 0.96 | 2987 |
| long, no reload | 93 % → 87 % | 41.8 px | 0.47 | 0.93 | 16221 | quarters: 0.50 → 0.47 → 0.44 → 0.35

Numbers say: light vs heavy: width 53.1 → 107.2 px, dark 0.55 → 0.52.

## Refs v3 · #30 Red gouache face
Gouache 1.00 + water 15 % · 76 px · 486.7 s

![Refs v3 · #30 Red gouache face](Refs-v3-30-Red-gouache-face.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 22 % → 22 % | 65.2 px | 0.51 | 0.97 | 1438 |
| heavy line | 24 % → 23 % | 70.5 px | 0.51 | 0.93 | 2125 |
| pressure swell | 18 % → 18 % | 68.6 px | 0.51 | 0.97 | 1580 |
| fast wave | 50 % → 43 % | 58.0 px | 0.51 | 0.86 | 12225 |
| slow wave | 52 % → 43 % | 59.5 px | 0.50 | 0.83 | 5663 |
| spiral | 61 % → 45 % | 40.1 px | 0.48 | 0.75 | 13443 |
| loop | 45 % → 41 % | 58.2 px | 0.50 | 0.90 | 5383 |
| tilted | 18 % → 18 % | 51.0 px | 0.52 | 1.00 | 4447 |
| over the wet one | 40 % → 37 % | 59.4 px | 0.52 | 0.94 | 2518 |
| long, no reload | 74 % → 58 % | 33.2 px | 0.47 | 0.78 | 14306 | quarters: 0.45 → 0.40 → 0.33 → 0.28

Numbers say: light vs heavy: width 65.2 → 70.5 px, dark 0.51 → 0.51; pressure barely changes the width.

## Refs v3 · #31 Warhol blotted line
Ink 0.98 · 25 px · 210.6 s

![Refs v3 · #31 Warhol blotted line](Refs-v3-31-Warhol-blotted-line.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 3 % → 5 % | 9.4 px | 0.56 | 1.51 | 840 |
| heavy line | 10 % → 10 % | 28.1 px | 0.65 | 1.00 | 595 |
| pressure swell | 5 % → 6 % | 19.8 px | 0.65 | 1.07 | 348 |
| fast wave | 19 % → 19 % | 21.9 px | 0.66 | 1.01 | 1470 |
| slow wave | 17 % → 17 % | 19.3 px | 0.64 | 1.04 | 748 |
| spiral | 27 % → 27 % | 17.9 px | 0.58 | 1.01 | 2329 |
| loop | 15 % → 15 % | 19.3 px | 0.64 | 1.03 | 1036 |
| tilted | 10 % → 10 % | 26.7 px | 0.67 | 1.00 | 734 |
| over the wet one | 16 % → 17 % | 19.3 px | 0.67 | 1.01 | 636 |
| long, no reload | 41 % → 41 % | 18.4 px | 0.59 | 1.01 | 2853 | quarters: 0.30 → 0.29 → 0.26 → 0.24

Numbers say: light vs heavy: width 9.4 → 28.1 px, dark 0.56 → 0.65; wet paint spreads well beyond the stroke.

## Refs v3 · #32 Thick orange swipes
Impasto 1.00 · 76 px · 171.9 s

![Refs v3 · #32 Thick orange swipes](Refs-v3-32-Thick-orange-swipes.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 23 % → 21 % | 66.8 px | 0.21 | 0.92 | 3016 |
| heavy line | 24 % → 18 % | 69.1 px | 0.21 | 0.75 | 2166 |
| pressure swell | 18 % → 16 % | 67.5 px | 0.26 | 0.88 | 2723 |
| fast wave | 53 % → 20 % | 60.7 px | 0.28 | 0.37 | 6165 |
| slow wave | 53 % → 20 % | 61.2 px | 0.23 | 0.38 | 6085 |
| spiral | 65 % → 22 % | 42.6 px | 0.28 | 0.35 | 12715 |
| loop | 47 % → 23 % | 61.0 px | 0.23 | 0.49 | 5337 |
| tilted | 18 % → 18 % | 49.3 px | 0.26 | 1.00 | 3172 |
| over the wet one | 39 % → 31 % | 58.7 px | 0.26 | 0.81 | 2856 |
| long, no reload | 79 % → 21 % | 35.5 px | 0.27 | 0.27 | 12361 | quarters: 0.23 → 0.09 → 0.03 → 0.00

Numbers say: light vs heavy: width 66.8 → 69.1 px, dark 0.21 → 0.21; pressure barely changes the width.

## Refs v3 · #33 Red wet-in-wet flames
Watercolour 1.00 + water 60 % · 96 px · 747.3 s

![Refs v3 · #33 Red wet-in-wet flames](Refs-v3-33-Red-wet-in-wet-flames.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 30 % → 45 % | 85.7 px | 0.45 | 1.54 | 1107 |
| heavy line | 48 % → 54 % | 140.7 px | 0.52 | 1.11 | 3376 |
| pressure swell | 29 % → 35 % | 107.6 px | 0.45 | 1.21 | 3042 |
| fast wave | 76 % → 81 % | 87.9 px | 0.49 | 1.06 | 10672 |
| slow wave | 78 % → 80 % | 90.0 px | 0.48 | 1.03 | 26753 |
| spiral | 86 % → 91 % | 56.9 px | 0.47 | 1.05 | 30378 |
| loop | 66 % → 71 % | 85.5 px | 0.48 | 1.08 | 10905 |
| tilted | 38 % → 38 % | 105.4 px | 0.45 | 1.00 | 4658 |
| over the wet one | 68 % → 76 % | 85.3 px | 0.45 | 1.11 | 4010 |
| long, no reload | 97 % → 99 % | 43.5 px | 0.49 | 1.02 | 63609 | quarters: 0.63 → 0.54 → 0.47 → 0.37

Numbers say: light vs heavy: width 85.7 → 140.7 px, dark 0.45 → 0.52; wet paint spreads well beyond the stroke.

## Refs v3 · #34 Magenta oil patches
Gouache 1.00 + turpentine 20 % · 90 px · 629.7 s

![Refs v3 · #34 Magenta oil patches](Refs-v3-34-Magenta-oil-patches.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 29 % → 26 % | 83.0 px | 0.28 | 0.90 | 2196 |
| heavy line | 30 % → 28 % | 86.8 px | 0.28 | 0.93 | 3192 |
| pressure swell | 23 % → 22 % | 85.1 px | 0.30 | 0.99 | 2465 |
| fast wave | 64 % → 35 % | 74.0 px | 0.34 | 0.55 | 10180 |
| slow wave | 63 % → 38 % | 73.3 px | 0.30 | 0.60 | 17748 |
| spiral | 76 % → 38 % | 50.4 px | 0.34 | 0.50 | 28824 |
| loop | 56 % → 43 % | 72.7 px | 0.29 | 0.76 | 9184 |
| tilted | 21 % → 21 % | 59.9 px | 0.32 | 1.00 | 4603 |
| over the wet one | 47 % → 44 % | 71.7 px | 0.32 | 0.92 | 5201 |
| long, no reload | 96 % → 39 % | 42.9 px | 0.31 | 0.41 | 60662 | quarters: 0.31 → 0.30 → 0.25 → 0.16

Numbers say: light vs heavy: width 83.0 → 86.8 px, dark 0.28 → 0.28; pressure barely changes the width.

## Refs v3 · #35 Red band with runs
Watercolour 1.00 + water 70 % · 176 px · 1201.8 s

![Refs v3 · #35 Red band with runs](Refs-v3-35-Red-band-with-runs.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 51 % → 66 % | 149.4 px | 0.29 | 1.29 | 3402 |
| heavy line | 82 % → 80 % | 236.7 px | 0.41 | 0.99 | 16535 |
| pressure swell | 54 % → 70 % | 204.2 px | 0.30 | 1.28 | 13023 |
| fast wave | 92 % → 96 % | 106.8 px | 0.38 | 1.04 | 41527 |
| slow wave | 93 % → 94 % | 107.5 px | 0.50 | 1.01 | 50596 |
| spiral | 98 % → 100 % | 64.8 px | 0.20 | 1.01 | 67979 |
| loop | 100 % → 100 % | 129.1 px | 0.38 | 1.00 | 53147 |
| tilted | 86 % → 86 % | 240.4 px | 0.43 | 1.00 | 33666 |
| over the wet one | 93 % → 95 % | 20.5 px | 0.43 | 1.01 | 31233 |
| long, no reload | 99 % → 100 % | 44.5 px | 0.46 | 1.01 | 130444 | quarters: 0.53 → 0.51 → 0.48 → 0.34

Numbers say: light vs heavy: width 149.4 → 236.7 px, dark 0.29 → 0.41.

## Refs v3 · #36 Magenta letters flat
Gouache 1.00 + water 15 % · 64 px · 499.8 s

![Refs v3 · #36 Magenta letters flat](Refs-v3-36-Magenta-letters-flat.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 19 % → 18 % | 54.4 px | 0.40 | 0.98 | 1113 |
| heavy line | 21 % → 20 % | 61.5 px | 0.40 | 0.93 | 1866 |
| pressure swell | 15 % → 15 % | 57.3 px | 0.41 | 0.99 | 1138 |
| fast wave | 44 % → 37 % | 51.2 px | 0.41 | 0.83 | 4055 |
| slow wave | 45 % → 38 % | 51.9 px | 0.39 | 0.85 | 3990 |
| spiral | 58 % → 43 % | 38.2 px | 0.38 | 0.75 | 11584 |
| loop | 39 % → 35 % | 50.5 px | 0.40 | 0.89 | 6443 |
| tilted | 16 % → 16 % | 44.7 px | 0.41 | 1.00 | 5222 |
| over the wet one | 34 % → 33 % | 50.9 px | 0.41 | 0.96 | 3600 |
| long, no reload | 68 % → 51 % | 30.6 px | 0.39 | 0.74 | 12529 | quarters: 0.36 → 0.31 → 0.25 → 0.21

Numbers say: light vs heavy: width 54.4 → 61.5 px, dark 0.40 → 0.40.

## Refs v3 · #37 Oil still life
Gouache 1.00 + turpentine 20 % · 28 px · 320.6 s

![Refs v3 · #37 Oil still life](Refs-v3-37-Oil-still-life.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 9 % → 9 % | 27.1 px | 0.27 | 0.93 | 474 |
| heavy line | 10 % → 10 % | 29.8 px | 0.28 | 0.98 | 616 |
| pressure swell | 8 % → 8 % | 28.9 px | 0.31 | 0.97 | 567 |
| fast wave | 25 % → 12 % | 29.2 px | 0.35 | 0.49 | 1586 |
| slow wave | 25 % → 13 % | 28.8 px | 0.30 | 0.52 | 2586 |
| spiral | 42 % → 14 % | 27.7 px | 0.31 | 0.34 | 3985 |
| loop | 21 % → 11 % | 27.1 px | 0.28 | 0.54 | 6157 |
| tilted | 9 % → 9 % | 26.3 px | 0.33 | 1.00 | 1100 |
| over the wet one | 19 % → 17 % | 27.0 px | 0.33 | 0.90 | 1725 |
| long, no reload | 50 % → 13 % | 22.2 px | 0.31 | 0.26 | 11858 | quarters: 0.19 → 0.12 → 0.04 → 0.02

Numbers say: light vs heavy: width 27.1 → 29.8 px, dark 0.27 → 0.28; pressure barely changes the width.

## Refs v3 · #38 Sanguine drawing
Charcoal 0.50 · Pastel 0.50 · 12 px · 67.8 s

![Refs v3 · #38 Sanguine drawing](Refs-v3-38-Sanguine-drawing.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 2 % → 2 % | 6.7 px | 0.40 | 1.00 | 79 |
| heavy line | 3 % → 3 % | 9.7 px | 0.40 | 1.00 | 104 |
| pressure swell | 3 % → 3 % | 9.6 px | 0.39 | 1.00 | 58 |
| fast wave | 8 % → 8 % | 9.7 px | 0.39 | 1.00 | 209 |
| slow wave | 8 % → 8 % | 9.4 px | 0.39 | 1.00 | 232 |
| spiral | 13 % → 13 % | 8.7 px | 0.39 | 1.00 | 363 |
| loop | 7 % → 7 % | 8.6 px | 0.39 | 1.00 | 217 |
| tilted | 3 % → 3 % | 8.1 px | 0.39 | 1.00 | 139 |
| over the wet one | 6 % → 6 % | 9.0 px | 0.39 | 1.00 | 107 |
| long, no reload | 17 % → 17 % | 7.5 px | 0.39 | 1.00 | 599 | quarters: 0.07 → 0.07 → 0.07 → 0.07

Numbers say: light vs heavy: width 6.7 → 9.7 px, dark 0.40 → 0.40; the long stroke does not run out of paint.

## Refs v3 · #39 Thick impasto weave
Impasto 1.00 · 96 px · 286.2 s

![Refs v3 · #39 Thick impasto weave](Refs-v3-39-Thick-impasto-weave.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 28 % → 26 % | 81.6 px | 0.48 | 0.94 | 4665 |
| heavy line | 29 % → 22 % | 84.8 px | 0.48 | 0.75 | 7715 |
| pressure swell | 22 % → 21 % | 83.2 px | 0.49 | 0.93 | 4643 |
| fast wave | 62 % → 26 % | 71.7 px | 0.51 | 0.41 | 12755 |
| slow wave | 62 % → 24 % | 71.3 px | 0.49 | 0.39 | 20167 |
| spiral | 69 % → 25 % | 45.8 px | 0.50 | 0.36 | 20783 |
| loop | 56 % → 28 % | 73.1 px | 0.48 | 0.50 | 13587 |
| tilted | 21 % → 21 % | 59.9 px | 0.50 | 1.00 | 25290 |
| over the wet one | 47 % → 38 % | 70.0 px | 0.50 | 0.82 | 14261 |
| long, no reload | 86 % → 26 % | 38.4 px | 0.49 | 0.31 | 41327 | quarters: 0.48 → 0.42 → 0.36 → 0.31

Numbers say: light vs heavy: width 81.6 → 84.8 px, dark 0.48 → 0.48; pressure barely changes the width.

## Refs v3 · #40 Watercolour blooms
Watercolour 1.00 + water 55 % · 112 px · 772.0 s

![Refs v3 · #40 Watercolour blooms](Refs-v3-40-Watercolour-blooms.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 26 % → 38 % | 74.3 px | 0.03 | 1.47 | 2005 |
| heavy line | 47 % → 50 % | 137.8 px | 0.03 | 1.05 | 6734 |
| pressure swell | 30 % → 34 % | 112.0 px | 0.03 | 1.13 | 6322 |
| fast wave | 79 % → 85 % | 91.2 px | 0.04 | 1.07 | 45688 |
| slow wave | 77 % → 79 % | 89.4 px | 0.03 | 1.03 | 27946 |
| spiral | 86 % → 88 % | 56.9 px | 0.02 | 1.01 | 40706 |
| loop | 66 % → 68 % | 85.3 px | 0.03 | 1.03 | 12354 |
| tilted | 35 % → 35 % | 96.8 px | 0.03 | 1.00 | 6366 |
| over the wet one | 68 % → 75 % | 91.7 px | 0.03 | 1.11 | 6431 |
| long, no reload | 98 % → 99 % | 43.8 px | 0.03 | 1.02 | 75545 | quarters: 0.05 → 0.03 → 0.02 → 0.01

Numbers say: light vs heavy: width 74.3 → 137.8 px, dark 0.03 → 0.03.

## Refs v3 · #41 Coloured pencil
Charcoal 0.50 · Pastel 0.50 · 12 px · 111.2 s

![Refs v3 · #41 Coloured pencil](Refs-v3-41-Coloured-pencil.png)

A light paint: laid on a grey sheet (on white it cannot be seen); **dark** = how far it is from the grey either way.

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 2 % → 2 % | 6.7 px | 0.38 | 1.00 | 137 |
| heavy line | 3 % → 3 % | 9.7 px | 0.38 | 1.00 | 304 |
| pressure swell | 3 % → 3 % | 9.6 px | 0.37 | 1.00 | 152 |
| fast wave | 8 % → 8 % | 9.7 px | 0.38 | 1.00 | 381 |
| slow wave | 8 % → 8 % | 9.4 px | 0.37 | 1.00 | 342 |
| spiral | 13 % → 13 % | 8.7 px | 0.37 | 1.00 | 662 |
| loop | 7 % → 7 % | 8.6 px | 0.37 | 1.00 | 773 |
| tilted | 3 % → 3 % | 8.1 px | 0.37 | 1.00 | 449 |
| over the wet one | 6 % → 6 % | 9.0 px | 0.37 | 1.00 | 492 |
| long, no reload | 17 % → 17 % | 7.5 px | 0.38 | 1.00 | 3135 | quarters: 0.00 → 0.00 → 0.00 → 0.00

Numbers say: light vs heavy: width 6.7 → 9.7 px, dark 0.38 → 0.38; the long stroke does not run out of paint.

## Refs v3 · #42 Pink shaggy pastel
Pastel 1.00 · 38 px · 111.4 s

![Refs v3 · #42 Pink shaggy pastel](Refs-v3-42-Pink-shaggy-pastel.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 7 % → 7 % | 19.2 px | 0.19 | 1.00 | 1510 |
| heavy line | 11 % → 11 % | 31.6 px | 0.19 | 1.00 | 1934 |
| pressure swell | 8 % → 8 % | 28.9 px | 0.19 | 1.00 | 1340 |
| fast wave | 25 % → 25 % | 28.5 px | 0.19 | 1.00 | 2736 |
| slow wave | 23 % → 23 % | 27.0 px | 0.19 | 1.00 | 3450 |
| spiral | 38 % → 38 % | 24.8 px | 0.19 | 1.00 | 5763 |
| loop | 19 % → 19 % | 24.5 px | 0.19 | 1.00 | 2106 |
| tilted | 5 % → 5 % | 15.2 px | 0.19 | 1.00 | 1540 |
| over the wet one | 15 % → 15 % | 25.8 px | 0.19 | 1.00 | 941 |
| long, no reload | 45 % → 45 % | 20.0 px | 0.19 | 1.00 | 5577 | quarters: 0.10 → 0.09 → 0.10 → 0.10

Numbers say: light vs heavy: width 19.2 → 31.6 px, dark 0.19 → 0.19; the long stroke does not run out of paint.

## Refs v3 · #43 Dragged black blocks
Ink 0.93 · Gouache 0.07 · 112 px · 746.8 s

![Refs v3 · #43 Dragged black blocks](Refs-v3-43-Dragged-black-blocks.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 33 % → 34 % | 95.5 px | 0.87 | 1.03 | 3251 |
| heavy line | 37 % → 36 % | 106.7 px | 0.87 | 0.98 | 9907 |
| pressure swell | 27 % → 29 % | 99.5 px | 0.86 | 1.08 | 3967 |
| fast wave | 73 % → 77 % | 84.6 px | 0.85 | 1.05 | 13035 |
| slow wave | 71 % → 70 % | 82.4 px | 0.86 | 0.99 | 9813 |
| spiral | 81 % → 80 % | 53.7 px | 0.85 | 0.98 | 19495 |
| loop | 64 % → 64 % | 82.5 px | 0.86 | 1.00 | 22388 |
| tilted | 27 % → 27 % | 75.8 px | 0.86 | 1.00 | 5816 |
| over the wet one | 56 % → 57 % | 79.6 px | 0.86 | 1.02 | 6555 |
| long, no reload | 93 % → 93 % | 41.5 px | 0.83 | 1.00 | 27761 | quarters: 0.83 → 0.82 → 0.79 → 0.71

Numbers say: light vs heavy: width 95.5 → 106.7 px, dark 0.87 → 0.87; the long stroke does not run out of paint.

## Refs v3 · #44 Blue looping ribbon
Oil 0.52 · Gouache 0.48 + turpentine 10 % · 51 px · 432.5 s

![Refs v3 · #44 Blue looping ribbon](Refs-v3-44-Blue-looping-ribbon.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 16 % → 16 % | 45.8 px | 0.42 | 0.98 | 1004 |
| heavy line | 17 % → 16 % | 49.0 px | 0.42 | 0.97 | 1452 |
| pressure swell | 13 % → 12 % | 47.7 px | 0.44 | 0.98 | 1308 |
| fast wave | 41 % → 23 % | 47.2 px | 0.49 | 0.56 | 4553 |
| slow wave | 40 % → 31 % | 46.4 px | 0.44 | 0.78 | 3941 |
| spiral | 63 % → 29 % | 41.7 px | 0.48 | 0.45 | 5860 |
| loop | 34 % → 29 % | 44.3 px | 0.43 | 0.85 | 3689 |
| tilted | 15 % → 15 % | 40.8 px | 0.45 | 1.00 | 2390 |
| over the wet one | 30 % → 27 % | 42.0 px | 0.45 | 0.91 | 2784 |
| long, no reload | 75 % → 28 % | 33.6 px | 0.45 | 0.37 | 23824 | quarters: 0.38 → 0.35 → 0.25 → 0.14

Numbers say: light vs heavy: width 45.8 → 49.0 px, dark 0.42 → 0.42; pressure barely changes the width.

## Refs v3 · #45 Pastel pepper
Pastel 1.00 · 64 px · 104.1 s

![Refs v3 · #45 Pastel pepper](Refs-v3-45-Pastel-pepper.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 11 % → 11 % | 32.0 px | 0.57 | 1.00 | 1116 |
| heavy line | 19 % → 19 % | 53.8 px | 0.57 | 1.00 | 1590 |
| pressure swell | 13 % → 13 % | 48.6 px | 0.57 | 1.00 | 1064 |
| fast wave | 39 % → 39 % | 45.5 px | 0.57 | 1.00 | 3355 |
| slow wave | 37 % → 37 % | 43.3 px | 0.57 | 1.00 | 3173 |
| spiral | 60 % → 60 % | 39.5 px | 0.57 | 1.00 | 4691 |
| loop | 30 % → 30 % | 39.1 px | 0.57 | 1.00 | 2614 |
| tilted | 8 % → 8 % | 22.9 px | 0.57 | 1.00 | 1415 |
| over the wet one | 24 % → 24 % | 42.8 px | 0.57 | 1.00 | 1416 |
| long, no reload | 68 % → 68 % | 30.5 px | 0.57 | 1.00 | 7265 | quarters: 0.42 → 0.42 → 0.42 → 0.42

Numbers say: light vs heavy: width 32.0 → 53.8 px, dark 0.57 → 0.57; the long stroke does not run out of paint.

## Refs v3 · #46 Ink lips on wet paper
Watercolour 1.00 + water 65 % · 56 px · 502.5 s

![Refs v3 · #46 Ink lips on wet paper](Refs-v3-46-Ink-lips-on-wet-paper.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 12 % → 21 % | 33.5 px | 0.62 | 1.78 | 591 |
| heavy line | 24 % → 27 % | 70.1 px | 0.66 | 1.12 | 1561 |
| pressure swell | 15 % → 16 % | 54.8 px | 0.63 | 1.07 | 1421 |
| fast wave | 48 % → 52 % | 55.8 px | 0.60 | 1.07 | 5838 |
| slow wave | 45 % → 49 % | 51.8 px | 0.63 | 1.10 | 9556 |
| spiral | 67 % → 69 % | 44.4 px | 0.56 | 1.02 | 13402 |
| loop | 40 % → 43 % | 52.4 px | 0.60 | 1.05 | 6582 |
| tilted | 19 % → 19 % | 53.8 px | 0.59 | 1.00 | 2799 |
| over the wet one | 38 % → 41 % | 52.9 px | 0.59 | 1.07 | 2890 |
| long, no reload | 87 % → 91 % | 39.0 px | 0.55 | 1.04 | 10581 | quarters: 0.62 → 0.57 → 0.51 → 0.42

Numbers say: light vs heavy: width 33.5 → 70.1 px, dark 0.62 → 0.66; wet paint spreads well beyond the stroke.

## Refs v3 · #47 Pink knife slabs
Impasto 1.00 · 112 px · 241.3 s

![Refs v3 · #47 Pink knife slabs](Refs-v3-47-Pink-knife-slabs.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 36 % → 33 % | 104.4 px | 0.19 | 0.92 | 814 |
| heavy line | 33 % → 28 % | 94.8 px | 0.19 | 0.85 | 898 |
| pressure swell | 26 % → 26 % | 96.7 px | 0.19 | 1.02 | 770 |
| fast wave | 66 % → 65 % | 76.7 px | 0.18 | 0.98 | 7794 |
| slow wave | 61 % → 51 % | 70.6 px | 0.19 | 0.84 | 2388 |
| spiral | 62 % → 44 % | 41.0 px | 0.18 | 0.71 | 4650 |
| loop | 54 % → 42 % | 69.9 px | 0.19 | 0.78 | 3810 |
| tilted | 24 % → 24 % | 65.7 px | 0.19 | 1.00 | 873 |
| over the wet one | 54 % → 51 % | 85.3 px | 0.19 | 0.95 | 906 |
| long, no reload | 84 % → 77 % | 37.8 px | 0.18 | 0.91 | 4618 | quarters: 0.16 → 0.16 → 0.14 → 0.13

Numbers say: light vs heavy: width 104.4 → 94.8 px, dark 0.19 → 0.19.

## Refs v3 · #48 Black bands with drips
Watercolour 1.00 + water 35 % · 112 px · 595.1 s

![Refs v3 · #48 Black bands with drips](Refs-v3-48-Black-bands-with-drips.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 32 % → 33 % | 91.9 px | 0.75 | 1.04 | 10345 |
| heavy line | 33 % → 33 % | 96.3 px | 0.77 | 0.99 | 6020 |
| pressure swell | 25 % → 27 % | 93.2 px | 0.73 | 1.08 | 4306 |
| fast wave | 68 % → 69 % | 79.1 px | 0.66 | 1.01 | 17461 |
| slow wave | 68 % → 66 % | 78.0 px | 0.63 | 0.98 | 12557 |
| spiral | 77 % → 74 % | 50.6 px | 0.58 | 0.97 | 15747 |
| loop | 62 % → 61 % | 80.1 px | 0.66 | 0.99 | 9615 |
| tilted | 26 % → 26 % | 73.4 px | 0.68 | 0.99 | 7925 |
| over the wet one | 53 % → 52 % | 73.8 px | 0.68 | 0.98 | 12088 |
| long, no reload | 85 % → 83 % | 38.1 px | 0.58 | 0.98 | 32833 | quarters: 0.74 → 0.59 → 0.39 → 0.32

Numbers say: light vs heavy: width 91.9 → 96.3 px, dark 0.75 → 0.77; pressure barely changes the width.

## Refs v3 · #49 Magenta letters round
Ink 0.98 · 64 px · 402.9 s

![Refs v3 · #49 Magenta letters round](Refs-v3-49-Magenta-letters-round.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 7 % → 8 % | 20.5 px | 0.47 | 1.16 | 516 |
| heavy line | 20 % → 20 % | 58.5 px | 0.50 | 1.00 | 4243 |
| pressure swell | 11 % → 11 % | 41.8 px | 0.53 | 1.02 | 2172 |
| fast wave | 40 % → 40 % | 46.5 px | 0.54 | 1.00 | 4597 |
| slow wave | 36 % → 36 % | 41.3 px | 0.49 | 1.02 | 3009 |
| spiral | 60 % → 60 % | 39.4 px | 0.45 | 1.00 | 7280 |
| loop | 31 % → 31 % | 39.7 px | 0.49 | 1.01 | 2484 |
| tilted | 19 % → 19 % | 53.4 px | 0.51 | 1.00 | 1793 |
| over the wet one | 33 % → 33 % | 38.1 px | 0.51 | 1.01 | 1533 |
| long, no reload | 79 % → 78 % | 35.3 px | 0.49 | 0.99 | 14596 | quarters: 0.43 → 0.43 → 0.41 → 0.38

Numbers say: light vs heavy: width 20.5 → 58.5 px, dark 0.47 → 0.50; the long stroke does not run out of paint.

## Refs v3 · #50 Swipes on seaside
Gouache 1.00 + water 15 % · 80 px · 494.3 s

![Refs v3 · #50 Swipes on seaside](Refs-v3-50-Swipes-on-seaside.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 24 % → 23 % | 69.0 px | 0.30 | 0.97 | 2500 |
| heavy line | 25 % → 24 % | 73.1 px | 0.31 | 0.94 | 2142 |
| pressure swell | 19 % → 19 % | 71.2 px | 0.33 | 1.00 | 5772 |
| fast wave | 52 % → 46 % | 60.5 px | 0.33 | 0.87 | 9610 |
| slow wave | 53 % → 44 % | 60.8 px | 0.29 | 0.84 | 15745 |
| spiral | 63 % → 46 % | 41.3 px | 0.28 | 0.74 | 15315 |
| loop | 47 % → 43 % | 60.8 px | 0.30 | 0.92 | 6277 |
| tilted | 19 % → 19 % | 53.1 px | 0.34 | 1.00 | 3784 |
| over the wet one | 41 % → 39 % | 61.4 px | 0.34 | 0.95 | 3104 |
| long, no reload | 74 % → 57 % | 33.2 px | 0.27 | 0.77 | 39747 | quarters: 0.26 → 0.22 → 0.17 → 0.14

Numbers say: light vs heavy: width 69.0 → 73.1 px, dark 0.30 → 0.31; pressure barely changes the width.

## Refs v3 · #01 HW peach cloud — own sheet
own sheet 800 × 1095 · Gouache 1.00 + turpentine 30 % · 104 px · 2271.3 s

![Refs v3 · #01 HW peach cloud — own sheet](Refs-v3-01-HW-peach-cloud-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 9 % → 73 % | 103.7 px | 0.13 | 7.76 | 1211 |
| stroke 2 | 14 % → 77 % | 175.1 px | 0.13 | 5.42 | 1515 |
| stroke 3 | 20 % → 79 % | 298.8 px | 0.13 | 3.92 | 1382 |
| stroke 4 | 21 % → 79 % | 361.1 px | 0.13 | 3.70 | 1516 |
| stroke 5 | 12 % → 85 % | 124.2 px | 0.25 | 7.36 | 4263 |
| stroke 6 | 24 % → 85 % | 267.2 px | 0.15 | 3.52 | 4102 |
| stroke 7 | 41 % → 87 % | 805.3 px | 0.15 | 2.10 | 1270 |
| stroke 8 | 27 % → 80 % | 188.5 px | 0.15 | 2.99 | 7726 |
| stroke 9 | 44 % → 79 % | 401.2 px | 0.20 | 1.79 | 2987 |
| stroke 10 | 39 % → 78 % | 429.5 px | 0.12 | 2.01 | 6044 |
| stroke 11 | 60 % → 82 % | 945.5 px | 0.12 | 1.36 | 1646 |
| stroke 12 | 20 % → 80 % | 180.0 px | 0.18 | 4.04 | 11367 |
| stroke 13 | 64 % → 85 % | 992.6 px | 0.15 | 1.32 | 7381 |
| stroke 14 | 51 % → 87 % | 683.6 px | 0.13 | 1.69 | 7486 |
| stroke 15 | 54 % → 91 % | 765.7 px | 0.17 | 1.68 | 8608 |
| stroke 16 | 43 % → 78 % | 885.4 px | 0.13 | 1.79 | 3653 |
| stroke 17 | 49 % → 86 % | 697.9 px | 0.16 | 1.75 | 4261 |
| stroke 18 | 49 % → 75 % | 677.9 px | 0.13 | 1.52 | 3190 |
| stroke 19 | 58 % → 91 % | 1311.9 px | 0.17 | 1.56 | 1664 |
| stroke 20 | 60 % → 76 % | 521.8 px | 0.12 | 1.27 | 5104 |
| stroke 21 | 59 % → 73 % | 816.3 px | 0.12 | 1.24 | 2079 |
| stroke 22 | 45 % → 87 % | 890.6 px | 0.20 | 1.93 | 1950 |
| stroke 23 | 61 % → 83 % | 924.8 px | 0.16 | 1.35 | 2798 |
| stroke 24 | 74 % → 83 % | 1429.5 px | 0.12 | 1.13 | 2133 |
| stroke 25 | 64 % → 86 % | 984.8 px | 0.16 | 1.35 | 2551 |
| stroke 26 | 59 % → 89 % | 1365.4 px | 0.19 | 1.51 | 1593 |
| stroke 27 | 60 % → 86 % | 1150.7 px | 0.19 | 1.42 | 2642 |
| stroke 28 | 73 % → 88 % | 1656.6 px | 0.15 | 1.20 | 2372 |
| stroke 29 | 82 % → 83 % | 1259.7 px | 0.12 | 1.02 | 2254 |
| stroke 30 | 64 % → 92 % | 1297.2 px | 0.20 | 1.44 | 2232 |
| stroke 31 | 78 % → 91 % | 1652.1 px | 0.15 | 1.18 | 2433 |
| stroke 32 | 22 % → 86 % | 303.6 px | 0.29 | 3.86 | 2701 |
| stroke 33 | 27 % → 87 % | 439.2 px | 0.30 | 3.21 | 1902 |
| stroke 34 | 25 % → 73 % | 266.5 px | 0.26 | 2.90 | 398 |
| stroke 35 | 44 % → 68 % | 1085.5 px | 0.13 | 1.53 | 62 |
| stroke 36 | 61 % → 68 % | 468.9 px | 0.12 | 1.11 | 417 |
| stroke 37 | 69 % → 74 % | 837.2 px | 0.13 | 1.07 | 342 |
| stroke 38 | 66 % → 68 % | 558.8 px | 0.12 | 1.04 | 382 |
| stroke 39 | 69 % → 73 % | 1014.0 px | 0.12 | 1.05 | 385 |
| stroke 40 | 67 % → 70 % | 837.2 px | 0.13 | 1.05 | 256 |
| stroke 41 | 67 % → 72 % | 1940.1 px | 0.13 | 1.07 | 89 |
| stroke 42 | 69 % → 73 % | 2658.2 px | 0.13 | 1.06 | 145 |
| stroke 43 | 67 % → 71 % | 1916.0 px | 0.13 | 1.06 | 136 |
| stroke 44 | 64 % → 75 % | 1013.1 px | 0.14 | 1.16 | 284 |
| stroke 45 | 65 % → 75 % | 684.9 px | 0.14 | 1.14 | 354 |
| stroke 46 | 68 % → 75 % | 2783.3 px | 0.13 | 1.10 | 84 |
| stroke 47 | 63 % → 73 % | 2109.9 px | 0.14 | 1.17 | 163 |
| stroke 48 | 76 % → 79 % | 1474.5 px | 0.12 | 1.03 | 417 |
| stroke 49 | 76 % → 81 % | 1349.1 px | 0.13 | 1.07 | 810 |
| stroke 50 | 75 % → 79 % | 2127.3 px | 0.13 | 1.05 | 262 |
| stroke 51 | 82 % → 84 % | 2890.8 px | 0.12 | 1.02 | 186 |
| stroke 52 | 77 % → 84 % | 2680.8 px | 0.14 | 1.08 | 326 |
| stroke 53 | 78 % → 78 % | 1546.2 px | 0.12 | 1.00 | 329 |
| stroke 54 | 77 % → 80 % | 1430.9 px | 0.13 | 1.03 | 312 |
| stroke 55 | 82 % → 83 % | 1811.1 px | 0.12 | 1.00 | 313 |
| stroke 56 | 78 % → 80 % | 2123.9 px | 0.13 | 1.02 | 237 |
| stroke 57 | 76 % → 80 % | 2165.3 px | 0.14 | 1.04 | 206 |
| stroke 58 | 85 % → 84 % | 1416.0 px | 0.12 | 0.99 | 472 |
| stroke 59 | 79 % → 84 % | 1625.7 px | 0.14 | 1.07 | 430 |
| stroke 60 | 80 % → 78 % | 2078.7 px | 0.12 | 0.98 | 300 |
| stroke 61 | 87 % → 85 % | 2561.0 px | 0.12 | 0.97 | 231 |
| stroke 62 | 79 % → 80 % | 3921.7 px | 0.13 | 1.01 | 94 |
| stroke 63 | 80 % → 80 % | 3576.7 px | 0.12 | 1.00 | 125 |
| stroke 64 | 79 % → 81 % | 2509.4 px | 0.13 | 1.02 | 218 |
| stroke 65 | 86 % → 85 % | 5462.3 px | 0.12 | 0.98 | 80 |
| stroke 66 | 87 % → 84 % | 4197.4 px | 0.12 | 0.97 | 131 |
| stroke 67 | 79 % → 79 % | 2799.2 px | 0.13 | 1.00 | 190 |
| stroke 68 | 83 % → 86 % | 3351.3 px | 0.14 | 1.04 | 254 |
| stroke 69 | 78 % → 79 % | 3105.3 px | 0.13 | 1.01 | 161 |
| stroke 70 | 85 % → 83 % | 3986.5 px | 0.12 | 0.97 | 159 |
| stroke 71 | 80 % → 81 % | 5093.0 px | 0.13 | 1.01 | 101 |
| stroke 72 | 81 % → 80 % | 3749.0 px | 0.13 | 0.99 | 183 |
| stroke 73 | 88 % → 85 % | 4617.6 px | 0.12 | 0.97 | 110 |
| stroke 74 | 75 % → 73 % | 1624.1 px | 0.13 | 0.97 | 107 |
| stroke 75 | 74 % → 72 % | 2458.2 px | 0.13 | 0.97 | 79 |
| stroke 76 | 77 % → 74 % | 1327.2 px | 0.13 | 0.96 | 215 |
| stroke 77 | 76 % → 74 % | 2805.3 px | 0.13 | 0.97 | 113 |
| stroke 78 | 76 % → 73 % | 2340.0 px | 0.13 | 0.97 | 104 |
| stroke 79 | 63 % → 81 % | 3096.5 px | 0.15 | 1.30 | 98 |
| stroke 80 | 59 % → 83 % | 3641.3 px | 0.16 | 1.40 | 95 |
| stroke 81 | 60 % → 81 % | 3348.8 px | 0.15 | 1.35 | 98 |
| stroke 82 | 61 % → 82 % | 2704.8 px | 0.16 | 1.33 | 163 |
| stroke 83 | 71 % → 83 % | 3552.9 px | 0.17 | 1.18 | 100 |
| stroke 84 | 60 % → 84 % | 1316.0 px | 0.21 | 1.40 | 294 |
| stroke 85 | 67 % → 84 % | 3062.9 px | 0.18 | 1.26 | 110 |
| stroke 86 | 62 % → 84 % | 2463.1 px | 0.21 | 1.35 | 209 |
| stroke 87 | 33 % → 73 % | 330.4 px | 0.25 | 2.23 | 386 |
| stroke 88 | 58 % → 79 % | 678.8 px | 0.17 | 1.37 | 511 |
| stroke 89 | 43 % → 77 % | 529.0 px | 0.22 | 1.77 | 692 |
| stroke 90 | 60 % → 82 % | 2370.3 px | 0.17 | 1.37 | 155 |
| stroke 91 | 35 % → 73 % | 385.5 px | 0.26 | 2.10 | 417 |
| stroke 92 | 58 % → 77 % | 576.0 px | 0.19 | 1.33 | 537 |
| stroke 93 | 65 % → 78 % | 584.4 px | 0.17 | 1.20 | 568 |
| stroke 94 | 67 % → 79 % | 1546.1 px | 0.17 | 1.19 | 214 |
| stroke 95 | 67 % → 82 % | 1615.8 px | 0.17 | 1.22 | 222 |
| stroke 96 | 70 % → 79 % | 1287.8 px | 0.16 | 1.13 | 311 |
| stroke 97 | 61 % → 78 % | 1049.2 px | 0.19 | 1.27 | 433 |
| stroke 98 | 70 % → 80 % | 2641.2 px | 0.17 | 1.15 | 154 |
| stroke 99 | 58 % → 77 % | 842.5 px | 0.20 | 1.34 | 434 |
| stroke 100 | 69 % → 82 % | 2560.2 px | 0.17 | 1.18 | 297 |
| stroke 101 | 66 % → 76 % | 1539.5 px | 0.19 | 1.16 | 251 |
| stroke 102 | 70 % → 82 % | 2940.9 px | 0.17 | 1.17 | 138 |
| stroke 103 | 72 % → 79 % | 2650.4 px | 0.16 | 1.11 | 128 |
| stroke 104 | 69 % → 78 % | 1117.5 px | 0.17 | 1.14 | 435 |
| stroke 105 | 72 % → 79 % | 2039.9 px | 0.16 | 1.11 | 202 |
| stroke 106 | 67 % → 79 % | 1307.3 px | 0.18 | 1.18 | 383 |
| stroke 107 | 72 % → 79 % | 2795.7 px | 0.17 | 1.10 | 98 |
| stroke 108 | 70 % → 81 % | 3173.9 px | 0.16 | 1.16 | 91 |
| stroke 109 | 66 % → 92 % | 1594.2 px | 0.20 | 1.39 | 366 |
| stroke 110 | 68 % → 92 % | 3921.4 px | 0.20 | 1.35 | 126 |
| stroke 111 | 65 % → 92 % | 3681.8 px | 0.21 | 1.42 | 140 |
| stroke 112 | 69 % → 92 % | 3972.3 px | 0.19 | 1.33 | 113 |
| stroke 113 | 68 % → 91 % | 4431.4 px | 0.20 | 1.33 | 88 |
| stroke 114 | 44 % → 80 % | 466.9 px | 0.23 | 1.83 | 518 |
| stroke 115 | 34 % → 79 % | 343.5 px | 0.22 | 2.28 | 464 |
| stroke 116 | 26 % → 78 % | 528.3 px | 0.26 | 3.05 | 312 |
| stroke 117 | 10 % → 73 % | 104.7 px | 0.35 | 7.63 | 290 |
| stroke 118 | 10 % → 75 % | 247.4 px | 0.36 | 7.43 | 136 |
| stroke 119 | 31 % → 77 % | 314.2 px | 0.27 | 2.48 | 447 |
| stroke 120 | 22 % → 78 % | 357.4 px | 0.32 | 3.58 | 298 |
| stroke 121 | 54 % → 80 % | 873.3 px | 0.22 | 1.47 | 335 |
| stroke 122 | 53 % → 78 % | 756.1 px | 0.20 | 1.47 | 299 |
| stroke 123 | 34 % → 78 % | 690.7 px | 0.26 | 2.25 | 228 |
| stroke 124 | 24 % → 78 % | 870.7 px | 0.29 | 3.24 | 122 |
| stroke 125 | 12 % → 73 % | 455.3 px | 0.36 | 6.24 | 69 |
| stroke 126 | 52 % → 89 % | 1179.9 px | 0.25 | 1.69 | 340 |
| stroke 127 | 60 % → 88 % | 1185.5 px | 0.22 | 1.46 | 420 |
| stroke 128 | 53 % → 89 % | 3397.0 px | 0.26 | 1.70 | 93 |
| stroke 129 | 64 % → 90 % | 2390.2 px | 0.22 | 1.42 | 189 |
| stroke 130 | 9 % → 80 % | 501.0 px | 0.40 | 9.01 | 67 |
| stroke 131 | 9 % → 80 % | 540.4 px | 0.39 | 8.55 | 81 |
| stroke 132 | 10 % → 81 % | 567.3 px | 0.39 | 8.36 | 86 |
| stroke 133 | 24 % → 61 % | 341.7 px | 0.32 | 2.51 | 201 |
| stroke 134 | 25 % → 62 % | 756.1 px | 0.31 | 2.42 | 94 |
| stroke 135 | 27 % → 62 % | 793.5 px | 0.31 | 2.31 | 86 |
| stroke 136 | 25 % → 60 % | 758.5 px | 0.32 | 2.45 | 91 |
| stroke 137 | 12 % → 76 % | 268.2 px | 0.40 | 6.24 | 211 |
| stroke 138 | 17 % → 69 % | 343.8 px | 0.38 | 4.04 | 247 |
| stroke 139 | 20 % → 67 % | 205.8 px | 0.38 | 3.37 | 363 |
| stroke 140 | 17 % → 74 % | 442.9 px | 0.41 | 4.49 | 174 |
| stroke 141 | 18 % → 75 % | 707.2 px | 0.40 | 4.26 | 109 |
| stroke 142 | 22 % → 67 % | 1060.1 px | 0.38 | 2.99 | 78 |
| stroke 143 | 15 % → 76 % | 686.2 px | 0.40 | 4.91 | 102 |
| stroke 144 | 76 % → 79 % | 4287.7 px | 0.12 | 1.04 | 43 |
| stroke 145 | 71 % → 72 % | 812.0 px | 0.15 | 1.02 | 266 |
| stroke 146 | 84 % → 88 % | 2824.7 px | 0.13 | 1.05 | 229 |
| stroke 147 | 69 % → 92 % | 1774.1 px | 0.20 | 1.34 | 178 |
| stroke 148 | 59 % → 95 % | 2449.3 px | 0.25 | 1.61 | 77 |
| stroke 149 | 54 % → 83 % | 3194.0 px | 0.24 | 1.54 | 26 |
| stroke 150 | 37 % → 81 % | 629.7 px | 0.27 | 2.22 | 193 |
| stroke 151 | 26 % → 83 % | 1285.0 px | 0.35 | 3.15 | 72 |
| stroke 152 | 25 % → 92 % | 1417.1 px | 0.35 | 3.62 | 50 |
| stroke 153 | 20 % → 80 % | 260.9 px | 0.39 | 4.11 | 501 |
| stroke 154 | 23 % → 78 % | 260.7 px | 0.37 | 3.39 | 280 |
| stroke 155 | 43 % → 73 % | 695.3 px | 0.27 | 1.69 | 284 |
| stroke 156 | 34 % → 75 % | 1989.4 px | 0.33 | 2.19 | 60 |
| stroke 157 | 33 % → 70 % | 791.5 px | 0.33 | 2.13 | 149 |
| stroke 158 | 25 % → 79 % | 1086.3 px | 0.39 | 3.10 | 78 |
| stroke 159 | 14 % → 73 % | 350.4 px | 0.42 | 5.09 | 33 |
| stroke 160 | 71 % → 72 % | 1143.2 px | 0.13 | 1.01 | 293 |
| stroke 161 | 70 % → 71 % | 983.8 px | 0.13 | 1.01 | 352 |
| stroke 162 | 72 % → 72 % | 848.9 px | 0.14 | 1.00 | 312 |
| stroke 163 | 74 % → 73 % | 2555.0 px | 0.13 | 0.99 | 126 |
| stroke 164 | 73 % → 73 % | 1622.6 px | 0.13 | 0.99 | 160 |
| stroke 165 | 71 % → 69 % | 574.3 px | 0.14 | 0.97 | 514 |
| stroke 166 | 57 % → 93 % | 1221.5 px | 0.25 | 1.62 | 395 |
| stroke 167 | 57 % → 93 % | 1473.3 px | 0.25 | 1.63 | 342 |
| stroke 168 | 65 % → 93 % | 3705.2 px | 0.23 | 1.43 | 151 |
| stroke 169 | 65 % → 93 % | 2640.4 px | 0.22 | 1.44 | 187 |
| stroke 170 | 60 % → 93 % | 1319.6 px | 0.25 | 1.54 | 379 |
| stroke 171 | 47 % → 92 % | 1526.9 px | 0.29 | 1.97 | 249 |
| stroke 172 | 75 % → 93 % | 4296.0 px | 0.19 | 1.24 | 132 |
| stroke 173 | 61 % → 94 % | 938.3 px | 0.26 | 1.55 | 645 |
| stroke 174 | 54 % → 93 % | 895.0 px | 0.29 | 1.71 | 651 |
| stroke 175 | 28 % → 87 % | 826.1 px | 0.39 | 3.07 | 243 |
| stroke 176 | 69 % → 94 % | 3434.7 px | 0.24 | 1.36 | 138 |
| stroke 177 | 39 % → 89 % | 859.6 px | 0.36 | 2.25 | 350 |
| stroke 178 | 53 % → 95 % | 1836.5 px | 0.31 | 1.79 | 173 |
| stroke 179 | 30 % → 82 % | 1166.1 px | 0.39 | 2.68 | 309 |
| stroke 180 | 32 % → 90 % | 767.6 px | 0.38 | 2.81 | 329 |
| stroke 181 | 55 % → 95 % | 1677.5 px | 0.31 | 1.71 | 206 |
| stroke 182 | 58 % → 92 % | 1569.0 px | 0.30 | 1.58 | 269 |
| stroke 183 | 48 % → 93 % | 2369.5 px | 0.35 | 1.95 | 116 |
| stroke 184 | 66 % → 95 % | 1927.9 px | 0.27 | 1.43 | 260 |
| stroke 185 | 78 % → 93 % | 3830.7 px | 0.22 | 1.20 | 117 |
| stroke 186 | 62 % → 95 % | 2026.6 px | 0.29 | 1.52 | 227 |
| stroke 187 | 48 % → 89 % | 1249.5 px | 0.34 | 1.85 | 285 |
| stroke 188 | 70 % → 93 % | 1776.2 px | 0.26 | 1.34 | 297 |
| stroke 189 | 35 % → 87 % | 1580.5 px | 0.39 | 2.47 | 141 |
| stroke 190 | 37 % → 89 % | 1846.5 px | 0.37 | 2.38 | 126 |
| stroke 191 | 58 % → 95 % | 2141.6 px | 0.31 | 1.64 | 198 |
| stroke 192 | 79 % → 93 % | 4417.3 px | 0.21 | 1.17 | 110 |
| stroke 193 | 77 % → 93 % | 3851.6 px | 0.22 | 1.20 | 138 |
| stroke 194 | 71 % → 94 % | 4010.8 px | 0.26 | 1.33 | 226 |
| stroke 195 | 54 % → 84 % | 1265.5 px | 0.29 | 1.54 | 289 |
| stroke 196 | 48 % → 83 % | 2089.5 px | 0.32 | 1.74 | 157 |
| stroke 197 | 53 % → 83 % | 1449.1 px | 0.29 | 1.56 | 458 |
| stroke 198 | 55 % → 84 % | 2013.8 px | 0.29 | 1.52 | 229 |
| stroke 199 | 41 % → 80 % | 434.4 px | 0.30 | 1.95 | 834 |
| stroke 200 | 46 % → 81 % | 500.1 px | 0.28 | 1.78 | 967 |
| stroke 201 | 62 % → 81 % | 1836.9 px | 0.24 | 1.31 | 210 |
| stroke 202 | 58 % → 80 % | 1653.4 px | 0.25 | 1.37 | 215 |
| stroke 203 | 29 % → 81 % | 572.1 px | 0.37 | 2.79 | 572 |
| stroke 204 | 62 % → 82 % | 1927.5 px | 0.25 | 1.32 | 246 |
| stroke 205 | 28 % → 80 % | 793.8 px | 0.37 | 2.88 | 183 |
| stroke 206 | 32 % → 80 % | 812.3 px | 0.35 | 2.48 | 199 |
| stroke 207 | 40 % → 79 % | 1550.2 px | 0.30 | 1.97 | 101 |
| stroke 208 | 68 % → 80 % | 1718.5 px | 0.21 | 1.17 | 244 |
| stroke 209 | 66 % → 79 % | 1501.4 px | 0.22 | 1.19 | 324 |
| stroke 210 | 73 % → 81 % | 1354.2 px | 0.20 | 1.11 | 388 |
| stroke 211 | 64 % → 79 % | 2110.1 px | 0.23 | 1.22 | 212 |
| stroke 212 | 77 % → 82 % | 2984.0 px | 0.18 | 1.07 | 143 |
| stroke 213 | 73 % → 82 % | 3200.6 px | 0.21 | 1.13 | 144 |
| stroke 214 | 32 % → 86 % | 543.2 px | 0.39 | 2.68 | 420 |
| stroke 215 | 31 % → 85 % | 887.4 px | 0.38 | 2.71 | 229 |
| stroke 216 | 30 % → 77 % | 402.4 px | 0.39 | 2.57 | 451 |
| stroke 217 | 29 % → 79 % | 565.4 px | 0.40 | 2.76 | 253 |
| stroke 218 | 33 % → 75 % | 1197.7 px | 0.38 | 2.30 | 92 |
| stroke 219 | 28 % → 78 % | 509.0 px | 0.41 | 2.75 | 247 |
| stroke 220 | 33 % → 84 % | 1176.7 px | 0.41 | 2.57 | 140 |
| stroke 221 | 29 % → 78 % | 832.5 px | 0.41 | 2.68 | 253 |
| stroke 222 | 32 % → 84 % | 1232.4 px | 0.41 | 2.60 | 240 |
| stroke 223 | 29 % → 79 % | 639.4 px | 0.42 | 2.76 | 381 |
| stroke 224 | 35 % → 81 % | 1319.0 px | 0.39 | 2.29 | 208 |
| stroke 225 | 39 % → 74 % | 1384.1 px | 0.37 | 1.89 | 117 |
| stroke 226 | 36 % → 81 % | 968.2 px | 0.40 | 2.25 | 218 |
| stroke 227 | 39 % → 82 % | 826.2 px | 0.40 | 2.13 | 507 |
| stroke 228 | 37 % → 81 % | 1455.7 px | 0.39 | 2.16 | 200 |
| stroke 229 | 32 % → 78 % | 1126.1 px | 0.42 | 2.44 | 175 |
| stroke 230 | 44 % → 88 % | 892.7 px | 0.38 | 1.99 | 438 |
| stroke 231 | 33 % → 78 % | 796.9 px | 0.42 | 2.35 | 239 |
| stroke 232 | 37 % → 82 % | 1278.3 px | 0.41 | 2.18 | 202 |
| stroke 233 | 38 % → 81 % | 2066.8 px | 0.39 | 2.13 | 106 |
| stroke 234 | 35 % → 78 % | 1632.1 px | 0.41 | 2.20 | 134 |
| stroke 235 | 37 % → 88 % | 1866.3 px | 0.41 | 2.34 | 128 |
| stroke 236 | 39 % → 77 % | 504.9 px | 0.40 | 1.97 | 400 |
| stroke 237 | 38 % → 79 % | 999.8 px | 0.42 | 2.06 | 175 |
| stroke 238 | 38 % → 80 % | 1434.6 px | 0.43 | 2.11 | 119 |
| stroke 239 | 40 % → 80 % | 1701.1 px | 0.42 | 2.03 | 252 |
| stroke 240 | 81 % → 82 % | 1094.3 px | 0.16 | 1.02 | 340 |
| stroke 241 | 76 % → 95 % | 4404.8 px | 0.23 | 1.26 | 110 |
| stroke 242 | 81 % → 84 % | 5172.6 px | 0.17 | 1.04 | 35 |
| stroke 243 | 77 % → 81 % | 1656.9 px | 0.18 | 1.06 | 175 |
| stroke 244 | 56 % → 85 % | 1124.6 px | 0.31 | 1.52 | 299 |
| stroke 245 | 56 % → 81 % | 3272.2 px | 0.31 | 1.43 | 28 |
| stroke 246 | 54 % → 71 % | 551.1 px | 0.26 | 1.30 | 347 |
| stroke 247 | 42 % → 73 % | 617.6 px | 0.39 | 1.75 | 140 |
| stroke 248 | 66 % → 90 % | 1540.1 px | 0.27 | 1.37 | 221 |
| stroke 249 | 67 % → 93 % | 1497.5 px | 0.29 | 1.39 | 243 |
| stroke 250 | 71 % → 92 % | 1530.1 px | 0.26 | 1.30 | 212 |
| stroke 251 | 54 % → 90 % | 985.1 px | 0.37 | 1.65 | 209 |
| stroke 252 | 74 % → 93 % | 1831.9 px | 0.26 | 1.25 | 240 |
| stroke 253 | 56 % → 89 % | 1026.9 px | 0.36 | 1.58 | 203 |
| stroke 254 | 65 % → 91 % | 1779.1 px | 0.32 | 1.40 | 168 |
| stroke 255 | 76 % → 89 % | 4981.9 px | 0.24 | 1.17 | 60 |
| stroke 256 | 69 % → 89 % | 3409.0 px | 0.28 | 1.28 | 111 |
| stroke 257 | 70 % → 93 % | 2283.5 px | 0.30 | 1.32 | 143 |
| stroke 258 | 64 % → 91 % | 3175.9 px | 0.34 | 1.42 | 60 |
| stroke 259 | 48 % → 88 % | 1930.9 px | 0.41 | 1.83 | 82 |
| stroke 260 | 47 % → 86 % | 1747.1 px | 0.42 | 1.85 | 86 |
| stroke 261 | 58 % → 90 % | 3241.7 px | 0.38 | 1.56 | 74 |
| stroke 262 | 69 % → 92 % | 3485.1 px | 0.31 | 1.32 | 74 |
| stroke 263 | 63 % → 91 % | 4044.1 px | 0.35 | 1.44 | 71 |
| stroke 264 | 73 % → 93 % | 3025.5 px | 0.29 | 1.26 | 129 |
| stroke 265 | 81 % → 94 % | 5193.6 px | 0.24 | 1.16 | 66 |
| stroke 266 | 81 % → 92 % | 5258.6 px | 0.23 | 1.14 | 54 |
| stroke 267 | 55 % → 88 % | 1339.5 px | 0.38 | 1.60 | 191 |
| stroke 268 | 66 % → 93 % | 1885.3 px | 0.34 | 1.41 | 174 |
| stroke 269 | 55 % → 86 % | 1051.0 px | 0.39 | 1.57 | 266 |
| stroke 270 | 66 % → 91 % | 1479.6 px | 0.35 | 1.39 | 161 |
| stroke 271 | 52 % → 85 % | 2684.4 px | 0.39 | 1.62 | 123 |
| stroke 272 | 63 % → 91 % | 1183.1 px | 0.36 | 1.44 | 306 |
| stroke 273 | 62 % → 91 % | 1254.8 px | 0.37 | 1.47 | 335 |
| stroke 274 | 69 % → 95 % | 3099.7 px | 0.35 | 1.37 | 115 |
| stroke 275 | 54 % → 85 % | 3079.7 px | 0.40 | 1.58 | 82 |
| stroke 276 | 71 % → 93 % | 2877.0 px | 0.34 | 1.31 | 106 |
| stroke 277 | 58 % → 90 % | 3251.6 px | 0.39 | 1.56 | 112 |
| stroke 278 | 63 % → 91 % | 3523.1 px | 0.37 | 1.43 | 162 |
| stroke 279 | 47 % → 77 % | 473.4 px | 0.41 | 1.63 | 485 |
| stroke 280 | 49 % → 76 % | 1096.0 px | 0.40 | 1.56 | 195 |
| stroke 281 | 50 % → 78 % | 1157.8 px | 0.42 | 1.56 | 228 |
| stroke 282 | 52 % → 78 % | 663.3 px | 0.41 | 1.52 | 530 |
| stroke 283 | 52 % → 77 % | 679.7 px | 0.41 | 1.47 | 475 |
| stroke 284 | 56 % → 77 % | 1045.7 px | 0.40 | 1.38 | 137 |
| stroke 285 | 54 % → 77 % | 2168.1 px | 0.40 | 1.42 | 105 |
| stroke 286 | 54 % → 75 % | 2462.8 px | 0.39 | 1.40 | 47 |
| stroke 287 | 53 % → 75 % | 1199.6 px | 0.44 | 1.40 | 57 |
| stroke 288 | 55 % → 77 % | 840.2 px | 0.41 | 1.42 | 144 |
| stroke 289 | 55 % → 74 % | 2512.7 px | 0.38 | 1.36 | 45 |
| stroke 290 | 56 % → 76 % | 1114.9 px | 0.41 | 1.37 | 89 |
| stroke 291 | 54 % → 74 % | 1960.7 px | 0.41 | 1.36 | 55 |
| stroke 292 | 55 % → 78 % | 3039.1 px | 0.41 | 1.42 | 32 |
| stroke 293 | 56 % → 80 % | 2068.1 px | 0.41 | 1.43 | 90 |
| stroke 294 | 55 % → 75 % | 2220.4 px | 0.41 | 1.36 | 65 |
| stroke 295 | 78 % → 77 % | 1015.0 px | 0.12 | 0.99 | 257 |
| stroke 296 | 76 % → 74 % | 1383.1 px | 0.13 | 0.97 | 194 |
| stroke 297 | 75 % → 73 % | 1135.2 px | 0.13 | 0.97 | 260 |
| stroke 298 | 81 % → 82 % | 2807.8 px | 0.18 | 1.01 | 110 |
| stroke 299 | 84 % → 94 % | 2948.3 px | 0.23 | 1.12 | 115 |
| stroke 300 | 75 % → 84 % | 3500.7 px | 0.25 | 1.13 | 67 |
| stroke 301 | 71 % → 80 % | 1727.6 px | 0.20 | 1.12 | 195 |
| stroke 302 | 67 % → 82 % | 2271.0 px | 0.32 | 1.22 | 111 |
| stroke 303 | 68 % → 84 % | 1100.4 px | 0.35 | 1.24 | 404 |
| stroke 304 | 65 % → 87 % | 4146.0 px | 0.34 | 1.34 | 39 |
| stroke 305 | 61 % → 79 % | 1694.9 px | 0.40 | 1.30 | 100 |
| stroke 306 | 59 % → 82 % | 1912.1 px | 0.42 | 1.38 | 113 |
| stroke 307 | 55 % → 71 % | 1992.1 px | 0.27 | 1.29 | 57 |
| stroke 308 | 55 % → 73 % | 1227.8 px | 0.31 | 1.32 | 211 |
| stroke 309 | 58 % → 80 % | 3526.7 px | 0.36 | 1.39 | 31 |
| stroke 310 | 59 % → 84 % | 1418.7 px | 0.42 | 1.41 | 114 |
| stroke 311 | 58 % → 83 % | 2483.5 px | 0.43 | 1.43 | 48 |
| stroke 312 | 79 % → 76 % | 1105.1 px | 0.12 | 0.96 | 308 |
| stroke 313 | 81 % → 78 % | 1854.9 px | 0.12 | 0.96 | 234 |
| stroke 314 | 78 % → 78 % | 929.0 px | 0.13 | 0.99 | 492 |
| stroke 315 | 78 % → 76 % | 1445.9 px | 0.13 | 0.98 | 234 |
| stroke 316 | 78 % → 75 % | 1826.0 px | 0.13 | 0.97 | 199 |
| stroke 317 | 74 % → 90 % | 4110.8 px | 0.34 | 1.23 | 84 |
| stroke 318 | 76 % → 91 % | 1104.7 px | 0.32 | 1.20 | 630 |
| stroke 319 | 88 % → 95 % | 1273.3 px | 0.25 | 1.07 | 650 |
| stroke 320 | 85 % → 92 % | 2240.0 px | 0.29 | 1.09 | 218 |
| stroke 321 | 78 % → 90 % | 1896.1 px | 0.35 | 1.16 | 234 |
| stroke 322 | 69 % → 86 % | 1091.0 px | 0.39 | 1.25 | 711 |
| stroke 323 | 84 % → 92 % | 4701.3 px | 0.34 | 1.09 | 87 |
| stroke 324 | 67 % → 86 % | 2502.0 px | 0.39 | 1.30 | 196 |
| stroke 325 | 82 % → 90 % | 4092.9 px | 0.34 | 1.09 | 466 |
| stroke 326 | 87 % → 95 % | 4324.2 px | 0.29 | 1.09 | 450 |
| stroke 327 | 84 % → 93 % | 4150.2 px | 0.33 | 1.11 | 186 |
| stroke 328 | 91 % → 94 % | 2077.1 px | 0.23 | 1.03 | 884 |
| stroke 329 | 69 % → 88 % | 3066.1 px | 0.39 | 1.28 | 179 |
| stroke 330 | 90 % → 95 % | 2572.3 px | 0.25 | 1.06 | 263 |
| stroke 331 | 80 % → 91 % | 3925.3 px | 0.35 | 1.14 | 156 |
| stroke 332 | 82 % → 85 % | 1711.5 px | 0.17 | 1.03 | 2713 |
| stroke 333 | 82 % → 84 % | 1198.1 px | 0.21 | 1.02 | 1207 |
| stroke 334 | 75 % → 79 % | 1027.0 px | 0.23 | 1.06 | 1251 |
| stroke 335 | 78 % → 79 % | 1050.5 px | 0.20 | 1.02 | 1000 |
| stroke 336 | 71 % → 81 % | 1153.5 px | 0.27 | 1.13 | 785 |
| stroke 337 | 62 % → 75 % | 1907.9 px | 0.29 | 1.21 | 248 |
| stroke 338 | 69 % → 79 % | 1426.6 px | 0.27 | 1.15 | 323 |
| stroke 339 | 83 % → 90 % | 2832.1 px | 0.35 | 1.09 | 139 |
| stroke 340 | 86 % → 92 % | 2637.4 px | 0.32 | 1.06 | 207 |
| stroke 341 | 74 % → 89 % | 1359.7 px | 0.41 | 1.21 | 417 |
| stroke 342 | 87 % → 91 % | 2970.5 px | 0.34 | 1.05 | 131 |
| stroke 343 | 89 % → 91 % | 2403.6 px | 0.31 | 1.03 | 292 |
| stroke 344 | 74 % → 89 % | 3101.7 px | 0.41 | 1.21 | 216 |
| stroke 345 | 88 % → 92 % | 1563.7 px | 0.35 | 1.04 | 377 |
| stroke 346 | 81 % → 92 % | 3027.3 px | 0.41 | 1.13 | 140 |
| stroke 347 | 92 % → 92 % | 5123.5 px | 0.30 | 1.00 | 93 |
| stroke 348 | 83 % → 92 % | 2084.2 px | 0.39 | 1.10 | 281 |
| stroke 349 | 64 % → 79 % | 1040.0 px | 0.40 | 1.24 | 482 |
| stroke 350 | 58 % → 76 % | 927.5 px | 0.41 | 1.31 | 790 |
| stroke 351 | 67 % → 77 % | 591.9 px | 0.43 | 1.15 | 619 |
| stroke 352 | 51 % → 64 % | 345.2 px | 0.40 | 1.25 | 468 |
| stroke 353 | 70 % → 83 % | 2516.2 px | 0.43 | 1.18 | 96 |
| stroke 354 | 61 % → 73 % | 736.4 px | 0.42 | 1.20 | 334 |
| stroke 355 | 73 % → 78 % | 867.2 px | 0.41 | 1.07 | 438 |
| stroke 356 | 73 % → 79 % | 1444.7 px | 0.39 | 1.08 | 718 |
| stroke 357 | 70 % → 76 % | 1994.5 px | 0.42 | 1.08 | 167 |
| stroke 358 | 64 % → 66 % | 704.7 px | 0.33 | 1.02 | 373 |
| stroke 359 | 76 % → 78 % | 1228.8 px | 0.40 | 1.03 | 425 |
| stroke 360 | 59 % → 61 % | 835.9 px | 0.36 | 1.04 | 157 |
| stroke 361 | 75 % → 79 % | 1820.4 px | 0.44 | 1.05 | 143 |
| stroke 362 | 71 % → 71 % | 1154.3 px | 0.40 | 1.01 | 332 |
| stroke 363 | 75 % → 77 % | 1678.5 px | 0.42 | 1.03 | 217 |
| stroke 364 | 76 % → 76 % | 724.9 px | 0.43 | 1.00 | 307 |
| stroke 365 | 80 % → 80 % | 1788.9 px | 0.40 | 1.00 | 270 |
| stroke 366 | 63 % → 64 % | 1175.9 px | 0.38 | 1.00 | 185 |
| stroke 367 | 77 % → 77 % | 3675.3 px | 0.40 | 1.00 | 93 |
| stroke 368 | 66 % → 65 % | 1304.7 px | 0.32 | 0.98 | 268 |
| stroke 369 | 61 % → 60 % | 1714.5 px | 0.33 | 0.98 | 98 |
| stroke 370 | 85 % → 85 % | 3753.6 px | 0.42 | 1.00 | 106 |
| stroke 371 | 80 % → 80 % | 2904.5 px | 0.39 | 1.00 | 158 |
| stroke 372 | 79 % → 78 % | 3044.4 px | 0.15 | 0.98 | 26 |
| stroke 373 | 83 % → 82 % | 1859.3 px | 0.21 | 0.98 | 96 |
| stroke 374 | 92 % → 91 % | 1294.7 px | 0.26 | 0.99 | 714 |
| stroke 375 | 94 % → 94 % | 4473.5 px | 0.27 | 0.99 | 133 |

Numbers say: wet paint spreads well beyond the stroke.

## Refs v3 · #02 HW cream strokes — own sheet
own sheet 800 × 650 · Gouache 1.00 + turpentine 30 % · 51 px · 699.6 s

![Refs v3 · #02 HW cream strokes — own sheet](Refs-v3-02-HW-cream-strokes-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 6 % → 57 % | 49.8 px | 0.14 | 8.97 | 302 |
| stroke 2 | 10 % → 54 % | 60.0 px | 0.14 | 5.19 | 842 |
| stroke 3 | 17 % → 45 % | 172.0 px | 0.12 | 2.70 | 288 |
| stroke 4 | 4 % → 97 % | 52.6 px | 0.27 | 23.34 | 198 |
| stroke 5 | 13 % → 85 % | 65.7 px | 0.22 | 6.77 | 638 |
| stroke 6 | 22 % → 74 % | 117.2 px | 0.16 | 3.30 | 620 |
| stroke 7 | 28 % → 78 % | 203.7 px | 0.12 | 2.82 | 427 |
| stroke 8 | 29 % → 66 % | 163.9 px | 0.12 | 2.28 | 663 |
| stroke 9 | 32 % → 81 % | 198.1 px | 0.20 | 2.54 | 475 |
| stroke 10 | 23 % → 62 % | 133.7 px | 0.14 | 2.68 | 480 |
| stroke 11 | 34 % → 87 % | 215.5 px | 0.19 | 2.57 | 614 |
| stroke 12 | 6 % → 94 % | 65.0 px | 0.19 | 16.82 | 191 |
| stroke 13 | 16 % → 76 % | 71.8 px | 0.17 | 4.76 | 865 |
| stroke 14 | 25 % → 79 % | 184.8 px | 0.17 | 3.19 | 460 |
| stroke 15 | 28 % → 95 % | 145.0 px | 0.18 | 3.40 | 627 |
| stroke 16 | 20 % → 95 % | 106.3 px | 0.19 | 4.79 | 859 |
| stroke 17 | 34 % → 96 % | 292.8 px | 0.19 | 2.83 | 401 |
| stroke 18 | 8 % → 96 % | 49.0 px | 0.11 | 11.82 | 531 |
| stroke 19 | 15 % → 95 % | 76.1 px | 0.15 | 6.32 | 750 |
| stroke 20 | 26 % → 94 % | 150.7 px | 0.17 | 3.60 | 731 |
| stroke 21 | 17 % → 93 % | 151.4 px | 0.24 | 5.60 | 300 |
| stroke 22 | 30 % → 90 % | 161.5 px | 0.14 | 2.98 | 710 |
| stroke 23 | 32 % → 87 % | 135.4 px | 0.12 | 2.74 | 1054 |
| stroke 24 | 34 % → 88 % | 169.7 px | 0.13 | 2.57 | 1048 |
| stroke 25 | 39 % → 95 % | 324.3 px | 0.14 | 2.41 | 521 |
| stroke 26 | 33 % → 86 % | 294.8 px | 0.14 | 2.63 | 277 |
| stroke 27 | 8 % → 55 % | 50.1 px | 0.16 | 7.10 | 641 |
| stroke 28 | 15 % → 68 % | 64.6 px | 0.20 | 4.64 | 1421 |
| stroke 29 | 23 % → 79 % | 91.5 px | 0.21 | 3.39 | 1543 |
| stroke 30 | 16 % → 90 % | 108.1 px | 0.28 | 5.71 | 605 |
| stroke 31 | 29 % → 79 % | 196.8 px | 0.22 | 2.75 | 661 |
| stroke 32 | 33 % → 85 % | 196.6 px | 0.22 | 2.61 | 1720 |
| stroke 33 | 30 % → 91 % | 201.6 px | 0.25 | 3.08 | 1466 |
| stroke 34 | 40 % → 84 % | 156.7 px | 0.21 | 2.11 | 5708 |
| stroke 35 | 44 % → 92 % | 320.5 px | 0.20 | 2.09 | 1363 |
| stroke 36 | 43 % → 62 % | 399.7 px | 0.13 | 1.43 | 767 |
| stroke 37 | 38 % → 95 % | 484.3 px | 0.23 | 2.49 | 598 |
| stroke 38 | 48 % → 90 % | 594.4 px | 0.21 | 1.90 | 502 |
| stroke 39 | 24 % → 73 % | 109.8 px | 0.21 | 3.01 | 1806 |
| stroke 40 | 37 % → 85 % | 242.7 px | 0.16 | 2.27 | 1258 |
| stroke 41 | 26 % → 58 % | 119.9 px | 0.20 | 2.22 | 1863 |
| stroke 42 | 33 % → 84 % | 313.4 px | 0.25 | 2.52 | 1075 |
| stroke 43 | 19 % → 97 % | 351.6 px | 0.19 | 5.01 | 98 |
| stroke 44 | 42 % → 58 % | 215.3 px | 0.20 | 1.40 | 746 |
| stroke 45 | 32 % → 87 % | 242.2 px | 0.15 | 2.73 | 313 |
| stroke 46 | 37 % → 76 % | 172.7 px | 0.17 | 2.06 | 685 |
| stroke 47 | 33 % → 62 % | 203.5 px | 0.16 | 1.86 | 539 |
| stroke 48 | 39 % → 74 % | 207.4 px | 0.18 | 1.92 | 803 |
| stroke 49 | 50 % → 79 % | 492.5 px | 0.14 | 1.57 | 311 |
| stroke 50 | 42 % → 76 % | 233.7 px | 0.18 | 1.80 | 544 |
| stroke 51 | 50 % → 73 % | 625.8 px | 0.18 | 1.45 | 101 |
| stroke 52 | 44 % → 78 % | 450.6 px | 0.20 | 1.80 | 164 |
| stroke 53 | 50 % → 82 % | 334.7 px | 0.15 | 1.66 | 426 |
| stroke 54 | 47 % → 74 % | 285.3 px | 0.15 | 1.58 | 410 |
| stroke 55 | 55 % → 76 % | 400.2 px | 0.17 | 1.38 | 517 |
| stroke 56 | 51 % → 70 % | 506.9 px | 0.12 | 1.38 | 167 |
| stroke 57 | 55 % → 74 % | 808.6 px | 0.18 | 1.34 | 137 |
| stroke 58 | 44 % → 82 % | 455.0 px | 0.19 | 1.87 | 264 |
| stroke 59 | 49 % → 67 % | 703.4 px | 0.14 | 1.38 | 126 |
| stroke 60 | 56 % → 68 % | 643.0 px | 0.15 | 1.22 | 192 |
| stroke 61 | 52 % → 75 % | 785.8 px | 0.19 | 1.45 | 135 |
| stroke 62 | 64 % → 89 % | 896.6 px | 0.13 | 1.39 | 164 |
| stroke 63 | 56 % → 69 % | 479.3 px | 0.16 | 1.23 | 246 |
| stroke 64 | 55 % → 90 % | 501.8 px | 0.17 | 1.64 | 297 |
| stroke 65 | 56 % → 74 % | 467.1 px | 0.16 | 1.34 | 232 |
| stroke 66 | 54 % → 70 % | 628.6 px | 0.14 | 1.31 | 205 |
| stroke 67 | 59 % → 72 % | 755.8 px | 0.13 | 1.21 | 134 |
| stroke 68 | 49 % → 87 % | 765.8 px | 0.19 | 1.78 | 170 |
| stroke 69 | 50 % → 96 % | 390.9 px | 0.22 | 1.93 | 425 |
| stroke 70 | 51 % → 95 % | 532.7 px | 0.22 | 1.87 | 254 |
| stroke 71 | 39 % → 86 % | 220.8 px | 0.27 | 2.24 | 644 |
| stroke 72 | 49 % → 84 % | 394.7 px | 0.23 | 1.71 | 251 |
| stroke 73 | 45 % → 86 % | 389.9 px | 0.26 | 1.91 | 246 |
| stroke 74 | 51 % → 95 % | 643.7 px | 0.22 | 1.85 | 179 |
| stroke 75 | 48 % → 98 % | 549.6 px | 0.27 | 2.03 | 122 |
| stroke 76 | 62 % → 96 % | 507.5 px | 0.20 | 1.54 | 415 |
| stroke 77 | 48 % → 97 % | 568.4 px | 0.28 | 2.02 | 216 |
| stroke 78 | 56 % → 95 % | 515.0 px | 0.22 | 1.69 | 399 |
| stroke 79 | 49 % → 97 % | 527.2 px | 0.28 | 1.98 | 259 |
| stroke 80 | 52 % → 82 % | 673.7 px | 0.24 | 1.59 | 187 |
| stroke 81 | 60 % → 95 % | 656.7 px | 0.21 | 1.58 | 216 |
| stroke 82 | 54 % → 94 % | 767.4 px | 0.24 | 1.75 | 200 |
| stroke 83 | 38 % → 75 % | 379.3 px | 0.16 | 1.97 | 181 |
| stroke 84 | 44 % → 69 % | 254.9 px | 0.14 | 1.57 | 267 |
| stroke 85 | 32 % → 55 % | 296.4 px | 0.17 | 1.71 | 135 |
| stroke 86 | 44 % → 74 % | 590.9 px | 0.17 | 1.68 | 155 |
| stroke 87 | 43 % → 68 % | 524.2 px | 0.16 | 1.56 | 124 |
| stroke 88 | 63 % → 96 % | 945.5 px | 0.14 | 1.54 | 81 |
| stroke 89 | 62 % → 95 % | 335.7 px | 0.19 | 1.53 | 477 |
| stroke 90 | 63 % → 94 % | 408.8 px | 0.19 | 1.50 | 319 |
| stroke 91 | 66 % → 94 % | 691.3 px | 0.20 | 1.41 | 155 |
| stroke 92 | 71 % → 94 % | 969.6 px | 0.17 | 1.32 | 124 |
| stroke 93 | 62 % → 79 % | 303.2 px | 0.08 | 1.28 | 423 |
| stroke 94 | 58 % → 90 % | 309.4 px | 0.17 | 1.57 | 755 |
| stroke 95 | 80 % → 97 % | 900.1 px | 0.08 | 1.21 | 182 |
| stroke 96 | 53 % → 65 % | 373.1 px | 0.10 | 1.24 | 267 |
| stroke 97 | 61 % → 72 % | 428.9 px | 0.08 | 1.18 | 339 |
| stroke 98 | 65 % → 85 % | 329.4 px | 0.11 | 1.31 | 519 |
| stroke 99 | 45 % → 91 % | 504.3 px | 0.27 | 2.02 | 185 |
| stroke 100 | 63 % → 86 % | 421.3 px | 0.12 | 1.37 | 416 |
| stroke 101 | 44 % → 89 % | 408.9 px | 0.30 | 2.00 | 292 |
| stroke 102 | 69 % → 85 % | 649.3 px | 0.10 | 1.23 | 263 |
| stroke 103 | 84 % → 93 % | 1019.9 px | 0.09 | 1.11 | 141 |
| stroke 104 | 78 % → 94 % | 474.9 px | 0.12 | 1.20 | 509 |
| stroke 105 | 72 % → 79 % | 971.0 px | 0.09 | 1.09 | 194 |
| stroke 106 | 57 % → 90 % | 773.8 px | 0.23 | 1.57 | 142 |
| stroke 107 | 62 % → 67 % | 619.2 px | 0.07 | 1.07 | 202 |
| stroke 108 | 55 % → 81 % | 519.2 px | 0.15 | 1.46 | 140 |
| stroke 109 | 66 % → 93 % | 820.9 px | 0.18 | 1.41 | 151 |
| stroke 110 | 74 % → 77 % | 867.5 px | 0.07 | 1.04 | 309 |
| stroke 111 | 91 % → 95 % | 1358.5 px | 0.08 | 1.05 | 143 |
| stroke 112 | 90 % → 98 % | 1366.0 px | 0.09 | 1.09 | 116 |
| stroke 113 | 57 % → 85 % | 485.0 px | 0.17 | 1.50 | 154 |
| stroke 114 | 66 % → 94 % | 334.4 px | 0.19 | 1.42 | 521 |
| stroke 115 | 46 % → 86 % | 335.0 px | 0.28 | 1.88 | 301 |
| stroke 116 | 48 % → 51 % | 810.9 px | 0.07 | 1.06 | 46 |
| stroke 117 | 72 % → 92 % | 353.5 px | 0.17 | 1.28 | 572 |
| stroke 118 | 70 % → 87 % | 662.1 px | 0.19 | 1.24 | 208 |
| stroke 119 | 62 % → 76 % | 415.2 px | 0.15 | 1.23 | 376 |
| stroke 120 | 66 % → 77 % | 368.4 px | 0.18 | 1.18 | 589 |
| stroke 121 | 68 % → 80 % | 609.5 px | 0.19 | 1.17 | 273 |
| stroke 122 | 70 % → 81 % | 409.4 px | 0.17 | 1.15 | 479 |
| stroke 123 | 65 % → 82 % | 872.2 px | 0.15 | 1.25 | 219 |
| stroke 124 | 59 % → 69 % | 907.1 px | 0.14 | 1.17 | 161 |
| stroke 125 | 78 % → 88 % | 709.5 px | 0.18 | 1.13 | 293 |
| stroke 126 | 66 % → 73 % | 448.9 px | 0.17 | 1.12 | 413 |
| stroke 127 | 65 % → 75 % | 861.6 px | 0.19 | 1.16 | 391 |
| stroke 128 | 73 % → 82 % | 662.4 px | 0.17 | 1.13 | 485 |
| stroke 129 | 63 % → 79 % | 299.8 px | 0.13 | 1.26 | 692 |
| stroke 130 | 78 % → 90 % | 403.5 px | 0.13 | 1.15 | 714 |
| stroke 131 | 81 % → 87 % | 427.4 px | 0.15 | 1.07 | 754 |
| stroke 132 | 88 % → 96 % | 769.7 px | 0.19 | 1.08 | 303 |
| stroke 133 | 84 % → 89 % | 519.6 px | 0.16 | 1.06 | 595 |
| stroke 134 | 83 % → 89 % | 500.8 px | 0.14 | 1.06 | 391 |
| stroke 135 | 91 % → 93 % | 796.3 px | 0.14 | 1.03 | 235 |
| stroke 136 | 84 % → 95 % | 784.0 px | 0.20 | 1.13 | 203 |
| stroke 137 | 83 % → 83 % | 560.9 px | 0.13 | 1.01 | 325 |
| stroke 138 | 88 % → 88 % | 1318.0 px | 0.15 | 1.00 | 142 |
| stroke 139 | 90 % → 91 % | 507.9 px | 0.13 | 1.01 | 482 |
| stroke 140 | 80 % → 81 % | 512.7 px | 0.13 | 1.00 | 329 |
| stroke 141 | 91 % → 97 % | 1370.4 px | 0.18 | 1.06 | 139 |
| stroke 142 | 76 % → 76 % | 527.7 px | 0.16 | 1.00 | 320 |
| stroke 143 | 84 % → 84 % | 1278.9 px | 0.16 | 1.00 | 124 |
| stroke 144 | 86 % → 87 % | 793.9 px | 0.13 | 1.02 | 156 |
| stroke 145 | 82 % → 95 % | 920.6 px | 0.21 | 1.15 | 175 |
| stroke 146 | 52 % → 86 % | 419.4 px | 0.27 | 1.68 | 276 |
| stroke 147 | 61 % → 94 % | 822.2 px | 0.25 | 1.55 | 104 |
| stroke 148 | 60 % → 95 % | 912.7 px | 0.26 | 1.58 | 117 |
| stroke 149 | 52 % → 86 % | 451.3 px | 0.27 | 1.65 | 316 |
| stroke 150 | 58 % → 72 % | 597.2 px | 0.22 | 1.23 | 64 |
| stroke 151 | 66 % → 70 % | 1099.4 px | 0.19 | 1.06 | 33 |
| stroke 152 | 63 % → 76 % | 623.9 px | 0.19 | 1.21 | 90 |
| stroke 153 | 66 % → 95 % | 605.9 px | 0.24 | 1.44 | 248 |
| stroke 154 | 60 % → 98 % | 1082.7 px | 0.27 | 1.63 | 59 |
| stroke 155 | 70 % → 95 % | 384.6 px | 0.19 | 1.36 | 618 |
| stroke 156 | 81 % → 82 % | 441.9 px | 0.09 | 1.02 | 340 |
| stroke 157 | 88 % → 95 % | 529.8 px | 0.10 | 1.08 | 355 |
| stroke 158 | 14 % → 43 % | 21.0 px | 0.53 | 3.05 | 1319 |
| stroke 159 | 78 % → 88 % | 518.4 px | 0.14 | 1.11 | 419 |
| stroke 160 | 78 % → 86 % | 544.2 px | 0.14 | 1.10 | 793 |
| stroke 161 | 84 % → 95 % | 834.0 px | 0.17 | 1.13 | 293 |
| stroke 162 | 88 % → 97 % | 1054.9 px | 0.17 | 1.10 | 233 |
| stroke 163 | 66 % → 86 % | 293.1 px | 0.22 | 1.31 | 580 |
| stroke 164 | 80 % → 95 % | 443.3 px | 0.25 | 1.19 | 536 |
| stroke 165 | 74 % → 86 % | 377.9 px | 0.22 | 1.17 | 643 |
| stroke 166 | 79 % → 94 % | 462.6 px | 0.17 | 1.19 | 518 |
| stroke 167 | 84 % → 91 % | 441.7 px | 0.21 | 1.08 | 743 |
| stroke 168 | 90 % → 95 % | 484.4 px | 0.22 | 1.05 | 1098 |
| stroke 169 | 93 % → 94 % | 802.2 px | 0.17 | 1.01 | 386 |
| stroke 170 | 93 % → 96 % | 758.1 px | 0.25 | 1.02 | 513 |
| stroke 171 | 85 % → 87 % | 413.2 px | 0.23 | 1.02 | 664 |
| stroke 172 | 94 % → 96 % | 995.6 px | 0.23 | 1.02 | 204 |
| stroke 173 | 92 % → 92 % | 1125.5 px | 0.17 | 1.00 | 229 |
| stroke 174 | 86 % → 95 % | 582.3 px | 0.18 | 1.11 | 707 |
| stroke 175 | 96 % → 98 % | 1478.8 px | 0.24 | 1.02 | 118 |
| stroke 176 | 95 % → 96 % | 804.2 px | 0.27 | 1.01 | 327 |
| stroke 177 | 92 % → 95 % | 1414.1 px | 0.21 | 1.03 | 149 |
| stroke 178 | 68 % → 71 % | 274.3 px | 0.18 | 1.05 | 376 |
| stroke 179 | 68 % → 69 % | 515.6 px | 0.21 | 1.01 | 153 |
| stroke 180 | 96 % → 95 % | 679.5 px | 0.13 | 1.00 | 347 |
| stroke 181 | 79 % → 79 % | 590.9 px | 0.08 | 1.00 | 232 |
| stroke 182 | 58 % → 81 % | 256.9 px | 0.34 | 1.40 | 3198 |
| stroke 183 | 66 % → 74 % | 341.3 px | 0.36 | 1.12 | 1307 |
| stroke 184 | 72 % → 76 % | 271.3 px | 0.45 | 1.06 | 2144 |
| stroke 185 | 68 % → 67 % | 182.3 px | 0.57 | 0.98 | 2902 |
| stroke 186 | 87 % → 86 % | 461.8 px | 0.40 | 0.99 | 1391 |
| stroke 187 | 86 % → 84 % | 393.2 px | 0.56 | 0.98 | 1112 |

Numbers say: wet paint spreads well beyond the stroke.

## Refs v3 · #03 HW navy contours — own sheet
own sheet 800 × 600 · Gouache 1.00 + turpentine 30 % · 80 px · 497.2 s

![Refs v3 · #03 HW navy contours — own sheet](Refs-v3-03-HW-navy-contours-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 6 % → 88 % | 77.8 px | 0.49 | 14.54 | 1051 |
| stroke 2 | 13 % → 83 % | 108.5 px | 0.48 | 6.57 | 2868 |
| stroke 3 | 23 % → 87 % | 186.1 px | 0.50 | 3.81 | 2626 |
| stroke 4 | 24 % → 77 % | 224.9 px | 0.48 | 3.26 | 2057 |
| stroke 5 | 28 % → 85 % | 279.5 px | 0.50 | 3.05 | 2367 |
| stroke 6 | 36 % → 92 % | 440.0 px | 0.50 | 2.59 | 2482 |
| stroke 7 | 31 % → 88 % | 324.1 px | 0.49 | 2.85 | 2517 |
| stroke 8 | 40 % → 76 % | 667.8 px | 0.43 | 1.89 | 998 |
| stroke 9 | 22 % → 67 % | 186.7 px | 0.54 | 3.04 | 1847 |
| stroke 10 | 30 % → 70 % | 354.4 px | 0.53 | 2.32 | 1124 |
| stroke 11 | 35 % → 66 % | 548.1 px | 0.51 | 1.85 | 927 |
| stroke 12 | 35 % → 67 % | 442.4 px | 0.54 | 1.90 | 1782 |
| stroke 13 | 19 % → 79 % | 326.0 px | 0.47 | 4.25 | 784 |
| stroke 14 | 10 % → 93 % | 88.8 px | 0.47 | 9.63 | 149 |
| stroke 15 | 3 % → 30 % | 28.3 px | 0.22 | 8.97 | 193 |
| stroke 16 | 16 % → 93 % | 118.9 px | 0.48 | 5.88 | 257 |
| stroke 17 | 9 % → 68 % | 80.4 px | 0.44 | 7.80 | 149 |
| stroke 18 | 10 % → 36 % | 69.7 px | 0.32 | 3.48 | 250 |
| stroke 19 | 14 % → 55 % | 99.7 px | 0.40 | 3.88 | 390 |
| stroke 20 | 16 % → 53 % | 177.1 px | 0.44 | 3.25 | 178 |
| stroke 21 | 15 % → 75 % | 198.8 px | 0.48 | 4.92 | 63 |
| stroke 22 | 18 % → 87 % | 144.5 px | 0.47 | 4.79 | 121 |
| stroke 23 | 20 % → 93 % | 452.7 px | 0.47 | 4.69 | 54 |
| stroke 24 | 9 % → 35 % | 53.3 px | 0.40 | 3.85 | 327 |
| stroke 25 | 10 % → 36 % | 80.7 px | 0.42 | 3.42 | 382 |
| stroke 26 | 26 % → 90 % | 160.9 px | 0.45 | 3.50 | 309 |
| stroke 27 | 16 % → 31 % | 123.5 px | 0.28 | 1.95 | 324 |
| stroke 28 | 24 % → 92 % | 263.3 px | 0.45 | 3.77 | 156 |
| stroke 29 | 21 % → 38 % | 185.9 px | 0.36 | 1.81 | 327 |
| stroke 30 | 16 % → 81 % | 148.0 px | 0.46 | 4.98 | 242 |
| stroke 31 | 14 % → 39 % | 183.0 px | 0.44 | 2.82 | 155 |
| stroke 32 | 30 % → 90 % | 368.2 px | 0.47 | 2.97 | 78 |
| stroke 33 | 30 % → 82 % | 563.8 px | 0.47 | 2.71 | 59 |
| stroke 34 | 29 % → 90 % | 276.7 px | 0.45 | 3.06 | 171 |
| stroke 35 | 19 % → 77 % | 214.5 px | 0.49 | 4.04 | 72 |
| stroke 36 | 28 % → 92 % | 223.7 px | 0.45 | 3.31 | 268 |
| stroke 37 | 20 % → 81 % | 207.3 px | 0.48 | 4.14 | 191 |
| stroke 38 | 34 % → 84 % | 429.1 px | 0.47 | 2.49 | 111 |
| stroke 39 | 21 % → 81 % | 173.6 px | 0.48 | 3.78 | 174 |
| stroke 40 | 27 % → 94 % | 430.6 px | 0.49 | 3.49 | 200 |
| stroke 41 | 23 % → 82 % | 384.4 px | 0.47 | 3.66 | 128 |
| stroke 42 | 19 % → 25 % | 301.9 px | 0.21 | 1.31 | 117 |
| stroke 43 | 30 % → 94 % | 350.3 px | 0.47 | 3.13 | 214 |
| stroke 44 | 17 % → 35 % | 105.6 px | 0.38 | 2.07 | 282 |
| stroke 45 | 28 % → 62 % | 750.6 px | 0.43 | 2.21 | 60 |
| stroke 46 | 14 % → 41 % | 163.5 px | 0.49 | 2.92 | 113 |
| stroke 47 | 33 % → 91 % | 718.5 px | 0.44 | 2.76 | 52 |
| stroke 48 | 30 % → 94 % | 664.2 px | 0.47 | 3.14 | 95 |
| stroke 49 | 31 % → 69 % | 620.1 px | 0.44 | 2.21 | 91 |
| stroke 50 | 33 % → 92 % | 771.4 px | 0.45 | 2.82 | 42 |
| stroke 51 | 38 % → 90 % | 775.2 px | 0.45 | 2.38 | 57 |
| stroke 52 | 30 % → 78 % | 1269.3 px | 0.46 | 2.57 | 72 |
| stroke 53 | 34 % → 73 % | 503.9 px | 0.46 | 2.13 | 397 |
| stroke 54 | 32 % → 79 % | 297.2 px | 0.53 | 2.51 | 886 |
| stroke 55 | 40 % → 87 % | 229.1 px | 0.51 | 2.14 | 890 |
| stroke 56 | 34 % → 80 % | 288.0 px | 0.54 | 2.34 | 1279 |
| stroke 57 | 45 % → 87 % | 320.5 px | 0.51 | 1.91 | 716 |
| stroke 58 | 48 % → 85 % | 342.6 px | 0.52 | 1.79 | 604 |
| stroke 59 | 34 % → 73 % | 1063.7 px | 0.48 | 2.12 | 176 |
| stroke 60 | 47 % → 82 % | 669.0 px | 0.54 | 1.77 | 236 |
| stroke 61 | 33 % → 64 % | 307.3 px | 0.54 | 1.93 | 967 |
| stroke 62 | 39 % → 60 % | 538.1 px | 0.56 | 1.56 | 304 |
| stroke 63 | 41 % → 61 % | 308.7 px | 0.54 | 1.49 | 899 |
| stroke 64 | 54 % → 81 % | 1093.3 px | 0.48 | 1.50 | 440 |
| stroke 65 | 45 % → 56 % | 764.8 px | 0.53 | 1.25 | 263 |
| stroke 66 | 40 % → 60 % | 738.8 px | 0.52 | 1.48 | 221 |
| stroke 67 | 49 % → 63 % | 347.7 px | 0.53 | 1.28 | 743 |
| stroke 68 | 48 % → 59 % | 1240.6 px | 0.54 | 1.23 | 216 |
| stroke 69 | 53 % → 74 % | 1537.5 px | 0.50 | 1.40 | 159 |
| stroke 70 | 48 % → 66 % | 571.6 px | 0.51 | 1.38 | 668 |
| stroke 71 | 49 % → 63 % | 679.9 px | 0.57 | 1.30 | 406 |
| stroke 72 | 55 % → 66 % | 1201.5 px | 0.51 | 1.19 | 270 |
| stroke 73 | 53 % → 61 % | 740.5 px | 0.46 | 1.15 | 666 |
| stroke 74 | 54 % → 72 % | 613.3 px | 0.50 | 1.35 | 661 |
| stroke 75 | 60 % → 63 % | 364.5 px | 0.51 | 1.05 | 697 |
| stroke 76 | 55 % → 60 % | 1321.6 px | 0.55 | 1.10 | 261 |
| stroke 77 | 70 % → 73 % | 1612.4 px | 0.58 | 1.05 | 223 |
| stroke 78 | 54 % → 58 % | 723.5 px | 0.46 | 1.08 | 505 |
| stroke 79 | 73 % → 75 % | 1217.2 px | 0.58 | 1.02 | 285 |
| stroke 80 | 59 % → 64 % | 1905.3 px | 0.45 | 1.08 | 162 |
| stroke 81 | 59 % → 61 % | 1487.4 px | 0.54 | 1.03 | 164 |
| stroke 82 | 62 % → 64 % | 751.0 px | 0.51 | 1.03 | 312 |
| stroke 83 | 58 % → 62 % | 1847.3 px | 0.46 | 1.07 | 144 |
| stroke 84 | 48 % → 88 % | 284.6 px | 0.48 | 1.84 | 696 |
| stroke 85 | 57 % → 88 % | 460.9 px | 0.51 | 1.53 | 729 |
| stroke 86 | 55 % → 91 % | 1008.6 px | 0.51 | 1.65 | 222 |
| stroke 87 | 57 % → 85 % | 796.7 px | 0.50 | 1.50 | 329 |
| stroke 88 | 52 % → 69 % | 407.5 px | 0.44 | 1.33 | 472 |
| stroke 89 | 61 % → 90 % | 837.1 px | 0.47 | 1.48 | 311 |
| stroke 90 | 67 % → 90 % | 901.7 px | 0.48 | 1.35 | 320 |
| stroke 91 | 70 % → 93 % | 1237.8 px | 0.49 | 1.34 | 228 |
| stroke 92 | 63 % → 85 % | 1109.6 px | 0.48 | 1.36 | 256 |
| stroke 93 | 64 % → 85 % | 582.8 px | 0.50 | 1.32 | 594 |
| stroke 94 | 68 % → 86 % | 631.5 px | 0.49 | 1.27 | 718 |
| stroke 95 | 70 % → 85 % | 1100.6 px | 0.51 | 1.20 | 474 |
| stroke 96 | 68 % → 86 % | 738.4 px | 0.51 | 1.28 | 469 |
| stroke 97 | 72 % → 91 % | 2080.7 px | 0.49 | 1.26 | 148 |
| stroke 98 | 64 % → 82 % | 805.7 px | 0.53 | 1.28 | 896 |
| stroke 99 | 76 % → 90 % | 1546.6 px | 0.48 | 1.18 | 263 |
| stroke 100 | 73 % → 84 % | 1567.3 px | 0.49 | 1.15 | 278 |
| stroke 101 | 76 % → 87 % | 1928.5 px | 0.52 | 1.14 | 177 |
| stroke 102 | 66 % → 88 % | 1135.4 px | 0.50 | 1.34 | 279 |
| stroke 103 | 64 % → 88 % | 1845.9 px | 0.52 | 1.37 | 144 |
| stroke 104 | 73 % → 83 % | 1516.6 px | 0.48 | 1.13 | 255 |
| stroke 105 | 65 % → 86 % | 800.9 px | 0.52 | 1.32 | 359 |
| stroke 106 | 85 % → 90 % | 1442.9 px | 0.49 | 1.07 | 259 |
| stroke 107 | 75 % → 90 % | 1720.4 px | 0.50 | 1.20 | 237 |
| stroke 108 | 80 % → 87 % | 2459.9 px | 0.47 | 1.09 | 167 |
| stroke 109 | 87 % → 93 % | 2145.5 px | 0.49 | 1.06 | 124 |
| stroke 110 | 71 % → 86 % | 2029.7 px | 0.52 | 1.20 | 102 |
| stroke 111 | 51 % → 56 % | 1568.4 px | 0.43 | 1.08 | 86 |
| stroke 112 | 68 % → 75 % | 723.2 px | 0.46 | 1.10 | 784 |
| stroke 113 | 61 % → 63 % | 1725.8 px | 0.43 | 1.04 | 177 |
| stroke 114 | 61 % → 66 % | 875.6 px | 0.45 | 1.09 | 357 |
| stroke 115 | 70 % → 77 % | 2427.5 px | 0.45 | 1.10 | 133 |
| stroke 116 | 62 % → 62 % | 1054.2 px | 0.46 | 1.01 | 268 |
| stroke 117 | 59 % → 96 % | 1723.3 px | 0.49 | 1.62 | 78 |
| stroke 118 | 57 % → 86 % | 911.2 px | 0.48 | 1.50 | 325 |
| stroke 119 | 48 % → 54 % | 2066.9 px | 0.54 | 1.13 | 23 |
| stroke 120 | 55 % → 65 % | 2413.0 px | 0.51 | 1.20 | 50 |
| stroke 121 | 64 % → 64 % | 1628.7 px | 0.56 | 1.00 | 50 |
| stroke 122 | 77 % → 90 % | 2804.0 px | 0.46 | 1.16 | 65 |
| stroke 123 | 71 % → 72 % | 1484.4 px | 0.56 | 1.01 | 88 |
| stroke 124 | 68 % → 69 % | 1042.1 px | 0.58 | 1.02 | 118 |
| stroke 125 | 71 % → 72 % | 2951.5 px | 0.52 | 1.02 | 54 |
| stroke 126 | 68 % → 85 % | 464.0 px | 0.52 | 1.25 | 2209 |
| stroke 127 | 76 % → 88 % | 670.9 px | 0.51 | 1.15 | 914 |
| stroke 128 | 75 % → 79 % | 349.2 px | 0.55 | 1.05 | 2748 |
| stroke 129 | 84 % → 87 % | 619.8 px | 0.51 | 1.03 | 3369 |
| stroke 130 | 79 % → 80 % | 356.3 px | 0.57 | 1.01 | 1911 |
| stroke 131 | 92 % → 93 % | 897.4 px | 0.53 | 1.01 | 893 |
| stroke 132 | 84 % → 84 % | 747.9 px | 0.55 | 1.00 | 474 |
| stroke 133 | 86 % → 85 % | 983.3 px | 0.54 | 1.00 | 655 |
| stroke 134 | 70 % → 73 % | 627.8 px | 0.44 | 1.04 | 1767 |
| stroke 135 | 79 % → 79 % | 908.1 px | 0.46 | 1.00 | 1945 |
| stroke 136 | 55 % → 55 % | 930.7 px | 0.52 | 1.00 | 124 |

Numbers say: wet paint spreads well beyond the stroke.

## Refs v3 · #04 HW grey cloud — own sheet
own sheet 800 × 635 · Gouache 1.00 + turpentine 30 % · 93 px · 696.3 s

![Refs v3 · #04 HW grey cloud — own sheet](Refs-v3-04-HW-grey-cloud-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 14 % → 98 % | 83.8 px | 0.21 | 7.23 | 3082 |
| stroke 2 | 12 % → 97 % | 81.5 px | 0.19 | 7.92 | 3071 |
| stroke 3 | 25 % → 98 % | 245.1 px | 0.22 | 3.91 | 2214 |
| stroke 4 | 37 % → 97 % | 198.4 px | 0.22 | 2.66 | 5976 |
| stroke 5 | 33 % → 98 % | 328.5 px | 0.20 | 2.98 | 2607 |
| stroke 6 | 50 % → 97 % | 649.9 px | 0.19 | 1.96 | 1155 |
| stroke 7 | 40 % → 97 % | 600.7 px | 0.18 | 2.45 | 1362 |
| stroke 8 | 55 % → 98 % | 451.9 px | 0.23 | 1.81 | 1732 |
| stroke 9 | 65 % → 99 % | 533.1 px | 0.22 | 1.53 | 2439 |
| stroke 10 | 53 % → 97 % | 665.8 px | 0.18 | 1.82 | 1660 |
| stroke 11 | 35 % → 98 % | 438.5 px | 0.21 | 2.79 | 1484 |
| stroke 12 | 61 % → 98 % | 1012.1 px | 0.21 | 1.60 | 1251 |
| stroke 13 | 61 % → 98 % | 772.8 px | 0.23 | 1.60 | 1817 |
| stroke 14 | 67 % → 99 % | 711.0 px | 0.23 | 1.47 | 1098 |
| stroke 15 | 54 % → 99 % | 999.6 px | 0.20 | 1.83 | 1326 |
| stroke 16 | 59 % → 98 % | 699.8 px | 0.22 | 1.68 | 3048 |
| stroke 17 | 64 % → 98 % | 758.0 px | 0.22 | 1.54 | 3152 |
| stroke 18 | 41 % → 97 % | 370.8 px | 0.20 | 2.35 | 1529 |
| stroke 19 | 56 % → 98 % | 727.4 px | 0.21 | 1.74 | 1136 |
| stroke 20 | 76 % → 98 % | 816.7 px | 0.23 | 1.30 | 1931 |
| stroke 21 | 73 % → 99 % | 927.3 px | 0.22 | 1.35 | 1767 |
| stroke 22 | 58 % → 99 % | 1010.2 px | 0.21 | 1.71 | 1382 |
| stroke 23 | 40 % → 98 % | 822.8 px | 0.17 | 2.45 | 1026 |
| stroke 24 | 68 % → 98 % | 1110.8 px | 0.21 | 1.44 | 1130 |
| stroke 25 | 31 % → 99 % | 652.4 px | 0.17 | 3.25 | 751 |
| stroke 26 | 18 % → 97 % | 581.3 px | 0.17 | 5.44 | 59 |
| stroke 27 | 17 % → 95 % | 338.8 px | 0.16 | 5.49 | 52 |
| stroke 28 | 4 % → 93 % | 60.5 px | 0.14 | 22.70 | 41 |
| stroke 29 | 62 % → 98 % | 668.8 px | 0.21 | 1.58 | 2357 |
| stroke 30 | 51 % → 99 % | 470.8 px | 0.19 | 1.94 | 2565 |
| stroke 31 | 38 % → 97 % | 266.1 px | 0.15 | 2.59 | 2753 |
| stroke 32 | 36 % → 97 % | 313.5 px | 0.14 | 2.69 | 2535 |
| stroke 33 | 73 % → 98 % | 781.5 px | 0.21 | 1.34 | 1973 |
| stroke 34 | 80 % → 98 % | 983.2 px | 0.22 | 1.23 | 2571 |
| stroke 35 | 64 % → 99 % | 1553.2 px | 0.19 | 1.55 | 644 |
| stroke 36 | 77 % → 98 % | 1114.2 px | 0.21 | 1.29 | 1632 |
| stroke 37 | 41 % → 94 % | 427.5 px | 0.15 | 2.29 | 533 |
| stroke 38 | 88 % → 99 % | 1980.6 px | 0.23 | 1.13 | 864 |
| stroke 39 | 67 % → 99 % | 871.9 px | 0.19 | 1.49 | 1886 |
| stroke 40 | 55 % → 99 % | 959.1 px | 0.16 | 1.80 | 1025 |
| stroke 41 | 67 % → 98 % | 1122.0 px | 0.18 | 1.45 | 1062 |
| stroke 42 | 48 % → 97 % | 1134.6 px | 0.14 | 2.02 | 741 |
| stroke 43 | 88 % → 99 % | 1595.3 px | 0.23 | 1.12 | 621 |
| stroke 44 | 91 % → 99 % | 2428.7 px | 0.22 | 1.09 | 592 |
| stroke 45 | 55 % → 97 % | 474.7 px | 0.15 | 1.77 | 1774 |
| stroke 46 | 50 % → 99 % | 1067.4 px | 0.14 | 2.00 | 615 |
| stroke 47 | 71 % → 99 % | 1930.5 px | 0.18 | 1.39 | 570 |
| stroke 48 | 58 % → 99 % | 1543.1 px | 0.15 | 1.70 | 535 |
| stroke 49 | 65 % → 97 % | 1013.9 px | 0.17 | 1.49 | 618 |
| stroke 50 | 80 % → 98 % | 1814.7 px | 0.22 | 1.23 | 495 |
| stroke 51 | 50 % → 99 % | 1201.7 px | 0.14 | 1.99 | 503 |
| stroke 52 | 77 % → 98 % | 1676.7 px | 0.21 | 1.26 | 592 |
| stroke 53 | 74 % → 98 % | 825.7 px | 0.20 | 1.32 | 1643 |
| stroke 54 | 62 % → 96 % | 553.6 px | 0.18 | 1.56 | 1471 |
| stroke 55 | 79 % → 98 % | 796.2 px | 0.21 | 1.24 | 1933 |
| stroke 56 | 51 % → 95 % | 540.3 px | 0.16 | 1.87 | 637 |
| stroke 57 | 66 % → 96 % | 900.7 px | 0.18 | 1.46 | 1451 |
| stroke 58 | 75 % → 97 % | 2198.8 px | 0.20 | 1.29 | 98 |
| stroke 59 | 58 % → 96 % | 1344.7 px | 0.17 | 1.66 | 251 |
| stroke 60 | 81 % → 97 % | 425.4 px | 0.19 | 1.19 | 1768 |
| stroke 61 | 91 % → 99 % | 1477.0 px | 0.22 | 1.08 | 582 |
| stroke 62 | 93 % → 97 % | 446.0 px | 0.21 | 1.04 | 2366 |
| stroke 63 | 92 % → 96 % | 924.0 px | 0.19 | 1.05 | 812 |
| stroke 64 | 96 % → 98 % | 925.0 px | 0.21 | 1.02 | 1066 |
| stroke 65 | 92 % → 96 % | 1328.8 px | 0.19 | 1.04 | 386 |
| stroke 66 | 95 % → 97 % | 1495.2 px | 0.19 | 1.02 | 467 |
| stroke 67 | 95 % → 96 % | 770.2 px | 0.16 | 1.01 | 469 |
| stroke 68 | 96 % → 96 % | 923.7 px | 0.18 | 1.00 | 866 |
| stroke 69 | 96 % → 96 % | 1131.6 px | 0.17 | 1.00 | 527 |
| stroke 70 | 98 % → 98 % | 1593.3 px | 0.20 | 1.00 | 554 |
| stroke 71 | 75 % → 97 % | 806.3 px | 0.18 | 1.29 | 1239 |
| stroke 72 | 84 % → 98 % | 496.7 px | 0.21 | 1.17 | 1829 |
| stroke 73 | 85 % → 98 % | 908.8 px | 0.19 | 1.15 | 1288 |
| stroke 74 | 90 % → 99 % | 925.5 px | 0.22 | 1.09 | 908 |
| stroke 75 | 93 % → 98 % | 583.7 px | 0.21 | 1.05 | 593 |
| stroke 76 | 83 % → 97 % | 573.2 px | 0.18 | 1.16 | 1268 |
| stroke 77 | 98 % → 98 % | 783.4 px | 0.21 | 1.00 | 711 |
| stroke 78 | 98 % → 98 % | 533.8 px | 0.21 | 1.00 | 771 |
| stroke 79 | 81 % → 97 % | 1511.6 px | 0.18 | 1.20 | 568 |
| stroke 80 | 96 % → 98 % | 1107.3 px | 0.20 | 1.02 | 826 |
| stroke 81 | 97 % → 97 % | 1174.3 px | 0.20 | 1.00 | 481 |
| stroke 82 | 49 % → 96 % | 385.4 px | 0.13 | 1.94 | 1645 |
| stroke 83 | 63 % → 97 % | 662.9 px | 0.15 | 1.53 | 1956 |
| stroke 84 | 54 % → 95 % | 511.4 px | 0.13 | 1.76 | 1360 |
| stroke 85 | 61 % → 94 % | 557.8 px | 0.15 | 1.54 | 782 |
| stroke 86 | 62 % → 97 % | 796.6 px | 0.14 | 1.57 | 1391 |
| stroke 87 | 55 % → 95 % | 1352.4 px | 0.12 | 1.74 | 382 |
| stroke 88 | 71 % → 95 % | 1142.1 px | 0.15 | 1.35 | 569 |
| stroke 89 | 59 % → 92 % | 536.7 px | 0.11 | 1.56 | 555 |
| stroke 90 | 75 % → 93 % | 1324.9 px | 0.15 | 1.25 | 316 |
| stroke 91 | 75 % → 95 % | 1614.6 px | 0.15 | 1.28 | 436 |
| stroke 92 | 64 % → 98 % | 1970.3 px | 0.14 | 1.52 | 393 |
| stroke 93 | 68 % → 95 % | 1151.3 px | 0.14 | 1.40 | 659 |
| stroke 94 | 72 % → 94 % | 1130.7 px | 0.15 | 1.31 | 521 |
| stroke 95 | 62 % → 96 % | 779.5 px | 0.14 | 1.55 | 553 |
| stroke 96 | 64 % → 95 % | 863.5 px | 0.14 | 1.48 | 425 |
| stroke 97 | 76 % → 98 % | 333.3 px | 0.12 | 1.28 | 5989 |
| stroke 98 | 73 % → 96 % | 355.6 px | 0.09 | 1.31 | 3377 |
| stroke 99 | 92 % → 97 % | 591.8 px | 0.13 | 1.06 | 4109 |
| stroke 100 | 86 % → 95 % | 516.4 px | 0.11 | 1.11 | 4379 |
| stroke 101 | 96 % → 100 % | 1038.7 px | 0.10 | 1.03 | 1187 |
| stroke 102 | 88 % → 93 % | 443.2 px | 0.07 | 1.06 | 2936 |
| stroke 103 | 96 % → 96 % | 1025.3 px | 0.14 | 1.00 | 1681 |
| stroke 104 | 95 % → 95 % | 769.9 px | 0.11 | 1.00 | 3361 |
| stroke 105 | 96 % → 96 % | 774.1 px | 0.12 | 1.00 | 3826 |
| stroke 106 | 97 % → 96 % | 599.8 px | 0.12 | 0.99 | 1548 |
| stroke 107 | 100 % → 100 % | 1053.2 px | 0.13 | 1.00 | 2977 |
| stroke 108 | 96 % → 96 % | 1229.0 px | 0.08 | 1.00 | 1347 |
| stroke 109 | 96 % → 96 % | 1954.7 px | 0.18 | 1.00 | 72 |

Numbers say: wet paint spreads well beyond the stroke.

## Refs v3 · #05 HW green in rust loops — own sheet
own sheet 800 × 1045 · Gouache 1.00 + turpentine 30 % · 104 px · 1175.1 s

![Refs v3 · #05 HW green in rust loops — own sheet](Refs-v3-05-HW-green-in-rust-loops-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 11 % → 97 % | 81.1 px | 0.24 | 9.22 | 4941 |
| stroke 2 | 18 % → 94 % | 192.3 px | 0.24 | 5.14 | 4259 |
| stroke 3 | 23 % → 94 % | 266.2 px | 0.30 | 4.13 | 2439 |
| stroke 4 | 24 % → 96 % | 199.4 px | 0.31 | 3.98 | 5864 |
| stroke 5 | 29 % → 94 % | 277.7 px | 0.21 | 3.24 | 6419 |
| stroke 6 | 36 % → 89 % | 225.1 px | 0.24 | 2.51 | 5852 |
| stroke 7 | 50 % → 92 % | 688.6 px | 0.09 | 1.83 | 2538 |
| stroke 8 | 40 % → 93 % | 472.2 px | 0.23 | 2.33 | 4692 |
| stroke 9 | 44 % → 93 % | 400.2 px | 0.26 | 2.13 | 7489 |
| stroke 10 | 50 % → 99 % | 780.5 px | 0.31 | 1.96 | 2459 |
| stroke 11 | 60 % → 99 % | 1074.2 px | 0.21 | 1.65 | 2458 |
| stroke 12 | 75 % → 99 % | 1636.5 px | 0.13 | 1.32 | 1340 |
| stroke 13 | 42 % → 95 % | 520.1 px | 0.26 | 2.26 | 2238 |
| stroke 14 | 63 % → 91 % | 1019.0 px | 0.17 | 1.44 | 3471 |
| stroke 15 | 76 % → 99 % | 1538.7 px | 0.15 | 1.30 | 2293 |
| stroke 16 | 62 % → 99 % | 1330.4 px | 0.27 | 1.61 | 2180 |
| stroke 17 | 54 % → 99 % | 1123.4 px | 0.31 | 1.83 | 2193 |
| stroke 18 | 58 % → 95 % | 1115.0 px | 0.21 | 1.65 | 1644 |
| stroke 19 | 71 % → 99 % | 1617.5 px | 0.22 | 1.39 | 2145 |
| stroke 20 | 80 % → 92 % | 1650.8 px | 0.09 | 1.15 | 1625 |
| stroke 21 | 67 % → 87 % | 981.8 px | 0.13 | 1.31 | 2094 |
| stroke 22 | 60 % → 93 % | 1253.3 px | 0.23 | 1.55 | 1395 |
| stroke 23 | 59 % → 98 % | 932.7 px | 0.25 | 1.66 | 2612 |
| stroke 24 | 60 % → 96 % | 926.8 px | 0.21 | 1.59 | 2601 |
| stroke 25 | 53 % → 96 % | 849.7 px | 0.30 | 1.83 | 1790 |
| stroke 26 | 88 % → 99 % | 2070.9 px | 0.12 | 1.12 | 1483 |
| stroke 27 | 51 % → 96 % | 995.3 px | 0.28 | 1.89 | 1156 |
| stroke 28 | 68 % → 95 % | 1456.8 px | 0.18 | 1.40 | 1362 |
| stroke 29 | 22 % → 82 % | 265.1 px | 0.47 | 3.68 | 544 |
| stroke 30 | 18 % → 79 % | 291.7 px | 0.50 | 4.37 | 364 |
| stroke 31 | 4 % → 89 % | 61.3 px | 0.60 | 22.71 | 382 |
| stroke 32 | 7 % → 89 % | 125.2 px | 0.59 | 13.60 | 490 |
| stroke 33 | 11 % → 89 % | 162.2 px | 0.57 | 8.22 | 753 |
| stroke 34 | 23 % → 92 % | 789.7 px | 0.54 | 4.03 | 289 |
| stroke 35 | 30 % → 91 % | 564.5 px | 0.51 | 3.07 | 582 |
| stroke 36 | 33 % → 91 % | 804.0 px | 0.49 | 2.74 | 696 |
| stroke 37 | 30 % → 92 % | 393.8 px | 0.49 | 3.06 | 1299 |
| stroke 38 | 53 % → 97 % | 553.3 px | 0.39 | 1.83 | 1726 |
| stroke 39 | 42 % → 94 % | 804.5 px | 0.46 | 2.27 | 927 |
| stroke 40 | 40 % → 91 % | 1102.5 px | 0.51 | 2.26 | 461 |
| stroke 41 | 48 % → 96 % | 1056.4 px | 0.44 | 2.01 | 593 |
| stroke 42 | 54 % → 97 % | 1025.9 px | 0.40 | 1.79 | 765 |
| stroke 43 | 48 % → 95 % | 583.8 px | 0.45 | 1.99 | 1534 |
| stroke 44 | 39 % → 89 % | 706.1 px | 0.53 | 2.30 | 1351 |
| stroke 45 | 44 % → 91 % | 845.3 px | 0.48 | 2.05 | 1517 |
| stroke 46 | 61 % → 97 % | 1255.2 px | 0.38 | 1.58 | 927 |
| stroke 47 | 43 % → 91 % | 1597.9 px | 0.50 | 2.09 | 553 |
| stroke 48 | 37 % → 89 % | 1037.1 px | 0.56 | 2.43 | 455 |
| stroke 49 | 25 % → 83 % | 641.1 px | 0.46 | 3.32 | 767 |
| stroke 50 | 27 % → 84 % | 992.8 px | 0.43 | 3.14 | 80 |
| stroke 51 | 7 % → 76 % | 173.5 px | 0.62 | 11.19 | 83 |
| stroke 52 | 7 % → 77 % | 80.9 px | 0.64 | 10.78 | 501 |
| stroke 53 | 1 % → 79 % | 39.0 px | 0.58 | 62.08 | 68 |
| stroke 54 | 7 % → 79 % | 262.4 px | 0.68 | 11.59 | 71 |
| stroke 55 | 4 % → 80 % | 168.8 px | 0.66 | 20.95 | 43 |
| stroke 56 | 21 % → 78 % | 174.2 px | 0.51 | 3.81 | 780 |
| stroke 57 | 67 % → 88 % | 1450.8 px | 0.15 | 1.32 | 437 |
| stroke 58 | 35 % → 83 % | 426.5 px | 0.41 | 2.36 | 796 |
| stroke 59 | 48 % → 82 % | 465.2 px | 0.32 | 1.70 | 1087 |
| stroke 60 | 22 % → 77 % | 448.6 px | 0.60 | 3.54 | 170 |
| stroke 61 | 68 % → 87 % | 674.6 px | 0.20 | 1.27 | 726 |
| stroke 62 | 61 % → 90 % | 1831.0 px | 0.29 | 1.47 | 162 |
| stroke 63 | 53 % → 87 % | 1320.6 px | 0.35 | 1.63 | 248 |
| stroke 64 | 67 % → 89 % | 1181.6 px | 0.24 | 1.32 | 363 |
| stroke 65 | 60 % → 89 % | 1865.0 px | 0.31 | 1.48 | 191 |
| stroke 66 | 72 % → 93 % | 1680.6 px | 0.25 | 1.30 | 274 |
| stroke 67 | 70 % → 93 % | 604.4 px | 0.27 | 1.33 | 614 |
| stroke 68 | 76 % → 94 % | 1617.3 px | 0.31 | 1.24 | 232 |
| stroke 69 | 78 % → 94 % | 2496.7 px | 0.28 | 1.21 | 163 |
| stroke 70 | 77 % → 92 % | 2325.7 px | 0.20 | 1.19 | 159 |
| stroke 71 | 43 % → 84 % | 448.6 px | 0.38 | 1.95 | 728 |
| stroke 72 | 56 % → 94 % | 675.3 px | 0.34 | 1.68 | 434 |
| stroke 73 | 51 % → 86 % | 487.5 px | 0.35 | 1.68 | 523 |
| stroke 74 | 55 % → 95 % | 1533.0 px | 0.36 | 1.71 | 224 |
| stroke 75 | 52 % → 93 % | 1154.7 px | 0.38 | 1.79 | 310 |
| stroke 76 | 34 % → 75 % | 259.3 px | 0.32 | 2.21 | 594 |
| stroke 77 | 39 % → 78 % | 389.4 px | 0.35 | 2.00 | 717 |
| stroke 78 | 54 % → 87 % | 1143.1 px | 0.28 | 1.61 | 269 |
| stroke 79 | 44 % → 80 % | 1317.5 px | 0.33 | 1.80 | 221 |
| stroke 80 | 50 % → 80 % | 1178.8 px | 0.29 | 1.58 | 215 |
| stroke 81 | 32 % → 74 % | 541.8 px | 0.42 | 2.30 | 255 |
| stroke 82 | 42 % → 76 % | 1351.1 px | 0.35 | 1.81 | 174 |
| stroke 83 | 61 % → 87 % | 1238.7 px | 0.25 | 1.43 | 382 |
| stroke 84 | 40 % → 88 % | 611.4 px | 0.61 | 2.19 | 76 |
| stroke 85 | 31 % → 87 % | 916.1 px | 0.63 | 2.77 | 51 |
| stroke 86 | 75 % → 85 % | 2573.2 px | 0.14 | 1.13 | 65 |
| stroke 87 | 78 % → 93 % | 1117.4 px | 0.24 | 1.20 | 327 |
| stroke 88 | 65 % → 94 % | 3079.2 px | 0.29 | 1.44 | 48 |
| stroke 89 | 78 % → 93 % | 1104.7 px | 0.23 | 1.20 | 234 |
| stroke 90 | 74 % → 93 % | 1073.7 px | 0.24 | 1.26 | 272 |
| stroke 91 | 69 % → 94 % | 1272.0 px | 0.28 | 1.36 | 206 |
| stroke 92 | 80 % → 93 % | 2268.8 px | 0.20 | 1.16 | 113 |
| stroke 93 | 76 % → 93 % | 1435.2 px | 0.23 | 1.23 | 212 |
| stroke 94 | 71 % → 94 % | 1000.5 px | 0.26 | 1.31 | 344 |
| stroke 95 | 81 % → 92 % | 3986.4 px | 0.18 | 1.13 | 65 |
| stroke 96 | 66 % → 94 % | 2498.2 px | 0.30 | 1.43 | 118 |
| stroke 97 | 82 % → 92 % | 2708.1 px | 0.19 | 1.12 | 78 |
| stroke 98 | 79 % → 94 % | 4372.7 px | 0.20 | 1.19 | 54 |
| stroke 99 | 61 % → 97 % | 1059.7 px | 0.32 | 1.58 | 301 |
| stroke 100 | 59 % → 99 % | 4556.3 px | 0.34 | 1.70 | 53 |
| stroke 101 | 62 % → 95 % | 2032.4 px | 0.33 | 1.54 | 119 |
| stroke 102 | 50 % → 92 % | 1230.2 px | 0.39 | 1.84 | 203 |
| stroke 103 | 52 % → 98 % | 3417.8 px | 0.40 | 1.86 | 59 |
| stroke 104 | 62 % → 99 % | 4822.6 px | 0.34 | 1.61 | 56 |
| stroke 105 | 56 % → 99 % | 2358.1 px | 0.37 | 1.77 | 124 |
| stroke 106 | 53 % → 98 % | 3045.4 px | 0.40 | 1.85 | 84 |
| stroke 107 | 66 % → 95 % | 2700.6 px | 0.30 | 1.44 | 81 |
| stroke 108 | 55 % → 99 % | 4320.9 px | 0.38 | 1.79 | 53 |
| stroke 109 | 57 % → 99 % | 4406.1 px | 0.37 | 1.75 | 48 |
| stroke 110 | 55 % → 99 % | 4237.6 px | 0.37 | 1.79 | 50 |
| stroke 111 | 35 % → 86 % | 618.0 px | 0.61 | 2.44 | 50 |
| stroke 112 | 62 % → 90 % | 652.5 px | 0.27 | 1.46 | 604 |
| stroke 113 | 62 % → 95 % | 2646.6 px | 0.30 | 1.54 | 92 |
| stroke 114 | 50 % → 85 % | 857.6 px | 0.44 | 1.69 | 830 |
| stroke 115 | 41 % → 89 % | 563.5 px | 0.57 | 2.18 | 1854 |
| stroke 116 | 58 % → 92 % | 1201.0 px | 0.45 | 1.59 | 1629 |
| stroke 117 | 58 % → 85 % | 359.9 px | 0.39 | 1.46 | 6927 |
| stroke 118 | 51 % → 80 % | 297.6 px | 0.60 | 1.58 | 4039 |
| stroke 119 | 72 % → 88 % | 728.3 px | 0.37 | 1.22 | 4030 |
| stroke 120 | 69 % → 81 % | 527.6 px | 0.39 | 1.17 | 3472 |
| stroke 121 | 65 % → 78 % | 515.6 px | 0.47 | 1.19 | 4293 |
| stroke 122 | 76 % → 82 % | 928.7 px | 0.37 | 1.08 | 2973 |
| stroke 123 | 73 % → 77 % | 672.7 px | 0.54 | 1.06 | 3674 |
| stroke 124 | 77 % → 80 % | 1108.6 px | 0.39 | 1.04 | 1954 |
| stroke 125 | 77 % → 80 % | 862.1 px | 0.61 | 1.04 | 2335 |
| stroke 126 | 82 % → 83 % | 863.2 px | 0.42 | 1.01 | 1964 |
| stroke 127 | 81 % → 82 % | 750.7 px | 0.53 | 1.01 | 2871 |
| stroke 128 | 94 % → 94 % | 1766.3 px | 0.41 | 1.00 | 1410 |
| stroke 129 | 76 % → 76 % | 977.0 px | 0.57 | 1.00 | 1034 |
| stroke 130 | 85 % → 84 % | 1741.8 px | 0.55 | 0.99 | 947 |
| stroke 131 | 91 % → 90 % | 1882.4 px | 0.39 | 0.99 | 1517 |
| stroke 132 | 98 % → 98 % | 1783.7 px | 0.35 | 0.99 | 1694 |
| stroke 133 | 95 % → 95 % | 1823.6 px | 0.36 | 1.00 | 1407 |
| stroke 134 | 33 % → 79 % | 865.1 px | 0.62 | 2.42 | 25 |
| stroke 135 | 56 % → 87 % | 637.1 px | 0.41 | 1.55 | 2332 |
| stroke 136 | 71 % → 93 % | 725.5 px | 0.40 | 1.32 | 3153 |
| stroke 137 | 75 % → 97 % | 1506.3 px | 0.42 | 1.30 | 2110 |
| stroke 138 | 66 % → 91 % | 809.6 px | 0.47 | 1.38 | 2578 |
| stroke 139 | 69 % → 90 % | 1206.8 px | 0.46 | 1.30 | 1140 |
| stroke 140 | 81 % → 93 % | 779.3 px | 0.37 | 1.15 | 3981 |
| stroke 141 | 74 % → 85 % | 601.3 px | 0.41 | 1.14 | 3495 |
| stroke 142 | 77 % → 91 % | 405.7 px | 0.40 | 1.18 | 2984 |
| stroke 143 | 66 % → 81 % | 453.0 px | 0.62 | 1.22 | 1360 |
| stroke 144 | 80 % → 87 % | 1559.6 px | 0.44 | 1.09 | 686 |
| stroke 145 | 91 % → 94 % | 2217.7 px | 0.32 | 1.03 | 746 |
| stroke 146 | 88 % → 98 % | 2336.9 px | 0.40 | 1.11 | 774 |
| stroke 147 | 87 % → 91 % | 2077.1 px | 0.40 | 1.05 | 782 |
| stroke 148 | 90 % → 92 % | 1695.3 px | 0.33 | 1.01 | 906 |
| stroke 149 | 81 % → 84 % | 1516.3 px | 0.55 | 1.04 | 522 |
| stroke 150 | 94 % → 99 % | 2677.1 px | 0.32 | 1.06 | 909 |
| stroke 151 | 85 % → 93 % | 889.2 px | 0.47 | 1.09 | 2786 |
| stroke 152 | 95 % → 97 % | 1115.4 px | 0.33 | 1.02 | 1703 |
| stroke 153 | 98 % → 98 % | 2305.7 px | 0.29 | 1.00 | 849 |
| stroke 154 | 78 % → 87 % | 1378.5 px | 0.62 | 1.12 | 1010 |
| stroke 155 | 82 % → 88 % | 731.8 px | 0.61 | 1.08 | 1658 |
| stroke 156 | 95 % → 96 % | 2227.9 px | 0.31 | 1.02 | 1163 |
| stroke 157 | 98 % → 99 % | 2661.1 px | 0.35 | 1.01 | 932 |
| stroke 158 | 80 % → 86 % | 991.0 px | 0.61 | 1.08 | 746 |
| stroke 159 | 85 % → 85 % | 1143.2 px | 0.43 | 1.00 | 1141 |
| stroke 160 | 92 % → 92 % | 483.2 px | 0.40 | 1.00 | 2317 |
| stroke 161 | 90 % → 91 % | 1236.4 px | 0.60 | 1.00 | 1526 |
| stroke 162 | 92 % → 93 % | 1857.7 px | 0.47 | 1.00 | 1096 |
| stroke 163 | 84 % → 84 % | 1552.2 px | 0.63 | 1.00 | 445 |
| stroke 164 | 98 % → 98 % | 2881.6 px | 0.37 | 1.00 | 749 |
| stroke 165 | 90 % → 89 % | 1717.7 px | 0.65 | 1.00 | 815 |
| stroke 166 | 93 % → 93 % | 2522.4 px | 0.49 | 1.00 | 737 |

Numbers say: wet paint spreads well beyond the stroke.

## Refs v3 · #06 HW scrubbed grey — own sheet
own sheet 800 × 635 · Gouache 1.00 + turpentine 30 % · 93 px · 699.4 s

![Refs v3 · #06 HW scrubbed grey — own sheet](Refs-v3-06-HW-scrubbed-grey-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 14 % → 98 % | 84.1 px | 0.21 | 7.21 | 2750 |
| stroke 2 | 12 % → 97 % | 81.2 px | 0.19 | 7.95 | 3210 |
| stroke 3 | 25 % → 98 % | 245.0 px | 0.22 | 3.91 | 2186 |
| stroke 4 | 37 % → 97 % | 197.9 px | 0.22 | 2.67 | 5138 |
| stroke 5 | 33 % → 98 % | 328.0 px | 0.20 | 2.99 | 3111 |
| stroke 6 | 50 % → 97 % | 649.5 px | 0.19 | 1.96 | 1030 |
| stroke 7 | 40 % → 97 % | 600.9 px | 0.18 | 2.45 | 1711 |
| stroke 8 | 54 % → 98 % | 451.4 px | 0.23 | 1.81 | 2301 |
| stroke 9 | 64 % → 99 % | 532.5 px | 0.22 | 1.53 | 2458 |
| stroke 10 | 53 % → 97 % | 665.4 px | 0.18 | 1.82 | 1910 |
| stroke 11 | 35 % → 98 % | 439.2 px | 0.22 | 2.78 | 1822 |
| stroke 12 | 61 % → 98 % | 1011.4 px | 0.22 | 1.60 | 1626 |
| stroke 13 | 61 % → 98 % | 772.4 px | 0.23 | 1.60 | 1940 |
| stroke 14 | 67 % → 99 % | 711.1 px | 0.23 | 1.47 | 1564 |
| stroke 15 | 54 % → 99 % | 999.2 px | 0.21 | 1.83 | 1298 |
| stroke 16 | 59 % → 99 % | 699.5 px | 0.22 | 1.68 | 3874 |
| stroke 17 | 64 % → 98 % | 757.6 px | 0.22 | 1.54 | 3149 |
| stroke 18 | 41 % → 97 % | 370.8 px | 0.21 | 2.35 | 1636 |
| stroke 19 | 56 % → 98 % | 727.2 px | 0.22 | 1.74 | 1158 |
| stroke 20 | 76 % → 98 % | 816.0 px | 0.23 | 1.30 | 1984 |
| stroke 21 | 73 % → 99 % | 926.4 px | 0.23 | 1.35 | 1803 |
| stroke 22 | 58 % → 99 % | 1009.7 px | 0.22 | 1.71 | 1506 |
| stroke 23 | 40 % → 98 % | 823.1 px | 0.17 | 2.45 | 926 |
| stroke 24 | 68 % → 98 % | 1110.7 px | 0.21 | 1.44 | 1284 |
| stroke 25 | 31 % → 99 % | 653.2 px | 0.17 | 3.25 | 744 |
| stroke 26 | 18 % → 97 % | 582.7 px | 0.17 | 5.42 | 88 |
| stroke 27 | 17 % → 95 % | 339.4 px | 0.16 | 5.48 | 60 |
| stroke 28 | 4 % → 93 % | 60.4 px | 0.14 | 22.66 | 39 |
| stroke 29 | 62 % → 98 % | 668.9 px | 0.21 | 1.58 | 2176 |
| stroke 30 | 51 % → 99 % | 471.3 px | 0.19 | 1.94 | 2653 |
| stroke 31 | 38 % → 97 % | 266.2 px | 0.16 | 2.58 | 2656 |
| stroke 32 | 36 % → 97 % | 313.9 px | 0.14 | 2.68 | 2312 |
| stroke 33 | 73 % → 98 % | 781.7 px | 0.22 | 1.34 | 1982 |
| stroke 34 | 80 % → 98 % | 983.6 px | 0.22 | 1.23 | 1769 |
| stroke 35 | 64 % → 99 % | 1555.5 px | 0.19 | 1.55 | 1011 |
| stroke 36 | 77 % → 98 % | 1115.3 px | 0.21 | 1.29 | 1631 |
| stroke 37 | 41 % → 94 % | 427.4 px | 0.15 | 2.29 | 652 |
| stroke 38 | 87 % → 99 % | 1979.5 px | 0.23 | 1.13 | 643 |
| stroke 39 | 67 % → 99 % | 872.6 px | 0.19 | 1.49 | 1800 |
| stroke 40 | 55 % → 99 % | 959.9 px | 0.16 | 1.80 | 1015 |
| stroke 41 | 68 % → 98 % | 1123.5 px | 0.18 | 1.45 | 1598 |
| stroke 42 | 48 % → 96 % | 1135.6 px | 0.14 | 2.02 | 677 |
| stroke 43 | 88 % → 99 % | 1594.9 px | 0.23 | 1.12 | 788 |
| stroke 44 | 91 % → 99 % | 2428.9 px | 0.22 | 1.09 | 1337 |
| stroke 45 | 55 % → 97 % | 475.0 px | 0.15 | 1.77 | 2803 |
| stroke 46 | 50 % → 99 % | 1068.2 px | 0.14 | 2.00 | 832 |
| stroke 47 | 71 % → 99 % | 1930.4 px | 0.18 | 1.39 | 732 |
| stroke 48 | 58 % → 99 % | 1542.7 px | 0.15 | 1.70 | 635 |
| stroke 49 | 65 % → 96 % | 1013.7 px | 0.17 | 1.48 | 1014 |
| stroke 50 | 80 % → 98 % | 1814.4 px | 0.22 | 1.23 | 725 |
| stroke 51 | 50 % → 99 % | 1200.4 px | 0.14 | 1.99 | 643 |
| stroke 52 | 77 % → 98 % | 1676.0 px | 0.21 | 1.26 | 703 |
| stroke 53 | 74 % → 98 % | 825.5 px | 0.20 | 1.32 | 2460 |
| stroke 54 | 61 % → 96 % | 553.3 px | 0.18 | 1.56 | 2174 |
| stroke 55 | 79 % → 98 % | 795.8 px | 0.21 | 1.24 | 2813 |
| stroke 56 | 51 % → 95 % | 539.6 px | 0.16 | 1.87 | 629 |
| stroke 57 | 66 % → 96 % | 900.0 px | 0.18 | 1.46 | 1238 |
| stroke 58 | 75 % → 97 % | 2197.0 px | 0.20 | 1.30 | 102 |
| stroke 59 | 58 % → 96 % | 1344.1 px | 0.17 | 1.66 | 210 |
| stroke 60 | 81 % → 97 % | 424.6 px | 0.19 | 1.19 | 1404 |
| stroke 61 | 91 % → 99 % | 1476.1 px | 0.22 | 1.08 | 484 |
| stroke 62 | 93 % → 97 % | 445.6 px | 0.21 | 1.05 | 1982 |
| stroke 63 | 92 % → 96 % | 923.0 px | 0.19 | 1.05 | 709 |
| stroke 64 | 96 % → 98 % | 924.3 px | 0.21 | 1.02 | 1069 |
| stroke 65 | 92 % → 96 % | 1327.4 px | 0.19 | 1.04 | 355 |
| stroke 66 | 94 % → 97 % | 1493.8 px | 0.19 | 1.02 | 440 |
| stroke 67 | 95 % → 96 % | 769.2 px | 0.16 | 1.01 | 384 |
| stroke 68 | 96 % → 96 % | 922.8 px | 0.18 | 1.00 | 480 |
| stroke 69 | 96 % → 96 % | 1130.5 px | 0.17 | 1.00 | 362 |
| stroke 70 | 98 % → 98 % | 1592.9 px | 0.20 | 1.00 | 355 |
| stroke 71 | 75 % → 97 % | 806.4 px | 0.18 | 1.29 | 999 |
| stroke 72 | 84 % → 98 % | 496.6 px | 0.21 | 1.17 | 1412 |
| stroke 73 | 85 % → 98 % | 908.9 px | 0.19 | 1.15 | 949 |
| stroke 74 | 90 % → 99 % | 925.7 px | 0.23 | 1.09 | 726 |
| stroke 75 | 93 % → 98 % | 583.7 px | 0.21 | 1.05 | 494 |
| stroke 76 | 83 % → 97 % | 573.1 px | 0.18 | 1.16 | 1295 |
| stroke 77 | 98 % → 98 % | 783.1 px | 0.21 | 1.00 | 562 |
| stroke 78 | 98 % → 98 % | 533.5 px | 0.22 | 1.00 | 530 |
| stroke 79 | 80 % → 97 % | 1511.3 px | 0.18 | 1.20 | 454 |
| stroke 80 | 96 % → 98 % | 1106.8 px | 0.20 | 1.02 | 867 |
| stroke 81 | 97 % → 97 % | 1173.9 px | 0.20 | 1.00 | 339 |
| stroke 82 | 49 % → 96 % | 385.0 px | 0.13 | 1.95 | 1525 |
| stroke 83 | 63 % → 97 % | 662.4 px | 0.16 | 1.53 | 1667 |
| stroke 84 | 54 % → 95 % | 511.4 px | 0.13 | 1.76 | 1290 |
| stroke 85 | 61 % → 94 % | 557.5 px | 0.15 | 1.54 | 830 |
| stroke 86 | 62 % → 97 % | 796.3 px | 0.14 | 1.57 | 1606 |
| stroke 87 | 55 % → 95 % | 1351.4 px | 0.12 | 1.74 | 358 |
| stroke 88 | 71 % → 95 % | 1141.3 px | 0.15 | 1.35 | 616 |
| stroke 89 | 59 % → 92 % | 536.2 px | 0.11 | 1.56 | 510 |
| stroke 90 | 75 % → 93 % | 1324.5 px | 0.15 | 1.25 | 367 |
| stroke 91 | 75 % → 95 % | 1613.9 px | 0.15 | 1.28 | 422 |
| stroke 92 | 64 % → 98 % | 1969.8 px | 0.14 | 1.52 | 460 |
| stroke 93 | 67 % → 95 % | 1150.7 px | 0.14 | 1.41 | 630 |
| stroke 94 | 72 % → 94 % | 1130.4 px | 0.15 | 1.31 | 592 |
| stroke 95 | 62 % → 96 % | 779.1 px | 0.14 | 1.55 | 620 |
| stroke 96 | 64 % → 95 % | 863.6 px | 0.14 | 1.47 | 394 |
| stroke 97 | 76 % → 97 % | 333.2 px | 0.12 | 1.28 | 6002 |
| stroke 98 | 73 % → 96 % | 355.6 px | 0.09 | 1.31 | 3337 |
| stroke 99 | 92 % → 97 % | 592.1 px | 0.13 | 1.06 | 4019 |
| stroke 100 | 86 % → 95 % | 516.9 px | 0.11 | 1.10 | 4714 |
| stroke 101 | 97 % → 100 % | 1039.7 px | 0.10 | 1.03 | 1235 |
| stroke 102 | 88 % → 93 % | 443.3 px | 0.07 | 1.06 | 2839 |
| stroke 103 | 96 % → 96 % | 1025.3 px | 0.14 | 0.99 | 1692 |
| stroke 104 | 95 % → 95 % | 770.0 px | 0.11 | 1.00 | 3298 |
| stroke 105 | 96 % → 96 % | 774.2 px | 0.12 | 1.00 | 3811 |
| stroke 106 | 97 % → 96 % | 599.6 px | 0.12 | 0.99 | 1872 |
| stroke 107 | 100 % → 100 % | 1053.2 px | 0.13 | 1.00 | 3101 |
| stroke 108 | 96 % → 96 % | 1228.8 px | 0.08 | 1.00 | 1278 |
| stroke 109 | 96 % → 96 % | 1953.9 px | 0.18 | 1.00 | 92 |

Numbers say: wet paint spreads well beyond the stroke.

## Refs v3 · #07 HW blue L and zigzag — own sheet
own sheet 800 × 1065 · Gouache 1.00 + turpentine 30 % · 104 px · 800.3 s

![Refs v3 · #07 HW blue L and zigzag — own sheet](Refs-v3-07-HW-blue-L-and-zigzag-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 12 % → 90 % | 92.6 px | 0.24 | 7.20 | 3306 |
| stroke 2 | 31 % → 80 % | 122.6 px | 0.27 | 2.61 | 4926 |
| stroke 3 | 36 % → 84 % | 406.3 px | 0.26 | 2.33 | 1832 |
| stroke 4 | 60 % → 99 % | 657.6 px | 0.17 | 1.64 | 1314 |
| stroke 5 | 20 % → 85 % | 160.2 px | 0.32 | 4.36 | 3874 |
| stroke 6 | 65 % → 98 % | 514.8 px | 0.14 | 1.53 | 2667 |
| stroke 7 | 32 % → 87 % | 247.1 px | 0.23 | 2.69 | 3600 |
| stroke 8 | 74 % → 99 % | 907.2 px | 0.15 | 1.34 | 1701 |
| stroke 9 | 42 % → 88 % | 276.9 px | 0.20 | 2.08 | 3620 |
| stroke 10 | 38 % → 84 % | 447.9 px | 0.28 | 2.19 | 3388 |
| stroke 11 | 76 % → 97 % | 937.8 px | 0.11 | 1.28 | 1663 |
| stroke 12 | 59 % → 90 % | 698.0 px | 0.20 | 1.53 | 2264 |
| stroke 13 | 66 % → 94 % | 1099.4 px | 0.23 | 1.41 | 1691 |
| stroke 14 | 72 % → 96 % | 1071.6 px | 0.20 | 1.33 | 2342 |
| stroke 15 | 62 % → 91 % | 704.0 px | 0.24 | 1.48 | 2845 |
| stroke 16 | 58 % → 87 % | 772.2 px | 0.18 | 1.50 | 1102 |
| stroke 17 | 41 % → 72 % | 410.9 px | 0.31 | 1.76 | 2484 |
| stroke 18 | 67 % → 91 % | 886.4 px | 0.16 | 1.37 | 1396 |
| stroke 19 | 67 % → 90 % | 591.3 px | 0.18 | 1.33 | 2593 |
| stroke 20 | 64 % → 85 % | 686.3 px | 0.24 | 1.34 | 1280 |
| stroke 21 | 53 % → 85 % | 845.4 px | 0.25 | 1.61 | 2013 |
| stroke 22 | 88 % → 99 % | 964.4 px | 0.14 | 1.13 | 2131 |
| stroke 23 | 49 % → 83 % | 1632.4 px | 0.22 | 1.69 | 74 |
| stroke 24 | 22 % → 64 % | 159.9 px | 0.36 | 2.86 | 6193 |
| stroke 25 | 24 % → 63 % | 267.4 px | 0.40 | 2.67 | 3061 |
| stroke 26 | 25 % → 42 % | 215.7 px | 0.36 | 1.71 | 3956 |
| stroke 27 | 35 % → 58 % | 391.3 px | 0.36 | 1.67 | 2093 |
| stroke 28 | 36 % → 65 % | 611.5 px | 0.38 | 1.77 | 1609 |
| stroke 29 | 35 % → 62 % | 546.6 px | 0.38 | 1.77 | 2062 |
| stroke 30 | 47 % → 73 % | 679.6 px | 0.30 | 1.54 | 2144 |
| stroke 31 | 67 % → 87 % | 684.8 px | 0.21 | 1.30 | 1792 |
| stroke 32 | 65 % → 87 % | 674.4 px | 0.22 | 1.33 | 1556 |
| stroke 33 | 65 % → 85 % | 815.7 px | 0.22 | 1.30 | 895 |
| stroke 34 | 68 % → 83 % | 1244.2 px | 0.19 | 1.23 | 521 |
| stroke 35 | 71 % → 87 % | 679.0 px | 0.20 | 1.24 | 1261 |
| stroke 36 | 69 % → 84 % | 1146.1 px | 0.19 | 1.22 | 519 |
| stroke 37 | 64 % → 81 % | 1383.3 px | 0.21 | 1.26 | 373 |
| stroke 38 | 58 % → 84 % | 833.6 px | 0.28 | 1.46 | 1366 |
| stroke 39 | 64 % → 86 % | 911.9 px | 0.26 | 1.34 | 1253 |
| stroke 40 | 66 % → 89 % | 1324.2 px | 0.26 | 1.35 | 702 |
| stroke 41 | 55 % → 83 % | 1896.0 px | 0.31 | 1.51 | 331 |
| stroke 42 | 51 % → 81 % | 1529.2 px | 0.33 | 1.60 | 555 |
| stroke 43 | 55 % → 86 % | 2082.5 px | 0.32 | 1.56 | 382 |
| stroke 44 | 61 % → 87 % | 2300.3 px | 0.28 | 1.42 | 436 |
| stroke 45 | 59 % → 81 % | 2204.5 px | 0.28 | 1.38 | 358 |
| stroke 46 | 2 % → 43 % | 39.6 px | 0.58 | 23.10 | 252 |
| stroke 47 | 3 % → 41 % | 82.8 px | 0.56 | 12.87 | 185 |
| stroke 48 | 4 % → 45 % | 148.4 px | 0.57 | 12.78 | 116 |
| stroke 49 | 8 % → 64 % | 75.1 px | 0.59 | 8.01 | 475 |
| stroke 50 | 12 % → 78 % | 192.9 px | 0.61 | 6.54 | 162 |
| stroke 51 | 12 % → 74 % | 198.2 px | 0.59 | 6.06 | 263 |
| stroke 52 | 14 % → 82 % | 444.7 px | 0.59 | 5.87 | 88 |
| stroke 53 | 14 % → 66 % | 458.2 px | 0.57 | 4.78 | 122 |
| stroke 54 | 9 % → 43 % | 127.7 px | 0.61 | 4.74 | 608 |
| stroke 55 | 11 % → 46 % | 157.7 px | 0.61 | 4.21 | 655 |
| stroke 56 | 11 % → 48 % | 373.9 px | 0.61 | 4.21 | 167 |
| stroke 57 | 14 % → 49 % | 358.9 px | 0.61 | 3.54 | 256 |
| stroke 58 | 16 % → 38 % | 545.9 px | 0.57 | 2.39 | 193 |
| stroke 59 | 15 % → 36 % | 290.0 px | 0.59 | 2.44 | 447 |
| stroke 60 | 17 % → 48 % | 859.4 px | 0.60 | 2.78 | 95 |
| stroke 61 | 19 % → 51 % | 887.1 px | 0.60 | 2.75 | 132 |
| stroke 62 | 25 % → 51 % | 188.4 px | 0.60 | 2.02 | 2023 |
| stroke 63 | 42 % → 69 % | 524.9 px | 0.39 | 1.66 | 1569 |
| stroke 64 | 26 % → 49 % | 331.2 px | 0.63 | 1.89 | 855 |
| stroke 65 | 52 % → 66 % | 633.3 px | 0.40 | 1.27 | 1790 |
| stroke 66 | 55 % → 74 % | 1595.5 px | 0.39 | 1.35 | 705 |
| stroke 67 | 31 % → 43 % | 334.7 px | 0.61 | 1.36 | 1565 |
| stroke 68 | 38 % → 51 % | 460.8 px | 0.60 | 1.34 | 1327 |
| stroke 69 | 58 % → 78 % | 1865.9 px | 0.37 | 1.34 | 508 |
| stroke 70 | 53 % → 63 % | 778.1 px | 0.60 | 1.21 | 616 |
| stroke 71 | 51 % → 62 % | 535.3 px | 0.60 | 1.20 | 1211 |
| stroke 72 | 49 % → 66 % | 718.9 px | 0.38 | 1.35 | 1665 |
| stroke 73 | 52 % → 61 % | 456.8 px | 0.60 | 1.17 | 1426 |
| stroke 74 | 58 % → 71 % | 1458.4 px | 0.43 | 1.21 | 622 |
| stroke 75 | 58 % → 71 % | 887.4 px | 0.32 | 1.23 | 1095 |
| stroke 76 | 51 % → 56 % | 1140.3 px | 0.57 | 1.09 | 559 |
| stroke 77 | 47 % → 50 % | 729.0 px | 0.62 | 1.06 | 817 |
| stroke 78 | 52 % → 54 % | 897.8 px | 0.61 | 1.04 | 841 |
| stroke 79 | 34 % → 35 % | 332.6 px | 0.57 | 1.02 | 1450 |
| stroke 80 | 53 % → 55 % | 961.6 px | 0.57 | 1.04 | 918 |
| stroke 81 | 72 % → 78 % | 1426.6 px | 0.32 | 1.08 | 1011 |
| stroke 82 | 44 % → 45 % | 536.2 px | 0.58 | 1.01 | 1316 |
| stroke 83 | 37 % → 37 % | 1180.1 px | 0.56 | 1.01 | 434 |
| stroke 84 | 65 % → 69 % | 1075.4 px | 0.39 | 1.06 | 1206 |
| stroke 85 | 43 % → 57 % | 1319.0 px | 0.51 | 1.31 | 539 |
| stroke 86 | 44 % → 45 % | 1090.2 px | 0.59 | 1.01 | 642 |
| stroke 87 | 71 % → 77 % | 2579.9 px | 0.38 | 1.08 | 407 |
| stroke 88 | 45 % → 58 % | 1525.0 px | 0.50 | 1.29 | 465 |
| stroke 89 | 54 % → 66 % | 1293.2 px | 0.36 | 1.21 | 603 |
| stroke 90 | 62 % → 62 % | 1775.2 px | 0.60 | 1.01 | 402 |
| stroke 91 | 64 % → 64 % | 1149.6 px | 0.60 | 1.00 | 603 |
| stroke 92 | 54 % → 55 % | 1454.6 px | 0.60 | 1.01 | 572 |
| stroke 93 | 60 % → 60 % | 1243.6 px | 0.57 | 1.00 | 295 |
| stroke 94 | 48 % → 48 % | 741.7 px | 0.63 | 1.00 | 1140 |
| stroke 95 | 74 % → 78 % | 2843.7 px | 0.37 | 1.05 | 393 |
| stroke 96 | 33 % → 48 % | 349.9 px | 0.41 | 1.45 | 1490 |
| stroke 97 | 42 % → 55 % | 476.8 px | 0.42 | 1.32 | 1451 |
| stroke 98 | 35 % → 42 % | 470.4 px | 0.37 | 1.20 | 520 |
| stroke 99 | 63 % → 71 % | 1045.3 px | 0.32 | 1.14 | 588 |
| stroke 100 | 73 % → 77 % | 1026.2 px | 0.27 | 1.06 | 881 |
| stroke 101 | 30 % → 33 % | 415.7 px | 0.38 | 1.11 | 844 |
| stroke 102 | 80 % → 84 % | 1562.6 px | 0.27 | 1.05 | 705 |
| stroke 103 | 62 % → 67 % | 1087.6 px | 0.36 | 1.07 | 595 |
| stroke 104 | 35 % → 37 % | 505.0 px | 0.36 | 1.05 | 746 |
| stroke 105 | 35 % → 36 % | 521.3 px | 0.36 | 1.02 | 578 |
| stroke 106 | 69 % → 72 % | 1042.4 px | 0.30 | 1.03 | 631 |
| stroke 107 | 75 % → 75 % | 1175.0 px | 0.28 | 1.01 | 677 |
| stroke 108 | 81 % → 81 % | 3081.5 px | 0.28 | 1.01 | 209 |
| stroke 109 | 29 % → 28 % | 717.9 px | 0.44 | 0.99 | 235 |
| stroke 110 | 60 % → 61 % | 1073.3 px | 0.41 | 1.00 | 717 |
| stroke 111 | 72 % → 72 % | 2254.0 px | 0.32 | 1.00 | 176 |
| stroke 112 | 38 % → 37 % | 925.5 px | 0.40 | 1.00 | 302 |
| stroke 113 | 79 % → 79 % | 3074.7 px | 0.29 | 1.00 | 178 |
| stroke 114 | 62 % → 62 % | 1580.2 px | 0.47 | 1.00 | 146 |
| stroke 115 | 71 % → 74 % | 4056.4 px | 0.42 | 1.04 | 52 |
| stroke 116 | 84 % → 87 % | 1187.4 px | 0.25 | 1.03 | 1090 |
| stroke 117 | 86 % → 89 % | 967.1 px | 0.25 | 1.03 | 2100 |
| stroke 118 | 88 % → 91 % | 1108.5 px | 0.24 | 1.03 | 998 |
| stroke 119 | 96 % → 96 % | 1088.3 px | 0.21 | 1.00 | 1111 |
| stroke 120 | 98 % → 99 % | 1228.7 px | 0.17 | 1.00 | 1452 |
| stroke 121 | 93 % → 93 % | 1097.4 px | 0.23 | 1.00 | 1401 |
| stroke 122 | 89 % → 91 % | 720.6 px | 0.17 | 1.02 | 1491 |
| stroke 123 | 95 % → 97 % | 1254.3 px | 0.12 | 1.02 | 679 |
| stroke 124 | 95 % → 96 % | 1068.9 px | 0.12 | 1.01 | 426 |
| stroke 125 | 96 % → 96 % | 1045.8 px | 0.12 | 0.99 | 471 |
| stroke 126 | 77 % → 78 % | 1623.2 px | 0.26 | 1.00 | 103 |
| stroke 127 | 99 % → 99 % | 535.7 px | 0.15 | 1.00 | 319 |

Numbers say: wet paint spreads well beyond the stroke.

## Refs v3 · #08 HW lilac crown basket — own sheet
own sheet 800 × 1150 · Gouache 1.00 + turpentine 30 % · 36 px · 2017.4 s

![Refs v3 · #08 HW lilac crown basket — own sheet](Refs-v3-08-HW-lilac-crown-basket-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 17 % → 83 % | 35.1 px | 0.15 | 4.86 | 412 |
| stroke 2 | 27 % → 73 % | 90.9 px | 0.16 | 2.66 | 121 |
| stroke 3 | 24 % → 91 % | 67.1 px | 0.16 | 3.71 | 237 |
| stroke 4 | 22 % → 94 % | 50.1 px | 0.28 | 4.30 | 283 |
| stroke 5 | 37 % → 90 % | 96.3 px | 0.14 | 2.45 | 221 |
| stroke 6 | 29 % → 77 % | 81.5 px | 0.17 | 2.69 | 291 |
| stroke 7 | 39 % → 90 % | 183.3 px | 0.16 | 2.34 | 109 |
| stroke 8 | 51 % → 91 % | 282.3 px | 0.16 | 1.78 | 84 |
| stroke 9 | 34 % → 73 % | 107.3 px | 0.15 | 2.13 | 245 |
| stroke 10 | 11 % → 70 % | 34.9 px | 0.10 | 6.53 | 351 |
| stroke 11 | 17 % → 83 % | 129.8 px | 0.08 | 4.77 | 116 |
| stroke 12 | 21 % → 79 % | 107.6 px | 0.08 | 3.74 | 222 |
| stroke 13 | 27 % → 75 % | 96.0 px | 0.12 | 2.78 | 322 |
| stroke 14 | 25 % → 92 % | 141.0 px | 0.09 | 3.69 | 262 |
| stroke 15 | 37 % → 87 % | 175.5 px | 0.09 | 2.36 | 211 |
| stroke 16 | 41 % → 73 % | 334.4 px | 0.11 | 1.79 | 95 |
| stroke 17 | 30 % → 89 % | 166.3 px | 0.09 | 2.94 | 284 |
| stroke 18 | 45 % → 74 % | 347.8 px | 0.09 | 1.65 | 127 |
| stroke 19 | 31 % → 91 % | 234.8 px | 0.10 | 2.90 | 127 |
| stroke 20 | 25 % → 96 % | 183.3 px | 0.15 | 3.78 | 112 |
| stroke 21 | 35 % → 93 % | 309.9 px | 0.11 | 2.67 | 94 |
| stroke 22 | 42 % → 89 % | 263.4 px | 0.08 | 2.12 | 122 |
| stroke 23 | 50 % → 75 % | 432.6 px | 0.08 | 1.51 | 111 |
| stroke 24 | 36 % → 58 % | 312.3 px | 0.12 | 1.62 | 110 |
| stroke 25 | 50 % → 93 % | 471.2 px | 0.10 | 1.85 | 79 |
| stroke 26 | 7 % → 28 % | 36.4 px | 0.15 | 3.80 | 84 |
| stroke 27 | 9 % → 29 % | 49.4 px | 0.18 | 3.39 | 106 |
| stroke 28 | 12 % → 24 % | 78.1 px | 0.16 | 1.97 | 95 |
| stroke 29 | 13 % → 88 % | 34.7 px | 0.20 | 6.72 | 314 |
| stroke 30 | 12 % → 56 % | 44.9 px | 0.20 | 4.73 | 321 |
| stroke 31 | 29 % → 84 % | 62.9 px | 0.19 | 2.85 | 537 |
| stroke 32 | 12 % → 75 % | 31.9 px | 0.20 | 6.07 | 295 |
| stroke 33 | 37 % → 91 % | 98.5 px | 0.19 | 2.43 | 235 |
| stroke 34 | 38 % → 90 % | 92.5 px | 0.20 | 2.35 | 371 |
| stroke 35 | 40 % → 89 % | 177.2 px | 0.20 | 2.24 | 141 |
| stroke 36 | 32 % → 68 % | 215.5 px | 0.17 | 2.13 | 111 |
| stroke 37 | 9 % → 95 % | 35.0 px | 0.33 | 10.35 | 308 |
| stroke 38 | 17 % → 99 % | 56.9 px | 0.29 | 5.97 | 375 |
| stroke 39 | 24 % → 98 % | 72.4 px | 0.33 | 4.10 | 585 |
| stroke 40 | 23 % → 100 % | 107.6 px | 0.37 | 4.39 | 604 |
| stroke 41 | 28 % → 100 % | 100.2 px | 0.37 | 3.51 | 462 |
| stroke 42 | 32 % → 98 % | 105.3 px | 0.29 | 3.09 | 677 |
| stroke 43 | 40 % → 99 % | 267.9 px | 0.28 | 2.49 | 123 |
| stroke 44 | 19 % → 92 % | 110.3 px | 0.31 | 4.81 | 162 |
| stroke 45 | 34 % → 96 % | 158.4 px | 0.28 | 2.86 | 302 |
| stroke 46 | 41 % → 100 % | 300.0 px | 0.30 | 2.47 | 144 |
| stroke 47 | 8 % → 72 % | 35.3 px | 0.20 | 8.99 | 243 |
| stroke 48 | 8 % → 51 % | 36.1 px | 0.16 | 6.71 | 301 |
| stroke 49 | 17 % → 60 % | 124.0 px | 0.16 | 3.60 | 126 |
| stroke 50 | 16 % → 63 % | 71.0 px | 0.16 | 3.79 | 261 |
| stroke 51 | 19 % → 68 % | 90.6 px | 0.20 | 3.63 | 410 |
| stroke 52 | 19 % → 45 % | 87.9 px | 0.16 | 2.35 | 365 |
| stroke 53 | 31 % → 66 % | 200.7 px | 0.16 | 2.10 | 245 |
| stroke 54 | 19 % → 77 % | 171.3 px | 0.22 | 3.98 | 83 |
| stroke 55 | 34 % → 64 % | 343.6 px | 0.16 | 1.88 | 85 |
| stroke 56 | 9 % → 60 % | 34.7 px | 0.04 | 6.39 | 710 |
| stroke 57 | 24 % → 91 % | 64.7 px | 0.04 | 3.74 | 441 |
| stroke 58 | 8 % → 50 % | 59.3 px | 0.04 | 6.22 | 171 |
| stroke 59 | 21 % → 54 % | 76.4 px | 0.04 | 2.53 | 231 |
| stroke 60 | 33 % → 66 % | 93.9 px | 0.04 | 2.03 | 730 |
| stroke 61 | 48 % → 74 % | 115.4 px | 0.04 | 1.54 | 776 |
| stroke 62 | 34 % → 68 % | 167.2 px | 0.04 | 2.01 | 287 |
| stroke 63 | 35 % → 47 % | 172.5 px | 0.03 | 1.33 | 180 |
| stroke 64 | 38 % → 53 % | 156.7 px | 0.03 | 1.40 | 340 |
| stroke 65 | 34 % → 46 % | 227.0 px | 0.04 | 1.36 | 177 |
| stroke 66 | 58 % → 65 % | 181.2 px | 0.04 | 1.11 | 450 |
| stroke 67 | 30 % → 77 % | 170.5 px | 0.07 | 2.59 | 256 |
| stroke 68 | 50 % → 69 % | 461.8 px | 0.04 | 1.40 | 83 |
| stroke 69 | 59 % → 71 % | 249.8 px | 0.04 | 1.20 | 347 |
| stroke 70 | 42 % → 44 % | 196.9 px | 0.04 | 1.04 | 243 |
| stroke 71 | 54 % → 75 % | 312.2 px | 0.04 | 1.38 | 196 |
| stroke 72 | 86 % → 90 % | 253.3 px | 0.04 | 1.05 | 407 |
| stroke 73 | 54 % → 59 % | 218.7 px | 0.04 | 1.08 | 480 |
| stroke 74 | 76 % → 82 % | 266.3 px | 0.04 | 1.08 | 442 |
| stroke 75 | 58 % → 70 % | 317.7 px | 0.04 | 1.20 | 296 |
| stroke 76 | 55 % → 75 % | 318.0 px | 0.04 | 1.36 | 227 |
| stroke 77 | 50 % → 75 % | 337.1 px | 0.05 | 1.50 | 221 |
| stroke 78 | 74 % → 73 % | 428.3 px | 0.04 | 0.99 | 200 |
| stroke 79 | 34 % → 77 % | 287.2 px | 0.10 | 2.30 | 95 |
| stroke 80 | 64 % → 67 % | 458.2 px | 0.03 | 1.04 | 133 |
| stroke 81 | 72 % → 73 % | 486.0 px | 0.04 | 1.02 | 140 |
| stroke 82 | 48 % → 76 % | 410.1 px | 0.06 | 1.59 | 188 |
| stroke 83 | 5 % → 8 % | 37.8 px | 0.02 | 1.79 | 70 |
| stroke 84 | 10 % → 9 % | 86.0 px | 0.02 | 0.88 | 68 |
| stroke 85 | 18 % → 31 % | 36.2 px | 0.03 | 1.74 | 294 |
| stroke 86 | 22 % → 30 % | 51.6 px | 0.03 | 1.35 | 275 |
| stroke 87 | 33 % → 35 % | 73.7 px | 0.03 | 1.07 | 192 |
| stroke 88 | 30 % → 29 % | 183.6 px | 0.03 | 0.97 | 112 |
| stroke 89 | 5 % → 47 % | 14.8 px | 0.24 | 9.22 | 107 |
| stroke 90 | 6 % → 53 % | 18.0 px | 0.08 | 8.65 | 27 |
| stroke 91 | 6 % → 45 % | 32.5 px | 0.14 | 7.20 | 63 |
| stroke 92 | 8 % → 63 % | 44.1 px | 0.11 | 8.37 | 25 |
| stroke 93 | 4 % → 70 % | 19.5 px | 0.15 | 16.82 | 122 |
| stroke 94 | 4 % → 91 % | 23.6 px | 0.27 | 25.16 | 48 |
| stroke 95 | 7 % → 90 % | 63.2 px | 0.27 | 12.77 | 39 |
| stroke 96 | 4 % → 89 % | 16.7 px | 0.32 | 22.34 | 30 |
| stroke 97 | 19 % → 87 % | 78.8 px | 0.26 | 4.58 | 111 |
| stroke 98 | 36 % → 63 % | 103.9 px | 0.12 | 1.78 | 150 |
| stroke 99 | 7 % → 86 % | 29.6 px | 0.46 | 11.87 | 257 |
| stroke 100 | 6 % → 89 % | 32.7 px | 0.36 | 15.00 | 130 |
| stroke 101 | 6 % → 94 % | 34.6 px | 0.31 | 15.45 | 139 |
| stroke 102 | 10 % → 73 % | 77.3 px | 0.24 | 7.04 | 90 |
| stroke 103 | 32 % → 33 % | 113.7 px | 0.06 | 1.02 | 172 |
| stroke 104 | 15 % → 66 % | 83.1 px | 0.16 | 4.50 | 87 |
| stroke 105 | 24 % → 76 % | 131.6 px | 0.16 | 3.15 | 137 |
| stroke 106 | 41 % → 64 % | 212.3 px | 0.10 | 1.55 | 187 |
| stroke 107 | 27 % → 69 % | 93.6 px | 0.16 | 2.54 | 281 |
| stroke 108 | 47 % → 85 % | 504.1 px | 0.17 | 1.83 | 39 |
| stroke 109 | 29 % → 95 % | 120.6 px | 0.19 | 3.22 | 333 |
| stroke 110 | 44 % → 76 % | 192.0 px | 0.15 | 1.72 | 169 |
| stroke 111 | 23 % → 97 % | 89.9 px | 0.26 | 4.21 | 238 |
| stroke 112 | 47 % → 76 % | 230.5 px | 0.15 | 1.61 | 156 |
| stroke 113 | 61 % → 90 % | 233.4 px | 0.15 | 1.48 | 276 |
| stroke 114 | 55 % → 96 % | 308.6 px | 0.12 | 1.75 | 144 |
| stroke 115 | 56 % → 93 % | 532.3 px | 0.13 | 1.65 | 48 |
| stroke 116 | 48 % → 91 % | 325.1 px | 0.13 | 1.91 | 74 |
| stroke 117 | 71 % → 91 % | 297.5 px | 0.14 | 1.28 | 220 |
| stroke 118 | 30 % → 96 % | 274.1 px | 0.29 | 3.24 | 51 |
| stroke 119 | 65 % → 94 % | 617.0 px | 0.13 | 1.44 | 57 |
| stroke 120 | 69 % → 96 % | 791.6 px | 0.10 | 1.38 | 72 |
| stroke 121 | 49 % → 96 % | 418.2 px | 0.19 | 1.97 | 145 |
| stroke 122 | 76 % → 94 % | 624.9 px | 0.13 | 1.24 | 74 |
| stroke 123 | 57 % → 99 % | 553.5 px | 0.18 | 1.75 | 68 |
| stroke 124 | 38 % → 69 % | 254.6 px | 0.13 | 1.81 | 55 |
| stroke 125 | 38 % → 96 % | 382.3 px | 0.22 | 2.49 | 65 |
| stroke 126 | 78 % → 95 % | 636.2 px | 0.11 | 1.21 | 83 |
| stroke 127 | 9 % → 82 % | 52.9 px | 0.11 | 9.21 | 118 |
| stroke 128 | 13 % → 74 % | 95.2 px | 0.12 | 5.71 | 108 |
| stroke 129 | 15 % → 87 % | 160.0 px | 0.12 | 5.97 | 49 |
| stroke 130 | 16 % → 78 % | 157.8 px | 0.12 | 4.95 | 70 |
| stroke 131 | 17 % → 81 % | 194.2 px | 0.12 | 4.84 | 49 |
| stroke 132 | 38 % → 80 % | 139.9 px | 0.19 | 2.08 | 238 |
| stroke 133 | 22 % → 69 % | 102.8 px | 0.19 | 3.09 | 206 |
| stroke 134 | 28 % → 61 % | 126.8 px | 0.20 | 2.22 | 242 |
| stroke 135 | 16 % → 78 % | 178.9 px | 0.18 | 5.01 | 41 |
| stroke 136 | 40 % → 76 % | 262.6 px | 0.20 | 1.89 | 137 |
| stroke 137 | 46 % → 73 % | 338.9 px | 0.19 | 1.60 | 98 |
| stroke 138 | 50 % → 87 % | 215.2 px | 0.20 | 1.73 | 202 |
| stroke 139 | 26 % → 68 % | 297.2 px | 0.18 | 2.62 | 55 |
| stroke 140 | 45 % → 63 % | 463.0 px | 0.18 | 1.39 | 62 |
| stroke 141 | 33 % → 94 % | 142.3 px | 0.24 | 2.84 | 145 |
| stroke 142 | 34 % → 95 % | 175.1 px | 0.27 | 2.82 | 113 |
| stroke 143 | 45 % → 93 % | 308.1 px | 0.19 | 2.07 | 64 |
| stroke 144 | 16 % → 93 % | 70.2 px | 0.25 | 5.79 | 188 |
| stroke 145 | 34 % → 93 % | 367.5 px | 0.23 | 2.75 | 35 |
| stroke 146 | 23 % → 93 % | 188.4 px | 0.25 | 4.07 | 82 |
| stroke 147 | 22 % → 93 % | 242.1 px | 0.21 | 4.21 | 37 |
| stroke 148 | 15 % → 98 % | 140.9 px | 0.21 | 6.44 | 54 |
| stroke 149 | 37 % → 92 % | 403.3 px | 0.24 | 2.49 | 51 |
| stroke 150 | 17 % → 56 % | 72.2 px | 0.25 | 3.26 | 229 |
| stroke 151 | 28 % → 73 % | 118.3 px | 0.18 | 2.61 | 214 |
| stroke 152 | 22 % → 59 % | 96.0 px | 0.25 | 2.66 | 319 |
| stroke 153 | 32 % → 68 % | 129.3 px | 0.19 | 2.15 | 361 |
| stroke 154 | 35 % → 60 % | 191.0 px | 0.19 | 1.74 | 142 |
| stroke 155 | 32 % → 81 % | 120.7 px | 0.28 | 2.54 | 328 |
| stroke 156 | 32 % → 83 % | 144.8 px | 0.30 | 2.57 | 264 |
| stroke 157 | 38 % → 75 % | 157.1 px | 0.20 | 2.00 | 220 |
| stroke 158 | 41 % → 88 % | 445.7 px | 0.19 | 2.14 | 36 |
| stroke 159 | 33 % → 79 % | 113.9 px | 0.21 | 2.39 | 281 |
| stroke 160 | 27 % → 91 % | 69.1 px | 0.37 | 3.34 | 285 |
| stroke 161 | 30 % → 95 % | 95.5 px | 0.40 | 3.16 | 199 |
| stroke 162 | 25 % → 46 % | 177.0 px | 0.22 | 1.88 | 96 |
| stroke 163 | 39 % → 74 % | 341.3 px | 0.22 | 1.91 | 85 |
| stroke 164 | 41 % → 93 % | 125.8 px | 0.33 | 2.27 | 168 |
| stroke 165 | 45 % → 81 % | 493.4 px | 0.19 | 1.79 | 66 |
| stroke 166 | 44 % → 71 % | 304.0 px | 0.18 | 1.63 | 129 |
| stroke 167 | 41 % → 81 % | 162.9 px | 0.27 | 1.96 | 265 |
| stroke 168 | 43 % → 80 % | 273.8 px | 0.23 | 1.85 | 127 |
| stroke 169 | 44 % → 83 % | 315.7 px | 0.24 | 1.86 | 125 |
| stroke 170 | 37 % → 81 % | 205.1 px | 0.21 | 2.21 | 124 |
| stroke 171 | 40 % → 93 % | 172.5 px | 0.35 | 2.34 | 120 |
| stroke 172 | 44 % → 75 % | 290.1 px | 0.20 | 1.70 | 153 |
| stroke 173 | 46 % → 89 % | 318.0 px | 0.25 | 1.93 | 98 |
| stroke 174 | 37 % → 91 % | 176.1 px | 0.37 | 2.45 | 124 |
| stroke 175 | 42 % → 71 % | 457.5 px | 0.17 | 1.68 | 55 |
| stroke 176 | 38 % → 74 % | 216.6 px | 0.20 | 1.93 | 147 |
| stroke 177 | 49 % → 79 % | 464.8 px | 0.19 | 1.61 | 68 |
| stroke 178 | 41 % → 86 % | 191.9 px | 0.22 | 2.06 | 164 |
| stroke 179 | 43 % → 88 % | 337.5 px | 0.34 | 2.05 | 67 |
| stroke 180 | 47 % → 84 % | 326.1 px | 0.22 | 1.77 | 105 |
| stroke 181 | 46 % → 83 % | 314.2 px | 0.20 | 1.80 | 123 |
| stroke 182 | 38 % → 94 % | 161.9 px | 0.39 | 2.51 | 133 |
| stroke 183 | 42 % → 95 % | 185.1 px | 0.38 | 2.26 | 126 |
| stroke 184 | 43 % → 67 % | 227.4 px | 0.19 | 1.55 | 152 |
| stroke 185 | 46 % → 70 % | 377.6 px | 0.18 | 1.51 | 71 |
| stroke 186 | 39 % → 48 % | 285.1 px | 0.18 | 1.22 | 104 |
| stroke 187 | 46 % → 76 % | 290.5 px | 0.20 | 1.64 | 129 |
| stroke 188 | 38 % → 57 % | 302.8 px | 0.21 | 1.50 | 137 |
| stroke 189 | 51 % → 77 % | 505.4 px | 0.20 | 1.50 | 88 |
| stroke 190 | 17 % → 85 % | 170.0 px | 0.27 | 4.95 | 42 |
| stroke 191 | 20 % → 87 % | 104.4 px | 0.28 | 4.41 | 158 |
| stroke 192 | 26 % → 83 % | 126.0 px | 0.27 | 3.20 | 227 |
| stroke 193 | 27 % → 54 % | 255.4 px | 0.15 | 2.00 | 33 |
| stroke 194 | 16 % → 71 % | 98.1 px | 0.11 | 4.42 | 93 |
| stroke 195 | 28 % → 72 % | 297.1 px | 0.09 | 2.61 | 20 |
| stroke 196 | 11 % → 66 % | 78.6 px | 0.17 | 5.77 | 73 |
| stroke 197 | 10 % → 97 % | 53.2 px | 0.24 | 9.76 | 119 |
| stroke 198 | 11 % → 99 % | 50.1 px | 0.37 | 8.59 | 213 |
| stroke 199 | 37 % → 89 % | 150.4 px | 0.22 | 2.38 | 118 |
| stroke 200 | 25 % → 76 % | 99.5 px | 0.29 | 3.08 | 255 |
| stroke 201 | 21 % → 87 % | 120.5 px | 0.40 | 4.12 | 83 |
| stroke 202 | 6 % → 96 % | 36.0 px | 0.45 | 15.66 | 82 |
| stroke 203 | 22 % → 96 % | 143.3 px | 0.35 | 4.26 | 98 |
| stroke 204 | 33 % → 94 % | 275.4 px | 0.34 | 2.88 | 47 |
| stroke 205 | 25 % → 67 % | 100.9 px | 0.17 | 2.67 | 2981 |
| stroke 206 | 35 % → 84 % | 68.4 px | 0.19 | 2.43 | 1372 |
| stroke 207 | 34 % → 65 % | 103.9 px | 0.11 | 1.93 | 1794 |
| stroke 208 | 38 % → 52 % | 108.8 px | 0.10 | 1.36 | 877 |
| stroke 209 | 48 % → 52 % | 173.7 px | 0.10 | 1.08 | 727 |
| stroke 210 | 52 % → 81 % | 278.8 px | 0.16 | 1.57 | 475 |
| stroke 211 | 37 % → 79 % | 143.1 px | 0.21 | 2.13 | 877 |
| stroke 212 | 60 % → 71 % | 186.6 px | 0.10 | 1.17 | 1157 |
| stroke 213 | 53 % → 80 % | 181.7 px | 0.17 | 1.51 | 1562 |
| stroke 214 | 54 % → 95 % | 212.4 px | 0.17 | 1.77 | 532 |
| stroke 215 | 62 % → 83 % | 200.5 px | 0.13 | 1.34 | 949 |
| stroke 216 | 61 % → 98 % | 195.6 px | 0.14 | 1.60 | 987 |
| stroke 217 | 60 % → 99 % | 307.5 px | 0.21 | 1.66 | 366 |
| stroke 218 | 69 % → 95 % | 291.5 px | 0.14 | 1.38 | 462 |
| stroke 219 | 60 % → 82 % | 253.6 px | 0.13 | 1.38 | 2107 |
| stroke 220 | 70 % → 100 % | 272.0 px | 0.17 | 1.42 | 1292 |
| stroke 221 | 58 % → 58 % | 185.7 px | 0.10 | 1.01 | 763 |
| stroke 222 | 73 % → 90 % | 347.6 px | 0.13 | 1.23 | 1563 |
| stroke 223 | 72 % → 92 % | 363.8 px | 0.17 | 1.27 | 829 |
| stroke 224 | 71 % → 93 % | 258.1 px | 0.17 | 1.31 | 1293 |
| stroke 225 | 67 % → 82 % | 267.6 px | 0.11 | 1.22 | 1071 |
| stroke 226 | 53 % → 70 % | 224.1 px | 0.17 | 1.33 | 1646 |
| stroke 227 | 68 % → 97 % | 274.8 px | 0.22 | 1.42 | 950 |
| stroke 228 | 71 % → 71 % | 273.0 px | 0.11 | 1.00 | 1999 |
| stroke 229 | 59 % → 73 % | 286.1 px | 0.14 | 1.22 | 808 |
| stroke 230 | 56 % → 71 % | 336.8 px | 0.15 | 1.26 | 523 |
| stroke 231 | 82 % → 87 % | 439.8 px | 0.10 | 1.06 | 461 |
| stroke 232 | 38 % → 49 % | 148.4 px | 0.11 | 1.30 | 267 |
| stroke 233 | 47 % → 54 % | 175.4 px | 0.15 | 1.16 | 565 |
| stroke 234 | 63 % → 68 % | 270.2 px | 0.13 | 1.08 | 454 |
| stroke 235 | 72 % → 93 % | 256.2 px | 0.18 | 1.29 | 1134 |
| stroke 236 | 70 % → 97 % | 387.3 px | 0.21 | 1.39 | 443 |
| stroke 237 | 81 % → 93 % | 446.0 px | 0.17 | 1.15 | 496 |
| stroke 238 | 68 % → 74 % | 360.6 px | 0.11 | 1.08 | 351 |
| stroke 239 | 65 % → 70 % | 574.2 px | 0.12 | 1.08 | 104 |
| stroke 240 | 76 % → 81 % | 770.3 px | 0.11 | 1.06 | 82 |
| stroke 241 | 71 % → 75 % | 617.0 px | 0.12 | 1.06 | 80 |
| stroke 242 | 83 % → 96 % | 569.5 px | 0.13 | 1.16 | 143 |
| stroke 243 | 73 % → 78 % | 270.2 px | 0.13 | 1.08 | 547 |
| stroke 244 | 81 % → 85 % | 312.2 px | 0.13 | 1.05 | 452 |
| stroke 245 | 80 % → 84 % | 403.5 px | 0.13 | 1.05 | 294 |
| stroke 246 | 53 % → 62 % | 236.6 px | 0.19 | 1.17 | 505 |
| stroke 247 | 59 % → 70 % | 326.4 px | 0.19 | 1.18 | 288 |
| stroke 248 | 44 % → 89 % | 134.0 px | 0.27 | 2.02 | 1096 |
| stroke 249 | 45 % → 93 % | 195.0 px | 0.30 | 2.05 | 707 |
| stroke 250 | 61 % → 90 % | 218.5 px | 0.22 | 1.46 | 631 |
| stroke 251 | 48 % → 96 % | 311.6 px | 0.30 | 1.99 | 166 |
| stroke 252 | 42 % → 82 % | 185.8 px | 0.27 | 1.96 | 429 |
| stroke 253 | 19 % → 100 % | 67.3 px | 0.46 | 5.23 | 493 |
| stroke 254 | 56 % → 92 % | 204.4 px | 0.29 | 1.64 | 555 |
| stroke 255 | 63 % → 99 % | 327.4 px | 0.29 | 1.58 | 218 |
| stroke 256 | 25 % → 100 % | 117.2 px | 0.47 | 4.00 | 283 |
| stroke 257 | 48 % → 99 % | 308.7 px | 0.39 | 2.05 | 178 |
| stroke 258 | 63 % → 84 % | 282.2 px | 0.21 | 1.33 | 412 |
| stroke 259 | 43 % → 82 % | 196.7 px | 0.28 | 1.90 | 315 |
| stroke 260 | 50 % → 85 % | 240.6 px | 0.26 | 1.71 | 270 |
| stroke 261 | 70 % → 88 % | 313.8 px | 0.24 | 1.26 | 389 |
| stroke 262 | 79 % → 99 % | 313.0 px | 0.24 | 1.26 | 222 |
| stroke 263 | 51 % → 84 % | 295.7 px | 0.29 | 1.63 | 210 |
| stroke 264 | 80 % → 93 % | 428.7 px | 0.24 | 1.15 | 251 |
| stroke 265 | 65 % → 100 % | 483.7 px | 0.32 | 1.54 | 101 |
| stroke 266 | 55 % → 87 % | 175.2 px | 0.31 | 1.59 | 519 |
| stroke 267 | 66 % → 89 % | 396.1 px | 0.30 | 1.36 | 205 |
| stroke 268 | 79 % → 86 % | 762.5 px | 0.27 | 1.10 | 89 |
| stroke 269 | 77 % → 98 % | 360.2 px | 0.27 | 1.27 | 285 |
| stroke 270 | 76 % → 94 % | 317.3 px | 0.28 | 1.24 | 337 |
| stroke 271 | 77 % → 86 % | 271.2 px | 0.21 | 1.12 | 357 |
| stroke 272 | 70 % → 86 % | 500.0 px | 0.28 | 1.24 | 164 |
| stroke 273 | 83 % → 88 % | 560.1 px | 0.20 | 1.06 | 138 |
| stroke 274 | 60 % → 96 % | 405.5 px | 0.28 | 1.60 | 138 |
| stroke 275 | 72 % → 92 % | 332.4 px | 0.25 | 1.28 | 241 |
| stroke 276 | 54 % → 98 % | 241.6 px | 0.30 | 1.82 | 227 |
| stroke 277 | 52 % → 99 % | 441.9 px | 0.41 | 1.93 | 99 |
| stroke 278 | 87 % → 92 % | 570.8 px | 0.23 | 1.06 | 195 |
| stroke 279 | 74 % → 85 % | 692.9 px | 0.25 | 1.15 | 93 |
| stroke 280 | 88 % → 93 % | 457.2 px | 0.20 | 1.05 | 217 |
| stroke 281 | 88 % → 99 % | 345.8 px | 0.22 | 1.13 | 336 |
| stroke 282 | 86 % → 90 % | 354.3 px | 0.22 | 1.04 | 424 |
| stroke 283 | 91 % → 91 % | 733.8 px | 0.22 | 1.00 | 140 |
| stroke 284 | 91 % → 91 % | 904.0 px | 0.21 | 1.00 | 132 |
| stroke 285 | 44 % → 99 % | 429.2 px | 0.41 | 2.25 | 131 |
| stroke 286 | 57 % → 100 % | 356.1 px | 0.30 | 1.74 | 147 |
| stroke 287 | 46 % → 100 % | 425.5 px | 0.44 | 2.19 | 105 |
| stroke 288 | 48 % → 99 % | 342.3 px | 0.42 | 2.08 | 125 |
| stroke 289 | 73 % → 86 % | 691.7 px | 0.27 | 1.17 | 105 |
| stroke 290 | 42 % → 100 % | 187.8 px | 0.45 | 2.37 | 284 |
| stroke 291 | 92 % → 93 % | 586.5 px | 0.22 | 1.01 | 166 |
| stroke 292 | 89 % → 91 % | 831.9 px | 0.22 | 1.03 | 135 |
| stroke 293 | 67 % → 81 % | 658.1 px | 0.25 | 1.20 | 90 |
| stroke 294 | 77 % → 99 % | 633.6 px | 0.30 | 1.28 | 96 |
| stroke 295 | 28 % → 100 % | 236.6 px | 0.49 | 3.51 | 97 |
| stroke 296 | 83 % → 82 % | 823.4 px | 0.22 | 1.00 | 90 |
| stroke 297 | 88 % → 91 % | 812.5 px | 0.25 | 1.04 | 99 |
| stroke 298 | 92 % → 95 % | 870.3 px | 0.24 | 1.03 | 98 |
| stroke 299 | 84 % → 84 % | 622.0 px | 0.20 | 1.00 | 152 |
| stroke 300 | 74 % → 92 % | 712.7 px | 0.30 | 1.25 | 93 |
| stroke 301 | 47 % → 99 % | 451.5 px | 0.45 | 2.10 | 85 |
| stroke 302 | 66 % → 99 % | 663.1 px | 0.35 | 1.51 | 90 |
| stroke 303 | 17 % → 100 % | 130.7 px | 0.47 | 6.03 | 136 |
| stroke 304 | 16 % → 100 % | 100.9 px | 0.52 | 6.20 | 148 |
| stroke 305 | 20 % → 100 % | 127.5 px | 0.51 | 4.90 | 169 |
| stroke 306 | 23 % → 100 % | 169.6 px | 0.52 | 4.42 | 131 |
| stroke 307 | 29 % → 100 % | 152.5 px | 0.47 | 3.43 | 250 |
| stroke 308 | 38 % → 76 % | 217.5 px | 0.24 | 2.03 | 127 |
| stroke 309 | 41 % → 75 % | 178.8 px | 0.30 | 1.83 | 354 |
| stroke 310 | 49 % → 76 % | 255.1 px | 0.28 | 1.57 | 322 |
| stroke 311 | 55 % → 76 % | 366.3 px | 0.26 | 1.39 | 147 |
| stroke 312 | 68 % → 82 % | 545.6 px | 0.24 | 1.21 | 193 |
| stroke 313 | 38 % → 88 % | 374.5 px | 0.41 | 2.32 | 118 |
| stroke 314 | 56 % → 82 % | 347.8 px | 0.29 | 1.47 | 446 |
| stroke 315 | 58 % → 87 % | 367.4 px | 0.28 | 1.49 | 352 |
| stroke 316 | 67 % → 71 % | 489.1 px | 0.23 | 1.07 | 264 |
| stroke 317 | 60 % → 82 % | 379.8 px | 0.27 | 1.37 | 328 |
| stroke 318 | 71 % → 75 % | 493.4 px | 0.22 | 1.06 | 123 |
| stroke 319 | 62 % → 86 % | 603.5 px | 0.31 | 1.39 | 108 |
| stroke 320 | 52 % → 85 % | 515.5 px | 0.37 | 1.63 | 85 |
| stroke 321 | 55 % → 78 % | 483.7 px | 0.32 | 1.42 | 122 |
| stroke 322 | 17 % → 85 % | 81.2 px | 0.46 | 4.91 | 208 |
| stroke 323 | 30 % → 89 % | 113.6 px | 0.43 | 2.96 | 338 |
| stroke 324 | 28 % → 82 % | 230.6 px | 0.44 | 2.96 | 113 |
| stroke 325 | 46 % → 90 % | 432.9 px | 0.36 | 1.94 | 73 |
| stroke 326 | 29 % → 91 % | 164.3 px | 0.42 | 3.18 | 131 |
| stroke 327 | 52 % → 83 % | 223.9 px | 0.25 | 1.58 | 487 |
| stroke 328 | 27 % → 91 % | 143.2 px | 0.49 | 3.42 | 138 |
| stroke 329 | 59 % → 95 % | 188.0 px | 0.27 | 1.62 | 415 |
| stroke 330 | 33 % → 91 % | 146.4 px | 0.47 | 2.75 | 177 |
| stroke 331 | 56 % → 82 % | 227.2 px | 0.26 | 1.47 | 375 |
| stroke 332 | 62 % → 88 % | 251.7 px | 0.25 | 1.42 | 324 |
| stroke 333 | 69 % → 94 % | 246.6 px | 0.25 | 1.37 | 413 |
| stroke 334 | 35 % → 97 % | 177.0 px | 0.42 | 2.78 | 226 |
| stroke 335 | 56 % → 77 % | 243.7 px | 0.24 | 1.36 | 537 |
| stroke 336 | 50 % → 97 % | 375.0 px | 0.36 | 1.95 | 99 |
| stroke 337 | 65 % → 94 % | 654.1 px | 0.27 | 1.44 | 55 |
| stroke 338 | 63 % → 94 % | 517.7 px | 0.26 | 1.50 | 103 |
| stroke 339 | 69 % → 92 % | 324.4 px | 0.35 | 1.35 | 254 |
| stroke 340 | 43 % → 97 % | 346.7 px | 0.40 | 2.26 | 115 |
| stroke 341 | 72 % → 95 % | 412.5 px | 0.31 | 1.32 | 174 |
| stroke 342 | 65 % → 93 % | 549.7 px | 0.30 | 1.43 | 73 |
| stroke 343 | 60 % → 94 % | 315.3 px | 0.33 | 1.57 | 271 |
| stroke 344 | 74 % → 96 % | 735.1 px | 0.29 | 1.30 | 65 |
| stroke 345 | 64 % → 95 % | 231.2 px | 0.30 | 1.49 | 457 |
| stroke 346 | 80 % → 92 % | 422.8 px | 0.34 | 1.15 | 240 |
| stroke 347 | 78 % → 89 % | 320.1 px | 0.21 | 1.15 | 328 |
| stroke 348 | 77 % → 89 % | 474.0 px | 0.23 | 1.16 | 160 |
| stroke 349 | 38 % → 99 % | 336.8 px | 0.46 | 2.62 | 96 |
| stroke 350 | 69 % → 93 % | 640.3 px | 0.31 | 1.34 | 74 |
| stroke 351 | 73 % → 91 % | 415.1 px | 0.28 | 1.25 | 197 |
| stroke 352 | 78 % → 94 % | 528.7 px | 0.34 | 1.22 | 157 |
| stroke 353 | 76 % → 94 % | 365.9 px | 0.26 | 1.24 | 320 |
| stroke 354 | 75 % → 96 % | 577.6 px | 0.30 | 1.28 | 183 |
| stroke 355 | 76 % → 80 % | 618.0 px | 0.20 | 1.05 | 184 |
| stroke 356 | 74 % → 96 % | 654.4 px | 0.33 | 1.30 | 216 |
| stroke 357 | 78 % → 88 % | 447.1 px | 0.26 | 1.14 | 809 |
| stroke 358 | 69 % → 89 % | 656.6 px | 0.41 | 1.30 | 144 |
| stroke 359 | 78 % → 84 % | 656.9 px | 0.25 | 1.08 | 235 |
| stroke 360 | 85 % → 90 % | 641.3 px | 0.25 | 1.06 | 264 |
| stroke 361 | 54 % → 90 % | 414.3 px | 0.45 | 1.67 | 85 |
| stroke 362 | 71 % → 97 % | 711.5 px | 0.35 | 1.36 | 84 |
| stroke 363 | 85 % → 88 % | 233.2 px | 0.09 | 1.04 | 74 |
| stroke 364 | 35 % → 67 % | 130.9 px | 0.35 | 1.93 | 157 |
| stroke 365 | 56 % → 79 % | 531.3 px | 0.26 | 1.42 | 934 |
| stroke 366 | 64 % → 69 % | 282.6 px | 0.16 | 1.09 | 298 |
| stroke 367 | 73 % → 75 % | 600.0 px | 0.16 | 1.04 | 118 |
| stroke 368 | 59 % → 63 % | 478.9 px | 0.17 | 1.08 | 159 |
| stroke 369 | 87 % → 87 % | 552.9 px | 0.08 | 0.99 | 251 |
| stroke 370 | 68 % → 71 % | 699.8 px | 0.12 | 1.04 | 113 |
| stroke 371 | 86 % → 91 % | 620.8 px | 0.14 | 1.05 | 103 |
| stroke 372 | 58 % → 100 % | 386.6 px | 0.36 | 1.72 | 81 |
| stroke 373 | 33 % → 99 % | 202.2 px | 0.48 | 3.02 | 73 |
| stroke 374 | 27 % → 94 % | 248.1 px | 0.45 | 3.51 | 28 |
| stroke 375 | 64 % → 90 % | 364.6 px | 0.33 | 1.39 | 114 |
| stroke 376 | 39 % → 84 % | 404.3 px | 0.42 | 2.15 | 51 |
| stroke 377 | 73 % → 77 % | 201.6 px | 0.23 | 1.05 | 2010 |
| stroke 378 | 63 % → 62 % | 220.0 px | 0.31 | 0.99 | 468 |
| stroke 379 | 67 % → 96 % | 198.7 px | 0.32 | 1.42 | 1604 |
| stroke 380 | 61 % → 97 % | 178.7 px | 0.40 | 1.60 | 1787 |
| stroke 381 | 72 % → 96 % | 197.1 px | 0.42 | 1.34 | 1766 |
| stroke 382 | 63 % → 99 % | 183.2 px | 0.45 | 1.57 | 1593 |
| stroke 383 | 71 % → 95 % | 170.0 px | 0.39 | 1.34 | 1359 |
| stroke 384 | 76 % → 98 % | 216.0 px | 0.50 | 1.29 | 1227 |
| stroke 385 | 56 % → 88 % | 191.4 px | 0.50 | 1.57 | 905 |
| stroke 386 | 86 % → 95 % | 355.9 px | 0.37 | 1.11 | 812 |
| stroke 387 | 92 % → 96 % | 265.6 px | 0.37 | 1.05 | 2010 |
| stroke 388 | 89 % → 96 % | 278.8 px | 0.35 | 1.08 | 1944 |
| stroke 389 | 82 % → 99 % | 248.8 px | 0.43 | 1.20 | 1659 |
| stroke 390 | 82 % → 98 % | 264.1 px | 0.32 | 1.20 | 1014 |
| stroke 391 | 64 % → 87 % | 202.9 px | 0.38 | 1.37 | 914 |
| stroke 392 | 72 % → 88 % | 220.5 px | 0.51 | 1.23 | 919 |
| stroke 393 | 85 % → 95 % | 382.1 px | 0.39 | 1.12 | 2482 |
| stroke 394 | 82 % → 89 % | 338.9 px | 0.34 | 1.09 | 1188 |
| stroke 395 | 95 % → 100 % | 329.5 px | 0.53 | 1.05 | 1220 |
| stroke 396 | 94 % → 96 % | 452.3 px | 0.41 | 1.02 | 394 |
| stroke 397 | 95 % → 100 % | 524.1 px | 0.38 | 1.05 | 270 |
| stroke 398 | 94 % → 99 % | 460.5 px | 0.41 | 1.05 | 657 |
| stroke 399 | 80 % → 88 % | 249.9 px | 0.46 | 1.10 | 706 |
| stroke 400 | 95 % → 97 % | 323.8 px | 0.33 | 1.02 | 993 |
| stroke 401 | 97 % → 97 % | 550.4 px | 0.29 | 1.00 | 432 |
| stroke 402 | 96 % → 97 % | 376.4 px | 0.43 | 1.01 | 1197 |
| stroke 403 | 99 % → 100 % | 438.6 px | 0.41 | 1.01 | 484 |
| stroke 404 | 100 % → 100 % | 454.5 px | 0.51 | 1.00 | 531 |
| stroke 405 | 99 % → 100 % | 538.8 px | 0.54 | 1.01 | 570 |
| stroke 406 | 77 % → 80 % | 349.5 px | 0.40 | 1.04 | 504 |
| stroke 407 | 89 % → 89 % | 448.9 px | 0.38 | 1.00 | 556 |
| stroke 408 | 97 % → 97 % | 471.7 px | 0.49 | 1.00 | 300 |
| stroke 409 | 92 % → 93 % | 498.0 px | 0.43 | 1.01 | 430 |
| stroke 410 | 100 % → 100 % | 479.6 px | 0.45 | 1.00 | 505 |
| stroke 411 | 90 % → 99 % | 461.4 px | 0.49 | 1.10 | 411 |
| stroke 412 | 81 % → 92 % | 319.5 px | 0.44 | 1.13 | 784 |
| stroke 413 | 87 % → 89 % | 333.3 px | 0.48 | 1.03 | 469 |
| stroke 414 | 100 % → 100 % | 439.7 px | 0.51 | 1.00 | 554 |
| stroke 415 | 83 % → 83 % | 371.1 px | 0.45 | 1.00 | 327 |
| stroke 416 | 93 % → 97 % | 518.6 px | 0.46 | 1.04 | 446 |
| stroke 417 | 99 % → 99 % | 554.0 px | 0.43 | 1.00 | 600 |
| stroke 418 | 100 % → 100 % | 621.5 px | 0.53 | 1.00 | 340 |
| stroke 419 | 99 % → 100 % | 494.1 px | 0.44 | 1.00 | 678 |
| stroke 420 | 99 % → 99 % | 542.4 px | 0.52 | 1.00 | 406 |
| stroke 421 | 83 % → 89 % | 260.5 px | 0.38 | 1.07 | 1623 |
| stroke 422 | 86 % → 92 % | 525.5 px | 0.37 | 1.07 | 381 |
| stroke 423 | 86 % → 88 % | 380.4 px | 0.40 | 1.02 | 690 |
| stroke 424 | 92 % → 92 % | 585.1 px | 0.28 | 1.00 | 444 |
| stroke 425 | 83 % → 83 % | 441.3 px | 0.42 | 0.99 | 553 |
| stroke 426 | 73 % → 74 % | 290.3 px | 0.12 | 1.01 | 241 |
| stroke 427 | 88 % → 87 % | 256.2 px | 0.16 | 0.99 | 193 |
| stroke 428 | 62 % → 64 % | 642.5 px | 0.15 | 1.03 | 42 |
| stroke 429 | 72 % → 73 % | 448.8 px | 0.15 | 1.01 | 160 |
| stroke 430 | 60 % → 60 % | 411.1 px | 0.15 | 1.00 | 151 |
| stroke 431 | 85 % → 85 % | 248.8 px | 0.25 | 1.00 | 529 |

Numbers say: wet paint spreads well beyond the stroke.

## Refs v3 · #09 HW white loops — own sheet
own sheet 800 × 640 · Gouache 1.00 + turpentine 30 % · 104 px · 536.8 s

![Refs v3 · #09 HW white loops — own sheet](Refs-v3-09-HW-white-loops-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 14 % → 93 % | 91.4 px | 0.09 | 6.83 | 4648 |
| stroke 2 | 29 % → 87 % | 248.1 px | 0.10 | 2.98 | 1351 |
| stroke 3 | 24 % → 90 % | 131.9 px | 0.10 | 3.76 | 4226 |
| stroke 4 | 22 % → 84 % | 170.8 px | 0.14 | 3.82 | 5822 |
| stroke 5 | 40 % → 95 % | 363.1 px | 0.09 | 2.34 | 4640 |
| stroke 6 | 49 % → 93 % | 355.9 px | 0.10 | 1.90 | 6405 |
| stroke 7 | 41 % → 89 % | 691.0 px | 0.09 | 2.18 | 3176 |
| stroke 8 | 45 % → 81 % | 406.1 px | 0.11 | 1.81 | 4392 |
| stroke 9 | 58 % → 90 % | 399.7 px | 0.09 | 1.57 | 6462 |
| stroke 10 | 47 % → 86 % | 401.5 px | 0.17 | 1.82 | 4033 |
| stroke 11 | 49 % → 85 % | 659.6 px | 0.14 | 1.74 | 2580 |
| stroke 12 | 58 % → 89 % | 720.7 px | 0.09 | 1.53 | 4632 |
| stroke 13 | 63 % → 89 % | 511.4 px | 0.12 | 1.41 | 9100 |
| stroke 14 | 62 % → 88 % | 757.4 px | 0.15 | 1.41 | 6041 |
| stroke 15 | 72 % → 83 % | 1068.5 px | 0.10 | 1.14 | 1951 |
| stroke 16 | 77 % → 94 % | 743.0 px | 0.09 | 1.22 | 5126 |
| stroke 17 | 79 % → 87 % | 543.1 px | 0.10 | 1.10 | 4430 |
| stroke 18 | 81 % → 94 % | 1234.0 px | 0.09 | 1.16 | 2919 |
| stroke 19 | 68 % → 87 % | 1138.8 px | 0.14 | 1.27 | 3376 |
| stroke 20 | 65 % → 80 % | 1112.5 px | 0.12 | 1.23 | 1814 |
| stroke 21 | 64 % → 88 % | 743.8 px | 0.16 | 1.36 | 3397 |
| stroke 22 | 81 % → 93 % | 579.7 px | 0.11 | 1.15 | 4732 |
| stroke 23 | 85 % → 96 % | 1444.5 px | 0.10 | 1.14 | 2313 |
| stroke 24 | 80 % → 87 % | 950.1 px | 0.10 | 1.08 | 2174 |
| stroke 25 | 75 % → 91 % | 1522.2 px | 0.14 | 1.21 | 1427 |
| stroke 26 | 70 % → 83 % | 397.0 px | 0.16 | 1.18 | 4717 |
| stroke 27 | 86 % → 92 % | 1300.4 px | 0.09 | 1.07 | 1579 |
| stroke 28 | 86 % → 91 % | 1290.3 px | 0.09 | 1.05 | 1547 |
| stroke 29 | 93 % → 96 % | 1462.8 px | 0.09 | 1.03 | 2365 |
| stroke 30 | 91 % → 93 % | 1625.6 px | 0.09 | 1.03 | 1645 |
| stroke 31 | 70 % → 82 % | 940.9 px | 0.13 | 1.17 | 2424 |
| stroke 32 | 90 % → 93 % | 1314.1 px | 0.11 | 1.03 | 1944 |
| stroke 33 | 73 % → 77 % | 1183.3 px | 0.10 | 1.04 | 1413 |
| stroke 34 | 83 % → 85 % | 1557.9 px | 0.10 | 1.03 | 1930 |
| stroke 35 | 69 % → 84 % | 1108.2 px | 0.18 | 1.22 | 904 |
| stroke 36 | 91 % → 94 % | 1183.7 px | 0.12 | 1.03 | 1592 |
| stroke 37 | 81 % → 85 % | 1134.3 px | 0.09 | 1.05 | 1413 |
| stroke 38 | 93 % → 94 % | 1420.5 px | 0.10 | 1.01 | 1358 |
| stroke 39 | 31 % → 43 % | 425.5 px | 0.07 | 1.41 | 35 |
| stroke 40 | 87 % → 89 % | 1471.3 px | 0.09 | 1.02 | 128 |
| stroke 41 | 88 % → 89 % | 1239.3 px | 0.09 | 1.01 | 258 |
| stroke 42 | 90 % → 89 % | 1603.7 px | 0.09 | 1.00 | 215 |
| stroke 43 | 89 % → 89 % | 2730.4 px | 0.09 | 1.00 | 221 |
| stroke 44 | 91 % → 90 % | 6659.7 px | 0.09 | 1.00 | 39 |
| stroke 45 | 87 % → 87 % | 5335.2 px | 0.09 | 1.00 | 39 |
| stroke 46 | 90 % → 89 % | 2384.2 px | 0.09 | 0.99 | 143 |
| stroke 47 | 88 % → 88 % | 5356.6 px | 0.09 | 0.99 | 32 |
| stroke 48 | 88 % → 87 % | 4842.4 px | 0.09 | 0.99 | 49 |
| stroke 49 | 90 % → 90 % | 3212.1 px | 0.09 | 0.99 | 83 |
| stroke 50 | 68 % → 83 % | 2495.9 px | 0.20 | 1.23 | 91 |
| stroke 51 | 67 % → 83 % | 3152.9 px | 0.21 | 1.24 | 48 |
| stroke 52 | 69 % → 84 % | 2397.8 px | 0.20 | 1.22 | 94 |
| stroke 53 | 81 % → 82 % | 315.8 px | 0.11 | 1.02 | 1352 |
| stroke 54 | 75 % → 74 % | 1946.4 px | 0.10 | 0.99 | 122 |
| stroke 55 | 78 % → 79 % | 3136.9 px | 0.12 | 1.02 | 101 |
| stroke 56 | 78 % → 90 % | 2826.2 px | 0.17 | 1.15 | 76 |
| stroke 57 | 79 % → 90 % | 5075.9 px | 0.17 | 1.14 | 40 |
| stroke 58 | 64 % → 77 % | 573.5 px | 0.21 | 1.21 | 132 |
| stroke 59 | 48 % → 68 % | 545.2 px | 0.27 | 1.43 | 75 |
| stroke 60 | 88 % → 91 % | 911.8 px | 0.12 | 1.04 | 386 |
| stroke 61 | 72 % → 83 % | 887.1 px | 0.19 | 1.16 | 273 |
| stroke 62 | 86 % → 88 % | 1069.9 px | 0.14 | 1.03 | 285 |
| stroke 63 | 80 % → 87 % | 1144.0 px | 0.16 | 1.08 | 326 |
| stroke 64 | 73 % → 83 % | 1150.9 px | 0.19 | 1.14 | 246 |
| stroke 65 | 74 % → 85 % | 2371.1 px | 0.20 | 1.15 | 123 |
| stroke 66 | 90 % → 91 % | 2282.4 px | 0.13 | 1.01 | 117 |
| stroke 67 | 93 % → 94 % | 3029.0 px | 0.12 | 1.00 | 119 |
| stroke 68 | 91 % → 91 % | 2342.3 px | 0.13 | 1.00 | 126 |
| stroke 69 | 80 % → 87 % | 2718.3 px | 0.17 | 1.08 | 120 |
| stroke 70 | 67 % → 77 % | 616.8 px | 0.24 | 1.14 | 700 |
| stroke 71 | 73 % → 79 % | 867.6 px | 0.22 | 1.09 | 452 |
| stroke 72 | 80 % → 84 % | 1719.9 px | 0.20 | 1.05 | 243 |
| stroke 73 | 79 % → 81 % | 902.3 px | 0.21 | 1.03 | 502 |
| stroke 74 | 79 % → 81 % | 2039.6 px | 0.21 | 1.03 | 248 |
| stroke 75 | 80 % → 80 % | 827.8 px | 0.19 | 1.00 | 591 |
| stroke 76 | 81 % → 81 % | 830.2 px | 0.18 | 1.00 | 662 |

Numbers say: wet paint spreads well beyond the stroke.

## Refs v3 · #10 HW maroon loops — own sheet
own sheet 800 × 1070 · Gouache 1.00 + turpentine 30 % · 104 px · 700.4 s

![Refs v3 · #10 HW maroon loops — own sheet](Refs-v3-10-HW-maroon-loops-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 8 % → 76 % | 94.3 px | 0.42 | 9.54 | 5071 |
| stroke 2 | 15 % → 67 % | 151.0 px | 0.38 | 4.55 | 6783 |
| stroke 3 | 28 % → 77 % | 552.7 px | 0.25 | 2.78 | 1872 |
| stroke 4 | 27 % → 48 % | 649.9 px | 0.23 | 1.75 | 1306 |
| stroke 5 | 25 % → 89 % | 438.6 px | 0.47 | 3.59 | 2167 |
| stroke 6 | 26 % → 56 % | 355.2 px | 0.21 | 2.13 | 4111 |
| stroke 7 | 38 % → 80 % | 550.6 px | 0.37 | 2.13 | 2654 |
| stroke 8 | 34 % → 68 % | 470.3 px | 0.30 | 1.99 | 6280 |
| stroke 9 | 35 % → 76 % | 745.0 px | 0.35 | 2.18 | 2212 |
| stroke 10 | 46 % → 78 % | 799.4 px | 0.29 | 1.71 | 3376 |
| stroke 11 | 48 % → 87 % | 1127.5 px | 0.41 | 1.81 | 1705 |
| stroke 12 | 39 % → 60 % | 627.3 px | 0.32 | 1.54 | 4056 |
| stroke 13 | 46 % → 87 % | 1055.6 px | 0.43 | 1.88 | 1993 |
| stroke 14 | 9 % → 88 % | 68.5 px | 0.38 | 9.96 | 1816 |
| stroke 15 | 19 % → 94 % | 104.7 px | 0.49 | 4.95 | 3621 |
| stroke 16 | 24 % → 94 % | 183.7 px | 0.49 | 3.87 | 3136 |
| stroke 17 | 44 % → 92 % | 594.8 px | 0.36 | 2.12 | 824 |
| stroke 18 | 28 % → 94 % | 385.1 px | 0.49 | 3.33 | 2009 |
| stroke 19 | 32 % → 96 % | 343.1 px | 0.49 | 3.01 | 2535 |
| stroke 20 | 40 % → 90 % | 431.2 px | 0.44 | 2.24 | 2117 |
| stroke 21 | 59 % → 90 % | 611.7 px | 0.33 | 1.51 | 653 |
| stroke 22 | 50 % → 94 % | 757.0 px | 0.42 | 1.89 | 845 |
| stroke 23 | 34 % → 77 % | 565.2 px | 0.43 | 2.25 | 809 |
| stroke 24 | 8 % → 71 % | 143.6 px | 0.43 | 9.12 | 781 |
| stroke 25 | 9 % → 81 % | 117.6 px | 0.54 | 9.27 | 1488 |
| stroke 26 | 22 % → 68 % | 267.3 px | 0.36 | 3.07 | 729 |
| stroke 27 | 15 % → 82 % | 386.4 px | 0.51 | 5.30 | 649 |
| stroke 28 | 21 % → 76 % | 316.2 px | 0.47 | 3.67 | 1252 |
| stroke 29 | 22 % → 83 % | 525.7 px | 0.52 | 3.71 | 1021 |
| stroke 30 | 19 % → 82 % | 482.9 px | 0.53 | 4.25 | 919 |
| stroke 31 | 23 % → 91 % | 517.5 px | 0.55 | 3.93 | 918 |
| stroke 32 | 35 % → 71 % | 429.2 px | 0.45 | 2.03 | 292 |
| stroke 33 | 35 % → 78 % | 1788.5 px | 0.46 | 2.23 | 37 |
| stroke 34 | 36 % → 50 % | 412.7 px | 0.20 | 1.39 | 2099 |
| stroke 35 | 44 % → 54 % | 390.6 px | 0.21 | 1.24 | 3355 |
| stroke 36 | 43 % → 53 % | 673.6 px | 0.20 | 1.22 | 1221 |
| stroke 37 | 47 % → 56 % | 909.3 px | 0.21 | 1.18 | 1223 |
| stroke 38 | 47 % → 73 % | 547.6 px | 0.37 | 1.56 | 1928 |
| stroke 39 | 53 % → 78 % | 868.8 px | 0.41 | 1.48 | 1419 |
| stroke 40 | 49 % → 52 % | 625.4 px | 0.20 | 1.06 | 1465 |
| stroke 41 | 59 % → 64 % | 1659.7 px | 0.20 | 1.09 | 601 |
| stroke 42 | 47 % → 48 % | 504.3 px | 0.20 | 1.03 | 1900 |
| stroke 43 | 49 % → 47 % | 915.7 px | 0.18 | 0.96 | 476 |
| stroke 44 | 51 % → 73 % | 1394.3 px | 0.40 | 1.43 | 609 |
| stroke 45 | 54 % → 76 % | 1461.8 px | 0.41 | 1.42 | 766 |
| stroke 46 | 41 % → 66 % | 550.4 px | 0.41 | 1.60 | 1999 |
| stroke 47 | 42 % → 45 % | 810.9 px | 0.26 | 1.06 | 1210 |
| stroke 48 | 43 % → 65 % | 923.1 px | 0.40 | 1.50 | 1044 |
| stroke 49 | 54 % → 86 % | 438.6 px | 0.46 | 1.58 | 5670 |
| stroke 50 | 54 % → 93 % | 536.7 px | 0.49 | 1.71 | 5733 |
| stroke 51 | 52 % → 89 % | 502.5 px | 0.53 | 1.71 | 3043 |
| stroke 52 | 66 % → 86 % | 435.6 px | 0.43 | 1.31 | 3878 |
| stroke 53 | 77 % → 91 % | 1163.6 px | 0.49 | 1.18 | 2065 |
| stroke 54 | 67 % → 90 % | 1206.8 px | 0.51 | 1.34 | 1359 |
| stroke 55 | 81 % → 94 % | 959.2 px | 0.50 | 1.16 | 2396 |
| stroke 56 | 69 % → 85 % | 834.1 px | 0.47 | 1.23 | 3540 |
| stroke 57 | 83 % → 93 % | 1233.8 px | 0.47 | 1.12 | 1832 |
| stroke 58 | 82 % → 99 % | 1956.7 px | 0.57 | 1.21 | 1249 |
| stroke 59 | 80 % → 96 % | 1304.9 px | 0.50 | 1.19 | 2289 |
| stroke 60 | 75 % → 95 % | 1105.1 px | 0.59 | 1.27 | 2308 |
| stroke 61 | 78 % → 93 % | 1504.6 px | 0.50 | 1.19 | 1863 |
| stroke 62 | 87 % → 94 % | 1224.1 px | 0.56 | 1.09 | 2188 |
| stroke 63 | 76 % → 94 % | 1378.6 px | 0.51 | 1.24 | 2220 |
| stroke 64 | 89 % → 96 % | 873.4 px | 0.51 | 1.08 | 4590 |
| stroke 65 | 93 % → 93 % | 958.4 px | 0.44 | 1.00 | 2191 |
| stroke 66 | 87 % → 89 % | 1607.4 px | 0.49 | 1.02 | 1681 |
| stroke 67 | 95 % → 97 % | 1455.2 px | 0.52 | 1.03 | 2626 |
| stroke 68 | 83 % → 83 % | 1284.0 px | 0.48 | 1.00 | 1772 |
| stroke 69 | 93 % → 92 % | 1334.0 px | 0.46 | 1.00 | 2140 |
| stroke 70 | 83 % → 94 % | 1674.7 px | 0.59 | 1.14 | 1640 |
| stroke 71 | 72 % → 91 % | 1275.4 px | 0.55 | 1.28 | 2204 |
| stroke 72 | 61 % → 73 % | 716.2 px | 0.46 | 1.20 | 2511 |
| stroke 73 | 69 % → 80 % | 1631.5 px | 0.48 | 1.15 | 1240 |
| stroke 74 | 67 % → 75 % | 659.5 px | 0.48 | 1.13 | 3352 |
| stroke 75 | 66 % → 72 % | 1274.5 px | 0.46 | 1.09 | 1336 |
| stroke 76 | 77 % → 80 % | 1029.7 px | 0.51 | 1.03 | 3760 |
| stroke 77 | 78 % → 78 % | 1268.8 px | 0.50 | 1.01 | 1458 |
| stroke 78 | 79 % → 79 % | 1431.1 px | 0.50 | 1.01 | 1384 |
| stroke 79 | 76 % → 81 % | 1261.4 px | 0.51 | 1.06 | 1727 |
| stroke 80 | 75 % → 76 % | 592.9 px | 0.46 | 1.02 | 3222 |
| stroke 81 | 77 % → 77 % | 1232.5 px | 0.48 | 1.00 | 1660 |
| stroke 82 | 78 % → 78 % | 978.8 px | 0.49 | 1.00 | 2155 |
| stroke 83 | 83 % → 82 % | 1049.8 px | 0.48 | 1.00 | 397 |
| stroke 84 | 95 % → 95 % | 2269.9 px | 0.55 | 1.00 | 378 |
| stroke 85 | 92 % → 91 % | 2182.3 px | 0.37 | 0.99 | 72 |

Numbers say: wet paint spreads well beyond the stroke.

## Refs v3 · #11 HW purple balls — own sheet
own sheet 800 × 985 · Gouache 1.00 + turpentine 30 % · 104 px · 806.4 s

![Refs v3 · #11 HW purple balls — own sheet](Refs-v3-11-HW-purple-balls-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 7 % → 87 % | 95.6 px | 0.31 | 12.05 | 2195 |
| stroke 2 | 17 % → 88 % | 140.3 px | 0.16 | 5.25 | 5347 |
| stroke 3 | 23 % → 88 % | 257.6 px | 0.21 | 3.80 | 3623 |
| stroke 4 | 20 % → 66 % | 193.2 px | 0.04 | 3.32 | 1845 |
| stroke 5 | 16 % → 86 % | 84.8 px | 0.04 | 5.38 | 4814 |
| stroke 6 | 24 % → 71 % | 252.2 px | 0.04 | 2.88 | 2729 |
| stroke 7 | 23 % → 90 % | 185.8 px | 0.05 | 3.91 | 2657 |
| stroke 8 | 32 % → 77 % | 265.7 px | 0.04 | 2.44 | 4111 |
| stroke 9 | 38 % → 86 % | 293.9 px | 0.04 | 2.27 | 6030 |
| stroke 10 | 52 % → 87 % | 481.7 px | 0.05 | 1.66 | 5341 |
| stroke 11 | 49 % → 92 % | 293.7 px | 0.04 | 1.87 | 6203 |
| stroke 12 | 65 % → 88 % | 355.0 px | 0.04 | 1.36 | 5763 |
| stroke 13 | 58 % → 92 % | 553.3 px | 0.09 | 1.59 | 3797 |
| stroke 14 | 68 % → 98 % | 1566.9 px | 0.08 | 1.45 | 1498 |
| stroke 15 | 46 % → 85 % | 459.7 px | 0.22 | 1.84 | 3285 |
| stroke 16 | 53 % → 89 % | 783.0 px | 0.18 | 1.70 | 3264 |
| stroke 17 | 71 % → 83 % | 853.4 px | 0.04 | 1.17 | 2744 |
| stroke 18 | 70 % → 89 % | 516.8 px | 0.04 | 1.28 | 4351 |
| stroke 19 | 73 % → 89 % | 880.6 px | 0.04 | 1.22 | 2238 |
| stroke 20 | 84 % → 98 % | 1965.4 px | 0.04 | 1.17 | 1512 |
| stroke 21 | 72 % → 81 % | 864.7 px | 0.04 | 1.13 | 3597 |
| stroke 22 | 48 % → 86 % | 607.2 px | 0.25 | 1.79 | 3692 |
| stroke 23 | 71 % → 75 % | 863.8 px | 0.04 | 1.06 | 2531 |
| stroke 24 | 85 % → 95 % | 1117.9 px | 0.04 | 1.12 | 3788 |
| stroke 25 | 85 % → 91 % | 1279.4 px | 0.04 | 1.07 | 2884 |
| stroke 26 | 80 % → 85 % | 710.2 px | 0.04 | 1.06 | 2966 |
| stroke 27 | 79 % → 81 % | 1806.1 px | 0.04 | 1.03 | 1322 |
| stroke 28 | 88 % → 91 % | 1492.2 px | 0.04 | 1.03 | 2018 |
| stroke 29 | 89 % → 97 % | 1809.3 px | 0.05 | 1.09 | 1702 |
| stroke 30 | 67 % → 88 % | 1192.2 px | 0.15 | 1.31 | 1929 |
| stroke 31 | 71 % → 97 % | 1617.7 px | 0.19 | 1.36 | 1212 |
| stroke 32 | 64 % → 78 % | 1045.9 px | 0.14 | 1.22 | 1215 |
| stroke 33 | 79 % → 82 % | 1034.2 px | 0.04 | 1.03 | 2011 |
| stroke 34 | 86 % → 87 % | 1491.4 px | 0.04 | 1.01 | 1459 |
| stroke 35 | 95 % → 97 % | 2300.2 px | 0.04 | 1.03 | 1350 |
| stroke 36 | 79 % → 80 % | 802.2 px | 0.04 | 1.01 | 3817 |
| stroke 37 | 52 % → 77 % | 513.0 px | 0.26 | 1.50 | 5343 |
| stroke 38 | 88 % → 90 % | 1518.0 px | 0.04 | 1.03 | 2721 |
| stroke 39 | 42 % → 79 % | 612.2 px | 0.33 | 1.87 | 4260 |
| stroke 40 | 76 % → 90 % | 1734.3 px | 0.13 | 1.18 | 1978 |
| stroke 41 | 96 % → 98 % | 2267.3 px | 0.04 | 1.02 | 1980 |
| stroke 42 | 93 % → 93 % | 2027.5 px | 0.04 | 0.99 | 1922 |
| stroke 43 | 66 % → 79 % | 534.3 px | 0.16 | 1.21 | 6112 |
| stroke 44 | 88 % → 87 % | 2075.9 px | 0.04 | 0.99 | 1933 |
| stroke 45 | 53 % → 92 % | 1144.0 px | 0.33 | 1.72 | 1539 |
| stroke 46 | 69 % → 96 % | 1096.8 px | 0.24 | 1.39 | 2635 |
| stroke 47 | 92 % → 92 % | 1810.6 px | 0.04 | 0.99 | 1325 |
| stroke 48 | 80 % → 79 % | 1388.5 px | 0.03 | 0.99 | 1451 |
| stroke 49 | 89 % → 88 % | 1705.8 px | 0.06 | 1.00 | 1918 |
| stroke 50 | 90 % → 89 % | 1453.4 px | 0.04 | 0.99 | 1354 |
| stroke 51 | 70 % → 98 % | 1923.4 px | 0.25 | 1.40 | 211 |
| stroke 52 | 71 % → 99 % | 2938.4 px | 0.26 | 1.39 | 118 |
| stroke 53 | 61 % → 97 % | 3424.0 px | 0.31 | 1.59 | 69 |
| stroke 54 | 65 % → 99 % | 6186.6 px | 0.30 | 1.53 | 37 |
| stroke 55 | 68 % → 96 % | 6465.7 px | 0.27 | 1.43 | 37 |
| stroke 56 | 58 % → 98 % | 4486.9 px | 0.33 | 1.67 | 59 |
| stroke 57 | 68 % → 98 % | 2042.7 px | 0.27 | 1.45 | 198 |
| stroke 58 | 74 % → 98 % | 2691.0 px | 0.23 | 1.32 | 141 |
| stroke 59 | 64 % → 98 % | 6152.1 px | 0.30 | 1.53 | 53 |
| stroke 60 | 82 % → 81 % | 2518.9 px | 0.04 | 0.99 | 62 |
| stroke 61 | 64 % → 76 % | 1255.1 px | 0.16 | 1.18 | 241 |
| stroke 62 | 29 % → 76 % | 980.4 px | 0.45 | 2.66 | 66 |
| stroke 63 | 37 % → 70 % | 1033.7 px | 0.37 | 1.90 | 96 |
| stroke 64 | 20 % → 64 % | 539.5 px | 0.51 | 3.17 | 54 |
| stroke 65 | 3 % → 87 % | 17.8 px | 0.65 | 25.55 | 240 |
| stroke 66 | 10 % → 99 % | 216.5 px | 0.63 | 9.98 | 68 |
| stroke 67 | 54 % → 85 % | 255.9 px | 0.45 | 1.58 | 7866 |
| stroke 68 | 69 % → 92 % | 642.4 px | 0.40 | 1.33 | 4786 |
| stroke 69 | 69 % → 80 % | 323.8 px | 0.49 | 1.17 | 7599 |
| stroke 70 | 82 % → 89 % | 939.7 px | 0.35 | 1.09 | 4548 |
| stroke 71 | 76 % → 79 % | 889.7 px | 0.42 | 1.04 | 2656 |
| stroke 72 | 72 % → 83 % | 1017.4 px | 0.55 | 1.16 | 1538 |
| stroke 73 | 76 % → 78 % | 1200.6 px | 0.38 | 1.03 | 1865 |
| stroke 74 | 77 % → 83 % | 1084.0 px | 0.44 | 1.07 | 2174 |
| stroke 75 | 91 % → 94 % | 790.5 px | 0.62 | 1.04 | 1620 |
| stroke 76 | 96 % → 96 % | 2149.4 px | 0.40 | 1.00 | 1437 |
| stroke 77 | 76 % → 76 % | 570.7 px | 0.46 | 1.00 | 2409 |
| stroke 78 | 80 % → 80 % | 1157.8 px | 0.52 | 1.00 | 1446 |
| stroke 79 | 97 % → 96 % | 1507.2 px | 0.43 | 1.00 | 1993 |
| stroke 80 | 85 % → 84 % | 817.3 px | 0.60 | 1.00 | 2257 |

Numbers say: wet paint spreads well beyond the stroke.

## Refs v3 · #12 HW black-olive cage — own sheet
own sheet 800 × 1150 · Gouache 1.00 + turpentine 30 % · 36 px · 2069.4 s

![Refs v3 · #12 HW black-olive cage — own sheet](Refs-v3-12-HW-black-olive-cage-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 17 % → 83 % | 35.0 px | 0.15 | 4.87 | 441 |
| stroke 2 | 27 % → 73 % | 90.9 px | 0.16 | 2.66 | 99 |
| stroke 3 | 24 % → 91 % | 66.8 px | 0.16 | 3.73 | 261 |
| stroke 4 | 22 % → 94 % | 50.0 px | 0.27 | 4.31 | 244 |
| stroke 5 | 36 % → 90 % | 95.9 px | 0.14 | 2.46 | 201 |
| stroke 6 | 29 % → 77 % | 81.3 px | 0.17 | 2.70 | 277 |
| stroke 7 | 39 % → 90 % | 183.0 px | 0.16 | 2.34 | 108 |
| stroke 8 | 51 % → 91 % | 282.2 px | 0.16 | 1.78 | 82 |
| stroke 9 | 34 % → 73 % | 107.3 px | 0.15 | 2.13 | 262 |
| stroke 10 | 11 % → 70 % | 34.7 px | 0.10 | 6.57 | 373 |
| stroke 11 | 17 % → 83 % | 129.4 px | 0.08 | 4.78 | 115 |
| stroke 12 | 21 % → 79 % | 107.4 px | 0.08 | 3.74 | 259 |
| stroke 13 | 27 % → 74 % | 96.1 px | 0.12 | 2.78 | 365 |
| stroke 14 | 25 % → 92 % | 141.5 px | 0.09 | 3.68 | 262 |
| stroke 15 | 37 % → 87 % | 175.9 px | 0.09 | 2.35 | 245 |
| stroke 16 | 41 % → 73 % | 335.1 px | 0.11 | 1.78 | 97 |
| stroke 17 | 30 % → 89 % | 166.5 px | 0.09 | 2.93 | 290 |
| stroke 18 | 45 % → 74 % | 347.7 px | 0.09 | 1.64 | 125 |
| stroke 19 | 31 % → 91 % | 235.2 px | 0.10 | 2.90 | 137 |
| stroke 20 | 25 % → 96 % | 183.3 px | 0.15 | 3.78 | 112 |
| stroke 21 | 35 % → 93 % | 310.2 px | 0.11 | 2.66 | 96 |
| stroke 22 | 42 % → 89 % | 263.7 px | 0.08 | 2.12 | 137 |
| stroke 23 | 50 % → 75 % | 432.9 px | 0.08 | 1.51 | 115 |
| stroke 24 | 36 % → 58 % | 312.8 px | 0.12 | 1.61 | 141 |
| stroke 25 | 50 % → 93 % | 471.3 px | 0.10 | 1.84 | 81 |
| stroke 26 | 7 % → 28 % | 36.3 px | 0.15 | 3.78 | 82 |
| stroke 27 | 9 % → 29 % | 49.4 px | 0.17 | 3.37 | 116 |
| stroke 28 | 12 % → 24 % | 77.9 px | 0.16 | 1.96 | 84 |
| stroke 29 | 13 % → 88 % | 34.6 px | 0.20 | 6.74 | 278 |
| stroke 30 | 12 % → 56 % | 44.9 px | 0.20 | 4.73 | 407 |
| stroke 31 | 29 % → 84 % | 63.0 px | 0.19 | 2.85 | 523 |
| stroke 32 | 12 % → 75 % | 32.4 px | 0.20 | 5.99 | 310 |
| stroke 33 | 38 % → 91 % | 99.2 px | 0.19 | 2.41 | 218 |
| stroke 34 | 38 % → 90 % | 92.9 px | 0.20 | 2.34 | 394 |
| stroke 35 | 40 % → 89 % | 177.6 px | 0.20 | 2.24 | 128 |
| stroke 36 | 32 % → 68 % | 215.6 px | 0.17 | 2.13 | 89 |
| stroke 37 | 9 % → 95 % | 34.9 px | 0.33 | 10.37 | 376 |
| stroke 38 | 17 % → 99 % | 57.3 px | 0.29 | 5.93 | 360 |
| stroke 39 | 24 % → 98 % | 72.7 px | 0.33 | 4.08 | 425 |
| stroke 40 | 23 % → 100 % | 107.9 px | 0.37 | 4.37 | 244 |
| stroke 41 | 29 % → 100 % | 100.6 px | 0.36 | 3.50 | 364 |
| stroke 42 | 32 % → 98 % | 105.7 px | 0.29 | 3.08 | 483 |
| stroke 43 | 40 % → 100 % | 268.5 px | 0.27 | 2.48 | 124 |
| stroke 44 | 19 % → 92 % | 110.1 px | 0.31 | 4.82 | 178 |
| stroke 45 | 34 % → 96 % | 158.6 px | 0.28 | 2.86 | 276 |
| stroke 46 | 41 % → 100 % | 300.9 px | 0.30 | 2.46 | 144 |
| stroke 47 | 8 % → 72 % | 35.4 px | 0.20 | 8.99 | 192 |
| stroke 48 | 8 % → 51 % | 36.0 px | 0.16 | 6.74 | 274 |
| stroke 49 | 17 % → 60 % | 124.3 px | 0.16 | 3.60 | 96 |
| stroke 50 | 16 % → 62 % | 70.7 px | 0.16 | 3.81 | 222 |
| stroke 51 | 19 % → 68 % | 90.9 px | 0.20 | 3.62 | 298 |
| stroke 52 | 19 % → 45 % | 87.9 px | 0.16 | 2.35 | 599 |
| stroke 53 | 31 % → 66 % | 200.9 px | 0.16 | 2.10 | 177 |
| stroke 54 | 19 % → 77 % | 172.0 px | 0.22 | 3.97 | 113 |
| stroke 55 | 34 % → 64 % | 344.5 px | 0.16 | 1.88 | 89 |
| stroke 56 | 9 % → 60 % | 34.7 px | 0.04 | 6.38 | 343 |
| stroke 57 | 24 % → 91 % | 64.6 px | 0.04 | 3.75 | 188 |
| stroke 58 | 8 % → 50 % | 59.4 px | 0.04 | 6.21 | 91 |
| stroke 59 | 22 % → 54 % | 76.7 px | 0.04 | 2.52 | 170 |
| stroke 60 | 33 % → 66 % | 94.0 px | 0.04 | 2.02 | 441 |
| stroke 61 | 48 % → 74 % | 115.4 px | 0.04 | 1.54 | 490 |
| stroke 62 | 34 % → 68 % | 167.2 px | 0.04 | 2.01 | 192 |
| stroke 63 | 35 % → 47 % | 172.2 px | 0.03 | 1.33 | 143 |
| stroke 64 | 38 % → 53 % | 156.5 px | 0.03 | 1.40 | 247 |
| stroke 65 | 34 % → 46 % | 227.2 px | 0.04 | 1.35 | 103 |
| stroke 66 | 58 % → 65 % | 181.0 px | 0.04 | 1.11 | 292 |
| stroke 67 | 30 % → 77 % | 170.0 px | 0.07 | 2.59 | 152 |
| stroke 68 | 49 % → 69 % | 460.8 px | 0.04 | 1.40 | 72 |
| stroke 69 | 59 % → 71 % | 249.6 px | 0.04 | 1.20 | 248 |
| stroke 70 | 42 % → 44 % | 196.7 px | 0.04 | 1.04 | 179 |
| stroke 71 | 54 % → 74 % | 311.9 px | 0.04 | 1.38 | 137 |
| stroke 72 | 86 % → 90 % | 253.2 px | 0.04 | 1.05 | 257 |
| stroke 73 | 54 % → 59 % | 218.4 px | 0.04 | 1.08 | 363 |
| stroke 74 | 76 % → 82 % | 266.4 px | 0.04 | 1.07 | 324 |
| stroke 75 | 58 % → 70 % | 317.6 px | 0.04 | 1.20 | 177 |
| stroke 76 | 55 % → 75 % | 317.3 px | 0.04 | 1.36 | 158 |
| stroke 77 | 50 % → 75 % | 336.6 px | 0.05 | 1.50 | 138 |
| stroke 78 | 74 % → 73 % | 428.4 px | 0.04 | 0.99 | 142 |
| stroke 79 | 33 % → 77 % | 286.4 px | 0.10 | 2.30 | 90 |
| stroke 80 | 64 % → 67 % | 458.3 px | 0.03 | 1.04 | 101 |
| stroke 81 | 72 % → 73 % | 485.7 px | 0.04 | 1.02 | 144 |
| stroke 82 | 48 % → 76 % | 409.7 px | 0.06 | 1.58 | 92 |
| stroke 83 | 5 % → 8 % | 38.4 px | 0.02 | 1.78 | 65 |
| stroke 84 | 10 % → 9 % | 86.5 px | 0.02 | 0.88 | 59 |
| stroke 85 | 18 % → 31 % | 36.2 px | 0.03 | 1.74 | 238 |
| stroke 86 | 22 % → 30 % | 51.6 px | 0.03 | 1.35 | 254 |
| stroke 87 | 33 % → 35 % | 73.8 px | 0.03 | 1.06 | 182 |
| stroke 88 | 30 % → 29 % | 183.6 px | 0.03 | 0.97 | 87 |
| stroke 89 | 5 % → 47 % | 14.8 px | 0.24 | 9.21 | 261 |
| stroke 90 | 6 % → 53 % | 18.1 px | 0.08 | 8.58 | 37 |
| stroke 91 | 6 % → 45 % | 32.8 px | 0.14 | 7.14 | 176 |
| stroke 92 | 8 % → 63 % | 44.1 px | 0.11 | 8.38 | 63 |
| stroke 93 | 4 % → 70 % | 19.6 px | 0.15 | 16.79 | 176 |
| stroke 94 | 4 % → 91 % | 23.7 px | 0.27 | 25.04 | 101 |
| stroke 95 | 7 % → 90 % | 63.2 px | 0.27 | 12.74 | 48 |
| stroke 96 | 4 % → 89 % | 16.7 px | 0.32 | 22.36 | 42 |
| stroke 97 | 19 % → 87 % | 79.1 px | 0.26 | 4.57 | 114 |
| stroke 98 | 36 % → 63 % | 104.1 px | 0.12 | 1.77 | 186 |
| stroke 99 | 7 % → 86 % | 29.6 px | 0.45 | 11.85 | 406 |
| stroke 100 | 6 % → 89 % | 32.7 px | 0.36 | 14.99 | 154 |
| stroke 101 | 6 % → 94 % | 34.8 px | 0.31 | 15.40 | 245 |
| stroke 102 | 10 % → 73 % | 77.5 px | 0.24 | 7.03 | 185 |
| stroke 103 | 32 % → 33 % | 113.9 px | 0.06 | 1.02 | 276 |
| stroke 104 | 14 % → 65 % | 82.5 px | 0.16 | 4.52 | 125 |
| stroke 105 | 24 % → 76 % | 130.9 px | 0.16 | 3.16 | 168 |
| stroke 106 | 41 % → 64 % | 212.1 px | 0.10 | 1.55 | 254 |
| stroke 107 | 27 % → 69 % | 93.3 px | 0.16 | 2.54 | 411 |
| stroke 108 | 47 % → 85 % | 505.5 px | 0.17 | 1.82 | 61 |
| stroke 109 | 30 % → 95 % | 120.8 px | 0.19 | 3.22 | 400 |
| stroke 110 | 44 % → 76 % | 192.1 px | 0.15 | 1.72 | 232 |
| stroke 111 | 23 % → 97 % | 90.1 px | 0.26 | 4.20 | 262 |
| stroke 112 | 47 % → 76 % | 230.7 px | 0.15 | 1.61 | 187 |
| stroke 113 | 61 % → 90 % | 233.5 px | 0.15 | 1.48 | 380 |
| stroke 114 | 55 % → 96 % | 308.4 px | 0.12 | 1.75 | 173 |
| stroke 115 | 56 % → 93 % | 530.9 px | 0.13 | 1.65 | 54 |
| stroke 116 | 47 % → 91 % | 324.6 px | 0.13 | 1.91 | 146 |
| stroke 117 | 71 % → 91 % | 297.5 px | 0.14 | 1.28 | 452 |
| stroke 118 | 30 % → 96 % | 274.9 px | 0.29 | 3.23 | 67 |
| stroke 119 | 65 % → 94 % | 616.4 px | 0.13 | 1.44 | 63 |
| stroke 120 | 69 % → 96 % | 791.3 px | 0.10 | 1.38 | 68 |
| stroke 121 | 49 % → 96 % | 418.9 px | 0.19 | 1.97 | 109 |
| stroke 122 | 76 % → 94 % | 624.7 px | 0.13 | 1.24 | 82 |
| stroke 123 | 57 % → 99 % | 553.5 px | 0.18 | 1.75 | 61 |
| stroke 124 | 38 % → 69 % | 255.0 px | 0.13 | 1.81 | 71 |
| stroke 125 | 38 % → 96 % | 383.1 px | 0.22 | 2.49 | 80 |
| stroke 126 | 78 % → 95 % | 635.5 px | 0.11 | 1.21 | 93 |
| stroke 127 | 9 % → 82 % | 53.2 px | 0.12 | 9.16 | 126 |
| stroke 128 | 13 % → 73 % | 95.4 px | 0.12 | 5.70 | 121 |
| stroke 129 | 15 % → 87 % | 160.6 px | 0.12 | 5.94 | 44 |
| stroke 130 | 16 % → 78 % | 158.0 px | 0.12 | 4.95 | 74 |
| stroke 131 | 17 % → 81 % | 194.8 px | 0.12 | 4.82 | 51 |
| stroke 132 | 38 % → 80 % | 139.8 px | 0.19 | 2.08 | 216 |
| stroke 133 | 22 % → 69 % | 102.8 px | 0.19 | 3.09 | 232 |
| stroke 134 | 28 % → 61 % | 126.9 px | 0.20 | 2.21 | 457 |
| stroke 135 | 16 % → 78 % | 179.1 px | 0.18 | 5.01 | 59 |
| stroke 136 | 40 % → 76 % | 262.4 px | 0.20 | 1.89 | 134 |
| stroke 137 | 46 % → 73 % | 338.8 px | 0.19 | 1.60 | 108 |
| stroke 138 | 50 % → 87 % | 215.2 px | 0.20 | 1.73 | 160 |
| stroke 139 | 26 % → 68 % | 296.4 px | 0.18 | 2.62 | 52 |
| stroke 140 | 45 % → 63 % | 462.9 px | 0.18 | 1.40 | 53 |
| stroke 141 | 33 % → 94 % | 142.2 px | 0.24 | 2.84 | 134 |
| stroke 142 | 34 % → 95 % | 174.7 px | 0.27 | 2.82 | 133 |
| stroke 143 | 45 % → 93 % | 307.8 px | 0.19 | 2.07 | 71 |
| stroke 144 | 16 % → 93 % | 69.8 px | 0.25 | 5.82 | 177 |
| stroke 145 | 34 % → 93 % | 365.7 px | 0.23 | 2.76 | 43 |
| stroke 146 | 23 % → 93 % | 187.4 px | 0.25 | 4.09 | 86 |
| stroke 147 | 22 % → 93 % | 240.9 px | 0.21 | 4.23 | 36 |
| stroke 148 | 15 % → 98 % | 140.4 px | 0.21 | 6.46 | 58 |
| stroke 149 | 37 % → 92 % | 402.5 px | 0.24 | 2.49 | 40 |
| stroke 150 | 17 % → 56 % | 72.4 px | 0.24 | 3.26 | 229 |
| stroke 151 | 28 % → 73 % | 118.1 px | 0.18 | 2.61 | 213 |
| stroke 152 | 22 % → 59 % | 96.1 px | 0.25 | 2.67 | 300 |
| stroke 153 | 32 % → 68 % | 129.4 px | 0.19 | 2.15 | 1079 |
| stroke 154 | 35 % → 60 % | 191.2 px | 0.19 | 1.74 | 221 |
| stroke 155 | 32 % → 81 % | 120.7 px | 0.28 | 2.54 | 530 |
| stroke 156 | 32 % → 83 % | 144.9 px | 0.30 | 2.57 | 331 |
| stroke 157 | 38 % → 75 % | 156.9 px | 0.20 | 2.00 | 278 |
| stroke 158 | 41 % → 88 % | 445.2 px | 0.19 | 2.15 | 58 |
| stroke 159 | 33 % → 79 % | 113.6 px | 0.21 | 2.39 | 371 |
| stroke 160 | 27 % → 91 % | 69.2 px | 0.37 | 3.34 | 332 |
| stroke 161 | 30 % → 95 % | 95.6 px | 0.40 | 3.15 | 235 |
| stroke 162 | 25 % → 46 % | 177.1 px | 0.22 | 1.88 | 79 |
| stroke 163 | 39 % → 74 % | 341.4 px | 0.22 | 1.91 | 122 |
| stroke 164 | 41 % → 93 % | 125.6 px | 0.33 | 2.27 | 200 |
| stroke 165 | 45 % → 80 % | 491.5 px | 0.19 | 1.80 | 70 |
| stroke 166 | 44 % → 71 % | 304.0 px | 0.18 | 1.63 | 140 |
| stroke 167 | 41 % → 81 % | 163.0 px | 0.27 | 1.96 | 341 |
| stroke 168 | 43 % → 80 % | 273.0 px | 0.23 | 1.85 | 103 |
| stroke 169 | 44 % → 83 % | 315.8 px | 0.24 | 1.86 | 113 |
| stroke 170 | 37 % → 81 % | 205.0 px | 0.21 | 2.21 | 119 |
| stroke 171 | 40 % → 93 % | 172.2 px | 0.35 | 2.34 | 153 |
| stroke 172 | 44 % → 75 % | 290.1 px | 0.20 | 1.70 | 158 |
| stroke 173 | 46 % → 89 % | 318.0 px | 0.25 | 1.93 | 222 |
| stroke 174 | 37 % → 91 % | 176.2 px | 0.37 | 2.45 | 140 |
| stroke 175 | 42 % → 71 % | 456.9 px | 0.17 | 1.68 | 134 |
| stroke 176 | 38 % → 74 % | 216.8 px | 0.20 | 1.93 | 132 |
| stroke 177 | 49 % → 79 % | 463.6 px | 0.19 | 1.62 | 70 |
| stroke 178 | 41 % → 86 % | 191.7 px | 0.22 | 2.06 | 166 |
| stroke 179 | 43 % → 89 % | 337.5 px | 0.34 | 2.06 | 75 |
| stroke 180 | 47 % → 84 % | 325.6 px | 0.22 | 1.77 | 116 |
| stroke 181 | 46 % → 83 % | 314.2 px | 0.20 | 1.80 | 91 |
| stroke 182 | 38 % → 94 % | 161.7 px | 0.39 | 2.52 | 139 |
| stroke 183 | 42 % → 95 % | 185.0 px | 0.38 | 2.27 | 81 |
| stroke 184 | 43 % → 67 % | 226.9 px | 0.19 | 1.55 | 155 |
| stroke 185 | 46 % → 70 % | 377.4 px | 0.18 | 1.51 | 75 |
| stroke 186 | 39 % → 48 % | 285.2 px | 0.18 | 1.22 | 90 |
| stroke 187 | 46 % → 76 % | 290.7 px | 0.20 | 1.64 | 136 |
| stroke 188 | 38 % → 57 % | 302.9 px | 0.21 | 1.50 | 103 |
| stroke 189 | 51 % → 77 % | 505.4 px | 0.20 | 1.50 | 80 |
| stroke 190 | 17 % → 85 % | 169.8 px | 0.27 | 4.96 | 46 |
| stroke 191 | 20 % → 87 % | 103.8 px | 0.27 | 4.43 | 157 |
| stroke 192 | 26 % → 83 % | 125.5 px | 0.27 | 3.22 | 209 |
| stroke 193 | 27 % → 54 % | 255.2 px | 0.15 | 2.00 | 39 |
| stroke 194 | 16 % → 71 % | 97.9 px | 0.11 | 4.43 | 74 |
| stroke 195 | 28 % → 72 % | 296.9 px | 0.09 | 2.61 | 29 |
| stroke 196 | 11 % → 66 % | 78.8 px | 0.17 | 5.75 | 69 |
| stroke 197 | 10 % → 97 % | 53.2 px | 0.24 | 9.76 | 110 |
| stroke 198 | 11 % → 99 % | 50.0 px | 0.37 | 8.60 | 171 |
| stroke 199 | 37 % → 89 % | 150.6 px | 0.22 | 2.37 | 120 |
| stroke 200 | 25 % → 75 % | 99.7 px | 0.29 | 3.07 | 230 |
| stroke 201 | 21 % → 87 % | 120.6 px | 0.40 | 4.11 | 87 |
| stroke 202 | 6 % → 96 % | 35.8 px | 0.45 | 15.72 | 63 |
| stroke 203 | 22 % → 96 % | 142.9 px | 0.34 | 4.27 | 107 |
| stroke 204 | 33 % → 94 % | 275.2 px | 0.34 | 2.88 | 51 |
| stroke 205 | 25 % → 66 % | 100.9 px | 0.17 | 2.66 | 2171 |
| stroke 206 | 35 % → 84 % | 68.7 px | 0.19 | 2.42 | 1517 |
| stroke 207 | 34 % → 65 % | 104.3 px | 0.11 | 1.92 | 2035 |
| stroke 208 | 38 % → 52 % | 109.5 px | 0.10 | 1.36 | 970 |
| stroke 209 | 48 % → 52 % | 173.6 px | 0.10 | 1.08 | 944 |
| stroke 210 | 52 % → 81 % | 279.0 px | 0.16 | 1.57 | 531 |
| stroke 211 | 37 % → 79 % | 142.7 px | 0.21 | 2.14 | 1012 |
| stroke 212 | 60 % → 71 % | 186.4 px | 0.10 | 1.17 | 1305 |
| stroke 213 | 53 % → 80 % | 181.2 px | 0.17 | 1.52 | 1576 |
| stroke 214 | 53 % → 95 % | 211.3 px | 0.17 | 1.78 | 687 |
| stroke 215 | 62 % → 83 % | 201.1 px | 0.13 | 1.34 | 1238 |
| stroke 216 | 61 % → 98 % | 196.0 px | 0.14 | 1.59 | 1226 |
| stroke 217 | 60 % → 99 % | 308.1 px | 0.21 | 1.66 | 449 |
| stroke 218 | 69 % → 95 % | 291.3 px | 0.14 | 1.38 | 639 |
| stroke 219 | 60 % → 82 % | 253.8 px | 0.13 | 1.38 | 884 |
| stroke 220 | 70 % → 100 % | 272.4 px | 0.17 | 1.42 | 945 |
| stroke 221 | 58 % → 59 % | 186.0 px | 0.11 | 1.01 | 687 |
| stroke 222 | 73 % → 90 % | 347.5 px | 0.13 | 1.23 | 872 |
| stroke 223 | 72 % → 92 % | 363.8 px | 0.17 | 1.27 | 570 |
| stroke 224 | 71 % → 93 % | 258.2 px | 0.17 | 1.31 | 968 |
| stroke 225 | 68 % → 82 % | 268.3 px | 0.11 | 1.21 | 904 |
| stroke 226 | 53 % → 70 % | 224.2 px | 0.17 | 1.33 | 1422 |
| stroke 227 | 68 % → 97 % | 275.0 px | 0.22 | 1.42 | 710 |
| stroke 228 | 71 % → 71 % | 273.2 px | 0.11 | 1.00 | 1037 |
| stroke 229 | 59 % → 73 % | 285.6 px | 0.14 | 1.23 | 724 |
| stroke 230 | 56 % → 71 % | 336.6 px | 0.15 | 1.26 | 496 |
| stroke 231 | 82 % → 87 % | 441.2 px | 0.10 | 1.06 | 447 |
| stroke 232 | 38 % → 49 % | 148.3 px | 0.11 | 1.30 | 293 |
| stroke 233 | 47 % → 54 % | 175.3 px | 0.15 | 1.16 | 600 |
| stroke 234 | 63 % → 68 % | 270.7 px | 0.13 | 1.08 | 437 |
| stroke 235 | 72 % → 93 % | 256.1 px | 0.18 | 1.29 | 1390 |
| stroke 236 | 70 % → 97 % | 388.0 px | 0.21 | 1.39 | 445 |
| stroke 237 | 81 % → 93 % | 445.8 px | 0.17 | 1.15 | 639 |
| stroke 238 | 68 % → 73 % | 360.9 px | 0.11 | 1.07 | 533 |
| stroke 239 | 65 % → 70 % | 574.4 px | 0.12 | 1.08 | 149 |
| stroke 240 | 76 % → 81 % | 771.6 px | 0.11 | 1.06 | 183 |
| stroke 241 | 71 % → 75 % | 619.0 px | 0.12 | 1.05 | 181 |
| stroke 242 | 83 % → 96 % | 569.3 px | 0.13 | 1.16 | 311 |
| stroke 243 | 73 % → 78 % | 270.2 px | 0.13 | 1.08 | 1069 |
| stroke 244 | 81 % → 85 % | 312.2 px | 0.13 | 1.05 | 1291 |
| stroke 245 | 80 % → 84 % | 403.5 px | 0.13 | 1.05 | 480 |
| stroke 246 | 53 % → 62 % | 236.4 px | 0.19 | 1.17 | 716 |
| stroke 247 | 59 % → 70 % | 325.8 px | 0.19 | 1.18 | 370 |
| stroke 248 | 44 % → 89 % | 134.1 px | 0.27 | 2.02 | 541 |
| stroke 249 | 45 % → 93 % | 194.8 px | 0.30 | 2.05 | 488 |
| stroke 250 | 61 % → 90 % | 218.2 px | 0.22 | 1.47 | 602 |
| stroke 251 | 48 % → 96 % | 312.1 px | 0.30 | 1.99 | 122 |
| stroke 252 | 42 % → 82 % | 185.9 px | 0.27 | 1.96 | 348 |
| stroke 253 | 19 % → 100 % | 67.4 px | 0.46 | 5.23 | 388 |
| stroke 254 | 56 % → 92 % | 204.1 px | 0.29 | 1.64 | 448 |
| stroke 255 | 63 % → 99 % | 327.4 px | 0.29 | 1.58 | 201 |
| stroke 256 | 25 % → 100 % | 117.5 px | 0.47 | 4.00 | 259 |
| stroke 257 | 48 % → 99 % | 308.8 px | 0.38 | 2.05 | 166 |
| stroke 258 | 63 % → 84 % | 281.9 px | 0.21 | 1.33 | 345 |
| stroke 259 | 43 % → 82 % | 196.8 px | 0.28 | 1.90 | 277 |
| stroke 260 | 50 % → 85 % | 240.7 px | 0.26 | 1.71 | 235 |
| stroke 261 | 70 % → 88 % | 313.4 px | 0.24 | 1.27 | 369 |
| stroke 262 | 79 % → 99 % | 313.0 px | 0.24 | 1.26 | 240 |
| stroke 263 | 51 % → 84 % | 295.7 px | 0.28 | 1.63 | 249 |
| stroke 264 | 80 % → 93 % | 428.3 px | 0.24 | 1.15 | 226 |
| stroke 265 | 65 % → 100 % | 483.4 px | 0.32 | 1.54 | 115 |
| stroke 266 | 55 % → 87 % | 175.5 px | 0.31 | 1.58 | 511 |
| stroke 267 | 66 % → 89 % | 396.1 px | 0.31 | 1.36 | 175 |
| stroke 268 | 78 % → 86 % | 761.8 px | 0.28 | 1.10 | 80 |
| stroke 269 | 77 % → 98 % | 360.2 px | 0.27 | 1.27 | 247 |
| stroke 270 | 76 % → 94 % | 317.0 px | 0.28 | 1.24 | 384 |
| stroke 271 | 77 % → 86 % | 271.1 px | 0.21 | 1.12 | 371 |
| stroke 272 | 70 % → 86 % | 499.8 px | 0.28 | 1.24 | 142 |
| stroke 273 | 83 % → 88 % | 559.4 px | 0.20 | 1.06 | 127 |
| stroke 274 | 60 % → 96 % | 405.7 px | 0.28 | 1.59 | 115 |
| stroke 275 | 72 % → 92 % | 332.3 px | 0.25 | 1.28 | 232 |
| stroke 276 | 54 % → 98 % | 241.9 px | 0.30 | 1.81 | 235 |
| stroke 277 | 52 % → 99 % | 441.3 px | 0.41 | 1.93 | 97 |
| stroke 278 | 87 % → 92 % | 569.9 px | 0.23 | 1.06 | 181 |
| stroke 279 | 74 % → 85 % | 692.3 px | 0.25 | 1.15 | 80 |
| stroke 280 | 88 % → 93 % | 457.0 px | 0.20 | 1.05 | 209 |
| stroke 281 | 88 % → 99 % | 345.7 px | 0.22 | 1.13 | 320 |
| stroke 282 | 86 % → 90 % | 354.2 px | 0.22 | 1.04 | 335 |
| stroke 283 | 91 % → 91 % | 733.4 px | 0.22 | 1.00 | 119 |
| stroke 284 | 91 % → 90 % | 903.6 px | 0.21 | 1.00 | 136 |
| stroke 285 | 44 % → 99 % | 429.5 px | 0.41 | 2.25 | 134 |
| stroke 286 | 58 % → 100 % | 356.6 px | 0.30 | 1.74 | 234 |
| stroke 287 | 46 % → 100 % | 425.1 px | 0.44 | 2.19 | 108 |
| stroke 288 | 48 % → 100 % | 341.9 px | 0.42 | 2.08 | 137 |
| stroke 289 | 73 % → 86 % | 691.0 px | 0.27 | 1.18 | 116 |
| stroke 290 | 42 % → 100 % | 187.7 px | 0.45 | 2.37 | 371 |
| stroke 291 | 92 % → 93 % | 586.1 px | 0.22 | 1.01 | 370 |
| stroke 292 | 89 % → 91 % | 831.6 px | 0.22 | 1.03 | 202 |
| stroke 293 | 67 % → 81 % | 658.3 px | 0.25 | 1.20 | 125 |
| stroke 294 | 77 % → 99 % | 633.0 px | 0.30 | 1.28 | 93 |
| stroke 295 | 28 % → 100 % | 236.5 px | 0.49 | 3.52 | 96 |
| stroke 296 | 83 % → 82 % | 823.1 px | 0.22 | 1.00 | 229 |
| stroke 297 | 87 % → 91 % | 811.5 px | 0.25 | 1.04 | 266 |
| stroke 298 | 92 % → 95 % | 870.0 px | 0.24 | 1.03 | 307 |
| stroke 299 | 84 % → 84 % | 621.6 px | 0.20 | 1.00 | 250 |
| stroke 300 | 74 % → 92 % | 711.7 px | 0.30 | 1.25 | 265 |
| stroke 301 | 47 % → 99 % | 450.6 px | 0.45 | 2.11 | 146 |
| stroke 302 | 66 % → 100 % | 662.1 px | 0.35 | 1.51 | 147 |
| stroke 303 | 17 % → 100 % | 131.0 px | 0.47 | 6.02 | 125 |
| stroke 304 | 16 % → 100 % | 101.6 px | 0.52 | 6.16 | 146 |
| stroke 305 | 20 % → 100 % | 128.0 px | 0.51 | 4.88 | 175 |
| stroke 306 | 23 % → 100 % | 169.8 px | 0.52 | 4.41 | 117 |
| stroke 307 | 29 % → 100 % | 152.5 px | 0.47 | 3.43 | 250 |
| stroke 308 | 38 % → 76 % | 218.4 px | 0.24 | 2.02 | 195 |
| stroke 309 | 41 % → 75 % | 179.0 px | 0.30 | 1.83 | 303 |
| stroke 310 | 49 % → 76 % | 255.1 px | 0.28 | 1.57 | 203 |
| stroke 311 | 55 % → 76 % | 366.4 px | 0.25 | 1.39 | 116 |
| stroke 312 | 68 % → 82 % | 545.2 px | 0.24 | 1.22 | 112 |
| stroke 313 | 38 % → 88 % | 373.9 px | 0.41 | 2.33 | 84 |
| stroke 314 | 56 % → 82 % | 347.9 px | 0.29 | 1.47 | 228 |
| stroke 315 | 58 % → 87 % | 367.8 px | 0.28 | 1.49 | 174 |
| stroke 316 | 67 % → 71 % | 489.7 px | 0.23 | 1.07 | 126 |
| stroke 317 | 60 % → 82 % | 380.3 px | 0.27 | 1.37 | 291 |
| stroke 318 | 70 % → 75 % | 493.1 px | 0.22 | 1.06 | 124 |
| stroke 319 | 62 % → 86 % | 603.7 px | 0.31 | 1.39 | 85 |
| stroke 320 | 52 % → 85 % | 515.2 px | 0.37 | 1.63 | 108 |
| stroke 321 | 55 % → 77 % | 483.3 px | 0.32 | 1.42 | 147 |
| stroke 322 | 17 % → 85 % | 81.6 px | 0.46 | 4.88 | 240 |
| stroke 323 | 30 % → 89 % | 113.9 px | 0.42 | 2.95 | 331 |
| stroke 324 | 28 % → 82 % | 231.5 px | 0.44 | 2.94 | 120 |
| stroke 325 | 46 % → 89 % | 433.9 px | 0.36 | 1.94 | 84 |
| stroke 326 | 29 % → 91 % | 164.5 px | 0.42 | 3.18 | 201 |
| stroke 327 | 52 % → 83 % | 223.9 px | 0.25 | 1.58 | 810 |
| stroke 328 | 27 % → 91 % | 143.1 px | 0.49 | 3.42 | 462 |
| stroke 329 | 59 % → 95 % | 188.0 px | 0.27 | 1.62 | 763 |
| stroke 330 | 33 % → 91 % | 146.2 px | 0.46 | 2.76 | 220 |
| stroke 331 | 56 % → 82 % | 226.9 px | 0.26 | 1.47 | 377 |
| stroke 332 | 61 % → 88 % | 251.2 px | 0.24 | 1.43 | 300 |
| stroke 333 | 69 % → 94 % | 246.5 px | 0.24 | 1.37 | 350 |
| stroke 334 | 35 % → 97 % | 176.9 px | 0.42 | 2.78 | 307 |
| stroke 335 | 56 % → 77 % | 243.8 px | 0.24 | 1.36 | 578 |
| stroke 336 | 50 % → 97 % | 374.4 px | 0.36 | 1.96 | 111 |
| stroke 337 | 65 % → 94 % | 653.7 px | 0.27 | 1.44 | 57 |
| stroke 338 | 63 % → 94 % | 517.5 px | 0.26 | 1.50 | 110 |
| stroke 339 | 69 % → 92 % | 324.0 px | 0.35 | 1.35 | 248 |
| stroke 340 | 43 % → 97 % | 346.4 px | 0.40 | 2.26 | 111 |
| stroke 341 | 72 % → 95 % | 412.0 px | 0.31 | 1.33 | 165 |
| stroke 342 | 65 % → 94 % | 548.6 px | 0.30 | 1.43 | 74 |
| stroke 343 | 60 % → 94 % | 315.1 px | 0.33 | 1.57 | 485 |
| stroke 344 | 74 % → 96 % | 734.9 px | 0.29 | 1.30 | 66 |
| stroke 345 | 64 % → 95 % | 231.0 px | 0.30 | 1.49 | 458 |
| stroke 346 | 80 % → 92 % | 422.5 px | 0.34 | 1.15 | 235 |
| stroke 347 | 78 % → 89 % | 320.1 px | 0.21 | 1.15 | 308 |
| stroke 348 | 77 % → 89 % | 474.2 px | 0.23 | 1.16 | 170 |
| stroke 349 | 38 % → 99 % | 335.7 px | 0.46 | 2.63 | 113 |
| stroke 350 | 69 % → 93 % | 640.2 px | 0.31 | 1.35 | 109 |
| stroke 351 | 73 % → 91 % | 414.6 px | 0.28 | 1.25 | 232 |
| stroke 352 | 78 % → 94 % | 528.6 px | 0.34 | 1.22 | 157 |
| stroke 353 | 76 % → 94 % | 365.9 px | 0.26 | 1.24 | 299 |
| stroke 354 | 75 % → 96 % | 577.5 px | 0.30 | 1.28 | 111 |
| stroke 355 | 76 % → 80 % | 618.2 px | 0.20 | 1.05 | 128 |
| stroke 356 | 73 % → 96 % | 653.8 px | 0.33 | 1.30 | 112 |
| stroke 357 | 78 % → 88 % | 446.8 px | 0.26 | 1.14 | 217 |
| stroke 358 | 69 % → 89 % | 655.9 px | 0.41 | 1.30 | 101 |
| stroke 359 | 78 % → 84 % | 656.3 px | 0.25 | 1.08 | 154 |
| stroke 360 | 85 % → 90 % | 641.1 px | 0.25 | 1.06 | 144 |
| stroke 361 | 54 % → 90 % | 413.8 px | 0.45 | 1.67 | 86 |
| stroke 362 | 71 % → 97 % | 710.4 px | 0.35 | 1.37 | 83 |
| stroke 363 | 85 % → 89 % | 234.2 px | 0.09 | 1.04 | 69 |
| stroke 364 | 34 % → 67 % | 129.3 px | 0.35 | 1.95 | 32 |
| stroke 365 | 55 % → 79 % | 528.8 px | 0.25 | 1.42 | 47 |
| stroke 366 | 64 % → 69 % | 282.6 px | 0.16 | 1.09 | 136 |
| stroke 367 | 73 % → 76 % | 600.8 px | 0.16 | 1.04 | 35 |
| stroke 368 | 58 % → 63 % | 478.4 px | 0.16 | 1.08 | 59 |
| stroke 369 | 87 % → 87 % | 552.3 px | 0.09 | 0.99 | 107 |
| stroke 370 | 68 % → 71 % | 700.5 px | 0.12 | 1.04 | 67 |
| stroke 371 | 86 % → 91 % | 621.0 px | 0.14 | 1.05 | 58 |
| stroke 372 | 58 % → 100 % | 386.9 px | 0.36 | 1.72 | 53 |
| stroke 373 | 33 % → 99 % | 201.7 px | 0.48 | 3.03 | 70 |
| stroke 374 | 27 % → 94 % | 248.0 px | 0.45 | 3.50 | 24 |
| stroke 375 | 64 % → 90 % | 364.6 px | 0.33 | 1.39 | 95 |
| stroke 376 | 39 % → 84 % | 404.8 px | 0.41 | 2.15 | 29 |
| stroke 377 | 73 % → 77 % | 201.2 px | 0.23 | 1.05 | 1497 |
| stroke 378 | 62 % → 62 % | 219.1 px | 0.31 | 0.99 | 454 |
| stroke 379 | 67 % → 96 % | 198.7 px | 0.32 | 1.42 | 1228 |
| stroke 380 | 61 % → 97 % | 178.9 px | 0.40 | 1.59 | 1720 |
| stroke 381 | 72 % → 96 % | 197.2 px | 0.42 | 1.33 | 1613 |
| stroke 382 | 63 % → 99 % | 183.2 px | 0.45 | 1.57 | 1804 |
| stroke 383 | 71 % → 94 % | 170.0 px | 0.39 | 1.34 | 1387 |
| stroke 384 | 76 % → 98 % | 215.6 px | 0.50 | 1.30 | 1244 |
| stroke 385 | 56 % → 88 % | 191.1 px | 0.50 | 1.57 | 758 |
| stroke 386 | 86 % → 95 % | 355.9 px | 0.37 | 1.11 | 940 |
| stroke 387 | 92 % → 96 % | 265.8 px | 0.37 | 1.05 | 1231 |
| stroke 388 | 89 % → 96 % | 278.4 px | 0.35 | 1.08 | 2230 |
| stroke 389 | 82 % → 99 % | 248.9 px | 0.43 | 1.20 | 1673 |
| stroke 390 | 82 % → 98 % | 264.3 px | 0.32 | 1.20 | 956 |
| stroke 391 | 64 % → 87 % | 203.2 px | 0.38 | 1.37 | 1011 |
| stroke 392 | 72 % → 88 % | 220.8 px | 0.51 | 1.23 | 748 |
| stroke 393 | 85 % → 95 % | 382.1 px | 0.39 | 1.12 | 890 |
| stroke 394 | 82 % → 89 % | 339.0 px | 0.34 | 1.09 | 1084 |
| stroke 395 | 95 % → 100 % | 329.4 px | 0.53 | 1.05 | 910 |
| stroke 396 | 94 % → 96 % | 452.7 px | 0.41 | 1.02 | 501 |
| stroke 397 | 95 % → 100 % | 524.4 px | 0.38 | 1.05 | 277 |
| stroke 398 | 94 % → 99 % | 460.4 px | 0.41 | 1.05 | 601 |
| stroke 399 | 80 % → 88 % | 249.8 px | 0.46 | 1.10 | 722 |
| stroke 400 | 95 % → 97 % | 324.0 px | 0.33 | 1.02 | 1025 |
| stroke 401 | 97 % → 97 % | 550.2 px | 0.29 | 1.00 | 363 |
| stroke 402 | 96 % → 97 % | 376.4 px | 0.43 | 1.01 | 1226 |
| stroke 403 | 99 % → 100 % | 438.5 px | 0.41 | 1.01 | 558 |
| stroke 404 | 100 % → 100 % | 454.5 px | 0.51 | 1.00 | 553 |
| stroke 405 | 99 % → 100 % | 538.8 px | 0.54 | 1.01 | 396 |
| stroke 406 | 77 % → 80 % | 349.3 px | 0.40 | 1.04 | 582 |
| stroke 407 | 89 % → 89 % | 448.6 px | 0.38 | 1.00 | 744 |
| stroke 408 | 97 % → 97 % | 471.3 px | 0.49 | 1.00 | 456 |
| stroke 409 | 92 % → 93 % | 497.9 px | 0.43 | 1.01 | 511 |
| stroke 410 | 100 % → 100 % | 479.6 px | 0.45 | 1.00 | 576 |
| stroke 411 | 90 % → 99 % | 461.2 px | 0.49 | 1.10 | 523 |
| stroke 412 | 81 % → 92 % | 319.4 px | 0.44 | 1.13 | 1158 |
| stroke 413 | 87 % → 89 % | 333.2 px | 0.48 | 1.03 | 666 |
| stroke 414 | 100 % → 100 % | 439.8 px | 0.51 | 1.00 | 648 |
| stroke 415 | 83 % → 83 % | 371.3 px | 0.45 | 1.00 | 714 |
| stroke 416 | 93 % → 97 % | 518.6 px | 0.46 | 1.04 | 486 |
| stroke 417 | 99 % → 99 % | 553.8 px | 0.43 | 1.00 | 485 |
| stroke 418 | 100 % → 100 % | 621.5 px | 0.53 | 1.00 | 437 |
| stroke 419 | 99 % → 100 % | 494.1 px | 0.44 | 1.00 | 738 |
| stroke 420 | 99 % → 99 % | 542.7 px | 0.52 | 1.00 | 420 |
| stroke 421 | 83 % → 89 % | 260.2 px | 0.38 | 1.07 | 2074 |
| stroke 422 | 86 % → 92 % | 525.2 px | 0.37 | 1.07 | 403 |
| stroke 423 | 86 % → 88 % | 379.7 px | 0.40 | 1.02 | 750 |
| stroke 424 | 92 % → 92 % | 585.6 px | 0.27 | 1.00 | 516 |
| stroke 425 | 83 % → 83 % | 440.9 px | 0.41 | 0.99 | 452 |
| stroke 426 | 73 % → 74 % | 290.5 px | 0.11 | 1.01 | 188 |
| stroke 427 | 88 % → 87 % | 256.3 px | 0.16 | 0.99 | 246 |
| stroke 428 | 62 % → 64 % | 641.5 px | 0.15 | 1.03 | 47 |
| stroke 429 | 72 % → 73 % | 449.0 px | 0.15 | 1.01 | 210 |
| stroke 430 | 60 % → 60 % | 410.6 px | 0.15 | 1.00 | 122 |
| stroke 431 | 85 % → 85 % | 248.8 px | 0.25 | 1.00 | 561 |

Numbers say: wet paint spreads well beyond the stroke.

## Refs v3 · #13 HW blue streaky form — own sheet
own sheet 800 × 1020 · Gouache 1.00 + turpentine 30 % · 104 px · 1949.9 s

![Refs v3 · #13 HW blue streaky form — own sheet](Refs-v3-13-HW-blue-streaky-form-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 8 % → 95 % | 94.7 px | 0.19 | 11.21 | 2912 |
| stroke 2 | 13 % → 86 % | 93.4 px | 0.21 | 6.51 | 3207 |
| stroke 3 | 18 % → 96 % | 191.6 px | 0.22 | 5.22 | 3918 |
| stroke 4 | 29 % → 91 % | 264.7 px | 0.14 | 3.11 | 6551 |
| stroke 5 | 31 % → 94 % | 312.6 px | 0.28 | 3.05 | 2667 |
| stroke 6 | 49 % → 93 % | 466.4 px | 0.23 | 1.89 | 4401 |
| stroke 7 | 56 % → 95 % | 816.1 px | 0.22 | 1.70 | 2363 |
| stroke 8 | 43 % → 94 % | 472.0 px | 0.14 | 2.17 | 3999 |
| stroke 9 | 47 % → 91 % | 1042.4 px | 0.15 | 1.92 | 1514 |
| stroke 10 | 52 % → 97 % | 914.6 px | 0.18 | 1.89 | 1974 |
| stroke 11 | 36 % → 91 % | 483.3 px | 0.13 | 2.51 | 2215 |
| stroke 12 | 35 % → 96 % | 713.0 px | 0.22 | 2.77 | 1001 |
| stroke 13 | 46 % → 98 % | 707.0 px | 0.28 | 2.16 | 1929 |
| stroke 14 | 43 % → 91 % | 876.7 px | 0.13 | 2.11 | 1567 |
| stroke 15 | 79 % → 97 % | 1478.0 px | 0.19 | 1.23 | 2363 |
| stroke 16 | 48 % → 92 % | 707.4 px | 0.14 | 1.92 | 4154 |
| stroke 17 | 69 % → 97 % | 968.1 px | 0.16 | 1.40 | 3905 |
| stroke 18 | 50 % → 92 % | 1035.8 px | 0.16 | 1.85 | 1786 |
| stroke 19 | 66 % → 88 % | 862.3 px | 0.18 | 1.34 | 3441 |
| stroke 20 | 39 % → 86 % | 434.4 px | 0.12 | 2.21 | 3999 |
| stroke 21 | 60 % → 98 % | 973.6 px | 0.27 | 1.63 | 2490 |
| stroke 22 | 71 % → 91 % | 930.6 px | 0.21 | 1.28 | 3854 |
| stroke 23 | 48 % → 89 % | 960.6 px | 0.12 | 1.85 | 1558 |
| stroke 24 | 75 % → 94 % | 1622.6 px | 0.15 | 1.25 | 2105 |
| stroke 25 | 57 % → 88 % | 837.0 px | 0.14 | 1.54 | 1942 |
| stroke 26 | 71 % → 93 % | 1158.9 px | 0.14 | 1.31 | 2597 |
| stroke 27 | 68 % → 87 % | 1073.5 px | 0.23 | 1.27 | 1438 |
| stroke 28 | 66 % → 93 % | 1536.4 px | 0.15 | 1.41 | 1550 |
| stroke 29 | 62 % → 92 % | 1201.3 px | 0.23 | 1.49 | 1419 |
| stroke 30 | 42 % → 84 % | 596.3 px | 0.11 | 2.00 | 1781 |
| stroke 31 | 41 % → 82 % | 740.7 px | 0.11 | 2.00 | 1232 |
| stroke 32 | 32 % → 93 % | 472.0 px | 0.19 | 2.95 | 209 |
| stroke 33 | 49 % → 89 % | 1397.7 px | 0.13 | 1.83 | 74 |
| stroke 34 | 34 % → 81 % | 1461.0 px | 0.10 | 2.41 | 24 |
| stroke 35 | 43 % → 87 % | 730.4 px | 0.11 | 2.01 | 199 |
| stroke 36 | 59 % → 90 % | 753.6 px | 0.12 | 1.53 | 470 |
| stroke 37 | 66 % → 91 % | 1336.6 px | 0.13 | 1.36 | 407 |
| stroke 38 | 46 % → 93 % | 556.8 px | 0.19 | 2.03 | 480 |
| stroke 39 | 55 % → 89 % | 856.4 px | 0.14 | 1.63 | 323 |
| stroke 40 | 66 % → 90 % | 1392.2 px | 0.13 | 1.36 | 366 |
| stroke 41 | 54 % → 90 % | 722.9 px | 0.14 | 1.68 | 316 |
| stroke 42 | 38 % → 96 % | 941.9 px | 0.25 | 2.53 | 193 |
| stroke 43 | 65 % → 89 % | 1104.0 px | 0.11 | 1.37 | 309 |
| stroke 44 | 67 % → 89 % | 1268.6 px | 0.13 | 1.33 | 462 |
| stroke 45 | 34 % → 95 % | 1112.5 px | 0.26 | 2.79 | 124 |
| stroke 46 | 77 % → 94 % | 1755.6 px | 0.14 | 1.23 | 441 |
| stroke 47 | 76 % → 93 % | 2055.2 px | 0.14 | 1.23 | 397 |
| stroke 48 | 69 % → 92 % | 3160.7 px | 0.13 | 1.33 | 186 |
| stroke 49 | 41 % → 96 % | 1108.6 px | 0.26 | 2.34 | 217 |
| stroke 50 | 54 % → 92 % | 1540.2 px | 0.17 | 1.70 | 168 |
| stroke 51 | 57 % → 88 % | 2036.5 px | 0.12 | 1.54 | 190 |
| stroke 52 | 44 % → 95 % | 1495.8 px | 0.22 | 2.17 | 161 |
| stroke 53 | 66 % → 89 % | 1071.6 px | 0.12 | 1.35 | 437 |
| stroke 54 | 72 % → 91 % | 2960.9 px | 0.13 | 1.26 | 182 |
| stroke 55 | 77 % → 92 % | 3146.4 px | 0.14 | 1.20 | 203 |
| stroke 56 | 62 % → 89 % | 2837.1 px | 0.12 | 1.43 | 256 |
| stroke 57 | 55 % → 86 % | 2097.4 px | 0.11 | 1.56 | 97 |
| stroke 58 | 60 % → 87 % | 2084.1 px | 0.11 | 1.45 | 137 |
| stroke 59 | 55 % → 99 % | 2277.0 px | 0.23 | 1.78 | 158 |
| stroke 60 | 60 % → 98 % | 2412.4 px | 0.21 | 1.63 | 175 |
| stroke 61 | 74 % → 97 % | 2653.6 px | 0.23 | 1.30 | 223 |
| stroke 62 | 69 % → 96 % | 2660.7 px | 0.24 | 1.41 | 242 |
| stroke 63 | 67 % → 97 % | 3826.4 px | 0.24 | 1.46 | 137 |
| stroke 64 | 37 % → 83 % | 1032.4 px | 0.11 | 2.28 | 116 |
| stroke 65 | 48 % → 83 % | 583.0 px | 0.10 | 1.71 | 452 |
| stroke 66 | 54 % → 82 % | 1637.7 px | 0.11 | 1.53 | 144 |
| stroke 67 | 22 % → 81 % | 454.6 px | 0.09 | 3.63 | 145 |
| stroke 68 | 57 % → 85 % | 800.5 px | 0.12 | 1.48 | 623 |
| stroke 69 | 65 % → 88 % | 1683.5 px | 0.12 | 1.34 | 350 |
| stroke 70 | 67 % → 87 % | 2119.6 px | 0.14 | 1.31 | 233 |
| stroke 71 | 46 % → 81 % | 525.7 px | 0.10 | 1.77 | 474 |
| stroke 72 | 41 % → 80 % | 401.9 px | 0.09 | 1.95 | 565 |
| stroke 73 | 52 % → 83 % | 1482.8 px | 0.10 | 1.61 | 154 |
| stroke 74 | 65 % → 88 % | 1655.5 px | 0.13 | 1.36 | 346 |
| stroke 75 | 50 % → 82 % | 757.8 px | 0.11 | 1.63 | 385 |
| stroke 76 | 38 % → 82 % | 580.5 px | 0.09 | 2.16 | 243 |
| stroke 77 | 48 % → 82 % | 548.9 px | 0.10 | 1.70 | 421 |
| stroke 78 | 68 % → 86 % | 1184.6 px | 0.12 | 1.26 | 471 |
| stroke 79 | 69 % → 87 % | 1301.6 px | 0.13 | 1.27 | 403 |
| stroke 80 | 65 % → 84 % | 1189.2 px | 0.12 | 1.28 | 463 |
| stroke 81 | 59 % → 81 % | 581.1 px | 0.10 | 1.37 | 835 |
| stroke 82 | 55 % → 82 % | 593.9 px | 0.10 | 1.47 | 516 |
| stroke 83 | 70 % → 81 % | 1478.8 px | 0.10 | 1.15 | 269 |
| stroke 84 | 67 % → 84 % | 2029.0 px | 0.12 | 1.25 | 267 |
| stroke 85 | 77 % → 86 % | 3506.2 px | 0.12 | 1.11 | 192 |
| stroke 86 | 75 % → 89 % | 2025.1 px | 0.12 | 1.18 | 300 |
| stroke 87 | 75 % → 84 % | 1239.5 px | 0.11 | 1.11 | 469 |
| stroke 88 | 84 % → 89 % | 2648.6 px | 0.13 | 1.06 | 313 |
| stroke 89 | 75 % → 84 % | 3405.3 px | 0.11 | 1.13 | 168 |
| stroke 90 | 57 % → 81 % | 1276.3 px | 0.10 | 1.42 | 171 |
| stroke 91 | 73 % → 82 % | 1380.2 px | 0.10 | 1.13 | 616 |
| stroke 92 | 59 % → 82 % | 729.4 px | 0.10 | 1.40 | 818 |
| stroke 93 | 78 % → 85 % | 1682.8 px | 0.12 | 1.08 | 699 |
| stroke 94 | 71 % → 82 % | 1303.8 px | 0.11 | 1.16 | 678 |
| stroke 95 | 62 % → 85 % | 2260.6 px | 0.10 | 1.38 | 205 |
| stroke 96 | 84 % → 93 % | 2200.8 px | 0.14 | 1.10 | 809 |
| stroke 97 | 94 % → 95 % | 4327.8 px | 0.16 | 1.02 | 238 |
| stroke 98 | 65 % → 80 % | 875.6 px | 0.10 | 1.23 | 601 |
| stroke 99 | 81 % → 83 % | 3159.2 px | 0.11 | 1.03 | 255 |
| stroke 100 | 53 % → 82 % | 1344.5 px | 0.09 | 1.55 | 194 |
| stroke 101 | 60 % → 82 % | 901.3 px | 0.10 | 1.38 | 492 |
| stroke 102 | 60 % → 83 % | 2308.7 px | 0.10 | 1.39 | 158 |
| stroke 103 | 71 % → 86 % | 3306.2 px | 0.13 | 1.22 | 169 |
| stroke 104 | 65 % → 86 % | 3026.8 px | 0.11 | 1.31 | 247 |
| stroke 105 | 64 % → 83 % | 2523.1 px | 0.11 | 1.31 | 127 |
| stroke 106 | 67 % → 85 % | 1278.4 px | 0.13 | 1.26 | 262 |
| stroke 107 | 70 % → 85 % | 1196.9 px | 0.12 | 1.22 | 393 |
| stroke 108 | 77 % → 86 % | 1520.4 px | 0.14 | 1.11 | 371 |
| stroke 109 | 68 % → 85 % | 1708.9 px | 0.12 | 1.25 | 230 |
| stroke 110 | 54 % → 95 % | 1486.0 px | 0.22 | 1.76 | 169 |
| stroke 111 | 63 % → 89 % | 2148.7 px | 0.24 | 1.40 | 116 |
| stroke 112 | 78 % → 98 % | 2897.7 px | 0.23 | 1.25 | 124 |
| stroke 113 | 76 % → 88 % | 3252.2 px | 0.21 | 1.15 | 86 |
| stroke 114 | 85 % → 86 % | 1607.7 px | 0.18 | 1.02 | 148 |
| stroke 115 | 81 % → 91 % | 5299.9 px | 0.13 | 1.11 | 45 |
| stroke 116 | 84 % → 86 % | 2252.3 px | 0.15 | 1.02 | 161 |
| stroke 117 | 70 % → 83 % | 2236.2 px | 0.14 | 1.18 | 39 |
| stroke 118 | 73 % → 84 % | 3493.5 px | 0.14 | 1.16 | 34 |
| stroke 119 | 47 % → 93 % | 236.3 px | 0.22 | 1.96 | 1626 |
| stroke 120 | 43 % → 95 % | 761.0 px | 0.30 | 2.18 | 673 |
| stroke 121 | 45 % → 95 % | 285.0 px | 0.32 | 2.11 | 1553 |
| stroke 122 | 41 % → 95 % | 518.6 px | 0.33 | 2.33 | 387 |
| stroke 123 | 47 % → 95 % | 411.1 px | 0.33 | 2.04 | 967 |
| stroke 124 | 58 % → 94 % | 677.9 px | 0.28 | 1.63 | 922 |
| stroke 125 | 56 % → 94 % | 1597.6 px | 0.29 | 1.70 | 358 |
| stroke 126 | 58 % → 94 % | 697.9 px | 0.27 | 1.61 | 734 |
| stroke 127 | 61 % → 94 % | 423.0 px | 0.25 | 1.53 | 1193 |
| stroke 128 | 71 % → 94 % | 1583.5 px | 0.19 | 1.33 | 441 |
| stroke 129 | 42 % → 90 % | 419.1 px | 0.33 | 2.13 | 1066 |
| stroke 130 | 41 % → 89 % | 734.2 px | 0.34 | 2.16 | 514 |
| stroke 131 | 32 % → 89 % | 400.2 px | 0.39 | 2.78 | 461 |
| stroke 132 | 50 % → 88 % | 388.9 px | 0.32 | 1.75 | 1200 |
| stroke 133 | 35 % → 97 % | 546.7 px | 0.39 | 2.74 | 775 |
| stroke 134 | 48 % → 97 % | 961.9 px | 0.35 | 2.04 | 757 |
| stroke 135 | 50 % → 99 % | 1366.0 px | 0.35 | 1.98 | 655 |
| stroke 136 | 52 % → 99 % | 1495.8 px | 0.34 | 1.91 | 503 |
| stroke 137 | 49 % → 97 % | 865.3 px | 0.35 | 1.97 | 788 |
| stroke 138 | 38 % → 97 % | 761.1 px | 0.40 | 2.56 | 593 |
| stroke 139 | 50 % → 97 % | 1148.8 px | 0.36 | 1.95 | 689 |
| stroke 140 | 39 % → 97 % | 1281.8 px | 0.40 | 2.50 | 436 |
| stroke 141 | 69 % → 95 % | 1470.7 px | 0.23 | 1.37 | 844 |
| stroke 142 | 77 % → 92 % | 858.9 px | 0.16 | 1.20 | 2614 |
| stroke 143 | 77 % → 93 % | 1071.1 px | 0.18 | 1.21 | 1615 |
| stroke 144 | 79 % → 91 % | 821.0 px | 0.14 | 1.15 | 4423 |
| stroke 145 | 83 % → 90 % | 1233.2 px | 0.13 | 1.09 | 2610 |
| stroke 146 | 80 % → 92 % | 1312.0 px | 0.18 | 1.16 | 1702 |
| stroke 147 | 73 % → 95 % | 2144.9 px | 0.23 | 1.30 | 738 |
| stroke 148 | 85 % → 90 % | 2295.2 px | 0.12 | 1.06 | 456 |
| stroke 149 | 81 % → 92 % | 2106.3 px | 0.17 | 1.15 | 399 |
| stroke 150 | 61 % → 81 % | 547.7 px | 0.10 | 1.33 | 843 |
| stroke 151 | 74 % → 85 % | 546.6 px | 0.10 | 1.15 | 2983 |
| stroke 152 | 70 % → 82 % | 902.4 px | 0.09 | 1.18 | 1593 |
| stroke 153 | 70 % → 80 % | 554.4 px | 0.09 | 1.14 | 1735 |
| stroke 154 | 78 % → 85 % | 1224.7 px | 0.10 | 1.08 | 1007 |
| stroke 155 | 75 % → 82 % | 738.8 px | 0.09 | 1.09 | 1435 |
| stroke 156 | 78 % → 84 % | 1330.1 px | 0.09 | 1.08 | 429 |
| stroke 157 | 79 % → 84 % | 1721.3 px | 0.10 | 1.05 | 490 |
| stroke 158 | 77 % → 80 % | 522.5 px | 0.10 | 1.05 | 847 |
| stroke 159 | 83 % → 83 % | 2624.4 px | 0.11 | 1.00 | 671 |
| stroke 160 | 83 % → 83 % | 2162.9 px | 0.11 | 1.00 | 571 |
| stroke 161 | 85 % → 84 % | 1717.9 px | 0.11 | 0.99 | 1027 |
| stroke 162 | 84 % → 83 % | 2248.0 px | 0.10 | 0.99 | 485 |
| stroke 163 | 53 % → 81 % | 857.6 px | 0.10 | 1.51 | 314 |
| stroke 164 | 65 % → 82 % | 551.0 px | 0.09 | 1.26 | 761 |
| stroke 165 | 80 % → 84 % | 802.8 px | 0.11 | 1.04 | 1289 |
| stroke 166 | 79 % → 83 % | 864.3 px | 0.10 | 1.05 | 1068 |
| stroke 167 | 82 % → 84 % | 1184.1 px | 0.11 | 1.02 | 806 |
| stroke 168 | 81 % → 83 % | 1130.5 px | 0.10 | 1.03 | 629 |
| stroke 169 | 84 % → 84 % | 1600.2 px | 0.11 | 1.00 | 584 |
| stroke 170 | 81 % → 82 % | 1024.3 px | 0.10 | 1.01 | 667 |
| stroke 171 | 81 % → 82 % | 1114.2 px | 0.08 | 1.00 | 572 |
| stroke 172 | 85 % → 84 % | 1773.1 px | 0.10 | 0.99 | 670 |
| stroke 173 | 84 % → 83 % | 1798.7 px | 0.10 | 0.99 | 433 |
| stroke 174 | 40 % → 90 % | 618.1 px | 0.37 | 2.25 | 247 |
| stroke 175 | 30 % → 94 % | 501.3 px | 0.43 | 3.16 | 235 |
| stroke 176 | 42 % → 91 % | 497.3 px | 0.38 | 2.13 | 474 |
| stroke 177 | 38 % → 93 % | 373.2 px | 0.42 | 2.44 | 581 |
| stroke 178 | 52 % → 91 % | 710.7 px | 0.36 | 1.75 | 1077 |
| stroke 179 | 50 % → 92 % | 839.0 px | 0.38 | 1.83 | 281 |
| stroke 180 | 46 % → 92 % | 531.1 px | 0.42 | 2.02 | 300 |
| stroke 181 | 45 % → 94 % | 660.2 px | 0.41 | 2.08 | 405 |
| stroke 182 | 46 % → 96 % | 1611.4 px | 0.42 | 2.09 | 122 |
| stroke 183 | 58 % → 90 % | 657.9 px | 0.38 | 1.54 | 418 |
| stroke 184 | 50 % → 93 % | 697.2 px | 0.42 | 1.86 | 353 |
| stroke 185 | 54 % → 92 % | 658.5 px | 0.38 | 1.71 | 979 |
| stroke 186 | 58 % → 92 % | 983.5 px | 0.42 | 1.58 | 152 |
| stroke 187 | 57 % → 93 % | 998.9 px | 0.42 | 1.63 | 146 |
| stroke 188 | 56 % → 92 % | 1118.6 px | 0.42 | 1.63 | 155 |
| stroke 189 | 55 % → 92 % | 602.2 px | 0.42 | 1.68 | 362 |
| stroke 190 | 58 % → 92 % | 1517.3 px | 0.41 | 1.60 | 133 |
| stroke 191 | 60 % → 93 % | 902.7 px | 0.43 | 1.54 | 190 |
| stroke 192 | 61 % → 90 % | 2063.2 px | 0.39 | 1.48 | 110 |
| stroke 193 | 49 % → 96 % | 2285.8 px | 0.42 | 1.97 | 101 |
| stroke 194 | 60 % → 92 % | 2192.5 px | 0.38 | 1.53 | 98 |
| stroke 195 | 59 % → 93 % | 1668.0 px | 0.42 | 1.58 | 119 |
| stroke 196 | 32 % → 96 % | 484.3 px | 0.50 | 3.01 | 237 |
| stroke 197 | 41 % → 95 % | 363.6 px | 0.48 | 2.34 | 449 |
| stroke 198 | 47 % → 96 % | 836.2 px | 0.42 | 2.03 | 240 |
| stroke 199 | 39 % → 96 % | 523.9 px | 0.50 | 2.46 | 291 |
| stroke 200 | 46 % → 95 % | 939.8 px | 0.43 | 2.10 | 274 |
| stroke 201 | 45 % → 96 % | 1625.9 px | 0.49 | 2.14 | 86 |
| stroke 202 | 44 % → 96 % | 1700.9 px | 0.49 | 2.16 | 75 |
| stroke 203 | 42 % → 95 % | 1246.7 px | 0.47 | 2.24 | 134 |
| stroke 204 | 44 % → 96 % | 1924.1 px | 0.45 | 2.17 | 103 |
| stroke 205 | 49 % → 95 % | 1078.2 px | 0.39 | 1.93 | 162 |
| stroke 206 | 56 % → 95 % | 1502.9 px | 0.36 | 1.71 | 153 |
| stroke 207 | 58 % → 95 % | 1094.9 px | 0.35 | 1.65 | 245 |
| stroke 208 | 53 % → 95 % | 2012.7 px | 0.38 | 1.79 | 115 |
| stroke 209 | 55 % → 95 % | 1336.4 px | 0.37 | 1.75 | 201 |
| stroke 210 | 54 % → 95 % | 1390.9 px | 0.40 | 1.76 | 116 |
| stroke 211 | 74 % → 97 % | 3342.1 px | 0.27 | 1.31 | 71 |
| stroke 212 | 73 % → 96 % | 1505.4 px | 0.30 | 1.31 | 301 |
| stroke 213 | 72 % → 95 % | 1695.8 px | 0.30 | 1.31 | 435 |
| stroke 214 | 74 % → 98 % | 3402.7 px | 0.32 | 1.34 | 203 |
| stroke 215 | 79 % → 99 % | 3898.7 px | 0.28 | 1.25 | 92 |
| stroke 216 | 79 % → 98 % | 2566.1 px | 0.28 | 1.24 | 233 |
| stroke 217 | 77 % → 99 % | 3477.7 px | 0.30 | 1.28 | 225 |
| stroke 218 | 73 % → 96 % | 3635.6 px | 0.31 | 1.32 | 155 |
| stroke 219 | 77 % → 98 % | 3885.7 px | 0.30 | 1.28 | 116 |
| stroke 220 | 74 % → 92 % | 1240.4 px | 0.32 | 1.24 | 379 |
| stroke 221 | 77 % → 94 % | 1579.7 px | 0.31 | 1.21 | 357 |
| stroke 222 | 77 % → 92 % | 1932.0 px | 0.32 | 1.19 | 188 |
| stroke 223 | 78 % → 93 % | 1912.7 px | 0.32 | 1.20 | 281 |
| stroke 224 | 77 % → 92 % | 3860.7 px | 0.33 | 1.21 | 145 |
| stroke 225 | 80 % → 94 % | 1745.1 px | 0.30 | 1.17 | 285 |
| stroke 226 | 79 % → 92 % | 2609.4 px | 0.32 | 1.17 | 176 |
| stroke 227 | 62 % → 95 % | 929.9 px | 0.39 | 1.55 | 98 |
| stroke 228 | 65 % → 95 % | 1152.6 px | 0.36 | 1.47 | 192 |
| stroke 229 | 67 % → 96 % | 1817.1 px | 0.40 | 1.43 | 114 |
| stroke 230 | 84 % → 99 % | 3980.5 px | 0.25 | 1.18 | 92 |
| stroke 231 | 78 % → 99 % | 2012.8 px | 0.33 | 1.26 | 551 |
| stroke 232 | 70 % → 94 % | 585.0 px | 0.39 | 1.35 | 952 |
| stroke 233 | 79 % → 98 % | 2121.1 px | 0.33 | 1.24 | 533 |
| stroke 234 | 80 % → 95 % | 890.3 px | 0.33 | 1.19 | 1004 |
| stroke 235 | 78 % → 96 % | 1063.4 px | 0.39 | 1.23 | 897 |
| stroke 236 | 86 % → 95 % | 1087.6 px | 0.30 | 1.10 | 717 |
| stroke 237 | 81 % → 96 % | 1140.4 px | 0.38 | 1.18 | 990 |
| stroke 238 | 78 % → 95 % | 1167.5 px | 0.47 | 1.22 | 301 |
| stroke 239 | 91 % → 97 % | 1776.6 px | 0.26 | 1.06 | 672 |
| stroke 240 | 87 % → 95 % | 1074.5 px | 0.37 | 1.09 | 949 |
| stroke 241 | 90 % → 95 % | 1914.9 px | 0.30 | 1.06 | 501 |
| stroke 242 | 81 % → 96 % | 1321.2 px | 0.43 | 1.19 | 625 |
| stroke 243 | 80 % → 96 % | 1490.4 px | 0.46 | 1.19 | 417 |
| stroke 244 | 87 % → 96 % | 1152.2 px | 0.43 | 1.10 | 680 |
| stroke 245 | 92 % → 97 % | 1321.6 px | 0.28 | 1.05 | 1321 |
| stroke 246 | 90 % → 95 % | 1085.4 px | 0.39 | 1.06 | 497 |
| stroke 247 | 92 % → 95 % | 2019.9 px | 0.33 | 1.04 | 418 |
| stroke 248 | 92 % → 95 % | 3048.5 px | 0.34 | 1.04 | 233 |
| stroke 249 | 95 % → 96 % | 1475.2 px | 0.34 | 1.01 | 476 |
| stroke 250 | 91 % → 96 % | 2032.5 px | 0.45 | 1.05 | 342 |
| stroke 251 | 89 % → 96 % | 1890.9 px | 0.43 | 1.08 | 449 |
| stroke 252 | 93 % → 96 % | 1520.2 px | 0.36 | 1.03 | 424 |
| stroke 253 | 94 % → 97 % | 4342.1 px | 0.36 | 1.03 | 235 |
| stroke 254 | 90 % → 96 % | 2020.7 px | 0.43 | 1.06 | 401 |
| stroke 255 | 96 % → 99 % | 2733.3 px | 0.27 | 1.03 | 515 |
| stroke 256 | 84 % → 96 % | 2207.3 px | 0.46 | 1.15 | 333 |
| stroke 257 | 94 % → 96 % | 1816.4 px | 0.36 | 1.02 | 565 |
| stroke 258 | 95 % → 95 % | 3946.0 px | 0.31 | 1.00 | 591 |
| stroke 259 | 96 % → 97 % | 2235.5 px | 0.36 | 1.00 | 387 |
| stroke 260 | 95 % → 95 % | 2133.4 px | 0.38 | 1.00 | 312 |
| stroke 261 | 96 % → 96 % | 2323.3 px | 0.37 | 1.00 | 421 |
| stroke 262 | 96 % → 95 % | 2539.3 px | 0.37 | 1.00 | 265 |
| stroke 263 | 94 % → 96 % | 4284.2 px | 0.34 | 1.02 | 223 |
| stroke 264 | 86 % → 91 % | 897.5 px | 0.31 | 1.06 | 1910 |
| stroke 265 | 85 % → 91 % | 863.0 px | 0.35 | 1.06 | 1019 |
| stroke 266 | 92 % → 94 % | 969.0 px | 0.32 | 1.02 | 1366 |
| stroke 267 | 89 % → 91 % | 1332.0 px | 0.36 | 1.02 | 549 |
| stroke 268 | 89 % → 90 % | 674.2 px | 0.35 | 1.01 | 1228 |
| stroke 269 | 90 % → 91 % | 2038.0 px | 0.36 | 1.01 | 458 |
| stroke 270 | 97 % → 97 % | 1750.7 px | 0.35 | 1.00 | 595 |
| stroke 271 | 95 % → 94 % | 1504.9 px | 0.29 | 1.00 | 889 |
| stroke 272 | 90 % → 90 % | 2159.5 px | 0.35 | 1.00 | 296 |
| stroke 273 | 90 % → 90 % | 1878.5 px | 0.33 | 0.99 | 417 |
| stroke 274 | 92 % → 92 % | 2046.4 px | 0.39 | 1.00 | 396 |
| stroke 275 | 93 % → 93 % | 1729.5 px | 0.42 | 1.00 | 274 |
| stroke 276 | 97 % → 96 % | 3177.9 px | 0.35 | 1.00 | 386 |
| stroke 277 | 90 % → 90 % | 2845.5 px | 0.36 | 1.00 | 296 |
| stroke 278 | 90 % → 90 % | 2834.3 px | 0.36 | 1.00 | 239 |
| stroke 279 | 94 % → 94 % | 2197.5 px | 0.38 | 1.00 | 432 |
| stroke 280 | 98 % → 98 % | 4536.1 px | 0.32 | 1.00 | 298 |
| stroke 281 | 93 % → 92 % | 3277.9 px | 0.30 | 0.99 | 206 |

Numbers say: wet paint spreads well beyond the stroke.

## Refs v3 · #14 HW olive totem — own sheet
own sheet 800 × 1040 · Gouache 1.00 + turpentine 30 % · 57 px · 1257.7 s

![Refs v3 · #14 HW olive totem — own sheet](Refs-v3-14-HW-olive-totem-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 7 % → 87 % | 56.9 px | 0.20 | 13.37 | 363 |
| stroke 2 | 10 % → 87 % | 125.3 px | 0.20 | 8.39 | 225 |
| stroke 3 | 6 % → 76 % | 55.5 px | 0.23 | 11.86 | 392 |
| stroke 4 | 10 % → 71 % | 85.1 px | 0.23 | 7.26 | 514 |
| stroke 5 | 16 % → 62 % | 98.4 px | 0.24 | 3.87 | 557 |
| stroke 6 | 20 % → 78 % | 165.5 px | 0.24 | 3.82 | 437 |
| stroke 7 | 7 % → 96 % | 54.1 px | 0.19 | 13.01 | 561 |
| stroke 8 | 11 % → 97 % | 87.1 px | 0.20 | 8.44 | 275 |
| stroke 9 | 24 % → 97 % | 111.5 px | 0.20 | 4.09 | 584 |
| stroke 10 | 20 % → 96 % | 182.5 px | 0.20 | 4.81 | 408 |
| stroke 11 | 28 % → 95 % | 156.5 px | 0.20 | 3.45 | 706 |
| stroke 12 | 30 % → 98 % | 329.0 px | 0.21 | 3.27 | 285 |
| stroke 13 | 47 % → 97 % | 304.5 px | 0.21 | 2.05 | 471 |
| stroke 14 | 50 % → 97 % | 506.5 px | 0.22 | 1.93 | 239 |
| stroke 15 | 42 % → 97 % | 238.1 px | 0.18 | 2.31 | 524 |
| stroke 16 | 43 % → 98 % | 320.4 px | 0.22 | 2.27 | 486 |
| stroke 17 | 32 % → 89 % | 317.1 px | 0.19 | 2.83 | 400 |
| stroke 18 | 53 % → 97 % | 556.4 px | 0.20 | 1.83 | 286 |
| stroke 19 | 28 % → 84 % | 301.5 px | 0.18 | 2.97 | 287 |
| stroke 20 | 23 % → 70 % | 157.0 px | 0.24 | 3.04 | 597 |
| stroke 21 | 29 % → 63 % | 304.9 px | 0.25 | 2.22 | 306 |
| stroke 22 | 43 % → 62 % | 402.4 px | 0.28 | 1.45 | 235 |
| stroke 23 | 17 % → 98 % | 86.3 px | 0.21 | 5.71 | 1265 |
| stroke 24 | 10 % → 96 % | 116.3 px | 0.21 | 9.96 | 302 |
| stroke 25 | 22 % → 97 % | 233.6 px | 0.22 | 4.44 | 305 |
| stroke 26 | 17 % → 99 % | 196.3 px | 0.25 | 5.71 | 257 |
| stroke 27 | 27 % → 98 % | 345.3 px | 0.26 | 3.63 | 294 |
| stroke 28 | 23 % → 97 % | 294.8 px | 0.22 | 4.17 | 347 |
| stroke 29 | 38 % → 97 % | 286.4 px | 0.22 | 2.53 | 712 |
| stroke 30 | 32 % → 91 % | 272.7 px | 0.21 | 2.85 | 608 |
| stroke 31 | 22 % → 99 % | 200.7 px | 0.24 | 4.51 | 458 |
| stroke 32 | 37 % → 96 % | 329.2 px | 0.25 | 2.60 | 415 |
| stroke 33 | 55 % → 97 % | 570.9 px | 0.26 | 1.77 | 435 |
| stroke 34 | 54 % → 97 % | 399.3 px | 0.22 | 1.79 | 748 |
| stroke 35 | 47 % → 96 % | 590.9 px | 0.21 | 2.07 | 347 |
| stroke 36 | 36 % → 98 % | 493.4 px | 0.24 | 2.70 | 268 |
| stroke 37 | 63 % → 97 % | 855.4 px | 0.22 | 1.54 | 327 |
| stroke 38 | 67 % → 96 % | 985.5 px | 0.21 | 1.43 | 251 |
| stroke 39 | 11 % → 96 % | 53.3 px | 0.30 | 8.38 | 2475 |
| stroke 40 | 12 % → 82 % | 90.6 px | 0.26 | 6.60 | 1143 |
| stroke 41 | 19 % → 98 % | 133.3 px | 0.28 | 5.11 | 797 |
| stroke 42 | 32 % → 99 % | 356.1 px | 0.26 | 3.12 | 549 |
| stroke 43 | 18 % → 80 % | 118.2 px | 0.28 | 4.43 | 1172 |
| stroke 44 | 31 % → 97 % | 249.1 px | 0.27 | 3.14 | 1015 |
| stroke 45 | 30 % → 88 % | 191.6 px | 0.29 | 2.88 | 976 |
| stroke 46 | 24 % → 100 % | 181.0 px | 0.30 | 4.21 | 784 |
| stroke 47 | 34 % → 99 % | 222.4 px | 0.28 | 2.95 | 760 |
| stroke 48 | 27 % → 78 % | 197.2 px | 0.26 | 2.93 | 971 |
| stroke 49 | 33 % → 66 % | 186.2 px | 0.26 | 2.01 | 679 |
| stroke 50 | 48 % → 98 % | 274.5 px | 0.29 | 2.06 | 1208 |
| stroke 51 | 52 % → 99 % | 557.8 px | 0.29 | 1.88 | 395 |
| stroke 52 | 33 % → 89 % | 240.7 px | 0.28 | 2.71 | 735 |
| stroke 53 | 37 % → 94 % | 216.4 px | 0.29 | 2.55 | 1261 |
| stroke 54 | 38 % → 64 % | 297.2 px | 0.26 | 1.67 | 448 |
| stroke 55 | 46 % → 90 % | 339.8 px | 0.26 | 1.97 | 805 |
| stroke 56 | 57 % → 99 % | 390.4 px | 0.29 | 1.73 | 899 |
| stroke 57 | 57 % → 93 % | 476.8 px | 0.29 | 1.64 | 610 |
| stroke 58 | 51 % → 80 % | 426.2 px | 0.26 | 1.59 | 482 |
| stroke 59 | 62 % → 88 % | 678.9 px | 0.28 | 1.42 | 400 |
| stroke 60 | 41 % → 64 % | 390.5 px | 0.26 | 1.57 | 612 |
| stroke 61 | 54 % → 82 % | 342.3 px | 0.28 | 1.53 | 1088 |
| stroke 62 | 77 % → 99 % | 649.0 px | 0.29 | 1.29 | 564 |
| stroke 63 | 65 % → 99 % | 451.3 px | 0.30 | 1.52 | 701 |
| stroke 64 | 70 % → 88 % | 665.0 px | 0.25 | 1.25 | 524 |
| stroke 65 | 49 % → 68 % | 678.4 px | 0.26 | 1.38 | 320 |
| stroke 66 | 38 % → 52 % | 419.0 px | 0.27 | 1.37 | 214 |
| stroke 67 | 46 % → 60 % | 470.2 px | 0.27 | 1.30 | 300 |
| stroke 68 | 62 % → 99 % | 752.7 px | 0.30 | 1.61 | 362 |
| stroke 69 | 59 % → 94 % | 518.7 px | 0.28 | 1.60 | 538 |
| stroke 70 | 67 % → 85 % | 823.2 px | 0.27 | 1.27 | 335 |
| stroke 71 | 45 % → 99 % | 559.5 px | 0.30 | 2.22 | 309 |
| stroke 72 | 61 % → 81 % | 716.7 px | 0.28 | 1.34 | 423 |
| stroke 73 | 53 % → 68 % | 450.7 px | 0.25 | 1.28 | 387 |
| stroke 74 | 78 % → 98 % | 886.8 px | 0.30 | 1.25 | 429 |
| stroke 75 | 57 % → 100 % | 540.0 px | 0.30 | 1.74 | 494 |
| stroke 76 | 37 % → 53 % | 542.5 px | 0.27 | 1.41 | 238 |
| stroke 77 | 45 % → 100 % | 617.4 px | 0.30 | 2.24 | 264 |
| stroke 78 | 55 % → 76 % | 785.9 px | 0.29 | 1.39 | 574 |
| stroke 79 | 53 % → 62 % | 475.5 px | 0.26 | 1.17 | 602 |
| stroke 80 | 49 % → 92 % | 499.1 px | 0.28 | 1.90 | 431 |
| stroke 81 | 74 % → 99 % | 730.0 px | 0.28 | 1.34 | 440 |
| stroke 82 | 57 % → 100 % | 782.5 px | 0.31 | 1.74 | 326 |
| stroke 83 | 75 % → 99 % | 979.3 px | 0.30 | 1.32 | 245 |
| stroke 84 | 52 % → 63 % | 454.4 px | 0.24 | 1.20 | 281 |
| stroke 85 | 13 % → 81 % | 63.3 px | 0.22 | 6.37 | 264 |
| stroke 86 | 11 % → 75 % | 173.8 px | 0.19 | 6.74 | 32 |
| stroke 87 | 13 % → 95 % | 153.0 px | 0.21 | 7.27 | 95 |
| stroke 88 | 20 % → 91 % | 426.8 px | 0.21 | 4.44 | 52 |
| stroke 89 | 46 % → 96 % | 536.8 px | 0.22 | 2.12 | 123 |
| stroke 90 | 17 % → 63 % | 299.0 px | 0.22 | 3.64 | 55 |
| stroke 91 | 20 % → 81 % | 170.9 px | 0.19 | 4.08 | 144 |
| stroke 92 | 52 % → 90 % | 935.1 px | 0.29 | 1.73 | 58 |
| stroke 93 | 17 % → 98 % | 186.9 px | 0.28 | 5.77 | 123 |
| stroke 94 | 28 % → 89 % | 422.2 px | 0.28 | 3.22 | 50 |
| stroke 95 | 27 % → 67 % | 196.3 px | 0.20 | 2.44 | 972 |
| stroke 96 | 50 % → 96 % | 293.5 px | 0.21 | 1.92 | 2006 |
| stroke 97 | 58 % → 98 % | 341.7 px | 0.18 | 1.69 | 1765 |
| stroke 98 | 43 % → 84 % | 206.8 px | 0.21 | 1.97 | 2451 |
| stroke 99 | 71 % → 97 % | 392.1 px | 0.21 | 1.36 | 2756 |
| stroke 100 | 45 % → 83 % | 232.4 px | 0.21 | 1.87 | 2555 |
| stroke 101 | 39 % → 76 % | 154.5 px | 0.21 | 1.94 | 1424 |
| stroke 102 | 50 % → 84 % | 314.9 px | 0.19 | 1.69 | 1840 |
| stroke 103 | 61 % → 93 % | 281.9 px | 0.20 | 1.52 | 3145 |
| stroke 104 | 62 % → 92 % | 519.4 px | 0.21 | 1.47 | 1061 |
| stroke 105 | 68 % → 97 % | 636.2 px | 0.20 | 1.41 | 941 |
| stroke 106 | 75 % → 97 % | 740.3 px | 0.21 | 1.31 | 740 |
| stroke 107 | 83 % → 97 % | 503.9 px | 0.20 | 1.17 | 1644 |
| stroke 108 | 61 % → 85 % | 441.4 px | 0.28 | 1.39 | 1352 |
| stroke 109 | 65 % → 84 % | 309.9 px | 0.21 | 1.29 | 1840 |
| stroke 110 | 70 % → 94 % | 463.6 px | 0.21 | 1.35 | 1830 |
| stroke 111 | 64 % → 81 % | 372.0 px | 0.21 | 1.26 | 1699 |
| stroke 112 | 68 % → 83 % | 406.8 px | 0.20 | 1.23 | 2050 |
| stroke 113 | 57 % → 70 % | 339.5 px | 0.23 | 1.23 | 2733 |
| stroke 114 | 76 % → 84 % | 438.7 px | 0.21 | 1.11 | 1008 |
| stroke 115 | 75 % → 81 % | 541.6 px | 0.22 | 1.08 | 1131 |
| stroke 116 | 71 % → 85 % | 475.6 px | 0.25 | 1.20 | 1640 |
| stroke 117 | 89 % → 93 % | 573.3 px | 0.20 | 1.04 | 1809 |
| stroke 118 | 74 % → 80 % | 628.3 px | 0.22 | 1.08 | 1043 |
| stroke 119 | 64 % → 73 % | 428.8 px | 0.25 | 1.14 | 1572 |
| stroke 120 | 88 % → 96 % | 830.2 px | 0.22 | 1.10 | 1190 |
| stroke 121 | 69 % → 70 % | 483.6 px | 0.21 | 1.01 | 1936 |
| stroke 122 | 79 % → 91 % | 765.2 px | 0.22 | 1.16 | 1672 |
| stroke 123 | 56 % → 77 % | 516.8 px | 0.19 | 1.37 | 1475 |
| stroke 124 | 94 % → 96 % | 806.7 px | 0.20 | 1.02 | 2508 |
| stroke 125 | 96 % → 97 % | 1035.4 px | 0.22 | 1.01 | 1385 |
| stroke 126 | 79 % → 85 % | 543.6 px | 0.21 | 1.08 | 2376 |
| stroke 127 | 97 % → 97 % | 1000.8 px | 0.21 | 1.00 | 2294 |
| stroke 128 | 92 % → 96 % | 953.1 px | 0.21 | 1.04 | 1535 |
| stroke 129 | 73 % → 84 % | 559.7 px | 0.25 | 1.15 | 1545 |
| stroke 130 | 71 % → 78 % | 800.2 px | 0.22 | 1.09 | 598 |
| stroke 131 | 53 % → 59 % | 312.9 px | 0.27 | 1.12 | 1638 |
| stroke 132 | 83 % → 99 % | 799.6 px | 0.28 | 1.19 | 746 |
| stroke 133 | 78 % → 99 % | 425.8 px | 0.30 | 1.27 | 3024 |
| stroke 134 | 86 % → 99 % | 630.3 px | 0.29 | 1.16 | 1229 |
| stroke 135 | 58 % → 66 % | 415.1 px | 0.26 | 1.14 | 199 |
| stroke 136 | 56 % → 96 % | 502.5 px | 0.15 | 1.71 | 123 |
| stroke 137 | 29 % → 99 % | 279.8 px | 0.25 | 3.39 | 193 |
| stroke 138 | 66 % → 66 % | 312.2 px | 0.17 | 1.01 | 1422 |
| stroke 139 | 79 % → 81 % | 411.6 px | 0.19 | 1.02 | 2227 |
| stroke 140 | 62 % → 98 % | 231.6 px | 0.15 | 1.58 | 2890 |
| stroke 141 | 76 % → 99 % | 402.4 px | 0.10 | 1.30 | 1180 |
| stroke 142 | 83 % → 99 % | 519.9 px | 0.15 | 1.19 | 2024 |
| stroke 143 | 75 % → 99 % | 378.4 px | 0.25 | 1.32 | 2393 |
| stroke 144 | 79 % → 99 % | 480.5 px | 0.20 | 1.25 | 1235 |
| stroke 145 | 85 % → 98 % | 440.6 px | 0.08 | 1.15 | 1275 |
| stroke 146 | 95 % → 97 % | 453.9 px | 0.11 | 1.02 | 1818 |
| stroke 147 | 98 % → 97 % | 462.7 px | 0.14 | 0.99 | 1896 |
| stroke 148 | 54 % → 96 % | 134.7 px | 0.22 | 1.80 | 3521 |
| stroke 149 | 64 % → 98 % | 263.3 px | 0.24 | 1.54 | 2051 |
| stroke 150 | 82 % → 97 % | 339.1 px | 0.13 | 1.18 | 1184 |
| stroke 151 | 71 % → 98 % | 425.9 px | 0.26 | 1.39 | 1749 |
| stroke 152 | 83 % → 97 % | 187.4 px | 0.14 | 1.16 | 1757 |
| stroke 153 | 38 % → 68 % | 207.3 px | 0.29 | 1.76 | 1187 |
| stroke 154 | 64 % → 78 % | 929.8 px | 0.26 | 1.22 | 62 |
| stroke 155 | 72 % → 74 % | 544.0 px | 0.22 | 1.02 | 518 |
| stroke 156 | 70 % → 72 % | 743.4 px | 0.23 | 1.02 | 203 |
| stroke 157 | 68 % → 68 % | 897.5 px | 0.22 | 0.99 | 206 |
| stroke 158 | 55 % → 59 % | 344.4 px | 0.26 | 1.07 | 482 |
| stroke 159 | 52 % → 52 % | 469.5 px | 0.26 | 1.00 | 326 |
| stroke 160 | 74 % → 91 % | 399.3 px | 0.27 | 1.23 | 1820 |
| stroke 161 | 68 % → 73 % | 452.6 px | 0.28 | 1.07 | 1369 |
| stroke 162 | 91 % → 97 % | 675.4 px | 0.23 | 1.07 | 1803 |
| stroke 163 | 89 % → 100 % | 800.9 px | 0.22 | 1.12 | 911 |
| stroke 164 | 77 % → 94 % | 462.8 px | 0.28 | 1.23 | 742 |
| stroke 165 | 81 % → 93 % | 498.2 px | 0.28 | 1.16 | 704 |
| stroke 166 | 82 % → 99 % | 482.5 px | 0.29 | 1.20 | 595 |
| stroke 167 | 81 % → 99 % | 424.0 px | 0.28 | 1.23 | 812 |
| stroke 168 | 79 % → 93 % | 537.4 px | 0.29 | 1.18 | 1265 |
| stroke 169 | 83 % → 88 % | 894.4 px | 0.28 | 1.06 | 542 |
| stroke 170 | 89 % → 99 % | 664.9 px | 0.28 | 1.11 | 1467 |
| stroke 171 | 89 % → 100 % | 610.8 px | 0.31 | 1.12 | 1632 |
| stroke 172 | 88 % → 100 % | 521.8 px | 0.28 | 1.14 | 909 |
| stroke 173 | 87 % → 100 % | 674.8 px | 0.30 | 1.15 | 219 |
| stroke 174 | 93 % → 96 % | 1420.0 px | 0.30 | 1.03 | 243 |
| stroke 175 | 92 % → 99 % | 683.4 px | 0.25 | 1.08 | 1062 |
| stroke 176 | 91 % → 99 % | 1284.3 px | 0.32 | 1.10 | 217 |
| stroke 177 | 95 % → 99 % | 836.5 px | 0.24 | 1.04 | 639 |
| stroke 178 | 94 % → 99 % | 712.7 px | 0.33 | 1.06 | 493 |
| stroke 179 | 97 % → 100 % | 514.6 px | 0.33 | 1.03 | 616 |
| stroke 180 | 95 % → 97 % | 773.9 px | 0.28 | 1.02 | 626 |
| stroke 181 | 94 % → 98 % | 836.1 px | 0.28 | 1.04 | 485 |
| stroke 182 | 99 % → 100 % | 878.3 px | 0.30 | 1.00 | 515 |
| stroke 183 | 83 % → 86 % | 645.7 px | 0.30 | 1.04 | 521 |
| stroke 184 | 98 % → 99 % | 590.4 px | 0.28 | 1.00 | 715 |
| stroke 185 | 86 % → 88 % | 750.3 px | 0.30 | 1.03 | 614 |
| stroke 186 | 97 % → 97 % | 939.2 px | 0.29 | 1.00 | 314 |
| stroke 187 | 92 % → 94 % | 1185.1 px | 0.30 | 1.01 | 344 |
| stroke 188 | 99 % → 99 % | 510.2 px | 0.30 | 1.00 | 789 |
| stroke 189 | 99 % → 99 % | 659.6 px | 0.29 | 1.00 | 369 |
| stroke 190 | 99 % → 99 % | 1075.0 px | 0.31 | 1.00 | 436 |
| stroke 191 | 100 % → 100 % | 1066.4 px | 0.21 | 1.00 | 513 |
| stroke 192 | 100 % → 100 % | 1582.1 px | 0.23 | 1.00 | 312 |
| stroke 193 | 100 % → 100 % | 1364.2 px | 0.32 | 1.00 | 491 |
| stroke 194 | 97 % → 97 % | 1516.9 px | 0.22 | 1.00 | 641 |
| stroke 195 | 97 % → 98 % | 1536.0 px | 0.28 | 1.02 | 225 |
| stroke 196 | 98 % → 98 % | 1422.7 px | 0.23 | 1.00 | 257 |
| stroke 197 | 97 % → 97 % | 1351.7 px | 0.30 | 1.00 | 230 |
| stroke 198 | 94 % → 94 % | 1180.2 px | 0.30 | 1.00 | 267 |
| stroke 199 | 69 % → 71 % | 386.7 px | 0.26 | 1.02 | 1172 |
| stroke 200 | 76 % → 76 % | 625.5 px | 0.27 | 1.00 | 786 |
| stroke 201 | 67 % → 67 % | 681.5 px | 0.26 | 1.00 | 509 |
| stroke 202 | 97 % → 97 % | 985.7 px | 0.16 | 1.00 | 153 |
| stroke 203 | 97 % → 97 % | 1438.5 px | 0.28 | 1.00 | 100 |

Numbers say: wet paint spreads well beyond the stroke.

## Refs v3 · #15 Ultramarine script — own sheet
own sheet 800 × 1422 · Ink 0.98 · 39 px · 950.3 s

![Refs v3 · #15 Ultramarine script — own sheet](Refs-v3-15-Ultramarine-script-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 3 % → 33 % | 15.9 px | 0.69 | 12.41 | 112 |
| stroke 2 | 4 % → 35 % | 21.3 px | 0.71 | 8.92 | 18 |
| stroke 3 | 11 % → 36 % | 23.7 px | 0.70 | 3.26 | 126 |
| stroke 4 | 14 % → 34 % | 77.1 px | 0.70 | 2.38 | 42 |
| stroke 5 | 16 % → 30 % | 202.7 px | 0.70 | 1.86 | 16 |
| stroke 6 | 17 % → 31 % | 223.3 px | 0.70 | 1.76 | 10 |
| stroke 7 | 17 % → 29 % | 93.4 px | 0.69 | 1.67 | 54 |
| stroke 8 | 27 % → 35 % | 241.4 px | 0.71 | 1.31 | 25 |
| stroke 9 | 3 % → 27 % | 15.4 px | 0.70 | 10.02 | 27 |
| stroke 10 | 5 % → 34 % | 27.0 px | 0.70 | 6.93 | 42 |
| stroke 11 | 4 % → 26 % | 58.4 px | 0.70 | 5.87 | 18 |
| stroke 12 | 9 % → 27 % | 31.5 px | 0.70 | 2.98 | 125 |
| stroke 13 | 13 % → 27 % | 92.9 px | 0.70 | 2.05 | 43 |
| stroke 14 | 18 % → 27 % | 112.5 px | 0.70 | 1.56 | 61 |
| stroke 15 | 19 % → 29 % | 96.2 px | 0.69 | 1.56 | 87 |
| stroke 16 | 11 % → 35 % | 91.6 px | 0.69 | 3.30 | 43 |
| stroke 17 | 4 % → 42 % | 21.2 px | 0.70 | 9.73 | 26 |
| stroke 18 | 11 % → 40 % | 49.3 px | 0.70 | 3.64 | 38 |
| stroke 19 | 15 % → 32 % | 87.9 px | 0.69 | 2.19 | 44 |
| stroke 20 | 17 % → 37 % | 226.4 px | 0.69 | 2.15 | 15 |
| stroke 21 | 18 % → 34 % | 231.1 px | 0.69 | 1.86 | 30 |
| stroke 22 | 22 % → 37 % | 62.3 px | 0.69 | 1.66 | 147 |
| stroke 23 | 35 % → 40 % | 367.0 px | 0.69 | 1.15 | 26 |
| stroke 24 | 2 % → 27 % | 19.5 px | 0.68 | 14.03 | 21 |
| stroke 25 | 2 % → 41 % | 36.9 px | 0.69 | 18.28 | 13 |
| stroke 26 | 4 % → 53 % | 19.2 px | 0.70 | 12.76 | 44 |
| stroke 27 | 4 % → 38 % | 43.5 px | 0.70 | 10.10 | 26 |
| stroke 28 | 25 % → 49 % | 67.6 px | 0.70 | 1.96 | 82 |
| stroke 29 | 4 % → 42 % | 33.2 px | 0.69 | 10.02 | 29 |
| stroke 30 | 7 % → 34 % | 40.0 px | 0.69 | 4.57 | 76 |
| stroke 31 | 10 % → 38 % | 92.1 px | 0.69 | 3.73 | 30 |
| stroke 32 | 14 % → 33 % | 117.0 px | 0.69 | 2.43 | 29 |
| stroke 33 | 9 % → 29 % | 72.0 px | 0.69 | 3.16 | 38 |
| stroke 34 | 7 % → 31 % | 49.3 px | 0.69 | 4.40 | 48 |
| stroke 35 | 14 % → 34 % | 134.8 px | 0.69 | 2.42 | 29 |
| stroke 36 | 9 % → 31 % | 44.8 px | 0.69 | 3.52 | 68 |
| stroke 37 | 17 % → 50 % | 94.0 px | 0.70 | 2.97 | 46 |
| stroke 38 | 14 % → 29 % | 68.9 px | 0.68 | 2.04 | 76 |
| stroke 39 | 24 % → 42 % | 132.2 px | 0.69 | 1.75 | 57 |
| stroke 40 | 27 % → 43 % | 190.7 px | 0.69 | 1.62 | 44 |
| stroke 41 | 29 % → 43 % | 464.6 px | 0.69 | 1.49 | 27 |
| stroke 42 | 25 % → 38 % | 486.0 px | 0.69 | 1.51 | 6 |
| stroke 43 | 22 % → 39 % | 125.8 px | 0.69 | 1.76 | 62 |
| stroke 44 | 23 % → 41 % | 128.8 px | 0.70 | 1.80 | 90 |
| stroke 45 | 18 % → 34 % | 223.6 px | 0.69 | 1.88 | 13 |
| stroke 46 | 25 % → 49 % | 225.3 px | 0.70 | 1.97 | 36 |
| stroke 47 | 32 % → 44 % | 103.7 px | 0.70 | 1.38 | 100 |
| stroke 48 | 24 % → 35 % | 312.7 px | 0.69 | 1.44 | 18 |
| stroke 49 | 26 % → 36 % | 287.8 px | 0.69 | 1.39 | 27 |
| stroke 50 | 26 % → 33 % | 312.6 px | 0.69 | 1.25 | 18 |
| stroke 51 | 31 % → 40 % | 168.9 px | 0.69 | 1.28 | 49 |
| stroke 52 | 15 % → 45 % | 201.8 px | 0.70 | 2.89 | 22 |
| stroke 53 | 7 % → 37 % | 144.7 px | 0.68 | 5.00 | 15 |
| stroke 54 | 5 % → 44 % | 29.0 px | 0.69 | 8.95 | 91 |
| stroke 55 | 5 % → 46 % | 34.0 px | 0.70 | 10.07 | 35 |
| stroke 56 | 8 % → 37 % | 39.7 px | 0.68 | 4.49 | 31 |
| stroke 57 | 12 % → 37 % | 93.6 px | 0.70 | 3.07 | 87 |
| stroke 58 | 10 % → 49 % | 78.0 px | 0.69 | 4.83 | 48 |
| stroke 59 | 24 % → 51 % | 218.3 px | 0.70 | 2.11 | 55 |
| stroke 60 | 11 % → 38 % | 79.9 px | 0.69 | 3.60 | 40 |
| stroke 61 | 11 % → 33 % | 69.0 px | 0.69 | 3.16 | 41 |
| stroke 62 | 29 % → 49 % | 334.6 px | 0.70 | 1.72 | 21 |
| stroke 63 | 14 % → 43 % | 163.7 px | 0.69 | 3.00 | 20 |
| stroke 64 | 15 % → 46 % | 105.1 px | 0.69 | 3.19 | 31 |
| stroke 65 | 26 % → 47 % | 106.9 px | 0.70 | 1.86 | 106 |
| stroke 66 | 10 % → 45 % | 133.2 px | 0.70 | 4.42 | 18 |
| stroke 67 | 18 % → 43 % | 110.4 px | 0.70 | 2.32 | 63 |
| stroke 68 | 28 % → 43 % | 232.4 px | 0.70 | 1.52 | 50 |
| stroke 69 | 34 % → 41 % | 267.1 px | 0.70 | 1.21 | 79 |
| stroke 70 | 15 % → 40 % | 227.5 px | 0.68 | 2.75 | 7 |
| stroke 71 | 27 % → 40 % | 351.9 px | 0.70 | 1.49 | 22 |
| stroke 72 | 17 % → 44 % | 100.3 px | 0.68 | 2.52 | 70 |
| stroke 73 | 24 % → 38 % | 369.6 px | 0.69 | 1.63 | 16 |
| stroke 74 | 21 % → 45 % | 104.7 px | 0.68 | 2.16 | 74 |
| stroke 75 | 22 % → 47 % | 191.5 px | 0.69 | 2.19 | 53 |
| stroke 76 | 34 % → 42 % | 119.2 px | 0.68 | 1.26 | 119 |
| stroke 77 | 33 % → 39 % | 177.8 px | 0.70 | 1.19 | 218 |
| stroke 78 | 26 % → 36 % | 117.6 px | 0.69 | 1.38 | 99 |
| stroke 79 | 30 % → 41 % | 167.1 px | 0.69 | 1.37 | 59 |
| stroke 80 | 27 % → 42 % | 245.6 px | 0.69 | 1.58 | 35 |
| stroke 81 | 29 % → 40 % | 160.2 px | 0.69 | 1.38 | 51 |
| stroke 82 | 24 % → 49 % | 89.5 px | 0.70 | 2.01 | 127 |
| stroke 83 | 35 % → 40 % | 340.9 px | 0.70 | 1.14 | 52 |
| stroke 84 | 34 % → 39 % | 625.7 px | 0.68 | 1.13 | 16 |
| stroke 85 | 29 % → 55 % | 221.7 px | 0.70 | 1.88 | 42 |
| stroke 86 | 32 % → 48 % | 228.0 px | 0.69 | 1.50 | 54 |
| stroke 87 | 18 % → 44 % | 97.3 px | 0.69 | 2.46 | 71 |
| stroke 88 | 18 % → 44 % | 264.4 px | 0.69 | 2.45 | 16 |
| stroke 89 | 24 % → 43 % | 88.8 px | 0.70 | 1.83 | 207 |
| stroke 90 | 27 % → 44 % | 212.3 px | 0.69 | 1.66 | 39 |
| stroke 91 | 37 % → 44 % | 329.1 px | 0.69 | 1.21 | 50 |
| stroke 92 | 28 % → 56 % | 227.7 px | 0.71 | 2.04 | 21 |
| stroke 93 | 6 % → 53 % | 36.7 px | 0.71 | 8.28 | 21 |
| stroke 94 | 22 % → 55 % | 136.0 px | 0.71 | 2.48 | 53 |
| stroke 95 | 31 % → 57 % | 224.1 px | 0.71 | 1.82 | 18 |
| stroke 96 | 25 % → 51 % | 394.7 px | 0.71 | 2.01 | 16 |
| stroke 97 | 17 % → 44 % | 117.2 px | 0.71 | 2.51 | 29 |
| stroke 98 | 29 % → 49 % | 312.2 px | 0.71 | 1.70 | 22 |
| stroke 99 | 27 % → 46 % | 146.2 px | 0.71 | 1.70 | 61 |
| stroke 100 | 45 % → 53 % | 241.6 px | 0.71 | 1.20 | 60 |
| stroke 101 | 14 % → 40 % | 120.1 px | 0.71 | 2.89 | 50 |
| stroke 102 | 12 % → 40 % | 87.5 px | 0.71 | 3.44 | 49 |
| stroke 103 | 14 % → 37 % | 167.2 px | 0.70 | 2.68 | 18 |
| stroke 104 | 30 % → 48 % | 212.2 px | 0.71 | 1.62 | 64 |
| stroke 105 | 21 % → 48 % | 226.0 px | 0.71 | 2.28 | 20 |
| stroke 106 | 16 % → 53 % | 177.9 px | 0.71 | 3.22 | 30 |
| stroke 107 | 17 % → 37 % | 91.0 px | 0.70 | 2.24 | 60 |
| stroke 108 | 30 % → 46 % | 256.6 px | 0.71 | 1.54 | 32 |
| stroke 109 | 25 % → 41 % | 117.6 px | 0.71 | 1.65 | 75 |
| stroke 110 | 27 % → 50 % | 384.6 px | 0.71 | 1.83 | 22 |
| stroke 111 | 31 % → 42 % | 472.9 px | 0.71 | 1.39 | 24 |
| stroke 112 | 34 % → 43 % | 586.7 px | 0.71 | 1.27 | 10 |
| stroke 113 | 31 % → 43 % | 411.1 px | 0.71 | 1.39 | 46 |
| stroke 114 | 36 % → 40 % | 562.4 px | 0.70 | 1.09 | 26 |
| stroke 115 | 32 % → 39 % | 295.0 px | 0.71 | 1.21 | 63 |
| stroke 116 | 3 % → 47 % | 20.8 px | 0.69 | 13.89 | 64 |
| stroke 117 | 27 % → 52 % | 158.1 px | 0.70 | 1.96 | 65 |
| stroke 118 | 28 % → 49 % | 487.8 px | 0.70 | 1.75 | 14 |
| stroke 119 | 24 % → 58 % | 335.5 px | 0.70 | 2.37 | 26 |
| stroke 120 | 5 % → 41 % | 85.9 px | 0.70 | 7.90 | 18 |
| stroke 121 | 7 % → 49 % | 33.4 px | 0.70 | 7.28 | 133 |
| stroke 122 | 12 % → 32 % | 42.7 px | 0.70 | 2.56 | 107 |
| stroke 123 | 16 % → 51 % | 105.9 px | 0.70 | 3.18 | 63 |
| stroke 124 | 15 % → 46 % | 105.6 px | 0.69 | 3.19 | 53 |
| stroke 125 | 4 % → 46 % | 33.7 px | 0.69 | 10.94 | 49 |
| stroke 126 | 10 % → 45 % | 64.2 px | 0.70 | 4.58 | 126 |
| stroke 127 | 16 % → 52 % | 70.3 px | 0.69 | 3.18 | 86 |
| stroke 128 | 12 % → 50 % | 86.2 px | 0.69 | 4.10 | 52 |
| stroke 129 | 27 % → 52 % | 299.4 px | 0.69 | 1.89 | 24 |
| stroke 130 | 19 % → 46 % | 120.4 px | 0.70 | 2.48 | 58 |
| stroke 131 | 24 % → 52 % | 136.5 px | 0.69 | 2.18 | 75 |
| stroke 132 | 30 % → 48 % | 227.2 px | 0.70 | 1.64 | 104 |
| stroke 133 | 22 % → 46 % | 91.2 px | 0.70 | 2.10 | 173 |
| stroke 134 | 22 % → 44 % | 131.5 px | 0.70 | 2.01 | 56 |
| stroke 135 | 18 % → 48 % | 287.2 px | 0.70 | 2.70 | 11 |
| stroke 136 | 31 % → 50 % | 161.2 px | 0.70 | 1.61 | 102 |
| stroke 137 | 41 % → 52 % | 734.3 px | 0.70 | 1.28 | 7 |
| stroke 138 | 28 % → 48 % | 240.8 px | 0.69 | 1.70 | 27 |
| stroke 139 | 34 % → 50 % | 252.7 px | 0.70 | 1.45 | 69 |
| stroke 140 | 34 % → 53 % | 443.3 px | 0.70 | 1.57 | 20 |
| stroke 141 | 35 % → 55 % | 381.7 px | 0.70 | 1.58 | 27 |
| stroke 142 | 31 % → 45 % | 168.6 px | 0.70 | 1.42 | 81 |
| stroke 143 | 35 % → 54 % | 480.7 px | 0.70 | 1.52 | 17 |
| stroke 144 | 39 % → 52 % | 274.3 px | 0.70 | 1.34 | 43 |
| stroke 145 | 43 % → 52 % | 312.9 px | 0.70 | 1.21 | 65 |
| stroke 146 | 43 % → 50 % | 330.1 px | 0.70 | 1.16 | 84 |
| stroke 147 | 47 % → 49 % | 194.9 px | 0.70 | 1.05 | 80 |
| stroke 148 | 34 % → 40 % | 655.6 px | 0.70 | 1.18 | 8 |
| stroke 149 | 6 % → 37 % | 66.4 px | 0.70 | 5.87 | 31 |
| stroke 150 | 14 % → 42 % | 103.4 px | 0.70 | 2.89 | 57 |
| stroke 151 | 7 % → 44 % | 41.6 px | 0.70 | 5.91 | 41 |
| stroke 152 | 20 % → 42 % | 125.6 px | 0.70 | 2.13 | 135 |
| stroke 153 | 42 % → 51 % | 244.9 px | 0.70 | 1.22 | 70 |
| stroke 154 | 31 % → 47 % | 77.0 px | 0.71 | 1.52 | 101 |
| stroke 155 | 44 % → 54 % | 529.7 px | 0.70 | 1.22 | 27 |
| stroke 156 | 21 % → 40 % | 183.8 px | 0.70 | 1.91 | 28 |
| stroke 157 | 20 % → 42 % | 125.6 px | 0.70 | 2.04 | 35 |
| stroke 158 | 21 % → 42 % | 169.5 px | 0.70 | 1.95 | 51 |
| stroke 159 | 35 % → 43 % | 157.5 px | 0.70 | 1.20 | 53 |
| stroke 160 | 27 % → 40 % | 145.9 px | 0.70 | 1.46 | 75 |
| stroke 161 | 31 % → 41 % | 142.1 px | 0.70 | 1.31 | 106 |
| stroke 162 | 8 % → 42 % | 65.7 px | 0.70 | 5.39 | 24 |
| stroke 163 | 1 % → 46 % | 15.8 px | 0.69 | 31.30 | 24 |
| stroke 164 | 16 % → 46 % | 139.9 px | 0.70 | 2.77 | 29 |
| stroke 165 | 17 % → 45 % | 146.4 px | 0.70 | 2.62 | 35 |
| stroke 166 | 44 % → 52 % | 272.4 px | 0.70 | 1.19 | 57 |
| stroke 167 | 22 % → 49 % | 293.7 px | 0.69 | 2.25 | 25 |
| stroke 168 | 3 % → 54 % | 40.1 px | 0.69 | 20.39 | 11 |
| stroke 169 | 3 % → 62 % | 13.2 px | 0.69 | 24.46 | 31 |
| stroke 170 | 3 % → 48 % | 30.0 px | 0.69 | 14.91 | 46 |
| stroke 171 | 7 % → 47 % | 54.2 px | 0.68 | 6.46 | 32 |
| stroke 172 | 42 % → 50 % | 402.6 px | 0.70 | 1.18 | 39 |
| stroke 173 | 8 % → 51 % | 35.2 px | 0.69 | 6.74 | 101 |
| stroke 174 | 15 % → 56 % | 75.6 px | 0.69 | 3.70 | 42 |
| stroke 175 | 5 % → 43 % | 49.9 px | 0.69 | 8.18 | 38 |
| stroke 176 | 7 % → 44 % | 55.5 px | 0.69 | 6.18 | 53 |
| stroke 177 | 12 % → 46 % | 82.6 px | 0.69 | 4.03 | 105 |
| stroke 178 | 28 % → 48 % | 92.6 px | 0.69 | 1.73 | 175 |
| stroke 179 | 15 % → 46 % | 110.8 px | 0.69 | 3.13 | 117 |
| stroke 180 | 17 % → 43 % | 162.0 px | 0.69 | 2.47 | 89 |
| stroke 181 | 27 % → 41 % | 270.5 px | 0.68 | 1.51 | 108 |
| stroke 182 | 23 % → 43 % | 188.2 px | 0.70 | 1.87 | 119 |
| stroke 183 | 13 % → 54 % | 189.8 px | 0.68 | 4.17 | 16 |
| stroke 184 | 17 % → 49 % | 150.1 px | 0.69 | 2.81 | 50 |
| stroke 185 | 24 % → 41 % | 287.6 px | 0.70 | 1.73 | 34 |
| stroke 186 | 29 % → 56 % | 77.2 px | 0.68 | 1.96 | 119 |
| stroke 187 | 17 % → 42 % | 195.6 px | 0.69 | 2.45 | 40 |
| stroke 188 | 35 % → 45 % | 152.7 px | 0.69 | 1.27 | 126 |
| stroke 189 | 24 % → 55 % | 47.4 px | 0.69 | 2.33 | 269 |
| stroke 190 | 35 % → 46 % | 258.6 px | 0.69 | 1.30 | 100 |
| stroke 191 | 23 % → 44 % | 172.8 px | 0.68 | 1.88 | 99 |
| stroke 192 | 29 % → 47 % | 216.0 px | 0.69 | 1.65 | 55 |
| stroke 193 | 39 % → 45 % | 368.1 px | 0.70 | 1.17 | 62 |
| stroke 194 | 28 % → 49 % | 172.8 px | 0.69 | 1.77 | 158 |
| stroke 195 | 34 % → 47 % | 250.9 px | 0.68 | 1.39 | 53 |
| stroke 196 | 36 % → 47 % | 155.5 px | 0.68 | 1.30 | 89 |
| stroke 197 | 33 % → 41 % | 64.6 px | 0.70 | 1.23 | 258 |
| stroke 198 | 20 % → 44 % | 97.5 px | 0.69 | 2.14 | 75 |
| stroke 199 | 25 % → 40 % | 317.3 px | 0.69 | 1.61 | 31 |
| stroke 200 | 33 % → 41 % | 161.4 px | 0.68 | 1.27 | 116 |
| stroke 201 | 29 % → 38 % | 217.2 px | 0.69 | 1.29 | 121 |
| stroke 202 | 35 % → 42 % | 254.2 px | 0.69 | 1.22 | 51 |
| stroke 203 | 34 % → 40 % | 392.2 px | 0.69 | 1.17 | 12 |
| stroke 204 | 40 % → 43 % | 204.6 px | 0.69 | 1.07 | 43 |
| stroke 205 | 2 % → 36 % | 27.4 px | 0.69 | 17.15 | 21 |
| stroke 206 | 24 % → 48 % | 113.6 px | 0.69 | 2.01 | 97 |
| stroke 207 | 18 % → 47 % | 138.7 px | 0.70 | 2.62 | 43 |
| stroke 208 | 2 % → 52 % | 13.4 px | 0.69 | 27.24 | 14 |
| stroke 209 | 11 % → 37 % | 47.6 px | 0.69 | 3.29 | 42 |
| stroke 210 | 9 % → 44 % | 57.6 px | 0.68 | 4.77 | 50 |
| stroke 211 | 8 % → 46 % | 76.1 px | 0.69 | 5.97 | 39 |
| stroke 212 | 15 % → 49 % | 39.1 px | 0.70 | 3.32 | 149 |
| stroke 213 | 23 % → 51 % | 91.7 px | 0.69 | 2.22 | 75 |
| stroke 214 | 20 % → 44 % | 316.0 px | 0.68 | 2.26 | 11 |
| stroke 215 | 25 % → 48 % | 366.0 px | 0.69 | 1.88 | 18 |
| stroke 216 | 20 % → 46 % | 129.1 px | 0.69 | 2.26 | 37 |
| stroke 217 | 30 % → 50 % | 266.4 px | 0.69 | 1.66 | 24 |
| stroke 218 | 36 % → 48 % | 165.6 px | 0.69 | 1.33 | 106 |
| stroke 219 | 30 % → 46 % | 260.6 px | 0.69 | 1.50 | 40 |
| stroke 220 | 36 % → 46 % | 564.5 px | 0.69 | 1.28 | 17 |
| stroke 221 | 33 % → 46 % | 230.9 px | 0.69 | 1.40 | 48 |
| stroke 222 | 41 % → 46 % | 324.8 px | 0.69 | 1.11 | 43 |
| stroke 223 | 39 % → 52 % | 306.4 px | 0.69 | 1.34 | 27 |
| stroke 224 | 14 % → 37 % | 99.4 px | 0.70 | 2.72 | 39 |
| stroke 225 | 17 % → 42 % | 133.4 px | 0.69 | 2.53 | 58 |
| stroke 226 | 30 % → 43 % | 133.6 px | 0.69 | 1.46 | 148 |
| stroke 227 | 25 % → 43 % | 214.3 px | 0.69 | 1.75 | 41 |
| stroke 228 | 12 % → 39 % | 147.4 px | 0.69 | 3.30 | 19 |
| stroke 229 | 26 % → 39 % | 143.9 px | 0.69 | 1.51 | 63 |
| stroke 230 | 26 % → 45 % | 94.3 px | 0.69 | 1.75 | 84 |
| stroke 231 | 19 % → 41 % | 158.2 px | 0.69 | 2.15 | 35 |
| stroke 232 | 25 % → 43 % | 305.6 px | 0.69 | 1.70 | 30 |
| stroke 233 | 30 % → 44 % | 133.1 px | 0.69 | 1.47 | 76 |
| stroke 234 | 24 % → 52 % | 274.1 px | 0.69 | 2.16 | 21 |
| stroke 235 | 12 % → 35 % | 77.8 px | 0.69 | 3.02 | 67 |
| stroke 236 | 28 % → 48 % | 215.2 px | 0.69 | 1.74 | 50 |
| stroke 237 | 29 % → 44 % | 125.4 px | 0.69 | 1.56 | 93 |
| stroke 238 | 23 % → 38 % | 87.1 px | 0.69 | 1.61 | 115 |
| stroke 239 | 27 % → 40 % | 252.0 px | 0.69 | 1.52 | 39 |
| stroke 240 | 21 % → 37 % | 177.8 px | 0.69 | 1.74 | 39 |
| stroke 241 | 30 % → 40 % | 117.5 px | 0.70 | 1.32 | 105 |
| stroke 242 | 2 % → 39 % | 15.9 px | 0.69 | 20.86 | 39 |
| stroke 243 | 7 % → 46 % | 27.2 px | 0.70 | 6.69 | 94 |
| stroke 244 | 18 % → 52 % | 215.1 px | 0.69 | 2.93 | 28 |
| stroke 245 | 1 % → 26 % | 13.9 px | 0.69 | 24.94 | 13 |
| stroke 246 | 4 % → 35 % | 23.8 px | 0.69 | 8.89 | 44 |
| stroke 247 | 10 % → 32 % | 50.1 px | 0.69 | 3.34 | 43 |
| stroke 248 | 9 % → 24 % | 78.7 px | 0.69 | 2.79 | 21 |
| stroke 249 | 7 % → 29 % | 58.5 px | 0.68 | 4.04 | 32 |
| stroke 250 | 15 % → 51 % | 141.3 px | 0.70 | 3.42 | 26 |
| stroke 251 | 8 % → 37 % | 72.4 px | 0.68 | 4.70 | 29 |
| stroke 252 | 11 % → 50 % | 128.8 px | 0.69 | 4.74 | 13 |
| stroke 253 | 8 % → 53 % | 130.6 px | 0.69 | 6.37 | 13 |
| stroke 254 | 11 % → 45 % | 76.4 px | 0.69 | 4.02 | 38 |
| stroke 255 | 23 % → 45 % | 273.6 px | 0.68 | 1.98 | 18 |
| stroke 256 | 18 % → 43 % | 190.0 px | 0.69 | 2.37 | 35 |
| stroke 257 | 22 % → 44 % | 322.2 px | 0.69 | 2.04 | 14 |
| stroke 258 | 39 % → 52 % | 257.8 px | 0.69 | 1.35 | 50 |
| stroke 259 | 15 % → 51 % | 194.8 px | 0.69 | 3.46 | 23 |
| stroke 260 | 31 % → 50 % | 129.6 px | 0.69 | 1.58 | 66 |
| stroke 261 | 18 % → 46 % | 85.1 px | 0.69 | 2.56 | 71 |
| stroke 262 | 17 % → 43 % | 271.0 px | 0.70 | 2.49 | 13 |
| stroke 263 | 17 % → 41 % | 149.2 px | 0.69 | 2.39 | 49 |
| stroke 264 | 24 % → 45 % | 301.6 px | 0.69 | 1.87 | 14 |
| stroke 265 | 20 % → 36 % | 309.5 px | 0.69 | 1.84 | 8 |
| stroke 266 | 13 % → 23 % | 179.3 px | 0.69 | 1.74 | 15 |
| stroke 267 | 13 % → 25 % | 79.4 px | 0.68 | 1.94 | 53 |
| stroke 268 | 19 % → 40 % | 178.8 px | 0.69 | 2.12 | 48 |
| stroke 269 | 27 % → 48 % | 140.3 px | 0.69 | 1.77 | 65 |
| stroke 270 | 18 % → 25 % | 259.1 px | 0.68 | 1.44 | 21 |
| stroke 271 | 28 % → 42 % | 207.2 px | 0.69 | 1.51 | 34 |
| stroke 272 | 39 % → 52 % | 392.3 px | 0.69 | 1.33 | 22 |
| stroke 273 | 22 % → 38 % | 130.6 px | 0.69 | 1.69 | 39 |
| stroke 274 | 26 % → 29 % | 221.6 px | 0.68 | 1.10 | 38 |
| stroke 275 | 35 % → 46 % | 198.5 px | 0.69 | 1.32 | 70 |
| stroke 276 | 33 % → 43 % | 548.8 px | 0.69 | 1.28 | 11 |
| stroke 277 | 28 % → 37 % | 237.9 px | 0.69 | 1.33 | 39 |
| stroke 278 | 41 % → 49 % | 279.9 px | 0.69 | 1.19 | 66 |
| stroke 279 | 26 % → 39 % | 295.8 px | 0.70 | 1.51 | 22 |
| stroke 280 | 31 % → 41 % | 501.5 px | 0.70 | 1.32 | 16 |
| stroke 281 | 39 % → 43 % | 348.2 px | 0.69 | 1.10 | 26 |
| stroke 282 | 41 % → 43 % | 157.0 px | 0.69 | 1.05 | 82 |
| stroke 283 | 28 % → 43 % | 83.2 px | 0.68 | 1.52 | 101 |
| stroke 284 | 12 % → 32 % | 57.4 px | 0.67 | 2.78 | 26 |
| stroke 285 | 10 % → 28 % | 58.0 px | 0.68 | 2.84 | 45 |
| stroke 286 | 16 % → 27 % | 110.0 px | 0.67 | 1.63 | 29 |
| stroke 287 | 33 % → 38 % | 151.2 px | 0.67 | 1.15 | 59 |
| stroke 288 | 35 % → 38 % | 233.9 px | 0.67 | 1.11 | 26 |
| stroke 289 | 26 % → 43 % | 225.8 px | 0.70 | 1.65 | 35 |
| stroke 290 | 16 % → 46 % | 89.1 px | 0.71 | 2.90 | 36 |
| stroke 291 | 38 % → 55 % | 176.0 px | 0.70 | 1.45 | 44 |
| stroke 292 | 26 % → 51 % | 192.8 px | 0.71 | 1.95 | 17 |
| stroke 293 | 38 % → 52 % | 102.9 px | 0.70 | 1.36 | 86 |
| stroke 294 | 32 % → 45 % | 215.8 px | 0.71 | 1.41 | 77 |
| stroke 295 | 9 % → 26 % | 80.8 px | 0.70 | 2.99 | 34 |
| stroke 296 | 26 % → 29 % | 73.8 px | 0.70 | 1.12 | 259 |
| stroke 297 | 26 % → 60 % | 97.2 px | 0.71 | 2.33 | 42 |
| stroke 298 | 4 % → 31 % | 31.6 px | 0.69 | 7.68 | 44 |
| stroke 299 | 2 % → 21 % | 14.3 px | 0.69 | 8.96 | 39 |
| stroke 300 | 7 % → 24 % | 70.5 px | 0.69 | 3.57 | 24 |
| stroke 301 | 8 % → 20 % | 43.6 px | 0.68 | 2.64 | 27 |
| stroke 302 | 16 % → 36 % | 50.5 px | 0.69 | 2.23 | 131 |
| stroke 303 | 16 % → 31 % | 130.7 px | 0.69 | 1.89 | 35 |
| stroke 304 | 13 % → 27 % | 112.3 px | 0.69 | 2.12 | 26 |
| stroke 305 | 20 % → 36 % | 200.4 px | 0.69 | 1.78 | 24 |
| stroke 306 | 20 % → 34 % | 167.4 px | 0.69 | 1.70 | 30 |
| stroke 307 | 10 % → 22 % | 82.3 px | 0.68 | 2.07 | 30 |
| stroke 308 | 18 % → 29 % | 164.9 px | 0.69 | 1.63 | 24 |
| stroke 309 | 18 % → 28 % | 146.3 px | 0.69 | 1.57 | 32 |
| stroke 310 | 17 % → 20 % | 91.6 px | 0.68 | 1.19 | 47 |
| stroke 311 | 13 % → 34 % | 72.3 px | 0.69 | 2.57 | 65 |
| stroke 312 | 2 % → 27 % | 19.8 px | 0.69 | 15.00 | 40 |
| stroke 313 | 15 % → 36 % | 122.3 px | 0.69 | 2.35 | 34 |
| stroke 314 | 24 % → 35 % | 287.2 px | 0.69 | 1.46 | 24 |
| stroke 315 | 13 % → 35 % | 159.6 px | 0.69 | 2.68 | 49 |
| stroke 316 | 24 % → 35 % | 172.5 px | 0.69 | 1.45 | 63 |
| stroke 317 | 27 % → 36 % | 464.2 px | 0.69 | 1.34 | 14 |
| stroke 318 | 20 % → 32 % | 158.9 px | 0.69 | 1.59 | 25 |
| stroke 319 | 26 % → 32 % | 494.5 px | 0.69 | 1.23 | 7 |
| stroke 320 | 20 % → 32 % | 179.4 px | 0.69 | 1.57 | 104 |
| stroke 321 | 8 % → 34 % | 61.7 px | 0.69 | 4.34 | 66 |
| stroke 322 | 16 % → 48 % | 148.9 px | 0.70 | 2.92 | 62 |
| stroke 323 | 7 % → 44 % | 43.0 px | 0.69 | 6.71 | 131 |
| stroke 324 | 26 % → 47 % | 52.9 px | 0.70 | 1.82 | 346 |
| stroke 325 | 30 % → 49 % | 199.7 px | 0.70 | 1.65 | 36 |
| stroke 326 | 29 % → 43 % | 220.9 px | 0.70 | 1.50 | 88 |
| stroke 327 | 18 % → 40 % | 71.8 px | 0.69 | 2.24 | 90 |
| stroke 328 | 23 % → 38 % | 85.8 px | 0.69 | 1.66 | 128 |
| stroke 329 | 28 % → 42 % | 165.3 px | 0.69 | 1.48 | 46 |
| stroke 330 | 18 % → 40 % | 52.4 px | 0.69 | 2.26 | 214 |
| stroke 331 | 36 % → 44 % | 385.7 px | 0.70 | 1.23 | 78 |
| stroke 332 | 34 % → 41 % | 221.2 px | 0.69 | 1.19 | 47 |
| stroke 333 | 6 % → 43 % | 44.7 px | 0.69 | 6.99 | 52 |
| stroke 334 | 6 % → 45 % | 51.4 px | 0.69 | 7.61 | 29 |
| stroke 335 | 8 % → 51 % | 65.1 px | 0.70 | 6.25 | 45 |
| stroke 336 | 2 % → 39 % | 15.4 px | 0.69 | 16.31 | 38 |
| stroke 337 | 6 % → 45 % | 39.8 px | 0.69 | 7.44 | 65 |
| stroke 338 | 12 % → 44 % | 149.3 px | 0.69 | 3.76 | 103 |
| stroke 339 | 24 % → 47 % | 205.1 px | 0.69 | 1.93 | 100 |
| stroke 340 | 12 % → 59 % | 97.3 px | 0.70 | 4.79 | 109 |
| stroke 341 | 29 % → 46 % | 170.2 px | 0.69 | 1.57 | 248 |
| stroke 342 | 8 % → 51 % | 89.0 px | 0.69 | 6.23 | 83 |
| stroke 343 | 19 % → 50 % | 153.0 px | 0.69 | 2.69 | 63 |
| stroke 344 | 22 % → 53 % | 362.0 px | 0.70 | 2.41 | 43 |
| stroke 345 | 19 % → 50 % | 164.8 px | 0.69 | 2.64 | 29 |
| stroke 346 | 28 % → 52 % | 392.0 px | 0.69 | 1.89 | 24 |
| stroke 347 | 29 % → 45 % | 97.3 px | 0.69 | 1.52 | 270 |
| stroke 348 | 36 % → 46 % | 228.1 px | 0.70 | 1.28 | 74 |
| stroke 349 | 38 % → 46 % | 234.9 px | 0.69 | 1.21 | 91 |
| stroke 350 | 35 % → 48 % | 313.8 px | 0.69 | 1.37 | 52 |
| stroke 351 | 32 % → 46 % | 279.7 px | 0.69 | 1.42 | 49 |
| stroke 352 | 33 % → 49 % | 569.1 px | 0.69 | 1.48 | 10 |
| stroke 353 | 28 % → 39 % | 251.3 px | 0.69 | 1.38 | 49 |
| stroke 354 | 11 % → 39 % | 69.9 px | 0.69 | 3.56 | 49 |
| stroke 355 | 22 % → 42 % | 188.6 px | 0.69 | 1.89 | 42 |
| stroke 356 | 6 % → 27 % | 28.1 px | 0.69 | 4.49 | 47 |
| stroke 357 | 19 % → 41 % | 79.5 px | 0.69 | 2.15 | 113 |
| stroke 358 | 8 % → 34 % | 42.2 px | 0.69 | 4.02 | 83 |
| stroke 359 | 14 % → 31 % | 100.9 px | 0.69 | 2.28 | 52 |
| stroke 360 | 18 % → 41 % | 216.0 px | 0.69 | 2.26 | 25 |
| stroke 361 | 21 % → 40 % | 382.0 px | 0.69 | 1.91 | 8 |
| stroke 362 | 20 % → 38 % | 137.4 px | 0.69 | 1.91 | 33 |
| stroke 363 | 19 % → 35 % | 295.3 px | 0.69 | 1.87 | 29 |
| stroke 364 | 25 % → 42 % | 195.8 px | 0.69 | 1.64 | 60 |
| stroke 365 | 23 % → 31 % | 276.4 px | 0.70 | 1.32 | 15 |
| stroke 366 | 31 % → 37 % | 224.3 px | 0.70 | 1.19 | 36 |
| stroke 367 | 16 % → 52 % | 48.1 px | 0.69 | 3.29 | 33 |
| stroke 368 | 4 % → 61 % | 17.4 px | 0.69 | 13.90 | 29 |
| stroke 369 | 17 % → 44 % | 90.0 px | 0.68 | 2.65 | 18 |
| stroke 370 | 8 % → 45 % | 75.5 px | 0.68 | 5.37 | 21 |
| stroke 371 | 10 % → 39 % | 180.6 px | 0.68 | 3.73 | 13 |
| stroke 372 | 11 % → 44 % | 109.8 px | 0.68 | 3.87 | 26 |
| stroke 373 | 18 % → 41 % | 74.6 px | 0.68 | 2.22 | 77 |
| stroke 374 | 23 % → 45 % | 131.8 px | 0.68 | 1.93 | 28 |
| stroke 375 | 17 % → 38 % | 150.9 px | 0.68 | 2.21 | 36 |
| stroke 376 | 31 % → 46 % | 279.4 px | 0.68 | 1.51 | 13 |
| stroke 377 | 24 % → 38 % | 82.5 px | 0.68 | 1.56 | 146 |
| stroke 378 | 8 % → 39 % | 43.9 px | 0.69 | 4.97 | 35 |
| stroke 379 | 25 % → 45 % | 103.1 px | 0.69 | 1.78 | 125 |
| stroke 380 | 12 % → 42 % | 71.4 px | 0.68 | 3.60 | 47 |
| stroke 381 | 12 % → 38 % | 47.7 px | 0.68 | 3.24 | 37 |
| stroke 382 | 28 % → 41 % | 96.4 px | 0.69 | 1.46 | 144 |
| stroke 383 | 23 % → 40 % | 151.3 px | 0.68 | 1.72 | 64 |
| stroke 384 | 29 % → 41 % | 185.3 px | 0.68 | 1.43 | 45 |
| stroke 385 | 6 % → 56 % | 24.4 px | 0.70 | 10.03 | 32 |
| stroke 386 | 14 % → 41 % | 59.8 px | 0.70 | 2.83 | 165 |
| stroke 387 | 4 % → 44 % | 27.9 px | 0.69 | 12.08 | 60 |
| stroke 388 | 33 % → 55 % | 65.4 px | 0.69 | 1.66 | 152 |
| stroke 389 | 20 % → 46 % | 82.8 px | 0.69 | 2.31 | 82 |
| stroke 390 | 8 % → 50 % | 126.2 px | 0.70 | 6.38 | 14 |
| stroke 391 | 27 % → 50 % | 91.9 px | 0.70 | 1.86 | 191 |
| stroke 392 | 21 % → 46 % | 68.9 px | 0.69 | 2.14 | 138 |
| stroke 393 | 26 % → 45 % | 138.1 px | 0.70 | 1.74 | 135 |
| stroke 394 | 30 % → 50 % | 167.3 px | 0.70 | 1.66 | 76 |
| stroke 395 | 19 % → 39 % | 62.0 px | 0.69 | 2.05 | 119 |
| stroke 396 | 34 % → 49 % | 280.9 px | 0.70 | 1.46 | 39 |
| stroke 397 | 39 % → 47 % | 701.2 px | 0.70 | 1.22 | 15 |
| stroke 398 | 22 % → 38 % | 411.2 px | 0.69 | 1.77 | 18 |
| stroke 399 | 28 % → 47 % | 242.0 px | 0.70 | 1.67 | 30 |
| stroke 400 | 44 % → 51 % | 182.1 px | 0.70 | 1.18 | 179 |
| stroke 401 | 39 % → 48 % | 116.1 px | 0.69 | 1.21 | 133 |
| stroke 402 | 37 % → 47 % | 329.7 px | 0.70 | 1.26 | 521 |
| stroke 403 | 42 % → 46 % | 257.9 px | 0.70 | 1.09 | 214 |
| stroke 404 | 55 % → 58 % | 1051.1 px | 0.69 | 1.06 | 26 |
| stroke 405 | 11 % → 35 % | 90.8 px | 0.69 | 3.25 | 79 |
| stroke 406 | 27 % → 38 % | 83.0 px | 0.69 | 1.41 | 263 |
| stroke 407 | 30 % → 41 % | 144.3 px | 0.69 | 1.38 | 90 |
| stroke 408 | 32 % → 42 % | 82.7 px | 0.69 | 1.29 | 65 |
| stroke 409 | 35 % → 41 % | 100.4 px | 0.70 | 1.18 | 35 |
| stroke 410 | 47 % → 52 % | 309.4 px | 0.70 | 1.11 | 9 |
| stroke 411 | 23 % → 38 % | 146.8 px | 0.69 | 1.70 | 14 |
| stroke 412 | 26 % → 39 % | 187.2 px | 0.69 | 1.48 | 10 |
| stroke 413 | 31 % → 38 % | 214.0 px | 0.69 | 1.25 | 14 |
| stroke 414 | 29 % → 38 % | 205.0 px | 0.70 | 1.30 | 17 |
| stroke 415 | 31 % → 38 % | 316.6 px | 0.69 | 1.20 | 8 |
| stroke 416 | 32 % → 37 % | 224.6 px | 0.69 | 1.16 | 18 |
| stroke 417 | 36 % → 41 % | 215.3 px | 0.70 | 1.16 | 109 |
| stroke 418 | 37 % → 39 % | 202.1 px | 0.70 | 1.07 | 73 |
| stroke 419 | 42 % → 45 % | 327.0 px | 0.69 | 1.08 | 18 |
| stroke 420 | 33 % → 36 % | 111.7 px | 0.69 | 1.09 | 28 |

Numbers say: wet paint spreads well beyond the stroke.

## Refs v3 · #16 Shrigley strokes — own sheet
own sheet 800 × 1000 · Watercolour 1.00 + water 30 % · 64 px · 319.8 s

![Refs v3 · #16 Shrigley strokes — own sheet](Refs-v3-16-Shrigley-strokes-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 6 % → 60 % | 32.8 px | 0.25 | 10.53 | 304 |
| stroke 2 | 4 % → 48 % | 48.6 px | 0.20 | 12.44 | 57 |
| stroke 3 | 7 % → 54 % | 87.9 px | 0.20 | 7.47 | 204 |
| stroke 4 | 10 % → 70 % | 45.4 px | 0.24 | 6.77 | 917 |
| stroke 5 | 3 % → 50 % | 28.8 px | 0.19 | 18.91 | 65 |
| stroke 6 | 7 % → 65 % | 119.3 px | 0.23 | 8.98 | 95 |
| stroke 7 | 8 % → 57 % | 55.3 px | 0.20 | 7.22 | 990 |
| stroke 8 | 15 % → 61 % | 115.1 px | 0.21 | 4.15 | 429 |
| stroke 9 | 19 % → 55 % | 333.5 px | 0.20 | 2.93 | 153 |
| stroke 10 | 14 % → 60 % | 72.2 px | 0.22 | 4.47 | 1312 |
| stroke 11 | 10 % → 59 % | 83.6 px | 0.22 | 5.87 | 447 |
| stroke 12 | 15 % → 51 % | 75.7 px | 0.19 | 3.44 | 626 |
| stroke 13 | 8 % → 58 % | 40.3 px | 0.21 | 7.29 | 1001 |
| stroke 14 | 8 % → 59 % | 79.5 px | 0.22 | 7.32 | 462 |
| stroke 15 | 24 % → 53 % | 121.6 px | 0.20 | 2.21 | 596 |
| stroke 16 | 12 % → 48 % | 87.5 px | 0.23 | 3.96 | 713 |
| stroke 17 | 27 % → 51 % | 246.6 px | 0.23 | 1.86 | 422 |
| stroke 18 | 11 % → 50 % | 130.8 px | 0.23 | 4.59 | 134 |
| stroke 19 | 10 % → 49 % | 45.5 px | 0.24 | 4.82 | 1267 |
| stroke 20 | 15 % → 51 % | 158.5 px | 0.24 | 3.37 | 386 |
| stroke 21 | 16 % → 53 % | 196.9 px | 0.24 | 3.25 | 139 |
| stroke 22 | 14 % → 55 % | 71.5 px | 0.22 | 4.06 | 894 |
| stroke 23 | 22 % → 51 % | 118.7 px | 0.24 | 2.37 | 1021 |
| stroke 24 | 17 % → 54 % | 104.0 px | 0.23 | 3.23 | 278 |
| stroke 25 | 24 % → 69 % | 98.3 px | 0.24 | 2.85 | 460 |
| stroke 26 | 29 % → 71 % | 161.0 px | 0.24 | 2.47 | 207 |
| stroke 27 | 24 % → 52 % | 127.9 px | 0.20 | 2.18 | 975 |
| stroke 28 | 23 % → 57 % | 178.3 px | 0.19 | 2.48 | 167 |
| stroke 29 | 27 % → 58 % | 246.3 px | 0.19 | 2.12 | 118 |
| stroke 30 | 18 % → 58 % | 564.7 px | 0.24 | 3.21 | 20 |
| stroke 31 | 27 % → 69 % | 300.6 px | 0.21 | 2.58 | 240 |
| stroke 32 | 28 % → 67 % | 677.0 px | 0.21 | 2.44 | 53 |
| stroke 33 | 33 % → 64 % | 253.6 px | 0.20 | 1.95 | 464 |
| stroke 34 | 27 % → 55 % | 211.7 px | 0.19 | 2.03 | 188 |
| stroke 35 | 39 % → 59 % | 263.2 px | 0.18 | 1.49 | 194 |
| stroke 36 | 36 % → 52 % | 400.6 px | 0.20 | 1.44 | 349 |
| stroke 37 | 41 % → 61 % | 288.0 px | 0.19 | 1.49 | 521 |
| stroke 38 | 38 % → 57 % | 208.0 px | 0.18 | 1.51 | 317 |
| stroke 39 | 44 % → 54 % | 401.4 px | 0.20 | 1.25 | 209 |
| stroke 40 | 31 % → 56 % | 357.3 px | 0.20 | 1.79 | 264 |
| stroke 41 | 28 % → 55 % | 248.1 px | 0.22 | 1.99 | 558 |
| stroke 42 | 33 % → 56 % | 488.2 px | 0.23 | 1.68 | 84 |
| stroke 43 | 23 % → 56 % | 132.0 px | 0.20 | 2.42 | 698 |
| stroke 44 | 25 % → 48 % | 198.0 px | 0.23 | 1.90 | 262 |
| stroke 45 | 36 % → 56 % | 482.6 px | 0.22 | 1.55 | 114 |
| stroke 46 | 27 % → 58 % | 282.6 px | 0.21 | 2.12 | 110 |
| stroke 47 | 30 % → 48 % | 740.9 px | 0.22 | 1.58 | 48 |
| stroke 48 | 24 % → 46 % | 290.3 px | 0.22 | 1.91 | 179 |
| stroke 49 | 31 % → 49 % | 340.2 px | 0.21 | 1.57 | 231 |
| stroke 50 | 36 % → 51 % | 297.1 px | 0.21 | 1.41 | 879 |
| stroke 51 | 30 % → 63 % | 406.3 px | 0.21 | 2.10 | 95 |
| stroke 52 | 32 % → 63 % | 425.5 px | 0.19 | 1.98 | 161 |
| stroke 53 | 35 % → 61 % | 1038.1 px | 0.19 | 1.75 | 34 |
| stroke 54 | 26 % → 47 % | 267.4 px | 0.23 | 1.84 | 180 |
| stroke 55 | 21 % → 46 % | 578.2 px | 0.25 | 2.22 | 23 |
| stroke 56 | 32 % → 60 % | 177.7 px | 0.22 | 1.85 | 828 |
| stroke 57 | 27 % → 51 % | 153.2 px | 0.23 | 1.88 | 195 |
| stroke 58 | 27 % → 51 % | 477.7 px | 0.24 | 1.87 | 153 |
| stroke 59 | 19 % → 53 % | 333.0 px | 0.25 | 2.79 | 39 |
| stroke 60 | 37 % → 51 % | 126.0 px | 0.25 | 1.39 | 312 |
| stroke 61 | 32 % → 51 % | 1116.1 px | 0.19 | 1.61 | 30 |
| stroke 62 | 44 % → 58 % | 245.1 px | 0.22 | 1.31 | 1745 |
| stroke 63 | 54 % → 57 % | 203.1 px | 0.19 | 1.04 | 954 |
| stroke 64 | 47 % → 54 % | 419.9 px | 0.22 | 1.16 | 245 |
| stroke 65 | 62 % → 68 % | 262.9 px | 0.22 | 1.10 | 1423 |
| stroke 66 | 37 % → 47 % | 1234.8 px | 0.18 | 1.28 | 44 |
| stroke 67 | 48 % → 52 % | 339.8 px | 0.19 | 1.09 | 679 |
| stroke 68 | 53 % → 51 % | 1178.3 px | 0.18 | 0.98 | 117 |
| stroke 69 | 50 % → 57 % | 309.0 px | 0.20 | 1.15 | 354 |
| stroke 70 | 44 % → 56 % | 239.8 px | 0.21 | 1.26 | 601 |
| stroke 71 | 40 % → 50 % | 179.6 px | 0.21 | 1.25 | 1914 |
| stroke 72 | 36 % → 48 % | 788.9 px | 0.21 | 1.32 | 124 |
| stroke 73 | 35 % → 50 % | 511.1 px | 0.21 | 1.45 | 134 |
| stroke 74 | 51 % → 57 % | 406.7 px | 0.21 | 1.11 | 472 |
| stroke 75 | 33 % → 56 % | 299.2 px | 0.25 | 1.68 | 436 |
| stroke 76 | 34 % → 50 % | 223.2 px | 0.26 | 1.46 | 316 |
| stroke 77 | 31 % → 49 % | 206.7 px | 0.25 | 1.60 | 428 |
| stroke 78 | 65 % → 67 % | 265.5 px | 0.23 | 1.04 | 1139 |
| stroke 79 | 48 % → 52 % | 649.5 px | 0.21 | 1.10 | 77 |
| stroke 80 | 59 % → 61 % | 651.4 px | 0.22 | 1.04 | 219 |
| stroke 81 | 56 % → 59 % | 690.6 px | 0.19 | 1.05 | 59 |
| stroke 82 | 67 % → 67 % | 909.0 px | 0.20 | 1.00 | 210 |
| stroke 83 | 58 % → 57 % | 539.9 px | 0.19 | 0.99 | 138 |
| stroke 84 | 60 % → 60 % | 1181.4 px | 0.17 | 0.99 | 67 |
| stroke 85 | 46 % → 51 % | 369.1 px | 0.23 | 1.11 | 515 |
| stroke 86 | 44 % → 50 % | 1319.2 px | 0.21 | 1.15 | 24 |
| stroke 87 | 51 % → 56 % | 1050.8 px | 0.23 | 1.08 | 97 |
| stroke 88 | 52 % → 51 % | 537.2 px | 0.22 | 0.99 | 384 |
| stroke 89 | 52 % → 53 % | 343.9 px | 0.22 | 1.04 | 810 |
| stroke 90 | 35 % → 43 % | 1124.8 px | 0.24 | 1.23 | 29 |
| stroke 91 | 33 % → 41 % | 962.6 px | 0.24 | 1.23 | 59 |
| stroke 92 | 51 % → 51 % | 260.0 px | 0.23 | 1.00 | 1815 |
| stroke 93 | 48 % → 48 % | 216.5 px | 0.25 | 0.99 | 548 |
| stroke 94 | 52 % → 52 % | 202.5 px | 0.24 | 0.99 | 488 |

Numbers say: wet paint spreads well beyond the stroke.

## Refs v3 · #17 Krovostok dry brush — own sheet
own sheet 800 × 720 · Ink 0.93 · Gouache 0.07 · 16 px · 296.6 s

![Refs v3 · #17 Krovostok dry brush — own sheet](Refs-v3-17-Krovostok-dry-brush-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 4 % → 15 % | 18.9 px | 0.37 | 3.71 | 20 |
| stroke 2 | 7 % → 7 % | 24.6 px | 0.37 | 0.96 | 9 |
| stroke 3 | 13 % → 31 % | 42.4 px | 0.39 | 2.45 | 16 |
| stroke 4 | 4 % → 32 % | 18.3 px | 0.42 | 8.34 | 9 |
| stroke 5 | 9 % → 47 % | 29.5 px | 0.41 | 5.43 | 20 |
| stroke 6 | 16 % → 9 % | 22.8 px | 0.39 | 0.56 | 135 |
| stroke 7 | 13 % → 44 % | 35.6 px | 0.42 | 3.44 | 30 |
| stroke 8 | 15 % → 0 % | 53.1 px | 0.00 | 0.00 | 38 |
| stroke 9 | 25 % → 8 % | 57.2 px | 0.39 | 0.31 | 42 |
| stroke 10 | 23 % → 31 % | 102.3 px | 0.41 | 1.36 | 8 |
| stroke 11 | 20 % → 43 % | 54.6 px | 0.42 | 2.17 | 22 |
| stroke 12 | 32 % → 23 % | 57.6 px | 0.41 | 0.71 | 66 |
| stroke 13 | 31 % → 42 % | 84.3 px | 0.42 | 1.38 | 26 |
| stroke 14 | 36 % → 26 % | 51.8 px | 0.43 | 0.71 | 108 |
| stroke 15 | 38 % → 46 % | 190.2 px | 0.43 | 1.20 | 11 |
| stroke 16 | 4 % → 11 % | 18.2 px | 0.42 | 2.79 | 6 |
| stroke 17 | 39 % → 37 % | 105.3 px | 0.44 | 0.94 | 28 |
| stroke 18 | 40 % → 31 % | 136.8 px | 0.44 | 0.77 | 14 |
| stroke 19 | 7 % → 2 % | 32.8 px | 0.40 | 0.31 | 6 |
| stroke 20 | 35 % → 28 % | 97.1 px | 0.44 | 0.79 | 24 |
| stroke 21 | 10 % → 0 % | 43.3 px | 0.25 | 0.00 | 11 |
| stroke 22 | 32 % → 25 % | 74.9 px | 0.44 | 0.79 | 33 |
| stroke 23 | 14 % → 0 % | 46.4 px | 0.00 | 0.00 | 18 |
| stroke 24 | 25 % → 21 % | 82.9 px | 0.44 | 0.85 | 20 |
| stroke 25 | 16 % → 0 % | 31.4 px | 0.00 | 0.00 | 50 |
| stroke 26 | 21 % → 0 % | 39.0 px | 0.00 | 0.00 | 53 |
| stroke 27 | 19 % → 1 % | 45.8 px | 0.45 | 0.03 | 31 |
| stroke 28 | 19 % → 7 % | 46.0 px | 0.44 | 0.37 | 19 |
| stroke 29 | 5 % → 1 % | 17.2 px | 0.46 | 0.18 | 11 |
| stroke 30 | 4 % → 17 % | 17.5 px | 0.43 | 4.31 | 10 |
| stroke 31 | 8 % → 18 % | 20.2 px | 0.43 | 2.38 | 31 |
| stroke 32 | 12 % → 18 % | 29.9 px | 0.43 | 1.56 | 26 |
| stroke 33 | 16 % → 24 % | 71.1 px | 0.43 | 1.52 | 13 |
| stroke 34 | 31 % → 0 % | 146.2 px | 0.46 | 0.01 | 12 |
| stroke 35 | 36 % → 0 % | 127.9 px | 0.00 | 0.00 | 20 |
| stroke 36 | 39 % → 0 % | 185.2 px | 0.00 | 0.00 | 7 |
| stroke 37 | 5 % → 10 % | 20.7 px | 0.44 | 2.25 | 8 |
| stroke 38 | 12 % → 10 % | 41.4 px | 0.44 | 0.84 | 14 |
| stroke 39 | 18 % → 11 % | 62.8 px | 0.43 | 0.62 | 13 |
| stroke 40 | 25 % → 13 % | 119.5 px | 0.43 | 0.54 | 7 |
| stroke 41 | 31 % → 17 % | 118.4 px | 0.43 | 0.54 | 8 |
| stroke 42 | 6 % → 12 % | 18.7 px | 0.42 | 1.85 | 24 |
| stroke 43 | 12 % → 13 % | 33.3 px | 0.43 | 1.10 | 28 |
| stroke 44 | 21 % → 14 % | 73.9 px | 0.43 | 0.65 | 27 |
| stroke 45 | 25 % → 10 % | 73.3 px | 0.43 | 0.41 | 24 |
| stroke 46 | 6 % → 13 % | 16.5 px | 0.44 | 2.08 | 15 |
| stroke 47 | 12 % → 14 % | 31.7 px | 0.44 | 1.21 | 22 |
| stroke 48 | 15 % → 18 % | 71.4 px | 0.44 | 1.25 | 6 |
| stroke 49 | 4 % → 10 % | 17.9 px | 0.40 | 2.67 | 8 |
| stroke 50 | 8 % → 11 % | 28.8 px | 0.40 | 1.30 | 20 |
| stroke 51 | 6 % → 24 % | 22.3 px | 0.40 | 3.71 | 9 |
| stroke 52 | 10 % → 25 % | 50.4 px | 0.41 | 2.40 | 8 |
| stroke 53 | 8 % → 0 % | 11.7 px | 0.00 | 0.00 | 15 |
| stroke 54 | 13 % → 0 % | 13.3 px | 0.00 | 0.00 | 32 |
| stroke 55 | 2 % → 0 % | 7.9 px | 0.00 | 0.00 | 7 |
| stroke 56 | 9 % → 0 % | 29.3 px | 0.00 | 0.00 | 18 |
| stroke 57 | 6 % → 20 % | 11.6 px | 0.43 | 3.38 | 29 |
| stroke 58 | 5 % → 0 % | 19.1 px | 0.00 | 0.00 | 7 |
| stroke 59 | 8 % → 0 % | 17.9 px | 0.00 | 0.00 | 13 |
| stroke 60 | 9 % → 22 % | 27.0 px | 0.43 | 2.41 | 24 |
| stroke 61 | 14 % → 22 % | 32.4 px | 0.43 | 1.65 | 13 |
| stroke 62 | 12 % → 16 % | 25.1 px | 0.43 | 1.27 | 16 |
| stroke 63 | 29 % → 19 % | 65.0 px | 0.43 | 0.66 | 18 |
| stroke 64 | 7 % → 6 % | 12.6 px | 0.39 | 0.93 | 71 |
| stroke 65 | 5 % → 15 % | 11.0 px | 0.43 | 3.08 | 15 |
| stroke 66 | 7 % → 15 % | 12.8 px | 0.42 | 2.28 | 17 |
| stroke 67 | 10 % → 8 % | 23.2 px | 0.42 | 0.81 | 9 |
| stroke 68 | 11 % → 10 % | 30.8 px | 0.43 | 0.93 | 18 |
| stroke 69 | 7 % → 18 % | 13.6 px | 0.39 | 2.55 | 20 |
| stroke 70 | 4 % → 9 % | 9.4 px | 0.44 | 2.33 | 15 |
| stroke 71 | 6 % → 6 % | 9.5 px | 0.45 | 1.08 | 38 |
| stroke 72 | 8 % → 0 % | 15.8 px | 0.00 | 0.00 | 18 |
| stroke 73 | 24 % → 16 % | 36.7 px | 0.40 | 0.66 | 131 |
| stroke 74 | 33 % → 16 % | 77.1 px | 0.41 | 0.48 | 74 |
| stroke 75 | 12 % → 11 % | 40.1 px | 0.43 | 0.90 | 34 |
| stroke 76 | 27 % → 8 % | 47.0 px | 0.43 | 0.29 | 122 |
| stroke 77 | 36 % → 17 % | 52.6 px | 0.43 | 0.48 | 148 |
| stroke 78 | 38 % → 2 % | 53.8 px | 0.43 | 0.05 | 204 |
| stroke 79 | 20 % → 9 % | 36.6 px | 0.39 | 0.46 | 98 |
| stroke 80 | 31 % → 18 % | 100.7 px | 0.44 | 0.57 | 30 |
| stroke 81 | 39 % → 2 % | 67.9 px | 0.41 | 0.05 | 122 |
| stroke 82 | 23 % → 12 % | 77.3 px | 0.43 | 0.53 | 35 |
| stroke 83 | 35 % → 10 % | 46.8 px | 0.43 | 0.29 | 268 |
| stroke 84 | 31 % → 18 % | 83.4 px | 0.43 | 0.60 | 41 |
| stroke 85 | 43 % → 4 % | 64.2 px | 0.41 | 0.10 | 229 |
| stroke 86 | 45 % → 8 % | 60.5 px | 0.42 | 0.17 | 301 |
| stroke 87 | 29 % → 18 % | 96.5 px | 0.43 | 0.63 | 48 |
| stroke 88 | 49 % → 3 % | 73.5 px | 0.36 | 0.07 | 183 |
| stroke 89 | 45 % → 4 % | 53.5 px | 0.42 | 0.10 | 399 |
| stroke 90 | 61 % → 5 % | 65.1 px | 0.41 | 0.09 | 624 |
| stroke 91 | 49 % → 7 % | 136.0 px | 0.43 | 0.15 | 59 |
| stroke 92 | 62 % → 3 % | 76.3 px | 0.43 | 0.05 | 294 |
| stroke 93 | 65 % → 6 % | 136.3 px | 0.44 | 0.09 | 90 |
| stroke 94 | 43 % → 15 % | 101.3 px | 0.41 | 0.34 | 62 |
| stroke 95 | 61 % → 6 % | 91.5 px | 0.44 | 0.10 | 194 |
| stroke 96 | 64 % → 8 % | 84.7 px | 0.41 | 0.13 | 254 |
| stroke 97 | 54 % → 10 % | 92.6 px | 0.44 | 0.18 | 147 |
| stroke 98 | 60 % → 0 % | 160.8 px | 0.00 | 0.00 | 57 |
| stroke 99 | 60 % → 10 % | 99.7 px | 0.42 | 0.17 | 167 |
| stroke 100 | 57 % → 11 % | 62.7 px | 0.43 | 0.19 | 493 |
| stroke 101 | 55 % → 12 % | 58.7 px | 0.43 | 0.22 | 626 |
| stroke 102 | 28 % → 18 % | 63.0 px | 0.42 | 0.65 | 63 |
| stroke 103 | 57 % → 14 % | 60.5 px | 0.43 | 0.25 | 606 |
| stroke 104 | 34 % → 17 % | 113.3 px | 0.42 | 0.50 | 36 |
| stroke 105 | 13 % → 6 % | 42.7 px | 0.41 | 0.47 | 29 |
| stroke 106 | 49 % → 26 % | 75.3 px | 0.44 | 0.54 | 166 |
| stroke 107 | 60 % → 5 % | 75.0 px | 0.39 | 0.09 | 338 |
| stroke 108 | 20 % → 2 % | 68.6 px | 0.36 | 0.11 | 34 |
| stroke 109 | 49 % → 22 % | 72.1 px | 0.44 | 0.46 | 172 |
| stroke 110 | 57 % → 7 % | 78.0 px | 0.37 | 0.13 | 280 |
| stroke 111 | 30 % → 0 % | 69.0 px | 0.17 | 0.00 | 70 |
| stroke 112 | 42 % → 18 % | 71.8 px | 0.45 | 0.42 | 186 |
| stroke 113 | 54 % → 5 % | 74.1 px | 0.40 | 0.10 | 271 |
| stroke 114 | 27 % → 15 % | 89.5 px | 0.37 | 0.58 | 27 |
| stroke 115 | 33 % → 0 % | 59.2 px | 0.00 | 0.00 | 140 |
| stroke 116 | 46 % → 17 % | 62.9 px | 0.45 | 0.36 | 245 |
| stroke 117 | 41 % → 5 % | 107.7 px | 0.42 | 0.11 | 55 |
| stroke 118 | 60 % → 1 % | 124.1 px | 0.40 | 0.02 | 107 |
| stroke 119 | 52 % → 7 % | 54.2 px | 0.45 | 0.14 | 654 |
| stroke 120 | 58 % → 7 % | 67.9 px | 0.44 | 0.13 | 358 |
| stroke 121 | 59 % → 12 % | 101.4 px | 0.45 | 0.20 | 117 |
| stroke 122 | 21 % → 10 % | 46.5 px | 0.38 | 0.46 | 106 |
| stroke 123 | 64 % → 4 % | 70.8 px | 0.44 | 0.07 | 463 |
| stroke 124 | 58 % → 3 % | 64.3 px | 0.43 | 0.05 | 566 |
| stroke 125 | 49 % → 0 % | 77.0 px | 0.48 | 0.01 | 193 |
| stroke 126 | 60 % → 4 % | 70.9 px | 0.43 | 0.07 | 347 |
| stroke 127 | 56 % → 6 % | 59.3 px | 0.43 | 0.10 | 675 |
| stroke 128 | 33 % → 0 % | 110.7 px | 0.00 | 0.00 | 38 |
| stroke 129 | 65 % → 10 % | 82.4 px | 0.43 | 0.15 | 325 |
| stroke 130 | 56 % → 9 % | 87.0 px | 0.42 | 0.16 | 213 |
| stroke 131 | 62 % → 12 % | 118.2 px | 0.43 | 0.19 | 150 |
| stroke 132 | 42 % → 8 % | 72.3 px | 0.42 | 0.20 | 159 |
| stroke 133 | 50 % → 13 % | 170.8 px | 0.43 | 0.26 | 49 |
| stroke 134 | 44 % → 9 % | 88.7 px | 0.42 | 0.21 | 112 |
| stroke 135 | 24 % → 0 % | 83.4 px | 0.00 | 0.00 | 52 |
| stroke 136 | 41 % → 10 % | 131.3 px | 0.44 | 0.24 | 40 |
| stroke 137 | 40 % → 8 % | 70.1 px | 0.42 | 0.20 | 235 |
| stroke 138 | 44 % → 8 % | 119.7 px | 0.42 | 0.19 | 111 |
| stroke 139 | 28 % → 9 % | 65.1 px | 0.43 | 0.32 | 128 |
| stroke 140 | 23 % → 13 % | 51.5 px | 0.43 | 0.55 | 196 |
| stroke 141 | 44 % → 3 % | 75.7 px | 0.43 | 0.06 | 291 |
| stroke 142 | 32 % → 0 % | 86.8 px | 0.00 | 0.00 | 115 |
| stroke 143 | 47 % → 12 % | 96.5 px | 0.44 | 0.25 | 232 |
| stroke 144 | 47 % → 2 % | 96.7 px | 0.43 | 0.04 | 191 |
| stroke 145 | 24 % → 0 % | 77.4 px | 0.00 | 0.00 | 63 |
| stroke 146 | 38 % → 2 % | 100.1 px | 0.45 | 0.04 | 190 |
| stroke 147 | 40 % → 0 % | 80.6 px | 0.00 | 0.00 | 164 |
| stroke 148 | 39 % → 0 % | 130.3 px | 0.00 | 0.00 | 104 |
| stroke 149 | 49 % → 16 % | 85.3 px | 0.44 | 0.33 | 263 |
| stroke 150 | 49 % → 9 % | 113.3 px | 0.44 | 0.19 | 208 |
| stroke 151 | 54 % → 9 % | 59.3 px | 0.44 | 0.16 | 1322 |
| stroke 152 | 59 % → 11 % | 135.8 px | 0.44 | 0.19 | 99 |
| stroke 153 | 62 % → 23 % | 143.8 px | 0.44 | 0.37 | 160 |
| stroke 154 | 58 % → 13 % | 200.0 px | 0.44 | 0.23 | 40 |
| stroke 155 | 20 % → 2 % | 36.9 px | 0.39 | 0.08 | 364 |
| stroke 156 | 24 % → 3 % | 43.5 px | 0.41 | 0.14 | 649 |
| stroke 157 | 39 % → 4 % | 69.9 px | 0.41 | 0.11 | 640 |
| stroke 158 | 35 % → 0 % | 75.1 px | 0.38 | 0.01 | 261 |
| stroke 159 | 34 % → 0 % | 122.1 px | 0.00 | 0.00 | 49 |
| stroke 160 | 41 % → 3 % | 74.1 px | 0.41 | 0.07 | 1696 |
| stroke 161 | 34 % → 0 % | 120.9 px | 0.00 | 0.00 | 53 |
| stroke 162 | 44 % → 3 % | 83.1 px | 0.42 | 0.07 | 848 |
| stroke 163 | 40 % → 0 % | 146.8 px | 0.00 | 0.00 | 79 |
| stroke 164 | 63 % → 9 % | 134.0 px | 0.42 | 0.15 | 158 |
| stroke 165 | 55 % → 5 % | 105.3 px | 0.41 | 0.09 | 219 |
| stroke 166 | 41 % → 8 % | 144.2 px | 0.42 | 0.19 | 40 |
| stroke 167 | 53 % → 11 % | 158.1 px | 0.42 | 0.22 | 51 |
| stroke 168 | 60 % → 9 % | 211.7 px | 0.41 | 0.16 | 29 |
| stroke 169 | 62 % → 0 % | 225.2 px | 0.00 | 0.00 | 58 |
| stroke 170 | 49 % → 6 % | 117.8 px | 0.42 | 0.13 | 97 |
| stroke 171 | 42 % → 7 % | 109.5 px | 0.42 | 0.16 | 69 |
| stroke 172 | 43 % → 0 % | 149.9 px | 0.00 | 0.00 | 47 |
| stroke 173 | 39 % → 7 % | 103.1 px | 0.42 | 0.17 | 73 |
| stroke 174 | 27 % → 8 % | 79.4 px | 0.44 | 0.30 | 53 |
| stroke 175 | 32 % → 0 % | 115.2 px | 0.00 | 0.00 | 36 |
| stroke 176 | 42 % → 5 % | 125.8 px | 0.42 | 0.12 | 61 |
| stroke 177 | 44 % → 7 % | 79.7 px | 0.43 | 0.17 | 286 |
| stroke 178 | 43 % → 2 % | 95.6 px | 0.42 | 0.05 | 105 |
| stroke 179 | 37 % → 18 % | 87.0 px | 0.43 | 0.50 | 94 |
| stroke 180 | 50 % → 6 % | 179.9 px | 0.44 | 0.12 | 43 |
| stroke 181 | 49 % → 2 % | 89.1 px | 0.44 | 0.04 | 278 |
| stroke 182 | 53 % → 21 % | 122.5 px | 0.43 | 0.39 | 122 |
| stroke 183 | 50 % → 2 % | 89.8 px | 0.44 | 0.03 | 303 |
| stroke 184 | 67 % → 20 % | 246.9 px | 0.43 | 0.29 | 54 |
| stroke 185 | 54 % → 0 % | 162.9 px | 0.00 | 0.00 | 74 |
| stroke 186 | 56 % → 3 % | 111.6 px | 0.44 | 0.05 | 157 |
| stroke 187 | 60 % → 2 % | 107.9 px | 0.43 | 0.04 | 298 |
| stroke 188 | 67 % → 1 % | 134.4 px | 0.46 | 0.01 | 230 |
| stroke 189 | 59 % → 5 % | 212.4 px | 0.43 | 0.08 | 34 |
| stroke 190 | 66 % → 3 % | 133.5 px | 0.42 | 0.05 | 154 |
| stroke 191 | 6 % → 42 % | 23.9 px | 0.41 | 6.50 | 10 |
| stroke 192 | 6 % → 9 % | 13.8 px | 0.45 | 1.66 | 14 |
| stroke 193 | 17 % → 15 % | 36.2 px | 0.43 | 0.89 | 40 |
| stroke 194 | 24 % → 13 % | 43.2 px | 0.42 | 0.54 | 35 |
| stroke 195 | 13 % → 2 % | 44.3 px | 0.38 | 0.19 | 20 |
| stroke 196 | 8 % → 0 % | 17.8 px | 0.00 | 0.00 | 32 |
| stroke 197 | 12 % → 0 % | 35.0 px | 0.00 | 0.00 | 16 |
| stroke 198 | 15 % → 0 % | 33.0 px | 0.00 | 0.00 | 49 |
| stroke 199 | 21 % → 0 % | 100.3 px | 0.00 | 0.00 | 15 |
| stroke 200 | 24 % → 0 % | 65.6 px | 0.00 | 0.00 | 35 |
| stroke 201 | 29 % → 0 % | 101.9 px | 0.00 | 0.00 | 27 |
| stroke 202 | 30 % → 0 % | 131.5 px | 0.00 | 0.00 | 16 |
| stroke 203 | 5 % → 18 % | 19.4 px | 0.43 | 3.37 | 14 |
| stroke 204 | 5 % → 21 % | 19.1 px | 0.43 | 4.11 | 21 |
| stroke 205 | 8 % → 14 % | 41.0 px | 0.43 | 1.62 | 14 |
| stroke 206 | 7 % → 21 % | 32.8 px | 0.43 | 3.06 | 16 |
| stroke 207 | 13 % → 9 % | 46.0 px | 0.43 | 0.74 | 21 |
| stroke 208 | 18 % → 7 % | 47.6 px | 0.43 | 0.37 | 36 |
| stroke 209 | 11 % → 0 % | 50.7 px | 0.00 | 0.00 | 14 |
| stroke 210 | 22 % → 2 % | 64.3 px | 0.45 | 0.08 | 27 |
| stroke 211 | 17 % → 0 % | 82.9 px | 0.00 | 0.00 | 11 |
| stroke 212 | 29 % → 2 % | 105.1 px | 0.44 | 0.06 | 20 |
| stroke 213 | 25 % → 0 % | 93.0 px | 0.00 | 0.00 | 31 |
| stroke 214 | 28 % → 1 % | 71.3 px | 0.45 | 0.02 | 38 |
| stroke 215 | 34 % → 0 % | 169.9 px | 0.00 | 0.00 | 15 |
| stroke 216 | 34 % → 0 % | 160.7 px | 0.00 | 0.00 | 11 |
| stroke 217 | 32 % → 0 % | 96.2 px | 0.00 | 0.00 | 21 |
| stroke 218 | 4 % → 12 % | 18.1 px | 0.42 | 3.34 | 8 |
| stroke 219 | 9 % → 21 % | 42.9 px | 0.43 | 2.30 | 14 |
| stroke 220 | 12 % → 5 % | 33.5 px | 0.42 | 0.44 | 26 |
| stroke 221 | 15 % → 0 % | 71.3 px | 0.38 | 0.03 | 12 |
| stroke 222 | 25 % → 9 % | 113.3 px | 0.43 | 0.38 | 6 |
| stroke 223 | 18 % → 1 % | 89.0 px | 0.45 | 0.06 | 11 |
| stroke 224 | 24 % → 4 % | 80.2 px | 0.42 | 0.17 | 24 |
| stroke 225 | 5 % → 1 % | 23.5 px | 0.42 | 0.10 | 14 |
| stroke 226 | 9 % → 1 % | 32.9 px | 0.47 | 0.07 | 22 |
| stroke 227 | 14 % → 4 % | 33.2 px | 0.44 | 0.27 | 42 |
| stroke 228 | 19 % → 6 % | 90.4 px | 0.43 | 0.29 | 8 |
| stroke 229 | 16 % → 9 % | 35.1 px | 0.44 | 0.56 | 48 |
| stroke 230 | 19 % → 10 % | 42.4 px | 0.43 | 0.53 | 52 |
| stroke 231 | 24 % → 5 % | 57.7 px | 0.45 | 0.19 | 43 |
| stroke 232 | 32 % → 13 % | 58.9 px | 0.44 | 0.42 | 103 |
| stroke 233 | 31 % → 7 % | 87.0 px | 0.44 | 0.23 | 32 |
| stroke 234 | 34 % → 17 % | 82.4 px | 0.44 | 0.49 | 67 |
| stroke 235 | 32 % → 10 % | 148.3 px | 0.44 | 0.32 | 21 |
| stroke 236 | 32 % → 14 % | 158.3 px | 0.44 | 0.42 | 9 |
| stroke 237 | 33 % → 15 % | 150.8 px | 0.44 | 0.45 | 16 |
| stroke 238 | 26 % → 0 % | 110.8 px | 0.00 | 0.00 | 14 |
| stroke 239 | 33 % → 0 % | 114.0 px | 0.00 | 0.00 | 19 |
| stroke 240 | 33 % → 0 % | 82.7 px | 0.00 | 0.00 | 42 |
| stroke 241 | 25 % → 0 % | 115.5 px | 0.00 | 0.00 | 8 |
| stroke 242 | 30 % → 1 % | 65.4 px | 0.46 | 0.03 | 47 |
| stroke 243 | 30 % → 3 % | 150.5 px | 0.45 | 0.10 | 12 |
| stroke 244 | 6 % → 0 % | 20.5 px | 0.00 | 0.00 | 22 |
| stroke 245 | 11 % → 1 % | 48.2 px | 0.42 | 0.10 | 8 |
| stroke 246 | 15 % → 4 % | 40.3 px | 0.42 | 0.25 | 33 |
| stroke 247 | 21 % → 5 % | 103.8 px | 0.40 | 0.24 | 9 |
| stroke 248 | 23 % → 7 % | 109.3 px | 0.41 | 0.32 | 11 |
| stroke 249 | 14 % → 0 % | 68.2 px | 0.55 | 0.00 | 13 |
| stroke 250 | 9 % → 0 % | 43.9 px | 0.55 | 0.00 | 7 |
| stroke 251 | 13 % → 2 % | 46.2 px | 0.45 | 0.15 | 17 |
| stroke 252 | 19 % → 8 % | 48.0 px | 0.43 | 0.39 | 50 |
| stroke 253 | 5 % → 0 % | 18.0 px | 0.00 | 0.00 | 21 |
| stroke 254 | 15 % → 0 % | 46.7 px | 0.00 | 0.00 | 30 |
| stroke 255 | 10 % → 1 % | 49.6 px | 0.34 | 0.08 | 11 |
| stroke 256 | 20 % → 0 % | 53.5 px | 0.00 | 0.00 | 35 |
| stroke 257 | 29 % → 3 % | 70.1 px | 0.44 | 0.09 | 40 |
| stroke 258 | 31 % → 10 % | 65.6 px | 0.43 | 0.32 | 80 |
| stroke 259 | 30 % → 4 % | 60.8 px | 0.43 | 0.14 | 100 |
| stroke 260 | 35 % → 3 % | 85.9 px | 0.43 | 0.07 | 68 |
| stroke 261 | 10 % → 7 % | 35.8 px | 0.44 | 0.71 | 18 |
| stroke 262 | 16 % → 6 % | 47.6 px | 0.44 | 0.40 | 21 |
| stroke 263 | 20 % → 5 % | 44.4 px | 0.43 | 0.24 | 64 |
| stroke 264 | 30 % → 3 % | 81.8 px | 0.44 | 0.10 | 30 |
| stroke 265 | 43 % → 0 % | 158.6 px | 0.39 | 0.00 | 20 |
| stroke 266 | 3 % → 14 % | 17.3 px | 0.42 | 4.19 | 6 |
| stroke 267 | 11 % → 8 % | 19.7 px | 0.42 | 0.78 | 94 |
| stroke 268 | 19 % → 4 % | 64.3 px | 0.42 | 0.22 | 21 |
| stroke 269 | 21 % → 2 % | 74.3 px | 0.42 | 0.12 | 13 |
| stroke 270 | 21 % → 1 % | 104.6 px | 0.44 | 0.03 | 13 |
| stroke 271 | 8 % → 20 % | 18.8 px | 0.40 | 2.40 | 52 |
| stroke 272 | 14 % → 21 % | 35.8 px | 0.41 | 1.54 | 34 |
| stroke 273 | 20 % → 16 % | 98.9 px | 0.42 | 0.81 | 7 |
| stroke 274 | 18 % → 0 % | 64.9 px | 0.00 | 0.00 | 16 |
| stroke 275 | 15 % → 0 % | 54.5 px | 0.00 | 0.00 | 19 |
| stroke 276 | 4 % → 18 % | 22.5 px | 0.40 | 3.94 | 12 |
| stroke 277 | 9 % → 24 % | 33.5 px | 0.40 | 2.55 | 33 |
| stroke 278 | 13 % → 21 % | 38.6 px | 0.40 | 1.62 | 29 |
| stroke 279 | 16 % → 18 % | 59.1 px | 0.39 | 1.10 | 20 |
| stroke 280 | 6 % → 5 % | 19.4 px | 0.41 | 0.88 | 21 |
| stroke 281 | 12 % → 10 % | 29.1 px | 0.40 | 0.81 | 39 |
| stroke 282 | 9 % → 15 % | 20.5 px | 0.43 | 1.78 | 31 |
| stroke 283 | 16 % → 8 % | 45.2 px | 0.39 | 0.50 | 58 |
| stroke 284 | 15 % → 13 % | 30.0 px | 0.43 | 0.86 | 49 |
| stroke 285 | 28 % → 11 % | 135.4 px | 0.44 | 0.40 | 12 |
| stroke 286 | 31 % → 3 % | 145.5 px | 0.46 | 0.09 | 21 |
| stroke 287 | 32 % → 1 % | 151.5 px | 0.38 | 0.02 | 17 |
| stroke 288 | 19 % → 12 % | 71.2 px | 0.40 | 0.61 | 11 |
| stroke 289 | 23 % → 10 % | 59.2 px | 0.40 | 0.46 | 38 |
| stroke 290 | 26 % → 4 % | 125.9 px | 0.35 | 0.16 | 13 |
| stroke 291 | 12 % → 16 % | 17.3 px | 0.43 | 1.33 | 69 |
| stroke 292 | 8 % → 15 % | 14.0 px | 0.43 | 1.92 | 39 |
| stroke 293 | 8 % → 14 % | 27.4 px | 0.43 | 1.80 | 7 |
| stroke 294 | 17 % → 19 % | 63.5 px | 0.43 | 1.15 | 15 |
| stroke 295 | 11 % → 12 % | 32.7 px | 0.41 | 1.02 | 39 |
| stroke 296 | 7 % → 13 % | 17.8 px | 0.44 | 1.90 | 20 |
| stroke 297 | 9 % → 19 % | 18.8 px | 0.43 | 2.22 | 28 |
| stroke 298 | 8 % → 18 % | 29.8 px | 0.43 | 2.17 | 9 |
| stroke 299 | 18 % → 20 % | 46.2 px | 0.43 | 1.12 | 12 |
| stroke 300 | 8 % → 9 % | 23.5 px | 0.44 | 1.20 | 20 |
| stroke 301 | 12 % → 25 % | 31.4 px | 0.44 | 2.12 | 11 |
| stroke 302 | 13 % → 16 % | 26.3 px | 0.44 | 1.22 | 34 |
| stroke 303 | 7 % → 8 % | 27.6 px | 0.43 | 1.09 | 20 |
| stroke 304 | 7 % → 14 % | 22.9 px | 0.45 | 1.96 | 19 |
| stroke 305 | 10 % → 22 % | 19.7 px | 0.42 | 2.19 | 112 |
| stroke 306 | 25 % → 28 % | 25.5 px | 0.41 | 1.13 | 96 |
| stroke 307 | 5 % → 6 % | 12.7 px | 0.42 | 1.32 | 17 |
| stroke 308 | 8 % → 9 % | 20.2 px | 0.42 | 1.15 | 37 |
| stroke 309 | 3 % → 5 % | 12.8 px | 0.44 | 1.32 | 6 |
| stroke 310 | 9 % → 15 % | 33.0 px | 0.44 | 1.60 | 13 |
| stroke 311 | 5 % → 8 % | 14.5 px | 0.43 | 1.73 | 11 |
| stroke 312 | 5 % → 12 % | 14.5 px | 0.42 | 2.53 | 14 |
| stroke 313 | 12 % → 16 % | 41.6 px | 0.43 | 1.27 | 15 |
| stroke 314 | 5 % → 16 % | 14.9 px | 0.42 | 3.53 | 18 |
| stroke 315 | 8 % → 17 % | 25.6 px | 0.42 | 2.19 | 9 |
| stroke 316 | 11 % → 14 % | 33.1 px | 0.42 | 1.24 | 22 |
| stroke 317 | 9 % → 17 % | 18.6 px | 0.39 | 1.77 | 34 |
| stroke 318 | 8 % → 11 % | 21.1 px | 0.39 | 1.25 | 13 |
| stroke 319 | 9 % → 10 % | 18.1 px | 0.37 | 1.15 | 53 |
| stroke 320 | 6 % → 12 % | 12.9 px | 0.41 | 1.87 | 31 |
| stroke 321 | 14 % → 19 % | 32.9 px | 0.42 | 1.41 | 45 |
| stroke 322 | 21 % → 24 % | 61.3 px | 0.42 | 1.15 | 9 |
| stroke 323 | 5 % → 17 % | 15.0 px | 0.43 | 3.86 | 11 |
| stroke 324 | 15 % → 16 % | 40.4 px | 0.43 | 1.12 | 30 |

Numbers say: wet paint spreads well beyond the stroke.

## Refs v3 · #18 Twombly blue sticks — own sheet
own sheet 800 × 789 · Wax 1.00 · 19 px · 73.5 s

![Refs v3 · #18 Twombly blue sticks — own sheet](Refs-v3-18-Twombly-blue-sticks-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 3 % → 27 % | 19.2 px | 0.35 | 8.18 | 24 |
| stroke 2 | 5 % → 8 % | 32.3 px | 0.35 | 1.49 | 8 |
| stroke 3 | 5 % → 21 % | 14.8 px | 0.35 | 3.92 | 24 |
| stroke 4 | 11 % → 6 % | 24.6 px | 0.34 | 0.57 | 28 |
| stroke 5 | 9 % → 13 % | 36.2 px | 0.35 | 1.48 | 13 |
| stroke 6 | 11 % → 14 % | 68.3 px | 0.35 | 1.25 | 10 |
| stroke 7 | 13 % → 22 % | 43.3 px | 0.35 | 1.66 | 20 |
| stroke 8 | 17 % → 10 % | 71.1 px | 0.35 | 0.59 | 11 |
| stroke 9 | 10 % → 33 % | 41.0 px | 0.35 | 3.30 | 13 |
| stroke 10 | 13 % → 40 % | 78.4 px | 0.35 | 2.98 | 12 |
| stroke 11 | 17 % → 40 % | 48.1 px | 0.35 | 2.38 | 24 |
| stroke 12 | 16 % → 30 % | 27.7 px | 0.35 | 1.92 | 54 |
| stroke 13 | 4 % → 0 % | 17.2 px | 0.00 | 0.00 | 10 |
| stroke 14 | 24 % → 31 % | 131.5 px | 0.35 | 1.30 | 9 |
| stroke 15 | 19 % → 15 % | 83.5 px | 0.35 | 0.80 | 17 |
| stroke 16 | 18 % → 46 % | 99.9 px | 0.35 | 2.58 | 6 |
| stroke 17 | 28 % → 18 % | 117.9 px | 0.35 | 0.65 | 9 |
| stroke 18 | 8 % → 0 % | 28.6 px | 0.00 | 0.00 | 16 |
| stroke 19 | 4 % → 0 % | 21.9 px | 0.00 | 0.00 | 10 |
| stroke 20 | 20 % → 22 % | 46.7 px | 0.35 | 1.09 | 29 |
| stroke 21 | 17 % → 0 % | 48.6 px | 0.30 | 0.00 | 24 |
| stroke 22 | 8 % → 0 % | 21.0 px | 0.00 | 0.00 | 27 |
| stroke 23 | 11 % → 36 % | 64.5 px | 0.35 | 3.23 | 14 |
| stroke 24 | 24 % → 19 % | 139.4 px | 0.35 | 0.80 | 7 |
| stroke 25 | 27 % → 4 % | 108.7 px | 0.35 | 0.16 | 14 |
| stroke 26 | 13 % → 0 % | 79.5 px | 0.00 | 0.00 | 11 |
| stroke 27 | 14 % → 1 % | 36.6 px | 0.33 | 0.05 | 24 |
| stroke 28 | 22 % → 18 % | 61.8 px | 0.35 | 0.81 | 21 |
| stroke 29 | 9 % → 4 % | 30.9 px | 0.35 | 0.43 | 15 |
| stroke 30 | 14 % → 0 % | 44.2 px | 0.00 | 0.00 | 26 |
| stroke 31 | 8 % → 0 % | 42.7 px | 0.00 | 0.00 | 13 |
| stroke 32 | 16 % → 0 % | 35.1 px | 0.00 | 0.00 | 47 |
| stroke 33 | 7 % → 0 % | 40.5 px | 0.00 | 0.00 | 12 |
| stroke 34 | 18 % → 5 % | 33.6 px | 0.35 | 0.30 | 64 |
| stroke 35 | 18 % → 0 % | 61.3 px | 0.00 | 0.00 | 23 |
| stroke 36 | 10 % → 0 % | 47.7 px | 0.00 | 0.00 | 13 |
| stroke 37 | 24 % → 6 % | 50.5 px | 0.35 | 0.27 | 50 |
| stroke 38 | 24 % → 0 % | 138.0 px | 0.00 | 0.00 | 10 |
| stroke 39 | 17 % → 0 % | 97.9 px | 0.00 | 0.00 | 12 |
| stroke 40 | 11 % → 0 % | 53.7 px | 0.00 | 0.00 | 16 |
| stroke 41 | 21 % → 6 % | 44.2 px | 0.35 | 0.31 | 50 |
| stroke 42 | 34 % → 0 % | 139.0 px | 0.00 | 0.00 | 16 |
| stroke 43 | 23 % → 0 % | 53.2 px | 0.00 | 0.00 | 41 |
| stroke 44 | 11 % → 0 % | 61.6 px | 0.00 | 0.00 | 13 |
| stroke 45 | 27 % → 0 % | 153.3 px | 0.34 | 0.02 | 9 |
| stroke 46 | 18 % → 0 % | 100.4 px | 0.00 | 0.00 | 11 |
| stroke 47 | 11 % → 1 % | 56.8 px | 0.33 | 0.10 | 11 |
| stroke 48 | 17 % → 2 % | 37.0 px | 0.34 | 0.11 | 45 |
| stroke 49 | 22 % → 0 % | 69.9 px | 0.00 | 0.00 | 21 |
| stroke 50 | 10 % → 8 % | 58.6 px | 0.35 | 0.75 | 7 |
| stroke 51 | 3 % → 0 % | 17.9 px | 0.00 | 0.00 | 8 |
| stroke 52 | 14 % → 0 % | 31.0 px | 0.00 | 0.00 | 39 |
| stroke 53 | 11 % → 6 % | 15.2 px | 0.35 | 0.53 | 127 |
| stroke 54 | 14 % → 9 % | 24.9 px | 0.35 | 0.63 | 60 |
| stroke 55 | 10 % → 0 % | 24.7 px | 0.00 | 0.00 | 29 |
| stroke 56 | 17 % → 0 % | 41.7 px | 0.00 | 0.00 | 36 |
| stroke 57 | 21 % → 5 % | 27.9 px | 0.35 | 0.24 | 247 |
| stroke 58 | 21 % → 10 % | 53.0 px | 0.35 | 0.48 | 24 |
| stroke 59 | 23 % → 3 % | 32.4 px | 0.35 | 0.12 | 388 |
| stroke 60 | 30 % → 3 % | 41.9 px | 0.35 | 0.09 | 441 |
| stroke 61 | 39 % → 2 % | 52.3 px | 0.35 | 0.04 | 296 |
| stroke 62 | 39 % → 0 % | 52.1 px | 0.00 | 0.00 | 167 |
| stroke 63 | 19 % → 0 % | 11.1 px | 0.00 | 0.00 | 299 |
| stroke 64 | 29 % → 0 % | 37.0 px | 0.00 | 0.00 | 49 |
| stroke 65 | 32 % → 0 % | 144.1 px | 0.00 | 0.00 | 6 |
| stroke 66 | 31 % → 0 % | 21.2 px | 0.00 | 0.00 | 316 |
| stroke 67 | 11 % → 0 % | 20.3 px | 0.00 | 0.00 | 58 |
| stroke 68 | 7 % → 4 % | 22.7 px | 0.35 | 0.58 | 40 |
| stroke 69 | 5 % → 47 % | 22.4 px | 0.35 | 9.71 | 21 |
| stroke 70 | 6 % → 21 % | 26.9 px | 0.35 | 3.58 | 22 |
| stroke 71 | 10 % → 46 % | 27.1 px | 0.35 | 4.82 | 46 |
| stroke 72 | 5 % → 0 % | 22.8 px | 0.00 | 0.00 | 21 |
| stroke 73 | 7 % → 7 % | 29.5 px | 0.35 | 0.96 | 34 |
| stroke 74 | 7 % → 5 % | 24.7 px | 0.35 | 0.80 | 29 |
| stroke 75 | 8 % → 8 % | 21.5 px | 0.35 | 1.04 | 55 |
| stroke 76 | 17 % → 0 % | 79.6 px | 0.00 | 0.00 | 18 |
| stroke 77 | 18 % → 40 % | 56.3 px | 0.35 | 2.17 | 37 |
| stroke 78 | 15 % → 45 % | 40.2 px | 0.35 | 2.90 | 47 |
| stroke 79 | 5 % → 28 % | 19.4 px | 0.35 | 5.29 | 23 |
| stroke 80 | 8 % → 17 % | 39.9 px | 0.35 | 2.04 | 29 |
| stroke 81 | 12 % → 0 % | 50.2 px | 0.00 | 0.00 | 29 |
| stroke 82 | 8 % → 15 % | 26.3 px | 0.35 | 1.83 | 52 |
| stroke 83 | 16 % → 28 % | 72.6 px | 0.35 | 1.78 | 22 |
| stroke 84 | 12 % → 36 % | 32.4 px | 0.35 | 3.07 | 50 |
| stroke 85 | 17 % → 0 % | 67.1 px | 0.00 | 0.00 | 36 |
| stroke 86 | 26 % → 46 % | 100.0 px | 0.35 | 1.78 | 35 |
| stroke 87 | 16 % → 33 % | 72.0 px | 0.35 | 2.03 | 23 |
| stroke 88 | 19 % → 11 % | 59.7 px | 0.35 | 0.57 | 50 |
| stroke 89 | 16 % → 32 % | 52.9 px | 0.35 | 2.04 | 35 |
| stroke 90 | 22 % → 18 % | 103.5 px | 0.35 | 0.80 | 24 |
| stroke 91 | 24 % → 0 % | 67.3 px | 0.00 | 0.00 | 66 |
| stroke 92 | 24 % → 11 % | 54.8 px | 0.35 | 0.46 | 77 |
| stroke 93 | 5 % → 0 % | 21.2 px | 0.00 | 0.00 | 32 |
| stroke 94 | 19 % → 27 % | 53.9 px | 0.35 | 1.42 | 60 |
| stroke 95 | 15 % → 16 % | 51.1 px | 0.35 | 1.05 | 35 |
| stroke 96 | 24 % → 21 % | 101.9 px | 0.35 | 0.87 | 21 |
| stroke 97 | 21 % → 12 % | 94.1 px | 0.35 | 0.57 | 25 |
| stroke 98 | 23 % → 21 % | 68.2 px | 0.35 | 0.90 | 41 |
| stroke 99 | 13 % → 13 % | 58.5 px | 0.35 | 1.01 | 24 |
| stroke 100 | 39 % → 28 % | 183.9 px | 0.35 | 0.71 | 26 |
| stroke 101 | 35 % → 22 % | 149.3 px | 0.35 | 0.65 | 25 |
| stroke 102 | 37 % → 29 % | 139.2 px | 0.35 | 0.78 | 38 |
| stroke 103 | 27 % → 18 % | 92.8 px | 0.35 | 0.66 | 34 |
| stroke 104 | 36 % → 35 % | 94.8 px | 0.35 | 0.97 | 51 |
| stroke 105 | 35 % → 28 % | 133.2 px | 0.35 | 0.79 | 28 |
| stroke 106 | 36 % → 38 % | 138.9 px | 0.35 | 1.05 | 31 |
| stroke 107 | 16 % → 12 % | 70.5 px | 0.35 | 0.76 | 29 |
| stroke 108 | 29 % → 16 % | 130.7 px | 0.35 | 0.56 | 29 |
| stroke 109 | 35 % → 8 % | 151.1 px | 0.35 | 0.22 | 27 |
| stroke 110 | 41 % → 23 % | 122.1 px | 0.35 | 0.55 | 48 |
| stroke 111 | 29 % → 15 % | 102.8 px | 0.35 | 0.51 | 40 |
| stroke 112 | 12 % → 36 % | 42.0 px | 0.35 | 3.05 | 28 |
| stroke 113 | 35 % → 4 % | 156.6 px | 0.34 | 0.11 | 22 |
| stroke 114 | 32 % → 6 % | 80.6 px | 0.35 | 0.19 | 41 |
| stroke 115 | 36 % → 15 % | 168.7 px | 0.35 | 0.43 | 26 |
| stroke 116 | 46 % → 40 % | 213.5 px | 0.35 | 0.87 | 24 |
| stroke 117 | 52 % → 34 % | 184.4 px | 0.35 | 0.65 | 35 |
| stroke 118 | 44 % → 13 % | 190.3 px | 0.35 | 0.29 | 34 |
| stroke 119 | 28 % → 28 % | 110.5 px | 0.35 | 1.00 | 40 |
| stroke 120 | 29 % → 30 % | 92.1 px | 0.35 | 1.02 | 36 |
| stroke 121 | 53 % → 43 % | 210.8 px | 0.35 | 0.82 | 23 |
| stroke 122 | 11 % → 0 % | 18.7 px | 0.00 | 0.00 | 99 |
| stroke 123 | 6 % → 0 % | 23.7 px | 0.00 | 0.00 | 30 |
| stroke 124 | 16 % → 0 % | 53.7 px | 0.00 | 0.00 | 32 |
| stroke 125 | 14 % → 0 % | 38.8 px | 0.00 | 0.00 | 91 |
| stroke 126 | 8 % → 0 % | 25.1 px | 0.00 | 0.00 | 37 |
| stroke 127 | 27 % → 0 % | 98.3 px | 0.00 | 0.00 | 31 |
| stroke 128 | 10 % → 17 % | 19.7 px | 0.35 | 1.76 | 68 |
| stroke 129 | 12 % → 40 % | 15.2 px | 0.35 | 3.46 | 199 |
| stroke 130 | 20 % → 33 % | 51.2 px | 0.35 | 1.67 | 37 |
| stroke 131 | 12 % → 53 % | 42.6 px | 0.35 | 4.42 | 27 |
| stroke 132 | 20 % → 56 % | 84.5 px | 0.35 | 2.80 | 26 |
| stroke 133 | 15 % → 60 % | 69.8 px | 0.35 | 4.04 | 21 |
| stroke 134 | 28 % → 74 % | 117.0 px | 0.35 | 2.69 | 28 |
| stroke 135 | 23 % → 27 % | 51.5 px | 0.35 | 1.16 | 86 |
| stroke 136 | 29 % → 51 % | 123.8 px | 0.35 | 1.79 | 23 |
| stroke 137 | 33 % → 35 % | 147.0 px | 0.35 | 1.04 | 26 |
| stroke 138 | 15 % → 33 % | 49.9 px | 0.35 | 2.23 | 37 |
| stroke 139 | 25 % → 32 % | 116.1 px | 0.35 | 1.29 | 21 |
| stroke 140 | 29 % → 31 % | 76.4 px | 0.35 | 1.06 | 55 |
| stroke 141 | 29 % → 1 % | 119.0 px | 0.34 | 0.03 | 23 |
| stroke 142 | 17 % → 53 % | 76.1 px | 0.35 | 3.20 | 19 |
| stroke 143 | 22 % → 59 % | 85.4 px | 0.35 | 2.70 | 28 |
| stroke 144 | 34 % → 0 % | 85.7 px | 0.00 | 0.00 | 74 |
| stroke 145 | 32 % → 0 % | 95.8 px | 0.00 | 0.00 | 24 |
| stroke 146 | 35 % → 0 % | 130.1 px | 0.33 | 0.00 | 38 |
| stroke 147 | 21 % → 26 % | 90.6 px | 0.35 | 1.24 | 33 |
| stroke 148 | 42 % → 24 % | 110.8 px | 0.35 | 0.56 | 81 |
| stroke 149 | 55 % → 31 % | 252.1 px | 0.35 | 0.56 | 24 |
| stroke 150 | 57 % → 31 % | 196.9 px | 0.35 | 0.55 | 33 |
| stroke 151 | 27 % → 0 % | 77.5 px | 0.00 | 0.00 | 63 |
| stroke 152 | 23 % → 0 % | 49.6 px | 0.00 | 0.00 | 81 |
| stroke 153 | 13 % → 6 % | 31.9 px | 0.35 | 0.46 | 66 |
| stroke 154 | 17 % → 0 % | 61.7 px | 0.30 | 0.01 | 31 |
| stroke 155 | 33 % → 0 % | 124.4 px | 0.35 | 0.00 | 24 |
| stroke 156 | 38 % → 0 % | 96.0 px | 0.00 | 0.00 | 50 |
| stroke 157 | 17 % → 0 % | 46.5 px | 0.00 | 0.00 | 42 |
| stroke 158 | 8 % → 0 % | 29.9 px | 0.00 | 0.00 | 27 |
| stroke 159 | 11 % → 0 % | 42.2 px | 0.00 | 0.00 | 25 |
| stroke 160 | 7 % → 3 % | 19.7 px | 0.35 | 0.40 | 42 |
| stroke 161 | 4 % → 13 % | 12.2 px | 0.35 | 3.21 | 16 |
| stroke 162 | 8 % → 12 % | 22.8 px | 0.35 | 1.42 | 19 |
| stroke 163 | 11 % → 9 % | 43.8 px | 0.35 | 0.81 | 12 |
| stroke 164 | 19 % → 3 % | 107.4 px | 0.35 | 0.17 | 8 |
| stroke 165 | 10 % → 17 % | 56.7 px | 0.35 | 1.74 | 8 |
| stroke 166 | 18 % → 1 % | 66.0 px | 0.35 | 0.04 | 14 |
| stroke 167 | 2 % → 12 % | 14.4 px | 0.35 | 5.39 | 6 |
| stroke 168 | 4 % → 22 % | 12.0 px | 0.35 | 5.19 | 20 |
| stroke 169 | 8 % → 14 % | 22.7 px | 0.35 | 1.65 | 21 |
| stroke 170 | 19 % → 0 % | 85.9 px | 0.00 | 0.00 | 10 |
| stroke 171 | 5 % → 9 % | 22.3 px | 0.35 | 1.78 | 6 |
| stroke 172 | 9 % → 15 % | 41.0 px | 0.35 | 1.66 | 8 |
| stroke 173 | 15 % → 14 % | 42.6 px | 0.35 | 0.92 | 22 |
| stroke 174 | 20 % → 0 % | 95.2 px | 0.00 | 0.00 | 10 |
| stroke 175 | 18 % → 0 % | 81.0 px | 0.00 | 0.00 | 10 |
| stroke 176 | 16 % → 4 % | 47.1 px | 0.35 | 0.27 | 24 |
| stroke 177 | 19 % → 0 % | 45.6 px | 0.35 | 0.01 | 42 |
| stroke 178 | 8 % → 1 % | 25.9 px | 0.35 | 0.12 | 11 |
| stroke 179 | 16 % → 10 % | 37.2 px | 0.35 | 0.65 | 41 |
| stroke 180 | 20 % → 0 % | 55.1 px | 0.00 | 0.00 | 20 |
| stroke 181 | 21 % → 0 % | 94.1 px | 0.00 | 0.00 | 9 |
| stroke 182 | 8 % → 0 % | 49.0 px | 0.00 | 0.00 | 8 |
| stroke 183 | 17 % → 1 % | 65.8 px | 0.35 | 0.05 | 11 |
| stroke 184 | 20 % → 0 % | 115.7 px | 0.00 | 0.00 | 4 |
| stroke 185 | 27 % → 0 % | 158.9 px | 0.00 | 0.00 | 4 |
| stroke 186 | 19 % → 3 % | 46.9 px | 0.35 | 0.16 | 32 |
| stroke 187 | 31 % → 0 % | 104.3 px | 0.00 | 0.00 | 13 |
| stroke 188 | 14 % → 0 % | 34.6 px | 0.31 | 0.00 | 39 |
| stroke 189 | 23 % → 0 % | 136.8 px | 0.00 | 0.00 | 4 |
| stroke 190 | 22 % → 2 % | 52.3 px | 0.35 | 0.10 | 45 |
| stroke 191 | 17 % → 0 % | 51.2 px | 0.00 | 0.00 | 15 |
| stroke 192 | 29 % → 0 % | 83.7 px | 0.00 | 0.00 | 18 |
| stroke 193 | 23 % → 0 % | 77.3 px | 0.00 | 0.00 | 9 |
| stroke 194 | 25 % → 0 % | 58.9 px | 0.00 | 0.00 | 47 |
| stroke 195 | 21 % → 0 % | 50.3 px | 0.00 | 0.00 | 37 |
| stroke 196 | 28 % → 3 % | 64.2 px | 0.35 | 0.10 | 60 |
| stroke 197 | 28 % → 0 % | 105.2 px | 0.00 | 0.00 | 10 |
| stroke 198 | 23 % → 0 % | 135.3 px | 0.00 | 0.00 | 8 |
| stroke 199 | 30 % → 0 % | 71.8 px | 0.00 | 0.00 | 42 |
| stroke 200 | 30 % → 0 % | 98.9 px | 0.00 | 0.00 | 16 |
| stroke 201 | 22 % → 0 % | 130.3 px | 0.00 | 0.00 | 25 |
| stroke 202 | 26 % → 0 % | 117.6 px | 0.00 | 0.00 | 10 |
| stroke 203 | 29 % → 0 % | 130.6 px | 0.00 | 0.00 | 6 |
| stroke 204 | 29 % → 0 % | 184.0 px | 0.00 | 0.00 | 7 |
| stroke 205 | 28 % → 0 % | 126.7 px | 0.00 | 0.00 | 10 |
| stroke 206 | 26 % → 0 % | 67.2 px | 0.00 | 0.00 | 25 |
| stroke 207 | 28 % → 0 % | 173.2 px | 0.00 | 0.00 | 5 |
| stroke 208 | 25 % → 0 % | 96.5 px | 0.00 | 0.00 | 12 |
| stroke 209 | 24 % → 0 % | 140.1 px | 0.00 | 0.00 | 5 |
| stroke 210 | 24 % → 0 % | 111.6 px | 0.00 | 0.00 | 5 |
| stroke 211 | 24 % → 0 % | 144.0 px | 0.00 | 0.00 | 8 |
| stroke 212 | 17 % → 0 % | 78.1 px | 0.00 | 0.00 | 9 |
| stroke 213 | 24 % → 0 % | 58.5 px | 0.00 | 0.00 | 39 |
| stroke 214 | 28 % → 0 % | 101.8 px | 0.00 | 0.00 | 9 |
| stroke 215 | 14 % → 4 % | 39.9 px | 0.35 | 0.25 | 20 |
| stroke 216 | 27 % → 0 % | 82.4 px | 0.00 | 0.00 | 18 |
| stroke 217 | 24 % → 0 % | 107.7 px | 0.00 | 0.00 | 15 |
| stroke 218 | 28 % → 0 % | 157.2 px | 0.00 | 0.00 | 5 |
| stroke 219 | 20 % → 0 % | 74.0 px | 0.00 | 0.00 | 15 |
| stroke 220 | 26 % → 0 % | 84.5 px | 0.00 | 0.00 | 15 |
| stroke 221 | 24 % → 3 % | 108.3 px | 0.35 | 0.11 | 13 |
| stroke 222 | 25 % → 0 % | 70.1 px | 0.00 | 0.00 | 17 |
| stroke 223 | 28 % → 1 % | 70.4 px | 0.34 | 0.02 | 30 |
| stroke 224 | 23 % → 0 % | 104.8 px | 0.00 | 0.00 | 8 |
| stroke 225 | 31 % → 0 % | 92.2 px | 0.00 | 0.00 | 17 |
| stroke 226 | 29 % → 4 % | 94.6 px | 0.35 | 0.15 | 15 |
| stroke 227 | 23 % → 0 % | 100.1 px | 0.00 | 0.00 | 10 |
| stroke 228 | 29 % → 3 % | 67.5 px | 0.35 | 0.10 | 39 |
| stroke 229 | 12 % → 8 % | 51.2 px | 0.35 | 0.71 | 8 |
| stroke 230 | 30 % → 1 % | 70.4 px | 0.34 | 0.04 | 50 |
| stroke 231 | 16 % → 8 % | 73.9 px | 0.35 | 0.53 | 8 |
| stroke 232 | 36 % → 0 % | 92.2 px | 0.00 | 0.00 | 26 |
| stroke 233 | 21 % → 5 % | 54.9 px | 0.35 | 0.22 | 30 |
| stroke 234 | 37 % → 0 % | 89.9 px | 0.31 | 0.00 | 55 |
| stroke 235 | 38 % → 0 % | 92.5 px | 0.00 | 0.00 | 46 |
| stroke 236 | 19 % → 5 % | 50.6 px | 0.35 | 0.25 | 23 |
| stroke 237 | 27 % → 2 % | 64.0 px | 0.35 | 0.07 | 53 |
| stroke 238 | 38 % → 0 % | 88.6 px | 0.00 | 0.00 | 39 |
| stroke 239 | 38 % → 0 % | 91.4 px | 0.00 | 0.00 | 29 |
| stroke 240 | 37 % → 0 % | 102.1 px | 0.00 | 0.00 | 19 |
| stroke 241 | 33 % → 0 % | 149.3 px | 0.00 | 0.00 | 12 |
| stroke 242 | 12 % → 36 % | 38.4 px | 0.35 | 2.98 | 51 |
| stroke 243 | 24 % → 32 % | 90.4 px | 0.35 | 1.36 | 55 |
| stroke 244 | 9 % → 30 % | 35.5 px | 0.35 | 3.21 | 55 |
| stroke 245 | 16 % → 28 % | 50.7 px | 0.35 | 1.78 | 57 |
| stroke 246 | 39 % → 43 % | 103.7 px | 0.35 | 1.12 | 100 |
| stroke 247 | 41 % → 41 % | 165.7 px | 0.35 | 1.00 | 56 |
| stroke 248 | 10 % → 55 % | 32.1 px | 0.35 | 5.57 | 58 |
| stroke 249 | 13 % → 27 % | 35.6 px | 0.35 | 2.19 | 68 |
| stroke 250 | 25 % → 30 % | 62.8 px | 0.35 | 1.23 | 93 |
| stroke 251 | 16 % → 70 % | 59.8 px | 0.35 | 4.53 | 43 |
| stroke 252 | 26 % → 47 % | 70.2 px | 0.35 | 1.80 | 108 |
| stroke 253 | 30 % → 46 % | 96.6 px | 0.35 | 1.52 | 53 |
| stroke 254 | 15 % → 40 % | 60.9 px | 0.35 | 2.67 | 26 |
| stroke 255 | 21 % → 55 % | 55.1 px | 0.35 | 2.62 | 84 |
| stroke 256 | 22 % → 41 % | 57.2 px | 0.35 | 1.87 | 83 |
| stroke 257 | 34 % → 34 % | 114.5 px | 0.35 | 1.02 | 61 |
| stroke 258 | 46 % → 57 % | 195.1 px | 0.35 | 1.24 | 40 |
| stroke 259 | 16 % → 52 % | 62.9 px | 0.35 | 3.31 | 34 |
| stroke 260 | 46 % → 52 % | 159.6 px | 0.35 | 1.14 | 48 |
| stroke 261 | 23 % → 46 % | 90.7 px | 0.35 | 1.95 | 42 |
| stroke 262 | 33 % → 63 % | 143.1 px | 0.35 | 1.90 | 43 |
| stroke 263 | 42 % → 63 % | 166.7 px | 0.35 | 1.50 | 48 |
| stroke 264 | 53 % → 58 % | 184.6 px | 0.35 | 1.08 | 55 |
| stroke 265 | 45 % → 63 % | 158.6 px | 0.35 | 1.40 | 53 |
| stroke 266 | 40 % → 50 % | 175.5 px | 0.35 | 1.27 | 39 |
| stroke 267 | 73 % → 82 % | 319.3 px | 0.35 | 1.13 | 27 |
| stroke 268 | 62 % → 65 % | 206.8 px | 0.35 | 1.04 | 60 |
| stroke 269 | 52 % → 53 % | 206.0 px | 0.35 | 1.02 | 41 |
| stroke 270 | 56 % → 56 % | 167.8 px | 0.35 | 1.00 | 71 |
| stroke 271 | 21 % → 21 % | 45.6 px | 0.35 | 1.00 | 107 |
| stroke 272 | 13 % → 21 % | 59.5 px | 0.35 | 1.70 | 25 |
| stroke 273 | 16 % → 16 % | 64.5 px | 0.35 | 1.01 | 37 |
| stroke 274 | 11 % → 37 % | 34.9 px | 0.35 | 3.48 | 61 |
| stroke 275 | 19 % → 44 % | 72.7 px | 0.35 | 2.31 | 46 |
| stroke 276 | 25 % → 36 % | 93.9 px | 0.35 | 1.45 | 51 |
| stroke 277 | 27 % → 32 % | 93.4 px | 0.35 | 1.19 | 51 |
| stroke 278 | 39 % → 40 % | 136.8 px | 0.35 | 1.04 | 60 |
| stroke 279 | 9 % → 35 % | 39.4 px | 0.35 | 4.10 | 32 |
| stroke 280 | 16 % → 27 % | 49.5 px | 0.35 | 1.71 | 58 |
| stroke 281 | 21 % → 28 % | 82.8 px | 0.35 | 1.31 | 50 |
| stroke 282 | 23 % → 48 % | 71.5 px | 0.35 | 2.10 | 68 |
| stroke 283 | 25 % → 46 % | 68.0 px | 0.35 | 1.83 | 69 |
| stroke 284 | 12 % → 26 % | 49.3 px | 0.35 | 2.20 | 30 |
| stroke 285 | 16 % → 20 % | 72.2 px | 0.35 | 1.23 | 41 |
| stroke 286 | 27 % → 43 % | 106.2 px | 0.35 | 1.59 | 43 |
| stroke 287 | 38 % → 54 % | 155.8 px | 0.35 | 1.44 | 37 |
| stroke 288 | 43 % → 51 % | 144.7 px | 0.35 | 1.18 | 84 |
| stroke 289 | 33 % → 33 % | 113.7 px | 0.35 | 1.00 | 47 |
| stroke 290 | 9 % → 9 % | 34.8 px | 0.35 | 1.00 | 27 |
| stroke 291 | 11 % → 11 % | 26.4 px | 0.35 | 1.00 | 77 |
| stroke 292 | 10 % → 10 % | 25.8 px | 0.35 | 1.00 | 69 |

Numbers say: wet paint spreads well beyond the stroke.

## Refs v3 · #19 Guston charcoal hand — own sheet
own sheet 800 × 800 · Charcoal 1.00 · 39 px · 35.7 s

![Refs v3 · #19 Guston charcoal hand — own sheet](Refs-v3-19-Guston-charcoal-hand-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 5 % → 21 % | 21.0 px | 0.60 | 4.64 | 57 |
| stroke 2 | 8 % → 22 % | 44.5 px | 0.60 | 2.61 | 46 |
| stroke 3 | 8 % → 21 % | 100.9 px | 0.60 | 2.61 | 28 |
| stroke 4 | 12 % → 21 % | 65.1 px | 0.60 | 1.75 | 66 |
| stroke 5 | 6 % → 19 % | 40.8 px | 0.60 | 2.97 | 75 |
| stroke 6 | 17 % → 23 % | 229.3 px | 0.60 | 1.36 | 26 |
| stroke 7 | 18 % → 22 % | 260.0 px | 0.60 | 1.20 | 27 |
| stroke 8 | 17 % → 21 % | 126.5 px | 0.60 | 1.23 | 62 |
| stroke 9 | 3 % → 38 % | 19.9 px | 0.60 | 14.43 | 62 |
| stroke 10 | 5 % → 42 % | 43.5 px | 0.60 | 8.16 | 34 |
| stroke 11 | 4 % → 26 % | 24.9 px | 0.60 | 6.53 | 44 |
| stroke 12 | 3 % → 37 % | 23.4 px | 0.60 | 10.60 | 75 |
| stroke 13 | 3 % → 34 % | 29.2 px | 0.60 | 10.97 | 21 |
| stroke 14 | 2 % → 40 % | 29.8 px | 0.60 | 21.75 | 30 |
| stroke 15 | 8 % → 41 % | 50.4 px | 0.60 | 5.14 | 73 |
| stroke 16 | 7 % → 50 % | 61.0 px | 0.60 | 7.10 | 44 |
| stroke 17 | 7 % → 27 % | 91.0 px | 0.60 | 3.81 | 27 |
| stroke 18 | 2 % → 38 % | 27.3 px | 0.60 | 22.18 | 18 |
| stroke 19 | 2 % → 50 % | 21.3 px | 0.60 | 22.44 | 37 |
| stroke 20 | 2 % → 33 % | 27.8 px | 0.60 | 17.39 | 30 |
| stroke 21 | 10 % → 42 % | 85.0 px | 0.60 | 4.18 | 54 |
| stroke 22 | 5 % → 40 % | 68.0 px | 0.60 | 7.83 | 22 |
| stroke 23 | 14 % → 26 % | 59.5 px | 0.60 | 1.90 | 138 |
| stroke 24 | 10 % → 19 % | 39.8 px | 0.60 | 1.87 | 156 |
| stroke 25 | 3 % → 43 % | 30.6 px | 0.60 | 12.59 | 61 |
| stroke 26 | 10 % → 58 % | 99.2 px | 0.60 | 6.00 | 45 |
| stroke 27 | 13 % → 59 % | 136.9 px | 0.60 | 4.52 | 65 |
| stroke 28 | 14 % → 56 % | 71.9 px | 0.60 | 3.88 | 132 |
| stroke 29 | 9 % → 46 % | 93.0 px | 0.60 | 4.99 | 37 |
| stroke 30 | 16 % → 40 % | 71.4 px | 0.60 | 2.48 | 133 |
| stroke 31 | 5 % → 37 % | 68.6 px | 0.60 | 7.20 | 34 |
| stroke 32 | 7 % → 39 % | 103.5 px | 0.60 | 5.55 | 34 |
| stroke 33 | 7 % → 33 % | 79.3 px | 0.60 | 4.94 | 37 |
| stroke 34 | 21 % → 60 % | 154.1 px | 0.60 | 2.86 | 76 |
| stroke 35 | 17 % → 54 % | 198.0 px | 0.60 | 3.24 | 35 |
| stroke 36 | 15 % → 24 % | 50.7 px | 0.60 | 1.61 | 103 |
| stroke 37 | 19 % → 40 % | 179.6 px | 0.60 | 2.06 | 48 |
| stroke 38 | 9 % → 30 % | 59.4 px | 0.60 | 3.31 | 59 |
| stroke 39 | 15 % → 49 % | 183.6 px | 0.60 | 3.25 | 30 |
| stroke 40 | 18 % → 44 % | 133.6 px | 0.60 | 2.47 | 56 |
| stroke 41 | 17 % → 32 % | 138.0 px | 0.60 | 1.91 | 47 |
| stroke 42 | 12 % → 44 % | 107.0 px | 0.60 | 3.53 | 50 |
| stroke 43 | 11 % → 34 % | 93.2 px | 0.60 | 3.15 | 36 |
| stroke 44 | 17 % → 38 % | 69.3 px | 0.60 | 2.18 | 169 |
| stroke 45 | 15 % → 27 % | 58.3 px | 0.60 | 1.78 | 183 |
| stroke 46 | 19 % → 52 % | 209.0 px | 0.60 | 2.76 | 34 |
| stroke 47 | 18 % → 51 % | 251.8 px | 0.60 | 2.81 | 21 |
| stroke 48 | 20 % → 47 % | 171.6 px | 0.60 | 2.37 | 49 |
| stroke 49 | 5 % → 22 % | 31.6 px | 0.60 | 4.63 | 70 |
| stroke 50 | 30 % → 54 % | 289.2 px | 0.60 | 1.81 | 70 |
| stroke 51 | 29 % → 50 % | 208.5 px | 0.60 | 1.76 | 59 |
| stroke 52 | 13 % → 32 % | 109.6 px | 0.60 | 2.49 | 49 |
| stroke 53 | 13 % → 37 % | 110.1 px | 0.60 | 2.88 | 61 |
| stroke 54 | 14 % → 33 % | 167.9 px | 0.60 | 2.44 | 29 |
| stroke 55 | 29 % → 47 % | 253.6 px | 0.60 | 1.63 | 58 |
| stroke 56 | 24 % → 50 % | 332.9 px | 0.60 | 2.11 | 28 |
| stroke 57 | 19 % → 46 % | 237.6 px | 0.60 | 2.47 | 32 |
| stroke 58 | 10 % → 28 % | 93.6 px | 0.60 | 2.75 | 46 |
| stroke 59 | 33 % → 54 % | 337.9 px | 0.60 | 1.63 | 39 |
| stroke 60 | 29 % → 53 % | 212.7 px | 0.60 | 1.83 | 57 |
| stroke 61 | 19 % → 31 % | 280.6 px | 0.60 | 1.63 | 21 |
| stroke 62 | 24 % → 29 % | 185.4 px | 0.60 | 1.24 | 85 |
| stroke 63 | 39 % → 56 % | 319.6 px | 0.60 | 1.43 | 47 |
| stroke 64 | 22 % → 37 % | 68.8 px | 0.60 | 1.68 | 243 |
| stroke 65 | 24 % → 41 % | 107.6 px | 0.60 | 1.71 | 142 |
| stroke 66 | 19 % → 30 % | 166.4 px | 0.60 | 1.54 | 61 |
| stroke 67 | 28 % → 44 % | 122.1 px | 0.60 | 1.58 | 145 |
| stroke 68 | 38 % → 54 % | 215.0 px | 0.60 | 1.43 | 82 |
| stroke 69 | 29 % → 51 % | 316.7 px | 0.60 | 1.76 | 36 |
| stroke 70 | 27 % → 31 % | 326.9 px | 0.60 | 1.15 | 23 |
| stroke 71 | 14 % → 26 % | 191.5 px | 0.60 | 1.93 | 29 |
| stroke 72 | 37 % → 55 % | 216.0 px | 0.60 | 1.49 | 67 |
| stroke 73 | 30 % → 46 % | 389.8 px | 0.60 | 1.55 | 23 |
| stroke 74 | 29 % → 32 % | 70.1 px | 0.60 | 1.11 | 256 |
| stroke 75 | 28 % → 41 % | 284.0 px | 0.60 | 1.46 | 39 |
| stroke 76 | 47 % → 57 % | 456.4 px | 0.60 | 1.21 | 43 |
| stroke 77 | 36 % → 44 % | 241.2 px | 0.60 | 1.22 | 60 |
| stroke 78 | 36 % → 50 % | 399.9 px | 0.60 | 1.40 | 36 |
| stroke 79 | 32 % → 47 % | 547.0 px | 0.60 | 1.45 | 25 |
| stroke 80 | 37 % → 49 % | 438.8 px | 0.60 | 1.34 | 38 |
| stroke 81 | 29 % → 33 % | 135.4 px | 0.60 | 1.16 | 151 |
| stroke 82 | 34 % → 49 % | 287.7 px | 0.60 | 1.43 | 53 |
| stroke 83 | 31 % → 40 % | 456.2 px | 0.60 | 1.28 | 30 |
| stroke 84 | 34 % → 41 % | 252.6 px | 0.60 | 1.19 | 62 |
| stroke 85 | 30 % → 33 % | 187.0 px | 0.60 | 1.11 | 82 |
| stroke 86 | 17 % → 25 % | 143.2 px | 0.60 | 1.41 | 49 |
| stroke 87 | 32 % → 37 % | 197.9 px | 0.60 | 1.17 | 80 |
| stroke 88 | 42 % → 50 % | 258.4 px | 0.60 | 1.20 | 82 |
| stroke 89 | 33 % → 47 % | 426.4 px | 0.60 | 1.39 | 32 |
| stroke 90 | 17 % → 22 % | 185.3 px | 0.60 | 1.27 | 32 |
| stroke 91 | 30 % → 32 % | 256.9 px | 0.60 | 1.07 | 45 |
| stroke 92 | 45 % → 51 % | 365.0 px | 0.60 | 1.14 | 38 |
| stroke 93 | 44 % → 51 % | 576.4 px | 0.60 | 1.17 | 37 |
| stroke 94 | 30 % → 38 % | 178.5 px | 0.60 | 1.25 | 83 |
| stroke 95 | 48 % → 54 % | 413.6 px | 0.60 | 1.14 | 45 |
| stroke 96 | 18 % → 22 % | 268.5 px | 0.60 | 1.18 | 20 |
| stroke 97 | 29 % → 32 % | 116.5 px | 0.60 | 1.08 | 148 |
| stroke 98 | 43 % → 47 % | 696.1 px | 0.60 | 1.08 | 20 |
| stroke 99 | 45 % → 50 % | 724.5 px | 0.60 | 1.13 | 30 |
| stroke 100 | 36 % → 37 % | 296.1 px | 0.60 | 1.01 | 44 |
| stroke 101 | 40 % → 45 % | 335.7 px | 0.60 | 1.12 | 76 |
| stroke 102 | 52 % → 56 % | 483.8 px | 0.60 | 1.06 | 43 |
| stroke 103 | 19 % → 22 % | 343.6 px | 0.60 | 1.13 | 17 |
| stroke 104 | 40 % → 45 % | 682.8 px | 0.60 | 1.13 | 21 |
| stroke 105 | 47 % → 49 % | 518.6 px | 0.60 | 1.03 | 39 |
| stroke 106 | 29 % → 35 % | 275.1 px | 0.60 | 1.23 | 38 |
| stroke 107 | 55 % → 57 % | 561.3 px | 0.60 | 1.02 | 40 |
| stroke 108 | 47 % → 47 % | 246.8 px | 0.60 | 1.00 | 121 |
| stroke 109 | 58 % → 59 % | 879.8 px | 0.60 | 1.01 | 43 |
| stroke 110 | 32 % → 32 % | 270.3 px | 0.60 | 1.00 | 59 |
| stroke 111 | 40 % → 42 % | 318.6 px | 0.60 | 1.05 | 56 |
| stroke 112 | 38 % → 38 % | 243.6 px | 0.60 | 1.00 | 87 |
| stroke 113 | 53 % → 53 % | 536.3 px | 0.60 | 1.00 | 40 |
| stroke 114 | 31 % → 31 % | 260.3 px | 0.60 | 1.00 | 58 |
| stroke 115 | 23 % → 23 % | 212.9 px | 0.60 | 1.00 | 39 |

Numbers say: wet paint spreads well beyond the stroke.

## Refs v3 · #20 Orange crayon — own sheet
own sheet 800 × 1245 · Wax 1.00 · 48 px · 233.6 s

![Refs v3 · #20 Orange crayon — own sheet](Refs-v3-20-Orange-crayon-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 8 % → 68 % | 44.8 px | 0.55 | 8.13 | 255 |
| stroke 2 | 16 % → 79 % | 51.6 px | 0.55 | 5.08 | 457 |
| stroke 3 | 6 % → 47 % | 48.5 px | 0.55 | 8.18 | 163 |
| stroke 4 | 6 % → 31 % | 45.9 px | 0.55 | 5.60 | 174 |
| stroke 5 | 21 % → 85 % | 62.3 px | 0.55 | 4.12 | 782 |
| stroke 6 | 9 % → 54 % | 68.5 px | 0.55 | 5.88 | 208 |
| stroke 7 | 14 % → 41 % | 81.9 px | 0.55 | 3.05 | 316 |
| stroke 8 | 4 % → 12 % | 61.6 px | 0.51 | 2.79 | 70 |
| stroke 9 | 24 % → 89 % | 73.5 px | 0.55 | 3.67 | 1052 |
| stroke 10 | 18 % → 53 % | 79.3 px | 0.55 | 3.00 | 794 |
| stroke 11 | 23 % → 78 % | 86.1 px | 0.55 | 3.35 | 2391 |
| stroke 12 | 7 % → 19 % | 116.1 px | 0.52 | 2.60 | 74 |
| stroke 13 | 30 % → 81 % | 106.3 px | 0.55 | 2.73 | 2374 |
| stroke 14 | 11 % → 30 % | 127.2 px | 0.53 | 2.81 | 125 |
| stroke 15 | 37 % → 85 % | 136.2 px | 0.55 | 2.32 | 2223 |
| stroke 16 | 15 % → 44 % | 159.0 px | 0.54 | 2.85 | 128 |
| stroke 17 | 40 % → 86 % | 162.2 px | 0.55 | 2.13 | 2380 |
| stroke 18 | 21 % → 58 % | 150.1 px | 0.54 | 2.73 | 251 |
| stroke 19 | 43 % → 87 % | 184.8 px | 0.55 | 2.00 | 2290 |
| stroke 20 | 31 % → 72 % | 172.2 px | 0.55 | 2.35 | 382 |
| stroke 21 | 53 % → 94 % | 206.2 px | 0.55 | 1.79 | 1657 |
| stroke 22 | 39 % → 83 % | 174.9 px | 0.55 | 2.13 | 831 |
| stroke 23 | 24 % → 46 % | 300.8 px | 0.54 | 1.88 | 98 |
| stroke 24 | 53 % → 96 % | 207.1 px | 0.55 | 1.80 | 1629 |
| stroke 25 | 35 % → 74 % | 150.0 px | 0.54 | 2.14 | 1278 |
| stroke 26 | 43 % → 86 % | 204.1 px | 0.55 | 1.98 | 3320 |
| stroke 27 | 47 % → 90 % | 217.4 px | 0.55 | 1.92 | 2639 |
| stroke 28 | 49 % → 93 % | 226.5 px | 0.55 | 1.89 | 2569 |
| stroke 29 | 40 % → 83 % | 201.9 px | 0.55 | 2.06 | 3369 |
| stroke 30 | 56 % → 99 % | 232.5 px | 0.55 | 1.77 | 2349 |
| stroke 31 | 39 % → 84 % | 172.4 px | 0.54 | 2.13 | 815 |
| stroke 32 | 17 % → 49 % | 211.4 px | 0.55 | 2.84 | 88 |
| stroke 33 | 56 % → 99 % | 227.7 px | 0.55 | 1.75 | 1930 |
| stroke 34 | 52 % → 97 % | 234.1 px | 0.54 | 1.87 | 835 |
| stroke 35 | 25 % → 63 % | 157.0 px | 0.55 | 2.50 | 365 |
| stroke 36 | 56 % → 99 % | 225.4 px | 0.55 | 1.75 | 1878 |
| stroke 37 | 46 % → 93 % | 205.1 px | 0.54 | 2.02 | 1208 |
| stroke 38 | 34 % → 72 % | 246.2 px | 0.55 | 2.09 | 318 |
| stroke 39 | 43 % → 86 % | 216.0 px | 0.55 | 2.00 | 4005 |
| stroke 40 | 44 % → 87 % | 220.9 px | 0.55 | 1.97 | 5256 |
| stroke 41 | 45 % → 88 % | 226.6 px | 0.55 | 1.94 | 4493 |
| stroke 42 | 46 % → 89 % | 231.1 px | 0.55 | 1.91 | 3777 |
| stroke 43 | 48 % → 89 % | 234.4 px | 0.55 | 1.86 | 6839 |
| stroke 44 | 50 % → 88 % | 234.3 px | 0.55 | 1.75 | 7151 |
| stroke 45 | 53 % → 87 % | 230.5 px | 0.55 | 1.62 | 7315 |
| stroke 46 | 61 % → 96 % | 254.0 px | 0.55 | 1.57 | 4558 |
| stroke 47 | 45 % → 46 % | 225.3 px | 0.55 | 1.02 | 260 |
| stroke 48 | 65 % → 96 % | 253.0 px | 0.55 | 1.49 | 5031 |
| stroke 49 | 62 % → 98 % | 235.5 px | 0.55 | 1.57 | 3845 |
| stroke 50 | 75 % → 83 % | 305.4 px | 0.55 | 1.11 | 466 |
| stroke 51 | 66 % → 98 % | 231.2 px | 0.55 | 1.49 | 2149 |
| stroke 52 | 79 % → 87 % | 476.9 px | 0.55 | 1.11 | 379 |
| stroke 53 | 73 % → 97 % | 232.5 px | 0.55 | 1.33 | 2549 |
| stroke 54 | 72 % → 99 % | 221.1 px | 0.55 | 1.37 | 1576 |
| stroke 55 | 89 % → 95 % | 391.8 px | 0.55 | 1.07 | 211 |
| stroke 56 | 79 % → 99 % | 219.0 px | 0.55 | 1.25 | 1389 |
| stroke 57 | 83 % → 99 % | 214.1 px | 0.55 | 1.19 | 1177 |
| stroke 58 | 86 % → 98 % | 206.5 px | 0.55 | 1.14 | 910 |
| stroke 59 | 91 % → 98 % | 214.9 px | 0.55 | 1.08 | 783 |
| stroke 60 | 95 % → 97 % | 250.9 px | 0.55 | 1.02 | 421 |
| stroke 61 | 65 % → 66 % | 197.2 px | 0.55 | 1.01 | 2477 |
| stroke 62 | 87 % → 87 % | 252.7 px | 0.55 | 1.00 | 3230 |
| stroke 63 | 94 % → 94 % | 286.9 px | 0.55 | 1.00 | 2342 |
| stroke 64 | 98 % → 98 % | 246.4 px | 0.55 | 1.00 | 5958 |
| stroke 65 | 98 % → 99 % | 205.4 px | 0.55 | 1.00 | 1494 |
| stroke 66 | 98 % → 98 % | 241.1 px | 0.55 | 1.00 | 1921 |
| stroke 67 | 98 % → 98 % | 205.4 px | 0.55 | 1.00 | 2114 |
| stroke 68 | 97 % → 97 % | 191.4 px | 0.55 | 1.01 | 2327 |
| stroke 69 | 97 % → 97 % | 221.9 px | 0.55 | 1.00 | 1954 |
| stroke 70 | 88 % → 88 % | 192.8 px | 0.55 | 1.00 | 2113 |
| stroke 71 | 78 % → 78 % | 286.1 px | 0.55 | 1.00 | 1567 |
| stroke 72 | 56 % → 56 % | 229.1 px | 0.55 | 1.01 | 1715 |
| stroke 73 | 48 % → 49 % | 183.3 px | 0.55 | 1.01 | 2481 |
| stroke 74 | 80 % → 80 % | 338.3 px | 0.55 | 1.00 | 2328 |
| stroke 75 | 65 % → 66 % | 234.7 px | 0.55 | 1.01 | 2546 |
| stroke 76 | 54 % → 55 % | 209.8 px | 0.54 | 1.03 | 1431 |
| stroke 77 | 72 % → 73 % | 326.7 px | 0.55 | 1.02 | 1942 |
| stroke 78 | 64 % → 64 % | 290.0 px | 0.55 | 1.00 | 1141 |
| stroke 79 | 54 % → 54 % | 193.8 px | 0.55 | 1.00 | 1711 |
| stroke 80 | 45 % → 45 % | 493.0 px | 0.55 | 1.00 | 206 |
| stroke 81 | 98 % → 98 % | 417.2 px | 0.55 | 1.00 | 1232 |
| stroke 82 | 97 % → 97 % | 554.3 px | 0.55 | 1.00 | 719 |
| stroke 83 | 99 % → 99 % | 409.7 px | 0.54 | 1.00 | 938 |
| stroke 84 | 99 % → 99 % | 623.5 px | 0.54 | 1.00 | 530 |
| stroke 85 | 99 % → 99 % | 369.0 px | 0.54 | 1.00 | 995 |
| stroke 86 | 85 % → 85 % | 352.4 px | 0.55 | 1.00 | 1003 |
| stroke 87 | 92 % → 92 % | 546.3 px | 0.55 | 1.00 | 534 |
| stroke 88 | 59 % → 59 % | 242.3 px | 0.55 | 1.00 | 684 |

Numbers say: wet paint spreads well beyond the stroke.

## Refs v3 · #21 Gritty dog contours — own sheet
own sheet 800 × 1130 · Gouache 1.00 + water 15 % · 53 px · 669.5 s

![Refs v3 · #21 Gritty dog contours — own sheet](Refs-v3-21-Gritty-dog-contours-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 5 % → 2 % | 53.8 px | 0.42 | 0.44 | 245 |
| stroke 2 | 8 % → 2 % | 113.6 px | 0.42 | 0.27 | 129 |
| stroke 3 | 10 % → 1 % | 75.5 px | 0.41 | 0.14 | 575 |
| stroke 4 | 16 % → 2 % | 148.2 px | 0.42 | 0.15 | 370 |
| stroke 5 | 25 % → 2 % | 448.1 px | 0.42 | 0.09 | 101 |
| stroke 6 | 18 % → 3 % | 144.6 px | 0.43 | 0.17 | 479 |
| stroke 7 | 21 % → 2 % | 159.0 px | 0.42 | 0.12 | 739 |
| stroke 8 | 20 % → 3 % | 167.1 px | 0.43 | 0.13 | 397 |
| stroke 9 | 18 % → 4 % | 110.6 px | 0.43 | 0.21 | 1267 |
| stroke 10 | 33 % → 1 % | 356.0 px | 0.42 | 0.04 | 325 |
| stroke 11 | 41 % → 2 % | 746.6 px | 0.44 | 0.04 | 121 |
| stroke 12 | 23 % → 3 % | 150.8 px | 0.43 | 0.12 | 1095 |
| stroke 13 | 34 % → 2 % | 291.7 px | 0.43 | 0.07 | 414 |
| stroke 14 | 31 % → 4 % | 208.5 px | 0.43 | 0.12 | 660 |
| stroke 15 | 22 % → 5 % | 305.0 px | 0.43 | 0.24 | 177 |
| stroke 16 | 41 % → 2 % | 736.1 px | 0.44 | 0.04 | 120 |
| stroke 17 | 34 % → 5 % | 224.3 px | 0.43 | 0.14 | 872 |
| stroke 18 | 34 % → 2 % | 593.7 px | 0.44 | 0.05 | 108 |
| stroke 19 | 32 % → 4 % | 205.4 px | 0.43 | 0.12 | 1049 |
| stroke 20 | 45 % → 5 % | 517.5 px | 0.43 | 0.11 | 245 |
| stroke 21 | 36 % → 5 % | 452.7 px | 0.43 | 0.15 | 192 |
| stroke 22 | 38 % → 4 % | 304.4 px | 0.43 | 0.11 | 841 |
| stroke 23 | 33 % → 5 % | 348.4 px | 0.43 | 0.16 | 272 |
| stroke 24 | 32 % → 5 % | 324.6 px | 0.43 | 0.15 | 315 |
| stroke 25 | 29 % → 4 % | 253.6 px | 0.43 | 0.15 | 434 |
| stroke 26 | 6 % → 2 % | 78.9 px | 0.43 | 0.40 | 191 |
| stroke 27 | 31 % → 5 % | 309.7 px | 0.43 | 0.17 | 397 |
| stroke 28 | 45 % → 5 % | 690.0 px | 0.43 | 0.12 | 137 |
| stroke 29 | 29 % → 4 % | 222.9 px | 0.42 | 0.16 | 752 |
| stroke 30 | 7 % → 2 % | 84.3 px | 0.43 | 0.24 | 320 |
| stroke 31 | 32 % → 6 % | 343.4 px | 0.43 | 0.18 | 443 |
| stroke 32 | 46 % → 6 % | 577.3 px | 0.44 | 0.13 | 312 |
| stroke 33 | 31 % → 6 % | 218.0 px | 0.42 | 0.19 | 954 |
| stroke 34 | 13 % → 1 % | 144.4 px | 0.42 | 0.09 | 301 |
| stroke 35 | 34 % → 7 % | 422.0 px | 0.43 | 0.19 | 366 |
| stroke 36 | 43 % → 7 % | 527.7 px | 0.43 | 0.17 | 251 |
| stroke 37 | 30 % → 5 % | 202.6 px | 0.42 | 0.17 | 778 |
| stroke 38 | 14 % → 1 % | 164.1 px | 0.42 | 0.06 | 549 |
| stroke 39 | 37 % → 9 % | 655.3 px | 0.43 | 0.24 | 304 |
| stroke 40 | 40 % → 8 % | 546.7 px | 0.43 | 0.19 | 362 |
| stroke 41 | 30 % → 4 % | 200.3 px | 0.42 | 0.14 | 1909 |
| stroke 42 | 20 % → 0 % | 194.8 px | 0.42 | 0.02 | 890 |
| stroke 43 | 37 % → 9 % | 652.5 px | 0.43 | 0.24 | 304 |
| stroke 44 | 44 % → 6 % | 545.4 px | 0.41 | 0.13 | 403 |
| stroke 45 | 32 % → 3 % | 209.5 px | 0.42 | 0.11 | 2018 |
| stroke 46 | 31 % → 0 % | 437.6 px | 0.42 | 0.01 | 194 |
| stroke 47 | 23 % → 0 % | 344.1 px | 0.40 | 0.00 | 440 |
| stroke 48 | 35 % → 8 % | 397.6 px | 0.43 | 0.23 | 479 |
| stroke 49 | 28 % → 3 % | 175.6 px | 0.42 | 0.12 | 2410 |
| stroke 50 | 26 % → 1 % | 357.1 px | 0.43 | 0.02 | 322 |
| stroke 51 | 30 % → 10 % | 533.3 px | 0.43 | 0.32 | 127 |
| stroke 52 | 43 % → 5 % | 462.2 px | 0.41 | 0.12 | 401 |
| stroke 53 | 35 % → 2 % | 226.8 px | 0.42 | 0.07 | 976 |
| stroke 54 | 28 % → 1 % | 353.2 px | 0.43 | 0.02 | 235 |
| stroke 55 | 28 % → 9 % | 342.8 px | 0.43 | 0.31 | 205 |
| stroke 56 | 40 % → 3 % | 262.6 px | 0.42 | 0.09 | 1624 |
| stroke 57 | 44 % → 0 % | 779.9 px | 0.43 | 0.01 | 461 |
| stroke 58 | 30 % → 1 % | 414.7 px | 0.43 | 0.02 | 406 |
| stroke 59 | 43 % → 6 % | 767.6 px | 0.41 | 0.14 | 252 |
| stroke 60 | 44 % → 3 % | 292.7 px | 0.42 | 0.07 | 2328 |
| stroke 61 | 33 % → 1 % | 267.0 px | 0.43 | 0.02 | 1079 |
| stroke 62 | 24 % → 8 % | 332.0 px | 0.42 | 0.33 | 275 |
| stroke 63 | 42 % → 6 % | 351.3 px | 0.42 | 0.14 | 934 |
| stroke 64 | 49 % → 4 % | 320.9 px | 0.42 | 0.07 | 2159 |
| stroke 65 | 49 % → 1 % | 893.9 px | 0.43 | 0.02 | 288 |
| stroke 66 | 33 % → 1 % | 412.0 px | 0.43 | 0.02 | 612 |
| stroke 67 | 38 % → 6 % | 413.5 px | 0.41 | 0.16 | 457 |
| stroke 68 | 50 % → 4 % | 320.7 px | 0.42 | 0.08 | 1707 |
| stroke 69 | 32 % → 1 % | 369.6 px | 0.43 | 0.02 | 431 |
| stroke 70 | 31 % → 8 % | 545.2 px | 0.41 | 0.27 | 149 |
| stroke 71 | 48 % → 4 % | 300.0 px | 0.42 | 0.08 | 1356 |
| stroke 72 | 35 % → 1 % | 373.3 px | 0.43 | 0.02 | 282 |
| stroke 73 | 24 % → 7 % | 258.2 px | 0.42 | 0.29 | 290 |
| stroke 74 | 49 % → 5 % | 311.7 px | 0.41 | 0.09 | 1517 |
| stroke 75 | 30 % → 1 % | 253.2 px | 0.42 | 0.03 | 500 |
| stroke 76 | 41 % → 5 % | 253.7 px | 0.42 | 0.13 | 2192 |
| stroke 77 | 58 % → 1 % | 783.0 px | 0.43 | 0.02 | 226 |
| stroke 78 | 30 % → 1 % | 226.6 px | 0.41 | 0.04 | 619 |
| stroke 79 | 31 % → 7 % | 280.9 px | 0.42 | 0.24 | 518 |
| stroke 80 | 53 % → 6 % | 348.2 px | 0.41 | 0.12 | 952 |
| stroke 81 | 56 % → 1 % | 567.1 px | 0.43 | 0.02 | 387 |
| stroke 82 | 34 % → 1 % | 265.3 px | 0.41 | 0.04 | 548 |
| stroke 83 | 31 % → 7 % | 333.3 px | 0.42 | 0.22 | 298 |
| stroke 84 | 51 % → 7 % | 321.2 px | 0.42 | 0.14 | 1368 |
| stroke 85 | 57 % → 1 % | 541.8 px | 0.43 | 0.02 | 436 |
| stroke 86 | 36 % → 1 % | 308.7 px | 0.41 | 0.04 | 520 |
| stroke 87 | 46 % → 6 % | 284.5 px | 0.42 | 0.13 | 1592 |
| stroke 88 | 54 % → 1 % | 521.0 px | 0.43 | 0.02 | 428 |
| stroke 89 | 39 % → 2 % | 369.8 px | 0.42 | 0.04 | 703 |
| stroke 90 | 47 % → 6 % | 293.3 px | 0.42 | 0.14 | 1845 |
| stroke 91 | 57 % → 2 % | 1018.4 px | 0.42 | 0.04 | 116 |
| stroke 92 | 55 % → 2 % | 552.5 px | 0.42 | 0.03 | 299 |
| stroke 93 | 45 % → 8 % | 426.7 px | 0.42 | 0.17 | 463 |
| stroke 94 | 54 % → 10 % | 406.1 px | 0.42 | 0.19 | 690 |
| stroke 95 | 56 % → 3 % | 507.1 px | 0.42 | 0.06 | 379 |
| stroke 96 | 52 % → 2 % | 485.7 px | 0.41 | 0.04 | 801 |
| stroke 97 | 48 % → 11 % | 517.9 px | 0.42 | 0.22 | 378 |
| stroke 98 | 53 % → 5 % | 325.4 px | 0.41 | 0.09 | 2307 |
| stroke 99 | 51 % → 7 % | 316.9 px | 0.42 | 0.14 | 2249 |
| stroke 100 | 48 % → 2 % | 723.8 px | 0.41 | 0.04 | 199 |
| stroke 101 | 47 % → 11 % | 584.6 px | 0.42 | 0.23 | 360 |
| stroke 102 | 53 % → 7 % | 346.8 px | 0.41 | 0.14 | 1132 |
| stroke 103 | 44 % → 9 % | 420.6 px | 0.42 | 0.21 | 382 |
| stroke 104 | 55 % → 9 % | 552.8 px | 0.41 | 0.16 | 406 |
| stroke 105 | 52 % → 6 % | 784.2 px | 0.41 | 0.11 | 216 |
| stroke 106 | 43 % → 10 % | 433.8 px | 0.42 | 0.22 | 727 |
| stroke 107 | 49 % → 9 % | 750.3 px | 0.41 | 0.19 | 365 |
| stroke 108 | 40 % → 10 % | 430.4 px | 0.42 | 0.25 | 1814 |
| stroke 109 | 46 % → 9 % | 525.6 px | 0.41 | 0.19 | 1656 |
| stroke 110 | 40 % → 11 % | 492.2 px | 0.42 | 0.27 | 288 |
| stroke 111 | 45 % → 8 % | 365.6 px | 0.41 | 0.18 | 492 |
| stroke 112 | 41 % → 10 % | 469.2 px | 0.41 | 0.24 | 363 |
| stroke 113 | 34 % → 8 % | 587.3 px | 0.40 | 0.22 | 187 |
| stroke 114 | 39 % → 10 % | 485.4 px | 0.41 | 0.26 | 205 |
| stroke 115 | 35 % → 10 % | 397.2 px | 0.41 | 0.27 | 236 |
| stroke 116 | 32 % → 9 % | 403.5 px | 0.41 | 0.29 | 204 |
| stroke 117 | 28 % → 9 % | 323.5 px | 0.41 | 0.30 | 236 |
| stroke 118 | 24 % → 8 % | 371.1 px | 0.40 | 0.33 | 162 |
| stroke 119 | 25 % → 3 % | 240.0 px | 0.42 | 0.10 | 290 |
| stroke 120 | 60 % → 2 % | 280.6 px | 0.42 | 0.04 | 1746 |
| stroke 121 | 48 % → 1 % | 188.6 px | 0.42 | 0.03 | 1868 |
| stroke 122 | 56 % → 3 % | 302.8 px | 0.43 | 0.06 | 1219 |
| stroke 123 | 65 % → 2 % | 359.8 px | 0.42 | 0.03 | 989 |
| stroke 124 | 67 % → 3 % | 274.4 px | 0.43 | 0.04 | 1593 |
| stroke 125 | 72 % → 1 % | 359.8 px | 0.41 | 0.02 | 1835 |
| stroke 126 | 97 % → 4 % | 473.2 px | 0.42 | 0.04 | 1676 |
| stroke 127 | 79 % → 5 % | 381.8 px | 0.41 | 0.06 | 1495 |
| stroke 128 | 77 % → 7 % | 419.8 px | 0.41 | 0.09 | 1838 |
| stroke 129 | 80 % → 11 % | 357.5 px | 0.42 | 0.14 | 1893 |
| stroke 130 | 49 % → 8 % | 264.1 px | 0.42 | 0.17 | 1683 |
| stroke 131 | 45 % → 8 % | 212.6 px | 0.42 | 0.18 | 1829 |
| stroke 132 | 53 % → 8 % | 236.5 px | 0.42 | 0.15 | 1874 |
| stroke 133 | 58 % → 9 % | 250.2 px | 0.42 | 0.15 | 1444 |
| stroke 134 | 78 % → 7 % | 409.7 px | 0.42 | 0.09 | 1588 |
| stroke 135 | 87 % → 3 % | 418.3 px | 0.41 | 0.04 | 2042 |
| stroke 136 | 77 % → 4 % | 311.1 px | 0.41 | 0.05 | 1666 |
| stroke 137 | 76 % → 4 % | 371.4 px | 0.42 | 0.05 | 1461 |
| stroke 138 | 68 % → 5 % | 353.2 px | 0.43 | 0.08 | 1384 |
| stroke 139 | 47 % → 5 % | 194.7 px | 0.43 | 0.12 | 1591 |
| stroke 140 | 65 % → 3 % | 287.6 px | 0.43 | 0.04 | 1707 |
| stroke 141 | 57 % → 3 % | 309.2 px | 0.43 | 0.06 | 1412 |
| stroke 142 | 52 % → 4 % | 196.4 px | 0.43 | 0.08 | 1471 |
| stroke 143 | 73 % → 3 % | 385.0 px | 0.42 | 0.04 | 1390 |
| stroke 144 | 60 % → 1 % | 243.3 px | 0.43 | 0.02 | 1684 |
| stroke 145 | 53 % → 1 % | 244.4 px | 0.43 | 0.02 | 1910 |
| stroke 146 | 52 % → 1 % | 234.8 px | 0.41 | 0.02 | 1627 |
| stroke 147 | 65 % → 1 % | 384.8 px | 0.42 | 0.01 | 1546 |
| stroke 148 | 68 % → 1 % | 307.0 px | 0.43 | 0.01 | 1447 |
| stroke 149 | 89 % → 1 % | 376.0 px | 0.43 | 0.01 | 1585 |
| stroke 150 | 79 % → 1 % | 365.9 px | 0.42 | 0.01 | 1732 |
| stroke 151 | 60 % → 2 % | 553.6 px | 0.41 | 0.03 | 518 |
| stroke 152 | 74 % → 6 % | 324.0 px | 0.43 | 0.08 | 1138 |
| stroke 153 | 52 % → 9 % | 265.1 px | 0.43 | 0.17 | 920 |
| stroke 154 | 55 % → 8 % | 565.9 px | 0.42 | 0.15 | 410 |
| stroke 155 | 50 % → 8 % | 691.5 px | 0.43 | 0.16 | 414 |
| stroke 156 | 86 % → 6 % | 334.1 px | 0.42 | 0.07 | 1389 |
| stroke 157 | 99 % → 5 % | 520.9 px | 0.41 | 0.05 | 957 |
| stroke 158 | 58 % → 8 % | 283.1 px | 0.41 | 0.14 | 1090 |
| stroke 159 | 1 % → 4 % | 18.8 px | 0.44 | 4.49 | 25 |
| stroke 160 | 2 % → 2 % | 13.9 px | 0.43 | 1.49 | 54 |
| stroke 161 | 2 % → 2 % | 12.6 px | 0.42 | 1.25 | 141 |
| stroke 162 | 2 % → 2 % | 19.1 px | 0.42 | 0.71 | 52 |
| stroke 163 | 3 % → 1 % | 27.4 px | 0.43 | 0.38 | 88 |
| stroke 164 | 6 % → 2 % | 90.0 px | 0.42 | 0.35 | 38 |
| stroke 165 | 7 % → 2 % | 170.3 px | 0.42 | 0.33 | 19 |
| stroke 166 | 7 % → 2 % | 78.4 px | 0.42 | 0.28 | 51 |
| stroke 167 | 8 % → 2 % | 129.1 px | 0.42 | 0.21 | 39 |
| stroke 168 | 10 % → 2 % | 142.9 px | 0.42 | 0.20 | 21 |
| stroke 169 | 9 % → 3 % | 66.3 px | 0.43 | 0.30 | 97 |
| stroke 170 | 14 % → 2 % | 242.3 px | 0.42 | 0.16 | 29 |
| stroke 171 | 13 % → 1 % | 217.7 px | 0.43 | 0.09 | 35 |
| stroke 172 | 10 % → 3 % | 136.1 px | 0.43 | 0.28 | 49 |
| stroke 173 | 6 % → 3 % | 64.3 px | 0.43 | 0.44 | 57 |
| stroke 174 | 4 % → 7 % | 58.6 px | 0.43 | 1.79 | 19 |
| stroke 175 | 9 % → 4 % | 188.0 px | 0.43 | 0.51 | 15 |
| stroke 176 | 5 % → 8 % | 47.1 px | 0.43 | 1.70 | 43 |
| stroke 177 | 4 % → 9 % | 42.7 px | 0.43 | 2.22 | 28 |
| stroke 178 | 2 % → 1 % | 27.0 px | 0.44 | 0.36 | 24 |
| stroke 179 | 6 % → 10 % | 173.5 px | 0.43 | 1.80 | 9 |
| stroke 180 | 7 % → 7 % | 50.5 px | 0.43 | 1.07 | 68 |
| stroke 181 | 7 % → 4 % | 164.3 px | 0.43 | 0.65 | 9 |
| stroke 182 | 8 % → 4 % | 210.2 px | 0.43 | 0.56 | 8 |
| stroke 183 | 8 % → 7 % | 153.2 px | 0.43 | 0.88 | 14 |
| stroke 184 | 10 % → 7 % | 146.2 px | 0.43 | 0.68 | 19 |
| stroke 185 | 8 % → 9 % | 110.1 px | 0.43 | 1.15 | 45 |
| stroke 186 | 7 % → 4 % | 94.7 px | 0.41 | 0.67 | 25 |
| stroke 187 | 1 % → 4 % | 17.1 px | 0.43 | 4.34 | 14 |
| stroke 188 | 6 % → 8 % | 70.8 px | 0.41 | 1.37 | 41 |
| stroke 189 | 4 % → 5 % | 55.1 px | 0.41 | 1.29 | 34 |
| stroke 190 | 3 % → 6 % | 28.8 px | 0.41 | 1.65 | 71 |
| stroke 191 | 2 % → 12 % | 40.6 px | 0.42 | 5.00 | 44 |
| stroke 192 | 4 % → 11 % | 32.7 px | 0.42 | 2.67 | 94 |
| stroke 193 | 5 % → 8 % | 46.1 px | 0.43 | 1.69 | 25 |
| stroke 194 | 1 % → 1 % | 21.9 px | 0.43 | 0.93 | 32 |
| stroke 195 | 3 % → 1 % | 22.6 px | 0.43 | 0.29 | 101 |
| stroke 196 | 7 % → 1 % | 74.2 px | 0.43 | 0.17 | 53 |
| stroke 197 | 5 % → 3 % | 47.2 px | 0.42 | 0.65 | 80 |
| stroke 198 | 6 % → 3 % | 113.9 px | 0.41 | 0.57 | 24 |
| stroke 199 | 1 % → 1 % | 25.2 px | 0.43 | 1.00 | 7 |
| stroke 200 | 1 % → 1 % | 35.4 px | 0.41 | 0.84 | 12 |
| stroke 201 | 3 % → 1 % | 44.6 px | 0.43 | 0.17 | 35 |
| stroke 202 | 1 % → 5 % | 31.8 px | 0.41 | 3.74 | 12 |
| stroke 203 | 1 % → 6 % | 16.9 px | 0.40 | 8.21 | 9 |
| stroke 204 | 2 % → 3 % | 25.8 px | 0.39 | 1.72 | 15 |
| stroke 205 | 1 % → 1 % | 30.2 px | 0.42 | 0.53 | 40 |
| stroke 206 | 3 % → 0 % | 72.1 px | 0.41 | 0.14 | 29 |
| stroke 207 | 3 % → 0 % | 86.6 px | 0.43 | 0.09 | 34 |
| stroke 208 | 4 % → 1 % | 71.0 px | 0.44 | 0.22 | 71 |
| stroke 209 | 5 % → 2 % | 82.3 px | 0.44 | 0.38 | 73 |
| stroke 210 | 6 % → 3 % | 88.9 px | 0.44 | 0.53 | 69 |
| stroke 211 | 7 % → 4 % | 76.2 px | 0.43 | 0.52 | 114 |
| stroke 212 | 8 % → 4 % | 76.1 px | 0.43 | 0.42 | 139 |
| stroke 213 | 9 % → 3 % | 75.9 px | 0.43 | 0.36 | 177 |
| stroke 214 | 12 % → 4 % | 159.6 px | 0.43 | 0.33 | 88 |
| stroke 215 | 11 % → 4 % | 69.8 px | 0.43 | 0.37 | 388 |
| stroke 216 | 11 % → 3 % | 65.1 px | 0.43 | 0.28 | 421 |
| stroke 217 | 13 % → 2 % | 128.9 px | 0.43 | 0.17 | 237 |
| stroke 218 | 4 % → 5 % | 40.1 px | 0.43 | 1.36 | 114 |
| stroke 219 | 7 % → 4 % | 40.0 px | 0.43 | 0.52 | 383 |
| stroke 220 | 9 % → 3 % | 46.8 px | 0.43 | 0.37 | 547 |
| stroke 221 | 13 % → 4 % | 68.0 px | 0.43 | 0.29 | 505 |
| stroke 222 | 19 % → 4 % | 134.8 px | 0.43 | 0.23 | 637 |
| stroke 223 | 27 % → 6 % | 705.9 px | 0.43 | 0.22 | 35 |
| stroke 224 | 16 % → 3 % | 110.3 px | 0.43 | 0.18 | 505 |
| stroke 225 | 20 % → 5 % | 119.7 px | 0.43 | 0.26 | 504 |
| stroke 226 | 18 % → 5 % | 114.3 px | 0.43 | 0.26 | 409 |
| stroke 227 | 18 % → 3 % | 138.9 px | 0.43 | 0.17 | 279 |
| stroke 228 | 17 % → 1 % | 462.1 px | 0.44 | 0.07 | 31 |
| stroke 229 | 17 % → 3 % | 193.1 px | 0.44 | 0.18 | 98 |
| stroke 230 | 18 % → 4 % | 230.6 px | 0.43 | 0.22 | 94 |
| stroke 231 | 19 % → 4 % | 181.0 px | 0.43 | 0.22 | 146 |
| stroke 232 | 8 % → 6 % | 128.9 px | 0.41 | 0.84 | 65 |
| stroke 233 | 17 % → 7 % | 113.3 px | 0.42 | 0.41 | 394 |
| stroke 234 | 19 % → 7 % | 158.3 px | 0.42 | 0.39 | 190 |
| stroke 235 | 20 % → 7 % | 169.5 px | 0.42 | 0.36 | 149 |
| stroke 236 | 28 % → 4 % | 570.9 px | 0.43 | 0.14 | 71 |
| stroke 237 | 20 % → 7 % | 283.9 px | 0.41 | 0.37 | 75 |
| stroke 238 | 21 % → 7 % | 559.2 px | 0.42 | 0.33 | 31 |
| stroke 239 | 22 % → 7 % | 600.0 px | 0.42 | 0.32 | 38 |
| stroke 240 | 21 % → 10 % | 439.8 px | 0.42 | 0.46 | 42 |
| stroke 241 | 21 % → 11 % | 317.2 px | 0.42 | 0.51 | 73 |
| stroke 242 | 21 % → 12 % | 175.6 px | 0.42 | 0.55 | 146 |
| stroke 243 | 21 % → 12 % | 182.5 px | 0.42 | 0.54 | 151 |
| stroke 244 | 21 % → 10 % | 301.9 px | 0.42 | 0.48 | 87 |
| stroke 245 | 20 % → 7 % | 142.8 px | 0.42 | 0.36 | 347 |
| stroke 246 | 23 % → 10 % | 147.7 px | 0.42 | 0.42 | 391 |
| stroke 247 | 29 % → 7 % | 184.4 px | 0.43 | 0.24 | 737 |
| stroke 248 | 35 % → 3 % | 211.3 px | 0.43 | 0.10 | 618 |
| stroke 249 | 28 % → 6 % | 177.3 px | 0.42 | 0.22 | 555 |
| stroke 250 | 28 % → 7 % | 1556.3 px | 0.41 | 0.26 | 29 |
| stroke 251 | 44 % → 9 % | 934.1 px | 0.43 | 0.20 | 62 |
| stroke 252 | 46 % → 5 % | 692.4 px | 0.43 | 0.10 | 132 |
| stroke 253 | 40 % → 9 % | 676.8 px | 0.43 | 0.22 | 96 |
| stroke 254 | 1 % → 2 % | 11.8 px | 0.42 | 3.35 | 20 |
| stroke 255 | 1 % → 2 % | 18.0 px | 0.42 | 1.46 | 24 |
| stroke 256 | 1 % → 4 % | 11.1 px | 0.43 | 3.71 | 38 |
| stroke 257 | 3 % → 3 % | 14.0 px | 0.43 | 1.25 | 164 |
| stroke 258 | 3 % → 7 % | 26.9 px | 0.43 | 2.27 | 138 |
| stroke 259 | 6 % → 7 % | 38.5 px | 0.43 | 1.27 | 124 |
| stroke 260 | 8 % → 9 % | 211.8 px | 0.43 | 1.15 | 9 |
| stroke 261 | 3 % → 5 % | 74.1 px | 0.42 | 1.49 | 8 |
| stroke 262 | 4 % → 7 % | 23.5 px | 0.42 | 1.75 | 309 |
| stroke 263 | 1 % → 7 % | 21.3 px | 0.43 | 5.14 | 31 |
| stroke 264 | 4 % → 8 % | 64.9 px | 0.43 | 2.29 | 48 |
| stroke 265 | 5 % → 6 % | 52.8 px | 0.43 | 1.35 | 42 |
| stroke 266 | 5 % → 10 % | 64.0 px | 0.42 | 1.90 | 31 |
| stroke 267 | 0 % → 1 % | 10.6 px | 0.43 | 3.96 | 34 |
| stroke 268 | 3 % → 9 % | 31.6 px | 0.41 | 2.58 | 256 |
| stroke 269 | 9 % → 12 % | 167.3 px | 0.42 | 1.46 | 32 |
| stroke 270 | 6 % → 9 % | 33.2 px | 0.41 | 1.51 | 108 |
| stroke 271 | 9 % → 12 % | 121.7 px | 0.41 | 1.35 | 46 |
| stroke 272 | 1 % → 1 % | 20.5 px | 0.43 | 1.35 | 14 |
| stroke 273 | 6 % → 7 % | 57.8 px | 0.41 | 1.14 | 41 |
| stroke 274 | 5 % → 6 % | 122.4 px | 0.41 | 1.17 | 11 |
| stroke 275 | 1 % → 1 % | 12.1 px | 0.39 | 1.66 | 7 |
| stroke 276 | 1 % → 2 % | 27.0 px | 0.41 | 1.36 | 10 |

Numbers say: wet paint spreads well beyond the stroke.

## Refs v3 · #22 Wasilewski brush poster — own sheet
own sheet 800 × 1633 · Ink 0.98 · 64 px · 379.0 s

![Refs v3 · #22 Wasilewski brush poster — own sheet](Refs-v3-22-Wasilewski-brush-poster-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 3 % → 39 % | 97.0 px | 0.92 | 14.88 | 121 |
| stroke 2 | 4 % → 69 % | 99.4 px | 0.92 | 17.72 | 50 |
| stroke 3 | 10 % → 77 % | 41.8 px | 0.92 | 7.41 | 440 |
| stroke 4 | 2 % → 48 % | 105.3 px | 0.92 | 19.24 | 57 |
| stroke 5 | 4 % → 53 % | 58.9 px | 0.93 | 13.61 | 270 |
| stroke 6 | 3 % → 34 % | 81.8 px | 0.93 | 11.35 | 133 |
| stroke 7 | 2 % → 37 % | 59.9 px | 0.92 | 20.28 | 61 |
| stroke 8 | 6 % → 58 % | 223.1 px | 0.92 | 9.70 | 42 |
| stroke 9 | 6 % → 27 % | 196.0 px | 0.92 | 4.44 | 48 |
| stroke 10 | 6 % → 38 % | 163.1 px | 0.92 | 6.73 | 95 |
| stroke 11 | 9 % → 29 % | 123.1 px | 0.92 | 3.22 | 238 |
| stroke 12 | 7 % → 55 % | 168.3 px | 0.92 | 8.07 | 84 |
| stroke 13 | 8 % → 44 % | 327.9 px | 0.92 | 5.33 | 92 |
| stroke 14 | 9 % → 34 % | 288.3 px | 0.93 | 3.69 | 76 |
| stroke 15 | 3 % → 14 % | 98.8 px | 0.92 | 4.29 | 43 |
| stroke 16 | 6 % → 34 % | 274.0 px | 0.93 | 5.51 | 28 |
| stroke 17 | 14 % → 47 % | 122.6 px | 0.92 | 3.41 | 164 |
| stroke 18 | 3 % → 43 % | 82.6 px | 0.93 | 13.89 | 101 |
| stroke 19 | 1 % → 38 % | 56.5 px | 0.93 | 30.38 | 25 |
| stroke 20 | 9 % → 34 % | 106.3 px | 0.92 | 3.85 | 535 |
| stroke 21 | 15 % → 50 % | 301.0 px | 0.92 | 3.35 | 356 |
| stroke 22 | 4 % → 34 % | 128.0 px | 0.92 | 8.20 | 108 |
| stroke 23 | 16 % → 29 % | 93.4 px | 0.91 | 1.78 | 1834 |
| stroke 24 | 18 % → 70 % | 719.3 px | 0.92 | 3.80 | 70 |
| stroke 25 | 5 % → 25 % | 171.6 px | 0.92 | 4.72 | 100 |
| stroke 26 | 4 % → 13 % | 142.9 px | 0.92 | 3.50 | 79 |
| stroke 27 | 2 % → 23 % | 70.2 px | 0.92 | 12.51 | 112 |
| stroke 28 | 8 % → 39 % | 217.3 px | 0.92 | 4.62 | 257 |
| stroke 29 | 12 % → 44 % | 435.1 px | 0.93 | 3.78 | 151 |
| stroke 30 | 6 % → 25 % | 71.7 px | 0.92 | 4.27 | 466 |
| stroke 31 | 7 % → 23 % | 179.8 px | 0.92 | 3.23 | 201 |
| stroke 32 | 13 % → 42 % | 232.8 px | 0.92 | 3.20 | 404 |
| stroke 33 | 26 % → 83 % | 413.8 px | 0.92 | 3.18 | 106 |
| stroke 34 | 8 % → 25 % | 146.2 px | 0.92 | 3.02 | 249 |
| stroke 35 | 10 % → 22 % | 221.8 px | 0.92 | 2.22 | 111 |
| stroke 36 | 7 % → 30 % | 110.5 px | 0.93 | 4.19 | 259 |
| stroke 37 | 10 % → 27 % | 115.1 px | 0.93 | 2.67 | 627 |
| stroke 38 | 16 % → 22 % | 104.9 px | 0.93 | 1.42 | 2073 |
| stroke 39 | 17 % → 42 % | 180.9 px | 0.92 | 2.46 | 679 |
| stroke 40 | 12 % → 25 % | 459.9 px | 0.92 | 2.10 | 43 |
| stroke 41 | 23 % → 38 % | 244.2 px | 0.93 | 1.69 | 942 |
| stroke 42 | 12 % → 24 % | 217.5 px | 0.92 | 1.96 | 195 |
| stroke 43 | 18 % → 38 % | 258.3 px | 0.92 | 2.08 | 276 |
| stroke 44 | 16 % → 16 % | 175.8 px | 0.93 | 1.00 | 450 |
| stroke 45 | 21 % → 41 % | 230.6 px | 0.92 | 1.93 | 714 |
| stroke 46 | 28 % → 72 % | 722.8 px | 0.92 | 2.58 | 87 |
| stroke 47 | 22 % → 44 % | 1005.2 px | 0.92 | 1.97 | 39 |
| stroke 48 | 15 % → 25 % | 416.5 px | 0.92 | 1.63 | 94 |
| stroke 49 | 18 % → 48 % | 288.3 px | 0.92 | 2.72 | 128 |
| stroke 50 | 23 % → 50 % | 972.5 px | 0.92 | 2.15 | 71 |
| stroke 51 | 39 % → 77 % | 844.9 px | 0.92 | 1.99 | 155 |
| stroke 52 | 11 % → 28 % | 149.2 px | 0.93 | 2.47 | 225 |
| stroke 53 | 36 % → 73 % | 656.5 px | 0.92 | 2.00 | 191 |
| stroke 54 | 39 % → 72 % | 627.2 px | 0.92 | 1.86 | 100 |
| stroke 55 | 29 % → 45 % | 256.0 px | 0.92 | 1.54 | 801 |
| stroke 56 | 25 % → 53 % | 556.9 px | 0.92 | 2.11 | 513 |
| stroke 57 | 30 % → 54 % | 510.8 px | 0.92 | 1.80 | 396 |
| stroke 58 | 19 % → 24 % | 317.8 px | 0.92 | 1.25 | 479 |
| stroke 59 | 12 % → 52 % | 146.7 px | 0.93 | 4.35 | 2926 |
| stroke 60 | 18 % → 24 % | 276.0 px | 0.92 | 1.29 | 332 |
| stroke 61 | 27 % → 39 % | 359.2 px | 0.92 | 1.44 | 719 |
| stroke 62 | 17 % → 29 % | 224.4 px | 0.92 | 1.71 | 659 |
| stroke 63 | 45 % → 79 % | 691.7 px | 0.93 | 1.77 | 439 |
| stroke 64 | 31 % → 46 % | 189.6 px | 0.93 | 1.50 | 2574 |
| stroke 65 | 19 % → 26 % | 605.3 px | 0.92 | 1.40 | 166 |
| stroke 66 | 26 % → 37 % | 461.0 px | 0.92 | 1.39 | 512 |
| stroke 67 | 18 % → 24 % | 594.1 px | 0.93 | 1.28 | 150 |
| stroke 68 | 21 % → 28 % | 427.2 px | 0.92 | 1.30 | 374 |
| stroke 69 | 6 % → 16 % | 252.8 px | 0.92 | 2.51 | 129 |
| stroke 70 | 35 % → 37 % | 417.1 px | 0.93 | 1.04 | 533 |
| stroke 71 | 23 % → 36 % | 1017.1 px | 0.92 | 1.57 | 45 |
| stroke 72 | 52 % → 72 % | 1004.8 px | 0.92 | 1.41 | 189 |
| stroke 73 | 44 % → 56 % | 510.9 px | 0.92 | 1.27 | 584 |
| stroke 74 | 58 % → 71 % | 1496.5 px | 0.92 | 1.22 | 263 |
| stroke 75 | 64 % → 81 % | 760.1 px | 0.92 | 1.27 | 178 |
| stroke 76 | 46 % → 59 % | 607.3 px | 0.92 | 1.28 | 410 |
| stroke 77 | 17 % → 24 % | 546.3 px | 0.92 | 1.40 | 75 |
| stroke 78 | 29 % → 44 % | 311.2 px | 0.92 | 1.52 | 468 |
| stroke 79 | 51 % → 64 % | 794.7 px | 0.92 | 1.27 | 84 |
| stroke 80 | 74 % → 85 % | 702.4 px | 0.92 | 1.15 | 227 |
| stroke 81 | 66 % → 72 % | 391.3 px | 0.93 | 1.09 | 484 |
| stroke 82 | 35 % → 56 % | 1014.2 px | 0.92 | 1.57 | 132 |
| stroke 83 | 35 % → 45 % | 604.7 px | 0.92 | 1.31 | 131 |
| stroke 84 | 30 % → 33 % | 433.7 px | 0.92 | 1.08 | 217 |
| stroke 85 | 6 % → 15 % | 153.2 px | 0.92 | 2.57 | 70 |
| stroke 86 | 38 % → 39 % | 315.9 px | 0.92 | 1.04 | 749 |
| stroke 87 | 48 % → 61 % | 977.6 px | 0.92 | 1.25 | 253 |
| stroke 88 | 23 % → 27 % | 398.9 px | 0.92 | 1.15 | 230 |
| stroke 89 | 35 % → 36 % | 573.6 px | 0.93 | 1.02 | 252 |
| stroke 90 | 18 % → 23 % | 479.9 px | 0.91 | 1.27 | 104 |
| stroke 91 | 29 % → 35 % | 410.1 px | 0.92 | 1.20 | 242 |
| stroke 92 | 20 % → 23 % | 566.8 px | 0.92 | 1.18 | 102 |
| stroke 93 | 19 % → 22 % | 674.6 px | 0.92 | 1.14 | 150 |
| stroke 94 | 43 % → 46 % | 331.1 px | 0.92 | 1.07 | 767 |
| stroke 95 | 37 % → 37 % | 858.7 px | 0.92 | 1.00 | 161 |
| stroke 96 | 65 % → 69 % | 827.1 px | 0.92 | 1.05 | 264 |
| stroke 97 | 23 % → 26 % | 878.9 px | 0.91 | 1.10 | 81 |
| stroke 98 | 23 % → 23 % | 544.5 px | 0.92 | 1.03 | 106 |
| stroke 99 | 49 % → 50 % | 852.1 px | 0.92 | 1.01 | 164 |
| stroke 100 | 16 % → 19 % | 246.3 px | 0.92 | 1.17 | 366 |
| stroke 101 | 37 % → 38 % | 458.5 px | 0.93 | 1.04 | 171 |
| stroke 102 | 16 % → 17 % | 268.9 px | 0.92 | 1.04 | 196 |
| stroke 103 | 22 % → 22 % | 746.2 px | 0.91 | 1.00 | 56 |
| stroke 104 | 33 % → 33 % | 280.5 px | 0.93 | 1.00 | 599 |
| stroke 105 | 40 % → 40 % | 1782.1 px | 0.93 | 1.00 | 30 |
| stroke 106 | 47 % → 47 % | 1690.0 px | 0.92 | 1.00 | 79 |
| stroke 107 | 24 % → 23 % | 807.1 px | 0.92 | 1.00 | 81 |
| stroke 108 | 32 % → 32 % | 238.5 px | 0.93 | 1.00 | 736 |
| stroke 109 | 8 % → 26 % | 50.8 px | 0.93 | 3.18 | 216 |
| stroke 110 | 6 % → 28 % | 36.6 px | 0.91 | 4.70 | 126 |
| stroke 111 | 12 % → 33 % | 276.4 px | 0.93 | 2.82 | 35 |
| stroke 112 | 15 % → 26 % | 128.8 px | 0.92 | 1.68 | 486 |
| stroke 113 | 21 % → 21 % | 86.3 px | 0.92 | 1.00 | 2350 |

Numbers say: wet paint spreads well beyond the stroke.

## Refs v3 · #23 Report dry white mask — own sheet
own sheet 800 × 804 · Ink 0.93 · Gouache 0.07 · 89 px · 426.7 s

![Refs v3 · #23 Report dry white mask — own sheet](Refs-v3-23-Report-dry-white-mask-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 9 % → 22 % | 84.3 px | 0.53 | 2.43 | 1223 |
| stroke 2 | 13 % → 19 % | 102.4 px | 0.53 | 1.50 | 3059 |
| stroke 3 | 17 % → 23 % | 139.7 px | 0.53 | 1.38 | 3354 |
| stroke 4 | 20 % → 30 % | 253.5 px | 0.53 | 1.49 | 3046 |
| stroke 5 | 37 % → 20 % | 489.9 px | 0.53 | 0.52 | 1066 |
| stroke 6 | 22 % → 31 % | 258.4 px | 0.53 | 1.42 | 2422 |
| stroke 7 | 36 % → 21 % | 844.3 px | 0.53 | 0.57 | 511 |
| stroke 8 | 23 % → 29 % | 247.0 px | 0.53 | 1.25 | 4530 |
| stroke 9 | 23 % → 24 % | 259.3 px | 0.53 | 1.06 | 3006 |
| stroke 10 | 44 % → 38 % | 747.3 px | 0.53 | 0.86 | 1029 |
| stroke 11 | 22 % → 22 % | 391.5 px | 0.52 | 1.01 | 1129 |
| stroke 12 | 37 % → 36 % | 589.9 px | 0.53 | 0.98 | 1381 |
| stroke 13 | 23 % → 22 % | 284.2 px | 0.52 | 0.98 | 1533 |
| stroke 14 | 34 % → 40 % | 509.3 px | 0.53 | 1.18 | 1170 |
| stroke 15 | 24 % → 21 % | 274.8 px | 0.52 | 0.89 | 1739 |
| stroke 16 | 35 % → 33 % | 450.6 px | 0.53 | 0.95 | 3022 |
| stroke 17 | 30 % → 23 % | 301.5 px | 0.52 | 0.75 | 2472 |
| stroke 18 | 42 % → 30 % | 868.6 px | 0.52 | 0.71 | 837 |
| stroke 19 | 34 % → 35 % | 909.4 px | 0.53 | 1.05 | 736 |
| stroke 20 | 44 % → 24 % | 368.1 px | 0.53 | 0.55 | 4377 |
| stroke 21 | 48 % → 25 % | 409.4 px | 0.53 | 0.52 | 2936 |
| stroke 22 | 45 % → 26 % | 400.7 px | 0.53 | 0.57 | 2483 |
| stroke 23 | 39 % → 21 % | 560.9 px | 0.53 | 0.53 | 1352 |
| stroke 24 | 51 % → 18 % | 265.4 px | 0.53 | 0.35 | 8830 |
| stroke 25 | 50 % → 27 % | 424.7 px | 0.53 | 0.54 | 25253 |
| stroke 26 | 56 % → 33 % | 410.4 px | 0.53 | 0.59 | 6876 |
| stroke 27 | 58 % → 23 % | 483.3 px | 0.53 | 0.40 | 5407 |
| stroke 28 | 60 % → 23 % | 427.6 px | 0.53 | 0.38 | 4705 |
| stroke 29 | 55 % → 23 % | 322.0 px | 0.53 | 0.43 | 6005 |
| stroke 30 | 56 % → 22 % | 361.4 px | 0.52 | 0.38 | 8041 |
| stroke 31 | 55 % → 28 % | 427.9 px | 0.53 | 0.51 | 4839 |
| stroke 32 | 62 % → 17 % | 1684.8 px | 0.53 | 0.28 | 293 |
| stroke 33 | 89 % → 31 % | 2341.1 px | 0.52 | 0.35 | 558 |
| stroke 34 | 57 % → 30 % | 1197.5 px | 0.53 | 0.53 | 725 |
| stroke 35 | 59 % → 32 % | 933.2 px | 0.53 | 0.54 | 1359 |
| stroke 36 | 62 % → 20 % | 741.9 px | 0.53 | 0.32 | 1711 |
| stroke 37 | 67 % → 22 % | 481.0 px | 0.53 | 0.33 | 4695 |
| stroke 38 | 1 % → 25 % | 38.9 px | 0.52 | 21.24 | 142 |
| stroke 39 | 2 % → 23 % | 44.2 px | 0.52 | 11.76 | 216 |
| stroke 40 | 3 % → 24 % | 180.2 px | 0.52 | 7.87 | 67 |
| stroke 41 | 4 % → 33 % | 51.0 px | 0.53 | 7.97 | 652 |
| stroke 42 | 7 % → 25 % | 454.8 px | 0.52 | 3.33 | 51 |
| stroke 43 | 6 % → 32 % | 73.4 px | 0.53 | 5.53 | 569 |
| stroke 44 | 9 % → 25 % | 550.2 px | 0.52 | 2.72 | 67 |
| stroke 45 | 9 % → 41 % | 225.7 px | 0.53 | 4.38 | 236 |
| stroke 46 | 10 % → 26 % | 627.8 px | 0.52 | 2.45 | 32 |
| stroke 47 | 11 % → 40 % | 321.6 px | 0.53 | 3.69 | 154 |
| stroke 48 | 11 % → 26 % | 533.7 px | 0.52 | 2.29 | 65 |
| stroke 49 | 12 % → 38 % | 322.2 px | 0.53 | 3.10 | 165 |
| stroke 50 | 13 % → 27 % | 800.3 px | 0.52 | 2.03 | 36 |
| stroke 51 | 12 % → 29 % | 243.5 px | 0.52 | 2.32 | 261 |
| stroke 52 | 13 % → 24 % | 219.1 px | 0.52 | 1.89 | 352 |
| stroke 53 | 14 % → 41 % | 172.2 px | 0.53 | 2.93 | 883 |
| stroke 54 | 14 % → 24 % | 208.1 px | 0.52 | 1.75 | 618 |
| stroke 55 | 14 % → 24 % | 189.2 px | 0.52 | 1.64 | 718 |
| stroke 56 | 15 % → 25 % | 216.7 px | 0.52 | 1.70 | 596 |
| stroke 57 | 15 % → 38 % | 231.9 px | 0.53 | 2.55 | 1227 |
| stroke 58 | 16 % → 45 % | 3956.2 px | 0.53 | 2.74 | 13 |
| stroke 59 | 16 % → 28 % | 237.6 px | 0.53 | 1.78 | 582 |
| stroke 60 | 17 % → 24 % | 227.0 px | 0.52 | 1.39 | 656 |
| stroke 61 | 16 % → 24 % | 230.8 px | 0.52 | 1.52 | 575 |
| stroke 62 | 18 % → 33 % | 311.7 px | 0.53 | 1.80 | 383 |
| stroke 63 | 1 % → 32 % | 33.0 px | 0.54 | 32.87 | 60 |
| stroke 64 | 18 % → 36 % | 1111.7 px | 0.53 | 1.97 | 88 |
| stroke 65 | 5 % → 31 % | 78.9 px | 0.54 | 6.37 | 249 |
| stroke 66 | 17 % → 31 % | 182.0 px | 0.53 | 1.80 | 780 |
| stroke 67 | 8 % → 28 % | 356.1 px | 0.54 | 3.41 | 58 |
| stroke 68 | 24 % → 36 % | 1444.5 px | 0.53 | 1.48 | 62 |
| stroke 69 | 18 % → 30 % | 483.2 px | 0.53 | 1.70 | 167 |
| stroke 70 | 12 % → 28 % | 437.0 px | 0.54 | 2.39 | 70 |
| stroke 71 | 11 % → 27 % | 682.0 px | 0.54 | 2.55 | 25 |
| stroke 72 | 26 % → 36 % | 1585.2 px | 0.53 | 1.38 | 52 |
| stroke 73 | 12 % → 26 % | 264.7 px | 0.54 | 2.10 | 118 |
| stroke 74 | 26 % → 35 % | 1225.2 px | 0.53 | 1.32 | 103 |
| stroke 75 | 13 % → 24 % | 590.7 px | 0.54 | 1.80 | 39 |
| stroke 76 | 26 % → 34 % | 1013.7 px | 0.53 | 1.30 | 169 |
| stroke 77 | 17 % → 25 % | 453.4 px | 0.54 | 1.49 | 100 |
| stroke 78 | 26 % → 31 % | 738.7 px | 0.53 | 1.22 | 210 |
| stroke 79 | 21 % → 27 % | 687.5 px | 0.53 | 1.28 | 75 |
| stroke 80 | 24 % → 28 % | 496.6 px | 0.53 | 1.16 | 271 |
| stroke 81 | 18 % → 29 % | 162.6 px | 0.54 | 1.62 | 423 |
| stroke 82 | 18 % → 24 % | 176.9 px | 0.54 | 1.38 | 473 |
| stroke 83 | 23 % → 25 % | 259.3 px | 0.53 | 1.11 | 522 |
| stroke 84 | 23 % → 28 % | 272.8 px | 0.53 | 1.22 | 416 |
| stroke 85 | 25 % → 28 % | 357.0 px | 0.53 | 1.09 | 707 |
| stroke 86 | 29 % → 30 % | 317.3 px | 0.53 | 1.06 | 958 |
| stroke 87 | 28 % → 29 % | 354.2 px | 0.53 | 1.04 | 973 |
| stroke 88 | 27 % → 34 % | 339.9 px | 0.53 | 1.27 | 721 |
| stroke 89 | 23 % → 31 % | 494.6 px | 0.54 | 1.37 | 223 |
| stroke 90 | 2 % → 16 % | 35.9 px | 0.54 | 8.22 | 93 |
| stroke 91 | 6 % → 14 % | 53.7 px | 0.53 | 2.36 | 327 |
| stroke 92 | 9 % → 15 % | 75.6 px | 0.53 | 1.75 | 424 |
| stroke 93 | 13 % → 18 % | 523.6 px | 0.53 | 1.42 | 69 |
| stroke 94 | 11 % → 25 % | 190.7 px | 0.53 | 2.17 | 119 |
| stroke 95 | 16 % → 19 % | 675.0 px | 0.53 | 1.22 | 53 |
| stroke 96 | 17 % → 20 % | 769.8 px | 0.53 | 1.17 | 61 |
| stroke 97 | 11 % → 17 % | 108.1 px | 0.53 | 1.56 | 464 |
| stroke 98 | 17 % → 18 % | 182.7 px | 0.53 | 1.07 | 498 |
| stroke 99 | 18 % → 18 % | 181.9 px | 0.53 | 1.04 | 481 |
| stroke 100 | 14 % → 18 % | 120.3 px | 0.53 | 1.32 | 482 |
| stroke 101 | 4 % → 16 % | 41.4 px | 0.53 | 3.82 | 698 |
| stroke 102 | 7 % → 21 % | 277.0 px | 0.54 | 2.80 | 151 |
| stroke 103 | 8 % → 18 % | 91.8 px | 0.53 | 2.23 | 484 |
| stroke 104 | 10 % → 21 % | 561.4 px | 0.54 | 2.16 | 81 |
| stroke 105 | 11 % → 21 % | 190.0 px | 0.53 | 1.86 | 220 |
| stroke 106 | 12 % → 23 % | 1032.9 px | 0.54 | 1.90 | 40 |
| stroke 107 | 14 % → 22 % | 311.1 px | 0.53 | 1.62 | 157 |
| stroke 108 | 14 % → 24 % | 818.5 px | 0.54 | 1.76 | 69 |
| stroke 109 | 16 % → 24 % | 481.1 px | 0.53 | 1.48 | 116 |
| stroke 110 | 17 % → 26 % | 549.1 px | 0.53 | 1.50 | 109 |
| stroke 111 | 21 % → 27 % | 766.6 px | 0.53 | 1.30 | 127 |
| stroke 112 | 22 % → 26 % | 252.5 px | 0.53 | 1.18 | 497 |
| stroke 113 | 19 % → 21 % | 222.2 px | 0.53 | 1.11 | 506 |
| stroke 114 | 24 % → 25 % | 311.0 px | 0.53 | 1.07 | 686 |
| stroke 115 | 22 % → 25 % | 285.6 px | 0.53 | 1.13 | 709 |
| stroke 116 | 18 % → 20 % | 216.0 px | 0.53 | 1.16 | 828 |
| stroke 117 | 19 % → 20 % | 461.3 px | 0.53 | 1.04 | 255 |
| stroke 118 | 20 % → 22 % | 272.6 px | 0.53 | 1.12 | 706 |
| stroke 119 | 22 % → 23 % | 287.5 px | 0.53 | 1.03 | 756 |
| stroke 120 | 18 % → 19 % | 219.8 px | 0.53 | 1.06 | 771 |
| stroke 121 | 20 % → 22 % | 1245.2 px | 0.54 | 1.09 | 70 |
| stroke 122 | 3 % → 18 % | 67.9 px | 0.53 | 5.76 | 98 |
| stroke 123 | 3 % → 24 % | 154.6 px | 0.53 | 6.98 | 19 |
| stroke 124 | 7 % → 16 % | 51.5 px | 0.53 | 2.38 | 512 |
| stroke 125 | 7 % → 17 % | 576.0 px | 0.53 | 2.35 | 22 |
| stroke 126 | 10 % → 19 % | 68.6 px | 0.53 | 1.99 | 380 |
| stroke 127 | 9 % → 16 % | 687.9 px | 0.53 | 1.81 | 41 |
| stroke 128 | 21 % → 31 % | 337.9 px | 0.53 | 1.44 | 78 |
| stroke 129 | 10 % → 16 % | 876.5 px | 0.53 | 1.59 | 24 |
| stroke 130 | 10 % → 15 % | 866.6 px | 0.53 | 1.50 | 48 |
| stroke 131 | 11 % → 15 % | 665.5 px | 0.53 | 1.40 | 43 |
| stroke 132 | 12 % → 16 % | 1010.0 px | 0.53 | 1.31 | 45 |
| stroke 133 | 13 % → 16 % | 823.5 px | 0.53 | 1.23 | 58 |
| stroke 134 | 16 % → 20 % | 115.1 px | 0.53 | 1.30 | 496 |
| stroke 135 | 12 % → 15 % | 129.2 px | 0.53 | 1.25 | 1058 |
| stroke 136 | 17 % → 18 % | 188.5 px | 0.53 | 1.07 | 528 |
| stroke 137 | 16 % → 17 % | 181.4 px | 0.53 | 1.05 | 651 |
| stroke 138 | 18 % → 18 % | 150.7 px | 0.53 | 1.04 | 488 |
| stroke 139 | 25 % → 26 % | 253.7 px | 0.53 | 1.03 | 215 |

Numbers say: wet paint spreads well beyond the stroke.

## Refs v3 · #24 Picasso flat oil — own sheet
own sheet 800 × 1156 · Gouache 1.00 + turpentine 20 % · 51 px · 2523.1 s

![Refs v3 · #24 Picasso flat oil — own sheet](Refs-v3-24-Picasso-flat-oil-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 8 % → 74 % | 50.5 px | 0.12 | 9.55 | 188 |
| stroke 2 | 8 % → 95 % | 52.4 px | 0.41 | 11.45 | 644 |
| stroke 3 | 16 % → 90 % | 88.8 px | 0.39 | 5.58 | 879 |
| stroke 4 | 18 % → 96 % | 120.0 px | 0.43 | 5.22 | 746 |
| stroke 5 | 18 % → 95 % | 217.9 px | 0.21 | 5.18 | 200 |
| stroke 6 | 23 % → 94 % | 167.1 px | 0.51 | 4.14 | 654 |
| stroke 7 | 36 % → 93 % | 424.1 px | 0.51 | 2.59 | 582 |
| stroke 8 | 42 % → 92 % | 505.6 px | 0.41 | 2.18 | 219 |
| stroke 9 | 20 % → 90 % | 100.3 px | 0.49 | 4.40 | 836 |
| stroke 10 | 40 % → 97 % | 500.3 px | 0.53 | 2.43 | 344 |
| stroke 11 | 28 % → 95 % | 130.7 px | 0.50 | 3.38 | 1281 |
| stroke 12 | 38 % → 89 % | 282.3 px | 0.35 | 2.37 | 623 |
| stroke 13 | 41 % → 99 % | 254.7 px | 0.53 | 2.42 | 886 |
| stroke 14 | 43 % → 90 % | 366.7 px | 0.45 | 2.08 | 854 |
| stroke 15 | 36 % → 99 % | 213.3 px | 0.50 | 2.74 | 928 |
| stroke 16 | 39 % → 98 % | 242.3 px | 0.51 | 2.49 | 790 |
| stroke 17 | 47 % → 94 % | 620.4 px | 0.48 | 1.97 | 194 |
| stroke 18 | 56 % → 91 % | 560.7 px | 0.50 | 1.63 | 349 |
| stroke 19 | 55 % → 97 % | 476.5 px | 0.49 | 1.78 | 492 |
| stroke 20 | 30 % → 84 % | 227.7 px | 0.21 | 2.82 | 391 |
| stroke 21 | 39 % → 99 % | 274.1 px | 0.50 | 2.55 | 564 |
| stroke 22 | 61 % → 99 % | 716.6 px | 0.54 | 1.62 | 326 |
| stroke 23 | 56 % → 94 % | 587.3 px | 0.39 | 1.67 | 380 |
| stroke 24 | 54 % → 90 % | 479.4 px | 0.46 | 1.65 | 378 |
| stroke 25 | 42 % → 97 % | 358.4 px | 0.51 | 2.28 | 462 |
| stroke 26 | 60 % → 92 % | 745.4 px | 0.52 | 1.54 | 271 |
| stroke 27 | 47 % → 96 % | 252.6 px | 0.47 | 2.02 | 1123 |
| stroke 28 | 39 % → 99 % | 201.6 px | 0.44 | 2.53 | 1047 |
| stroke 29 | 48 % → 95 % | 447.1 px | 0.46 | 2.00 | 458 |
| stroke 30 | 67 % → 98 % | 579.4 px | 0.49 | 1.48 | 508 |
| stroke 31 | 42 % → 93 % | 387.3 px | 0.41 | 2.22 | 371 |
| stroke 32 | 40 % → 92 % | 424.8 px | 0.40 | 2.28 | 450 |
| stroke 33 | 58 % → 99 % | 512.8 px | 0.46 | 1.71 | 494 |
| stroke 34 | 14 % → 79 % | 51.3 px | 0.53 | 5.63 | 1055 |
| stroke 35 | 26 % → 81 % | 122.1 px | 0.55 | 3.14 | 706 |
| stroke 36 | 32 % → 94 % | 101.5 px | 0.47 | 2.93 | 1401 |
| stroke 37 | 37 % → 76 % | 183.8 px | 0.57 | 2.05 | 837 |
| stroke 38 | 57 % → 91 % | 197.1 px | 0.56 | 1.61 | 1026 |
| stroke 39 | 67 % → 95 % | 461.7 px | 0.54 | 1.42 | 361 |
| stroke 40 | 63 % → 90 % | 424.7 px | 0.57 | 1.44 | 497 |
| stroke 41 | 39 % → 73 % | 146.1 px | 0.52 | 1.88 | 896 |
| stroke 42 | 60 % → 70 % | 316.1 px | 0.59 | 1.15 | 376 |
| stroke 43 | 63 % → 78 % | 433.2 px | 0.57 | 1.23 | 480 |
| stroke 44 | 21 % → 91 % | 156.8 px | 0.40 | 4.27 | 235 |
| stroke 45 | 87 % → 95 % | 404.3 px | 0.58 | 1.09 | 308 |
| stroke 46 | 51 % → 82 % | 414.5 px | 0.53 | 1.61 | 498 |
| stroke 47 | 82 % → 94 % | 287.8 px | 0.57 | 1.14 | 436 |
| stroke 48 | 83 % → 91 % | 376.0 px | 0.58 | 1.09 | 617 |
| stroke 49 | 97 % → 94 % | 270.4 px | 0.59 | 0.97 | 372 |
| stroke 50 | 49 % → 86 % | 296.6 px | 0.50 | 1.74 | 674 |
| stroke 51 | 67 % → 96 % | 460.7 px | 0.52 | 1.42 | 334 |
| stroke 52 | 78 % → 80 % | 746.5 px | 0.58 | 1.03 | 358 |
| stroke 53 | 66 % → 85 % | 489.1 px | 0.54 | 1.28 | 477 |
| stroke 54 | 80 % → 96 % | 793.3 px | 0.55 | 1.19 | 241 |
| stroke 55 | 96 % → 94 % | 818.3 px | 0.58 | 0.98 | 264 |
| stroke 56 | 97 % → 95 % | 336.1 px | 0.58 | 0.98 | 448 |
| stroke 57 | 97 % → 95 % | 605.0 px | 0.58 | 0.98 | 428 |
| stroke 58 | 80 % → 77 % | 657.5 px | 0.59 | 0.96 | 415 |
| stroke 59 | 34 % → 91 % | 276.7 px | 0.43 | 2.70 | 235 |
| stroke 60 | 14 % → 53 % | 48.3 px | 0.47 | 3.65 | 690 |
| stroke 61 | 15 % → 83 % | 72.4 px | 0.39 | 5.39 | 807 |
| stroke 62 | 30 % → 66 % | 88.1 px | 0.43 | 2.19 | 1435 |
| stroke 63 | 35 % → 69 % | 253.3 px | 0.41 | 1.96 | 380 |
| stroke 64 | 46 % → 72 % | 247.1 px | 0.44 | 1.58 | 394 |
| stroke 65 | 39 % → 39 % | 192.3 px | 0.53 | 1.01 | 202 |
| stroke 66 | 41 % → 45 % | 286.4 px | 0.49 | 1.10 | 253 |
| stroke 67 | 39 % → 70 % | 224.0 px | 0.42 | 1.79 | 669 |
| stroke 68 | 9 % → 76 % | 52.0 px | 0.14 | 8.63 | 159 |
| stroke 69 | 11 % → 75 % | 67.7 px | 0.10 | 7.07 | 143 |
| stroke 70 | 11 % → 75 % | 181.8 px | 0.11 | 6.79 | 52 |
| stroke 71 | 15 % → 74 % | 226.9 px | 0.19 | 4.95 | 33 |
| stroke 72 | 13 % → 75 % | 92.2 px | 0.10 | 5.97 | 107 |
| stroke 73 | 14 % → 89 % | 80.3 px | 0.20 | 6.29 | 78 |
| stroke 74 | 12 % → 86 % | 64.4 px | 0.21 | 7.49 | 72 |
| stroke 75 | 19 % → 88 % | 222.2 px | 0.21 | 4.54 | 28 |
| stroke 76 | 23 % → 89 % | 144.4 px | 0.21 | 3.88 | 98 |
| stroke 77 | 18 % → 87 % | 130.1 px | 0.21 | 4.71 | 66 |
| stroke 78 | 20 % → 87 % | 137.6 px | 0.21 | 4.30 | 72 |
| stroke 79 | 22 % → 89 % | 350.5 px | 0.20 | 4.02 | 37 |
| stroke 80 | 23 % → 89 % | 400.1 px | 0.19 | 3.88 | 45 |
| stroke 81 | 26 % → 87 % | 268.3 px | 0.23 | 3.34 | 25 |
| stroke 82 | 31 % → 87 % | 275.7 px | 0.24 | 2.84 | 52 |
| stroke 83 | 30 % → 89 % | 384.4 px | 0.21 | 2.96 | 37 |
| stroke 84 | 18 % → 90 % | 87.5 px | 0.14 | 4.86 | 224 |
| stroke 85 | 19 % → 91 % | 128.7 px | 0.15 | 4.88 | 89 |
| stroke 86 | 25 % → 89 % | 105.1 px | 0.15 | 3.53 | 274 |
| stroke 87 | 16 % → 92 % | 110.3 px | 0.09 | 5.65 | 107 |
| stroke 88 | 27 % → 93 % | 185.4 px | 0.13 | 3.37 | 137 |
| stroke 89 | 39 % → 88 % | 494.8 px | 0.19 | 2.25 | 57 |
| stroke 90 | 36 % → 90 % | 421.6 px | 0.18 | 2.49 | 57 |
| stroke 91 | 23 % → 91 % | 195.3 px | 0.11 | 4.05 | 103 |
| stroke 92 | 25 % → 92 % | 450.7 px | 0.13 | 3.62 | 39 |
| stroke 93 | 34 % → 91 % | 511.6 px | 0.17 | 2.64 | 42 |
| stroke 94 | 45 % → 86 % | 570.3 px | 0.21 | 1.92 | 39 |
| stroke 95 | 37 % → 94 % | 353.7 px | 0.23 | 2.52 | 187 |
| stroke 96 | 40 % → 93 % | 320.9 px | 0.26 | 2.33 | 269 |
| stroke 97 | 43 % → 94 % | 496.5 px | 0.27 | 2.18 | 152 |
| stroke 98 | 44 % → 96 % | 826.9 px | 0.29 | 2.18 | 61 |
| stroke 99 | 56 % → 91 % | 1170.1 px | 0.36 | 1.64 | 53 |
| stroke 100 | 38 % → 83 % | 717.7 px | 0.27 | 2.17 | 39 |
| stroke 101 | 39 % → 84 % | 711.2 px | 0.28 | 2.15 | 56 |
| stroke 102 | 59 % → 96 % | 816.2 px | 0.41 | 1.62 | 132 |
| stroke 103 | 63 % → 95 % | 1201.3 px | 0.46 | 1.51 | 64 |
| stroke 104 | 51 % → 96 % | 1304.8 px | 0.41 | 1.87 | 26 |
| stroke 105 | 51 % → 95 % | 764.4 px | 0.43 | 1.87 | 92 |
| stroke 106 | 56 % → 97 % | 822.4 px | 0.47 | 1.74 | 71 |
| stroke 107 | 62 % → 96 % | 709.0 px | 0.43 | 1.55 | 125 |
| stroke 108 | 4 % → 89 % | 25.2 px | 0.30 | 24.74 | 181 |
| stroke 109 | 7 % → 83 % | 44.1 px | 0.24 | 12.58 | 160 |
| stroke 110 | 8 % → 88 % | 52.7 px | 0.23 | 10.98 | 171 |
| stroke 111 | 10 % → 92 % | 105.6 px | 0.19 | 9.39 | 121 |
| stroke 112 | 14 % → 86 % | 200.4 px | 0.29 | 6.37 | 64 |
| stroke 113 | 8 % → 93 % | 214.0 px | 0.19 | 11.04 | 42 |
| stroke 114 | 15 % → 89 % | 136.4 px | 0.28 | 6.04 | 117 |
| stroke 115 | 11 % → 95 % | 177.0 px | 0.30 | 8.89 | 90 |
| stroke 116 | 15 % → 81 % | 372.7 px | 0.23 | 5.36 | 41 |
| stroke 117 | 16 % → 82 % | 295.5 px | 0.29 | 5.20 | 56 |
| stroke 118 | 17 % → 89 % | 409.7 px | 0.27 | 5.36 | 27 |
| stroke 119 | 17 % → 84 % | 208.2 px | 0.27 | 4.98 | 89 |
| stroke 120 | 9 % → 92 % | 181.4 px | 0.30 | 10.67 | 38 |
| stroke 121 | 12 % → 88 % | 298.8 px | 0.29 | 7.33 | 35 |
| stroke 122 | 8 % → 91 % | 111.2 px | 0.31 | 12.16 | 60 |
| stroke 123 | 11 % → 92 % | 290.0 px | 0.21 | 8.10 | 48 |
| stroke 124 | 16 % → 92 % | 395.5 px | 0.30 | 5.71 | 64 |
| stroke 125 | 13 % → 87 % | 289.3 px | 0.20 | 6.51 | 81 |
| stroke 126 | 16 % → 89 % | 334.1 px | 0.24 | 5.58 | 47 |
| stroke 127 | 78 % → 90 % | 1489.2 px | 0.48 | 1.15 | 52 |
| stroke 128 | 79 % → 90 % | 1000.4 px | 0.49 | 1.14 | 99 |
| stroke 129 | 31 % → 94 % | 298.5 px | 0.32 | 3.04 | 131 |
| stroke 130 | 47 % → 99 % | 340.8 px | 0.43 | 2.09 | 277 |
| stroke 131 | 35 % → 94 % | 464.7 px | 0.34 | 2.67 | 88 |
| stroke 132 | 54 % → 97 % | 1029.3 px | 0.44 | 1.81 | 59 |
| stroke 133 | 40 % → 99 % | 274.9 px | 0.41 | 2.51 | 325 |
| stroke 134 | 58 % → 98 % | 654.6 px | 0.44 | 1.69 | 143 |
| stroke 135 | 52 % → 99 % | 409.2 px | 0.44 | 1.89 | 199 |
| stroke 136 | 40 % → 95 % | 849.1 px | 0.40 | 2.37 | 41 |
| stroke 137 | 26 % → 99 % | 566.2 px | 0.39 | 3.78 | 43 |
| stroke 138 | 60 % → 99 % | 1478.3 px | 0.44 | 1.66 | 54 |
| stroke 139 | 55 % → 99 % | 770.7 px | 0.44 | 1.81 | 80 |
| stroke 140 | 48 % → 99 % | 1237.3 px | 0.42 | 2.04 | 35 |
| stroke 141 | 38 % → 94 % | 511.0 px | 0.33 | 2.44 | 92 |
| stroke 142 | 51 % → 92 % | 1270.7 px | 0.41 | 1.81 | 54 |
| stroke 143 | 67 % → 99 % | 1251.3 px | 0.45 | 1.46 | 70 |
| stroke 144 | 62 % → 98 % | 1524.1 px | 0.44 | 1.59 | 44 |
| stroke 145 | 48 % → 94 % | 1028.2 px | 0.41 | 1.97 | 58 |
| stroke 146 | 57 % → 99 % | 1446.0 px | 0.44 | 1.73 | 46 |
| stroke 147 | 69 % → 99 % | 1724.4 px | 0.46 | 1.44 | 52 |
| stroke 148 | 76 % → 92 % | 1085.0 px | 0.48 | 1.22 | 95 |
| stroke 149 | 73 % → 92 % | 1046.6 px | 0.47 | 1.27 | 150 |
| stroke 150 | 40 % → 100 % | 260.7 px | 0.38 | 2.50 | 196 |
| stroke 151 | 46 % → 100 % | 317.0 px | 0.38 | 2.18 | 225 |
| stroke 152 | 29 % → 100 % | 386.9 px | 0.37 | 3.47 | 59 |
| stroke 153 | 37 % → 100 % | 469.3 px | 0.36 | 2.69 | 94 |
| stroke 154 | 35 % → 99 % | 328.5 px | 0.42 | 2.80 | 115 |
| stroke 155 | 29 % → 99 % | 269.1 px | 0.40 | 3.40 | 126 |
| stroke 156 | 59 % → 100 % | 981.7 px | 0.45 | 1.68 | 65 |
| stroke 157 | 32 % → 99 % | 328.8 px | 0.41 | 3.06 | 130 |
| stroke 158 | 59 % → 99 % | 614.7 px | 0.46 | 1.67 | 149 |
| stroke 159 | 93 % → 99 % | 1428.1 px | 0.53 | 1.07 | 101 |
| stroke 160 | 88 % → 99 % | 1652.5 px | 0.53 | 1.12 | 80 |
| stroke 161 | 46 % → 99 % | 507.6 px | 0.43 | 2.15 | 120 |
| stroke 162 | 83 % → 99 % | 727.4 px | 0.51 | 1.19 | 186 |
| stroke 163 | 32 % → 98 % | 668.3 px | 0.40 | 3.10 | 66 |
| stroke 164 | 64 % → 100 % | 1048.1 px | 0.45 | 1.56 | 108 |
| stroke 165 | 23 % → 98 % | 591.6 px | 0.39 | 4.19 | 50 |
| stroke 166 | 45 % → 99 % | 1114.2 px | 0.42 | 2.21 | 41 |
| stroke 167 | 61 % → 99 % | 1302.8 px | 0.46 | 1.62 | 72 |
| stroke 168 | 52 % → 99 % | 1305.5 px | 0.43 | 1.90 | 33 |
| stroke 169 | 85 % → 99 % | 1252.4 px | 0.50 | 1.16 | 102 |
| stroke 170 | 8 % → 70 % | 54.8 px | 0.30 | 9.11 | 170 |
| stroke 171 | 17 % → 65 % | 119.8 px | 0.27 | 3.74 | 226 |
| stroke 172 | 26 % → 75 % | 228.8 px | 0.36 | 2.88 | 192 |
| stroke 173 | 12 % → 70 % | 290.2 px | 0.29 | 6.03 | 33 |
| stroke 174 | 19 % → 63 % | 175.2 px | 0.27 | 3.41 | 182 |
| stroke 175 | 14 % → 61 % | 103.1 px | 0.29 | 4.40 | 207 |
| stroke 176 | 19 % → 72 % | 192.6 px | 0.32 | 3.77 | 116 |
| stroke 177 | 30 % → 79 % | 421.5 px | 0.35 | 2.66 | 151 |
| stroke 178 | 24 % → 63 % | 433.7 px | 0.26 | 2.66 | 44 |
| stroke 179 | 22 % → 64 % | 253.7 px | 0.28 | 2.92 | 96 |
| stroke 180 | 21 % → 75 % | 449.6 px | 0.30 | 3.58 | 68 |
| stroke 181 | 24 % → 72 % | 590.2 px | 0.29 | 3.04 | 37 |
| stroke 182 | 17 % → 74 % | 317.6 px | 0.30 | 4.29 | 49 |
| stroke 183 | 22 % → 67 % | 322.6 px | 0.29 | 3.10 | 72 |
| stroke 184 | 33 % → 74 % | 477.0 px | 0.37 | 2.23 | 89 |
| stroke 185 | 24 % → 71 % | 252.2 px | 0.28 | 3.00 | 154 |
| stroke 186 | 22 % → 76 % | 302.2 px | 0.30 | 3.52 | 102 |
| stroke 187 | 20 % → 67 % | 295.7 px | 0.29 | 3.42 | 89 |
| stroke 188 | 26 % → 69 % | 645.0 px | 0.27 | 2.65 | 34 |
| stroke 189 | 19 % → 93 % | 336.7 px | 0.39 | 5.05 | 41 |
| stroke 190 | 20 % → 93 % | 297.6 px | 0.39 | 4.69 | 64 |
| stroke 191 | 20 % → 93 % | 140.8 px | 0.38 | 4.69 | 177 |
| stroke 192 | 33 % → 90 % | 443.2 px | 0.39 | 2.78 | 59 |
| stroke 193 | 30 % → 91 % | 315.0 px | 0.39 | 3.04 | 66 |
| stroke 194 | 45 % → 92 % | 260.8 px | 0.40 | 2.03 | 137 |
| stroke 195 | 48 % → 91 % | 576.0 px | 0.40 | 1.91 | 35 |
| stroke 196 | 36 % → 96 % | 421.0 px | 0.38 | 2.69 | 74 |
| stroke 197 | 40 % → 93 % | 458.0 px | 0.38 | 2.31 | 78 |
| stroke 198 | 34 % → 96 % | 601.1 px | 0.38 | 2.83 | 42 |
| stroke 199 | 41 % → 94 % | 356.6 px | 0.38 | 2.32 | 143 |
| stroke 200 | 34 % → 97 % | 422.8 px | 0.38 | 2.83 | 101 |
| stroke 201 | 39 % → 86 % | 914.3 px | 0.29 | 2.17 | 30 |
| stroke 202 | 66 % → 88 % | 1377.7 px | 0.43 | 1.34 | 47 |
| stroke 203 | 53 % → 90 % | 939.5 px | 0.39 | 1.70 | 49 |
| stroke 204 | 83 % → 96 % | 1775.2 px | 0.54 | 1.15 | 25 |
| stroke 205 | 14 % → 100 % | 272.0 px | 0.38 | 7.00 | 39 |
| stroke 206 | 23 % → 78 % | 195.7 px | 0.45 | 3.35 | 117 |
| stroke 207 | 29 % → 87 % | 174.2 px | 0.31 | 2.99 | 367 |
| stroke 208 | 26 % → 83 % | 417.8 px | 0.45 | 3.22 | 34 |
| stroke 209 | 48 % → 84 % | 605.4 px | 0.51 | 1.76 | 188 |
| stroke 210 | 46 % → 93 % | 1010.6 px | 0.36 | 2.02 | 18 |
| stroke 211 | 58 % → 91 % | 370.7 px | 0.48 | 1.58 | 124 |
| stroke 212 | 45 % → 56 % | 305.2 px | 0.44 | 1.23 | 84 |
| stroke 213 | 41 % → 38 % | 487.6 px | 0.52 | 0.93 | 39 |
| stroke 214 | 46 % → 99 % | 234.2 px | 0.33 | 2.15 | 1352 |
| stroke 215 | 45 % → 90 % | 263.9 px | 0.28 | 2.01 | 1066 |
| stroke 216 | 45 % → 92 % | 243.6 px | 0.36 | 2.06 | 1048 |
| stroke 217 | 53 % → 100 % | 234.0 px | 0.36 | 1.90 | 1865 |
| stroke 218 | 52 % → 95 % | 250.9 px | 0.26 | 1.83 | 2653 |
| stroke 219 | 61 % → 92 % | 510.6 px | 0.34 | 1.51 | 562 |
| stroke 220 | 59 % → 93 % | 696.0 px | 0.32 | 1.58 | 391 |
| stroke 221 | 37 % → 99 % | 377.9 px | 0.36 | 2.69 | 486 |
| stroke 222 | 59 % → 96 % | 267.8 px | 0.31 | 1.64 | 1662 |
| stroke 223 | 59 % → 98 % | 373.5 px | 0.33 | 1.67 | 746 |
| stroke 224 | 62 % → 95 % | 517.4 px | 0.30 | 1.53 | 486 |
| stroke 225 | 48 % → 99 % | 359.5 px | 0.37 | 2.08 | 929 |
| stroke 226 | 49 % → 91 % | 422.0 px | 0.24 | 1.85 | 488 |
| stroke 227 | 59 % → 98 % | 327.8 px | 0.35 | 1.67 | 906 |
| stroke 228 | 72 % → 99 % | 366.8 px | 0.34 | 1.37 | 991 |
| stroke 229 | 63 % → 96 % | 448.9 px | 0.28 | 1.51 | 586 |
| stroke 230 | 81 % → 99 % | 529.5 px | 0.37 | 1.23 | 879 |
| stroke 231 | 64 % → 96 % | 398.8 px | 0.29 | 1.50 | 1193 |
| stroke 232 | 71 % → 99 % | 849.3 px | 0.30 | 1.38 | 396 |
| stroke 233 | 60 % → 95 % | 783.1 px | 0.32 | 1.58 | 253 |
| stroke 234 | 48 % → 88 % | 402.7 px | 0.23 | 1.82 | 549 |
| stroke 235 | 55 % → 96 % | 564.6 px | 0.38 | 1.75 | 297 |
| stroke 236 | 75 % → 96 % | 811.4 px | 0.31 | 1.29 | 370 |
| stroke 237 | 65 % → 100 % | 665.8 px | 0.37 | 1.54 | 422 |
| stroke 238 | 73 % → 100 % | 907.6 px | 0.34 | 1.38 | 305 |
| stroke 239 | 72 % → 96 % | 878.6 px | 0.30 | 1.33 | 379 |
| stroke 240 | 56 % → 99 % | 695.2 px | 0.35 | 1.79 | 305 |
| stroke 241 | 71 % → 99 % | 376.0 px | 0.47 | 1.38 | 1057 |
| stroke 242 | 88 % → 99 % | 1048.8 px | 0.50 | 1.12 | 318 |
| stroke 243 | 83 % → 99 % | 676.0 px | 0.41 | 1.20 | 633 |
| stroke 244 | 78 % → 99 % | 416.8 px | 0.39 | 1.28 | 882 |
| stroke 245 | 86 % → 100 % | 552.8 px | 0.40 | 1.16 | 750 |
| stroke 246 | 78 % → 99 % | 860.6 px | 0.40 | 1.26 | 264 |
| stroke 247 | 39 % → 92 % | 334.0 px | 0.38 | 2.38 | 322 |
| stroke 248 | 62 % → 98 % | 381.5 px | 0.35 | 1.59 | 771 |
| stroke 249 | 58 % → 99 % | 413.3 px | 0.35 | 1.69 | 582 |
| stroke 250 | 69 % → 96 % | 339.4 px | 0.38 | 1.39 | 678 |
| stroke 251 | 68 % → 93 % | 543.1 px | 0.39 | 1.36 | 408 |
| stroke 252 | 44 % → 86 % | 253.6 px | 0.45 | 1.95 | 708 |
| stroke 253 | 58 % → 87 % | 618.5 px | 0.49 | 1.49 | 350 |
| stroke 254 | 53 % → 94 % | 267.5 px | 0.42 | 1.75 | 728 |
| stroke 255 | 42 % → 97 % | 565.7 px | 0.29 | 2.33 | 33 |
| stroke 256 | 21 % → 54 % | 399.0 px | 0.52 | 2.58 | 46 |
| stroke 257 | 54 % → 99 % | 277.9 px | 0.42 | 1.84 | 680 |
| stroke 258 | 31 % → 64 % | 768.3 px | 0.48 | 2.06 | 23 |
| stroke 259 | 45 % → 77 % | 202.4 px | 0.45 | 1.70 | 2205 |
| stroke 260 | 45 % → 72 % | 242.8 px | 0.45 | 1.58 | 1322 |
| stroke 261 | 44 % → 60 % | 217.2 px | 0.48 | 1.37 | 2151 |
| stroke 262 | 61 % → 92 % | 376.5 px | 0.37 | 1.50 | 1056 |
| stroke 263 | 72 % → 84 % | 445.3 px | 0.49 | 1.16 | 931 |
| stroke 264 | 61 % → 77 % | 332.2 px | 0.49 | 1.27 | 1202 |
| stroke 265 | 69 % → 77 % | 850.4 px | 0.52 | 1.12 | 228 |
| stroke 266 | 54 % → 88 % | 442.6 px | 0.33 | 1.62 | 538 |
| stroke 267 | 57 % → 69 % | 444.5 px | 0.49 | 1.21 | 464 |
| stroke 268 | 56 % → 76 % | 544.0 px | 0.38 | 1.35 | 329 |
| stroke 269 | 69 % → 94 % | 621.0 px | 0.38 | 1.36 | 447 |
| stroke 270 | 71 % → 77 % | 883.3 px | 0.49 | 1.08 | 247 |
| stroke 271 | 68 % → 86 % | 319.1 px | 0.43 | 1.26 | 1464 |
| stroke 272 | 81 % → 87 % | 341.6 px | 0.44 | 1.08 | 1366 |
| stroke 273 | 78 % → 92 % | 642.4 px | 0.41 | 1.18 | 436 |
| stroke 274 | 81 % → 97 % | 436.5 px | 0.43 | 1.20 | 871 |
| stroke 275 | 84 % → 94 % | 448.8 px | 0.42 | 1.12 | 793 |
| stroke 276 | 77 % → 95 % | 413.1 px | 0.41 | 1.24 | 850 |
| stroke 277 | 86 % → 89 % | 915.8 px | 0.44 | 1.03 | 263 |
| stroke 278 | 80 % → 82 % | 826.1 px | 0.45 | 1.03 | 310 |
| stroke 279 | 75 % → 96 % | 304.1 px | 0.36 | 1.28 | 1437 |
| stroke 280 | 76 % → 99 % | 738.8 px | 0.37 | 1.29 | 201 |
| stroke 281 | 86 % → 96 % | 379.8 px | 0.37 | 1.12 | 3951 |
| stroke 282 | 88 % → 95 % | 446.5 px | 0.37 | 1.08 | 1477 |
| stroke 283 | 91 % → 99 % | 666.4 px | 0.39 | 1.08 | 871 |
| stroke 284 | 94 % → 99 % | 981.1 px | 0.36 | 1.06 | 777 |
| stroke 285 | 92 % → 99 % | 730.4 px | 0.37 | 1.08 | 792 |
| stroke 286 | 87 % → 95 % | 555.0 px | 0.36 | 1.09 | 980 |
| stroke 287 | 89 % → 97 % | 544.0 px | 0.36 | 1.09 | 892 |
| stroke 288 | 89 % → 95 % | 908.8 px | 0.38 | 1.07 | 336 |
| stroke 289 | 88 % → 94 % | 860.4 px | 0.37 | 1.07 | 385 |
| stroke 290 | 93 % → 99 % | 682.6 px | 0.37 | 1.06 | 709 |
| stroke 291 | 92 % → 99 % | 855.8 px | 0.36 | 1.07 | 402 |
| stroke 292 | 13 % → 100 % | 53.6 px | 0.01 | 7.47 | 426 |
| stroke 293 | 16 % → 74 % | 74.7 px | 0.05 | 4.60 | 937 |
| stroke 294 | 36 % → 77 % | 148.6 px | 0.04 | 2.16 | 385 |
| stroke 295 | 30 % → 78 % | 172.8 px | 0.12 | 2.58 | 791 |
| stroke 296 | 22 % → 99 % | 61.2 px | 0.01 | 4.43 | 787 |
| stroke 297 | 27 % → 77 % | 138.0 px | 0.05 | 2.80 | 875 |
| stroke 298 | 25 % → 99 % | 105.5 px | 0.03 | 4.00 | 869 |
| stroke 299 | 33 % → 71 % | 208.4 px | 0.04 | 2.13 | 461 |
| stroke 300 | 36 % → 92 % | 141.5 px | 0.01 | 2.56 | 690 |
| stroke 301 | 38 % → 98 % | 181.0 px | 0.11 | 2.56 | 1554 |
| stroke 302 | 49 % → 85 % | 186.5 px | 0.14 | 1.74 | 1457 |
| stroke 303 | 39 % → 72 % | 179.5 px | 0.06 | 1.84 | 482 |
| stroke 304 | 62 % → 99 % | 206.1 px | 0.01 | 1.61 | 428 |
| stroke 305 | 48 % → 97 % | 261.9 px | 0.11 | 2.04 | 962 |
| stroke 306 | 62 % → 99 % | 244.5 px | 0.04 | 1.58 | 994 |
| stroke 307 | 73 % → 99 % | 336.3 px | 0.04 | 1.35 | 582 |
| stroke 308 | 39 % → 91 % | 167.2 px | 0.01 | 2.34 | 1524 |
| stroke 309 | 54 % → 96 % | 291.9 px | 0.01 | 1.77 | 938 |
| stroke 310 | 43 % → 72 % | 208.6 px | 0.02 | 1.67 | 534 |
| stroke 311 | 59 % → 95 % | 308.1 px | 0.01 | 1.62 | 532 |
| stroke 312 | 74 % → 92 % | 325.0 px | 0.01 | 1.24 | 494 |
| stroke 313 | 74 % → 90 % | 315.9 px | 0.12 | 1.21 | 867 |
| stroke 314 | 58 % → 80 % | 245.2 px | 0.11 | 1.38 | 575 |
| stroke 315 | 74 % → 100 % | 679.9 px | 0.01 | 1.34 | 285 |
| stroke 316 | 58 % → 76 % | 315.4 px | 0.02 | 1.31 | 318 |
| stroke 317 | 74 % → 99 % | 465.7 px | 0.08 | 1.34 | 554 |
| stroke 318 | 80 % → 99 % | 365.6 px | 0.02 | 1.24 | 520 |
| stroke 319 | 61 % → 93 % | 450.7 px | 0.01 | 1.52 | 371 |
| stroke 320 | 83 % → 99 % | 762.1 px | 0.01 | 1.20 | 167 |
| stroke 321 | 86 % → 99 % | 294.9 px | 0.01 | 1.16 | 524 |
| stroke 322 | 72 % → 99 % | 704.3 px | 0.01 | 1.38 | 179 |
| stroke 323 | 80 % → 98 % | 320.4 px | 0.01 | 1.23 | 242 |
| stroke 324 | 73 % → 80 % | 363.1 px | 0.15 | 1.10 | 400 |
| stroke 325 | 62 % → 78 % | 502.5 px | 0.10 | 1.26 | 364 |
| stroke 326 | 76 % → 99 % | 469.7 px | 0.01 | 1.30 | 302 |
| stroke 327 | 53 % → 80 % | 279.6 px | 0.11 | 1.51 | 936 |
| stroke 328 | 78 % → 99 % | 396.9 px | 0.01 | 1.28 | 395 |
| stroke 329 | 56 % → 76 % | 271.9 px | 0.03 | 1.37 | 386 |
| stroke 330 | 54 % → 79 % | 208.2 px | 0.04 | 1.48 | 597 |
| stroke 331 | 54 % → 81 % | 337.5 px | 0.01 | 1.50 | 471 |
| stroke 332 | 78 % → 99 % | 527.7 px | 0.01 | 1.27 | 280 |
| stroke 333 | 76 % → 100 % | 504.6 px | 0.01 | 1.31 | 452 |
| stroke 334 | 92 % → 99 % | 500.4 px | 0.01 | 1.08 | 348 |
| stroke 335 | 95 % → 100 % | 554.5 px | 0.01 | 1.05 | 457 |
| stroke 336 | 54 % → 76 % | 338.8 px | 0.02 | 1.40 | 433 |
| stroke 337 | 68 % → 77 % | 515.7 px | 0.11 | 1.13 | 453 |
| stroke 338 | 72 % → 75 % | 480.0 px | 0.23 | 1.03 | 247 |
| stroke 339 | 58 % → 75 % | 242.7 px | 0.02 | 1.30 | 564 |
| stroke 340 | 84 % → 91 % | 368.3 px | 0.01 | 1.08 | 429 |
| stroke 341 | 90 % → 97 % | 1110.9 px | 0.15 | 1.08 | 188 |
| stroke 342 | 90 % → 99 % | 848.5 px | 0.02 | 1.10 | 303 |
| stroke 343 | 86 % → 100 % | 794.0 px | 0.01 | 1.17 | 222 |
| stroke 344 | 98 % → 100 % | 817.4 px | 0.01 | 1.02 | 167 |
| stroke 345 | 86 % → 93 % | 438.7 px | 0.01 | 1.08 | 376 |
| stroke 346 | 84 % → 87 % | 399.2 px | 0.01 | 1.03 | 335 |
| stroke 347 | 92 % → 99 % | 465.6 px | 0.01 | 1.08 | 253 |
| stroke 348 | 63 % → 88 % | 498.8 px | 0.01 | 1.39 | 829 |
| stroke 349 | 50 % → 70 % | 350.4 px | 0.03 | 1.39 | 591 |
| stroke 350 | 66 % → 79 % | 352.1 px | 0.05 | 1.19 | 432 |
| stroke 351 | 87 % → 93 % | 642.8 px | 0.01 | 1.08 | 252 |
| stroke 352 | 98 % → 98 % | 473.6 px | 0.01 | 1.01 | 227 |
| stroke 353 | 68 % → 79 % | 431.0 px | 0.09 | 1.17 | 531 |
| stroke 354 | 68 % → 80 % | 747.9 px | 0.19 | 1.16 | 172 |
| stroke 355 | 97 % → 100 % | 332.8 px | 0.01 | 1.02 | 508 |
| stroke 356 | 74 % → 86 % | 676.3 px | 0.01 | 1.16 | 298 |
| stroke 357 | 98 % → 100 % | 562.2 px | 0.01 | 1.01 | 401 |
| stroke 358 | 97 % → 99 % | 880.0 px | 0.01 | 1.02 | 159 |
| stroke 359 | 99 % → 99 % | 831.2 px | 0.01 | 1.01 | 186 |
| stroke 360 | 76 % → 78 % | 608.5 px | 0.03 | 1.03 | 140 |
| stroke 361 | 99 % → 99 % | 742.5 px | 0.01 | 1.00 | 176 |
| stroke 362 | 59 % → 75 % | 301.9 px | 0.01 | 1.28 | 279 |
| stroke 363 | 88 % → 98 % | 1120.9 px | 0.07 | 1.12 | 179 |
| stroke 364 | 86 % → 88 % | 880.2 px | 0.12 | 1.02 | 321 |
| stroke 365 | 68 % → 74 % | 442.0 px | 0.04 | 1.09 | 284 |
| stroke 366 | 99 % → 100 % | 616.6 px | 0.01 | 1.01 | 321 |
| stroke 367 | 65 % → 72 % | 655.4 px | 0.03 | 1.12 | 163 |
| stroke 368 | 61 % → 73 % | 550.7 px | 0.03 | 1.20 | 219 |
| stroke 369 | 93 % → 100 % | 1083.8 px | 0.01 | 1.08 | 187 |
| stroke 370 | 81 % → 84 % | 705.5 px | 0.13 | 1.04 | 331 |
| stroke 371 | 91 % → 92 % | 591.4 px | 0.01 | 1.01 | 235 |
| stroke 372 | 59 % → 77 % | 505.8 px | 0.03 | 1.31 | 504 |
| stroke 373 | 86 % → 88 % | 948.6 px | 0.22 | 1.02 | 282 |
| stroke 374 | 81 % → 100 % | 965.1 px | 0.01 | 1.23 | 140 |
| stroke 375 | 75 % → 74 % | 426.6 px | 0.15 | 0.98 | 224 |
| stroke 376 | 95 % → 96 % | 749.9 px | 0.01 | 1.01 | 137 |
| stroke 377 | 99 % → 99 % | 425.7 px | 0.01 | 1.00 | 194 |
| stroke 378 | 86 % → 98 % | 799.8 px | 0.18 | 1.14 | 572 |
| stroke 379 | 91 % → 100 % | 1061.9 px | 0.03 | 1.10 | 380 |
| stroke 380 | 91 % → 90 % | 673.3 px | 0.10 | 0.99 | 461 |
| stroke 381 | 51 % → 66 % | 540.9 px | 0.04 | 1.30 | 228 |
| stroke 382 | 86 % → 99 % | 730.6 px | 0.06 | 1.15 | 463 |
| stroke 383 | 62 % → 74 % | 643.7 px | 0.10 | 1.19 | 435 |
| stroke 384 | 91 % → 91 % | 843.2 px | 0.01 | 1.01 | 153 |
| stroke 385 | 90 % → 91 % | 1196.2 px | 0.19 | 1.01 | 197 |
| stroke 386 | 57 % → 70 % | 500.4 px | 0.06 | 1.23 | 239 |
| stroke 387 | 64 % → 73 % | 720.8 px | 0.10 | 1.14 | 146 |
| stroke 388 | 76 % → 82 % | 876.0 px | 0.20 | 1.08 | 183 |
| stroke 389 | 99 % → 99 % | 965.1 px | 0.05 | 1.00 | 289 |
| stroke 390 | 64 % → 71 % | 827.3 px | 0.02 | 1.11 | 158 |
| stroke 391 | 97 % → 97 % | 704.2 px | 0.01 | 1.00 | 121 |
| stroke 392 | 92 % → 100 % | 1005.8 px | 0.01 | 1.08 | 188 |
| stroke 393 | 71 % → 73 % | 690.0 px | 0.03 | 1.03 | 140 |
| stroke 394 | 100 % → 100 % | 1147.6 px | 0.01 | 1.00 | 137 |
| stroke 395 | 75 % → 81 % | 794.1 px | 0.06 | 1.07 | 175 |
| stroke 396 | 97 % → 99 % | 1125.2 px | 0.01 | 1.03 | 151 |
| stroke 397 | 98 % → 98 % | 847.8 px | 0.03 | 1.00 | 224 |
| stroke 398 | 76 % → 79 % | 688.9 px | 0.04 | 1.03 | 185 |
| stroke 399 | 100 % → 100 % | 911.1 px | 0.01 | 1.00 | 143 |
| stroke 400 | 97 % → 98 % | 602.2 px | 0.01 | 1.01 | 134 |
| stroke 401 | 75 % → 81 % | 937.3 px | 0.07 | 1.08 | 155 |
| stroke 402 | 61 % → 74 % | 583.6 px | 0.04 | 1.21 | 254 |
| stroke 403 | 95 % → 98 % | 1193.8 px | 0.01 | 1.02 | 143 |
| stroke 404 | 91 % → 98 % | 1205.0 px | 0.05 | 1.08 | 141 |
| stroke 405 | 92 % → 93 % | 913.7 px | 0.01 | 1.02 | 255 |
| stroke 406 | 86 % → 87 % | 1030.9 px | 0.01 | 1.01 | 161 |
| stroke 407 | 68 % → 77 % | 887.3 px | 0.04 | 1.14 | 286 |
| stroke 408 | 57 % → 64 % | 433.8 px | 0.02 | 1.12 | 209 |
| stroke 409 | 100 % → 99 % | 781.5 px | 0.01 | 0.99 | 149 |
| stroke 410 | 82 % → 84 % | 1042.0 px | 0.10 | 1.02 | 164 |
| stroke 411 | 90 % → 90 % | 919.7 px | 0.01 | 1.01 | 160 |
| stroke 412 | 74 % → 72 % | 560.8 px | 0.01 | 0.98 | 481 |
| stroke 413 | 92 % → 91 % | 1121.1 px | 0.12 | 0.99 | 487 |
| stroke 414 | 80 % → 98 % | 1024.1 px | 0.11 | 1.23 | 479 |
| stroke 415 | 100 % → 99 % | 764.6 px | 0.01 | 0.99 | 209 |
| stroke 416 | 93 % → 98 % | 1137.0 px | 0.10 | 1.06 | 135 |
| stroke 417 | 84 % → 86 % | 996.3 px | 0.01 | 1.02 | 146 |
| stroke 418 | 78 % → 99 % | 894.1 px | 0.07 | 1.28 | 202 |
| stroke 419 | 22 % → 79 % | 153.5 px | 0.07 | 3.53 | 198 |
| stroke 420 | 49 % → 72 % | 270.7 px | 0.03 | 1.47 | 350 |
| stroke 421 | 47 % → 70 % | 346.4 px | 0.04 | 1.51 | 130 |
| stroke 422 | 55 % → 74 % | 251.6 px | 0.08 | 1.35 | 700 |
| stroke 423 | 56 % → 74 % | 370.9 px | 0.08 | 1.33 | 426 |
| stroke 424 | 57 % → 80 % | 362.9 px | 0.14 | 1.40 | 281 |
| stroke 425 | 61 % → 73 % | 628.0 px | 0.04 | 1.19 | 627 |
| stroke 426 | 62 % → 73 % | 297.6 px | 0.05 | 1.16 | 316 |
| stroke 427 | 71 % → 78 % | 423.9 px | 0.06 | 1.10 | 299 |
| stroke 428 | 81 % → 89 % | 470.0 px | 0.08 | 1.10 | 481 |
| stroke 429 | 73 % → 74 % | 750.4 px | 0.01 | 1.01 | 514 |
| stroke 430 | 68 % → 68 % | 538.9 px | 0.05 | 1.00 | 359 |
| stroke 431 | 71 % → 84 % | 444.2 px | 0.20 | 1.18 | 298 |
| stroke 432 | 73 % → 73 % | 402.2 px | 0.04 | 0.99 | 363 |
| stroke 433 | 71 % → 74 % | 349.9 px | 0.08 | 1.04 | 1841 |
| stroke 434 | 73 % → 75 % | 562.3 px | 0.06 | 1.02 | 245 |
| stroke 435 | 74 % → 80 % | 754.0 px | 0.08 | 1.09 | 161 |
| stroke 436 | 70 % → 76 % | 634.4 px | 0.13 | 1.09 | 258 |
| stroke 437 | 83 % → 89 % | 421.1 px | 0.17 | 1.07 | 295 |
| stroke 438 | 79 % → 87 % | 637.4 px | 0.20 | 1.11 | 91 |
| stroke 439 | 90 % → 91 % | 587.7 px | 0.14 | 1.01 | 277 |
| stroke 440 | 92 % → 93 % | 1306.1 px | 0.14 | 1.02 | 121 |
| stroke 441 | 86 % → 88 % | 484.5 px | 0.20 | 1.02 | 498 |
| stroke 442 | 87 % → 88 % | 609.0 px | 0.18 | 1.01 | 247 |
| stroke 443 | 91 % → 93 % | 1415.5 px | 0.12 | 1.02 | 60 |
| stroke 444 | 93 % → 94 % | 863.0 px | 0.14 | 1.00 | 144 |
| stroke 445 | 89 % → 89 % | 930.2 px | 0.19 | 1.00 | 178 |
| stroke 446 | 88 % → 88 % | 825.8 px | 0.19 | 0.99 | 129 |
| stroke 447 | 88 % → 86 % | 845.6 px | 0.22 | 0.98 | 69 |
| stroke 448 | 90 % → 88 % | 850.6 px | 0.20 | 0.99 | 91 |
| stroke 449 | 79 % → 77 % | 779.0 px | 0.18 | 0.97 | 72 |
| stroke 450 | 78 % → 75 % | 994.8 px | 0.17 | 0.97 | 69 |
| stroke 451 | 78 % → 75 % | 1050.0 px | 0.17 | 0.96 | 82 |
| stroke 452 | 66 % → 88 % | 371.3 px | 0.12 | 1.34 | 317 |
| stroke 453 | 68 % → 85 % | 495.4 px | 0.10 | 1.25 | 217 |
| stroke 454 | 75 % → 85 % | 466.7 px | 0.08 | 1.13 | 263 |
| stroke 455 | 72 % → 85 % | 480.1 px | 0.16 | 1.18 | 293 |
| stroke 456 | 81 % → 92 % | 692.4 px | 0.11 | 1.13 | 232 |
| stroke 457 | 69 % → 77 % | 1201.1 px | 0.06 | 1.11 | 79 |
| stroke 458 | 76 % → 82 % | 667.3 px | 0.01 | 1.07 | 152 |
| stroke 459 | 82 % → 88 % | 1101.8 px | 0.02 | 1.07 | 70 |
| stroke 460 | 95 % → 98 % | 1050.6 px | 0.16 | 1.03 | 118 |
| stroke 461 | 88 % → 95 % | 933.8 px | 0.15 | 1.08 | 368 |
| stroke 462 | 80 % → 87 % | 549.6 px | 0.10 | 1.08 | 478 |
| stroke 463 | 77 % → 83 % | 623.7 px | 0.12 | 1.07 | 269 |
| stroke 464 | 95 % → 96 % | 1625.6 px | 0.05 | 1.01 | 66 |
| stroke 465 | 77 % → 81 % | 1315.8 px | 0.11 | 1.05 | 88 |
| stroke 466 | 81 % → 86 % | 714.3 px | 0.16 | 1.07 | 126 |
| stroke 467 | 77 % → 82 % | 782.0 px | 0.14 | 1.06 | 118 |
| stroke 468 | 76 % → 77 % | 1298.6 px | 0.09 | 1.01 | 50 |
| stroke 469 | 84 % → 87 % | 805.9 px | 0.12 | 1.04 | 121 |
| stroke 470 | 84 % → 84 % | 719.9 px | 0.07 | 1.01 | 124 |
| stroke 471 | 96 % → 97 % | 1060.3 px | 0.20 | 1.01 | 1362 |
| stroke 472 | 78 % → 80 % | 1199.1 px | 0.14 | 1.03 | 266 |
| stroke 473 | 97 % → 98 % | 1497.9 px | 0.19 | 1.01 | 95 |
| stroke 474 | 91 % → 95 % | 1511.1 px | 0.17 | 1.04 | 74 |
| stroke 475 | 82 % → 85 % | 1408.5 px | 0.14 | 1.04 | 47 |
| stroke 476 | 88 % → 88 % | 1079.3 px | 0.04 | 1.00 | 71 |
| stroke 477 | 78 % → 80 % | 1327.2 px | 0.15 | 1.02 | 46 |
| stroke 478 | 83 % → 89 % | 1552.9 px | 0.18 | 1.07 | 39 |
| stroke 479 | 77 % → 78 % | 1207.7 px | 0.10 | 1.00 | 56 |
| stroke 480 | 77 % → 82 % | 1423.0 px | 0.20 | 1.06 | 65 |
| stroke 481 | 79 % → 82 % | 1504.9 px | 0.14 | 1.05 | 44 |
| stroke 482 | 79 % → 79 % | 1444.1 px | 0.01 | 1.00 | 31 |
| stroke 483 | 78 % → 81 % | 1131.4 px | 0.12 | 1.04 | 47 |
| stroke 484 | 86 % → 88 % | 802.1 px | 0.32 | 1.02 | 104 |
| stroke 485 | 83 % → 85 % | 1418.7 px | 0.32 | 1.02 | 63 |
| stroke 486 | 87 % → 88 % | 752.1 px | 0.30 | 1.01 | 151 |
| stroke 487 | 83 % → 82 % | 1425.5 px | 0.20 | 1.00 | 61 |
| stroke 488 | 80 % → 86 % | 528.9 px | 0.18 | 1.08 | 278 |
| stroke 489 | 85 % → 85 % | 704.0 px | 0.21 | 1.00 | 175 |
| stroke 490 | 61 % → 72 % | 414.4 px | 0.26 | 1.17 | 163 |
| stroke 491 | 82 % → 89 % | 461.4 px | 0.37 | 1.08 | 281 |
| stroke 492 | 65 % → 71 % | 735.3 px | 0.38 | 1.09 | 111 |
| stroke 493 | 70 % → 79 % | 407.5 px | 0.28 | 1.13 | 305 |
| stroke 494 | 66 % → 79 % | 626.9 px | 0.30 | 1.19 | 130 |
| stroke 495 | 68 % → 76 % | 435.0 px | 0.32 | 1.12 | 289 |
| stroke 496 | 74 % → 84 % | 512.5 px | 0.30 | 1.13 | 225 |
| stroke 497 | 81 % → 87 % | 706.9 px | 0.34 | 1.08 | 168 |
| stroke 498 | 53 % → 57 % | 482.7 px | 0.31 | 1.08 | 177 |
| stroke 499 | 54 % → 58 % | 590.4 px | 0.28 | 1.09 | 102 |
| stroke 500 | 62 % → 65 % | 437.2 px | 0.23 | 1.05 | 170 |
| stroke 501 | 52 % → 56 % | 396.5 px | 0.25 | 1.09 | 147 |
| stroke 502 | 77 % → 81 % | 632.1 px | 0.29 | 1.04 | 198 |
| stroke 503 | 79 % → 79 % | 1066.2 px | 0.23 | 1.00 | 109 |
| stroke 504 | 72 % → 72 % | 718.6 px | 0.28 | 1.01 | 144 |
| stroke 505 | 57 % → 59 % | 417.9 px | 0.27 | 1.04 | 190 |
| stroke 506 | 65 % → 65 % | 469.6 px | 0.25 | 1.00 | 206 |
| stroke 507 | 83 % → 84 % | 1054.3 px | 0.37 | 1.01 | 99 |
| stroke 508 | 92 % → 92 % | 712.8 px | 0.40 | 1.00 | 163 |
| stroke 509 | 89 % → 89 % | 760.3 px | 0.37 | 1.01 | 167 |
| stroke 510 | 87 % → 88 % | 760.7 px | 0.30 | 1.02 | 141 |
| stroke 511 | 75 % → 77 % | 1129.8 px | 0.30 | 1.02 | 68 |
| stroke 512 | 63 % → 64 % | 1024.7 px | 0.26 | 1.01 | 57 |
| stroke 513 | 54 % → 54 % | 449.6 px | 0.26 | 1.00 | 130 |
| stroke 514 | 60 % → 60 % | 698.5 px | 0.25 | 1.00 | 92 |
| stroke 515 | 66 % → 66 % | 936.0 px | 0.34 | 1.00 | 82 |
| stroke 516 | 84 % → 84 % | 1133.2 px | 0.30 | 1.00 | 76 |
| stroke 517 | 57 % → 57 % | 793.5 px | 0.29 | 1.00 | 79 |
| stroke 518 | 75 % → 75 % | 1120.6 px | 0.29 | 1.00 | 69 |
| stroke 519 | 82 % → 83 % | 1357.8 px | 0.31 | 1.00 | 57 |
| stroke 520 | 97 % → 100 % | 539.7 px | 0.38 | 1.02 | 369 |
| stroke 521 | 98 % → 99 % | 1437.3 px | 0.39 | 1.01 | 69 |
| stroke 522 | 97 % → 100 % | 717.0 px | 0.39 | 1.02 | 332 |
| stroke 523 | 98 % → 99 % | 797.8 px | 0.41 | 1.01 | 556 |
| stroke 524 | 99 % → 99 % | 1654.0 px | 0.43 | 1.01 | 201 |
| stroke 525 | 99 % → 100 % | 1118.0 px | 0.41 | 1.01 | 137 |
| stroke 526 | 99 % → 99 % | 865.0 px | 0.43 | 1.00 | 239 |
| stroke 527 | 98 % → 99 % | 1828.0 px | 0.44 | 1.01 | 103 |
| stroke 528 | 100 % → 100 % | 1290.4 px | 0.41 | 1.00 | 336 |
| stroke 529 | 96 % → 99 % | 1330.9 px | 0.37 | 1.04 | 216 |
| stroke 530 | 99 % → 99 % | 861.6 px | 0.39 | 1.00 | 231 |
| stroke 531 | 100 % → 100 % | 732.1 px | 0.39 | 1.00 | 248 |
| stroke 532 | 97 % → 99 % | 1348.2 px | 0.37 | 1.02 | 90 |
| stroke 533 | 92 % → 95 % | 462.8 px | 0.39 | 1.03 | 584 |
| stroke 534 | 93 % → 92 % | 650.0 px | 0.46 | 0.99 | 132 |
| stroke 535 | 98 % → 99 % | 555.6 px | 0.41 | 1.01 | 223 |
| stroke 536 | 97 % → 97 % | 629.7 px | 0.38 | 1.00 | 142 |
| stroke 537 | 98 % → 99 % | 851.0 px | 0.38 | 1.00 | 95 |
| stroke 538 | 97 % → 97 % | 1586.3 px | 0.38 | 1.00 | 45 |
| stroke 539 | 98 % → 98 % | 1338.3 px | 0.40 | 1.00 | 73 |
| stroke 540 | 94 % → 93 % | 1649.2 px | 0.40 | 0.99 | 48 |
| stroke 541 | 99 % → 99 % | 1802.6 px | 0.37 | 1.00 | 48 |
| stroke 542 | 72 % → 71 % | 952.5 px | 0.03 | 0.98 | 14 |
| stroke 543 | 96 % → 96 % | 665.1 px | 0.38 | 1.00 | 123 |
| stroke 544 | 87 % → 87 % | 1822.6 px | 0.34 | 1.01 | 10 |
| stroke 545 | 90 % → 90 % | 843.2 px | 0.41 | 0.99 | 67 |
| stroke 546 | 100 % → 100 % | 2453.1 px | 0.39 | 1.00 | 15 |
| stroke 547 | 98 % → 98 % | 700.0 px | 0.36 | 1.00 | 103 |
| stroke 548 | 97 % → 97 % | 1269.0 px | 0.38 | 1.00 | 37 |

Numbers say: wet paint spreads well beyond the stroke.

## Refs v3 · #25 Yellow heavy stroke — own sheet
own sheet 800 × 1198 · Impasto 1.00 · 272 px · 234.4 s

![Refs v3 · #25 Yellow heavy stroke — own sheet](Refs-v3-25-Yellow-heavy-stroke-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 21 % → 21 % | 224.9 px | 0.15 | 0.97 | 43762 |
| stroke 2 | 28 % → 27 % | 71.7 px | 0.15 | 0.95 | 55110 |
| stroke 3 | 29 % → 17 % | 9.3 px | 0.15 | 0.60 | 75444 |

## Refs v3 · #26 Ink caricature — own sheet
own sheet 800 × 1065 · Ink 0.98 · 64 px · 131.9 s

![Refs v3 · #26 Ink caricature — own sheet](Refs-v3-26-Ink-caricature-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 8 % → 19 % | 21.4 px | 0.75 | 2.48 | 315 |
| stroke 2 | 3 % → 43 % | 66.4 px | 0.78 | 12.98 | 240 |
| stroke 3 | 9 % → 31 % | 51.9 px | 0.78 | 3.54 | 1315 |
| stroke 4 | 5 % → 50 % | 166.7 px | 0.78 | 10.32 | 25 |
| stroke 5 | 6 % → 33 % | 31.6 px | 0.77 | 5.18 | 1017 |
| stroke 6 | 10 % → 37 % | 323.3 px | 0.78 | 3.68 | 25 |
| stroke 7 | 8 % → 40 % | 78.5 px | 0.78 | 4.86 | 202 |
| stroke 8 | 16 % → 35 % | 116.2 px | 0.78 | 2.12 | 1188 |
| stroke 9 | 14 % → 29 % | 101.0 px | 0.78 | 1.99 | 881 |
| stroke 10 | 2 % → 25 % | 40.1 px | 0.76 | 14.45 | 43 |
| stroke 11 | 19 % → 43 % | 132.9 px | 0.78 | 2.32 | 357 |
| stroke 12 | 16 % → 49 % | 286.0 px | 0.78 | 3.02 | 88 |
| stroke 13 | 19 % → 41 % | 126.7 px | 0.78 | 2.16 | 482 |
| stroke 14 | 27 % → 48 % | 353.6 px | 0.78 | 1.77 | 139 |
| stroke 15 | 33 % → 43 % | 529.3 px | 0.78 | 1.32 | 340 |
| stroke 16 | 25 % → 42 % | 495.0 px | 0.78 | 1.71 | 345 |
| stroke 17 | 35 % → 45 % | 296.4 px | 0.78 | 1.29 | 809 |
| stroke 18 | 43 % → 46 % | 778.6 px | 0.78 | 1.06 | 239 |
| stroke 19 | 22 % → 28 % | 126.4 px | 0.77 | 1.31 | 2498 |
| stroke 20 | 37 % → 39 % | 640.7 px | 0.78 | 1.06 | 120 |
| stroke 21 | 21 % → 36 % | 564.9 px | 0.77 | 1.68 | 37 |
| stroke 22 | 36 % → 39 % | 311.4 px | 0.77 | 1.09 | 560 |
| stroke 23 | 19 % → 22 % | 222.6 px | 0.75 | 1.16 | 43 |
| stroke 24 | 33 % → 34 % | 153.1 px | 0.78 | 1.04 | 1284 |
| stroke 25 | 37 % → 38 % | 400.8 px | 0.77 | 1.02 | 144 |
| stroke 26 | 53 % → 54 % | 935.3 px | 0.78 | 1.02 | 78 |
| stroke 27 | 8 % → 23 % | 68.0 px | 0.76 | 2.76 | 172 |
| stroke 28 | 8 % → 19 % | 68.6 px | 0.76 | 2.48 | 130 |
| stroke 29 | 16 % → 28 % | 149.2 px | 0.76 | 1.68 | 186 |
| stroke 30 | 23 % → 27 % | 709.9 px | 0.76 | 1.19 | 30 |
| stroke 31 | 12 % → 22 % | 102.2 px | 0.76 | 1.86 | 163 |
| stroke 32 | 11 % → 17 % | 87.1 px | 0.76 | 1.47 | 421 |
| stroke 33 | 17 % → 25 % | 308.9 px | 0.76 | 1.48 | 61 |
| stroke 34 | 7 % → 13 % | 55.1 px | 0.76 | 1.92 | 338 |
| stroke 35 | 17 % → 27 % | 220.9 px | 0.76 | 1.59 | 72 |
| stroke 36 | 14 % → 21 % | 113.5 px | 0.76 | 1.55 | 229 |
| stroke 37 | 12 % → 20 % | 131.4 px | 0.76 | 1.62 | 122 |
| stroke 38 | 12 % → 20 % | 113.8 px | 0.76 | 1.61 | 116 |
| stroke 39 | 14 % → 18 % | 124.0 px | 0.76 | 1.30 | 100 |
| stroke 40 | 17 % → 19 % | 181.1 px | 0.75 | 1.11 | 164 |
| stroke 41 | 13 % → 13 % | 71.1 px | 0.77 | 1.07 | 248 |
| stroke 42 | 4 % → 4 % | 12.0 px | 0.78 | 1.13 | 80 |

Numbers say: wet paint spreads well beyond the stroke.

## Refs v3 · #27 Orange impasto swatch — own sheet
own sheet 800 × 1000 · Impasto 1.00 · 80 px · 68.9 s

![Refs v3 · #27 Orange impasto swatch — own sheet](Refs-v3-27-Orange-impasto-swatch-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 6 % → 1 % | 76.1 px | 0.19 | 0.17 | 878 |
| stroke 2 | 10 % → 1 % | 91.1 px | 0.19 | 0.08 | 1732 |
| stroke 3 | 13 % → 1 % | 120.1 px | 0.19 | 0.05 | 2256 |
| stroke 4 | 17 % → 1 % | 152.7 px | 0.19 | 0.04 | 3194 |
| stroke 5 | 19 % → 0 % | 486.4 px | 0.00 | 0.00 | 375 |
| stroke 6 | 19 % → 1 % | 150.4 px | 0.19 | 0.03 | 4339 |
| stroke 7 | 23 % → 1 % | 179.2 px | 0.19 | 0.02 | 3672 |
| stroke 8 | 32 % → 1 % | 274.8 px | 0.19 | 0.02 | 2703 |
| stroke 9 | 36 % → 0 % | 323.8 px | 0.19 | 0.01 | 2607 |
| stroke 10 | 38 % → 0 % | 449.2 px | 0.19 | 0.00 | 1355 |
| stroke 11 | 35 % → 0 % | 422.9 px | 0.00 | 0.00 | 1518 |
| stroke 12 | 33 % → 0 % | 471.9 px | 0.00 | 0.00 | 1227 |
| stroke 13 | 31 % → 0 % | 310.6 px | 0.00 | 0.00 | 2088 |
| stroke 14 | 29 % → 0 % | 268.5 px | 0.00 | 0.00 | 2074 |
| stroke 15 | 29 % → 0 % | 265.2 px | 0.00 | 0.00 | 2038 |
| stroke 16 | 31 % → 0 % | 370.2 px | 0.00 | 0.00 | 1142 |
| stroke 17 | 32 % → 0 % | 509.6 px | 0.00 | 0.00 | 978 |
| stroke 18 | 3 % → 0 % | 65.7 px | 0.00 | 0.00 | 209 |
| stroke 19 | 3 % → 0 % | 58.1 px | 0.00 | 0.00 | 720 |
| stroke 20 | 6 % → 0 % | 87.8 px | 0.23 | 0.05 | 710 |
| stroke 21 | 8 % → 1 % | 124.1 px | 0.24 | 0.08 | 590 |
| stroke 22 | 10 % → 1 % | 165.9 px | 0.24 | 0.07 | 665 |
| stroke 23 | 13 % → 1 % | 321.8 px | 0.24 | 0.06 | 312 |
| stroke 24 | 1 % → 1 % | 21.2 px | 0.19 | 0.96 | 94 |
| stroke 25 | 1 % → 1 % | 23.4 px | 0.24 | 0.95 | 62 |

## Refs v3 · #28 Miles Davis lines — own sheet
own sheet 800 × 753 · Ink 0.98 · 18 px · 194.2 s

![Refs v3 · #28 Miles Davis lines — own sheet](Refs-v3-28-Miles-Davis-lines-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 5 % → 0 % | 8.0 px | 0.00 | 0.00 | 43 |
| stroke 2 | 4 % → 0 % | 9.2 px | 0.00 | 0.00 | 7 |
| stroke 3 | 9 % → 0 % | 21.0 px | 0.00 | 0.00 | 10 |
| stroke 4 | 15 % → 0 % | 19.5 px | 0.00 | 0.00 | 27 |
| stroke 5 | 8 % → 0 % | 11.9 px | 0.00 | 0.00 | 23 |
| stroke 6 | 8 % → 0 % | 10.0 px | 0.00 | 0.00 | 21 |
| stroke 7 | 7 % → 0 % | 14.7 px | 0.00 | 0.00 | 22 |
| stroke 8 | 5 % → 26 % | 10.8 px | 0.89 | 4.86 | 5 |
| stroke 9 | 3 % → 56 % | 6.5 px | 0.90 | 20.47 | 18 |
| stroke 10 | 3 % → 76 % | 7.9 px | 0.90 | 23.13 | 15 |
| stroke 11 | 2 % → 65 % | 5.5 px | 0.90 | 41.41 | 8 |
| stroke 12 | 4 % → 21 % | 11.1 px | 0.87 | 5.20 | 15 |
| stroke 13 | 4 % → 81 % | 8.4 px | 0.90 | 18.46 | 14 |
| stroke 14 | 10 % → 80 % | 17.5 px | 0.90 | 7.71 | 22 |
| stroke 15 | 6 % → 55 % | 14.6 px | 0.89 | 9.69 | 24 |
| stroke 16 | 4 % → 69 % | 13.5 px | 0.89 | 15.97 | 20 |
| stroke 17 | 23 % → 32 % | 31.8 px | 0.90 | 1.37 | 275 |
| stroke 18 | 8 % → 22 % | 17.9 px | 0.89 | 2.63 | 89 |
| stroke 19 | 8 % → 30 % | 15.5 px | 0.89 | 3.63 | 51 |
| stroke 20 | 8 % → 42 % | 14.5 px | 0.89 | 5.37 | 57 |
| stroke 21 | 22 % → 74 % | 31.5 px | 0.90 | 3.38 | 197 |
| stroke 22 | 15 % → 45 % | 46.5 px | 0.90 | 3.04 | 21 |
| stroke 23 | 7 % → 65 % | 14.4 px | 0.89 | 8.69 | 54 |
| stroke 24 | 15 % → 57 % | 26.5 px | 0.89 | 3.80 | 72 |
| stroke 25 | 22 % → 40 % | 26.0 px | 0.88 | 1.80 | 230 |
| stroke 26 | 10 % → 14 % | 21.3 px | 0.90 | 1.41 | 362 |
| stroke 27 | 20 % → 39 % | 29.6 px | 0.89 | 1.90 | 1198 |
| stroke 28 | 9 % → 64 % | 40.1 px | 0.89 | 7.06 | 10 |
| stroke 29 | 28 % → 48 % | 45.1 px | 0.90 | 1.73 | 96 |
| stroke 30 | 14 % → 49 % | 18.4 px | 0.87 | 3.56 | 169 |
| stroke 31 | 25 % → 70 % | 32.3 px | 0.90 | 2.83 | 123 |
| stroke 32 | 58 % → 77 % | 71.5 px | 0.90 | 1.34 | 174 |
| stroke 33 | 24 % → 32 % | 29.7 px | 0.89 | 1.32 | 440 |
| stroke 34 | 22 % → 30 % | 42.8 px | 0.89 | 1.36 | 1204 |
| stroke 35 | 14 % → 16 % | 31.3 px | 0.91 | 1.15 | 466 |
| stroke 36 | 17 % → 41 % | 69.6 px | 0.87 | 2.48 | 19 |
| stroke 37 | 19 % → 84 % | 51.4 px | 0.90 | 4.49 | 49 |
| stroke 38 | 27 % → 62 % | 57.5 px | 0.90 | 2.28 | 129 |
| stroke 39 | 9 % → 69 % | 31.9 px | 0.91 | 7.32 | 25 |
| stroke 40 | 4 % → 71 % | 20.3 px | 0.89 | 16.30 | 9 |
| stroke 41 | 11 % → 57 % | 20.4 px | 0.89 | 5.26 | 43 |
| stroke 42 | 27 % → 54 % | 49.5 px | 0.90 | 1.96 | 105 |
| stroke 43 | 8 % → 52 % | 24.9 px | 0.88 | 6.56 | 22 |
| stroke 44 | 8 % → 61 % | 31.2 px | 0.90 | 7.67 | 17 |
| stroke 45 | 11 % → 65 % | 26.4 px | 0.90 | 5.66 | 50 |
| stroke 46 | 20 % → 59 % | 46.8 px | 0.89 | 2.91 | 51 |
| stroke 47 | 11 % → 69 % | 30.2 px | 0.90 | 6.00 | 43 |
| stroke 48 | 27 % → 61 % | 69.0 px | 0.88 | 2.24 | 67 |
| stroke 49 | 24 % → 62 % | 83.0 px | 0.89 | 2.63 | 29 |
| stroke 50 | 28 % → 62 % | 69.7 px | 0.89 | 2.26 | 28 |
| stroke 51 | 26 % → 66 % | 43.9 px | 0.90 | 2.53 | 95 |
| stroke 52 | 21 % → 51 % | 36.8 px | 0.90 | 2.47 | 214 |
| stroke 53 | 23 % → 66 % | 72.7 px | 0.90 | 2.88 | 50 |
| stroke 54 | 22 % → 57 % | 33.3 px | 0.89 | 2.62 | 64 |
| stroke 55 | 36 % → 75 % | 78.3 px | 0.90 | 2.11 | 41 |
| stroke 56 | 42 % → 80 % | 144.6 px | 0.90 | 1.88 | 41 |
| stroke 57 | 19 % → 48 % | 38.4 px | 0.89 | 2.59 | 40 |
| stroke 58 | 50 % → 79 % | 146.3 px | 0.90 | 1.59 | 51 |
| stroke 59 | 51 % → 68 % | 150.5 px | 0.90 | 1.33 | 72 |
| stroke 60 | 20 % → 56 % | 53.2 px | 0.90 | 2.88 | 113 |
| stroke 61 | 26 % → 62 % | 66.0 px | 0.90 | 2.42 | 53 |
| stroke 62 | 27 % → 61 % | 80.2 px | 0.90 | 2.21 | 106 |
| stroke 63 | 21 % → 53 % | 96.9 px | 0.90 | 2.47 | 29 |
| stroke 64 | 19 % → 56 % | 40.5 px | 0.89 | 2.95 | 96 |
| stroke 65 | 20 % → 51 % | 45.6 px | 0.90 | 2.49 | 35 |
| stroke 66 | 37 % → 50 % | 110.9 px | 0.89 | 1.35 | 55 |
| stroke 67 | 31 % → 68 % | 124.0 px | 0.88 | 2.16 | 13 |
| stroke 68 | 8 % → 38 % | 27.0 px | 0.88 | 4.45 | 25 |
| stroke 69 | 13 % → 43 % | 36.6 px | 0.87 | 3.32 | 20 |
| stroke 70 | 35 % → 65 % | 85.2 px | 0.90 | 1.87 | 82 |
| stroke 71 | 60 % → 78 % | 240.7 px | 0.90 | 1.30 | 46 |
| stroke 72 | 55 % → 67 % | 145.7 px | 0.89 | 1.21 | 47 |
| stroke 73 | 40 % → 74 % | 65.8 px | 0.90 | 1.83 | 59 |
| stroke 74 | 31 % → 62 % | 72.8 px | 0.89 | 1.97 | 58 |
| stroke 75 | 53 % → 62 % | 137.9 px | 0.90 | 1.19 | 39 |
| stroke 76 | 58 % → 66 % | 118.4 px | 0.90 | 1.15 | 83 |
| stroke 77 | 28 % → 54 % | 101.3 px | 0.88 | 1.94 | 20 |
| stroke 78 | 21 % → 38 % | 30.5 px | 0.88 | 1.86 | 333 |
| stroke 79 | 40 % → 51 % | 66.2 px | 0.88 | 1.26 | 67 |
| stroke 80 | 53 % → 64 % | 83.3 px | 0.89 | 1.21 | 129 |
| stroke 81 | 41 % → 64 % | 110.5 px | 0.90 | 1.56 | 40 |
| stroke 82 | 44 % → 59 % | 92.2 px | 0.90 | 1.34 | 59 |
| stroke 83 | 21 % → 45 % | 88.6 px | 0.89 | 2.19 | 12 |
| stroke 84 | 36 % → 44 % | 61.9 px | 0.89 | 1.22 | 258 |
| stroke 85 | 46 % → 57 % | 101.2 px | 0.89 | 1.23 | 47 |
| stroke 86 | 52 % → 76 % | 154.1 px | 0.89 | 1.46 | 28 |
| stroke 87 | 63 % → 69 % | 199.5 px | 0.90 | 1.09 | 63 |
| stroke 88 | 54 % → 63 % | 127.2 px | 0.88 | 1.17 | 46 |
| stroke 89 | 21 % → 34 % | 58.6 px | 0.90 | 1.58 | 25 |
| stroke 90 | 20 % → 37 % | 52.3 px | 0.89 | 1.84 | 47 |
| stroke 91 | 6 % → 44 % | 24.9 px | 0.89 | 6.78 | 23 |
| stroke 92 | 45 % → 62 % | 92.3 px | 0.90 | 1.37 | 235 |
| stroke 93 | 43 % → 55 % | 111.4 px | 0.89 | 1.27 | 40 |
| stroke 94 | 51 % → 55 % | 133.0 px | 0.89 | 1.10 | 40 |
| stroke 95 | 25 % → 48 % | 46.6 px | 0.89 | 1.92 | 68 |
| stroke 96 | 22 % → 53 % | 53.3 px | 0.89 | 2.39 | 55 |
| stroke 97 | 36 % → 56 % | 94.5 px | 0.88 | 1.54 | 63 |
| stroke 98 | 70 % → 84 % | 183.5 px | 0.89 | 1.20 | 74 |
| stroke 99 | 32 % → 47 % | 60.6 px | 0.88 | 1.47 | 77 |
| stroke 100 | 58 % → 68 % | 225.9 px | 0.89 | 1.17 | 14 |
| stroke 101 | 65 % → 76 % | 296.5 px | 0.89 | 1.16 | 20 |
| stroke 102 | 20 % → 43 % | 32.1 px | 0.89 | 2.17 | 95 |
| stroke 103 | 27 % → 32 % | 68.7 px | 0.90 | 1.19 | 29 |
| stroke 104 | 25 % → 33 % | 41.1 px | 0.89 | 1.33 | 113 |
| stroke 105 | 66 % → 74 % | 208.4 px | 0.89 | 1.13 | 21 |
| stroke 106 | 69 % → 69 % | 192.7 px | 0.90 | 1.01 | 35 |
| stroke 107 | 34 % → 44 % | 107.5 px | 0.90 | 1.30 | 27 |
| stroke 108 | 42 % → 57 % | 89.7 px | 0.89 | 1.35 | 78 |
| stroke 109 | 64 % → 71 % | 149.8 px | 0.90 | 1.11 | 59 |
| stroke 110 | 42 % → 49 % | 182.2 px | 0.89 | 1.17 | 13 |
| stroke 111 | 26 % → 44 % | 54.5 px | 0.89 | 1.68 | 45 |
| stroke 112 | 46 % → 49 % | 74.2 px | 0.89 | 1.06 | 141 |
| stroke 113 | 53 % → 56 % | 158.5 px | 0.90 | 1.07 | 26 |
| stroke 114 | 46 % → 51 % | 58.4 px | 0.89 | 1.12 | 242 |
| stroke 115 | 55 % → 64 % | 145.8 px | 0.89 | 1.17 | 46 |
| stroke 116 | 61 % → 62 % | 195.4 px | 0.89 | 1.01 | 31 |
| stroke 117 | 68 % → 72 % | 197.3 px | 0.89 | 1.05 | 39 |
| stroke 118 | 23 % → 49 % | 58.1 px | 0.89 | 2.17 | 28 |
| stroke 119 | 70 % → 72 % | 220.6 px | 0.90 | 1.02 | 34 |
| stroke 120 | 49 % → 49 % | 88.1 px | 0.90 | 1.01 | 194 |
| stroke 121 | 70 % → 70 % | 324.3 px | 0.90 | 1.00 | 26 |
| stroke 122 | 40 % → 45 % | 106.1 px | 0.89 | 1.12 | 121 |
| stroke 123 | 35 % → 38 % | 123.3 px | 0.89 | 1.07 | 45 |
| stroke 124 | 87 % → 87 % | 228.2 px | 0.90 | 1.00 | 65 |
| stroke 125 | 52 % → 54 % | 208.9 px | 0.88 | 1.03 | 17 |
| stroke 126 | 70 % → 72 % | 260.2 px | 0.89 | 1.02 | 21 |
| stroke 127 | 38 % → 39 % | 148.0 px | 0.90 | 1.03 | 41 |
| stroke 128 | 56 % → 58 % | 236.9 px | 0.89 | 1.04 | 15 |
| stroke 129 | 33 % → 50 % | 43.6 px | 0.88 | 1.50 | 169 |
| stroke 130 | 35 % → 52 % | 44.1 px | 0.90 | 1.50 | 121 |
| stroke 131 | 41 % → 52 % | 54.9 px | 0.89 | 1.29 | 121 |
| stroke 132 | 58 % → 61 % | 147.1 px | 0.90 | 1.05 | 97 |

Numbers say: wet paint spreads well beyond the stroke.

## Refs v3 · #29 Shrigley asterisk — own sheet
own sheet 800 × 1028 · Watercolour 1.00 + water 50 % · 64 px · 147.2 s

![Refs v3 · #29 Shrigley asterisk — own sheet](Refs-v3-29-Shrigley-asterisk-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 15 % → 46 % | 72.5 px | 0.52 | 3.03 | 1442 |
| stroke 2 | 25 % → 54 % | 108.3 px | 0.50 | 2.20 | 1665 |
| stroke 3 | 8 % → 28 % | 79.4 px | 0.50 | 3.45 | 241 |
| stroke 4 | 23 % → 37 % | 112.2 px | 0.51 | 1.65 | 5732 |
| stroke 5 | 31 % → 47 % | 154.1 px | 0.50 | 1.51 | 2010 |
| stroke 6 | 31 % → 38 % | 141.7 px | 0.50 | 1.23 | 3296 |
| stroke 7 | 34 % → 37 % | 188.6 px | 0.52 | 1.09 | 2963 |
| stroke 8 | 31 % → 32 % | 179.5 px | 0.51 | 1.04 | 5185 |
| stroke 9 | 63 % → 68 % | 828.3 px | 0.50 | 1.08 | 897 |
| stroke 10 | 73 % → 82 % | 1351.3 px | 0.50 | 1.12 | 563 |
| stroke 11 | 59 % → 70 % | 808.5 px | 0.50 | 1.18 | 697 |
| stroke 12 | 67 % → 71 % | 980.2 px | 0.50 | 1.07 | 572 |
| stroke 13 | 41 % → 41 % | 276.8 px | 0.50 | 0.98 | 2832 |

Numbers say: wet paint spreads well beyond the stroke.

## Refs v3 · #30 Red gouache face — own sheet
own sheet 800 × 1084 · Gouache 1.00 + water 15 % · 76 px · 928.1 s

![Refs v3 · #30 Red gouache face — own sheet](Refs-v3-30-Red-gouache-face-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 10 % → 79 % | 70.1 px | 0.51 | 8.12 | 1869 |
| stroke 2 | 15 % → 93 % | 106.9 px | 0.51 | 6.06 | 2248 |
| stroke 3 | 20 % → 98 % | 147.3 px | 0.51 | 4.96 | 3343 |
| stroke 4 | 13 % → 68 % | 124.3 px | 0.52 | 5.21 | 1522 |
| stroke 5 | 24 % → 80 % | 175.0 px | 0.52 | 3.27 | 2568 |
| stroke 6 | 21 % → 62 % | 157.5 px | 0.50 | 3.01 | 1975 |
| stroke 7 | 38 % → 96 % | 330.4 px | 0.50 | 2.52 | 1409 |
| stroke 8 | 18 % → 73 % | 144.4 px | 0.51 | 3.96 | 2816 |
| stroke 9 | 42 % → 82 % | 276.8 px | 0.51 | 1.94 | 2884 |
| stroke 10 | 22 % → 80 % | 210.0 px | 0.52 | 3.57 | 1924 |
| stroke 11 | 51 % → 79 % | 475.9 px | 0.50 | 1.55 | 1868 |
| stroke 12 | 48 % → 96 % | 378.1 px | 0.52 | 2.02 | 2225 |
| stroke 13 | 50 % → 90 % | 567.5 px | 0.51 | 1.81 | 1386 |
| stroke 14 | 42 % → 80 % | 375.6 px | 0.51 | 1.89 | 2694 |
| stroke 15 | 49 % → 87 % | 516.0 px | 0.52 | 1.77 | 1880 |
| stroke 16 | 46 % → 77 % | 334.2 px | 0.51 | 1.68 | 2945 |
| stroke 17 | 62 % → 83 % | 1165.1 px | 0.50 | 1.35 | 740 |
| stroke 18 | 71 % → 98 % | 833.4 px | 0.49 | 1.38 | 1045 |
| stroke 19 | 54 % → 95 % | 428.6 px | 0.51 | 1.74 | 2425 |
| stroke 20 | 32 % → 82 % | 435.1 px | 0.53 | 2.54 | 1158 |
| stroke 21 | 49 % → 79 % | 365.8 px | 0.52 | 1.62 | 2256 |
| stroke 22 | 70 % → 97 % | 745.1 px | 0.50 | 1.39 | 1510 |
| stroke 23 | 63 % → 88 % | 777.9 px | 0.51 | 1.38 | 1277 |
| stroke 24 | 35 % → 75 % | 308.9 px | 0.52 | 2.15 | 2517 |
| stroke 25 | 34 % → 76 % | 442.5 px | 0.53 | 2.28 | 924 |
| stroke 26 | 75 % → 99 % | 1373.9 px | 0.49 | 1.31 | 619 |
| stroke 27 | 40 % → 77 % | 408.1 px | 0.51 | 1.92 | 1775 |
| stroke 28 | 46 % → 89 % | 813.1 px | 0.53 | 1.94 | 643 |
| stroke 29 | 48 % → 81 % | 462.8 px | 0.51 | 1.70 | 1967 |
| stroke 30 | 50 % → 80 % | 763.1 px | 0.51 | 1.60 | 1007 |
| stroke 31 | 33 % → 65 % | 363.5 px | 0.52 | 1.95 | 856 |
| stroke 32 | 77 % → 98 % | 1066.0 px | 0.51 | 1.27 | 889 |
| stroke 33 | 59 % → 94 % | 1042.0 px | 0.52 | 1.60 | 642 |
| stroke 34 | 53 % → 82 % | 858.4 px | 0.51 | 1.56 | 831 |
| stroke 35 | 55 % → 86 % | 1025.6 px | 0.51 | 1.56 | 805 |
| stroke 36 | 59 % → 85 % | 703.7 px | 0.51 | 1.44 | 1020 |
| stroke 37 | 83 % → 97 % | 1531.8 px | 0.49 | 1.17 | 621 |
| stroke 38 | 66 % → 75 % | 884.9 px | 0.50 | 1.15 | 805 |
| stroke 39 | 65 % → 92 % | 684.3 px | 0.51 | 1.40 | 1124 |
| stroke 40 | 70 % → 90 % | 816.0 px | 0.52 | 1.29 | 1531 |
| stroke 41 | 50 % → 82 % | 584.8 px | 0.50 | 1.65 | 1447 |
| stroke 42 | 67 % → 75 % | 1215.0 px | 0.49 | 1.12 | 813 |
| stroke 43 | 45 % → 72 % | 690.3 px | 0.51 | 1.61 | 676 |
| stroke 44 | 77 % → 99 % | 891.6 px | 0.51 | 1.29 | 1409 |
| stroke 45 | 82 % → 98 % | 1284.9 px | 0.51 | 1.20 | 707 |
| stroke 46 | 37 % → 68 % | 605.2 px | 0.52 | 1.81 | 692 |
| stroke 47 | 83 % → 99 % | 1187.6 px | 0.51 | 1.19 | 687 |
| stroke 48 | 92 % → 99 % | 1659.0 px | 0.50 | 1.07 | 502 |
| stroke 49 | 85 % → 98 % | 1431.2 px | 0.51 | 1.16 | 858 |
| stroke 50 | 77 % → 93 % | 1338.1 px | 0.51 | 1.22 | 976 |
| stroke 51 | 84 % → 98 % | 1481.2 px | 0.50 | 1.16 | 737 |
| stroke 52 | 47 % → 64 % | 445.8 px | 0.50 | 1.34 | 1495 |
| stroke 53 | 52 % → 61 % | 679.8 px | 0.48 | 1.18 | 894 |
| stroke 54 | 73 % → 93 % | 971.8 px | 0.51 | 1.27 | 180 |
| stroke 55 | 51 % → 73 % | 1202.0 px | 0.51 | 1.42 | 35 |
| stroke 56 | 83 % → 96 % | 3679.9 px | 0.51 | 1.16 | 12 |
| stroke 57 | 34 % → 68 % | 1111.9 px | 0.53 | 2.01 | 65 |
| stroke 58 | 34 % → 55 % | 861.1 px | 0.50 | 1.63 | 51 |
| stroke 59 | 31 % → 53 % | 391.2 px | 0.50 | 1.70 | 157 |
| stroke 60 | 35 % → 57 % | 523.4 px | 0.51 | 1.62 | 99 |
| stroke 61 | 38 % → 57 % | 1257.6 px | 0.50 | 1.49 | 28 |
| stroke 62 | 41 % → 61 % | 598.2 px | 0.51 | 1.46 | 141 |
| stroke 63 | 45 % → 70 % | 1786.4 px | 0.52 | 1.58 | 22 |
| stroke 64 | 45 % → 84 % | 837.6 px | 0.53 | 1.88 | 18 |
| stroke 65 | 56 % → 86 % | 1225.1 px | 0.52 | 1.54 | 28 |
| stroke 66 | 49 % → 72 % | 1156.2 px | 0.52 | 1.48 | 37 |
| stroke 67 | 58 % → 71 % | 1670.9 px | 0.49 | 1.23 | 25 |
| stroke 68 | 54 % → 77 % | 1184.8 px | 0.52 | 1.42 | 26 |
| stroke 69 | 35 % → 73 % | 996.2 px | 0.54 | 2.10 | 42 |
| stroke 70 | 32 % → 67 % | 831.8 px | 0.54 | 2.10 | 49 |
| stroke 71 | 27 % → 58 % | 449.1 px | 0.54 | 2.12 | 95 |
| stroke 72 | 34 % → 63 % | 1080.4 px | 0.54 | 1.86 | 19 |
| stroke 73 | 29 % → 62 % | 618.1 px | 0.55 | 2.12 | 63 |
| stroke 74 | 46 % → 65 % | 301.0 px | 0.52 | 1.42 | 1105 |
| stroke 75 | 87 % → 99 % | 730.4 px | 0.51 | 1.14 | 1285 |
| stroke 76 | 44 % → 51 % | 342.3 px | 0.51 | 1.15 | 848 |
| stroke 77 | 39 % → 66 % | 397.2 px | 0.54 | 1.71 | 1603 |
| stroke 78 | 45 % → 60 % | 553.1 px | 0.51 | 1.34 | 448 |
| stroke 79 | 53 % → 76 % | 400.7 px | 0.52 | 1.43 | 1133 |
| stroke 80 | 53 % → 69 % | 517.2 px | 0.51 | 1.29 | 1329 |
| stroke 81 | 39 % → 54 % | 269.5 px | 0.54 | 1.39 | 902 |
| stroke 82 | 48 % → 67 % | 664.0 px | 0.54 | 1.39 | 327 |
| stroke 83 | 78 % → 85 % | 637.4 px | 0.50 | 1.09 | 1349 |
| stroke 84 | 96 % → 99 % | 1202.7 px | 0.50 | 1.03 | 683 |
| stroke 85 | 46 % → 58 % | 530.1 px | 0.53 | 1.26 | 640 |
| stroke 86 | 52 % → 62 % | 419.4 px | 0.52 | 1.18 | 1435 |
| stroke 87 | 50 % → 54 % | 482.7 px | 0.51 | 1.08 | 759 |
| stroke 88 | 80 % → 87 % | 910.9 px | 0.51 | 1.08 | 686 |
| stroke 89 | 59 % → 68 % | 756.9 px | 0.53 | 1.15 | 634 |
| stroke 90 | 65 % → 72 % | 628.3 px | 0.50 | 1.10 | 736 |
| stroke 91 | 93 % → 97 % | 1446.0 px | 0.50 | 1.04 | 587 |
| stroke 92 | 95 % → 99 % | 1113.6 px | 0.51 | 1.04 | 672 |
| stroke 93 | 47 % → 53 % | 1116.6 px | 0.53 | 1.13 | 279 |
| stroke 94 | 85 % → 90 % | 1224.7 px | 0.50 | 1.06 | 731 |
| stroke 95 | 83 % → 87 % | 1349.3 px | 0.51 | 1.05 | 506 |
| stroke 96 | 46 % → 57 % | 1047.8 px | 0.54 | 1.25 | 243 |
| stroke 97 | 86 % → 89 % | 1084.4 px | 0.50 | 1.03 | 549 |
| stroke 98 | 66 % → 68 % | 1076.4 px | 0.49 | 1.04 | 441 |
| stroke 99 | 75 % → 80 % | 1926.8 px | 0.51 | 1.07 | 1278 |
| stroke 100 | 71 % → 71 % | 522.9 px | 0.50 | 1.00 | 1284 |
| stroke 101 | 50 % → 65 % | 688.5 px | 0.55 | 1.30 | 361 |
| stroke 102 | 97 % → 99 % | 1050.1 px | 0.51 | 1.02 | 1177 |
| stroke 103 | 58 % → 61 % | 1089.2 px | 0.52 | 1.05 | 409 |
| stroke 104 | 93 % → 95 % | 1554.0 px | 0.50 | 1.01 | 675 |
| stroke 105 | 56 % → 77 % | 419.8 px | 0.53 | 1.38 | 723 |
| stroke 106 | 63 % → 71 % | 773.5 px | 0.54 | 1.14 | 768 |
| stroke 107 | 51 % → 80 % | 692.0 px | 0.54 | 1.58 | 170 |
| stroke 108 | 44 % → 49 % | 841.7 px | 0.54 | 1.11 | 408 |
| stroke 109 | 66 % → 72 % | 1006.8 px | 0.54 | 1.10 | 511 |
| stroke 110 | 62 % → 65 % | 998.5 px | 0.53 | 1.05 | 612 |
| stroke 111 | 75 % → 75 % | 849.4 px | 0.50 | 1.00 | 532 |
| stroke 112 | 53 % → 56 % | 584.1 px | 0.51 | 1.05 | 585 |
| stroke 113 | 74 % → 74 % | 1453.4 px | 0.52 | 1.00 | 360 |
| stroke 114 | 69 % → 75 % | 820.1 px | 0.52 | 1.09 | 360 |
| stroke 115 | 46 % → 48 % | 496.4 px | 0.55 | 1.04 | 363 |
| stroke 116 | 49 % → 50 % | 832.0 px | 0.54 | 1.02 | 266 |
| stroke 117 | 77 % → 77 % | 1887.2 px | 0.51 | 1.00 | 223 |
| stroke 118 | 44 % → 45 % | 1182.4 px | 0.54 | 1.02 | 156 |
| stroke 119 | 53 % → 53 % | 608.0 px | 0.55 | 1.00 | 316 |
| stroke 120 | 74 % → 74 % | 1052.1 px | 0.51 | 1.00 | 355 |
| stroke 121 | 99 % → 99 % | 2657.8 px | 0.50 | 1.01 | 227 |
| stroke 122 | 50 % → 50 % | 396.4 px | 0.51 | 1.00 | 1051 |
| stroke 123 | 93 % → 95 % | 2094.8 px | 0.51 | 1.01 | 243 |
| stroke 124 | 69 % → 76 % | 1504.9 px | 0.52 | 1.10 | 367 |
| stroke 125 | 68 % → 81 % | 1100.7 px | 0.52 | 1.20 | 737 |
| stroke 126 | 94 % → 96 % | 1979.0 px | 0.52 | 1.01 | 415 |
| stroke 127 | 94 % → 95 % | 2319.2 px | 0.51 | 1.01 | 399 |
| stroke 128 | 97 % → 97 % | 2043.1 px | 0.50 | 1.00 | 573 |
| stroke 129 | 67 % → 69 % | 1003.1 px | 0.54 | 1.02 | 657 |
| stroke 130 | 76 % → 77 % | 2037.8 px | 0.54 | 1.01 | 599 |
| stroke 131 | 62 % → 63 % | 1340.8 px | 0.53 | 1.01 | 408 |
| stroke 132 | 71 % → 70 % | 1592.4 px | 0.53 | 0.99 | 180 |
| stroke 133 | 47 % → 66 % | 348.4 px | 0.51 | 1.40 | 639 |
| stroke 134 | 59 % → 73 % | 395.3 px | 0.51 | 1.24 | 857 |
| stroke 135 | 79 % → 88 % | 741.5 px | 0.52 | 1.12 | 745 |
| stroke 136 | 58 % → 62 % | 384.0 px | 0.51 | 1.07 | 579 |
| stroke 137 | 83 % → 87 % | 864.9 px | 0.52 | 1.05 | 439 |
| stroke 138 | 64 % → 69 % | 587.6 px | 0.51 | 1.08 | 769 |
| stroke 139 | 84 % → 87 % | 1297.3 px | 0.52 | 1.04 | 287 |
| stroke 140 | 84 % → 88 % | 1132.4 px | 0.52 | 1.05 | 374 |
| stroke 141 | 64 % → 65 % | 1496.7 px | 0.51 | 1.03 | 221 |
| stroke 142 | 57 % → 59 % | 822.9 px | 0.51 | 1.03 | 291 |
| stroke 143 | 60 % → 60 % | 716.1 px | 0.51 | 1.00 | 300 |
| stroke 144 | 83 % → 86 % | 1358.5 px | 0.52 | 1.03 | 314 |
| stroke 145 | 95 % → 97 % | 925.2 px | 0.50 | 1.02 | 965 |
| stroke 146 | 97 % → 99 % | 1104.7 px | 0.50 | 1.02 | 707 |
| stroke 147 | 97 % → 99 % | 1523.2 px | 0.51 | 1.02 | 810 |
| stroke 148 | 98 % → 99 % | 1705.8 px | 0.50 | 1.01 | 439 |
| stroke 149 | 97 % → 97 % | 993.8 px | 0.51 | 1.00 | 860 |
| stroke 150 | 99 % → 99 % | 2011.8 px | 0.50 | 1.00 | 349 |
| stroke 151 | 96 % → 96 % | 2231.2 px | 0.51 | 1.00 | 299 |
| stroke 152 | 99 % → 99 % | 2168.5 px | 0.49 | 1.00 | 319 |
| stroke 153 | 62 % → 62 % | 364.1 px | 0.50 | 1.00 | 1446 |
| stroke 154 | 87 % → 87 % | 905.5 px | 0.52 | 1.00 | 1130 |

Numbers say: wet paint spreads well beyond the stroke.

## Refs v3 · #31 Warhol blotted line — own sheet
own sheet 800 × 708 · Ink 0.98 · 25 px · 119.9 s

![Refs v3 · #31 Warhol blotted line — own sheet](Refs-v3-31-Warhol-blotted-line-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 1 % → 17 % | 10.1 px | 0.56 | 12.70 | 19 |
| stroke 2 | 2 % → 45 % | 11.1 px | 0.55 | 22.56 | 8 |
| stroke 3 | 2 % → 38 % | 14.5 px | 0.55 | 15.56 | 11 |
| stroke 4 | 1 % → 50 % | 11.6 px | 0.55 | 33.44 | 6 |
| stroke 5 | 2 % → 49 % | 10.3 px | 0.55 | 29.69 | 8 |
| stroke 6 | 5 % → 51 % | 33.1 px | 0.55 | 9.57 | 13 |
| stroke 7 | 4 % → 54 % | 23.6 px | 0.56 | 13.65 | 10 |
| stroke 8 | 2 % → 38 % | 11.3 px | 0.58 | 17.25 | 18 |
| stroke 9 | 5 % → 22 % | 13.6 px | 0.57 | 4.58 | 89 |
| stroke 10 | 4 % → 30 % | 18.9 px | 0.55 | 8.55 | 30 |
| stroke 11 | 4 % → 40 % | 26.2 px | 0.56 | 9.51 | 7 |
| stroke 12 | 6 % → 42 % | 30.4 px | 0.56 | 7.39 | 12 |
| stroke 13 | 7 % → 38 % | 38.5 px | 0.56 | 5.13 | 13 |
| stroke 14 | 6 % → 28 % | 18.9 px | 0.57 | 4.28 | 98 |
| stroke 15 | 6 % → 12 % | 18.7 px | 0.56 | 1.81 | 41 |
| stroke 16 | 2 % → 20 % | 12.9 px | 0.55 | 8.61 | 15 |
| stroke 17 | 6 % → 57 % | 52.6 px | 0.56 | 9.11 | 7 |
| stroke 18 | 16 % → 41 % | 52.2 px | 0.57 | 2.52 | 60 |
| stroke 19 | 9 % → 28 % | 41.1 px | 0.55 | 3.04 | 25 |
| stroke 20 | 10 % → 38 % | 74.0 px | 0.57 | 3.70 | 12 |
| stroke 21 | 1 % → 35 % | 8.6 px | 0.57 | 35.61 | 6 |
| stroke 22 | 5 % → 21 % | 12.6 px | 0.58 | 4.39 | 143 |
| stroke 23 | 3 % → 26 % | 10.5 px | 0.55 | 8.54 | 31 |
| stroke 24 | 4 % → 32 % | 12.5 px | 0.56 | 8.22 | 43 |
| stroke 25 | 11 % → 31 % | 50.5 px | 0.56 | 2.74 | 23 |
| stroke 26 | 11 % → 24 % | 47.9 px | 0.54 | 2.15 | 26 |
| stroke 27 | 9 % → 53 % | 41.3 px | 0.56 | 5.81 | 19 |
| stroke 28 | 8 % → 39 % | 63.3 px | 0.55 | 5.19 | 10 |
| stroke 29 | 11 % → 58 % | 55.9 px | 0.56 | 5.33 | 12 |
| stroke 30 | 3 % → 31 % | 13.1 px | 0.55 | 9.16 | 35 |
| stroke 31 | 12 % → 49 % | 40.5 px | 0.57 | 4.18 | 38 |
| stroke 32 | 4 % → 34 % | 16.6 px | 0.56 | 9.21 | 30 |
| stroke 33 | 9 % → 28 % | 42.7 px | 0.57 | 3.06 | 38 |
| stroke 34 | 9 % → 34 % | 71.5 px | 0.56 | 3.64 | 10 |
| stroke 35 | 12 % → 22 % | 33.0 px | 0.57 | 1.82 | 154 |
| stroke 36 | 7 % → 45 % | 23.7 px | 0.55 | 6.16 | 48 |
| stroke 37 | 14 % → 44 % | 58.5 px | 0.56 | 3.27 | 22 |
| stroke 38 | 14 % → 44 % | 95.2 px | 0.55 | 3.24 | 6 |
| stroke 39 | 6 % → 33 % | 23.1 px | 0.56 | 5.35 | 24 |
| stroke 40 | 13 % → 41 % | 73.6 px | 0.55 | 3.14 | 15 |
| stroke 41 | 5 % → 35 % | 19.2 px | 0.56 | 6.65 | 29 |
| stroke 42 | 8 % → 37 % | 32.7 px | 0.57 | 4.79 | 14 |
| stroke 43 | 16 % → 45 % | 54.2 px | 0.55 | 2.91 | 44 |
| stroke 44 | 14 % → 39 % | 45.3 px | 0.55 | 2.71 | 33 |
| stroke 45 | 21 % → 58 % | 118.0 px | 0.56 | 2.69 | 20 |
| stroke 46 | 7 % → 37 % | 53.0 px | 0.56 | 5.35 | 7 |
| stroke 47 | 13 % → 32 % | 56.5 px | 0.55 | 2.44 | 20 |
| stroke 48 | 18 % → 30 % | 69.5 px | 0.55 | 1.67 | 14 |
| stroke 49 | 25 % → 41 % | 145.6 px | 0.57 | 1.63 | 20 |
| stroke 50 | 26 % → 58 % | 175.3 px | 0.56 | 2.23 | 12 |
| stroke 51 | 20 % → 43 % | 69.9 px | 0.57 | 2.12 | 43 |
| stroke 52 | 14 % → 30 % | 48.4 px | 0.54 | 2.15 | 46 |
| stroke 53 | 11 % → 16 % | 28.7 px | 0.57 | 1.52 | 135 |
| stroke 54 | 19 % → 51 % | 77.7 px | 0.56 | 2.68 | 16 |
| stroke 55 | 3 % → 34 % | 20.7 px | 0.56 | 11.47 | 11 |
| stroke 56 | 31 % → 43 % | 113.7 px | 0.56 | 1.40 | 29 |
| stroke 57 | 15 % → 22 % | 34.5 px | 0.57 | 1.49 | 184 |
| stroke 58 | 21 % → 55 % | 145.4 px | 0.56 | 2.61 | 15 |
| stroke 59 | 31 % → 42 % | 122.4 px | 0.57 | 1.33 | 33 |
| stroke 60 | 30 % → 43 % | 111.7 px | 0.55 | 1.44 | 27 |
| stroke 61 | 11 % → 38 % | 46.7 px | 0.56 | 3.39 | 21 |
| stroke 62 | 23 % → 45 % | 102.3 px | 0.56 | 1.99 | 17 |
| stroke 63 | 25 % → 46 % | 158.6 px | 0.55 | 1.85 | 11 |
| stroke 64 | 21 % → 47 % | 86.5 px | 0.57 | 2.30 | 23 |
| stroke 65 | 21 % → 33 % | 80.3 px | 0.57 | 1.57 | 36 |
| stroke 66 | 20 % → 35 % | 107.7 px | 0.55 | 1.78 | 11 |
| stroke 67 | 20 % → 34 % | 91.1 px | 0.57 | 1.70 | 24 |
| stroke 68 | 11 % → 34 % | 38.4 px | 0.56 | 3.10 | 59 |
| stroke 69 | 16 % → 36 % | 66.3 px | 0.56 | 2.16 | 27 |
| stroke 70 | 29 % → 44 % | 163.8 px | 0.56 | 1.54 | 18 |
| stroke 71 | 21 % → 43 % | 154.6 px | 0.56 | 2.10 | 6 |
| stroke 72 | 27 % → 42 % | 217.5 px | 0.55 | 1.56 | 8 |
| stroke 73 | 28 % → 42 % | 224.8 px | 0.55 | 1.49 | 7 |
| stroke 74 | 30 % → 50 % | 108.2 px | 0.56 | 1.65 | 38 |
| stroke 75 | 12 % → 26 % | 53.3 px | 0.56 | 2.13 | 14 |
| stroke 76 | 33 % → 53 % | 153.3 px | 0.56 | 1.62 | 20 |
| stroke 77 | 18 % → 21 % | 49.6 px | 0.58 | 1.18 | 117 |
| stroke 78 | 22 % → 36 % | 160.5 px | 0.57 | 1.60 | 15 |
| stroke 79 | 18 % → 33 % | 37.9 px | 0.57 | 1.84 | 81 |
| stroke 80 | 25 % → 39 % | 175.7 px | 0.56 | 1.54 | 17 |
| stroke 81 | 29 % → 46 % | 238.3 px | 0.55 | 1.61 | 5 |
| stroke 82 | 15 % → 33 % | 62.4 px | 0.56 | 2.27 | 40 |
| stroke 83 | 24 % → 34 % | 77.0 px | 0.56 | 1.40 | 28 |
| stroke 84 | 30 % → 40 % | 251.5 px | 0.55 | 1.30 | 9 |
| stroke 85 | 34 % → 46 % | 127.4 px | 0.56 | 1.35 | 34 |
| stroke 86 | 35 % → 47 % | 226.4 px | 0.55 | 1.32 | 14 |
| stroke 87 | 17 % → 36 % | 145.2 px | 0.57 | 2.15 | 7 |
| stroke 88 | 30 % → 39 % | 155.6 px | 0.56 | 1.31 | 28 |
| stroke 89 | 37 % → 45 % | 164.5 px | 0.55 | 1.21 | 21 |
| stroke 90 | 43 % → 52 % | 242.0 px | 0.55 | 1.20 | 13 |
| stroke 91 | 23 % → 35 % | 94.9 px | 0.57 | 1.56 | 28 |
| stroke 92 | 20 % → 32 % | 68.5 px | 0.55 | 1.65 | 40 |
| stroke 93 | 24 % → 31 % | 70.9 px | 0.56 | 1.27 | 74 |
| stroke 94 | 27 % → 37 % | 225.2 px | 0.55 | 1.35 | 11 |
| stroke 95 | 25 % → 30 % | 80.5 px | 0.56 | 1.20 | 41 |
| stroke 96 | 23 % → 34 % | 169.3 px | 0.57 | 1.51 | 7 |
| stroke 97 | 39 % → 49 % | 175.2 px | 0.56 | 1.27 | 18 |
| stroke 98 | 46 % → 48 % | 153.3 px | 0.56 | 1.05 | 84 |
| stroke 99 | 13 % → 14 % | 51.3 px | 0.58 | 1.08 | 441 |
| stroke 100 | 24 % → 26 % | 180.0 px | 0.55 | 1.06 | 6 |
| stroke 101 | 9 % → 24 % | 35.9 px | 0.56 | 2.68 | 26 |
| stroke 102 | 37 % → 43 % | 137.2 px | 0.55 | 1.18 | 53 |
| stroke 103 | 21 % → 36 % | 80.9 px | 0.55 | 1.72 | 28 |
| stroke 104 | 37 % → 38 % | 285.0 px | 0.55 | 1.03 | 10 |
| stroke 105 | 37 % → 38 % | 126.5 px | 0.57 | 1.02 | 53 |
| stroke 106 | 32 % → 42 % | 135.5 px | 0.56 | 1.30 | 26 |
| stroke 107 | 21 % → 36 % | 159.3 px | 0.56 | 1.75 | 5 |
| stroke 108 | 34 % → 36 % | 111.6 px | 0.55 | 1.06 | 36 |
| stroke 109 | 30 % → 34 % | 198.2 px | 0.55 | 1.12 | 12 |
| stroke 110 | 24 % → 29 % | 92.7 px | 0.56 | 1.20 | 25 |
| stroke 111 | 21 % → 26 % | 54.1 px | 0.56 | 1.26 | 120 |
| stroke 112 | 43 % → 45 % | 219.7 px | 0.56 | 1.04 | 24 |
| stroke 113 | 61 % → 62 % | 413.2 px | 0.56 | 1.02 | 13 |
| stroke 114 | 33 % → 37 % | 208.5 px | 0.55 | 1.10 | 28 |
| stroke 115 | 19 % → 24 % | 69.9 px | 0.56 | 1.29 | 40 |
| stroke 116 | 39 % → 49 % | 147.2 px | 0.56 | 1.24 | 46 |
| stroke 117 | 32 % → 39 % | 133.3 px | 0.55 | 1.23 | 16 |
| stroke 118 | 31 % → 32 % | 176.2 px | 0.56 | 1.05 | 14 |
| stroke 119 | 36 % → 37 % | 142.4 px | 0.56 | 1.03 | 45 |
| stroke 120 | 31 % → 33 % | 132.9 px | 0.56 | 1.06 | 23 |
| stroke 121 | 28 % → 38 % | 139.1 px | 0.55 | 1.38 | 43 |
| stroke 122 | 40 % → 45 % | 178.7 px | 0.56 | 1.13 | 35 |
| stroke 123 | 32 % → 36 % | 154.9 px | 0.56 | 1.14 | 16 |
| stroke 124 | 43 % → 45 % | 228.9 px | 0.55 | 1.05 | 16 |

Numbers say: wet paint spreads well beyond the stroke.

## Refs v3 · #32 Thick orange swipes — own sheet
own sheet 800 × 800 · Impasto 1.00 · 76 px · 127.0 s

![Refs v3 · #32 Thick orange swipes — own sheet](Refs-v3-32-Thick-orange-swipes-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 14 % → 22 % | 68.6 px | 0.32 | 1.63 | 2489 |
| stroke 2 | 19 % → 32 % | 154.9 px | 0.32 | 1.69 | 1558 |
| stroke 3 | 15 % → 30 % | 277.8 px | 0.32 | 2.01 | 583 |
| stroke 4 | 22 % → 34 % | 217.6 px | 0.32 | 1.51 | 1702 |
| stroke 5 | 16 % → 34 % | 370.3 px | 0.32 | 2.09 | 440 |
| stroke 6 | 25 % → 33 % | 348.5 px | 0.31 | 1.32 | 1044 |
| stroke 7 | 18 % → 38 % | 418.4 px | 0.32 | 2.13 | 475 |
| stroke 8 | 27 % → 31 % | 459.3 px | 0.31 | 1.17 | 639 |
| stroke 9 | 25 % → 32 % | 486.6 px | 0.31 | 1.29 | 507 |
| stroke 10 | 22 % → 34 % | 437.9 px | 0.31 | 1.54 | 378 |
| stroke 11 | 13 % → 49 % | 296.3 px | 0.32 | 3.77 | 276 |
| stroke 12 | 19 % → 37 % | 365.2 px | 0.32 | 1.97 | 426 |
| stroke 13 | 16 % → 61 % | 136.6 px | 0.32 | 3.75 | 1810 |
| stroke 14 | 16 % → 40 % | 280.9 px | 0.32 | 2.50 | 518 |
| stroke 15 | 16 % → 45 % | 210.0 px | 0.32 | 2.80 | 720 |
| stroke 16 | 18 % → 49 % | 182.4 px | 0.32 | 2.72 | 1161 |
| stroke 17 | 19 % → 46 % | 213.6 px | 0.33 | 2.45 | 1177 |
| stroke 18 | 20 % → 44 % | 240.1 px | 0.33 | 2.23 | 797 |
| stroke 19 | 21 % → 35 % | 355.8 px | 0.33 | 1.71 | 515 |
| stroke 20 | 20 % → 32 % | 386.4 px | 0.34 | 1.59 | 462 |
| stroke 21 | 19 % → 28 % | 321.2 px | 0.34 | 1.50 | 577 |
| stroke 22 | 6 % → 44 % | 102.9 px | 0.33 | 7.35 | 732 |
| stroke 23 | 17 % → 27 % | 291.3 px | 0.34 | 1.58 | 731 |
| stroke 24 | 12 % → 32 % | 100.4 px | 0.33 | 2.63 | 2299 |
| stroke 25 | 16 % → 24 % | 285.6 px | 0.34 | 1.45 | 625 |
| stroke 26 | 25 % → 23 % | 158.8 px | 0.33 | 0.94 | 3230 |
| stroke 27 | 26 % → 15 % | 139.6 px | 0.33 | 0.59 | 3640 |
| stroke 28 | 34 % → 13 % | 173.6 px | 0.33 | 0.38 | 3238 |
| stroke 29 | 10 % → 40 % | 104.3 px | 0.32 | 3.94 | 1370 |
| stroke 30 | 18 % → 41 % | 125.7 px | 0.32 | 2.35 | 4445 |
| stroke 31 | 25 % → 44 % | 158.8 px | 0.32 | 1.78 | 4211 |
| stroke 32 | 31 % → 48 % | 195.5 px | 0.32 | 1.55 | 4557 |
| stroke 33 | 41 % → 67 % | 365.2 px | 0.32 | 1.64 | 2629 |
| stroke 34 | 36 % → 54 % | 235.5 px | 0.32 | 1.48 | 4430 |
| stroke 35 | 38 % → 57 % | 269.2 px | 0.32 | 1.50 | 4477 |
| stroke 36 | 36 % → 52 % | 249.0 px | 0.33 | 1.45 | 4826 |
| stroke 37 | 34 % → 41 % | 216.2 px | 0.33 | 1.22 | 5396 |
| stroke 38 | 38 % → 41 % | 301.8 px | 0.33 | 1.10 | 3596 |
| stroke 39 | 38 % → 37 % | 383.7 px | 0.33 | 0.97 | 2367 |

Numbers say: wet paint spreads well beyond the stroke.

## Refs v3 · #33 Red wet-in-wet flames — own sheet
own sheet 800 × 1083 · Watercolour 1.00 + water 60 % · 96 px · 211.0 s

![Refs v3 · #33 Red wet-in-wet flames — own sheet](Refs-v3-33-Red-wet-in-wet-flames-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 25 % → 53 % | 103.1 px | 0.34 | 2.10 | 7866 |
| stroke 2 | 28 % → 48 % | 139.9 px | 0.26 | 1.69 | 2481 |
| stroke 3 | 29 % → 48 % | 244.9 px | 0.25 | 1.63 | 2942 |
| stroke 4 | 36 % → 50 % | 247.5 px | 0.25 | 1.40 | 3171 |
| stroke 5 | 37 % → 48 % | 345.1 px | 0.25 | 1.32 | 1542 |
| stroke 6 | 36 % → 48 % | 308.7 px | 0.24 | 1.34 | 2764 |
| stroke 7 | 33 % → 45 % | 192.6 px | 0.23 | 1.38 | 3595 |
| stroke 8 | 39 % → 43 % | 196.2 px | 0.23 | 1.09 | 3316 |

Numbers say: wet paint spreads well beyond the stroke.

## Refs v3 · #34 Magenta oil patches — own sheet
own sheet 800 × 1420 · Gouache 1.00 + turpentine 20 % · 90 px · 1762.5 s

![Refs v3 · #34 Magenta oil patches — own sheet](Refs-v3-34-Magenta-oil-patches-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 15 % → 97 % | 84.2 px | 0.30 | 6.54 | 3386 |
| stroke 2 | 30 % → 95 % | 186.6 px | 0.25 | 3.18 | 1587 |
| stroke 3 | 21 % → 99 % | 230.9 px | 0.31 | 4.83 | 2752 |
| stroke 4 | 49 % → 96 % | 207.6 px | 0.34 | 1.96 | 3145 |
| stroke 5 | 55 % → 98 % | 298.8 px | 0.29 | 1.79 | 2383 |
| stroke 6 | 37 % → 99 % | 384.1 px | 0.31 | 2.71 | 2611 |
| stroke 7 | 44 % → 100 % | 719.0 px | 0.29 | 2.26 | 1372 |
| stroke 8 | 53 % → 97 % | 426.3 px | 0.33 | 1.81 | 2514 |
| stroke 9 | 62 % → 99 % | 626.9 px | 0.30 | 1.60 | 1988 |
| stroke 10 | 45 % → 96 % | 381.3 px | 0.25 | 2.15 | 2808 |
| stroke 11 | 75 % → 100 % | 941.3 px | 0.34 | 1.32 | 821 |
| stroke 12 | 58 % → 97 % | 385.2 px | 0.27 | 1.68 | 985 |
| stroke 13 | 74 % → 98 % | 570.9 px | 0.30 | 1.32 | 1729 |
| stroke 14 | 75 % → 99 % | 651.5 px | 0.31 | 1.32 | 2029 |
| stroke 15 | 62 % → 97 % | 795.3 px | 0.27 | 1.56 | 1165 |
| stroke 16 | 53 % → 94 % | 447.6 px | 0.25 | 1.78 | 1145 |
| stroke 17 | 61 % → 99 % | 739.1 px | 0.28 | 1.62 | 1781 |
| stroke 18 | 67 % → 100 % | 701.4 px | 0.34 | 1.48 | 2382 |
| stroke 19 | 7 % → 99 % | 91.1 px | 0.25 | 14.32 | 2173 |
| stroke 20 | 13 % → 99 % | 159.6 px | 0.28 | 7.76 | 2490 |
| stroke 21 | 18 % → 100 % | 372.0 px | 0.26 | 5.70 | 1260 |
| stroke 22 | 21 % → 99 % | 474.6 px | 0.30 | 4.74 | 1575 |
| stroke 23 | 6 % → 92 % | 100.4 px | 0.21 | 15.85 | 1268 |
| stroke 24 | 9 % → 86 % | 175.8 px | 0.20 | 9.46 | 1503 |
| stroke 25 | 12 % → 97 % | 111.5 px | 0.22 | 7.83 | 2964 |
| stroke 26 | 22 % → 99 % | 159.2 px | 0.21 | 4.51 | 3867 |
| stroke 27 | 31 % → 95 % | 213.7 px | 0.31 | 3.05 | 3873 |
| stroke 28 | 30 % → 95 % | 397.3 px | 0.28 | 3.17 | 1805 |
| stroke 29 | 41 % → 98 % | 621.8 px | 0.26 | 2.38 | 2163 |
| stroke 30 | 28 % → 94 % | 480.2 px | 0.29 | 3.32 | 1061 |
| stroke 31 | 47 % → 93 % | 635.5 px | 0.34 | 1.97 | 1289 |
| stroke 32 | 28 % → 100 % | 585.1 px | 0.19 | 3.51 | 909 |
| stroke 33 | 31 % → 94 % | 396.7 px | 0.30 | 2.98 | 1521 |
| stroke 34 | 37 % → 99 % | 657.0 px | 0.23 | 2.64 | 1549 |
| stroke 35 | 32 % → 95 % | 643.5 px | 0.29 | 2.95 | 1483 |
| stroke 36 | 41 % → 92 % | 539.3 px | 0.21 | 2.27 | 210 |
| stroke 37 | 63 % → 96 % | 293.6 px | 0.35 | 1.52 | 3008 |
| stroke 38 | 50 % → 93 % | 508.7 px | 0.23 | 1.87 | 1253 |
| stroke 39 | 20 % → 99 % | 211.5 px | 0.24 | 4.87 | 3141 |
| stroke 40 | 51 % → 95 % | 389.4 px | 0.31 | 1.84 | 5725 |
| stroke 41 | 57 % → 96 % | 516.4 px | 0.30 | 1.68 | 4709 |
| stroke 42 | 48 % → 94 % | 319.2 px | 0.31 | 1.95 | 6624 |
| stroke 43 | 73 % → 99 % | 1110.1 px | 0.33 | 1.36 | 2186 |
| stroke 44 | 43 % → 99 % | 491.5 px | 0.25 | 2.32 | 3684 |
| stroke 45 | 66 % → 94 % | 932.4 px | 0.32 | 1.42 | 3014 |
| stroke 46 | 26 % → 96 % | 331.1 px | 0.22 | 3.71 | 2290 |
| stroke 47 | 71 % → 93 % | 1059.6 px | 0.36 | 1.31 | 1375 |
| stroke 48 | 78 % → 99 % | 1122.7 px | 0.33 | 1.27 | 2339 |
| stroke 49 | 65 % → 94 % | 673.4 px | 0.33 | 1.45 | 3378 |
| stroke 50 | 76 % → 99 % | 1556.7 px | 0.33 | 1.30 | 1358 |
| stroke 51 | 83 % → 96 % | 750.2 px | 0.35 | 1.16 | 6235 |
| stroke 52 | 66 % → 99 % | 1122.6 px | 0.31 | 1.49 | 2958 |
| stroke 53 | 77 % → 99 % | 1123.7 px | 0.32 | 1.30 | 3176 |
| stroke 54 | 45 % → 95 % | 936.5 px | 0.28 | 2.09 | 3315 |
| stroke 55 | 48 % → 99 % | 422.6 px | 0.26 | 2.08 | 3777 |
| stroke 56 | 33 % → 70 % | 178.2 px | 0.25 | 2.13 | 4327 |
| stroke 57 | 65 % → 95 % | 334.4 px | 0.34 | 1.47 | 4321 |
| stroke 58 | 65 % → 94 % | 696.5 px | 0.34 | 1.45 | 1934 |
| stroke 59 | 79 % → 95 % | 386.0 px | 0.38 | 1.20 | 3042 |
| stroke 60 | 66 % → 94 % | 427.6 px | 0.30 | 1.41 | 2922 |
| stroke 61 | 77 % → 98 % | 1039.2 px | 0.32 | 1.26 | 1876 |
| stroke 62 | 88 % → 97 % | 943.6 px | 0.36 | 1.10 | 1542 |
| stroke 63 | 59 % → 96 % | 464.7 px | 0.23 | 1.63 | 3458 |
| stroke 64 | 70 % → 100 % | 1001.1 px | 0.26 | 1.41 | 2275 |
| stroke 65 | 69 % → 98 % | 1198.7 px | 0.24 | 1.42 | 1402 |
| stroke 66 | 74 % → 92 % | 649.8 px | 0.35 | 1.24 | 2333 |
| stroke 67 | 41 % → 98 % | 316.7 px | 0.17 | 2.40 | 4457 |
| stroke 68 | 30 % → 94 % | 326.9 px | 0.19 | 3.08 | 5606 |
| stroke 69 | 43 % → 98 % | 411.6 px | 0.20 | 2.28 | 8794 |
| stroke 70 | 54 % → 97 % | 354.6 px | 0.23 | 1.78 | 8092 |
| stroke 71 | 56 % → 96 % | 491.6 px | 0.24 | 1.72 | 3449 |
| stroke 72 | 46 % → 84 % | 416.8 px | 0.22 | 1.84 | 1712 |
| stroke 73 | 67 % → 94 % | 518.2 px | 0.24 | 1.41 | 3112 |
| stroke 74 | 48 % → 90 % | 735.9 px | 0.19 | 1.86 | 1933 |
| stroke 75 | 58 % → 99 % | 454.4 px | 0.20 | 1.71 | 2869 |
| stroke 76 | 59 % → 100 % | 935.3 px | 0.19 | 1.69 | 1558 |
| stroke 77 | 64 % → 87 % | 712.8 px | 0.22 | 1.35 | 1537 |
| stroke 78 | 68 % → 97 % | 1191.1 px | 0.21 | 1.43 | 2120 |
| stroke 79 | 54 % → 78 % | 402.0 px | 0.20 | 1.43 | 2772 |
| stroke 80 | 88 % → 96 % | 801.8 px | 0.27 | 1.09 | 2472 |
| stroke 81 | 69 % → 95 % | 1263.7 px | 0.19 | 1.38 | 2273 |
| stroke 82 | 82 % → 95 % | 899.6 px | 0.28 | 1.16 | 2253 |
| stroke 83 | 74 % → 95 % | 955.3 px | 0.22 | 1.29 | 3272 |
| stroke 84 | 78 % → 98 % | 977.4 px | 0.25 | 1.26 | 1518 |
| stroke 85 | 63 % → 98 % | 756.2 px | 0.21 | 1.56 | 1845 |
| stroke 86 | 89 % → 96 % | 866.4 px | 0.26 | 1.08 | 2911 |
| stroke 87 | 66 % → 81 % | 549.4 px | 0.21 | 1.22 | 3372 |
| stroke 88 | 60 % → 88 % | 733.5 px | 0.19 | 1.47 | 2769 |
| stroke 89 | 27 % → 63 % | 300.8 px | 0.19 | 2.31 | 1529 |
| stroke 90 | 72 % → 93 % | 939.3 px | 0.31 | 1.29 | 1411 |
| stroke 91 | 63 % → 91 % | 1021.9 px | 0.34 | 1.44 | 238 |
| stroke 92 | 43 % → 99 % | 380.4 px | 0.19 | 2.29 | 4707 |
| stroke 93 | 44 % → 99 % | 249.8 px | 0.14 | 2.23 | 6506 |
| stroke 94 | 47 % → 99 % | 325.6 px | 0.10 | 2.10 | 4328 |
| stroke 95 | 60 % → 100 % | 1032.4 px | 0.19 | 1.65 | 1971 |
| stroke 96 | 48 % → 99 % | 599.8 px | 0.07 | 2.05 | 2155 |
| stroke 97 | 56 % → 98 % | 455.7 px | 0.16 | 1.76 | 6669 |
| stroke 98 | 67 % → 100 % | 616.9 px | 0.20 | 1.48 | 5276 |
| stroke 99 | 60 % → 99 % | 471.8 px | 0.07 | 1.65 | 3184 |
| stroke 100 | 70 % → 97 % | 436.8 px | 0.13 | 1.40 | 5353 |
| stroke 101 | 68 % → 99 % | 1019.3 px | 0.07 | 1.44 | 2409 |
| stroke 102 | 82 % → 99 % | 1615.7 px | 0.23 | 1.21 | 1763 |
| stroke 103 | 55 % → 99 % | 705.8 px | 0.06 | 1.79 | 1142 |
| stroke 104 | 76 % → 99 % | 863.0 px | 0.24 | 1.30 | 3019 |
| stroke 105 | 79 % → 97 % | 660.7 px | 0.27 | 1.23 | 5542 |
| stroke 106 | 64 % → 93 % | 716.6 px | 0.23 | 1.46 | 2786 |
| stroke 107 | 80 % → 98 % | 1034.6 px | 0.22 | 1.23 | 3320 |
| stroke 108 | 80 % → 100 % | 1091.6 px | 0.22 | 1.25 | 6581 |
| stroke 109 | 75 % → 92 % | 1396.8 px | 0.35 | 1.23 | 226 |
| stroke 110 | 71 % → 99 % | 559.6 px | 0.15 | 1.40 | 5451 |
| stroke 111 | 84 % → 99 % | 648.3 px | 0.18 | 1.18 | 6606 |
| stroke 112 | 86 % → 100 % | 1132.1 px | 0.14 | 1.16 | 2878 |
| stroke 113 | 81 % → 99 % | 727.5 px | 0.15 | 1.21 | 1614 |
| stroke 114 | 91 % → 100 % | 1269.8 px | 0.15 | 1.10 | 2039 |
| stroke 115 | 97 % → 99 % | 722.3 px | 0.13 | 1.03 | 2360 |
| stroke 116 | 96 % → 99 % | 1113.8 px | 0.10 | 1.03 | 958 |
| stroke 117 | 97 % → 99 % | 1112.0 px | 0.07 | 1.02 | 1670 |
| stroke 118 | 97 % → 99 % | 1805.7 px | 0.21 | 1.02 | 2338 |
| stroke 119 | 97 % → 99 % | 1598.4 px | 0.16 | 1.02 | 1734 |
| stroke 120 | 99 % → 99 % | 1925.6 px | 0.23 | 1.00 | 1760 |
| stroke 121 | 100 % → 100 % | 1137.2 px | 0.13 | 1.00 | 4049 |
| stroke 122 | 100 % → 99 % | 1548.6 px | 0.20 | 1.00 | 2000 |
| stroke 123 | 99 % → 99 % | 1139.0 px | 0.13 | 1.00 | 1284 |
| stroke 124 | 98 % → 99 % | 899.3 px | 0.16 | 1.01 | 2844 |
| stroke 125 | 99 % → 99 % | 1714.9 px | 0.08 | 1.00 | 3838 |
| stroke 126 | 99 % → 100 % | 1802.7 px | 0.19 | 1.01 | 2412 |
| stroke 127 | 99 % → 99 % | 1264.9 px | 0.07 | 1.00 | 2045 |
| stroke 128 | 91 % → 96 % | 2011.6 px | 0.34 | 1.05 | 84 |
| stroke 129 | 66 % → 94 % | 210.6 px | 0.15 | 1.42 | 1007 |
| stroke 130 | 94 % → 94 % | 421.7 px | 0.40 | 0.99 | 463 |
| stroke 131 | 80 % → 93 % | 486.9 px | 0.31 | 1.15 | 6135 |
| stroke 132 | 84 % → 91 % | 418.4 px | 0.33 | 1.08 | 4084 |
| stroke 133 | 86 % → 91 % | 588.9 px | 0.30 | 1.06 | 3771 |
| stroke 134 | 90 % → 92 % | 839.8 px | 0.33 | 1.02 | 2472 |
| stroke 135 | 88 % → 90 % | 1181.4 px | 0.29 | 1.02 | 1103 |
| stroke 136 | 90 % → 89 % | 1188.4 px | 0.31 | 0.98 | 1014 |
| stroke 137 | 79 % → 97 % | 546.4 px | 0.17 | 1.23 | 4854 |
| stroke 138 | 91 % → 98 % | 821.6 px | 0.21 | 1.07 | 5490 |
| stroke 139 | 91 % → 98 % | 1044.0 px | 0.23 | 1.07 | 3698 |
| stroke 140 | 92 % → 97 % | 703.8 px | 0.17 | 1.05 | 4461 |
| stroke 141 | 95 % → 96 % | 669.0 px | 0.19 | 1.01 | 5704 |
| stroke 142 | 98 % → 99 % | 1894.6 px | 0.21 | 1.01 | 1657 |
| stroke 143 | 97 % → 97 % | 1014.6 px | 0.19 | 1.00 | 11698 |
| stroke 144 | 96 % → 97 % | 806.4 px | 0.08 | 1.01 | 4318 |
| stroke 145 | 100 % → 100 % | 2016.1 px | 0.25 | 1.00 | 1619 |
| stroke 146 | 96 % → 96 % | 1142.0 px | 0.11 | 1.00 | 2013 |
| stroke 147 | 95 % → 95 % | 1375.2 px | 0.21 | 0.99 | 1142 |
| stroke 148 | 77 % → 98 % | 1173.9 px | 0.21 | 1.27 | 1702 |
| stroke 149 | 56 % → 72 % | 602.8 px | 0.19 | 1.28 | 2669 |
| stroke 150 | 61 % → 73 % | 513.1 px | 0.20 | 1.20 | 2983 |
| stroke 151 | 80 % → 84 % | 844.3 px | 0.19 | 1.05 | 5919 |
| stroke 152 | 76 % → 76 % | 836.0 px | 0.18 | 1.01 | 2641 |
| stroke 153 | 87 % → 88 % | 900.2 px | 0.19 | 1.01 | 5822 |
| stroke 154 | 93 % → 93 % | 1610.7 px | 0.18 | 1.00 | 1159 |
| stroke 155 | 83 % → 83 % | 1506.7 px | 0.17 | 1.00 | 1252 |
| stroke 156 | 69 % → 68 % | 1426.7 px | 0.14 | 0.99 | 1479 |
| stroke 157 | 77 % → 76 % | 1232.7 px | 0.18 | 0.99 | 2835 |

Numbers say: wet paint spreads well beyond the stroke.

## Refs v3 · #35 Red band with runs — own sheet
own sheet 800 × 1191 · Watercolour 1.00 + water 70 % · 176 px · 311.5 s

![Refs v3 · #35 Red band with runs — own sheet](Refs-v3-35-Red-band-with-runs-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 40 % → 51 % | 296.2 px | 0.38 | 1.27 | 25335 |
| stroke 2 | 50 % → 52 % | 369.0 px | 0.38 | 1.03 | 43083 |
| stroke 3 | 49 % → 52 % | 361.1 px | 0.38 | 1.05 | 44849 |

## Refs v3 · #36 Magenta letters flat — own sheet
own sheet 800 × 1000 · Gouache 1.00 + water 15 % · 64 px · 246.6 s

![Refs v3 · #36 Magenta letters flat — own sheet](Refs-v3-36-Magenta-letters-flat-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 4 % → 36 % | 82.0 px | 0.40 | 9.72 | 383 |
| stroke 2 | 7 % → 34 % | 218.7 px | 0.40 | 5.12 | 124 |
| stroke 3 | 7 % → 25 % | 103.9 px | 0.41 | 3.50 | 142 |
| stroke 4 | 13 % → 30 % | 157.4 px | 0.41 | 2.36 | 268 |
| stroke 5 | 21 % → 33 % | 127.5 px | 0.41 | 1.60 | 881 |
| stroke 6 | 9 % → 30 % | 63.7 px | 0.39 | 3.27 | 564 |
| stroke 7 | 26 % → 38 % | 184.2 px | 0.40 | 1.47 | 796 |
| stroke 8 | 5 % → 41 % | 76.1 px | 0.40 | 7.73 | 557 |
| stroke 9 | 9 % → 41 % | 140.1 px | 0.40 | 4.53 | 343 |
| stroke 10 | 14 % → 32 % | 173.3 px | 0.40 | 2.29 | 530 |
| stroke 11 | 19 % → 35 % | 223.0 px | 0.40 | 1.92 | 488 |
| stroke 12 | 22 % → 36 % | 323.3 px | 0.40 | 1.65 | 360 |
| stroke 13 | 38 % → 41 % | 197.6 px | 0.40 | 1.07 | 1181 |
| stroke 14 | 25 % → 31 % | 73.8 px | 0.42 | 1.24 | 3126 |
| stroke 15 | 12 % → 39 % | 246.2 px | 0.41 | 3.41 | 182 |
| stroke 16 | 18 % → 41 % | 136.7 px | 0.41 | 2.22 | 790 |
| stroke 17 | 29 % → 41 % | 283.0 px | 0.40 | 1.42 | 849 |
| stroke 18 | 29 % → 42 % | 452.8 px | 0.40 | 1.46 | 457 |
| stroke 19 | 30 % → 42 % | 308.0 px | 0.41 | 1.39 | 556 |
| stroke 20 | 15 % → 38 % | 554.2 px | 0.41 | 2.58 | 75 |
| stroke 21 | 26 % → 42 % | 119.5 px | 0.41 | 1.64 | 1608 |
| stroke 22 | 22 % → 43 % | 172.9 px | 0.41 | 1.92 | 731 |
| stroke 23 | 17 % → 46 % | 194.4 px | 0.40 | 2.76 | 517 |
| stroke 24 | 11 % → 48 % | 105.5 px | 0.40 | 4.49 | 629 |
| stroke 25 | 26 % → 35 % | 321.4 px | 0.40 | 1.35 | 413 |
| stroke 26 | 36 % → 39 % | 440.7 px | 0.40 | 1.09 | 413 |
| stroke 27 | 35 % → 38 % | 436.0 px | 0.40 | 1.08 | 329 |
| stroke 28 | 6 % → 50 % | 63.7 px | 0.41 | 8.13 | 271 |
| stroke 29 | 31 % → 39 % | 155.0 px | 0.41 | 1.28 | 1349 |
| stroke 30 | 40 % → 44 % | 254.9 px | 0.41 | 1.11 | 808 |
| stroke 31 | 30 % → 41 % | 91.5 px | 0.40 | 1.34 | 2283 |
| stroke 32 | 30 % → 43 % | 112.0 px | 0.40 | 1.41 | 1737 |
| stroke 33 | 21 % → 43 % | 337.5 px | 0.40 | 2.09 | 543 |
| stroke 34 | 12 % → 45 % | 151.3 px | 0.41 | 3.59 | 471 |
| stroke 35 | 35 % → 41 % | 241.1 px | 0.41 | 1.17 | 1962 |
| stroke 36 | 33 % → 38 % | 373.0 px | 0.40 | 1.16 | 588 |
| stroke 37 | 13 % → 34 % | 104.7 px | 0.41 | 2.71 | 613 |
| stroke 38 | 28 % → 42 % | 315.2 px | 0.41 | 1.51 | 716 |
| stroke 39 | 25 % → 35 % | 214.2 px | 0.41 | 1.39 | 508 |
| stroke 40 | 10 % → 26 % | 189.8 px | 0.41 | 2.52 | 193 |
| stroke 41 | 23 % → 34 % | 296.2 px | 0.41 | 1.49 | 217 |
| stroke 42 | 33 % → 34 % | 248.3 px | 0.41 | 1.03 | 923 |
| stroke 43 | 30 % → 30 % | 691.0 px | 0.41 | 0.98 | 129 |
| stroke 44 | 40 % → 39 % | 318.0 px | 0.40 | 0.98 | 454 |

Numbers say: wet paint spreads well beyond the stroke.

## Refs v3 · #37 Oil still life — own sheet
own sheet 800 × 810 · Gouache 1.00 + turpentine 20 % · 28 px · 736.6 s

![Refs v3 · #37 Oil still life — own sheet](Refs-v3-37-Oil-still-life-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 7 % → 87 % | 30.9 px | 0.21 | 11.71 | 357 |
| stroke 2 | 16 % → 95 % | 62.6 px | 0.29 | 5.93 | 269 |
| stroke 3 | 17 % → 98 % | 123.4 px | 0.31 | 5.86 | 38 |
| stroke 4 | 23 % → 98 % | 62.0 px | 0.35 | 4.23 | 439 |
| stroke 5 | 31 % → 97 % | 113.6 px | 0.32 | 3.14 | 224 |
| stroke 6 | 31 % → 87 % | 188.7 px | 0.20 | 2.78 | 85 |
| stroke 7 | 34 % → 98 % | 252.1 px | 0.32 | 2.86 | 126 |
| stroke 8 | 27 % → 97 % | 142.0 px | 0.21 | 3.54 | 284 |
| stroke 9 | 30 % → 97 % | 148.9 px | 0.25 | 3.26 | 160 |
| stroke 10 | 27 % → 95 % | 91.0 px | 0.17 | 3.54 | 159 |
| stroke 11 | 55 % → 91 % | 262.3 px | 0.28 | 1.65 | 188 |
| stroke 12 | 49 % → 99 % | 314.0 px | 0.34 | 2.02 | 94 |
| stroke 13 | 10 % → 84 % | 80.8 px | 0.24 | 8.08 | 65 |
| stroke 14 | 63 % → 98 % | 250.0 px | 0.35 | 1.56 | 161 |
| stroke 15 | 33 % → 74 % | 263.3 px | 0.20 | 2.20 | 51 |
| stroke 16 | 23 % → 86 % | 91.6 px | 0.30 | 3.73 | 182 |
| stroke 17 | 59 % → 96 % | 435.8 px | 0.26 | 1.61 | 57 |
| stroke 18 | 66 % → 94 % | 506.8 px | 0.32 | 1.42 | 68 |
| stroke 19 | 36 % → 76 % | 186.9 px | 0.19 | 2.13 | 142 |
| stroke 20 | 43 % → 96 % | 297.0 px | 0.20 | 2.22 | 60 |
| stroke 21 | 17 % → 92 % | 56.9 px | 0.26 | 5.41 | 229 |
| stroke 22 | 17 % → 96 % | 53.8 px | 0.29 | 5.78 | 177 |
| stroke 23 | 30 % → 95 % | 84.1 px | 0.30 | 3.13 | 312 |
| stroke 24 | 21 % → 95 % | 97.7 px | 0.24 | 4.56 | 263 |
| stroke 25 | 31 % → 86 % | 126.1 px | 0.29 | 2.75 | 144 |
| stroke 26 | 6 % → 74 % | 32.9 px | 0.16 | 12.80 | 61 |
| stroke 27 | 11 % → 67 % | 71.7 px | 0.16 | 5.87 | 74 |
| stroke 28 | 16 % → 81 % | 104.8 px | 0.19 | 4.92 | 56 |
| stroke 29 | 15 % → 71 % | 57.7 px | 0.16 | 4.71 | 171 |
| stroke 30 | 13 % → 83 % | 71.4 px | 0.24 | 6.35 | 46 |
| stroke 31 | 63 % → 97 % | 244.8 px | 0.31 | 1.53 | 288 |
| stroke 32 | 70 % → 89 % | 162.6 px | 0.36 | 1.27 | 964 |
| stroke 33 | 68 % → 90 % | 157.8 px | 0.34 | 1.32 | 798 |
| stroke 34 | 79 % → 96 % | 206.3 px | 0.37 | 1.22 | 611 |
| stroke 35 | 10 % → 87 % | 55.1 px | 0.29 | 8.41 | 137 |
| stroke 36 | 19 % → 92 % | 78.1 px | 0.34 | 4.85 | 268 |
| stroke 37 | 26 % → 96 % | 115.4 px | 0.34 | 3.71 | 265 |
| stroke 38 | 34 % → 89 % | 193.1 px | 0.37 | 2.59 | 186 |
| stroke 39 | 22 % → 96 % | 90.3 px | 0.31 | 4.31 | 490 |
| stroke 40 | 28 % → 90 % | 136.0 px | 0.27 | 3.23 | 204 |
| stroke 41 | 31 % → 90 % | 113.2 px | 0.28 | 2.90 | 445 |
| stroke 42 | 13 % → 76 % | 51.9 px | 0.23 | 6.02 | 212 |
| stroke 43 | 18 % → 74 % | 87.0 px | 0.23 | 4.01 | 243 |
| stroke 44 | 24 % → 84 % | 105.1 px | 0.20 | 3.51 | 298 |
| stroke 45 | 18 % → 83 % | 54.4 px | 0.22 | 4.56 | 472 |
| stroke 46 | 28 % → 82 % | 155.1 px | 0.25 | 2.93 | 170 |
| stroke 47 | 37 % → 96 % | 189.8 px | 0.29 | 2.55 | 150 |
| stroke 48 | 32 % → 85 % | 155.3 px | 0.23 | 2.66 | 149 |
| stroke 49 | 43 % → 98 % | 149.0 px | 0.41 | 2.25 | 331 |
| stroke 50 | 22 % → 87 % | 54.3 px | 0.24 | 3.96 | 468 |
| stroke 51 | 34 % → 94 % | 94.9 px | 0.24 | 2.77 | 551 |
| stroke 52 | 34 % → 96 % | 207.4 px | 0.27 | 2.83 | 176 |
| stroke 53 | 66 % → 98 % | 301.3 px | 0.43 | 1.49 | 228 |
| stroke 54 | 67 % → 98 % | 261.2 px | 0.39 | 1.47 | 350 |
| stroke 55 | 58 % → 96 % | 192.9 px | 0.32 | 1.65 | 771 |
| stroke 56 | 45 % → 89 % | 154.6 px | 0.25 | 1.96 | 446 |
| stroke 57 | 49 % → 95 % | 301.5 px | 0.26 | 1.95 | 194 |
| stroke 58 | 64 % → 93 % | 165.4 px | 0.29 | 1.46 | 1194 |
| stroke 59 | 68 % → 96 % | 296.7 px | 0.32 | 1.41 | 422 |
| stroke 60 | 54 % → 93 % | 282.8 px | 0.27 | 1.73 | 146 |
| stroke 61 | 65 % → 86 % | 345.6 px | 0.30 | 1.34 | 167 |
| stroke 62 | 92 % → 98 % | 562.3 px | 0.44 | 1.06 | 139 |
| stroke 63 | 45 % → 96 % | 247.7 px | 0.21 | 2.12 | 138 |
| stroke 64 | 92 % → 97 % | 493.8 px | 0.42 | 1.05 | 170 |
| stroke 65 | 67 % → 97 % | 352.0 px | 0.31 | 1.44 | 176 |
| stroke 66 | 49 % → 80 % | 290.8 px | 0.24 | 1.65 | 117 |
| stroke 67 | 65 % → 87 % | 359.2 px | 0.29 | 1.33 | 133 |
| stroke 68 | 15 % → 73 % | 100.3 px | 0.11 | 4.75 | 51 |
| stroke 69 | 10 % → 86 % | 40.1 px | 0.21 | 8.37 | 162 |
| stroke 70 | 14 % → 84 % | 54.8 px | 0.22 | 6.18 | 137 |
| stroke 71 | 22 % → 88 % | 91.6 px | 0.23 | 3.96 | 120 |
| stroke 72 | 21 % → 89 % | 140.7 px | 0.21 | 4.26 | 81 |
| stroke 73 | 36 % → 92 % | 47.8 px | 0.07 | 2.54 | 883 |
| stroke 74 | 48 % → 97 % | 107.1 px | 0.08 | 2.03 | 590 |
| stroke 75 | 46 % → 84 % | 66.8 px | 0.07 | 1.80 | 1129 |
| stroke 76 | 59 % → 87 % | 180.1 px | 0.09 | 1.47 | 495 |
| stroke 77 | 90 % → 96 % | 122.2 px | 0.07 | 1.06 | 787 |
| stroke 78 | 35 % → 67 % | 64.4 px | 0.05 | 1.93 | 573 |
| stroke 79 | 57 % → 66 % | 78.0 px | 0.05 | 1.14 | 673 |
| stroke 80 | 72 % → 96 % | 241.5 px | 0.12 | 1.34 | 417 |
| stroke 81 | 81 % → 90 % | 304.6 px | 0.07 | 1.12 | 266 |
| stroke 82 | 77 % → 88 % | 143.2 px | 0.10 | 1.15 | 293 |
| stroke 83 | 40 % → 42 % | 204.5 px | 0.04 | 1.04 | 158 |
| stroke 84 | 84 % → 96 % | 238.8 px | 0.07 | 1.14 | 317 |
| stroke 85 | 72 % → 80 % | 215.0 px | 0.09 | 1.11 | 192 |
| stroke 86 | 88 % → 99 % | 336.1 px | 0.09 | 1.12 | 303 |
| stroke 87 | 69 % → 81 % | 117.7 px | 0.06 | 1.17 | 499 |
| stroke 88 | 68 % → 76 % | 310.7 px | 0.08 | 1.10 | 176 |
| stroke 89 | 63 % → 89 % | 117.4 px | 0.06 | 1.42 | 692 |
| stroke 90 | 70 % → 65 % | 172.3 px | 0.05 | 0.94 | 209 |
| stroke 91 | 94 % → 96 % | 187.6 px | 0.06 | 1.02 | 305 |
| stroke 92 | 84 % → 79 % | 128.5 px | 0.05 | 0.95 | 327 |
| stroke 93 | 71 % → 96 % | 301.3 px | 0.15 | 1.35 | 307 |
| stroke 94 | 88 % → 95 % | 217.5 px | 0.08 | 1.09 | 215 |
| stroke 95 | 63 % → 61 % | 223.1 px | 0.09 | 0.97 | 234 |
| stroke 96 | 69 % → 86 % | 298.0 px | 0.11 | 1.25 | 353 |
| stroke 97 | 76 % → 97 % | 364.6 px | 0.10 | 1.28 | 210 |
| stroke 98 | 15 % → 43 % | 57.7 px | 0.02 | 3.00 | 289 |
| stroke 99 | 31 % → 64 % | 96.2 px | 0.07 | 2.10 | 468 |
| stroke 100 | 43 % → 69 % | 132.5 px | 0.06 | 1.60 | 507 |
| stroke 101 | 36 % → 62 % | 154.9 px | 0.14 | 1.73 | 150 |
| stroke 102 | 69 % → 83 % | 237.6 px | 0.16 | 1.20 | 338 |
| stroke 103 | 72 % → 80 % | 202.6 px | 0.18 | 1.10 | 353 |
| stroke 104 | 73 % → 77 % | 264.1 px | 0.09 | 1.05 | 263 |
| stroke 105 | 48 % → 60 % | 149.2 px | 0.04 | 1.24 | 362 |
| stroke 106 | 69 % → 71 % | 283.2 px | 0.04 | 1.03 | 182 |
| stroke 107 | 64 % → 62 % | 307.0 px | 0.02 | 0.97 | 134 |
| stroke 108 | 43 % → 79 % | 116.2 px | 0.15 | 1.81 | 384 |
| stroke 109 | 31 % → 96 % | 142.2 px | 0.11 | 3.13 | 424 |
| stroke 110 | 31 % → 44 % | 137.3 px | 0.28 | 1.44 | 798 |
| stroke 111 | 27 % → 77 % | 72.2 px | 0.04 | 2.87 | 732 |
| stroke 112 | 51 % → 77 % | 187.1 px | 0.11 | 1.50 | 385 |
| stroke 113 | 43 % → 89 % | 119.4 px | 0.09 | 2.09 | 1109 |
| stroke 114 | 41 % → 64 % | 100.1 px | 0.20 | 1.53 | 429 |
| stroke 115 | 84 % → 97 % | 293.0 px | 0.27 | 1.15 | 735 |
| stroke 116 | 33 % → 59 % | 88.5 px | 0.16 | 1.77 | 1345 |
| stroke 117 | 55 % → 78 % | 171.8 px | 0.22 | 1.44 | 1168 |
| stroke 118 | 47 % → 67 % | 147.4 px | 0.17 | 1.40 | 421 |
| stroke 119 | 68 % → 78 % | 153.8 px | 0.16 | 1.15 | 312 |
| stroke 120 | 60 % → 66 % | 126.6 px | 0.17 | 1.09 | 1403 |
| stroke 121 | 77 % → 90 % | 162.7 px | 0.20 | 1.17 | 593 |
| stroke 122 | 49 % → 86 % | 191.4 px | 0.13 | 1.75 | 582 |
| stroke 123 | 66 % → 69 % | 254.9 px | 0.21 | 1.04 | 276 |
| stroke 124 | 34 % → 72 % | 81.9 px | 0.03 | 2.11 | 532 |
| stroke 125 | 69 % → 77 % | 285.5 px | 0.30 | 1.11 | 294 |
| stroke 126 | 67 % → 81 % | 190.5 px | 0.15 | 1.21 | 674 |
| stroke 127 | 75 % → 87 % | 259.0 px | 0.22 | 1.16 | 148 |
| stroke 128 | 59 % → 67 % | 182.1 px | 0.12 | 1.15 | 308 |
| stroke 129 | 80 % → 80 % | 227.5 px | 0.11 | 1.01 | 316 |
| stroke 130 | 88 % → 94 % | 223.3 px | 0.21 | 1.07 | 387 |
| stroke 131 | 40 % → 50 % | 163.7 px | 0.12 | 1.25 | 232 |
| stroke 132 | 63 % → 87 % | 204.0 px | 0.04 | 1.38 | 335 |
| stroke 133 | 79 % → 85 % | 207.7 px | 0.21 | 1.08 | 372 |
| stroke 134 | 82 % → 85 % | 331.5 px | 0.25 | 1.03 | 283 |
| stroke 135 | 72 % → 70 % | 215.3 px | 0.09 | 0.98 | 154 |
| stroke 136 | 77 % → 87 % | 260.3 px | 0.16 | 1.13 | 486 |
| stroke 137 | 71 % → 82 % | 248.6 px | 0.18 | 1.15 | 604 |
| stroke 138 | 69 % → 71 % | 307.0 px | 0.14 | 1.02 | 143 |
| stroke 139 | 83 % → 83 % | 229.1 px | 0.19 | 1.00 | 634 |
| stroke 140 | 34 % → 33 % | 142.3 px | 0.20 | 0.97 | 163 |
| stroke 141 | 79 % → 78 % | 259.4 px | 0.17 | 0.98 | 406 |
| stroke 142 | 92 % → 94 % | 256.9 px | 0.14 | 1.02 | 204 |
| stroke 143 | 96 % → 95 % | 452.1 px | 0.20 | 0.99 | 243 |
| stroke 144 | 63 % → 67 % | 205.6 px | 0.19 | 1.07 | 377 |
| stroke 145 | 78 % → 75 % | 227.2 px | 0.26 | 0.95 | 344 |
| stroke 146 | 43 % → 49 % | 222.9 px | 0.07 | 1.16 | 159 |
| stroke 147 | 68 % → 83 % | 325.0 px | 0.07 | 1.22 | 222 |
| stroke 148 | 79 % → 85 % | 381.7 px | 0.18 | 1.08 | 259 |
| stroke 149 | 85 % → 83 % | 377.5 px | 0.18 | 0.98 | 183 |
| stroke 150 | 94 % → 93 % | 487.9 px | 0.10 | 0.99 | 184 |
| stroke 151 | 37 % → 74 % | 94.9 px | 0.20 | 1.97 | 1005 |
| stroke 152 | 40 % → 80 % | 191.1 px | 0.11 | 2.00 | 176 |
| stroke 153 | 41 % → 66 % | 187.6 px | 0.10 | 1.59 | 379 |
| stroke 154 | 28 % → 56 % | 120.6 px | 0.11 | 1.98 | 981 |
| stroke 155 | 47 % → 63 % | 108.8 px | 0.22 | 1.33 | 4141 |
| stroke 156 | 62 % → 75 % | 219.4 px | 0.22 | 1.21 | 447 |
| stroke 157 | 61 % → 66 % | 172.8 px | 0.22 | 1.08 | 1095 |
| stroke 158 | 64 % → 63 % | 172.5 px | 0.16 | 0.98 | 507 |
| stroke 159 | 49 % → 50 % | 196.9 px | 0.16 | 1.01 | 236 |
| stroke 160 | 38 % → 40 % | 132.6 px | 0.07 | 1.07 | 214 |
| stroke 161 | 32 % → 83 % | 129.6 px | 0.11 | 2.58 | 397 |
| stroke 162 | 68 % → 94 % | 241.0 px | 0.11 | 1.39 | 417 |
| stroke 163 | 22 % → 57 % | 95.4 px | 0.03 | 2.59 | 263 |
| stroke 164 | 63 % → 80 % | 197.3 px | 0.07 | 1.26 | 1319 |
| stroke 165 | 60 % → 64 % | 337.6 px | 0.09 | 1.06 | 180 |
| stroke 166 | 88 % → 96 % | 406.0 px | 0.12 | 1.09 | 253 |
| stroke 167 | 77 % → 86 % | 239.4 px | 0.05 | 1.11 | 354 |
| stroke 168 | 87 % → 89 % | 399.0 px | 0.05 | 1.03 | 150 |
| stroke 169 | 77 % → 79 % | 388.5 px | 0.10 | 1.02 | 145 |
| stroke 170 | 63 % → 70 % | 323.5 px | 0.03 | 1.11 | 171 |
| stroke 171 | 29 % → 33 % | 142.9 px | 0.02 | 1.13 | 134 |
| stroke 172 | 42 % → 39 % | 221.8 px | 0.02 | 0.94 | 105 |
| stroke 173 | 57 % → 59 % | 267.0 px | 0.08 | 1.04 | 177 |
| stroke 174 | 51 % → 80 % | 144.4 px | 0.08 | 1.56 | 340 |
| stroke 175 | 58 % → 86 % | 151.7 px | 0.08 | 1.49 | 448 |
| stroke 176 | 44 % → 95 % | 199.8 px | 0.02 | 2.13 | 195 |
| stroke 177 | 59 % → 88 % | 306.4 px | 0.11 | 1.51 | 126 |
| stroke 178 | 52 % → 87 % | 215.3 px | 0.02 | 1.68 | 193 |
| stroke 179 | 61 % → 83 % | 199.4 px | 0.12 | 1.37 | 226 |
| stroke 180 | 70 % → 82 % | 211.9 px | 0.10 | 1.18 | 493 |
| stroke 181 | 67 % → 94 % | 250.2 px | 0.02 | 1.40 | 218 |
| stroke 182 | 46 % → 77 % | 217.4 px | 0.02 | 1.69 | 121 |
| stroke 183 | 61 % → 93 % | 259.4 px | 0.02 | 1.53 | 167 |
| stroke 184 | 72 % → 92 % | 408.5 px | 0.02 | 1.28 | 102 |
| stroke 185 | 69 % → 84 % | 288.9 px | 0.02 | 1.22 | 189 |
| stroke 186 | 55 % → 75 % | 262.8 px | 0.06 | 1.35 | 191 |
| stroke 187 | 82 % → 88 % | 455.0 px | 0.02 | 1.08 | 134 |
| stroke 188 | 80 % → 85 % | 370.0 px | 0.03 | 1.06 | 181 |
| stroke 189 | 84 % → 94 % | 393.3 px | 0.02 | 1.12 | 160 |
| stroke 190 | 91 % → 91 % | 422.2 px | 0.12 | 1.00 | 145 |
| stroke 191 | 93 % → 92 % | 471.2 px | 0.05 | 0.99 | 146 |
| stroke 192 | 79 % → 81 % | 427.6 px | 0.10 | 1.02 | 138 |
| stroke 193 | 68 % → 75 % | 355.8 px | 0.02 | 1.10 | 273 |
| stroke 194 | 76 % → 76 % | 376.8 px | 0.02 | 1.00 | 208 |
| stroke 195 | 87 % → 92 % | 261.4 px | 0.21 | 1.06 | 228 |
| stroke 196 | 84 % → 91 % | 229.8 px | 0.25 | 1.09 | 307 |
| stroke 197 | 86 % → 97 % | 762.2 px | 0.23 | 1.12 | 52 |
| stroke 198 | 92 % → 96 % | 449.2 px | 0.15 | 1.04 | 109 |
| stroke 199 | 90 % → 96 % | 275.9 px | 0.23 | 1.07 | 291 |
| stroke 200 | 88 % → 91 % | 590.4 px | 0.18 | 1.04 | 75 |
| stroke 201 | 80 % → 82 % | 729.4 px | 0.21 | 1.03 | 47 |
| stroke 202 | 80 % → 83 % | 318.9 px | 0.19 | 1.04 | 237 |
| stroke 203 | 94 % → 96 % | 587.9 px | 0.13 | 1.02 | 63 |
| stroke 204 | 87 % → 88 % | 317.1 px | 0.25 | 1.02 | 180 |
| stroke 205 | 74 % → 74 % | 497.2 px | 0.15 | 1.01 | 97 |
| stroke 206 | 86 % → 86 % | 433.6 px | 0.20 | 1.01 | 147 |
| stroke 207 | 85 % → 86 % | 308.2 px | 0.22 | 1.01 | 121 |
| stroke 208 | 94 % → 95 % | 627.0 px | 0.18 | 1.01 | 100 |
| stroke 209 | 91 % → 93 % | 841.6 px | 0.15 | 1.01 | 54 |
| stroke 210 | 80 % → 79 % | 382.9 px | 0.21 | 0.98 | 113 |
| stroke 211 | 80 % → 79 % | 621.6 px | 0.19 | 0.99 | 65 |
| stroke 212 | 97 % → 97 % | 847.0 px | 0.25 | 1.00 | 50 |
| stroke 213 | 85 % → 85 % | 582.0 px | 0.24 | 0.99 | 90 |
| stroke 214 | 90 % → 90 % | 662.5 px | 0.16 | 1.00 | 49 |
| stroke 215 | 95 % → 97 % | 600.4 px | 0.16 | 1.02 | 62 |
| stroke 216 | 95 % → 97 % | 692.6 px | 0.19 | 1.02 | 68 |
| stroke 217 | 83 % → 87 % | 345.8 px | 0.23 | 1.05 | 167 |
| stroke 218 | 84 % → 90 % | 526.4 px | 0.25 | 1.07 | 76 |
| stroke 219 | 92 % → 93 % | 385.8 px | 0.25 | 1.01 | 177 |
| stroke 220 | 93 % → 94 % | 726.7 px | 0.22 | 1.01 | 77 |
| stroke 221 | 90 % → 90 % | 397.2 px | 0.27 | 1.00 | 156 |
| stroke 222 | 84 % → 84 % | 771.4 px | 0.14 | 1.00 | 36 |
| stroke 223 | 87 % → 87 % | 650.4 px | 0.18 | 1.00 | 61 |
| stroke 224 | 83 % → 83 % | 760.3 px | 0.19 | 1.00 | 53 |
| stroke 225 | 87 % → 87 % | 682.2 px | 0.16 | 1.00 | 58 |
| stroke 226 | 91 % → 90 % | 842.9 px | 0.19 | 0.99 | 45 |
| stroke 227 | 86 % → 85 % | 787.8 px | 0.26 | 1.00 | 46 |
| stroke 228 | 83 % → 85 % | 330.3 px | 0.38 | 1.02 | 196 |
| stroke 229 | 90 % → 93 % | 606.4 px | 0.40 | 1.03 | 74 |
| stroke 230 | 96 % → 97 % | 536.9 px | 0.33 | 1.02 | 109 |
| stroke 231 | 95 % → 95 % | 431.1 px | 0.35 | 1.00 | 135 |
| stroke 232 | 90 % → 90 % | 572.7 px | 0.35 | 1.00 | 81 |
| stroke 233 | 98 % → 98 % | 681.2 px | 0.30 | 1.00 | 76 |
| stroke 234 | 75 % → 78 % | 421.3 px | 0.02 | 1.04 | 51 |
| stroke 235 | 91 % → 92 % | 469.9 px | 0.02 | 1.01 | 82 |
| stroke 236 | 85 % → 86 % | 769.5 px | 0.02 | 1.01 | 22 |
| stroke 237 | 92 % → 92 % | 511.4 px | 0.02 | 1.00 | 47 |
| stroke 238 | 81 % → 80 % | 498.2 px | 0.02 | 0.99 | 72 |
| stroke 239 | 88 % → 87 % | 406.7 px | 0.02 | 0.99 | 73 |
| stroke 240 | 64 % → 68 % | 493.5 px | 0.15 | 1.07 | 47 |
| stroke 241 | 71 % → 74 % | 619.7 px | 0.15 | 1.05 | 48 |
| stroke 242 | 59 % → 62 % | 441.4 px | 0.15 | 1.05 | 70 |
| stroke 243 | 69 % → 70 % | 305.0 px | 0.12 | 1.01 | 135 |
| stroke 244 | 55 % → 54 % | 385.3 px | 0.02 | 0.98 | 32 |
| stroke 245 | 56 % → 56 % | 187.3 px | 0.13 | 0.99 | 226 |
| stroke 246 | 69 % → 68 % | 208.1 px | 0.18 | 0.99 | 178 |

Numbers say: wet paint spreads well beyond the stroke.

## Refs v3 · #38 Sanguine drawing — own sheet
own sheet 800 × 1092 · Charcoal 0.50 · Pastel 0.50 · 12 px · 555.7 s

![Refs v3 · #38 Sanguine drawing — own sheet](Refs-v3-38-Sanguine-drawing-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 5 % → 44 % | 9.4 px | 0.46 | 8.46 | 88 |
| stroke 2 | 6 % → 32 % | 8.6 px | 0.51 | 5.27 | 9 |
| stroke 3 | 9 % → 42 % | 13.5 px | 0.46 | 4.91 | 18 |
| stroke 4 | 7 % → 33 % | 9.8 px | 0.48 | 4.80 | 32 |
| stroke 5 | 16 % → 32 % | 22.1 px | 0.48 | 1.98 | 39 |
| stroke 6 | 10 % → 46 % | 14.3 px | 0.47 | 4.38 | 20 |
| stroke 7 | 14 % → 42 % | 19.1 px | 0.48 | 3.09 | 13 |
| stroke 8 | 16 % → 30 % | 29.1 px | 0.49 | 1.83 | 9 |
| stroke 9 | 24 % → 29 % | 51.9 px | 0.48 | 1.21 | 12 |
| stroke 10 | 33 % → 32 % | 54.6 px | 0.47 | 0.99 | 15 |
| stroke 11 | 31 % → 27 % | 87.2 px | 0.44 | 0.88 | 3 |
| stroke 12 | 21 % → 40 % | 44.2 px | 0.49 | 1.88 | 6 |
| stroke 13 | 34 % → 18 % | 83.7 px | 0.51 | 0.52 | 4 |
| stroke 14 | 24 % → 35 % | 51.7 px | 0.47 | 1.44 | 9 |
| stroke 15 | 13 % → 51 % | 35.9 px | 0.45 | 4.02 | 6 |
| stroke 16 | 15 % → 50 % | 17.3 px | 0.47 | 3.29 | 69 |
| stroke 17 | 25 % → 44 % | 35.3 px | 0.48 | 1.75 | 27 |
| stroke 18 | 29 % → 36 % | 29.1 px | 0.45 | 1.23 | 30 |
| stroke 19 | 39 % → 28 % | 42.2 px | 0.49 | 0.71 | 46 |
| stroke 20 | 28 % → 39 % | 33.0 px | 0.49 | 1.40 | 36 |
| stroke 21 | 30 % → 43 % | 44.6 px | 0.47 | 1.46 | 19 |
| stroke 22 | 40 % → 28 % | 41.6 px | 0.49 | 0.69 | 40 |
| stroke 23 | 33 % → 40 % | 31.0 px | 0.48 | 1.20 | 43 |
| stroke 24 | 32 % → 38 % | 37.7 px | 0.49 | 1.17 | 43 |
| stroke 25 | 38 % → 32 % | 114.4 px | 0.50 | 0.83 | 4 |
| stroke 26 | 7 % → 29 % | 10.4 px | 0.48 | 4.00 | 25 |
| stroke 27 | 22 % → 43 % | 45.1 px | 0.49 | 1.96 | 12 |
| stroke 28 | 15 % → 32 % | 18.1 px | 0.49 | 2.15 | 41 |
| stroke 29 | 16 % → 31 % | 20.2 px | 0.49 | 1.91 | 58 |
| stroke 30 | 7 % → 51 % | 8.4 px | 0.48 | 7.39 | 15 |
| stroke 31 | 6 % → 38 % | 10.0 px | 0.47 | 6.61 | 37 |
| stroke 32 | 6 % → 43 % | 10.1 px | 0.48 | 6.72 | 15 |
| stroke 33 | 13 % → 38 % | 21.1 px | 0.48 | 2.87 | 345 |
| stroke 34 | 13 % → 46 % | 16.3 px | 0.47 | 3.63 | 13 |
| stroke 35 | 25 % → 40 % | 39.0 px | 0.48 | 1.62 | 14 |
| stroke 36 | 25 % → 40 % | 45.0 px | 0.48 | 1.58 | 8 |
| stroke 37 | 23 % → 47 % | 26.8 px | 0.48 | 2.07 | 41 |
| stroke 38 | 29 % → 40 % | 33.0 px | 0.49 | 1.40 | 43 |
| stroke 39 | 18 % → 52 % | 18.3 px | 0.48 | 2.88 | 47 |
| stroke 40 | 17 % → 51 % | 15.0 px | 0.48 | 3.07 | 57 |
| stroke 41 | 23 % → 47 % | 26.2 px | 0.48 | 2.03 | 42 |
| stroke 42 | 33 % → 44 % | 43.6 px | 0.48 | 1.32 | 80 |
| stroke 43 | 31 % → 48 % | 82.5 px | 0.48 | 1.56 | 9 |
| stroke 44 | 8 % → 54 % | 9.8 px | 0.48 | 6.48 | 24 |
| stroke 45 | 10 % → 49 % | 15.1 px | 0.47 | 5.13 | 11 |
| stroke 46 | 8 % → 14 % | 18.6 px | 0.45 | 1.86 | 8 |
| stroke 47 | 15 % → 55 % | 32.6 px | 0.47 | 3.72 | 3 |
| stroke 48 | 21 % → 43 % | 47.6 px | 0.49 | 2.06 | 4 |
| stroke 49 | 20 % → 27 % | 37.8 px | 0.48 | 1.39 | 11 |
| stroke 50 | 15 % → 53 % | 17.3 px | 0.48 | 3.48 | 38 |
| stroke 51 | 17 % → 53 % | 17.7 px | 0.48 | 3.08 | 43 |
| stroke 52 | 26 % → 54 % | 105.3 px | 0.47 | 2.10 | 6 |
| stroke 53 | 24 % → 40 % | 25.0 px | 0.47 | 1.66 | 43 |
| stroke 54 | 30 % → 43 % | 31.3 px | 0.47 | 1.44 | 38 |
| stroke 55 | 25 % → 16 % | 43.7 px | 0.47 | 0.65 | 23 |
| stroke 56 | 7 % → 31 % | 8.6 px | 0.49 | 4.16 | 26 |
| stroke 57 | 6 % → 41 % | 9.7 px | 0.48 | 6.88 | 17 |
| stroke 58 | 7 % → 39 % | 9.1 px | 0.49 | 5.93 | 15 |
| stroke 59 | 26 % → 40 % | 51.4 px | 0.49 | 1.53 | 7 |
| stroke 60 | 12 % → 42 % | 28.5 px | 0.47 | 3.50 | 6 |
| stroke 61 | 17 % → 32 % | 30.2 px | 0.48 | 1.92 | 6 |
| stroke 62 | 13 % → 30 % | 20.7 px | 0.48 | 2.30 | 20 |
| stroke 63 | 26 % → 14 % | 73.3 px | 0.51 | 0.54 | 2 |
| stroke 64 | 17 % → 35 % | 44.7 px | 0.50 | 2.01 | 2 |
| stroke 65 | 24 % → 41 % | 67.6 px | 0.46 | 1.70 | 4 |
| stroke 66 | 27 % → 37 % | 65.6 px | 0.48 | 1.37 | 3 |
| stroke 67 | 21 % → 22 % | 41.2 px | 0.49 | 1.08 | 10 |
| stroke 68 | 29 % → 37 % | 63.8 px | 0.48 | 1.28 | 10 |
| stroke 69 | 22 % → 42 % | 50.2 px | 0.49 | 1.94 | 3 |
| stroke 70 | 28 % → 22 % | 30.5 px | 0.49 | 0.77 | 32 |
| stroke 71 | 34 % → 31 % | 40.0 px | 0.49 | 0.89 | 30 |
| stroke 72 | 27 % → 38 % | 26.1 px | 0.49 | 1.40 | 42 |
| stroke 73 | 34 % → 38 % | 37.1 px | 0.49 | 1.12 | 39 |
| stroke 74 | 37 % → 34 % | 44.8 px | 0.49 | 0.94 | 38 |
| stroke 75 | 28 % → 36 % | 28.2 px | 0.50 | 1.28 | 34 |
| stroke 76 | 32 % → 27 % | 50.8 px | 0.49 | 0.84 | 11 |
| stroke 77 | 31 % → 39 % | 39.6 px | 0.49 | 1.29 | 13 |
| stroke 78 | 26 % → 38 % | 27.9 px | 0.49 | 1.49 | 38 |
| stroke 79 | 39 % → 34 % | 39.8 px | 0.48 | 0.87 | 47 |
| stroke 80 | 35 % → 43 % | 71.8 px | 0.47 | 1.24 | 12 |
| stroke 81 | 4 % → 55 % | 10.9 px | 0.49 | 14.27 | 3 |
| stroke 82 | 10 % → 60 % | 17.2 px | 0.49 | 6.10 | 14 |
| stroke 83 | 15 % → 56 % | 15.7 px | 0.49 | 3.75 | 23 |
| stroke 84 | 22 % → 48 % | 49.0 px | 0.48 | 2.14 | 7 |
| stroke 85 | 29 % → 47 % | 26.7 px | 0.48 | 1.65 | 22 |
| stroke 86 | 7 % → 40 % | 10.8 px | 0.48 | 5.64 | 19 |
| stroke 87 | 7 % → 43 % | 16.0 px | 0.47 | 6.63 | 4 |
| stroke 88 | 7 % → 46 % | 10.7 px | 0.48 | 6.71 | 16 |
| stroke 89 | 10 % → 42 % | 15.2 px | 0.48 | 4.14 | 17 |
| stroke 90 | 15 % → 34 % | 20.8 px | 0.46 | 2.26 | 18 |
| stroke 91 | 10 % → 22 % | 11.0 px | 0.46 | 2.20 | 20 |
| stroke 92 | 9 % → 48 % | 13.8 px | 0.42 | 5.12 | 16 |
| stroke 93 | 11 % → 46 % | 23.7 px | 0.47 | 4.01 | 10 |
| stroke 94 | 11 % → 55 % | 14.5 px | 0.44 | 4.80 | 14 |
| stroke 95 | 6 % → 35 % | 15.1 px | 0.47 | 5.87 | 3 |
| stroke 96 | 21 % → 54 % | 31.6 px | 0.46 | 2.53 | 12 |
| stroke 97 | 21 % → 51 % | 27.7 px | 0.41 | 2.41 | 17 |
| stroke 98 | 16 % → 36 % | 36.8 px | 0.48 | 2.21 | 4 |
| stroke 99 | 19 % → 64 % | 33.4 px | 0.46 | 3.28 | 11 |
| stroke 100 | 31 % → 50 % | 72.4 px | 0.46 | 1.60 | 3 |
| stroke 101 | 27 % → 34 % | 45.4 px | 0.49 | 1.24 | 11 |
| stroke 102 | 22 % → 38 % | 26.9 px | 0.48 | 1.75 | 15 |
| stroke 103 | 21 % → 25 % | 31.7 px | 0.51 | 1.21 | 15 |
| stroke 104 | 17 % → 42 % | 34.0 px | 0.47 | 2.49 | 11 |
| stroke 105 | 26 % → 40 % | 42.1 px | 0.49 | 1.50 | 16 |
| stroke 106 | 28 % → 30 % | 34.8 px | 0.47 | 1.05 | 17 |
| stroke 107 | 23 % → 58 % | 60.0 px | 0.39 | 2.47 | 6 |
| stroke 108 | 20 % → 50 % | 57.0 px | 0.47 | 2.47 | 13 |
| stroke 109 | 30 % → 8 % | 37.7 px | 0.47 | 0.27 | 22 |
| stroke 110 | 14 % → 48 % | 35.3 px | 0.46 | 3.57 | 14 |
| stroke 111 | 43 % → 32 % | 73.8 px | 0.48 | 0.73 | 53 |
| stroke 112 | 10 % → 44 % | 19.3 px | 0.50 | 4.31 | 15 |
| stroke 113 | 17 % → 30 % | 31.1 px | 0.47 | 1.78 | 35 |
| stroke 114 | 37 % → 41 % | 87.1 px | 0.46 | 1.09 | 25 |
| stroke 115 | 35 % → 56 % | 52.2 px | 0.42 | 1.57 | 17 |
| stroke 116 | 30 % → 44 % | 83.8 px | 0.50 | 1.46 | 10 |
| stroke 117 | 32 % → 39 % | 63.1 px | 0.45 | 1.21 | 43 |
| stroke 118 | 21 % → 48 % | 44.9 px | 0.48 | 2.27 | 34 |
| stroke 119 | 32 % → 34 % | 70.8 px | 0.47 | 1.04 | 10 |
| stroke 120 | 28 % → 39 % | 75.9 px | 0.46 | 1.38 | 15 |
| stroke 121 | 28 % → 33 % | 76.3 px | 0.50 | 1.20 | 5 |
| stroke 122 | 28 % → 43 % | 37.4 px | 0.48 | 1.57 | 162 |
| stroke 123 | 43 % → 43 % | 48.2 px | 0.49 | 0.99 | 90 |
| stroke 124 | 38 % → 49 % | 44.6 px | 0.48 | 1.28 | 113 |
| stroke 125 | 38 % → 44 % | 40.1 px | 0.46 | 1.16 | 150 |
| stroke 126 | 44 % → 42 % | 51.5 px | 0.44 | 0.96 | 45 |
| stroke 127 | 32 % → 54 % | 35.4 px | 0.43 | 1.67 | 164 |
| stroke 128 | 33 % → 48 % | 40.3 px | 0.45 | 1.44 | 914 |
| stroke 129 | 33 % → 45 % | 46.3 px | 0.47 | 1.36 | 142 |
| stroke 130 | 33 % → 35 % | 31.3 px | 0.47 | 1.08 | 99 |
| stroke 131 | 34 % → 30 % | 36.4 px | 0.48 | 0.88 | 143 |
| stroke 132 | 38 % → 39 % | 39.3 px | 0.47 | 1.03 | 116 |
| stroke 133 | 40 % → 32 % | 45.6 px | 0.49 | 0.79 | 151 |
| stroke 134 | 31 % → 40 % | 34.9 px | 0.48 | 1.31 | 76 |
| stroke 135 | 36 % → 49 % | 119.3 px | 0.46 | 1.37 | 9 |
| stroke 136 | 44 % → 31 % | 50.5 px | 0.47 | 0.71 | 84 |
| stroke 137 | 45 % → 24 % | 50.2 px | 0.48 | 0.53 | 68 |
| stroke 138 | 46 % → 31 % | 50.2 px | 0.48 | 0.68 | 47 |
| stroke 139 | 41 % → 46 % | 47.4 px | 0.44 | 1.12 | 58 |
| stroke 140 | 57 % → 32 % | 60.6 px | 0.45 | 0.55 | 72 |
| stroke 141 | 73 % → 11 % | 182.7 px | 0.47 | 0.15 | 6 |
| stroke 142 | 24 % → 41 % | 19.4 px | 0.49 | 1.72 | 70 |
| stroke 143 | 21 % → 44 % | 59.0 px | 0.50 | 2.06 | 10 |
| stroke 144 | 8 % → 58 % | 10.1 px | 0.48 | 7.34 | 13 |
| stroke 145 | 19 % → 59 % | 47.4 px | 0.47 | 3.15 | 6 |
| stroke 146 | 16 % → 61 % | 15.1 px | 0.48 | 3.87 | 43 |
| stroke 147 | 24 % → 56 % | 32.8 px | 0.48 | 2.37 | 32 |
| stroke 148 | 33 % → 67 % | 73.7 px | 0.47 | 2.03 | 8 |
| stroke 149 | 36 % → 63 % | 38.7 px | 0.47 | 1.72 | 22 |
| stroke 150 | 11 % → 58 % | 17.5 px | 0.48 | 5.43 | 16 |
| stroke 151 | 21 % → 64 % | 50.9 px | 0.48 | 3.09 | 8 |
| stroke 152 | 18 % → 58 % | 44.9 px | 0.47 | 3.14 | 3 |
| stroke 153 | 19 % → 58 % | 21.6 px | 0.47 | 3.04 | 81 |
| stroke 154 | 25 % → 63 % | 40.2 px | 0.47 | 2.56 | 53 |
| stroke 155 | 8 % → 52 % | 13.4 px | 0.48 | 6.79 | 10 |
| stroke 156 | 14 % → 47 % | 22.7 px | 0.48 | 3.29 | 29 |
| stroke 157 | 18 % → 46 % | 48.9 px | 0.47 | 2.53 | 5 |
| stroke 158 | 22 % → 49 % | 35.0 px | 0.48 | 2.27 | 17 |
| stroke 159 | 30 % → 48 % | 61.3 px | 0.48 | 1.58 | 21 |
| stroke 160 | 23 % → 50 % | 53.1 px | 0.48 | 2.17 | 5 |
| stroke 161 | 27 % → 47 % | 27.1 px | 0.48 | 1.72 | 57 |
| stroke 162 | 29 % → 52 % | 37.3 px | 0.48 | 1.76 | 68 |
| stroke 163 | 31 % → 50 % | 48.3 px | 0.49 | 1.62 | 35 |
| stroke 164 | 9 % → 65 % | 26.1 px | 0.48 | 6.96 | 9 |
| stroke 165 | 13 % → 64 % | 16.2 px | 0.48 | 4.87 | 18 |
| stroke 166 | 5 % → 41 % | 11.0 px | 0.50 | 8.23 | 5 |
| stroke 167 | 8 % → 48 % | 12.5 px | 0.51 | 6.10 | 33 |
| stroke 168 | 11 % → 26 % | 18.2 px | 0.51 | 2.49 | 5 |
| stroke 169 | 16 % → 44 % | 44.3 px | 0.51 | 2.82 | 8 |
| stroke 170 | 13 % → 48 % | 31.7 px | 0.49 | 3.78 | 4 |
| stroke 171 | 15 % → 38 % | 36.7 px | 0.51 | 2.50 | 17 |
| stroke 172 | 19 % → 53 % | 16.2 px | 0.49 | 2.86 | 58 |
| stroke 173 | 19 % → 40 % | 18.6 px | 0.51 | 2.08 | 54 |
| stroke 174 | 22 % → 32 % | 45.1 px | 0.51 | 1.45 | 17 |
| stroke 175 | 20 % → 35 % | 21.7 px | 0.51 | 1.71 | 70 |
| stroke 176 | 21 % → 47 % | 19.7 px | 0.50 | 2.19 | 37 |
| stroke 177 | 25 % → 41 % | 37.2 px | 0.51 | 1.63 | 44 |
| stroke 178 | 7 % → 60 % | 16.1 px | 0.47 | 8.31 | 9 |
| stroke 179 | 11 % → 60 % | 12.0 px | 0.47 | 5.32 | 41 |
| stroke 180 | 5 % → 15 % | 11.9 px | 0.46 | 2.87 | 11 |
| stroke 181 | 11 % → 16 % | 24.1 px | 0.45 | 1.44 | 10 |
| stroke 182 | 15 % → 32 % | 42.2 px | 0.48 | 2.11 | 4 |
| stroke 183 | 13 % → 19 % | 12.3 px | 0.48 | 1.48 | 41 |
| stroke 184 | 18 % → 15 % | 28.6 px | 0.46 | 0.82 | 18 |
| stroke 185 | 15 % → 24 % | 41.3 px | 0.53 | 1.66 | 6 |
| stroke 186 | 13 % → 31 % | 36.8 px | 0.53 | 2.30 | 6 |
| stroke 187 | 20 % → 26 % | 29.0 px | 0.53 | 1.31 | 12 |
| stroke 188 | 20 % → 32 % | 44.3 px | 0.52 | 1.64 | 6 |
| stroke 189 | 28 % → 32 % | 30.5 px | 0.52 | 1.13 | 25 |
| stroke 190 | 6 % → 57 % | 10.4 px | 0.49 | 9.83 | 18 |
| stroke 191 | 11 % → 50 % | 20.1 px | 0.48 | 4.40 | 16 |
| stroke 192 | 13 % → 54 % | 11.7 px | 0.49 | 4.08 | 54 |
| stroke 193 | 20 % → 54 % | 38.7 px | 0.49 | 2.67 | 50 |
| stroke 194 | 12 % → 45 % | 22.3 px | 0.47 | 3.62 | 16 |
| stroke 195 | 18 % → 32 % | 51.0 px | 0.46 | 1.79 | 5 |
| stroke 196 | 20 % → 39 % | 17.6 px | 0.47 | 1.93 | 32 |
| stroke 197 | 6 % → 32 % | 9.0 px | 0.48 | 5.25 | 13 |
| stroke 198 | 11 % → 39 % | 19.3 px | 0.48 | 3.65 | 16 |
| stroke 199 | 11 % → 37 % | 14.7 px | 0.49 | 3.27 | 17 |
| stroke 200 | 14 % → 53 % | 15.7 px | 0.49 | 3.77 | 26 |
| stroke 201 | 23 % → 39 % | 27.2 px | 0.51 | 1.71 | 26 |
| stroke 202 | 17 % → 51 % | 42.8 px | 0.46 | 3.04 | 3 |
| stroke 203 | 19 % → 49 % | 25.9 px | 0.49 | 2.54 | 22 |
| stroke 204 | 25 % → 44 % | 63.5 px | 0.50 | 1.73 | 5 |
| stroke 205 | 28 % → 31 % | 60.7 px | 0.46 | 1.11 | 5 |
| stroke 206 | 19 % → 40 % | 23.2 px | 0.48 | 2.08 | 35 |
| stroke 207 | 25 % → 41 % | 26.8 px | 0.50 | 1.65 | 199 |
| stroke 208 | 23 % → 52 % | 20.9 px | 0.49 | 2.23 | 80 |
| stroke 209 | 34 % → 52 % | 34.9 px | 0.49 | 1.51 | 40 |
| stroke 210 | 35 % → 43 % | 36.9 px | 0.47 | 1.24 | 48 |
| stroke 211 | 33 % → 39 % | 58.4 px | 0.46 | 1.19 | 34 |
| stroke 212 | 6 % → 48 % | 9.6 px | 0.47 | 7.85 | 21 |
| stroke 213 | 8 % → 22 % | 10.6 px | 0.47 | 2.90 | 27 |
| stroke 214 | 10 % → 34 % | 17.5 px | 0.46 | 3.43 | 11 |
| stroke 215 | 6 % → 20 % | 9.8 px | 0.48 | 3.20 | 52 |
| stroke 216 | 6 % → 25 % | 10.7 px | 0.46 | 3.94 | 13 |
| stroke 217 | 9 % → 43 % | 14.5 px | 0.47 | 4.68 | 16 |
| stroke 218 | 14 % → 22 % | 21.6 px | 0.48 | 1.62 | 15 |
| stroke 219 | 12 % → 44 % | 16.7 px | 0.48 | 3.63 | 19 |
| stroke 220 | 6 % → 40 % | 11.4 px | 0.53 | 6.86 | 6 |
| stroke 221 | 6 % → 23 % | 10.3 px | 0.47 | 3.94 | 10 |
| stroke 222 | 6 % → 0 % | 11.4 px | 0.00 | 0.00 | 10 |
| stroke 223 | 13 % → 51 % | 21.6 px | 0.46 | 3.99 | 20 |
| stroke 224 | 6 % → 20 % | 9.9 px | 0.50 | 3.47 | 14 |
| stroke 225 | 6 % → 36 % | 10.1 px | 0.51 | 5.90 | 17 |
| stroke 226 | 6 % → 59 % | 9.6 px | 0.46 | 9.53 | 15 |
| stroke 227 | 14 % → 13 % | 18.2 px | 0.49 | 0.99 | 28 |
| stroke 228 | 8 % → 27 % | 20.1 px | 0.50 | 3.31 | 7 |
| stroke 229 | 10 % → 53 % | 16.7 px | 0.46 | 5.35 | 11 |
| stroke 230 | 13 % → 55 % | 21.7 px | 0.47 | 4.10 | 10 |
| stroke 231 | 17 % → 16 % | 25.2 px | 0.48 | 0.95 | 9 |
| stroke 232 | 6 % → 40 % | 10.9 px | 0.46 | 7.04 | 8 |
| stroke 233 | 5 % → 46 % | 9.6 px | 0.46 | 8.60 | 11 |
| stroke 234 | 15 % → 47 % | 16.8 px | 0.47 | 3.18 | 25 |
| stroke 235 | 26 % → 10 % | 50.6 px | 0.49 | 0.37 | 4 |
| stroke 236 | 11 % → 27 % | 17.5 px | 0.50 | 2.44 | 16 |
| stroke 237 | 10 % → 31 % | 15.7 px | 0.49 | 3.00 | 23 |
| stroke 238 | 13 % → 21 % | 21.7 px | 0.49 | 1.54 | 16 |
| stroke 239 | 6 % → 44 % | 10.1 px | 0.46 | 7.13 | 13 |
| stroke 240 | 6 % → 47 % | 9.6 px | 0.46 | 7.64 | 23 |
| stroke 241 | 12 % → 50 % | 20.2 px | 0.46 | 4.02 | 13 |
| stroke 242 | 7 % → 20 % | 9.5 px | 0.48 | 3.03 | 14 |
| stroke 243 | 16 % → 49 % | 26.7 px | 0.48 | 3.08 | 16 |
| stroke 244 | 12 % → 43 % | 16.2 px | 0.49 | 3.74 | 25 |
| stroke 245 | 13 % → 48 % | 19.9 px | 0.46 | 3.79 | 22 |
| stroke 246 | 12 % → 39 % | 19.3 px | 0.46 | 3.18 | 16 |
| stroke 247 | 13 % → 39 % | 16.2 px | 0.49 | 2.92 | 15 |
| stroke 248 | 27 % → 30 % | 62.5 px | 0.49 | 1.10 | 4 |
| stroke 249 | 9 % → 43 % | 13.7 px | 0.47 | 4.99 | 17 |
| stroke 250 | 28 % → 25 % | 34.6 px | 0.48 | 0.88 | 19 |
| stroke 251 | 13 % → 29 % | 19.4 px | 0.46 | 2.14 | 21 |
| stroke 252 | 22 % → 37 % | 42.0 px | 0.46 | 1.70 | 14 |
| stroke 253 | 11 % → 36 % | 18.8 px | 0.52 | 3.23 | 10 |
| stroke 254 | 11 % → 12 % | 18.6 px | 0.53 | 1.13 | 14 |
| stroke 255 | 13 % → 46 % | 25.2 px | 0.52 | 3.57 | 10 |
| stroke 256 | 13 % → 39 % | 27.7 px | 0.47 | 3.10 | 8 |
| stroke 257 | 23 % → 40 % | 41.6 px | 0.48 | 1.72 | 7 |
| stroke 258 | 15 % → 19 % | 24.4 px | 0.53 | 1.27 | 16 |
| stroke 259 | 18 % → 48 % | 28.1 px | 0.46 | 2.70 | 18 |
| stroke 260 | 8 % → 40 % | 8.7 px | 0.51 | 4.87 | 31 |
| stroke 261 | 13 % → 48 % | 21.5 px | 0.47 | 3.84 | 16 |
| stroke 262 | 14 % → 53 % | 21.1 px | 0.47 | 3.92 | 37 |
| stroke 263 | 23 % → 38 % | 36.0 px | 0.46 | 1.67 | 27 |
| stroke 264 | 19 % → 53 % | 31.7 px | 0.46 | 2.81 | 14 |
| stroke 265 | 30 % → 36 % | 64.4 px | 0.50 | 1.20 | 8 |
| stroke 266 | 32 % → 30 % | 47.3 px | 0.46 | 0.94 | 25 |
| stroke 267 | 14 % → 47 % | 33.4 px | 0.52 | 3.31 | 6 |
| stroke 268 | 14 % → 32 % | 20.7 px | 0.51 | 2.30 | 25 |
| stroke 269 | 8 % → 43 % | 21.9 px | 0.49 | 5.67 | 4 |
| stroke 270 | 16 % → 43 % | 22.5 px | 0.50 | 2.71 | 12 |
| stroke 271 | 16 % → 39 % | 26.7 px | 0.46 | 2.40 | 7 |
| stroke 272 | 16 % → 36 % | 21.3 px | 0.50 | 2.18 | 12 |
| stroke 273 | 13 % → 30 % | 20.7 px | 0.48 | 2.28 | 25 |
| stroke 274 | 10 % → 62 % | 26.5 px | 0.49 | 5.95 | 3 |
| stroke 275 | 15 % → 45 % | 24.4 px | 0.50 | 3.08 | 19 |
| stroke 276 | 16 % → 15 % | 28.9 px | 0.45 | 0.93 | 9 |
| stroke 277 | 10 % → 64 % | 17.6 px | 0.46 | 6.70 | 9 |
| stroke 278 | 13 % → 57 % | 31.6 px | 0.47 | 4.39 | 4 |
| stroke 279 | 27 % → 11 % | 68.3 px | 0.49 | 0.41 | 4 |
| stroke 280 | 19 % → 38 % | 54.0 px | 0.47 | 1.97 | 4 |
| stroke 281 | 28 % → 52 % | 63.0 px | 0.46 | 1.84 | 5 |
| stroke 282 | 15 % → 24 % | 28.7 px | 0.53 | 1.56 | 9 |
| stroke 283 | 19 % → 41 % | 39.6 px | 0.51 | 2.15 | 9 |
| stroke 284 | 12 % → 54 % | 18.8 px | 0.47 | 4.73 | 17 |
| stroke 285 | 25 % → 34 % | 37.7 px | 0.47 | 1.34 | 17 |
| stroke 286 | 44 % → 28 % | 75.7 px | 0.46 | 0.63 | 10 |
| stroke 287 | 18 % → 31 % | 28.1 px | 0.47 | 1.74 | 16 |
| stroke 288 | 23 % → 3 % | 27.2 px | 0.52 | 0.14 | 23 |
| stroke 289 | 17 % → 54 % | 33.0 px | 0.47 | 3.25 | 7 |
| stroke 290 | 20 % → 19 % | 48.7 px | 0.53 | 0.95 | 10 |
| stroke 291 | 23 % → 50 % | 37.7 px | 0.50 | 2.21 | 11 |
| stroke 292 | 22 % → 40 % | 39.8 px | 0.46 | 1.81 | 9 |
| stroke 293 | 17 % → 58 % | 36.7 px | 0.47 | 3.37 | 11 |
| stroke 294 | 24 % → 20 % | 41.6 px | 0.51 | 0.85 | 10 |
| stroke 295 | 25 % → 49 % | 42.0 px | 0.47 | 1.97 | 9 |
| stroke 296 | 23 % → 15 % | 49.9 px | 0.47 | 0.65 | 5 |
| stroke 297 | 8 % → 10 % | 15.7 px | 0.51 | 1.30 | 8 |
| stroke 298 | 30 % → 1 % | 84.6 px | 0.52 | 0.04 | 8 |
| stroke 299 | 24 % → 50 % | 43.9 px | 0.47 | 2.09 | 10 |
| stroke 300 | 28 % → 55 % | 77.8 px | 0.49 | 1.99 | 3 |
| stroke 301 | 17 % → 28 % | 48.2 px | 0.49 | 1.63 | 7 |
| stroke 302 | 23 % → 36 % | 33.1 px | 0.51 | 1.57 | 34 |
| stroke 303 | 36 % → 56 % | 69.6 px | 0.46 | 1.56 | 7 |
| stroke 304 | 23 % → 47 % | 36.9 px | 0.48 | 2.08 | 16 |
| stroke 305 | 19 % → 45 % | 28.6 px | 0.47 | 2.42 | 10 |
| stroke 306 | 12 % → 63 % | 23.7 px | 0.45 | 5.42 | 10 |
| stroke 307 | 27 % → 48 % | 39.3 px | 0.47 | 1.75 | 18 |
| stroke 308 | 18 % → 50 % | 28.0 px | 0.48 | 2.82 | 22 |
| stroke 309 | 28 % → 20 % | 47.0 px | 0.51 | 0.71 | 17 |
| stroke 310 | 17 % → 18 % | 33.9 px | 0.50 | 1.07 | 7 |
| stroke 311 | 31 % → 46 % | 51.0 px | 0.46 | 1.47 | 17 |
| stroke 312 | 16 % → 60 % | 38.2 px | 0.49 | 3.84 | 5 |
| stroke 313 | 17 % → 59 % | 28.9 px | 0.47 | 3.42 | 17 |
| stroke 314 | 19 % → 42 % | 31.8 px | 0.50 | 2.21 | 17 |
| stroke 315 | 24 % → 20 % | 39.6 px | 0.52 | 0.82 | 20 |
| stroke 316 | 14 % → 46 % | 30.6 px | 0.46 | 3.33 | 11 |
| stroke 317 | 15 % → 23 % | 43.0 px | 0.48 | 1.49 | 10 |
| stroke 318 | 20 % → 44 % | 48.2 px | 0.51 | 2.25 | 6 |
| stroke 319 | 7 % → 19 % | 20.8 px | 0.52 | 2.51 | 5 |
| stroke 320 | 22 % → 59 % | 53.9 px | 0.47 | 2.73 | 5 |
| stroke 321 | 37 % → 14 % | 81.7 px | 0.53 | 0.38 | 5 |
| stroke 322 | 40 % → 0 % | 65.7 px | 0.44 | 0.00 | 6 |
| stroke 323 | 40 % → 21 % | 76.1 px | 0.46 | 0.52 | 5 |
| stroke 324 | 33 % → 36 % | 94.3 px | 0.45 | 1.11 | 3 |
| stroke 325 | 34 % → 26 % | 83.9 px | 0.51 | 0.76 | 8 |
| stroke 326 | 18 % → 43 % | 31.3 px | 0.52 | 2.40 | 15 |
| stroke 327 | 37 % → 55 % | 90.2 px | 0.45 | 1.48 | 9 |
| stroke 328 | 18 % → 8 % | 30.6 px | 0.50 | 0.45 | 10 |
| stroke 329 | 21 % → 52 % | 38.7 px | 0.48 | 2.46 | 10 |
| stroke 330 | 40 % → 42 % | 82.4 px | 0.46 | 1.06 | 8 |
| stroke 331 | 20 % → 47 % | 51.0 px | 0.49 | 2.35 | 5 |
| stroke 332 | 18 % → 59 % | 43.0 px | 0.44 | 3.34 | 4 |
| stroke 333 | 27 % → 37 % | 44.7 px | 0.47 | 1.40 | 17 |
| stroke 334 | 44 % → 20 % | 89.8 px | 0.53 | 0.44 | 12 |
| stroke 335 | 25 % → 57 % | 41.3 px | 0.47 | 2.32 | 10 |
| stroke 336 | 28 % → 56 % | 66.7 px | 0.46 | 2.02 | 8 |
| stroke 337 | 39 % → 32 % | 85.5 px | 0.46 | 0.82 | 5 |
| stroke 338 | 24 % → 3 % | 40.4 px | 0.46 | 0.13 | 14 |
| stroke 339 | 31 % → 47 % | 67.6 px | 0.45 | 1.54 | 7 |
| stroke 340 | 33 % → 0 % | 72.4 px | 0.45 | 0.01 | 5 |
| stroke 341 | 21 % → 60 % | 45.7 px | 0.46 | 2.86 | 10 |
| stroke 342 | 27 % → 19 % | 61.9 px | 0.47 | 0.69 | 7 |
| stroke 343 | 22 % → 3 % | 43.5 px | 0.52 | 0.16 | 5 |
| stroke 344 | 33 % → 29 % | 70.2 px | 0.50 | 0.90 | 16 |
| stroke 345 | 27 % → 19 % | 53.8 px | 0.45 | 0.68 | 25 |
| stroke 346 | 30 % → 16 % | 69.1 px | 0.52 | 0.54 | 6 |
| stroke 347 | 50 % → 18 % | 90.6 px | 0.53 | 0.36 | 17 |
| stroke 348 | 29 % → 54 % | 64.8 px | 0.46 | 1.87 | 11 |
| stroke 349 | 22 % → 37 % | 56.2 px | 0.52 | 1.69 | 4 |
| stroke 350 | 32 % → 45 % | 71.5 px | 0.47 | 1.39 | 9 |
| stroke 351 | 46 % → 11 % | 128.6 px | 0.52 | 0.24 | 6 |
| stroke 352 | 43 % → 27 % | 124.0 px | 0.52 | 0.64 | 6 |
| stroke 353 | 22 % → 29 % | 24.5 px | 0.53 | 1.30 | 13 |
| stroke 354 | 35 % → 49 % | 86.7 px | 0.45 | 1.39 | 9 |
| stroke 355 | 33 % → 19 % | 94.9 px | 0.50 | 0.58 | 6 |
| stroke 356 | 34 % → 62 % | 94.8 px | 0.46 | 1.84 | 5 |
| stroke 357 | 24 % → 45 % | 67.9 px | 0.46 | 1.86 | 7 |
| stroke 358 | 30 % → 47 % | 73.9 px | 0.47 | 1.58 | 8 |
| stroke 359 | 26 % → 38 % | 62.7 px | 0.52 | 1.46 | 7 |
| stroke 360 | 38 % → 32 % | 88.6 px | 0.48 | 0.85 | 9 |
| stroke 361 | 42 % → 23 % | 113.8 px | 0.46 | 0.54 | 6 |
| stroke 362 | 43 % → 31 % | 122.8 px | 0.48 | 0.72 | 6 |
| stroke 363 | 28 % → 35 % | 66.6 px | 0.46 | 1.24 | 7 |
| stroke 364 | 33 % → 21 % | 69.8 px | 0.46 | 0.64 | 9 |
| stroke 365 | 33 % → 61 % | 91.0 px | 0.48 | 1.84 | 11 |
| stroke 366 | 44 % → 27 % | 103.6 px | 0.45 | 0.63 | 5 |
| stroke 367 | 27 % → 50 % | 77.9 px | 0.48 | 1.83 | 6 |
| stroke 368 | 42 % → 49 % | 90.4 px | 0.46 | 1.17 | 7 |
| stroke 369 | 35 % → 15 % | 55.5 px | 0.50 | 0.44 | 9 |
| stroke 370 | 31 % → 41 % | 84.7 px | 0.47 | 1.33 | 3 |
| stroke 371 | 36 % → 39 % | 96.8 px | 0.46 | 1.10 | 7 |
| stroke 372 | 45 % → 27 % | 127.5 px | 0.53 | 0.61 | 7 |
| stroke 373 | 41 % → 44 % | 91.0 px | 0.47 | 1.08 | 5 |
| stroke 374 | 41 % → 42 % | 90.4 px | 0.46 | 1.03 | 4 |
| stroke 375 | 27 % → 47 % | 75.1 px | 0.47 | 1.74 | 7 |
| stroke 376 | 34 % → 32 % | 90.4 px | 0.46 | 0.95 | 6 |
| stroke 377 | 42 % → 28 % | 103.3 px | 0.46 | 0.67 | 4 |
| stroke 378 | 52 % → 10 % | 109.9 px | 0.45 | 0.19 | 12 |
| stroke 379 | 25 % → 39 % | 51.4 px | 0.51 | 1.56 | 14 |
| stroke 380 | 25 % → 1 % | 55.5 px | 0.46 | 0.04 | 4 |
| stroke 381 | 36 % → 15 % | 102.1 px | 0.45 | 0.42 | 8 |
| stroke 382 | 15 % → 60 % | 41.6 px | 0.46 | 4.04 | 5 |
| stroke 383 | 23 % → 10 % | 29.1 px | 0.50 | 0.46 | 37 |
| stroke 384 | 35 % → 34 % | 41.6 px | 0.48 | 0.97 | 54 |
| stroke 385 | 36 % → 55 % | 41.4 px | 0.47 | 1.51 | 50 |
| stroke 386 | 33 % → 36 % | 40.6 px | 0.50 | 1.07 | 42 |
| stroke 387 | 29 % → 31 % | 28.9 px | 0.51 | 1.06 | 37 |
| stroke 388 | 28 % → 39 % | 30.9 px | 0.52 | 1.40 | 36 |
| stroke 389 | 38 % → 46 % | 44.5 px | 0.49 | 1.21 | 41 |
| stroke 390 | 49 % → 54 % | 52.3 px | 0.47 | 1.11 | 48 |
| stroke 391 | 51 % → 40 % | 50.5 px | 0.47 | 0.79 | 38 |
| stroke 392 | 39 % → 36 % | 38.1 px | 0.48 | 0.93 | 66 |
| stroke 393 | 42 % → 34 % | 27.0 px | 0.49 | 0.82 | 41 |
| stroke 394 | 35 % → 37 % | 41.9 px | 0.49 | 1.06 | 48 |
| stroke 395 | 48 % → 31 % | 59.4 px | 0.47 | 0.65 | 49 |
| stroke 396 | 31 % → 51 % | 30.8 px | 0.47 | 1.66 | 36 |
| stroke 397 | 39 % → 48 % | 40.1 px | 0.46 | 1.22 | 49 |
| stroke 398 | 48 % → 48 % | 58.2 px | 0.46 | 1.01 | 51 |
| stroke 399 | 38 % → 46 % | 45.2 px | 0.46 | 1.21 | 44 |
| stroke 400 | 31 % → 49 % | 32.7 px | 0.46 | 1.56 | 46 |
| stroke 401 | 41 % → 44 % | 56.6 px | 0.46 | 1.07 | 30 |
| stroke 402 | 42 % → 47 % | 48.5 px | 0.46 | 1.13 | 40 |
| stroke 403 | 41 % → 52 % | 36.9 px | 0.46 | 1.25 | 42 |
| stroke 404 | 41 % → 51 % | 44.1 px | 0.46 | 1.24 | 38 |
| stroke 405 | 34 % → 58 % | 32.6 px | 0.47 | 1.71 | 42 |
| stroke 406 | 48 % → 40 % | 56.1 px | 0.46 | 0.84 | 43 |
| stroke 407 | 44 % → 41 % | 45.5 px | 0.46 | 0.93 | 44 |
| stroke 408 | 45 % → 45 % | 58.5 px | 0.46 | 1.00 | 50 |
| stroke 409 | 26 % → 55 % | 30.5 px | 0.48 | 2.09 | 30 |
| stroke 410 | 34 % → 52 % | 43.1 px | 0.47 | 1.56 | 55 |
| stroke 411 | 40 % → 50 % | 42.3 px | 0.47 | 1.27 | 45 |
| stroke 412 | 42 % → 44 % | 44.7 px | 0.46 | 1.05 | 40 |
| stroke 413 | 49 % → 42 % | 58.0 px | 0.46 | 0.85 | 41 |
| stroke 414 | 56 % → 40 % | 73.1 px | 0.46 | 0.72 | 41 |
| stroke 415 | 36 % → 48 % | 49.7 px | 0.48 | 1.34 | 50 |
| stroke 416 | 40 % → 48 % | 41.6 px | 0.48 | 1.21 | 39 |
| stroke 417 | 49 % → 39 % | 52.7 px | 0.46 | 0.79 | 87 |
| stroke 418 | 41 % → 28 % | 48.7 px | 0.49 | 0.70 | 71 |
| stroke 419 | 24 % → 39 % | 24.3 px | 0.52 | 1.59 | 41 |
| stroke 420 | 34 % → 38 % | 38.2 px | 0.52 | 1.10 | 49 |
| stroke 421 | 23 % → 42 % | 22.0 px | 0.51 | 1.78 | 40 |
| stroke 422 | 37 % → 38 % | 43.4 px | 0.49 | 1.03 | 64 |
| stroke 423 | 37 % → 39 % | 41.2 px | 0.47 | 1.04 | 34 |
| stroke 424 | 30 % → 20 % | 35.4 px | 0.48 | 0.65 | 42 |
| stroke 425 | 20 % → 43 % | 29.2 px | 0.49 | 2.16 | 12 |
| stroke 426 | 27 % → 18 % | 40.0 px | 0.49 | 0.68 | 41 |
| stroke 427 | 38 % → 2 % | 42.8 px | 0.51 | 0.04 | 70 |
| stroke 428 | 38 % → 16 % | 34.6 px | 0.52 | 0.42 | 48 |
| stroke 429 | 40 % → 30 % | 58.7 px | 0.53 | 0.73 | 52 |
| stroke 430 | 31 % → 53 % | 42.3 px | 0.49 | 1.71 | 37 |
| stroke 431 | 43 % → 56 % | 44.1 px | 0.47 | 1.30 | 41 |
| stroke 432 | 46 % → 57 % | 47.5 px | 0.47 | 1.24 | 48 |
| stroke 433 | 49 % → 58 % | 57.6 px | 0.46 | 1.17 | 70 |
| stroke 434 | 48 % → 54 % | 53.1 px | 0.47 | 1.12 | 65 |
| stroke 435 | 51 % → 44 % | 59.9 px | 0.47 | 0.85 | 63 |
| stroke 436 | 44 % → 54 % | 44.8 px | 0.47 | 1.23 | 36 |
| stroke 437 | 53 % → 39 % | 42.9 px | 0.47 | 0.73 | 36 |
| stroke 438 | 52 % → 41 % | 62.3 px | 0.46 | 0.79 | 68 |
| stroke 439 | 43 % → 44 % | 55.5 px | 0.48 | 1.01 | 36 |
| stroke 440 | 47 % → 42 % | 52.0 px | 0.48 | 0.89 | 33 |
| stroke 441 | 44 % → 52 % | 49.7 px | 0.46 | 1.18 | 107 |
| stroke 442 | 55 % → 57 % | 56.5 px | 0.46 | 1.04 | 57 |
| stroke 443 | 45 % → 55 % | 46.3 px | 0.47 | 1.22 | 106 |
| stroke 444 | 41 % → 42 % | 51.4 px | 0.51 | 1.04 | 82 |
| stroke 445 | 39 % → 34 % | 44.8 px | 0.52 | 0.87 | 182 |
| stroke 446 | 34 % → 40 % | 45.9 px | 0.52 | 1.18 | 66 |
| stroke 447 | 36 % → 37 % | 40.1 px | 0.51 | 1.03 | 77 |
| stroke 448 | 31 % → 47 % | 30.9 px | 0.48 | 1.50 | 130 |
| stroke 449 | 39 % → 26 % | 47.6 px | 0.48 | 0.67 | 133 |
| stroke 450 | 36 % → 27 % | 71.8 px | 0.50 | 0.76 | 18 |
| stroke 451 | 23 % → 60 % | 27.9 px | 0.47 | 2.59 | 301 |
| stroke 452 | 28 % → 55 % | 30.3 px | 0.47 | 1.95 | 129 |
| stroke 453 | 39 % → 62 % | 47.9 px | 0.46 | 1.61 | 70 |
| stroke 454 | 42 % → 58 % | 33.0 px | 0.46 | 1.36 | 103 |
| stroke 455 | 50 % → 31 % | 46.4 px | 0.49 | 0.61 | 111 |
| stroke 456 | 69 % → 9 % | 256.3 px | 0.46 | 0.13 | 43 |
| stroke 457 | 55 % → 30 % | 59.0 px | 0.53 | 0.54 | 242 |
| stroke 458 | 62 % → 17 % | 120.6 px | 0.53 | 0.28 | 44 |
| stroke 459 | 54 % → 19 % | 65.5 px | 0.48 | 0.34 | 71 |
| stroke 460 | 69 % → 6 % | 72.4 px | 0.52 | 0.09 | 71 |
| stroke 461 | 63 % → 8 % | 80.2 px | 0.46 | 0.12 | 40 |
| stroke 462 | 56 % → 32 % | 72.4 px | 0.47 | 0.58 | 47 |
| stroke 463 | 50 % → 45 % | 50.8 px | 0.46 | 0.90 | 74 |
| stroke 464 | 59 % → 41 % | 79.5 px | 0.47 | 0.69 | 62 |
| stroke 465 | 51 % → 31 % | 62.7 px | 0.47 | 0.60 | 46 |
| stroke 466 | 59 % → 31 % | 69.3 px | 0.47 | 0.53 | 144 |
| stroke 467 | 53 % → 12 % | 93.1 px | 0.49 | 0.22 | 20 |
| stroke 468 | 34 % → 14 % | 33.8 px | 0.52 | 0.42 | 63 |
| stroke 469 | 35 % → 28 % | 35.9 px | 0.53 | 0.80 | 61 |
| stroke 470 | 37 % → 25 % | 48.2 px | 0.52 | 0.67 | 84 |
| stroke 471 | 26 % → 39 % | 37.5 px | 0.50 | 1.52 | 67 |
| stroke 472 | 26 % → 44 % | 26.8 px | 0.51 | 1.71 | 116 |
| stroke 473 | 26 % → 37 % | 29.4 px | 0.49 | 1.42 | 86 |
| stroke 474 | 31 % → 19 % | 37.3 px | 0.48 | 0.63 | 41 |
| stroke 475 | 39 % → 19 % | 39.5 px | 0.52 | 0.48 | 80 |
| stroke 476 | 45 % → 25 % | 49.4 px | 0.49 | 0.56 | 79 |
| stroke 477 | 36 % → 18 % | 40.0 px | 0.46 | 0.50 | 83 |
| stroke 478 | 31 % → 26 % | 25.5 px | 0.47 | 0.85 | 128 |
| stroke 479 | 46 % → 21 % | 55.1 px | 0.47 | 0.45 | 59 |
| stroke 480 | 53 % → 17 % | 54.1 px | 0.48 | 0.33 | 44 |
| stroke 481 | 36 % → 2 % | 79.2 px | 0.53 | 0.06 | 23 |
| stroke 482 | 30 % → 44 % | 25.8 px | 0.50 | 1.49 | 57 |
| stroke 483 | 37 % → 28 % | 49.4 px | 0.47 | 0.76 | 45 |
| stroke 484 | 41 % → 37 % | 45.9 px | 0.49 | 0.90 | 83 |
| stroke 485 | 29 % → 44 % | 31.8 px | 0.49 | 1.50 | 29 |
| stroke 486 | 5 % → 67 % | 10.5 px | 0.48 | 12.16 | 19 |
| stroke 487 | 10 % → 65 % | 8.9 px | 0.48 | 6.34 | 49 |
| stroke 488 | 6 % → 57 % | 12.1 px | 0.48 | 9.19 | 4 |
| stroke 489 | 10 % → 58 % | 10.1 px | 0.48 | 5.55 | 27 |
| stroke 490 | 13 % → 62 % | 22.8 px | 0.48 | 4.78 | 16 |
| stroke 491 | 16 % → 63 % | 35.8 px | 0.47 | 3.99 | 8 |
| stroke 492 | 20 % → 63 % | 14.8 px | 0.48 | 3.15 | 34 |
| stroke 493 | 8 % → 55 % | 13.1 px | 0.49 | 6.64 | 14 |
| stroke 494 | 17 % → 55 % | 11.0 px | 0.49 | 3.34 | 62 |
| stroke 495 | 7 % → 54 % | 20.3 px | 0.47 | 7.44 | 8 |
| stroke 496 | 9 % → 51 % | 10.5 px | 0.48 | 5.92 | 35 |
| stroke 497 | 9 % → 44 % | 14.8 px | 0.49 | 4.68 | 27 |
| stroke 498 | 10 % → 46 % | 27.1 px | 0.49 | 4.68 | 6 |
| stroke 499 | 14 % → 33 % | 37.1 px | 0.50 | 2.29 | 7 |
| stroke 500 | 15 % → 40 % | 13.4 px | 0.49 | 2.65 | 114 |
| stroke 501 | 21 % → 36 % | 25.8 px | 0.49 | 1.73 | 44 |
| stroke 502 | 15 % → 28 % | 35.3 px | 0.49 | 1.91 | 4 |
| stroke 503 | 19 % → 28 % | 22.0 px | 0.49 | 1.44 | 29 |
| stroke 504 | 14 % → 16 % | 26.8 px | 0.46 | 1.16 | 14 |
| stroke 505 | 14 % → 11 % | 22.8 px | 0.46 | 0.77 | 23 |
| stroke 506 | 18 % → 15 % | 13.6 px | 0.47 | 0.84 | 62 |
| stroke 507 | 21 % → 52 % | 40.6 px | 0.45 | 2.51 | 12 |
| stroke 508 | 33 % → 52 % | 28.6 px | 0.46 | 1.58 | 40 |
| stroke 509 | 8 % → 38 % | 19.2 px | 0.51 | 4.88 | 10 |
| stroke 510 | 10 % → 42 % | 21.1 px | 0.53 | 4.04 | 22 |
| stroke 511 | 20 % → 36 % | 56.1 px | 0.52 | 1.80 | 4 |
| stroke 512 | 19 % → 42 % | 17.6 px | 0.53 | 2.19 | 50 |
| stroke 513 | 24 % → 40 % | 21.8 px | 0.52 | 1.69 | 51 |
| stroke 514 | 7 % → 66 % | 11.1 px | 0.46 | 10.04 | 27 |
| stroke 515 | 7 % → 48 % | 11.1 px | 0.49 | 7.10 | 15 |
| stroke 516 | 13 % → 54 % | 23.0 px | 0.47 | 4.12 | 26 |
| stroke 517 | 11 % → 59 % | 15.8 px | 0.49 | 5.38 | 42 |
| stroke 518 | 18 % → 58 % | 35.8 px | 0.46 | 3.18 | 10 |
| stroke 519 | 12 % → 67 % | 21.4 px | 0.49 | 5.61 | 22 |
| stroke 520 | 26 % → 65 % | 33.4 px | 0.47 | 2.53 | 32 |
| stroke 521 | 17 % → 66 % | 14.1 px | 0.49 | 3.85 | 187 |
| stroke 522 | 28 % → 54 % | 25.9 px | 0.48 | 1.89 | 123 |
| stroke 523 | 40 % → 59 % | 122.1 px | 0.47 | 1.49 | 30 |
| stroke 524 | 24 % → 62 % | 23.0 px | 0.48 | 2.63 | 76 |
| stroke 525 | 27 % → 61 % | 25.3 px | 0.48 | 2.27 | 93 |
| stroke 526 | 23 % → 59 % | 32.9 px | 0.49 | 2.61 | 53 |
| stroke 527 | 22 % → 41 % | 61.9 px | 0.48 | 1.91 | 10 |
| stroke 528 | 24 % → 43 % | 29.2 px | 0.48 | 1.81 | 22 |
| stroke 529 | 8 % → 76 % | 12.4 px | 0.49 | 9.57 | 24 |
| stroke 530 | 16 % → 73 % | 12.2 px | 0.48 | 4.57 | 72 |
| stroke 531 | 7 % → 38 % | 12.0 px | 0.48 | 5.45 | 15 |
| stroke 532 | 13 % → 27 % | 24.7 px | 0.49 | 2.12 | 26 |
| stroke 533 | 14 % → 45 % | 25.0 px | 0.48 | 3.20 | 13 |
| stroke 534 | 17 % → 20 % | 31.8 px | 0.47 | 1.17 | 20 |
| stroke 535 | 17 % → 3 % | 26.3 px | 0.46 | 0.15 | 57 |
| stroke 536 | 24 % → 44 % | 49.4 px | 0.49 | 1.83 | 12 |
| stroke 537 | 24 % → 51 % | 39.9 px | 0.50 | 2.15 | 22 |
| stroke 538 | 26 % → 11 % | 57.1 px | 0.46 | 0.44 | 4 |
| stroke 539 | 27 % → 1 % | 78.3 px | 0.45 | 0.05 | 8 |
| stroke 540 | 20 % → 0 % | 58.1 px | 0.00 | 0.00 | 3 |
| stroke 541 | 24 % → 3 % | 30.1 px | 0.46 | 0.13 | 37 |
| stroke 542 | 34 % → 27 % | 37.7 px | 0.48 | 0.81 | 33 |
| stroke 543 | 39 % → 41 % | 48.8 px | 0.49 | 1.07 | 35 |
| stroke 544 | 30 % → 50 % | 28.4 px | 0.49 | 1.67 | 38 |
| stroke 545 | 39 % → 33 % | 43.3 px | 0.48 | 0.83 | 43 |
| stroke 546 | 31 % → 12 % | 40.3 px | 0.46 | 0.37 | 52 |
| stroke 547 | 7 % → 21 % | 9.0 px | 0.46 | 3.16 | 24 |
| stroke 548 | 18 % → 19 % | 29.1 px | 0.46 | 1.07 | 14 |
| stroke 549 | 5 % → 58 % | 11.1 px | 0.51 | 10.52 | 11 |
| stroke 550 | 9 % → 33 % | 14.3 px | 0.48 | 3.65 | 25 |
| stroke 551 | 20 % → 25 % | 32.4 px | 0.47 | 1.21 | 20 |
| stroke 552 | 19 % → 16 % | 30.9 px | 0.48 | 0.86 | 19 |
| stroke 553 | 29 % → 20 % | 46.5 px | 0.46 | 0.69 | 19 |
| stroke 554 | 25 % → 2 % | 68.8 px | 0.44 | 0.07 | 3 |
| stroke 555 | 18 % → 4 % | 50.5 px | 0.53 | 0.23 | 5 |
| stroke 556 | 42 % → 22 % | 71.4 px | 0.46 | 0.53 | 15 |
| stroke 557 | 23 % → 37 % | 42.7 px | 0.49 | 1.61 | 14 |
| stroke 558 | 29 % → 21 % | 39.6 px | 0.48 | 0.73 | 63 |
| stroke 559 | 33 % → 38 % | 33.3 px | 0.48 | 1.14 | 47 |
| stroke 560 | 40 % → 22 % | 43.8 px | 0.47 | 0.55 | 43 |
| stroke 561 | 37 % → 16 % | 40.6 px | 0.46 | 0.43 | 41 |
| stroke 562 | 35 % → 12 % | 45.5 px | 0.46 | 0.36 | 39 |
| stroke 563 | 39 % → 9 % | 48.8 px | 0.46 | 0.24 | 41 |
| stroke 564 | 22 % → 52 % | 16.2 px | 0.51 | 2.41 | 37 |
| stroke 565 | 6 % → 6 % | 9.3 px | 0.52 | 0.93 | 21 |
| stroke 566 | 9 % → 0 % | 19.0 px | 0.00 | 0.00 | 6 |
| stroke 567 | 21 % → 11 % | 32.5 px | 0.46 | 0.51 | 30 |
| stroke 568 | 5 % → 26 % | 12.6 px | 0.53 | 4.82 | 4 |
| stroke 569 | 12 % → 23 % | 28.7 px | 0.46 | 2.00 | 4 |
| stroke 570 | 18 % → 0 % | 39.0 px | 0.00 | 0.00 | 10 |
| stroke 571 | 21 % → 28 % | 49.5 px | 0.46 | 1.32 | 10 |
| stroke 572 | 14 % → 0 % | 27.9 px | 0.00 | 0.00 | 8 |
| stroke 573 | 19 % → 2 % | 21.8 px | 0.52 | 0.13 | 46 |
| stroke 574 | 32 % → 6 % | 48.0 px | 0.46 | 0.19 | 33 |
| stroke 575 | 33 % → 24 % | 36.3 px | 0.47 | 0.72 | 40 |
| stroke 576 | 31 % → 20 % | 32.7 px | 0.47 | 0.63 | 42 |
| stroke 577 | 34 % → 6 % | 41.6 px | 0.52 | 0.17 | 36 |
| stroke 578 | 33 % → 2 % | 68.9 px | 0.52 | 0.07 | 15 |
| stroke 579 | 25 % → 21 % | 19.4 px | 0.53 | 0.85 | 41 |
| stroke 580 | 24 % → 0 % | 16.3 px | 0.00 | 0.00 | 48 |
| stroke 581 | 11 % → 54 % | 27.7 px | 0.48 | 4.98 | 5 |
| stroke 582 | 8 % → 52 % | 17.7 px | 0.50 | 6.36 | 5 |
| stroke 583 | 23 % → 61 % | 61.1 px | 0.46 | 2.72 | 6 |
| stroke 584 | 12 % → 56 % | 15.4 px | 0.50 | 4.67 | 16 |
| stroke 585 | 18 % → 64 % | 44.0 px | 0.48 | 3.53 | 5 |
| stroke 586 | 19 % → 54 % | 47.9 px | 0.49 | 2.90 | 4 |
| stroke 587 | 26 % → 60 % | 26.1 px | 0.49 | 2.31 | 55 |
| stroke 588 | 35 % → 56 % | 35.5 px | 0.49 | 1.61 | 55 |
| stroke 589 | 27 % → 56 % | 25.1 px | 0.50 | 2.11 | 44 |
| stroke 590 | 31 % → 55 % | 38.6 px | 0.50 | 1.78 | 39 |
| stroke 591 | 14 % → 67 % | 37.3 px | 0.50 | 4.89 | 4 |
| stroke 592 | 18 % → 70 % | 19.3 px | 0.50 | 3.91 | 18 |
| stroke 593 | 6 % → 19 % | 11.0 px | 0.52 | 3.25 | 9 |
| stroke 594 | 10 % → 18 % | 8.6 px | 0.52 | 1.80 | 36 |
| stroke 595 | 9 % → 62 % | 9.7 px | 0.50 | 7.24 | 20 |
| stroke 596 | 8 % → 49 % | 8.3 px | 0.49 | 6.40 | 29 |
| stroke 597 | 10 % → 53 % | 10.0 px | 0.52 | 5.20 | 33 |
| stroke 598 | 4 % → 50 % | 10.4 px | 0.46 | 12.78 | 3 |
| stroke 599 | 8 % → 58 % | 8.3 px | 0.50 | 7.08 | 24 |
| stroke 600 | 7 % → 58 % | 8.8 px | 0.49 | 7.83 | 36 |
| stroke 601 | 6 % → 39 % | 8.5 px | 0.52 | 6.10 | 37 |
| stroke 602 | 8 % → 61 % | 10.8 px | 0.49 | 7.54 | 40 |
| stroke 603 | 6 % → 38 % | 9.0 px | 0.47 | 6.66 | 25 |
| stroke 604 | 6 % → 50 % | 9.4 px | 0.47 | 7.74 | 24 |
| stroke 605 | 16 % → 49 % | 16.7 px | 0.49 | 3.08 | 58 |
| stroke 606 | 6 % → 56 % | 9.3 px | 0.46 | 8.74 | 20 |
| stroke 607 | 9 % → 55 % | 9.9 px | 0.50 | 6.44 | 26 |
| stroke 608 | 17 % → 63 % | 41.3 px | 0.50 | 3.67 | 4 |
| stroke 609 | 6 % → 56 % | 9.6 px | 0.51 | 8.73 | 32 |
| stroke 610 | 5 % → 26 % | 13.1 px | 0.47 | 4.90 | 13 |
| stroke 611 | 6 % → 63 % | 9.5 px | 0.49 | 10.04 | 16 |
| stroke 612 | 10 % → 59 % | 12.8 px | 0.52 | 5.75 | 24 |
| stroke 613 | 7 % → 55 % | 10.3 px | 0.49 | 8.36 | 26 |
| stroke 614 | 7 % → 60 % | 8.6 px | 0.52 | 8.77 | 42 |
| stroke 615 | 8 % → 60 % | 11.0 px | 0.42 | 7.18 | 21 |
| stroke 616 | 12 % → 58 % | 18.0 px | 0.51 | 5.03 | 34 |
| stroke 617 | 10 % → 43 % | 13.9 px | 0.52 | 4.48 | 39 |
| stroke 618 | 6 % → 43 % | 9.6 px | 0.52 | 7.05 | 31 |
| stroke 619 | 8 % → 43 % | 12.9 px | 0.51 | 5.33 | 24 |
| stroke 620 | 8 % → 34 % | 11.5 px | 0.52 | 4.12 | 38 |
| stroke 621 | 7 % → 47 % | 9.7 px | 0.48 | 7.16 | 35 |
| stroke 622 | 16 % → 47 % | 22.0 px | 0.52 | 2.97 | 28 |
| stroke 623 | 10 % → 46 % | 22.6 px | 0.49 | 4.69 | 5 |
| stroke 624 | 10 % → 43 % | 10.5 px | 0.52 | 4.45 | 37 |
| stroke 625 | 13 % → 55 % | 20.7 px | 0.51 | 4.21 | 35 |
| stroke 626 | 11 % → 57 % | 16.8 px | 0.45 | 5.16 | 26 |
| stroke 627 | 14 % → 52 % | 13.8 px | 0.49 | 3.63 | 22 |
| stroke 628 | 6 % → 59 % | 8.7 px | 0.49 | 9.57 | 21 |
| stroke 629 | 9 % → 53 % | 14.5 px | 0.46 | 6.12 | 10 |
| stroke 630 | 16 % → 34 % | 23.9 px | 0.53 | 2.13 | 51 |
| stroke 631 | 6 % → 25 % | 10.7 px | 0.48 | 4.30 | 11 |
| stroke 632 | 7 % → 50 % | 9.5 px | 0.50 | 7.41 | 32 |
| stroke 633 | 14 % → 44 % | 18.8 px | 0.50 | 3.15 | 16 |
| stroke 634 | 12 % → 54 % | 15.8 px | 0.51 | 4.36 | 29 |
| stroke 635 | 9 % → 35 % | 10.2 px | 0.51 | 4.01 | 39 |
| stroke 636 | 7 % → 44 % | 8.8 px | 0.48 | 6.24 | 19 |
| stroke 637 | 11 % → 45 % | 14.2 px | 0.51 | 4.11 | 33 |
| stroke 638 | 6 % → 56 % | 9.5 px | 0.48 | 8.73 | 25 |
| stroke 639 | 9 % → 52 % | 12.2 px | 0.48 | 5.71 | 32 |
| stroke 640 | 11 % → 44 % | 16.8 px | 0.49 | 4.16 | 27 |
| stroke 641 | 11 % → 49 % | 9.5 px | 0.52 | 4.41 | 27 |
| stroke 642 | 23 % → 50 % | 36.4 px | 0.52 | 2.14 | 18 |
| stroke 643 | 5 % → 66 % | 10.0 px | 0.46 | 13.02 | 5 |
| stroke 644 | 27 % → 53 % | 70.4 px | 0.48 | 1.95 | 12 |
| stroke 645 | 11 % → 55 % | 17.8 px | 0.50 | 4.84 | 84 |
| stroke 646 | 16 % → 57 % | 20.4 px | 0.44 | 3.59 | 23 |
| stroke 647 | 7 % → 56 % | 8.7 px | 0.49 | 8.18 | 37 |
| stroke 648 | 12 % → 51 % | 16.0 px | 0.48 | 4.13 | 32 |
| stroke 649 | 10 % → 45 % | 14.5 px | 0.50 | 4.65 | 33 |
| stroke 650 | 7 % → 31 % | 10.1 px | 0.48 | 4.54 | 21 |
| stroke 651 | 14 % → 51 % | 18.6 px | 0.47 | 3.56 | 26 |
| stroke 652 | 16 % → 52 % | 23.6 px | 0.50 | 3.27 | 26 |
| stroke 653 | 10 % → 61 % | 10.4 px | 0.47 | 6.15 | 51 |
| stroke 654 | 9 % → 57 % | 8.7 px | 0.50 | 6.28 | 26 |
| stroke 655 | 8 % → 40 % | 9.3 px | 0.48 | 5.19 | 29 |
| stroke 656 | 19 % → 50 % | 20.9 px | 0.47 | 2.65 | 22 |
| stroke 657 | 15 % → 50 % | 20.8 px | 0.48 | 3.41 | 16 |
| stroke 658 | 11 % → 57 % | 10.4 px | 0.53 | 5.08 | 30 |
| stroke 659 | 14 % → 42 % | 19.2 px | 0.52 | 2.98 | 16 |
| stroke 660 | 10 % → 42 % | 16.7 px | 0.45 | 4.02 | 13 |
| stroke 661 | 23 % → 52 % | 36.4 px | 0.52 | 2.30 | 25 |
| stroke 662 | 12 % → 59 % | 19.5 px | 0.49 | 4.82 | 17 |
| stroke 663 | 15 % → 52 % | 20.5 px | 0.50 | 3.49 | 50 |
| stroke 664 | 16 % → 60 % | 21.9 px | 0.49 | 3.79 | 23 |
| stroke 665 | 16 % → 58 % | 25.2 px | 0.52 | 3.61 | 25 |
| stroke 666 | 7 % → 46 % | 9.4 px | 0.48 | 6.74 | 24 |
| stroke 667 | 13 % → 62 % | 21.5 px | 0.46 | 4.91 | 19 |
| stroke 668 | 7 % → 59 % | 8.9 px | 0.48 | 8.45 | 37 |
| stroke 669 | 21 % → 46 % | 31.4 px | 0.50 | 2.23 | 25 |
| stroke 670 | 9 % → 40 % | 10.5 px | 0.48 | 4.66 | 23 |
| stroke 671 | 8 % → 50 % | 9.7 px | 0.50 | 6.43 | 6 |
| stroke 672 | 12 % → 50 % | 18.6 px | 0.47 | 4.30 | 11 |
| stroke 673 | 20 % → 52 % | 24.2 px | 0.45 | 2.59 | 20 |
| stroke 674 | 15 % → 59 % | 22.4 px | 0.48 | 3.85 | 14 |
| stroke 675 | 6 % → 44 % | 8.8 px | 0.46 | 7.37 | 39 |
| stroke 676 | 18 % → 46 % | 27.0 px | 0.49 | 2.49 | 44 |
| stroke 677 | 13 % → 55 % | 19.7 px | 0.47 | 4.22 | 22 |
| stroke 678 | 11 % → 65 % | 17.2 px | 0.52 | 5.66 | 24 |
| stroke 679 | 14 % → 36 % | 21.4 px | 0.49 | 2.60 | 33 |
| stroke 680 | 16 % → 53 % | 9.5 px | 0.52 | 3.39 | 19 |
| stroke 681 | 15 % → 57 % | 18.9 px | 0.52 | 3.91 | 35 |
| stroke 682 | 13 % → 39 % | 13.6 px | 0.50 | 3.09 | 28 |
| stroke 683 | 12 % → 44 % | 16.4 px | 0.50 | 3.54 | 15 |
| stroke 684 | 5 % → 50 % | 10.2 px | 0.49 | 10.76 | 7 |
| stroke 685 | 19 % → 52 % | 24.7 px | 0.49 | 2.78 | 19 |
| stroke 686 | 10 % → 50 % | 13.1 px | 0.50 | 5.00 | 27 |
| stroke 687 | 17 % → 36 % | 34.2 px | 0.49 | 2.07 | 11 |
| stroke 688 | 9 % → 51 % | 10.7 px | 0.48 | 5.75 | 16 |
| stroke 689 | 13 % → 53 % | 20.1 px | 0.47 | 4.18 | 42 |
| stroke 690 | 17 % → 53 % | 17.5 px | 0.46 | 3.18 | 28 |
| stroke 691 | 22 % → 47 % | 34.7 px | 0.49 | 2.16 | 19 |
| stroke 692 | 21 % → 38 % | 19.6 px | 0.52 | 1.77 | 125 |
| stroke 693 | 19 % → 56 % | 19.1 px | 0.52 | 2.89 | 44 |
| stroke 694 | 33 % → 58 % | 52.8 px | 0.51 | 1.74 | 21 |
| stroke 695 | 13 % → 54 % | 18.4 px | 0.48 | 4.26 | 42 |
| stroke 696 | 23 % → 56 % | 61.8 px | 0.52 | 2.44 | 4 |
| stroke 697 | 24 % → 54 % | 30.9 px | 0.52 | 2.30 | 24 |
| stroke 698 | 12 % → 51 % | 18.2 px | 0.50 | 4.11 | 34 |
| stroke 699 | 26 % → 66 % | 24.9 px | 0.48 | 2.55 | 45 |
| stroke 700 | 15 % → 60 % | 16.9 px | 0.47 | 4.02 | 33 |
| stroke 701 | 14 % → 61 % | 36.3 px | 0.46 | 4.31 | 6 |
| stroke 702 | 19 % → 59 % | 44.8 px | 0.48 | 3.20 | 8 |
| stroke 703 | 20 % → 56 % | 28.7 px | 0.46 | 2.79 | 28 |
| stroke 704 | 22 % → 61 % | 32.5 px | 0.52 | 2.71 | 18 |
| stroke 705 | 21 % → 56 % | 24.1 px | 0.51 | 2.61 | 23 |
| stroke 706 | 17 % → 44 % | 17.6 px | 0.51 | 2.56 | 25 |
| stroke 707 | 31 % → 41 % | 45.5 px | 0.53 | 1.34 | 10 |
| stroke 708 | 16 % → 52 % | 24.8 px | 0.48 | 3.20 | 16 |
| stroke 709 | 13 % → 40 % | 20.3 px | 0.48 | 3.15 | 35 |
| stroke 710 | 28 % → 51 % | 34.5 px | 0.51 | 1.82 | 19 |
| stroke 711 | 24 % → 61 % | 37.7 px | 0.50 | 2.52 | 22 |
| stroke 712 | 24 % → 46 % | 31.1 px | 0.50 | 1.96 | 27 |
| stroke 713 | 16 % → 69 % | 29.7 px | 0.48 | 4.46 | 4 |
| stroke 714 | 18 % → 53 % | 27.3 px | 0.50 | 2.90 | 29 |
| stroke 715 | 9 % → 32 % | 13.5 px | 0.46 | 3.39 | 20 |
| stroke 716 | 18 % → 46 % | 50.3 px | 0.47 | 2.59 | 10 |
| stroke 717 | 16 % → 39 % | 18.6 px | 0.51 | 2.53 | 25 |
| stroke 718 | 17 % → 44 % | 25.5 px | 0.53 | 2.64 | 9 |
| stroke 719 | 6 % → 33 % | 16.5 px | 0.45 | 5.14 | 10 |
| stroke 720 | 12 % → 43 % | 15.2 px | 0.47 | 3.67 | 10 |
| stroke 721 | 13 % → 53 % | 19.1 px | 0.49 | 4.01 | 25 |
| stroke 722 | 22 % → 48 % | 23.1 px | 0.50 | 2.16 | 26 |
| stroke 723 | 20 % → 53 % | 30.6 px | 0.50 | 2.60 | 17 |
| stroke 724 | 28 % → 52 % | 36.8 px | 0.53 | 1.86 | 15 |
| stroke 725 | 12 % → 47 % | 19.3 px | 0.51 | 3.91 | 21 |
| stroke 726 | 8 % → 54 % | 10.9 px | 0.50 | 6.78 | 25 |
| stroke 727 | 23 % → 53 % | 27.9 px | 0.51 | 2.33 | 21 |
| stroke 728 | 23 % → 56 % | 40.8 px | 0.45 | 2.43 | 16 |
| stroke 729 | 16 % → 68 % | 26.6 px | 0.49 | 4.33 | 6 |
| stroke 730 | 33 % → 57 % | 34.5 px | 0.53 | 1.75 | 42 |
| stroke 731 | 20 % → 52 % | 35.6 px | 0.51 | 2.61 | 7 |
| stroke 732 | 19 % → 60 % | 29.6 px | 0.50 | 3.24 | 19 |
| stroke 733 | 19 % → 49 % | 21.3 px | 0.50 | 2.51 | 24 |
| stroke 734 | 29 % → 55 % | 47.5 px | 0.49 | 1.87 | 19 |
| stroke 735 | 20 % → 48 % | 30.0 px | 0.48 | 2.43 | 20 |
| stroke 736 | 4 % → 46 % | 9.9 px | 0.45 | 11.62 | 3 |
| stroke 737 | 29 % → 43 % | 44.9 px | 0.52 | 1.52 | 21 |
| stroke 738 | 16 % → 48 % | 27.1 px | 0.49 | 2.99 | 11 |
| stroke 739 | 18 % → 50 % | 27.9 px | 0.50 | 2.70 | 29 |
| stroke 740 | 20 % → 49 % | 37.6 px | 0.49 | 2.41 | 10 |
| stroke 741 | 24 % → 65 % | 38.3 px | 0.48 | 2.71 | 20 |
| stroke 742 | 20 % → 57 % | 32.2 px | 0.48 | 2.90 | 14 |
| stroke 743 | 7 % → 58 % | 9.3 px | 0.47 | 8.62 | 12 |
| stroke 744 | 31 % → 54 % | 41.8 px | 0.51 | 1.76 | 20 |
| stroke 745 | 22 % → 61 % | 31.1 px | 0.49 | 2.73 | 43 |
| stroke 746 | 26 % → 55 % | 41.4 px | 0.51 | 2.09 | 25 |
| stroke 747 | 14 % → 52 % | 17.8 px | 0.49 | 3.60 | 34 |
| stroke 748 | 10 % → 60 % | 25.5 px | 0.46 | 6.17 | 4 |
| stroke 749 | 21 % → 60 % | 25.2 px | 0.48 | 2.89 | 20 |
| stroke 750 | 32 % → 47 % | 46.9 px | 0.49 | 1.49 | 21 |
| stroke 751 | 20 % → 48 % | 32.0 px | 0.48 | 2.43 | 27 |
| stroke 752 | 20 % → 49 % | 31.0 px | 0.50 | 2.47 | 38 |
| stroke 753 | 19 % → 55 % | 13.8 px | 0.53 | 2.93 | 63 |
| stroke 754 | 14 % → 48 % | 37.9 px | 0.46 | 3.56 | 10 |
| stroke 755 | 31 % → 56 % | 56.1 px | 0.47 | 1.82 | 28 |
| stroke 756 | 13 % → 45 % | 25.7 px | 0.46 | 3.48 | 12 |
| stroke 757 | 33 % → 43 % | 56.8 px | 0.50 | 1.33 | 8 |
| stroke 758 | 15 % → 44 % | 25.0 px | 0.51 | 3.00 | 62 |
| stroke 759 | 21 % → 48 % | 21.9 px | 0.52 | 2.23 | 45 |
| stroke 760 | 22 % → 51 % | 35.6 px | 0.49 | 2.30 | 39 |
| stroke 761 | 19 % → 57 % | 47.1 px | 0.48 | 2.95 | 16 |
| stroke 762 | 36 % → 53 % | 47.9 px | 0.49 | 1.48 | 41 |
| stroke 763 | 10 % → 40 % | 13.8 px | 0.51 | 3.99 | 50 |
| stroke 764 | 41 % → 69 % | 71.5 px | 0.52 | 1.67 | 19 |
| stroke 765 | 9 % → 34 % | 11.1 px | 0.51 | 3.97 | 33 |
| stroke 766 | 16 % → 51 % | 24.3 px | 0.47 | 3.28 | 45 |
| stroke 767 | 17 % → 53 % | 26.0 px | 0.48 | 3.09 | 39 |
| stroke 768 | 30 % → 52 % | 36.1 px | 0.52 | 1.72 | 26 |
| stroke 769 | 15 % → 48 % | 21.9 px | 0.47 | 3.16 | 35 |
| stroke 770 | 34 % → 54 % | 43.8 px | 0.47 | 1.60 | 23 |
| stroke 771 | 19 % → 45 % | 22.7 px | 0.49 | 2.34 | 55 |
| stroke 772 | 29 % → 49 % | 50.7 px | 0.51 | 1.68 | 17 |
| stroke 773 | 14 % → 39 % | 29.1 px | 0.53 | 2.74 | 15 |
| stroke 774 | 14 % → 56 % | 24.3 px | 0.49 | 3.88 | 29 |
| stroke 775 | 13 % → 43 % | 22.1 px | 0.47 | 3.34 | 15 |
| stroke 776 | 18 % → 47 % | 29.6 px | 0.50 | 2.58 | 21 |
| stroke 777 | 24 % → 62 % | 36.7 px | 0.51 | 2.55 | 24 |
| stroke 778 | 31 % → 58 % | 48.4 px | 0.50 | 1.89 | 24 |
| stroke 779 | 17 % → 60 % | 21.2 px | 0.52 | 3.56 | 16 |
| stroke 780 | 26 % → 54 % | 38.8 px | 0.52 | 2.11 | 19 |
| stroke 781 | 22 % → 64 % | 36.5 px | 0.47 | 2.93 | 10 |
| stroke 782 | 42 % → 53 % | 26.6 px | 0.52 | 1.28 | 25 |
| stroke 783 | 32 % → 59 % | 49.4 px | 0.48 | 1.82 | 18 |
| stroke 784 | 35 % → 60 % | 54.9 px | 0.50 | 1.70 | 24 |
| stroke 785 | 29 % → 43 % | 45.9 px | 0.49 | 1.46 | 16 |
| stroke 786 | 14 % → 38 % | 18.8 px | 0.50 | 2.73 | 16 |
| stroke 787 | 27 % → 61 % | 19.8 px | 0.52 | 2.29 | 21 |
| stroke 788 | 9 % → 57 % | 17.3 px | 0.47 | 6.10 | 15 |
| stroke 789 | 21 % → 55 % | 38.1 px | 0.46 | 2.58 | 12 |
| stroke 790 | 10 % → 51 % | 15.8 px | 0.46 | 5.15 | 24 |
| stroke 791 | 29 % → 46 % | 35.6 px | 0.52 | 1.62 | 42 |
| stroke 792 | 35 % → 64 % | 63.4 px | 0.52 | 1.83 | 7 |
| stroke 793 | 28 % → 51 % | 36.3 px | 0.50 | 1.82 | 41 |
| stroke 794 | 28 % → 57 % | 39.6 px | 0.48 | 2.06 | 42 |
| stroke 795 | 12 % → 51 % | 28.1 px | 0.46 | 4.19 | 5 |
| stroke 796 | 23 % → 57 % | 31.8 px | 0.50 | 2.50 | 45 |
| stroke 797 | 17 % → 38 % | 25.7 px | 0.50 | 2.26 | 7 |
| stroke 798 | 27 % → 49 % | 42.0 px | 0.49 | 1.81 | 24 |
| stroke 799 | 34 % → 66 % | 86.9 px | 0.52 | 1.95 | 5 |
| stroke 800 | 40 % → 67 % | 76.2 px | 0.53 | 1.69 | 15 |
| stroke 801 | 23 % → 51 % | 43.4 px | 0.48 | 2.18 | 12 |
| stroke 802 | 16 % → 46 % | 11.0 px | 0.53 | 2.91 | 35 |
| stroke 803 | 29 % → 55 % | 31.1 px | 0.52 | 1.89 | 22 |
| stroke 804 | 34 % → 61 % | 66.3 px | 0.50 | 1.78 | 7 |
| stroke 805 | 22 % → 61 % | 29.0 px | 0.48 | 2.84 | 23 |
| stroke 806 | 39 % → 60 % | 64.2 px | 0.52 | 1.54 | 17 |
| stroke 807 | 14 % → 50 % | 34.9 px | 0.47 | 3.45 | 13 |
| stroke 808 | 21 % → 54 % | 30.7 px | 0.48 | 2.61 | 10 |
| stroke 809 | 11 % → 41 % | 19.8 px | 0.45 | 3.73 | 16 |
| stroke 810 | 36 % → 59 % | 79.9 px | 0.49 | 1.66 | 13 |
| stroke 811 | 43 % → 63 % | 119.7 px | 0.49 | 1.47 | 3 |
| stroke 812 | 24 % → 39 % | 32.7 px | 0.49 | 1.60 | 11 |
| stroke 813 | 35 % → 52 % | 52.5 px | 0.51 | 1.49 | 14 |
| stroke 814 | 17 % → 51 % | 27.4 px | 0.46 | 3.05 | 25 |
| stroke 815 | 34 % → 63 % | 62.0 px | 0.48 | 1.88 | 11 |
| stroke 816 | 33 % → 65 % | 94.0 px | 0.49 | 1.94 | 9 |
| stroke 817 | 28 % → 43 % | 47.7 px | 0.51 | 1.52 | 26 |
| stroke 818 | 40 % → 61 % | 65.5 px | 0.50 | 1.52 | 25 |
| stroke 819 | 21 % → 41 % | 25.8 px | 0.51 | 1.92 | 30 |
| stroke 820 | 34 % → 58 % | 34.9 px | 0.47 | 1.71 | 34 |
| stroke 821 | 32 % → 55 % | 40.6 px | 0.51 | 1.72 | 11 |
| stroke 822 | 37 % → 60 % | 51.2 px | 0.48 | 1.62 | 24 |
| stroke 823 | 12 % → 41 % | 16.7 px | 0.47 | 3.44 | 38 |
| stroke 824 | 27 % → 53 % | 75.9 px | 0.47 | 1.95 | 12 |
| stroke 825 | 18 % → 39 % | 38.2 px | 0.52 | 2.19 | 12 |
| stroke 826 | 26 % → 60 % | 46.2 px | 0.47 | 2.36 | 12 |
| stroke 827 | 28 % → 59 % | 50.3 px | 0.51 | 2.08 | 7 |
| stroke 828 | 19 % → 53 % | 44.8 px | 0.46 | 2.77 | 8 |
| stroke 829 | 8 % → 45 % | 16.1 px | 0.46 | 5.57 | 11 |
| stroke 830 | 18 % → 41 % | 51.9 px | 0.46 | 2.24 | 6 |
| stroke 831 | 17 % → 35 % | 42.7 px | 0.52 | 2.09 | 6 |
| stroke 832 | 49 % → 54 % | 85.2 px | 0.53 | 1.10 | 8 |
| stroke 833 | 31 % → 51 % | 47.6 px | 0.47 | 1.64 | 46 |
| stroke 834 | 23 % → 54 % | 31.2 px | 0.47 | 2.40 | 38 |
| stroke 835 | 16 % → 62 % | 16.9 px | 0.50 | 3.90 | 21 |
| stroke 836 | 46 % → 60 % | 61.5 px | 0.53 | 1.32 | 5 |
| stroke 837 | 31 % → 52 % | 60.9 px | 0.51 | 1.67 | 19 |
| stroke 838 | 41 % → 55 % | 43.6 px | 0.50 | 1.34 | 22 |
| stroke 839 | 24 % → 52 % | 36.0 px | 0.47 | 2.12 | 19 |
| stroke 840 | 28 % → 59 % | 67.9 px | 0.50 | 2.12 | 4 |
| stroke 841 | 46 % → 57 % | 66.0 px | 0.52 | 1.23 | 27 |
| stroke 842 | 31 % → 49 % | 41.1 px | 0.49 | 1.61 | 15 |
| stroke 843 | 37 % → 59 % | 67.0 px | 0.40 | 1.60 | 20 |
| stroke 844 | 34 % → 53 % | 61.7 px | 0.46 | 1.56 | 20 |
| stroke 845 | 28 % → 49 % | 35.2 px | 0.49 | 1.75 | 23 |
| stroke 846 | 20 % → 58 % | 54.4 px | 0.49 | 2.83 | 3 |
| stroke 847 | 19 % → 63 % | 40.4 px | 0.49 | 3.39 | 14 |
| stroke 848 | 39 % → 60 % | 72.4 px | 0.51 | 1.55 | 14 |
| stroke 849 | 56 % → 57 % | 106.2 px | 0.52 | 1.02 | 9 |
| stroke 850 | 22 % → 53 % | 45.7 px | 0.47 | 2.37 | 8 |
| stroke 851 | 42 % → 50 % | 83.9 px | 0.51 | 1.18 | 13 |
| stroke 852 | 42 % → 54 % | 104.4 px | 0.48 | 1.28 | 9 |
| stroke 853 | 28 % → 44 % | 28.4 px | 0.53 | 1.59 | 31 |
| stroke 854 | 34 % → 52 % | 54.2 px | 0.47 | 1.54 | 29 |
| stroke 855 | 51 % → 64 % | 99.5 px | 0.53 | 1.24 | 10 |
| stroke 856 | 47 % → 58 % | 59.7 px | 0.50 | 1.24 | 102 |
| stroke 857 | 40 % → 54 % | 78.7 px | 0.53 | 1.35 | 10 |
| stroke 858 | 42 % → 62 % | 45.2 px | 0.52 | 1.47 | 45 |
| stroke 859 | 31 % → 55 % | 45.4 px | 0.46 | 1.77 | 27 |
| stroke 860 | 33 % → 57 % | 43.6 px | 0.51 | 1.71 | 15 |
| stroke 861 | 37 % → 56 % | 41.8 px | 0.50 | 1.51 | 17 |
| stroke 862 | 19 % → 42 % | 38.5 px | 0.46 | 2.24 | 10 |
| stroke 863 | 27 % → 51 % | 59.6 px | 0.48 | 1.91 | 6 |
| stroke 864 | 50 % → 69 % | 53.2 px | 0.48 | 1.39 | 32 |
| stroke 865 | 39 % → 64 % | 64.9 px | 0.48 | 1.63 | 45 |
| stroke 866 | 38 % → 58 % | 97.1 px | 0.47 | 1.54 | 3 |
| stroke 867 | 28 % → 63 % | 46.3 px | 0.47 | 2.21 | 28 |
| stroke 868 | 24 % → 58 % | 31.9 px | 0.47 | 2.37 | 34 |
| stroke 869 | 29 % → 43 % | 39.1 px | 0.51 | 1.46 | 18 |
| stroke 870 | 22 % → 51 % | 40.1 px | 0.52 | 2.35 | 26 |
| stroke 871 | 9 % → 45 % | 14.6 px | 0.46 | 5.30 | 12 |
| stroke 872 | 23 % → 47 % | 39.5 px | 0.47 | 2.09 | 10 |
| stroke 873 | 35 % → 50 % | 49.6 px | 0.49 | 1.44 | 21 |
| stroke 874 | 28 % → 45 % | 36.8 px | 0.50 | 1.62 | 17 |
| stroke 875 | 25 % → 43 % | 35.0 px | 0.50 | 1.74 | 13 |
| stroke 876 | 19 % → 49 % | 30.3 px | 0.47 | 2.64 | 23 |
| stroke 877 | 36 % → 52 % | 73.6 px | 0.50 | 1.45 | 12 |
| stroke 878 | 29 % → 54 % | 39.9 px | 0.48 | 1.85 | 8 |
| stroke 879 | 46 % → 64 % | 62.4 px | 0.49 | 1.38 | 33 |
| stroke 880 | 49 % → 55 % | 79.8 px | 0.52 | 1.11 | 16 |
| stroke 881 | 30 % → 43 % | 43.9 px | 0.49 | 1.44 | 27 |
| stroke 882 | 39 % → 59 % | 109.5 px | 0.51 | 1.53 | 5 |
| stroke 883 | 39 % → 62 % | 75.2 px | 0.48 | 1.57 | 14 |
| stroke 884 | 26 % → 60 % | 24.3 px | 0.53 | 2.27 | 11 |
| stroke 885 | 30 % → 64 % | 59.8 px | 0.48 | 2.14 | 5 |
| stroke 886 | 34 % → 46 % | 54.6 px | 0.49 | 1.37 | 14 |
| stroke 887 | 35 % → 59 % | 83.8 px | 0.49 | 1.66 | 7 |
| stroke 888 | 37 % → 59 % | 55.0 px | 0.51 | 1.60 | 33 |
| stroke 889 | 22 % → 40 % | 35.9 px | 0.52 | 1.82 | 24 |
| stroke 890 | 22 % → 41 % | 37.2 px | 0.49 | 1.90 | 16 |
| stroke 891 | 31 % → 44 % | 65.8 px | 0.49 | 1.44 | 11 |
| stroke 892 | 15 % → 49 % | 28.9 px | 0.46 | 3.20 | 5 |
| stroke 893 | 38 % → 59 % | 73.3 px | 0.51 | 1.56 | 15 |
| stroke 894 | 45 % → 57 % | 57.9 px | 0.51 | 1.25 | 10 |
| stroke 895 | 32 % → 54 % | 69.8 px | 0.46 | 1.69 | 5 |
| stroke 896 | 27 % → 56 % | 50.9 px | 0.45 | 2.10 | 12 |
| stroke 897 | 46 % → 63 % | 86.4 px | 0.52 | 1.38 | 7 |
| stroke 898 | 26 % → 54 % | 43.7 px | 0.53 | 2.08 | 6 |
| stroke 899 | 36 % → 49 % | 41.4 px | 0.50 | 1.36 | 22 |
| stroke 900 | 28 % → 61 % | 68.6 px | 0.49 | 2.13 | 23 |
| stroke 901 | 40 % → 57 % | 73.0 px | 0.50 | 1.44 | 8 |
| stroke 902 | 25 % → 64 % | 52.0 px | 0.47 | 2.61 | 7 |
| stroke 903 | 20 % → 42 % | 28.6 px | 0.48 | 2.04 | 17 |
| stroke 904 | 28 % → 47 % | 43.7 px | 0.51 | 1.67 | 47 |
| stroke 905 | 16 % → 46 % | 23.0 px | 0.46 | 2.95 | 17 |
| stroke 906 | 24 % → 61 % | 60.1 px | 0.46 | 2.58 | 3 |
| stroke 907 | 39 % → 50 % | 59.7 px | 0.49 | 1.29 | 8 |
| stroke 908 | 38 % → 60 % | 68.4 px | 0.47 | 1.58 | 21 |
| stroke 909 | 39 % → 48 % | 58.4 px | 0.49 | 1.23 | 18 |
| stroke 910 | 36 % → 48 % | 44.7 px | 0.49 | 1.35 | 18 |
| stroke 911 | 8 % → 28 % | 21.9 px | 0.46 | 3.63 | 4 |
| stroke 912 | 34 % → 59 % | 67.5 px | 0.48 | 1.75 | 11 |
| stroke 913 | 26 % → 50 % | 42.4 px | 0.49 | 1.91 | 17 |
| stroke 914 | 20 % → 50 % | 32.2 px | 0.46 | 2.46 | 16 |
| stroke 915 | 43 % → 57 % | 116.5 px | 0.52 | 1.32 | 3 |
| stroke 916 | 34 % → 56 % | 70.2 px | 0.50 | 1.66 | 9 |
| stroke 917 | 17 % → 45 % | 28.1 px | 0.48 | 2.68 | 33 |
| stroke 918 | 31 % → 50 % | 88.2 px | 0.43 | 1.57 | 14 |
| stroke 919 | 20 % → 45 % | 31.3 px | 0.48 | 2.31 | 22 |
| stroke 920 | 32 % → 57 % | 57.1 px | 0.52 | 1.80 | 11 |
| stroke 921 | 36 % → 53 % | 51.3 px | 0.51 | 1.47 | 10 |
| stroke 922 | 15 % → 33 % | 34.0 px | 0.48 | 2.27 | 4 |
| stroke 923 | 28 % → 51 % | 47.4 px | 0.47 | 1.80 | 11 |
| stroke 924 | 9 % → 32 % | 18.1 px | 0.46 | 3.43 | 15 |
| stroke 925 | 30 % → 45 % | 53.0 px | 0.50 | 1.51 | 11 |
| stroke 926 | 42 % → 53 % | 89.0 px | 0.48 | 1.28 | 10 |
| stroke 927 | 27 % → 44 % | 73.7 px | 0.43 | 1.65 | 7 |
| stroke 928 | 35 % → 56 % | 53.6 px | 0.51 | 1.60 | 25 |
| stroke 929 | 48 % → 61 % | 69.8 px | 0.53 | 1.27 | 9 |
| stroke 930 | 50 % → 61 % | 66.6 px | 0.48 | 1.22 | 15 |
| stroke 931 | 23 % → 38 % | 60.9 px | 0.49 | 1.65 | 4 |
| stroke 932 | 53 % → 59 % | 142.1 px | 0.52 | 1.12 | 8 |
| stroke 933 | 31 % → 57 % | 55.3 px | 0.47 | 1.87 | 8 |
| stroke 934 | 33 % → 58 % | 53.5 px | 0.50 | 1.79 | 15 |
| stroke 935 | 26 % → 43 % | 45.8 px | 0.53 | 1.63 | 11 |
| stroke 936 | 38 % → 59 % | 50.2 px | 0.47 | 1.55 | 18 |
| stroke 937 | 45 % → 64 % | 78.2 px | 0.51 | 1.40 | 9 |
| stroke 938 | 43 % → 63 % | 95.2 px | 0.48 | 1.46 | 13 |
| stroke 939 | 28 % → 39 % | 61.2 px | 0.52 | 1.41 | 4 |
| stroke 940 | 31 % → 47 % | 58.1 px | 0.48 | 1.53 | 9 |
| stroke 941 | 42 % → 61 % | 67.7 px | 0.51 | 1.45 | 21 |
| stroke 942 | 44 % → 47 % | 124.6 px | 0.49 | 1.05 | 4 |
| stroke 943 | 23 % → 41 % | 31.6 px | 0.52 | 1.76 | 13 |
| stroke 944 | 27 % → 47 % | 41.0 px | 0.47 | 1.78 | 23 |
| stroke 945 | 23 % → 43 % | 62.4 px | 0.47 | 1.89 | 3 |
| stroke 946 | 42 % → 61 % | 66.6 px | 0.52 | 1.44 | 7 |
| stroke 947 | 42 % → 55 % | 49.7 px | 0.52 | 1.30 | 23 |
| stroke 948 | 30 % → 52 % | 41.1 px | 0.48 | 1.75 | 29 |
| stroke 949 | 45 % → 49 % | 80.9 px | 0.52 | 1.07 | 8 |
| stroke 950 | 32 % → 51 % | 55.2 px | 0.51 | 1.59 | 12 |
| stroke 951 | 21 % → 53 % | 49.6 px | 0.47 | 2.58 | 9 |
| stroke 952 | 33 % → 58 % | 50.7 px | 0.51 | 1.78 | 4 |
| stroke 953 | 39 % → 62 % | 110.5 px | 0.49 | 1.57 | 6 |
| stroke 954 | 53 % → 62 % | 110.0 px | 0.51 | 1.19 | 7 |
| stroke 955 | 14 % → 30 % | 33.6 px | 0.52 | 2.20 | 4 |
| stroke 956 | 26 % → 38 % | 47.7 px | 0.52 | 1.47 | 11 |
| stroke 957 | 46 % → 62 % | 79.8 px | 0.52 | 1.35 | 13 |
| stroke 958 | 26 % → 45 % | 57.5 px | 0.48 | 1.71 | 5 |
| stroke 959 | 46 % → 49 % | 127.7 px | 0.49 | 1.07 | 5 |
| stroke 960 | 41 % → 55 % | 77.1 px | 0.49 | 1.36 | 13 |
| stroke 961 | 38 % → 56 % | 69.5 px | 0.50 | 1.49 | 22 |
| stroke 962 | 22 % → 50 % | 41.2 px | 0.46 | 2.25 | 15 |
| stroke 963 | 35 % → 50 % | 74.7 px | 0.49 | 1.46 | 3 |
| stroke 964 | 26 % → 56 % | 42.1 px | 0.47 | 2.10 | 9 |
| stroke 965 | 57 % → 64 % | 110.4 px | 0.51 | 1.13 | 7 |
| stroke 966 | 23 % → 50 % | 39.4 px | 0.47 | 2.18 | 29 |
| stroke 967 | 36 % → 50 % | 78.9 px | 0.51 | 1.41 | 22 |
| stroke 968 | 34 % → 42 % | 59.3 px | 0.51 | 1.25 | 15 |
| stroke 969 | 45 % → 59 % | 81.1 px | 0.53 | 1.33 | 15 |
| stroke 970 | 38 % → 68 % | 87.7 px | 0.51 | 1.77 | 10 |
| stroke 971 | 24 % → 37 % | 67.3 px | 0.50 | 1.54 | 6 |
| stroke 972 | 47 % → 58 % | 97.1 px | 0.52 | 1.23 | 14 |
| stroke 973 | 39 % → 54 % | 93.0 px | 0.50 | 1.36 | 10 |
| stroke 974 | 36 % → 52 % | 74.1 px | 0.52 | 1.44 | 12 |
| stroke 975 | 25 % → 36 % | 68.5 px | 0.49 | 1.41 | 5 |
| stroke 976 | 33 % → 54 % | 36.6 px | 0.48 | 1.65 | 12 |
| stroke 977 | 43 % → 55 % | 66.6 px | 0.47 | 1.29 | 18 |
| stroke 978 | 31 % → 42 % | 47.1 px | 0.51 | 1.37 | 7 |
| stroke 979 | 25 % → 38 % | 39.1 px | 0.48 | 1.48 | 13 |
| stroke 980 | 23 % → 41 % | 40.5 px | 0.46 | 1.80 | 27 |
| stroke 981 | 28 % → 58 % | 70.3 px | 0.47 | 2.13 | 8 |
| stroke 982 | 31 % → 57 % | 84.5 px | 0.47 | 1.87 | 13 |
| stroke 983 | 23 % → 43 % | 51.5 px | 0.46 | 1.86 | 9 |
| stroke 984 | 29 % → 39 % | 42.2 px | 0.52 | 1.32 | 9 |
| stroke 985 | 33 % → 48 % | 86.1 px | 0.46 | 1.47 | 5 |
| stroke 986 | 45 % → 56 % | 73.2 px | 0.50 | 1.22 | 32 |
| stroke 987 | 18 % → 31 % | 38.6 px | 0.45 | 1.78 | 9 |
| stroke 988 | 31 % → 56 % | 48.8 px | 0.49 | 1.80 | 23 |
| stroke 989 | 27 % → 39 % | 50.7 px | 0.49 | 1.47 | 13 |
| stroke 990 | 53 % → 60 % | 78.8 px | 0.53 | 1.13 | 11 |
| stroke 991 | 34 % → 43 % | 68.0 px | 0.50 | 1.26 | 8 |
| stroke 992 | 30 % → 46 % | 66.3 px | 0.50 | 1.50 | 7 |
| stroke 993 | 36 % → 40 % | 93.2 px | 0.51 | 1.12 | 3 |
| stroke 994 | 26 % → 50 % | 42.5 px | 0.47 | 1.95 | 16 |
| stroke 995 | 50 % → 60 % | 70.0 px | 0.52 | 1.19 | 12 |
| stroke 996 | 40 % → 55 % | 75.6 px | 0.47 | 1.39 | 13 |
| stroke 997 | 47 % → 56 % | 78.7 px | 0.51 | 1.19 | 17 |
| stroke 998 | 16 % → 32 % | 38.8 px | 0.47 | 2.02 | 9 |
| stroke 999 | 47 % → 55 % | 128.5 px | 0.50 | 1.19 | 4 |
| stroke 1000 | 28 % → 36 % | 67.4 px | 0.47 | 1.29 | 9 |
| stroke 1001 | 35 % → 53 % | 79.0 px | 0.51 | 1.51 | 10 |
| stroke 1002 | 27 % → 43 % | 49.5 px | 0.48 | 1.60 | 15 |
| stroke 1003 | 44 % → 58 % | 65.6 px | 0.49 | 1.33 | 10 |
| stroke 1004 | 34 % → 51 % | 67.4 px | 0.50 | 1.52 | 8 |
| stroke 1005 | 50 % → 59 % | 120.5 px | 0.47 | 1.19 | 10 |
| stroke 1006 | 50 % → 58 % | 102.0 px | 0.47 | 1.16 | 11 |
| stroke 1007 | 55 % → 63 % | 86.0 px | 0.51 | 1.15 | 18 |
| stroke 1008 | 37 % → 50 % | 66.0 px | 0.51 | 1.34 | 13 |
| stroke 1009 | 41 % → 65 % | 40.8 px | 0.50 | 1.58 | 15 |
| stroke 1010 | 32 % → 60 % | 69.7 px | 0.47 | 1.89 | 12 |
| stroke 1011 | 26 % → 47 % | 74.0 px | 0.46 | 1.84 | 6 |
| stroke 1012 | 50 % → 57 % | 98.7 px | 0.49 | 1.14 | 8 |
| stroke 1013 | 16 % → 32 % | 40.2 px | 0.46 | 2.04 | 4 |
| stroke 1014 | 21 % → 44 % | 42.9 px | 0.46 | 2.09 | 8 |
| stroke 1015 | 39 % → 48 % | 101.2 px | 0.48 | 1.23 | 6 |
| stroke 1016 | 40 % → 51 % | 93.9 px | 0.47 | 1.27 | 4 |
| stroke 1017 | 42 % → 51 % | 113.4 px | 0.48 | 1.22 | 5 |
| stroke 1018 | 30 % → 50 % | 66.5 px | 0.51 | 1.67 | 6 |
| stroke 1019 | 41 % → 51 % | 77.6 px | 0.49 | 1.25 | 5 |
| stroke 1020 | 42 % → 67 % | 116.0 px | 0.45 | 1.59 | 3 |
| stroke 1021 | 31 % → 49 % | 87.9 px | 0.47 | 1.58 | 3 |
| stroke 1022 | 63 % → 63 % | 174.5 px | 0.52 | 1.00 | 7 |
| stroke 1023 | 34 % → 64 % | 94.6 px | 0.47 | 1.88 | 3 |
| stroke 1024 | 32 % → 51 % | 68.3 px | 0.47 | 1.62 | 10 |
| stroke 1025 | 48 % → 50 % | 114.2 px | 0.52 | 1.04 | 5 |
| stroke 1026 | 38 % → 48 % | 68.4 px | 0.46 | 1.27 | 16 |
| stroke 1027 | 50 % → 58 % | 110.5 px | 0.53 | 1.16 | 10 |
| stroke 1028 | 45 % → 52 % | 110.8 px | 0.52 | 1.14 | 6 |
| stroke 1029 | 27 % → 36 % | 49.6 px | 0.49 | 1.32 | 14 |
| stroke 1030 | 54 % → 68 % | 150.3 px | 0.50 | 1.27 | 4 |
| stroke 1031 | 51 % → 60 % | 95.1 px | 0.49 | 1.17 | 13 |
| stroke 1032 | 5 % → 18 % | 10.8 px | 0.47 | 3.43 | 7 |
| stroke 1033 | 25 % → 49 % | 70.6 px | 0.49 | 1.98 | 6 |
| stroke 1034 | 52 % → 52 % | 130.3 px | 0.48 | 1.00 | 4 |
| stroke 1035 | 56 % → 70 % | 122.0 px | 0.49 | 1.26 | 10 |
| stroke 1036 | 28 % → 37 % | 47.1 px | 0.46 | 1.31 | 23 |
| stroke 1037 | 19 % → 28 % | 52.4 px | 0.52 | 1.52 | 6 |
| stroke 1038 | 50 % → 50 % | 110.7 px | 0.49 | 1.00 | 5 |
| stroke 1039 | 43 % → 58 % | 84.5 px | 0.48 | 1.33 | 13 |
| stroke 1040 | 48 % → 61 % | 99.5 px | 0.52 | 1.27 | 14 |
| stroke 1041 | 48 % → 64 % | 106.1 px | 0.46 | 1.33 | 10 |
| stroke 1042 | 28 % → 38 % | 59.0 px | 0.49 | 1.37 | 9 |
| stroke 1043 | 18 % → 27 % | 33.8 px | 0.49 | 1.51 | 14 |
| stroke 1044 | 42 % → 48 % | 90.4 px | 0.52 | 1.16 | 7 |
| stroke 1045 | 30 % → 40 % | 53.6 px | 0.49 | 1.34 | 15 |
| stroke 1046 | 41 % → 58 % | 105.4 px | 0.48 | 1.41 | 5 |
| stroke 1047 | 54 % → 61 % | 102.4 px | 0.50 | 1.14 | 9 |
| stroke 1048 | 37 % → 55 % | 68.3 px | 0.48 | 1.48 | 15 |
| stroke 1049 | 44 % → 61 % | 104.7 px | 0.48 | 1.39 | 5 |
| stroke 1050 | 14 % → 28 % | 40.0 px | 0.53 | 2.00 | 6 |
| stroke 1051 | 13 % → 30 % | 33.8 px | 0.46 | 2.25 | 4 |
| stroke 1052 | 43 % → 60 % | 120.1 px | 0.47 | 1.40 | 5 |
| stroke 1053 | 44 % → 54 % | 88.5 px | 0.46 | 1.23 | 11 |
| stroke 1054 | 39 % → 54 % | 73.1 px | 0.48 | 1.38 | 7 |
| stroke 1055 | 31 % → 45 % | 81.4 px | 0.46 | 1.46 | 8 |
| stroke 1056 | 52 % → 61 % | 108.0 px | 0.51 | 1.17 | 7 |
| stroke 1057 | 35 % → 59 % | 77.6 px | 0.47 | 1.70 | 12 |
| stroke 1058 | 47 % → 56 % | 99.7 px | 0.49 | 1.18 | 7 |
| stroke 1059 | 57 % → 62 % | 124.0 px | 0.49 | 1.07 | 7 |
| stroke 1060 | 42 % → 53 % | 119.0 px | 0.51 | 1.27 | 3 |
| stroke 1061 | 40 % → 61 % | 82.3 px | 0.47 | 1.52 | 9 |
| stroke 1062 | 34 % → 49 % | 41.4 px | 0.53 | 1.46 | 13 |
| stroke 1063 | 32 % → 48 % | 66.3 px | 0.48 | 1.50 | 7 |
| stroke 1064 | 23 % → 43 % | 63.4 px | 0.47 | 1.89 | 8 |
| stroke 1065 | 36 % → 55 % | 89.2 px | 0.47 | 1.53 | 4 |
| stroke 1066 | 42 % → 51 % | 57.9 px | 0.47 | 1.23 | 4 |
| stroke 1067 | 30 % → 49 % | 57.6 px | 0.47 | 1.61 | 9 |
| stroke 1068 | 16 % → 22 % | 45.6 px | 0.53 | 1.37 | 3 |
| stroke 1069 | 33 % → 53 % | 80.0 px | 0.53 | 1.61 | 8 |
| stroke 1070 | 24 % → 36 % | 47.1 px | 0.49 | 1.49 | 3 |
| stroke 1071 | 24 % → 42 % | 68.0 px | 0.47 | 1.75 | 8 |
| stroke 1072 | 29 % → 42 % | 82.2 px | 0.48 | 1.43 | 3 |
| stroke 1073 | 40 % → 53 % | 93.7 px | 0.51 | 1.31 | 5 |
| stroke 1074 | 38 % → 49 % | 94.2 px | 0.44 | 1.29 | 5 |
| stroke 1075 | 67 % → 72 % | 106.7 px | 0.53 | 1.08 | 12 |
| stroke 1076 | 30 % → 45 % | 69.0 px | 0.46 | 1.47 | 11 |
| stroke 1077 | 34 % → 43 % | 62.9 px | 0.52 | 1.27 | 8 |
| stroke 1078 | 29 % → 46 % | 77.9 px | 0.49 | 1.61 | 4 |
| stroke 1079 | 28 % → 47 % | 68.1 px | 0.45 | 1.69 | 9 |
| stroke 1080 | 54 % → 54 % | 86.6 px | 0.52 | 1.00 | 11 |
| stroke 1081 | 42 % → 57 % | 95.2 px | 0.41 | 1.34 | 9 |
| stroke 1082 | 55 % → 68 % | 85.5 px | 0.49 | 1.25 | 16 |
| stroke 1083 | 50 % → 55 % | 96.7 px | 0.50 | 1.09 | 9 |
| stroke 1084 | 44 % → 64 % | 91.4 px | 0.45 | 1.44 | 13 |
| stroke 1085 | 39 % → 49 % | 73.2 px | 0.52 | 1.26 | 13 |
| stroke 1086 | 53 % → 57 % | 141.8 px | 0.47 | 1.07 | 6 |
| stroke 1087 | 49 % → 51 % | 141.1 px | 0.52 | 1.03 | 6 |
| stroke 1088 | 61 % → 61 % | 166.7 px | 0.52 | 1.00 | 3 |
| stroke 1089 | 48 % → 60 % | 36.9 px | 0.50 | 1.24 | 42 |
| stroke 1090 | 26 % → 33 % | 73.4 px | 0.51 | 1.28 | 5 |
| stroke 1091 | 38 % → 49 % | 68.3 px | 0.51 | 1.31 | 8 |
| stroke 1092 | 64 % → 68 % | 164.5 px | 0.52 | 1.06 | 3 |
| stroke 1093 | 45 % → 52 % | 104.2 px | 0.50 | 1.14 | 4 |
| stroke 1094 | 58 % → 59 % | 161.6 px | 0.51 | 1.03 | 3 |
| stroke 1095 | 46 % → 64 % | 125.5 px | 0.47 | 1.38 | 5 |
| stroke 1096 | 31 % → 53 % | 42.0 px | 0.46 | 1.70 | 21 |
| stroke 1097 | 16 % → 26 % | 35.9 px | 0.52 | 1.61 | 12 |
| stroke 1098 | 32 % → 45 % | 86.0 px | 0.51 | 1.42 | 6 |
| stroke 1099 | 51 % → 68 % | 117.9 px | 0.48 | 1.34 | 7 |
| stroke 1100 | 38 % → 54 % | 93.3 px | 0.47 | 1.42 | 10 |
| stroke 1101 | 46 % → 61 % | 72.7 px | 0.50 | 1.32 | 8 |
| stroke 1102 | 41 % → 57 % | 79.6 px | 0.47 | 1.39 | 14 |
| stroke 1103 | 37 % → 48 % | 85.6 px | 0.48 | 1.31 | 9 |
| stroke 1104 | 54 % → 57 % | 100.7 px | 0.52 | 1.05 | 14 |
| stroke 1105 | 40 % → 52 % | 80.3 px | 0.47 | 1.31 | 11 |
| stroke 1106 | 29 % → 41 % | 74.6 px | 0.48 | 1.41 | 6 |
| stroke 1107 | 54 % → 54 % | 137.4 px | 0.52 | 1.00 | 3 |
| stroke 1108 | 22 % → 35 % | 59.4 px | 0.49 | 1.63 | 7 |
| stroke 1109 | 50 % → 56 % | 140.9 px | 0.53 | 1.12 | 5 |
| stroke 1110 | 43 % → 64 % | 97.0 px | 0.47 | 1.48 | 9 |
| stroke 1111 | 58 % → 58 % | 128.1 px | 0.52 | 1.00 | 9 |
| stroke 1112 | 17 % → 36 % | 48.5 px | 0.46 | 2.13 | 5 |
| stroke 1113 | 27 % → 50 % | 65.4 px | 0.47 | 1.84 | 4 |
| stroke 1114 | 57 % → 64 % | 138.7 px | 0.49 | 1.12 | 7 |
| stroke 1115 | 35 % → 48 % | 72.6 px | 0.53 | 1.36 | 4 |
| stroke 1116 | 35 % → 60 % | 71.4 px | 0.46 | 1.70 | 5 |
| stroke 1117 | 50 % → 62 % | 66.2 px | 0.52 | 1.24 | 11 |
| stroke 1118 | 28 % → 41 % | 53.5 px | 0.47 | 1.48 | 11 |
| stroke 1119 | 29 % → 40 % | 61.8 px | 0.50 | 1.41 | 4 |
| stroke 1120 | 65 % → 66 % | 157.4 px | 0.52 | 1.02 | 4 |
| stroke 1121 | 39 % → 49 % | 86.4 px | 0.49 | 1.25 | 10 |
| stroke 1122 | 47 % → 51 % | 27.7 px | 0.52 | 1.08 | 57 |
| stroke 1123 | 30 % → 32 % | 27.9 px | 0.51 | 1.10 | 52 |
| stroke 1124 | 40 % → 41 % | 43.7 px | 0.49 | 1.03 | 58 |
| stroke 1125 | 36 % → 41 % | 43.4 px | 0.49 | 1.12 | 40 |
| stroke 1126 | 33 % → 39 % | 41.7 px | 0.49 | 1.16 | 43 |
| stroke 1127 | 41 % → 46 % | 46.6 px | 0.48 | 1.10 | 54 |
| stroke 1128 | 41 % → 48 % | 50.1 px | 0.49 | 1.17 | 68 |
| stroke 1129 | 33 % → 37 % | 47.5 px | 0.51 | 1.12 | 60 |
| stroke 1130 | 42 % → 46 % | 48.8 px | 0.52 | 1.10 | 81 |
| stroke 1131 | 43 % → 46 % | 48.8 px | 0.51 | 1.07 | 54 |
| stroke 1132 | 52 % → 61 % | 53.6 px | 0.48 | 1.17 | 63 |
| stroke 1133 | 53 % → 65 % | 55.0 px | 0.48 | 1.22 | 69 |
| stroke 1134 | 48 % → 55 % | 50.8 px | 0.46 | 1.17 | 63 |
| stroke 1135 | 46 % → 54 % | 53.5 px | 0.47 | 1.19 | 79 |
| stroke 1136 | 37 % → 46 % | 53.0 px | 0.50 | 1.26 | 54 |
| stroke 1137 | 36 % → 43 % | 40.4 px | 0.51 | 1.20 | 62 |
| stroke 1138 | 38 % → 46 % | 41.1 px | 0.49 | 1.21 | 48 |
| stroke 1139 | 40 % → 45 % | 41.0 px | 0.49 | 1.12 | 67 |
| stroke 1140 | 31 % → 36 % | 33.3 px | 0.49 | 1.15 | 68 |
| stroke 1141 | 39 % → 42 % | 45.2 px | 0.49 | 1.05 | 43 |
| stroke 1142 | 45 % → 47 % | 63.8 px | 0.49 | 1.03 | 43 |
| stroke 1143 | 24 % → 30 % | 29.9 px | 0.47 | 1.24 | 48 |
| stroke 1144 | 44 % → 50 % | 46.6 px | 0.48 | 1.12 | 59 |
| stroke 1145 | 50 % → 53 % | 64.5 px | 0.49 | 1.07 | 51 |
| stroke 1146 | 41 % → 48 % | 56.7 px | 0.48 | 1.16 | 52 |
| stroke 1147 | 50 % → 56 % | 67.7 px | 0.48 | 1.12 | 44 |
| stroke 1148 | 44 % → 47 % | 54.5 px | 0.49 | 1.07 | 54 |
| stroke 1149 | 34 % → 36 % | 42.8 px | 0.49 | 1.07 | 61 |
| stroke 1150 | 31 % → 36 % | 35.4 px | 0.48 | 1.15 | 51 |
| stroke 1151 | 38 % → 46 % | 47.5 px | 0.48 | 1.22 | 83 |
| stroke 1152 | 37 % → 45 % | 38.0 px | 0.47 | 1.21 | 57 |
| stroke 1153 | 46 % → 50 % | 51.7 px | 0.47 | 1.09 | 44 |
| stroke 1154 | 44 % → 50 % | 58.2 px | 0.44 | 1.13 | 68 |
| stroke 1155 | 35 % → 45 % | 34.2 px | 0.47 | 1.28 | 52 |
| stroke 1156 | 26 % → 34 % | 25.2 px | 0.47 | 1.31 | 72 |
| stroke 1157 | 42 % → 45 % | 46.6 px | 0.45 | 1.09 | 61 |
| stroke 1158 | 53 % → 55 % | 56.8 px | 0.43 | 1.03 | 61 |
| stroke 1159 | 39 % → 46 % | 44.6 px | 0.44 | 1.16 | 66 |
| stroke 1160 | 44 % → 48 % | 51.3 px | 0.47 | 1.10 | 44 |
| stroke 1161 | 42 % → 45 % | 39.0 px | 0.46 | 1.06 | 67 |
| stroke 1162 | 46 % → 50 % | 60.0 px | 0.49 | 1.08 | 47 |
| stroke 1163 | 35 % → 39 % | 36.0 px | 0.49 | 1.11 | 63 |
| stroke 1164 | 37 % → 46 % | 45.7 px | 0.48 | 1.24 | 55 |
| stroke 1165 | 33 % → 38 % | 37.9 px | 0.47 | 1.15 | 43 |
| stroke 1166 | 39 % → 43 % | 40.5 px | 0.47 | 1.10 | 43 |
| stroke 1167 | 41 % → 44 % | 46.5 px | 0.46 | 1.06 | 61 |
| stroke 1168 | 47 % → 51 % | 57.1 px | 0.46 | 1.08 | 63 |
| stroke 1169 | 41 % → 46 % | 47.9 px | 0.47 | 1.15 | 38 |
| stroke 1170 | 52 % → 57 % | 59.0 px | 0.48 | 1.10 | 68 |
| stroke 1171 | 40 % → 49 % | 52.1 px | 0.46 | 1.23 | 45 |
| stroke 1172 | 35 % → 44 % | 36.2 px | 0.46 | 1.26 | 78 |
| stroke 1173 | 31 % → 39 % | 30.2 px | 0.45 | 1.27 | 76 |
| stroke 1174 | 42 % → 54 % | 47.8 px | 0.47 | 1.30 | 68 |
| stroke 1175 | 38 % → 53 % | 54.1 px | 0.46 | 1.39 | 60 |
| stroke 1176 | 34 % → 46 % | 36.5 px | 0.46 | 1.37 | 57 |
| stroke 1177 | 38 % → 45 % | 42.8 px | 0.46 | 1.21 | 50 |
| stroke 1178 | 37 % → 43 % | 46.0 px | 0.46 | 1.17 | 77 |
| stroke 1179 | 46 % → 53 % | 61.3 px | 0.46 | 1.16 | 41 |
| stroke 1180 | 38 % → 51 % | 51.3 px | 0.46 | 1.34 | 62 |
| stroke 1181 | 23 % → 36 % | 27.4 px | 0.46 | 1.61 | 81 |
| stroke 1182 | 22 % → 36 % | 21.7 px | 0.46 | 1.65 | 52 |
| stroke 1183 | 31 % → 45 % | 39.8 px | 0.46 | 1.49 | 49 |
| stroke 1184 | 38 % → 54 % | 39.6 px | 0.46 | 1.39 | 62 |
| stroke 1185 | 22 % → 36 % | 29.4 px | 0.48 | 1.65 | 59 |
| stroke 1186 | 23 % → 29 % | 26.1 px | 0.49 | 1.28 | 60 |
| stroke 1187 | 42 % → 54 % | 43.4 px | 0.47 | 1.28 | 57 |
| stroke 1188 | 46 % → 52 % | 45.8 px | 0.50 | 1.14 | 47 |
| stroke 1189 | 34 % → 39 % | 27.7 px | 0.51 | 1.17 | 39 |
| stroke 1190 | 36 % → 41 % | 33.5 px | 0.49 | 1.14 | 48 |
| stroke 1191 | 41 % → 46 % | 43.0 px | 0.46 | 1.13 | 68 |
| stroke 1192 | 46 % → 52 % | 55.8 px | 0.46 | 1.13 | 43 |
| stroke 1193 | 54 % → 58 % | 58.2 px | 0.48 | 1.07 | 72 |
| stroke 1194 | 33 % → 34 % | 34.6 px | 0.47 | 1.04 | 68 |
| stroke 1195 | 36 % → 40 % | 44.2 px | 0.49 | 1.14 | 49 |
| stroke 1196 | 44 % → 45 % | 34.7 px | 0.49 | 1.03 | 46 |
| stroke 1197 | 55 % → 60 % | 53.4 px | 0.48 | 1.08 | 55 |
| stroke 1198 | 58 % → 61 % | 44.8 px | 0.50 | 1.05 | 61 |
| stroke 1199 | 49 % → 50 % | 55.8 px | 0.52 | 1.02 | 42 |
| stroke 1200 | 42 % → 43 % | 46.3 px | 0.52 | 1.02 | 75 |
| stroke 1201 | 40 % → 42 % | 61.7 px | 0.51 | 1.05 | 32 |
| stroke 1202 | 35 % → 40 % | 46.2 px | 0.50 | 1.12 | 37 |
| stroke 1203 | 35 % → 35 % | 42.3 px | 0.52 | 1.02 | 56 |
| stroke 1204 | 35 % → 36 % | 52.4 px | 0.53 | 1.04 | 38 |
| stroke 1205 | 37 % → 38 % | 55.6 px | 0.52 | 1.02 | 35 |
| stroke 1206 | 35 % → 35 % | 40.1 px | 0.52 | 1.02 | 43 |
| stroke 1207 | 41 % → 42 % | 30.3 px | 0.52 | 1.05 | 52 |
| stroke 1208 | 51 % → 54 % | 29.2 px | 0.52 | 1.06 | 42 |
| stroke 1209 | 44 % → 44 % | 50.4 px | 0.51 | 1.02 | 38 |
| stroke 1210 | 42 % → 42 % | 50.3 px | 0.50 | 1.01 | 43 |
| stroke 1211 | 34 % → 37 % | 51.3 px | 0.47 | 1.10 | 60 |
| stroke 1212 | 25 % → 29 % | 28.3 px | 0.46 | 1.17 | 39 |
| stroke 1213 | 32 % → 37 % | 34.2 px | 0.47 | 1.14 | 66 |
| stroke 1214 | 39 % → 44 % | 51.5 px | 0.47 | 1.12 | 41 |
| stroke 1215 | 48 % → 54 % | 50.7 px | 0.48 | 1.13 | 48 |
| stroke 1216 | 51 % → 51 % | 54.6 px | 0.48 | 1.01 | 52 |
| stroke 1217 | 33 % → 35 % | 34.5 px | 0.50 | 1.05 | 62 |
| stroke 1218 | 38 % → 40 % | 53.0 px | 0.50 | 1.04 | 40 |
| stroke 1219 | 29 % → 34 % | 27.7 px | 0.48 | 1.17 | 86 |
| stroke 1220 | 41 % → 45 % | 46.2 px | 0.48 | 1.10 | 64 |
| stroke 1221 | 43 % → 44 % | 49.2 px | 0.52 | 1.02 | 55 |
| stroke 1222 | 56 % → 57 % | 35.3 px | 0.53 | 1.02 | 66 |
| stroke 1223 | 55 % → 56 % | 34.9 px | 0.53 | 1.02 | 54 |
| stroke 1224 | 62 % → 63 % | 39.3 px | 0.51 | 1.01 | 38 |
| stroke 1225 | 56 % → 64 % | 35.0 px | 0.50 | 1.16 | 64 |
| stroke 1226 | 53 % → 62 % | 36.3 px | 0.50 | 1.17 | 61 |
| stroke 1227 | 33 % → 42 % | 40.4 px | 0.47 | 1.30 | 40 |
| stroke 1228 | 35 % → 39 % | 37.5 px | 0.50 | 1.11 | 60 |
| stroke 1229 | 34 % → 39 % | 43.2 px | 0.49 | 1.13 | 42 |
| stroke 1230 | 39 % → 41 % | 44.1 px | 0.49 | 1.05 | 35 |
| stroke 1231 | 30 % → 34 % | 30.6 px | 0.47 | 1.12 | 47 |
| stroke 1232 | 40 % → 41 % | 58.0 px | 0.47 | 1.02 | 42 |
| stroke 1233 | 48 % → 52 % | 66.5 px | 0.48 | 1.07 | 60 |
| stroke 1234 | 48 % → 49 % | 62.5 px | 0.46 | 1.03 | 34 |
| stroke 1235 | 38 % → 45 % | 47.9 px | 0.47 | 1.18 | 35 |
| stroke 1236 | 46 % → 46 % | 60.1 px | 0.49 | 1.01 | 46 |
| stroke 1237 | 40 % → 42 % | 55.8 px | 0.48 | 1.04 | 58 |
| stroke 1238 | 44 % → 47 % | 67.2 px | 0.48 | 1.08 | 38 |
| stroke 1239 | 54 % → 55 % | 51.2 px | 0.47 | 1.00 | 47 |
| stroke 1240 | 68 % → 68 % | 464.6 px | 0.47 | 1.00 | 2 |
| stroke 1241 | 57 % → 61 % | 68.5 px | 0.46 | 1.07 | 41 |
| stroke 1242 | 56 % → 56 % | 70.6 px | 0.48 | 1.00 | 43 |
| stroke 1243 | 39 % → 50 % | 41.6 px | 0.46 | 1.28 | 38 |
| stroke 1244 | 40 % → 48 % | 42.2 px | 0.48 | 1.20 | 59 |
| stroke 1245 | 39 % → 49 % | 43.9 px | 0.49 | 1.25 | 52 |
| stroke 1246 | 43 % → 48 % | 43.2 px | 0.50 | 1.12 | 49 |
| stroke 1247 | 36 % → 40 % | 34.3 px | 0.51 | 1.11 | 44 |
| stroke 1248 | 29 % → 33 % | 26.9 px | 0.52 | 1.13 | 39 |
| stroke 1249 | 43 % → 48 % | 63.1 px | 0.51 | 1.13 | 37 |
| stroke 1250 | 58 % → 63 % | 62.1 px | 0.49 | 1.09 | 65 |
| stroke 1251 | 51 % → 52 % | 66.3 px | 0.50 | 1.02 | 52 |
| stroke 1252 | 31 % → 32 % | 40.4 px | 0.51 | 1.03 | 48 |
| stroke 1253 | 49 % → 50 % | 54.1 px | 0.50 | 1.02 | 50 |
| stroke 1254 | 45 % → 47 % | 57.2 px | 0.51 | 1.04 | 59 |
| stroke 1255 | 44 % → 46 % | 65.4 px | 0.52 | 1.04 | 40 |
| stroke 1256 | 46 % → 47 % | 71.0 px | 0.47 | 1.00 | 45 |
| stroke 1257 | 58 % → 58 % | 54.2 px | 0.48 | 1.00 | 31 |
| stroke 1258 | 57 % → 57 % | 390.1 px | 0.47 | 1.00 | 1 |
| stroke 1259 | 28 % → 32 % | 36.0 px | 0.47 | 1.12 | 115 |
| stroke 1260 | 34 % → 35 % | 42.8 px | 0.48 | 1.01 | 49 |
| stroke 1261 | 30 % → 30 % | 137.1 px | 0.48 | 1.00 | 8 |
| stroke 1262 | 39 % → 44 % | 47.3 px | 0.50 | 1.14 | 46 |
| stroke 1263 | 35 % → 35 % | 33.5 px | 0.52 | 1.01 | 58 |
| stroke 1264 | 42 % → 46 % | 38.9 px | 0.52 | 1.11 | 58 |
| stroke 1265 | 53 % → 57 % | 57.7 px | 0.50 | 1.09 | 60 |
| stroke 1266 | 53 % → 56 % | 56.7 px | 0.50 | 1.05 | 39 |
| stroke 1267 | 38 % → 44 % | 46.5 px | 0.50 | 1.17 | 52 |
| stroke 1268 | 43 % → 51 % | 45.9 px | 0.49 | 1.19 | 52 |
| stroke 1269 | 54 % → 57 % | 68.9 px | 0.49 | 1.05 | 57 |
| stroke 1270 | 36 % → 39 % | 52.3 px | 0.51 | 1.10 | 39 |
| stroke 1271 | 37 % → 38 % | 53.9 px | 0.51 | 1.03 | 43 |
| stroke 1272 | 59 % → 60 % | 97.4 px | 0.49 | 1.02 | 20 |
| stroke 1273 | 62 % → 62 % | 61.9 px | 0.48 | 1.01 | 39 |
| stroke 1274 | 66 % → 66 % | 180.4 px | 0.48 | 1.00 | 20 |
| stroke 1275 | 55 % → 57 % | 61.2 px | 0.48 | 1.03 | 50 |
| stroke 1276 | 55 % → 55 % | 81.5 px | 0.48 | 1.00 | 33 |
| stroke 1277 | 51 % → 58 % | 57.0 px | 0.46 | 1.14 | 42 |
| stroke 1278 | 45 % → 50 % | 47.5 px | 0.46 | 1.12 | 55 |
| stroke 1279 | 55 % → 56 % | 69.6 px | 0.47 | 1.02 | 36 |
| stroke 1280 | 59 % → 59 % | 129.8 px | 0.46 | 1.00 | 10 |
| stroke 1281 | 23 % → 35 % | 27.1 px | 0.53 | 1.55 | 54 |
| stroke 1282 | 28 % → 45 % | 33.0 px | 0.52 | 1.63 | 43 |
| stroke 1283 | 35 % → 42 % | 42.8 px | 0.49 | 1.21 | 80 |
| stroke 1284 | 39 % → 45 % | 44.6 px | 0.48 | 1.16 | 61 |
| stroke 1285 | 48 % → 54 % | 52.9 px | 0.49 | 1.13 | 39 |
| stroke 1286 | 38 % → 47 % | 55.1 px | 0.48 | 1.25 | 61 |
| stroke 1287 | 32 % → 41 % | 36.9 px | 0.47 | 1.29 | 68 |
| stroke 1288 | 39 % → 51 % | 42.7 px | 0.47 | 1.29 | 145 |
| stroke 1289 | 43 % → 50 % | 52.7 px | 0.47 | 1.16 | 69 |
| stroke 1290 | 49 % → 56 % | 54.1 px | 0.47 | 1.14 | 58 |
| stroke 1291 | 50 % → 56 % | 64.6 px | 0.47 | 1.13 | 96 |
| stroke 1292 | 43 % → 45 % | 60.4 px | 0.51 | 1.03 | 75 |
| stroke 1293 | 25 % → 28 % | 40.4 px | 0.53 | 1.12 | 31 |
| stroke 1294 | 32 % → 32 % | 28.7 px | 0.46 | 1.00 | 38 |
| stroke 1295 | 24 % → 24 % | 20.5 px | 0.49 | 1.00 | 44 |
| stroke 1296 | 51 % → 56 % | 57.5 px | 0.47 | 1.08 | 53 |
| stroke 1297 | 56 % → 57 % | 65.4 px | 0.47 | 1.03 | 41 |
| stroke 1298 | 57 % → 57 % | 83.7 px | 0.47 | 1.00 | 30 |
| stroke 1299 | 55 % → 56 % | 52.4 px | 0.47 | 1.00 | 60 |
| stroke 1300 | 67 % → 67 % | 218.8 px | 0.48 | 1.00 | 6 |
| stroke 1301 | 54 % → 56 % | 67.0 px | 0.48 | 1.05 | 43 |
| stroke 1302 | 47 % → 52 % | 55.5 px | 0.49 | 1.09 | 63 |
| stroke 1303 | 49 % → 54 % | 67.6 px | 0.48 | 1.10 | 70 |
| stroke 1304 | 66 % → 66 % | 447.9 px | 0.47 | 1.00 | 4 |
| stroke 1305 | 24 % → 45 % | 41.9 px | 0.47 | 1.88 | 11 |
| stroke 1306 | 53 % → 56 % | 67.5 px | 0.49 | 1.06 | 44 |
| stroke 1307 | 60 % → 60 % | 85.6 px | 0.49 | 1.00 | 30 |
| stroke 1308 | 39 % → 47 % | 23.4 px | 0.52 | 1.19 | 80 |
| stroke 1309 | 39 % → 50 % | 22.2 px | 0.53 | 1.28 | 67 |
| stroke 1310 | 32 % → 49 % | 23.5 px | 0.52 | 1.55 | 54 |
| stroke 1311 | 40 % → 48 % | 29.6 px | 0.53 | 1.22 | 39 |
| stroke 1312 | 39 % → 39 % | 33.5 px | 0.52 | 1.00 | 31 |
| stroke 1313 | 57 % → 65 % | 73.3 px | 0.50 | 1.14 | 36 |
| stroke 1314 | 59 % → 61 % | 69.0 px | 0.50 | 1.03 | 43 |
| stroke 1315 | 59 % → 59 % | 73.6 px | 0.51 | 1.00 | 30 |
| stroke 1316 | 12 % → 39 % | 16.0 px | 0.50 | 3.30 | 31 |
| stroke 1317 | 11 % → 28 % | 26.5 px | 0.48 | 2.57 | 4 |
| stroke 1318 | 16 % → 41 % | 21.5 px | 0.51 | 2.54 | 28 |
| stroke 1319 | 22 % → 43 % | 34.1 px | 0.51 | 1.91 | 15 |
| stroke 1320 | 13 % → 40 % | 28.3 px | 0.52 | 2.96 | 10 |
| stroke 1321 | 28 % → 41 % | 63.8 px | 0.47 | 1.47 | 7 |
| stroke 1322 | 16 % → 34 % | 38.2 px | 0.52 | 2.12 | 7 |
| stroke 1323 | 34 % → 48 % | 93.5 px | 0.53 | 1.40 | 7 |
| stroke 1324 | 23 % → 33 % | 24.7 px | 0.49 | 1.47 | 64 |
| stroke 1325 | 24 % → 37 % | 32.8 px | 0.52 | 1.58 | 52 |
| stroke 1326 | 34 % → 37 % | 36.7 px | 0.52 | 1.09 | 41 |
| stroke 1327 | 41 % → 43 % | 48.8 px | 0.51 | 1.05 | 37 |
| stroke 1328 | 26 % → 26 % | 42.4 px | 0.48 | 1.00 | 15 |
| stroke 1329 | 17 % → 29 % | 36.2 px | 0.48 | 1.69 | 4 |
| stroke 1330 | 26 % → 32 % | 25.3 px | 0.48 | 1.22 | 25 |
| stroke 1331 | 5 % → 55 % | 9.1 px | 0.48 | 10.28 | 25 |
| stroke 1332 | 8 % → 31 % | 8.8 px | 0.53 | 4.14 | 13 |
| stroke 1333 | 9 % → 54 % | 11.6 px | 0.50 | 6.30 | 23 |
| stroke 1334 | 13 % → 53 % | 15.2 px | 0.47 | 4.18 | 20 |
| stroke 1335 | 14 % → 37 % | 21.3 px | 0.50 | 2.68 | 24 |
| stroke 1336 | 9 % → 56 % | 12.3 px | 0.51 | 6.32 | 25 |
| stroke 1337 | 12 % → 44 % | 17.6 px | 0.47 | 3.51 | 26 |
| stroke 1338 | 13 % → 58 % | 19.5 px | 0.52 | 4.42 | 38 |
| stroke 1339 | 14 % → 43 % | 29.6 px | 0.48 | 3.16 | 4 |
| stroke 1340 | 17 % → 43 % | 47.0 px | 0.49 | 2.50 | 4 |
| stroke 1341 | 18 % → 47 % | 17.2 px | 0.53 | 2.68 | 21 |
| stroke 1342 | 16 % → 48 % | 18.2 px | 0.53 | 3.00 | 17 |
| stroke 1343 | 21 % → 35 % | 47.8 px | 0.48 | 1.71 | 14 |
| stroke 1344 | 16 % → 31 % | 24.0 px | 0.49 | 1.91 | 26 |
| stroke 1345 | 10 % → 45 % | 14.9 px | 0.52 | 4.47 | 18 |
| stroke 1346 | 15 % → 45 % | 13.3 px | 0.53 | 2.97 | 16 |
| stroke 1347 | 23 % → 51 % | 32.1 px | 0.50 | 2.19 | 22 |
| stroke 1348 | 19 % → 45 % | 27.5 px | 0.52 | 2.34 | 15 |
| stroke 1349 | 17 % → 42 % | 28.2 px | 0.47 | 2.44 | 10 |
| stroke 1350 | 34 % → 51 % | 45.2 px | 0.52 | 1.49 | 22 |
| stroke 1351 | 17 % → 43 % | 22.7 px | 0.53 | 2.52 | 27 |
| stroke 1352 | 21 % → 46 % | 54.8 px | 0.47 | 2.13 | 8 |
| stroke 1353 | 33 % → 59 % | 37.1 px | 0.53 | 1.80 | 16 |
| stroke 1354 | 20 % → 40 % | 31.8 px | 0.51 | 2.02 | 20 |
| stroke 1355 | 30 % → 50 % | 57.9 px | 0.50 | 1.67 | 8 |
| stroke 1356 | 36 % → 53 % | 54.1 px | 0.53 | 1.46 | 6 |
| stroke 1357 | 24 % → 52 % | 36.7 px | 0.53 | 2.16 | 6 |
| stroke 1358 | 31 % → 59 % | 56.6 px | 0.52 | 1.89 | 11 |
| stroke 1359 | 43 % → 62 % | 109.0 px | 0.53 | 1.45 | 3 |
| stroke 1360 | 35 % → 54 % | 50.4 px | 0.52 | 1.57 | 18 |
| stroke 1361 | 30 % → 54 % | 72.5 px | 0.49 | 1.84 | 6 |
| stroke 1362 | 34 % → 42 % | 87.7 px | 0.51 | 1.25 | 3 |
| stroke 1363 | 17 % → 33 % | 32.2 px | 0.49 | 1.95 | 12 |
| stroke 1364 | 43 % → 58 % | 94.5 px | 0.53 | 1.34 | 10 |
| stroke 1365 | 24 % → 44 % | 52.7 px | 0.47 | 1.83 | 11 |
| stroke 1366 | 13 % → 23 % | 30.3 px | 0.47 | 1.75 | 9 |
| stroke 1367 | 35 % → 51 % | 49.9 px | 0.52 | 1.44 | 6 |
| stroke 1368 | 21 % → 34 % | 51.1 px | 0.53 | 1.61 | 3 |
| stroke 1369 | 36 % → 55 % | 102.1 px | 0.51 | 1.52 | 3 |
| stroke 1370 | 26 % → 55 % | 60.4 px | 0.47 | 2.15 | 8 |
| stroke 1371 | 46 % → 54 % | 116.9 px | 0.53 | 1.19 | 7 |
| stroke 1372 | 56 % → 60 % | 135.2 px | 0.53 | 1.08 | 4 |
| stroke 1373 | 27 % → 32 % | 24.7 px | 0.47 | 1.19 | 47 |
| stroke 1374 | 31 % → 34 % | 42.9 px | 0.47 | 1.09 | 35 |
| stroke 1375 | 40 % → 42 % | 25.5 px | 0.53 | 1.05 | 63 |
| stroke 1376 | 43 % → 48 % | 27.2 px | 0.53 | 1.12 | 65 |
| stroke 1377 | 25 % → 30 % | 15.4 px | 0.53 | 1.21 | 69 |
| stroke 1378 | 34 % → 37 % | 39.6 px | 0.52 | 1.10 | 57 |
| stroke 1379 | 36 % → 46 % | 43.4 px | 0.49 | 1.27 | 98 |
| stroke 1380 | 27 % → 32 % | 27.9 px | 0.47 | 1.17 | 55 |
| stroke 1381 | 40 % → 50 % | 42.1 px | 0.48 | 1.25 | 87 |
| stroke 1382 | 38 % → 46 % | 56.4 px | 0.49 | 1.20 | 68 |
| stroke 1383 | 25 % → 31 % | 24.6 px | 0.48 | 1.23 | 56 |
| stroke 1384 | 35 % → 36 % | 44.7 px | 0.50 | 1.04 | 49 |
| stroke 1385 | 40 % → 42 % | 49.2 px | 0.51 | 1.06 | 50 |
| stroke 1386 | 33 % → 39 % | 48.1 px | 0.50 | 1.19 | 38 |
| stroke 1387 | 28 % → 32 % | 25.8 px | 0.52 | 1.14 | 55 |
| stroke 1388 | 43 % → 44 % | 41.0 px | 0.53 | 1.03 | 52 |
| stroke 1389 | 37 % → 37 % | 332.4 px | 0.53 | 1.00 | 0 |
| stroke 1390 | 44 % → 56 % | 56.5 px | 0.51 | 1.27 | 25 |
| stroke 1391 | 55 % → 60 % | 63.1 px | 0.51 | 1.08 | 27 |
| stroke 1392 | 47 % → 52 % | 53.8 px | 0.49 | 1.11 | 43 |
| stroke 1393 | 56 % → 59 % | 56.3 px | 0.48 | 1.05 | 45 |
| stroke 1394 | 55 % → 55 % | 80.9 px | 0.49 | 1.00 | 20 |
| stroke 1395 | 11 % → 29 % | 14.7 px | 0.50 | 2.66 | 16 |
| stroke 1396 | 14 % → 30 % | 23.4 px | 0.50 | 2.14 | 12 |
| stroke 1397 | 31 % → 49 % | 39.6 px | 0.50 | 1.59 | 21 |
| stroke 1398 | 27 % → 38 % | 76.5 px | 0.50 | 1.39 | 4 |
| stroke 1399 | 19 % → 29 % | 22.1 px | 0.49 | 1.55 | 54 |
| stroke 1400 | 30 % → 32 % | 25.3 px | 0.51 | 1.06 | 34 |
| stroke 1401 | 25 % → 29 % | 29.6 px | 0.49 | 1.16 | 69 |
| stroke 1402 | 25 % → 25 % | 136.0 px | 0.50 | 1.00 | 3 |
| stroke 1403 | 4 % → 27 % | 10.9 px | 0.46 | 6.48 | 3 |
| stroke 1404 | 11 % → 30 % | 20.7 px | 0.46 | 2.77 | 11 |
| stroke 1405 | 13 % → 30 % | 35.3 px | 0.46 | 2.39 | 4 |
| stroke 1406 | 19 % → 38 % | 49.7 px | 0.46 | 2.01 | 6 |
| stroke 1407 | 17 % → 21 % | 19.6 px | 0.47 | 1.22 | 78 |
| stroke 1408 | 19 % → 19 % | 23.2 px | 0.46 | 1.00 | 80 |
| stroke 1409 | 7 % → 25 % | 10.3 px | 0.47 | 3.33 | 66 |
| stroke 1410 | 10 % → 24 % | 21.5 px | 0.49 | 2.42 | 6 |
| stroke 1411 | 18 % → 30 % | 30.8 px | 0.48 | 1.70 | 11 |
| stroke 1412 | 13 % → 19 % | 19.8 px | 0.48 | 1.47 | 37 |
| stroke 1413 | 21 % → 25 % | 18.9 px | 0.47 | 1.20 | 59 |
| stroke 1414 | 23 % → 23 % | 31.2 px | 0.47 | 1.00 | 42 |

Numbers say: wet paint spreads well beyond the stroke.

## Refs v3 · #39 Thick impasto weave — own sheet
own sheet 800 × 1065 · Impasto 1.00 · 96 px · 442.2 s

![Refs v3 · #39 Thick impasto weave — own sheet](Refs-v3-39-Thick-impasto-weave-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 6 % → 1 % | 76.9 px | 0.30 | 0.10 | 694 |
| stroke 2 | 15 % → 0 % | 87.8 px | 0.30 | 0.02 | 3842 |
| stroke 3 | 19 % → 1 % | 117.0 px | 0.29 | 0.03 | 5348 |
| stroke 4 | 22 % → 1 % | 140.9 px | 0.29 | 0.03 | 6804 |
| stroke 5 | 28 % → 1 % | 196.5 px | 0.29 | 0.05 | 6110 |
| stroke 6 | 38 % → 1 % | 486.7 px | 0.30 | 0.01 | 3064 |
| stroke 7 | 38 % → 0 % | 564.8 px | 0.30 | 0.01 | 2715 |
| stroke 8 | 38 % → 1 % | 557.1 px | 0.29 | 0.02 | 3080 |
| stroke 9 | 36 % → 1 % | 529.3 px | 0.30 | 0.04 | 6870 |
| stroke 10 | 34 % → 1 % | 501.1 px | 0.30 | 0.04 | 7394 |
| stroke 11 | 31 % → 1 % | 436.0 px | 0.30 | 0.04 | 3961 |
| stroke 12 | 28 % → 1 % | 433.0 px | 0.30 | 0.04 | 2499 |
| stroke 13 | 26 % → 1 % | 598.9 px | 0.30 | 0.05 | 1678 |
| stroke 14 | 41 % → 1 % | 326.1 px | 0.30 | 0.02 | 11626 |
| stroke 15 | 53 % → 1 % | 277.2 px | 0.29 | 0.02 | 12510 |
| stroke 16 | 67 % → 1 % | 365.9 px | 0.30 | 0.02 | 8801 |
| stroke 17 | 58 % → 1 % | 390.0 px | 0.30 | 0.02 | 7015 |
| stroke 18 | 45 % → 2 % | 946.8 px | 0.30 | 0.04 | 1931 |
| stroke 19 | 12 % → 1 % | 83.9 px | 0.30 | 0.05 | 3855 |
| stroke 20 | 14 % → 1 % | 269.1 px | 0.30 | 0.08 | 694 |
| stroke 21 | 21 % → 1 % | 114.7 px | 0.30 | 0.03 | 6197 |
| stroke 22 | 28 % → 1 % | 151.1 px | 0.30 | 0.02 | 7594 |
| stroke 23 | 42 % → 1 % | 243.1 px | 0.30 | 0.02 | 5563 |
| stroke 24 | 54 % → 1 % | 320.9 px | 0.30 | 0.02 | 3889 |
| stroke 25 | 63 % → 1 % | 295.3 px | 0.30 | 0.01 | 6001 |
| stroke 26 | 65 % → 1 % | 259.1 px | 0.30 | 0.01 | 6247 |
| stroke 27 | 69 % → 1 % | 235.6 px | 0.30 | 0.01 | 5952 |
| stroke 28 | 71 % → 1 % | 275.1 px | 0.30 | 0.01 | 9293 |
| stroke 29 | 64 % → 1 % | 378.9 px | 0.30 | 0.01 | 7293 |
| stroke 30 | 44 % → 1 % | 286.9 px | 0.30 | 0.01 | 7834 |
| stroke 31 | 49 % → 1 % | 375.7 px | 0.30 | 0.02 | 6862 |
| stroke 32 | 65 % → 1 % | 276.6 px | 0.30 | 0.02 | 7833 |
| stroke 33 | 9 % → 0 % | 87.1 px | 0.30 | 0.03 | 1830 |
| stroke 34 | 14 % → 0 % | 131.7 px | 0.00 | 0.00 | 2253 |
| stroke 35 | 18 % → 0 % | 178.2 px | 0.00 | 0.00 | 2313 |
| stroke 36 | 23 % → 1 % | 217.1 px | 0.30 | 0.05 | 1866 |
| stroke 37 | 28 % → 2 % | 264.8 px | 0.29 | 0.07 | 2376 |
| stroke 38 | 34 % → 2 % | 305.9 px | 0.29 | 0.07 | 1966 |
| stroke 39 | 37 % → 2 % | 302.9 px | 0.29 | 0.07 | 1845 |
| stroke 40 | 40 % → 3 % | 283.8 px | 0.29 | 0.07 | 2065 |
| stroke 41 | 48 % → 3 % | 336.7 px | 0.29 | 0.07 | 1575 |
| stroke 42 | 36 % → 2 % | 135.7 px | 0.29 | 0.04 | 7365 |
| stroke 43 | 36 % → 2 % | 252.9 px | 0.29 | 0.04 | 5087 |
| stroke 44 | 11 % → 1 % | 181.2 px | 0.29 | 0.10 | 1460 |
| stroke 45 | 6 % → 1 % | 89.4 px | 0.30 | 0.22 | 1846 |
| stroke 46 | 2 % → 0 % | 21.0 px | 0.00 | 0.00 | 81 |
| stroke 47 | 4 % → 1 % | 96.8 px | 0.30 | 0.36 | 673 |
| stroke 48 | 8 % → 1 % | 109.3 px | 0.30 | 0.12 | 2165 |
| stroke 49 | 12 % → 1 % | 121.8 px | 0.30 | 0.09 | 3604 |
| stroke 50 | 18 % → 1 % | 143.5 px | 0.30 | 0.06 | 4087 |
| stroke 51 | 23 % → 1 % | 179.2 px | 0.30 | 0.05 | 4661 |
| stroke 52 | 28 % → 1 % | 221.7 px | 0.30 | 0.04 | 5383 |
| stroke 53 | 35 % → 0 % | 481.3 px | 0.30 | 0.01 | 2372 |
| stroke 54 | 53 % → 0 % | 692.8 px | 0.00 | 0.00 | 1387 |
| stroke 55 | 35 % → 1 % | 489.9 px | 0.29 | 0.04 | 2271 |
| stroke 56 | 33 % → 2 % | 452.6 px | 0.29 | 0.05 | 2316 |
| stroke 57 | 32 % → 2 % | 397.1 px | 0.29 | 0.05 | 2293 |
| stroke 58 | 32 % → 2 % | 353.8 px | 0.29 | 0.06 | 2531 |
| stroke 59 | 33 % → 2 % | 385.9 px | 0.29 | 0.07 | 1970 |
| stroke 60 | 37 % → 3 % | 435.5 px | 0.29 | 0.07 | 1938 |
| stroke 61 | 42 % → 3 % | 680.5 px | 0.29 | 0.08 | 1014 |
| stroke 62 | 54 % → 1 % | 272.5 px | 0.30 | 0.02 | 7122 |
| stroke 63 | 52 % → 2 % | 324.3 px | 0.29 | 0.04 | 8775 |
| stroke 64 | 40 % → 2 % | 290.5 px | 0.29 | 0.04 | 7463 |
| stroke 65 | 48 % → 1 % | 1084.4 px | 0.30 | 0.03 | 1087 |
| stroke 66 | 9 % → 0 % | 87.9 px | 0.29 | 0.00 | 2509 |
| stroke 67 | 15 % → 1 % | 124.9 px | 0.30 | 0.04 | 2776 |
| stroke 68 | 24 % → 0 % | 229.0 px | 0.00 | 0.00 | 2183 |
| stroke 69 | 20 % → 0 % | 99.8 px | 0.29 | 0.00 | 6010 |
| stroke 70 | 29 % → 0 % | 509.3 px | 0.00 | 0.00 | 1308 |
| stroke 71 | 2 % → 2 % | 29.1 px | 0.29 | 0.87 | 225 |
| stroke 72 | 3 % → 2 % | 44.0 px | 0.29 | 0.59 | 304 |
| stroke 73 | 4 % → 2 % | 136.4 px | 0.29 | 0.45 | 120 |
| stroke 74 | 6 % → 2 % | 190.0 px | 0.29 | 0.43 | 90 |
| stroke 75 | 5 % → 2 % | 209.6 px | 0.29 | 0.34 | 128 |
| stroke 76 | 5 % → 1 % | 188.3 px | 0.29 | 0.28 | 120 |
| stroke 77 | 5 % → 1 % | 361.8 px | 0.29 | 0.23 | 74 |
| stroke 78 | 7 % → 2 % | 66.4 px | 0.29 | 0.30 | 879 |
| stroke 79 | 8 % → 2 % | 483.2 px | 0.29 | 0.30 | 56 |
| stroke 80 | 1 % → 0 % | 30.2 px | 0.00 | 0.00 | 87 |
| stroke 81 | 7 % → 0 % | 39.0 px | 0.30 | 0.06 | 742 |
| stroke 82 | 8 % → 0 % | 50.1 px | 0.30 | 0.05 | 1259 |
| stroke 83 | 10 % → 0 % | 60.1 px | 0.30 | 0.04 | 916 |
| stroke 84 | 13 % → 0 % | 196.6 px | 0.00 | 0.00 | 349 |
| stroke 85 | 13 % → 0 % | 133.1 px | 0.00 | 0.00 | 794 |
| stroke 86 | 13 % → 0 % | 137.3 px | 0.30 | 0.02 | 488 |
| stroke 87 | 17 % → 1 % | 162.1 px | 0.30 | 0.04 | 560 |
| stroke 88 | 14 % → 0 % | 145.9 px | 0.30 | 0.01 | 420 |
| stroke 89 | 15 % → 0 % | 137.3 px | 0.00 | 0.00 | 492 |
| stroke 90 | 18 % → 0 % | 662.1 px | 0.00 | 0.00 | 87 |
| stroke 91 | 9 % → 0 % | 498.6 px | 0.30 | 0.05 | 71 |
| stroke 92 | 10 % → 0 % | 298.3 px | 0.30 | 0.04 | 156 |
| stroke 93 | 9 % → 0 % | 247.7 px | 0.30 | 0.04 | 187 |
| stroke 94 | 9 % → 0 % | 647.7 px | 0.00 | 0.00 | 29 |
| stroke 95 | 10 % → 1 % | 131.3 px | 0.29 | 0.09 | 521 |
| stroke 96 | 10 % → 0 % | 369.0 px | 0.30 | 0.04 | 123 |
| stroke 97 | 10 % → 1 % | 154.6 px | 0.30 | 0.07 | 342 |
| stroke 98 | 11 % → 0 % | 576.2 px | 0.00 | 0.00 | 38 |
| stroke 99 | 11 % → 0 % | 176.4 px | 0.00 | 0.00 | 219 |
| stroke 100 | 11 % → 0 % | 264.6 px | 0.00 | 0.00 | 128 |
| stroke 101 | 14 % → 0 % | 216.9 px | 0.30 | 0.03 | 516 |
| stroke 102 | 14 % → 0 % | 338.1 px | 0.30 | 0.02 | 295 |
| stroke 103 | 12 % → 0 % | 145.9 px | 0.30 | 0.03 | 475 |
| stroke 104 | 13 % → 0 % | 165.4 px | 0.30 | 0.03 | 665 |
| stroke 105 | 13 % → 0 % | 228.9 px | 0.00 | 0.00 | 337 |
| stroke 106 | 8 % → 1 % | 469.6 px | 0.30 | 0.15 | 69 |
| stroke 107 | 9 % → 1 % | 359.0 px | 0.30 | 0.15 | 128 |
| stroke 108 | 9 % → 1 % | 374.3 px | 0.30 | 0.13 | 246 |
| stroke 109 | 1 % → 0 % | 28.2 px | 0.29 | 0.09 | 116 |
| stroke 110 | 3 % → 1 % | 32.2 px | 0.30 | 0.33 | 359 |
| stroke 111 | 4 % → 1 % | 61.2 px | 0.30 | 0.27 | 325 |
| stroke 112 | 8 % → 0 % | 109.3 px | 0.00 | 0.00 | 165 |
| stroke 113 | 6 % → 1 % | 191.8 px | 0.29 | 0.10 | 160 |
| stroke 114 | 10 % → 0 % | 317.7 px | 0.00 | 0.00 | 69 |
| stroke 115 | 6 % → 1 % | 237.7 px | 0.30 | 0.19 | 221 |
| stroke 116 | 6 % → 1 % | 74.6 px | 0.29 | 0.09 | 499 |
| stroke 117 | 6 % → 1 % | 85.4 px | 0.30 | 0.13 | 500 |
| stroke 118 | 11 % → 0 % | 304.0 px | 0.00 | 0.00 | 108 |
| stroke 119 | 6 % → 1 % | 254.3 px | 0.30 | 0.16 | 86 |
| stroke 120 | 6 % → 1 % | 166.6 px | 0.30 | 0.22 | 208 |
| stroke 121 | 7 % → 1 % | 177.8 px | 0.30 | 0.22 | 189 |
| stroke 122 | 7 % → 2 % | 529.4 px | 0.30 | 0.25 | 60 |
| stroke 123 | 8 % → 2 % | 289.2 px | 0.30 | 0.19 | 247 |
| stroke 124 | 8 % → 1 % | 199.8 px | 0.30 | 0.16 | 274 |
| stroke 125 | 12 % → 0 % | 512.2 px | 0.00 | 0.00 | 40 |
| stroke 126 | 12 % → 0 % | 321.5 px | 0.00 | 0.00 | 94 |
| stroke 127 | 13 % → 0 % | 360.6 px | 0.00 | 0.00 | 358 |
| stroke 128 | 6 % → 2 % | 220.1 px | 0.30 | 0.24 | 101 |
| stroke 129 | 6 % → 2 % | 257.8 px | 0.30 | 0.26 | 104 |
| stroke 130 | 11 % → 0 % | 759.8 px | 0.00 | 0.00 | 37 |
| stroke 131 | 8 % → 1 % | 117.0 px | 0.30 | 0.16 | 468 |
| stroke 132 | 14 % → 0 % | 145.0 px | 0.29 | 0.01 | 374 |
| stroke 133 | 11 % → 1 % | 168.5 px | 0.30 | 0.13 | 300 |
| stroke 134 | 18 % → 0 % | 287.9 px | 0.00 | 0.00 | 177 |
| stroke 135 | 14 % → 1 % | 286.4 px | 0.29 | 0.04 | 235 |
| stroke 136 | 11 % → 1 % | 258.2 px | 0.30 | 0.13 | 188 |
| stroke 137 | 17 % → 0 % | 278.8 px | 0.29 | 0.00 | 300 |
| stroke 138 | 12 % → 1 % | 180.2 px | 0.30 | 0.11 | 500 |
| stroke 139 | 13 % → 1 % | 191.3 px | 0.30 | 0.10 | 529 |
| stroke 140 | 11 % → 2 % | 369.6 px | 0.30 | 0.14 | 318 |
| stroke 141 | 7 % → 2 % | 380.1 px | 0.30 | 0.23 | 46 |
| stroke 142 | 9 % → 2 % | 304.9 px | 0.30 | 0.20 | 131 |
| stroke 143 | 10 % → 2 % | 310.9 px | 0.30 | 0.15 | 136 |
| stroke 144 | 12 % → 1 % | 278.9 px | 0.30 | 0.12 | 201 |
| stroke 145 | 11 % → 2 % | 170.8 px | 0.30 | 0.16 | 572 |
| stroke 146 | 10 % → 2 % | 399.7 px | 0.30 | 0.19 | 208 |
| stroke 147 | 4 % → 1 % | 105.9 px | 0.30 | 0.32 | 237 |
| stroke 148 | 5 % → 1 % | 408.8 px | 0.30 | 0.22 | 47 |
| stroke 149 | 6 % → 2 % | 243.4 px | 0.30 | 0.34 | 172 |
| stroke 150 | 5 % → 1 % | 235.1 px | 0.30 | 0.25 | 151 |
| stroke 151 | 2 % → 4 % | 22.5 px | 0.29 | 1.94 | 129 |
| stroke 152 | 5 % → 5 % | 65.5 px | 0.29 | 0.96 | 72 |
| stroke 153 | 1 % → 1 % | 46.6 px | 0.30 | 0.95 | 42 |
| stroke 154 | 1 % → 1 % | 21.3 px | 0.30 | 0.95 | 157 |
| stroke 155 | 1 % → 1 % | 21.7 px | 0.30 | 0.97 | 170 |

Numbers say: wet paint spreads well beyond the stroke.

## Refs v3 · #40 Watercolour blooms — own sheet
own sheet 800 × 1170 · Watercolour 1.00 + water 55 % · 112 px · 1326.0 s

![Refs v3 · #40 Watercolour blooms — own sheet](Refs-v3-40-Watercolour-blooms-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 11 % → 99 % | 117.4 px | 0.14 | 8.72 | 4519 |
| stroke 2 | 18 % → 93 % | 268.3 px | 0.11 | 5.01 | 3650 |
| stroke 3 | 16 % → 54 % | 238.6 px | 0.07 | 3.39 | 4001 |
| stroke 4 | 25 % → 100 % | 147.7 px | 0.20 | 3.97 | 8443 |
| stroke 5 | 45 % → 93 % | 306.7 px | 0.08 | 2.06 | 8043 |
| stroke 6 | 53 % → 97 % | 686.6 px | 0.07 | 1.83 | 15760 |
| stroke 7 | 44 % → 79 % | 527.9 px | 0.07 | 1.80 | 8143 |
| stroke 8 | 63 % → 99 % | 687.4 px | 0.10 | 1.59 | 9789 |
| stroke 9 | 70 % → 98 % | 710.9 px | 0.06 | 1.40 | 11767 |
| stroke 10 | 55 % → 99 % | 868.3 px | 0.15 | 1.81 | 3868 |
| stroke 11 | 39 % → 67 % | 552.8 px | 0.07 | 1.74 | 5774 |
| stroke 12 | 54 % → 94 % | 1424.1 px | 0.12 | 1.73 | 1347 |
| stroke 13 | 79 % → 99 % | 898.0 px | 0.09 | 1.25 | 6050 |
| stroke 14 | 45 % → 100 % | 696.5 px | 0.18 | 2.23 | 1839 |
| stroke 15 | 56 % → 98 % | 720.7 px | 0.15 | 1.75 | 5115 |
| stroke 16 | 80 % → 99 % | 1620.5 px | 0.09 | 1.23 | 2882 |
| stroke 17 | 59 % → 100 % | 1106.1 px | 0.17 | 1.69 | 4010 |
| stroke 18 | 66 % → 99 % | 1203.3 px | 0.15 | 1.51 | 3400 |
| stroke 19 | 80 % → 99 % | 1645.9 px | 0.09 | 1.24 | 2650 |
| stroke 20 | 32 % → 50 % | 483.0 px | 0.07 | 1.54 | 4810 |
| stroke 21 | 50 % → 66 % | 1086.2 px | 0.06 | 1.31 | 3612 |
| stroke 22 | 84 % → 100 % | 1008.2 px | 0.08 | 1.19 | 2006 |
| stroke 23 | 89 % → 98 % | 2232.0 px | 0.08 | 1.11 | 2287 |
| stroke 24 | 68 % → 98 % | 664.0 px | 0.12 | 1.44 | 13641 |
| stroke 25 | 57 % → 100 % | 448.0 px | 0.17 | 1.73 | 15885 |
| stroke 26 | 72 % → 100 % | 454.6 px | 0.13 | 1.39 | 11355 |
| stroke 27 | 77 % → 97 % | 534.4 px | 0.08 | 1.27 | 10122 |
| stroke 28 | 64 % → 92 % | 709.3 px | 0.11 | 1.44 | 5374 |
| stroke 29 | 41 % → 58 % | 330.2 px | 0.07 | 1.41 | 12365 |
| stroke 30 | 51 % → 64 % | 1359.2 px | 0.06 | 1.25 | 2493 |
| stroke 31 | 11 % → 100 % | 133.2 px | 0.29 | 9.07 | 1941 |
| stroke 32 | 38 % → 56 % | 1841.8 px | 0.07 | 1.45 | 74 |
| stroke 33 | 34 % → 54 % | 537.5 px | 0.07 | 1.57 | 171 |
| stroke 34 | 54 % → 100 % | 1801.1 px | 0.19 | 1.86 | 650 |
| stroke 35 | 63 % → 100 % | 686.4 px | 0.16 | 1.58 | 1806 |
| stroke 36 | 56 % → 100 % | 812.4 px | 0.19 | 1.79 | 955 |
| stroke 37 | 53 % → 100 % | 1061.9 px | 0.20 | 1.88 | 1800 |
| stroke 38 | 60 % → 100 % | 1445.0 px | 0.18 | 1.68 | 700 |
| stroke 39 | 54 % → 100 % | 960.7 px | 0.20 | 1.85 | 583 |
| stroke 40 | 64 % → 100 % | 1189.7 px | 0.17 | 1.55 | 840 |
| stroke 41 | 65 % → 100 % | 1873.7 px | 0.17 | 1.53 | 669 |
| stroke 42 | 57 % → 100 % | 376.8 px | 0.20 | 1.77 | 3614 |
| stroke 43 | 68 % → 100 % | 923.7 px | 0.17 | 1.47 | 1243 |
| stroke 44 | 65 % → 100 % | 790.8 px | 0.18 | 1.53 | 1967 |
| stroke 45 | 65 % → 100 % | 562.3 px | 0.19 | 1.53 | 546 |
| stroke 46 | 85 % → 100 % | 745.5 px | 0.11 | 1.17 | 2825 |
| stroke 47 | 83 % → 100 % | 586.3 px | 0.16 | 1.21 | 1935 |
| stroke 48 | 85 % → 100 % | 1047.3 px | 0.16 | 1.17 | 1174 |
| stroke 49 | 90 % → 100 % | 1253.8 px | 0.11 | 1.11 | 1452 |
| stroke 50 | 83 % → 100 % | 1724.8 px | 0.18 | 1.21 | 340 |
| stroke 51 | 81 % → 100 % | 1165.5 px | 0.21 | 1.24 | 528 |
| stroke 52 | 87 % → 100 % | 1746.7 px | 0.18 | 1.15 | 372 |
| stroke 53 | 89 % → 100 % | 509.5 px | 0.15 | 1.12 | 2555 |
| stroke 54 | 88 % → 100 % | 365.5 px | 0.16 | 1.14 | 4326 |
| stroke 55 | 84 % → 100 % | 1490.0 px | 0.19 | 1.20 | 404 |
| stroke 56 | 90 % → 100 % | 2568.5 px | 0.13 | 1.10 | 743 |
| stroke 57 | 92 % → 100 % | 684.5 px | 0.11 | 1.09 | 3244 |
| stroke 58 | 89 % → 100 % | 1578.4 px | 0.13 | 1.12 | 676 |
| stroke 59 | 56 % → 87 % | 915.0 px | 0.12 | 1.56 | 2589 |
| stroke 60 | 42 % → 65 % | 1045.8 px | 0.09 | 1.55 | 896 |
| stroke 61 | 46 % → 67 % | 1766.7 px | 0.08 | 1.46 | 1053 |
| stroke 62 | 52 % → 85 % | 2264.2 px | 0.13 | 1.65 | 547 |
| stroke 63 | 55 % → 93 % | 2136.8 px | 0.15 | 1.68 | 914 |
| stroke 64 | 73 % → 98 % | 3137.7 px | 0.13 | 1.34 | 653 |
| stroke 65 | 45 % → 62 % | 1605.3 px | 0.08 | 1.37 | 605 |
| stroke 66 | 65 % → 92 % | 2817.6 px | 0.12 | 1.41 | 550 |
| stroke 67 | 44 % → 70 % | 557.9 px | 0.12 | 1.59 | 3403 |
| stroke 68 | 62 % → 90 % | 658.4 px | 0.13 | 1.45 | 3754 |
| stroke 69 | 47 % → 68 % | 886.4 px | 0.10 | 1.45 | 2278 |
| stroke 70 | 75 % → 82 % | 688.7 px | 0.05 | 1.10 | 2885 |
| stroke 71 | 76 % → 85 % | 934.1 px | 0.05 | 1.12 | 1573 |
| stroke 72 | 66 % → 76 % | 1202.3 px | 0.06 | 1.15 | 794 |
| stroke 73 | 77 % → 83 % | 2154.1 px | 0.06 | 1.08 | 906 |
| stroke 74 | 61 % → 65 % | 908.8 px | 0.06 | 1.07 | 1621 |
| stroke 75 | 66 % → 70 % | 844.5 px | 0.06 | 1.06 | 1479 |
| stroke 76 | 61 % → 64 % | 880.7 px | 0.06 | 1.05 | 1189 |
| stroke 77 | 75 % → 77 % | 1991.9 px | 0.06 | 1.03 | 1285 |
| stroke 78 | 55 % → 57 % | 1835.0 px | 0.06 | 1.04 | 530 |
| stroke 79 | 90 % → 93 % | 2156.8 px | 0.06 | 1.03 | 668 |
| stroke 80 | 82 % → 84 % | 2485.2 px | 0.05 | 1.03 | 711 |
| stroke 81 | 67 % → 69 % | 2112.1 px | 0.06 | 1.03 | 818 |
| stroke 82 | 53 % → 56 % | 943.1 px | 0.07 | 1.04 | 710 |
| stroke 83 | 64 % → 65 % | 661.0 px | 0.06 | 1.02 | 3156 |
| stroke 84 | 83 % → 85 % | 753.3 px | 0.06 | 1.02 | 3387 |
| stroke 85 | 79 % → 80 % | 520.0 px | 0.06 | 1.01 | 4040 |
| stroke 86 | 62 % → 63 % | 698.8 px | 0.07 | 1.01 | 1641 |
| stroke 87 | 96 % → 100 % | 1120.1 px | 0.08 | 1.04 | 217 |
| stroke 88 | 70 % → 98 % | 6169.8 px | 0.15 | 1.39 | 52 |
| stroke 89 | 68 % → 100 % | 346.8 px | 0.21 | 1.47 | 6973 |
| stroke 90 | 76 % → 100 % | 717.4 px | 0.21 | 1.31 | 5266 |
| stroke 91 | 89 % → 100 % | 615.3 px | 0.27 | 1.13 | 6647 |
| stroke 92 | 81 % → 100 % | 716.9 px | 0.22 | 1.23 | 7260 |
| stroke 93 | 70 % → 100 % | 819.9 px | 0.29 | 1.42 | 3294 |
| stroke 94 | 77 % → 100 % | 1297.3 px | 0.21 | 1.30 | 5764 |
| stroke 95 | 78 % → 100 % | 368.4 px | 0.21 | 1.29 | 14664 |
| stroke 96 | 78 % → 100 % | 538.3 px | 0.21 | 1.28 | 8856 |
| stroke 97 | 65 % → 99 % | 657.3 px | 0.24 | 1.52 | 5735 |
| stroke 98 | 50 % → 99 % | 1539.7 px | 0.24 | 1.97 | 958 |
| stroke 99 | 78 % → 100 % | 1197.1 px | 0.21 | 1.29 | 4277 |
| stroke 100 | 78 % → 100 % | 1088.1 px | 0.22 | 1.28 | 4657 |
| stroke 101 | 45 % → 79 % | 721.4 px | 0.16 | 1.77 | 1399 |
| stroke 102 | 75 % → 95 % | 578.7 px | 0.25 | 1.28 | 6046 |
| stroke 103 | 70 % → 89 % | 725.1 px | 0.21 | 1.28 | 3366 |
| stroke 104 | 95 % → 100 % | 2039.9 px | 0.27 | 1.05 | 1545 |
| stroke 105 | 74 % → 90 % | 723.0 px | 0.23 | 1.22 | 3630 |
| stroke 106 | 88 % → 99 % | 743.6 px | 0.23 | 1.12 | 3236 |
| stroke 107 | 99 % → 100 % | 1226.9 px | 0.29 | 1.01 | 1670 |
| stroke 108 | 79 % → 87 % | 1011.5 px | 0.19 | 1.11 | 3820 |
| stroke 109 | 98 % → 100 % | 1097.9 px | 0.28 | 1.02 | 2822 |
| stroke 110 | 91 % → 100 % | 1875.7 px | 0.26 | 1.10 | 1418 |
| stroke 111 | 93 % → 100 % | 1457.6 px | 0.26 | 1.07 | 2090 |
| stroke 112 | 69 % → 82 % | 1243.8 px | 0.17 | 1.18 | 1408 |
| stroke 113 | 83 % → 91 % | 512.6 px | 0.23 | 1.10 | 20207 |
| stroke 114 | 85 % → 93 % | 655.2 px | 0.23 | 1.09 | 9027 |
| stroke 115 | 74 % → 86 % | 2508.0 px | 0.19 | 1.16 | 825 |
| stroke 116 | 99 % → 100 % | 2375.0 px | 0.20 | 1.01 | 1762 |
| stroke 117 | 79 % → 83 % | 1529.8 px | 0.13 | 1.06 | 2117 |
| stroke 118 | 76 % → 81 % | 2218.5 px | 0.12 | 1.07 | 1377 |
| stroke 119 | 84 % → 88 % | 1751.3 px | 0.15 | 1.05 | 2083 |
| stroke 120 | 80 % → 85 % | 1270.5 px | 0.14 | 1.05 | 2676 |
| stroke 121 | 86 % → 86 % | 1409.8 px | 0.06 | 1.00 | 1982 |
| stroke 122 | 100 % → 100 % | 2163.0 px | 0.26 | 1.00 | 36 |
| stroke 123 | 98 % → 100 % | 673.9 px | 0.12 | 1.02 | 3518 |
| stroke 124 | 100 % → 100 % | 696.5 px | 0.14 | 1.00 | 4722 |
| stroke 125 | 100 % → 100 % | 759.6 px | 0.13 | 1.00 | 3674 |
| stroke 126 | 100 % → 100 % | 2325.6 px | 0.14 | 1.00 | 1119 |
| stroke 127 | 100 % → 100 % | 644.8 px | 0.12 | 1.00 | 8397 |
| stroke 128 | 100 % → 100 % | 670.2 px | 0.13 | 1.00 | 4039 |
| stroke 129 | 94 % → 97 % | 1242.0 px | 0.16 | 1.03 | 3474 |
| stroke 130 | 96 % → 97 % | 1094.8 px | 0.20 | 1.01 | 4701 |
| stroke 131 | 96 % → 97 % | 1731.2 px | 0.17 | 1.00 | 2292 |
| stroke 132 | 99 % → 100 % | 1412.0 px | 0.23 | 1.00 | 8458 |
| stroke 133 | 100 % → 100 % | 1422.9 px | 0.22 | 1.00 | 5537 |
| stroke 134 | 99 % → 99 % | 3023.5 px | 0.20 | 1.00 | 1061 |
| stroke 135 | 95 % → 96 % | 2726.2 px | 0.17 | 1.00 | 1088 |
| stroke 136 | 100 % → 100 % | 2180.3 px | 0.22 | 1.00 | 1601 |
| stroke 137 | 97 % → 97 % | 3168.9 px | 0.19 | 1.00 | 769 |
| stroke 138 | 100 % → 100 % | 2068.2 px | 0.24 | 1.00 | 1266 |
| stroke 139 | 100 % → 100 % | 3130.5 px | 0.25 | 1.00 | 607 |
| stroke 140 | 96 % → 96 % | 1138.5 px | 0.17 | 1.00 | 4146 |
| stroke 141 | 100 % → 100 % | 966.7 px | 0.21 | 1.00 | 4986 |
| stroke 142 | 100 % → 100 % | 883.4 px | 0.23 | 1.00 | 4948 |
| stroke 143 | 100 % → 100 % | 1022.0 px | 0.19 | 1.00 | 6656 |
| stroke 144 | 96 % → 97 % | 1978.1 px | 0.16 | 1.00 | 2883 |

Numbers say: wet paint spreads well beyond the stroke.

## Refs v3 · #41 Coloured pencil — own sheet
own sheet 800 × 1108 · Charcoal 0.50 · Pastel 0.50 · 12 px · 468.2 s

![Refs v3 · #41 Coloured pencil — own sheet](Refs-v3-41-Coloured-pencil-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 6 % → 0 % | 9.7 px | 0.00 | 0.00 | 159 |
| stroke 2 | 7 % → 0 % | 9.4 px | 0.00 | 0.00 | 31 |
| stroke 3 | 9 % → 0 % | 14.2 px | 0.00 | 0.00 | 11 |
| stroke 4 | 10 % → 0 % | 12.6 px | 0.00 | 0.00 | 28 |
| stroke 5 | 13 % → 0 % | 22.1 px | 0.00 | 0.00 | 17 |
| stroke 6 | 9 % → 0 % | 9.5 px | 0.00 | 0.00 | 34 |
| stroke 7 | 24 % → 0 % | 32.5 px | 0.00 | 0.00 | 29 |
| stroke 8 | 16 % → 0 % | 23.2 px | 0.00 | 0.00 | 18 |
| stroke 9 | 28 % → 0 % | 42.7 px | 0.00 | 0.00 | 12 |
| stroke 10 | 17 % → 1 % | 20.2 px | 0.14 | 0.04 | 24 |
| stroke 11 | 19 % → 0 % | 30.3 px | 0.00 | 0.00 | 20 |
| stroke 12 | 20 % → 0 % | 26.9 px | 0.00 | 0.00 | 17 |
| stroke 13 | 11 % → 0 % | 19.2 px | 0.00 | 0.00 | 16 |
| stroke 14 | 23 % → 0 % | 34.6 px | 0.00 | 0.00 | 12 |
| stroke 15 | 20 % → 0 % | 29.1 px | 0.14 | 0.02 | 19 |
| stroke 16 | 37 % → 0 % | 55.1 px | 0.00 | 0.00 | 23 |
| stroke 17 | 24 % → 0 % | 42.8 px | 0.00 | 0.00 | 11 |
| stroke 18 | 24 % → 0 % | 26.8 px | 0.00 | 0.00 | 27 |
| stroke 19 | 19 % → 0 % | 30.1 px | 0.00 | 0.00 | 11 |
| stroke 20 | 28 % → 0 % | 45.0 px | 0.00 | 0.00 | 21 |
| stroke 21 | 18 % → 13 % | 24.1 px | 0.16 | 0.75 | 14 |
| stroke 22 | 31 % → 0 % | 44.2 px | 0.00 | 0.00 | 19 |
| stroke 23 | 43 % → 0 % | 67.7 px | 0.00 | 0.00 | 15 |
| stroke 24 | 34 % → 0 % | 63.3 px | 0.00 | 0.00 | 10 |
| stroke 25 | 15 % → 10 % | 21.6 px | 0.15 | 0.71 | 13 |
| stroke 26 | 50 % → 0 % | 59.7 px | 0.00 | 0.00 | 17 |
| stroke 27 | 31 % → 0 % | 83.0 px | 0.00 | 0.00 | 3 |
| stroke 28 | 40 % → 0 % | 59.4 px | 0.00 | 0.00 | 12 |
| stroke 29 | 48 % → 0 % | 85.1 px | 0.00 | 0.00 | 16 |
| stroke 30 | 46 % → 0 % | 128.0 px | 0.00 | 0.00 | 7 |
| stroke 31 | 22 % → 0 % | 32.9 px | 0.00 | 0.00 | 30 |
| stroke 32 | 35 % → 0 % | 55.9 px | 0.00 | 0.00 | 24 |
| stroke 33 | 58 % → 0 % | 165.3 px | 0.00 | 0.00 | 4 |
| stroke 34 | 27 % → 0 % | 43.2 px | 0.00 | 0.00 | 16 |
| stroke 35 | 36 % → 0 % | 83.0 px | 0.00 | 0.00 | 11 |
| stroke 36 | 30 % → 0 % | 52.6 px | 0.00 | 0.00 | 15 |
| stroke 37 | 30 % → 0 % | 82.9 px | 0.00 | 0.00 | 7 |
| stroke 38 | 37 % → 0 % | 70.2 px | 0.00 | 0.00 | 11 |
| stroke 39 | 18 % → 36 % | 50.3 px | 0.17 | 2.00 | 7 |
| stroke 40 | 48 % → 1 % | 116.3 px | 0.14 | 0.02 | 4 |
| stroke 41 | 25 % → 0 % | 57.5 px | 0.00 | 0.00 | 7 |
| stroke 42 | 45 % → 0 % | 90.0 px | 0.00 | 0.00 | 14 |
| stroke 43 | 55 % → 0 % | 121.7 px | 0.00 | 0.00 | 10 |
| stroke 44 | 41 % → 0 % | 114.1 px | 0.00 | 0.00 | 3 |
| stroke 45 | 48 % → 0 % | 122.5 px | 0.00 | 0.00 | 5 |
| stroke 46 | 29 % → 0 % | 82.1 px | 0.00 | 0.00 | 13 |
| stroke 47 | 50 % → 0 % | 82.4 px | 0.00 | 0.00 | 14 |
| stroke 48 | 46 % → 0 % | 130.7 px | 0.00 | 0.00 | 3 |
| stroke 49 | 20 % → 0 % | 55.3 px | 0.00 | 0.00 | 3 |
| stroke 50 | 34 % → 0 % | 79.9 px | 0.00 | 0.00 | 6 |
| stroke 51 | 55 % → 0 % | 155.3 px | 0.00 | 0.00 | 4 |
| stroke 52 | 30 % → 16 % | 36.9 px | 0.17 | 0.54 | 36 |
| stroke 53 | 41 % → 3 % | 41.1 px | 0.16 | 0.08 | 35 |
| stroke 54 | 40 % → 0 % | 51.7 px | 0.00 | 0.00 | 47 |
| stroke 55 | 39 % → 0 % | 57.2 px | 0.00 | 0.00 | 47 |
| stroke 56 | 36 % → 0 % | 45.6 px | 0.00 | 0.00 | 38 |
| stroke 57 | 42 % → 0 % | 36.0 px | 0.00 | 0.00 | 35 |
| stroke 58 | 33 % → 0 % | 34.6 px | 0.00 | 0.00 | 39 |
| stroke 59 | 32 % → 0 % | 44.9 px | 0.00 | 0.00 | 35 |
| stroke 60 | 37 % → 0 % | 53.2 px | 0.00 | 0.00 | 33 |
| stroke 61 | 39 % → 0 % | 45.4 px | 0.00 | 0.00 | 45 |
| stroke 62 | 30 % → 1 % | 37.1 px | 0.14 | 0.04 | 30 |
| stroke 63 | 10 % → 0 % | 10.6 px | 0.00 | 0.00 | 26 |
| stroke 64 | 10 % → 0 % | 13.8 px | 0.00 | 0.00 | 27 |
| stroke 65 | 19 % → 0 % | 21.3 px | 0.00 | 0.00 | 22 |
| stroke 66 | 10 % → 0 % | 15.5 px | 0.00 | 0.00 | 31 |
| stroke 67 | 6 % → 0 % | 9.0 px | 0.00 | 0.00 | 27 |
| stroke 68 | 15 % → 0 % | 19.8 px | 0.00 | 0.00 | 23 |
| stroke 69 | 18 % → 0 % | 29.5 px | 0.00 | 0.00 | 14 |
| stroke 70 | 7 % → 0 % | 18.5 px | 0.00 | 0.00 | 2 |
| stroke 71 | 31 % → 0 % | 50.3 px | 0.00 | 0.00 | 13 |
| stroke 72 | 21 % → 0 % | 33.7 px | 0.00 | 0.00 | 12 |
| stroke 73 | 6 % → 2 % | 8.9 px | 0.21 | 0.25 | 17 |
| stroke 74 | 18 % → 0 % | 24.0 px | 0.00 | 0.00 | 22 |
| stroke 75 | 23 % → 1 % | 32.2 px | 0.19 | 0.05 | 20 |
| stroke 76 | 18 % → 0 % | 30.4 px | 0.00 | 0.00 | 11 |
| stroke 77 | 19 % → 5 % | 28.9 px | 0.19 | 0.29 | 18 |
| stroke 78 | 33 % → 0 % | 56.4 px | 0.00 | 0.00 | 11 |
| stroke 79 | 26 % → 0 % | 30.2 px | 0.00 | 0.00 | 41 |
| stroke 80 | 31 % → 0 % | 67.7 px | 0.00 | 0.00 | 6 |
| stroke 81 | 22 % → 0 % | 28.1 px | 0.00 | 0.00 | 43 |
| stroke 82 | 19 % → 0 % | 29.5 px | 0.00 | 0.00 | 38 |
| stroke 83 | 32 % → 0 % | 52.3 px | 0.00 | 0.00 | 13 |
| stroke 84 | 41 % → 0 % | 59.3 px | 0.00 | 0.00 | 38 |
| stroke 85 | 30 % → 0 % | 56.2 px | 0.00 | 0.00 | 9 |
| stroke 86 | 44 % → 0 % | 62.3 px | 0.00 | 0.00 | 15 |
| stroke 87 | 24 % → 0 % | 35.1 px | 0.00 | 0.00 | 31 |
| stroke 88 | 51 % → 0 % | 104.3 px | 0.00 | 0.00 | 7 |
| stroke 89 | 39 % → 0 % | 96.0 px | 0.00 | 0.00 | 6 |
| stroke 90 | 51 % → 0 % | 97.2 px | 0.00 | 0.00 | 11 |
| stroke 91 | 36 % → 0 % | 58.4 px | 0.00 | 0.00 | 26 |
| stroke 92 | 38 % → 0 % | 59.5 px | 0.00 | 0.00 | 17 |
| stroke 93 | 50 % → 0 % | 97.0 px | 0.00 | 0.00 | 9 |
| stroke 94 | 42 % → 0 % | 116.0 px | 0.00 | 0.00 | 19 |
| stroke 95 | 55 % → 0 % | 66.8 px | 0.00 | 0.00 | 27 |
| stroke 96 | 42 % → 0 % | 77.3 px | 0.00 | 0.00 | 11 |
| stroke 97 | 39 % → 0 % | 113.1 px | 0.00 | 0.00 | 14 |
| stroke 98 | 55 % → 0 % | 88.6 px | 0.00 | 0.00 | 24 |
| stroke 99 | 61 % → 0 % | 132.6 px | 0.00 | 0.00 | 6 |
| stroke 100 | 18 % → 0 % | 35.8 px | 0.00 | 0.00 | 10 |
| stroke 101 | 39 % → 0 % | 75.7 px | 0.00 | 0.00 | 7 |
| stroke 102 | 56 % → 0 % | 126.7 px | 0.00 | 0.00 | 46 |
| stroke 103 | 32 % → 0 % | 87.6 px | 0.00 | 0.00 | 7 |
| stroke 104 | 29 % → 0 % | 50.9 px | 0.00 | 0.00 | 23 |
| stroke 105 | 26 % → 0 % | 72.5 px | 0.00 | 0.00 | 6 |
| stroke 106 | 34 % → 0 % | 64.6 px | 0.00 | 0.00 | 7 |
| stroke 107 | 21 % → 0 % | 56.3 px | 0.00 | 0.00 | 7 |
| stroke 108 | 56 % → 0 % | 157.2 px | 0.00 | 0.00 | 3 |
| stroke 109 | 56 % → 0 % | 137.8 px | 0.00 | 0.00 | 14 |
| stroke 110 | 42 % → 1 % | 51.6 px | 0.21 | 0.02 | 53 |
| stroke 111 | 38 % → 0 % | 42.2 px | 0.00 | 0.00 | 39 |
| stroke 112 | 44 % → 0 % | 50.6 px | 0.00 | 0.00 | 88 |
| stroke 113 | 38 % → 0 % | 56.0 px | 0.00 | 0.00 | 41 |
| stroke 114 | 33 % → 0 % | 42.2 px | 0.00 | 0.00 | 53 |
| stroke 115 | 31 % → 0 % | 32.5 px | 0.00 | 0.00 | 59 |
| stroke 116 | 39 % → 0 % | 55.3 px | 0.00 | 0.00 | 56 |
| stroke 117 | 50 % → 0 % | 50.2 px | 0.00 | 0.00 | 60 |
| stroke 118 | 41 % → 4 % | 50.3 px | 0.18 | 0.10 | 36 |
| stroke 119 | 40 % → 1 % | 59.8 px | 0.20 | 0.02 | 36 |
| stroke 120 | 31 % → 0 % | 40.4 px | 0.00 | 0.00 | 16 |
| stroke 121 | 7 % → 6 % | 9.7 px | 0.16 | 0.82 | 30 |
| stroke 122 | 8 % → 0 % | 8.5 px | 0.00 | 0.00 | 25 |
| stroke 123 | 14 % → 0 % | 17.7 px | 0.00 | 0.00 | 25 |
| stroke 124 | 9 % → 6 % | 10.5 px | 0.15 | 0.68 | 20 |
| stroke 125 | 7 % → 0 % | 11.8 px | 0.00 | 0.00 | 20 |
| stroke 126 | 10 % → 15 % | 15.9 px | 0.17 | 1.44 | 22 |
| stroke 127 | 18 % → 0 % | 21.4 px | 0.00 | 0.00 | 27 |
| stroke 128 | 13 % → 0 % | 22.4 px | 0.00 | 0.00 | 13 |
| stroke 129 | 8 % → 0 % | 20.3 px | 0.00 | 0.00 | 2 |
| stroke 130 | 25 % → 0 % | 37.1 px | 0.00 | 0.00 | 16 |
| stroke 131 | 12 % → 0 % | 17.6 px | 0.00 | 0.00 | 20 |
| stroke 132 | 16 % → 28 % | 22.4 px | 0.16 | 1.75 | 22 |
| stroke 133 | 18 % → 0 % | 25.4 px | 0.00 | 0.00 | 38 |
| stroke 134 | 19 % → 0 % | 32.2 px | 0.00 | 0.00 | 16 |
| stroke 135 | 20 % → 0 % | 33.6 px | 0.00 | 0.00 | 24 |
| stroke 136 | 31 % → 1 % | 53.3 px | 0.15 | 0.04 | 10 |
| stroke 137 | 36 % → 1 % | 56.5 px | 0.15 | 0.02 | 17 |
| stroke 138 | 30 % → 0 % | 53.8 px | 0.00 | 0.00 | 10 |
| stroke 139 | 37 % → 0 % | 49.5 px | 0.00 | 0.00 | 15 |
| stroke 140 | 29 % → 0 % | 46.8 px | 0.00 | 0.00 | 17 |
| stroke 141 | 25 % → 0 % | 46.6 px | 0.00 | 0.00 | 6 |
| stroke 142 | 40 % → 0 % | 56.2 px | 0.00 | 0.00 | 8 |
| stroke 143 | 24 % → 0 % | 52.7 px | 0.00 | 0.00 | 8 |
| stroke 144 | 32 % → 13 % | 48.2 px | 0.17 | 0.40 | 44 |
| stroke 145 | 23 % → 0 % | 49.7 px | 0.00 | 0.00 | 5 |
| stroke 146 | 22 % → 0 % | 56.4 px | 0.00 | 0.00 | 3 |
| stroke 147 | 29 % → 21 % | 45.3 px | 0.17 | 0.71 | 25 |
| stroke 148 | 43 % → 0 % | 110.5 px | 0.00 | 0.00 | 3 |
| stroke 149 | 25 % → 0 % | 36.3 px | 0.00 | 0.00 | 8 |
| stroke 150 | 51 % → 0 % | 76.5 px | 0.00 | 0.00 | 7 |
| stroke 151 | 39 % → 0 % | 70.4 px | 0.00 | 0.00 | 33 |
| stroke 152 | 45 % → 17 % | 127.0 px | 0.16 | 0.37 | 7 |
| stroke 153 | 47 % → 0 % | 120.7 px | 0.00 | 0.00 | 6 |
| stroke 154 | 49 % → 14 % | 122.1 px | 0.15 | 0.29 | 6 |
| stroke 155 | 34 % → 0 % | 56.9 px | 0.00 | 0.00 | 13 |
| stroke 156 | 27 % → 6 % | 39.2 px | 0.16 | 0.23 | 10 |
| stroke 157 | 27 % → 0 % | 71.0 px | 0.00 | 0.00 | 3 |
| stroke 158 | 47 % → 0 % | 104.2 px | 0.00 | 0.00 | 4 |
| stroke 159 | 52 % → 0 % | 112.1 px | 0.00 | 0.00 | 8 |
| stroke 160 | 49 % → 0 % | 109.7 px | 0.00 | 0.00 | 14 |
| stroke 161 | 42 % → 0 % | 76.8 px | 0.00 | 0.00 | 16 |
| stroke 162 | 44 % → 12 % | 64.6 px | 0.15 | 0.28 | 15 |
| stroke 163 | 48 % → 0 % | 121.9 px | 0.00 | 0.00 | 3 |
| stroke 164 | 39 % → 0 % | 112.4 px | 0.00 | 0.00 | 3 |
| stroke 165 | 50 % → 0 % | 117.3 px | 0.00 | 0.00 | 8 |
| stroke 166 | 53 % → 16 % | 143.7 px | 0.17 | 0.30 | 3 |
| stroke 167 | 34 % → 27 % | 41.5 px | 0.16 | 0.81 | 63 |
| stroke 168 | 36 % → 21 % | 55.2 px | 0.17 | 0.59 | 67 |
| stroke 169 | 43 % → 8 % | 45.5 px | 0.16 | 0.18 | 36 |
| stroke 170 | 43 % → 0 % | 45.4 px | 0.00 | 0.00 | 78 |
| stroke 171 | 31 % → 0 % | 43.9 px | 0.00 | 0.00 | 41 |
| stroke 172 | 34 % → 0 % | 43.8 px | 0.00 | 0.00 | 44 |
| stroke 173 | 38 % → 0 % | 46.7 px | 0.00 | 0.00 | 43 |
| stroke 174 | 45 % → 0 % | 59.1 px | 0.00 | 0.00 | 60 |
| stroke 175 | 36 % → 0 % | 42.1 px | 0.00 | 0.00 | 39 |
| stroke 176 | 28 % → 0 % | 27.8 px | 0.00 | 0.00 | 41 |
| stroke 177 | 45 % → 0 % | 51.7 px | 0.00 | 0.00 | 42 |
| stroke 178 | 47 % → 0 % | 57.2 px | 0.00 | 0.00 | 48 |
| stroke 179 | 26 % → 15 % | 39.5 px | 0.17 | 0.57 | 32 |
| stroke 180 | 6 % → 3 % | 9.6 px | 0.17 | 0.54 | 26 |
| stroke 181 | 13 % → 8 % | 20.3 px | 0.19 | 0.62 | 23 |
| stroke 182 | 9 % → 0 % | 15.4 px | 0.00 | 0.00 | 14 |
| stroke 183 | 11 % → 0 % | 11.6 px | 0.00 | 0.00 | 29 |
| stroke 184 | 22 % → 1 % | 32.3 px | 0.20 | 0.04 | 10 |
| stroke 185 | 12 % → 0 % | 14.6 px | 0.00 | 0.00 | 34 |
| stroke 186 | 12 % → 0 % | 12.8 px | 0.00 | 0.00 | 27 |
| stroke 187 | 26 % → 0 % | 34.1 px | 0.00 | 0.00 | 32 |
| stroke 188 | 29 % → 0 % | 35.4 px | 0.00 | 0.00 | 16 |
| stroke 189 | 21 % → 17 % | 31.6 px | 0.19 | 0.81 | 30 |
| stroke 190 | 12 % → 13 % | 15.4 px | 0.18 | 1.04 | 20 |
| stroke 191 | 13 % → 0 % | 22.0 px | 0.00 | 0.00 | 21 |
| stroke 192 | 36 % → 0 % | 58.6 px | 0.00 | 0.00 | 11 |
| stroke 193 | 10 % → 0 % | 10.5 px | 0.00 | 0.00 | 11 |
| stroke 194 | 33 % → 0 % | 51.3 px | 0.00 | 0.00 | 16 |
| stroke 195 | 14 % → 0 % | 23.1 px | 0.00 | 0.00 | 25 |
| stroke 196 | 12 % → 29 % | 22.5 px | 0.17 | 2.31 | 18 |
| stroke 197 | 21 % → 11 % | 58.9 px | 0.17 | 0.51 | 7 |
| stroke 198 | 33 % → 0 % | 50.2 px | 0.15 | 0.00 | 32 |
| stroke 199 | 26 % → 0 % | 43.8 px | 0.00 | 0.00 | 9 |
| stroke 200 | 24 % → 0 % | 60.0 px | 0.00 | 0.00 | 4 |
| stroke 201 | 31 % → 0 % | 42.0 px | 0.00 | 0.00 | 26 |
| stroke 202 | 25 % → 16 % | 40.0 px | 0.18 | 0.65 | 27 |
| stroke 203 | 30 % → 0 % | 48.7 px | 0.00 | 0.00 | 16 |
| stroke 204 | 43 % → 0 % | 99.3 px | 0.00 | 0.00 | 6 |
| stroke 205 | 36 % → 1 % | 56.2 px | 0.16 | 0.03 | 15 |
| stroke 206 | 39 % → 0 % | 59.6 px | 0.00 | 0.00 | 22 |
| stroke 207 | 33 % → 15 % | 85.9 px | 0.16 | 0.45 | 7 |
| stroke 208 | 50 % → 0 % | 139.4 px | 0.00 | 0.00 | 3 |
| stroke 209 | 39 % → 0 % | 86.3 px | 0.00 | 0.00 | 7 |
| stroke 210 | 51 % → 0 % | 79.7 px | 0.00 | 0.00 | 39 |
| stroke 211 | 26 % → 0 % | 44.7 px | 0.00 | 0.00 | 16 |
| stroke 212 | 30 % → 0 % | 38.2 px | 0.00 | 0.00 | 37 |
| stroke 213 | 32 % → 0 % | 68.8 px | 0.00 | 0.00 | 15 |
| stroke 214 | 41 % → 0 % | 109.9 px | 0.00 | 0.00 | 3 |
| stroke 215 | 42 % → 0 % | 110.1 px | 0.00 | 0.00 | 6 |
| stroke 216 | 53 % → 0 % | 125.6 px | 0.00 | 0.00 | 6 |
| stroke 217 | 57 % → 0 % | 148.6 px | 0.00 | 0.00 | 6 |
| stroke 218 | 43 % → 0 % | 82.3 px | 0.00 | 0.00 | 17 |
| stroke 219 | 24 % → 0 % | 64.4 px | 0.00 | 0.00 | 8 |
| stroke 220 | 40 % → 0 % | 114.7 px | 0.00 | 0.00 | 4 |
| stroke 221 | 53 % → 0 % | 81.5 px | 0.00 | 0.00 | 22 |
| stroke 222 | 28 % → 24 % | 78.6 px | 0.18 | 0.85 | 9 |
| stroke 223 | 57 % → 0 % | 156.6 px | 0.00 | 0.00 | 8 |
| stroke 224 | 34 % → 0 % | 84.3 px | 0.00 | 0.00 | 4 |
| stroke 225 | 49 % → 0 % | 116.8 px | 0.00 | 0.00 | 7 |
| stroke 226 | 26 % → 32 % | 69.9 px | 0.19 | 1.21 | 3 |
| stroke 227 | 31 % → 18 % | 41.0 px | 0.17 | 0.58 | 66 |
| stroke 228 | 34 % → 0 % | 42.5 px | 0.00 | 0.00 | 79 |
| stroke 229 | 35 % → 0 % | 48.1 px | 0.00 | 0.00 | 51 |
| stroke 230 | 42 % → 0 % | 47.3 px | 0.00 | 0.00 | 58 |
| stroke 231 | 45 % → 0 % | 54.7 px | 0.00 | 0.00 | 50 |
| stroke 232 | 32 % → 0 % | 47.9 px | 0.00 | 0.00 | 54 |
| stroke 233 | 29 % → 0 % | 23.1 px | 0.00 | 0.00 | 60 |
| stroke 234 | 43 % → 0 % | 45.1 px | 0.00 | 0.00 | 44 |
| stroke 235 | 43 % → 6 % | 45.6 px | 0.21 | 0.14 | 43 |
| stroke 236 | 32 % → 20 % | 42.4 px | 0.19 | 0.63 | 47 |
| stroke 237 | 32 % → 28 % | 41.6 px | 0.19 | 0.86 | 42 |
| stroke 238 | 35 % → 32 % | 104.1 px | 0.19 | 0.92 | 10 |
| stroke 239 | 13 % → 0 % | 22.5 px | 0.00 | 0.00 | 8 |
| stroke 240 | 11 % → 0 % | 29.4 px | 0.00 | 0.00 | 4 |
| stroke 241 | 22 % → 0 % | 50.3 px | 0.00 | 0.00 | 8 |
| stroke 242 | 20 % → 0 % | 43.4 px | 0.00 | 0.00 | 8 |
| stroke 243 | 26 % → 0 % | 25.0 px | 0.00 | 0.00 | 35 |
| stroke 244 | 22 % → 0 % | 21.0 px | 0.00 | 0.00 | 49 |
| stroke 245 | 24 % → 0 % | 64.8 px | 0.00 | 0.00 | 10 |
| stroke 246 | 10 % → 0 % | 18.6 px | 0.00 | 0.00 | 9 |
| stroke 247 | 15 % → 0 % | 35.4 px | 0.00 | 0.00 | 6 |
| stroke 248 | 20 % → 0 % | 17.2 px | 0.00 | 0.00 | 38 |
| stroke 249 | 24 % → 0 % | 61.5 px | 0.00 | 0.00 | 20 |
| stroke 250 | 5 % → 36 % | 9.4 px | 0.17 | 7.34 | 18 |
| stroke 251 | 8 % → 5 % | 11.4 px | 0.16 | 0.66 | 58 |
| stroke 252 | 9 % → 0 % | 14.0 px | 0.15 | 0.02 | 28 |
| stroke 253 | 14 % → 29 % | 21.8 px | 0.18 | 2.07 | 15 |
| stroke 254 | 26 % → 12 % | 34.1 px | 0.17 | 0.46 | 15 |
| stroke 255 | 21 % → 26 % | 29.7 px | 0.17 | 1.26 | 18 |
| stroke 256 | 24 % → 0 % | 58.9 px | 0.00 | 0.00 | 4 |
| stroke 257 | 27 % → 6 % | 51.7 px | 0.15 | 0.23 | 9 |
| stroke 258 | 28 % → 0 % | 41.8 px | 0.15 | 0.01 | 31 |
| stroke 259 | 7 % → 0 % | 12.0 px | 0.00 | 0.00 | 13 |
| stroke 260 | 14 % → 0 % | 29.7 px | 0.00 | 0.00 | 7 |
| stroke 261 | 23 % → 2 % | 64.5 px | 0.20 | 0.08 | 3 |
| stroke 262 | 28 % → 0 % | 79.2 px | 0.00 | 0.00 | 28 |
| stroke 263 | 32 % → 0 % | 93.9 px | 0.00 | 0.00 | 4 |
| stroke 264 | 32 % → 0 % | 76.1 px | 0.00 | 0.00 | 7 |
| stroke 265 | 27 % → 7 % | 76.7 px | 0.15 | 0.26 | 6 |
| stroke 266 | 36 % → 0 % | 77.5 px | 0.00 | 0.00 | 7 |
| stroke 267 | 22 % → 0 % | 53.5 px | 0.00 | 0.00 | 4 |
| stroke 268 | 31 % → 0 % | 89.2 px | 0.00 | 0.00 | 7 |
| stroke 269 | 16 % → 0 % | 20.6 px | 0.00 | 0.00 | 30 |
| stroke 270 | 30 % → 0 % | 41.5 px | 0.11 | 0.00 | 45 |
| stroke 271 | 35 % → 20 % | 45.1 px | 0.17 | 0.57 | 49 |
| stroke 272 | 27 % → 28 % | 27.5 px | 0.18 | 1.05 | 56 |
| stroke 273 | 32 % → 7 % | 44.5 px | 0.19 | 0.23 | 38 |
| stroke 274 | 38 % → 0 % | 48.2 px | 0.00 | 0.00 | 45 |
| stroke 275 | 29 % → 0 % | 44.4 px | 0.00 | 0.00 | 47 |
| stroke 276 | 24 % → 0 % | 42.3 px | 0.00 | 0.00 | 15 |
| stroke 277 | 6 % → 10 % | 9.3 px | 0.16 | 1.82 | 16 |
| stroke 278 | 6 % → 0 % | 8.7 px | 0.00 | 0.00 | 15 |
| stroke 279 | 11 % → 17 % | 13.9 px | 0.16 | 1.65 | 22 |
| stroke 280 | 9 % → 15 % | 12.1 px | 0.20 | 1.66 | 17 |
| stroke 281 | 21 % → 0 % | 33.2 px | 0.00 | 0.00 | 6 |
| stroke 282 | 13 % → 0 % | 22.3 px | 0.00 | 0.00 | 10 |
| stroke 283 | 28 % → 0 % | 61.3 px | 0.00 | 0.00 | 6 |
| stroke 284 | 19 % → 29 % | 35.2 px | 0.16 | 1.58 | 11 |
| stroke 285 | 19 % → 0 % | 29.2 px | 0.15 | 0.02 | 6 |
| stroke 286 | 28 % → 0 % | 60.2 px | 0.00 | 0.00 | 4 |
| stroke 287 | 20 % → 30 % | 51.2 px | 0.18 | 1.51 | 4 |
| stroke 288 | 19 % → 16 % | 50.5 px | 0.20 | 0.85 | 4 |
| stroke 289 | 21 % → 0 % | 21.0 px | 0.00 | 0.00 | 48 |
| stroke 290 | 37 % → 2 % | 45.1 px | 0.20 | 0.05 | 57 |
| stroke 291 | 35 % → 13 % | 35.2 px | 0.17 | 0.38 | 43 |
| stroke 292 | 24 % → 10 % | 20.6 px | 0.15 | 0.42 | 38 |
| stroke 293 | 32 % → 26 % | 34.1 px | 0.17 | 0.81 | 44 |
| stroke 294 | 31 % → 17 % | 26.8 px | 0.19 | 0.56 | 56 |
| stroke 295 | 43 % → 0 % | 46.8 px | 0.15 | 0.01 | 47 |
| stroke 296 | 37 % → 0 % | 133.2 px | 0.00 | 0.00 | 11 |
| stroke 297 | 7 % → 0 % | 9.9 px | 0.00 | 0.00 | 8 |
| stroke 298 | 11 % → 0 % | 23.1 px | 0.00 | 0.00 | 5 |
| stroke 299 | 17 % → 0 % | 24.0 px | 0.00 | 0.00 | 28 |
| stroke 300 | 9 % → 0 % | 12.7 px | 0.00 | 0.00 | 18 |
| stroke 301 | 8 % → 0 % | 15.4 px | 0.00 | 0.00 | 5 |
| stroke 302 | 12 % → 0 % | 20.7 px | 0.00 | 0.00 | 9 |
| stroke 303 | 23 % → 0 % | 43.5 px | 0.00 | 0.00 | 12 |
| stroke 304 | 20 % → 0 % | 53.0 px | 0.00 | 0.00 | 3 |
| stroke 305 | 20 % → 0 % | 53.7 px | 0.00 | 0.00 | 3 |
| stroke 306 | 25 % → 0 % | 59.4 px | 0.00 | 0.00 | 4 |
| stroke 307 | 37 % → 0 % | 101.0 px | 0.00 | 0.00 | 2 |
| stroke 308 | 15 % → 0 % | 42.1 px | 0.00 | 0.00 | 3 |
| stroke 309 | 22 % → 0 % | 28.1 px | 0.00 | 0.00 | 32 |
| stroke 310 | 28 % → 0 % | 32.9 px | 0.00 | 0.00 | 51 |
| stroke 311 | 22 % → 0 % | 22.2 px | 0.00 | 0.00 | 62 |
| stroke 312 | 30 % → 0 % | 38.8 px | 0.00 | 0.00 | 56 |
| stroke 313 | 37 % → 0 % | 50.7 px | 0.00 | 0.00 | 69 |
| stroke 314 | 25 % → 0 % | 23.4 px | 0.00 | 0.00 | 49 |
| stroke 315 | 29 % → 0 % | 60.0 px | 0.00 | 0.00 | 19 |
| stroke 316 | 9 % → 0 % | 13.9 px | 0.00 | 0.00 | 23 |
| stroke 317 | 8 % → 0 % | 12.9 px | 0.00 | 0.00 | 37 |
| stroke 318 | 18 % → 0 % | 25.8 px | 0.00 | 0.00 | 39 |
| stroke 319 | 8 % → 0 % | 10.5 px | 0.00 | 0.00 | 34 |
| stroke 320 | 17 % → 0 % | 27.1 px | 0.00 | 0.00 | 16 |
| stroke 321 | 18 % → 0 % | 34.4 px | 0.00 | 0.00 | 13 |
| stroke 322 | 22 % → 0 % | 37.4 px | 0.00 | 0.00 | 20 |
| stroke 323 | 15 % → 0 % | 35.7 px | 0.00 | 0.00 | 8 |
| stroke 324 | 28 % → 0 % | 44.0 px | 0.00 | 0.00 | 23 |
| stroke 325 | 15 % → 0 % | 34.4 px | 0.00 | 0.00 | 15 |
| stroke 326 | 24 % → 0 % | 33.0 px | 0.00 | 0.00 | 20 |
| stroke 327 | 29 % → 0 % | 45.9 px | 0.00 | 0.00 | 22 |
| stroke 328 | 43 % → 0 % | 83.3 px | 0.00 | 0.00 | 12 |
| stroke 329 | 40 % → 0 % | 113.6 px | 0.00 | 0.00 | 6 |
| stroke 330 | 34 % → 0 % | 77.4 px | 0.00 | 0.00 | 5 |
| stroke 331 | 24 % → 0 % | 59.7 px | 0.00 | 0.00 | 8 |
| stroke 332 | 40 % → 0 % | 105.3 px | 0.00 | 0.00 | 4 |
| stroke 333 | 51 % → 0 % | 146.2 px | 0.00 | 0.00 | 3 |
| stroke 334 | 29 % → 0 % | 30.4 px | 0.00 | 0.00 | 39 |
| stroke 335 | 28 % → 0 % | 42.7 px | 0.00 | 0.00 | 36 |
| stroke 336 | 34 % → 0 % | 48.2 px | 0.00 | 0.00 | 43 |
| stroke 337 | 36 % → 0 % | 42.5 px | 0.00 | 0.00 | 43 |
| stroke 338 | 34 % → 0 % | 50.4 px | 0.00 | 0.00 | 31 |
| stroke 339 | 34 % → 0 % | 33.0 px | 0.00 | 0.00 | 63 |
| stroke 340 | 42 % → 0 % | 58.4 px | 0.00 | 0.00 | 48 |
| stroke 341 | 38 % → 0 % | 45.0 px | 0.00 | 0.00 | 33 |
| stroke 342 | 55 % → 0 % | 57.9 px | 0.00 | 0.00 | 34 |
| stroke 343 | 59 % → 0 % | 112.4 px | 0.00 | 0.00 | 21 |
| stroke 344 | 8 % → 0 % | 10.4 px | 0.00 | 0.00 | 16 |
| stroke 345 | 19 % → 0 % | 22.7 px | 0.00 | 0.00 | 18 |
| stroke 346 | 18 % → 0 % | 50.0 px | 0.00 | 0.00 | 6 |
| stroke 347 | 20 % → 0 % | 17.1 px | 0.00 | 0.00 | 44 |
| stroke 348 | 30 % → 0 % | 28.0 px | 0.00 | 0.00 | 40 |
| stroke 349 | 6 % → 0 % | 12.1 px | 0.00 | 0.00 | 6 |
| stroke 350 | 11 % → 0 % | 30.5 px | 0.00 | 0.00 | 5 |
| stroke 351 | 12 % → 0 % | 10.6 px | 0.00 | 0.00 | 27 |
| stroke 352 | 23 % → 0 % | 43.6 px | 0.00 | 0.00 | 10 |
| stroke 353 | 21 % → 0 % | 26.2 px | 0.00 | 0.00 | 17 |
| stroke 354 | 6 % → 0 % | 9.6 px | 0.00 | 0.00 | 12 |
| stroke 355 | 13 % → 0 % | 34.8 px | 0.00 | 0.00 | 5 |
| stroke 356 | 13 % → 0 % | 9.9 px | 0.00 | 0.00 | 58 |
| stroke 357 | 25 % → 0 % | 156.0 px | 0.00 | 0.00 | 4 |
| stroke 358 | 7 % → 0 % | 10.4 px | 0.00 | 0.00 | 21 |
| stroke 359 | 7 % → 0 % | 17.3 px | 0.00 | 0.00 | 6 |
| stroke 360 | 17 % → 0 % | 29.8 px | 0.00 | 0.00 | 8 |
| stroke 361 | 18 % → 0 % | 41.5 px | 0.00 | 0.00 | 8 |
| stroke 362 | 23 % → 0 % | 20.9 px | 0.00 | 0.00 | 35 |
| stroke 363 | 25 % → 0 % | 24.4 px | 0.00 | 0.00 | 41 |
| stroke 364 | 32 % → 0 % | 54.4 px | 0.00 | 0.00 | 15 |
| stroke 365 | 8 % → 0 % | 9.0 px | 0.00 | 0.00 | 29 |
| stroke 366 | 11 % → 0 % | 27.8 px | 0.00 | 0.00 | 7 |
| stroke 367 | 18 % → 0 % | 20.5 px | 0.00 | 0.00 | 34 |
| stroke 368 | 12 % → 0 % | 18.1 px | 0.00 | 0.00 | 22 |
| stroke 369 | 27 % → 0 % | 53.4 px | 0.00 | 0.00 | 12 |
| stroke 370 | 21 % → 0 % | 45.4 px | 0.00 | 0.00 | 6 |
| stroke 371 | 29 % → 0 % | 67.6 px | 0.00 | 0.00 | 7 |
| stroke 372 | 42 % → 0 % | 65.2 px | 0.00 | 0.00 | 10 |
| stroke 373 | 42 % → 0 % | 78.8 px | 0.00 | 0.00 | 6 |
| stroke 374 | 27 % → 0 % | 49.1 px | 0.00 | 0.00 | 5 |
| stroke 375 | 28 % → 0 % | 31.9 px | 0.00 | 0.00 | 42 |
| stroke 376 | 32 % → 0 % | 37.4 px | 0.00 | 0.00 | 46 |
| stroke 377 | 39 % → 0 % | 42.9 px | 0.00 | 0.00 | 46 |
| stroke 378 | 30 % → 0 % | 28.9 px | 0.00 | 0.00 | 49 |
| stroke 379 | 31 % → 0 % | 364.7 px | 0.00 | 0.00 | 1 |
| stroke 380 | 8 % → 0 % | 9.2 px | 0.00 | 0.00 | 30 |
| stroke 381 | 14 % → 0 % | 15.0 px | 0.00 | 0.00 | 30 |
| stroke 382 | 9 % → 0 % | 8.0 px | 0.00 | 0.00 | 33 |
| stroke 383 | 19 % → 0 % | 32.5 px | 0.00 | 0.00 | 8 |
| stroke 384 | 12 % → 0 % | 13.6 px | 0.00 | 0.00 | 24 |
| stroke 385 | 18 % → 0 % | 13.9 px | 0.00 | 0.00 | 31 |
| stroke 386 | 24 % → 0 % | 23.9 px | 0.00 | 0.00 | 38 |
| stroke 387 | 6 % → 0 % | 8.7 px | 0.00 | 0.00 | 17 |
| stroke 388 | 6 % → 0 % | 9.1 px | 0.00 | 0.00 | 9 |
| stroke 389 | 17 % → 0 % | 22.3 px | 0.00 | 0.00 | 28 |
| stroke 390 | 29 % → 0 % | 63.1 px | 0.00 | 0.00 | 5 |
| stroke 391 | 24 % → 0 % | 40.1 px | 0.00 | 0.00 | 16 |
| stroke 392 | 17 % → 0 % | 23.7 px | 0.00 | 0.00 | 10 |
| stroke 393 | 22 % → 0 % | 33.2 px | 0.00 | 0.00 | 7 |
| stroke 394 | 17 % → 0 % | 40.2 px | 0.00 | 0.00 | 9 |
| stroke 395 | 26 % → 0 % | 52.1 px | 0.00 | 0.00 | 12 |
| stroke 396 | 24 % → 0 % | 57.9 px | 0.00 | 0.00 | 8 |
| stroke 397 | 22 % → 0 % | 38.5 px | 0.00 | 0.00 | 8 |
| stroke 398 | 33 % → 0 % | 50.1 px | 0.00 | 0.00 | 31 |
| stroke 399 | 18 % → 0 % | 36.9 px | 0.00 | 0.00 | 9 |
| stroke 400 | 24 % → 0 % | 52.8 px | 0.00 | 0.00 | 7 |
| stroke 401 | 51 % → 0 % | 105.0 px | 0.00 | 0.00 | 9 |
| stroke 402 | 46 % → 0 % | 74.3 px | 0.00 | 0.00 | 11 |
| stroke 403 | 34 % → 0 % | 84.8 px | 0.00 | 0.00 | 5 |
| stroke 404 | 44 % → 0 % | 73.8 px | 0.00 | 0.00 | 8 |
| stroke 405 | 39 % → 0 % | 107.2 px | 0.00 | 0.00 | 3 |
| stroke 406 | 26 % → 0 % | 22.3 px | 0.00 | 0.00 | 35 |
| stroke 407 | 43 % → 0 % | 37.6 px | 0.00 | 0.00 | 57 |
| stroke 408 | 43 % → 0 % | 33.2 px | 0.00 | 0.00 | 37 |
| stroke 409 | 37 % → 0 % | 37.4 px | 0.00 | 0.00 | 38 |
| stroke 410 | 37 % → 0 % | 38.3 px | 0.00 | 0.00 | 40 |
| stroke 411 | 33 % → 0 % | 29.7 px | 0.00 | 0.00 | 35 |
| stroke 412 | 20 % → 0 % | 16.4 px | 0.00 | 0.00 | 40 |
| stroke 413 | 26 % → 0 % | 24.9 px | 0.00 | 0.00 | 45 |
| stroke 414 | 30 % → 0 % | 44.0 px | 0.00 | 0.00 | 33 |
| stroke 415 | 36 % → 0 % | 40.5 px | 0.00 | 0.00 | 59 |
| stroke 416 | 36 % → 0 % | 52.6 px | 0.00 | 0.00 | 38 |
| stroke 417 | 37 % → 0 % | 44.0 px | 0.00 | 0.00 | 45 |
| stroke 418 | 29 % → 0 % | 42.4 px | 0.00 | 0.00 | 20 |
| stroke 419 | 6 % → 0 % | 10.9 px | 0.00 | 0.00 | 10 |
| stroke 420 | 11 % → 0 % | 9.5 px | 0.00 | 0.00 | 15 |
| stroke 421 | 17 % → 0 % | 36.1 px | 0.00 | 0.00 | 2 |
| stroke 422 | 18 % → 0 % | 20.7 px | 0.00 | 0.00 | 14 |
| stroke 423 | 6 % → 0 % | 10.4 px | 0.00 | 0.00 | 13 |
| stroke 424 | 10 % → 0 % | 16.6 px | 0.00 | 0.00 | 20 |
| stroke 425 | 13 % → 0 % | 13.5 px | 0.00 | 0.00 | 43 |
| stroke 426 | 17 % → 0 % | 32.1 px | 0.00 | 0.00 | 23 |
| stroke 427 | 20 % → 0 % | 29.2 px | 0.00 | 0.00 | 19 |
| stroke 428 | 8 % → 0 % | 17.1 px | 0.00 | 0.00 | 9 |
| stroke 429 | 17 % → 0 % | 14.1 px | 0.00 | 0.00 | 32 |
| stroke 430 | 8 % → 0 % | 10.2 px | 0.00 | 0.00 | 27 |
| stroke 431 | 17 % → 0 % | 27.4 px | 0.00 | 0.00 | 20 |
| stroke 432 | 21 % → 0 % | 32.1 px | 0.00 | 0.00 | 10 |
| stroke 433 | 26 % → 0 % | 58.6 px | 0.00 | 0.00 | 11 |
| stroke 434 | 32 % → 0 % | 50.3 px | 0.00 | 0.00 | 5 |
| stroke 435 | 34 % → 0 % | 93.9 px | 0.00 | 0.00 | 6 |
| stroke 436 | 27 % → 0 % | 79.0 px | 0.00 | 0.00 | 6 |
| stroke 437 | 26 % → 0 % | 35.9 px | 0.00 | 0.00 | 33 |
| stroke 438 | 35 % → 0 % | 36.5 px | 0.00 | 0.00 | 28 |
| stroke 439 | 38 % → 0 % | 32.7 px | 0.00 | 0.00 | 38 |
| stroke 440 | 37 % → 0 % | 77.2 px | 0.00 | 0.00 | 7 |
| stroke 441 | 4 % → 0 % | 12.2 px | 0.00 | 0.00 | 4 |
| stroke 442 | 7 % → 0 % | 9.8 px | 0.00 | 0.00 | 10 |
| stroke 443 | 16 % → 3 % | 18.3 px | 0.15 | 0.18 | 12 |
| stroke 444 | 17 % → 1 % | 14.1 px | 0.15 | 0.07 | 24 |
| stroke 445 | 25 % → 5 % | 53.3 px | 0.16 | 0.22 | 3 |
| stroke 446 | 25 % → 1 % | 16.8 px | 0.15 | 0.04 | 44 |
| stroke 447 | 31 % → 4 % | 21.3 px | 0.16 | 0.12 | 41 |
| stroke 448 | 26 % → 0 % | 46.6 px | 0.00 | 0.00 | 10 |
| stroke 449 | 5 % → 17 % | 11.0 px | 0.21 | 3.40 | 12 |
| stroke 450 | 9 % → 2 % | 14.3 px | 0.20 | 0.23 | 22 |
| stroke 451 | 13 % → 2 % | 36.4 px | 0.20 | 0.13 | 6 |
| stroke 452 | 14 % → 24 % | 30.0 px | 0.21 | 1.72 | 10 |
| stroke 453 | 23 % → 0 % | 51.5 px | 0.00 | 0.00 | 6 |
| stroke 454 | 17 % → 12 % | 21.0 px | 0.21 | 0.68 | 33 |
| stroke 455 | 20 % → 2 % | 17.5 px | 0.20 | 0.10 | 43 |
| stroke 456 | 22 % → 9 % | 34.2 px | 0.21 | 0.40 | 45 |
| stroke 457 | 6 % → 4 % | 11.3 px | 0.21 | 0.64 | 12 |
| stroke 458 | 12 % → 15 % | 17.0 px | 0.19 | 1.33 | 20 |
| stroke 459 | 18 % → 27 % | 35.7 px | 0.20 | 1.45 | 10 |
| stroke 460 | 21 % → 2 % | 46.9 px | 0.16 | 0.08 | 10 |
| stroke 461 | 18 % → 33 % | 34.0 px | 0.19 | 1.89 | 9 |
| stroke 462 | 31 % → 12 % | 74.8 px | 0.21 | 0.40 | 6 |
| stroke 463 | 24 % → 17 % | 25.0 px | 0.19 | 0.69 | 41 |
| stroke 464 | 28 % → 12 % | 33.5 px | 0.20 | 0.44 | 49 |
| stroke 465 | 33 % → 32 % | 52.7 px | 0.20 | 0.96 | 20 |
| stroke 466 | 5 % → 0 % | 12.7 px | 0.00 | 0.00 | 12 |
| stroke 467 | 10 % → 0 % | 18.2 px | 0.00 | 0.00 | 12 |
| stroke 468 | 15 % → 7 % | 29.3 px | 0.16 | 0.49 | 7 |
| stroke 469 | 14 % → 0 % | 37.3 px | 0.00 | 0.00 | 2 |
| stroke 470 | 15 % → 7 % | 16.8 px | 0.16 | 0.49 | 38 |
| stroke 471 | 21 % → 6 % | 22.0 px | 0.16 | 0.28 | 43 |
| stroke 472 | 25 % → 14 % | 118.6 px | 0.17 | 0.55 | 2 |
| stroke 473 | 10 % → 38 % | 16.6 px | 0.16 | 3.80 | 16 |
| stroke 474 | 22 % → 16 % | 27.1 px | 0.15 | 0.72 | 14 |
| stroke 475 | 16 % → 52 % | 28.5 px | 0.17 | 3.16 | 29 |
| stroke 476 | 14 % → 0 % | 18.9 px | 0.00 | 0.00 | 6 |
| stroke 477 | 18 % → 0 % | 12.1 px | 0.00 | 0.00 | 29 |
| stroke 478 | 5 % → 57 % | 9.3 px | 0.16 | 10.68 | 5 |
| stroke 479 | 10 % → 53 % | 7.9 px | 0.16 | 5.48 | 30 |
| stroke 480 | 11 % → 0 % | 16.3 px | 0.00 | 0.00 | 14 |
| stroke 481 | 14 % → 0 % | 25.4 px | 0.00 | 0.00 | 15 |
| stroke 482 | 26 % → 0 % | 22.0 px | 0.00 | 0.00 | 14 |
| stroke 483 | 28 % → 0 % | 19.4 px | 0.00 | 0.00 | 54 |
| stroke 484 | 29 % → 0 % | 50.5 px | 0.00 | 0.00 | 12 |
| stroke 485 | 5 % → 0 % | 11.1 px | 0.00 | 0.00 | 13 |
| stroke 486 | 10 % → 0 % | 28.4 px | 0.00 | 0.00 | 6 |
| stroke 487 | 11 % → 0 % | 10.0 px | 0.00 | 0.00 | 30 |
| stroke 488 | 5 % → 0 % | 12.4 px | 0.00 | 0.00 | 5 |
| stroke 489 | 7 % → 0 % | 10.8 px | 0.00 | 0.00 | 9 |
| stroke 490 | 4 % → 0 % | 11.7 px | 0.00 | 0.00 | 3 |
| stroke 491 | 9 % → 0 % | 10.4 px | 0.00 | 0.00 | 34 |
| stroke 492 | 6 % → 0 % | 8.9 px | 0.00 | 0.00 | 29 |
| stroke 493 | 6 % → 0 % | 9.4 px | 0.00 | 0.00 | 27 |
| stroke 494 | 12 % → 0 % | 15.3 px | 0.00 | 0.00 | 34 |
| stroke 495 | 11 % → 0 % | 16.4 px | 0.00 | 0.00 | 24 |
| stroke 496 | 14 % → 0 % | 21.2 px | 0.00 | 0.00 | 29 |
| stroke 497 | 6 % → 0 % | 8.5 px | 0.00 | 0.00 | 17 |
| stroke 498 | 7 % → 0 % | 11.3 px | 0.00 | 0.00 | 19 |
| stroke 499 | 14 % → 0 % | 20.0 px | 0.00 | 0.00 | 13 |
| stroke 500 | 20 % → 0 % | 40.4 px | 0.00 | 0.00 | 11 |
| stroke 501 | 7 % → 0 % | 12.6 px | 0.00 | 0.00 | 7 |
| stroke 502 | 6 % → 0 % | 9.7 px | 0.00 | 0.00 | 15 |
| stroke 503 | 16 % → 0 % | 25.1 px | 0.00 | 0.00 | 24 |
| stroke 504 | 8 % → 0 % | 8.7 px | 0.00 | 0.00 | 18 |
| stroke 505 | 30 % → 0 % | 57.3 px | 0.00 | 0.00 | 10 |
| stroke 506 | 27 % → 0 % | 42.5 px | 0.00 | 0.00 | 18 |
| stroke 507 | 12 % → 0 % | 18.6 px | 0.00 | 0.00 | 36 |
| stroke 508 | 23 % → 0 % | 35.3 px | 0.00 | 0.00 | 13 |
| stroke 509 | 29 % → 0 % | 50.4 px | 0.00 | 0.00 | 13 |
| stroke 510 | 24 % → 0 % | 28.7 px | 0.00 | 0.00 | 22 |
| stroke 511 | 31 % → 0 % | 55.5 px | 0.00 | 0.00 | 7 |
| stroke 512 | 33 % → 0 % | 53.0 px | 0.00 | 0.00 | 31 |
| stroke 513 | 30 % → 0 % | 44.6 px | 0.00 | 0.00 | 19 |
| stroke 514 | 20 % → 0 % | 29.9 px | 0.00 | 0.00 | 26 |
| stroke 515 | 15 % → 0 % | 25.4 px | 0.00 | 0.00 | 9 |
| stroke 516 | 24 % → 0 % | 49.3 px | 0.00 | 0.00 | 8 |
| stroke 517 | 13 % → 0 % | 17.3 px | 0.00 | 0.00 | 14 |
| stroke 518 | 15 % → 0 % | 23.6 px | 0.00 | 0.00 | 24 |
| stroke 519 | 34 % → 0 % | 52.7 px | 0.00 | 0.00 | 12 |
| stroke 520 | 32 % → 0 % | 50.8 px | 0.00 | 0.00 | 12 |
| stroke 521 | 17 % → 0 % | 25.1 px | 0.00 | 0.00 | 16 |
| stroke 522 | 24 % → 0 % | 42.1 px | 0.00 | 0.00 | 9 |
| stroke 523 | 16 % → 0 % | 21.7 px | 0.00 | 0.00 | 23 |
| stroke 524 | 34 % → 0 % | 83.8 px | 0.00 | 0.00 | 8 |
| stroke 525 | 44 % → 0 % | 72.3 px | 0.00 | 0.00 | 8 |
| stroke 526 | 43 % → 0 % | 88.1 px | 0.00 | 0.00 | 16 |
| stroke 527 | 29 % → 0 % | 45.7 px | 0.00 | 0.00 | 12 |
| stroke 528 | 27 % → 0 % | 63.4 px | 0.00 | 0.00 | 14 |
| stroke 529 | 46 % → 0 % | 85.7 px | 0.00 | 0.00 | 7 |
| stroke 530 | 29 % → 0 % | 45.7 px | 0.00 | 0.00 | 23 |
| stroke 531 | 18 % → 0 % | 30.1 px | 0.00 | 0.00 | 15 |
| stroke 532 | 33 % → 0 % | 66.4 px | 0.00 | 0.00 | 14 |
| stroke 533 | 36 % → 0 % | 72.4 px | 0.00 | 0.00 | 5 |
| stroke 534 | 42 % → 0 % | 80.9 px | 0.00 | 0.00 | 13 |
| stroke 535 | 12 % → 0 % | 27.9 px | 0.00 | 0.00 | 11 |
| stroke 536 | 13 % → 0 % | 28.5 px | 0.00 | 0.00 | 13 |
| stroke 537 | 48 % → 0 % | 129.2 px | 0.00 | 0.00 | 6 |
| stroke 538 | 41 % → 0 % | 74.8 px | 0.00 | 0.00 | 7 |
| stroke 539 | 22 % → 0 % | 62.5 px | 0.00 | 0.00 | 4 |
| stroke 540 | 32 % → 0 % | 76.6 px | 0.00 | 0.00 | 6 |
| stroke 541 | 15 % → 0 % | 32.3 px | 0.00 | 0.00 | 11 |
| stroke 542 | 18 % → 0 % | 51.6 px | 0.00 | 0.00 | 3 |
| stroke 543 | 39 % → 0 % | 110.0 px | 0.00 | 0.00 | 3 |
| stroke 544 | 55 % → 0 % | 157.8 px | 0.00 | 0.00 | 6 |
| stroke 545 | 34 % → 0 % | 90.3 px | 0.00 | 0.00 | 5 |
| stroke 546 | 63 % → 0 % | 139.5 px | 0.00 | 0.00 | 5 |
| stroke 547 | 39 % → 0 % | 87.4 px | 0.00 | 0.00 | 4 |
| stroke 548 | 25 % → 0 % | 62.3 px | 0.00 | 0.00 | 4 |
| stroke 549 | 34 % → 0 % | 73.1 px | 0.00 | 0.00 | 3 |
| stroke 550 | 42 % → 0 % | 119.7 px | 0.00 | 0.00 | 3 |
| stroke 551 | 35 % → 0 % | 87.1 px | 0.00 | 0.00 | 8 |
| stroke 552 | 39 % → 0 % | 106.9 px | 0.00 | 0.00 | 6 |
| stroke 553 | 44 % → 0 % | 124.2 px | 0.00 | 0.00 | 6 |
| stroke 554 | 13 % → 0 % | 12.9 px | 0.00 | 0.00 | 36 |
| stroke 555 | 31 % → 0 % | 44.4 px | 0.00 | 0.00 | 37 |
| stroke 556 | 44 % → 0 % | 45.8 px | 0.00 | 0.00 | 41 |
| stroke 557 | 56 % → 0 % | 62.7 px | 0.00 | 0.00 | 46 |
| stroke 558 | 37 % → 0 % | 42.6 px | 0.00 | 0.00 | 27 |
| stroke 559 | 40 % → 0 % | 39.8 px | 0.00 | 0.00 | 53 |
| stroke 560 | 29 % → 0 % | 25.6 px | 0.00 | 0.00 | 50 |
| stroke 561 | 36 % → 0 % | 52.1 px | 0.00 | 0.00 | 38 |
| stroke 562 | 39 % → 0 % | 56.8 px | 0.00 | 0.00 | 42 |
| stroke 563 | 30 % → 0 % | 35.2 px | 0.00 | 0.00 | 53 |
| stroke 564 | 30 % → 0 % | 41.1 px | 0.00 | 0.00 | 51 |
| stroke 565 | 30 % → 0 % | 39.2 px | 0.00 | 0.00 | 41 |
| stroke 566 | 35 % → 0 % | 44.5 px | 0.00 | 0.00 | 43 |
| stroke 567 | 36 % → 0 % | 57.1 px | 0.00 | 0.00 | 36 |
| stroke 568 | 32 % → 0 % | 41.0 px | 0.00 | 0.00 | 31 |
| stroke 569 | 28 % → 0 % | 36.4 px | 0.00 | 0.00 | 48 |
| stroke 570 | 32 % → 0 % | 34.4 px | 0.00 | 0.00 | 60 |
| stroke 571 | 31 % → 0 % | 45.1 px | 0.00 | 0.00 | 33 |
| stroke 572 | 32 % → 0 % | 40.3 px | 0.00 | 0.00 | 55 |
| stroke 573 | 38 % → 0 % | 40.5 px | 0.00 | 0.00 | 52 |
| stroke 574 | 40 % → 0 % | 47.3 px | 0.00 | 0.00 | 39 |
| stroke 575 | 28 % → 0 % | 37.6 px | 0.00 | 0.00 | 42 |
| stroke 576 | 30 % → 0 % | 37.9 px | 0.00 | 0.00 | 33 |
| stroke 577 | 52 % → 0 % | 49.4 px | 0.00 | 0.00 | 33 |
| stroke 578 | 58 % → 0 % | 188.4 px | 0.00 | 0.00 | 8 |
| stroke 579 | 58 % → 0 % | 63.2 px | 0.00 | 0.00 | 26 |
| stroke 580 | 62 % → 0 % | 90.8 px | 0.00 | 0.00 | 22 |
| stroke 581 | 32 % → 0 % | 31.5 px | 0.00 | 0.00 | 37 |
| stroke 582 | 27 % → 0 % | 37.5 px | 0.00 | 0.00 | 32 |
| stroke 583 | 4 % → 0 % | 10.0 px | 0.00 | 0.00 | 7 |
| stroke 584 | 6 % → 0 % | 8.7 px | 0.00 | 0.00 | 23 |
| stroke 585 | 6 % → 0 % | 9.1 px | 0.00 | 0.00 | 26 |
| stroke 586 | 7 % → 0 % | 11.3 px | 0.00 | 0.00 | 19 |
| stroke 587 | 10 % → 0 % | 15.7 px | 0.00 | 0.00 | 28 |
| stroke 588 | 16 % → 0 % | 33.1 px | 0.00 | 0.00 | 7 |
| stroke 589 | 11 % → 0 % | 20.0 px | 0.00 | 0.00 | 16 |
| stroke 590 | 20 % → 0 % | 41.5 px | 0.00 | 0.00 | 9 |
| stroke 591 | 25 % → 0 % | 39.3 px | 0.00 | 0.00 | 17 |
| stroke 592 | 26 % → 0 % | 46.8 px | 0.00 | 0.00 | 6 |
| stroke 593 | 25 % → 0 % | 46.3 px | 0.00 | 0.00 | 12 |
| stroke 594 | 37 % → 0 % | 67.5 px | 0.00 | 0.00 | 14 |
| stroke 595 | 17 % → 0 % | 41.6 px | 0.00 | 0.00 | 6 |
| stroke 596 | 42 % → 0 % | 86.0 px | 0.00 | 0.00 | 5 |
| stroke 597 | 32 % → 0 % | 87.7 px | 0.00 | 0.00 | 2 |
| stroke 598 | 32 % → 0 % | 65.3 px | 0.00 | 0.00 | 7 |
| stroke 599 | 24 % → 0 % | 66.4 px | 0.00 | 0.00 | 3 |
| stroke 600 | 25 % → 0 % | 66.8 px | 0.00 | 0.00 | 15 |
| stroke 601 | 23 % → 0 % | 65.8 px | 0.00 | 0.00 | 5 |
| stroke 602 | 38 % → 0 % | 102.0 px | 0.00 | 0.00 | 4 |
| stroke 603 | 24 % → 0 % | 31.1 px | 0.00 | 0.00 | 47 |
| stroke 604 | 37 % → 0 % | 48.0 px | 0.00 | 0.00 | 49 |
| stroke 605 | 24 % → 0 % | 33.4 px | 0.00 | 0.00 | 52 |
| stroke 606 | 24 % → 0 % | 28.6 px | 0.00 | 0.00 | 54 |
| stroke 607 | 35 % → 0 % | 48.5 px | 0.00 | 0.00 | 56 |
| stroke 608 | 31 % → 0 % | 37.6 px | 0.00 | 0.00 | 53 |
| stroke 609 | 30 % → 0 % | 133.7 px | 0.00 | 0.00 | 5 |
| stroke 610 | 5 % → 0 % | 10.3 px | 0.00 | 0.00 | 7 |
| stroke 611 | 11 % → 0 % | 22.0 px | 0.00 | 0.00 | 4 |
| stroke 612 | 11 % → 0 % | 8.7 px | 0.00 | 0.00 | 46 |
| stroke 613 | 17 % → 0 % | 89.1 px | 0.00 | 0.00 | 2 |
| stroke 614 | 7 % → 0 % | 10.9 px | 0.00 | 0.00 | 32 |
| stroke 615 | 14 % → 0 % | 29.3 px | 0.00 | 0.00 | 6 |
| stroke 616 | 20 % → 0 % | 34.0 px | 0.00 | 0.00 | 9 |
| stroke 617 | 11 % → 0 % | 12.1 px | 0.00 | 0.00 | 22 |
| stroke 618 | 26 % → 0 % | 35.0 px | 0.00 | 0.00 | 16 |
| stroke 619 | 20 % → 0 % | 46.2 px | 0.00 | 0.00 | 6 |
| stroke 620 | 25 % → 0 % | 30.8 px | 0.00 | 0.00 | 45 |
| stroke 621 | 25 % → 0 % | 25.7 px | 0.00 | 0.00 | 30 |
| stroke 622 | 41 % → 0 % | 37.6 px | 0.00 | 0.00 | 70 |
| stroke 623 | 39 % → 0 % | 46.4 px | 0.00 | 0.00 | 38 |
| stroke 624 | 23 % → 0 % | 15.0 px | 0.00 | 0.00 | 58 |
| stroke 625 | 11 % → 0 % | 13.9 px | 0.00 | 0.00 | 21 |
| stroke 626 | 18 % → 0 % | 15.2 px | 0.00 | 0.00 | 16 |
| stroke 627 | 22 % → 0 % | 31.5 px | 0.00 | 0.00 | 21 |
| stroke 628 | 18 % → 0 % | 30.5 px | 0.00 | 0.00 | 11 |
| stroke 629 | 9 % → 0 % | 10.8 px | 0.00 | 0.00 | 9 |
| stroke 630 | 17 % → 0 % | 18.0 px | 0.00 | 0.00 | 18 |
| stroke 631 | 16 % → 0 % | 13.3 px | 0.00 | 0.00 | 17 |
| stroke 632 | 18 % → 0 % | 36.5 px | 0.00 | 0.00 | 3 |
| stroke 633 | 15 % → 0 % | 33.9 px | 0.00 | 0.00 | 5 |
| stroke 634 | 35 % → 0 % | 33.1 px | 0.00 | 0.00 | 12 |
| stroke 635 | 23 % → 0 % | 48.8 px | 0.00 | 0.00 | 8 |
| stroke 636 | 27 % → 0 % | 18.0 px | 0.00 | 0.00 | 20 |
| stroke 637 | 32 % → 0 % | 23.6 px | 0.00 | 0.00 | 58 |
| stroke 638 | 42 % → 0 % | 21.2 px | 0.00 | 0.00 | 53 |
| stroke 639 | 35 % → 0 % | 31.3 px | 0.00 | 0.00 | 34 |
| stroke 640 | 29 % → 0 % | 35.9 px | 0.00 | 0.00 | 16 |
| stroke 641 | 32 % → 0 % | 30.3 px | 0.00 | 0.00 | 27 |
| stroke 642 | 16 % → 0 % | 31.0 px | 0.00 | 0.00 | 9 |
| stroke 643 | 12 % → 0 % | 19.5 px | 0.00 | 0.00 | 17 |
| stroke 644 | 22 % → 0 % | 61.4 px | 0.00 | 0.00 | 2 |
| stroke 645 | 21 % → 0 % | 19.2 px | 0.00 | 0.00 | 41 |
| stroke 646 | 30 % → 0 % | 28.7 px | 0.00 | 0.00 | 30 |
| stroke 647 | 9 % → 0 % | 13.5 px | 0.00 | 0.00 | 27 |
| stroke 648 | 6 % → 0 % | 8.8 px | 0.00 | 0.00 | 17 |
| stroke 649 | 11 % → 0 % | 17.3 px | 0.00 | 0.00 | 35 |
| stroke 650 | 6 % → 0 % | 9.5 px | 0.00 | 0.00 | 10 |
| stroke 651 | 6 % → 0 % | 8.9 px | 0.00 | 0.00 | 16 |
| stroke 652 | 17 % → 0 % | 30.6 px | 0.00 | 0.00 | 11 |
| stroke 653 | 8 % → 0 % | 12.5 px | 0.00 | 0.00 | 10 |
| stroke 654 | 24 % → 0 % | 39.3 px | 0.00 | 0.00 | 33 |
| stroke 655 | 22 % → 0 % | 29.9 px | 0.00 | 0.00 | 11 |
| stroke 656 | 19 % → 0 % | 24.4 px | 0.00 | 0.00 | 34 |
| stroke 657 | 7 % → 0 % | 8.7 px | 0.00 | 0.00 | 28 |
| stroke 658 | 18 % → 0 % | 25.8 px | 0.00 | 0.00 | 53 |
| stroke 659 | 30 % → 0 % | 66.5 px | 0.00 | 0.00 | 15 |
| stroke 660 | 15 % → 0 % | 18.6 px | 0.00 | 0.00 | 46 |
| stroke 661 | 14 % → 0 % | 34.0 px | 0.00 | 0.00 | 29 |
| stroke 662 | 20 % → 0 % | 25.4 px | 0.00 | 0.00 | 29 |
| stroke 663 | 24 % → 0 % | 30.2 px | 0.00 | 0.00 | 25 |
| stroke 664 | 18 % → 0 % | 22.3 px | 0.00 | 0.00 | 23 |
| stroke 665 | 19 % → 0 % | 26.4 px | 0.00 | 0.00 | 10 |
| stroke 666 | 29 % → 0 % | 46.6 px | 0.00 | 0.00 | 19 |
| stroke 667 | 35 % → 0 % | 55.7 px | 0.00 | 0.00 | 15 |
| stroke 668 | 29 % → 0 % | 46.6 px | 0.00 | 0.00 | 13 |
| stroke 669 | 33 % → 0 % | 41.3 px | 0.00 | 0.00 | 16 |
| stroke 670 | 30 % → 0 % | 41.3 px | 0.00 | 0.00 | 18 |
| stroke 671 | 26 % → 0 % | 30.5 px | 0.00 | 0.00 | 24 |
| stroke 672 | 26 % → 0 % | 40.1 px | 0.00 | 0.00 | 14 |
| stroke 673 | 18 % → 0 % | 40.0 px | 0.00 | 0.00 | 18 |
| stroke 674 | 22 % → 0 % | 60.2 px | 0.00 | 0.00 | 3 |
| stroke 675 | 20 % → 0 % | 53.4 px | 0.00 | 0.00 | 10 |
| stroke 676 | 28 % → 0 % | 41.2 px | 0.00 | 0.00 | 20 |
| stroke 677 | 32 % → 0 % | 77.4 px | 0.00 | 0.00 | 6 |
| stroke 678 | 27 % → 0 % | 51.1 px | 0.00 | 0.00 | 6 |
| stroke 679 | 17 % → 0 % | 48.6 px | 0.00 | 0.00 | 6 |
| stroke 680 | 44 % → 0 % | 106.5 px | 0.00 | 0.00 | 7 |
| stroke 681 | 35 % → 0 % | 57.6 px | 0.00 | 0.00 | 12 |
| stroke 682 | 43 % → 0 % | 105.5 px | 0.00 | 0.00 | 10 |
| stroke 683 | 49 % → 0 % | 82.9 px | 0.00 | 0.00 | 8 |
| stroke 684 | 18 % → 0 % | 40.0 px | 0.00 | 0.00 | 13 |
| stroke 685 | 47 % → 0 % | 126.7 px | 0.00 | 0.00 | 8 |
| stroke 686 | 31 % → 0 % | 62.3 px | 0.00 | 0.00 | 10 |
| stroke 687 | 22 % → 0 % | 48.6 px | 0.00 | 0.00 | 3 |
| stroke 688 | 35 % → 0 % | 83.4 px | 0.00 | 0.00 | 4 |
| stroke 689 | 35 % → 0 % | 97.9 px | 0.00 | 0.00 | 3 |
| stroke 690 | 36 % → 0 % | 98.5 px | 0.00 | 0.00 | 13 |
| stroke 691 | 27 % → 0 % | 40.1 px | 0.00 | 0.00 | 43 |
| stroke 692 | 31 % → 0 % | 37.8 px | 0.00 | 0.00 | 47 |
| stroke 693 | 29 % → 0 % | 27.8 px | 0.00 | 0.00 | 60 |
| stroke 694 | 31 % → 0 % | 31.6 px | 0.00 | 0.00 | 48 |
| stroke 695 | 44 % → 0 % | 45.6 px | 0.00 | 0.00 | 41 |
| stroke 696 | 38 % → 0 % | 48.6 px | 0.00 | 0.00 | 44 |
| stroke 697 | 37 % → 0 % | 45.4 px | 0.00 | 0.00 | 58 |
| stroke 698 | 43 % → 0 % | 40.6 px | 0.00 | 0.00 | 52 |
| stroke 699 | 50 % → 0 % | 53.5 px | 0.00 | 0.00 | 42 |
| stroke 700 | 41 % → 0 % | 53.6 px | 0.00 | 0.00 | 67 |
| stroke 701 | 33 % → 0 % | 26.0 px | 0.00 | 0.00 | 49 |
| stroke 702 | 46 % → 0 % | 50.3 px | 0.00 | 0.00 | 55 |
| stroke 703 | 42 % → 0 % | 56.3 px | 0.00 | 0.00 | 46 |
| stroke 704 | 35 % → 0 % | 40.8 px | 0.00 | 0.00 | 55 |
| stroke 705 | 32 % → 0 % | 29.3 px | 0.00 | 0.00 | 48 |
| stroke 706 | 39 % → 0 % | 51.2 px | 0.00 | 0.00 | 42 |
| stroke 707 | 40 % → 0 % | 54.6 px | 0.00 | 0.00 | 44 |
| stroke 708 | 35 % → 0 % | 43.8 px | 0.00 | 0.00 | 42 |
| stroke 709 | 32 % → 0 % | 43.4 px | 0.00 | 0.00 | 42 |
| stroke 710 | 62 % → 0 % | 59.0 px | 0.00 | 0.00 | 44 |
| stroke 711 | 67 % → 0 % | 218.3 px | 0.00 | 0.00 | 5 |
| stroke 712 | 10 % → 0 % | 12.5 px | 0.00 | 0.00 | 17 |
| stroke 713 | 10 % → 0 % | 10.8 px | 0.00 | 0.00 | 34 |
| stroke 714 | 12 % → 0 % | 15.0 px | 0.00 | 0.00 | 28 |
| stroke 715 | 23 % → 0 % | 24.0 px | 0.00 | 0.00 | 21 |
| stroke 716 | 24 % → 0 % | 47.4 px | 0.00 | 0.00 | 7 |
| stroke 717 | 15 % → 0 % | 17.7 px | 0.00 | 0.00 | 11 |
| stroke 718 | 23 % → 0 % | 58.4 px | 0.00 | 0.00 | 9 |
| stroke 719 | 11 % → 0 % | 21.2 px | 0.00 | 0.00 | 9 |
| stroke 720 | 16 % → 0 % | 40.0 px | 0.00 | 0.00 | 6 |
| stroke 721 | 25 % → 0 % | 38.4 px | 0.00 | 0.00 | 7 |
| stroke 722 | 23 % → 0 % | 43.3 px | 0.00 | 0.00 | 6 |
| stroke 723 | 47 % → 0 % | 70.5 px | 0.00 | 0.00 | 7 |
| stroke 724 | 30 % → 0 % | 76.3 px | 0.00 | 0.00 | 7 |
| stroke 725 | 39 % → 0 % | 91.1 px | 0.00 | 0.00 | 15 |
| stroke 726 | 33 % → 0 % | 42.2 px | 0.00 | 0.00 | 41 |
| stroke 727 | 40 % → 0 % | 46.3 px | 0.00 | 0.00 | 30 |
| stroke 728 | 37 % → 0 % | 40.7 px | 0.00 | 0.00 | 44 |
| stroke 729 | 21 % → 0 % | 19.2 px | 0.00 | 0.00 | 38 |
| stroke 730 | 39 % → 0 % | 43.6 px | 0.00 | 0.00 | 35 |
| stroke 731 | 42 % → 0 % | 44.4 px | 0.00 | 0.00 | 33 |
| stroke 732 | 39 % → 0 % | 43.3 px | 0.00 | 0.00 | 39 |
| stroke 733 | 42 % → 0 % | 24.5 px | 0.00 | 0.00 | 35 |
| stroke 734 | 24 % → 0 % | 19.8 px | 0.00 | 0.00 | 27 |
| stroke 735 | 18 % → 0 % | 22.5 px | 0.00 | 0.00 | 18 |
| stroke 736 | 10 % → 0 % | 21.1 px | 0.00 | 0.00 | 3 |
| stroke 737 | 13 % → 0 % | 13.0 px | 0.00 | 0.00 | 19 |
| stroke 738 | 5 % → 0 % | 10.3 px | 0.00 | 0.00 | 29 |
| stroke 739 | 11 % → 0 % | 18.3 px | 0.00 | 0.00 | 13 |
| stroke 740 | 21 % → 0 % | 58.1 px | 0.00 | 0.00 | 2 |
| stroke 741 | 14 % → 0 % | 14.5 px | 0.00 | 0.00 | 30 |
| stroke 742 | 18 % → 0 % | 23.8 px | 0.00 | 0.00 | 35 |
| stroke 743 | 14 % → 0 % | 33.1 px | 0.00 | 0.00 | 9 |
| stroke 744 | 20 % → 0 % | 18.0 px | 0.00 | 0.00 | 37 |
| stroke 745 | 5 % → 0 % | 11.4 px | 0.00 | 0.00 | 4 |
| stroke 746 | 11 % → 0 % | 19.2 px | 0.00 | 0.00 | 7 |
| stroke 747 | 13 % → 0 % | 11.6 px | 0.00 | 0.00 | 27 |
| stroke 748 | 4 % → 0 % | 10.2 px | 0.00 | 0.00 | 8 |
| stroke 749 | 7 % → 0 % | 10.0 px | 0.00 | 0.00 | 11 |
| stroke 750 | 22 % → 0 % | 58.7 px | 0.00 | 0.00 | 3 |
| stroke 751 | 24 % → 0 % | 31.7 px | 0.00 | 0.00 | 18 |
| stroke 752 | 9 % → 0 % | 11.0 px | 0.00 | 0.00 | 54 |
| stroke 753 | 7 % → 0 % | 11.5 px | 0.00 | 0.00 | 27 |
| stroke 754 | 19 % → 0 % | 18.3 px | 0.00 | 0.00 | 67 |
| stroke 755 | 15 % → 0 % | 32.8 px | 0.00 | 0.00 | 4 |
| stroke 756 | 34 % → 0 % | 39.7 px | 0.00 | 0.00 | 15 |
| stroke 757 | 28 % → 0 % | 32.7 px | 0.00 | 0.00 | 53 |
| stroke 758 | 26 % → 0 % | 35.4 px | 0.00 | 0.00 | 55 |
| stroke 759 | 33 % → 0 % | 31.3 px | 0.00 | 0.00 | 49 |
| stroke 760 | 33 % → 0 % | 92.1 px | 0.00 | 0.00 | 4 |
| stroke 761 | 15 % → 0 % | 39.5 px | 0.00 | 0.00 | 6 |
| stroke 762 | 20 % → 0 % | 25.3 px | 0.00 | 0.00 | 14 |
| stroke 763 | 9 % → 0 % | 10.6 px | 0.00 | 0.00 | 27 |
| stroke 764 | 23 % → 0 % | 51.5 px | 0.00 | 0.00 | 7 |
| stroke 765 | 15 % → 0 % | 40.4 px | 0.00 | 0.00 | 7 |
| stroke 766 | 18 % → 0 % | 16.1 px | 0.00 | 0.00 | 34 |
| stroke 767 | 24 % → 0 % | 25.5 px | 0.00 | 0.00 | 29 |
| stroke 768 | 10 % → 0 % | 11.6 px | 0.00 | 0.00 | 18 |
| stroke 769 | 10 % → 0 % | 14.5 px | 0.00 | 0.00 | 18 |
| stroke 770 | 19 % → 0 % | 30.0 px | 0.00 | 0.00 | 7 |
| stroke 771 | 21 % → 0 % | 34.8 px | 0.00 | 0.00 | 9 |
| stroke 772 | 26 % → 0 % | 34.0 px | 0.00 | 0.00 | 10 |
| stroke 773 | 16 % → 0 % | 31.4 px | 0.00 | 0.00 | 9 |
| stroke 774 | 23 % → 0 % | 25.1 px | 0.00 | 0.00 | 34 |
| stroke 775 | 28 % → 0 % | 30.1 px | 0.00 | 0.00 | 50 |
| stroke 776 | 33 % → 0 % | 32.4 px | 0.00 | 0.00 | 46 |
| stroke 777 | 30 % → 0 % | 28.8 px | 0.00 | 0.00 | 50 |
| stroke 778 | 35 % → 0 % | 38.9 px | 0.00 | 0.00 | 31 |
| stroke 779 | 5 % → 0 % | 13.2 px | 0.00 | 0.00 | 4 |
| stroke 780 | 10 % → 0 % | 14.9 px | 0.00 | 0.00 | 9 |
| stroke 781 | 20 % → 0 % | 42.4 px | 0.00 | 0.00 | 4 |
| stroke 782 | 20 % → 0 % | 52.0 px | 0.00 | 0.00 | 12 |
| stroke 783 | 16 % → 0 % | 18.1 px | 0.00 | 0.00 | 23 |
| stroke 784 | 20 % → 0 % | 16.2 px | 0.00 | 0.00 | 46 |
| stroke 785 | 21 % → 0 % | 40.2 px | 0.00 | 0.00 | 10 |
| stroke 786 | 7 % → 0 % | 11.1 px | 0.00 | 0.00 | 24 |
| stroke 787 | 12 % → 0 % | 15.7 px | 0.00 | 0.00 | 34 |
| stroke 788 | 21 % → 0 % | 41.7 px | 0.00 | 0.00 | 5 |
| stroke 789 | 14 % → 0 % | 38.1 px | 0.00 | 0.00 | 8 |
| stroke 790 | 32 % → 0 % | 85.8 px | 0.00 | 0.00 | 4 |
| stroke 791 | 27 % → 0 % | 73.4 px | 0.00 | 0.00 | 11 |
| stroke 792 | 23 % → 0 % | 27.5 px | 0.00 | 0.00 | 42 |
| stroke 793 | 24 % → 0 % | 23.2 px | 0.00 | 0.00 | 46 |
| stroke 794 | 33 % → 0 % | 40.1 px | 0.00 | 0.00 | 34 |
| stroke 795 | 38 % → 0 % | 39.4 px | 0.00 | 0.00 | 27 |
| stroke 796 | 10 % → 0 % | 26.8 px | 0.00 | 0.00 | 6 |
| stroke 797 | 16 % → 0 % | 23.8 px | 0.00 | 0.00 | 7 |
| stroke 798 | 7 % → 0 % | 17.9 px | 0.00 | 0.00 | 5 |
| stroke 799 | 10 % → 0 % | 12.6 px | 0.00 | 0.00 | 16 |
| stroke 800 | 5 % → 0 % | 12.1 px | 0.00 | 0.00 | 2 |
| stroke 801 | 10 % → 0 % | 23.2 px | 0.00 | 0.00 | 6 |
| stroke 802 | 14 % → 0 % | 35.8 px | 0.00 | 0.00 | 5 |
| stroke 803 | 15 % → 0 % | 10.6 px | 0.00 | 0.00 | 48 |
| stroke 804 | 28 % → 0 % | 55.6 px | 0.00 | 0.00 | 7 |
| stroke 805 | 6 % → 0 % | 12.1 px | 0.20 | 0.03 | 15 |
| stroke 806 | 13 % → 0 % | 8.3 px | 0.00 | 0.00 | 32 |
| stroke 807 | 11 % → 0 % | 9.1 px | 0.00 | 0.00 | 34 |
| stroke 808 | 27 % → 0 % | 17.0 px | 0.00 | 0.00 | 29 |
| stroke 809 | 19 % → 0 % | 42.9 px | 0.00 | 0.00 | 3 |
| stroke 810 | 26 % → 0 % | 32.0 px | 0.00 | 0.00 | 6 |
| stroke 811 | 22 % → 0 % | 49.1 px | 0.00 | 0.00 | 5 |
| stroke 812 | 25 % → 0 % | 29.1 px | 0.00 | 0.00 | 26 |
| stroke 813 | 11 % → 0 % | 17.2 px | 0.00 | 0.00 | 8 |
| stroke 814 | 31 % → 0 % | 52.5 px | 0.00 | 0.00 | 4 |
| stroke 815 | 28 % → 0 % | 19.3 px | 0.00 | 0.00 | 99 |
| stroke 816 | 40 % → 0 % | 22.6 px | 0.00 | 0.00 | 56 |
| stroke 817 | 29 % → 0 % | 15.8 px | 0.00 | 0.00 | 63 |
| stroke 818 | 31 % → 0 % | 26.8 px | 0.00 | 0.00 | 42 |
| stroke 819 | 30 % → 0 % | 32.0 px | 0.00 | 0.00 | 54 |
| stroke 820 | 7 % → 0 % | 10.3 px | 0.00 | 0.00 | 7 |
| stroke 821 | 14 % → 0 % | 13.5 px | 0.00 | 0.00 | 10 |
| stroke 822 | 18 % → 0 % | 15.9 px | 0.00 | 0.00 | 14 |
| stroke 823 | 20 % → 0 % | 13.3 px | 0.00 | 0.00 | 18 |
| stroke 824 | 8 % → 0 % | 10.8 px | 0.00 | 0.00 | 28 |
| stroke 825 | 10 % → 0 % | 16.1 px | 0.00 | 0.00 | 46 |
| stroke 826 | 14 % → 0 % | 30.0 px | 0.00 | 0.00 | 5 |
| stroke 827 | 11 % → 0 % | 19.0 px | 0.00 | 0.00 | 9 |
| stroke 828 | 26 % → 0 % | 48.6 px | 0.00 | 0.00 | 12 |
| stroke 829 | 10 % → 0 % | 19.3 px | 0.00 | 0.00 | 15 |
| stroke 830 | 10 % → 0 % | 16.5 px | 0.00 | 0.00 | 52 |
| stroke 831 | 19 % → 0 % | 25.6 px | 0.00 | 0.00 | 31 |
| stroke 832 | 31 % → 0 % | 49.1 px | 0.00 | 0.00 | 19 |
| stroke 833 | 28 % → 0 % | 75.8 px | 0.00 | 0.00 | 3 |
| stroke 834 | 12 % → 0 % | 34.5 px | 0.00 | 0.00 | 4 |
| stroke 835 | 48 % → 0 % | 123.2 px | 0.00 | 0.00 | 5 |
| stroke 836 | 22 % → 0 % | 61.4 px | 0.00 | 0.00 | 4 |
| stroke 837 | 16 % → 0 % | 14.5 px | 0.00 | 0.00 | 30 |
| stroke 838 | 24 % → 0 % | 25.2 px | 0.00 | 0.00 | 49 |
| stroke 839 | 29 % → 0 % | 41.2 px | 0.00 | 0.00 | 67 |
| stroke 840 | 27 % → 0 % | 26.8 px | 0.00 | 0.00 | 54 |
| stroke 841 | 33 % → 0 % | 37.9 px | 0.00 | 0.00 | 63 |
| stroke 842 | 31 % → 0 % | 44.9 px | 0.00 | 0.00 | 57 |
| stroke 843 | 27 % → 0 % | 34.7 px | 0.00 | 0.00 | 62 |
| stroke 844 | 20 % → 0 % | 238.5 px | 0.00 | 0.00 | 1 |
| stroke 845 | 9 % → 0 % | 10.4 px | 0.00 | 0.00 | 32 |
| stroke 846 | 7 % → 0 % | 9.8 px | 0.00 | 0.00 | 22 |
| stroke 847 | 6 % → 12 % | 9.1 px | 0.21 | 1.90 | 16 |
| stroke 848 | 14 % → 0 % | 25.8 px | 0.00 | 0.00 | 13 |
| stroke 849 | 9 % → 0 % | 13.0 px | 0.00 | 0.00 | 97 |
| stroke 850 | 22 % → 0 % | 29.8 px | 0.00 | 0.00 | 104 |
| stroke 851 | 28 % → 0 % | 45.7 px | 0.00 | 0.00 | 35 |
| stroke 852 | 15 % → 0 % | 19.9 px | 0.00 | 0.00 | 139 |
| stroke 853 | 11 % → 0 % | 16.5 px | 0.21 | 0.01 | 28 |
| stroke 854 | 18 % → 0 % | 29.2 px | 0.00 | 0.00 | 50 |
| stroke 855 | 14 % → 0 % | 30.8 px | 0.00 | 0.00 | 20 |
| stroke 856 | 42 % → 0 % | 92.8 px | 0.00 | 0.00 | 40 |
| stroke 857 | 13 % → 0 % | 20.4 px | 0.00 | 0.00 | 41 |
| stroke 858 | 15 % → 0 % | 37.0 px | 0.00 | 0.00 | 12 |
| stroke 859 | 33 % → 0 % | 52.4 px | 0.00 | 0.00 | 75 |
| stroke 860 | 15 % → 0 % | 42.7 px | 0.00 | 0.00 | 46 |
| stroke 861 | 35 % → 0 % | 69.1 px | 0.00 | 0.00 | 14 |
| stroke 862 | 17 % → 6 % | 45.8 px | 0.21 | 0.35 | 8 |
| stroke 863 | 42 % → 0 % | 47.5 px | 0.00 | 0.00 | 45 |
| stroke 864 | 27 % → 0 % | 40.7 px | 0.00 | 0.00 | 10 |
| stroke 865 | 33 % → 0 % | 91.1 px | 0.00 | 0.00 | 9 |
| stroke 866 | 35 % → 0 % | 96.4 px | 0.00 | 0.00 | 9 |
| stroke 867 | 26 % → 0 % | 28.9 px | 0.00 | 0.00 | 57 |
| stroke 868 | 24 % → 0 % | 27.8 px | 0.00 | 0.00 | 80 |
| stroke 869 | 43 % → 0 % | 46.8 px | 0.00 | 0.00 | 45 |
| stroke 870 | 36 % → 0 % | 36.9 px | 0.00 | 0.00 | 92 |
| stroke 871 | 36 % → 0 % | 47.7 px | 0.00 | 0.00 | 69 |
| stroke 872 | 25 % → 0 % | 22.7 px | 0.00 | 0.00 | 61 |
| stroke 873 | 32 % → 0 % | 41.2 px | 0.00 | 0.00 | 47 |
| stroke 874 | 44 % → 0 % | 46.9 px | 0.00 | 0.00 | 37 |
| stroke 875 | 34 % → 0 % | 37.1 px | 0.00 | 0.00 | 75 |
| stroke 876 | 27 % → 0 % | 33.7 px | 0.00 | 0.00 | 35 |
| stroke 877 | 57 % → 0 % | 62.7 px | 0.00 | 0.00 | 74 |
| stroke 878 | 67 % → 0 % | 76.4 px | 0.00 | 0.00 | 86 |
| stroke 879 | 19 % → 15 % | 17.2 px | 0.21 | 0.81 | 52 |
| stroke 880 | 20 % → 12 % | 24.0 px | 0.21 | 0.61 | 29 |
| stroke 881 | 13 % → 0 % | 17.1 px | 0.00 | 0.00 | 65 |
| stroke 882 | 11 % → 0 % | 18.0 px | 0.00 | 0.00 | 24 |
| stroke 883 | 18 % → 0 % | 30.1 px | 0.00 | 0.00 | 13 |
| stroke 884 | 24 % → 0 % | 29.6 px | 0.00 | 0.00 | 27 |
| stroke 885 | 29 % → 0 % | 38.5 px | 0.00 | 0.00 | 29 |
| stroke 886 | 36 % → 0 % | 61.6 px | 0.00 | 0.00 | 24 |
| stroke 887 | 30 % → 0 % | 76.0 px | 0.00 | 0.00 | 4 |
| stroke 888 | 23 % → 0 % | 37.4 px | 0.00 | 0.00 | 17 |
| stroke 889 | 21 % → 0 % | 50.6 px | 0.00 | 0.00 | 6 |
| stroke 890 | 48 % → 0 % | 135.1 px | 0.00 | 0.00 | 4 |
| stroke 891 | 43 % → 0 % | 121.8 px | 0.00 | 0.00 | 3 |
| stroke 892 | 31 % → 0 % | 86.9 px | 0.00 | 0.00 | 3 |
| stroke 893 | 30 % → 0 % | 30.9 px | 0.00 | 0.00 | 42 |
| stroke 894 | 34 % → 0 % | 48.3 px | 0.00 | 0.00 | 131 |
| stroke 895 | 33 % → 0 % | 40.0 px | 0.00 | 0.00 | 64 |
| stroke 896 | 46 % → 0 % | 54.6 px | 0.00 | 0.00 | 38 |
| stroke 897 | 55 % → 0 % | 78.9 px | 0.00 | 0.00 | 47 |
| stroke 898 | 40 % → 0 % | 56.2 px | 0.00 | 0.00 | 39 |
| stroke 899 | 7 % → 0 % | 11.5 px | 0.00 | 0.00 | 18 |
| stroke 900 | 12 % → 0 % | 17.1 px | 0.00 | 0.00 | 20 |
| stroke 901 | 18 % → 0 % | 34.4 px | 0.00 | 0.00 | 6 |
| stroke 902 | 15 % → 0 % | 15.1 px | 0.00 | 0.00 | 48 |
| stroke 903 | 20 % → 0 % | 18.7 px | 0.00 | 0.00 | 60 |
| stroke 904 | 16 % → 0 % | 191.2 px | 0.00 | 0.00 | 0 |
| stroke 905 | 8 % → 0 % | 10.7 px | 0.00 | 0.00 | 17 |
| stroke 906 | 19 % → 0 % | 19.6 px | 0.00 | 0.00 | 22 |
| stroke 907 | 9 % → 15 % | 15.4 px | 0.17 | 1.69 | 7 |
| stroke 908 | 27 % → 0 % | 30.3 px | 0.00 | 0.00 | 19 |
| stroke 909 | 28 % → 6 % | 37.1 px | 0.17 | 0.20 | 26 |
| stroke 910 | 28 % → 7 % | 32.9 px | 0.17 | 0.26 | 67 |
| stroke 911 | 30 % → 0 % | 30.6 px | 0.00 | 0.00 | 88 |
| stroke 912 | 38 % → 0 % | 42.0 px | 0.20 | 0.01 | 67 |
| stroke 913 | 28 % → 12 % | 43.2 px | 0.17 | 0.42 | 19 |
| stroke 914 | 7 % → 22 % | 10.6 px | 0.20 | 3.05 | 33 |
| stroke 915 | 11 % → 12 % | 20.9 px | 0.20 | 1.05 | 7 |
| stroke 916 | 15 % → 3 % | 17.4 px | 0.21 | 0.21 | 26 |
| stroke 917 | 26 % → 0 % | 33.7 px | 0.00 | 0.00 | 19 |
| stroke 918 | 17 % → 19 % | 32.0 px | 0.19 | 1.09 | 24 |
| stroke 919 | 16 % → 22 % | 21.9 px | 0.20 | 1.36 | 52 |
| stroke 920 | 26 % → 9 % | 27.7 px | 0.21 | 0.36 | 71 |
| stroke 921 | 25 % → 1 % | 25.3 px | 0.20 | 0.05 | 48 |
| stroke 922 | 30 % → 17 % | 36.2 px | 0.20 | 0.57 | 56 |
| stroke 923 | 20 % → 29 % | 37.4 px | 0.19 | 1.42 | 32 |
| stroke 924 | 9 % → 23 % | 10.4 px | 0.16 | 2.69 | 22 |
| stroke 925 | 8 % → 13 % | 12.6 px | 0.15 | 1.59 | 13 |
| stroke 926 | 12 % → 40 % | 19.2 px | 0.16 | 3.36 | 13 |
| stroke 927 | 20 % → 43 % | 47.3 px | 0.16 | 2.13 | 6 |
| stroke 928 | 14 % → 29 % | 24.3 px | 0.16 | 2.09 | 12 |
| stroke 929 | 28 % → 10 % | 77.3 px | 0.15 | 0.35 | 4 |
| stroke 930 | 25 % → 2 % | 60.6 px | 0.15 | 0.07 | 5 |
| stroke 931 | 30 % → 18 % | 65.6 px | 0.15 | 0.60 | 9 |
| stroke 932 | 25 % → 44 % | 61.2 px | 0.15 | 1.76 | 4 |
| stroke 933 | 28 % → 28 % | 37.4 px | 0.16 | 1.03 | 52 |
| stroke 934 | 22 % → 38 % | 19.3 px | 0.16 | 1.76 | 40 |
| stroke 935 | 33 % → 18 % | 35.2 px | 0.15 | 0.54 | 49 |
| stroke 936 | 28 % → 32 % | 36.0 px | 0.16 | 1.16 | 34 |
| stroke 937 | 10 % → 36 % | 18.0 px | 0.18 | 3.43 | 13 |
| stroke 938 | 10 % → 32 % | 15.6 px | 0.17 | 3.16 | 16 |
| stroke 939 | 6 % → 0 % | 9.7 px | 0.00 | 0.00 | 18 |
| stroke 940 | 6 % → 0 % | 10.0 px | 0.00 | 0.00 | 16 |
| stroke 941 | 13 % → 0 % | 29.5 px | 0.00 | 0.00 | 5 |
| stroke 942 | 9 % → 0 % | 13.8 px | 0.00 | 0.00 | 38 |
| stroke 943 | 11 % → 0 % | 16.9 px | 0.00 | 0.00 | 34 |
| stroke 944 | 12 % → 0 % | 20.2 px | 0.00 | 0.00 | 14 |
| stroke 945 | 20 % → 0 % | 31.0 px | 0.00 | 0.00 | 21 |
| stroke 946 | 12 % → 0 % | 18.7 px | 0.00 | 0.00 | 23 |
| stroke 947 | 15 % → 0 % | 43.2 px | 0.00 | 0.00 | 4 |
| stroke 948 | 31 % → 0 % | 61.6 px | 0.00 | 0.00 | 17 |
| stroke 949 | 17 % → 0 % | 28.5 px | 0.00 | 0.00 | 7 |
| stroke 950 | 27 % → 0 % | 46.8 px | 0.00 | 0.00 | 12 |
| stroke 951 | 21 % → 0 % | 43.7 px | 0.00 | 0.00 | 4 |
| stroke 952 | 25 % → 0 % | 41.7 px | 0.00 | 0.00 | 15 |
| stroke 953 | 37 % → 0 % | 103.2 px | 0.00 | 0.00 | 2 |
| stroke 954 | 30 % → 0 % | 60.2 px | 0.00 | 0.00 | 5 |
| stroke 955 | 46 % → 0 % | 77.2 px | 0.00 | 0.00 | 34 |
| stroke 956 | 28 % → 0 % | 68.5 px | 0.00 | 0.00 | 9 |
| stroke 957 | 30 % → 0 % | 66.4 px | 0.00 | 0.00 | 6 |
| stroke 958 | 41 % → 0 % | 100.7 px | 0.00 | 0.00 | 11 |
| stroke 959 | 32 % → 0 % | 65.6 px | 0.00 | 0.00 | 15 |
| stroke 960 | 35 % → 0 % | 34.4 px | 0.00 | 0.00 | 44 |
| stroke 961 | 34 % → 0 % | 37.9 px | 0.00 | 0.00 | 61 |
| stroke 962 | 26 % → 0 % | 37.4 px | 0.00 | 0.00 | 47 |
| stroke 963 | 36 % → 0 % | 50.1 px | 0.00 | 0.00 | 124 |
| stroke 964 | 51 % → 0 % | 61.7 px | 0.00 | 0.00 | 75 |
| stroke 965 | 35 % → 0 % | 39.7 px | 0.00 | 0.00 | 77 |
| stroke 966 | 29 % → 0 % | 40.7 px | 0.00 | 0.00 | 47 |
| stroke 967 | 28 % → 0 % | 28.9 px | 0.00 | 0.00 | 60 |
| stroke 968 | 30 % → 0 % | 40.6 px | 0.00 | 0.00 | 54 |
| stroke 969 | 40 % → 0 % | 51.8 px | 0.00 | 0.00 | 38 |
| stroke 970 | 38 % → 0 % | 110.2 px | 0.00 | 0.00 | 11 |
| stroke 971 | 14 % → 0 % | 23.5 px | 0.00 | 0.00 | 7 |
| stroke 972 | 20 % → 0 % | 17.2 px | 0.21 | 0.00 | 47 |
| stroke 973 | 5 % → 0 % | 9.9 px | 0.00 | 0.00 | 15 |
| stroke 974 | 6 % → 0 % | 8.5 px | 0.00 | 0.00 | 37 |
| stroke 975 | 14 % → 0 % | 22.7 px | 0.00 | 0.00 | 27 |
| stroke 976 | 9 % → 0 % | 13.7 px | 0.00 | 0.00 | 24 |
| stroke 977 | 9 % → 0 % | 13.3 px | 0.00 | 0.00 | 12 |
| stroke 978 | 14 % → 4 % | 22.8 px | 0.20 | 0.30 | 14 |
| stroke 979 | 11 % → 0 % | 19.0 px | 0.00 | 0.00 | 29 |
| stroke 980 | 18 % → 0 % | 40.7 px | 0.00 | 0.00 | 6 |
| stroke 981 | 21 % → 0 % | 35.3 px | 0.00 | 0.00 | 24 |
| stroke 982 | 18 % → 0 % | 46.1 px | 0.00 | 0.00 | 7 |
| stroke 983 | 30 % → 0 % | 72.9 px | 0.00 | 0.00 | 13 |
| stroke 984 | 35 % → 0 % | 61.1 px | 0.00 | 0.00 | 10 |
| stroke 985 | 17 % → 0 % | 36.5 px | 0.00 | 0.00 | 7 |
| stroke 986 | 22 % → 0 % | 52.5 px | 0.00 | 0.00 | 10 |
| stroke 987 | 20 % → 0 % | 34.5 px | 0.00 | 0.00 | 16 |
| stroke 988 | 46 % → 0 % | 112.6 px | 0.00 | 0.00 | 8 |
| stroke 989 | 18 % → 0 % | 50.2 px | 0.00 | 0.00 | 6 |
| stroke 990 | 36 % → 0 % | 100.8 px | 0.00 | 0.00 | 3 |
| stroke 991 | 29 % → 0 % | 36.6 px | 0.00 | 0.00 | 33 |
| stroke 992 | 30 % → 3 % | 37.2 px | 0.20 | 0.09 | 41 |
| stroke 993 | 29 % → 2 % | 36.6 px | 0.20 | 0.08 | 59 |
| stroke 994 | 35 % → 0 % | 55.3 px | 0.00 | 0.00 | 37 |
| stroke 995 | 31 % → 0 % | 54.4 px | 0.00 | 0.00 | 20 |
| stroke 996 | 28 % → 0 % | 35.2 px | 0.00 | 0.00 | 54 |
| stroke 997 | 20 % → 0 % | 19.9 px | 0.00 | 0.00 | 51 |
| stroke 998 | 31 % → 0 % | 39.7 px | 0.00 | 0.00 | 38 |
| stroke 999 | 36 % → 0 % | 35.5 px | 0.00 | 0.00 | 41 |
| stroke 1000 | 7 % → 0 % | 8.4 px | 0.00 | 0.00 | 17 |
| stroke 1001 | 11 % → 0 % | 15.0 px | 0.00 | 0.00 | 14 |
| stroke 1002 | 16 % → 2 % | 21.4 px | 0.19 | 0.14 | 9 |
| stroke 1003 | 13 % → 0 % | 32.6 px | 0.00 | 0.00 | 6 |
| stroke 1004 | 21 % → 4 % | 57.4 px | 0.15 | 0.19 | 3 |
| stroke 1005 | 17 % → 0 % | 14.4 px | 0.00 | 0.00 | 34 |
| stroke 1006 | 23 % → 0 % | 20.0 px | 0.15 | 0.01 | 39 |
| stroke 1007 | 28 % → 0 % | 33.8 px | 0.00 | 0.00 | 29 |
| stroke 1008 | 7 % → 0 % | 14.8 px | 0.00 | 0.00 | 9 |
| stroke 1009 | 14 % → 0 % | 12.7 px | 0.00 | 0.00 | 23 |
| stroke 1010 | 4 % → 0 % | 10.8 px | 0.00 | 0.00 | 6 |
| stroke 1011 | 8 % → 0 % | 18.0 px | 0.00 | 0.00 | 7 |
| stroke 1012 | 13 % → 0 % | 32.7 px | 0.00 | 0.00 | 3 |
| stroke 1013 | 11 % → 0 % | 31.5 px | 0.00 | 0.00 | 7 |
| stroke 1014 | 11 % → 0 % | 13.8 px | 0.00 | 0.00 | 37 |
| stroke 1015 | 15 % → 0 % | 16.6 px | 0.00 | 0.00 | 101 |
| stroke 1016 | 22 % → 0 % | 64.1 px | 0.00 | 0.00 | 6 |
| stroke 1017 | 5 % → 0 % | 8.6 px | 0.00 | 0.00 | 14 |
| stroke 1018 | 7 % → 0 % | 13.5 px | 0.00 | 0.00 | 4 |
| stroke 1019 | 13 % → 0 % | 10.0 px | 0.00 | 0.00 | 46 |
| stroke 1020 | 21 % → 0 % | 76.1 px | 0.00 | 0.00 | 7 |
| stroke 1021 | 19 % → 0 % | 20.2 px | 0.00 | 0.00 | 23 |
| stroke 1022 | 16 % → 0 % | 18.4 px | 0.00 | 0.00 | 15 |
| stroke 1023 | 6 % → 0 % | 11.0 px | 0.00 | 0.00 | 21 |
| stroke 1024 | 15 % → 0 % | 10.0 px | 0.00 | 0.00 | 29 |
| stroke 1025 | 14 % → 0 % | 11.6 px | 0.00 | 0.00 | 34 |
| stroke 1026 | 25 % → 0 % | 24.9 px | 0.00 | 0.00 | 20 |
| stroke 1027 | 34 % → 0 % | 40.0 px | 0.00 | 0.00 | 15 |
| stroke 1028 | 17 % → 0 % | 23.4 px | 0.00 | 0.00 | 32 |
| stroke 1029 | 23 % → 0 % | 56.6 px | 0.00 | 0.00 | 4 |
| stroke 1030 | 12 % → 0 % | 10.6 px | 0.00 | 0.00 | 20 |
| stroke 1031 | 23 % → 0 % | 37.0 px | 0.00 | 0.00 | 13 |
| stroke 1032 | 35 % → 0 % | 60.5 px | 0.00 | 0.00 | 8 |
| stroke 1033 | 33 % → 0 % | 87.5 px | 0.00 | 0.00 | 3 |
| stroke 1034 | 43 % → 0 % | 107.6 px | 0.00 | 0.00 | 3 |
| stroke 1035 | 42 % → 0 % | 77.0 px | 0.00 | 0.00 | 8 |
| stroke 1036 | 36 % → 0 % | 97.1 px | 0.00 | 0.00 | 6 |
| stroke 1037 | 32 % → 0 % | 32.2 px | 0.00 | 0.00 | 29 |
| stroke 1038 | 25 % → 0 % | 26.8 px | 0.00 | 0.00 | 35 |
| stroke 1039 | 37 % → 0 % | 38.8 px | 0.00 | 0.00 | 32 |
| stroke 1040 | 30 % → 0 % | 32.7 px | 0.00 | 0.00 | 33 |
| stroke 1041 | 47 % → 0 % | 34.5 px | 0.00 | 0.00 | 52 |
| stroke 1042 | 61 % → 0 % | 38.7 px | 0.00 | 0.00 | 51 |
| stroke 1043 | 49 % → 0 % | 84.9 px | 0.00 | 0.00 | 13 |
| stroke 1044 | 9 % → 0 % | 18.9 px | 0.00 | 0.00 | 9 |
| stroke 1045 | 12 % → 0 % | 24.4 px | 0.00 | 0.00 | 12 |
| stroke 1046 | 15 % → 0 % | 13.4 px | 0.00 | 0.00 | 39 |
| stroke 1047 | 7 % → 0 % | 8.8 px | 0.00 | 0.00 | 13 |
| stroke 1048 | 7 % → 0 % | 12.7 px | 0.00 | 0.00 | 13 |
| stroke 1049 | 16 % → 0 % | 30.7 px | 0.00 | 0.00 | 9 |
| stroke 1050 | 14 % → 0 % | 28.0 px | 0.00 | 0.00 | 8 |
| stroke 1051 | 15 % → 0 % | 42.1 px | 0.00 | 0.00 | 5 |
| stroke 1052 | 20 % → 0 % | 15.6 px | 0.00 | 0.00 | 47 |
| stroke 1053 | 19 % → 0 % | 20.4 px | 0.00 | 0.00 | 29 |
| stroke 1054 | 18 % → 0 % | 15.1 px | 0.00 | 0.00 | 44 |
| stroke 1055 | 26 % → 0 % | 163.9 px | 0.00 | 0.00 | 3 |
| stroke 1056 | 7 % → 0 % | 15.6 px | 0.00 | 0.00 | 7 |
| stroke 1057 | 19 % → 0 % | 18.6 px | 0.00 | 0.00 | 27 |
| stroke 1058 | 7 % → 15 % | 11.3 px | 0.17 | 2.15 | 17 |
| stroke 1059 | 12 % → 0 % | 10.1 px | 0.00 | 0.00 | 17 |
| stroke 1060 | 4 % → 0 % | 12.0 px | 0.00 | 0.00 | 6 |
| stroke 1061 | 8 % → 0 % | 9.1 px | 0.00 | 0.00 | 22 |
| stroke 1062 | 4 % → 0 % | 9.8 px | 0.00 | 0.00 | 4 |
| stroke 1063 | 8 % → 17 % | 9.3 px | 0.18 | 2.21 | 21 |
| stroke 1064 | 12 % → 12 % | 11.7 px | 0.21 | 1.07 | 25 |
| stroke 1065 | 9 % → 0 % | 9.9 px | 0.00 | 0.00 | 30 |
| stroke 1066 | 19 % → 3 % | 36.5 px | 0.21 | 0.17 | 14 |
| stroke 1067 | 20 % → 0 % | 24.0 px | 0.00 | 0.00 | 15 |
| stroke 1068 | 7 % → 12 % | 10.5 px | 0.19 | 1.76 | 13 |
| stroke 1069 | 26 % → 5 % | 39.5 px | 0.20 | 0.19 | 21 |
| stroke 1070 | 18 % → 8 % | 29.1 px | 0.21 | 0.44 | 19 |
| stroke 1071 | 36 % → 0 % | 61.4 px | 0.00 | 0.00 | 11 |
| stroke 1072 | 23 % → 1 % | 47.2 px | 0.21 | 0.03 | 9 |
| stroke 1073 | 21 % → 0 % | 22.6 px | 0.00 | 0.00 | 32 |
| stroke 1074 | 28 % → 20 % | 31.3 px | 0.18 | 0.72 | 17 |
| stroke 1075 | 13 % → 12 % | 20.1 px | 0.19 | 0.89 | 37 |
| stroke 1076 | 37 % → 9 % | 49.1 px | 0.19 | 0.24 | 12 |
| stroke 1077 | 22 % → 31 % | 36.9 px | 0.18 | 1.42 | 16 |
| stroke 1078 | 30 % → 9 % | 57.9 px | 0.21 | 0.30 | 20 |
| stroke 1079 | 32 % → 16 % | 54.4 px | 0.19 | 0.50 | 8 |
| stroke 1080 | 41 % → 0 % | 105.4 px | 0.00 | 0.00 | 3 |
| stroke 1081 | 25 % → 29 % | 66.5 px | 0.18 | 1.15 | 7 |
| stroke 1082 | 49 % → 6 % | 90.7 px | 0.21 | 0.12 | 8 |
| stroke 1083 | 29 % → 5 % | 55.2 px | 0.21 | 0.19 | 9 |
| stroke 1084 | 43 % → 11 % | 107.9 px | 0.20 | 0.26 | 19 |
| stroke 1085 | 26 % → 9 % | 72.8 px | 0.16 | 0.35 | 5 |
| stroke 1086 | 49 % → 0 % | 112.9 px | 0.00 | 0.00 | 13 |
| stroke 1087 | 44 % → 0 % | 124.3 px | 0.00 | 0.00 | 6 |
| stroke 1088 | 29 % → 2 % | 39.7 px | 0.21 | 0.08 | 36 |
| stroke 1089 | 32 % → 17 % | 44.0 px | 0.21 | 0.55 | 29 |
| stroke 1090 | 29 % → 6 % | 44.6 px | 0.20 | 0.20 | 154 |
| stroke 1091 | 31 % → 23 % | 41.8 px | 0.18 | 0.75 | 76 |
| stroke 1092 | 31 % → 27 % | 48.6 px | 0.17 | 0.85 | 76 |
| stroke 1093 | 30 % → 12 % | 35.7 px | 0.18 | 0.40 | 59 |
| stroke 1094 | 32 % → 0 % | 35.4 px | 0.00 | 0.00 | 111 |
| stroke 1095 | 7 % → 10 % | 9.7 px | 0.20 | 1.32 | 32 |
| stroke 1096 | 10 % → 29 % | 15.1 px | 0.19 | 2.96 | 40 |
| stroke 1097 | 11 % → 0 % | 16.3 px | 0.00 | 0.00 | 16 |
| stroke 1098 | 11 % → 10 % | 16.8 px | 0.20 | 0.97 | 23 |
| stroke 1099 | 23 % → 0 % | 44.1 px | 0.00 | 0.00 | 11 |
| stroke 1100 | 23 % → 0 % | 38.5 px | 0.00 | 0.00 | 13 |
| stroke 1101 | 26 % → 20 % | 35.4 px | 0.20 | 0.76 | 49 |
| stroke 1102 | 31 % → 11 % | 74.2 px | 0.20 | 0.36 | 8 |
| stroke 1103 | 30 % → 21 % | 75.0 px | 0.20 | 0.71 | 11 |
| stroke 1104 | 25 % → 11 % | 66.4 px | 0.20 | 0.47 | 7 |
| stroke 1105 | 41 % → 4 % | 99.7 px | 0.20 | 0.09 | 6 |
| stroke 1106 | 52 % → 5 % | 116.1 px | 0.20 | 0.09 | 5 |
| stroke 1107 | 37 % → 0 % | 102.8 px | 0.00 | 0.00 | 3 |
| stroke 1108 | 20 % → 0 % | 55.7 px | 0.00 | 0.00 | 6 |
| stroke 1109 | 32 % → 0 % | 83.5 px | 0.00 | 0.00 | 3 |
| stroke 1110 | 27 % → 0 % | 40.1 px | 0.00 | 0.00 | 44 |
| stroke 1111 | 29 % → 17 % | 34.9 px | 0.19 | 0.57 | 65 |
| stroke 1112 | 31 % → 28 % | 46.8 px | 0.19 | 0.90 | 74 |
| stroke 1113 | 34 % → 12 % | 41.6 px | 0.20 | 0.36 | 52 |
| stroke 1114 | 39 % → 0 % | 39.8 px | 0.00 | 0.00 | 36 |
| stroke 1115 | 29 % → 0 % | 44.4 px | 0.00 | 0.00 | 17 |
| stroke 1116 | 5 % → 0 % | 10.8 px | 0.00 | 0.00 | 8 |
| stroke 1117 | 9 % → 0 % | 8.9 px | 0.00 | 0.00 | 26 |
| stroke 1118 | 6 % → 0 % | 13.0 px | 0.00 | 0.00 | 13 |
| stroke 1119 | 9 % → 0 % | 9.1 px | 0.00 | 0.00 | 27 |
| stroke 1120 | 4 % → 0 % | 10.7 px | 0.00 | 0.00 | 4 |
| stroke 1121 | 9 % → 0 % | 9.8 px | 0.00 | 0.00 | 24 |
| stroke 1122 | 8 % → 0 % | 10.1 px | 0.00 | 0.00 | 39 |
| stroke 1123 | 17 % → 0 % | 25.6 px | 0.00 | 0.00 | 19 |
| stroke 1124 | 7 % → 0 % | 8.7 px | 0.00 | 0.00 | 14 |
| stroke 1125 | 17 % → 0 % | 26.2 px | 0.00 | 0.00 | 24 |
| stroke 1126 | 9 % → 0 % | 12.4 px | 0.00 | 0.00 | 23 |
| stroke 1127 | 26 % → 0 % | 44.8 px | 0.00 | 0.00 | 14 |
| stroke 1128 | 15 % → 0 % | 22.1 px | 0.00 | 0.00 | 18 |
| stroke 1129 | 14 % → 0 % | 17.9 px | 0.00 | 0.00 | 28 |
| stroke 1130 | 19 % → 0 % | 22.0 px | 0.00 | 0.00 | 22 |
| stroke 1131 | 10 % → 0 % | 18.6 px | 0.00 | 0.00 | 12 |
| stroke 1132 | 24 % → 0 % | 36.1 px | 0.00 | 0.00 | 16 |
| stroke 1133 | 39 % → 0 % | 65.9 px | 0.00 | 0.00 | 19 |
| stroke 1134 | 23 % → 0 % | 41.5 px | 0.00 | 0.00 | 8 |
| stroke 1135 | 27 % → 0 % | 42.7 px | 0.00 | 0.00 | 21 |
| stroke 1136 | 30 % → 0 % | 54.3 px | 0.00 | 0.00 | 12 |
| stroke 1137 | 28 % → 0 % | 61.1 px | 0.00 | 0.00 | 11 |
| stroke 1138 | 27 % → 0 % | 70.0 px | 0.00 | 0.00 | 15 |
| stroke 1139 | 36 % → 0 % | 78.9 px | 0.00 | 0.00 | 6 |
| stroke 1140 | 25 % → 0 % | 28.1 px | 0.00 | 0.00 | 48 |
| stroke 1141 | 29 % → 0 % | 31.6 px | 0.00 | 0.00 | 54 |
| stroke 1142 | 31 % → 0 % | 44.5 px | 0.00 | 0.00 | 26 |
| stroke 1143 | 30 % → 0 % | 36.1 px | 0.00 | 0.00 | 44 |
| stroke 1144 | 32 % → 0 % | 43.6 px | 0.00 | 0.00 | 85 |
| stroke 1145 | 32 % → 0 % | 39.1 px | 0.00 | 0.00 | 71 |
| stroke 1146 | 31 % → 0 % | 31.5 px | 0.00 | 0.00 | 46 |
| stroke 1147 | 31 % → 0 % | 27.8 px | 0.00 | 0.00 | 30 |
| stroke 1148 | 18 % → 0 % | 15.7 px | 0.00 | 0.00 | 29 |
| stroke 1149 | 33 % → 0 % | 31.2 px | 0.00 | 0.00 | 37 |
| stroke 1150 | 17 % → 0 % | 26.7 px | 0.00 | 0.00 | 7 |
| stroke 1151 | 13 % → 0 % | 37.5 px | 0.00 | 0.00 | 5 |
| stroke 1152 | 18 % → 0 % | 26.3 px | 0.00 | 0.00 | 19 |
| stroke 1153 | 5 % → 0 % | 10.1 px | 0.00 | 0.00 | 5 |
| stroke 1154 | 7 % → 0 % | 9.3 px | 0.00 | 0.00 | 21 |
| stroke 1155 | 18 % → 0 % | 28.3 px | 0.00 | 0.00 | 12 |
| stroke 1156 | 23 % → 0 % | 50.2 px | 0.00 | 0.00 | 5 |
| stroke 1157 | 23 % → 0 % | 41.2 px | 0.00 | 0.00 | 13 |
| stroke 1158 | 28 % → 0 % | 77.3 px | 0.00 | 0.00 | 5 |
| stroke 1159 | 19 % → 0 % | 23.9 px | 0.00 | 0.00 | 56 |
| stroke 1160 | 26 % → 0 % | 28.1 px | 0.00 | 0.00 | 73 |
| stroke 1161 | 22 % → 0 % | 28.7 px | 0.00 | 0.00 | 36 |
| stroke 1162 | 6 % → 0 % | 10.2 px | 0.00 | 0.00 | 21 |
| stroke 1163 | 8 % → 0 % | 17.6 px | 0.00 | 0.00 | 12 |
| stroke 1164 | 20 % → 0 % | 47.4 px | 0.00 | 0.00 | 3 |
| stroke 1165 | 21 % → 0 % | 58.9 px | 0.00 | 0.00 | 10 |
| stroke 1166 | 15 % → 0 % | 18.0 px | 0.00 | 0.00 | 49 |
| stroke 1167 | 23 % → 0 % | 20.9 px | 0.00 | 0.00 | 47 |
| stroke 1168 | 25 % → 0 % | 31.8 px | 0.00 | 0.00 | 21 |
| stroke 1169 | 14 % → 0 % | 20.7 px | 0.00 | 0.00 | 26 |
| stroke 1170 | 10 % → 0 % | 27.6 px | 0.00 | 0.00 | 3 |
| stroke 1171 | 20 % → 0 % | 25.6 px | 0.00 | 0.00 | 29 |
| stroke 1172 | 15 % → 0 % | 17.0 px | 0.00 | 0.00 | 36 |
| stroke 1173 | 25 % → 0 % | 53.0 px | 0.00 | 0.00 | 13 |
| stroke 1174 | 7 % → 0 % | 9.0 px | 0.00 | 0.00 | 14 |
| stroke 1175 | 5 % → 0 % | 12.6 px | 0.00 | 0.00 | 5 |
| stroke 1176 | 12 % → 0 % | 18.1 px | 0.00 | 0.00 | 15 |
| stroke 1177 | 14 % → 0 % | 38.5 px | 0.00 | 0.00 | 3 |
| stroke 1178 | 18 % → 0 % | 49.9 px | 0.00 | 0.00 | 4 |
| stroke 1179 | 17 % → 0 % | 44.4 px | 0.00 | 0.00 | 3 |
| stroke 1180 | 17 % → 0 % | 17.1 px | 0.00 | 0.00 | 64 |
| stroke 1181 | 22 % → 0 % | 16.1 px | 0.00 | 0.00 | 45 |
| stroke 1182 | 29 % → 0 % | 41.4 px | 0.00 | 0.00 | 15 |
| stroke 1183 | 5 % → 0 % | 10.5 px | 0.00 | 0.00 | 13 |
| stroke 1184 | 9 % → 0 % | 9.4 px | 0.00 | 0.00 | 26 |
| stroke 1185 | 6 % → 0 % | 8.7 px | 0.00 | 0.00 | 29 |
| stroke 1186 | 9 % → 0 % | 13.5 px | 0.00 | 0.00 | 20 |
| stroke 1187 | 14 % → 0 % | 14.1 px | 0.00 | 0.00 | 18 |
| stroke 1188 | 15 % → 0 % | 23.1 px | 0.00 | 0.00 | 9 |
| stroke 1189 | 20 % → 0 % | 29.8 px | 0.00 | 0.00 | 27 |
| stroke 1190 | 14 % → 0 % | 20.5 px | 0.00 | 0.00 | 31 |
| stroke 1191 | 9 % → 0 % | 12.8 px | 0.00 | 0.00 | 37 |
| stroke 1192 | 14 % → 0 % | 15.5 px | 0.00 | 0.00 | 18 |
| stroke 1193 | 21 % → 0 % | 32.5 px | 0.00 | 0.00 | 20 |
| stroke 1194 | 33 % → 0 % | 53.4 px | 0.00 | 0.00 | 22 |
| stroke 1195 | 30 % → 0 % | 51.9 px | 0.00 | 0.00 | 32 |
| stroke 1196 | 24 % → 0 % | 39.0 px | 0.00 | 0.00 | 11 |
| stroke 1197 | 26 % → 0 % | 73.4 px | 0.00 | 0.00 | 3 |
| stroke 1198 | 23 % → 0 % | 35.1 px | 0.00 | 0.00 | 9 |
| stroke 1199 | 30 % → 0 % | 52.8 px | 0.00 | 0.00 | 6 |
| stroke 1200 | 37 % → 0 % | 61.4 px | 0.00 | 0.00 | 16 |
| stroke 1201 | 38 % → 0 % | 58.8 px | 0.00 | 0.00 | 15 |
| stroke 1202 | 29 % → 0 % | 46.3 px | 0.00 | 0.00 | 19 |
| stroke 1203 | 48 % → 0 % | 102.7 px | 0.00 | 0.00 | 4 |
| stroke 1204 | 48 % → 0 % | 118.6 px | 0.00 | 0.00 | 7 |
| stroke 1205 | 27 % → 0 % | 75.2 px | 0.00 | 0.00 | 7 |
| stroke 1206 | 32 % → 0 % | 68.0 px | 0.00 | 0.00 | 7 |
| stroke 1207 | 31 % → 0 % | 74.6 px | 0.00 | 0.00 | 7 |
| stroke 1208 | 22 % → 0 % | 58.5 px | 0.00 | 0.00 | 4 |
| stroke 1209 | 41 % → 0 % | 110.2 px | 0.00 | 0.00 | 3 |
| stroke 1210 | 46 % → 0 % | 123.2 px | 0.00 | 0.00 | 6 |
| stroke 1211 | 22 % → 0 % | 27.0 px | 0.00 | 0.00 | 40 |
| stroke 1212 | 30 % → 0 % | 32.7 px | 0.00 | 0.00 | 33 |
| stroke 1213 | 36 % → 0 % | 46.8 px | 0.00 | 0.00 | 55 |
| stroke 1214 | 38 % → 0 % | 57.5 px | 0.00 | 0.00 | 48 |
| stroke 1215 | 30 % → 0 % | 30.4 px | 0.00 | 0.00 | 60 |
| stroke 1216 | 32 % → 0 % | 36.7 px | 0.00 | 0.00 | 75 |
| stroke 1217 | 39 % → 0 % | 53.1 px | 0.00 | 0.00 | 53 |
| stroke 1218 | 38 % → 0 % | 46.8 px | 0.00 | 0.00 | 79 |
| stroke 1219 | 38 % → 0 % | 55.4 px | 0.00 | 0.00 | 32 |
| stroke 1220 | 8 % → 0 % | 17.0 px | 0.00 | 0.00 | 10 |
| stroke 1221 | 11 % → 0 % | 12.2 px | 0.00 | 0.00 | 28 |
| stroke 1222 | 6 % → 0 % | 8.8 px | 0.00 | 0.00 | 10 |
| stroke 1223 | 10 % → 0 % | 8.4 px | 0.00 | 0.00 | 46 |
| stroke 1224 | 17 % → 0 % | 39.1 px | 0.00 | 0.00 | 10 |
| stroke 1225 | 21 % → 0 % | 22.3 px | 0.00 | 0.00 | 29 |
| stroke 1226 | 7 % → 41 % | 8.8 px | 0.17 | 5.63 | 21 |
| stroke 1227 | 7 % → 41 % | 9.7 px | 0.19 | 6.04 | 55 |
| stroke 1228 | 14 % → 50 % | 22.2 px | 0.16 | 3.63 | 22 |
| stroke 1229 | 19 % → 43 % | 25.4 px | 0.19 | 2.24 | 16 |
| stroke 1230 | 8 % → 22 % | 10.4 px | 0.20 | 2.84 | 45 |
| stroke 1231 | 10 % → 49 % | 11.5 px | 0.17 | 4.84 | 28 |
| stroke 1232 | 8 % → 33 % | 14.4 px | 0.18 | 4.13 | 17 |
| stroke 1233 | 12 % → 30 % | 18.4 px | 0.19 | 2.55 | 31 |
| stroke 1234 | 6 % → 26 % | 9.7 px | 0.17 | 4.30 | 23 |
| stroke 1235 | 25 % → 52 % | 36.1 px | 0.18 | 2.12 | 18 |
| stroke 1236 | 18 % → 38 % | 28.5 px | 0.17 | 2.07 | 18 |
| stroke 1237 | 18 % → 37 % | 20.3 px | 0.17 | 2.08 | 26 |
| stroke 1238 | 24 % → 41 % | 35.9 px | 0.18 | 1.72 | 11 |
| stroke 1239 | 21 % → 38 % | 42.7 px | 0.17 | 1.84 | 5 |
| stroke 1240 | 18 % → 43 % | 37.2 px | 0.17 | 2.36 | 10 |
| stroke 1241 | 24 % → 40 % | 59.1 px | 0.16 | 1.67 | 8 |
| stroke 1242 | 26 % → 44 % | 72.9 px | 0.19 | 1.72 | 28 |
| stroke 1243 | 22 % → 38 % | 30.7 px | 0.16 | 1.78 | 12 |
| stroke 1244 | 25 % → 33 % | 65.3 px | 0.19 | 1.35 | 4 |
| stroke 1245 | 17 % → 35 % | 42.0 px | 0.16 | 2.04 | 10 |
| stroke 1246 | 33 % → 48 % | 72.9 px | 0.18 | 1.46 | 13 |
| stroke 1247 | 33 % → 52 % | 56.2 px | 0.17 | 1.59 | 6 |
| stroke 1248 | 48 % → 61 % | 77.3 px | 0.17 | 1.28 | 7 |
| stroke 1249 | 22 % → 31 % | 32.3 px | 0.21 | 1.40 | 9 |
| stroke 1250 | 30 % → 41 % | 74.7 px | 0.18 | 1.34 | 7 |
| stroke 1251 | 18 % → 24 % | 15.7 px | 0.21 | 1.32 | 42 |
| stroke 1252 | 25 % → 30 % | 35.8 px | 0.21 | 1.19 | 17 |
| stroke 1253 | 30 % → 35 % | 30.7 px | 0.18 | 1.18 | 65 |
| stroke 1254 | 30 % → 39 % | 31.5 px | 0.17 | 1.28 | 60 |
| stroke 1255 | 24 % → 30 % | 35.3 px | 0.17 | 1.24 | 33 |
| stroke 1256 | 22 % → 26 % | 23.4 px | 0.18 | 1.17 | 48 |
| stroke 1257 | 24 % → 25 % | 31.8 px | 0.17 | 1.04 | 56 |
| stroke 1258 | 36 % → 39 % | 41.4 px | 0.17 | 1.08 | 39 |
| stroke 1259 | 35 % → 38 % | 46.0 px | 0.16 | 1.09 | 41 |
| stroke 1260 | 34 % → 35 % | 41.8 px | 0.16 | 1.03 | 41 |
| stroke 1261 | 35 % → 37 % | 35.0 px | 0.17 | 1.06 | 46 |
| stroke 1262 | 24 % → 30 % | 33.6 px | 0.19 | 1.21 | 40 |
| stroke 1263 | 27 % → 30 % | 25.9 px | 0.20 | 1.09 | 39 |
| stroke 1264 | 27 % → 29 % | 39.4 px | 0.19 | 1.10 | 39 |
| stroke 1265 | 30 % → 30 % | 49.2 px | 0.19 | 1.00 | 19 |
| stroke 1266 | 8 % → 41 % | 8.1 px | 0.16 | 5.13 | 23 |
| stroke 1267 | 6 % → 35 % | 10.9 px | 0.20 | 5.88 | 11 |
| stroke 1268 | 12 % → 32 % | 25.9 px | 0.21 | 2.76 | 5 |
| stroke 1269 | 11 % → 35 % | 15.4 px | 0.18 | 3.29 | 10 |
| stroke 1270 | 16 % → 37 % | 25.3 px | 0.16 | 2.32 | 10 |
| stroke 1271 | 8 % → 33 % | 13.6 px | 0.17 | 4.11 | 16 |
| stroke 1272 | 11 % → 24 % | 17.4 px | 0.17 | 2.29 | 10 |
| stroke 1273 | 17 % → 35 % | 33.9 px | 0.21 | 2.12 | 8 |
| stroke 1274 | 21 % → 33 % | 37.3 px | 0.20 | 1.55 | 14 |
| stroke 1275 | 15 % → 24 % | 23.4 px | 0.17 | 1.59 | 18 |
| stroke 1276 | 21 % → 39 % | 27.0 px | 0.16 | 1.80 | 19 |
| stroke 1277 | 16 % → 34 % | 40.4 px | 0.16 | 2.10 | 7 |
| stroke 1278 | 28 % → 41 % | 68.7 px | 0.16 | 1.49 | 7 |
| stroke 1279 | 28 % → 37 % | 79.0 px | 0.16 | 1.33 | 4 |
| stroke 1280 | 22 % → 35 % | 48.6 px | 0.17 | 1.59 | 5 |
| stroke 1281 | 22 % → 26 % | 33.4 px | 0.16 | 1.16 | 33 |
| stroke 1282 | 20 % → 22 % | 27.2 px | 0.17 | 1.06 | 53 |
| stroke 1283 | 20 % → 20 % | 27.7 px | 0.17 | 1.03 | 43 |
| stroke 1284 | 30 % → 32 % | 43.2 px | 0.16 | 1.06 | 40 |
| stroke 1285 | 27 % → 34 % | 26.8 px | 0.17 | 1.23 | 42 |
| stroke 1286 | 32 % → 34 % | 32.3 px | 0.17 | 1.06 | 50 |
| stroke 1287 | 35 % → 35 % | 87.1 px | 0.16 | 1.00 | 13 |
| stroke 1288 | 22 % → 26 % | 25.1 px | 0.20 | 1.22 | 39 |
| stroke 1289 | 23 % → 23 % | 23.4 px | 0.21 | 1.00 | 37 |
| stroke 1290 | 34 % → 34 % | 406.6 px | 0.21 | 1.00 | 0 |

Numbers say: wet paint spreads well beyond the stroke.

## Refs v3 · #42 Pink shaggy pastel — own sheet
own sheet 800 × 976 · Pastel 1.00 · 38 px · 179.4 s

![Refs v3 · #42 Pink shaggy pastel — own sheet](Refs-v3-42-Pink-shaggy-pastel-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 4 % → 17 % | 42.3 px | 0.35 | 4.14 | 217 |
| stroke 2 | 4 % → 45 % | 45.5 px | 0.34 | 12.78 | 53 |
| stroke 3 | 9 % → 40 % | 72.2 px | 0.34 | 4.59 | 92 |
| stroke 4 | 12 % → 39 % | 124.0 px | 0.34 | 3.15 | 65 |
| stroke 5 | 7 % → 0 % | 34.5 px | 0.00 | 0.00 | 169 |
| stroke 6 | 10 % → 0 % | 45.6 px | 0.00 | 0.00 | 317 |
| stroke 7 | 17 % → 0 % | 98.7 px | 0.00 | 0.00 | 178 |
| stroke 8 | 20 % → 0 % | 93.4 px | 0.24 | 0.00 | 249 |
| stroke 9 | 28 % → 0 % | 359.6 px | 0.00 | 0.00 | 44 |
| stroke 10 | 25 % → 0 % | 110.4 px | 0.00 | 0.00 | 319 |
| stroke 11 | 31 % → 0 % | 376.0 px | 0.00 | 0.00 | 68 |
| stroke 12 | 26 % → 0 % | 93.0 px | 0.00 | 0.00 | 548 |
| stroke 13 | 18 % → 8 % | 177.0 px | 0.34 | 0.43 | 72 |
| stroke 14 | 25 % → 0 % | 87.9 px | 0.00 | 0.00 | 715 |
| stroke 15 | 35 % → 8 % | 125.6 px | 0.34 | 0.22 | 556 |
| stroke 16 | 26 % → 0 % | 107.0 px | 0.00 | 0.00 | 396 |
| stroke 17 | 35 % → 19 % | 136.4 px | 0.34 | 0.54 | 581 |
| stroke 18 | 47 % → 0 % | 357.1 px | 0.00 | 0.00 | 124 |
| stroke 19 | 30 % → 0 % | 115.8 px | 0.00 | 0.00 | 684 |
| stroke 20 | 30 % → 9 % | 109.9 px | 0.34 | 0.28 | 1732 |
| stroke 21 | 45 % → 15 % | 159.9 px | 0.34 | 0.34 | 749 |
| stroke 22 | 36 % → 0 % | 131.6 px | 0.00 | 0.00 | 653 |
| stroke 23 | 46 % → 21 % | 190.3 px | 0.34 | 0.46 | 403 |
| stroke 24 | 54 % → 0 % | 307.0 px | 0.00 | 0.00 | 190 |
| stroke 25 | 43 % → 0 % | 165.5 px | 0.00 | 0.00 | 429 |
| stroke 26 | 46 % → 23 % | 184.4 px | 0.34 | 0.51 | 388 |
| stroke 27 | 53 % → 0 % | 266.2 px | 0.00 | 0.00 | 194 |
| stroke 28 | 47 % → 0 % | 239.2 px | 0.00 | 0.00 | 209 |
| stroke 29 | 51 % → 18 % | 196.3 px | 0.34 | 0.35 | 460 |
| stroke 30 | 50 % → 0 % | 416.8 px | 0.00 | 0.00 | 102 |
| stroke 31 | 41 % → 0 % | 209.1 px | 0.00 | 0.00 | 196 |
| stroke 32 | 50 % → 22 % | 283.8 px | 0.34 | 0.43 | 158 |
| stroke 33 | 54 % → 0 % | 400.7 px | 0.34 | 0.00 | 127 |
| stroke 34 | 46 % → 0 % | 444.0 px | 0.00 | 0.00 | 67 |
| stroke 35 | 35 % → 0 % | 166.3 px | 0.00 | 0.00 | 243 |
| stroke 36 | 50 % → 20 % | 331.4 px | 0.35 | 0.40 | 149 |
| stroke 37 | 53 % → 0 % | 444.2 px | 0.33 | 0.00 | 87 |
| stroke 38 | 41 % → 0 % | 544.1 px | 0.00 | 0.00 | 65 |
| stroke 39 | 33 % → 0 % | 165.4 px | 0.33 | 0.01 | 237 |
| stroke 40 | 49 % → 11 % | 204.0 px | 0.35 | 0.22 | 374 |
| stroke 41 | 38 % → 0 % | 461.0 px | 0.00 | 0.00 | 48 |
| stroke 42 | 31 % → 0 % | 166.6 px | 0.00 | 0.00 | 178 |
| stroke 43 | 42 % → 7 % | 159.4 px | 0.35 | 0.18 | 420 |
| stroke 44 | 29 % → 0 % | 152.4 px | 0.00 | 0.00 | 182 |
| stroke 45 | 43 % → 16 % | 563.0 px | 0.35 | 0.37 | 161 |
| stroke 46 | 40 % → 2 % | 141.0 px | 0.35 | 0.06 | 1005 |
| stroke 47 | 40 % → 17 % | 243.5 px | 0.35 | 0.43 | 161 |
| stroke 48 | 40 % → 3 % | 151.8 px | 0.35 | 0.08 | 610 |
| stroke 49 | 31 % → 0 % | 139.7 px | 0.32 | 0.00 | 353 |
| stroke 50 | 41 % → 14 % | 415.2 px | 0.35 | 0.33 | 95 |
| stroke 51 | 42 % → 2 % | 152.6 px | 0.35 | 0.06 | 1228 |
| stroke 52 | 35 % → 0 % | 171.4 px | 0.00 | 0.00 | 330 |
| stroke 53 | 48 % → 1 % | 617.8 px | 0.35 | 0.03 | 84 |
| stroke 54 | 43 % → 0 % | 175.9 px | 0.00 | 0.00 | 715 |
| stroke 55 | 35 % → 0 % | 196.2 px | 0.00 | 0.00 | 286 |
| stroke 56 | 32 % → 10 % | 397.1 px | 0.35 | 0.31 | 119 |
| stroke 57 | 44 % → 0 % | 174.2 px | 0.00 | 0.00 | 778 |
| stroke 58 | 31 % → 0 % | 204.9 px | 0.00 | 0.00 | 222 |
| stroke 59 | 39 % → 3 % | 171.6 px | 0.35 | 0.07 | 535 |
| stroke 60 | 48 % → 0 % | 178.2 px | 0.00 | 0.00 | 521 |
| stroke 61 | 27 % → 1 % | 197.5 px | 0.32 | 0.02 | 166 |
| stroke 62 | 29 % → 0 % | 354.2 px | 0.34 | 0.01 | 71 |
| stroke 63 | 47 % → 0 % | 163.7 px | 0.00 | 0.00 | 916 |
| stroke 64 | 30 % → 0 % | 198.3 px | 0.00 | 0.00 | 123 |
| stroke 65 | 47 % → 0 % | 167.4 px | 0.00 | 0.00 | 749 |
| stroke 66 | 34 % → 0 % | 222.2 px | 0.00 | 0.00 | 152 |
| stroke 67 | 38 % → 0 % | 508.7 px | 0.00 | 0.00 | 54 |
| stroke 68 | 49 % → 0 % | 176.5 px | 0.00 | 0.00 | 495 |
| stroke 69 | 46 % → 0 % | 166.3 px | 0.00 | 0.00 | 531 |
| stroke 70 | 32 % → 0 % | 263.9 px | 0.00 | 0.00 | 74 |
| stroke 71 | 48 % → 0 % | 407.7 px | 0.00 | 0.00 | 112 |
| stroke 72 | 52 % → 0 % | 443.2 px | 0.00 | 0.00 | 99 |
| stroke 73 | 48 % → 0 % | 243.2 px | 0.00 | 0.00 | 215 |
| stroke 74 | 39 % → 0 % | 210.3 px | 0.00 | 0.00 | 185 |
| stroke 75 | 54 % → 0 % | 454.5 px | 0.00 | 0.00 | 107 |
| stroke 76 | 12 % → 0 % | 23.3 px | 0.00 | 0.00 | 1044 |
| stroke 77 | 19 % → 0 % | 47.7 px | 0.00 | 0.00 | 686 |
| stroke 78 | 26 % → 0 % | 66.7 px | 0.00 | 0.00 | 551 |
| stroke 79 | 33 % → 0 % | 84.1 px | 0.00 | 0.00 | 638 |
| stroke 80 | 40 % → 0 % | 103.2 px | 0.00 | 0.00 | 836 |
| stroke 81 | 41 % → 0 % | 106.4 px | 0.00 | 0.00 | 602 |
| stroke 82 | 39 % → 0 % | 99.7 px | 0.21 | 0.00 | 638 |
| stroke 83 | 42 % → 1 % | 134.7 px | 0.32 | 0.02 | 414 |
| stroke 84 | 37 % → 1 % | 233.1 px | 0.32 | 0.02 | 150 |
| stroke 85 | 6 % → 0 % | 28.8 px | 0.00 | 0.00 | 167 |
| stroke 86 | 40 % → 0 % | 151.1 px | 0.33 | 0.01 | 273 |
| stroke 87 | 30 % → 0 % | 73.6 px | 0.33 | 0.01 | 1039 |
| stroke 88 | 36 % → 0 % | 98.1 px | 0.00 | 0.00 | 578 |
| stroke 89 | 46 % → 2 % | 297.6 px | 0.32 | 0.04 | 128 |
| stroke 90 | 32 % → 1 % | 132.9 px | 0.32 | 0.04 | 273 |
| stroke 91 | 41 % → 0 % | 114.2 px | 0.00 | 0.00 | 589 |
| stroke 92 | 49 % → 0 % | 591.4 px | 0.33 | 0.01 | 63 |
| stroke 93 | 47 % → 0 % | 149.5 px | 0.00 | 0.00 | 391 |
| stroke 94 | 46 % → 1 % | 563.4 px | 0.32 | 0.02 | 68 |
| stroke 95 | 52 % → 0 % | 189.0 px | 0.00 | 0.00 | 306 |
| stroke 96 | 45 % → 1 % | 175.0 px | 0.32 | 0.03 | 252 |
| stroke 97 | 50 % → 0 % | 194.7 px | 0.00 | 0.00 | 245 |
| stroke 98 | 54 % → 0 % | 279.3 px | 0.00 | 0.00 | 170 |
| stroke 99 | 56 % → 2 % | 669.7 px | 0.32 | 0.04 | 44 |
| stroke 100 | 48 % → 0 % | 332.3 px | 0.00 | 0.00 | 113 |
| stroke 101 | 56 % → 2 % | 432.6 px | 0.32 | 0.03 | 103 |
| stroke 102 | 53 % → 2 % | 493.7 px | 0.32 | 0.03 | 86 |
| stroke 103 | 1 % → 0 % | 17.3 px | 0.00 | 0.00 | 9 |
| stroke 104 | 3 % → 1 % | 20.0 px | 0.32 | 0.49 | 32 |
| stroke 105 | 12 % → 10 % | 31.8 px | 0.34 | 0.87 | 600 |
| stroke 106 | 19 % → 16 % | 81.3 px | 0.33 | 0.81 | 312 |
| stroke 107 | 15 % → 6 % | 37.4 px | 0.34 | 0.36 | 1260 |
| stroke 108 | 24 % → 15 % | 114.0 px | 0.33 | 0.62 | 276 |
| stroke 109 | 23 % → 5 % | 57.7 px | 0.34 | 0.22 | 1143 |
| stroke 110 | 29 % → 17 % | 138.0 px | 0.33 | 0.58 | 300 |
| stroke 111 | 31 % → 14 % | 175.1 px | 0.34 | 0.46 | 261 |
| stroke 112 | 29 % → 0 % | 99.1 px | 0.00 | 0.00 | 651 |
| stroke 113 | 31 % → 22 % | 141.9 px | 0.33 | 0.72 | 290 |
| stroke 114 | 35 % → 16 % | 217.5 px | 0.34 | 0.45 | 125 |
| stroke 115 | 40 % → 0 % | 228.5 px | 0.00 | 0.00 | 162 |
| stroke 116 | 32 % → 0 % | 302.9 px | 0.00 | 0.00 | 113 |
| stroke 117 | 28 % → 27 % | 110.5 px | 0.34 | 0.99 | 328 |
| stroke 118 | 32 % → 22 % | 201.6 px | 0.34 | 0.68 | 315 |
| stroke 119 | 44 % → 0 % | 190.9 px | 0.00 | 0.00 | 302 |
| stroke 120 | 28 % → 26 % | 134.3 px | 0.33 | 0.92 | 181 |
| stroke 121 | 26 % → 31 % | 187.9 px | 0.34 | 1.19 | 159 |
| stroke 122 | 39 % → 0 % | 171.8 px | 0.00 | 0.00 | 381 |
| stroke 123 | 28 % → 26 % | 145.6 px | 0.33 | 0.94 | 181 |
| stroke 124 | 38 % → 0 % | 354.9 px | 0.00 | 0.00 | 74 |
| stroke 125 | 27 % → 30 % | 129.9 px | 0.34 | 1.12 | 171 |
| stroke 126 | 28 % → 0 % | 347.3 px | 0.00 | 0.00 | 62 |
| stroke 127 | 26 % → 28 % | 116.8 px | 0.34 | 1.10 | 201 |
| stroke 128 | 25 % → 27 % | 125.8 px | 0.34 | 1.07 | 188 |
| stroke 129 | 27 % → 21 % | 168.4 px | 0.34 | 0.79 | 140 |
| stroke 130 | 27 % → 21 % | 230.4 px | 0.34 | 0.75 | 72 |
| stroke 131 | 25 % → 18 % | 272.8 px | 0.34 | 0.70 | 59 |
| stroke 132 | 22 % → 17 % | 241.1 px | 0.34 | 0.78 | 58 |
| stroke 133 | 18 % → 15 % | 212.5 px | 0.34 | 0.85 | 52 |
| stroke 134 | 16 % → 12 % | 186.9 px | 0.34 | 0.76 | 45 |
| stroke 135 | 16 % → 15 % | 76.1 px | 0.35 | 0.93 | 214 |
| stroke 136 | 18 % → 13 % | 88.2 px | 0.35 | 0.72 | 218 |
| stroke 137 | 21 % → 13 % | 94.0 px | 0.35 | 0.64 | 294 |
| stroke 138 | 23 % → 9 % | 99.1 px | 0.35 | 0.41 | 273 |
| stroke 139 | 27 % → 3 % | 117.5 px | 0.35 | 0.12 | 250 |
| stroke 140 | 29 % → 0 % | 184.7 px | 0.00 | 0.00 | 153 |
| stroke 141 | 32 % → 0 % | 399.0 px | 0.34 | 0.00 | 60 |
| stroke 142 | 31 % → 0 % | 226.0 px | 0.00 | 0.00 | 139 |
| stroke 143 | 25 % → 0 % | 91.6 px | 0.00 | 0.00 | 331 |
| stroke 144 | 32 % → 0 % | 180.2 px | 0.00 | 0.00 | 155 |
| stroke 145 | 31 % → 0 % | 193.7 px | 0.00 | 0.00 | 137 |
| stroke 146 | 25 % → 0 % | 82.7 px | 0.00 | 0.00 | 306 |
| stroke 147 | 32 % → 0 % | 348.3 px | 0.00 | 0.00 | 51 |
| stroke 148 | 32 % → 0 % | 157.8 px | 0.00 | 0.00 | 212 |
| stroke 149 | 31 % → 0 % | 151.6 px | 0.00 | 0.00 | 244 |
| stroke 150 | 30 % → 0 % | 145.7 px | 0.00 | 0.00 | 202 |
| stroke 151 | 29 % → 0 % | 330.7 px | 0.00 | 0.00 | 39 |
| stroke 152 | 34 % → 0 % | 167.7 px | 0.00 | 0.00 | 169 |
| stroke 153 | 28 % → 0 % | 235.2 px | 0.00 | 0.00 | 70 |
| stroke 154 | 35 % → 0 % | 216.8 px | 0.00 | 0.00 | 159 |
| stroke 155 | 31 % → 0 % | 191.3 px | 0.00 | 0.00 | 108 |
| stroke 156 | 31 % → 0 % | 136.1 px | 0.00 | 0.00 | 190 |
| stroke 157 | 43 % → 39 % | 414.4 px | 0.34 | 0.91 | 76 |
| stroke 158 | 52 % → 32 % | 638.5 px | 0.34 | 0.62 | 51 |
| stroke 159 | 6 % → 2 % | 36.4 px | 0.32 | 0.29 | 126 |
| stroke 160 | 10 % → 1 % | 51.4 px | 0.32 | 0.14 | 230 |
| stroke 161 | 13 % → 1 % | 53.9 px | 0.32 | 0.06 | 236 |
| stroke 162 | 14 % → 0 % | 89.7 px | 0.00 | 0.00 | 114 |
| stroke 163 | 17 % → 0 % | 51.8 px | 0.32 | 0.03 | 638 |
| stroke 164 | 26 % → 0 % | 211.3 px | 0.33 | 0.00 | 114 |
| stroke 165 | 21 % → 0 % | 74.4 px | 0.00 | 0.00 | 309 |
| stroke 166 | 25 % → 0 % | 78.3 px | 0.00 | 0.00 | 515 |
| stroke 167 | 35 % → 0 % | 328.1 px | 0.00 | 0.00 | 79 |
| stroke 168 | 28 % → 0 % | 100.0 px | 0.00 | 0.00 | 319 |
| stroke 169 | 24 % → 0 % | 150.1 px | 0.00 | 0.00 | 137 |
| stroke 170 | 32 % → 0 % | 75.5 px | 0.00 | 0.00 | 1175 |
| stroke 171 | 23 % → 0 % | 90.3 px | 0.00 | 0.00 | 241 |
| stroke 172 | 37 % → 0 % | 86.3 px | 0.00 | 0.00 | 1149 |
| stroke 173 | 28 % → 0 % | 97.7 px | 0.00 | 0.00 | 322 |
| stroke 174 | 46 % → 0 % | 117.6 px | 0.00 | 0.00 | 936 |
| stroke 175 | 43 % → 0 % | 112.7 px | 0.00 | 0.00 | 1167 |
| stroke 176 | 4 % → 11 % | 42.7 px | 0.35 | 2.65 | 69 |
| stroke 177 | 36 % → 0 % | 352.3 px | 0.00 | 0.00 | 78 |
| stroke 178 | 4 % → 0 % | 44.0 px | 0.00 | 0.00 | 45 |
| stroke 179 | 7 % → 0 % | 46.3 px | 0.00 | 0.00 | 175 |
| stroke 180 | 12 % → 0 % | 151.0 px | 0.00 | 0.00 | 67 |
| stroke 181 | 2 % → 0 % | 17.5 px | 0.00 | 0.00 | 40 |
| stroke 182 | 2 % → 0 % | 23.0 px | 0.00 | 0.00 | 26 |
| stroke 183 | 1 % → 0 % | 18.6 px | 0.00 | 0.00 | 34 |
| stroke 184 | 4 % → 0 % | 20.0 px | 0.00 | 0.00 | 97 |
| stroke 185 | 2 % → 0 % | 40.2 px | 0.00 | 0.00 | 22 |
| stroke 186 | 5 % → 0 % | 45.2 px | 0.00 | 0.00 | 58 |
| stroke 187 | 6 % → 0 % | 124.8 px | 0.00 | 0.00 | 24 |
| stroke 188 | 2 % → 0 % | 42.5 px | 0.00 | 0.00 | 18 |
| stroke 189 | 9 % → 0 % | 146.3 px | 0.00 | 0.00 | 62 |
| stroke 190 | 5 % → 0 % | 56.5 px | 0.00 | 0.00 | 95 |
| stroke 191 | 11 % → 0 % | 198.5 px | 0.00 | 0.00 | 54 |
| stroke 192 | 14 % → 0 % | 75.1 px | 0.00 | 0.00 | 174 |
| stroke 193 | 19 % → 0 % | 186.4 px | 0.00 | 0.00 | 82 |
| stroke 194 | 2 % → 0 % | 40.1 px | 0.34 | 0.04 | 33 |
| stroke 195 | 4 % → 0 % | 65.8 px | 0.00 | 0.00 | 27 |
| stroke 196 | 4 % → 0 % | 76.2 px | 0.33 | 0.00 | 33 |
| stroke 197 | 9 % → 0 % | 57.4 px | 0.00 | 0.00 | 110 |
| stroke 198 | 13 % → 0 % | 126.5 px | 0.00 | 0.00 | 75 |
| stroke 199 | 17 % → 0 % | 139.6 px | 0.00 | 0.00 | 89 |
| stroke 200 | 20 % → 0 % | 82.4 px | 0.00 | 0.00 | 202 |
| stroke 201 | 23 % → 0 % | 366.2 px | 0.00 | 0.00 | 38 |
| stroke 202 | 30 % → 0 % | 356.8 px | 0.00 | 0.00 | 64 |
| stroke 203 | 24 % → 0 % | 290.5 px | 0.00 | 0.00 | 48 |
| stroke 204 | 26 % → 0 % | 477.3 px | 0.00 | 0.00 | 25 |
| stroke 205 | 12 % → 14 % | 65.7 px | 0.35 | 1.19 | 160 |
| stroke 206 | 19 % → 8 % | 77.0 px | 0.35 | 0.42 | 390 |
| stroke 207 | 30 % → 16 % | 374.6 px | 0.35 | 0.52 | 52 |
| stroke 208 | 30 % → 4 % | 143.6 px | 0.35 | 0.14 | 241 |
| stroke 209 | 37 % → 12 % | 723.9 px | 0.35 | 0.31 | 29 |
| stroke 210 | 27 % → 0 % | 353.9 px | 0.00 | 0.00 | 56 |
| stroke 211 | 3 % → 0 % | 34.0 px | 0.00 | 0.00 | 46 |
| stroke 212 | 5 % → 0 % | 58.2 px | 0.00 | 0.00 | 50 |
| stroke 213 | 10 % → 0 % | 131.2 px | 0.00 | 0.00 | 43 |
| stroke 214 | 10 % → 0 % | 99.0 px | 0.00 | 0.00 | 61 |
| stroke 215 | 14 % → 0 % | 74.0 px | 0.00 | 0.00 | 218 |
| stroke 216 | 24 % → 0 % | 134.9 px | 0.00 | 0.00 | 222 |
| stroke 217 | 22 % → 0 % | 282.8 px | 0.00 | 0.00 | 45 |
| stroke 218 | 3 % → 0 % | 55.1 px | 0.34 | 0.16 | 29 |
| stroke 219 | 4 % → 1 % | 28.3 px | 0.33 | 0.26 | 90 |
| stroke 220 | 6 % → 0 % | 51.4 px | 0.30 | 0.02 | 92 |
| stroke 221 | 9 % → 3 % | 70.4 px | 0.34 | 0.29 | 143 |
| stroke 222 | 9 % → 0 % | 75.8 px | 0.00 | 0.00 | 99 |
| stroke 223 | 8 % → 0 % | 143.8 px | 0.00 | 0.00 | 27 |
| stroke 224 | 13 % → 0 % | 67.7 px | 0.00 | 0.00 | 125 |
| stroke 225 | 3 % → 0 % | 53.5 px | 0.00 | 0.00 | 28 |
| stroke 226 | 12 % → 0 % | 64.2 px | 0.00 | 0.00 | 168 |
| stroke 227 | 22 % → 0 % | 385.5 px | 0.00 | 0.00 | 40 |
| stroke 228 | 14 % → 0 % | 123.6 px | 0.00 | 0.00 | 94 |
| stroke 229 | 4 % → 0 % | 30.9 px | 0.00 | 0.00 | 100 |
| stroke 230 | 7 % → 0 % | 43.0 px | 0.00 | 0.00 | 124 |
| stroke 231 | 9 % → 0 % | 58.3 px | 0.00 | 0.00 | 128 |
| stroke 232 | 13 % → 0 % | 90.1 px | 0.00 | 0.00 | 97 |
| stroke 233 | 17 % → 0 % | 173.5 px | 0.00 | 0.00 | 70 |
| stroke 234 | 2 % → 0 % | 40.7 px | 0.00 | 0.00 | 35 |
| stroke 235 | 9 % → 0 % | 82.1 px | 0.00 | 0.00 | 75 |
| stroke 236 | 12 % → 0 % | 125.6 px | 0.00 | 0.00 | 79 |
| stroke 237 | 12 % → 0 % | 107.3 px | 0.00 | 0.00 | 99 |
| stroke 238 | 14 % → 0 % | 238.4 px | 0.00 | 0.00 | 36 |
| stroke 239 | 13 % → 0 % | 220.8 px | 0.00 | 0.00 | 41 |
| stroke 240 | 4 % → 0 % | 27.3 px | 0.00 | 0.00 | 95 |
| stroke 241 | 7 % → 0 % | 33.4 px | 0.00 | 0.00 | 311 |
| stroke 242 | 10 % → 0 % | 47.5 px | 0.00 | 0.00 | 382 |
| stroke 243 | 21 % → 0 % | 107.4 px | 0.00 | 0.00 | 292 |
| stroke 244 | 18 % → 0 % | 95.0 px | 0.00 | 0.00 | 172 |
| stroke 245 | 18 % → 0 % | 157.3 px | 0.00 | 0.00 | 83 |
| stroke 246 | 14 % → 0 % | 81.8 px | 0.00 | 0.00 | 139 |
| stroke 247 | 15 % → 0 % | 60.1 px | 0.00 | 0.00 | 271 |
| stroke 248 | 19 % → 0 % | 93.5 px | 0.00 | 0.00 | 204 |
| stroke 249 | 22 % → 0 % | 161.0 px | 0.00 | 0.00 | 127 |
| stroke 250 | 24 % → 0 % | 227.4 px | 0.33 | 0.02 | 73 |
| stroke 251 | 23 % → 1 % | 144.0 px | 0.32 | 0.06 | 137 |
| stroke 252 | 27 % → 0 % | 266.9 px | 0.00 | 0.00 | 62 |
| stroke 253 | 20 % → 2 % | 194.3 px | 0.32 | 0.09 | 81 |
| stroke 254 | 22 % → 2 % | 381.2 px | 0.32 | 0.09 | 29 |
| stroke 255 | 19 % → 2 % | 156.2 px | 0.32 | 0.10 | 73 |
| stroke 256 | 19 % → 2 % | 137.2 px | 0.32 | 0.09 | 92 |
| stroke 257 | 18 % → 2 % | 184.4 px | 0.32 | 0.10 | 71 |
| stroke 258 | 16 % → 2 % | 114.3 px | 0.32 | 0.11 | 93 |
| stroke 259 | 24 % → 1 % | 303.7 px | 0.32 | 0.05 | 39 |
| stroke 260 | 13 % → 1 % | 213.3 px | 0.32 | 0.08 | 32 |
| stroke 261 | 34 % → 2 % | 602.8 px | 0.32 | 0.06 | 27 |
| stroke 262 | 20 % → 2 % | 190.8 px | 0.32 | 0.10 | 61 |
| stroke 263 | 26 % → 2 % | 208.9 px | 0.32 | 0.07 | 80 |
| stroke 264 | 45 % → 2 % | 568.9 px | 0.32 | 0.04 | 43 |
| stroke 265 | 24 % → 2 % | 293.3 px | 0.32 | 0.08 | 49 |
| stroke 266 | 25 % → 2 % | 200.9 px | 0.32 | 0.07 | 86 |
| stroke 267 | 44 % → 2 % | 520.0 px | 0.32 | 0.05 | 44 |
| stroke 268 | 28 % → 2 % | 322.6 px | 0.32 | 0.07 | 54 |
| stroke 269 | 29 % → 2 % | 335.3 px | 0.32 | 0.07 | 50 |
| stroke 270 | 27 % → 2 % | 223.1 px | 0.32 | 0.07 | 93 |
| stroke 271 | 27 % → 2 % | 265.4 px | 0.32 | 0.07 | 56 |
| stroke 272 | 21 % → 2 % | 267.9 px | 0.32 | 0.09 | 36 |
| stroke 273 | 6 % → 0 % | 26.2 px | 0.00 | 0.00 | 164 |
| stroke 274 | 10 % → 0 % | 38.5 px | 0.00 | 0.00 | 269 |
| stroke 275 | 15 % → 0 % | 174.6 px | 0.00 | 0.00 | 60 |
| stroke 276 | 15 % → 0 % | 185.2 px | 0.00 | 0.00 | 43 |
| stroke 277 | 16 % → 0 % | 285.1 px | 0.00 | 0.00 | 33 |
| stroke 278 | 16 % → 0 % | 273.1 px | 0.00 | 0.00 | 34 |
| stroke 279 | 19 % → 0 % | 239.5 px | 0.00 | 0.00 | 53 |
| stroke 280 | 17 % → 0 % | 265.7 px | 0.00 | 0.00 | 46 |
| stroke 281 | 21 % → 0 % | 268.6 px | 0.00 | 0.00 | 48 |
| stroke 282 | 20 % → 0 % | 232.4 px | 0.00 | 0.00 | 49 |
| stroke 283 | 19 % → 0 % | 227.8 px | 0.00 | 0.00 | 59 |
| stroke 284 | 19 % → 0 % | 316.9 px | 0.00 | 0.00 | 31 |
| stroke 285 | 16 % → 0 % | 274.7 px | 0.00 | 0.00 | 39 |
| stroke 286 | 15 % → 0 % | 278.8 px | 0.00 | 0.00 | 29 |
| stroke 287 | 14 % → 0 % | 248.3 px | 0.00 | 0.00 | 32 |
| stroke 288 | 12 % → 0 % | 199.4 px | 0.00 | 0.00 | 35 |
| stroke 289 | 18 % → 0 % | 183.2 px | 0.00 | 0.00 | 67 |
| stroke 290 | 15 % → 0 % | 185.3 px | 0.00 | 0.00 | 39 |
| stroke 291 | 23 % → 0 % | 83.1 px | 0.00 | 0.00 | 224 |
| stroke 292 | 26 % → 0 % | 95.6 px | 0.00 | 0.00 | 263 |
| stroke 293 | 30 % → 0 % | 107.1 px | 0.00 | 0.00 | 302 |
| stroke 294 | 32 % → 0 % | 115.3 px | 0.00 | 0.00 | 297 |
| stroke 295 | 31 % → 0 % | 164.0 px | 0.00 | 0.00 | 199 |
| stroke 296 | 2 % → 0 % | 15.7 px | 0.00 | 0.00 | 71 |
| stroke 297 | 5 % → 0 % | 34.9 px | 0.00 | 0.00 | 56 |
| stroke 298 | 3 % → 0 % | 43.6 px | 0.00 | 0.00 | 52 |
| stroke 299 | 8 % → 0 % | 37.4 px | 0.00 | 0.00 | 203 |
| stroke 300 | 13 % → 0 % | 125.3 px | 0.00 | 0.00 | 72 |
| stroke 301 | 6 % → 0 % | 38.4 px | 0.00 | 0.00 | 129 |
| stroke 302 | 10 % → 0 % | 48.5 px | 0.00 | 0.00 | 202 |
| stroke 303 | 14 % → 0 % | 76.2 px | 0.00 | 0.00 | 202 |
| stroke 304 | 18 % → 0 % | 106.8 px | 0.00 | 0.00 | 152 |
| stroke 305 | 22 % → 0 % | 108.4 px | 0.00 | 0.00 | 176 |
| stroke 306 | 23 % → 0 % | 127.2 px | 0.00 | 0.00 | 162 |
| stroke 307 | 25 % → 0 % | 203.3 px | 0.00 | 0.00 | 104 |
| stroke 308 | 1 % → 0 % | 11.1 px | 0.00 | 0.00 | 12 |
| stroke 309 | 3 % → 24 % | 28.0 px | 0.34 | 7.43 | 102 |
| stroke 310 | 6 % → 21 % | 33.6 px | 0.34 | 3.81 | 176 |
| stroke 311 | 8 % → 19 % | 40.3 px | 0.34 | 2.42 | 199 |
| stroke 312 | 16 % → 34 % | 268.0 px | 0.34 | 2.16 | 34 |
| stroke 313 | 17 % → 36 % | 308.1 px | 0.34 | 2.12 | 26 |
| stroke 314 | 18 % → 36 % | 229.9 px | 0.34 | 2.03 | 51 |
| stroke 315 | 16 % → 29 % | 95.8 px | 0.34 | 1.77 | 136 |
| stroke 316 | 19 % → 34 % | 115.8 px | 0.34 | 1.78 | 132 |
| stroke 317 | 26 % → 41 % | 468.6 px | 0.34 | 1.58 | 29 |
| stroke 318 | 21 % → 40 % | 263.0 px | 0.34 | 1.94 | 131 |
| stroke 319 | 17 % → 36 % | 172.9 px | 0.34 | 2.12 | 70 |
| stroke 320 | 19 % → 32 % | 121.4 px | 0.34 | 1.71 | 117 |
| stroke 321 | 17 % → 35 % | 131.4 px | 0.34 | 2.06 | 108 |
| stroke 322 | 16 % → 37 % | 103.4 px | 0.34 | 2.28 | 135 |
| stroke 323 | 21 % → 40 % | 181.7 px | 0.34 | 1.92 | 96 |
| stroke 324 | 19 % → 37 % | 187.9 px | 0.34 | 2.02 | 57 |
| stroke 325 | 25 % → 40 % | 436.1 px | 0.34 | 1.61 | 36 |
| stroke 326 | 18 % → 33 % | 283.4 px | 0.34 | 1.82 | 36 |
| stroke 327 | 21 % → 35 % | 388.9 px | 0.34 | 1.66 | 29 |
| stroke 328 | 15 % → 28 % | 198.4 px | 0.35 | 1.79 | 50 |
| stroke 329 | 20 % → 33 % | 362.9 px | 0.34 | 1.68 | 28 |
| stroke 330 | 15 % → 25 % | 153.5 px | 0.35 | 1.69 | 53 |
| stroke 331 | 18 % → 27 % | 143.2 px | 0.35 | 1.45 | 85 |
| stroke 332 | 20 % → 26 % | 139.0 px | 0.35 | 1.28 | 101 |
| stroke 333 | 23 % → 26 % | 160.0 px | 0.35 | 1.11 | 103 |
| stroke 334 | 24 % → 24 % | 163.6 px | 0.34 | 1.00 | 106 |
| stroke 335 | 2 % → 2 % | 35.8 px | 0.32 | 1.00 | 31 |

Numbers say: wet paint spreads well beyond the stroke.

## Refs v3 · #43 Dragged black blocks — own sheet
own sheet 800 × 1115 · Ink 0.93 · Gouache 0.07 · 112 px · 836.9 s

![Refs v3 · #43 Dragged black blocks — own sheet](Refs-v3-43-Dragged-black-blocks-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 11 % → 68 % | 101.3 px | 0.50 | 6.08 | 1084 |
| stroke 2 | 16 % → 73 % | 161.6 px | 0.50 | 4.54 | 1313 |
| stroke 3 | 18 % → 76 % | 211.9 px | 0.49 | 4.15 | 1780 |
| stroke 4 | 21 % → 79 % | 266.0 px | 0.49 | 3.70 | 2225 |
| stroke 5 | 22 % → 82 % | 223.2 px | 0.49 | 3.66 | 3936 |
| stroke 6 | 26 % → 87 % | 336.5 px | 0.49 | 3.28 | 3094 |
| stroke 7 | 26 % → 88 % | 269.6 px | 0.49 | 3.40 | 3403 |
| stroke 8 | 23 % → 54 % | 526.5 px | 0.49 | 2.31 | 956 |
| stroke 9 | 26 % → 78 % | 232.1 px | 0.50 | 2.94 | 8820 |
| stroke 10 | 28 % → 78 % | 264.0 px | 0.50 | 2.73 | 11315 |
| stroke 11 | 31 % → 77 % | 306.7 px | 0.50 | 2.47 | 7690 |
| stroke 12 | 35 % → 81 % | 338.7 px | 0.50 | 2.35 | 8477 |
| stroke 13 | 40 % → 92 % | 415.2 px | 0.50 | 2.27 | 6020 |
| stroke 14 | 44 % → 85 % | 783.7 px | 0.50 | 1.92 | 3053 |
| stroke 15 | 37 % → 86 % | 377.5 px | 0.50 | 2.35 | 11568 |
| stroke 16 | 17 % → 53 % | 159.6 px | 0.50 | 3.12 | 2184 |
| stroke 17 | 38 % → 88 % | 406.1 px | 0.50 | 2.30 | 18718 |
| stroke 18 | 34 % → 64 % | 287.3 px | 0.50 | 1.89 | 3639 |
| stroke 19 | 43 % → 81 % | 377.2 px | 0.50 | 1.90 | 17903 |
| stroke 20 | 45 % → 82 % | 432.2 px | 0.50 | 1.80 | 16500 |
| stroke 21 | 50 % → 91 % | 444.9 px | 0.50 | 1.81 | 11890 |
| stroke 22 | 56 % → 78 % | 623.8 px | 0.50 | 1.40 | 4476 |
| stroke 23 | 59 % → 90 % | 468.1 px | 0.50 | 1.52 | 19658 |
| stroke 24 | 58 % → 88 % | 446.9 px | 0.51 | 1.53 | 7235 |
| stroke 25 | 66 % → 86 % | 642.2 px | 0.50 | 1.30 | 8584 |
| stroke 26 | 59 % → 86 % | 498.7 px | 0.51 | 1.45 | 5541 |
| stroke 27 | 67 % → 87 % | 654.1 px | 0.50 | 1.30 | 5058 |
| stroke 28 | 61 % → 85 % | 595.2 px | 0.51 | 1.39 | 4762 |
| stroke 29 | 67 % → 88 % | 668.5 px | 0.50 | 1.31 | 12490 |
| stroke 30 | 63 % → 88 % | 634.7 px | 0.51 | 1.41 | 9466 |
| stroke 31 | 67 % → 88 % | 683.8 px | 0.50 | 1.32 | 7384 |
| stroke 32 | 64 % → 90 % | 649.4 px | 0.51 | 1.40 | 4992 |
| stroke 33 | 66 % → 87 % | 718.9 px | 0.50 | 1.32 | 3314 |
| stroke 34 | 63 % → 89 % | 628.3 px | 0.51 | 1.40 | 5287 |
| stroke 35 | 66 % → 86 % | 751.8 px | 0.50 | 1.31 | 3272 |
| stroke 36 | 68 % → 87 % | 643.3 px | 0.51 | 1.28 | 4688 |
| stroke 37 | 67 % → 85 % | 873.2 px | 0.50 | 1.27 | 1844 |
| stroke 38 | 71 % → 86 % | 613.7 px | 0.51 | 1.21 | 3541 |
| stroke 39 | 75 % → 84 % | 572.6 px | 0.51 | 1.11 | 3898 |
| stroke 40 | 77 % → 81 % | 524.1 px | 0.51 | 1.06 | 4076 |
| stroke 41 | 78 % → 80 % | 601.6 px | 0.51 | 1.02 | 2500 |
| stroke 42 | 84 % → 84 % | 891.0 px | 0.51 | 1.00 | 964 |

Numbers say: wet paint spreads well beyond the stroke.

## Refs v3 · #44 Blue looping ribbon — own sheet
own sheet 800 × 1204 · Oil 0.52 · Gouache 0.48 + turpentine 10 % · 51 px · 1041.1 s

![Refs v3 · #44 Blue looping ribbon — own sheet](Refs-v3-44-Blue-looping-ribbon-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 7 % → 1 % | 49.5 px | 0.28 | 0.10 | 691 |
| stroke 2 | 10 % → 0 % | 58.6 px | 0.28 | 0.05 | 1384 |
| stroke 3 | 11 % → 0 % | 71.5 px | 0.29 | 0.01 | 1000 |
| stroke 4 | 17 % → 0 % | 99.7 px | 0.28 | 0.02 | 2095 |
| stroke 5 | 22 % → 0 % | 151.4 px | 0.00 | 0.00 | 391 |
| stroke 6 | 14 % → 0 % | 84.7 px | 0.28 | 0.02 | 3005 |
| stroke 7 | 21 % → 0 % | 167.2 px | 0.00 | 0.00 | 213 |
| stroke 8 | 18 % → 0 % | 125.1 px | 0.00 | 0.00 | 761 |
| stroke 9 | 39 % → 1 % | 689.9 px | 0.28 | 0.03 | 138 |
| stroke 10 | 39 % → 1 % | 401.2 px | 0.28 | 0.02 | 395 |
| stroke 11 | 21 % → 0 % | 176.4 px | 0.00 | 0.00 | 127 |
| stroke 12 | 20 % → 0 % | 143.3 px | 0.00 | 0.00 | 663 |
| stroke 13 | 21 % → 0 % | 206.1 px | 0.00 | 0.00 | 147 |
| stroke 14 | 20 % → 0 % | 171.6 px | 0.00 | 0.00 | 444 |
| stroke 15 | 20 % → 0 % | 192.2 px | 0.00 | 0.00 | 386 |
| stroke 16 | 19 % → 0 % | 182.1 px | 0.00 | 0.00 | 373 |
| stroke 17 | 20 % → 0 % | 205.6 px | 0.00 | 0.00 | 325 |
| stroke 18 | 19 % → 0 % | 174.6 px | 0.00 | 0.00 | 394 |
| stroke 19 | 21 % → 0 % | 157.5 px | 0.00 | 0.00 | 628 |
| stroke 20 | 24 % → 0 % | 391.2 px | 0.00 | 0.00 | 189 |
| stroke 21 | 31 % → 0 % | 352.2 px | 0.00 | 0.00 | 296 |
| stroke 22 | 30 % → 0 % | 336.7 px | 0.00 | 0.00 | 528 |
| stroke 23 | 29 % → 0 % | 419.6 px | 0.00 | 0.00 | 193 |
| stroke 24 | 25 % → 0 % | 434.7 px | 0.00 | 0.00 | 256 |
| stroke 25 | 22 % → 0 % | 321.1 px | 0.00 | 0.00 | 172 |
| stroke 26 | 20 % → 0 % | 344.6 px | 0.00 | 0.00 | 185 |
| stroke 27 | 25 % → 0 % | 109.0 px | 0.00 | 0.00 | 2214 |
| stroke 28 | 36 % → 0 % | 150.5 px | 0.00 | 0.00 | 1859 |
| stroke 29 | 32 % → 0 % | 144.4 px | 0.30 | 0.00 | 1640 |
| stroke 30 | 42 % → 0 % | 206.4 px | 0.00 | 0.00 | 1802 |
| stroke 31 | 30 % → 0 % | 165.0 px | 0.00 | 0.00 | 1793 |
| stroke 32 | 30 % → 1 % | 153.3 px | 0.28 | 0.02 | 1496 |
| stroke 33 | 42 % → 1 % | 156.7 px | 0.28 | 0.02 | 1577 |
| stroke 34 | 32 % → 1 % | 165.5 px | 0.28 | 0.02 | 1351 |
| stroke 35 | 10 % → 0 % | 105.1 px | 0.00 | 0.00 | 224 |
| stroke 36 | 33 % → 0 % | 79.4 px | 0.00 | 0.00 | 1565 |
| stroke 37 | 35 % → 0 % | 370.6 px | 0.00 | 0.00 | 145 |
| stroke 38 | 43 % → 0 % | 381.2 px | 0.00 | 0.00 | 388 |
| stroke 39 | 45 % → 0 % | 450.7 px | 0.00 | 0.00 | 520 |
| stroke 40 | 34 % → 0 % | 189.6 px | 0.00 | 0.00 | 599 |
| stroke 41 | 36 % → 0 % | 197.9 px | 0.00 | 0.00 | 501 |
| stroke 42 | 16 % → 0 % | 128.0 px | 0.00 | 0.00 | 563 |
| stroke 43 | 23 % → 0 % | 132.7 px | 0.00 | 0.00 | 1125 |
| stroke 44 | 26 % → 0 % | 146.8 px | 0.00 | 0.00 | 1556 |
| stroke 45 | 29 % → 0 % | 162.5 px | 0.00 | 0.00 | 1294 |
| stroke 46 | 31 % → 0 % | 179.6 px | 0.00 | 0.00 | 1850 |
| stroke 47 | 30 % → 0 % | 165.7 px | 0.00 | 0.00 | 1196 |
| stroke 48 | 33 % → 0 % | 198.2 px | 0.00 | 0.00 | 1061 |
| stroke 49 | 39 % → 0 % | 250.6 px | 0.00 | 0.00 | 893 |
| stroke 50 | 37 % → 0 % | 236.9 px | 0.00 | 0.00 | 566 |
| stroke 51 | 37 % → 0 % | 213.9 px | 0.00 | 0.00 | 922 |
| stroke 52 | 39 % → 0 % | 261.6 px | 0.00 | 0.00 | 540 |
| stroke 53 | 38 % → 0 % | 656.2 px | 0.00 | 0.00 | 129 |
| stroke 54 | 55 % → 0 % | 255.6 px | 0.00 | 0.00 | 1703 |
| stroke 55 | 60 % → 0 % | 249.6 px | 0.00 | 0.00 | 2356 |
| stroke 56 | 50 % → 0 % | 207.8 px | 0.00 | 0.00 | 2243 |
| stroke 57 | 55 % → 0 % | 331.8 px | 0.00 | 0.00 | 1070 |
| stroke 58 | 45 % → 0 % | 246.3 px | 0.00 | 0.00 | 1311 |
| stroke 59 | 47 % → 0 % | 275.1 px | 0.00 | 0.00 | 1195 |
| stroke 60 | 17 % → 0 % | 156.1 px | 0.00 | 0.00 | 223 |
| stroke 61 | 23 % → 0 % | 113.4 px | 0.00 | 0.00 | 780 |
| stroke 62 | 30 % → 0 % | 171.0 px | 0.00 | 0.00 | 592 |
| stroke 63 | 20 % → 0 % | 149.2 px | 0.00 | 0.00 | 346 |
| stroke 64 | 14 % → 0 % | 194.1 px | 0.00 | 0.00 | 150 |
| stroke 65 | 45 % → 0 % | 725.5 px | 0.00 | 0.00 | 122 |
| stroke 66 | 15 % → 0 % | 240.6 px | 0.00 | 0.00 | 146 |
| stroke 67 | 56 % → 0 % | 653.6 px | 0.00 | 0.00 | 243 |
| stroke 68 | 61 % → 0 % | 832.0 px | 0.00 | 0.00 | 231 |
| stroke 69 | 60 % → 0 % | 457.5 px | 0.00 | 0.00 | 1077 |
| stroke 70 | 39 % → 0 % | 147.3 px | 0.00 | 0.00 | 6781 |
| stroke 71 | 36 % → 0 % | 234.3 px | 0.00 | 0.00 | 1384 |
| stroke 72 | 55 % → 0 % | 564.7 px | 0.00 | 0.00 | 508 |
| stroke 73 | 16 % → 0 % | 75.2 px | 0.00 | 0.00 | 1447 |
| stroke 74 | 17 % → 0 % | 163.9 px | 0.00 | 0.00 | 508 |
| stroke 75 | 28 % → 0 % | 407.1 px | 0.00 | 0.00 | 290 |
| stroke 76 | 36 % → 0 % | 369.5 px | 0.00 | 0.00 | 284 |
| stroke 77 | 16 % → 0 % | 265.0 px | 0.00 | 0.00 | 228 |
| stroke 78 | 17 % → 0 % | 47.4 px | 0.00 | 0.00 | 3443 |
| stroke 79 | 21 % → 0 % | 61.8 px | 0.00 | 0.00 | 2198 |
| stroke 80 | 26 % → 0 % | 79.7 px | 0.00 | 0.00 | 2417 |
| stroke 81 | 32 % → 0 % | 104.3 px | 0.00 | 0.00 | 2173 |
| stroke 82 | 39 % → 0 % | 135.3 px | 0.00 | 0.00 | 1718 |
| stroke 83 | 39 % → 0 % | 137.1 px | 0.00 | 0.00 | 1495 |
| stroke 84 | 48 % → 0 % | 127.5 px | 0.00 | 0.00 | 1718 |
| stroke 85 | 44 % → 0 % | 142.6 px | 0.00 | 0.00 | 1743 |
| stroke 86 | 4 % → 0 % | 63.7 px | 0.00 | 0.00 | 89 |
| stroke 87 | 11 % → 0 % | 138.3 px | 0.00 | 0.00 | 173 |
| stroke 88 | 15 % → 0 % | 142.2 px | 0.00 | 0.00 | 336 |
| stroke 89 | 14 % → 0 % | 209.9 px | 0.00 | 0.00 | 169 |
| stroke 90 | 15 % → 0 % | 170.5 px | 0.00 | 0.00 | 454 |
| stroke 91 | 16 % → 0 % | 170.9 px | 0.00 | 0.00 | 350 |
| stroke 92 | 18 % → 0 % | 227.8 px | 0.00 | 0.00 | 193 |
| stroke 93 | 25 % → 0 % | 274.8 px | 0.00 | 0.00 | 364 |
| stroke 94 | 20 % → 0 % | 86.3 px | 0.00 | 0.00 | 1479 |
| stroke 95 | 8 % → 0 % | 108.4 px | 0.00 | 0.00 | 134 |
| stroke 96 | 22 % → 0 % | 124.9 px | 0.00 | 0.00 | 692 |
| stroke 97 | 24 % → 0 % | 136.9 px | 0.00 | 0.00 | 790 |
| stroke 98 | 28 % → 0 % | 114.2 px | 0.00 | 0.00 | 1281 |
| stroke 99 | 32 % → 0 % | 220.2 px | 0.00 | 0.00 | 570 |
| stroke 100 | 33 % → 0 % | 473.9 px | 0.00 | 0.00 | 167 |
| stroke 101 | 44 % → 0 % | 356.0 px | 0.00 | 0.00 | 531 |
| stroke 102 | 2 % → 0 % | 11.4 px | 0.00 | 0.00 | 92 |
| stroke 103 | 1 % → 0 % | 12.3 px | 0.00 | 0.00 | 29 |
| stroke 104 | 2 % → 0 % | 11.4 px | 0.00 | 0.00 | 35 |
| stroke 105 | 1 % → 0 % | 26.3 px | 0.00 | 0.00 | 12 |
| stroke 106 | 1 % → 0 % | 16.4 px | 0.00 | 0.00 | 22 |
| stroke 107 | 1 % → 0 % | 12.7 px | 0.00 | 0.00 | 26 |
| stroke 108 | 2 % → 0 % | 34.9 px | 0.00 | 0.00 | 20 |
| stroke 109 | 1 % → 0 % | 13.3 px | 0.00 | 0.00 | 24 |
| stroke 110 | 4 % → 0 % | 29.7 px | 0.00 | 0.00 | 89 |
| stroke 111 | 1 % → 0 % | 17.5 px | 0.00 | 0.00 | 22 |
| stroke 112 | 3 % → 0 % | 35.1 px | 0.00 | 0.00 | 56 |
| stroke 113 | 6 % → 0 % | 58.1 px | 0.00 | 0.00 | 552 |
| stroke 114 | 10 % → 0 % | 68.0 px | 0.27 | 0.03 | 863 |
| stroke 115 | 12 % → 0 % | 78.3 px | 0.28 | 0.04 | 1086 |
| stroke 116 | 15 % → 0 % | 92.3 px | 0.28 | 0.03 | 1432 |
| stroke 117 | 17 % → 0 % | 103.6 px | 0.28 | 0.02 | 1672 |
| stroke 118 | 21 % → 0 % | 125.2 px | 0.28 | 0.02 | 2032 |
| stroke 119 | 23 % → 0 % | 109.3 px | 0.28 | 0.02 | 2061 |
| stroke 120 | 32 % → 1 % | 415.4 px | 0.28 | 0.03 | 468 |
| stroke 121 | 22 % → 0 % | 192.9 px | 0.00 | 0.00 | 450 |
| stroke 122 | 13 % → 0 % | 56.3 px | 0.00 | 0.00 | 1001 |
| stroke 123 | 17 % → 0 % | 68.6 px | 0.00 | 0.00 | 1579 |
| stroke 124 | 21 % → 0 % | 84.0 px | 0.00 | 0.00 | 1603 |
| stroke 125 | 27 % → 0 % | 156.5 px | 0.00 | 0.00 | 984 |
| stroke 126 | 36 % → 0 % | 214.8 px | 0.00 | 0.00 | 842 |
| stroke 127 | 25 % → 0 % | 112.7 px | 0.00 | 0.00 | 2829 |
| stroke 128 | 32 % → 0 % | 178.3 px | 0.27 | 0.00 | 2182 |
| stroke 129 | 38 % → 0 % | 240.2 px | 0.00 | 0.00 | 890 |
| stroke 130 | 33 % → 0 % | 178.1 px | 0.28 | 0.01 | 2006 |
| stroke 131 | 39 % → 0 % | 519.1 px | 0.00 | 0.00 | 261 |
| stroke 132 | 27 % → 0 % | 338.7 px | 0.00 | 0.00 | 433 |
| stroke 133 | 33 % → 1 % | 211.7 px | 0.28 | 0.02 | 1138 |
| stroke 134 | 54 % → 0 % | 333.7 px | 0.00 | 0.00 | 1051 |
| stroke 135 | 38 % → 0 % | 231.8 px | 0.00 | 0.00 | 906 |
| stroke 136 | 36 % → 1 % | 211.2 px | 0.28 | 0.01 | 1427 |
| stroke 137 | 55 % → 0 % | 381.0 px | 0.00 | 0.00 | 2945 |
| stroke 138 | 32 % → 0 % | 210.4 px | 0.00 | 0.00 | 2516 |
| stroke 139 | 37 % → 1 % | 217.6 px | 0.28 | 0.01 | 2883 |
| stroke 140 | 40 % → 0 % | 211.2 px | 0.00 | 0.00 | 3786 |
| stroke 141 | 39 % → 0 % | 220.6 px | 0.28 | 0.01 | 2387 |
| stroke 142 | 40 % → 0 % | 212.1 px | 0.00 | 0.00 | 2629 |
| stroke 143 | 47 % → 0 % | 654.5 px | 0.00 | 0.00 | 266 |
| stroke 144 | 46 % → 0 % | 352.6 px | 0.00 | 0.00 | 820 |
| stroke 145 | 48 % → 0 % | 476.1 px | 0.00 | 0.00 | 378 |
| stroke 146 | 42 % → 0 % | 225.8 px | 0.00 | 0.00 | 2185 |
| stroke 147 | 47 % → 0 % | 668.8 px | 0.00 | 0.00 | 303 |
| stroke 148 | 49 % → 0 % | 690.2 px | 0.00 | 0.00 | 172 |
| stroke 149 | 49 % → 0 % | 285.0 px | 0.00 | 0.00 | 1690 |
| stroke 150 | 38 % → 0 % | 208.6 px | 0.00 | 0.00 | 1792 |
| stroke 151 | 48 % → 0 % | 339.3 px | 0.00 | 0.00 | 638 |
| stroke 152 | 51 % → 0 % | 293.0 px | 0.00 | 0.00 | 1067 |
| stroke 153 | 56 % → 0 % | 440.5 px | 0.00 | 0.00 | 574 |
| stroke 154 | 33 % → 0 % | 211.2 px | 0.00 | 0.00 | 686 |
| stroke 155 | 44 % → 0 % | 320.4 px | 0.00 | 0.00 | 634 |
| stroke 156 | 50 % → 0 % | 281.4 px | 0.00 | 0.00 | 1228 |
| stroke 157 | 43 % → 0 % | 222.8 px | 0.00 | 0.00 | 2102 |
| stroke 158 | 43 % → 0 % | 258.6 px | 0.00 | 0.00 | 1007 |
| stroke 159 | 47 % → 0 % | 310.6 px | 0.00 | 0.00 | 884 |
| stroke 160 | 55 % → 0 % | 452.5 px | 0.00 | 0.00 | 462 |
| stroke 161 | 57 % → 0 % | 439.5 px | 0.00 | 0.00 | 496 |
| stroke 162 | 39 % → 0 % | 212.0 px | 0.00 | 0.00 | 756 |
| stroke 163 | 42 % → 0 % | 246.1 px | 0.00 | 0.00 | 974 |
| stroke 164 | 50 % → 0 % | 691.8 px | 0.00 | 0.00 | 217 |
| stroke 165 | 50 % → 0 % | 464.2 px | 0.00 | 0.00 | 1210 |
| stroke 166 | 54 % → 0 % | 468.2 px | 0.00 | 0.00 | 1530 |
| stroke 167 | 54 % → 0 % | 403.4 px | 0.00 | 0.00 | 1481 |
| stroke 168 | 42 % → 0 % | 207.9 px | 0.00 | 0.00 | 1093 |
| stroke 169 | 40 % → 0 % | 238.2 px | 0.00 | 0.00 | 1186 |
| stroke 170 | 49 % → 0 % | 273.3 px | 0.00 | 0.00 | 1554 |
| stroke 171 | 56 % → 0 % | 362.2 px | 0.00 | 0.00 | 1688 |
| stroke 172 | 52 % → 0 % | 256.7 px | 0.00 | 0.00 | 1229 |
| stroke 173 | 37 % → 0 % | 256.5 px | 0.00 | 0.00 | 876 |
| stroke 174 | 49 % → 0 % | 271.8 px | 0.00 | 0.00 | 1669 |
| stroke 175 | 56 % → 0 % | 295.0 px | 0.00 | 0.00 | 1415 |
| stroke 176 | 35 % → 0 % | 307.4 px | 0.00 | 0.00 | 403 |
| stroke 177 | 52 % → 0 % | 274.1 px | 0.00 | 0.00 | 3018 |
| stroke 178 | 34 % → 0 % | 343.9 px | 0.00 | 0.00 | 372 |
| stroke 179 | 50 % → 0 % | 273.8 px | 0.00 | 0.00 | 1733 |
| stroke 180 | 55 % → 0 % | 315.4 px | 0.00 | 0.00 | 1187 |
| stroke 181 | 34 % → 0 % | 339.3 px | 0.00 | 0.00 | 902 |
| stroke 182 | 34 % → 0 % | 319.0 px | 0.00 | 0.00 | 1426 |
| stroke 183 | 53 % → 0 % | 295.1 px | 0.00 | 0.00 | 4932 |
| stroke 184 | 53 % → 0 % | 322.3 px | 0.00 | 0.00 | 1377 |
| stroke 185 | 32 % → 0 % | 293.5 px | 0.00 | 0.00 | 382 |
| stroke 186 | 27 % → 0 % | 296.1 px | 0.00 | 0.00 | 284 |
| stroke 187 | 54 % → 0 % | 298.4 px | 0.00 | 0.00 | 1452 |
| stroke 188 | 50 % → 0 % | 333.1 px | 0.00 | 0.00 | 813 |
| stroke 189 | 24 % → 0 % | 291.9 px | 0.00 | 0.00 | 269 |
| stroke 190 | 34 % → 0 % | 372.9 px | 0.00 | 0.00 | 269 |
| stroke 191 | 51 % → 0 % | 291.9 px | 0.00 | 0.00 | 1304 |
| stroke 192 | 48 % → 0 % | 472.1 px | 0.00 | 0.00 | 326 |
| stroke 193 | 25 % → 0 % | 275.5 px | 0.00 | 0.00 | 286 |
| stroke 194 | 32 % → 0 % | 452.9 px | 0.00 | 0.00 | 177 |
| stroke 195 | 49 % → 0 % | 270.4 px | 0.00 | 0.00 | 1348 |
| stroke 196 | 42 % → 0 % | 391.7 px | 0.00 | 0.00 | 828 |
| stroke 197 | 29 % → 0 % | 196.4 px | 0.00 | 0.00 | 1004 |
| stroke 198 | 36 % → 0 % | 247.9 px | 0.00 | 0.00 | 662 |
| stroke 199 | 48 % → 0 % | 256.7 px | 0.00 | 0.00 | 1736 |
| stroke 200 | 38 % → 0 % | 415.0 px | 0.00 | 0.00 | 258 |
| stroke 201 | 37 % → 0 % | 196.5 px | 0.00 | 0.00 | 1738 |
| stroke 202 | 33 % → 0 % | 458.0 px | 0.00 | 0.00 | 249 |
| stroke 203 | 44 % → 0 % | 278.0 px | 0.00 | 0.00 | 980 |
| stroke 204 | 51 % → 0 % | 379.8 px | 0.00 | 0.00 | 609 |
| stroke 205 | 34 % → 0 % | 382.8 px | 0.00 | 0.00 | 259 |
| stroke 206 | 46 % → 0 % | 261.4 px | 0.00 | 0.00 | 722 |
| stroke 207 | 43 % → 0 % | 243.5 px | 0.00 | 0.00 | 2102 |
| stroke 208 | 53 % → 0 % | 304.9 px | 0.00 | 0.00 | 2409 |
| stroke 209 | 39 % → 0 % | 388.4 px | 0.00 | 0.00 | 426 |
| stroke 210 | 51 % → 0 % | 293.5 px | 0.00 | 0.00 | 957 |
| stroke 211 | 40 % → 0 % | 322.9 px | 0.00 | 0.00 | 984 |
| stroke 212 | 52 % → 0 % | 352.2 px | 0.00 | 0.00 | 1077 |
| stroke 213 | 40 % → 0 % | 268.5 px | 0.00 | 0.00 | 680 |
| stroke 214 | 53 % → 0 % | 236.4 px | 0.00 | 0.00 | 1682 |
| stroke 215 | 50 % → 0 % | 256.1 px | 0.00 | 0.00 | 3451 |
| stroke 216 | 60 % → 0 % | 283.7 px | 0.00 | 0.00 | 969 |
| stroke 217 | 48 % → 0 % | 260.4 px | 0.00 | 0.00 | 3417 |
| stroke 218 | 67 % → 0 % | 297.5 px | 0.00 | 0.00 | 1689 |
| stroke 219 | 50 % → 0 % | 261.6 px | 0.00 | 0.00 | 4184 |
| stroke 220 | 57 % → 0 % | 249.4 px | 0.00 | 0.00 | 2946 |
| stroke 221 | 63 % → 0 % | 265.2 px | 0.00 | 0.00 | 1793 |
| stroke 222 | 68 % → 0 % | 264.2 px | 0.00 | 0.00 | 1653 |
| stroke 223 | 71 % → 0 % | 259.8 px | 0.00 | 0.00 | 1449 |
| stroke 224 | 73 % → 0 % | 264.6 px | 0.00 | 0.00 | 1088 |
| stroke 225 | 76 % → 0 % | 301.8 px | 0.00 | 0.00 | 640 |
| stroke 226 | 74 % → 0 % | 463.2 px | 0.00 | 0.00 | 226 |
| stroke 227 | 64 % → 0 % | 253.1 px | 0.00 | 0.00 | 1276 |
| stroke 228 | 58 % → 0 % | 266.1 px | 0.00 | 0.00 | 1424 |
| stroke 229 | 63 % → 0 % | 311.1 px | 0.00 | 0.00 | 1232 |
| stroke 230 | 80 % → 0 % | 290.8 px | 0.00 | 0.00 | 1385 |
| stroke 231 | 92 % → 0 % | 251.9 px | 0.00 | 0.00 | 1540 |
| stroke 232 | 59 % → 0 % | 221.8 px | 0.00 | 0.00 | 1526 |
| stroke 233 | 67 % → 0 % | 276.6 px | 0.00 | 0.00 | 1589 |
| stroke 234 | 83 % → 0 % | 309.7 px | 0.00 | 0.00 | 1405 |
| stroke 235 | 88 % → 0 % | 361.3 px | 0.00 | 0.00 | 1317 |
| stroke 236 | 92 % → 0 % | 407.3 px | 0.00 | 0.00 | 1303 |
| stroke 237 | 91 % → 0 % | 422.4 px | 0.00 | 0.00 | 1477 |
| stroke 238 | 88 % → 0 % | 359.7 px | 0.00 | 0.00 | 1424 |
| stroke 239 | 75 % → 0 % | 328.9 px | 0.00 | 0.00 | 1600 |
| stroke 240 | 84 % → 0 % | 390.0 px | 0.00 | 0.00 | 2100 |
| stroke 241 | 93 % → 0 % | 394.8 px | 0.00 | 0.00 | 1588 |
| stroke 242 | 97 % → 0 % | 391.8 px | 0.00 | 0.00 | 1615 |
| stroke 243 | 87 % → 0 % | 399.0 px | 0.00 | 0.00 | 1876 |
| stroke 244 | 70 % → 1 % | 322.4 px | 0.28 | 0.01 | 1619 |
| stroke 245 | 74 % → 0 % | 341.4 px | 0.00 | 0.00 | 1443 |
| stroke 246 | 60 % → 0 % | 279.3 px | 0.00 | 0.00 | 1713 |
| stroke 247 | 71 % → 0 % | 368.1 px | 0.00 | 0.00 | 1726 |
| stroke 248 | 68 % → 1 % | 291.5 px | 0.28 | 0.01 | 1782 |
| stroke 249 | 61 % → 0 % | 307.6 px | 0.28 | 0.01 | 1498 |
| stroke 250 | 73 % → 0 % | 239.5 px | 0.00 | 0.00 | 1388 |
| stroke 251 | 78 % → 0 % | 246.7 px | 0.00 | 0.00 | 1421 |
| stroke 252 | 62 % → 0 % | 256.9 px | 0.00 | 0.00 | 1460 |
| stroke 253 | 75 % → 0 % | 607.4 px | 0.00 | 0.00 | 401 |
| stroke 254 | 69 % → 0 % | 646.1 px | 0.00 | 0.00 | 299 |
| stroke 255 | 66 % → 0 % | 818.4 px | 0.00 | 0.00 | 239 |
| stroke 256 | 74 % → 0 % | 623.1 px | 0.00 | 0.00 | 338 |
| stroke 257 | 86 % → 0 % | 334.2 px | 0.00 | 0.00 | 1300 |
| stroke 258 | 88 % → 0 % | 343.2 px | 0.00 | 0.00 | 1210 |
| stroke 259 | 95 % → 0 % | 519.0 px | 0.00 | 0.00 | 1768 |
| stroke 260 | 93 % → 0 % | 324.5 px | 0.00 | 0.00 | 3069 |
| stroke 261 | 93 % → 0 % | 408.3 px | 0.00 | 0.00 | 1916 |
| stroke 262 | 95 % → 0 % | 459.2 px | 0.00 | 0.00 | 2031 |
| stroke 263 | 94 % → 0 % | 1373.9 px | 0.00 | 0.00 | 2005 |
| stroke 264 | 81 % → 0 % | 405.2 px | 0.00 | 0.00 | 3110 |
| stroke 265 | 95 % → 0 % | 379.9 px | 0.00 | 0.00 | 3266 |
| stroke 266 | 68 % → 0 % | 321.6 px | 0.00 | 0.00 | 2175 |
| stroke 267 | 63 % → 0 % | 2666.9 px | 0.00 | 0.00 | 49 |
| stroke 268 | 1 % → 1 % | 18.9 px | 0.28 | 1.23 | 14 |

## Refs v3 · #45 Pastel pepper — own sheet
own sheet 800 × 800 · Pastel 1.00 · 64 px · 277.3 s

![Refs v3 · #45 Pastel pepper — own sheet](Refs-v3-45-Pastel-pepper-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 3 % → 66 % | 54.7 px | 0.63 | 18.83 | 355 |
| stroke 2 | 7 % → 75 % | 45.9 px | 0.67 | 10.99 | 956 |
| stroke 3 | 8 % → 74 % | 54.1 px | 0.70 | 9.18 | 1133 |
| stroke 4 | 16 % → 83 % | 103.2 px | 0.68 | 5.01 | 1332 |
| stroke 5 | 18 % → 74 % | 129.1 px | 0.65 | 4.17 | 911 |
| stroke 6 | 33 % → 88 % | 330.4 px | 0.66 | 2.66 | 502 |
| stroke 7 | 22 % → 63 % | 261.1 px | 0.68 | 2.84 | 459 |
| stroke 8 | 24 % → 67 % | 224.3 px | 0.63 | 2.76 | 559 |
| stroke 9 | 22 % → 61 % | 333.4 px | 0.62 | 2.79 | 307 |
| stroke 10 | 22 % → 76 % | 289.6 px | 0.69 | 3.44 | 692 |
| stroke 11 | 29 % → 79 % | 322.6 px | 0.65 | 2.76 | 520 |
| stroke 12 | 34 % → 83 % | 298.1 px | 0.68 | 2.43 | 903 |
| stroke 13 | 22 % → 76 % | 133.6 px | 0.68 | 3.50 | 2435 |
| stroke 14 | 22 % → 74 % | 112.7 px | 0.67 | 3.36 | 2236 |
| stroke 15 | 40 % → 90 % | 536.9 px | 0.67 | 2.26 | 1026 |
| stroke 16 | 33 % → 87 % | 299.8 px | 0.69 | 2.68 | 798 |
| stroke 17 | 21 % → 76 % | 112.3 px | 0.70 | 3.55 | 2227 |
| stroke 18 | 23 % → 73 % | 140.9 px | 0.70 | 3.19 | 1759 |
| stroke 19 | 8 % → 94 % | 48.4 px | 0.60 | 11.45 | 1159 |
| stroke 20 | 16 % → 94 % | 112.5 px | 0.65 | 5.95 | 1088 |
| stroke 21 | 21 % → 99 % | 139.5 px | 0.62 | 4.64 | 1039 |
| stroke 22 | 16 % → 95 % | 114.2 px | 0.70 | 5.81 | 629 |
| stroke 23 | 19 % → 77 % | 123.4 px | 0.60 | 4.04 | 708 |
| stroke 24 | 14 % → 73 % | 69.0 px | 0.56 | 5.24 | 814 |
| stroke 25 | 31 % → 88 % | 199.5 px | 0.58 | 2.88 | 1082 |
| stroke 26 | 34 % → 74 % | 280.3 px | 0.56 | 2.17 | 1102 |
| stroke 27 | 45 % → 94 % | 298.4 px | 0.55 | 2.10 | 708 |
| stroke 28 | 22 % → 69 % | 146.4 px | 0.60 | 3.15 | 607 |
| stroke 29 | 19 % → 100 % | 306.6 px | 0.73 | 5.14 | 267 |
| stroke 30 | 22 % → 95 % | 172.7 px | 0.71 | 4.28 | 928 |
| stroke 31 | 37 % → 100 % | 232.5 px | 0.63 | 2.69 | 1259 |
| stroke 32 | 50 % → 94 % | 313.5 px | 0.59 | 1.87 | 1020 |
| stroke 33 | 30 % → 77 % | 284.3 px | 0.61 | 2.54 | 496 |
| stroke 34 | 42 % → 90 % | 410.9 px | 0.62 | 2.15 | 227 |
| stroke 35 | 49 % → 99 % | 680.6 px | 0.62 | 2.04 | 326 |
| stroke 36 | 32 % → 62 % | 393.6 px | 0.57 | 1.97 | 731 |
| stroke 37 | 44 % → 90 % | 399.8 px | 0.61 | 2.06 | 596 |
| stroke 38 | 44 % → 91 % | 495.8 px | 0.63 | 2.08 | 271 |
| stroke 39 | 59 % → 85 % | 756.5 px | 0.53 | 1.45 | 301 |
| stroke 40 | 57 % → 100 % | 680.0 px | 0.58 | 1.74 | 620 |
| stroke 41 | 58 % → 93 % | 529.6 px | 0.56 | 1.61 | 595 |
| stroke 42 | 58 % → 100 % | 841.2 px | 0.59 | 1.71 | 433 |
| stroke 43 | 52 % → 75 % | 585.8 px | 0.54 | 1.43 | 521 |
| stroke 44 | 39 % → 68 % | 247.6 px | 0.60 | 1.75 | 497 |
| stroke 45 | 59 % → 99 % | 916.9 px | 0.59 | 1.70 | 251 |
| stroke 46 | 61 % → 93 % | 549.1 px | 0.58 | 1.52 | 570 |
| stroke 47 | 61 % → 69 % | 470.6 px | 0.50 | 1.13 | 343 |
| stroke 48 | 36 % → 71 % | 517.2 px | 0.61 | 1.95 | 220 |
| stroke 49 | 33 % → 96 % | 476.6 px | 0.65 | 2.93 | 273 |
| stroke 50 | 57 % → 99 % | 830.6 px | 0.60 | 1.76 | 457 |
| stroke 51 | 49 % → 75 % | 207.9 px | 0.58 | 1.53 | 1898 |
| stroke 52 | 55 % → 80 % | 346.1 px | 0.57 | 1.45 | 2001 |
| stroke 53 | 46 % → 83 % | 241.2 px | 0.61 | 1.81 | 2292 |
| stroke 54 | 41 % → 75 % | 138.7 px | 0.61 | 1.85 | 2280 |
| stroke 55 | 46 % → 80 % | 227.5 px | 0.61 | 1.76 | 2312 |
| stroke 56 | 39 % → 94 % | 203.2 px | 0.64 | 2.43 | 2091 |
| stroke 57 | 60 % → 99 % | 343.6 px | 0.60 | 1.66 | 1834 |
| stroke 58 | 55 % → 94 % | 240.0 px | 0.62 | 1.70 | 2209 |
| stroke 59 | 55 % → 91 % | 383.9 px | 0.62 | 1.66 | 1022 |
| stroke 60 | 24 % → 89 % | 269.9 px | 0.66 | 3.75 | 566 |
| stroke 61 | 25 % → 91 % | 318.8 px | 0.67 | 3.66 | 327 |
| stroke 62 | 37 % → 98 % | 283.6 px | 0.68 | 2.67 | 197 |
| stroke 63 | 8 % → 56 % | 63.9 px | 0.63 | 6.67 | 195 |
| stroke 64 | 17 % → 50 % | 129.4 px | 0.59 | 2.96 | 244 |
| stroke 65 | 21 % → 70 % | 166.4 px | 0.65 | 3.38 | 375 |
| stroke 66 | 22 % → 59 % | 247.3 px | 0.61 | 2.68 | 215 |
| stroke 67 | 30 % → 83 % | 583.3 px | 0.66 | 2.79 | 101 |
| stroke 68 | 19 % → 61 % | 349.5 px | 0.66 | 3.29 | 84 |
| stroke 69 | 21 % → 52 % | 325.2 px | 0.63 | 2.48 | 250 |
| stroke 70 | 27 % → 57 % | 463.7 px | 0.61 | 2.08 | 183 |
| stroke 71 | 27 % → 53 % | 434.2 px | 0.61 | 1.95 | 221 |
| stroke 72 | 27 % → 67 % | 230.8 px | 0.65 | 2.49 | 436 |
| stroke 73 | 31 % → 83 % | 627.5 px | 0.67 | 2.70 | 159 |
| stroke 74 | 35 % → 55 % | 285.9 px | 0.59 | 1.56 | 175 |
| stroke 75 | 36 % → 65 % | 572.4 px | 0.63 | 1.78 | 105 |
| stroke 76 | 32 % → 66 % | 193.9 px | 0.64 | 2.05 | 714 |
| stroke 77 | 37 % → 57 % | 181.0 px | 0.60 | 1.53 | 1386 |
| stroke 78 | 29 % → 50 % | 138.4 px | 0.63 | 1.72 | 1129 |
| stroke 79 | 30 % → 66 % | 192.9 px | 0.66 | 2.22 | 658 |
| stroke 80 | 36 % → 80 % | 244.7 px | 0.66 | 2.21 | 637 |
| stroke 81 | 37 % → 70 % | 242.8 px | 0.64 | 1.89 | 995 |
| stroke 82 | 41 % → 68 % | 335.4 px | 0.64 | 1.67 | 698 |
| stroke 83 | 42 % → 67 % | 152.8 px | 0.64 | 1.61 | 2534 |
| stroke 84 | 43 % → 65 % | 539.9 px | 0.61 | 1.50 | 367 |
| stroke 85 | 55 % → 78 % | 379.9 px | 0.64 | 1.42 | 1122 |
| stroke 86 | 60 % → 89 % | 564.1 px | 0.65 | 1.48 | 1129 |
| stroke 87 | 70 % → 92 % | 599.8 px | 0.61 | 1.30 | 662 |
| stroke 88 | 65 % → 78 % | 565.2 px | 0.61 | 1.19 | 748 |
| stroke 89 | 73 % → 89 % | 734.9 px | 0.64 | 1.21 | 818 |
| stroke 90 | 75 % → 80 % | 1066.7 px | 0.65 | 1.07 | 306 |
| stroke 91 | 80 % → 89 % | 1249.0 px | 0.64 | 1.11 | 295 |
| stroke 92 | 80 % → 87 % | 1049.0 px | 0.64 | 1.09 | 529 |
| stroke 93 | 68 % → 76 % | 334.9 px | 0.61 | 1.11 | 1942 |
| stroke 94 | 72 % → 80 % | 385.1 px | 0.63 | 1.11 | 2382 |
| stroke 95 | 74 % → 89 % | 556.6 px | 0.64 | 1.21 | 1397 |
| stroke 96 | 38 % → 55 % | 316.4 px | 0.64 | 1.46 | 611 |
| stroke 97 | 34 % → 45 % | 526.3 px | 0.62 | 1.33 | 255 |
| stroke 98 | 48 % → 80 % | 252.0 px | 0.65 | 1.69 | 728 |
| stroke 99 | 48 % → 90 % | 313.6 px | 0.67 | 1.89 | 1185 |
| stroke 100 | 49 % → 72 % | 251.2 px | 0.66 | 1.45 | 676 |
| stroke 101 | 68 % → 88 % | 524.5 px | 0.68 | 1.30 | 612 |
| stroke 102 | 60 % → 94 % | 385.3 px | 0.68 | 1.57 | 1849 |
| stroke 103 | 72 % → 93 % | 995.0 px | 0.69 | 1.29 | 302 |
| stroke 104 | 58 % → 87 % | 678.7 px | 0.66 | 1.50 | 359 |
| stroke 105 | 69 % → 97 % | 723.8 px | 0.66 | 1.41 | 512 |
| stroke 106 | 65 % → 100 % | 869.1 px | 0.71 | 1.55 | 590 |
| stroke 107 | 68 % → 97 % | 568.8 px | 0.69 | 1.44 | 934 |
| stroke 108 | 60 % → 84 % | 516.5 px | 0.67 | 1.41 | 931 |
| stroke 109 | 72 % → 90 % | 789.6 px | 0.69 | 1.25 | 1089 |
| stroke 110 | 60 % → 100 % | 812.7 px | 0.72 | 1.66 | 538 |
| stroke 111 | 68 % → 91 % | 1054.2 px | 0.65 | 1.32 | 514 |
| stroke 112 | 63 % → 88 % | 274.9 px | 0.69 | 1.39 | 2727 |
| stroke 113 | 68 % → 96 % | 423.4 px | 0.67 | 1.41 | 2459 |
| stroke 114 | 59 % → 85 % | 285.8 px | 0.67 | 1.45 | 3366 |
| stroke 115 | 66 % → 89 % | 413.9 px | 0.67 | 1.35 | 2371 |
| stroke 116 | 61 % → 75 % | 261.3 px | 0.69 | 1.23 | 2032 |
| stroke 117 | 67 % → 69 % | 1438.9 px | 0.68 | 1.03 | 169 |
| stroke 118 | 74 % → 78 % | 306.0 px | 0.64 | 1.05 | 1082 |
| stroke 119 | 81 % → 83 % | 544.3 px | 0.67 | 1.02 | 923 |
| stroke 120 | 81 % → 82 % | 282.5 px | 0.66 | 1.02 | 1845 |
| stroke 121 | 73 % → 99 % | 487.9 px | 0.68 | 1.35 | 823 |
| stroke 122 | 81 % → 99 % | 601.7 px | 0.67 | 1.23 | 715 |
| stroke 123 | 89 % → 99 % | 718.3 px | 0.67 | 1.11 | 824 |
| stroke 124 | 85 % → 99 % | 665.8 px | 0.65 | 1.16 | 513 |
| stroke 125 | 87 % → 99 % | 902.1 px | 0.61 | 1.14 | 479 |
| stroke 126 | 92 % → 99 % | 1389.6 px | 0.63 | 1.07 | 324 |
| stroke 127 | 89 % → 100 % | 665.9 px | 0.67 | 1.12 | 721 |
| stroke 128 | 87 % → 94 % | 1243.0 px | 0.68 | 1.08 | 288 |
| stroke 129 | 93 % → 99 % | 1009.4 px | 0.68 | 1.06 | 540 |
| stroke 130 | 90 % → 99 % | 1400.7 px | 0.66 | 1.10 | 392 |
| stroke 131 | 95 % → 100 % | 1076.0 px | 0.72 | 1.05 | 603 |
| stroke 132 | 95 % → 99 % | 1574.5 px | 0.62 | 1.05 | 435 |
| stroke 133 | 92 % → 96 % | 539.1 px | 0.63 | 1.04 | 2269 |
| stroke 134 | 94 % → 99 % | 495.7 px | 0.67 | 1.05 | 3598 |
| stroke 135 | 92 % → 96 % | 558.6 px | 0.68 | 1.05 | 8333 |
| stroke 136 | 90 % → 93 % | 4610.7 px | 0.67 | 1.03 | 323 |
| stroke 137 | 64 % → 81 % | 328.4 px | 0.60 | 1.27 | 2580 |
| stroke 138 | 74 % → 82 % | 433.7 px | 0.59 | 1.11 | 2492 |
| stroke 139 | 69 % → 80 % | 521.5 px | 0.60 | 1.16 | 1447 |
| stroke 140 | 61 % → 69 % | 451.8 px | 0.62 | 1.14 | 1132 |
| stroke 141 | 77 % → 82 % | 474.7 px | 0.64 | 1.06 | 1198 |
| stroke 142 | 75 % → 79 % | 314.2 px | 0.61 | 1.05 | 2496 |
| stroke 143 | 78 % → 81 % | 404.4 px | 0.59 | 1.04 | 2948 |
| stroke 144 | 54 % → 57 % | 696.6 px | 0.62 | 1.05 | 143 |
| stroke 145 | 66 % → 69 % | 761.6 px | 0.62 | 1.04 | 196 |
| stroke 146 | 57 % → 62 % | 450.4 px | 0.63 | 1.09 | 428 |
| stroke 147 | 51 % → 52 % | 1140.0 px | 0.60 | 1.02 | 70 |
| stroke 148 | 54 % → 54 % | 850.5 px | 0.61 | 1.01 | 160 |
| stroke 149 | 69 % → 69 % | 1332.6 px | 0.60 | 1.00 | 62 |
| stroke 150 | 57 % → 59 % | 334.1 px | 0.62 | 1.02 | 864 |
| stroke 151 | 59 % → 59 % | 1098.1 px | 0.61 | 1.00 | 182 |
| stroke 152 | 70 % → 70 % | 469.6 px | 0.62 | 1.00 | 492 |
| stroke 153 | 92 % → 98 % | 1562.9 px | 0.67 | 1.07 | 209 |
| stroke 154 | 84 % → 90 % | 1038.4 px | 0.68 | 1.07 | 434 |
| stroke 155 | 95 % → 100 % | 1171.5 px | 0.58 | 1.05 | 506 |
| stroke 156 | 98 % → 100 % | 1297.1 px | 0.72 | 1.02 | 533 |
| stroke 157 | 93 % → 94 % | 793.8 px | 0.64 | 1.01 | 751 |
| stroke 158 | 92 % → 96 % | 1266.4 px | 0.67 | 1.04 | 234 |
| stroke 159 | 96 % → 98 % | 1182.0 px | 0.64 | 1.02 | 510 |
| stroke 160 | 94 % → 95 % | 852.2 px | 0.71 | 1.02 | 782 |
| stroke 161 | 96 % → 100 % | 1394.4 px | 0.69 | 1.04 | 362 |
| stroke 162 | 86 % → 90 % | 1541.8 px | 0.66 | 1.05 | 300 |
| stroke 163 | 79 % → 82 % | 1535.4 px | 0.66 | 1.05 | 275 |
| stroke 164 | 95 % → 98 % | 1705.0 px | 0.67 | 1.03 | 277 |
| stroke 165 | 91 % → 93 % | 1272.6 px | 0.67 | 1.02 | 261 |
| stroke 166 | 91 % → 93 % | 1029.8 px | 0.65 | 1.02 | 386 |
| stroke 167 | 83 % → 85 % | 1079.2 px | 0.66 | 1.02 | 328 |
| stroke 168 | 92 % → 93 % | 2180.4 px | 0.66 | 1.02 | 128 |
| stroke 169 | 92 % → 94 % | 904.4 px | 0.61 | 1.01 | 576 |
| stroke 170 | 99 % → 99 % | 2605.3 px | 0.61 | 1.00 | 164 |
| stroke 171 | 95 % → 96 % | 1471.7 px | 0.67 | 1.01 | 312 |
| stroke 172 | 97 % → 100 % | 1993.4 px | 0.59 | 1.02 | 282 |
| stroke 173 | 93 % → 93 % | 1972.2 px | 0.66 | 1.01 | 299 |
| stroke 174 | 92 % → 93 % | 1346.8 px | 0.58 | 1.01 | 262 |
| stroke 175 | 98 % → 98 % | 1744.6 px | 0.68 | 1.01 | 247 |
| stroke 176 | 99 % → 100 % | 1431.4 px | 0.72 | 1.01 | 571 |
| stroke 177 | 93 % → 93 % | 1162.3 px | 0.62 | 1.00 | 400 |
| stroke 178 | 96 % → 96 % | 1461.7 px | 0.68 | 1.00 | 207 |
| stroke 179 | 85 % → 85 % | 1642.5 px | 0.67 | 1.00 | 145 |
| stroke 180 | 93 % → 93 % | 2143.2 px | 0.62 | 1.00 | 141 |
| stroke 181 | 81 % → 82 % | 2577.5 px | 0.66 | 1.00 | 68 |
| stroke 182 | 98 % → 99 % | 2277.7 px | 0.61 | 1.01 | 119 |
| stroke 183 | 96 % → 97 % | 1837.8 px | 0.67 | 1.00 | 148 |
| stroke 184 | 95 % → 96 % | 1842.8 px | 0.67 | 1.00 | 133 |
| stroke 185 | 99 % → 100 % | 1773.2 px | 0.70 | 1.00 | 193 |
| stroke 186 | 100 % → 100 % | 2643.2 px | 0.72 | 1.00 | 115 |
| stroke 187 | 92 % → 92 % | 1930.3 px | 0.66 | 1.00 | 142 |
| stroke 188 | 99 % → 100 % | 2286.5 px | 0.59 | 1.01 | 115 |
| stroke 189 | 92 % → 92 % | 2927.2 px | 0.66 | 1.00 | 84 |
| stroke 190 | 86 % → 86 % | 1828.6 px | 0.67 | 1.00 | 157 |
| stroke 191 | 93 % → 93 % | 2962.5 px | 0.66 | 1.00 | 82 |
| stroke 192 | 92 % → 92 % | 2443.8 px | 0.65 | 1.00 | 93 |
| stroke 193 | 97 % → 97 % | 2613.2 px | 0.65 | 1.00 | 119 |
| stroke 194 | 92 % → 92 % | 2575.2 px | 0.59 | 1.00 | 92 |
| stroke 195 | 91 % → 91 % | 2443.3 px | 0.58 | 1.00 | 73 |
| stroke 196 | 100 % → 100 % | 2607.9 px | 0.70 | 1.00 | 108 |
| stroke 197 | 100 % → 100 % | 2665.3 px | 0.74 | 1.00 | 120 |
| stroke 198 | 81 % → 81 % | 2564.0 px | 0.66 | 1.00 | 85 |
| stroke 199 | 98 % → 98 % | 911.7 px | 0.67 | 1.00 | 555 |
| stroke 200 | 94 % → 95 % | 659.2 px | 0.67 | 1.00 | 607 |
| stroke 201 | 88 % → 88 % | 695.0 px | 0.67 | 1.00 | 601 |
| stroke 202 | 83 % → 83 % | 589.0 px | 0.67 | 1.00 | 611 |
| stroke 203 | 88 % → 88 % | 796.9 px | 0.67 | 1.00 | 631 |
| stroke 204 | 98 % → 98 % | 1240.8 px | 0.67 | 1.00 | 263 |
| stroke 205 | 93 % → 94 % | 681.8 px | 0.62 | 1.00 | 577 |
| stroke 206 | 96 % → 99 % | 702.3 px | 0.59 | 1.02 | 535 |
| stroke 207 | 94 % → 94 % | 794.5 px | 0.63 | 1.00 | 755 |
| stroke 208 | 91 % → 91 % | 4727.7 px | 0.65 | 1.00 | 64 |
| stroke 209 | 100 % → 100 % | 1747.5 px | 0.70 | 1.00 | 237 |
| stroke 210 | 93 % → 93 % | 2116.6 px | 0.68 | 1.00 | 112 |
| stroke 211 | 83 % → 83 % | 1274.7 px | 0.60 | 1.00 | 146 |
| stroke 212 | 86 % → 86 % | 756.8 px | 0.61 | 1.01 | 446 |
| stroke 213 | 99 % → 99 % | 2605.6 px | 0.61 | 1.00 | 101 |
| stroke 214 | 93 % → 93 % | 1281.9 px | 0.61 | 1.00 | 195 |
| stroke 215 | 83 % → 83 % | 775.7 px | 0.59 | 1.00 | 319 |
| stroke 216 | 95 % → 95 % | 827.6 px | 0.61 | 1.00 | 498 |
| stroke 217 | 89 % → 92 % | 743.2 px | 0.57 | 1.03 | 315 |
| stroke 218 | 58 % → 60 % | 1354.6 px | 0.58 | 1.04 | 67 |
| stroke 219 | 87 % → 89 % | 1011.8 px | 0.57 | 1.02 | 269 |
| stroke 220 | 70 % → 71 % | 1084.4 px | 0.56 | 1.02 | 140 |
| stroke 221 | 74 % → 75 % | 1567.5 px | 0.56 | 1.02 | 132 |
| stroke 222 | 97 % → 97 % | 1588.4 px | 0.58 | 1.01 | 129 |
| stroke 223 | 81 % → 82 % | 1056.0 px | 0.58 | 1.01 | 229 |
| stroke 224 | 89 % → 89 % | 1196.4 px | 0.61 | 1.01 | 167 |
| stroke 225 | 88 % → 88 % | 1099.8 px | 0.61 | 1.01 | 246 |
| stroke 226 | 57 % → 58 % | 1507.0 px | 0.58 | 1.01 | 68 |
| stroke 227 | 85 % → 86 % | 2267.4 px | 0.62 | 1.01 | 81 |
| stroke 228 | 97 % → 97 % | 1126.7 px | 0.57 | 1.00 | 290 |
| stroke 229 | 93 % → 93 % | 1661.2 px | 0.60 | 1.00 | 146 |
| stroke 230 | 88 % → 88 % | 2131.8 px | 0.62 | 1.00 | 137 |
| stroke 231 | 64 % → 64 % | 1380.8 px | 0.58 | 1.00 | 118 |
| stroke 232 | 93 % → 93 % | 2426.5 px | 0.60 | 1.00 | 121 |
| stroke 233 | 70 % → 70 % | 1484.7 px | 0.58 | 1.00 | 125 |
| stroke 234 | 90 % → 90 % | 2319.3 px | 0.61 | 1.00 | 77 |
| stroke 235 | 92 % → 92 % | 2176.2 px | 0.61 | 1.00 | 107 |
| stroke 236 | 89 % → 89 % | 2806.3 px | 0.62 | 1.00 | 95 |
| stroke 237 | 99 % → 99 % | 2578.1 px | 0.58 | 1.00 | 97 |
| stroke 238 | 87 % → 87 % | 681.4 px | 0.62 | 1.00 | 650 |
| stroke 239 | 88 % → 88 % | 1362.1 px | 0.62 | 1.00 | 331 |
| stroke 240 | 71 % → 71 % | 599.2 px | 0.56 | 1.00 | 612 |
| stroke 241 | 92 % → 92 % | 686.7 px | 0.57 | 1.00 | 632 |
| stroke 242 | 94 % → 94 % | 769.4 px | 0.58 | 1.00 | 634 |
| stroke 243 | 76 % → 76 % | 696.4 px | 0.56 | 1.00 | 913 |
| stroke 244 | 65 % → 65 % | 1849.4 px | 0.56 | 1.00 | 115 |
| stroke 245 | 59 % → 61 % | 760.0 px | 0.68 | 1.04 | 230 |
| stroke 246 | 72 % → 74 % | 697.7 px | 0.68 | 1.03 | 336 |
| stroke 247 | 73 % → 74 % | 575.7 px | 0.67 | 1.02 | 419 |
| stroke 248 | 87 % → 87 % | 899.6 px | 0.68 | 1.01 | 375 |
| stroke 249 | 58 % → 59 % | 693.6 px | 0.65 | 1.01 | 178 |
| stroke 250 | 88 % → 88 % | 1000.1 px | 0.68 | 1.01 | 260 |
| stroke 251 | 66 % → 66 % | 1103.0 px | 0.65 | 1.00 | 106 |
| stroke 252 | 88 % → 88 % | 1037.4 px | 0.69 | 1.00 | 327 |
| stroke 253 | 91 % → 91 % | 1935.2 px | 0.68 | 1.00 | 129 |
| stroke 254 | 90 % → 90 % | 1866.9 px | 0.68 | 1.00 | 140 |
| stroke 255 | 84 % → 84 % | 1341.9 px | 0.69 | 1.00 | 165 |
| stroke 256 | 74 % → 74 % | 1520.0 px | 0.67 | 1.00 | 99 |
| stroke 257 | 80 % → 80 % | 2200.6 px | 0.68 | 1.00 | 87 |
| stroke 258 | 68 % → 68 % | 1384.5 px | 0.64 | 1.00 | 101 |
| stroke 259 | 82 % → 82 % | 1676.3 px | 0.67 | 1.00 | 94 |
| stroke 260 | 79 % → 79 % | 1953.3 px | 0.64 | 1.00 | 57 |
| stroke 261 | 74 % → 74 % | 771.8 px | 0.61 | 1.00 | 201 |
| stroke 262 | 79 % → 79 % | 629.4 px | 0.67 | 1.00 | 1106 |
| stroke 263 | 88 % → 88 % | 1150.1 px | 0.68 | 1.00 | 139 |
| stroke 264 | 99 % → 99 % | 1256.4 px | 0.63 | 1.00 | 194 |

Numbers say: wet paint spreads well beyond the stroke.

## Refs v3 · #46 Ink lips on wet paper — own sheet
own sheet 800 × 1047 · Watercolour 1.00 + water 65 % · 56 px · 104.4 s

![Refs v3 · #46 Ink lips on wet paper — own sheet](Refs-v3-46-Ink-lips-on-wet-paper-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 14 % → 17 % | 59.9 px | 0.62 | 1.26 | 1219 |
| stroke 2 | 13 % → 15 % | 60.3 px | 0.57 | 1.15 | 1480 |

## Refs v3 · #47 Pink knife slabs — own sheet
own sheet 800 × 1190 · Impasto 1.00 · 112 px · 216.1 s

![Refs v3 · #47 Pink knife slabs — own sheet](Refs-v3-47-Pink-knife-slabs-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 11 % → 0 % | 109.4 px | 0.00 | 0.00 | 243 |
| stroke 2 | 22 % → 0 % | 119.4 px | 0.00 | 0.00 | 479 |
| stroke 3 | 28 % → 0 % | 115.4 px | 0.07 | 0.01 | 822 |
| stroke 4 | 35 % → 0 % | 157.5 px | 0.07 | 0.01 | 930 |
| stroke 5 | 38 % → 0 % | 273.7 px | 0.00 | 0.00 | 526 |
| stroke 6 | 39 % → 0 % | 426.2 px | 0.07 | 0.01 | 228 |
| stroke 7 | 45 % → 0 % | 319.3 px | 0.00 | 0.00 | 587 |
| stroke 8 | 48 % → 0 % | 488.4 px | 0.07 | 0.01 | 247 |
| stroke 9 | 47 % → 0 % | 678.2 px | 0.00 | 0.00 | 148 |
| stroke 10 | 48 % → 0 % | 600.8 px | 0.00 | 0.00 | 385 |
| stroke 11 | 48 % → 0 % | 502.2 px | 0.07 | 0.01 | 246 |
| stroke 12 | 47 % → 0 % | 380.6 px | 0.00 | 0.00 | 614 |
| stroke 13 | 44 % → 0 % | 589.5 px | 0.07 | 0.01 | 279 |
| stroke 14 | 49 % → 0 % | 777.7 px | 0.00 | 0.00 | 185 |
| stroke 15 | 40 % → 0 % | 503.1 px | 0.07 | 0.01 | 274 |
| stroke 16 | 41 % → 0 % | 348.2 px | 0.06 | 0.01 | 427 |
| stroke 17 | 35 % → 1 % | 567.1 px | 0.07 | 0.02 | 170 |
| stroke 18 | 42 % → 0 % | 354.8 px | 0.07 | 0.00 | 457 |
| stroke 19 | 33 % → 1 % | 382.3 px | 0.06 | 0.03 | 230 |
| stroke 20 | 42 % → 0 % | 294.7 px | 0.06 | 0.01 | 735 |
| stroke 21 | 39 % → 1 % | 374.3 px | 0.06 | 0.02 | 356 |
| stroke 22 | 43 % → 0 % | 296.2 px | 0.06 | 0.01 | 882 |
| stroke 23 | 44 % → 1 % | 390.4 px | 0.06 | 0.02 | 402 |
| stroke 24 | 48 % → 0 % | 319.7 px | 0.06 | 0.01 | 830 |
| stroke 25 | 44 % → 1 % | 589.6 px | 0.06 | 0.01 | 251 |
| stroke 26 | 50 % → 0 % | 383.2 px | 0.06 | 0.01 | 698 |
| stroke 27 | 46 % → 1 % | 610.4 px | 0.06 | 0.01 | 199 |
| stroke 28 | 51 % → 0 % | 716.5 px | 0.00 | 0.00 | 341 |
| stroke 29 | 52 % → 0 % | 426.3 px | 0.06 | 0.01 | 618 |
| stroke 30 | 48 % → 0 % | 1035.8 px | 0.00 | 0.00 | 100 |
| stroke 31 | 51 % → 0 % | 441.0 px | 0.06 | 0.01 | 470 |
| stroke 32 | 45 % → 0 % | 587.1 px | 0.00 | 0.00 | 153 |
| stroke 33 | 50 % → 0 % | 418.2 px | 0.06 | 0.01 | 506 |
| stroke 34 | 40 % → 0 % | 488.7 px | 0.00 | 0.00 | 200 |
| stroke 35 | 46 % → 0 % | 353.0 px | 0.06 | 0.01 | 453 |
| stroke 36 | 35 % → 0 % | 439.2 px | 0.00 | 0.00 | 199 |
| stroke 37 | 43 % → 0 % | 353.6 px | 0.06 | 0.01 | 403 |
| stroke 38 | 34 % → 0 % | 352.2 px | 0.00 | 0.00 | 261 |
| stroke 39 | 39 % → 0 % | 320.4 px | 0.04 | 0.00 | 433 |
| stroke 40 | 31 % → 0 % | 369.3 px | 0.00 | 0.00 | 264 |
| stroke 41 | 36 % → 0 % | 304.9 px | 0.00 | 0.00 | 363 |
| stroke 42 | 38 % → 0 % | 355.9 px | 0.00 | 0.00 | 284 |
| stroke 43 | 45 % → 0 % | 451.6 px | 0.00 | 0.00 | 261 |
| stroke 44 | 48 % → 0 % | 334.4 px | 0.00 | 0.00 | 567 |
| stroke 45 | 55 % → 0 % | 609.4 px | 0.00 | 0.00 | 222 |
| stroke 46 | 51 % → 0 % | 406.5 px | 0.00 | 0.00 | 548 |
| stroke 47 | 55 % → 0 % | 787.7 px | 0.00 | 0.00 | 105 |
| stroke 48 | 67 % → 0 % | 462.0 px | 0.00 | 0.00 | 1177 |
| stroke 49 | 83 % → 0 % | 485.0 px | 0.00 | 0.00 | 1245 |
| stroke 50 | 68 % → 0 % | 421.9 px | 0.00 | 0.00 | 1117 |
| stroke 51 | 71 % → 0 % | 405.7 px | 0.07 | 0.00 | 1051 |
| stroke 52 | 76 % → 1 % | 399.5 px | 0.06 | 0.01 | 908 |
| stroke 53 | 78 % → 1 % | 513.7 px | 0.06 | 0.01 | 1394 |
| stroke 54 | 77 % → 0 % | 553.1 px | 0.06 | 0.01 | 1376 |
| stroke 55 | 79 % → 0 % | 675.8 px | 0.07 | 0.00 | 1241 |
| stroke 56 | 86 % → 0 % | 588.3 px | 0.00 | 0.00 | 1503 |
| stroke 57 | 84 % → 0 % | 886.2 px | 0.06 | 0.00 | 1166 |
| stroke 58 | 77 % → 0 % | 630.4 px | 0.06 | 0.00 | 1863 |
| stroke 59 | 67 % → 0 % | 398.9 px | 0.06 | 0.00 | 4463 |
| stroke 60 | 76 % → 0 % | 828.4 px | 0.06 | 0.00 | 5969 |
| stroke 61 | 82 % → 0 % | 593.9 px | 0.00 | 0.00 | 2867 |
| stroke 62 | 70 % → 0 % | 551.9 px | 0.06 | 0.00 | 1504 |
| stroke 63 | 61 % → 0 % | 1830.8 px | 0.00 | 0.00 | 217 |
| stroke 64 | 14 % → 0 % | 37.6 px | 0.00 | 0.00 | 363 |
| stroke 65 | 19 % → 0 % | 63.5 px | 0.00 | 0.00 | 700 |
| stroke 66 | 22 % → 0 % | 243.4 px | 0.00 | 0.00 | 129 |
| stroke 67 | 24 % → 0 % | 208.3 px | 0.00 | 0.00 | 308 |
| stroke 68 | 25 % → 0 % | 404.2 px | 0.00 | 0.00 | 96 |
| stroke 69 | 25 % → 0 % | 495.0 px | 0.00 | 0.00 | 168 |
| stroke 70 | 24 % → 0 % | 123.1 px | 0.00 | 0.00 | 300 |
| stroke 71 | 29 % → 0 % | 152.5 px | 0.00 | 0.00 | 257 |
| stroke 72 | 25 % → 0 % | 139.9 px | 0.00 | 0.00 | 599 |
| stroke 73 | 30 % → 0 % | 201.6 px | 0.00 | 0.00 | 666 |
| stroke 74 | 30 % → 0 % | 257.7 px | 0.00 | 0.00 | 483 |
| stroke 75 | 23 % → 0 % | 221.4 px | 0.00 | 0.00 | 220 |
| stroke 76 | 25 % → 0 % | 418.2 px | 0.00 | 0.00 | 72 |
| stroke 77 | 20 % → 0 % | 784.4 px | 0.07 | 0.01 | 102 |
| stroke 78 | 16 % → 0 % | 494.3 px | 0.07 | 0.02 | 93 |
| stroke 79 | 21 % → 0 % | 343.1 px | 0.07 | 0.01 | 341 |
| stroke 80 | 6 % → 0 % | 248.7 px | 0.07 | 0.04 | 70 |
| stroke 81 | 7 % → 0 % | 159.1 px | 0.07 | 0.03 | 169 |
| stroke 82 | 9 % → 0 % | 127.1 px | 0.07 | 0.02 | 223 |
| stroke 83 | 11 % → 0 % | 115.8 px | 0.07 | 0.02 | 763 |
| stroke 84 | 17 % → 0 % | 355.9 px | 0.07 | 0.02 | 154 |
| stroke 85 | 18 % → 1 % | 376.6 px | 0.06 | 0.03 | 90 |
| stroke 86 | 19 % → 0 % | 878.8 px | 0.06 | 0.02 | 33 |
| stroke 87 | 15 % → 0 % | 187.8 px | 0.06 | 0.02 | 414 |
| stroke 88 | 17 % → 1 % | 191.7 px | 0.06 | 0.03 | 483 |
| stroke 89 | 22 % → 0 % | 6579.9 px | 0.06 | 0.02 | 9 |
| stroke 90 | 18 % → 0 % | 826.9 px | 0.00 | 0.00 | 72 |
| stroke 91 | 23 % → 0 % | 599.6 px | 0.00 | 0.00 | 101 |
| stroke 92 | 4 % → 0 % | 107.8 px | 0.00 | 0.00 | 38 |
| stroke 93 | 6 % → 0 % | 61.4 px | 0.00 | 0.00 | 107 |
| stroke 94 | 2 % → 0 % | 67.1 px | 0.00 | 0.00 | 21 |
| stroke 95 | 7 % → 0 % | 48.5 px | 0.00 | 0.00 | 208 |
| stroke 96 | 4 % → 1 % | 67.6 px | 0.06 | 0.21 | 98 |
| stroke 97 | 6 % → 0 % | 173.8 px | 0.00 | 0.00 | 53 |
| stroke 98 | 9 % → 0 % | 131.4 px | 0.06 | 0.03 | 119 |
| stroke 99 | 10 % → 0 % | 147.8 px | 0.06 | 0.04 | 121 |
| stroke 100 | 11 % → 0 % | 223.4 px | 0.06 | 0.03 | 94 |
| stroke 101 | 12 % → 0 % | 229.0 px | 0.06 | 0.03 | 90 |
| stroke 102 | 14 % → 0 % | 241.8 px | 0.06 | 0.03 | 106 |
| stroke 103 | 15 % → 0 % | 272.1 px | 0.06 | 0.02 | 110 |
| stroke 104 | 16 % → 0 % | 309.1 px | 0.06 | 0.02 | 98 |
| stroke 105 | 17 % → 0 % | 307.7 px | 0.03 | 0.00 | 88 |
| stroke 106 | 17 % → 0 % | 289.1 px | 0.00 | 0.00 | 115 |
| stroke 107 | 17 % → 0 % | 375.7 px | 0.00 | 0.00 | 91 |
| stroke 108 | 17 % → 0 % | 225.3 px | 0.06 | 0.02 | 312 |
| stroke 109 | 22 % → 0 % | 223.3 px | 0.07 | 0.00 | 522 |
| stroke 110 | 16 % → 0 % | 207.0 px | 0.06 | 0.02 | 350 |
| stroke 111 | 24 % → 0 % | 2131.6 px | 0.00 | 0.00 | 25 |
| stroke 112 | 3 % → 0 % | 65.8 px | 0.00 | 0.00 | 21 |
| stroke 113 | 6 % → 0 % | 59.7 px | 0.00 | 0.00 | 116 |
| stroke 114 | 14 % → 0 % | 414.4 px | 0.00 | 0.00 | 21 |
| stroke 115 | 16 % → 0 % | 360.8 px | 0.00 | 0.00 | 33 |
| stroke 116 | 18 % → 0 % | 334.4 px | 0.00 | 0.00 | 59 |
| stroke 117 | 21 % → 0 % | 294.0 px | 0.00 | 0.00 | 46 |
| stroke 118 | 27 % → 0 % | 257.1 px | 0.00 | 0.00 | 88 |
| stroke 119 | 34 % → 0 % | 174.6 px | 0.00 | 0.00 | 448 |
| stroke 120 | 29 % → 0 % | 358.3 px | 0.00 | 0.00 | 101 |
| stroke 121 | 19 % → 0 % | 619.8 px | 0.00 | 0.00 | 42 |
| stroke 122 | 18 % → 0 % | 582.1 px | 0.00 | 0.00 | 41 |
| stroke 123 | 22 % → 0 % | 436.6 px | 0.00 | 0.00 | 59 |
| stroke 124 | 25 % → 0 % | 338.6 px | 0.00 | 0.00 | 104 |
| stroke 125 | 28 % → 0 % | 290.5 px | 0.00 | 0.00 | 192 |
| stroke 126 | 28 % → 0 % | 215.7 px | 0.00 | 0.00 | 442 |
| stroke 127 | 26 % → 0 % | 339.9 px | 0.00 | 0.00 | 233 |
| stroke 128 | 1 % → 1 % | 21.4 px | 0.07 | 0.99 | 7 |
| stroke 129 | 0 % → 0 % | 21.1 px | 0.06 | 1.00 | 10 |

## Refs v3 · #48 Black bands with drips — own sheet
own sheet 800 × 1045 · Watercolour 1.00 + water 35 % · 112 px · 440.2 s

![Refs v3 · #48 Black bands with drips — own sheet](Refs-v3-48-Black-bands-with-drips-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 13 % → 96 % | 77.5 px | 0.29 | 7.48 | 1254 |
| stroke 2 | 16 % → 95 % | 124.8 px | 0.30 | 6.02 | 2303 |
| stroke 3 | 34 % → 92 % | 106.3 px | 0.30 | 2.72 | 10724 |
| stroke 4 | 42 % → 93 % | 151.6 px | 0.29 | 2.18 | 9741 |
| stroke 5 | 47 % → 93 % | 227.9 px | 0.29 | 2.00 | 8239 |
| stroke 6 | 51 % → 93 % | 258.2 px | 0.29 | 1.83 | 22701 |
| stroke 7 | 56 % → 94 % | 265.5 px | 0.30 | 1.69 | 13537 |
| stroke 8 | 57 % → 95 % | 271.7 px | 0.29 | 1.68 | 18764 |
| stroke 9 | 58 % → 95 % | 277.5 px | 0.30 | 1.66 | 10690 |
| stroke 10 | 56 % → 96 % | 346.9 px | 0.29 | 1.71 | 8270 |
| stroke 11 | 56 % → 96 % | 354.9 px | 0.29 | 1.71 | 8278 |
| stroke 12 | 57 % → 95 % | 296.3 px | 0.30 | 1.66 | 9909 |
| stroke 13 | 57 % → 91 % | 274.0 px | 0.29 | 1.59 | 9823 |
| stroke 14 | 58 % → 83 % | 274.6 px | 0.29 | 1.44 | 8818 |
| stroke 15 | 56 % → 74 % | 299.8 px | 0.29 | 1.31 | 7090 |
| stroke 16 | 58 % → 66 % | 275.0 px | 0.29 | 1.13 | 9544 |
| stroke 17 | 56 % → 57 % | 353.6 px | 0.29 | 1.02 | 8637 |
| stroke 18 | 53 % → 53 % | 817.0 px | 0.29 | 1.00 | 1120 |

Numbers say: wet paint spreads well beyond the stroke.

## Refs v3 · #49 Magenta letters round — own sheet
own sheet 800 × 1000 · Ink 0.98 · 64 px · 170.4 s

![Refs v3 · #49 Magenta letters round — own sheet](Refs-v3-49-Magenta-letters-round-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 3 % → 29 % | 58.6 px | 0.48 | 11.22 | 119 |
| stroke 2 | 5 % → 27 % | 150.4 px | 0.48 | 5.91 | 46 |
| stroke 3 | 5 % → 20 % | 65.6 px | 0.49 | 4.51 | 98 |
| stroke 4 | 9 % → 23 % | 113.1 px | 0.49 | 2.59 | 166 |
| stroke 5 | 16 % → 27 % | 100.7 px | 0.49 | 1.63 | 1172 |
| stroke 6 | 7 % → 24 % | 51.2 px | 0.46 | 3.17 | 567 |
| stroke 7 | 19 % → 29 % | 135.0 px | 0.47 | 1.54 | 470 |
| stroke 8 | 5 % → 36 % | 66.9 px | 0.48 | 7.76 | 347 |
| stroke 9 | 8 % → 37 % | 129.8 px | 0.49 | 4.40 | 307 |
| stroke 10 | 12 % → 27 % | 149.5 px | 0.48 | 2.24 | 428 |
| stroke 11 | 16 % → 32 % | 276.8 px | 0.48 | 1.96 | 217 |
| stroke 12 | 17 % → 30 % | 210.9 px | 0.49 | 1.70 | 334 |
| stroke 13 | 31 % → 34 % | 157.6 px | 0.47 | 1.11 | 1369 |
| stroke 14 | 20 % → 27 % | 58.6 px | 0.50 | 1.35 | 3633 |
| stroke 15 | 10 % → 35 % | 215.8 px | 0.48 | 3.49 | 190 |
| stroke 16 | 17 % → 35 % | 121.5 px | 0.48 | 2.13 | 1199 |
| stroke 17 | 25 % → 35 % | 241.5 px | 0.48 | 1.42 | 1160 |
| stroke 18 | 25 % → 36 % | 400.1 px | 0.48 | 1.44 | 480 |
| stroke 19 | 26 % → 36 % | 265.5 px | 0.48 | 1.41 | 990 |
| stroke 20 | 13 % → 34 % | 499.1 px | 0.48 | 2.59 | 29 |
| stroke 21 | 22 % → 37 % | 104.0 px | 0.48 | 1.66 | 2266 |
| stroke 22 | 18 % → 37 % | 142.7 px | 0.48 | 2.02 | 749 |
| stroke 23 | 14 % → 40 % | 159.4 px | 0.47 | 2.93 | 845 |
| stroke 24 | 9 % → 41 % | 88.5 px | 0.48 | 4.56 | 680 |
| stroke 25 | 21 % → 29 % | 262.7 px | 0.47 | 1.38 | 867 |
| stroke 26 | 29 % → 32 % | 359.2 px | 0.47 | 1.10 | 431 |
| stroke 27 | 29 % → 31 % | 352.8 px | 0.47 | 1.10 | 267 |
| stroke 28 | 6 % → 45 % | 62.9 px | 0.49 | 7.31 | 291 |
| stroke 29 | 27 % → 35 % | 135.8 px | 0.48 | 1.28 | 1150 |
| stroke 30 | 33 % → 37 % | 207.7 px | 0.48 | 1.13 | 807 |
| stroke 31 | 24 % → 36 % | 73.8 px | 0.48 | 1.46 | 2137 |
| stroke 32 | 26 % → 40 % | 96.6 px | 0.48 | 1.52 | 1745 |
| stroke 33 | 18 % → 38 % | 296.4 px | 0.48 | 2.11 | 367 |
| stroke 34 | 11 % → 37 % | 130.4 px | 0.49 | 3.48 | 478 |
| stroke 35 | 29 % → 34 % | 195.0 px | 0.48 | 1.19 | 979 |
| stroke 36 | 27 % → 32 % | 311.2 px | 0.48 | 1.18 | 377 |
| stroke 37 | 11 % → 29 % | 92.2 px | 0.50 | 2.62 | 337 |
| stroke 38 | 23 % → 34 % | 255.8 px | 0.50 | 1.51 | 432 |
| stroke 39 | 20 % → 29 % | 172.7 px | 0.50 | 1.42 | 225 |
| stroke 40 | 9 % → 22 % | 157.6 px | 0.51 | 2.56 | 101 |
| stroke 41 | 19 % → 29 % | 252.4 px | 0.50 | 1.53 | 178 |
| stroke 42 | 26 % → 28 % | 195.8 px | 0.50 | 1.05 | 1065 |
| stroke 43 | 25 % → 25 % | 566.8 px | 0.50 | 1.02 | 94 |
| stroke 44 | 35 % → 36 % | 282.8 px | 0.49 | 1.01 | 605 |

Numbers say: wet paint spreads well beyond the stroke.

## Refs v3 · #50 Swipes on seaside — own sheet
own sheet 800 × 1160 · Gouache 1.00 + water 15 % · 80 px · 376.9 s

![Refs v3 · #50 Swipes on seaside — own sheet](Refs-v3-50-Swipes-on-seaside-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 10 % → 0 % | 75.2 px | 0.00 | 0.00 | 898 |
| stroke 2 | 13 % → 0 % | 182.4 px | 0.00 | 0.00 | 524 |
| stroke 3 | 11 % → 0 % | 74.0 px | 0.00 | 0.00 | 1262 |
| stroke 4 | 21 % → 0 % | 277.7 px | 0.00 | 0.00 | 564 |
| stroke 5 | 8 % → 0 % | 112.5 px | 0.00 | 0.00 | 588 |
| stroke 6 | 15 % → 0 % | 115.6 px | 0.00 | 0.00 | 1319 |
| stroke 7 | 26 % → 0 % | 118.7 px | 0.00 | 0.00 | 4336 |
| stroke 8 | 37 % → 0 % | 328.8 px | 0.00 | 0.00 | 1004 |
| stroke 9 | 34 % → 0 % | 172.4 px | 0.00 | 0.00 | 3073 |
| stroke 10 | 45 % → 4 % | 262.9 px | 0.34 | 0.09 | 2426 |
| stroke 11 | 39 % → 3 % | 305.5 px | 0.36 | 0.07 | 1569 |
| stroke 12 | 46 % → 11 % | 256.8 px | 0.39 | 0.23 | 2762 |
| stroke 13 | 44 % → 12 % | 282.9 px | 0.38 | 0.28 | 1891 |
| stroke 14 | 49 % → 20 % | 252.8 px | 0.41 | 0.42 | 3355 |
| stroke 15 | 51 % → 23 % | 287.4 px | 0.40 | 0.45 | 2459 |
| stroke 16 | 52 % → 32 % | 242.1 px | 0.41 | 0.62 | 4331 |
| stroke 17 | 50 % → 30 % | 449.9 px | 0.41 | 0.61 | 929 |
| stroke 18 | 50 % → 43 % | 340.0 px | 0.42 | 0.86 | 3564 |
| stroke 19 | 48 % → 41 % | 399.6 px | 0.41 | 0.86 | 1339 |
| stroke 20 | 17 % → 70 % | 371.1 px | 0.44 | 4.03 | 307 |
| stroke 21 | 1 % → 74 % | 24.5 px | 0.44 | 71.72 | 79 |
| stroke 22 | 10 % → 0 % | 66.6 px | 0.00 | 0.00 | 1702 |
| stroke 23 | 6 % → 0 % | 110.4 px | 0.00 | 0.00 | 312 |
| stroke 24 | 20 % → 0 % | 91.5 px | 0.00 | 0.00 | 4068 |
| stroke 25 | 25 % → 0 % | 215.3 px | 0.00 | 0.00 | 1147 |
| stroke 26 | 29 % → 0 % | 185.1 px | 0.00 | 0.00 | 3077 |
| stroke 27 | 24 % → 0 % | 206.6 px | 0.00 | 0.00 | 3530 |
| stroke 28 | 38 % → 0 % | 151.1 px | 0.00 | 0.00 | 16216 |
| stroke 29 | 38 % → 0 % | 894.6 px | 0.00 | 0.00 | 515 |
| stroke 30 | 49 % → 0 % | 827.4 px | 0.00 | 0.00 | 1042 |
| stroke 31 | 33 % → 0 % | 564.5 px | 0.00 | 0.00 | 498 |
| stroke 32 | 37 % → 0 % | 351.9 px | 0.00 | 0.00 | 1396 |
| stroke 33 | 39 % → 0 % | 427.5 px | 0.00 | 0.00 | 1239 |
| stroke 34 | 7 % → 35 % | 79.0 px | 0.41 | 4.95 | 1125 |
| stroke 35 | 9 % → 49 % | 165.2 px | 0.41 | 5.50 | 390 |
| stroke 36 | 11 % → 55 % | 275.1 px | 0.42 | 5.04 | 325 |
| stroke 37 | 3 % → 76 % | 76.6 px | 0.44 | 24.56 | 301 |
| stroke 38 | 1 % → 0 % | 22.4 px | 0.00 | 0.00 | 51 |
| stroke 39 | 1 % → 1 % | 22.1 px | 0.35 | 1.48 | 21 |
| stroke 40 | 8 % → 0 % | 38.7 px | 0.00 | 0.00 | 531 |
| stroke 41 | 11 % → 0 % | 59.0 px | 0.00 | 0.00 | 723 |
| stroke 42 | 4 % → 0 % | 40.3 px | 0.00 | 0.00 | 349 |
| stroke 43 | 5 % → 0 % | 177.0 px | 0.00 | 0.00 | 88 |
| stroke 44 | 8 % → 0 % | 56.3 px | 0.00 | 0.00 | 696 |
| stroke 45 | 9 % → 0 % | 132.4 px | 0.00 | 0.00 | 227 |
| stroke 46 | 2 % → 0 % | 41.1 px | 0.00 | 0.00 | 120 |
| stroke 47 | 12 % → 0 % | 66.3 px | 0.00 | 0.00 | 1625 |
| stroke 48 | 20 % → 0 % | 105.6 px | 0.00 | 0.00 | 1350 |
| stroke 49 | 4 % → 3 % | 39.1 px | 0.34 | 0.62 | 521 |
| stroke 50 | 7 % → 6 % | 54.5 px | 0.35 | 0.95 | 661 |
| stroke 51 | 10 % → 12 % | 94.3 px | 0.38 | 1.21 | 413 |
| stroke 52 | 13 % → 16 % | 165.6 px | 0.39 | 1.29 | 288 |
| stroke 53 | 5 % → 75 % | 39.3 px | 0.43 | 15.67 | 427 |
| stroke 54 | 7 % → 76 % | 68.1 px | 0.43 | 10.98 | 376 |
| stroke 55 | 10 % → 80 % | 134.3 px | 0.44 | 7.92 | 217 |
| stroke 56 | 13 % → 76 % | 417.1 px | 0.44 | 5.93 | 72 |
| stroke 57 | 5 % → 0 % | 45.7 px | 0.00 | 0.00 | 213 |
| stroke 58 | 7 % → 0 % | 76.2 px | 0.00 | 0.00 | 252 |
| stroke 59 | 2 % → 0 % | 48.1 px | 0.00 | 0.00 | 130 |
| stroke 60 | 4 % → 0 % | 92.5 px | 0.00 | 0.00 | 129 |
| stroke 61 | 5 % → 0 % | 96.6 px | 0.00 | 0.00 | 188 |
| stroke 62 | 7 % → 0 % | 75.0 px | 0.00 | 0.00 | 510 |
| stroke 63 | 9 % → 0 % | 198.5 px | 0.00 | 0.00 | 177 |
| stroke 64 | 4 % → 0 % | 63.3 px | 0.00 | 0.00 | 155 |
| stroke 65 | 9 % → 0 % | 61.3 px | 0.00 | 0.00 | 602 |
| stroke 66 | 12 % → 0 % | 78.0 px | 0.00 | 0.00 | 793 |
| stroke 67 | 13 % → 0 % | 218.6 px | 0.00 | 0.00 | 243 |
| stroke 68 | 4 % → 37 % | 45.8 px | 0.43 | 8.33 | 357 |
| stroke 69 | 5 % → 77 % | 45.4 px | 0.45 | 15.90 | 315 |
| stroke 70 | 8 % → 74 % | 106.2 px | 0.45 | 9.53 | 185 |
| stroke 71 | 5 % → 46 % | 83.1 px | 0.43 | 9.38 | 394 |
| stroke 72 | 10 % → 52 % | 106.7 px | 0.42 | 5.36 | 992 |
| stroke 73 | 5 % → 44 % | 87.3 px | 0.41 | 8.26 | 734 |
| stroke 74 | 17 % → 58 % | 120.1 px | 0.43 | 3.37 | 2328 |
| stroke 75 | 24 % → 56 % | 163.4 px | 0.42 | 2.30 | 1253 |
| stroke 76 | 32 % → 64 % | 118.1 px | 0.43 | 2.03 | 4771 |
| stroke 77 | 31 % → 70 % | 457.0 px | 0.44 | 2.22 | 378 |
| stroke 78 | 43 % → 76 % | 201.1 px | 0.43 | 1.77 | 8336 |
| stroke 79 | 37 % → 74 % | 360.4 px | 0.45 | 2.03 | 1168 |
| stroke 80 | 50 % → 81 % | 329.7 px | 0.44 | 1.61 | 3700 |
| stroke 81 | 44 % → 74 % | 579.3 px | 0.42 | 1.69 | 676 |
| stroke 82 | 57 % → 78 % | 241.3 px | 0.44 | 1.38 | 4250 |
| stroke 83 | 50 % → 75 % | 457.0 px | 0.43 | 1.51 | 912 |
| stroke 84 | 67 % → 77 % | 285.4 px | 0.45 | 1.15 | 4961 |
| stroke 85 | 62 % → 72 % | 308.7 px | 0.44 | 1.16 | 2708 |
| stroke 86 | 75 % → 74 % | 265.1 px | 0.45 | 1.00 | 3073 |
| stroke 87 | 70 % → 70 % | 290.2 px | 0.44 | 0.99 | 1975 |

Numbers say: wet paint spreads well beyond the stroke.



## Measures of the own sheets (v4 §9)

| sheet | fine lines (across ÷ along) | gaps | edge steps |
|---|---|---|---|
| Refs v3 · #01 HW peach cloud — own sheet | 1.74 | 0.9 % | 28.4 % |
| Refs v3 · #02 HW cream strokes — own sheet | 2.14 | 24.0 % | 29.7 % |
| Refs v3 · #03 HW navy contours — own sheet | 1.72 | 5.3 % | 30.6 % |
| Refs v3 · #04 HW grey cloud — own sheet | 2.04 | 10.2 % | 30.4 % |
| Refs v3 · #05 HW green in rust loops — own sheet | 1.73 | 2.4 % | 28.1 % |
| Refs v3 · #06 HW scrubbed grey — own sheet | 2.04 | 10.3 % | 30.6 % |
| Refs v3 · #07 HW blue L and zigzag — own sheet | 1.71 | 5.3 % | 26.5 % |
| Refs v3 · #08 HW lilac crown basket — own sheet | 1.84 | 15.8 % | 34.7 % |
| Refs v3 · #09 HW white loops — own sheet | 1.98 | 9.4 % | 28.3 % |
| Refs v3 · #10 HW maroon loops — own sheet | 1.73 | 1.6 % | 28.0 % |
| Refs v3 · #11 HW purple balls — own sheet | 1.67 | 46.9 % | 38.4 % |
| Refs v3 · #12 HW black-olive cage — own sheet | 1.86 | 15.8 % | 34.4 % |
| Refs v3 · #13 HW blue streaky form — own sheet | 1.64 | 2.4 % | 27.1 % |
| Refs v3 · #14 HW olive totem — own sheet | 1.65 | 8.4 % | 36.8 % |
| Refs v3 · #15 Ultramarine script — own sheet | 1.07 | 2.4 % | 41.9 % |
| Refs v3 · #16 Shrigley strokes — own sheet | 1.05 | 5.4 % | 40.9 % |
| Refs v3 · #17 Krovostok dry brush — own sheet | 1.48 | 1.2 % | 34.0 % |
| Refs v3 · #18 Twombly blue sticks — own sheet | 1.56 | 0.1 % | 28.4 % |
| Refs v3 · #19 Guston charcoal hand — own sheet | 1.01 | 0.0 % | 32.9 % |
| Refs v3 · #20 Orange crayon — own sheet | 1.00 | 0.0 % | 31.7 % |
| Refs v3 · #21 Gritty dog contours — own sheet | 1.30 | 42.9 % | 48.9 % |
| Refs v3 · #22 Wasilewski brush poster — own sheet | 0.99 | 5.9 % | 35.4 % |
| Refs v3 · #23 Report dry white mask — own sheet | 1.34 | 0.1 % | 37.1 % |
| Refs v3 · #24 Picasso flat oil — own sheet | 1.73 | 34.8 % | 32.5 % |
| Refs v3 · #25 Yellow heavy stroke — own sheet | 1.67 | 1.3 % | 12.6 % |
| Refs v3 · #26 Ink caricature — own sheet | 1.14 | 0.8 % | 41.0 % |
| Refs v3 · #27 Orange impasto swatch — own sheet | 2.01 | 0.2 % | 35.9 % |
| Refs v3 · #28 Miles Davis lines — own sheet | 1.12 | 1.6 % | 37.4 % |
| Refs v3 · #29 Shrigley asterisk — own sheet | 1.01 | 0.0 % | 40.0 % |
| Refs v3 · #30 Red gouache face — own sheet | 1.52 | 0.5 % | 40.6 % |
| Refs v3 · #31 Warhol blotted line — own sheet | 1.25 | 4.2 % | 39.6 % |
| Refs v3 · #32 Thick orange swipes — own sheet | 3.43 | 0.1 % | 21.1 % |
| Refs v3 · #33 Red wet-in-wet flames — own sheet | 1.12 | 2.5 % | 36.9 % |
| Refs v3 · #34 Magenta oil patches — own sheet | 1.91 | 14.4 % | 29.6 % |
| Refs v3 · #35 Red band with runs — own sheet | 1.02 | 0.0 % | 34.9 % |
| Refs v3 · #36 Magenta letters flat — own sheet | 1.38 | 3.1 % | 33.4 % |
| Refs v3 · #37 Oil still life — own sheet | 1.65 | 52.4 % | 33.9 % |
| Refs v3 · #38 Sanguine drawing — own sheet | 1.81 | 1.1 % | 40.2 % |
| Refs v3 · #39 Thick impasto weave — own sheet | 1.47 | 0.1 % | 30.1 % |
| Refs v3 · #40 Watercolour blooms — own sheet | 1.25 | 13.5 % | 45.0 % |
| Refs v3 · #41 Coloured pencil — own sheet | 1.72 | 22.8 % | 40.1 % |
| Refs v3 · #42 Pink shaggy pastel — own sheet | 1.37 | 0.0 % | 24.0 % |
| Refs v3 · #43 Dragged black blocks — own sheet | 1.96 | 0.1 % | 55.8 % |
| Refs v3 · #44 Blue looping ribbon — own sheet | 1.36 | 0.0 % | 41.9 % |
| Refs v3 · #45 Pastel pepper — own sheet | 1.33 | 0.0 % | 32.7 % |
| Refs v3 · #46 Ink lips on wet paper — own sheet | 1.01 | 0.0 % | 37.7 % |
| Refs v3 · #47 Pink knife slabs — own sheet | 0.84 | 55.7 % | 43.3 % |
| Refs v3 · #48 Black bands with drips — own sheet | 1.59 | 0.0 % | 27.3 % |
| Refs v3 · #49 Magenta letters round — own sheet | 1.47 | 0.0 % | 33.9 % |
| Refs v3 · #50 Swipes on seaside — own sheet | 2.60 | 6.3 % | 17.5 % |
