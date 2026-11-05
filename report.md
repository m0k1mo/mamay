![All brushes](contact.png)

# Brush Lab — 180 brushes · Nov 5, 2026 at 12:14 AM

Every sheet: 1500 × 600, ten strokes in a 5 × 2 grid — 1. light line · 2. heavy line · 3. pressure swell · 4. fast wave · 5. slow wave · 6. spiral · 7. loop · 8. tilted · 9. over the wet one · 10. long, no reload (cell 8 holds «tilted» and «over the wet one» crossed). The CPU reference of Mamay's paint engine; the wet layer settles 20 s at the end.

Columns: **covered** = share of the cell with paint right after the stroke → after settling; **width** = painted area of the stroke ÷ its length (px); **dark** = mean darkness of the painted pixels above the paper's own grain (0 = paper, 1 = black); **spread** = how far wet paint went beyond the stroke (1.0 = stayed); **ms** = the stroke on the CPU; long stroke: paint in each quarter of its length (it should run out: wet → streaks → dry tail).

## Ink Line
Ink · 12 px · 32.0 s

![Ink Line](Ink-Line.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 1 % → 4 % | 4.3 px | 0.55 | 2.45 | 108 |
| heavy line | 5 % → 6 % | 15.7 px | 0.68 | 1.14 | 74 |
| pressure swell | 3 % → 4 % | 11.3 px | 0.64 | 1.40 | 46 |
| fast wave | 10 % → 11 % | 11.2 px | 0.59 | 1.11 | 207 |
| slow wave | 8 % → 10 % | 9.6 px | 0.57 | 1.16 | 114 |
| spiral | 14 % → 15 % | 8.9 px | 0.49 | 1.07 | 225 |
| loop | 8 % → 9 % | 10.6 px | 0.61 | 1.15 | 152 |
| tilted | 5 % → 5 % | 14.3 px | 0.64 | 1.05 | 69 |
| over the wet one | 10 % → 11 % | 12.5 px | 0.64 | 1.15 | 65 |
| long, no reload | 18 % → 17 % | 8.1 px | 0.47 | 0.96 | 456 | quarters: 0.22 → 0.09 → 0.04 → 0.02

Numbers say: light vs heavy: width 4.3 → 15.7 px, dark 0.55 → 0.68; wet paint spreads well beyond the stroke.

## Dense Ink
Ink · 14 px · 32.6 s

![Dense Ink](Dense-Ink.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 5 % → 7 % | 15.2 px | 0.72 | 1.27 | 134 |
| heavy line | 7 % → 7 % | 19.1 px | 0.73 | 1.09 | 89 |
| pressure swell | 5 % → 6 % | 17.9 px | 0.72 | 1.18 | 59 |
| fast wave | 13 % → 13 % | 15.2 px | 0.69 | 1.01 | 207 |
| slow wave | 12 % → 12 % | 13.5 px | 0.67 | 1.04 | 170 |
| spiral | 18 % → 15 % | 12.2 px | 0.65 | 0.80 | 292 |
| loop | 11 % → 12 % | 14.8 px | 0.69 | 1.08 | 189 |
| tilted | 5 % → 6 % | 14.5 px | 0.72 | 1.07 | 85 |
| over the wet one | 12 % → 13 % | 17.7 px | 0.72 | 1.12 | 80 |
| long, no reload | 23 % → 15 % | 10.1 px | 0.64 | 0.66 | 520 | quarters: 0.30 → 0.12 → 0.04 → 0.02

Numbers say: light vs heavy: width 15.2 → 19.1 px, dark 0.72 → 0.73.

## Transparent Wash
Watercolor · 22 px · 33.3 s

![Transparent Wash](Transparent-Wash.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 2 % → 5 % | 6.9 px | 0.27 | 2.26 | 102 |
| heavy line | 7 % → 9 % | 20.4 px | 0.27 | 1.23 | 72 |
| pressure swell | 4 % → 6 % | 15.2 px | 0.28 | 1.54 | 43 |
| fast wave | 14 % → 16 % | 16.1 px | 0.20 | 1.17 | 204 |
| slow wave | 12 % → 15 % | 13.7 px | 0.21 | 1.28 | 186 |
| spiral | 18 % → 22 % | 11.9 px | 0.16 | 1.22 | 211 |
| loop | 11 % → 13 % | 14.5 px | 0.22 | 1.20 | 128 |
| tilted | 8 % → 8 % | 21.1 px | 0.24 | 1.06 | 80 |
| over the wet one | 13 % → 16 % | 16.4 px | 0.24 | 1.19 | 67 |
| long, no reload | 26 % → 32 % | 11.6 px | 0.13 | 1.22 | 440 | quarters: 0.11 → 0.04 → 0.02 → 0.01

Numbers say: light vs heavy: width 6.9 → 20.4 px, dark 0.27 → 0.27; wet paint spreads well beyond the stroke.

## Dry Brush
Gouache · 24 px · 30.6 s

![Dry Brush](Dry-Brush.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 5 % → 1 % | 13.8 px | 0.65 | 0.11 | 67 |
| heavy line | 6 % → 0 % | 18.4 px | 0.65 | 0.02 | 179 |
| pressure swell | 5 % → 0 % | 18.1 px | 0.65 | 0.09 | 128 |
| fast wave | 6 % → 1 % | 6.9 px | 0.65 | 0.08 | 201 |
| slow wave | 7 % → 0 % | 7.8 px | 0.65 | 0.07 | 411 |
| spiral | 7 % → 1 % | 4.4 px | 0.65 | 0.08 | 378 |
| loop | 9 % → 0 % | 12.2 px | 0.65 | 0.05 | 200 |
| tilted | 4 % → 3 % | 10.3 px | 0.65 | 0.89 | 97 |
| over the wet one | 9 % → 1 % | 14.3 px | 0.65 | 0.12 | 82 |
| long, no reload | 6 % → 1 % | 2.7 px | 0.65 | 0.15 | 451 | quarters: 0.12 → 0.00 → 0.00 → 0.00

Numbers say: light vs heavy: width 13.8 → 18.4 px, dark 0.65 → 0.65.

## Wax Crayon
Wax · 8 px · 13.9 s

![Wax Crayon](Wax-Crayon.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 1 % → 1 % | 2.5 px | 0.71 | 1.00 | 24 |
| heavy line | 1 % → 1 % | 3.9 px | 0.69 | 1.00 | 40 |
| pressure swell | 1 % → 1 % | 3.3 px | 0.70 | 1.00 | 26 |
| fast wave | 3 % → 3 % | 3.5 px | 0.69 | 1.00 | 90 |
| slow wave | 3 % → 3 % | 3.4 px | 0.70 | 1.00 | 94 |
| spiral | 5 % → 5 % | 3.3 px | 0.70 | 1.00 | 87 |
| loop | 3 % → 3 % | 3.3 px | 0.70 | 1.00 | 47 |
| tilted | 2 % → 2 % | 5.6 px | 0.68 | 1.00 | 54 |
| over the wet one | 3 % → 3 % | 3.6 px | 0.68 | 1.00 | 22 |
| long, no reload | 7 % → 7 % | 3.3 px | 0.70 | 1.00 | 140 | quarters: 0.06 → 0.06 → 0.06 → 0.06

Numbers say: light vs heavy: width 2.5 → 3.9 px, dark 0.71 → 0.69; the long stroke does not run out of paint.

## Oil Pastel
Wax · 12 px · 14.4 s

![Oil Pastel](Oil-Pastel.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 1 % → 1 % | 4.0 px | 0.68 | 1.00 | 42 |
| heavy line | 2 % → 2 % | 6.5 px | 0.68 | 1.00 | 68 |
| pressure swell | 2 % → 2 % | 5.7 px | 0.69 | 1.00 | 45 |
| fast wave | 5 % → 5 % | 5.7 px | 0.68 | 1.00 | 123 |
| slow wave | 5 % → 5 % | 5.5 px | 0.68 | 1.00 | 99 |
| spiral | 8 % → 8 % | 5.5 px | 0.68 | 1.00 | 372 |
| loop | 4 % → 4 % | 5.6 px | 0.68 | 1.00 | 104 |
| tilted | 2 % → 2 % | 6.8 px | 0.68 | 1.00 | 58 |
| over the wet one | 5 % → 5 % | 5.8 px | 0.68 | 1.00 | 45 |
| long, no reload | 13 % → 13 % | 5.6 px | 0.68 | 1.00 | 242 | quarters: 0.10 → 0.09 → 0.10 → 0.10

Numbers say: light vs heavy: width 4.0 → 6.5 px, dark 0.68 → 0.68; the long stroke does not run out of paint.

## Charcoal
Charcoal · 5 px · 12.4 s

![Charcoal](Charcoal.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 1 % → 1 % | 2.0 px | 0.74 | 1.00 | 40 |
| heavy line | 1 % → 1 % | 3.0 px | 0.74 | 1.00 | 23 |
| pressure swell | 1 % → 1 % | 2.7 px | 0.74 | 1.00 | 15 |
| fast wave | 2 % → 2 % | 2.7 px | 0.73 | 1.00 | 66 |
| slow wave | 2 % → 2 % | 2.6 px | 0.74 | 1.00 | 36 |
| spiral | 4 % → 4 % | 2.5 px | 0.74 | 1.00 | 73 |
| loop | 2 % → 2 % | 2.6 px | 0.74 | 1.00 | 32 |
| tilted | 2 % → 2 % | 4.3 px | 0.72 | 1.00 | 30 |
| over the wet one | 2 % → 2 % | 2.4 px | 0.72 | 1.00 | 17 |
| long, no reload | 6 % → 6 % | 2.7 px | 0.73 | 1.00 | 109 | quarters: 0.05 → 0.05 → 0.05 → 0.05

Numbers say: light vs heavy: width 2.0 → 3.0 px, dark 0.74 → 0.74; the long stroke does not run out of paint.

## Impasto
Heavy acrylic · 22 px · 18.8 s

![Impasto](Impasto.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 8 % → 8 % | 24.1 px | 0.72 | 0.93 | 90 |
| heavy line | 10 % → 9 % | 28.8 px | 0.70 | 0.94 | 153 |
| pressure swell | 7 % → 7 % | 28.1 px | 0.72 | 0.94 | 88 |
| fast wave | 20 % → 13 % | 23.4 px | 0.71 | 0.64 | 275 |
| slow wave | 21 % → 14 % | 24.5 px | 0.71 | 0.66 | 387 |
| spiral | 30 % → 14 % | 19.9 px | 0.71 | 0.46 | 349 |
| loop | 18 % → 14 % | 23.9 px | 0.71 | 0.77 | 163 |
| tilted | 8 % → 8 % | 21.7 px | 0.70 | 1.00 | 134 |
| over the wet one | 17 % → 15 % | 25.4 px | 0.70 | 0.91 | 114 |
| long, no reload | 33 % → 14 % | 14.9 px | 0.71 | 0.42 | 608 | quarters: 0.38 → 0.21 → 0.10 → 0.03

Numbers say: light vs heavy: width 24.1 → 28.8 px, dark 0.72 → 0.70.

## Oil Round
Oil · 18 px · 19.7 s

![Oil Round](Oil-Round.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 2 % → 2 % | 7.2 px | 0.75 | 1.00 | 65 |
| heavy line | 7 % → 7 % | 19.3 px | 0.73 | 1.00 | 134 |
| pressure swell | 4 % → 4 % | 13.7 px | 0.72 | 1.00 | 75 |
| fast wave | 11 % → 11 % | 12.8 px | 0.65 | 1.00 | 162 |
| slow wave | 8 % → 8 % | 9.0 px | 0.57 | 1.00 | 181 |
| spiral | 10 % → 10 % | 6.6 px | 0.50 | 1.00 | 271 |
| loop | 6 % → 6 % | 7.2 px | 0.45 | 1.00 | 144 |
| tilted | 4 % → 4 % | 10.1 px | 0.52 | 1.00 | 87 |
| over the wet one | 6 % → 6 % | 7.6 px | 0.52 | 1.00 | 76 |
| long, no reload | 15 % → 15 % | 6.9 px | 0.42 | 1.00 | 382 | quarters: 0.09 → 0.08 → 0.07 → 0.06

Numbers say: light vs heavy: width 7.2 → 19.3 px, dark 0.75 → 0.73.

## Palette Knife
Oil · 20 px · 18.4 s

![Palette Knife](Palette-Knife.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 8 % → 8 % | 21.9 px | 0.67 | 1.00 | 16 |
| heavy line | 8 % → 8 % | 22.5 px | 0.74 | 1.00 | 17 |
| pressure swell | 6 % → 6 % | 22.3 px | 0.74 | 1.00 | 9 |
| fast wave | 16 % → 16 % | 18.9 px | 0.50 | 1.00 | 42 |
| slow wave | 17 % → 17 % | 19.9 px | 0.43 | 1.00 | 47 |
| spiral | 17 % → 17 % | 11.3 px | 0.46 | 1.00 | 46 |
| loop | 16 % → 16 % | 21.0 px | 0.59 | 1.00 | 24 |
| tilted | 5 % → 5 % | 15.0 px | 0.72 | 1.00 | 11 |
| over the wet one | 13 % → 13 % | 21.0 px | 0.72 | 1.00 | 14 |
| long, no reload | 16 % → 16 % | 7.2 px | 0.49 | 1.00 | 67 | quarters: 0.29 → 0.05 → 0.00 → 0.00

Numbers say: light vs heavy: width 21.9 → 22.5 px, dark 0.67 → 0.74; pressure barely changes the width.

## Water
Watercolor · 20 px · 42.2 s · over bands of wet oil paint and oil pastel in turn (it works on paint already there: look at what it does to the bands; covered counts the bands too)

![Water](Water.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 25 % → 27 % | 73.8 px | 0.80 | 1.06 | 27 |
| heavy line | 24 % → 25 % | 69.8 px | 0.81 | 1.04 | 102 |
| pressure swell | 24 % → 25 % | 89.6 px | 0.81 | 1.03 | 65 |
| fast wave | 24 % → 26 % | 27.7 px | 0.81 | 1.07 | 186 |
| slow wave | 24 % → 25 % | 27.8 px | 0.81 | 1.06 | 158 |
| spiral | 24 % → 26 % | 15.9 px | 0.81 | 1.07 | 192 |
| loop | 24 % → 25 % | 31.1 px | 0.81 | 1.03 | 110 |
| tilted | 24 % → 24 % | 67.0 px | 0.81 | 1.00 | 66 |
| over the wet one | 24 % → 25 % | 0.0 px | 0.81 | 1.06 | 45 |
| long, no reload | 24 % → 26 % | 10.7 px | 0.81 | 1.08 | 328 | quarters: 0.21 → 0.27 → 0.18 → 0.27

Numbers say: light vs heavy: width 73.8 → 69.8 px, dark 0.80 → 0.81; pressure barely changes the width; the long stroke does not run out of paint.

## Blender
Pastel · 16 px · 27.0 s · over bands of wet oil paint and oil pastel in turn (it works on paint already there: look at what it does to the bands; covered counts the bands too)

![Blender](Blender.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 24 % → 24 % | 70.7 px | 0.81 | 1.00 | 21 |
| heavy line | 25 % → 25 % | 72.1 px | 0.80 | 1.00 | 49 |
| pressure swell | 24 % → 24 % | 91.3 px | 0.81 | 1.00 | 30 |
| fast wave | 26 % → 26 % | 30.0 px | 0.79 | 1.00 | 91 |
| slow wave | 26 % → 26 % | 29.9 px | 0.80 | 1.00 | 149 |
| spiral | 28 % → 28 % | 18.7 px | 0.77 | 1.00 | 167 |
| loop | 25 % → 25 % | 33.0 px | 0.80 | 1.00 | 117 |
| tilted | 25 % → 25 % | 70.1 px | 0.79 | 1.00 | 53 |
| over the wet one | 26 % → 26 % | 1.8 px | 0.79 | 1.00 | 40 |
| long, no reload | 30 % → 30 % | 13.7 px | 0.76 | 1.00 | 335 | quarters: 0.20 → 0.28 → 0.23 → 0.30

Numbers say: light vs heavy: width 70.7 → 72.1 px, dark 0.81 → 0.80; pressure barely changes the width; the long stroke does not run out of paint.

## Eraser
Eraser · 16 px · 27.0 s · over bands of wet oil paint and oil pastel in turn (it works on paint already there: look at what it does to the bands; covered counts the bands too)

![Eraser](Eraser.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 24 % → 24 % | 69.6 px | 0.82 | 1.00 | 29 |
| heavy line | 23 % → 23 % | 67.9 px | 0.82 | 1.00 | 58 |
| pressure swell | 23 % → 23 % | 87.3 px | 0.82 | 1.00 | 33 |
| fast wave | 22 % → 22 % | 25.7 px | 0.82 | 1.00 | 158 |
| slow wave | 22 % → 22 % | 25.7 px | 0.82 | 1.00 | 110 |
| spiral | 22 % → 22 % | 14.4 px | 0.82 | 1.00 | 193 |
| loop | 22 % → 22 % | 28.6 px | 0.82 | 1.00 | 113 |
| tilted | 23 % → 23 % | 65.1 px | 0.82 | 1.00 | 73 |
| over the wet one | 23 % → 23 % | 0.0 px | 0.82 | 1.00 | 59 |
| long, no reload | 20 % → 20 % | 8.9 px | 0.82 | 1.00 | 485 | quarters: 0.15 → 0.20 → 0.15 → 0.20

Numbers say: light vs heavy: width 69.6 → 67.9 px, dark 0.82 → 0.82; pressure barely changes the width; the long stroke does not run out of paint.

## Fan
Gouache · 30 px · 34.9 s

![Fan](Fan.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 9 % → 3 % | 25.6 px | 0.63 | 0.37 | 32 |
| heavy line | 11 % → 4 % | 30.9 px | 0.63 | 0.39 | 69 |
| pressure swell | 8 % → 5 % | 31.7 px | 0.63 | 0.55 | 37 |
| fast wave | 17 % → 5 % | 20.2 px | 0.63 | 0.26 | 137 |
| slow wave | 18 % → 5 % | 21.0 px | 0.63 | 0.25 | 351 |
| spiral | 24 % → 5 % | 15.5 px | 0.63 | 0.19 | 317 |
| loop | 17 % → 5 % | 22.7 px | 0.63 | 0.28 | 109 |
| tilted | 5 % → 6 % | 15.0 px | 0.63 | 1.05 | 60 |
| over the wet one | 16 % → 8 % | 29.7 px | 0.63 | 0.49 | 52 |
| long, no reload | 22 % → 5 % | 9.9 px | 0.63 | 0.22 | 293 | quarters: 0.29 → 0.07 → 0.01 → 0.00

Numbers say: light vs heavy: width 25.6 → 30.9 px, dark 0.63 → 0.63.

## Sponge
Gouache · 30 px · 35.4 s

![Sponge](Sponge.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 4 % → 0 % | 11.3 px | 0.62 | 0.12 | 56 |
| heavy line | 12 % → 2 % | 35.4 px | 0.62 | 0.14 | 95 |
| pressure swell | 7 % → 2 % | 27.9 px | 0.62 | 0.28 | 92 |
| fast wave | 20 % → 4 % | 23.2 px | 0.62 | 0.19 | 276 |
| slow wave | 21 % → 4 % | 23.8 px | 0.62 | 0.18 | 313 |
| spiral | 28 % → 4 % | 18.3 px | 0.62 | 0.14 | 274 |
| loop | 18 % → 5 % | 23.0 px | 0.62 | 0.29 | 134 |
| tilted | 7 % → 7 % | 18.2 px | 0.62 | 1.04 | 129 |
| over the wet one | 16 % → 6 % | 27.8 px | 0.62 | 0.37 | 61 |
| long, no reload | 29 % → 5 % | 12.9 px | 0.62 | 0.17 | 390 | quarters: 0.29 → 0.13 → 0.07 → 0.04

Numbers say: light vs heavy: width 11.3 → 35.4 px, dark 0.62 → 0.62.

## Ink — sumi brush
Watercolour 1.00 · 22 px · 36.6 s

![Ink — sumi brush](Ink-sumi-brush.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 8 % → 9 % | 23.6 px | 0.87 | 1.13 | 84 |
| heavy line | 13 % → 13 % | 37.9 px | 0.86 | 1.01 | 108 |
| pressure swell | 9 % → 9 % | 33.5 px | 0.87 | 1.05 | 116 |
| fast wave | 28 % → 28 % | 32.1 px | 0.81 | 1.00 | 331 |
| slow wave | 26 % → 26 % | 29.8 px | 0.82 | 1.02 | 358 |
| spiral | 38 % → 37 % | 25.2 px | 0.74 | 0.96 | 408 |
| loop | 22 % → 22 % | 28.5 px | 0.85 | 1.02 | 180 |
| tilted | 9 % → 9 % | 25.3 px | 0.86 | 1.01 | 93 |
| over the wet one | 20 % → 21 % | 30.5 px | 0.86 | 1.03 | 93 |
| long, no reload | 45 % → 40 % | 20.0 px | 0.70 | 0.89 | 554 | quarters: 0.55 → 0.40 → 0.23 → 0.14

Numbers say: light vs heavy: width 23.6 → 37.9 px, dark 0.87 → 0.86.

## Ink — wash
Watercolour 1.00 · 40 px · 43.4 s

![Ink — wash](Ink-wash.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 13 % → 13 % | 37.3 px | 0.42 | 1.02 | 93 |
| heavy line | 19 % → 19 % | 55.2 px | 0.35 | 1.01 | 124 |
| pressure swell | 13 % → 13 % | 48.2 px | 0.41 | 1.02 | 98 |
| fast wave | 41 % → 42 % | 47.8 px | 0.32 | 1.02 | 241 |
| slow wave | 39 % → 40 % | 45.3 px | 0.42 | 1.02 | 546 |
| spiral | 60 % → 62 % | 39.7 px | 0.33 | 1.02 | 462 |
| loop | 34 % → 34 % | 43.8 px | 0.39 | 1.01 | 207 |
| tilted | 15 % → 15 % | 40.7 px | 0.43 | 1.01 | 228 |
| over the wet one | 30 % → 31 % | 43.4 px | 0.43 | 1.02 | 157 |
| long, no reload | 71 % → 75 % | 32.0 px | 0.31 | 1.05 | 624 | quarters: 0.40 → 0.29 → 0.19 → 0.12

Numbers say: light vs heavy: width 37.3 → 55.2 px, dark 0.42 → 0.35.

## Ink — dry brush
Ink 1.00 · 30 px · 33.5 s

![Ink — dry brush](Ink-dry-brush.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 6 % → 5 % | 17.8 px | 0.83 | 0.86 | 105 |
| heavy line | 7 % → 6 % | 19.2 px | 0.82 | 0.88 | 213 |
| pressure swell | 5 % → 5 % | 18.7 px | 0.83 | 0.95 | 134 |
| fast wave | 12 % → 8 % | 13.7 px | 0.80 | 0.67 | 299 |
| slow wave | 12 % → 7 % | 13.6 px | 0.81 | 0.59 | 465 |
| spiral | 19 % → 9 % | 12.5 px | 0.79 | 0.45 | 801 |
| loop | 11 % → 8 % | 14.4 px | 0.79 | 0.72 | 419 |
| tilted | 6 % → 6 % | 16.0 px | 0.81 | 1.07 | 145 |
| over the wet one | 12 % → 12 % | 18.4 px | 0.81 | 0.95 | 136 |
| long, no reload | 19 % → 9 % | 8.7 px | 0.78 | 0.45 | 1468 | quarters: 0.26 → 0.09 → 0.03 → 0.01

Numbers say: light vs heavy: width 17.8 → 19.2 px, dark 0.83 → 0.82; pressure barely changes the width.

## Ink — nib
Watercolour 1.00 · 5 px · 31.4 s

![Ink — nib](Ink-nib.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 2 % → 5 % | 5.5 px | 0.89 | 2.46 | 47 |
| heavy line | 2 % → 5 % | 6.4 px | 0.89 | 2.34 | 32 |
| pressure swell | 2 % → 4 % | 6.2 px | 0.89 | 2.53 | 24 |
| fast wave | 5 % → 8 % | 5.9 px | 0.89 | 1.63 | 74 |
| slow wave | 5 % → 8 % | 5.7 px | 0.89 | 1.70 | 161 |
| spiral | 8 % → 11 % | 5.0 px | 0.87 | 1.41 | 231 |
| loop | 4 % → 8 % | 5.7 px | 0.89 | 1.74 | 127 |
| tilted | 4 % → 4 % | 10.3 px | 0.89 | 1.02 | 43 |
| over the wet one | 6 % → 9 % | 6.1 px | 0.89 | 1.61 | 47 |
| long, no reload | 9 % → 12 % | 4.2 px | 0.85 | 1.30 | 286 | quarters: 0.24 → 0.11 → 0.07 → 0.05

Numbers say: light vs heavy: width 5.5 → 6.4 px, dark 0.89 → 0.89; wet paint spreads well beyond the stroke.

## 0.45 · Dry brush
Gouache 0.91 · Ink 0.07 · 34 px · 34.3 s

![0.45 · Dry brush](0-45-Dry-brush.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 9 % → 4 % | 26.8 px | 0.68 | 0.49 | 190 |
| heavy line | 10 % → 4 % | 28.6 px | 0.68 | 0.43 | 123 |
| pressure swell | 7 % → 5 % | 27.9 px | 0.68 | 0.72 | 107 |
| fast wave | 17 % → 6 % | 19.7 px | 0.68 | 0.34 | 301 |
| slow wave | 20 % → 7 % | 22.8 px | 0.68 | 0.37 | 549 |
| spiral | 31 % → 7 % | 20.6 px | 0.68 | 0.21 | 600 |
| loop | 18 % → 8 % | 22.7 px | 0.68 | 0.44 | 298 |
| tilted | 8 % → 8 % | 22.5 px | 0.68 | 1.02 | 166 |
| over the wet one | 17 % → 12 % | 24.5 px | 0.68 | 0.68 | 167 |
| long, no reload | 31 % → 9 % | 14.1 px | 0.68 | 0.27 | 1048 | quarters: 0.35 → 0.26 → 0.16 → 0.13

Numbers say: light vs heavy: width 26.8 → 28.6 px, dark 0.68 → 0.68; pressure barely changes the width.

## Dry pastel
Pastel 1.00 · 26 px · 10.8 s

![Dry pastel](Dry-pastel.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 3 % → 3 % | 8.3 px | 0.38 | 1.00 | 45 |
| heavy line | 5 % → 5 % | 13.2 px | 0.39 | 1.00 | 36 |
| pressure swell | 3 % → 3 % | 11.7 px | 0.38 | 1.00 | 26 |
| fast wave | 10 % → 10 % | 11.8 px | 0.39 | 1.00 | 90 |
| slow wave | 10 % → 10 % | 11.3 px | 0.39 | 1.00 | 217 |
| spiral | 15 % → 15 % | 9.6 px | 0.38 | 1.00 | 199 |
| loop | 7 % → 7 % | 9.4 px | 0.39 | 1.00 | 82 |
| tilted | 3 % → 3 % | 8.3 px | 0.38 | 1.00 | 45 |
| over the wet one | 7 % → 7 % | 11.1 px | 0.38 | 1.00 | 42 |
| long, no reload | 18 % → 18 % | 8.2 px | 0.39 | 1.00 | 245 | quarters: 0.08 → 0.08 → 0.08 → 0.07

Numbers say: light vs heavy: width 8.3 → 13.2 px, dark 0.38 → 0.39; the long stroke does not run out of paint.

## 0.45 · Charcoal
Charcoal 1.00 · 18 px · 12.8 s

![0.45 · Charcoal](0-45-Charcoal.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 2 % → 2 % | 6.5 px | 0.80 | 1.00 | 24 |
| heavy line | 3 % → 3 % | 9.2 px | 0.80 | 1.00 | 21 |
| pressure swell | 2 % → 2 % | 8.8 px | 0.80 | 1.00 | 15 |
| fast wave | 7 % → 7 % | 7.8 px | 0.80 | 1.00 | 52 |
| slow wave | 7 % → 7 % | 8.0 px | 0.80 | 1.00 | 71 |
| spiral | 12 % → 12 % | 7.9 px | 0.80 | 1.00 | 94 |
| loop | 6 % → 6 % | 8.1 px | 0.80 | 1.00 | 48 |
| tilted | 3 % → 3 % | 7.5 px | 0.80 | 1.00 | 27 |
| over the wet one | 6 % → 6 % | 7.8 px | 0.80 | 1.00 | 21 |
| long, no reload | 17 % → 17 % | 7.8 px | 0.80 | 1.00 | 151 | quarters: 0.15 → 0.16 → 0.15 → 0.16

Numbers say: light vs heavy: width 6.5 → 9.2 px, dark 0.80 → 0.80; the long stroke does not run out of paint.

## Watercolour — wash
Watercolour 1.00 · 50 px · 54.7 s

![Watercolour — wash](Watercolour-wash.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 16 % → 16 % | 45.5 px | 0.22 | 1.01 | 170 |
| heavy line | 22 % → 22 % | 64.9 px | 0.19 | 1.00 | 251 |
| pressure swell | 15 % → 15 % | 56.1 px | 0.22 | 1.01 | 112 |
| fast wave | 48 % → 49 % | 55.5 px | 0.19 | 1.01 | 416 |
| slow wave | 46 % → 46 % | 53.3 px | 0.24 | 1.00 | 597 |
| spiral | 66 % → 66 % | 43.7 px | 0.21 | 1.00 | 635 |
| loop | 40 % → 40 % | 51.4 px | 0.22 | 1.00 | 289 |
| tilted | 18 % → 18 % | 49.7 px | 0.23 | 1.00 | 225 |
| over the wet one | 36 % → 36 % | 49.6 px | 0.23 | 1.01 | 150 |
| long, no reload | 84 % → 84 % | 37.7 px | 0.20 | 1.00 | 1292 | quarters: 0.24 → 0.20 → 0.16 → 0.12

Numbers say: light vs heavy: width 45.5 → 64.9 px, dark 0.22 → 0.19.

## Watercolour — wet-in-wet
Watercolour 1.00 · 44 px · 53.9 s

![Watercolour — wet-in-wet](Watercolour-wet-in-wet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 13 % → 21 % | 37.6 px | 0.32 | 1.62 | 115 |
| heavy line | 19 % → 22 % | 54.2 px | 0.34 | 1.18 | 140 |
| pressure swell | 12 % → 17 % | 46.4 px | 0.35 | 1.34 | 93 |
| fast wave | 42 % → 49 % | 48.0 px | 0.33 | 1.18 | 280 |
| slow wave | 40 % → 48 % | 46.4 px | 0.40 | 1.20 | 759 |
| spiral | 63 % → 69 % | 41.7 px | 0.37 | 1.10 | 573 |
| loop | 34 % → 41 % | 44.5 px | 0.37 | 1.20 | 269 |
| tilted | 15 % → 16 % | 41.4 px | 0.36 | 1.06 | 213 |
| over the wet one | 31 % → 40 % | 44.7 px | 0.36 | 1.30 | 144 |
| long, no reload | 78 % → 87 % | 34.9 px | 0.36 | 1.12 | 835 | quarters: 0.40 → 0.37 → 0.32 → 0.26

Numbers say: light vs heavy: width 37.6 → 54.2 px, dark 0.32 → 0.34; wet paint spreads well beyond the stroke.

## Watercolour — glaze
Watercolour 1.00 · 38 px · 45.6 s

![Watercolour — glaze](Watercolour-glaze.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 13 % → 13 % | 36.6 px | 0.07 | 1.02 | 123 |
| heavy line | 19 % → 19 % | 55.4 px | 0.07 | 1.00 | 125 |
| pressure swell | 13 % → 13 % | 47.0 px | 0.07 | 1.02 | 131 |
| fast wave | 39 % → 40 % | 45.6 px | 0.07 | 1.01 | 459 |
| slow wave | 37 % → 37 % | 42.8 px | 0.07 | 1.01 | 545 |
| spiral | 59 % → 60 % | 38.8 px | 0.06 | 1.01 | 501 |
| loop | 33 % → 33 % | 42.6 px | 0.07 | 1.00 | 264 |
| tilted | 14 % → 14 % | 40.1 px | 0.07 | 1.00 | 204 |
| over the wet one | 30 % → 30 % | 42.3 px | 0.07 | 1.01 | 117 |
| long, no reload | 69 % → 70 % | 30.9 px | 0.06 | 1.01 | 711 | quarters: 0.06 → 0.05 → 0.03 → 0.02

Numbers say: light vs heavy: width 36.6 → 55.4 px, dark 0.07 → 0.07.

## Watercolour — granulating
Watercolour 1.00 · 44 px · 41.5 s

![Watercolour — granulating](Watercolour-granulating.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 14 % → 14 % | 41.4 px | 0.35 | 1.01 | 106 |
| heavy line | 21 % → 21 % | 60.4 px | 0.31 | 1.00 | 112 |
| pressure swell | 14 % → 14 % | 52.2 px | 0.34 | 1.01 | 95 |
| fast wave | 45 % → 45 % | 51.7 px | 0.29 | 1.01 | 309 |
| slow wave | 42 % → 42 % | 48.2 px | 0.35 | 1.01 | 449 |
| spiral | 62 % → 63 % | 41.0 px | 0.30 | 1.01 | 486 |
| loop | 37 % → 37 % | 47.6 px | 0.33 | 1.00 | 254 |
| tilted | 16 % → 16 % | 45.5 px | 0.36 | 1.00 | 156 |
| over the wet one | 33 % → 33 % | 46.2 px | 0.36 | 1.01 | 125 |
| long, no reload | 75 % → 76 % | 33.6 px | 0.29 | 1.01 | 812 | quarters: 0.34 → 0.26 → 0.20 → 0.14

Numbers say: light vs heavy: width 41.4 → 60.4 px, dark 0.35 → 0.31.

## Watercolour — dry brush
Watercolour 1.00 · 36 px · 32.0 s

![Watercolour — dry brush](Watercolour-dry-brush.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 9 % → 10 % | 27.4 px | 0.17 | 1.01 | 129 |
| heavy line | 14 % → 13 % | 39.9 px | 0.15 | 0.92 | 228 |
| pressure swell | 11 % → 11 % | 40.5 px | 0.16 | 0.98 | 109 |
| fast wave | 27 % → 20 % | 30.8 px | 0.13 | 0.73 | 459 |
| slow wave | 24 % → 17 % | 28.0 px | 0.14 | 0.70 | 580 |
| spiral | 34 % → 20 % | 22.3 px | 0.13 | 0.58 | 520 |
| loop | 21 % → 18 % | 27.2 px | 0.14 | 0.86 | 342 |
| tilted | 10 % → 10 % | 28.3 px | 0.16 | 1.00 | 200 |
| over the wet one | 21 % → 20 % | 31.2 px | 0.16 | 0.95 | 156 |
| long, no reload | 36 % → 19 % | 16.0 px | 0.14 | 0.54 | 833 | quarters: 0.09 → 0.03 → 0.01 → 0.00

Numbers say: light vs heavy: width 27.4 → 39.9 px, dark 0.17 → 0.15.

## Gouache
Gouache 1.00 · 30 px · 34.6 s

![Gouache](Gouache.png)

A light paint: laid on a grey sheet (on white it cannot be seen); **dark** = how far it is from the grey either way.

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 8 % → 5 % | 23.3 px | 0.29 | 0.61 | 100 |
| heavy line | 12 % → 5 % | 35.6 px | 0.28 | 0.41 | 122 |
| pressure swell | 10 % → 5 % | 36.2 px | 0.28 | 0.50 | 100 |
| fast wave | 22 % → 6 % | 25.1 px | 0.28 | 0.27 | 321 |
| slow wave | 22 % → 7 % | 25.8 px | 0.28 | 0.30 | 470 |
| spiral | 28 % → 7 % | 18.5 px | 0.28 | 0.23 | 523 |
| loop | 18 % → 7 % | 23.7 px | 0.28 | 0.37 | 311 |
| tilted | 9 % → 9 % | 24.0 px | 0.28 | 1.01 | 113 |
| over the wet one | 19 % → 12 % | 28.7 px | 0.28 | 0.63 | 93 |
| long, no reload | 27 % → 9 % | 12.2 px | 0.28 | 0.31 | 616 | quarters: 0.01 → 0.02 → 0.02 → 0.02

Numbers say: light vs heavy: width 23.3 → 35.6 px, dark 0.29 → 0.28; the long stroke does not run out of paint.

## Oil — alla prima
Oil 0.89 · Oil glaze 0.11 · 30 px · 16.9 s

![Oil — alla prima](Oil-alla-prima.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 9 % → 9 % | 26.1 px | 0.50 | 1.00 | 96 |
| heavy line | 9 % → 9 % | 26.9 px | 0.48 | 1.00 | 137 |
| pressure swell | 8 % → 8 % | 28.7 px | 0.50 | 1.00 | 92 |
| fast wave | 21 % → 21 % | 24.3 px | 0.49 | 1.00 | 317 |
| slow wave | 23 % → 23 % | 26.8 px | 0.50 | 1.00 | 509 |
| spiral | 36 % → 36 % | 23.7 px | 0.49 | 1.00 | 433 |
| loop | 19 % → 19 % | 24.9 px | 0.50 | 1.00 | 200 |
| tilted | 11 % → 11 % | 29.6 px | 0.50 | 1.00 | 115 |
| over the wet one | 20 % → 20 % | 24.9 px | 0.50 | 1.00 | 96 |
| long, no reload | 41 % → 41 % | 18.6 px | 0.49 | 1.00 | 754 | quarters: 0.29 → 0.23 → 0.21 → 0.17

Numbers say: light vs heavy: width 26.1 → 26.9 px, dark 0.50 → 0.48; pressure barely changes the width.

## Oil — impasto
Oil heavy 1.00 · 34 px · 19.9 s

![Oil — impasto](Oil-impasto.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 12 % → 12 % | 33.4 px | 0.23 | 1.00 | 151 |
| heavy line | 12 % → 12 % | 36.3 px | 0.22 | 1.00 | 160 |
| pressure swell | 10 % → 10 % | 35.7 px | 0.24 | 1.00 | 95 |
| fast wave | 27 % → 27 % | 31.6 px | 0.21 | 1.00 | 335 |
| slow wave | 29 % → 29 % | 34.0 px | 0.23 | 1.00 | 511 |
| spiral | 49 % → 49 % | 32.6 px | 0.21 | 1.00 | 551 |
| loop | 25 % → 25 % | 32.5 px | 0.23 | 1.00 | 325 |
| tilted | 12 % → 12 % | 32.7 px | 0.24 | 1.00 | 204 |
| over the wet one | 22 % → 22 % | 29.8 px | 0.24 | 1.00 | 285 |
| long, no reload | 52 % → 52 % | 23.1 px | 0.21 | 1.00 | 1313 | quarters: 0.17 → 0.13 → 0.10 → 0.08

Numbers say: light vs heavy: width 33.4 → 36.3 px, dark 0.23 → 0.22; pressure barely changes the width.

## Oil — glaze
Oil glaze 1.00 · 40 px · 22.3 s

![Oil — glaze](Oil-glaze.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 9 % → 9 % | 27.0 px | 0.50 | 1.00 | 185 |
| heavy line | 13 % → 13 % | 38.3 px | 0.49 | 1.00 | 167 |
| pressure swell | 10 % → 10 % | 36.6 px | 0.50 | 1.00 | 90 |
| fast wave | 29 % → 29 % | 33.5 px | 0.49 | 1.00 | 296 |
| slow wave | 30 % → 30 % | 34.6 px | 0.50 | 1.00 | 542 |
| spiral | 46 % → 46 % | 30.1 px | 0.49 | 1.00 | 700 |
| loop | 24 % → 24 % | 31.4 px | 0.50 | 1.00 | 320 |
| tilted | 11 % → 11 % | 30.4 px | 0.50 | 1.00 | 208 |
| over the wet one | 23 % → 23 % | 32.5 px | 0.50 | 1.00 | 154 |
| long, no reload | 52 % → 52 % | 23.5 px | 0.49 | 1.00 | 847 | quarters: 0.34 → 0.30 → 0.27 → 0.22

Numbers say: light vs heavy: width 27.0 → 38.3 px, dark 0.50 → 0.49.

## Oil — scumble
Oil 1.00 · 36 px · 22.3 s

![Oil — scumble](Oil-scumble.png)

A light paint: laid on a grey sheet (on white it cannot be seen); **dark** = how far it is from the grey either way.

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 10 % → 10 % | 30.1 px | 0.23 | 1.00 | 187 |
| heavy line | 10 % → 10 % | 30.3 px | 0.19 | 1.00 | 199 |
| pressure swell | 8 % → 8 % | 30.7 px | 0.25 | 1.00 | 155 |
| fast wave | 21 % → 21 % | 23.8 px | 0.09 | 1.00 | 538 |
| slow wave | 21 % → 21 % | 24.2 px | 0.19 | 1.00 | 1399 |
| spiral | 37 % → 37 % | 24.4 px | 0.13 | 1.00 | 1332 |
| loop | 19 % → 19 % | 24.9 px | 0.18 | 1.00 | 640 |
| tilted | 10 % → 10 % | 27.9 px | 0.21 | 1.00 | 226 |
| over the wet one | 19 % → 19 % | 23.8 px | 0.21 | 1.00 | 186 |
| long, no reload | 35 % → 35 % | 15.8 px | 0.14 | 1.00 | 1132 | quarters: 0.00 → 0.00 → 0.00 → 0.00

Numbers say: light vs heavy: width 30.1 → 30.3 px, dark 0.23 → 0.19; pressure barely changes the width.

## Acrylic — heavy body
Impasto 0.98 · 30 px · 21.3 s

![Acrylic — heavy body](Acrylic-heavy-body.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 9 % → 8 % | 26.4 px | 0.52 | 0.88 | 399 |
| heavy line | 10 % → 9 % | 28.5 px | 0.52 | 0.88 | 228 |
| pressure swell | 8 % → 7 % | 29.2 px | 0.53 | 0.91 | 109 |
| fast wave | 17 % → 13 % | 20.1 px | 0.52 | 0.74 | 498 |
| slow wave | 20 % → 15 % | 22.8 px | 0.52 | 0.77 | 567 |
| spiral | 28 % → 16 % | 18.8 px | 0.52 | 0.55 | 612 |
| loop | 17 % → 13 % | 21.6 px | 0.52 | 0.79 | 313 |
| tilted | 8 % → 8 % | 22.4 px | 0.53 | 1.00 | 158 |
| over the wet one | 17 % → 15 % | 25.2 px | 0.53 | 0.88 | 149 |
| long, no reload | 30 % → 17 % | 13.3 px | 0.52 | 0.57 | 842 | quarters: 0.24 → 0.15 → 0.11 → 0.08

Numbers say: light vs heavy: width 26.4 → 28.5 px, dark 0.52 → 0.52; pressure barely changes the width.

## Acrylic — fluid
Watercolour 1.00 · 36 px · 40.5 s

![Acrylic — fluid](Acrylic-fluid.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 12 % → 12 % | 34.6 px | 0.24 | 1.01 | 102 |
| heavy line | 18 % → 18 % | 51.8 px | 0.21 | 0.99 | 131 |
| pressure swell | 12 % → 12 % | 44.9 px | 0.23 | 1.01 | 130 |
| fast wave | 38 % → 37 % | 43.4 px | 0.19 | 0.99 | 298 |
| slow wave | 35 % → 35 % | 40.0 px | 0.22 | 1.00 | 462 |
| spiral | 55 % → 53 % | 36.0 px | 0.19 | 0.98 | 518 |
| loop | 31 % → 31 % | 39.9 px | 0.21 | 1.00 | 175 |
| tilted | 12 % → 12 % | 34.0 px | 0.24 | 1.00 | 117 |
| over the wet one | 27 % → 28 % | 42.2 px | 0.24 | 1.02 | 93 |
| long, no reload | 61 % → 58 % | 27.5 px | 0.19 | 0.95 | 707 | quarters: 0.20 → 0.14 → 0.09 → 0.06

Numbers say: light vs heavy: width 34.6 → 51.8 px, dark 0.24 → 0.21.

## Acrylic — palette knife
Impasto 1.00 · 42 px · 24.4 s

![Acrylic — palette knife](Acrylic-palette-knife.png)

A light paint: laid on a grey sheet (on white it cannot be seen); **dark** = how far it is from the grey either way.

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 15 % → 15 % | 44.1 px | 0.39 | 0.98 | 33 |
| heavy line | 15 % → 15 % | 44.3 px | 0.40 | 0.98 | 33 |
| pressure swell | 12 % → 12 % | 43.6 px | 0.42 | 0.99 | 13 |
| fast wave | 36 % → 20 % | 41.9 px | 0.37 | 0.55 | 98 |
| slow wave | 37 % → 21 % | 42.7 px | 0.37 | 0.57 | 202 |
| spiral | 47 % → 18 % | 30.7 px | 0.37 | 0.39 | 172 |
| loop | 32 % → 24 % | 41.3 px | 0.36 | 0.77 | 107 |
| tilted | 12 % → 12 % | 33.7 px | 0.39 | 1.00 | 48 |
| over the wet one | 26 % → 25 % | 39.8 px | 0.39 | 0.97 | 41 |
| long, no reload | 53 % → 21 % | 23.7 px | 0.35 | 0.39 | 312 | quarters: 0.00 → 0.00 → 0.00 → 0.01

Numbers say: light vs heavy: width 44.1 → 44.3 px, dark 0.39 → 0.40; pressure barely changes the width; the long stroke does not run out of paint.

## Finger on oil
Oil 1.00 · 30 px · 17.6 s

![Finger on oil](Finger-on-oil.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 6 % → 6 % | 16.7 px | 0.23 | 1.00 | 78 |
| heavy line | 9 % → 9 % | 27.6 px | 0.28 | 1.00 | 80 |
| pressure swell | 7 % → 7 % | 25.3 px | 0.35 | 1.00 | 47 |
| fast wave | 15 % → 15 % | 17.0 px | 0.12 | 1.00 | 186 |
| slow wave | 16 % → 16 % | 18.6 px | 0.24 | 1.00 | 245 |
| spiral | 28 % → 28 % | 18.2 px | 0.24 | 1.00 | 420 |
| loop | 19 % → 19 % | 24.9 px | 0.27 | 1.00 | 196 |
| tilted | 9 % → 9 % | 26.4 px | 0.28 | 1.00 | 115 |
| over the wet one | 16 % → 16 % | 19.6 px | 0.28 | 1.00 | 47 |
| long, no reload | 36 % → 36 % | 15.9 px | 0.22 | 1.00 | 396 | quarters: 0.12 → 0.11 → 0.07 → 0.04

Numbers say: light vs heavy: width 16.7 → 27.6 px, dark 0.23 → 0.28.

## Palette knife — oil
Oil heavy 0.93 · Impasto 0.07 · 44 px · 21.9 s

![Palette knife — oil](Palette-knife-oil.png)

A light paint: laid on a grey sheet (on white it cannot be seen); **dark** = how far it is from the grey either way.

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 16 % → 14 % | 45.7 px | 0.37 | 0.91 | 39 |
| heavy line | 16 % → 16 % | 46.3 px | 0.38 | 0.98 | 43 |
| pressure swell | 12 % → 12 % | 45.2 px | 0.38 | 0.99 | 15 |
| fast wave | 39 % → 34 % | 44.9 px | 0.35 | 0.89 | 104 |
| slow wave | 39 % → 36 % | 45.4 px | 0.35 | 0.92 | 182 |
| spiral | 62 % → 37 % | 40.7 px | 0.35 | 0.60 | 138 |
| loop | 34 % → 31 % | 43.7 px | 0.36 | 0.92 | 94 |
| tilted | 13 % → 13 % | 36.6 px | 0.37 | 1.00 | 32 |
| over the wet one | 28 % → 27 % | 40.8 px | 0.37 | 0.97 | 45 |
| long, no reload | 74 % → 40 % | 33.0 px | 0.34 | 0.54 | 265 | quarters: 0.00 → 0.00 → 0.01 → 0.01

Numbers say: light vs heavy: width 45.7 → 46.3 px, dark 0.37 → 0.38; pressure barely changes the width; the long stroke does not run out of paint.

## 0.45 · Sponge
Watercolour 0.93 · Ink 0.07 · 46 px · 38.9 s

![0.45 · Sponge](0-45-Sponge.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 27 % → 26 % | 78.9 px | 0.12 | 0.96 | 84 |
| heavy line | 32 % → 29 % | 91.5 px | 0.12 | 0.91 | 113 |
| pressure swell | 24 % → 22 % | 90.7 px | 0.13 | 0.89 | 55 |
| fast wave | 60 % → 55 % | 68.8 px | 0.12 | 0.93 | 261 |
| slow wave | 61 % → 58 % | 70.5 px | 0.17 | 0.95 | 335 |
| spiral | 77 % → 75 % | 50.8 px | 0.16 | 0.97 | 393 |
| loop | 53 % → 50 % | 68.9 px | 0.14 | 0.95 | 284 |
| tilted | 18 % → 18 % | 50.7 px | 0.18 | 1.00 | 115 |
| over the wet one | 45 % → 42 % | 74.3 px | 0.18 | 0.93 | 93 |
| long, no reload | 94 % → 89 % | 42.0 px | 0.17 | 0.95 | 542 | quarters: 0.17 → 0.18 → 0.16 → 0.14

Numbers say: light vs heavy: width 78.9 → 91.5 px, dark 0.12 → 0.12.

## 0.45 · Eraser
Watercolour 1.00 · 30 px · 24.6 s · over bands of wet oil paint and oil pastel in turn (it works on paint already there: look at what it does to the bands; covered counts the bands too)

![0.45 · Eraser](0-45-Eraser.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 24 % → 24 % | 69.2 px | 0.82 | 1.00 | 72 |
| heavy line | 23 % → 23 % | 67.4 px | 0.82 | 1.00 | 61 |
| pressure swell | 23 % → 23 % | 86.8 px | 0.82 | 1.00 | 51 |
| fast wave | 21 % → 21 % | 24.7 px | 0.81 | 1.00 | 164 |
| slow wave | 20 % → 20 % | 23.5 px | 0.82 | 1.00 | 280 |
| spiral | 20 % → 20 % | 13.5 px | 0.79 | 1.00 | 228 |
| loop | 21 % → 21 % | 27.8 px | 0.80 | 1.00 | 136 |
| tilted | 23 % → 23 % | 64.8 px | 0.81 | 1.00 | 63 |
| over the wet one | 22 % → 22 % | 0.0 px | 0.81 | 1.00 | 71 |
| long, no reload | 17 % → 17 % | 7.5 px | 0.79 | 1.00 | 342 | quarters: 0.13 → 0.16 → 0.13 → 0.17

Numbers say: light vs heavy: width 69.2 → 67.4 px, dark 0.82 → 0.82; pressure barely changes the width; the long stroke does not run out of paint.

## Lift wet paint
Watercolour 1.00 · 30 px · 23.2 s · over bands of wet oil paint and oil pastel in turn (it works on paint already there: look at what it does to the bands; covered counts the bands too)

![Lift wet paint](Lift-wet-paint.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 24 % → 24 % | 70.1 px | 0.82 | 1.00 | 33 |
| heavy line | 24 % → 24 % | 69.8 px | 0.82 | 1.00 | 52 |
| pressure swell | 24 % → 24 % | 89.6 px | 0.82 | 1.00 | 41 |
| fast wave | 24 % → 24 % | 27.7 px | 0.82 | 1.00 | 130 |
| slow wave | 24 % → 24 % | 27.7 px | 0.82 | 1.00 | 181 |
| spiral | 24 % → 24 % | 15.9 px | 0.82 | 1.00 | 172 |
| loop | 24 % → 24 % | 31.1 px | 0.82 | 1.00 | 108 |
| tilted | 24 % → 24 % | 66.8 px | 0.82 | 1.00 | 50 |
| over the wet one | 24 % → 24 % | 0.0 px | 0.82 | 1.00 | 42 |
| long, no reload | 24 % → 24 % | 10.7 px | 0.82 | 1.00 | 332 | quarters: 0.18 → 0.24 → 0.17 → 0.24

Numbers say: light vs heavy: width 70.1 → 69.8 px, dark 0.82 → 0.82; pressure barely changes the width; the long stroke does not run out of paint.

## Sgraffito
Watercolour 1.00 · 10 px · 21.7 s · over bands of wet oil paint and oil pastel in turn (it works on paint already there: look at what it does to the bands; covered counts the bands too)

![Sgraffito](Sgraffito.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 24 % → 24 % | 69.9 px | 0.81 | 1.00 | 10 |
| heavy line | 24 % → 24 % | 69.8 px | 0.82 | 1.00 | 10 |
| pressure swell | 24 % → 24 % | 89.6 px | 0.82 | 1.00 | 9 |
| fast wave | 24 % → 24 % | 27.7 px | 0.82 | 1.00 | 42 |
| slow wave | 24 % → 24 % | 27.7 px | 0.82 | 1.00 | 25 |
| spiral | 24 % → 24 % | 15.9 px | 0.82 | 1.00 | 41 |
| loop | 24 % → 24 % | 31.1 px | 0.82 | 1.00 | 25 |
| tilted | 24 % → 24 % | 66.9 px | 0.82 | 1.00 | 9 |
| over the wet one | 24 % → 24 % | 0.0 px | 0.82 | 1.00 | 8 |
| long, no reload | 24 % → 24 % | 10.6 px | 0.82 | 1.00 | 64 | quarters: 0.17 → 0.24 → 0.17 → 0.24

Numbers say: light vs heavy: width 69.9 → 69.8 px, dark 0.81 → 0.82; pressure barely changes the width; the long stroke does not run out of paint.

## Brush Artist · Refs · #01 Henry Ward peach cloud
Gouache 1.00 · 44 px · 33.6 s

![Brush Artist · Refs · #01 Henry Ward peach cloud](Brush-Artist-Refs-01-Henry-Ward-peach-cloud.png)

A light paint: laid on a grey sheet (on white it cannot be seen); **dark** = how far it is from the grey either way.

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 8 % → 0 % | 24.5 px | 0.00 | 0.00 | 125 |
| heavy line | 9 % → 2 % | 25.1 px | 0.32 | 0.27 | 147 |
| pressure swell | 8 % → 4 % | 31.0 px | 0.32 | 0.48 | 126 |
| fast wave | 27 % → 0 % | 30.6 px | 0.00 | 0.00 | 441 |
| slow wave | 22 % → 6 % | 25.6 px | 0.32 | 0.29 | 746 |
| spiral | 38 % → 4 % | 24.9 px | 0.31 | 0.12 | 989 |
| loop | 31 % → 6 % | 39.8 px | 0.32 | 0.19 | 351 |
| tilted | 11 % → 10 % | 30.1 px | 0.32 | 0.97 | 198 |
| over the wet one | 17 % → 3 % | 18.2 px | 0.32 | 0.18 | 186 |
| long, no reload | 45 % → 8 % | 20.2 px | 0.32 | 0.18 | 929 | quarters: 0.02 → 0.02 → 0.03 → 0.03

Numbers say: light vs heavy: width 24.5 → 25.1 px, dark 0.00 → 0.32; pressure barely changes the width; the long stroke does not run out of paint.

## Brush Artist · Refs · #02 Henry Ward cream strokes
Gouache 1.00 · 46 px · 33.4 s

![Brush Artist · Refs · #02 Henry Ward cream strokes](Brush-Artist-Refs-02-Henry-Ward-cream-strokes.png)

A light paint: laid on a grey sheet (on white it cannot be seen); **dark** = how far it is from the grey either way.

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 10 % → 2 % | 29.8 px | 0.40 | 0.17 | 163 |
| heavy line | 10 % → 2 % | 29.4 px | 0.40 | 0.23 | 156 |
| pressure swell | 9 % → 4 % | 34.8 px | 0.41 | 0.42 | 127 |
| fast wave | 25 % → 0 % | 28.8 px | 0.00 | 0.00 | 534 |
| slow wave | 19 % → 6 % | 22.1 px | 0.40 | 0.31 | 646 |
| spiral | 36 % → 4 % | 24.0 px | 0.38 | 0.10 | 888 |
| loop | 29 % → 5 % | 37.8 px | 0.39 | 0.17 | 388 |
| tilted | 11 % → 11 % | 31.3 px | 0.39 | 0.97 | 200 |
| over the wet one | 18 % → 3 % | 18.7 px | 0.39 | 0.15 | 169 |
| long, no reload | 43 % → 10 % | 19.2 px | 0.39 | 0.24 | 1120 | quarters: 0.02 → 0.03 → 0.03 → 0.04

Numbers say: light vs heavy: width 29.8 → 29.4 px, dark 0.40 → 0.40; pressure barely changes the width; the long stroke does not run out of paint.

## Brush Artist · Refs · #03 Henry Ward navy contours
Impasto 1.00 · 22 px · 15.9 s

![Brush Artist · Refs · #03 Henry Ward navy contours](Brush-Artist-Refs-03-Henry-Ward-navy-contours.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 7 % → 6 % | 19.4 px | 0.71 | 0.89 | 76 |
| heavy line | 7 % → 7 % | 20.8 px | 0.70 | 0.91 | 83 |
| pressure swell | 5 % → 5 % | 20.3 px | 0.74 | 0.90 | 71 |
| fast wave | 16 % → 11 % | 18.6 px | 0.73 | 0.70 | 256 |
| slow wave | 17 % → 13 % | 19.6 px | 0.73 | 0.74 | 526 |
| spiral | 25 % → 13 % | 16.3 px | 0.73 | 0.51 | 530 |
| loop | 14 % → 11 % | 18.4 px | 0.73 | 0.80 | 200 |
| tilted | 8 % → 8 % | 22.6 px | 0.72 | 1.00 | 101 |
| over the wet one | 15 % → 13 % | 18.8 px | 0.72 | 0.87 | 99 |
| long, no reload | 30 % → 13 % | 13.3 px | 0.73 | 0.42 | 533 | quarters: 0.31 → 0.25 → 0.18 → 0.11

Numbers say: light vs heavy: width 19.4 → 20.8 px, dark 0.71 → 0.70; pressure barely changes the width.

## Brush Artist · Refs · #04 Henry Ward grey cloud
Gouache 1.00 · 50 px · 40.7 s

![Brush Artist · Refs · #04 Henry Ward grey cloud](Brush-Artist-Refs-04-Henry-Ward-grey-cloud.png)

A light paint: laid on a grey sheet (on white it cannot be seen); **dark** = how far it is from the grey either way.

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 11 % → 2 % | 32.8 px | 0.31 | 0.14 | 249 |
| heavy line | 11 % → 3 % | 32.6 px | 0.31 | 0.27 | 225 |
| pressure swell | 10 % → 4 % | 37.4 px | 0.31 | 0.45 | 137 |
| fast wave | 29 % → 2 % | 33.8 px | 0.31 | 0.06 | 404 |
| slow wave | 20 % → 6 % | 22.6 px | 0.31 | 0.31 | 752 |
| spiral | 43 % → 4 % | 28.6 px | 0.31 | 0.08 | 741 |
| loop | 32 % → 6 % | 40.9 px | 0.31 | 0.19 | 564 |
| tilted | 12 % → 12 % | 34.1 px | 0.31 | 0.98 | 254 |
| over the wet one | 19 % → 3 % | 18.7 px | 0.31 | 0.18 | 202 |
| long, no reload | 47 % → 7 % | 21.3 px | 0.31 | 0.15 | 1833 | quarters: 0.02 → 0.02 → 0.02 → 0.03

Numbers say: light vs heavy: width 32.8 → 32.6 px, dark 0.31 → 0.31; pressure barely changes the width; the long stroke does not run out of paint.

## Brush Artist · Refs · #05 Henry Ward green in rust loops
Impasto 1.00 · 20 px · 17.1 s

![Brush Artist · Refs · #05 Henry Ward green in rust loops](Brush-Artist-Refs-05-Henry-Ward-green-in-rust-loops.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 7 % → 6 % | 18.9 px | 0.55 | 0.91 | 87 |
| heavy line | 7 % → 7 % | 20.7 px | 0.55 | 0.92 | 96 |
| pressure swell | 6 % → 5 % | 20.8 px | 0.56 | 0.91 | 59 |
| fast wave | 16 % → 11 % | 18.7 px | 0.56 | 0.68 | 200 |
| slow wave | 17 % → 12 % | 19.7 px | 0.56 | 0.70 | 292 |
| spiral | 25 % → 12 % | 16.8 px | 0.56 | 0.47 | 395 |
| loop | 14 % → 12 % | 18.8 px | 0.56 | 0.80 | 199 |
| tilted | 8 % → 8 % | 21.8 px | 0.56 | 0.99 | 104 |
| over the wet one | 15 % → 13 % | 18.7 px | 0.56 | 0.88 | 84 |
| long, no reload | 29 % → 12 % | 13.2 px | 0.56 | 0.40 | 513 | quarters: 0.24 → 0.18 → 0.11 → 0.04

Numbers say: light vs heavy: width 18.9 → 20.7 px, dark 0.55 → 0.55; pressure barely changes the width.

## Brush Artist · Refs · #06 Henry Ward scrubbed grey
Gouache 1.00 · 50 px · 41.6 s

![Brush Artist · Refs · #06 Henry Ward scrubbed grey](Brush-Artist-Refs-06-Henry-Ward-scrubbed-grey.png)

A light paint: laid on a grey sheet (on white it cannot be seen); **dark** = how far it is from the grey either way.

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 11 % → 2 % | 32.8 px | 0.32 | 0.14 | 158 |
| heavy line | 11 % → 3 % | 32.6 px | 0.32 | 0.27 | 171 |
| pressure swell | 10 % → 4 % | 37.4 px | 0.32 | 0.45 | 128 |
| fast wave | 29 % → 2 % | 33.8 px | 0.32 | 0.06 | 519 |
| slow wave | 20 % → 6 % | 22.6 px | 0.32 | 0.31 | 932 |
| spiral | 43 % → 4 % | 28.6 px | 0.32 | 0.08 | 1228 |
| loop | 32 % → 6 % | 40.9 px | 0.32 | 0.19 | 606 |
| tilted | 12 % → 12 % | 34.1 px | 0.32 | 0.98 | 283 |
| over the wet one | 19 % → 3 % | 18.7 px | 0.32 | 0.18 | 227 |
| long, no reload | 47 % → 7 % | 21.3 px | 0.32 | 0.15 | 1372 | quarters: 0.03 → 0.02 → 0.02 → 0.04

Numbers say: light vs heavy: width 32.8 → 32.6 px, dark 0.32 → 0.32; pressure barely changes the width; the long stroke does not run out of paint.

## Brush Artist · Refs · #07 Henry Ward blue L + black zigzag
Impasto 1.00 · 34 px · 23.8 s

![Brush Artist · Refs · #07 Henry Ward blue L + black zigzag](Brush-Artist-Refs-07-Henry-Ward-blue-L-black-zigzag.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 11 % → 9 % | 31.5 px | 0.58 | 0.85 | 132 |
| heavy line | 11 % → 10 % | 33.2 px | 0.58 | 0.88 | 122 |
| pressure swell | 9 % → 8 % | 33.5 px | 0.60 | 0.88 | 113 |
| fast wave | 26 % → 19 % | 30.5 px | 0.59 | 0.70 | 423 |
| slow wave | 27 % → 20 % | 31.5 px | 0.59 | 0.74 | 695 |
| spiral | 41 % → 21 % | 27.3 px | 0.59 | 0.52 | 918 |
| loop | 23 % → 18 % | 30.1 px | 0.59 | 0.77 | 452 |
| tilted | 11 % → 11 % | 30.2 px | 0.59 | 1.00 | 209 |
| over the wet one | 22 % → 19 % | 29.9 px | 0.59 | 0.89 | 170 |
| long, no reload | 48 % → 22 % | 21.4 px | 0.59 | 0.46 | 934 | quarters: 0.37 → 0.29 → 0.21 → 0.12

Numbers say: light vs heavy: width 31.5 → 33.2 px, dark 0.58 → 0.58; pressure barely changes the width.

## Brush Artist · Refs · #08 Henry Ward olive bands
Gouache 1.00 · 34 px · 25.9 s

![Brush Artist · Refs · #08 Henry Ward olive bands](Brush-Artist-Refs-08-Henry-Ward-olive-bands.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 4 % → 0 % | 12.4 px | 0.61 | 0.02 | 90 |
| heavy line | 7 % → 0 % | 20.1 px | 0.61 | 0.06 | 222 |
| pressure swell | 5 % → 1 % | 18.9 px | 0.61 | 0.24 | 131 |
| fast wave | 10 % → 0 % | 11.4 px | 0.61 | 0.02 | 311 |
| slow wave | 10 % → 1 % | 11.7 px | 0.61 | 0.05 | 520 |
| spiral | 23 % → 0 % | 15.2 px | 0.00 | 0.00 | 509 |
| loop | 16 % → 0 % | 20.9 px | 0.61 | 0.01 | 270 |
| tilted | 8 % → 7 % | 21.3 px | 0.61 | 0.94 | 156 |
| over the wet one | 11 % → 2 % | 9.6 px | 0.61 | 0.14 | 190 |
| long, no reload | 23 % → 2 % | 10.3 px | 0.61 | 0.08 | 926 | quarters: 0.16 → 0.19 → 0.12 → 0.08

Numbers say: light vs heavy: width 12.4 → 20.1 px, dark 0.61 → 0.61.

## Brush Artist · Refs · #09 Henry Ward white loops
Gouache 1.00 · 46 px · 36.0 s

![Brush Artist · Refs · #09 Henry Ward white loops](Brush-Artist-Refs-09-Henry-Ward-white-loops.png)

A light paint: laid on a grey sheet (on white it cannot be seen); **dark** = how far it is from the grey either way.

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 10 % → 2 % | 29.8 px | 0.42 | 0.17 | 146 |
| heavy line | 10 % → 2 % | 29.4 px | 0.42 | 0.23 | 195 |
| pressure swell | 9 % → 4 % | 34.8 px | 0.44 | 0.42 | 123 |
| fast wave | 25 % → 0 % | 28.8 px | 0.00 | 0.00 | 415 |
| slow wave | 19 % → 6 % | 22.1 px | 0.43 | 0.31 | 755 |
| spiral | 36 % → 4 % | 24.0 px | 0.40 | 0.10 | 910 |
| loop | 29 % → 5 % | 37.8 px | 0.40 | 0.17 | 419 |
| tilted | 11 % → 11 % | 31.3 px | 0.41 | 0.97 | 198 |
| over the wet one | 18 % → 3 % | 18.7 px | 0.41 | 0.15 | 161 |
| long, no reload | 43 % → 10 % | 19.2 px | 0.41 | 0.24 | 1086 | quarters: 0.02 → 0.03 → 0.03 → 0.04

Numbers say: light vs heavy: width 29.8 → 29.4 px, dark 0.42 → 0.42; pressure barely changes the width; the long stroke does not run out of paint.

## Brush Artist · Refs · #10 Henry Ward maroon loops
Impasto 1.00 · 30 px · 18.6 s

![Brush Artist · Refs · #10 Henry Ward maroon loops](Brush-Artist-Refs-10-Henry-Ward-maroon-loops.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 9 % → 8 % | 26.5 px | 0.71 | 0.91 | 94 |
| heavy line | 10 % → 9 % | 28.5 px | 0.72 | 0.92 | 104 |
| pressure swell | 7 % → 7 % | 28.0 px | 0.74 | 0.92 | 69 |
| fast wave | 23 % → 16 % | 26.2 px | 0.73 | 0.72 | 271 |
| slow wave | 24 % → 18 % | 27.5 px | 0.73 | 0.76 | 573 |
| spiral | 36 % → 18 % | 23.6 px | 0.73 | 0.51 | 556 |
| loop | 20 % → 16 % | 25.9 px | 0.73 | 0.82 | 281 |
| tilted | 10 % → 10 % | 28.1 px | 0.73 | 1.00 | 134 |
| over the wet one | 19 % → 17 % | 25.6 px | 0.73 | 0.90 | 106 |
| long, no reload | 42 % → 19 % | 18.9 px | 0.73 | 0.44 | 639 | quarters: 0.42 → 0.36 → 0.29 → 0.21

Numbers say: light vs heavy: width 26.5 → 28.5 px, dark 0.71 → 0.72; pressure barely changes the width.

## Brush Artist · Refs · #11 Henry Ward purple spun balls
Impasto 1.00 · 36 px · 21.2 s

![Brush Artist · Refs · #11 Henry Ward purple spun balls](Brush-Artist-Refs-11-Henry-Ward-purple-spun-balls.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 11 % → 11 % | 33.1 px | 0.73 | 0.92 | 155 |
| heavy line | 12 % → 11 % | 34.4 px | 0.73 | 0.94 | 150 |
| pressure swell | 9 % → 9 % | 35.2 px | 0.75 | 0.94 | 127 |
| fast wave | 27 % → 22 % | 31.4 px | 0.75 | 0.79 | 403 |
| slow wave | 29 % → 23 % | 33.0 px | 0.75 | 0.81 | 745 |
| spiral | 44 % → 25 % | 29.1 px | 0.74 | 0.57 | 664 |
| loop | 24 % → 21 % | 31.0 px | 0.74 | 0.86 | 339 |
| tilted | 11 % → 11 % | 30.4 px | 0.74 | 1.00 | 176 |
| over the wet one | 22 % → 20 % | 30.7 px | 0.74 | 0.92 | 138 |
| long, no reload | 50 % → 25 % | 22.5 px | 0.75 | 0.49 | 816 | quarters: 0.50 → 0.42 → 0.36 → 0.27

Numbers say: light vs heavy: width 33.1 → 34.4 px, dark 0.73 → 0.73; pressure barely changes the width.

## Brush Artist · Refs · #12 Henry Ward black-olive cage
Gouache 1.00 · 28 px · 26.7 s

![Brush Artist · Refs · #12 Henry Ward black-olive cage](Brush-Artist-Refs-12-Henry-Ward-black-olive-cage.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 4 % → 0 % | 11.6 px | 0.00 | 0.00 | 80 |
| heavy line | 6 % → 1 % | 17.6 px | 0.64 | 0.13 | 188 |
| pressure swell | 4 % → 1 % | 15.9 px | 0.64 | 0.30 | 98 |
| fast wave | 10 % → 0 % | 11.8 px | 0.00 | 0.00 | 311 |
| slow wave | 9 % → 1 % | 10.1 px | 0.64 | 0.11 | 481 |
| spiral | 17 % → 0 % | 11.2 px | 0.64 | 0.00 | 414 |
| loop | 13 % → 0 % | 16.9 px | 0.64 | 0.03 | 224 |
| tilted | 7 % → 6 % | 19.1 px | 0.64 | 0.92 | 117 |
| over the wet one | 10 % → 1 % | 8.9 px | 0.64 | 0.12 | 164 |
| long, no reload | 20 % → 2 % | 8.8 px | 0.64 | 0.11 | 1086 | quarters: 0.16 → 0.17 → 0.11 → 0.08

Numbers say: light vs heavy: width 11.6 → 17.6 px, dark 0.00 → 0.64.

## Brush Artist · Refs · #13 Henry Ward blue streaky form
Gouache 1.00 · 50 px · 41.0 s

![Brush Artist · Refs · #13 Henry Ward blue streaky form](Brush-Artist-Refs-13-Henry-Ward-blue-streaky-form.png)

A light paint: laid on a grey sheet (on white it cannot be seen); **dark** = how far it is from the grey either way.

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 11 % → 2 % | 32.8 px | 0.32 | 0.14 | 187 |
| heavy line | 11 % → 3 % | 32.6 px | 0.32 | 0.27 | 221 |
| pressure swell | 10 % → 4 % | 37.4 px | 0.32 | 0.45 | 187 |
| fast wave | 29 % → 2 % | 33.8 px | 0.32 | 0.06 | 582 |
| slow wave | 20 % → 6 % | 22.6 px | 0.32 | 0.31 | 971 |
| spiral | 43 % → 4 % | 28.6 px | 0.32 | 0.08 | 1354 |
| loop | 32 % → 6 % | 40.9 px | 0.32 | 0.19 | 556 |
| tilted | 12 % → 12 % | 34.1 px | 0.32 | 0.98 | 293 |
| over the wet one | 19 % → 3 % | 18.7 px | 0.32 | 0.18 | 205 |
| long, no reload | 47 % → 7 % | 21.3 px | 0.32 | 0.15 | 1315 | quarters: 0.03 → 0.02 → 0.02 → 0.04

Numbers say: light vs heavy: width 32.8 → 32.6 px, dark 0.32 → 0.32; pressure barely changes the width; the long stroke does not run out of paint.

## Brush Artist · Refs · #14 Henry Ward olive totem
Impasto 1.00 · 48 px · 26.8 s

![Brush Artist · Refs · #14 Henry Ward olive totem](Brush-Artist-Refs-14-Henry-Ward-olive-totem.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 15 % → 14 % | 44.4 px | 0.31 | 0.92 | 217 |
| heavy line | 16 % → 15 % | 46.1 px | 0.31 | 0.94 | 284 |
| pressure swell | 12 % → 12 % | 46.6 px | 0.31 | 0.94 | 215 |
| fast wave | 37 % → 29 % | 42.9 px | 0.30 | 0.79 | 619 |
| slow wave | 38 % → 31 % | 44.4 px | 0.30 | 0.81 | 905 |
| spiral | 55 % → 32 % | 36.5 px | 0.30 | 0.57 | 909 |
| loop | 32 % → 28 % | 41.8 px | 0.30 | 0.87 | 416 |
| tilted | 13 % → 13 % | 37.2 px | 0.31 | 1.00 | 295 |
| over the wet one | 28 % → 26 % | 40.1 px | 0.31 | 0.93 | 190 |
| long, no reload | 66 % → 33 % | 29.4 px | 0.30 | 0.51 | 1257 | quarters: 0.24 → 0.18 → 0.11 → 0.04

Numbers say: light vs heavy: width 44.4 → 46.1 px, dark 0.31 → 0.31; pressure barely changes the width.

## Brush Artist · Refs · #15 Ultramarine brush script
Ink 1.00 · 4 px · 29.7 s

![Brush Artist · Refs · #15 Ultramarine brush script](Brush-Artist-Refs-15-Ultramarine-brush-script.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 1 % → 3 % | 2.1 px | 0.54 | 4.15 | 49 |
| heavy line | 6 % → 6 % | 16.8 px | 0.59 | 0.99 | 71 |
| pressure swell | 3 % → 4 % | 11.8 px | 0.64 | 1.17 | 41 |
| fast wave | 9 % → 7 % | 10.5 px | 0.54 | 0.81 | 115 |
| slow wave | 7 % → 7 % | 8.4 px | 0.54 | 0.92 | 122 |
| spiral | 11 % → 7 % | 7.2 px | 0.52 | 0.67 | 251 |
| loop | 7 % → 7 % | 9.1 px | 0.54 | 0.98 | 145 |
| tilted | 3 % → 3 % | 8.4 px | 0.63 | 1.01 | 75 |
| over the wet one | 7 % → 8 % | 11.5 px | 0.63 | 1.06 | 84 |
| long, no reload | 16 % → 8 % | 7.3 px | 0.50 | 0.49 | 631 | quarters: 0.15 → 0.04 → 0.01 → 0.00

Numbers say: light vs heavy: width 2.1 → 16.8 px, dark 0.54 → 0.59; wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #18 Blue oil-stick scribbles
Pastel 1.00 · 10 px · 15.2 s

![Brush Artist · Refs · #18 Blue oil-stick scribbles](Brush-Artist-Refs-18-Blue-oil-stick-scribbles.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 1 % → 1 % | 2.9 px | 0.52 | 1.00 | 55 |
| heavy line | 2 % → 2 % | 5.5 px | 0.53 | 1.00 | 55 |
| pressure swell | 1 % → 1 % | 5.0 px | 0.53 | 1.00 | 42 |
| fast wave | 4 % → 4 % | 4.8 px | 0.53 | 1.00 | 137 |
| slow wave | 4 % → 4 % | 4.4 px | 0.53 | 1.00 | 76 |
| spiral | 7 % → 7 % | 4.5 px | 0.52 | 1.00 | 146 |
| loop | 3 % → 3 % | 4.5 px | 0.52 | 1.00 | 77 |
| tilted | 2 % → 2 % | 4.8 px | 0.53 | 1.00 | 52 |
| over the wet one | 3 % → 3 % | 4.7 px | 0.53 | 1.00 | 41 |
| long, no reload | 10 % → 10 % | 4.4 px | 0.53 | 1.00 | 208 | quarters: 0.06 → 0.06 → 0.06 → 0.06

Numbers say: light vs heavy: width 2.9 → 5.5 px, dark 0.52 → 0.53; the long stroke does not run out of paint.

## Brush Artist · Refs · #20 Orange-red crayon scribble
Pastel 1.00 · 14 px · 15.0 s

![Brush Artist · Refs · #20 Orange-red crayon scribble](Brush-Artist-Refs-20-Orange-red-crayon-scribble.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 1 % → 1 % | 4.0 px | 0.53 | 1.00 | 22 |
| heavy line | 3 % → 3 % | 8.0 px | 0.53 | 1.00 | 37 |
| pressure swell | 2 % → 2 % | 7.6 px | 0.53 | 1.00 | 22 |
| fast wave | 6 % → 6 % | 7.2 px | 0.53 | 1.00 | 140 |
| slow wave | 6 % → 6 % | 6.6 px | 0.53 | 1.00 | 132 |
| spiral | 9 % → 9 % | 6.2 px | 0.53 | 1.00 | 234 |
| loop | 5 % → 5 % | 6.2 px | 0.53 | 1.00 | 95 |
| tilted | 2 % → 2 % | 5.6 px | 0.53 | 1.00 | 45 |
| over the wet one | 4 % → 4 % | 6.6 px | 0.53 | 1.00 | 45 |
| long, no reload | 13 % → 13 % | 5.7 px | 0.53 | 1.00 | 383 | quarters: 0.07 → 0.07 → 0.08 → 0.08

Numbers say: light vs heavy: width 4.0 → 8.0 px, dark 0.53 → 0.53; the long stroke does not run out of paint.

## Brush Artist · Refs · #21 Gritty black contours
Gouache 1.00 · 12 px · 26.0 s

![Brush Artist · Refs · #21 Gritty black contours](Brush-Artist-Refs-21-Gritty-black-contours.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 1 % → 0 % | 3.7 px | 0.81 | 0.04 | 109 |
| heavy line | 2 % → 0 % | 5.7 px | 0.81 | 0.10 | 194 |
| pressure swell | 1 % → 0 % | 5.5 px | 0.00 | 0.00 | 177 |
| fast wave | 4 % → 0 % | 4.2 px | 0.81 | 0.01 | 413 |
| slow wave | 3 % → 0 % | 4.0 px | 0.81 | 0.02 | 287 |
| spiral | 6 % → 0 % | 3.8 px | 0.00 | 0.00 | 531 |
| loop | 5 % → 0 % | 6.1 px | 0.81 | 0.00 | 263 |
| tilted | 2 % → 2 % | 6.7 px | 0.81 | 0.88 | 114 |
| over the wet one | 4 % → 0 % | 4.0 px | 0.81 | 0.11 | 136 |
| long, no reload | 7 % → 0 % | 3.0 px | 0.81 | 0.04 | 693 | quarters: 0.10 → 0.06 → 0.05 → 0.04

Numbers say: light vs heavy: width 3.7 → 5.7 px, dark 0.81 → 0.81.

## Brush Artist · Refs · #22 Bold black brush poster
Ink 1.00 · 20 px · 39.3 s

![Brush Artist · Refs · #22 Bold black brush poster](Brush-Artist-Refs-22-Bold-black-brush-poster.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 3 % → 5 % | 9.2 px | 0.79 | 1.68 | 82 |
| heavy line | 15 % → 15 % | 44.2 px | 0.87 | 0.98 | 130 |
| pressure swell | 8 % → 9 % | 30.9 px | 0.87 | 1.05 | 68 |
| fast wave | 27 % → 26 % | 31.1 px | 0.87 | 0.98 | 190 |
| slow wave | 22 % → 22 % | 25.7 px | 0.87 | 0.99 | 302 |
| spiral | 34 % → 32 % | 22.4 px | 0.87 | 0.94 | 306 |
| loop | 20 % → 20 % | 26.1 px | 0.88 | 1.00 | 165 |
| tilted | 8 % → 8 % | 22.9 px | 0.88 | 1.01 | 122 |
| over the wet one | 19 % → 19 % | 30.0 px | 0.88 | 1.00 | 70 |
| long, no reload | 45 % → 37 % | 20.2 px | 0.86 | 0.82 | 483 | quarters: 0.54 → 0.44 → 0.35 → 0.26

Numbers say: light vs heavy: width 9.2 → 44.2 px, dark 0.79 → 0.87; wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #23 Dry white on orange + black line
Gouache 1.00 · 50 px · 29.7 s

![Brush Artist · Refs · #23 Dry white on orange + black line](Brush-Artist-Refs-23-Dry-white-on-orange-black-line.png)

A light paint: laid on a grey sheet (on white it cannot be seen); **dark** = how far it is from the grey either way.

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 5 % → 0 % | 14.1 px | 0.00 | 0.00 | 116 |
| heavy line | 9 % → 0 % | 27.6 px | 0.42 | 0.01 | 300 |
| pressure swell | 7 % → 0 % | 26.9 px | 0.42 | 0.06 | 249 |
| fast wave | 12 % → 0 % | 13.9 px | 0.00 | 0.00 | 463 |
| slow wave | 14 % → 0 % | 15.9 px | 0.42 | 0.03 | 1116 |
| spiral | 30 % → 0 % | 20.0 px | 0.00 | 0.00 | 869 |
| loop | 20 % → 0 % | 25.9 px | 0.40 | 0.02 | 470 |
| tilted | 9 % → 9 % | 25.5 px | 0.40 | 0.94 | 245 |
| over the wet one | 14 % → 0 % | 13.9 px | 0.40 | 0.01 | 199 |
| long, no reload | 32 % → 1 % | 14.2 px | 0.40 | 0.02 | 1366 | quarters: 0.02 → 0.02 → 0.02 → 0.03

Numbers say: light vs heavy: width 14.1 → 27.6 px, dark 0.00 → 0.42; the long stroke does not run out of paint.

## Brush Artist · Refs · #24 Picasso flat oil
Oil 0.89 · Oil glaze 0.11 · 34 px · 21.8 s

![Brush Artist · Refs · #24 Picasso flat oil](Brush-Artist-Refs-24-Picasso-flat-oil.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 10 % → 10 % | 27.7 px | 0.39 | 1.00 | 188 |
| heavy line | 10 % → 10 % | 30.4 px | 0.39 | 1.00 | 210 |
| pressure swell | 8 % → 8 % | 29.4 px | 0.40 | 1.00 | 151 |
| fast wave | 25 % → 25 % | 29.1 px | 0.40 | 1.00 | 563 |
| slow wave | 26 % → 26 % | 30.3 px | 0.40 | 1.00 | 1140 |
| spiral | 42 % → 42 % | 28.0 px | 0.39 | 1.00 | 1055 |
| loop | 22 % → 22 % | 27.9 px | 0.40 | 1.00 | 507 |
| tilted | 11 % → 11 % | 31.3 px | 0.40 | 1.00 | 212 |
| over the wet one | 21 % → 21 % | 26.9 px | 0.40 | 1.00 | 152 |
| long, no reload | 51 % → 51 % | 22.9 px | 0.39 | 1.00 | 1099 | quarters: 0.25 → 0.23 → 0.21 → 0.20

Numbers say: light vs heavy: width 27.7 → 30.4 px, dark 0.39 → 0.39; pressure barely changes the width.

## Brush Artist · Refs · #25 Yellow heavy flat stroke
Impasto 1.00 · 110 px · 47.5 s

![Brush Artist · Refs · #25 Yellow heavy flat stroke](Brush-Artist-Refs-25-Yellow-heavy-flat-stroke.png)

A light paint: laid on a grey sheet (on white it cannot be seen); **dark** = how far it is from the grey either way.

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 35 % → 36 % | 101.3 px | 0.30 | 1.03 | 798 |
| heavy line | 36 % → 35 % | 105.0 px | 0.31 | 0.97 | 858 |
| pressure swell | 28 % → 29 % | 105.5 px | 0.31 | 1.04 | 420 |
| fast wave | 72 % → 76 % | 83.7 px | 0.31 | 1.05 | 1404 |
| slow wave | 73 % → 72 % | 84.7 px | 0.30 | 0.98 | 3399 |
| spiral | 86 % → 84 % | 56.8 px | 0.29 | 0.98 | 2790 |
| loop | 64 % → 64 % | 83.4 px | 0.31 | 0.99 | 1499 |
| tilted | 26 % → 26 % | 71.4 px | 0.31 | 1.00 | 711 |
| over the wet one | 55 % → 54 % | 83.3 px | 0.31 | 0.97 | 545 |
| long, no reload | 98 % → 97 % | 44.1 px | 0.30 | 0.99 | 2847 | quarters: 0.00 → 0.00 → 0.00 → 0.00

Numbers say: light vs heavy: width 101.3 → 105.0 px, dark 0.30 → 0.31; pressure barely changes the width; the long stroke does not run out of paint.

## Brush Artist · Refs · #27 Orange impasto swatch
Impasto 1.00 · 60 px · 29.7 s

![Brush Artist · Refs · #27 Orange impasto swatch](Brush-Artist-Refs-27-Orange-impasto-swatch.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 20 % → 19 % | 56.9 px | 0.34 | 0.97 | 279 |
| heavy line | 20 % → 20 % | 59.3 px | 0.34 | 0.97 | 243 |
| pressure swell | 16 % → 15 % | 59.7 px | 0.35 | 0.97 | 161 |
| fast wave | 48 % → 46 % | 55.0 px | 0.34 | 0.97 | 652 |
| slow wave | 48 % → 47 % | 56.0 px | 0.35 | 0.97 | 1371 |
| spiral | 69 % → 63 % | 45.5 px | 0.34 | 0.91 | 1323 |
| loop | 41 % → 40 % | 53.6 px | 0.34 | 0.97 | 629 |
| tilted | 16 % → 16 % | 44.0 px | 0.35 | 1.00 | 316 |
| over the wet one | 34 % → 33 % | 50.8 px | 0.35 | 0.96 | 390 |
| long, no reload | 85 % → 75 % | 38.1 px | 0.34 | 0.89 | 2000 | quarters: 0.32 → 0.31 → 0.30 → 0.26

Numbers say: light vs heavy: width 56.9 → 59.3 px, dark 0.34 → 0.34; pressure barely changes the width.

## Brush Artist · Refs · #28 Miles Davis black lines
Ink 1.00 · 22 px · 34.8 s

![Brush Artist · Refs · #28 Miles Davis black lines](Brush-Artist-Refs-28-Miles-Davis-black-lines.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 4 % → 6 % | 12.1 px | 0.81 | 1.49 | 61 |
| heavy line | 17 % → 16 % | 48.3 px | 0.88 | 0.97 | 199 |
| pressure swell | 9 % → 10 % | 34.7 px | 0.87 | 1.04 | 105 |
| fast wave | 30 % → 29 % | 34.7 px | 0.87 | 0.98 | 292 |
| slow wave | 25 % → 25 % | 28.9 px | 0.87 | 1.00 | 314 |
| spiral | 39 % → 36 % | 25.5 px | 0.87 | 0.94 | 374 |
| loop | 23 % → 22 % | 29.2 px | 0.88 | 1.00 | 243 |
| tilted | 9 % → 9 % | 24.5 px | 0.88 | 1.01 | 94 |
| over the wet one | 21 % → 21 % | 34.2 px | 0.88 | 1.01 | 90 |
| long, no reload | 51 % → 42 % | 22.7 px | 0.86 | 0.82 | 499 | quarters: 0.59 → 0.51 → 0.39 → 0.30

Numbers say: light vs heavy: width 12.1 → 48.3 px, dark 0.81 → 0.88.

## Brush Artist · Refs · #29 Shrigley magenta asterisk
Watercolour 1.00 · 70 px · 41.8 s

![Brush Artist · Refs · #29 Shrigley magenta asterisk](Brush-Artist-Refs-29-Shrigley-magenta-asterisk.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 10 % → 13 % | 28.0 px | 0.61 | 1.39 | 72 |
| heavy line | 17 % → 18 % | 50.3 px | 0.61 | 1.04 | 181 |
| pressure swell | 11 % → 13 % | 41.1 px | 0.62 | 1.14 | 110 |
| fast wave | 38 % → 38 % | 43.8 px | 0.60 | 1.01 | 335 |
| slow wave | 35 % → 39 % | 41.0 px | 0.62 | 1.11 | 487 |
| spiral | 61 % → 61 % | 40.0 px | 0.60 | 1.01 | 512 |
| loop | 31 % → 32 % | 40.2 px | 0.61 | 1.03 | 355 |
| tilted | 18 % → 18 % | 49.0 px | 0.61 | 1.00 | 206 |
| over the wet one | 31 % → 34 % | 38.5 px | 0.61 | 1.08 | 131 |
| long, no reload | 75 % → 76 % | 33.6 px | 0.60 | 1.01 | 821 | quarters: 0.53 → 0.50 → 0.48 → 0.45

Numbers say: light vs heavy: width 28.0 → 50.3 px, dark 0.61 → 0.61; the long stroke does not run out of paint.

## Brush Artist · Refs · #30 Red gouache face patch
Gouache 1.00 · 60 px · 54.7 s

![Brush Artist · Refs · #30 Red gouache face patch](Brush-Artist-Refs-30-Red-gouache-face-patch.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 16 % → 15 % | 47.0 px | 0.49 | 0.91 | 162 |
| heavy line | 25 % → 20 % | 73.9 px | 0.49 | 0.80 | 236 |
| pressure swell | 19 % → 17 % | 72.6 px | 0.49 | 0.86 | 150 |
| fast wave | 49 % → 28 % | 56.1 px | 0.49 | 0.58 | 543 |
| slow wave | 48 % → 28 % | 55.4 px | 0.49 | 0.59 | 975 |
| spiral | 60 % → 28 % | 39.3 px | 0.49 | 0.47 | 1022 |
| loop | 40 % → 29 % | 51.6 px | 0.49 | 0.74 | 742 |
| tilted | 16 % → 17 % | 46.0 px | 0.49 | 1.00 | 285 |
| over the wet one | 36 % → 32 % | 55.3 px | 0.49 | 0.89 | 166 |
| long, no reload | 67 % → 30 % | 30.0 px | 0.49 | 0.44 | 1433 | quarters: 0.43 → 0.39 → 0.32 → 0.26

Numbers say: light vs heavy: width 47.0 → 73.9 px, dark 0.49 → 0.49.

## Brush Artist · Refs · #31 Warhol blotted line
Ink 1.00 · 6 px · 27.0 s

![Brush Artist · Refs · #31 Warhol blotted line](Brush-Artist-Refs-31-Warhol-blotted-line.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 1 % → 3 % | 2.6 px | 0.74 | 3.47 | 40 |
| heavy line | 7 % → 7 % | 20.7 px | 0.83 | 0.97 | 91 |
| pressure swell | 4 % → 4 % | 14.7 px | 0.84 | 1.13 | 38 |
| fast wave | 12 % → 9 % | 13.8 px | 0.81 | 0.73 | 177 |
| slow wave | 10 % → 8 % | 11.3 px | 0.81 | 0.81 | 206 |
| spiral | 15 % → 8 % | 9.7 px | 0.79 | 0.58 | 412 |
| loop | 9 % → 8 % | 11.9 px | 0.80 | 0.92 | 130 |
| tilted | 3 % → 3 % | 8.9 px | 0.84 | 1.02 | 48 |
| over the wet one | 8 % → 9 % | 14.5 px | 0.84 | 1.02 | 57 |
| long, no reload | 21 % → 9 % | 9.4 px | 0.77 | 0.44 | 374 | quarters: 0.25 → 0.13 → 0.04 → 0.01

Numbers say: light vs heavy: width 2.6 → 20.7 px, dark 0.74 → 0.83; wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #32 Thick orange swipes
Impasto 1.00 · 90 px · 49.0 s

![Brush Artist · Refs · #32 Thick orange swipes](Brush-Artist-Refs-32-Thick-orange-swipes.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 29 % → 29 % | 83.1 px | 0.38 | 1.01 | 453 |
| heavy line | 30 % → 29 % | 86.3 px | 0.38 | 0.97 | 454 |
| pressure swell | 23 % → 23 % | 86.6 px | 0.38 | 1.01 | 311 |
| fast wave | 63 % → 65 % | 73.0 px | 0.38 | 1.03 | 1547 |
| slow wave | 64 % → 62 % | 73.6 px | 0.38 | 0.98 | 3238 |
| spiral | 79 % → 78 % | 52.2 px | 0.38 | 0.98 | 2174 |
| loop | 57 % → 56 % | 73.3 px | 0.38 | 0.98 | 1168 |
| tilted | 21 % → 21 % | 59.2 px | 0.38 | 1.00 | 727 |
| over the wet one | 47 % → 45 % | 71.0 px | 0.38 | 0.97 | 759 |
| long, no reload | 95 % → 93 % | 42.8 px | 0.38 | 0.97 | 3131 | quarters: 0.37 → 0.37 → 0.37 → 0.35

Numbers say: light vs heavy: width 83.1 → 86.3 px, dark 0.38 → 0.38; pressure barely changes the width; the long stroke does not run out of paint.

## Brush Artist · Refs · #33 Red wet-in-wet band
Watercolour 1.00 · 80 px · 73.8 s

![Brush Artist · Refs · #33 Red wet-in-wet band](Brush-Artist-Refs-33-Red-wet-in-wet-band.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 24 % → 42 % | 69.9 px | 0.53 | 1.73 | 205 |
| heavy line | 34 % → 50 % | 98.3 px | 0.54 | 1.46 | 361 |
| pressure swell | 20 % → 30 % | 73.2 px | 0.57 | 1.55 | 305 |
| fast wave | 65 % → 79 % | 75.5 px | 0.61 | 1.21 | 1092 |
| slow wave | 61 % → 78 % | 70.0 px | 0.63 | 1.29 | 2052 |
| spiral | 78 % → 89 % | 51.5 px | 0.64 | 1.15 | 1266 |
| loop | 54 % → 68 % | 70.2 px | 0.62 | 1.25 | 782 |
| tilted | 28 % → 30 % | 77.4 px | 0.57 | 1.08 | 451 |
| over the wet one | 55 % → 79 % | 75.7 px | 0.57 | 1.44 | 280 |
| long, no reload | 96 % → 99 % | 43.2 px | 0.66 | 1.03 | 1874 | quarters: 0.68 → 0.68 → 0.68 → 0.63

Numbers say: light vs heavy: width 69.9 → 98.3 px, dark 0.53 → 0.54; the long stroke does not run out of paint; wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #34 Magenta oil patches
Oil 0.89 · Oil glaze 0.11 · 60 px · 28.5 s

![Brush Artist · Refs · #34 Magenta oil patches](Brush-Artist-Refs-34-Magenta-oil-patches.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 18 % → 18 % | 52.8 px | 0.60 | 1.01 | 379 |
| heavy line | 19 % → 19 % | 54.0 px | 0.61 | 1.00 | 396 |
| pressure swell | 15 % → 16 % | 58.1 px | 0.61 | 1.01 | 251 |
| fast wave | 48 % → 49 % | 55.5 px | 0.61 | 1.02 | 934 |
| slow wave | 50 % → 50 % | 57.3 px | 0.61 | 1.00 | 1676 |
| spiral | 71 % → 71 % | 46.8 px | 0.61 | 1.00 | 1775 |
| loop | 39 % → 39 % | 50.6 px | 0.61 | 1.00 | 1080 |
| tilted | 17 % → 17 % | 46.3 px | 0.61 | 1.00 | 412 |
| over the wet one | 33 % → 33 % | 46.1 px | 0.61 | 1.00 | 354 |
| long, no reload | 83 % → 83 % | 37.1 px | 0.61 | 1.00 | 2149 | quarters: 0.57 → 0.55 → 0.54 → 0.48

Numbers say: light vs heavy: width 52.8 → 54.0 px, dark 0.60 → 0.61; pressure barely changes the width.

## Brush Artist · Refs · #35 Red band with runs
Watercolour 1.00 · 70 px · 69.0 s

![Brush Artist · Refs · #35 Red band with runs](Brush-Artist-Refs-35-Red-band-with-runs.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 40 % → 45 % | 115.4 px | 0.42 | 1.14 | 163 |
| heavy line | 46 % → 51 % | 134.0 px | 0.42 | 1.11 | 349 |
| pressure swell | 21 % → 28 % | 77.2 px | 0.48 | 1.36 | 202 |
| fast wave | 67 % → 77 % | 77.3 px | 0.49 | 1.14 | 822 |
| slow wave | 65 % → 75 % | 75.0 px | 0.52 | 1.16 | 1625 |
| spiral | 87 % → 94 % | 57.3 px | 0.53 | 1.09 | 991 |
| loop | 79 % → 88 % | 102.3 px | 0.48 | 1.11 | 463 |
| tilted | 50 % → 50 % | 138.3 px | 0.47 | 1.02 | 423 |
| over the wet one | 77 % → 84 % | 76.1 px | 0.47 | 1.10 | 252 |
| long, no reload | 97 % → 100 % | 43.5 px | 0.58 | 1.03 | 2142 | quarters: 0.60 → 0.60 → 0.59 → 0.56

Numbers say: light vs heavy: width 115.4 → 134.0 px, dark 0.42 → 0.42; the long stroke does not run out of paint.

## Brush Artist · Refs · #36 Magenta letters flat brush
Gouache 1.00 · 36 px · 42.2 s

![Brush Artist · Refs · #36 Magenta letters flat brush](Brush-Artist-Refs-36-Magenta-letters-flat-brush.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 10 % → 10 % | 29.0 px | 0.45 | 0.98 | 129 |
| heavy line | 17 % → 14 % | 49.0 px | 0.45 | 0.85 | 111 |
| pressure swell | 13 % → 12 % | 49.3 px | 0.45 | 0.89 | 95 |
| fast wave | 35 % → 19 % | 40.9 px | 0.45 | 0.54 | 327 |
| slow wave | 35 % → 19 % | 40.0 px | 0.45 | 0.54 | 855 |
| spiral | 46 % → 19 % | 30.4 px | 0.45 | 0.42 | 566 |
| loop | 27 % → 20 % | 35.4 px | 0.45 | 0.72 | 247 |
| tilted | 11 % → 11 % | 30.0 px | 0.45 | 1.00 | 146 |
| over the wet one | 24 % → 23 % | 38.1 px | 0.45 | 0.93 | 100 |
| long, no reload | 46 % → 19 % | 20.8 px | 0.45 | 0.40 | 814 | quarters: 0.29 → 0.26 → 0.22 → 0.18

Numbers say: light vs heavy: width 29.0 → 49.0 px, dark 0.45 → 0.45.

## Brush Artist · Refs · #37 Oil still life dabs
Oil 0.89 · Oil glaze 0.11 · 40 px · 19.9 s

![Brush Artist · Refs · #37 Oil still life dabs](Brush-Artist-Refs-37-Oil-still-life-dabs.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 12 % → 12 % | 34.9 px | 0.37 | 1.00 | 146 |
| heavy line | 13 % → 13 % | 38.1 px | 0.37 | 1.00 | 181 |
| pressure swell | 10 % → 10 % | 37.1 px | 0.39 | 1.00 | 133 |
| fast wave | 31 % → 31 % | 36.2 px | 0.38 | 1.00 | 591 |
| slow wave | 32 % → 32 % | 37.5 px | 0.38 | 1.00 | 1086 |
| spiral | 52 % → 52 % | 34.2 px | 0.38 | 1.00 | 1209 |
| loop | 27 % → 27 % | 35.0 px | 0.39 | 1.00 | 551 |
| tilted | 13 % → 13 % | 35.6 px | 0.38 | 1.00 | 269 |
| over the wet one | 25 % → 25 % | 33.9 px | 0.38 | 1.00 | 263 |
| long, no reload | 61 % → 61 % | 27.2 px | 0.37 | 1.00 | 1028 | quarters: 0.28 → 0.26 → 0.24 → 0.21

Numbers say: light vs heavy: width 34.9 → 38.1 px, dark 0.37 → 0.37; pressure barely changes the width.

## Brush Artist · Refs · #38 Sanguine drawing
Pastel 1.00 · 6 px · 10.5 s

![Brush Artist · Refs · #38 Sanguine drawing](Brush-Artist-Refs-38-Sanguine-drawing.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 1 % → 1 % | 2.0 px | 0.61 | 1.00 | 17 |
| heavy line | 1 % → 1 % | 3.5 px | 0.62 | 1.00 | 42 |
| pressure swell | 1 % → 1 % | 3.3 px | 0.62 | 1.00 | 18 |
| fast wave | 3 % → 3 % | 3.2 px | 0.61 | 1.00 | 74 |
| slow wave | 3 % → 3 % | 3.0 px | 0.61 | 1.00 | 65 |
| spiral | 4 % → 4 % | 2.9 px | 0.61 | 1.00 | 75 |
| loop | 2 % → 2 % | 3.0 px | 0.61 | 1.00 | 38 |
| tilted | 1 % → 1 % | 3.4 px | 0.62 | 1.00 | 26 |
| over the wet one | 2 % → 2 % | 2.9 px | 0.62 | 1.00 | 19 |
| long, no reload | 7 % → 7 % | 3.0 px | 0.61 | 1.00 | 136 | quarters: 0.04 → 0.05 → 0.05 → 0.05

Numbers say: light vs heavy: width 2.0 → 3.5 px, dark 0.61 → 0.62; the long stroke does not run out of paint.

## Brush Artist · Refs · #39 Very thick impasto
Impasto 1.00 · 60 px · 28.8 s

![Brush Artist · Refs · #39 Very thick impasto](Brush-Artist-Refs-39-Very-thick-impasto.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 20 % → 19 % | 56.9 px | 0.61 | 0.97 | 285 |
| heavy line | 20 % → 20 % | 59.4 px | 0.61 | 0.97 | 188 |
| pressure swell | 16 % → 15 % | 59.8 px | 0.62 | 0.97 | 164 |
| fast wave | 48 % → 47 % | 55.1 px | 0.62 | 0.98 | 594 |
| slow wave | 49 % → 47 % | 56.2 px | 0.62 | 0.98 | 881 |
| spiral | 69 % → 65 % | 45.7 px | 0.62 | 0.94 | 939 |
| loop | 41 % → 40 % | 53.7 px | 0.62 | 0.97 | 479 |
| tilted | 16 % → 16 % | 44.1 px | 0.62 | 1.00 | 280 |
| over the wet one | 34 % → 33 % | 50.8 px | 0.62 | 0.97 | 232 |
| long, no reload | 85 % → 79 % | 38.3 px | 0.62 | 0.93 | 1581 | quarters: 0.57 → 0.57 → 0.56 → 0.52

Numbers say: light vs heavy: width 56.9 → 59.4 px, dark 0.61 → 0.61; pressure barely changes the width; the long stroke does not run out of paint.

## Brush Artist · Refs · #40 Watercolour blooms
Watercolour 1.00 · 90 px · 69.5 s

![Brush Artist · Refs · #40 Watercolour blooms](Brush-Artist-Refs-40-Watercolour-blooms.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 27 % → 46 % | 79.7 px | 0.08 | 1.69 | 199 |
| heavy line | 39 % → 53 % | 112.7 px | 0.09 | 1.35 | 409 |
| pressure swell | 26 % → 40 % | 97.4 px | 0.09 | 1.54 | 322 |
| fast wave | 68 % → 82 % | 78.6 px | 0.11 | 1.21 | 920 |
| slow wave | 68 % → 81 % | 79.0 px | 0.15 | 1.18 | 1341 |
| spiral | 83 % → 93 % | 54.4 px | 0.15 | 1.13 | 1368 |
| loop | 59 % → 72 % | 75.8 px | 0.13 | 1.24 | 764 |
| tilted | 33 % → 36 % | 93.3 px | 0.12 | 1.07 | 527 |
| over the wet one | 61 % → 81 % | 77.1 px | 0.12 | 1.33 | 456 |
| long, no reload | 98 % → 100 % | 43.9 px | 0.17 | 1.02 | 2048 | quarters: 0.21 → 0.19 → 0.17 → 0.12

Numbers say: light vs heavy: width 79.7 → 112.7 px, dark 0.08 → 0.09; wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #41 Coloured pencil hatching
Pastel 1.00 · 4 px · 12.9 s

![Brush Artist · Refs · #41 Coloured pencil hatching](Brush-Artist-Refs-41-Coloured-pencil-hatching.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 1 % → 1 % | 1.6 px | 0.42 | 1.00 | 16 |
| heavy line | 1 % → 1 % | 2.6 px | 0.43 | 1.00 | 17 |
| pressure swell | 1 % → 1 % | 2.1 px | 0.43 | 1.00 | 22 |
| fast wave | 2 % → 2 % | 2.2 px | 0.42 | 1.00 | 57 |
| slow wave | 2 % → 2 % | 2.1 px | 0.43 | 1.00 | 52 |
| spiral | 3 % → 3 % | 2.1 px | 0.43 | 1.00 | 76 |
| loop | 2 % → 2 % | 2.2 px | 0.43 | 1.00 | 40 |
| tilted | 1 % → 1 % | 3.0 px | 0.42 | 1.00 | 17 |
| over the wet one | 2 % → 2 % | 2.2 px | 0.42 | 1.00 | 14 |
| long, no reload | 5 % → 5 % | 2.3 px | 0.43 | 1.00 | 103 | quarters: 0.02 → 0.02 → 0.02 → 0.03

Numbers say: light vs heavy: width 1.6 → 2.6 px, dark 0.42 → 0.43; the long stroke does not run out of paint.

## Brush Artist · Refs · #42 Oil pastel shaggy
Pastel 1.00 · 18 px · 13.2 s

![Brush Artist · Refs · #42 Oil pastel shaggy](Brush-Artist-Refs-42-Oil-pastel-shaggy.png)

A light paint: laid on a grey sheet (on white it cannot be seen); **dark** = how far it is from the grey either way.

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 2 % → 2 % | 5.1 px | 0.35 | 1.00 | 36 |
| heavy line | 4 % → 4 % | 10.7 px | 0.36 | 1.00 | 44 |
| pressure swell | 3 % → 3 % | 9.5 px | 0.36 | 1.00 | 28 |
| fast wave | 8 % → 8 % | 9.1 px | 0.36 | 1.00 | 99 |
| slow wave | 7 % → 7 % | 8.2 px | 0.36 | 1.00 | 135 |
| spiral | 12 % → 12 % | 7.8 px | 0.36 | 1.00 | 168 |
| loop | 6 % → 6 % | 7.9 px | 0.36 | 1.00 | 69 |
| tilted | 2 % → 2 % | 6.9 px | 0.36 | 1.00 | 46 |
| over the wet one | 6 % → 6 % | 8.5 px | 0.36 | 1.00 | 38 |
| long, no reload | 15 % → 15 % | 6.9 px | 0.36 | 1.00 | 243 | quarters: 0.00 → 0.00 → 0.00 → 0.00

Numbers say: light vs heavy: width 5.1 → 10.7 px, dark 0.35 → 0.36; the long stroke does not run out of paint.

## Brush Artist · Refs · #43 Dragged black ink blocks
Gouache 1.00 · 70 px · 35.7 s

![Brush Artist · Refs · #43 Dragged black ink blocks](Brush-Artist-Refs-43-Dragged-black-ink-blocks.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 9 % → 0 % | 25.3 px | 0.00 | 0.00 | 246 |
| heavy line | 18 % → 3 % | 52.6 px | 0.62 | 0.19 | 571 |
| pressure swell | 13 % → 4 % | 48.3 px | 0.62 | 0.31 | 180 |
| fast wave | 27 % → 0 % | 31.5 px | 0.00 | 0.00 | 706 |
| slow wave | 30 % → 4 % | 34.9 px | 0.62 | 0.12 | 1176 |
| spiral | 56 % → 0 % | 36.8 px | 0.62 | 0.01 | 1178 |
| loop | 36 % → 3 % | 46.3 px | 0.62 | 0.09 | 763 |
| tilted | 15 % → 15 % | 42.4 px | 0.62 | 0.97 | 277 |
| over the wet one | 26 % → 3 % | 30.3 px | 0.62 | 0.12 | 343 |
| long, no reload | 59 % → 6 % | 26.3 px | 0.62 | 0.10 | 2253 | quarters: 0.40 → 0.36 → 0.41 → 0.34

Numbers say: light vs heavy: width 25.3 → 52.6 px, dark 0.00 → 0.62; the long stroke does not run out of paint.

## Brush Artist · Refs · #44 Blue looping ribbon
Oil 1.00 · 80 px · 35.0 s

![Brush Artist · Refs · #44 Blue looping ribbon](Brush-Artist-Refs-44-Blue-looping-ribbon.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 25 % → 26 % | 73.2 px | 0.71 | 1.04 | 366 |
| heavy line | 26 % → 26 % | 76.8 px | 0.71 | 1.00 | 433 |
| pressure swell | 20 % → 21 % | 76.8 px | 0.72 | 1.03 | 290 |
| fast wave | 62 % → 64 % | 71.1 px | 0.72 | 1.04 | 1044 |
| slow wave | 62 % → 62 % | 71.8 px | 0.72 | 1.00 | 1909 |
| spiral | 77 % → 77 % | 50.8 px | 0.73 | 1.00 | 2394 |
| loop | 54 % → 54 % | 70.3 px | 0.72 | 1.00 | 940 |
| tilted | 20 % → 20 % | 56.3 px | 0.72 | 1.00 | 851 |
| over the wet one | 43 % → 43 % | 62.5 px | 0.72 | 1.00 | 806 |
| long, no reload | 93 % → 93 % | 41.6 px | 0.73 | 1.00 | 3148 | quarters: 0.72 → 0.71 → 0.71 → 0.65

Numbers say: light vs heavy: width 73.2 → 76.8 px, dark 0.71 → 0.71; pressure barely changes the width; the long stroke does not run out of paint.

## Brush Artist · Refs · #45 Soft pastel pepper
Pastel 1.00 · 40 px · 12.0 s

![Brush Artist · Refs · #45 Soft pastel pepper](Brush-Artist-Refs-45-Soft-pastel-pepper.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 4 % → 4 % | 11.3 px | 0.53 | 1.00 | 73 |
| heavy line | 8 % → 8 % | 23.0 px | 0.53 | 1.00 | 54 |
| pressure swell | 5 % → 5 % | 19.5 px | 0.53 | 1.00 | 41 |
| fast wave | 17 % → 17 % | 19.4 px | 0.53 | 1.00 | 134 |
| slow wave | 15 % → 15 % | 17.1 px | 0.53 | 1.00 | 231 |
| spiral | 25 % → 25 % | 16.3 px | 0.53 | 1.00 | 375 |
| loop | 12 % → 12 % | 16.1 px | 0.53 | 1.00 | 232 |
| tilted | 5 % → 5 % | 12.8 px | 0.53 | 1.00 | 125 |
| over the wet one | 11 % → 11 % | 17.7 px | 0.53 | 1.00 | 131 |
| long, no reload | 30 % → 30 % | 13.6 px | 0.54 | 1.00 | 390 | quarters: 0.18 → 0.18 → 0.18 → 0.18

Numbers say: light vs heavy: width 11.3 → 23.0 px, dark 0.53 → 0.53; the long stroke does not run out of paint.

## Brush Artist · Refs · #46 Red-brown ink lips
Watercolour 1.00 · 50 px · 45.3 s

![Brush Artist · Refs · #46 Red-brown ink lips](Brush-Artist-Refs-46-Red-brown-ink-lips.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 15 % → 31 % | 43.3 px | 0.59 | 2.06 | 68 |
| heavy line | 22 % → 35 % | 62.8 px | 0.60 | 1.64 | 115 |
| pressure swell | 13 % → 22 % | 47.7 px | 0.64 | 1.71 | 71 |
| fast wave | 41 % → 64 % | 47.8 px | 0.64 | 1.56 | 259 |
| slow wave | 41 % → 63 % | 47.0 px | 0.67 | 1.54 | 476 |
| spiral | 65 % → 79 % | 42.7 px | 0.69 | 1.23 | 505 |
| loop | 37 % → 56 % | 47.8 px | 0.66 | 1.51 | 208 |
| tilted | 20 % → 23 % | 56.4 px | 0.60 | 1.12 | 178 |
| over the wet one | 41 % → 63 % | 57.1 px | 0.60 | 1.55 | 158 |
| long, no reload | 80 % → 96 % | 35.9 px | 0.69 | 1.20 | 1013 | quarters: 0.71 → 0.71 → 0.70 → 0.65

Numbers say: light vs heavy: width 43.3 → 62.8 px, dark 0.59 → 0.60; the long stroke does not run out of paint; wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #47 Pink knife slabs
Impasto 1.00 · 90 px · 32.5 s

![Brush Artist · Refs · #47 Pink knife slabs](Brush-Artist-Refs-47-Pink-knife-slabs.png)

A light paint: laid on a grey sheet (on white it cannot be seen); **dark** = how far it is from the grey either way.

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 28 % → 27 % | 81.2 px | 0.29 | 0.97 | 314 |
| heavy line | 29 % → 28 % | 83.6 px | 0.29 | 0.97 | 255 |
| pressure swell | 22 % → 22 % | 83.5 px | 0.29 | 1.01 | 152 |
| fast wave | 61 % → 60 % | 70.4 px | 0.28 | 0.99 | 763 |
| slow wave | 61 % → 59 % | 70.9 px | 0.27 | 0.96 | 1013 |
| spiral | 76 % → 58 % | 50.1 px | 0.27 | 0.76 | 1027 |
| loop | 55 % → 54 % | 71.8 px | 0.28 | 0.97 | 523 |
| tilted | 21 % → 21 % | 59.3 px | 0.29 | 1.00 | 305 |
| over the wet one | 46 % → 44 % | 68.0 px | 0.29 | 0.96 | 296 |
| long, no reload | 92 % → 76 % | 41.4 px | 0.26 | 0.82 | 2138 | quarters: 0.00 → 0.00 → 0.00 → 0.00

Numbers say: light vs heavy: width 81.2 → 83.6 px, dark 0.29 → 0.29; pressure barely changes the width; the long stroke does not run out of paint.

## Brush Artist · Refs · #48 Black bands with drips
Gouache 1.00 · 70 px · 48.1 s

![Brush Artist · Refs · #48 Black bands with drips](Brush-Artist-Refs-48-Black-bands-with-drips.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 27 % → 24 % | 79.0 px | 0.64 | 0.87 | 172 |
| heavy line | 35 % → 29 % | 102.8 px | 0.64 | 0.82 | 387 |
| pressure swell | 25 % → 22 % | 91.9 px | 0.64 | 0.89 | 266 |
| fast wave | 64 % → 43 % | 74.0 px | 0.64 | 0.67 | 871 |
| slow wave | 61 % → 41 % | 70.7 px | 0.64 | 0.67 | 1022 |
| spiral | 69 % → 39 % | 45.7 px | 0.64 | 0.56 | 895 |
| loop | 54 % → 42 % | 70.4 px | 0.64 | 0.77 | 429 |
| tilted | 29 % → 29 % | 80.7 px | 0.64 | 1.00 | 291 |
| over the wet one | 58 % → 49 % | 80.4 px | 0.64 | 0.85 | 217 |
| long, no reload | 78 % → 39 % | 34.9 px | 0.64 | 0.50 | 1697 | quarters: 0.61 → 0.57 → 0.51 → 0.42

Numbers say: light vs heavy: width 79.0 → 102.8 px, dark 0.64 → 0.64.

## Brush Artist · Refs · #49 Magenta letters round brush
Ink 1.00 · 30 px · 32.2 s

![Brush Artist · Refs · #49 Magenta letters round brush](Brush-Artist-Refs-49-Magenta-letters-round-brush.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 6 % → 8 % | 17.3 px | 0.50 | 1.29 | 50 |
| heavy line | 21 % → 21 % | 61.2 px | 0.51 | 0.99 | 131 |
| pressure swell | 12 % → 12 % | 44.6 px | 0.52 | 1.02 | 103 |
| fast wave | 38 % → 38 % | 44.2 px | 0.51 | 0.99 | 290 |
| slow wave | 32 % → 32 % | 36.7 px | 0.51 | 0.99 | 386 |
| spiral | 50 % → 48 % | 33.0 px | 0.51 | 0.96 | 385 |
| loop | 29 % → 29 % | 37.3 px | 0.51 | 1.00 | 184 |
| tilted | 11 % → 11 % | 30.9 px | 0.52 | 1.01 | 97 |
| over the wet one | 26 % → 26 % | 42.2 px | 0.52 | 1.01 | 87 |
| long, no reload | 61 % → 55 % | 27.5 px | 0.50 | 0.90 | 560 | quarters: 0.41 → 0.36 → 0.30 → 0.24

Numbers say: light vs heavy: width 17.3 → 61.2 px, dark 0.50 → 0.51.

## Brush Artist · Refs · #50 Thick swipes on photo
Impasto 1.00 · 40 px · 19.3 s

![Brush Artist · Refs · #50 Thick swipes on photo](Brush-Artist-Refs-50-Thick-swipes-on-photo.png)

A light paint: laid on a grey sheet (on white it cannot be seen); **dark** = how far it is from the grey either way.

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 13 % → 13 % | 38.3 px | 0.27 | 0.96 | 123 |
| heavy line | 14 % → 13 % | 39.8 px | 0.27 | 0.96 | 170 |
| pressure swell | 11 % → 10 % | 40.2 px | 0.26 | 0.95 | 113 |
| fast wave | 33 % → 31 % | 38.4 px | 0.26 | 0.93 | 802 |
| slow wave | 34 % → 32 % | 39.1 px | 0.26 | 0.95 | 1136 |
| spiral | 58 % → 47 % | 38.6 px | 0.25 | 0.80 | 576 |
| loop | 28 % → 27 % | 36.6 px | 0.26 | 0.95 | 278 |
| tilted | 12 % → 12 % | 34.1 px | 0.26 | 1.00 | 155 |
| over the wet one | 25 % → 23 % | 35.1 px | 0.26 | 0.95 | 127 |
| long, no reload | 66 % → 45 % | 29.5 px | 0.24 | 0.69 | 790 | quarters: 0.00 → 0.00 → 0.00 → 0.00

Numbers say: light vs heavy: width 38.3 → 39.8 px, dark 0.27 → 0.27; pressure barely changes the width; the long stroke does not run out of paint.

## Brush Artist · Refs · Drag #e8b4a8
Gouache 1.00 · 40 px · 17.6 s

![Brush Artist · Refs · Drag #e8b4a8](Brush-Artist-Refs-Drag-e8b4a8.png)

A light paint: laid on a grey sheet (on white it cannot be seen); **dark** = how far it is from the grey either way.

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 3 % → 0 % | 8.1 px | 0.00 | 0.00 | 106 |
| heavy line | 3 % → 0 % | 8.1 px | 0.00 | 0.00 | 119 |
| pressure swell | 3 % → 0 % | 13.1 px | 0.00 | 0.00 | 87 |
| fast wave | 9 % → 0 % | 10.5 px | 0.00 | 0.00 | 296 |
| slow wave | 5 % → 0 % | 5.4 px | 0.00 | 0.00 | 495 |
| spiral | 18 % → 0 % | 11.8 px | 0.00 | 0.00 | 668 |
| loop | 16 % → 0 % | 20.3 px | 0.00 | 0.00 | 367 |
| tilted | 5 % → 4 % | 14.9 px | 0.00 | 0.83 | 145 |
| over the wet one | 7 % → 0 % | 4.1 px | 0.00 | 0.00 | 115 |
| long, no reload | 19 % → 0 % | 8.5 px | 0.34 | 0.01 | 869 | quarters: 0.01 → 0.01 → 0.01 → 0.01

Numbers say: light vs heavy: width 8.1 → 8.1 px, dark 0.00 → 0.00; pressure barely changes the width; the long stroke does not run out of paint.

## Brush Artist · Refs · Drag #e8e4e0
Gouache 1.00 · 40 px · 17.8 s

![Brush Artist · Refs · Drag #e8e4e0](Brush-Artist-Refs-Drag-e8e4e0.png)

A light paint: laid on a grey sheet (on white it cannot be seen); **dark** = how far it is from the grey either way.

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 3 % → 0 % | 8.1 px | 0.00 | 0.00 | 146 |
| heavy line | 3 % → 0 % | 8.1 px | 0.00 | 0.00 | 168 |
| pressure swell | 3 % → 0 % | 13.1 px | 0.00 | 0.00 | 88 |
| fast wave | 9 % → 0 % | 10.5 px | 0.00 | 0.00 | 328 |
| slow wave | 5 % → 0 % | 5.4 px | 0.00 | 0.00 | 627 |
| spiral | 18 % → 0 % | 11.8 px | 0.00 | 0.00 | 536 |
| loop | 16 % → 0 % | 20.3 px | 0.00 | 0.00 | 300 |
| tilted | 5 % → 4 % | 14.9 px | 0.00 | 0.83 | 151 |
| over the wet one | 7 % → 0 % | 4.1 px | 0.00 | 0.00 | 118 |
| long, no reload | 19 % → 0 % | 8.5 px | 0.42 | 0.01 | 1033 | quarters: 0.01 → 0.01 → 0.01 → 0.01

Numbers say: light vs heavy: width 8.1 → 8.1 px, dark 0.00 → 0.00; pressure barely changes the width; the long stroke does not run out of paint.

## Brush Artist · Refs · Finger
Pastel 1.00 · 36 px · 20.6 s · over bands of wet oil paint and oil pastel in turn (it works on paint already there: look at what it does to the bands; covered counts the bands too)

![Brush Artist · Refs · Finger](Brush-Artist-Refs-Finger.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 25 % → 25 % | 73.8 px | 0.80 | 1.00 | 42 |
| heavy line | 27 % → 27 % | 78.6 px | 0.80 | 1.00 | 48 |
| pressure swell | 26 % → 26 % | 97.7 px | 0.80 | 1.00 | 36 |
| fast wave | 32 % → 32 % | 37.3 px | 0.78 | 1.00 | 120 |
| slow wave | 31 % → 31 % | 36.3 px | 0.78 | 1.00 | 214 |
| spiral | 38 % → 38 % | 25.2 px | 0.76 | 1.00 | 279 |
| loop | 30 % → 30 % | 39.5 px | 0.78 | 1.00 | 154 |
| tilted | 26 % → 26 % | 73.4 px | 0.78 | 1.00 | 94 |
| over the wet one | 29 % → 29 % | 6.8 px | 0.78 | 1.00 | 51 |
| long, no reload | 41 % → 41 % | 18.2 px | 0.76 | 1.00 | 302 | quarters: 0.25 → 0.37 → 0.34 → 0.39

Numbers say: light vs heavy: width 73.8 → 78.6 px, dark 0.80 → 0.80; pressure barely changes the width; the long stroke does not run out of paint.

## Brush Artist · Ink — wash
Watercolour 1.00 · 38 px · 33.4 s

![Brush Artist · Ink — wash](Brush-Artist-Ink-wash.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 11 % → 11 % | 31.6 px | 0.39 | 1.04 | 82 |
| heavy line | 19 % → 19 % | 54.3 px | 0.32 | 1.03 | 97 |
| pressure swell | 12 % → 13 % | 45.2 px | 0.37 | 1.04 | 59 |
| fast wave | 39 % → 41 % | 45.5 px | 0.31 | 1.04 | 208 |
| slow wave | 37 % → 38 % | 42.9 px | 0.37 | 1.03 | 385 |
| spiral | 58 % → 61 % | 38.6 px | 0.31 | 1.04 | 326 |
| loop | 32 % → 33 % | 41.9 px | 0.35 | 1.02 | 171 |
| tilted | 13 % → 14 % | 37.0 px | 0.38 | 1.04 | 100 |
| over the wet one | 29 % → 30 % | 42.8 px | 0.38 | 1.04 | 93 |
| long, no reload | 67 % → 72 % | 30.0 px | 0.29 | 1.07 | 460 | quarters: 0.34 → 0.27 → 0.19 → 0.12

Numbers say: light vs heavy: width 31.6 → 54.3 px, dark 0.39 → 0.32.

## Brush Artist · Ink — brush line
Ink 1.00 · 16 px · 24.9 s

![Brush Artist · Ink — brush line](Brush-Artist-Ink-brush-line.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 3 % → 5 % | 7.5 px | 0.77 | 1.89 | 36 |
| heavy line | 13 % → 13 % | 38.4 px | 0.88 | 0.99 | 84 |
| pressure swell | 7 % → 8 % | 27.7 px | 0.87 | 1.06 | 60 |
| fast wave | 24 % → 23 % | 27.4 px | 0.87 | 0.96 | 222 |
| slow wave | 20 % → 19 % | 22.8 px | 0.87 | 0.97 | 248 |
| spiral | 30 % → 26 % | 20.0 px | 0.86 | 0.87 | 322 |
| loop | 18 % → 18 % | 23.4 px | 0.87 | 0.99 | 134 |
| tilted | 7 % → 7 % | 20.3 px | 0.88 | 1.01 | 64 |
| over the wet one | 17 % → 17 % | 26.5 px | 0.88 | 1.00 | 65 |
| long, no reload | 42 % → 30 % | 18.7 px | 0.85 | 0.71 | 389 | quarters: 0.49 → 0.40 → 0.29 → 0.20

Numbers say: light vs heavy: width 7.5 → 38.4 px, dark 0.77 → 0.88; wet paint spreads well beyond the stroke.

## Brush Artist · Ink — dry brush
Gouache 1.00 · 30 px · 17.0 s

![Brush Artist · Ink — dry brush](Brush-Artist-Ink-dry-brush.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 3 % → 0 % | 9.7 px | 0.00 | 0.00 | 57 |
| heavy line | 5 % → 0 % | 15.2 px | 0.00 | 0.00 | 155 |
| pressure swell | 4 % → 0 % | 14.5 px | 0.77 | 0.06 | 80 |
| fast wave | 9 % → 0 % | 10.3 px | 0.00 | 0.00 | 217 |
| slow wave | 7 % → 0 % | 8.6 px | 0.77 | 0.01 | 388 |
| spiral | 16 % → 0 % | 10.4 px | 0.00 | 0.00 | 378 |
| loop | 12 % → 0 % | 15.0 px | 0.77 | 0.01 | 204 |
| tilted | 6 % → 6 % | 17.0 px | 0.77 | 0.91 | 104 |
| over the wet one | 9 % → 0 % | 7.7 px | 0.77 | 0.03 | 88 |
| long, no reload | 18 % → 1 % | 7.8 px | 0.77 | 0.03 | 565 | quarters: 0.19 → 0.19 → 0.13 → 0.09

Numbers say: light vs heavy: width 9.7 → 15.2 px, dark 0.00 → 0.00.

## Brush Artist · Watercolour — blue
Watercolour 0.93 · Ink 0.07 · 40 px · 31.5 s

![Brush Artist · Watercolour — blue](Brush-Artist-Watercolour-blue.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 6 % → 11 % | 16.2 px | 0.29 | 1.88 | 33 |
| heavy line | 11 % → 13 % | 31.9 px | 0.29 | 1.17 | 71 |
| pressure swell | 7 % → 9 % | 25.7 px | 0.30 | 1.38 | 42 |
| fast wave | 24 % → 27 % | 28.2 px | 0.29 | 1.12 | 157 |
| slow wave | 23 % → 32 % | 26.4 px | 0.31 | 1.41 | 241 |
| spiral | 39 % → 47 % | 25.6 px | 0.29 | 1.21 | 234 |
| loop | 20 % → 25 % | 25.7 px | 0.30 | 1.25 | 126 |
| tilted | 12 % → 12 % | 34.0 px | 0.30 | 1.00 | 171 |
| over the wet one | 21 % → 25 % | 25.2 px | 0.30 | 1.19 | 95 |
| long, no reload | 53 % → 59 % | 23.6 px | 0.30 | 1.12 | 427 | quarters: 0.23 → 0.21 → 0.19 → 0.16

Numbers say: light vs heavy: width 16.2 → 31.9 px, dark 0.29 → 0.29; wet paint spreads well beyond the stroke.

## Brush Artist · Watercolour — violet
Watercolour 0.93 · Ink 0.07 · 40 px · 32.0 s

![Brush Artist · Watercolour — violet](Brush-Artist-Watercolour-violet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 6 % → 11 % | 16.2 px | 0.36 | 1.88 | 30 |
| heavy line | 11 % → 13 % | 31.9 px | 0.37 | 1.17 | 60 |
| pressure swell | 7 % → 9 % | 25.7 px | 0.38 | 1.38 | 38 |
| fast wave | 24 % → 27 % | 28.2 px | 0.38 | 1.12 | 196 |
| slow wave | 23 % → 32 % | 26.4 px | 0.39 | 1.41 | 338 |
| spiral | 39 % → 47 % | 25.6 px | 0.37 | 1.21 | 261 |
| loop | 20 % → 25 % | 25.7 px | 0.38 | 1.25 | 134 |
| tilted | 12 % → 12 % | 34.0 px | 0.38 | 1.00 | 113 |
| over the wet one | 21 % → 25 % | 25.2 px | 0.38 | 1.19 | 72 |
| long, no reload | 53 % → 59 % | 23.6 px | 0.38 | 1.12 | 392 | quarters: 0.28 → 0.27 → 0.24 → 0.21

Numbers say: light vs heavy: width 16.2 → 31.9 px, dark 0.36 → 0.37; wet paint spreads well beyond the stroke.

## Brush Artist · Watercolour — teal
Watercolour 0.93 · Ink 0.07 · 40 px · 30.9 s

![Brush Artist · Watercolour — teal](Brush-Artist-Watercolour-teal.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 6 % → 11 % | 16.2 px | 0.23 | 1.88 | 32 |
| heavy line | 11 % → 13 % | 31.9 px | 0.23 | 1.17 | 70 |
| pressure swell | 7 % → 9 % | 25.7 px | 0.24 | 1.38 | 65 |
| fast wave | 24 % → 27 % | 28.2 px | 0.23 | 1.12 | 201 |
| slow wave | 23 % → 32 % | 26.4 px | 0.25 | 1.41 | 229 |
| spiral | 39 % → 47 % | 25.6 px | 0.23 | 1.21 | 279 |
| loop | 20 % → 25 % | 25.7 px | 0.24 | 1.25 | 151 |
| tilted | 12 % → 12 % | 34.0 px | 0.24 | 1.00 | 124 |
| over the wet one | 21 % → 25 % | 25.2 px | 0.24 | 1.19 | 65 |
| long, no reload | 53 % → 59 % | 23.6 px | 0.24 | 1.12 | 369 | quarters: 0.18 → 0.16 → 0.15 → 0.13

Numbers say: light vs heavy: width 16.2 → 31.9 px, dark 0.23 → 0.23; wet paint spreads well beyond the stroke.

## Brush Artist · Gouache
Gouache 1.00 · 30 px · 38.8 s

![Brush Artist · Gouache](Brush-Artist-Gouache.png)

A light paint: laid on a grey sheet (on white it cannot be seen); **dark** = how far it is from the grey either way.

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 8 % → 8 % | 24.4 px | 0.27 | 0.97 | 76 |
| heavy line | 15 % → 12 % | 42.8 px | 0.27 | 0.78 | 92 |
| pressure swell | 11 % → 9 % | 41.0 px | 0.27 | 0.85 | 58 |
| fast wave | 30 % → 14 % | 34.9 px | 0.26 | 0.45 | 198 |
| slow wave | 29 % → 14 % | 34.0 px | 0.26 | 0.47 | 407 |
| spiral | 40 % → 14 % | 26.6 px | 0.26 | 0.35 | 342 |
| loop | 24 % → 15 % | 30.6 px | 0.26 | 0.62 | 184 |
| tilted | 10 % → 10 % | 27.4 px | 0.27 | 1.01 | 109 |
| over the wet one | 22 % → 19 % | 32.9 px | 0.27 | 0.89 | 86 |
| long, no reload | 43 % → 15 % | 19.1 px | 0.26 | 0.35 | 659 | quarters: 0.01 → 0.01 → 0.01 → 0.01

Numbers say: light vs heavy: width 24.4 → 42.8 px, dark 0.27 → 0.27; the long stroke does not run out of paint.

## Brush Artist · Oil — bristle
Oil 0.89 · Oil glaze 0.11 · 30 px · 17.9 s

![Brush Artist · Oil — bristle](Brush-Artist-Oil-bristle.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 9 % → 9 % | 25.5 px | 0.52 | 1.00 | 146 |
| heavy line | 10 % → 10 % | 28.7 px | 0.54 | 1.00 | 151 |
| pressure swell | 7 % → 7 % | 27.1 px | 0.55 | 1.00 | 101 |
| fast wave | 23 % → 23 % | 27.1 px | 0.55 | 1.00 | 283 |
| slow wave | 24 % → 24 % | 27.6 px | 0.54 | 1.00 | 548 |
| spiral | 40 % → 40 % | 26.3 px | 0.54 | 1.00 | 535 |
| loop | 20 % → 20 % | 26.1 px | 0.54 | 1.00 | 288 |
| tilted | 11 % → 11 % | 29.9 px | 0.55 | 1.00 | 165 |
| over the wet one | 20 % → 20 % | 25.0 px | 0.55 | 1.00 | 148 |
| long, no reload | 50 % → 50 % | 22.3 px | 0.54 | 1.00 | 921 | quarters: 0.32 → 0.30 → 0.29 → 0.28

Numbers say: light vs heavy: width 25.5 → 28.7 px, dark 0.52 → 0.54; the long stroke does not run out of paint.

## Brush Artist · Charcoal — stick
Charcoal 0.78 · Pastel 0.22 · 28 px · 12.7 s

![Brush Artist · Charcoal — stick](Brush-Artist-Charcoal-stick.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 5 % → 5 % | 15.5 px | 0.85 | 1.00 | 24 |
| heavy line | 8 % → 8 % | 24.0 px | 0.85 | 1.00 | 32 |
| pressure swell | 5 % → 5 % | 20.6 px | 0.85 | 1.00 | 24 |
| fast wave | 18 % → 18 % | 20.6 px | 0.85 | 1.00 | 76 |
| slow wave | 17 % → 17 % | 20.1 px | 0.85 | 1.00 | 109 |
| spiral | 29 % → 29 % | 19.1 px | 0.85 | 1.00 | 103 |
| loop | 15 % → 15 % | 19.4 px | 0.85 | 1.00 | 55 |
| tilted | 6 % → 6 % | 16.6 px | 0.85 | 1.00 | 51 |
| over the wet one | 13 % → 13 % | 19.9 px | 0.85 | 1.00 | 35 |
| long, no reload | 41 % → 41 % | 18.6 px | 0.85 | 1.00 | 193 | quarters: 0.39 → 0.39 → 0.39 → 0.39

Numbers say: light vs heavy: width 15.5 → 24.0 px, dark 0.85 → 0.85; the long stroke does not run out of paint.

## Brush Artist · Charcoal — stick B
Charcoal 0.78 · Pastel 0.22 · 36 px · 14.5 s

![Brush Artist · Charcoal — stick B](Brush-Artist-Charcoal-stick-B.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 7 % → 7 % | 19.8 px | 0.85 | 1.00 | 57 |
| heavy line | 10 % → 10 % | 30.4 px | 0.85 | 1.00 | 47 |
| pressure swell | 7 % → 7 % | 26.0 px | 0.85 | 1.00 | 34 |
| fast wave | 23 % → 23 % | 26.8 px | 0.85 | 1.00 | 153 |
| slow wave | 22 % → 22 % | 25.5 px | 0.85 | 1.00 | 209 |
| spiral | 38 % → 38 % | 25.4 px | 0.85 | 1.00 | 202 |
| loop | 19 % → 19 % | 25.0 px | 0.85 | 1.00 | 103 |
| tilted | 7 % → 7 % | 20.4 px | 0.85 | 1.00 | 51 |
| over the wet one | 17 % → 17 % | 25.9 px | 0.85 | 1.00 | 51 |
| long, no reload | 51 % → 51 % | 22.7 px | 0.85 | 1.00 | 334 | quarters: 0.47 → 0.47 → 0.47 → 0.47

Numbers say: light vs heavy: width 19.8 → 30.4 px, dark 0.85 → 0.85; the long stroke does not run out of paint.

## Brush Artist · Charcoal — stick C
Charcoal 0.78 · Pastel 0.22 · 22 px · 13.7 s

![Brush Artist · Charcoal — stick C](Brush-Artist-Charcoal-stick-C.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 4 % → 4 % | 12.9 px | 0.85 | 1.00 | 60 |
| heavy line | 7 % → 7 % | 19.5 px | 0.85 | 1.00 | 29 |
| pressure swell | 4 % → 4 % | 16.8 px | 0.85 | 1.00 | 27 |
| fast wave | 15 % → 15 % | 17.0 px | 0.85 | 1.00 | 68 |
| slow wave | 14 % → 14 % | 16.1 px | 0.85 | 1.00 | 125 |
| spiral | 24 % → 24 % | 15.6 px | 0.85 | 1.00 | 118 |
| loop | 12 % → 12 % | 15.9 px | 0.85 | 1.00 | 81 |
| tilted | 5 % → 5 % | 14.4 px | 0.85 | 1.00 | 71 |
| over the wet one | 11 % → 11 % | 16.7 px | 0.85 | 1.00 | 83 |
| long, no reload | 34 % → 34 % | 15.5 px | 0.85 | 1.00 | 203 | quarters: 0.33 → 0.32 → 0.32 → 0.33

Numbers say: light vs heavy: width 12.9 → 19.5 px, dark 0.85 → 0.85; the long stroke does not run out of paint.

## Oil · Henry Ward · Loaded flat
Oil 1.00 · 46 px · 19.7 s

![Oil · Henry Ward · Loaded flat](Oil-Henry-Ward-Loaded-flat.png)

A light paint: laid on a grey sheet (on white it cannot be seen); **dark** = how far it is from the grey either way.

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 14 % → 14 % | 40.2 px | 0.29 | 1.00 | 240 |
| heavy line | 12 % → 12 % | 35.5 px | 0.35 | 1.00 | 242 |
| pressure swell | 11 % → 11 % | 39.6 px | 0.34 | 1.00 | 177 |
| fast wave | 34 % → 34 % | 38.9 px | 0.25 | 1.00 | 584 |
| slow wave | 29 % → 29 % | 34.1 px | 0.31 | 1.00 | 1005 |
| spiral | 50 % → 50 % | 32.9 px | 0.31 | 1.00 | 832 |
| loop | 28 % → 28 % | 35.7 px | 0.34 | 1.00 | 580 |
| tilted | 13 % → 13 % | 36.8 px | 0.34 | 1.00 | 335 |
| over the wet one | 25 % → 25 % | 32.9 px | 0.34 | 1.00 | 256 |
| long, no reload | 56 % → 56 % | 25.2 px | 0.30 | 1.00 | 1189 | quarters: 0.00 → 0.00 → 0.00 → 0.00

Numbers say: light vs heavy: width 40.2 → 35.5 px, dark 0.29 → 0.35; the long stroke does not run out of paint.

## Oil · Henry Ward · Dry scrub
Oil 1.00 · 50 px · 20.4 s

![Oil · Henry Ward · Dry scrub](Oil-Henry-Ward-Dry-scrub.png)

A light paint: laid on a grey sheet (on white it cannot be seen); **dark** = how far it is from the grey either way.

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 10 % → 10 % | 28.4 px | 0.15 | 1.00 | 196 |
| heavy line | 9 % → 9 % | 25.6 px | 0.19 | 1.00 | 216 |
| pressure swell | 9 % → 9 % | 32.3 px | 0.27 | 1.00 | 186 |
| fast wave | 24 % → 25 % | 28.2 px | 0.15 | 1.01 | 592 |
| slow wave | 19 % → 19 % | 22.5 px | 0.21 | 1.00 | 1066 |
| spiral | 51 % → 51 % | 33.3 px | 0.24 | 1.00 | 845 |
| loop | 31 % → 31 % | 39.9 px | 0.27 | 1.00 | 468 |
| tilted | 12 % → 12 % | 32.1 px | 0.23 | 1.00 | 244 |
| over the wet one | 17 % → 17 % | 16.5 px | 0.23 | 1.00 | 189 |
| long, no reload | 52 % → 52 % | 23.3 px | 0.22 | 1.00 | 1389 | quarters: 0.00 → 0.00 → 0.00 → 0.00

Numbers say: light vs heavy: width 28.4 → 25.6 px, dark 0.15 → 0.19; the long stroke does not run out of paint.

## Oil · Henry Ward · Dirty contour
Oil 1.00 · 24 px · 17.6 s

![Oil · Henry Ward · Dirty contour](Oil-Henry-Ward-Dirty-contour.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 8 % → 8 % | 24.1 px | 0.73 | 1.00 | 112 |
| heavy line | 9 % → 9 % | 25.3 px | 0.74 | 1.00 | 131 |
| pressure swell | 7 % → 7 % | 25.8 px | 0.77 | 1.00 | 88 |
| fast wave | 19 % → 19 % | 22.1 px | 0.75 | 1.00 | 318 |
| slow wave | 22 % → 22 % | 24.9 px | 0.76 | 1.00 | 516 |
| spiral | 32 % → 32 % | 21.2 px | 0.74 | 1.00 | 570 |
| loop | 18 % → 18 % | 22.9 px | 0.76 | 1.00 | 335 |
| tilted | 9 % → 9 % | 25.4 px | 0.76 | 1.00 | 156 |
| over the wet one | 17 % → 17 % | 23.0 px | 0.76 | 1.00 | 124 |
| long, no reload | 39 % → 39 % | 17.4 px | 0.73 | 1.00 | 779 | quarters: 0.42 → 0.35 → 0.28 → 0.22

Numbers say: light vs heavy: width 24.1 → 25.3 px, dark 0.73 → 0.74; pressure barely changes the width.

## Oil · Henry Ward · Wet drag
Oil 1.00 · 44 px · 20.6 s

![Oil · Henry Ward · Wet drag](Oil-Henry-Ward-Wet-drag.png)

A light paint: laid on a grey sheet (on white it cannot be seen); **dark** = how far it is from the grey either way.

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 11 % → 11 % | 31.5 px | 0.18 | 1.00 | 270 |
| heavy line | 14 % → 14 % | 40.0 px | 0.35 | 1.00 | 228 |
| pressure swell | 11 % → 11 % | 40.4 px | 0.32 | 1.00 | 171 |
| fast wave | 30 % → 30 % | 34.3 px | 0.24 | 1.00 | 668 |
| slow wave | 29 % → 29 % | 34.0 px | 0.29 | 1.00 | 1456 |
| spiral | 50 % → 50 % | 33.1 px | 0.27 | 1.00 | 1343 |
| loop | 30 % → 30 % | 38.7 px | 0.32 | 1.00 | 514 |
| tilted | 13 % → 13 % | 35.0 px | 0.31 | 1.00 | 238 |
| over the wet one | 24 % → 24 % | 31.6 px | 0.31 | 1.00 | 185 |
| long, no reload | 61 % → 61 % | 27.4 px | 0.28 | 1.00 | 1336 | quarters: 0.00 → 0.00 → 0.00 → 0.00

Numbers say: light vs heavy: width 31.5 → 40.0 px, dark 0.18 → 0.35; the long stroke does not run out of paint.

## Oil · Henry Ward · Thin veil
Oil 0.81 · Ink 0.19 · 56 px · 39.7 s

![Oil · Henry Ward · Thin veil](Oil-Henry-Ward-Thin-veil.png)

A light paint: laid on a grey sheet (on white it cannot be seen); **dark** = how far it is from the grey either way.

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 17 % → 13 % | 49.9 px | 0.16 | 0.77 | 370 |
| heavy line | 16 % → 13 % | 47.7 px | 0.16 | 0.81 | 403 |
| pressure swell | 13 % → 12 % | 47.5 px | 0.21 | 0.94 | 183 |
| fast wave | 35 % → 18 % | 40.5 px | 0.09 | 0.52 | 536 |
| slow wave | 36 % → 28 % | 41.0 px | 0.20 | 0.79 | 1223 |
| spiral | 58 % → 53 % | 38.1 px | 0.13 | 0.91 | 1277 |
| loop | 38 % → 32 % | 49.5 px | 0.15 | 0.83 | 639 |
| tilted | 15 % → 15 % | 40.8 px | 0.17 | 1.02 | 246 |
| over the wet one | 22 % → 20 % | 20.5 px | 0.17 | 0.93 | 184 |
| long, no reload | 65 % → 56 % | 28.9 px | 0.14 | 0.87 | 1178 | quarters: 0.01 → 0.01 → 0.01 → 0.01

Numbers say: light vs heavy: width 49.9 → 47.7 px, dark 0.16 → 0.16; pressure barely changes the width; the long stroke does not run out of paint.

## Oil · Henry Ward · Ground
Gouache 1.00 · 160 px · 78.5 s

![Oil · Henry Ward · Ground](Oil-Henry-Ward-Ground.png)

A light paint: laid on a grey sheet (on white it cannot be seen); **dark** = how far it is from the grey either way.

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 51 % → 46 % | 148.6 px | 0.36 | 0.90 | 1159 |
| heavy line | 52 % → 46 % | 150.6 px | 0.36 | 0.89 | 935 |
| pressure swell | 42 % → 45 % | 158.1 px | 0.36 | 1.06 | 726 |
| fast wave | 83 % → 83 % | 96.2 px | 0.36 | 1.00 | 2852 |
| slow wave | 85 % → 70 % | 98.5 px | 0.36 | 0.82 | 3226 |
| spiral | 91 % → 78 % | 60.3 px | 0.36 | 0.86 | 5400 |
| loop | 76 % → 69 % | 98.1 px | 0.36 | 0.91 | 2228 |
| tilted | 38 % → 38 % | 105.0 px | 0.36 | 1.00 | 1178 |
| over the wet one | 76 % → 69 % | 105.8 px | 0.36 | 0.92 | 979 |
| long, no reload | 96 % → 81 % | 43.0 px | 0.36 | 0.85 | 5309 | quarters: 0.00 → 0.00 → 0.00 → 0.01

Numbers say: light vs heavy: width 148.6 → 150.6 px, dark 0.36 → 0.36; pressure barely changes the width.

## Oil · Henry Ward · HW #02 cream over wet olive
Oil 0.81 · Ink 0.19 · 56 px · 37.6 s

![Oil · Henry Ward · HW #02 cream over wet olive](Oil-Henry-Ward-HW-02-cream-over-wet-olive.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 17 % → 13 % | 49.9 px | 0.64 | 0.77 | 246 |
| heavy line | 16 % → 13 % | 47.7 px | 0.64 | 0.81 | 323 |
| pressure swell | 13 % → 12 % | 47.5 px | 0.66 | 0.94 | 177 |
| fast wave | 35 % → 18 % | 40.5 px | 0.61 | 0.52 | 1124 |
| slow wave | 36 % → 28 % | 41.0 px | 0.65 | 0.79 | 1381 |
| spiral | 58 % → 53 % | 38.1 px | 0.65 | 0.91 | 1270 |
| loop | 38 % → 32 % | 49.5 px | 0.65 | 0.83 | 565 |
| tilted | 15 % → 15 % | 40.8 px | 0.65 | 1.02 | 308 |
| over the wet one | 22 % → 20 % | 20.5 px | 0.65 | 0.93 | 237 |
| long, no reload | 65 % → 56 % | 28.9 px | 0.64 | 0.87 | 1462 | quarters: 0.40 → 0.47 → 0.45 → 0.26

Numbers say: light vs heavy: width 49.9 → 47.7 px, dark 0.64 → 0.64; pressure barely changes the width.

## Oil · Henry Ward · HW #04 grey arcs over ochre
Oil 1.00 · 46 px · 16.0 s

![Oil · Henry Ward · HW #04 grey arcs over ochre](Oil-Henry-Ward-HW-04-grey-arcs-over-ochre.png)

A light paint: laid on a grey sheet (on white it cannot be seen); **dark** = how far it is from the grey either way.

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 14 % → 14 % | 40.2 px | 0.21 | 1.00 | 150 |
| heavy line | 12 % → 12 % | 35.5 px | 0.26 | 1.00 | 179 |
| pressure swell | 11 % → 11 % | 39.6 px | 0.25 | 1.00 | 127 |
| fast wave | 34 % → 34 % | 38.9 px | 0.18 | 1.00 | 431 |
| slow wave | 29 % → 29 % | 34.1 px | 0.23 | 1.00 | 739 |
| spiral | 50 % → 50 % | 32.9 px | 0.23 | 1.00 | 701 |
| loop | 28 % → 28 % | 35.7 px | 0.25 | 1.00 | 461 |
| tilted | 13 % → 13 % | 36.8 px | 0.25 | 1.00 | 351 |
| over the wet one | 25 % → 25 % | 32.9 px | 0.25 | 1.00 | 306 |
| long, no reload | 56 % → 56 % | 25.2 px | 0.22 | 1.00 | 1164 | quarters: 0.00 → 0.00 → 0.00 → 0.00

Numbers say: light vs heavy: width 40.2 → 35.5 px, dark 0.21 → 0.26; the long stroke does not run out of paint.

## Oil · Henry Ward · HW #09 white arches over wet blue-grey
Oil 1.00 · 46 px · 15.6 s

![Oil · Henry Ward · HW #09 white arches over wet blue-grey](Oil-Henry-Ward-HW-09-white-arches-over-wet-blue-grey.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 14 % → 14 % | 40.2 px | 0.31 | 1.00 | 147 |
| heavy line | 12 % → 12 % | 35.5 px | 0.37 | 1.00 | 162 |
| pressure swell | 11 % → 11 % | 39.6 px | 0.39 | 1.00 | 116 |
| fast wave | 34 % → 34 % | 38.9 px | 0.27 | 1.00 | 410 |
| slow wave | 29 % → 29 % | 34.1 px | 0.33 | 1.00 | 708 |
| spiral | 50 % → 50 % | 32.9 px | 0.34 | 1.00 | 1028 |
| loop | 28 % → 28 % | 35.7 px | 0.37 | 1.00 | 529 |
| tilted | 13 % → 13 % | 36.8 px | 0.36 | 1.00 | 213 |
| over the wet one | 25 % → 25 % | 32.9 px | 0.36 | 1.00 | 158 |
| long, no reload | 56 % → 56 % | 25.2 px | 0.33 | 1.00 | 1060 | quarters: 0.26 → 0.25 → 0.17 → 0.13

Numbers say: light vs heavy: width 40.2 → 35.5 px, dark 0.31 → 0.37.

## Oil · Henry Ward · HW #03 navy contours over wet band
Oil 1.00 · 46 px · 17.3 s

![Oil · Henry Ward · HW #03 navy contours over wet band](Oil-Henry-Ward-HW-03-navy-contours-over-wet-band.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 14 % → 14 % | 40.2 px | 0.33 | 1.00 | 143 |
| heavy line | 12 % → 12 % | 35.5 px | 0.39 | 1.00 | 161 |
| pressure swell | 11 % → 11 % | 39.6 px | 0.41 | 1.00 | 217 |
| fast wave | 34 % → 34 % | 38.9 px | 0.29 | 1.00 | 654 |
| slow wave | 29 % → 29 % | 34.1 px | 0.35 | 1.00 | 810 |
| spiral | 50 % → 50 % | 32.9 px | 0.36 | 1.00 | 704 |
| loop | 28 % → 28 % | 35.7 px | 0.39 | 1.00 | 386 |
| tilted | 13 % → 13 % | 36.8 px | 0.38 | 1.00 | 196 |
| over the wet one | 25 % → 25 % | 32.9 px | 0.38 | 1.00 | 169 |
| long, no reload | 56 % → 56 % | 25.2 px | 0.35 | 1.00 | 1015 | quarters: 0.28 → 0.26 → 0.18 → 0.14

Numbers say: light vs heavy: width 40.2 → 35.5 px, dark 0.33 → 0.39.

## Oil · Henry Ward · Ground #2b2f1c
Gouache 1.00 · 160 px · 71.2 s

![Oil · Henry Ward · Ground #2b2f1c](Oil-Henry-Ward-Ground-2b2f1c.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 51 % → 46 % | 148.6 px | 0.51 | 0.90 | 1524 |
| heavy line | 52 % → 46 % | 150.6 px | 0.51 | 0.89 | 817 |
| pressure swell | 42 % → 45 % | 158.1 px | 0.51 | 1.06 | 523 |
| fast wave | 83 % → 83 % | 96.2 px | 0.51 | 1.00 | 2153 |
| slow wave | 85 % → 70 % | 98.5 px | 0.51 | 0.82 | 3143 |
| spiral | 91 % → 78 % | 60.3 px | 0.51 | 0.86 | 3159 |
| loop | 76 % → 69 % | 98.1 px | 0.51 | 0.91 | 1639 |
| tilted | 38 % → 38 % | 105.0 px | 0.51 | 1.00 | 1132 |
| over the wet one | 76 % → 69 % | 105.8 px | 0.51 | 0.92 | 744 |
| long, no reload | 96 % → 81 % | 43.0 px | 0.51 | 0.85 | 4512 | quarters: 0.51 → 0.51 → 0.50 → 0.46

Numbers say: light vs heavy: width 148.6 → 150.6 px, dark 0.51 → 0.51; pressure barely changes the width; the long stroke does not run out of paint.

## Oil · Henry Ward · Thin veil #2b3a44
Oil 0.81 · Ink 0.19 · 56 px · 31.8 s

![Oil · Henry Ward · Thin veil #2b3a44](Oil-Henry-Ward-Thin-veil-2b3a44.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 17 % → 13 % | 49.9 px | 0.64 | 0.77 | 193 |
| heavy line | 16 % → 13 % | 47.7 px | 0.64 | 0.81 | 217 |
| pressure swell | 13 % → 12 % | 47.5 px | 0.66 | 0.94 | 146 |
| fast wave | 35 % → 18 % | 40.5 px | 0.61 | 0.52 | 731 |
| slow wave | 36 % → 28 % | 41.0 px | 0.65 | 0.79 | 877 |
| spiral | 58 % → 53 % | 38.1 px | 0.65 | 0.91 | 853 |
| loop | 38 % → 32 % | 49.5 px | 0.65 | 0.83 | 480 |
| tilted | 15 % → 15 % | 40.8 px | 0.65 | 1.02 | 329 |
| over the wet one | 22 % → 20 % | 20.5 px | 0.65 | 0.93 | 254 |
| long, no reload | 65 % → 56 % | 28.9 px | 0.64 | 0.87 | 1220 | quarters: 0.40 → 0.47 → 0.45 → 0.26

Numbers say: light vs heavy: width 49.9 → 47.7 px, dark 0.64 → 0.64; pressure barely changes the width.

## Oil · Henry Ward · Loaded flat #ece6c0
Oil 1.00 · 46 px · 16.2 s

![Oil · Henry Ward · Loaded flat #ece6c0](Oil-Henry-Ward-Loaded-flat-ece6c0.png)

A light paint: laid on a grey sheet (on white it cannot be seen); **dark** = how far it is from the grey either way.

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 14 % → 14 % | 40.2 px | 0.31 | 1.00 | 151 |
| heavy line | 12 % → 12 % | 35.5 px | 0.37 | 1.00 | 175 |
| pressure swell | 11 % → 11 % | 39.6 px | 0.37 | 1.00 | 118 |
| fast wave | 34 % → 34 % | 38.9 px | 0.26 | 1.00 | 416 |
| slow wave | 29 % → 29 % | 34.1 px | 0.33 | 1.00 | 935 |
| spiral | 50 % → 50 % | 32.9 px | 0.33 | 1.00 | 894 |
| loop | 28 % → 28 % | 35.7 px | 0.36 | 1.00 | 364 |
| tilted | 13 % → 13 % | 36.8 px | 0.36 | 1.00 | 194 |
| over the wet one | 25 % → 25 % | 32.9 px | 0.36 | 1.00 | 165 |
| long, no reload | 56 % → 56 % | 25.2 px | 0.32 | 1.00 | 1023 | quarters: 0.00 → 0.00 → 0.00 → 0.00

Numbers say: light vs heavy: width 40.2 → 35.5 px, dark 0.31 → 0.37; the long stroke does not run out of paint.

## Oil · Henry Ward · Dry scrub #ece6c0
Oil 1.00 · 50 px · 15.9 s

![Oil · Henry Ward · Dry scrub #ece6c0](Oil-Henry-Ward-Dry-scrub-ece6c0.png)

A light paint: laid on a grey sheet (on white it cannot be seen); **dark** = how far it is from the grey either way.

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 10 % → 10 % | 28.4 px | 0.16 | 1.00 | 160 |
| heavy line | 9 % → 9 % | 25.6 px | 0.21 | 1.00 | 173 |
| pressure swell | 9 % → 9 % | 32.3 px | 0.29 | 1.00 | 132 |
| fast wave | 24 % → 25 % | 28.2 px | 0.16 | 1.01 | 427 |
| slow wave | 19 % → 19 % | 22.5 px | 0.23 | 1.00 | 714 |
| spiral | 51 % → 51 % | 33.3 px | 0.26 | 1.00 | 737 |
| loop | 31 % → 31 % | 39.9 px | 0.29 | 1.00 | 415 |
| tilted | 12 % → 12 % | 32.1 px | 0.24 | 1.00 | 213 |
| over the wet one | 17 % → 17 % | 16.5 px | 0.24 | 1.00 | 160 |
| long, no reload | 52 % → 52 % | 23.3 px | 0.24 | 1.00 | 1264 | quarters: 0.00 → 0.00 → 0.00 → 0.00

Numbers say: light vs heavy: width 28.4 → 25.6 px, dark 0.16 → 0.21; the long stroke does not run out of paint.

## Oil · Henry Ward · Ground #8a6a20
Gouache 1.00 · 160 px · 74.7 s

![Oil · Henry Ward · Ground #8a6a20](Oil-Henry-Ward-Ground-8a6a20.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 51 % → 46 % | 148.6 px | 0.32 | 0.90 | 689 |
| heavy line | 52 % → 46 % | 150.6 px | 0.32 | 0.89 | 1069 |
| pressure swell | 42 % → 45 % | 158.1 px | 0.32 | 1.06 | 704 |
| fast wave | 83 % → 83 % | 96.2 px | 0.32 | 1.00 | 2023 |
| slow wave | 85 % → 70 % | 98.5 px | 0.32 | 0.82 | 3179 |
| spiral | 91 % → 78 % | 60.3 px | 0.32 | 0.86 | 3581 |
| loop | 76 % → 69 % | 98.1 px | 0.32 | 0.91 | 1896 |
| tilted | 38 % → 38 % | 105.0 px | 0.32 | 1.00 | 886 |
| over the wet one | 76 % → 69 % | 105.8 px | 0.32 | 0.92 | 761 |
| long, no reload | 96 % → 81 % | 43.0 px | 0.31 | 0.85 | 4786 | quarters: 0.32 → 0.32 → 0.31 → 0.26

Numbers say: light vs heavy: width 148.6 → 150.6 px, dark 0.32 → 0.32; pressure barely changes the width.

## Oil · Henry Ward · Loaded flat #b8bcc0
Oil 1.00 · 46 px · 15.7 s

![Oil · Henry Ward · Loaded flat #b8bcc0](Oil-Henry-Ward-Loaded-flat-b8bcc0.png)

A light paint: laid on a grey sheet (on white it cannot be seen); **dark** = how far it is from the grey either way.

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 14 % → 14 % | 40.2 px | 0.21 | 1.00 | 144 |
| heavy line | 12 % → 12 % | 35.5 px | 0.26 | 1.00 | 168 |
| pressure swell | 11 % → 11 % | 39.6 px | 0.25 | 1.00 | 116 |
| fast wave | 34 % → 34 % | 38.9 px | 0.18 | 1.00 | 494 |
| slow wave | 29 % → 29 % | 34.1 px | 0.23 | 1.00 | 711 |
| spiral | 50 % → 50 % | 32.9 px | 0.23 | 1.00 | 673 |
| loop | 28 % → 28 % | 35.7 px | 0.25 | 1.00 | 362 |
| tilted | 13 % → 13 % | 36.8 px | 0.25 | 1.00 | 192 |
| over the wet one | 25 % → 25 % | 32.9 px | 0.25 | 1.00 | 160 |
| long, no reload | 56 % → 56 % | 25.2 px | 0.22 | 1.00 | 1238 | quarters: 0.00 → 0.00 → 0.00 → 0.00

Numbers say: light vs heavy: width 40.2 → 35.5 px, dark 0.21 → 0.26; the long stroke does not run out of paint.

## Oil · Henry Ward · Dry scrub #c8ccd0
Oil 1.00 · 50 px · 17.2 s

![Oil · Henry Ward · Dry scrub #c8ccd0](Oil-Henry-Ward-Dry-scrub-c8ccd0.png)

A light paint: laid on a grey sheet (on white it cannot be seen); **dark** = how far it is from the grey either way.

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 10 % → 10 % | 28.4 px | 0.12 | 1.00 | 158 |
| heavy line | 9 % → 9 % | 25.6 px | 0.16 | 1.00 | 172 |
| pressure swell | 9 % → 9 % | 32.3 px | 0.24 | 1.00 | 129 |
| fast wave | 24 % → 25 % | 28.2 px | 0.12 | 1.01 | 430 |
| slow wave | 19 % → 19 % | 22.5 px | 0.18 | 1.00 | 800 |
| spiral | 51 % → 51 % | 33.3 px | 0.21 | 1.00 | 973 |
| loop | 31 % → 31 % | 39.9 px | 0.23 | 1.00 | 435 |
| tilted | 12 % → 12 % | 32.1 px | 0.19 | 1.00 | 212 |
| over the wet one | 17 % → 17 % | 16.5 px | 0.19 | 1.00 | 158 |
| long, no reload | 52 % → 52 % | 23.3 px | 0.19 | 1.00 | 1099 | quarters: 0.00 → 0.00 → 0.00 → 0.00

Numbers say: light vs heavy: width 28.4 → 25.6 px, dark 0.12 → 0.16; the long stroke does not run out of paint.

## Oil · Henry Ward · Wet drag #9ea4aa
Oil 1.00 · 44 px · 17.5 s

![Oil · Henry Ward · Wet drag #9ea4aa](Oil-Henry-Ward-Wet-drag-9ea4aa.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 11 % → 11 % | 31.5 px | 0.11 | 1.00 | 204 |
| heavy line | 14 % → 14 % | 40.0 px | 0.23 | 1.00 | 327 |
| pressure swell | 11 % → 11 % | 40.4 px | 0.22 | 1.00 | 192 |
| fast wave | 30 % → 30 % | 34.3 px | 0.15 | 1.00 | 917 |
| slow wave | 29 % → 29 % | 34.0 px | 0.19 | 1.00 | 801 |
| spiral | 50 % → 50 % | 33.1 px | 0.18 | 1.00 | 697 |
| loop | 30 % → 30 % | 38.7 px | 0.21 | 1.00 | 372 |
| tilted | 13 % → 13 % | 35.0 px | 0.21 | 1.00 | 240 |
| over the wet one | 24 % → 24 % | 31.6 px | 0.21 | 1.00 | 203 |
| long, no reload | 61 % → 61 % | 27.4 px | 0.19 | 1.00 | 1045 | quarters: 0.16 → 0.15 → 0.10 → 0.10

Numbers say: light vs heavy: width 31.5 → 40.0 px, dark 0.11 → 0.23.

## Oil · Henry Ward · Ground #e8b4a8
Gouache 1.00 · 160 px · 71.2 s

![Oil · Henry Ward · Ground #e8b4a8](Oil-Henry-Ward-Ground-e8b4a8.png)

A light paint: laid on a grey sheet (on white it cannot be seen); **dark** = how far it is from the grey either way.

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 51 % → 46 % | 148.6 px | 0.30 | 0.90 | 669 |
| heavy line | 52 % → 46 % | 150.6 px | 0.30 | 0.89 | 745 |
| pressure swell | 42 % → 45 % | 158.1 px | 0.30 | 1.06 | 597 |
| fast wave | 83 % → 83 % | 96.2 px | 0.30 | 1.00 | 1793 |
| slow wave | 85 % → 70 % | 98.5 px | 0.30 | 0.82 | 3375 |
| spiral | 91 % → 78 % | 60.3 px | 0.30 | 0.86 | 3548 |
| loop | 76 % → 69 % | 98.1 px | 0.30 | 0.91 | 1823 |
| tilted | 38 % → 38 % | 105.0 px | 0.30 | 1.00 | 868 |
| over the wet one | 76 % → 69 % | 105.8 px | 0.30 | 0.92 | 1026 |
| long, no reload | 96 % → 81 % | 43.0 px | 0.29 | 0.85 | 4680 | quarters: 0.00 → 0.00 → 0.00 → 0.00

Numbers say: light vs heavy: width 148.6 → 150.6 px, dark 0.30 → 0.30; pressure barely changes the width.

## Oil · Henry Ward · Loaded flat #6e7f90
Oil 1.00 · 46 px · 16.1 s

![Oil · Henry Ward · Loaded flat #6e7f90](Oil-Henry-Ward-Loaded-flat-6e7f90.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 14 % → 14 % | 40.2 px | 0.31 | 1.00 | 166 |
| heavy line | 12 % → 12 % | 35.5 px | 0.37 | 1.00 | 251 |
| pressure swell | 11 % → 11 % | 39.6 px | 0.39 | 1.00 | 139 |
| fast wave | 34 % → 34 % | 38.9 px | 0.27 | 1.00 | 438 |
| slow wave | 29 % → 29 % | 34.1 px | 0.33 | 1.00 | 733 |
| spiral | 50 % → 50 % | 32.9 px | 0.34 | 1.00 | 694 |
| loop | 28 % → 28 % | 35.7 px | 0.37 | 1.00 | 447 |
| tilted | 13 % → 13 % | 36.8 px | 0.36 | 1.00 | 239 |
| over the wet one | 25 % → 25 % | 32.9 px | 0.36 | 1.00 | 158 |
| long, no reload | 56 % → 56 % | 25.2 px | 0.33 | 1.00 | 1006 | quarters: 0.26 → 0.25 → 0.17 → 0.13

Numbers say: light vs heavy: width 40.2 → 35.5 px, dark 0.31 → 0.37.

## Oil · Henry Ward · Loaded flat #f6f6f2
Oil 1.00 · 46 px · 15.7 s

![Oil · Henry Ward · Loaded flat #f6f6f2](Oil-Henry-Ward-Loaded-flat-f6f6f2.png)

A light paint: laid on a grey sheet (on white it cannot be seen); **dark** = how far it is from the grey either way.

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 14 % → 14 % | 40.2 px | 0.34 | 1.00 | 144 |
| heavy line | 12 % → 12 % | 35.5 px | 0.41 | 1.00 | 178 |
| pressure swell | 11 % → 11 % | 39.6 px | 0.40 | 1.00 | 116 |
| fast wave | 34 % → 34 % | 38.9 px | 0.30 | 1.00 | 406 |
| slow wave | 29 % → 29 % | 34.1 px | 0.37 | 1.00 | 732 |
| spiral | 50 % → 50 % | 32.9 px | 0.36 | 1.00 | 691 |
| loop | 28 % → 28 % | 35.7 px | 0.40 | 1.00 | 363 |
| tilted | 13 % → 13 % | 36.8 px | 0.39 | 1.00 | 263 |
| over the wet one | 25 % → 25 % | 32.9 px | 0.39 | 1.00 | 209 |
| long, no reload | 56 % → 56 % | 25.2 px | 0.35 | 1.00 | 1454 | quarters: 0.00 → 0.00 → 0.00 → 0.00

Numbers say: light vs heavy: width 40.2 → 35.5 px, dark 0.34 → 0.41; the long stroke does not run out of paint.

## Oil · Henry Ward · Dry scrub #f6f6f2
Oil 1.00 · 50 px · 16.2 s

![Oil · Henry Ward · Dry scrub #f6f6f2](Oil-Henry-Ward-Dry-scrub-f6f6f2.png)

A light paint: laid on a grey sheet (on white it cannot be seen); **dark** = how far it is from the grey either way.

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 10 % → 10 % | 28.4 px | 0.19 | 1.00 | 214 |
| heavy line | 9 % → 9 % | 25.6 px | 0.24 | 1.00 | 305 |
| pressure swell | 9 % → 9 % | 32.3 px | 0.32 | 1.00 | 188 |
| fast wave | 24 % → 25 % | 28.2 px | 0.19 | 1.01 | 544 |
| slow wave | 19 % → 19 % | 22.5 px | 0.26 | 1.00 | 725 |
| spiral | 51 % → 51 % | 33.3 px | 0.29 | 1.00 | 759 |
| loop | 31 % → 31 % | 39.9 px | 0.32 | 1.00 | 418 |
| tilted | 12 % → 12 % | 32.1 px | 0.27 | 1.00 | 210 |
| over the wet one | 17 % → 17 % | 16.5 px | 0.27 | 1.00 | 157 |
| long, no reload | 52 % → 52 % | 23.3 px | 0.27 | 1.00 | 1143 | quarters: 0.00 → 0.00 → 0.00 → 0.00

Numbers say: light vs heavy: width 28.4 → 25.6 px, dark 0.19 → 0.24; the long stroke does not run out of paint.

## Oil · Henry Ward · Ground #e8e2da
Gouache 1.00 · 160 px · 72.1 s

![Oil · Henry Ward · Ground #e8e2da](Oil-Henry-Ward-Ground-e8e2da.png)

A light paint: laid on a grey sheet (on white it cannot be seen); **dark** = how far it is from the grey either way.

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 51 % → 46 % | 148.6 px | 0.38 | 0.90 | 690 |
| heavy line | 52 % → 46 % | 150.6 px | 0.38 | 0.89 | 1075 |
| pressure swell | 42 % → 45 % | 158.1 px | 0.38 | 1.06 | 548 |
| fast wave | 83 % → 83 % | 96.2 px | 0.38 | 1.00 | 1832 |
| slow wave | 85 % → 70 % | 98.5 px | 0.37 | 0.82 | 3191 |
| spiral | 91 % → 78 % | 60.3 px | 0.37 | 0.86 | 3780 |
| loop | 76 % → 69 % | 98.1 px | 0.38 | 0.91 | 1788 |
| tilted | 38 % → 38 % | 105.0 px | 0.38 | 1.00 | 1056 |
| over the wet one | 76 % → 69 % | 105.8 px | 0.38 | 0.92 | 1258 |
| long, no reload | 96 % → 81 % | 43.0 px | 0.37 | 0.85 | 4603 | quarters: 0.00 → 0.00 → 0.00 → 0.01

Numbers say: light vs heavy: width 148.6 → 150.6 px, dark 0.38 → 0.38; pressure barely changes the width.

## Oil · Henry Ward · Loaded flat #6a7a80
Oil 1.00 · 46 px · 15.5 s

![Oil · Henry Ward · Loaded flat #6a7a80](Oil-Henry-Ward-Loaded-flat-6a7a80.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 14 % → 14 % | 40.2 px | 0.33 | 1.00 | 155 |
| heavy line | 12 % → 12 % | 35.5 px | 0.39 | 1.00 | 164 |
| pressure swell | 11 % → 11 % | 39.6 px | 0.41 | 1.00 | 124 |
| fast wave | 34 % → 34 % | 38.9 px | 0.29 | 1.00 | 418 |
| slow wave | 29 % → 29 % | 34.1 px | 0.35 | 1.00 | 728 |
| spiral | 50 % → 50 % | 32.9 px | 0.36 | 1.00 | 687 |
| loop | 28 % → 28 % | 35.7 px | 0.39 | 1.00 | 376 |
| tilted | 13 % → 13 % | 36.8 px | 0.38 | 1.00 | 197 |
| over the wet one | 25 % → 25 % | 32.9 px | 0.38 | 1.00 | 165 |
| long, no reload | 56 % → 56 % | 25.2 px | 0.35 | 1.00 | 1029 | quarters: 0.28 → 0.26 → 0.18 → 0.14

Numbers say: light vs heavy: width 40.2 → 35.5 px, dark 0.33 → 0.39.

## Oil · Henry Ward · Loaded flat #5a1810
Oil 1.00 · 46 px · 17.0 s

![Oil · Henry Ward · Loaded flat #5a1810](Oil-Henry-Ward-Loaded-flat-5a1810.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 14 % → 14 % | 40.2 px | 0.72 | 1.00 | 252 |
| heavy line | 12 % → 12 % | 35.5 px | 0.75 | 1.00 | 281 |
| pressure swell | 11 % → 11 % | 39.6 px | 0.77 | 1.00 | 202 |
| fast wave | 34 % → 34 % | 38.9 px | 0.71 | 1.00 | 686 |
| slow wave | 29 % → 29 % | 34.1 px | 0.74 | 1.00 | 1073 |
| spiral | 50 % → 50 % | 32.9 px | 0.75 | 1.00 | 918 |
| loop | 28 % → 28 % | 35.7 px | 0.76 | 1.00 | 367 |
| tilted | 13 % → 13 % | 36.8 px | 0.75 | 1.00 | 194 |
| over the wet one | 25 % → 25 % | 32.9 px | 0.75 | 1.00 | 157 |
| long, no reload | 56 % → 56 % | 25.2 px | 0.74 | 1.00 | 999 | quarters: 0.54 → 0.54 → 0.41 → 0.33

Numbers say: light vs heavy: width 40.2 → 35.5 px, dark 0.72 → 0.75.

## Oil · Henry Ward · Dirty contour #1c2240
Oil 1.00 · 24 px · 13.3 s

![Oil · Henry Ward · Dirty contour #1c2240](Oil-Henry-Ward-Dirty-contour-1c2240.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 8 % → 8 % | 24.1 px | 0.73 | 1.00 | 127 |
| heavy line | 9 % → 9 % | 25.3 px | 0.74 | 1.00 | 134 |
| pressure swell | 7 % → 7 % | 25.8 px | 0.77 | 1.00 | 98 |
| fast wave | 19 % → 19 % | 22.1 px | 0.75 | 1.00 | 251 |
| slow wave | 22 % → 22 % | 24.9 px | 0.76 | 1.00 | 417 |
| spiral | 32 % → 32 % | 21.2 px | 0.74 | 1.00 | 429 |
| loop | 18 % → 18 % | 22.9 px | 0.76 | 1.00 | 216 |
| tilted | 9 % → 9 % | 25.4 px | 0.76 | 1.00 | 118 |
| over the wet one | 17 % → 17 % | 23.0 px | 0.76 | 1.00 | 107 |
| long, no reload | 39 % → 39 % | 17.4 px | 0.73 | 1.00 | 628 | quarters: 0.42 → 0.35 → 0.28 → 0.22

Numbers say: light vs heavy: width 24.1 → 25.3 px, dark 0.73 → 0.74; pressure barely changes the width.

## Brush Artist · Refs · #01 Henry Ward peach cloud — own sheet
own sheet 600 × 600 · Gouache 1.00 · 44 px · 12.9 s

![Brush Artist · Refs · #01 Henry Ward peach cloud — own sheet](Brush-Artist-Refs-01-Henry-Ward-peach-cloud-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 11 % → 21 % | 32.7 px | 0.55 | 1.80 | 286 |
| stroke 2 | 16 % → 34 % | 51.4 px | 0.55 | 2.20 | 155 |
| stroke 3 | 18 % → 33 % | 53.1 px | 0.55 | 1.81 | 134 |
| stroke 4 | 21 % → 38 % | 67.1 px | 0.55 | 1.85 | 141 |
| stroke 5 | 22 % → 36 % | 62.7 px | 0.55 | 1.66 | 143 |
| stroke 6 | 22 % → 28 % | 68.5 px | 0.55 | 1.25 | 134 |
| stroke 7 | 17 % → 46 % | 43.1 px | 0.55 | 2.64 | 149 |
| stroke 8 | 18 % → 43 % | 45.7 px | 0.55 | 2.36 | 148 |
| stroke 9 | 22 % → 44 % | 55.4 px | 0.55 | 2.05 | 138 |
| stroke 10 | 21 % → 45 % | 56.2 px | 0.55 | 2.14 | 146 |
| stroke 11 | 21 % → 48 % | 60.3 px | 0.55 | 2.24 | 140 |
| stroke 12 | 22 % → 50 % | 65.8 px | 0.55 | 2.29 | 126 |
| stroke 13 | 27 % → 52 % | 78.5 px | 0.55 | 1.91 | 133 |
| stroke 14 | 36 % → 53 % | 103.2 px | 0.55 | 1.46 | 187 |
| stroke 15 | 48 % → 55 % | 142.6 px | 0.55 | 1.14 | 197 |
| stroke 16 | 49 % → 55 % | 148.3 px | 0.55 | 1.13 | 171 |
| stroke 17 | 50 % → 57 % | 139.6 px | 0.55 | 1.14 | 183 |
| stroke 18 | 48 % → 56 % | 139.8 px | 0.55 | 1.16 | 162 |
| stroke 19 | 51 % → 54 % | 143.8 px | 0.55 | 1.05 | 149 |
| stroke 20 | 52 % → 51 % | 149.9 px | 0.55 | 0.98 | 163 |
| stroke 21 | 51 % → 47 % | 146.9 px | 0.55 | 0.93 | 145 |
| stroke 22 | 53 % → 48 % | 155.8 px | 0.55 | 0.90 | 166 |
| stroke 23 | 51 % → 45 % | 145.0 px | 0.55 | 0.88 | 139 |
| stroke 24 | 53 % → 46 % | 159.0 px | 0.55 | 0.87 | 113 |

Numbers say: wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #02 Henry Ward cream strokes — own sheet
own sheet 600 × 600 · Gouache 1.00 · 46 px · 7.2 s

![Brush Artist · Refs · #02 Henry Ward cream strokes — own sheet](Brush-Artist-Refs-02-Henry-Ward-cream-strokes-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 16 % → 9 % | 33.4 px | 0.63 | 0.56 | 303 |
| stroke 2 | 20 % → 11 % | 53.2 px | 0.64 | 0.54 | 198 |
| stroke 3 | 21 % → 17 % | 52.6 px | 0.63 | 0.83 | 204 |
| stroke 4 | 24 % → 17 % | 60.3 px | 0.63 | 0.71 | 216 |
| stroke 5 | 25 % → 20 % | 62.4 px | 0.63 | 0.79 | 203 |
| stroke 6 | 18 % → 21 % | 44.7 px | 0.62 | 1.14 | 196 |
| stroke 7 | 26 % → 15 % | 65.2 px | 0.61 | 0.59 | 207 |

## Brush Artist · Refs · #03 Henry Ward navy contours — own sheet
own sheet 600 × 600 · Impasto 1.00 · 22 px · 2.5 s

![Brush Artist · Refs · #03 Henry Ward navy contours — own sheet](Brush-Artist-Refs-03-Henry-Ward-navy-contours-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 10 % → 15 % | 20.4 px | 0.69 | 1.49 | 114 |
| stroke 2 | 18 % → 20 % | 25.6 px | 0.69 | 1.12 | 101 |
| stroke 3 | 21 % → 21 % | 30.7 px | 0.69 | 0.99 | 126 |
| stroke 4 | 20 % → 18 % | 45.1 px | 0.69 | 0.88 | 149 |

## Brush Artist · Refs · #04 Henry Ward grey cloud — own sheet
own sheet 600 × 600 · Gouache 1.00 · 50 px · 12.4 s

![Brush Artist · Refs · #04 Henry Ward grey cloud — own sheet](Brush-Artist-Refs-04-Henry-Ward-grey-cloud-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 12 % → 29 % | 35.6 px | 0.34 | 2.38 | 213 |
| stroke 2 | 16 % → 32 % | 45.1 px | 0.34 | 2.03 | 218 |
| stroke 3 | 24 % → 35 % | 67.9 px | 0.34 | 1.44 | 298 |
| stroke 4 | 26 % → 35 % | 74.4 px | 0.33 | 1.39 | 328 |
| stroke 5 | 29 % → 39 % | 89.2 px | 0.33 | 1.32 | 347 |
| stroke 6 | 37 % → 41 % | 120.7 px | 0.33 | 1.12 | 294 |
| stroke 7 | 44 % → 46 % | 127.9 px | 0.34 | 1.05 | 317 |
| stroke 8 | 40 % → 47 % | 119.7 px | 0.33 | 1.16 | 202 |
| stroke 9 | 35 % → 50 % | 105.5 px | 0.33 | 1.42 | 200 |
| stroke 10 | 41 % → 50 % | 131.1 px | 0.33 | 1.22 | 215 |
| stroke 11 | 38 % → 50 % | 108.9 px | 0.33 | 1.30 | 195 |
| stroke 12 | 41 % → 49 % | 123.5 px | 0.33 | 1.21 | 190 |
| stroke 13 | 35 % → 50 % | 99.6 px | 0.33 | 1.45 | 187 |
| stroke 14 | 40 % → 52 % | 120.4 px | 0.33 | 1.28 | 219 |
| stroke 15 | 39 % → 47 % | 113.1 px | 0.33 | 1.19 | 215 |
| stroke 16 | 38 % → 45 % | 115.2 px | 0.33 | 1.18 | 208 |
| stroke 17 | 36 % → 41 % | 103.9 px | 0.33 | 1.13 | 197 |
| stroke 18 | 37 % → 38 % | 121.2 px | 0.33 | 1.04 | 184 |
| stroke 19 | 40 % → 34 % | 120.3 px | 0.33 | 0.85 | 209 |
| stroke 20 | 43 % → 34 % | 136.3 px | 0.33 | 0.79 | 210 |

Numbers say: wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #05 Henry Ward green in rust loops — own sheet
own sheet 600 × 600 · Impasto 1.00 · 20 px · 2.3 s

![Brush Artist · Refs · #05 Henry Ward green in rust loops — own sheet](Brush-Artist-Refs-05-Henry-Ward-green-in-rust-loops-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 11 % → 18 % | 20.2 px | 0.02 | 1.55 | 149 |
| stroke 2 | 11 % → 11 % | 22.7 px | 0.02 | 0.92 | 151 |
| stroke 3 | 22 % → 20 % | 40.0 px | 0.02 | 0.91 | 129 |

Numbers say: wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #06 Henry Ward scrubbed grey — own sheet
own sheet 600 × 600 · Gouache 1.00 · 50 px · 13.0 s

![Brush Artist · Refs · #06 Henry Ward scrubbed grey — own sheet](Brush-Artist-Refs-06-Henry-Ward-scrubbed-grey-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 14 % → 27 % | 35.5 px | 0.33 | 1.88 | 200 |
| stroke 2 | 18 % → 31 % | 48.4 px | 0.33 | 1.70 | 203 |
| stroke 3 | 25 % → 31 % | 76.3 px | 0.33 | 1.25 | 197 |
| stroke 4 | 26 % → 30 % | 83.5 px | 0.33 | 1.14 | 202 |
| stroke 5 | 34 % → 39 % | 101.8 px | 0.33 | 1.15 | 194 |
| stroke 6 | 40 % → 38 % | 123.1 px | 0.33 | 0.94 | 205 |
| stroke 7 | 43 % → 40 % | 123.4 px | 0.33 | 0.93 | 219 |
| stroke 8 | 41 % → 41 % | 130.2 px | 0.33 | 1.01 | 194 |
| stroke 9 | 33 % → 44 % | 100.1 px | 0.33 | 1.35 | 192 |
| stroke 10 | 36 % → 46 % | 116.0 px | 0.33 | 1.29 | 194 |
| stroke 11 | 34 % → 48 % | 100.2 px | 0.33 | 1.41 | 213 |
| stroke 12 | 37 % → 48 % | 112.7 px | 0.33 | 1.29 | 221 |
| stroke 13 | 29 % → 50 % | 83.5 px | 0.33 | 1.68 | 204 |
| stroke 14 | 34 % → 49 % | 99.5 px | 0.33 | 1.43 | 219 |
| stroke 15 | 37 % → 53 % | 107.3 px | 0.33 | 1.43 | 219 |
| stroke 16 | 36 % → 55 % | 115.8 px | 0.33 | 1.53 | 226 |
| stroke 17 | 37 % → 50 % | 108.3 px | 0.32 | 1.37 | 225 |
| stroke 18 | 39 % → 48 % | 117.2 px | 0.32 | 1.24 | 202 |
| stroke 19 | 41 % → 48 % | 120.9 px | 0.32 | 1.18 | 212 |
| stroke 20 | 42 % → 46 % | 132.3 px | 0.32 | 1.08 | 213 |
| stroke 21 | 41 % → 39 % | 118.0 px | 0.32 | 0.96 | 205 |
| stroke 22 | 45 % → 34 % | 146.9 px | 0.32 | 0.77 | 208 |

Numbers say: wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #07 Henry Ward blue L + black zigzag — own sheet
own sheet 600 × 600 · Impasto 1.00 · 34 px · 2.5 s

![Brush Artist · Refs · #07 Henry Ward blue L + black zigzag — own sheet](Brush-Artist-Refs-07-Henry-Ward-blue-L-black-zigzag-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 14 % → 15 % | 32.4 px | 0.59 | 1.10 | 112 |
| stroke 2 | 16 % → 14 % | 38.8 px | 0.59 | 0.89 | 87 |

## Brush Artist · Refs · #08 Henry Ward olive bands — own sheet
own sheet 600 × 600 · Gouache 1.00 · 34 px · 5.0 s

![Brush Artist · Refs · #08 Henry Ward olive bands — own sheet](Brush-Artist-Refs-08-Henry-Ward-olive-bands-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 11 % → 7 % | 21.7 px | 0.58 | 0.64 | 172 |
| stroke 2 | 16 % → 7 % | 35.3 px | 0.58 | 0.47 | 168 |
| stroke 3 | 11 % → 10 % | 24.1 px | 0.58 | 0.85 | 173 |
| stroke 4 | 14 % → 9 % | 31.2 px | 0.58 | 0.59 | 182 |
| stroke 5 | 18 % → 11 % | 36.6 px | 0.58 | 0.60 | 180 |
| stroke 6 | 13 % → 4 % | 23.8 px | 0.58 | 0.36 | 177 |

## Brush Artist · Refs · #09 Henry Ward white loops — own sheet
own sheet 600 × 600 · Gouache 1.00 · 46 px · 6.3 s

![Brush Artist · Refs · #09 Henry Ward white loops — own sheet](Brush-Artist-Refs-09-Henry-Ward-white-loops-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 26 % → 0 % | 13.8 px | 0.00 | 0.00 | 963 |
| stroke 2 | 27 % → 0 % | 27.0 px | 0.06 | 0.00 | 1010 |
| stroke 3 | 33 % → 0 % | 31.0 px | 0.06 | 0.00 | 923 |
| stroke 4 | 4 % → 0 % | 10.0 px | 0.00 | 0.00 | 177 |
| stroke 5 | 2 % → 0 % | 4.5 px | 0.00 | 0.00 | 158 |
| stroke 6 | 5 % → 0 % | 12.8 px | 0.06 | 0.00 | 165 |
| stroke 7 | 13 % → 0 % | 34.9 px | 0.06 | 0.00 | 181 |
| stroke 8 | 7 % → 0 % | 11.4 px | 0.00 | 0.00 | 182 |

## Brush Artist · Refs · #10 Henry Ward maroon loops — own sheet
own sheet 600 × 600 · Impasto 1.00 · 30 px · 3.0 s

![Brush Artist · Refs · #10 Henry Ward maroon loops — own sheet](Brush-Artist-Refs-10-Henry-Ward-maroon-loops-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 11 % → 26 % | 26.6 px | 0.72 | 2.41 | 209 |
| stroke 2 | 21 % → 38 % | 46.3 px | 0.72 | 1.86 | 120 |
| stroke 3 | 28 % → 35 % | 55.8 px | 0.72 | 1.26 | 158 |
| stroke 4 | 39 % → 37 % | 87.7 px | 0.72 | 0.96 | 104 |
| stroke 5 | 32 % → 29 % | 80.8 px | 0.72 | 0.91 | 147 |

Numbers say: wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #11 Henry Ward purple spun balls — own sheet
own sheet 600 × 600 · Impasto 1.00 · 36 px · 2.9 s

![Brush Artist · Refs · #11 Henry Ward purple spun balls — own sheet](Brush-Artist-Refs-11-Henry-Ward-purple-spun-balls-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 24 % → 34 % | 26.4 px | 0.68 | 1.41 | 224 |
| stroke 2 | 35 % → 45 % | 38.0 px | 0.68 | 1.31 | 220 |
| stroke 3 | 35 % → 34 % | 38.9 px | 0.68 | 0.96 | 223 |

## Brush Artist · Refs · #12 Henry Ward black-olive cage — own sheet
own sheet 600 × 600 · Gouache 1.00 · 28 px · 5.3 s

![Brush Artist · Refs · #12 Henry Ward black-olive cage — own sheet](Brush-Artist-Refs-12-Henry-Ward-black-olive-cage-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 8 % → 10 % | 15.1 px | 0.59 | 1.30 | 223 |
| stroke 2 | 8 % → 11 % | 17.9 px | 0.59 | 1.40 | 183 |
| stroke 3 | 17 % → 14 % | 27.3 px | 0.59 | 0.79 | 227 |
| stroke 4 | 19 % → 14 % | 37.9 px | 0.59 | 0.76 | 136 |
| stroke 5 | 16 % → 9 % | 29.2 px | 0.59 | 0.53 | 139 |
| stroke 6 | 27 % → 15 % | 52.1 px | 0.59 | 0.55 | 174 |

## Brush Artist · Refs · #13 Henry Ward blue streaky form — own sheet
own sheet 600 × 600 · Gouache 1.00 · 50 px · 9.7 s

![Brush Artist · Refs · #13 Henry Ward blue streaky form — own sheet](Brush-Artist-Refs-13-Henry-Ward-blue-streaky-form-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 12 % → 0 % | 35.5 px | 0.00 | 0.00 | 198 |
| stroke 2 | 15 % → 0 % | 46.9 px | 0.00 | 0.00 | 219 |
| stroke 3 | 26 % → 0 % | 74.6 px | 0.00 | 0.00 | 296 |
| stroke 4 | 27 % → 0 % | 88.0 px | 0.00 | 0.00 | 253 |
| stroke 5 | 35 % → 0 % | 101.1 px | 0.00 | 0.00 | 275 |
| stroke 6 | 40 % → 0 % | 113.6 px | 0.00 | 0.00 | 280 |
| stroke 7 | 43 % → 0 % | 126.9 px | 0.00 | 0.00 | 313 |
| stroke 8 | 41 % → 0 % | 123.4 px | 0.00 | 0.00 | 217 |
| stroke 9 | 35 % → 0 % | 108.5 px | 0.00 | 0.00 | 176 |
| stroke 10 | 38 % → 0 % | 125.0 px | 0.00 | 0.00 | 188 |
| stroke 11 | 34 % → 0 % | 103.5 px | 0.00 | 0.00 | 187 |
| stroke 12 | 35 % → 0 % | 104.9 px | 0.00 | 0.00 | 194 |
| stroke 13 | 29 % → 0 % | 89.8 px | 0.00 | 0.00 | 167 |
| stroke 14 | 33 % → 0 % | 98.0 px | 0.00 | 0.00 | 214 |
| stroke 15 | 38 % → 0 % | 109.8 px | 0.00 | 0.00 | 212 |
| stroke 16 | 38 % → 0 % | 112.3 px | 0.00 | 0.00 | 194 |
| stroke 17 | 45 % → 0 % | 112.1 px | 0.00 | 0.00 | 195 |
| stroke 18 | 49 % → 0 % | 117.9 px | 0.00 | 0.00 | 196 |
| stroke 19 | 56 % → 0 % | 114.2 px | 0.00 | 0.00 | 206 |
| stroke 20 | 66 % → 0 % | 126.3 px | 0.00 | 0.00 | 226 |
| stroke 21 | 2 % → 0 % | 5.0 px | 0.00 | 0.00 | 149 |
| stroke 22 | 10 % → 0 % | 29.3 px | 0.00 | 0.00 | 186 |
| stroke 23 | 11 % → 0 % | 35.2 px | 0.00 | 0.00 | 148 |
| stroke 24 | 0 % → 0 % | 0.0 px | 0.00 | 1.00 | 183 |
| stroke 25 | 0 % → 0 % | 0.0 px | 0.00 | 1.00 | 166 |

## Brush Artist · Refs · #14 Henry Ward olive totem — own sheet
own sheet 600 × 600 · Impasto 1.00 · 48 px · 6.9 s

![Brush Artist · Refs · #14 Henry Ward olive totem — own sheet](Brush-Artist-Refs-14-Henry-Ward-olive-totem-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 18 % → 46 % | 46.2 px | 0.39 | 2.61 | 191 |
| stroke 2 | 21 % → 50 % | 64.3 px | 0.39 | 2.43 | 180 |
| stroke 3 | 29 % → 52 % | 100.4 px | 0.39 | 1.77 | 155 |
| stroke 4 | 30 % → 54 % | 112.7 px | 0.39 | 1.81 | 190 |
| stroke 5 | 39 % → 63 % | 134.8 px | 0.39 | 1.63 | 169 |
| stroke 6 | 39 % → 65 % | 150.1 px | 0.39 | 1.68 | 169 |
| stroke 7 | 37 % → 61 % | 123.4 px | 0.39 | 1.66 | 127 |
| stroke 8 | 37 % → 62 % | 141.3 px | 0.39 | 1.69 | 124 |
| stroke 9 | 37 % → 63 % | 129.0 px | 0.39 | 1.69 | 119 |
| stroke 10 | 38 % → 61 % | 140.5 px | 0.39 | 1.62 | 126 |
| stroke 11 | 40 % → 64 % | 143.3 px | 0.39 | 1.61 | 124 |
| stroke 12 | 38 % → 65 % | 143.4 px | 0.39 | 1.71 | 126 |
| stroke 13 | 38 % → 66 % | 134.3 px | 0.39 | 1.73 | 116 |
| stroke 14 | 37 % → 62 % | 134.1 px | 0.39 | 1.68 | 133 |
| stroke 15 | 40 % → 65 % | 136.4 px | 0.39 | 1.65 | 120 |
| stroke 16 | 38 % → 63 % | 137.2 px | 0.39 | 1.67 | 126 |
| stroke 17 | 37 % → 62 % | 124.9 px | 0.39 | 1.66 | 129 |
| stroke 18 | 40 % → 66 % | 154.4 px | 0.39 | 1.64 | 123 |
| stroke 19 | 39 % → 60 % | 137.5 px | 0.38 | 1.51 | 121 |
| stroke 20 | 40 % → 54 % | 142.7 px | 0.38 | 1.34 | 132 |
| stroke 21 | 46 % → 54 % | 136.3 px | 0.38 | 1.18 | 122 |
| stroke 22 | 54 % → 53 % | 146.1 px | 0.38 | 0.98 | 129 |

Numbers say: wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #15 Ultramarine brush script — own sheet
own sheet 600 × 600 · Ink 1.00 · 4 px · 8.3 s

![Brush Artist · Refs · #15 Ultramarine brush script — own sheet](Brush-Artist-Refs-15-Ultramarine-brush-script-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 40 % → 42 % | 9.0 px | 0.67 | 1.05 | 50 |
| stroke 2 | 40 % → 43 % | 8.9 px | 0.66 | 1.07 | 50 |
| stroke 3 | 40 % → 42 % | 9.5 px | 0.73 | 1.06 | 27 |
| stroke 4 | 41 % → 45 % | 10.0 px | 0.75 | 1.09 | 17 |
| stroke 5 | 45 % → 48 % | 9.8 px | 0.73 | 1.09 | 26 |
| stroke 6 | 42 % → 44 % | 9.5 px | 0.64 | 1.05 | 54 |
| stroke 7 | 43 % → 47 % | 9.2 px | 0.72 | 1.09 | 31 |
| stroke 8 | 39 % → 41 % | 9.3 px | 0.68 | 1.05 | 44 |
| stroke 9 | 40 % → 42 % | 9.2 px | 0.70 | 1.06 | 42 |
| stroke 10 | 36 % → 38 % | 9.9 px | 0.68 | 1.06 | 46 |
| stroke 11 | 42 % → 45 % | 9.5 px | 0.70 | 1.07 | 39 |
| stroke 12 | 39 % → 41 % | 9.4 px | 0.66 | 1.06 | 48 |
| stroke 13 | 45 % → 48 % | 10.3 px | 0.71 | 1.06 | 31 |
| stroke 14 | 38 % → 41 % | 9.8 px | 0.73 | 1.08 | 24 |
| stroke 15 | 37 % → 39 % | 9.1 px | 0.69 | 1.07 | 42 |
| stroke 16 | 42 % → 45 % | 9.3 px | 0.72 | 1.07 | 27 |
| stroke 17 | 41 % → 44 % | 7.1 px | 0.71 | 1.09 | 44 |
| stroke 18 | 43 % → 45 % | 9.3 px | 0.73 | 1.06 | 26 |
| stroke 19 | 39 % → 41 % | 8.8 px | 0.65 | 1.06 | 56 |
| stroke 20 | 40 % → 43 % | 9.4 px | 0.71 | 1.06 | 33 |
| stroke 21 | 40 % → 43 % | 9.8 px | 0.70 | 1.08 | 37 |
| stroke 22 | 42 % → 45 % | 8.5 px | 0.65 | 1.06 | 56 |
| stroke 23 | 40 % → 43 % | 10.0 px | 0.73 | 1.09 | 23 |
| stroke 24 | 38 % → 41 % | 8.8 px | 0.73 | 1.08 | 33 |
| stroke 25 | 41 % → 44 % | 9.9 px | 0.72 | 1.07 | 31 |
| stroke 26 | 47 % → 49 % | 9.3 px | 0.68 | 1.06 | 44 |
| stroke 27 | 42 % → 45 % | 8.8 px | 0.63 | 1.05 | 59 |
| stroke 28 | 44 % → 46 % | 9.1 px | 0.70 | 1.06 | 40 |
| stroke 29 | 36 % → 39 % | 10.5 px | 0.72 | 1.08 | 25 |
| stroke 30 | 39 % → 41 % | 8.5 px | 0.71 | 1.05 | 40 |
| stroke 31 | 42 % → 46 % | 10.3 px | 0.74 | 1.07 | 19 |
| stroke 32 | 42 % → 46 % | 9.5 px | 0.73 | 1.10 | 25 |
| stroke 33 | 35 % → 38 % | 10.8 px | 0.72 | 1.09 | 22 |
| stroke 34 | 40 % → 43 % | 9.8 px | 0.74 | 1.08 | 23 |
| stroke 35 | 36 % → 38 % | 9.4 px | 0.66 | 1.05 | 48 |

## Brush Artist · Refs · #18 Blue oil-stick scribbles — own sheet
own sheet 600 × 600 · Pastel 1.00 · 10 px · 3.1 s

![Brush Artist · Refs · #18 Blue oil-stick scribbles — own sheet](Brush-Artist-Refs-18-Blue-oil-stick-scribbles-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 15 % → 31 % | 3.8 px | 0.49 | 2.11 | 174 |
| stroke 2 | 13 % → 37 % | 3.6 px | 0.49 | 2.73 | 208 |
| stroke 3 | 16 % → 26 % | 5.8 px | 0.49 | 1.66 | 191 |
| stroke 4 | 15 % → 29 % | 8.0 px | 0.49 | 1.88 | 186 |
| stroke 5 | 29 % → 34 % | 8.4 px | 0.49 | 1.19 | 154 |
| stroke 6 | 25 % → 26 % | 9.4 px | 0.49 | 1.02 | 133 |
| stroke 7 | 26 % → 32 % | 8.3 px | 0.49 | 1.24 | 160 |
| stroke 8 | 30 % → 30 % | 17.0 px | 0.49 | 1.00 | 185 |

Numbers say: wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #20 Orange-red crayon scribble — own sheet
own sheet 600 × 600 · Pastel 1.00 · 14 px · 2.7 s

![Brush Artist · Refs · #20 Orange-red crayon scribble — own sheet](Brush-Artist-Refs-20-Orange-red-crayon-scribble-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 8 % → 18 % | 5.5 px | 0.59 | 2.46 | 199 |
| stroke 2 | 9 % → 23 % | 6.8 px | 0.59 | 2.48 | 168 |
| stroke 3 | 13 % → 21 % | 8.5 px | 0.59 | 1.64 | 155 |
| stroke 4 | 24 % → 32 % | 8.9 px | 0.59 | 1.34 | 177 |
| stroke 5 | 27 % → 27 % | 7.7 px | 0.59 | 1.00 | 166 |
| stroke 6 | 22 % → 22 % | 16.8 px | 0.59 | 1.00 | 185 |

Numbers say: wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #21 Gritty black contours — own sheet
own sheet 600 × 600 · Gouache 1.00 · 12 px · 4.5 s

![Brush Artist · Refs · #21 Gritty black contours — own sheet](Brush-Artist-Refs-21-Gritty-black-contours-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 5 % → 4 % | 5.5 px | 0.37 | 0.78 | 159 |
| stroke 2 | 5 % → 3 % | 8.1 px | 0.37 | 0.56 | 191 |
| stroke 3 | 7 % → 3 % | 6.4 px | 0.37 | 0.37 | 121 |
| stroke 4 | 8 % → 3 % | 10.0 px | 0.37 | 0.39 | 137 |
| stroke 5 | 8 % → 2 % | 10.1 px | 0.37 | 0.29 | 94 |

## Brush Artist · Refs · #22 Bold black brush poster — own sheet
own sheet 600 × 600 · Ink 1.00 · 20 px · 5.2 s

![Brush Artist · Refs · #22 Bold black brush poster — own sheet](Brush-Artist-Refs-22-Bold-black-brush-poster-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 22 % → 26 % | 35.8 px | 0.95 | 1.20 | 98 |
| stroke 2 | 27 % → 37 % | 41.0 px | 0.95 | 1.37 | 25 |
| stroke 3 | 28 % → 28 % | 42.5 px | 0.95 | 1.00 | 48 |
| stroke 4 | 27 % → 39 % | 53.4 px | 0.95 | 1.43 | 79 |
| stroke 5 | 25 % → 25 % | 43.4 px | 0.94 | 1.00 | 112 |

## Brush Artist · Refs · #23 Dry white on orange + black line — own sheet
own sheet 600 × 600 · Gouache 1.00 · 50 px · 9.0 s

![Brush Artist · Refs · #23 Dry white on orange + black line — own sheet](Brush-Artist-Refs-23-Dry-white-on-orange-black-line-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 8 % → 7 % | 26.1 px | 0.40 | 0.94 | 154 |
| stroke 2 | 8 % → 6 % | 29.2 px | 0.40 | 0.78 | 207 |
| stroke 3 | 13 % → 7 % | 48.1 px | 0.40 | 0.52 | 200 |
| stroke 4 | 14 % → 8 % | 53.9 px | 0.40 | 0.57 | 206 |
| stroke 5 | 18 % → 9 % | 66.6 px | 0.40 | 0.51 | 235 |
| stroke 6 | 21 % → 9 % | 85.0 px | 0.40 | 0.46 | 190 |
| stroke 7 | 18 % → 8 % | 68.1 px | 0.39 | 0.46 | 220 |
| stroke 8 | 17 % → 8 % | 67.9 px | 0.39 | 0.44 | 209 |
| stroke 9 | 16 % → 9 % | 59.1 px | 0.39 | 0.60 | 170 |
| stroke 10 | 16 % → 10 % | 63.2 px | 0.39 | 0.65 | 146 |
| stroke 11 | 16 % → 11 % | 60.5 px | 0.39 | 0.69 | 145 |
| stroke 12 | 17 % → 12 % | 65.2 px | 0.39 | 0.72 | 156 |
| stroke 13 | 15 % → 12 % | 57.0 px | 0.39 | 0.79 | 143 |
| stroke 14 | 18 % → 12 % | 69.6 px | 0.39 | 0.67 | 166 |
| stroke 15 | 21 % → 11 % | 79.4 px | 0.39 | 0.52 | 149 |
| stroke 16 | 18 % → 9 % | 72.2 px | 0.39 | 0.51 | 149 |
| stroke 17 | 20 % → 8 % | 68.6 px | 0.39 | 0.42 | 145 |
| stroke 18 | 22 % → 8 % | 78.2 px | 0.39 | 0.37 | 126 |

## Brush Artist · Refs · #24 Picasso flat oil — own sheet
own sheet 600 × 600 · Oil 0.89 · Oil glaze 0.11 · 34 px · 6.6 s

![Brush Artist · Refs · #24 Picasso flat oil — own sheet](Brush-Artist-Refs-24-Picasso-flat-oil-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 14 % → 42 % | 29.5 px | 0.23 | 3.02 | 128 |
| stroke 2 | 18 % → 46 % | 41.9 px | 0.23 | 2.56 | 133 |
| stroke 3 | 26 % → 56 % | 55.9 px | 0.23 | 2.19 | 133 |
| stroke 4 | 35 % → 62 % | 77.6 px | 0.23 | 1.79 | 136 |
| stroke 5 | 41 % → 68 % | 90.4 px | 0.23 | 1.65 | 128 |
| stroke 6 | 42 % → 62 % | 97.4 px | 0.22 | 1.49 | 128 |
| stroke 7 | 42 % → 62 % | 88.1 px | 0.23 | 1.48 | 129 |
| stroke 8 | 42 % → 62 % | 100.6 px | 0.23 | 1.49 | 128 |
| stroke 9 | 34 % → 58 % | 73.8 px | 0.23 | 1.71 | 123 |
| stroke 10 | 36 % → 57 % | 85.1 px | 0.23 | 1.58 | 126 |
| stroke 11 | 33 % → 55 % | 70.7 px | 0.23 | 1.66 | 132 |
| stroke 12 | 35 % → 55 % | 84.2 px | 0.23 | 1.56 | 128 |
| stroke 13 | 34 % → 62 % | 75.2 px | 0.23 | 1.81 | 134 |
| stroke 14 | 36 % → 64 % | 81.0 px | 0.23 | 1.78 | 131 |
| stroke 15 | 34 % → 57 % | 72.3 px | 0.22 | 1.66 | 131 |
| stroke 16 | 34 % → 50 % | 78.3 px | 0.22 | 1.47 | 147 |
| stroke 17 | 39 % → 44 % | 81.8 px | 0.22 | 1.14 | 161 |
| stroke 18 | 39 % → 39 % | 94.5 px | 0.22 | 1.00 | 189 |

Numbers say: wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #25 Yellow heavy flat stroke — own sheet
own sheet 600 × 600 · Impasto 1.00 · 110 px · 3.8 s

![Brush Artist · Refs · #25 Yellow heavy flat stroke — own sheet](Brush-Artist-Refs-25-Yellow-heavy-flat-stroke-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 18 % → 18 % | 104.5 px | 0.17 | 0.98 | 619 |

## Brush Artist · Refs · #27 Orange impasto swatch — own sheet
own sheet 600 × 600 · Impasto 1.00 · 60 px · 4.6 s

![Brush Artist · Refs · #27 Orange impasto swatch — own sheet](Brush-Artist-Refs-27-Orange-impasto-swatch-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 8 % → 21 % | 62.0 px | 0.33 | 2.59 | 114 |
| stroke 2 | 7 % → 33 % | 62.5 px | 0.33 | 4.66 | 80 |
| stroke 3 | 25 % → 35 % | 246.4 px | 0.33 | 1.40 | 68 |
| stroke 4 | 10 % → 12 % | 69.8 px | 0.33 | 1.25 | 111 |
| stroke 5 | 17 % → 33 % | 63.8 px | 0.32 | 1.89 | 125 |
| stroke 6 | 18 % → 31 % | 144.9 px | 0.32 | 1.79 | 138 |
| stroke 7 | 8 % → 15 % | 69.7 px | 0.32 | 1.88 | 95 |
| stroke 8 | 33 % → 34 % | 337.7 px | 0.33 | 1.04 | 77 |
| stroke 9 | 38 % → 37 % | 185.6 px | 0.33 | 0.97 | 150 |
| stroke 10 | 33 % → 33 % | 304.5 px | 0.32 | 0.98 | 71 |

Numbers say: wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #28 Miles Davis black lines — own sheet
own sheet 600 × 600 · Ink 1.00 · 22 px · 7.7 s

![Brush Artist · Refs · #28 Miles Davis black lines — own sheet](Brush-Artist-Refs-28-Miles-Davis-black-lines-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 22 % → 31 % | 36.1 px | 0.88 | 1.43 | 281 |
| stroke 2 | 28 % → 48 % | 38.4 px | 0.88 | 1.72 | 237 |
| stroke 3 | 39 % → 43 % | 74.7 px | 0.88 | 1.11 | 199 |
| stroke 4 | 42 % → 48 % | 82.9 px | 0.88 | 1.16 | 307 |
| stroke 5 | 54 % → 54 % | 109.1 px | 0.88 | 1.00 | 180 |

Numbers say: wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #29 Shrigley magenta asterisk — own sheet
own sheet 600 × 600 · Watercolour 1.00 · 70 px · 7.5 s

![Brush Artist · Refs · #29 Shrigley magenta asterisk — own sheet](Brush-Artist-Refs-29-Shrigley-magenta-asterisk-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 13 % → 37 % | 46.6 px | 0.67 | 2.86 | 314 |
| stroke 2 | 12 % → 12 % | 87.1 px | 0.67 | 1.00 | 252 |
| stroke 3 | 28 % → 37 % | 100.9 px | 0.67 | 1.31 | 206 |
| stroke 4 | 23 % → 23 % | 164.0 px | 0.67 | 1.02 | 213 |

Numbers say: wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #30 Red gouache face patch — own sheet
own sheet 600 × 600 · Gouache 1.00 · 60 px · 13.0 s

![Brush Artist · Refs · #30 Red gouache face patch — own sheet](Brush-Artist-Refs-30-Red-gouache-face-patch-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 12 % → 37 % | 51.5 px | 0.54 | 3.23 | 314 |
| stroke 2 | 15 % → 40 % | 74.5 px | 0.54 | 2.72 | 238 |
| stroke 3 | 24 % → 50 % | 115.9 px | 0.54 | 2.06 | 214 |
| stroke 4 | 27 % → 52 % | 134.1 px | 0.54 | 1.94 | 203 |
| stroke 5 | 34 % → 60 % | 159.9 px | 0.54 | 1.77 | 179 |
| stroke 6 | 35 % → 61 % | 178.3 px | 0.54 | 1.76 | 150 |
| stroke 7 | 34 % → 59 % | 160.9 px | 0.54 | 1.73 | 152 |
| stroke 8 | 34 % → 56 % | 162.5 px | 0.54 | 1.66 | 163 |
| stroke 9 | 36 % → 60 % | 173.1 px | 0.54 | 1.66 | 145 |
| stroke 10 | 38 % → 62 % | 196.8 px | 0.54 | 1.64 | 141 |
| stroke 11 | 37 % → 61 % | 182.4 px | 0.54 | 1.66 | 142 |
| stroke 12 | 36 % → 58 % | 178.3 px | 0.54 | 1.62 | 154 |
| stroke 13 | 33 % → 46 % | 156.5 px | 0.54 | 1.39 | 144 |
| stroke 14 | 33 % → 41 % | 157.6 px | 0.54 | 1.25 | 169 |
| stroke 15 | 33 % → 37 % | 153.4 px | 0.54 | 1.12 | 160 |
| stroke 16 | 39 % → 39 % | 184.9 px | 0.54 | 0.99 | 150 |

Numbers say: wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #31 Warhol blotted line — own sheet
own sheet 600 × 600 · Ink 1.00 · 6 px · 4.6 s

![Brush Artist · Refs · #31 Warhol blotted line — own sheet](Brush-Artist-Refs-31-Warhol-blotted-line-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 21 % → 42 % | 15.8 px | 0.82 | 1.97 | 86 |
| stroke 2 | 17 % → 23 % | 15.9 px | 0.82 | 1.34 | 74 |
| stroke 3 | 24 % → 25 % | 25.1 px | 0.81 | 1.02 | 80 |
| stroke 4 | 31 % → 40 % | 31.8 px | 0.82 | 1.28 | 51 |
| stroke 5 | 35 % → 44 % | 36.4 px | 0.82 | 1.23 | 74 |
| stroke 6 | 32 % → 33 % | 26.8 px | 0.81 | 1.03 | 71 |

Numbers say: wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #32 Thick orange swipes — own sheet
own sheet 600 × 600 · Impasto 1.00 · 90 px · 3.7 s

![Brush Artist · Refs · #32 Thick orange swipes — own sheet](Brush-Artist-Refs-32-Thick-orange-swipes-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 14 % → 27 % | 86.2 px | 0.02 | 1.90 | 310 |
| stroke 2 | 26 % → 38 % | 177.0 px | 0.02 | 1.43 | 349 |
| stroke 3 | 28 % → 27 % | 177.7 px | 0.02 | 0.98 | 335 |

Numbers say: wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #33 Red wet-in-wet band — own sheet
own sheet 600 × 600 · Watercolour 1.00 · 80 px · 16.0 s

![Brush Artist · Refs · #33 Red wet-in-wet band — own sheet](Brush-Artist-Refs-33-Red-wet-in-wet-band-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 24 % → 57 % | 90.3 px | 0.61 | 2.42 | 368 |
| stroke 2 | 29 % → 51 % | 234.2 px | 0.62 | 1.79 | 108 |
| stroke 3 | 35 % → 54 % | 342.3 px | 0.61 | 1.52 | 147 |
| stroke 4 | 41 % → 61 % | 398.1 px | 0.62 | 1.48 | 168 |
| stroke 5 | 40 % → 56 % | 341.8 px | 0.61 | 1.38 | 266 |
| stroke 6 | 41 % → 48 % | 313.9 px | 0.59 | 1.17 | 229 |

Numbers say: wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #34 Magenta oil patches — own sheet
own sheet 600 × 600 · Oil 0.89 · Oil glaze 0.11 · 60 px · 5.0 s

![Brush Artist · Refs · #34 Magenta oil patches — own sheet](Brush-Artist-Refs-34-Magenta-oil-patches-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 8 % → 40 % | 59.8 px | 0.12 | 4.75 | 88 |
| stroke 2 | 8 % → 28 % | 56.4 px | 0.12 | 3.39 | 71 |
| stroke 3 | 7 % → 34 % | 62.2 px | 0.12 | 4.54 | 83 |
| stroke 4 | 16 % → 20 % | 129.9 px | 0.12 | 1.26 | 77 |
| stroke 5 | 23 % → 33 % | 120.8 px | 0.12 | 1.44 | 122 |
| stroke 6 | 19 % → 36 % | 164.5 px | 0.12 | 1.87 | 82 |
| stroke 7 | 28 % → 33 % | 221.8 px | 0.12 | 1.19 | 91 |
| stroke 8 | 32 % → 38 % | 226.1 px | 0.12 | 1.19 | 114 |
| stroke 9 | 24 % → 26 % | 155.5 px | 0.12 | 1.07 | 97 |
| stroke 10 | 28 % → 28 % | 247.7 px | 0.12 | 1.00 | 72 |
| stroke 11 | 34 % → 34 % | 306.2 px | 0.12 | 1.00 | 68 |
| stroke 12 | 26 % → 26 % | 181.4 px | 0.12 | 1.00 | 97 |

Numbers say: wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #35 Red band with runs — own sheet
own sheet 600 × 600 · Watercolour 1.00 · 70 px · 14.2 s

![Brush Artist · Refs · #35 Red band with runs — own sheet](Brush-Artist-Refs-35-Red-band-with-runs-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 37 % → 48 % | 138.8 px | 0.46 | 1.30 | 819 |

## Brush Artist · Refs · #36 Magenta letters flat brush — own sheet
own sheet 600 × 600 · Gouache 1.00 · 36 px · 16.0 s

![Brush Artist · Refs · #36 Magenta letters flat brush — own sheet](Brush-Artist-Refs-36-Magenta-letters-flat-brush-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 20 % → 39 % | 59.0 px | 0.50 | 1.95 | 57 |
| stroke 2 | 20 % → 32 % | 46.6 px | 0.50 | 1.59 | 70 |
| stroke 3 | 29 % → 54 % | 86.8 px | 0.50 | 1.86 | 73 |
| stroke 4 | 26 % → 44 % | 51.2 px | 0.50 | 1.67 | 184 |
| stroke 5 | 33 % → 55 % | 96.1 px | 0.50 | 1.67 | 138 |
| stroke 6 | 42 % → 56 % | 242.4 px | 0.50 | 1.33 | 28 |
| stroke 7 | 30 % → 44 % | 56.7 px | 0.50 | 1.45 | 227 |
| stroke 8 | 31 % → 53 % | 98.5 px | 0.50 | 1.68 | 78 |
| stroke 9 | 38 % → 51 % | 158.3 px | 0.50 | 1.33 | 57 |
| stroke 10 | 37 % → 63 % | 106.7 px | 0.50 | 1.72 | 71 |
| stroke 11 | 39 % → 62 % | 225.9 px | 0.50 | 1.58 | 15 |
| stroke 12 | 43 % → 56 % | 81.9 px | 0.50 | 1.29 | 143 |
| stroke 13 | 32 % → 46 % | 117.6 px | 0.50 | 1.43 | 37 |
| stroke 14 | 35 % → 52 % | 134.4 px | 0.50 | 1.47 | 36 |
| stroke 15 | 38 % → 56 % | 108.5 px | 0.50 | 1.49 | 93 |
| stroke 16 | 41 % → 50 % | 232.0 px | 0.50 | 1.23 | 25 |
| stroke 17 | 44 % → 52 % | 81.7 px | 0.50 | 1.19 | 137 |
| stroke 18 | 27 % → 36 % | 97.5 px | 0.50 | 1.35 | 66 |
| stroke 19 | 40 % → 39 % | 117.0 px | 0.50 | 0.96 | 43 |
| stroke 20 | 45 % → 45 % | 132.2 px | 0.50 | 0.99 | 48 |
| stroke 21 | 41 % → 39 % | 78.6 px | 0.50 | 0.96 | 121 |

Numbers say: wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #37 Oil still life dabs — own sheet
own sheet 600 × 600 · Oil 0.89 · Oil glaze 0.11 · 40 px · 4.3 s

![Brush Artist · Refs · #37 Oil still life dabs — own sheet](Brush-Artist-Refs-37-Oil-still-life-dabs-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 7 % → 7 % | 41.8 px | 0.38 | 1.00 | 42 |
| stroke 2 | 6 % → 26 % | 42.9 px | 0.39 | 4.41 | 29 |
| stroke 3 | 11 % → 34 % | 88.8 px | 0.39 | 3.00 | 28 |
| stroke 4 | 9 % → 9 % | 41.0 px | 0.38 | 1.00 | 49 |
| stroke 5 | 6 % → 10 % | 40.9 px | 0.38 | 1.73 | 33 |
| stroke 6 | 13 % → 29 % | 80.2 px | 0.39 | 2.32 | 37 |
| stroke 7 | 10 % → 23 % | 109.0 px | 0.38 | 2.21 | 13 |
| stroke 8 | 8 % → 13 % | 84.0 px | 0.38 | 1.65 | 22 |
| stroke 9 | 12 % → 13 % | 64.8 px | 0.38 | 1.08 | 60 |
| stroke 10 | 20 % → 24 % | 102.2 px | 0.38 | 1.20 | 59 |
| stroke 11 | 23 % → 27 % | 195.3 px | 0.39 | 1.17 | 36 |
| stroke 12 | 20 % → 20 % | 218.8 px | 0.39 | 1.01 | 24 |
| stroke 13 | 16 % → 16 % | 160.2 px | 0.39 | 1.00 | 30 |
| stroke 14 | 16 % → 16 % | 126.3 px | 0.38 | 1.00 | 24 |

Numbers say: wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #38 Sanguine drawing — own sheet
own sheet 600 × 600 · Pastel 1.00 · 6 px · 3.3 s

![Brush Artist · Refs · #38 Sanguine drawing — own sheet](Brush-Artist-Refs-38-Sanguine-drawing-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 3 % → 14 % | 2.9 px | 0.57 | 5.29 | 21 |
| stroke 2 | 3 % → 7 % | 2.9 px | 0.58 | 2.89 | 23 |
| stroke 3 | 3 % → 9 % | 2.9 px | 0.57 | 3.41 | 13 |
| stroke 4 | 2 % → 17 % | 2.7 px | 0.57 | 7.18 | 13 |
| stroke 5 | 2 % → 7 % | 2.7 px | 0.57 | 3.02 | 7 |
| stroke 6 | 3 % → 19 % | 3.4 px | 0.57 | 6.32 | 10 |
| stroke 7 | 5 % → 14 % | 5.2 px | 0.57 | 3.07 | 10 |
| stroke 8 | 4 % → 16 % | 4.7 px | 0.57 | 3.78 | 13 |
| stroke 9 | 3 % → 7 % | 2.9 px | 0.57 | 2.65 | 15 |
| stroke 10 | 4 % → 16 % | 4.7 px | 0.57 | 3.83 | 12 |
| stroke 11 | 3 % → 4 % | 2.9 px | 0.57 | 1.61 | 13 |
| stroke 12 | 4 % → 15 % | 4.8 px | 0.57 | 3.58 | 7 |
| stroke 13 | 8 % → 17 % | 8.9 px | 0.57 | 2.23 | 8 |
| stroke 14 | 4 % → 14 % | 4.9 px | 0.57 | 3.19 | 11 |
| stroke 15 | 9 % → 18 % | 10.7 px | 0.57 | 1.87 | 7 |
| stroke 16 | 6 % → 16 % | 6.6 px | 0.57 | 2.70 | 6 |
| stroke 17 | 4 % → 9 % | 4.4 px | 0.57 | 2.25 | 7 |
| stroke 18 | 3 % → 5 % | 2.9 px | 0.57 | 1.85 | 9 |
| stroke 19 | 6 % → 16 % | 6.9 px | 0.57 | 2.68 | 8 |
| stroke 20 | 8 % → 14 % | 9.2 px | 0.57 | 1.70 | 9 |
| stroke 21 | 4 % → 4 % | 4.3 px | 0.57 | 1.00 | 7 |
| stroke 22 | 8 % → 13 % | 8.6 px | 0.57 | 1.79 | 8 |
| stroke 23 | 7 % → 12 % | 8.3 px | 0.57 | 1.61 | 9 |
| stroke 24 | 4 % → 7 % | 4.8 px | 0.57 | 1.71 | 12 |
| stroke 25 | 8 % → 14 % | 8.7 px | 0.57 | 1.84 | 9 |
| stroke 26 | 6 % → 8 % | 6.5 px | 0.57 | 1.34 | 9 |
| stroke 27 | 4 % → 4 % | 4.3 px | 0.57 | 1.10 | 7 |
| stroke 28 | 7 % → 11 % | 8.2 px | 0.57 | 1.59 | 9 |
| stroke 29 | 8 % → 17 % | 8.7 px | 0.57 | 2.21 | 8 |
| stroke 30 | 13 % → 17 % | 14.9 px | 0.57 | 1.29 | 12 |
| stroke 31 | 5 % → 6 % | 5.4 px | 0.57 | 1.29 | 9 |
| stroke 32 | 10 % → 13 % | 11.8 px | 0.57 | 1.24 | 7 |
| stroke 33 | 7 % → 8 % | 8.5 px | 0.57 | 1.07 | 8 |
| stroke 34 | 11 % → 14 % | 12.0 px | 0.57 | 1.36 | 8 |
| stroke 35 | 9 % → 14 % | 10.0 px | 0.57 | 1.61 | 10 |
| stroke 36 | 10 % → 13 % | 11.4 px | 0.57 | 1.26 | 8 |
| stroke 37 | 9 % → 16 % | 10.5 px | 0.57 | 1.71 | 7 |
| stroke 38 | 13 % → 19 % | 14.8 px | 0.57 | 1.48 | 7 |
| stroke 39 | 14 % → 17 % | 15.7 px | 0.57 | 1.21 | 13 |
| stroke 40 | 6 % → 7 % | 7.2 px | 0.57 | 1.14 | 9 |
| stroke 41 | 16 % → 16 % | 17.7 px | 0.57 | 1.01 | 8 |
| stroke 42 | 14 % → 16 % | 15.2 px | 0.57 | 1.17 | 9 |
| stroke 43 | 10 % → 12 % | 11.7 px | 0.57 | 1.17 | 9 |
| stroke 44 | 13 % → 15 % | 14.3 px | 0.57 | 1.22 | 9 |
| stroke 45 | 2 % → 2 % | 2.7 px | 0.57 | 1.00 | 9 |
| stroke 46 | 16 % → 16 % | 18.5 px | 0.57 | 1.00 | 10 |
| stroke 47 | 13 % → 13 % | 15.0 px | 0.57 | 1.00 | 8 |
| stroke 48 | 12 % → 13 % | 14.3 px | 0.57 | 1.07 | 13 |
| stroke 49 | 19 % → 19 % | 21.4 px | 0.57 | 1.00 | 15 |
| stroke 50 | 10 % → 10 % | 11.6 px | 0.57 | 1.00 | 11 |

Numbers say: wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #39 Very thick impasto — own sheet
own sheet 600 × 600 · Impasto 1.00 · 60 px · 5.9 s

![Brush Artist · Refs · #39 Very thick impasto — own sheet](Brush-Artist-Refs-39-Very-thick-impasto-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 26 % → 37 % | 59.7 px | 0.43 | 1.42 | 437 |
| stroke 2 | 31 % → 48 % | 93.9 px | 0.43 | 1.53 | 427 |
| stroke 3 | 37 % → 49 % | 124.6 px | 0.43 | 1.32 | 470 |
| stroke 4 | 31 % → 44 % | 91.0 px | 0.43 | 1.41 | 376 |
| stroke 5 | 42 % → 41 % | 104.5 px | 0.43 | 0.97 | 453 |

Numbers say: wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #40 Watercolour blooms — own sheet
own sheet 600 × 600 · Watercolour 1.00 · 90 px · 12.1 s

![Brush Artist · Refs · #40 Watercolour blooms — own sheet](Brush-Artist-Refs-40-Watercolour-blooms-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 21 % → 27 % | 94.8 px | 0.12 | 1.26 | 1169 |

## Brush Artist · Refs · #41 Coloured pencil hatching — own sheet
own sheet 600 × 600 · Pastel 1.00 · 4 px · 3.3 s

![Brush Artist · Refs · #41 Coloured pencil hatching — own sheet](Brush-Artist-Refs-41-Coloured-pencil-hatching-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 3 % → 13 % | 2.2 px | 0.35 | 4.64 | 9 |
| stroke 2 | 3 % → 7 % | 2.3 px | 0.35 | 2.29 | 10 |
| stroke 3 | 2 % → 11 % | 1.9 px | 0.35 | 4.38 | 11 |
| stroke 4 | 3 % → 19 % | 2.1 px | 0.35 | 6.71 | 5 |
| stroke 5 | 4 % → 7 % | 2.9 px | 0.35 | 1.83 | 4 |
| stroke 6 | 3 % → 13 % | 2.3 px | 0.35 | 4.19 | 5 |
| stroke 7 | 3 % → 15 % | 2.6 px | 0.35 | 4.43 | 8 |
| stroke 8 | 3 % → 12 % | 2.1 px | 0.35 | 4.18 | 11 |
| stroke 9 | 5 % → 11 % | 3.6 px | 0.35 | 2.27 | 5 |
| stroke 10 | 5 % → 15 % | 3.8 px | 0.35 | 2.99 | 5 |
| stroke 11 | 4 % → 13 % | 3.0 px | 0.35 | 3.27 | 5 |
| stroke 12 | 3 % → 3 % | 2.1 px | 0.35 | 1.00 | 5 |
| stroke 13 | 7 % → 17 % | 5.2 px | 0.35 | 2.45 | 4 |
| stroke 14 | 3 % → 13 % | 2.4 px | 0.35 | 4.20 | 11 |
| stroke 15 | 6 % → 12 % | 4.5 px | 0.35 | 2.09 | 5 |
| stroke 16 | 7 % → 11 % | 5.1 px | 0.35 | 1.61 | 13 |
| stroke 17 | 3 % → 3 % | 2.1 px | 0.35 | 1.00 | 10 |
| stroke 18 | 5 % → 8 % | 3.6 px | 0.35 | 1.65 | 13 |
| stroke 19 | 5 % → 13 % | 3.8 px | 0.35 | 2.71 | 9 |
| stroke 20 | 5 % → 14 % | 3.7 px | 0.35 | 2.91 | 11 |
| stroke 21 | 4 % → 13 % | 3.2 px | 0.35 | 3.19 | 10 |
| stroke 22 | 9 % → 16 % | 6.8 px | 0.35 | 1.77 | 6 |
| stroke 23 | 9 % → 13 % | 6.5 px | 0.35 | 1.55 | 5 |
| stroke 24 | 6 % → 14 % | 4.7 px | 0.35 | 2.18 | 7 |
| stroke 25 | 5 % → 10 % | 3.5 px | 0.35 | 2.27 | 10 |
| stroke 26 | 4 % → 6 % | 2.7 px | 0.35 | 1.81 | 5 |
| stroke 27 | 3 % → 7 % | 2.3 px | 0.35 | 2.26 | 5 |
| stroke 28 | 6 % → 10 % | 4.5 px | 0.35 | 1.71 | 7 |
| stroke 29 | 3 % → 13 % | 2.4 px | 0.35 | 4.21 | 5 |
| stroke 30 | 6 % → 9 % | 4.4 px | 0.35 | 1.46 | 5 |
| stroke 31 | 7 % → 14 % | 5.1 px | 0.35 | 2.14 | 6 |
| stroke 32 | 3 % → 6 % | 2.5 px | 0.35 | 1.78 | 8 |
| stroke 33 | 6 % → 11 % | 5.0 px | 0.35 | 1.67 | 7 |
| stroke 34 | 3 % → 6 % | 2.6 px | 0.35 | 1.73 | 5 |
| stroke 35 | 7 % → 14 % | 5.0 px | 0.35 | 2.09 | 9 |
| stroke 36 | 5 % → 5 % | 3.7 px | 0.35 | 1.01 | 7 |
| stroke 37 | 7 % → 15 % | 5.2 px | 0.35 | 2.15 | 6 |
| stroke 38 | 8 % → 13 % | 5.8 px | 0.35 | 1.66 | 12 |
| stroke 39 | 7 % → 11 % | 5.1 px | 0.35 | 1.67 | 5 |
| stroke 40 | 8 % → 18 % | 6.2 px | 0.35 | 2.20 | 12 |
| stroke 41 | 9 % → 13 % | 6.9 px | 0.35 | 1.48 | 9 |
| stroke 42 | 10 % → 17 % | 7.7 px | 0.35 | 1.73 | 5 |
| stroke 43 | 5 % → 9 % | 3.9 px | 0.35 | 1.66 | 6 |
| stroke 44 | 10 % → 13 % | 7.3 px | 0.35 | 1.40 | 5 |
| stroke 45 | 13 % → 18 % | 10.0 px | 0.35 | 1.35 | 5 |
| stroke 46 | 5 % → 7 % | 3.6 px | 0.34 | 1.41 | 11 |
| stroke 47 | 11 % → 13 % | 8.0 px | 0.35 | 1.20 | 5 |
| stroke 48 | 12 % → 16 % | 9.2 px | 0.35 | 1.34 | 7 |
| stroke 49 | 6 % → 9 % | 4.2 px | 0.35 | 1.65 | 5 |
| stroke 50 | 7 % → 7 % | 5.2 px | 0.34 | 1.00 | 5 |
| stroke 51 | 8 % → 15 % | 6.4 px | 0.35 | 1.73 | 9 |
| stroke 52 | 12 % → 14 % | 9.1 px | 0.35 | 1.19 | 5 |
| stroke 53 | 11 % → 14 % | 8.1 px | 0.35 | 1.36 | 7 |
| stroke 54 | 10 % → 14 % | 7.4 px | 0.35 | 1.47 | 5 |
| stroke 55 | 11 % → 14 % | 8.2 px | 0.35 | 1.33 | 10 |
| stroke 56 | 11 % → 12 % | 8.5 px | 0.35 | 1.11 | 7 |
| stroke 57 | 9 % → 13 % | 7.2 px | 0.35 | 1.36 | 5 |
| stroke 58 | 10 % → 11 % | 7.7 px | 0.35 | 1.14 | 8 |
| stroke 59 | 11 % → 13 % | 8.4 px | 0.35 | 1.17 | 6 |
| stroke 60 | 16 % → 20 % | 11.9 px | 0.35 | 1.26 | 7 |
| stroke 61 | 19 % → 20 % | 14.6 px | 0.35 | 1.04 | 5 |
| stroke 62 | 10 % → 10 % | 7.3 px | 0.35 | 1.00 | 5 |
| stroke 63 | 11 % → 12 % | 8.7 px | 0.35 | 1.07 | 5 |
| stroke 64 | 14 % → 14 % | 10.7 px | 0.35 | 1.02 | 4 |
| stroke 65 | 15 % → 15 % | 11.6 px | 0.35 | 1.00 | 5 |
| stroke 66 | 14 % → 14 % | 10.7 px | 0.35 | 1.00 | 5 |
| stroke 67 | 12 % → 12 % | 8.8 px | 0.35 | 1.06 | 4 |
| stroke 68 | 5 % → 9 % | 3.6 px | 0.35 | 1.88 | 5 |
| stroke 69 | 5 % → 5 % | 4.1 px | 0.35 | 1.00 | 5 |
| stroke 70 | 10 % → 13 % | 7.4 px | 0.35 | 1.28 | 5 |
| stroke 71 | 9 % → 11 % | 7.1 px | 0.35 | 1.15 | 6 |
| stroke 72 | 5 % → 7 % | 4.2 px | 0.35 | 1.23 | 7 |
| stroke 73 | 12 % → 12 % | 9.3 px | 0.35 | 1.00 | 5 |
| stroke 74 | 14 % → 14 % | 10.8 px | 0.35 | 1.00 | 6 |
| stroke 75 | 15 % → 15 % | 11.4 px | 0.35 | 1.00 | 5 |
| stroke 76 | 14 % → 14 % | 10.5 px | 0.35 | 1.00 | 5 |
| stroke 77 | 7 % → 10 % | 5.4 px | 0.35 | 1.34 | 11 |
| stroke 78 | 9 % → 9 % | 7.0 px | 0.35 | 1.00 | 5 |
| stroke 79 | 7 % → 7 % | 5.7 px | 0.35 | 1.00 | 10 |
| stroke 80 | 11 % → 11 % | 8.3 px | 0.35 | 1.00 | 5 |

Numbers say: wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #42 Oil pastel shaggy — own sheet
own sheet 600 × 600 · Pastel 1.00 · 18 px · 3.4 s

![Brush Artist · Refs · #42 Oil pastel shaggy — own sheet](Brush-Artist-Refs-42-Oil-pastel-shaggy-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 5 % → 27 % | 8.0 px | 0.28 | 5.72 | 11 |
| stroke 2 | 5 % → 24 % | 8.6 px | 0.28 | 4.69 | 10 |
| stroke 3 | 5 % → 29 % | 8.9 px | 0.28 | 5.42 | 10 |
| stroke 4 | 5 % → 11 % | 8.8 px | 0.28 | 2.08 | 10 |
| stroke 5 | 6 % → 11 % | 9.9 px | 0.28 | 1.85 | 11 |
| stroke 6 | 8 % → 37 % | 13.9 px | 0.29 | 4.44 | 11 |
| stroke 7 | 11 % → 31 % | 17.7 px | 0.28 | 2.90 | 10 |
| stroke 8 | 7 % → 38 % | 11.4 px | 0.28 | 5.55 | 10 |
| stroke 9 | 8 % → 21 % | 13.9 px | 0.28 | 2.53 | 10 |
| stroke 10 | 8 % → 18 % | 13.2 px | 0.28 | 2.32 | 12 |
| stroke 11 | 6 % → 27 % | 9.4 px | 0.28 | 4.75 | 15 |
| stroke 12 | 8 % → 19 % | 13.6 px | 0.28 | 2.28 | 11 |
| stroke 13 | 13 % → 24 % | 21.0 px | 0.28 | 1.92 | 11 |
| stroke 14 | 5 % → 23 % | 7.9 px | 0.28 | 4.77 | 10 |
| stroke 15 | 5 % → 24 % | 9.0 px | 0.29 | 4.38 | 11 |
| stroke 16 | 9 % → 21 % | 15.7 px | 0.29 | 2.18 | 11 |
| stroke 17 | 17 % → 39 % | 28.0 px | 0.29 | 2.33 | 10 |
| stroke 18 | 14 % → 25 % | 22.8 px | 0.29 | 1.80 | 10 |
| stroke 19 | 15 % → 32 % | 24.9 px | 0.28 | 2.09 | 10 |
| stroke 20 | 21 % → 39 % | 35.1 px | 0.28 | 1.85 | 14 |
| stroke 21 | 9 % → 16 % | 14.4 px | 0.28 | 1.88 | 17 |
| stroke 22 | 14 % → 17 % | 23.9 px | 0.28 | 1.20 | 15 |
| stroke 23 | 12 % → 17 % | 20.6 px | 0.29 | 1.34 | 16 |
| stroke 24 | 18 % → 26 % | 30.0 px | 0.29 | 1.45 | 16 |
| stroke 25 | 20 % → 34 % | 32.6 px | 0.28 | 1.74 | 14 |
| stroke 26 | 6 % → 14 % | 9.2 px | 0.28 | 2.43 | 21 |
| stroke 27 | 18 % → 26 % | 30.5 px | 0.29 | 1.42 | 16 |
| stroke 28 | 14 % → 24 % | 23.7 px | 0.28 | 1.68 | 13 |
| stroke 29 | 9 % → 27 % | 14.9 px | 0.29 | 3.01 | 14 |
| stroke 30 | 15 % → 37 % | 25.0 px | 0.29 | 2.43 | 12 |
| stroke 31 | 14 % → 17 % | 23.3 px | 0.28 | 1.23 | 13 |
| stroke 32 | 16 % → 29 % | 27.0 px | 0.29 | 1.82 | 16 |
| stroke 33 | 15 % → 16 % | 24.5 px | 0.29 | 1.10 | 15 |
| stroke 34 | 19 % → 28 % | 31.4 px | 0.28 | 1.44 | 11 |
| stroke 35 | 26 % → 36 % | 42.6 px | 0.28 | 1.40 | 12 |
| stroke 36 | 25 % → 34 % | 41.0 px | 0.28 | 1.36 | 15 |
| stroke 37 | 12 % → 12 % | 19.3 px | 0.28 | 1.03 | 14 |
| stroke 38 | 19 % → 25 % | 31.7 px | 0.28 | 1.31 | 13 |
| stroke 39 | 16 % → 22 % | 27.3 px | 0.28 | 1.37 | 12 |
| stroke 40 | 22 % → 31 % | 36.6 px | 0.28 | 1.38 | 18 |
| stroke 41 | 32 % → 36 % | 53.1 px | 0.28 | 1.12 | 12 |
| stroke 42 | 23 % → 30 % | 38.3 px | 0.29 | 1.29 | 19 |
| stroke 43 | 12 % → 12 % | 20.3 px | 0.28 | 1.00 | 19 |
| stroke 44 | 30 % → 37 % | 49.0 px | 0.28 | 1.26 | 13 |
| stroke 45 | 16 % → 16 % | 26.3 px | 0.28 | 1.00 | 11 |
| stroke 46 | 29 % → 34 % | 48.1 px | 0.29 | 1.15 | 12 |
| stroke 47 | 38 % → 41 % | 62.0 px | 0.28 | 1.10 | 12 |
| stroke 48 | 29 % → 36 % | 47.9 px | 0.29 | 1.27 | 13 |
| stroke 49 | 27 % → 30 % | 45.1 px | 0.29 | 1.11 | 18 |
| stroke 50 | 38 % → 40 % | 63.4 px | 0.28 | 1.06 | 13 |
| stroke 51 | 16 % → 16 % | 26.1 px | 0.28 | 1.00 | 11 |
| stroke 52 | 38 % → 38 % | 62.5 px | 0.29 | 1.01 | 15 |
| stroke 53 | 22 % → 27 % | 37.0 px | 0.28 | 1.18 | 13 |
| stroke 54 | 17 % → 19 % | 29.0 px | 0.29 | 1.09 | 13 |
| stroke 55 | 15 % → 15 % | 25.0 px | 0.28 | 1.00 | 15 |
| stroke 56 | 13 % → 14 % | 21.6 px | 0.28 | 1.08 | 13 |
| stroke 57 | 23 % → 23 % | 37.7 px | 0.29 | 1.00 | 16 |
| stroke 58 | 28 % → 29 % | 46.1 px | 0.28 | 1.05 | 16 |
| stroke 59 | 40 % → 40 % | 67.3 px | 0.28 | 1.00 | 13 |
| stroke 60 | 22 % → 22 % | 35.6 px | 0.28 | 1.00 | 13 |

Numbers say: wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #43 Dragged black ink blocks — own sheet
own sheet 600 × 600 · Gouache 1.00 · 70 px · 10.0 s

![Brush Artist · Refs · #43 Dragged black ink blocks — own sheet](Brush-Artist-Refs-43-Dragged-black-ink-blocks-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 21 % → 14 % | 48.0 px | 0.44 | 0.68 | 605 |
| stroke 2 | 19 % → 13 % | 68.5 px | 0.44 | 0.69 | 609 |
| stroke 3 | 21 % → 12 % | 76.2 px | 0.44 | 0.58 | 553 |
| stroke 4 | 21 % → 12 % | 74.0 px | 0.44 | 0.58 | 504 |
| stroke 5 | 24 % → 10 % | 56.4 px | 0.44 | 0.40 | 757 |

## Brush Artist · Refs · #44 Blue looping ribbon — own sheet
own sheet 600 × 600 · Oil 1.00 · 80 px · 7.3 s

![Brush Artist · Refs · #44 Blue looping ribbon — own sheet](Brush-Artist-Refs-44-Blue-looping-ribbon-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 32 % → 32 % | 42.1 px | 0.78 | 1.00 | 4166 |

## Brush Artist · Refs · #45 Soft pastel pepper — own sheet
own sheet 600 × 600 · Pastel 1.00 · 40 px · 5.9 s

![Brush Artist · Refs · #45 Soft pastel pepper — own sheet](Brush-Artist-Refs-45-Soft-pastel-pepper-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 10 % → 39 % | 11.3 px | 0.49 | 3.75 | 499 |
| stroke 2 | 18 % → 34 % | 21.3 px | 0.49 | 1.87 | 421 |
| stroke 3 | 25 % → 37 % | 17.6 px | 0.49 | 1.46 | 384 |
| stroke 4 | 24 % → 35 % | 30.5 px | 0.49 | 1.43 | 544 |
| stroke 5 | 30 % → 30 % | 21.2 px | 0.49 | 1.00 | 302 |
| stroke 6 | 36 % → 44 % | 23.0 px | 0.48 | 1.23 | 449 |
| stroke 7 | 39 % → 43 % | 21.6 px | 0.48 | 1.10 | 599 |
| stroke 8 | 44 % → 44 % | 44.4 px | 0.49 | 1.00 | 456 |

Numbers say: wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #46 Red-brown ink lips — own sheet
own sheet 600 × 600 · Watercolour 1.00 · 50 px · 11.1 s

![Brush Artist · Refs · #46 Red-brown ink lips — own sheet](Brush-Artist-Refs-46-Red-brown-ink-lips-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 13 % → 27 % | 55.9 px | 0.56 | 1.99 | 182 |
| stroke 2 | 17 % → 32 % | 74.2 px | 0.53 | 1.87 | 98 |

Numbers say: wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #47 Pink knife slabs — own sheet
own sheet 600 × 600 · Impasto 1.00 · 90 px · 5.6 s

![Brush Artist · Refs · #47 Pink knife slabs — own sheet](Brush-Artist-Refs-47-Pink-knife-slabs-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 17 % → 32 % | 83.4 px | 0.11 | 1.94 | 413 |
| stroke 2 | 29 % → 43 % | 166.0 px | 0.11 | 1.46 | 323 |
| stroke 3 | 29 % → 43 % | 166.0 px | 0.11 | 1.46 | 360 |
| stroke 4 | 39 % → 38 % | 166.0 px | 0.11 | 0.98 | 285 |

Numbers say: wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #48 Black bands with drips — own sheet
own sheet 600 × 600 · Gouache 1.00 · 70 px · 15.8 s

![Brush Artist · Refs · #48 Black bands with drips — own sheet](Brush-Artist-Refs-48-Black-bands-with-drips-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 28 % → 41 % | 73.2 px | 0.39 | 1.46 | 714 |
| stroke 2 | 43 % → 57 % | 137.5 px | 0.39 | 1.33 | 668 |
| stroke 3 | 45 % → 57 % | 141.4 px | 0.39 | 1.27 | 775 |
| stroke 4 | 48 % → 46 % | 140.3 px | 0.39 | 0.96 | 728 |

## Brush Artist · Refs · #49 Magenta letters round brush — own sheet
own sheet 600 × 600 · Ink 1.00 · 30 px · 14.9 s

![Brush Artist · Refs · #49 Magenta letters round brush — own sheet](Brush-Artist-Refs-49-Magenta-letters-round-brush-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 27 % → 45 % | 62.8 px | 0.52 | 1.70 | 42 |
| stroke 2 | 29 % → 40 % | 52.1 px | 0.53 | 1.39 | 62 |
| stroke 3 | 40 % → 67 % | 94.9 px | 0.52 | 1.65 | 42 |
| stroke 4 | 33 % → 51 % | 53.1 px | 0.52 | 1.55 | 185 |
| stroke 5 | 39 % → 65 % | 92.8 px | 0.52 | 1.66 | 124 |
| stroke 6 | 53 % → 69 % | 227.1 px | 0.52 | 1.30 | 34 |
| stroke 7 | 41 % → 56 % | 63.5 px | 0.52 | 1.35 | 243 |
| stroke 8 | 35 % → 61 % | 90.4 px | 0.53 | 1.74 | 135 |
| stroke 9 | 48 % → 60 % | 151.1 px | 0.53 | 1.24 | 59 |
| stroke 10 | 42 % → 71 % | 98.8 px | 0.52 | 1.71 | 117 |
| stroke 11 | 51 % → 71 % | 216.6 px | 0.52 | 1.39 | 31 |
| stroke 12 | 52 % → 67 % | 81.1 px | 0.52 | 1.30 | 147 |
| stroke 13 | 42 % → 54 % | 115.2 px | 0.53 | 1.29 | 47 |
| stroke 14 | 45 % → 69 % | 131.3 px | 0.53 | 1.52 | 37 |
| stroke 15 | 43 % → 62 % | 101.5 px | 0.52 | 1.46 | 95 |
| stroke 16 | 51 % → 61 % | 218.6 px | 0.52 | 1.19 | 16 |
| stroke 17 | 53 % → 63 % | 81.3 px | 0.52 | 1.19 | 150 |
| stroke 18 | 36 % → 44 % | 99.3 px | 0.52 | 1.22 | 38 |
| stroke 19 | 53 % → 53 % | 122.7 px | 0.52 | 1.00 | 29 |
| stroke 20 | 54 % → 54 % | 123.7 px | 0.52 | 1.00 | 40 |
| stroke 21 | 49 % → 49 % | 80.7 px | 0.52 | 1.00 | 134 |

Numbers say: wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #50 Thick swipes on photo — own sheet
own sheet 600 × 600 · Impasto 1.00 · 40 px · 3.8 s

![Brush Artist · Refs · #50 Thick swipes on photo — own sheet](Brush-Artist-Refs-50-Thick-swipes-on-photo-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 9 % → 21 % | 43.0 px | 0.34 | 2.32 | 37 |
| stroke 2 | 9 % → 16 % | 42.1 px | 0.34 | 1.79 | 44 |
| stroke 3 | 10 % → 11 % | 42.0 px | 0.34 | 1.06 | 49 |
| stroke 4 | 11 % → 18 % | 42.6 px | 0.34 | 1.64 | 67 |
| stroke 5 | 11 % → 10 % | 42.0 px | 0.34 | 0.94 | 51 |
| stroke 6 | 17 % → 21 % | 97.5 px | 0.34 | 1.20 | 31 |
| stroke 7 | 22 % → 26 % | 91.9 px | 0.34 | 1.18 | 61 |
| stroke 8 | 21 % → 21 % | 119.5 px | 0.34 | 0.96 | 42 |
| stroke 9 | 9 % → 10 % | 41.6 px | 0.34 | 1.08 | 53 |
| stroke 10 | 22 % → 21 % | 73.4 px | 0.33 | 0.96 | 60 |
| stroke 11 | 9 % → 8 % | 42.4 px | 0.34 | 0.95 | 52 |
| stroke 12 | 17 % → 16 % | 92.8 px | 0.34 | 0.96 | 29 |

Numbers say: wet paint spreads well beyond the stroke.

## Brush Artist · Ink — dry brush — own sheet
own sheet 600 × 600 · Gouache 1.00 · 30 px · 4.0 s

![Brush Artist · Ink — dry brush — own sheet](Brush-Artist-Ink-dry-brush-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| ear | 7 % → 2 % | 8.8 px | 0.85 | 0.24 | 631 |
| drag0 | 6 % → 4 % | 10.3 px | 0.85 | 0.75 | 173 |
| drag1 | 8 % → 4 % | 16.7 px | 0.85 | 0.55 | 150 |
| drag2 | 10 % → 5 % | 21.7 px | 0.85 | 0.47 | 125 |
| drag3 | 10 % → 4 % | 24.5 px | 0.85 | 0.44 | 94 |

## Brush Artist · Watercolour — blue — own sheet
own sheet 600 × 600 · Watercolour 0.93 · Ink 0.07 · 40 px · 17.0 s

![Brush Artist · Watercolour — blue — own sheet](Brush-Artist-Watercolour-blue-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| s0 | 7 % → 24 % | 28.8 px | 0.30 | 3.32 | 68 |
| s1 | 6 % → 33 % | 10.1 px | 0.37 | 6.00 | 66 |
| s2 | 10 % → 19 % | 44.2 px | 0.26 | 1.81 | 62 |
| s3 | 10 % → 18 % | 26.7 px | 0.31 | 1.92 | 83 |
| s4 | 14 % → 30 % | 38.6 px | 0.36 | 2.16 | 144 |
| s5 | 19 % → 29 % | 39.3 px | 0.37 | 1.54 | 111 |
| s6 | 18 % → 22 % | 48.7 px | 0.31 | 1.25 | 103 |
| s7 | 25 % → 36 % | 32.7 px | 0.37 | 1.46 | 100 |
| s8 | 21 % → 25 % | 79.8 px | 0.30 | 1.20 | 52 |

Numbers say: wet paint spreads well beyond the stroke.

## Brush Artist · Charcoal — stick — own sheet
own sheet 600 × 600 · Charcoal 0.78 · Pastel 0.22 · 28 px · 2.1 s

![Brush Artist · Charcoal — stick — own sheet](Brush-Artist-Charcoal-stick-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| finger0 | 13 % → 25 % | 22.0 px | 0.83 | 2.01 | 74 |
| tip0 | 13 % → 21 % | 34.1 px | 0.83 | 1.68 | 19 |
| finger1 | 24 % → 41 % | 42.3 px | 0.83 | 1.69 | 58 |
| tip1 | 21 % → 30 % | 57.0 px | 0.83 | 1.41 | 28 |
| finger2 | 24 % → 36 % | 42.6 px | 0.83 | 1.51 | 76 |
| tip2 | 21 % → 30 % | 56.6 px | 0.83 | 1.42 | 25 |
| finger3 | 24 % → 27 % | 42.3 px | 0.83 | 1.15 | 74 |
| tip3 | 21 % → 21 % | 57.0 px | 0.83 | 1.00 | 22 |
| cig0 | 34 % → 46 % | 75.1 px | 0.83 | 1.37 | 22 |
| cig1 | 36 % → 46 % | 80.6 px | 0.83 | 1.28 | 27 |
| cig2 | 39 % → 46 % | 86.2 px | 0.83 | 1.19 | 18 |
| cig3 | 41 % → 46 % | 91.7 px | 0.83 | 1.12 | 25 |
| cig4 | 44 % → 46 % | 97.3 px | 0.83 | 1.05 | 32 |
| cig5 | 46 % → 46 % | 102.1 px | 0.83 | 1.00 | 25 |

Numbers say: wet paint spreads well beyond the stroke.

## Oil · Henry Ward · HW #02 cream over wet olive — own sheet
own sheet 600 × 600 · Oil 0.81 · Ink 0.19 · 56 px · 38.5 s

![Oil · Henry Ward · HW #02 cream over wet olive — own sheet](Oil-Henry-Ward-HW-02-cream-over-wet-olive-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 65 % → 27 % | 78.9 px | 0.36 | 0.42 | 2868 |
| stroke 2 | 79 % → 39 % | 143.5 px | 0.45 | 0.49 | 3020 |
| stroke 3 | 81 % → 53 % | 170.4 px | 0.40 | 0.65 | 2491 |
| stroke 4 | 81 % → 57 % | 169.3 px | 0.41 | 0.70 | 2710 |
| stroke 5 | 82 % → 47 % | 170.6 px | 0.42 | 0.57 | 2926 |
| stroke 6 | 81 % → 43 % | 172.4 px | 0.46 | 0.54 | 2223 |
| stroke 7 | 80 % → 33 % | 169.7 px | 0.46 | 0.41 | 2314 |
| stroke 8 | 93 % → 23 % | 169.2 px | 0.43 | 0.25 | 2127 |
| stroke 9 | 100 % → 14 % | 123.5 px | 0.25 | 0.14 | 2098 |
| stroke 10 | 8 % → 43 % | 32.0 px | 0.42 | 5.36 | 365 |
| stroke 11 | 15 % → 58 % | 60.1 px | 0.42 | 3.94 | 376 |
| stroke 12 | 7 % → 32 % | 30.5 px | 0.46 | 4.62 | 229 |
| stroke 13 | 20 % → 48 % | 78.0 px | 0.41 | 2.41 | 261 |
| stroke 14 | 29 % → 51 % | 105.0 px | 0.40 | 1.75 | 349 |
| stroke 15 | 39 % → 59 % | 146.9 px | 0.41 | 1.50 | 336 |
| stroke 16 | 46 % → 69 % | 230.0 px | 0.40 | 1.50 | 234 |
| stroke 17 | 37 % → 53 % | 130.9 px | 0.44 | 1.45 | 288 |
| stroke 18 | 29 % → 55 % | 114.8 px | 0.43 | 1.89 | 219 |
| stroke 19 | 32 % → 51 % | 150.8 px | 0.41 | 1.57 | 203 |
| stroke 20 | 29 % → 36 % | 113.6 px | 0.47 | 1.22 | 254 |
| stroke 21 | 31 % → 32 % | 111.1 px | 0.47 | 1.02 | 335 |
| stroke 22 | 44 % → 44 % | 149.0 px | 0.40 | 1.00 | 394 |
| stroke 23 | 55 % → 55 % | 197.8 px | 0.40 | 1.00 | 331 |
| stroke 24 | 49 % → 52 % | 213.0 px | 0.43 | 1.07 | 223 |
| stroke 25 | 49 % → 49 % | 186.3 px | 0.44 | 1.00 | 307 |
| stroke 26 | 34 % → 33 % | 140.9 px | 0.47 | 0.98 | 390 |

Numbers say: wet paint spreads well beyond the stroke.

## Oil · Henry Ward · HW #04 grey arcs over ochre — own sheet
own sheet 600 × 600 · Oil 1.00 · 46 px · 38.0 s

![Oil · Henry Ward · HW #04 grey arcs over ochre — own sheet](Oil-Henry-Ward-HW-04-grey-arcs-over-ochre-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 76 % → 37 % | 82.1 px | 0.19 | 0.49 | 2936 |
| stroke 2 | 86 % → 51 % | 142.2 px | 0.20 | 0.59 | 2880 |
| stroke 3 | 88 % → 70 % | 155.9 px | 0.19 | 0.80 | 2360 |
| stroke 4 | 88 % → 56 % | 154.8 px | 0.19 | 0.64 | 2519 |
| stroke 5 | 88 % → 41 % | 154.1 px | 0.15 | 0.47 | 2946 |
| stroke 6 | 85 % → 31 % | 150.0 px | 0.12 | 0.36 | 2147 |
| stroke 7 | 87 % → 34 % | 154.5 px | 0.10 | 0.40 | 2221 |
| stroke 8 | 90 % → 28 % | 150.3 px | 0.11 | 0.31 | 2358 |
| stroke 9 | 100 % → 24 % | 104.1 px | 0.11 | 0.24 | 1930 |
| stroke 10 | 9 % → 64 % | 34.2 px | 0.19 | 6.95 | 276 |
| stroke 11 | 14 % → 54 % | 48.1 px | 0.19 | 3.91 | 331 |
| stroke 12 | 14 % → 52 % | 53.2 px | 0.17 | 3.72 | 231 |
| stroke 13 | 25 % → 62 % | 68.8 px | 0.19 | 2.47 | 409 |
| stroke 14 | 31 % → 61 % | 118.6 px | 0.19 | 1.99 | 293 |
| stroke 15 | 34 % → 54 % | 117.9 px | 0.19 | 1.58 | 449 |
| stroke 16 | 39 % → 56 % | 147.1 px | 0.18 | 1.43 | 279 |
| stroke 17 | 45 % → 60 % | 168.4 px | 0.19 | 1.34 | 322 |
| stroke 18 | 44 % → 57 % | 150.9 px | 0.18 | 1.30 | 274 |
| stroke 19 | 51 % → 64 % | 167.5 px | 0.19 | 1.25 | 390 |
| stroke 20 | 55 % → 68 % | 169.1 px | 0.19 | 1.24 | 438 |
| stroke 21 | 58 % → 71 % | 187.8 px | 0.19 | 1.22 | 352 |
| stroke 22 | 36 % → 51 % | 129.9 px | 0.17 | 1.42 | 374 |
| stroke 23 | 55 % → 62 % | 200.5 px | 0.18 | 1.13 | 422 |
| stroke 24 | 72 % → 75 % | 277.4 px | 0.19 | 1.04 | 233 |
| stroke 25 | 51 % → 62 % | 175.8 px | 0.18 | 1.20 | 346 |
| stroke 26 | 70 % → 72 % | 241.9 px | 0.19 | 1.04 | 284 |
| stroke 27 | 26 % → 34 % | 79.3 px | 0.13 | 1.31 | 258 |
| stroke 28 | 24 % → 41 % | 84.4 px | 0.10 | 1.73 | 230 |
| stroke 29 | 23 % → 32 % | 94.7 px | 0.11 | 1.38 | 155 |
| stroke 30 | 31 % → 31 % | 90.4 px | 0.11 | 1.00 | 264 |

Numbers say: wet paint spreads well beyond the stroke.

## Oil · Henry Ward · HW #09 white arches over wet blue-grey — own sheet
own sheet 600 × 600 · Oil 1.00 · 46 px · 35.3 s

![Oil · Henry Ward · HW #09 white arches over wet blue-grey — own sheet](Oil-Henry-Ward-HW-09-white-arches-over-wet-blue-grey-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 79 % → 0 % | 80.8 px | 0.12 | 0.00 | 1585 |
| stroke 2 | 86 % → 6 % | 140.5 px | 0.10 | 0.07 | 2318 |
| stroke 3 | 87 % → 23 % | 155.7 px | 0.10 | 0.26 | 2156 |
| stroke 4 | 88 % → 40 % | 157.3 px | 0.10 | 0.46 | 2738 |
| stroke 5 | 86 % → 53 % | 152.0 px | 0.11 | 0.62 | 2629 |
| stroke 6 | 86 % → 59 % | 148.7 px | 0.12 | 0.69 | 2387 |
| stroke 7 | 87 % → 55 % | 151.9 px | 0.13 | 0.63 | 2023 |
| stroke 8 | 89 % → 49 % | 151.8 px | 0.14 | 0.55 | 2335 |
| stroke 9 | 100 % → 41 % | 99.7 px | 0.17 | 0.41 | 1681 |
| stroke 10 | 7 % → 49 % | 29.5 px | 0.12 | 6.61 | 481 |
| stroke 11 | 14 % → 59 % | 26.8 px | 0.12 | 4.08 | 549 |
| stroke 12 | 16 % → 56 % | 28.7 px | 0.12 | 3.53 | 600 |
| stroke 13 | 22 % → 70 % | 48.6 px | 0.13 | 3.19 | 360 |
| stroke 14 | 25 % → 61 % | 17.7 px | 0.13 | 2.49 | 714 |
| stroke 15 | 34 % → 71 % | 95.2 px | 0.12 | 2.07 | 486 |
| stroke 16 | 43 % → 65 % | 127.8 px | 0.13 | 1.53 | 340 |
| stroke 17 | 53 % → 82 % | 153.7 px | 0.12 | 1.54 | 354 |
| stroke 18 | 47 % → 67 % | 128.1 px | 0.12 | 1.43 | 470 |
| stroke 19 | 52 % → 63 % | 160.0 px | 0.12 | 1.21 | 387 |
| stroke 20 | 47 % → 66 % | 121.0 px | 0.12 | 1.41 | 462 |
| stroke 21 | 36 % → 51 % | 92.3 px | 0.11 | 1.40 | 364 |
| stroke 22 | 48 % → 52 % | 128.9 px | 0.11 | 1.09 | 411 |
| stroke 23 | 66 % → 71 % | 208.8 px | 0.12 | 1.08 | 472 |
| stroke 24 | 63 % → 64 % | 202.2 px | 0.12 | 1.01 | 212 |
| stroke 25 | 51 % → 55 % | 144.2 px | 0.13 | 1.07 | 298 |
| stroke 26 | 56 % → 65 % | 217.0 px | 0.14 | 1.16 | 171 |
| stroke 27 | 42 % → 49 % | 102.2 px | 0.14 | 1.17 | 299 |
| stroke 28 | 49 % → 49 % | 114.5 px | 0.15 | 1.00 | 308 |

Numbers say: wet paint spreads well beyond the stroke.

## Oil · Henry Ward · HW #03 navy contours over wet band — own sheet
own sheet 600 × 600 · Oil 1.00 · 46 px · 21.9 s

![Oil · Henry Ward · HW #03 navy contours over wet band — own sheet](Oil-Henry-Ward-HW-03-navy-contours-over-wet-band-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 77 % → 19 % | 78.2 px | 0.76 | 0.25 | 1513 |
| stroke 2 | 86 % → 23 % | 145.0 px | 0.74 | 0.26 | 1940 |
| stroke 3 | 86 % → 27 % | 151.3 px | 0.65 | 0.32 | 1983 |
| stroke 4 | 86 % → 36 % | 151.0 px | 0.58 | 0.42 | 1924 |
| stroke 5 | 85 % → 37 % | 151.5 px | 0.52 | 0.43 | 2072 |
| stroke 6 | 87 % → 30 % | 153.6 px | 0.56 | 0.35 | 2381 |
| stroke 7 | 87 % → 19 % | 149.9 px | 0.63 | 0.22 | 1658 |
| stroke 8 | 89 % → 9 % | 151.0 px | 0.74 | 0.10 | 1661 |
| stroke 9 | 100 % → 3 % | 104.1 px | 0.74 | 0.03 | 1406 |
| stroke 10 | 9 % → 38 % | 39.7 px | 0.54 | 4.00 | 107 |
| stroke 11 | 16 % → 44 % | 62.3 px | 0.52 | 2.70 | 147 |
| stroke 12 | 18 % → 37 % | 64.1 px | 0.51 | 2.06 | 159 |
| stroke 13 | 21 % → 36 % | 71.1 px | 0.55 | 1.76 | 178 |
| stroke 14 | 13 % → 33 % | 43.6 px | 0.75 | 2.46 | 77 |
| stroke 15 | 19 % → 32 % | 69.0 px | 0.75 | 1.66 | 116 |
| stroke 16 | 25 % → 27 % | 57.4 px | 0.60 | 1.05 | 425 |
| stroke 17 | 29 % → 29 % | 74.9 px | 0.61 | 1.00 | 301 |

Numbers say: wet paint spreads well beyond the stroke.

