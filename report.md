![All brushes](contact.png)

# Brush Lab — 187 brushes · 8 Nov 2026 at 13:34

Every sheet: 1500 × 600, ten strokes in a 5 × 2 grid — 1. light line · 2. heavy line · 3. pressure swell · 4. fast wave · 5. slow wave · 6. spiral · 7. loop · 8. tilted · 9. over the wet one · 10. long, no reload (cell 8 holds «tilted» and «over the wet one» crossed). The CPU reference of Mamay's paint engine; the wet layer settles 20 s at the end.

Columns: **covered** = share of the cell with paint right after the stroke → after settling; **width** = painted area of the stroke ÷ its length (px); **dark** = mean darkness of the painted pixels above the paper's own grain (0 = paper, 1 = black); **spread** = how far wet paint went beyond the stroke (1.0 = stayed); **ms** = the stroke on the CPU; long stroke: paint in each quarter of its length (it should run out: wet → streaks → dry tail).

## Ink Line
Ink · 12 px · 26.0 s

![Ink Line](Ink-Line.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 1 % → 4 % | 4.3 px | 0.55 | 2.45 | 63 |
| heavy line | 5 % → 6 % | 15.7 px | 0.68 | 1.14 | 73 |
| pressure swell | 3 % → 4 % | 11.3 px | 0.64 | 1.40 | 42 |
| fast wave | 10 % → 11 % | 11.2 px | 0.59 | 1.11 | 137 |
| slow wave | 8 % → 10 % | 9.6 px | 0.57 | 1.16 | 135 |
| spiral | 14 % → 15 % | 8.9 px | 0.49 | 1.07 | 397 |
| loop | 8 % → 9 % | 10.6 px | 0.61 | 1.15 | 115 |
| tilted | 5 % → 5 % | 14.3 px | 0.64 | 1.05 | 53 |
| over the wet one | 10 % → 11 % | 12.5 px | 0.64 | 1.15 | 57 |
| long, no reload | 18 % → 17 % | 8.1 px | 0.47 | 0.96 | 264 | quarters: 0.22 → 0.09 → 0.04 → 0.02

Numbers say: light vs heavy: width 4.3 → 15.7 px, dark 0.55 → 0.68; wet paint spreads well beyond the stroke.

## Dense Ink
Ink · 14 px · 26.3 s

![Dense Ink](Dense-Ink.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 5 % → 7 % | 15.2 px | 0.72 | 1.27 | 45 |
| heavy line | 7 % → 7 % | 19.1 px | 0.73 | 1.09 | 71 |
| pressure swell | 5 % → 6 % | 17.9 px | 0.72 | 1.18 | 47 |
| fast wave | 13 % → 13 % | 15.2 px | 0.69 | 1.01 | 157 |
| slow wave | 12 % → 12 % | 13.5 px | 0.67 | 1.04 | 158 |
| spiral | 18 % → 15 % | 12.2 px | 0.65 | 0.80 | 296 |
| loop | 11 % → 12 % | 14.8 px | 0.69 | 1.08 | 136 |
| tilted | 5 % → 6 % | 14.5 px | 0.72 | 1.07 | 80 |
| over the wet one | 12 % → 13 % | 17.7 px | 0.72 | 1.12 | 65 |
| long, no reload | 23 % → 15 % | 10.1 px | 0.64 | 0.66 | 524 | quarters: 0.30 → 0.12 → 0.04 → 0.02

Numbers say: light vs heavy: width 15.2 → 19.1 px, dark 0.72 → 0.73.

## Transparent Wash
Watercolor · 22 px · 27.7 s

![Transparent Wash](Transparent-Wash.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 2 % → 5 % | 6.9 px | 0.27 | 2.26 | 78 |
| heavy line | 7 % → 9 % | 20.4 px | 0.27 | 1.23 | 65 |
| pressure swell | 4 % → 6 % | 15.2 px | 0.28 | 1.54 | 42 |
| fast wave | 14 % → 16 % | 16.1 px | 0.20 | 1.17 | 136 |
| slow wave | 12 % → 15 % | 13.7 px | 0.21 | 1.28 | 179 |
| spiral | 18 % → 22 % | 11.9 px | 0.16 | 1.22 | 201 |
| loop | 11 % → 13 % | 14.5 px | 0.22 | 1.20 | 103 |
| tilted | 8 % → 8 % | 21.1 px | 0.24 | 1.06 | 58 |
| over the wet one | 13 % → 16 % | 16.4 px | 0.24 | 1.19 | 53 |
| long, no reload | 26 % → 32 % | 11.6 px | 0.13 | 1.22 | 411 | quarters: 0.11 → 0.04 → 0.02 → 0.01

Numbers say: light vs heavy: width 6.9 → 20.4 px, dark 0.27 → 0.27; wet paint spreads well beyond the stroke.

## Dry Brush
Gouache · 24 px · 25.8 s

![Dry Brush](Dry-Brush.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 5 % → 1 % | 13.8 px | 0.65 | 0.11 | 191 |
| heavy line | 6 % → 0 % | 18.4 px | 0.65 | 0.02 | 105 |
| pressure swell | 5 % → 0 % | 18.1 px | 0.65 | 0.09 | 56 |
| fast wave | 6 % → 1 % | 6.9 px | 0.65 | 0.08 | 196 |
| slow wave | 7 % → 0 % | 7.8 px | 0.65 | 0.07 | 443 |
| spiral | 7 % → 1 % | 4.4 px | 0.65 | 0.08 | 275 |
| loop | 9 % → 0 % | 12.2 px | 0.65 | 0.05 | 155 |
| tilted | 4 % → 3 % | 10.3 px | 0.65 | 0.89 | 87 |
| over the wet one | 9 % → 1 % | 14.3 px | 0.65 | 0.12 | 52 |
| long, no reload | 6 % → 1 % | 2.7 px | 0.65 | 0.15 | 351 | quarters: 0.12 → 0.00 → 0.00 → 0.00

Numbers say: light vs heavy: width 13.8 → 18.4 px, dark 0.65 → 0.65.

## Wax Crayon
Wax · 8 px · 11.2 s

![Wax Crayon](Wax-Crayon.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 1 % → 1 % | 2.5 px | 0.71 | 1.00 | 72 |
| heavy line | 1 % → 1 % | 3.9 px | 0.69 | 1.00 | 20 |
| pressure swell | 1 % → 1 % | 3.3 px | 0.70 | 1.00 | 12 |
| fast wave | 3 % → 3 % | 3.5 px | 0.69 | 1.00 | 49 |
| slow wave | 3 % → 3 % | 3.4 px | 0.70 | 1.00 | 40 |
| spiral | 5 % → 5 % | 3.3 px | 0.70 | 1.00 | 85 |
| loop | 3 % → 3 % | 3.3 px | 0.70 | 1.00 | 57 |
| tilted | 2 % → 2 % | 5.6 px | 0.68 | 1.00 | 40 |
| over the wet one | 3 % → 3 % | 3.6 px | 0.68 | 1.00 | 30 |
| long, no reload | 7 % → 7 % | 3.3 px | 0.70 | 1.00 | 128 | quarters: 0.06 → 0.06 → 0.06 → 0.06

Numbers say: light vs heavy: width 2.5 → 3.9 px, dark 0.71 → 0.69; the long stroke does not run out of paint.

## Oil Pastel
Wax · 12 px · 11.2 s

![Oil Pastel](Oil-Pastel.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 1 % → 1 % | 4.0 px | 0.68 | 1.00 | 80 |
| heavy line | 2 % → 2 % | 6.5 px | 0.68 | 1.00 | 36 |
| pressure swell | 2 % → 2 % | 5.7 px | 0.69 | 1.00 | 22 |
| fast wave | 5 % → 5 % | 5.7 px | 0.68 | 1.00 | 66 |
| slow wave | 5 % → 5 % | 5.5 px | 0.68 | 1.00 | 61 |
| spiral | 8 % → 8 % | 5.5 px | 0.68 | 1.00 | 112 |
| loop | 4 % → 4 % | 5.6 px | 0.68 | 1.00 | 57 |
| tilted | 2 % → 2 % | 6.8 px | 0.68 | 1.00 | 43 |
| over the wet one | 5 % → 5 % | 5.8 px | 0.68 | 1.00 | 29 |
| long, no reload | 13 % → 13 % | 5.6 px | 0.68 | 1.00 | 169 | quarters: 0.10 → 0.09 → 0.10 → 0.10

Numbers say: light vs heavy: width 4.0 → 6.5 px, dark 0.68 → 0.68; the long stroke does not run out of paint.

## Charcoal
Charcoal · 5 px · 10.9 s

![Charcoal](Charcoal.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 1 % → 1 % | 2.0 px | 0.74 | 1.00 | 30 |
| heavy line | 1 % → 1 % | 3.0 px | 0.74 | 1.00 | 15 |
| pressure swell | 1 % → 1 % | 2.7 px | 0.74 | 1.00 | 9 |
| fast wave | 2 % → 2 % | 2.7 px | 0.73 | 1.00 | 33 |
| slow wave | 2 % → 2 % | 2.6 px | 0.74 | 1.00 | 35 |
| spiral | 4 % → 4 % | 2.5 px | 0.74 | 1.00 | 50 |
| loop | 2 % → 2 % | 2.6 px | 0.74 | 1.00 | 23 |
| tilted | 2 % → 2 % | 4.3 px | 0.72 | 1.00 | 25 |
| over the wet one | 2 % → 2 % | 2.4 px | 0.72 | 1.00 | 13 |
| long, no reload | 6 % → 6 % | 2.7 px | 0.73 | 1.00 | 164 | quarters: 0.05 → 0.05 → 0.05 → 0.05

Numbers say: light vs heavy: width 2.0 → 3.0 px, dark 0.74 → 0.74; the long stroke does not run out of paint.

## Impasto
Heavy acrylic · 22 px · 16.2 s

![Impasto](Impasto.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 8 % → 8 % | 24.1 px | 0.72 | 0.93 | 124 |
| heavy line | 10 % → 9 % | 28.8 px | 0.70 | 0.94 | 112 |
| pressure swell | 7 % → 7 % | 28.1 px | 0.72 | 0.94 | 49 |
| fast wave | 20 % → 13 % | 23.4 px | 0.71 | 0.64 | 183 |
| slow wave | 21 % → 14 % | 24.5 px | 0.71 | 0.66 | 268 |
| spiral | 30 % → 14 % | 19.9 px | 0.71 | 0.46 | 340 |
| loop | 18 % → 14 % | 23.9 px | 0.71 | 0.77 | 191 |
| tilted | 8 % → 8 % | 21.7 px | 0.70 | 1.00 | 78 |
| over the wet one | 17 % → 15 % | 25.4 px | 0.70 | 0.91 | 56 |
| long, no reload | 33 % → 14 % | 14.9 px | 0.71 | 0.42 | 435 | quarters: 0.38 → 0.21 → 0.10 → 0.03

Numbers say: light vs heavy: width 24.1 → 28.8 px, dark 0.72 → 0.70.

## Oil Round
Oil · 18 px · 19.2 s

![Oil Round](Oil-Round.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 2 % → 2 % | 7.2 px | 0.75 | 1.00 | 203 |
| heavy line | 7 % → 7 % | 19.3 px | 0.73 | 1.00 | 82 |
| pressure swell | 4 % → 4 % | 13.7 px | 0.72 | 1.00 | 35 |
| fast wave | 11 % → 11 % | 12.8 px | 0.65 | 1.00 | 153 |
| slow wave | 8 % → 8 % | 9.0 px | 0.57 | 1.00 | 196 |
| spiral | 10 % → 10 % | 6.6 px | 0.50 | 1.00 | 215 |
| loop | 6 % → 6 % | 7.2 px | 0.45 | 1.00 | 176 |
| tilted | 4 % → 4 % | 10.1 px | 0.52 | 1.00 | 68 |
| over the wet one | 6 % → 6 % | 7.6 px | 0.52 | 1.00 | 60 |
| long, no reload | 15 % → 15 % | 6.9 px | 0.42 | 1.00 | 362 | quarters: 0.09 → 0.08 → 0.07 → 0.06

Numbers say: light vs heavy: width 7.2 → 19.3 px, dark 0.75 → 0.73.

## Palette Knife
Oil · 20 px · 18.7 s

![Palette Knife](Palette-Knife.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 8 % → 8 % | 21.9 px | 0.67 | 1.00 | 169 |
| heavy line | 8 % → 8 % | 22.5 px | 0.74 | 1.00 | 13 |
| pressure swell | 6 % → 6 % | 22.3 px | 0.74 | 1.00 | 9 |
| fast wave | 16 % → 16 % | 18.9 px | 0.50 | 1.00 | 28 |
| slow wave | 17 % → 17 % | 19.9 px | 0.43 | 1.00 | 50 |
| spiral | 17 % → 17 % | 11.3 px | 0.46 | 1.00 | 82 |
| loop | 16 % → 16 % | 21.0 px | 0.59 | 1.00 | 35 |
| tilted | 5 % → 5 % | 15.0 px | 0.72 | 1.00 | 27 |
| over the wet one | 13 % → 13 % | 21.0 px | 0.72 | 1.00 | 14 |
| long, no reload | 16 % → 16 % | 7.2 px | 0.49 | 1.00 | 61 | quarters: 0.29 → 0.05 → 0.00 → 0.00

Numbers say: light vs heavy: width 21.9 → 22.5 px, dark 0.67 → 0.74; pressure barely changes the width.

## Water
Watercolor · 20 px · 34.6 s · over bands of wet oil paint and oil pastel in turn (it works on paint already there: look at what it does to the bands; covered counts the bands too)

![Water](Water.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 25 % → 27 % | 73.8 px | 0.80 | 1.06 | 24 |
| heavy line | 24 % → 25 % | 69.8 px | 0.81 | 1.04 | 60 |
| pressure swell | 24 % → 25 % | 89.6 px | 0.81 | 1.03 | 29 |
| fast wave | 24 % → 26 % | 27.7 px | 0.81 | 1.07 | 102 |
| slow wave | 24 % → 25 % | 27.8 px | 0.81 | 1.06 | 135 |
| spiral | 24 % → 26 % | 15.9 px | 0.81 | 1.07 | 168 |
| loop | 24 % → 25 % | 31.1 px | 0.81 | 1.03 | 88 |
| tilted | 24 % → 24 % | 67.0 px | 0.81 | 1.00 | 66 |
| over the wet one | 24 % → 25 % | 0.0 px | 0.81 | 1.06 | 38 |
| long, no reload | 24 % → 26 % | 10.7 px | 0.81 | 1.08 | 316 | quarters: 0.21 → 0.27 → 0.18 → 0.27

Numbers say: light vs heavy: width 73.8 → 69.8 px, dark 0.80 → 0.81; pressure barely changes the width; the long stroke does not run out of paint.

## Blender
Pastel · 16 px · 20.5 s · over bands of wet oil paint and oil pastel in turn (it works on paint already there: look at what it does to the bands; covered counts the bands too)

![Blender](Blender.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 24 % → 24 % | 70.7 px | 0.81 | 1.00 | 15 |
| heavy line | 25 % → 25 % | 72.1 px | 0.80 | 1.00 | 40 |
| pressure swell | 24 % → 24 % | 91.3 px | 0.81 | 1.00 | 18 |
| fast wave | 26 % → 26 % | 30.0 px | 0.79 | 1.00 | 65 |
| slow wave | 26 % → 26 % | 29.9 px | 0.80 | 1.00 | 75 |
| spiral | 28 % → 28 % | 18.7 px | 0.77 | 1.00 | 118 |
| loop | 25 % → 25 % | 33.0 px | 0.80 | 1.00 | 71 |
| tilted | 25 % → 25 % | 70.1 px | 0.79 | 1.00 | 40 |
| over the wet one | 26 % → 26 % | 1.8 px | 0.79 | 1.00 | 26 |
| long, no reload | 30 % → 30 % | 13.7 px | 0.76 | 1.00 | 208 | quarters: 0.20 → 0.28 → 0.23 → 0.30

Numbers say: light vs heavy: width 70.7 → 72.1 px, dark 0.81 → 0.80; pressure barely changes the width; the long stroke does not run out of paint.

## Eraser
Eraser · 16 px · 20.4 s · over bands of wet oil paint and oil pastel in turn (it works on paint already there: look at what it does to the bands; covered counts the bands too)

![Eraser](Eraser.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 24 % → 24 % | 69.6 px | 0.82 | 1.00 | 19 |
| heavy line | 23 % → 23 % | 67.9 px | 0.82 | 1.00 | 34 |
| pressure swell | 23 % → 23 % | 87.3 px | 0.82 | 1.00 | 35 |
| fast wave | 22 % → 22 % | 25.7 px | 0.82 | 1.00 | 71 |
| slow wave | 22 % → 22 % | 25.7 px | 0.82 | 1.00 | 67 |
| spiral | 22 % → 22 % | 14.4 px | 0.82 | 1.00 | 113 |
| loop | 22 % → 22 % | 28.6 px | 0.82 | 1.00 | 78 |
| tilted | 23 % → 23 % | 65.1 px | 0.82 | 1.00 | 48 |
| over the wet one | 23 % → 23 % | 0.0 px | 0.82 | 1.00 | 33 |
| long, no reload | 20 % → 20 % | 8.9 px | 0.82 | 1.00 | 198 | quarters: 0.15 → 0.20 → 0.15 → 0.20

Numbers say: light vs heavy: width 69.6 → 67.9 px, dark 0.82 → 0.82; pressure barely changes the width; the long stroke does not run out of paint.

## Fan
Gouache · 30 px · 28.2 s

![Fan](Fan.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 9 % → 3 % | 25.6 px | 0.63 | 0.37 | 38 |
| heavy line | 11 % → 4 % | 30.9 px | 0.63 | 0.39 | 38 |
| pressure swell | 8 % → 5 % | 31.7 px | 0.63 | 0.55 | 29 |
| fast wave | 17 % → 5 % | 20.2 px | 0.63 | 0.26 | 101 |
| slow wave | 18 % → 5 % | 21.0 px | 0.63 | 0.25 | 140 |
| spiral | 24 % → 5 % | 15.5 px | 0.63 | 0.19 | 169 |
| loop | 17 % → 5 % | 22.7 px | 0.63 | 0.28 | 87 |
| tilted | 5 % → 6 % | 15.0 px | 0.63 | 1.05 | 32 |
| over the wet one | 16 % → 8 % | 29.7 px | 0.63 | 0.49 | 43 |
| long, no reload | 22 % → 5 % | 9.9 px | 0.63 | 0.22 | 295 | quarters: 0.29 → 0.07 → 0.01 → 0.00

Numbers say: light vs heavy: width 25.6 → 30.9 px, dark 0.63 → 0.63.

## Sponge
Gouache · 30 px · 28.3 s

![Sponge](Sponge.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 4 % → 0 % | 11.3 px | 0.62 | 0.12 | 37 |
| heavy line | 12 % → 2 % | 35.4 px | 0.62 | 0.14 | 50 |
| pressure swell | 7 % → 2 % | 27.9 px | 0.62 | 0.28 | 36 |
| fast wave | 20 % → 4 % | 23.2 px | 0.62 | 0.19 | 129 |
| slow wave | 21 % → 4 % | 23.8 px | 0.62 | 0.18 | 290 |
| spiral | 28 % → 4 % | 18.3 px | 0.62 | 0.14 | 187 |
| loop | 18 % → 5 % | 23.0 px | 0.62 | 0.29 | 118 |
| tilted | 7 % → 7 % | 18.2 px | 0.62 | 1.04 | 75 |
| over the wet one | 16 % → 6 % | 27.8 px | 0.62 | 0.37 | 55 |
| long, no reload | 29 % → 5 % | 12.9 px | 0.62 | 0.17 | 266 | quarters: 0.29 → 0.13 → 0.07 → 0.04

Numbers say: light vs heavy: width 11.3 → 35.4 px, dark 0.62 → 0.62.

## Ink — sumi brush
Watercolour 1.00 · 22 px · 28.2 s

![Ink — sumi brush](Ink-sumi-brush.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 8 % → 9 % | 23.9 px | 0.87 | 1.13 | 56 |
| heavy line | 12 % → 13 % | 36.2 px | 0.86 | 1.01 | 69 |
| pressure swell | 10 % → 10 % | 36.1 px | 0.87 | 1.04 | 50 |
| fast wave | 27 % → 27 % | 31.0 px | 0.82 | 1.00 | 155 |
| slow wave | 27 % → 28 % | 31.2 px | 0.82 | 1.02 | 321 |
| spiral | 38 % → 36 % | 25.2 px | 0.75 | 0.95 | 264 |
| loop | 22 % → 23 % | 29.0 px | 0.84 | 1.01 | 142 |
| tilted | 9 % → 9 % | 25.7 px | 0.86 | 1.00 | 75 |
| over the wet one | 20 % → 20 % | 30.0 px | 0.86 | 1.02 | 57 |
| long, no reload | 46 % → 41 % | 20.7 px | 0.70 | 0.90 | 398 | quarters: 0.57 → 0.42 → 0.24 → 0.15

Numbers say: light vs heavy: width 23.9 → 36.2 px, dark 0.87 → 0.86.

## Ink — wash
Watercolour 1.00 · 40 px · 32.6 s

![Ink — wash](Ink-wash.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 13 % → 13 % | 37.3 px | 0.42 | 1.02 | 64 |
| heavy line | 19 % → 19 % | 55.2 px | 0.35 | 1.01 | 86 |
| pressure swell | 13 % → 13 % | 48.2 px | 0.41 | 1.02 | 52 |
| fast wave | 41 % → 42 % | 47.8 px | 0.32 | 1.02 | 206 |
| slow wave | 39 % → 40 % | 45.3 px | 0.42 | 1.02 | 314 |
| spiral | 60 % → 62 % | 39.7 px | 0.33 | 1.02 | 320 |
| loop | 34 % → 34 % | 43.8 px | 0.39 | 1.01 | 173 |
| tilted | 15 % → 15 % | 40.7 px | 0.43 | 1.01 | 124 |
| over the wet one | 30 % → 31 % | 43.4 px | 0.43 | 1.02 | 78 |
| long, no reload | 71 % → 75 % | 32.0 px | 0.31 | 1.05 | 493 | quarters: 0.40 → 0.29 → 0.19 → 0.12

Numbers say: light vs heavy: width 37.3 → 55.2 px, dark 0.42 → 0.35.

## Ink — dry brush
Ink 1.00 · 30 px · 24.6 s

![Ink — dry brush](Ink-dry-brush.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 5 % → 5 % | 14.9 px | 0.82 | 0.88 | 81 |
| heavy line | 7 % → 6 % | 19.4 px | 0.82 | 0.87 | 144 |
| pressure swell | 5 % → 5 % | 18.9 px | 0.81 | 0.96 | 69 |
| fast wave | 12 % → 7 % | 13.4 px | 0.80 | 0.65 | 290 |
| slow wave | 12 % → 8 % | 14.1 px | 0.81 | 0.62 | 380 |
| spiral | 16 % → 8 % | 10.8 px | 0.80 | 0.47 | 426 |
| loop | 11 % → 9 % | 14.5 px | 0.79 | 0.77 | 176 |
| tilted | 5 % → 6 % | 15.0 px | 0.81 | 1.08 | 107 |
| over the wet one | 12 % → 11 % | 18.4 px | 0.81 | 0.94 | 84 |
| long, no reload | 21 % → 10 % | 9.2 px | 0.77 | 0.47 | 565 | quarters: 0.28 → 0.10 → 0.03 → 0.01

Numbers say: light vs heavy: width 14.9 → 19.4 px, dark 0.82 → 0.82.

## Ink — nib
Watercolour 1.00 · 5 px · 23.3 s

![Ink — nib](Ink-nib.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 2 % → 5 % | 5.5 px | 0.89 | 2.46 | 22 |
| heavy line | 2 % → 5 % | 6.4 px | 0.89 | 2.34 | 31 |
| pressure swell | 2 % → 4 % | 6.2 px | 0.89 | 2.53 | 21 |
| fast wave | 5 % → 8 % | 5.9 px | 0.89 | 1.63 | 93 |
| slow wave | 5 % → 8 % | 5.7 px | 0.89 | 1.70 | 62 |
| spiral | 8 % → 11 % | 5.0 px | 0.87 | 1.41 | 114 |
| loop | 4 % → 8 % | 5.7 px | 0.89 | 1.74 | 66 |
| tilted | 4 % → 4 % | 10.3 px | 0.89 | 1.02 | 21 |
| over the wet one | 6 % → 9 % | 6.1 px | 0.89 | 1.61 | 31 |
| long, no reload | 9 % → 12 % | 4.2 px | 0.85 | 1.30 | 184 | quarters: 0.24 → 0.11 → 0.07 → 0.05

Numbers say: light vs heavy: width 5.5 → 6.4 px, dark 0.89 → 0.89; wet paint spreads well beyond the stroke.

## 0.45 · Dry brush
Gouache 0.91 · Ink 0.07 · 34 px · 31.7 s

![0.45 · Dry brush](0-45-Dry-brush.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 8 % → 2 % | 22.9 px | 0.68 | 0.24 | 106 |
| heavy line | 10 % → 5 % | 27.8 px | 0.68 | 0.52 | 139 |
| pressure swell | 7 % → 4 % | 26.5 px | 0.68 | 0.59 | 84 |
| fast wave | 19 % → 6 % | 21.4 px | 0.68 | 0.33 | 383 |
| slow wave | 20 % → 7 % | 23.0 px | 0.68 | 0.38 | 484 |
| spiral | 27 % → 8 % | 17.6 px | 0.68 | 0.29 | 519 |
| loop | 18 % → 9 % | 23.0 px | 0.68 | 0.51 | 244 |
| tilted | 8 % → 8 % | 21.8 px | 0.68 | 1.02 | 143 |
| over the wet one | 17 % → 12 % | 25.0 px | 0.68 | 0.73 | 108 |
| long, no reload | 34 % → 9 % | 15.3 px | 0.68 | 0.28 | 717 | quarters: 0.37 → 0.26 → 0.19 → 0.17

Numbers say: light vs heavy: width 22.9 → 27.8 px, dark 0.68 → 0.68.

## Dry pastel
Pastel 1.00 · 26 px · 10.3 s

![Dry pastel](Dry-pastel.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 3 % → 3 % | 8.2 px | 0.37 | 1.00 | 28 |
| heavy line | 5 % → 5 % | 13.1 px | 0.39 | 1.00 | 42 |
| pressure swell | 3 % → 3 % | 11.5 px | 0.39 | 1.00 | 27 |
| fast wave | 10 % → 10 % | 11.8 px | 0.39 | 1.00 | 87 |
| slow wave | 10 % → 10 % | 11.1 px | 0.39 | 1.00 | 157 |
| spiral | 14 % → 14 % | 9.1 px | 0.38 | 1.00 | 168 |
| loop | 7 % → 7 % | 9.5 px | 0.38 | 1.00 | 77 |
| tilted | 3 % → 3 % | 7.5 px | 0.39 | 1.00 | 59 |
| over the wet one | 6 % → 6 % | 10.6 px | 0.39 | 1.00 | 28 |
| long, no reload | 17 % → 17 % | 7.6 px | 0.38 | 1.00 | 204 | quarters: 0.08 → 0.07 → 0.07 → 0.07

Numbers say: light vs heavy: width 8.2 → 13.1 px, dark 0.37 → 0.39; the long stroke does not run out of paint.

## 0.45 · Charcoal
Charcoal 1.00 · 18 px · 9.6 s

![0.45 · Charcoal](0-45-Charcoal.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 2 % → 2 % | 5.4 px | 0.79 | 1.00 | 23 |
| heavy line | 3 % → 3 % | 8.0 px | 0.79 | 1.00 | 16 |
| pressure swell | 2 % → 2 % | 7.8 px | 0.80 | 1.00 | 16 |
| fast wave | 8 % → 8 % | 8.8 px | 0.80 | 1.00 | 55 |
| slow wave | 6 % → 6 % | 7.3 px | 0.80 | 1.00 | 72 |
| spiral | 10 % → 10 % | 6.7 px | 0.80 | 1.00 | 87 |
| loop | 6 % → 6 % | 8.2 px | 0.80 | 1.00 | 43 |
| tilted | 3 % → 3 % | 7.2 px | 0.79 | 1.00 | 21 |
| over the wet one | 5 % → 5 % | 7.4 px | 0.79 | 1.00 | 20 |
| long, no reload | 17 % → 17 % | 7.8 px | 0.80 | 1.00 | 92 | quarters: 0.15 → 0.16 → 0.16 → 0.16

Numbers say: light vs heavy: width 5.4 → 8.0 px, dark 0.79 → 0.79; the long stroke does not run out of paint.

## Watercolour — wash
Watercolour 1.00 · 50 px · 36.5 s

![Watercolour — wash](Watercolour-wash.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 16 % → 16 % | 45.5 px | 0.22 | 1.01 | 92 |
| heavy line | 22 % → 22 % | 64.9 px | 0.19 | 1.00 | 124 |
| pressure swell | 15 % → 15 % | 56.1 px | 0.22 | 1.01 | 88 |
| fast wave | 48 % → 49 % | 55.5 px | 0.19 | 1.01 | 268 |
| slow wave | 46 % → 46 % | 53.3 px | 0.24 | 1.00 | 606 |
| spiral | 66 % → 66 % | 43.7 px | 0.21 | 1.00 | 487 |
| loop | 40 % → 40 % | 51.4 px | 0.22 | 1.00 | 287 |
| tilted | 18 % → 18 % | 49.7 px | 0.23 | 1.00 | 176 |
| over the wet one | 36 % → 36 % | 49.6 px | 0.23 | 1.01 | 119 |
| long, no reload | 84 % → 84 % | 37.7 px | 0.20 | 1.00 | 719 | quarters: 0.24 → 0.20 → 0.16 → 0.12

Numbers say: light vs heavy: width 45.5 → 64.9 px, dark 0.22 → 0.19.

## Watercolour — wet-in-wet
Watercolour 1.00 · 44 px · 38.7 s

![Watercolour — wet-in-wet](Watercolour-wet-in-wet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 13 % → 21 % | 37.4 px | 0.32 | 1.63 | 89 |
| heavy line | 19 % → 22 % | 54.7 px | 0.34 | 1.17 | 99 |
| pressure swell | 12 % → 17 % | 45.7 px | 0.36 | 1.36 | 65 |
| fast wave | 42 % → 49 % | 48.5 px | 0.33 | 1.16 | 238 |
| slow wave | 40 % → 48 % | 45.7 px | 0.41 | 1.22 | 407 |
| spiral | 63 % → 69 % | 41.3 px | 0.37 | 1.11 | 570 |
| loop | 34 % → 41 % | 44.0 px | 0.37 | 1.21 | 221 |
| tilted | 16 % → 17 % | 44.6 px | 0.36 | 1.05 | 146 |
| over the wet one | 32 % → 40 % | 44.4 px | 0.36 | 1.26 | 111 |
| long, no reload | 79 % → 87 % | 35.3 px | 0.36 | 1.11 | 631 | quarters: 0.40 → 0.37 → 0.33 → 0.26

Numbers say: light vs heavy: width 37.4 → 54.7 px, dark 0.32 → 0.34; wet paint spreads well beyond the stroke.

## Watercolour — glaze
Watercolour 1.00 · 38 px · 33.4 s

![Watercolour — glaze](Watercolour-glaze.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 13 % → 13 % | 36.6 px | 0.07 | 1.02 | 66 |
| heavy line | 19 % → 19 % | 55.4 px | 0.07 | 1.00 | 109 |
| pressure swell | 13 % → 13 % | 47.0 px | 0.07 | 1.02 | 67 |
| fast wave | 39 % → 40 % | 45.6 px | 0.07 | 1.01 | 315 |
| slow wave | 37 % → 37 % | 42.8 px | 0.07 | 1.01 | 382 |
| spiral | 59 % → 60 % | 38.8 px | 0.06 | 1.01 | 434 |
| loop | 33 % → 33 % | 42.6 px | 0.07 | 1.00 | 199 |
| tilted | 14 % → 14 % | 40.1 px | 0.07 | 1.00 | 138 |
| over the wet one | 30 % → 30 % | 42.3 px | 0.07 | 1.01 | 98 |
| long, no reload | 69 % → 70 % | 30.9 px | 0.06 | 1.01 | 562 | quarters: 0.06 → 0.05 → 0.03 → 0.02

Numbers say: light vs heavy: width 36.6 → 55.4 px, dark 0.07 → 0.07.

## Watercolour — granulating
Watercolour 1.00 · 44 px · 34.9 s

![Watercolour — granulating](Watercolour-granulating.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 14 % → 14 % | 41.4 px | 0.35 | 1.01 | 90 |
| heavy line | 21 % → 21 % | 60.4 px | 0.31 | 1.00 | 92 |
| pressure swell | 14 % → 14 % | 52.2 px | 0.34 | 1.01 | 82 |
| fast wave | 45 % → 45 % | 51.7 px | 0.29 | 1.01 | 269 |
| slow wave | 42 % → 42 % | 48.2 px | 0.35 | 1.01 | 470 |
| spiral | 62 % → 63 % | 41.0 px | 0.30 | 1.01 | 420 |
| loop | 37 % → 37 % | 47.6 px | 0.33 | 1.00 | 234 |
| tilted | 16 % → 16 % | 45.5 px | 0.36 | 1.00 | 136 |
| over the wet one | 33 % → 33 % | 46.2 px | 0.36 | 1.01 | 105 |
| long, no reload | 75 % → 76 % | 33.6 px | 0.29 | 1.01 | 697 | quarters: 0.34 → 0.26 → 0.20 → 0.14

Numbers say: light vs heavy: width 41.4 → 60.4 px, dark 0.35 → 0.31.

## Watercolour — dry brush
Watercolour 1.00 · 36 px · 27.9 s

![Watercolour — dry brush](Watercolour-dry-brush.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 10 % → 9 % | 27.8 px | 0.17 | 0.99 | 137 |
| heavy line | 14 % → 12 % | 39.3 px | 0.16 | 0.92 | 120 |
| pressure swell | 11 % → 10 % | 39.6 px | 0.16 | 0.95 | 82 |
| fast wave | 27 % → 20 % | 31.3 px | 0.13 | 0.74 | 335 |
| slow wave | 25 % → 17 % | 28.9 px | 0.14 | 0.70 | 464 |
| spiral | 34 % → 19 % | 22.6 px | 0.13 | 0.56 | 518 |
| loop | 21 % → 18 % | 27.7 px | 0.14 | 0.85 | 217 |
| tilted | 10 % → 10 % | 28.5 px | 0.16 | 1.01 | 144 |
| over the wet one | 21 % → 20 % | 31.0 px | 0.16 | 0.95 | 127 |
| long, no reload | 35 % → 19 % | 15.9 px | 0.14 | 0.54 | 595 | quarters: 0.09 → 0.03 → 0.01 → 0.00

Numbers say: light vs heavy: width 27.8 → 39.3 px, dark 0.17 → 0.16.

## Gouache
Gouache 1.00 · 30 px · 31.5 s

![Gouache](Gouache.png)

A light paint: laid on a grey sheet (on white it cannot be seen); **dark** = how far it is from the grey either way.

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 8 % → 5 % | 23.3 px | 0.29 | 0.61 | 112 |
| heavy line | 12 % → 5 % | 35.6 px | 0.28 | 0.41 | 107 |
| pressure swell | 10 % → 5 % | 36.2 px | 0.28 | 0.49 | 71 |
| fast wave | 22 % → 6 % | 25.0 px | 0.28 | 0.27 | 219 |
| slow wave | 22 % → 7 % | 25.9 px | 0.28 | 0.30 | 421 |
| spiral | 28 % → 7 % | 18.5 px | 0.28 | 0.23 | 362 |
| loop | 18 % → 7 % | 23.7 px | 0.28 | 0.37 | 203 |
| tilted | 9 % → 9 % | 24.0 px | 0.28 | 1.01 | 117 |
| over the wet one | 19 % → 12 % | 28.7 px | 0.28 | 0.62 | 102 |
| long, no reload | 27 % → 8 % | 12.2 px | 0.28 | 0.31 | 613 | quarters: 0.01 → 0.02 → 0.02 → 0.02

Numbers say: light vs heavy: width 23.3 → 35.6 px, dark 0.29 → 0.28; the long stroke does not run out of paint.

## Oil — alla prima
Oil 0.89 · Oil glaze 0.11 · 30 px · 14.3 s

![Oil — alla prima](Oil-alla-prima.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 9 % → 9 % | 27.5 px | 0.49 | 1.00 | 94 |
| heavy line | 10 % → 10 % | 28.7 px | 0.50 | 1.00 | 116 |
| pressure swell | 7 % → 7 % | 27.5 px | 0.50 | 1.00 | 84 |
| fast wave | 22 % → 22 % | 25.5 px | 0.50 | 1.00 | 274 |
| slow wave | 25 % → 25 % | 29.0 px | 0.50 | 1.00 | 452 |
| spiral | 37 % → 37 % | 24.5 px | 0.49 | 1.00 | 445 |
| loop | 21 % → 21 % | 27.5 px | 0.50 | 1.00 | 222 |
| tilted | 10 % → 10 % | 26.8 px | 0.50 | 1.00 | 104 |
| over the wet one | 19 % → 19 % | 27.7 px | 0.50 | 1.00 | 116 |
| long, no reload | 46 % → 46 % | 20.5 px | 0.47 | 1.00 | 676 | quarters: 0.31 → 0.25 → 0.22 → 0.18

Numbers say: light vs heavy: width 27.5 → 28.7 px, dark 0.49 → 0.50; pressure barely changes the width.

## Oil — impasto
Oil heavy 1.00 · 34 px · 15.2 s

![Oil — impasto](Oil-impasto.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 8 % → 8 % | 24.0 px | 0.22 | 1.00 | 115 |
| heavy line | 12 % → 12 % | 35.3 px | 0.22 | 1.00 | 128 |
| pressure swell | 9 % → 9 % | 33.1 px | 0.23 | 1.00 | 81 |
| fast wave | 29 % → 29 % | 33.7 px | 0.22 | 1.00 | 305 |
| slow wave | 30 % → 30 % | 34.6 px | 0.22 | 1.00 | 510 |
| spiral | 47 % → 47 % | 31.3 px | 0.21 | 1.00 | 498 |
| loop | 25 % → 25 % | 32.5 px | 0.22 | 1.00 | 290 |
| tilted | 11 % → 11 % | 31.8 px | 0.24 | 1.00 | 152 |
| over the wet one | 21 % → 21 % | 26.8 px | 0.24 | 1.00 | 134 |
| long, no reload | 54 % → 54 % | 24.4 px | 0.20 | 1.00 | 736 | quarters: 0.16 → 0.14 → 0.11 → 0.09

Numbers say: light vs heavy: width 24.0 → 35.3 px, dark 0.22 → 0.22.

## Oil — glaze
Oil glaze 1.00 · 40 px · 16.0 s

![Oil — glaze](Oil-glaze.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 9 % → 9 % | 27.0 px | 0.50 | 1.00 | 99 |
| heavy line | 13 % → 13 % | 38.3 px | 0.49 | 1.00 | 141 |
| pressure swell | 10 % → 10 % | 36.6 px | 0.50 | 1.00 | 78 |
| fast wave | 29 % → 29 % | 33.5 px | 0.49 | 1.00 | 273 |
| slow wave | 30 % → 30 % | 34.6 px | 0.50 | 1.00 | 546 |
| spiral | 46 % → 46 % | 30.1 px | 0.49 | 1.00 | 479 |
| loop | 24 % → 24 % | 31.4 px | 0.50 | 1.00 | 244 |
| tilted | 11 % → 11 % | 30.4 px | 0.50 | 1.00 | 133 |
| over the wet one | 23 % → 23 % | 32.5 px | 0.50 | 1.00 | 101 |
| long, no reload | 52 % → 52 % | 23.5 px | 0.49 | 1.00 | 709 | quarters: 0.34 → 0.30 → 0.27 → 0.22

Numbers say: light vs heavy: width 27.0 → 38.3 px, dark 0.50 → 0.49.

## Oil — scumble
Oil 1.00 · 36 px · 15.2 s

![Oil — scumble](Oil-scumble.png)

A light paint: laid on a grey sheet (on white it cannot be seen); **dark** = how far it is from the grey either way.

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 5 % → 5 % | 13.1 px | 0.08 | 1.00 | 138 |
| heavy line | 6 % → 6 % | 17.3 px | 0.26 | 1.00 | 146 |
| pressure swell | 7 % → 7 % | 26.1 px | 0.19 | 1.00 | 93 |
| fast wave | 18 % → 18 % | 21.3 px | 0.18 | 1.00 | 448 |
| slow wave | 23 % → 23 % | 26.7 px | 0.17 | 1.00 | 555 |
| spiral | 30 % → 30 % | 20.0 px | 0.15 | 1.00 | 522 |
| loop | 18 % → 18 % | 23.0 px | 0.16 | 1.00 | 305 |
| tilted | 10 % → 10 % | 26.6 px | 0.22 | 1.00 | 168 |
| over the wet one | 16 % → 16 % | 18.6 px | 0.22 | 1.00 | 147 |
| long, no reload | 32 % → 32 % | 14.6 px | 0.13 | 1.00 | 871 | quarters: 0.01 → 0.00 → 0.00 → 0.00

Numbers say: light vs heavy: width 13.1 → 17.3 px, dark 0.08 → 0.26.

## Acrylic — heavy body
Impasto 0.98 · 30 px · 16.2 s

![Acrylic — heavy body](Acrylic-heavy-body.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 9 % → 7 % | 25.4 px | 0.52 | 0.83 | 100 |
| heavy line | 8 % → 7 % | 24.6 px | 0.52 | 0.88 | 101 |
| pressure swell | 8 % → 7 % | 28.6 px | 0.53 | 0.89 | 79 |
| fast wave | 17 % → 13 % | 19.4 px | 0.52 | 0.78 | 260 |
| slow wave | 19 % → 15 % | 21.6 px | 0.52 | 0.79 | 493 |
| spiral | 24 % → 15 % | 15.8 px | 0.52 | 0.61 | 484 |
| loop | 17 % → 13 % | 22.2 px | 0.52 | 0.78 | 236 |
| tilted | 8 % → 8 % | 23.3 px | 0.53 | 0.99 | 122 |
| over the wet one | 18 % → 15 % | 25.6 px | 0.53 | 0.85 | 106 |
| long, no reload | 31 % → 18 % | 14.0 px | 0.52 | 0.58 | 553 | quarters: 0.26 → 0.16 → 0.11 → 0.09

Numbers say: light vs heavy: width 25.4 → 24.6 px, dark 0.52 → 0.52; pressure barely changes the width.

## Acrylic — fluid
Watercolour 1.00 · 36 px · 31.2 s

![Acrylic — fluid](Acrylic-fluid.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 12 % → 12 % | 33.6 px | 0.24 | 1.01 | 92 |
| heavy line | 18 % → 17 % | 50.9 px | 0.21 | 0.99 | 115 |
| pressure swell | 12 % → 12 % | 45.5 px | 0.23 | 1.01 | 66 |
| fast wave | 39 % → 39 % | 45.1 px | 0.19 | 0.99 | 191 |
| slow wave | 35 % → 35 % | 40.9 px | 0.22 | 1.00 | 334 |
| spiral | 55 % → 54 % | 36.4 px | 0.19 | 0.98 | 323 |
| loop | 31 % → 31 % | 40.0 px | 0.21 | 1.00 | 169 |
| tilted | 13 % → 13 % | 36.0 px | 0.24 | 1.00 | 103 |
| over the wet one | 28 % → 28 % | 42.4 px | 0.24 | 1.01 | 90 |
| long, no reload | 61 % → 58 % | 27.4 px | 0.19 | 0.95 | 581 | quarters: 0.20 → 0.14 → 0.09 → 0.06

Numbers say: light vs heavy: width 33.6 → 50.9 px, dark 0.24 → 0.21.

## Acrylic — palette knife
Impasto 1.00 · 42 px · 19.1 s

![Acrylic — palette knife](Acrylic-palette-knife.png)

A light paint: laid on a grey sheet (on white it cannot be seen); **dark** = how far it is from the grey either way.

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 15 % → 15 % | 44.0 px | 0.39 | 0.98 | 40 |
| heavy line | 15 % → 15 % | 44.3 px | 0.40 | 0.98 | 59 |
| pressure swell | 12 % → 12 % | 43.6 px | 0.42 | 0.99 | 17 |
| fast wave | 36 % → 20 % | 42.0 px | 0.37 | 0.55 | 64 |
| slow wave | 37 % → 21 % | 42.7 px | 0.37 | 0.57 | 114 |
| spiral | 47 % → 18 % | 30.7 px | 0.37 | 0.39 | 130 |
| loop | 32 % → 24 % | 41.3 px | 0.36 | 0.77 | 71 |
| tilted | 12 % → 12 % | 33.7 px | 0.39 | 1.00 | 41 |
| over the wet one | 26 % → 25 % | 39.8 px | 0.39 | 0.97 | 40 |
| long, no reload | 53 % → 20 % | 23.7 px | 0.35 | 0.39 | 175 | quarters: 0.00 → 0.00 → 0.00 → 0.01

Numbers say: light vs heavy: width 44.0 → 44.3 px, dark 0.39 → 0.40; pressure barely changes the width; the long stroke does not run out of paint.

## Finger on oil
Oil 1.00 · 30 px · 13.1 s

![Finger on oil](Finger-on-oil.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 6 % → 6 % | 16.8 px | 0.23 | 1.00 | 57 |
| heavy line | 9 % → 9 % | 27.6 px | 0.28 | 1.00 | 109 |
| pressure swell | 7 % → 7 % | 25.3 px | 0.35 | 1.00 | 76 |
| fast wave | 15 % → 15 % | 17.0 px | 0.12 | 1.00 | 173 |
| slow wave | 16 % → 16 % | 18.6 px | 0.24 | 1.00 | 328 |
| spiral | 28 % → 28 % | 18.2 px | 0.24 | 1.00 | 215 |
| loop | 19 % → 19 % | 24.9 px | 0.28 | 1.00 | 122 |
| tilted | 9 % → 9 % | 26.4 px | 0.28 | 1.00 | 92 |
| over the wet one | 16 % → 16 % | 19.6 px | 0.28 | 1.00 | 50 |
| long, no reload | 36 % → 36 % | 15.9 px | 0.22 | 1.00 | 417 | quarters: 0.12 → 0.11 → 0.07 → 0.04

Numbers say: light vs heavy: width 16.8 → 27.6 px, dark 0.23 → 0.28.

## Palette knife — oil
Oil heavy 0.93 · Impasto 0.07 · 44 px · 17.7 s

![Palette knife — oil](Palette-knife-oil.png)

A light paint: laid on a grey sheet (on white it cannot be seen); **dark** = how far it is from the grey either way.

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 16 % → 14 % | 45.7 px | 0.37 | 0.91 | 51 |
| heavy line | 16 % → 16 % | 46.3 px | 0.38 | 0.98 | 60 |
| pressure swell | 12 % → 12 % | 45.2 px | 0.38 | 0.99 | 17 |
| fast wave | 39 % → 35 % | 44.9 px | 0.35 | 0.89 | 85 |
| slow wave | 39 % → 36 % | 45.4 px | 0.35 | 0.92 | 133 |
| spiral | 62 % → 37 % | 40.7 px | 0.35 | 0.60 | 223 |
| loop | 34 % → 31 % | 43.8 px | 0.36 | 0.92 | 95 |
| tilted | 13 % → 13 % | 36.6 px | 0.37 | 1.00 | 33 |
| over the wet one | 28 % → 27 % | 40.8 px | 0.37 | 0.97 | 38 |
| long, no reload | 74 % → 40 % | 33.0 px | 0.34 | 0.54 | 185 | quarters: 0.00 → 0.00 → 0.01 → 0.01

Numbers say: light vs heavy: width 45.7 → 46.3 px, dark 0.37 → 0.38; pressure barely changes the width; the long stroke does not run out of paint.

## 0.45 · Sponge
Watercolour 0.93 · Ink 0.07 · 46 px · 32.1 s

![0.45 · Sponge](0-45-Sponge.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 27 % → 24 % | 77.5 px | 0.13 | 0.91 | 56 |
| heavy line | 32 % → 28 % | 92.0 px | 0.13 | 0.89 | 94 |
| pressure swell | 24 % → 22 % | 90.9 px | 0.13 | 0.91 | 125 |
| fast wave | 60 % → 54 % | 69.8 px | 0.12 | 0.90 | 190 |
| slow wave | 63 % → 59 % | 72.4 px | 0.17 | 0.94 | 356 |
| spiral | 77 % → 74 % | 51.0 px | 0.16 | 0.96 | 314 |
| loop | 54 % → 51 % | 70.4 px | 0.15 | 0.94 | 168 |
| tilted | 17 % → 17 % | 47.9 px | 0.17 | 1.01 | 115 |
| over the wet one | 45 % → 42 % | 76.8 px | 0.17 | 0.93 | 80 |
| long, no reload | 94 % → 90 % | 42.3 px | 0.17 | 0.96 | 457 | quarters: 0.18 → 0.18 → 0.17 → 0.14

Numbers say: light vs heavy: width 77.5 → 92.0 px, dark 0.13 → 0.13.

## 0.45 · Eraser
Watercolour 1.00 · 30 px · 19.6 s · over bands of wet oil paint and oil pastel in turn (it works on paint already there: look at what it does to the bands; covered counts the bands too)

![0.45 · Eraser](0-45-Eraser.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 24 % → 24 % | 69.2 px | 0.82 | 1.00 | 36 |
| heavy line | 23 % → 23 % | 67.4 px | 0.82 | 1.00 | 51 |
| pressure swell | 23 % → 23 % | 86.8 px | 0.82 | 1.00 | 28 |
| fast wave | 21 % → 21 % | 24.7 px | 0.81 | 1.00 | 134 |
| slow wave | 20 % → 20 % | 23.5 px | 0.82 | 1.00 | 205 |
| spiral | 20 % → 20 % | 13.5 px | 0.79 | 1.00 | 188 |
| loop | 21 % → 21 % | 27.8 px | 0.80 | 1.00 | 121 |
| tilted | 23 % → 23 % | 64.8 px | 0.81 | 1.00 | 48 |
| over the wet one | 22 % → 22 % | 0.0 px | 0.81 | 1.00 | 47 |
| long, no reload | 17 % → 17 % | 7.5 px | 0.79 | 1.00 | 312 | quarters: 0.13 → 0.16 → 0.13 → 0.17

Numbers say: light vs heavy: width 69.2 → 67.4 px, dark 0.82 → 0.82; pressure barely changes the width; the long stroke does not run out of paint.

## Lift wet paint
Watercolour 1.00 · 30 px · 19.4 s · over bands of wet oil paint and oil pastel in turn (it works on paint already there: look at what it does to the bands; covered counts the bands too)

![Lift wet paint](Lift-wet-paint.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 24 % → 24 % | 70.1 px | 0.82 | 1.00 | 28 |
| heavy line | 24 % → 24 % | 69.8 px | 0.82 | 1.00 | 37 |
| pressure swell | 24 % → 24 % | 89.6 px | 0.82 | 1.00 | 25 |
| fast wave | 24 % → 24 % | 27.7 px | 0.82 | 1.00 | 96 |
| slow wave | 24 % → 24 % | 27.7 px | 0.82 | 1.00 | 153 |
| spiral | 24 % → 24 % | 15.9 px | 0.82 | 1.00 | 165 |
| loop | 24 % → 24 % | 31.1 px | 0.82 | 1.00 | 87 |
| tilted | 24 % → 24 % | 66.8 px | 0.82 | 1.00 | 49 |
| over the wet one | 24 % → 24 % | 0.0 px | 0.82 | 1.00 | 36 |
| long, no reload | 24 % → 24 % | 10.7 px | 0.82 | 1.00 | 235 | quarters: 0.18 → 0.24 → 0.17 → 0.24

Numbers say: light vs heavy: width 70.1 → 69.8 px, dark 0.82 → 0.82; pressure barely changes the width; the long stroke does not run out of paint.

## Sgraffito
Watercolour 1.00 · 10 px · 19.0 s · over bands of wet oil paint and oil pastel in turn (it works on paint already there: look at what it does to the bands; covered counts the bands too)

![Sgraffito](Sgraffito.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 24 % → 24 % | 69.9 px | 0.81 | 1.00 | 12 |
| heavy line | 24 % → 24 % | 69.8 px | 0.82 | 1.00 | 10 |
| pressure swell | 24 % → 24 % | 89.6 px | 0.82 | 1.00 | 6 |
| fast wave | 24 % → 24 % | 27.7 px | 0.82 | 1.00 | 38 |
| slow wave | 24 % → 24 % | 27.7 px | 0.82 | 1.00 | 29 |
| spiral | 24 % → 24 % | 15.9 px | 0.82 | 1.00 | 29 |
| loop | 24 % → 24 % | 31.1 px | 0.82 | 1.00 | 21 |
| tilted | 24 % → 24 % | 66.9 px | 0.82 | 1.00 | 7 |
| over the wet one | 24 % → 24 % | 0.0 px | 0.82 | 1.00 | 9 |
| long, no reload | 24 % → 24 % | 10.6 px | 0.82 | 1.00 | 59 | quarters: 0.17 → 0.24 → 0.17 → 0.24

Numbers say: light vs heavy: width 69.9 → 69.8 px, dark 0.81 → 0.82; pressure barely changes the width; the long stroke does not run out of paint.

## Brush Artist · Refs · #01 Henry Ward peach cloud
Gouache 1.00 · 44 px · 29.3 s

![Brush Artist · Refs · #01 Henry Ward peach cloud](Brush-Artist-Refs-01-Henry-Ward-peach-cloud.png)

A light paint: laid on a grey sheet (on white it cannot be seen); **dark** = how far it is from the grey either way.

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 5 % → 0 % | 13.3 px | 0.00 | 0.00 | 121 |
| heavy line | 9 % → 2 % | 24.9 px | 0.33 | 0.26 | 150 |
| pressure swell | 8 % → 5 % | 29.6 px | 0.33 | 0.62 | 102 |
| fast wave | 31 % → 4 % | 35.3 px | 0.32 | 0.12 | 374 |
| slow wave | 22 % → 5 % | 25.1 px | 0.33 | 0.23 | 591 |
| spiral | 35 % → 7 % | 23.2 px | 0.33 | 0.20 | 577 |
| loop | 19 % → 4 % | 24.3 px | 0.32 | 0.22 | 308 |
| tilted | 12 % → 11 % | 32.6 px | 0.32 | 0.98 | 160 |
| over the wet one | 19 % → 8 % | 20.9 px | 0.32 | 0.41 | 125 |
| long, no reload | 35 % → 7 % | 15.7 px | 0.33 | 0.20 | 789 | quarters: 0.02 → 0.02 → 0.03 → 0.03

Numbers say: light vs heavy: width 13.3 → 24.9 px, dark 0.00 → 0.33; the long stroke does not run out of paint.

## Brush Artist · Refs · #02 Henry Ward cream strokes
Gouache 1.00 · 46 px · 29.8 s

![Brush Artist · Refs · #02 Henry Ward cream strokes](Brush-Artist-Refs-02-Henry-Ward-cream-strokes.png)

A light paint: laid on a grey sheet (on white it cannot be seen); **dark** = how far it is from the grey either way.

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 5 % → 0 % | 14.3 px | 0.00 | 0.00 | 109 |
| heavy line | 10 % → 4 % | 27.8 px | 0.41 | 0.45 | 144 |
| pressure swell | 7 % → 3 % | 26.7 px | 0.42 | 0.48 | 101 |
| fast wave | 29 % → 7 % | 33.5 px | 0.39 | 0.23 | 371 |
| slow wave | 25 % → 8 % | 28.8 px | 0.40 | 0.31 | 662 |
| spiral | 43 % → 9 % | 28.4 px | 0.40 | 0.22 | 611 |
| loop | 20 % → 2 % | 25.5 px | 0.39 | 0.11 | 291 |
| tilted | 11 % → 11 % | 31.8 px | 0.40 | 0.97 | 169 |
| over the wet one | 19 % → 7 % | 20.1 px | 0.40 | 0.36 | 123 |
| long, no reload | 27 % → 8 % | 12.3 px | 0.41 | 0.28 | 871 | quarters: 0.02 → 0.04 → 0.03 → 0.04

Numbers say: light vs heavy: width 14.3 → 27.8 px, dark 0.00 → 0.41; the long stroke does not run out of paint.

## Brush Artist · Refs · #03 Henry Ward navy contours
Impasto 1.00 · 22 px · 13.1 s

![Brush Artist · Refs · #03 Henry Ward navy contours](Brush-Artist-Refs-03-Henry-Ward-navy-contours.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 7 % → 6 % | 19.1 px | 0.72 | 0.91 | 65 |
| heavy line | 6 % → 6 % | 18.5 px | 0.71 | 0.92 | 72 |
| pressure swell | 5 % → 5 % | 20.4 px | 0.73 | 0.88 | 49 |
| fast wave | 16 % → 11 % | 18.1 px | 0.73 | 0.72 | 174 |
| slow wave | 17 % → 13 % | 20.2 px | 0.72 | 0.76 | 263 |
| spiral | 27 % → 13 % | 18.0 px | 0.72 | 0.47 | 305 |
| loop | 13 % → 11 % | 16.9 px | 0.72 | 0.84 | 194 |
| tilted | 7 % → 7 % | 19.8 px | 0.72 | 0.99 | 114 |
| over the wet one | 14 % → 13 % | 20.4 px | 0.72 | 0.87 | 99 |
| long, no reload | 33 % → 13 % | 14.7 px | 0.73 | 0.40 | 471 | quarters: 0.34 → 0.27 → 0.20 → 0.11

Numbers say: light vs heavy: width 19.1 → 18.5 px, dark 0.72 → 0.71; pressure barely changes the width.

## Brush Artist · Refs · #04 Henry Ward grey cloud
Gouache 1.00 · 50 px · 30.1 s

![Brush Artist · Refs · #04 Henry Ward grey cloud](Brush-Artist-Refs-04-Henry-Ward-grey-cloud.png)

A light paint: laid on a grey sheet (on white it cannot be seen); **dark** = how far it is from the grey either way.

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 5 % → 0 % | 14.6 px | 0.00 | 0.00 | 113 |
| heavy line | 11 % → 5 % | 31.3 px | 0.32 | 0.50 | 153 |
| pressure swell | 7 % → 3 % | 24.9 px | 0.32 | 0.39 | 105 |
| fast wave | 32 % → 6 % | 36.7 px | 0.32 | 0.18 | 435 |
| slow wave | 26 % → 4 % | 30.3 px | 0.32 | 0.14 | 790 |
| spiral | 44 % → 8 % | 28.8 px | 0.32 | 0.18 | 729 |
| loop | 21 % → 2 % | 26.8 px | 0.32 | 0.08 | 315 |
| tilted | 12 % → 12 % | 32.8 px | 0.31 | 0.98 | 203 |
| over the wet one | 17 % → 7 % | 15.7 px | 0.31 | 0.43 | 139 |
| long, no reload | 28 % → 8 % | 12.7 px | 0.32 | 0.29 | 928 | quarters: 0.02 → 0.03 → 0.03 → 0.04

Numbers say: light vs heavy: width 14.6 → 31.3 px, dark 0.00 → 0.32; the long stroke does not run out of paint.

## Brush Artist · Refs · #05 Henry Ward green in rust loops
Impasto 1.00 · 20 px · 12.9 s

![Brush Artist · Refs · #05 Henry Ward green in rust loops](Brush-Artist-Refs-05-Henry-Ward-green-in-rust-loops.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 6 % → 6 % | 18.2 px | 0.56 | 0.89 | 73 |
| heavy line | 8 % → 7 % | 22.1 px | 0.55 | 0.87 | 75 |
| pressure swell | 4 % → 4 % | 16.5 px | 0.56 | 0.92 | 50 |
| fast wave | 15 % → 10 % | 17.7 px | 0.56 | 0.68 | 194 |
| slow wave | 16 % → 12 % | 18.7 px | 0.56 | 0.72 | 268 |
| spiral | 24 % → 11 % | 16.0 px | 0.56 | 0.45 | 324 |
| loop | 15 % → 12 % | 19.6 px | 0.55 | 0.79 | 172 |
| tilted | 7 % → 7 % | 19.1 px | 0.56 | 0.99 | 99 |
| over the wet one | 13 % → 11 % | 18.1 px | 0.56 | 0.85 | 92 |
| long, no reload | 29 % → 12 % | 12.9 px | 0.56 | 0.40 | 456 | quarters: 0.23 → 0.17 → 0.11 → 0.05

Numbers say: light vs heavy: width 18.2 → 22.1 px, dark 0.56 → 0.55.

## Brush Artist · Refs · #06 Henry Ward scrubbed grey
Gouache 1.00 · 50 px · 30.1 s

![Brush Artist · Refs · #06 Henry Ward scrubbed grey](Brush-Artist-Refs-06-Henry-Ward-scrubbed-grey.png)

A light paint: laid on a grey sheet (on white it cannot be seen); **dark** = how far it is from the grey either way.

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 5 % → 0 % | 14.6 px | 0.00 | 0.00 | 135 |
| heavy line | 11 % → 5 % | 31.3 px | 0.33 | 0.50 | 125 |
| pressure swell | 7 % → 3 % | 24.9 px | 0.33 | 0.39 | 110 |
| fast wave | 32 % → 6 % | 36.7 px | 0.33 | 0.18 | 413 |
| slow wave | 26 % → 4 % | 30.3 px | 0.33 | 0.14 | 666 |
| spiral | 44 % → 8 % | 28.8 px | 0.33 | 0.18 | 698 |
| loop | 21 % → 2 % | 26.8 px | 0.33 | 0.08 | 361 |
| tilted | 12 % → 12 % | 32.8 px | 0.33 | 0.98 | 179 |
| over the wet one | 17 % → 7 % | 15.7 px | 0.33 | 0.43 | 179 |
| long, no reload | 28 % → 8 % | 12.7 px | 0.33 | 0.29 | 920 | quarters: 0.02 → 0.03 → 0.04 → 0.04

Numbers say: light vs heavy: width 14.6 → 31.3 px, dark 0.00 → 0.33; the long stroke does not run out of paint.

## Brush Artist · Refs · #07 Henry Ward blue L + black zigzag
Impasto 1.00 · 34 px · 14.9 s

![Brush Artist · Refs · #07 Henry Ward blue L + black zigzag](Brush-Artist-Refs-07-Henry-Ward-blue-L-black-zigzag.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 10 % → 9 % | 30.1 px | 0.59 | 0.87 | 109 |
| heavy line | 11 % → 10 % | 30.9 px | 0.59 | 0.93 | 108 |
| pressure swell | 8 % → 8 % | 31.9 px | 0.59 | 0.92 | 72 |
| fast wave | 25 % → 19 % | 28.6 px | 0.59 | 0.76 | 277 |
| slow wave | 25 % → 19 % | 29.4 px | 0.59 | 0.75 | 441 |
| spiral | 43 % → 22 % | 28.4 px | 0.59 | 0.52 | 421 |
| loop | 23 % → 19 % | 30.2 px | 0.59 | 0.80 | 224 |
| tilted | 11 % → 11 % | 29.4 px | 0.59 | 1.00 | 103 |
| over the wet one | 22 % → 20 % | 31.8 px | 0.59 | 0.90 | 117 |
| long, no reload | 49 % → 23 % | 22.0 px | 0.59 | 0.47 | 626 | quarters: 0.38 → 0.31 → 0.22 → 0.13

Numbers say: light vs heavy: width 30.1 → 30.9 px, dark 0.59 → 0.59; pressure barely changes the width.

## Brush Artist · Refs · #08 Henry Ward olive bands
Gouache 1.00 · 34 px · 21.1 s

![Brush Artist · Refs · #08 Henry Ward olive bands](Brush-Artist-Refs-08-Henry-Ward-olive-bands.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 2 % → 0 % | 4.8 px | 0.00 | 0.00 | 60 |
| heavy line | 6 % → 1 % | 16.9 px | 0.61 | 0.10 | 124 |
| pressure swell | 5 % → 1 % | 17.1 px | 0.61 | 0.19 | 88 |
| fast wave | 16 % → 1 % | 18.2 px | 0.61 | 0.05 | 266 |
| slow wave | 14 % → 0 % | 16.2 px | 0.61 | 0.01 | 440 |
| spiral | 24 % → 0 % | 15.5 px | 0.61 | 0.01 | 428 |
| loop | 9 % → 1 % | 12.0 px | 0.61 | 0.09 | 247 |
| tilted | 6 % → 6 % | 17.2 px | 0.61 | 0.93 | 129 |
| over the wet one | 9 % → 1 % | 8.9 px | 0.61 | 0.08 | 103 |
| long, no reload | 21 % → 2 % | 9.4 px | 0.61 | 0.09 | 652 | quarters: 0.21 → 0.11 → 0.13 → 0.08

Numbers say: light vs heavy: width 4.8 → 16.9 px, dark 0.00 → 0.61.

## Brush Artist · Refs · #09 Henry Ward white loops
Gouache 1.00 · 46 px · 30.3 s

![Brush Artist · Refs · #09 Henry Ward white loops](Brush-Artist-Refs-09-Henry-Ward-white-loops.png)

A light paint: laid on a grey sheet (on white it cannot be seen); **dark** = how far it is from the grey either way.

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 5 % → 0 % | 14.3 px | 0.00 | 0.00 | 99 |
| heavy line | 10 % → 4 % | 27.8 px | 0.43 | 0.45 | 151 |
| pressure swell | 7 % → 3 % | 26.7 px | 0.44 | 0.48 | 95 |
| fast wave | 29 % → 7 % | 33.5 px | 0.40 | 0.23 | 380 |
| slow wave | 25 % → 8 % | 28.8 px | 0.41 | 0.31 | 671 |
| spiral | 43 % → 9 % | 28.4 px | 0.42 | 0.22 | 658 |
| loop | 20 % → 2 % | 25.5 px | 0.40 | 0.11 | 308 |
| tilted | 11 % → 11 % | 31.8 px | 0.41 | 0.97 | 225 |
| over the wet one | 19 % → 7 % | 20.1 px | 0.41 | 0.36 | 157 |
| long, no reload | 27 % → 8 % | 12.3 px | 0.43 | 0.28 | 850 | quarters: 0.02 → 0.04 → 0.03 → 0.04

Numbers say: light vs heavy: width 14.3 → 27.8 px, dark 0.00 → 0.43; the long stroke does not run out of paint.

## Brush Artist · Refs · #10 Henry Ward maroon loops
Impasto 1.00 · 30 px · 14.3 s

![Brush Artist · Refs · #10 Henry Ward maroon loops](Brush-Artist-Refs-10-Henry-Ward-maroon-loops.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 10 % → 8 % | 28.0 px | 0.72 | 0.87 | 78 |
| heavy line | 11 % → 10 % | 32.1 px | 0.73 | 0.89 | 102 |
| pressure swell | 8 % → 7 % | 29.8 px | 0.74 | 0.91 | 67 |
| fast wave | 23 % → 17 % | 26.1 px | 0.74 | 0.76 | 209 |
| slow wave | 22 % → 18 % | 25.5 px | 0.73 | 0.82 | 396 |
| spiral | 36 % → 18 % | 23.6 px | 0.73 | 0.51 | 409 |
| loop | 17 % → 14 % | 22.2 px | 0.73 | 0.84 | 206 |
| tilted | 10 % → 10 % | 27.1 px | 0.73 | 1.00 | 101 |
| over the wet one | 19 % → 16 % | 26.8 px | 0.73 | 0.85 | 87 |
| long, no reload | 40 % → 17 % | 17.8 px | 0.73 | 0.44 | 605 | quarters: 0.39 → 0.33 → 0.27 → 0.21

Numbers say: light vs heavy: width 28.0 → 32.1 px, dark 0.72 → 0.73.

## Brush Artist · Refs · #11 Henry Ward purple spun balls
Impasto 1.00 · 36 px · 15.3 s

![Brush Artist · Refs · #11 Henry Ward purple spun balls](Brush-Artist-Refs-11-Henry-Ward-purple-spun-balls.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 11 % → 10 % | 31.4 px | 0.74 | 0.93 | 149 |
| heavy line | 11 % → 10 % | 30.6 px | 0.74 | 0.95 | 124 |
| pressure swell | 10 % → 9 % | 36.6 px | 0.75 | 0.93 | 83 |
| fast wave | 27 % → 21 % | 30.7 px | 0.75 | 0.79 | 334 |
| slow wave | 30 % → 24 % | 34.1 px | 0.75 | 0.80 | 567 |
| spiral | 39 % → 23 % | 25.9 px | 0.75 | 0.59 | 466 |
| loop | 24 % → 21 % | 30.6 px | 0.75 | 0.89 | 229 |
| tilted | 10 % → 10 % | 28.1 px | 0.74 | 1.00 | 116 |
| over the wet one | 22 % → 20 % | 33.6 px | 0.74 | 0.90 | 105 |
| long, no reload | 52 % → 25 % | 23.4 px | 0.75 | 0.47 | 598 | quarters: 0.51 → 0.45 → 0.38 → 0.28

Numbers say: light vs heavy: width 31.4 → 30.6 px, dark 0.74 → 0.74; pressure barely changes the width.

## Brush Artist · Refs · #12 Henry Ward black-olive cage
Gouache 1.00 · 28 px · 20.9 s

![Brush Artist · Refs · #12 Henry Ward black-olive cage](Brush-Artist-Refs-12-Henry-Ward-black-olive-cage.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 2 % → 0 % | 5.7 px | 0.00 | 0.00 | 58 |
| heavy line | 5 % → 1 % | 15.0 px | 0.65 | 0.16 | 120 |
| pressure swell | 4 % → 1 % | 15.8 px | 0.65 | 0.19 | 64 |
| fast wave | 12 % → 0 % | 14.4 px | 0.00 | 0.00 | 204 |
| slow wave | 12 % → 1 % | 14.1 px | 0.65 | 0.07 | 377 |
| spiral | 16 % → 0 % | 10.3 px | 0.65 | 0.01 | 347 |
| loop | 10 % → 1 % | 12.6 px | 0.65 | 0.09 | 186 |
| tilted | 5 % → 5 % | 14.5 px | 0.65 | 0.92 | 94 |
| over the wet one | 8 % → 0 % | 8.7 px | 0.65 | 0.03 | 96 |
| long, no reload | 16 % → 2 % | 7.3 px | 0.65 | 0.13 | 518 | quarters: 0.17 → 0.14 → 0.07 → 0.03

Numbers say: light vs heavy: width 5.7 → 15.0 px, dark 0.00 → 0.65.

## Brush Artist · Refs · #13 Henry Ward blue streaky form
Gouache 1.00 · 50 px · 31.0 s

![Brush Artist · Refs · #13 Henry Ward blue streaky form](Brush-Artist-Refs-13-Henry-Ward-blue-streaky-form.png)

A light paint: laid on a grey sheet (on white it cannot be seen); **dark** = how far it is from the grey either way.

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 5 % → 0 % | 14.6 px | 0.00 | 0.00 | 107 |
| heavy line | 11 % → 5 % | 31.3 px | 0.33 | 0.50 | 161 |
| pressure swell | 7 % → 3 % | 24.9 px | 0.33 | 0.39 | 120 |
| fast wave | 32 % → 6 % | 36.7 px | 0.33 | 0.18 | 381 |
| slow wave | 26 % → 4 % | 30.3 px | 0.33 | 0.14 | 588 |
| spiral | 44 % → 8 % | 28.8 px | 0.33 | 0.18 | 705 |
| loop | 21 % → 2 % | 26.8 px | 0.33 | 0.08 | 348 |
| tilted | 12 % → 12 % | 32.8 px | 0.33 | 0.98 | 226 |
| over the wet one | 17 % → 7 % | 15.7 px | 0.33 | 0.43 | 159 |
| long, no reload | 28 % → 8 % | 12.7 px | 0.33 | 0.29 | 917 | quarters: 0.02 → 0.03 → 0.04 → 0.04

Numbers say: light vs heavy: width 14.6 → 31.3 px, dark 0.00 → 0.33; the long stroke does not run out of paint.

## Brush Artist · Refs · #14 Henry Ward olive totem
Impasto 1.00 · 48 px · 17.3 s

![Brush Artist · Refs · #14 Henry Ward olive totem](Brush-Artist-Refs-14-Henry-Ward-olive-totem.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 15 % → 14 % | 44.3 px | 0.31 | 0.92 | 137 |
| heavy line | 16 % → 15 % | 46.4 px | 0.31 | 0.95 | 143 |
| pressure swell | 12 % → 11 % | 44.5 px | 0.31 | 0.94 | 95 |
| fast wave | 36 % → 29 % | 41.2 px | 0.30 | 0.80 | 326 |
| slow wave | 36 % → 31 % | 41.9 px | 0.30 | 0.86 | 571 |
| spiral | 57 % → 34 % | 37.6 px | 0.30 | 0.59 | 578 |
| loop | 30 % → 27 % | 39.1 px | 0.30 | 0.88 | 296 |
| tilted | 13 % → 13 % | 36.2 px | 0.31 | 1.00 | 168 |
| over the wet one | 27 % → 25 % | 40.1 px | 0.31 | 0.92 | 145 |
| long, no reload | 59 % → 32 % | 26.5 px | 0.30 | 0.53 | 926 | quarters: 0.22 → 0.16 → 0.10 → 0.05

Numbers say: light vs heavy: width 44.3 → 46.4 px, dark 0.31 → 0.31; pressure barely changes the width.

## Brush Artist · Refs · #15 Ultramarine brush script
Ink 1.00 · 4 px · 21.1 s

![Brush Artist · Refs · #15 Ultramarine brush script](Brush-Artist-Refs-15-Ultramarine-brush-script.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 1 % → 3 % | 2.1 px | 0.55 | 3.99 | 26 |
| heavy line | 5 % → 5 % | 15.6 px | 0.62 | 1.00 | 39 |
| pressure swell | 3 % → 4 % | 11.0 px | 0.62 | 1.21 | 25 |
| fast wave | 9 % → 7 % | 10.2 px | 0.54 | 0.81 | 84 |
| slow wave | 8 % → 7 % | 8.8 px | 0.53 | 0.89 | 91 |
| spiral | 11 % → 8 % | 7.3 px | 0.53 | 0.68 | 167 |
| loop | 7 % → 7 % | 9.4 px | 0.54 | 0.96 | 82 |
| tilted | 3 % → 3 % | 7.4 px | 0.64 | 1.04 | 31 |
| over the wet one | 7 % → 7 % | 10.7 px | 0.64 | 1.08 | 34 |
| long, no reload | 16 % → 7 % | 7.1 px | 0.51 | 0.47 | 199 | quarters: 0.14 → 0.04 → 0.01 → 0.00

Numbers say: light vs heavy: width 2.1 → 15.6 px, dark 0.55 → 0.62; wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #18 Blue oil-stick scribbles
Pastel 1.00 · 10 px · 9.4 s

![Brush Artist · Refs · #18 Blue oil-stick scribbles](Brush-Artist-Refs-18-Blue-oil-stick-scribbles.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 1 % → 1 % | 2.9 px | 0.53 | 1.00 | 18 |
| heavy line | 2 % → 2 % | 6.0 px | 0.53 | 1.00 | 27 |
| pressure swell | 1 % → 1 % | 5.5 px | 0.52 | 1.00 | 20 |
| fast wave | 5 % → 5 % | 5.3 px | 0.53 | 1.00 | 60 |
| slow wave | 4 % → 4 % | 5.2 px | 0.53 | 1.00 | 60 |
| spiral | 7 % → 7 % | 4.4 px | 0.52 | 1.00 | 83 |
| loop | 4 % → 4 % | 4.6 px | 0.52 | 1.00 | 57 |
| tilted | 2 % → 2 % | 4.4 px | 0.53 | 1.00 | 32 |
| over the wet one | 3 % → 3 % | 4.8 px | 0.53 | 1.00 | 21 |
| long, no reload | 9 % → 9 % | 4.2 px | 0.52 | 1.00 | 145 | quarters: 0.05 → 0.05 → 0.06 → 0.06

Numbers say: light vs heavy: width 2.9 → 6.0 px, dark 0.53 → 0.53; the long stroke does not run out of paint.

## Brush Artist · Refs · #20 Orange-red crayon scribble
Pastel 1.00 · 14 px · 9.8 s

![Brush Artist · Refs · #20 Orange-red crayon scribble](Brush-Artist-Refs-20-Orange-red-crayon-scribble.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 1 % → 1 % | 3.8 px | 0.53 | 1.00 | 15 |
| heavy line | 3 % → 3 % | 8.0 px | 0.53 | 1.00 | 34 |
| pressure swell | 2 % → 2 % | 7.6 px | 0.53 | 1.00 | 28 |
| fast wave | 6 % → 6 % | 7.3 px | 0.53 | 1.00 | 53 |
| slow wave | 6 % → 6 % | 6.9 px | 0.53 | 1.00 | 77 |
| spiral | 9 % → 9 % | 6.0 px | 0.53 | 1.00 | 108 |
| loop | 5 % → 5 % | 6.1 px | 0.53 | 1.00 | 59 |
| tilted | 2 % → 2 % | 5.6 px | 0.53 | 1.00 | 25 |
| over the wet one | 4 % → 4 % | 6.2 px | 0.53 | 1.00 | 23 |
| long, no reload | 12 % → 12 % | 5.4 px | 0.53 | 1.00 | 138 | quarters: 0.07 → 0.07 → 0.07 → 0.07

Numbers say: light vs heavy: width 3.8 → 8.0 px, dark 0.53 → 0.53; the long stroke does not run out of paint.

## Brush Artist · Refs · #21 Gritty black contours
Gouache 1.00 · 12 px · 19.7 s

![Brush Artist · Refs · #21 Gritty black contours](Brush-Artist-Refs-21-Gritty-black-contours.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 1 % → 0 % | 2.7 px | 0.00 | 0.00 | 49 |
| heavy line | 2 % → 0 % | 5.2 px | 0.00 | 0.00 | 98 |
| pressure swell | 1 % → 0 % | 4.7 px | 0.00 | 0.00 | 56 |
| fast wave | 4 % → 0 % | 4.3 px | 0.00 | 0.00 | 179 |
| slow wave | 4 % → 0 % | 4.5 px | 0.82 | 0.00 | 227 |
| spiral | 6 % → 0 % | 4.1 px | 0.81 | 0.02 | 414 |
| loop | 4 % → 0 % | 4.9 px | 0.81 | 0.08 | 170 |
| tilted | 2 % → 2 % | 6.3 px | 0.00 | 0.85 | 86 |
| over the wet one | 3 % → 0 % | 1.9 px | 0.00 | 0.00 | 73 |
| long, no reload | 4 % → 0 % | 2.0 px | 0.81 | 0.00 | 625 | quarters: 0.08 → 0.03 → 0.03 → 0.03

Numbers say: light vs heavy: width 2.7 → 5.2 px, dark 0.00 → 0.00.

## Brush Artist · Refs · #22 Bold black brush poster
Ink 1.00 · 20 px · 27.9 s

![Brush Artist · Refs · #22 Bold black brush poster](Brush-Artist-Refs-22-Bold-black-brush-poster.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 4 % → 5 % | 10.3 px | 0.79 | 1.52 | 32 |
| heavy line | 15 % → 14 % | 42.6 px | 0.88 | 0.99 | 78 |
| pressure swell | 9 % → 9 % | 33.6 px | 0.87 | 1.03 | 43 |
| fast wave | 28 % → 27 % | 32.3 px | 0.88 | 0.98 | 161 |
| slow wave | 23 % → 23 % | 27.0 px | 0.87 | 0.98 | 261 |
| spiral | 35 % → 32 % | 23.0 px | 0.87 | 0.92 | 237 |
| loop | 22 % → 22 % | 28.2 px | 0.88 | 1.00 | 126 |
| tilted | 9 % → 9 % | 24.2 px | 0.88 | 1.00 | 224 |
| over the wet one | 20 % → 20 % | 30.8 px | 0.88 | 1.00 | 61 |
| long, no reload | 48 % → 38 % | 21.3 px | 0.85 | 0.79 | 341 | quarters: 0.56 → 0.45 → 0.35 → 0.26

Numbers say: light vs heavy: width 10.3 → 42.6 px, dark 0.79 → 0.88; wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #23 Dry white on orange + black line
Gouache 1.00 · 50 px · 24.0 s

![Brush Artist · Refs · #23 Dry white on orange + black line](Brush-Artist-Refs-23-Dry-white-on-orange-black-line.png)

A light paint: laid on a grey sheet (on white it cannot be seen); **dark** = how far it is from the grey either way.

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 3 % → 0 % | 8.4 px | 0.00 | 0.00 | 88 |
| heavy line | 8 % → 1 % | 24.1 px | 0.42 | 0.17 | 233 |
| pressure swell | 6 % → 0 % | 22.1 px | 0.41 | 0.02 | 123 |
| fast wave | 21 % → 0 % | 24.4 px | 0.00 | 0.00 | 369 |
| slow wave | 22 % → 0 % | 24.9 px | 0.41 | 0.02 | 733 |
| spiral | 28 % → 0 % | 18.8 px | 0.40 | 0.01 | 610 |
| loop | 17 % → 0 % | 22.4 px | 0.40 | 0.00 | 307 |
| tilted | 9 % → 8 % | 24.1 px | 0.40 | 0.92 | 195 |
| over the wet one | 13 % → 0 % | 11.7 px | 0.40 | 0.02 | 161 |
| long, no reload | 28 % → 3 % | 12.3 px | 0.41 | 0.11 | 942 | quarters: 0.02 → 0.03 → 0.03 → 0.03

Numbers say: light vs heavy: width 8.4 → 24.1 px, dark 0.00 → 0.42; the long stroke does not run out of paint.

## Brush Artist · Refs · #24 Picasso flat oil
Oil 0.89 · Oil glaze 0.11 · 34 px · 15.5 s

![Brush Artist · Refs · #24 Picasso flat oil](Brush-Artist-Refs-24-Picasso-flat-oil.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 10 % → 10 % | 28.8 px | 0.38 | 1.00 | 105 |
| heavy line | 11 % → 11 % | 32.5 px | 0.39 | 1.00 | 124 |
| pressure swell | 8 % → 8 % | 31.6 px | 0.40 | 1.00 | 101 |
| fast wave | 30 % → 30 % | 35.1 px | 0.37 | 1.00 | 305 |
| slow wave | 28 % → 28 % | 32.8 px | 0.39 | 1.00 | 545 |
| spiral | 42 % → 42 % | 27.8 px | 0.38 | 1.00 | 495 |
| loop | 22 % → 22 % | 28.8 px | 0.40 | 1.00 | 257 |
| tilted | 11 % → 11 % | 31.3 px | 0.39 | 1.00 | 177 |
| over the wet one | 20 % → 20 % | 25.3 px | 0.39 | 1.00 | 131 |
| long, no reload | 58 % → 58 % | 26.0 px | 0.38 | 1.00 | 832 | quarters: 0.27 → 0.25 → 0.23 → 0.20

Numbers say: light vs heavy: width 28.8 → 32.5 px, dark 0.38 → 0.39.

## Brush Artist · Refs · #25 Yellow heavy flat stroke
Impasto 1.00 · 110 px · 38.6 s

![Brush Artist · Refs · #25 Yellow heavy flat stroke](Brush-Artist-Refs-25-Yellow-heavy-flat-stroke.png)

A light paint: laid on a grey sheet (on white it cannot be seen); **dark** = how far it is from the grey either way.

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 35 % → 35 % | 101.2 px | 0.30 | 1.00 | 375 |
| heavy line | 36 % → 35 % | 104.3 px | 0.31 | 0.97 | 568 |
| pressure swell | 28 % → 29 % | 104.4 px | 0.31 | 1.05 | 321 |
| fast wave | 72 % → 75 % | 82.9 px | 0.31 | 1.04 | 1015 |
| slow wave | 72 % → 71 % | 83.7 px | 0.30 | 0.98 | 1906 |
| spiral | 85 % → 79 % | 56.4 px | 0.29 | 0.93 | 2762 |
| loop | 64 % → 63 % | 82.8 px | 0.31 | 0.99 | 999 |
| tilted | 25 % → 25 % | 70.3 px | 0.31 | 1.00 | 592 |
| over the wet one | 55 % → 53 % | 83.5 px | 0.31 | 0.97 | 540 |
| long, no reload | 98 % → 96 % | 43.9 px | 0.30 | 0.98 | 2624 | quarters: 0.00 → 0.00 → 0.00 → 0.00

Numbers say: light vs heavy: width 101.2 → 104.3 px, dark 0.30 → 0.31; pressure barely changes the width; the long stroke does not run out of paint.

## Brush Artist · Refs · #27 Orange impasto swatch
Impasto 1.00 · 60 px · 22.8 s

![Brush Artist · Refs · #27 Orange impasto swatch](Brush-Artist-Refs-27-Orange-impasto-swatch.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 18 % → 18 % | 53.5 px | 0.34 | 0.97 | 196 |
| heavy line | 21 % → 20 % | 59.9 px | 0.34 | 0.96 | 213 |
| pressure swell | 15 % → 15 % | 58.1 px | 0.35 | 0.97 | 115 |
| fast wave | 48 % → 47 % | 55.3 px | 0.34 | 0.97 | 442 |
| slow wave | 46 % → 45 % | 53.6 px | 0.34 | 0.97 | 869 |
| spiral | 68 % → 61 % | 44.9 px | 0.34 | 0.89 | 825 |
| loop | 40 % → 39 % | 52.0 px | 0.34 | 0.97 | 478 |
| tilted | 16 % → 16 % | 43.7 px | 0.35 | 1.00 | 368 |
| over the wet one | 34 % → 33 % | 50.2 px | 0.35 | 0.97 | 358 |
| long, no reload | 84 % → 75 % | 37.7 px | 0.34 | 0.89 | 1312 | quarters: 0.32 → 0.31 → 0.30 → 0.26

Numbers say: light vs heavy: width 53.5 → 59.9 px, dark 0.34 → 0.34.

## Brush Artist · Refs · #28 Miles Davis black lines
Ink 1.00 · 22 px · 31.0 s

![Brush Artist · Refs · #28 Miles Davis black lines](Brush-Artist-Refs-28-Miles-Davis-black-lines.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 4 % → 6 % | 12.3 px | 0.80 | 1.40 | 35 |
| heavy line | 16 % → 16 % | 45.9 px | 0.88 | 0.99 | 82 |
| pressure swell | 10 % → 10 % | 36.7 px | 0.87 | 1.03 | 45 |
| fast wave | 29 % → 29 % | 33.8 px | 0.88 | 0.99 | 164 |
| slow wave | 27 % → 26 % | 30.7 px | 0.88 | 0.99 | 237 |
| spiral | 39 % → 36 % | 25.4 px | 0.87 | 0.93 | 245 |
| loop | 24 % → 24 % | 31.0 px | 0.88 | 1.00 | 140 |
| tilted | 9 % → 9 % | 26.0 px | 0.88 | 1.01 | 166 |
| over the wet one | 21 % → 21 % | 32.9 px | 0.88 | 1.00 | 80 |
| long, no reload | 53 % → 45 % | 23.9 px | 0.85 | 0.83 | 417 | quarters: 0.61 → 0.53 → 0.41 → 0.31

Numbers say: light vs heavy: width 12.3 → 45.9 px, dark 0.80 → 0.88.

## Brush Artist · Refs · #29 Shrigley magenta asterisk
Watercolour 1.00 · 70 px · 35.6 s

![Brush Artist · Refs · #29 Shrigley magenta asterisk](Brush-Artist-Refs-29-Shrigley-magenta-asterisk.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 10 % → 13 % | 28.0 px | 0.61 | 1.39 | 71 |
| heavy line | 17 % → 18 % | 50.3 px | 0.61 | 1.04 | 134 |
| pressure swell | 11 % → 13 % | 41.1 px | 0.62 | 1.14 | 91 |
| fast wave | 38 % → 38 % | 43.8 px | 0.60 | 1.01 | 283 |
| slow wave | 35 % → 39 % | 41.0 px | 0.62 | 1.11 | 564 |
| spiral | 61 % → 61 % | 40.0 px | 0.60 | 1.01 | 690 |
| loop | 31 % → 32 % | 40.2 px | 0.61 | 1.03 | 243 |
| tilted | 18 % → 18 % | 49.0 px | 0.61 | 1.00 | 199 |
| over the wet one | 31 % → 34 % | 38.5 px | 0.61 | 1.08 | 106 |
| long, no reload | 75 % → 76 % | 33.6 px | 0.60 | 1.01 | 818 | quarters: 0.53 → 0.50 → 0.48 → 0.45

Numbers say: light vs heavy: width 28.0 → 50.3 px, dark 0.61 → 0.61; the long stroke does not run out of paint.

## Brush Artist · Refs · #30 Red gouache face patch
Gouache 1.00 · 60 px · 43.5 s

![Brush Artist · Refs · #30 Red gouache face patch](Brush-Artist-Refs-30-Red-gouache-face-patch.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 16 % → 15 % | 47.0 px | 0.49 | 0.91 | 155 |
| heavy line | 25 % → 20 % | 73.9 px | 0.49 | 0.80 | 234 |
| pressure swell | 19 % → 17 % | 72.6 px | 0.49 | 0.86 | 261 |
| fast wave | 49 % → 28 % | 56.1 px | 0.49 | 0.58 | 458 |
| slow wave | 48 % → 28 % | 55.4 px | 0.49 | 0.59 | 823 |
| spiral | 60 % → 28 % | 39.3 px | 0.49 | 0.47 | 802 |
| loop | 40 % → 29 % | 51.6 px | 0.49 | 0.74 | 358 |
| tilted | 16 % → 17 % | 46.0 px | 0.49 | 1.00 | 222 |
| over the wet one | 36 % → 32 % | 55.3 px | 0.49 | 0.89 | 207 |
| long, no reload | 67 % → 30 % | 30.0 px | 0.49 | 0.44 | 1164 | quarters: 0.43 → 0.39 → 0.32 → 0.26

Numbers say: light vs heavy: width 47.0 → 73.9 px, dark 0.49 → 0.49.

## Brush Artist · Refs · #31 Warhol blotted line
Ink 1.00 · 6 px · 25.3 s

![Brush Artist · Refs · #31 Warhol blotted line](Brush-Artist-Refs-31-Warhol-blotted-line.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 1 % → 4 % | 3.0 px | 0.72 | 3.49 | 24 |
| heavy line | 7 % → 7 % | 19.5 px | 0.84 | 0.98 | 54 |
| pressure swell | 4 % → 4 % | 14.2 px | 0.82 | 1.18 | 29 |
| fast wave | 12 % → 9 % | 13.6 px | 0.81 | 0.73 | 104 |
| slow wave | 11 % → 9 % | 12.3 px | 0.80 | 0.80 | 84 |
| spiral | 15 % → 9 % | 10.0 px | 0.79 | 0.58 | 188 |
| loop | 10 % → 9 % | 12.6 px | 0.80 | 0.94 | 93 |
| tilted | 4 % → 4 % | 11.0 px | 0.83 | 1.03 | 45 |
| over the wet one | 9 % → 9 % | 14.0 px | 0.83 | 1.05 | 40 |
| long, no reload | 21 % → 10 % | 9.5 px | 0.78 | 0.45 | 305 | quarters: 0.25 → 0.13 → 0.05 → 0.01

Numbers say: light vs heavy: width 3.0 → 19.5 px, dark 0.72 → 0.84; wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #32 Thick orange swipes
Impasto 1.00 · 90 px · 34.6 s

![Brush Artist · Refs · #32 Thick orange swipes](Brush-Artist-Refs-32-Thick-orange-swipes.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 29 % → 28 % | 83.7 px | 0.37 | 0.99 | 353 |
| heavy line | 30 % → 29 % | 86.8 px | 0.37 | 0.97 | 309 |
| pressure swell | 23 % → 23 % | 85.2 px | 0.37 | 1.01 | 193 |
| fast wave | 64 % → 66 % | 74.3 px | 0.37 | 1.02 | 799 |
| slow wave | 64 % → 62 % | 73.9 px | 0.37 | 0.97 | 1429 |
| spiral | 80 % → 74 % | 52.5 px | 0.37 | 0.93 | 1625 |
| loop | 56 % → 55 % | 72.9 px | 0.37 | 0.98 | 780 |
| tilted | 21 % → 21 % | 58.9 px | 0.37 | 1.00 | 450 |
| over the wet one | 46 % → 45 % | 70.8 px | 0.37 | 0.96 | 413 |
| long, no reload | 95 % → 92 % | 42.8 px | 0.37 | 0.97 | 2854 | quarters: 0.37 → 0.37 → 0.36 → 0.35

Numbers say: light vs heavy: width 83.7 → 86.8 px, dark 0.37 → 0.37; pressure barely changes the width; the long stroke does not run out of paint.

## Brush Artist · Refs · #33 Red wet-in-wet band
Watercolour 1.00 · 80 px · 51.2 s

![Brush Artist · Refs · #33 Red wet-in-wet band](Brush-Artist-Refs-33-Red-wet-in-wet-band.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 24 % → 42 % | 69.3 px | 0.54 | 1.75 | 126 |
| heavy line | 33 % → 48 % | 96.9 px | 0.55 | 1.45 | 238 |
| pressure swell | 19 % → 30 % | 72.1 px | 0.57 | 1.56 | 154 |
| fast wave | 65 % → 79 % | 75.5 px | 0.60 | 1.21 | 474 |
| slow wave | 61 % → 78 % | 70.5 px | 0.63 | 1.28 | 1180 |
| spiral | 77 % → 89 % | 50.8 px | 0.64 | 1.15 | 833 |
| loop | 54 % → 67 % | 70.5 px | 0.62 | 1.23 | 494 |
| tilted | 28 % → 30 % | 78.0 px | 0.58 | 1.09 | 362 |
| over the wet one | 55 % → 79 % | 76.7 px | 0.58 | 1.43 | 259 |
| long, no reload | 96 % → 99 % | 42.9 px | 0.66 | 1.04 | 1436 | quarters: 0.68 → 0.68 → 0.68 → 0.64

Numbers say: light vs heavy: width 69.3 → 96.9 px, dark 0.54 → 0.55; the long stroke does not run out of paint; wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #34 Magenta oil patches
Oil 0.89 · Oil glaze 0.11 · 60 px · 21.6 s

![Brush Artist · Refs · #34 Magenta oil patches](Brush-Artist-Refs-34-Magenta-oil-patches.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 18 % → 18 % | 51.4 px | 0.61 | 1.00 | 183 |
| heavy line | 19 % → 19 % | 55.0 px | 0.61 | 1.00 | 220 |
| pressure swell | 15 % → 15 % | 54.5 px | 0.61 | 1.01 | 167 |
| fast wave | 44 % → 45 % | 51.1 px | 0.61 | 1.02 | 634 |
| slow wave | 45 % → 45 % | 52.4 px | 0.61 | 1.00 | 1362 |
| spiral | 68 % → 68 % | 44.8 px | 0.61 | 1.00 | 1254 |
| loop | 42 % → 42 % | 54.2 px | 0.61 | 1.00 | 736 |
| tilted | 17 % → 17 % | 46.2 px | 0.61 | 1.00 | 776 |
| over the wet one | 34 % → 34 % | 48.4 px | 0.61 | 1.00 | 341 |
| long, no reload | 83 % → 83 % | 37.0 px | 0.61 | 1.00 | 1844 | quarters: 0.57 → 0.56 → 0.55 → 0.49

Numbers say: light vs heavy: width 51.4 → 55.0 px, dark 0.61 → 0.61; pressure barely changes the width; the long stroke does not run out of paint.

## Brush Artist · Refs · #35 Red band with runs
Watercolour 1.00 · 70 px · 53.0 s

![Brush Artist · Refs · #35 Red band with runs](Brush-Artist-Refs-35-Red-band-with-runs.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 40 % → 45 % | 115.3 px | 0.42 | 1.14 | 178 |
| heavy line | 45 % → 50 % | 132.0 px | 0.42 | 1.09 | 324 |
| pressure swell | 20 % → 28 % | 76.7 px | 0.48 | 1.37 | 229 |
| fast wave | 66 % → 76 % | 76.8 px | 0.49 | 1.14 | 658 |
| slow wave | 65 % → 76 % | 75.6 px | 0.52 | 1.16 | 1005 |
| spiral | 86 % → 94 % | 56.9 px | 0.53 | 1.09 | 951 |
| loop | 79 % → 88 % | 102.7 px | 0.49 | 1.11 | 538 |
| tilted | 50 % → 51 % | 139.1 px | 0.47 | 1.02 | 317 |
| over the wet one | 78 % → 84 % | 77.5 px | 0.47 | 1.09 | 196 |
| long, no reload | 96 % → 100 % | 43.2 px | 0.58 | 1.04 | 1347 | quarters: 0.59 → 0.60 → 0.59 → 0.56

Numbers say: light vs heavy: width 115.3 → 132.0 px, dark 0.42 → 0.42; the long stroke does not run out of paint.

## Brush Artist · Refs · #36 Magenta letters flat brush
Gouache 1.00 · 36 px · 37.3 s

![Brush Artist · Refs · #36 Magenta letters flat brush](Brush-Artist-Refs-36-Magenta-letters-flat-brush.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 10 % → 10 % | 29.0 px | 0.45 | 0.98 | 136 |
| heavy line | 17 % → 14 % | 49.0 px | 0.45 | 0.85 | 160 |
| pressure swell | 13 % → 12 % | 49.3 px | 0.45 | 0.89 | 74 |
| fast wave | 35 % → 19 % | 40.9 px | 0.45 | 0.54 | 680 |
| slow wave | 35 % → 19 % | 40.0 px | 0.45 | 0.54 | 458 |
| spiral | 46 % → 19 % | 30.4 px | 0.45 | 0.42 | 449 |
| loop | 27 % → 20 % | 35.4 px | 0.45 | 0.72 | 290 |
| tilted | 11 % → 11 % | 30.0 px | 0.45 | 1.00 | 132 |
| over the wet one | 24 % → 23 % | 38.1 px | 0.45 | 0.93 | 110 |
| long, no reload | 46 % → 19 % | 20.8 px | 0.45 | 0.40 | 633 | quarters: 0.29 → 0.26 → 0.22 → 0.18

Numbers say: light vs heavy: width 29.0 → 49.0 px, dark 0.45 → 0.45.

## Brush Artist · Refs · #37 Oil still life dabs
Oil 0.89 · Oil glaze 0.11 · 40 px · 16.7 s

![Brush Artist · Refs · #37 Oil still life dabs](Brush-Artist-Refs-37-Oil-still-life-dabs.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 11 % → 11 % | 31.9 px | 0.36 | 1.00 | 227 |
| heavy line | 12 % → 12 % | 36.1 px | 0.39 | 1.00 | 171 |
| pressure swell | 10 % → 10 % | 39.2 px | 0.38 | 1.00 | 133 |
| fast wave | 30 % → 30 % | 35.0 px | 0.37 | 1.00 | 549 |
| slow wave | 35 % → 35 % | 40.5 px | 0.37 | 1.00 | 716 |
| spiral | 52 % → 52 % | 34.3 px | 0.38 | 1.00 | 816 |
| loop | 29 % → 29 % | 36.9 px | 0.38 | 1.00 | 340 |
| tilted | 12 % → 12 % | 34.7 px | 0.38 | 1.00 | 189 |
| over the wet one | 23 % → 23 % | 30.6 px | 0.38 | 1.00 | 146 |
| long, no reload | 59 % → 59 % | 26.5 px | 0.37 | 1.00 | 1057 | quarters: 0.28 → 0.25 → 0.23 → 0.20

Numbers say: light vs heavy: width 31.9 → 36.1 px, dark 0.36 → 0.39.

## Brush Artist · Refs · #38 Sanguine drawing
Pastel 1.00 · 6 px · 9.9 s

![Brush Artist · Refs · #38 Sanguine drawing](Brush-Artist-Refs-38-Sanguine-drawing.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 1 % → 1 % | 2.1 px | 0.61 | 1.00 | 15 |
| heavy line | 1 % → 1 % | 3.9 px | 0.61 | 1.00 | 17 |
| pressure swell | 1 % → 1 % | 3.8 px | 0.61 | 1.00 | 8 |
| fast wave | 3 % → 3 % | 3.4 px | 0.61 | 1.00 | 58 |
| slow wave | 3 % → 3 % | 3.4 px | 0.61 | 1.00 | 62 |
| spiral | 4 % → 4 % | 2.8 px | 0.61 | 1.00 | 70 |
| loop | 2 % → 2 % | 3.1 px | 0.61 | 1.00 | 52 |
| tilted | 1 % → 1 % | 3.4 px | 0.61 | 1.00 | 21 |
| over the wet one | 2 % → 2 % | 2.9 px | 0.61 | 1.00 | 16 |
| long, no reload | 6 % → 6 % | 2.7 px | 0.61 | 1.00 | 129 | quarters: 0.04 → 0.04 → 0.04 → 0.04

Numbers say: light vs heavy: width 2.1 → 3.9 px, dark 0.61 → 0.61; the long stroke does not run out of paint.

## Brush Artist · Refs · #39 Very thick impasto
Impasto 1.00 · 60 px · 23.1 s

![Brush Artist · Refs · #39 Very thick impasto](Brush-Artist-Refs-39-Very-thick-impasto.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 19 % → 18 % | 53.7 px | 0.61 | 0.97 | 192 |
| heavy line | 21 % → 20 % | 59.8 px | 0.62 | 0.96 | 224 |
| pressure swell | 16 % → 15 % | 58.3 px | 0.62 | 0.97 | 145 |
| fast wave | 48 % → 47 % | 55.4 px | 0.62 | 0.98 | 596 |
| slow wave | 47 % → 45 % | 53.9 px | 0.62 | 0.97 | 832 |
| spiral | 68 % → 63 % | 45.1 px | 0.62 | 0.92 | 1005 |
| loop | 40 % → 39 % | 52.2 px | 0.62 | 0.97 | 463 |
| tilted | 16 % → 16 % | 43.8 px | 0.62 | 1.00 | 254 |
| over the wet one | 34 % → 33 % | 50.3 px | 0.62 | 0.97 | 236 |
| long, no reload | 85 % → 79 % | 37.9 px | 0.62 | 0.93 | 1385 | quarters: 0.57 → 0.56 → 0.55 → 0.52

Numbers say: light vs heavy: width 53.7 → 59.8 px, dark 0.61 → 0.62; the long stroke does not run out of paint.

## Brush Artist · Refs · #40 Watercolour blooms
Watercolour 1.00 · 90 px · 52.6 s

![Brush Artist · Refs · #40 Watercolour blooms](Brush-Artist-Refs-40-Watercolour-blooms.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 27 % → 47 % | 78.4 px | 0.08 | 1.72 | 177 |
| heavy line | 38 % → 51 % | 110.0 px | 0.09 | 1.36 | 360 |
| pressure swell | 24 % → 39 % | 91.8 px | 0.09 | 1.61 | 194 |
| fast wave | 68 % → 82 % | 78.3 px | 0.11 | 1.21 | 586 |
| slow wave | 68 % → 81 % | 79.1 px | 0.15 | 1.18 | 1220 |
| spiral | 81 % → 92 % | 53.5 px | 0.14 | 1.14 | 1116 |
| loop | 58 % → 72 % | 75.3 px | 0.13 | 1.24 | 653 |
| tilted | 34 % → 36 % | 94.8 px | 0.11 | 1.07 | 354 |
| over the wet one | 62 % → 81 % | 78.2 px | 0.11 | 1.31 | 268 |
| long, no reload | 97 % → 100 % | 43.6 px | 0.17 | 1.03 | 1483 | quarters: 0.21 → 0.20 → 0.17 → 0.13

Numbers say: light vs heavy: width 78.4 → 110.0 px, dark 0.08 → 0.09; wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #41 Coloured pencil hatching
Pastel 1.00 · 4 px · 9.9 s

![Brush Artist · Refs · #41 Coloured pencil hatching](Brush-Artist-Refs-41-Coloured-pencil-hatching.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 1 % → 1 % | 1.6 px | 0.43 | 1.00 | 14 |
| heavy line | 1 % → 1 % | 2.9 px | 0.43 | 1.00 | 11 |
| pressure swell | 1 % → 1 % | 2.8 px | 0.43 | 1.00 | 16 |
| fast wave | 2 % → 2 % | 2.5 px | 0.43 | 1.00 | 65 |
| slow wave | 2 % → 2 % | 2.5 px | 0.43 | 1.00 | 28 |
| spiral | 3 % → 3 % | 2.1 px | 0.43 | 1.00 | 57 |
| loop | 2 % → 2 % | 2.3 px | 0.43 | 1.00 | 26 |
| tilted | 1 % → 1 % | 3.0 px | 0.43 | 1.00 | 18 |
| over the wet one | 2 % → 2 % | 2.3 px | 0.43 | 1.00 | 20 |
| long, no reload | 5 % → 5 % | 2.0 px | 0.42 | 1.00 | 66 | quarters: 0.02 → 0.02 → 0.02 → 0.02

Numbers say: light vs heavy: width 1.6 → 2.9 px, dark 0.43 → 0.43; the long stroke does not run out of paint.

## Brush Artist · Refs · #42 Oil pastel shaggy
Pastel 1.00 · 18 px · 10.1 s

![Brush Artist · Refs · #42 Oil pastel shaggy](Brush-Artist-Refs-42-Oil-pastel-shaggy.png)

A light paint: laid on a grey sheet (on white it cannot be seen); **dark** = how far it is from the grey either way.

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 2 % → 2 % | 4.7 px | 0.36 | 1.00 | 34 |
| heavy line | 3 % → 3 % | 10.0 px | 0.36 | 1.00 | 30 |
| pressure swell | 2 % → 2 % | 9.3 px | 0.37 | 1.00 | 19 |
| fast wave | 8 % → 8 % | 9.2 px | 0.36 | 1.00 | 128 |
| slow wave | 7 % → 7 % | 8.6 px | 0.36 | 1.00 | 99 |
| spiral | 11 % → 11 % | 7.5 px | 0.36 | 1.00 | 118 |
| loop | 6 % → 6 % | 7.8 px | 0.36 | 1.00 | 52 |
| tilted | 2 % → 2 % | 6.5 px | 0.36 | 1.00 | 33 |
| over the wet one | 5 % → 5 % | 7.6 px | 0.36 | 1.00 | 27 |
| long, no reload | 15 % → 15 % | 6.5 px | 0.36 | 1.00 | 164 | quarters: 0.00 → 0.00 → 0.00 → 0.00

Numbers say: light vs heavy: width 4.7 → 10.0 px, dark 0.36 → 0.36; the long stroke does not run out of paint.

## Brush Artist · Refs · #43 Dragged black ink blocks
Gouache 1.00 · 70 px · 26.9 s

![Brush Artist · Refs · #43 Dragged black ink blocks](Brush-Artist-Refs-43-Dragged-black-ink-blocks.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 4 % → 0 % | 13.0 px | 0.00 | 0.00 | 109 |
| heavy line | 13 % → 3 % | 37.3 px | 0.66 | 0.22 | 413 |
| pressure swell | 10 % → 3 % | 37.6 px | 0.66 | 0.33 | 179 |
| fast wave | 34 % → 1 % | 39.3 px | 0.66 | 0.02 | 563 |
| slow wave | 28 % → 1 % | 32.6 px | 0.66 | 0.04 | 989 |
| spiral | 45 % → 2 % | 29.7 px | 0.66 | 0.05 | 816 |
| loop | 27 % → 2 % | 34.7 px | 0.66 | 0.06 | 514 |
| tilted | 11 % → 11 % | 31.3 px | 0.66 | 0.95 | 260 |
| over the wet one | 19 % → 1 % | 21.9 px | 0.66 | 0.07 | 197 |
| long, no reload | 40 % → 7 % | 17.9 px | 0.66 | 0.17 | 1192 | quarters: 0.44 → 0.36 → 0.17 → 0.14

Numbers say: light vs heavy: width 13.0 → 37.3 px, dark 0.00 → 0.66.

## Brush Artist · Refs · #44 Blue looping ribbon
Oil 1.00 · 80 px · 26.5 s

![Brush Artist · Refs · #44 Blue looping ribbon](Brush-Artist-Refs-44-Blue-looping-ribbon.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 25 % → 26 % | 73.0 px | 0.72 | 1.04 | 387 |
| heavy line | 27 % → 27 % | 77.6 px | 0.72 | 1.00 | 347 |
| pressure swell | 20 % → 21 % | 76.3 px | 0.71 | 1.03 | 201 |
| fast wave | 62 % → 64 % | 71.3 px | 0.72 | 1.04 | 755 |
| slow wave | 58 % → 58 % | 67.4 px | 0.72 | 1.00 | 1388 |
| spiral | 76 % → 76 % | 50.2 px | 0.72 | 1.00 | 1392 |
| loop | 53 % → 53 % | 69.0 px | 0.71 | 1.00 | 754 |
| tilted | 20 % → 20 % | 56.0 px | 0.72 | 1.00 | 447 |
| over the wet one | 41 % → 41 % | 58.7 px | 0.72 | 1.00 | 407 |
| long, no reload | 89 % → 89 % | 40.1 px | 0.72 | 1.00 | 1956 | quarters: 0.69 → 0.70 → 0.68 → 0.61

Numbers say: light vs heavy: width 73.0 → 77.6 px, dark 0.72 → 0.72; pressure barely changes the width; the long stroke does not run out of paint.

## Brush Artist · Refs · #45 Soft pastel pepper
Pastel 1.00 · 40 px · 10.8 s

![Brush Artist · Refs · #45 Soft pastel pepper](Brush-Artist-Refs-45-Soft-pastel-pepper.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 4 % → 4 % | 11.0 px | 0.53 | 1.00 | 48 |
| heavy line | 7 % → 7 % | 21.2 px | 0.53 | 1.00 | 52 |
| pressure swell | 5 % → 5 % | 19.0 px | 0.53 | 1.00 | 30 |
| fast wave | 17 % → 17 % | 19.3 px | 0.53 | 1.00 | 132 |
| slow wave | 16 % → 16 % | 18.0 px | 0.53 | 1.00 | 234 |
| spiral | 23 % → 23 % | 15.4 px | 0.53 | 1.00 | 213 |
| loop | 12 % → 12 % | 15.4 px | 0.53 | 1.00 | 125 |
| tilted | 4 % → 4 % | 11.4 px | 0.53 | 1.00 | 69 |
| over the wet one | 10 % → 10 % | 16.7 px | 0.53 | 1.00 | 63 |
| long, no reload | 28 % → 28 % | 12.6 px | 0.53 | 1.00 | 349 | quarters: 0.17 → 0.16 → 0.17 → 0.17

Numbers say: light vs heavy: width 11.0 → 21.2 px, dark 0.53 → 0.53; the long stroke does not run out of paint.

## Brush Artist · Refs · #46 Red-brown ink lips
Watercolour 1.00 · 50 px · 42.1 s

![Brush Artist · Refs · #46 Red-brown ink lips](Brush-Artist-Refs-46-Red-brown-ink-lips.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 15 % → 31 % | 43.9 px | 0.59 | 2.04 | 61 |
| heavy line | 22 % → 35 % | 63.4 px | 0.60 | 1.58 | 109 |
| pressure swell | 13 % → 22 % | 50.3 px | 0.63 | 1.64 | 79 |
| fast wave | 43 % → 64 % | 49.7 px | 0.64 | 1.50 | 282 |
| slow wave | 42 % → 63 % | 49.1 px | 0.67 | 1.49 | 433 |
| spiral | 65 % → 79 % | 42.6 px | 0.69 | 1.22 | 457 |
| loop | 38 % → 55 % | 48.8 px | 0.67 | 1.47 | 220 |
| tilted | 21 % → 23 % | 58.2 px | 0.60 | 1.11 | 121 |
| over the wet one | 42 % → 63 % | 58.5 px | 0.60 | 1.51 | 96 |
| long, no reload | 78 % → 95 % | 35.1 px | 0.70 | 1.21 | 676 | quarters: 0.71 → 0.71 → 0.69 → 0.65

Numbers say: light vs heavy: width 43.9 → 63.4 px, dark 0.59 → 0.60; the long stroke does not run out of paint; wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #47 Pink knife slabs
Impasto 1.00 · 90 px · 25.1 s

![Brush Artist · Refs · #47 Pink knife slabs](Brush-Artist-Refs-47-Pink-knife-slabs.png)

A light paint: laid on a grey sheet (on white it cannot be seen); **dark** = how far it is from the grey either way.

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 27 % → 26 % | 78.9 px | 0.30 | 0.97 | 247 |
| heavy line | 29 % → 28 % | 84.5 px | 0.29 | 0.96 | 277 |
| pressure swell | 22 % → 22 % | 81.3 px | 0.29 | 1.01 | 150 |
| fast wave | 62 % → 61 % | 71.6 px | 0.28 | 0.98 | 556 |
| slow wave | 62 % → 58 % | 71.3 px | 0.28 | 0.93 | 1116 |
| spiral | 74 % → 60 % | 48.6 px | 0.27 | 0.81 | 1231 |
| loop | 56 % → 54 % | 72.0 px | 0.28 | 0.97 | 547 |
| tilted | 22 % → 22 % | 60.3 px | 0.29 | 1.00 | 287 |
| over the wet one | 46 % → 45 % | 69.5 px | 0.29 | 0.96 | 277 |
| long, no reload | 93 % → 77 % | 41.5 px | 0.26 | 0.83 | 1542 | quarters: 0.00 → 0.00 → 0.00 → 0.00

Numbers say: light vs heavy: width 78.9 → 84.5 px, dark 0.30 → 0.29; pressure barely changes the width; the long stroke does not run out of paint.

## Brush Artist · Refs · #48 Black bands with drips
Gouache 1.00 · 70 px · 46.7 s

![Brush Artist · Refs · #48 Black bands with drips](Brush-Artist-Refs-48-Black-bands-with-drips.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 27 % → 24 % | 79.0 px | 0.64 | 0.87 | 185 |
| heavy line | 35 % → 29 % | 102.8 px | 0.64 | 0.82 | 278 |
| pressure swell | 25 % → 22 % | 91.9 px | 0.64 | 0.89 | 209 |
| fast wave | 64 % → 43 % | 74.0 px | 0.64 | 0.67 | 689 |
| slow wave | 61 % → 41 % | 70.7 px | 0.64 | 0.67 | 1022 |
| spiral | 69 % → 39 % | 45.7 px | 0.64 | 0.56 | 980 |
| loop | 54 % → 42 % | 70.4 px | 0.64 | 0.77 | 543 |
| tilted | 29 % → 29 % | 80.7 px | 0.64 | 1.00 | 333 |
| over the wet one | 58 % → 49 % | 80.4 px | 0.64 | 0.85 | 243 |
| long, no reload | 78 % → 39 % | 34.9 px | 0.64 | 0.50 | 1340 | quarters: 0.61 → 0.57 → 0.51 → 0.42

Numbers say: light vs heavy: width 79.0 → 102.8 px, dark 0.64 → 0.64.

## Brush Artist · Refs · #49 Magenta letters round brush
Ink 1.00 · 30 px · 32.3 s

![Brush Artist · Refs · #49 Magenta letters round brush](Brush-Artist-Refs-49-Magenta-letters-round-brush.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 6 % → 8 % | 18.1 px | 0.49 | 1.21 | 44 |
| heavy line | 21 % → 20 % | 60.3 px | 0.51 | 0.98 | 108 |
| pressure swell | 13 % → 13 % | 47.1 px | 0.51 | 1.01 | 74 |
| fast wave | 38 % → 38 % | 44.0 px | 0.51 | 1.00 | 225 |
| slow wave | 34 % → 34 % | 39.4 px | 0.51 | 0.99 | 328 |
| spiral | 49 % → 48 % | 32.6 px | 0.51 | 0.96 | 281 |
| loop | 30 % → 30 % | 38.3 px | 0.51 | 1.00 | 199 |
| tilted | 11 % → 12 % | 32.0 px | 0.52 | 1.00 | 108 |
| over the wet one | 27 % → 27 % | 42.2 px | 0.52 | 1.01 | 77 |
| long, no reload | 63 % → 56 % | 28.2 px | 0.50 | 0.90 | 593 | quarters: 0.42 → 0.37 → 0.30 → 0.25

Numbers say: light vs heavy: width 18.1 → 60.3 px, dark 0.49 → 0.51.

## Brush Artist · Refs · #50 Thick swipes on photo
Impasto 1.00 · 40 px · 18.1 s

![Brush Artist · Refs · #50 Thick swipes on photo](Brush-Artist-Refs-50-Thick-swipes-on-photo.png)

A light paint: laid on a grey sheet (on white it cannot be seen); **dark** = how far it is from the grey either way.

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 13 % → 13 % | 38.6 px | 0.27 | 0.96 | 121 |
| heavy line | 14 % → 13 % | 40.0 px | 0.27 | 0.96 | 144 |
| pressure swell | 11 % → 10 % | 40.1 px | 0.26 | 0.95 | 115 |
| fast wave | 35 % → 31 % | 40.0 px | 0.26 | 0.90 | 325 |
| slow wave | 34 % → 32 % | 39.5 px | 0.26 | 0.93 | 609 |
| spiral | 58 % → 45 % | 38.2 px | 0.25 | 0.78 | 552 |
| loop | 29 % → 28 % | 37.4 px | 0.26 | 0.96 | 291 |
| tilted | 12 % → 12 % | 33.7 px | 0.27 | 1.00 | 124 |
| over the wet one | 25 % → 24 % | 36.6 px | 0.27 | 0.96 | 127 |
| long, no reload | 67 % → 46 % | 30.1 px | 0.24 | 0.69 | 903 | quarters: 0.00 → 0.00 → 0.00 → 0.00

Numbers say: light vs heavy: width 38.6 → 40.0 px, dark 0.27 → 0.27; pressure barely changes the width.

## Brush Artist · Refs · Drag #e8b4a8
Gouache 1.00 · 40 px · 17.3 s

![Brush Artist · Refs · Drag #e8b4a8](Brush-Artist-Refs-Drag-e8b4a8.png)

A light paint: laid on a grey sheet (on white it cannot be seen); **dark** = how far it is from the grey either way.

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 3 % → 0 % | 7.5 px | 0.00 | 0.00 | 83 |
| heavy line | 5 % → 0 % | 13.4 px | 0.34 | 0.02 | 134 |
| pressure swell | 3 % → 0 % | 11.2 px | 0.00 | 0.00 | 94 |
| fast wave | 13 % → 0 % | 15.1 px | 0.00 | 0.00 | 352 |
| slow wave | 11 % → 0 % | 12.7 px | 0.00 | 0.00 | 611 |
| spiral | 17 % → 0 % | 11.0 px | 0.00 | 0.00 | 552 |
| loop | 11 % → 0 % | 14.4 px | 0.00 | 0.00 | 250 |
| tilted | 5 % → 4 % | 13.1 px | 0.00 | 0.77 | 227 |
| over the wet one | 5 % → 0 % | 1.4 px | 0.00 | 0.00 | 106 |
| long, no reload | 9 % → 0 % | 3.9 px | 0.00 | 0.00 | 762 | quarters: 0.01 → 0.01 → 0.01 → 0.01

Numbers say: light vs heavy: width 7.5 → 13.4 px, dark 0.00 → 0.34; the long stroke does not run out of paint.

## Brush Artist · Refs · Drag #e8e4e0
Gouache 1.00 · 40 px · 18.3 s

![Brush Artist · Refs · Drag #e8e4e0](Brush-Artist-Refs-Drag-e8e4e0.png)

A light paint: laid on a grey sheet (on white it cannot be seen); **dark** = how far it is from the grey either way.

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 3 % → 0 % | 7.5 px | 0.00 | 0.00 | 109 |
| heavy line | 5 % → 0 % | 13.4 px | 0.43 | 0.02 | 122 |
| pressure swell | 3 % → 0 % | 11.2 px | 0.00 | 0.00 | 103 |
| fast wave | 13 % → 0 % | 15.1 px | 0.00 | 0.00 | 343 |
| slow wave | 11 % → 0 % | 12.7 px | 0.00 | 0.00 | 613 |
| spiral | 17 % → 0 % | 11.0 px | 0.00 | 0.00 | 544 |
| loop | 11 % → 0 % | 14.4 px | 0.00 | 0.00 | 247 |
| tilted | 5 % → 4 % | 13.1 px | 0.00 | 0.77 | 181 |
| over the wet one | 5 % → 0 % | 1.4 px | 0.00 | 0.00 | 105 |
| long, no reload | 9 % → 0 % | 3.9 px | 0.00 | 0.00 | 730 | quarters: 0.01 → 0.01 → 0.02 → 0.02

Numbers say: light vs heavy: width 7.5 → 13.4 px, dark 0.00 → 0.43; the long stroke does not run out of paint.

## Brush Artist · Refs · Finger
Pastel 1.00 · 36 px · 22.1 s · over bands of wet oil paint and oil pastel in turn (it works on paint already there: look at what it does to the bands; covered counts the bands too)

![Brush Artist · Refs · Finger](Brush-Artist-Refs-Finger.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 25 % → 25 % | 73.8 px | 0.80 | 1.00 | 46 |
| heavy line | 27 % → 27 % | 78.6 px | 0.80 | 1.00 | 45 |
| pressure swell | 26 % → 26 % | 97.7 px | 0.80 | 1.00 | 41 |
| fast wave | 32 % → 32 % | 37.3 px | 0.78 | 1.00 | 165 |
| slow wave | 31 % → 31 % | 36.3 px | 0.78 | 1.00 | 207 |
| spiral | 38 % → 38 % | 25.2 px | 0.76 | 1.00 | 213 |
| loop | 30 % → 30 % | 39.5 px | 0.78 | 1.00 | 139 |
| tilted | 26 % → 26 % | 73.4 px | 0.78 | 1.00 | 69 |
| over the wet one | 29 % → 29 % | 6.8 px | 0.78 | 1.00 | 58 |
| long, no reload | 41 % → 41 % | 18.2 px | 0.76 | 1.00 | 419 | quarters: 0.25 → 0.37 → 0.34 → 0.39

Numbers say: light vs heavy: width 73.8 → 78.6 px, dark 0.80 → 0.80; pressure barely changes the width; the long stroke does not run out of paint.

## Brush Artist · Ink — wash
Watercolour 1.00 · 38 px · 33.1 s

![Brush Artist · Ink — wash](Brush-Artist-Ink-wash.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 11 % → 11 % | 31.6 px | 0.39 | 1.04 | 65 |
| heavy line | 19 % → 19 % | 54.3 px | 0.32 | 1.03 | 99 |
| pressure swell | 12 % → 13 % | 45.2 px | 0.37 | 1.04 | 41 |
| fast wave | 39 % → 41 % | 45.5 px | 0.31 | 1.04 | 159 |
| slow wave | 37 % → 38 % | 42.9 px | 0.37 | 1.03 | 346 |
| spiral | 58 % → 61 % | 38.6 px | 0.31 | 1.04 | 462 |
| loop | 32 % → 33 % | 41.9 px | 0.35 | 1.02 | 159 |
| tilted | 13 % → 14 % | 37.0 px | 0.38 | 1.04 | 108 |
| over the wet one | 29 % → 30 % | 42.8 px | 0.38 | 1.04 | 69 |
| long, no reload | 67 % → 72 % | 30.0 px | 0.29 | 1.07 | 507 | quarters: 0.34 → 0.27 → 0.19 → 0.12

Numbers say: light vs heavy: width 31.6 → 54.3 px, dark 0.39 → 0.32.

## Brush Artist · Ink — brush line
Ink 1.00 · 16 px · 28.5 s

![Brush Artist · Ink — brush line](Brush-Artist-Ink-brush-line.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 3 % → 5 % | 8.2 px | 0.77 | 1.72 | 35 |
| heavy line | 12 % → 12 % | 35.2 px | 0.88 | 0.99 | 101 |
| pressure swell | 8 % → 8 % | 28.5 px | 0.86 | 1.06 | 44 |
| fast wave | 24 % → 24 % | 28.2 px | 0.87 | 0.98 | 160 |
| slow wave | 20 % → 20 % | 23.7 px | 0.87 | 0.97 | 191 |
| spiral | 31 % → 27 % | 20.3 px | 0.86 | 0.87 | 245 |
| loop | 19 % → 19 % | 24.3 px | 0.87 | 0.99 | 119 |
| tilted | 8 % → 8 % | 21.2 px | 0.88 | 1.01 | 97 |
| over the wet one | 17 % → 17 % | 26.2 px | 0.88 | 1.01 | 81 |
| long, no reload | 44 % → 31 % | 19.7 px | 0.84 | 0.70 | 462 | quarters: 0.51 → 0.41 → 0.30 → 0.20

Numbers say: light vs heavy: width 8.2 → 35.2 px, dark 0.77 → 0.88; wet paint spreads well beyond the stroke.

## Brush Artist · Ink — dry brush
Gouache 1.00 · 30 px · 21.5 s

![Brush Artist · Ink — dry brush](Brush-Artist-Ink-dry-brush.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 2 % → 0 % | 5.7 px | 0.00 | 0.00 | 64 |
| heavy line | 4 % → 0 % | 10.2 px | 0.77 | 0.01 | 141 |
| pressure swell | 4 % → 0 % | 14.1 px | 0.77 | 0.06 | 73 |
| fast wave | 12 % → 0 % | 14.0 px | 0.77 | 0.00 | 314 |
| slow wave | 10 % → 0 % | 11.9 px | 0.77 | 0.00 | 562 |
| spiral | 17 % → 0 % | 11.1 px | 0.77 | 0.00 | 337 |
| loop | 9 % → 0 % | 11.2 px | 0.77 | 0.01 | 206 |
| tilted | 5 % → 4 % | 13.5 px | 0.77 | 0.89 | 92 |
| over the wet one | 7 % → 0 % | 5.9 px | 0.77 | 0.00 | 111 |
| long, no reload | 14 % → 1 % | 6.5 px | 0.77 | 0.08 | 689 | quarters: 0.21 → 0.14 → 0.10 → 0.07

Numbers say: light vs heavy: width 5.7 → 10.2 px, dark 0.00 → 0.77.

## Brush Artist · Watercolour — blue
Watercolour 0.93 · Ink 0.07 · 40 px · 31.4 s

![Brush Artist · Watercolour — blue](Brush-Artist-Watercolour-blue.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 6 % → 11 % | 16.2 px | 0.29 | 1.88 | 28 |
| heavy line | 11 % → 13 % | 31.9 px | 0.29 | 1.17 | 102 |
| pressure swell | 7 % → 9 % | 25.7 px | 0.30 | 1.38 | 51 |
| fast wave | 24 % → 27 % | 28.2 px | 0.29 | 1.12 | 170 |
| slow wave | 23 % → 32 % | 26.4 px | 0.31 | 1.41 | 397 |
| spiral | 39 % → 47 % | 25.6 px | 0.29 | 1.21 | 226 |
| loop | 20 % → 25 % | 25.7 px | 0.30 | 1.25 | 120 |
| tilted | 12 % → 12 % | 34.0 px | 0.30 | 1.00 | 102 |
| over the wet one | 21 % → 25 % | 25.2 px | 0.30 | 1.19 | 70 |
| long, no reload | 53 % → 59 % | 23.6 px | 0.30 | 1.12 | 483 | quarters: 0.23 → 0.21 → 0.19 → 0.16

Numbers say: light vs heavy: width 16.2 → 31.9 px, dark 0.29 → 0.29; wet paint spreads well beyond the stroke.

## Brush Artist · Watercolour — violet
Watercolour 0.93 · Ink 0.07 · 40 px · 30.1 s

![Brush Artist · Watercolour — violet](Brush-Artist-Watercolour-violet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 6 % → 11 % | 16.2 px | 0.36 | 1.88 | 34 |
| heavy line | 11 % → 13 % | 31.9 px | 0.37 | 1.17 | 69 |
| pressure swell | 7 % → 9 % | 25.7 px | 0.38 | 1.38 | 43 |
| fast wave | 24 % → 27 % | 28.2 px | 0.38 | 1.12 | 149 |
| slow wave | 23 % → 32 % | 26.4 px | 0.39 | 1.41 | 263 |
| spiral | 39 % → 47 % | 25.6 px | 0.37 | 1.21 | 227 |
| loop | 20 % → 25 % | 25.7 px | 0.38 | 1.25 | 132 |
| tilted | 12 % → 12 % | 34.0 px | 0.38 | 1.00 | 88 |
| over the wet one | 21 % → 25 % | 25.2 px | 0.38 | 1.19 | 57 |
| long, no reload | 53 % → 59 % | 23.6 px | 0.38 | 1.12 | 409 | quarters: 0.28 → 0.27 → 0.24 → 0.21

Numbers say: light vs heavy: width 16.2 → 31.9 px, dark 0.36 → 0.37; wet paint spreads well beyond the stroke.

## Brush Artist · Watercolour — teal
Watercolour 0.93 · Ink 0.07 · 40 px · 30.2 s

![Brush Artist · Watercolour — teal](Brush-Artist-Watercolour-teal.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 6 % → 11 % | 16.2 px | 0.23 | 1.88 | 41 |
| heavy line | 11 % → 13 % | 31.9 px | 0.23 | 1.17 | 88 |
| pressure swell | 7 % → 9 % | 25.7 px | 0.24 | 1.38 | 32 |
| fast wave | 24 % → 27 % | 28.2 px | 0.23 | 1.12 | 159 |
| slow wave | 23 % → 32 % | 26.4 px | 0.25 | 1.41 | 235 |
| spiral | 39 % → 47 % | 25.6 px | 0.23 | 1.21 | 212 |
| loop | 20 % → 25 % | 25.7 px | 0.24 | 1.25 | 124 |
| tilted | 12 % → 12 % | 34.0 px | 0.24 | 1.00 | 97 |
| over the wet one | 21 % → 25 % | 25.2 px | 0.24 | 1.19 | 63 |
| long, no reload | 53 % → 59 % | 23.6 px | 0.24 | 1.12 | 409 | quarters: 0.18 → 0.16 → 0.15 → 0.13

Numbers say: light vs heavy: width 16.2 → 31.9 px, dark 0.23 → 0.23; wet paint spreads well beyond the stroke.

## Brush Artist · Gouache
Gouache 1.00 · 30 px · 32.7 s

![Brush Artist · Gouache](Brush-Artist-Gouache.png)

A light paint: laid on a grey sheet (on white it cannot be seen); **dark** = how far it is from the grey either way.

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 8 % → 8 % | 24.4 px | 0.27 | 0.97 | 79 |
| heavy line | 15 % → 12 % | 42.8 px | 0.27 | 0.78 | 93 |
| pressure swell | 11 % → 9 % | 41.0 px | 0.27 | 0.85 | 81 |
| fast wave | 30 % → 14 % | 34.9 px | 0.26 | 0.45 | 190 |
| slow wave | 29 % → 14 % | 34.0 px | 0.26 | 0.47 | 309 |
| spiral | 40 % → 14 % | 26.6 px | 0.26 | 0.35 | 334 |
| loop | 24 % → 15 % | 30.6 px | 0.26 | 0.62 | 231 |
| tilted | 10 % → 10 % | 27.4 px | 0.27 | 1.01 | 111 |
| over the wet one | 22 % → 19 % | 32.9 px | 0.27 | 0.89 | 90 |
| long, no reload | 43 % → 15 % | 19.1 px | 0.26 | 0.35 | 471 | quarters: 0.01 → 0.01 → 0.01 → 0.01

Numbers say: light vs heavy: width 24.4 → 42.8 px, dark 0.27 → 0.27; the long stroke does not run out of paint.

## Brush Artist · Oil — bristle
Oil 0.89 · Oil glaze 0.11 · 30 px · 15.1 s

![Brush Artist · Oil — bristle](Brush-Artist-Oil-bristle.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 10 % → 10 % | 28.5 px | 0.53 | 1.00 | 110 |
| heavy line | 11 % → 11 % | 32.4 px | 0.54 | 1.00 | 125 |
| pressure swell | 8 % → 8 % | 31.8 px | 0.54 | 1.00 | 60 |
| fast wave | 28 % → 28 % | 32.0 px | 0.54 | 1.00 | 304 |
| slow wave | 27 % → 27 % | 31.6 px | 0.54 | 1.00 | 489 |
| spiral | 48 % → 48 % | 31.3 px | 0.53 | 1.00 | 493 |
| loop | 22 % → 22 % | 28.9 px | 0.54 | 1.00 | 231 |
| tilted | 11 % → 11 % | 29.9 px | 0.54 | 1.00 | 141 |
| over the wet one | 21 % → 21 % | 29.6 px | 0.54 | 1.00 | 138 |
| long, no reload | 55 % → 55 % | 24.7 px | 0.52 | 1.00 | 869 | quarters: 0.35 → 0.33 → 0.31 → 0.29

Numbers say: light vs heavy: width 28.5 → 32.4 px, dark 0.53 → 0.54.

## Brush Artist · Charcoal — stick
Charcoal 0.78 · Pastel 0.22 · 28 px · 10.7 s

![Brush Artist · Charcoal — stick](Brush-Artist-Charcoal-stick.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 5 % → 5 % | 15.2 px | 0.85 | 1.00 | 12 |
| heavy line | 8 % → 8 % | 24.2 px | 0.85 | 1.00 | 17 |
| pressure swell | 5 % → 5 % | 19.3 px | 0.85 | 1.00 | 22 |
| fast wave | 19 % → 19 % | 21.5 px | 0.85 | 1.00 | 82 |
| slow wave | 18 % → 18 % | 21.1 px | 0.85 | 1.00 | 141 |
| spiral | 25 % → 25 % | 16.3 px | 0.85 | 1.00 | 97 |
| loop | 16 % → 16 % | 20.2 px | 0.85 | 1.00 | 47 |
| tilted | 6 % → 6 % | 17.3 px | 0.85 | 1.00 | 25 |
| over the wet one | 14 % → 14 % | 20.5 px | 0.85 | 1.00 | 25 |
| long, no reload | 41 % → 41 % | 18.5 px | 0.85 | 1.00 | 198 | quarters: 0.39 → 0.39 → 0.39 → 0.39

Numbers say: light vs heavy: width 15.2 → 24.2 px, dark 0.85 → 0.85; the long stroke does not run out of paint.

## Brush Artist · Charcoal — stick B
Charcoal 0.78 · Pastel 0.22 · 36 px · 10.7 s

![Brush Artist · Charcoal — stick B](Brush-Artist-Charcoal-stick-B.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 7 % → 7 % | 19.2 px | 0.85 | 1.00 | 24 |
| heavy line | 10 % → 10 % | 30.5 px | 0.85 | 1.00 | 37 |
| pressure swell | 7 % → 7 % | 24.5 px | 0.85 | 1.00 | 28 |
| fast wave | 24 % → 24 % | 27.6 px | 0.85 | 1.00 | 104 |
| slow wave | 23 % → 23 % | 26.6 px | 0.85 | 1.00 | 168 |
| spiral | 35 % → 35 % | 23.2 px | 0.85 | 1.00 | 188 |
| loop | 19 % → 19 % | 25.2 px | 0.85 | 1.00 | 91 |
| tilted | 7 % → 7 % | 20.3 px | 0.85 | 1.00 | 39 |
| over the wet one | 17 % → 17 % | 25.9 px | 0.85 | 1.00 | 35 |
| long, no reload | 50 % → 50 % | 22.6 px | 0.85 | 1.00 | 255 | quarters: 0.47 → 0.47 → 0.47 → 0.47

Numbers say: light vs heavy: width 19.2 → 30.5 px, dark 0.85 → 0.85; the long stroke does not run out of paint.

## Brush Artist · Charcoal — stick C
Charcoal 0.78 · Pastel 0.22 · 22 px · 10.0 s

![Brush Artist · Charcoal — stick C](Brush-Artist-Charcoal-stick-C.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 4 % → 4 % | 12.2 px | 0.85 | 1.00 | 16 |
| heavy line | 7 % → 7 % | 19.4 px | 0.85 | 1.00 | 23 |
| pressure swell | 4 % → 4 % | 14.3 px | 0.85 | 1.00 | 18 |
| fast wave | 15 % → 15 % | 17.1 px | 0.85 | 1.00 | 54 |
| slow wave | 15 % → 15 % | 17.0 px | 0.85 | 1.00 | 84 |
| spiral | 20 % → 20 % | 13.3 px | 0.85 | 1.00 | 76 |
| loop | 12 % → 12 % | 16.1 px | 0.85 | 1.00 | 44 |
| tilted | 5 % → 5 % | 15.1 px | 0.85 | 1.00 | 28 |
| over the wet one | 11 % → 11 % | 16.8 px | 0.85 | 1.00 | 25 |
| long, no reload | 34 % → 34 % | 15.3 px | 0.85 | 1.00 | 141 | quarters: 0.33 → 0.32 → 0.32 → 0.32

Numbers say: light vs heavy: width 12.2 → 19.4 px, dark 0.85 → 0.85; the long stroke does not run out of paint.

## Oil · Henry Ward · Loaded flat
Oil 1.00 · 46 px · 19.8 s

![Oil · Henry Ward · Loaded flat](Oil-Henry-Ward-Loaded-flat.png)

A light paint: laid on a grey sheet (on white it cannot be seen); **dark** = how far it is from the grey either way.

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 8 % → 8 % | 22.0 px | 0.30 | 1.00 | 154 |
| heavy line | 15 % → 15 % | 43.2 px | 0.37 | 1.00 | 191 |
| pressure swell | 11 % → 11 % | 40.8 px | 0.34 | 1.00 | 146 |
| fast wave | 32 % → 32 % | 36.7 px | 0.32 | 1.00 | 473 |
| slow wave | 26 % → 26 % | 30.4 px | 0.33 | 1.00 | 719 |
| spiral | 50 % → 50 % | 32.9 px | 0.30 | 1.00 | 950 |
| loop | 27 % → 27 % | 35.3 px | 0.34 | 1.00 | 385 |
| tilted | 13 % → 13 % | 35.9 px | 0.34 | 1.00 | 239 |
| over the wet one | 26 % → 26 % | 36.5 px | 0.34 | 1.00 | 167 |
| long, no reload | 47 % → 47 % | 21.2 px | 0.30 | 1.00 | 1075 | quarters: 0.00 → 0.00 → 0.00 → 0.00

Numbers say: light vs heavy: width 22.0 → 43.2 px, dark 0.30 → 0.37; the long stroke does not run out of paint.

## Oil · Henry Ward · Dry scrub
Oil 1.00 · 50 px · 15.5 s

![Oil · Henry Ward · Dry scrub](Oil-Henry-Ward-Dry-scrub.png)

A light paint: laid on a grey sheet (on white it cannot be seen); **dark** = how far it is from the grey either way.

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 5 % → 5 % | 15.2 px | 0.18 | 1.00 | 151 |
| heavy line | 9 % → 9 % | 25.5 px | 0.24 | 1.00 | 154 |
| pressure swell | 7 % → 7 % | 27.9 px | 0.26 | 1.00 | 126 |
| fast wave | 26 % → 26 % | 29.8 px | 0.25 | 1.01 | 497 |
| slow wave | 27 % → 27 % | 30.9 px | 0.24 | 1.00 | 851 |
| spiral | 43 % → 43 % | 28.6 px | 0.20 | 1.00 | 877 |
| loop | 21 % → 21 % | 26.9 px | 0.25 | 1.00 | 369 |
| tilted | 12 % → 12 % | 33.3 px | 0.24 | 1.00 | 215 |
| over the wet one | 17 % → 17 % | 15.0 px | 0.24 | 1.00 | 151 |
| long, no reload | 33 % → 33 % | 14.8 px | 0.22 | 1.00 | 993 | quarters: 0.00 → 0.00 → 0.00 → 0.00

Numbers say: light vs heavy: width 15.2 → 25.5 px, dark 0.18 → 0.24; the long stroke does not run out of paint.

## Oil · Henry Ward · Dirty contour
Oil 1.00 · 24 px · 13.6 s

![Oil · Henry Ward · Dirty contour](Oil-Henry-Ward-Dirty-contour.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 8 % → 8 % | 21.8 px | 0.75 | 1.00 | 91 |
| heavy line | 8 % → 8 % | 24.4 px | 0.74 | 1.00 | 109 |
| pressure swell | 7 % → 7 % | 26.8 px | 0.76 | 1.00 | 86 |
| fast wave | 18 % → 18 % | 21.2 px | 0.74 | 1.00 | 280 |
| slow wave | 21 % → 21 % | 24.0 px | 0.76 | 1.00 | 478 |
| spiral | 30 % → 30 % | 20.0 px | 0.74 | 1.00 | 609 |
| loop | 16 % → 16 % | 21.3 px | 0.76 | 1.00 | 252 |
| tilted | 9 % → 9 % | 25.4 px | 0.75 | 1.00 | 114 |
| over the wet one | 17 % → 17 % | 22.7 px | 0.75 | 1.00 | 91 |
| long, no reload | 39 % → 39 % | 17.7 px | 0.73 | 1.00 | 720 | quarters: 0.43 → 0.35 → 0.28 → 0.23

Numbers say: light vs heavy: width 21.8 → 24.4 px, dark 0.75 → 0.74.

## Oil · Henry Ward · Wet drag
Oil 1.00 · 44 px · 15.6 s

![Oil · Henry Ward · Wet drag](Oil-Henry-Ward-Wet-drag.png)

A light paint: laid on a grey sheet (on white it cannot be seen); **dark** = how far it is from the grey either way.

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 8 % → 8 % | 24.2 px | 0.22 | 1.00 | 135 |
| heavy line | 10 % → 10 % | 29.1 px | 0.34 | 1.00 | 187 |
| pressure swell | 10 % → 10 % | 35.9 px | 0.29 | 1.00 | 121 |
| fast wave | 29 % → 29 % | 33.7 px | 0.29 | 1.00 | 448 |
| slow wave | 31 % → 31 % | 35.8 px | 0.27 | 1.00 | 867 |
| spiral | 50 % → 50 % | 33.1 px | 0.26 | 1.00 | 684 |
| loop | 23 % → 23 % | 29.5 px | 0.33 | 1.00 | 320 |
| tilted | 12 % → 12 % | 33.1 px | 0.30 | 1.00 | 216 |
| over the wet one | 24 % → 24 % | 33.3 px | 0.30 | 1.00 | 173 |
| long, no reload | 54 % → 54 % | 24.0 px | 0.28 | 1.00 | 970 | quarters: 0.00 → 0.00 → 0.00 → 0.00

Numbers say: light vs heavy: width 24.2 → 29.1 px, dark 0.22 → 0.34; the long stroke does not run out of paint.

## Oil · Henry Ward · Thin veil
Oil 0.81 · Ink 0.19 · 56 px · 32.5 s

![Oil · Henry Ward · Thin veil](Oil-Henry-Ward-Thin-veil.png)

A light paint: laid on a grey sheet (on white it cannot be seen); **dark** = how far it is from the grey either way.

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 6 % → 4 % | 18.6 px | 0.08 | 0.67 | 148 |
| heavy line | 13 % → 12 % | 37.3 px | 0.27 | 0.92 | 210 |
| pressure swell | 10 % → 8 % | 37.0 px | 0.19 | 0.81 | 139 |
| fast wave | 38 % → 31 % | 43.4 px | 0.14 | 0.81 | 599 |
| slow wave | 36 % → 33 % | 42.0 px | 0.17 | 0.91 | 880 |
| spiral | 61 % → 49 % | 40.0 px | 0.15 | 0.80 | 865 |
| loop | 28 % → 24 % | 36.2 px | 0.16 | 0.85 | 392 |
| tilted | 14 % → 15 % | 40.4 px | 0.16 | 1.02 | 229 |
| over the wet one | 24 % → 21 % | 26.4 px | 0.16 | 0.86 | 197 |
| long, no reload | 55 % → 44 % | 24.7 px | 0.16 | 0.79 | 1262 | quarters: 0.01 → 0.01 → 0.01 → 0.01

Numbers say: light vs heavy: width 18.6 → 37.3 px, dark 0.08 → 0.27; the long stroke does not run out of paint.

## Oil · Henry Ward · Ground
Gouache 1.00 · 160 px · 66.3 s

![Oil · Henry Ward · Ground](Oil-Henry-Ward-Ground.png)

A light paint: laid on a grey sheet (on white it cannot be seen); **dark** = how far it is from the grey either way.

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 51 % → 45 % | 147.8 px | 0.37 | 0.89 | 733 |
| heavy line | 52 % → 47 % | 150.7 px | 0.37 | 0.91 | 838 |
| pressure swell | 41 % → 45 % | 153.1 px | 0.37 | 1.09 | 595 |
| fast wave | 83 % → 83 % | 95.7 px | 0.37 | 1.00 | 1991 |
| slow wave | 85 % → 70 % | 98.0 px | 0.37 | 0.82 | 3867 |
| spiral | 88 % → 75 % | 58.1 px | 0.36 | 0.85 | 3648 |
| loop | 74 % → 67 % | 96.4 px | 0.37 | 0.90 | 1751 |
| tilted | 38 % → 38 % | 107.0 px | 0.37 | 1.00 | 890 |
| over the wet one | 76 % → 70 % | 104.5 px | 0.37 | 0.92 | 877 |
| long, no reload | 96 % → 81 % | 43.1 px | 0.36 | 0.84 | 4725 | quarters: 0.00 → 0.00 → 0.00 → 0.00

Numbers say: light vs heavy: width 147.8 → 150.7 px, dark 0.37 → 0.37; pressure barely changes the width.

## Oil · Henry Ward · HW #02 cream over wet olive
Oil 0.81 · Ink 0.19 · 56 px · 34.1 s

![Oil · Henry Ward · HW #02 cream over wet olive](Oil-Henry-Ward-HW-02-cream-over-wet-olive.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 6 % → 4 % | 18.6 px | 0.62 | 0.67 | 158 |
| heavy line | 13 % → 12 % | 37.3 px | 0.67 | 0.92 | 252 |
| pressure swell | 10 % → 8 % | 37.0 px | 0.64 | 0.81 | 148 |
| fast wave | 38 % → 31 % | 43.4 px | 0.65 | 0.81 | 492 |
| slow wave | 36 % → 33 % | 42.0 px | 0.66 | 0.91 | 831 |
| spiral | 61 % → 49 % | 40.0 px | 0.64 | 0.80 | 814 |
| loop | 28 % → 24 % | 36.2 px | 0.65 | 0.85 | 428 |
| tilted | 14 % → 15 % | 40.4 px | 0.64 | 1.02 | 254 |
| over the wet one | 24 % → 21 % | 26.4 px | 0.64 | 0.86 | 203 |
| long, no reload | 55 % → 44 % | 24.7 px | 0.64 | 0.79 | 1467 | quarters: 0.45 → 0.29 → 0.25 → 0.28

Numbers say: light vs heavy: width 18.6 → 37.3 px, dark 0.62 → 0.67.

## Oil · Henry Ward · HW #04 grey arcs over ochre
Oil 1.00 · 46 px · 18.7 s

![Oil · Henry Ward · HW #04 grey arcs over ochre](Oil-Henry-Ward-HW-04-grey-arcs-over-ochre.png)

A light paint: laid on a grey sheet (on white it cannot be seen); **dark** = how far it is from the grey either way.

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 8 % → 8 % | 22.0 px | 0.22 | 1.00 | 133 |
| heavy line | 15 % → 15 % | 43.2 px | 0.28 | 1.00 | 163 |
| pressure swell | 11 % → 11 % | 40.8 px | 0.25 | 1.00 | 114 |
| fast wave | 32 % → 32 % | 36.7 px | 0.23 | 1.00 | 392 |
| slow wave | 26 % → 26 % | 30.4 px | 0.25 | 1.00 | 642 |
| spiral | 50 % → 50 % | 32.9 px | 0.22 | 1.00 | 686 |
| loop | 27 % → 27 % | 35.3 px | 0.25 | 1.00 | 377 |
| tilted | 13 % → 13 % | 35.9 px | 0.25 | 1.00 | 215 |
| over the wet one | 26 % → 26 % | 36.5 px | 0.25 | 1.00 | 325 |
| long, no reload | 47 % → 47 % | 21.2 px | 0.22 | 1.00 | 1225 | quarters: 0.00 → 0.01 → 0.01 → 0.01

Numbers say: light vs heavy: width 22.0 → 43.2 px, dark 0.22 → 0.28; the long stroke does not run out of paint.

## Oil · Henry Ward · HW #09 white arches over wet blue-grey
Oil 1.00 · 46 px · 19.0 s

![Oil · Henry Ward · HW #09 white arches over wet blue-grey](Oil-Henry-Ward-HW-09-white-arches-over-wet-blue-grey.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 8 % → 8 % | 22.0 px | 0.33 | 1.00 | 122 |
| heavy line | 15 % → 15 % | 43.2 px | 0.37 | 1.00 | 153 |
| pressure swell | 11 % → 11 % | 40.8 px | 0.38 | 1.00 | 132 |
| fast wave | 32 % → 32 % | 36.7 px | 0.35 | 1.00 | 391 |
| slow wave | 26 % → 26 % | 30.4 px | 0.35 | 1.00 | 708 |
| spiral | 50 % → 50 % | 32.9 px | 0.32 | 1.00 | 736 |
| loop | 27 % → 27 % | 35.3 px | 0.36 | 1.00 | 429 |
| tilted | 13 % → 13 % | 35.9 px | 0.36 | 1.00 | 258 |
| over the wet one | 26 % → 26 % | 36.5 px | 0.36 | 1.00 | 245 |
| long, no reload | 47 % → 47 % | 21.2 px | 0.33 | 1.00 | 1040 | quarters: 0.26 → 0.17 → 0.14 → 0.10

Numbers say: light vs heavy: width 22.0 → 43.2 px, dark 0.33 → 0.37.

## Oil · Henry Ward · HW #03 navy contours over wet band
Oil 1.00 · 46 px · 18.9 s

![Oil · Henry Ward · HW #03 navy contours over wet band](Oil-Henry-Ward-HW-03-navy-contours-over-wet-band.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 8 % → 8 % | 22.0 px | 0.35 | 1.00 | 149 |
| heavy line | 15 % → 15 % | 43.2 px | 0.39 | 1.00 | 166 |
| pressure swell | 11 % → 11 % | 40.8 px | 0.41 | 1.00 | 137 |
| fast wave | 32 % → 32 % | 36.7 px | 0.37 | 1.00 | 517 |
| slow wave | 26 % → 26 % | 30.4 px | 0.37 | 1.00 | 829 |
| spiral | 50 % → 50 % | 32.9 px | 0.34 | 1.00 | 865 |
| loop | 27 % → 27 % | 35.3 px | 0.38 | 1.00 | 421 |
| tilted | 13 % → 13 % | 35.9 px | 0.38 | 1.00 | 192 |
| over the wet one | 26 % → 26 % | 36.5 px | 0.38 | 1.00 | 185 |
| long, no reload | 47 % → 47 % | 21.2 px | 0.35 | 1.00 | 1070 | quarters: 0.28 → 0.18 → 0.15 → 0.11

Numbers say: light vs heavy: width 22.0 → 43.2 px, dark 0.35 → 0.39.

## Oil · Henry Ward · Ground #2b2f1c
Gouache 1.00 · 160 px · 65.4 s

![Oil · Henry Ward · Ground #2b2f1c](Oil-Henry-Ward-Ground-2b2f1c.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 51 % → 45 % | 147.8 px | 0.52 | 0.89 | 732 |
| heavy line | 52 % → 47 % | 150.7 px | 0.52 | 0.91 | 840 |
| pressure swell | 41 % → 45 % | 153.1 px | 0.52 | 1.09 | 694 |
| fast wave | 83 % → 83 % | 95.7 px | 0.52 | 1.00 | 1996 |
| slow wave | 85 % → 70 % | 98.0 px | 0.52 | 0.82 | 3446 |
| spiral | 88 % → 75 % | 58.1 px | 0.52 | 0.85 | 3557 |
| loop | 74 % → 67 % | 96.4 px | 0.52 | 0.90 | 1791 |
| tilted | 38 % → 38 % | 107.0 px | 0.52 | 1.00 | 901 |
| over the wet one | 76 % → 70 % | 104.5 px | 0.52 | 0.92 | 777 |
| long, no reload | 96 % → 81 % | 43.1 px | 0.52 | 0.84 | 4943 | quarters: 0.52 → 0.52 → 0.51 → 0.46

Numbers say: light vs heavy: width 147.8 → 150.7 px, dark 0.52 → 0.52; pressure barely changes the width; the long stroke does not run out of paint.

## Oil · Henry Ward · Thin veil #2b3a44
Oil 0.81 · Ink 0.19 · 56 px · 32.0 s

![Oil · Henry Ward · Thin veil #2b3a44](Oil-Henry-Ward-Thin-veil-2b3a44.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 6 % → 4 % | 18.6 px | 0.62 | 0.67 | 157 |
| heavy line | 13 % → 12 % | 37.3 px | 0.67 | 0.92 | 207 |
| pressure swell | 10 % → 8 % | 37.0 px | 0.64 | 0.81 | 192 |
| fast wave | 38 % → 31 % | 43.4 px | 0.65 | 0.81 | 663 |
| slow wave | 36 % → 33 % | 42.0 px | 0.66 | 0.91 | 891 |
| spiral | 61 % → 49 % | 40.0 px | 0.64 | 0.80 | 893 |
| loop | 28 % → 24 % | 36.2 px | 0.65 | 0.85 | 447 |
| tilted | 14 % → 15 % | 40.4 px | 0.64 | 1.02 | 234 |
| over the wet one | 24 % → 21 % | 26.4 px | 0.64 | 0.86 | 186 |
| long, no reload | 55 % → 44 % | 24.7 px | 0.64 | 0.79 | 1319 | quarters: 0.45 → 0.29 → 0.25 → 0.28

Numbers say: light vs heavy: width 18.6 → 37.3 px, dark 0.62 → 0.67.

## Oil · Henry Ward · Loaded flat #ece6c0
Oil 1.00 · 46 px · 19.1 s

![Oil · Henry Ward · Loaded flat #ece6c0](Oil-Henry-Ward-Loaded-flat-ece6c0.png)

A light paint: laid on a grey sheet (on white it cannot be seen); **dark** = how far it is from the grey either way.

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 8 % → 8 % | 22.0 px | 0.32 | 1.00 | 177 |
| heavy line | 15 % → 15 % | 43.2 px | 0.39 | 1.00 | 230 |
| pressure swell | 11 % → 11 % | 40.8 px | 0.36 | 1.00 | 136 |
| fast wave | 32 % → 32 % | 36.7 px | 0.34 | 1.00 | 512 |
| slow wave | 26 % → 26 % | 30.4 px | 0.35 | 1.00 | 738 |
| spiral | 50 % → 50 % | 32.9 px | 0.32 | 1.00 | 816 |
| loop | 27 % → 27 % | 35.3 px | 0.36 | 1.00 | 377 |
| tilted | 13 % → 13 % | 35.9 px | 0.36 | 1.00 | 225 |
| over the wet one | 26 % → 26 % | 36.5 px | 0.36 | 1.00 | 183 |
| long, no reload | 47 % → 47 % | 21.2 px | 0.32 | 1.00 | 1002 | quarters: 0.00 → 0.00 → 0.00 → 0.00

Numbers say: light vs heavy: width 22.0 → 43.2 px, dark 0.32 → 0.39; the long stroke does not run out of paint.

## Oil · Henry Ward · Dry scrub #ece6c0
Oil 1.00 · 50 px · 15.1 s

![Oil · Henry Ward · Dry scrub #ece6c0](Oil-Henry-Ward-Dry-scrub-ece6c0.png)

A light paint: laid on a grey sheet (on white it cannot be seen); **dark** = how far it is from the grey either way.

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 5 % → 5 % | 15.2 px | 0.19 | 1.00 | 264 |
| heavy line | 9 % → 9 % | 25.5 px | 0.26 | 1.00 | 183 |
| pressure swell | 7 % → 7 % | 27.9 px | 0.27 | 1.00 | 132 |
| fast wave | 26 % → 26 % | 29.8 px | 0.27 | 1.01 | 485 |
| slow wave | 27 % → 27 % | 30.9 px | 0.26 | 1.00 | 776 |
| spiral | 43 % → 43 % | 28.6 px | 0.22 | 1.00 | 765 |
| loop | 21 % → 21 % | 26.9 px | 0.26 | 1.00 | 385 |
| tilted | 12 % → 12 % | 33.3 px | 0.25 | 1.00 | 210 |
| over the wet one | 17 % → 17 % | 15.0 px | 0.25 | 1.00 | 157 |
| long, no reload | 33 % → 33 % | 14.8 px | 0.23 | 1.00 | 995 | quarters: 0.00 → 0.00 → 0.00 → 0.00

Numbers say: light vs heavy: width 15.2 → 25.5 px, dark 0.19 → 0.26; the long stroke does not run out of paint.

## Oil · Henry Ward · Ground #8a6a20
Gouache 1.00 · 160 px · 69.1 s

![Oil · Henry Ward · Ground #8a6a20](Oil-Henry-Ward-Ground-8a6a20.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 51 % → 45 % | 147.8 px | 0.32 | 0.89 | 854 |
| heavy line | 52 % → 47 % | 150.7 px | 0.32 | 0.91 | 913 |
| pressure swell | 41 % → 45 % | 153.1 px | 0.32 | 1.09 | 519 |
| fast wave | 83 % → 83 % | 95.7 px | 0.32 | 1.00 | 1878 |
| slow wave | 85 % → 70 % | 98.0 px | 0.32 | 0.82 | 3480 |
| spiral | 88 % → 75 % | 58.1 px | 0.32 | 0.85 | 3664 |
| loop | 74 % → 67 % | 96.4 px | 0.32 | 0.90 | 1750 |
| tilted | 38 % → 38 % | 107.0 px | 0.32 | 1.00 | 864 |
| over the wet one | 76 % → 70 % | 104.5 px | 0.32 | 0.92 | 763 |
| long, no reload | 96 % → 81 % | 43.1 px | 0.32 | 0.84 | 4845 | quarters: 0.32 → 0.32 → 0.31 → 0.27

Numbers say: light vs heavy: width 147.8 → 150.7 px, dark 0.32 → 0.32; pressure barely changes the width.

## Oil · Henry Ward · Loaded flat #b8bcc0
Oil 1.00 · 46 px · 17.7 s

![Oil · Henry Ward · Loaded flat #b8bcc0](Oil-Henry-Ward-Loaded-flat-b8bcc0.png)

A light paint: laid on a grey sheet (on white it cannot be seen); **dark** = how far it is from the grey either way.

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 8 % → 8 % | 22.0 px | 0.22 | 1.00 | 132 |
| heavy line | 15 % → 15 % | 43.2 px | 0.28 | 1.00 | 155 |
| pressure swell | 11 % → 11 % | 40.8 px | 0.25 | 1.00 | 112 |
| fast wave | 32 % → 32 % | 36.7 px | 0.23 | 1.00 | 391 |
| slow wave | 26 % → 26 % | 30.4 px | 0.25 | 1.00 | 623 |
| spiral | 50 % → 50 % | 32.9 px | 0.22 | 1.00 | 669 |
| loop | 27 % → 27 % | 35.3 px | 0.25 | 1.00 | 378 |
| tilted | 13 % → 13 % | 35.9 px | 0.25 | 1.00 | 221 |
| over the wet one | 26 % → 26 % | 36.5 px | 0.25 | 1.00 | 170 |
| long, no reload | 47 % → 47 % | 21.2 px | 0.22 | 1.00 | 1079 | quarters: 0.00 → 0.01 → 0.01 → 0.01

Numbers say: light vs heavy: width 22.0 → 43.2 px, dark 0.22 → 0.28; the long stroke does not run out of paint.

## Oil · Henry Ward · Dry scrub #c8ccd0
Oil 1.00 · 50 px · 14.1 s

![Oil · Henry Ward · Dry scrub #c8ccd0](Oil-Henry-Ward-Dry-scrub-c8ccd0.png)

A light paint: laid on a grey sheet (on white it cannot be seen); **dark** = how far it is from the grey either way.

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 5 % → 5 % | 15.2 px | 0.15 | 1.00 | 155 |
| heavy line | 9 % → 9 % | 25.5 px | 0.21 | 1.00 | 158 |
| pressure swell | 7 % → 7 % | 27.9 px | 0.22 | 1.00 | 112 |
| fast wave | 26 % → 26 % | 29.8 px | 0.22 | 1.01 | 426 |
| slow wave | 27 % → 27 % | 30.9 px | 0.21 | 1.00 | 708 |
| spiral | 43 % → 43 % | 28.6 px | 0.17 | 1.00 | 737 |
| loop | 21 % → 21 % | 26.9 px | 0.21 | 1.00 | 357 |
| tilted | 12 % → 12 % | 33.3 px | 0.20 | 1.00 | 213 |
| over the wet one | 17 % → 17 % | 15.0 px | 0.20 | 1.00 | 146 |
| long, no reload | 33 % → 33 % | 14.8 px | 0.18 | 1.00 | 998 | quarters: 0.00 → 0.00 → 0.00 → 0.00

Numbers say: light vs heavy: width 15.2 → 25.5 px, dark 0.15 → 0.21; the long stroke does not run out of paint.

## Oil · Henry Ward · Wet drag #9ea4aa
Oil 1.00 · 44 px · 14.7 s

![Oil · Henry Ward · Wet drag #9ea4aa](Oil-Henry-Ward-Wet-drag-9ea4aa.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 8 % → 8 % | 24.2 px | 0.15 | 1.00 | 138 |
| heavy line | 10 % → 10 % | 29.1 px | 0.22 | 1.00 | 143 |
| pressure swell | 10 % → 10 % | 35.9 px | 0.20 | 1.00 | 100 |
| fast wave | 29 % → 29 % | 33.7 px | 0.19 | 1.00 | 412 |
| slow wave | 31 % → 31 % | 35.8 px | 0.18 | 1.00 | 672 |
| spiral | 50 % → 50 % | 33.1 px | 0.18 | 1.00 | 680 |
| loop | 23 % → 23 % | 29.5 px | 0.22 | 1.00 | 332 |
| tilted | 12 % → 12 % | 33.1 px | 0.20 | 1.00 | 196 |
| over the wet one | 24 % → 24 % | 33.3 px | 0.20 | 1.00 | 171 |
| long, no reload | 54 % → 54 % | 24.0 px | 0.19 | 1.00 | 1048 | quarters: 0.17 → 0.12 → 0.09 → 0.06

Numbers say: light vs heavy: width 24.2 → 29.1 px, dark 0.15 → 0.22.

## Oil · Henry Ward · Ground #e8b4a8
Gouache 1.00 · 160 px · 68.9 s

![Oil · Henry Ward · Ground #e8b4a8](Oil-Henry-Ward-Ground-e8b4a8.png)

A light paint: laid on a grey sheet (on white it cannot be seen); **dark** = how far it is from the grey either way.

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 51 % → 45 % | 147.8 px | 0.30 | 0.89 | 700 |
| heavy line | 52 % → 47 % | 150.7 px | 0.30 | 0.91 | 779 |
| pressure swell | 41 % → 45 % | 153.1 px | 0.30 | 1.09 | 598 |
| fast wave | 83 % → 83 % | 95.7 px | 0.30 | 1.00 | 1896 |
| slow wave | 85 % → 70 % | 98.0 px | 0.30 | 0.82 | 3574 |
| spiral | 88 % → 75 % | 58.1 px | 0.30 | 0.85 | 3285 |
| loop | 74 % → 67 % | 96.4 px | 0.30 | 0.90 | 1747 |
| tilted | 38 % → 38 % | 107.0 px | 0.30 | 1.00 | 930 |
| over the wet one | 76 % → 70 % | 104.5 px | 0.30 | 0.92 | 762 |
| long, no reload | 96 % → 81 % | 43.1 px | 0.30 | 0.84 | 4746 | quarters: 0.00 → 0.00 → 0.00 → 0.00

Numbers say: light vs heavy: width 147.8 → 150.7 px, dark 0.30 → 0.30; pressure barely changes the width.

## Oil · Henry Ward · Loaded flat #6e7f90
Oil 1.00 · 46 px · 17.6 s

![Oil · Henry Ward · Loaded flat #6e7f90](Oil-Henry-Ward-Loaded-flat-6e7f90.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 8 % → 8 % | 22.0 px | 0.33 | 1.00 | 140 |
| heavy line | 15 % → 15 % | 43.2 px | 0.37 | 1.00 | 172 |
| pressure swell | 11 % → 11 % | 40.8 px | 0.38 | 1.00 | 114 |
| fast wave | 32 % → 32 % | 36.7 px | 0.35 | 1.00 | 421 |
| slow wave | 26 % → 26 % | 30.4 px | 0.35 | 1.00 | 568 |
| spiral | 50 % → 50 % | 32.9 px | 0.32 | 1.00 | 661 |
| loop | 27 % → 27 % | 35.3 px | 0.36 | 1.00 | 310 |
| tilted | 13 % → 13 % | 35.9 px | 0.36 | 1.00 | 228 |
| over the wet one | 26 % → 26 % | 36.5 px | 0.36 | 1.00 | 153 |
| long, no reload | 47 % → 47 % | 21.2 px | 0.33 | 1.00 | 1117 | quarters: 0.26 → 0.17 → 0.14 → 0.10

Numbers say: light vs heavy: width 22.0 → 43.2 px, dark 0.33 → 0.37.

## Oil · Henry Ward · Loaded flat #f6f6f2
Oil 1.00 · 46 px · 18.1 s

![Oil · Henry Ward · Loaded flat #f6f6f2](Oil-Henry-Ward-Loaded-flat-f6f6f2.png)

A light paint: laid on a grey sheet (on white it cannot be seen); **dark** = how far it is from the grey either way.

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 8 % → 8 % | 22.0 px | 0.36 | 1.00 | 135 |
| heavy line | 15 % → 15 % | 43.2 px | 0.42 | 1.00 | 185 |
| pressure swell | 11 % → 11 % | 40.8 px | 0.40 | 1.00 | 114 |
| fast wave | 32 % → 32 % | 36.7 px | 0.37 | 1.00 | 428 |
| slow wave | 26 % → 26 % | 30.4 px | 0.39 | 1.00 | 804 |
| spiral | 50 % → 50 % | 32.9 px | 0.35 | 1.00 | 760 |
| loop | 27 % → 27 % | 35.3 px | 0.39 | 1.00 | 413 |
| tilted | 13 % → 13 % | 35.9 px | 0.40 | 1.00 | 207 |
| over the wet one | 26 % → 26 % | 36.5 px | 0.40 | 1.00 | 172 |
| long, no reload | 47 % → 47 % | 21.2 px | 0.35 | 1.00 | 1035 | quarters: 0.00 → 0.00 → 0.00 → 0.00

Numbers say: light vs heavy: width 22.0 → 43.2 px, dark 0.36 → 0.42; the long stroke does not run out of paint.

## Oil · Henry Ward · Dry scrub #f6f6f2
Oil 1.00 · 50 px · 14.6 s

![Oil · Henry Ward · Dry scrub #f6f6f2](Oil-Henry-Ward-Dry-scrub-f6f6f2.png)

A light paint: laid on a grey sheet (on white it cannot be seen); **dark** = how far it is from the grey either way.

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 5 % → 5 % | 15.2 px | 0.22 | 1.00 | 143 |
| heavy line | 9 % → 9 % | 25.5 px | 0.29 | 1.00 | 179 |
| pressure swell | 7 % → 7 % | 27.9 px | 0.30 | 1.00 | 134 |
| fast wave | 26 % → 26 % | 29.8 px | 0.30 | 1.01 | 426 |
| slow wave | 27 % → 27 % | 30.9 px | 0.29 | 1.00 | 684 |
| spiral | 43 % → 43 % | 28.6 px | 0.25 | 1.00 | 728 |
| loop | 21 % → 21 % | 26.9 px | 0.29 | 1.00 | 358 |
| tilted | 12 % → 12 % | 33.3 px | 0.28 | 1.00 | 195 |
| over the wet one | 17 % → 17 % | 15.0 px | 0.28 | 1.00 | 148 |
| long, no reload | 33 % → 33 % | 14.8 px | 0.26 | 1.00 | 929 | quarters: 0.00 → 0.00 → 0.00 → 0.00

Numbers say: light vs heavy: width 15.2 → 25.5 px, dark 0.22 → 0.29; the long stroke does not run out of paint.

## Oil · Henry Ward · Ground #e8e2da
Gouache 1.00 · 160 px · 71.1 s

![Oil · Henry Ward · Ground #e8e2da](Oil-Henry-Ward-Ground-e8e2da.png)

A light paint: laid on a grey sheet (on white it cannot be seen); **dark** = how far it is from the grey either way.

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 51 % → 45 % | 147.8 px | 0.38 | 0.89 | 748 |
| heavy line | 52 % → 47 % | 150.7 px | 0.38 | 0.91 | 802 |
| pressure swell | 41 % → 45 % | 153.1 px | 0.38 | 1.09 | 538 |
| fast wave | 83 % → 83 % | 95.7 px | 0.38 | 1.00 | 1863 |
| slow wave | 85 % → 70 % | 98.0 px | 0.38 | 0.82 | 3393 |
| spiral | 88 % → 75 % | 58.1 px | 0.38 | 0.85 | 3599 |
| loop | 74 % → 67 % | 96.4 px | 0.38 | 0.90 | 1819 |
| tilted | 38 % → 38 % | 107.0 px | 0.38 | 1.00 | 901 |
| over the wet one | 76 % → 70 % | 104.5 px | 0.38 | 0.92 | 780 |
| long, no reload | 96 % → 81 % | 43.1 px | 0.37 | 0.84 | 4776 | quarters: 0.00 → 0.00 → 0.00 → 0.01

Numbers say: light vs heavy: width 147.8 → 150.7 px, dark 0.38 → 0.38; pressure barely changes the width.

## Oil · Henry Ward · Loaded flat #6a7a80
Oil 1.00 · 46 px · 18.2 s

![Oil · Henry Ward · Loaded flat #6a7a80](Oil-Henry-Ward-Loaded-flat-6a7a80.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 8 % → 8 % | 22.0 px | 0.35 | 1.00 | 143 |
| heavy line | 15 % → 15 % | 43.2 px | 0.39 | 1.00 | 169 |
| pressure swell | 11 % → 11 % | 40.8 px | 0.41 | 1.00 | 113 |
| fast wave | 32 % → 32 % | 36.7 px | 0.37 | 1.00 | 402 |
| slow wave | 26 % → 26 % | 30.4 px | 0.37 | 1.00 | 682 |
| spiral | 50 % → 50 % | 32.9 px | 0.34 | 1.00 | 694 |
| loop | 27 % → 27 % | 35.3 px | 0.38 | 1.00 | 326 |
| tilted | 13 % → 13 % | 35.9 px | 0.38 | 1.00 | 194 |
| over the wet one | 26 % → 26 % | 36.5 px | 0.38 | 1.00 | 219 |
| long, no reload | 47 % → 47 % | 21.2 px | 0.35 | 1.00 | 983 | quarters: 0.28 → 0.18 → 0.15 → 0.11

Numbers say: light vs heavy: width 22.0 → 43.2 px, dark 0.35 → 0.39.

## Oil · Henry Ward · Loaded flat #5a1810
Oil 1.00 · 46 px · 17.9 s

![Oil · Henry Ward · Loaded flat #5a1810](Oil-Henry-Ward-Loaded-flat-5a1810.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 8 % → 8 % | 22.0 px | 0.74 | 1.00 | 159 |
| heavy line | 15 % → 15 % | 43.2 px | 0.73 | 1.00 | 177 |
| pressure swell | 11 % → 11 % | 40.8 px | 0.77 | 1.00 | 115 |
| fast wave | 32 % → 32 % | 36.7 px | 0.75 | 1.00 | 402 |
| slow wave | 26 % → 26 % | 30.4 px | 0.75 | 1.00 | 613 |
| spiral | 50 % → 50 % | 32.9 px | 0.74 | 1.00 | 690 |
| loop | 27 % → 27 % | 35.3 px | 0.75 | 1.00 | 379 |
| tilted | 13 % → 13 % | 35.9 px | 0.75 | 1.00 | 205 |
| over the wet one | 26 % → 26 % | 36.5 px | 0.75 | 1.00 | 157 |
| long, no reload | 47 % → 47 % | 21.2 px | 0.74 | 1.00 | 939 | quarters: 0.53 → 0.40 → 0.35 → 0.26

Numbers say: light vs heavy: width 22.0 → 43.2 px, dark 0.74 → 0.73.

## Oil · Henry Ward · Dirty contour #1c2240
Oil 1.00 · 24 px · 12.8 s

![Oil · Henry Ward · Dirty contour #1c2240](Oil-Henry-Ward-Dirty-contour-1c2240.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 8 % → 8 % | 21.8 px | 0.75 | 1.00 | 81 |
| heavy line | 8 % → 8 % | 24.4 px | 0.74 | 1.00 | 91 |
| pressure swell | 7 % → 7 % | 26.8 px | 0.76 | 1.00 | 94 |
| fast wave | 18 % → 18 % | 21.2 px | 0.74 | 1.00 | 256 |
| slow wave | 21 % → 21 % | 24.0 px | 0.76 | 1.00 | 425 |
| spiral | 30 % → 30 % | 20.0 px | 0.74 | 1.00 | 404 |
| loop | 16 % → 16 % | 21.3 px | 0.76 | 1.00 | 228 |
| tilted | 9 % → 9 % | 25.4 px | 0.75 | 1.00 | 109 |
| over the wet one | 17 % → 17 % | 22.7 px | 0.75 | 1.00 | 97 |
| long, no reload | 39 % → 39 % | 17.7 px | 0.73 | 1.00 | 690 | quarters: 0.43 → 0.35 → 0.28 → 0.23

Numbers say: light vs heavy: width 21.8 → 24.4 px, dark 0.75 → 0.74.

## v3 · Any shape · K stamp
Gouache 1.00 · 48 px · 44.0 s

![v3 · Any shape · K stamp](v3-Any-shape-K-stamp.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 20 % → 19 % | 59.0 px | 0.40 | 0.93 | 210 |
| heavy line | 20 % → 19 % | 59.1 px | 0.40 | 0.94 | 223 |
| pressure swell | 12 % → 11 % | 43.7 px | 0.40 | 0.98 | 152 |
| fast wave | 42 % → 34 % | 48.2 px | 0.40 | 0.83 | 537 |
| slow wave | 42 % → 34 % | 48.3 px | 0.40 | 0.82 | 869 |
| spiral | 66 % → 44 % | 43.5 px | 0.40 | 0.67 | 916 |
| loop | 37 % → 34 % | 48.2 px | 0.40 | 0.91 | 470 |
| tilted | 15 % → 15 % | 42.0 px | 0.40 | 1.01 | 253 |
| over the wet one | 33 % → 32 % | 51.3 px | 0.40 | 0.95 | 203 |
| long, no reload | 81 % → 47 % | 36.3 px | 0.40 | 0.58 | 1354 | quarters: 0.35 → 0.34 → 0.32 → 0.28

Numbers say: light vs heavy: width 59.0 → 59.1 px, dark 0.40 → 0.40; pressure barely changes the width.

## v3 · Any shape · K of hairs
Oil 1.00 · 48 px · 15.3 s

![v3 · Any shape · K of hairs](v3-Any-shape-K-of-hairs.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 18 % → 18 % | 51.8 px | 0.40 | 1.00 | 127 |
| heavy line | 27 % → 27 % | 78.4 px | 0.46 | 1.00 | 177 |
| pressure swell | 16 % → 16 % | 58.4 px | 0.47 | 1.01 | 128 |
| fast wave | 49 % → 51 % | 56.8 px | 0.44 | 1.04 | 379 |
| slow wave | 50 % → 50 % | 57.8 px | 0.48 | 1.00 | 662 |
| spiral | 67 % → 67 % | 44.1 px | 0.45 | 1.00 | 683 |
| loop | 45 % → 45 % | 58.8 px | 0.48 | 1.00 | 339 |
| tilted | 16 % → 16 % | 45.8 px | 0.46 | 1.00 | 186 |
| over the wet one | 39 % → 39 % | 62.3 px | 0.46 | 1.01 | 152 |
| long, no reload | 84 % → 84 % | 37.8 px | 0.43 | 1.00 | 954 | quarters: 0.48 → 0.46 → 0.33 → 0.26

Numbers say: light vs heavy: width 51.8 → 78.4 px, dark 0.40 → 0.46.

## v3 · Any shape · Star stamp
Gouache 1.00 · 44 px · 38.2 s

![v3 · Any shape · Star stamp](v3-Any-shape-Star-stamp.png)

A light paint: laid on a grey sheet (on white it cannot be seen); **dark** = how far it is from the grey either way.

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 13 % → 11 % | 37.9 px | 0.36 | 0.84 | 121 |
| heavy line | 13 % → 12 % | 38.4 px | 0.36 | 0.87 | 98 |
| pressure swell | 10 % → 10 % | 39.2 px | 0.36 | 0.93 | 71 |
| fast wave | 33 % → 28 % | 38.0 px | 0.36 | 0.84 | 290 |
| slow wave | 33 % → 27 % | 38.4 px | 0.35 | 0.80 | 457 |
| spiral | 56 % → 41 % | 37.2 px | 0.35 | 0.73 | 441 |
| loop | 28 % → 25 % | 36.0 px | 0.36 | 0.88 | 212 |
| tilted | 13 % → 13 % | 37.0 px | 0.36 | 1.01 | 133 |
| over the wet one | 26 % → 24 % | 36.5 px | 0.36 | 0.91 | 115 |
| long, no reload | 68 % → 45 % | 30.4 px | 0.35 | 0.67 | 678 | quarters: 0.01 → 0.01 → 0.01 → 0.01

Numbers say: light vs heavy: width 37.9 → 38.4 px, dark 0.36 → 0.36; pressure barely changes the width; the long stroke does not run out of paint.

## v3 · Any shape · Star of hairs
Oil 1.00 · 44 px · 14.7 s

![v3 · Any shape · Star of hairs](v3-Any-shape-Star-of-hairs.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 15 % → 15 % | 43.7 px | 0.34 | 1.00 | 125 |
| heavy line | 23 % → 23 % | 67.9 px | 0.33 | 1.00 | 148 |
| pressure swell | 14 % → 14 % | 53.1 px | 0.35 | 1.00 | 100 |
| fast wave | 45 % → 46 % | 52.0 px | 0.32 | 1.01 | 394 |
| slow wave | 44 % → 44 % | 50.7 px | 0.33 | 1.00 | 579 |
| spiral | 63 % → 63 % | 41.7 px | 0.32 | 1.00 | 536 |
| loop | 39 % → 39 % | 50.4 px | 0.33 | 1.00 | 308 |
| tilted | 14 % → 14 % | 39.1 px | 0.34 | 1.00 | 165 |
| over the wet one | 34 % → 34 % | 55.5 px | 0.34 | 1.00 | 148 |
| long, no reload | 78 % → 78 % | 35.1 px | 0.30 | 1.00 | 807 | quarters: 0.32 → 0.28 → 0.23 → 0.17

Numbers say: light vs heavy: width 43.7 → 67.9 px, dark 0.34 → 0.33.

## v3 · Any shape · Rag
Oil 1.00 · 60 px · 20.7 s

![v3 · Any shape · Rag](v3-Any-shape-Rag.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 22 % → 25 % | 64.2 px | 0.16 | 1.12 | 206 |
| heavy line | 38 % → 38 % | 111.5 px | 0.29 | 1.00 | 296 |
| pressure swell | 25 % → 26 % | 94.4 px | 0.24 | 1.02 | 166 |
| fast wave | 68 % → 73 % | 78.9 px | 0.26 | 1.07 | 605 |
| slow wave | 71 % → 71 % | 82.3 px | 0.27 | 1.00 | 1059 |
| spiral | 81 % → 81 % | 53.5 px | 0.28 | 1.00 | 1035 |
| loop | 61 % → 62 % | 79.6 px | 0.29 | 1.00 | 560 |
| tilted | 22 % → 22 % | 61.1 px | 0.26 | 1.00 | 269 |
| over the wet one | 51 % → 52 % | 80.5 px | 0.26 | 1.03 | 228 |
| long, no reload | 94 % → 94 % | 42.3 px | 0.29 | 1.00 | 1729 | quarters: 0.35 → 0.32 → 0.27 → 0.21

Numbers say: light vs heavy: width 64.2 → 111.5 px, dark 0.16 → 0.29.

## v3 · Any shape · Dry oil on canvas
Oil 1.00 · 40 px · 13.4 s

![v3 · Any shape · Dry oil on canvas](v3-Any-shape-Dry-oil-on-canvas.png)

A light paint: laid on a grey sheet (on white it cannot be seen); **dark** = how far it is from the grey either way.

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 5 % → 5 % | 13.3 px | 0.14 | 1.00 | 85 |
| heavy line | 8 % → 8 % | 23.7 px | 0.35 | 1.00 | 101 |
| pressure swell | 9 % → 9 % | 32.2 px | 0.27 | 1.00 | 71 |
| fast wave | 27 % → 27 % | 31.7 px | 0.25 | 1.00 | 232 |
| slow wave | 26 % → 26 % | 30.5 px | 0.24 | 1.00 | 401 |
| spiral | 45 % → 45 % | 29.7 px | 0.25 | 1.00 | 462 |
| loop | 21 % → 21 % | 27.3 px | 0.24 | 1.00 | 207 |
| tilted | 9 % → 9 % | 26.3 px | 0.24 | 1.00 | 109 |
| over the wet one | 18 % → 18 % | 23.1 px | 0.24 | 1.00 | 84 |
| long, no reload | 41 % → 41 % | 18.2 px | 0.21 | 1.00 | 751 | quarters: 0.00 → 0.00 → 0.00 → 0.00

Numbers say: light vs heavy: width 13.3 → 23.7 px, dark 0.14 → 0.35; the long stroke does not run out of paint.

## v3 · Any shape · Two colours streaks
Oil 1.00 · 44 px · 18.2 s

![v3 · Any shape · Two colours streaks](v3-Any-shape-Two-colours-streaks.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 14 % → 14 % | 39.6 px | 0.35 | 1.00 | 149 |
| heavy line | 16 % → 16 % | 46.1 px | 0.31 | 1.00 | 115 |
| pressure swell | 11 % → 11 % | 42.9 px | 0.39 | 1.00 | 99 |
| fast wave | 37 % → 37 % | 43.1 px | 0.34 | 1.00 | 344 |
| slow wave | 35 % → 35 % | 40.7 px | 0.31 | 1.00 | 579 |
| spiral | 61 % → 61 % | 40.4 px | 0.35 | 1.00 | 599 |
| loop | 32 % → 32 % | 41.1 px | 0.32 | 1.00 | 322 |
| tilted | 13 % → 13 % | 37.2 px | 0.36 | 1.00 | 178 |
| over the wet one | 27 % → 27 % | 39.3 px | 0.36 | 1.00 | 127 |
| long, no reload | 73 % → 73 % | 32.6 px | 0.31 | 1.00 | 911 | quarters: 0.29 → 0.28 → 0.24 → 0.18

Numbers say: light vs heavy: width 39.6 → 46.1 px, dark 0.35 → 0.31.

## Brush Artist · Refs · #01 Henry Ward peach cloud — own sheet
own sheet 600 × 600 · Gouache 1.00 · 44 px · 15.1 s

![Brush Artist · Refs · #01 Henry Ward peach cloud — own sheet](Brush-Artist-Refs-01-Henry-Ward-peach-cloud-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 7 % → 21 % | 18.9 px | 0.56 | 3.13 | 133 |
| stroke 2 | 13 % → 37 % | 41.5 px | 0.56 | 2.92 | 114 |
| stroke 3 | 19 % → 38 % | 54.7 px | 0.56 | 2.01 | 151 |
| stroke 4 | 23 % → 42 % | 73.9 px | 0.56 | 1.84 | 152 |
| stroke 5 | 22 % → 37 % | 64.8 px | 0.56 | 1.66 | 130 |
| stroke 6 | 21 % → 28 % | 65.0 px | 0.56 | 1.31 | 147 |
| stroke 7 | 10 % → 39 % | 25.5 px | 0.56 | 3.79 | 128 |
| stroke 8 | 14 % → 37 % | 35.0 px | 0.56 | 2.64 | 139 |
| stroke 9 | 14 % → 38 % | 36.8 px | 0.56 | 2.65 | 141 |
| stroke 10 | 15 % → 39 % | 40.1 px | 0.56 | 2.60 | 147 |
| stroke 11 | 17 % → 41 % | 48.5 px | 0.56 | 2.42 | 147 |
| stroke 12 | 17 % → 44 % | 52.1 px | 0.56 | 2.54 | 114 |
| stroke 13 | 24 % → 47 % | 70.2 px | 0.56 | 1.95 | 152 |
| stroke 14 | 31 % → 49 % | 87.4 px | 0.56 | 1.60 | 166 |
| stroke 15 | 36 % → 54 % | 107.7 px | 0.56 | 1.47 | 137 |
| stroke 16 | 40 % → 54 % | 122.3 px | 0.56 | 1.34 | 163 |
| stroke 17 | 41 % → 55 % | 114.5 px | 0.56 | 1.36 | 146 |
| stroke 18 | 45 % → 55 % | 131.7 px | 0.56 | 1.21 | 159 |
| stroke 19 | 46 % → 55 % | 129.7 px | 0.56 | 1.19 | 153 |
| stroke 20 | 47 % → 52 % | 135.9 px | 0.56 | 1.10 | 163 |
| stroke 21 | 48 % → 48 % | 138.5 px | 0.56 | 1.01 | 159 |
| stroke 22 | 49 % → 49 % | 144.0 px | 0.56 | 0.99 | 192 |
| stroke 23 | 52 % → 49 % | 147.8 px | 0.56 | 0.94 | 180 |
| stroke 24 | 55 % → 52 % | 165.9 px | 0.56 | 0.93 | 164 |

Numbers say: wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #02 Henry Ward cream strokes — own sheet
own sheet 600 × 600 · Gouache 1.00 · 46 px · 8.9 s

![Brush Artist · Refs · #02 Henry Ward cream strokes — own sheet](Brush-Artist-Refs-02-Henry-Ward-cream-strokes-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 11 % → 7 % | 23.2 px | 0.66 | 0.60 | 204 |
| stroke 2 | 17 % → 9 % | 44.6 px | 0.67 | 0.55 | 200 |
| stroke 3 | 18 % → 24 % | 45.7 px | 0.66 | 1.32 | 195 |
| stroke 4 | 21 % → 24 % | 52.8 px | 0.66 | 1.12 | 262 |
| stroke 5 | 25 % → 31 % | 62.0 px | 0.66 | 1.22 | 234 |
| stroke 6 | 22 % → 24 % | 52.7 px | 0.65 | 1.12 | 218 |
| stroke 7 | 24 % → 16 % | 60.7 px | 0.65 | 0.69 | 198 |

## Brush Artist · Refs · #03 Henry Ward navy contours — own sheet
own sheet 600 × 600 · Impasto 1.00 · 22 px · 3.4 s

![Brush Artist · Refs · #03 Henry Ward navy contours — own sheet](Brush-Artist-Refs-03-Henry-Ward-navy-contours-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 10 % → 15 % | 19.8 px | 0.69 | 1.51 | 108 |
| stroke 2 | 16 % → 19 % | 22.2 px | 0.69 | 1.18 | 144 |
| stroke 3 | 20 % → 20 % | 29.6 px | 0.69 | 0.99 | 168 |
| stroke 4 | 19 % → 17 % | 43.6 px | 0.69 | 0.89 | 197 |

Numbers say: wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #04 Henry Ward grey cloud — own sheet
own sheet 600 × 600 · Gouache 1.00 · 50 px · 14.8 s

![Brush Artist · Refs · #04 Henry Ward grey cloud — own sheet](Brush-Artist-Refs-04-Henry-Ward-grey-cloud-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 7 % → 28 % | 20.7 px | 0.33 | 4.01 | 243 |
| stroke 2 | 15 % → 29 % | 42.0 px | 0.33 | 2.00 | 244 |
| stroke 3 | 22 % → 31 % | 61.2 px | 0.33 | 1.41 | 289 |
| stroke 4 | 28 % → 33 % | 82.9 px | 0.33 | 1.16 | 278 |
| stroke 5 | 30 % → 37 % | 90.7 px | 0.33 | 1.23 | 263 |
| stroke 6 | 35 % → 41 % | 114.9 px | 0.33 | 1.17 | 263 |
| stroke 7 | 37 % → 49 % | 109.4 px | 0.33 | 1.32 | 211 |
| stroke 8 | 39 % → 50 % | 115.9 px | 0.33 | 1.29 | 240 |
| stroke 9 | 32 % → 50 % | 96.1 px | 0.33 | 1.55 | 266 |
| stroke 10 | 35 % → 50 % | 113.1 px | 0.33 | 1.42 | 382 |
| stroke 11 | 36 % → 47 % | 103.1 px | 0.33 | 1.29 | 564 |
| stroke 12 | 35 % → 45 % | 106.6 px | 0.33 | 1.28 | 423 |
| stroke 13 | 32 % → 48 % | 92.0 px | 0.33 | 1.50 | 215 |
| stroke 14 | 37 % → 48 % | 109.5 px | 0.33 | 1.31 | 287 |
| stroke 15 | 39 % → 47 % | 112.4 px | 0.33 | 1.20 | 270 |
| stroke 16 | 42 % → 45 % | 127.5 px | 0.33 | 1.07 | 288 |
| stroke 17 | 40 % → 38 % | 116.3 px | 0.33 | 0.95 | 234 |
| stroke 18 | 42 % → 35 % | 139.1 px | 0.33 | 0.84 | 232 |
| stroke 19 | 40 % → 28 % | 118.3 px | 0.33 | 0.71 | 253 |
| stroke 20 | 42 % → 28 % | 132.4 px | 0.33 | 0.66 | 213 |

Numbers say: wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #05 Henry Ward green in rust loops — own sheet
own sheet 600 × 600 · Impasto 1.00 · 20 px · 3.0 s

![Brush Artist · Refs · #05 Henry Ward green in rust loops — own sheet](Brush-Artist-Refs-05-Henry-Ward-green-in-rust-loops-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 11 % → 16 % | 18.9 px | 0.02 | 1.48 | 166 |
| stroke 2 | 12 % → 10 % | 23.8 px | 0.02 | 0.86 | 214 |
| stroke 3 | 20 % → 17 % | 35.5 px | 0.02 | 0.89 | 150 |

## Brush Artist · Refs · #06 Henry Ward scrubbed grey — own sheet
own sheet 600 × 600 · Gouache 1.00 · 50 px · 15.2 s

![Brush Artist · Refs · #06 Henry Ward scrubbed grey — own sheet](Brush-Artist-Refs-06-Henry-Ward-scrubbed-grey-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 9 % → 31 % | 20.9 px | 0.34 | 3.69 | 221 |
| stroke 2 | 17 % → 33 % | 45.7 px | 0.34 | 1.90 | 255 |
| stroke 3 | 22 % → 31 % | 68.2 px | 0.34 | 1.40 | 247 |
| stroke 4 | 27 % → 32 % | 83.8 px | 0.34 | 1.21 | 547 |
| stroke 5 | 34 % → 41 % | 101.4 px | 0.34 | 1.21 | 523 |
| stroke 6 | 40 % → 41 % | 121.4 px | 0.34 | 1.04 | 472 |
| stroke 7 | 39 % → 47 % | 110.9 px | 0.34 | 1.21 | 231 |
| stroke 8 | 41 % → 47 % | 129.4 px | 0.34 | 1.16 | 248 |
| stroke 9 | 35 % → 47 % | 107.5 px | 0.33 | 1.34 | 218 |
| stroke 10 | 35 % → 48 % | 113.7 px | 0.33 | 1.36 | 296 |
| stroke 11 | 36 % → 47 % | 104.8 px | 0.33 | 1.31 | 268 |
| stroke 12 | 35 % → 45 % | 106.0 px | 0.33 | 1.29 | 230 |
| stroke 13 | 29 % → 47 % | 81.3 px | 0.33 | 1.64 | 224 |
| stroke 14 | 33 % → 49 % | 95.8 px | 0.33 | 1.49 | 360 |
| stroke 15 | 38 % → 55 % | 107.6 px | 0.33 | 1.47 | 241 |
| stroke 16 | 39 % → 54 % | 125.5 px | 0.33 | 1.37 | 272 |
| stroke 17 | 39 % → 49 % | 115.6 px | 0.33 | 1.27 | 208 |
| stroke 18 | 43 % → 47 % | 130.2 px | 0.33 | 1.10 | 207 |
| stroke 19 | 40 % → 42 % | 119.9 px | 0.33 | 1.06 | 190 |
| stroke 20 | 41 % → 41 % | 126.3 px | 0.33 | 1.01 | 216 |
| stroke 21 | 41 % → 35 % | 118.1 px | 0.33 | 0.86 | 256 |
| stroke 22 | 39 % → 32 % | 129.1 px | 0.33 | 0.81 | 181 |

Numbers say: wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #07 Henry Ward blue L + black zigzag — own sheet
own sheet 600 × 600 · Impasto 1.00 · 34 px · 3.4 s

![Brush Artist · Refs · #07 Henry Ward blue L + black zigzag — own sheet](Brush-Artist-Refs-07-Henry-Ward-blue-L-black-zigzag-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 13 % → 15 % | 31.1 px | 0.58 | 1.11 | 165 |
| stroke 2 | 15 % → 14 % | 37.5 px | 0.58 | 0.90 | 151 |

## Brush Artist · Refs · #08 Henry Ward olive bands — own sheet
own sheet 600 × 600 · Gouache 1.00 · 34 px · 5.9 s

![Brush Artist · Refs · #08 Henry Ward olive bands — own sheet](Brush-Artist-Refs-08-Henry-Ward-olive-bands-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 7 % → 4 % | 13.6 px | 0.59 | 0.55 | 190 |
| stroke 2 | 11 % → 4 % | 24.7 px | 0.59 | 0.35 | 198 |
| stroke 3 | 12 % → 11 % | 24.3 px | 0.59 | 0.92 | 271 |
| stroke 4 | 15 % → 9 % | 33.0 px | 0.59 | 0.61 | 245 |
| stroke 5 | 20 % → 12 % | 41.1 px | 0.59 | 0.62 | 209 |
| stroke 6 | 14 % → 6 % | 27.3 px | 0.59 | 0.41 | 229 |

## Brush Artist · Refs · #09 Henry Ward white loops — own sheet
own sheet 600 × 600 · Gouache 1.00 · 46 px · 7.4 s

![Brush Artist · Refs · #09 Henry Ward white loops — own sheet](Brush-Artist-Refs-09-Henry-Ward-white-loops-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 23 % → 0 % | 12.5 px | 0.06 | 0.00 | 1279 |
| stroke 2 | 26 % → 0 % | 26.2 px | 0.05 | 0.00 | 1324 |
| stroke 3 | 33 % → 0 % | 30.6 px | 0.05 | 0.00 | 1041 |
| stroke 4 | 6 % → 0 % | 14.6 px | 0.00 | 0.00 | 177 |
| stroke 5 | 5 % → 0 % | 13.1 px | 0.06 | 0.00 | 166 |
| stroke 6 | 4 % → 0 % | 11.5 px | 0.05 | 0.00 | 145 |
| stroke 7 | 9 % → 0 % | 23.3 px | 0.05 | 0.00 | 156 |
| stroke 8 | 4 % → 0 % | 6.6 px | 0.00 | 0.00 | 198 |

## Brush Artist · Refs · #10 Henry Ward maroon loops — own sheet
own sheet 600 × 600 · Impasto 1.00 · 30 px · 3.7 s

![Brush Artist · Refs · #10 Henry Ward maroon loops — own sheet](Brush-Artist-Refs-10-Henry-Ward-maroon-loops-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 12 % → 26 % | 28.6 px | 0.71 | 2.26 | 305 |
| stroke 2 | 23 % → 39 % | 51.0 px | 0.71 | 1.74 | 167 |
| stroke 3 | 30 % → 35 % | 59.6 px | 0.71 | 1.20 | 196 |
| stroke 4 | 40 % → 38 % | 90.9 px | 0.71 | 0.95 | 116 |
| stroke 5 | 32 % → 29 % | 81.4 px | 0.71 | 0.89 | 156 |

Numbers say: wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #11 Henry Ward purple spun balls — own sheet
own sheet 600 × 600 · Impasto 1.00 · 36 px · 2.9 s

![Brush Artist · Refs · #11 Henry Ward purple spun balls — own sheet](Brush-Artist-Refs-11-Henry-Ward-purple-spun-balls-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 22 % → 31 % | 24.3 px | 0.68 | 1.42 | 254 |
| stroke 2 | 31 % → 43 % | 34.4 px | 0.68 | 1.39 | 245 |
| stroke 3 | 34 % → 33 % | 37.8 px | 0.68 | 0.96 | 229 |

## Brush Artist · Refs · #12 Henry Ward black-olive cage — own sheet
own sheet 600 × 600 · Gouache 1.00 · 28 px · 5.3 s

![Brush Artist · Refs · #12 Henry Ward black-olive cage — own sheet](Brush-Artist-Refs-12-Henry-Ward-black-olive-cage-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 8 % → 9 % | 15.8 px | 0.59 | 1.14 | 227 |
| stroke 2 | 6 % → 8 % | 14.2 px | 0.59 | 1.37 | 207 |
| stroke 3 | 16 % → 11 % | 25.2 px | 0.59 | 0.68 | 235 |
| stroke 4 | 18 % → 13 % | 35.6 px | 0.59 | 0.70 | 125 |
| stroke 5 | 17 % → 6 % | 30.8 px | 0.59 | 0.37 | 120 |
| stroke 6 | 26 % → 14 % | 50.4 px | 0.59 | 0.51 | 156 |

## Brush Artist · Refs · #13 Henry Ward blue streaky form — own sheet
own sheet 600 × 600 · Gouache 1.00 · 50 px · 10.4 s

![Brush Artist · Refs · #13 Henry Ward blue streaky form — own sheet](Brush-Artist-Refs-13-Henry-Ward-blue-streaky-form-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 7 % → 0 % | 20.8 px | 0.00 | 0.00 | 197 |
| stroke 2 | 15 % → 0 % | 44.9 px | 0.00 | 0.00 | 228 |
| stroke 3 | 23 % → 0 % | 65.8 px | 0.00 | 0.00 | 204 |
| stroke 4 | 26 % → 0 % | 84.2 px | 0.00 | 0.00 | 234 |
| stroke 5 | 34 % → 0 % | 98.8 px | 0.00 | 0.00 | 231 |
| stroke 6 | 39 % → 0 % | 111.0 px | 0.00 | 0.00 | 259 |
| stroke 7 | 38 % → 0 % | 112.7 px | 0.00 | 0.00 | 191 |
| stroke 8 | 40 % → 0 % | 121.7 px | 0.00 | 0.00 | 225 |
| stroke 9 | 34 % → 0 % | 104.5 px | 0.00 | 0.00 | 170 |
| stroke 10 | 34 % → 0 % | 110.5 px | 0.00 | 0.00 | 199 |
| stroke 11 | 32 % → 0 % | 98.3 px | 0.00 | 0.00 | 189 |
| stroke 12 | 30 % → 0 % | 90.4 px | 0.00 | 0.00 | 213 |
| stroke 13 | 28 % → 0 % | 87.4 px | 0.00 | 0.00 | 187 |
| stroke 14 | 32 % → 0 % | 94.1 px | 0.00 | 0.00 | 210 |
| stroke 15 | 35 % → 0 % | 100.4 px | 0.00 | 0.00 | 186 |
| stroke 16 | 39 % → 0 % | 116.9 px | 0.00 | 0.00 | 209 |
| stroke 17 | 44 % → 0 % | 108.9 px | 0.00 | 0.00 | 223 |
| stroke 18 | 51 % → 0 % | 124.8 px | 0.00 | 0.00 | 246 |
| stroke 19 | 53 % → 0 % | 108.6 px | 0.00 | 0.00 | 230 |
| stroke 20 | 63 % → 0 % | 119.6 px | 0.00 | 0.00 | 280 |
| stroke 21 | 6 % → 0 % | 11.8 px | 0.00 | 0.00 | 179 |
| stroke 22 | 6 % → 0 % | 18.0 px | 0.00 | 0.00 | 206 |
| stroke 23 | 11 % → 0 % | 33.4 px | 0.00 | 0.00 | 180 |
| stroke 24 | 4 % → 0 % | 11.1 px | 0.00 | 0.00 | 169 |
| stroke 25 | 3 % → 0 % | 8.4 px | 0.00 | 0.00 | 147 |

## Brush Artist · Refs · #14 Henry Ward olive totem — own sheet
own sheet 600 × 600 · Impasto 1.00 · 48 px · 7.6 s

![Brush Artist · Refs · #14 Henry Ward olive totem — own sheet](Brush-Artist-Refs-14-Henry-Ward-olive-totem-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 18 % → 46 % | 46.6 px | 0.39 | 2.57 | 160 |
| stroke 2 | 20 % → 50 % | 61.7 px | 0.39 | 2.53 | 127 |
| stroke 3 | 28 % → 52 % | 94.6 px | 0.39 | 1.88 | 151 |
| stroke 4 | 30 % → 54 % | 110.9 px | 0.39 | 1.83 | 131 |
| stroke 5 | 39 % → 63 % | 134.2 px | 0.39 | 1.64 | 143 |
| stroke 6 | 38 % → 64 % | 149.8 px | 0.39 | 1.68 | 218 |
| stroke 7 | 35 % → 60 % | 119.3 px | 0.39 | 1.70 | 122 |
| stroke 8 | 37 % → 62 % | 141.8 px | 0.39 | 1.67 | 153 |
| stroke 9 | 38 % → 62 % | 131.5 px | 0.39 | 1.64 | 137 |
| stroke 10 | 37 % → 61 % | 136.8 px | 0.39 | 1.65 | 162 |
| stroke 11 | 38 % → 64 % | 136.5 px | 0.39 | 1.66 | 159 |
| stroke 12 | 38 % → 64 % | 143.8 px | 0.39 | 1.68 | 147 |
| stroke 13 | 37 % → 66 % | 129.9 px | 0.39 | 1.78 | 156 |
| stroke 14 | 36 % → 61 % | 131.1 px | 0.39 | 1.70 | 182 |
| stroke 15 | 39 % → 65 % | 134.5 px | 0.39 | 1.66 | 142 |
| stroke 16 | 38 % → 63 % | 136.7 px | 0.39 | 1.67 | 136 |
| stroke 17 | 37 % → 61 % | 124.0 px | 0.39 | 1.64 | 184 |
| stroke 18 | 40 % → 65 % | 152.2 px | 0.39 | 1.63 | 126 |
| stroke 19 | 38 % → 58 % | 131.2 px | 0.39 | 1.55 | 156 |
| stroke 20 | 40 % → 53 % | 142.8 px | 0.39 | 1.31 | 186 |
| stroke 21 | 46 % → 53 % | 136.2 px | 0.39 | 1.15 | 163 |
| stroke 22 | 53 % → 51 % | 143.2 px | 0.38 | 0.97 | 159 |

Numbers say: wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #15 Ultramarine brush script — own sheet
own sheet 600 × 600 · Ink 1.00 · 4 px · 9.3 s

![Brush Artist · Refs · #15 Ultramarine brush script — own sheet](Brush-Artist-Refs-15-Ultramarine-brush-script-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 40 % → 42 % | 9.0 px | 0.65 | 1.05 | 58 |
| stroke 2 | 41 % → 43 % | 9.0 px | 0.67 | 1.07 | 54 |
| stroke 3 | 39 % → 42 % | 9.4 px | 0.72 | 1.08 | 28 |
| stroke 4 | 42 % → 46 % | 10.2 px | 0.74 | 1.10 | 21 |
| stroke 5 | 46 % → 49 % | 10.1 px | 0.72 | 1.06 | 29 |
| stroke 6 | 43 % → 45 % | 9.7 px | 0.65 | 1.05 | 122 |
| stroke 7 | 44 % → 47 % | 9.3 px | 0.72 | 1.08 | 27 |
| stroke 8 | 37 % → 39 % | 8.9 px | 0.65 | 1.06 | 70 |
| stroke 9 | 39 % → 42 % | 9.1 px | 0.70 | 1.07 | 47 |
| stroke 10 | 35 % → 37 % | 9.6 px | 0.66 | 1.05 | 60 |
| stroke 11 | 44 % → 47 % | 9.9 px | 0.69 | 1.06 | 68 |
| stroke 12 | 39 % → 41 % | 9.4 px | 0.65 | 1.06 | 81 |
| stroke 13 | 45 % → 46 % | 10.1 px | 0.69 | 1.04 | 39 |
| stroke 14 | 37 % → 40 % | 9.6 px | 0.71 | 1.07 | 34 |
| stroke 15 | 37 % → 38 % | 9.0 px | 0.67 | 1.05 | 59 |
| stroke 16 | 42 % → 45 % | 9.4 px | 0.70 | 1.06 | 17 |
| stroke 17 | 41 % → 45 % | 7.1 px | 0.71 | 1.09 | 68 |
| stroke 18 | 43 % → 45 % | 9.3 px | 0.73 | 1.05 | 32 |
| stroke 19 | 40 % → 42 % | 9.0 px | 0.65 | 1.06 | 74 |
| stroke 20 | 42 % → 44 % | 9.7 px | 0.69 | 1.06 | 62 |
| stroke 21 | 39 % → 42 % | 9.6 px | 0.69 | 1.07 | 36 |
| stroke 22 | 44 % → 46 % | 8.9 px | 0.65 | 1.06 | 79 |
| stroke 23 | 38 % → 42 % | 9.5 px | 0.72 | 1.10 | 33 |
| stroke 24 | 39 % → 42 % | 9.1 px | 0.73 | 1.06 | 44 |
| stroke 25 | 41 % → 44 % | 10.0 px | 0.71 | 1.06 | 36 |
| stroke 26 | 45 % → 47 % | 9.1 px | 0.66 | 1.04 | 63 |
| stroke 27 | 43 % → 45 % | 9.0 px | 0.62 | 1.05 | 74 |
| stroke 28 | 45 % → 47 % | 9.3 px | 0.70 | 1.06 | 53 |
| stroke 29 | 35 % → 38 % | 10.4 px | 0.69 | 1.08 | 26 |
| stroke 30 | 39 % → 40 % | 8.5 px | 0.70 | 1.04 | 66 |
| stroke 31 | 43 % → 46 % | 10.4 px | 0.74 | 1.07 | 15 |
| stroke 32 | 41 % → 45 % | 9.3 px | 0.70 | 1.09 | 26 |
| stroke 33 | 35 % → 40 % | 10.9 px | 0.73 | 1.13 | 41 |
| stroke 34 | 41 % → 45 % | 10.1 px | 0.74 | 1.09 | 23 |
| stroke 35 | 36 % → 38 % | 9.4 px | 0.67 | 1.06 | 89 |

## Brush Artist · Refs · #18 Blue oil-stick scribbles — own sheet
own sheet 600 × 600 · Pastel 1.00 · 10 px · 3.6 s

![Brush Artist · Refs · #18 Blue oil-stick scribbles — own sheet](Brush-Artist-Refs-18-Blue-oil-stick-scribbles-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 16 % → 32 % | 3.9 px | 0.49 | 2.03 | 150 |
| stroke 2 | 13 % → 37 % | 3.6 px | 0.49 | 2.75 | 201 |
| stroke 3 | 16 % → 26 % | 5.8 px | 0.49 | 1.64 | 275 |
| stroke 4 | 15 % → 29 % | 7.9 px | 0.49 | 1.91 | 245 |
| stroke 5 | 29 % → 34 % | 8.5 px | 0.49 | 1.18 | 206 |
| stroke 6 | 26 % → 26 % | 9.4 px | 0.49 | 1.02 | 209 |
| stroke 7 | 26 % → 32 % | 8.4 px | 0.49 | 1.24 | 238 |
| stroke 8 | 30 % → 30 % | 17.0 px | 0.49 | 1.00 | 226 |

Numbers say: wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #20 Orange-red crayon scribble — own sheet
own sheet 600 × 600 · Pastel 1.00 · 14 px · 3.4 s

![Brush Artist · Refs · #20 Orange-red crayon scribble — own sheet](Brush-Artist-Refs-20-Orange-red-crayon-scribble-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 8 % → 19 % | 5.5 px | 0.59 | 2.47 | 279 |
| stroke 2 | 9 % → 22 % | 6.6 px | 0.59 | 2.50 | 232 |
| stroke 3 | 13 % → 21 % | 8.3 px | 0.59 | 1.65 | 213 |
| stroke 4 | 24 % → 32 % | 8.8 px | 0.59 | 1.36 | 231 |
| stroke 5 | 28 % → 28 % | 7.9 px | 0.59 | 1.00 | 229 |
| stroke 6 | 22 % → 22 % | 16.4 px | 0.59 | 1.00 | 258 |

Numbers say: wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #21 Gritty black contours — own sheet
own sheet 600 × 600 · Gouache 1.00 · 12 px · 4.4 s

![Brush Artist · Refs · #21 Gritty black contours — own sheet](Brush-Artist-Refs-21-Gritty-black-contours-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 5 % → 4 % | 5.4 px | 0.37 | 0.78 | 211 |
| stroke 2 | 4 % → 2 % | 7.1 px | 0.37 | 0.49 | 197 |
| stroke 3 | 8 % → 2 % | 6.8 px | 0.37 | 0.21 | 135 |
| stroke 4 | 8 % → 3 % | 9.9 px | 0.37 | 0.39 | 141 |
| stroke 5 | 9 % → 3 % | 11.5 px | 0.37 | 0.34 | 110 |

## Brush Artist · Refs · #22 Bold black brush poster — own sheet
own sheet 600 × 600 · Ink 1.00 · 20 px · 5.5 s

![Brush Artist · Refs · #22 Bold black brush poster — own sheet](Brush-Artist-Refs-22-Bold-black-brush-poster-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 24 % → 28 % | 38.8 px | 0.95 | 1.18 | 96 |
| stroke 2 | 28 % → 39 % | 42.9 px | 0.94 | 1.38 | 29 |
| stroke 3 | 30 % → 30 % | 46.0 px | 0.94 | 1.00 | 52 |
| stroke 4 | 30 % → 41 % | 57.8 px | 0.94 | 1.41 | 48 |
| stroke 5 | 27 % → 27 % | 46.3 px | 0.93 | 1.00 | 94 |

## Brush Artist · Refs · #23 Dry white on orange + black line — own sheet
own sheet 600 × 600 · Gouache 1.00 · 50 px · 8.3 s

![Brush Artist · Refs · #23 Dry white on orange + black line — own sheet](Brush-Artist-Refs-23-Dry-white-on-orange-black-line-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 4 % → 10 % | 12.3 px | 0.39 | 2.80 | 120 |
| stroke 2 | 7 % → 9 % | 23.6 px | 0.39 | 1.34 | 173 |
| stroke 3 | 12 % → 9 % | 42.9 px | 0.39 | 0.81 | 145 |
| stroke 4 | 15 % → 10 % | 60.0 px | 0.39 | 0.68 | 211 |
| stroke 5 | 21 % → 11 % | 75.3 px | 0.39 | 0.55 | 177 |
| stroke 6 | 23 % → 12 % | 95.1 px | 0.39 | 0.52 | 203 |
| stroke 7 | 20 % → 11 % | 75.9 px | 0.39 | 0.56 | 131 |
| stroke 8 | 20 % → 10 % | 76.4 px | 0.39 | 0.53 | 196 |
| stroke 9 | 16 % → 10 % | 59.8 px | 0.39 | 0.61 | 167 |
| stroke 10 | 15 % → 10 % | 59.0 px | 0.39 | 0.64 | 163 |
| stroke 11 | 17 % → 10 % | 63.4 px | 0.39 | 0.57 | 177 |
| stroke 12 | 16 % → 11 % | 63.8 px | 0.39 | 0.65 | 193 |
| stroke 13 | 18 % → 12 % | 66.7 px | 0.39 | 0.69 | 162 |
| stroke 14 | 19 % → 12 % | 73.8 px | 0.39 | 0.63 | 182 |
| stroke 15 | 19 % → 11 % | 70.2 px | 0.39 | 0.61 | 128 |
| stroke 16 | 19 % → 10 % | 76.7 px | 0.39 | 0.51 | 191 |
| stroke 17 | 19 % → 8 % | 66.0 px | 0.38 | 0.40 | 148 |
| stroke 18 | 24 % → 8 % | 85.8 px | 0.38 | 0.34 | 152 |

Numbers say: wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #24 Picasso flat oil — own sheet
own sheet 600 × 600 · Oil 0.89 · Oil glaze 0.11 · 34 px · 5.6 s

![Brush Artist · Refs · #24 Picasso flat oil — own sheet](Brush-Artist-Refs-24-Picasso-flat-oil-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 14 % → 44 % | 30.0 px | 0.23 | 3.11 | 150 |
| stroke 2 | 19 % → 47 % | 44.5 px | 0.23 | 2.49 | 161 |
| stroke 3 | 27 % → 56 % | 59.7 px | 0.23 | 2.06 | 160 |
| stroke 4 | 37 % → 62 % | 82.9 px | 0.23 | 1.69 | 154 |
| stroke 5 | 41 % → 68 % | 91.2 px | 0.23 | 1.64 | 189 |
| stroke 6 | 42 % → 63 % | 96.4 px | 0.23 | 1.52 | 176 |
| stroke 7 | 42 % → 63 % | 87.5 px | 0.23 | 1.51 | 164 |
| stroke 8 | 42 % → 63 % | 101.5 px | 0.23 | 1.50 | 183 |
| stroke 9 | 34 % → 60 % | 74.4 px | 0.23 | 1.76 | 149 |
| stroke 10 | 38 % → 58 % | 89.8 px | 0.23 | 1.55 | 174 |
| stroke 11 | 35 % → 56 % | 74.6 px | 0.23 | 1.61 | 142 |
| stroke 12 | 37 % → 58 % | 88.3 px | 0.23 | 1.56 | 145 |
| stroke 13 | 35 % → 64 % | 77.9 px | 0.23 | 1.81 | 162 |
| stroke 14 | 36 % → 66 % | 81.9 px | 0.23 | 1.82 | 141 |
| stroke 15 | 36 % → 60 % | 75.9 px | 0.23 | 1.67 | 141 |
| stroke 16 | 36 % → 52 % | 83.2 px | 0.23 | 1.46 | 161 |
| stroke 17 | 41 % → 47 % | 86.1 px | 0.23 | 1.15 | 140 |
| stroke 18 | 42 % → 42 % | 101.0 px | 0.23 | 1.00 | 135 |

Numbers say: wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #25 Yellow heavy flat stroke — own sheet
own sheet 600 × 600 · Impasto 1.00 · 110 px · 3.2 s

![Brush Artist · Refs · #25 Yellow heavy flat stroke — own sheet](Brush-Artist-Refs-25-Yellow-heavy-flat-stroke-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 18 % → 18 % | 103.9 px | 0.17 | 0.98 | 846 |

## Brush Artist · Refs · #27 Orange impasto swatch — own sheet
own sheet 600 × 600 · Impasto 1.00 · 60 px · 3.3 s

![Brush Artist · Refs · #27 Orange impasto swatch — own sheet](Brush-Artist-Refs-27-Orange-impasto-swatch-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 8 % → 21 % | 59.0 px | 0.32 | 2.65 | 68 |
| stroke 2 | 7 % → 33 % | 62.1 px | 0.32 | 4.65 | 62 |
| stroke 3 | 25 % → 35 % | 239.2 px | 0.32 | 1.41 | 57 |
| stroke 4 | 10 % → 12 % | 69.8 px | 0.32 | 1.26 | 65 |
| stroke 5 | 17 % → 32 % | 61.8 px | 0.32 | 1.91 | 88 |
| stroke 6 | 17 % → 31 % | 144.0 px | 0.32 | 1.78 | 84 |
| stroke 7 | 8 % → 14 % | 69.2 px | 0.32 | 1.88 | 62 |
| stroke 8 | 32 % → 33 % | 330.4 px | 0.32 | 1.04 | 48 |
| stroke 9 | 37 % → 36 % | 183.2 px | 0.32 | 0.97 | 81 |
| stroke 10 | 33 % → 32 % | 300.4 px | 0.32 | 0.97 | 56 |

Numbers say: wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #28 Miles Davis black lines — own sheet
own sheet 600 × 600 · Ink 1.00 · 22 px · 6.4 s

![Brush Artist · Refs · #28 Miles Davis black lines — own sheet](Brush-Artist-Refs-28-Miles-Davis-black-lines-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 22 % → 31 % | 36.1 px | 0.88 | 1.42 | 199 |
| stroke 2 | 26 % → 47 % | 35.8 px | 0.88 | 1.79 | 144 |
| stroke 3 | 38 % → 42 % | 73.3 px | 0.88 | 1.11 | 110 |
| stroke 4 | 41 % → 47 % | 81.4 px | 0.88 | 1.16 | 172 |
| stroke 5 | 54 % → 54 % | 108.2 px | 0.88 | 1.00 | 141 |

Numbers say: wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #29 Shrigley magenta asterisk — own sheet
own sheet 600 × 600 · Watercolour 1.00 · 70 px · 6.1 s

![Brush Artist · Refs · #29 Shrigley magenta asterisk — own sheet](Brush-Artist-Refs-29-Shrigley-magenta-asterisk-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 13 % → 37 % | 46.6 px | 0.67 | 2.86 | 193 |
| stroke 2 | 12 % → 12 % | 87.1 px | 0.67 | 1.00 | 219 |
| stroke 3 | 28 % → 37 % | 100.9 px | 0.67 | 1.31 | 210 |
| stroke 4 | 23 % → 23 % | 164.0 px | 0.67 | 1.02 | 193 |

Numbers say: wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #30 Red gouache face patch — own sheet
own sheet 600 × 600 · Gouache 1.00 · 60 px · 11.7 s

![Brush Artist · Refs · #30 Red gouache face patch — own sheet](Brush-Artist-Refs-30-Red-gouache-face-patch-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 12 % → 37 % | 51.5 px | 0.54 | 3.23 | 151 |
| stroke 2 | 15 % → 40 % | 74.5 px | 0.54 | 2.72 | 177 |
| stroke 3 | 24 % → 50 % | 115.9 px | 0.54 | 2.06 | 177 |
| stroke 4 | 27 % → 52 % | 134.1 px | 0.54 | 1.94 | 159 |
| stroke 5 | 34 % → 60 % | 159.9 px | 0.54 | 1.77 | 180 |
| stroke 6 | 35 % → 61 % | 178.3 px | 0.54 | 1.76 | 193 |
| stroke 7 | 34 % → 59 % | 160.9 px | 0.54 | 1.73 | 189 |
| stroke 8 | 34 % → 56 % | 162.5 px | 0.54 | 1.66 | 166 |
| stroke 9 | 36 % → 60 % | 173.1 px | 0.54 | 1.66 | 146 |
| stroke 10 | 38 % → 62 % | 196.8 px | 0.54 | 1.64 | 180 |
| stroke 11 | 37 % → 61 % | 182.4 px | 0.54 | 1.66 | 169 |
| stroke 12 | 36 % → 58 % | 178.3 px | 0.54 | 1.62 | 184 |
| stroke 13 | 33 % → 46 % | 156.5 px | 0.54 | 1.39 | 170 |
| stroke 14 | 33 % → 41 % | 157.6 px | 0.54 | 1.25 | 177 |
| stroke 15 | 33 % → 37 % | 153.4 px | 0.54 | 1.12 | 190 |
| stroke 16 | 39 % → 39 % | 184.9 px | 0.54 | 0.99 | 169 |

Numbers say: wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #31 Warhol blotted line — own sheet
own sheet 600 × 600 · Ink 1.00 · 6 px · 5.0 s

![Brush Artist · Refs · #31 Warhol blotted line — own sheet](Brush-Artist-Refs-31-Warhol-blotted-line-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 22 % → 43 % | 16.5 px | 0.83 | 1.94 | 105 |
| stroke 2 | 17 % → 23 % | 15.7 px | 0.81 | 1.35 | 76 |
| stroke 3 | 24 % → 25 % | 24.9 px | 0.81 | 1.03 | 75 |
| stroke 4 | 32 % → 41 % | 32.7 px | 0.83 | 1.28 | 58 |
| stroke 5 | 37 % → 45 % | 38.1 px | 0.83 | 1.21 | 72 |
| stroke 6 | 34 % → 35 % | 27.8 px | 0.81 | 1.03 | 95 |

Numbers say: wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #32 Thick orange swipes — own sheet
own sheet 600 × 600 · Impasto 1.00 · 90 px · 3.7 s

![Brush Artist · Refs · #32 Thick orange swipes — own sheet](Brush-Artist-Refs-32-Thick-orange-swipes-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 14 % → 27 % | 86.9 px | 0.02 | 1.89 | 355 |
| stroke 2 | 26 % → 37 % | 178.2 px | 0.02 | 1.41 | 346 |
| stroke 3 | 27 % → 27 % | 176.5 px | 0.02 | 0.98 | 371 |

Numbers say: wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #33 Red wet-in-wet band — own sheet
own sheet 600 × 600 · Watercolour 1.00 · 80 px · 11.5 s

![Brush Artist · Refs · #33 Red wet-in-wet band — own sheet](Brush-Artist-Refs-33-Red-wet-in-wet-band-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 22 % → 57 % | 83.4 px | 0.61 | 2.61 | 467 |
| stroke 2 | 28 % → 51 % | 228.4 px | 0.62 | 1.82 | 106 |
| stroke 3 | 34 % → 53 % | 330.0 px | 0.61 | 1.57 | 125 |
| stroke 4 | 40 % → 60 % | 389.9 px | 0.62 | 1.51 | 127 |
| stroke 5 | 40 % → 55 % | 339.4 px | 0.61 | 1.38 | 137 |
| stroke 6 | 41 % → 48 % | 310.3 px | 0.59 | 1.18 | 128 |

Numbers say: wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #34 Magenta oil patches — own sheet
own sheet 600 × 600 · Oil 0.89 · Oil glaze 0.11 · 60 px · 3.4 s

![Brush Artist · Refs · #34 Magenta oil patches — own sheet](Brush-Artist-Refs-34-Magenta-oil-patches-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 8 % → 39 % | 57.1 px | 0.13 | 4.77 | 83 |
| stroke 2 | 8 % → 28 % | 56.7 px | 0.13 | 3.32 | 73 |
| stroke 3 | 7 % → 32 % | 58.5 px | 0.12 | 4.60 | 70 |
| stroke 4 | 15 % → 19 % | 122.1 px | 0.12 | 1.26 | 61 |
| stroke 5 | 21 % → 30 % | 112.0 px | 0.12 | 1.45 | 132 |
| stroke 6 | 19 % → 36 % | 159.5 px | 0.12 | 1.91 | 69 |
| stroke 7 | 28 % → 33 % | 226.4 px | 0.12 | 1.17 | 65 |
| stroke 8 | 30 % → 37 % | 213.4 px | 0.13 | 1.21 | 95 |
| stroke 9 | 23 % → 24 % | 147.7 px | 0.13 | 1.07 | 89 |
| stroke 10 | 27 % → 27 % | 240.3 px | 0.13 | 1.00 | 63 |
| stroke 11 | 33 % → 33 % | 296.9 px | 0.12 | 1.00 | 68 |
| stroke 12 | 24 % → 24 % | 173.5 px | 0.12 | 1.00 | 74 |

Numbers say: wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #35 Red band with runs — own sheet
own sheet 600 × 600 · Watercolour 1.00 · 70 px · 8.9 s

![Brush Artist · Refs · #35 Red band with runs — own sheet](Brush-Artist-Refs-35-Red-band-with-runs-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 37 % → 47 % | 140.3 px | 0.45 | 1.27 | 385 |

## Brush Artist · Refs · #36 Magenta letters flat brush — own sheet
own sheet 600 × 600 · Gouache 1.00 · 36 px · 11.5 s

![Brush Artist · Refs · #36 Magenta letters flat brush — own sheet](Brush-Artist-Refs-36-Magenta-letters-flat-brush-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 20 % → 39 % | 59.0 px | 0.50 | 1.95 | 24 |
| stroke 2 | 20 % → 32 % | 46.6 px | 0.50 | 1.59 | 35 |
| stroke 3 | 29 % → 54 % | 86.8 px | 0.50 | 1.86 | 29 |
| stroke 4 | 26 % → 44 % | 51.2 px | 0.50 | 1.67 | 128 |
| stroke 5 | 33 % → 55 % | 96.1 px | 0.50 | 1.67 | 77 |
| stroke 6 | 42 % → 56 % | 242.4 px | 0.50 | 1.33 | 19 |
| stroke 7 | 30 % → 44 % | 56.7 px | 0.50 | 1.45 | 128 |
| stroke 8 | 31 % → 53 % | 98.5 px | 0.50 | 1.68 | 68 |
| stroke 9 | 38 % → 51 % | 158.3 px | 0.50 | 1.33 | 35 |
| stroke 10 | 37 % → 63 % | 106.7 px | 0.50 | 1.72 | 62 |
| stroke 11 | 39 % → 62 % | 225.9 px | 0.50 | 1.58 | 17 |
| stroke 12 | 43 % → 56 % | 81.9 px | 0.50 | 1.29 | 120 |
| stroke 13 | 32 % → 46 % | 117.6 px | 0.50 | 1.43 | 35 |
| stroke 14 | 35 % → 52 % | 134.4 px | 0.50 | 1.47 | 38 |
| stroke 15 | 38 % → 56 % | 108.5 px | 0.50 | 1.49 | 121 |
| stroke 16 | 41 % → 50 % | 232.0 px | 0.50 | 1.23 | 18 |
| stroke 17 | 44 % → 52 % | 81.7 px | 0.50 | 1.19 | 121 |
| stroke 18 | 27 % → 36 % | 97.5 px | 0.50 | 1.35 | 45 |
| stroke 19 | 40 % → 39 % | 117.0 px | 0.50 | 0.96 | 34 |
| stroke 20 | 45 % → 45 % | 132.2 px | 0.50 | 0.99 | 41 |
| stroke 21 | 41 % → 39 % | 78.6 px | 0.50 | 0.96 | 105 |

Numbers say: wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #37 Oil still life dabs — own sheet
own sheet 600 × 600 · Oil 0.89 · Oil glaze 0.11 · 40 px · 2.8 s

![Brush Artist · Refs · #37 Oil still life dabs — own sheet](Brush-Artist-Refs-37-Oil-still-life-dabs-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 6 % → 6 % | 38.2 px | 0.37 | 1.00 | 36 |
| stroke 2 | 6 % → 26 % | 39.8 px | 0.39 | 4.69 | 25 |
| stroke 3 | 11 % → 33 % | 86.6 px | 0.39 | 3.00 | 17 |
| stroke 4 | 8 % → 8 % | 39.3 px | 0.39 | 1.00 | 47 |
| stroke 5 | 6 % → 10 % | 43.2 px | 0.38 | 1.67 | 27 |
| stroke 6 | 13 % → 29 % | 80.2 px | 0.39 | 2.26 | 33 |
| stroke 7 | 11 % → 22 % | 113.8 px | 0.38 | 2.08 | 17 |
| stroke 8 | 8 % → 13 % | 85.1 px | 0.38 | 1.59 | 11 |
| stroke 9 | 12 % → 13 % | 61.0 px | 0.38 | 1.12 | 46 |
| stroke 10 | 20 % → 24 % | 100.4 px | 0.39 | 1.20 | 38 |
| stroke 11 | 23 % → 27 % | 194.4 px | 0.39 | 1.15 | 12 |
| stroke 12 | 20 % → 20 % | 212.6 px | 0.39 | 1.00 | 12 |
| stroke 13 | 15 % → 15 % | 150.6 px | 0.39 | 1.00 | 9 |
| stroke 14 | 15 % → 15 % | 121.2 px | 0.38 | 1.00 | 16 |

Numbers say: wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #38 Sanguine drawing — own sheet
own sheet 600 × 600 · Pastel 1.00 · 6 px · 2.4 s

![Brush Artist · Refs · #38 Sanguine drawing — own sheet](Brush-Artist-Refs-38-Sanguine-drawing-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 3 % → 15 % | 3.3 px | 0.57 | 4.99 | 9 |
| stroke 2 | 3 % → 8 % | 2.9 px | 0.57 | 3.03 | 4 |
| stroke 3 | 3 % → 9 % | 3.3 px | 0.57 | 3.13 | 12 |
| stroke 4 | 2 % → 18 % | 2.8 px | 0.57 | 7.17 | 9 |
| stroke 5 | 3 % → 7 % | 2.9 px | 0.57 | 2.87 | 3 |
| stroke 6 | 3 % → 19 % | 3.5 px | 0.57 | 6.36 | 3 |
| stroke 7 | 5 % → 15 % | 5.3 px | 0.57 | 3.13 | 7 |
| stroke 8 | 4 % → 16 % | 4.8 px | 0.57 | 3.71 | 8 |
| stroke 9 | 3 % → 8 % | 3.4 px | 0.57 | 2.52 | 3 |
| stroke 10 | 4 % → 16 % | 4.9 px | 0.57 | 3.75 | 9 |
| stroke 11 | 3 % → 4 % | 3.0 px | 0.57 | 1.63 | 8 |
| stroke 12 | 4 % → 16 % | 4.7 px | 0.57 | 3.75 | 3 |
| stroke 13 | 8 % → 18 % | 9.2 px | 0.57 | 2.20 | 5 |
| stroke 14 | 5 % → 14 % | 5.3 px | 0.57 | 2.95 | 4 |
| stroke 15 | 9 % → 18 % | 10.7 px | 0.57 | 1.88 | 12 |
| stroke 16 | 6 % → 16 % | 7.0 px | 0.57 | 2.64 | 8 |
| stroke 17 | 4 % → 9 % | 5.0 px | 0.57 | 2.12 | 18 |
| stroke 18 | 3 % → 5 % | 3.1 px | 0.57 | 1.89 | 10 |
| stroke 19 | 6 % → 17 % | 7.4 px | 0.57 | 2.68 | 10 |
| stroke 20 | 9 % → 14 % | 9.8 px | 0.57 | 1.66 | 7 |
| stroke 21 | 4 % → 4 % | 4.6 px | 0.57 | 1.00 | 3 |
| stroke 22 | 8 % → 14 % | 9.2 px | 0.57 | 1.71 | 6 |
| stroke 23 | 8 % → 12 % | 8.7 px | 0.57 | 1.63 | 10 |
| stroke 24 | 4 % → 8 % | 5.0 px | 0.57 | 1.72 | 9 |
| stroke 25 | 8 % → 15 % | 9.3 px | 0.57 | 1.87 | 6 |
| stroke 26 | 6 % → 8 % | 6.9 px | 0.57 | 1.32 | 6 |
| stroke 27 | 4 % → 5 % | 4.8 px | 0.57 | 1.07 | 10 |
| stroke 28 | 8 % → 13 % | 8.9 px | 0.57 | 1.61 | 8 |
| stroke 29 | 8 % → 17 % | 9.0 px | 0.57 | 2.18 | 12 |
| stroke 30 | 13 % → 17 % | 15.2 px | 0.57 | 1.29 | 6 |
| stroke 31 | 5 % → 7 % | 6.0 px | 0.57 | 1.24 | 4 |
| stroke 32 | 11 % → 14 % | 12.9 px | 0.57 | 1.23 | 12 |
| stroke 33 | 8 % → 9 % | 9.5 px | 0.57 | 1.06 | 8 |
| stroke 34 | 11 % → 14 % | 12.3 px | 0.57 | 1.34 | 3 |
| stroke 35 | 9 % → 15 % | 10.7 px | 0.57 | 1.57 | 4 |
| stroke 36 | 10 % → 13 % | 11.9 px | 0.57 | 1.26 | 3 |
| stroke 37 | 10 % → 16 % | 11.4 px | 0.57 | 1.63 | 7 |
| stroke 38 | 14 % → 20 % | 15.3 px | 0.57 | 1.46 | 3 |
| stroke 39 | 14 % → 17 % | 16.5 px | 0.57 | 1.20 | 5 |
| stroke 40 | 6 % → 7 % | 7.3 px | 0.57 | 1.15 | 6 |
| stroke 41 | 16 % → 16 % | 18.2 px | 0.57 | 1.01 | 5 |
| stroke 42 | 14 % → 16 % | 16.1 px | 0.57 | 1.15 | 5 |
| stroke 43 | 11 % → 13 % | 13.0 px | 0.57 | 1.16 | 4 |
| stroke 44 | 13 % → 16 % | 15.2 px | 0.57 | 1.19 | 5 |
| stroke 45 | 2 % → 2 % | 2.8 px | 0.56 | 1.00 | 3 |
| stroke 46 | 17 % → 17 % | 18.9 px | 0.57 | 1.00 | 6 |
| stroke 47 | 14 % → 14 % | 15.9 px | 0.57 | 1.00 | 7 |
| stroke 48 | 13 % → 14 % | 14.7 px | 0.57 | 1.06 | 5 |
| stroke 49 | 19 % → 19 % | 21.8 px | 0.57 | 1.00 | 8 |
| stroke 50 | 11 % → 11 % | 12.2 px | 0.57 | 1.00 | 3 |

Numbers say: wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #39 Very thick impasto — own sheet
own sheet 600 × 600 · Impasto 1.00 · 60 px · 5.1 s

![Brush Artist · Refs · #39 Very thick impasto — own sheet](Brush-Artist-Refs-39-Very-thick-impasto-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 24 % → 35 % | 56.0 px | 0.43 | 1.45 | 343 |
| stroke 2 | 30 % → 46 % | 91.6 px | 0.43 | 1.53 | 331 |
| stroke 3 | 37 % → 49 % | 123.2 px | 0.43 | 1.32 | 327 |
| stroke 4 | 31 % → 43 % | 90.4 px | 0.43 | 1.39 | 384 |
| stroke 5 | 41 % → 40 % | 102.1 px | 0.43 | 0.97 | 383 |

Numbers say: wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #40 Watercolour blooms — own sheet
own sheet 600 × 600 · Watercolour 1.00 · 90 px · 9.4 s

![Brush Artist · Refs · #40 Watercolour blooms — own sheet](Brush-Artist-Refs-40-Watercolour-blooms-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 21 % → 27 % | 92.8 px | 0.12 | 1.28 | 953 |

## Brush Artist · Refs · #41 Coloured pencil hatching — own sheet
own sheet 600 × 600 · Pastel 1.00 · 4 px · 3.0 s

![Brush Artist · Refs · #41 Coloured pencil hatching — own sheet](Brush-Artist-Refs-41-Coloured-pencil-hatching-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 3 % → 15 % | 2.3 px | 0.35 | 5.04 | 11 |
| stroke 2 | 3 % → 8 % | 2.5 px | 0.35 | 2.34 | 8 |
| stroke 3 | 3 % → 12 % | 2.2 px | 0.35 | 4.03 | 4 |
| stroke 4 | 3 % → 20 % | 2.4 px | 0.35 | 6.35 | 4 |
| stroke 5 | 4 % → 8 % | 3.5 px | 0.35 | 1.78 | 5 |
| stroke 6 | 3 % → 14 % | 2.3 px | 0.35 | 4.57 | 5 |
| stroke 7 | 4 % → 17 % | 3.0 px | 0.35 | 4.34 | 3 |
| stroke 8 | 3 % → 13 % | 2.4 px | 0.35 | 4.14 | 5 |
| stroke 9 | 5 % → 12 % | 4.1 px | 0.35 | 2.18 | 7 |
| stroke 10 | 6 % → 17 % | 4.4 px | 0.35 | 2.92 | 5 |
| stroke 11 | 4 % → 14 % | 3.2 px | 0.35 | 3.38 | 4 |
| stroke 12 | 3 % → 3 % | 2.2 px | 0.35 | 1.00 | 10 |
| stroke 13 | 8 % → 19 % | 6.0 px | 0.35 | 2.35 | 5 |
| stroke 14 | 4 % → 15 % | 2.7 px | 0.35 | 4.14 | 2 |
| stroke 15 | 6 % → 13 % | 4.6 px | 0.35 | 2.12 | 9 |
| stroke 16 | 7 % → 12 % | 5.6 px | 0.35 | 1.63 | 6 |
| stroke 17 | 3 % → 3 % | 2.4 px | 0.35 | 1.00 | 3 |
| stroke 18 | 5 % → 9 % | 4.0 px | 0.36 | 1.63 | 4 |
| stroke 19 | 5 % → 14 % | 4.0 px | 0.35 | 2.72 | 6 |
| stroke 20 | 6 % → 16 % | 4.2 px | 0.35 | 2.94 | 2 |
| stroke 21 | 5 % → 15 % | 3.6 px | 0.35 | 3.13 | 5 |
| stroke 22 | 10 % → 18 % | 7.7 px | 0.35 | 1.77 | 18 |
| stroke 23 | 10 % → 15 % | 7.2 px | 0.35 | 1.54 | 6 |
| stroke 24 | 7 % → 15 % | 5.3 px | 0.35 | 2.12 | 11 |
| stroke 25 | 5 % → 12 % | 4.0 px | 0.35 | 2.27 | 5 |
| stroke 26 | 4 % → 7 % | 3.1 px | 0.35 | 1.79 | 6 |
| stroke 27 | 3 % → 8 % | 2.6 px | 0.35 | 2.35 | 7 |
| stroke 28 | 7 % → 11 % | 5.2 px | 0.36 | 1.68 | 5 |
| stroke 29 | 3 % → 15 % | 2.6 px | 0.35 | 4.48 | 4 |
| stroke 30 | 7 % → 10 % | 5.2 px | 0.35 | 1.40 | 5 |
| stroke 31 | 7 % → 16 % | 5.8 px | 0.35 | 2.09 | 3 |
| stroke 32 | 3 % → 6 % | 2.4 px | 0.36 | 1.93 | 4 |
| stroke 33 | 8 % → 13 % | 5.9 px | 0.35 | 1.65 | 6 |
| stroke 34 | 3 % → 6 % | 2.6 px | 0.35 | 1.71 | 8 |
| stroke 35 | 7 % → 15 % | 5.4 px | 0.35 | 2.11 | 8 |
| stroke 36 | 5 % → 5 % | 4.0 px | 0.35 | 1.01 | 6 |
| stroke 37 | 8 % → 16 % | 5.9 px | 0.35 | 2.07 | 11 |
| stroke 38 | 8 % → 14 % | 6.2 px | 0.35 | 1.71 | 5 |
| stroke 39 | 7 % → 12 % | 5.4 px | 0.35 | 1.65 | 9 |
| stroke 40 | 9 % → 20 % | 6.7 px | 0.36 | 2.23 | 3 |
| stroke 41 | 10 % → 15 % | 7.7 px | 0.35 | 1.46 | 7 |
| stroke 42 | 11 % → 19 % | 8.5 px | 0.36 | 1.73 | 4 |
| stroke 43 | 5 % → 9 % | 4.1 px | 0.35 | 1.66 | 8 |
| stroke 44 | 11 % → 15 % | 8.5 px | 0.36 | 1.41 | 5 |
| stroke 45 | 14 % → 19 % | 10.5 px | 0.35 | 1.37 | 2 |
| stroke 46 | 5 % → 7 % | 4.0 px | 0.35 | 1.38 | 6 |
| stroke 47 | 11 % → 14 % | 8.7 px | 0.36 | 1.21 | 5 |
| stroke 48 | 13 % → 18 % | 10.0 px | 0.36 | 1.36 | 6 |
| stroke 49 | 6 % → 9 % | 4.3 px | 0.35 | 1.65 | 5 |
| stroke 50 | 7 % → 7 % | 5.6 px | 0.35 | 1.00 | 4 |
| stroke 51 | 10 % → 16 % | 7.4 px | 0.36 | 1.67 | 9 |
| stroke 52 | 14 % → 16 % | 10.5 px | 0.35 | 1.19 | 5 |
| stroke 53 | 12 % → 16 % | 9.0 px | 0.35 | 1.35 | 6 |
| stroke 54 | 11 % → 16 % | 8.5 px | 0.35 | 1.46 | 5 |
| stroke 55 | 12 % → 16 % | 9.0 px | 0.35 | 1.34 | 2 |
| stroke 56 | 12 % → 13 % | 9.0 px | 0.35 | 1.11 | 5 |
| stroke 57 | 11 % → 14 % | 8.2 px | 0.36 | 1.31 | 4 |
| stroke 58 | 11 % → 12 % | 8.6 px | 0.35 | 1.12 | 3 |
| stroke 59 | 13 % → 15 % | 9.8 px | 0.35 | 1.16 | 2 |
| stroke 60 | 17 % → 22 % | 13.1 px | 0.35 | 1.26 | 6 |
| stroke 61 | 21 % → 22 % | 15.6 px | 0.35 | 1.05 | 5 |
| stroke 62 | 10 % → 10 % | 7.5 px | 0.35 | 1.00 | 5 |
| stroke 63 | 12 % → 13 % | 9.5 px | 0.35 | 1.09 | 7 |
| stroke 64 | 16 % → 17 % | 12.4 px | 0.35 | 1.02 | 7 |
| stroke 65 | 17 % → 17 % | 12.7 px | 0.35 | 1.00 | 7 |
| stroke 66 | 15 % → 15 % | 11.9 px | 0.35 | 1.00 | 5 |
| stroke 67 | 13 % → 14 % | 9.9 px | 0.35 | 1.06 | 4 |
| stroke 68 | 5 % → 10 % | 4.1 px | 0.35 | 1.90 | 2 |
| stroke 69 | 6 % → 6 % | 4.3 px | 0.35 | 1.00 | 5 |
| stroke 70 | 11 % → 14 % | 8.5 px | 0.35 | 1.28 | 4 |
| stroke 71 | 10 % → 12 % | 7.7 px | 0.35 | 1.17 | 8 |
| stroke 72 | 6 % → 7 % | 4.5 px | 0.35 | 1.26 | 3 |
| stroke 73 | 14 % → 14 % | 10.4 px | 0.35 | 1.00 | 3 |
| stroke 74 | 16 % → 16 % | 12.3 px | 0.35 | 1.00 | 12 |
| stroke 75 | 17 % → 17 % | 13.1 px | 0.35 | 1.00 | 4 |
| stroke 76 | 15 % → 15 % | 11.7 px | 0.36 | 1.00 | 5 |
| stroke 77 | 8 % → 10 % | 6.0 px | 0.35 | 1.32 | 9 |
| stroke 78 | 10 % → 10 % | 7.5 px | 0.35 | 1.00 | 4 |
| stroke 79 | 8 % → 8 % | 6.2 px | 0.35 | 1.00 | 6 |
| stroke 80 | 12 % → 12 % | 9.1 px | 0.36 | 1.00 | 2 |

Numbers say: wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #42 Oil pastel shaggy — own sheet
own sheet 600 × 600 · Pastel 1.00 · 18 px · 3.1 s

![Brush Artist · Refs · #42 Oil pastel shaggy — own sheet](Brush-Artist-Refs-42-Oil-pastel-shaggy-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 5 % → 27 % | 8.5 px | 0.29 | 5.25 | 13 |
| stroke 2 | 5 % → 24 % | 7.8 px | 0.29 | 5.03 | 6 |
| stroke 3 | 5 % → 29 % | 8.8 px | 0.29 | 5.49 | 10 |
| stroke 4 | 5 % → 11 % | 9.1 px | 0.28 | 1.99 | 9 |
| stroke 5 | 6 % → 11 % | 10.2 px | 0.28 | 1.77 | 12 |
| stroke 6 | 8 % → 36 % | 13.4 px | 0.29 | 4.51 | 10 |
| stroke 7 | 11 % → 30 % | 18.0 px | 0.28 | 2.80 | 19 |
| stroke 8 | 7 % → 37 % | 10.8 px | 0.29 | 5.62 | 11 |
| stroke 9 | 8 % → 21 % | 13.4 px | 0.29 | 2.61 | 14 |
| stroke 10 | 8 % → 18 % | 13.2 px | 0.28 | 2.30 | 8 |
| stroke 11 | 5 % → 26 % | 8.8 px | 0.28 | 4.90 | 16 |
| stroke 12 | 8 % → 19 % | 13.1 px | 0.29 | 2.34 | 14 |
| stroke 13 | 12 % → 23 % | 20.4 px | 0.28 | 1.92 | 10 |
| stroke 14 | 5 % → 22 % | 7.6 px | 0.29 | 4.76 | 7 |
| stroke 15 | 6 % → 24 % | 9.2 px | 0.29 | 4.26 | 11 |
| stroke 16 | 9 % → 21 % | 15.6 px | 0.29 | 2.20 | 15 |
| stroke 17 | 16 % → 37 % | 26.4 px | 0.29 | 2.36 | 14 |
| stroke 18 | 14 % → 25 % | 22.6 px | 0.29 | 1.82 | 13 |
| stroke 19 | 14 % → 30 % | 23.7 px | 0.29 | 2.08 | 6 |
| stroke 20 | 21 % → 39 % | 35.4 px | 0.28 | 1.81 | 7 |
| stroke 21 | 9 % → 16 % | 14.3 px | 0.29 | 1.88 | 12 |
| stroke 22 | 14 % → 17 % | 23.1 px | 0.28 | 1.19 | 10 |
| stroke 23 | 12 % → 17 % | 20.4 px | 0.29 | 1.37 | 11 |
| stroke 24 | 18 % → 26 % | 30.0 px | 0.29 | 1.43 | 15 |
| stroke 25 | 19 % → 34 % | 32.1 px | 0.29 | 1.75 | 13 |
| stroke 26 | 5 % → 13 % | 8.8 px | 0.28 | 2.45 | 6 |
| stroke 27 | 18 % → 26 % | 30.3 px | 0.29 | 1.41 | 13 |
| stroke 28 | 14 % → 23 % | 23.2 px | 0.29 | 1.66 | 9 |
| stroke 29 | 9 % → 26 % | 14.2 px | 0.29 | 3.08 | 12 |
| stroke 30 | 15 % → 36 % | 24.5 px | 0.29 | 2.44 | 15 |
| stroke 31 | 13 % → 17 % | 22.4 px | 0.28 | 1.24 | 8 |
| stroke 32 | 16 % → 29 % | 26.3 px | 0.29 | 1.82 | 9 |
| stroke 33 | 15 % → 16 % | 24.4 px | 0.29 | 1.09 | 7 |
| stroke 34 | 19 % → 27 % | 31.4 px | 0.28 | 1.44 | 19 |
| stroke 35 | 25 % → 35 % | 40.9 px | 0.29 | 1.39 | 21 |
| stroke 36 | 24 % → 33 % | 40.3 px | 0.29 | 1.34 | 10 |
| stroke 37 | 11 % → 12 % | 18.4 px | 0.28 | 1.04 | 9 |
| stroke 38 | 19 % → 24 % | 30.6 px | 0.29 | 1.31 | 8 |
| stroke 39 | 16 % → 22 % | 27.0 px | 0.28 | 1.35 | 8 |
| stroke 40 | 21 % → 29 % | 34.9 px | 0.29 | 1.38 | 12 |
| stroke 41 | 31 % → 34 % | 51.2 px | 0.29 | 1.12 | 11 |
| stroke 42 | 23 % → 29 % | 37.9 px | 0.29 | 1.28 | 40 |
| stroke 43 | 12 % → 12 % | 20.2 px | 0.28 | 1.00 | 28 |
| stroke 44 | 29 % → 36 % | 48.4 px | 0.28 | 1.25 | 12 |
| stroke 45 | 16 % → 16 % | 25.6 px | 0.28 | 1.00 | 13 |
| stroke 46 | 28 % → 33 % | 46.9 px | 0.29 | 1.15 | 16 |
| stroke 47 | 37 % → 41 % | 61.7 px | 0.28 | 1.09 | 11 |
| stroke 48 | 28 % → 35 % | 47.2 px | 0.29 | 1.26 | 8 |
| stroke 49 | 27 % → 30 % | 43.8 px | 0.29 | 1.11 | 12 |
| stroke 50 | 37 % → 40 % | 61.9 px | 0.28 | 1.07 | 10 |
| stroke 51 | 15 % → 15 % | 25.8 px | 0.29 | 1.00 | 6 |
| stroke 52 | 37 % → 37 % | 61.5 px | 0.29 | 1.01 | 6 |
| stroke 53 | 22 % → 26 % | 35.6 px | 0.29 | 1.20 | 14 |
| stroke 54 | 17 % → 19 % | 29.0 px | 0.29 | 1.10 | 6 |
| stroke 55 | 15 % → 15 % | 24.6 px | 0.29 | 1.00 | 12 |
| stroke 56 | 13 % → 14 % | 21.3 px | 0.28 | 1.08 | 10 |
| stroke 57 | 23 % → 23 % | 38.0 px | 0.29 | 1.00 | 10 |
| stroke 58 | 26 % → 28 % | 43.7 px | 0.29 | 1.06 | 11 |
| stroke 59 | 40 % → 40 % | 66.1 px | 0.29 | 1.00 | 11 |
| stroke 60 | 21 % → 21 % | 34.4 px | 0.29 | 1.00 | 13 |

Numbers say: wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #43 Dragged black ink blocks — own sheet
own sheet 600 × 600 · Gouache 1.00 · 70 px · 7.0 s

![Brush Artist · Refs · #43 Dragged black ink blocks — own sheet](Brush-Artist-Refs-43-Dragged-black-ink-blocks-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 9 % → 4 % | 22.0 px | 0.46 | 0.44 | 412 |
| stroke 2 | 9 % → 8 % | 32.8 px | 0.46 | 0.83 | 445 |
| stroke 3 | 17 % → 13 % | 59.6 px | 0.46 | 0.80 | 449 |
| stroke 4 | 19 % → 11 % | 67.2 px | 0.46 | 0.55 | 475 |
| stroke 5 | 28 % → 12 % | 64.7 px | 0.46 | 0.44 | 436 |

## Brush Artist · Refs · #44 Blue looping ribbon — own sheet
own sheet 600 × 600 · Oil 1.00 · 80 px · 5.0 s

![Brush Artist · Refs · #44 Blue looping ribbon — own sheet](Brush-Artist-Refs-44-Blue-looping-ribbon-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 32 % → 32 % | 42.1 px | 0.78 | 1.00 | 2828 |

## Brush Artist · Refs · #45 Soft pastel pepper — own sheet
own sheet 600 × 600 · Pastel 1.00 · 40 px · 4.6 s

![Brush Artist · Refs · #45 Soft pastel pepper — own sheet](Brush-Artist-Refs-45-Soft-pastel-pepper-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 10 % → 38 % | 11.3 px | 0.49 | 3.70 | 386 |
| stroke 2 | 18 % → 33 % | 20.7 px | 0.49 | 1.89 | 351 |
| stroke 3 | 25 % → 36 % | 16.9 px | 0.49 | 1.46 | 312 |
| stroke 4 | 24 % → 34 % | 29.4 px | 0.49 | 1.45 | 318 |
| stroke 5 | 30 % → 30 % | 20.9 px | 0.49 | 1.00 | 223 |
| stroke 6 | 35 % → 44 % | 22.7 px | 0.49 | 1.24 | 307 |
| stroke 7 | 39 % → 43 % | 21.3 px | 0.48 | 1.11 | 333 |
| stroke 8 | 43 % → 43 % | 43.6 px | 0.49 | 1.00 | 346 |

Numbers say: wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #46 Red-brown ink lips — own sheet
own sheet 600 × 600 · Watercolour 1.00 · 50 px · 7.7 s

![Brush Artist · Refs · #46 Red-brown ink lips — own sheet](Brush-Artist-Refs-46-Red-brown-ink-lips-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 13 % → 26 % | 54.5 px | 0.56 | 1.96 | 99 |
| stroke 2 | 17 % → 31 % | 72.4 px | 0.53 | 1.89 | 85 |

Numbers say: wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #47 Pink knife slabs — own sheet
own sheet 600 × 600 · Impasto 1.00 · 90 px · 4.5 s

![Brush Artist · Refs · #47 Pink knife slabs — own sheet](Brush-Artist-Refs-47-Pink-knife-slabs-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 16 % → 32 % | 81.7 px | 0.10 | 1.97 | 329 |
| stroke 2 | 29 % → 42 % | 165.7 px | 0.10 | 1.45 | 309 |
| stroke 3 | 29 % → 43 % | 165.3 px | 0.10 | 1.47 | 304 |
| stroke 4 | 39 % → 38 % | 166.2 px | 0.10 | 0.97 | 338 |

Numbers say: wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #48 Black bands with drips — own sheet
own sheet 600 × 600 · Gouache 1.00 · 70 px · 10.3 s

![Brush Artist · Refs · #48 Black bands with drips — own sheet](Brush-Artist-Refs-48-Black-bands-with-drips-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 28 % → 41 % | 73.2 px | 0.39 | 1.46 | 467 |
| stroke 2 | 43 % → 57 % | 137.5 px | 0.39 | 1.33 | 534 |
| stroke 3 | 45 % → 57 % | 141.4 px | 0.39 | 1.27 | 512 |
| stroke 4 | 48 % → 46 % | 140.3 px | 0.39 | 0.96 | 516 |

## Brush Artist · Refs · #49 Magenta letters round brush — own sheet
own sheet 600 × 600 · Ink 1.00 · 30 px · 9.0 s

![Brush Artist · Refs · #49 Magenta letters round brush — own sheet](Brush-Artist-Refs-49-Magenta-letters-round-brush-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 27 % → 46 % | 64.7 px | 0.52 | 1.68 | 33 |
| stroke 2 | 29 % → 41 % | 53.0 px | 0.53 | 1.40 | 40 |
| stroke 3 | 42 % → 68 % | 98.0 px | 0.52 | 1.62 | 37 |
| stroke 4 | 33 % → 52 % | 53.5 px | 0.52 | 1.56 | 156 |
| stroke 5 | 41 % → 66 % | 97.1 px | 0.52 | 1.62 | 85 |
| stroke 6 | 56 % → 72 % | 237.9 px | 0.52 | 1.28 | 20 |
| stroke 7 | 42 % → 58 % | 65.1 px | 0.52 | 1.36 | 122 |
| stroke 8 | 36 % → 61 % | 92.6 px | 0.53 | 1.71 | 69 |
| stroke 9 | 50 % → 62 % | 156.5 px | 0.52 | 1.24 | 27 |
| stroke 10 | 43 % → 73 % | 102.9 px | 0.52 | 1.68 | 69 |
| stroke 11 | 52 % → 72 % | 221.9 px | 0.52 | 1.39 | 22 |
| stroke 12 | 54 % → 70 % | 84.9 px | 0.52 | 1.28 | 139 |
| stroke 13 | 42 % → 53 % | 116.2 px | 0.53 | 1.27 | 44 |
| stroke 14 | 45 % → 68 % | 131.6 px | 0.53 | 1.52 | 39 |
| stroke 15 | 43 % → 63 % | 101.8 px | 0.52 | 1.47 | 68 |
| stroke 16 | 52 % → 61 % | 220.3 px | 0.52 | 1.19 | 20 |
| stroke 17 | 53 % → 64 % | 82.3 px | 0.52 | 1.19 | 103 |
| stroke 18 | 36 % → 43 % | 98.8 px | 0.53 | 1.20 | 35 |
| stroke 19 | 53 % → 52 % | 122.0 px | 0.52 | 0.99 | 51 |
| stroke 20 | 55 % → 55 % | 127.4 px | 0.52 | 1.00 | 32 |
| stroke 21 | 49 % → 49 % | 80.4 px | 0.52 | 1.00 | 92 |

Numbers say: wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #50 Thick swipes on photo — own sheet
own sheet 600 × 600 · Impasto 1.00 · 40 px · 3.0 s

![Brush Artist · Refs · #50 Thick swipes on photo — own sheet](Brush-Artist-Refs-50-Thick-swipes-on-photo-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 9 % → 21 % | 43.0 px | 0.34 | 2.34 | 51 |
| stroke 2 | 9 % → 16 % | 42.2 px | 0.35 | 1.82 | 33 |
| stroke 3 | 10 % → 11 % | 42.0 px | 0.34 | 1.07 | 55 |
| stroke 4 | 11 % → 18 % | 43.8 px | 0.35 | 1.61 | 40 |
| stroke 5 | 11 % → 10 % | 42.2 px | 0.34 | 0.94 | 37 |
| stroke 6 | 18 % → 21 % | 99.9 px | 0.34 | 1.19 | 35 |
| stroke 7 | 22 % → 26 % | 93.0 px | 0.35 | 1.19 | 38 |
| stroke 8 | 21 % → 21 % | 120.4 px | 0.34 | 0.96 | 32 |
| stroke 9 | 10 % → 11 % | 43.1 px | 0.34 | 1.12 | 44 |
| stroke 10 | 22 % → 22 % | 75.6 px | 0.34 | 0.96 | 64 |
| stroke 11 | 8 % → 8 % | 42.1 px | 0.35 | 0.95 | 44 |
| stroke 12 | 17 % → 16 % | 94.7 px | 0.34 | 0.96 | 31 |

Numbers say: wet paint spreads well beyond the stroke.

## Brush Artist · Ink — dry brush — own sheet
own sheet 600 × 600 · Gouache 1.00 · 30 px · 3.3 s

![Brush Artist · Ink — dry brush — own sheet](Brush-Artist-Ink-dry-brush-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| ear | 8 % → 2 % | 9.7 px | 0.85 | 0.22 | 573 |
| drag0 | 4 % → 6 % | 7.6 px | 0.85 | 1.51 | 122 |
| drag1 | 7 % → 7 % | 15.1 px | 0.85 | 0.89 | 114 |
| drag2 | 10 % → 7 % | 22.1 px | 0.85 | 0.71 | 90 |
| drag3 | 12 % → 7 % | 30.1 px | 0.85 | 0.60 | 80 |

Numbers say: wet paint spreads well beyond the stroke.

## Brush Artist · Watercolour — blue — own sheet
own sheet 600 × 600 · Watercolour 0.93 · Ink 0.07 · 40 px · 9.2 s

![Brush Artist · Watercolour — blue — own sheet](Brush-Artist-Watercolour-blue-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| s0 | 7 % → 24 % | 28.8 px | 0.30 | 3.32 | 46 |
| s1 | 6 % → 33 % | 10.1 px | 0.37 | 6.00 | 44 |
| s2 | 10 % → 19 % | 44.2 px | 0.26 | 1.81 | 57 |
| s3 | 10 % → 18 % | 26.7 px | 0.31 | 1.92 | 60 |
| s4 | 14 % → 30 % | 38.6 px | 0.36 | 2.16 | 78 |
| s5 | 19 % → 29 % | 39.3 px | 0.37 | 1.54 | 61 |
| s6 | 18 % → 22 % | 48.7 px | 0.31 | 1.25 | 57 |
| s7 | 25 % → 36 % | 32.7 px | 0.37 | 1.46 | 41 |
| s8 | 21 % → 25 % | 79.8 px | 0.30 | 1.20 | 47 |

Numbers say: wet paint spreads well beyond the stroke.

## Brush Artist · Charcoal — stick — own sheet
own sheet 600 × 600 · Charcoal 0.78 · Pastel 0.22 · 28 px · 1.3 s

![Brush Artist · Charcoal — stick — own sheet](Brush-Artist-Charcoal-stick-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| finger0 | 12 % → 25 % | 21.2 px | 0.83 | 2.03 | 44 |
| tip0 | 13 % → 21 % | 33.8 px | 0.83 | 1.70 | 6 |
| finger1 | 23 % → 41 % | 40.4 px | 0.83 | 1.77 | 42 |
| tip1 | 21 % → 29 % | 57.3 px | 0.83 | 1.38 | 15 |
| finger2 | 25 % → 37 % | 43.8 px | 0.83 | 1.49 | 39 |
| tip2 | 21 % → 29 % | 55.7 px | 0.83 | 1.40 | 14 |
| finger3 | 24 % → 27 % | 42.7 px | 0.83 | 1.14 | 33 |
| tip3 | 20 % → 20 % | 54.1 px | 0.83 | 1.00 | 17 |
| cig0 | 34 % → 47 % | 75.0 px | 0.83 | 1.39 | 14 |
| cig1 | 36 % → 47 % | 80.5 px | 0.83 | 1.30 | 16 |
| cig2 | 39 % → 47 % | 86.7 px | 0.83 | 1.20 | 17 |
| cig3 | 41 % → 47 % | 91.3 px | 0.83 | 1.14 | 16 |
| cig4 | 44 % → 46 % | 97.5 px | 0.83 | 1.06 | 16 |
| cig5 | 46 % → 46 % | 102.9 px | 0.83 | 1.00 | 19 |

Numbers say: wet paint spreads well beyond the stroke.

## Oil · Henry Ward · HW #02 cream over wet olive — own sheet
own sheet 600 × 600 · Oil 0.81 · Ink 0.19 · 56 px · 19.3 s

![Oil · Henry Ward · HW #02 cream over wet olive — own sheet](Oil-Henry-Ward-HW-02-cream-over-wet-olive-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 65 % → 27 % | 78.3 px | 0.39 | 0.41 | 1455 |
| stroke 2 | 79 % → 38 % | 144.1 px | 0.45 | 0.49 | 1789 |
| stroke 3 | 81 % → 53 % | 169.0 px | 0.41 | 0.65 | 1524 |
| stroke 4 | 81 % → 58 % | 169.0 px | 0.42 | 0.72 | 1541 |
| stroke 5 | 81 % → 51 % | 169.0 px | 0.45 | 0.62 | 1502 |
| stroke 6 | 81 % → 48 % | 172.1 px | 0.49 | 0.60 | 1288 |
| stroke 7 | 80 % → 35 % | 169.8 px | 0.50 | 0.44 | 1219 |
| stroke 8 | 92 % → 24 % | 167.0 px | 0.48 | 0.26 | 1327 |
| stroke 9 | 100 % → 14 % | 123.5 px | 0.40 | 0.14 | 1013 |
| stroke 10 | 10 % → 43 % | 39.5 px | 0.41 | 4.34 | 143 |
| stroke 11 | 17 % → 60 % | 67.8 px | 0.43 | 3.58 | 164 |
| stroke 12 | 6 % → 34 % | 24.8 px | 0.49 | 6.11 | 103 |
| stroke 13 | 27 % → 49 % | 105.8 px | 0.41 | 1.82 | 114 |
| stroke 14 | 33 % → 51 % | 117.3 px | 0.42 | 1.57 | 154 |
| stroke 15 | 39 % → 60 % | 146.4 px | 0.42 | 1.52 | 158 |
| stroke 16 | 46 % → 70 % | 231.0 px | 0.42 | 1.52 | 109 |
| stroke 17 | 33 % → 57 % | 115.8 px | 0.46 | 1.74 | 133 |
| stroke 18 | 30 % → 60 % | 119.6 px | 0.45 | 1.98 | 129 |
| stroke 19 | 31 % → 55 % | 146.5 px | 0.45 | 1.75 | 107 |
| stroke 20 | 31 % → 38 % | 121.8 px | 0.50 | 1.22 | 141 |
| stroke 21 | 32 % → 34 % | 115.3 px | 0.50 | 1.05 | 180 |
| stroke 22 | 43 % → 44 % | 144.1 px | 0.41 | 1.02 | 167 |
| stroke 23 | 52 % → 56 % | 186.3 px | 0.42 | 1.07 | 162 |
| stroke 24 | 52 % → 57 % | 228.3 px | 0.45 | 1.10 | 100 |
| stroke 25 | 52 % → 53 % | 198.9 px | 0.46 | 1.01 | 157 |
| stroke 26 | 36 % → 35 % | 149.6 px | 0.50 | 0.98 | 158 |

Numbers say: wet paint spreads well beyond the stroke.

## Oil · Henry Ward · HW #04 grey arcs over ochre — own sheet
own sheet 600 × 600 · Oil 1.00 · 46 px · 19.4 s

![Oil · Henry Ward · HW #04 grey arcs over ochre — own sheet](Oil-Henry-Ward-HW-04-grey-arcs-over-ochre-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 75 % → 40 % | 81.6 px | 0.20 | 0.54 | 1484 |
| stroke 2 | 87 % → 55 % | 142.8 px | 0.21 | 0.64 | 1818 |
| stroke 3 | 88 % → 77 % | 154.4 px | 0.20 | 0.88 | 1542 |
| stroke 4 | 88 % → 60 % | 154.4 px | 0.19 | 0.69 | 1512 |
| stroke 5 | 87 % → 39 % | 152.5 px | 0.17 | 0.44 | 1456 |
| stroke 6 | 85 % → 25 % | 149.8 px | 0.13 | 0.29 | 1297 |
| stroke 7 | 87 % → 30 % | 154.7 px | 0.10 | 0.35 | 1217 |
| stroke 8 | 89 % → 27 % | 148.0 px | 0.11 | 0.30 | 1331 |
| stroke 9 | 100 % → 23 % | 104.1 px | 0.11 | 0.23 | 1006 |
| stroke 10 | 10 % → 68 % | 37.3 px | 0.20 | 6.83 | 136 |
| stroke 11 | 17 % → 57 % | 59.3 px | 0.20 | 3.33 | 166 |
| stroke 12 | 18 % → 52 % | 69.7 px | 0.18 | 2.82 | 103 |
| stroke 13 | 33 % → 66 % | 89.4 px | 0.20 | 2.04 | 213 |
| stroke 14 | 39 % → 65 % | 149.0 px | 0.20 | 1.67 | 149 |
| stroke 15 | 39 % → 58 % | 134.5 px | 0.20 | 1.49 | 210 |
| stroke 16 | 45 % → 59 % | 167.0 px | 0.19 | 1.32 | 119 |
| stroke 17 | 50 % → 65 % | 186.5 px | 0.20 | 1.31 | 171 |
| stroke 18 | 50 % → 60 % | 171.1 px | 0.19 | 1.20 | 144 |
| stroke 19 | 56 % → 68 % | 184.4 px | 0.20 | 1.20 | 220 |
| stroke 20 | 59 % → 72 % | 182.4 px | 0.20 | 1.22 | 204 |
| stroke 21 | 63 % → 75 % | 204.4 px | 0.20 | 1.20 | 195 |
| stroke 22 | 34 % → 49 % | 123.9 px | 0.18 | 1.45 | 146 |
| stroke 23 | 57 % → 65 % | 207.7 px | 0.19 | 1.13 | 190 |
| stroke 24 | 74 % → 79 % | 284.7 px | 0.20 | 1.07 | 102 |
| stroke 25 | 53 % → 60 % | 181.9 px | 0.19 | 1.14 | 162 |
| stroke 26 | 73 % → 75 % | 253.8 px | 0.20 | 1.03 | 137 |
| stroke 27 | 20 % → 27 % | 63.2 px | 0.14 | 1.34 | 99 |
| stroke 28 | 19 % → 36 % | 67.7 px | 0.10 | 1.89 | 103 |
| stroke 29 | 21 % → 31 % | 85.3 px | 0.11 | 1.46 | 75 |
| stroke 30 | 29 % → 29 % | 86.7 px | 0.11 | 1.00 | 126 |

Numbers say: wet paint spreads well beyond the stroke.

## Oil · Henry Ward · HW #09 white arches over wet blue-grey — own sheet
own sheet 600 × 600 · Oil 1.00 · 46 px · 19.7 s

![Oil · Henry Ward · HW #09 white arches over wet blue-grey — own sheet](Oil-Henry-Ward-HW-09-white-arches-over-wet-blue-grey-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 78 % → 0 % | 80.2 px | 0.17 | 0.00 | 1414 |
| stroke 2 | 86 % → 5 % | 141.2 px | 0.11 | 0.06 | 1790 |
| stroke 3 | 87 % → 22 % | 154.3 px | 0.10 | 0.26 | 1507 |
| stroke 4 | 88 % → 39 % | 156.9 px | 0.10 | 0.45 | 1531 |
| stroke 5 | 85 % → 54 % | 150.4 px | 0.11 | 0.64 | 1446 |
| stroke 6 | 86 % → 64 % | 148.5 px | 0.11 | 0.74 | 1246 |
| stroke 7 | 87 % → 65 % | 152.0 px | 0.12 | 0.75 | 1213 |
| stroke 8 | 88 % → 58 % | 149.6 px | 0.14 | 0.66 | 1368 |
| stroke 9 | 100 % → 50 % | 99.7 px | 0.18 | 0.50 | 987 |
| stroke 10 | 8 % → 53 % | 30.2 px | 0.13 | 6.95 | 204 |
| stroke 11 | 17 % → 64 % | 31.3 px | 0.13 | 3.78 | 275 |
| stroke 12 | 19 % → 61 % | 34.8 px | 0.13 | 3.18 | 326 |
| stroke 13 | 27 % → 75 % | 60.6 px | 0.13 | 2.74 | 213 |
| stroke 14 | 30 % → 70 % | 22.0 px | 0.14 | 2.29 | 375 |
| stroke 15 | 38 % → 74 % | 107.4 px | 0.12 | 1.93 | 260 |
| stroke 16 | 47 % → 67 % | 142.0 px | 0.13 | 1.42 | 189 |
| stroke 17 | 56 % → 85 % | 161.2 px | 0.12 | 1.51 | 170 |
| stroke 18 | 48 % → 68 % | 131.5 px | 0.12 | 1.42 | 262 |
| stroke 19 | 53 % → 65 % | 163.1 px | 0.12 | 1.21 | 220 |
| stroke 20 | 49 % → 69 % | 128.0 px | 0.12 | 1.41 | 269 |
| stroke 21 | 39 % → 57 % | 98.4 px | 0.11 | 1.47 | 188 |
| stroke 22 | 50 % → 58 % | 134.7 px | 0.12 | 1.15 | 215 |
| stroke 23 | 68 % → 75 % | 216.3 px | 0.12 | 1.09 | 254 |
| stroke 24 | 66 % → 69 % | 211.2 px | 0.11 | 1.05 | 115 |
| stroke 25 | 57 % → 64 % | 160.8 px | 0.12 | 1.12 | 147 |
| stroke 26 | 64 % → 73 % | 245.4 px | 0.14 | 1.14 | 103 |
| stroke 27 | 53 % → 58 % | 128.5 px | 0.14 | 1.11 | 165 |
| stroke 28 | 59 % → 59 % | 137.4 px | 0.15 | 1.00 | 140 |

Numbers say: wet paint spreads well beyond the stroke.

## Oil · Henry Ward · HW #03 navy contours over wet band — own sheet
own sheet 600 × 600 · Oil 1.00 · 46 px · 15.8 s

![Oil · Henry Ward · HW #03 navy contours over wet band — own sheet](Oil-Henry-Ward-HW-03-navy-contours-over-wet-band-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 77 % → 19 % | 77.6 px | 0.75 | 0.24 | 1346 |
| stroke 2 | 87 % → 22 % | 145.4 px | 0.73 | 0.26 | 1727 |
| stroke 3 | 85 % → 28 % | 150.0 px | 0.64 | 0.33 | 1531 |
| stroke 4 | 86 % → 38 % | 150.5 px | 0.57 | 0.44 | 1464 |
| stroke 5 | 85 % → 42 % | 149.9 px | 0.50 | 0.50 | 1397 |
| stroke 6 | 87 % → 34 % | 153.3 px | 0.53 | 0.39 | 1217 |
| stroke 7 | 87 % → 22 % | 150.0 px | 0.59 | 0.25 | 1181 |
| stroke 8 | 88 % → 9 % | 148.8 px | 0.73 | 0.10 | 1418 |
| stroke 9 | 100 % → 3 % | 104.1 px | 0.74 | 0.03 | 963 |
| stroke 10 | 10 % → 40 % | 39.9 px | 0.53 | 4.15 | 73 |
| stroke 11 | 18 % → 49 % | 69.7 px | 0.50 | 2.68 | 91 |
| stroke 12 | 22 % → 43 % | 78.3 px | 0.49 | 1.96 | 98 |
| stroke 13 | 26 % → 41 % | 88.6 px | 0.53 | 1.59 | 112 |
| stroke 14 | 15 % → 32 % | 48.7 px | 0.75 | 2.16 | 48 |
| stroke 15 | 19 % → 31 % | 67.1 px | 0.74 | 1.68 | 70 |
| stroke 16 | 27 % → 28 % | 61.9 px | 0.58 | 1.04 | 262 |
| stroke 17 | 32 % → 32 % | 82.9 px | 0.58 | 1.00 | 184 |

Numbers say: wet paint spreads well beyond the stroke.

