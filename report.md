![All brushes](contact.png)

# Brush Lab — 152 brushes · Nov 4, 2026 at 1:09 AM

Every sheet: 1500 × 600, ten strokes in a 5 × 2 grid — 1. light line · 2. heavy line · 3. pressure swell · 4. fast wave · 5. slow wave · 6. spiral · 7. loop · 8. tilted · 9. over the wet one · 10. long, no reload (cell 8 holds «tilted» and «over the wet one» crossed). The CPU reference of Mamay's paint engine; the wet layer settles 20 s at the end.

Columns: **covered** = share of the cell with paint right after the stroke → after settling; **width** = painted area of the stroke ÷ its length (px); **dark** = mean darkness of the painted pixels above the paper's own grain (0 = paper, 1 = black); **spread** = how far wet paint went beyond the stroke (1.0 = stayed); **ms** = the stroke on the CPU; long stroke: paint in each quarter of its length (it should run out: wet → streaks → dry tail).

## Ink Line
Ink · 12 px · 29.5 s

![Ink Line](Ink-Line.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 1 % → 4 % | 4.3 px | 0.55 | 2.44 | 46 |
| heavy line | 5 % → 6 % | 15.7 px | 0.68 | 1.13 | 85 |
| pressure swell | 3 % → 4 % | 11.3 px | 0.64 | 1.40 | 43 |
| fast wave | 10 % → 11 % | 11.2 px | 0.59 | 1.11 | 176 |
| slow wave | 8 % → 10 % | 9.6 px | 0.57 | 1.16 | 159 |
| spiral | 14 % → 15 % | 8.9 px | 0.50 | 1.07 | 271 |
| loop | 8 % → 9 % | 10.6 px | 0.61 | 1.16 | 139 |
| tilted | 5 % → 5 % | 14.4 px | 0.65 | 1.05 | 69 |
| over the wet one | 10 % → 11 % | 12.5 px | 0.65 | 1.15 | 64 |
| long, no reload | 18 % → 17 % | 8.1 px | 0.47 | 0.96 | 407 | quarters: 0.22 → 0.09 → 0.04 → 0.02

Numbers say: light vs heavy: width 4.3 → 15.7 px, dark 0.55 → 0.68; wet paint spreads well beyond the stroke.

## Dense Ink
Ink · 14 px · 30.8 s

![Dense Ink](Dense-Ink.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 5 % → 7 % | 15.2 px | 0.72 | 1.26 | 66 |
| heavy line | 7 % → 7 % | 19.1 px | 0.73 | 1.09 | 96 |
| pressure swell | 5 % → 6 % | 17.9 px | 0.72 | 1.17 | 74 |
| fast wave | 13 % → 13 % | 15.3 px | 0.69 | 1.01 | 184 |
| slow wave | 12 % → 12 % | 13.6 px | 0.67 | 1.04 | 216 |
| spiral | 18 % → 15 % | 12.2 px | 0.65 | 0.80 | 314 |
| loop | 11 % → 12 % | 14.8 px | 0.69 | 1.08 | 159 |
| tilted | 5 % → 6 % | 14.6 px | 0.72 | 1.07 | 85 |
| over the wet one | 12 % → 13 % | 17.7 px | 0.72 | 1.11 | 92 |
| long, no reload | 23 % → 15 % | 10.1 px | 0.64 | 0.66 | 439 | quarters: 0.30 → 0.12 → 0.04 → 0.02

Numbers say: light vs heavy: width 15.2 → 19.1 px, dark 0.72 → 0.73.

## Transparent Wash
Watercolor · 22 px · 31.2 s

![Transparent Wash](Transparent-Wash.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 2 % → 5 % | 6.9 px | 0.27 | 2.25 | 41 |
| heavy line | 7 % → 9 % | 20.4 px | 0.27 | 1.22 | 81 |
| pressure swell | 4 % → 6 % | 15.2 px | 0.28 | 1.54 | 54 |
| fast wave | 14 % → 16 % | 16.1 px | 0.20 | 1.17 | 185 |
| slow wave | 12 % → 15 % | 13.7 px | 0.21 | 1.28 | 231 |
| spiral | 18 % → 22 % | 11.9 px | 0.16 | 1.23 | 228 |
| loop | 11 % → 13 % | 14.5 px | 0.22 | 1.20 | 138 |
| tilted | 8 % → 8 % | 21.1 px | 0.24 | 1.06 | 81 |
| over the wet one | 13 % → 16 % | 16.4 px | 0.24 | 1.18 | 64 |
| long, no reload | 26 % → 32 % | 11.6 px | 0.13 | 1.22 | 366 | quarters: 0.11 → 0.04 → 0.02 → 0.01

Numbers say: light vs heavy: width 6.9 → 20.4 px, dark 0.27 → 0.27; wet paint spreads well beyond the stroke.

## Dry Brush
Gouache · 24 px · 25.1 s

![Dry Brush](Dry-Brush.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 5 % → 0 % | 14.0 px | 0.65 | 0.09 | 61 |
| heavy line | 6 % → 0 % | 18.6 px | 0.65 | 0.02 | 125 |
| pressure swell | 5 % → 0 % | 18.2 px | 0.65 | 0.08 | 71 |
| fast wave | 6 % → 1 % | 7.3 px | 0.65 | 0.08 | 215 |
| slow wave | 7 % → 0 % | 8.1 px | 0.65 | 0.06 | 332 |
| spiral | 7 % → 0 % | 4.6 px | 0.65 | 0.07 | 421 |
| loop | 10 % → 0 % | 12.4 px | 0.65 | 0.04 | 255 |
| tilted | 4 % → 3 % | 10.6 px | 0.65 | 0.88 | 87 |
| over the wet one | 9 % → 1 % | 14.5 px | 0.65 | 0.12 | 91 |
| long, no reload | 6 % → 1 % | 2.9 px | 0.65 | 0.14 | 432 | quarters: 0.12 → 0.00 → 0.00 → 0.00

Numbers say: light vs heavy: width 14.0 → 18.6 px, dark 0.65 → 0.65.

## Wax Crayon
Wax · 8 px · 12.8 s

![Wax Crayon](Wax-Crayon.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 1 % → 1 % | 2.5 px | 0.71 | 1.00 | 31 |
| heavy line | 1 % → 1 % | 3.9 px | 0.69 | 1.00 | 24 |
| pressure swell | 1 % → 1 % | 3.3 px | 0.70 | 1.00 | 14 |
| fast wave | 3 % → 3 % | 3.5 px | 0.69 | 1.00 | 58 |
| slow wave | 3 % → 3 % | 3.4 px | 0.70 | 1.00 | 70 |
| spiral | 5 % → 5 % | 3.3 px | 0.70 | 1.00 | 111 |
| loop | 3 % → 3 % | 3.3 px | 0.70 | 1.00 | 56 |
| tilted | 2 % → 2 % | 5.6 px | 0.68 | 1.00 | 37 |
| over the wet one | 3 % → 3 % | 3.6 px | 0.68 | 1.00 | 27 |
| long, no reload | 7 % → 7 % | 3.3 px | 0.70 | 1.00 | 157 | quarters: 0.06 → 0.06 → 0.06 → 0.06

Numbers say: light vs heavy: width 2.5 → 3.9 px, dark 0.71 → 0.69; the long stroke does not run out of paint.

## Oil Pastel
Wax · 12 px · 12.8 s

![Oil Pastel](Oil-Pastel.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 1 % → 1 % | 4.0 px | 0.68 | 1.00 | 26 |
| heavy line | 2 % → 2 % | 6.5 px | 0.68 | 1.00 | 41 |
| pressure swell | 2 % → 2 % | 5.7 px | 0.69 | 1.00 | 27 |
| fast wave | 5 % → 5 % | 5.7 px | 0.68 | 1.00 | 94 |
| slow wave | 5 % → 5 % | 5.5 px | 0.68 | 1.00 | 93 |
| spiral | 8 % → 8 % | 5.5 px | 0.68 | 1.00 | 138 |
| loop | 4 % → 4 % | 5.6 px | 0.68 | 1.00 | 75 |
| tilted | 2 % → 2 % | 6.8 px | 0.68 | 1.00 | 83 |
| over the wet one | 5 % → 5 % | 5.8 px | 0.68 | 1.00 | 38 |
| long, no reload | 13 % → 13 % | 5.6 px | 0.68 | 1.00 | 287 | quarters: 0.10 → 0.09 → 0.10 → 0.10

Numbers say: light vs heavy: width 4.0 → 6.5 px, dark 0.68 → 0.68; the long stroke does not run out of paint.

## Charcoal
Charcoal · 5 px · 12.4 s

![Charcoal](Charcoal.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 1 % → 1 % | 2.0 px | 0.74 | 1.00 | 12 |
| heavy line | 1 % → 1 % | 3.0 px | 0.74 | 1.00 | 12 |
| pressure swell | 1 % → 1 % | 2.7 px | 0.74 | 1.00 | 9 |
| fast wave | 2 % → 2 % | 2.7 px | 0.73 | 1.00 | 40 |
| slow wave | 2 % → 2 % | 2.6 px | 0.74 | 1.00 | 29 |
| spiral | 4 % → 4 % | 2.5 px | 0.74 | 1.00 | 62 |
| loop | 2 % → 2 % | 2.6 px | 0.74 | 1.00 | 35 |
| tilted | 2 % → 2 % | 4.3 px | 0.72 | 1.00 | 24 |
| over the wet one | 2 % → 2 % | 2.4 px | 0.72 | 1.00 | 16 |
| long, no reload | 6 % → 6 % | 2.7 px | 0.73 | 1.00 | 86 | quarters: 0.05 → 0.05 → 0.05 → 0.05

Numbers say: light vs heavy: width 2.0 → 3.0 px, dark 0.74 → 0.74; the long stroke does not run out of paint.

## Impasto
Heavy acrylic · 22 px · 19.7 s

![Impasto](Impasto.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 8 % → 8 % | 24.1 px | 0.71 | 0.93 | 61 |
| heavy line | 10 % → 9 % | 28.8 px | 0.70 | 0.94 | 110 |
| pressure swell | 7 % → 7 % | 28.1 px | 0.72 | 0.94 | 66 |
| fast wave | 20 % → 13 % | 23.5 px | 0.71 | 0.64 | 216 |
| slow wave | 21 % → 14 % | 24.5 px | 0.71 | 0.66 | 335 |
| spiral | 30 % → 14 % | 20.0 px | 0.71 | 0.46 | 491 |
| loop | 18 % → 14 % | 23.9 px | 0.71 | 0.77 | 207 |
| tilted | 8 % → 8 % | 21.8 px | 0.70 | 1.00 | 109 |
| over the wet one | 17 % → 15 % | 25.4 px | 0.70 | 0.91 | 102 |
| long, no reload | 34 % → 14 % | 15.2 px | 0.71 | 0.41 | 508 | quarters: 0.38 → 0.21 → 0.10 → 0.03

Numbers say: light vs heavy: width 24.1 → 28.8 px, dark 0.71 → 0.70.

## Oil Round
Oil · 18 px · 22.5 s

![Oil Round](Oil-Round.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 2 % → 2 % | 7.2 px | 0.75 | 1.00 | 58 |
| heavy line | 7 % → 7 % | 19.3 px | 0.73 | 1.00 | 101 |
| pressure swell | 4 % → 4 % | 13.7 px | 0.72 | 1.00 | 48 |
| fast wave | 11 % → 11 % | 12.7 px | 0.65 | 1.00 | 211 |
| slow wave | 8 % → 8 % | 9.0 px | 0.57 | 1.00 | 236 |
| spiral | 10 % → 10 % | 6.6 px | 0.50 | 1.00 | 265 |
| loop | 5 % → 5 % | 7.1 px | 0.45 | 1.00 | 142 |
| tilted | 4 % → 4 % | 10.1 px | 0.52 | 1.00 | 144 |
| over the wet one | 6 % → 6 % | 7.4 px | 0.52 | 1.00 | 75 |
| long, no reload | 15 % → 15 % | 6.8 px | 0.42 | 1.00 | 561 | quarters: 0.08 → 0.08 → 0.07 → 0.06

Numbers say: light vs heavy: width 7.2 → 19.3 px, dark 0.75 → 0.73.

## Palette Knife
Oil · 20 px · 22.1 s

![Palette Knife](Palette-Knife.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 8 % → 8 % | 21.9 px | 0.67 | 1.00 | 18 |
| heavy line | 8 % → 8 % | 22.5 px | 0.73 | 1.00 | 20 |
| pressure swell | 6 % → 6 % | 22.4 px | 0.74 | 1.00 | 9 |
| fast wave | 17 % → 17 % | 19.3 px | 0.49 | 1.00 | 34 |
| slow wave | 17 % → 17 % | 19.9 px | 0.43 | 1.00 | 48 |
| spiral | 18 % → 18 % | 11.7 px | 0.45 | 1.00 | 70 |
| loop | 16 % → 16 % | 21.0 px | 0.58 | 1.00 | 50 |
| tilted | 5 % → 5 % | 15.0 px | 0.72 | 1.00 | 18 |
| over the wet one | 13 % → 13 % | 21.0 px | 0.72 | 1.00 | 12 |
| long, no reload | 17 % → 17 % | 7.5 px | 0.47 | 1.00 | 152 | quarters: 0.29 → 0.05 → 0.00 → 0.00

Numbers say: light vs heavy: width 21.9 → 22.5 px, dark 0.67 → 0.73; pressure barely changes the width.

## Water
Watercolor · 20 px · 42.1 s · over bands of wet oil paint and oil pastel in turn (it works on paint already there: look at what it does to the bands; covered counts the bands too)

![Water](Water.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 25 % → 27 % | 73.8 px | 0.80 | 1.06 | 34 |
| heavy line | 24 % → 25 % | 69.8 px | 0.81 | 1.04 | 62 |
| pressure swell | 24 % → 25 % | 89.6 px | 0.81 | 1.03 | 56 |
| fast wave | 24 % → 26 % | 27.7 px | 0.81 | 1.07 | 165 |
| slow wave | 24 % → 25 % | 27.7 px | 0.81 | 1.06 | 202 |
| spiral | 24 % → 26 % | 15.9 px | 0.81 | 1.07 | 319 |
| loop | 24 % → 25 % | 31.1 px | 0.81 | 1.03 | 102 |
| tilted | 24 % → 24 % | 67.0 px | 0.81 | 1.00 | 58 |
| over the wet one | 24 % → 25 % | 0.0 px | 0.81 | 1.06 | 49 |
| long, no reload | 24 % → 26 % | 10.7 px | 0.81 | 1.08 | 285 | quarters: 0.21 → 0.27 → 0.18 → 0.27

Numbers say: light vs heavy: width 73.8 → 69.8 px, dark 0.80 → 0.81; pressure barely changes the width; the long stroke does not run out of paint.

## Blender
Pastel · 16 px · 25.1 s · over bands of wet oil paint and oil pastel in turn (it works on paint already there: look at what it does to the bands; covered counts the bands too)

![Blender](Blender.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 24 % → 24 % | 70.7 px | 0.81 | 1.00 | 23 |
| heavy line | 25 % → 25 % | 72.1 px | 0.80 | 1.00 | 40 |
| pressure swell | 24 % → 24 % | 91.3 px | 0.81 | 1.00 | 26 |
| fast wave | 26 % → 26 % | 30.0 px | 0.79 | 1.00 | 136 |
| slow wave | 26 % → 26 % | 29.9 px | 0.80 | 1.00 | 113 |
| spiral | 28 % → 28 % | 18.7 px | 0.77 | 1.00 | 163 |
| loop | 25 % → 25 % | 32.9 px | 0.80 | 1.00 | 92 |
| tilted | 25 % → 25 % | 70.1 px | 0.79 | 1.00 | 51 |
| over the wet one | 26 % → 26 % | 1.8 px | 0.79 | 1.00 | 48 |
| long, no reload | 30 % → 30 % | 13.7 px | 0.76 | 1.00 | 312 | quarters: 0.20 → 0.28 → 0.23 → 0.30

Numbers say: light vs heavy: width 70.7 → 72.1 px, dark 0.81 → 0.80; pressure barely changes the width; the long stroke does not run out of paint.

## Eraser
Eraser · 16 px · 24.6 s · over bands of wet oil paint and oil pastel in turn (it works on paint already there: look at what it does to the bands; covered counts the bands too)

![Eraser](Eraser.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 24 % → 24 % | 69.5 px | 0.82 | 1.00 | 26 |
| heavy line | 23 % → 23 % | 67.9 px | 0.82 | 1.00 | 39 |
| pressure swell | 23 % → 23 % | 87.3 px | 0.82 | 1.00 | 30 |
| fast wave | 22 % → 22 % | 25.7 px | 0.82 | 1.00 | 97 |
| slow wave | 22 % → 22 % | 25.7 px | 0.82 | 1.00 | 109 |
| spiral | 22 % → 22 % | 14.4 px | 0.82 | 1.00 | 150 |
| loop | 22 % → 22 % | 28.6 px | 0.82 | 1.00 | 142 |
| tilted | 23 % → 23 % | 65.1 px | 0.82 | 1.00 | 56 |
| over the wet one | 23 % → 23 % | 0.0 px | 0.82 | 1.00 | 52 |
| long, no reload | 20 % → 20 % | 8.9 px | 0.82 | 1.00 | 367 | quarters: 0.15 → 0.20 → 0.15 → 0.20

Numbers say: light vs heavy: width 69.5 → 67.9 px, dark 0.82 → 0.82; pressure barely changes the width; the long stroke does not run out of paint.

## Fan
Gouache · 30 px · 35.4 s

![Fan](Fan.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 9 % → 3 % | 25.7 px | 0.63 | 0.37 | 44 |
| heavy line | 11 % → 4 % | 31.0 px | 0.63 | 0.39 | 74 |
| pressure swell | 8 % → 5 % | 31.7 px | 0.63 | 0.55 | 39 |
| fast wave | 18 % → 5 % | 20.3 px | 0.63 | 0.26 | 151 |
| slow wave | 18 % → 5 % | 21.1 px | 0.63 | 0.25 | 213 |
| spiral | 24 % → 5 % | 15.8 px | 0.63 | 0.20 | 231 |
| loop | 17 % → 5 % | 22.7 px | 0.63 | 0.29 | 117 |
| tilted | 5 % → 6 % | 15.1 px | 0.63 | 1.05 | 55 |
| over the wet one | 16 % → 8 % | 29.8 px | 0.63 | 0.50 | 70 |
| long, no reload | 23 % → 5 % | 10.1 px | 0.63 | 0.22 | 462 | quarters: 0.29 → 0.07 → 0.01 → 0.00

Numbers say: light vs heavy: width 25.7 → 31.0 px, dark 0.63 → 0.63.

## Sponge
Gouache · 30 px · 35.8 s

![Sponge](Sponge.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 4 % → 0 % | 11.4 px | 0.62 | 0.12 | 48 |
| heavy line | 12 % → 2 % | 35.4 px | 0.62 | 0.14 | 89 |
| pressure swell | 7 % → 2 % | 27.9 px | 0.62 | 0.27 | 55 |
| fast wave | 20 % → 4 % | 23.2 px | 0.62 | 0.19 | 157 |
| slow wave | 21 % → 4 % | 23.7 px | 0.62 | 0.18 | 294 |
| spiral | 28 % → 4 % | 18.3 px | 0.62 | 0.14 | 251 |
| loop | 18 % → 5 % | 23.0 px | 0.62 | 0.29 | 135 |
| tilted | 7 % → 7 % | 18.2 px | 0.62 | 1.04 | 128 |
| over the wet one | 16 % → 6 % | 27.8 px | 0.62 | 0.37 | 110 |
| long, no reload | 29 % → 5 % | 12.9 px | 0.62 | 0.17 | 471 | quarters: 0.29 → 0.13 → 0.07 → 0.04

Numbers say: light vs heavy: width 11.4 → 35.4 px, dark 0.62 → 0.62.

## Ink — sumi brush
Watercolor · 22 px · 37.3 s

![Ink — sumi brush](Ink-sumi-brush.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 8 % → 9 % | 23.8 px | 0.77 | 1.13 | 85 |
| heavy line | 13 % → 13 % | 38.0 px | 0.72 | 1.01 | 80 |
| pressure swell | 9 % → 10 % | 34.5 px | 0.75 | 1.05 | 55 |
| fast wave | 28 % → 28 % | 32.1 px | 0.58 | 1.02 | 210 |
| slow wave | 25 % → 26 % | 29.2 px | 0.62 | 1.04 | 310 |
| spiral | 37 % → 38 % | 24.5 px | 0.51 | 1.03 | 402 |
| loop | 22 % → 22 % | 28.3 px | 0.66 | 1.03 | 243 |
| tilted | 9 % → 9 % | 24.8 px | 0.73 | 1.03 | 131 |
| over the wet one | 20 % → 21 % | 31.1 px | 0.73 | 1.03 | 90 |
| long, no reload | 42 % → 43 % | 19.0 px | 0.46 | 1.02 | 497 | quarters: 0.48 → 0.24 → 0.11 → 0.06

Numbers say: light vs heavy: width 23.8 → 38.0 px, dark 0.77 → 0.72.

## Ink — wash
Watercolor · 40 px · 39.8 s

![Ink — wash](Ink-wash.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 13 % → 13 % | 36.5 px | 0.17 | 1.04 | 272 |
| heavy line | 18 % → 19 % | 53.5 px | 0.13 | 1.04 | 154 |
| pressure swell | 12 % → 13 % | 46.6 px | 0.16 | 1.05 | 87 |
| fast wave | 40 % → 42 % | 45.9 px | 0.12 | 1.06 | 288 |
| slow wave | 38 % → 40 % | 43.6 px | 0.17 | 1.06 | 460 |
| spiral | 58 % → 62 % | 38.5 px | 0.12 | 1.06 | 467 |
| loop | 33 % → 34 % | 42.9 px | 0.15 | 1.03 | 218 |
| tilted | 14 % → 14 % | 38.1 px | 0.17 | 1.03 | 161 |
| over the wet one | 29 % → 31 % | 43.2 px | 0.17 | 1.06 | 139 |
| long, no reload | 66 % → 75 % | 29.8 px | 0.12 | 1.12 | 694 | quarters: 0.16 → 0.11 → 0.07 → 0.04

Numbers say: light vs heavy: width 36.5 → 53.5 px, dark 0.17 → 0.13.

## Ink — dry brush
Ink · 30 px · 27.5 s

![Ink — dry brush](Ink-dry-brush.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 9 % → 7 % | 25.4 px | 0.81 | 0.78 | 141 |
| heavy line | 10 % → 8 % | 29.9 px | 0.79 | 0.75 | 168 |
| pressure swell | 7 % → 6 % | 28.1 px | 0.81 | 0.84 | 92 |
| fast wave | 21 % → 8 % | 24.3 px | 0.79 | 0.40 | 322 |
| slow wave | 17 % → 7 % | 20.2 px | 0.79 | 0.39 | 462 |
| spiral | 23 % → 8 % | 15.4 px | 0.78 | 0.34 | 503 |
| loop | 19 % → 8 % | 24.4 px | 0.78 | 0.44 | 264 |
| tilted | 8 % → 8 % | 22.7 px | 0.78 | 1.02 | 165 |
| over the wet one | 17 % → 14 % | 25.9 px | 0.78 | 0.81 | 124 |
| long, no reload | 20 % → 8 % | 9.0 px | 0.79 | 0.42 | 691 | quarters: 0.32 → 0.02 → 0.00 → 0.00

Numbers say: light vs heavy: width 25.4 → 29.9 px, dark 0.81 → 0.79.

## Ink — nib
Watercolor · 5 px · 25.6 s

![Ink — nib](Ink-nib.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 2 % → 5 % | 5.4 px | 0.86 | 2.46 | 29 |
| heavy line | 2 % → 5 % | 6.4 px | 0.86 | 2.33 | 37 |
| pressure swell | 2 % → 4 % | 6.2 px | 0.86 | 2.52 | 31 |
| fast wave | 5 % → 8 % | 5.9 px | 0.82 | 1.65 | 86 |
| slow wave | 5 % → 8 % | 5.6 px | 0.82 | 1.72 | 85 |
| spiral | 7 % → 11 % | 4.8 px | 0.75 | 1.45 | 161 |
| loop | 4 % → 8 % | 5.6 px | 0.84 | 1.75 | 77 |
| tilted | 4 % → 4 % | 10.2 px | 0.85 | 1.04 | 32 |
| over the wet one | 6 % → 9 % | 6.2 px | 0.85 | 1.61 | 85 |
| long, no reload | 9 % → 12 % | 4.0 px | 0.70 | 1.37 | 273 | quarters: 0.23 → 0.08 → 0.04 → 0.02

Numbers say: light vs heavy: width 5.4 → 6.4 px, dark 0.86 → 0.86; wet paint spreads well beyond the stroke.

## 0.45 · Dry brush
Gouache · 34 px · 30.2 s

![0.45 · Dry brush](0-45-Dry-brush.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 8 % → 2 % | 23.2 px | 0.68 | 0.30 | 141 |
| heavy line | 8 % → 3 % | 24.3 px | 0.68 | 0.32 | 138 |
| pressure swell | 7 % → 3 % | 25.6 px | 0.68 | 0.42 | 100 |
| fast wave | 14 % → 3 % | 15.7 px | 0.68 | 0.22 | 365 |
| slow wave | 16 % → 3 % | 18.7 px | 0.68 | 0.20 | 694 |
| spiral | 20 % → 3 % | 13.4 px | 0.68 | 0.15 | 629 |
| loop | 14 % → 4 % | 18.3 px | 0.68 | 0.26 | 344 |
| tilted | 7 % → 7 % | 18.9 px | 0.68 | 1.01 | 223 |
| over the wet one | 15 % → 6 % | 23.1 px | 0.68 | 0.43 | 227 |
| long, no reload | 21 % → 4 % | 9.4 px | 0.68 | 0.18 | 935 | quarters: 0.28 → 0.14 → 0.07 → 0.03

Numbers say: light vs heavy: width 23.2 → 24.3 px, dark 0.68 → 0.68; pressure barely changes the width.

## Dry pastel
Pastel · 26 px · 13.3 s

![Dry pastel](Dry-pastel.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 3 % → 3 % | 8.3 px | 0.38 | 1.00 | 52 |
| heavy line | 5 % → 5 % | 13.2 px | 0.39 | 1.00 | 49 |
| pressure swell | 3 % → 3 % | 11.7 px | 0.38 | 1.00 | 35 |
| fast wave | 10 % → 10 % | 11.9 px | 0.39 | 1.00 | 124 |
| slow wave | 10 % → 10 % | 11.3 px | 0.39 | 1.00 | 210 |
| spiral | 15 % → 15 % | 9.6 px | 0.39 | 1.00 | 185 |
| loop | 7 % → 7 % | 9.4 px | 0.39 | 1.00 | 119 |
| tilted | 3 % → 3 % | 8.3 px | 0.38 | 1.00 | 47 |
| over the wet one | 7 % → 7 % | 11.1 px | 0.38 | 1.00 | 43 |
| long, no reload | 18 % → 18 % | 8.2 px | 0.39 | 1.00 | 315 | quarters: 0.08 → 0.08 → 0.08 → 0.07

Numbers say: light vs heavy: width 8.3 → 13.2 px, dark 0.38 → 0.39; the long stroke does not run out of paint.

## 0.45 · Charcoal
Charcoal · 18 px · 12.6 s

![0.45 · Charcoal](0-45-Charcoal.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 2 % → 2 % | 6.5 px | 0.80 | 1.00 | 29 |
| heavy line | 3 % → 3 % | 9.2 px | 0.80 | 1.00 | 19 |
| pressure swell | 2 % → 2 % | 8.8 px | 0.80 | 1.00 | 19 |
| fast wave | 7 % → 7 % | 8.5 px | 0.80 | 1.00 | 56 |
| slow wave | 7 % → 7 % | 8.0 px | 0.80 | 1.00 | 77 |
| spiral | 12 % → 12 % | 7.9 px | 0.80 | 1.00 | 90 |
| loop | 6 % → 6 % | 8.1 px | 0.80 | 1.00 | 44 |
| tilted | 3 % → 3 % | 7.5 px | 0.80 | 1.00 | 33 |
| over the wet one | 6 % → 6 % | 7.9 px | 0.80 | 1.00 | 24 |
| long, no reload | 17 % → 17 % | 7.8 px | 0.80 | 1.00 | 132 | quarters: 0.15 → 0.16 → 0.15 → 0.16

Numbers say: light vs heavy: width 6.5 → 9.2 px, dark 0.80 → 0.80; the long stroke does not run out of paint.

## Watercolour — wash
Watercolor · 50 px · 46.1 s

![Watercolour — wash](Watercolour-wash.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 15 % → 16 % | 43.3 px | 0.03 | 1.05 | 127 |
| heavy line | 21 % → 22 % | 62.1 px | 0.03 | 1.04 | 157 |
| pressure swell | 14 % → 15 % | 54.3 px | 0.03 | 1.04 | 95 |
| fast wave | 47 % → 49 % | 53.8 px | 0.02 | 1.04 | 344 |
| slow wave | 45 % → 46 % | 52.0 px | 0.04 | 1.03 | 577 |
| spiral | 64 % → 66 % | 42.5 px | 0.03 | 1.03 | 775 |
| loop | 39 % → 40 % | 50.3 px | 0.03 | 1.02 | 308 |
| tilted | 17 % → 17 % | 47.3 px | 0.04 | 1.03 | 219 |
| over the wet one | 35 % → 36 % | 49.0 px | 0.04 | 1.04 | 159 |
| long, no reload | 79 % → 84 % | 35.5 px | 0.03 | 1.06 | 894 | quarters: 0.04 → 0.03 → 0.02 → 0.01

Numbers say: light vs heavy: width 43.3 → 62.1 px, dark 0.03 → 0.03.

## Watercolour — wet-in-wet
Watercolor · 44 px · 46.2 s

![Watercolour — wet-in-wet](Watercolour-wet-in-wet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 13 % → 19 % | 36.6 px | 0.05 | 1.51 | 93 |
| heavy line | 18 % → 20 % | 52.4 px | 0.05 | 1.09 | 133 |
| pressure swell | 12 % → 15 % | 44.9 px | 0.06 | 1.26 | 83 |
| fast wave | 40 % → 45 % | 45.9 px | 0.05 | 1.13 | 303 |
| slow wave | 39 % → 45 % | 45.0 px | 0.07 | 1.15 | 502 |
| spiral | 62 % → 67 % | 40.8 px | 0.06 | 1.08 | 495 |
| loop | 33 % → 37 % | 43.2 px | 0.06 | 1.12 | 302 |
| tilted | 14 % → 14 % | 39.1 px | 0.06 | 1.03 | 161 |
| over the wet one | 29 % → 37 % | 41.7 px | 0.06 | 1.28 | 185 |
| long, no reload | 75 % → 84 % | 33.6 px | 0.06 | 1.12 | 850 | quarters: 0.07 → 0.06 → 0.04 → 0.03

Numbers say: light vs heavy: width 36.6 → 52.4 px, dark 0.05 → 0.05; wet paint spreads well beyond the stroke.

## Watercolour — glaze
Watercolor · 38 px · 42.6 s

![Watercolour — glaze](Watercolour-glaze.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 12 % → 13 % | 35.2 px | 0.03 | 1.05 | 109 |
| heavy line | 18 % → 19 % | 52.2 px | 0.02 | 1.06 | 113 |
| pressure swell | 12 % → 13 % | 44.6 px | 0.02 | 1.07 | 83 |
| fast wave | 37 % → 40 % | 42.7 px | 0.02 | 1.08 | 278 |
| slow wave | 35 % → 37 % | 40.3 px | 0.02 | 1.07 | 595 |
| spiral | 55 % → 60 % | 36.2 px | 0.02 | 1.08 | 437 |
| loop | 32 % → 33 % | 40.9 px | 0.02 | 1.04 | 248 |
| tilted | 13 % → 14 % | 37.0 px | 0.03 | 1.03 | 148 |
| over the wet one | 28 % → 30 % | 41.6 px | 0.03 | 1.06 | 166 |
| long, no reload | 60 % → 69 % | 27.1 px | 0.02 | 1.15 | 1027 | quarters: 0.02 → 0.01 → 0.01 → 0.00

Numbers say: light vs heavy: width 35.2 → 52.2 px, dark 0.03 → 0.02.

## Watercolour — granulating
Watercolor · 44 px · 40.3 s

![Watercolour — granulating](Watercolour-granulating.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 14 % → 14 % | 40.5 px | 0.05 | 1.03 | 103 |
| heavy line | 20 % → 21 % | 59.2 px | 0.04 | 1.02 | 107 |
| pressure swell | 14 % → 14 % | 51.3 px | 0.05 | 1.02 | 89 |
| fast wave | 44 % → 45 % | 50.3 px | 0.04 | 1.04 | 284 |
| slow wave | 40 % → 42 % | 46.0 px | 0.06 | 1.06 | 462 |
| spiral | 59 % → 63 % | 38.7 px | 0.04 | 1.07 | 504 |
| loop | 36 % → 37 % | 46.9 px | 0.05 | 1.02 | 244 |
| tilted | 15 % → 16 % | 43.1 px | 0.06 | 1.03 | 162 |
| over the wet one | 32 % → 33 % | 46.6 px | 0.06 | 1.04 | 122 |
| long, no reload | 68 % → 76 % | 30.3 px | 0.04 | 1.12 | 795 | quarters: 0.06 → 0.04 → 0.02 → 0.02

Numbers say: light vs heavy: width 40.5 → 59.2 px, dark 0.05 → 0.04.

## Watercolour — dry brush
Watercolor · 36 px · 31.8 s

![Watercolour — dry brush](Watercolour-dry-brush.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 9 % → 10 % | 26.3 px | 0.07 | 1.07 | 132 |
| heavy line | 13 % → 13 % | 37.2 px | 0.06 | 1.00 | 194 |
| pressure swell | 10 % → 11 % | 37.0 px | 0.06 | 1.07 | 112 |
| fast wave | 24 % → 20 % | 28.0 px | 0.05 | 0.82 | 278 |
| slow wave | 22 % → 17 % | 25.4 px | 0.05 | 0.78 | 551 |
| spiral | 29 % → 20 % | 19.4 px | 0.05 | 0.66 | 501 |
| loop | 19 % → 18 % | 25.0 px | 0.05 | 0.94 | 263 |
| tilted | 9 % → 10 % | 25.3 px | 0.06 | 1.09 | 153 |
| over the wet one | 21 % → 20 % | 32.2 px | 0.06 | 0.99 | 145 |
| long, no reload | 28 % → 19 % | 12.3 px | 0.05 | 0.70 | 654 | quarters: 0.03 → 0.01 → 0.00 → 0.00

Numbers say: light vs heavy: width 26.3 → 37.2 px, dark 0.07 → 0.06.

## Gouache
Gouache · 30 px · 28.9 s

![Gouache](Gouache.png)

A light paint: laid on a grey sheet (on white it cannot be seen); **dark** = how far it is from the grey either way.

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 8 % → 6 % | 24.7 px | 0.28 | 0.66 | 109 |
| heavy line | 14 % → 7 % | 39.8 px | 0.28 | 0.49 | 97 |
| pressure swell | 10 % → 6 % | 38.8 px | 0.28 | 0.62 | 71 |
| fast wave | 28 % → 8 % | 32.8 px | 0.28 | 0.27 | 229 |
| slow wave | 27 % → 8 % | 31.6 px | 0.28 | 0.30 | 386 |
| spiral | 38 % → 8 % | 25.0 px | 0.28 | 0.22 | 473 |
| loop | 22 % → 8 % | 28.8 px | 0.28 | 0.36 | 230 |
| tilted | 9 % → 9 % | 24.6 px | 0.27 | 1.00 | 110 |
| over the wet one | 20 % → 13 % | 31.0 px | 0.27 | 0.67 | 90 |
| long, no reload | 40 % → 10 % | 17.9 px | 0.27 | 0.24 | 504 | quarters: 0.01 → 0.01 → 0.02 → 0.02

Numbers say: light vs heavy: width 24.7 → 39.8 px, dark 0.28 → 0.28; the long stroke does not run out of paint.

## Oil — alla prima
Oil · 30 px · 25.6 s

![Oil — alla prima](Oil-alla-prima.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 10 % → 10 % | 28.5 px | 0.51 | 1.00 | 114 |
| heavy line | 11 % → 11 % | 31.2 px | 0.51 | 1.00 | 108 |
| pressure swell | 8 % → 8 % | 30.9 px | 0.53 | 1.00 | 84 |
| fast wave | 26 % → 26 % | 29.5 px | 0.52 | 1.00 | 292 |
| slow wave | 26 % → 26 % | 30.2 px | 0.52 | 1.00 | 515 |
| spiral | 41 % → 41 % | 27.0 px | 0.51 | 1.00 | 531 |
| loop | 22 % → 22 % | 28.0 px | 0.52 | 1.00 | 270 |
| tilted | 11 % → 11 % | 31.9 px | 0.52 | 1.00 | 148 |
| over the wet one | 21 % → 21 % | 27.5 px | 0.52 | 1.00 | 113 |
| long, no reload | 50 % → 50 % | 22.5 px | 0.50 | 1.00 | 865 | quarters: 0.33 → 0.30 → 0.26 → 0.23

Numbers say: light vs heavy: width 28.5 → 31.2 px, dark 0.51 → 0.51; pressure barely changes the width.

## Oil — impasto
Oil · 34 px · 27.2 s

![Oil — impasto](Oil-impasto.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 12 % → 12 % | 34.5 px | 0.23 | 1.00 | 150 |
| heavy line | 13 % → 13 % | 37.4 px | 0.23 | 1.00 | 159 |
| pressure swell | 10 % → 10 % | 37.1 px | 0.25 | 1.00 | 102 |
| fast wave | 28 % → 28 % | 31.9 px | 0.23 | 1.00 | 352 |
| slow wave | 30 % → 30 % | 34.3 px | 0.23 | 1.00 | 642 |
| spiral | 46 % → 46 % | 30.3 px | 0.22 | 1.00 | 568 |
| loop | 25 % → 25 % | 32.2 px | 0.24 | 1.00 | 314 |
| tilted | 12 % → 12 % | 33.4 px | 0.24 | 1.00 | 293 |
| over the wet one | 24 % → 24 % | 32.6 px | 0.24 | 1.00 | 203 |
| long, no reload | 51 % → 51 % | 22.7 px | 0.22 | 1.00 | 1524 | quarters: 0.17 → 0.13 → 0.10 → 0.08

Numbers say: light vs heavy: width 34.5 → 37.4 px, dark 0.23 → 0.23; pressure barely changes the width.

## Oil — glaze
Oil · 40 px · 22.1 s

![Oil — glaze](Oil-glaze.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 9 % → 9 % | 27.0 px | 0.50 | 1.00 | 110 |
| heavy line | 13 % → 13 % | 38.2 px | 0.49 | 1.00 | 150 |
| pressure swell | 10 % → 10 % | 36.6 px | 0.50 | 1.00 | 92 |
| fast wave | 29 % → 29 % | 33.5 px | 0.49 | 1.00 | 330 |
| slow wave | 30 % → 30 % | 34.5 px | 0.50 | 1.00 | 555 |
| spiral | 46 % → 46 % | 30.0 px | 0.49 | 1.00 | 594 |
| loop | 24 % → 24 % | 31.4 px | 0.50 | 1.00 | 283 |
| tilted | 11 % → 11 % | 30.3 px | 0.50 | 1.00 | 172 |
| over the wet one | 22 % → 22 % | 32.5 px | 0.50 | 1.00 | 133 |
| long, no reload | 52 % → 52 % | 23.5 px | 0.49 | 1.00 | 999 | quarters: 0.34 → 0.30 → 0.27 → 0.22

Numbers say: light vs heavy: width 27.0 → 38.2 px, dark 0.50 → 0.49.

## Oil — scumble
Oil · 36 px · 23.6 s

![Oil — scumble](Oil-scumble.png)

A light paint: laid on a grey sheet (on white it cannot be seen); **dark** = how far it is from the grey either way.

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 10 % → 10 % | 27.7 px | 0.28 | 1.00 | 175 |
| heavy line | 9 % → 9 % | 27.2 px | 0.27 | 1.00 | 171 |
| pressure swell | 9 % → 9 % | 32.2 px | 0.26 | 1.00 | 120 |
| fast wave | 18 % → 18 % | 21.0 px | 0.22 | 1.00 | 431 |
| slow wave | 22 % → 22 % | 25.5 px | 0.21 | 1.00 | 751 |
| spiral | 32 % → 32 % | 20.9 px | 0.17 | 1.00 | 736 |
| loop | 18 % → 18 % | 23.1 px | 0.23 | 1.00 | 384 |
| tilted | 10 % → 10 % | 27.2 px | 0.25 | 1.00 | 202 |
| over the wet one | 20 % → 20 % | 27.5 px | 0.25 | 1.00 | 187 |
| long, no reload | 35 % → 35 % | 15.5 px | 0.15 | 1.00 | 1058 | quarters: 0.00 → 0.00 → 0.00 → 0.00

Numbers say: light vs heavy: width 27.7 → 27.2 px, dark 0.28 → 0.27; pressure barely changes the width.

## Acrylic — heavy body
Heavy acrylic · 30 px · 18.9 s

![Acrylic — heavy body](Acrylic-heavy-body.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 10 % → 9 % | 30.0 px | 0.51 | 0.92 | 105 |
| heavy line | 11 % → 10 % | 32.1 px | 0.51 | 0.93 | 112 |
| pressure swell | 9 % → 8 % | 31.9 px | 0.53 | 0.94 | 85 |
| fast wave | 23 % → 15 % | 27.1 px | 0.51 | 0.62 | 348 |
| slow wave | 24 % → 16 % | 28.1 px | 0.51 | 0.65 | 536 |
| spiral | 36 % → 15 % | 23.5 px | 0.51 | 0.42 | 523 |
| loop | 21 % → 16 % | 27.1 px | 0.51 | 0.76 | 249 |
| tilted | 9 % → 9 % | 26.2 px | 0.51 | 1.00 | 145 |
| over the wet one | 20 % → 18 % | 28.4 px | 0.51 | 0.90 | 105 |
| long, no reload | 39 % → 15 % | 17.4 px | 0.51 | 0.40 | 699 | quarters: 0.30 → 0.19 → 0.11 → 0.04

Numbers say: light vs heavy: width 30.0 → 32.1 px, dark 0.51 → 0.51; pressure barely changes the width.

## Acrylic — fluid
Watercolor · 36 px · 39.4 s

![Acrylic — fluid](Acrylic-fluid.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 12 % → 12 % | 34.3 px | 0.08 | 1.02 | 99 |
| heavy line | 18 % → 18 % | 51.6 px | 0.07 | 1.01 | 128 |
| pressure swell | 12 % → 12 % | 44.8 px | 0.08 | 1.01 | 91 |
| fast wave | 37 % → 38 % | 42.6 px | 0.07 | 1.02 | 245 |
| slow wave | 34 % → 35 % | 39.2 px | 0.07 | 1.03 | 425 |
| spiral | 52 % → 53 % | 34.2 px | 0.07 | 1.03 | 553 |
| loop | 30 % → 31 % | 39.4 px | 0.07 | 1.02 | 289 |
| tilted | 12 % → 12 % | 32.6 px | 0.08 | 1.04 | 143 |
| over the wet one | 27 % → 28 % | 43.2 px | 0.08 | 1.02 | 103 |
| long, no reload | 56 % → 58 % | 25.3 px | 0.06 | 1.04 | 616 | quarters: 0.06 → 0.05 → 0.03 → 0.02

Numbers say: light vs heavy: width 34.3 → 51.6 px, dark 0.08 → 0.07.

## Acrylic — palette knife
Heavy acrylic · 42 px · 20.8 s

![Acrylic — palette knife](Acrylic-palette-knife.png)

A light paint: laid on a grey sheet (on white it cannot be seen); **dark** = how far it is from the grey either way.

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 16 % → 15 % | 45.6 px | 0.39 | 0.98 | 64 |
| heavy line | 16 % → 15 % | 45.8 px | 0.40 | 0.98 | 49 |
| pressure swell | 12 % → 12 % | 45.6 px | 0.42 | 0.99 | 19 |
| fast wave | 37 % → 20 % | 42.6 px | 0.37 | 0.55 | 139 |
| slow wave | 37 % → 21 % | 43.2 px | 0.37 | 0.57 | 220 |
| spiral | 50 % → 18 % | 32.8 px | 0.37 | 0.37 | 157 |
| loop | 32 % → 24 % | 41.2 px | 0.36 | 0.75 | 91 |
| tilted | 13 % → 13 % | 35.1 px | 0.39 | 1.00 | 33 |
| over the wet one | 27 % → 27 % | 41.3 px | 0.39 | 0.97 | 37 |
| long, no reload | 57 % → 21 % | 25.6 px | 0.35 | 0.36 | 219 | quarters: 0.00 → 0.00 → 0.00 → 0.01

Numbers say: light vs heavy: width 45.6 → 45.8 px, dark 0.39 → 0.40; pressure barely changes the width; the long stroke does not run out of paint.

## Finger on oil
Oil · 30 px · 16.3 s

![Finger on oil](Finger-on-oil.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 6 % → 6 % | 16.8 px | 0.40 | 1.00 | 96 |
| heavy line | 7 % → 7 % | 21.5 px | 0.39 | 1.00 | 119 |
| pressure swell | 6 % → 6 % | 22.3 px | 0.40 | 1.00 | 52 |
| fast wave | 12 % → 12 % | 13.6 px | 0.37 | 1.00 | 163 |
| slow wave | 17 % → 17 % | 19.5 px | 0.36 | 1.00 | 276 |
| spiral | 22 % → 22 % | 14.3 px | 0.34 | 1.00 | 291 |
| loop | 13 % → 13 % | 16.6 px | 0.37 | 1.00 | 151 |
| tilted | 8 % → 8 % | 21.4 px | 0.39 | 1.00 | 103 |
| over the wet one | 15 % → 15 % | 20.3 px | 0.39 | 1.00 | 78 |
| long, no reload | 22 % → 22 % | 10.0 px | 0.33 | 1.00 | 406 | quarters: 0.14 → 0.08 → 0.06 → 0.04

Numbers say: light vs heavy: width 16.8 → 21.5 px, dark 0.40 → 0.39.

## Palette knife — oil
Oil · 44 px · 23.0 s

![Palette knife — oil](Palette-knife-oil.png)

A light paint: laid on a grey sheet (on white it cannot be seen); **dark** = how far it is from the grey either way.

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 16 % → 16 % | 47.4 px | 0.36 | 1.00 | 53 |
| heavy line | 17 % → 17 % | 48.1 px | 0.39 | 1.00 | 39 |
| pressure swell | 13 % → 13 % | 47.5 px | 0.39 | 1.00 | 13 |
| fast wave | 39 % → 40 % | 45.6 px | 0.35 | 1.01 | 94 |
| slow wave | 40 % → 40 % | 46.1 px | 0.35 | 1.00 | 179 |
| spiral | 63 % → 63 % | 41.3 px | 0.27 | 1.00 | 161 |
| loop | 34 % → 34 % | 43.8 px | 0.36 | 1.00 | 79 |
| tilted | 14 % → 14 % | 38.3 px | 0.38 | 1.00 | 35 |
| over the wet one | 29 % → 29 % | 42.5 px | 0.38 | 1.00 | 36 |
| long, no reload | 75 % → 75 % | 33.4 px | 0.25 | 1.00 | 185 | quarters: 0.00 → 0.00 → 0.00 → 0.00

Numbers say: light vs heavy: width 47.4 → 48.1 px, dark 0.36 → 0.39; pressure barely changes the width; the long stroke does not run out of paint.

## 0.45 · Sponge
Watercolor · 46 px · 43.6 s

![0.45 · Sponge](0-45-Sponge.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 24 % → 18 % | 70.4 px | 0.03 | 0.74 | 78 |
| heavy line | 29 % → 25 % | 83.6 px | 0.03 | 0.85 | 91 |
| pressure swell | 21 % → 17 % | 79.2 px | 0.03 | 0.81 | 52 |
| fast wave | 51 % → 43 % | 59.1 px | 0.03 | 0.84 | 220 |
| slow wave | 54 % → 48 % | 62.4 px | 0.05 | 0.88 | 296 |
| spiral | 67 % → 57 % | 44.5 px | 0.04 | 0.85 | 388 |
| loop | 48 % → 43 % | 62.4 px | 0.04 | 0.89 | 191 |
| tilted | 16 % → 17 % | 45.1 px | 0.05 | 1.05 | 118 |
| over the wet one | 41 % → 37 % | 69.0 px | 0.05 | 0.91 | 74 |
| long, no reload | 78 % → 71 % | 35.0 px | 0.04 | 0.90 | 550 | quarters: 0.05 → 0.05 → 0.03 → 0.02

Numbers say: light vs heavy: width 70.4 → 83.6 px, dark 0.03 → 0.03.

## 0.45 · Eraser
Eraser · 30 px · 26.1 s · over bands of wet oil paint and oil pastel in turn (it works on paint already there: look at what it does to the bands; covered counts the bands too)

![0.45 · Eraser](0-45-Eraser.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 24 % → 24 % | 69.2 px | 0.82 | 1.00 | 41 |
| heavy line | 23 % → 23 % | 67.4 px | 0.81 | 1.00 | 79 |
| pressure swell | 23 % → 23 % | 86.7 px | 0.82 | 1.00 | 55 |
| fast wave | 21 % → 21 % | 24.7 px | 0.81 | 1.00 | 155 |
| slow wave | 20 % → 20 % | 23.5 px | 0.82 | 1.00 | 248 |
| spiral | 20 % → 20 % | 13.5 px | 0.79 | 1.00 | 233 |
| loop | 21 % → 21 % | 27.8 px | 0.80 | 1.00 | 146 |
| tilted | 23 % → 23 % | 64.8 px | 0.81 | 1.00 | 79 |
| over the wet one | 22 % → 22 % | 0.0 px | 0.81 | 1.00 | 65 |
| long, no reload | 17 % → 17 % | 7.5 px | 0.79 | 1.00 | 414 | quarters: 0.13 → 0.16 → 0.13 → 0.17

Numbers say: light vs heavy: width 69.2 → 67.4 px, dark 0.82 → 0.81; pressure barely changes the width; the long stroke does not run out of paint.

## Lift wet paint
Eraser · 30 px · 25.5 s · over bands of wet oil paint and oil pastel in turn (it works on paint already there: look at what it does to the bands; covered counts the bands too)

![Lift wet paint](Lift-wet-paint.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 24 % → 24 % | 70.1 px | 0.82 | 1.00 | 41 |
| heavy line | 24 % → 24 % | 69.8 px | 0.82 | 1.00 | 54 |
| pressure swell | 24 % → 24 % | 89.5 px | 0.82 | 1.00 | 42 |
| fast wave | 24 % → 24 % | 27.7 px | 0.82 | 1.00 | 122 |
| slow wave | 24 % → 24 % | 27.7 px | 0.82 | 1.00 | 221 |
| spiral | 24 % → 24 % | 15.9 px | 0.82 | 1.00 | 249 |
| loop | 24 % → 24 % | 31.1 px | 0.82 | 1.00 | 123 |
| tilted | 24 % → 24 % | 66.8 px | 0.82 | 1.00 | 66 |
| over the wet one | 24 % → 24 % | 0.0 px | 0.82 | 1.00 | 62 |
| long, no reload | 24 % → 24 % | 10.7 px | 0.82 | 1.00 | 380 | quarters: 0.18 → 0.24 → 0.17 → 0.24

Numbers say: light vs heavy: width 70.1 → 69.8 px, dark 0.82 → 0.82; pressure barely changes the width; the long stroke does not run out of paint.

## Sgraffito
Eraser · 10 px · 25.1 s · over bands of wet oil paint and oil pastel in turn (it works on paint already there: look at what it does to the bands; covered counts the bands too)

![Sgraffito](Sgraffito.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 24 % → 24 % | 69.5 px | 0.81 | 1.00 | 18 |
| heavy line | 24 % → 24 % | 69.5 px | 0.82 | 1.00 | 16 |
| pressure swell | 24 % → 24 % | 89.5 px | 0.82 | 1.00 | 6 |
| fast wave | 24 % → 24 % | 27.4 px | 0.82 | 1.00 | 24 |
| slow wave | 24 % → 24 % | 27.4 px | 0.81 | 1.00 | 25 |
| spiral | 24 % → 24 % | 15.7 px | 0.81 | 1.00 | 42 |
| loop | 24 % → 24 % | 30.9 px | 0.82 | 1.00 | 19 |
| tilted | 24 % → 24 % | 66.6 px | 0.82 | 1.00 | 9 |
| over the wet one | 24 % → 24 % | 0.0 px | 0.82 | 1.00 | 11 |
| long, no reload | 24 % → 24 % | 10.6 px | 0.82 | 1.00 | 70 | quarters: 0.17 → 0.24 → 0.17 → 0.24

Numbers say: light vs heavy: width 69.5 → 69.5 px, dark 0.81 → 0.82; pressure barely changes the width; the long stroke does not run out of paint.

## Brush Artist · Refs · #01 Henry Ward peach cloud
Gouache · 44 px · 43.1 s

![Brush Artist · Refs · #01 Henry Ward peach cloud](Brush-Artist-Refs-01-Henry-Ward-peach-cloud.png)

A light paint: laid on a grey sheet (on white it cannot be seen); **dark** = how far it is from the grey either way.

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 9 % → 5 % | 27.0 px | 0.34 | 0.50 | 231 |
| heavy line | 12 % → 8 % | 34.1 px | 0.34 | 0.64 | 188 |
| pressure swell | 9 % → 7 % | 34.8 px | 0.34 | 0.71 | 132 |
| fast wave | 12 % → 4 % | 14.4 px | 0.34 | 0.36 | 436 |
| slow wave | 27 % → 14 % | 31.1 px | 0.34 | 0.52 | 822 |
| spiral | 35 % → 14 % | 22.8 px | 0.34 | 0.41 | 782 |
| loop | 21 % → 13 % | 27.6 px | 0.34 | 0.62 | 455 |
| tilted | 9 % → 9 % | 23.9 px | 0.34 | 1.01 | 310 |
| over the wet one | 20 % → 15 % | 31.0 px | 0.34 | 0.77 | 253 |
| long, no reload | 37 % → 18 % | 16.8 px | 0.34 | 0.47 | 1423 | quarters: 0.01 → 0.02 → 0.02 → 0.02

Numbers say: light vs heavy: width 27.0 → 34.1 px, dark 0.34 → 0.34; the long stroke does not run out of paint.

## Brush Artist · Refs · #02 Henry Ward cream strokes
Gouache · 46 px · 41.4 s

![Brush Artist · Refs · #02 Henry Ward cream strokes](Brush-Artist-Refs-02-Henry-Ward-cream-strokes.png)

A light paint: laid on a grey sheet (on white it cannot be seen); **dark** = how far it is from the grey either way.

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 9 % → 4 % | 27.1 px | 0.41 | 0.40 | 183 |
| heavy line | 12 % → 7 % | 34.6 px | 0.42 | 0.62 | 204 |
| pressure swell | 9 % → 6 % | 35.2 px | 0.42 | 0.69 | 153 |
| fast wave | 12 % → 4 % | 14.4 px | 0.41 | 0.30 | 503 |
| slow wave | 27 % → 13 % | 30.9 px | 0.41 | 0.50 | 858 |
| spiral | 34 % → 14 % | 22.6 px | 0.41 | 0.39 | 851 |
| loop | 21 % → 13 % | 27.7 px | 0.41 | 0.60 | 633 |
| tilted | 8 % → 8 % | 23.1 px | 0.41 | 1.01 | 298 |
| over the wet one | 20 % → 16 % | 31.9 px | 0.41 | 0.79 | 263 |
| long, no reload | 37 % → 17 % | 16.6 px | 0.41 | 0.47 | 1138 | quarters: 0.01 → 0.02 → 0.03 → 0.03

Numbers say: light vs heavy: width 27.1 → 34.6 px, dark 0.41 → 0.42; the long stroke does not run out of paint.

## Brush Artist · Refs · #03 Henry Ward navy contours
Heavy acrylic · 22 px · 24.7 s

![Brush Artist · Refs · #03 Henry Ward navy contours](Brush-Artist-Refs-03-Henry-Ward-navy-contours.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 8 % → 7 % | 22.1 px | 0.70 | 0.94 | 102 |
| heavy line | 8 % → 8 % | 24.0 px | 0.70 | 0.95 | 132 |
| pressure swell | 6 % → 6 % | 23.8 px | 0.73 | 0.94 | 74 |
| fast wave | 19 % → 12 % | 22.0 px | 0.72 | 0.65 | 248 |
| slow wave | 20 % → 13 % | 22.6 px | 0.72 | 0.68 | 542 |
| spiral | 30 % → 13 % | 19.6 px | 0.72 | 0.45 | 549 |
| loop | 17 % → 13 % | 21.5 px | 0.72 | 0.81 | 292 |
| tilted | 8 % → 8 % | 23.2 px | 0.72 | 1.00 | 117 |
| over the wet one | 16 % → 14 % | 21.8 px | 0.72 | 0.90 | 120 |
| long, no reload | 34 % → 13 % | 15.1 px | 0.72 | 0.40 | 588 | quarters: 0.35 → 0.29 → 0.19 → 0.08

Numbers say: light vs heavy: width 22.1 → 24.0 px, dark 0.70 → 0.70; pressure barely changes the width.

## Brush Artist · Refs · #04 Henry Ward grey cloud
Gouache · 50 px · 44.4 s

![Brush Artist · Refs · #04 Henry Ward grey cloud](Brush-Artist-Refs-04-Henry-Ward-grey-cloud.png)

A light paint: laid on a grey sheet (on white it cannot be seen); **dark** = how far it is from the grey either way.

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 11 % → 5 % | 31.5 px | 0.33 | 0.44 | 215 |
| heavy line | 14 % → 9 % | 39.8 px | 0.33 | 0.63 | 227 |
| pressure swell | 11 % → 8 % | 40.2 px | 0.33 | 0.70 | 185 |
| fast wave | 14 % → 5 % | 16.6 px | 0.33 | 0.35 | 580 |
| slow wave | 31 % → 16 % | 35.5 px | 0.33 | 0.51 | 773 |
| spiral | 37 % → 17 % | 24.6 px | 0.33 | 0.46 | 809 |
| loop | 25 % → 15 % | 32.0 px | 0.33 | 0.61 | 885 |
| tilted | 10 % → 10 % | 26.5 px | 0.33 | 1.02 | 309 |
| over the wet one | 23 % → 18 % | 36.5 px | 0.33 | 0.79 | 220 |
| long, no reload | 42 % → 21 % | 18.7 px | 0.33 | 0.49 | 1416 | quarters: 0.01 → 0.02 → 0.02 → 0.02

Numbers say: light vs heavy: width 31.5 → 39.8 px, dark 0.33 → 0.33; the long stroke does not run out of paint.

## Brush Artist · Refs · #05 Henry Ward green in rust loops
Heavy acrylic · 20 px · 23.7 s

![Brush Artist · Refs · #05 Henry Ward green in rust loops](Brush-Artist-Refs-05-Henry-Ward-green-in-rust-loops.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 7 % → 6 % | 19.9 px | 0.55 | 0.94 | 145 |
| heavy line | 7 % → 7 % | 21.7 px | 0.55 | 0.94 | 202 |
| pressure swell | 6 % → 5 % | 22.0 px | 0.57 | 0.92 | 90 |
| fast wave | 17 % → 11 % | 19.9 px | 0.56 | 0.64 | 287 |
| slow wave | 18 % → 12 % | 20.5 px | 0.55 | 0.66 | 416 |
| spiral | 27 % → 11 % | 17.9 px | 0.55 | 0.42 | 409 |
| loop | 15 % → 12 % | 19.5 px | 0.55 | 0.79 | 344 |
| tilted | 8 % → 8 % | 22.1 px | 0.56 | 1.00 | 147 |
| over the wet one | 15 % → 13 % | 19.7 px | 0.56 | 0.87 | 131 |
| long, no reload | 30 % → 12 % | 13.4 px | 0.56 | 0.39 | 761 | quarters: 0.25 → 0.18 → 0.10 → 0.02

Numbers say: light vs heavy: width 19.9 → 21.7 px, dark 0.55 → 0.55; pressure barely changes the width.

## Brush Artist · Refs · #06 Henry Ward scrubbed grey
Gouache · 50 px · 43.0 s

![Brush Artist · Refs · #06 Henry Ward scrubbed grey](Brush-Artist-Refs-06-Henry-Ward-scrubbed-grey.png)

A light paint: laid on a grey sheet (on white it cannot be seen); **dark** = how far it is from the grey either way.

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 11 % → 5 % | 31.5 px | 0.34 | 0.44 | 375 |
| heavy line | 14 % → 9 % | 39.8 px | 0.34 | 0.63 | 366 |
| pressure swell | 11 % → 8 % | 40.2 px | 0.34 | 0.70 | 157 |
| fast wave | 14 % → 5 % | 16.6 px | 0.34 | 0.35 | 413 |
| slow wave | 31 % → 16 % | 35.5 px | 0.34 | 0.51 | 1111 |
| spiral | 37 % → 17 % | 24.6 px | 0.34 | 0.46 | 977 |
| loop | 25 % → 15 % | 32.0 px | 0.34 | 0.61 | 473 |
| tilted | 10 % → 10 % | 26.5 px | 0.34 | 1.02 | 269 |
| over the wet one | 23 % → 18 % | 36.5 px | 0.34 | 0.79 | 241 |
| long, no reload | 42 % → 21 % | 18.7 px | 0.34 | 0.49 | 1216 | quarters: 0.01 → 0.02 → 0.02 → 0.02

Numbers say: light vs heavy: width 31.5 → 39.8 px, dark 0.34 → 0.34; the long stroke does not run out of paint.

## Brush Artist · Refs · #07 Henry Ward blue L + black zigzag
Heavy acrylic · 34 px · 19.3 s

![Brush Artist · Refs · #07 Henry Ward blue L + black zigzag](Brush-Artist-Refs-07-Henry-Ward-blue-L-black-zigzag.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 12 % → 11 % | 34.2 px | 0.58 | 0.93 | 139 |
| heavy line | 13 % → 12 % | 36.9 px | 0.58 | 0.93 | 141 |
| pressure swell | 10 % → 9 % | 36.6 px | 0.59 | 0.94 | 97 |
| fast wave | 30 % → 20 % | 34.1 px | 0.58 | 0.69 | 372 |
| slow wave | 30 % → 22 % | 34.6 px | 0.58 | 0.73 | 540 |
| spiral | 48 % → 22 % | 31.5 px | 0.58 | 0.46 | 529 |
| loop | 25 % → 21 % | 32.7 px | 0.58 | 0.82 | 285 |
| tilted | 11 % → 11 % | 31.0 px | 0.58 | 1.00 | 188 |
| over the wet one | 23 % → 21 % | 32.8 px | 0.58 | 0.91 | 155 |
| long, no reload | 53 % → 22 % | 23.9 px | 0.58 | 0.41 | 770 | quarters: 0.40 → 0.32 → 0.21 → 0.10

Numbers say: light vs heavy: width 34.2 → 36.9 px, dark 0.58 → 0.58; pressure barely changes the width.

## Brush Artist · Refs · #08 Henry Ward olive bands
Gouache · 34 px · 28.4 s

![Brush Artist · Refs · #08 Henry Ward olive bands](Brush-Artist-Refs-08-Henry-Ward-olive-bands.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 4 % → 0 % | 12.2 px | 0.61 | 0.04 | 95 |
| heavy line | 7 % → 0 % | 19.3 px | 0.61 | 0.02 | 190 |
| pressure swell | 5 % → 0 % | 18.7 px | 0.61 | 0.03 | 98 |
| fast wave | 10 % → 0 % | 11.1 px | 0.61 | 0.02 | 304 |
| slow wave | 15 % → 1 % | 17.0 px | 0.61 | 0.06 | 624 |
| spiral | 19 % → 1 % | 12.7 px | 0.61 | 0.03 | 566 |
| loop | 12 % → 1 % | 15.3 px | 0.61 | 0.09 | 255 |
| tilted | 5 % → 5 % | 15.1 px | 0.61 | 0.96 | 133 |
| over the wet one | 11 % → 2 % | 16.9 px | 0.61 | 0.22 | 129 |
| long, no reload | 22 % → 2 % | 9.8 px | 0.61 | 0.09 | 986 | quarters: 0.21 → 0.15 → 0.11 → 0.09

Numbers say: light vs heavy: width 12.2 → 19.3 px, dark 0.61 → 0.61.

## Brush Artist · Refs · #09 Henry Ward white loops
Gouache · 46 px · 43.1 s

![Brush Artist · Refs · #09 Henry Ward white loops](Brush-Artist-Refs-09-Henry-Ward-white-loops.png)

A light paint: laid on a grey sheet (on white it cannot be seen); **dark** = how far it is from the grey either way.

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 9 % → 4 % | 27.1 px | 0.43 | 0.40 | 168 |
| heavy line | 12 % → 7 % | 34.6 px | 0.44 | 0.62 | 175 |
| pressure swell | 9 % → 6 % | 35.2 px | 0.44 | 0.69 | 199 |
| fast wave | 12 % → 4 % | 14.4 px | 0.43 | 0.30 | 631 |
| slow wave | 27 % → 13 % | 30.9 px | 0.43 | 0.50 | 1005 |
| spiral | 34 % → 14 % | 22.6 px | 0.43 | 0.39 | 883 |
| loop | 21 % → 13 % | 27.7 px | 0.43 | 0.60 | 449 |
| tilted | 8 % → 8 % | 23.1 px | 0.43 | 1.01 | 226 |
| over the wet one | 20 % → 16 % | 31.9 px | 0.43 | 0.79 | 196 |
| long, no reload | 37 % → 17 % | 16.6 px | 0.43 | 0.47 | 1286 | quarters: 0.02 → 0.02 → 0.03 → 0.03

Numbers say: light vs heavy: width 27.1 → 34.6 px, dark 0.43 → 0.44; the long stroke does not run out of paint.

## Brush Artist · Refs · #10 Henry Ward maroon loops
Heavy acrylic · 30 px · 19.9 s

![Brush Artist · Refs · #10 Henry Ward maroon loops](Brush-Artist-Refs-10-Henry-Ward-maroon-loops.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 10 % → 9 % | 28.8 px | 0.71 | 0.95 | 108 |
| heavy line | 11 % → 10 % | 31.2 px | 0.71 | 0.95 | 104 |
| pressure swell | 8 % → 8 % | 31.1 px | 0.73 | 0.95 | 79 |
| fast wave | 25 % → 18 % | 28.7 px | 0.72 | 0.71 | 467 |
| slow wave | 25 % → 19 % | 29.4 px | 0.72 | 0.73 | 746 |
| spiral | 40 % → 19 % | 26.2 px | 0.72 | 0.47 | 506 |
| loop | 21 % → 18 % | 27.6 px | 0.72 | 0.85 | 341 |
| tilted | 10 % → 10 % | 28.7 px | 0.72 | 1.00 | 163 |
| over the wet one | 20 % → 18 % | 27.7 px | 0.72 | 0.91 | 128 |
| long, no reload | 46 % → 18 % | 20.7 px | 0.72 | 0.40 | 700 | quarters: 0.44 → 0.38 → 0.30 → 0.22

Numbers say: light vs heavy: width 28.8 → 31.2 px, dark 0.71 → 0.71; pressure barely changes the width.

## Brush Artist · Refs · #11 Henry Ward purple spun balls
Heavy acrylic · 36 px · 24.0 s

![Brush Artist · Refs · #11 Henry Ward purple spun balls](Brush-Artist-Refs-11-Henry-Ward-purple-spun-balls.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 12 % → 12 % | 35.3 px | 0.71 | 0.96 | 159 |
| heavy line | 13 % → 12 % | 37.9 px | 0.71 | 0.96 | 149 |
| pressure swell | 10 % → 10 % | 37.7 px | 0.74 | 0.96 | 110 |
| fast wave | 30 % → 23 % | 35.1 px | 0.73 | 0.75 | 404 |
| slow wave | 31 % → 24 % | 35.5 px | 0.73 | 0.79 | 578 |
| spiral | 49 % → 25 % | 32.6 px | 0.73 | 0.50 | 626 |
| loop | 26 % → 23 % | 33.4 px | 0.73 | 0.88 | 311 |
| tilted | 12 % → 12 % | 32.4 px | 0.73 | 1.00 | 182 |
| over the wet one | 24 % → 22 % | 33.5 px | 0.73 | 0.93 | 145 |
| long, no reload | 56 % → 24 % | 24.9 px | 0.73 | 0.44 | 2500 | quarters: 0.51 → 0.46 → 0.39 → 0.29

Numbers say: light vs heavy: width 35.3 → 37.9 px, dark 0.71 → 0.71; pressure barely changes the width.

## Brush Artist · Refs · #12 Henry Ward black-olive cage
Gouache · 28 px · 30.3 s

![Brush Artist · Refs · #12 Henry Ward black-olive cage](Brush-Artist-Refs-12-Henry-Ward-black-olive-cage.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 3 % → 0 % | 10.1 px | 0.65 | 0.08 | 78 |
| heavy line | 5 % → 0 % | 15.3 px | 0.65 | 0.08 | 163 |
| pressure swell | 4 % → 0 % | 14.9 px | 0.65 | 0.10 | 88 |
| fast wave | 8 % → 0 % | 8.9 px | 0.65 | 0.04 | 235 |
| slow wave | 12 % → 1 % | 13.6 px | 0.65 | 0.09 | 443 |
| spiral | 16 % → 1 % | 10.4 px | 0.65 | 0.04 | 465 |
| loop | 9 % → 2 % | 12.3 px | 0.65 | 0.17 | 750 |
| tilted | 5 % → 4 % | 13.0 px | 0.65 | 0.95 | 215 |
| over the wet one | 9 % → 3 % | 13.2 px | 0.65 | 0.27 | 121 |
| long, no reload | 18 % → 2 % | 8.3 px | 0.65 | 0.12 | 696 | quarters: 0.19 → 0.14 → 0.11 → 0.10

Numbers say: light vs heavy: width 10.1 → 15.3 px, dark 0.65 → 0.65.

## Brush Artist · Refs · #13 Henry Ward blue streaky form
Gouache · 50 px · 45.3 s

![Brush Artist · Refs · #13 Henry Ward blue streaky form](Brush-Artist-Refs-13-Henry-Ward-blue-streaky-form.png)

A light paint: laid on a grey sheet (on white it cannot be seen); **dark** = how far it is from the grey either way.

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 11 % → 5 % | 31.5 px | 0.34 | 0.44 | 214 |
| heavy line | 14 % → 9 % | 39.8 px | 0.34 | 0.63 | 221 |
| pressure swell | 11 % → 8 % | 40.2 px | 0.34 | 0.70 | 133 |
| fast wave | 14 % → 5 % | 16.6 px | 0.34 | 0.35 | 518 |
| slow wave | 31 % → 16 % | 35.5 px | 0.34 | 0.51 | 989 |
| spiral | 37 % → 17 % | 24.6 px | 0.34 | 0.46 | 902 |
| loop | 25 % → 15 % | 32.0 px | 0.34 | 0.61 | 706 |
| tilted | 10 % → 10 % | 26.5 px | 0.34 | 1.02 | 211 |
| over the wet one | 23 % → 18 % | 36.5 px | 0.34 | 0.79 | 178 |
| long, no reload | 42 % → 21 % | 18.7 px | 0.34 | 0.49 | 997 | quarters: 0.01 → 0.02 → 0.02 → 0.02

Numbers say: light vs heavy: width 31.5 → 39.8 px, dark 0.34 → 0.34; the long stroke does not run out of paint.

## Brush Artist · Refs · #14 Henry Ward olive totem
Heavy acrylic · 48 px · 23.1 s

![Brush Artist · Refs · #14 Henry Ward olive totem](Brush-Artist-Refs-14-Henry-Ward-olive-totem.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 16 % → 15 % | 46.8 px | 0.31 | 0.95 | 200 |
| heavy line | 17 % → 16 % | 49.8 px | 0.31 | 0.95 | 218 |
| pressure swell | 13 % → 13 % | 49.6 px | 0.32 | 0.96 | 119 |
| fast wave | 39 % → 31 % | 44.9 px | 0.30 | 0.79 | 539 |
| slow wave | 39 % → 32 % | 45.4 px | 0.30 | 0.81 | 932 |
| spiral | 59 % → 32 % | 38.7 px | 0.30 | 0.55 | 907 |
| loop | 33 % → 29 % | 42.7 px | 0.30 | 0.89 | 551 |
| tilted | 14 % → 14 % | 39.5 px | 0.31 | 1.00 | 219 |
| over the wet one | 30 % → 28 % | 43.3 px | 0.31 | 0.94 | 168 |
| long, no reload | 68 % → 33 % | 30.6 px | 0.30 | 0.48 | 1608 | quarters: 0.25 → 0.18 → 0.09 → 0.04

Numbers say: light vs heavy: width 46.8 → 49.8 px, dark 0.31 → 0.31; pressure barely changes the width.

## Brush Artist · Refs · #15 Ultramarine brush script
Ink · 4 px · 25.9 s

![Brush Artist · Refs · #15 Ultramarine brush script](Brush-Artist-Refs-15-Ultramarine-brush-script.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 1 % → 3 % | 2.2 px | 0.55 | 3.90 | 39 |
| heavy line | 6 % → 6 % | 16.7 px | 0.58 | 0.99 | 47 |
| pressure swell | 3 % → 4 % | 12.1 px | 0.64 | 1.15 | 33 |
| fast wave | 9 % → 7 % | 10.6 px | 0.54 | 0.81 | 318 |
| slow wave | 7 % → 7 % | 8.4 px | 0.54 | 0.93 | 129 |
| spiral | 11 % → 7 % | 7.2 px | 0.52 | 0.66 | 156 |
| loop | 7 % → 7 % | 9.2 px | 0.53 | 0.98 | 122 |
| tilted | 3 % → 3 % | 8.2 px | 0.62 | 1.02 | 42 |
| over the wet one | 7 % → 7 % | 11.5 px | 0.62 | 1.05 | 41 |
| long, no reload | 16 % → 8 % | 7.3 px | 0.50 | 0.48 | 230 | quarters: 0.15 → 0.04 → 0.01 → 0.00

Numbers say: light vs heavy: width 2.2 → 16.7 px, dark 0.55 → 0.58; wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #18 Blue oil-stick scribbles
Pastel · 10 px · 14.4 s

![Brush Artist · Refs · #18 Blue oil-stick scribbles](Brush-Artist-Refs-18-Blue-oil-stick-scribbles.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 1 % → 1 % | 2.9 px | 0.52 | 1.00 | 28 |
| heavy line | 2 % → 2 % | 5.5 px | 0.53 | 1.00 | 32 |
| pressure swell | 1 % → 1 % | 5.0 px | 0.53 | 1.00 | 21 |
| fast wave | 4 % → 4 % | 4.8 px | 0.53 | 1.00 | 138 |
| slow wave | 4 % → 4 % | 4.4 px | 0.53 | 1.00 | 83 |
| spiral | 7 % → 7 % | 4.5 px | 0.52 | 1.00 | 150 |
| loop | 3 % → 3 % | 4.5 px | 0.52 | 1.00 | 79 |
| tilted | 2 % → 2 % | 4.7 px | 0.53 | 1.00 | 41 |
| over the wet one | 3 % → 3 % | 4.7 px | 0.53 | 1.00 | 32 |
| long, no reload | 10 % → 10 % | 4.4 px | 0.53 | 1.00 | 247 | quarters: 0.06 → 0.06 → 0.06 → 0.06

Numbers say: light vs heavy: width 2.9 → 5.5 px, dark 0.52 → 0.53; the long stroke does not run out of paint.

## Brush Artist · Refs · #20 Orange-red crayon scribble
Pastel · 14 px · 17.3 s

![Brush Artist · Refs · #20 Orange-red crayon scribble](Brush-Artist-Refs-20-Orange-red-crayon-scribble.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 1 % → 1 % | 4.0 px | 0.53 | 1.00 | 32 |
| heavy line | 3 % → 3 % | 8.0 px | 0.53 | 1.00 | 39 |
| pressure swell | 2 % → 2 % | 7.6 px | 0.53 | 1.00 | 44 |
| fast wave | 6 % → 6 % | 7.2 px | 0.53 | 1.00 | 180 |
| slow wave | 6 % → 6 % | 6.6 px | 0.53 | 1.00 | 144 |
| spiral | 9 % → 9 % | 6.2 px | 0.53 | 1.00 | 208 |
| loop | 5 % → 5 % | 6.2 px | 0.53 | 1.00 | 109 |
| tilted | 2 % → 2 % | 5.6 px | 0.53 | 1.00 | 63 |
| over the wet one | 4 % → 4 % | 6.6 px | 0.53 | 1.00 | 41 |
| long, no reload | 13 % → 13 % | 5.7 px | 0.53 | 1.00 | 260 | quarters: 0.07 → 0.07 → 0.08 → 0.08

Numbers say: light vs heavy: width 4.0 → 8.0 px, dark 0.53 → 0.53; the long stroke does not run out of paint.

## Brush Artist · Refs · #21 Gritty black contours
Gouache · 12 px · 35.2 s

![Brush Artist · Refs · #21 Gritty black contours](Brush-Artist-Refs-21-Gritty-black-contours.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 1 % → 0 % | 3.3 px | 0.81 | 0.08 | 156 |
| heavy line | 2 % → 0 % | 5.2 px | 0.81 | 0.03 | 165 |
| pressure swell | 1 % → 0 % | 5.4 px | 0.81 | 0.04 | 87 |
| fast wave | 2 % → 0 % | 2.7 px | 0.81 | 0.01 | 335 |
| slow wave | 4 % → 0 % | 4.4 px | 0.81 | 0.04 | 318 |
| spiral | 5 % → 0 % | 3.1 px | 0.81 | 0.02 | 650 |
| loop | 3 % → 0 % | 4.1 px | 0.81 | 0.02 | 367 |
| tilted | 2 % → 2 % | 4.8 px | 0.81 | 0.93 | 188 |
| over the wet one | 3 % → 0 % | 4.7 px | 0.81 | 0.11 | 223 |
| long, no reload | 6 % → 0 % | 2.7 px | 0.81 | 0.06 | 724 | quarters: 0.09 → 0.06 → 0.05 → 0.04

Numbers say: light vs heavy: width 3.3 → 5.2 px, dark 0.81 → 0.81.

## Brush Artist · Refs · #22 Bold black brush poster
Ink · 20 px · 43.2 s

![Brush Artist · Refs · #22 Bold black brush poster](Brush-Artist-Refs-22-Bold-black-brush-poster.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 3 % → 5 % | 9.6 px | 0.79 | 1.64 | 57 |
| heavy line | 15 % → 15 % | 44.6 px | 0.88 | 0.99 | 134 |
| pressure swell | 9 % → 9 % | 31.9 px | 0.87 | 1.04 | 101 |
| fast wave | 27 % → 27 % | 31.7 px | 0.87 | 0.98 | 345 |
| slow wave | 22 % → 22 % | 25.4 px | 0.87 | 0.98 | 350 |
| spiral | 34 % → 32 % | 22.4 px | 0.87 | 0.94 | 430 |
| loop | 20 % → 20 % | 26.4 px | 0.88 | 1.00 | 167 |
| tilted | 8 % → 8 % | 23.1 px | 0.88 | 1.01 | 150 |
| over the wet one | 19 % → 19 % | 30.4 px | 0.88 | 1.00 | 145 |
| long, no reload | 45 % → 38 % | 20.3 px | 0.86 | 0.83 | 1087 | quarters: 0.54 → 0.45 → 0.35 → 0.26

Numbers say: light vs heavy: width 9.6 → 44.6 px, dark 0.79 → 0.88; wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #23 Dry white on orange + black line
Gouache · 50 px · 36.7 s

![Brush Artist · Refs · #23 Dry white on orange + black line](Brush-Artist-Refs-23-Dry-white-on-orange-black-line.png)

A light paint: laid on a grey sheet (on white it cannot be seen); **dark** = how far it is from the grey either way.

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 5 % → 0 % | 15.7 px | 0.42 | 0.02 | 138 |
| heavy line | 9 % → 0 % | 25.3 px | 0.42 | 0.00 | 374 |
| pressure swell | 6 % → 0 % | 23.8 px | 0.41 | 0.00 | 147 |
| fast wave | 12 % → 0 % | 13.7 px | 0.41 | 0.01 | 626 |
| slow wave | 19 % → 0 % | 21.6 px | 0.41 | 0.02 | 2048 |
| spiral | 24 % → 0 % | 15.6 px | 0.40 | 0.01 | 1744 |
| loop | 15 % → 1 % | 19.8 px | 0.40 | 0.04 | 697 |
| tilted | 6 % → 6 % | 17.5 px | 0.40 | 0.94 | 248 |
| over the wet one | 14 % → 1 % | 20.6 px | 0.40 | 0.09 | 226 |
| long, no reload | 27 % → 1 % | 12.3 px | 0.40 | 0.05 | 1356 | quarters: 0.02 → 0.03 → 0.03 → 0.03

Numbers say: light vs heavy: width 15.7 → 25.3 px, dark 0.42 → 0.42; the long stroke does not run out of paint.

## Brush Artist · Refs · #24 Picasso flat oil
Oil · 34 px · 27.0 s

![Brush Artist · Refs · #24 Picasso flat oil](Brush-Artist-Refs-24-Picasso-flat-oil.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 11 % → 12 % | 33.4 px | 0.40 | 1.00 | 286 |
| heavy line | 12 % → 13 % | 36.2 px | 0.40 | 1.00 | 323 |
| pressure swell | 10 % → 10 % | 35.8 px | 0.41 | 1.00 | 184 |
| fast wave | 30 % → 30 % | 34.6 px | 0.41 | 1.00 | 456 |
| slow wave | 31 % → 31 % | 35.4 px | 0.40 | 1.00 | 770 |
| spiral | 52 % → 52 % | 34.0 px | 0.40 | 1.00 | 664 |
| loop | 25 % → 25 % | 32.7 px | 0.41 | 1.00 | 371 |
| tilted | 12 % → 12 % | 33.0 px | 0.40 | 1.00 | 244 |
| over the wet one | 23 % → 23 % | 31.9 px | 0.40 | 1.00 | 165 |
| long, no reload | 62 % → 62 % | 27.7 px | 0.39 | 1.00 | 1173 | quarters: 0.28 → 0.27 → 0.26 → 0.24

Numbers say: light vs heavy: width 33.4 → 36.2 px, dark 0.40 → 0.40; pressure barely changes the width; the long stroke does not run out of paint.

## Brush Artist · Refs · #25 Yellow heavy flat stroke
Heavy acrylic · 110 px · 43.2 s

![Brush Artist · Refs · #25 Yellow heavy flat stroke](Brush-Artist-Refs-25-Yellow-heavy-flat-stroke.png)

A light paint: laid on a grey sheet (on white it cannot be seen); **dark** = how far it is from the grey either way.

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 38 % → 39 % | 109.9 px | 0.30 | 1.02 | 543 |
| heavy line | 39 % → 39 % | 114.6 px | 0.30 | 0.98 | 686 |
| pressure swell | 31 % → 32 % | 115.0 px | 0.30 | 1.05 | 311 |
| fast wave | 75 % → 78 % | 86.6 px | 0.30 | 1.04 | 1043 |
| slow wave | 76 % → 74 % | 87.5 px | 0.30 | 0.98 | 2702 |
| spiral | 87 % → 83 % | 57.1 px | 0.29 | 0.96 | 2383 |
| loop | 65 % → 64 % | 83.7 px | 0.30 | 0.99 | 1387 |
| tilted | 29 % → 29 % | 81.2 px | 0.30 | 1.00 | 714 |
| over the wet one | 62 % → 61 % | 91.1 px | 0.30 | 0.98 | 438 |
| long, no reload | 100 % → 99 % | 44.7 px | 0.29 | 0.99 | 2558 | quarters: 0.00 → 0.00 → 0.00 → 0.00

Numbers say: light vs heavy: width 109.9 → 114.6 px, dark 0.30 → 0.30; pressure barely changes the width.

## Brush Artist · Refs · #27 Orange impasto swatch
Heavy acrylic · 60 px · 31.4 s

![Brush Artist · Refs · #27 Orange impasto swatch](Brush-Artist-Refs-27-Orange-impasto-swatch.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 21 % → 21 % | 59.7 px | 0.35 | 1.00 | 285 |
| heavy line | 22 % → 22 % | 62.5 px | 0.35 | 1.00 | 244 |
| pressure swell | 17 % → 17 % | 63.2 px | 0.36 | 1.01 | 192 |
| fast wave | 49 % → 48 % | 56.3 px | 0.35 | 0.98 | 516 |
| slow wave | 49 % → 48 % | 57.1 px | 0.35 | 0.98 | 1102 |
| spiral | 70 % → 63 % | 46.1 px | 0.34 | 0.91 | 1574 |
| loop | 42 % → 40 % | 53.9 px | 0.35 | 0.97 | 555 |
| tilted | 17 % → 17 % | 46.9 px | 0.35 | 1.00 | 317 |
| over the wet one | 36 % → 36 % | 53.9 px | 0.35 | 1.00 | 242 |
| long, no reload | 86 % → 76 % | 38.6 px | 0.35 | 0.88 | 2034 | quarters: 0.33 → 0.31 → 0.29 → 0.27

Numbers say: light vs heavy: width 59.7 → 62.5 px, dark 0.35 → 0.35; pressure barely changes the width.

## Brush Artist · Refs · #28 Miles Davis black lines
Ink · 22 px · 31.1 s

![Brush Artist · Refs · #28 Miles Davis black lines](Brush-Artist-Refs-28-Miles-Davis-black-lines.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 4 % → 6 % | 12.3 px | 0.81 | 1.49 | 50 |
| heavy line | 17 % → 17 % | 49.0 px | 0.88 | 0.99 | 161 |
| pressure swell | 10 % → 10 % | 35.9 px | 0.87 | 1.03 | 58 |
| fast wave | 31 % → 30 % | 35.5 px | 0.87 | 0.98 | 195 |
| slow wave | 25 % → 25 % | 28.7 px | 0.87 | 0.99 | 245 |
| spiral | 39 % → 37 % | 25.5 px | 0.87 | 0.95 | 254 |
| loop | 23 % → 23 % | 29.6 px | 0.88 | 1.00 | 129 |
| tilted | 9 % → 9 % | 25.3 px | 0.88 | 1.01 | 80 |
| over the wet one | 21 % → 21 % | 34.1 px | 0.88 | 1.00 | 81 |
| long, no reload | 51 % → 43 % | 22.9 px | 0.86 | 0.84 | 393 | quarters: 0.59 → 0.51 → 0.40 → 0.31

Numbers say: light vs heavy: width 12.3 → 49.0 px, dark 0.81 → 0.88.

## Brush Artist · Refs · #29 Shrigley magenta asterisk
Watercolor · 70 px · 41.4 s

![Brush Artist · Refs · #29 Shrigley magenta asterisk](Brush-Artist-Refs-29-Shrigley-magenta-asterisk.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 10 % → 13 % | 28.0 px | 0.65 | 1.36 | 56 |
| heavy line | 17 % → 18 % | 50.3 px | 0.64 | 1.03 | 181 |
| pressure swell | 11 % → 12 % | 41.1 px | 0.65 | 1.13 | 88 |
| fast wave | 38 % → 38 % | 43.8 px | 0.64 | 1.01 | 318 |
| slow wave | 35 % → 39 % | 41.0 px | 0.65 | 1.10 | 418 |
| spiral | 61 % → 61 % | 40.0 px | 0.64 | 1.01 | 432 |
| loop | 31 % → 32 % | 40.2 px | 0.65 | 1.03 | 271 |
| tilted | 18 % → 18 % | 49.0 px | 0.65 | 1.00 | 346 |
| over the wet one | 31 % → 34 % | 38.4 px | 0.65 | 1.07 | 179 |
| long, no reload | 75 % → 75 % | 33.6 px | 0.64 | 1.00 | 726 | quarters: 0.55 → 0.53 → 0.52 → 0.49

Numbers say: light vs heavy: width 28.0 → 50.3 px, dark 0.65 → 0.64; the long stroke does not run out of paint.

## Brush Artist · Refs · #30 Red gouache face patch
Gouache · 60 px · 46.9 s

![Brush Artist · Refs · #30 Red gouache face patch](Brush-Artist-Refs-30-Red-gouache-face-patch.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 16 % → 15 % | 47.0 px | 0.49 | 0.91 | 159 |
| heavy line | 25 % → 20 % | 74.0 px | 0.49 | 0.80 | 273 |
| pressure swell | 19 % → 17 % | 72.7 px | 0.49 | 0.86 | 199 |
| fast wave | 49 % → 28 % | 56.2 px | 0.49 | 0.58 | 697 |
| slow wave | 48 % → 28 % | 55.4 px | 0.49 | 0.59 | 1309 |
| spiral | 60 % → 28 % | 39.4 px | 0.49 | 0.47 | 1098 |
| loop | 40 % → 29 % | 51.6 px | 0.49 | 0.74 | 479 |
| tilted | 16 % → 17 % | 46.0 px | 0.49 | 1.00 | 388 |
| over the wet one | 36 % → 32 % | 55.3 px | 0.49 | 0.89 | 250 |
| long, no reload | 67 % → 30 % | 30.1 px | 0.49 | 0.44 | 1188 | quarters: 0.43 → 0.39 → 0.32 → 0.26

Numbers say: light vs heavy: width 47.0 → 74.0 px, dark 0.49 → 0.49.

## Brush Artist · Refs · #31 Warhol blotted line
Ink · 6 px · 27.5 s

![Brush Artist · Refs · #31 Warhol blotted line](Brush-Artist-Refs-31-Warhol-blotted-line.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 1 % → 3 % | 2.7 px | 0.75 | 3.30 | 43 |
| heavy line | 7 % → 7 % | 20.7 px | 0.83 | 0.98 | 76 |
| pressure swell | 4 % → 4 % | 14.8 px | 0.84 | 1.12 | 52 |
| fast wave | 12 % → 9 % | 13.9 px | 0.82 | 0.76 | 172 |
| slow wave | 10 % → 8 % | 11.2 px | 0.80 | 0.84 | 164 |
| spiral | 15 % → 8 % | 9.7 px | 0.80 | 0.57 | 316 |
| loop | 9 % → 9 % | 11.9 px | 0.80 | 0.93 | 193 |
| tilted | 3 % → 3 % | 8.8 px | 0.84 | 1.03 | 71 |
| over the wet one | 8 % → 8 % | 14.4 px | 0.84 | 1.02 | 67 |
| long, no reload | 21 % → 9 % | 9.6 px | 0.78 | 0.43 | 354 | quarters: 0.25 → 0.13 → 0.05 → 0.01

Numbers say: light vs heavy: width 2.7 → 20.7 px, dark 0.75 → 0.83; wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #32 Thick orange swipes
Heavy acrylic · 90 px · 42.2 s

![Brush Artist · Refs · #32 Thick orange swipes](Brush-Artist-Refs-32-Thick-orange-swipes.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 31 % → 32 % | 89.3 px | 0.38 | 1.03 | 438 |
| heavy line | 32 % → 31 % | 92.9 px | 0.38 | 0.98 | 390 |
| pressure swell | 25 % → 26 % | 93.5 px | 0.39 | 1.04 | 225 |
| fast wave | 65 % → 67 % | 75.6 px | 0.38 | 1.02 | 1383 |
| slow wave | 66 % → 65 % | 76.0 px | 0.38 | 0.98 | 1520 |
| spiral | 80 % → 78 % | 52.8 px | 0.38 | 0.98 | 1902 |
| loop | 57 % → 56 % | 73.4 px | 0.38 | 0.99 | 970 |
| tilted | 24 % → 24 % | 66.2 px | 0.38 | 1.00 | 499 |
| over the wet one | 51 % → 51 % | 77.2 px | 0.38 | 0.99 | 454 |
| long, no reload | 97 % → 95 % | 43.4 px | 0.38 | 0.98 | 3353 | quarters: 0.38 → 0.38 → 0.37 → 0.37

Numbers say: light vs heavy: width 89.3 → 92.9 px, dark 0.38 → 0.38; pressure barely changes the width; the long stroke does not run out of paint.

## Brush Artist · Refs · #33 Red wet-in-wet band
Watercolor · 80 px · 54.7 s

![Brush Artist · Refs · #33 Red wet-in-wet band](Brush-Artist-Refs-33-Red-wet-in-wet-band.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 19 % → 31 % | 55.6 px | 0.58 | 1.61 | 155 |
| heavy line | 29 % → 39 % | 83.7 px | 0.59 | 1.35 | 240 |
| pressure swell | 19 % → 27 % | 71.5 px | 0.61 | 1.42 | 242 |
| fast wave | 58 % → 74 % | 67.5 px | 0.61 | 1.27 | 515 |
| slow wave | 57 % → 72 % | 65.7 px | 0.63 | 1.26 | 811 |
| spiral | 75 % → 84 % | 49.6 px | 0.64 | 1.12 | 975 |
| loop | 51 % → 63 % | 66.4 px | 0.63 | 1.22 | 450 |
| tilted | 24 % → 25 % | 66.3 px | 0.60 | 1.03 | 367 |
| over the wet one | 48 % → 67 % | 66.7 px | 0.60 | 1.40 | 241 |
| long, no reload | 95 % → 99 % | 42.6 px | 0.66 | 1.04 | 1789 | quarters: 0.68 → 0.68 → 0.68 → 0.64

Numbers say: light vs heavy: width 55.6 → 83.7 px, dark 0.58 → 0.59; the long stroke does not run out of paint; wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #34 Magenta oil patches
Oil · 60 px · 28.9 s

![Brush Artist · Refs · #34 Magenta oil patches](Brush-Artist-Refs-34-Magenta-oil-patches.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 20 % → 20 % | 58.8 px | 0.61 | 1.01 | 216 |
| heavy line | 22 % → 22 % | 63.1 px | 0.61 | 1.00 | 289 |
| pressure swell | 17 % → 17 % | 62.7 px | 0.62 | 1.01 | 233 |
| fast wave | 49 % → 50 % | 56.7 px | 0.62 | 1.02 | 615 |
| slow wave | 49 % → 49 % | 57.1 px | 0.62 | 1.00 | 1098 |
| spiral | 71 % → 71 % | 46.9 px | 0.61 | 1.00 | 1034 |
| loop | 42 % → 42 % | 54.3 px | 0.62 | 1.00 | 783 |
| tilted | 18 % → 18 % | 49.8 px | 0.61 | 1.00 | 361 |
| over the wet one | 37 % → 37 % | 53.2 px | 0.61 | 1.00 | 217 |
| long, no reload | 88 % → 88 % | 39.2 px | 0.62 | 1.00 | 2357 | quarters: 0.59 → 0.58 → 0.56 → 0.54

Numbers say: light vs heavy: width 58.8 → 63.1 px, dark 0.61 → 0.61; pressure barely changes the width; the long stroke does not run out of paint.

## Brush Artist · Refs · #35 Red band with runs
Watercolor · 70 px · 48.5 s

![Brush Artist · Refs · #35 Red band with runs](Brush-Artist-Refs-35-Red-band-with-runs.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 17 % → 33 % | 48.3 px | 0.48 | 2.00 | 167 |
| heavy line | 25 % → 42 % | 73.9 px | 0.49 | 1.64 | 206 |
| pressure swell | 17 % → 26 % | 63.0 px | 0.53 | 1.52 | 121 |
| fast wave | 54 % → 73 % | 61.9 px | 0.52 | 1.36 | 445 |
| slow wave | 52 % → 71 % | 59.9 px | 0.55 | 1.38 | 831 |
| spiral | 72 % → 89 % | 47.4 px | 0.55 | 1.24 | 735 |
| loop | 47 % → 72 % | 61.2 px | 0.51 | 1.52 | 359 |
| tilted | 21 % → 22 % | 57.8 px | 0.50 | 1.06 | 339 |
| over the wet one | 43 % → 70 % | 62.0 px | 0.50 | 1.63 | 285 |
| long, no reload | 92 % → 99 % | 41.4 px | 0.59 | 1.07 | 998 | quarters: 0.60 → 0.60 → 0.60 → 0.56

Numbers say: light vs heavy: width 48.3 → 73.9 px, dark 0.48 → 0.49; the long stroke does not run out of paint; wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #36 Magenta letters flat brush
Gouache · 36 px · 33.3 s

![Brush Artist · Refs · #36 Magenta letters flat brush](Brush-Artist-Refs-36-Magenta-letters-flat-brush.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 10 % → 10 % | 29.1 px | 0.45 | 0.98 | 92 |
| heavy line | 17 % → 14 % | 49.1 px | 0.45 | 0.85 | 105 |
| pressure swell | 13 % → 12 % | 49.4 px | 0.45 | 0.89 | 66 |
| fast wave | 35 % → 19 % | 41.0 px | 0.45 | 0.54 | 237 |
| slow wave | 35 % → 19 % | 40.0 px | 0.45 | 0.54 | 383 |
| spiral | 46 % → 19 % | 30.5 px | 0.45 | 0.42 | 587 |
| loop | 27 % → 20 % | 35.4 px | 0.45 | 0.72 | 197 |
| tilted | 11 % → 11 % | 30.0 px | 0.45 | 1.00 | 102 |
| over the wet one | 24 % → 23 % | 38.1 px | 0.45 | 0.92 | 91 |
| long, no reload | 47 % → 19 % | 20.9 px | 0.45 | 0.40 | 549 | quarters: 0.29 → 0.26 → 0.22 → 0.18

Numbers say: light vs heavy: width 29.1 → 49.1 px, dark 0.45 → 0.45.

## Brush Artist · Refs · #37 Oil still life dabs
Oil · 40 px · 21.4 s

![Brush Artist · Refs · #37 Oil still life dabs](Brush-Artist-Refs-37-Oil-still-life-dabs.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 14 % → 14 % | 39.4 px | 0.39 | 1.00 | 142 |
| heavy line | 15 % → 15 % | 42.6 px | 0.39 | 1.00 | 155 |
| pressure swell | 11 % → 11 % | 42.0 px | 0.40 | 1.00 | 113 |
| fast wave | 35 % → 35 % | 40.4 px | 0.39 | 1.00 | 411 |
| slow wave | 35 % → 35 % | 40.8 px | 0.39 | 1.00 | 673 |
| spiral | 59 % → 59 % | 39.1 px | 0.38 | 1.00 | 628 |
| loop | 29 % → 29 % | 37.8 px | 0.39 | 1.00 | 346 |
| tilted | 13 % → 14 % | 37.6 px | 0.39 | 1.00 | 175 |
| over the wet one | 27 % → 27 % | 37.3 px | 0.39 | 1.00 | 155 |
| long, no reload | 69 % → 69 % | 31.1 px | 0.37 | 1.00 | 1040 | quarters: 0.31 → 0.30 → 0.28 → 0.25

Numbers say: light vs heavy: width 39.4 → 42.6 px, dark 0.39 → 0.39; pressure barely changes the width.

## Brush Artist · Refs · #38 Sanguine drawing
Pastel · 6 px · 9.5 s

![Brush Artist · Refs · #38 Sanguine drawing](Brush-Artist-Refs-38-Sanguine-drawing.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 1 % → 1 % | 2.0 px | 0.61 | 1.00 | 27 |
| heavy line | 1 % → 1 % | 3.5 px | 0.62 | 1.00 | 20 |
| pressure swell | 1 % → 1 % | 3.3 px | 0.62 | 1.00 | 12 |
| fast wave | 3 % → 3 % | 3.2 px | 0.61 | 1.00 | 41 |
| slow wave | 3 % → 3 % | 3.0 px | 0.61 | 1.00 | 41 |
| spiral | 4 % → 4 % | 2.9 px | 0.61 | 1.00 | 72 |
| loop | 2 % → 2 % | 3.0 px | 0.61 | 1.00 | 38 |
| tilted | 1 % → 1 % | 3.4 px | 0.62 | 1.00 | 20 |
| over the wet one | 2 % → 2 % | 2.9 px | 0.62 | 1.00 | 17 |
| long, no reload | 7 % → 7 % | 3.0 px | 0.61 | 1.00 | 147 | quarters: 0.04 → 0.05 → 0.05 → 0.05

Numbers say: light vs heavy: width 2.0 → 3.5 px, dark 0.61 → 0.62; the long stroke does not run out of paint.

## Brush Artist · Refs · #39 Very thick impasto
Heavy acrylic · 60 px · 26.6 s

![Brush Artist · Refs · #39 Very thick impasto](Brush-Artist-Refs-39-Very-thick-impasto.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 21 % → 21 % | 59.8 px | 0.61 | 1.02 | 239 |
| heavy line | 22 % → 22 % | 62.6 px | 0.61 | 1.02 | 207 |
| pressure swell | 17 % → 17 % | 63.3 px | 0.63 | 1.03 | 153 |
| fast wave | 49 % → 48 % | 56.4 px | 0.62 | 0.99 | 590 |
| slow wave | 50 % → 49 % | 57.3 px | 0.62 | 0.98 | 845 |
| spiral | 70 % → 66 % | 46.3 px | 0.62 | 0.94 | 857 |
| loop | 42 % → 41 % | 54.0 px | 0.62 | 0.97 | 420 |
| tilted | 17 % → 17 % | 46.9 px | 0.62 | 1.00 | 245 |
| over the wet one | 36 % → 37 % | 54.0 px | 0.62 | 1.02 | 218 |
| long, no reload | 87 % → 80 % | 38.8 px | 0.62 | 0.93 | 1492 | quarters: 0.58 → 0.57 → 0.55 → 0.53

Numbers say: light vs heavy: width 59.8 → 62.6 px, dark 0.61 → 0.61; pressure barely changes the width; the long stroke does not run out of paint.

## Brush Artist · Refs · #40 Watercolour blooms
Watercolor · 90 px · 48.0 s

![Brush Artist · Refs · #40 Watercolour blooms](Brush-Artist-Refs-40-Watercolour-blooms.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 22 % → 34 % | 63.3 px | 0.10 | 1.54 | 157 |
| heavy line | 33 % → 42 % | 94.9 px | 0.11 | 1.28 | 325 |
| pressure swell | 22 % → 30 % | 84.1 px | 0.12 | 1.34 | 215 |
| fast wave | 64 % → 79 % | 73.9 px | 0.11 | 1.23 | 622 |
| slow wave | 63 % → 76 % | 72.4 px | 0.16 | 1.21 | 904 |
| spiral | 79 % → 87 % | 52.1 px | 0.15 | 1.10 | 883 |
| loop | 56 % → 66 % | 72.5 px | 0.13 | 1.18 | 475 |
| tilted | 26 % → 27 % | 73.1 px | 0.13 | 1.03 | 344 |
| over the wet one | 53 % → 72 % | 73.8 px | 0.13 | 1.36 | 207 |
| long, no reload | 97 % → 100 % | 43.6 px | 0.17 | 1.02 | 1477 | quarters: 0.21 → 0.19 → 0.17 → 0.13

Numbers say: light vs heavy: width 63.3 → 94.9 px, dark 0.10 → 0.11; wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #41 Coloured pencil hatching
Pastel · 4 px · 8.8 s

![Brush Artist · Refs · #41 Coloured pencil hatching](Brush-Artist-Refs-41-Coloured-pencil-hatching.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 1 % → 1 % | 1.6 px | 0.42 | 1.00 | 17 |
| heavy line | 1 % → 1 % | 2.6 px | 0.43 | 1.00 | 15 |
| pressure swell | 1 % → 1 % | 2.1 px | 0.43 | 1.00 | 9 |
| fast wave | 2 % → 2 % | 2.2 px | 0.42 | 1.00 | 33 |
| slow wave | 2 % → 2 % | 2.1 px | 0.43 | 1.00 | 33 |
| spiral | 3 % → 3 % | 2.1 px | 0.43 | 1.00 | 52 |
| loop | 2 % → 2 % | 2.2 px | 0.43 | 1.00 | 26 |
| tilted | 1 % → 1 % | 3.0 px | 0.42 | 1.00 | 24 |
| over the wet one | 2 % → 2 % | 2.2 px | 0.42 | 1.00 | 12 |
| long, no reload | 5 % → 5 % | 2.3 px | 0.43 | 1.00 | 77 | quarters: 0.02 → 0.02 → 0.02 → 0.03

Numbers say: light vs heavy: width 1.6 → 2.6 px, dark 0.42 → 0.43; the long stroke does not run out of paint.

## Brush Artist · Refs · #42 Oil pastel shaggy
Pastel · 18 px · 9.8 s

![Brush Artist · Refs · #42 Oil pastel shaggy](Brush-Artist-Refs-42-Oil-pastel-shaggy.png)

A light paint: laid on a grey sheet (on white it cannot be seen); **dark** = how far it is from the grey either way.

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 2 % → 2 % | 5.1 px | 0.35 | 1.00 | 22 |
| heavy line | 4 % → 4 % | 10.7 px | 0.36 | 1.00 | 26 |
| pressure swell | 3 % → 3 % | 9.5 px | 0.36 | 1.00 | 18 |
| fast wave | 8 % → 8 % | 9.0 px | 0.36 | 1.00 | 94 |
| slow wave | 7 % → 7 % | 8.2 px | 0.36 | 1.00 | 110 |
| spiral | 12 % → 12 % | 7.7 px | 0.36 | 1.00 | 156 |
| loop | 6 % → 6 % | 7.9 px | 0.36 | 1.00 | 86 |
| tilted | 2 % → 2 % | 6.9 px | 0.36 | 1.00 | 32 |
| over the wet one | 6 % → 6 % | 8.5 px | 0.36 | 1.00 | 27 |
| long, no reload | 15 % → 15 % | 6.9 px | 0.36 | 1.00 | 161 | quarters: 0.00 → 0.00 → 0.00 → 0.00

Numbers say: light vs heavy: width 5.1 → 10.7 px, dark 0.35 → 0.36; the long stroke does not run out of paint.

## Brush Artist · Refs · #43 Dragged black ink blocks
Gouache · 70 px · 28.7 s

![Brush Artist · Refs · #43 Dragged black ink blocks](Brush-Artist-Refs-43-Dragged-black-ink-blocks.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 11 % → 0 % | 31.1 px | 0.65 | 0.03 | 126 |
| heavy line | 16 % → 1 % | 46.9 px | 0.65 | 0.08 | 315 |
| pressure swell | 12 % → 1 % | 44.8 px | 0.65 | 0.11 | 180 |
| fast wave | 22 % → 2 % | 25.8 px | 0.65 | 0.09 | 883 |
| slow wave | 34 % → 4 % | 39.7 px | 0.65 | 0.13 | 1261 |
| spiral | 40 % → 4 % | 26.3 px | 0.65 | 0.11 | 983 |
| loop | 28 % → 4 % | 36.5 px | 0.65 | 0.14 | 500 |
| tilted | 10 % → 10 % | 28.3 px | 0.65 | 0.98 | 258 |
| over the wet one | 24 % → 9 % | 40.0 px | 0.65 | 0.36 | 235 |
| long, no reload | 47 % → 8 % | 20.9 px | 0.65 | 0.16 | 1281 | quarters: 0.45 → 0.36 → 0.28 → 0.23

Numbers say: light vs heavy: width 31.1 → 46.9 px, dark 0.65 → 0.65.

## Brush Artist · Refs · #44 Blue looping ribbon
Oil · 80 px · 27.9 s

![Brush Artist · Refs · #44 Blue looping ribbon](Brush-Artist-Refs-44-Blue-looping-ribbon.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 28 % → 29 % | 80.0 px | 0.72 | 1.04 | 473 |
| heavy line | 29 % → 29 % | 85.0 px | 0.72 | 1.00 | 516 |
| pressure swell | 23 % → 23 % | 84.4 px | 0.72 | 1.03 | 357 |
| fast wave | 63 % → 65 % | 72.4 px | 0.72 | 1.04 | 1012 |
| slow wave | 62 % → 62 % | 72.1 px | 0.73 | 1.00 | 1436 |
| spiral | 79 % → 79 % | 51.9 px | 0.72 | 1.00 | 1485 |
| loop | 54 % → 54 % | 69.7 px | 0.73 | 1.00 | 687 |
| tilted | 22 % → 22 % | 62.4 px | 0.72 | 1.00 | 366 |
| over the wet one | 47 % → 48 % | 70.0 px | 0.72 | 1.01 | 306 |
| long, no reload | 97 % → 97 % | 43.5 px | 0.73 | 1.00 | 1928 | quarters: 0.72 → 0.72 → 0.72 → 0.72

Numbers say: light vs heavy: width 80.0 → 85.0 px, dark 0.72 → 0.72; pressure barely changes the width; the long stroke does not run out of paint.

## Brush Artist · Refs · #45 Soft pastel pepper
Pastel · 40 px · 10.4 s

![Brush Artist · Refs · #45 Soft pastel pepper](Brush-Artist-Refs-45-Soft-pastel-pepper.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 4 % → 4 % | 11.3 px | 0.53 | 1.00 | 48 |
| heavy line | 8 % → 8 % | 23.0 px | 0.53 | 1.00 | 53 |
| pressure swell | 5 % → 5 % | 19.5 px | 0.53 | 1.00 | 38 |
| fast wave | 17 % → 17 % | 19.4 px | 0.53 | 1.00 | 131 |
| slow wave | 15 % → 15 % | 17.1 px | 0.53 | 1.00 | 270 |
| spiral | 25 % → 25 % | 16.3 px | 0.53 | 1.00 | 275 |
| loop | 12 % → 12 % | 16.1 px | 0.53 | 1.00 | 158 |
| tilted | 5 % → 5 % | 12.8 px | 0.53 | 1.00 | 66 |
| over the wet one | 11 % → 11 % | 17.7 px | 0.53 | 1.00 | 60 |
| long, no reload | 30 % → 30 % | 13.6 px | 0.53 | 1.00 | 327 | quarters: 0.18 → 0.18 → 0.18 → 0.18

Numbers say: light vs heavy: width 11.3 → 23.0 px, dark 0.53 → 0.53; the long stroke does not run out of paint.

## Brush Artist · Refs · #46 Red-brown ink lips
Watercolor · 50 px · 37.5 s

![Brush Artist · Refs · #46 Red-brown ink lips](Brush-Artist-Refs-46-Red-brown-ink-lips.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 12 % → 24 % | 33.6 px | 0.66 | 2.04 | 58 |
| heavy line | 19 % → 30 % | 54.1 px | 0.64 | 1.62 | 148 |
| pressure swell | 12 % → 21 % | 43.7 px | 0.67 | 1.76 | 88 |
| fast wave | 40 % → 61 % | 46.7 px | 0.66 | 1.50 | 296 |
| slow wave | 39 % → 59 % | 44.6 px | 0.68 | 1.54 | 383 |
| spiral | 63 % → 76 % | 41.7 px | 0.70 | 1.20 | 375 |
| loop | 35 % → 52 % | 44.9 px | 0.67 | 1.51 | 193 |
| tilted | 16 % → 17 % | 43.6 px | 0.66 | 1.07 | 141 |
| over the wet one | 33 % → 52 % | 47.6 px | 0.66 | 1.58 | 92 |
| long, no reload | 79 % → 95 % | 35.4 px | 0.70 | 1.21 | 550 | quarters: 0.71 → 0.71 → 0.70 → 0.65

Numbers say: light vs heavy: width 33.6 → 54.1 px, dark 0.66 → 0.64; the long stroke does not run out of paint; wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #47 Pink knife slabs
Heavy acrylic · 90 px · 29.0 s

![Brush Artist · Refs · #47 Pink knife slabs](Brush-Artist-Refs-47-Pink-knife-slabs.png)

A light paint: laid on a grey sheet (on white it cannot be seen); **dark** = how far it is from the grey either way.

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 30 % → 30 % | 88.0 px | 0.29 | 0.98 | 315 |
| heavy line | 31 % → 30 % | 90.3 px | 0.29 | 0.97 | 299 |
| pressure swell | 24 % → 25 % | 91.2 px | 0.28 | 1.01 | 152 |
| fast wave | 63 % → 62 % | 73.0 px | 0.28 | 0.98 | 551 |
| slow wave | 64 % → 61 % | 73.7 px | 0.27 | 0.96 | 975 |
| spiral | 77 % → 59 % | 50.8 px | 0.27 | 0.76 | 930 |
| loop | 55 % → 54 % | 71.8 px | 0.28 | 0.97 | 475 |
| tilted | 24 % → 24 % | 66.3 px | 0.29 | 1.00 | 259 |
| over the wet one | 51 % → 49 % | 74.8 px | 0.29 | 0.97 | 233 |
| long, no reload | 94 % → 78 % | 42.1 px | 0.26 | 0.83 | 1314 | quarters: 0.00 → 0.00 → 0.00 → 0.00

Numbers say: light vs heavy: width 88.0 → 90.3 px, dark 0.29 → 0.29; pressure barely changes the width; the long stroke does not run out of paint.

## Brush Artist · Refs · #48 Black bands with drips
Gouache · 70 px · 45.5 s

![Brush Artist · Refs · #48 Black bands with drips](Brush-Artist-Refs-48-Black-bands-with-drips.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 19 % → 18 % | 54.7 px | 0.68 | 0.94 | 171 |
| heavy line | 29 % → 24 % | 83.1 px | 0.68 | 0.85 | 237 |
| pressure swell | 23 % → 21 % | 86.1 px | 0.68 | 0.92 | 160 |
| fast wave | 54 % → 37 % | 62.8 px | 0.68 | 0.67 | 673 |
| slow wave | 54 % → 36 % | 61.9 px | 0.68 | 0.67 | 909 |
| spiral | 64 % → 35 % | 42.2 px | 0.68 | 0.54 | 824 |
| loop | 45 % → 37 % | 58.1 px | 0.68 | 0.82 | 422 |
| tilted | 19 % → 19 % | 52.5 px | 0.68 | 1.00 | 251 |
| over the wet one | 41 % → 38 % | 62.5 px | 0.68 | 0.92 | 199 |
| long, no reload | 74 % → 37 % | 33.4 px | 0.68 | 0.50 | 1213 | quarters: 0.64 → 0.61 → 0.54 → 0.44

Numbers say: light vs heavy: width 54.7 → 83.1 px, dark 0.68 → 0.68.

## Brush Artist · Refs · #49 Magenta letters round brush
Ink · 30 px · 36.4 s

![Brush Artist · Refs · #49 Magenta letters round brush](Brush-Artist-Refs-49-Magenta-letters-round-brush.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 6 % → 8 % | 17.5 px | 0.50 | 1.29 | 44 |
| heavy line | 21 % → 21 % | 62.0 px | 0.51 | 0.99 | 110 |
| pressure swell | 12 % → 13 % | 46.3 px | 0.52 | 1.02 | 66 |
| fast wave | 39 % → 38 % | 44.8 px | 0.51 | 0.99 | 184 |
| slow wave | 32 % → 31 % | 36.7 px | 0.51 | 0.99 | 302 |
| spiral | 50 % → 49 % | 33.2 px | 0.51 | 0.97 | 308 |
| loop | 29 % → 29 % | 37.8 px | 0.51 | 1.00 | 161 |
| tilted | 11 % → 11 % | 31.0 px | 0.52 | 1.01 | 158 |
| over the wet one | 26 % → 26 % | 42.0 px | 0.52 | 1.01 | 115 |
| long, no reload | 62 % → 56 % | 27.7 px | 0.50 | 0.91 | 608 | quarters: 0.41 → 0.36 → 0.30 → 0.25

Numbers say: light vs heavy: width 17.5 → 62.0 px, dark 0.50 → 0.51.

## Brush Artist · Refs · #50 Thick swipes on photo
Heavy acrylic · 40 px · 29.5 s

![Brush Artist · Refs · #50 Thick swipes on photo](Brush-Artist-Refs-50-Thick-swipes-on-photo.png)

A light paint: laid on a grey sheet (on white it cannot be seen); **dark** = how far it is from the grey either way.

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 14 % → 13 % | 39.4 px | 0.26 | 0.99 | 196 |
| heavy line | 14 % → 14 % | 41.6 px | 0.26 | 0.98 | 143 |
| pressure swell | 11 % → 11 % | 41.9 px | 0.25 | 0.99 | 98 |
| fast wave | 34 % → 31 % | 38.9 px | 0.25 | 0.93 | 407 |
| slow wave | 34 % → 33 % | 39.7 px | 0.26 | 0.95 | 739 |
| spiral | 59 % → 47 % | 38.9 px | 0.25 | 0.80 | 707 |
| loop | 28 % → 27 % | 36.9 px | 0.26 | 0.95 | 343 |
| tilted | 13 % → 13 % | 35.4 px | 0.26 | 1.00 | 313 |
| over the wet one | 26 % → 25 % | 36.8 px | 0.26 | 0.98 | 333 |
| long, no reload | 66 % → 46 % | 29.8 px | 0.24 | 0.69 | 2205 | quarters: 0.00 → 0.00 → 0.00 → 0.00

Numbers say: light vs heavy: width 39.4 → 41.6 px, dark 0.26 → 0.26; pressure barely changes the width; the long stroke does not run out of paint.

## Brush Artist · Refs · Drag #e8b4a8
Gouache · 40 px · 19.8 s

![Brush Artist · Refs · Drag #e8b4a8](Brush-Artist-Refs-Drag-e8b4a8.png)

A light paint: laid on a grey sheet (on white it cannot be seen); **dark** = how far it is from the grey either way.

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 2 % → 0 % | 5.0 px | 0.00 | 0.00 | 152 |
| heavy line | 3 % → 0 % | 8.7 px | 0.00 | 0.00 | 143 |
| pressure swell | 2 % → 0 % | 9.1 px | 0.00 | 0.00 | 93 |
| fast wave | 3 % → 0 % | 3.4 px | 0.00 | 0.00 | 275 |
| slow wave | 9 % → 0 % | 10.9 px | 0.00 | 0.00 | 593 |
| spiral | 10 % → 0 % | 6.9 px | 0.00 | 0.00 | 502 |
| loop | 6 % → 0 % | 7.9 px | 0.34 | 0.01 | 362 |
| tilted | 2 % → 2 % | 6.3 px | 0.34 | 0.89 | 147 |
| over the wet one | 5 % → 0 % | 8.2 px | 0.34 | 0.02 | 149 |
| long, no reload | 12 % → 0 % | 5.4 px | 0.34 | 0.01 | 679 | quarters: 0.01 → 0.01 → 0.01 → 0.01

Numbers say: light vs heavy: width 5.0 → 8.7 px, dark 0.00 → 0.00; the long stroke does not run out of paint.

## Brush Artist · Refs · Drag #e8e4e0
Gouache · 40 px · 21.3 s

![Brush Artist · Refs · Drag #e8e4e0](Brush-Artist-Refs-Drag-e8e4e0.png)

A light paint: laid on a grey sheet (on white it cannot be seen); **dark** = how far it is from the grey either way.

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 2 % → 0 % | 5.0 px | 0.00 | 0.00 | 118 |
| heavy line | 3 % → 0 % | 8.7 px | 0.00 | 0.00 | 108 |
| pressure swell | 2 % → 0 % | 9.1 px | 0.00 | 0.00 | 76 |
| fast wave | 3 % → 0 % | 3.4 px | 0.00 | 0.00 | 267 |
| slow wave | 9 % → 0 % | 10.9 px | 0.00 | 0.00 | 512 |
| spiral | 10 % → 0 % | 6.9 px | 0.00 | 0.00 | 493 |
| loop | 6 % → 0 % | 7.9 px | 0.42 | 0.01 | 256 |
| tilted | 2 % → 2 % | 6.3 px | 0.42 | 0.89 | 204 |
| over the wet one | 5 % → 0 % | 8.2 px | 0.42 | 0.02 | 190 |
| long, no reload | 12 % → 0 % | 5.4 px | 0.43 | 0.01 | 889 | quarters: 0.01 → 0.01 → 0.01 → 0.01

Numbers say: light vs heavy: width 5.0 → 8.7 px, dark 0.00 → 0.00; the long stroke does not run out of paint.

## Brush Artist · Refs · Finger
Pastel · 36 px · 21.5 s · over bands of wet oil paint and oil pastel in turn (it works on paint already there: look at what it does to the bands; covered counts the bands too)

![Brush Artist · Refs · Finger](Brush-Artist-Refs-Finger.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 25 % → 25 % | 73.9 px | 0.80 | 1.00 | 44 |
| heavy line | 27 % → 27 % | 78.5 px | 0.80 | 1.00 | 50 |
| pressure swell | 26 % → 26 % | 97.7 px | 0.80 | 1.00 | 39 |
| fast wave | 32 % → 32 % | 37.1 px | 0.78 | 1.00 | 131 |
| slow wave | 31 % → 31 % | 36.2 px | 0.78 | 1.00 | 304 |
| spiral | 38 % → 38 % | 25.0 px | 0.76 | 1.00 | 223 |
| loop | 30 % → 30 % | 39.4 px | 0.78 | 1.00 | 184 |
| tilted | 26 % → 26 % | 73.4 px | 0.79 | 1.00 | 130 |
| over the wet one | 29 % → 29 % | 6.7 px | 0.79 | 1.00 | 88 |
| long, no reload | 40 % → 40 % | 18.0 px | 0.75 | 1.00 | 332 | quarters: 0.25 → 0.36 → 0.33 → 0.38

Numbers say: light vs heavy: width 73.9 → 78.5 px, dark 0.80 → 0.80; pressure barely changes the width; the long stroke does not run out of paint.

## Brush Artist · Ink — wash
Watercolor · 38 px · 34.9 s

![Brush Artist · Ink — wash](Brush-Artist-Ink-wash.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 11 % → 11 % | 31.6 px | 0.38 | 1.04 | 82 |
| heavy line | 19 % → 19 % | 54.3 px | 0.32 | 1.03 | 96 |
| pressure swell | 12 % → 12 % | 45.1 px | 0.36 | 1.04 | 58 |
| fast wave | 39 % → 41 % | 45.5 px | 0.30 | 1.04 | 192 |
| slow wave | 37 % → 38 % | 42.9 px | 0.37 | 1.03 | 326 |
| spiral | 58 % → 60 % | 38.5 px | 0.30 | 1.04 | 348 |
| loop | 32 % → 33 % | 41.9 px | 0.35 | 1.02 | 165 |
| tilted | 13 % → 14 % | 36.9 px | 0.38 | 1.04 | 107 |
| over the wet one | 29 % → 30 % | 42.7 px | 0.38 | 1.04 | 85 |
| long, no reload | 67 % → 71 % | 29.9 px | 0.29 | 1.07 | 484 | quarters: 0.33 → 0.26 → 0.19 → 0.12

Numbers say: light vs heavy: width 31.6 → 54.3 px, dark 0.38 → 0.32.

## Brush Artist · Ink — brush line
Ink · 16 px · 32.2 s

![Brush Artist · Ink — brush line](Brush-Artist-Ink-brush-line.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 3 % → 5 % | 7.7 px | 0.78 | 1.81 | 40 |
| heavy line | 13 % → 13 % | 39.0 px | 0.88 | 0.99 | 115 |
| pressure swell | 8 % → 8 % | 28.4 px | 0.87 | 1.05 | 60 |
| fast wave | 24 % → 23 % | 28.0 px | 0.87 | 0.96 | 169 |
| slow wave | 20 % → 19 % | 22.6 px | 0.87 | 0.97 | 202 |
| spiral | 30 % → 27 % | 20.1 px | 0.86 | 0.89 | 276 |
| loop | 18 % → 18 % | 23.6 px | 0.88 | 1.00 | 137 |
| tilted | 7 % → 7 % | 20.5 px | 0.88 | 1.01 | 70 |
| over the wet one | 17 % → 17 % | 26.8 px | 0.88 | 1.00 | 62 |
| long, no reload | 42 % → 30 % | 18.9 px | 0.85 | 0.71 | 496 | quarters: 0.49 → 0.40 → 0.30 → 0.20

Numbers say: light vs heavy: width 7.7 → 39.0 px, dark 0.78 → 0.88; wet paint spreads well beyond the stroke.

## Brush Artist · Ink — dry brush
Gouache · 30 px · 24.6 s

![Brush Artist · Ink — dry brush](Brush-Artist-Ink-dry-brush.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 3 % → 0 % | 9.2 px | 0.77 | 0.00 | 83 |
| heavy line | 5 % → 0 % | 14.0 px | 0.00 | 0.00 | 152 |
| pressure swell | 4 % → 0 % | 13.5 px | 0.77 | 0.01 | 110 |
| fast wave | 7 % → 0 % | 8.0 px | 0.77 | 0.00 | 257 |
| slow wave | 11 % → 0 % | 12.2 px | 0.77 | 0.01 | 403 |
| spiral | 14 % → 0 % | 9.2 px | 0.77 | 0.01 | 403 |
| loop | 9 % → 0 % | 11.1 px | 0.77 | 0.02 | 222 |
| tilted | 4 % → 4 % | 11.2 px | 0.77 | 0.94 | 107 |
| over the wet one | 8 % → 1 % | 12.2 px | 0.77 | 0.10 | 117 |
| long, no reload | 16 % → 1 % | 7.2 px | 0.77 | 0.03 | 632 | quarters: 0.21 → 0.15 → 0.12 → 0.11

Numbers say: light vs heavy: width 9.2 → 14.0 px, dark 0.77 → 0.00.

## Brush Artist · Watercolour — blue
Watercolor · 40 px · 36.6 s

![Brush Artist · Watercolour — blue](Brush-Artist-Watercolour-blue.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 6 % → 10 % | 16.7 px | 0.25 | 1.71 | 92 |
| heavy line | 11 % → 12 % | 31.5 px | 0.25 | 1.13 | 110 |
| pressure swell | 7 % → 9 % | 25.4 px | 0.26 | 1.32 | 80 |
| fast wave | 24 % → 25 % | 27.8 px | 0.24 | 1.06 | 150 |
| slow wave | 22 % → 27 % | 25.9 px | 0.26 | 1.22 | 273 |
| spiral | 38 % → 41 % | 25.2 px | 0.22 | 1.08 | 411 |
| loop | 20 % → 22 % | 25.3 px | 0.26 | 1.13 | 263 |
| tilted | 12 % → 12 % | 33.3 px | 0.26 | 1.00 | 106 |
| over the wet one | 21 % → 24 % | 24.7 px | 0.26 | 1.15 | 67 |
| long, no reload | 52 % → 54 % | 23.1 px | 0.22 | 1.04 | 428 | quarters: 0.18 → 0.14 → 0.11 → 0.08

Numbers say: light vs heavy: width 16.7 → 31.5 px, dark 0.25 → 0.25; wet paint spreads well beyond the stroke.

## Brush Artist · Watercolour — violet
Watercolor · 40 px · 35.5 s

![Brush Artist · Watercolour — violet](Brush-Artist-Watercolour-violet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 6 % → 10 % | 16.7 px | 0.40 | 1.71 | 59 |
| heavy line | 11 % → 12 % | 31.5 px | 0.40 | 1.13 | 71 |
| pressure swell | 7 % → 9 % | 25.4 px | 0.41 | 1.32 | 41 |
| fast wave | 24 % → 25 % | 27.8 px | 0.38 | 1.06 | 274 |
| slow wave | 22 % → 27 % | 25.9 px | 0.41 | 1.22 | 865 |
| spiral | 38 % → 41 % | 25.2 px | 0.36 | 1.08 | 536 |
| loop | 20 % → 22 % | 25.3 px | 0.40 | 1.13 | 137 |
| tilted | 12 % → 12 % | 33.3 px | 0.40 | 1.00 | 117 |
| over the wet one | 21 % → 24 % | 24.7 px | 0.40 | 1.15 | 85 |
| long, no reload | 52 % → 54 % | 23.1 px | 0.34 | 1.04 | 559 | quarters: 0.28 → 0.22 → 0.18 → 0.14

Numbers say: light vs heavy: width 16.7 → 31.5 px, dark 0.40 → 0.40; wet paint spreads well beyond the stroke.

## Brush Artist · Watercolour — teal
Watercolor · 40 px · 35.8 s

![Brush Artist · Watercolour — teal](Brush-Artist-Watercolour-teal.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 6 % → 10 % | 16.7 px | 0.16 | 1.71 | 40 |
| heavy line | 11 % → 12 % | 31.5 px | 0.16 | 1.13 | 80 |
| pressure swell | 7 % → 9 % | 25.4 px | 0.17 | 1.32 | 43 |
| fast wave | 24 % → 25 % | 27.8 px | 0.15 | 1.06 | 157 |
| slow wave | 22 % → 27 % | 25.9 px | 0.17 | 1.22 | 527 |
| spiral | 38 % → 41 % | 25.2 px | 0.15 | 1.08 | 275 |
| loop | 20 % → 22 % | 25.3 px | 0.16 | 1.13 | 136 |
| tilted | 12 % → 12 % | 33.3 px | 0.16 | 1.00 | 122 |
| over the wet one | 21 % → 24 % | 24.7 px | 0.16 | 1.15 | 58 |
| long, no reload | 52 % → 54 % | 23.1 px | 0.14 | 1.04 | 389 | quarters: 0.11 → 0.09 → 0.07 → 0.06

Numbers say: light vs heavy: width 16.7 → 31.5 px, dark 0.16 → 0.16; wet paint spreads well beyond the stroke.

## Brush Artist · Gouache
Gouache · 30 px · 46.6 s

![Brush Artist · Gouache](Brush-Artist-Gouache.png)

A light paint: laid on a grey sheet (on white it cannot be seen); **dark** = how far it is from the grey either way.

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 8 % → 8 % | 24.4 px | 0.27 | 0.97 | 85 |
| heavy line | 15 % → 12 % | 42.9 px | 0.27 | 0.78 | 102 |
| pressure swell | 11 % → 9 % | 41.1 px | 0.27 | 0.85 | 112 |
| fast wave | 30 % → 14 % | 35.0 px | 0.26 | 0.45 | 322 |
| slow wave | 29 % → 14 % | 34.0 px | 0.26 | 0.47 | 442 |
| spiral | 40 % → 14 % | 26.7 px | 0.26 | 0.35 | 478 |
| loop | 24 % → 15 % | 30.6 px | 0.26 | 0.62 | 274 |
| tilted | 10 % → 10 % | 27.5 px | 0.27 | 1.01 | 141 |
| over the wet one | 22 % → 19 % | 32.8 px | 0.27 | 0.89 | 106 |
| long, no reload | 43 % → 15 % | 19.1 px | 0.26 | 0.35 | 650 | quarters: 0.01 → 0.01 → 0.01 → 0.01

Numbers say: light vs heavy: width 24.4 → 42.9 px, dark 0.27 → 0.27; the long stroke does not run out of paint.

## Brush Artist · Oil — bristle
Oil · 30 px · 27.4 s

![Brush Artist · Oil — bristle](Brush-Artist-Oil-bristle.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 9 % → 9 % | 27.1 px | 0.54 | 1.00 | 196 |
| heavy line | 10 % → 10 % | 29.4 px | 0.54 | 1.00 | 218 |
| pressure swell | 8 % → 8 % | 29.3 px | 0.55 | 1.00 | 155 |
| fast wave | 24 % → 24 % | 27.6 px | 0.55 | 1.00 | 386 |
| slow wave | 25 % → 25 % | 28.6 px | 0.55 | 1.00 | 668 |
| spiral | 39 % → 39 % | 25.8 px | 0.54 | 1.00 | 787 |
| loop | 20 % → 20 % | 26.3 px | 0.54 | 1.00 | 430 |
| tilted | 11 % → 11 % | 30.6 px | 0.53 | 1.00 | 243 |
| over the wet one | 20 % → 20 % | 26.4 px | 0.53 | 1.00 | 174 |
| long, no reload | 50 % → 50 % | 22.5 px | 0.54 | 1.00 | 1178 | quarters: 0.32 → 0.30 → 0.29 → 0.28

Numbers say: light vs heavy: width 27.1 → 29.4 px, dark 0.54 → 0.54; pressure barely changes the width; the long stroke does not run out of paint.

## Brush Artist · Charcoal — stick
Charcoal · 28 px · 15.4 s

![Brush Artist · Charcoal — stick](Brush-Artist-Charcoal-stick.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 3 % → 3 % | 8.4 px | 0.85 | 1.00 | 36 |
| heavy line | 6 % → 6 % | 17.8 px | 0.85 | 1.00 | 35 |
| pressure swell | 4 % → 4 % | 13.9 px | 0.85 | 1.00 | 17 |
| fast wave | 12 % → 12 % | 14.0 px | 0.85 | 1.00 | 62 |
| slow wave | 11 % → 11 % | 12.5 px | 0.85 | 1.00 | 128 |
| spiral | 19 % → 19 % | 12.7 px | 0.85 | 1.00 | 108 |
| loop | 10 % → 10 % | 12.8 px | 0.85 | 1.00 | 56 |
| tilted | 4 % → 4 % | 10.9 px | 0.85 | 1.00 | 49 |
| over the wet one | 9 % → 9 % | 13.5 px | 0.85 | 1.00 | 26 |
| long, no reload | 27 % → 27 % | 12.2 px | 0.85 | 1.00 | 167 | quarters: 0.26 → 0.25 → 0.26 → 0.27

Numbers say: light vs heavy: width 8.4 → 17.8 px, dark 0.85 → 0.85; the long stroke does not run out of paint.

## Brush Artist · Charcoal — stick B
Charcoal · 36 px · 14.4 s

![Brush Artist · Charcoal — stick B](Brush-Artist-Charcoal-stick-B.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 4 % → 4 % | 10.5 px | 0.85 | 1.00 | 57 |
| heavy line | 7 % → 7 % | 21.1 px | 0.85 | 1.00 | 60 |
| pressure swell | 4 % → 4 % | 16.5 px | 0.85 | 1.00 | 29 |
| fast wave | 15 % → 15 % | 16.8 px | 0.85 | 1.00 | 86 |
| slow wave | 13 % → 13 % | 14.7 px | 0.85 | 1.00 | 158 |
| spiral | 23 % → 23 % | 15.0 px | 0.85 | 1.00 | 152 |
| loop | 11 % → 11 % | 14.8 px | 0.85 | 1.00 | 125 |
| tilted | 4 % → 4 % | 12.3 px | 0.85 | 1.00 | 84 |
| over the wet one | 10 % → 10 % | 15.9 px | 0.85 | 1.00 | 55 |
| long, no reload | 31 % → 31 % | 13.9 px | 0.85 | 1.00 | 334 | quarters: 0.30 → 0.28 → 0.29 → 0.30

Numbers say: light vs heavy: width 10.5 → 21.1 px, dark 0.85 → 0.85; the long stroke does not run out of paint.

## Brush Artist · Charcoal — stick C
Charcoal · 22 px · 15.8 s

![Brush Artist · Charcoal — stick C](Brush-Artist-Charcoal-stick-C.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 2 % → 2 % | 6.9 px | 0.85 | 1.00 | 43 |
| heavy line | 5 % → 5 % | 15.3 px | 0.85 | 1.00 | 31 |
| pressure swell | 3 % → 3 % | 12.2 px | 0.85 | 1.00 | 32 |
| fast wave | 10 % → 10 % | 12.1 px | 0.85 | 1.00 | 47 |
| slow wave | 9 % → 9 % | 10.8 px | 0.85 | 1.00 | 82 |
| spiral | 17 % → 17 % | 11.0 px | 0.85 | 1.00 | 94 |
| loop | 9 % → 9 % | 11.4 px | 0.85 | 1.00 | 51 |
| tilted | 4 % → 4 % | 9.9 px | 0.85 | 1.00 | 35 |
| over the wet one | 8 % → 8 % | 11.7 px | 0.85 | 1.00 | 46 |
| long, no reload | 24 % → 24 % | 11.0 px | 0.85 | 1.00 | 137 | quarters: 0.24 → 0.22 → 0.23 → 0.24

Numbers say: light vs heavy: width 6.9 → 15.3 px, dark 0.85 → 0.85; the long stroke does not run out of paint.

## Dev · Knife #47
Heavy acrylic · 90 px · 38.1 s

![Dev · Knife #47](Dev-Knife-47.png)

A light paint: laid on a grey sheet (on white it cannot be seen); **dark** = how far it is from the grey either way.

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 34 % → 34 % | 98.8 px | 0.29 | 0.99 | 122 |
| heavy line | 34 % → 34 % | 98.8 px | 0.29 | 0.99 | 203 |
| pressure swell | 26 % → 27 % | 98.8 px | 0.29 | 1.04 | 126 |
| fast wave | 68 % → 58 % | 78.9 px | 0.26 | 0.85 | 376 |
| slow wave | 69 % → 61 % | 80.0 px | 0.26 | 0.88 | 527 |
| spiral | 67 % → 43 % | 44.4 px | 0.27 | 0.63 | 552 |
| loop | 60 % → 54 % | 77.8 px | 0.27 | 0.90 | 270 |
| tilted | 23 % → 23 % | 63.6 px | 0.28 | 1.00 | 84 |
| over the wet one | 53 % → 53 % | 83.8 px | 0.28 | 1.00 | 114 |
| long, no reload | 95 % → 62 % | 42.7 px | 0.25 | 0.65 | 497 | quarters: 0.00 → 0.00 → 0.00 → 0.00

Numbers say: light vs heavy: width 98.8 → 98.8 px, dark 0.29 → 0.29; pressure barely changes the width; the long stroke does not run out of paint.

## Brush Artist · Refs · #01 Henry Ward peach cloud — own sheet
own sheet 600 × 600 · Gouache · 44 px · 20.2 s

![Brush Artist · Refs · #01 Henry Ward peach cloud — own sheet](Brush-Artist-Refs-01-Henry-Ward-peach-cloud-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 12 % → 32 % | 34.1 px | 0.58 | 2.71 | 442 |
| stroke 2 | 20 % → 49 % | 66.6 px | 0.58 | 2.44 | 201 |
| stroke 3 | 23 % → 47 % | 67.7 px | 0.58 | 2.01 | 267 |
| stroke 4 | 26 % → 53 % | 83.6 px | 0.58 | 2.08 | 193 |
| stroke 5 | 25 % → 47 % | 71.5 px | 0.58 | 1.92 | 228 |
| stroke 6 | 25 % → 36 % | 76.6 px | 0.58 | 1.43 | 218 |
| stroke 7 | 11 % → 47 % | 28.6 px | 0.58 | 4.11 | 197 |
| stroke 8 | 14 % → 44 % | 34.8 px | 0.58 | 3.18 | 241 |
| stroke 9 | 17 % → 45 % | 44.6 px | 0.58 | 2.60 | 227 |
| stroke 10 | 19 % → 46 % | 51.1 px | 0.58 | 2.40 | 226 |
| stroke 11 | 22 % → 48 % | 60.9 px | 0.58 | 2.24 | 222 |
| stroke 12 | 25 % → 51 % | 73.7 px | 0.58 | 2.07 | 189 |
| stroke 13 | 32 % → 53 % | 91.6 px | 0.58 | 1.69 | 246 |
| stroke 14 | 34 % → 55 % | 98.2 px | 0.58 | 1.61 | 234 |
| stroke 15 | 45 % → 60 % | 133.9 px | 0.58 | 1.32 | 250 |
| stroke 16 | 47 % → 60 % | 142.8 px | 0.58 | 1.28 | 192 |
| stroke 17 | 49 % → 62 % | 137.2 px | 0.58 | 1.26 | 263 |
| stroke 18 | 50 % → 61 % | 145.4 px | 0.58 | 1.21 | 260 |
| stroke 19 | 52 % → 60 % | 145.8 px | 0.58 | 1.15 | 315 |
| stroke 20 | 52 % → 57 % | 149.7 px | 0.58 | 1.09 | 333 |
| stroke 21 | 52 % → 54 % | 150.5 px | 0.58 | 1.03 | 283 |
| stroke 22 | 54 % → 54 % | 156.1 px | 0.58 | 1.02 | 262 |
| stroke 23 | 53 % → 52 % | 151.0 px | 0.58 | 0.98 | 213 |
| stroke 24 | 57 % → 55 % | 169.4 px | 0.58 | 0.97 | 188 |

Numbers say: wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #02 Henry Ward cream strokes — own sheet
own sheet 600 × 600 · Gouache · 46 px · 13.2 s

![Brush Artist · Refs · #02 Henry Ward cream strokes — own sheet](Brush-Artist-Refs-02-Henry-Ward-cream-strokes-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 15 % → 25 % | 30.9 px | 0.70 | 1.67 | 434 |
| stroke 2 | 23 % → 29 % | 60.0 px | 0.70 | 1.29 | 355 |
| stroke 3 | 22 % → 36 % | 57.4 px | 0.70 | 1.58 | 351 |
| stroke 4 | 24 % → 33 % | 59.5 px | 0.70 | 1.38 | 360 |
| stroke 5 | 29 % → 36 % | 71.6 px | 0.70 | 1.24 | 304 |
| stroke 6 | 23 % → 31 % | 55.5 px | 0.70 | 1.35 | 360 |
| stroke 7 | 24 % → 21 % | 61.4 px | 0.70 | 0.88 | 278 |

Numbers say: wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #03 Henry Ward navy contours — own sheet
own sheet 600 × 600 · Heavy acrylic · 22 px · 3.6 s

![Brush Artist · Refs · #03 Henry Ward navy contours — own sheet](Brush-Artist-Refs-03-Henry-Ward-navy-contours-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 12 % → 18 % | 23.4 px | 0.69 | 1.57 | 184 |
| stroke 2 | 20 % → 23 % | 28.6 px | 0.69 | 1.15 | 172 |
| stroke 3 | 23 % → 23 % | 33.7 px | 0.69 | 1.01 | 189 |
| stroke 4 | 23 % → 21 % | 51.1 px | 0.69 | 0.92 | 210 |

Numbers say: wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #04 Henry Ward grey cloud — own sheet
own sheet 600 × 600 · Gouache · 50 px · 21.5 s

![Brush Artist · Refs · #04 Henry Ward grey cloud — own sheet](Brush-Artist-Refs-04-Henry-Ward-grey-cloud-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 11 % → 38 % | 31.6 px | 0.39 | 3.52 | 296 |
| stroke 2 | 14 % → 40 % | 40.5 px | 0.39 | 2.81 | 335 |
| stroke 3 | 21 % → 45 % | 59.1 px | 0.39 | 2.13 | 319 |
| stroke 4 | 24 % → 48 % | 69.5 px | 0.39 | 1.99 | 354 |
| stroke 5 | 29 % → 53 % | 88.8 px | 0.39 | 1.81 | 346 |
| stroke 6 | 32 % → 56 % | 104.9 px | 0.39 | 1.76 | 304 |
| stroke 7 | 37 % → 62 % | 109.7 px | 0.39 | 1.66 | 368 |
| stroke 8 | 37 % → 62 % | 110.4 px | 0.39 | 1.67 | 505 |
| stroke 9 | 36 % → 62 % | 107.6 px | 0.39 | 1.73 | 447 |
| stroke 10 | 38 % → 62 % | 120.7 px | 0.39 | 1.66 | 444 |
| stroke 11 | 38 % → 62 % | 107.0 px | 0.39 | 1.65 | 405 |
| stroke 12 | 38 % → 62 % | 115.1 px | 0.39 | 1.63 | 325 |
| stroke 13 | 38 % → 63 % | 107.6 px | 0.39 | 1.67 | 314 |
| stroke 14 | 38 % → 63 % | 114.2 px | 0.39 | 1.64 | 342 |
| stroke 15 | 38 % → 59 % | 108.6 px | 0.39 | 1.55 | 344 |
| stroke 16 | 39 % → 56 % | 118.1 px | 0.39 | 1.45 | 375 |
| stroke 17 | 37 % → 49 % | 106.3 px | 0.39 | 1.31 | 315 |
| stroke 18 | 37 % → 45 % | 121.8 px | 0.39 | 1.22 | 351 |
| stroke 19 | 37 % → 38 % | 111.3 px | 0.39 | 1.02 | 300 |
| stroke 20 | 39 % → 37 % | 122.3 px | 0.39 | 0.96 | 305 |

Numbers say: wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #05 Henry Ward green in rust loops — own sheet
own sheet 600 × 600 · Heavy acrylic · 20 px · 4.2 s

![Brush Artist · Refs · #05 Henry Ward green in rust loops — own sheet](Brush-Artist-Refs-05-Henry-Ward-green-in-rust-loops-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 12 % → 19 % | 21.2 px | 0.02 | 1.61 | 190 |
| stroke 2 | 12 % → 11 % | 23.7 px | 0.02 | 0.93 | 212 |
| stroke 3 | 23 % → 22 % | 41.7 px | 0.02 | 0.93 | 194 |

Numbers say: wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #06 Henry Ward scrubbed grey — own sheet
own sheet 600 × 600 · Gouache · 50 px · 22.4 s

![Brush Artist · Refs · #06 Henry Ward scrubbed grey — own sheet](Brush-Artist-Refs-06-Henry-Ward-scrubbed-grey-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 13 % → 42 % | 31.5 px | 0.39 | 3.25 | 325 |
| stroke 2 | 17 % → 44 % | 44.7 px | 0.39 | 2.60 | 324 |
| stroke 3 | 22 % → 47 % | 68.1 px | 0.39 | 2.11 | 301 |
| stroke 4 | 23 % → 47 % | 74.0 px | 0.39 | 2.02 | 325 |
| stroke 5 | 33 % → 60 % | 99.8 px | 0.39 | 1.79 | 361 |
| stroke 6 | 36 % → 60 % | 109.9 px | 0.39 | 1.66 | 320 |
| stroke 7 | 38 % → 62 % | 108.5 px | 0.39 | 1.63 | 303 |
| stroke 8 | 38 % → 62 % | 120.3 px | 0.39 | 1.62 | 335 |
| stroke 9 | 36 % → 61 % | 111.2 px | 0.39 | 1.70 | 301 |
| stroke 10 | 36 % → 61 % | 118.0 px | 0.39 | 1.70 | 325 |
| stroke 11 | 38 % → 62 % | 111.8 px | 0.39 | 1.62 | 313 |
| stroke 12 | 39 % → 62 % | 118.6 px | 0.39 | 1.60 | 280 |
| stroke 13 | 37 % → 62 % | 103.9 px | 0.39 | 1.70 | 312 |
| stroke 14 | 36 % → 62 % | 106.2 px | 0.39 | 1.72 | 308 |
| stroke 15 | 37 % → 62 % | 105.0 px | 0.39 | 1.71 | 314 |
| stroke 16 | 37 % → 62 % | 117.9 px | 0.39 | 1.68 | 280 |
| stroke 17 | 36 % → 55 % | 107.4 px | 0.39 | 1.53 | 281 |
| stroke 18 | 38 % → 53 % | 114.0 px | 0.39 | 1.41 | 306 |
| stroke 19 | 37 % → 48 % | 109.8 px | 0.39 | 1.31 | 307 |
| stroke 20 | 37 % → 47 % | 116.2 px | 0.39 | 1.25 | 369 |
| stroke 21 | 37 % → 40 % | 107.6 px | 0.39 | 1.07 | 425 |
| stroke 22 | 37 % → 36 % | 123.2 px | 0.39 | 0.96 | 358 |

Numbers say: wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #07 Henry Ward blue L + black zigzag — own sheet
own sheet 600 × 600 · Heavy acrylic · 34 px · 3.1 s

![Brush Artist · Refs · #07 Henry Ward blue L + black zigzag — own sheet](Brush-Artist-Refs-07-Henry-Ward-blue-L-black-zigzag-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 16 % → 17 % | 36.5 px | 0.59 | 1.11 | 183 |
| stroke 2 | 18 % → 17 % | 44.0 px | 0.59 | 0.93 | 132 |

## Brush Artist · Refs · #08 Henry Ward olive bands — own sheet
own sheet 600 × 600 · Gouache · 34 px · 7.9 s

![Brush Artist · Refs · #08 Henry Ward olive bands — own sheet](Brush-Artist-Refs-08-Henry-Ward-olive-bands-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 9 % → 7 % | 17.9 px | 0.59 | 0.82 | 307 |
| stroke 2 | 15 % → 9 % | 32.8 px | 0.59 | 0.63 | 302 |
| stroke 3 | 13 % → 13 % | 26.4 px | 0.59 | 1.02 | 292 |
| stroke 4 | 15 % → 11 % | 31.5 px | 0.59 | 0.78 | 241 |
| stroke 5 | 20 % → 14 % | 40.1 px | 0.59 | 0.71 | 270 |
| stroke 6 | 13 % → 7 % | 24.2 px | 0.59 | 0.52 | 209 |

## Brush Artist · Refs · #09 Henry Ward white loops — own sheet
own sheet 600 × 600 · Gouache · 46 px · 12.2 s

![Brush Artist · Refs · #09 Henry Ward white loops — own sheet](Brush-Artist-Refs-09-Henry-Ward-white-loops-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 19 % → 3 % | 10.2 px | 0.08 | 0.15 | 1430 |
| stroke 2 | 21 % → 2 % | 21.2 px | 0.08 | 0.12 | 1526 |
| stroke 3 | 28 % → 3 % | 25.7 px | 0.08 | 0.10 | 1272 |
| stroke 4 | 2 % → 0 % | 5.7 px | 0.07 | 0.18 | 199 |
| stroke 5 | 4 % → 1 % | 10.8 px | 0.08 | 0.32 | 231 |
| stroke 6 | 5 % → 3 % | 14.9 px | 0.08 | 0.53 | 200 |
| stroke 7 | 12 % → 3 % | 30.4 px | 0.08 | 0.25 | 225 |
| stroke 8 | 2 % → 0 % | 3.0 px | 0.05 | 0.06 | 252 |

## Brush Artist · Refs · #10 Henry Ward maroon loops — own sheet
own sheet 600 × 600 · Heavy acrylic · 30 px · 4.2 s

![Brush Artist · Refs · #10 Henry Ward maroon loops — own sheet](Brush-Artist-Refs-10-Henry-Ward-maroon-loops-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 12 % → 28 % | 29.0 px | 0.72 | 2.41 | 278 |
| stroke 2 | 22 % → 41 % | 49.1 px | 0.72 | 1.87 | 157 |
| stroke 3 | 29 % → 37 % | 59.1 px | 0.72 | 1.27 | 197 |
| stroke 4 | 42 % → 41 % | 95.0 px | 0.72 | 0.96 | 133 |
| stroke 5 | 35 % → 32 % | 87.1 px | 0.72 | 0.93 | 180 |

Numbers say: wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #11 Henry Ward purple spun balls — own sheet
own sheet 600 × 600 · Heavy acrylic · 36 px · 4.5 s

![Brush Artist · Refs · #11 Henry Ward purple spun balls — own sheet](Brush-Artist-Refs-11-Henry-Ward-purple-spun-balls-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 24 % → 35 % | 26.9 px | 0.68 | 1.44 | 292 |
| stroke 2 | 35 % → 47 % | 38.6 px | 0.68 | 1.34 | 422 |
| stroke 3 | 36 % → 35 % | 39.8 px | 0.68 | 0.97 | 402 |

## Brush Artist · Refs · #12 Henry Ward black-olive cage — own sheet
own sheet 600 × 600 · Gouache · 28 px · 7.6 s

![Brush Artist · Refs · #12 Henry Ward black-olive cage — own sheet](Brush-Artist-Refs-12-Henry-Ward-black-olive-cage-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 7 % → 12 % | 13.4 px | 0.60 | 1.68 | 343 |
| stroke 2 | 7 % → 12 % | 16.3 px | 0.60 | 1.80 | 312 |
| stroke 3 | 15 % → 16 % | 24.2 px | 0.60 | 1.03 | 390 |
| stroke 4 | 16 % → 15 % | 32.2 px | 0.60 | 0.92 | 233 |
| stroke 5 | 16 % → 11 % | 29.0 px | 0.60 | 0.68 | 226 |
| stroke 6 | 25 % → 16 % | 48.3 px | 0.60 | 0.65 | 296 |

Numbers say: wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #13 Henry Ward blue streaky form — own sheet
own sheet 600 × 600 · Gouache · 50 px · 18.5 s

![Brush Artist · Refs · #13 Henry Ward blue streaky form — own sheet](Brush-Artist-Refs-13-Henry-Ward-blue-streaky-form-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 11 % → 7 % | 32.9 px | 0.03 | 0.64 | 265 |
| stroke 2 | 15 % → 6 % | 46.8 px | 0.03 | 0.42 | 287 |
| stroke 3 | 24 % → 7 % | 69.0 px | 0.03 | 0.29 | 277 |
| stroke 4 | 24 % → 6 % | 79.3 px | 0.03 | 0.26 | 344 |
| stroke 5 | 36 % → 7 % | 103.1 px | 0.03 | 0.20 | 281 |
| stroke 6 | 36 % → 8 % | 104.0 px | 0.03 | 0.22 | 287 |
| stroke 7 | 37 % → 9 % | 109.8 px | 0.03 | 0.23 | 285 |
| stroke 8 | 38 % → 7 % | 114.0 px | 0.03 | 0.19 | 297 |
| stroke 9 | 36 % → 6 % | 111.9 px | 0.03 | 0.18 | 280 |
| stroke 10 | 37 % → 6 % | 120.7 px | 0.03 | 0.17 | 259 |
| stroke 11 | 35 % → 4 % | 108.3 px | 0.03 | 0.11 | 305 |
| stroke 12 | 36 % → 5 % | 107.0 px | 0.03 | 0.14 | 299 |
| stroke 13 | 36 % → 6 % | 111.1 px | 0.03 | 0.16 | 255 |
| stroke 14 | 35 % → 6 % | 103.9 px | 0.03 | 0.16 | 282 |
| stroke 15 | 35 % → 6 % | 101.6 px | 0.03 | 0.16 | 280 |
| stroke 16 | 37 % → 6 % | 111.8 px | 0.03 | 0.15 | 279 |
| stroke 17 | 44 % → 3 % | 108.9 px | 0.03 | 0.07 | 282 |
| stroke 18 | 46 % → 3 % | 112.6 px | 0.03 | 0.07 | 289 |
| stroke 19 | 52 % → 4 % | 105.5 px | 0.03 | 0.07 | 280 |
| stroke 20 | 58 % → 4 % | 110.7 px | 0.03 | 0.07 | 365 |
| stroke 21 | 1 % → 0 % | 2.9 px | 0.04 | 0.02 | 239 |
| stroke 22 | 9 % → 6 % | 27.5 px | 0.03 | 0.67 | 304 |
| stroke 23 | 18 % → 7 % | 57.2 px | 0.03 | 0.38 | 342 |
| stroke 24 | 11 % → 4 % | 29.3 px | 0.03 | 0.36 | 328 |
| stroke 25 | 13 % → 4 % | 34.0 px | 0.03 | 0.31 | 286 |

## Brush Artist · Refs · #14 Henry Ward olive totem — own sheet
own sheet 600 × 600 · Heavy acrylic · 48 px · 9.4 s

![Brush Artist · Refs · #14 Henry Ward olive totem — own sheet](Brush-Artist-Refs-14-Henry-Ward-olive-totem-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 19 % → 49 % | 48.9 px | 0.38 | 2.60 | 199 |
| stroke 2 | 22 % → 53 % | 67.8 px | 0.38 | 2.44 | 175 |
| stroke 3 | 31 % → 54 % | 105.7 px | 0.38 | 1.76 | 224 |
| stroke 4 | 32 % → 57 % | 120.2 px | 0.38 | 1.77 | 202 |
| stroke 5 | 41 % → 66 % | 143.0 px | 0.38 | 1.60 | 141 |
| stroke 6 | 41 % → 67 % | 158.1 px | 0.38 | 1.65 | 158 |
| stroke 7 | 39 % → 63 % | 130.7 px | 0.38 | 1.63 | 157 |
| stroke 8 | 39 % → 65 % | 147.7 px | 0.38 | 1.68 | 190 |
| stroke 9 | 39 % → 64 % | 134.6 px | 0.38 | 1.66 | 159 |
| stroke 10 | 39 % → 63 % | 143.8 px | 0.37 | 1.63 | 183 |
| stroke 11 | 41 % → 66 % | 147.3 px | 0.38 | 1.61 | 162 |
| stroke 12 | 39 % → 67 % | 148.5 px | 0.38 | 1.70 | 198 |
| stroke 13 | 40 % → 69 % | 141.8 px | 0.38 | 1.71 | 160 |
| stroke 14 | 38 % → 64 % | 139.1 px | 0.38 | 1.68 | 191 |
| stroke 15 | 41 % → 68 % | 141.2 px | 0.38 | 1.64 | 190 |
| stroke 16 | 40 % → 66 % | 143.5 px | 0.38 | 1.66 | 193 |
| stroke 17 | 39 % → 64 % | 131.8 px | 0.38 | 1.64 | 205 |
| stroke 18 | 42 % → 69 % | 160.9 px | 0.38 | 1.64 | 192 |
| stroke 19 | 41 % → 63 % | 143.3 px | 0.37 | 1.53 | 170 |
| stroke 20 | 42 % → 57 % | 149.6 px | 0.37 | 1.35 | 213 |
| stroke 21 | 48 % → 57 % | 142.8 px | 0.37 | 1.19 | 192 |
| stroke 22 | 56 % → 56 % | 152.7 px | 0.37 | 0.99 | 225 |

Numbers say: wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #15 Ultramarine brush script — own sheet
own sheet 600 × 600 · Ink · 4 px · 12.4 s

![Brush Artist · Refs · #15 Ultramarine brush script — own sheet](Brush-Artist-Refs-15-Ultramarine-brush-script-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 40 % → 42 % | 8.9 px | 0.66 | 1.05 | 65 |
| stroke 2 | 40 % → 42 % | 8.9 px | 0.66 | 1.06 | 63 |
| stroke 3 | 40 % → 42 % | 9.5 px | 0.74 | 1.06 | 46 |
| stroke 4 | 42 % → 45 % | 10.1 px | 0.74 | 1.08 | 18 |
| stroke 5 | 44 % → 48 % | 9.7 px | 0.73 | 1.08 | 32 |
| stroke 6 | 42 % → 44 % | 9.5 px | 0.65 | 1.05 | 53 |
| stroke 7 | 43 % → 47 % | 9.2 px | 0.72 | 1.08 | 40 |
| stroke 8 | 38 % → 41 % | 9.3 px | 0.68 | 1.05 | 59 |
| stroke 9 | 40 % → 42 % | 9.2 px | 0.69 | 1.06 | 60 |
| stroke 10 | 36 % → 38 % | 9.9 px | 0.68 | 1.05 | 50 |
| stroke 11 | 42 % → 45 % | 9.6 px | 0.70 | 1.06 | 46 |
| stroke 12 | 39 % → 41 % | 9.4 px | 0.66 | 1.05 | 62 |
| stroke 13 | 45 % → 48 % | 10.2 px | 0.71 | 1.06 | 44 |
| stroke 14 | 38 % → 41 % | 9.9 px | 0.73 | 1.07 | 50 |
| stroke 15 | 37 % → 39 % | 9.1 px | 0.69 | 1.06 | 62 |
| stroke 16 | 42 % → 45 % | 9.4 px | 0.72 | 1.06 | 43 |
| stroke 17 | 41 % → 44 % | 7.1 px | 0.71 | 1.08 | 64 |
| stroke 18 | 43 % → 45 % | 9.2 px | 0.73 | 1.06 | 37 |
| stroke 19 | 39 % → 41 % | 8.9 px | 0.66 | 1.05 | 84 |
| stroke 20 | 41 % → 43 % | 9.4 px | 0.71 | 1.06 | 39 |
| stroke 21 | 40 % → 43 % | 9.9 px | 0.70 | 1.06 | 60 |
| stroke 22 | 42 % → 44 % | 8.5 px | 0.65 | 1.05 | 80 |
| stroke 23 | 40 % → 43 % | 10.1 px | 0.73 | 1.07 | 26 |
| stroke 24 | 38 % → 41 % | 8.8 px | 0.73 | 1.07 | 40 |
| stroke 25 | 41 % → 43 % | 9.8 px | 0.72 | 1.07 | 36 |
| stroke 26 | 46 % → 49 % | 9.3 px | 0.68 | 1.05 | 57 |
| stroke 27 | 43 % → 45 % | 8.8 px | 0.63 | 1.05 | 85 |
| stroke 28 | 44 % → 46 % | 9.1 px | 0.70 | 1.06 | 56 |
| stroke 29 | 36 % → 39 % | 10.6 px | 0.72 | 1.08 | 40 |
| stroke 30 | 39 % → 41 % | 8.7 px | 0.71 | 1.04 | 59 |
| stroke 31 | 43 % → 46 % | 10.3 px | 0.75 | 1.07 | 27 |
| stroke 32 | 42 % → 46 % | 9.5 px | 0.73 | 1.09 | 49 |
| stroke 33 | 35 % → 38 % | 10.9 px | 0.72 | 1.08 | 23 |
| stroke 34 | 40 % → 43 % | 9.8 px | 0.73 | 1.08 | 29 |
| stroke 35 | 36 % → 37 % | 9.4 px | 0.65 | 1.05 | 59 |

## Brush Artist · Refs · #18 Blue oil-stick scribbles — own sheet
own sheet 600 × 600 · Pastel · 10 px · 4.3 s

![Brush Artist · Refs · #18 Blue oil-stick scribbles — own sheet](Brush-Artist-Refs-18-Blue-oil-stick-scribbles-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 15 % → 31 % | 3.8 px | 0.49 | 2.11 | 263 |
| stroke 2 | 13 % → 37 % | 3.6 px | 0.49 | 2.73 | 302 |
| stroke 3 | 16 % → 26 % | 5.8 px | 0.49 | 1.66 | 302 |
| stroke 4 | 15 % → 29 % | 8.0 px | 0.49 | 1.88 | 324 |
| stroke 5 | 29 % → 34 % | 8.4 px | 0.49 | 1.19 | 212 |
| stroke 6 | 25 % → 26 % | 9.4 px | 0.49 | 1.02 | 212 |
| stroke 7 | 26 % → 32 % | 8.3 px | 0.49 | 1.24 | 186 |
| stroke 8 | 30 % → 30 % | 17.0 px | 0.49 | 1.00 | 209 |

Numbers say: wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #20 Orange-red crayon scribble — own sheet
own sheet 600 × 600 · Pastel · 14 px · 5.4 s

![Brush Artist · Refs · #20 Orange-red crayon scribble — own sheet](Brush-Artist-Refs-20-Orange-red-crayon-scribble-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 8 % → 18 % | 5.5 px | 0.59 | 2.46 | 210 |
| stroke 2 | 9 % → 23 % | 6.8 px | 0.59 | 2.48 | 252 |
| stroke 3 | 13 % → 21 % | 8.5 px | 0.59 | 1.64 | 286 |
| stroke 4 | 24 % → 32 % | 8.9 px | 0.59 | 1.34 | 375 |
| stroke 5 | 27 % → 27 % | 7.7 px | 0.59 | 1.00 | 364 |
| stroke 6 | 22 % → 22 % | 16.8 px | 0.59 | 1.00 | 427 |

Numbers say: wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #21 Gritty black contours — own sheet
own sheet 600 × 600 · Gouache · 12 px · 7.1 s

![Brush Artist · Refs · #21 Gritty black contours — own sheet](Brush-Artist-Refs-21-Gritty-black-contours-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 4 % → 5 % | 4.7 px | 0.37 | 1.13 | 370 |
| stroke 2 | 4 % → 3 % | 7.3 px | 0.37 | 0.60 | 492 |
| stroke 3 | 7 % → 4 % | 6.2 px | 0.37 | 0.56 | 286 |
| stroke 4 | 9 % → 4 % | 10.7 px | 0.37 | 0.51 | 272 |
| stroke 5 | 10 % → 4 % | 12.7 px | 0.37 | 0.42 | 175 |

## Brush Artist · Refs · #22 Bold black brush poster — own sheet
own sheet 600 × 600 · Ink · 20 px · 7.9 s

![Brush Artist · Refs · #22 Bold black brush poster — own sheet](Brush-Artist-Refs-22-Bold-black-brush-poster-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 22 % → 27 % | 36.4 px | 0.94 | 1.20 | 262 |
| stroke 2 | 27 % → 37 % | 41.5 px | 0.95 | 1.36 | 35 |
| stroke 3 | 28 % → 28 % | 43.6 px | 0.95 | 1.00 | 53 |
| stroke 4 | 27 % → 39 % | 53.8 px | 0.94 | 1.42 | 79 |
| stroke 5 | 25 % → 25 % | 43.0 px | 0.94 | 1.00 | 126 |

## Brush Artist · Refs · #23 Dry white on orange + black line — own sheet
own sheet 600 × 600 · Gouache · 50 px · 12.7 s

![Brush Artist · Refs · #23 Dry white on orange + black line — own sheet](Brush-Artist-Refs-23-Dry-white-on-orange-black-line-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 5 % → 10 % | 18.7 px | 0.42 | 1.89 | 230 |
| stroke 2 | 7 % → 9 % | 24.3 px | 0.42 | 1.35 | 222 |
| stroke 3 | 10 % → 10 % | 39.0 px | 0.42 | 0.92 | 195 |
| stroke 4 | 12 % → 11 % | 45.8 px | 0.42 | 0.95 | 204 |
| stroke 5 | 17 % → 14 % | 60.0 px | 0.42 | 0.82 | 194 |
| stroke 6 | 17 % → 15 % | 70.6 px | 0.42 | 0.86 | 195 |
| stroke 7 | 14 % → 14 % | 52.6 px | 0.41 | 1.00 | 216 |
| stroke 8 | 14 % → 13 % | 55.2 px | 0.41 | 0.91 | 322 |
| stroke 9 | 15 % → 14 % | 54.3 px | 0.41 | 0.93 | 314 |
| stroke 10 | 14 % → 14 % | 56.6 px | 0.41 | 0.97 | 301 |
| stroke 11 | 16 % → 15 % | 60.6 px | 0.41 | 0.92 | 279 |
| stroke 12 | 16 % → 15 % | 63.4 px | 0.41 | 0.94 | 294 |
| stroke 13 | 17 % → 16 % | 61.2 px | 0.41 | 0.97 | 213 |
| stroke 14 | 16 % → 16 % | 63.9 px | 0.41 | 0.97 | 260 |
| stroke 15 | 16 % → 14 % | 59.9 px | 0.41 | 0.87 | 260 |
| stroke 16 | 15 % → 12 % | 61.4 px | 0.41 | 0.78 | 200 |
| stroke 17 | 16 % → 11 % | 56.7 px | 0.41 | 0.68 | 214 |
| stroke 18 | 19 % → 11 % | 69.3 px | 0.41 | 0.60 | 203 |

Numbers say: wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #24 Picasso flat oil — own sheet
own sheet 600 × 600 · Oil · 34 px · 10.2 s

![Brush Artist · Refs · #24 Picasso flat oil — own sheet](Brush-Artist-Refs-24-Picasso-flat-oil-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 17 % → 46 % | 35.6 px | 0.23 | 2.73 | 211 |
| stroke 2 | 21 % → 49 % | 48.5 px | 0.24 | 2.38 | 243 |
| stroke 3 | 29 % → 60 % | 64.2 px | 0.23 | 2.05 | 249 |
| stroke 4 | 38 % → 66 % | 85.1 px | 0.23 | 1.75 | 251 |
| stroke 5 | 44 % → 72 % | 97.2 px | 0.23 | 1.63 | 196 |
| stroke 6 | 45 % → 67 % | 104.5 px | 0.23 | 1.50 | 224 |
| stroke 7 | 46 % → 68 % | 97.4 px | 0.23 | 1.46 | 275 |
| stroke 8 | 45 % → 68 % | 109.1 px | 0.23 | 1.51 | 229 |
| stroke 9 | 38 % → 64 % | 83.4 px | 0.23 | 1.69 | 234 |
| stroke 10 | 40 % → 63 % | 95.6 px | 0.23 | 1.58 | 213 |
| stroke 11 | 38 % → 62 % | 81.6 px | 0.23 | 1.62 | 200 |
| stroke 12 | 40 % → 63 % | 94.7 px | 0.23 | 1.60 | 243 |
| stroke 13 | 40 % → 70 % | 87.1 px | 0.23 | 1.76 | 195 |
| stroke 14 | 41 % → 71 % | 92.4 px | 0.23 | 1.74 | 230 |
| stroke 15 | 41 % → 64 % | 86.1 px | 0.23 | 1.58 | 197 |
| stroke 16 | 39 % → 56 % | 91.3 px | 0.23 | 1.43 | 255 |
| stroke 17 | 45 % → 50 % | 93.3 px | 0.23 | 1.12 | 216 |
| stroke 18 | 44 % → 44 % | 106.7 px | 0.23 | 1.00 | 217 |

Numbers say: wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #25 Yellow heavy flat stroke — own sheet
own sheet 600 × 600 · Heavy acrylic · 110 px · 4.5 s

![Brush Artist · Refs · #25 Yellow heavy flat stroke — own sheet](Brush-Artist-Refs-25-Yellow-heavy-flat-stroke-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 19 % → 19 % | 110.5 px | 0.18 | 0.98 | 1045 |

## Brush Artist · Refs · #27 Orange impasto swatch — own sheet
own sheet 600 × 600 · Heavy acrylic · 60 px · 7.1 s

![Brush Artist · Refs · #27 Orange impasto swatch — own sheet](Brush-Artist-Refs-27-Orange-impasto-swatch-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 9 % → 29 % | 68.9 px | 0.35 | 3.19 | 120 |
| stroke 2 | 8 % → 41 % | 72.3 px | 0.34 | 4.94 | 87 |
| stroke 3 | 29 % → 45 % | 285.3 px | 0.35 | 1.52 | 67 |
| stroke 4 | 11 % → 15 % | 77.4 px | 0.34 | 1.39 | 120 |
| stroke 5 | 17 % → 33 % | 63.6 px | 0.33 | 1.90 | 119 |
| stroke 6 | 20 % → 40 % | 166.9 px | 0.34 | 1.96 | 99 |
| stroke 7 | 9 % → 18 % | 80.4 px | 0.34 | 2.03 | 77 |
| stroke 8 | 38 % → 44 % | 387.7 px | 0.34 | 1.16 | 68 |
| stroke 9 | 40 % → 40 % | 195.9 px | 0.34 | 1.00 | 125 |
| stroke 10 | 36 % → 38 % | 330.2 px | 0.33 | 1.03 | 92 |

Numbers say: wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #28 Miles Davis black lines — own sheet
own sheet 600 × 600 · Ink · 22 px · 9.1 s

![Brush Artist · Refs · #28 Miles Davis black lines — own sheet](Brush-Artist-Refs-28-Miles-Davis-black-lines-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 22 % → 32 % | 36.6 px | 0.88 | 1.42 | 251 |
| stroke 2 | 28 % → 49 % | 38.3 px | 0.88 | 1.73 | 157 |
| stroke 3 | 39 % → 44 % | 75.1 px | 0.88 | 1.12 | 125 |
| stroke 4 | 42 % → 48 % | 83.7 px | 0.88 | 1.15 | 246 |
| stroke 5 | 55 % → 55 % | 109.9 px | 0.88 | 1.00 | 169 |

Numbers say: wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #29 Shrigley magenta asterisk — own sheet
own sheet 600 × 600 · Watercolor · 70 px · 8.9 s

![Brush Artist · Refs · #29 Shrigley magenta asterisk — own sheet](Brush-Artist-Refs-29-Shrigley-magenta-asterisk-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 13 % → 37 % | 46.6 px | 0.72 | 2.85 | 258 |
| stroke 2 | 12 % → 12 % | 87.1 px | 0.71 | 1.00 | 231 |
| stroke 3 | 28 % → 37 % | 100.9 px | 0.72 | 1.31 | 309 |
| stroke 4 | 23 % → 23 % | 163.9 px | 0.71 | 1.02 | 406 |

Numbers say: wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #30 Red gouache face patch — own sheet
own sheet 600 × 600 · Gouache · 60 px · 15.7 s

![Brush Artist · Refs · #30 Red gouache face patch — own sheet](Brush-Artist-Refs-30-Red-gouache-face-patch-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 12 % → 37 % | 51.5 px | 0.53 | 3.22 | 213 |
| stroke 2 | 15 % → 40 % | 74.6 px | 0.53 | 2.72 | 236 |
| stroke 3 | 24 % → 50 % | 116.0 px | 0.53 | 2.06 | 204 |
| stroke 4 | 27 % → 51 % | 134.1 px | 0.53 | 1.93 | 238 |
| stroke 5 | 34 % → 60 % | 159.9 px | 0.53 | 1.77 | 216 |
| stroke 6 | 35 % → 61 % | 178.3 px | 0.53 | 1.76 | 239 |
| stroke 7 | 34 % → 59 % | 160.9 px | 0.54 | 1.73 | 215 |
| stroke 8 | 34 % → 56 % | 162.5 px | 0.53 | 1.65 | 265 |
| stroke 9 | 36 % → 60 % | 173.1 px | 0.53 | 1.66 | 208 |
| stroke 10 | 38 % → 62 % | 196.8 px | 0.53 | 1.63 | 207 |
| stroke 11 | 37 % → 61 % | 182.5 px | 0.53 | 1.66 | 211 |
| stroke 12 | 36 % → 58 % | 178.3 px | 0.53 | 1.62 | 224 |
| stroke 13 | 33 % → 46 % | 156.5 px | 0.53 | 1.39 | 211 |
| stroke 14 | 33 % → 41 % | 157.7 px | 0.53 | 1.25 | 255 |
| stroke 15 | 33 % → 37 % | 153.4 px | 0.53 | 1.12 | 203 |
| stroke 16 | 39 % → 39 % | 184.9 px | 0.53 | 0.99 | 220 |

Numbers say: wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #31 Warhol blotted line — own sheet
own sheet 600 × 600 · Ink · 6 px · 6.0 s

![Brush Artist · Refs · #31 Warhol blotted line — own sheet](Brush-Artist-Refs-31-Warhol-blotted-line-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 21 % → 42 % | 15.8 px | 0.82 | 1.98 | 119 |
| stroke 2 | 17 % → 23 % | 15.9 px | 0.82 | 1.34 | 117 |
| stroke 3 | 24 % → 25 % | 25.1 px | 0.81 | 1.02 | 119 |
| stroke 4 | 31 % → 40 % | 31.9 px | 0.82 | 1.28 | 79 |
| stroke 5 | 35 % → 44 % | 36.4 px | 0.82 | 1.23 | 117 |
| stroke 6 | 32 % → 33 % | 26.7 px | 0.81 | 1.03 | 87 |

Numbers say: wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #32 Thick orange swipes — own sheet
own sheet 600 × 600 · Heavy acrylic · 90 px · 4.6 s

![Brush Artist · Refs · #32 Thick orange swipes — own sheet](Brush-Artist-Refs-32-Thick-orange-swipes-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 15 % → 29 % | 91.7 px | 0.03 | 1.91 | 438 |
| stroke 2 | 28 % → 40 % | 188.8 px | 0.03 | 1.44 | 368 |
| stroke 3 | 30 % → 29 % | 190.2 px | 0.03 | 0.98 | 366 |

Numbers say: wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #33 Red wet-in-wet band — own sheet
own sheet 600 × 600 · Watercolor · 80 px · 12.6 s

![Brush Artist · Refs · #33 Red wet-in-wet band — own sheet](Brush-Artist-Refs-33-Red-wet-in-wet-band-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 23 % → 57 % | 88.2 px | 0.61 | 2.46 | 518 |
| stroke 2 | 30 % → 52 % | 243.9 px | 0.61 | 1.73 | 125 |
| stroke 3 | 37 % → 54 % | 356.6 px | 0.61 | 1.47 | 170 |
| stroke 4 | 42 % → 61 % | 412.6 px | 0.62 | 1.43 | 123 |
| stroke 5 | 42 % → 55 % | 354.2 px | 0.61 | 1.33 | 182 |
| stroke 6 | 42 % → 47 % | 321.5 px | 0.60 | 1.11 | 167 |

Numbers say: wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #34 Magenta oil patches — own sheet
own sheet 600 × 600 · Oil · 60 px · 7.3 s

![Brush Artist · Refs · #34 Magenta oil patches — own sheet](Brush-Artist-Refs-34-Magenta-oil-patches-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 10 % → 46 % | 68.9 px | 0.13 | 4.68 | 121 |
| stroke 2 | 11 % → 32 % | 71.2 px | 0.13 | 3.02 | 147 |
| stroke 3 | 9 % → 40 % | 71.5 px | 0.13 | 4.71 | 188 |
| stroke 4 | 18 % → 25 % | 149.6 px | 0.13 | 1.37 | 130 |
| stroke 5 | 27 % → 39 % | 145.1 px | 0.12 | 1.43 | 206 |
| stroke 6 | 22 % → 41 % | 187.6 px | 0.13 | 1.86 | 113 |
| stroke 7 | 34 % → 40 % | 268.4 px | 0.13 | 1.18 | 210 |
| stroke 8 | 36 % → 43 % | 256.5 px | 0.13 | 1.19 | 177 |
| stroke 9 | 26 % → 28 % | 170.2 px | 0.13 | 1.08 | 157 |
| stroke 10 | 31 % → 31 % | 275.9 px | 0.13 | 1.00 | 129 |
| stroke 11 | 40 % → 40 % | 359.9 px | 0.13 | 1.00 | 128 |
| stroke 12 | 29 % → 29 % | 205.9 px | 0.13 | 1.00 | 123 |

Numbers say: wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #35 Red band with runs — own sheet
own sheet 600 × 600 · Watercolor · 70 px · 8.0 s

![Brush Artist · Refs · #35 Red band with runs — own sheet](Brush-Artist-Refs-35-Red-band-with-runs-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 21 % → 36 % | 77.5 px | 0.46 | 1.75 | 430 |

Numbers say: wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #36 Magenta letters flat brush — own sheet
own sheet 600 × 600 · Gouache · 36 px · 15.3 s

![Brush Artist · Refs · #36 Magenta letters flat brush — own sheet](Brush-Artist-Refs-36-Magenta-letters-flat-brush-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 20 % → 39 % | 59.1 px | 0.50 | 1.95 | 44 |
| stroke 2 | 20 % → 32 % | 46.7 px | 0.50 | 1.59 | 49 |
| stroke 3 | 29 % → 54 % | 86.9 px | 0.50 | 1.86 | 36 |
| stroke 4 | 26 % → 44 % | 51.3 px | 0.50 | 1.67 | 143 |
| stroke 5 | 33 % → 55 % | 96.2 px | 0.50 | 1.67 | 101 |
| stroke 6 | 42 % → 56 % | 242.7 px | 0.50 | 1.33 | 23 |
| stroke 7 | 30 % → 44 % | 56.8 px | 0.50 | 1.45 | 136 |
| stroke 8 | 31 % → 53 % | 98.5 px | 0.50 | 1.68 | 78 |
| stroke 9 | 38 % → 51 % | 158.3 px | 0.50 | 1.33 | 36 |
| stroke 10 | 37 % → 64 % | 106.7 px | 0.50 | 1.72 | 99 |
| stroke 11 | 39 % → 62 % | 225.8 px | 0.50 | 1.58 | 23 |
| stroke 12 | 43 % → 56 % | 81.9 px | 0.50 | 1.29 | 142 |
| stroke 13 | 33 % → 46 % | 117.7 px | 0.50 | 1.43 | 42 |
| stroke 14 | 35 % → 52 % | 134.5 px | 0.50 | 1.47 | 35 |
| stroke 15 | 38 % → 56 % | 108.6 px | 0.50 | 1.49 | 117 |
| stroke 16 | 41 % → 50 % | 232.0 px | 0.50 | 1.23 | 28 |
| stroke 17 | 44 % → 52 % | 81.7 px | 0.50 | 1.19 | 136 |
| stroke 18 | 27 % → 36 % | 97.6 px | 0.50 | 1.35 | 44 |
| stroke 19 | 40 % → 39 % | 117.2 px | 0.50 | 0.96 | 40 |
| stroke 20 | 45 % → 45 % | 132.3 px | 0.50 | 0.99 | 30 |
| stroke 21 | 41 % → 39 % | 78.7 px | 0.50 | 0.96 | 100 |

Numbers say: wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #37 Oil still life dabs — own sheet
own sheet 600 × 600 · Oil · 40 px · 6.5 s

![Brush Artist · Refs · #37 Oil still life dabs — own sheet](Brush-Artist-Refs-37-Oil-still-life-dabs-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 8 % → 8 % | 50.5 px | 0.39 | 1.01 | 49 |
| stroke 2 | 7 % → 30 % | 52.7 px | 0.39 | 4.05 | 32 |
| stroke 3 | 14 % → 39 % | 109.5 px | 0.39 | 2.81 | 30 |
| stroke 4 | 10 % → 10 % | 47.7 px | 0.39 | 1.01 | 47 |
| stroke 5 | 7 % → 13 % | 51.7 px | 0.39 | 1.78 | 23 |
| stroke 6 | 14 % → 33 % | 90.8 px | 0.39 | 2.32 | 53 |
| stroke 7 | 13 % → 29 % | 144.0 px | 0.39 | 2.16 | 17 |
| stroke 8 | 11 % → 18 % | 117.7 px | 0.39 | 1.62 | 14 |
| stroke 9 | 15 % → 17 % | 79.1 px | 0.38 | 1.09 | 54 |
| stroke 10 | 23 % → 29 % | 117.3 px | 0.38 | 1.28 | 53 |
| stroke 11 | 27 % → 33 % | 223.3 px | 0.39 | 1.23 | 39 |
| stroke 12 | 23 % → 25 % | 253.7 px | 0.39 | 1.07 | 36 |
| stroke 13 | 19 % → 19 % | 189.1 px | 0.40 | 1.01 | 34 |
| stroke 14 | 20 % → 20 % | 163.8 px | 0.39 | 1.01 | 35 |

Numbers say: wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #38 Sanguine drawing — own sheet
own sheet 600 × 600 · Pastel · 6 px · 3.8 s

![Brush Artist · Refs · #38 Sanguine drawing — own sheet](Brush-Artist-Refs-38-Sanguine-drawing-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 3 % → 14 % | 2.9 px | 0.57 | 5.29 | 12 |
| stroke 2 | 3 % → 7 % | 2.9 px | 0.57 | 2.89 | 17 |
| stroke 3 | 3 % → 9 % | 2.9 px | 0.57 | 3.40 | 11 |
| stroke 4 | 2 % → 17 % | 2.7 px | 0.57 | 7.20 | 11 |
| stroke 5 | 2 % → 7 % | 2.7 px | 0.57 | 3.03 | 27 |
| stroke 6 | 3 % → 19 % | 3.4 px | 0.57 | 6.31 | 23 |
| stroke 7 | 5 % → 14 % | 5.2 px | 0.57 | 3.07 | 12 |
| stroke 8 | 4 % → 16 % | 4.7 px | 0.57 | 3.79 | 14 |
| stroke 9 | 3 % → 7 % | 2.9 px | 0.57 | 2.66 | 8 |
| stroke 10 | 4 % → 16 % | 4.7 px | 0.57 | 3.83 | 12 |
| stroke 11 | 3 % → 4 % | 2.9 px | 0.57 | 1.61 | 21 |
| stroke 12 | 4 % → 15 % | 4.8 px | 0.57 | 3.58 | 14 |
| stroke 13 | 8 % → 17 % | 8.9 px | 0.57 | 2.23 | 21 |
| stroke 14 | 4 % → 14 % | 4.9 px | 0.57 | 3.19 | 20 |
| stroke 15 | 9 % → 18 % | 10.7 px | 0.57 | 1.86 | 11 |
| stroke 16 | 6 % → 16 % | 6.6 px | 0.57 | 2.71 | 9 |
| stroke 17 | 4 % → 9 % | 4.4 px | 0.57 | 2.25 | 16 |
| stroke 18 | 3 % → 5 % | 2.9 px | 0.57 | 1.85 | 14 |
| stroke 19 | 6 % → 16 % | 6.9 px | 0.57 | 2.68 | 8 |
| stroke 20 | 8 % → 14 % | 9.2 px | 0.57 | 1.70 | 13 |
| stroke 21 | 4 % → 4 % | 4.3 px | 0.57 | 1.00 | 14 |
| stroke 22 | 8 % → 13 % | 8.6 px | 0.57 | 1.79 | 14 |
| stroke 23 | 7 % → 12 % | 8.3 px | 0.57 | 1.61 | 13 |
| stroke 24 | 4 % → 7 % | 4.7 px | 0.57 | 1.71 | 18 |
| stroke 25 | 8 % → 14 % | 8.7 px | 0.57 | 1.84 | 14 |
| stroke 26 | 6 % → 8 % | 6.5 px | 0.57 | 1.34 | 15 |
| stroke 27 | 4 % → 4 % | 4.3 px | 0.57 | 1.10 | 12 |
| stroke 28 | 7 % → 11 % | 8.2 px | 0.57 | 1.59 | 31 |
| stroke 29 | 8 % → 17 % | 8.8 px | 0.57 | 2.21 | 8 |
| stroke 30 | 13 % → 17 % | 14.9 px | 0.57 | 1.29 | 14 |
| stroke 31 | 5 % → 6 % | 5.4 px | 0.57 | 1.29 | 12 |
| stroke 32 | 10 % → 13 % | 11.8 px | 0.57 | 1.24 | 16 |
| stroke 33 | 7 % → 8 % | 8.5 px | 0.57 | 1.07 | 9 |
| stroke 34 | 11 % → 14 % | 12.0 px | 0.57 | 1.36 | 10 |
| stroke 35 | 9 % → 14 % | 10.0 px | 0.57 | 1.61 | 9 |
| stroke 36 | 10 % → 13 % | 11.4 px | 0.57 | 1.26 | 12 |
| stroke 37 | 9 % → 16 % | 10.5 px | 0.57 | 1.71 | 17 |
| stroke 38 | 13 % → 19 % | 14.8 px | 0.57 | 1.48 | 13 |
| stroke 39 | 14 % → 17 % | 15.7 px | 0.57 | 1.21 | 8 |
| stroke 40 | 6 % → 7 % | 7.2 px | 0.57 | 1.14 | 15 |
| stroke 41 | 16 % → 16 % | 17.7 px | 0.57 | 1.01 | 21 |
| stroke 42 | 14 % → 16 % | 15.2 px | 0.57 | 1.17 | 12 |
| stroke 43 | 10 % → 12 % | 11.6 px | 0.57 | 1.17 | 17 |
| stroke 44 | 12 % → 15 % | 14.3 px | 0.57 | 1.22 | 18 |
| stroke 45 | 2 % → 2 % | 2.7 px | 0.57 | 1.00 | 13 |
| stroke 46 | 16 % → 16 % | 18.5 px | 0.57 | 1.00 | 13 |
| stroke 47 | 13 % → 13 % | 15.0 px | 0.57 | 1.00 | 9 |
| stroke 48 | 12 % → 13 % | 14.3 px | 0.57 | 1.07 | 16 |
| stroke 49 | 19 % → 19 % | 21.5 px | 0.57 | 1.00 | 18 |
| stroke 50 | 10 % → 10 % | 11.6 px | 0.57 | 1.00 | 11 |

Numbers say: wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #39 Very thick impasto — own sheet
own sheet 600 × 600 · Heavy acrylic · 60 px · 7.7 s

![Brush Artist · Refs · #39 Very thick impasto — own sheet](Brush-Artist-Refs-39-Very-thick-impasto-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 27 % → 39 % | 61.5 px | 0.43 | 1.45 | 375 |
| stroke 2 | 32 % → 50 % | 96.9 px | 0.44 | 1.56 | 385 |
| stroke 3 | 38 % → 52 % | 128.8 px | 0.44 | 1.35 | 350 |
| stroke 4 | 32 % → 46 % | 93.6 px | 0.44 | 1.43 | 404 |
| stroke 5 | 43 % → 43 % | 108.0 px | 0.44 | 0.99 | 404 |

Numbers say: wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #40 Watercolour blooms — own sheet
own sheet 600 × 600 · Watercolor · 90 px · 9.9 s

![Brush Artist · Refs · #40 Watercolour blooms — own sheet](Brush-Artist-Refs-40-Watercolour-blooms-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 21 % → 25 % | 92.4 px | 0.13 | 1.20 | 977 |

## Brush Artist · Refs · #41 Coloured pencil hatching — own sheet
own sheet 600 × 600 · Pastel · 4 px · 3.6 s

![Brush Artist · Refs · #41 Coloured pencil hatching — own sheet](Brush-Artist-Refs-41-Coloured-pencil-hatching-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 3 % → 13 % | 2.2 px | 0.35 | 4.64 | 12 |
| stroke 2 | 3 % → 7 % | 2.3 px | 0.35 | 2.29 | 5 |
| stroke 3 | 2 % → 11 % | 1.9 px | 0.35 | 4.38 | 12 |
| stroke 4 | 3 % → 19 % | 2.1 px | 0.35 | 6.73 | 5 |
| stroke 5 | 4 % → 7 % | 2.9 px | 0.35 | 1.83 | 4 |
| stroke 6 | 3 % → 13 % | 2.3 px | 0.35 | 4.19 | 5 |
| stroke 7 | 3 % → 15 % | 2.6 px | 0.35 | 4.43 | 8 |
| stroke 8 | 3 % → 12 % | 2.1 px | 0.35 | 4.20 | 4 |
| stroke 9 | 5 % → 11 % | 3.6 px | 0.35 | 2.27 | 5 |
| stroke 10 | 5 % → 15 % | 3.8 px | 0.35 | 2.99 | 12 |
| stroke 11 | 4 % → 13 % | 3.0 px | 0.35 | 3.28 | 4 |
| stroke 12 | 3 % → 3 % | 2.1 px | 0.35 | 1.00 | 7 |
| stroke 13 | 7 % → 17 % | 5.2 px | 0.35 | 2.45 | 6 |
| stroke 14 | 3 % → 13 % | 2.4 px | 0.35 | 4.19 | 5 |
| stroke 15 | 6 % → 12 % | 4.4 px | 0.35 | 2.09 | 7 |
| stroke 16 | 7 % → 11 % | 5.1 px | 0.35 | 1.61 | 8 |
| stroke 17 | 3 % → 3 % | 2.1 px | 0.35 | 1.00 | 7 |
| stroke 18 | 5 % → 8 % | 3.6 px | 0.35 | 1.65 | 5 |
| stroke 19 | 5 % → 13 % | 3.8 px | 0.35 | 2.72 | 7 |
| stroke 20 | 5 % → 14 % | 3.7 px | 0.35 | 2.92 | 4 |
| stroke 21 | 4 % → 13 % | 3.2 px | 0.35 | 3.20 | 5 |
| stroke 22 | 9 % → 16 % | 6.8 px | 0.35 | 1.77 | 7 |
| stroke 23 | 9 % → 13 % | 6.5 px | 0.35 | 1.55 | 11 |
| stroke 24 | 6 % → 14 % | 4.7 px | 0.35 | 2.18 | 5 |
| stroke 25 | 5 % → 10 % | 3.5 px | 0.35 | 2.27 | 7 |
| stroke 26 | 3 % → 6 % | 2.7 px | 0.35 | 1.81 | 4 |
| stroke 27 | 3 % → 7 % | 2.3 px | 0.35 | 2.26 | 6 |
| stroke 28 | 6 % → 10 % | 4.5 px | 0.35 | 1.70 | 4 |
| stroke 29 | 3 % → 13 % | 2.4 px | 0.35 | 4.21 | 6 |
| stroke 30 | 6 % → 9 % | 4.4 px | 0.35 | 1.46 | 5 |
| stroke 31 | 7 % → 14 % | 5.1 px | 0.35 | 2.14 | 4 |
| stroke 32 | 3 % → 6 % | 2.5 px | 0.35 | 1.79 | 13 |
| stroke 33 | 6 % → 11 % | 5.0 px | 0.35 | 1.67 | 6 |
| stroke 34 | 3 % → 6 % | 2.6 px | 0.35 | 1.73 | 7 |
| stroke 35 | 7 % → 14 % | 5.0 px | 0.35 | 2.09 | 10 |
| stroke 36 | 5 % → 5 % | 3.7 px | 0.35 | 1.01 | 5 |
| stroke 37 | 7 % → 15 % | 5.2 px | 0.35 | 2.15 | 4 |
| stroke 38 | 8 % → 13 % | 5.8 px | 0.35 | 1.66 | 11 |
| stroke 39 | 7 % → 11 % | 5.1 px | 0.35 | 1.67 | 8 |
| stroke 40 | 8 % → 18 % | 6.2 px | 0.35 | 2.21 | 11 |
| stroke 41 | 9 % → 13 % | 6.9 px | 0.35 | 1.48 | 9 |
| stroke 42 | 10 % → 17 % | 7.7 px | 0.35 | 1.73 | 7 |
| stroke 43 | 5 % → 9 % | 3.9 px | 0.35 | 1.66 | 4 |
| stroke 44 | 10 % → 13 % | 7.3 px | 0.35 | 1.40 | 5 |
| stroke 45 | 13 % → 18 % | 9.9 px | 0.35 | 1.35 | 9 |
| stroke 46 | 5 % → 7 % | 3.6 px | 0.34 | 1.41 | 9 |
| stroke 47 | 11 % → 13 % | 8.0 px | 0.35 | 1.20 | 9 |
| stroke 48 | 12 % → 16 % | 9.2 px | 0.35 | 1.34 | 7 |
| stroke 49 | 6 % → 9 % | 4.2 px | 0.35 | 1.66 | 4 |
| stroke 50 | 7 % → 7 % | 5.2 px | 0.34 | 1.00 | 8 |
| stroke 51 | 8 % → 15 % | 6.4 px | 0.35 | 1.74 | 5 |
| stroke 52 | 12 % → 14 % | 9.1 px | 0.35 | 1.19 | 8 |
| stroke 53 | 11 % → 14 % | 8.1 px | 0.35 | 1.36 | 5 |
| stroke 54 | 10 % → 14 % | 7.4 px | 0.35 | 1.47 | 7 |
| stroke 55 | 11 % → 14 % | 8.2 px | 0.35 | 1.33 | 17 |
| stroke 56 | 11 % → 12 % | 8.4 px | 0.35 | 1.11 | 8 |
| stroke 57 | 9 % → 13 % | 7.1 px | 0.35 | 1.37 | 4 |
| stroke 58 | 10 % → 11 % | 7.7 px | 0.35 | 1.14 | 4 |
| stroke 59 | 11 % → 13 % | 8.4 px | 0.35 | 1.18 | 5 |
| stroke 60 | 16 % → 20 % | 11.9 px | 0.35 | 1.26 | 4 |
| stroke 61 | 19 % → 20 % | 14.5 px | 0.35 | 1.04 | 5 |
| stroke 62 | 10 % → 10 % | 7.3 px | 0.35 | 1.00 | 5 |
| stroke 63 | 11 % → 12 % | 8.7 px | 0.35 | 1.07 | 4 |
| stroke 64 | 14 % → 14 % | 10.7 px | 0.35 | 1.02 | 4 |
| stroke 65 | 15 % → 15 % | 11.5 px | 0.35 | 1.00 | 12 |
| stroke 66 | 14 % → 14 % | 10.7 px | 0.35 | 1.00 | 5 |
| stroke 67 | 12 % → 12 % | 8.8 px | 0.35 | 1.06 | 4 |
| stroke 68 | 5 % → 9 % | 3.6 px | 0.35 | 1.88 | 11 |
| stroke 69 | 5 % → 5 % | 4.1 px | 0.35 | 1.00 | 5 |
| stroke 70 | 10 % → 13 % | 7.4 px | 0.35 | 1.28 | 4 |
| stroke 71 | 9 % → 11 % | 7.1 px | 0.35 | 1.15 | 5 |
| stroke 72 | 5 % → 7 % | 4.2 px | 0.35 | 1.23 | 5 |
| stroke 73 | 12 % → 12 % | 9.3 px | 0.35 | 1.00 | 6 |
| stroke 74 | 14 % → 14 % | 10.8 px | 0.35 | 1.00 | 5 |
| stroke 75 | 15 % → 15 % | 11.4 px | 0.35 | 1.00 | 5 |
| stroke 76 | 14 % → 14 % | 10.5 px | 0.35 | 1.00 | 13 |
| stroke 77 | 7 % → 10 % | 5.4 px | 0.35 | 1.34 | 10 |
| stroke 78 | 9 % → 9 % | 7.0 px | 0.35 | 1.00 | 4 |
| stroke 79 | 7 % → 7 % | 5.7 px | 0.35 | 1.00 | 4 |
| stroke 80 | 11 % → 11 % | 8.3 px | 0.35 | 1.00 | 6 |

Numbers say: wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #42 Oil pastel shaggy — own sheet
own sheet 600 × 600 · Pastel · 18 px · 4.9 s

![Brush Artist · Refs · #42 Oil pastel shaggy — own sheet](Brush-Artist-Refs-42-Oil-pastel-shaggy-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 5 % → 27 % | 8.0 px | 0.28 | 5.73 | 10 |
| stroke 2 | 5 % → 24 % | 8.6 px | 0.28 | 4.69 | 15 |
| stroke 3 | 5 % → 29 % | 8.9 px | 0.28 | 5.42 | 12 |
| stroke 4 | 5 % → 11 % | 8.8 px | 0.28 | 2.08 | 11 |
| stroke 5 | 6 % → 11 % | 9.9 px | 0.28 | 1.85 | 14 |
| stroke 6 | 8 % → 37 % | 13.9 px | 0.29 | 4.44 | 13 |
| stroke 7 | 11 % → 31 % | 17.6 px | 0.28 | 2.90 | 9 |
| stroke 8 | 7 % → 38 % | 11.4 px | 0.28 | 5.55 | 9 |
| stroke 9 | 8 % → 21 % | 13.9 px | 0.28 | 2.53 | 16 |
| stroke 10 | 8 % → 18 % | 13.2 px | 0.28 | 2.32 | 11 |
| stroke 11 | 6 % → 27 % | 9.4 px | 0.28 | 4.74 | 11 |
| stroke 12 | 8 % → 19 % | 13.6 px | 0.28 | 2.29 | 10 |
| stroke 13 | 13 % → 24 % | 21.0 px | 0.28 | 1.92 | 19 |
| stroke 14 | 5 % → 23 % | 7.9 px | 0.28 | 4.77 | 12 |
| stroke 15 | 5 % → 24 % | 9.0 px | 0.29 | 4.38 | 14 |
| stroke 16 | 9 % → 21 % | 15.7 px | 0.29 | 2.18 | 12 |
| stroke 17 | 17 % → 39 % | 27.9 px | 0.29 | 2.34 | 11 |
| stroke 18 | 14 % → 25 % | 22.8 px | 0.29 | 1.79 | 21 |
| stroke 19 | 15 % → 32 % | 24.9 px | 0.28 | 2.09 | 16 |
| stroke 20 | 21 % → 39 % | 35.1 px | 0.28 | 1.85 | 13 |
| stroke 21 | 9 % → 16 % | 14.4 px | 0.28 | 1.88 | 11 |
| stroke 22 | 14 % → 17 % | 23.9 px | 0.28 | 1.20 | 11 |
| stroke 23 | 12 % → 17 % | 20.6 px | 0.29 | 1.34 | 14 |
| stroke 24 | 18 % → 26 % | 30.0 px | 0.29 | 1.44 | 18 |
| stroke 25 | 20 % → 34 % | 32.6 px | 0.28 | 1.74 | 13 |
| stroke 26 | 6 % → 14 % | 9.2 px | 0.28 | 2.43 | 16 |
| stroke 27 | 18 % → 26 % | 30.4 px | 0.29 | 1.41 | 11 |
| stroke 28 | 14 % → 24 % | 23.7 px | 0.28 | 1.68 | 14 |
| stroke 29 | 9 % → 27 % | 14.9 px | 0.29 | 3.01 | 11 |
| stroke 30 | 15 % → 36 % | 24.9 px | 0.29 | 2.43 | 17 |
| stroke 31 | 14 % → 17 % | 23.3 px | 0.28 | 1.23 | 18 |
| stroke 32 | 16 % → 29 % | 27.0 px | 0.29 | 1.82 | 20 |
| stroke 33 | 15 % → 16 % | 24.5 px | 0.29 | 1.09 | 17 |
| stroke 34 | 19 % → 27 % | 31.4 px | 0.28 | 1.44 | 23 |
| stroke 35 | 26 % → 36 % | 42.5 px | 0.28 | 1.40 | 29 |
| stroke 36 | 25 % → 34 % | 41.0 px | 0.28 | 1.36 | 17 |
| stroke 37 | 12 % → 12 % | 19.3 px | 0.28 | 1.03 | 21 |
| stroke 38 | 19 % → 25 % | 31.7 px | 0.28 | 1.30 | 21 |
| stroke 39 | 16 % → 22 % | 27.3 px | 0.28 | 1.37 | 17 |
| stroke 40 | 22 % → 31 % | 36.6 px | 0.28 | 1.38 | 25 |
| stroke 41 | 32 % → 36 % | 53.1 px | 0.28 | 1.12 | 19 |
| stroke 42 | 23 % → 30 % | 38.1 px | 0.29 | 1.29 | 20 |
| stroke 43 | 12 % → 12 % | 20.3 px | 0.28 | 1.00 | 10 |
| stroke 44 | 30 % → 37 % | 48.9 px | 0.28 | 1.26 | 16 |
| stroke 45 | 16 % → 16 % | 26.2 px | 0.28 | 1.00 | 40 |
| stroke 46 | 29 % → 34 % | 47.9 px | 0.29 | 1.15 | 53 |
| stroke 47 | 38 % → 41 % | 62.0 px | 0.28 | 1.10 | 20 |
| stroke 48 | 29 % → 36 % | 47.8 px | 0.29 | 1.27 | 38 |
| stroke 49 | 27 % → 30 % | 45.1 px | 0.29 | 1.11 | 29 |
| stroke 50 | 38 % → 40 % | 63.4 px | 0.28 | 1.06 | 37 |
| stroke 51 | 16 % → 16 % | 26.0 px | 0.28 | 1.00 | 54 |
| stroke 52 | 37 % → 38 % | 62.4 px | 0.29 | 1.01 | 28 |
| stroke 53 | 22 % → 26 % | 36.9 px | 0.28 | 1.18 | 19 |
| stroke 54 | 17 % → 19 % | 29.0 px | 0.29 | 1.09 | 13 |
| stroke 55 | 15 % → 15 % | 25.0 px | 0.28 | 1.00 | 28 |
| stroke 56 | 13 % → 14 % | 21.6 px | 0.28 | 1.08 | 24 |
| stroke 57 | 23 % → 23 % | 37.7 px | 0.29 | 1.00 | 38 |
| stroke 58 | 28 % → 29 % | 46.1 px | 0.28 | 1.05 | 18 |
| stroke 59 | 40 % → 40 % | 67.3 px | 0.28 | 1.00 | 45 |
| stroke 60 | 22 % → 22 % | 35.6 px | 0.28 | 1.00 | 26 |

Numbers say: wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #43 Dragged black ink blocks — own sheet
own sheet 600 × 600 · Gouache · 70 px · 11.6 s

![Brush Artist · Refs · #43 Dragged black ink blocks — own sheet](Brush-Artist-Refs-43-Dragged-black-ink-blocks-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 16 % → 12 % | 37.3 px | 0.46 | 0.73 | 972 |
| stroke 2 | 16 % → 13 % | 58.0 px | 0.46 | 0.78 | 1002 |
| stroke 3 | 20 % → 16 % | 72.4 px | 0.46 | 0.79 | 801 |
| stroke 4 | 20 % → 16 % | 70.6 px | 0.46 | 0.77 | 613 |
| stroke 5 | 24 % → 14 % | 56.0 px | 0.46 | 0.57 | 543 |

## Brush Artist · Refs · #44 Blue looping ribbon — own sheet
own sheet 600 × 600 · Oil · 80 px · 7.9 s

![Brush Artist · Refs · #44 Blue looping ribbon — own sheet](Brush-Artist-Refs-44-Blue-looping-ribbon-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 32 % → 32 % | 42.2 px | 0.78 | 1.00 | 3830 |

## Brush Artist · Refs · #45 Soft pastel pepper — own sheet
own sheet 600 × 600 · Pastel · 40 px · 6.1 s

![Brush Artist · Refs · #45 Soft pastel pepper — own sheet](Brush-Artist-Refs-45-Soft-pastel-pepper-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 10 % → 39 % | 11.3 px | 0.48 | 3.73 | 462 |
| stroke 2 | 18 % → 34 % | 21.3 px | 0.49 | 1.86 | 490 |
| stroke 3 | 25 % → 37 % | 17.6 px | 0.49 | 1.45 | 393 |
| stroke 4 | 24 % → 35 % | 30.5 px | 0.49 | 1.42 | 474 |
| stroke 5 | 30 % → 30 % | 21.2 px | 0.49 | 1.00 | 285 |
| stroke 6 | 35 % → 44 % | 22.5 px | 0.48 | 1.25 | 427 |
| stroke 7 | 39 % → 43 % | 21.4 px | 0.48 | 1.10 | 476 |
| stroke 8 | 44 % → 44 % | 44.2 px | 0.48 | 1.00 | 437 |

Numbers say: wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #46 Red-brown ink lips — own sheet
own sheet 600 × 600 · Watercolor · 50 px · 9.0 s

![Brush Artist · Refs · #46 Red-brown ink lips — own sheet](Brush-Artist-Refs-46-Red-brown-ink-lips-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 12 % → 24 % | 51.9 px | 0.59 | 1.91 | 162 |
| stroke 2 | 16 % → 27 % | 68.1 px | 0.54 | 1.74 | 170 |

Numbers say: wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #47 Pink knife slabs — own sheet
own sheet 600 × 600 · Heavy acrylic · 90 px · 8.5 s

![Brush Artist · Refs · #47 Pink knife slabs — own sheet](Brush-Artist-Refs-47-Pink-knife-slabs-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 18 % → 34 % | 88.7 px | 0.11 | 1.95 | 456 |
| stroke 2 | 31 % → 46 % | 176.8 px | 0.11 | 1.47 | 475 |
| stroke 3 | 31 % → 46 % | 176.8 px | 0.11 | 1.47 | 405 |
| stroke 4 | 42 % → 41 % | 176.8 px | 0.11 | 0.98 | 613 |

Numbers say: wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #48 Black bands with drips — own sheet
own sheet 600 × 600 · Gouache · 70 px · 15.6 s

![Brush Artist · Refs · #48 Black bands with drips — own sheet](Brush-Artist-Refs-48-Black-bands-with-drips-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 23 % → 36 % | 59.0 px | 0.39 | 1.58 | 844 |
| stroke 2 | 34 % → 48 % | 108.7 px | 0.39 | 1.41 | 1684 |
| stroke 3 | 36 % → 48 % | 112.8 px | 0.39 | 1.34 | 633 |
| stroke 4 | 38 % → 36 % | 111.8 px | 0.39 | 0.95 | 583 |

Numbers say: wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #49 Magenta letters round brush — own sheet
own sheet 600 × 600 · Ink · 30 px · 13.6 s

![Brush Artist · Refs · #49 Magenta letters round brush — own sheet](Brush-Artist-Refs-49-Magenta-letters-round-brush-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 27 % → 46 % | 64.3 px | 0.52 | 1.69 | 35 |
| stroke 2 | 29 % → 40 % | 52.5 px | 0.53 | 1.39 | 51 |
| stroke 3 | 41 % → 67 % | 96.4 px | 0.52 | 1.64 | 45 |
| stroke 4 | 34 % → 52 % | 53.7 px | 0.52 | 1.55 | 151 |
| stroke 5 | 40 % → 66 % | 94.8 px | 0.52 | 1.65 | 99 |
| stroke 6 | 54 % → 70 % | 231.2 px | 0.52 | 1.29 | 17 |
| stroke 7 | 41 % → 56 % | 63.9 px | 0.52 | 1.35 | 152 |
| stroke 8 | 36 % → 61 % | 91.9 px | 0.53 | 1.72 | 86 |
| stroke 9 | 49 % → 60 % | 152.9 px | 0.53 | 1.24 | 32 |
| stroke 10 | 42 % → 72 % | 100.5 px | 0.52 | 1.71 | 82 |
| stroke 11 | 52 % → 72 % | 219.5 px | 0.52 | 1.39 | 27 |
| stroke 12 | 53 % → 68 % | 82.2 px | 0.52 | 1.29 | 130 |
| stroke 13 | 42 % → 54 % | 116.0 px | 0.53 | 1.29 | 47 |
| stroke 14 | 45 % → 69 % | 131.9 px | 0.53 | 1.52 | 47 |
| stroke 15 | 43 % → 63 % | 102.4 px | 0.52 | 1.46 | 98 |
| stroke 16 | 52 % → 61 % | 220.2 px | 0.52 | 1.18 | 24 |
| stroke 17 | 53 % → 64 % | 82.3 px | 0.52 | 1.19 | 132 |
| stroke 18 | 36 % → 44 % | 99.6 px | 0.52 | 1.21 | 32 |
| stroke 19 | 54 % → 53 % | 123.8 px | 0.52 | 0.99 | 38 |
| stroke 20 | 54 % → 54 % | 125.3 px | 0.52 | 1.00 | 37 |
| stroke 21 | 49 % → 49 % | 81.3 px | 0.52 | 1.00 | 134 |

Numbers say: wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #50 Thick swipes on photo — own sheet
own sheet 600 × 600 · Heavy acrylic · 40 px · 5.7 s

![Brush Artist · Refs · #50 Thick swipes on photo — own sheet](Brush-Artist-Refs-50-Thick-swipes-on-photo-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 10 % → 26 % | 46.9 px | 0.32 | 2.58 | 55 |
| stroke 2 | 10 % → 20 % | 48.1 px | 0.31 | 1.93 | 40 |
| stroke 3 | 11 % → 13 % | 45.4 px | 0.32 | 1.16 | 48 |
| stroke 4 | 12 % → 25 % | 47.6 px | 0.32 | 2.05 | 53 |
| stroke 5 | 12 % → 13 % | 46.0 px | 0.32 | 1.07 | 46 |
| stroke 6 | 19 % → 25 % | 109.7 px | 0.31 | 1.30 | 50 |
| stroke 7 | 24 % → 31 % | 102.1 px | 0.32 | 1.29 | 58 |
| stroke 8 | 24 % → 25 % | 134.5 px | 0.32 | 1.03 | 38 |
| stroke 9 | 12 % → 14 % | 52.6 px | 0.31 | 1.20 | 70 |
| stroke 10 | 26 % → 28 % | 88.4 px | 0.31 | 1.08 | 49 |
| stroke 11 | 9 % → 10 % | 47.2 px | 0.32 | 1.09 | 42 |
| stroke 12 | 18 % → 19 % | 100.0 px | 0.32 | 1.07 | 29 |

Numbers say: wet paint spreads well beyond the stroke.

## Brush Artist · Ink — dry brush — own sheet
own sheet 600 × 600 · Gouache · 30 px · 4.0 s

![Brush Artist · Ink — dry brush — own sheet](Brush-Artist-Ink-dry-brush-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| ear | 6 % → 3 % | 7.8 px | 0.86 | 0.44 | 642 |
| drag0 | 6 % → 8 % | 10.2 px | 0.86 | 1.39 | 152 |
| drag1 | 8 % → 8 % | 16.5 px | 0.86 | 1.02 | 121 |
| drag2 | 10 % → 9 % | 22.5 px | 0.86 | 0.87 | 127 |
| drag3 | 12 % → 9 % | 29.4 px | 0.86 | 0.78 | 92 |

## Brush Artist · Watercolour — blue — own sheet
own sheet 600 × 600 · Watercolor · 40 px · 15.8 s

![Brush Artist · Watercolour — blue — own sheet](Brush-Artist-Watercolour-blue-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| s0 | 7 % → 23 % | 28.4 px | 0.25 | 3.20 | 51 |
| s1 | 5 % → 32 % | 9.9 px | 0.38 | 5.85 | 56 |
| s2 | 10 % → 18 % | 43.5 px | 0.19 | 1.75 | 51 |
| s3 | 9 % → 17 % | 26.3 px | 0.28 | 1.85 | 71 |
| s4 | 14 % → 29 % | 37.9 px | 0.36 | 2.11 | 126 |
| s5 | 19 % → 29 % | 38.9 px | 0.37 | 1.52 | 101 |
| s6 | 17 % → 21 % | 47.6 px | 0.27 | 1.22 | 74 |
| s7 | 24 % → 35 % | 31.9 px | 0.37 | 1.44 | 72 |
| s8 | 20 % → 24 % | 77.5 px | 0.27 | 1.18 | 75 |

Numbers say: wet paint spreads well beyond the stroke.

## Brush Artist · Charcoal — stick — own sheet
own sheet 600 × 600 · Charcoal · 28 px · 2.2 s

![Brush Artist · Charcoal — stick — own sheet](Brush-Artist-Charcoal-stick-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| finger0 | 9 % → 18 % | 15.5 px | 0.83 | 2.01 | 37 |
| tip0 | 8 % → 14 % | 22.1 px | 0.83 | 1.75 | 13 |
| finger1 | 17 % → 29 % | 29.4 px | 0.83 | 1.74 | 44 |
| tip1 | 15 % → 21 % | 39.1 px | 0.83 | 1.42 | 10 |
| finger2 | 17 % → 25 % | 29.5 px | 0.83 | 1.53 | 53 |
| tip2 | 14 % → 20 % | 39.0 px | 0.83 | 1.41 | 17 |
| finger3 | 16 % → 19 % | 29.3 px | 0.83 | 1.16 | 48 |
| tip3 | 15 % → 15 % | 39.0 px | 0.83 | 1.00 | 15 |
| cig0 | 25 % → 35 % | 54.8 px | 0.83 | 1.41 | 15 |
| cig1 | 26 % → 35 % | 58.8 px | 0.83 | 1.32 | 25 |
| cig2 | 28 % → 35 % | 63.2 px | 0.83 | 1.22 | 14 |
| cig3 | 30 % → 34 % | 67.3 px | 0.83 | 1.14 | 10 |
| cig4 | 32 % → 34 % | 71.5 px | 0.83 | 1.06 | 11 |
| cig5 | 34 % → 34 % | 75.3 px | 0.83 | 1.00 | 14 |

Numbers say: wet paint spreads well beyond the stroke.

## Dev · Knife #47 — own sheet
own sheet 600 × 600 · Heavy acrylic · 90 px · 5.8 s

![Dev · Knife #47 — own sheet](Dev-Knife-47-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 19 % → 39 % | 97.8 px | 0.11 | 1.98 | 89 |
| stroke 2 | 34 % → 51 % | 195.7 px | 0.11 | 1.48 | 83 |
| stroke 3 | 35 % → 51 % | 196.5 px | 0.11 | 1.48 | 98 |
| stroke 4 | 46 % → 46 % | 196.5 px | 0.11 | 0.99 | 71 |

Numbers say: wet paint spreads well beyond the stroke.

