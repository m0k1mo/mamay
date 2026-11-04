![All brushes](contact.png)

# Brush Lab — 150 brushes · Nov 4, 2026 at 6:19 AM

Every sheet: 1500 × 600, ten strokes in a 5 × 2 grid — 1. light line · 2. heavy line · 3. pressure swell · 4. fast wave · 5. slow wave · 6. spiral · 7. loop · 8. tilted · 9. over the wet one · 10. long, no reload (cell 8 holds «tilted» and «over the wet one» crossed). The CPU reference of Mamay's paint engine; the wet layer settles 20 s at the end.

Columns: **covered** = share of the cell with paint right after the stroke → after settling; **width** = painted area of the stroke ÷ its length (px); **dark** = mean darkness of the painted pixels above the paper's own grain (0 = paper, 1 = black); **spread** = how far wet paint went beyond the stroke (1.0 = stayed); **ms** = the stroke on the CPU; long stroke: paint in each quarter of its length (it should run out: wet → streaks → dry tail).

## Ink Line
Ink · 12 px · 22.9 s

![Ink Line](Ink-Line.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 1 % → 4 % | 4.3 px | 0.55 | 2.44 | 45 |
| heavy line | 5 % → 6 % | 15.7 px | 0.68 | 1.13 | 63 |
| pressure swell | 3 % → 4 % | 11.3 px | 0.64 | 1.40 | 37 |
| fast wave | 10 % → 11 % | 11.2 px | 0.59 | 1.11 | 128 |
| slow wave | 8 % → 10 % | 9.6 px | 0.57 | 1.16 | 134 |
| spiral | 14 % → 15 % | 8.9 px | 0.50 | 1.07 | 203 |
| loop | 8 % → 9 % | 10.6 px | 0.61 | 1.16 | 103 |
| tilted | 5 % → 5 % | 14.4 px | 0.65 | 1.05 | 54 |
| over the wet one | 10 % → 11 % | 12.5 px | 0.65 | 1.15 | 50 |
| long, no reload | 18 % → 17 % | 8.1 px | 0.47 | 0.96 | 304 | quarters: 0.22 → 0.09 → 0.04 → 0.02

Numbers say: light vs heavy: width 4.3 → 15.7 px, dark 0.55 → 0.68; wet paint spreads well beyond the stroke.

## Dense Ink
Ink · 14 px · 23.6 s

![Dense Ink](Dense-Ink.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 5 % → 7 % | 15.2 px | 0.72 | 1.26 | 51 |
| heavy line | 7 % → 7 % | 19.1 px | 0.73 | 1.09 | 73 |
| pressure swell | 5 % → 6 % | 17.9 px | 0.72 | 1.17 | 44 |
| fast wave | 13 % → 13 % | 15.3 px | 0.69 | 1.01 | 146 |
| slow wave | 12 % → 12 % | 13.6 px | 0.67 | 1.04 | 176 |
| spiral | 18 % → 15 % | 12.2 px | 0.65 | 0.80 | 229 |
| loop | 11 % → 12 % | 14.8 px | 0.69 | 1.08 | 121 |
| tilted | 5 % → 6 % | 14.6 px | 0.72 | 1.07 | 61 |
| over the wet one | 12 % → 13 % | 17.7 px | 0.72 | 1.11 | 55 |
| long, no reload | 23 % → 15 % | 10.1 px | 0.64 | 0.66 | 333 | quarters: 0.30 → 0.12 → 0.04 → 0.02

Numbers say: light vs heavy: width 15.2 → 19.1 px, dark 0.72 → 0.73.

## Transparent Wash
Watercolor · 22 px · 24.2 s

![Transparent Wash](Transparent-Wash.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 2 % → 5 % | 6.9 px | 0.27 | 2.25 | 41 |
| heavy line | 7 % → 9 % | 20.4 px | 0.27 | 1.22 | 59 |
| pressure swell | 4 % → 6 % | 15.2 px | 0.28 | 1.54 | 34 |
| fast wave | 14 % → 16 % | 16.1 px | 0.20 | 1.17 | 120 |
| slow wave | 12 % → 15 % | 13.7 px | 0.21 | 1.28 | 201 |
| spiral | 18 % → 22 % | 11.9 px | 0.16 | 1.23 | 180 |
| loop | 11 % → 13 % | 14.5 px | 0.22 | 1.20 | 96 |
| tilted | 8 % → 8 % | 21.1 px | 0.24 | 1.06 | 58 |
| over the wet one | 13 % → 16 % | 16.4 px | 0.24 | 1.18 | 48 |
| long, no reload | 26 % → 32 % | 11.6 px | 0.13 | 1.22 | 286 | quarters: 0.11 → 0.04 → 0.02 → 0.01

Numbers say: light vs heavy: width 6.9 → 20.4 px, dark 0.27 → 0.27; wet paint spreads well beyond the stroke.

## Dry Brush
Gouache · 24 px · 19.4 s

![Dry Brush](Dry-Brush.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 5 % → 0 % | 14.0 px | 0.65 | 0.09 | 61 |
| heavy line | 6 % → 0 % | 18.6 px | 0.65 | 0.02 | 113 |
| pressure swell | 5 % → 0 % | 18.2 px | 0.65 | 0.08 | 54 |
| fast wave | 6 % → 1 % | 7.3 px | 0.65 | 0.08 | 176 |
| slow wave | 7 % → 0 % | 8.1 px | 0.65 | 0.06 | 362 |
| spiral | 7 % → 0 % | 4.6 px | 0.65 | 0.07 | 244 |
| loop | 10 % → 0 % | 12.4 px | 0.65 | 0.04 | 134 |
| tilted | 4 % → 3 % | 10.6 px | 0.65 | 0.88 | 70 |
| over the wet one | 9 % → 1 % | 14.5 px | 0.65 | 0.12 | 64 |
| long, no reload | 6 % → 1 % | 2.9 px | 0.65 | 0.14 | 348 | quarters: 0.12 → 0.00 → 0.00 → 0.00

Numbers say: light vs heavy: width 14.0 → 18.6 px, dark 0.65 → 0.65.

## Wax Crayon
Wax · 8 px · 9.4 s

![Wax Crayon](Wax-Crayon.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 1 % → 1 % | 2.5 px | 0.71 | 1.00 | 21 |
| heavy line | 1 % → 1 % | 3.9 px | 0.69 | 1.00 | 22 |
| pressure swell | 1 % → 1 % | 3.3 px | 0.70 | 1.00 | 12 |
| fast wave | 3 % → 3 % | 3.5 px | 0.69 | 1.00 | 41 |
| slow wave | 3 % → 3 % | 3.4 px | 0.70 | 1.00 | 42 |
| spiral | 5 % → 5 % | 3.3 px | 0.70 | 1.00 | 86 |
| loop | 3 % → 3 % | 3.3 px | 0.70 | 1.00 | 49 |
| tilted | 2 % → 2 % | 5.6 px | 0.68 | 1.00 | 32 |
| over the wet one | 3 % → 3 % | 3.6 px | 0.68 | 1.00 | 23 |
| long, no reload | 7 % → 7 % | 3.3 px | 0.70 | 1.00 | 109 | quarters: 0.06 → 0.06 → 0.06 → 0.06

Numbers say: light vs heavy: width 2.5 → 3.9 px, dark 0.71 → 0.69; the long stroke does not run out of paint.

## Oil Pastel
Wax · 12 px · 9.5 s

![Oil Pastel](Oil-Pastel.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 1 % → 1 % | 4.0 px | 0.68 | 1.00 | 20 |
| heavy line | 2 % → 2 % | 6.5 px | 0.68 | 1.00 | 31 |
| pressure swell | 2 % → 2 % | 5.7 px | 0.69 | 1.00 | 19 |
| fast wave | 5 % → 5 % | 5.7 px | 0.68 | 1.00 | 74 |
| slow wave | 5 % → 5 % | 5.5 px | 0.68 | 1.00 | 78 |
| spiral | 8 % → 8 % | 5.5 px | 0.68 | 1.00 | 114 |
| loop | 4 % → 4 % | 5.6 px | 0.68 | 1.00 | 128 |
| tilted | 2 % → 2 % | 6.8 px | 0.68 | 1.00 | 41 |
| over the wet one | 5 % → 5 % | 5.8 px | 0.68 | 1.00 | 25 |
| long, no reload | 13 % → 13 % | 5.6 px | 0.68 | 1.00 | 154 | quarters: 0.10 → 0.09 → 0.10 → 0.10

Numbers say: light vs heavy: width 4.0 → 6.5 px, dark 0.68 → 0.68; the long stroke does not run out of paint.

## Charcoal
Charcoal · 5 px · 9.6 s

![Charcoal](Charcoal.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 1 % → 1 % | 2.0 px | 0.74 | 1.00 | 11 |
| heavy line | 1 % → 1 % | 3.0 px | 0.74 | 1.00 | 11 |
| pressure swell | 1 % → 1 % | 2.7 px | 0.74 | 1.00 | 8 |
| fast wave | 2 % → 2 % | 2.7 px | 0.73 | 1.00 | 32 |
| slow wave | 2 % → 2 % | 2.6 px | 0.74 | 1.00 | 38 |
| spiral | 4 % → 4 % | 2.5 px | 0.74 | 1.00 | 65 |
| loop | 2 % → 2 % | 2.6 px | 0.74 | 1.00 | 30 |
| tilted | 2 % → 2 % | 4.3 px | 0.72 | 1.00 | 25 |
| over the wet one | 2 % → 2 % | 2.4 px | 0.72 | 1.00 | 18 |
| long, no reload | 6 % → 6 % | 2.7 px | 0.73 | 1.00 | 100 | quarters: 0.05 → 0.05 → 0.05 → 0.05

Numbers say: light vs heavy: width 2.0 → 3.0 px, dark 0.74 → 0.74; the long stroke does not run out of paint.

## Impasto
Heavy acrylic · 22 px · 16.7 s

![Impasto](Impasto.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 8 % → 8 % | 24.1 px | 0.71 | 0.93 | 47 |
| heavy line | 10 % → 9 % | 28.8 px | 0.70 | 0.94 | 139 |
| pressure swell | 7 % → 7 % | 28.1 px | 0.72 | 0.94 | 65 |
| fast wave | 20 % → 13 % | 23.5 px | 0.71 | 0.64 | 205 |
| slow wave | 21 % → 14 % | 24.5 px | 0.71 | 0.66 | 342 |
| spiral | 30 % → 14 % | 20.0 px | 0.71 | 0.46 | 333 |
| loop | 18 % → 14 % | 23.9 px | 0.71 | 0.77 | 151 |
| tilted | 8 % → 8 % | 21.8 px | 0.70 | 1.00 | 76 |
| over the wet one | 17 % → 15 % | 25.4 px | 0.70 | 0.91 | 67 |
| long, no reload | 34 % → 14 % | 15.2 px | 0.71 | 0.41 | 382 | quarters: 0.38 → 0.21 → 0.10 → 0.03

Numbers say: light vs heavy: width 24.1 → 28.8 px, dark 0.71 → 0.70.

## Oil Round
Oil · 18 px · 18.3 s

![Oil Round](Oil-Round.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 2 % → 2 % | 7.2 px | 0.75 | 1.00 | 36 |
| heavy line | 7 % → 7 % | 19.3 px | 0.73 | 1.00 | 74 |
| pressure swell | 4 % → 4 % | 13.7 px | 0.72 | 1.00 | 42 |
| fast wave | 11 % → 11 % | 12.7 px | 0.65 | 1.00 | 180 |
| slow wave | 8 % → 8 % | 9.0 px | 0.57 | 1.00 | 293 |
| spiral | 10 % → 10 % | 6.6 px | 0.50 | 1.00 | 361 |
| loop | 5 % → 5 % | 7.1 px | 0.45 | 1.00 | 122 |
| tilted | 4 % → 4 % | 10.1 px | 0.52 | 1.00 | 90 |
| over the wet one | 6 % → 6 % | 7.4 px | 0.52 | 1.00 | 74 |
| long, no reload | 15 % → 15 % | 6.8 px | 0.42 | 1.00 | 481 | quarters: 0.08 → 0.08 → 0.07 → 0.06

Numbers say: light vs heavy: width 7.2 → 19.3 px, dark 0.75 → 0.73.

## Palette Knife
Oil · 20 px · 17.7 s

![Palette Knife](Palette-Knife.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 8 % → 8 % | 21.9 px | 0.67 | 1.00 | 13 |
| heavy line | 8 % → 8 % | 22.5 px | 0.73 | 1.00 | 19 |
| pressure swell | 6 % → 6 % | 22.4 px | 0.74 | 1.00 | 11 |
| fast wave | 17 % → 17 % | 19.3 px | 0.49 | 1.00 | 39 |
| slow wave | 17 % → 17 % | 19.9 px | 0.43 | 1.00 | 64 |
| spiral | 18 % → 18 % | 11.7 px | 0.45 | 1.00 | 70 |
| loop | 16 % → 16 % | 21.0 px | 0.58 | 1.00 | 34 |
| tilted | 5 % → 5 % | 15.0 px | 0.72 | 1.00 | 13 |
| over the wet one | 13 % → 13 % | 21.0 px | 0.72 | 1.00 | 17 |
| long, no reload | 17 % → 17 % | 7.5 px | 0.47 | 1.00 | 124 | quarters: 0.29 → 0.05 → 0.00 → 0.00

Numbers say: light vs heavy: width 21.9 → 22.5 px, dark 0.67 → 0.73; pressure barely changes the width.

## Water
Watercolor · 20 px · 32.0 s · over bands of wet oil paint and oil pastel in turn (it works on paint already there: look at what it does to the bands; covered counts the bands too)

![Water](Water.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 25 % → 27 % | 73.8 px | 0.80 | 1.06 | 25 |
| heavy line | 24 % → 25 % | 69.8 px | 0.81 | 1.04 | 55 |
| pressure swell | 24 % → 25 % | 89.6 px | 0.81 | 1.03 | 31 |
| fast wave | 24 % → 26 % | 27.7 px | 0.81 | 1.07 | 105 |
| slow wave | 24 % → 25 % | 27.7 px | 0.81 | 1.06 | 143 |
| spiral | 24 % → 26 % | 15.9 px | 0.81 | 1.07 | 165 |
| loop | 24 % → 25 % | 31.1 px | 0.81 | 1.03 | 90 |
| tilted | 24 % → 24 % | 67.0 px | 0.81 | 1.00 | 81 |
| over the wet one | 24 % → 25 % | 0.0 px | 0.81 | 1.06 | 69 |
| long, no reload | 24 % → 26 % | 10.7 px | 0.81 | 1.08 | 324 | quarters: 0.21 → 0.27 → 0.18 → 0.27

Numbers say: light vs heavy: width 73.8 → 69.8 px, dark 0.80 → 0.81; pressure barely changes the width; the long stroke does not run out of paint.

## Blender
Pastel · 16 px · 19.1 s · over bands of wet oil paint and oil pastel in turn (it works on paint already there: look at what it does to the bands; covered counts the bands too)

![Blender](Blender.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 24 % → 24 % | 70.7 px | 0.81 | 1.00 | 22 |
| heavy line | 25 % → 25 % | 72.1 px | 0.80 | 1.00 | 35 |
| pressure swell | 24 % → 24 % | 91.3 px | 0.81 | 1.00 | 23 |
| fast wave | 26 % → 26 % | 30.0 px | 0.79 | 1.00 | 74 |
| slow wave | 26 % → 26 % | 29.9 px | 0.80 | 1.00 | 86 |
| spiral | 28 % → 28 % | 18.7 px | 0.77 | 1.00 | 120 |
| loop | 25 % → 25 % | 32.9 px | 0.80 | 1.00 | 67 |
| tilted | 25 % → 25 % | 70.1 px | 0.79 | 1.00 | 43 |
| over the wet one | 26 % → 26 % | 1.8 px | 0.79 | 1.00 | 31 |
| long, no reload | 30 % → 30 % | 13.7 px | 0.76 | 1.00 | 197 | quarters: 0.20 → 0.28 → 0.23 → 0.30

Numbers say: light vs heavy: width 70.7 → 72.1 px, dark 0.81 → 0.80; pressure barely changes the width; the long stroke does not run out of paint.

## Eraser
Eraser · 16 px · 19.1 s · over bands of wet oil paint and oil pastel in turn (it works on paint already there: look at what it does to the bands; covered counts the bands too)

![Eraser](Eraser.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 24 % → 24 % | 69.5 px | 0.82 | 1.00 | 24 |
| heavy line | 23 % → 23 % | 67.9 px | 0.82 | 1.00 | 34 |
| pressure swell | 23 % → 23 % | 87.3 px | 0.82 | 1.00 | 23 |
| fast wave | 22 % → 22 % | 25.7 px | 0.82 | 1.00 | 75 |
| slow wave | 22 % → 22 % | 25.7 px | 0.82 | 1.00 | 88 |
| spiral | 22 % → 22 % | 14.4 px | 0.82 | 1.00 | 120 |
| loop | 22 % → 22 % | 28.6 px | 0.82 | 1.00 | 71 |
| tilted | 23 % → 23 % | 65.1 px | 0.82 | 1.00 | 42 |
| over the wet one | 23 % → 23 % | 0.0 px | 0.82 | 1.00 | 32 |
| long, no reload | 20 % → 20 % | 8.9 px | 0.82 | 1.00 | 194 | quarters: 0.15 → 0.20 → 0.15 → 0.20

Numbers say: light vs heavy: width 69.5 → 67.9 px, dark 0.82 → 0.82; pressure barely changes the width; the long stroke does not run out of paint.

## Fan
Gouache · 30 px · 26.8 s

![Fan](Fan.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 9 % → 3 % | 25.7 px | 0.63 | 0.37 | 28 |
| heavy line | 11 % → 4 % | 31.0 px | 0.63 | 0.39 | 54 |
| pressure swell | 8 % → 5 % | 31.7 px | 0.63 | 0.55 | 31 |
| fast wave | 18 % → 5 % | 20.3 px | 0.63 | 0.26 | 101 |
| slow wave | 18 % → 5 % | 21.1 px | 0.63 | 0.25 | 200 |
| spiral | 24 % → 5 % | 15.8 px | 0.63 | 0.20 | 232 |
| loop | 17 % → 5 % | 22.7 px | 0.63 | 0.29 | 137 |
| tilted | 5 % → 6 % | 15.1 px | 0.63 | 1.05 | 39 |
| over the wet one | 16 % → 8 % | 29.8 px | 0.63 | 0.50 | 41 |
| long, no reload | 23 % → 5 % | 10.1 px | 0.63 | 0.22 | 241 | quarters: 0.29 → 0.07 → 0.01 → 0.00

Numbers say: light vs heavy: width 25.7 → 31.0 px, dark 0.63 → 0.63.

## Sponge
Gouache · 30 px · 26.5 s

![Sponge](Sponge.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 4 % → 0 % | 11.4 px | 0.62 | 0.12 | 35 |
| heavy line | 12 % → 2 % | 35.4 px | 0.62 | 0.14 | 64 |
| pressure swell | 7 % → 2 % | 27.9 px | 0.62 | 0.27 | 40 |
| fast wave | 20 % → 4 % | 23.2 px | 0.62 | 0.19 | 118 |
| slow wave | 21 % → 4 % | 23.7 px | 0.62 | 0.18 | 300 |
| spiral | 28 % → 4 % | 18.3 px | 0.62 | 0.14 | 273 |
| loop | 18 % → 5 % | 23.0 px | 0.62 | 0.29 | 135 |
| tilted | 7 % → 7 % | 18.2 px | 0.62 | 1.04 | 86 |
| over the wet one | 16 % → 6 % | 27.8 px | 0.62 | 0.37 | 50 |
| long, no reload | 29 % → 5 % | 12.9 px | 0.62 | 0.17 | 285 | quarters: 0.29 → 0.13 → 0.07 → 0.04

Numbers say: light vs heavy: width 11.4 → 35.4 px, dark 0.62 → 0.62.

## Ink — sumi brush
Watercolor · 22 px · 28.3 s

![Ink — sumi brush](Ink-sumi-brush.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 8 % → 9 % | 23.9 px | 0.87 | 1.12 | 57 |
| heavy line | 13 % → 13 % | 38.1 px | 0.87 | 1.01 | 73 |
| pressure swell | 9 % → 10 % | 34.5 px | 0.87 | 1.04 | 89 |
| fast wave | 28 % → 28 % | 32.6 px | 0.85 | 1.00 | 200 |
| slow wave | 26 % → 26 % | 29.8 px | 0.86 | 1.02 | 286 |
| spiral | 39 % → 38 % | 25.5 px | 0.81 | 0.99 | 268 |
| loop | 22 % → 22 % | 28.6 px | 0.87 | 1.02 | 135 |
| tilted | 9 % → 9 % | 25.4 px | 0.87 | 1.00 | 72 |
| over the wet one | 20 % → 21 % | 30.6 px | 0.87 | 1.03 | 64 |
| long, no reload | 45 % → 43 % | 20.3 px | 0.76 | 0.95 | 393 | quarters: 0.56 → 0.45 → 0.30 → 0.20

Numbers say: light vs heavy: width 23.9 → 38.1 px, dark 0.87 → 0.87.

## Ink — wash
Watercolor · 40 px · 33.7 s

![Ink — wash](Ink-wash.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 13 % → 13 % | 37.6 px | 0.77 | 1.01 | 81 |
| heavy line | 19 % → 19 % | 55.6 px | 0.72 | 1.00 | 99 |
| pressure swell | 13 % → 13 % | 48.6 px | 0.76 | 1.01 | 58 |
| fast wave | 42 % → 42 % | 48.3 px | 0.69 | 1.01 | 261 |
| slow wave | 40 % → 40 % | 45.8 px | 0.75 | 1.01 | 407 |
| spiral | 61 % → 62 % | 40.3 px | 0.69 | 1.01 | 329 |
| loop | 34 % → 34 % | 44.0 px | 0.75 | 1.00 | 172 |
| tilted | 15 % → 15 % | 41.2 px | 0.76 | 1.00 | 105 |
| over the wet one | 30 % → 31 % | 43.4 px | 0.76 | 1.02 | 80 |
| long, no reload | 74 % → 75 % | 33.1 px | 0.64 | 1.02 | 496 | quarters: 0.68 → 0.60 → 0.47 → 0.33

Numbers say: light vs heavy: width 37.6 → 55.6 px, dark 0.77 → 0.72.

## Ink — dry brush
Ink · 30 px · 23.7 s

![Ink — dry brush](Ink-dry-brush.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 9 % → 7 % | 25.4 px | 0.81 | 0.78 | 102 |
| heavy line | 10 % → 8 % | 29.9 px | 0.79 | 0.75 | 142 |
| pressure swell | 7 % → 6 % | 28.1 px | 0.81 | 0.84 | 76 |
| fast wave | 21 % → 8 % | 24.3 px | 0.79 | 0.40 | 286 |
| slow wave | 17 % → 7 % | 20.2 px | 0.79 | 0.39 | 464 |
| spiral | 23 % → 8 % | 15.4 px | 0.78 | 0.34 | 366 |
| loop | 19 % → 8 % | 24.4 px | 0.78 | 0.44 | 198 |
| tilted | 8 % → 8 % | 22.7 px | 0.78 | 1.02 | 118 |
| over the wet one | 17 % → 14 % | 25.9 px | 0.78 | 0.81 | 95 |
| long, no reload | 20 % → 8 % | 9.0 px | 0.79 | 0.42 | 528 | quarters: 0.32 → 0.02 → 0.00 → 0.00

Numbers say: light vs heavy: width 25.4 → 29.9 px, dark 0.81 → 0.79.

## Ink — nib
Watercolor · 5 px · 22.1 s

![Ink — nib](Ink-nib.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 2 % → 5 % | 5.5 px | 0.89 | 2.46 | 43 |
| heavy line | 2 % → 5 % | 6.4 px | 0.89 | 2.33 | 26 |
| pressure swell | 2 % → 4 % | 6.2 px | 0.89 | 2.52 | 20 |
| fast wave | 5 % → 8 % | 6.0 px | 0.89 | 1.62 | 64 |
| slow wave | 5 % → 8 % | 5.7 px | 0.89 | 1.69 | 67 |
| spiral | 8 % → 11 % | 5.0 px | 0.88 | 1.40 | 110 |
| loop | 4 % → 8 % | 5.7 px | 0.89 | 1.73 | 60 |
| tilted | 4 % → 4 % | 10.3 px | 0.89 | 1.02 | 55 |
| over the wet one | 6 % → 9 % | 6.1 px | 0.89 | 1.61 | 44 |
| long, no reload | 10 % → 12 % | 4.3 px | 0.86 | 1.29 | 264 | quarters: 0.24 → 0.11 → 0.07 → 0.05

Numbers say: light vs heavy: width 5.5 → 6.4 px, dark 0.89 → 0.89; wet paint spreads well beyond the stroke.

## 0.45 · Dry brush
Gouache · 34 px · 24.0 s

![0.45 · Dry brush](0-45-Dry-brush.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 8 % → 2 % | 23.2 px | 0.68 | 0.30 | 125 |
| heavy line | 8 % → 3 % | 24.3 px | 0.68 | 0.32 | 114 |
| pressure swell | 7 % → 3 % | 25.6 px | 0.68 | 0.42 | 82 |
| fast wave | 14 % → 3 % | 15.7 px | 0.68 | 0.22 | 276 |
| slow wave | 16 % → 3 % | 18.7 px | 0.68 | 0.20 | 640 |
| spiral | 20 % → 3 % | 13.4 px | 0.68 | 0.15 | 466 |
| loop | 14 % → 4 % | 18.3 px | 0.68 | 0.26 | 246 |
| tilted | 7 % → 7 % | 18.9 px | 0.68 | 1.01 | 131 |
| over the wet one | 15 % → 6 % | 23.1 px | 0.68 | 0.43 | 119 |
| long, no reload | 21 % → 4 % | 9.4 px | 0.68 | 0.18 | 679 | quarters: 0.28 → 0.14 → 0.07 → 0.03

Numbers say: light vs heavy: width 23.2 → 24.3 px, dark 0.68 → 0.68; pressure barely changes the width.

## Dry pastel
Pastel · 26 px · 10.0 s

![Dry pastel](Dry-pastel.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 3 % → 3 % | 8.3 px | 0.38 | 1.00 | 30 |
| heavy line | 5 % → 5 % | 13.2 px | 0.39 | 1.00 | 49 |
| pressure swell | 3 % → 3 % | 11.7 px | 0.38 | 1.00 | 34 |
| fast wave | 10 % → 10 % | 11.9 px | 0.39 | 1.00 | 114 |
| slow wave | 10 % → 10 % | 11.3 px | 0.39 | 1.00 | 152 |
| spiral | 15 % → 15 % | 9.6 px | 0.39 | 1.00 | 204 |
| loop | 7 % → 7 % | 9.4 px | 0.39 | 1.00 | 75 |
| tilted | 3 % → 3 % | 8.3 px | 0.38 | 1.00 | 41 |
| over the wet one | 7 % → 7 % | 11.1 px | 0.38 | 1.00 | 34 |
| long, no reload | 18 % → 18 % | 8.2 px | 0.39 | 1.00 | 208 | quarters: 0.08 → 0.08 → 0.08 → 0.07

Numbers say: light vs heavy: width 8.3 → 13.2 px, dark 0.38 → 0.39; the long stroke does not run out of paint.

## 0.45 · Charcoal
Charcoal · 18 px · 9.9 s

![0.45 · Charcoal](0-45-Charcoal.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 2 % → 2 % | 6.5 px | 0.80 | 1.00 | 17 |
| heavy line | 3 % → 3 % | 9.2 px | 0.80 | 1.00 | 17 |
| pressure swell | 2 % → 2 % | 8.8 px | 0.80 | 1.00 | 15 |
| fast wave | 7 % → 7 % | 8.5 px | 0.80 | 1.00 | 51 |
| slow wave | 7 % → 7 % | 8.0 px | 0.80 | 1.00 | 58 |
| spiral | 12 % → 12 % | 7.9 px | 0.80 | 1.00 | 93 |
| loop | 6 % → 6 % | 8.1 px | 0.80 | 1.00 | 36 |
| tilted | 3 % → 3 % | 7.5 px | 0.80 | 1.00 | 26 |
| over the wet one | 6 % → 6 % | 7.9 px | 0.80 | 1.00 | 17 |
| long, no reload | 17 % → 17 % | 7.8 px | 0.80 | 1.00 | 106 | quarters: 0.15 → 0.16 → 0.15 → 0.16

Numbers say: light vs heavy: width 6.5 → 9.2 px, dark 0.80 → 0.80; the long stroke does not run out of paint.

## Watercolour — wash
Watercolor · 50 px · 35.4 s

![Watercolour — wash](Watercolour-wash.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 16 % → 16 % | 45.5 px | 0.22 | 1.00 | 92 |
| heavy line | 22 % → 22 % | 64.9 px | 0.19 | 1.00 | 117 |
| pressure swell | 15 % → 15 % | 56.1 px | 0.22 | 1.01 | 81 |
| fast wave | 48 % → 49 % | 55.6 px | 0.19 | 1.01 | 277 |
| slow wave | 46 % → 46 % | 53.3 px | 0.24 | 1.00 | 574 |
| spiral | 66 % → 66 % | 43.7 px | 0.21 | 1.00 | 481 |
| loop | 40 % → 40 % | 51.4 px | 0.22 | 1.00 | 235 |
| tilted | 18 % → 18 % | 49.7 px | 0.23 | 1.00 | 164 |
| over the wet one | 36 % → 36 % | 49.6 px | 0.23 | 1.01 | 106 |
| long, no reload | 84 % → 84 % | 37.7 px | 0.20 | 1.00 | 680 | quarters: 0.24 → 0.20 → 0.16 → 0.12

Numbers say: light vs heavy: width 45.5 → 64.9 px, dark 0.22 → 0.19.

## Watercolour — wet-in-wet
Watercolor · 44 px · 43.4 s

![Watercolour — wet-in-wet](Watercolour-wet-in-wet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 13 % → 19 % | 38.4 px | 0.34 | 1.43 | 80 |
| heavy line | 19 % → 20 % | 54.6 px | 0.36 | 1.05 | 97 |
| pressure swell | 12 % → 15 % | 46.5 px | 0.37 | 1.22 | 67 |
| fast wave | 41 % → 45 % | 47.7 px | 0.35 | 1.09 | 230 |
| slow wave | 40 % → 45 % | 46.2 px | 0.42 | 1.12 | 452 |
| spiral | 63 % → 67 % | 41.5 px | 0.38 | 1.06 | 389 |
| loop | 34 % → 37 % | 44.4 px | 0.40 | 1.09 | 188 |
| tilted | 15 % → 16 % | 41.5 px | 0.38 | 1.06 | 130 |
| over the wet one | 31 % → 37 % | 43.9 px | 0.38 | 1.21 | 84 |
| long, no reload | 78 % → 84 % | 34.8 px | 0.37 | 1.08 | 859 | quarters: 0.39 → 0.37 → 0.32 → 0.26

Numbers say: light vs heavy: width 38.4 → 54.6 px, dark 0.34 → 0.36.

## Watercolour — glaze
Watercolor · 38 px · 39.2 s

![Watercolour — glaze](Watercolour-glaze.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 13 % → 13 % | 36.6 px | 0.07 | 1.01 | 72 |
| heavy line | 19 % → 19 % | 55.4 px | 0.07 | 1.00 | 84 |
| pressure swell | 13 % → 13 % | 47.0 px | 0.07 | 1.01 | 57 |
| fast wave | 40 % → 40 % | 45.6 px | 0.07 | 1.01 | 189 |
| slow wave | 37 % → 37 % | 42.8 px | 0.07 | 1.01 | 318 |
| spiral | 59 % → 60 % | 38.8 px | 0.06 | 1.01 | 522 |
| loop | 33 % → 33 % | 42.6 px | 0.07 | 1.00 | 174 |
| tilted | 14 % → 14 % | 40.1 px | 0.07 | 1.00 | 108 |
| over the wet one | 30 % → 30 % | 42.3 px | 0.07 | 1.01 | 76 |
| long, no reload | 69 % → 70 % | 30.9 px | 0.06 | 1.01 | 467 | quarters: 0.06 → 0.05 → 0.03 → 0.02

Numbers say: light vs heavy: width 36.6 → 55.4 px, dark 0.07 → 0.07.

## Watercolour — granulating
Watercolor · 44 px · 55.9 s

![Watercolour — granulating](Watercolour-granulating.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 14 % → 14 % | 41.4 px | 0.35 | 1.00 | 128 |
| heavy line | 21 % → 21 % | 60.4 px | 0.31 | 1.00 | 146 |
| pressure swell | 14 % → 14 % | 52.2 px | 0.34 | 1.01 | 103 |
| fast wave | 45 % → 45 % | 51.7 px | 0.29 | 1.01 | 321 |
| slow wave | 42 % → 42 % | 48.2 px | 0.35 | 1.01 | 809 |
| spiral | 62 % → 63 % | 41.0 px | 0.30 | 1.01 | 655 |
| loop | 37 % → 37 % | 47.6 px | 0.33 | 1.00 | 453 |
| tilted | 16 % → 16 % | 45.5 px | 0.35 | 1.00 | 391 |
| over the wet one | 33 % → 33 % | 46.2 px | 0.35 | 1.01 | 240 |
| long, no reload | 75 % → 76 % | 33.6 px | 0.29 | 1.01 | 964 | quarters: 0.34 → 0.26 → 0.20 → 0.14

Numbers say: light vs heavy: width 41.4 → 60.4 px, dark 0.35 → 0.31.

## Watercolour — dry brush
Watercolor · 36 px · 44.1 s

![Watercolour — dry brush](Watercolour-dry-brush.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 10 % → 10 % | 28.0 px | 0.17 | 1.01 | 155 |
| heavy line | 14 % → 13 % | 40.1 px | 0.16 | 0.93 | 179 |
| pressure swell | 11 % → 11 % | 40.5 px | 0.16 | 0.98 | 202 |
| fast wave | 27 % → 20 % | 30.8 px | 0.13 | 0.74 | 751 |
| slow wave | 24 % → 17 % | 28.1 px | 0.14 | 0.71 | 884 |
| spiral | 34 % → 20 % | 22.4 px | 0.13 | 0.57 | 842 |
| loop | 21 % → 18 % | 27.2 px | 0.14 | 0.86 | 429 |
| tilted | 10 % → 10 % | 28.6 px | 0.16 | 1.00 | 201 |
| over the wet one | 22 % → 20 % | 31.4 px | 0.16 | 0.95 | 164 |
| long, no reload | 36 % → 19 % | 16.1 px | 0.14 | 0.54 | 1004 | quarters: 0.09 → 0.03 → 0.01 → 0.00

Numbers say: light vs heavy: width 28.0 → 40.1 px, dark 0.17 → 0.16.

## Gouache
Gouache · 30 px · 41.6 s

![Gouache](Gouache.png)

A light paint: laid on a grey sheet (on white it cannot be seen); **dark** = how far it is from the grey either way.

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 8 % → 6 % | 24.7 px | 0.28 | 0.66 | 167 |
| heavy line | 14 % → 7 % | 39.8 px | 0.28 | 0.49 | 145 |
| pressure swell | 10 % → 6 % | 38.8 px | 0.28 | 0.62 | 158 |
| fast wave | 28 % → 8 % | 32.8 px | 0.28 | 0.27 | 523 |
| slow wave | 27 % → 8 % | 31.6 px | 0.28 | 0.30 | 639 |
| spiral | 38 % → 8 % | 25.0 px | 0.28 | 0.22 | 558 |
| loop | 22 % → 8 % | 28.8 px | 0.28 | 0.36 | 317 |
| tilted | 9 % → 9 % | 24.6 px | 0.27 | 1.00 | 196 |
| over the wet one | 20 % → 13 % | 31.0 px | 0.27 | 0.67 | 141 |
| long, no reload | 40 % → 10 % | 17.9 px | 0.27 | 0.24 | 1124 | quarters: 0.01 → 0.01 → 0.02 → 0.02

Numbers say: light vs heavy: width 24.7 → 39.8 px, dark 0.28 → 0.28; the long stroke does not run out of paint.

## Oil — alla prima
Oil · 30 px · 28.2 s

![Oil — alla prima](Oil-alla-prima.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 10 % → 10 % | 28.5 px | 0.51 | 1.00 | 170 |
| heavy line | 11 % → 11 % | 31.2 px | 0.51 | 1.00 | 136 |
| pressure swell | 8 % → 8 % | 30.9 px | 0.53 | 1.00 | 162 |
| fast wave | 26 % → 26 % | 29.5 px | 0.52 | 1.00 | 576 |
| slow wave | 26 % → 26 % | 30.2 px | 0.52 | 1.00 | 627 |
| spiral | 41 % → 41 % | 27.0 px | 0.51 | 1.00 | 557 |
| loop | 22 % → 22 % | 28.0 px | 0.52 | 1.00 | 234 |
| tilted | 11 % → 11 % | 31.9 px | 0.52 | 1.00 | 161 |
| over the wet one | 21 % → 21 % | 27.5 px | 0.52 | 1.00 | 109 |
| long, no reload | 50 % → 50 % | 22.5 px | 0.50 | 1.00 | 758 | quarters: 0.33 → 0.30 → 0.26 → 0.23

Numbers say: light vs heavy: width 28.5 → 31.2 px, dark 0.51 → 0.51; pressure barely changes the width.

## Oil — impasto
Oil · 34 px · 30.8 s

![Oil — impasto](Oil-impasto.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 12 % → 12 % | 34.5 px | 0.23 | 1.00 | 178 |
| heavy line | 13 % → 13 % | 37.4 px | 0.23 | 1.00 | 290 |
| pressure swell | 10 % → 10 % | 37.1 px | 0.25 | 1.00 | 251 |
| fast wave | 28 % → 28 % | 31.9 px | 0.23 | 1.00 | 511 |
| slow wave | 30 % → 30 % | 34.3 px | 0.23 | 1.00 | 673 |
| spiral | 46 % → 46 % | 30.3 px | 0.22 | 1.00 | 639 |
| loop | 25 % → 25 % | 32.2 px | 0.24 | 1.00 | 316 |
| tilted | 12 % → 12 % | 33.4 px | 0.24 | 1.00 | 186 |
| over the wet one | 24 % → 24 % | 32.6 px | 0.24 | 1.00 | 142 |
| long, no reload | 51 % → 51 % | 22.7 px | 0.22 | 1.00 | 944 | quarters: 0.17 → 0.13 → 0.10 → 0.08

Numbers say: light vs heavy: width 34.5 → 37.4 px, dark 0.23 → 0.23; pressure barely changes the width.

## Oil — glaze
Oil · 40 px · 26.9 s

![Oil — glaze](Oil-glaze.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 9 % → 9 % | 27.0 px | 0.50 | 1.00 | 178 |
| heavy line | 13 % → 13 % | 38.2 px | 0.49 | 1.00 | 237 |
| pressure swell | 10 % → 10 % | 36.6 px | 0.50 | 1.00 | 138 |
| fast wave | 29 % → 29 % | 33.5 px | 0.49 | 1.00 | 422 |
| slow wave | 30 % → 30 % | 34.5 px | 0.50 | 1.00 | 694 |
| spiral | 46 % → 46 % | 30.0 px | 0.49 | 1.00 | 698 |
| loop | 24 % → 24 % | 31.4 px | 0.50 | 1.00 | 318 |
| tilted | 11 % → 11 % | 30.3 px | 0.50 | 1.00 | 216 |
| over the wet one | 22 % → 22 % | 32.5 px | 0.50 | 1.00 | 139 |
| long, no reload | 52 % → 52 % | 23.5 px | 0.49 | 1.00 | 931 | quarters: 0.34 → 0.30 → 0.27 → 0.22

Numbers say: light vs heavy: width 27.0 → 38.2 px, dark 0.50 → 0.49.

## Oil — scumble
Oil · 36 px · 25.5 s

![Oil — scumble](Oil-scumble.png)

A light paint: laid on a grey sheet (on white it cannot be seen); **dark** = how far it is from the grey either way.

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 10 % → 10 % | 27.7 px | 0.28 | 1.00 | 407 |
| heavy line | 9 % → 9 % | 27.2 px | 0.27 | 1.00 | 318 |
| pressure swell | 9 % → 9 % | 32.2 px | 0.26 | 1.00 | 177 |
| fast wave | 18 % → 18 % | 21.0 px | 0.22 | 1.00 | 494 |
| slow wave | 22 % → 22 % | 25.5 px | 0.21 | 1.00 | 790 |
| spiral | 32 % → 32 % | 20.9 px | 0.17 | 1.00 | 741 |
| loop | 18 % → 18 % | 23.1 px | 0.23 | 1.00 | 377 |
| tilted | 10 % → 10 % | 27.2 px | 0.25 | 1.00 | 247 |
| over the wet one | 20 % → 20 % | 27.5 px | 0.25 | 1.00 | 204 |
| long, no reload | 35 % → 35 % | 15.5 px | 0.15 | 1.00 | 981 | quarters: 0.00 → 0.00 → 0.00 → 0.00

Numbers say: light vs heavy: width 27.7 → 27.2 px, dark 0.28 → 0.27; pressure barely changes the width.

## Acrylic — heavy body
Heavy acrylic · 30 px · 19.8 s

![Acrylic — heavy body](Acrylic-heavy-body.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 10 % → 9 % | 30.0 px | 0.51 | 0.92 | 137 |
| heavy line | 11 % → 10 % | 32.1 px | 0.51 | 0.93 | 161 |
| pressure swell | 9 % → 8 % | 31.9 px | 0.53 | 0.94 | 107 |
| fast wave | 23 % → 15 % | 27.1 px | 0.51 | 0.62 | 370 |
| slow wave | 24 % → 16 % | 28.1 px | 0.51 | 0.65 | 611 |
| spiral | 36 % → 15 % | 23.5 px | 0.51 | 0.42 | 452 |
| loop | 21 % → 16 % | 27.1 px | 0.51 | 0.76 | 246 |
| tilted | 9 % → 9 % | 26.2 px | 0.51 | 1.00 | 129 |
| over the wet one | 20 % → 18 % | 28.4 px | 0.51 | 0.90 | 143 |
| long, no reload | 39 % → 15 % | 17.4 px | 0.51 | 0.40 | 722 | quarters: 0.30 → 0.19 → 0.11 → 0.04

Numbers say: light vs heavy: width 30.0 → 32.1 px, dark 0.51 → 0.51; pressure barely changes the width.

## Acrylic — fluid
Watercolor · 36 px · 41.8 s

![Acrylic — fluid](Acrylic-fluid.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 12 % → 12 % | 34.8 px | 0.24 | 1.01 | 83 |
| heavy line | 18 % → 18 % | 52.6 px | 0.21 | 0.99 | 111 |
| pressure swell | 12 % → 12 % | 45.4 px | 0.23 | 1.00 | 74 |
| fast wave | 38 % → 38 % | 44.1 px | 0.19 | 0.98 | 227 |
| slow wave | 35 % → 35 % | 40.5 px | 0.22 | 1.00 | 477 |
| spiral | 55 % → 53 % | 36.0 px | 0.19 | 0.98 | 429 |
| loop | 31 % → 31 % | 40.2 px | 0.21 | 1.00 | 242 |
| tilted | 12 % → 12 % | 34.2 px | 0.24 | 1.00 | 145 |
| over the wet one | 27 % → 28 % | 42.3 px | 0.24 | 1.01 | 100 |
| long, no reload | 61 % → 58 % | 27.6 px | 0.19 | 0.95 | 879 | quarters: 0.20 → 0.14 → 0.09 → 0.06

Numbers say: light vs heavy: width 34.8 → 52.6 px, dark 0.24 → 0.21.

## Acrylic — palette knife
Heavy acrylic · 42 px · 22.3 s

![Acrylic — palette knife](Acrylic-palette-knife.png)

A light paint: laid on a grey sheet (on white it cannot be seen); **dark** = how far it is from the grey either way.

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 16 % → 15 % | 45.6 px | 0.39 | 0.98 | 54 |
| heavy line | 16 % → 15 % | 45.8 px | 0.40 | 0.98 | 39 |
| pressure swell | 12 % → 12 % | 45.6 px | 0.42 | 0.99 | 16 |
| fast wave | 37 % → 20 % | 42.6 px | 0.37 | 0.55 | 104 |
| slow wave | 37 % → 21 % | 43.2 px | 0.37 | 0.57 | 151 |
| spiral | 50 % → 18 % | 32.8 px | 0.37 | 0.37 | 188 |
| loop | 32 % → 24 % | 41.2 px | 0.36 | 0.75 | 113 |
| tilted | 13 % → 13 % | 35.1 px | 0.39 | 1.00 | 53 |
| over the wet one | 27 % → 27 % | 41.3 px | 0.39 | 0.97 | 59 |
| long, no reload | 57 % → 21 % | 25.6 px | 0.35 | 0.36 | 276 | quarters: 0.00 → 0.00 → 0.00 → 0.01

Numbers say: light vs heavy: width 45.6 → 45.8 px, dark 0.39 → 0.40; pressure barely changes the width; the long stroke does not run out of paint.

## Finger on oil
Oil · 30 px · 17.6 s

![Finger on oil](Finger-on-oil.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 6 % → 6 % | 16.8 px | 0.40 | 1.00 | 103 |
| heavy line | 7 % → 7 % | 21.5 px | 0.39 | 1.00 | 147 |
| pressure swell | 6 % → 6 % | 22.3 px | 0.40 | 1.00 | 84 |
| fast wave | 12 % → 12 % | 13.6 px | 0.37 | 1.00 | 196 |
| slow wave | 17 % → 17 % | 19.5 px | 0.36 | 1.00 | 431 |
| spiral | 22 % → 22 % | 14.3 px | 0.34 | 1.00 | 298 |
| loop | 13 % → 13 % | 16.6 px | 0.37 | 1.00 | 184 |
| tilted | 8 % → 8 % | 21.4 px | 0.39 | 1.00 | 128 |
| over the wet one | 15 % → 15 % | 20.3 px | 0.39 | 1.00 | 64 |
| long, no reload | 22 % → 22 % | 10.0 px | 0.33 | 1.00 | 391 | quarters: 0.14 → 0.08 → 0.06 → 0.04

Numbers say: light vs heavy: width 16.8 → 21.5 px, dark 0.40 → 0.39.

## Palette knife — oil
Oil · 44 px · 25.0 s

![Palette knife — oil](Palette-knife-oil.png)

A light paint: laid on a grey sheet (on white it cannot be seen); **dark** = how far it is from the grey either way.

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 16 % → 16 % | 47.4 px | 0.36 | 1.00 | 50 |
| heavy line | 17 % → 17 % | 48.1 px | 0.39 | 1.00 | 48 |
| pressure swell | 13 % → 13 % | 47.5 px | 0.39 | 1.00 | 18 |
| fast wave | 39 % → 40 % | 45.6 px | 0.35 | 1.01 | 112 |
| slow wave | 40 % → 40 % | 46.1 px | 0.35 | 1.00 | 140 |
| spiral | 63 % → 63 % | 41.3 px | 0.27 | 1.00 | 216 |
| loop | 34 % → 34 % | 43.8 px | 0.36 | 1.00 | 96 |
| tilted | 14 % → 14 % | 38.3 px | 0.38 | 1.00 | 45 |
| over the wet one | 29 % → 29 % | 42.5 px | 0.38 | 1.00 | 43 |
| long, no reload | 75 % → 75 % | 33.4 px | 0.25 | 1.00 | 221 | quarters: 0.00 → 0.00 → 0.00 → 0.00

Numbers say: light vs heavy: width 47.4 → 48.1 px, dark 0.36 → 0.39; pressure barely changes the width; the long stroke does not run out of paint.

## 0.45 · Sponge
Watercolor · 46 px · 48.4 s

![0.45 · Sponge](0-45-Sponge.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 27 % → 18 % | 78.2 px | 0.09 | 0.67 | 76 |
| heavy line | 32 % → 25 % | 91.7 px | 0.09 | 0.78 | 100 |
| pressure swell | 24 % → 17 % | 90.3 px | 0.11 | 0.71 | 56 |
| fast wave | 59 % → 43 % | 68.1 px | 0.10 | 0.73 | 236 |
| slow wave | 59 % → 48 % | 68.5 px | 0.13 | 0.80 | 400 |
| spiral | 75 % → 57 % | 49.3 px | 0.12 | 0.76 | 394 |
| loop | 53 % → 43 % | 68.6 px | 0.11 | 0.81 | 230 |
| tilted | 18 % → 18 % | 49.4 px | 0.15 | 1.00 | 238 |
| over the wet one | 44 % → 37 % | 74.4 px | 0.15 | 0.84 | 150 |
| long, no reload | 89 % → 71 % | 39.9 px | 0.13 | 0.79 | 638 | quarters: 0.13 → 0.12 → 0.10 → 0.07

Numbers say: light vs heavy: width 78.2 → 91.7 px, dark 0.09 → 0.09.

## 0.45 · Eraser
Eraser · 30 px · 30.1 s · over bands of wet oil paint and oil pastel in turn (it works on paint already there: look at what it does to the bands; covered counts the bands too)

![0.45 · Eraser](0-45-Eraser.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 24 % → 24 % | 69.2 px | 0.82 | 1.00 | 62 |
| heavy line | 23 % → 23 % | 67.4 px | 0.81 | 1.00 | 69 |
| pressure swell | 23 % → 23 % | 86.7 px | 0.82 | 1.00 | 45 |
| fast wave | 21 % → 21 % | 24.7 px | 0.81 | 1.00 | 169 |
| slow wave | 20 % → 20 % | 23.5 px | 0.82 | 1.00 | 487 |
| spiral | 20 % → 20 % | 13.5 px | 0.79 | 1.00 | 412 |
| loop | 21 % → 21 % | 27.8 px | 0.80 | 1.00 | 225 |
| tilted | 23 % → 23 % | 64.8 px | 0.81 | 1.00 | 70 |
| over the wet one | 22 % → 22 % | 0.0 px | 0.81 | 1.00 | 78 |
| long, no reload | 17 % → 17 % | 7.5 px | 0.79 | 1.00 | 482 | quarters: 0.13 → 0.16 → 0.13 → 0.17

Numbers say: light vs heavy: width 69.2 → 67.4 px, dark 0.82 → 0.81; pressure barely changes the width; the long stroke does not run out of paint.

## Lift wet paint
Eraser · 30 px · 31.6 s · over bands of wet oil paint and oil pastel in turn (it works on paint already there: look at what it does to the bands; covered counts the bands too)

![Lift wet paint](Lift-wet-paint.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 24 % → 24 % | 70.1 px | 0.82 | 1.00 | 50 |
| heavy line | 24 % → 24 % | 69.8 px | 0.82 | 1.00 | 71 |
| pressure swell | 24 % → 24 % | 89.5 px | 0.82 | 1.00 | 42 |
| fast wave | 24 % → 24 % | 27.7 px | 0.82 | 1.00 | 122 |
| slow wave | 24 % → 24 % | 27.7 px | 0.82 | 1.00 | 228 |
| spiral | 24 % → 24 % | 15.9 px | 0.82 | 1.00 | 224 |
| loop | 24 % → 24 % | 31.1 px | 0.82 | 1.00 | 163 |
| tilted | 24 % → 24 % | 66.8 px | 0.82 | 1.00 | 101 |
| over the wet one | 24 % → 24 % | 0.0 px | 0.82 | 1.00 | 81 |
| long, no reload | 24 % → 24 % | 10.7 px | 0.82 | 1.00 | 484 | quarters: 0.18 → 0.24 → 0.17 → 0.24

Numbers say: light vs heavy: width 70.1 → 69.8 px, dark 0.82 → 0.82; pressure barely changes the width; the long stroke does not run out of paint.

## Sgraffito
Eraser · 10 px · 31.3 s · over bands of wet oil paint and oil pastel in turn (it works on paint already there: look at what it does to the bands; covered counts the bands too)

![Sgraffito](Sgraffito.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 24 % → 24 % | 69.5 px | 0.81 | 1.00 | 14 |
| heavy line | 24 % → 24 % | 69.5 px | 0.82 | 1.00 | 14 |
| pressure swell | 24 % → 24 % | 89.5 px | 0.82 | 1.00 | 7 |
| fast wave | 24 % → 24 % | 27.4 px | 0.82 | 1.00 | 36 |
| slow wave | 24 % → 24 % | 27.4 px | 0.81 | 1.00 | 28 |
| spiral | 24 % → 24 % | 15.7 px | 0.81 | 1.00 | 60 |
| loop | 24 % → 24 % | 30.9 px | 0.82 | 1.00 | 24 |
| tilted | 24 % → 24 % | 66.6 px | 0.82 | 1.00 | 15 |
| over the wet one | 24 % → 24 % | 0.0 px | 0.82 | 1.00 | 12 |
| long, no reload | 24 % → 24 % | 10.6 px | 0.82 | 1.00 | 104 | quarters: 0.17 → 0.24 → 0.17 → 0.24

Numbers say: light vs heavy: width 69.5 → 69.5 px, dark 0.81 → 0.82; pressure barely changes the width; the long stroke does not run out of paint.

## Brush Artist · Refs · #01 Henry Ward peach cloud
Gouache · 44 px · 47.7 s

![Brush Artist · Refs · #01 Henry Ward peach cloud](Brush-Artist-Refs-01-Henry-Ward-peach-cloud.png)

A light paint: laid on a grey sheet (on white it cannot be seen); **dark** = how far it is from the grey either way.

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 5 % → 1 % | 14.2 px | 0.34 | 0.15 | 271 |
| heavy line | 9 % → 5 % | 25.6 px | 0.34 | 0.52 | 280 |
| pressure swell | 7 % → 4 % | 26.4 px | 0.34 | 0.55 | 144 |
| fast wave | 7 % → 2 % | 8.1 px | 0.34 | 0.24 | 560 |
| slow wave | 24 % → 12 % | 27.3 px | 0.34 | 0.50 | 1180 |
| spiral | 27 % → 10 % | 18.0 px | 0.34 | 0.36 | 990 |
| loop | 16 % → 9 % | 21.3 px | 0.34 | 0.53 | 770 |
| tilted | 6 % → 6 % | 16.0 px | 0.34 | 1.01 | 359 |
| over the wet one | 14 % → 9 % | 24.3 px | 0.34 | 0.66 | 223 |
| long, no reload | 30 % → 14 % | 13.5 px | 0.34 | 0.46 | 1306 | quarters: 0.01 → 0.02 → 0.02 → 0.02

Numbers say: light vs heavy: width 14.2 → 25.6 px, dark 0.34 → 0.34; the long stroke does not run out of paint.

## Brush Artist · Refs · #02 Henry Ward cream strokes
Gouache · 46 px · 47.1 s

![Brush Artist · Refs · #02 Henry Ward cream strokes](Brush-Artist-Refs-02-Henry-Ward-cream-strokes.png)

A light paint: laid on a grey sheet (on white it cannot be seen); **dark** = how far it is from the grey either way.

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 5 % → 0 % | 13.8 px | 0.42 | 0.08 | 223 |
| heavy line | 9 % → 3 % | 26.0 px | 0.42 | 0.36 | 244 |
| pressure swell | 7 % → 3 % | 26.6 px | 0.42 | 0.43 | 207 |
| fast wave | 7 % → 1 % | 8.0 px | 0.42 | 0.14 | 734 |
| slow wave | 24 % → 11 % | 27.3 px | 0.41 | 0.44 | 1357 |
| spiral | 27 % → 8 % | 17.9 px | 0.41 | 0.31 | 950 |
| loop | 16 % → 7 % | 21.3 px | 0.41 | 0.45 | 484 |
| tilted | 6 % → 6 % | 15.9 px | 0.42 | 1.02 | 265 |
| over the wet one | 15 % → 9 % | 24.6 px | 0.42 | 0.64 | 189 |
| long, no reload | 30 % → 12 % | 13.3 px | 0.41 | 0.41 | 1305 | quarters: 0.02 → 0.02 → 0.02 → 0.03

Numbers say: light vs heavy: width 13.8 → 26.0 px, dark 0.42 → 0.42; the long stroke does not run out of paint.

## Brush Artist · Refs · #03 Henry Ward navy contours
Heavy acrylic · 22 px · 28.1 s

![Brush Artist · Refs · #03 Henry Ward navy contours](Brush-Artist-Refs-03-Henry-Ward-navy-contours.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 7 % → 5 % | 19.2 px | 0.73 | 0.80 | 224 |
| heavy line | 7 % → 6 % | 21.5 px | 0.73 | 0.83 | 129 |
| pressure swell | 6 % → 5 % | 22.1 px | 0.74 | 0.88 | 110 |
| fast wave | 12 % → 8 % | 14.0 px | 0.73 | 0.64 | 282 |
| slow wave | 17 % → 13 % | 19.5 px | 0.73 | 0.74 | 445 |
| spiral | 22 % → 14 % | 14.6 px | 0.73 | 0.61 | 535 |
| loop | 14 % → 10 % | 17.5 px | 0.73 | 0.74 | 268 |
| tilted | 7 % → 7 % | 18.5 px | 0.73 | 1.00 | 124 |
| over the wet one | 14 % → 11 % | 19.8 px | 0.73 | 0.81 | 95 |
| long, no reload | 25 % → 15 % | 11.3 px | 0.73 | 0.58 | 658 | quarters: 0.30 → 0.19 → 0.14 → 0.12

Numbers say: light vs heavy: width 19.2 → 21.5 px, dark 0.73 → 0.73.

## Brush Artist · Refs · #04 Henry Ward grey cloud
Gouache · 50 px · 45.7 s

![Brush Artist · Refs · #04 Henry Ward grey cloud](Brush-Artist-Refs-04-Henry-Ward-grey-cloud.png)

A light paint: laid on a grey sheet (on white it cannot be seen); **dark** = how far it is from the grey either way.

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 6 % → 1 % | 16.4 px | 0.33 | 0.12 | 187 |
| heavy line | 10 % → 4 % | 30.4 px | 0.33 | 0.41 | 235 |
| pressure swell | 8 % → 4 % | 30.7 px | 0.33 | 0.50 | 164 |
| fast wave | 8 % → 2 % | 9.2 px | 0.33 | 0.21 | 781 |
| slow wave | 27 % → 13 % | 31.6 px | 0.33 | 0.47 | 1580 |
| spiral | 30 % → 11 % | 19.6 px | 0.33 | 0.38 | 1165 |
| loop | 19 % → 10 % | 24.8 px | 0.33 | 0.50 | 648 |
| tilted | 7 % → 7 % | 18.5 px | 0.33 | 1.02 | 261 |
| over the wet one | 17 % → 11 % | 28.1 px | 0.33 | 0.66 | 251 |
| long, no reload | 34 % → 16 % | 15.2 px | 0.33 | 0.46 | 1396 | quarters: 0.02 → 0.02 → 0.02 → 0.02

Numbers say: light vs heavy: width 16.4 → 30.4 px, dark 0.33 → 0.33; the long stroke does not run out of paint.

## Brush Artist · Refs · #05 Henry Ward green in rust loops
Heavy acrylic · 20 px · 29.1 s

![Brush Artist · Refs · #05 Henry Ward green in rust loops](Brush-Artist-Refs-05-Henry-Ward-green-in-rust-loops.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 6 % → 5 % | 17.1 px | 0.57 | 0.78 | 175 |
| heavy line | 7 % → 5 % | 19.3 px | 0.56 | 0.81 | 159 |
| pressure swell | 5 % → 5 % | 20.2 px | 0.57 | 0.86 | 125 |
| fast wave | 11 % → 7 % | 12.3 px | 0.57 | 0.63 | 264 |
| slow wave | 15 % → 11 % | 17.5 px | 0.56 | 0.72 | 543 |
| spiral | 20 % → 12 % | 12.9 px | 0.56 | 0.61 | 635 |
| loop | 12 % → 9 % | 15.8 px | 0.56 | 0.72 | 251 |
| tilted | 6 % → 6 % | 16.8 px | 0.57 | 1.00 | 136 |
| over the wet one | 12 % → 10 % | 17.8 px | 0.57 | 0.79 | 119 |
| long, no reload | 23 % → 13 % | 10.1 px | 0.56 | 0.58 | 624 | quarters: 0.20 → 0.12 → 0.09 → 0.08

Numbers say: light vs heavy: width 17.1 → 19.3 px, dark 0.57 → 0.56.

## Brush Artist · Refs · #06 Henry Ward scrubbed grey
Gouache · 50 px · 43.6 s

![Brush Artist · Refs · #06 Henry Ward scrubbed grey](Brush-Artist-Refs-06-Henry-Ward-scrubbed-grey.png)

A light paint: laid on a grey sheet (on white it cannot be seen); **dark** = how far it is from the grey either way.

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 6 % → 1 % | 16.4 px | 0.35 | 0.12 | 247 |
| heavy line | 10 % → 4 % | 30.4 px | 0.35 | 0.41 | 295 |
| pressure swell | 8 % → 4 % | 30.7 px | 0.35 | 0.50 | 168 |
| fast wave | 8 % → 2 % | 9.2 px | 0.35 | 0.21 | 530 |
| slow wave | 27 % → 13 % | 31.6 px | 0.35 | 0.47 | 961 |
| spiral | 30 % → 11 % | 19.6 px | 0.35 | 0.38 | 922 |
| loop | 19 % → 10 % | 24.8 px | 0.35 | 0.50 | 498 |
| tilted | 7 % → 7 % | 18.5 px | 0.35 | 1.02 | 371 |
| over the wet one | 17 % → 11 % | 28.1 px | 0.35 | 0.66 | 316 |
| long, no reload | 34 % → 16 % | 15.2 px | 0.34 | 0.46 | 1486 | quarters: 0.02 → 0.02 → 0.02 → 0.02

Numbers say: light vs heavy: width 16.4 → 30.4 px, dark 0.35 → 0.35; the long stroke does not run out of paint.

## Brush Artist · Refs · #07 Henry Ward blue L + black zigzag
Heavy acrylic · 34 px · 29.6 s

![Brush Artist · Refs · #07 Henry Ward blue L + black zigzag](Brush-Artist-Refs-07-Henry-Ward-blue-L-black-zigzag.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 10 % → 8 % | 30.4 px | 0.59 | 0.78 | 155 |
| heavy line | 12 % → 9 % | 33.8 px | 0.59 | 0.82 | 126 |
| pressure swell | 9 % → 8 % | 34.3 px | 0.60 | 0.87 | 115 |
| fast wave | 19 % → 12 % | 22.4 px | 0.60 | 0.62 | 440 |
| slow wave | 26 % → 19 % | 30.6 px | 0.60 | 0.73 | 586 |
| spiral | 36 % → 22 % | 23.9 px | 0.60 | 0.60 | 552 |
| loop | 21 % → 16 % | 27.4 px | 0.60 | 0.74 | 312 |
| tilted | 9 % → 9 % | 25.1 px | 0.60 | 0.99 | 167 |
| over the wet one | 20 % → 16 % | 30.9 px | 0.60 | 0.81 | 168 |
| long, no reload | 39 % → 23 % | 17.6 px | 0.60 | 0.60 | 832 | quarters: 0.34 → 0.23 → 0.16 → 0.13

Numbers say: light vs heavy: width 30.4 → 33.8 px, dark 0.59 → 0.59; pressure barely changes the width.

## Brush Artist · Refs · #08 Henry Ward olive bands
Gouache · 34 px · 34.5 s

![Brush Artist · Refs · #08 Henry Ward olive bands](Brush-Artist-Refs-08-Henry-Ward-olive-bands.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 4 % → 0 % | 12.2 px | 0.61 | 0.04 | 82 |
| heavy line | 7 % → 0 % | 19.3 px | 0.61 | 0.02 | 205 |
| pressure swell | 5 % → 0 % | 18.7 px | 0.61 | 0.03 | 113 |
| fast wave | 10 % → 0 % | 11.1 px | 0.61 | 0.02 | 513 |
| slow wave | 15 % → 1 % | 17.0 px | 0.61 | 0.06 | 807 |
| spiral | 19 % → 1 % | 12.7 px | 0.61 | 0.03 | 626 |
| loop | 12 % → 1 % | 15.3 px | 0.61 | 0.09 | 347 |
| tilted | 5 % → 5 % | 15.1 px | 0.61 | 0.96 | 184 |
| over the wet one | 11 % → 2 % | 16.9 px | 0.61 | 0.22 | 132 |
| long, no reload | 22 % → 2 % | 9.8 px | 0.61 | 0.09 | 867 | quarters: 0.21 → 0.15 → 0.11 → 0.09

Numbers say: light vs heavy: width 12.2 → 19.3 px, dark 0.61 → 0.61.

## Brush Artist · Refs · #09 Henry Ward white loops
Gouache · 46 px · 44.6 s

![Brush Artist · Refs · #09 Henry Ward white loops](Brush-Artist-Refs-09-Henry-Ward-white-loops.png)

A light paint: laid on a grey sheet (on white it cannot be seen); **dark** = how far it is from the grey either way.

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 5 % → 0 % | 13.8 px | 0.43 | 0.08 | 146 |
| heavy line | 9 % → 3 % | 26.0 px | 0.44 | 0.36 | 200 |
| pressure swell | 7 % → 3 % | 26.6 px | 0.44 | 0.43 | 134 |
| fast wave | 7 % → 1 % | 8.0 px | 0.44 | 0.14 | 436 |
| slow wave | 24 % → 11 % | 27.3 px | 0.43 | 0.44 | 946 |
| spiral | 27 % → 8 % | 17.9 px | 0.43 | 0.31 | 1179 |
| loop | 16 % → 7 % | 21.3 px | 0.43 | 0.45 | 423 |
| tilted | 6 % → 6 % | 15.9 px | 0.43 | 1.02 | 203 |
| over the wet one | 15 % → 9 % | 24.6 px | 0.43 | 0.64 | 221 |
| long, no reload | 30 % → 12 % | 13.3 px | 0.43 | 0.41 | 1132 | quarters: 0.02 → 0.02 → 0.02 → 0.03

Numbers say: light vs heavy: width 13.8 → 26.0 px, dark 0.43 → 0.44; the long stroke does not run out of paint.

## Brush Artist · Refs · #10 Henry Ward maroon loops
Heavy acrylic · 30 px · 30.6 s

![Brush Artist · Refs · #10 Henry Ward maroon loops](Brush-Artist-Refs-10-Henry-Ward-maroon-loops.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 9 % → 7 % | 25.8 px | 0.73 | 0.79 | 154 |
| heavy line | 10 % → 8 % | 28.7 px | 0.73 | 0.82 | 133 |
| pressure swell | 8 % → 7 % | 29.1 px | 0.74 | 0.87 | 91 |
| fast wave | 16 % → 10 % | 18.9 px | 0.74 | 0.63 | 319 |
| slow wave | 23 % → 17 % | 26.1 px | 0.74 | 0.75 | 566 |
| spiral | 30 % → 19 % | 19.8 px | 0.74 | 0.62 | 556 |
| loop | 18 % → 14 % | 23.4 px | 0.74 | 0.75 | 259 |
| tilted | 8 % → 8 % | 22.7 px | 0.74 | 0.99 | 167 |
| over the wet one | 18 % → 14 % | 26.2 px | 0.74 | 0.81 | 138 |
| long, no reload | 33 % → 20 % | 15.0 px | 0.74 | 0.60 | 749 | quarters: 0.39 → 0.27 → 0.20 → 0.18

Numbers say: light vs heavy: width 25.8 → 28.7 px, dark 0.73 → 0.73.

## Brush Artist · Refs · #11 Henry Ward purple spun balls
Heavy acrylic · 36 px · 31.7 s

![Brush Artist · Refs · #11 Henry Ward purple spun balls](Brush-Artist-Refs-11-Henry-Ward-purple-spun-balls.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 11 % → 10 % | 33.0 px | 0.74 | 0.85 | 169 |
| heavy line | 12 % → 11 % | 36.1 px | 0.74 | 0.87 | 153 |
| pressure swell | 10 % → 9 % | 36.3 px | 0.75 | 0.91 | 121 |
| fast wave | 22 % → 14 % | 24.9 px | 0.75 | 0.67 | 397 |
| slow wave | 28 % → 22 % | 32.4 px | 0.75 | 0.79 | 713 |
| spiral | 39 % → 25 % | 25.7 px | 0.75 | 0.64 | 726 |
| loop | 23 % → 18 % | 29.4 px | 0.75 | 0.79 | 320 |
| tilted | 10 % → 10 % | 27.7 px | 0.75 | 0.99 | 305 |
| over the wet one | 22 % → 18 % | 32.4 px | 0.75 | 0.85 | 228 |
| long, no reload | 42 % → 27 % | 18.8 px | 0.75 | 0.63 | 1268 | quarters: 0.48 → 0.35 → 0.26 → 0.22

Numbers say: light vs heavy: width 33.0 → 36.1 px, dark 0.74 → 0.74; pressure barely changes the width.

## Brush Artist · Refs · #12 Henry Ward black-olive cage
Gouache · 28 px · 31.8 s

![Brush Artist · Refs · #12 Henry Ward black-olive cage](Brush-Artist-Refs-12-Henry-Ward-black-olive-cage.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 3 % → 0 % | 10.1 px | 0.65 | 0.08 | 70 |
| heavy line | 5 % → 0 % | 15.3 px | 0.65 | 0.08 | 152 |
| pressure swell | 4 % → 0 % | 14.9 px | 0.65 | 0.10 | 107 |
| fast wave | 8 % → 0 % | 8.9 px | 0.65 | 0.04 | 292 |
| slow wave | 12 % → 1 % | 13.6 px | 0.65 | 0.09 | 559 |
| spiral | 16 % → 1 % | 10.4 px | 0.65 | 0.04 | 765 |
| loop | 9 % → 2 % | 12.3 px | 0.65 | 0.17 | 402 |
| tilted | 5 % → 4 % | 13.0 px | 0.65 | 0.95 | 136 |
| over the wet one | 9 % → 3 % | 13.2 px | 0.65 | 0.27 | 117 |
| long, no reload | 18 % → 2 % | 8.3 px | 0.65 | 0.12 | 725 | quarters: 0.19 → 0.14 → 0.11 → 0.10

Numbers say: light vs heavy: width 10.1 → 15.3 px, dark 0.65 → 0.65.

## Brush Artist · Refs · #13 Henry Ward blue streaky form
Gouache · 50 px · 47.2 s

![Brush Artist · Refs · #13 Henry Ward blue streaky form](Brush-Artist-Refs-13-Henry-Ward-blue-streaky-form.png)

A light paint: laid on a grey sheet (on white it cannot be seen); **dark** = how far it is from the grey either way.

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 6 % → 1 % | 16.4 px | 0.34 | 0.12 | 210 |
| heavy line | 10 % → 4 % | 30.4 px | 0.35 | 0.41 | 341 |
| pressure swell | 8 % → 4 % | 30.7 px | 0.35 | 0.50 | 223 |
| fast wave | 8 % → 2 % | 9.2 px | 0.35 | 0.21 | 536 |
| slow wave | 27 % → 13 % | 31.6 px | 0.34 | 0.47 | 1002 |
| spiral | 30 % → 11 % | 19.6 px | 0.34 | 0.38 | 1062 |
| loop | 19 % → 10 % | 24.8 px | 0.34 | 0.50 | 569 |
| tilted | 7 % → 7 % | 18.5 px | 0.34 | 1.02 | 309 |
| over the wet one | 17 % → 11 % | 28.1 px | 0.34 | 0.66 | 219 |
| long, no reload | 34 % → 16 % | 15.2 px | 0.34 | 0.46 | 1854 | quarters: 0.02 → 0.02 → 0.02 → 0.02

Numbers say: light vs heavy: width 16.4 → 30.4 px, dark 0.34 → 0.35; the long stroke does not run out of paint.

## Brush Artist · Refs · #14 Henry Ward olive totem
Heavy acrylic · 48 px · 26.8 s

![Brush Artist · Refs · #14 Henry Ward olive totem](Brush-Artist-Refs-14-Henry-Ward-olive-totem.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 15 % → 13 % | 43.6 px | 0.31 | 0.84 | 195 |
| heavy line | 16 % → 14 % | 47.9 px | 0.31 | 0.87 | 204 |
| pressure swell | 13 % → 12 % | 48.0 px | 0.32 | 0.91 | 166 |
| fast wave | 28 % → 19 % | 32.5 px | 0.31 | 0.68 | 516 |
| slow wave | 36 % → 29 % | 42.0 px | 0.30 | 0.79 | 1327 |
| spiral | 48 % → 32 % | 31.7 px | 0.30 | 0.67 | 1162 |
| loop | 29 % → 23 % | 38.1 px | 0.31 | 0.79 | 493 |
| tilted | 12 % → 12 % | 34.4 px | 0.32 | 0.99 | 271 |
| over the wet one | 27 % → 23 % | 42.1 px | 0.32 | 0.86 | 213 |
| long, no reload | 54 % → 35 % | 24.0 px | 0.30 | 0.65 | 1258 | quarters: 0.22 → 0.14 → 0.09 → 0.07

Numbers say: light vs heavy: width 43.6 → 47.9 px, dark 0.31 → 0.31; pressure barely changes the width.

## Brush Artist · Refs · #15 Ultramarine brush script
Ink · 4 px · 32.5 s

![Brush Artist · Refs · #15 Ultramarine brush script](Brush-Artist-Refs-15-Ultramarine-brush-script.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 1 % → 3 % | 2.2 px | 0.55 | 3.90 | 34 |
| heavy line | 6 % → 6 % | 16.7 px | 0.58 | 0.99 | 66 |
| pressure swell | 3 % → 4 % | 12.1 px | 0.64 | 1.15 | 59 |
| fast wave | 9 % → 7 % | 10.6 px | 0.54 | 0.81 | 177 |
| slow wave | 7 % → 7 % | 8.4 px | 0.54 | 0.93 | 171 |
| spiral | 11 % → 7 % | 7.2 px | 0.52 | 0.66 | 281 |
| loop | 7 % → 7 % | 9.2 px | 0.53 | 0.98 | 121 |
| tilted | 3 % → 3 % | 8.2 px | 0.62 | 1.02 | 53 |
| over the wet one | 7 % → 7 % | 11.5 px | 0.62 | 1.05 | 66 |
| long, no reload | 16 % → 8 % | 7.3 px | 0.50 | 0.48 | 346 | quarters: 0.15 → 0.04 → 0.01 → 0.00

Numbers say: light vs heavy: width 2.2 → 16.7 px, dark 0.55 → 0.58; wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #18 Blue oil-stick scribbles
Pastel · 10 px · 16.1 s

![Brush Artist · Refs · #18 Blue oil-stick scribbles](Brush-Artist-Refs-18-Blue-oil-stick-scribbles.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 1 % → 1 % | 2.9 px | 0.52 | 1.00 | 46 |
| heavy line | 2 % → 2 % | 5.5 px | 0.53 | 1.00 | 28 |
| pressure swell | 1 % → 1 % | 5.0 px | 0.53 | 1.00 | 30 |
| fast wave | 4 % → 4 % | 4.8 px | 0.53 | 1.00 | 91 |
| slow wave | 4 % → 4 % | 4.4 px | 0.53 | 1.00 | 89 |
| spiral | 7 % → 7 % | 4.5 px | 0.52 | 1.00 | 160 |
| loop | 3 % → 3 % | 4.5 px | 0.52 | 1.00 | 124 |
| tilted | 2 % → 2 % | 4.7 px | 0.53 | 1.00 | 92 |
| over the wet one | 3 % → 3 % | 4.7 px | 0.53 | 1.00 | 54 |
| long, no reload | 10 % → 10 % | 4.4 px | 0.53 | 1.00 | 270 | quarters: 0.06 → 0.06 → 0.06 → 0.06

Numbers say: light vs heavy: width 2.9 → 5.5 px, dark 0.52 → 0.53; the long stroke does not run out of paint.

## Brush Artist · Refs · #20 Orange-red crayon scribble
Pastel · 14 px · 15.0 s

![Brush Artist · Refs · #20 Orange-red crayon scribble](Brush-Artist-Refs-20-Orange-red-crayon-scribble.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 1 % → 1 % | 4.0 px | 0.53 | 1.00 | 39 |
| heavy line | 3 % → 3 % | 8.0 px | 0.53 | 1.00 | 53 |
| pressure swell | 2 % → 2 % | 7.6 px | 0.53 | 1.00 | 36 |
| fast wave | 6 % → 6 % | 7.2 px | 0.53 | 1.00 | 154 |
| slow wave | 6 % → 6 % | 6.6 px | 0.53 | 1.00 | 83 |
| spiral | 9 % → 9 % | 6.2 px | 0.53 | 1.00 | 137 |
| loop | 5 % → 5 % | 6.2 px | 0.53 | 1.00 | 99 |
| tilted | 2 % → 2 % | 5.6 px | 0.53 | 1.00 | 40 |
| over the wet one | 4 % → 4 % | 6.6 px | 0.53 | 1.00 | 34 |
| long, no reload | 13 % → 13 % | 5.7 px | 0.53 | 1.00 | 229 | quarters: 0.07 → 0.07 → 0.08 → 0.08

Numbers say: light vs heavy: width 4.0 → 8.0 px, dark 0.53 → 0.53; the long stroke does not run out of paint.

## Brush Artist · Refs · #21 Gritty black contours
Gouache · 12 px · 29.9 s

![Brush Artist · Refs · #21 Gritty black contours](Brush-Artist-Refs-21-Gritty-black-contours.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 1 % → 0 % | 3.3 px | 0.81 | 0.08 | 144 |
| heavy line | 2 % → 0 % | 5.2 px | 0.81 | 0.03 | 179 |
| pressure swell | 1 % → 0 % | 5.4 px | 0.81 | 0.04 | 95 |
| fast wave | 2 % → 0 % | 2.7 px | 0.81 | 0.01 | 258 |
| slow wave | 4 % → 0 % | 4.4 px | 0.81 | 0.04 | 278 |
| spiral | 5 % → 0 % | 3.1 px | 0.81 | 0.02 | 489 |
| loop | 3 % → 0 % | 4.1 px | 0.81 | 0.02 | 198 |
| tilted | 2 % → 2 % | 4.8 px | 0.81 | 0.93 | 134 |
| over the wet one | 3 % → 0 % | 4.7 px | 0.81 | 0.11 | 186 |
| long, no reload | 6 % → 0 % | 2.7 px | 0.81 | 0.06 | 833 | quarters: 0.09 → 0.06 → 0.05 → 0.04

Numbers say: light vs heavy: width 3.3 → 5.2 px, dark 0.81 → 0.81.

## Brush Artist · Refs · #22 Bold black brush poster
Ink · 20 px · 40.8 s

![Brush Artist · Refs · #22 Bold black brush poster](Brush-Artist-Refs-22-Bold-black-brush-poster.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 3 % → 5 % | 9.6 px | 0.79 | 1.64 | 61 |
| heavy line | 15 % → 15 % | 44.6 px | 0.88 | 0.99 | 122 |
| pressure swell | 9 % → 9 % | 31.9 px | 0.87 | 1.04 | 64 |
| fast wave | 27 % → 27 % | 31.7 px | 0.87 | 0.98 | 218 |
| slow wave | 22 % → 22 % | 25.4 px | 0.87 | 0.98 | 297 |
| spiral | 34 % → 32 % | 22.4 px | 0.87 | 0.94 | 403 |
| loop | 20 % → 20 % | 26.4 px | 0.88 | 1.00 | 186 |
| tilted | 8 % → 8 % | 23.1 px | 0.88 | 1.01 | 102 |
| over the wet one | 19 % → 19 % | 30.4 px | 0.88 | 1.00 | 92 |
| long, no reload | 45 % → 38 % | 20.3 px | 0.86 | 0.83 | 767 | quarters: 0.54 → 0.45 → 0.35 → 0.26

Numbers say: light vs heavy: width 9.6 → 44.6 px, dark 0.79 → 0.88; wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #23 Dry white on orange + black line
Gouache · 50 px · 33.7 s

![Brush Artist · Refs · #23 Dry white on orange + black line](Brush-Artist-Refs-23-Dry-white-on-orange-black-line.png)

A light paint: laid on a grey sheet (on white it cannot be seen); **dark** = how far it is from the grey either way.

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 5 % → 0 % | 15.7 px | 0.42 | 0.02 | 122 |
| heavy line | 9 % → 0 % | 25.3 px | 0.42 | 0.00 | 320 |
| pressure swell | 6 % → 0 % | 23.8 px | 0.41 | 0.00 | 187 |
| fast wave | 12 % → 0 % | 13.7 px | 0.41 | 0.01 | 512 |
| slow wave | 19 % → 0 % | 21.6 px | 0.41 | 0.02 | 1382 |
| spiral | 24 % → 0 % | 15.6 px | 0.40 | 0.01 | 1108 |
| loop | 15 % → 1 % | 19.8 px | 0.40 | 0.04 | 445 |
| tilted | 6 % → 6 % | 17.5 px | 0.40 | 0.94 | 236 |
| over the wet one | 14 % → 1 % | 20.6 px | 0.40 | 0.09 | 214 |
| long, no reload | 27 % → 1 % | 12.3 px | 0.40 | 0.05 | 1309 | quarters: 0.02 → 0.03 → 0.03 → 0.03

Numbers say: light vs heavy: width 15.7 → 25.3 px, dark 0.42 → 0.42; the long stroke does not run out of paint.

## Brush Artist · Refs · #24 Picasso flat oil
Oil · 34 px · 28.0 s

![Brush Artist · Refs · #24 Picasso flat oil](Brush-Artist-Refs-24-Picasso-flat-oil.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 11 % → 12 % | 33.4 px | 0.40 | 1.00 | 193 |
| heavy line | 12 % → 13 % | 36.2 px | 0.40 | 1.00 | 219 |
| pressure swell | 10 % → 10 % | 35.8 px | 0.41 | 1.00 | 150 |
| fast wave | 30 % → 30 % | 34.6 px | 0.41 | 1.00 | 507 |
| slow wave | 31 % → 31 % | 35.4 px | 0.40 | 1.00 | 846 |
| spiral | 52 % → 52 % | 34.0 px | 0.40 | 1.00 | 837 |
| loop | 25 % → 25 % | 32.7 px | 0.41 | 1.00 | 476 |
| tilted | 12 % → 12 % | 33.0 px | 0.40 | 1.00 | 217 |
| over the wet one | 23 % → 23 % | 31.9 px | 0.40 | 1.00 | 185 |
| long, no reload | 62 % → 62 % | 27.7 px | 0.39 | 1.00 | 1341 | quarters: 0.28 → 0.27 → 0.26 → 0.24

Numbers say: light vs heavy: width 33.4 → 36.2 px, dark 0.40 → 0.40; pressure barely changes the width; the long stroke does not run out of paint.

## Brush Artist · Refs · #25 Yellow heavy flat stroke
Heavy acrylic · 110 px · 52.9 s

![Brush Artist · Refs · #25 Yellow heavy flat stroke](Brush-Artist-Refs-25-Yellow-heavy-flat-stroke.png)

A light paint: laid on a grey sheet (on white it cannot be seen); **dark** = how far it is from the grey either way.

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 38 % → 39 % | 109.9 px | 0.30 | 1.02 | 592 |
| heavy line | 39 % → 39 % | 114.6 px | 0.30 | 0.98 | 561 |
| pressure swell | 31 % → 32 % | 115.0 px | 0.30 | 1.05 | 370 |
| fast wave | 75 % → 78 % | 86.6 px | 0.30 | 1.04 | 1349 |
| slow wave | 76 % → 74 % | 87.5 px | 0.30 | 0.98 | 2536 |
| spiral | 87 % → 83 % | 57.1 px | 0.29 | 0.96 | 2551 |
| loop | 65 % → 64 % | 83.7 px | 0.30 | 0.99 | 1620 |
| tilted | 29 % → 29 % | 81.2 px | 0.30 | 1.00 | 648 |
| over the wet one | 62 % → 61 % | 91.1 px | 0.30 | 0.98 | 745 |
| long, no reload | 100 % → 99 % | 44.7 px | 0.29 | 0.99 | 4538 | quarters: 0.00 → 0.00 → 0.00 → 0.00

Numbers say: light vs heavy: width 109.9 → 114.6 px, dark 0.30 → 0.30; pressure barely changes the width.

## Brush Artist · Refs · #27 Orange impasto swatch
Heavy acrylic · 60 px · 40.0 s

![Brush Artist · Refs · #27 Orange impasto swatch](Brush-Artist-Refs-27-Orange-impasto-swatch.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 21 % → 21 % | 59.7 px | 0.35 | 1.00 | 254 |
| heavy line | 22 % → 22 % | 62.5 px | 0.35 | 1.00 | 261 |
| pressure swell | 17 % → 17 % | 63.2 px | 0.36 | 1.01 | 185 |
| fast wave | 49 % → 48 % | 56.3 px | 0.35 | 0.98 | 669 |
| slow wave | 49 % → 48 % | 57.1 px | 0.35 | 0.98 | 1082 |
| spiral | 70 % → 63 % | 46.1 px | 0.34 | 0.91 | 1062 |
| loop | 42 % → 40 % | 53.9 px | 0.35 | 0.97 | 758 |
| tilted | 17 % → 17 % | 46.9 px | 0.35 | 1.00 | 352 |
| over the wet one | 36 % → 36 % | 53.9 px | 0.35 | 1.00 | 264 |
| long, no reload | 86 % → 76 % | 38.6 px | 0.35 | 0.88 | 1772 | quarters: 0.33 → 0.31 → 0.29 → 0.27

Numbers say: light vs heavy: width 59.7 → 62.5 px, dark 0.35 → 0.35; pressure barely changes the width.

## Brush Artist · Refs · #28 Miles Davis black lines
Ink · 22 px · 41.2 s

![Brush Artist · Refs · #28 Miles Davis black lines](Brush-Artist-Refs-28-Miles-Davis-black-lines.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 4 % → 6 % | 12.3 px | 0.81 | 1.49 | 54 |
| heavy line | 17 % → 17 % | 49.0 px | 0.88 | 0.99 | 131 |
| pressure swell | 10 % → 10 % | 35.9 px | 0.87 | 1.03 | 63 |
| fast wave | 31 % → 30 % | 35.5 px | 0.87 | 0.98 | 254 |
| slow wave | 25 % → 25 % | 28.7 px | 0.87 | 0.99 | 547 |
| spiral | 39 % → 37 % | 25.5 px | 0.87 | 0.95 | 850 |
| loop | 23 % → 23 % | 29.6 px | 0.88 | 1.00 | 259 |
| tilted | 9 % → 9 % | 25.3 px | 0.88 | 1.01 | 80 |
| over the wet one | 21 % → 21 % | 34.1 px | 0.88 | 1.00 | 118 |
| long, no reload | 51 % → 43 % | 22.9 px | 0.86 | 0.84 | 650 | quarters: 0.59 → 0.51 → 0.40 → 0.31

Numbers say: light vs heavy: width 12.3 → 49.0 px, dark 0.81 → 0.88.

## Brush Artist · Refs · #29 Shrigley magenta asterisk
Watercolor · 70 px · 44.1 s

![Brush Artist · Refs · #29 Shrigley magenta asterisk](Brush-Artist-Refs-29-Shrigley-magenta-asterisk.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 10 % → 13 % | 28.0 px | 0.65 | 1.36 | 67 |
| heavy line | 17 % → 18 % | 50.3 px | 0.64 | 1.03 | 172 |
| pressure swell | 11 % → 12 % | 41.1 px | 0.65 | 1.13 | 112 |
| fast wave | 38 % → 38 % | 43.8 px | 0.64 | 1.01 | 343 |
| slow wave | 35 % → 39 % | 41.0 px | 0.65 | 1.10 | 650 |
| spiral | 61 % → 61 % | 40.0 px | 0.64 | 1.01 | 657 |
| loop | 31 % → 32 % | 40.2 px | 0.65 | 1.03 | 441 |
| tilted | 18 % → 18 % | 49.0 px | 0.65 | 1.00 | 290 |
| over the wet one | 31 % → 34 % | 38.4 px | 0.65 | 1.07 | 158 |
| long, no reload | 75 % → 75 % | 33.6 px | 0.64 | 1.00 | 964 | quarters: 0.55 → 0.53 → 0.52 → 0.49

Numbers say: light vs heavy: width 28.0 → 50.3 px, dark 0.65 → 0.64; the long stroke does not run out of paint.

## Brush Artist · Refs · #30 Red gouache face patch
Gouache · 60 px · 52.9 s

![Brush Artist · Refs · #30 Red gouache face patch](Brush-Artist-Refs-30-Red-gouache-face-patch.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 16 % → 15 % | 47.0 px | 0.49 | 0.91 | 174 |
| heavy line | 25 % → 20 % | 74.0 px | 0.49 | 0.80 | 300 |
| pressure swell | 19 % → 17 % | 72.7 px | 0.49 | 0.86 | 169 |
| fast wave | 49 % → 28 % | 56.2 px | 0.49 | 0.58 | 586 |
| slow wave | 48 % → 28 % | 55.4 px | 0.49 | 0.59 | 1013 |
| spiral | 60 % → 28 % | 39.4 px | 0.49 | 0.47 | 939 |
| loop | 40 % → 29 % | 51.6 px | 0.49 | 0.74 | 747 |
| tilted | 16 % → 17 % | 46.0 px | 0.49 | 1.00 | 296 |
| over the wet one | 36 % → 32 % | 55.3 px | 0.49 | 0.89 | 244 |
| long, no reload | 67 % → 30 % | 30.1 px | 0.49 | 0.44 | 1326 | quarters: 0.43 → 0.39 → 0.32 → 0.26

Numbers say: light vs heavy: width 47.0 → 74.0 px, dark 0.49 → 0.49.

## Brush Artist · Refs · #31 Warhol blotted line
Ink · 6 px · 29.8 s

![Brush Artist · Refs · #31 Warhol blotted line](Brush-Artist-Refs-31-Warhol-blotted-line.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 1 % → 3 % | 2.7 px | 0.75 | 3.30 | 46 |
| heavy line | 7 % → 7 % | 20.7 px | 0.83 | 0.98 | 70 |
| pressure swell | 4 % → 4 % | 14.8 px | 0.84 | 1.12 | 41 |
| fast wave | 12 % → 9 % | 13.9 px | 0.82 | 0.76 | 147 |
| slow wave | 10 % → 8 % | 11.2 px | 0.80 | 0.84 | 138 |
| spiral | 15 % → 8 % | 9.7 px | 0.80 | 0.57 | 304 |
| loop | 9 % → 9 % | 11.9 px | 0.80 | 0.93 | 176 |
| tilted | 3 % → 3 % | 8.8 px | 0.84 | 1.03 | 87 |
| over the wet one | 8 % → 8 % | 14.4 px | 0.84 | 1.02 | 84 |
| long, no reload | 21 % → 9 % | 9.6 px | 0.78 | 0.43 | 385 | quarters: 0.25 → 0.13 → 0.05 → 0.01

Numbers say: light vs heavy: width 2.7 → 20.7 px, dark 0.75 → 0.83; wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #32 Thick orange swipes
Heavy acrylic · 90 px · 47.9 s

![Brush Artist · Refs · #32 Thick orange swipes](Brush-Artist-Refs-32-Thick-orange-swipes.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 31 % → 32 % | 89.3 px | 0.38 | 1.03 | 479 |
| heavy line | 32 % → 31 % | 92.9 px | 0.38 | 0.98 | 659 |
| pressure swell | 25 % → 26 % | 93.5 px | 0.39 | 1.04 | 795 |
| fast wave | 65 % → 67 % | 75.6 px | 0.38 | 1.02 | 1912 |
| slow wave | 66 % → 65 % | 76.0 px | 0.38 | 0.98 | 1928 |
| spiral | 80 % → 78 % | 52.8 px | 0.38 | 0.98 | 1893 |
| loop | 57 % → 56 % | 73.4 px | 0.38 | 0.99 | 1035 |
| tilted | 24 % → 24 % | 66.2 px | 0.38 | 1.00 | 713 |
| over the wet one | 51 % → 51 % | 77.2 px | 0.38 | 0.99 | 578 |
| long, no reload | 97 % → 95 % | 43.4 px | 0.38 | 0.98 | 2766 | quarters: 0.38 → 0.38 → 0.37 → 0.37

Numbers say: light vs heavy: width 89.3 → 92.9 px, dark 0.38 → 0.38; pressure barely changes the width; the long stroke does not run out of paint.

## Brush Artist · Refs · #33 Red wet-in-wet band
Watercolor · 80 px · 66.1 s

![Brush Artist · Refs · #33 Red wet-in-wet band](Brush-Artist-Refs-33-Red-wet-in-wet-band.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 19 % → 31 % | 55.6 px | 0.58 | 1.61 | 178 |
| heavy line | 29 % → 39 % | 83.7 px | 0.59 | 1.35 | 493 |
| pressure swell | 19 % → 27 % | 71.5 px | 0.61 | 1.42 | 374 |
| fast wave | 58 % → 74 % | 67.5 px | 0.61 | 1.27 | 1023 |
| slow wave | 57 % → 72 % | 65.7 px | 0.63 | 1.26 | 1002 |
| spiral | 75 % → 84 % | 49.6 px | 0.64 | 1.12 | 983 |
| loop | 51 % → 63 % | 66.4 px | 0.63 | 1.22 | 533 |
| tilted | 24 % → 25 % | 66.3 px | 0.60 | 1.03 | 513 |
| over the wet one | 48 % → 67 % | 66.7 px | 0.60 | 1.40 | 283 |
| long, no reload | 95 % → 99 % | 42.6 px | 0.66 | 1.04 | 1512 | quarters: 0.68 → 0.68 → 0.68 → 0.64

Numbers say: light vs heavy: width 55.6 → 83.7 px, dark 0.58 → 0.59; the long stroke does not run out of paint; wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #34 Magenta oil patches
Oil · 60 px · 32.6 s

![Brush Artist · Refs · #34 Magenta oil patches](Brush-Artist-Refs-34-Magenta-oil-patches.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 20 % → 20 % | 58.8 px | 0.61 | 1.01 | 297 |
| heavy line | 22 % → 22 % | 63.1 px | 0.61 | 1.00 | 297 |
| pressure swell | 17 % → 17 % | 62.7 px | 0.62 | 1.01 | 213 |
| fast wave | 49 % → 50 % | 56.7 px | 0.62 | 1.02 | 781 |
| slow wave | 49 % → 49 % | 57.1 px | 0.62 | 1.00 | 1398 |
| spiral | 71 % → 71 % | 46.9 px | 0.61 | 1.00 | 1373 |
| loop | 42 % → 42 % | 54.3 px | 0.62 | 1.00 | 840 |
| tilted | 18 % → 18 % | 49.8 px | 0.61 | 1.00 | 516 |
| over the wet one | 37 % → 37 % | 53.2 px | 0.61 | 1.00 | 436 |
| long, no reload | 88 % → 88 % | 39.2 px | 0.62 | 1.00 | 1936 | quarters: 0.59 → 0.58 → 0.56 → 0.54

Numbers say: light vs heavy: width 58.8 → 63.1 px, dark 0.61 → 0.61; pressure barely changes the width; the long stroke does not run out of paint.

## Brush Artist · Refs · #35 Red band with runs
Watercolor · 70 px · 70.3 s

![Brush Artist · Refs · #35 Red band with runs](Brush-Artist-Refs-35-Red-band-with-runs.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 17 % → 32 % | 48.3 px | 0.48 | 1.94 | 157 |
| heavy line | 25 % → 40 % | 73.9 px | 0.50 | 1.59 | 270 |
| pressure swell | 17 % → 26 % | 63.0 px | 0.54 | 1.52 | 200 |
| fast wave | 54 % → 72 % | 61.9 px | 0.52 | 1.35 | 588 |
| slow wave | 52 % → 71 % | 59.9 px | 0.55 | 1.37 | 1367 |
| spiral | 72 % → 88 % | 47.4 px | 0.55 | 1.23 | 922 |
| loop | 47 % → 69 % | 61.0 px | 0.52 | 1.47 | 483 |
| tilted | 21 % → 22 % | 57.7 px | 0.51 | 1.05 | 343 |
| over the wet one | 43 % → 68 % | 61.9 px | 0.51 | 1.60 | 213 |
| long, no reload | 92 % → 99 % | 41.4 px | 0.59 | 1.07 | 1280 | quarters: 0.60 → 0.60 → 0.60 → 0.56

Numbers say: light vs heavy: width 48.3 → 73.9 px, dark 0.48 → 0.50; the long stroke does not run out of paint; wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #36 Magenta letters flat brush
Gouache · 36 px · 48.6 s

![Brush Artist · Refs · #36 Magenta letters flat brush](Brush-Artist-Refs-36-Magenta-letters-flat-brush.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 10 % → 10 % | 29.1 px | 0.45 | 0.98 | 127 |
| heavy line | 17 % → 14 % | 49.1 px | 0.45 | 0.85 | 143 |
| pressure swell | 13 % → 12 % | 49.4 px | 0.45 | 0.89 | 95 |
| fast wave | 35 % → 19 % | 41.0 px | 0.45 | 0.54 | 420 |
| slow wave | 35 % → 19 % | 40.0 px | 0.45 | 0.54 | 578 |
| spiral | 46 % → 19 % | 30.5 px | 0.45 | 0.42 | 526 |
| loop | 27 % → 20 % | 35.4 px | 0.45 | 0.72 | 286 |
| tilted | 11 % → 11 % | 30.0 px | 0.45 | 1.00 | 151 |
| over the wet one | 24 % → 23 % | 38.1 px | 0.45 | 0.92 | 126 |
| long, no reload | 47 % → 19 % | 20.9 px | 0.45 | 0.40 | 807 | quarters: 0.29 → 0.26 → 0.22 → 0.18

Numbers say: light vs heavy: width 29.1 → 49.1 px, dark 0.45 → 0.45.

## Brush Artist · Refs · #37 Oil still life dabs
Oil · 40 px · 32.1 s

![Brush Artist · Refs · #37 Oil still life dabs](Brush-Artist-Refs-37-Oil-still-life-dabs.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 14 % → 14 % | 39.4 px | 0.39 | 1.00 | 201 |
| heavy line | 15 % → 15 % | 42.6 px | 0.39 | 1.00 | 302 |
| pressure swell | 11 % → 11 % | 42.0 px | 0.40 | 1.00 | 197 |
| fast wave | 35 % → 35 % | 40.4 px | 0.39 | 1.00 | 495 |
| slow wave | 35 % → 35 % | 40.8 px | 0.39 | 1.00 | 837 |
| spiral | 59 % → 59 % | 39.1 px | 0.38 | 1.00 | 834 |
| loop | 29 % → 29 % | 37.8 px | 0.39 | 1.00 | 495 |
| tilted | 13 % → 14 % | 37.6 px | 0.39 | 1.00 | 394 |
| over the wet one | 27 % → 27 % | 37.3 px | 0.39 | 1.00 | 386 |
| long, no reload | 69 % → 69 % | 31.1 px | 0.37 | 1.00 | 1928 | quarters: 0.31 → 0.30 → 0.28 → 0.25

Numbers say: light vs heavy: width 39.4 → 42.6 px, dark 0.39 → 0.39; pressure barely changes the width.

## Brush Artist · Refs · #38 Sanguine drawing
Pastel · 6 px · 13.6 s

![Brush Artist · Refs · #38 Sanguine drawing](Brush-Artist-Refs-38-Sanguine-drawing.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 1 % → 1 % | 2.0 px | 0.61 | 1.00 | 22 |
| heavy line | 1 % → 1 % | 3.5 px | 0.62 | 1.00 | 22 |
| pressure swell | 1 % → 1 % | 3.3 px | 0.62 | 1.00 | 23 |
| fast wave | 3 % → 3 % | 3.2 px | 0.61 | 1.00 | 74 |
| slow wave | 3 % → 3 % | 3.0 px | 0.61 | 1.00 | 63 |
| spiral | 4 % → 4 % | 2.9 px | 0.61 | 1.00 | 97 |
| loop | 2 % → 2 % | 3.0 px | 0.61 | 1.00 | 49 |
| tilted | 1 % → 1 % | 3.4 px | 0.62 | 1.00 | 28 |
| over the wet one | 2 % → 2 % | 2.9 px | 0.62 | 1.00 | 23 |
| long, no reload | 7 % → 7 % | 3.0 px | 0.61 | 1.00 | 155 | quarters: 0.04 → 0.05 → 0.05 → 0.05

Numbers say: light vs heavy: width 2.0 → 3.5 px, dark 0.61 → 0.62; the long stroke does not run out of paint.

## Brush Artist · Refs · #39 Very thick impasto
Heavy acrylic · 60 px · 40.4 s

![Brush Artist · Refs · #39 Very thick impasto](Brush-Artist-Refs-39-Very-thick-impasto.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 21 % → 21 % | 59.8 px | 0.61 | 1.02 | 255 |
| heavy line | 22 % → 22 % | 62.6 px | 0.61 | 1.02 | 289 |
| pressure swell | 17 % → 17 % | 63.3 px | 0.63 | 1.03 | 217 |
| fast wave | 49 % → 48 % | 56.4 px | 0.62 | 0.99 | 674 |
| slow wave | 50 % → 49 % | 57.3 px | 0.62 | 0.98 | 1251 |
| spiral | 70 % → 66 % | 46.3 px | 0.62 | 0.94 | 1733 |
| loop | 42 % → 41 % | 54.0 px | 0.62 | 0.97 | 635 |
| tilted | 17 % → 17 % | 46.9 px | 0.62 | 1.00 | 324 |
| over the wet one | 36 % → 37 % | 54.0 px | 0.62 | 1.02 | 287 |
| long, no reload | 87 % → 80 % | 38.8 px | 0.62 | 0.93 | 1786 | quarters: 0.58 → 0.57 → 0.55 → 0.53

Numbers say: light vs heavy: width 59.8 → 62.6 px, dark 0.61 → 0.61; pressure barely changes the width; the long stroke does not run out of paint.

## Brush Artist · Refs · #40 Watercolour blooms
Watercolor · 90 px · 75.1 s

![Brush Artist · Refs · #40 Watercolour blooms](Brush-Artist-Refs-40-Watercolour-blooms.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 22 % → 34 % | 63.3 px | 0.10 | 1.54 | 190 |
| heavy line | 33 % → 42 % | 94.9 px | 0.11 | 1.28 | 391 |
| pressure swell | 22 % → 30 % | 84.1 px | 0.12 | 1.34 | 316 |
| fast wave | 64 % → 79 % | 73.9 px | 0.11 | 1.23 | 803 |
| slow wave | 63 % → 76 % | 72.4 px | 0.16 | 1.21 | 1797 |
| spiral | 79 % → 87 % | 52.1 px | 0.15 | 1.10 | 1409 |
| loop | 56 % → 66 % | 72.5 px | 0.13 | 1.18 | 697 |
| tilted | 26 % → 27 % | 73.1 px | 0.13 | 1.03 | 493 |
| over the wet one | 53 % → 72 % | 73.8 px | 0.13 | 1.36 | 314 |
| long, no reload | 97 % → 100 % | 43.6 px | 0.17 | 1.02 | 2657 | quarters: 0.21 → 0.19 → 0.17 → 0.13

Numbers say: light vs heavy: width 63.3 → 94.9 px, dark 0.10 → 0.11; wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #41 Coloured pencil hatching
Pastel · 4 px · 14.4 s

![Brush Artist · Refs · #41 Coloured pencil hatching](Brush-Artist-Refs-41-Coloured-pencil-hatching.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 1 % → 1 % | 1.6 px | 0.42 | 1.00 | 22 |
| heavy line | 1 % → 1 % | 2.6 px | 0.43 | 1.00 | 17 |
| pressure swell | 1 % → 1 % | 2.1 px | 0.43 | 1.00 | 16 |
| fast wave | 2 % → 2 % | 2.2 px | 0.42 | 1.00 | 67 |
| slow wave | 2 % → 2 % | 2.1 px | 0.43 | 1.00 | 68 |
| spiral | 3 % → 3 % | 2.1 px | 0.43 | 1.00 | 71 |
| loop | 2 % → 2 % | 2.2 px | 0.43 | 1.00 | 46 |
| tilted | 1 % → 1 % | 3.0 px | 0.42 | 1.00 | 28 |
| over the wet one | 2 % → 2 % | 2.2 px | 0.42 | 1.00 | 17 |
| long, no reload | 5 % → 5 % | 2.3 px | 0.43 | 1.00 | 124 | quarters: 0.02 → 0.02 → 0.02 → 0.03

Numbers say: light vs heavy: width 1.6 → 2.6 px, dark 0.42 → 0.43; the long stroke does not run out of paint.

## Brush Artist · Refs · #42 Oil pastel shaggy
Pastel · 18 px · 16.6 s

![Brush Artist · Refs · #42 Oil pastel shaggy](Brush-Artist-Refs-42-Oil-pastel-shaggy.png)

A light paint: laid on a grey sheet (on white it cannot be seen); **dark** = how far it is from the grey either way.

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 2 % → 2 % | 5.1 px | 0.35 | 1.00 | 63 |
| heavy line | 4 % → 4 % | 10.7 px | 0.36 | 1.00 | 76 |
| pressure swell | 3 % → 3 % | 9.5 px | 0.36 | 1.00 | 37 |
| fast wave | 8 % → 8 % | 9.0 px | 0.36 | 1.00 | 87 |
| slow wave | 7 % → 7 % | 8.2 px | 0.36 | 1.00 | 135 |
| spiral | 12 % → 12 % | 7.7 px | 0.36 | 1.00 | 154 |
| loop | 6 % → 6 % | 7.9 px | 0.36 | 1.00 | 93 |
| tilted | 2 % → 2 % | 6.9 px | 0.36 | 1.00 | 50 |
| over the wet one | 6 % → 6 % | 8.5 px | 0.36 | 1.00 | 40 |
| long, no reload | 15 % → 15 % | 6.9 px | 0.36 | 1.00 | 212 | quarters: 0.00 → 0.00 → 0.00 → 0.00

Numbers say: light vs heavy: width 5.1 → 10.7 px, dark 0.35 → 0.36; the long stroke does not run out of paint.

## Brush Artist · Refs · #43 Dragged black ink blocks
Gouache · 70 px · 43.5 s

![Brush Artist · Refs · #43 Dragged black ink blocks](Brush-Artist-Refs-43-Dragged-black-ink-blocks.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 11 % → 0 % | 31.1 px | 0.65 | 0.03 | 216 |
| heavy line | 16 % → 1 % | 46.9 px | 0.65 | 0.08 | 545 |
| pressure swell | 12 % → 1 % | 44.8 px | 0.65 | 0.11 | 253 |
| fast wave | 22 % → 2 % | 25.8 px | 0.65 | 0.09 | 1179 |
| slow wave | 34 % → 4 % | 39.7 px | 0.65 | 0.13 | 2245 |
| spiral | 40 % → 4 % | 26.3 px | 0.65 | 0.11 | 1447 |
| loop | 28 % → 4 % | 36.5 px | 0.65 | 0.14 | 691 |
| tilted | 10 % → 10 % | 28.3 px | 0.65 | 0.98 | 394 |
| over the wet one | 24 % → 9 % | 40.0 px | 0.65 | 0.36 | 352 |
| long, no reload | 47 % → 8 % | 20.9 px | 0.65 | 0.16 | 2534 | quarters: 0.45 → 0.36 → 0.28 → 0.23

Numbers say: light vs heavy: width 31.1 → 46.9 px, dark 0.65 → 0.65.

## Brush Artist · Refs · #44 Blue looping ribbon
Oil · 80 px · 40.5 s

![Brush Artist · Refs · #44 Blue looping ribbon](Brush-Artist-Refs-44-Blue-looping-ribbon.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 28 % → 29 % | 80.0 px | 0.72 | 1.04 | 696 |
| heavy line | 29 % → 29 % | 85.0 px | 0.72 | 1.00 | 485 |
| pressure swell | 23 % → 23 % | 84.4 px | 0.72 | 1.03 | 301 |
| fast wave | 63 % → 65 % | 72.4 px | 0.72 | 1.04 | 1123 |
| slow wave | 62 % → 62 % | 72.1 px | 0.73 | 1.00 | 2051 |
| spiral | 79 % → 79 % | 51.9 px | 0.72 | 1.00 | 2771 |
| loop | 54 % → 54 % | 69.7 px | 0.73 | 1.00 | 1044 |
| tilted | 22 % → 22 % | 62.4 px | 0.72 | 1.00 | 584 |
| over the wet one | 47 % → 48 % | 70.0 px | 0.72 | 1.01 | 448 |
| long, no reload | 97 % → 97 % | 43.5 px | 0.73 | 1.00 | 2744 | quarters: 0.72 → 0.72 → 0.72 → 0.72

Numbers say: light vs heavy: width 80.0 → 85.0 px, dark 0.72 → 0.72; pressure barely changes the width; the long stroke does not run out of paint.

## Brush Artist · Refs · #45 Soft pastel pepper
Pastel · 40 px · 18.0 s

![Brush Artist · Refs · #45 Soft pastel pepper](Brush-Artist-Refs-45-Soft-pastel-pepper.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 4 % → 4 % | 11.3 px | 0.53 | 1.00 | 55 |
| heavy line | 8 % → 8 % | 23.0 px | 0.53 | 1.00 | 150 |
| pressure swell | 5 % → 5 % | 19.5 px | 0.53 | 1.00 | 65 |
| fast wave | 17 % → 17 % | 19.4 px | 0.53 | 1.00 | 296 |
| slow wave | 15 % → 15 % | 17.1 px | 0.53 | 1.00 | 601 |
| spiral | 25 % → 25 % | 16.3 px | 0.53 | 1.00 | 382 |
| loop | 12 % → 12 % | 16.1 px | 0.53 | 1.00 | 169 |
| tilted | 5 % → 5 % | 12.8 px | 0.53 | 1.00 | 103 |
| over the wet one | 11 % → 11 % | 17.7 px | 0.53 | 1.00 | 109 |
| long, no reload | 30 % → 30 % | 13.6 px | 0.53 | 1.00 | 515 | quarters: 0.18 → 0.18 → 0.18 → 0.18

Numbers say: light vs heavy: width 11.3 → 23.0 px, dark 0.53 → 0.53; the long stroke does not run out of paint.

## Brush Artist · Refs · #46 Red-brown ink lips
Watercolor · 50 px · 65.9 s

![Brush Artist · Refs · #46 Red-brown ink lips](Brush-Artist-Refs-46-Red-brown-ink-lips.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 12 % → 24 % | 33.6 px | 0.66 | 2.04 | 157 |
| heavy line | 19 % → 30 % | 54.1 px | 0.64 | 1.62 | 166 |
| pressure swell | 12 % → 21 % | 43.7 px | 0.67 | 1.76 | 90 |
| fast wave | 40 % → 61 % | 46.7 px | 0.66 | 1.50 | 309 |
| slow wave | 39 % → 59 % | 44.6 px | 0.68 | 1.54 | 565 |
| spiral | 63 % → 76 % | 41.7 px | 0.70 | 1.20 | 529 |
| loop | 35 % → 52 % | 44.9 px | 0.67 | 1.51 | 319 |
| tilted | 16 % → 17 % | 43.6 px | 0.66 | 1.07 | 361 |
| over the wet one | 33 % → 52 % | 47.6 px | 0.66 | 1.58 | 244 |
| long, no reload | 79 % → 95 % | 35.4 px | 0.70 | 1.21 | 961 | quarters: 0.71 → 0.71 → 0.70 → 0.65

Numbers say: light vs heavy: width 33.6 → 54.1 px, dark 0.66 → 0.64; the long stroke does not run out of paint; wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #47 Pink knife slabs
Heavy acrylic · 90 px · 44.0 s

![Brush Artist · Refs · #47 Pink knife slabs](Brush-Artist-Refs-47-Pink-knife-slabs.png)

A light paint: laid on a grey sheet (on white it cannot be seen); **dark** = how far it is from the grey either way.

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 34 % → 34 % | 98.8 px | 0.29 | 0.99 | 161 |
| heavy line | 34 % → 34 % | 98.8 px | 0.29 | 0.99 | 114 |
| pressure swell | 26 % → 27 % | 98.8 px | 0.29 | 1.04 | 30 |
| fast wave | 68 % → 58 % | 78.9 px | 0.26 | 0.85 | 207 |
| slow wave | 69 % → 61 % | 80.0 px | 0.26 | 0.88 | 441 |
| spiral | 67 % → 43 % | 44.4 px | 0.27 | 0.63 | 549 |
| loop | 60 % → 54 % | 77.8 px | 0.27 | 0.90 | 314 |
| tilted | 23 % → 23 % | 63.6 px | 0.28 | 1.00 | 145 |
| over the wet one | 53 % → 53 % | 83.8 px | 0.28 | 1.00 | 255 |
| long, no reload | 95 % → 62 % | 42.7 px | 0.25 | 0.65 | 872 | quarters: 0.00 → 0.00 → 0.00 → 0.00

Numbers say: light vs heavy: width 98.8 → 98.8 px, dark 0.29 → 0.29; pressure barely changes the width; the long stroke does not run out of paint.

## Brush Artist · Refs · #48 Black bands with drips
Gouache · 70 px · 68.8 s

![Brush Artist · Refs · #48 Black bands with drips](Brush-Artist-Refs-48-Black-bands-with-drips.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 19 % → 18 % | 54.7 px | 0.68 | 0.94 | 327 |
| heavy line | 29 % → 24 % | 83.1 px | 0.68 | 0.85 | 439 |
| pressure swell | 23 % → 21 % | 86.1 px | 0.68 | 0.92 | 305 |
| fast wave | 54 % → 37 % | 62.8 px | 0.68 | 0.67 | 865 |
| slow wave | 54 % → 36 % | 61.9 px | 0.68 | 0.67 | 1487 |
| spiral | 64 % → 35 % | 42.2 px | 0.68 | 0.54 | 2068 |
| loop | 45 % → 37 % | 58.1 px | 0.68 | 0.82 | 1103 |
| tilted | 19 % → 19 % | 52.5 px | 0.68 | 1.00 | 757 |
| over the wet one | 41 % → 38 % | 62.5 px | 0.68 | 0.92 | 397 |
| long, no reload | 74 % → 37 % | 33.4 px | 0.68 | 0.50 | 3041 | quarters: 0.64 → 0.61 → 0.54 → 0.44

Numbers say: light vs heavy: width 54.7 → 83.1 px, dark 0.68 → 0.68.

## Brush Artist · Refs · #49 Magenta letters round brush
Ink · 30 px · 47.9 s

![Brush Artist · Refs · #49 Magenta letters round brush](Brush-Artist-Refs-49-Magenta-letters-round-brush.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 6 % → 8 % | 17.5 px | 0.50 | 1.29 | 61 |
| heavy line | 21 % → 21 % | 62.0 px | 0.51 | 0.99 | 164 |
| pressure swell | 12 % → 13 % | 46.3 px | 0.52 | 1.02 | 103 |
| fast wave | 39 % → 38 % | 44.8 px | 0.51 | 0.99 | 496 |
| slow wave | 32 % → 31 % | 36.7 px | 0.51 | 0.99 | 663 |
| spiral | 50 % → 49 % | 33.2 px | 0.51 | 0.97 | 481 |
| loop | 29 % → 29 % | 37.8 px | 0.51 | 1.00 | 239 |
| tilted | 11 % → 11 % | 31.0 px | 0.52 | 1.01 | 115 |
| over the wet one | 26 % → 26 % | 42.0 px | 0.52 | 1.01 | 128 |
| long, no reload | 62 % → 56 % | 27.7 px | 0.50 | 0.91 | 752 | quarters: 0.41 → 0.36 → 0.30 → 0.25

Numbers say: light vs heavy: width 17.5 → 62.0 px, dark 0.50 → 0.51.

## Brush Artist · Refs · #50 Thick swipes on photo
Heavy acrylic · 40 px · 35.1 s

![Brush Artist · Refs · #50 Thick swipes on photo](Brush-Artist-Refs-50-Thick-swipes-on-photo.png)

A light paint: laid on a grey sheet (on white it cannot be seen); **dark** = how far it is from the grey either way.

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 14 % → 13 % | 39.4 px | 0.26 | 0.99 | 285 |
| heavy line | 14 % → 14 % | 41.6 px | 0.26 | 0.98 | 232 |
| pressure swell | 11 % → 11 % | 41.9 px | 0.25 | 0.99 | 187 |
| fast wave | 34 % → 31 % | 38.9 px | 0.25 | 0.93 | 510 |
| slow wave | 34 % → 33 % | 39.7 px | 0.26 | 0.95 | 750 |
| spiral | 59 % → 47 % | 38.9 px | 0.25 | 0.80 | 770 |
| loop | 28 % → 27 % | 36.9 px | 0.26 | 0.95 | 392 |
| tilted | 13 % → 13 % | 35.4 px | 0.26 | 1.00 | 250 |
| over the wet one | 26 % → 25 % | 36.8 px | 0.26 | 0.98 | 167 |
| long, no reload | 66 % → 46 % | 29.8 px | 0.24 | 0.69 | 1382 | quarters: 0.00 → 0.00 → 0.00 → 0.00

Numbers say: light vs heavy: width 39.4 → 41.6 px, dark 0.26 → 0.26; pressure barely changes the width; the long stroke does not run out of paint.

## Brush Artist · Refs · Drag #e8b4a8
Gouache · 40 px · 30.9 s

![Brush Artist · Refs · Drag #e8b4a8](Brush-Artist-Refs-Drag-e8b4a8.png)

A light paint: laid on a grey sheet (on white it cannot be seen); **dark** = how far it is from the grey either way.

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 2 % → 0 % | 5.0 px | 0.00 | 0.00 | 195 |
| heavy line | 3 % → 0 % | 8.7 px | 0.00 | 0.00 | 139 |
| pressure swell | 2 % → 0 % | 9.1 px | 0.00 | 0.00 | 153 |
| fast wave | 3 % → 0 % | 3.4 px | 0.00 | 0.00 | 410 |
| slow wave | 9 % → 0 % | 10.9 px | 0.00 | 0.00 | 809 |
| spiral | 10 % → 0 % | 6.9 px | 0.00 | 0.00 | 785 |
| loop | 6 % → 0 % | 7.9 px | 0.34 | 0.01 | 558 |
| tilted | 2 % → 2 % | 6.3 px | 0.34 | 0.89 | 168 |
| over the wet one | 5 % → 0 % | 8.2 px | 0.34 | 0.02 | 250 |
| long, no reload | 12 % → 0 % | 5.4 px | 0.34 | 0.01 | 1188 | quarters: 0.01 → 0.01 → 0.01 → 0.01

Numbers say: light vs heavy: width 5.0 → 8.7 px, dark 0.00 → 0.00; the long stroke does not run out of paint.

## Brush Artist · Refs · Drag #e8e4e0
Gouache · 40 px · 30.8 s

![Brush Artist · Refs · Drag #e8e4e0](Brush-Artist-Refs-Drag-e8e4e0.png)

A light paint: laid on a grey sheet (on white it cannot be seen); **dark** = how far it is from the grey either way.

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 2 % → 0 % | 5.0 px | 0.00 | 0.00 | 140 |
| heavy line | 3 % → 0 % | 8.7 px | 0.00 | 0.00 | 202 |
| pressure swell | 2 % → 0 % | 9.1 px | 0.00 | 0.00 | 108 |
| fast wave | 3 % → 0 % | 3.4 px | 0.00 | 0.00 | 420 |
| slow wave | 9 % → 0 % | 10.9 px | 0.00 | 0.00 | 813 |
| spiral | 10 % → 0 % | 6.9 px | 0.00 | 0.00 | 1064 |
| loop | 6 % → 0 % | 7.9 px | 0.42 | 0.01 | 1027 |
| tilted | 2 % → 2 % | 6.3 px | 0.42 | 0.89 | 210 |
| over the wet one | 5 % → 0 % | 8.2 px | 0.42 | 0.02 | 197 |
| long, no reload | 12 % → 0 % | 5.4 px | 0.43 | 0.01 | 1047 | quarters: 0.01 → 0.01 → 0.01 → 0.01

Numbers say: light vs heavy: width 5.0 → 8.7 px, dark 0.00 → 0.00; the long stroke does not run out of paint.

## Brush Artist · Refs · Finger
Pastel · 36 px · 32.7 s · over bands of wet oil paint and oil pastel in turn (it works on paint already there: look at what it does to the bands; covered counts the bands too)

![Brush Artist · Refs · Finger](Brush-Artist-Refs-Finger.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 25 % → 25 % | 73.9 px | 0.80 | 1.00 | 63 |
| heavy line | 27 % → 27 % | 78.5 px | 0.80 | 1.00 | 80 |
| pressure swell | 26 % → 26 % | 97.7 px | 0.80 | 1.00 | 64 |
| fast wave | 32 % → 32 % | 37.1 px | 0.78 | 1.00 | 311 |
| slow wave | 31 % → 31 % | 36.2 px | 0.78 | 1.00 | 317 |
| spiral | 38 % → 38 % | 25.0 px | 0.76 | 1.00 | 352 |
| loop | 30 % → 30 % | 39.4 px | 0.78 | 1.00 | 167 |
| tilted | 26 % → 26 % | 73.4 px | 0.79 | 1.00 | 101 |
| over the wet one | 29 % → 29 % | 6.7 px | 0.79 | 1.00 | 68 |
| long, no reload | 40 % → 40 % | 18.0 px | 0.75 | 1.00 | 465 | quarters: 0.25 → 0.36 → 0.33 → 0.38

Numbers say: light vs heavy: width 73.9 → 78.5 px, dark 0.80 → 0.80; pressure barely changes the width; the long stroke does not run out of paint.

## Brush Artist · Ink — wash
Watercolor · 38 px · 48.5 s

![Brush Artist · Ink — wash](Brush-Artist-Ink-wash.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 11 % → 11 % | 31.6 px | 0.38 | 1.04 | 86 |
| heavy line | 19 % → 19 % | 54.3 px | 0.32 | 1.03 | 139 |
| pressure swell | 12 % → 12 % | 45.1 px | 0.36 | 1.04 | 88 |
| fast wave | 39 % → 41 % | 45.5 px | 0.30 | 1.04 | 424 |
| slow wave | 37 % → 38 % | 42.9 px | 0.37 | 1.03 | 644 |
| spiral | 58 % → 60 % | 38.5 px | 0.30 | 1.04 | 526 |
| loop | 32 % → 33 % | 41.9 px | 0.35 | 1.02 | 223 |
| tilted | 13 % → 14 % | 36.9 px | 0.38 | 1.04 | 179 |
| over the wet one | 29 % → 30 % | 42.7 px | 0.38 | 1.04 | 110 |
| long, no reload | 67 % → 71 % | 29.9 px | 0.29 | 1.07 | 667 | quarters: 0.33 → 0.26 → 0.19 → 0.12

Numbers say: light vs heavy: width 31.6 → 54.3 px, dark 0.38 → 0.32.

## Brush Artist · Ink — brush line
Ink · 16 px · 39.8 s

![Brush Artist · Ink — brush line](Brush-Artist-Ink-brush-line.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 3 % → 5 % | 7.7 px | 0.78 | 1.81 | 47 |
| heavy line | 13 % → 13 % | 39.0 px | 0.88 | 0.99 | 101 |
| pressure swell | 8 % → 8 % | 28.4 px | 0.87 | 1.05 | 72 |
| fast wave | 24 % → 23 % | 28.0 px | 0.87 | 0.96 | 207 |
| slow wave | 20 % → 19 % | 22.6 px | 0.87 | 0.97 | 235 |
| spiral | 30 % → 27 % | 20.1 px | 0.86 | 0.89 | 519 |
| loop | 18 % → 18 % | 23.6 px | 0.88 | 1.00 | 236 |
| tilted | 7 % → 7 % | 20.5 px | 0.88 | 1.01 | 102 |
| over the wet one | 17 % → 17 % | 26.8 px | 0.88 | 1.00 | 82 |
| long, no reload | 42 % → 30 % | 18.9 px | 0.85 | 0.71 | 534 | quarters: 0.49 → 0.40 → 0.30 → 0.20

Numbers say: light vs heavy: width 7.7 → 39.0 px, dark 0.78 → 0.88; wet paint spreads well beyond the stroke.

## Brush Artist · Ink — dry brush
Gouache · 30 px · 29.7 s

![Brush Artist · Ink — dry brush](Brush-Artist-Ink-dry-brush.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 3 % → 0 % | 9.2 px | 0.77 | 0.00 | 84 |
| heavy line | 5 % → 0 % | 14.0 px | 0.00 | 0.00 | 193 |
| pressure swell | 4 % → 0 % | 13.5 px | 0.77 | 0.01 | 101 |
| fast wave | 7 % → 0 % | 8.0 px | 0.77 | 0.00 | 334 |
| slow wave | 11 % → 0 % | 12.2 px | 0.77 | 0.01 | 629 |
| spiral | 14 % → 0 % | 9.2 px | 0.77 | 0.01 | 594 |
| loop | 9 % → 0 % | 11.1 px | 0.77 | 0.02 | 272 |
| tilted | 4 % → 4 % | 11.2 px | 0.77 | 0.94 | 156 |
| over the wet one | 8 % → 1 % | 12.2 px | 0.77 | 0.10 | 183 |
| long, no reload | 16 % → 1 % | 7.2 px | 0.77 | 0.03 | 1231 | quarters: 0.21 → 0.15 → 0.12 → 0.11

Numbers say: light vs heavy: width 9.2 → 14.0 px, dark 0.77 → 0.00.

## Brush Artist · Watercolour — blue
Watercolor · 40 px · 46.1 s

![Brush Artist · Watercolour — blue](Brush-Artist-Watercolour-blue.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 6 % → 10 % | 16.7 px | 0.25 | 1.71 | 56 |
| heavy line | 11 % → 12 % | 31.5 px | 0.25 | 1.13 | 100 |
| pressure swell | 7 % → 9 % | 25.4 px | 0.26 | 1.32 | 62 |
| fast wave | 24 % → 25 % | 27.8 px | 0.24 | 1.06 | 235 |
| slow wave | 22 % → 27 % | 25.9 px | 0.26 | 1.22 | 366 |
| spiral | 38 % → 41 % | 25.2 px | 0.22 | 1.08 | 413 |
| loop | 20 % → 22 % | 25.3 px | 0.26 | 1.13 | 207 |
| tilted | 12 % → 12 % | 33.3 px | 0.26 | 1.00 | 396 |
| over the wet one | 21 % → 24 % | 24.7 px | 0.26 | 1.15 | 247 |
| long, no reload | 52 % → 54 % | 23.1 px | 0.22 | 1.04 | 743 | quarters: 0.18 → 0.14 → 0.11 → 0.08

Numbers say: light vs heavy: width 16.7 → 31.5 px, dark 0.25 → 0.25; wet paint spreads well beyond the stroke.

## Brush Artist · Watercolour — violet
Watercolor · 40 px · 46.2 s

![Brush Artist · Watercolour — violet](Brush-Artist-Watercolour-violet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 6 % → 10 % | 16.7 px | 0.40 | 1.71 | 57 |
| heavy line | 11 % → 12 % | 31.5 px | 0.40 | 1.13 | 87 |
| pressure swell | 7 % → 9 % | 25.4 px | 0.41 | 1.32 | 73 |
| fast wave | 24 % → 25 % | 27.8 px | 0.38 | 1.06 | 237 |
| slow wave | 22 % → 27 % | 25.9 px | 0.41 | 1.22 | 377 |
| spiral | 38 % → 41 % | 25.2 px | 0.36 | 1.08 | 358 |
| loop | 20 % → 22 % | 25.3 px | 0.40 | 1.13 | 220 |
| tilted | 12 % → 12 % | 33.3 px | 0.40 | 1.00 | 402 |
| over the wet one | 21 % → 24 % | 24.7 px | 0.40 | 1.15 | 149 |
| long, no reload | 52 % → 54 % | 23.1 px | 0.34 | 1.04 | 656 | quarters: 0.28 → 0.22 → 0.18 → 0.14

Numbers say: light vs heavy: width 16.7 → 31.5 px, dark 0.40 → 0.40; wet paint spreads well beyond the stroke.

## Brush Artist · Watercolour — teal
Watercolor · 40 px · 45.6 s

![Brush Artist · Watercolour — teal](Brush-Artist-Watercolour-teal.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 6 % → 10 % | 16.7 px | 0.16 | 1.71 | 60 |
| heavy line | 11 % → 12 % | 31.5 px | 0.16 | 1.13 | 103 |
| pressure swell | 7 % → 9 % | 25.4 px | 0.17 | 1.32 | 79 |
| fast wave | 24 % → 25 % | 27.8 px | 0.15 | 1.06 | 202 |
| slow wave | 22 % → 27 % | 25.9 px | 0.17 | 1.22 | 340 |
| spiral | 38 % → 41 % | 25.2 px | 0.15 | 1.08 | 885 |
| loop | 20 % → 22 % | 25.3 px | 0.16 | 1.13 | 286 |
| tilted | 12 % → 12 % | 33.3 px | 0.16 | 1.00 | 171 |
| over the wet one | 21 % → 24 % | 24.7 px | 0.16 | 1.15 | 106 |
| long, no reload | 52 % → 54 % | 23.1 px | 0.14 | 1.04 | 601 | quarters: 0.11 → 0.09 → 0.07 → 0.06

Numbers say: light vs heavy: width 16.7 → 31.5 px, dark 0.16 → 0.16; wet paint spreads well beyond the stroke.

## Brush Artist · Gouache
Gouache · 30 px · 49.3 s

![Brush Artist · Gouache](Brush-Artist-Gouache.png)

A light paint: laid on a grey sheet (on white it cannot be seen); **dark** = how far it is from the grey either way.

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 8 % → 8 % | 24.4 px | 0.27 | 0.97 | 103 |
| heavy line | 15 % → 12 % | 42.9 px | 0.27 | 0.78 | 174 |
| pressure swell | 11 % → 9 % | 41.1 px | 0.27 | 0.85 | 120 |
| fast wave | 30 % → 14 % | 35.0 px | 0.26 | 0.45 | 414 |
| slow wave | 29 % → 14 % | 34.0 px | 0.26 | 0.47 | 537 |
| spiral | 40 % → 14 % | 26.7 px | 0.26 | 0.35 | 553 |
| loop | 24 % → 15 % | 30.6 px | 0.26 | 0.62 | 298 |
| tilted | 10 % → 10 % | 27.5 px | 0.27 | 1.01 | 141 |
| over the wet one | 22 % → 19 % | 32.8 px | 0.27 | 0.89 | 120 |
| long, no reload | 43 % → 15 % | 19.1 px | 0.26 | 0.35 | 772 | quarters: 0.01 → 0.01 → 0.01 → 0.01

Numbers say: light vs heavy: width 24.4 → 42.9 px, dark 0.27 → 0.27; the long stroke does not run out of paint.

## Brush Artist · Oil — bristle
Oil · 30 px · 30.2 s

![Brush Artist · Oil — bristle](Brush-Artist-Oil-bristle.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 9 % → 9 % | 27.1 px | 0.54 | 1.00 | 172 |
| heavy line | 10 % → 10 % | 29.4 px | 0.54 | 1.00 | 188 |
| pressure swell | 8 % → 8 % | 29.3 px | 0.55 | 1.00 | 174 |
| fast wave | 24 % → 24 % | 27.6 px | 0.55 | 1.00 | 658 |
| slow wave | 25 % → 25 % | 28.6 px | 0.55 | 1.00 | 892 |
| spiral | 39 % → 39 % | 25.8 px | 0.54 | 1.00 | 736 |
| loop | 20 % → 20 % | 26.3 px | 0.54 | 1.00 | 381 |
| tilted | 11 % → 11 % | 30.6 px | 0.53 | 1.00 | 232 |
| over the wet one | 20 % → 20 % | 26.4 px | 0.53 | 1.00 | 175 |
| long, no reload | 50 % → 50 % | 22.5 px | 0.54 | 1.00 | 1138 | quarters: 0.32 → 0.30 → 0.29 → 0.28

Numbers say: light vs heavy: width 27.1 → 29.4 px, dark 0.54 → 0.54; pressure barely changes the width; the long stroke does not run out of paint.

## Brush Artist · Charcoal — stick
Charcoal · 28 px · 16.4 s

![Brush Artist · Charcoal — stick](Brush-Artist-Charcoal-stick.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 3 % → 3 % | 8.4 px | 0.85 | 1.00 | 50 |
| heavy line | 6 % → 6 % | 17.8 px | 0.85 | 1.00 | 55 |
| pressure swell | 4 % → 4 % | 13.9 px | 0.85 | 1.00 | 39 |
| fast wave | 12 % → 12 % | 14.0 px | 0.85 | 1.00 | 92 |
| slow wave | 11 % → 11 % | 12.5 px | 0.85 | 1.00 | 169 |
| spiral | 19 % → 19 % | 12.7 px | 0.85 | 1.00 | 147 |
| loop | 10 % → 10 % | 12.8 px | 0.85 | 1.00 | 62 |
| tilted | 4 % → 4 % | 10.9 px | 0.85 | 1.00 | 42 |
| over the wet one | 9 % → 9 % | 13.5 px | 0.85 | 1.00 | 28 |
| long, no reload | 27 % → 27 % | 12.2 px | 0.85 | 1.00 | 195 | quarters: 0.26 → 0.25 → 0.26 → 0.27

Numbers say: light vs heavy: width 8.4 → 17.8 px, dark 0.85 → 0.85; the long stroke does not run out of paint.

## Brush Artist · Charcoal — stick B
Charcoal · 36 px · 16.1 s

![Brush Artist · Charcoal — stick B](Brush-Artist-Charcoal-stick-B.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 4 % → 4 % | 10.5 px | 0.85 | 1.00 | 47 |
| heavy line | 7 % → 7 % | 21.1 px | 0.85 | 1.00 | 55 |
| pressure swell | 4 % → 4 % | 16.5 px | 0.85 | 1.00 | 39 |
| fast wave | 15 % → 15 % | 16.8 px | 0.85 | 1.00 | 98 |
| slow wave | 13 % → 13 % | 14.7 px | 0.85 | 1.00 | 180 |
| spiral | 23 % → 23 % | 15.0 px | 0.85 | 1.00 | 182 |
| loop | 11 % → 11 % | 14.8 px | 0.85 | 1.00 | 86 |
| tilted | 4 % → 4 % | 12.3 px | 0.85 | 1.00 | 70 |
| over the wet one | 10 % → 10 % | 15.9 px | 0.85 | 1.00 | 40 |
| long, no reload | 31 % → 31 % | 13.9 px | 0.85 | 1.00 | 280 | quarters: 0.30 → 0.28 → 0.29 → 0.30

Numbers say: light vs heavy: width 10.5 → 21.1 px, dark 0.85 → 0.85; the long stroke does not run out of paint.

## Brush Artist · Charcoal — stick C
Charcoal · 22 px · 16.2 s

![Brush Artist · Charcoal — stick C](Brush-Artist-Charcoal-stick-C.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 2 % → 2 % | 6.9 px | 0.85 | 1.00 | 26 |
| heavy line | 5 % → 5 % | 15.3 px | 0.85 | 1.00 | 43 |
| pressure swell | 3 % → 3 % | 12.2 px | 0.85 | 1.00 | 15 |
| fast wave | 10 % → 10 % | 12.1 px | 0.85 | 1.00 | 61 |
| slow wave | 9 % → 9 % | 10.8 px | 0.85 | 1.00 | 90 |
| spiral | 17 % → 17 % | 11.0 px | 0.85 | 1.00 | 179 |
| loop | 9 % → 9 % | 11.4 px | 0.85 | 1.00 | 85 |
| tilted | 4 % → 4 % | 9.9 px | 0.85 | 1.00 | 64 |
| over the wet one | 8 % → 8 % | 11.7 px | 0.85 | 1.00 | 44 |
| long, no reload | 24 % → 24 % | 11.0 px | 0.85 | 1.00 | 295 | quarters: 0.24 → 0.22 → 0.23 → 0.24

Numbers say: light vs heavy: width 6.9 → 15.3 px, dark 0.85 → 0.85; the long stroke does not run out of paint.

## Brush Artist · Refs · #01 Henry Ward peach cloud — own sheet
own sheet 600 × 600 · Gouache · 44 px · 20.7 s

![Brush Artist · Refs · #01 Henry Ward peach cloud — own sheet](Brush-Artist-Refs-01-Henry-Ward-peach-cloud-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 9 % → 21 % | 26.0 px | 0.57 | 2.33 | 392 |
| stroke 2 | 15 % → 33 % | 50.8 px | 0.57 | 2.17 | 381 |
| stroke 3 | 18 % → 32 % | 51.6 px | 0.57 | 1.81 | 334 |
| stroke 4 | 20 % → 37 % | 64.2 px | 0.57 | 1.89 | 341 |
| stroke 5 | 19 % → 32 % | 53.7 px | 0.57 | 1.73 | 190 |
| stroke 6 | 19 % → 24 % | 58.2 px | 0.57 | 1.27 | 195 |
| stroke 7 | 6 % → 28 % | 16.1 px | 0.57 | 4.34 | 224 |
| stroke 8 | 8 % → 26 % | 19.5 px | 0.57 | 3.37 | 241 |
| stroke 9 | 10 % → 27 % | 26.8 px | 0.57 | 2.55 | 236 |
| stroke 10 | 12 % → 27 % | 31.2 px | 0.57 | 2.33 | 235 |
| stroke 11 | 14 % → 29 % | 38.5 px | 0.57 | 2.12 | 233 |
| stroke 12 | 15 % → 31 % | 46.4 px | 0.57 | 1.99 | 212 |
| stroke 13 | 20 % → 33 % | 58.7 px | 0.57 | 1.63 | 224 |
| stroke 14 | 22 % → 34 % | 63.7 px | 0.57 | 1.54 | 287 |
| stroke 15 | 29 % → 38 % | 86.4 px | 0.57 | 1.29 | 285 |
| stroke 16 | 31 % → 38 % | 92.5 px | 0.57 | 1.24 | 297 |
| stroke 17 | 32 % → 39 % | 89.8 px | 0.57 | 1.21 | 278 |
| stroke 18 | 33 % → 38 % | 95.5 px | 0.57 | 1.17 | 286 |
| stroke 19 | 35 % → 38 % | 97.2 px | 0.57 | 1.11 | 312 |
| stroke 20 | 35 % → 37 % | 99.6 px | 0.57 | 1.06 | 243 |
| stroke 21 | 35 % → 35 % | 102.1 px | 0.57 | 0.99 | 246 |
| stroke 22 | 37 % → 35 % | 107.0 px | 0.57 | 0.96 | 238 |
| stroke 23 | 37 % → 34 % | 104.8 px | 0.57 | 0.93 | 237 |
| stroke 24 | 40 % → 36 % | 118.3 px | 0.57 | 0.92 | 231 |

Numbers say: wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #02 Henry Ward cream strokes — own sheet
own sheet 600 × 600 · Gouache · 46 px · 12.9 s

![Brush Artist · Refs · #02 Henry Ward cream strokes — own sheet](Brush-Artist-Refs-02-Henry-Ward-cream-strokes-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 11 % → 16 % | 22.9 px | 0.69 | 1.44 | 395 |
| stroke 2 | 17 % → 19 % | 43.8 px | 0.69 | 1.14 | 348 |
| stroke 3 | 17 % → 23 % | 42.4 px | 0.69 | 1.40 | 380 |
| stroke 4 | 18 % → 22 % | 44.4 px | 0.69 | 1.21 | 400 |
| stroke 5 | 22 % → 24 % | 53.2 px | 0.69 | 1.10 | 371 |
| stroke 6 | 17 % → 20 % | 40.7 px | 0.69 | 1.21 | 383 |
| stroke 7 | 18 % → 14 % | 45.2 px | 0.69 | 0.79 | 352 |

## Brush Artist · Refs · #03 Henry Ward navy contours — own sheet
own sheet 600 × 600 · Heavy acrylic · 22 px · 5.7 s

![Brush Artist · Refs · #03 Henry Ward navy contours — own sheet](Brush-Artist-Refs-03-Henry-Ward-navy-contours-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 10 % → 14 % | 20.0 px | 0.69 | 1.37 | 223 |
| stroke 2 | 18 % → 18 % | 25.8 px | 0.69 | 1.01 | 190 |
| stroke 3 | 21 % → 19 % | 30.6 px | 0.69 | 0.94 | 244 |
| stroke 4 | 20 % → 16 % | 44.3 px | 0.69 | 0.83 | 254 |

## Brush Artist · Refs · #04 Henry Ward grey cloud — own sheet
own sheet 600 × 600 · Gouache · 50 px · 19.2 s

![Brush Artist · Refs · #04 Henry Ward grey cloud — own sheet](Brush-Artist-Refs-04-Henry-Ward-grey-cloud-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 6 % → 18 % | 18.3 px | 0.38 | 2.95 | 261 |
| stroke 2 | 8 % → 20 % | 23.0 px | 0.38 | 2.45 | 588 |
| stroke 3 | 12 % → 22 % | 34.5 px | 0.38 | 1.79 | 465 |
| stroke 4 | 14 % → 23 % | 39.6 px | 0.38 | 1.71 | 422 |
| stroke 5 | 17 % → 26 % | 51.4 px | 0.38 | 1.56 | 460 |
| stroke 6 | 18 % → 28 % | 59.8 px | 0.38 | 1.55 | 431 |
| stroke 7 | 22 % → 31 % | 63.6 px | 0.38 | 1.43 | 323 |
| stroke 8 | 22 % → 31 % | 64.4 px | 0.38 | 1.44 | 334 |
| stroke 9 | 20 % → 31 % | 61.2 px | 0.38 | 1.51 | 301 |
| stroke 10 | 21 % → 31 % | 68.8 px | 0.38 | 1.45 | 318 |
| stroke 11 | 22 % → 31 % | 62.4 px | 0.38 | 1.42 | 331 |
| stroke 12 | 22 % → 32 % | 65.7 px | 0.38 | 1.45 | 311 |
| stroke 13 | 22 % → 33 % | 62.5 px | 0.38 | 1.49 | 271 |
| stroke 14 | 22 % → 33 % | 65.2 px | 0.38 | 1.49 | 316 |
| stroke 15 | 22 % → 30 % | 62.9 px | 0.38 | 1.39 | 335 |
| stroke 16 | 22 % → 29 % | 68.1 px | 0.38 | 1.30 | 319 |
| stroke 17 | 21 % → 25 % | 60.8 px | 0.38 | 1.17 | 291 |
| stroke 18 | 21 % → 23 % | 69.5 px | 0.38 | 1.09 | 292 |
| stroke 19 | 22 % → 20 % | 64.9 px | 0.38 | 0.90 | 327 |
| stroke 20 | 23 % → 19 % | 71.5 px | 0.38 | 0.85 | 278 |

Numbers say: wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #05 Henry Ward green in rust loops — own sheet
own sheet 600 × 600 · Heavy acrylic · 20 px · 5.6 s

![Brush Artist · Refs · #05 Henry Ward green in rust loops — own sheet](Brush-Artist-Refs-05-Henry-Ward-green-in-rust-loops-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 10 % → 14 % | 18.6 px | 0.03 | 1.32 | 262 |
| stroke 2 | 10 % → 9 % | 20.4 px | 0.03 | 0.84 | 348 |
| stroke 3 | 21 % → 17 % | 37.1 px | 0.03 | 0.82 | 241 |

## Brush Artist · Refs · #06 Henry Ward scrubbed grey — own sheet
own sheet 600 × 600 · Gouache · 50 px · 19.3 s

![Brush Artist · Refs · #06 Henry Ward scrubbed grey — own sheet](Brush-Artist-Refs-06-Henry-Ward-scrubbed-grey-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 7 % → 20 % | 17.8 px | 0.38 | 2.68 | 354 |
| stroke 2 | 9 % → 21 % | 25.1 px | 0.38 | 2.21 | 304 |
| stroke 3 | 13 % → 23 % | 39.1 px | 0.38 | 1.79 | 293 |
| stroke 4 | 14 % → 23 % | 42.8 px | 0.38 | 1.71 | 325 |
| stroke 5 | 19 % → 29 % | 56.5 px | 0.38 | 1.56 | 287 |
| stroke 6 | 20 % → 30 % | 61.4 px | 0.38 | 1.47 | 335 |
| stroke 7 | 22 % → 31 % | 62.8 px | 0.38 | 1.41 | 327 |
| stroke 8 | 22 % → 31 % | 69.9 px | 0.38 | 1.40 | 289 |
| stroke 9 | 21 % → 31 % | 64.4 px | 0.38 | 1.47 | 269 |
| stroke 10 | 21 % → 31 % | 67.2 px | 0.38 | 1.50 | 281 |
| stroke 11 | 22 % → 31 % | 65.7 px | 0.38 | 1.40 | 314 |
| stroke 12 | 23 % → 31 % | 69.7 px | 0.38 | 1.37 | 333 |
| stroke 13 | 22 % → 33 % | 61.4 px | 0.38 | 1.51 | 289 |
| stroke 14 | 21 % → 33 % | 61.6 px | 0.38 | 1.57 | 309 |
| stroke 15 | 21 % → 33 % | 60.8 px | 0.38 | 1.54 | 318 |
| stroke 16 | 21 % → 32 % | 66.4 px | 0.38 | 1.55 | 263 |
| stroke 17 | 21 % → 29 % | 61.0 px | 0.38 | 1.39 | 301 |
| stroke 18 | 21 % → 28 % | 64.7 px | 0.38 | 1.28 | 336 |
| stroke 19 | 21 % → 25 % | 63.7 px | 0.38 | 1.17 | 395 |
| stroke 20 | 22 % → 24 % | 67.7 px | 0.38 | 1.11 | 466 |
| stroke 21 | 22 % → 21 % | 64.0 px | 0.38 | 0.95 | 451 |
| stroke 22 | 22 % → 19 % | 72.0 px | 0.38 | 0.86 | 398 |

Numbers say: wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #07 Henry Ward blue L + black zigzag — own sheet
own sheet 600 × 600 · Heavy acrylic · 34 px · 3.1 s

![Brush Artist · Refs · #07 Henry Ward blue L + black zigzag — own sheet](Brush-Artist-Refs-07-Henry-Ward-blue-L-black-zigzag-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 15 % → 15 % | 33.6 px | 0.58 | 1.02 | 197 |
| stroke 2 | 16 % → 14 % | 40.0 px | 0.58 | 0.84 | 141 |

## Brush Artist · Refs · #08 Henry Ward olive bands — own sheet
own sheet 600 × 600 · Gouache · 34 px · 8.9 s

![Brush Artist · Refs · #08 Henry Ward olive bands — own sheet](Brush-Artist-Refs-08-Henry-Ward-olive-bands-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 9 % → 7 % | 17.9 px | 0.59 | 0.82 | 236 |
| stroke 2 | 15 % → 9 % | 32.8 px | 0.59 | 0.63 | 283 |
| stroke 3 | 13 % → 13 % | 26.4 px | 0.59 | 1.02 | 254 |
| stroke 4 | 15 % → 11 % | 31.5 px | 0.59 | 0.78 | 278 |
| stroke 5 | 20 % → 14 % | 40.1 px | 0.59 | 0.71 | 266 |
| stroke 6 | 13 % → 7 % | 24.2 px | 0.59 | 0.52 | 234 |

## Brush Artist · Refs · #09 Henry Ward white loops — own sheet
own sheet 600 × 600 · Gouache · 46 px · 13.3 s

![Brush Artist · Refs · #09 Henry Ward white loops — own sheet](Brush-Artist-Refs-09-Henry-Ward-white-loops-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 15 % → 2 % | 7.8 px | 0.08 | 0.14 | 1479 |
| stroke 2 | 16 % → 2 % | 15.6 px | 0.08 | 0.11 | 1518 |
| stroke 3 | 20 % → 2 % | 18.5 px | 0.09 | 0.10 | 1454 |
| stroke 4 | 2 % → 0 % | 5.2 px | 0.08 | 0.18 | 240 |
| stroke 5 | 3 % → 1 % | 8.9 px | 0.09 | 0.25 | 243 |
| stroke 6 | 4 % → 2 % | 11.2 px | 0.08 | 0.49 | 251 |
| stroke 7 | 9 % → 2 % | 23.2 px | 0.08 | 0.23 | 265 |
| stroke 8 | 2 % → 0 % | 3.0 px | 0.06 | 0.06 | 275 |

## Brush Artist · Refs · #10 Henry Ward maroon loops — own sheet
own sheet 600 × 600 · Heavy acrylic · 30 px · 5.0 s

![Brush Artist · Refs · #10 Henry Ward maroon loops — own sheet](Brush-Artist-Refs-10-Henry-Ward-maroon-loops-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 10 % → 23 % | 24.5 px | 0.70 | 2.35 | 355 |
| stroke 2 | 20 % → 35 % | 46.0 px | 0.70 | 1.72 | 188 |
| stroke 3 | 27 % → 32 % | 54.1 px | 0.70 | 1.18 | 223 |
| stroke 4 | 37 % → 35 % | 84.5 px | 0.70 | 0.93 | 149 |
| stroke 5 | 30 % → 25 % | 75.6 px | 0.70 | 0.83 | 259 |

Numbers say: wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #11 Henry Ward purple spun balls — own sheet
own sheet 600 × 600 · Heavy acrylic · 36 px · 5.2 s

![Brush Artist · Refs · #11 Henry Ward purple spun balls — own sheet](Brush-Artist-Refs-11-Henry-Ward-purple-spun-balls-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 23 % → 30 % | 25.0 px | 0.67 | 1.30 | 371 |
| stroke 2 | 33 % → 40 % | 35.9 px | 0.67 | 1.21 | 411 |
| stroke 3 | 34 % → 30 % | 37.1 px | 0.67 | 0.89 | 412 |

## Brush Artist · Refs · #12 Henry Ward black-olive cage — own sheet
own sheet 600 × 600 · Gouache · 28 px · 9.4 s

![Brush Artist · Refs · #12 Henry Ward black-olive cage — own sheet](Brush-Artist-Refs-12-Henry-Ward-black-olive-cage-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 7 % → 12 % | 13.4 px | 0.60 | 1.68 | 351 |
| stroke 2 | 7 % → 12 % | 16.3 px | 0.60 | 1.80 | 299 |
| stroke 3 | 15 % → 16 % | 24.2 px | 0.60 | 1.03 | 333 |
| stroke 4 | 16 % → 15 % | 32.2 px | 0.60 | 0.92 | 290 |
| stroke 5 | 16 % → 11 % | 29.0 px | 0.60 | 0.68 | 218 |
| stroke 6 | 25 % → 16 % | 48.3 px | 0.60 | 0.65 | 424 |

Numbers say: wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #13 Henry Ward blue streaky form — own sheet
own sheet 600 × 600 · Gouache · 50 px · 18.4 s

![Brush Artist · Refs · #13 Henry Ward blue streaky form — own sheet](Brush-Artist-Refs-13-Henry-Ward-blue-streaky-form-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 6 % → 4 % | 19.6 px | 0.02 | 0.66 | 450 |
| stroke 2 | 9 % → 4 % | 26.3 px | 0.02 | 0.46 | 363 |
| stroke 3 | 14 % → 4 % | 39.4 px | 0.02 | 0.31 | 289 |
| stroke 4 | 14 % → 4 % | 45.3 px | 0.02 | 0.28 | 303 |
| stroke 5 | 20 % → 4 % | 58.9 px | 0.02 | 0.21 | 340 |
| stroke 6 | 21 % → 5 % | 59.4 px | 0.02 | 0.25 | 386 |
| stroke 7 | 21 % → 6 % | 62.5 px | 0.02 | 0.28 | 379 |
| stroke 8 | 21 % → 5 % | 63.7 px | 0.02 | 0.22 | 352 |
| stroke 9 | 20 % → 4 % | 63.1 px | 0.02 | 0.20 | 279 |
| stroke 10 | 20 % → 4 % | 67.2 px | 0.02 | 0.19 | 267 |
| stroke 11 | 20 % → 3 % | 61.3 px | 0.02 | 0.14 | 263 |
| stroke 12 | 20 % → 3 % | 59.7 px | 0.03 | 0.17 | 344 |
| stroke 13 | 20 % → 4 % | 63.4 px | 0.03 | 0.19 | 288 |
| stroke 14 | 20 % → 4 % | 59.0 px | 0.03 | 0.18 | 318 |
| stroke 15 | 21 % → 4 % | 59.2 px | 0.03 | 0.18 | 356 |
| stroke 16 | 22 % → 4 % | 64.9 px | 0.03 | 0.17 | 310 |
| stroke 17 | 25 % → 2 % | 61.3 px | 0.03 | 0.08 | 286 |
| stroke 18 | 26 % → 2 % | 63.5 px | 0.03 | 0.07 | 331 |
| stroke 19 | 30 % → 2 % | 60.0 px | 0.03 | 0.08 | 344 |
| stroke 20 | 32 % → 2 % | 61.4 px | 0.03 | 0.07 | 278 |
| stroke 21 | 1 % → 0 % | 2.9 px | 0.03 | 0.02 | 213 |
| stroke 22 | 6 % → 4 % | 17.0 px | 0.02 | 0.67 | 280 |
| stroke 23 | 11 % → 4 % | 35.5 px | 0.02 | 0.38 | 280 |
| stroke 24 | 7 % → 3 % | 18.5 px | 0.02 | 0.41 | 321 |
| stroke 25 | 8 % → 3 % | 20.3 px | 0.03 | 0.32 | 339 |

## Brush Artist · Refs · #14 Henry Ward olive totem — own sheet
own sheet 600 × 600 · Heavy acrylic · 48 px · 13.5 s

![Brush Artist · Refs · #14 Henry Ward olive totem — own sheet](Brush-Artist-Refs-14-Henry-Ward-olive-totem-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 17 % → 46 % | 45.4 px | 0.36 | 2.63 | 294 |
| stroke 2 | 21 % → 49 % | 64.9 px | 0.36 | 2.37 | 233 |
| stroke 3 | 29 % → 51 % | 100.4 px | 0.36 | 1.73 | 249 |
| stroke 4 | 31 % → 53 % | 115.8 px | 0.36 | 1.72 | 260 |
| stroke 5 | 40 % → 62 % | 139.2 px | 0.36 | 1.55 | 228 |
| stroke 6 | 40 % → 63 % | 154.0 px | 0.36 | 1.60 | 188 |
| stroke 7 | 37 % → 59 % | 126.1 px | 0.36 | 1.59 | 198 |
| stroke 8 | 38 % → 61 % | 143.6 px | 0.36 | 1.63 | 195 |
| stroke 9 | 37 % → 60 % | 129.6 px | 0.36 | 1.62 | 199 |
| stroke 10 | 37 % → 59 % | 138.2 px | 0.36 | 1.59 | 210 |
| stroke 11 | 40 % → 63 % | 142.7 px | 0.36 | 1.58 | 240 |
| stroke 12 | 39 % → 64 % | 145.1 px | 0.36 | 1.66 | 197 |
| stroke 13 | 39 % → 66 % | 137.4 px | 0.36 | 1.68 | 162 |
| stroke 14 | 37 % → 61 % | 135.6 px | 0.36 | 1.64 | 282 |
| stroke 15 | 40 % → 65 % | 137.4 px | 0.36 | 1.62 | 196 |
| stroke 16 | 39 % → 63 % | 140.6 px | 0.36 | 1.62 | 264 |
| stroke 17 | 38 % → 62 % | 128.3 px | 0.36 | 1.60 | 207 |
| stroke 18 | 41 % → 65 % | 157.3 px | 0.36 | 1.59 | 208 |
| stroke 19 | 40 % → 59 % | 140.0 px | 0.36 | 1.46 | 202 |
| stroke 20 | 41 % → 53 % | 146.1 px | 0.36 | 1.29 | 230 |
| stroke 21 | 47 % → 53 % | 139.7 px | 0.36 | 1.12 | 239 |
| stroke 22 | 55 % → 51 % | 148.4 px | 0.36 | 0.94 | 179 |

Numbers say: wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #15 Ultramarine brush script — own sheet
own sheet 600 × 600 · Ink · 4 px · 13.7 s

![Brush Artist · Refs · #15 Ultramarine brush script — own sheet](Brush-Artist-Refs-15-Ultramarine-brush-script-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 40 % → 42 % | 8.9 px | 0.66 | 1.05 | 84 |
| stroke 2 | 40 % → 42 % | 8.9 px | 0.66 | 1.06 | 81 |
| stroke 3 | 40 % → 42 % | 9.5 px | 0.74 | 1.06 | 46 |
| stroke 4 | 42 % → 45 % | 10.1 px | 0.74 | 1.08 | 28 |
| stroke 5 | 44 % → 48 % | 9.7 px | 0.73 | 1.08 | 48 |
| stroke 6 | 42 % → 44 % | 9.5 px | 0.65 | 1.05 | 85 |
| stroke 7 | 43 % → 47 % | 9.2 px | 0.72 | 1.08 | 48 |
| stroke 8 | 38 % → 41 % | 9.3 px | 0.68 | 1.05 | 88 |
| stroke 9 | 40 % → 42 % | 9.2 px | 0.69 | 1.06 | 71 |
| stroke 10 | 36 % → 38 % | 9.9 px | 0.68 | 1.05 | 79 |
| stroke 11 | 42 % → 45 % | 9.6 px | 0.70 | 1.06 | 68 |
| stroke 12 | 39 % → 41 % | 9.4 px | 0.66 | 1.05 | 77 |
| stroke 13 | 45 % → 48 % | 10.2 px | 0.71 | 1.06 | 37 |
| stroke 14 | 38 % → 41 % | 9.9 px | 0.73 | 1.07 | 34 |
| stroke 15 | 37 % → 39 % | 9.1 px | 0.69 | 1.06 | 90 |
| stroke 16 | 42 % → 45 % | 9.4 px | 0.72 | 1.06 | 47 |
| stroke 17 | 41 % → 44 % | 7.1 px | 0.71 | 1.08 | 68 |
| stroke 18 | 43 % → 45 % | 9.2 px | 0.73 | 1.06 | 40 |
| stroke 19 | 39 % → 41 % | 8.9 px | 0.66 | 1.05 | 132 |
| stroke 20 | 41 % → 43 % | 9.4 px | 0.71 | 1.06 | 61 |
| stroke 21 | 40 % → 43 % | 9.9 px | 0.70 | 1.06 | 62 |
| stroke 22 | 42 % → 44 % | 8.5 px | 0.65 | 1.05 | 71 |
| stroke 23 | 40 % → 43 % | 10.1 px | 0.73 | 1.07 | 40 |
| stroke 24 | 38 % → 41 % | 8.8 px | 0.73 | 1.07 | 50 |
| stroke 25 | 41 % → 43 % | 9.8 px | 0.72 | 1.07 | 51 |
| stroke 26 | 46 % → 49 % | 9.3 px | 0.68 | 1.05 | 66 |
| stroke 27 | 43 % → 45 % | 8.8 px | 0.63 | 1.05 | 90 |
| stroke 28 | 44 % → 46 % | 9.1 px | 0.70 | 1.06 | 68 |
| stroke 29 | 36 % → 39 % | 10.6 px | 0.72 | 1.08 | 44 |
| stroke 30 | 39 % → 41 % | 8.7 px | 0.71 | 1.04 | 51 |
| stroke 31 | 43 % → 46 % | 10.3 px | 0.75 | 1.07 | 26 |
| stroke 32 | 42 % → 46 % | 9.5 px | 0.73 | 1.09 | 46 |
| stroke 33 | 35 % → 38 % | 10.9 px | 0.72 | 1.08 | 46 |
| stroke 34 | 40 % → 43 % | 9.8 px | 0.73 | 1.08 | 25 |
| stroke 35 | 36 % → 37 % | 9.4 px | 0.65 | 1.05 | 63 |

## Brush Artist · Refs · #18 Blue oil-stick scribbles — own sheet
own sheet 600 × 600 · Pastel · 10 px · 4.6 s

![Brush Artist · Refs · #18 Blue oil-stick scribbles — own sheet](Brush-Artist-Refs-18-Blue-oil-stick-scribbles-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 15 % → 31 % | 3.8 px | 0.49 | 2.11 | 203 |
| stroke 2 | 13 % → 37 % | 3.6 px | 0.49 | 2.73 | 211 |
| stroke 3 | 16 % → 26 % | 5.8 px | 0.49 | 1.66 | 268 |
| stroke 4 | 15 % → 29 % | 8.0 px | 0.49 | 1.88 | 257 |
| stroke 5 | 29 % → 34 % | 8.4 px | 0.49 | 1.19 | 270 |
| stroke 6 | 25 % → 26 % | 9.4 px | 0.49 | 1.02 | 203 |
| stroke 7 | 26 % → 32 % | 8.3 px | 0.49 | 1.24 | 214 |
| stroke 8 | 30 % → 30 % | 17.0 px | 0.49 | 1.00 | 249 |

Numbers say: wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #20 Orange-red crayon scribble — own sheet
own sheet 600 × 600 · Pastel · 14 px · 5.3 s

![Brush Artist · Refs · #20 Orange-red crayon scribble — own sheet](Brush-Artist-Refs-20-Orange-red-crayon-scribble-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 8 % → 18 % | 5.5 px | 0.59 | 2.46 | 270 |
| stroke 2 | 9 % → 23 % | 6.8 px | 0.59 | 2.48 | 263 |
| stroke 3 | 13 % → 21 % | 8.5 px | 0.59 | 1.64 | 214 |
| stroke 4 | 24 % → 32 % | 8.9 px | 0.59 | 1.34 | 257 |
| stroke 5 | 27 % → 27 % | 7.7 px | 0.59 | 1.00 | 233 |
| stroke 6 | 22 % → 22 % | 16.8 px | 0.59 | 1.00 | 286 |

Numbers say: wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #21 Gritty black contours — own sheet
own sheet 600 × 600 · Gouache · 12 px · 8.0 s

![Brush Artist · Refs · #21 Gritty black contours — own sheet](Brush-Artist-Refs-21-Gritty-black-contours-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 4 % → 5 % | 4.7 px | 0.37 | 1.13 | 212 |
| stroke 2 | 4 % → 3 % | 7.3 px | 0.37 | 0.60 | 265 |
| stroke 3 | 7 % → 4 % | 6.2 px | 0.37 | 0.56 | 158 |
| stroke 4 | 9 % → 4 % | 10.7 px | 0.37 | 0.51 | 217 |
| stroke 5 | 10 % → 4 % | 12.7 px | 0.37 | 0.42 | 219 |

## Brush Artist · Refs · #22 Bold black brush poster — own sheet
own sheet 600 × 600 · Ink · 20 px · 9.5 s

![Brush Artist · Refs · #22 Bold black brush poster — own sheet](Brush-Artist-Refs-22-Bold-black-brush-poster-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 22 % → 27 % | 36.4 px | 0.94 | 1.20 | 243 |
| stroke 2 | 27 % → 37 % | 41.5 px | 0.95 | 1.36 | 63 |
| stroke 3 | 28 % → 28 % | 43.6 px | 0.95 | 1.00 | 121 |
| stroke 4 | 27 % → 39 % | 53.8 px | 0.94 | 1.42 | 126 |
| stroke 5 | 25 % → 25 % | 43.0 px | 0.94 | 1.00 | 219 |

## Brush Artist · Refs · #23 Dry white on orange + black line — own sheet
own sheet 600 × 600 · Gouache · 50 px · 12.9 s

![Brush Artist · Refs · #23 Dry white on orange + black line — own sheet](Brush-Artist-Refs-23-Dry-white-on-orange-black-line-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 5 % → 10 % | 18.7 px | 0.42 | 1.89 | 378 |
| stroke 2 | 7 % → 9 % | 24.3 px | 0.42 | 1.35 | 457 |
| stroke 3 | 10 % → 10 % | 39.0 px | 0.42 | 0.92 | 309 |
| stroke 4 | 12 % → 11 % | 45.8 px | 0.42 | 0.95 | 316 |
| stroke 5 | 17 % → 14 % | 60.0 px | 0.42 | 0.82 | 327 |
| stroke 6 | 17 % → 15 % | 70.6 px | 0.42 | 0.86 | 340 |
| stroke 7 | 14 % → 14 % | 52.6 px | 0.41 | 1.00 | 385 |
| stroke 8 | 14 % → 13 % | 55.2 px | 0.41 | 0.91 | 296 |
| stroke 9 | 15 % → 14 % | 54.3 px | 0.41 | 0.93 | 217 |
| stroke 10 | 14 % → 14 % | 56.6 px | 0.41 | 0.97 | 222 |
| stroke 11 | 16 % → 15 % | 60.6 px | 0.41 | 0.92 | 225 |
| stroke 12 | 16 % → 15 % | 63.4 px | 0.41 | 0.94 | 261 |
| stroke 13 | 17 % → 16 % | 61.2 px | 0.41 | 0.97 | 246 |
| stroke 14 | 16 % → 16 % | 63.9 px | 0.41 | 0.97 | 217 |
| stroke 15 | 16 % → 14 % | 59.9 px | 0.41 | 0.87 | 190 |
| stroke 16 | 15 % → 12 % | 61.4 px | 0.41 | 0.78 | 202 |
| stroke 17 | 16 % → 11 % | 56.7 px | 0.41 | 0.68 | 218 |
| stroke 18 | 19 % → 11 % | 69.3 px | 0.41 | 0.60 | 210 |

Numbers say: wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #24 Picasso flat oil — own sheet
own sheet 600 × 600 · Oil · 34 px · 9.6 s

![Brush Artist · Refs · #24 Picasso flat oil — own sheet](Brush-Artist-Refs-24-Picasso-flat-oil-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 17 % → 46 % | 35.6 px | 0.23 | 2.73 | 325 |
| stroke 2 | 21 % → 49 % | 48.5 px | 0.24 | 2.38 | 363 |
| stroke 3 | 29 % → 60 % | 64.2 px | 0.23 | 2.05 | 182 |
| stroke 4 | 38 % → 66 % | 85.1 px | 0.23 | 1.75 | 216 |
| stroke 5 | 44 % → 72 % | 97.2 px | 0.23 | 1.63 | 207 |
| stroke 6 | 45 % → 67 % | 104.5 px | 0.23 | 1.50 | 212 |
| stroke 7 | 46 % → 68 % | 97.4 px | 0.23 | 1.46 | 172 |
| stroke 8 | 45 % → 68 % | 109.1 px | 0.23 | 1.51 | 245 |
| stroke 9 | 38 % → 64 % | 83.4 px | 0.23 | 1.69 | 219 |
| stroke 10 | 40 % → 63 % | 95.6 px | 0.23 | 1.58 | 224 |
| stroke 11 | 38 % → 62 % | 81.6 px | 0.23 | 1.62 | 200 |
| stroke 12 | 40 % → 63 % | 94.7 px | 0.23 | 1.60 | 196 |
| stroke 13 | 40 % → 70 % | 87.1 px | 0.23 | 1.76 | 202 |
| stroke 14 | 41 % → 71 % | 92.4 px | 0.23 | 1.74 | 162 |
| stroke 15 | 41 % → 64 % | 86.1 px | 0.23 | 1.58 | 199 |
| stroke 16 | 39 % → 56 % | 91.3 px | 0.23 | 1.43 | 196 |
| stroke 17 | 45 % → 50 % | 93.3 px | 0.23 | 1.12 | 187 |
| stroke 18 | 44 % → 44 % | 106.7 px | 0.23 | 1.00 | 197 |

Numbers say: wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #25 Yellow heavy flat stroke — own sheet
own sheet 600 × 600 · Heavy acrylic · 110 px · 4.2 s

![Brush Artist · Refs · #25 Yellow heavy flat stroke — own sheet](Brush-Artist-Refs-25-Yellow-heavy-flat-stroke-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 19 % → 19 % | 110.5 px | 0.18 | 0.98 | 864 |

## Brush Artist · Refs · #27 Orange impasto swatch — own sheet
own sheet 600 × 600 · Heavy acrylic · 60 px · 7.0 s

![Brush Artist · Refs · #27 Orange impasto swatch — own sheet](Brush-Artist-Refs-27-Orange-impasto-swatch-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 9 % → 29 % | 68.9 px | 0.35 | 3.19 | 104 |
| stroke 2 | 8 % → 41 % | 72.3 px | 0.34 | 4.94 | 73 |
| stroke 3 | 29 % → 45 % | 285.3 px | 0.35 | 1.52 | 62 |
| stroke 4 | 11 % → 15 % | 77.4 px | 0.34 | 1.39 | 86 |
| stroke 5 | 17 % → 33 % | 63.6 px | 0.33 | 1.90 | 78 |
| stroke 6 | 20 % → 40 % | 166.9 px | 0.34 | 1.96 | 98 |
| stroke 7 | 9 % → 18 % | 80.4 px | 0.34 | 2.03 | 83 |
| stroke 8 | 38 % → 44 % | 387.7 px | 0.34 | 1.16 | 70 |
| stroke 9 | 40 % → 40 % | 195.9 px | 0.34 | 1.00 | 101 |
| stroke 10 | 36 % → 38 % | 330.2 px | 0.33 | 1.03 | 66 |

Numbers say: wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #28 Miles Davis black lines — own sheet
own sheet 600 × 600 · Ink · 22 px · 9.6 s

![Brush Artist · Refs · #28 Miles Davis black lines — own sheet](Brush-Artist-Refs-28-Miles-Davis-black-lines-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 22 % → 32 % | 36.6 px | 0.88 | 1.42 | 243 |
| stroke 2 | 28 % → 49 % | 38.3 px | 0.88 | 1.73 | 177 |
| stroke 3 | 39 % → 44 % | 75.1 px | 0.88 | 1.12 | 149 |
| stroke 4 | 42 % → 48 % | 83.7 px | 0.88 | 1.15 | 280 |
| stroke 5 | 55 % → 55 % | 109.9 px | 0.88 | 1.00 | 291 |

Numbers say: wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #29 Shrigley magenta asterisk — own sheet
own sheet 600 × 600 · Watercolor · 70 px · 9.6 s

![Brush Artist · Refs · #29 Shrigley magenta asterisk — own sheet](Brush-Artist-Refs-29-Shrigley-magenta-asterisk-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 13 % → 37 % | 46.6 px | 0.72 | 2.85 | 249 |
| stroke 2 | 12 % → 12 % | 87.1 px | 0.71 | 1.00 | 282 |
| stroke 3 | 28 % → 37 % | 100.9 px | 0.72 | 1.31 | 415 |
| stroke 4 | 23 % → 23 % | 163.9 px | 0.71 | 1.02 | 405 |

Numbers say: wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #30 Red gouache face patch — own sheet
own sheet 600 × 600 · Gouache · 60 px · 17.2 s

![Brush Artist · Refs · #30 Red gouache face patch — own sheet](Brush-Artist-Refs-30-Red-gouache-face-patch-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 12 % → 37 % | 51.5 px | 0.53 | 3.22 | 250 |
| stroke 2 | 15 % → 40 % | 74.6 px | 0.53 | 2.72 | 205 |
| stroke 3 | 24 % → 50 % | 116.0 px | 0.53 | 2.06 | 296 |
| stroke 4 | 27 % → 51 % | 134.1 px | 0.53 | 1.93 | 246 |
| stroke 5 | 34 % → 60 % | 159.9 px | 0.53 | 1.77 | 234 |
| stroke 6 | 35 % → 61 % | 178.3 px | 0.53 | 1.76 | 275 |
| stroke 7 | 34 % → 59 % | 160.9 px | 0.54 | 1.73 | 268 |
| stroke 8 | 34 % → 56 % | 162.5 px | 0.53 | 1.65 | 255 |
| stroke 9 | 36 % → 60 % | 173.1 px | 0.53 | 1.66 | 208 |
| stroke 10 | 38 % → 62 % | 196.8 px | 0.53 | 1.63 | 203 |
| stroke 11 | 37 % → 61 % | 182.5 px | 0.53 | 1.66 | 229 |
| stroke 12 | 36 % → 58 % | 178.3 px | 0.53 | 1.62 | 266 |
| stroke 13 | 33 % → 46 % | 156.5 px | 0.53 | 1.39 | 224 |
| stroke 14 | 33 % → 41 % | 157.7 px | 0.53 | 1.25 | 284 |
| stroke 15 | 33 % → 37 % | 153.4 px | 0.53 | 1.12 | 256 |
| stroke 16 | 39 % → 39 % | 184.9 px | 0.53 | 0.99 | 243 |

Numbers say: wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #31 Warhol blotted line — own sheet
own sheet 600 × 600 · Ink · 6 px · 7.1 s

![Brush Artist · Refs · #31 Warhol blotted line — own sheet](Brush-Artist-Refs-31-Warhol-blotted-line-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 21 % → 42 % | 15.8 px | 0.82 | 1.98 | 119 |
| stroke 2 | 17 % → 23 % | 15.9 px | 0.82 | 1.34 | 96 |
| stroke 3 | 24 % → 25 % | 25.1 px | 0.81 | 1.02 | 117 |
| stroke 4 | 31 % → 40 % | 31.9 px | 0.82 | 1.28 | 84 |
| stroke 5 | 35 % → 44 % | 36.4 px | 0.82 | 1.23 | 119 |
| stroke 6 | 32 % → 33 % | 26.7 px | 0.81 | 1.03 | 90 |

Numbers say: wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #32 Thick orange swipes — own sheet
own sheet 600 × 600 · Heavy acrylic · 90 px · 5.2 s

![Brush Artist · Refs · #32 Thick orange swipes — own sheet](Brush-Artist-Refs-32-Thick-orange-swipes-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 15 % → 29 % | 91.7 px | 0.03 | 1.91 | 422 |
| stroke 2 | 28 % → 40 % | 188.8 px | 0.03 | 1.44 | 484 |
| stroke 3 | 30 % → 29 % | 190.2 px | 0.03 | 0.98 | 382 |

Numbers say: wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #33 Red wet-in-wet band — own sheet
own sheet 600 × 600 · Watercolor · 80 px · 14.5 s

![Brush Artist · Refs · #33 Red wet-in-wet band — own sheet](Brush-Artist-Refs-33-Red-wet-in-wet-band-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 23 % → 57 % | 88.2 px | 0.61 | 2.46 | 734 |
| stroke 2 | 30 % → 52 % | 243.9 px | 0.61 | 1.73 | 188 |
| stroke 3 | 37 % → 54 % | 356.6 px | 0.61 | 1.47 | 188 |
| stroke 4 | 42 % → 61 % | 412.6 px | 0.62 | 1.43 | 134 |
| stroke 5 | 42 % → 55 % | 354.2 px | 0.61 | 1.33 | 138 |
| stroke 6 | 42 % → 47 % | 321.5 px | 0.60 | 1.11 | 165 |

Numbers say: wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #34 Magenta oil patches — own sheet
own sheet 600 × 600 · Oil · 60 px · 7.3 s

![Brush Artist · Refs · #34 Magenta oil patches — own sheet](Brush-Artist-Refs-34-Magenta-oil-patches-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 10 % → 46 % | 68.9 px | 0.13 | 4.68 | 210 |
| stroke 2 | 11 % → 32 % | 71.2 px | 0.13 | 3.02 | 143 |
| stroke 3 | 9 % → 40 % | 71.5 px | 0.13 | 4.71 | 108 |
| stroke 4 | 18 % → 25 % | 149.6 px | 0.13 | 1.37 | 90 |
| stroke 5 | 27 % → 39 % | 145.1 px | 0.12 | 1.43 | 143 |
| stroke 6 | 22 % → 41 % | 187.6 px | 0.13 | 1.86 | 90 |
| stroke 7 | 34 % → 40 % | 268.4 px | 0.13 | 1.18 | 118 |
| stroke 8 | 36 % → 43 % | 256.5 px | 0.13 | 1.19 | 140 |
| stroke 9 | 26 % → 28 % | 170.2 px | 0.13 | 1.08 | 141 |
| stroke 10 | 31 % → 31 % | 275.9 px | 0.13 | 1.00 | 94 |
| stroke 11 | 40 % → 40 % | 359.9 px | 0.13 | 1.00 | 99 |
| stroke 12 | 29 % → 29 % | 205.9 px | 0.13 | 1.00 | 99 |

Numbers say: wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #35 Red band with runs — own sheet
own sheet 600 × 600 · Watercolor · 70 px · 10.1 s

![Brush Artist · Refs · #35 Red band with runs — own sheet](Brush-Artist-Refs-35-Red-band-with-runs-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 21 % → 35 % | 77.5 px | 0.47 | 1.69 | 442 |

Numbers say: wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #36 Magenta letters flat brush — own sheet
own sheet 600 × 600 · Gouache · 36 px · 18.2 s

![Brush Artist · Refs · #36 Magenta letters flat brush — own sheet](Brush-Artist-Refs-36-Magenta-letters-flat-brush-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 20 % → 39 % | 59.1 px | 0.50 | 1.95 | 41 |
| stroke 2 | 20 % → 32 % | 46.7 px | 0.50 | 1.59 | 53 |
| stroke 3 | 29 % → 54 % | 86.9 px | 0.50 | 1.86 | 43 |
| stroke 4 | 26 % → 44 % | 51.3 px | 0.50 | 1.67 | 168 |
| stroke 5 | 33 % → 55 % | 96.2 px | 0.50 | 1.67 | 115 |
| stroke 6 | 42 % → 56 % | 242.7 px | 0.50 | 1.33 | 27 |
| stroke 7 | 30 % → 44 % | 56.8 px | 0.50 | 1.45 | 173 |
| stroke 8 | 31 % → 53 % | 98.5 px | 0.50 | 1.68 | 125 |
| stroke 9 | 38 % → 51 % | 158.3 px | 0.50 | 1.33 | 57 |
| stroke 10 | 37 % → 64 % | 106.7 px | 0.50 | 1.72 | 116 |
| stroke 11 | 39 % → 62 % | 225.8 px | 0.50 | 1.58 | 31 |
| stroke 12 | 43 % → 56 % | 81.9 px | 0.50 | 1.29 | 209 |
| stroke 13 | 33 % → 46 % | 117.7 px | 0.50 | 1.43 | 53 |
| stroke 14 | 35 % → 52 % | 134.5 px | 0.50 | 1.47 | 94 |
| stroke 15 | 38 % → 56 % | 108.6 px | 0.50 | 1.49 | 189 |
| stroke 16 | 41 % → 50 % | 232.0 px | 0.50 | 1.23 | 42 |
| stroke 17 | 44 % → 52 % | 81.7 px | 0.50 | 1.19 | 274 |
| stroke 18 | 27 % → 36 % | 97.6 px | 0.50 | 1.35 | 82 |
| stroke 19 | 40 % → 39 % | 117.2 px | 0.50 | 0.96 | 75 |
| stroke 20 | 45 % → 45 % | 132.3 px | 0.50 | 0.99 | 78 |
| stroke 21 | 41 % → 39 % | 78.7 px | 0.50 | 0.96 | 200 |

Numbers say: wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #37 Oil still life dabs — own sheet
own sheet 600 × 600 · Oil · 40 px · 6.9 s

![Brush Artist · Refs · #37 Oil still life dabs — own sheet](Brush-Artist-Refs-37-Oil-still-life-dabs-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 8 % → 8 % | 50.5 px | 0.39 | 1.01 | 102 |
| stroke 2 | 7 % → 30 % | 52.7 px | 0.39 | 4.05 | 39 |
| stroke 3 | 14 % → 39 % | 109.5 px | 0.39 | 2.81 | 44 |
| stroke 4 | 10 % → 10 % | 47.7 px | 0.39 | 1.01 | 86 |
| stroke 5 | 7 % → 13 % | 51.7 px | 0.39 | 1.78 | 50 |
| stroke 6 | 14 % → 33 % | 90.8 px | 0.39 | 2.32 | 96 |
| stroke 7 | 13 % → 29 % | 144.0 px | 0.39 | 2.16 | 29 |
| stroke 8 | 11 % → 18 % | 117.7 px | 0.39 | 1.62 | 52 |
| stroke 9 | 15 % → 17 % | 79.1 px | 0.38 | 1.09 | 64 |
| stroke 10 | 23 % → 29 % | 117.3 px | 0.38 | 1.28 | 53 |
| stroke 11 | 27 % → 33 % | 223.3 px | 0.39 | 1.23 | 35 |
| stroke 12 | 23 % → 25 % | 253.7 px | 0.39 | 1.07 | 24 |
| stroke 13 | 19 % → 19 % | 189.1 px | 0.40 | 1.01 | 28 |
| stroke 14 | 20 % → 20 % | 163.8 px | 0.39 | 1.01 | 37 |

Numbers say: wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #38 Sanguine drawing — own sheet
own sheet 600 × 600 · Pastel · 6 px · 3.6 s

![Brush Artist · Refs · #38 Sanguine drawing — own sheet](Brush-Artist-Refs-38-Sanguine-drawing-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 3 % → 14 % | 2.9 px | 0.57 | 5.29 | 14 |
| stroke 2 | 3 % → 7 % | 2.9 px | 0.57 | 2.89 | 10 |
| stroke 3 | 3 % → 9 % | 2.9 px | 0.57 | 3.40 | 10 |
| stroke 4 | 2 % → 17 % | 2.7 px | 0.57 | 7.20 | 6 |
| stroke 5 | 2 % → 7 % | 2.7 px | 0.57 | 3.03 | 10 |
| stroke 6 | 3 % → 19 % | 3.4 px | 0.57 | 6.31 | 13 |
| stroke 7 | 5 % → 14 % | 5.2 px | 0.57 | 3.07 | 13 |
| stroke 8 | 4 % → 16 % | 4.7 px | 0.57 | 3.79 | 18 |
| stroke 9 | 3 % → 7 % | 2.9 px | 0.57 | 2.66 | 15 |
| stroke 10 | 4 % → 16 % | 4.7 px | 0.57 | 3.83 | 6 |
| stroke 11 | 3 % → 4 % | 2.9 px | 0.57 | 1.61 | 12 |
| stroke 12 | 4 % → 15 % | 4.8 px | 0.57 | 3.58 | 12 |
| stroke 13 | 8 % → 17 % | 8.9 px | 0.57 | 2.23 | 8 |
| stroke 14 | 4 % → 14 % | 4.9 px | 0.57 | 3.19 | 14 |
| stroke 15 | 9 % → 18 % | 10.7 px | 0.57 | 1.86 | 12 |
| stroke 16 | 6 % → 16 % | 6.6 px | 0.57 | 2.71 | 14 |
| stroke 17 | 4 % → 9 % | 4.4 px | 0.57 | 2.25 | 12 |
| stroke 18 | 3 % → 5 % | 2.9 px | 0.57 | 1.85 | 10 |
| stroke 19 | 6 % → 16 % | 6.9 px | 0.57 | 2.68 | 6 |
| stroke 20 | 8 % → 14 % | 9.2 px | 0.57 | 1.70 | 10 |
| stroke 21 | 4 % → 4 % | 4.3 px | 0.57 | 1.00 | 9 |
| stroke 22 | 8 % → 13 % | 8.6 px | 0.57 | 1.79 | 11 |
| stroke 23 | 7 % → 12 % | 8.3 px | 0.57 | 1.61 | 9 |
| stroke 24 | 4 % → 7 % | 4.7 px | 0.57 | 1.71 | 12 |
| stroke 25 | 8 % → 14 % | 8.7 px | 0.57 | 1.84 | 6 |
| stroke 26 | 6 % → 8 % | 6.5 px | 0.57 | 1.34 | 10 |
| stroke 27 | 4 % → 4 % | 4.3 px | 0.57 | 1.10 | 10 |
| stroke 28 | 7 % → 11 % | 8.2 px | 0.57 | 1.59 | 10 |
| stroke 29 | 8 % → 17 % | 8.8 px | 0.57 | 2.21 | 12 |
| stroke 30 | 13 % → 17 % | 14.9 px | 0.57 | 1.29 | 14 |
| stroke 31 | 5 % → 6 % | 5.4 px | 0.57 | 1.29 | 11 |
| stroke 32 | 10 % → 13 % | 11.8 px | 0.57 | 1.24 | 9 |
| stroke 33 | 7 % → 8 % | 8.5 px | 0.57 | 1.07 | 14 |
| stroke 34 | 11 % → 14 % | 12.0 px | 0.57 | 1.36 | 12 |
| stroke 35 | 9 % → 14 % | 10.0 px | 0.57 | 1.61 | 12 |
| stroke 36 | 10 % → 13 % | 11.4 px | 0.57 | 1.26 | 11 |
| stroke 37 | 9 % → 16 % | 10.5 px | 0.57 | 1.71 | 15 |
| stroke 38 | 13 % → 19 % | 14.8 px | 0.57 | 1.48 | 8 |
| stroke 39 | 14 % → 17 % | 15.7 px | 0.57 | 1.21 | 12 |
| stroke 40 | 6 % → 7 % | 7.2 px | 0.57 | 1.14 | 13 |
| stroke 41 | 16 % → 16 % | 17.7 px | 0.57 | 1.01 | 7 |
| stroke 42 | 14 % → 16 % | 15.2 px | 0.57 | 1.17 | 12 |
| stroke 43 | 10 % → 12 % | 11.6 px | 0.57 | 1.17 | 9 |
| stroke 44 | 12 % → 15 % | 14.3 px | 0.57 | 1.22 | 10 |
| stroke 45 | 2 % → 2 % | 2.7 px | 0.57 | 1.00 | 17 |
| stroke 46 | 16 % → 16 % | 18.5 px | 0.57 | 1.00 | 7 |
| stroke 47 | 13 % → 13 % | 15.0 px | 0.57 | 1.00 | 9 |
| stroke 48 | 12 % → 13 % | 14.3 px | 0.57 | 1.07 | 7 |
| stroke 49 | 19 % → 19 % | 21.5 px | 0.57 | 1.00 | 8 |
| stroke 50 | 10 % → 10 % | 11.6 px | 0.57 | 1.00 | 8 |

Numbers say: wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #39 Very thick impasto — own sheet
own sheet 600 × 600 · Heavy acrylic · 60 px · 9.3 s

![Brush Artist · Refs · #39 Very thick impasto — own sheet](Brush-Artist-Refs-39-Very-thick-impasto-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 27 % → 39 % | 61.5 px | 0.43 | 1.45 | 497 |
| stroke 2 | 32 % → 50 % | 96.9 px | 0.44 | 1.56 | 491 |
| stroke 3 | 38 % → 52 % | 128.8 px | 0.44 | 1.35 | 376 |
| stroke 4 | 32 % → 46 % | 93.6 px | 0.44 | 1.43 | 451 |
| stroke 5 | 43 % → 43 % | 108.0 px | 0.44 | 0.99 | 424 |

Numbers say: wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #40 Watercolour blooms — own sheet
own sheet 600 × 600 · Watercolor · 90 px · 10.8 s

![Brush Artist · Refs · #40 Watercolour blooms — own sheet](Brush-Artist-Refs-40-Watercolour-blooms-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 21 % → 25 % | 92.4 px | 0.13 | 1.20 | 1166 |

## Brush Artist · Refs · #41 Coloured pencil hatching — own sheet
own sheet 600 × 600 · Pastel · 4 px · 4.4 s

![Brush Artist · Refs · #41 Coloured pencil hatching — own sheet](Brush-Artist-Refs-41-Coloured-pencil-hatching-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 3 % → 13 % | 2.2 px | 0.35 | 4.64 | 8 |
| stroke 2 | 3 % → 7 % | 2.3 px | 0.35 | 2.29 | 6 |
| stroke 3 | 2 % → 11 % | 1.9 px | 0.35 | 4.38 | 12 |
| stroke 4 | 3 % → 19 % | 2.1 px | 0.35 | 6.73 | 7 |
| stroke 5 | 4 % → 7 % | 2.9 px | 0.35 | 1.83 | 8 |
| stroke 6 | 3 % → 13 % | 2.3 px | 0.35 | 4.19 | 8 |
| stroke 7 | 3 % → 15 % | 2.6 px | 0.35 | 4.43 | 7 |
| stroke 8 | 3 % → 12 % | 2.1 px | 0.35 | 4.20 | 11 |
| stroke 9 | 5 % → 11 % | 3.6 px | 0.35 | 2.27 | 9 |
| stroke 10 | 5 % → 15 % | 3.8 px | 0.35 | 2.99 | 9 |
| stroke 11 | 4 % → 13 % | 3.0 px | 0.35 | 3.28 | 10 |
| stroke 12 | 3 % → 3 % | 2.1 px | 0.35 | 1.00 | 11 |
| stroke 13 | 7 % → 17 % | 5.2 px | 0.35 | 2.45 | 7 |
| stroke 14 | 3 % → 13 % | 2.4 px | 0.35 | 4.19 | 15 |
| stroke 15 | 6 % → 12 % | 4.4 px | 0.35 | 2.09 | 12 |
| stroke 16 | 7 % → 11 % | 5.1 px | 0.35 | 1.61 | 7 |
| stroke 17 | 3 % → 3 % | 2.1 px | 0.35 | 1.00 | 13 |
| stroke 18 | 5 % → 8 % | 3.6 px | 0.35 | 1.65 | 9 |
| stroke 19 | 5 % → 13 % | 3.8 px | 0.35 | 2.72 | 9 |
| stroke 20 | 5 % → 14 % | 3.7 px | 0.35 | 2.92 | 11 |
| stroke 21 | 4 % → 13 % | 3.2 px | 0.35 | 3.20 | 8 |
| stroke 22 | 9 % → 16 % | 6.8 px | 0.35 | 1.77 | 7 |
| stroke 23 | 9 % → 13 % | 6.5 px | 0.35 | 1.55 | 10 |
| stroke 24 | 6 % → 14 % | 4.7 px | 0.35 | 2.18 | 8 |
| stroke 25 | 5 % → 10 % | 3.5 px | 0.35 | 2.27 | 11 |
| stroke 26 | 3 % → 6 % | 2.7 px | 0.35 | 1.81 | 9 |
| stroke 27 | 3 % → 7 % | 2.3 px | 0.35 | 2.26 | 9 |
| stroke 28 | 6 % → 10 % | 4.5 px | 0.35 | 1.70 | 7 |
| stroke 29 | 3 % → 13 % | 2.4 px | 0.35 | 4.21 | 9 |
| stroke 30 | 6 % → 9 % | 4.4 px | 0.35 | 1.46 | 11 |
| stroke 31 | 7 % → 14 % | 5.1 px | 0.35 | 2.14 | 12 |
| stroke 32 | 3 % → 6 % | 2.5 px | 0.35 | 1.79 | 6 |
| stroke 33 | 6 % → 11 % | 5.0 px | 0.35 | 1.67 | 11 |
| stroke 34 | 3 % → 6 % | 2.6 px | 0.35 | 1.73 | 6 |
| stroke 35 | 7 % → 14 % | 5.0 px | 0.35 | 2.09 | 11 |
| stroke 36 | 5 % → 5 % | 3.7 px | 0.35 | 1.01 | 7 |
| stroke 37 | 7 % → 15 % | 5.2 px | 0.35 | 2.15 | 10 |
| stroke 38 | 8 % → 13 % | 5.8 px | 0.35 | 1.66 | 11 |
| stroke 39 | 7 % → 11 % | 5.1 px | 0.35 | 1.67 | 10 |
| stroke 40 | 8 % → 18 % | 6.2 px | 0.35 | 2.21 | 8 |
| stroke 41 | 9 % → 13 % | 6.9 px | 0.35 | 1.48 | 11 |
| stroke 42 | 10 % → 17 % | 7.7 px | 0.35 | 1.73 | 32 |
| stroke 43 | 5 % → 9 % | 3.9 px | 0.35 | 1.66 | 12 |
| stroke 44 | 10 % → 13 % | 7.3 px | 0.35 | 1.40 | 5 |
| stroke 45 | 13 % → 18 % | 9.9 px | 0.35 | 1.35 | 7 |
| stroke 46 | 5 % → 7 % | 3.6 px | 0.34 | 1.41 | 6 |
| stroke 47 | 11 % → 13 % | 8.0 px | 0.35 | 1.20 | 7 |
| stroke 48 | 12 % → 16 % | 9.2 px | 0.35 | 1.34 | 8 |
| stroke 49 | 6 % → 9 % | 4.2 px | 0.35 | 1.66 | 5 |
| stroke 50 | 7 % → 7 % | 5.2 px | 0.34 | 1.00 | 6 |
| stroke 51 | 8 % → 15 % | 6.4 px | 0.35 | 1.74 | 12 |
| stroke 52 | 12 % → 14 % | 9.1 px | 0.35 | 1.19 | 11 |
| stroke 53 | 11 % → 14 % | 8.1 px | 0.35 | 1.36 | 11 |
| stroke 54 | 10 % → 14 % | 7.4 px | 0.35 | 1.47 | 12 |
| stroke 55 | 11 % → 14 % | 8.2 px | 0.35 | 1.33 | 11 |
| stroke 56 | 11 % → 12 % | 8.4 px | 0.35 | 1.11 | 12 |
| stroke 57 | 9 % → 13 % | 7.1 px | 0.35 | 1.37 | 8 |
| stroke 58 | 10 % → 11 % | 7.7 px | 0.35 | 1.14 | 17 |
| stroke 59 | 11 % → 13 % | 8.4 px | 0.35 | 1.18 | 8 |
| stroke 60 | 16 % → 20 % | 11.9 px | 0.35 | 1.26 | 6 |
| stroke 61 | 19 % → 20 % | 14.5 px | 0.35 | 1.04 | 6 |
| stroke 62 | 10 % → 10 % | 7.3 px | 0.35 | 1.00 | 8 |
| stroke 63 | 11 % → 12 % | 8.7 px | 0.35 | 1.07 | 11 |
| stroke 64 | 14 % → 14 % | 10.7 px | 0.35 | 1.02 | 8 |
| stroke 65 | 15 % → 15 % | 11.5 px | 0.35 | 1.00 | 6 |
| stroke 66 | 14 % → 14 % | 10.7 px | 0.35 | 1.00 | 7 |
| stroke 67 | 12 % → 12 % | 8.8 px | 0.35 | 1.06 | 7 |
| stroke 68 | 5 % → 9 % | 3.6 px | 0.35 | 1.88 | 16 |
| stroke 69 | 5 % → 5 % | 4.1 px | 0.35 | 1.00 | 9 |
| stroke 70 | 10 % → 13 % | 7.4 px | 0.35 | 1.28 | 8 |
| stroke 71 | 9 % → 11 % | 7.1 px | 0.35 | 1.15 | 19 |
| stroke 72 | 5 % → 7 % | 4.2 px | 0.35 | 1.23 | 15 |
| stroke 73 | 12 % → 12 % | 9.3 px | 0.35 | 1.00 | 7 |
| stroke 74 | 14 % → 14 % | 10.8 px | 0.35 | 1.00 | 11 |
| stroke 75 | 15 % → 15 % | 11.4 px | 0.35 | 1.00 | 8 |
| stroke 76 | 14 % → 14 % | 10.5 px | 0.35 | 1.00 | 8 |
| stroke 77 | 7 % → 10 % | 5.4 px | 0.35 | 1.34 | 8 |
| stroke 78 | 9 % → 9 % | 7.0 px | 0.35 | 1.00 | 5 |
| stroke 79 | 7 % → 7 % | 5.7 px | 0.35 | 1.00 | 12 |
| stroke 80 | 11 % → 11 % | 8.3 px | 0.35 | 1.00 | 13 |

Numbers say: wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #42 Oil pastel shaggy — own sheet
own sheet 600 × 600 · Pastel · 18 px · 4.2 s

![Brush Artist · Refs · #42 Oil pastel shaggy — own sheet](Brush-Artist-Refs-42-Oil-pastel-shaggy-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 5 % → 27 % | 8.0 px | 0.28 | 5.73 | 24 |
| stroke 2 | 5 % → 24 % | 8.6 px | 0.28 | 4.69 | 16 |
| stroke 3 | 5 % → 29 % | 8.9 px | 0.28 | 5.42 | 14 |
| stroke 4 | 5 % → 11 % | 8.8 px | 0.28 | 2.08 | 18 |
| stroke 5 | 6 % → 11 % | 9.9 px | 0.28 | 1.85 | 17 |
| stroke 6 | 8 % → 37 % | 13.9 px | 0.29 | 4.44 | 14 |
| stroke 7 | 11 % → 31 % | 17.6 px | 0.28 | 2.90 | 18 |
| stroke 8 | 7 % → 38 % | 11.4 px | 0.28 | 5.55 | 19 |
| stroke 9 | 8 % → 21 % | 13.9 px | 0.28 | 2.53 | 18 |
| stroke 10 | 8 % → 18 % | 13.2 px | 0.28 | 2.32 | 19 |
| stroke 11 | 6 % → 27 % | 9.4 px | 0.28 | 4.74 | 20 |
| stroke 12 | 8 % → 19 % | 13.6 px | 0.28 | 2.29 | 18 |
| stroke 13 | 13 % → 24 % | 21.0 px | 0.28 | 1.92 | 18 |
| stroke 14 | 5 % → 23 % | 7.9 px | 0.28 | 4.77 | 15 |
| stroke 15 | 5 % → 24 % | 9.0 px | 0.29 | 4.38 | 18 |
| stroke 16 | 9 % → 21 % | 15.7 px | 0.29 | 2.18 | 15 |
| stroke 17 | 17 % → 39 % | 27.9 px | 0.29 | 2.34 | 13 |
| stroke 18 | 14 % → 25 % | 22.8 px | 0.29 | 1.79 | 15 |
| stroke 19 | 15 % → 32 % | 24.9 px | 0.28 | 2.09 | 13 |
| stroke 20 | 21 % → 39 % | 35.1 px | 0.28 | 1.85 | 14 |
| stroke 21 | 9 % → 16 % | 14.4 px | 0.28 | 1.88 | 16 |
| stroke 22 | 14 % → 17 % | 23.9 px | 0.28 | 1.20 | 16 |
| stroke 23 | 12 % → 17 % | 20.6 px | 0.29 | 1.34 | 16 |
| stroke 24 | 18 % → 26 % | 30.0 px | 0.29 | 1.44 | 22 |
| stroke 25 | 20 % → 34 % | 32.6 px | 0.28 | 1.74 | 18 |
| stroke 26 | 6 % → 14 % | 9.2 px | 0.28 | 2.43 | 17 |
| stroke 27 | 18 % → 26 % | 30.4 px | 0.29 | 1.41 | 18 |
| stroke 28 | 14 % → 24 % | 23.7 px | 0.28 | 1.68 | 14 |
| stroke 29 | 9 % → 27 % | 14.9 px | 0.29 | 3.01 | 16 |
| stroke 30 | 15 % → 36 % | 24.9 px | 0.29 | 2.43 | 15 |
| stroke 31 | 14 % → 17 % | 23.3 px | 0.28 | 1.23 | 20 |
| stroke 32 | 16 % → 29 % | 27.0 px | 0.29 | 1.82 | 18 |
| stroke 33 | 15 % → 16 % | 24.5 px | 0.29 | 1.09 | 17 |
| stroke 34 | 19 % → 27 % | 31.4 px | 0.28 | 1.44 | 16 |
| stroke 35 | 26 % → 36 % | 42.5 px | 0.28 | 1.40 | 17 |
| stroke 36 | 25 % → 34 % | 41.0 px | 0.28 | 1.36 | 15 |
| stroke 37 | 12 % → 12 % | 19.3 px | 0.28 | 1.03 | 12 |
| stroke 38 | 19 % → 25 % | 31.7 px | 0.28 | 1.30 | 12 |
| stroke 39 | 16 % → 22 % | 27.3 px | 0.28 | 1.37 | 18 |
| stroke 40 | 22 % → 31 % | 36.6 px | 0.28 | 1.38 | 11 |
| stroke 41 | 32 % → 36 % | 53.1 px | 0.28 | 1.12 | 14 |
| stroke 42 | 23 % → 30 % | 38.1 px | 0.29 | 1.29 | 17 |
| stroke 43 | 12 % → 12 % | 20.3 px | 0.28 | 1.00 | 16 |
| stroke 44 | 30 % → 37 % | 48.9 px | 0.28 | 1.26 | 18 |
| stroke 45 | 16 % → 16 % | 26.2 px | 0.28 | 1.00 | 14 |
| stroke 46 | 29 % → 34 % | 47.9 px | 0.29 | 1.15 | 14 |
| stroke 47 | 38 % → 41 % | 62.0 px | 0.28 | 1.10 | 18 |
| stroke 48 | 29 % → 36 % | 47.8 px | 0.29 | 1.27 | 14 |
| stroke 49 | 27 % → 30 % | 45.1 px | 0.29 | 1.11 | 21 |
| stroke 50 | 38 % → 40 % | 63.4 px | 0.28 | 1.06 | 13 |
| stroke 51 | 16 % → 16 % | 26.0 px | 0.28 | 1.00 | 18 |
| stroke 52 | 37 % → 38 % | 62.4 px | 0.29 | 1.01 | 16 |
| stroke 53 | 22 % → 26 % | 36.9 px | 0.28 | 1.18 | 17 |
| stroke 54 | 17 % → 19 % | 29.0 px | 0.29 | 1.09 | 15 |
| stroke 55 | 15 % → 15 % | 25.0 px | 0.28 | 1.00 | 13 |
| stroke 56 | 13 % → 14 % | 21.6 px | 0.28 | 1.08 | 16 |
| stroke 57 | 23 % → 23 % | 37.7 px | 0.29 | 1.00 | 20 |
| stroke 58 | 28 % → 29 % | 46.1 px | 0.28 | 1.05 | 16 |
| stroke 59 | 40 % → 40 % | 67.3 px | 0.28 | 1.00 | 13 |
| stroke 60 | 22 % → 22 % | 35.6 px | 0.28 | 1.00 | 15 |

Numbers say: wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #43 Dragged black ink blocks — own sheet
own sheet 600 × 600 · Gouache · 70 px · 15.0 s

![Brush Artist · Refs · #43 Dragged black ink blocks — own sheet](Brush-Artist-Refs-43-Dragged-black-ink-blocks-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 16 % → 12 % | 37.3 px | 0.46 | 0.73 | 671 |
| stroke 2 | 16 % → 13 % | 58.0 px | 0.46 | 0.78 | 732 |
| stroke 3 | 20 % → 16 % | 72.4 px | 0.46 | 0.79 | 691 |
| stroke 4 | 20 % → 16 % | 70.6 px | 0.46 | 0.77 | 795 |
| stroke 5 | 24 % → 14 % | 56.0 px | 0.46 | 0.57 | 696 |

## Brush Artist · Refs · #44 Blue looping ribbon — own sheet
own sheet 600 × 600 · Oil · 80 px · 11.7 s

![Brush Artist · Refs · #44 Blue looping ribbon — own sheet](Brush-Artist-Refs-44-Blue-looping-ribbon-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 32 % → 32 % | 42.2 px | 0.78 | 1.00 | 4398 |

## Brush Artist · Refs · #45 Soft pastel pepper — own sheet
own sheet 600 × 600 · Pastel · 40 px · 9.5 s

![Brush Artist · Refs · #45 Soft pastel pepper — own sheet](Brush-Artist-Refs-45-Soft-pastel-pepper-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 10 % → 39 % | 11.3 px | 0.48 | 3.73 | 553 |
| stroke 2 | 18 % → 34 % | 21.3 px | 0.49 | 1.86 | 584 |
| stroke 3 | 25 % → 37 % | 17.6 px | 0.49 | 1.45 | 453 |
| stroke 4 | 24 % → 35 % | 30.5 px | 0.49 | 1.42 | 508 |
| stroke 5 | 30 % → 30 % | 21.2 px | 0.49 | 1.00 | 369 |
| stroke 6 | 35 % → 44 % | 22.5 px | 0.48 | 1.25 | 513 |
| stroke 7 | 39 % → 43 % | 21.4 px | 0.48 | 1.10 | 610 |
| stroke 8 | 44 % → 44 % | 44.2 px | 0.48 | 1.00 | 545 |

Numbers say: wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #46 Red-brown ink lips — own sheet
own sheet 600 × 600 · Watercolor · 50 px · 8.2 s

![Brush Artist · Refs · #46 Red-brown ink lips — own sheet](Brush-Artist-Refs-46-Red-brown-ink-lips-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 12 % → 24 % | 51.9 px | 0.59 | 1.91 | 269 |
| stroke 2 | 16 % → 27 % | 68.1 px | 0.54 | 1.74 | 175 |

Numbers say: wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #47 Pink knife slabs — own sheet
own sheet 600 × 600 · Heavy acrylic · 90 px · 7.0 s

![Brush Artist · Refs · #47 Pink knife slabs — own sheet](Brush-Artist-Refs-47-Pink-knife-slabs-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 19 % → 39 % | 97.8 px | 0.11 | 1.98 | 144 |
| stroke 2 | 34 % → 51 % | 195.7 px | 0.11 | 1.48 | 144 |
| stroke 3 | 35 % → 51 % | 196.5 px | 0.11 | 1.48 | 103 |
| stroke 4 | 46 % → 46 % | 196.5 px | 0.11 | 0.99 | 98 |

Numbers say: wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #48 Black bands with drips — own sheet
own sheet 600 × 600 · Gouache · 70 px · 17.3 s

![Brush Artist · Refs · #48 Black bands with drips — own sheet](Brush-Artist-Refs-48-Black-bands-with-drips-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 23 % → 36 % | 59.0 px | 0.39 | 1.58 | 793 |
| stroke 2 | 34 % → 48 % | 108.8 px | 0.39 | 1.41 | 827 |
| stroke 3 | 36 % → 48 % | 112.9 px | 0.39 | 1.34 | 781 |
| stroke 4 | 38 % → 36 % | 111.9 px | 0.39 | 0.95 | 719 |

Numbers say: wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #49 Magenta letters round brush — own sheet
own sheet 600 × 600 · Ink · 30 px · 16.2 s

![Brush Artist · Refs · #49 Magenta letters round brush — own sheet](Brush-Artist-Refs-49-Magenta-letters-round-brush-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 27 % → 46 % | 64.3 px | 0.52 | 1.69 | 52 |
| stroke 2 | 29 % → 40 % | 52.5 px | 0.53 | 1.39 | 55 |
| stroke 3 | 41 % → 67 % | 96.4 px | 0.52 | 1.64 | 49 |
| stroke 4 | 34 % → 52 % | 53.7 px | 0.52 | 1.55 | 193 |
| stroke 5 | 40 % → 66 % | 94.8 px | 0.52 | 1.65 | 95 |
| stroke 6 | 54 % → 70 % | 231.2 px | 0.52 | 1.29 | 29 |
| stroke 7 | 41 % → 56 % | 63.9 px | 0.52 | 1.35 | 187 |
| stroke 8 | 36 % → 61 % | 91.9 px | 0.53 | 1.72 | 112 |
| stroke 9 | 49 % → 60 % | 152.9 px | 0.53 | 1.24 | 50 |
| stroke 10 | 42 % → 72 % | 100.5 px | 0.52 | 1.71 | 121 |
| stroke 11 | 52 % → 72 % | 219.5 px | 0.52 | 1.39 | 56 |
| stroke 12 | 53 % → 68 % | 82.2 px | 0.52 | 1.29 | 306 |
| stroke 13 | 42 % → 54 % | 116.0 px | 0.53 | 1.29 | 81 |
| stroke 14 | 45 % → 69 % | 131.9 px | 0.53 | 1.52 | 63 |
| stroke 15 | 43 % → 63 % | 102.4 px | 0.52 | 1.46 | 155 |
| stroke 16 | 52 % → 61 % | 220.2 px | 0.52 | 1.18 | 39 |
| stroke 17 | 53 % → 64 % | 82.3 px | 0.52 | 1.19 | 272 |
| stroke 18 | 36 % → 44 % | 99.6 px | 0.52 | 1.21 | 67 |
| stroke 19 | 54 % → 53 % | 123.8 px | 0.52 | 0.99 | 83 |
| stroke 20 | 54 % → 54 % | 125.3 px | 0.52 | 1.00 | 51 |
| stroke 21 | 49 % → 49 % | 81.3 px | 0.52 | 1.00 | 140 |

Numbers say: wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #50 Thick swipes on photo — own sheet
own sheet 600 × 600 · Heavy acrylic · 40 px · 7.4 s

![Brush Artist · Refs · #50 Thick swipes on photo — own sheet](Brush-Artist-Refs-50-Thick-swipes-on-photo-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 10 % → 26 % | 46.9 px | 0.32 | 2.58 | 55 |
| stroke 2 | 10 % → 20 % | 48.1 px | 0.31 | 1.93 | 56 |
| stroke 3 | 11 % → 13 % | 45.4 px | 0.32 | 1.16 | 62 |
| stroke 4 | 12 % → 25 % | 47.6 px | 0.32 | 2.05 | 65 |
| stroke 5 | 12 % → 13 % | 46.0 px | 0.32 | 1.07 | 52 |
| stroke 6 | 19 % → 25 % | 109.7 px | 0.31 | 1.30 | 64 |
| stroke 7 | 24 % → 31 % | 102.1 px | 0.32 | 1.29 | 107 |
| stroke 8 | 24 % → 25 % | 134.5 px | 0.32 | 1.03 | 92 |
| stroke 9 | 12 % → 14 % | 52.6 px | 0.31 | 1.20 | 101 |
| stroke 10 | 26 % → 28 % | 88.4 px | 0.31 | 1.08 | 95 |
| stroke 11 | 9 % → 10 % | 47.2 px | 0.32 | 1.09 | 69 |
| stroke 12 | 18 % → 19 % | 100.0 px | 0.32 | 1.07 | 46 |

Numbers say: wet paint spreads well beyond the stroke.

## Brush Artist · Ink — dry brush — own sheet
own sheet 600 × 600 · Gouache · 30 px · 4.9 s

![Brush Artist · Ink — dry brush — own sheet](Brush-Artist-Ink-dry-brush-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| ear | 6 % → 3 % | 7.8 px | 0.86 | 0.44 | 857 |
| drag0 | 6 % → 8 % | 10.2 px | 0.86 | 1.39 | 230 |
| drag1 | 8 % → 8 % | 16.5 px | 0.86 | 1.02 | 170 |
| drag2 | 10 % → 9 % | 22.5 px | 0.86 | 0.87 | 133 |
| drag3 | 12 % → 9 % | 29.4 px | 0.86 | 0.78 | 119 |

## Brush Artist · Watercolour — blue — own sheet
own sheet 600 × 600 · Watercolor · 40 px · 13.1 s

![Brush Artist · Watercolour — blue — own sheet](Brush-Artist-Watercolour-blue-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| s0 | 7 % → 23 % | 28.4 px | 0.25 | 3.20 | 61 |
| s1 | 5 % → 32 % | 9.9 px | 0.38 | 5.85 | 73 |
| s2 | 10 % → 18 % | 43.5 px | 0.19 | 1.75 | 48 |
| s3 | 9 % → 17 % | 26.3 px | 0.28 | 1.85 | 73 |
| s4 | 14 % → 29 % | 37.9 px | 0.36 | 2.11 | 97 |
| s5 | 19 % → 29 % | 38.9 px | 0.37 | 1.52 | 69 |
| s6 | 17 % → 21 % | 47.6 px | 0.27 | 1.22 | 73 |
| s7 | 24 % → 35 % | 31.9 px | 0.37 | 1.44 | 64 |
| s8 | 20 % → 24 % | 77.5 px | 0.27 | 1.18 | 59 |

Numbers say: wet paint spreads well beyond the stroke.

## Brush Artist · Charcoal — stick — own sheet
own sheet 600 × 600 · Charcoal · 28 px · 1.7 s

![Brush Artist · Charcoal — stick — own sheet](Brush-Artist-Charcoal-stick-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| finger0 | 9 % → 18 % | 15.5 px | 0.83 | 2.01 | 39 |
| tip0 | 8 % → 14 % | 22.1 px | 0.83 | 1.75 | 20 |
| finger1 | 17 % → 29 % | 29.4 px | 0.83 | 1.74 | 45 |
| tip1 | 15 % → 21 % | 39.1 px | 0.83 | 1.42 | 15 |
| finger2 | 17 % → 25 % | 29.5 px | 0.83 | 1.53 | 27 |
| tip2 | 14 % → 20 % | 39.0 px | 0.83 | 1.41 | 8 |
| finger3 | 16 % → 19 % | 29.3 px | 0.83 | 1.16 | 36 |
| tip3 | 15 % → 15 % | 39.0 px | 0.83 | 1.00 | 15 |
| cig0 | 25 % → 35 % | 54.8 px | 0.83 | 1.41 | 12 |
| cig1 | 26 % → 35 % | 58.8 px | 0.83 | 1.32 | 17 |
| cig2 | 28 % → 35 % | 63.2 px | 0.83 | 1.22 | 17 |
| cig3 | 30 % → 34 % | 67.3 px | 0.83 | 1.14 | 11 |
| cig4 | 32 % → 34 % | 71.5 px | 0.83 | 1.06 | 10 |
| cig5 | 34 % → 34 % | 75.3 px | 0.83 | 1.00 | 11 |

Numbers say: wet paint spreads well beyond the stroke.

