![All brushes](contact.png)

# Brush Lab — 224 brushes · 8 Nov 2026 at 23:07

Every sheet: 1500 × 600, ten strokes in a 5 × 2 grid — 1. light line · 2. heavy line · 3. pressure swell · 4. fast wave · 5. slow wave · 6. spiral · 7. loop · 8. tilted · 9. over the wet one · 10. long, no reload (cell 8 holds «tilted» and «over the wet one» crossed). The CPU reference of Mamay's paint engine; the wet layer settles 20 s at the end.

Columns: **covered** = share of the cell with paint right after the stroke → after settling; **width** = painted area of the stroke ÷ its length (px); **dark** = mean darkness of the painted pixels above the paper's own grain (0 = paper, 1 = black); **spread** = how far wet paint went beyond the stroke (1.0 = stayed); **ms** = the stroke on the CPU; long stroke: paint in each quarter of its length (it should run out: wet → streaks → dry tail).

## Brush Artist · Refs · #01 Henry Ward peach cloud
Gouache 1.00 · 44 px · 26.3 s

![Brush Artist · Refs · #01 Henry Ward peach cloud](Brush-Artist-Refs-01-Henry-Ward-peach-cloud.png)

A light paint: laid on a grey sheet (on white it cannot be seen); **dark** = how far it is from the grey either way.

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 5 % → 0 % | 13.4 px | 0.00 | 0.00 | 306 |
| heavy line | 8 % → 0 % | 22.4 px | 0.32 | 0.01 | 121 |
| pressure swell | 7 % → 3 % | 24.8 px | 0.33 | 0.40 | 93 |
| fast wave | 31 % → 3 % | 36.2 px | 0.27 | 0.09 | 380 |
| slow wave | 20 % → 2 % | 23.3 px | 0.32 | 0.10 | 691 |
| spiral | 33 % → 2 % | 21.6 px | 0.35 | 0.07 | 647 |
| loop | 17 % → 0 % | 22.4 px | 0.32 | 0.01 | 318 |
| tilted | 12 % → 11 % | 32.7 px | 0.25 | 0.97 | 177 |
| over the wet one | 16 % → 2 % | 12.9 px | 0.25 | 0.10 | 128 |
| long, no reload | 30 % → 2 % | 13.6 px | 0.32 | 0.08 | 797 | quarters: 0.03 → 0.03 → 0.03 → 0.03

Numbers say: light vs heavy: width 13.4 → 22.4 px, dark 0.00 → 0.32; the long stroke does not run out of paint.

## Brush Artist · Refs · #02 Henry Ward cream strokes
Gouache 1.00 · 46 px · 29.5 s

![Brush Artist · Refs · #02 Henry Ward cream strokes](Brush-Artist-Refs-02-Henry-Ward-cream-strokes.png)

A light paint: laid on a grey sheet (on white it cannot be seen); **dark** = how far it is from the grey either way.

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 5 % → 0 % | 14.3 px | 0.00 | 0.00 | 328 |
| heavy line | 8 % → 2 % | 24.6 px | 0.41 | 0.22 | 133 |
| pressure swell | 7 % → 3 % | 27.7 px | 0.41 | 0.38 | 93 |
| fast wave | 30 % → 4 % | 34.5 px | 0.36 | 0.15 | 393 |
| slow wave | 21 % → 5 % | 24.3 px | 0.39 | 0.21 | 654 |
| spiral | 43 % → 4 % | 28.4 px | 0.40 | 0.10 | 678 |
| loop | 19 % → 1 % | 24.8 px | 0.39 | 0.04 | 318 |
| tilted | 12 % → 12 % | 33.1 px | 0.34 | 0.98 | 179 |
| over the wet one | 17 % → 1 % | 13.0 px | 0.34 | 0.05 | 126 |
| long, no reload | 25 % → 4 % | 11.1 px | 0.41 | 0.17 | 765 | quarters: 0.03 → 0.04 → 0.03 → 0.04

Numbers say: light vs heavy: width 14.3 → 24.6 px, dark 0.00 → 0.41; the long stroke does not run out of paint.

## Brush Artist · Refs · #03 Henry Ward navy contours
Impasto 1.00 · 22 px · 13.9 s

![Brush Artist · Refs · #03 Henry Ward navy contours](Brush-Artist-Refs-03-Henry-Ward-navy-contours.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 7 % → 6 % | 19.4 px | 0.72 | 0.90 | 231 |
| heavy line | 6 % → 6 % | 18.3 px | 0.71 | 0.92 | 77 |
| pressure swell | 5 % → 5 % | 20.1 px | 0.75 | 0.89 | 49 |
| fast wave | 16 % → 11 % | 18.3 px | 0.76 | 0.71 | 181 |
| slow wave | 18 % → 14 % | 20.5 px | 0.72 | 0.78 | 368 |
| spiral | 28 % → 13 % | 18.3 px | 0.68 | 0.47 | 375 |
| loop | 13 % → 11 % | 17.0 px | 0.71 | 0.83 | 182 |
| tilted | 7 % → 7 % | 20.7 px | 0.73 | 0.99 | 107 |
| over the wet one | 15 % → 13 % | 20.4 px | 0.73 | 0.88 | 82 |
| long, no reload | 32 % → 13 % | 14.4 px | 0.71 | 0.41 | 456 | quarters: 0.33 → 0.27 → 0.19 → 0.08

Numbers say: light vs heavy: width 19.4 → 18.3 px, dark 0.72 → 0.71; pressure barely changes the width.

## Brush Artist · Refs · #04 Henry Ward grey cloud
Gouache 1.00 · 50 px · 29.3 s

![Brush Artist · Refs · #04 Henry Ward grey cloud](Brush-Artist-Refs-04-Henry-Ward-grey-cloud.png)

A light paint: laid on a grey sheet (on white it cannot be seen); **dark** = how far it is from the grey either way.

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 5 % → 0 % | 14.6 px | 0.00 | 0.00 | 366 |
| heavy line | 10 % → 2 % | 28.3 px | 0.31 | 0.25 | 148 |
| pressure swell | 7 % → 2 % | 24.5 px | 0.31 | 0.36 | 105 |
| fast wave | 32 % → 4 % | 37.5 px | 0.24 | 0.14 | 480 |
| slow wave | 23 % → 2 % | 26.3 px | 0.33 | 0.10 | 653 |
| spiral | 47 % → 3 % | 30.8 px | 0.37 | 0.06 | 712 |
| loop | 19 % → 0 % | 25.2 px | 0.00 | 0.00 | 354 |
| tilted | 12 % → 12 % | 33.3 px | 0.24 | 0.98 | 213 |
| over the wet one | 17 % → 3 % | 14.1 px | 0.24 | 0.17 | 142 |
| long, no reload | 22 % → 4 % | 9.9 px | 0.34 | 0.17 | 891 | quarters: 0.03 → 0.04 → 0.04 → 0.04

Numbers say: light vs heavy: width 14.6 → 28.3 px, dark 0.00 → 0.31; the long stroke does not run out of paint.

## Brush Artist · Refs · #05 Henry Ward green in rust loops
Impasto 1.00 · 20 px · 13.5 s

![Brush Artist · Refs · #05 Henry Ward green in rust loops](Brush-Artist-Refs-05-Henry-Ward-green-in-rust-loops.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 6 % → 6 % | 18.5 px | 0.56 | 0.88 | 239 |
| heavy line | 8 % → 7 % | 22.1 px | 0.56 | 0.87 | 96 |
| pressure swell | 4 % → 4 % | 16.1 px | 0.58 | 0.93 | 64 |
| fast wave | 16 % → 10 % | 17.9 px | 0.56 | 0.67 | 188 |
| slow wave | 16 % → 12 % | 19.1 px | 0.56 | 0.74 | 333 |
| spiral | 24 % → 11 % | 16.1 px | 0.53 | 0.46 | 386 |
| loop | 15 % → 12 % | 19.7 px | 0.56 | 0.79 | 154 |
| tilted | 7 % → 7 % | 19.8 px | 0.58 | 0.99 | 113 |
| over the wet one | 14 % → 12 % | 18.1 px | 0.58 | 0.85 | 64 |
| long, no reload | 28 % → 12 % | 12.6 px | 0.55 | 0.41 | 537 | quarters: 0.23 → 0.17 → 0.11 → 0.04

Numbers say: light vs heavy: width 18.5 → 22.1 px, dark 0.56 → 0.56.

## Brush Artist · Refs · #06 Henry Ward scrubbed grey
Gouache 1.00 · 50 px · 29.5 s

![Brush Artist · Refs · #06 Henry Ward scrubbed grey](Brush-Artist-Refs-06-Henry-Ward-scrubbed-grey.png)

A light paint: laid on a grey sheet (on white it cannot be seen); **dark** = how far it is from the grey either way.

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 5 % → 0 % | 14.6 px | 0.00 | 0.00 | 324 |
| heavy line | 10 % → 2 % | 28.3 px | 0.33 | 0.25 | 146 |
| pressure swell | 7 % → 2 % | 24.5 px | 0.33 | 0.36 | 109 |
| fast wave | 32 % → 4 % | 37.5 px | 0.25 | 0.14 | 390 |
| slow wave | 23 % → 2 % | 26.3 px | 0.34 | 0.10 | 724 |
| spiral | 47 % → 3 % | 30.8 px | 0.38 | 0.06 | 725 |
| loop | 19 % → 0 % | 25.2 px | 0.00 | 0.00 | 341 |
| tilted | 12 % → 12 % | 33.3 px | 0.25 | 0.98 | 219 |
| over the wet one | 17 % → 3 % | 14.1 px | 0.25 | 0.17 | 141 |
| long, no reload | 22 % → 4 % | 9.9 px | 0.36 | 0.17 | 885 | quarters: 0.03 → 0.04 → 0.04 → 0.04

Numbers say: light vs heavy: width 14.6 → 28.3 px, dark 0.00 → 0.33; the long stroke does not run out of paint.

## Brush Artist · Refs · #07 Henry Ward blue L + black zigzag
Impasto 1.00 · 34 px · 15.9 s

![Brush Artist · Refs · #07 Henry Ward blue L + black zigzag](Brush-Artist-Refs-07-Henry-Ward-blue-L-black-zigzag.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 10 % → 9 % | 30.2 px | 0.59 | 0.86 | 318 |
| heavy line | 11 % → 10 % | 30.8 px | 0.59 | 0.93 | 122 |
| pressure swell | 8 % → 8 % | 31.6 px | 0.59 | 0.92 | 99 |
| fast wave | 25 % → 19 % | 28.8 px | 0.60 | 0.77 | 286 |
| slow wave | 26 % → 20 % | 29.7 px | 0.57 | 0.76 | 515 |
| spiral | 44 % → 23 % | 29.1 px | 0.54 | 0.52 | 567 |
| loop | 24 % → 19 % | 30.4 px | 0.57 | 0.80 | 237 |
| tilted | 11 % → 11 % | 29.8 px | 0.61 | 1.00 | 155 |
| over the wet one | 22 % → 20 % | 32.0 px | 0.61 | 0.90 | 139 |
| long, no reload | 50 % → 23 % | 22.5 px | 0.57 | 0.46 | 773 | quarters: 0.36 → 0.31 → 0.21 → 0.10

Numbers say: light vs heavy: width 30.2 → 30.8 px, dark 0.59 → 0.59; pressure barely changes the width.

## Brush Artist · Refs · #08 Henry Ward olive bands
Gouache 1.00 · 34 px · 21.9 s

![Brush Artist · Refs · #08 Henry Ward olive bands](Brush-Artist-Refs-08-Henry-Ward-olive-bands.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 2 % → 0 % | 5.8 px | 0.00 | 0.00 | 227 |
| heavy line | 7 % → 1 % | 19.2 px | 0.61 | 0.15 | 141 |
| pressure swell | 5 % → 1 % | 19.1 px | 0.61 | 0.20 | 73 |
| fast wave | 18 % → 1 % | 21.1 px | 0.59 | 0.04 | 308 |
| slow wave | 16 % → 0 % | 18.3 px | 0.63 | 0.02 | 552 |
| spiral | 27 % → 0 % | 17.5 px | 0.52 | 0.01 | 495 |
| loop | 10 % → 1 % | 13.5 px | 0.61 | 0.12 | 233 |
| tilted | 7 % → 7 % | 20.5 px | 0.65 | 0.92 | 120 |
| over the wet one | 11 % → 1 % | 9.8 px | 0.65 | 0.12 | 115 |
| long, no reload | 23 % → 2 % | 10.4 px | 0.53 | 0.10 | 622 | quarters: 0.21 → 0.11 → 0.12 → 0.08

Numbers say: light vs heavy: width 5.8 → 19.2 px, dark 0.00 → 0.61.

## Brush Artist · Refs · #09 Henry Ward white loops
Gouache 1.00 · 46 px · 29.9 s

![Brush Artist · Refs · #09 Henry Ward white loops](Brush-Artist-Refs-09-Henry-Ward-white-loops.png)

A light paint: laid on a grey sheet (on white it cannot be seen); **dark** = how far it is from the grey either way.

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 5 % → 0 % | 14.3 px | 0.00 | 0.00 | 314 |
| heavy line | 8 % → 2 % | 24.6 px | 0.43 | 0.22 | 137 |
| pressure swell | 7 % → 3 % | 27.7 px | 0.43 | 0.38 | 114 |
| fast wave | 30 % → 4 % | 34.5 px | 0.38 | 0.15 | 419 |
| slow wave | 21 % → 5 % | 24.3 px | 0.40 | 0.21 | 623 |
| spiral | 43 % → 4 % | 28.4 px | 0.41 | 0.10 | 674 |
| loop | 19 % → 1 % | 24.8 px | 0.41 | 0.04 | 349 |
| tilted | 12 % → 12 % | 33.1 px | 0.37 | 0.98 | 195 |
| over the wet one | 17 % → 1 % | 13.0 px | 0.37 | 0.05 | 141 |
| long, no reload | 25 % → 4 % | 11.1 px | 0.41 | 0.17 | 837 | quarters: 0.03 → 0.04 → 0.04 → 0.04

Numbers say: light vs heavy: width 14.3 → 24.6 px, dark 0.00 → 0.43; the long stroke does not run out of paint.

## Brush Artist · Refs · #10 Henry Ward maroon loops
Impasto 1.00 · 30 px · 15.0 s

![Brush Artist · Refs · #10 Henry Ward maroon loops](Brush-Artist-Refs-10-Henry-Ward-maroon-loops.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 10 % → 8 % | 27.9 px | 0.73 | 0.88 | 307 |
| heavy line | 11 % → 10 % | 32.1 px | 0.73 | 0.90 | 79 |
| pressure swell | 8 % → 7 % | 29.7 px | 0.74 | 0.91 | 81 |
| fast wave | 23 % → 17 % | 26.5 px | 0.76 | 0.76 | 245 |
| slow wave | 22 % → 19 % | 25.9 px | 0.72 | 0.85 | 428 |
| spiral | 37 % → 18 % | 24.2 px | 0.72 | 0.50 | 446 |
| loop | 17 % → 15 % | 22.1 px | 0.73 | 0.86 | 252 |
| tilted | 10 % → 10 % | 27.6 px | 0.73 | 1.00 | 105 |
| over the wet one | 19 % → 17 % | 26.8 px | 0.73 | 0.86 | 95 |
| long, no reload | 40 % → 17 % | 18.0 px | 0.71 | 0.43 | 604 | quarters: 0.38 → 0.33 → 0.27 → 0.18

Numbers say: light vs heavy: width 27.9 → 32.1 px, dark 0.73 → 0.73.

## Brush Artist · Refs · #11 Henry Ward purple spun balls
Impasto 1.00 · 36 px · 16.0 s

![Brush Artist · Refs · #11 Henry Ward purple spun balls](Brush-Artist-Refs-11-Henry-Ward-purple-spun-balls.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 11 % → 10 % | 31.5 px | 0.74 | 0.93 | 103 |
| heavy line | 11 % → 10 % | 30.5 px | 0.74 | 0.95 | 115 |
| pressure swell | 10 % → 9 % | 36.4 px | 0.75 | 0.92 | 87 |
| fast wave | 27 % → 21 % | 31.1 px | 0.74 | 0.78 | 288 |
| slow wave | 30 % → 24 % | 34.6 px | 0.73 | 0.82 | 525 |
| spiral | 40 % → 24 % | 26.5 px | 0.70 | 0.59 | 522 |
| loop | 24 % → 21 % | 30.7 px | 0.75 | 0.90 | 259 |
| tilted | 10 % → 10 % | 28.5 px | 0.73 | 1.00 | 134 |
| over the wet one | 22 % → 20 % | 33.9 px | 0.73 | 0.91 | 134 |
| long, no reload | 53 % → 25 % | 23.9 px | 0.74 | 0.46 | 760 | quarters: 0.50 → 0.45 → 0.38 → 0.27

Numbers say: light vs heavy: width 31.5 → 30.5 px, dark 0.74 → 0.74; pressure barely changes the width.

## Brush Artist · Refs · #12 Henry Ward black-olive cage
Gouache 1.00 · 28 px · 21.3 s

![Brush Artist · Refs · #12 Henry Ward black-olive cage](Brush-Artist-Refs-12-Henry-Ward-black-olive-cage.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 2 % → 0 % | 6.3 px | 0.00 | 0.00 | 47 |
| heavy line | 6 % → 1 % | 16.9 px | 0.64 | 0.21 | 112 |
| pressure swell | 5 % → 1 % | 17.2 px | 0.64 | 0.22 | 74 |
| fast wave | 14 % → 0 % | 16.6 px | 0.00 | 0.00 | 250 |
| slow wave | 14 % → 1 % | 15.6 px | 0.64 | 0.07 | 392 |
| spiral | 18 % → 0 % | 11.7 px | 0.63 | 0.02 | 404 |
| loop | 11 % → 1 % | 14.3 px | 0.63 | 0.10 | 203 |
| tilted | 6 % → 6 % | 17.8 px | 0.68 | 0.92 | 122 |
| over the wet one | 10 % → 0 % | 9.7 px | 0.68 | 0.04 | 101 |
| long, no reload | 18 % → 2 % | 8.0 px | 0.59 | 0.12 | 471 | quarters: 0.15 → 0.12 → 0.06 → 0.02

Numbers say: light vs heavy: width 6.3 → 16.9 px, dark 0.00 → 0.64.

## Brush Artist · Refs · #13 Henry Ward blue streaky form
Gouache 1.00 · 50 px · 27.7 s

![Brush Artist · Refs · #13 Henry Ward blue streaky form](Brush-Artist-Refs-13-Henry-Ward-blue-streaky-form.png)

A light paint: laid on a grey sheet (on white it cannot be seen); **dark** = how far it is from the grey either way.

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 5 % → 0 % | 14.6 px | 0.00 | 0.00 | 125 |
| heavy line | 10 % → 2 % | 28.3 px | 0.33 | 0.25 | 163 |
| pressure swell | 7 % → 2 % | 24.5 px | 0.33 | 0.36 | 100 |
| fast wave | 32 % → 4 % | 37.5 px | 0.25 | 0.14 | 439 |
| slow wave | 23 % → 2 % | 26.3 px | 0.34 | 0.10 | 692 |
| spiral | 47 % → 3 % | 30.8 px | 0.38 | 0.06 | 746 |
| loop | 19 % → 0 % | 25.2 px | 0.00 | 0.00 | 312 |
| tilted | 12 % → 12 % | 33.3 px | 0.25 | 0.98 | 208 |
| over the wet one | 17 % → 3 % | 14.1 px | 0.25 | 0.17 | 121 |
| long, no reload | 22 % → 4 % | 9.9 px | 0.35 | 0.17 | 869 | quarters: 0.03 → 0.04 → 0.04 → 0.04

Numbers say: light vs heavy: width 14.6 → 28.3 px, dark 0.00 → 0.33; the long stroke does not run out of paint.

## Brush Artist · Refs · #14 Henry Ward olive totem
Impasto 1.00 · 48 px · 17.8 s

![Brush Artist · Refs · #14 Henry Ward olive totem](Brush-Artist-Refs-14-Henry-Ward-olive-totem.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 15 % → 14 % | 44.4 px | 0.31 | 0.91 | 135 |
| heavy line | 16 % → 15 % | 46.3 px | 0.31 | 0.95 | 163 |
| pressure swell | 12 % → 11 % | 44.0 px | 0.31 | 0.93 | 138 |
| fast wave | 36 % → 28 % | 41.7 px | 0.36 | 0.78 | 412 |
| slow wave | 37 % → 32 % | 42.3 px | 0.30 | 0.87 | 718 |
| spiral | 59 % → 35 % | 38.7 px | 0.28 | 0.59 | 762 |
| loop | 30 % → 27 % | 39.1 px | 0.29 | 0.89 | 400 |
| tilted | 13 % → 13 % | 36.4 px | 0.33 | 1.00 | 191 |
| over the wet one | 28 % → 25 % | 40.5 px | 0.33 | 0.92 | 158 |
| long, no reload | 61 % → 31 % | 27.3 px | 0.27 | 0.52 | 867 | quarters: 0.20 → 0.15 → 0.09 → 0.04

Numbers say: light vs heavy: width 44.4 → 46.3 px, dark 0.31 → 0.31; pressure barely changes the width.

## Brush Artist · Refs · #15 Ultramarine brush script
Ink 1.00 · 4 px · 20.4 s

![Brush Artist · Refs · #15 Ultramarine brush script](Brush-Artist-Refs-15-Ultramarine-brush-script.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 1 % → 3 % | 2.1 px | 0.55 | 3.99 | 26 |
| heavy line | 5 % → 5 % | 15.6 px | 0.62 | 1.00 | 46 |
| pressure swell | 3 % → 4 % | 11.0 px | 0.62 | 1.21 | 27 |
| fast wave | 9 % → 7 % | 10.2 px | 0.54 | 0.81 | 88 |
| slow wave | 8 % → 7 % | 8.8 px | 0.53 | 0.89 | 80 |
| spiral | 11 % → 8 % | 7.3 px | 0.53 | 0.68 | 163 |
| loop | 7 % → 7 % | 9.4 px | 0.54 | 0.96 | 78 |
| tilted | 3 % → 3 % | 7.4 px | 0.64 | 1.04 | 36 |
| over the wet one | 7 % → 7 % | 10.7 px | 0.64 | 1.08 | 34 |
| long, no reload | 16 % → 7 % | 7.1 px | 0.51 | 0.47 | 198 | quarters: 0.14 → 0.04 → 0.01 → 0.00

Numbers say: light vs heavy: width 2.1 → 15.6 px, dark 0.55 → 0.62; wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #18 Blue oil-stick scribbles
Pastel 1.00 · 10 px · 9.4 s

![Brush Artist · Refs · #18 Blue oil-stick scribbles](Brush-Artist-Refs-18-Blue-oil-stick-scribbles.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 1 % → 1 % | 2.9 px | 0.53 | 1.00 | 19 |
| heavy line | 2 % → 2 % | 6.0 px | 0.53 | 1.00 | 21 |
| pressure swell | 1 % → 1 % | 5.5 px | 0.52 | 1.00 | 18 |
| fast wave | 5 % → 5 % | 5.3 px | 0.53 | 1.00 | 61 |
| slow wave | 4 % → 4 % | 5.2 px | 0.53 | 1.00 | 52 |
| spiral | 7 % → 7 % | 4.4 px | 0.52 | 1.00 | 117 |
| loop | 4 % → 4 % | 4.6 px | 0.52 | 1.00 | 51 |
| tilted | 2 % → 2 % | 4.4 px | 0.53 | 1.00 | 23 |
| over the wet one | 3 % → 3 % | 4.8 px | 0.53 | 1.00 | 17 |
| long, no reload | 9 % → 9 % | 4.2 px | 0.52 | 1.00 | 197 | quarters: 0.05 → 0.05 → 0.06 → 0.06

Numbers say: light vs heavy: width 2.9 → 6.0 px, dark 0.53 → 0.53; the long stroke does not run out of paint.

## Brush Artist · Refs · #20 Orange-red crayon scribble
Pastel 1.00 · 14 px · 9.0 s

![Brush Artist · Refs · #20 Orange-red crayon scribble](Brush-Artist-Refs-20-Orange-red-crayon-scribble.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 1 % → 1 % | 3.8 px | 0.53 | 1.00 | 20 |
| heavy line | 3 % → 3 % | 8.0 px | 0.53 | 1.00 | 26 |
| pressure swell | 2 % → 2 % | 7.6 px | 0.55 | 1.00 | 14 |
| fast wave | 6 % → 6 % | 7.3 px | 0.56 | 1.00 | 75 |
| slow wave | 6 % → 6 % | 6.9 px | 0.53 | 1.00 | 65 |
| spiral | 9 % → 9 % | 6.0 px | 0.54 | 1.00 | 102 |
| loop | 5 % → 5 % | 6.1 px | 0.54 | 1.00 | 65 |
| tilted | 2 % → 2 % | 5.6 px | 0.55 | 1.00 | 38 |
| over the wet one | 4 % → 4 % | 6.2 px | 0.55 | 1.00 | 26 |
| long, no reload | 12 % → 12 % | 5.4 px | 0.53 | 1.00 | 151 | quarters: 0.07 → 0.07 → 0.07 → 0.07

Numbers say: light vs heavy: width 3.8 → 8.0 px, dark 0.53 → 0.53; the long stroke does not run out of paint.

## Brush Artist · Refs · #21 Gritty black contours
Gouache 1.00 · 12 px · 17.2 s

![Brush Artist · Refs · #21 Gritty black contours](Brush-Artist-Refs-21-Gritty-black-contours.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 1 % → 0 % | 3.2 px | 0.00 | 0.00 | 60 |
| heavy line | 2 % → 0 % | 6.0 px | 0.00 | 0.00 | 112 |
| pressure swell | 1 % → 0 % | 5.6 px | 0.00 | 0.00 | 68 |
| fast wave | 4 % → 0 % | 4.9 px | 0.00 | 0.00 | 200 |
| slow wave | 4 % → 0 % | 5.1 px | 0.81 | 0.01 | 192 |
| spiral | 7 % → 0 % | 4.6 px | 0.75 | 0.03 | 354 |
| loop | 4 % → 0 % | 5.5 px | 0.80 | 0.09 | 171 |
| tilted | 3 % → 2 % | 7.7 px | 0.66 | 0.84 | 87 |
| over the wet one | 3 % → 0 % | 2.1 px | 0.66 | 0.01 | 85 |
| long, no reload | 5 % → 0 % | 2.2 px | 0.76 | 0.00 | 440 | quarters: 0.07 → 0.03 → 0.03 → 0.02

Numbers say: light vs heavy: width 3.2 → 6.0 px, dark 0.00 → 0.00.

## Brush Artist · Refs · #22 Bold black brush poster
Ink 1.00 · 20 px · 24.9 s

![Brush Artist · Refs · #22 Bold black brush poster](Brush-Artist-Refs-22-Bold-black-brush-poster.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 4 % → 5 % | 10.3 px | 0.79 | 1.52 | 33 |
| heavy line | 15 % → 14 % | 42.6 px | 0.88 | 0.99 | 96 |
| pressure swell | 9 % → 9 % | 33.6 px | 0.87 | 1.03 | 54 |
| fast wave | 28 % → 27 % | 32.3 px | 0.88 | 0.98 | 143 |
| slow wave | 23 % → 23 % | 27.0 px | 0.87 | 0.98 | 181 |
| spiral | 35 % → 32 % | 23.0 px | 0.87 | 0.92 | 241 |
| loop | 22 % → 22 % | 28.2 px | 0.88 | 1.00 | 150 |
| tilted | 9 % → 9 % | 24.2 px | 0.88 | 1.00 | 72 |
| over the wet one | 20 % → 20 % | 30.8 px | 0.88 | 1.00 | 61 |
| long, no reload | 48 % → 38 % | 21.3 px | 0.85 | 0.79 | 355 | quarters: 0.56 → 0.45 → 0.35 → 0.26

Numbers say: light vs heavy: width 10.3 → 42.6 px, dark 0.79 → 0.88; wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #23 Dry white on orange + black line
Gouache 1.00 · 50 px · 21.3 s

![Brush Artist · Refs · #23 Dry white on orange + black line](Brush-Artist-Refs-23-Dry-white-on-orange-black-line.png)

A light paint: laid on a grey sheet (on white it cannot be seen); **dark** = how far it is from the grey either way.

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 3 % → 0 % | 9.9 px | 0.00 | 0.00 | 88 |
| heavy line | 9 % → 2 % | 26.8 px | 0.42 | 0.20 | 203 |
| pressure swell | 7 % → 0 % | 24.9 px | 0.41 | 0.03 | 111 |
| fast wave | 25 % → 0 % | 28.6 px | 0.00 | 0.00 | 403 |
| slow wave | 24 % → 1 % | 27.6 px | 0.40 | 0.02 | 578 |
| spiral | 33 % → 1 % | 21.5 px | 0.40 | 0.02 | 590 |
| loop | 20 % → 0 % | 26.0 px | 0.39 | 0.00 | 316 |
| tilted | 10 % → 9 % | 28.2 px | 0.38 | 0.93 | 196 |
| over the wet one | 15 % → 1 % | 13.1 px | 0.38 | 0.05 | 130 |
| long, no reload | 30 % → 4 % | 13.5 px | 0.40 | 0.12 | 789 | quarters: 0.02 → 0.03 → 0.03 → 0.03

Numbers say: light vs heavy: width 9.9 → 26.8 px, dark 0.00 → 0.42; the long stroke does not run out of paint.

## Brush Artist · Refs · #24 Picasso flat oil
Oil 0.89 · Oil glaze 0.11 · 34 px · 13.9 s

![Brush Artist · Refs · #24 Picasso flat oil](Brush-Artist-Refs-24-Picasso-flat-oil.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 10 % → 10 % | 28.8 px | 0.39 | 1.00 | 106 |
| heavy line | 11 % → 11 % | 32.5 px | 0.39 | 1.00 | 111 |
| pressure swell | 8 % → 8 % | 31.7 px | 0.38 | 1.00 | 96 |
| fast wave | 30 % → 30 % | 35.2 px | 0.39 | 1.00 | 347 |
| slow wave | 28 % → 28 % | 32.8 px | 0.38 | 1.00 | 555 |
| spiral | 42 % → 42 % | 27.8 px | 0.38 | 1.00 | 558 |
| loop | 22 % → 22 % | 28.8 px | 0.40 | 1.00 | 259 |
| tilted | 11 % → 11 % | 31.3 px | 0.41 | 1.00 | 182 |
| over the wet one | 20 % → 20 % | 25.3 px | 0.41 | 1.00 | 122 |
| long, no reload | 58 % → 58 % | 26.0 px | 0.32 | 1.00 | 823 | quarters: 0.23 → 0.22 → 0.19 → 0.17

Numbers say: light vs heavy: width 28.8 → 32.5 px, dark 0.39 → 0.39.

## Brush Artist · Refs · #25 Yellow heavy flat stroke
Impasto 1.00 · 110 px · 32.5 s

![Brush Artist · Refs · #25 Yellow heavy flat stroke](Brush-Artist-Refs-25-Yellow-heavy-flat-stroke.png)

A light paint: laid on a grey sheet (on white it cannot be seen); **dark** = how far it is from the grey either way.

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 35 % → 35 % | 101.0 px | 0.31 | 1.00 | 402 |
| heavy line | 36 % → 35 % | 104.1 px | 0.31 | 0.97 | 402 |
| pressure swell | 28 % → 29 % | 104.0 px | 0.28 | 1.05 | 294 |
| fast wave | 72 % → 75 % | 82.8 px | 0.25 | 1.04 | 1118 |
| slow wave | 72 % → 71 % | 83.7 px | 0.30 | 0.98 | 1840 |
| spiral | 86 % → 81 % | 56.5 px | 0.30 | 0.94 | 1940 |
| loop | 64 % → 63 % | 82.7 px | 0.31 | 0.99 | 932 |
| tilted | 25 % → 25 % | 70.3 px | 0.28 | 1.00 | 619 |
| over the wet one | 55 % → 53 % | 83.3 px | 0.28 | 0.97 | 477 |
| long, no reload | 98 % → 96 % | 43.9 px | 0.31 | 0.98 | 2686 | quarters: 0.00 → 0.00 → 0.00 → 0.00

Numbers say: light vs heavy: width 101.0 → 104.1 px, dark 0.31 → 0.31; pressure barely changes the width; the long stroke does not run out of paint.

## Brush Artist · Refs · #27 Orange impasto swatch
Impasto 1.00 · 60 px · 19.5 s

![Brush Artist · Refs · #27 Orange impasto swatch](Brush-Artist-Refs-27-Orange-impasto-swatch.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 18 % → 18 % | 52.9 px | 0.34 | 0.97 | 175 |
| heavy line | 21 % → 20 % | 60.0 px | 0.34 | 0.95 | 177 |
| pressure swell | 15 % → 15 % | 57.8 px | 0.36 | 0.97 | 142 |
| fast wave | 48 % → 46 % | 55.2 px | 0.37 | 0.97 | 519 |
| slow wave | 46 % → 45 % | 53.6 px | 0.33 | 0.97 | 773 |
| spiral | 68 % → 61 % | 45.1 px | 0.34 | 0.89 | 946 |
| loop | 40 % → 39 % | 51.8 px | 0.33 | 0.97 | 448 |
| tilted | 16 % → 16 % | 43.7 px | 0.35 | 1.00 | 274 |
| over the wet one | 34 % → 32 % | 50.0 px | 0.35 | 0.97 | 220 |
| long, no reload | 84 % → 76 % | 37.8 px | 0.32 | 0.90 | 1302 | quarters: 0.30 → 0.29 → 0.28 → 0.25

Numbers say: light vs heavy: width 52.9 → 60.0 px, dark 0.34 → 0.34.

## Brush Artist · Refs · #28 Miles Davis black lines
Ink 1.00 · 22 px · 25.1 s

![Brush Artist · Refs · #28 Miles Davis black lines](Brush-Artist-Refs-28-Miles-Davis-black-lines.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 4 % → 6 % | 12.3 px | 0.80 | 1.40 | 32 |
| heavy line | 16 % → 16 % | 45.9 px | 0.88 | 0.99 | 85 |
| pressure swell | 10 % → 10 % | 36.7 px | 0.87 | 1.03 | 41 |
| fast wave | 29 % → 29 % | 33.8 px | 0.88 | 0.99 | 118 |
| slow wave | 27 % → 26 % | 30.7 px | 0.88 | 0.99 | 201 |
| spiral | 39 % → 36 % | 25.4 px | 0.87 | 0.93 | 253 |
| loop | 24 % → 24 % | 31.0 px | 0.88 | 1.00 | 129 |
| tilted | 9 % → 9 % | 26.0 px | 0.88 | 1.01 | 64 |
| over the wet one | 21 % → 21 % | 32.9 px | 0.88 | 1.00 | 57 |
| long, no reload | 53 % → 45 % | 23.9 px | 0.85 | 0.83 | 369 | quarters: 0.61 → 0.53 → 0.41 → 0.31

Numbers say: light vs heavy: width 12.3 → 45.9 px, dark 0.80 → 0.88.

## Brush Artist · Refs · #29 Shrigley magenta asterisk
Watercolour 1.00 · 70 px · 28.6 s

![Brush Artist · Refs · #29 Shrigley magenta asterisk](Brush-Artist-Refs-29-Shrigley-magenta-asterisk.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 10 % → 13 % | 28.0 px | 0.61 | 1.39 | 57 |
| heavy line | 17 % → 18 % | 50.3 px | 0.61 | 1.04 | 127 |
| pressure swell | 11 % → 13 % | 41.1 px | 0.62 | 1.14 | 69 |
| fast wave | 38 % → 38 % | 43.8 px | 0.60 | 1.01 | 253 |
| slow wave | 35 % → 39 % | 41.0 px | 0.62 | 1.11 | 403 |
| spiral | 61 % → 61 % | 40.0 px | 0.60 | 1.01 | 395 |
| loop | 31 % → 32 % | 40.2 px | 0.61 | 1.03 | 217 |
| tilted | 18 % → 18 % | 49.0 px | 0.61 | 1.00 | 186 |
| over the wet one | 31 % → 34 % | 38.5 px | 0.61 | 1.08 | 88 |
| long, no reload | 75 % → 76 % | 33.6 px | 0.60 | 1.01 | 696 | quarters: 0.53 → 0.50 → 0.48 → 0.45

Numbers say: light vs heavy: width 28.0 → 50.3 px, dark 0.61 → 0.61; the long stroke does not run out of paint.

## Brush Artist · Refs · #30 Red gouache face patch
Gouache 1.00 · 60 px · 35.9 s

![Brush Artist · Refs · #30 Red gouache face patch](Brush-Artist-Refs-30-Red-gouache-face-patch.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 16 % → 14 % | 45.5 px | 0.49 | 0.87 | 147 |
| heavy line | 25 % → 19 % | 71.4 px | 0.49 | 0.78 | 193 |
| pressure swell | 20 % → 17 % | 74.8 px | 0.50 | 0.84 | 140 |
| fast wave | 48 % → 28 % | 55.1 px | 0.51 | 0.58 | 475 |
| slow wave | 50 % → 31 % | 57.3 px | 0.48 | 0.62 | 709 |
| spiral | 59 % → 30 % | 39.0 px | 0.48 | 0.50 | 717 |
| loop | 40 % → 28 % | 51.4 px | 0.48 | 0.71 | 378 |
| tilted | 17 % → 17 % | 46.7 px | 0.50 | 1.00 | 248 |
| over the wet one | 37 % → 32 % | 55.9 px | 0.50 | 0.87 | 177 |
| long, no reload | 66 % → 28 % | 29.6 px | 0.46 | 0.42 | 1032 | quarters: 0.40 → 0.36 → 0.31 → 0.26

Numbers say: light vs heavy: width 45.5 → 71.4 px, dark 0.49 → 0.49.

## Brush Artist · Refs · #31 Warhol blotted line
Ink 1.00 · 6 px · 19.7 s

![Brush Artist · Refs · #31 Warhol blotted line](Brush-Artist-Refs-31-Warhol-blotted-line.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 1 % → 4 % | 3.0 px | 0.72 | 3.49 | 32 |
| heavy line | 7 % → 7 % | 19.5 px | 0.84 | 0.98 | 51 |
| pressure swell | 4 % → 4 % | 14.2 px | 0.82 | 1.18 | 32 |
| fast wave | 12 % → 9 % | 13.6 px | 0.81 | 0.73 | 96 |
| slow wave | 11 % → 9 % | 12.3 px | 0.80 | 0.80 | 109 |
| spiral | 15 % → 9 % | 10.0 px | 0.79 | 0.58 | 175 |
| loop | 10 % → 9 % | 12.6 px | 0.80 | 0.94 | 81 |
| tilted | 4 % → 4 % | 11.0 px | 0.83 | 1.03 | 44 |
| over the wet one | 9 % → 9 % | 14.0 px | 0.83 | 1.05 | 39 |
| long, no reload | 21 % → 10 % | 9.5 px | 0.78 | 0.45 | 221 | quarters: 0.25 → 0.13 → 0.05 → 0.01

Numbers say: light vs heavy: width 3.0 → 19.5 px, dark 0.72 → 0.84; wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #32 Thick orange swipes
Impasto 1.00 · 90 px · 27.9 s

![Brush Artist · Refs · #32 Thick orange swipes](Brush-Artist-Refs-32-Thick-orange-swipes.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 29 % → 28 % | 83.5 px | 0.37 | 0.99 | 297 |
| heavy line | 30 % → 29 % | 86.8 px | 0.37 | 0.97 | 313 |
| pressure swell | 23 % → 23 % | 84.8 px | 0.38 | 1.01 | 252 |
| fast wave | 64 % → 65 % | 74.2 px | 0.39 | 1.02 | 850 |
| slow wave | 64 % → 62 % | 73.9 px | 0.37 | 0.97 | 1393 |
| spiral | 80 % → 75 % | 52.6 px | 0.35 | 0.94 | 1498 |
| loop | 56 % → 55 % | 73.0 px | 0.36 | 0.97 | 767 |
| tilted | 21 % → 21 % | 58.8 px | 0.38 | 1.00 | 429 |
| over the wet one | 46 % → 45 % | 70.6 px | 0.38 | 0.96 | 345 |
| long, no reload | 95 % → 92 % | 42.8 px | 0.36 | 0.97 | 2050 | quarters: 0.35 → 0.35 → 0.35 → 0.34

Numbers say: light vs heavy: width 83.5 → 86.8 px, dark 0.37 → 0.37; pressure barely changes the width; the long stroke does not run out of paint.

## Brush Artist · Refs · #33 Red wet-in-wet band
Watercolour 1.00 · 80 px · 42.1 s

![Brush Artist · Refs · #33 Red wet-in-wet band](Brush-Artist-Refs-33-Red-wet-in-wet-band.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 24 % → 42 % | 69.3 px | 0.54 | 1.75 | 140 |
| heavy line | 33 % → 48 % | 96.9 px | 0.55 | 1.45 | 214 |
| pressure swell | 19 % → 30 % | 72.1 px | 0.57 | 1.56 | 134 |
| fast wave | 65 % → 79 % | 75.5 px | 0.60 | 1.21 | 456 |
| slow wave | 61 % → 78 % | 70.5 px | 0.63 | 1.28 | 755 |
| spiral | 77 % → 89 % | 50.8 px | 0.64 | 1.15 | 719 |
| loop | 54 % → 67 % | 70.5 px | 0.62 | 1.23 | 386 |
| tilted | 28 % → 30 % | 78.0 px | 0.58 | 1.09 | 231 |
| over the wet one | 55 % → 79 % | 76.7 px | 0.58 | 1.43 | 175 |
| long, no reload | 96 % → 99 % | 42.9 px | 0.66 | 1.04 | 1088 | quarters: 0.68 → 0.68 → 0.68 → 0.64

Numbers say: light vs heavy: width 69.3 → 96.9 px, dark 0.54 → 0.55; the long stroke does not run out of paint; wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #34 Magenta oil patches
Oil 0.89 · Oil glaze 0.11 · 60 px · 16.7 s

![Brush Artist · Refs · #34 Magenta oil patches](Brush-Artist-Refs-34-Magenta-oil-patches.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 18 % → 18 % | 51.4 px | 0.61 | 1.00 | 191 |
| heavy line | 19 % → 19 % | 55.1 px | 0.61 | 1.00 | 217 |
| pressure swell | 15 % → 15 % | 54.6 px | 0.61 | 1.01 | 146 |
| fast wave | 44 % → 45 % | 51.1 px | 0.61 | 1.02 | 570 |
| slow wave | 45 % → 45 % | 52.4 px | 0.61 | 1.00 | 899 |
| spiral | 68 % → 68 % | 44.9 px | 0.58 | 1.00 | 973 |
| loop | 42 % → 42 % | 54.2 px | 0.61 | 1.00 | 464 |
| tilted | 17 % → 17 % | 46.3 px | 0.61 | 1.00 | 317 |
| over the wet one | 34 % → 34 % | 48.4 px | 0.61 | 1.00 | 244 |
| long, no reload | 83 % → 83 % | 37.1 px | 0.59 | 1.00 | 1463 | quarters: 0.54 → 0.54 → 0.53 → 0.47

Numbers say: light vs heavy: width 51.4 → 55.1 px, dark 0.61 → 0.61; pressure barely changes the width; the long stroke does not run out of paint.

## Brush Artist · Refs · #35 Red band with runs
Watercolour 1.00 · 70 px · 44.4 s

![Brush Artist · Refs · #35 Red band with runs](Brush-Artist-Refs-35-Red-band-with-runs.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 40 % → 45 % | 115.3 px | 0.42 | 1.14 | 141 |
| heavy line | 45 % → 50 % | 132.0 px | 0.42 | 1.09 | 241 |
| pressure swell | 20 % → 28 % | 76.7 px | 0.48 | 1.37 | 145 |
| fast wave | 66 % → 76 % | 76.8 px | 0.49 | 1.14 | 538 |
| slow wave | 65 % → 76 % | 75.6 px | 0.52 | 1.16 | 830 |
| spiral | 86 % → 94 % | 56.9 px | 0.53 | 1.09 | 668 |
| loop | 79 % → 88 % | 102.7 px | 0.49 | 1.11 | 344 |
| tilted | 50 % → 51 % | 139.1 px | 0.47 | 1.02 | 215 |
| over the wet one | 78 % → 84 % | 77.5 px | 0.47 | 1.09 | 157 |
| long, no reload | 96 % → 100 % | 43.2 px | 0.58 | 1.04 | 1017 | quarters: 0.59 → 0.60 → 0.59 → 0.56

Numbers say: light vs heavy: width 115.3 → 132.0 px, dark 0.42 → 0.42; the long stroke does not run out of paint.

## Brush Artist · Refs · #36 Magenta letters flat brush
Gouache 1.00 · 36 px · 30.6 s

![Brush Artist · Refs · #36 Magenta letters flat brush](Brush-Artist-Refs-36-Magenta-letters-flat-brush.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 10 % → 10 % | 29.6 px | 0.45 | 0.94 | 73 |
| heavy line | 16 % → 13 % | 47.5 px | 0.45 | 0.78 | 104 |
| pressure swell | 13 % → 11 % | 48.4 px | 0.47 | 0.85 | 85 |
| fast wave | 34 % → 16 % | 39.3 px | 0.47 | 0.48 | 279 |
| slow wave | 35 % → 20 % | 40.5 px | 0.45 | 0.57 | 380 |
| spiral | 46 % → 19 % | 30.6 px | 0.44 | 0.41 | 382 |
| loop | 27 % → 18 % | 35.0 px | 0.45 | 0.67 | 206 |
| tilted | 12 % → 12 % | 32.8 px | 0.47 | 1.00 | 123 |
| over the wet one | 26 % → 22 % | 38.5 px | 0.47 | 0.88 | 92 |
| long, no reload | 49 % → 19 % | 22.0 px | 0.44 | 0.39 | 598 | quarters: 0.30 → 0.27 → 0.22 → 0.18

Numbers say: light vs heavy: width 29.6 → 47.5 px, dark 0.45 → 0.45.

## Brush Artist · Refs · #37 Oil still life dabs
Oil 0.89 · Oil glaze 0.11 · 40 px · 14.0 s

![Brush Artist · Refs · #37 Oil still life dabs](Brush-Artist-Refs-37-Oil-still-life-dabs.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 11 % → 11 % | 32.1 px | 0.36 | 1.00 | 140 |
| heavy line | 12 % → 12 % | 36.1 px | 0.39 | 1.00 | 145 |
| pressure swell | 10 % → 10 % | 39.3 px | 0.40 | 1.00 | 103 |
| fast wave | 30 % → 30 % | 35.0 px | 0.39 | 1.00 | 368 |
| slow wave | 35 % → 35 % | 40.6 px | 0.37 | 1.00 | 631 |
| spiral | 52 % → 52 % | 34.4 px | 0.38 | 1.00 | 625 |
| loop | 29 % → 29 % | 36.9 px | 0.39 | 1.00 | 309 |
| tilted | 12 % → 12 % | 34.7 px | 0.41 | 1.00 | 183 |
| over the wet one | 23 % → 23 % | 30.6 px | 0.41 | 1.00 | 151 |
| long, no reload | 59 % → 59 % | 26.6 px | 0.31 | 1.00 | 911 | quarters: 0.23 → 0.22 → 0.20 → 0.17

Numbers say: light vs heavy: width 32.1 → 36.1 px, dark 0.36 → 0.39.

## Brush Artist · Refs · #38 Sanguine drawing
Pastel 1.00 · 6 px · 8.3 s

![Brush Artist · Refs · #38 Sanguine drawing](Brush-Artist-Refs-38-Sanguine-drawing.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 1 % → 1 % | 2.1 px | 0.61 | 1.00 | 11 |
| heavy line | 1 % → 1 % | 3.9 px | 0.61 | 1.00 | 15 |
| pressure swell | 1 % → 1 % | 3.8 px | 0.61 | 1.00 | 7 |
| fast wave | 3 % → 3 % | 3.4 px | 0.61 | 1.00 | 35 |
| slow wave | 3 % → 3 % | 3.4 px | 0.61 | 1.00 | 31 |
| spiral | 4 % → 4 % | 2.8 px | 0.61 | 1.00 | 58 |
| loop | 2 % → 2 % | 3.1 px | 0.61 | 1.00 | 40 |
| tilted | 1 % → 1 % | 3.4 px | 0.61 | 1.00 | 16 |
| over the wet one | 2 % → 2 % | 2.9 px | 0.61 | 1.00 | 20 |
| long, no reload | 6 % → 6 % | 2.7 px | 0.61 | 1.00 | 89 | quarters: 0.04 → 0.04 → 0.04 → 0.04

Numbers say: light vs heavy: width 2.1 → 3.9 px, dark 0.61 → 0.61; the long stroke does not run out of paint.

## Brush Artist · Refs · #39 Very thick impasto
Impasto 1.00 · 60 px · 19.3 s

![Brush Artist · Refs · #39 Very thick impasto](Brush-Artist-Refs-39-Very-thick-impasto.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 18 % → 18 % | 53.1 px | 0.61 | 0.97 | 161 |
| heavy line | 21 % → 20 % | 60.0 px | 0.62 | 0.96 | 177 |
| pressure swell | 15 % → 15 % | 58.1 px | 0.62 | 0.97 | 128 |
| fast wave | 48 % → 47 % | 55.3 px | 0.63 | 0.98 | 487 |
| slow wave | 47 % → 45 % | 53.9 px | 0.61 | 0.97 | 782 |
| spiral | 69 % → 63 % | 45.3 px | 0.61 | 0.92 | 864 |
| loop | 40 % → 39 % | 52.1 px | 0.61 | 0.97 | 413 |
| tilted | 16 % → 16 % | 43.8 px | 0.62 | 1.00 | 248 |
| over the wet one | 34 % → 33 % | 50.1 px | 0.62 | 0.97 | 211 |
| long, no reload | 85 % → 79 % | 38.0 px | 0.60 | 0.93 | 1222 | quarters: 0.56 → 0.55 → 0.54 → 0.51

Numbers say: light vs heavy: width 53.1 → 60.0 px, dark 0.61 → 0.62; the long stroke does not run out of paint.

## Brush Artist · Refs · #40 Watercolour blooms
Watercolour 1.00 · 90 px · 47.2 s

![Brush Artist · Refs · #40 Watercolour blooms](Brush-Artist-Refs-40-Watercolour-blooms.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 27 % → 47 % | 78.4 px | 0.08 | 1.72 | 144 |
| heavy line | 38 % → 51 % | 110.0 px | 0.09 | 1.36 | 255 |
| pressure swell | 24 % → 39 % | 91.8 px | 0.09 | 1.61 | 161 |
| fast wave | 68 % → 82 % | 78.3 px | 0.11 | 1.21 | 527 |
| slow wave | 68 % → 81 % | 79.1 px | 0.15 | 1.18 | 913 |
| spiral | 81 % → 92 % | 53.5 px | 0.14 | 1.14 | 885 |
| loop | 58 % → 72 % | 75.3 px | 0.13 | 1.24 | 463 |
| tilted | 34 % → 36 % | 94.8 px | 0.11 | 1.07 | 285 |
| over the wet one | 62 % → 81 % | 78.2 px | 0.11 | 1.31 | 177 |
| long, no reload | 97 % → 100 % | 43.6 px | 0.17 | 1.03 | 1243 | quarters: 0.21 → 0.20 → 0.17 → 0.13

Numbers say: light vs heavy: width 78.4 → 110.0 px, dark 0.08 → 0.09; wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #41 Coloured pencil hatching
Pastel 1.00 · 4 px · 8.3 s

![Brush Artist · Refs · #41 Coloured pencil hatching](Brush-Artist-Refs-41-Coloured-pencil-hatching.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 1 % → 1 % | 1.6 px | 0.43 | 1.00 | 9 |
| heavy line | 1 % → 1 % | 2.9 px | 0.43 | 1.00 | 8 |
| pressure swell | 1 % → 1 % | 2.8 px | 0.43 | 1.00 | 6 |
| fast wave | 2 % → 2 % | 2.5 px | 0.43 | 1.00 | 30 |
| slow wave | 2 % → 2 % | 2.5 px | 0.43 | 1.00 | 27 |
| spiral | 3 % → 3 % | 2.1 px | 0.43 | 1.00 | 52 |
| loop | 2 % → 2 % | 2.3 px | 0.43 | 1.00 | 26 |
| tilted | 1 % → 1 % | 3.0 px | 0.43 | 1.00 | 18 |
| over the wet one | 2 % → 2 % | 2.3 px | 0.43 | 1.00 | 13 |
| long, no reload | 5 % → 5 % | 2.0 px | 0.42 | 1.00 | 60 | quarters: 0.02 → 0.02 → 0.02 → 0.02

Numbers say: light vs heavy: width 1.6 → 2.9 px, dark 0.43 → 0.43; the long stroke does not run out of paint.

## Brush Artist · Refs · #42 Oil pastel shaggy
Pastel 1.00 · 18 px · 8.8 s

![Brush Artist · Refs · #42 Oil pastel shaggy](Brush-Artist-Refs-42-Oil-pastel-shaggy.png)

A light paint: laid on a grey sheet (on white it cannot be seen); **dark** = how far it is from the grey either way.

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 2 % → 2 % | 4.7 px | 0.36 | 1.00 | 18 |
| heavy line | 3 % → 3 % | 10.0 px | 0.36 | 1.00 | 23 |
| pressure swell | 2 % → 2 % | 9.3 px | 0.34 | 1.00 | 16 |
| fast wave | 8 % → 8 % | 9.2 px | 0.32 | 1.00 | 61 |
| slow wave | 7 % → 7 % | 8.6 px | 0.37 | 1.00 | 74 |
| spiral | 11 % → 11 % | 7.5 px | 0.36 | 1.00 | 104 |
| loop | 6 % → 6 % | 7.8 px | 0.35 | 1.00 | 55 |
| tilted | 2 % → 2 % | 6.5 px | 0.33 | 1.00 | 33 |
| over the wet one | 5 % → 5 % | 7.6 px | 0.33 | 1.00 | 25 |
| long, no reload | 15 % → 15 % | 6.5 px | 0.37 | 1.00 | 149 | quarters: 0.00 → 0.00 → 0.00 → 0.00

Numbers say: light vs heavy: width 4.7 → 10.0 px, dark 0.36 → 0.36; the long stroke does not run out of paint.

## Brush Artist · Refs · #43 Dragged black ink blocks
Gouache 1.00 · 70 px · 23.2 s

![Brush Artist · Refs · #43 Dragged black ink blocks](Brush-Artist-Refs-43-Dragged-black-ink-blocks.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 5 % → 0 % | 14.8 px | 0.00 | 0.00 | 99 |
| heavy line | 14 % → 4 % | 40.5 px | 0.66 | 0.27 | 286 |
| pressure swell | 11 % → 4 % | 42.1 px | 0.65 | 0.33 | 163 |
| fast wave | 38 % → 1 % | 43.8 px | 0.66 | 0.03 | 558 |
| slow wave | 32 % → 2 % | 36.6 px | 0.57 | 0.05 | 875 |
| spiral | 51 % → 4 % | 33.4 px | 0.54 | 0.07 | 890 |
| loop | 30 % → 2 % | 38.3 px | 0.62 | 0.06 | 466 |
| tilted | 13 % → 13 % | 37.0 px | 0.66 | 0.95 | 249 |
| over the wet one | 21 % → 2 % | 22.9 px | 0.66 | 0.10 | 204 |
| long, no reload | 44 % → 7 % | 19.8 px | 0.66 | 0.16 | 1093 | quarters: 0.47 → 0.37 → 0.18 → 0.13

Numbers say: light vs heavy: width 14.8 → 40.5 px, dark 0.00 → 0.66.

## Brush Artist · Refs · #44 Blue looping ribbon
Oil 1.00 · 80 px · 24.5 s

![Brush Artist · Refs · #44 Blue looping ribbon](Brush-Artist-Refs-44-Blue-looping-ribbon.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 25 % → 26 % | 73.1 px | 0.72 | 1.04 | 248 |
| heavy line | 27 % → 27 % | 77.7 px | 0.71 | 1.00 | 290 |
| pressure swell | 20 % → 21 % | 76.5 px | 0.71 | 1.03 | 214 |
| fast wave | 62 % → 64 % | 71.4 px | 0.71 | 1.04 | 778 |
| slow wave | 58 % → 58 % | 67.4 px | 0.70 | 1.00 | 1222 |
| spiral | 76 % → 77 % | 50.3 px | 0.69 | 1.00 | 1372 |
| loop | 53 % → 53 % | 69.2 px | 0.69 | 1.00 | 690 |
| tilted | 20 % → 20 % | 56.1 px | 0.74 | 1.00 | 374 |
| over the wet one | 41 % → 41 % | 58.7 px | 0.74 | 1.00 | 302 |
| long, no reload | 90 % → 90 % | 40.1 px | 0.69 | 1.00 | 1974 | quarters: 0.67 → 0.68 → 0.66 → 0.59

Numbers say: light vs heavy: width 73.1 → 77.7 px, dark 0.72 → 0.71; pressure barely changes the width; the long stroke does not run out of paint.

## Brush Artist · Refs · #45 Soft pastel pepper
Pastel 1.00 · 40 px · 9.4 s

![Brush Artist · Refs · #45 Soft pastel pepper](Brush-Artist-Refs-45-Soft-pastel-pepper.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 4 % → 4 % | 11.0 px | 0.53 | 1.00 | 39 |
| heavy line | 7 % → 7 % | 21.2 px | 0.53 | 1.00 | 43 |
| pressure swell | 5 % → 5 % | 19.0 px | 0.55 | 1.00 | 35 |
| fast wave | 17 % → 17 % | 19.3 px | 0.56 | 1.00 | 120 |
| slow wave | 16 % → 16 % | 18.0 px | 0.54 | 1.00 | 209 |
| spiral | 23 % → 23 % | 15.4 px | 0.54 | 1.00 | 205 |
| loop | 12 % → 12 % | 15.4 px | 0.54 | 1.00 | 103 |
| tilted | 4 % → 4 % | 11.4 px | 0.55 | 1.00 | 60 |
| over the wet one | 10 % → 10 % | 16.7 px | 0.55 | 1.00 | 48 |
| long, no reload | 28 % → 28 % | 12.6 px | 0.53 | 1.00 | 303 | quarters: 0.17 → 0.16 → 0.17 → 0.17

Numbers say: light vs heavy: width 11.0 → 21.2 px, dark 0.53 → 0.53; the long stroke does not run out of paint.

## Brush Artist · Refs · #46 Red-brown ink lips
Watercolour 1.00 · 50 px · 39.9 s

![Brush Artist · Refs · #46 Red-brown ink lips](Brush-Artist-Refs-46-Red-brown-ink-lips.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 15 % → 31 % | 43.9 px | 0.59 | 2.04 | 64 |
| heavy line | 22 % → 35 % | 63.4 px | 0.60 | 1.58 | 87 |
| pressure swell | 13 % → 22 % | 50.3 px | 0.63 | 1.64 | 66 |
| fast wave | 43 % → 64 % | 49.7 px | 0.64 | 1.50 | 213 |
| slow wave | 42 % → 63 % | 49.1 px | 0.67 | 1.49 | 358 |
| spiral | 65 % → 79 % | 42.6 px | 0.69 | 1.22 | 352 |
| loop | 38 % → 55 % | 48.8 px | 0.67 | 1.47 | 193 |
| tilted | 21 % → 23 % | 58.2 px | 0.60 | 1.11 | 118 |
| over the wet one | 42 % → 63 % | 58.5 px | 0.60 | 1.51 | 87 |
| long, no reload | 78 % → 95 % | 35.1 px | 0.70 | 1.21 | 533 | quarters: 0.71 → 0.71 → 0.69 → 0.65

Numbers say: light vs heavy: width 43.9 → 63.4 px, dark 0.59 → 0.60; the long stroke does not run out of paint; wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #47 Pink knife slabs
Impasto 1.00 · 90 px · 28.4 s

![Brush Artist · Refs · #47 Pink knife slabs](Brush-Artist-Refs-47-Pink-knife-slabs.png)

A light paint: laid on a grey sheet (on white it cannot be seen); **dark** = how far it is from the grey either way.

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 27 % → 26 % | 78.7 px | 0.29 | 0.97 | 204 |
| heavy line | 29 % → 28 % | 84.6 px | 0.29 | 0.96 | 231 |
| pressure swell | 22 % → 22 % | 81.2 px | 0.26 | 1.01 | 160 |
| fast wave | 62 % → 61 % | 71.8 px | 0.24 | 0.98 | 585 |
| slow wave | 62 % → 58 % | 71.5 px | 0.28 | 0.94 | 957 |
| spiral | 75 % → 60 % | 49.3 px | 0.28 | 0.80 | 1055 |
| loop | 56 % → 54 % | 72.1 px | 0.29 | 0.97 | 520 |
| tilted | 22 % → 22 % | 60.2 px | 0.25 | 1.00 | 351 |
| over the wet one | 46 % → 44 % | 69.3 px | 0.25 | 0.96 | 255 |
| long, no reload | 93 % → 77 % | 41.9 px | 0.26 | 0.83 | 1544 | quarters: 0.00 → 0.00 → 0.00 → 0.00

Numbers say: light vs heavy: width 78.7 → 84.6 px, dark 0.29 → 0.29; pressure barely changes the width; the long stroke does not run out of paint.

## Brush Artist · Refs · #48 Black bands with drips
Gouache 1.00 · 70 px · 48.3 s

![Brush Artist · Refs · #48 Black bands with drips](Brush-Artist-Refs-48-Black-bands-with-drips.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 28 % → 23 % | 80.2 px | 0.63 | 0.82 | 175 |
| heavy line | 35 % → 26 % | 100.7 px | 0.64 | 0.75 | 238 |
| pressure swell | 25 % → 21 % | 93.8 px | 0.63 | 0.85 | 171 |
| fast wave | 63 % → 41 % | 72.9 px | 0.63 | 0.64 | 528 |
| slow wave | 62 % → 41 % | 71.5 px | 0.63 | 0.66 | 881 |
| spiral | 69 % → 40 % | 45.7 px | 0.61 | 0.57 | 989 |
| loop | 54 % → 40 % | 69.9 px | 0.63 | 0.74 | 465 |
| tilted | 29 % → 29 % | 80.5 px | 0.62 | 1.01 | 530 |
| over the wet one | 59 % → 48 % | 82.9 px | 0.62 | 0.82 | 1045 |
| long, no reload | 78 % → 37 % | 34.9 px | 0.61 | 0.47 | 1535 | quarters: 0.58 → 0.54 → 0.47 → 0.39

Numbers say: light vs heavy: width 80.2 → 100.7 px, dark 0.63 → 0.64.

## Brush Artist · Refs · #49 Magenta letters round brush
Ink 1.00 · 30 px · 31.2 s

![Brush Artist · Refs · #49 Magenta letters round brush](Brush-Artist-Refs-49-Magenta-letters-round-brush.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 6 % → 8 % | 18.1 px | 0.49 | 1.21 | 31 |
| heavy line | 21 % → 20 % | 60.3 px | 0.51 | 0.98 | 100 |
| pressure swell | 13 % → 13 % | 47.1 px | 0.51 | 1.01 | 59 |
| fast wave | 38 % → 38 % | 44.0 px | 0.51 | 1.00 | 175 |
| slow wave | 34 % → 34 % | 39.4 px | 0.51 | 0.99 | 280 |
| spiral | 49 % → 48 % | 32.6 px | 0.51 | 0.96 | 272 |
| loop | 30 % → 30 % | 38.3 px | 0.51 | 1.00 | 138 |
| tilted | 11 % → 12 % | 32.0 px | 0.52 | 1.00 | 90 |
| over the wet one | 27 % → 27 % | 42.2 px | 0.52 | 1.01 | 66 |
| long, no reload | 63 % → 56 % | 28.2 px | 0.50 | 0.90 | 415 | quarters: 0.42 → 0.37 → 0.30 → 0.25

Numbers say: light vs heavy: width 18.1 → 60.3 px, dark 0.49 → 0.51.

## Brush Artist · Refs · #50 Thick swipes on photo
Impasto 1.00 · 40 px · 17.8 s

![Brush Artist · Refs · #50 Thick swipes on photo](Brush-Artist-Refs-50-Thick-swipes-on-photo.png)

A light paint: laid on a grey sheet (on white it cannot be seen); **dark** = how far it is from the grey either way.

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 13 % → 13 % | 38.6 px | 0.27 | 0.95 | 105 |
| heavy line | 14 % → 13 % | 40.0 px | 0.27 | 0.96 | 122 |
| pressure swell | 11 % → 10 % | 40.1 px | 0.24 | 0.95 | 83 |
| fast wave | 35 % → 31 % | 40.1 px | 0.24 | 0.89 | 295 |
| slow wave | 34 % → 32 % | 39.5 px | 0.26 | 0.93 | 600 |
| spiral | 58 % → 46 % | 38.5 px | 0.29 | 0.79 | 517 |
| loop | 29 % → 28 % | 37.4 px | 0.26 | 0.96 | 271 |
| tilted | 12 % → 12 % | 33.6 px | 0.22 | 1.00 | 158 |
| over the wet one | 25 % → 24 % | 36.7 px | 0.22 | 0.96 | 133 |
| long, no reload | 68 % → 46 % | 30.4 px | 0.26 | 0.68 | 749 | quarters: 0.00 → 0.00 → 0.00 → 0.00

Numbers say: light vs heavy: width 38.6 → 40.0 px, dark 0.27 → 0.27; pressure barely changes the width.

## Brush Artist · Refs · Drag #e8b4a8
Gouache 1.00 · 40 px · 17.6 s

![Brush Artist · Refs · Drag #e8b4a8](Brush-Artist-Refs-Drag-e8b4a8.png)

A light paint: laid on a grey sheet (on white it cannot be seen); **dark** = how far it is from the grey either way.

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 3 % → 0 % | 9.3 px | 0.00 | 0.00 | 112 |
| heavy line | 6 % → 0 % | 16.2 px | 0.34 | 0.01 | 113 |
| pressure swell | 3 % → 0 % | 12.9 px | 0.00 | 0.00 | 84 |
| fast wave | 16 % → 0 % | 18.1 px | 0.00 | 0.00 | 285 |
| slow wave | 13 % → 0 % | 15.0 px | 0.00 | 0.00 | 479 |
| spiral | 20 % → 0 % | 13.4 px | 0.00 | 0.00 | 454 |
| loop | 13 % → 0 % | 17.1 px | 0.00 | 0.00 | 252 |
| tilted | 6 % → 5 % | 16.8 px | 0.00 | 0.77 | 132 |
| over the wet one | 7 % → 0 % | 1.8 px | 0.00 | 0.00 | 98 |
| long, no reload | 10 % → 0 % | 4.6 px | 0.00 | 0.00 | 856 | quarters: 0.02 → 0.02 → 0.02 → 0.02

Numbers say: light vs heavy: width 9.3 → 16.2 px, dark 0.00 → 0.34; the long stroke does not run out of paint.

## Brush Artist · Refs · Drag #e8e4e0
Gouache 1.00 · 40 px · 18.9 s

![Brush Artist · Refs · Drag #e8e4e0](Brush-Artist-Refs-Drag-e8e4e0.png)

A light paint: laid on a grey sheet (on white it cannot be seen); **dark** = how far it is from the grey either way.

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 3 % → 0 % | 9.3 px | 0.00 | 0.00 | 86 |
| heavy line | 6 % → 0 % | 16.2 px | 0.43 | 0.01 | 231 |
| pressure swell | 3 % → 0 % | 12.9 px | 0.00 | 0.00 | 91 |
| fast wave | 16 % → 0 % | 18.1 px | 0.00 | 0.00 | 305 |
| slow wave | 13 % → 0 % | 15.0 px | 0.00 | 0.00 | 635 |
| spiral | 20 % → 0 % | 13.4 px | 0.00 | 0.00 | 532 |
| loop | 13 % → 0 % | 17.1 px | 0.00 | 0.00 | 238 |
| tilted | 6 % → 5 % | 16.8 px | 0.00 | 0.77 | 155 |
| over the wet one | 7 % → 0 % | 1.8 px | 0.00 | 0.00 | 122 |
| long, no reload | 10 % → 0 % | 4.6 px | 0.00 | 0.00 | 734 | quarters: 0.02 → 0.02 → 0.02 → 0.02

Numbers say: light vs heavy: width 9.3 → 16.2 px, dark 0.00 → 0.43; the long stroke does not run out of paint.

## Brush Artist · Refs · Finger
Pastel 1.00 · 36 px · 23.4 s · over bands of wet oil paint and oil pastel in turn (it works on paint already there: look at what it does to the bands; covered counts the bands too)

![Brush Artist · Refs · Finger](Brush-Artist-Refs-Finger.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 26 % → 26 % | 74.4 px | 0.80 | 1.00 | 36 |
| heavy line | 27 % → 27 % | 79.3 px | 0.80 | 1.00 | 47 |
| pressure swell | 26 % → 26 % | 98.0 px | 0.80 | 1.00 | 54 |
| fast wave | 33 % → 33 % | 38.0 px | 0.78 | 1.00 | 139 |
| slow wave | 31 % → 31 % | 36.3 px | 0.78 | 1.00 | 216 |
| spiral | 38 % → 38 % | 25.3 px | 0.76 | 1.00 | 234 |
| loop | 31 % → 31 % | 39.5 px | 0.79 | 1.00 | 132 |
| tilted | 26 % → 26 % | 73.5 px | 0.78 | 1.00 | 59 |
| over the wet one | 29 % → 29 % | 7.5 px | 0.78 | 1.00 | 50 |
| long, no reload | 39 % → 39 % | 17.4 px | 0.76 | 1.00 | 330 | quarters: 0.24 → 0.36 → 0.32 → 0.37

Numbers say: light vs heavy: width 74.4 → 79.3 px, dark 0.80 → 0.80; pressure barely changes the width; the long stroke does not run out of paint.

## Brush Artist · Ink — wash
Watercolour 1.00 · 38 px · 35.0 s

![Brush Artist · Ink — wash](Brush-Artist-Ink-wash.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 11 % → 11 % | 31.6 px | 0.39 | 1.04 | 67 |
| heavy line | 19 % → 19 % | 54.3 px | 0.32 | 1.03 | 91 |
| pressure swell | 12 % → 13 % | 45.2 px | 0.37 | 1.04 | 53 |
| fast wave | 39 % → 41 % | 45.5 px | 0.31 | 1.04 | 179 |
| slow wave | 37 % → 38 % | 42.9 px | 0.37 | 1.03 | 400 |
| spiral | 58 % → 61 % | 38.6 px | 0.31 | 1.04 | 336 |
| loop | 32 % → 33 % | 41.9 px | 0.35 | 1.02 | 187 |
| tilted | 13 % → 14 % | 37.0 px | 0.38 | 1.04 | 139 |
| over the wet one | 29 % → 30 % | 42.8 px | 0.38 | 1.04 | 89 |
| long, no reload | 67 % → 72 % | 30.0 px | 0.29 | 1.07 | 508 | quarters: 0.34 → 0.27 → 0.19 → 0.12

Numbers say: light vs heavy: width 31.6 → 54.3 px, dark 0.39 → 0.32.

## Brush Artist · Ink — brush line
Ink 1.00 · 16 px · 30.1 s

![Brush Artist · Ink — brush line](Brush-Artist-Ink-brush-line.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 3 % → 5 % | 8.2 px | 0.77 | 1.72 | 48 |
| heavy line | 12 % → 12 % | 35.2 px | 0.88 | 0.99 | 77 |
| pressure swell | 8 % → 8 % | 28.5 px | 0.86 | 1.06 | 61 |
| fast wave | 24 % → 24 % | 28.2 px | 0.87 | 0.98 | 225 |
| slow wave | 20 % → 20 % | 23.7 px | 0.87 | 0.97 | 213 |
| spiral | 31 % → 27 % | 20.3 px | 0.86 | 0.87 | 274 |
| loop | 19 % → 19 % | 24.3 px | 0.87 | 0.99 | 136 |
| tilted | 8 % → 8 % | 21.2 px | 0.88 | 1.01 | 73 |
| over the wet one | 17 % → 17 % | 26.2 px | 0.88 | 1.01 | 86 |
| long, no reload | 44 % → 31 % | 19.7 px | 0.84 | 0.70 | 405 | quarters: 0.51 → 0.41 → 0.30 → 0.20

Numbers say: light vs heavy: width 8.2 → 35.2 px, dark 0.77 → 0.88; wet paint spreads well beyond the stroke.

## Brush Artist · Ink — dry brush
Gouache 1.00 · 30 px · 22.6 s

![Brush Artist · Ink — dry brush](Brush-Artist-Ink-dry-brush.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 2 % → 0 % | 5.7 px | 0.00 | 0.00 | 74 |
| heavy line | 4 % → 0 % | 10.2 px | 0.77 | 0.01 | 107 |
| pressure swell | 4 % → 0 % | 14.1 px | 0.77 | 0.06 | 68 |
| fast wave | 12 % → 0 % | 14.0 px | 0.77 | 0.00 | 274 |
| slow wave | 10 % → 0 % | 11.9 px | 0.77 | 0.00 | 468 |
| spiral | 17 % → 0 % | 11.1 px | 0.77 | 0.00 | 423 |
| loop | 9 % → 0 % | 11.2 px | 0.77 | 0.01 | 231 |
| tilted | 5 % → 4 % | 13.5 px | 0.77 | 0.89 | 113 |
| over the wet one | 7 % → 0 % | 5.9 px | 0.77 | 0.00 | 94 |
| long, no reload | 14 % → 1 % | 6.5 px | 0.77 | 0.08 | 573 | quarters: 0.21 → 0.14 → 0.10 → 0.07

Numbers say: light vs heavy: width 5.7 → 10.2 px, dark 0.00 → 0.77.

## Brush Artist · Watercolour — blue
Watercolour 0.93 · Ink 0.07 · 40 px · 31.6 s

![Brush Artist · Watercolour — blue](Brush-Artist-Watercolour-blue.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 6 % → 11 % | 16.2 px | 0.29 | 1.88 | 35 |
| heavy line | 11 % → 13 % | 31.9 px | 0.29 | 1.17 | 77 |
| pressure swell | 7 % → 9 % | 25.7 px | 0.30 | 1.38 | 58 |
| fast wave | 24 % → 27 % | 28.2 px | 0.29 | 1.12 | 150 |
| slow wave | 23 % → 32 % | 26.4 px | 0.31 | 1.41 | 289 |
| spiral | 39 % → 47 % | 25.6 px | 0.29 | 1.21 | 227 |
| loop | 20 % → 25 % | 25.7 px | 0.30 | 1.25 | 129 |
| tilted | 12 % → 12 % | 34.0 px | 0.30 | 1.00 | 98 |
| over the wet one | 21 % → 25 % | 25.2 px | 0.30 | 1.19 | 64 |
| long, no reload | 53 % → 59 % | 23.6 px | 0.30 | 1.12 | 353 | quarters: 0.23 → 0.21 → 0.19 → 0.16

Numbers say: light vs heavy: width 16.2 → 31.9 px, dark 0.29 → 0.29; wet paint spreads well beyond the stroke.

## Brush Artist · Watercolour — violet
Watercolour 0.93 · Ink 0.07 · 40 px · 31.2 s

![Brush Artist · Watercolour — violet](Brush-Artist-Watercolour-violet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 6 % → 11 % | 16.2 px | 0.36 | 1.88 | 26 |
| heavy line | 11 % → 13 % | 31.9 px | 0.37 | 1.17 | 61 |
| pressure swell | 7 % → 9 % | 25.7 px | 0.38 | 1.38 | 39 |
| fast wave | 24 % → 27 % | 28.2 px | 0.38 | 1.12 | 148 |
| slow wave | 23 % → 32 % | 26.4 px | 0.39 | 1.41 | 233 |
| spiral | 39 % → 47 % | 25.6 px | 0.37 | 1.21 | 209 |
| loop | 20 % → 25 % | 25.7 px | 0.38 | 1.25 | 122 |
| tilted | 12 % → 12 % | 34.0 px | 0.38 | 1.00 | 98 |
| over the wet one | 21 % → 25 % | 25.2 px | 0.38 | 1.19 | 54 |
| long, no reload | 53 % → 59 % | 23.6 px | 0.38 | 1.12 | 360 | quarters: 0.28 → 0.27 → 0.24 → 0.21

Numbers say: light vs heavy: width 16.2 → 31.9 px, dark 0.36 → 0.37; wet paint spreads well beyond the stroke.

## Brush Artist · Watercolour — teal
Watercolour 0.93 · Ink 0.07 · 40 px · 31.1 s

![Brush Artist · Watercolour — teal](Brush-Artist-Watercolour-teal.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 6 % → 11 % | 16.2 px | 0.23 | 1.88 | 44 |
| heavy line | 11 % → 13 % | 31.9 px | 0.23 | 1.17 | 78 |
| pressure swell | 7 % → 9 % | 25.7 px | 0.24 | 1.38 | 43 |
| fast wave | 24 % → 27 % | 28.2 px | 0.23 | 1.12 | 128 |
| slow wave | 23 % → 32 % | 26.4 px | 0.25 | 1.41 | 245 |
| spiral | 39 % → 47 % | 25.6 px | 0.23 | 1.21 | 241 |
| loop | 20 % → 25 % | 25.7 px | 0.24 | 1.25 | 131 |
| tilted | 12 % → 12 % | 34.0 px | 0.24 | 1.00 | 113 |
| over the wet one | 21 % → 25 % | 25.2 px | 0.24 | 1.19 | 54 |
| long, no reload | 53 % → 59 % | 23.6 px | 0.24 | 1.12 | 384 | quarters: 0.18 → 0.16 → 0.15 → 0.13

Numbers say: light vs heavy: width 16.2 → 31.9 px, dark 0.23 → 0.23; wet paint spreads well beyond the stroke.

## Brush Artist · Gouache
Gouache 1.00 · 30 px · 34.9 s

![Brush Artist · Gouache](Brush-Artist-Gouache.png)

A light paint: laid on a grey sheet (on white it cannot be seen); **dark** = how far it is from the grey either way.

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 8 % → 8 % | 24.4 px | 0.27 | 0.97 | 66 |
| heavy line | 15 % → 12 % | 42.8 px | 0.27 | 0.78 | 103 |
| pressure swell | 11 % → 9 % | 41.0 px | 0.27 | 0.85 | 1807 |
| fast wave | 30 % → 14 % | 34.9 px | 0.26 | 0.45 | 208 |
| slow wave | 29 % → 14 % | 34.0 px | 0.26 | 0.47 | 356 |
| spiral | 40 % → 14 % | 26.6 px | 0.26 | 0.35 | 314 |
| loop | 24 % → 15 % | 30.6 px | 0.26 | 0.62 | 181 |
| tilted | 10 % → 10 % | 27.4 px | 0.27 | 1.01 | 102 |
| over the wet one | 22 % → 19 % | 32.9 px | 0.27 | 0.89 | 177 |
| long, no reload | 43 % → 15 % | 19.1 px | 0.26 | 0.35 | 483 | quarters: 0.01 → 0.01 → 0.01 → 0.01

Numbers say: light vs heavy: width 24.4 → 42.8 px, dark 0.27 → 0.27; the long stroke does not run out of paint.

## Brush Artist · Oil — bristle
Oil 0.89 · Oil glaze 0.11 · 30 px · 16.6 s

![Brush Artist · Oil — bristle](Brush-Artist-Oil-bristle.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 10 % → 10 % | 28.5 px | 0.53 | 1.00 | 108 |
| heavy line | 11 % → 11 % | 32.4 px | 0.54 | 1.00 | 1972 |
| pressure swell | 8 % → 8 % | 31.8 px | 0.54 | 1.00 | 90 |
| fast wave | 28 % → 28 % | 32.0 px | 0.54 | 1.00 | 321 |
| slow wave | 27 % → 27 % | 31.6 px | 0.54 | 1.00 | 512 |
| spiral | 48 % → 48 % | 31.3 px | 0.53 | 1.00 | 509 |
| loop | 22 % → 22 % | 28.9 px | 0.54 | 1.00 | 252 |
| tilted | 11 % → 11 % | 29.9 px | 0.54 | 1.00 | 142 |
| over the wet one | 21 % → 21 % | 29.6 px | 0.54 | 1.00 | 107 |
| long, no reload | 55 % → 55 % | 24.7 px | 0.52 | 1.00 | 811 | quarters: 0.35 → 0.33 → 0.31 → 0.29

Numbers say: light vs heavy: width 28.5 → 32.4 px, dark 0.53 → 0.54.

## Brush Artist · Charcoal — stick
Charcoal 0.78 · Pastel 0.22 · 28 px · 10.2 s

![Brush Artist · Charcoal — stick](Brush-Artist-Charcoal-stick.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 5 % → 5 % | 15.2 px | 0.85 | 1.00 | 17 |
| heavy line | 8 % → 8 % | 24.2 px | 0.85 | 1.00 | 22 |
| pressure swell | 5 % → 5 % | 19.3 px | 0.85 | 1.00 | 12 |
| fast wave | 19 % → 19 % | 21.5 px | 0.85 | 1.00 | 80 |
| slow wave | 18 % → 18 % | 21.1 px | 0.85 | 1.00 | 95 |
| spiral | 25 % → 25 % | 16.3 px | 0.85 | 1.00 | 89 |
| loop | 16 % → 16 % | 20.2 px | 0.85 | 1.00 | 69 |
| tilted | 6 % → 6 % | 17.3 px | 0.85 | 1.00 | 25 |
| over the wet one | 14 % → 14 % | 20.5 px | 0.85 | 1.00 | 25 |
| long, no reload | 41 % → 41 % | 18.5 px | 0.85 | 1.00 | 196 | quarters: 0.39 → 0.39 → 0.39 → 0.39

Numbers say: light vs heavy: width 15.2 → 24.2 px, dark 0.85 → 0.85; the long stroke does not run out of paint.

## Brush Artist · Charcoal — stick B
Charcoal 0.78 · Pastel 0.22 · 36 px · 10.5 s

![Brush Artist · Charcoal — stick B](Brush-Artist-Charcoal-stick-B.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 7 % → 7 % | 19.2 px | 0.85 | 1.00 | 31 |
| heavy line | 10 % → 10 % | 30.5 px | 0.85 | 1.00 | 39 |
| pressure swell | 7 % → 7 % | 24.5 px | 0.85 | 1.00 | 27 |
| fast wave | 24 % → 24 % | 27.6 px | 0.85 | 1.00 | 105 |
| slow wave | 23 % → 23 % | 26.6 px | 0.85 | 1.00 | 148 |
| spiral | 35 % → 35 % | 23.2 px | 0.85 | 1.00 | 157 |
| loop | 19 % → 19 % | 25.2 px | 0.85 | 1.00 | 79 |
| tilted | 7 % → 7 % | 20.3 px | 0.85 | 1.00 | 34 |
| over the wet one | 17 % → 17 % | 25.9 px | 0.85 | 1.00 | 58 |
| long, no reload | 50 % → 50 % | 22.6 px | 0.85 | 1.00 | 256 | quarters: 0.47 → 0.47 → 0.47 → 0.47

Numbers say: light vs heavy: width 19.2 → 30.5 px, dark 0.85 → 0.85; the long stroke does not run out of paint.

## Brush Artist · Charcoal — stick C
Charcoal 0.78 · Pastel 0.22 · 22 px · 9.5 s

![Brush Artist · Charcoal — stick C](Brush-Artist-Charcoal-stick-C.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 4 % → 4 % | 12.2 px | 0.85 | 1.00 | 17 |
| heavy line | 7 % → 7 % | 19.4 px | 0.85 | 1.00 | 38 |
| pressure swell | 4 % → 4 % | 14.3 px | 0.85 | 1.00 | 17 |
| fast wave | 15 % → 15 % | 17.1 px | 0.85 | 1.00 | 57 |
| slow wave | 15 % → 15 % | 17.0 px | 0.85 | 1.00 | 88 |
| spiral | 20 % → 20 % | 13.3 px | 0.85 | 1.00 | 105 |
| loop | 12 % → 12 % | 16.1 px | 0.85 | 1.00 | 61 |
| tilted | 5 % → 5 % | 15.1 px | 0.85 | 1.00 | 20 |
| over the wet one | 11 % → 11 % | 16.8 px | 0.85 | 1.00 | 13 |
| long, no reload | 34 % → 34 % | 15.3 px | 0.85 | 1.00 | 134 | quarters: 0.33 → 0.32 → 0.32 → 0.32

Numbers say: light vs heavy: width 12.2 → 19.4 px, dark 0.85 → 0.85; the long stroke does not run out of paint.

## Oil · Henry Ward · Loaded flat
Gouache 1.00 + turpentine 35 % · 84 px · 42.9 s

![Oil · Henry Ward · Loaded flat](Oil-Henry-Ward-Loaded-flat.png)

A light paint: laid on a grey sheet (on white it cannot be seen); **dark** = how far it is from the grey either way.

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 11 % → 3 % | 30.6 px | 0.39 | 0.24 | 228 |
| heavy line | 15 % → 12 % | 42.2 px | 0.39 | 0.82 | 307 |
| pressure swell | 15 % → 9 % | 58.0 px | 0.36 | 0.57 | 233 |
| fast wave | 48 % → 28 % | 55.7 px | 0.32 | 0.58 | 837 |
| slow wave | 42 % → 28 % | 48.3 px | 0.36 | 0.67 | 1536 |
| spiral | 63 % → 33 % | 41.5 px | 0.37 | 0.53 | 1316 |
| loop | 39 % → 22 % | 50.4 px | 0.35 | 0.55 | 658 |
| tilted | 19 % → 19 % | 53.0 px | 0.33 | 1.01 | 439 |
| over the wet one | 32 % → 28 % | 36.9 px | 0.33 | 0.88 | 271 |
| long, no reload | 61 % → 31 % | 27.3 px | 0.36 | 0.52 | 1718 | quarters: 0.00 → 0.01 → 0.01 → 0.02

Numbers say: light vs heavy: width 30.6 → 42.2 px, dark 0.39 → 0.39; the long stroke does not run out of paint.

## Oil · Henry Ward · Dry scrub
Gouache 1.00 + turpentine 20 % · 90 px · 33.1 s

![Oil · Henry Ward · Dry scrub](Oil-Henry-Ward-Dry-scrub.png)

A light paint: laid on a grey sheet (on white it cannot be seen); **dark** = how far it is from the grey either way.

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 8 % → 0 % | 21.9 px | 0.00 | 0.00 | 183 |
| heavy line | 14 % → 4 % | 40.9 px | 0.36 | 0.26 | 286 |
| pressure swell | 13 % → 2 % | 47.2 px | 0.32 | 0.14 | 228 |
| fast wave | 53 % → 15 % | 61.0 px | 0.28 | 0.28 | 805 |
| slow wave | 34 % → 12 % | 38.9 px | 0.35 | 0.34 | 1349 |
| spiral | 70 % → 5 % | 46.3 px | 0.33 | 0.07 | 1338 |
| loop | 30 % → 2 % | 39.3 px | 0.31 | 0.07 | 671 |
| tilted | 19 % → 19 % | 53.5 px | 0.27 | 1.01 | 453 |
| over the wet one | 25 % → 9 % | 16.9 px | 0.27 | 0.35 | 233 |
| long, no reload | 43 % → 3 % | 19.5 px | 0.34 | 0.07 | 1563 | quarters: 0.04 → 0.03 → 0.04 → 0.05

Numbers say: light vs heavy: width 21.9 → 40.9 px, dark 0.00 → 0.36; the long stroke does not run out of paint.

## Oil · Henry Ward · Dirty contour
Gouache 1.00 + turpentine 35 % · 34 px · 37.7 s

![Oil · Henry Ward · Dirty contour](Oil-Henry-Ward-Dirty-contour.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 11 % → 4 % | 30.7 px | 0.58 | 0.42 | 114 |
| heavy line | 24 % → 16 % | 69.3 px | 0.58 | 0.67 | 216 |
| pressure swell | 15 % → 11 % | 54.9 px | 0.60 | 0.72 | 169 |
| fast wave | 43 % → 19 % | 50.1 px | 0.59 | 0.44 | 527 |
| slow wave | 41 % → 24 % | 47.5 px | 0.57 | 0.58 | 694 |
| spiral | 59 % → 24 % | 39.1 px | 0.55 | 0.41 | 730 |
| loop | 37 % → 23 % | 47.5 px | 0.56 | 0.64 | 365 |
| tilted | 14 % → 14 % | 37.9 px | 0.61 | 1.01 | 171 |
| over the wet one | 32 % → 27 % | 52.1 px | 0.61 | 0.84 | 200 |
| long, no reload | 72 % → 28 % | 32.4 px | 0.58 | 0.39 | 1097 | quarters: 0.53 → 0.50 → 0.42 → 0.33

Numbers say: light vs heavy: width 30.7 → 69.3 px, dark 0.58 → 0.58.

## Oil · Henry Ward · Wet drag
Ink 1.00 + turpentine 65 % · 80 px · 39.5 s

![Oil · Henry Ward · Wet drag](Oil-Henry-Ward-Wet-drag.png)

A light paint: laid on a grey sheet (on white it cannot be seen); **dark** = how far it is from the grey either way.

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 8 % → 0 % | 23.9 px | 0.03 | 0.04 | 175 |
| heavy line | 20 % → 20 % | 58.7 px | 0.06 | 0.98 | 331 |
| pressure swell | 17 % → 12 % | 61.9 px | 0.06 | 0.73 | 234 |
| fast wave | 45 % → 40 % | 52.1 px | 0.06 | 0.89 | 658 |
| slow wave | 55 % → 54 % | 64.0 px | 0.06 | 0.97 | 1173 |
| spiral | 73 % → 63 % | 48.5 px | 0.07 | 0.86 | 1258 |
| loop | 47 % → 43 % | 60.5 px | 0.06 | 0.93 | 488 |
| tilted | 20 % → 20 % | 54.5 px | 0.07 | 1.02 | 391 |
| over the wet one | 32 % → 31 % | 34.7 px | 0.07 | 0.98 | 236 |
| long, no reload | 88 % → 84 % | 39.4 px | 0.06 | 0.96 | 1749 | quarters: 0.05 → 0.06 → 0.06 → 0.05

Numbers say: light vs heavy: width 23.9 → 58.7 px, dark 0.03 → 0.06; the long stroke does not run out of paint.

## Oil · Henry Ward · Thin veil
Watercolour 0.93 · Ink 0.07 + turpentine 80 % · 96 px · 39.1 s

![Oil · Henry Ward · Thin veil](Oil-Henry-Ward-Thin-veil.png)

A light paint: laid on a grey sheet (on white it cannot be seen); **dark** = how far it is from the grey either way.

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 3 % → 4 % | 9.5 px | 0.04 | 1.09 | 179 |
| heavy line | 17 % → 20 % | 50.1 px | 0.10 | 1.13 | 278 |
| pressure swell | 12 % → 14 % | 44.3 px | 0.09 | 1.21 | 210 |
| fast wave | 47 % → 54 % | 54.4 px | 0.10 | 1.14 | 756 |
| slow wave | 48 % → 55 % | 54.9 px | 0.10 | 1.16 | 1266 |
| spiral | 65 % → 70 % | 42.6 px | 0.10 | 1.09 | 1454 |
| loop | 40 % → 48 % | 52.2 px | 0.10 | 1.19 | 649 |
| tilted | 18 % → 19 % | 50.9 px | 0.10 | 1.03 | 644 |
| over the wet one | 28 % → 31 % | 28.0 px | 0.10 | 1.11 | 289 |
| long, no reload | 62 % → 78 % | 27.6 px | 0.09 | 1.26 | 1910 | quarters: 0.09 → 0.09 → 0.07 → 0.05

Numbers say: light vs heavy: width 9.5 → 50.1 px, dark 0.04 → 0.10.

## Oil · Henry Ward · Ground
Ink 0.65 · Watercolour 0.35 + turpentine 75 % · 160 px · 66.6 s

![Oil · Henry Ward · Ground](Oil-Henry-Ward-Ground.png)

A light paint: laid on a grey sheet (on white it cannot be seen); **dark** = how far it is from the grey either way.

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 51 % → 56 % | 148.0 px | 0.06 | 1.10 | 609 |
| heavy line | 53 % → 52 % | 153.8 px | 0.06 | 0.98 | 954 |
| pressure swell | 41 % → 50 % | 155.4 px | 0.05 | 1.21 | 602 |
| fast wave | 87 % → 93 % | 101.1 px | 0.05 | 1.06 | 2050 |
| slow wave | 88 % → 86 % | 101.4 px | 0.04 | 0.98 | 3502 |
| spiral | 93 % → 92 % | 61.6 px | 0.04 | 0.99 | 3287 |
| loop | 78 % → 78 % | 101.0 px | 0.04 | 1.00 | 1680 |
| tilted | 40 % → 40 % | 110.6 px | 0.05 | 1.01 | 975 |
| over the wet one | 77 % → 79 % | 104.0 px | 0.05 | 1.03 | 814 |
| long, no reload | 99 % → 100 % | 44.6 px | 0.04 | 1.00 | 5358 | quarters: 0.01 → 0.02 → 0.04 → 0.07

Numbers say: light vs heavy: width 148.0 → 153.8 px, dark 0.06 → 0.06; pressure barely changes the width; the long stroke does not run out of paint.

## Oil · Henry Ward · HW #02 cream over wet olive
Watercolour 0.93 · Ink 0.07 + turpentine 80 % · 96 px · 41.8 s

![Oil · Henry Ward · HW #02 cream over wet olive](Oil-Henry-Ward-HW-02-cream-over-wet-olive.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 3 % → 4 % | 9.5 px | 0.03 | 1.09 | 203 |
| heavy line | 17 % → 20 % | 50.1 px | 0.11 | 1.13 | 278 |
| pressure swell | 12 % → 14 % | 44.3 px | 0.13 | 1.21 | 203 |
| fast wave | 47 % → 54 % | 54.4 px | 0.10 | 1.14 | 876 |
| slow wave | 48 % → 55 % | 54.9 px | 0.10 | 1.16 | 1431 |
| spiral | 65 % → 70 % | 42.6 px | 0.10 | 1.09 | 1698 |
| loop | 40 % → 48 % | 52.2 px | 0.08 | 1.19 | 706 |
| tilted | 18 % → 19 % | 50.9 px | 0.15 | 1.03 | 524 |
| over the wet one | 28 % → 31 % | 28.0 px | 0.15 | 1.11 | 273 |
| long, no reload | 62 % → 78 % | 27.6 px | 0.11 | 1.26 | 1959 | quarters: 0.13 → 0.10 → 0.07 → 0.06

Numbers say: light vs heavy: width 9.5 → 50.1 px, dark 0.03 → 0.11.

## Oil · Henry Ward · HW #04 grey arcs over ochre
Gouache 1.00 + turpentine 35 % · 84 px · 42.6 s

![Oil · Henry Ward · HW #04 grey arcs over ochre](Oil-Henry-Ward-HW-04-grey-arcs-over-ochre.png)

A light paint: laid on a grey sheet (on white it cannot be seen); **dark** = how far it is from the grey either way.

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 8 % → 0 % | 24.3 px | 0.00 | 0.00 | 209 |
| heavy line | 19 % → 16 % | 54.3 px | 0.34 | 0.84 | 337 |
| pressure swell | 15 % → 12 % | 55.4 px | 0.29 | 0.83 | 258 |
| fast wave | 47 % → 36 % | 54.9 px | 0.24 | 0.77 | 926 |
| slow wave | 47 % → 28 % | 54.4 px | 0.28 | 0.60 | 1502 |
| spiral | 64 % → 29 % | 42.2 px | 0.24 | 0.46 | 1422 |
| loop | 38 % → 18 % | 49.3 px | 0.25 | 0.47 | 696 |
| tilted | 18 % → 19 % | 51.5 px | 0.23 | 1.00 | 413 |
| over the wet one | 36 % → 26 % | 48.2 px | 0.23 | 0.73 | 367 |
| long, no reload | 61 % → 34 % | 27.4 px | 0.23 | 0.56 | 1787 | quarters: 0.00 → 0.01 → 0.01 → 0.02

Numbers say: light vs heavy: width 24.3 → 54.3 px, dark 0.00 → 0.34; the long stroke does not run out of paint.

## Oil · Henry Ward · HW #09 white arches over wet blue-grey
Gouache 1.00 + turpentine 35 % · 84 px · 42.8 s

![Oil · Henry Ward · HW #09 white arches over wet blue-grey](Oil-Henry-Ward-HW-09-white-arches-over-wet-blue-grey.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 11 % → 3 % | 30.6 px | 0.19 | 0.24 | 206 |
| heavy line | 15 % → 12 % | 42.2 px | 0.26 | 0.82 | 291 |
| pressure swell | 15 % → 9 % | 58.0 px | 0.33 | 0.57 | 201 |
| fast wave | 48 % → 28 % | 55.7 px | 0.37 | 0.58 | 640 |
| slow wave | 42 % → 28 % | 48.3 px | 0.28 | 0.67 | 1412 |
| spiral | 63 % → 33 % | 41.5 px | 0.36 | 0.53 | 1529 |
| loop | 39 % → 22 % | 50.4 px | 0.29 | 0.55 | 679 |
| tilted | 19 % → 19 % | 53.0 px | 0.35 | 1.01 | 455 |
| over the wet one | 32 % → 28 % | 36.9 px | 0.35 | 0.88 | 319 |
| long, no reload | 61 % → 31 % | 27.3 px | 0.36 | 0.52 | 1705 | quarters: 0.31 → 0.20 → 0.14 → 0.10

Numbers say: light vs heavy: width 30.6 → 42.2 px, dark 0.19 → 0.26.

## Oil · Henry Ward · HW #03 navy contours over wet band
Gouache 1.00 + turpentine 35 % · 84 px · 43.8 s

![Oil · Henry Ward · HW #03 navy contours over wet band](Oil-Henry-Ward-HW-03-navy-contours-over-wet-band.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 11 % → 3 % | 30.6 px | 0.21 | 0.24 | 226 |
| heavy line | 15 % → 12 % | 42.2 px | 0.27 | 0.82 | 312 |
| pressure swell | 15 % → 9 % | 58.0 px | 0.35 | 0.57 | 185 |
| fast wave | 48 % → 28 % | 55.7 px | 0.39 | 0.58 | 787 |
| slow wave | 42 % → 28 % | 48.3 px | 0.30 | 0.67 | 1273 |
| spiral | 63 % → 33 % | 41.5 px | 0.37 | 0.53 | 1502 |
| loop | 39 % → 22 % | 50.4 px | 0.30 | 0.55 | 695 |
| tilted | 19 % → 19 % | 53.0 px | 0.37 | 1.01 | 463 |
| over the wet one | 32 % → 28 % | 36.9 px | 0.37 | 0.88 | 326 |
| long, no reload | 61 % → 31 % | 27.3 px | 0.38 | 0.52 | 1647 | quarters: 0.32 → 0.21 → 0.15 → 0.10

Numbers say: light vs heavy: width 30.6 → 42.2 px, dark 0.21 → 0.27.

## Oil · Henry Ward · HW #01 peach cloud and legs over teal
Gouache 1.00 + turpentine 35 % · 84 px · 44.9 s

![Oil · Henry Ward · HW #01 peach cloud and legs over teal](Oil-Henry-Ward-HW-01-peach-cloud-and-legs-over-teal.png)

A light paint: laid on a grey sheet (on white it cannot be seen); **dark** = how far it is from the grey either way.

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 8 % → 0 % | 24.3 px | 0.00 | 0.00 | 222 |
| heavy line | 19 % → 16 % | 54.3 px | 0.34 | 0.84 | 292 |
| pressure swell | 15 % → 12 % | 55.4 px | 0.30 | 0.83 | 280 |
| fast wave | 47 % → 36 % | 54.9 px | 0.25 | 0.77 | 997 |
| slow wave | 47 % → 28 % | 54.4 px | 0.28 | 0.60 | 1407 |
| spiral | 64 % → 29 % | 42.2 px | 0.24 | 0.46 | 1631 |
| loop | 38 % → 18 % | 49.3 px | 0.26 | 0.47 | 789 |
| tilted | 18 % → 19 % | 51.5 px | 0.24 | 1.00 | 429 |
| over the wet one | 36 % → 26 % | 48.2 px | 0.24 | 0.73 | 300 |
| long, no reload | 61 % → 34 % | 27.4 px | 0.24 | 0.56 | 1686 | quarters: 0.00 → 0.01 → 0.01 → 0.02

Numbers say: light vs heavy: width 24.3 → 54.3 px, dark 0.00 → 0.34; the long stroke does not run out of paint.

## Oil · Henry Ward · HW #05 rust, pink, green-black
Gouache 1.00 + turpentine 35 % · 84 px · 44.2 s

![Oil · Henry Ward · HW #05 rust, pink, green-black](Oil-Henry-Ward-HW-05-rust-pink-green-black.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 11 % → 3 % | 30.6 px | 0.37 | 0.24 | 214 |
| heavy line | 15 % → 12 % | 42.2 px | 0.44 | 0.82 | 313 |
| pressure swell | 15 % → 9 % | 58.0 px | 0.50 | 0.57 | 180 |
| fast wave | 48 % → 28 % | 55.7 px | 0.53 | 0.58 | 734 |
| slow wave | 42 % → 28 % | 48.3 px | 0.46 | 0.67 | 1216 |
| spiral | 63 % → 33 % | 41.5 px | 0.53 | 0.53 | 1377 |
| loop | 39 % → 22 % | 50.4 px | 0.47 | 0.55 | 677 |
| tilted | 19 % → 19 % | 53.0 px | 0.51 | 1.01 | 494 |
| over the wet one | 32 % → 28 % | 36.9 px | 0.51 | 0.88 | 319 |
| long, no reload | 61 % → 31 % | 27.3 px | 0.54 | 0.52 | 1801 | quarters: 0.46 → 0.33 → 0.27 → 0.19

Numbers say: light vs heavy: width 30.6 → 42.2 px, dark 0.37 → 0.44.

## Oil · Henry Ward · HW #07 blue L and zigzag on lilac
Gouache 1.00 + turpentine 20 % · 90 px · 37.1 s

![Oil · Henry Ward · HW #07 blue L and zigzag on lilac](Oil-Henry-Ward-HW-07-blue-L-and-zigzag-on-lilac.png)

A light paint: laid on a grey sheet (on white it cannot be seen); **dark** = how far it is from the grey either way.

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 8 % → 0 % | 23.4 px | 0.00 | 0.00 | 258 |
| heavy line | 17 % → 5 % | 49.3 px | 0.38 | 0.27 | 362 |
| pressure swell | 15 % → 5 % | 55.6 px | 0.36 | 0.33 | 221 |
| fast wave | 51 % → 8 % | 59.4 px | 0.32 | 0.16 | 890 |
| slow wave | 40 % → 7 % | 45.7 px | 0.34 | 0.19 | 1431 |
| spiral | 68 % → 8 % | 44.5 px | 0.29 | 0.12 | 1423 |
| loop | 34 % → 1 % | 43.6 px | 0.29 | 0.03 | 708 |
| tilted | 18 % → 19 % | 51.6 px | 0.30 | 1.00 | 413 |
| over the wet one | 27 % → 6 % | 24.7 px | 0.30 | 0.23 | 330 |
| long, no reload | 52 % → 8 % | 23.4 px | 0.29 | 0.14 | 1759 | quarters: 0.04 → 0.02 → 0.03 → 0.05

Numbers say: light vs heavy: width 23.4 → 49.3 px, dark 0.00 → 0.38; the long stroke does not run out of paint.

## Oil · Henry Ward · HW #08 crown and dark oval
Gouache 1.00 + turpentine 35 % · 84 px · 47.6 s

![Oil · Henry Ward · HW #08 crown and dark oval](Oil-Henry-Ward-HW-08-crown-and-dark-oval.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 22 % → 2 % | 63.8 px | 0.10 | 0.08 | 319 |
| heavy line | 31 % → 15 % | 91.2 px | 0.13 | 0.48 | 437 |
| pressure swell | 25 % → 11 % | 94.1 px | 0.18 | 0.44 | 317 |
| fast wave | 66 % → 37 % | 76.2 px | 0.24 | 0.56 | 1112 |
| slow wave | 56 % → 32 % | 65.1 px | 0.15 | 0.57 | 1871 |
| spiral | 67 % → 30 % | 44.1 px | 0.22 | 0.44 | 1906 |
| loop | 50 % → 25 % | 65.1 px | 0.13 | 0.51 | 960 |
| tilted | 22 % → 22 % | 62.6 px | 0.21 | 1.00 | 509 |
| over the wet one | 49 % → 35 % | 74.9 px | 0.21 | 0.71 | 452 |
| long, no reload | 90 % → 44 % | 40.3 px | 0.25 | 0.49 | 2345 | quarters: 0.23 → 0.22 → 0.13 → 0.07

Numbers say: light vs heavy: width 63.8 → 91.2 px, dark 0.10 → 0.13.

## Oil · Henry Ward · HW #10 green block over maroon
Gouache 1.00 + turpentine 35 % · 84 px · 46.7 s

![Oil · Henry Ward · HW #10 green block over maroon](Oil-Henry-Ward-HW-10-green-block-over-maroon.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 22 % → 2 % | 63.8 px | 0.08 | 0.08 | 285 |
| heavy line | 31 % → 15 % | 91.2 px | 0.11 | 0.48 | 413 |
| pressure swell | 25 % → 11 % | 94.1 px | 0.16 | 0.44 | 332 |
| fast wave | 66 % → 37 % | 76.2 px | 0.21 | 0.56 | 1062 |
| slow wave | 56 % → 32 % | 65.1 px | 0.13 | 0.57 | 1879 |
| spiral | 67 % → 30 % | 44.1 px | 0.20 | 0.44 | 1831 |
| loop | 50 % → 25 % | 65.1 px | 0.12 | 0.51 | 897 |
| tilted | 22 % → 22 % | 62.6 px | 0.19 | 1.00 | 541 |
| over the wet one | 49 % → 35 % | 74.9 px | 0.19 | 0.71 | 499 |
| long, no reload | 90 % → 44 % | 40.3 px | 0.22 | 0.49 | 2102 | quarters: 0.21 → 0.20 → 0.12 → 0.07

Numbers say: light vs heavy: width 63.8 → 91.2 px, dark 0.08 → 0.11.

## Oil · Henry Ward · HW #11 cream mass and purple balls
Gouache 1.00 + turpentine 35 % · 84 px · 43.2 s

![Oil · Henry Ward · HW #11 cream mass and purple balls](Oil-Henry-Ward-HW-11-cream-mass-and-purple-balls.png)

A light paint: laid on a grey sheet (on white it cannot be seen); **dark** = how far it is from the grey either way.

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 11 % → 3 % | 30.6 px | 0.42 | 0.24 | 203 |
| heavy line | 15 % → 12 % | 42.2 px | 0.40 | 0.82 | 315 |
| pressure swell | 15 % → 9 % | 58.0 px | 0.31 | 0.57 | 210 |
| fast wave | 48 % → 28 % | 55.7 px | 0.28 | 0.58 | 793 |
| slow wave | 42 % → 28 % | 48.3 px | 0.34 | 0.67 | 1252 |
| spiral | 63 % → 33 % | 41.5 px | 0.28 | 0.53 | 1549 |
| loop | 39 % → 22 % | 50.4 px | 0.32 | 0.55 | 667 |
| tilted | 19 % → 19 % | 53.0 px | 0.30 | 1.01 | 440 |
| over the wet one | 32 % → 28 % | 36.9 px | 0.30 | 0.88 | 290 |
| long, no reload | 61 % → 31 % | 27.3 px | 0.28 | 0.52 | 1724 | quarters: 0.00 → 0.01 → 0.01 → 0.02

Numbers say: light vs heavy: width 30.6 → 42.2 px, dark 0.42 → 0.40; the long stroke does not run out of paint.

## Oil · Henry Ward · HW #13 blue scrub under red
Gouache 1.00 + turpentine 35 % · 84 px · 42.8 s

![Oil · Henry Ward · HW #13 blue scrub under red](Oil-Henry-Ward-HW-13-blue-scrub-under-red.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 8 % → 0 % | 24.3 px | 0.00 | 0.00 | 215 |
| heavy line | 19 % → 16 % | 54.3 px | 0.50 | 0.84 | 338 |
| pressure swell | 15 % → 12 % | 55.4 px | 0.52 | 0.83 | 233 |
| fast wave | 47 % → 36 % | 54.9 px | 0.56 | 0.77 | 880 |
| slow wave | 47 % → 28 % | 54.4 px | 0.54 | 0.60 | 1546 |
| spiral | 64 % → 29 % | 42.2 px | 0.57 | 0.46 | 1443 |
| loop | 38 % → 18 % | 49.3 px | 0.55 | 0.47 | 756 |
| tilted | 18 % → 19 % | 51.5 px | 0.57 | 1.00 | 415 |
| over the wet one | 36 % → 26 % | 48.2 px | 0.57 | 0.73 | 328 |
| long, no reload | 61 % → 34 % | 27.4 px | 0.57 | 0.56 | 1802 | quarters: 0.50 → 0.40 → 0.31 → 0.15

Numbers say: light vs heavy: width 24.3 → 54.3 px, dark 0.00 → 0.50.

## Oil · Henry Ward · HW #14 olive totem on dark
Gouache 1.00 + turpentine 35 % · 84 px · 46.7 s

![Oil · Henry Ward · HW #14 olive totem on dark](Oil-Henry-Ward-HW-14-olive-totem-on-dark.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 22 % → 2 % | 63.8 px | 0.15 | 0.08 | 240 |
| heavy line | 31 % → 15 % | 91.2 px | 0.18 | 0.48 | 481 |
| pressure swell | 25 % → 11 % | 94.1 px | 0.23 | 0.44 | 313 |
| fast wave | 66 % → 37 % | 76.2 px | 0.29 | 0.56 | 1125 |
| slow wave | 56 % → 32 % | 65.1 px | 0.20 | 0.57 | 1988 |
| spiral | 67 % → 30 % | 44.1 px | 0.27 | 0.44 | 1904 |
| loop | 50 % → 25 % | 65.1 px | 0.19 | 0.51 | 925 |
| tilted | 22 % → 22 % | 62.6 px | 0.26 | 1.00 | 490 |
| over the wet one | 49 % → 35 % | 74.9 px | 0.26 | 0.71 | 472 |
| long, no reload | 90 % → 44 % | 40.3 px | 0.30 | 0.49 | 2792 | quarters: 0.28 → 0.27 → 0.17 → 0.09

Numbers say: light vs heavy: width 63.8 → 91.2 px, dark 0.15 → 0.18.

## Oil · Henry Ward · Ground #2b2f1c flat
Ink 0.65 · Watercolour 0.35 + turpentine 75 % · 160 px · 65.2 s

![Oil · Henry Ward · Ground #2b2f1c flat](Oil-Henry-Ward-Ground-2b2f1c-flat.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 51 % → 56 % | 148.0 px | 0.47 | 1.10 | 611 |
| heavy line | 53 % → 52 % | 153.8 px | 0.52 | 0.98 | 942 |
| pressure swell | 41 % → 50 % | 155.4 px | 0.53 | 1.21 | 562 |
| fast wave | 87 % → 93 % | 101.1 px | 0.57 | 1.06 | 2091 |
| slow wave | 88 % → 86 % | 101.4 px | 0.60 | 0.98 | 3816 |
| spiral | 93 % → 92 % | 61.6 px | 0.57 | 0.99 | 4828 |
| loop | 78 % → 78 % | 101.0 px | 0.58 | 1.00 | 1551 |
| tilted | 40 % → 40 % | 110.6 px | 0.56 | 1.01 | 864 |
| over the wet one | 77 % → 79 % | 104.0 px | 0.56 | 1.03 | 761 |
| long, no reload | 99 % → 100 % | 44.6 px | 0.60 | 1.00 | 4551 | quarters: 0.72 → 0.68 → 0.60 → 0.45

Numbers say: light vs heavy: width 148.0 → 153.8 px, dark 0.47 → 0.52; pressure barely changes the width.

## Oil · Henry Ward · Thin veil #2b3a44 flat
Watercolour 0.93 · Ink 0.07 + turpentine 80 % · 96 px · 40.9 s

![Oil · Henry Ward · Thin veil #2b3a44 flat](Oil-Henry-Ward-Thin-veil-2b3a44-flat.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 3 % → 4 % | 9.5 px | 0.03 | 1.09 | 282 |
| heavy line | 17 % → 20 % | 50.1 px | 0.11 | 1.13 | 262 |
| pressure swell | 12 % → 14 % | 44.3 px | 0.13 | 1.21 | 291 |
| fast wave | 47 % → 54 % | 54.4 px | 0.10 | 1.14 | 1386 |
| slow wave | 48 % → 55 % | 54.9 px | 0.10 | 1.16 | 1308 |
| spiral | 65 % → 70 % | 42.6 px | 0.10 | 1.09 | 1433 |
| loop | 40 % → 48 % | 52.2 px | 0.08 | 1.19 | 660 |
| tilted | 18 % → 19 % | 50.9 px | 0.15 | 1.03 | 510 |
| over the wet one | 28 % → 31 % | 28.0 px | 0.15 | 1.11 | 263 |
| long, no reload | 62 % → 78 % | 27.6 px | 0.11 | 1.26 | 1817 | quarters: 0.13 → 0.10 → 0.07 → 0.06

Numbers say: light vs heavy: width 9.5 → 50.1 px, dark 0.03 → 0.11.

## Oil · Henry Ward · Loaded flat #ece6c0 flat
Gouache 1.00 + turpentine 30 % · 84 px · 40.2 s

![Oil · Henry Ward · Loaded flat #ece6c0 flat](Oil-Henry-Ward-Loaded-flat-ece6c0-flat.png)

A light paint: laid on a grey sheet (on white it cannot be seen); **dark** = how far it is from the grey either way.

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 11 % → 3 % | 30.7 px | 0.43 | 0.24 | 201 |
| heavy line | 15 % → 12 % | 42.2 px | 0.42 | 0.83 | 255 |
| pressure swell | 15 % → 9 % | 58.1 px | 0.33 | 0.58 | 223 |
| fast wave | 48 % → 29 % | 55.7 px | 0.30 | 0.61 | 701 |
| slow wave | 42 % → 28 % | 48.3 px | 0.37 | 0.68 | 1193 |
| spiral | 63 % → 34 % | 41.5 px | 0.31 | 0.54 | 1352 |
| loop | 39 % → 22 % | 50.7 px | 0.34 | 0.57 | 626 |
| tilted | 19 % → 19 % | 53.1 px | 0.33 | 1.00 | 395 |
| over the wet one | 32 % → 28 % | 36.9 px | 0.33 | 0.88 | 271 |
| long, no reload | 61 % → 32 % | 27.3 px | 0.30 | 0.53 | 1482 | quarters: 0.00 → 0.01 → 0.02 → 0.02

Numbers say: light vs heavy: width 30.7 → 42.2 px, dark 0.43 → 0.42; the long stroke does not run out of paint.

## Oil · Henry Ward · Dry scrub #ece6c0 filbert
Gouache 1.00 + turpentine 20 % · 90 px · 33.3 s

![Oil · Henry Ward · Dry scrub #ece6c0 filbert](Oil-Henry-Ward-Dry-scrub-ece6c0-filbert.png)

A light paint: laid on a grey sheet (on white it cannot be seen); **dark** = how far it is from the grey either way.

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 8 % → 0 % | 23.4 px | 0.00 | 0.00 | 237 |
| heavy line | 17 % → 5 % | 49.3 px | 0.37 | 0.27 | 338 |
| pressure swell | 15 % → 5 % | 55.6 px | 0.35 | 0.33 | 265 |
| fast wave | 51 % → 8 % | 59.4 px | 0.30 | 0.16 | 850 |
| slow wave | 40 % → 7 % | 45.7 px | 0.33 | 0.19 | 1362 |
| spiral | 68 % → 8 % | 44.5 px | 0.27 | 0.12 | 1337 |
| loop | 34 % → 1 % | 43.6 px | 0.28 | 0.03 | 642 |
| tilted | 18 % → 19 % | 51.6 px | 0.28 | 1.00 | 402 |
| over the wet one | 27 % → 6 % | 24.7 px | 0.28 | 0.23 | 279 |
| long, no reload | 52 % → 8 % | 23.4 px | 0.27 | 0.14 | 1666 | quarters: 0.04 → 0.02 → 0.03 → 0.05

Numbers say: light vs heavy: width 23.4 → 49.3 px, dark 0.00 → 0.37; the long stroke does not run out of paint.

## Oil · Henry Ward · Ground #8a6a20 flat
Ink 0.65 · Watercolour 0.35 + turpentine 75 % · 160 px · 62.0 s

![Oil · Henry Ward · Ground #8a6a20 flat](Oil-Henry-Ward-Ground-8a6a20-flat.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 51 % → 56 % | 148.0 px | 0.17 | 1.10 | 544 |
| heavy line | 53 % → 52 % | 153.8 px | 0.18 | 0.98 | 1010 |
| pressure swell | 41 % → 50 % | 155.4 px | 0.19 | 1.21 | 540 |
| fast wave | 87 % → 93 % | 101.1 px | 0.21 | 1.06 | 1866 |
| slow wave | 88 % → 86 % | 101.4 px | 0.23 | 0.98 | 3013 |
| spiral | 93 % → 92 % | 61.6 px | 0.23 | 0.99 | 3104 |
| loop | 78 % → 78 % | 101.0 px | 0.22 | 1.00 | 1530 |
| tilted | 40 % → 40 % | 110.6 px | 0.22 | 1.01 | 892 |
| over the wet one | 77 % → 79 % | 104.0 px | 0.22 | 1.03 | 728 |
| long, no reload | 99 % → 100 % | 44.6 px | 0.23 | 1.00 | 5588 | quarters: 0.30 → 0.27 → 0.21 → 0.16

Numbers say: light vs heavy: width 148.0 → 153.8 px, dark 0.17 → 0.18; pressure barely changes the width.

## Oil · Henry Ward · Loaded flat #b8bcc0 filbert
Gouache 1.00 + turpentine 35 % · 84 px · 39.7 s

![Oil · Henry Ward · Loaded flat #b8bcc0 filbert](Oil-Henry-Ward-Loaded-flat-b8bcc0-filbert.png)

A light paint: laid on a grey sheet (on white it cannot be seen); **dark** = how far it is from the grey either way.

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 8 % → 0 % | 24.3 px | 0.00 | 0.00 | 215 |
| heavy line | 19 % → 16 % | 54.3 px | 0.34 | 0.84 | 282 |
| pressure swell | 15 % → 12 % | 55.4 px | 0.29 | 0.83 | 218 |
| fast wave | 47 % → 36 % | 54.9 px | 0.24 | 0.77 | 787 |
| slow wave | 47 % → 28 % | 54.4 px | 0.28 | 0.60 | 1292 |
| spiral | 64 % → 29 % | 42.2 px | 0.24 | 0.46 | 1281 |
| loop | 38 % → 18 % | 49.3 px | 0.25 | 0.47 | 636 |
| tilted | 18 % → 19 % | 51.5 px | 0.23 | 1.00 | 357 |
| over the wet one | 36 % → 26 % | 48.2 px | 0.23 | 0.73 | 317 |
| long, no reload | 61 % → 34 % | 27.4 px | 0.23 | 0.56 | 1803 | quarters: 0.00 → 0.01 → 0.01 → 0.02

Numbers say: light vs heavy: width 24.3 → 54.3 px, dark 0.00 → 0.34; the long stroke does not run out of paint.

## Oil · Henry Ward · Dry scrub #c8ccd0 worn
Gouache 1.00 + turpentine 20 % · 90 px · 31.0 s

![Oil · Henry Ward · Dry scrub #c8ccd0 worn](Oil-Henry-Ward-Dry-scrub-c8ccd0-worn.png)

A light paint: laid on a grey sheet (on white it cannot be seen); **dark** = how far it is from the grey either way.

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 17 % → 0 % | 48.2 px | 0.00 | 0.00 | 237 |
| heavy line | 30 % → 0 % | 85.8 px | 0.28 | 0.01 | 417 |
| pressure swell | 21 % → 6 % | 77.1 px | 0.29 | 0.28 | 275 |
| fast wave | 68 % → 7 % | 78.5 px | 0.21 | 0.10 | 1059 |
| slow wave | 51 % → 4 % | 58.7 px | 0.26 | 0.07 | 1618 |
| spiral | 72 % → 9 % | 47.6 px | 0.22 | 0.13 | 1666 |
| loop | 51 % → 1 % | 66.3 px | 0.25 | 0.01 | 760 |
| tilted | 20 % → 20 % | 56.8 px | 0.21 | 1.00 | 470 |
| over the wet one | 41 % → 7 % | 56.6 px | 0.21 | 0.16 | 345 |
| long, no reload | 79 % → 0 % | 35.4 px | 0.17 | 0.00 | 2370 | quarters: 0.01 → 0.01 → 0.01 → 0.02

Numbers say: light vs heavy: width 48.2 → 85.8 px, dark 0.00 → 0.28; the long stroke does not run out of paint.

## Oil · Henry Ward · Wet drag #9ea4aa flat
Ink 1.00 + turpentine 65 % · 80 px · 37.9 s

![Oil · Henry Ward · Wet drag #9ea4aa flat](Oil-Henry-Ward-Wet-drag-9ea4aa-flat.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 8 % → 0 % | 23.9 px | 0.03 | 0.04 | 147 |
| heavy line | 20 % → 20 % | 58.7 px | 0.07 | 0.98 | 330 |
| pressure swell | 17 % → 12 % | 61.9 px | 0.06 | 0.73 | 204 |
| fast wave | 45 % → 40 % | 52.1 px | 0.07 | 0.89 | 619 |
| slow wave | 55 % → 54 % | 64.0 px | 0.07 | 0.97 | 1057 |
| spiral | 73 % → 63 % | 48.5 px | 0.07 | 0.86 | 1205 |
| loop | 47 % → 43 % | 60.5 px | 0.07 | 0.93 | 540 |
| tilted | 20 % → 20 % | 54.5 px | 0.09 | 1.02 | 368 |
| over the wet one | 32 % → 31 % | 34.7 px | 0.09 | 0.98 | 209 |
| long, no reload | 88 % → 84 % | 39.4 px | 0.07 | 0.96 | 2510 | quarters: 0.08 → 0.08 → 0.06 → 0.05

Numbers say: light vs heavy: width 23.9 → 58.7 px, dark 0.03 → 0.07.

## Oil · Henry Ward · Ground #e8b4a8 flat
Ink 0.65 · Watercolour 0.35 + turpentine 75 % · 160 px · 70.4 s

![Oil · Henry Ward · Ground #e8b4a8 flat](Oil-Henry-Ward-Ground-e8b4a8-flat.png)

A light paint: laid on a grey sheet (on white it cannot be seen); **dark** = how far it is from the grey either way.

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 51 % → 56 % | 148.0 px | 0.06 | 1.10 | 518 |
| heavy line | 53 % → 52 % | 153.8 px | 0.05 | 0.98 | 862 |
| pressure swell | 41 % → 50 % | 155.4 px | 0.05 | 1.21 | 555 |
| fast wave | 87 % → 93 % | 101.1 px | 0.04 | 1.06 | 1857 |
| slow wave | 88 % → 86 % | 101.4 px | 0.04 | 0.98 | 3931 |
| spiral | 93 % → 92 % | 61.6 px | 0.04 | 0.99 | 3006 |
| loop | 78 % → 78 % | 101.0 px | 0.04 | 1.00 | 1440 |
| tilted | 40 % → 40 % | 110.6 px | 0.04 | 1.01 | 929 |
| over the wet one | 77 % → 79 % | 104.0 px | 0.04 | 1.03 | 742 |
| long, no reload | 99 % → 100 % | 44.6 px | 0.04 | 1.00 | 4983 | quarters: 0.00 → 0.01 → 0.04 → 0.06

Numbers say: light vs heavy: width 148.0 → 153.8 px, dark 0.06 → 0.05; pressure barely changes the width; the long stroke does not run out of paint.

## Oil · Henry Ward · Loaded flat #6e7f90 flat
Gouache 1.00 + turpentine 35 % · 84 px · 40.7 s

![Oil · Henry Ward · Loaded flat #6e7f90 flat](Oil-Henry-Ward-Loaded-flat-6e7f90-flat.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 11 % → 3 % | 30.6 px | 0.19 | 0.24 | 192 |
| heavy line | 15 % → 12 % | 42.2 px | 0.26 | 0.82 | 270 |
| pressure swell | 15 % → 9 % | 58.0 px | 0.33 | 0.57 | 186 |
| fast wave | 48 % → 28 % | 55.7 px | 0.37 | 0.58 | 783 |
| slow wave | 42 % → 28 % | 48.3 px | 0.28 | 0.67 | 1141 |
| spiral | 63 % → 33 % | 41.5 px | 0.36 | 0.53 | 1279 |
| loop | 39 % → 22 % | 50.4 px | 0.29 | 0.55 | 663 |
| tilted | 19 % → 19 % | 53.0 px | 0.35 | 1.01 | 400 |
| over the wet one | 32 % → 28 % | 36.9 px | 0.35 | 0.88 | 376 |
| long, no reload | 61 % → 31 % | 27.3 px | 0.36 | 0.52 | 1513 | quarters: 0.31 → 0.20 → 0.14 → 0.10

Numbers say: light vs heavy: width 30.6 → 42.2 px, dark 0.19 → 0.26.

## Oil · Henry Ward · Loaded flat #f6f6f2 filbert
Gouache 1.00 + turpentine 30 % · 84 px · 41.3 s

![Oil · Henry Ward · Loaded flat #f6f6f2 filbert](Oil-Henry-Ward-Loaded-flat-f6f6f2-filbert.png)

A light paint: laid on a grey sheet (on white it cannot be seen); **dark** = how far it is from the grey either way.

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 8 % → 0 % | 24.4 px | 0.00 | 0.00 | 213 |
| heavy line | 19 % → 16 % | 54.2 px | 0.43 | 0.84 | 278 |
| pressure swell | 15 % → 12 % | 55.2 px | 0.38 | 0.84 | 206 |
| fast wave | 48 % → 38 % | 54.9 px | 0.35 | 0.79 | 773 |
| slow wave | 47 % → 29 % | 54.3 px | 0.37 | 0.61 | 1398 |
| spiral | 64 % → 30 % | 42.3 px | 0.34 | 0.46 | 1275 |
| loop | 38 % → 19 % | 49.6 px | 0.35 | 0.49 | 678 |
| tilted | 18 % → 19 % | 51.6 px | 0.35 | 1.00 | 436 |
| over the wet one | 36 % → 26 % | 48.4 px | 0.35 | 0.74 | 374 |
| long, no reload | 61 % → 35 % | 27.3 px | 0.34 | 0.57 | 1553 | quarters: 0.00 → 0.01 → 0.02 → 0.03

Numbers say: light vs heavy: width 24.4 → 54.2 px, dark 0.00 → 0.43; the long stroke does not run out of paint.

## Oil · Henry Ward · Dry scrub #f6f6f2 filbert
Gouache 1.00 + turpentine 20 % · 90 px · 32.1 s

![Oil · Henry Ward · Dry scrub #f6f6f2 filbert](Oil-Henry-Ward-Dry-scrub-f6f6f2-filbert.png)

A light paint: laid on a grey sheet (on white it cannot be seen); **dark** = how far it is from the grey either way.

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 8 % → 0 % | 23.4 px | 0.00 | 0.00 | 212 |
| heavy line | 17 % → 5 % | 49.3 px | 0.38 | 0.27 | 290 |
| pressure swell | 15 % → 5 % | 55.6 px | 0.36 | 0.33 | 230 |
| fast wave | 51 % → 8 % | 59.4 px | 0.32 | 0.16 | 890 |
| slow wave | 40 % → 7 % | 45.7 px | 0.34 | 0.19 | 1288 |
| spiral | 68 % → 8 % | 44.5 px | 0.30 | 0.12 | 1400 |
| loop | 34 % → 1 % | 43.6 px | 0.30 | 0.03 | 930 |
| tilted | 18 % → 19 % | 51.6 px | 0.30 | 1.00 | 419 |
| over the wet one | 27 % → 6 % | 24.7 px | 0.30 | 0.23 | 276 |
| long, no reload | 52 % → 8 % | 23.4 px | 0.30 | 0.14 | 1571 | quarters: 0.04 → 0.02 → 0.03 → 0.05

Numbers say: light vs heavy: width 23.4 → 49.3 px, dark 0.00 → 0.38; the long stroke does not run out of paint.

## Oil · Henry Ward · Ground #e8e2da flat
Gouache 1.00 + turpentine 30 % · 160 px · 78.1 s

![Oil · Henry Ward · Ground #e8e2da flat](Oil-Henry-Ward-Ground-e8e2da-flat.png)

A light paint: laid on a grey sheet (on white it cannot be seen); **dark** = how far it is from the grey either way.

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 51 % → 43 % | 148.1 px | 0.37 | 0.84 | 648 |
| heavy line | 52 % → 45 % | 151.1 px | 0.37 | 0.87 | 792 |
| pressure swell | 41 % → 43 % | 154.5 px | 0.36 | 1.04 | 569 |
| fast wave | 85 % → 83 % | 97.9 px | 0.36 | 0.98 | 2438 |
| slow wave | 86 % → 70 % | 99.3 px | 0.37 | 0.81 | 3653 |
| spiral | 89 % → 64 % | 58.5 px | 0.36 | 0.72 | 3290 |
| loop | 75 % → 67 % | 97.0 px | 0.37 | 0.89 | 1660 |
| tilted | 38 % → 38 % | 107.0 px | 0.37 | 1.00 | 1010 |
| over the wet one | 76 % → 69 % | 104.8 px | 0.37 | 0.90 | 838 |
| long, no reload | 99 % → 85 % | 44.3 px | 0.36 | 0.86 | 5065 | quarters: 0.00 → 0.00 → 0.00 → 0.00

Numbers say: light vs heavy: width 148.1 → 151.1 px, dark 0.37 → 0.37; pressure barely changes the width.

## Oil · Henry Ward · Loaded flat #6a7a80 flat
Gouache 1.00 + turpentine 35 % · 84 px · 46.7 s

![Oil · Henry Ward · Loaded flat #6a7a80 flat](Oil-Henry-Ward-Loaded-flat-6a7a80-flat.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 11 % → 3 % | 30.6 px | 0.21 | 0.24 | 322 |
| heavy line | 15 % → 12 % | 42.2 px | 0.27 | 0.82 | 271 |
| pressure swell | 15 % → 9 % | 58.0 px | 0.35 | 0.57 | 178 |
| fast wave | 48 % → 28 % | 55.7 px | 0.39 | 0.58 | 648 |
| slow wave | 42 % → 28 % | 48.3 px | 0.30 | 0.67 | 1179 |
| spiral | 63 % → 33 % | 41.5 px | 0.37 | 0.53 | 1312 |
| loop | 39 % → 22 % | 50.4 px | 0.30 | 0.55 | 613 |
| tilted | 19 % → 19 % | 53.0 px | 0.37 | 1.01 | 412 |
| over the wet one | 32 % → 28 % | 36.9 px | 0.37 | 0.88 | 257 |
| long, no reload | 61 % → 31 % | 27.3 px | 0.38 | 0.52 | 1434 | quarters: 0.32 → 0.21 → 0.15 → 0.10

Numbers say: light vs heavy: width 30.6 → 42.2 px, dark 0.21 → 0.27.

## Oil · Henry Ward · Loaded flat #5a1810 flat
Gouache 1.00 + turpentine 35 % · 84 px · 47.4 s

![Oil · Henry Ward · Loaded flat #5a1810 flat](Oil-Henry-Ward-Loaded-flat-5a1810-flat.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 11 % → 3 % | 30.6 px | 0.53 | 0.24 | 200 |
| heavy line | 15 % → 12 % | 42.2 px | 0.59 | 0.82 | 262 |
| pressure swell | 15 % → 9 % | 58.0 px | 0.61 | 0.57 | 186 |
| fast wave | 48 % → 28 % | 55.7 px | 0.64 | 0.58 | 704 |
| slow wave | 42 % → 28 % | 48.3 px | 0.60 | 0.67 | 1198 |
| spiral | 63 % → 33 % | 41.5 px | 0.63 | 0.53 | 1345 |
| loop | 39 % → 22 % | 50.4 px | 0.60 | 0.55 | 600 |
| tilted | 19 % → 19 % | 53.0 px | 0.63 | 1.01 | 454 |
| over the wet one | 32 % → 28 % | 36.9 px | 0.63 | 0.88 | 277 |
| long, no reload | 61 % → 31 % | 27.3 px | 0.64 | 0.52 | 1513 | quarters: 0.56 → 0.42 → 0.34 → 0.24

Numbers say: light vs heavy: width 30.6 → 42.2 px, dark 0.53 → 0.59.

## Oil · Henry Ward · Dirty contour #1c2240 flat
Gouache 1.00 + turpentine 35 % · 34 px · 43.6 s

![Oil · Henry Ward · Dirty contour #1c2240 flat](Oil-Henry-Ward-Dirty-contour-1c2240-flat.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 11 % → 4 % | 30.7 px | 0.53 | 0.42 | 110 |
| heavy line | 24 % → 16 % | 69.3 px | 0.54 | 0.67 | 221 |
| pressure swell | 15 % → 11 % | 54.9 px | 0.58 | 0.72 | 135 |
| fast wave | 43 % → 19 % | 50.1 px | 0.63 | 0.44 | 407 |
| slow wave | 41 % → 24 % | 47.5 px | 0.59 | 0.58 | 677 |
| spiral | 59 % → 24 % | 39.1 px | 0.60 | 0.41 | 716 |
| loop | 37 % → 23 % | 47.5 px | 0.57 | 0.64 | 416 |
| tilted | 14 % → 14 % | 37.9 px | 0.63 | 1.01 | 177 |
| over the wet one | 32 % → 27 % | 52.1 px | 0.63 | 0.84 | 181 |
| long, no reload | 72 % → 28 % | 32.4 px | 0.62 | 0.39 | 1080 | quarters: 0.57 → 0.54 → 0.46 → 0.37

Numbers say: light vs heavy: width 30.7 → 69.3 px, dark 0.53 → 0.54.

## Oil · Henry Ward · Ground #22403f flat
Ink 0.65 · Watercolour 0.35 + turpentine 75 % · 160 px · 73.3 s

![Oil · Henry Ward · Ground #22403f flat](Oil-Henry-Ward-Ground-22403f-flat.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 51 % → 56 % | 148.0 px | 0.37 | 1.10 | 503 |
| heavy line | 53 % → 52 % | 153.8 px | 0.41 | 0.98 | 867 |
| pressure swell | 41 % → 50 % | 155.4 px | 0.42 | 1.21 | 538 |
| fast wave | 87 % → 93 % | 101.1 px | 0.47 | 1.06 | 1837 |
| slow wave | 88 % → 86 % | 101.4 px | 0.50 | 0.98 | 2950 |
| spiral | 93 % → 92 % | 61.6 px | 0.48 | 0.99 | 3055 |
| loop | 78 % → 78 % | 101.0 px | 0.48 | 1.00 | 1478 |
| tilted | 40 % → 40 % | 110.6 px | 0.46 | 1.01 | 875 |
| over the wet one | 77 % → 79 % | 104.0 px | 0.46 | 1.03 | 780 |
| long, no reload | 99 % → 100 % | 44.6 px | 0.49 | 1.00 | 7084 | quarters: 0.62 → 0.57 → 0.47 → 0.35

Numbers say: light vs heavy: width 148.0 → 153.8 px, dark 0.37 → 0.41; pressure barely changes the width.

## Oil · Henry Ward · Loaded flat #f0b89a filbert
Gouache 1.00 + turpentine 35 % · 84 px · 51.3 s

![Oil · Henry Ward · Loaded flat #f0b89a filbert](Oil-Henry-Ward-Loaded-flat-f0b89a-filbert.png)

A light paint: laid on a grey sheet (on white it cannot be seen); **dark** = how far it is from the grey either way.

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 8 % → 0 % | 24.3 px | 0.00 | 0.00 | 213 |
| heavy line | 19 % → 16 % | 54.3 px | 0.34 | 0.84 | 292 |
| pressure swell | 15 % → 12 % | 55.4 px | 0.30 | 0.83 | 224 |
| fast wave | 47 % → 36 % | 54.9 px | 0.25 | 0.77 | 870 |
| slow wave | 47 % → 28 % | 54.4 px | 0.28 | 0.60 | 1262 |
| spiral | 64 % → 29 % | 42.2 px | 0.24 | 0.46 | 3852 |
| loop | 38 % → 18 % | 49.3 px | 0.26 | 0.47 | 684 |
| tilted | 18 % → 19 % | 51.5 px | 0.24 | 1.00 | 403 |
| over the wet one | 36 % → 26 % | 48.2 px | 0.24 | 0.73 | 309 |
| long, no reload | 61 % → 34 % | 27.4 px | 0.24 | 0.56 | 3717 | quarters: 0.00 → 0.01 → 0.01 → 0.02

Numbers say: light vs heavy: width 24.3 → 54.3 px, dark 0.00 → 0.34; the long stroke does not run out of paint.

## Oil · Henry Ward · Dry scrub #f0b89a filbert
Gouache 1.00 + turpentine 20 % · 90 px · 41.8 s

![Oil · Henry Ward · Dry scrub #f0b89a filbert](Oil-Henry-Ward-Dry-scrub-f0b89a-filbert.png)

A light paint: laid on a grey sheet (on white it cannot be seen); **dark** = how far it is from the grey either way.

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 8 % → 0 % | 23.4 px | 0.00 | 0.00 | 214 |
| heavy line | 17 % → 5 % | 49.4 px | 0.34 | 0.28 | 295 |
| pressure swell | 15 % → 5 % | 55.6 px | 0.30 | 0.32 | 201 |
| fast wave | 51 % → 8 % | 59.4 px | 0.25 | 0.15 | 801 |
| slow wave | 40 % → 7 % | 45.8 px | 0.27 | 0.18 | 3930 |
| spiral | 68 % → 8 % | 44.6 px | 0.20 | 0.12 | 1344 |
| loop | 34 % → 1 % | 43.6 px | 0.22 | 0.03 | 676 |
| tilted | 18 % → 19 % | 51.6 px | 0.21 | 1.00 | 414 |
| over the wet one | 27 % → 6 % | 24.7 px | 0.21 | 0.22 | 2120 |
| long, no reload | 52 % → 7 % | 23.4 px | 0.21 | 0.14 | 5159 | quarters: 0.03 → 0.02 → 0.02 → 0.04

Numbers say: light vs heavy: width 23.4 → 49.4 px, dark 0.00 → 0.34; the long stroke does not run out of paint.

## Oil · Henry Ward · Dirty contour #1c2238 flat
Gouache 1.00 + turpentine 35 % · 34 px · 46.6 s

![Oil · Henry Ward · Dirty contour #1c2238 flat](Oil-Henry-Ward-Dirty-contour-1c2238-flat.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 11 % → 4 % | 30.7 px | 0.53 | 0.42 | 98 |
| heavy line | 24 % → 16 % | 69.3 px | 0.54 | 0.67 | 186 |
| pressure swell | 15 % → 11 % | 54.9 px | 0.58 | 0.72 | 122 |
| fast wave | 43 % → 19 % | 50.1 px | 0.63 | 0.44 | 361 |
| slow wave | 41 % → 24 % | 47.5 px | 0.59 | 0.58 | 669 |
| spiral | 59 % → 24 % | 39.1 px | 0.60 | 0.41 | 744 |
| loop | 37 % → 23 % | 47.5 px | 0.57 | 0.64 | 435 |
| tilted | 14 % → 14 % | 37.9 px | 0.63 | 1.01 | 192 |
| over the wet one | 32 % → 27 % | 52.1 px | 0.63 | 0.84 | 303 |
| long, no reload | 72 % → 28 % | 32.4 px | 0.62 | 0.39 | 1252 | quarters: 0.57 → 0.54 → 0.46 → 0.37

Numbers say: light vs heavy: width 30.7 → 69.3 px, dark 0.53 → 0.54.

## Oil · Henry Ward · Ground #ece8e2 flat
Gouache 1.00 + turpentine 30 % · 160 px · 84.0 s

![Oil · Henry Ward · Ground #ece8e2 flat](Oil-Henry-Ward-Ground-ece8e2-flat.png)

A light paint: laid on a grey sheet (on white it cannot be seen); **dark** = how far it is from the grey either way.

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 51 % → 43 % | 148.1 px | 0.37 | 0.84 | 698 |
| heavy line | 52 % → 45 % | 151.1 px | 0.38 | 0.87 | 844 |
| pressure swell | 41 % → 43 % | 154.5 px | 0.37 | 1.04 | 597 |
| fast wave | 85 % → 83 % | 97.9 px | 0.37 | 0.98 | 4396 |
| slow wave | 86 % → 70 % | 99.3 px | 0.37 | 0.81 | 7106 |
| spiral | 89 % → 64 % | 58.5 px | 0.37 | 0.72 | 3855 |
| loop | 75 % → 67 % | 97.0 px | 0.38 | 0.89 | 1771 |
| tilted | 38 % → 38 % | 107.0 px | 0.37 | 1.00 | 1121 |
| over the wet one | 76 % → 69 % | 104.8 px | 0.37 | 0.90 | 942 |
| long, no reload | 99 % → 85 % | 44.3 px | 0.37 | 0.86 | 7163 | quarters: 0.00 → 0.00 → 0.00 → 0.00

Numbers say: light vs heavy: width 148.1 → 151.1 px, dark 0.37 → 0.38; pressure barely changes the width.

## Oil · Henry Ward · Loaded flat #a03c1c flat
Gouache 1.00 + turpentine 35 % · 84 px · 45.3 s

![Oil · Henry Ward · Loaded flat #a03c1c flat](Oil-Henry-Ward-Loaded-flat-a03c1c-flat.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 11 % → 3 % | 30.6 px | 0.37 | 0.24 | 194 |
| heavy line | 15 % → 12 % | 42.2 px | 0.44 | 0.82 | 289 |
| pressure swell | 15 % → 9 % | 58.0 px | 0.50 | 0.57 | 193 |
| fast wave | 48 % → 28 % | 55.7 px | 0.53 | 0.58 | 856 |
| slow wave | 42 % → 28 % | 48.3 px | 0.46 | 0.67 | 1227 |
| spiral | 63 % → 33 % | 41.5 px | 0.53 | 0.53 | 1474 |
| loop | 39 % → 22 % | 50.4 px | 0.47 | 0.55 | 650 |
| tilted | 19 % → 19 % | 53.0 px | 0.51 | 1.01 | 452 |
| over the wet one | 32 % → 28 % | 36.9 px | 0.51 | 0.88 | 285 |
| long, no reload | 61 % → 31 % | 27.3 px | 0.54 | 0.52 | 1653 | quarters: 0.46 → 0.33 → 0.27 → 0.19

Numbers say: light vs heavy: width 30.6 → 42.2 px, dark 0.37 → 0.44.

## Oil · Henry Ward · Dirty contour #1f3a2c flat
Gouache 1.00 + turpentine 35 % · 34 px · 40.6 s

![Oil · Henry Ward · Dirty contour #1f3a2c flat](Oil-Henry-Ward-Dirty-contour-1f3a2c-flat.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 11 % → 4 % | 30.7 px | 0.47 | 0.42 | 102 |
| heavy line | 24 % → 16 % | 69.3 px | 0.48 | 0.67 | 275 |
| pressure swell | 15 % → 11 % | 54.9 px | 0.53 | 0.72 | 133 |
| fast wave | 43 % → 19 % | 50.1 px | 0.58 | 0.44 | 442 |
| slow wave | 41 % → 24 % | 47.5 px | 0.53 | 0.58 | 797 |
| spiral | 59 % → 24 % | 39.1 px | 0.54 | 0.41 | 766 |
| loop | 37 % → 23 % | 47.5 px | 0.51 | 0.64 | 361 |
| tilted | 14 % → 14 % | 37.9 px | 0.58 | 1.01 | 194 |
| over the wet one | 32 % → 27 % | 52.1 px | 0.58 | 0.84 | 192 |
| long, no reload | 72 % → 28 % | 32.4 px | 0.56 | 0.39 | 1176 | quarters: 0.52 → 0.48 → 0.40 → 0.31

Numbers say: light vs heavy: width 30.7 → 69.3 px, dark 0.47 → 0.48.

## Oil · Henry Ward · Loaded flat #ecc8c8 worn
Gouache 1.00 + turpentine 35 % · 84 px · 51.7 s

![Oil · Henry Ward · Loaded flat #ecc8c8 worn](Oil-Henry-Ward-Loaded-flat-ecc8c8-worn.png)

A light paint: laid on a grey sheet (on white it cannot be seen); **dark** = how far it is from the grey either way.

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 22 % → 2 % | 63.8 px | 0.30 | 0.08 | 295 |
| heavy line | 31 % → 15 % | 91.2 px | 0.33 | 0.48 | 441 |
| pressure swell | 25 % → 11 % | 94.1 px | 0.30 | 0.44 | 337 |
| fast wave | 66 % → 37 % | 76.2 px | 0.25 | 0.56 | 1020 |
| slow wave | 56 % → 32 % | 65.1 px | 0.31 | 0.57 | 1767 |
| spiral | 67 % → 30 % | 44.1 px | 0.26 | 0.44 | 1789 |
| loop | 50 % → 25 % | 65.1 px | 0.30 | 0.51 | 1081 |
| tilted | 22 % → 22 % | 62.6 px | 0.26 | 1.00 | 627 |
| over the wet one | 49 % → 35 % | 74.9 px | 0.26 | 0.71 | 557 |
| long, no reload | 90 % → 44 % | 40.3 px | 0.24 | 0.49 | 2489 | quarters: 0.00 → 0.00 → 0.01 → 0.01

Numbers say: light vs heavy: width 63.8 → 91.2 px, dark 0.30 → 0.33; the long stroke does not run out of paint.

## Oil · Henry Ward · Loaded flat #62c8e8 flat
Gouache 1.00 + turpentine 35 % · 84 px · 47.6 s

![Oil · Henry Ward · Loaded flat #62c8e8 flat](Oil-Henry-Ward-Loaded-flat-62c8e8-flat.png)

A light paint: laid on a grey sheet (on white it cannot be seen); **dark** = how far it is from the grey either way.

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 11 % → 3 % | 30.6 px | 0.34 | 0.24 | 245 |
| heavy line | 15 % → 12 % | 42.2 px | 0.30 | 0.82 | 298 |
| pressure swell | 15 % → 9 % | 58.0 px | 0.21 | 0.57 | 195 |
| fast wave | 48 % → 28 % | 55.7 px | 0.17 | 0.58 | 748 |
| slow wave | 42 % → 28 % | 48.3 px | 0.25 | 0.67 | 1221 |
| spiral | 63 % → 33 % | 41.5 px | 0.18 | 0.53 | 1471 |
| loop | 39 % → 22 % | 50.4 px | 0.23 | 0.55 | 839 |
| tilted | 19 % → 19 % | 53.0 px | 0.20 | 1.01 | 548 |
| over the wet one | 32 % → 28 % | 36.9 px | 0.20 | 0.88 | 450 |
| long, no reload | 61 % → 31 % | 27.3 px | 0.18 | 0.52 | 2036 | quarters: 0.00 → 0.01 → 0.01 → 0.01

Numbers say: light vs heavy: width 30.6 → 42.2 px, dark 0.34 → 0.30; the long stroke does not run out of paint.

## Oil · Henry Ward · Loaded flat #0f2018 flat
Gouache 1.00 + turpentine 35 % · 84 px · 48.2 s

![Oil · Henry Ward · Loaded flat #0f2018 flat](Oil-Henry-Ward-Loaded-flat-0f2018-flat.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 11 % → 3 % | 30.6 px | 0.55 | 0.24 | 246 |
| heavy line | 15 % → 12 % | 42.2 px | 0.61 | 0.82 | 342 |
| pressure swell | 15 % → 9 % | 58.0 px | 0.66 | 0.57 | 260 |
| fast wave | 48 % → 28 % | 55.7 px | 0.68 | 0.58 | 1015 |
| slow wave | 42 % → 28 % | 48.3 px | 0.63 | 0.67 | 1433 |
| spiral | 63 % → 33 % | 41.5 px | 0.68 | 0.53 | 1594 |
| loop | 39 % → 22 % | 50.4 px | 0.63 | 0.55 | 715 |
| tilted | 19 % → 19 % | 53.0 px | 0.67 | 1.01 | 488 |
| over the wet one | 32 % → 28 % | 36.9 px | 0.67 | 0.88 | 378 |
| long, no reload | 61 % → 31 % | 27.3 px | 0.69 | 0.52 | 1739 | quarters: 0.60 → 0.46 → 0.38 → 0.27

Numbers say: light vs heavy: width 30.6 → 42.2 px, dark 0.55 → 0.61.

## Oil · Henry Ward · Ground #e6e2ee flat
Gouache 1.00 + turpentine 30 % · 160 px · 81.8 s

![Oil · Henry Ward · Ground #e6e2ee flat](Oil-Henry-Ward-Ground-e6e2ee-flat.png)

A light paint: laid on a grey sheet (on white it cannot be seen); **dark** = how far it is from the grey either way.

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 51 % → 43 % | 148.1 px | 0.37 | 0.84 | 770 |
| heavy line | 52 % → 45 % | 151.1 px | 0.37 | 0.87 | 990 |
| pressure swell | 41 % → 43 % | 154.5 px | 0.37 | 1.04 | 687 |
| fast wave | 85 % → 83 % | 97.9 px | 0.36 | 0.98 | 2561 |
| slow wave | 86 % → 70 % | 99.3 px | 0.37 | 0.81 | 4659 |
| spiral | 89 % → 64 % | 58.5 px | 0.37 | 0.72 | 4224 |
| loop | 75 % → 67 % | 97.0 px | 0.37 | 0.89 | 2940 |
| tilted | 38 % → 38 % | 107.0 px | 0.37 | 1.00 | 1287 |
| over the wet one | 76 % → 69 % | 104.8 px | 0.37 | 0.90 | 938 |
| long, no reload | 99 % → 85 % | 44.3 px | 0.36 | 0.86 | 6232 | quarters: 0.00 → 0.00 → 0.00 → 0.00

Numbers say: light vs heavy: width 148.1 → 151.1 px, dark 0.37 → 0.37; pressure barely changes the width.

## Oil · Henry Ward · Dry scrub #f2f0f6 filbert
Gouache 1.00 + turpentine 20 % · 90 px · 39.7 s

![Oil · Henry Ward · Dry scrub #f2f0f6 filbert](Oil-Henry-Ward-Dry-scrub-f2f0f6-filbert.png)

A light paint: laid on a grey sheet (on white it cannot be seen); **dark** = how far it is from the grey either way.

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 8 % → 0 % | 23.4 px | 0.00 | 0.00 | 249 |
| heavy line | 17 % → 5 % | 49.3 px | 0.38 | 0.27 | 434 |
| pressure swell | 15 % → 5 % | 55.6 px | 0.36 | 0.33 | 254 |
| fast wave | 51 % → 8 % | 59.4 px | 0.32 | 0.16 | 999 |
| slow wave | 40 % → 7 % | 45.7 px | 0.34 | 0.19 | 1531 |
| spiral | 68 % → 8 % | 44.5 px | 0.29 | 0.12 | 1888 |
| loop | 34 % → 1 % | 43.6 px | 0.29 | 0.03 | 731 |
| tilted | 18 % → 19 % | 51.6 px | 0.30 | 1.00 | 497 |
| over the wet one | 27 % → 6 % | 24.7 px | 0.30 | 0.23 | 349 |
| long, no reload | 52 % → 8 % | 23.4 px | 0.29 | 0.14 | 1932 | quarters: 0.04 → 0.02 → 0.03 → 0.05

Numbers say: light vs heavy: width 23.4 → 49.3 px, dark 0.00 → 0.38; the long stroke does not run out of paint.

## Oil · Henry Ward · Dirty contour #1e4a78 flat
Gouache 1.00 + turpentine 35 % · 34 px · 43.4 s

![Oil · Henry Ward · Dirty contour #1e4a78 flat](Oil-Henry-Ward-Dirty-contour-1e4a78-flat.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 11 % → 4 % | 30.7 px | 0.41 | 0.42 | 108 |
| heavy line | 24 % → 16 % | 69.3 px | 0.43 | 0.67 | 251 |
| pressure swell | 15 % → 11 % | 54.9 px | 0.47 | 0.72 | 125 |
| fast wave | 43 % → 19 % | 50.1 px | 0.53 | 0.44 | 468 |
| slow wave | 41 % → 24 % | 47.5 px | 0.48 | 0.58 | 895 |
| spiral | 59 % → 24 % | 39.1 px | 0.49 | 0.41 | 769 |
| loop | 37 % → 23 % | 47.5 px | 0.46 | 0.64 | 434 |
| tilted | 14 % → 14 % | 37.9 px | 0.53 | 1.01 | 225 |
| over the wet one | 32 % → 27 % | 52.1 px | 0.53 | 0.84 | 213 |
| long, no reload | 72 % → 28 % | 32.4 px | 0.51 | 0.39 | 1369 | quarters: 0.47 → 0.43 → 0.34 → 0.25

Numbers say: light vs heavy: width 30.7 → 69.3 px, dark 0.41 → 0.43.

## Oil · Henry Ward · Dirty contour #141414 flat
Gouache 1.00 + turpentine 35 % · 34 px · 45.0 s

![Oil · Henry Ward · Dirty contour #141414 flat](Oil-Henry-Ward-Dirty-contour-141414-flat.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 11 % → 4 % | 30.7 px | 0.60 | 0.42 | 95 |
| heavy line | 24 % → 16 % | 69.3 px | 0.61 | 0.67 | 263 |
| pressure swell | 15 % → 11 % | 54.9 px | 0.64 | 0.72 | 158 |
| fast wave | 43 % → 19 % | 50.1 px | 0.68 | 0.44 | 510 |
| slow wave | 41 % → 24 % | 47.5 px | 0.65 | 0.58 | 842 |
| spiral | 59 % → 24 % | 39.1 px | 0.65 | 0.41 | 760 |
| loop | 37 % → 23 % | 47.5 px | 0.63 | 0.64 | 766 |
| tilted | 14 % → 14 % | 37.9 px | 0.67 | 1.01 | 249 |
| over the wet one | 32 % → 27 % | 52.1 px | 0.67 | 0.84 | 509 |
| long, no reload | 72 % → 28 % | 32.4 px | 0.67 | 0.39 | 1281 | quarters: 0.61 → 0.59 → 0.51 → 0.42

Numbers say: light vs heavy: width 30.7 → 69.3 px, dark 0.60 → 0.61.

## Oil · Henry Ward · Dry scrub #c89038 filbert
Gouache 1.00 + turpentine 20 % · 90 px · 39.8 s

![Oil · Henry Ward · Dry scrub #c89038 filbert](Oil-Henry-Ward-Dry-scrub-c89038-filbert.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 8 % → 0 % | 23.4 px | 0.00 | 0.00 | 296 |
| heavy line | 17 % → 5 % | 49.4 px | 0.12 | 0.28 | 334 |
| pressure swell | 15 % → 5 % | 55.6 px | 0.17 | 0.32 | 242 |
| fast wave | 51 % → 8 % | 59.4 px | 0.21 | 0.15 | 1609 |
| slow wave | 40 % → 7 % | 45.8 px | 0.18 | 0.18 | 2063 |
| spiral | 68 % → 8 % | 44.6 px | 0.29 | 0.12 | 1606 |
| loop | 34 % → 1 % | 43.6 px | 0.23 | 0.03 | 752 |
| tilted | 18 % → 19 % | 51.6 px | 0.26 | 1.00 | 437 |
| over the wet one | 27 % → 6 % | 24.7 px | 0.26 | 0.22 | 322 |
| long, no reload | 52 % → 7 % | 23.4 px | 0.27 | 0.14 | 1834 | quarters: 0.09 → 0.14 → 0.10 → 0.04

Numbers say: light vs heavy: width 23.4 → 49.4 px, dark 0.00 → 0.12.

## Oil · Henry Ward · Ground #efe8b8 flat
Gouache 1.00 + turpentine 30 % · 160 px · 80.4 s

![Oil · Henry Ward · Ground #efe8b8 flat](Oil-Henry-Ward-Ground-efe8b8-flat.png)

A light paint: laid on a grey sheet (on white it cannot be seen); **dark** = how far it is from the grey either way.

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 51 % → 43 % | 148.1 px | 0.37 | 0.84 | 1283 |
| heavy line | 52 % → 45 % | 151.1 px | 0.37 | 0.87 | 1333 |
| pressure swell | 41 % → 43 % | 154.5 px | 0.37 | 1.04 | 1047 |
| fast wave | 85 % → 83 % | 97.9 px | 0.36 | 0.98 | 2569 |
| slow wave | 86 % → 70 % | 99.3 px | 0.37 | 0.81 | 4321 |
| spiral | 89 % → 64 % | 58.5 px | 0.37 | 0.72 | 4591 |
| loop | 75 % → 67 % | 97.0 px | 0.37 | 0.89 | 2589 |
| tilted | 38 % → 38 % | 107.0 px | 0.37 | 1.00 | 1314 |
| over the wet one | 76 % → 69 % | 104.8 px | 0.37 | 0.90 | 955 |
| long, no reload | 99 % → 85 % | 44.3 px | 0.36 | 0.86 | 6077 | quarters: 0.00 → 0.00 → 0.00 → 0.00

Numbers say: light vs heavy: width 148.1 → 151.1 px, dark 0.37 → 0.37; pressure barely changes the width.

## Oil · Henry Ward · Loaded flat #a89ac8 worn
Gouache 1.00 + turpentine 35 % · 84 px · 49.9 s

![Oil · Henry Ward · Loaded flat #a89ac8 worn](Oil-Henry-Ward-Loaded-flat-a89ac8-worn.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 22 % → 2 % | 63.8 px | 0.10 | 0.08 | 306 |
| heavy line | 31 % → 15 % | 91.2 px | 0.13 | 0.48 | 499 |
| pressure swell | 25 % → 11 % | 94.1 px | 0.18 | 0.44 | 339 |
| fast wave | 66 % → 37 % | 76.2 px | 0.24 | 0.56 | 1203 |
| slow wave | 56 % → 32 % | 65.1 px | 0.15 | 0.57 | 2000 |
| spiral | 67 % → 30 % | 44.1 px | 0.22 | 0.44 | 1891 |
| loop | 50 % → 25 % | 65.1 px | 0.13 | 0.51 | 1074 |
| tilted | 22 % → 22 % | 62.6 px | 0.21 | 1.00 | 662 |
| over the wet one | 49 % → 35 % | 74.9 px | 0.21 | 0.71 | 725 |
| long, no reload | 90 % → 44 % | 40.3 px | 0.25 | 0.49 | 2392 | quarters: 0.23 → 0.22 → 0.13 → 0.07

Numbers say: light vs heavy: width 63.8 → 91.2 px, dark 0.10 → 0.13.

## Oil · Henry Ward · Dirty contour #2a2418 flat
Gouache 1.00 + turpentine 35 % · 34 px · 41.3 s

![Oil · Henry Ward · Dirty contour #2a2418 flat](Oil-Henry-Ward-Dirty-contour-2a2418-flat.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 11 % → 4 % | 30.7 px | 0.52 | 0.42 | 122 |
| heavy line | 24 % → 16 % | 69.3 px | 0.54 | 0.67 | 242 |
| pressure swell | 15 % → 11 % | 54.9 px | 0.57 | 0.72 | 173 |
| fast wave | 43 % → 19 % | 50.1 px | 0.62 | 0.44 | 450 |
| slow wave | 41 % → 24 % | 47.5 px | 0.58 | 0.58 | 846 |
| spiral | 59 % → 24 % | 39.1 px | 0.59 | 0.41 | 813 |
| loop | 37 % → 23 % | 47.5 px | 0.57 | 0.64 | 620 |
| tilted | 14 % → 14 % | 37.9 px | 0.62 | 1.01 | 204 |
| over the wet one | 32 % → 27 % | 52.1 px | 0.62 | 0.84 | 229 |
| long, no reload | 72 % → 28 % | 32.4 px | 0.61 | 0.39 | 1469 | quarters: 0.56 → 0.53 → 0.45 → 0.36

Numbers say: light vs heavy: width 30.7 → 69.3 px, dark 0.52 → 0.54.

## Oil · Henry Ward · Loaded flat #2a2418 filbert
Gouache 1.00 + turpentine 35 % · 84 px · 45.8 s

![Oil · Henry Ward · Loaded flat #2a2418 filbert](Oil-Henry-Ward-Loaded-flat-2a2418-filbert.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 8 % → 0 % | 24.3 px | 0.00 | 0.00 | 341 |
| heavy line | 19 % → 16 % | 54.3 px | 0.55 | 0.84 | 437 |
| pressure swell | 15 % → 12 % | 55.4 px | 0.58 | 0.83 | 227 |
| fast wave | 47 % → 36 % | 54.9 px | 0.62 | 0.77 | 1038 |
| slow wave | 47 % → 28 % | 54.4 px | 0.60 | 0.60 | 1502 |
| spiral | 64 % → 29 % | 42.2 px | 0.64 | 0.46 | 1430 |
| loop | 38 % → 18 % | 49.3 px | 0.62 | 0.47 | 817 |
| tilted | 18 % → 19 % | 51.5 px | 0.63 | 1.00 | 450 |
| over the wet one | 36 % → 26 % | 48.2 px | 0.63 | 0.73 | 330 |
| long, no reload | 61 % → 34 % | 27.4 px | 0.63 | 0.56 | 1774 | quarters: 0.56 → 0.45 → 0.35 → 0.17

Numbers say: light vs heavy: width 24.3 → 54.3 px, dark 0.00 → 0.55.

## Oil · Henry Ward · Dry scrub #efeee6 worn
Gouache 1.00 + turpentine 20 % · 90 px · 35.7 s

![Oil · Henry Ward · Dry scrub #efeee6 worn](Oil-Henry-Ward-Dry-scrub-efeee6-worn.png)

A light paint: laid on a grey sheet (on white it cannot be seen); **dark** = how far it is from the grey either way.

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 17 % → 0 % | 48.2 px | 0.00 | 0.00 | 321 |
| heavy line | 30 % → 0 % | 85.8 px | 0.32 | 0.01 | 470 |
| pressure swell | 21 % → 6 % | 77.1 px | 0.31 | 0.28 | 516 |
| fast wave | 68 % → 7 % | 78.5 px | 0.26 | 0.10 | 1531 |
| slow wave | 51 % → 4 % | 58.7 px | 0.29 | 0.07 | 2025 |
| spiral | 72 % → 10 % | 47.6 px | 0.26 | 0.13 | 2192 |
| loop | 51 % → 1 % | 66.3 px | 0.28 | 0.01 | 926 |
| tilted | 20 % → 20 % | 56.8 px | 0.26 | 1.00 | 594 |
| over the wet one | 41 % → 7 % | 56.6 px | 0.26 | 0.17 | 436 |
| long, no reload | 79 % → 0 % | 35.4 px | 0.23 | 0.00 | 1929 | quarters: 0.01 → 0.02 → 0.01 → 0.02

Numbers say: light vs heavy: width 48.2 → 85.8 px, dark 0.00 → 0.32; the long stroke does not run out of paint.

## Oil · Henry Ward · Ground #e6e2f0 flat
Gouache 1.00 + turpentine 30 % · 160 px · 78.9 s

![Oil · Henry Ward · Ground #e6e2f0 flat](Oil-Henry-Ward-Ground-e6e2f0-flat.png)

A light paint: laid on a grey sheet (on white it cannot be seen); **dark** = how far it is from the grey either way.

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 51 % → 43 % | 148.1 px | 0.37 | 0.84 | 922 |
| heavy line | 52 % → 45 % | 151.1 px | 0.37 | 0.87 | 1089 |
| pressure swell | 41 % → 43 % | 154.5 px | 0.37 | 1.04 | 817 |
| fast wave | 85 % → 83 % | 97.9 px | 0.36 | 0.98 | 2465 |
| slow wave | 86 % → 70 % | 99.3 px | 0.37 | 0.81 | 4337 |
| spiral | 89 % → 64 % | 58.5 px | 0.37 | 0.72 | 3817 |
| loop | 75 % → 67 % | 97.0 px | 0.37 | 0.89 | 2010 |
| tilted | 38 % → 38 % | 107.0 px | 0.37 | 1.00 | 1414 |
| over the wet one | 76 % → 69 % | 104.8 px | 0.37 | 0.90 | 945 |
| long, no reload | 99 % → 85 % | 44.3 px | 0.36 | 0.86 | 5278 | quarters: 0.00 → 0.00 → 0.00 → 0.00

Numbers say: light vs heavy: width 148.1 → 151.1 px, dark 0.37 → 0.37; pressure barely changes the width.

## Oil · Henry Ward · Loaded flat #a8b84a worn
Gouache 1.00 + turpentine 35 % · 84 px · 47.0 s

![Oil · Henry Ward · Loaded flat #a8b84a worn](Oil-Henry-Ward-Loaded-flat-a8b84a-worn.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 22 % → 2 % | 63.8 px | 0.08 | 0.08 | 321 |
| heavy line | 31 % → 15 % | 91.2 px | 0.11 | 0.48 | 619 |
| pressure swell | 25 % → 11 % | 94.1 px | 0.16 | 0.44 | 353 |
| fast wave | 66 % → 37 % | 76.2 px | 0.21 | 0.56 | 1242 |
| slow wave | 56 % → 32 % | 65.1 px | 0.13 | 0.57 | 1866 |
| spiral | 67 % → 30 % | 44.1 px | 0.20 | 0.44 | 1843 |
| loop | 50 % → 25 % | 65.1 px | 0.12 | 0.51 | 873 |
| tilted | 22 % → 22 % | 62.6 px | 0.19 | 1.00 | 523 |
| over the wet one | 49 % → 35 % | 74.9 px | 0.19 | 0.71 | 552 |
| long, no reload | 90 % → 44 % | 40.3 px | 0.22 | 0.49 | 2414 | quarters: 0.21 → 0.20 → 0.12 → 0.07

Numbers say: light vs heavy: width 63.8 → 91.2 px, dark 0.08 → 0.11.

## Oil · Henry Ward · Thin veil #5a8a6a flat
Watercolour 0.93 · Ink 0.07 + turpentine 80 % · 96 px · 42.0 s

![Oil · Henry Ward · Thin veil #5a8a6a flat](Oil-Henry-Ward-Thin-veil-5a8a6a-flat.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 3 % → 4 % | 9.5 px | 0.02 | 1.09 | 320 |
| heavy line | 17 % → 20 % | 50.1 px | 0.06 | 1.13 | 280 |
| pressure swell | 12 % → 14 % | 44.3 px | 0.06 | 1.21 | 192 |
| fast wave | 47 % → 54 % | 54.4 px | 0.06 | 1.14 | 805 |
| slow wave | 48 % → 55 % | 54.9 px | 0.06 | 1.16 | 1438 |
| spiral | 65 % → 70 % | 42.6 px | 0.06 | 1.09 | 1671 |
| loop | 40 % → 48 % | 52.2 px | 0.05 | 1.19 | 784 |
| tilted | 18 % → 19 % | 50.9 px | 0.07 | 1.03 | 828 |
| over the wet one | 28 % → 31 % | 28.0 px | 0.07 | 1.11 | 417 |
| long, no reload | 62 % → 78 % | 27.6 px | 0.06 | 1.26 | 2030 | quarters: 0.06 → 0.06 → 0.04 → 0.03

Numbers say: light vs heavy: width 9.5 → 50.1 px, dark 0.02 → 0.06.

## Oil · Henry Ward · Loaded flat #4a1420 worn
Gouache 1.00 + turpentine 35 % · 84 px · 49.3 s

![Oil · Henry Ward · Loaded flat #4a1420 worn](Oil-Henry-Ward-Loaded-flat-4a1420-worn.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 22 % → 2 % | 63.8 px | 0.49 | 0.08 | 307 |
| heavy line | 31 % → 15 % | 91.2 px | 0.51 | 0.48 | 434 |
| pressure swell | 25 % → 11 % | 94.1 px | 0.52 | 0.44 | 303 |
| fast wave | 66 % → 37 % | 76.2 px | 0.55 | 0.56 | 1071 |
| slow wave | 56 % → 32 % | 65.1 px | 0.52 | 0.57 | 2250 |
| spiral | 67 % → 30 % | 44.1 px | 0.54 | 0.44 | 1840 |
| loop | 50 % → 25 % | 65.1 px | 0.50 | 0.51 | 1163 |
| tilted | 22 % → 22 % | 62.6 px | 0.54 | 1.00 | 486 |
| over the wet one | 49 % → 35 % | 74.9 px | 0.54 | 0.71 | 524 |
| long, no reload | 90 % → 44 % | 40.3 px | 0.56 | 0.49 | 2136 | quarters: 0.55 → 0.54 → 0.48 → 0.41

Numbers say: light vs heavy: width 63.8 → 91.2 px, dark 0.49 → 0.51.

## Oil · Henry Ward · Dirty contour #2a0a10 flat
Gouache 1.00 + turpentine 35 % · 34 px · 42.1 s

![Oil · Henry Ward · Dirty contour #2a0a10 flat](Oil-Henry-Ward-Dirty-contour-2a0a10-flat.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 11 % → 4 % | 30.7 px | 0.62 | 0.42 | 108 |
| heavy line | 24 % → 16 % | 69.3 px | 0.63 | 0.67 | 203 |
| pressure swell | 15 % → 11 % | 54.9 px | 0.64 | 0.72 | 138 |
| fast wave | 43 % → 19 % | 50.1 px | 0.67 | 0.44 | 421 |
| slow wave | 41 % → 24 % | 47.5 px | 0.65 | 0.58 | 684 |
| spiral | 59 % → 24 % | 39.1 px | 0.65 | 0.41 | 816 |
| loop | 37 % → 23 % | 47.5 px | 0.64 | 0.64 | 396 |
| tilted | 14 % → 14 % | 37.9 px | 0.66 | 1.01 | 186 |
| over the wet one | 32 % → 27 % | 52.1 px | 0.66 | 0.84 | 189 |
| long, no reload | 72 % → 28 % | 32.4 px | 0.66 | 0.39 | 1108 | quarters: 0.61 → 0.58 → 0.50 → 0.41

Numbers say: light vs heavy: width 30.7 → 69.3 px, dark 0.62 → 0.63.

## Oil · Henry Ward · Dry scrub #c0506a worn
Gouache 1.00 + turpentine 20 % · 90 px · 37.1 s

![Oil · Henry Ward · Dry scrub #c0506a worn](Oil-Henry-Ward-Dry-scrub-c0506a-worn.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 17 % → 0 % | 48.2 px | 0.00 | 0.00 | 275 |
| heavy line | 30 % → 0 % | 85.8 px | 0.26 | 0.01 | 394 |
| pressure swell | 21 % → 6 % | 77.1 px | 0.26 | 0.28 | 330 |
| fast wave | 68 % → 7 % | 78.5 px | 0.34 | 0.10 | 1122 |
| slow wave | 51 % → 4 % | 58.7 px | 0.28 | 0.07 | 1746 |
| spiral | 72 % → 9 % | 47.6 px | 0.35 | 0.13 | 1770 |
| loop | 51 % → 1 % | 66.3 px | 0.26 | 0.01 | 859 |
| tilted | 20 % → 20 % | 56.8 px | 0.34 | 1.00 | 512 |
| over the wet one | 41 % → 7 % | 56.6 px | 0.34 | 0.16 | 371 |
| long, no reload | 79 % → 0 % | 35.4 px | 0.38 | 0.00 | 2008 | quarters: 0.21 → 0.16 → 0.16 → 0.11

Numbers say: light vs heavy: width 48.2 → 85.8 px, dark 0.00 → 0.26.

## Oil · Henry Ward · Ground #d8d4c8 flat
Ink 0.65 · Watercolour 0.35 + turpentine 75 % · 160 px · 75.5 s

![Oil · Henry Ward · Ground #d8d4c8 flat](Oil-Henry-Ward-Ground-d8d4c8-flat.png)

A light paint: laid on a grey sheet (on white it cannot be seen); **dark** = how far it is from the grey either way.

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 51 % → 56 % | 148.0 px | 0.06 | 1.10 | 558 |
| heavy line | 53 % → 52 % | 153.8 px | 0.06 | 0.98 | 922 |
| pressure swell | 41 % → 50 % | 155.4 px | 0.06 | 1.21 | 616 |
| fast wave | 87 % → 93 % | 101.1 px | 0.05 | 1.06 | 1911 |
| slow wave | 88 % → 86 % | 101.4 px | 0.04 | 0.98 | 3128 |
| spiral | 93 % → 92 % | 61.6 px | 0.04 | 0.99 | 3149 |
| loop | 78 % → 78 % | 101.0 px | 0.04 | 1.00 | 2084 |
| tilted | 40 % → 40 % | 110.6 px | 0.05 | 1.01 | 1172 |
| over the wet one | 77 % → 79 % | 104.0 px | 0.05 | 1.03 | 1798 |
| long, no reload | 99 % → 100 % | 44.6 px | 0.04 | 1.00 | 7826 | quarters: 0.01 → 0.02 → 0.04 → 0.07

Numbers say: light vs heavy: width 148.0 → 153.8 px, dark 0.06 → 0.06; pressure barely changes the width; the long stroke does not run out of paint.

## Oil · Henry Ward · Loaded flat #e8d8b0 flat
Gouache 1.00 + turpentine 35 % · 84 px · 46.1 s

![Oil · Henry Ward · Loaded flat #e8d8b0 flat](Oil-Henry-Ward-Loaded-flat-e8d8b0-flat.png)

A light paint: laid on a grey sheet (on white it cannot be seen); **dark** = how far it is from the grey either way.

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 11 % → 3 % | 30.6 px | 0.42 | 0.24 | 215 |
| heavy line | 15 % → 12 % | 42.2 px | 0.40 | 0.82 | 289 |
| pressure swell | 15 % → 9 % | 58.0 px | 0.31 | 0.57 | 192 |
| fast wave | 48 % → 28 % | 55.7 px | 0.28 | 0.58 | 729 |
| slow wave | 42 % → 28 % | 48.3 px | 0.34 | 0.67 | 1303 |
| spiral | 63 % → 33 % | 41.5 px | 0.28 | 0.53 | 1329 |
| loop | 39 % → 22 % | 50.4 px | 0.32 | 0.55 | 658 |
| tilted | 19 % → 19 % | 53.0 px | 0.30 | 1.01 | 418 |
| over the wet one | 32 % → 28 % | 36.9 px | 0.30 | 0.88 | 268 |
| long, no reload | 61 % → 31 % | 27.3 px | 0.28 | 0.52 | 2094 | quarters: 0.00 → 0.01 → 0.01 → 0.02

Numbers say: light vs heavy: width 30.6 → 42.2 px, dark 0.42 → 0.40; the long stroke does not run out of paint.

## Oil · Henry Ward · Dry scrub #f2ead0 filbert
Gouache 1.00 + turpentine 20 % · 90 px · 39.7 s

![Oil · Henry Ward · Dry scrub #f2ead0 filbert](Oil-Henry-Ward-Dry-scrub-f2ead0-filbert.png)

A light paint: laid on a grey sheet (on white it cannot be seen); **dark** = how far it is from the grey either way.

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 8 % → 0 % | 23.4 px | 0.00 | 0.00 | 241 |
| heavy line | 17 % → 5 % | 49.3 px | 0.38 | 0.27 | 308 |
| pressure swell | 15 % → 5 % | 55.6 px | 0.35 | 0.33 | 224 |
| fast wave | 51 % → 8 % | 59.4 px | 0.31 | 0.16 | 836 |
| slow wave | 40 % → 7 % | 45.7 px | 0.33 | 0.19 | 1359 |
| spiral | 68 % → 8 % | 44.5 px | 0.28 | 0.12 | 1545 |
| loop | 34 % → 1 % | 43.6 px | 0.28 | 0.03 | 942 |
| tilted | 18 % → 19 % | 51.6 px | 0.28 | 1.00 | 575 |
| over the wet one | 27 % → 6 % | 24.7 px | 0.28 | 0.23 | 407 |
| long, no reload | 52 % → 8 % | 23.4 px | 0.28 | 0.14 | 3370 | quarters: 0.04 → 0.02 → 0.03 → 0.05

Numbers say: light vs heavy: width 23.4 → 49.3 px, dark 0.00 → 0.38; the long stroke does not run out of paint.

## Oil · Henry Ward · Loaded flat #2a1428 flat
Gouache 1.00 + turpentine 35 % · 84 px · 46.4 s

![Oil · Henry Ward · Loaded flat #2a1428 flat](Oil-Henry-Ward-Loaded-flat-2a1428-flat.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 11 % → 3 % | 30.6 px | 0.55 | 0.24 | 242 |
| heavy line | 15 % → 12 % | 42.2 px | 0.61 | 0.82 | 337 |
| pressure swell | 15 % → 9 % | 58.0 px | 0.66 | 0.57 | 246 |
| fast wave | 48 % → 28 % | 55.7 px | 0.68 | 0.58 | 1066 |
| slow wave | 42 % → 28 % | 48.3 px | 0.63 | 0.67 | 1799 |
| spiral | 63 % → 33 % | 41.5 px | 0.68 | 0.53 | 2241 |
| loop | 39 % → 22 % | 50.4 px | 0.63 | 0.55 | 1257 |
| tilted | 19 % → 19 % | 53.0 px | 0.67 | 1.01 | 576 |
| over the wet one | 32 % → 28 % | 36.9 px | 0.67 | 0.88 | 327 |
| long, no reload | 61 % → 31 % | 27.3 px | 0.68 | 0.52 | 1575 | quarters: 0.60 → 0.46 → 0.38 → 0.27

Numbers say: light vs heavy: width 30.6 → 42.2 px, dark 0.55 → 0.61.

## Oil · Henry Ward · Ground #e8e4e0 flat
Gouache 1.00 + turpentine 30 % · 160 px · 79.2 s

![Oil · Henry Ward · Ground #e8e4e0 flat](Oil-Henry-Ward-Ground-e8e4e0-flat.png)

A light paint: laid on a grey sheet (on white it cannot be seen); **dark** = how far it is from the grey either way.

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 51 % → 43 % | 148.1 px | 0.37 | 0.84 | 922 |
| heavy line | 52 % → 45 % | 151.1 px | 0.37 | 0.87 | 1949 |
| pressure swell | 41 % → 43 % | 154.5 px | 0.37 | 1.04 | 1076 |
| fast wave | 85 % → 83 % | 97.9 px | 0.36 | 0.98 | 4356 |
| slow wave | 86 % → 70 % | 99.3 px | 0.37 | 0.81 | 3919 |
| spiral | 89 % → 64 % | 58.5 px | 0.37 | 0.72 | 3429 |
| loop | 75 % → 67 % | 97.0 px | 0.37 | 0.89 | 1748 |
| tilted | 38 % → 38 % | 107.0 px | 0.37 | 1.00 | 1022 |
| over the wet one | 76 % → 69 % | 104.8 px | 0.37 | 0.90 | 877 |
| long, no reload | 99 % → 85 % | 44.3 px | 0.36 | 0.86 | 5512 | quarters: 0.00 → 0.00 → 0.00 → 0.00

Numbers say: light vs heavy: width 148.1 → 151.1 px, dark 0.37 → 0.37; pressure barely changes the width.

## Oil · Henry Ward · Loaded flat #8a2a18 filbert
Gouache 1.00 + turpentine 35 % · 84 px · 48.6 s

![Oil · Henry Ward · Loaded flat #8a2a18 filbert](Oil-Henry-Ward-Loaded-flat-8a2a18-filbert.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 8 % → 0 % | 24.3 px | 0.00 | 0.00 | 436 |
| heavy line | 19 % → 16 % | 54.3 px | 0.50 | 0.84 | 904 |
| pressure swell | 15 % → 12 % | 55.4 px | 0.52 | 0.83 | 338 |
| fast wave | 47 % → 36 % | 54.9 px | 0.56 | 0.77 | 1409 |
| slow wave | 47 % → 28 % | 54.4 px | 0.54 | 0.60 | 2604 |
| spiral | 64 % → 29 % | 42.2 px | 0.57 | 0.46 | 1436 |
| loop | 38 % → 18 % | 49.3 px | 0.55 | 0.47 | 697 |
| tilted | 18 % → 19 % | 51.5 px | 0.57 | 1.00 | 385 |
| over the wet one | 36 % → 26 % | 48.2 px | 0.57 | 0.73 | 353 |
| long, no reload | 61 % → 34 % | 27.4 px | 0.57 | 0.56 | 1727 | quarters: 0.50 → 0.40 → 0.31 → 0.15

Numbers say: light vs heavy: width 24.3 → 54.3 px, dark 0.00 → 0.50.

## Oil · Henry Ward · Loaded flat #a8c8dc filbert
Gouache 1.00 + turpentine 35 % · 84 px · 46.1 s

![Oil · Henry Ward · Loaded flat #a8c8dc filbert](Oil-Henry-Ward-Loaded-flat-a8c8dc-filbert.png)

A light paint: laid on a grey sheet (on white it cannot be seen); **dark** = how far it is from the grey either way.

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 8 % → 0 % | 24.3 px | 0.00 | 0.00 | 344 |
| heavy line | 19 % → 16 % | 54.3 px | 0.35 | 0.84 | 685 |
| pressure swell | 15 % → 12 % | 55.4 px | 0.30 | 0.83 | 460 |
| fast wave | 47 % → 36 % | 54.9 px | 0.26 | 0.77 | 903 |
| slow wave | 47 % → 28 % | 54.4 px | 0.29 | 0.60 | 1335 |
| spiral | 64 % → 29 % | 42.2 px | 0.25 | 0.46 | 1363 |
| loop | 38 % → 18 % | 49.3 px | 0.26 | 0.47 | 675 |
| tilted | 18 % → 19 % | 51.5 px | 0.24 | 1.00 | 388 |
| over the wet one | 36 % → 26 % | 48.2 px | 0.24 | 0.73 | 268 |
| long, no reload | 61 % → 34 % | 27.4 px | 0.25 | 0.56 | 1710 | quarters: 0.00 → 0.01 → 0.01 → 0.02

Numbers say: light vs heavy: width 24.3 → 54.3 px, dark 0.00 → 0.35; the long stroke does not run out of paint.

## Oil · Henry Ward · Dry scrub #d8e8f0 filbert
Gouache 1.00 + turpentine 20 % · 90 px · 37.8 s

![Oil · Henry Ward · Dry scrub #d8e8f0 filbert](Oil-Henry-Ward-Dry-scrub-d8e8f0-filbert.png)

A light paint: laid on a grey sheet (on white it cannot be seen); **dark** = how far it is from the grey either way.

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 8 % → 0 % | 23.4 px | 0.00 | 0.00 | 235 |
| heavy line | 17 % → 5 % | 49.3 px | 0.38 | 0.27 | 318 |
| pressure swell | 15 % → 5 % | 55.6 px | 0.35 | 0.33 | 230 |
| fast wave | 51 % → 8 % | 59.4 px | 0.30 | 0.16 | 848 |
| slow wave | 40 % → 7 % | 45.7 px | 0.33 | 0.19 | 1556 |
| spiral | 68 % → 8 % | 44.5 px | 0.27 | 0.12 | 1469 |
| loop | 34 % → 1 % | 43.6 px | 0.28 | 0.03 | 651 |
| tilted | 18 % → 19 % | 51.6 px | 0.28 | 1.00 | 396 |
| over the wet one | 27 % → 6 % | 24.7 px | 0.28 | 0.23 | 266 |
| long, no reload | 52 % → 8 % | 23.4 px | 0.28 | 0.14 | 1753 | quarters: 0.04 → 0.02 → 0.03 → 0.05

Numbers say: light vs heavy: width 23.4 → 49.3 px, dark 0.00 → 0.38; the long stroke does not run out of paint.

## Oil · Henry Ward · Ground #3a3a34 flat
Ink 0.65 · Watercolour 0.35 + turpentine 75 % · 160 px · 67.8 s

![Oil · Henry Ward · Ground #3a3a34 flat](Oil-Henry-Ward-Ground-3a3a34-flat.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 51 % → 56 % | 148.0 px | 0.36 | 1.10 | 538 |
| heavy line | 53 % → 52 % | 153.8 px | 0.40 | 0.98 | 893 |
| pressure swell | 41 % → 50 % | 155.4 px | 0.41 | 1.21 | 563 |
| fast wave | 87 % → 93 % | 101.1 px | 0.45 | 1.06 | 2005 |
| slow wave | 88 % → 86 % | 101.4 px | 0.49 | 0.98 | 3053 |
| spiral | 93 % → 92 % | 61.6 px | 0.47 | 0.99 | 3143 |
| loop | 78 % → 78 % | 101.0 px | 0.47 | 1.00 | 1476 |
| tilted | 40 % → 40 % | 110.6 px | 0.45 | 1.01 | 959 |
| over the wet one | 77 % → 79 % | 104.0 px | 0.45 | 1.03 | 841 |
| long, no reload | 99 % → 100 % | 44.6 px | 0.48 | 1.00 | 6527 | quarters: 0.62 → 0.57 → 0.47 → 0.34

Numbers say: light vs heavy: width 148.0 → 153.8 px, dark 0.36 → 0.40; pressure barely changes the width.

## Oil · Henry Ward · Loaded flat #8a906a worn
Gouache 1.00 + turpentine 35 % · 84 px · 48.8 s

![Oil · Henry Ward · Loaded flat #8a906a worn](Oil-Henry-Ward-Loaded-flat-8a906a-worn.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 22 % → 2 % | 63.8 px | 0.15 | 0.08 | 281 |
| heavy line | 31 % → 15 % | 91.2 px | 0.18 | 0.48 | 405 |
| pressure swell | 25 % → 11 % | 94.1 px | 0.23 | 0.44 | 299 |
| fast wave | 66 % → 37 % | 76.2 px | 0.29 | 0.56 | 1032 |
| slow wave | 56 % → 32 % | 65.1 px | 0.20 | 0.57 | 1740 |
| spiral | 67 % → 30 % | 44.1 px | 0.27 | 0.44 | 1636 |
| loop | 50 % → 25 % | 65.1 px | 0.19 | 0.51 | 1016 |
| tilted | 22 % → 22 % | 62.6 px | 0.26 | 1.00 | 488 |
| over the wet one | 49 % → 35 % | 74.9 px | 0.26 | 0.71 | 511 |
| long, no reload | 90 % → 44 % | 40.3 px | 0.30 | 0.49 | 2464 | quarters: 0.28 → 0.27 → 0.17 → 0.09

Numbers say: light vs heavy: width 63.8 → 91.2 px, dark 0.15 → 0.18.

## Oil · Henry Ward · Loaded flat #7a8458 flat
Gouache 1.00 + turpentine 35 % · 84 px · 44.9 s

![Oil · Henry Ward · Loaded flat #7a8458 flat](Oil-Henry-Ward-Loaded-flat-7a8458-flat.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 11 % → 3 % | 30.6 px | 0.18 | 0.24 | 220 |
| heavy line | 15 % → 12 % | 42.2 px | 0.25 | 0.82 | 256 |
| pressure swell | 15 % → 9 % | 58.0 px | 0.32 | 0.57 | 196 |
| fast wave | 48 % → 28 % | 55.7 px | 0.37 | 0.58 | 709 |
| slow wave | 42 % → 28 % | 48.3 px | 0.28 | 0.67 | 1237 |
| spiral | 63 % → 33 % | 41.5 px | 0.35 | 0.53 | 1345 |
| loop | 39 % → 22 % | 50.4 px | 0.28 | 0.55 | 726 |
| tilted | 19 % → 19 % | 53.0 px | 0.35 | 1.01 | 477 |
| over the wet one | 32 % → 28 % | 36.9 px | 0.35 | 0.88 | 385 |
| long, no reload | 61 % → 31 % | 27.3 px | 0.36 | 0.52 | 2038 | quarters: 0.30 → 0.19 → 0.14 → 0.10

Numbers say: light vs heavy: width 30.6 → 42.2 px, dark 0.18 → 0.25.

## Oil · Henry Ward · Dry scrub #a8ae88 filbert
Gouache 1.00 + turpentine 20 % · 90 px · 38.6 s

![Oil · Henry Ward · Dry scrub #a8ae88 filbert](Oil-Henry-Ward-Dry-scrub-a8ae88-filbert.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 8 % → 0 % | 23.4 px | 0.00 | 0.00 | 233 |
| heavy line | 17 % → 5 % | 49.4 px | 0.06 | 0.28 | 314 |
| pressure swell | 15 % → 5 % | 55.6 px | 0.12 | 0.32 | 217 |
| fast wave | 51 % → 8 % | 59.4 px | 0.16 | 0.15 | 886 |
| slow wave | 40 % → 7 % | 45.8 px | 0.13 | 0.18 | 1366 |
| spiral | 68 % → 8 % | 44.6 px | 0.24 | 0.12 | 1676 |
| loop | 34 % → 1 % | 43.6 px | 0.18 | 0.03 | 734 |
| tilted | 18 % → 19 % | 51.6 px | 0.21 | 1.00 | 491 |
| over the wet one | 27 % → 6 % | 24.7 px | 0.21 | 0.22 | 302 |
| long, no reload | 52 % → 7 % | 23.4 px | 0.22 | 0.14 | 2471 | quarters: 0.06 → 0.10 → 0.07 → 0.03

Numbers say: light vs heavy: width 23.4 → 49.4 px, dark 0.00 → 0.06.

## v3 · Any shape · K stamp
Gouache 1.00 · 48 px · 43.3 s

![v3 · Any shape · K stamp](v3-Any-shape-K-stamp.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 20 % → 18 % | 59.0 px | 0.40 | 0.91 | 197 |
| heavy line | 20 % → 19 % | 59.2 px | 0.40 | 0.95 | 359 |
| pressure swell | 12 % → 11 % | 43.7 px | 0.40 | 0.98 | 190 |
| fast wave | 42 % → 34 % | 48.2 px | 0.40 | 0.82 | 689 |
| slow wave | 42 % → 33 % | 48.3 px | 0.40 | 0.80 | 1169 |
| spiral | 66 % → 49 % | 43.6 px | 0.40 | 0.74 | 1458 |
| loop | 37 % → 33 % | 48.2 px | 0.40 | 0.90 | 529 |
| tilted | 15 % → 15 % | 42.0 px | 0.40 | 1.01 | 268 |
| over the wet one | 33 % → 31 % | 51.2 px | 0.40 | 0.94 | 241 |
| long, no reload | 81 % → 51 % | 36.5 px | 0.40 | 0.63 | 1439 | quarters: 0.35 → 0.35 → 0.33 → 0.31

Numbers say: light vs heavy: width 59.0 → 59.2 px, dark 0.40 → 0.40; pressure barely changes the width; the long stroke does not run out of paint.

## v3 · Any shape · K of hairs
Oil 1.00 · 48 px · 17.3 s

![v3 · Any shape · K of hairs](v3-Any-shape-K-of-hairs.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 18 % → 18 % | 51.3 px | 0.40 | 1.00 | 256 |
| heavy line | 27 % → 27 % | 78.5 px | 0.46 | 1.00 | 256 |
| pressure swell | 16 % → 16 % | 58.2 px | 0.47 | 1.01 | 123 |
| fast wave | 49 % → 51 % | 57.1 px | 0.45 | 1.04 | 509 |
| slow wave | 50 % → 50 % | 58.1 px | 0.48 | 1.00 | 1036 |
| spiral | 68 % → 68 % | 44.6 px | 0.45 | 1.00 | 807 |
| loop | 46 % → 46 % | 59.0 px | 0.48 | 1.00 | 412 |
| tilted | 16 % → 16 % | 45.9 px | 0.46 | 1.00 | 200 |
| over the wet one | 39 % → 39 % | 62.7 px | 0.46 | 1.01 | 175 |
| long, no reload | 85 % → 85 % | 38.0 px | 0.43 | 1.00 | 1097 | quarters: 0.48 → 0.45 → 0.34 → 0.27

Numbers say: light vs heavy: width 51.3 → 78.5 px, dark 0.40 → 0.46.

## v3 · Any shape · Star stamp
Gouache 1.00 · 44 px · 34.3 s

![v3 · Any shape · Star stamp](v3-Any-shape-Star-stamp.png)

A light paint: laid on a grey sheet (on white it cannot be seen); **dark** = how far it is from the grey either way.

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 13 % → 10 % | 37.9 px | 0.36 | 0.79 | 128 |
| heavy line | 13 % → 12 % | 38.5 px | 0.36 | 0.88 | 114 |
| pressure swell | 10 % → 10 % | 39.2 px | 0.36 | 0.93 | 87 |
| fast wave | 33 % → 27 % | 38.0 px | 0.36 | 0.83 | 361 |
| slow wave | 33 % → 26 % | 38.4 px | 0.35 | 0.79 | 514 |
| spiral | 56 % → 42 % | 37.3 px | 0.35 | 0.75 | 490 |
| loop | 28 % → 24 % | 36.0 px | 0.36 | 0.88 | 240 |
| tilted | 13 % → 13 % | 36.9 px | 0.36 | 1.01 | 128 |
| over the wet one | 26 % → 23 % | 36.3 px | 0.36 | 0.89 | 114 |
| long, no reload | 68 % → 47 % | 30.5 px | 0.35 | 0.70 | 655 | quarters: 0.01 → 0.01 → 0.01 → 0.01

Numbers say: light vs heavy: width 37.9 → 38.5 px, dark 0.36 → 0.36; pressure barely changes the width; the long stroke does not run out of paint.

## v3 · Any shape · Star of hairs
Oil 1.00 · 44 px · 15.2 s

![v3 · Any shape · Star of hairs](v3-Any-shape-Star-of-hairs.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 15 % → 15 % | 43.7 px | 0.34 | 1.00 | 203 |
| heavy line | 23 % → 23 % | 68.0 px | 0.32 | 1.00 | 171 |
| pressure swell | 14 % → 14 % | 53.2 px | 0.35 | 1.00 | 123 |
| fast wave | 45 % → 46 % | 52.0 px | 0.32 | 1.01 | 423 |
| slow wave | 44 % → 44 % | 51.0 px | 0.33 | 1.00 | 651 |
| spiral | 64 % → 64 % | 41.9 px | 0.32 | 1.00 | 595 |
| loop | 39 % → 39 % | 50.6 px | 0.34 | 1.00 | 373 |
| tilted | 14 % → 14 % | 39.2 px | 0.34 | 1.00 | 190 |
| over the wet one | 34 % → 34 % | 55.5 px | 0.34 | 1.00 | 153 |
| long, no reload | 79 % → 79 % | 35.3 px | 0.30 | 1.00 | 890 | quarters: 0.32 → 0.29 → 0.24 → 0.17

Numbers say: light vs heavy: width 43.7 → 68.0 px, dark 0.34 → 0.32.

## v3 · Any shape · Rag
Oil 1.00 · 60 px · 19.5 s

![v3 · Any shape · Rag](v3-Any-shape-Rag.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 22 % → 24 % | 62.8 px | 0.16 | 1.12 | 201 |
| heavy line | 38 % → 38 % | 111.4 px | 0.29 | 1.00 | 312 |
| pressure swell | 25 % → 26 % | 93.9 px | 0.23 | 1.02 | 204 |
| fast wave | 68 % → 73 % | 79.1 px | 0.26 | 1.07 | 678 |
| slow wave | 71 % → 71 % | 82.1 px | 0.27 | 1.00 | 1186 |
| spiral | 82 % → 82 % | 53.9 px | 0.28 | 1.00 | 1164 |
| loop | 61 % → 61 % | 79.5 px | 0.29 | 1.00 | 596 |
| tilted | 22 % → 22 % | 61.2 px | 0.26 | 1.00 | 268 |
| over the wet one | 51 % → 52 % | 80.3 px | 0.26 | 1.03 | 218 |
| long, no reload | 94 % → 94 % | 42.2 px | 0.29 | 1.00 | 1529 | quarters: 0.35 → 0.32 → 0.27 → 0.21

Numbers say: light vs heavy: width 62.8 → 111.4 px, dark 0.16 → 0.29.

## v3 · Any shape · Dry oil on canvas
Oil 1.00 · 40 px · 12.5 s

![v3 · Any shape · Dry oil on canvas](v3-Any-shape-Dry-oil-on-canvas.png)

A light paint: laid on a grey sheet (on white it cannot be seen); **dark** = how far it is from the grey either way.

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 5 % → 5 % | 13.4 px | 0.14 | 1.00 | 84 |
| heavy line | 8 % → 8 % | 23.6 px | 0.35 | 1.00 | 94 |
| pressure swell | 9 % → 9 % | 32.6 px | 0.27 | 1.00 | 66 |
| fast wave | 27 % → 27 % | 31.8 px | 0.25 | 1.00 | 244 |
| slow wave | 26 % → 26 % | 30.4 px | 0.24 | 1.00 | 455 |
| spiral | 46 % → 46 % | 30.2 px | 0.24 | 1.00 | 446 |
| loop | 21 % → 21 % | 27.4 px | 0.24 | 1.00 | 214 |
| tilted | 9 % → 9 % | 26.5 px | 0.23 | 1.00 | 108 |
| over the wet one | 18 % → 18 % | 23.1 px | 0.23 | 1.00 | 101 |
| long, no reload | 41 % → 41 % | 18.3 px | 0.21 | 1.00 | 573 | quarters: 0.00 → 0.00 → 0.01 → 0.00

Numbers say: light vs heavy: width 13.4 → 23.6 px, dark 0.14 → 0.35; the long stroke does not run out of paint.

## v3 · Any shape · Two colours streaks
Oil 1.00 · 44 px · 14.1 s

![v3 · Any shape · Two colours streaks](v3-Any-shape-Two-colours-streaks.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 14 % → 14 % | 39.7 px | 0.35 | 1.00 | 96 |
| heavy line | 16 % → 16 % | 46.1 px | 0.30 | 1.00 | 121 |
| pressure swell | 11 % → 11 % | 42.7 px | 0.39 | 1.00 | 87 |
| fast wave | 37 % → 37 % | 43.1 px | 0.34 | 1.00 | 332 |
| slow wave | 36 % → 36 % | 41.1 px | 0.30 | 1.00 | 546 |
| spiral | 62 % → 62 % | 40.6 px | 0.35 | 1.00 | 676 |
| loop | 32 % → 32 % | 41.1 px | 0.32 | 1.00 | 291 |
| tilted | 13 % → 13 % | 37.2 px | 0.36 | 1.00 | 176 |
| over the wet one | 27 % → 27 % | 39.1 px | 0.36 | 1.00 | 135 |
| long, no reload | 73 % → 73 % | 32.8 px | 0.32 | 1.00 | 808 | quarters: 0.29 → 0.28 → 0.25 → 0.20

Numbers say: light vs heavy: width 39.7 → 46.1 px, dark 0.35 → 0.30.

## Watercolour · Wash
Watercolour 1.00 + water 65 % · 60 px · 37.3 s

![Watercolour · Wash](Watercolour-Wash.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 15 % → 18 % | 43.3 px | 0.14 | 1.23 | 111 |
| heavy line | 30 % → 30 % | 86.5 px | 0.13 | 1.01 | 204 |
| pressure swell | 18 % → 19 % | 68.1 px | 0.16 | 1.06 | 135 |
| fast wave | 57 % → 59 % | 65.8 px | 0.13 | 1.04 | 506 |
| slow wave | 53 % → 55 % | 61.7 px | 0.14 | 1.02 | 741 |
| spiral | 70 % → 71 % | 46.4 px | 0.11 | 1.01 | 759 |
| loop | 46 % → 48 % | 60.0 px | 0.13 | 1.03 | 373 |
| tilted | 21 % → 21 % | 57.6 px | 0.15 | 1.01 | 252 |
| over the wet one | 42 % → 45 % | 60.4 px | 0.15 | 1.06 | 189 |
| long, no reload | 89 % → 91 % | 39.7 px | 0.09 | 1.03 | 1150 | quarters: 0.14 → 0.11 → 0.07 → 0.04

Numbers say: light vs heavy: width 43.3 → 86.5 px, dark 0.14 → 0.13.

## Watercolour · Wet-in-wet
Watercolour 1.00 + water 80 % · 60 px · 45.0 s

![Watercolour · Wet-in-wet](Watercolour-Wet-in-wet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 13 % → 30 % | 37.6 px | 0.17 | 2.31 | 90 |
| heavy line | 25 % → 38 % | 73.7 px | 0.19 | 1.52 | 176 |
| pressure swell | 16 % → 28 % | 58.1 px | 0.22 | 1.78 | 221 |
| fast wave | 49 % → 73 % | 56.2 px | 0.20 | 1.49 | 444 |
| slow wave | 47 % → 69 % | 54.7 px | 0.22 | 1.46 | 697 |
| spiral | 67 % → 80 % | 44.3 px | 0.18 | 1.19 | 711 |
| loop | 43 % → 60 % | 55.3 px | 0.23 | 1.40 | 348 |
| tilted | 20 % → 21 % | 55.9 px | 0.18 | 1.03 | 208 |
| over the wet one | 40 % → 64 % | 56.1 px | 0.18 | 1.58 | 181 |
| long, no reload | 85 % → 97 % | 37.9 px | 0.18 | 1.15 | 1523 | quarters: 0.31 → 0.22 → 0.15 → 0.09

Numbers say: light vs heavy: width 37.6 → 73.7 px, dark 0.17 → 0.19; wet paint spreads well beyond the stroke.

## Watercolour · Glaze
Watercolour 1.00 + water 75 % · 50 px · 36.1 s

![Watercolour · Glaze](Watercolour-Glaze.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 13 % → 16 % | 38.2 px | 0.03 | 1.25 | 79 |
| heavy line | 26 % → 27 % | 74.7 px | 0.03 | 1.04 | 164 |
| pressure swell | 16 % → 18 % | 60.2 px | 0.03 | 1.09 | 117 |
| fast wave | 50 % → 54 % | 58.2 px | 0.03 | 1.08 | 379 |
| slow wave | 47 % → 50 % | 53.9 px | 0.03 | 1.07 | 588 |
| spiral | 63 % → 67 % | 41.9 px | 0.02 | 1.05 | 633 |
| loop | 42 % → 44 % | 54.2 px | 0.03 | 1.05 | 306 |
| tilted | 17 % → 17 % | 47.1 px | 0.03 | 1.03 | 198 |
| over the wet one | 37 % → 40 % | 57.4 px | 0.03 | 1.08 | 157 |
| long, no reload | 80 % → 87 % | 35.7 px | 0.02 | 1.09 | 1015 | quarters: 0.04 → 0.02 → 0.01 → 0.01

Numbers say: light vs heavy: width 38.2 → 74.7 px, dark 0.03 → 0.03.

## Watercolour · Granulating
Watercolour 1.00 + water 60 % · 56 px · 38.4 s

![Watercolour · Granulating](Watercolour-Granulating.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 14 % → 17 % | 40.6 px | 0.20 | 1.23 | 99 |
| heavy line | 28 % → 28 % | 80.2 px | 0.18 | 1.01 | 186 |
| pressure swell | 17 % → 18 % | 63.0 px | 0.23 | 1.05 | 143 |
| fast wave | 53 % → 55 % | 61.2 px | 0.18 | 1.04 | 422 |
| slow wave | 51 % → 52 % | 59.0 px | 0.19 | 1.03 | 666 |
| spiral | 68 % → 69 % | 44.8 px | 0.15 | 1.01 | 755 |
| loop | 45 % → 46 % | 58.1 px | 0.20 | 1.03 | 361 |
| tilted | 20 % → 20 % | 54.6 px | 0.21 | 1.01 | 233 |
| over the wet one | 40 % → 42 % | 57.6 px | 0.21 | 1.05 | 684 |
| long, no reload | 88 % → 90 % | 39.4 px | 0.15 | 1.02 | 1132 | quarters: 0.22 → 0.17 → 0.11 → 0.06

Numbers say: light vs heavy: width 40.6 → 80.2 px, dark 0.20 → 0.18.

## Watercolour · Dry brush
Watercolour 1.00 + water 35 % · 44 px · 32.0 s

![Watercolour · Dry brush](Watercolour-Dry-brush.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 5 % → 2 % | 15.8 px | 0.01 | 0.29 | 68 |
| heavy line | 20 % → 20 % | 56.8 px | 0.09 | 1.00 | 145 |
| pressure swell | 14 % → 14 % | 51.9 px | 0.08 | 1.02 | 92 |
| fast wave | 47 % → 47 % | 54.1 px | 0.03 | 0.99 | 356 |
| slow wave | 35 % → 35 % | 40.0 px | 0.04 | 1.00 | 495 |
| spiral | 61 % → 62 % | 40.4 px | 0.02 | 1.01 | 536 |
| loop | 32 % → 30 % | 41.6 px | 0.02 | 0.92 | 255 |
| tilted | 11 % → 12 % | 31.3 px | 0.04 | 1.05 | 146 |
| over the wet one | 25 % → 26 % | 38.4 px | 0.04 | 1.04 | 116 |
| long, no reload | 69 % → 64 % | 31.1 px | 0.02 | 0.93 | 654 | quarters: 0.01 → 0.01 → 0.01 → 0.02

Numbers say: light vs heavy: width 15.8 → 56.8 px, dark 0.01 → 0.09; the long stroke does not run out of paint.

## Watercolour · Runs
Watercolour 1.00 + water 80 % · 60 px · 45.9 s

![Watercolour · Runs](Watercolour-Runs.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 26 % → 35 % | 74.7 px | 0.34 | 1.37 | 121 |
| heavy line | 39 % → 42 % | 114.3 px | 0.38 | 1.06 | 216 |
| pressure swell | 17 % → 28 % | 64.3 px | 0.41 | 1.61 | 143 |
| fast wave | 64 % → 74 % | 73.9 px | 0.40 | 1.16 | 549 |
| slow wave | 57 % → 68 % | 65.4 px | 0.42 | 1.21 | 844 |
| spiral | 74 % → 82 % | 48.6 px | 0.42 | 1.12 | 981 |
| loop | 60 % → 69 % | 78.3 px | 0.41 | 1.14 | 426 |
| tilted | 30 % → 30 % | 82.4 px | 0.37 | 1.02 | 250 |
| over the wet one | 55 % → 67 % | 70.2 px | 0.37 | 1.23 | 226 |
| long, no reload | 90 % → 99 % | 40.5 px | 0.43 | 1.09 | 1269 | quarters: 0.57 → 0.50 → 0.41 → 0.27

Numbers say: light vs heavy: width 74.7 → 114.3 px, dark 0.34 → 0.38; wet paint spreads well beyond the stroke.

## Watercolour · Two-tone
Watercolour 1.00 + water 60 % · 56 px · 39.9 s

![Watercolour · Two-tone](Watercolour-Two-tone.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 15 % → 18 % | 43.8 px | 0.55 | 1.19 | 90 |
| heavy line | 30 % → 30 % | 85.9 px | 0.57 | 1.01 | 216 |
| pressure swell | 18 % → 18 % | 66.0 px | 0.57 | 1.05 | 138 |
| fast wave | 56 % → 58 % | 64.6 px | 0.52 | 1.04 | 558 |
| slow wave | 52 % → 54 % | 60.6 px | 0.56 | 1.02 | 762 |
| spiral | 69 % → 70 % | 45.7 px | 0.31 | 1.01 | 847 |
| loop | 47 % → 48 % | 61.1 px | 0.53 | 1.02 | 359 |
| tilted | 19 % → 19 % | 53.0 px | 0.53 | 1.01 | 204 |
| over the wet one | 41 % → 43 % | 61.9 px | 0.53 | 1.05 | 183 |
| long, no reload | 87 % → 90 % | 39.1 px | 0.18 | 1.03 | 1278 | quarters: 0.25 → 0.22 → 0.15 → 0.09

Numbers say: light vs heavy: width 43.8 → 85.9 px, dark 0.55 → 0.57.

## Watercolour · SH blue
Watercolour 1.00 + water 50 % · 40 px · 27.4 s

![Watercolour · SH blue](Watercolour-SH-blue.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 6 % → 11 % | 16.6 px | 0.17 | 1.90 | 41 |
| heavy line | 12 % → 16 % | 33.6 px | 0.19 | 1.38 | 92 |
| pressure swell | 7 % → 10 % | 26.7 px | 0.20 | 1.47 | 61 |
| fast wave | 25 % → 31 % | 28.6 px | 0.20 | 1.24 | 296 |
| slow wave | 24 % → 30 % | 27.6 px | 0.17 | 1.27 | 311 |
| spiral | 38 % → 45 % | 24.9 px | 0.15 | 1.19 | 298 |
| loop | 20 % → 27 % | 26.1 px | 0.18 | 1.32 | 171 |
| tilted | 14 % → 14 % | 38.7 px | 0.17 | 1.01 | 114 |
| over the wet one | 23 % → 27 % | 24.8 px | 0.17 | 1.18 | 81 |
| long, no reload | 51 % → 56 % | 22.7 px | 0.12 | 1.11 | 523 | quarters: 0.12 → 0.08 → 0.06 → 0.04

Numbers say: light vs heavy: width 16.6 → 33.6 px, dark 0.17 → 0.19; wet paint spreads well beyond the stroke.

## Watercolour · SH violet
Watercolour 1.00 + water 50 % · 40 px · 27.8 s

![Watercolour · SH violet](Watercolour-SH-violet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 6 % → 11 % | 16.6 px | 0.28 | 1.90 | 46 |
| heavy line | 12 % → 16 % | 33.6 px | 0.30 | 1.38 | 93 |
| pressure swell | 7 % → 10 % | 26.7 px | 0.33 | 1.47 | 94 |
| fast wave | 25 % → 31 % | 28.6 px | 0.32 | 1.24 | 199 |
| slow wave | 24 % → 30 % | 27.6 px | 0.28 | 1.27 | 296 |
| spiral | 38 % → 45 % | 24.9 px | 0.24 | 1.19 | 298 |
| loop | 20 % → 27 % | 26.1 px | 0.29 | 1.32 | 160 |
| tilted | 14 % → 14 % | 38.7 px | 0.28 | 1.01 | 102 |
| over the wet one | 23 % → 27 % | 24.8 px | 0.28 | 1.18 | 87 |
| long, no reload | 51 % → 56 % | 22.7 px | 0.20 | 1.11 | 488 | quarters: 0.19 → 0.13 → 0.09 → 0.06

Numbers say: light vs heavy: width 16.6 → 33.6 px, dark 0.28 → 0.30; wet paint spreads well beyond the stroke.

## Watercolour · SH teal
Watercolour 1.00 + water 50 % · 40 px · 27.8 s

![Watercolour · SH teal](Watercolour-SH-teal.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 6 % → 11 % | 16.6 px | 0.12 | 1.90 | 47 |
| heavy line | 12 % → 16 % | 33.6 px | 0.13 | 1.38 | 92 |
| pressure swell | 7 % → 10 % | 26.7 px | 0.14 | 1.47 | 47 |
| fast wave | 25 % → 31 % | 28.6 px | 0.14 | 1.24 | 225 |
| slow wave | 24 % → 30 % | 27.6 px | 0.12 | 1.27 | 291 |
| spiral | 38 % → 45 % | 24.9 px | 0.11 | 1.19 | 337 |
| loop | 20 % → 27 % | 26.1 px | 0.12 | 1.32 | 153 |
| tilted | 14 % → 14 % | 38.7 px | 0.12 | 1.01 | 142 |
| over the wet one | 23 % → 27 % | 24.8 px | 0.12 | 1.18 | 113 |
| long, no reload | 51 % → 56 % | 22.7 px | 0.10 | 1.11 | 488 | quarters: 0.08 → 0.06 → 0.05 → 0.03

Numbers say: light vs heavy: width 16.6 → 33.6 px, dark 0.12 → 0.13; wet paint spreads well beyond the stroke.

## Watercolour · #16 Shrigley strokes
Watercolour 1.00 + water 50 % · 40 px · 26.9 s

![Watercolour · #16 Shrigley strokes](Watercolour-16-Shrigley-strokes.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 6 % → 11 % | 16.6 px | 0.17 | 1.90 | 43 |
| heavy line | 12 % → 16 % | 33.6 px | 0.19 | 1.38 | 106 |
| pressure swell | 7 % → 10 % | 26.7 px | 0.20 | 1.47 | 84 |
| fast wave | 25 % → 31 % | 28.6 px | 0.20 | 1.24 | 249 |
| slow wave | 24 % → 30 % | 27.6 px | 0.17 | 1.27 | 387 |
| spiral | 38 % → 45 % | 24.9 px | 0.15 | 1.19 | 311 |
| loop | 20 % → 27 % | 26.1 px | 0.18 | 1.32 | 220 |
| tilted | 14 % → 14 % | 38.7 px | 0.17 | 1.01 | 106 |
| over the wet one | 23 % → 27 % | 24.8 px | 0.17 | 1.18 | 102 |
| long, no reload | 51 % → 56 % | 22.7 px | 0.12 | 1.11 | 511 | quarters: 0.12 → 0.08 → 0.06 → 0.04

Numbers say: light vs heavy: width 16.6 → 33.6 px, dark 0.17 → 0.19; wet paint spreads well beyond the stroke.

## Watercolour · #29 Shrigley asterisk
Watercolour 1.00 + water 50 % · 70 px · 42.2 s

![Watercolour · #29 Shrigley asterisk](Watercolour-29-Shrigley-asterisk.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 20 % → 23 % | 57.6 px | 0.60 | 1.15 | 222 |
| heavy line | 39 % → 39 % | 112.5 px | 0.62 | 1.00 | 394 |
| pressure swell | 24 % → 25 % | 88.7 px | 0.61 | 1.06 | 339 |
| fast wave | 68 % → 72 % | 78.7 px | 0.61 | 1.06 | 715 |
| slow wave | 64 % → 65 % | 74.5 px | 0.62 | 1.01 | 1051 |
| spiral | 77 % → 77 % | 50.8 px | 0.57 | 1.00 | 962 |
| loop | 57 % → 58 % | 74.3 px | 0.60 | 1.01 | 493 |
| tilted | 24 % → 24 % | 67.8 px | 0.60 | 1.00 | 311 |
| over the wet one | 53 % → 55 % | 78.8 px | 0.60 | 1.05 | 254 |
| long, no reload | 93 % → 94 % | 41.7 px | 0.55 | 1.01 | 1586 | quarters: 0.57 → 0.56 → 0.54 → 0.46

Numbers say: light vs heavy: width 57.6 → 112.5 px, dark 0.60 → 0.62.

## Watercolour · Pink flame
Watercolour 1.00 + water 85 % · 50 px · 40.1 s

![Watercolour · Pink flame](Watercolour-Pink-flame.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 11 % → 28 % | 31.5 px | 0.02 | 2.58 | 80 |
| heavy line | 22 % → 35 % | 63.0 px | 0.03 | 1.62 | 160 |
| pressure swell | 13 % → 25 % | 49.2 px | 0.03 | 1.91 | 102 |
| fast wave | 43 % → 68 % | 49.2 px | 0.03 | 1.61 | 380 |
| slow wave | 41 % → 64 % | 47.1 px | 0.03 | 1.58 | 531 |
| spiral | 62 % → 77 % | 41.2 px | 0.03 | 1.24 | 590 |
| loop | 36 % → 56 % | 46.7 px | 0.04 | 1.56 | 265 |
| tilted | 17 % → 18 % | 48.5 px | 0.03 | 1.04 | 161 |
| over the wet one | 35 % → 58 % | 49.1 px | 0.03 | 1.66 | 141 |
| long, no reload | 76 % → 95 % | 34.2 px | 0.03 | 1.24 | 845 | quarters: 0.05 → 0.03 → 0.02 → 0.01

Numbers say: light vs heavy: width 31.5 → 63.0 px, dark 0.02 → 0.03; wet paint spreads well beyond the stroke.

## Watercolour · #33 Red band, pink flames
Watercolour 1.00 + water 60 % · 90 px · 50.6 s

![Watercolour · #33 Red band, pink flames](Watercolour-33-Red-band-pink-flames.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 28 % → 48 % | 82.7 px | 0.43 | 1.70 | 200 |
| heavy line | 45 % → 57 % | 129.7 px | 0.49 | 1.27 | 379 |
| pressure swell | 27 % → 46 % | 100.3 px | 0.46 | 1.71 | 258 |
| fast wave | 71 % → 86 % | 82.6 px | 0.57 | 1.20 | 770 |
| slow wave | 72 % → 83 % | 83.7 px | 0.56 | 1.14 | 1129 |
| spiral | 85 % → 95 % | 56.1 px | 0.55 | 1.12 | 1246 |
| loop | 62 % → 79 % | 80.7 px | 0.54 | 1.27 | 613 |
| tilted | 37 % → 39 % | 104.3 px | 0.51 | 1.04 | 400 |
| over the wet one | 66 % → 87 % | 80.3 px | 0.51 | 1.32 | 300 |
| long, no reload | 96 % → 100 % | 42.9 px | 0.59 | 1.04 | 1835 | quarters: 0.66 → 0.64 → 0.61 → 0.49

Numbers say: light vs heavy: width 82.7 → 129.7 px, dark 0.43 → 0.49; wet paint spreads well beyond the stroke.

## Watercolour · #35 Red band with runs
Watercolour 1.00 + water 70 % · 80 px · 52.9 s

![Watercolour · #35 Red band with runs](Watercolour-35-Red-band-with-runs.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 41 % → 51 % | 118.6 px | 0.26 | 1.24 | 165 |
| heavy line | 54 % → 57 % | 157.5 px | 0.35 | 1.05 | 340 |
| pressure swell | 22 % → 36 % | 84.2 px | 0.31 | 1.61 | 225 |
| fast wave | 72 % → 82 % | 83.5 px | 0.40 | 1.13 | 730 |
| slow wave | 73 % → 79 % | 83.8 px | 0.43 | 1.09 | 1179 |
| spiral | 91 % → 96 % | 59.8 px | 0.18 | 1.06 | 1219 |
| loop | 78 % → 87 % | 101.0 px | 0.39 | 1.12 | 508 |
| tilted | 51 % → 52 % | 143.4 px | 0.34 | 1.01 | 323 |
| over the wet one | 77 % → 89 % | 71.8 px | 0.34 | 1.16 | 280 |
| long, no reload | 96 % → 100 % | 42.8 px | 0.27 | 1.05 | 1810 | quarters: 0.37 → 0.32 → 0.25 → 0.14

Numbers say: light vs heavy: width 118.6 → 157.5 px, dark 0.26 → 0.35; wet paint spreads well beyond the stroke.

## Watercolour · Sepia wash
Watercolour 1.00 + water 85 % · 70 px · 44.7 s

![Watercolour · Sepia wash](Watercolour-Sepia-wash.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 15 % → 33 % | 43.2 px | 0.02 | 2.19 | 122 |
| heavy line | 28 % → 41 % | 81.3 px | 0.03 | 1.47 | 225 |
| pressure swell | 18 % → 30 % | 65.7 px | 0.03 | 1.72 | 142 |
| fast wave | 54 % → 77 % | 62.6 px | 0.03 | 1.42 | 555 |
| slow wave | 53 % → 73 % | 60.8 px | 0.03 | 1.38 | 784 |
| spiral | 70 % → 83 % | 46.3 px | 0.03 | 1.18 | 834 |
| loop | 47 % → 62 % | 61.1 px | 0.03 | 1.32 | 414 |
| tilted | 22 % → 23 % | 61.9 px | 0.03 | 1.03 | 290 |
| over the wet one | 44 % → 68 % | 61.9 px | 0.03 | 1.54 | 210 |
| long, no reload | 88 % → 98 % | 39.6 px | 0.03 | 1.11 | 1300 | quarters: 0.06 → 0.04 → 0.02 → 0.01

Numbers say: light vs heavy: width 43.2 → 81.3 px, dark 0.02 → 0.03; wet paint spreads well beyond the stroke.

## Watercolour · #40 Olive and sepia blooms
Watercolour 1.00 + water 75 % · 80 px · 45.6 s

![Watercolour · #40 Olive and sepia blooms](Watercolour-40-Olive-and-sepia-blooms.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 17 % → 35 % | 50.2 px | 0.04 | 2.03 | 123 |
| heavy line | 32 % → 44 % | 92.7 px | 0.05 | 1.37 | 256 |
| pressure swell | 20 % → 32 % | 75.0 px | 0.05 | 1.61 | 172 |
| fast wave | 60 % → 81 % | 68.9 px | 0.06 | 1.36 | 641 |
| slow wave | 58 % → 76 % | 67.2 px | 0.06 | 1.30 | 896 |
| spiral | 75 % → 85 % | 49.6 px | 0.06 | 1.14 | 992 |
| loop | 53 % → 65 % | 68.0 px | 0.06 | 1.24 | 503 |
| tilted | 25 % → 26 % | 70.0 px | 0.05 | 1.02 | 316 |
| over the wet one | 50 % → 73 % | 69.0 px | 0.05 | 1.46 | 261 |
| long, no reload | 92 % → 99 % | 41.1 px | 0.06 | 1.08 | 1551 | quarters: 0.10 → 0.07 → 0.05 → 0.03

Numbers say: light vs heavy: width 50.2 → 92.7 px, dark 0.04 → 0.05; wet paint spreads well beyond the stroke.

## Watercolour · #46 Lips on wet paper
Watercolour 1.00 + water 65 % · 50 px · 38.9 s

![Watercolour · #46 Lips on wet paper](Watercolour-46-Lips-on-wet-paper.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 11 % → 28 % | 32.3 px | 0.61 | 2.48 | 71 |
| heavy line | 22 % → 35 % | 64.7 px | 0.64 | 1.56 | 151 |
| pressure swell | 13 % → 25 % | 49.9 px | 0.63 | 1.86 | 94 |
| fast wave | 44 % → 68 % | 50.6 px | 0.65 | 1.56 | 359 |
| slow wave | 41 % → 64 % | 47.8 px | 0.65 | 1.54 | 519 |
| spiral | 64 % → 77 % | 42.2 px | 0.67 | 1.20 | 569 |
| loop | 37 % → 56 % | 47.7 px | 0.66 | 1.51 | 269 |
| tilted | 18 % → 19 % | 50.4 px | 0.62 | 1.05 | 154 |
| over the wet one | 36 % → 58 % | 50.8 px | 0.62 | 1.59 | 139 |
| long, no reload | 79 % → 96 % | 35.5 px | 0.66 | 1.21 | 791 | quarters: 0.72 → 0.71 → 0.67 → 0.57

Numbers say: light vs heavy: width 32.3 → 64.7 px, dark 0.61 → 0.64; wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #01 Henry Ward peach cloud — own sheet
own sheet 600 × 600 · Gouache 1.00 · 44 px · 10.0 s

![Brush Artist · Refs · #01 Henry Ward peach cloud — own sheet](Brush-Artist-Refs-01-Henry-Ward-peach-cloud-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 5 % → 16 % | 15.6 px | 0.53 | 2.97 | 105 |
| stroke 2 | 11 % → 29 % | 35.1 px | 0.54 | 2.71 | 123 |
| stroke 3 | 16 % → 31 % | 45.4 px | 0.54 | 2.00 | 130 |
| stroke 4 | 21 % → 34 % | 68.0 px | 0.54 | 1.63 | 138 |
| stroke 5 | 21 % → 31 % | 60.5 px | 0.54 | 1.48 | 153 |
| stroke 6 | 20 % → 24 % | 61.5 px | 0.54 | 1.21 | 136 |
| stroke 7 | 9 % → 33 % | 22.9 px | 0.53 | 3.58 | 126 |
| stroke 8 | 14 % → 32 % | 34.7 px | 0.53 | 2.28 | 141 |
| stroke 9 | 13 % → 33 % | 33.9 px | 0.53 | 2.47 | 123 |
| stroke 10 | 13 % → 34 % | 35.3 px | 0.53 | 2.57 | 135 |
| stroke 11 | 14 % → 36 % | 40.5 px | 0.54 | 2.53 | 134 |
| stroke 12 | 14 % → 39 % | 42.4 px | 0.54 | 2.76 | 108 |
| stroke 13 | 19 % → 42 % | 54.8 px | 0.54 | 2.23 | 116 |
| stroke 14 | 27 % → 44 % | 77.4 px | 0.54 | 1.63 | 160 |
| stroke 15 | 30 % → 48 % | 88.5 px | 0.53 | 1.60 | 123 |
| stroke 16 | 35 % → 48 % | 104.8 px | 0.53 | 1.39 | 149 |
| stroke 17 | 35 % → 50 % | 98.5 px | 0.53 | 1.41 | 146 |
| stroke 18 | 41 % → 49 % | 117.6 px | 0.53 | 1.21 | 138 |
| stroke 19 | 41 % → 49 % | 116.0 px | 0.54 | 1.18 | 137 |
| stroke 20 | 43 % → 46 % | 123.0 px | 0.54 | 1.07 | 155 |
| stroke 21 | 43 % → 42 % | 125.4 px | 0.54 | 0.96 | 164 |
| stroke 22 | 45 % → 42 % | 131.2 px | 0.54 | 0.94 | 149 |
| stroke 23 | 49 % → 43 % | 139.0 px | 0.54 | 0.88 | 139 |
| stroke 24 | 52 % → 45 % | 156.2 px | 0.54 | 0.86 | 112 |

Numbers say: wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #02 Henry Ward cream strokes — own sheet
own sheet 600 × 600 · Gouache 1.00 · 46 px · 6.7 s

![Brush Artist · Refs · #02 Henry Ward cream strokes — own sheet](Brush-Artist-Refs-02-Henry-Ward-cream-strokes-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 9 % → 2 % | 17.7 px | 0.65 | 0.26 | 158 |
| stroke 2 | 15 % → 6 % | 39.4 px | 0.66 | 0.41 | 175 |
| stroke 3 | 19 % → 22 % | 48.9 px | 0.64 | 1.15 | 192 |
| stroke 4 | 23 % → 22 % | 56.7 px | 0.64 | 0.97 | 231 |
| stroke 5 | 24 % → 27 % | 59.0 px | 0.64 | 1.11 | 194 |
| stroke 6 | 18 % → 16 % | 43.4 px | 0.64 | 0.88 | 190 |
| stroke 7 | 21 % → 10 % | 53.1 px | 0.64 | 0.48 | 180 |

## Brush Artist · Refs · #03 Henry Ward navy contours — own sheet
own sheet 600 × 600 · Impasto 1.00 · 22 px · 2.4 s

![Brush Artist · Refs · #03 Henry Ward navy contours — own sheet](Brush-Artist-Refs-03-Henry-Ward-navy-contours-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 10 % → 15 % | 20.0 px | 0.70 | 1.51 | 114 |
| stroke 2 | 16 % → 19 % | 22.1 px | 0.70 | 1.19 | 93 |
| stroke 3 | 20 % → 20 % | 29.5 px | 0.71 | 0.99 | 127 |
| stroke 4 | 19 % → 17 % | 43.6 px | 0.71 | 0.89 | 159 |

Numbers say: wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #04 Henry Ward grey cloud — own sheet
own sheet 600 × 600 · Gouache 1.00 · 50 px · 9.8 s

![Brush Artist · Refs · #04 Henry Ward grey cloud — own sheet](Brush-Artist-Refs-04-Henry-Ward-grey-cloud-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 5 % → 21 % | 15.7 px | 0.32 | 3.88 | 146 |
| stroke 2 | 14 % → 21 % | 40.2 px | 0.31 | 1.53 | 185 |
| stroke 3 | 21 % → 22 % | 59.7 px | 0.31 | 1.05 | 192 |
| stroke 4 | 27 % → 23 % | 79.5 px | 0.31 | 0.84 | 208 |
| stroke 5 | 27 % → 26 % | 83.3 px | 0.31 | 0.94 | 296 |
| stroke 6 | 33 % → 30 % | 109.0 px | 0.31 | 0.89 | 211 |
| stroke 7 | 34 % → 36 % | 100.8 px | 0.30 | 1.03 | 200 |
| stroke 8 | 38 % → 38 % | 112.6 px | 0.30 | 0.99 | 200 |
| stroke 9 | 32 % → 39 % | 94.9 px | 0.31 | 1.23 | 161 |
| stroke 10 | 33 % → 39 % | 106.9 px | 0.31 | 1.19 | 158 |
| stroke 11 | 34 % → 36 % | 96.9 px | 0.31 | 1.05 | 196 |
| stroke 12 | 32 % → 34 % | 96.3 px | 0.30 | 1.06 | 163 |
| stroke 13 | 27 % → 38 % | 78.1 px | 0.31 | 1.38 | 170 |
| stroke 14 | 34 % → 38 % | 100.7 px | 0.31 | 1.11 | 226 |
| stroke 15 | 35 % → 37 % | 100.1 px | 0.31 | 1.07 | 185 |
| stroke 16 | 38 % → 36 % | 116.5 px | 0.31 | 0.93 | 216 |
| stroke 17 | 39 % → 31 % | 112.7 px | 0.31 | 0.79 | 177 |
| stroke 18 | 40 % → 28 % | 133.2 px | 0.31 | 0.70 | 187 |
| stroke 19 | 38 % → 24 % | 113.0 px | 0.32 | 0.63 | 180 |
| stroke 20 | 40 % → 23 % | 125.2 px | 0.32 | 0.57 | 214 |

Numbers say: wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #05 Henry Ward green in rust loops — own sheet
own sheet 600 × 600 · Impasto 1.00 · 20 px · 2.2 s

![Brush Artist · Refs · #05 Henry Ward green in rust loops — own sheet](Brush-Artist-Refs-05-Henry-Ward-green-in-rust-loops-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 11 % → 16 % | 19.1 px | 0.02 | 1.49 | 125 |
| stroke 2 | 12 % → 10 % | 24.0 px | 0.02 | 0.86 | 145 |
| stroke 3 | 20 % → 17 % | 35.4 px | 0.02 | 0.89 | 113 |

## Brush Artist · Refs · #06 Henry Ward scrubbed grey — own sheet
own sheet 600 × 600 · Gouache 1.00 · 50 px · 10.9 s

![Brush Artist · Refs · #06 Henry Ward scrubbed grey — own sheet](Brush-Artist-Refs-06-Henry-Ward-scrubbed-grey-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 6 % → 24 % | 15.9 px | 0.32 | 3.69 | 166 |
| stroke 2 | 16 % → 25 % | 41.5 px | 0.31 | 1.58 | 214 |
| stroke 3 | 21 % → 23 % | 64.7 px | 0.31 | 1.10 | 216 |
| stroke 4 | 25 % → 24 % | 78.0 px | 0.31 | 0.96 | 216 |
| stroke 5 | 31 % → 30 % | 92.8 px | 0.31 | 0.97 | 181 |
| stroke 6 | 38 % → 31 % | 115.7 px | 0.31 | 0.81 | 214 |
| stroke 7 | 36 % → 35 % | 103.6 px | 0.31 | 0.98 | 205 |
| stroke 8 | 40 % → 36 % | 125.1 px | 0.31 | 0.90 | 183 |
| stroke 9 | 35 % → 37 % | 107.6 px | 0.31 | 1.06 | 168 |
| stroke 10 | 34 % → 38 % | 111.3 px | 0.31 | 1.10 | 165 |
| stroke 11 | 35 % → 37 % | 101.5 px | 0.31 | 1.06 | 195 |
| stroke 12 | 33 % → 35 % | 99.4 px | 0.31 | 1.08 | 140 |
| stroke 13 | 24 % → 37 % | 69.3 px | 0.31 | 1.53 | 179 |
| stroke 14 | 30 % → 39 % | 88.5 px | 0.31 | 1.30 | 220 |
| stroke 15 | 33 % → 44 % | 95.1 px | 0.32 | 1.34 | 184 |
| stroke 16 | 35 % → 45 % | 111.8 px | 0.32 | 1.28 | 227 |
| stroke 17 | 37 % → 42 % | 110.5 px | 0.32 | 1.12 | 195 |
| stroke 18 | 41 % → 40 % | 123.6 px | 0.32 | 0.98 | 211 |
| stroke 19 | 38 % → 35 % | 112.0 px | 0.32 | 0.93 | 197 |
| stroke 20 | 38 % → 34 % | 117.9 px | 0.32 | 0.90 | 217 |
| stroke 21 | 40 % → 30 % | 116.2 px | 0.33 | 0.75 | 207 |
| stroke 22 | 39 % → 28 % | 127.1 px | 0.33 | 0.73 | 193 |

Numbers say: wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #07 Henry Ward blue L + black zigzag — own sheet
own sheet 600 × 600 · Impasto 1.00 · 34 px · 1.9 s

![Brush Artist · Refs · #07 Henry Ward blue L + black zigzag — own sheet](Brush-Artist-Refs-07-Henry-Ward-blue-L-black-zigzag-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 13 % → 15 % | 31.2 px | 0.58 | 1.09 | 122 |
| stroke 2 | 15 % → 14 % | 37.7 px | 0.58 | 0.90 | 81 |

## Brush Artist · Refs · #08 Henry Ward olive bands — own sheet
own sheet 600 × 600 · Gouache 1.00 · 34 px · 4.9 s

![Brush Artist · Refs · #08 Henry Ward olive bands — own sheet](Brush-Artist-Refs-08-Henry-Ward-olive-bands-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 8 % → 4 % | 15.7 px | 0.58 | 0.53 | 133 |
| stroke 2 | 12 % → 4 % | 28.0 px | 0.58 | 0.35 | 152 |
| stroke 3 | 13 % → 11 % | 27.5 px | 0.58 | 0.87 | 155 |
| stroke 4 | 17 % → 10 % | 37.3 px | 0.58 | 0.57 | 197 |
| stroke 5 | 22 % → 13 % | 45.2 px | 0.56 | 0.59 | 177 |
| stroke 6 | 16 % → 6 % | 30.5 px | 0.54 | 0.40 | 171 |

## Brush Artist · Refs · #09 Henry Ward white loops — own sheet
own sheet 600 × 600 · Gouache 1.00 · 46 px · 6.1 s

![Brush Artist · Refs · #09 Henry Ward white loops — own sheet](Brush-Artist-Refs-09-Henry-Ward-white-loops-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 23 % → 0 % | 12.1 px | 0.06 | 0.00 | 837 |
| stroke 2 | 27 % → 0 % | 27.4 px | 0.07 | 0.00 | 986 |
| stroke 3 | 34 % → 0 % | 31.4 px | 0.07 | 0.00 | 881 |
| stroke 4 | 8 % → 0 % | 18.4 px | 0.00 | 0.00 | 183 |
| stroke 5 | 5 % → 0 % | 14.8 px | 0.06 | 0.00 | 174 |
| stroke 6 | 5 % → 0 % | 13.8 px | 0.08 | 0.00 | 163 |
| stroke 7 | 10 % → 0 % | 26.8 px | 0.08 | 0.00 | 146 |
| stroke 8 | 5 % → 0 % | 8.2 px | 0.00 | 0.00 | 164 |

## Brush Artist · Refs · #10 Henry Ward maroon loops — own sheet
own sheet 600 × 600 · Impasto 1.00 · 30 px · 3.0 s

![Brush Artist · Refs · #10 Henry Ward maroon loops — own sheet](Brush-Artist-Refs-10-Henry-Ward-maroon-loops-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 12 % → 26 % | 28.9 px | 0.72 | 2.25 | 220 |
| stroke 2 | 23 % → 39 % | 51.0 px | 0.72 | 1.74 | 117 |
| stroke 3 | 30 % → 36 % | 59.6 px | 0.72 | 1.20 | 179 |
| stroke 4 | 40 % → 38 % | 91.4 px | 0.72 | 0.94 | 112 |
| stroke 5 | 33 % → 29 % | 82.1 px | 0.71 | 0.89 | 149 |

Numbers say: wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #11 Henry Ward purple spun balls — own sheet
own sheet 600 × 600 · Impasto 1.00 · 36 px · 2.5 s

![Brush Artist · Refs · #11 Henry Ward purple spun balls — own sheet](Brush-Artist-Refs-11-Henry-Ward-purple-spun-balls-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 22 % → 31 % | 24.4 px | 0.69 | 1.42 | 203 |
| stroke 2 | 31 % → 44 % | 34.3 px | 0.69 | 1.39 | 209 |
| stroke 3 | 34 % → 33 % | 37.7 px | 0.69 | 0.97 | 252 |

## Brush Artist · Refs · #12 Henry Ward black-olive cage — own sheet
own sheet 600 × 600 · Gouache 1.00 · 28 px · 4.8 s

![Brush Artist · Refs · #12 Henry Ward black-olive cage — own sheet](Brush-Artist-Refs-12-Henry-Ward-black-olive-cage-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 9 % → 10 % | 17.0 px | 0.58 | 1.15 | 212 |
| stroke 2 | 7 % → 10 % | 15.8 px | 0.58 | 1.46 | 174 |
| stroke 3 | 18 % → 13 % | 28.0 px | 0.58 | 0.72 | 212 |
| stroke 4 | 20 % → 14 % | 39.4 px | 0.59 | 0.70 | 142 |
| stroke 5 | 18 % → 7 % | 33.8 px | 0.58 | 0.40 | 135 |
| stroke 6 | 29 % → 15 % | 54.8 px | 0.58 | 0.52 | 202 |

## Brush Artist · Refs · #13 Henry Ward blue streaky form — own sheet
own sheet 600 × 600 · Gouache 1.00 · 50 px · 8.7 s

![Brush Artist · Refs · #13 Henry Ward blue streaky form — own sheet](Brush-Artist-Refs-13-Henry-Ward-blue-streaky-form-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 5 % → 0 % | 15.9 px | 0.00 | 0.00 | 157 |
| stroke 2 | 13 % → 0 % | 40.6 px | 0.00 | 0.00 | 191 |
| stroke 3 | 22 % → 0 % | 62.3 px | 0.00 | 0.00 | 190 |
| stroke 4 | 24 % → 0 % | 78.4 px | 0.00 | 0.00 | 213 |
| stroke 5 | 31 % → 0 % | 90.1 px | 0.00 | 0.00 | 195 |
| stroke 6 | 37 % → 0 % | 105.3 px | 0.00 | 0.00 | 211 |
| stroke 7 | 36 % → 0 % | 107.2 px | 0.00 | 0.00 | 198 |
| stroke 8 | 40 % → 0 % | 120.3 px | 0.00 | 0.00 | 187 |
| stroke 9 | 33 % → 0 % | 102.9 px | 0.00 | 0.00 | 180 |
| stroke 10 | 32 % → 0 % | 105.4 px | 0.00 | 0.00 | 178 |
| stroke 11 | 30 % → 0 % | 92.1 px | 0.00 | 0.00 | 188 |
| stroke 12 | 26 % → 0 % | 78.3 px | 0.00 | 0.00 | 162 |
| stroke 13 | 24 % → 0 % | 74.8 px | 0.00 | 0.00 | 165 |
| stroke 14 | 29 % → 0 % | 84.9 px | 0.00 | 0.00 | 223 |
| stroke 15 | 30 % → 0 % | 86.3 px | 0.00 | 0.00 | 171 |
| stroke 16 | 35 % → 0 % | 104.8 px | 0.00 | 0.00 | 218 |
| stroke 17 | 41 % → 0 % | 103.0 px | 0.00 | 0.00 | 200 |
| stroke 18 | 49 % → 0 % | 117.7 px | 0.00 | 0.00 | 215 |
| stroke 19 | 51 % → 0 % | 104.2 px | 0.00 | 0.00 | 194 |
| stroke 20 | 60 % → 0 % | 115.5 px | 0.00 | 0.00 | 223 |
| stroke 21 | 7 % → 0 % | 15.0 px | 0.00 | 0.00 | 144 |
| stroke 22 | 6 % → 0 % | 18.5 px | 0.00 | 0.00 | 193 |
| stroke 23 | 11 % → 0 % | 35.1 px | 0.00 | 0.00 | 144 |
| stroke 24 | 4 % → 0 % | 11.0 px | 0.00 | 0.00 | 150 |
| stroke 25 | 4 % → 0 % | 9.1 px | 0.00 | 0.00 | 147 |

## Brush Artist · Refs · #14 Henry Ward olive totem — own sheet
own sheet 600 × 600 · Impasto 1.00 · 48 px · 6.7 s

![Brush Artist · Refs · #14 Henry Ward olive totem — own sheet](Brush-Artist-Refs-14-Henry-Ward-olive-totem-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 18 % → 46 % | 46.6 px | 0.38 | 2.57 | 140 |
| stroke 2 | 20 % → 50 % | 61.7 px | 0.38 | 2.53 | 139 |
| stroke 3 | 27 % → 52 % | 93.9 px | 0.39 | 1.89 | 129 |
| stroke 4 | 30 % → 54 % | 110.9 px | 0.39 | 1.82 | 147 |
| stroke 5 | 38 % → 63 % | 134.1 px | 0.39 | 1.64 | 132 |
| stroke 6 | 38 % → 64 % | 149.8 px | 0.39 | 1.67 | 142 |
| stroke 7 | 35 % → 60 % | 119.1 px | 0.39 | 1.70 | 129 |
| stroke 8 | 37 % → 62 % | 141.6 px | 0.39 | 1.67 | 140 |
| stroke 9 | 38 % → 62 % | 131.6 px | 0.39 | 1.64 | 139 |
| stroke 10 | 37 % → 61 % | 136.5 px | 0.39 | 1.65 | 145 |
| stroke 11 | 38 % → 64 % | 136.7 px | 0.39 | 1.66 | 141 |
| stroke 12 | 38 % → 64 % | 143.5 px | 0.38 | 1.68 | 135 |
| stroke 13 | 37 % → 66 % | 129.3 px | 0.39 | 1.78 | 126 |
| stroke 14 | 36 % → 61 % | 131.1 px | 0.39 | 1.70 | 148 |
| stroke 15 | 39 % → 65 % | 134.4 px | 0.39 | 1.66 | 117 |
| stroke 16 | 38 % → 63 % | 136.6 px | 0.39 | 1.67 | 167 |
| stroke 17 | 37 % → 61 % | 124.1 px | 0.39 | 1.64 | 165 |
| stroke 18 | 40 % → 65 % | 152.2 px | 0.39 | 1.63 | 139 |
| stroke 19 | 38 % → 58 % | 131.3 px | 0.39 | 1.54 | 115 |
| stroke 20 | 40 % → 53 % | 142.6 px | 0.39 | 1.31 | 160 |
| stroke 21 | 46 % → 53 % | 136.0 px | 0.39 | 1.15 | 131 |
| stroke 22 | 53 % → 51 % | 143.0 px | 0.39 | 0.97 | 144 |

Numbers say: wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #15 Ultramarine brush script — own sheet
own sheet 600 × 600 · Ink 1.00 · 4 px · 8.0 s

![Brush Artist · Refs · #15 Ultramarine brush script — own sheet](Brush-Artist-Refs-15-Ultramarine-brush-script-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 40 % → 42 % | 9.0 px | 0.65 | 1.05 | 45 |
| stroke 2 | 41 % → 43 % | 9.0 px | 0.67 | 1.07 | 44 |
| stroke 3 | 39 % → 42 % | 9.4 px | 0.72 | 1.08 | 24 |
| stroke 4 | 42 % → 46 % | 10.2 px | 0.74 | 1.10 | 13 |
| stroke 5 | 46 % → 49 % | 10.1 px | 0.72 | 1.06 | 24 |
| stroke 6 | 43 % → 45 % | 9.7 px | 0.65 | 1.05 | 44 |
| stroke 7 | 44 % → 47 % | 9.3 px | 0.72 | 1.08 | 25 |
| stroke 8 | 37 % → 39 % | 8.9 px | 0.65 | 1.06 | 41 |
| stroke 9 | 39 % → 42 % | 9.1 px | 0.70 | 1.07 | 42 |
| stroke 10 | 35 % → 37 % | 9.6 px | 0.66 | 1.05 | 36 |
| stroke 11 | 44 % → 47 % | 9.9 px | 0.69 | 1.06 | 34 |
| stroke 12 | 39 % → 41 % | 9.4 px | 0.65 | 1.06 | 56 |
| stroke 13 | 45 % → 46 % | 10.1 px | 0.69 | 1.04 | 34 |
| stroke 14 | 37 % → 40 % | 9.6 px | 0.71 | 1.07 | 21 |
| stroke 15 | 37 % → 38 % | 9.0 px | 0.67 | 1.05 | 49 |
| stroke 16 | 42 % → 45 % | 9.4 px | 0.70 | 1.06 | 28 |
| stroke 17 | 41 % → 45 % | 7.1 px | 0.71 | 1.09 | 49 |
| stroke 18 | 43 % → 45 % | 9.3 px | 0.73 | 1.05 | 26 |
| stroke 19 | 40 % → 42 % | 9.0 px | 0.65 | 1.06 | 56 |
| stroke 20 | 42 % → 44 % | 9.7 px | 0.69 | 1.06 | 33 |
| stroke 21 | 39 % → 42 % | 9.6 px | 0.69 | 1.07 | 37 |
| stroke 22 | 44 % → 46 % | 8.9 px | 0.65 | 1.06 | 52 |
| stroke 23 | 38 % → 42 % | 9.5 px | 0.72 | 1.10 | 23 |
| stroke 24 | 39 % → 42 % | 9.1 px | 0.73 | 1.06 | 26 |
| stroke 25 | 41 % → 44 % | 10.0 px | 0.71 | 1.06 | 34 |
| stroke 26 | 45 % → 47 % | 9.1 px | 0.66 | 1.04 | 40 |
| stroke 27 | 43 % → 45 % | 9.0 px | 0.62 | 1.05 | 57 |
| stroke 28 | 45 % → 47 % | 9.3 px | 0.70 | 1.06 | 50 |
| stroke 29 | 35 % → 38 % | 10.4 px | 0.69 | 1.08 | 28 |
| stroke 30 | 39 % → 40 % | 8.5 px | 0.70 | 1.04 | 33 |
| stroke 31 | 43 % → 46 % | 10.4 px | 0.74 | 1.07 | 18 |
| stroke 32 | 41 % → 45 % | 9.3 px | 0.70 | 1.09 | 28 |
| stroke 33 | 35 % → 40 % | 10.9 px | 0.73 | 1.13 | 17 |
| stroke 34 | 41 % → 45 % | 10.1 px | 0.74 | 1.09 | 22 |
| stroke 35 | 36 % → 38 % | 9.4 px | 0.67 | 1.06 | 43 |

## Brush Artist · Refs · #18 Blue oil-stick scribbles — own sheet
own sheet 600 × 600 · Pastel 1.00 · 10 px · 3.1 s

![Brush Artist · Refs · #18 Blue oil-stick scribbles — own sheet](Brush-Artist-Refs-18-Blue-oil-stick-scribbles-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 16 % → 32 % | 3.9 px | 0.49 | 2.03 | 124 |
| stroke 2 | 13 % → 37 % | 3.6 px | 0.49 | 2.75 | 157 |
| stroke 3 | 16 % → 26 % | 5.8 px | 0.49 | 1.64 | 183 |
| stroke 4 | 15 % → 29 % | 7.9 px | 0.49 | 1.91 | 208 |
| stroke 5 | 29 % → 34 % | 8.5 px | 0.49 | 1.18 | 161 |
| stroke 6 | 26 % → 26 % | 9.4 px | 0.49 | 1.02 | 160 |
| stroke 7 | 26 % → 32 % | 8.4 px | 0.49 | 1.24 | 183 |
| stroke 8 | 30 % → 30 % | 17.0 px | 0.49 | 1.00 | 188 |

Numbers say: wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #20 Orange-red crayon scribble — own sheet
own sheet 600 × 600 · Pastel 1.00 · 14 px · 2.7 s

![Brush Artist · Refs · #20 Orange-red crayon scribble — own sheet](Brush-Artist-Refs-20-Orange-red-crayon-scribble-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 8 % → 19 % | 5.5 px | 0.59 | 2.47 | 178 |
| stroke 2 | 9 % → 22 % | 6.6 px | 0.60 | 2.50 | 164 |
| stroke 3 | 13 % → 21 % | 8.3 px | 0.60 | 1.65 | 175 |
| stroke 4 | 24 % → 32 % | 8.8 px | 0.60 | 1.36 | 202 |
| stroke 5 | 28 % → 28 % | 7.9 px | 0.59 | 1.00 | 177 |
| stroke 6 | 22 % → 22 % | 16.4 px | 0.60 | 1.00 | 180 |

Numbers say: wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #21 Gritty black contours — own sheet
own sheet 600 × 600 · Gouache 1.00 · 12 px · 3.7 s

![Brush Artist · Refs · #21 Gritty black contours — own sheet](Brush-Artist-Refs-21-Gritty-black-contours-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 6 % → 4 % | 6.2 px | 0.36 | 0.68 | 141 |
| stroke 2 | 5 % → 2 % | 7.9 px | 0.36 | 0.47 | 167 |
| stroke 3 | 9 % → 2 % | 7.8 px | 0.37 | 0.17 | 117 |
| stroke 4 | 9 % → 3 % | 10.9 px | 0.36 | 0.36 | 156 |
| stroke 5 | 10 % → 4 % | 12.7 px | 0.35 | 0.35 | 105 |

## Brush Artist · Refs · #22 Bold black brush poster — own sheet
own sheet 600 × 600 · Ink 1.00 · 20 px · 4.6 s

![Brush Artist · Refs · #22 Bold black brush poster — own sheet](Brush-Artist-Refs-22-Bold-black-brush-poster-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 24 % → 28 % | 38.8 px | 0.95 | 1.18 | 102 |
| stroke 2 | 28 % → 39 % | 42.9 px | 0.94 | 1.38 | 30 |
| stroke 3 | 30 % → 30 % | 46.0 px | 0.94 | 1.00 | 42 |
| stroke 4 | 30 % → 41 % | 57.8 px | 0.94 | 1.41 | 58 |
| stroke 5 | 27 % → 27 % | 46.3 px | 0.93 | 1.00 | 77 |

## Brush Artist · Refs · #23 Dry white on orange + black line — own sheet
own sheet 600 × 600 · Gouache 1.00 · 50 px · 7.6 s

![Brush Artist · Refs · #23 Dry white on orange + black line — own sheet](Brush-Artist-Refs-23-Dry-white-on-orange-black-line-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 4 % → 11 % | 14.5 px | 0.38 | 2.70 | 126 |
| stroke 2 | 8 % → 10 % | 26.7 px | 0.38 | 1.35 | 152 |
| stroke 3 | 13 % → 11 % | 49.0 px | 0.38 | 0.81 | 150 |
| stroke 4 | 17 % → 12 % | 68.6 px | 0.38 | 0.67 | 153 |
| stroke 5 | 23 % → 13 % | 85.0 px | 0.38 | 0.55 | 258 |
| stroke 6 | 26 % → 14 % | 106.9 px | 0.38 | 0.53 | 183 |
| stroke 7 | 23 % → 13 % | 86.4 px | 0.38 | 0.57 | 134 |
| stroke 8 | 22 % → 12 % | 87.4 px | 0.38 | 0.53 | 159 |
| stroke 9 | 19 % → 11 % | 69.7 px | 0.38 | 0.60 | 137 |
| stroke 10 | 18 % → 11 % | 68.9 px | 0.38 | 0.63 | 144 |
| stroke 11 | 20 % → 11 % | 73.3 px | 0.38 | 0.56 | 146 |
| stroke 12 | 19 % → 12 % | 72.9 px | 0.38 | 0.65 | 148 |
| stroke 13 | 20 % → 14 % | 75.6 px | 0.38 | 0.70 | 137 |
| stroke 14 | 21 % → 14 % | 84.0 px | 0.38 | 0.64 | 167 |
| stroke 15 | 21 % → 13 % | 79.6 px | 0.38 | 0.62 | 129 |
| stroke 16 | 22 % → 11 % | 87.4 px | 0.38 | 0.52 | 164 |
| stroke 17 | 22 % → 9 % | 76.2 px | 0.38 | 0.40 | 146 |
| stroke 18 | 27 % → 9 % | 99.3 px | 0.38 | 0.34 | 139 |

Numbers say: wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #24 Picasso flat oil — own sheet
own sheet 600 × 600 · Oil 0.89 · Oil glaze 0.11 · 34 px · 5.2 s

![Brush Artist · Refs · #24 Picasso flat oil — own sheet](Brush-Artist-Refs-24-Picasso-flat-oil-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 14 % → 44 % | 30.0 px | 0.22 | 3.11 | 132 |
| stroke 2 | 19 % → 47 % | 44.5 px | 0.23 | 2.49 | 128 |
| stroke 3 | 27 % → 56 % | 59.7 px | 0.23 | 2.06 | 145 |
| stroke 4 | 37 % → 62 % | 82.9 px | 0.23 | 1.69 | 155 |
| stroke 5 | 41 % → 68 % | 91.2 px | 0.22 | 1.64 | 152 |
| stroke 6 | 42 % → 63 % | 96.5 px | 0.22 | 1.52 | 133 |
| stroke 7 | 42 % → 63 % | 87.5 px | 0.23 | 1.51 | 126 |
| stroke 8 | 42 % → 63 % | 101.6 px | 0.23 | 1.50 | 145 |
| stroke 9 | 34 % → 60 % | 74.4 px | 0.23 | 1.76 | 132 |
| stroke 10 | 38 % → 58 % | 89.8 px | 0.23 | 1.55 | 137 |
| stroke 11 | 35 % → 56 % | 74.6 px | 0.24 | 1.61 | 143 |
| stroke 12 | 37 % → 58 % | 88.3 px | 0.24 | 1.56 | 129 |
| stroke 13 | 35 % → 64 % | 77.9 px | 0.25 | 1.81 | 156 |
| stroke 14 | 36 % → 66 % | 82.0 px | 0.24 | 1.82 | 137 |
| stroke 15 | 36 % → 60 % | 76.0 px | 0.24 | 1.67 | 137 |
| stroke 16 | 36 % → 52 % | 83.2 px | 0.24 | 1.46 | 152 |
| stroke 17 | 41 % → 47 % | 86.1 px | 0.24 | 1.15 | 159 |
| stroke 18 | 42 % → 42 % | 101.0 px | 0.24 | 1.00 | 136 |

Numbers say: wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #25 Yellow heavy flat stroke — own sheet
own sheet 600 × 600 · Impasto 1.00 · 110 px · 2.8 s

![Brush Artist · Refs · #25 Yellow heavy flat stroke — own sheet](Brush-Artist-Refs-25-Yellow-heavy-flat-stroke-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 18 % → 18 % | 103.7 px | 0.16 | 0.98 | 717 |

## Brush Artist · Refs · #27 Orange impasto swatch — own sheet
own sheet 600 × 600 · Impasto 1.00 · 60 px · 3.0 s

![Brush Artist · Refs · #27 Orange impasto swatch — own sheet](Brush-Artist-Refs-27-Orange-impasto-swatch-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 8 % → 21 % | 58.4 px | 0.32 | 2.66 | 73 |
| stroke 2 | 7 % → 33 % | 62.2 px | 0.32 | 4.61 | 49 |
| stroke 3 | 25 % → 34 % | 238.0 px | 0.32 | 1.41 | 52 |
| stroke 4 | 10 % → 12 % | 69.5 px | 0.34 | 1.26 | 63 |
| stroke 5 | 17 % → 32 % | 61.8 px | 0.31 | 1.90 | 76 |
| stroke 6 | 17 % → 31 % | 143.7 px | 0.32 | 1.77 | 67 |
| stroke 7 | 8 % → 14 % | 68.6 px | 0.31 | 1.88 | 58 |
| stroke 8 | 32 % → 33 % | 328.8 px | 0.32 | 1.04 | 56 |
| stroke 9 | 37 % → 36 % | 182.9 px | 0.32 | 0.97 | 72 |
| stroke 10 | 33 % → 32 % | 298.6 px | 0.32 | 0.97 | 53 |

Numbers say: wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #28 Miles Davis black lines — own sheet
own sheet 600 × 600 · Ink 1.00 · 22 px · 5.6 s

![Brush Artist · Refs · #28 Miles Davis black lines — own sheet](Brush-Artist-Refs-28-Miles-Davis-black-lines-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 22 % → 31 % | 36.1 px | 0.88 | 1.42 | 171 |
| stroke 2 | 26 % → 47 % | 35.8 px | 0.88 | 1.79 | 150 |
| stroke 3 | 38 % → 42 % | 73.3 px | 0.88 | 1.11 | 96 |
| stroke 4 | 41 % → 47 % | 81.4 px | 0.88 | 1.16 | 166 |
| stroke 5 | 54 % → 54 % | 108.2 px | 0.88 | 1.00 | 131 |

Numbers say: wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #29 Shrigley magenta asterisk — own sheet
own sheet 600 × 600 · Watercolour 1.00 · 70 px · 5.7 s

![Brush Artist · Refs · #29 Shrigley magenta asterisk — own sheet](Brush-Artist-Refs-29-Shrigley-magenta-asterisk-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 13 % → 37 % | 46.6 px | 0.67 | 2.86 | 181 |
| stroke 2 | 12 % → 12 % | 87.1 px | 0.67 | 1.00 | 178 |
| stroke 3 | 28 % → 37 % | 100.9 px | 0.67 | 1.31 | 195 |
| stroke 4 | 23 % → 23 % | 164.0 px | 0.67 | 1.02 | 184 |

Numbers say: wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #30 Red gouache face patch — own sheet
own sheet 600 × 600 · Gouache 1.00 · 60 px · 11.2 s

![Brush Artist · Refs · #30 Red gouache face patch — own sheet](Brush-Artist-Refs-30-Red-gouache-face-patch-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 11 % → 37 % | 50.6 px | 0.54 | 3.29 | 156 |
| stroke 2 | 15 % → 41 % | 74.2 px | 0.54 | 2.74 | 146 |
| stroke 3 | 24 % → 50 % | 115.1 px | 0.54 | 2.08 | 176 |
| stroke 4 | 26 % → 52 % | 133.4 px | 0.54 | 1.95 | 202 |
| stroke 5 | 34 % → 60 % | 160.6 px | 0.54 | 1.77 | 183 |
| stroke 6 | 35 % → 61 % | 178.6 px | 0.54 | 1.76 | 184 |
| stroke 7 | 35 % → 59 % | 164.2 px | 0.54 | 1.70 | 213 |
| stroke 8 | 34 % → 56 % | 162.3 px | 0.54 | 1.66 | 192 |
| stroke 9 | 36 % → 60 % | 172.7 px | 0.53 | 1.66 | 172 |
| stroke 10 | 38 % → 62 % | 196.7 px | 0.53 | 1.64 | 180 |
| stroke 11 | 37 % → 61 % | 181.6 px | 0.53 | 1.67 | 174 |
| stroke 12 | 36 % → 58 % | 179.8 px | 0.53 | 1.60 | 171 |
| stroke 13 | 33 % → 46 % | 157.0 px | 0.53 | 1.38 | 217 |
| stroke 14 | 33 % → 41 % | 159.9 px | 0.53 | 1.24 | 220 |
| stroke 15 | 33 % → 37 % | 153.6 px | 0.53 | 1.12 | 189 |
| stroke 16 | 39 % → 39 % | 186.3 px | 0.53 | 0.98 | 178 |

Numbers say: wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #31 Warhol blotted line — own sheet
own sheet 600 × 600 · Ink 1.00 · 6 px · 4.5 s

![Brush Artist · Refs · #31 Warhol blotted line — own sheet](Brush-Artist-Refs-31-Warhol-blotted-line-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 22 % → 43 % | 16.5 px | 0.83 | 1.94 | 71 |
| stroke 2 | 17 % → 23 % | 15.7 px | 0.81 | 1.35 | 78 |
| stroke 3 | 24 % → 25 % | 24.9 px | 0.81 | 1.03 | 69 |
| stroke 4 | 32 % → 41 % | 32.7 px | 0.83 | 1.28 | 44 |
| stroke 5 | 37 % → 45 % | 38.1 px | 0.83 | 1.21 | 69 |
| stroke 6 | 34 % → 35 % | 27.8 px | 0.81 | 1.03 | 71 |

Numbers say: wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #32 Thick orange swipes — own sheet
own sheet 600 × 600 · Impasto 1.00 · 90 px · 3.4 s

![Brush Artist · Refs · #32 Thick orange swipes — own sheet](Brush-Artist-Refs-32-Thick-orange-swipes-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 14 % → 27 % | 86.6 px | 0.02 | 1.89 | 342 |
| stroke 2 | 26 % → 37 % | 177.9 px | 0.02 | 1.41 | 294 |
| stroke 3 | 27 % → 27 % | 176.1 px | 0.02 | 0.98 | 325 |

Numbers say: wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #33 Red wet-in-wet band — own sheet
own sheet 600 × 600 · Watercolour 1.00 · 80 px · 9.8 s

![Brush Artist · Refs · #33 Red wet-in-wet band — own sheet](Brush-Artist-Refs-33-Red-wet-in-wet-band-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 22 % → 57 % | 83.4 px | 0.61 | 2.61 | 405 |
| stroke 2 | 28 % → 51 % | 228.4 px | 0.62 | 1.82 | 125 |
| stroke 3 | 34 % → 53 % | 330.0 px | 0.61 | 1.57 | 116 |
| stroke 4 | 40 % → 60 % | 389.9 px | 0.62 | 1.51 | 94 |
| stroke 5 | 40 % → 55 % | 339.4 px | 0.61 | 1.38 | 119 |
| stroke 6 | 41 % → 48 % | 310.3 px | 0.59 | 1.18 | 123 |

Numbers say: wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #34 Magenta oil patches — own sheet
own sheet 600 × 600 · Oil 0.89 · Oil glaze 0.11 · 60 px · 3.3 s

![Brush Artist · Refs · #34 Magenta oil patches — own sheet](Brush-Artist-Refs-34-Magenta-oil-patches-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 8 % → 39 % | 57.1 px | 0.13 | 4.77 | 92 |
| stroke 2 | 8 % → 28 % | 56.8 px | 0.14 | 3.32 | 72 |
| stroke 3 | 7 % → 32 % | 58.6 px | 0.13 | 4.60 | 70 |
| stroke 4 | 15 % → 19 % | 122.2 px | 0.12 | 1.26 | 67 |
| stroke 5 | 21 % → 30 % | 112.2 px | 0.13 | 1.45 | 87 |
| stroke 6 | 19 % → 36 % | 159.7 px | 0.13 | 1.91 | 70 |
| stroke 7 | 28 % → 33 % | 226.6 px | 0.13 | 1.17 | 68 |
| stroke 8 | 30 % → 37 % | 213.6 px | 0.13 | 1.21 | 103 |
| stroke 9 | 23 % → 25 % | 147.9 px | 0.14 | 1.07 | 91 |
| stroke 10 | 27 % → 27 % | 240.6 px | 0.14 | 1.00 | 74 |
| stroke 11 | 33 % → 33 % | 297.2 px | 0.13 | 1.00 | 67 |
| stroke 12 | 24 % → 24 % | 173.6 px | 0.13 | 1.00 | 66 |

Numbers say: wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #35 Red band with runs — own sheet
own sheet 600 × 600 · Watercolour 1.00 · 70 px · 7.5 s

![Brush Artist · Refs · #35 Red band with runs — own sheet](Brush-Artist-Refs-35-Red-band-with-runs-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 37 % → 47 % | 140.3 px | 0.45 | 1.27 | 330 |

## Brush Artist · Refs · #36 Magenta letters flat brush — own sheet
own sheet 600 × 600 · Gouache 1.00 · 36 px · 10.4 s

![Brush Artist · Refs · #36 Magenta letters flat brush — own sheet](Brush-Artist-Refs-36-Magenta-letters-flat-brush-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 20 % → 38 % | 58.3 px | 0.50 | 1.95 | 22 |
| stroke 2 | 20 % → 31 % | 45.2 px | 0.51 | 1.54 | 34 |
| stroke 3 | 28 % → 52 % | 84.6 px | 0.50 | 1.83 | 31 |
| stroke 4 | 26 % → 44 % | 50.3 px | 0.51 | 1.69 | 119 |
| stroke 5 | 33 % → 54 % | 96.3 px | 0.50 | 1.63 | 76 |
| stroke 6 | 43 % → 56 % | 246.0 px | 0.49 | 1.30 | 17 |
| stroke 7 | 30 % → 43 % | 56.6 px | 0.50 | 1.43 | 111 |
| stroke 8 | 31 % → 52 % | 97.7 px | 0.51 | 1.66 | 80 |
| stroke 9 | 38 % → 50 % | 158.2 px | 0.51 | 1.31 | 30 |
| stroke 10 | 37 % → 62 % | 107.5 px | 0.50 | 1.68 | 76 |
| stroke 11 | 39 % → 61 % | 225.6 px | 0.49 | 1.55 | 17 |
| stroke 12 | 44 % → 55 % | 82.9 px | 0.50 | 1.26 | 109 |
| stroke 13 | 31 % → 45 % | 113.5 px | 0.51 | 1.43 | 38 |
| stroke 14 | 34 % → 50 % | 129.9 px | 0.51 | 1.47 | 31 |
| stroke 15 | 36 % → 54 % | 105.5 px | 0.50 | 1.49 | 75 |
| stroke 16 | 39 % → 47 % | 221.7 px | 0.50 | 1.23 | 19 |
| stroke 17 | 43 % → 51 % | 81.6 px | 0.50 | 1.18 | 120 |
| stroke 18 | 26 % → 35 % | 95.6 px | 0.50 | 1.34 | 30 |
| stroke 19 | 39 % → 37 % | 112.8 px | 0.50 | 0.97 | 29 |
| stroke 20 | 45 % → 44 % | 129.9 px | 0.51 | 0.98 | 35 |
| stroke 21 | 40 % → 38 % | 78.2 px | 0.50 | 0.94 | 82 |

Numbers say: wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #37 Oil still life dabs — own sheet
own sheet 600 × 600 · Oil 0.89 · Oil glaze 0.11 · 40 px · 2.5 s

![Brush Artist · Refs · #37 Oil still life dabs — own sheet](Brush-Artist-Refs-37-Oil-still-life-dabs-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 6 % → 6 % | 38.2 px | 0.37 | 1.00 | 29 |
| stroke 2 | 6 % → 26 % | 39.8 px | 0.40 | 4.69 | 20 |
| stroke 3 | 11 % → 33 % | 86.6 px | 0.39 | 3.00 | 16 |
| stroke 4 | 8 % → 8 % | 39.3 px | 0.37 | 1.00 | 40 |
| stroke 5 | 6 % → 10 % | 43.2 px | 0.38 | 1.67 | 26 |
| stroke 6 | 13 % → 29 % | 80.2 px | 0.40 | 2.26 | 29 |
| stroke 7 | 11 % → 22 % | 113.9 px | 0.38 | 2.08 | 9 |
| stroke 8 | 8 % → 13 % | 85.3 px | 0.38 | 1.59 | 12 |
| stroke 9 | 12 % → 13 % | 61.1 px | 0.36 | 1.12 | 43 |
| stroke 10 | 20 % → 24 % | 100.4 px | 0.40 | 1.20 | 39 |
| stroke 11 | 23 % → 27 % | 194.4 px | 0.41 | 1.15 | 17 |
| stroke 12 | 20 % → 20 % | 212.5 px | 0.39 | 1.00 | 11 |
| stroke 13 | 15 % → 15 % | 150.5 px | 0.42 | 1.00 | 16 |
| stroke 14 | 15 % → 15 % | 121.2 px | 0.38 | 1.00 | 15 |

Numbers say: wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #38 Sanguine drawing — own sheet
own sheet 600 × 600 · Pastel 1.00 · 6 px · 2.1 s

![Brush Artist · Refs · #38 Sanguine drawing — own sheet](Brush-Artist-Refs-38-Sanguine-drawing-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 3 % → 15 % | 3.3 px | 0.57 | 4.99 | 5 |
| stroke 2 | 3 % → 8 % | 2.9 px | 0.57 | 3.03 | 7 |
| stroke 3 | 3 % → 9 % | 3.3 px | 0.57 | 3.13 | 6 |
| stroke 4 | 2 % → 18 % | 2.8 px | 0.57 | 7.17 | 6 |
| stroke 5 | 3 % → 7 % | 2.9 px | 0.57 | 2.87 | 9 |
| stroke 6 | 3 % → 19 % | 3.5 px | 0.57 | 6.36 | 3 |
| stroke 7 | 5 % → 15 % | 5.3 px | 0.57 | 3.13 | 6 |
| stroke 8 | 4 % → 16 % | 4.8 px | 0.57 | 3.71 | 4 |
| stroke 9 | 3 % → 8 % | 3.4 px | 0.57 | 2.52 | 9 |
| stroke 10 | 4 % → 16 % | 4.9 px | 0.57 | 3.75 | 3 |
| stroke 11 | 3 % → 4 % | 3.0 px | 0.57 | 1.63 | 6 |
| stroke 12 | 4 % → 16 % | 4.7 px | 0.57 | 3.75 | 3 |
| stroke 13 | 8 % → 18 % | 9.2 px | 0.57 | 2.20 | 7 |
| stroke 14 | 5 % → 14 % | 5.3 px | 0.57 | 2.95 | 3 |
| stroke 15 | 9 % → 18 % | 10.7 px | 0.57 | 1.88 | 7 |
| stroke 16 | 6 % → 16 % | 7.0 px | 0.57 | 2.64 | 4 |
| stroke 17 | 4 % → 9 % | 5.0 px | 0.57 | 2.12 | 4 |
| stroke 18 | 3 % → 5 % | 3.1 px | 0.57 | 1.89 | 3 |
| stroke 19 | 6 % → 17 % | 7.4 px | 0.57 | 2.68 | 9 |
| stroke 20 | 9 % → 14 % | 9.8 px | 0.57 | 1.66 | 3 |
| stroke 21 | 4 % → 4 % | 4.6 px | 0.57 | 1.00 | 6 |
| stroke 22 | 8 % → 14 % | 9.2 px | 0.57 | 1.71 | 5 |
| stroke 23 | 8 % → 12 % | 8.7 px | 0.57 | 1.63 | 4 |
| stroke 24 | 4 % → 8 % | 5.0 px | 0.57 | 1.72 | 3 |
| stroke 25 | 8 % → 15 % | 9.3 px | 0.57 | 1.87 | 7 |
| stroke 26 | 6 % → 8 % | 6.9 px | 0.57 | 1.32 | 4 |
| stroke 27 | 4 % → 5 % | 4.8 px | 0.57 | 1.07 | 5 |
| stroke 28 | 8 % → 13 % | 8.9 px | 0.57 | 1.61 | 4 |
| stroke 29 | 8 % → 17 % | 9.0 px | 0.57 | 2.18 | 7 |
| stroke 30 | 13 % → 17 % | 15.2 px | 0.57 | 1.29 | 4 |
| stroke 31 | 5 % → 7 % | 6.0 px | 0.57 | 1.24 | 7 |
| stroke 32 | 11 % → 14 % | 12.9 px | 0.57 | 1.23 | 5 |
| stroke 33 | 8 % → 9 % | 9.5 px | 0.57 | 1.06 | 10 |
| stroke 34 | 11 % → 14 % | 12.3 px | 0.57 | 1.34 | 4 |
| stroke 35 | 9 % → 15 % | 10.7 px | 0.57 | 1.57 | 6 |
| stroke 36 | 10 % → 13 % | 11.9 px | 0.57 | 1.26 | 7 |
| stroke 37 | 10 % → 16 % | 11.4 px | 0.57 | 1.63 | 4 |
| stroke 38 | 14 % → 20 % | 15.3 px | 0.57 | 1.46 | 5 |
| stroke 39 | 14 % → 17 % | 16.5 px | 0.57 | 1.20 | 4 |
| stroke 40 | 6 % → 7 % | 7.3 px | 0.57 | 1.15 | 5 |
| stroke 41 | 16 % → 16 % | 18.2 px | 0.57 | 1.01 | 8 |
| stroke 42 | 14 % → 16 % | 16.1 px | 0.57 | 1.15 | 4 |
| stroke 43 | 11 % → 13 % | 13.0 px | 0.57 | 1.16 | 5 |
| stroke 44 | 13 % → 16 % | 15.2 px | 0.57 | 1.19 | 3 |
| stroke 45 | 2 % → 2 % | 2.8 px | 0.56 | 1.00 | 9 |
| stroke 46 | 17 % → 17 % | 18.9 px | 0.57 | 1.00 | 7 |
| stroke 47 | 14 % → 14 % | 15.9 px | 0.57 | 1.00 | 4 |
| stroke 48 | 13 % → 14 % | 14.7 px | 0.57 | 1.06 | 3 |
| stroke 49 | 19 % → 19 % | 21.8 px | 0.57 | 1.00 | 6 |
| stroke 50 | 11 % → 11 % | 12.2 px | 0.57 | 1.00 | 4 |

Numbers say: wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #39 Very thick impasto — own sheet
own sheet 600 × 600 · Impasto 1.00 · 60 px · 4.1 s

![Brush Artist · Refs · #39 Very thick impasto — own sheet](Brush-Artist-Refs-39-Very-thick-impasto-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 24 % → 35 % | 55.6 px | 0.43 | 1.44 | 279 |
| stroke 2 | 30 % → 46 % | 91.2 px | 0.43 | 1.52 | 284 |
| stroke 3 | 37 % → 48 % | 123.1 px | 0.44 | 1.31 | 271 |
| stroke 4 | 31 % → 43 % | 90.2 px | 0.43 | 1.39 | 303 |
| stroke 5 | 41 % → 39 % | 102.0 px | 0.43 | 0.97 | 266 |

Numbers say: wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #40 Watercolour blooms — own sheet
own sheet 600 × 600 · Watercolour 1.00 · 90 px · 7.9 s

![Brush Artist · Refs · #40 Watercolour blooms — own sheet](Brush-Artist-Refs-40-Watercolour-blooms-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 21 % → 27 % | 92.8 px | 0.12 | 1.28 | 730 |

## Brush Artist · Refs · #41 Coloured pencil hatching — own sheet
own sheet 600 × 600 · Pastel 1.00 · 4 px · 2.3 s

![Brush Artist · Refs · #41 Coloured pencil hatching — own sheet](Brush-Artist-Refs-41-Coloured-pencil-hatching-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 3 % → 15 % | 2.3 px | 0.35 | 5.04 | 8 |
| stroke 2 | 3 % → 8 % | 2.5 px | 0.35 | 2.34 | 3 |
| stroke 3 | 3 % → 12 % | 2.2 px | 0.35 | 4.03 | 4 |
| stroke 4 | 3 % → 20 % | 2.4 px | 0.35 | 6.35 | 5 |
| stroke 5 | 4 % → 8 % | 3.5 px | 0.35 | 1.78 | 5 |
| stroke 6 | 3 % → 14 % | 2.3 px | 0.35 | 4.57 | 2 |
| stroke 7 | 4 % → 17 % | 3.0 px | 0.35 | 4.34 | 7 |
| stroke 8 | 3 % → 13 % | 2.4 px | 0.35 | 4.14 | 2 |
| stroke 9 | 5 % → 12 % | 4.1 px | 0.35 | 2.18 | 4 |
| stroke 10 | 6 % → 17 % | 4.4 px | 0.35 | 2.92 | 2 |
| stroke 11 | 4 % → 14 % | 3.2 px | 0.35 | 3.38 | 3 |
| stroke 12 | 3 % → 3 % | 2.2 px | 0.35 | 1.00 | 3 |
| stroke 13 | 8 % → 19 % | 6.0 px | 0.35 | 2.35 | 5 |
| stroke 14 | 4 % → 15 % | 2.7 px | 0.35 | 4.14 | 5 |
| stroke 15 | 6 % → 13 % | 4.6 px | 0.35 | 2.12 | 3 |
| stroke 16 | 7 % → 12 % | 5.6 px | 0.35 | 1.63 | 3 |
| stroke 17 | 3 % → 3 % | 2.4 px | 0.35 | 1.00 | 3 |
| stroke 18 | 5 % → 9 % | 4.0 px | 0.36 | 1.63 | 2 |
| stroke 19 | 5 % → 14 % | 4.0 px | 0.35 | 2.72 | 5 |
| stroke 20 | 6 % → 16 % | 4.2 px | 0.35 | 2.94 | 6 |
| stroke 21 | 5 % → 15 % | 3.6 px | 0.35 | 3.13 | 3 |
| stroke 22 | 10 % → 18 % | 7.7 px | 0.35 | 1.77 | 5 |
| stroke 23 | 10 % → 15 % | 7.2 px | 0.35 | 1.54 | 3 |
| stroke 24 | 7 % → 15 % | 5.3 px | 0.35 | 2.12 | 4 |
| stroke 25 | 5 % → 12 % | 4.0 px | 0.35 | 2.27 | 3 |
| stroke 26 | 4 % → 7 % | 3.1 px | 0.35 | 1.79 | 2 |
| stroke 27 | 3 % → 8 % | 2.6 px | 0.35 | 2.35 | 4 |
| stroke 28 | 7 % → 11 % | 5.2 px | 0.36 | 1.68 | 3 |
| stroke 29 | 3 % → 15 % | 2.6 px | 0.35 | 4.48 | 2 |
| stroke 30 | 7 % → 10 % | 5.2 px | 0.35 | 1.40 | 5 |
| stroke 31 | 7 % → 16 % | 5.8 px | 0.35 | 2.09 | 3 |
| stroke 32 | 3 % → 6 % | 2.4 px | 0.36 | 1.93 | 3 |
| stroke 33 | 8 % → 13 % | 5.9 px | 0.35 | 1.65 | 5 |
| stroke 34 | 3 % → 6 % | 2.6 px | 0.35 | 1.71 | 6 |
| stroke 35 | 7 % → 15 % | 5.4 px | 0.35 | 2.11 | 3 |
| stroke 36 | 5 % → 5 % | 4.0 px | 0.35 | 1.01 | 2 |
| stroke 37 | 8 % → 16 % | 5.9 px | 0.35 | 2.07 | 3 |
| stroke 38 | 8 % → 14 % | 6.2 px | 0.35 | 1.71 | 2 |
| stroke 39 | 7 % → 12 % | 5.4 px | 0.35 | 1.65 | 4 |
| stroke 40 | 9 % → 20 % | 6.7 px | 0.36 | 2.23 | 3 |
| stroke 41 | 10 % → 15 % | 7.7 px | 0.35 | 1.46 | 8 |
| stroke 42 | 11 % → 19 % | 8.5 px | 0.36 | 1.73 | 3 |
| stroke 43 | 5 % → 9 % | 4.1 px | 0.35 | 1.66 | 2 |
| stroke 44 | 11 % → 15 % | 8.5 px | 0.36 | 1.41 | 4 |
| stroke 45 | 14 % → 19 % | 10.5 px | 0.35 | 1.37 | 2 |
| stroke 46 | 5 % → 7 % | 4.0 px | 0.35 | 1.38 | 2 |
| stroke 47 | 11 % → 14 % | 8.7 px | 0.36 | 1.21 | 2 |
| stroke 48 | 13 % → 18 % | 10.0 px | 0.36 | 1.36 | 2 |
| stroke 49 | 6 % → 9 % | 4.3 px | 0.35 | 1.65 | 5 |
| stroke 50 | 7 % → 7 % | 5.6 px | 0.35 | 1.00 | 3 |
| stroke 51 | 10 % → 16 % | 7.4 px | 0.36 | 1.67 | 5 |
| stroke 52 | 14 % → 16 % | 10.5 px | 0.35 | 1.19 | 3 |
| stroke 53 | 12 % → 16 % | 9.0 px | 0.35 | 1.35 | 4 |
| stroke 54 | 11 % → 16 % | 8.5 px | 0.35 | 1.46 | 3 |
| stroke 55 | 12 % → 16 % | 9.0 px | 0.35 | 1.34 | 5 |
| stroke 56 | 12 % → 13 % | 9.0 px | 0.35 | 1.11 | 2 |
| stroke 57 | 11 % → 14 % | 8.2 px | 0.36 | 1.31 | 5 |
| stroke 58 | 11 % → 12 % | 8.6 px | 0.35 | 1.12 | 3 |
| stroke 59 | 13 % → 15 % | 9.8 px | 0.35 | 1.16 | 4 |
| stroke 60 | 17 % → 22 % | 13.1 px | 0.35 | 1.26 | 3 |
| stroke 61 | 21 % → 22 % | 15.6 px | 0.35 | 1.05 | 5 |
| stroke 62 | 10 % → 10 % | 7.5 px | 0.35 | 1.00 | 3 |
| stroke 63 | 12 % → 13 % | 9.5 px | 0.35 | 1.09 | 5 |
| stroke 64 | 16 % → 17 % | 12.4 px | 0.35 | 1.02 | 3 |
| stroke 65 | 17 % → 17 % | 12.7 px | 0.35 | 1.00 | 3 |
| stroke 66 | 15 % → 15 % | 11.9 px | 0.35 | 1.00 | 2 |
| stroke 67 | 13 % → 14 % | 9.9 px | 0.35 | 1.06 | 3 |
| stroke 68 | 5 % → 10 % | 4.1 px | 0.35 | 1.90 | 3 |
| stroke 69 | 6 % → 6 % | 4.3 px | 0.35 | 1.00 | 3 |
| stroke 70 | 11 % → 14 % | 8.5 px | 0.35 | 1.28 | 4 |
| stroke 71 | 10 % → 12 % | 7.7 px | 0.35 | 1.17 | 3 |
| stroke 72 | 6 % → 7 % | 4.5 px | 0.35 | 1.26 | 5 |
| stroke 73 | 14 % → 14 % | 10.4 px | 0.35 | 1.00 | 2 |
| stroke 74 | 16 % → 16 % | 12.3 px | 0.35 | 1.00 | 5 |
| stroke 75 | 17 % → 17 % | 13.1 px | 0.35 | 1.00 | 2 |
| stroke 76 | 15 % → 15 % | 11.7 px | 0.36 | 1.00 | 4 |
| stroke 77 | 8 % → 10 % | 6.0 px | 0.35 | 1.32 | 2 |
| stroke 78 | 10 % → 10 % | 7.5 px | 0.35 | 1.00 | 4 |
| stroke 79 | 8 % → 8 % | 6.2 px | 0.35 | 1.00 | 2 |
| stroke 80 | 12 % → 12 % | 9.1 px | 0.36 | 1.00 | 4 |

Numbers say: wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #42 Oil pastel shaggy — own sheet
own sheet 600 × 600 · Pastel 1.00 · 18 px · 2.4 s

![Brush Artist · Refs · #42 Oil pastel shaggy — own sheet](Brush-Artist-Refs-42-Oil-pastel-shaggy-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 5 % → 27 % | 8.5 px | 0.27 | 5.25 | 11 |
| stroke 2 | 5 % → 24 % | 7.8 px | 0.29 | 5.02 | 8 |
| stroke 3 | 5 % → 29 % | 8.8 px | 0.28 | 5.49 | 9 |
| stroke 4 | 5 % → 11 % | 9.1 px | 0.26 | 1.99 | 7 |
| stroke 5 | 6 % → 11 % | 10.2 px | 0.26 | 1.77 | 7 |
| stroke 6 | 8 % → 36 % | 13.4 px | 0.28 | 4.52 | 11 |
| stroke 7 | 11 % → 30 % | 18.0 px | 0.28 | 2.79 | 8 |
| stroke 8 | 7 % → 37 % | 10.8 px | 0.28 | 5.63 | 6 |
| stroke 9 | 8 % → 21 % | 13.4 px | 0.28 | 2.61 | 8 |
| stroke 10 | 8 % → 18 % | 13.2 px | 0.29 | 2.30 | 10 |
| stroke 11 | 5 % → 26 % | 8.8 px | 0.28 | 4.89 | 8 |
| stroke 12 | 8 % → 19 % | 13.1 px | 0.28 | 2.33 | 6 |
| stroke 13 | 12 % → 23 % | 20.4 px | 0.28 | 1.91 | 9 |
| stroke 14 | 5 % → 22 % | 7.6 px | 0.28 | 4.76 | 10 |
| stroke 15 | 6 % → 24 % | 9.1 px | 0.28 | 4.28 | 6 |
| stroke 16 | 9 % → 21 % | 15.5 px | 0.29 | 2.21 | 9 |
| stroke 17 | 16 % → 37 % | 26.3 px | 0.28 | 2.36 | 11 |
| stroke 18 | 14 % → 25 % | 22.6 px | 0.28 | 1.82 | 9 |
| stroke 19 | 14 % → 30 % | 23.7 px | 0.28 | 2.08 | 10 |
| stroke 20 | 21 % → 39 % | 35.4 px | 0.28 | 1.81 | 7 |
| stroke 21 | 9 % → 16 % | 14.2 px | 0.28 | 1.88 | 6 |
| stroke 22 | 14 % → 17 % | 23.1 px | 0.27 | 1.19 | 9 |
| stroke 23 | 12 % → 17 % | 20.4 px | 0.29 | 1.37 | 10 |
| stroke 24 | 18 % → 26 % | 30.0 px | 0.29 | 1.43 | 6 |
| stroke 25 | 19 % → 34 % | 32.1 px | 0.28 | 1.75 | 8 |
| stroke 26 | 5 % → 13 % | 8.8 px | 0.28 | 2.45 | 8 |
| stroke 27 | 18 % → 26 % | 30.3 px | 0.29 | 1.41 | 11 |
| stroke 28 | 14 % → 23 % | 23.2 px | 0.29 | 1.66 | 8 |
| stroke 29 | 9 % → 26 % | 14.2 px | 0.29 | 3.08 | 7 |
| stroke 30 | 15 % → 36 % | 24.5 px | 0.28 | 2.44 | 7 |
| stroke 31 | 13 % → 17 % | 22.3 px | 0.29 | 1.24 | 11 |
| stroke 32 | 16 % → 29 % | 26.3 px | 0.29 | 1.82 | 11 |
| stroke 33 | 15 % → 16 % | 24.3 px | 0.28 | 1.09 | 6 |
| stroke 34 | 19 % → 27 % | 31.4 px | 0.28 | 1.44 | 9 |
| stroke 35 | 25 % → 35 % | 40.9 px | 0.28 | 1.39 | 10 |
| stroke 36 | 24 % → 33 % | 40.2 px | 0.28 | 1.34 | 6 |
| stroke 37 | 11 % → 12 % | 18.4 px | 0.28 | 1.04 | 7 |
| stroke 38 | 19 % → 24 % | 30.7 px | 0.29 | 1.31 | 8 |
| stroke 39 | 16 % → 22 % | 27.0 px | 0.27 | 1.35 | 11 |
| stroke 40 | 21 % → 29 % | 34.9 px | 0.28 | 1.37 | 6 |
| stroke 41 | 31 % → 34 % | 51.2 px | 0.28 | 1.12 | 9 |
| stroke 42 | 23 % → 29 % | 37.9 px | 0.28 | 1.28 | 11 |
| stroke 43 | 12 % → 12 % | 20.2 px | 0.28 | 1.00 | 9 |
| stroke 44 | 29 % → 36 % | 48.3 px | 0.28 | 1.24 | 12 |
| stroke 45 | 16 % → 16 % | 25.6 px | 0.27 | 1.00 | 8 |
| stroke 46 | 28 % → 33 % | 46.9 px | 0.28 | 1.15 | 6 |
| stroke 47 | 37 % → 41 % | 61.6 px | 0.28 | 1.09 | 11 |
| stroke 48 | 28 % → 35 % | 47.2 px | 0.28 | 1.26 | 7 |
| stroke 49 | 27 % → 30 % | 43.8 px | 0.29 | 1.11 | 11 |
| stroke 50 | 37 % → 40 % | 61.8 px | 0.28 | 1.07 | 10 |
| stroke 51 | 15 % → 15 % | 25.8 px | 0.28 | 1.00 | 11 |
| stroke 52 | 37 % → 37 % | 61.4 px | 0.28 | 1.01 | 7 |
| stroke 53 | 22 % → 26 % | 35.6 px | 0.29 | 1.20 | 6 |
| stroke 54 | 17 % → 19 % | 29.0 px | 0.29 | 1.10 | 9 |
| stroke 55 | 15 % → 15 % | 24.6 px | 0.29 | 1.00 | 7 |
| stroke 56 | 13 % → 14 % | 21.3 px | 0.27 | 1.08 | 6 |
| stroke 57 | 23 % → 23 % | 38.0 px | 0.29 | 1.00 | 12 |
| stroke 58 | 26 % → 28 % | 43.7 px | 0.28 | 1.06 | 11 |
| stroke 59 | 40 % → 40 % | 66.1 px | 0.28 | 1.00 | 7 |
| stroke 60 | 21 % → 21 % | 34.4 px | 0.29 | 1.00 | 6 |

Numbers say: wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #43 Dragged black ink blocks — own sheet
own sheet 600 × 600 · Gouache 1.00 · 70 px · 6.0 s

![Brush Artist · Refs · #43 Dragged black ink blocks — own sheet](Brush-Artist-Refs-43-Dragged-black-ink-blocks-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 11 % → 4 % | 24.9 px | 0.46 | 0.40 | 310 |
| stroke 2 | 10 % → 8 % | 35.4 px | 0.46 | 0.82 | 363 |
| stroke 3 | 18 % → 14 % | 66.1 px | 0.46 | 0.77 | 376 |
| stroke 4 | 22 % → 11 % | 75.0 px | 0.43 | 0.53 | 402 |
| stroke 5 | 31 % → 13 % | 72.0 px | 0.43 | 0.43 | 388 |

## Brush Artist · Refs · #44 Blue looping ribbon — own sheet
own sheet 600 × 600 · Oil 1.00 · 80 px · 4.3 s

![Brush Artist · Refs · #44 Blue looping ribbon — own sheet](Brush-Artist-Refs-44-Blue-looping-ribbon-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 32 % → 32 % | 42.1 px | 0.78 | 1.00 | 2381 |

## Brush Artist · Refs · #45 Soft pastel pepper — own sheet
own sheet 600 × 600 · Pastel 1.00 · 40 px · 4.1 s

![Brush Artist · Refs · #45 Soft pastel pepper — own sheet](Brush-Artist-Refs-45-Soft-pastel-pepper-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 10 % → 38 % | 11.3 px | 0.50 | 3.71 | 305 |
| stroke 2 | 18 % → 33 % | 20.7 px | 0.50 | 1.88 | 275 |
| stroke 3 | 25 % → 36 % | 16.9 px | 0.50 | 1.46 | 258 |
| stroke 4 | 24 % → 34 % | 29.4 px | 0.50 | 1.45 | 286 |
| stroke 5 | 30 % → 30 % | 20.9 px | 0.49 | 1.00 | 205 |
| stroke 6 | 35 % → 44 % | 22.7 px | 0.50 | 1.24 | 292 |
| stroke 7 | 39 % → 43 % | 21.3 px | 0.50 | 1.11 | 367 |
| stroke 8 | 43 % → 43 % | 43.7 px | 0.50 | 1.00 | 370 |

Numbers say: wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #46 Red-brown ink lips — own sheet
own sheet 600 × 600 · Watercolour 1.00 · 50 px · 7.2 s

![Brush Artist · Refs · #46 Red-brown ink lips — own sheet](Brush-Artist-Refs-46-Red-brown-ink-lips-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 13 % → 26 % | 54.5 px | 0.56 | 1.96 | 97 |
| stroke 2 | 17 % → 31 % | 72.4 px | 0.53 | 1.89 | 77 |

Numbers say: wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #47 Pink knife slabs — own sheet
own sheet 600 × 600 · Impasto 1.00 · 90 px · 4.1 s

![Brush Artist · Refs · #47 Pink knife slabs — own sheet](Brush-Artist-Refs-47-Pink-knife-slabs-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 16 % → 32 % | 81.5 px | 0.10 | 1.97 | 262 |
| stroke 2 | 29 % → 42 % | 165.6 px | 0.11 | 1.45 | 260 |
| stroke 3 | 29 % → 43 % | 165.1 px | 0.13 | 1.47 | 297 |
| stroke 4 | 39 % → 38 % | 165.8 px | 0.14 | 0.97 | 300 |

Numbers say: wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #48 Black bands with drips — own sheet
own sheet 600 × 600 · Gouache 1.00 · 70 px · 10.7 s

![Brush Artist · Refs · #48 Black bands with drips — own sheet](Brush-Artist-Refs-48-Black-bands-with-drips-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 28 % → 40 % | 72.6 px | 0.38 | 1.43 | 466 |
| stroke 2 | 43 % → 55 % | 137.3 px | 0.38 | 1.30 | 436 |
| stroke 3 | 45 % → 56 % | 141.4 px | 0.38 | 1.23 | 505 |
| stroke 4 | 48 % → 45 % | 139.2 px | 0.37 | 0.94 | 558 |

## Brush Artist · Refs · #49 Magenta letters round brush — own sheet
own sheet 600 × 600 · Ink 1.00 · 30 px · 8.7 s

![Brush Artist · Refs · #49 Magenta letters round brush — own sheet](Brush-Artist-Refs-49-Magenta-letters-round-brush-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 27 % → 46 % | 64.7 px | 0.52 | 1.68 | 26 |
| stroke 2 | 29 % → 41 % | 53.0 px | 0.53 | 1.40 | 38 |
| stroke 3 | 42 % → 68 % | 98.0 px | 0.52 | 1.62 | 39 |
| stroke 4 | 33 % → 52 % | 53.5 px | 0.52 | 1.56 | 104 |
| stroke 5 | 41 % → 66 % | 97.1 px | 0.52 | 1.62 | 90 |
| stroke 6 | 56 % → 72 % | 237.9 px | 0.52 | 1.28 | 16 |
| stroke 7 | 42 % → 58 % | 65.1 px | 0.52 | 1.36 | 109 |
| stroke 8 | 36 % → 61 % | 92.6 px | 0.53 | 1.71 | 62 |
| stroke 9 | 50 % → 62 % | 156.5 px | 0.52 | 1.24 | 24 |
| stroke 10 | 43 % → 73 % | 102.9 px | 0.52 | 1.68 | 73 |
| stroke 11 | 52 % → 72 % | 221.9 px | 0.52 | 1.39 | 18 |
| stroke 12 | 54 % → 70 % | 84.9 px | 0.52 | 1.28 | 109 |
| stroke 13 | 42 % → 53 % | 116.2 px | 0.53 | 1.27 | 32 |
| stroke 14 | 45 % → 68 % | 131.6 px | 0.53 | 1.52 | 29 |
| stroke 15 | 43 % → 63 % | 101.8 px | 0.52 | 1.47 | 65 |
| stroke 16 | 52 % → 61 % | 220.3 px | 0.52 | 1.19 | 16 |
| stroke 17 | 53 % → 64 % | 82.3 px | 0.52 | 1.19 | 98 |
| stroke 18 | 36 % → 43 % | 98.8 px | 0.53 | 1.20 | 28 |
| stroke 19 | 53 % → 52 % | 122.0 px | 0.52 | 0.99 | 30 |
| stroke 20 | 55 % → 55 % | 127.4 px | 0.52 | 1.00 | 27 |
| stroke 21 | 49 % → 49 % | 80.4 px | 0.52 | 1.00 | 79 |

Numbers say: wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #50 Thick swipes on photo — own sheet
own sheet 600 × 600 · Impasto 1.00 · 40 px · 2.7 s

![Brush Artist · Refs · #50 Thick swipes on photo — own sheet](Brush-Artist-Refs-50-Thick-swipes-on-photo-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 9 % → 21 % | 43.0 px | 0.35 | 2.32 | 34 |
| stroke 2 | 9 % → 16 % | 42.2 px | 0.34 | 1.82 | 24 |
| stroke 3 | 10 % → 11 % | 42.0 px | 0.32 | 1.06 | 47 |
| stroke 4 | 11 % → 18 % | 44.0 px | 0.35 | 1.60 | 32 |
| stroke 5 | 11 % → 10 % | 42.2 px | 0.34 | 0.94 | 46 |
| stroke 6 | 17 % → 21 % | 99.5 px | 0.35 | 1.19 | 24 |
| stroke 7 | 22 % → 26 % | 92.9 px | 0.35 | 1.18 | 40 |
| stroke 8 | 21 % → 20 % | 119.7 px | 0.35 | 0.96 | 40 |
| stroke 9 | 10 % → 11 % | 43.0 px | 0.30 | 1.11 | 42 |
| stroke 10 | 22 % → 22 % | 75.4 px | 0.35 | 0.96 | 40 |
| stroke 11 | 8 % → 8 % | 41.8 px | 0.36 | 0.95 | 32 |
| stroke 12 | 17 % → 16 % | 94.4 px | 0.35 | 0.96 | 19 |

Numbers say: wet paint spreads well beyond the stroke.

## Brush Artist · Ink — dry brush — own sheet
own sheet 600 × 600 · Gouache 1.00 · 30 px · 2.8 s

![Brush Artist · Ink — dry brush — own sheet](Brush-Artist-Ink-dry-brush-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| ear | 8 % → 2 % | 9.7 px | 0.85 | 0.22 | 431 |
| drag0 | 4 % → 6 % | 7.6 px | 0.85 | 1.51 | 108 |
| drag1 | 7 % → 7 % | 15.1 px | 0.85 | 0.89 | 93 |
| drag2 | 10 % → 7 % | 22.1 px | 0.85 | 0.71 | 88 |
| drag3 | 12 % → 7 % | 30.1 px | 0.85 | 0.60 | 62 |

Numbers say: wet paint spreads well beyond the stroke.

## Brush Artist · Watercolour — blue — own sheet
own sheet 600 × 600 · Watercolour 0.93 · Ink 0.07 · 40 px · 9.8 s

![Brush Artist · Watercolour — blue — own sheet](Brush-Artist-Watercolour-blue-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| s0 | 7 % → 24 % | 28.8 px | 0.30 | 3.32 | 40 |
| s1 | 6 % → 33 % | 10.1 px | 0.37 | 6.00 | 34 |
| s2 | 10 % → 19 % | 44.2 px | 0.26 | 1.81 | 31 |
| s3 | 10 % → 18 % | 26.7 px | 0.31 | 1.92 | 42 |
| s4 | 14 % → 30 % | 38.6 px | 0.36 | 2.16 | 54 |
| s5 | 19 % → 29 % | 39.3 px | 0.37 | 1.54 | 63 |
| s6 | 18 % → 22 % | 48.7 px | 0.31 | 1.25 | 57 |
| s7 | 25 % → 36 % | 32.7 px | 0.37 | 1.46 | 39 |
| s8 | 21 % → 25 % | 79.8 px | 0.30 | 1.20 | 48 |

Numbers say: wet paint spreads well beyond the stroke.

## Brush Artist · Charcoal — stick — own sheet
own sheet 600 × 600 · Charcoal 0.78 · Pastel 0.22 · 28 px · 1.1 s

![Brush Artist · Charcoal — stick — own sheet](Brush-Artist-Charcoal-stick-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| finger0 | 12 % → 25 % | 21.2 px | 0.83 | 2.03 | 35 |
| tip0 | 13 % → 21 % | 33.8 px | 0.83 | 1.70 | 8 |
| finger1 | 23 % → 41 % | 40.4 px | 0.83 | 1.77 | 33 |
| tip1 | 21 % → 29 % | 57.3 px | 0.83 | 1.38 | 12 |
| finger2 | 25 % → 37 % | 43.8 px | 0.83 | 1.49 | 33 |
| tip2 | 21 % → 29 % | 55.7 px | 0.83 | 1.40 | 9 |
| finger3 | 24 % → 27 % | 42.7 px | 0.83 | 1.14 | 33 |
| tip3 | 20 % → 20 % | 54.1 px | 0.83 | 1.00 | 11 |
| cig0 | 34 % → 47 % | 75.0 px | 0.83 | 1.39 | 11 |
| cig1 | 36 % → 47 % | 80.5 px | 0.83 | 1.30 | 17 |
| cig2 | 39 % → 47 % | 86.7 px | 0.83 | 1.20 | 16 |
| cig3 | 41 % → 47 % | 91.3 px | 0.83 | 1.14 | 17 |
| cig4 | 44 % → 46 % | 97.5 px | 0.83 | 1.06 | 15 |
| cig5 | 46 % → 46 % | 102.9 px | 0.83 | 1.00 | 14 |

Numbers say: wet paint spreads well beyond the stroke.

## Oil · Henry Ward · HW #02 cream over wet olive — own sheet
own sheet 600 × 600 · Watercolour 0.93 · Ink 0.07 + turpentine 80 % · 96 px · 37.6 s

![Oil · Henry Ward · HW #02 cream over wet olive — own sheet](Oil-Henry-Ward-HW-02-cream-over-wet-olive-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 44 % → 44 % | 86.0 px | 0.59 | 0.98 | 1507 |
| stroke 2 | 56 % → 50 % | 144.3 px | 0.56 | 0.89 | 1854 |
| stroke 3 | 65 % → 50 % | 205.6 px | 0.57 | 0.76 | 1941 |
| stroke 4 | 69 % → 50 % | 241.1 px | 0.58 | 0.73 | 2557 |
| stroke 5 | 69 % → 57 % | 240.7 px | 0.58 | 0.82 | 2153 |
| stroke 6 | 68 % → 46 % | 240.2 px | 0.56 | 0.67 | 2101 |
| stroke 7 | 77 % → 35 % | 239.6 px | 0.58 | 0.46 | 1964 |
| stroke 8 | 94 % → 29 % | 239.8 px | 0.60 | 0.31 | 2085 |
| stroke 9 | 100 % → 27 % | 192.3 px | 0.59 | 0.27 | 1773 |
| stroke 10 | 6 % → 49 % | 43.6 px | 0.57 | 8.17 | 286 |
| stroke 11 | 12 % → 54 % | 77.4 px | 0.58 | 4.68 | 320 |
| stroke 12 | 10 % → 39 % | 88.7 px | 0.57 | 4.07 | 155 |
| stroke 13 | 28 % → 50 % | 121.1 px | 0.56 | 1.82 | 335 |
| stroke 14 | 30 % → 50 % | 173.8 px | 0.57 | 1.68 | 376 |
| stroke 15 | 30 % → 48 % | 203.1 px | 0.57 | 1.61 | 271 |
| stroke 16 | 35 % → 47 % | 179.3 px | 0.58 | 1.34 | 545 |
| stroke 17 | 39 % → 55 % | 261.0 px | 0.58 | 1.39 | 363 |
| stroke 18 | 43 % → 55 % | 303.5 px | 0.58 | 1.28 | 523 |
| stroke 19 | 40 % → 50 % | 348.7 px | 0.56 | 1.22 | 239 |
| stroke 20 | 35 % → 40 % | 289.4 px | 0.57 | 1.14 | 281 |
| stroke 21 | 39 % → 37 % | 196.3 px | 0.57 | 0.95 | 490 |
| stroke 22 | 53 % → 50 % | 462.2 px | 0.57 | 0.94 | 265 |
| stroke 23 | 50 % → 47 % | 340.3 px | 0.58 | 0.94 | 583 |
| stroke 24 | 57 % → 54 % | 374.9 px | 0.58 | 0.95 | 713 |
| stroke 25 | 61 % → 58 % | 538.5 px | 0.57 | 0.96 | 306 |
| stroke 26 | 42 % → 39 % | 335.5 px | 0.57 | 0.93 | 367 |

Numbers say: wet paint spreads well beyond the stroke.

## Oil · Henry Ward · HW #04 grey arcs over ochre — own sheet
own sheet 600 × 600 · Gouache 1.00 + turpentine 35 % · 84 px · 44.3 s

![Oil · Henry Ward · HW #04 grey arcs over ochre — own sheet](Oil-Henry-Ward-HW-04-grey-arcs-over-ochre-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 47 % → 54 % | 79.1 px | 0.39 | 1.15 | 1479 |
| stroke 2 | 63 % → 63 % | 149.2 px | 0.39 | 1.01 | 1873 |
| stroke 3 | 70 % → 56 % | 209.4 px | 0.39 | 0.80 | 2007 |
| stroke 4 | 71 % → 62 % | 217.9 px | 0.33 | 0.88 | 2611 |
| stroke 5 | 71 % → 61 % | 218.3 px | 0.27 | 0.86 | 2156 |
| stroke 6 | 71 % → 49 % | 217.0 px | 0.20 | 0.69 | 1996 |
| stroke 7 | 75 % → 37 % | 218.9 px | 0.08 | 0.50 | 1919 |
| stroke 8 | 94 % → 39 % | 218.4 px | 0.02 | 0.42 | 2052 |
| stroke 9 | 100 % → 36 % | 167.6 px | 0.02 | 0.36 | 1651 |
| stroke 10 | 11 % → 64 % | 62.2 px | 0.28 | 5.98 | 361 |
| stroke 11 | 15 % → 56 % | 78.3 px | 0.29 | 3.68 | 489 |
| stroke 12 | 18 % → 57 % | 119.7 px | 0.30 | 3.10 | 288 |
| stroke 13 | 27 % → 60 % | 164.0 px | 0.35 | 2.28 | 330 |
| stroke 14 | 26 % → 64 % | 216.3 px | 0.29 | 2.48 | 329 |
| stroke 15 | 32 % → 58 % | 243.9 px | 0.36 | 1.84 | 288 |
| stroke 16 | 28 % → 55 % | 137.0 px | 0.31 | 1.97 | 645 |
| stroke 17 | 45 % → 58 % | 191.1 px | 0.39 | 1.29 | 494 |
| stroke 18 | 39 % → 55 % | 183.6 px | 0.34 | 1.41 | 755 |
| stroke 19 | 48 % → 56 % | 219.7 px | 0.38 | 1.16 | 626 |
| stroke 20 | 44 % → 58 % | 336.6 px | 0.32 | 1.33 | 510 |
| stroke 21 | 45 % → 60 % | 292.3 px | 0.29 | 1.33 | 1003 |
| stroke 22 | 50 % → 65 % | 340.3 px | 0.28 | 1.30 | 621 |
| stroke 23 | 52 % → 57 % | 255.3 px | 0.33 | 1.10 | 675 |
| stroke 24 | 51 % → 57 % | 264.0 px | 0.32 | 1.10 | 1027 |
| stroke 25 | 54 % → 55 % | 316.4 px | 0.34 | 1.02 | 923 |
| stroke 26 | 50 % → 56 % | 264.1 px | 0.31 | 1.10 | 1148 |
| stroke 27 | 36 % → 49 % | 201.0 px | 0.20 | 1.39 | 385 |
| stroke 28 | 34 % → 44 % | 232.6 px | 0.13 | 1.27 | 316 |
| stroke 29 | 34 % → 39 % | 207.7 px | 0.10 | 1.15 | 541 |
| stroke 30 | 40 % → 39 % | 183.7 px | 0.02 | 0.98 | 342 |

Numbers say: wet paint spreads well beyond the stroke.

## Oil · Henry Ward · HW #09 white arches over wet blue-grey — own sheet
own sheet 600 × 600 · Gouache 1.00 + turpentine 35 % · 84 px · 47.6 s

![Oil · Henry Ward · HW #09 white arches over wet blue-grey — own sheet](Oil-Henry-Ward-HW-09-white-arches-over-wet-blue-grey-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 47 % → 18 % | 81.2 px | 0.15 | 0.38 | 1469 |
| stroke 2 | 62 % → 30 % | 144.0 px | 0.15 | 0.49 | 1895 |
| stroke 3 | 70 % → 38 % | 206.7 px | 0.15 | 0.54 | 1957 |
| stroke 4 | 71 % → 50 % | 217.4 px | 0.15 | 0.70 | 2470 |
| stroke 5 | 71 % → 62 % | 219.0 px | 0.15 | 0.88 | 2130 |
| stroke 6 | 71 % → 63 % | 217.3 px | 0.15 | 0.89 | 2023 |
| stroke 7 | 75 % → 58 % | 218.8 px | 0.14 | 0.77 | 1969 |
| stroke 8 | 93 % → 56 % | 218.7 px | 0.14 | 0.60 | 2155 |
| stroke 9 | 100 % → 52 % | 167.6 px | 0.13 | 0.52 | 1677 |
| stroke 10 | 8 % → 46 % | 21.0 px | 0.15 | 6.12 | 735 |
| stroke 11 | 15 % → 53 % | 34.6 px | 0.15 | 3.61 | 711 |
| stroke 12 | 16 % → 55 % | 50.1 px | 0.15 | 3.39 | 634 |
| stroke 13 | 18 % → 60 % | 60.1 px | 0.15 | 3.37 | 401 |
| stroke 14 | 20 % → 59 % | 29.3 px | 0.14 | 2.90 | 733 |
| stroke 15 | 26 % → 55 % | 114.0 px | 0.15 | 2.15 | 797 |
| stroke 16 | 36 % → 65 % | 187.9 px | 0.15 | 1.78 | 720 |
| stroke 17 | 36 % → 49 % | 130.9 px | 0.16 | 1.39 | 819 |
| stroke 18 | 43 % → 55 % | 172.7 px | 0.15 | 1.26 | 1487 |
| stroke 19 | 48 % → 55 % | 197.9 px | 0.16 | 1.14 | 802 |
| stroke 20 | 51 % → 59 % | 208.7 px | 0.15 | 1.16 | 1222 |
| stroke 21 | 52 % → 55 % | 194.9 px | 0.14 | 1.04 | 1308 |
| stroke 22 | 61 % → 65 % | 362.9 px | 0.15 | 1.06 | 704 |
| stroke 23 | 58 % → 58 % | 268.9 px | 0.15 | 1.00 | 999 |
| stroke 24 | 60 % → 62 % | 327.8 px | 0.15 | 1.03 | 818 |
| stroke 25 | 69 % → 70 % | 480.3 px | 0.14 | 1.03 | 377 |
| stroke 26 | 58 % → 58 % | 288.3 px | 0.14 | 1.01 | 1054 |
| stroke 27 | 58 % → 59 % | 381.8 px | 0.14 | 1.02 | 488 |
| stroke 28 | 62 % → 56 % | 242.8 px | 0.14 | 0.90 | 950 |

Numbers say: wet paint spreads well beyond the stroke.

## Oil · Henry Ward · HW #03 navy contours over wet band — own sheet
own sheet 600 × 600 · Gouache 1.00 + turpentine 35 % · 84 px · 26.7 s

![Oil · Henry Ward · HW #03 navy contours over wet band — own sheet](Oil-Henry-Ward-HW-03-navy-contours-over-wet-band-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 50 % → 37 % | 87.6 px | 0.65 | 0.73 | 1234 |
| stroke 2 | 61 % → 41 % | 145.4 px | 0.61 | 0.68 | 1644 |
| stroke 3 | 69 % → 43 % | 202.2 px | 0.58 | 0.62 | 1820 |
| stroke 4 | 71 % → 48 % | 218.6 px | 0.57 | 0.68 | 2135 |
| stroke 5 | 71 % → 51 % | 217.2 px | 0.58 | 0.72 | 1838 |
| stroke 6 | 71 % → 39 % | 222.3 px | 0.56 | 0.54 | 1746 |
| stroke 7 | 74 % → 29 % | 218.0 px | 0.56 | 0.39 | 1624 |
| stroke 8 | 95 % → 23 % | 218.1 px | 0.62 | 0.24 | 1830 |
| stroke 9 | 100 % → 17 % | 170.3 px | 0.66 | 0.17 | 1360 |
| stroke 10 | 7 % → 45 % | 47.5 px | 0.57 | 6.55 | 254 |
| stroke 11 | 12 % → 52 % | 114.2 px | 0.58 | 4.26 | 171 |
| stroke 12 | 20 % → 52 % | 186.7 px | 0.56 | 2.61 | 150 |
| stroke 13 | 18 % → 41 % | 158.3 px | 0.56 | 2.20 | 208 |
| stroke 14 | 18 % → 48 % | 157.3 px | 0.63 | 2.61 | 114 |
| stroke 15 | 27 % → 47 % | 217.1 px | 0.60 | 1.77 | 143 |
| stroke 16 | 37 % → 37 % | 109.6 px | 0.57 | 0.99 | 700 |
| stroke 17 | 42 % → 38 % | 151.9 px | 0.58 | 0.91 | 626 |

Numbers say: wet paint spreads well beyond the stroke.

## Oil · Henry Ward · HW #01 peach cloud and legs over teal — own sheet
own sheet 600 × 600 · Gouache 1.00 + turpentine 35 % · 84 px · 37.6 s

![Oil · Henry Ward · HW #01 peach cloud and legs over teal — own sheet](Oil-Henry-Ward-HW-01-peach-cloud-and-legs-over-teal-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 50 % → 45 % | 88.9 px | 0.52 | 0.89 | 1549 |
| stroke 2 | 62 % → 53 % | 146.9 px | 0.54 | 0.86 | 1871 |
| stroke 3 | 69 % → 56 % | 203.4 px | 0.54 | 0.81 | 1949 |
| stroke 4 | 72 % → 61 % | 220.2 px | 0.54 | 0.86 | 2493 |
| stroke 5 | 70 % → 52 % | 218.3 px | 0.53 | 0.74 | 2119 |
| stroke 6 | 71 % → 50 % | 218.2 px | 0.46 | 0.70 | 1965 |
| stroke 7 | 77 % → 45 % | 222.3 px | 0.33 | 0.59 | 1981 |
| stroke 8 | 95 % → 40 % | 219.1 px | 0.24 | 0.42 | 2196 |
| stroke 9 | 100 % → 37 % | 170.3 px | 0.11 | 0.37 | 1632 |
| stroke 10 | 13 % → 52 % | 48.3 px | 0.54 | 4.09 | 352 |
| stroke 11 | 21 % → 55 % | 94.4 px | 0.54 | 2.57 | 346 |
| stroke 12 | 22 % → 57 % | 116.2 px | 0.54 | 2.56 | 308 |
| stroke 13 | 30 % → 61 % | 155.2 px | 0.54 | 2.01 | 348 |
| stroke 14 | 46 % → 52 % | 175.2 px | 0.54 | 1.13 | 489 |
| stroke 15 | 38 % → 56 % | 188.0 px | 0.54 | 1.46 | 307 |
| stroke 16 | 38 % → 60 % | 201.9 px | 0.54 | 1.58 | 452 |
| stroke 17 | 33 % → 52 % | 178.8 px | 0.43 | 1.59 | 307 |
| stroke 18 | 38 % → 55 % | 323.6 px | 0.43 | 1.44 | 328 |
| stroke 19 | 49 % → 70 % | 405.9 px | 0.43 | 1.41 | 337 |
| stroke 20 | 49 % → 69 % | 374.2 px | 0.43 | 1.43 | 400 |
| stroke 21 | 44 % → 57 % | 362.1 px | 0.44 | 1.29 | 339 |
| stroke 22 | 42 % → 50 % | 293.1 px | 0.44 | 1.18 | 287 |
| stroke 23 | 41 % → 46 % | 144.4 px | 0.24 | 1.14 | 284 |
| stroke 24 | 48 % → 44 % | 180.0 px | 0.23 | 0.90 | 494 |

Numbers say: wet paint spreads well beyond the stroke.

## Oil · Henry Ward · HW #05 rust, pink, green-black — own sheet
own sheet 600 × 600 · Gouache 1.00 + turpentine 35 % · 84 px · 36.5 s

![Oil · Henry Ward · HW #05 rust, pink, green-black — own sheet](Oil-Henry-Ward-HW-05-rust-pink-green-black-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 49 % → 53 % | 83.9 px | 0.58 | 1.08 | 1188 |
| stroke 2 | 63 % → 60 % | 148.0 px | 0.49 | 0.96 | 1643 |
| stroke 3 | 69 % → 60 % | 207.2 px | 0.40 | 0.88 | 1805 |
| stroke 4 | 71 % → 68 % | 218.5 px | 0.34 | 0.96 | 2334 |
| stroke 5 | 71 % → 67 % | 220.5 px | 0.35 | 0.94 | 1867 |
| stroke 6 | 70 % → 63 % | 216.1 px | 0.35 | 0.90 | 1799 |
| stroke 7 | 74 % → 53 % | 217.7 px | 0.39 | 0.72 | 1700 |
| stroke 8 | 93 % → 50 % | 217.2 px | 0.49 | 0.53 | 1816 |
| stroke 9 | 100 % → 42 % | 167.6 px | 0.69 | 0.42 | 1444 |
| stroke 10 | 15 % → 57 % | 53.7 px | 0.56 | 3.76 | 314 |
| stroke 11 | 22 % → 62 % | 94.0 px | 0.44 | 2.78 | 340 |
| stroke 12 | 26 % → 62 % | 137.0 px | 0.40 | 2.37 | 367 |
| stroke 13 | 31 % → 65 % | 163.8 px | 0.36 | 2.10 | 386 |
| stroke 14 | 48 % → 59 % | 216.8 px | 0.50 | 1.23 | 232 |
| stroke 15 | 42 % → 63 % | 211.5 px | 0.42 | 1.49 | 274 |
| stroke 16 | 38 % → 65 % | 254.1 px | 0.36 | 1.73 | 203 |
| stroke 17 | 43 % → 68 % | 221.3 px | 0.34 | 1.58 | 681 |
| stroke 18 | 45 % → 68 % | 242.7 px | 0.35 | 1.52 | 717 |
| stroke 19 | 43 % → 63 % | 217.8 px | 0.36 | 1.45 | 491 |
| stroke 20 | 48 % → 62 % | 354.6 px | 0.39 | 1.30 | 145 |
| stroke 21 | 50 % → 61 % | 363.4 px | 0.40 | 1.23 | 287 |
| stroke 22 | 51 % → 63 % | 424.5 px | 0.41 | 1.24 | 201 |
| stroke 23 | 46 % → 56 % | 264.4 px | 0.35 | 1.21 | 498 |
| stroke 24 | 47 % → 49 % | 223.8 px | 0.46 | 1.04 | 383 |
| stroke 25 | 52 % → 49 % | 184.5 px | 0.56 | 0.93 | 381 |

Numbers say: wet paint spreads well beyond the stroke.

## Oil · Henry Ward · HW #07 blue L and zigzag on lilac — own sheet
own sheet 600 × 600 · Gouache 1.00 + turpentine 20 % · 90 px · 40.3 s

![Oil · Henry Ward · HW #07 blue L and zigzag on lilac — own sheet](Oil-Henry-Ward-HW-07-blue-L-and-zigzag-on-lilac-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 45 % → 29 % | 81.5 px | 0.28 | 0.64 | 1224 |
| stroke 2 | 58 % → 39 % | 140.1 px | 0.36 | 0.67 | 1655 |
| stroke 3 | 67 % → 67 % | 204.7 px | 0.37 | 1.00 | 2097 |
| stroke 4 | 70 % → 51 % | 231.5 px | 0.35 | 0.72 | 1901 |
| stroke 5 | 69 % → 60 % | 227.8 px | 0.33 | 0.87 | 1843 |
| stroke 6 | 69 % → 61 % | 227.3 px | 0.31 | 0.90 | 1739 |
| stroke 7 | 75 % → 56 % | 228.0 px | 0.26 | 0.75 | 1666 |
| stroke 8 | 96 % → 50 % | 229.1 px | 0.19 | 0.52 | 1878 |
| stroke 9 | 100 % → 54 % | 182.6 px | 0.16 | 0.54 | 1475 |
| stroke 10 | 12 % → 33 % | 33.5 px | 0.30 | 2.69 | 397 |
| stroke 11 | 22 % → 41 % | 73.6 px | 0.38 | 1.90 | 493 |
| stroke 12 | 21 % → 42 % | 75.1 px | 0.38 | 2.02 | 325 |
| stroke 13 | 23 % → 46 % | 87.9 px | 0.37 | 2.05 | 379 |
| stroke 14 | 28 % → 49 % | 127.2 px | 0.35 | 1.75 | 551 |
| stroke 15 | 30 % → 55 % | 150.9 px | 0.33 | 1.81 | 367 |
| stroke 16 | 36 % → 61 % | 160.5 px | 0.33 | 1.70 | 572 |
| stroke 17 | 34 % → 62 % | 168.7 px | 0.31 | 1.85 | 528 |
| stroke 18 | 43 % → 61 % | 187.9 px | 0.29 | 1.42 | 629 |
| stroke 19 | 46 % → 56 % | 189.0 px | 0.26 | 1.20 | 503 |
| stroke 20 | 52 % → 55 % | 202.0 px | 0.22 | 1.04 | 555 |
| stroke 21 | 62 % → 51 % | 203.4 px | 0.19 | 0.82 | 1027 |
| stroke 22 | 71 % → 50 % | 219.7 px | 0.17 | 0.71 | 544 |
| stroke 23 | 61 % → 53 % | 339.8 px | 0.29 | 0.86 | 304 |
| stroke 24 | 73 % → 55 % | 481.2 px | 0.23 | 0.76 | 368 |
| stroke 25 | 67 % → 52 % | 251.0 px | 0.33 | 0.78 | 843 |
| stroke 26 | 67 % → 60 % | 725.7 px | 0.29 | 0.90 | 256 |
| stroke 27 | 75 % → 63 % | 714.6 px | 0.28 | 0.84 | 206 |
| stroke 28 | 75 % → 62 % | 562.8 px | 0.28 | 0.83 | 558 |
| stroke 29 | 74 % → 62 % | 653.2 px | 0.28 | 0.83 | 204 |
| stroke 30 | 78 % → 64 % | 607.6 px | 0.28 | 0.82 | 280 |
| stroke 31 | 78 % → 64 % | 1158.0 px | 0.26 | 0.82 | 159 |

Numbers say: wet paint spreads well beyond the stroke.

## Oil · Henry Ward · HW #08 crown and dark oval — own sheet
own sheet 600 × 600 · Gouache 1.00 + turpentine 35 % · 84 px · 27.8 s

![Oil · Henry Ward · HW #08 crown and dark oval — own sheet](Oil-Henry-Ward-HW-08-crown-and-dark-oval-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 50 % → 0 % | 88.5 px | 0.00 | 0.00 | 1500 |
| stroke 2 | 61 % → 0 % | 142.2 px | 0.00 | 0.00 | 1642 |
| stroke 3 | 70 % → 3 % | 206.2 px | 0.09 | 0.04 | 1829 |
| stroke 4 | 72 % → 7 % | 223.5 px | 0.08 | 0.10 | 1986 |
| stroke 5 | 71 % → 13 % | 220.0 px | 0.08 | 0.18 | 1816 |
| stroke 6 | 70 % → 13 % | 219.6 px | 0.08 | 0.18 | 1807 |
| stroke 7 | 74 % → 13 % | 217.8 px | 0.08 | 0.18 | 1688 |
| stroke 8 | 94 % → 13 % | 217.3 px | 0.08 | 0.14 | 1895 |
| stroke 9 | 100 % → 9 % | 166.8 px | 0.09 | 0.09 | 1388 |
| stroke 10 | 19 % → 0 % | 78.0 px | 0.00 | 0.00 | 475 |
| stroke 11 | 31 % → 1 % | 159.4 px | 0.08 | 0.03 | 523 |
| stroke 12 | 35 % → 3 % | 220.7 px | 0.09 | 0.09 | 411 |
| stroke 13 | 33 % → 9 % | 99.9 px | 0.08 | 0.27 | 720 |
| stroke 14 | 41 % → 12 % | 298.0 px | 0.08 | 0.30 | 626 |
| stroke 15 | 42 % → 12 % | 346.6 px | 0.08 | 0.29 | 424 |
| stroke 16 | 41 % → 12 % | 334.3 px | 0.08 | 0.30 | 283 |
| stroke 17 | 44 % → 14 % | 281.7 px | 0.08 | 0.31 | 350 |
| stroke 18 | 11 % → 13 % | 97.1 px | 0.08 | 1.19 | 532 |
| stroke 19 | 22 % → 13 % | 191.6 px | 0.08 | 0.57 | 513 |
| stroke 20 | 28 % → 13 % | 212.5 px | 0.08 | 0.47 | 633 |

## Oil · Henry Ward · HW #10 green block over maroon — own sheet
own sheet 600 × 600 · Gouache 1.00 + turpentine 35 % · 84 px · 37.0 s

![Oil · Henry Ward · HW #10 green block over maroon — own sheet](Oil-Henry-Ward-HW-10-green-block-over-maroon-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 50 % → 39 % | 86.8 px | 0.17 | 0.79 | 1291 |
| stroke 2 | 61 % → 44 % | 141.4 px | 0.30 | 0.72 | 1738 |
| stroke 3 | 70 % → 48 % | 209.0 px | 0.41 | 0.69 | 1816 |
| stroke 4 | 71 % → 55 % | 218.3 px | 0.49 | 0.77 | 2001 |
| stroke 5 | 70 % → 57 % | 215.7 px | 0.58 | 0.81 | 1876 |
| stroke 6 | 71 % → 54 % | 218.8 px | 0.62 | 0.76 | 1770 |
| stroke 7 | 75 % → 45 % | 219.0 px | 0.63 | 0.59 | 1724 |
| stroke 8 | 93 % → 40 % | 217.8 px | 0.61 | 0.43 | 1951 |
| stroke 9 | 100 % → 30 % | 172.0 px | 0.54 | 0.30 | 1636 |
| stroke 10 | 14 % → 44 % | 78.5 px | 0.22 | 3.20 | 296 |
| stroke 11 | 24 % → 46 % | 155.7 px | 0.34 | 1.95 | 557 |
| stroke 12 | 26 % → 53 % | 227.1 px | 0.46 | 2.01 | 512 |
| stroke 13 | 39 % → 47 % | 260.6 px | 0.31 | 1.19 | 227 |
| stroke 14 | 34 % → 51 % | 275.3 px | 0.38 | 1.50 | 278 |
| stroke 15 | 29 % → 53 % | 259.7 px | 0.44 | 1.85 | 262 |
| stroke 16 | 29 % → 53 % | 208.5 px | 0.47 | 1.81 | 1022 |
| stroke 17 | 33 % → 56 % | 221.2 px | 0.54 | 1.70 | 719 |
| stroke 18 | 36 % → 56 % | 248.9 px | 0.60 | 1.58 | 646 |
| stroke 19 | 38 % → 53 % | 272.6 px | 0.62 | 1.41 | 685 |
| stroke 20 | 37 % → 49 % | 265.3 px | 0.63 | 1.33 | 554 |
| stroke 21 | 42 % → 46 % | 156.1 px | 0.50 | 1.08 | 1211 |
| stroke 22 | 41 % → 46 % | 332.1 px | 0.63 | 1.11 | 489 |
| stroke 23 | 45 % → 43 % | 280.7 px | 0.62 | 0.94 | 655 |
| stroke 24 | 50 % → 36 % | 278.5 px | 0.58 | 0.72 | 427 |

Numbers say: wet paint spreads well beyond the stroke.

## Oil · Henry Ward · HW #11 cream mass and purple balls — own sheet
own sheet 600 × 600 · Gouache 1.00 + turpentine 35 % · 84 px · 39.0 s

![Oil · Henry Ward · HW #11 cream mass and purple balls — own sheet](Oil-Henry-Ward-HW-11-cream-mass-and-purple-balls-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 49 % → 41 % | 83.5 px | 0.10 | 0.84 | 1504 |
| stroke 2 | 62 % → 44 % | 147.7 px | 0.11 | 0.71 | 1917 |
| stroke 3 | 70 % → 46 % | 210.2 px | 0.12 | 0.66 | 1968 |
| stroke 4 | 71 % → 49 % | 221.0 px | 0.12 | 0.69 | 2260 |
| stroke 5 | 71 % → 48 % | 217.6 px | 0.20 | 0.68 | 2070 |
| stroke 6 | 70 % → 48 % | 216.5 px | 0.29 | 0.69 | 2033 |
| stroke 7 | 76 % → 40 % | 221.8 px | 0.35 | 0.52 | 1948 |
| stroke 8 | 94 % → 36 % | 219.3 px | 0.43 | 0.39 | 2601 |
| stroke 9 | 100 % → 37 % | 171.2 px | 0.54 | 0.37 | 2341 |
| stroke 10 | 14 % → 44 % | 59.6 px | 0.11 | 3.12 | 596 |
| stroke 11 | 20 % → 44 % | 104.4 px | 0.11 | 2.25 | 345 |
| stroke 12 | 24 % → 46 % | 133.1 px | 0.12 | 1.95 | 542 |
| stroke 13 | 27 % → 48 % | 172.1 px | 0.11 | 1.76 | 468 |
| stroke 14 | 30 % → 48 % | 199.1 px | 0.14 | 1.63 | 523 |
| stroke 15 | 30 % → 48 % | 182.9 px | 0.18 | 1.60 | 464 |
| stroke 16 | 31 % → 50 % | 206.4 px | 0.26 | 1.62 | 393 |
| stroke 17 | 29 % → 48 % | 184.9 px | 0.29 | 1.66 | 411 |
| stroke 18 | 44 % → 44 % | 225.6 px | 0.11 | 1.00 | 516 |
| stroke 19 | 46 % → 45 % | 268.8 px | 0.11 | 0.99 | 487 |
| stroke 20 | 49 % → 47 % | 340.5 px | 0.11 | 0.96 | 527 |
| stroke 21 | 52 % → 49 % | 408.4 px | 0.12 | 0.95 | 534 |
| stroke 22 | 48 % → 48 % | 336.3 px | 0.15 | 1.00 | 503 |
| stroke 23 | 38 % → 49 % | 254.7 px | 0.24 | 1.29 | 600 |
| stroke 24 | 34 % → 49 % | 239.4 px | 0.27 | 1.45 | 613 |
| stroke 25 | 41 % → 48 % | 115.7 px | 0.34 | 1.17 | 791 |
| stroke 26 | 53 % → 54 % | 157.2 px | 0.34 | 1.02 | 796 |
| stroke 27 | 51 % → 47 % | 132.4 px | 0.33 | 0.93 | 471 |

Numbers say: wet paint spreads well beyond the stroke.

## Oil · Henry Ward · HW #13 blue scrub under red — own sheet
own sheet 600 × 600 · Gouache 1.00 + turpentine 35 % · 84 px · 34.2 s

![Oil · Henry Ward · HW #13 blue scrub under red — own sheet](Oil-Henry-Ward-HW-13-blue-scrub-under-red-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 49 % → 10 % | 83.9 px | 0.06 | 0.20 | 1407 |
| stroke 2 | 61 % → 23 % | 142.5 px | 0.06 | 0.37 | 2733 |
| stroke 3 | 69 % → 30 % | 204.0 px | 0.06 | 0.43 | 2692 |
| stroke 4 | 71 % → 40 % | 220.1 px | 0.06 | 0.56 | 3320 |
| stroke 5 | 70 % → 55 % | 216.6 px | 0.06 | 0.79 | 3320 |
| stroke 6 | 71 % → 64 % | 220.3 px | 0.06 | 0.90 | 1958 |
| stroke 7 | 75 % → 64 % | 216.2 px | 0.06 | 0.86 | 1685 |
| stroke 8 | 95 % → 66 % | 222.8 px | 0.06 | 0.70 | 1922 |
| stroke 9 | 100 % → 70 % | 165.9 px | 0.06 | 0.70 | 1340 |
| stroke 10 | 15 % → 12 % | 55.6 px | 0.07 | 0.81 | 310 |
| stroke 11 | 18 % → 28 % | 108.8 px | 0.05 | 1.54 | 244 |
| stroke 12 | 19 % → 30 % | 117.2 px | 0.05 | 1.55 | 259 |
| stroke 13 | 9 % → 33 % | 43.7 px | 0.06 | 3.67 | 325 |
| stroke 14 | 19 % → 45 % | 99.3 px | 0.05 | 2.39 | 453 |
| stroke 15 | 27 % → 54 % | 140.4 px | 0.06 | 2.04 | 310 |
| stroke 16 | 34 % → 61 % | 175.7 px | 0.06 | 1.78 | 331 |
| stroke 17 | 37 % → 66 % | 196.9 px | 0.06 | 1.75 | 308 |
| stroke 18 | 39 % → 64 % | 176.2 px | 0.06 | 1.65 | 379 |
| stroke 19 | 44 % → 64 % | 182.0 px | 0.06 | 1.46 | 424 |
| stroke 20 | 55 % → 66 % | 204.4 px | 0.06 | 1.21 | 364 |
| stroke 21 | 68 % → 71 % | 206.1 px | 0.05 | 1.04 | 309 |
| stroke 22 | 42 % → 39 % | 225.8 px | 0.06 | 0.93 | 343 |
| stroke 23 | 55 % → 51 % | 279.9 px | 0.06 | 0.94 | 400 |
| stroke 24 | 59 % → 56 % | 339.8 px | 0.06 | 0.94 | 301 |
| stroke 25 | 66 % → 63 % | 324.7 px | 0.06 | 0.96 | 281 |
| stroke 26 | 68 % → 66 % | 351.4 px | 0.06 | 0.96 | 349 |
| stroke 27 | 67 % → 64 % | 322.4 px | 0.06 | 0.97 | 274 |
| stroke 28 | 70 % → 66 % | 288.6 px | 0.06 | 0.95 | 324 |
| stroke 29 | 72 % → 67 % | 281.7 px | 0.06 | 0.93 | 296 |

Numbers say: wet paint spreads well beyond the stroke.

## Oil · Henry Ward · HW #14 olive totem on dark — own sheet
own sheet 600 × 600 · Gouache 1.00 + turpentine 35 % · 84 px · 31.3 s

![Oil · Henry Ward · HW #14 olive totem on dark — own sheet](Oil-Henry-Ward-HW-14-olive-totem-on-dark-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 47 % → 42 % | 78.9 px | 0.38 | 0.89 | 2246 |
| stroke 2 | 62 % → 50 % | 146.1 px | 0.40 | 0.80 | 3555 |
| stroke 3 | 70 % → 48 % | 208.2 px | 0.41 | 0.68 | 2404 |
| stroke 4 | 71 % → 55 % | 219.4 px | 0.41 | 0.77 | 2286 |
| stroke 5 | 71 % → 60 % | 217.3 px | 0.40 | 0.85 | 2182 |
| stroke 6 | 71 % → 56 % | 216.7 px | 0.41 | 0.80 | 2040 |
| stroke 7 | 74 % → 45 % | 219.2 px | 0.40 | 0.62 | 1821 |
| stroke 8 | 94 % → 46 % | 217.9 px | 0.39 | 0.49 | 1926 |
| stroke 9 | 100 % → 42 % | 172.0 px | 0.39 | 0.42 | 1482 |
| stroke 10 | 22 % → 69 % | 90.9 px | 0.40 | 3.21 | 406 |
| stroke 11 | 28 % → 72 % | 119.1 px | 0.40 | 2.58 | 369 |
| stroke 12 | 44 % → 63 % | 183.0 px | 0.40 | 1.42 | 347 |
| stroke 13 | 39 % → 48 % | 189.5 px | 0.41 | 1.25 | 331 |
| stroke 14 | 46 % → 52 % | 263.5 px | 0.40 | 1.14 | 379 |
| stroke 15 | 50 % → 57 % | 270.2 px | 0.40 | 1.15 | 377 |
| stroke 16 | 38 % → 49 % | 211.6 px | 0.40 | 1.28 | 282 |
| stroke 17 | 36 % → 44 % | 183.0 px | 0.39 | 1.23 | 221 |
| stroke 18 | 43 % → 46 % | 202.6 px | 0.39 | 1.06 | 232 |
| stroke 19 | 53 % → 50 % | 286.6 px | 0.41 | 0.94 | 218 |
| stroke 20 | 51 % → 51 % | 316.0 px | 0.41 | 0.99 | 235 |
| stroke 21 | 55 % → 55 % | 361.8 px | 0.41 | 0.99 | 262 |
| stroke 22 | 59 % → 59 % | 398.7 px | 0.40 | 0.99 | 197 |
| stroke 23 | 62 % → 60 % | 403.3 px | 0.40 | 0.96 | 201 |
| stroke 24 | 58 % → 55 % | 398.9 px | 0.41 | 0.95 | 161 |
| stroke 25 | 53 % → 51 % | 348.1 px | 0.40 | 0.95 | 171 |
| stroke 26 | 48 % → 44 % | 297.3 px | 0.40 | 0.92 | 226 |
| stroke 27 | 49 % → 44 % | 239.3 px | 0.39 | 0.91 | 221 |

Numbers say: wet paint spreads well beyond the stroke.

## Watercolour · #16 Shrigley strokes — own sheet
own sheet 600 × 600 · Watercolour 1.00 + water 50 % · 40 px · 11.9 s

![Watercolour · #16 Shrigley strokes — own sheet](Watercolour-16-Shrigley-strokes-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| s0 | 8 % → 28 % | 29.8 px | 0.17 | 3.69 | 109 |
| s1 | 6 % → 38 % | 10.5 px | 0.28 | 6.63 | 168 |
| s2 | 11 % → 21 % | 46.6 px | 0.13 | 1.97 | 76 |
| s3 | 10 % → 22 % | 28.3 px | 0.23 | 2.23 | 141 |
| s4 | 15 % → 34 % | 41.2 px | 0.27 | 2.31 | 166 |
| s5 | 20 % → 32 % | 42.0 px | 0.26 | 1.59 | 72 |
| s6 | 19 % → 26 % | 52.6 px | 0.19 | 1.37 | 79 |
| s7 | 27 % → 42 % | 36.2 px | 0.29 | 1.55 | 75 |
| s8 | 22 % → 28 % | 87.1 px | 0.20 | 1.27 | 83 |

Numbers say: wet paint spreads well beyond the stroke.

## Watercolour · #29 Shrigley asterisk — own sheet
own sheet 600 × 600 · Watercolour 1.00 + water 50 % · 70 px · 15.2 s

![Watercolour · #29 Shrigley asterisk — own sheet](Watercolour-29-Shrigley-asterisk-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 28 % → 63 % | 98.2 px | 0.65 | 2.25 | 641 |
| stroke 2 | 24 % → 24 % | 170.9 px | 0.65 | 1.00 | 682 |
| stroke 3 | 50 % → 63 % | 179.7 px | 0.66 | 1.24 | 675 |
| stroke 4 | 42 % → 42 % | 300.0 px | 0.65 | 1.00 | 517 |

Numbers say: wet paint spreads well beyond the stroke.

## Watercolour · #33 Red band, pink flames — own sheet
own sheet 600 × 600 · Watercolour 1.00 + water 60 % · 90 px · 17.5 s

![Watercolour · #33 Red band, pink flames — own sheet](Watercolour-33-Red-band-pink-flames-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 25 % → 60 % | 101.7 px | 0.32 | 2.42 | 1303 |
| stroke 2 | 26 % → 53 % | 163.0 px | 0.30 | 2.07 | 96 |
| stroke 3 | 29 % → 51 % | 226.9 px | 0.31 | 1.75 | 102 |
| stroke 4 | 33 % → 55 % | 271.5 px | 0.29 | 1.68 | 110 |
| stroke 5 | 33 % → 57 % | 312.8 px | 0.27 | 1.73 | 77 |
| stroke 6 | 35 % → 53 % | 277.6 px | 0.26 | 1.51 | 92 |
| stroke 7 | 42 % → 55 % | 237.8 px | 0.24 | 1.29 | 96 |

Numbers say: wet paint spreads well beyond the stroke.

## Watercolour · #35 Red band with runs — own sheet
own sheet 600 × 600 · Watercolour 1.00 + water 70 % · 80 px · 12.4 s

![Watercolour · #35 Red band with runs — own sheet](Watercolour-35-Red-band-with-runs-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 41 % → 53 % | 163.1 px | 0.28 | 1.29 | 608 |

## Watercolour · #40 Olive and sepia blooms — own sheet
own sheet 600 × 600 · Watercolour 1.00 + water 75 % · 80 px · 14.6 s

![Watercolour · #40 Olive and sepia blooms — own sheet](Watercolour-40-Olive-and-sepia-blooms-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 27 % → 53 % | 87.3 px | 0.04 | 1.96 | 961 |
| stroke 2 | 42 % → 54 % | 122.1 px | 0.04 | 1.28 | 639 |

Numbers say: wet paint spreads well beyond the stroke.

## Watercolour · #46 Lips on wet paper — own sheet
own sheet 600 × 600 · Watercolour 1.00 + water 65 % · 50 px · 10.9 s

![Watercolour · #46 Lips on wet paper — own sheet](Watercolour-46-Lips-on-wet-paper-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 13 % → 31 % | 56.0 px | 0.53 | 2.32 | 131 |
| stroke 2 | 15 % → 32 % | 63.8 px | 0.52 | 2.20 | 109 |

Numbers say: wet paint spreads well beyond the stroke.

