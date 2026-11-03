![All brushes](contact.png)

# Brush Lab — 147 brushes · Nov 3, 2026 at 7:09 PM

Every sheet: 1500 × 600, ten strokes in a 5 × 2 grid — 1. light line · 2. heavy line · 3. pressure swell · 4. fast wave · 5. slow wave · 6. spiral · 7. loop · 8. tilted · 9. over the wet one · 10. long, no reload (cell 8 holds «tilted» and «over the wet one» crossed). The CPU reference of Mamay's paint engine; the wet layer settles 20 s at the end.

Columns: **covered** = share of the cell with paint right after the stroke → after settling; **width** = painted area of the stroke ÷ its length (px); **dark** = mean darkness of the painted pixels above the paper's own grain (0 = paper, 1 = black); **spread** = how far wet paint went beyond the stroke (1.0 = stayed); **ms** = the stroke on the CPU; long stroke: paint in each quarter of its length (it should run out: wet → streaks → dry tail).

## Ink Line
Ink · 12 px · 27.5 s

![Ink Line](Ink-Line.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 1 % → 4 % | 4.3 px | 0.55 | 2.44 | 50 |
| heavy line | 5 % → 6 % | 15.7 px | 0.68 | 1.13 | 76 |
| pressure swell | 3 % → 4 % | 11.3 px | 0.64 | 1.40 | 47 |
| fast wave | 10 % → 11 % | 11.2 px | 0.59 | 1.11 | 168 |
| slow wave | 8 % → 10 % | 9.6 px | 0.57 | 1.16 | 134 |
| spiral | 14 % → 15 % | 8.9 px | 0.50 | 1.07 | 352 |
| loop | 8 % → 9 % | 10.6 px | 0.61 | 1.16 | 181 |
| tilted | 5 % → 5 % | 14.4 px | 0.65 | 1.05 | 66 |
| over the wet one | 10 % → 11 % | 12.5 px | 0.65 | 1.15 | 62 |
| long, no reload | 18 % → 17 % | 8.1 px | 0.47 | 0.96 | 352 | quarters: 0.22 → 0.09 → 0.04 → 0.02

Numbers say: light vs heavy: width 4.3 → 15.7 px, dark 0.55 → 0.68; wet paint spreads well beyond the stroke.

## Dense Ink
Ink · 14 px · 28.0 s

![Dense Ink](Dense-Ink.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 5 % → 7 % | 15.2 px | 0.72 | 1.26 | 61 |
| heavy line | 7 % → 7 % | 19.1 px | 0.73 | 1.09 | 97 |
| pressure swell | 5 % → 6 % | 17.9 px | 0.72 | 1.17 | 61 |
| fast wave | 13 % → 13 % | 15.3 px | 0.69 | 1.01 | 167 |
| slow wave | 12 % → 12 % | 13.6 px | 0.67 | 1.04 | 185 |
| spiral | 18 % → 15 % | 12.2 px | 0.65 | 0.80 | 532 |
| loop | 11 % → 12 % | 14.8 px | 0.69 | 1.08 | 263 |
| tilted | 5 % → 6 % | 14.6 px | 0.72 | 1.07 | 92 |
| over the wet one | 12 % → 13 % | 17.7 px | 0.72 | 1.11 | 66 |
| long, no reload | 23 % → 15 % | 10.1 px | 0.64 | 0.66 | 391 | quarters: 0.30 → 0.12 → 0.04 → 0.02

Numbers say: light vs heavy: width 15.2 → 19.1 px, dark 0.72 → 0.73.

## Transparent Wash
Watercolor · 22 px · 28.8 s

![Transparent Wash](Transparent-Wash.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 2 % → 5 % | 6.9 px | 0.27 | 2.25 | 41 |
| heavy line | 7 % → 9 % | 20.4 px | 0.27 | 1.22 | 68 |
| pressure swell | 4 % → 6 % | 15.2 px | 0.28 | 1.54 | 46 |
| fast wave | 14 % → 16 % | 16.1 px | 0.20 | 1.17 | 170 |
| slow wave | 12 % → 15 % | 13.7 px | 0.21 | 1.28 | 208 |
| spiral | 18 % → 22 % | 11.9 px | 0.16 | 1.23 | 372 |
| loop | 11 % → 13 % | 14.5 px | 0.22 | 1.20 | 145 |
| tilted | 8 % → 8 % | 21.1 px | 0.24 | 1.06 | 71 |
| over the wet one | 13 % → 16 % | 16.4 px | 0.24 | 1.18 | 60 |
| long, no reload | 26 % → 32 % | 11.6 px | 0.13 | 1.22 | 327 | quarters: 0.11 → 0.04 → 0.02 → 0.01

Numbers say: light vs heavy: width 6.9 → 20.4 px, dark 0.27 → 0.27; wet paint spreads well beyond the stroke.

## Dry Brush
Gouache · 24 px · 21.1 s

![Dry Brush](Dry-Brush.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 5 % → 0 % | 14.0 px | 0.65 | 0.09 | 45 |
| heavy line | 6 % → 0 % | 18.6 px | 0.65 | 0.02 | 102 |
| pressure swell | 5 % → 0 % | 18.2 px | 0.65 | 0.08 | 51 |
| fast wave | 6 % → 1 % | 7.3 px | 0.65 | 0.08 | 252 |
| slow wave | 7 % → 0 % | 8.1 px | 0.65 | 0.06 | 257 |
| spiral | 7 % → 0 % | 4.6 px | 0.65 | 0.07 | 282 |
| loop | 10 % → 0 % | 12.4 px | 0.65 | 0.04 | 138 |
| tilted | 4 % → 3 % | 10.6 px | 0.65 | 0.88 | 105 |
| over the wet one | 9 % → 1 % | 14.5 px | 0.65 | 0.12 | 62 |
| long, no reload | 6 % → 1 % | 2.9 px | 0.65 | 0.14 | 355 | quarters: 0.12 → 0.00 → 0.00 → 0.00

Numbers say: light vs heavy: width 14.0 → 18.6 px, dark 0.65 → 0.65.

## Wax Crayon
Wax · 8 px · 10.0 s

![Wax Crayon](Wax-Crayon.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 1 % → 1 % | 2.5 px | 0.71 | 1.00 | 16 |
| heavy line | 1 % → 1 % | 3.9 px | 0.69 | 1.00 | 17 |
| pressure swell | 1 % → 1 % | 3.3 px | 0.70 | 1.00 | 12 |
| fast wave | 3 % → 3 % | 3.5 px | 0.69 | 1.00 | 42 |
| slow wave | 3 % → 3 % | 3.4 px | 0.70 | 1.00 | 80 |
| spiral | 5 % → 5 % | 3.3 px | 0.70 | 1.00 | 128 |
| loop | 3 % → 3 % | 3.3 px | 0.70 | 1.00 | 53 |
| tilted | 2 % → 2 % | 5.6 px | 0.68 | 1.00 | 46 |
| over the wet one | 3 % → 3 % | 3.6 px | 0.68 | 1.00 | 17 |
| long, no reload | 7 % → 7 % | 3.3 px | 0.70 | 1.00 | 108 | quarters: 0.06 → 0.06 → 0.06 → 0.06

Numbers say: light vs heavy: width 2.5 → 3.9 px, dark 0.71 → 0.69; the long stroke does not run out of paint.

## Oil Pastel
Wax · 12 px · 10.3 s

![Oil Pastel](Oil-Pastel.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 1 % → 1 % | 4.0 px | 0.68 | 1.00 | 22 |
| heavy line | 2 % → 2 % | 6.5 px | 0.68 | 1.00 | 45 |
| pressure swell | 2 % → 2 % | 5.7 px | 0.69 | 1.00 | 39 |
| fast wave | 5 % → 5 % | 5.7 px | 0.68 | 1.00 | 100 |
| slow wave | 5 % → 5 % | 5.5 px | 0.68 | 1.00 | 81 |
| spiral | 8 % → 8 % | 5.5 px | 0.68 | 1.00 | 103 |
| loop | 4 % → 4 % | 5.6 px | 0.68 | 1.00 | 53 |
| tilted | 2 % → 2 % | 6.8 px | 0.68 | 1.00 | 41 |
| over the wet one | 5 % → 5 % | 5.8 px | 0.68 | 1.00 | 25 |
| long, no reload | 13 % → 13 % | 5.6 px | 0.68 | 1.00 | 161 | quarters: 0.10 → 0.09 → 0.10 → 0.10

Numbers say: light vs heavy: width 4.0 → 6.5 px, dark 0.68 → 0.68; the long stroke does not run out of paint.

## Charcoal
Charcoal · 5 px · 10.9 s

![Charcoal](Charcoal.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 1 % → 1 % | 2.0 px | 0.74 | 1.00 | 12 |
| heavy line | 1 % → 1 % | 3.0 px | 0.74 | 1.00 | 13 |
| pressure swell | 1 % → 1 % | 2.7 px | 0.74 | 1.00 | 10 |
| fast wave | 2 % → 2 % | 2.7 px | 0.73 | 1.00 | 31 |
| slow wave | 2 % → 2 % | 2.6 px | 0.74 | 1.00 | 31 |
| spiral | 4 % → 4 % | 2.5 px | 0.74 | 1.00 | 52 |
| loop | 2 % → 2 % | 2.6 px | 0.74 | 1.00 | 43 |
| tilted | 2 % → 2 % | 4.3 px | 0.72 | 1.00 | 35 |
| over the wet one | 2 % → 2 % | 2.4 px | 0.72 | 1.00 | 23 |
| long, no reload | 6 % → 6 % | 2.7 px | 0.73 | 1.00 | 201 | quarters: 0.05 → 0.05 → 0.05 → 0.05

Numbers say: light vs heavy: width 2.0 → 3.0 px, dark 0.74 → 0.74; the long stroke does not run out of paint.

## Impasto
Heavy acrylic · 22 px · 16.3 s

![Impasto](Impasto.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 8 % → 8 % | 24.1 px | 0.71 | 0.93 | 50 |
| heavy line | 10 % → 9 % | 28.8 px | 0.70 | 0.94 | 124 |
| pressure swell | 7 % → 7 % | 28.1 px | 0.72 | 0.94 | 114 |
| fast wave | 20 % → 13 % | 23.5 px | 0.71 | 0.64 | 543 |
| slow wave | 21 % → 14 % | 24.5 px | 0.71 | 0.66 | 583 |
| spiral | 30 % → 14 % | 20.0 px | 0.71 | 0.46 | 288 |
| loop | 18 % → 14 % | 23.9 px | 0.71 | 0.77 | 152 |
| tilted | 8 % → 8 % | 21.8 px | 0.70 | 1.00 | 78 |
| over the wet one | 17 % → 15 % | 25.4 px | 0.70 | 0.91 | 76 |
| long, no reload | 34 % → 14 % | 15.2 px | 0.71 | 0.41 | 401 | quarters: 0.38 → 0.21 → 0.10 → 0.03

Numbers say: light vs heavy: width 24.1 → 28.8 px, dark 0.71 → 0.70.

## Oil Round
Oil · 18 px · 16.9 s

![Oil Round](Oil-Round.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 2 % → 2 % | 7.2 px | 0.75 | 1.00 | 37 |
| heavy line | 7 % → 7 % | 19.3 px | 0.73 | 1.00 | 74 |
| pressure swell | 4 % → 4 % | 13.7 px | 0.72 | 1.00 | 41 |
| fast wave | 11 % → 11 % | 12.7 px | 0.65 | 1.00 | 187 |
| slow wave | 8 % → 8 % | 9.0 px | 0.57 | 1.00 | 176 |
| spiral | 10 % → 10 % | 6.6 px | 0.50 | 1.00 | 211 |
| loop | 5 % → 5 % | 7.1 px | 0.45 | 1.00 | 116 |
| tilted | 4 % → 4 % | 10.1 px | 0.52 | 1.00 | 65 |
| over the wet one | 6 % → 6 % | 7.4 px | 0.52 | 1.00 | 55 |
| long, no reload | 15 % → 15 % | 6.8 px | 0.42 | 1.00 | 498 | quarters: 0.08 → 0.08 → 0.07 → 0.06

Numbers say: light vs heavy: width 7.2 → 19.3 px, dark 0.75 → 0.73.

## Palette Knife
Oil · 20 px · 16.5 s

![Palette Knife](Palette-Knife.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 8 % → 8 % | 21.9 px | 0.67 | 1.00 | 20 |
| heavy line | 8 % → 8 % | 22.5 px | 0.73 | 1.00 | 15 |
| pressure swell | 6 % → 6 % | 22.4 px | 0.74 | 1.00 | 6 |
| fast wave | 17 % → 17 % | 19.3 px | 0.49 | 1.00 | 25 |
| slow wave | 17 % → 17 % | 19.9 px | 0.43 | 1.00 | 43 |
| spiral | 18 % → 18 % | 11.7 px | 0.45 | 1.00 | 44 |
| loop | 16 % → 16 % | 21.0 px | 0.58 | 1.00 | 28 |
| tilted | 5 % → 5 % | 15.0 px | 0.72 | 1.00 | 11 |
| over the wet one | 13 % → 13 % | 21.0 px | 0.72 | 1.00 | 11 |
| long, no reload | 17 % → 17 % | 7.5 px | 0.47 | 1.00 | 78 | quarters: 0.29 → 0.05 → 0.00 → 0.00

Numbers say: light vs heavy: width 21.9 → 22.5 px, dark 0.67 → 0.73; pressure barely changes the width.

## Water
Watercolor · 20 px · 35.9 s · over bands of wet oil paint and oil pastel in turn (it works on paint already there: look at what it does to the bands; covered counts the bands too)

![Water](Water.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 25 % → 27 % | 73.8 px | 0.80 | 1.06 | 25 |
| heavy line | 24 % → 25 % | 69.8 px | 0.81 | 1.04 | 55 |
| pressure swell | 24 % → 25 % | 89.6 px | 0.81 | 1.03 | 40 |
| fast wave | 24 % → 26 % | 27.7 px | 0.81 | 1.07 | 108 |
| slow wave | 24 % → 25 % | 27.7 px | 0.81 | 1.06 | 147 |
| spiral | 24 % → 26 % | 15.9 px | 0.81 | 1.07 | 167 |
| loop | 24 % → 25 % | 31.1 px | 0.81 | 1.03 | 110 |
| tilted | 24 % → 24 % | 67.0 px | 0.81 | 1.00 | 80 |
| over the wet one | 24 % → 25 % | 0.0 px | 0.81 | 1.06 | 63 |
| long, no reload | 24 % → 26 % | 10.7 px | 0.81 | 1.08 | 309 | quarters: 0.21 → 0.27 → 0.18 → 0.27

Numbers say: light vs heavy: width 73.8 → 69.8 px, dark 0.80 → 0.81; pressure barely changes the width; the long stroke does not run out of paint.

## Blender
Pastel · 16 px · 24.5 s · over bands of wet oil paint and oil pastel in turn (it works on paint already there: look at what it does to the bands; covered counts the bands too)

![Blender](Blender.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 24 % → 24 % | 70.7 px | 0.81 | 1.00 | 22 |
| heavy line | 25 % → 25 % | 72.1 px | 0.80 | 1.00 | 34 |
| pressure swell | 24 % → 24 % | 91.3 px | 0.81 | 1.00 | 22 |
| fast wave | 26 % → 26 % | 30.0 px | 0.79 | 1.00 | 77 |
| slow wave | 26 % → 26 % | 29.9 px | 0.80 | 1.00 | 85 |
| spiral | 28 % → 28 % | 18.7 px | 0.77 | 1.00 | 121 |
| loop | 25 % → 25 % | 32.9 px | 0.80 | 1.00 | 66 |
| tilted | 25 % → 25 % | 70.1 px | 0.79 | 1.00 | 46 |
| over the wet one | 26 % → 26 % | 1.8 px | 0.79 | 1.00 | 34 |
| long, no reload | 30 % → 30 % | 13.7 px | 0.76 | 1.00 | 190 | quarters: 0.20 → 0.28 → 0.23 → 0.30

Numbers say: light vs heavy: width 70.7 → 72.1 px, dark 0.81 → 0.80; pressure barely changes the width; the long stroke does not run out of paint.

## Eraser
Eraser · 16 px · 20.7 s · over bands of wet oil paint and oil pastel in turn (it works on paint already there: look at what it does to the bands; covered counts the bands too)

![Eraser](Eraser.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 24 % → 24 % | 69.5 px | 0.82 | 1.00 | 25 |
| heavy line | 23 % → 23 % | 67.9 px | 0.82 | 1.00 | 35 |
| pressure swell | 23 % → 23 % | 87.3 px | 0.82 | 1.00 | 23 |
| fast wave | 22 % → 22 % | 25.7 px | 0.82 | 1.00 | 80 |
| slow wave | 22 % → 22 % | 25.7 px | 0.82 | 1.00 | 94 |
| spiral | 22 % → 22 % | 14.4 px | 0.82 | 1.00 | 124 |
| loop | 22 % → 22 % | 28.6 px | 0.82 | 1.00 | 70 |
| tilted | 23 % → 23 % | 65.1 px | 0.82 | 1.00 | 46 |
| over the wet one | 23 % → 23 % | 0.0 px | 0.82 | 1.00 | 32 |
| long, no reload | 20 % → 20 % | 8.9 px | 0.82 | 1.00 | 195 | quarters: 0.15 → 0.20 → 0.15 → 0.20

Numbers say: light vs heavy: width 69.5 → 67.9 px, dark 0.82 → 0.82; pressure barely changes the width; the long stroke does not run out of paint.

## Fan
Gouache · 30 px · 35.4 s

![Fan](Fan.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 9 % → 3 % | 25.7 px | 0.63 | 0.37 | 60 |
| heavy line | 11 % → 4 % | 31.0 px | 0.63 | 0.39 | 98 |
| pressure swell | 8 % → 5 % | 31.7 px | 0.63 | 0.55 | 50 |
| fast wave | 18 % → 5 % | 20.3 px | 0.63 | 0.26 | 299 |
| slow wave | 18 % → 5 % | 21.1 px | 0.63 | 0.25 | 295 |
| spiral | 24 % → 5 % | 15.8 px | 0.63 | 0.20 | 236 |
| loop | 17 % → 5 % | 22.7 px | 0.63 | 0.29 | 128 |
| tilted | 5 % → 6 % | 15.1 px | 0.63 | 1.05 | 53 |
| over the wet one | 16 % → 8 % | 29.8 px | 0.63 | 0.50 | 60 |
| long, no reload | 23 % → 5 % | 10.1 px | 0.63 | 0.22 | 366 | quarters: 0.29 → 0.07 → 0.01 → 0.00

Numbers say: light vs heavy: width 25.7 → 31.0 px, dark 0.63 → 0.63.

## Sponge
Gouache · 30 px · 34.0 s

![Sponge](Sponge.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 4 % → 0 % | 11.4 px | 0.62 | 0.12 | 76 |
| heavy line | 12 % → 2 % | 35.4 px | 0.62 | 0.14 | 138 |
| pressure swell | 7 % → 2 % | 27.9 px | 0.62 | 0.27 | 60 |
| fast wave | 20 % → 4 % | 23.2 px | 0.62 | 0.19 | 185 |
| slow wave | 21 % → 4 % | 23.7 px | 0.62 | 0.18 | 388 |
| spiral | 28 % → 4 % | 18.3 px | 0.62 | 0.14 | 287 |
| loop | 18 % → 5 % | 23.0 px | 0.62 | 0.29 | 148 |
| tilted | 7 % → 7 % | 18.2 px | 0.62 | 1.04 | 136 |
| over the wet one | 16 % → 6 % | 27.8 px | 0.62 | 0.37 | 77 |
| long, no reload | 29 % → 5 % | 12.9 px | 0.62 | 0.17 | 609 | quarters: 0.29 → 0.13 → 0.07 → 0.04

Numbers say: light vs heavy: width 11.4 → 35.4 px, dark 0.62 → 0.62.

## Ink — sumi brush
Watercolor · 22 px · 34.9 s

![Ink — sumi brush](Ink-sumi-brush.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 8 % → 9 % | 23.8 px | 0.77 | 1.13 | 117 |
| heavy line | 13 % → 13 % | 38.0 px | 0.72 | 1.01 | 86 |
| pressure swell | 9 % → 10 % | 34.5 px | 0.75 | 1.05 | 61 |
| fast wave | 27 % → 28 % | 31.7 px | 0.58 | 1.03 | 201 |
| slow wave | 25 % → 26 % | 29.0 px | 0.61 | 1.05 | 375 |
| spiral | 37 % → 38 % | 24.3 px | 0.51 | 1.03 | 385 |
| loop | 22 % → 22 % | 28.2 px | 0.66 | 1.03 | 183 |
| tilted | 9 % → 9 % | 24.7 px | 0.73 | 1.03 | 121 |
| over the wet one | 20 % → 21 % | 31.1 px | 0.73 | 1.03 | 100 |
| long, no reload | 42 % → 43 % | 18.9 px | 0.46 | 1.02 | 835 | quarters: 0.47 → 0.23 → 0.11 → 0.06

Numbers say: light vs heavy: width 23.8 → 38.0 px, dark 0.77 → 0.72.

## Ink — wash
Watercolor · 40 px · 32.6 s

![Ink — wash](Ink-wash.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 13 % → 13 % | 36.5 px | 0.17 | 1.04 | 130 |
| heavy line | 18 % → 19 % | 53.5 px | 0.13 | 1.04 | 83 |
| pressure swell | 12 % → 13 % | 46.6 px | 0.16 | 1.05 | 58 |
| fast wave | 40 % → 42 % | 45.9 px | 0.12 | 1.06 | 201 |
| slow wave | 38 % → 40 % | 43.6 px | 0.17 | 1.06 | 409 |
| spiral | 58 % → 62 % | 38.5 px | 0.12 | 1.06 | 474 |
| loop | 33 % → 34 % | 42.9 px | 0.15 | 1.03 | 165 |
| tilted | 14 % → 14 % | 38.1 px | 0.17 | 1.03 | 103 |
| over the wet one | 29 % → 31 % | 43.2 px | 0.17 | 1.06 | 85 |
| long, no reload | 66 % → 75 % | 29.8 px | 0.12 | 1.12 | 496 | quarters: 0.16 → 0.11 → 0.07 → 0.04

Numbers say: light vs heavy: width 36.5 → 53.5 px, dark 0.17 → 0.13.

## Ink — dry brush
Ink · 30 px · 23.2 s

![Ink — dry brush](Ink-dry-brush.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 9 % → 7 % | 25.2 px | 0.81 | 0.79 | 86 |
| heavy line | 10 % → 8 % | 29.6 px | 0.80 | 0.76 | 123 |
| pressure swell | 7 % → 6 % | 27.9 px | 0.81 | 0.85 | 106 |
| fast wave | 21 % → 8 % | 24.2 px | 0.79 | 0.40 | 271 |
| slow wave | 18 % → 7 % | 20.3 px | 0.79 | 0.39 | 397 |
| spiral | 24 % → 8 % | 15.6 px | 0.78 | 0.34 | 370 |
| loop | 19 % → 8 % | 24.3 px | 0.78 | 0.45 | 215 |
| tilted | 8 % → 8 % | 22.2 px | 0.78 | 1.02 | 123 |
| over the wet one | 17 % → 14 % | 25.9 px | 0.78 | 0.81 | 104 |
| long, no reload | 20 % → 8 % | 9.1 px | 0.79 | 0.41 | 541 | quarters: 0.32 → 0.02 → 0.00 → 0.00

Numbers say: light vs heavy: width 25.2 → 29.6 px, dark 0.81 → 0.80.

## Ink — nib
Watercolor · 5 px · 21.6 s

![Ink — nib](Ink-nib.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 2 % → 5 % | 5.4 px | 0.86 | 2.45 | 37 |
| heavy line | 2 % → 5 % | 6.4 px | 0.86 | 2.33 | 28 |
| pressure swell | 2 % → 4 % | 6.2 px | 0.86 | 2.52 | 19 |
| fast wave | 5 % → 8 % | 5.8 px | 0.82 | 1.65 | 78 |
| slow wave | 5 % → 8 % | 5.6 px | 0.82 | 1.73 | 65 |
| spiral | 7 % → 11 % | 4.8 px | 0.75 | 1.45 | 137 |
| loop | 4 % → 8 % | 5.6 px | 0.84 | 1.75 | 59 |
| tilted | 4 % → 4 % | 10.1 px | 0.85 | 1.04 | 42 |
| over the wet one | 6 % → 9 % | 6.3 px | 0.85 | 1.61 | 26 |
| long, no reload | 9 % → 12 % | 4.0 px | 0.70 | 1.37 | 163 | quarters: 0.23 → 0.08 → 0.04 → 0.02

Numbers say: light vs heavy: width 5.4 → 6.4 px, dark 0.86 → 0.86; wet paint spreads well beyond the stroke.

## 0.45 · Dry brush
Gouache · 34 px · 24.5 s

![0.45 · Dry brush](0-45-Dry-brush.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 10 % → 3 % | 29.4 px | 0.67 | 0.27 | 112 |
| heavy line | 11 % → 3 % | 31.6 px | 0.67 | 0.29 | 120 |
| pressure swell | 8 % → 3 % | 31.5 px | 0.67 | 0.41 | 122 |
| fast wave | 19 % → 3 % | 22.5 px | 0.67 | 0.18 | 422 |
| slow wave | 20 % → 4 % | 23.2 px | 0.67 | 0.18 | 492 |
| spiral | 21 % → 3 % | 14.1 px | 0.67 | 0.16 | 506 |
| loop | 20 % → 4 % | 26.1 px | 0.67 | 0.20 | 351 |
| tilted | 9 % → 8 % | 24.0 px | 0.67 | 0.98 | 145 |
| over the wet one | 19 % → 6 % | 28.2 px | 0.67 | 0.34 | 121 |
| long, no reload | 20 % → 4 % | 9.1 px | 0.67 | 0.19 | 769 | quarters: 0.36 → 0.10 → 0.00 → 0.00

Numbers say: light vs heavy: width 29.4 → 31.6 px, dark 0.67 → 0.67; pressure barely changes the width.

## Dry pastel
Pastel · 26 px · 10.7 s

![Dry pastel](Dry-pastel.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 3 % → 3 % | 8.3 px | 0.38 | 1.00 | 31 |
| heavy line | 5 % → 5 % | 13.2 px | 0.39 | 1.00 | 34 |
| pressure swell | 3 % → 3 % | 11.7 px | 0.38 | 1.00 | 39 |
| fast wave | 10 % → 10 % | 11.9 px | 0.39 | 1.00 | 119 |
| slow wave | 10 % → 10 % | 11.3 px | 0.39 | 1.00 | 220 |
| spiral | 15 % → 15 % | 9.6 px | 0.39 | 1.00 | 225 |
| loop | 7 % → 7 % | 9.4 px | 0.39 | 1.00 | 77 |
| tilted | 3 % → 3 % | 8.3 px | 0.38 | 1.00 | 41 |
| over the wet one | 7 % → 7 % | 11.1 px | 0.38 | 1.00 | 35 |
| long, no reload | 18 % → 18 % | 8.2 px | 0.39 | 1.00 | 216 | quarters: 0.08 → 0.08 → 0.08 → 0.07

Numbers say: light vs heavy: width 8.3 → 13.2 px, dark 0.38 → 0.39; the long stroke does not run out of paint.

## 0.45 · Charcoal
Charcoal · 18 px · 10.2 s

![0.45 · Charcoal](0-45-Charcoal.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 2 % → 2 % | 6.5 px | 0.80 | 1.00 | 17 |
| heavy line | 3 % → 3 % | 9.2 px | 0.80 | 1.00 | 17 |
| pressure swell | 2 % → 2 % | 8.8 px | 0.80 | 1.00 | 13 |
| fast wave | 7 % → 7 % | 8.5 px | 0.80 | 1.00 | 43 |
| slow wave | 7 % → 7 % | 8.0 px | 0.80 | 1.00 | 72 |
| spiral | 12 % → 12 % | 7.9 px | 0.80 | 1.00 | 86 |
| loop | 6 % → 6 % | 8.1 px | 0.80 | 1.00 | 45 |
| tilted | 3 % → 3 % | 7.5 px | 0.80 | 1.00 | 26 |
| over the wet one | 6 % → 6 % | 7.9 px | 0.80 | 1.00 | 17 |
| long, no reload | 17 % → 17 % | 7.8 px | 0.80 | 1.00 | 108 | quarters: 0.15 → 0.16 → 0.15 → 0.16

Numbers say: light vs heavy: width 6.5 → 9.2 px, dark 0.80 → 0.80; the long stroke does not run out of paint.

## Watercolour — wash
Watercolor · 50 px · 38.5 s

![Watercolour — wash](Watercolour-wash.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 15 % → 16 % | 43.3 px | 0.03 | 1.05 | 103 |
| heavy line | 21 % → 22 % | 62.1 px | 0.03 | 1.04 | 173 |
| pressure swell | 14 % → 15 % | 54.3 px | 0.03 | 1.04 | 142 |
| fast wave | 47 % → 49 % | 53.8 px | 0.02 | 1.04 | 392 |
| slow wave | 45 % → 46 % | 52.0 px | 0.04 | 1.03 | 472 |
| spiral | 64 % → 66 % | 42.5 px | 0.03 | 1.03 | 482 |
| loop | 39 % → 40 % | 50.3 px | 0.03 | 1.02 | 255 |
| tilted | 17 % → 17 % | 47.3 px | 0.04 | 1.03 | 180 |
| over the wet one | 35 % → 36 % | 49.0 px | 0.04 | 1.04 | 140 |
| long, no reload | 79 % → 84 % | 35.5 px | 0.03 | 1.06 | 728 | quarters: 0.04 → 0.03 → 0.02 → 0.01

Numbers say: light vs heavy: width 43.3 → 62.1 px, dark 0.03 → 0.03.

## Watercolour — wet-in-wet
Watercolor · 44 px · 39.2 s

![Watercolour — wet-in-wet](Watercolour-wet-in-wet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 13 % → 19 % | 36.6 px | 0.05 | 1.51 | 79 |
| heavy line | 18 % → 20 % | 52.4 px | 0.05 | 1.09 | 97 |
| pressure swell | 12 % → 15 % | 44.9 px | 0.06 | 1.26 | 68 |
| fast wave | 40 % → 45 % | 45.9 px | 0.05 | 1.13 | 279 |
| slow wave | 39 % → 45 % | 45.0 px | 0.07 | 1.15 | 403 |
| spiral | 62 % → 67 % | 40.8 px | 0.06 | 1.08 | 374 |
| loop | 33 % → 37 % | 43.2 px | 0.06 | 1.12 | 196 |
| tilted | 14 % → 14 % | 39.1 px | 0.06 | 1.03 | 127 |
| over the wet one | 29 % → 37 % | 41.7 px | 0.06 | 1.28 | 90 |
| long, no reload | 75 % → 84 % | 33.6 px | 0.06 | 1.12 | 673 | quarters: 0.07 → 0.06 → 0.04 → 0.03

Numbers say: light vs heavy: width 36.6 → 52.4 px, dark 0.05 → 0.05; wet paint spreads well beyond the stroke.

## Watercolour — glaze
Watercolor · 38 px · 36.8 s

![Watercolour — glaze](Watercolour-glaze.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 12 % → 13 % | 35.2 px | 0.03 | 1.05 | 73 |
| heavy line | 18 % → 19 % | 52.2 px | 0.02 | 1.06 | 175 |
| pressure swell | 12 % → 13 % | 44.6 px | 0.02 | 1.07 | 84 |
| fast wave | 37 % → 40 % | 42.4 px | 0.02 | 1.08 | 225 |
| slow wave | 35 % → 37 % | 40.2 px | 0.02 | 1.08 | 507 |
| spiral | 54 % → 59 % | 35.9 px | 0.02 | 1.09 | 343 |
| loop | 32 % → 33 % | 40.8 px | 0.02 | 1.05 | 174 |
| tilted | 13 % → 14 % | 37.0 px | 0.03 | 1.03 | 239 |
| over the wet one | 28 % → 30 % | 41.7 px | 0.03 | 1.06 | 78 |
| long, no reload | 60 % → 69 % | 26.8 px | 0.02 | 1.15 | 579 | quarters: 0.02 → 0.01 → 0.01 → 0.00

Numbers say: light vs heavy: width 35.2 → 52.2 px, dark 0.03 → 0.02.

## Watercolour — granulating
Watercolor · 44 px · 38.3 s

![Watercolour — granulating](Watercolour-granulating.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 14 % → 14 % | 40.5 px | 0.05 | 1.03 | 117 |
| heavy line | 20 % → 21 % | 59.2 px | 0.04 | 1.02 | 108 |
| pressure swell | 14 % → 14 % | 51.3 px | 0.05 | 1.02 | 73 |
| fast wave | 44 % → 45 % | 50.3 px | 0.04 | 1.04 | 246 |
| slow wave | 40 % → 42 % | 46.0 px | 0.06 | 1.06 | 578 |
| spiral | 59 % → 63 % | 38.7 px | 0.04 | 1.07 | 492 |
| loop | 36 % → 37 % | 46.9 px | 0.05 | 1.02 | 232 |
| tilted | 15 % → 16 % | 43.1 px | 0.06 | 1.03 | 146 |
| over the wet one | 32 % → 33 % | 46.6 px | 0.06 | 1.04 | 111 |
| long, no reload | 68 % → 76 % | 30.3 px | 0.04 | 1.12 | 794 | quarters: 0.06 → 0.04 → 0.02 → 0.02

Numbers say: light vs heavy: width 40.5 → 59.2 px, dark 0.05 → 0.04.

## Watercolour — dry brush
Watercolor · 36 px · 30.8 s

![Watercolour — dry brush](Watercolour-dry-brush.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 9 % → 9 % | 24.9 px | 0.07 | 1.09 | 91 |
| heavy line | 13 % → 13 % | 36.7 px | 0.06 | 0.99 | 106 |
| pressure swell | 10 % → 10 % | 36.4 px | 0.06 | 1.04 | 90 |
| fast wave | 24 % → 19 % | 27.3 px | 0.05 | 0.82 | 407 |
| slow wave | 22 % → 17 % | 25.2 px | 0.05 | 0.78 | 506 |
| spiral | 29 % → 20 % | 19.3 px | 0.05 | 0.67 | 667 |
| loop | 19 % → 18 % | 24.6 px | 0.05 | 0.94 | 226 |
| tilted | 9 % → 10 % | 24.3 px | 0.06 | 1.10 | 162 |
| over the wet one | 20 % → 20 % | 31.7 px | 0.06 | 0.99 | 117 |
| long, no reload | 28 % → 19 % | 12.4 px | 0.05 | 0.70 | 765 | quarters: 0.03 → 0.01 → 0.00 → 0.00

Numbers say: light vs heavy: width 24.9 → 36.7 px, dark 0.07 → 0.06.

## Gouache
Gouache · 30 px · 31.3 s

![Gouache](Gouache.png)

A light paint: laid on a grey sheet (on white it cannot be seen); **dark** = how far it is from the grey either way.

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 8 % → 5 % | 24.4 px | 0.28 | 0.64 | 117 |
| heavy line | 14 % → 6 % | 39.7 px | 0.28 | 0.47 | 89 |
| pressure swell | 10 % → 6 % | 38.6 px | 0.28 | 0.60 | 64 |
| fast wave | 28 % → 7 % | 32.2 px | 0.28 | 0.25 | 234 |
| slow wave | 27 % → 8 % | 31.4 px | 0.28 | 0.29 | 440 |
| spiral | 38 % → 8 % | 24.8 px | 0.27 | 0.22 | 409 |
| loop | 22 % → 8 % | 28.6 px | 0.28 | 0.35 | 184 |
| tilted | 9 % → 9 % | 23.8 px | 0.27 | 1.01 | 109 |
| over the wet one | 20 % → 13 % | 31.1 px | 0.27 | 0.66 | 87 |
| long, no reload | 40 % → 9 % | 17.9 px | 0.27 | 0.24 | 657 | quarters: 0.01 → 0.01 → 0.02 → 0.02

Numbers say: light vs heavy: width 24.4 → 39.7 px, dark 0.28 → 0.28; the long stroke does not run out of paint.

## Oil — alla prima
Oil · 30 px · 14.8 s

![Oil — alla prima](Oil-alla-prima.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 10 % → 10 % | 27.6 px | 0.51 | 1.00 | 106 |
| heavy line | 10 % → 10 % | 30.4 px | 0.51 | 1.00 | 106 |
| pressure swell | 8 % → 8 % | 29.9 px | 0.53 | 1.00 | 79 |
| fast wave | 24 % → 24 % | 28.1 px | 0.51 | 1.00 | 289 |
| slow wave | 26 % → 26 % | 29.6 px | 0.51 | 1.00 | 508 |
| spiral | 40 % → 40 % | 26.4 px | 0.51 | 1.00 | 404 |
| loop | 21 % → 21 % | 27.7 px | 0.52 | 1.00 | 212 |
| tilted | 11 % → 11 % | 30.4 px | 0.51 | 1.00 | 110 |
| over the wet one | 20 % → 20 % | 26.6 px | 0.51 | 1.00 | 95 |
| long, no reload | 49 % → 49 % | 22.0 px | 0.50 | 1.00 | 689 | quarters: 0.32 → 0.29 → 0.26 → 0.22

Numbers say: light vs heavy: width 27.6 → 30.4 px, dark 0.51 → 0.51; pressure barely changes the width.

## Oil — impasto
Oil · 34 px · 20.8 s

![Oil — impasto](Oil-impasto.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 12 % → 12 % | 33.5 px | 0.24 | 1.00 | 123 |
| heavy line | 13 % → 13 % | 36.4 px | 0.23 | 1.00 | 147 |
| pressure swell | 10 % → 10 % | 35.9 px | 0.26 | 1.00 | 109 |
| fast wave | 30 % → 30 % | 35.1 px | 0.24 | 1.00 | 360 |
| slow wave | 31 % → 31 % | 35.8 px | 0.24 | 1.00 | 475 |
| spiral | 52 % → 52 % | 34.1 px | 0.22 | 1.00 | 554 |
| loop | 26 % → 26 % | 33.7 px | 0.24 | 1.00 | 296 |
| tilted | 12 % → 12 % | 32.8 px | 0.24 | 1.00 | 219 |
| over the wet one | 23 % → 23 % | 32.0 px | 0.24 | 1.00 | 151 |
| long, no reload | 60 % → 60 % | 27.0 px | 0.22 | 1.00 | 692 | quarters: 0.18 → 0.16 → 0.13 → 0.10

Numbers say: light vs heavy: width 33.5 → 36.4 px, dark 0.24 → 0.23; pressure barely changes the width.

## Oil — glaze
Oil · 40 px · 18.5 s

![Oil — glaze](Oil-glaze.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 9 % → 9 % | 25.4 px | 0.50 | 1.00 | 101 |
| heavy line | 13 % → 13 % | 36.3 px | 0.49 | 1.00 | 131 |
| pressure swell | 9 % → 9 % | 35.3 px | 0.50 | 1.00 | 125 |
| fast wave | 26 % → 26 % | 30.1 px | 0.48 | 1.00 | 387 |
| slow wave | 29 % → 29 % | 33.7 px | 0.49 | 1.00 | 428 |
| spiral | 44 % → 44 % | 29.0 px | 0.49 | 1.00 | 441 |
| loop | 23 % → 23 % | 30.2 px | 0.50 | 1.00 | 245 |
| tilted | 10 % → 10 % | 28.9 px | 0.50 | 1.00 | 285 |
| over the wet one | 22 % → 22 % | 31.6 px | 0.50 | 1.00 | 155 |
| long, no reload | 51 % → 51 % | 22.7 px | 0.49 | 1.00 | 748 | quarters: 0.33 → 0.29 → 0.26 → 0.22

Numbers say: light vs heavy: width 25.4 → 36.3 px, dark 0.50 → 0.49.

## Oil — scumble
Oil · 36 px · 17.4 s

![Oil — scumble](Oil-scumble.png)

A light paint: laid on a grey sheet (on white it cannot be seen); **dark** = how far it is from the grey either way.

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 11 % → 11 % | 33.1 px | 0.28 | 1.00 | 118 |
| heavy line | 12 % → 12 % | 36.1 px | 0.28 | 1.00 | 134 |
| pressure swell | 9 % → 9 % | 35.5 px | 0.28 | 1.00 | 92 |
| fast wave | 26 % → 26 % | 29.6 px | 0.19 | 1.00 | 316 |
| slow wave | 27 % → 27 % | 30.9 px | 0.18 | 1.00 | 535 |
| spiral | 41 % → 41 % | 27.1 px | 0.13 | 1.00 | 567 |
| loop | 24 % → 24 % | 30.7 px | 0.20 | 1.00 | 486 |
| tilted | 11 % → 11 % | 30.5 px | 0.25 | 1.00 | 258 |
| over the wet one | 22 % → 22 % | 31.5 px | 0.25 | 1.00 | 239 |
| long, no reload | 45 % → 45 % | 20.3 px | 0.12 | 1.00 | 1950 | quarters: 0.00 → 0.00 → 0.00 → 0.00

Numbers say: light vs heavy: width 33.1 → 36.1 px, dark 0.28 → 0.28; pressure barely changes the width.

## Acrylic — heavy body
Heavy acrylic · 30 px · 16.2 s

![Acrylic — heavy body](Acrylic-heavy-body.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 10 % → 9 % | 29.0 px | 0.51 | 0.90 | 237 |
| heavy line | 11 % → 10 % | 31.2 px | 0.51 | 0.92 | 137 |
| pressure swell | 8 % → 8 % | 30.8 px | 0.53 | 0.94 | 69 |
| fast wave | 23 % → 15 % | 26.5 px | 0.52 | 0.64 | 255 |
| slow wave | 24 % → 16 % | 27.8 px | 0.51 | 0.64 | 475 |
| spiral | 35 % → 15 % | 23.3 px | 0.51 | 0.43 | 499 |
| loop | 21 % → 16 % | 26.9 px | 0.51 | 0.76 | 204 |
| tilted | 9 % → 9 % | 24.9 px | 0.51 | 0.99 | 116 |
| over the wet one | 19 % → 17 % | 27.8 px | 0.51 | 0.89 | 94 |
| long, no reload | 39 % → 16 % | 17.3 px | 0.51 | 0.41 | 597 | quarters: 0.29 → 0.20 → 0.12 → 0.04

Numbers say: light vs heavy: width 29.0 → 31.2 px, dark 0.51 → 0.51; pressure barely changes the width.

## Acrylic — fluid
Watercolor · 36 px · 32.1 s

![Acrylic — fluid](Acrylic-fluid.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 12 % → 12 % | 34.3 px | 0.08 | 1.02 | 84 |
| heavy line | 18 % → 18 % | 51.6 px | 0.07 | 1.01 | 109 |
| pressure swell | 12 % → 12 % | 44.8 px | 0.08 | 1.01 | 72 |
| fast wave | 37 % → 38 % | 42.6 px | 0.07 | 1.02 | 203 |
| slow wave | 34 % → 35 % | 39.2 px | 0.07 | 1.03 | 344 |
| spiral | 52 % → 53 % | 34.2 px | 0.07 | 1.03 | 349 |
| loop | 30 % → 31 % | 39.4 px | 0.07 | 1.02 | 178 |
| tilted | 12 % → 12 % | 32.6 px | 0.08 | 1.04 | 103 |
| over the wet one | 27 % → 28 % | 43.2 px | 0.08 | 1.02 | 80 |
| long, no reload | 56 % → 58 % | 25.3 px | 0.06 | 1.04 | 498 | quarters: 0.06 → 0.05 → 0.03 → 0.02

Numbers say: light vs heavy: width 34.3 → 51.6 px, dark 0.08 → 0.07.

## Acrylic — palette knife
Heavy acrylic · 42 px · 19.7 s

![Acrylic — palette knife](Acrylic-palette-knife.png)

A light paint: laid on a grey sheet (on white it cannot be seen); **dark** = how far it is from the grey either way.

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 15 % → 15 % | 44.0 px | 0.39 | 0.98 | 30 |
| heavy line | 15 % → 15 % | 44.2 px | 0.40 | 0.97 | 35 |
| pressure swell | 12 % → 12 % | 43.5 px | 0.42 | 0.99 | 10 |
| fast wave | 36 % → 20 % | 41.9 px | 0.36 | 0.56 | 67 |
| slow wave | 37 % → 21 % | 42.6 px | 0.37 | 0.57 | 111 |
| spiral | 50 % → 18 % | 32.7 px | 0.37 | 0.37 | 115 |
| loop | 32 % → 24 % | 41.2 px | 0.36 | 0.75 | 57 |
| tilted | 12 % → 12 % | 33.6 px | 0.39 | 1.00 | 25 |
| over the wet one | 26 % → 25 % | 39.7 px | 0.39 | 0.97 | 48 |
| long, no reload | 57 % → 21 % | 25.6 px | 0.34 | 0.36 | 164 | quarters: 0.00 → 0.00 → 0.00 → 0.01

Numbers say: light vs heavy: width 44.0 → 44.2 px, dark 0.39 → 0.40; pressure barely changes the width; the long stroke does not run out of paint.

## Finger on oil
Oil · 30 px · 13.5 s

![Finger on oil](Finger-on-oil.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 8 % → 8 % | 23.8 px | 0.41 | 1.00 | 57 |
| heavy line | 13 % → 13 % | 36.6 px | 0.39 | 1.00 | 80 |
| pressure swell | 9 % → 9 % | 33.4 px | 0.41 | 1.00 | 44 |
| fast wave | 22 % → 22 % | 26.0 px | 0.35 | 1.00 | 131 |
| slow wave | 24 % → 24 % | 27.9 px | 0.35 | 1.00 | 225 |
| spiral | 36 % → 36 % | 23.5 px | 0.28 | 1.00 | 229 |
| loop | 21 % → 21 % | 27.4 px | 0.36 | 1.00 | 120 |
| tilted | 10 % → 10 % | 26.5 px | 0.40 | 1.00 | 77 |
| over the wet one | 20 % → 20 % | 29.4 px | 0.40 | 1.00 | 50 |
| long, no reload | 37 % → 37 % | 16.4 px | 0.26 | 1.00 | 317 | quarters: 0.23 → 0.11 → 0.05 → 0.02

Numbers say: light vs heavy: width 23.8 → 36.6 px, dark 0.41 → 0.39.

## Palette knife — oil
Oil · 44 px · 17.8 s

![Palette knife — oil](Palette-knife-oil.png)

A light paint: laid on a grey sheet (on white it cannot be seen); **dark** = how far it is from the grey either way.

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 16 % → 16 % | 45.6 px | 0.36 | 1.00 | 50 |
| heavy line | 16 % → 16 % | 46.3 px | 0.38 | 1.00 | 27 |
| pressure swell | 12 % → 12 % | 45.2 px | 0.38 | 1.00 | 10 |
| fast wave | 39 % → 39 % | 44.9 px | 0.34 | 1.01 | 57 |
| slow wave | 39 % → 39 % | 45.4 px | 0.35 | 1.00 | 97 |
| spiral | 62 % → 62 % | 40.9 px | 0.27 | 1.00 | 109 |
| loop | 34 % → 34 % | 43.8 px | 0.35 | 1.00 | 52 |
| tilted | 13 % → 13 % | 36.6 px | 0.37 | 1.00 | 22 |
| over the wet one | 28 % → 28 % | 40.8 px | 0.37 | 1.00 | 25 |
| long, no reload | 74 % → 74 % | 33.1 px | 0.25 | 1.00 | 137 | quarters: 0.00 → 0.00 → 0.00 → 0.00

Numbers say: light vs heavy: width 45.6 → 46.3 px, dark 0.36 → 0.38; pressure barely changes the width; the long stroke does not run out of paint.

## 0.45 · Sponge
Watercolor · 46 px · 32.2 s

![0.45 · Sponge](0-45-Sponge.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 23 % → 15 % | 66.4 px | 0.02 | 0.67 | 60 |
| heavy line | 28 % → 23 % | 81.1 px | 0.02 | 0.81 | 103 |
| pressure swell | 20 % → 16 % | 76.7 px | 0.03 | 0.76 | 59 |
| fast wave | 46 % → 32 % | 53.0 px | 0.03 | 0.70 | 171 |
| slow wave | 53 % → 46 % | 60.7 px | 0.04 | 0.87 | 323 |
| spiral | 65 % → 53 % | 42.6 px | 0.04 | 0.82 | 276 |
| loop | 46 % → 40 % | 60.1 px | 0.04 | 0.86 | 210 |
| tilted | 16 % → 17 % | 43.8 px | 0.05 | 1.07 | 142 |
| over the wet one | 40 % → 35 % | 67.3 px | 0.05 | 0.89 | 77 |
| long, no reload | 74 % → 65 % | 33.2 px | 0.04 | 0.88 | 484 | quarters: 0.05 → 0.04 → 0.03 → 0.02

Numbers say: light vs heavy: width 66.4 → 81.1 px, dark 0.02 → 0.02.

## 0.45 · Eraser
Eraser · 30 px · 20.6 s · over bands of wet oil paint and oil pastel in turn (it works on paint already there: look at what it does to the bands; covered counts the bands too)

![0.45 · Eraser](0-45-Eraser.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 24 % → 24 % | 69.2 px | 0.82 | 1.00 | 47 |
| heavy line | 23 % → 23 % | 67.4 px | 0.81 | 1.00 | 55 |
| pressure swell | 23 % → 23 % | 86.7 px | 0.82 | 1.00 | 43 |
| fast wave | 21 % → 21 % | 24.7 px | 0.81 | 1.00 | 147 |
| slow wave | 20 % → 20 % | 23.5 px | 0.82 | 1.00 | 215 |
| spiral | 20 % → 20 % | 13.5 px | 0.79 | 1.00 | 211 |
| loop | 21 % → 21 % | 27.8 px | 0.80 | 1.00 | 115 |
| tilted | 23 % → 23 % | 64.8 px | 0.81 | 1.00 | 56 |
| over the wet one | 22 % → 22 % | 0.0 px | 0.81 | 1.00 | 53 |
| long, no reload | 17 % → 17 % | 7.5 px | 0.79 | 1.00 | 312 | quarters: 0.13 → 0.16 → 0.13 → 0.17

Numbers say: light vs heavy: width 69.2 → 67.4 px, dark 0.82 → 0.81; pressure barely changes the width; the long stroke does not run out of paint.

## Lift wet paint
Eraser · 30 px · 20.7 s · over bands of wet oil paint and oil pastel in turn (it works on paint already there: look at what it does to the bands; covered counts the bands too)

![Lift wet paint](Lift-wet-paint.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 24 % → 24 % | 70.1 px | 0.82 | 1.00 | 33 |
| heavy line | 24 % → 24 % | 69.8 px | 0.82 | 1.00 | 42 |
| pressure swell | 24 % → 24 % | 89.5 px | 0.82 | 1.00 | 38 |
| fast wave | 24 % → 24 % | 27.7 px | 0.82 | 1.00 | 108 |
| slow wave | 24 % → 24 % | 27.7 px | 0.82 | 1.00 | 187 |
| spiral | 24 % → 24 % | 15.9 px | 0.82 | 1.00 | 188 |
| loop | 24 % → 24 % | 31.1 px | 0.82 | 1.00 | 95 |
| tilted | 24 % → 24 % | 66.8 px | 0.82 | 1.00 | 59 |
| over the wet one | 24 % → 24 % | 0.0 px | 0.82 | 1.00 | 44 |
| long, no reload | 24 % → 24 % | 10.7 px | 0.82 | 1.00 | 262 | quarters: 0.18 → 0.24 → 0.17 → 0.24

Numbers say: light vs heavy: width 70.1 → 69.8 px, dark 0.82 → 0.82; pressure barely changes the width; the long stroke does not run out of paint.

## Sgraffito
Eraser · 10 px · 21.3 s · over bands of wet oil paint and oil pastel in turn (it works on paint already there: look at what it does to the bands; covered counts the bands too)

![Sgraffito](Sgraffito.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 24 % → 24 % | 69.5 px | 0.81 | 1.00 | 18 |
| heavy line | 24 % → 24 % | 69.5 px | 0.82 | 1.00 | 7 |
| pressure swell | 24 % → 24 % | 89.5 px | 0.82 | 1.00 | 6 |
| fast wave | 24 % → 24 % | 27.4 px | 0.82 | 1.00 | 18 |
| slow wave | 24 % → 24 % | 27.4 px | 0.81 | 1.00 | 40 |
| spiral | 24 % → 24 % | 15.7 px | 0.81 | 1.00 | 46 |
| loop | 24 % → 24 % | 30.9 px | 0.82 | 1.00 | 37 |
| tilted | 24 % → 24 % | 66.6 px | 0.82 | 1.00 | 10 |
| over the wet one | 24 % → 24 % | 0.0 px | 0.82 | 1.00 | 8 |
| long, no reload | 24 % → 24 % | 10.6 px | 0.82 | 1.00 | 47 | quarters: 0.17 → 0.24 → 0.17 → 0.24

Numbers say: light vs heavy: width 69.5 → 69.5 px, dark 0.81 → 0.82; pressure barely changes the width; the long stroke does not run out of paint.

## Brush Artist · Refs · #01 Henry Ward peach cloud
Gouache · 44 px · 37.0 s

![Brush Artist · Refs · #01 Henry Ward peach cloud](Brush-Artist-Refs-01-Henry-Ward-peach-cloud.png)

A light paint: laid on a grey sheet (on white it cannot be seen); **dark** = how far it is from the grey either way.

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 15 % → 12 % | 42.2 px | 0.32 | 0.80 | 138 |
| heavy line | 16 % → 13 % | 45.5 px | 0.32 | 0.84 | 144 |
| pressure swell | 12 % → 10 % | 44.0 px | 0.32 | 0.87 | 107 |
| fast wave | 37 % → 18 % | 43.1 px | 0.32 | 0.48 | 371 |
| slow wave | 37 % → 18 % | 43.1 px | 0.32 | 0.48 | 650 |
| spiral | 59 % → 19 % | 39.1 px | 0.32 | 0.32 | 1062 |
| loop | 32 % → 19 % | 41.3 px | 0.32 | 0.60 | 327 |
| tilted | 13 % → 13 % | 36.7 px | 0.32 | 0.99 | 241 |
| over the wet one | 27 % → 23 % | 38.9 px | 0.32 | 0.85 | 225 |
| long, no reload | 69 % → 20 % | 30.8 px | 0.32 | 0.29 | 1035 | quarters: 0.01 → 0.01 → 0.01 → 0.02

Numbers say: light vs heavy: width 42.2 → 45.5 px, dark 0.32 → 0.32; pressure barely changes the width; the long stroke does not run out of paint.

## Brush Artist · Refs · #02 Henry Ward cream strokes
Gouache · 46 px · 33.9 s

![Brush Artist · Refs · #02 Henry Ward cream strokes](Brush-Artist-Refs-02-Henry-Ward-cream-strokes.png)

A light paint: laid on a grey sheet (on white it cannot be seen); **dark** = how far it is from the grey either way.

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 14 % → 13 % | 40.8 px | 0.41 | 0.90 | 240 |
| heavy line | 15 % → 14 % | 43.9 px | 0.41 | 0.92 | 252 |
| pressure swell | 11 % → 11 % | 42.8 px | 0.41 | 0.94 | 102 |
| fast wave | 36 % → 18 % | 41.0 px | 0.40 | 0.50 | 573 |
| slow wave | 36 % → 18 % | 41.1 px | 0.40 | 0.49 | 706 |
| spiral | 58 % → 19 % | 38.1 px | 0.40 | 0.33 | 763 |
| loop | 31 % → 20 % | 39.7 px | 0.40 | 0.64 | 364 |
| tilted | 13 % → 13 % | 36.9 px | 0.41 | 0.99 | 206 |
| over the wet one | 27 % → 23 % | 37.9 px | 0.41 | 0.86 | 154 |
| long, no reload | 67 % → 21 % | 30.1 px | 0.40 | 0.31 | 944 | quarters: 0.01 → 0.01 → 0.01 → 0.02

Numbers say: light vs heavy: width 40.8 → 43.9 px, dark 0.41 → 0.41; pressure barely changes the width; the long stroke does not run out of paint.

## Brush Artist · Refs · #03 Henry Ward navy contours
Heavy acrylic · 22 px · 16.5 s

![Brush Artist · Refs · #03 Henry Ward navy contours](Brush-Artist-Refs-03-Henry-Ward-navy-contours.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 7 % → 7 % | 21.6 px | 0.70 | 0.94 | 75 |
| heavy line | 8 % → 8 % | 23.5 px | 0.70 | 0.95 | 78 |
| pressure swell | 6 % → 6 % | 23.2 px | 0.73 | 0.94 | 78 |
| fast wave | 19 % → 12 % | 21.8 px | 0.72 | 0.66 | 203 |
| slow wave | 19 % → 13 % | 22.5 px | 0.72 | 0.69 | 303 |
| spiral | 30 % → 13 % | 19.5 px | 0.72 | 0.45 | 344 |
| loop | 17 % → 13 % | 21.5 px | 0.72 | 0.81 | 167 |
| tilted | 8 % → 8 % | 22.6 px | 0.71 | 1.00 | 96 |
| over the wet one | 16 % → 14 % | 21.4 px | 0.71 | 0.89 | 78 |
| long, no reload | 34 % → 13 % | 15.1 px | 0.72 | 0.40 | 454 | quarters: 0.35 → 0.29 → 0.20 → 0.08

Numbers say: light vs heavy: width 21.6 → 23.5 px, dark 0.70 → 0.70; pressure barely changes the width.

## Brush Artist · Refs · #04 Henry Ward grey cloud
Gouache · 50 px · 33.8 s

![Brush Artist · Refs · #04 Henry Ward grey cloud](Brush-Artist-Refs-04-Henry-Ward-grey-cloud.png)

A light paint: laid on a grey sheet (on white it cannot be seen); **dark** = how far it is from the grey either way.

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 16 % → 14 % | 46.7 px | 0.31 | 0.85 | 166 |
| heavy line | 17 % → 15 % | 50.2 px | 0.31 | 0.89 | 210 |
| pressure swell | 13 % → 12 % | 48.7 px | 0.31 | 0.91 | 122 |
| fast wave | 40 % → 20 % | 46.5 px | 0.31 | 0.50 | 514 |
| slow wave | 40 % → 20 % | 46.5 px | 0.31 | 0.49 | 975 |
| spiral | 61 % → 21 % | 40.0 px | 0.31 | 0.34 | 731 |
| loop | 35 % → 22 % | 45.2 px | 0.31 | 0.64 | 378 |
| tilted | 14 % → 14 % | 40.0 px | 0.31 | 0.99 | 225 |
| over the wet one | 30 % → 26 % | 42.8 px | 0.31 | 0.87 | 193 |
| long, no reload | 73 % → 23 % | 32.7 px | 0.31 | 0.31 | 1064 | quarters: 0.01 → 0.01 → 0.01 → 0.02

Numbers say: light vs heavy: width 46.7 → 50.2 px, dark 0.31 → 0.31; pressure barely changes the width; the long stroke does not run out of paint.

## Brush Artist · Refs · #05 Henry Ward green in rust loops
Heavy acrylic · 20 px · 13.5 s

![Brush Artist · Refs · #05 Henry Ward green in rust loops](Brush-Artist-Refs-05-Henry-Ward-green-in-rust-loops.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 7 % → 6 % | 19.5 px | 0.55 | 0.94 | 75 |
| heavy line | 7 % → 7 % | 21.4 px | 0.55 | 0.94 | 79 |
| pressure swell | 6 % → 5 % | 21.5 px | 0.57 | 0.92 | 56 |
| fast wave | 17 % → 11 % | 19.8 px | 0.56 | 0.64 | 191 |
| slow wave | 18 % → 12 % | 20.4 px | 0.56 | 0.66 | 273 |
| spiral | 27 % → 11 % | 17.9 px | 0.55 | 0.42 | 325 |
| loop | 15 % → 12 % | 19.5 px | 0.55 | 0.80 | 184 |
| tilted | 8 % → 8 % | 21.7 px | 0.56 | 1.00 | 99 |
| over the wet one | 15 % → 13 % | 19.3 px | 0.56 | 0.87 | 79 |
| long, no reload | 30 % → 12 % | 13.4 px | 0.56 | 0.39 | 463 | quarters: 0.25 → 0.18 → 0.10 → 0.02

Numbers say: light vs heavy: width 19.5 → 21.4 px, dark 0.55 → 0.55; pressure barely changes the width.

## Brush Artist · Refs · #06 Henry Ward scrubbed grey
Gouache · 50 px · 33.4 s

![Brush Artist · Refs · #06 Henry Ward scrubbed grey](Brush-Artist-Refs-06-Henry-Ward-scrubbed-grey.png)

A light paint: laid on a grey sheet (on white it cannot be seen); **dark** = how far it is from the grey either way.

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 16 % → 14 % | 46.7 px | 0.33 | 0.85 | 152 |
| heavy line | 17 % → 15 % | 50.2 px | 0.33 | 0.89 | 155 |
| pressure swell | 13 % → 12 % | 48.7 px | 0.33 | 0.91 | 114 |
| fast wave | 40 % → 20 % | 46.5 px | 0.33 | 0.50 | 423 |
| slow wave | 40 % → 20 % | 46.5 px | 0.33 | 0.49 | 870 |
| spiral | 61 % → 21 % | 40.0 px | 0.33 | 0.34 | 954 |
| loop | 35 % → 22 % | 45.2 px | 0.32 | 0.64 | 365 |
| tilted | 14 % → 14 % | 40.0 px | 0.33 | 0.99 | 200 |
| over the wet one | 30 % → 26 % | 42.8 px | 0.33 | 0.87 | 161 |
| long, no reload | 73 % → 23 % | 32.7 px | 0.32 | 0.31 | 1009 | quarters: 0.01 → 0.01 → 0.01 → 0.02

Numbers say: light vs heavy: width 46.7 → 50.2 px, dark 0.33 → 0.33; pressure barely changes the width; the long stroke does not run out of paint.

## Brush Artist · Refs · #07 Henry Ward blue L + black zigzag
Heavy acrylic · 34 px · 16.1 s

![Brush Artist · Refs · #07 Henry Ward blue L + black zigzag](Brush-Artist-Refs-07-Henry-Ward-blue-L-black-zigzag.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 11 % → 11 % | 33.2 px | 0.57 | 0.93 | 100 |
| heavy line | 12 % → 12 % | 35.8 px | 0.57 | 0.93 | 107 |
| pressure swell | 9 % → 9 % | 35.2 px | 0.59 | 0.94 | 74 |
| fast wave | 29 % → 20 % | 33.6 px | 0.59 | 0.69 | 264 |
| slow wave | 30 % → 21 % | 34.2 px | 0.58 | 0.72 | 436 |
| spiral | 47 % → 22 % | 31.3 px | 0.58 | 0.46 | 600 |
| loop | 25 % → 21 % | 32.7 px | 0.58 | 0.82 | 239 |
| tilted | 11 % → 11 % | 29.9 px | 0.58 | 1.00 | 129 |
| over the wet one | 22 % → 20 % | 31.8 px | 0.58 | 0.91 | 120 |
| long, no reload | 53 % → 22 % | 23.8 px | 0.59 | 0.42 | 745 | quarters: 0.40 → 0.32 → 0.21 → 0.10

Numbers say: light vs heavy: width 33.2 → 35.8 px, dark 0.57 → 0.57; pressure barely changes the width.

## Brush Artist · Refs · #08 Henry Ward olive bands
Gouache · 34 px · 24.8 s

![Brush Artist · Refs · #08 Henry Ward olive bands](Brush-Artist-Refs-08-Henry-Ward-olive-bands.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 8 % → 2 % | 24.7 px | 0.57 | 0.27 | 72 |
| heavy line | 12 % → 3 % | 33.9 px | 0.57 | 0.22 | 151 |
| pressure swell | 8 % → 3 % | 30.8 px | 0.57 | 0.38 | 83 |
| fast wave | 25 % → 4 % | 29.2 px | 0.57 | 0.15 | 290 |
| slow wave | 25 % → 4 % | 28.9 px | 0.57 | 0.15 | 477 |
| spiral | 39 % → 4 % | 25.7 px | 0.57 | 0.10 | 455 |
| loop | 22 % → 5 % | 28.8 px | 0.57 | 0.21 | 317 |
| tilted | 10 % → 10 % | 28.6 px | 0.57 | 0.98 | 176 |
| over the wet one | 20 % → 8 % | 28.3 px | 0.57 | 0.40 | 134 |
| long, no reload | 45 % → 6 % | 20.0 px | 0.57 | 0.13 | 680 | quarters: 0.35 → 0.27 → 0.17 → 0.08

Numbers say: light vs heavy: width 24.7 → 33.9 px, dark 0.57 → 0.57.

## Brush Artist · Refs · #09 Henry Ward white loops
Gouache · 46 px · 34.4 s

![Brush Artist · Refs · #09 Henry Ward white loops](Brush-Artist-Refs-09-Henry-Ward-white-loops.png)

A light paint: laid on a grey sheet (on white it cannot be seen); **dark** = how far it is from the grey either way.

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 14 % → 13 % | 40.8 px | 0.43 | 0.90 | 150 |
| heavy line | 15 % → 14 % | 43.9 px | 0.43 | 0.92 | 156 |
| pressure swell | 11 % → 11 % | 42.8 px | 0.44 | 0.94 | 107 |
| fast wave | 36 % → 18 % | 41.0 px | 0.43 | 0.50 | 511 |
| slow wave | 36 % → 18 % | 41.1 px | 0.43 | 0.49 | 790 |
| spiral | 58 % → 19 % | 38.1 px | 0.42 | 0.33 | 666 |
| loop | 31 % → 20 % | 39.7 px | 0.42 | 0.64 | 333 |
| tilted | 13 % → 13 % | 36.9 px | 0.43 | 0.99 | 292 |
| over the wet one | 27 % → 23 % | 37.9 px | 0.43 | 0.86 | 262 |
| long, no reload | 67 % → 21 % | 30.1 px | 0.42 | 0.31 | 1311 | quarters: 0.01 → 0.01 → 0.01 → 0.02

Numbers say: light vs heavy: width 40.8 → 43.9 px, dark 0.43 → 0.43; pressure barely changes the width; the long stroke does not run out of paint.

## Brush Artist · Refs · #10 Henry Ward maroon loops
Heavy acrylic · 30 px · 16.4 s

![Brush Artist · Refs · #10 Henry Ward maroon loops](Brush-Artist-Refs-10-Henry-Ward-maroon-loops.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 10 % → 9 % | 28.0 px | 0.71 | 0.94 | 88 |
| heavy line | 10 % → 10 % | 30.3 px | 0.71 | 0.95 | 92 |
| pressure swell | 8 % → 8 % | 30.0 px | 0.73 | 0.94 | 64 |
| fast wave | 25 % → 17 % | 28.3 px | 0.73 | 0.71 | 222 |
| slow wave | 25 % → 18 % | 29.0 px | 0.73 | 0.73 | 471 |
| spiral | 39 % → 18 % | 26.0 px | 0.72 | 0.47 | 692 |
| loop | 21 % → 18 % | 27.6 px | 0.72 | 0.85 | 328 |
| tilted | 10 % → 10 % | 27.9 px | 0.72 | 1.00 | 212 |
| over the wet one | 20 % → 18 % | 27.0 px | 0.72 | 0.91 | 143 |
| long, no reload | 46 % → 18 % | 20.6 px | 0.73 | 0.40 | 625 | quarters: 0.44 → 0.38 → 0.31 → 0.22

Numbers say: light vs heavy: width 28.0 → 30.3 px, dark 0.71 → 0.71; pressure barely changes the width.

## Brush Artist · Refs · #11 Henry Ward purple spun balls
Heavy acrylic · 36 px · 18.2 s

![Brush Artist · Refs · #11 Henry Ward purple spun balls](Brush-Artist-Refs-11-Henry-Ward-purple-spun-balls.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 12 % → 11 % | 34.2 px | 0.71 | 0.96 | 110 |
| heavy line | 13 % → 12 % | 36.7 px | 0.71 | 0.95 | 109 |
| pressure swell | 10 % → 9 % | 36.2 px | 0.74 | 0.95 | 76 |
| fast wave | 30 % → 23 % | 34.6 px | 0.73 | 0.75 | 359 |
| slow wave | 30 % → 24 % | 35.0 px | 0.73 | 0.79 | 636 |
| spiral | 49 % → 25 % | 32.3 px | 0.73 | 0.50 | 473 |
| loop | 26 % → 23 % | 33.4 px | 0.73 | 0.88 | 236 |
| tilted | 11 % → 11 % | 31.2 px | 0.72 | 1.00 | 178 |
| over the wet one | 23 % → 21 % | 32.3 px | 0.72 | 0.93 | 146 |
| long, no reload | 55 % → 24 % | 24.8 px | 0.73 | 0.44 | 1007 | quarters: 0.51 → 0.46 → 0.39 → 0.28

Numbers say: light vs heavy: width 34.2 → 36.7 px, dark 0.71 → 0.71; pressure barely changes the width.

## Brush Artist · Refs · #12 Henry Ward black-olive cage
Gouache · 28 px · 26.3 s

![Brush Artist · Refs · #12 Henry Ward black-olive cage](Brush-Artist-Refs-12-Henry-Ward-black-olive-cage.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 7 % → 3 % | 20.9 px | 0.61 | 0.35 | 81 |
| heavy line | 9 % → 4 % | 26.1 px | 0.61 | 0.41 | 210 |
| pressure swell | 6 % → 4 % | 23.9 px | 0.61 | 0.61 | 66 |
| fast wave | 20 % → 4 % | 23.7 px | 0.61 | 0.19 | 219 |
| slow wave | 20 % → 4 % | 23.3 px | 0.61 | 0.21 | 504 |
| spiral | 32 % → 4 % | 21.4 px | 0.61 | 0.14 | 494 |
| loop | 18 % → 5 % | 22.8 px | 0.61 | 0.28 | 188 |
| tilted | 9 % → 9 % | 25.4 px | 0.61 | 0.98 | 110 |
| over the wet one | 17 % → 8 % | 21.8 px | 0.61 | 0.46 | 89 |
| long, no reload | 39 % → 6 % | 17.6 px | 0.61 | 0.15 | 538 | quarters: 0.31 → 0.26 → 0.19 → 0.10

Numbers say: light vs heavy: width 20.9 → 26.1 px, dark 0.61 → 0.61.

## Brush Artist · Refs · #13 Henry Ward blue streaky form
Gouache · 50 px · 47.7 s

![Brush Artist · Refs · #13 Henry Ward blue streaky form](Brush-Artist-Refs-13-Henry-Ward-blue-streaky-form.png)

A light paint: laid on a grey sheet (on white it cannot be seen); **dark** = how far it is from the grey either way.

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 16 % → 14 % | 46.7 px | 0.33 | 0.85 | 233 |
| heavy line | 17 % → 15 % | 50.2 px | 0.33 | 0.89 | 239 |
| pressure swell | 13 % → 12 % | 48.7 px | 0.33 | 0.91 | 137 |
| fast wave | 40 % → 20 % | 46.5 px | 0.33 | 0.50 | 455 |
| slow wave | 40 % → 20 % | 46.5 px | 0.33 | 0.49 | 1405 |
| spiral | 61 % → 21 % | 40.0 px | 0.32 | 0.34 | 979 |
| loop | 35 % → 22 % | 45.2 px | 0.32 | 0.64 | 443 |
| tilted | 14 % → 14 % | 40.0 px | 0.33 | 0.99 | 320 |
| over the wet one | 30 % → 26 % | 42.8 px | 0.33 | 0.87 | 288 |
| long, no reload | 73 % → 23 % | 32.7 px | 0.32 | 0.31 | 1449 | quarters: 0.01 → 0.01 → 0.01 → 0.02

Numbers say: light vs heavy: width 46.7 → 50.2 px, dark 0.33 → 0.33; pressure barely changes the width; the long stroke does not run out of paint.

## Brush Artist · Refs · #14 Henry Ward olive totem
Heavy acrylic · 48 px · 26.9 s

![Brush Artist · Refs · #14 Henry Ward olive totem](Brush-Artist-Refs-14-Henry-Ward-olive-totem.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 15 % → 15 % | 44.8 px | 0.31 | 0.94 | 293 |
| heavy line | 16 % → 16 % | 47.7 px | 0.31 | 0.95 | 315 |
| pressure swell | 13 % → 12 % | 47.0 px | 0.32 | 0.95 | 152 |
| fast wave | 38 % → 30 % | 43.9 px | 0.30 | 0.79 | 470 |
| slow wave | 39 % → 31 % | 44.6 px | 0.30 | 0.81 | 821 |
| spiral | 58 % → 32 % | 38.2 px | 0.30 | 0.55 | 848 |
| loop | 33 % → 29 % | 42.7 px | 0.30 | 0.89 | 497 |
| tilted | 13 % → 13 % | 37.5 px | 0.31 | 1.00 | 296 |
| over the wet one | 28 % → 26 % | 41.2 px | 0.31 | 0.93 | 266 |
| long, no reload | 68 % → 33 % | 30.3 px | 0.30 | 0.49 | 1271 | quarters: 0.25 → 0.18 → 0.10 → 0.03

Numbers say: light vs heavy: width 44.8 → 47.7 px, dark 0.31 → 0.31; pressure barely changes the width.

## Brush Artist · Refs · #15 Ultramarine brush script
Ink · 6 px · 31.8 s

![Brush Artist · Refs · #15 Ultramarine brush script](Brush-Artist-Refs-15-Ultramarine-brush-script.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 1 % → 4 % | 2.8 px | 0.53 | 3.61 | 34 |
| heavy line | 7 % → 7 % | 21.0 px | 0.61 | 0.99 | 83 |
| pressure swell | 4 % → 5 % | 15.1 px | 0.66 | 1.16 | 42 |
| fast wave | 12 % → 10 % | 14.2 px | 0.55 | 0.82 | 271 |
| slow wave | 10 % → 9 % | 11.5 px | 0.54 | 0.93 | 241 |
| spiral | 15 % → 10 % | 9.9 px | 0.52 | 0.66 | 279 |
| loop | 9 % → 9 % | 12.2 px | 0.54 | 0.99 | 121 |
| tilted | 3 % → 3 % | 9.2 px | 0.64 | 1.05 | 48 |
| over the wet one | 9 % → 9 % | 15.0 px | 0.64 | 1.07 | 77 |
| long, no reload | 22 % → 10 % | 9.8 px | 0.51 | 0.47 | 384 | quarters: 0.19 → 0.06 → 0.02 → 0.00

Numbers say: light vs heavy: width 2.8 → 21.0 px, dark 0.53 → 0.61; wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #18 Blue oil-stick scribbles
Pastel · 10 px · 18.0 s

![Brush Artist · Refs · #18 Blue oil-stick scribbles](Brush-Artist-Refs-18-Blue-oil-stick-scribbles.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 1 % → 1 % | 2.9 px | 0.52 | 1.00 | 46 |
| heavy line | 2 % → 2 % | 5.5 px | 0.53 | 1.00 | 68 |
| pressure swell | 1 % → 1 % | 5.0 px | 0.53 | 1.00 | 26 |
| fast wave | 4 % → 4 % | 4.8 px | 0.53 | 1.00 | 94 |
| slow wave | 4 % → 4 % | 4.4 px | 0.53 | 1.00 | 101 |
| spiral | 7 % → 7 % | 4.5 px | 0.52 | 1.00 | 120 |
| loop | 3 % → 3 % | 4.5 px | 0.52 | 1.00 | 93 |
| tilted | 2 % → 2 % | 4.7 px | 0.53 | 1.00 | 63 |
| over the wet one | 3 % → 3 % | 4.7 px | 0.53 | 1.00 | 32 |
| long, no reload | 10 % → 10 % | 4.4 px | 0.53 | 1.00 | 243 | quarters: 0.06 → 0.06 → 0.06 → 0.06

Numbers say: light vs heavy: width 2.9 → 5.5 px, dark 0.52 → 0.53; the long stroke does not run out of paint.

## Brush Artist · Refs · #20 Orange-red crayon scribble
Pastel · 14 px · 15.7 s

![Brush Artist · Refs · #20 Orange-red crayon scribble](Brush-Artist-Refs-20-Orange-red-crayon-scribble.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 1 % → 1 % | 4.0 px | 0.53 | 1.00 | 59 |
| heavy line | 3 % → 3 % | 8.0 px | 0.53 | 1.00 | 52 |
| pressure swell | 2 % → 2 % | 7.6 px | 0.53 | 1.00 | 33 |
| fast wave | 6 % → 6 % | 7.2 px | 0.53 | 1.00 | 148 |
| slow wave | 6 % → 6 % | 6.6 px | 0.53 | 1.00 | 153 |
| spiral | 9 % → 9 % | 6.2 px | 0.53 | 1.00 | 235 |
| loop | 5 % → 5 % | 6.2 px | 0.53 | 1.00 | 65 |
| tilted | 2 % → 2 % | 5.6 px | 0.53 | 1.00 | 35 |
| over the wet one | 4 % → 4 % | 6.6 px | 0.53 | 1.00 | 61 |
| long, no reload | 13 % → 13 % | 5.7 px | 0.53 | 1.00 | 222 | quarters: 0.07 → 0.07 → 0.08 → 0.08

Numbers say: light vs heavy: width 4.0 → 8.0 px, dark 0.53 → 0.53; the long stroke does not run out of paint.

## Brush Artist · Refs · #21 Gritty black contours
Gouache · 12 px · 29.2 s

![Brush Artist · Refs · #21 Gritty black contours](Brush-Artist-Refs-21-Gritty-black-contours.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 3 % → 0 % | 8.8 px | 0.79 | 0.12 | 129 |
| heavy line | 4 % → 0 % | 11.9 px | 0.79 | 0.10 | 225 |
| pressure swell | 3 % → 0 % | 11.6 px | 0.79 | 0.15 | 138 |
| fast wave | 7 % → 1 % | 8.5 px | 0.79 | 0.10 | 230 |
| slow wave | 8 % → 1 % | 9.0 px | 0.79 | 0.09 | 281 |
| spiral | 9 % → 1 % | 6.0 px | 0.79 | 0.10 | 419 |
| loop | 8 % → 1 % | 9.9 px | 0.79 | 0.09 | 382 |
| tilted | 4 % → 4 % | 10.8 px | 0.79 | 0.90 | 173 |
| over the wet one | 7 % → 1 % | 9.7 px | 0.79 | 0.17 | 160 |
| long, no reload | 7 % → 1 % | 3.3 px | 0.79 | 0.12 | 817 | quarters: 0.20 → 0.07 → 0.00 → 0.00

Numbers say: light vs heavy: width 8.8 → 11.9 px, dark 0.79 → 0.79.

## Brush Artist · Refs · #22 Bold black brush poster
Ink · 20 px · 37.0 s

![Brush Artist · Refs · #22 Bold black brush poster](Brush-Artist-Refs-22-Bold-black-brush-poster.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 3 % → 5 % | 9.5 px | 0.79 | 1.63 | 46 |
| heavy line | 15 % → 15 % | 44.6 px | 0.88 | 0.99 | 147 |
| pressure swell | 9 % → 9 % | 31.9 px | 0.87 | 1.04 | 70 |
| fast wave | 27 % → 26 % | 31.2 px | 0.87 | 0.98 | 198 |
| slow wave | 22 % → 21 % | 25.2 px | 0.87 | 0.98 | 252 |
| spiral | 34 % → 32 % | 22.2 px | 0.87 | 0.94 | 510 |
| loop | 20 % → 20 % | 26.2 px | 0.88 | 1.00 | 228 |
| tilted | 8 % → 8 % | 22.7 px | 0.88 | 1.01 | 134 |
| over the wet one | 19 % → 19 % | 30.5 px | 0.88 | 1.00 | 93 |
| long, no reload | 45 % → 38 % | 20.2 px | 0.86 | 0.84 | 684 | quarters: 0.54 → 0.45 → 0.35 → 0.27

Numbers say: light vs heavy: width 9.5 → 44.6 px, dark 0.79 → 0.88; wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #23 Dry white on orange + black line
Gouache · 50 px · 34.2 s

![Brush Artist · Refs · #23 Dry white on orange + black line](Brush-Artist-Refs-23-Dry-white-on-orange-black-line.png)

A light paint: laid on a grey sheet (on white it cannot be seen); **dark** = how far it is from the grey either way.

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 12 % → 2 % | 35.1 px | 0.39 | 0.13 | 174 |
| heavy line | 16 % → 2 % | 46.9 px | 0.39 | 0.11 | 351 |
| pressure swell | 11 % → 2 % | 42.6 px | 0.39 | 0.19 | 226 |
| fast wave | 34 % → 3 % | 39.7 px | 0.39 | 0.09 | 716 |
| slow wave | 34 % → 3 % | 39.0 px | 0.39 | 0.10 | 1453 |
| spiral | 49 % → 4 % | 32.6 px | 0.38 | 0.07 | 860 |
| loop | 30 % → 4 % | 39.1 px | 0.38 | 0.12 | 380 |
| tilted | 13 % → 12 % | 34.9 px | 0.38 | 0.98 | 238 |
| over the wet one | 26 % → 7 % | 38.0 px | 0.38 | 0.27 | 205 |
| long, no reload | 58 % → 5 % | 26.1 px | 0.38 | 0.09 | 1301 | quarters: 0.02 → 0.02 → 0.03 → 0.04

Numbers say: light vs heavy: width 35.1 → 46.9 px, dark 0.39 → 0.39; the long stroke does not run out of paint.

## Brush Artist · Refs · #24 Picasso flat oil
Oil · 34 px · 21.6 s

![Brush Artist · Refs · #24 Picasso flat oil](Brush-Artist-Refs-24-Picasso-flat-oil.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 11 % → 11 % | 32.4 px | 0.40 | 1.00 | 149 |
| heavy line | 12 % → 12 % | 35.2 px | 0.40 | 1.00 | 167 |
| pressure swell | 9 % → 9 % | 34.4 px | 0.41 | 1.00 | 137 |
| fast wave | 30 % → 30 % | 34.2 px | 0.41 | 1.00 | 476 |
| slow wave | 30 % → 30 % | 35.0 px | 0.41 | 1.00 | 773 |
| spiral | 51 % → 51 % | 33.8 px | 0.40 | 1.00 | 1069 |
| loop | 25 % → 25 % | 32.6 px | 0.41 | 1.00 | 511 |
| tilted | 11 % → 11 % | 32.0 px | 0.41 | 1.00 | 214 |
| over the wet one | 23 % → 23 % | 30.8 px | 0.41 | 1.00 | 164 |
| long, no reload | 62 % → 62 % | 27.6 px | 0.39 | 1.00 | 1066 | quarters: 0.28 → 0.28 → 0.26 → 0.24

Numbers say: light vs heavy: width 32.4 → 35.2 px, dark 0.40 → 0.40; pressure barely changes the width.

## Brush Artist · Refs · #25 Yellow heavy flat stroke
Heavy acrylic · 110 px · 52.0 s

![Brush Artist · Refs · #25 Yellow heavy flat stroke](Brush-Artist-Refs-25-Yellow-heavy-flat-stroke.png)

A light paint: laid on a grey sheet (on white it cannot be seen); **dark** = how far it is from the grey either way.

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 35 % → 36 % | 101.5 px | 0.30 | 1.02 | 559 |
| heavy line | 36 % → 35 % | 105.1 px | 0.31 | 0.97 | 588 |
| pressure swell | 28 % → 29 % | 105.4 px | 0.30 | 1.04 | 533 |
| fast wave | 73 % → 76 % | 83.8 px | 0.31 | 1.05 | 1459 |
| slow wave | 73 % → 72 % | 84.7 px | 0.30 | 0.98 | 3772 |
| spiral | 86 % → 83 % | 56.7 px | 0.29 | 0.97 | 2531 |
| loop | 65 % → 64 % | 83.6 px | 0.31 | 0.99 | 1316 |
| tilted | 26 % → 26 % | 71.5 px | 0.30 | 1.00 | 623 |
| over the wet one | 55 % → 54 % | 83.2 px | 0.30 | 0.97 | 609 |
| long, no reload | 98 % → 97 % | 44.1 px | 0.29 | 0.99 | 4148 | quarters: 0.00 → 0.00 → 0.00 → 0.00

Numbers say: light vs heavy: width 101.5 → 105.1 px, dark 0.30 → 0.31; pressure barely changes the width; the long stroke does not run out of paint.

## Brush Artist · Refs · #27 Orange impasto swatch
Heavy acrylic · 60 px · 32.3 s

![Brush Artist · Refs · #27 Orange impasto swatch](Brush-Artist-Refs-27-Orange-impasto-swatch.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 20 % → 19 % | 56.8 px | 0.34 | 0.97 | 262 |
| heavy line | 20 % → 20 % | 59.5 px | 0.34 | 0.97 | 232 |
| pressure swell | 16 % → 15 % | 59.6 px | 0.36 | 0.97 | 167 |
| fast wave | 48 % → 46 % | 55.0 px | 0.35 | 0.98 | 615 |
| slow wave | 48 % → 47 % | 55.9 px | 0.35 | 0.98 | 1100 |
| spiral | 69 % → 62 % | 45.5 px | 0.34 | 0.91 | 1085 |
| loop | 42 % → 40 % | 53.9 px | 0.35 | 0.97 | 525 |
| tilted | 16 % → 16 % | 44.0 px | 0.35 | 1.00 | 290 |
| over the wet one | 34 % → 33 % | 50.9 px | 0.35 | 0.96 | 279 |
| long, no reload | 85 % → 75 % | 38.1 px | 0.35 | 0.88 | 1995 | quarters: 0.33 → 0.31 → 0.29 → 0.26

Numbers say: light vs heavy: width 56.8 → 59.5 px, dark 0.34 → 0.34; pressure barely changes the width.

## Brush Artist · Refs · #28 Miles Davis black lines
Ink · 22 px · 39.0 s

![Brush Artist · Refs · #28 Miles Davis black lines](Brush-Artist-Refs-28-Miles-Davis-black-lines.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 4 % → 6 % | 12.2 px | 0.81 | 1.48 | 64 |
| heavy line | 17 % → 17 % | 49.1 px | 0.88 | 0.99 | 115 |
| pressure swell | 10 % → 10 % | 35.9 px | 0.87 | 1.03 | 82 |
| fast wave | 30 % → 30 % | 35.0 px | 0.87 | 0.98 | 211 |
| slow wave | 25 % → 25 % | 28.5 px | 0.87 | 0.99 | 330 |
| spiral | 38 % → 37 % | 25.3 px | 0.87 | 0.96 | 322 |
| loop | 23 % → 23 % | 29.4 px | 0.88 | 1.00 | 168 |
| tilted | 9 % → 9 % | 25.0 px | 0.88 | 1.01 | 137 |
| over the wet one | 21 % → 21 % | 34.1 px | 0.88 | 1.00 | 103 |
| long, no reload | 51 % → 43 % | 22.7 px | 0.86 | 0.85 | 530 | quarters: 0.59 → 0.51 → 0.40 → 0.31

Numbers say: light vs heavy: width 12.2 → 49.1 px, dark 0.81 → 0.88.

## Brush Artist · Refs · #29 Shrigley magenta asterisk
Watercolor · 70 px · 36.2 s

![Brush Artist · Refs · #29 Shrigley magenta asterisk](Brush-Artist-Refs-29-Shrigley-magenta-asterisk.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 10 % → 13 % | 28.0 px | 0.65 | 1.36 | 68 |
| heavy line | 17 % → 18 % | 50.3 px | 0.64 | 1.03 | 170 |
| pressure swell | 11 % → 12 % | 41.1 px | 0.65 | 1.13 | 143 |
| fast wave | 38 % → 38 % | 43.7 px | 0.64 | 1.00 | 566 |
| slow wave | 35 % → 39 % | 41.0 px | 0.65 | 1.10 | 494 |
| spiral | 61 % → 61 % | 40.0 px | 0.64 | 1.01 | 412 |
| loop | 31 % → 32 % | 40.2 px | 0.65 | 1.03 | 215 |
| tilted | 18 % → 18 % | 49.0 px | 0.65 | 1.00 | 209 |
| over the wet one | 31 % → 34 % | 38.4 px | 0.65 | 1.07 | 119 |
| long, no reload | 75 % → 75 % | 33.5 px | 0.64 | 1.00 | 767 | quarters: 0.55 → 0.53 → 0.52 → 0.49

Numbers say: light vs heavy: width 28.0 → 50.3 px, dark 0.65 → 0.64; the long stroke does not run out of paint.

## Brush Artist · Refs · #30 Red gouache face patch
Gouache · 60 px · 43.5 s

![Brush Artist · Refs · #30 Red gouache face patch](Brush-Artist-Refs-30-Red-gouache-face-patch.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 16 % → 15 % | 46.9 px | 0.49 | 0.91 | 164 |
| heavy line | 25 % → 20 % | 73.8 px | 0.49 | 0.80 | 225 |
| pressure swell | 19 % → 17 % | 72.6 px | 0.49 | 0.86 | 142 |
| fast wave | 48 % → 28 % | 55.1 px | 0.49 | 0.58 | 416 |
| slow wave | 48 % → 28 % | 55.3 px | 0.49 | 0.59 | 976 |
| spiral | 59 % → 28 % | 39.1 px | 0.49 | 0.48 | 1300 |
| loop | 40 % → 29 % | 51.3 px | 0.49 | 0.74 | 410 |
| tilted | 16 % → 16 % | 45.7 px | 0.49 | 1.01 | 248 |
| over the wet one | 36 % → 32 % | 55.3 px | 0.49 | 0.88 | 211 |
| long, no reload | 67 % → 30 % | 30.0 px | 0.49 | 0.45 | 1406 | quarters: 0.43 → 0.38 → 0.32 → 0.26

Numbers say: light vs heavy: width 46.9 → 73.8 px, dark 0.49 → 0.49.

## Brush Artist · Refs · #31 Warhol blotted line
Ink · 6 px · 24.3 s

![Brush Artist · Refs · #31 Warhol blotted line](Brush-Artist-Refs-31-Warhol-blotted-line.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 1 % → 3 % | 2.6 px | 0.75 | 3.30 | 37 |
| heavy line | 7 % → 7 % | 20.6 px | 0.83 | 0.97 | 56 |
| pressure swell | 4 % → 4 % | 14.8 px | 0.84 | 1.12 | 35 |
| fast wave | 12 % → 9 % | 13.8 px | 0.82 | 0.77 | 122 |
| slow wave | 10 % → 8 % | 11.2 px | 0.80 | 0.85 | 146 |
| spiral | 15 % → 9 % | 9.7 px | 0.80 | 0.58 | 317 |
| loop | 9 % → 9 % | 11.9 px | 0.80 | 0.94 | 165 |
| tilted | 3 % → 3 % | 8.6 px | 0.84 | 1.04 | 49 |
| over the wet one | 8 % → 8 % | 14.5 px | 0.84 | 1.02 | 72 |
| long, no reload | 21 % → 9 % | 9.6 px | 0.78 | 0.43 | 324 | quarters: 0.25 → 0.13 → 0.05 → 0.01

Numbers say: light vs heavy: width 2.6 → 20.6 px, dark 0.75 → 0.83; wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #32 Thick orange swipes
Heavy acrylic · 90 px · 39.9 s

![Brush Artist · Refs · #32 Thick orange swipes](Brush-Artist-Refs-32-Thick-orange-swipes.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 29 % → 29 % | 83.1 px | 0.38 | 1.00 | 306 |
| heavy line | 30 % → 29 % | 86.4 px | 0.38 | 0.97 | 373 |
| pressure swell | 23 % → 23 % | 86.5 px | 0.38 | 1.01 | 253 |
| fast wave | 63 % → 65 % | 73.1 px | 0.38 | 1.03 | 879 |
| slow wave | 64 % → 63 % | 73.5 px | 0.38 | 0.98 | 2755 |
| spiral | 79 % → 77 % | 52.2 px | 0.38 | 0.98 | 1653 |
| loop | 57 % → 56 % | 73.4 px | 0.38 | 0.99 | 808 |
| tilted | 21 % → 21 % | 59.3 px | 0.38 | 1.00 | 508 |
| over the wet one | 47 % → 45 % | 71.0 px | 0.38 | 0.97 | 448 |
| long, no reload | 95 % → 93 % | 42.8 px | 0.38 | 0.97 | 2547 | quarters: 0.38 → 0.38 → 0.37 → 0.35

Numbers say: light vs heavy: width 83.1 → 86.4 px, dark 0.38 → 0.38; pressure barely changes the width; the long stroke does not run out of paint.

## Brush Artist · Refs · #33 Red wet-in-wet band
Watercolor · 80 px · 58.2 s

![Brush Artist · Refs · #33 Red wet-in-wet band](Brush-Artist-Refs-33-Red-wet-in-wet-band.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 19 % → 34 % | 55.6 px | 0.53 | 1.77 | 108 |
| heavy line | 29 % → 42 % | 83.7 px | 0.56 | 1.47 | 214 |
| pressure swell | 19 % → 27 % | 71.5 px | 0.60 | 1.42 | 186 |
| fast wave | 58 % → 75 % | 67.4 px | 0.59 | 1.28 | 882 |
| slow wave | 57 % → 73 % | 65.6 px | 0.62 | 1.29 | 764 |
| spiral | 75 % → 89 % | 49.5 px | 0.62 | 1.19 | 772 |
| loop | 52 % → 71 % | 67.2 px | 0.58 | 1.37 | 406 |
| tilted | 24 % → 25 % | 66.5 px | 0.57 | 1.04 | 301 |
| over the wet one | 48 % → 72 % | 67.1 px | 0.57 | 1.50 | 170 |
| long, no reload | 95 % → 99 % | 42.4 px | 0.66 | 1.04 | 1764 | quarters: 0.68 → 0.68 → 0.68 → 0.64

Numbers say: light vs heavy: width 55.6 → 83.7 px, dark 0.53 → 0.56; the long stroke does not run out of paint; wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #34 Magenta oil patches
Oil · 60 px · 28.8 s

![Brush Artist · Refs · #34 Magenta oil patches](Brush-Artist-Refs-34-Magenta-oil-patches.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 19 % → 19 % | 55.8 px | 0.61 | 1.00 | 443 |
| heavy line | 21 % → 21 % | 59.9 px | 0.61 | 1.00 | 508 |
| pressure swell | 16 % → 16 % | 58.9 px | 0.62 | 1.01 | 225 |
| fast wave | 48 % → 49 % | 55.4 px | 0.62 | 1.02 | 814 |
| slow wave | 48 % → 48 % | 55.8 px | 0.62 | 1.00 | 1231 |
| spiral | 70 % → 70 % | 46.3 px | 0.62 | 1.00 | 1554 |
| loop | 42 % → 42 % | 54.3 px | 0.62 | 1.00 | 1023 |
| tilted | 17 % → 17 % | 46.8 px | 0.61 | 1.00 | 495 |
| over the wet one | 35 % → 35 % | 50.1 px | 0.61 | 1.00 | 286 |
| long, no reload | 86 % → 86 % | 38.7 px | 0.62 | 1.00 | 1963 | quarters: 0.59 → 0.58 → 0.57 → 0.52

Numbers say: light vs heavy: width 55.8 → 59.9 px, dark 0.61 → 0.61; pressure barely changes the width; the long stroke does not run out of paint.

## Brush Artist · Refs · #35 Red band with runs
Watercolor · 70 px · 61.8 s

![Brush Artist · Refs · #35 Red band with runs](Brush-Artist-Refs-35-Red-band-with-runs.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 17 % → 32 % | 48.3 px | 0.49 | 1.91 | 114 |
| heavy line | 25 % → 39 % | 73.9 px | 0.51 | 1.55 | 203 |
| pressure swell | 17 % → 25 % | 63.0 px | 0.55 | 1.47 | 184 |
| fast wave | 54 % → 72 % | 61.8 px | 0.52 | 1.34 | 452 |
| slow wave | 52 % → 70 % | 59.8 px | 0.55 | 1.35 | 648 |
| spiral | 72 % → 88 % | 47.3 px | 0.56 | 1.22 | 667 |
| loop | 47 % → 68 % | 61.0 px | 0.53 | 1.44 | 321 |
| tilted | 21 % → 22 % | 57.7 px | 0.51 | 1.06 | 253 |
| over the wet one | 43 % → 67 % | 62.0 px | 0.51 | 1.57 | 162 |
| long, no reload | 92 % → 98 % | 41.3 px | 0.59 | 1.07 | 1456 | quarters: 0.60 → 0.60 → 0.59 → 0.56

Numbers say: light vs heavy: width 48.3 → 73.9 px, dark 0.49 → 0.51; the long stroke does not run out of paint; wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #36 Magenta letters flat brush
Gouache · 36 px · 40.1 s

![Brush Artist · Refs · #36 Magenta letters flat brush](Brush-Artist-Refs-36-Magenta-letters-flat-brush.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 10 % → 10 % | 29.0 px | 0.45 | 0.98 | 113 |
| heavy line | 17 % → 14 % | 49.1 px | 0.45 | 0.85 | 122 |
| pressure swell | 13 % → 12 % | 49.4 px | 0.45 | 0.89 | 88 |
| fast wave | 35 % → 19 % | 40.3 px | 0.45 | 0.54 | 235 |
| slow wave | 35 % → 19 % | 39.9 px | 0.45 | 0.54 | 435 |
| spiral | 46 % → 19 % | 30.4 px | 0.45 | 0.42 | 493 |
| loop | 27 % → 20 % | 35.3 px | 0.45 | 0.72 | 285 |
| tilted | 11 % → 11 % | 29.8 px | 0.45 | 1.00 | 284 |
| over the wet one | 24 % → 22 % | 38.1 px | 0.45 | 0.92 | 180 |
| long, no reload | 46 % → 19 % | 20.8 px | 0.45 | 0.40 | 768 | quarters: 0.29 → 0.25 → 0.22 → 0.18

Numbers say: light vs heavy: width 29.0 → 49.1 px, dark 0.45 → 0.45.

## Brush Artist · Refs · #37 Oil still life dabs
Oil · 40 px · 18.2 s

![Brush Artist · Refs · #37 Oil still life dabs](Brush-Artist-Refs-37-Oil-still-life-dabs.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 13 % → 13 % | 38.0 px | 0.38 | 1.00 | 147 |
| heavy line | 14 % → 14 % | 41.1 px | 0.38 | 1.00 | 148 |
| pressure swell | 11 % → 11 % | 40.2 px | 0.40 | 1.00 | 107 |
| fast wave | 34 % → 34 % | 39.8 px | 0.39 | 1.00 | 372 |
| slow wave | 35 % → 35 % | 40.2 px | 0.39 | 1.00 | 614 |
| spiral | 59 % → 59 % | 38.7 px | 0.38 | 1.00 | 664 |
| loop | 29 % → 29 % | 37.8 px | 0.39 | 1.00 | 350 |
| tilted | 13 % → 13 % | 36.3 px | 0.39 | 1.00 | 199 |
| over the wet one | 26 % → 26 % | 35.8 px | 0.39 | 1.00 | 146 |
| long, no reload | 69 % → 69 % | 30.9 px | 0.37 | 1.00 | 1005 | quarters: 0.31 → 0.30 → 0.28 → 0.24

Numbers say: light vs heavy: width 38.0 → 41.1 px, dark 0.38 → 0.38; pressure barely changes the width.

## Brush Artist · Refs · #38 Sanguine drawing
Pastel · 6 px · 12.6 s

![Brush Artist · Refs · #38 Sanguine drawing](Brush-Artist-Refs-38-Sanguine-drawing.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 1 % → 1 % | 2.0 px | 0.61 | 1.00 | 46 |
| heavy line | 1 % → 1 % | 3.5 px | 0.62 | 1.00 | 21 |
| pressure swell | 1 % → 1 % | 3.3 px | 0.62 | 1.00 | 16 |
| fast wave | 3 % → 3 % | 3.2 px | 0.61 | 1.00 | 92 |
| slow wave | 3 % → 3 % | 3.0 px | 0.61 | 1.00 | 81 |
| spiral | 4 % → 4 % | 2.9 px | 0.61 | 1.00 | 139 |
| loop | 2 % → 2 % | 3.0 px | 0.61 | 1.00 | 113 |
| tilted | 1 % → 1 % | 3.4 px | 0.62 | 1.00 | 43 |
| over the wet one | 2 % → 2 % | 2.9 px | 0.62 | 1.00 | 34 |
| long, no reload | 7 % → 7 % | 3.0 px | 0.61 | 1.00 | 160 | quarters: 0.04 → 0.05 → 0.05 → 0.05

Numbers say: light vs heavy: width 2.0 → 3.5 px, dark 0.61 → 0.62; the long stroke does not run out of paint.

## Brush Artist · Refs · #39 Very thick impasto
Heavy acrylic · 60 px · 31.4 s

![Brush Artist · Refs · #39 Very thick impasto](Brush-Artist-Refs-39-Very-thick-impasto.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 20 % → 19 % | 56.9 px | 0.60 | 0.97 | 252 |
| heavy line | 21 % → 20 % | 59.6 px | 0.60 | 0.97 | 213 |
| pressure swell | 16 % → 15 % | 59.7 px | 0.62 | 0.97 | 154 |
| fast wave | 48 % → 47 % | 55.2 px | 0.62 | 0.98 | 603 |
| slow wave | 49 % → 47 % | 56.0 px | 0.62 | 0.98 | 1116 |
| spiral | 69 % → 65 % | 45.6 px | 0.62 | 0.93 | 1149 |
| loop | 42 % → 41 % | 54.0 px | 0.62 | 0.97 | 794 |
| tilted | 16 % → 16 % | 44.0 px | 0.61 | 1.00 | 557 |
| over the wet one | 34 % → 33 % | 51.0 px | 0.61 | 0.97 | 552 |
| long, no reload | 85 % → 79 % | 38.3 px | 0.62 | 0.92 | 1958 | quarters: 0.58 → 0.57 → 0.55 → 0.52

Numbers say: light vs heavy: width 56.9 → 59.6 px, dark 0.60 → 0.60; pressure barely changes the width; the long stroke does not run out of paint.

## Brush Artist · Refs · #40 Watercolour blooms
Watercolor · 90 px · 67.9 s

![Brush Artist · Refs · #40 Watercolour blooms](Brush-Artist-Refs-40-Watercolour-blooms.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 22 % → 37 % | 63.3 px | 0.09 | 1.70 | 244 |
| heavy line | 33 % → 46 % | 94.9 px | 0.10 | 1.41 | 401 |
| pressure swell | 22 % → 30 % | 84.1 px | 0.11 | 1.35 | 313 |
| fast wave | 64 % → 79 % | 73.9 px | 0.11 | 1.23 | 1385 |
| slow wave | 63 % → 77 % | 72.3 px | 0.15 | 1.23 | 1223 |
| spiral | 79 % → 91 % | 52.1 px | 0.15 | 1.16 | 1231 |
| loop | 57 % → 75 % | 73.6 px | 0.12 | 1.32 | 544 |
| tilted | 26 % → 27 % | 73.6 px | 0.12 | 1.04 | 675 |
| over the wet one | 53 % → 77 % | 74.1 px | 0.12 | 1.46 | 276 |
| long, no reload | 97 % → 99 % | 43.4 px | 0.17 | 1.03 | 1532 | quarters: 0.21 → 0.19 → 0.16 → 0.13

Numbers say: light vs heavy: width 63.3 → 94.9 px, dark 0.09 → 0.10; wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #41 Coloured pencil hatching
Pastel · 4 px · 11.9 s

![Brush Artist · Refs · #41 Coloured pencil hatching](Brush-Artist-Refs-41-Coloured-pencil-hatching.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 1 % → 1 % | 1.6 px | 0.42 | 1.00 | 16 |
| heavy line | 1 % → 1 % | 2.6 px | 0.43 | 1.00 | 24 |
| pressure swell | 1 % → 1 % | 2.1 px | 0.43 | 1.00 | 19 |
| fast wave | 2 % → 2 % | 2.2 px | 0.42 | 1.00 | 45 |
| slow wave | 2 % → 2 % | 2.1 px | 0.43 | 1.00 | 46 |
| spiral | 3 % → 3 % | 2.1 px | 0.43 | 1.00 | 91 |
| loop | 2 % → 2 % | 2.2 px | 0.43 | 1.00 | 32 |
| tilted | 1 % → 1 % | 3.0 px | 0.42 | 1.00 | 30 |
| over the wet one | 2 % → 2 % | 2.2 px | 0.42 | 1.00 | 32 |
| long, no reload | 5 % → 5 % | 2.3 px | 0.43 | 1.00 | 137 | quarters: 0.02 → 0.02 → 0.02 → 0.03

Numbers say: light vs heavy: width 1.6 → 2.6 px, dark 0.42 → 0.43; the long stroke does not run out of paint.

## Brush Artist · Refs · #42 Oil pastel shaggy
Pastel · 18 px · 12.3 s

![Brush Artist · Refs · #42 Oil pastel shaggy](Brush-Artist-Refs-42-Oil-pastel-shaggy.png)

A light paint: laid on a grey sheet (on white it cannot be seen); **dark** = how far it is from the grey either way.

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 2 % → 2 % | 5.1 px | 0.35 | 1.00 | 35 |
| heavy line | 4 % → 4 % | 10.7 px | 0.36 | 1.00 | 31 |
| pressure swell | 3 % → 3 % | 9.5 px | 0.36 | 1.00 | 19 |
| fast wave | 8 % → 8 % | 9.0 px | 0.36 | 1.00 | 68 |
| slow wave | 7 % → 7 % | 8.2 px | 0.36 | 1.00 | 98 |
| spiral | 12 % → 12 % | 7.7 px | 0.36 | 1.00 | 149 |
| loop | 6 % → 6 % | 7.9 px | 0.36 | 1.00 | 75 |
| tilted | 2 % → 2 % | 6.9 px | 0.36 | 1.00 | 58 |
| over the wet one | 6 % → 6 % | 8.5 px | 0.36 | 1.00 | 32 |
| long, no reload | 15 % → 15 % | 6.9 px | 0.36 | 1.00 | 222 | quarters: 0.00 → 0.00 → 0.00 → 0.00

Numbers say: light vs heavy: width 5.1 → 10.7 px, dark 0.35 → 0.36; the long stroke does not run out of paint.

## Brush Artist · Refs · #43 Dragged black ink blocks
Gouache · 70 px · 43.2 s

![Brush Artist · Refs · #43 Dragged black ink blocks](Brush-Artist-Refs-43-Dragged-black-ink-blocks.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 19 % → 5 % | 54.9 px | 0.57 | 0.28 | 236 |
| heavy line | 24 % → 9 % | 69.0 px | 0.57 | 0.38 | 515 |
| pressure swell | 17 % → 9 % | 63.4 px | 0.57 | 0.53 | 219 |
| fast wave | 51 % → 11 % | 58.7 px | 0.57 | 0.21 | 853 |
| slow wave | 50 % → 10 % | 58.1 px | 0.57 | 0.20 | 1365 |
| spiral | 65 % → 14 % | 42.6 px | 0.57 | 0.22 | 1341 |
| loop | 45 % → 12 % | 58.1 px | 0.57 | 0.27 | 635 |
| tilted | 17 % → 16 % | 46.4 px | 0.57 | 0.98 | 620 |
| over the wet one | 37 % → 20 % | 55.6 px | 0.57 | 0.56 | 485 |
| long, no reload | 82 % → 17 % | 36.6 px | 0.57 | 0.21 | 2098 | quarters: 0.54 → 0.52 → 0.47 → 0.40

Numbers say: light vs heavy: width 54.9 → 69.0 px, dark 0.57 → 0.57.

## Brush Artist · Refs · #44 Blue looping ribbon
Oil · 80 px · 36.3 s

![Brush Artist · Refs · #44 Blue looping ribbon](Brush-Artist-Refs-44-Blue-looping-ribbon.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 26 % → 27 % | 74.9 px | 0.72 | 1.04 | 396 |
| heavy line | 27 % → 27 % | 79.6 px | 0.72 | 1.00 | 387 |
| pressure swell | 21 % → 21 % | 78.1 px | 0.72 | 1.03 | 275 |
| fast wave | 61 % → 64 % | 70.3 px | 0.73 | 1.05 | 930 |
| slow wave | 61 % → 61 % | 70.0 px | 0.73 | 1.00 | 2791 |
| spiral | 78 % → 78 % | 51.3 px | 0.73 | 1.00 | 2008 |
| loop | 54 % → 54 % | 69.7 px | 0.73 | 1.00 | 873 |
| tilted | 21 % → 21 % | 57.3 px | 0.72 | 1.00 | 498 |
| over the wet one | 44 % → 44 % | 64.9 px | 0.72 | 1.00 | 477 |
| long, no reload | 96 % → 96 % | 42.8 px | 0.73 | 1.00 | 2701 | quarters: 0.72 → 0.73 → 0.73 → 0.69

Numbers say: light vs heavy: width 74.9 → 79.6 px, dark 0.72 → 0.72; pressure barely changes the width; the long stroke does not run out of paint.

## Brush Artist · Refs · #45 Soft pastel pepper
Pastel · 40 px · 16.2 s

![Brush Artist · Refs · #45 Soft pastel pepper](Brush-Artist-Refs-45-Soft-pastel-pepper.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 4 % → 4 % | 11.3 px | 0.53 | 1.00 | 76 |
| heavy line | 8 % → 8 % | 23.0 px | 0.53 | 1.00 | 73 |
| pressure swell | 5 % → 5 % | 19.5 px | 0.53 | 1.00 | 55 |
| fast wave | 17 % → 17 % | 19.4 px | 0.53 | 1.00 | 185 |
| slow wave | 15 % → 15 % | 17.1 px | 0.53 | 1.00 | 327 |
| spiral | 25 % → 25 % | 16.3 px | 0.53 | 1.00 | 311 |
| loop | 12 % → 12 % | 16.1 px | 0.53 | 1.00 | 172 |
| tilted | 5 % → 5 % | 12.8 px | 0.53 | 1.00 | 90 |
| over the wet one | 11 % → 11 % | 17.7 px | 0.53 | 1.00 | 76 |
| long, no reload | 30 % → 30 % | 13.6 px | 0.53 | 1.00 | 409 | quarters: 0.18 → 0.18 → 0.18 → 0.18

Numbers say: light vs heavy: width 11.3 → 23.0 px, dark 0.53 → 0.53; the long stroke does not run out of paint.

## Brush Artist · Refs · #46 Red-brown ink lips
Watercolor · 70 px · 64.6 s

![Brush Artist · Refs · #46 Red-brown ink lips](Brush-Artist-Refs-46-Red-brown-ink-lips.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 17 % → 31 % | 48.3 px | 0.60 | 1.88 | 121 |
| heavy line | 25 % → 39 % | 73.9 px | 0.62 | 1.53 | 235 |
| pressure swell | 17 % → 25 % | 63.0 px | 0.67 | 1.47 | 114 |
| fast wave | 54 % → 71 % | 61.8 px | 0.65 | 1.33 | 430 |
| slow wave | 52 % → 69 % | 59.8 px | 0.68 | 1.34 | 1090 |
| spiral | 72 % → 86 % | 47.3 px | 0.68 | 1.21 | 1208 |
| loop | 47 % → 66 % | 60.8 px | 0.65 | 1.41 | 383 |
| tilted | 21 % → 22 % | 57.5 px | 0.63 | 1.05 | 289 |
| over the wet one | 43 % → 66 % | 61.9 px | 0.63 | 1.54 | 196 |
| long, no reload | 92 % → 98 % | 41.2 px | 0.72 | 1.07 | 1086 | quarters: 0.73 → 0.73 → 0.73 → 0.70

Numbers say: light vs heavy: width 48.3 → 73.9 px, dark 0.60 → 0.62; the long stroke does not run out of paint; wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #47 Pink knife slabs
Heavy acrylic · 90 px · 41.6 s

![Brush Artist · Refs · #47 Pink knife slabs](Brush-Artist-Refs-47-Pink-knife-slabs.png)

A light paint: laid on a grey sheet (on white it cannot be seen); **dark** = how far it is from the grey either way.

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 28 % → 27 % | 81.1 px | 0.29 | 0.97 | 306 |
| heavy line | 29 % → 28 % | 83.5 px | 0.29 | 0.97 | 311 |
| pressure swell | 22 % → 22 % | 83.4 px | 0.29 | 1.01 | 195 |
| fast wave | 61 % → 60 % | 70.2 px | 0.28 | 0.98 | 726 |
| slow wave | 61 % → 59 % | 71.0 px | 0.27 | 0.96 | 3364 |
| spiral | 76 % → 58 % | 50.0 px | 0.27 | 0.76 | 1271 |
| loop | 55 % → 54 % | 71.7 px | 0.28 | 0.97 | 709 |
| tilted | 21 % → 21 % | 59.3 px | 0.29 | 1.00 | 356 |
| over the wet one | 46 % → 44 % | 68.0 px | 0.29 | 0.96 | 338 |
| long, no reload | 92 % → 76 % | 41.3 px | 0.26 | 0.83 | 1688 | quarters: 0.00 → 0.00 → 0.00 → 0.00

Numbers say: light vs heavy: width 81.1 → 83.5 px, dark 0.29 → 0.29; pressure barely changes the width; the long stroke does not run out of paint.

## Brush Artist · Refs · #48 Black bands with drips
Gouache · 70 px · 58.9 s

![Brush Artist · Refs · #48 Black bands with drips](Brush-Artist-Refs-48-Black-bands-with-drips.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 19 % → 18 % | 54.6 px | 0.69 | 0.93 | 250 |
| heavy line | 29 % → 24 % | 83.0 px | 0.69 | 0.84 | 346 |
| pressure swell | 23 % → 21 % | 86.1 px | 0.69 | 0.92 | 188 |
| fast wave | 53 % → 36 % | 61.8 px | 0.69 | 0.68 | 730 |
| slow wave | 53 % → 36 % | 61.7 px | 0.69 | 0.67 | 1749 |
| spiral | 64 % → 35 % | 41.9 px | 0.69 | 0.55 | 1188 |
| loop | 45 % → 36 % | 57.8 px | 0.69 | 0.81 | 645 |
| tilted | 19 % → 19 % | 52.3 px | 0.69 | 1.00 | 298 |
| over the wet one | 41 % → 38 % | 62.4 px | 0.69 | 0.92 | 261 |
| long, no reload | 74 % → 37 % | 33.3 px | 0.69 | 0.50 | 2404 | quarters: 0.64 → 0.61 → 0.54 → 0.45

Numbers say: light vs heavy: width 54.6 → 83.0 px, dark 0.69 → 0.69.

## Brush Artist · Refs · #49 Magenta letters round brush
Ink · 30 px · 48.5 s

![Brush Artist · Refs · #49 Magenta letters round brush](Brush-Artist-Refs-49-Magenta-letters-round-brush.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 6 % → 8 % | 17.5 px | 0.50 | 1.28 | 65 |
| heavy line | 21 % → 21 % | 62.0 px | 0.51 | 0.99 | 268 |
| pressure swell | 12 % → 13 % | 46.3 px | 0.52 | 1.01 | 118 |
| fast wave | 38 % → 38 % | 44.3 px | 0.51 | 0.99 | 255 |
| slow wave | 32 % → 31 % | 36.4 px | 0.51 | 0.99 | 412 |
| spiral | 50 % → 48 % | 32.8 px | 0.51 | 0.97 | 454 |
| loop | 29 % → 29 % | 37.6 px | 0.51 | 1.00 | 243 |
| tilted | 11 % → 11 % | 30.7 px | 0.52 | 1.01 | 106 |
| over the wet one | 26 % → 26 % | 42.1 px | 0.52 | 1.01 | 116 |
| long, no reload | 61 % → 56 % | 27.5 px | 0.51 | 0.92 | 573 | quarters: 0.41 → 0.36 → 0.30 → 0.25

Numbers say: light vs heavy: width 17.5 → 62.0 px, dark 0.50 → 0.51.

## Brush Artist · Refs · #50 Thick swipes on photo
Heavy acrylic · 40 px · 26.7 s

![Brush Artist · Refs · #50 Thick swipes on photo](Brush-Artist-Refs-50-Thick-swipes-on-photo.png)

A light paint: laid on a grey sheet (on white it cannot be seen); **dark** = how far it is from the grey either way.

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 13 % → 13 % | 38.1 px | 0.26 | 0.96 | 185 |
| heavy line | 14 % → 13 % | 40.2 px | 0.27 | 0.96 | 198 |
| pressure swell | 11 % → 10 % | 40.1 px | 0.25 | 0.95 | 132 |
| fast wave | 33 % → 31 % | 38.3 px | 0.25 | 0.93 | 627 |
| slow wave | 34 % → 32 % | 39.1 px | 0.26 | 0.95 | 766 |
| spiral | 58 % → 47 % | 38.5 px | 0.24 | 0.80 | 1027 |
| loop | 28 % → 27 % | 36.9 px | 0.26 | 0.95 | 556 |
| tilted | 12 % → 12 % | 34.0 px | 0.26 | 1.00 | 175 |
| over the wet one | 25 % → 24 % | 35.3 px | 0.26 | 0.95 | 162 |
| long, no reload | 66 % → 46 % | 29.6 px | 0.24 | 0.69 | 1018 | quarters: 0.00 → 0.00 → 0.00 → 0.00

Numbers say: light vs heavy: width 38.1 → 40.2 px, dark 0.26 → 0.27; pressure barely changes the width; the long stroke does not run out of paint.

## Brush Artist · Ink — wash
Watercolor · 38 px · 44.1 s

![Brush Artist · Ink — wash](Brush-Artist-Ink-wash.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 11 % → 11 % | 31.6 px | 0.38 | 1.03 | 83 |
| heavy line | 19 % → 19 % | 54.3 px | 0.32 | 1.03 | 133 |
| pressure swell | 12 % → 12 % | 45.1 px | 0.36 | 1.04 | 76 |
| fast wave | 39 % → 41 % | 44.7 px | 0.30 | 1.05 | 457 |
| slow wave | 37 % → 38 % | 42.6 px | 0.37 | 1.04 | 663 |
| spiral | 57 % → 60 % | 37.9 px | 0.30 | 1.04 | 478 |
| loop | 32 % → 33 % | 41.8 px | 0.34 | 1.02 | 172 |
| tilted | 13 % → 14 % | 36.8 px | 0.38 | 1.04 | 169 |
| over the wet one | 29 % → 30 % | 42.8 px | 0.38 | 1.04 | 151 |
| long, no reload | 65 % → 70 % | 29.2 px | 0.29 | 1.08 | 688 | quarters: 0.33 → 0.26 → 0.18 → 0.11

Numbers say: light vs heavy: width 31.6 → 54.3 px, dark 0.38 → 0.32.

## Brush Artist · Ink — brush line
Ink · 16 px · 36.5 s

![Brush Artist · Ink — brush line](Brush-Artist-Ink-brush-line.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 3 % → 5 % | 7.7 px | 0.78 | 1.80 | 64 |
| heavy line | 13 % → 13 % | 39.0 px | 0.88 | 0.99 | 113 |
| pressure swell | 8 % → 8 % | 28.4 px | 0.87 | 1.05 | 70 |
| fast wave | 24 % → 23 % | 27.6 px | 0.87 | 0.96 | 200 |
| slow wave | 19 % → 19 % | 22.5 px | 0.87 | 0.97 | 336 |
| spiral | 30 % → 27 % | 19.9 px | 0.86 | 0.90 | 530 |
| loop | 18 % → 18 % | 23.4 px | 0.88 | 1.00 | 181 |
| tilted | 7 % → 7 % | 20.1 px | 0.88 | 1.01 | 86 |
| over the wet one | 17 % → 17 % | 26.8 px | 0.88 | 1.00 | 79 |
| long, no reload | 42 % → 31 % | 18.8 px | 0.85 | 0.73 | 566 | quarters: 0.49 → 0.40 → 0.30 → 0.21

Numbers say: light vs heavy: width 7.7 → 39.0 px, dark 0.78 → 0.88; wet paint spreads well beyond the stroke.

## Brush Artist · Ink — dry brush
Gouache · 30 px · 30.8 s

![Brush Artist · Ink — dry brush](Brush-Artist-Ink-dry-brush.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 7 % → 1 % | 21.8 px | 0.71 | 0.11 | 88 |
| heavy line | 10 % → 1 % | 27.7 px | 0.71 | 0.10 | 177 |
| pressure swell | 7 % → 2 % | 25.5 px | 0.71 | 0.23 | 109 |
| fast wave | 21 % → 2 % | 24.2 px | 0.71 | 0.09 | 466 |
| slow wave | 21 % → 2 % | 23.9 px | 0.71 | 0.08 | 827 |
| spiral | 31 % → 2 % | 20.6 px | 0.71 | 0.06 | 589 |
| loop | 18 % → 2 % | 23.9 px | 0.71 | 0.13 | 312 |
| tilted | 9 % → 8 % | 24.1 px | 0.71 | 0.96 | 168 |
| over the wet one | 17 % → 4 % | 22.8 px | 0.71 | 0.24 | 140 |
| long, no reload | 31 % → 3 % | 14.0 px | 0.71 | 0.09 | 888 | quarters: 0.38 → 0.32 → 0.22 → 0.09

Numbers say: light vs heavy: width 21.8 → 27.7 px, dark 0.71 → 0.71.

## Brush Artist · Watercolour — blue
Watercolor · 40 px · 41.8 s

![Brush Artist · Watercolour — blue](Brush-Artist-Watercolour-blue.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 6 % → 10 % | 16.7 px | 0.25 | 1.70 | 53 |
| heavy line | 11 % → 12 % | 31.5 px | 0.25 | 1.13 | 74 |
| pressure swell | 7 % → 9 % | 25.4 px | 0.26 | 1.32 | 63 |
| fast wave | 24 % → 25 % | 27.8 px | 0.24 | 1.05 | 255 |
| slow wave | 22 % → 27 % | 25.9 px | 0.26 | 1.22 | 448 |
| spiral | 38 % → 41 % | 25.1 px | 0.22 | 1.08 | 304 |
| loop | 20 % → 22 % | 25.3 px | 0.26 | 1.13 | 159 |
| tilted | 12 % → 12 % | 33.3 px | 0.26 | 1.00 | 122 |
| over the wet one | 21 % → 24 % | 24.7 px | 0.26 | 1.15 | 68 |
| long, no reload | 51 % → 54 % | 23.0 px | 0.22 | 1.04 | 495 | quarters: 0.18 → 0.14 → 0.11 → 0.08

Numbers say: light vs heavy: width 16.7 → 31.5 px, dark 0.25 → 0.25; wet paint spreads well beyond the stroke.

## Brush Artist · Watercolour — violet
Watercolor · 40 px · 42.4 s

![Brush Artist · Watercolour — violet](Brush-Artist-Watercolour-violet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 6 % → 10 % | 16.7 px | 0.40 | 1.70 | 50 |
| heavy line | 11 % → 12 % | 31.5 px | 0.40 | 1.13 | 88 |
| pressure swell | 7 % → 9 % | 25.4 px | 0.41 | 1.32 | 56 |
| fast wave | 24 % → 25 % | 27.8 px | 0.38 | 1.05 | 172 |
| slow wave | 22 % → 27 % | 25.9 px | 0.40 | 1.22 | 334 |
| spiral | 38 % → 41 % | 25.1 px | 0.36 | 1.08 | 340 |
| loop | 20 % → 22 % | 25.3 px | 0.40 | 1.13 | 214 |
| tilted | 12 % → 12 % | 33.3 px | 0.40 | 1.00 | 170 |
| over the wet one | 21 % → 24 % | 24.7 px | 0.40 | 1.15 | 73 |
| long, no reload | 51 % → 54 % | 23.0 px | 0.34 | 1.04 | 787 | quarters: 0.28 → 0.22 → 0.17 → 0.14

Numbers say: light vs heavy: width 16.7 → 31.5 px, dark 0.40 → 0.40; wet paint spreads well beyond the stroke.

## Brush Artist · Watercolour — teal
Watercolor · 40 px · 40.9 s

![Brush Artist · Watercolour — teal](Brush-Artist-Watercolour-teal.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 6 % → 10 % | 16.7 px | 0.16 | 1.70 | 54 |
| heavy line | 11 % → 12 % | 31.5 px | 0.16 | 1.13 | 99 |
| pressure swell | 7 % → 9 % | 25.4 px | 0.17 | 1.32 | 72 |
| fast wave | 24 % → 25 % | 27.8 px | 0.15 | 1.05 | 242 |
| slow wave | 22 % → 27 % | 25.9 px | 0.17 | 1.22 | 332 |
| spiral | 38 % → 41 % | 25.1 px | 0.15 | 1.08 | 497 |
| loop | 20 % → 22 % | 25.3 px | 0.16 | 1.13 | 178 |
| tilted | 12 % → 12 % | 33.3 px | 0.16 | 1.00 | 142 |
| over the wet one | 21 % → 24 % | 24.7 px | 0.16 | 1.15 | 74 |
| long, no reload | 51 % → 54 % | 23.0 px | 0.14 | 1.04 | 457 | quarters: 0.11 → 0.09 → 0.07 → 0.06

Numbers say: light vs heavy: width 16.7 → 31.5 px, dark 0.16 → 0.16; wet paint spreads well beyond the stroke.

## Brush Artist · Gouache
Gouache · 30 px · 45.5 s

![Brush Artist · Gouache](Brush-Artist-Gouache.png)

A light paint: laid on a grey sheet (on white it cannot be seen); **dark** = how far it is from the grey either way.

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 8 % → 8 % | 24.4 px | 0.27 | 0.97 | 132 |
| heavy line | 15 % → 11 % | 42.8 px | 0.27 | 0.78 | 154 |
| pressure swell | 11 % → 9 % | 41.0 px | 0.27 | 0.84 | 101 |
| fast wave | 30 % → 13 % | 34.4 px | 0.26 | 0.45 | 267 |
| slow wave | 29 % → 14 % | 33.9 px | 0.26 | 0.46 | 463 |
| spiral | 40 % → 14 % | 26.6 px | 0.26 | 0.35 | 488 |
| loop | 23 % → 15 % | 30.4 px | 0.26 | 0.62 | 224 |
| tilted | 10 % → 10 % | 27.1 px | 0.26 | 1.01 | 168 |
| over the wet one | 21 % → 19 % | 32.8 px | 0.26 | 0.89 | 149 |
| long, no reload | 43 % → 15 % | 19.1 px | 0.26 | 0.35 | 735 | quarters: 0.01 → 0.01 → 0.01 → 0.01

Numbers say: light vs heavy: width 24.4 → 42.8 px, dark 0.27 → 0.27; the long stroke does not run out of paint.

## Brush Artist · Oil — bristle
Oil · 30 px · 20.3 s

![Brush Artist · Oil — bristle](Brush-Artist-Oil-bristle.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 9 % → 9 % | 26.3 px | 0.54 | 1.00 | 150 |
| heavy line | 10 % → 10 % | 28.6 px | 0.54 | 1.00 | 153 |
| pressure swell | 8 % → 8 % | 28.2 px | 0.55 | 1.00 | 130 |
| fast wave | 24 % → 24 % | 27.3 px | 0.55 | 1.00 | 398 |
| slow wave | 25 % → 25 % | 28.3 px | 0.55 | 1.00 | 682 |
| spiral | 39 % → 39 % | 25.6 px | 0.54 | 1.00 | 629 |
| loop | 20 % → 20 % | 26.3 px | 0.54 | 1.00 | 350 |
| tilted | 11 % → 11 % | 29.9 px | 0.53 | 1.00 | 276 |
| over the wet one | 20 % → 20 % | 25.5 px | 0.53 | 1.00 | 248 |
| long, no reload | 50 % → 50 % | 22.4 px | 0.54 | 1.00 | 1170 | quarters: 0.32 → 0.30 → 0.29 → 0.28

Numbers say: light vs heavy: width 26.3 → 28.6 px, dark 0.54 → 0.54; pressure barely changes the width; the long stroke does not run out of paint.

## Brush Artist · Charcoal — stick
Charcoal · 28 px · 14.0 s

![Brush Artist · Charcoal — stick](Brush-Artist-Charcoal-stick.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 3 % → 3 % | 8.4 px | 0.85 | 1.00 | 25 |
| heavy line | 6 % → 6 % | 17.8 px | 0.85 | 1.00 | 28 |
| pressure swell | 4 % → 4 % | 13.9 px | 0.85 | 1.00 | 24 |
| fast wave | 12 % → 12 % | 14.0 px | 0.85 | 1.00 | 78 |
| slow wave | 11 % → 11 % | 12.5 px | 0.85 | 1.00 | 176 |
| spiral | 19 % → 19 % | 12.7 px | 0.85 | 1.00 | 174 |
| loop | 10 % → 10 % | 12.8 px | 0.85 | 1.00 | 86 |
| tilted | 4 % → 4 % | 10.9 px | 0.85 | 1.00 | 70 |
| over the wet one | 9 % → 9 % | 13.5 px | 0.85 | 1.00 | 25 |
| long, no reload | 27 % → 27 % | 12.2 px | 0.85 | 1.00 | 189 | quarters: 0.26 → 0.25 → 0.26 → 0.27

Numbers say: light vs heavy: width 8.4 → 17.8 px, dark 0.85 → 0.85; the long stroke does not run out of paint.

## Brush Artist · Charcoal — stick B
Charcoal · 36 px · 15.5 s

![Brush Artist · Charcoal — stick B](Brush-Artist-Charcoal-stick-B.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 4 % → 4 % | 10.5 px | 0.85 | 1.00 | 47 |
| heavy line | 7 % → 7 % | 21.1 px | 0.85 | 1.00 | 68 |
| pressure swell | 4 % → 4 % | 16.5 px | 0.85 | 1.00 | 40 |
| fast wave | 15 % → 15 % | 16.8 px | 0.85 | 1.00 | 124 |
| slow wave | 13 % → 13 % | 14.7 px | 0.85 | 1.00 | 268 |
| spiral | 23 % → 23 % | 15.0 px | 0.85 | 1.00 | 173 |
| loop | 11 % → 11 % | 14.8 px | 0.85 | 1.00 | 66 |
| tilted | 4 % → 4 % | 12.3 px | 0.85 | 1.00 | 68 |
| over the wet one | 10 % → 10 % | 15.9 px | 0.85 | 1.00 | 39 |
| long, no reload | 31 % → 31 % | 13.9 px | 0.85 | 1.00 | 239 | quarters: 0.30 → 0.28 → 0.29 → 0.30

Numbers say: light vs heavy: width 10.5 → 21.1 px, dark 0.85 → 0.85; the long stroke does not run out of paint.

## Brush Artist · Charcoal — stick C
Charcoal · 22 px · 14.2 s

![Brush Artist · Charcoal — stick C](Brush-Artist-Charcoal-stick-C.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 2 % → 2 % | 6.9 px | 0.85 | 1.00 | 50 |
| heavy line | 5 % → 5 % | 15.3 px | 0.85 | 1.00 | 23 |
| pressure swell | 3 % → 3 % | 12.2 px | 0.85 | 1.00 | 23 |
| fast wave | 10 % → 10 % | 12.1 px | 0.85 | 1.00 | 67 |
| slow wave | 9 % → 9 % | 10.8 px | 0.85 | 1.00 | 91 |
| spiral | 17 % → 17 % | 11.0 px | 0.85 | 1.00 | 97 |
| loop | 9 % → 9 % | 11.4 px | 0.85 | 1.00 | 56 |
| tilted | 4 % → 4 % | 9.9 px | 0.85 | 1.00 | 38 |
| over the wet one | 8 % → 8 % | 11.7 px | 0.85 | 1.00 | 28 |
| long, no reload | 24 % → 24 % | 11.0 px | 0.85 | 1.00 | 148 | quarters: 0.24 → 0.22 → 0.23 → 0.24

Numbers say: light vs heavy: width 6.9 → 15.3 px, dark 0.85 → 0.85; the long stroke does not run out of paint.

## Brush Artist · Refs · #01 Henry Ward peach cloud — own sheet
own sheet 600 × 600 · Gouache · 44 px · 23.3 s

![Brush Artist · Refs · #01 Henry Ward peach cloud — own sheet](Brush-Artist-Refs-01-Henry-Ward-peach-cloud-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 16 % → 43 % | 45.1 px | 0.59 | 2.70 | 308 |
| stroke 2 | 27 % → 63 % | 88.6 px | 0.59 | 2.33 | 164 |
| stroke 3 | 31 % → 62 % | 90.6 px | 0.59 | 1.99 | 290 |
| stroke 4 | 34 % → 68 % | 109.8 px | 0.59 | 2.03 | 231 |
| stroke 5 | 33 % → 59 % | 95.9 px | 0.59 | 1.80 | 255 |
| stroke 6 | 33 % → 46 % | 100.5 px | 0.59 | 1.40 | 199 |
| stroke 7 | 18 % → 54 % | 44.9 px | 0.60 | 2.99 | 196 |
| stroke 8 | 19 % → 50 % | 48.5 px | 0.60 | 2.61 | 273 |
| stroke 9 | 23 % → 51 % | 58.2 px | 0.60 | 2.27 | 248 |
| stroke 10 | 25 % → 52 % | 67.0 px | 0.60 | 2.08 | 243 |
| stroke 11 | 27 % → 55 % | 77.1 px | 0.60 | 2.00 | 275 |
| stroke 12 | 31 % → 57 % | 93.0 px | 0.60 | 1.85 | 271 |
| stroke 13 | 39 % → 60 % | 113.7 px | 0.60 | 1.53 | 264 |
| stroke 14 | 41 % → 62 % | 118.3 px | 0.60 | 1.50 | 222 |
| stroke 15 | 55 % → 68 % | 163.9 px | 0.59 | 1.23 | 233 |
| stroke 16 | 57 % → 69 % | 171.7 px | 0.59 | 1.22 | 236 |
| stroke 17 | 57 % → 70 % | 160.2 px | 0.60 | 1.22 | 232 |
| stroke 18 | 58 % → 68 % | 169.1 px | 0.60 | 1.17 | 259 |
| stroke 19 | 60 % → 67 % | 167.7 px | 0.59 | 1.12 | 273 |
| stroke 20 | 59 % → 64 % | 170.4 px | 0.59 | 1.08 | 248 |
| stroke 21 | 59 % → 61 % | 171.3 px | 0.59 | 1.03 | 358 |
| stroke 22 | 60 % → 62 % | 176.0 px | 0.59 | 1.03 | 329 |
| stroke 23 | 60 % → 60 % | 171.0 px | 0.59 | 1.00 | 338 |
| stroke 24 | 64 % → 63 % | 190.6 px | 0.59 | 1.00 | 255 |

Numbers say: wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #02 Henry Ward cream strokes — own sheet
own sheet 600 × 600 · Gouache · 46 px · 14.9 s

![Brush Artist · Refs · #02 Henry Ward cream strokes — own sheet](Brush-Artist-Refs-02-Henry-Ward-cream-strokes-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 21 % → 39 % | 42.9 px | 0.71 | 1.87 | 360 |
| stroke 2 | 32 % → 45 % | 84.2 px | 0.71 | 1.40 | 357 |
| stroke 3 | 31 % → 52 % | 79.7 px | 0.72 | 1.68 | 341 |
| stroke 4 | 34 % → 49 % | 83.3 px | 0.71 | 1.45 | 393 |
| stroke 5 | 39 % → 52 % | 96.5 px | 0.72 | 1.33 | 346 |
| stroke 6 | 32 % → 46 % | 76.7 px | 0.71 | 1.47 | 355 |
| stroke 7 | 34 % → 32 % | 86.2 px | 0.71 | 0.95 | 303 |

Numbers say: wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #03 Henry Ward navy contours — own sheet
own sheet 600 × 600 · Heavy acrylic · 22 px · 4.0 s

![Brush Artist · Refs · #03 Henry Ward navy contours — own sheet](Brush-Artist-Refs-03-Henry-Ward-navy-contours-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 11 % → 18 % | 23.1 px | 0.69 | 1.56 | 224 |
| stroke 2 | 20 % → 23 % | 28.3 px | 0.69 | 1.14 | 138 |
| stroke 3 | 23 % → 23 % | 33.4 px | 0.69 | 1.01 | 196 |
| stroke 4 | 23 % → 21 % | 50.8 px | 0.69 | 0.92 | 223 |

Numbers say: wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #04 Henry Ward grey cloud — own sheet
own sheet 600 × 600 · Gouache · 50 px · 22.6 s

![Brush Artist · Refs · #04 Henry Ward grey cloud — own sheet](Brush-Artist-Refs-04-Henry-Ward-grey-cloud-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 17 % → 49 % | 48.9 px | 0.40 | 2.96 | 454 |
| stroke 2 | 20 % → 51 % | 57.9 px | 0.40 | 2.54 | 382 |
| stroke 3 | 29 % → 58 % | 81.5 px | 0.40 | 2.00 | 350 |
| stroke 4 | 32 % → 62 % | 93.4 px | 0.40 | 1.92 | 381 |
| stroke 5 | 38 % → 68 % | 116.0 px | 0.40 | 1.78 | 355 |
| stroke 6 | 41 % → 72 % | 135.7 px | 0.40 | 1.74 | 288 |
| stroke 7 | 48 % → 78 % | 140.2 px | 0.40 | 1.63 | 306 |
| stroke 8 | 46 % → 78 % | 137.7 px | 0.40 | 1.68 | 308 |
| stroke 9 | 47 % → 78 % | 142.1 px | 0.40 | 1.65 | 315 |
| stroke 10 | 48 % → 78 % | 153.4 px | 0.40 | 1.64 | 314 |
| stroke 11 | 48 % → 78 % | 135.7 px | 0.40 | 1.63 | 310 |
| stroke 12 | 49 % → 78 % | 147.0 px | 0.40 | 1.60 | 310 |
| stroke 13 | 48 % → 78 % | 137.3 px | 0.40 | 1.63 | 299 |
| stroke 14 | 49 % → 78 % | 144.8 px | 0.40 | 1.61 | 308 |
| stroke 15 | 49 % → 74 % | 140.0 px | 0.40 | 1.52 | 371 |
| stroke 16 | 49 % → 71 % | 148.6 px | 0.40 | 1.46 | 290 |
| stroke 17 | 48 % → 62 % | 137.0 px | 0.40 | 1.31 | 290 |
| stroke 18 | 47 % → 58 % | 154.0 px | 0.40 | 1.24 | 291 |
| stroke 19 | 48 % → 48 % | 142.0 px | 0.40 | 1.02 | 505 |
| stroke 20 | 48 % → 48 % | 152.3 px | 0.40 | 0.99 | 521 |

Numbers say: wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #05 Henry Ward green in rust loops — own sheet
own sheet 600 × 600 · Heavy acrylic · 20 px · 3.7 s

![Brush Artist · Refs · #05 Henry Ward green in rust loops — own sheet](Brush-Artist-Refs-05-Henry-Ward-green-in-rust-loops-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 12 % → 19 % | 20.9 px | 0.02 | 1.60 | 160 |
| stroke 2 | 12 % → 11 % | 23.5 px | 0.02 | 0.93 | 256 |
| stroke 3 | 23 % → 21 % | 41.5 px | 0.02 | 0.93 | 174 |

Numbers say: wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #06 Henry Ward scrubbed grey — own sheet
own sheet 600 × 600 · Gouache · 50 px · 26.0 s

![Brush Artist · Refs · #06 Henry Ward scrubbed grey — own sheet](Brush-Artist-Refs-06-Henry-Ward-scrubbed-grey-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 20 % → 56 % | 48.6 px | 0.40 | 2.83 | 510 |
| stroke 2 | 24 % → 58 % | 64.3 px | 0.40 | 2.41 | 517 |
| stroke 3 | 31 % → 63 % | 93.7 px | 0.40 | 2.04 | 582 |
| stroke 4 | 31 % → 63 % | 98.4 px | 0.40 | 2.01 | 587 |
| stroke 5 | 45 % → 78 % | 136.2 px | 0.40 | 1.71 | 532 |
| stroke 6 | 48 % → 78 % | 145.5 px | 0.40 | 1.64 | 403 |
| stroke 7 | 49 % → 78 % | 139.4 px | 0.40 | 1.61 | 343 |
| stroke 8 | 48 % → 78 % | 152.1 px | 0.40 | 1.63 | 370 |
| stroke 9 | 47 % → 78 % | 144.8 px | 0.40 | 1.67 | 278 |
| stroke 10 | 47 % → 79 % | 152.5 px | 0.40 | 1.68 | 258 |
| stroke 11 | 48 % → 79 % | 141.3 px | 0.40 | 1.63 | 308 |
| stroke 12 | 48 % → 79 % | 147.5 px | 0.40 | 1.63 | 348 |
| stroke 13 | 47 % → 78 % | 133.4 px | 0.40 | 1.66 | 347 |
| stroke 14 | 46 % → 78 % | 135.2 px | 0.40 | 1.69 | 365 |
| stroke 15 | 47 % → 78 % | 134.5 px | 0.40 | 1.67 | 305 |
| stroke 16 | 48 % → 78 % | 152.3 px | 0.40 | 1.65 | 294 |
| stroke 17 | 48 % → 72 % | 141.4 px | 0.40 | 1.52 | 328 |
| stroke 18 | 49 % → 70 % | 147.0 px | 0.40 | 1.43 | 297 |
| stroke 19 | 47 % → 63 % | 139.2 px | 0.40 | 1.36 | 331 |
| stroke 20 | 47 % → 61 % | 146.4 px | 0.40 | 1.30 | 331 |
| stroke 21 | 47 % → 52 % | 137.0 px | 0.40 | 1.10 | 326 |
| stroke 22 | 47 % → 47 % | 156.1 px | 0.40 | 0.99 | 290 |

Numbers say: wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #07 Henry Ward blue L + black zigzag — own sheet
own sheet 600 × 600 · Heavy acrylic · 34 px · 3.4 s

![Brush Artist · Refs · #07 Henry Ward blue L + black zigzag — own sheet](Brush-Artist-Refs-07-Henry-Ward-blue-L-black-zigzag-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 15 % → 17 % | 35.6 px | 0.59 | 1.14 | 312 |
| stroke 2 | 17 % → 16 % | 42.8 px | 0.59 | 0.93 | 159 |

## Brush Artist · Refs · #08 Henry Ward olive bands — own sheet
own sheet 600 × 600 · Gouache · 34 px · 7.9 s

![Brush Artist · Refs · #08 Henry Ward olive bands — own sheet](Brush-Artist-Refs-08-Henry-Ward-olive-bands-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 16 % → 16 % | 32.3 px | 0.57 | 1.03 | 230 |
| stroke 2 | 27 % → 21 % | 61.7 px | 0.57 | 0.76 | 251 |
| stroke 3 | 24 % → 29 % | 50.1 px | 0.57 | 1.23 | 246 |
| stroke 4 | 28 % → 26 % | 61.0 px | 0.57 | 0.91 | 306 |
| stroke 5 | 36 % → 31 % | 73.5 px | 0.57 | 0.87 | 271 |
| stroke 6 | 25 % → 15 % | 46.3 px | 0.57 | 0.61 | 215 |

## Brush Artist · Refs · #09 Henry Ward white loops — own sheet
own sheet 600 × 600 · Gouache · 46 px · 14.3 s

![Brush Artist · Refs · #09 Henry Ward white loops — own sheet](Brush-Artist-Refs-09-Henry-Ward-white-loops-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 29 % → 42 % | 15.7 px | 0.16 | 1.41 | 1538 |
| stroke 2 | 37 % → 36 % | 36.9 px | 0.17 | 0.97 | 2247 |
| stroke 3 | 43 % → 38 % | 39.6 px | 0.17 | 0.88 | 1667 |

## Brush Artist · Refs · #10 Henry Ward maroon loops — own sheet
own sheet 600 × 600 · Heavy acrylic · 30 px · 5.4 s

![Brush Artist · Refs · #10 Henry Ward maroon loops — own sheet](Brush-Artist-Refs-10-Henry-Ward-maroon-loops-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 12 % → 28 % | 28.7 px | 0.72 | 2.39 | 295 |
| stroke 2 | 22 % → 40 % | 48.5 px | 0.72 | 1.87 | 177 |
| stroke 3 | 29 % → 37 % | 58.5 px | 0.72 | 1.27 | 303 |
| stroke 4 | 41 % → 39 % | 92.8 px | 0.72 | 0.96 | 236 |
| stroke 5 | 34 % → 32 % | 85.8 px | 0.72 | 0.93 | 445 |

Numbers say: wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #11 Henry Ward purple spun balls — own sheet
own sheet 600 × 600 · Heavy acrylic · 36 px · 4.2 s

![Brush Artist · Refs · #11 Henry Ward purple spun balls — own sheet](Brush-Artist-Refs-11-Henry-Ward-purple-spun-balls-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 24 % → 35 % | 26.5 px | 0.68 | 1.43 | 336 |
| stroke 2 | 35 % → 46 % | 38.2 px | 0.68 | 1.33 | 368 |
| stroke 3 | 36 % → 34 % | 39.2 px | 0.68 | 0.97 | 358 |

## Brush Artist · Refs · #12 Henry Ward black-olive cage — own sheet
own sheet 600 × 600 · Gouache · 28 px · 8.9 s

![Brush Artist · Refs · #12 Henry Ward black-olive cage — own sheet](Brush-Artist-Refs-12-Henry-Ward-black-olive-cage-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 13 % → 21 % | 24.3 px | 0.59 | 1.64 | 363 |
| stroke 2 | 13 % → 22 % | 29.9 px | 0.59 | 1.76 | 292 |
| stroke 3 | 27 % → 28 % | 43.0 px | 0.59 | 1.04 | 395 |
| stroke 4 | 28 % → 27 % | 55.3 px | 0.59 | 0.98 | 245 |
| stroke 5 | 28 % → 18 % | 51.1 px | 0.59 | 0.65 | 204 |
| stroke 6 | 44 % → 30 % | 84.4 px | 0.59 | 0.68 | 306 |

Numbers say: wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #13 Henry Ward blue streaky form — own sheet
own sheet 600 × 600 · Gouache · 50 px · 23.3 s

![Brush Artist · Refs · #13 Henry Ward blue streaky form — own sheet](Brush-Artist-Refs-13-Henry-Ward-blue-streaky-form-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 16 % → 48 % | 48.7 px | 0.05 | 3.02 | 363 |
| stroke 2 | 22 % → 52 % | 67.0 px | 0.05 | 2.38 | 400 |
| stroke 3 | 33 % → 64 % | 95.7 px | 0.05 | 1.93 | 357 |
| stroke 4 | 33 % → 64 % | 105.8 px | 0.05 | 1.96 | 308 |
| stroke 5 | 48 % → 78 % | 138.8 px | 0.05 | 1.64 | 419 |
| stroke 6 | 47 % → 79 % | 135.4 px | 0.05 | 1.66 | 470 |
| stroke 7 | 49 % → 78 % | 144.3 px | 0.05 | 1.60 | 426 |
| stroke 8 | 49 % → 78 % | 149.4 px | 0.05 | 1.58 | 411 |
| stroke 9 | 48 % → 78 % | 150.1 px | 0.05 | 1.61 | 288 |
| stroke 10 | 48 % → 78 % | 159.4 px | 0.05 | 1.60 | 263 |
| stroke 11 | 46 % → 78 % | 142.9 px | 0.05 | 1.67 | 283 |
| stroke 12 | 48 % → 78 % | 142.7 px | 0.05 | 1.63 | 302 |
| stroke 13 | 47 % → 77 % | 145.1 px | 0.05 | 1.66 | 309 |
| stroke 14 | 45 % → 77 % | 134.5 px | 0.05 | 1.71 | 319 |
| stroke 15 | 46 % → 76 % | 132.5 px | 0.06 | 1.65 | 343 |
| stroke 16 | 48 % → 75 % | 142.0 px | 0.06 | 1.58 | 326 |
| stroke 17 | 58 % → 75 % | 144.8 px | 0.06 | 1.29 | 305 |
| stroke 18 | 60 % → 75 % | 145.4 px | 0.06 | 1.25 | 323 |
| stroke 19 | 67 % → 74 % | 136.1 px | 0.06 | 1.11 | 281 |
| stroke 20 | 75 % → 74 % | 143.2 px | 0.06 | 0.99 | 334 |

Numbers say: wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #14 Henry Ward olive totem — own sheet
own sheet 600 × 600 · Heavy acrylic · 48 px · 10.3 s

![Brush Artist · Refs · #14 Henry Ward olive totem — own sheet](Brush-Artist-Refs-14-Henry-Ward-olive-totem-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 18 % → 46 % | 46.9 px | 0.38 | 2.58 | 215 |
| stroke 2 | 21 % → 50 % | 64.3 px | 0.38 | 2.44 | 197 |
| stroke 3 | 29 % → 52 % | 100.6 px | 0.38 | 1.78 | 199 |
| stroke 4 | 30 % → 54 % | 113.7 px | 0.38 | 1.80 | 269 |
| stroke 5 | 39 % → 63 % | 135.6 px | 0.38 | 1.63 | 307 |
| stroke 6 | 39 % → 65 % | 150.4 px | 0.38 | 1.68 | 246 |
| stroke 7 | 37 % → 61 % | 124.3 px | 0.38 | 1.66 | 221 |
| stroke 8 | 37 % → 63 % | 142.4 px | 0.38 | 1.69 | 259 |
| stroke 9 | 38 % → 63 % | 130.9 px | 0.38 | 1.67 | 239 |
| stroke 10 | 38 % → 62 % | 141.0 px | 0.38 | 1.62 | 232 |
| stroke 11 | 40 % → 65 % | 143.7 px | 0.38 | 1.60 | 272 |
| stroke 12 | 38 % → 65 % | 144.2 px | 0.38 | 1.70 | 188 |
| stroke 13 | 39 % → 66 % | 135.5 px | 0.38 | 1.72 | 166 |
| stroke 14 | 37 % → 62 % | 134.5 px | 0.38 | 1.68 | 181 |
| stroke 15 | 40 % → 66 % | 136.9 px | 0.38 | 1.65 | 194 |
| stroke 16 | 38 % → 64 % | 138.8 px | 0.38 | 1.66 | 195 |
| stroke 17 | 38 % → 62 % | 126.2 px | 0.38 | 1.65 | 186 |
| stroke 18 | 40 % → 66 % | 154.9 px | 0.38 | 1.64 | 183 |
| stroke 19 | 40 % → 60 % | 137.9 px | 0.38 | 1.52 | 199 |
| stroke 20 | 41 % → 55 % | 144.4 px | 0.38 | 1.34 | 186 |
| stroke 21 | 46 % → 55 % | 137.7 px | 0.38 | 1.18 | 162 |
| stroke 22 | 54 % → 53 % | 146.7 px | 0.38 | 0.99 | 182 |

Numbers say: wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #15 Ultramarine brush script — own sheet
own sheet 600 × 600 · Ink · 6 px · 12.2 s

![Brush Artist · Refs · #15 Ultramarine brush script — own sheet](Brush-Artist-Refs-15-Ultramarine-brush-script-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 39 % → 45 % | 10.6 px | 0.70 | 1.15 | 70 |
| stroke 2 | 40 % → 45 % | 10.5 px | 0.68 | 1.12 | 71 |
| stroke 3 | 40 % → 46 % | 10.9 px | 0.69 | 1.16 | 61 |
| stroke 4 | 41 % → 45 % | 10.3 px | 0.65 | 1.09 | 99 |
| stroke 5 | 39 % → 43 % | 10.2 px | 0.65 | 1.10 | 88 |
| stroke 6 | 37 % → 43 % | 11.3 px | 0.71 | 1.16 | 41 |
| stroke 7 | 41 % → 45 % | 10.3 px | 0.65 | 1.11 | 109 |
| stroke 8 | 39 % → 44 % | 11.0 px | 0.70 | 1.12 | 63 |
| stroke 9 | 39 % → 44 % | 10.6 px | 0.67 | 1.12 | 106 |
| stroke 10 | 38 % → 42 % | 10.8 px | 0.70 | 1.12 | 55 |
| stroke 11 | 41 % → 46 % | 11.0 px | 0.69 | 1.13 | 53 |
| stroke 12 | 41 % → 44 % | 10.3 px | 0.65 | 1.08 | 86 |
| stroke 13 | 40 % → 44 % | 10.2 px | 0.66 | 1.10 | 99 |
| stroke 14 | 37 % → 43 % | 11.1 px | 0.71 | 1.17 | 40 |
| stroke 15 | 38 % → 43 % | 11.3 px | 0.71 | 1.15 | 49 |
| stroke 16 | 39 % → 44 % | 11.0 px | 0.70 | 1.13 | 54 |
| stroke 17 | 37 % → 42 % | 11.0 px | 0.72 | 1.12 | 55 |
| stroke 18 | 39 % → 44 % | 10.8 px | 0.69 | 1.14 | 68 |
| stroke 19 | 36 % → 43 % | 11.5 px | 0.70 | 1.18 | 51 |
| stroke 20 | 38 % → 44 % | 11.5 px | 0.71 | 1.16 | 50 |
| stroke 21 | 42 % → 46 % | 10.4 px | 0.65 | 1.09 | 126 |
| stroke 22 | 47 % → 51 % | 8.3 px | 0.68 | 1.09 | 109 |
| stroke 23 | 39 % → 44 % | 10.6 px | 0.69 | 1.14 | 61 |
| stroke 24 | 37 % → 42 % | 11.1 px | 0.71 | 1.15 | 51 |
| stroke 25 | 41 % → 45 % | 10.7 px | 0.67 | 1.10 | 73 |
| stroke 26 | 42 % → 45 % | 10.2 px | 0.65 | 1.09 | 113 |

## Brush Artist · Refs · #18 Blue oil-stick scribbles — own sheet
own sheet 600 × 600 · Pastel · 10 px · 5.1 s

![Brush Artist · Refs · #18 Blue oil-stick scribbles — own sheet](Brush-Artist-Refs-18-Blue-oil-stick-scribbles-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 15 % → 31 % | 3.8 px | 0.49 | 2.11 | 203 |
| stroke 2 | 13 % → 37 % | 3.6 px | 0.49 | 2.73 | 261 |
| stroke 3 | 16 % → 26 % | 5.8 px | 0.49 | 1.66 | 269 |
| stroke 4 | 15 % → 29 % | 8.0 px | 0.49 | 1.88 | 269 |
| stroke 5 | 29 % → 34 % | 8.4 px | 0.49 | 1.19 | 228 |
| stroke 6 | 25 % → 26 % | 9.4 px | 0.49 | 1.02 | 225 |
| stroke 7 | 26 % → 32 % | 8.3 px | 0.49 | 1.24 | 236 |
| stroke 8 | 30 % → 30 % | 17.0 px | 0.49 | 1.00 | 247 |

Numbers say: wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #20 Orange-red crayon scribble — own sheet
own sheet 600 × 600 · Pastel · 14 px · 4.0 s

![Brush Artist · Refs · #20 Orange-red crayon scribble — own sheet](Brush-Artist-Refs-20-Orange-red-crayon-scribble-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 8 % → 18 % | 5.5 px | 0.59 | 2.46 | 354 |
| stroke 2 | 9 % → 23 % | 6.8 px | 0.59 | 2.48 | 303 |
| stroke 3 | 13 % → 21 % | 8.5 px | 0.59 | 1.64 | 198 |
| stroke 4 | 24 % → 32 % | 8.9 px | 0.59 | 1.34 | 218 |
| stroke 5 | 27 % → 27 % | 7.7 px | 0.59 | 1.00 | 233 |
| stroke 6 | 22 % → 22 % | 16.8 px | 0.59 | 1.00 | 288 |

Numbers say: wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #21 Gritty black contours — own sheet
own sheet 600 × 600 · Gouache · 12 px · 5.8 s

![Brush Artist · Refs · #21 Gritty black contours — own sheet](Brush-Artist-Refs-21-Gritty-black-contours-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 10 % → 8 % | 10.6 px | 0.36 | 0.84 | 256 |
| stroke 2 | 9 % → 5 % | 15.4 px | 0.36 | 0.57 | 242 |
| stroke 3 | 14 % → 4 % | 12.9 px | 0.36 | 0.28 | 215 |
| stroke 4 | 16 % → 8 % | 19.7 px | 0.36 | 0.50 | 213 |
| stroke 5 | 18 % → 8 % | 21.5 px | 0.36 | 0.47 | 123 |

## Brush Artist · Refs · #22 Bold black brush poster — own sheet
own sheet 600 × 600 · Ink · 20 px · 7.4 s

![Brush Artist · Refs · #22 Bold black brush poster — own sheet](Brush-Artist-Refs-22-Bold-black-brush-poster-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 22 % → 27 % | 36.3 px | 0.94 | 1.20 | 161 |
| stroke 2 | 27 % → 37 % | 41.4 px | 0.95 | 1.36 | 29 |
| stroke 3 | 28 % → 28 % | 43.6 px | 0.94 | 1.00 | 72 |
| stroke 4 | 27 % → 39 % | 53.8 px | 0.94 | 1.42 | 83 |
| stroke 5 | 25 % → 25 % | 42.9 px | 0.94 | 1.00 | 144 |

## Brush Artist · Refs · #23 Dry white on orange + black line — own sheet
own sheet 600 × 600 · Gouache · 50 px · 15.7 s

![Brush Artist · Refs · #23 Dry white on orange + black line — own sheet](Brush-Artist-Refs-23-Dry-white-on-orange-black-line-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 13 % → 35 % | 44.0 px | 0.44 | 2.78 | 202 |
| stroke 2 | 15 % → 32 % | 53.3 px | 0.44 | 2.13 | 251 |
| stroke 3 | 22 % → 35 % | 82.6 px | 0.44 | 1.59 | 225 |
| stroke 4 | 24 % → 39 % | 95.4 px | 0.44 | 1.61 | 218 |
| stroke 5 | 35 % → 47 % | 126.2 px | 0.44 | 1.36 | 247 |
| stroke 6 | 36 % → 51 % | 146.8 px | 0.44 | 1.43 | 222 |
| stroke 7 | 31 % → 50 % | 118.1 px | 0.44 | 1.61 | 205 |
| stroke 8 | 31 % → 48 % | 122.2 px | 0.44 | 1.52 | 208 |
| stroke 9 | 31 % → 48 % | 117.4 px | 0.44 | 1.54 | 207 |
| stroke 10 | 32 % → 49 % | 127.1 px | 0.43 | 1.51 | 242 |
| stroke 11 | 35 % → 51 % | 129.9 px | 0.43 | 1.48 | 250 |
| stroke 12 | 35 % → 50 % | 135.5 px | 0.44 | 1.45 | 293 |
| stroke 13 | 36 % → 53 % | 134.7 px | 0.43 | 1.45 | 356 |
| stroke 14 | 35 % → 52 % | 137.7 px | 0.43 | 1.48 | 379 |
| stroke 15 | 35 % → 47 % | 132.2 px | 0.43 | 1.33 | 315 |
| stroke 16 | 34 % → 41 % | 135.8 px | 0.43 | 1.19 | 374 |
| stroke 17 | 34 % → 34 % | 119.2 px | 0.43 | 1.01 | 293 |
| stroke 18 | 41 % → 36 % | 149.1 px | 0.43 | 0.88 | 242 |

Numbers say: wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #24 Picasso flat oil — own sheet
own sheet 600 × 600 · Oil · 34 px · 8.9 s

![Brush Artist · Refs · #24 Picasso flat oil — own sheet](Brush-Artist-Refs-24-Picasso-flat-oil-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 16 % → 45 % | 34.7 px | 0.23 | 2.74 | 162 |
| stroke 2 | 20 % → 48 % | 47.2 px | 0.24 | 2.40 | 185 |
| stroke 3 | 29 % → 59 % | 62.5 px | 0.23 | 2.07 | 164 |
| stroke 4 | 37 % → 65 % | 83.1 px | 0.23 | 1.76 | 216 |
| stroke 5 | 43 % → 71 % | 94.5 px | 0.23 | 1.65 | 165 |
| stroke 6 | 44 % → 66 % | 102.1 px | 0.23 | 1.50 | 183 |
| stroke 7 | 45 % → 66 % | 94.8 px | 0.23 | 1.46 | 180 |
| stroke 8 | 44 % → 66 % | 106.9 px | 0.23 | 1.50 | 171 |
| stroke 9 | 37 % → 62 % | 81.5 px | 0.23 | 1.67 | 240 |
| stroke 10 | 39 % → 62 % | 93.1 px | 0.23 | 1.58 | 222 |
| stroke 11 | 37 % → 60 % | 78.6 px | 0.23 | 1.62 | 354 |
| stroke 12 | 38 % → 61 % | 91.1 px | 0.23 | 1.60 | 281 |
| stroke 13 | 38 % → 67 % | 84.4 px | 0.23 | 1.76 | 314 |
| stroke 14 | 39 % → 69 % | 88.9 px | 0.23 | 1.75 | 321 |
| stroke 15 | 39 % → 62 % | 83.3 px | 0.23 | 1.58 | 274 |
| stroke 16 | 38 % → 55 % | 87.9 px | 0.23 | 1.43 | 339 |
| stroke 17 | 43 % → 48 % | 90.0 px | 0.23 | 1.12 | 277 |
| stroke 18 | 42 % → 42 % | 102.6 px | 0.23 | 1.00 | 240 |

Numbers say: wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #25 Yellow heavy flat stroke — own sheet
own sheet 600 × 600 · Heavy acrylic · 110 px · 5.1 s

![Brush Artist · Refs · #25 Yellow heavy flat stroke — own sheet](Brush-Artist-Refs-25-Yellow-heavy-flat-stroke-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 18 % → 18 % | 104.2 px | 0.17 | 0.98 | 1432 |

## Brush Artist · Refs · #27 Orange impasto swatch — own sheet
own sheet 600 × 600 · Heavy acrylic · 60 px · 5.0 s

![Brush Artist · Refs · #27 Orange impasto swatch — own sheet](Brush-Artist-Refs-27-Orange-impasto-swatch-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 8 % → 21 % | 61.8 px | 0.33 | 2.60 | 134 |
| stroke 2 | 7 % → 33 % | 62.5 px | 0.33 | 4.67 | 111 |
| stroke 3 | 25 % → 36 % | 245.4 px | 0.33 | 1.40 | 75 |
| stroke 4 | 10 % → 12 % | 69.5 px | 0.33 | 1.25 | 97 |
| stroke 5 | 17 % → 33 % | 63.5 px | 0.33 | 1.90 | 106 |
| stroke 6 | 18 % → 31 % | 145.0 px | 0.33 | 1.79 | 78 |
| stroke 7 | 8 % → 15 % | 70.2 px | 0.33 | 1.86 | 75 |
| stroke 8 | 33 % → 34 % | 337.0 px | 0.33 | 1.04 | 62 |
| stroke 9 | 38 % → 37 % | 185.4 px | 0.33 | 0.98 | 147 |
| stroke 10 | 33 % → 33 % | 304.7 px | 0.33 | 0.98 | 74 |

Numbers say: wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #28 Miles Davis black lines — own sheet
own sheet 600 × 600 · Ink · 22 px · 10.3 s

![Brush Artist · Refs · #28 Miles Davis black lines — own sheet](Brush-Artist-Refs-28-Miles-Davis-black-lines-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 22 % → 32 % | 36.4 px | 0.88 | 1.42 | 295 |
| stroke 2 | 28 % → 48 % | 38.1 px | 0.88 | 1.73 | 180 |
| stroke 3 | 39 % → 44 % | 75.0 px | 0.88 | 1.12 | 174 |
| stroke 4 | 42 % → 48 % | 83.5 px | 0.88 | 1.15 | 269 |
| stroke 5 | 55 % → 55 % | 109.6 px | 0.88 | 1.00 | 206 |

Numbers say: wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #29 Shrigley magenta asterisk — own sheet
own sheet 600 × 600 · Watercolor · 70 px · 13.1 s

![Brush Artist · Refs · #29 Shrigley magenta asterisk — own sheet](Brush-Artist-Refs-29-Shrigley-magenta-asterisk-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 13 % → 37 % | 46.6 px | 0.72 | 2.85 | 292 |
| stroke 2 | 12 % → 12 % | 87.1 px | 0.71 | 1.00 | 260 |
| stroke 3 | 28 % → 37 % | 100.9 px | 0.72 | 1.31 | 271 |
| stroke 4 | 23 % → 23 % | 163.9 px | 0.71 | 1.02 | 408 |

Numbers say: wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #30 Red gouache face patch — own sheet
own sheet 600 × 600 · Gouache · 60 px · 21.5 s

![Brush Artist · Refs · #30 Red gouache face patch — own sheet](Brush-Artist-Refs-30-Red-gouache-face-patch-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 12 % → 37 % | 51.5 px | 0.53 | 3.23 | 236 |
| stroke 2 | 15 % → 40 % | 74.5 px | 0.53 | 2.72 | 195 |
| stroke 3 | 24 % → 50 % | 115.9 px | 0.53 | 2.06 | 200 |
| stroke 4 | 27 % → 51 % | 134.0 px | 0.53 | 1.93 | 261 |
| stroke 5 | 34 % → 60 % | 159.9 px | 0.53 | 1.77 | 449 |
| stroke 6 | 35 % → 61 % | 178.2 px | 0.53 | 1.76 | 381 |
| stroke 7 | 34 % → 59 % | 160.8 px | 0.53 | 1.73 | 384 |
| stroke 8 | 34 % → 56 % | 162.4 px | 0.53 | 1.65 | 474 |
| stroke 9 | 36 % → 60 % | 173.0 px | 0.53 | 1.66 | 269 |
| stroke 10 | 38 % → 62 % | 196.7 px | 0.53 | 1.64 | 257 |
| stroke 11 | 37 % → 61 % | 182.4 px | 0.53 | 1.66 | 295 |
| stroke 12 | 36 % → 58 % | 178.3 px | 0.53 | 1.62 | 570 |
| stroke 13 | 33 % → 46 % | 156.5 px | 0.53 | 1.39 | 507 |
| stroke 14 | 33 % → 41 % | 157.6 px | 0.53 | 1.25 | 616 |
| stroke 15 | 33 % → 37 % | 153.3 px | 0.53 | 1.12 | 502 |
| stroke 16 | 39 % → 39 % | 184.8 px | 0.53 | 0.99 | 368 |

Numbers say: wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #31 Warhol blotted line — own sheet
own sheet 600 × 600 · Ink · 6 px · 9.7 s

![Brush Artist · Refs · #31 Warhol blotted line — own sheet](Brush-Artist-Refs-31-Warhol-blotted-line-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 21 % → 42 % | 15.7 px | 0.82 | 1.98 | 156 |
| stroke 2 | 17 % → 23 % | 15.8 px | 0.82 | 1.34 | 212 |
| stroke 3 | 24 % → 25 % | 25.0 px | 0.82 | 1.02 | 193 |
| stroke 4 | 31 % → 40 % | 31.7 px | 0.82 | 1.28 | 157 |
| stroke 5 | 35 % → 43 % | 36.3 px | 0.82 | 1.23 | 211 |
| stroke 6 | 32 % → 33 % | 26.5 px | 0.81 | 1.03 | 186 |

Numbers say: wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #32 Thick orange swipes — own sheet
own sheet 600 × 600 · Heavy acrylic · 90 px · 6.1 s

![Brush Artist · Refs · #32 Thick orange swipes — own sheet](Brush-Artist-Refs-32-Thick-orange-swipes-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 14 % → 27 % | 86.0 px | 0.03 | 1.90 | 488 |
| stroke 2 | 26 % → 38 % | 176.9 px | 0.03 | 1.43 | 413 |
| stroke 3 | 28 % → 27 % | 177.5 px | 0.03 | 0.98 | 395 |

Numbers say: wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #33 Red wet-in-wet band — own sheet
own sheet 600 × 600 · Watercolor · 80 px · 14.9 s

![Brush Artist · Refs · #33 Red wet-in-wet band — own sheet](Brush-Artist-Refs-33-Red-wet-in-wet-band-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 23 % → 62 % | 88.2 px | 0.58 | 2.69 | 778 |
| stroke 2 | 31 % → 54 % | 250.0 px | 0.60 | 1.77 | 150 |
| stroke 3 | 38 % → 57 % | 367.0 px | 0.59 | 1.50 | 169 |
| stroke 4 | 44 % → 64 % | 426.5 px | 0.60 | 1.45 | 151 |
| stroke 5 | 44 % → 58 % | 369.6 px | 0.59 | 1.34 | 167 |
| stroke 6 | 44 % → 50 % | 337.5 px | 0.58 | 1.12 | 150 |

Numbers say: wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #34 Magenta oil patches — own sheet
own sheet 600 × 600 · Oil · 60 px · 6.9 s

![Brush Artist · Refs · #34 Magenta oil patches — own sheet](Brush-Artist-Refs-34-Magenta-oil-patches-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 9 % → 42 % | 61.9 px | 0.13 | 4.82 | 175 |
| stroke 2 | 9 % → 29 % | 62.8 px | 0.13 | 3.15 | 143 |
| stroke 3 | 7 % → 35 % | 62.3 px | 0.13 | 4.71 | 106 |
| stroke 4 | 16 % → 20 % | 132.0 px | 0.12 | 1.27 | 100 |
| stroke 5 | 23 % → 33 % | 124.6 px | 0.13 | 1.43 | 137 |
| stroke 6 | 20 % → 38 % | 171.4 px | 0.13 | 1.90 | 93 |
| stroke 7 | 30 % → 35 % | 237.9 px | 0.13 | 1.18 | 115 |
| stroke 8 | 33 % → 39 % | 235.0 px | 0.13 | 1.18 | 143 |
| stroke 9 | 25 % → 26 % | 159.7 px | 0.13 | 1.07 | 153 |
| stroke 10 | 29 % → 29 % | 257.2 px | 0.13 | 1.00 | 120 |
| stroke 11 | 36 % → 36 % | 324.6 px | 0.13 | 1.00 | 103 |
| stroke 12 | 26 % → 26 % | 184.4 px | 0.13 | 1.00 | 109 |

Numbers say: wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #35 Red band with runs — own sheet
own sheet 600 × 600 · Watercolor · 70 px · 8.2 s

![Brush Artist · Refs · #35 Red band with runs — own sheet](Brush-Artist-Refs-35-Red-band-with-runs-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 21 % → 32 % | 77.5 px | 0.50 | 1.54 | 399 |

Numbers say: wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #36 Magenta letters flat brush — own sheet
own sheet 600 × 600 · Gouache · 36 px · 16.9 s

![Brush Artist · Refs · #36 Magenta letters flat brush — own sheet](Brush-Artist-Refs-36-Magenta-letters-flat-brush-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 20 % → 39 % | 59.1 px | 0.50 | 1.95 | 44 |
| stroke 2 | 20 % → 32 % | 46.7 px | 0.50 | 1.59 | 50 |
| stroke 3 | 29 % → 54 % | 86.9 px | 0.50 | 1.86 | 43 |
| stroke 4 | 26 % → 44 % | 51.2 px | 0.50 | 1.67 | 160 |
| stroke 5 | 33 % → 55 % | 96.1 px | 0.50 | 1.67 | 94 |
| stroke 6 | 42 % → 56 % | 242.5 px | 0.50 | 1.33 | 21 |
| stroke 7 | 30 % → 44 % | 56.7 px | 0.50 | 1.45 | 178 |
| stroke 8 | 31 % → 53 % | 98.5 px | 0.50 | 1.68 | 110 |
| stroke 9 | 38 % → 51 % | 158.3 px | 0.50 | 1.33 | 50 |
| stroke 10 | 37 % → 63 % | 106.7 px | 0.50 | 1.72 | 172 |
| stroke 11 | 39 % → 62 % | 225.9 px | 0.50 | 1.58 | 35 |
| stroke 12 | 43 % → 56 % | 81.8 px | 0.50 | 1.29 | 240 |
| stroke 13 | 33 % → 46 % | 117.7 px | 0.50 | 1.43 | 59 |
| stroke 14 | 35 % → 52 % | 134.5 px | 0.50 | 1.47 | 59 |
| stroke 15 | 38 % → 56 % | 108.5 px | 0.50 | 1.49 | 210 |
| stroke 16 | 41 % → 50 % | 231.8 px | 0.50 | 1.23 | 26 |
| stroke 17 | 44 % → 52 % | 81.6 px | 0.50 | 1.19 | 188 |
| stroke 18 | 27 % → 36 % | 97.6 px | 0.50 | 1.35 | 44 |
| stroke 19 | 40 % → 39 % | 117.2 px | 0.50 | 0.96 | 51 |
| stroke 20 | 45 % → 45 % | 132.3 px | 0.50 | 0.98 | 53 |
| stroke 21 | 41 % → 39 % | 78.6 px | 0.50 | 0.96 | 120 |

Numbers say: wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #37 Oil still life dabs — own sheet
own sheet 600 × 600 · Oil · 40 px · 4.9 s

![Brush Artist · Refs · #37 Oil still life dabs — own sheet](Brush-Artist-Refs-37-Oil-still-life-dabs-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 7 % → 7 % | 44.1 px | 0.39 | 1.00 | 54 |
| stroke 2 | 6 % → 27 % | 44.4 px | 0.39 | 4.43 | 36 |
| stroke 3 | 12 % → 36 % | 92.6 px | 0.39 | 3.01 | 34 |
| stroke 4 | 9 % → 9 % | 42.7 px | 0.39 | 1.00 | 69 |
| stroke 5 | 6 % → 10 % | 43.2 px | 0.39 | 1.71 | 32 |
| stroke 6 | 13 % → 31 % | 83.4 px | 0.39 | 2.32 | 39 |
| stroke 7 | 11 % → 24 % | 115.5 px | 0.39 | 2.18 | 24 |
| stroke 8 | 8 % → 14 % | 89.6 px | 0.39 | 1.63 | 21 |
| stroke 9 | 13 % → 14 % | 68.1 px | 0.38 | 1.09 | 43 |
| stroke 10 | 21 % → 25 % | 106.5 px | 0.39 | 1.20 | 47 |
| stroke 11 | 24 % → 28 % | 201.6 px | 0.39 | 1.17 | 26 |
| stroke 12 | 21 % → 21 % | 227.4 px | 0.39 | 1.01 | 13 |
| stroke 13 | 16 % → 16 % | 167.7 px | 0.40 | 1.00 | 22 |
| stroke 14 | 16 % → 16 % | 132.7 px | 0.39 | 1.00 | 26 |

Numbers say: wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #38 Sanguine drawing — own sheet
own sheet 600 × 600 · Pastel · 6 px · 3.0 s

![Brush Artist · Refs · #38 Sanguine drawing — own sheet](Brush-Artist-Refs-38-Sanguine-drawing-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 3 % → 14 % | 2.9 px | 0.57 | 5.29 | 38 |
| stroke 2 | 3 % → 7 % | 2.9 px | 0.57 | 2.89 | 12 |
| stroke 3 | 3 % → 9 % | 2.9 px | 0.57 | 3.40 | 10 |
| stroke 4 | 2 % → 17 % | 2.7 px | 0.57 | 7.20 | 12 |
| stroke 5 | 2 % → 7 % | 2.7 px | 0.57 | 3.03 | 12 |
| stroke 6 | 3 % → 19 % | 3.4 px | 0.57 | 6.31 | 11 |
| stroke 7 | 5 % → 14 % | 5.2 px | 0.57 | 3.07 | 11 |
| stroke 8 | 4 % → 16 % | 4.7 px | 0.57 | 3.79 | 12 |
| stroke 9 | 3 % → 7 % | 2.9 px | 0.57 | 2.66 | 10 |
| stroke 10 | 4 % → 16 % | 4.7 px | 0.57 | 3.83 | 12 |
| stroke 11 | 3 % → 4 % | 2.9 px | 0.57 | 1.61 | 8 |
| stroke 12 | 4 % → 15 % | 4.8 px | 0.57 | 3.58 | 8 |
| stroke 13 | 8 % → 17 % | 8.9 px | 0.57 | 2.23 | 8 |
| stroke 14 | 4 % → 14 % | 4.9 px | 0.57 | 3.19 | 7 |
| stroke 15 | 9 % → 18 % | 10.7 px | 0.57 | 1.86 | 11 |
| stroke 16 | 6 % → 16 % | 6.6 px | 0.57 | 2.71 | 7 |
| stroke 17 | 4 % → 9 % | 4.4 px | 0.57 | 2.25 | 7 |
| stroke 18 | 3 % → 5 % | 2.9 px | 0.57 | 1.85 | 8 |
| stroke 19 | 6 % → 16 % | 6.9 px | 0.57 | 2.68 | 7 |
| stroke 20 | 8 % → 14 % | 9.2 px | 0.57 | 1.70 | 12 |
| stroke 21 | 4 % → 4 % | 4.3 px | 0.57 | 1.00 | 13 |
| stroke 22 | 8 % → 13 % | 8.6 px | 0.57 | 1.79 | 10 |
| stroke 23 | 7 % → 12 % | 8.3 px | 0.57 | 1.61 | 9 |
| stroke 24 | 4 % → 7 % | 4.7 px | 0.57 | 1.71 | 6 |
| stroke 25 | 8 % → 14 % | 8.7 px | 0.57 | 1.84 | 13 |
| stroke 26 | 6 % → 8 % | 6.5 px | 0.57 | 1.34 | 9 |
| stroke 27 | 4 % → 4 % | 4.3 px | 0.57 | 1.10 | 13 |
| stroke 28 | 7 % → 11 % | 8.2 px | 0.57 | 1.59 | 9 |
| stroke 29 | 8 % → 17 % | 8.8 px | 0.57 | 2.21 | 6 |
| stroke 30 | 13 % → 17 % | 14.9 px | 0.57 | 1.29 | 8 |
| stroke 31 | 5 % → 6 % | 5.4 px | 0.57 | 1.29 | 7 |
| stroke 32 | 10 % → 13 % | 11.8 px | 0.57 | 1.24 | 9 |
| stroke 33 | 7 % → 8 % | 8.5 px | 0.57 | 1.07 | 7 |
| stroke 34 | 11 % → 14 % | 12.0 px | 0.57 | 1.36 | 7 |
| stroke 35 | 9 % → 14 % | 10.0 px | 0.57 | 1.61 | 9 |
| stroke 36 | 10 % → 13 % | 11.4 px | 0.57 | 1.26 | 12 |
| stroke 37 | 9 % → 16 % | 10.5 px | 0.57 | 1.71 | 7 |
| stroke 38 | 13 % → 19 % | 14.8 px | 0.57 | 1.48 | 10 |
| stroke 39 | 14 % → 17 % | 15.7 px | 0.57 | 1.21 | 6 |
| stroke 40 | 6 % → 7 % | 7.2 px | 0.57 | 1.14 | 11 |
| stroke 41 | 16 % → 16 % | 17.7 px | 0.57 | 1.01 | 9 |
| stroke 42 | 14 % → 16 % | 15.2 px | 0.57 | 1.17 | 7 |
| stroke 43 | 10 % → 12 % | 11.6 px | 0.57 | 1.17 | 8 |
| stroke 44 | 12 % → 15 % | 14.3 px | 0.57 | 1.22 | 8 |
| stroke 45 | 2 % → 2 % | 2.7 px | 0.57 | 1.00 | 8 |
| stroke 46 | 16 % → 16 % | 18.5 px | 0.57 | 1.00 | 6 |
| stroke 47 | 13 % → 13 % | 15.0 px | 0.57 | 1.00 | 12 |
| stroke 48 | 12 % → 13 % | 14.3 px | 0.57 | 1.07 | 6 |
| stroke 49 | 19 % → 19 % | 21.5 px | 0.57 | 1.00 | 9 |
| stroke 50 | 10 % → 10 % | 11.6 px | 0.57 | 1.00 | 11 |

Numbers say: wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #39 Very thick impasto — own sheet
own sheet 600 × 600 · Heavy acrylic · 60 px · 6.1 s

![Brush Artist · Refs · #39 Very thick impasto — own sheet](Brush-Artist-Refs-39-Very-thick-impasto-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 26 % → 37 % | 59.6 px | 0.43 | 1.42 | 367 |
| stroke 2 | 31 % → 48 % | 93.9 px | 0.44 | 1.54 | 400 |
| stroke 3 | 37 % → 49 % | 124.6 px | 0.43 | 1.33 | 327 |
| stroke 4 | 31 % → 44 % | 90.9 px | 0.44 | 1.41 | 396 |
| stroke 5 | 42 % → 41 % | 104.2 px | 0.44 | 0.98 | 404 |

Numbers say: wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #40 Watercolour blooms — own sheet
own sheet 600 × 600 · Watercolor · 90 px · 9.7 s

![Brush Artist · Refs · #40 Watercolour blooms — own sheet](Brush-Artist-Refs-40-Watercolour-blooms-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 21 % → 28 % | 92.4 px | 0.11 | 1.32 | 1032 |

## Brush Artist · Refs · #41 Coloured pencil hatching — own sheet
own sheet 600 × 600 · Pastel · 4 px · 4.3 s

![Brush Artist · Refs · #41 Coloured pencil hatching — own sheet](Brush-Artist-Refs-41-Coloured-pencil-hatching-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 3 % → 13 % | 2.2 px | 0.35 | 4.64 | 7 |
| stroke 2 | 3 % → 7 % | 2.3 px | 0.35 | 2.29 | 12 |
| stroke 3 | 2 % → 11 % | 1.9 px | 0.35 | 4.38 | 8 |
| stroke 4 | 3 % → 19 % | 2.1 px | 0.35 | 6.73 | 9 |
| stroke 5 | 4 % → 7 % | 2.9 px | 0.35 | 1.83 | 4 |
| stroke 6 | 3 % → 13 % | 2.3 px | 0.35 | 4.19 | 5 |
| stroke 7 | 3 % → 15 % | 2.6 px | 0.35 | 4.43 | 5 |
| stroke 8 | 3 % → 12 % | 2.1 px | 0.35 | 4.20 | 5 |
| stroke 9 | 5 % → 11 % | 3.6 px | 0.35 | 2.27 | 6 |
| stroke 10 | 5 % → 15 % | 3.8 px | 0.35 | 2.99 | 7 |
| stroke 11 | 4 % → 13 % | 3.0 px | 0.35 | 3.28 | 8 |
| stroke 12 | 3 % → 3 % | 2.1 px | 0.35 | 1.00 | 4 |
| stroke 13 | 7 % → 17 % | 5.2 px | 0.35 | 2.45 | 5 |
| stroke 14 | 3 % → 13 % | 2.4 px | 0.35 | 4.19 | 7 |
| stroke 15 | 6 % → 12 % | 4.4 px | 0.35 | 2.09 | 5 |
| stroke 16 | 7 % → 11 % | 5.1 px | 0.35 | 1.61 | 5 |
| stroke 17 | 3 % → 3 % | 2.1 px | 0.35 | 1.00 | 7 |
| stroke 18 | 5 % → 8 % | 3.6 px | 0.35 | 1.65 | 8 |
| stroke 19 | 5 % → 13 % | 3.8 px | 0.35 | 2.72 | 9 |
| stroke 20 | 5 % → 14 % | 3.7 px | 0.35 | 2.92 | 5 |
| stroke 21 | 4 % → 13 % | 3.2 px | 0.35 | 3.20 | 4 |
| stroke 22 | 9 % → 16 % | 6.8 px | 0.35 | 1.77 | 10 |
| stroke 23 | 9 % → 13 % | 6.5 px | 0.35 | 1.55 | 5 |
| stroke 24 | 6 % → 14 % | 4.7 px | 0.35 | 2.18 | 4 |
| stroke 25 | 5 % → 10 % | 3.5 px | 0.35 | 2.27 | 7 |
| stroke 26 | 3 % → 6 % | 2.7 px | 0.35 | 1.81 | 9 |
| stroke 27 | 3 % → 7 % | 2.3 px | 0.35 | 2.26 | 18 |
| stroke 28 | 6 % → 10 % | 4.5 px | 0.35 | 1.70 | 4 |
| stroke 29 | 3 % → 13 % | 2.4 px | 0.35 | 4.21 | 5 |
| stroke 30 | 6 % → 9 % | 4.4 px | 0.35 | 1.46 | 4 |
| stroke 31 | 7 % → 14 % | 5.1 px | 0.35 | 2.14 | 4 |
| stroke 32 | 3 % → 6 % | 2.5 px | 0.35 | 1.79 | 4 |
| stroke 33 | 6 % → 11 % | 5.0 px | 0.35 | 1.67 | 8 |
| stroke 34 | 3 % → 6 % | 2.6 px | 0.35 | 1.73 | 5 |
| stroke 35 | 7 % → 14 % | 5.0 px | 0.35 | 2.09 | 8 |
| stroke 36 | 5 % → 5 % | 3.7 px | 0.35 | 1.01 | 5 |
| stroke 37 | 7 % → 15 % | 5.2 px | 0.35 | 2.15 | 6 |
| stroke 38 | 8 % → 13 % | 5.8 px | 0.35 | 1.66 | 5 |
| stroke 39 | 7 % → 11 % | 5.1 px | 0.35 | 1.67 | 5 |
| stroke 40 | 8 % → 18 % | 6.2 px | 0.35 | 2.21 | 8 |
| stroke 41 | 9 % → 13 % | 6.9 px | 0.35 | 1.48 | 6 |
| stroke 42 | 10 % → 17 % | 7.7 px | 0.35 | 1.73 | 10 |
| stroke 43 | 5 % → 9 % | 3.9 px | 0.35 | 1.66 | 7 |
| stroke 44 | 10 % → 13 % | 7.3 px | 0.35 | 1.40 | 10 |
| stroke 45 | 13 % → 18 % | 9.9 px | 0.35 | 1.35 | 5 |
| stroke 46 | 5 % → 7 % | 3.6 px | 0.34 | 1.41 | 7 |
| stroke 47 | 11 % → 13 % | 8.0 px | 0.35 | 1.20 | 6 |
| stroke 48 | 12 % → 16 % | 9.2 px | 0.35 | 1.34 | 7 |
| stroke 49 | 6 % → 9 % | 4.2 px | 0.35 | 1.66 | 6 |
| stroke 50 | 7 % → 7 % | 5.2 px | 0.34 | 1.00 | 7 |
| stroke 51 | 8 % → 15 % | 6.4 px | 0.35 | 1.74 | 6 |
| stroke 52 | 12 % → 14 % | 9.1 px | 0.35 | 1.19 | 11 |
| stroke 53 | 11 % → 14 % | 8.1 px | 0.35 | 1.36 | 9 |
| stroke 54 | 10 % → 14 % | 7.4 px | 0.35 | 1.47 | 10 |
| stroke 55 | 11 % → 14 % | 8.2 px | 0.35 | 1.33 | 7 |
| stroke 56 | 11 % → 12 % | 8.4 px | 0.35 | 1.11 | 6 |
| stroke 57 | 9 % → 13 % | 7.1 px | 0.35 | 1.37 | 6 |
| stroke 58 | 10 % → 11 % | 7.7 px | 0.35 | 1.14 | 7 |
| stroke 59 | 11 % → 13 % | 8.4 px | 0.35 | 1.18 | 5 |
| stroke 60 | 16 % → 20 % | 11.9 px | 0.35 | 1.26 | 8 |
| stroke 61 | 19 % → 20 % | 14.5 px | 0.35 | 1.04 | 12 |
| stroke 62 | 10 % → 10 % | 7.3 px | 0.35 | 1.00 | 6 |
| stroke 63 | 11 % → 12 % | 8.7 px | 0.35 | 1.07 | 6 |
| stroke 64 | 14 % → 14 % | 10.7 px | 0.35 | 1.02 | 7 |
| stroke 65 | 15 % → 15 % | 11.5 px | 0.35 | 1.00 | 6 |
| stroke 66 | 14 % → 14 % | 10.7 px | 0.35 | 1.00 | 11 |
| stroke 67 | 12 % → 12 % | 8.8 px | 0.35 | 1.06 | 11 |
| stroke 68 | 5 % → 9 % | 3.6 px | 0.35 | 1.88 | 14 |
| stroke 69 | 5 % → 5 % | 4.1 px | 0.35 | 1.00 | 10 |
| stroke 70 | 10 % → 13 % | 7.4 px | 0.35 | 1.28 | 8 |
| stroke 71 | 9 % → 11 % | 7.1 px | 0.35 | 1.15 | 8 |
| stroke 72 | 5 % → 7 % | 4.2 px | 0.35 | 1.23 | 5 |
| stroke 73 | 12 % → 12 % | 9.3 px | 0.35 | 1.00 | 5 |
| stroke 74 | 14 % → 14 % | 10.8 px | 0.35 | 1.00 | 11 |
| stroke 75 | 15 % → 15 % | 11.4 px | 0.35 | 1.00 | 9 |
| stroke 76 | 14 % → 14 % | 10.5 px | 0.35 | 1.00 | 10 |
| stroke 77 | 7 % → 10 % | 5.4 px | 0.35 | 1.34 | 9 |
| stroke 78 | 9 % → 9 % | 7.0 px | 0.35 | 1.00 | 7 |
| stroke 79 | 7 % → 7 % | 5.7 px | 0.35 | 1.00 | 11 |
| stroke 80 | 11 % → 11 % | 8.3 px | 0.35 | 1.00 | 8 |

Numbers say: wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #42 Oil pastel shaggy — own sheet
own sheet 600 × 600 · Pastel · 18 px · 3.7 s

![Brush Artist · Refs · #42 Oil pastel shaggy — own sheet](Brush-Artist-Refs-42-Oil-pastel-shaggy-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 5 % → 27 % | 8.0 px | 0.28 | 5.73 | 22 |
| stroke 2 | 5 % → 24 % | 8.6 px | 0.28 | 4.69 | 28 |
| stroke 3 | 5 % → 29 % | 8.9 px | 0.28 | 5.42 | 12 |
| stroke 4 | 5 % → 11 % | 8.8 px | 0.28 | 2.08 | 15 |
| stroke 5 | 6 % → 11 % | 9.9 px | 0.28 | 1.85 | 17 |
| stroke 6 | 8 % → 37 % | 13.9 px | 0.29 | 4.44 | 13 |
| stroke 7 | 11 % → 31 % | 17.6 px | 0.28 | 2.90 | 12 |
| stroke 8 | 7 % → 38 % | 11.4 px | 0.28 | 5.55 | 14 |
| stroke 9 | 8 % → 21 % | 13.9 px | 0.28 | 2.53 | 10 |
| stroke 10 | 8 % → 18 % | 13.2 px | 0.28 | 2.32 | 13 |
| stroke 11 | 6 % → 27 % | 9.4 px | 0.28 | 4.74 | 13 |
| stroke 12 | 8 % → 19 % | 13.6 px | 0.28 | 2.29 | 15 |
| stroke 13 | 13 % → 24 % | 21.0 px | 0.28 | 1.92 | 15 |
| stroke 14 | 5 % → 23 % | 7.9 px | 0.28 | 4.77 | 12 |
| stroke 15 | 5 % → 24 % | 9.0 px | 0.29 | 4.38 | 11 |
| stroke 16 | 9 % → 21 % | 15.7 px | 0.29 | 2.18 | 12 |
| stroke 17 | 17 % → 39 % | 27.9 px | 0.29 | 2.34 | 15 |
| stroke 18 | 14 % → 25 % | 22.8 px | 0.29 | 1.79 | 19 |
| stroke 19 | 15 % → 32 % | 24.9 px | 0.28 | 2.09 | 13 |
| stroke 20 | 21 % → 39 % | 35.1 px | 0.28 | 1.85 | 10 |
| stroke 21 | 9 % → 16 % | 14.4 px | 0.28 | 1.88 | 11 |
| stroke 22 | 14 % → 17 % | 23.9 px | 0.28 | 1.20 | 17 |
| stroke 23 | 12 % → 17 % | 20.6 px | 0.29 | 1.34 | 15 |
| stroke 24 | 18 % → 26 % | 30.0 px | 0.29 | 1.44 | 14 |
| stroke 25 | 20 % → 34 % | 32.6 px | 0.28 | 1.74 | 13 |
| stroke 26 | 6 % → 14 % | 9.2 px | 0.28 | 2.43 | 11 |
| stroke 27 | 18 % → 26 % | 30.4 px | 0.29 | 1.41 | 12 |
| stroke 28 | 14 % → 24 % | 23.7 px | 0.28 | 1.68 | 15 |
| stroke 29 | 9 % → 27 % | 14.9 px | 0.29 | 3.01 | 18 |
| stroke 30 | 15 % → 36 % | 24.9 px | 0.29 | 2.43 | 14 |
| stroke 31 | 14 % → 17 % | 23.3 px | 0.28 | 1.23 | 20 |
| stroke 32 | 16 % → 29 % | 27.0 px | 0.29 | 1.82 | 10 |
| stroke 33 | 15 % → 16 % | 24.5 px | 0.29 | 1.09 | 19 |
| stroke 34 | 19 % → 27 % | 31.4 px | 0.28 | 1.44 | 16 |
| stroke 35 | 26 % → 36 % | 42.5 px | 0.28 | 1.40 | 11 |
| stroke 36 | 25 % → 34 % | 41.0 px | 0.28 | 1.36 | 13 |
| stroke 37 | 12 % → 12 % | 19.3 px | 0.28 | 1.03 | 17 |
| stroke 38 | 19 % → 25 % | 31.7 px | 0.28 | 1.30 | 16 |
| stroke 39 | 16 % → 22 % | 27.3 px | 0.28 | 1.37 | 16 |
| stroke 40 | 22 % → 31 % | 36.6 px | 0.28 | 1.38 | 19 |
| stroke 41 | 32 % → 36 % | 53.1 px | 0.28 | 1.12 | 14 |
| stroke 42 | 23 % → 30 % | 38.1 px | 0.29 | 1.29 | 13 |
| stroke 43 | 12 % → 12 % | 20.3 px | 0.28 | 1.00 | 16 |
| stroke 44 | 30 % → 37 % | 48.9 px | 0.28 | 1.26 | 12 |
| stroke 45 | 16 % → 16 % | 26.2 px | 0.28 | 1.00 | 18 |
| stroke 46 | 29 % → 34 % | 47.9 px | 0.29 | 1.15 | 13 |
| stroke 47 | 38 % → 41 % | 62.0 px | 0.28 | 1.10 | 13 |
| stroke 48 | 29 % → 36 % | 47.8 px | 0.29 | 1.27 | 14 |
| stroke 49 | 27 % → 30 % | 45.1 px | 0.29 | 1.11 | 12 |
| stroke 50 | 38 % → 40 % | 63.4 px | 0.28 | 1.06 | 13 |
| stroke 51 | 16 % → 16 % | 26.0 px | 0.28 | 1.00 | 14 |
| stroke 52 | 37 % → 38 % | 62.4 px | 0.29 | 1.01 | 13 |
| stroke 53 | 22 % → 26 % | 36.9 px | 0.28 | 1.18 | 14 |
| stroke 54 | 17 % → 19 % | 29.0 px | 0.29 | 1.09 | 19 |
| stroke 55 | 15 % → 15 % | 25.0 px | 0.28 | 1.00 | 12 |
| stroke 56 | 13 % → 14 % | 21.6 px | 0.28 | 1.08 | 19 |
| stroke 57 | 23 % → 23 % | 37.7 px | 0.29 | 1.00 | 10 |
| stroke 58 | 28 % → 29 % | 46.1 px | 0.28 | 1.05 | 20 |
| stroke 59 | 40 % → 40 % | 67.3 px | 0.28 | 1.00 | 21 |
| stroke 60 | 22 % → 22 % | 35.6 px | 0.28 | 1.00 | 15 |

Numbers say: wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #43 Dragged black ink blocks — own sheet
own sheet 600 × 600 · Gouache · 70 px · 12.1 s

![Brush Artist · Refs · #43 Dragged black ink blocks — own sheet](Brush-Artist-Refs-43-Dragged-black-ink-blocks-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 29 % → 29 % | 66.4 px | 0.42 | 1.00 | 582 |
| stroke 2 | 30 % → 31 % | 105.8 px | 0.42 | 1.02 | 642 |
| stroke 3 | 37 % → 36 % | 132.0 px | 0.42 | 0.99 | 576 |
| stroke 4 | 37 % → 34 % | 128.9 px | 0.42 | 0.93 | 591 |
| stroke 5 | 44 % → 30 % | 103.8 px | 0.42 | 0.66 | 596 |

## Brush Artist · Refs · #44 Blue looping ribbon — own sheet
own sheet 600 × 600 · Oil · 80 px · 6.4 s

![Brush Artist · Refs · #44 Blue looping ribbon — own sheet](Brush-Artist-Refs-44-Blue-looping-ribbon-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 32 % → 32 % | 42.2 px | 0.78 | 1.00 | 3348 |

## Brush Artist · Refs · #45 Soft pastel pepper — own sheet
own sheet 600 × 600 · Pastel · 40 px · 4.4 s

![Brush Artist · Refs · #45 Soft pastel pepper — own sheet](Brush-Artist-Refs-45-Soft-pastel-pepper-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 10 % → 29 % | 11.3 px | 0.49 | 2.77 | 419 |
| stroke 2 | 18 % → 29 % | 21.3 px | 0.49 | 1.61 | 402 |
| stroke 3 | 25 % → 33 % | 17.6 px | 0.49 | 1.31 | 391 |
| stroke 4 | 24 % → 27 % | 30.5 px | 0.49 | 1.12 | 432 |
| stroke 5 | 30 % → 30 % | 21.2 px | 0.49 | 1.00 | 281 |

Numbers say: wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #46 Red-brown ink lips — own sheet
own sheet 600 × 600 · Watercolor · 70 px · 8.9 s

![Brush Artist · Refs · #46 Red-brown ink lips — own sheet](Brush-Artist-Refs-46-Red-brown-ink-lips-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 12 % → 33 % | 73.4 px | 0.60 | 2.75 | 266 |
| stroke 2 | 28 % → 38 % | 180.3 px | 0.59 | 1.34 | 254 |

Numbers say: wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #47 Pink knife slabs — own sheet
own sheet 600 × 600 · Heavy acrylic · 90 px · 6.9 s

![Brush Artist · Refs · #47 Pink knife slabs — own sheet](Brush-Artist-Refs-47-Pink-knife-slabs-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 17 % → 32 % | 83.2 px | 0.11 | 1.94 | 345 |
| stroke 2 | 29 % → 43 % | 165.7 px | 0.11 | 1.46 | 443 |
| stroke 3 | 29 % → 43 % | 165.6 px | 0.11 | 1.47 | 393 |
| stroke 4 | 39 % → 38 % | 165.6 px | 0.11 | 0.98 | 592 |

Numbers say: wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #48 Black bands with drips — own sheet
own sheet 600 × 600 · Gouache · 70 px · 14.8 s

![Brush Artist · Refs · #48 Black bands with drips — own sheet](Brush-Artist-Refs-48-Black-bands-with-drips-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 22 % → 40 % | 59.2 px | 0.39 | 1.82 | 785 |
| stroke 2 | 35 % → 48 % | 111.1 px | 0.39 | 1.38 | 663 |
| stroke 3 | 36 % → 47 % | 115.8 px | 0.39 | 1.32 | 698 |
| stroke 4 | 36 % → 34 % | 106.8 px | 0.39 | 0.95 | 673 |

Numbers say: wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #49 Magenta letters round brush — own sheet
own sheet 600 × 600 · Ink · 30 px · 14.3 s

![Brush Artist · Refs · #49 Magenta letters round brush — own sheet](Brush-Artist-Refs-49-Magenta-letters-round-brush-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 27 % → 46 % | 64.3 px | 0.52 | 1.69 | 54 |
| stroke 2 | 29 % → 40 % | 52.5 px | 0.53 | 1.39 | 53 |
| stroke 3 | 41 % → 67 % | 96.4 px | 0.52 | 1.64 | 55 |
| stroke 4 | 34 % → 52 % | 53.7 px | 0.52 | 1.55 | 163 |
| stroke 5 | 40 % → 66 % | 94.7 px | 0.52 | 1.65 | 127 |
| stroke 6 | 54 % → 70 % | 231.1 px | 0.52 | 1.29 | 21 |
| stroke 7 | 41 % → 56 % | 63.9 px | 0.52 | 1.35 | 170 |
| stroke 8 | 36 % → 61 % | 91.9 px | 0.53 | 1.72 | 85 |
| stroke 9 | 49 % → 60 % | 152.9 px | 0.53 | 1.24 | 42 |
| stroke 10 | 42 % → 72 % | 100.4 px | 0.52 | 1.71 | 127 |
| stroke 11 | 52 % → 72 % | 219.5 px | 0.52 | 1.39 | 31 |
| stroke 12 | 53 % → 68 % | 82.2 px | 0.52 | 1.29 | 155 |
| stroke 13 | 42 % → 54 % | 116.0 px | 0.53 | 1.29 | 33 |
| stroke 14 | 45 % → 69 % | 131.9 px | 0.53 | 1.52 | 40 |
| stroke 15 | 43 % → 63 % | 102.4 px | 0.52 | 1.46 | 90 |
| stroke 16 | 52 % → 61 % | 220.2 px | 0.52 | 1.18 | 31 |
| stroke 17 | 53 % → 64 % | 82.2 px | 0.52 | 1.19 | 152 |
| stroke 18 | 36 % → 44 % | 99.6 px | 0.52 | 1.21 | 41 |
| stroke 19 | 54 % → 53 % | 123.8 px | 0.52 | 0.99 | 30 |
| stroke 20 | 54 % → 54 % | 125.3 px | 0.52 | 1.00 | 29 |
| stroke 21 | 49 % → 49 % | 81.3 px | 0.52 | 1.00 | 107 |

Numbers say: wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #50 Thick swipes on photo — own sheet
own sheet 600 × 600 · Heavy acrylic · 40 px · 3.8 s

![Brush Artist · Refs · #50 Thick swipes on photo — own sheet](Brush-Artist-Refs-50-Thick-swipes-on-photo-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 9 % → 21 % | 42.6 px | 0.33 | 2.35 | 49 |
| stroke 2 | 9 % → 16 % | 42.4 px | 0.33 | 1.79 | 47 |
| stroke 3 | 10 % → 11 % | 41.8 px | 0.33 | 1.06 | 62 |
| stroke 4 | 11 % → 18 % | 42.6 px | 0.33 | 1.64 | 46 |
| stroke 5 | 11 % → 10 % | 41.8 px | 0.33 | 0.95 | 48 |
| stroke 6 | 17 % → 21 % | 97.3 px | 0.32 | 1.20 | 39 |
| stroke 7 | 22 % → 26 % | 92.7 px | 0.33 | 1.18 | 66 |
| stroke 8 | 21 % → 21 % | 119.6 px | 0.33 | 0.97 | 41 |
| stroke 9 | 9 % → 10 % | 42.0 px | 0.32 | 1.09 | 55 |
| stroke 10 | 22 % → 21 % | 73.6 px | 0.32 | 0.96 | 58 |
| stroke 11 | 9 % → 8 % | 42.6 px | 0.33 | 0.95 | 44 |
| stroke 12 | 17 % → 16 % | 93.0 px | 0.33 | 0.96 | 26 |

Numbers say: wet paint spreads well beyond the stroke.

## Brush Artist · Ink — dry brush — own sheet
own sheet 600 × 600 · Gouache · 30 px · 5.0 s

![Brush Artist · Ink — dry brush — own sheet](Brush-Artist-Ink-dry-brush-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| ear | 13 % → 4 % | 16.7 px | 0.82 | 0.32 | 701 |
| drag0 | 14 % → 16 % | 25.0 px | 0.82 | 1.22 | 184 |
| drag1 | 17 % → 18 % | 35.3 px | 0.82 | 1.02 | 168 |
| drag2 | 20 % → 18 % | 45.7 px | 0.82 | 0.91 | 178 |
| drag3 | 22 % → 19 % | 56.9 px | 0.82 | 0.84 | 135 |

## Brush Artist · Watercolour — blue — own sheet
own sheet 600 × 600 · Watercolor · 40 px · 20.0 s

![Brush Artist · Watercolour — blue — own sheet](Brush-Artist-Watercolour-blue-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| s0 | 7 % → 23 % | 28.4 px | 0.25 | 3.20 | 43 |
| s1 | 5 % → 32 % | 9.9 px | 0.38 | 5.84 | 54 |
| s2 | 10 % → 18 % | 43.5 px | 0.19 | 1.75 | 46 |
| s3 | 9 % → 17 % | 26.3 px | 0.28 | 1.85 | 67 |
| s4 | 14 % → 29 % | 37.9 px | 0.36 | 2.11 | 73 |
| s5 | 19 % → 29 % | 38.9 px | 0.37 | 1.51 | 80 |
| s6 | 17 % → 21 % | 47.6 px | 0.27 | 1.22 | 69 |
| s7 | 24 % → 35 % | 31.9 px | 0.37 | 1.44 | 80 |
| s8 | 20 % → 23 % | 77.5 px | 0.27 | 1.18 | 76 |

Numbers say: wet paint spreads well beyond the stroke.

## Brush Artist · Charcoal — stick — own sheet
own sheet 600 × 600 · Charcoal · 28 px · 1.8 s

![Brush Artist · Charcoal — stick — own sheet](Brush-Artist-Charcoal-stick-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| finger0 | 9 % → 18 % | 15.5 px | 0.83 | 2.01 | 43 |
| tip0 | 8 % → 14 % | 22.1 px | 0.83 | 1.75 | 14 |
| finger1 | 17 % → 29 % | 29.4 px | 0.83 | 1.74 | 44 |
| tip1 | 15 % → 21 % | 39.1 px | 0.83 | 1.42 | 15 |
| finger2 | 17 % → 25 % | 29.5 px | 0.83 | 1.53 | 40 |
| tip2 | 14 % → 20 % | 39.0 px | 0.83 | 1.41 | 8 |
| finger3 | 16 % → 19 % | 29.3 px | 0.83 | 1.16 | 30 |
| tip3 | 15 % → 15 % | 39.0 px | 0.83 | 1.00 | 16 |
| cig0 | 25 % → 35 % | 54.8 px | 0.83 | 1.41 | 12 |
| cig1 | 26 % → 35 % | 58.8 px | 0.83 | 1.32 | 13 |
| cig2 | 28 % → 35 % | 63.2 px | 0.83 | 1.22 | 17 |
| cig3 | 30 % → 34 % | 67.3 px | 0.83 | 1.14 | 16 |
| cig4 | 32 % → 34 % | 71.5 px | 0.83 | 1.06 | 14 |
| cig5 | 34 % → 34 % | 75.3 px | 0.83 | 1.00 | 16 |

Numbers say: wet paint spreads well beyond the stroke.

