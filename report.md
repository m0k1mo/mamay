![All brushes](contact.png)

# Brush Lab — 150 brushes · Nov 3, 2026 at 10:11 PM

Every sheet: 1500 × 600, ten strokes in a 5 × 2 grid — 1. light line · 2. heavy line · 3. pressure swell · 4. fast wave · 5. slow wave · 6. spiral · 7. loop · 8. tilted · 9. over the wet one · 10. long, no reload (cell 8 holds «tilted» and «over the wet one» crossed). The CPU reference of Mamay's paint engine; the wet layer settles 20 s at the end.

Columns: **covered** = share of the cell with paint right after the stroke → after settling; **width** = painted area of the stroke ÷ its length (px); **dark** = mean darkness of the painted pixels above the paper's own grain (0 = paper, 1 = black); **spread** = how far wet paint went beyond the stroke (1.0 = stayed); **ms** = the stroke on the CPU; long stroke: paint in each quarter of its length (it should run out: wet → streaks → dry tail).

## Ink Line
Ink · 12 px · 23.4 s

![Ink Line](Ink-Line.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 1 % → 4 % | 4.3 px | 0.55 | 2.44 | 39 |
| heavy line | 5 % → 6 % | 15.7 px | 0.68 | 1.13 | 89 |
| pressure swell | 3 % → 4 % | 11.3 px | 0.64 | 1.40 | 53 |
| fast wave | 10 % → 11 % | 11.2 px | 0.59 | 1.11 | 125 |
| slow wave | 8 % → 10 % | 9.6 px | 0.57 | 1.16 | 144 |
| spiral | 14 % → 15 % | 8.9 px | 0.50 | 1.07 | 222 |
| loop | 8 % → 9 % | 10.6 px | 0.61 | 1.16 | 145 |
| tilted | 5 % → 5 % | 14.4 px | 0.65 | 1.05 | 72 |
| over the wet one | 10 % → 11 % | 12.5 px | 0.65 | 1.15 | 57 |
| long, no reload | 18 % → 17 % | 8.1 px | 0.47 | 0.96 | 305 | quarters: 0.22 → 0.09 → 0.04 → 0.02

Numbers say: light vs heavy: width 4.3 → 15.7 px, dark 0.55 → 0.68; wet paint spreads well beyond the stroke.

## Dense Ink
Ink · 14 px · 24.0 s

![Dense Ink](Dense-Ink.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 5 % → 7 % | 15.2 px | 0.72 | 1.26 | 43 |
| heavy line | 7 % → 7 % | 19.1 px | 0.73 | 1.09 | 83 |
| pressure swell | 5 % → 6 % | 17.9 px | 0.72 | 1.17 | 62 |
| fast wave | 13 % → 13 % | 15.3 px | 0.69 | 1.01 | 129 |
| slow wave | 12 % → 12 % | 13.6 px | 0.67 | 1.04 | 170 |
| spiral | 18 % → 15 % | 12.2 px | 0.65 | 0.80 | 260 |
| loop | 11 % → 12 % | 14.8 px | 0.69 | 1.08 | 207 |
| tilted | 5 % → 6 % | 14.6 px | 0.72 | 1.07 | 72 |
| over the wet one | 12 % → 13 % | 17.7 px | 0.72 | 1.11 | 58 |
| long, no reload | 23 % → 15 % | 10.1 px | 0.64 | 0.66 | 334 | quarters: 0.30 → 0.12 → 0.04 → 0.02

Numbers say: light vs heavy: width 15.2 → 19.1 px, dark 0.72 → 0.73.

## Transparent Wash
Watercolor · 22 px · 24.6 s

![Transparent Wash](Transparent-Wash.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 2 % → 5 % | 6.9 px | 0.27 | 2.25 | 34 |
| heavy line | 7 % → 9 % | 20.4 px | 0.27 | 1.22 | 100 |
| pressure swell | 4 % → 6 % | 15.2 px | 0.28 | 1.54 | 49 |
| fast wave | 14 % → 16 % | 16.1 px | 0.20 | 1.17 | 115 |
| slow wave | 12 % → 15 % | 13.7 px | 0.21 | 1.28 | 197 |
| spiral | 18 % → 22 % | 11.9 px | 0.16 | 1.23 | 188 |
| loop | 11 % → 13 % | 14.5 px | 0.22 | 1.20 | 135 |
| tilted | 8 % → 8 % | 21.1 px | 0.24 | 1.06 | 77 |
| over the wet one | 13 % → 16 % | 16.4 px | 0.24 | 1.18 | 50 |
| long, no reload | 26 % → 32 % | 11.6 px | 0.13 | 1.22 | 280 | quarters: 0.11 → 0.04 → 0.02 → 0.01

Numbers say: light vs heavy: width 6.9 → 20.4 px, dark 0.27 → 0.27; wet paint spreads well beyond the stroke.

## Dry Brush
Gouache · 24 px · 20.0 s

![Dry Brush](Dry-Brush.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 5 % → 0 % | 14.0 px | 0.65 | 0.09 | 50 |
| heavy line | 6 % → 0 % | 18.6 px | 0.65 | 0.02 | 88 |
| pressure swell | 5 % → 0 % | 18.2 px | 0.65 | 0.08 | 58 |
| fast wave | 6 % → 1 % | 7.3 px | 0.65 | 0.08 | 159 |
| slow wave | 7 % → 0 % | 8.1 px | 0.65 | 0.06 | 248 |
| spiral | 7 % → 0 % | 4.6 px | 0.65 | 0.07 | 244 |
| loop | 10 % → 0 % | 12.4 px | 0.65 | 0.04 | 198 |
| tilted | 4 % → 3 % | 10.6 px | 0.65 | 0.88 | 106 |
| over the wet one | 9 % → 1 % | 14.5 px | 0.65 | 0.12 | 90 |
| long, no reload | 6 % → 1 % | 2.9 px | 0.65 | 0.14 | 365 | quarters: 0.12 → 0.00 → 0.00 → 0.00

Numbers say: light vs heavy: width 14.0 → 18.6 px, dark 0.65 → 0.65.

## Wax Crayon
Wax · 8 px · 9.5 s

![Wax Crayon](Wax-Crayon.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 1 % → 1 % | 2.5 px | 0.71 | 1.00 | 18 |
| heavy line | 1 % → 1 % | 3.9 px | 0.69 | 1.00 | 25 |
| pressure swell | 1 % → 1 % | 3.3 px | 0.70 | 1.00 | 18 |
| fast wave | 3 % → 3 % | 3.5 px | 0.69 | 1.00 | 53 |
| slow wave | 3 % → 3 % | 3.4 px | 0.70 | 1.00 | 40 |
| spiral | 5 % → 5 % | 3.3 px | 0.70 | 1.00 | 88 |
| loop | 3 % → 3 % | 3.3 px | 0.70 | 1.00 | 39 |
| tilted | 2 % → 2 % | 5.6 px | 0.68 | 1.00 | 31 |
| over the wet one | 3 % → 3 % | 3.6 px | 0.68 | 1.00 | 17 |
| long, no reload | 7 % → 7 % | 3.3 px | 0.70 | 1.00 | 109 | quarters: 0.06 → 0.06 → 0.06 → 0.06

Numbers say: light vs heavy: width 2.5 → 3.9 px, dark 0.71 → 0.69; the long stroke does not run out of paint.

## Oil Pastel
Wax · 12 px · 9.8 s

![Oil Pastel](Oil-Pastel.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 1 % → 1 % | 4.0 px | 0.68 | 1.00 | 32 |
| heavy line | 2 % → 2 % | 6.5 px | 0.68 | 1.00 | 34 |
| pressure swell | 2 % → 2 % | 5.7 px | 0.69 | 1.00 | 19 |
| fast wave | 5 % → 5 % | 5.7 px | 0.68 | 1.00 | 90 |
| slow wave | 5 % → 5 % | 5.5 px | 0.68 | 1.00 | 62 |
| spiral | 8 % → 8 % | 5.5 px | 0.68 | 1.00 | 102 |
| loop | 4 % → 4 % | 5.6 px | 0.68 | 1.00 | 52 |
| tilted | 2 % → 2 % | 6.8 px | 0.68 | 1.00 | 40 |
| over the wet one | 5 % → 5 % | 5.8 px | 0.68 | 1.00 | 25 |
| long, no reload | 13 % → 13 % | 5.6 px | 0.68 | 1.00 | 152 | quarters: 0.10 → 0.09 → 0.10 → 0.10

Numbers say: light vs heavy: width 4.0 → 6.5 px, dark 0.68 → 0.68; the long stroke does not run out of paint.

## Charcoal
Charcoal · 5 px · 10.3 s

![Charcoal](Charcoal.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 1 % → 1 % | 2.0 px | 0.74 | 1.00 | 11 |
| heavy line | 1 % → 1 % | 3.0 px | 0.74 | 1.00 | 11 |
| pressure swell | 1 % → 1 % | 2.7 px | 0.74 | 1.00 | 11 |
| fast wave | 2 % → 2 % | 2.7 px | 0.73 | 1.00 | 28 |
| slow wave | 2 % → 2 % | 2.6 px | 0.74 | 1.00 | 28 |
| spiral | 4 % → 4 % | 2.5 px | 0.74 | 1.00 | 53 |
| loop | 2 % → 2 % | 2.6 px | 0.74 | 1.00 | 32 |
| tilted | 2 % → 2 % | 4.3 px | 0.72 | 1.00 | 43 |
| over the wet one | 2 % → 2 % | 2.4 px | 0.72 | 1.00 | 35 |
| long, no reload | 6 % → 6 % | 2.7 px | 0.73 | 1.00 | 120 | quarters: 0.05 → 0.05 → 0.05 → 0.05

Numbers say: light vs heavy: width 2.0 → 3.0 px, dark 0.74 → 0.74; the long stroke does not run out of paint.

## Impasto
Heavy acrylic · 22 px · 15.5 s

![Impasto](Impasto.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 8 % → 8 % | 24.1 px | 0.71 | 0.93 | 42 |
| heavy line | 10 % → 9 % | 28.8 px | 0.70 | 0.94 | 97 |
| pressure swell | 7 % → 7 % | 28.1 px | 0.72 | 0.94 | 161 |
| fast wave | 20 % → 13 % | 23.5 px | 0.71 | 0.64 | 330 |
| slow wave | 21 % → 14 % | 24.5 px | 0.71 | 0.66 | 409 |
| spiral | 30 % → 14 % | 20.0 px | 0.71 | 0.46 | 402 |
| loop | 18 % → 14 % | 23.9 px | 0.71 | 0.77 | 140 |
| tilted | 8 % → 8 % | 21.8 px | 0.70 | 1.00 | 85 |
| over the wet one | 17 % → 15 % | 25.4 px | 0.70 | 0.91 | 71 |
| long, no reload | 34 % → 14 % | 15.2 px | 0.71 | 0.41 | 394 | quarters: 0.38 → 0.21 → 0.10 → 0.03

Numbers say: light vs heavy: width 24.1 → 28.8 px, dark 0.71 → 0.70.

## Oil Round
Oil · 18 px · 16.4 s

![Oil Round](Oil-Round.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 2 % → 2 % | 7.2 px | 0.75 | 1.00 | 38 |
| heavy line | 7 % → 7 % | 19.3 px | 0.73 | 1.00 | 75 |
| pressure swell | 4 % → 4 % | 13.7 px | 0.72 | 1.00 | 42 |
| fast wave | 11 % → 11 % | 12.7 px | 0.65 | 1.00 | 169 |
| slow wave | 8 % → 8 % | 9.0 px | 0.57 | 1.00 | 169 |
| spiral | 10 % → 10 % | 6.6 px | 0.50 | 1.00 | 212 |
| loop | 5 % → 5 % | 7.1 px | 0.45 | 1.00 | 161 |
| tilted | 4 % → 4 % | 10.1 px | 0.52 | 1.00 | 93 |
| over the wet one | 6 % → 6 % | 7.4 px | 0.52 | 1.00 | 65 |
| long, no reload | 15 % → 15 % | 6.8 px | 0.42 | 1.00 | 338 | quarters: 0.08 → 0.08 → 0.07 → 0.06

Numbers say: light vs heavy: width 7.2 → 19.3 px, dark 0.75 → 0.73.

## Palette Knife
Oil · 20 px · 16.0 s

![Palette Knife](Palette-Knife.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 8 % → 8 % | 21.9 px | 0.67 | 1.00 | 11 |
| heavy line | 8 % → 8 % | 22.5 px | 0.73 | 1.00 | 13 |
| pressure swell | 6 % → 6 % | 22.4 px | 0.74 | 1.00 | 6 |
| fast wave | 17 % → 17 % | 19.3 px | 0.49 | 1.00 | 26 |
| slow wave | 17 % → 17 % | 19.9 px | 0.43 | 1.00 | 35 |
| spiral | 18 % → 18 % | 11.7 px | 0.45 | 1.00 | 43 |
| loop | 16 % → 16 % | 21.0 px | 0.58 | 1.00 | 30 |
| tilted | 5 % → 5 % | 15.0 px | 0.72 | 1.00 | 12 |
| over the wet one | 13 % → 13 % | 21.0 px | 0.72 | 1.00 | 13 |
| long, no reload | 17 % → 17 % | 7.5 px | 0.47 | 1.00 | 58 | quarters: 0.29 → 0.05 → 0.00 → 0.00

Numbers say: light vs heavy: width 21.9 → 22.5 px, dark 0.67 → 0.73; pressure barely changes the width.

## Water
Watercolor · 20 px · 31.9 s · over bands of wet oil paint and oil pastel in turn (it works on paint already there: look at what it does to the bands; covered counts the bands too)

![Water](Water.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 25 % → 27 % | 73.8 px | 0.80 | 1.06 | 25 |
| heavy line | 24 % → 25 % | 69.8 px | 0.81 | 1.04 | 55 |
| pressure swell | 24 % → 25 % | 89.6 px | 0.81 | 1.03 | 36 |
| fast wave | 24 % → 26 % | 27.7 px | 0.81 | 1.07 | 107 |
| slow wave | 24 % → 25 % | 27.7 px | 0.81 | 1.06 | 142 |
| spiral | 24 % → 26 % | 15.9 px | 0.81 | 1.07 | 162 |
| loop | 24 % → 25 % | 31.1 px | 0.81 | 1.03 | 123 |
| tilted | 24 % → 24 % | 67.0 px | 0.81 | 1.00 | 54 |
| over the wet one | 24 % → 25 % | 0.0 px | 0.81 | 1.06 | 42 |
| long, no reload | 24 % → 26 % | 10.7 px | 0.81 | 1.08 | 255 | quarters: 0.21 → 0.27 → 0.18 → 0.27

Numbers say: light vs heavy: width 73.8 → 69.8 px, dark 0.80 → 0.81; pressure barely changes the width; the long stroke does not run out of paint.

## Blender
Pastel · 16 px · 19.1 s · over bands of wet oil paint and oil pastel in turn (it works on paint already there: look at what it does to the bands; covered counts the bands too)

![Blender](Blender.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 24 % → 24 % | 70.7 px | 0.81 | 1.00 | 21 |
| heavy line | 25 % → 25 % | 72.1 px | 0.80 | 1.00 | 35 |
| pressure swell | 24 % → 24 % | 91.3 px | 0.81 | 1.00 | 23 |
| fast wave | 26 % → 26 % | 30.0 px | 0.79 | 1.00 | 75 |
| slow wave | 26 % → 26 % | 29.9 px | 0.80 | 1.00 | 85 |
| spiral | 28 % → 28 % | 18.7 px | 0.77 | 1.00 | 123 |
| loop | 25 % → 25 % | 32.9 px | 0.80 | 1.00 | 69 |
| tilted | 25 % → 25 % | 70.1 px | 0.79 | 1.00 | 44 |
| over the wet one | 26 % → 26 % | 1.8 px | 0.79 | 1.00 | 31 |
| long, no reload | 30 % → 30 % | 13.7 px | 0.76 | 1.00 | 195 | quarters: 0.20 → 0.28 → 0.23 → 0.30

Numbers say: light vs heavy: width 70.7 → 72.1 px, dark 0.81 → 0.80; pressure barely changes the width; the long stroke does not run out of paint.

## Eraser
Eraser · 16 px · 18.8 s · over bands of wet oil paint and oil pastel in turn (it works on paint already there: look at what it does to the bands; covered counts the bands too)

![Eraser](Eraser.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 24 % → 24 % | 69.5 px | 0.82 | 1.00 | 25 |
| heavy line | 23 % → 23 % | 67.9 px | 0.82 | 1.00 | 36 |
| pressure swell | 23 % → 23 % | 87.3 px | 0.82 | 1.00 | 27 |
| fast wave | 22 % → 22 % | 25.7 px | 0.82 | 1.00 | 76 |
| slow wave | 22 % → 22 % | 25.7 px | 0.82 | 1.00 | 89 |
| spiral | 22 % → 22 % | 14.4 px | 0.82 | 1.00 | 121 |
| loop | 22 % → 22 % | 28.6 px | 0.82 | 1.00 | 71 |
| tilted | 23 % → 23 % | 65.1 px | 0.82 | 1.00 | 42 |
| over the wet one | 23 % → 23 % | 0.0 px | 0.82 | 1.00 | 32 |
| long, no reload | 20 % → 20 % | 8.9 px | 0.82 | 1.00 | 196 | quarters: 0.15 → 0.20 → 0.15 → 0.20

Numbers say: light vs heavy: width 69.5 → 67.9 px, dark 0.82 → 0.82; pressure barely changes the width; the long stroke does not run out of paint.

## Fan
Gouache · 30 px · 34.5 s

![Fan](Fan.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 9 % → 3 % | 25.7 px | 0.63 | 0.37 | 35 |
| heavy line | 11 % → 4 % | 31.0 px | 0.63 | 0.39 | 54 |
| pressure swell | 8 % → 5 % | 31.7 px | 0.63 | 0.55 | 43 |
| fast wave | 18 % → 5 % | 20.3 px | 0.63 | 0.26 | 176 |
| slow wave | 18 % → 5 % | 21.1 px | 0.63 | 0.25 | 368 |
| spiral | 24 % → 5 % | 15.8 px | 0.63 | 0.20 | 171 |
| loop | 17 % → 5 % | 22.7 px | 0.63 | 0.29 | 87 |
| tilted | 5 % → 6 % | 15.1 px | 0.63 | 1.05 | 45 |
| over the wet one | 16 % → 8 % | 29.8 px | 0.63 | 0.50 | 45 |
| long, no reload | 23 % → 5 % | 10.1 px | 0.63 | 0.22 | 337 | quarters: 0.29 → 0.07 → 0.01 → 0.00

Numbers say: light vs heavy: width 25.7 → 31.0 px, dark 0.63 → 0.63.

## Sponge
Gouache · 30 px · 34.3 s

![Sponge](Sponge.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 4 % → 0 % | 11.4 px | 0.62 | 0.12 | 35 |
| heavy line | 12 % → 2 % | 35.4 px | 0.62 | 0.14 | 68 |
| pressure swell | 7 % → 2 % | 27.9 px | 0.62 | 0.27 | 43 |
| fast wave | 20 % → 4 % | 23.2 px | 0.62 | 0.19 | 200 |
| slow wave | 21 % → 4 % | 23.7 px | 0.62 | 0.18 | 281 |
| spiral | 28 % → 4 % | 18.3 px | 0.62 | 0.14 | 189 |
| loop | 18 % → 5 % | 23.0 px | 0.62 | 0.29 | 103 |
| tilted | 7 % → 7 % | 18.2 px | 0.62 | 1.04 | 115 |
| over the wet one | 16 % → 6 % | 27.8 px | 0.62 | 0.37 | 84 |
| long, no reload | 29 % → 5 % | 12.9 px | 0.62 | 0.17 | 416 | quarters: 0.29 → 0.13 → 0.07 → 0.04

Numbers say: light vs heavy: width 11.4 → 35.4 px, dark 0.62 → 0.62.

## Ink — sumi brush
Watercolor · 22 px · 36.7 s

![Ink — sumi brush](Ink-sumi-brush.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 8 % → 9 % | 23.8 px | 0.77 | 1.13 | 81 |
| heavy line | 13 % → 13 % | 38.0 px | 0.72 | 1.01 | 145 |
| pressure swell | 9 % → 10 % | 34.5 px | 0.75 | 1.05 | 49 |
| fast wave | 27 % → 28 % | 31.7 px | 0.58 | 1.03 | 155 |
| slow wave | 25 % → 26 % | 29.0 px | 0.61 | 1.05 | 246 |
| spiral | 37 % → 38 % | 24.3 px | 0.51 | 1.03 | 342 |
| loop | 22 % → 22 % | 28.2 px | 0.66 | 1.03 | 170 |
| tilted | 9 % → 9 % | 24.7 px | 0.73 | 1.03 | 100 |
| over the wet one | 20 % → 21 % | 31.1 px | 0.73 | 1.03 | 70 |
| long, no reload | 42 % → 43 % | 18.9 px | 0.46 | 1.02 | 537 | quarters: 0.47 → 0.23 → 0.11 → 0.06

Numbers say: light vs heavy: width 23.8 → 38.0 px, dark 0.77 → 0.72.

## Ink — wash
Watercolor · 40 px · 45.3 s

![Ink — wash](Ink-wash.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 13 % → 13 % | 36.5 px | 0.17 | 1.04 | 114 |
| heavy line | 18 % → 19 % | 53.5 px | 0.13 | 1.04 | 124 |
| pressure swell | 12 % → 13 % | 46.6 px | 0.16 | 1.05 | 63 |
| fast wave | 40 % → 42 % | 45.9 px | 0.12 | 1.06 | 283 |
| slow wave | 38 % → 40 % | 43.6 px | 0.17 | 1.06 | 564 |
| spiral | 58 % → 62 % | 38.5 px | 0.12 | 1.06 | 429 |
| loop | 33 % → 34 % | 42.9 px | 0.15 | 1.03 | 220 |
| tilted | 14 % → 14 % | 38.1 px | 0.17 | 1.03 | 144 |
| over the wet one | 29 % → 31 % | 43.2 px | 0.17 | 1.06 | 119 |
| long, no reload | 66 % → 75 % | 29.8 px | 0.12 | 1.12 | 793 | quarters: 0.16 → 0.11 → 0.07 → 0.04

Numbers say: light vs heavy: width 36.5 → 53.5 px, dark 0.17 → 0.13.

## Ink — dry brush
Ink · 30 px · 31.9 s

![Ink — dry brush](Ink-dry-brush.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 9 % → 7 % | 25.2 px | 0.81 | 0.79 | 121 |
| heavy line | 10 % → 8 % | 29.6 px | 0.80 | 0.76 | 180 |
| pressure swell | 7 % → 6 % | 27.9 px | 0.81 | 0.85 | 123 |
| fast wave | 21 % → 8 % | 24.2 px | 0.79 | 0.40 | 295 |
| slow wave | 18 % → 7 % | 20.3 px | 0.79 | 0.39 | 658 |
| spiral | 24 % → 8 % | 15.6 px | 0.78 | 0.34 | 469 |
| loop | 19 % → 8 % | 24.3 px | 0.78 | 0.45 | 280 |
| tilted | 8 % → 8 % | 22.2 px | 0.78 | 1.02 | 176 |
| over the wet one | 17 % → 14 % | 25.9 px | 0.78 | 0.81 | 145 |
| long, no reload | 20 % → 8 % | 9.1 px | 0.79 | 0.41 | 740 | quarters: 0.32 → 0.02 → 0.00 → 0.00

Numbers say: light vs heavy: width 25.2 → 29.6 px, dark 0.81 → 0.80.

## Ink — nib
Watercolor · 5 px · 30.1 s

![Ink — nib](Ink-nib.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 2 % → 5 % | 5.4 px | 0.86 | 2.45 | 46 |
| heavy line | 2 % → 5 % | 6.4 px | 0.86 | 2.33 | 37 |
| pressure swell | 2 % → 4 % | 6.2 px | 0.86 | 2.52 | 28 |
| fast wave | 5 % → 8 % | 5.8 px | 0.82 | 1.65 | 80 |
| slow wave | 5 % → 8 % | 5.6 px | 0.82 | 1.73 | 96 |
| spiral | 7 % → 11 % | 4.8 px | 0.75 | 1.45 | 179 |
| loop | 4 % → 8 % | 5.6 px | 0.84 | 1.75 | 80 |
| tilted | 4 % → 4 % | 10.1 px | 0.85 | 1.04 | 52 |
| over the wet one | 6 % → 9 % | 6.3 px | 0.85 | 1.61 | 31 |
| long, no reload | 9 % → 12 % | 4.0 px | 0.70 | 1.37 | 282 | quarters: 0.23 → 0.08 → 0.04 → 0.02

Numbers say: light vs heavy: width 5.4 → 6.4 px, dark 0.86 → 0.86; wet paint spreads well beyond the stroke.

## 0.45 · Dry brush
Gouache · 34 px · 31.5 s

![0.45 · Dry brush](0-45-Dry-brush.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 10 % → 3 % | 29.4 px | 0.67 | 0.27 | 169 |
| heavy line | 11 % → 3 % | 31.6 px | 0.67 | 0.29 | 166 |
| pressure swell | 8 % → 3 % | 31.5 px | 0.67 | 0.41 | 115 |
| fast wave | 19 % → 3 % | 22.5 px | 0.67 | 0.18 | 410 |
| slow wave | 20 % → 4 % | 23.2 px | 0.67 | 0.18 | 665 |
| spiral | 21 % → 3 % | 14.1 px | 0.67 | 0.16 | 711 |
| loop | 20 % → 4 % | 26.1 px | 0.67 | 0.20 | 557 |
| tilted | 9 % → 8 % | 24.0 px | 0.67 | 0.98 | 217 |
| over the wet one | 19 % → 6 % | 28.2 px | 0.67 | 0.34 | 186 |
| long, no reload | 20 % → 4 % | 9.1 px | 0.67 | 0.19 | 1078 | quarters: 0.36 → 0.10 → 0.00 → 0.00

Numbers say: light vs heavy: width 29.4 → 31.6 px, dark 0.67 → 0.67; pressure barely changes the width.

## Dry pastel
Pastel · 26 px · 14.2 s

![Dry pastel](Dry-pastel.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 3 % → 3 % | 8.3 px | 0.38 | 1.00 | 41 |
| heavy line | 5 % → 5 % | 13.2 px | 0.39 | 1.00 | 47 |
| pressure swell | 3 % → 3 % | 11.7 px | 0.38 | 1.00 | 31 |
| fast wave | 10 % → 10 % | 11.9 px | 0.39 | 1.00 | 109 |
| slow wave | 10 % → 10 % | 11.3 px | 0.39 | 1.00 | 218 |
| spiral | 15 % → 15 % | 9.6 px | 0.39 | 1.00 | 220 |
| loop | 7 % → 7 % | 9.4 px | 0.39 | 1.00 | 105 |
| tilted | 3 % → 3 % | 8.3 px | 0.38 | 1.00 | 53 |
| over the wet one | 7 % → 7 % | 11.1 px | 0.38 | 1.00 | 54 |
| long, no reload | 18 % → 18 % | 8.2 px | 0.39 | 1.00 | 414 | quarters: 0.08 → 0.08 → 0.08 → 0.07

Numbers say: light vs heavy: width 8.3 → 13.2 px, dark 0.38 → 0.39; the long stroke does not run out of paint.

## 0.45 · Charcoal
Charcoal · 18 px · 13.7 s

![0.45 · Charcoal](0-45-Charcoal.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 2 % → 2 % | 6.5 px | 0.80 | 1.00 | 19 |
| heavy line | 3 % → 3 % | 9.2 px | 0.80 | 1.00 | 29 |
| pressure swell | 2 % → 2 % | 8.8 px | 0.80 | 1.00 | 18 |
| fast wave | 7 % → 7 % | 8.5 px | 0.80 | 1.00 | 53 |
| slow wave | 7 % → 7 % | 8.0 px | 0.80 | 1.00 | 109 |
| spiral | 12 % → 12 % | 7.9 px | 0.80 | 1.00 | 93 |
| loop | 6 % → 6 % | 8.1 px | 0.80 | 1.00 | 58 |
| tilted | 3 % → 3 % | 7.5 px | 0.80 | 1.00 | 53 |
| over the wet one | 6 % → 6 % | 7.9 px | 0.80 | 1.00 | 35 |
| long, no reload | 17 % → 17 % | 7.8 px | 0.80 | 1.00 | 164 | quarters: 0.15 → 0.16 → 0.15 → 0.16

Numbers say: light vs heavy: width 6.5 → 9.2 px, dark 0.80 → 0.80; the long stroke does not run out of paint.

## Watercolour — wash
Watercolor · 50 px · 49.2 s

![Watercolour — wash](Watercolour-wash.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 15 % → 16 % | 43.3 px | 0.03 | 1.05 | 162 |
| heavy line | 21 % → 22 % | 62.1 px | 0.03 | 1.04 | 158 |
| pressure swell | 14 % → 15 % | 54.3 px | 0.03 | 1.04 | 125 |
| fast wave | 47 % → 49 % | 53.8 px | 0.02 | 1.04 | 495 |
| slow wave | 45 % → 46 % | 52.0 px | 0.04 | 1.03 | 649 |
| spiral | 64 % → 66 % | 42.5 px | 0.03 | 1.03 | 647 |
| loop | 39 % → 40 % | 50.3 px | 0.03 | 1.02 | 374 |
| tilted | 17 % → 17 % | 47.3 px | 0.04 | 1.03 | 201 |
| over the wet one | 35 % → 36 % | 49.0 px | 0.04 | 1.04 | 164 |
| long, no reload | 79 % → 84 % | 35.5 px | 0.03 | 1.06 | 950 | quarters: 0.04 → 0.03 → 0.02 → 0.01

Numbers say: light vs heavy: width 43.3 → 62.1 px, dark 0.03 → 0.03.

## Watercolour — wet-in-wet
Watercolor · 44 px · 49.2 s

![Watercolour — wet-in-wet](Watercolour-wet-in-wet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 13 % → 19 % | 36.6 px | 0.05 | 1.51 | 131 |
| heavy line | 18 % → 20 % | 52.4 px | 0.05 | 1.09 | 128 |
| pressure swell | 12 % → 15 % | 44.9 px | 0.06 | 1.26 | 101 |
| fast wave | 40 % → 45 % | 45.9 px | 0.05 | 1.13 | 303 |
| slow wave | 39 % → 45 % | 45.0 px | 0.07 | 1.15 | 545 |
| spiral | 62 % → 67 % | 40.8 px | 0.06 | 1.08 | 905 |
| loop | 33 % → 37 % | 43.2 px | 0.06 | 1.12 | 391 |
| tilted | 14 % → 14 % | 39.1 px | 0.06 | 1.03 | 194 |
| over the wet one | 29 % → 37 % | 41.7 px | 0.06 | 1.28 | 123 |
| long, no reload | 75 % → 84 % | 33.6 px | 0.06 | 1.12 | 731 | quarters: 0.07 → 0.06 → 0.04 → 0.03

Numbers say: light vs heavy: width 36.6 → 52.4 px, dark 0.05 → 0.05; wet paint spreads well beyond the stroke.

## Watercolour — glaze
Watercolor · 38 px · 45.2 s

![Watercolour — glaze](Watercolour-glaze.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 12 % → 13 % | 35.2 px | 0.03 | 1.05 | 111 |
| heavy line | 18 % → 19 % | 52.2 px | 0.02 | 1.06 | 260 |
| pressure swell | 12 % → 13 % | 44.6 px | 0.02 | 1.07 | 157 |
| fast wave | 37 % → 40 % | 42.4 px | 0.02 | 1.08 | 552 |
| slow wave | 35 % → 37 % | 40.2 px | 0.02 | 1.08 | 433 |
| spiral | 54 % → 59 % | 35.9 px | 0.02 | 1.09 | 498 |
| loop | 32 % → 33 % | 40.8 px | 0.02 | 1.05 | 221 |
| tilted | 13 % → 14 % | 37.0 px | 0.03 | 1.03 | 162 |
| over the wet one | 28 % → 30 % | 41.7 px | 0.03 | 1.06 | 112 |
| long, no reload | 60 % → 69 % | 26.8 px | 0.02 | 1.15 | 870 | quarters: 0.02 → 0.01 → 0.01 → 0.00

Numbers say: light vs heavy: width 35.2 → 52.2 px, dark 0.03 → 0.02.

## Watercolour — granulating
Watercolor · 44 px · 44.9 s

![Watercolour — granulating](Watercolour-granulating.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 14 % → 14 % | 40.5 px | 0.05 | 1.03 | 128 |
| heavy line | 20 % → 21 % | 59.2 px | 0.04 | 1.02 | 173 |
| pressure swell | 14 % → 14 % | 51.3 px | 0.05 | 1.02 | 119 |
| fast wave | 44 % → 45 % | 50.3 px | 0.04 | 1.04 | 348 |
| slow wave | 40 % → 42 % | 46.0 px | 0.06 | 1.06 | 517 |
| spiral | 59 % → 63 % | 38.7 px | 0.04 | 1.07 | 500 |
| loop | 36 % → 37 % | 46.9 px | 0.05 | 1.02 | 233 |
| tilted | 15 % → 16 % | 43.1 px | 0.06 | 1.03 | 176 |
| over the wet one | 32 % → 33 % | 46.6 px | 0.06 | 1.04 | 125 |
| long, no reload | 68 % → 76 % | 30.3 px | 0.04 | 1.12 | 823 | quarters: 0.06 → 0.04 → 0.02 → 0.02

Numbers say: light vs heavy: width 40.5 → 59.2 px, dark 0.05 → 0.04.

## Watercolour — dry brush
Watercolor · 36 px · 36.2 s

![Watercolour — dry brush](Watercolour-dry-brush.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 9 % → 9 % | 24.9 px | 0.07 | 1.09 | 126 |
| heavy line | 13 % → 13 % | 36.7 px | 0.06 | 0.99 | 142 |
| pressure swell | 10 % → 10 % | 36.4 px | 0.06 | 1.04 | 112 |
| fast wave | 24 % → 19 % | 27.3 px | 0.05 | 0.82 | 352 |
| slow wave | 22 % → 17 % | 25.2 px | 0.05 | 0.78 | 810 |
| spiral | 29 % → 20 % | 19.3 px | 0.05 | 0.67 | 553 |
| loop | 19 % → 18 % | 24.6 px | 0.05 | 0.94 | 295 |
| tilted | 9 % → 10 % | 24.3 px | 0.06 | 1.10 | 142 |
| over the wet one | 20 % → 20 % | 31.7 px | 0.06 | 0.99 | 135 |
| long, no reload | 28 % → 19 % | 12.4 px | 0.05 | 0.70 | 757 | quarters: 0.03 → 0.01 → 0.00 → 0.00

Numbers say: light vs heavy: width 24.9 → 36.7 px, dark 0.07 → 0.06.

## Gouache
Gouache · 30 px · 34.3 s

![Gouache](Gouache.png)

A light paint: laid on a grey sheet (on white it cannot be seen); **dark** = how far it is from the grey either way.

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 8 % → 5 % | 24.4 px | 0.28 | 0.64 | 103 |
| heavy line | 14 % → 6 % | 39.7 px | 0.28 | 0.47 | 124 |
| pressure swell | 10 % → 6 % | 38.6 px | 0.28 | 0.60 | 82 |
| fast wave | 28 % → 7 % | 32.2 px | 0.28 | 0.25 | 359 |
| slow wave | 27 % → 8 % | 31.4 px | 0.28 | 0.29 | 471 |
| spiral | 38 % → 8 % | 24.8 px | 0.27 | 0.22 | 484 |
| loop | 22 % → 8 % | 28.6 px | 0.28 | 0.35 | 234 |
| tilted | 9 % → 9 % | 23.8 px | 0.27 | 1.01 | 126 |
| over the wet one | 20 % → 13 % | 31.1 px | 0.27 | 0.66 | 108 |
| long, no reload | 40 % → 9 % | 17.9 px | 0.27 | 0.24 | 650 | quarters: 0.01 → 0.01 → 0.02 → 0.02

Numbers say: light vs heavy: width 24.4 → 39.7 px, dark 0.28 → 0.28; the long stroke does not run out of paint.

## Oil — alla prima
Oil · 30 px · 19.6 s

![Oil — alla prima](Oil-alla-prima.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 10 % → 10 % | 27.6 px | 0.51 | 1.00 | 171 |
| heavy line | 10 % → 10 % | 30.4 px | 0.51 | 1.00 | 117 |
| pressure swell | 8 % → 8 % | 29.9 px | 0.53 | 1.00 | 103 |
| fast wave | 24 % → 24 % | 28.1 px | 0.51 | 1.00 | 315 |
| slow wave | 26 % → 26 % | 29.6 px | 0.51 | 1.00 | 507 |
| spiral | 40 % → 40 % | 26.4 px | 0.51 | 1.00 | 529 |
| loop | 21 % → 21 % | 27.7 px | 0.52 | 1.00 | 454 |
| tilted | 11 % → 11 % | 30.4 px | 0.51 | 1.00 | 215 |
| over the wet one | 20 % → 20 % | 26.6 px | 0.51 | 1.00 | 201 |
| long, no reload | 49 % → 49 % | 22.0 px | 0.50 | 1.00 | 747 | quarters: 0.32 → 0.29 → 0.26 → 0.22

Numbers say: light vs heavy: width 27.6 → 30.4 px, dark 0.51 → 0.51; pressure barely changes the width.

## Oil — impasto
Oil · 34 px · 25.8 s

![Oil — impasto](Oil-impasto.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 12 % → 12 % | 33.5 px | 0.24 | 1.00 | 183 |
| heavy line | 13 % → 13 % | 36.4 px | 0.23 | 1.00 | 156 |
| pressure swell | 10 % → 10 % | 35.9 px | 0.26 | 1.00 | 130 |
| fast wave | 30 % → 30 % | 35.1 px | 0.24 | 1.00 | 365 |
| slow wave | 31 % → 31 % | 35.8 px | 0.24 | 1.00 | 741 |
| spiral | 52 % → 52 % | 34.1 px | 0.22 | 1.00 | 883 |
| loop | 26 % → 26 % | 33.7 px | 0.24 | 1.00 | 366 |
| tilted | 12 % → 12 % | 32.8 px | 0.24 | 1.00 | 169 |
| over the wet one | 23 % → 23 % | 32.0 px | 0.24 | 1.00 | 170 |
| long, no reload | 60 % → 60 % | 27.0 px | 0.22 | 1.00 | 1030 | quarters: 0.18 → 0.16 → 0.13 → 0.10

Numbers say: light vs heavy: width 33.5 → 36.4 px, dark 0.24 → 0.23; pressure barely changes the width.

## Oil — glaze
Oil · 40 px · 21.7 s

![Oil — glaze](Oil-glaze.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 9 % → 9 % | 25.4 px | 0.50 | 1.00 | 141 |
| heavy line | 13 % → 13 % | 36.3 px | 0.49 | 1.00 | 183 |
| pressure swell | 9 % → 9 % | 35.3 px | 0.50 | 1.00 | 94 |
| fast wave | 26 % → 26 % | 30.1 px | 0.48 | 1.00 | 372 |
| slow wave | 29 % → 29 % | 33.7 px | 0.49 | 1.00 | 931 |
| spiral | 44 % → 44 % | 29.0 px | 0.49 | 1.00 | 896 |
| loop | 23 % → 23 % | 30.2 px | 0.50 | 1.00 | 348 |
| tilted | 10 % → 10 % | 28.9 px | 0.50 | 1.00 | 157 |
| over the wet one | 22 % → 22 % | 31.6 px | 0.50 | 1.00 | 179 |
| long, no reload | 51 % → 51 % | 22.7 px | 0.49 | 1.00 | 1016 | quarters: 0.33 → 0.29 → 0.26 → 0.22

Numbers say: light vs heavy: width 25.4 → 36.3 px, dark 0.50 → 0.49.

## Oil — scumble
Oil · 36 px · 20.5 s

![Oil — scumble](Oil-scumble.png)

A light paint: laid on a grey sheet (on white it cannot be seen); **dark** = how far it is from the grey either way.

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 11 % → 11 % | 33.1 px | 0.28 | 1.00 | 158 |
| heavy line | 12 % → 12 % | 36.1 px | 0.28 | 1.00 | 165 |
| pressure swell | 9 % → 9 % | 35.5 px | 0.28 | 1.00 | 144 |
| fast wave | 26 % → 26 % | 29.6 px | 0.19 | 1.00 | 421 |
| slow wave | 27 % → 27 % | 30.9 px | 0.18 | 1.00 | 738 |
| spiral | 41 % → 41 % | 27.1 px | 0.13 | 1.00 | 767 |
| loop | 24 % → 24 % | 30.7 px | 0.20 | 1.00 | 366 |
| tilted | 11 % → 11 % | 30.5 px | 0.25 | 1.00 | 245 |
| over the wet one | 22 % → 22 % | 31.5 px | 0.25 | 1.00 | 164 |
| long, no reload | 45 % → 45 % | 20.3 px | 0.12 | 1.00 | 1093 | quarters: 0.00 → 0.00 → 0.00 → 0.00

Numbers say: light vs heavy: width 33.1 → 36.1 px, dark 0.28 → 0.28; pressure barely changes the width.

## Acrylic — heavy body
Heavy acrylic · 30 px · 20.2 s

![Acrylic — heavy body](Acrylic-heavy-body.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 10 % → 9 % | 29.0 px | 0.51 | 0.90 | 141 |
| heavy line | 11 % → 10 % | 31.2 px | 0.51 | 0.92 | 143 |
| pressure swell | 8 % → 8 % | 30.8 px | 0.53 | 0.94 | 89 |
| fast wave | 23 % → 15 % | 26.5 px | 0.52 | 0.64 | 295 |
| slow wave | 24 % → 16 % | 27.8 px | 0.51 | 0.64 | 557 |
| spiral | 35 % → 15 % | 23.3 px | 0.51 | 0.43 | 560 |
| loop | 21 % → 16 % | 26.9 px | 0.51 | 0.76 | 266 |
| tilted | 9 % → 9 % | 24.9 px | 0.51 | 0.99 | 182 |
| over the wet one | 19 % → 17 % | 27.8 px | 0.51 | 0.89 | 210 |
| long, no reload | 39 % → 16 % | 17.3 px | 0.51 | 0.41 | 895 | quarters: 0.29 → 0.20 → 0.12 → 0.04

Numbers say: light vs heavy: width 29.0 → 31.2 px, dark 0.51 → 0.51; pressure barely changes the width.

## Acrylic — fluid
Watercolor · 36 px · 44.4 s

![Acrylic — fluid](Acrylic-fluid.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 12 % → 12 % | 34.3 px | 0.08 | 1.02 | 109 |
| heavy line | 18 % → 18 % | 51.6 px | 0.07 | 1.01 | 118 |
| pressure swell | 12 % → 12 % | 44.8 px | 0.08 | 1.01 | 98 |
| fast wave | 37 % → 38 % | 42.6 px | 0.07 | 1.02 | 286 |
| slow wave | 34 % → 35 % | 39.2 px | 0.07 | 1.03 | 459 |
| spiral | 52 % → 53 % | 34.2 px | 0.07 | 1.03 | 464 |
| loop | 30 % → 31 % | 39.4 px | 0.07 | 1.02 | 224 |
| tilted | 12 % → 12 % | 32.6 px | 0.08 | 1.04 | 143 |
| over the wet one | 27 % → 28 % | 43.2 px | 0.08 | 1.02 | 118 |
| long, no reload | 56 % → 58 % | 25.3 px | 0.06 | 1.04 | 671 | quarters: 0.06 → 0.05 → 0.03 → 0.02

Numbers say: light vs heavy: width 34.3 → 51.6 px, dark 0.08 → 0.07.

## Acrylic — palette knife
Heavy acrylic · 42 px · 28.2 s

![Acrylic — palette knife](Acrylic-palette-knife.png)

A light paint: laid on a grey sheet (on white it cannot be seen); **dark** = how far it is from the grey either way.

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 15 % → 15 % | 44.0 px | 0.39 | 0.98 | 63 |
| heavy line | 15 % → 15 % | 44.2 px | 0.40 | 0.97 | 42 |
| pressure swell | 12 % → 12 % | 43.5 px | 0.42 | 0.99 | 24 |
| fast wave | 36 % → 20 % | 41.9 px | 0.36 | 0.56 | 75 |
| slow wave | 37 % → 21 % | 42.6 px | 0.37 | 0.57 | 151 |
| spiral | 50 % → 18 % | 32.7 px | 0.37 | 0.37 | 127 |
| loop | 32 % → 24 % | 41.2 px | 0.36 | 0.75 | 64 |
| tilted | 12 % → 12 % | 33.6 px | 0.39 | 1.00 | 30 |
| over the wet one | 26 % → 25 % | 39.7 px | 0.39 | 0.97 | 31 |
| long, no reload | 57 % → 21 % | 25.6 px | 0.34 | 0.36 | 198 | quarters: 0.00 → 0.00 → 0.00 → 0.01

Numbers say: light vs heavy: width 44.0 → 44.2 px, dark 0.39 → 0.40; pressure barely changes the width; the long stroke does not run out of paint.

## Finger on oil
Oil · 30 px · 18.3 s

![Finger on oil](Finger-on-oil.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 8 % → 8 % | 23.8 px | 0.41 | 1.00 | 75 |
| heavy line | 13 % → 13 % | 36.6 px | 0.39 | 1.00 | 85 |
| pressure swell | 9 % → 9 % | 33.4 px | 0.41 | 1.00 | 56 |
| fast wave | 22 % → 22 % | 26.0 px | 0.35 | 1.00 | 157 |
| slow wave | 24 % → 24 % | 27.9 px | 0.35 | 1.00 | 321 |
| spiral | 36 % → 36 % | 23.5 px | 0.28 | 1.00 | 280 |
| loop | 21 % → 21 % | 27.4 px | 0.36 | 1.00 | 169 |
| tilted | 10 % → 10 % | 26.5 px | 0.40 | 1.00 | 95 |
| over the wet one | 20 % → 20 % | 29.4 px | 0.40 | 1.00 | 84 |
| long, no reload | 37 % → 37 % | 16.4 px | 0.26 | 1.00 | 691 | quarters: 0.23 → 0.11 → 0.05 → 0.02

Numbers say: light vs heavy: width 23.8 → 36.6 px, dark 0.41 → 0.39.

## Palette knife — oil
Oil · 44 px · 24.9 s

![Palette knife — oil](Palette-knife-oil.png)

A light paint: laid on a grey sheet (on white it cannot be seen); **dark** = how far it is from the grey either way.

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 16 % → 16 % | 45.6 px | 0.36 | 1.00 | 43 |
| heavy line | 16 % → 16 % | 46.3 px | 0.38 | 1.00 | 36 |
| pressure swell | 12 % → 12 % | 45.2 px | 0.38 | 1.00 | 17 |
| fast wave | 39 % → 39 % | 44.9 px | 0.34 | 1.01 | 146 |
| slow wave | 39 % → 39 % | 45.4 px | 0.35 | 1.00 | 346 |
| spiral | 62 % → 62 % | 40.9 px | 0.27 | 1.00 | 244 |
| loop | 34 % → 34 % | 43.8 px | 0.35 | 1.00 | 77 |
| tilted | 13 % → 13 % | 36.6 px | 0.37 | 1.00 | 35 |
| over the wet one | 28 % → 28 % | 40.8 px | 0.37 | 1.00 | 37 |
| long, no reload | 74 % → 74 % | 33.1 px | 0.25 | 1.00 | 178 | quarters: 0.00 → 0.00 → 0.00 → 0.00

Numbers say: light vs heavy: width 45.6 → 46.3 px, dark 0.36 → 0.38; pressure barely changes the width; the long stroke does not run out of paint.

## 0.45 · Sponge
Watercolor · 46 px · 43.5 s

![0.45 · Sponge](0-45-Sponge.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 23 % → 15 % | 66.4 px | 0.02 | 0.67 | 85 |
| heavy line | 28 % → 23 % | 81.1 px | 0.02 | 0.81 | 104 |
| pressure swell | 20 % → 16 % | 76.7 px | 0.03 | 0.76 | 71 |
| fast wave | 46 % → 32 % | 53.0 px | 0.03 | 0.70 | 245 |
| slow wave | 53 % → 46 % | 60.7 px | 0.04 | 0.87 | 448 |
| spiral | 65 % → 53 % | 42.6 px | 0.04 | 0.82 | 389 |
| loop | 46 % → 40 % | 60.1 px | 0.04 | 0.86 | 233 |
| tilted | 16 % → 17 % | 43.8 px | 0.05 | 1.07 | 135 |
| over the wet one | 40 % → 35 % | 67.3 px | 0.05 | 0.89 | 84 |
| long, no reload | 74 % → 65 % | 33.2 px | 0.04 | 0.88 | 566 | quarters: 0.05 → 0.04 → 0.03 → 0.02

Numbers say: light vs heavy: width 66.4 → 81.1 px, dark 0.02 → 0.02.

## 0.45 · Eraser
Eraser · 30 px · 25.8 s · over bands of wet oil paint and oil pastel in turn (it works on paint already there: look at what it does to the bands; covered counts the bands too)

![0.45 · Eraser](0-45-Eraser.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 24 % → 24 % | 69.2 px | 0.82 | 1.00 | 51 |
| heavy line | 23 % → 23 % | 67.4 px | 0.81 | 1.00 | 74 |
| pressure swell | 23 % → 23 % | 86.7 px | 0.82 | 1.00 | 46 |
| fast wave | 21 % → 21 % | 24.7 px | 0.81 | 1.00 | 245 |
| slow wave | 20 % → 20 % | 23.5 px | 0.82 | 1.00 | 266 |
| spiral | 20 % → 20 % | 13.5 px | 0.79 | 1.00 | 252 |
| loop | 21 % → 21 % | 27.8 px | 0.80 | 1.00 | 158 |
| tilted | 23 % → 23 % | 64.8 px | 0.81 | 1.00 | 69 |
| over the wet one | 22 % → 22 % | 0.0 px | 0.81 | 1.00 | 68 |
| long, no reload | 17 % → 17 % | 7.5 px | 0.79 | 1.00 | 411 | quarters: 0.13 → 0.16 → 0.13 → 0.17

Numbers say: light vs heavy: width 69.2 → 67.4 px, dark 0.82 → 0.81; pressure barely changes the width; the long stroke does not run out of paint.

## Lift wet paint
Eraser · 30 px · 26.6 s · over bands of wet oil paint and oil pastel in turn (it works on paint already there: look at what it does to the bands; covered counts the bands too)

![Lift wet paint](Lift-wet-paint.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 24 % → 24 % | 70.1 px | 0.82 | 1.00 | 51 |
| heavy line | 24 % → 24 % | 69.8 px | 0.82 | 1.00 | 53 |
| pressure swell | 24 % → 24 % | 89.5 px | 0.82 | 1.00 | 41 |
| fast wave | 24 % → 24 % | 27.7 px | 0.82 | 1.00 | 123 |
| slow wave | 24 % → 24 % | 27.7 px | 0.82 | 1.00 | 204 |
| spiral | 24 % → 24 % | 15.9 px | 0.82 | 1.00 | 207 |
| loop | 24 % → 24 % | 31.1 px | 0.82 | 1.00 | 126 |
| tilted | 24 % → 24 % | 66.8 px | 0.82 | 1.00 | 80 |
| over the wet one | 24 % → 24 % | 0.0 px | 0.82 | 1.00 | 44 |
| long, no reload | 24 % → 24 % | 10.7 px | 0.82 | 1.00 | 357 | quarters: 0.18 → 0.24 → 0.17 → 0.24

Numbers say: light vs heavy: width 70.1 → 69.8 px, dark 0.82 → 0.82; pressure barely changes the width; the long stroke does not run out of paint.

## Sgraffito
Eraser · 10 px · 26.2 s · over bands of wet oil paint and oil pastel in turn (it works on paint already there: look at what it does to the bands; covered counts the bands too)

![Sgraffito](Sgraffito.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 24 % → 24 % | 69.5 px | 0.81 | 1.00 | 16 |
| heavy line | 24 % → 24 % | 69.5 px | 0.82 | 1.00 | 11 |
| pressure swell | 24 % → 24 % | 89.5 px | 0.82 | 1.00 | 6 |
| fast wave | 24 % → 24 % | 27.4 px | 0.82 | 1.00 | 27 |
| slow wave | 24 % → 24 % | 27.4 px | 0.81 | 1.00 | 30 |
| spiral | 24 % → 24 % | 15.7 px | 0.81 | 1.00 | 52 |
| loop | 24 % → 24 % | 30.9 px | 0.82 | 1.00 | 41 |
| tilted | 24 % → 24 % | 66.6 px | 0.82 | 1.00 | 8 |
| over the wet one | 24 % → 24 % | 0.0 px | 0.82 | 1.00 | 11 |
| long, no reload | 24 % → 24 % | 10.6 px | 0.82 | 1.00 | 68 | quarters: 0.17 → 0.24 → 0.17 → 0.24

Numbers say: light vs heavy: width 69.5 → 69.5 px, dark 0.81 → 0.82; pressure barely changes the width; the long stroke does not run out of paint.

## Brush Artist · Refs · #01 Henry Ward peach cloud
Gouache · 44 px · 49.3 s

![Brush Artist · Refs · #01 Henry Ward peach cloud](Brush-Artist-Refs-01-Henry-Ward-peach-cloud.png)

A light paint: laid on a grey sheet (on white it cannot be seen); **dark** = how far it is from the grey either way.

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 15 % → 12 % | 42.2 px | 0.32 | 0.80 | 291 |
| heavy line | 16 % → 13 % | 45.5 px | 0.32 | 0.83 | 210 |
| pressure swell | 12 % → 10 % | 44.0 px | 0.32 | 0.87 | 142 |
| fast wave | 37 % → 18 % | 43.0 px | 0.32 | 0.48 | 505 |
| slow wave | 37 % → 18 % | 43.1 px | 0.32 | 0.48 | 882 |
| spiral | 59 % → 19 % | 39.1 px | 0.32 | 0.32 | 954 |
| loop | 32 % → 19 % | 41.2 px | 0.32 | 0.60 | 461 |
| tilted | 13 % → 13 % | 36.6 px | 0.32 | 0.99 | 299 |
| over the wet one | 27 % → 23 % | 38.9 px | 0.32 | 0.85 | 218 |
| long, no reload | 69 % → 20 % | 30.8 px | 0.32 | 0.29 | 1264 | quarters: 0.01 → 0.01 → 0.01 → 0.02

Numbers say: light vs heavy: width 42.2 → 45.5 px, dark 0.32 → 0.32; pressure barely changes the width; the long stroke does not run out of paint.

## Brush Artist · Refs · #02 Henry Ward cream strokes
Gouache · 46 px · 45.5 s

![Brush Artist · Refs · #02 Henry Ward cream strokes](Brush-Artist-Refs-02-Henry-Ward-cream-strokes.png)

A light paint: laid on a grey sheet (on white it cannot be seen); **dark** = how far it is from the grey either way.

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 14 % → 13 % | 40.8 px | 0.41 | 0.90 | 234 |
| heavy line | 15 % → 14 % | 43.9 px | 0.41 | 0.92 | 201 |
| pressure swell | 11 % → 11 % | 42.8 px | 0.41 | 0.94 | 137 |
| fast wave | 35 % → 18 % | 40.9 px | 0.40 | 0.50 | 514 |
| slow wave | 36 % → 18 % | 41.1 px | 0.40 | 0.49 | 900 |
| spiral | 58 % → 19 % | 38.0 px | 0.40 | 0.33 | 896 |
| loop | 31 % → 20 % | 39.7 px | 0.40 | 0.64 | 494 |
| tilted | 13 % → 13 % | 36.8 px | 0.41 | 0.99 | 246 |
| over the wet one | 27 % → 23 % | 37.8 px | 0.41 | 0.86 | 193 |
| long, no reload | 67 % → 21 % | 30.1 px | 0.40 | 0.31 | 1223 | quarters: 0.01 → 0.01 → 0.01 → 0.02

Numbers say: light vs heavy: width 40.8 → 43.9 px, dark 0.41 → 0.41; pressure barely changes the width; the long stroke does not run out of paint.

## Brush Artist · Refs · #03 Henry Ward navy contours
Heavy acrylic · 22 px · 20.8 s

![Brush Artist · Refs · #03 Henry Ward navy contours](Brush-Artist-Refs-03-Henry-Ward-navy-contours.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 7 % → 7 % | 21.6 px | 0.70 | 0.94 | 109 |
| heavy line | 8 % → 8 % | 23.5 px | 0.70 | 0.95 | 122 |
| pressure swell | 6 % → 6 % | 23.2 px | 0.73 | 0.94 | 81 |
| fast wave | 19 % → 12 % | 21.8 px | 0.72 | 0.66 | 290 |
| slow wave | 19 % → 13 % | 22.5 px | 0.72 | 0.69 | 393 |
| spiral | 30 % → 13 % | 19.5 px | 0.72 | 0.45 | 475 |
| loop | 17 % → 13 % | 21.5 px | 0.72 | 0.81 | 212 |
| tilted | 8 % → 8 % | 22.6 px | 0.71 | 1.00 | 135 |
| over the wet one | 16 % → 14 % | 21.4 px | 0.71 | 0.89 | 108 |
| long, no reload | 34 % → 13 % | 15.1 px | 0.72 | 0.40 | 594 | quarters: 0.35 → 0.29 → 0.20 → 0.08

Numbers say: light vs heavy: width 21.6 → 23.5 px, dark 0.70 → 0.70; pressure barely changes the width.

## Brush Artist · Refs · #04 Henry Ward grey cloud
Gouache · 50 px · 46.4 s

![Brush Artist · Refs · #04 Henry Ward grey cloud](Brush-Artist-Refs-04-Henry-Ward-grey-cloud.png)

A light paint: laid on a grey sheet (on white it cannot be seen); **dark** = how far it is from the grey either way.

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 16 % → 14 % | 46.7 px | 0.31 | 0.85 | 290 |
| heavy line | 17 % → 15 % | 50.2 px | 0.31 | 0.89 | 227 |
| pressure swell | 13 % → 12 % | 48.7 px | 0.31 | 0.91 | 163 |
| fast wave | 40 % → 20 % | 46.4 px | 0.31 | 0.51 | 777 |
| slow wave | 40 % → 20 % | 46.5 px | 0.31 | 0.49 | 1078 |
| spiral | 61 % → 21 % | 40.0 px | 0.31 | 0.34 | 929 |
| loop | 35 % → 22 % | 45.2 px | 0.31 | 0.64 | 537 |
| tilted | 14 % → 14 % | 39.9 px | 0.31 | 1.00 | 287 |
| over the wet one | 30 % → 26 % | 42.8 px | 0.31 | 0.87 | 246 |
| long, no reload | 73 % → 23 % | 32.7 px | 0.31 | 0.31 | 1689 | quarters: 0.01 → 0.01 → 0.01 → 0.02

Numbers say: light vs heavy: width 46.7 → 50.2 px, dark 0.31 → 0.31; pressure barely changes the width; the long stroke does not run out of paint.

## Brush Artist · Refs · #05 Henry Ward green in rust loops
Heavy acrylic · 20 px · 18.6 s

![Brush Artist · Refs · #05 Henry Ward green in rust loops](Brush-Artist-Refs-05-Henry-Ward-green-in-rust-loops.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 7 % → 6 % | 19.5 px | 0.55 | 0.94 | 91 |
| heavy line | 7 % → 7 % | 21.4 px | 0.55 | 0.94 | 95 |
| pressure swell | 6 % → 5 % | 21.5 px | 0.57 | 0.92 | 115 |
| fast wave | 17 % → 11 % | 19.8 px | 0.56 | 0.64 | 302 |
| slow wave | 18 % → 12 % | 20.4 px | 0.56 | 0.66 | 367 |
| spiral | 27 % → 11 % | 17.9 px | 0.55 | 0.42 | 458 |
| loop | 15 % → 12 % | 19.5 px | 0.55 | 0.80 | 240 |
| tilted | 8 % → 8 % | 21.7 px | 0.56 | 1.00 | 126 |
| over the wet one | 15 % → 13 % | 19.3 px | 0.56 | 0.87 | 104 |
| long, no reload | 30 % → 12 % | 13.4 px | 0.56 | 0.39 | 640 | quarters: 0.25 → 0.18 → 0.10 → 0.02

Numbers say: light vs heavy: width 19.5 → 21.4 px, dark 0.55 → 0.55; pressure barely changes the width.

## Brush Artist · Refs · #06 Henry Ward scrubbed grey
Gouache · 50 px · 51.0 s

![Brush Artist · Refs · #06 Henry Ward scrubbed grey](Brush-Artist-Refs-06-Henry-Ward-scrubbed-grey.png)

A light paint: laid on a grey sheet (on white it cannot be seen); **dark** = how far it is from the grey either way.

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 16 % → 14 % | 46.7 px | 0.33 | 0.85 | 215 |
| heavy line | 17 % → 15 % | 50.2 px | 0.33 | 0.89 | 221 |
| pressure swell | 13 % → 12 % | 48.7 px | 0.33 | 0.91 | 190 |
| fast wave | 40 % → 20 % | 46.4 px | 0.33 | 0.51 | 588 |
| slow wave | 40 % → 20 % | 46.5 px | 0.33 | 0.49 | 1033 |
| spiral | 61 % → 21 % | 40.0 px | 0.33 | 0.34 | 1201 |
| loop | 35 % → 22 % | 45.2 px | 0.32 | 0.64 | 717 |
| tilted | 14 % → 14 % | 39.9 px | 0.33 | 1.00 | 296 |
| over the wet one | 30 % → 26 % | 42.8 px | 0.33 | 0.87 | 223 |
| long, no reload | 73 % → 23 % | 32.7 px | 0.32 | 0.31 | 1465 | quarters: 0.01 → 0.01 → 0.01 → 0.02

Numbers say: light vs heavy: width 46.7 → 50.2 px, dark 0.33 → 0.33; pressure barely changes the width; the long stroke does not run out of paint.

## Brush Artist · Refs · #07 Henry Ward blue L + black zigzag
Heavy acrylic · 34 px · 23.1 s

![Brush Artist · Refs · #07 Henry Ward blue L + black zigzag](Brush-Artist-Refs-07-Henry-Ward-blue-L-black-zigzag.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 11 % → 11 % | 33.2 px | 0.57 | 0.93 | 155 |
| heavy line | 12 % → 12 % | 35.8 px | 0.57 | 0.93 | 122 |
| pressure swell | 9 % → 9 % | 35.2 px | 0.59 | 0.94 | 98 |
| fast wave | 29 % → 20 % | 33.6 px | 0.59 | 0.69 | 326 |
| slow wave | 30 % → 21 % | 34.2 px | 0.58 | 0.72 | 719 |
| spiral | 47 % → 22 % | 31.3 px | 0.58 | 0.46 | 677 |
| loop | 25 % → 21 % | 32.7 px | 0.58 | 0.82 | 330 |
| tilted | 11 % → 11 % | 29.9 px | 0.58 | 1.00 | 175 |
| over the wet one | 22 % → 20 % | 31.8 px | 0.58 | 0.91 | 135 |
| long, no reload | 53 % → 22 % | 23.8 px | 0.59 | 0.42 | 1169 | quarters: 0.40 → 0.32 → 0.21 → 0.10

Numbers say: light vs heavy: width 33.2 → 35.8 px, dark 0.57 → 0.57; pressure barely changes the width.

## Brush Artist · Refs · #08 Henry Ward olive bands
Gouache · 34 px · 35.9 s

![Brush Artist · Refs · #08 Henry Ward olive bands](Brush-Artist-Refs-08-Henry-Ward-olive-bands.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 8 % → 2 % | 24.7 px | 0.57 | 0.27 | 97 |
| heavy line | 12 % → 3 % | 33.9 px | 0.57 | 0.22 | 231 |
| pressure swell | 8 % → 3 % | 30.8 px | 0.57 | 0.38 | 129 |
| fast wave | 25 % → 4 % | 29.2 px | 0.57 | 0.15 | 445 |
| slow wave | 25 % → 4 % | 28.9 px | 0.57 | 0.15 | 901 |
| spiral | 39 % → 4 % | 25.7 px | 0.57 | 0.10 | 729 |
| loop | 22 % → 5 % | 28.8 px | 0.57 | 0.21 | 288 |
| tilted | 10 % → 10 % | 28.6 px | 0.57 | 0.98 | 157 |
| over the wet one | 20 % → 8 % | 28.3 px | 0.57 | 0.40 | 143 |
| long, no reload | 45 % → 6 % | 20.0 px | 0.57 | 0.13 | 845 | quarters: 0.35 → 0.27 → 0.17 → 0.08

Numbers say: light vs heavy: width 24.7 → 33.9 px, dark 0.57 → 0.57.

## Brush Artist · Refs · #09 Henry Ward white loops
Gouache · 46 px · 48.7 s

![Brush Artist · Refs · #09 Henry Ward white loops](Brush-Artist-Refs-09-Henry-Ward-white-loops.png)

A light paint: laid on a grey sheet (on white it cannot be seen); **dark** = how far it is from the grey either way.

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 14 % → 13 % | 40.8 px | 0.43 | 0.90 | 236 |
| heavy line | 15 % → 14 % | 43.9 px | 0.43 | 0.92 | 207 |
| pressure swell | 11 % → 11 % | 42.8 px | 0.44 | 0.94 | 145 |
| fast wave | 35 % → 18 % | 40.9 px | 0.43 | 0.50 | 628 |
| slow wave | 36 % → 18 % | 41.1 px | 0.43 | 0.49 | 2374 |
| spiral | 58 % → 19 % | 38.0 px | 0.42 | 0.33 | 940 |
| loop | 31 % → 20 % | 39.7 px | 0.42 | 0.64 | 447 |
| tilted | 13 % → 13 % | 36.8 px | 0.43 | 0.99 | 253 |
| over the wet one | 27 % → 23 % | 37.8 px | 0.43 | 0.86 | 223 |
| long, no reload | 67 % → 21 % | 30.1 px | 0.42 | 0.31 | 1422 | quarters: 0.01 → 0.01 → 0.01 → 0.02

Numbers say: light vs heavy: width 40.8 → 43.9 px, dark 0.43 → 0.43; pressure barely changes the width; the long stroke does not run out of paint.

## Brush Artist · Refs · #10 Henry Ward maroon loops
Heavy acrylic · 30 px · 22.5 s

![Brush Artist · Refs · #10 Henry Ward maroon loops](Brush-Artist-Refs-10-Henry-Ward-maroon-loops.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 10 % → 9 % | 28.0 px | 0.71 | 0.94 | 120 |
| heavy line | 10 % → 10 % | 30.3 px | 0.71 | 0.95 | 146 |
| pressure swell | 8 % → 8 % | 30.0 px | 0.73 | 0.94 | 128 |
| fast wave | 25 % → 17 % | 28.3 px | 0.73 | 0.71 | 325 |
| slow wave | 25 % → 18 % | 29.0 px | 0.73 | 0.73 | 557 |
| spiral | 39 % → 18 % | 26.0 px | 0.72 | 0.47 | 558 |
| loop | 21 % → 18 % | 27.6 px | 0.72 | 0.85 | 280 |
| tilted | 10 % → 10 % | 27.9 px | 0.72 | 1.00 | 152 |
| over the wet one | 20 % → 18 % | 27.0 px | 0.72 | 0.91 | 150 |
| long, no reload | 46 % → 18 % | 20.6 px | 0.73 | 0.40 | 878 | quarters: 0.44 → 0.38 → 0.31 → 0.22

Numbers say: light vs heavy: width 28.0 → 30.3 px, dark 0.71 → 0.71; pressure barely changes the width.

## Brush Artist · Refs · #11 Henry Ward purple spun balls
Heavy acrylic · 36 px · 24.2 s

![Brush Artist · Refs · #11 Henry Ward purple spun balls](Brush-Artist-Refs-11-Henry-Ward-purple-spun-balls.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 12 % → 11 % | 34.2 px | 0.71 | 0.96 | 152 |
| heavy line | 13 % → 12 % | 36.7 px | 0.71 | 0.95 | 184 |
| pressure swell | 10 % → 9 % | 36.2 px | 0.74 | 0.95 | 100 |
| fast wave | 30 % → 23 % | 34.6 px | 0.73 | 0.75 | 377 |
| slow wave | 30 % → 24 % | 35.0 px | 0.73 | 0.79 | 678 |
| spiral | 49 % → 25 % | 32.3 px | 0.73 | 0.50 | 696 |
| loop | 26 % → 23 % | 33.4 px | 0.73 | 0.88 | 307 |
| tilted | 11 % → 11 % | 31.2 px | 0.72 | 1.00 | 254 |
| over the wet one | 23 % → 21 % | 32.3 px | 0.72 | 0.93 | 245 |
| long, no reload | 55 % → 24 % | 24.8 px | 0.73 | 0.44 | 1044 | quarters: 0.51 → 0.46 → 0.39 → 0.28

Numbers say: light vs heavy: width 34.2 → 36.7 px, dark 0.71 → 0.71; pressure barely changes the width.

## Brush Artist · Refs · #12 Henry Ward black-olive cage
Gouache · 28 px · 31.7 s

![Brush Artist · Refs · #12 Henry Ward black-olive cage](Brush-Artist-Refs-12-Henry-Ward-black-olive-cage.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 7 % → 3 % | 20.9 px | 0.61 | 0.35 | 97 |
| heavy line | 9 % → 4 % | 26.1 px | 0.61 | 0.41 | 162 |
| pressure swell | 6 % → 4 % | 23.9 px | 0.61 | 0.61 | 93 |
| fast wave | 20 % → 4 % | 23.7 px | 0.61 | 0.19 | 312 |
| slow wave | 20 % → 4 % | 23.3 px | 0.61 | 0.21 | 528 |
| spiral | 32 % → 4 % | 21.4 px | 0.61 | 0.14 | 640 |
| loop | 18 % → 5 % | 22.8 px | 0.61 | 0.28 | 326 |
| tilted | 9 % → 9 % | 25.4 px | 0.61 | 0.98 | 138 |
| over the wet one | 17 % → 8 % | 21.8 px | 0.61 | 0.46 | 133 |
| long, no reload | 39 % → 6 % | 17.6 px | 0.61 | 0.15 | 1168 | quarters: 0.31 → 0.26 → 0.19 → 0.10

Numbers say: light vs heavy: width 20.9 → 26.1 px, dark 0.61 → 0.61.

## Brush Artist · Refs · #13 Henry Ward blue streaky form
Gouache · 50 px · 49.6 s

![Brush Artist · Refs · #13 Henry Ward blue streaky form](Brush-Artist-Refs-13-Henry-Ward-blue-streaky-form.png)

A light paint: laid on a grey sheet (on white it cannot be seen); **dark** = how far it is from the grey either way.

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 16 % → 14 % | 46.7 px | 0.33 | 0.85 | 217 |
| heavy line | 17 % → 15 % | 50.2 px | 0.33 | 0.89 | 243 |
| pressure swell | 13 % → 12 % | 48.7 px | 0.33 | 0.91 | 179 |
| fast wave | 40 % → 20 % | 46.4 px | 0.33 | 0.51 | 561 |
| slow wave | 40 % → 20 % | 46.5 px | 0.33 | 0.49 | 1051 |
| spiral | 61 % → 21 % | 40.0 px | 0.32 | 0.34 | 1277 |
| loop | 35 % → 22 % | 45.2 px | 0.32 | 0.64 | 489 |
| tilted | 14 % → 14 % | 39.9 px | 0.33 | 1.00 | 301 |
| over the wet one | 30 % → 26 % | 42.8 px | 0.33 | 0.87 | 263 |
| long, no reload | 73 % → 23 % | 32.7 px | 0.32 | 0.31 | 1481 | quarters: 0.01 → 0.01 → 0.01 → 0.02

Numbers say: light vs heavy: width 46.7 → 50.2 px, dark 0.33 → 0.33; pressure barely changes the width; the long stroke does not run out of paint.

## Brush Artist · Refs · #14 Henry Ward olive totem
Heavy acrylic · 48 px · 27.5 s

![Brush Artist · Refs · #14 Henry Ward olive totem](Brush-Artist-Refs-14-Henry-Ward-olive-totem.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 15 % → 15 % | 44.8 px | 0.31 | 0.94 | 200 |
| heavy line | 16 % → 16 % | 47.7 px | 0.31 | 0.95 | 225 |
| pressure swell | 13 % → 12 % | 47.0 px | 0.32 | 0.95 | 162 |
| fast wave | 38 % → 30 % | 43.9 px | 0.30 | 0.79 | 586 |
| slow wave | 39 % → 31 % | 44.6 px | 0.30 | 0.81 | 945 |
| spiral | 58 % → 32 % | 38.2 px | 0.30 | 0.55 | 931 |
| loop | 33 % → 29 % | 42.7 px | 0.30 | 0.89 | 653 |
| tilted | 13 % → 13 % | 37.5 px | 0.31 | 1.00 | 339 |
| over the wet one | 28 % → 26 % | 41.2 px | 0.31 | 0.93 | 214 |
| long, no reload | 68 % → 33 % | 30.3 px | 0.30 | 0.49 | 1305 | quarters: 0.25 → 0.18 → 0.10 → 0.03

Numbers say: light vs heavy: width 44.8 → 47.7 px, dark 0.31 → 0.31; pressure barely changes the width.

## Brush Artist · Refs · #15 Ultramarine brush script
Ink · 4 px · 31.4 s

![Brush Artist · Refs · #15 Ultramarine brush script](Brush-Artist-Refs-15-Ultramarine-brush-script.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 1 % → 3 % | 2.2 px | 0.55 | 3.86 | 46 |
| heavy line | 6 % → 6 % | 16.6 px | 0.58 | 0.99 | 72 |
| pressure swell | 3 % → 4 % | 12.0 px | 0.64 | 1.15 | 48 |
| fast wave | 9 % → 7 % | 10.5 px | 0.55 | 0.82 | 208 |
| slow wave | 7 % → 7 % | 8.4 px | 0.54 | 0.93 | 137 |
| spiral | 11 % → 7 % | 7.2 px | 0.52 | 0.68 | 222 |
| loop | 7 % → 7 % | 9.2 px | 0.53 | 0.99 | 128 |
| tilted | 3 % → 3 % | 8.0 px | 0.62 | 1.02 | 47 |
| over the wet one | 7 % → 7 % | 11.4 px | 0.62 | 1.05 | 55 |
| long, no reload | 16 % → 8 % | 7.3 px | 0.50 | 0.49 | 348 | quarters: 0.14 → 0.04 → 0.01 → 0.00

Numbers say: light vs heavy: width 2.2 → 16.6 px, dark 0.55 → 0.58; wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #18 Blue oil-stick scribbles
Pastel · 10 px · 15.3 s

![Brush Artist · Refs · #18 Blue oil-stick scribbles](Brush-Artist-Refs-18-Blue-oil-stick-scribbles.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 1 % → 1 % | 2.9 px | 0.52 | 1.00 | 75 |
| heavy line | 2 % → 2 % | 5.5 px | 0.53 | 1.00 | 57 |
| pressure swell | 1 % → 1 % | 5.0 px | 0.53 | 1.00 | 42 |
| fast wave | 4 % → 4 % | 4.8 px | 0.53 | 1.00 | 145 |
| slow wave | 4 % → 4 % | 4.4 px | 0.53 | 1.00 | 348 |
| spiral | 7 % → 7 % | 4.5 px | 0.52 | 1.00 | 203 |
| loop | 3 % → 3 % | 4.5 px | 0.52 | 1.00 | 127 |
| tilted | 2 % → 2 % | 4.7 px | 0.53 | 1.00 | 53 |
| over the wet one | 3 % → 3 % | 4.7 px | 0.53 | 1.00 | 33 |
| long, no reload | 10 % → 10 % | 4.4 px | 0.53 | 1.00 | 221 | quarters: 0.06 → 0.06 → 0.06 → 0.06

Numbers say: light vs heavy: width 2.9 → 5.5 px, dark 0.52 → 0.53; the long stroke does not run out of paint.

## Brush Artist · Refs · #20 Orange-red crayon scribble
Pastel · 14 px · 14.6 s

![Brush Artist · Refs · #20 Orange-red crayon scribble](Brush-Artist-Refs-20-Orange-red-crayon-scribble.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 1 % → 1 % | 4.0 px | 0.53 | 1.00 | 44 |
| heavy line | 3 % → 3 % | 8.0 px | 0.53 | 1.00 | 40 |
| pressure swell | 2 % → 2 % | 7.6 px | 0.53 | 1.00 | 22 |
| fast wave | 6 % → 6 % | 7.2 px | 0.53 | 1.00 | 90 |
| slow wave | 6 % → 6 % | 6.6 px | 0.53 | 1.00 | 99 |
| spiral | 9 % → 9 % | 6.2 px | 0.53 | 1.00 | 183 |
| loop | 5 % → 5 % | 6.2 px | 0.53 | 1.00 | 136 |
| tilted | 2 % → 2 % | 5.6 px | 0.53 | 1.00 | 39 |
| over the wet one | 4 % → 4 % | 6.6 px | 0.53 | 1.00 | 48 |
| long, no reload | 13 % → 13 % | 5.7 px | 0.53 | 1.00 | 215 | quarters: 0.07 → 0.07 → 0.08 → 0.08

Numbers say: light vs heavy: width 4.0 → 8.0 px, dark 0.53 → 0.53; the long stroke does not run out of paint.

## Brush Artist · Refs · #21 Gritty black contours
Gouache · 12 px · 28.4 s

![Brush Artist · Refs · #21 Gritty black contours](Brush-Artist-Refs-21-Gritty-black-contours.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 3 % → 0 % | 8.8 px | 0.79 | 0.12 | 94 |
| heavy line | 4 % → 0 % | 11.9 px | 0.79 | 0.10 | 142 |
| pressure swell | 3 % → 0 % | 11.6 px | 0.79 | 0.15 | 115 |
| fast wave | 7 % → 1 % | 8.5 px | 0.79 | 0.10 | 344 |
| slow wave | 8 % → 1 % | 9.0 px | 0.79 | 0.09 | 304 |
| spiral | 9 % → 1 % | 6.0 px | 0.79 | 0.10 | 562 |
| loop | 8 % → 1 % | 9.9 px | 0.79 | 0.09 | 263 |
| tilted | 4 % → 4 % | 10.8 px | 0.79 | 0.90 | 200 |
| over the wet one | 7 % → 1 % | 9.7 px | 0.79 | 0.17 | 192 |
| long, no reload | 7 % → 1 % | 3.3 px | 0.79 | 0.12 | 874 | quarters: 0.20 → 0.07 → 0.00 → 0.00

Numbers say: light vs heavy: width 8.8 → 11.9 px, dark 0.79 → 0.79.

## Brush Artist · Refs · #22 Bold black brush poster
Ink · 20 px · 37.2 s

![Brush Artist · Refs · #22 Bold black brush poster](Brush-Artist-Refs-22-Bold-black-brush-poster.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 3 % → 5 % | 9.5 px | 0.79 | 1.63 | 56 |
| heavy line | 15 % → 15 % | 44.6 px | 0.88 | 0.99 | 120 |
| pressure swell | 9 % → 9 % | 31.9 px | 0.87 | 1.04 | 92 |
| fast wave | 27 % → 26 % | 31.2 px | 0.87 | 0.98 | 222 |
| slow wave | 22 % → 21 % | 25.2 px | 0.87 | 0.98 | 314 |
| spiral | 34 % → 32 % | 22.2 px | 0.87 | 0.94 | 399 |
| loop | 20 % → 20 % | 26.2 px | 0.88 | 1.00 | 229 |
| tilted | 8 % → 8 % | 22.7 px | 0.88 | 1.01 | 88 |
| over the wet one | 19 % → 19 % | 30.5 px | 0.88 | 1.00 | 119 |
| long, no reload | 45 % → 38 % | 20.2 px | 0.86 | 0.84 | 656 | quarters: 0.54 → 0.45 → 0.35 → 0.27

Numbers say: light vs heavy: width 9.5 → 44.6 px, dark 0.79 → 0.88; wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #23 Dry white on orange + black line
Gouache · 50 px · 34.4 s

![Brush Artist · Refs · #23 Dry white on orange + black line](Brush-Artist-Refs-23-Dry-white-on-orange-black-line.png)

A light paint: laid on a grey sheet (on white it cannot be seen); **dark** = how far it is from the grey either way.

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 12 % → 2 % | 35.1 px | 0.39 | 0.13 | 253 |
| heavy line | 16 % → 2 % | 46.9 px | 0.39 | 0.11 | 430 |
| pressure swell | 11 % → 2 % | 42.6 px | 0.39 | 0.19 | 148 |
| fast wave | 34 % → 3 % | 39.7 px | 0.39 | 0.09 | 535 |
| slow wave | 34 % → 3 % | 39.0 px | 0.39 | 0.10 | 997 |
| spiral | 49 % → 4 % | 32.6 px | 0.38 | 0.07 | 953 |
| loop | 30 % → 4 % | 39.1 px | 0.38 | 0.12 | 502 |
| tilted | 13 % → 12 % | 34.9 px | 0.38 | 0.98 | 275 |
| over the wet one | 26 % → 7 % | 38.0 px | 0.38 | 0.27 | 356 |
| long, no reload | 58 % → 5 % | 26.1 px | 0.38 | 0.09 | 1356 | quarters: 0.02 → 0.02 → 0.03 → 0.04

Numbers say: light vs heavy: width 35.1 → 46.9 px, dark 0.39 → 0.39; the long stroke does not run out of paint.

## Brush Artist · Refs · #24 Picasso flat oil
Oil · 34 px · 22.2 s

![Brush Artist · Refs · #24 Picasso flat oil](Brush-Artist-Refs-24-Picasso-flat-oil.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 11 % → 11 % | 32.4 px | 0.40 | 1.00 | 153 |
| heavy line | 12 % → 12 % | 35.2 px | 0.40 | 1.00 | 164 |
| pressure swell | 9 % → 9 % | 34.4 px | 0.41 | 1.00 | 122 |
| fast wave | 30 % → 30 % | 34.2 px | 0.41 | 1.00 | 414 |
| slow wave | 30 % → 30 % | 35.0 px | 0.41 | 1.00 | 697 |
| spiral | 51 % → 51 % | 33.8 px | 0.40 | 1.00 | 746 |
| loop | 25 % → 25 % | 32.6 px | 0.41 | 1.00 | 353 |
| tilted | 11 % → 11 % | 32.0 px | 0.41 | 1.00 | 276 |
| over the wet one | 23 % → 23 % | 30.8 px | 0.41 | 1.00 | 259 |
| long, no reload | 62 % → 62 % | 27.6 px | 0.39 | 1.00 | 1275 | quarters: 0.28 → 0.28 → 0.26 → 0.24

Numbers say: light vs heavy: width 32.4 → 35.2 px, dark 0.40 → 0.40; pressure barely changes the width.

## Brush Artist · Refs · #25 Yellow heavy flat stroke
Heavy acrylic · 110 px · 51.3 s

![Brush Artist · Refs · #25 Yellow heavy flat stroke](Brush-Artist-Refs-25-Yellow-heavy-flat-stroke.png)

A light paint: laid on a grey sheet (on white it cannot be seen); **dark** = how far it is from the grey either way.

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 35 % → 36 % | 101.5 px | 0.30 | 1.02 | 533 |
| heavy line | 36 % → 35 % | 105.1 px | 0.31 | 0.97 | 549 |
| pressure swell | 28 % → 29 % | 105.4 px | 0.30 | 1.04 | 432 |
| fast wave | 73 % → 76 % | 83.8 px | 0.31 | 1.05 | 1553 |
| slow wave | 73 % → 72 % | 84.7 px | 0.30 | 0.98 | 2691 |
| spiral | 86 % → 83 % | 56.7 px | 0.29 | 0.97 | 3183 |
| loop | 65 % → 64 % | 83.6 px | 0.31 | 0.99 | 1725 |
| tilted | 26 % → 26 % | 71.5 px | 0.30 | 1.00 | 637 |
| over the wet one | 55 % → 54 % | 83.2 px | 0.30 | 0.97 | 507 |
| long, no reload | 98 % → 97 % | 44.1 px | 0.29 | 0.99 | 4229 | quarters: 0.00 → 0.00 → 0.00 → 0.00

Numbers say: light vs heavy: width 101.5 → 105.1 px, dark 0.30 → 0.31; pressure barely changes the width; the long stroke does not run out of paint.

## Brush Artist · Refs · #27 Orange impasto swatch
Heavy acrylic · 60 px · 32.3 s

![Brush Artist · Refs · #27 Orange impasto swatch](Brush-Artist-Refs-27-Orange-impasto-swatch.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 20 % → 19 % | 56.8 px | 0.34 | 0.97 | 306 |
| heavy line | 20 % → 20 % | 59.5 px | 0.34 | 0.97 | 307 |
| pressure swell | 16 % → 15 % | 59.6 px | 0.36 | 0.97 | 229 |
| fast wave | 48 % → 46 % | 55.0 px | 0.35 | 0.98 | 853 |
| slow wave | 48 % → 47 % | 55.9 px | 0.35 | 0.98 | 1392 |
| spiral | 69 % → 62 % | 45.5 px | 0.34 | 0.91 | 1763 |
| loop | 42 % → 40 % | 53.9 px | 0.35 | 0.97 | 549 |
| tilted | 16 % → 16 % | 44.0 px | 0.35 | 1.00 | 271 |
| over the wet one | 34 % → 33 % | 50.9 px | 0.35 | 0.96 | 253 |
| long, no reload | 85 % → 75 % | 38.1 px | 0.35 | 0.88 | 1555 | quarters: 0.33 → 0.31 → 0.29 → 0.26

Numbers say: light vs heavy: width 56.8 → 59.5 px, dark 0.34 → 0.34; pressure barely changes the width.

## Brush Artist · Refs · #28 Miles Davis black lines
Ink · 22 px · 39.5 s

![Brush Artist · Refs · #28 Miles Davis black lines](Brush-Artist-Refs-28-Miles-Davis-black-lines.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 4 % → 6 % | 12.2 px | 0.81 | 1.48 | 90 |
| heavy line | 17 % → 17 % | 49.1 px | 0.88 | 0.99 | 204 |
| pressure swell | 10 % → 10 % | 35.9 px | 0.87 | 1.03 | 76 |
| fast wave | 30 % → 30 % | 35.0 px | 0.87 | 0.98 | 206 |
| slow wave | 25 % → 25 % | 28.5 px | 0.87 | 0.99 | 317 |
| spiral | 38 % → 37 % | 25.3 px | 0.87 | 0.96 | 335 |
| loop | 23 % → 23 % | 29.4 px | 0.88 | 1.00 | 222 |
| tilted | 9 % → 9 % | 25.0 px | 0.88 | 1.01 | 122 |
| over the wet one | 21 % → 21 % | 34.1 px | 0.88 | 1.00 | 131 |
| long, no reload | 51 % → 43 % | 22.7 px | 0.86 | 0.85 | 511 | quarters: 0.59 → 0.51 → 0.40 → 0.31

Numbers say: light vs heavy: width 12.2 → 49.1 px, dark 0.81 → 0.88.

## Brush Artist · Refs · #29 Shrigley magenta asterisk
Watercolor · 70 px · 47.3 s

![Brush Artist · Refs · #29 Shrigley magenta asterisk](Brush-Artist-Refs-29-Shrigley-magenta-asterisk.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 10 % → 13 % | 28.0 px | 0.65 | 1.36 | 90 |
| heavy line | 17 % → 18 % | 50.3 px | 0.64 | 1.03 | 180 |
| pressure swell | 11 % → 12 % | 41.1 px | 0.65 | 1.13 | 122 |
| fast wave | 38 % → 38 % | 43.7 px | 0.64 | 1.00 | 326 |
| slow wave | 35 % → 39 % | 41.0 px | 0.65 | 1.10 | 553 |
| spiral | 61 % → 61 % | 40.0 px | 0.64 | 1.01 | 796 |
| loop | 31 % → 32 % | 40.2 px | 0.65 | 1.03 | 377 |
| tilted | 18 % → 18 % | 49.0 px | 0.65 | 1.00 | 293 |
| over the wet one | 31 % → 34 % | 38.4 px | 0.65 | 1.07 | 143 |
| long, no reload | 75 % → 75 % | 33.5 px | 0.64 | 1.00 | 939 | quarters: 0.55 → 0.53 → 0.52 → 0.49

Numbers say: light vs heavy: width 28.0 → 50.3 px, dark 0.65 → 0.64; the long stroke does not run out of paint.

## Brush Artist · Refs · #30 Red gouache face patch
Gouache · 60 px · 53.5 s

![Brush Artist · Refs · #30 Red gouache face patch](Brush-Artist-Refs-30-Red-gouache-face-patch.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 16 % → 15 % | 46.9 px | 0.49 | 0.91 | 206 |
| heavy line | 25 % → 20 % | 73.8 px | 0.49 | 0.80 | 291 |
| pressure swell | 19 % → 17 % | 72.6 px | 0.49 | 0.86 | 198 |
| fast wave | 48 % → 28 % | 55.1 px | 0.49 | 0.58 | 687 |
| slow wave | 48 % → 28 % | 55.3 px | 0.49 | 0.59 | 1426 |
| spiral | 59 % → 28 % | 39.1 px | 0.49 | 0.48 | 999 |
| loop | 40 % → 29 % | 51.3 px | 0.49 | 0.74 | 493 |
| tilted | 16 % → 16 % | 45.7 px | 0.49 | 1.01 | 317 |
| over the wet one | 36 % → 32 % | 55.3 px | 0.49 | 0.88 | 256 |
| long, no reload | 67 % → 30 % | 30.0 px | 0.49 | 0.45 | 1839 | quarters: 0.43 → 0.38 → 0.32 → 0.26

Numbers say: light vs heavy: width 46.9 → 73.8 px, dark 0.49 → 0.49.

## Brush Artist · Refs · #31 Warhol blotted line
Ink · 6 px · 29.8 s

![Brush Artist · Refs · #31 Warhol blotted line](Brush-Artist-Refs-31-Warhol-blotted-line.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 1 % → 3 % | 2.6 px | 0.75 | 3.30 | 48 |
| heavy line | 7 % → 7 % | 20.6 px | 0.83 | 0.97 | 91 |
| pressure swell | 4 % → 4 % | 14.8 px | 0.84 | 1.12 | 40 |
| fast wave | 12 % → 9 % | 13.8 px | 0.82 | 0.77 | 148 |
| slow wave | 10 % → 8 % | 11.2 px | 0.80 | 0.85 | 137 |
| spiral | 15 % → 9 % | 9.7 px | 0.80 | 0.58 | 300 |
| loop | 9 % → 9 % | 11.9 px | 0.80 | 0.94 | 178 |
| tilted | 3 % → 3 % | 8.6 px | 0.84 | 1.04 | 60 |
| over the wet one | 8 % → 8 % | 14.5 px | 0.84 | 1.02 | 60 |
| long, no reload | 21 % → 9 % | 9.6 px | 0.78 | 0.43 | 420 | quarters: 0.25 → 0.13 → 0.05 → 0.01

Numbers say: light vs heavy: width 2.6 → 20.6 px, dark 0.75 → 0.83; wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #32 Thick orange swipes
Heavy acrylic · 90 px · 46.7 s

![Brush Artist · Refs · #32 Thick orange swipes](Brush-Artist-Refs-32-Thick-orange-swipes.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 29 % → 29 % | 83.1 px | 0.38 | 1.00 | 1301 |
| heavy line | 30 % → 29 % | 86.4 px | 0.38 | 0.97 | 745 |
| pressure swell | 23 % → 23 % | 86.5 px | 0.38 | 1.01 | 511 |
| fast wave | 63 % → 65 % | 73.1 px | 0.38 | 1.03 | 1111 |
| slow wave | 64 % → 63 % | 73.5 px | 0.38 | 0.98 | 2054 |
| spiral | 79 % → 77 % | 52.2 px | 0.38 | 0.98 | 1720 |
| loop | 57 % → 56 % | 73.4 px | 0.38 | 0.99 | 1177 |
| tilted | 21 % → 21 % | 59.3 px | 0.38 | 1.00 | 555 |
| over the wet one | 47 % → 45 % | 71.0 px | 0.38 | 0.97 | 517 |
| long, no reload | 95 % → 93 % | 42.8 px | 0.38 | 0.97 | 2819 | quarters: 0.38 → 0.38 → 0.37 → 0.35

Numbers say: light vs heavy: width 83.1 → 86.4 px, dark 0.38 → 0.38; pressure barely changes the width; the long stroke does not run out of paint.

## Brush Artist · Refs · #33 Red wet-in-wet band
Watercolor · 80 px · 62.9 s

![Brush Artist · Refs · #33 Red wet-in-wet band](Brush-Artist-Refs-33-Red-wet-in-wet-band.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 19 % → 30 % | 55.6 px | 0.59 | 1.58 | 179 |
| heavy line | 29 % → 38 % | 83.7 px | 0.59 | 1.33 | 295 |
| pressure swell | 19 % → 27 % | 71.5 px | 0.61 | 1.40 | 163 |
| fast wave | 58 % → 73 % | 67.4 px | 0.61 | 1.26 | 605 |
| slow wave | 57 % → 71 % | 65.7 px | 0.63 | 1.25 | 820 |
| spiral | 75 % → 84 % | 49.5 px | 0.64 | 1.12 | 1150 |
| loop | 51 % → 62 % | 66.4 px | 0.63 | 1.21 | 449 |
| tilted | 24 % → 25 % | 66.3 px | 0.60 | 1.03 | 365 |
| over the wet one | 48 % → 66 % | 66.6 px | 0.60 | 1.38 | 213 |
| long, no reload | 95 % → 99 % | 42.4 px | 0.66 | 1.05 | 1323 | quarters: 0.68 → 0.68 → 0.68 → 0.63

Numbers say: light vs heavy: width 55.6 → 83.7 px, dark 0.59 → 0.59; the long stroke does not run out of paint; wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #34 Magenta oil patches
Oil · 60 px · 30.2 s

![Brush Artist · Refs · #34 Magenta oil patches](Brush-Artist-Refs-34-Magenta-oil-patches.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 19 % → 19 % | 55.8 px | 0.61 | 1.00 | 281 |
| heavy line | 21 % → 21 % | 59.9 px | 0.61 | 1.00 | 311 |
| pressure swell | 16 % → 16 % | 58.9 px | 0.62 | 1.01 | 309 |
| fast wave | 48 % → 49 % | 55.4 px | 0.62 | 1.02 | 947 |
| slow wave | 48 % → 48 % | 55.8 px | 0.62 | 1.00 | 1257 |
| spiral | 70 % → 70 % | 46.3 px | 0.62 | 1.00 | 1305 |
| loop | 42 % → 42 % | 54.3 px | 0.62 | 1.00 | 638 |
| tilted | 17 % → 17 % | 46.8 px | 0.61 | 1.00 | 353 |
| over the wet one | 35 % → 35 % | 50.1 px | 0.61 | 1.00 | 288 |
| long, no reload | 86 % → 86 % | 38.7 px | 0.62 | 1.00 | 1857 | quarters: 0.59 → 0.58 → 0.57 → 0.52

Numbers say: light vs heavy: width 55.8 → 59.9 px, dark 0.61 → 0.61; pressure barely changes the width; the long stroke does not run out of paint.

## Brush Artist · Refs · #35 Red band with runs
Watercolor · 70 px · 62.1 s

![Brush Artist · Refs · #35 Red band with runs](Brush-Artist-Refs-35-Red-band-with-runs.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 17 % → 32 % | 48.3 px | 0.49 | 1.91 | 131 |
| heavy line | 25 % → 39 % | 73.9 px | 0.51 | 1.55 | 232 |
| pressure swell | 17 % → 25 % | 63.0 px | 0.55 | 1.47 | 164 |
| fast wave | 54 % → 72 % | 61.8 px | 0.52 | 1.34 | 426 |
| slow wave | 52 % → 70 % | 59.8 px | 0.55 | 1.35 | 743 |
| spiral | 72 % → 88 % | 47.3 px | 0.56 | 1.22 | 787 |
| loop | 47 % → 68 % | 61.0 px | 0.53 | 1.44 | 373 |
| tilted | 21 % → 22 % | 57.7 px | 0.51 | 1.06 | 267 |
| over the wet one | 43 % → 67 % | 62.0 px | 0.51 | 1.57 | 148 |
| long, no reload | 92 % → 98 % | 41.3 px | 0.59 | 1.07 | 1443 | quarters: 0.60 → 0.60 → 0.59 → 0.56

Numbers say: light vs heavy: width 48.3 → 73.9 px, dark 0.49 → 0.51; the long stroke does not run out of paint; wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #36 Magenta letters flat brush
Gouache · 36 px · 44.3 s

![Brush Artist · Refs · #36 Magenta letters flat brush](Brush-Artist-Refs-36-Magenta-letters-flat-brush.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 10 % → 10 % | 29.0 px | 0.45 | 0.98 | 105 |
| heavy line | 17 % → 14 % | 49.1 px | 0.45 | 0.85 | 162 |
| pressure swell | 13 % → 12 % | 49.4 px | 0.45 | 0.89 | 101 |
| fast wave | 35 % → 19 % | 40.3 px | 0.45 | 0.54 | 302 |
| slow wave | 35 % → 19 % | 39.9 px | 0.45 | 0.54 | 541 |
| spiral | 46 % → 19 % | 30.4 px | 0.45 | 0.42 | 633 |
| loop | 27 % → 20 % | 35.3 px | 0.45 | 0.72 | 334 |
| tilted | 11 % → 11 % | 29.8 px | 0.45 | 1.00 | 133 |
| over the wet one | 24 % → 22 % | 38.1 px | 0.45 | 0.92 | 120 |
| long, no reload | 46 % → 19 % | 20.8 px | 0.45 | 0.40 | 689 | quarters: 0.29 → 0.25 → 0.22 → 0.18

Numbers say: light vs heavy: width 29.0 → 49.1 px, dark 0.45 → 0.45.

## Brush Artist · Refs · #37 Oil still life dabs
Oil · 40 px · 22.3 s

![Brush Artist · Refs · #37 Oil still life dabs](Brush-Artist-Refs-37-Oil-still-life-dabs.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 13 % → 13 % | 38.0 px | 0.38 | 1.00 | 170 |
| heavy line | 14 % → 14 % | 41.1 px | 0.38 | 1.00 | 240 |
| pressure swell | 11 % → 11 % | 40.2 px | 0.40 | 1.00 | 150 |
| fast wave | 34 % → 34 % | 39.8 px | 0.39 | 1.00 | 517 |
| slow wave | 35 % → 35 % | 40.2 px | 0.39 | 1.00 | 971 |
| spiral | 59 % → 59 % | 38.7 px | 0.38 | 1.00 | 1911 |
| loop | 29 % → 29 % | 37.8 px | 0.39 | 1.00 | 399 |
| tilted | 13 % → 13 % | 36.3 px | 0.39 | 1.00 | 225 |
| over the wet one | 26 % → 26 % | 35.8 px | 0.39 | 1.00 | 191 |
| long, no reload | 69 % → 69 % | 30.9 px | 0.37 | 1.00 | 1159 | quarters: 0.31 → 0.30 → 0.28 → 0.24

Numbers say: light vs heavy: width 38.0 → 41.1 px, dark 0.38 → 0.38; pressure barely changes the width.

## Brush Artist · Refs · #38 Sanguine drawing
Pastel · 6 px · 12.7 s

![Brush Artist · Refs · #38 Sanguine drawing](Brush-Artist-Refs-38-Sanguine-drawing.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 1 % → 1 % | 2.0 px | 0.61 | 1.00 | 23 |
| heavy line | 1 % → 1 % | 3.5 px | 0.62 | 1.00 | 21 |
| pressure swell | 1 % → 1 % | 3.3 px | 0.62 | 1.00 | 21 |
| fast wave | 3 % → 3 % | 3.2 px | 0.61 | 1.00 | 55 |
| slow wave | 3 % → 3 % | 3.0 px | 0.61 | 1.00 | 61 |
| spiral | 4 % → 4 % | 2.9 px | 0.61 | 1.00 | 96 |
| loop | 2 % → 2 % | 3.0 px | 0.61 | 1.00 | 47 |
| tilted | 1 % → 1 % | 3.4 px | 0.62 | 1.00 | 28 |
| over the wet one | 2 % → 2 % | 2.9 px | 0.62 | 1.00 | 27 |
| long, no reload | 7 % → 7 % | 3.0 px | 0.61 | 1.00 | 156 | quarters: 0.04 → 0.05 → 0.05 → 0.05

Numbers say: light vs heavy: width 2.0 → 3.5 px, dark 0.61 → 0.62; the long stroke does not run out of paint.

## Brush Artist · Refs · #39 Very thick impasto
Heavy acrylic · 60 px · 30.1 s

![Brush Artist · Refs · #39 Very thick impasto](Brush-Artist-Refs-39-Very-thick-impasto.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 20 % → 19 % | 56.9 px | 0.60 | 0.97 | 362 |
| heavy line | 21 % → 20 % | 59.6 px | 0.60 | 0.97 | 246 |
| pressure swell | 16 % → 15 % | 59.7 px | 0.62 | 0.97 | 166 |
| fast wave | 48 % → 47 % | 55.2 px | 0.62 | 0.98 | 627 |
| slow wave | 49 % → 47 % | 56.0 px | 0.62 | 0.98 | 1130 |
| spiral | 69 % → 65 % | 45.6 px | 0.62 | 0.93 | 1086 |
| loop | 42 % → 41 % | 54.0 px | 0.62 | 0.97 | 536 |
| tilted | 16 % → 16 % | 44.0 px | 0.61 | 1.00 | 303 |
| over the wet one | 34 % → 33 % | 51.0 px | 0.61 | 0.97 | 246 |
| long, no reload | 85 % → 79 % | 38.3 px | 0.62 | 0.92 | 1724 | quarters: 0.58 → 0.57 → 0.55 → 0.52

Numbers say: light vs heavy: width 56.9 → 59.6 px, dark 0.60 → 0.60; pressure barely changes the width; the long stroke does not run out of paint.

## Brush Artist · Refs · #40 Watercolour blooms
Watercolor · 90 px · 70.1 s

![Brush Artist · Refs · #40 Watercolour blooms](Brush-Artist-Refs-40-Watercolour-blooms.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 22 % → 33 % | 63.3 px | 0.10 | 1.51 | 185 |
| heavy line | 33 % → 41 % | 94.9 px | 0.11 | 1.26 | 327 |
| pressure swell | 22 % → 30 % | 84.1 px | 0.12 | 1.33 | 198 |
| fast wave | 64 % → 78 % | 73.9 px | 0.11 | 1.22 | 618 |
| slow wave | 63 % → 75 % | 72.3 px | 0.16 | 1.20 | 1280 |
| spiral | 79 % → 86 % | 52.0 px | 0.15 | 1.09 | 1100 |
| loop | 56 % → 65 % | 72.5 px | 0.13 | 1.17 | 535 |
| tilted | 26 % → 27 % | 73.1 px | 0.13 | 1.03 | 413 |
| over the wet one | 53 % → 71 % | 73.8 px | 0.13 | 1.35 | 244 |
| long, no reload | 97 % → 100 % | 43.4 px | 0.16 | 1.03 | 1587 | quarters: 0.21 → 0.19 → 0.16 → 0.12

Numbers say: light vs heavy: width 63.3 → 94.9 px, dark 0.10 → 0.11; wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #41 Coloured pencil hatching
Pastel · 4 px · 12.2 s

![Brush Artist · Refs · #41 Coloured pencil hatching](Brush-Artist-Refs-41-Coloured-pencil-hatching.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 1 % → 1 % | 1.6 px | 0.42 | 1.00 | 27 |
| heavy line | 1 % → 1 % | 2.6 px | 0.43 | 1.00 | 14 |
| pressure swell | 1 % → 1 % | 2.1 px | 0.43 | 1.00 | 12 |
| fast wave | 2 % → 2 % | 2.2 px | 0.42 | 1.00 | 148 |
| slow wave | 2 % → 2 % | 2.1 px | 0.43 | 1.00 | 51 |
| spiral | 3 % → 3 % | 2.1 px | 0.43 | 1.00 | 112 |
| loop | 2 % → 2 % | 2.2 px | 0.43 | 1.00 | 44 |
| tilted | 1 % → 1 % | 3.0 px | 0.42 | 1.00 | 20 |
| over the wet one | 2 % → 2 % | 2.2 px | 0.42 | 1.00 | 20 |
| long, no reload | 5 % → 5 % | 2.3 px | 0.43 | 1.00 | 101 | quarters: 0.02 → 0.02 → 0.02 → 0.03

Numbers say: light vs heavy: width 1.6 → 2.6 px, dark 0.42 → 0.43; the long stroke does not run out of paint.

## Brush Artist · Refs · #42 Oil pastel shaggy
Pastel · 18 px · 13.5 s

![Brush Artist · Refs · #42 Oil pastel shaggy](Brush-Artist-Refs-42-Oil-pastel-shaggy.png)

A light paint: laid on a grey sheet (on white it cannot be seen); **dark** = how far it is from the grey either way.

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 2 % → 2 % | 5.1 px | 0.35 | 1.00 | 30 |
| heavy line | 4 % → 4 % | 10.7 px | 0.36 | 1.00 | 64 |
| pressure swell | 3 % → 3 % | 9.5 px | 0.36 | 1.00 | 38 |
| fast wave | 8 % → 8 % | 9.0 px | 0.36 | 1.00 | 101 |
| slow wave | 7 % → 7 % | 8.2 px | 0.36 | 1.00 | 120 |
| spiral | 12 % → 12 % | 7.7 px | 0.36 | 1.00 | 153 |
| loop | 6 % → 6 % | 7.9 px | 0.36 | 1.00 | 77 |
| tilted | 2 % → 2 % | 6.9 px | 0.36 | 1.00 | 43 |
| over the wet one | 6 % → 6 % | 8.5 px | 0.36 | 1.00 | 35 |
| long, no reload | 15 % → 15 % | 6.9 px | 0.36 | 1.00 | 217 | quarters: 0.00 → 0.00 → 0.00 → 0.00

Numbers say: light vs heavy: width 5.1 → 10.7 px, dark 0.35 → 0.36; the long stroke does not run out of paint.

## Brush Artist · Refs · #43 Dragged black ink blocks
Gouache · 70 px · 45.0 s

![Brush Artist · Refs · #43 Dragged black ink blocks](Brush-Artist-Refs-43-Dragged-black-ink-blocks.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 19 % → 5 % | 54.9 px | 0.57 | 0.28 | 183 |
| heavy line | 24 % → 9 % | 69.0 px | 0.57 | 0.38 | 414 |
| pressure swell | 17 % → 9 % | 63.4 px | 0.57 | 0.53 | 276 |
| fast wave | 51 % → 11 % | 58.7 px | 0.57 | 0.21 | 767 |
| slow wave | 50 % → 10 % | 58.1 px | 0.57 | 0.20 | 1621 |
| spiral | 65 % → 14 % | 42.6 px | 0.57 | 0.22 | 1255 |
| loop | 45 % → 12 % | 58.1 px | 0.57 | 0.27 | 675 |
| tilted | 17 % → 16 % | 46.4 px | 0.57 | 0.98 | 386 |
| over the wet one | 37 % → 20 % | 55.6 px | 0.57 | 0.56 | 380 |
| long, no reload | 82 % → 17 % | 36.6 px | 0.57 | 0.21 | 2981 | quarters: 0.54 → 0.52 → 0.47 → 0.40

Numbers say: light vs heavy: width 54.9 → 69.0 px, dark 0.57 → 0.57.

## Brush Artist · Refs · #44 Blue looping ribbon
Oil · 80 px · 38.4 s

![Brush Artist · Refs · #44 Blue looping ribbon](Brush-Artist-Refs-44-Blue-looping-ribbon.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 26 % → 27 % | 74.9 px | 0.72 | 1.04 | 395 |
| heavy line | 27 % → 27 % | 79.6 px | 0.72 | 1.00 | 391 |
| pressure swell | 21 % → 21 % | 78.1 px | 0.72 | 1.03 | 285 |
| fast wave | 61 % → 64 % | 70.3 px | 0.73 | 1.05 | 1133 |
| slow wave | 61 % → 61 % | 70.0 px | 0.73 | 1.00 | 1928 |
| spiral | 78 % → 78 % | 51.3 px | 0.73 | 1.00 | 2411 |
| loop | 54 % → 54 % | 69.7 px | 0.73 | 1.00 | 1541 |
| tilted | 21 % → 21 % | 57.3 px | 0.72 | 1.00 | 500 |
| over the wet one | 44 % → 44 % | 64.9 px | 0.72 | 1.00 | 453 |
| long, no reload | 96 % → 96 % | 42.8 px | 0.73 | 1.00 | 3250 | quarters: 0.72 → 0.73 → 0.73 → 0.69

Numbers say: light vs heavy: width 74.9 → 79.6 px, dark 0.72 → 0.72; pressure barely changes the width; the long stroke does not run out of paint.

## Brush Artist · Refs · #45 Soft pastel pepper
Pastel · 40 px · 16.9 s

![Brush Artist · Refs · #45 Soft pastel pepper](Brush-Artist-Refs-45-Soft-pastel-pepper.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 4 % → 4 % | 11.3 px | 0.53 | 1.00 | 80 |
| heavy line | 8 % → 8 % | 23.0 px | 0.53 | 1.00 | 70 |
| pressure swell | 5 % → 5 % | 19.5 px | 0.53 | 1.00 | 66 |
| fast wave | 17 % → 17 % | 19.4 px | 0.53 | 1.00 | 242 |
| slow wave | 15 % → 15 % | 17.1 px | 0.53 | 1.00 | 391 |
| spiral | 25 % → 25 % | 16.3 px | 0.53 | 1.00 | 314 |
| loop | 12 % → 12 % | 16.1 px | 0.53 | 1.00 | 160 |
| tilted | 5 % → 5 % | 12.8 px | 0.53 | 1.00 | 77 |
| over the wet one | 11 % → 11 % | 17.7 px | 0.53 | 1.00 | 78 |
| long, no reload | 30 % → 30 % | 13.6 px | 0.53 | 1.00 | 449 | quarters: 0.18 → 0.18 → 0.18 → 0.18

Numbers say: light vs heavy: width 11.3 → 23.0 px, dark 0.53 → 0.53; the long stroke does not run out of paint.

## Brush Artist · Refs · #46 Red-brown ink lips
Watercolor · 50 px · 55.6 s

![Brush Artist · Refs · #46 Red-brown ink lips](Brush-Artist-Refs-46-Red-brown-ink-lips.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 12 % → 23 % | 33.6 px | 0.67 | 2.00 | 73 |
| heavy line | 19 % → 30 % | 54.1 px | 0.65 | 1.59 | 179 |
| pressure swell | 12 % → 20 % | 43.7 px | 0.67 | 1.73 | 99 |
| fast wave | 40 % → 60 % | 46.7 px | 0.66 | 1.48 | 275 |
| slow wave | 39 % → 58 % | 44.6 px | 0.69 | 1.52 | 494 |
| spiral | 63 % → 75 % | 41.6 px | 0.70 | 1.19 | 531 |
| loop | 35 % → 51 % | 44.9 px | 0.68 | 1.48 | 281 |
| tilted | 16 % → 17 % | 43.6 px | 0.67 | 1.07 | 199 |
| over the wet one | 33 % → 51 % | 47.6 px | 0.67 | 1.55 | 97 |
| long, no reload | 78 % → 95 % | 35.2 px | 0.70 | 1.21 | 689 | quarters: 0.71 → 0.71 → 0.70 → 0.64

Numbers say: light vs heavy: width 33.6 → 54.1 px, dark 0.67 → 0.65; the long stroke does not run out of paint; wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #47 Pink knife slabs
Heavy acrylic · 90 px · 38.6 s

![Brush Artist · Refs · #47 Pink knife slabs](Brush-Artist-Refs-47-Pink-knife-slabs.png)

A light paint: laid on a grey sheet (on white it cannot be seen); **dark** = how far it is from the grey either way.

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 28 % → 27 % | 81.1 px | 0.29 | 0.97 | 294 |
| heavy line | 29 % → 28 % | 83.5 px | 0.29 | 0.97 | 407 |
| pressure swell | 22 % → 22 % | 83.4 px | 0.29 | 1.01 | 242 |
| fast wave | 61 % → 60 % | 70.2 px | 0.28 | 0.98 | 810 |
| slow wave | 61 % → 59 % | 71.0 px | 0.27 | 0.96 | 1329 |
| spiral | 76 % → 58 % | 50.0 px | 0.27 | 0.76 | 1492 |
| loop | 55 % → 54 % | 71.7 px | 0.28 | 0.97 | 750 |
| tilted | 21 % → 21 % | 59.3 px | 0.29 | 1.00 | 399 |
| over the wet one | 46 % → 44 % | 68.0 px | 0.29 | 0.96 | 311 |
| long, no reload | 92 % → 76 % | 41.3 px | 0.26 | 0.83 | 2068 | quarters: 0.00 → 0.00 → 0.00 → 0.00

Numbers say: light vs heavy: width 81.1 → 83.5 px, dark 0.29 → 0.29; pressure barely changes the width; the long stroke does not run out of paint.

## Brush Artist · Refs · #48 Black bands with drips
Gouache · 70 px · 57.2 s

![Brush Artist · Refs · #48 Black bands with drips](Brush-Artist-Refs-48-Black-bands-with-drips.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 19 % → 18 % | 54.6 px | 0.69 | 0.93 | 229 |
| heavy line | 29 % → 24 % | 83.0 px | 0.69 | 0.84 | 307 |
| pressure swell | 23 % → 21 % | 86.1 px | 0.69 | 0.92 | 226 |
| fast wave | 53 % → 36 % | 61.8 px | 0.69 | 0.68 | 654 |
| slow wave | 53 % → 36 % | 61.7 px | 0.69 | 0.67 | 1182 |
| spiral | 64 % → 35 % | 41.9 px | 0.69 | 0.55 | 1271 |
| loop | 45 % → 36 % | 57.8 px | 0.69 | 0.81 | 564 |
| tilted | 19 % → 19 % | 52.3 px | 0.69 | 1.00 | 394 |
| over the wet one | 41 % → 38 % | 62.4 px | 0.69 | 0.92 | 272 |
| long, no reload | 74 % → 37 % | 33.3 px | 0.69 | 0.50 | 1501 | quarters: 0.64 → 0.61 → 0.54 → 0.45

Numbers say: light vs heavy: width 54.6 → 83.0 px, dark 0.69 → 0.69.

## Brush Artist · Refs · #49 Magenta letters round brush
Ink · 30 px · 43.1 s

![Brush Artist · Refs · #49 Magenta letters round brush](Brush-Artist-Refs-49-Magenta-letters-round-brush.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 6 % → 8 % | 17.5 px | 0.50 | 1.28 | 88 |
| heavy line | 21 % → 21 % | 62.0 px | 0.51 | 0.99 | 203 |
| pressure swell | 12 % → 13 % | 46.3 px | 0.52 | 1.01 | 125 |
| fast wave | 38 % → 38 % | 44.3 px | 0.51 | 0.99 | 438 |
| slow wave | 32 % → 31 % | 36.4 px | 0.51 | 0.99 | 421 |
| spiral | 50 % → 48 % | 32.8 px | 0.51 | 0.97 | 434 |
| loop | 29 % → 29 % | 37.6 px | 0.51 | 1.00 | 211 |
| tilted | 11 % → 11 % | 30.7 px | 0.52 | 1.01 | 109 |
| over the wet one | 26 % → 26 % | 42.1 px | 0.52 | 1.01 | 115 |
| long, no reload | 61 % → 56 % | 27.5 px | 0.51 | 0.92 | 897 | quarters: 0.41 → 0.36 → 0.30 → 0.25

Numbers say: light vs heavy: width 17.5 → 62.0 px, dark 0.50 → 0.51.

## Brush Artist · Refs · #50 Thick swipes on photo
Heavy acrylic · 40 px · 26.0 s

![Brush Artist · Refs · #50 Thick swipes on photo](Brush-Artist-Refs-50-Thick-swipes-on-photo.png)

A light paint: laid on a grey sheet (on white it cannot be seen); **dark** = how far it is from the grey either way.

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 13 % → 13 % | 38.1 px | 0.26 | 0.96 | 144 |
| heavy line | 14 % → 13 % | 40.2 px | 0.27 | 0.96 | 181 |
| pressure swell | 11 % → 10 % | 40.1 px | 0.25 | 0.95 | 122 |
| fast wave | 33 % → 31 % | 38.3 px | 0.25 | 0.93 | 398 |
| slow wave | 34 % → 32 % | 39.1 px | 0.26 | 0.95 | 667 |
| spiral | 58 % → 47 % | 38.5 px | 0.24 | 0.80 | 741 |
| loop | 28 % → 27 % | 36.9 px | 0.26 | 0.95 | 351 |
| tilted | 12 % → 12 % | 34.0 px | 0.26 | 1.00 | 176 |
| over the wet one | 25 % → 24 % | 35.3 px | 0.26 | 0.95 | 192 |
| long, no reload | 66 % → 46 % | 29.6 px | 0.24 | 0.69 | 1318 | quarters: 0.00 → 0.00 → 0.00 → 0.00

Numbers say: light vs heavy: width 38.1 → 40.2 px, dark 0.26 → 0.27; pressure barely changes the width; the long stroke does not run out of paint.

## Brush Artist · Refs · Drag #e8b4a8
Gouache · 40 px · 31.8 s

![Brush Artist · Refs · Drag #e8b4a8](Brush-Artist-Refs-Drag-e8b4a8.png)

A light paint: laid on a grey sheet (on white it cannot be seen); **dark** = how far it is from the grey either way.

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 12 % → 1 % | 35.1 px | 0.31 | 0.06 | 179 |
| heavy line | 14 % → 2 % | 39.4 px | 0.31 | 0.12 | 401 |
| pressure swell | 10 % → 2 % | 37.8 px | 0.31 | 0.21 | 184 |
| fast wave | 30 % → 3 % | 35.1 px | 0.31 | 0.08 | 518 |
| slow wave | 30 % → 3 % | 35.2 px | 0.31 | 0.09 | 773 |
| spiral | 41 % → 3 % | 26.8 px | 0.31 | 0.07 | 746 |
| loop | 27 % → 3 % | 34.5 px | 0.31 | 0.12 | 386 |
| tilted | 11 % → 11 % | 30.6 px | 0.31 | 0.96 | 233 |
| over the wet one | 23 % → 5 % | 33.4 px | 0.31 | 0.23 | 199 |
| long, no reload | 37 % → 4 % | 16.8 px | 0.31 | 0.10 | 1079 | quarters: 0.01 → 0.02 → 0.03 → 0.05

Numbers say: light vs heavy: width 35.1 → 39.4 px, dark 0.31 → 0.31; the long stroke does not run out of paint.

## Brush Artist · Refs · Drag #e8e4e0
Gouache · 40 px · 31.1 s

![Brush Artist · Refs · Drag #e8e4e0](Brush-Artist-Refs-Drag-e8e4e0.png)

A light paint: laid on a grey sheet (on white it cannot be seen); **dark** = how far it is from the grey either way.

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 12 % → 1 % | 35.1 px | 0.39 | 0.06 | 170 |
| heavy line | 14 % → 2 % | 39.4 px | 0.39 | 0.12 | 165 |
| pressure swell | 10 % → 2 % | 37.8 px | 0.39 | 0.21 | 132 |
| fast wave | 30 % → 3 % | 35.1 px | 0.39 | 0.08 | 471 |
| slow wave | 30 % → 3 % | 35.2 px | 0.39 | 0.09 | 785 |
| spiral | 41 % → 3 % | 26.8 px | 0.39 | 0.07 | 979 |
| loop | 27 % → 3 % | 34.5 px | 0.38 | 0.12 | 384 |
| tilted | 11 % → 11 % | 30.6 px | 0.38 | 0.96 | 211 |
| over the wet one | 23 % → 5 % | 33.4 px | 0.38 | 0.23 | 172 |
| long, no reload | 37 % → 4 % | 16.8 px | 0.38 | 0.10 | 1023 | quarters: 0.01 → 0.02 → 0.04 → 0.05

Numbers say: light vs heavy: width 35.1 → 39.4 px, dark 0.39 → 0.39; the long stroke does not run out of paint.

## Brush Artist · Refs · Finger
Pastel · 36 px · 27.5 s · over bands of wet oil paint and oil pastel in turn (it works on paint already there: look at what it does to the bands; covered counts the bands too)

![Brush Artist · Refs · Finger](Brush-Artist-Refs-Finger.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 27 % → 27 % | 79.5 px | 0.78 | 1.00 | 56 |
| heavy line | 30 % → 30 % | 87.1 px | 0.76 | 1.00 | 73 |
| pressure swell | 28 % → 28 % | 103.6 px | 0.78 | 1.00 | 44 |
| fast wave | 36 % → 36 % | 41.8 px | 0.72 | 1.00 | 160 |
| slow wave | 35 % → 35 % | 40.3 px | 0.72 | 1.00 | 345 |
| spiral | 43 % → 43 % | 28.7 px | 0.68 | 1.00 | 266 |
| loop | 33 % → 33 % | 42.9 px | 0.73 | 1.00 | 141 |
| tilted | 28 % → 28 % | 77.0 px | 0.74 | 1.00 | 65 |
| over the wet one | 32 % → 32 % | 13.1 px | 0.74 | 1.00 | 69 |
| long, no reload | 48 % → 48 % | 21.5 px | 0.66 | 1.00 | 364 | quarters: 0.33 → 0.35 → 0.33 → 0.37

Numbers say: light vs heavy: width 79.5 → 87.1 px, dark 0.78 → 0.76; pressure barely changes the width; the long stroke does not run out of paint.

## Brush Artist · Ink — wash
Watercolor · 38 px · 44.4 s

![Brush Artist · Ink — wash](Brush-Artist-Ink-wash.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 11 % → 11 % | 31.6 px | 0.38 | 1.03 | 81 |
| heavy line | 19 % → 19 % | 54.3 px | 0.32 | 1.03 | 150 |
| pressure swell | 12 % → 12 % | 45.1 px | 0.36 | 1.04 | 82 |
| fast wave | 39 % → 41 % | 44.7 px | 0.30 | 1.05 | 242 |
| slow wave | 37 % → 38 % | 42.6 px | 0.37 | 1.04 | 423 |
| spiral | 57 % → 60 % | 37.9 px | 0.30 | 1.04 | 426 |
| loop | 32 % → 33 % | 41.8 px | 0.34 | 1.02 | 665 |
| tilted | 13 % → 14 % | 36.8 px | 0.38 | 1.04 | 120 |
| over the wet one | 29 % → 30 % | 42.8 px | 0.38 | 1.04 | 95 |
| long, no reload | 65 % → 70 % | 29.2 px | 0.29 | 1.08 | 629 | quarters: 0.33 → 0.26 → 0.18 → 0.11

Numbers say: light vs heavy: width 31.6 → 54.3 px, dark 0.38 → 0.32.

## Brush Artist · Ink — brush line
Ink · 16 px · 35.8 s

![Brush Artist · Ink — brush line](Brush-Artist-Ink-brush-line.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 3 % → 5 % | 7.7 px | 0.78 | 1.80 | 49 |
| heavy line | 13 % → 13 % | 39.0 px | 0.88 | 0.99 | 107 |
| pressure swell | 8 % → 8 % | 28.4 px | 0.87 | 1.05 | 65 |
| fast wave | 24 % → 23 % | 27.6 px | 0.87 | 0.96 | 560 |
| slow wave | 19 % → 19 % | 22.5 px | 0.87 | 0.97 | 310 |
| spiral | 30 % → 27 % | 19.9 px | 0.86 | 0.90 | 333 |
| loop | 18 % → 18 % | 23.4 px | 0.88 | 1.00 | 177 |
| tilted | 7 % → 7 % | 20.1 px | 0.88 | 1.01 | 85 |
| over the wet one | 17 % → 17 % | 26.8 px | 0.88 | 1.00 | 79 |
| long, no reload | 42 % → 31 % | 18.8 px | 0.85 | 0.73 | 510 | quarters: 0.49 → 0.40 → 0.30 → 0.21

Numbers say: light vs heavy: width 7.7 → 39.0 px, dark 0.78 → 0.88; wet paint spreads well beyond the stroke.

## Brush Artist · Ink — dry brush
Gouache · 30 px · 30.0 s

![Brush Artist · Ink — dry brush](Brush-Artist-Ink-dry-brush.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 7 % → 1 % | 21.8 px | 0.71 | 0.11 | 174 |
| heavy line | 10 % → 1 % | 27.7 px | 0.71 | 0.10 | 309 |
| pressure swell | 7 % → 2 % | 25.5 px | 0.71 | 0.23 | 81 |
| fast wave | 21 % → 2 % | 24.2 px | 0.71 | 0.09 | 330 |
| slow wave | 21 % → 2 % | 23.9 px | 0.71 | 0.08 | 568 |
| spiral | 31 % → 2 % | 20.6 px | 0.71 | 0.06 | 509 |
| loop | 18 % → 2 % | 23.9 px | 0.71 | 0.13 | 294 |
| tilted | 9 % → 8 % | 24.1 px | 0.71 | 0.96 | 169 |
| over the wet one | 17 % → 4 % | 22.8 px | 0.71 | 0.24 | 135 |
| long, no reload | 31 % → 3 % | 14.0 px | 0.71 | 0.09 | 757 | quarters: 0.38 → 0.32 → 0.22 → 0.09

Numbers say: light vs heavy: width 21.8 → 27.7 px, dark 0.71 → 0.71.

## Brush Artist · Watercolour — blue
Watercolor · 40 px · 36.0 s

![Brush Artist · Watercolour — blue](Brush-Artist-Watercolour-blue.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 6 % → 10 % | 16.7 px | 0.25 | 1.70 | 43 |
| heavy line | 11 % → 12 % | 31.5 px | 0.25 | 1.13 | 79 |
| pressure swell | 7 % → 9 % | 25.4 px | 0.26 | 1.32 | 43 |
| fast wave | 24 % → 25 % | 27.8 px | 0.24 | 1.05 | 204 |
| slow wave | 22 % → 27 % | 25.9 px | 0.26 | 1.22 | 315 |
| spiral | 38 % → 41 % | 25.1 px | 0.22 | 1.08 | 327 |
| loop | 20 % → 22 % | 25.3 px | 0.26 | 1.13 | 170 |
| tilted | 12 % → 12 % | 33.3 px | 0.26 | 1.00 | 176 |
| over the wet one | 21 % → 24 % | 24.7 px | 0.26 | 1.15 | 97 |
| long, no reload | 51 % → 54 % | 23.0 px | 0.22 | 1.04 | 514 | quarters: 0.18 → 0.14 → 0.11 → 0.08

Numbers say: light vs heavy: width 16.7 → 31.5 px, dark 0.25 → 0.25; wet paint spreads well beyond the stroke.

## Brush Artist · Watercolour — violet
Watercolor · 40 px · 36.4 s

![Brush Artist · Watercolour — violet](Brush-Artist-Watercolour-violet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 6 % → 10 % | 16.7 px | 0.40 | 1.70 | 48 |
| heavy line | 11 % → 12 % | 31.5 px | 0.40 | 1.13 | 104 |
| pressure swell | 7 % → 9 % | 25.4 px | 0.41 | 1.32 | 58 |
| fast wave | 24 % → 25 % | 27.8 px | 0.38 | 1.05 | 203 |
| slow wave | 22 % → 27 % | 25.9 px | 0.40 | 1.22 | 421 |
| spiral | 38 % → 41 % | 25.1 px | 0.36 | 1.08 | 469 |
| loop | 20 % → 22 % | 25.3 px | 0.40 | 1.13 | 170 |
| tilted | 12 % → 12 % | 33.3 px | 0.40 | 1.00 | 165 |
| over the wet one | 21 % → 24 % | 24.7 px | 0.40 | 1.15 | 128 |
| long, no reload | 51 % → 54 % | 23.0 px | 0.34 | 1.04 | 470 | quarters: 0.28 → 0.22 → 0.17 → 0.14

Numbers say: light vs heavy: width 16.7 → 31.5 px, dark 0.40 → 0.40; wet paint spreads well beyond the stroke.

## Brush Artist · Watercolour — teal
Watercolor · 40 px · 40.3 s

![Brush Artist · Watercolour — teal](Brush-Artist-Watercolour-teal.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 6 % → 10 % | 16.7 px | 0.16 | 1.70 | 61 |
| heavy line | 11 % → 12 % | 31.5 px | 0.16 | 1.13 | 132 |
| pressure swell | 7 % → 9 % | 25.4 px | 0.17 | 1.32 | 46 |
| fast wave | 24 % → 25 % | 27.8 px | 0.15 | 1.05 | 181 |
| slow wave | 22 % → 27 % | 25.9 px | 0.17 | 1.22 | 427 |
| spiral | 38 % → 41 % | 25.1 px | 0.15 | 1.08 | 284 |
| loop | 20 % → 22 % | 25.3 px | 0.16 | 1.13 | 155 |
| tilted | 12 % → 12 % | 33.3 px | 0.16 | 1.00 | 146 |
| over the wet one | 21 % → 24 % | 24.7 px | 0.16 | 1.15 | 79 |
| long, no reload | 51 % → 54 % | 23.0 px | 0.14 | 1.04 | 447 | quarters: 0.11 → 0.09 → 0.07 → 0.06

Numbers say: light vs heavy: width 16.7 → 31.5 px, dark 0.16 → 0.16; wet paint spreads well beyond the stroke.

## Brush Artist · Gouache
Gouache · 30 px · 44.8 s

![Brush Artist · Gouache](Brush-Artist-Gouache.png)

A light paint: laid on a grey sheet (on white it cannot be seen); **dark** = how far it is from the grey either way.

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 8 % → 8 % | 24.4 px | 0.27 | 0.97 | 104 |
| heavy line | 15 % → 11 % | 42.8 px | 0.27 | 0.78 | 122 |
| pressure swell | 11 % → 9 % | 41.0 px | 0.27 | 0.84 | 64 |
| fast wave | 30 % → 13 % | 34.4 px | 0.26 | 0.45 | 244 |
| slow wave | 29 % → 14 % | 33.9 px | 0.26 | 0.46 | 731 |
| spiral | 40 % → 14 % | 26.6 px | 0.26 | 0.35 | 635 |
| loop | 23 % → 15 % | 30.4 px | 0.26 | 0.62 | 231 |
| tilted | 10 % → 10 % | 27.1 px | 0.26 | 1.01 | 154 |
| over the wet one | 21 % → 19 % | 32.8 px | 0.26 | 0.89 | 104 |
| long, no reload | 43 % → 15 % | 19.1 px | 0.26 | 0.35 | 692 | quarters: 0.01 → 0.01 → 0.01 → 0.01

Numbers say: light vs heavy: width 24.4 → 42.8 px, dark 0.27 → 0.27; the long stroke does not run out of paint.

## Brush Artist · Oil — bristle
Oil · 30 px · 22.1 s

![Brush Artist · Oil — bristle](Brush-Artist-Oil-bristle.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 9 % → 9 % | 26.3 px | 0.54 | 1.00 | 114 |
| heavy line | 10 % → 10 % | 28.6 px | 0.54 | 1.00 | 278 |
| pressure swell | 8 % → 8 % | 28.2 px | 0.55 | 1.00 | 173 |
| fast wave | 24 % → 24 % | 27.3 px | 0.55 | 1.00 | 642 |
| slow wave | 25 % → 25 % | 28.3 px | 0.55 | 1.00 | 1221 |
| spiral | 39 % → 39 % | 25.6 px | 0.54 | 1.00 | 831 |
| loop | 20 % → 20 % | 26.3 px | 0.54 | 1.00 | 394 |
| tilted | 11 % → 11 % | 29.9 px | 0.53 | 1.00 | 188 |
| over the wet one | 20 % → 20 % | 25.5 px | 0.53 | 1.00 | 150 |
| long, no reload | 50 % → 50 % | 22.4 px | 0.54 | 1.00 | 1081 | quarters: 0.32 → 0.30 → 0.29 → 0.28

Numbers say: light vs heavy: width 26.3 → 28.6 px, dark 0.54 → 0.54; pressure barely changes the width; the long stroke does not run out of paint.

## Brush Artist · Charcoal — stick
Charcoal · 28 px · 14.5 s

![Brush Artist · Charcoal — stick](Brush-Artist-Charcoal-stick.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 3 % → 3 % | 8.4 px | 0.85 | 1.00 | 30 |
| heavy line | 6 % → 6 % | 17.8 px | 0.85 | 1.00 | 34 |
| pressure swell | 4 % → 4 % | 13.9 px | 0.85 | 1.00 | 23 |
| fast wave | 12 % → 12 % | 14.0 px | 0.85 | 1.00 | 72 |
| slow wave | 11 % → 11 % | 12.5 px | 0.85 | 1.00 | 123 |
| spiral | 19 % → 19 % | 12.7 px | 0.85 | 1.00 | 127 |
| loop | 10 % → 10 % | 12.8 px | 0.85 | 1.00 | 58 |
| tilted | 4 % → 4 % | 10.9 px | 0.85 | 1.00 | 47 |
| over the wet one | 9 % → 9 % | 13.5 px | 0.85 | 1.00 | 35 |
| long, no reload | 27 % → 27 % | 12.2 px | 0.85 | 1.00 | 164 | quarters: 0.26 → 0.25 → 0.26 → 0.27

Numbers say: light vs heavy: width 8.4 → 17.8 px, dark 0.85 → 0.85; the long stroke does not run out of paint.

## Brush Artist · Charcoal — stick B
Charcoal · 36 px · 14.3 s

![Brush Artist · Charcoal — stick B](Brush-Artist-Charcoal-stick-B.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 4 % → 4 % | 10.5 px | 0.85 | 1.00 | 48 |
| heavy line | 7 % → 7 % | 21.1 px | 0.85 | 1.00 | 38 |
| pressure swell | 4 % → 4 % | 16.5 px | 0.85 | 1.00 | 31 |
| fast wave | 15 % → 15 % | 16.8 px | 0.85 | 1.00 | 88 |
| slow wave | 13 % → 13 % | 14.7 px | 0.85 | 1.00 | 141 |
| spiral | 23 % → 23 % | 15.0 px | 0.85 | 1.00 | 149 |
| loop | 11 % → 11 % | 14.8 px | 0.85 | 1.00 | 72 |
| tilted | 4 % → 4 % | 12.3 px | 0.85 | 1.00 | 49 |
| over the wet one | 10 % → 10 % | 15.9 px | 0.85 | 1.00 | 35 |
| long, no reload | 31 % → 31 % | 13.9 px | 0.85 | 1.00 | 247 | quarters: 0.30 → 0.28 → 0.29 → 0.30

Numbers say: light vs heavy: width 10.5 → 21.1 px, dark 0.85 → 0.85; the long stroke does not run out of paint.

## Brush Artist · Charcoal — stick C
Charcoal · 22 px · 13.8 s

![Brush Artist · Charcoal — stick C](Brush-Artist-Charcoal-stick-C.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 2 % → 2 % | 6.9 px | 0.85 | 1.00 | 37 |
| heavy line | 5 % → 5 % | 15.3 px | 0.85 | 1.00 | 29 |
| pressure swell | 3 % → 3 % | 12.2 px | 0.85 | 1.00 | 19 |
| fast wave | 10 % → 10 % | 12.1 px | 0.85 | 1.00 | 65 |
| slow wave | 9 % → 9 % | 10.8 px | 0.85 | 1.00 | 89 |
| spiral | 17 % → 17 % | 11.0 px | 0.85 | 1.00 | 98 |
| loop | 9 % → 9 % | 11.4 px | 0.85 | 1.00 | 57 |
| tilted | 4 % → 4 % | 9.9 px | 0.85 | 1.00 | 42 |
| over the wet one | 8 % → 8 % | 11.7 px | 0.85 | 1.00 | 25 |
| long, no reload | 24 % → 24 % | 11.0 px | 0.85 | 1.00 | 136 | quarters: 0.24 → 0.22 → 0.23 → 0.24

Numbers say: light vs heavy: width 6.9 → 15.3 px, dark 0.85 → 0.85; the long stroke does not run out of paint.

## Brush Artist · Refs · #01 Henry Ward peach cloud — own sheet
own sheet 600 × 600 · Gouache · 44 px · 20.7 s

![Brush Artist · Refs · #01 Henry Ward peach cloud — own sheet](Brush-Artist-Refs-01-Henry-Ward-peach-cloud-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 16 % → 42 % | 45.1 px | 0.59 | 2.69 | 251 |
| stroke 2 | 27 % → 63 % | 88.6 px | 0.59 | 2.33 | 238 |
| stroke 3 | 31 % → 62 % | 90.5 px | 0.59 | 1.99 | 212 |
| stroke 4 | 34 % → 68 % | 109.7 px | 0.59 | 2.03 | 201 |
| stroke 5 | 33 % → 59 % | 95.9 px | 0.59 | 1.80 | 231 |
| stroke 6 | 33 % → 46 % | 100.5 px | 0.59 | 1.40 | 171 |
| stroke 7 | 18 % → 54 % | 44.9 px | 0.60 | 2.99 | 214 |
| stroke 8 | 19 % → 50 % | 48.4 px | 0.60 | 2.61 | 207 |
| stroke 9 | 23 % → 51 % | 58.1 px | 0.60 | 2.27 | 353 |
| stroke 10 | 25 % → 52 % | 66.9 px | 0.60 | 2.08 | 305 |
| stroke 11 | 27 % → 55 % | 77.1 px | 0.60 | 2.00 | 348 |
| stroke 12 | 31 % → 57 % | 92.9 px | 0.60 | 1.85 | 310 |
| stroke 13 | 39 % → 60 % | 113.6 px | 0.60 | 1.53 | 251 |
| stroke 14 | 41 % → 62 % | 118.2 px | 0.60 | 1.50 | 223 |
| stroke 15 | 55 % → 68 % | 163.8 px | 0.59 | 1.23 | 201 |
| stroke 16 | 57 % → 69 % | 171.6 px | 0.59 | 1.22 | 211 |
| stroke 17 | 57 % → 70 % | 160.1 px | 0.59 | 1.22 | 229 |
| stroke 18 | 58 % → 68 % | 169.0 px | 0.59 | 1.17 | 199 |
| stroke 19 | 60 % → 67 % | 167.7 px | 0.59 | 1.12 | 204 |
| stroke 20 | 59 % → 64 % | 170.4 px | 0.59 | 1.08 | 211 |
| stroke 21 | 59 % → 61 % | 171.3 px | 0.59 | 1.03 | 223 |
| stroke 22 | 60 % → 62 % | 176.0 px | 0.59 | 1.03 | 210 |
| stroke 23 | 60 % → 60 % | 170.9 px | 0.59 | 1.00 | 223 |
| stroke 24 | 64 % → 63 % | 190.6 px | 0.59 | 1.00 | 217 |

Numbers say: wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #02 Henry Ward cream strokes — own sheet
own sheet 600 × 600 · Gouache · 46 px · 13.5 s

![Brush Artist · Refs · #02 Henry Ward cream strokes — own sheet](Brush-Artist-Refs-02-Henry-Ward-cream-strokes-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 21 % → 39 % | 42.9 px | 0.71 | 1.87 | 389 |
| stroke 2 | 32 % → 45 % | 84.2 px | 0.71 | 1.40 | 328 |
| stroke 3 | 31 % → 52 % | 79.6 px | 0.72 | 1.68 | 285 |
| stroke 4 | 34 % → 49 % | 83.2 px | 0.71 | 1.45 | 316 |
| stroke 5 | 39 % → 52 % | 96.5 px | 0.72 | 1.33 | 331 |
| stroke 6 | 32 % → 46 % | 76.6 px | 0.71 | 1.46 | 282 |
| stroke 7 | 34 % → 32 % | 86.1 px | 0.71 | 0.94 | 308 |

Numbers say: wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #03 Henry Ward navy contours — own sheet
own sheet 600 × 600 · Heavy acrylic · 22 px · 3.8 s

![Brush Artist · Refs · #03 Henry Ward navy contours — own sheet](Brush-Artist-Refs-03-Henry-Ward-navy-contours-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 11 % → 18 % | 23.1 px | 0.69 | 1.56 | 244 |
| stroke 2 | 20 % → 23 % | 28.3 px | 0.69 | 1.14 | 217 |
| stroke 3 | 23 % → 23 % | 33.4 px | 0.69 | 1.01 | 217 |
| stroke 4 | 23 % → 21 % | 50.8 px | 0.69 | 0.92 | 285 |

Numbers say: wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #04 Henry Ward grey cloud — own sheet
own sheet 600 × 600 · Gouache · 50 px · 20.2 s

![Brush Artist · Refs · #04 Henry Ward grey cloud — own sheet](Brush-Artist-Refs-04-Henry-Ward-grey-cloud-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 17 % → 49 % | 48.9 px | 0.40 | 2.96 | 251 |
| stroke 2 | 20 % → 51 % | 57.9 px | 0.40 | 2.54 | 276 |
| stroke 3 | 29 % → 58 % | 81.5 px | 0.40 | 2.00 | 285 |
| stroke 4 | 32 % → 62 % | 93.3 px | 0.40 | 1.92 | 293 |
| stroke 5 | 38 % → 68 % | 116.0 px | 0.40 | 1.78 | 269 |
| stroke 6 | 41 % → 72 % | 135.7 px | 0.40 | 1.74 | 319 |
| stroke 7 | 48 % → 78 % | 140.2 px | 0.40 | 1.63 | 320 |
| stroke 8 | 46 % → 78 % | 137.6 px | 0.40 | 1.68 | 324 |
| stroke 9 | 47 % → 78 % | 142.0 px | 0.40 | 1.65 | 329 |
| stroke 10 | 48 % → 78 % | 153.3 px | 0.40 | 1.64 | 293 |
| stroke 11 | 48 % → 78 % | 135.7 px | 0.40 | 1.63 | 284 |
| stroke 12 | 49 % → 78 % | 147.0 px | 0.40 | 1.60 | 275 |
| stroke 13 | 48 % → 78 % | 137.3 px | 0.40 | 1.63 | 265 |
| stroke 14 | 49 % → 78 % | 144.8 px | 0.40 | 1.61 | 291 |
| stroke 15 | 49 % → 74 % | 139.9 px | 0.40 | 1.52 | 276 |
| stroke 16 | 49 % → 71 % | 148.5 px | 0.40 | 1.46 | 290 |
| stroke 17 | 48 % → 62 % | 136.9 px | 0.40 | 1.31 | 275 |
| stroke 18 | 47 % → 58 % | 154.0 px | 0.40 | 1.24 | 376 |
| stroke 19 | 48 % → 48 % | 142.0 px | 0.40 | 1.02 | 373 |
| stroke 20 | 48 % → 48 % | 152.3 px | 0.40 | 0.99 | 372 |

Numbers say: wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #05 Henry Ward green in rust loops — own sheet
own sheet 600 × 600 · Heavy acrylic · 20 px · 3.2 s

![Brush Artist · Refs · #05 Henry Ward green in rust loops — own sheet](Brush-Artist-Refs-05-Henry-Ward-green-in-rust-loops-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 12 % → 19 % | 20.9 px | 0.02 | 1.60 | 152 |
| stroke 2 | 12 % → 11 % | 23.5 px | 0.02 | 0.93 | 202 |
| stroke 3 | 23 % → 21 % | 41.5 px | 0.02 | 0.93 | 158 |

Numbers say: wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #06 Henry Ward scrubbed grey — own sheet
own sheet 600 × 600 · Gouache · 50 px · 25.9 s

![Brush Artist · Refs · #06 Henry Ward scrubbed grey — own sheet](Brush-Artist-Refs-06-Henry-Ward-scrubbed-grey-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 20 % → 56 % | 48.6 px | 0.40 | 2.83 | 397 |
| stroke 2 | 24 % → 58 % | 64.3 px | 0.40 | 2.41 | 395 |
| stroke 3 | 31 % → 63 % | 93.7 px | 0.40 | 2.04 | 353 |
| stroke 4 | 31 % → 63 % | 98.4 px | 0.40 | 2.01 | 292 |
| stroke 5 | 45 % → 78 % | 136.1 px | 0.40 | 1.71 | 307 |
| stroke 6 | 48 % → 78 % | 145.5 px | 0.40 | 1.64 | 279 |
| stroke 7 | 49 % → 78 % | 139.4 px | 0.40 | 1.61 | 275 |
| stroke 8 | 48 % → 78 % | 152.1 px | 0.40 | 1.63 | 297 |
| stroke 9 | 47 % → 78 % | 144.7 px | 0.40 | 1.67 | 281 |
| stroke 10 | 47 % → 79 % | 152.5 px | 0.40 | 1.68 | 295 |
| stroke 11 | 48 % → 79 % | 141.3 px | 0.40 | 1.63 | 322 |
| stroke 12 | 48 % → 79 % | 147.5 px | 0.40 | 1.63 | 298 |
| stroke 13 | 47 % → 78 % | 133.4 px | 0.40 | 1.66 | 316 |
| stroke 14 | 46 % → 78 % | 135.2 px | 0.40 | 1.69 | 297 |
| stroke 15 | 47 % → 78 % | 134.5 px | 0.40 | 1.67 | 320 |
| stroke 16 | 48 % → 78 % | 152.3 px | 0.40 | 1.65 | 276 |
| stroke 17 | 48 % → 72 % | 141.3 px | 0.40 | 1.52 | 368 |
| stroke 18 | 49 % → 70 % | 147.0 px | 0.40 | 1.43 | 289 |
| stroke 19 | 47 % → 63 % | 139.2 px | 0.40 | 1.36 | 339 |
| stroke 20 | 47 % → 61 % | 146.3 px | 0.40 | 1.30 | 391 |
| stroke 21 | 47 % → 52 % | 137.0 px | 0.40 | 1.10 | 336 |
| stroke 22 | 47 % → 47 % | 156.1 px | 0.40 | 0.99 | 296 |

Numbers say: wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #07 Henry Ward blue L + black zigzag — own sheet
own sheet 600 × 600 · Heavy acrylic · 34 px · 2.6 s

![Brush Artist · Refs · #07 Henry Ward blue L + black zigzag — own sheet](Brush-Artist-Refs-07-Henry-Ward-blue-L-black-zigzag-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 15 % → 17 % | 35.6 px | 0.59 | 1.14 | 146 |
| stroke 2 | 17 % → 16 % | 42.8 px | 0.59 | 0.93 | 120 |

## Brush Artist · Refs · #08 Henry Ward olive bands — own sheet
own sheet 600 × 600 · Gouache · 34 px · 9.1 s

![Brush Artist · Refs · #08 Henry Ward olive bands — own sheet](Brush-Artist-Refs-08-Henry-Ward-olive-bands-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 16 % → 16 % | 32.3 px | 0.57 | 1.03 | 253 |
| stroke 2 | 27 % → 21 % | 61.7 px | 0.57 | 0.76 | 238 |
| stroke 3 | 24 % → 29 % | 50.1 px | 0.57 | 1.23 | 269 |
| stroke 4 | 28 % → 26 % | 61.0 px | 0.57 | 0.91 | 255 |
| stroke 5 | 36 % → 31 % | 73.5 px | 0.57 | 0.87 | 251 |
| stroke 6 | 25 % → 15 % | 46.3 px | 0.57 | 0.61 | 232 |

## Brush Artist · Refs · #09 Henry Ward white loops — own sheet
own sheet 600 × 600 · Gouache · 46 px · 15.8 s

![Brush Artist · Refs · #09 Henry Ward white loops — own sheet](Brush-Artist-Refs-09-Henry-Ward-white-loops-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 29 % → 15 % | 15.7 px | 0.04 | 0.50 | 2221 |
| stroke 2 | 37 % → 10 % | 36.9 px | 0.05 | 0.28 | 1530 |
| stroke 3 | 43 % → 10 % | 39.6 px | 0.05 | 0.23 | 1459 |
| stroke 4 | 15 % → 5 % | 35.7 px | 0.04 | 0.31 | 403 |
| stroke 5 | 13 % → 5 % | 36.4 px | 0.05 | 0.35 | 483 |
| stroke 6 | 14 % → 10 % | 37.4 px | 0.05 | 0.72 | 526 |
| stroke 7 | 27 % → 10 % | 70.6 px | 0.05 | 0.37 | 427 |
| stroke 8 | 21 % → 7 % | 35.8 px | 0.03 | 0.35 | 475 |

## Brush Artist · Refs · #10 Henry Ward maroon loops — own sheet
own sheet 600 × 600 · Heavy acrylic · 30 px · 5.4 s

![Brush Artist · Refs · #10 Henry Ward maroon loops — own sheet](Brush-Artist-Refs-10-Henry-Ward-maroon-loops-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 12 % → 28 % | 28.7 px | 0.72 | 2.39 | 282 |
| stroke 2 | 22 % → 40 % | 48.5 px | 0.72 | 1.87 | 156 |
| stroke 3 | 29 % → 37 % | 58.5 px | 0.72 | 1.27 | 236 |
| stroke 4 | 41 % → 39 % | 92.8 px | 0.72 | 0.96 | 142 |
| stroke 5 | 34 % → 32 % | 85.8 px | 0.72 | 0.93 | 208 |

Numbers say: wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #11 Henry Ward purple spun balls — own sheet
own sheet 600 × 600 · Heavy acrylic · 36 px · 5.4 s

![Brush Artist · Refs · #11 Henry Ward purple spun balls — own sheet](Brush-Artist-Refs-11-Henry-Ward-purple-spun-balls-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 24 % → 35 % | 26.5 px | 0.68 | 1.43 | 491 |
| stroke 2 | 35 % → 46 % | 38.2 px | 0.68 | 1.33 | 524 |
| stroke 3 | 36 % → 34 % | 39.2 px | 0.68 | 0.97 | 579 |

## Brush Artist · Refs · #12 Henry Ward black-olive cage — own sheet
own sheet 600 × 600 · Gouache · 28 px · 8.0 s

![Brush Artist · Refs · #12 Henry Ward black-olive cage — own sheet](Brush-Artist-Refs-12-Henry-Ward-black-olive-cage-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 13 % → 21 % | 24.3 px | 0.59 | 1.64 | 388 |
| stroke 2 | 13 % → 22 % | 29.9 px | 0.59 | 1.76 | 237 |
| stroke 3 | 27 % → 28 % | 43.0 px | 0.59 | 1.04 | 321 |
| stroke 4 | 28 % → 27 % | 55.3 px | 0.59 | 0.98 | 176 |
| stroke 5 | 28 % → 18 % | 51.1 px | 0.59 | 0.65 | 205 |
| stroke 6 | 44 % → 30 % | 84.4 px | 0.59 | 0.68 | 332 |

Numbers say: wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #13 Henry Ward blue streaky form — own sheet
own sheet 600 × 600 · Gouache · 50 px · 18.6 s

![Brush Artist · Refs · #13 Henry Ward blue streaky form — own sheet](Brush-Artist-Refs-13-Henry-Ward-blue-streaky-form-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 16 % → 9 % | 48.6 px | 0.04 | 0.60 | 323 |
| stroke 2 | 22 % → 9 % | 67.0 px | 0.04 | 0.41 | 355 |
| stroke 3 | 33 % → 9 % | 95.7 px | 0.04 | 0.29 | 315 |
| stroke 4 | 33 % → 9 % | 105.7 px | 0.04 | 0.27 | 313 |
| stroke 5 | 48 % → 10 % | 138.8 px | 0.04 | 0.21 | 412 |
| stroke 6 | 47 % → 11 % | 135.4 px | 0.04 | 0.24 | 347 |
| stroke 7 | 49 % → 12 % | 144.2 px | 0.04 | 0.25 | 305 |
| stroke 8 | 49 % → 10 % | 149.4 px | 0.04 | 0.21 | 291 |
| stroke 9 | 48 % → 9 % | 150.0 px | 0.04 | 0.19 | 287 |
| stroke 10 | 48 % → 9 % | 159.4 px | 0.04 | 0.18 | 283 |
| stroke 11 | 46 % → 7 % | 142.9 px | 0.04 | 0.14 | 362 |
| stroke 12 | 48 % → 8 % | 142.7 px | 0.04 | 0.17 | 324 |
| stroke 13 | 47 % → 10 % | 145.1 px | 0.04 | 0.21 | 346 |
| stroke 14 | 45 % → 9 % | 134.4 px | 0.04 | 0.21 | 292 |
| stroke 15 | 46 % → 10 % | 132.4 px | 0.04 | 0.21 | 337 |
| stroke 16 | 48 % → 10 % | 141.9 px | 0.04 | 0.20 | 347 |
| stroke 17 | 58 % → 6 % | 144.8 px | 0.04 | 0.11 | 376 |
| stroke 18 | 60 % → 6 % | 145.4 px | 0.04 | 0.10 | 343 |
| stroke 19 | 67 % → 7 % | 136.1 px | 0.04 | 0.11 | 282 |
| stroke 20 | 75 % → 8 % | 143.1 px | 0.04 | 0.10 | 521 |
| stroke 21 | 17 % → 5 % | 35.8 px | 0.04 | 0.32 | 310 |
| stroke 22 | 13 % → 9 % | 38.5 px | 0.04 | 0.66 | 363 |
| stroke 23 | 25 % → 10 % | 79.1 px | 0.04 | 0.38 | 241 |
| stroke 24 | 16 % → 7 % | 43.6 px | 0.04 | 0.42 | 295 |
| stroke 25 | 21 % → 8 % | 54.3 px | 0.04 | 0.36 | 297 |

## Brush Artist · Refs · #14 Henry Ward olive totem — own sheet
own sheet 600 × 600 · Heavy acrylic · 48 px · 10.5 s

![Brush Artist · Refs · #14 Henry Ward olive totem — own sheet](Brush-Artist-Refs-14-Henry-Ward-olive-totem-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 18 % → 46 % | 46.9 px | 0.38 | 2.58 | 242 |
| stroke 2 | 21 % → 50 % | 64.3 px | 0.38 | 2.44 | 218 |
| stroke 3 | 29 % → 52 % | 100.6 px | 0.38 | 1.78 | 156 |
| stroke 4 | 30 % → 54 % | 113.7 px | 0.38 | 1.80 | 173 |
| stroke 5 | 39 % → 63 % | 135.6 px | 0.38 | 1.63 | 164 |
| stroke 6 | 39 % → 65 % | 150.4 px | 0.38 | 1.68 | 161 |
| stroke 7 | 37 % → 61 % | 124.3 px | 0.38 | 1.66 | 197 |
| stroke 8 | 37 % → 63 % | 142.4 px | 0.38 | 1.69 | 203 |
| stroke 9 | 38 % → 63 % | 130.9 px | 0.38 | 1.67 | 149 |
| stroke 10 | 38 % → 62 % | 141.0 px | 0.38 | 1.62 | 194 |
| stroke 11 | 40 % → 65 % | 143.7 px | 0.38 | 1.60 | 230 |
| stroke 12 | 38 % → 65 % | 144.2 px | 0.38 | 1.70 | 180 |
| stroke 13 | 39 % → 66 % | 135.5 px | 0.38 | 1.72 | 168 |
| stroke 14 | 37 % → 62 % | 134.5 px | 0.38 | 1.68 | 216 |
| stroke 15 | 40 % → 66 % | 136.9 px | 0.38 | 1.65 | 229 |
| stroke 16 | 38 % → 64 % | 138.8 px | 0.38 | 1.66 | 171 |
| stroke 17 | 38 % → 62 % | 126.2 px | 0.38 | 1.65 | 201 |
| stroke 18 | 40 % → 66 % | 154.9 px | 0.38 | 1.64 | 188 |
| stroke 19 | 40 % → 60 % | 137.9 px | 0.38 | 1.52 | 190 |
| stroke 20 | 41 % → 55 % | 144.4 px | 0.38 | 1.34 | 209 |
| stroke 21 | 46 % → 55 % | 137.7 px | 0.38 | 1.18 | 215 |
| stroke 22 | 54 % → 53 % | 146.7 px | 0.38 | 0.99 | 167 |

Numbers say: wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #15 Ultramarine brush script — own sheet
own sheet 600 × 600 · Ink · 4 px · 12.9 s

![Brush Artist · Refs · #15 Ultramarine brush script — own sheet](Brush-Artist-Refs-15-Ultramarine-brush-script-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 39 % → 42 % | 8.9 px | 0.67 | 1.05 | 73 |
| stroke 2 | 40 % → 42 % | 8.8 px | 0.66 | 1.06 | 76 |
| stroke 3 | 40 % → 42 % | 9.5 px | 0.73 | 1.06 | 52 |
| stroke 4 | 42 % → 45 % | 10.1 px | 0.74 | 1.08 | 25 |
| stroke 5 | 44 % → 48 % | 9.7 px | 0.73 | 1.08 | 37 |
| stroke 6 | 42 % → 44 % | 9.4 px | 0.65 | 1.04 | 76 |
| stroke 7 | 43 % → 46 % | 9.2 px | 0.72 | 1.08 | 55 |
| stroke 8 | 38 % → 40 % | 9.2 px | 0.68 | 1.06 | 65 |
| stroke 9 | 40 % → 42 % | 9.2 px | 0.69 | 1.06 | 52 |
| stroke 10 | 36 % → 38 % | 9.8 px | 0.68 | 1.05 | 65 |
| stroke 11 | 42 % → 45 % | 9.5 px | 0.70 | 1.06 | 58 |
| stroke 12 | 39 % → 41 % | 9.4 px | 0.66 | 1.05 | 62 |
| stroke 13 | 45 % → 48 % | 10.2 px | 0.71 | 1.06 | 39 |
| stroke 14 | 38 % → 41 % | 9.8 px | 0.72 | 1.06 | 33 |
| stroke 15 | 37 % → 39 % | 9.1 px | 0.69 | 1.06 | 63 |
| stroke 16 | 42 % → 45 % | 9.4 px | 0.72 | 1.06 | 36 |
| stroke 17 | 41 % → 44 % | 7.1 px | 0.71 | 1.08 | 64 |
| stroke 18 | 43 % → 45 % | 9.2 px | 0.73 | 1.06 | 51 |
| stroke 19 | 39 % → 41 % | 8.8 px | 0.66 | 1.05 | 115 |
| stroke 20 | 40 % → 43 % | 9.4 px | 0.71 | 1.06 | 66 |
| stroke 21 | 40 % → 43 % | 9.9 px | 0.70 | 1.06 | 73 |
| stroke 22 | 42 % → 44 % | 8.4 px | 0.65 | 1.06 | 111 |
| stroke 23 | 40 % → 43 % | 10.1 px | 0.73 | 1.07 | 47 |
| stroke 24 | 38 % → 40 % | 8.7 px | 0.73 | 1.07 | 53 |
| stroke 25 | 40 % → 43 % | 9.8 px | 0.72 | 1.07 | 76 |
| stroke 26 | 46 % → 48 % | 9.2 px | 0.68 | 1.05 | 76 |
| stroke 27 | 42 % → 45 % | 8.8 px | 0.63 | 1.05 | 117 |
| stroke 28 | 44 % → 46 % | 9.1 px | 0.70 | 1.06 | 54 |
| stroke 29 | 36 % → 39 % | 10.6 px | 0.72 | 1.08 | 37 |
| stroke 30 | 39 % → 40 % | 8.6 px | 0.71 | 1.04 | 58 |
| stroke 31 | 43 % → 46 % | 10.3 px | 0.75 | 1.07 | 33 |
| stroke 32 | 42 % → 45 % | 9.4 px | 0.73 | 1.09 | 40 |
| stroke 33 | 35 % → 38 % | 10.8 px | 0.72 | 1.08 | 31 |
| stroke 34 | 40 % → 43 % | 9.7 px | 0.73 | 1.07 | 34 |
| stroke 35 | 35 % → 37 % | 9.3 px | 0.65 | 1.05 | 71 |

## Brush Artist · Refs · #18 Blue oil-stick scribbles — own sheet
own sheet 600 × 600 · Pastel · 10 px · 4.3 s

![Brush Artist · Refs · #18 Blue oil-stick scribbles — own sheet](Brush-Artist-Refs-18-Blue-oil-stick-scribbles-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 15 % → 31 % | 3.8 px | 0.49 | 2.11 | 192 |
| stroke 2 | 13 % → 37 % | 3.6 px | 0.49 | 2.73 | 315 |
| stroke 3 | 16 % → 26 % | 5.8 px | 0.49 | 1.66 | 240 |
| stroke 4 | 15 % → 29 % | 8.0 px | 0.49 | 1.88 | 259 |
| stroke 5 | 29 % → 34 % | 8.4 px | 0.49 | 1.19 | 206 |
| stroke 6 | 25 % → 26 % | 9.4 px | 0.49 | 1.02 | 166 |
| stroke 7 | 26 % → 32 % | 8.3 px | 0.49 | 1.24 | 235 |
| stroke 8 | 30 % → 30 % | 17.0 px | 0.49 | 1.00 | 246 |

Numbers say: wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #20 Orange-red crayon scribble — own sheet
own sheet 600 × 600 · Pastel · 14 px · 4.2 s

![Brush Artist · Refs · #20 Orange-red crayon scribble — own sheet](Brush-Artist-Refs-20-Orange-red-crayon-scribble-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 8 % → 18 % | 5.5 px | 0.59 | 2.46 | 340 |
| stroke 2 | 9 % → 23 % | 6.8 px | 0.59 | 2.48 | 258 |
| stroke 3 | 13 % → 21 % | 8.5 px | 0.59 | 1.64 | 217 |
| stroke 4 | 24 % → 32 % | 8.9 px | 0.59 | 1.34 | 242 |
| stroke 5 | 27 % → 27 % | 7.7 px | 0.59 | 1.00 | 232 |
| stroke 6 | 22 % → 22 % | 16.8 px | 0.59 | 1.00 | 300 |

Numbers say: wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #21 Gritty black contours — own sheet
own sheet 600 × 600 · Gouache · 12 px · 6.8 s

![Brush Artist · Refs · #21 Gritty black contours — own sheet](Brush-Artist-Refs-21-Gritty-black-contours-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 10 % → 8 % | 10.6 px | 0.36 | 0.84 | 249 |
| stroke 2 | 9 % → 5 % | 15.4 px | 0.36 | 0.57 | 306 |
| stroke 3 | 14 % → 4 % | 12.9 px | 0.36 | 0.28 | 194 |
| stroke 4 | 16 % → 8 % | 19.7 px | 0.36 | 0.50 | 208 |
| stroke 5 | 18 % → 8 % | 21.5 px | 0.36 | 0.47 | 120 |

## Brush Artist · Refs · #22 Bold black brush poster — own sheet
own sheet 600 × 600 · Ink · 20 px · 8.0 s

![Brush Artist · Refs · #22 Bold black brush poster — own sheet](Brush-Artist-Refs-22-Bold-black-brush-poster-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 22 % → 27 % | 36.3 px | 0.94 | 1.20 | 166 |
| stroke 2 | 27 % → 37 % | 41.4 px | 0.95 | 1.36 | 49 |
| stroke 3 | 28 % → 28 % | 43.6 px | 0.94 | 1.00 | 60 |
| stroke 4 | 27 % → 39 % | 53.8 px | 0.94 | 1.42 | 92 |
| stroke 5 | 25 % → 25 % | 42.9 px | 0.94 | 1.00 | 178 |

## Brush Artist · Refs · #23 Dry white on orange + black line — own sheet
own sheet 600 × 600 · Gouache · 50 px · 16.1 s

![Brush Artist · Refs · #23 Dry white on orange + black line — own sheet](Brush-Artist-Refs-23-Dry-white-on-orange-black-line-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 13 % → 35 % | 44.0 px | 0.44 | 2.78 | 237 |
| stroke 2 | 15 % → 32 % | 53.3 px | 0.44 | 2.13 | 252 |
| stroke 3 | 22 % → 35 % | 82.6 px | 0.44 | 1.59 | 241 |
| stroke 4 | 24 % → 39 % | 95.4 px | 0.44 | 1.61 | 360 |
| stroke 5 | 35 % → 47 % | 126.2 px | 0.44 | 1.36 | 338 |
| stroke 6 | 36 % → 51 % | 146.8 px | 0.44 | 1.43 | 345 |
| stroke 7 | 31 % → 50 % | 118.1 px | 0.44 | 1.61 | 304 |
| stroke 8 | 31 % → 48 % | 122.2 px | 0.44 | 1.52 | 369 |
| stroke 9 | 31 % → 48 % | 117.4 px | 0.44 | 1.54 | 245 |
| stroke 10 | 32 % → 49 % | 127.1 px | 0.43 | 1.51 | 208 |
| stroke 11 | 35 % → 51 % | 129.9 px | 0.43 | 1.48 | 246 |
| stroke 12 | 35 % → 50 % | 135.5 px | 0.44 | 1.45 | 270 |
| stroke 13 | 36 % → 53 % | 134.7 px | 0.43 | 1.45 | 205 |
| stroke 14 | 35 % → 52 % | 137.7 px | 0.43 | 1.48 | 218 |
| stroke 15 | 35 % → 47 % | 132.2 px | 0.43 | 1.33 | 231 |
| stroke 16 | 34 % → 41 % | 135.8 px | 0.43 | 1.19 | 249 |
| stroke 17 | 34 % → 34 % | 119.2 px | 0.43 | 1.01 | 277 |
| stroke 18 | 41 % → 36 % | 149.1 px | 0.43 | 0.88 | 221 |

Numbers say: wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #24 Picasso flat oil — own sheet
own sheet 600 × 600 · Oil · 34 px · 8.0 s

![Brush Artist · Refs · #24 Picasso flat oil — own sheet](Brush-Artist-Refs-24-Picasso-flat-oil-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 16 % → 45 % | 34.7 px | 0.23 | 2.74 | 175 |
| stroke 2 | 20 % → 48 % | 47.2 px | 0.24 | 2.40 | 248 |
| stroke 3 | 29 % → 59 % | 62.5 px | 0.23 | 2.07 | 206 |
| stroke 4 | 37 % → 65 % | 83.1 px | 0.23 | 1.76 | 209 |
| stroke 5 | 43 % → 71 % | 94.5 px | 0.23 | 1.65 | 176 |
| stroke 6 | 44 % → 66 % | 102.1 px | 0.23 | 1.50 | 188 |
| stroke 7 | 45 % → 66 % | 94.8 px | 0.23 | 1.46 | 172 |
| stroke 8 | 44 % → 66 % | 106.9 px | 0.23 | 1.50 | 174 |
| stroke 9 | 37 % → 62 % | 81.5 px | 0.23 | 1.67 | 159 |
| stroke 10 | 39 % → 62 % | 93.1 px | 0.23 | 1.58 | 221 |
| stroke 11 | 37 % → 60 % | 78.6 px | 0.23 | 1.62 | 216 |
| stroke 12 | 38 % → 61 % | 91.1 px | 0.23 | 1.60 | 200 |
| stroke 13 | 38 % → 67 % | 84.4 px | 0.23 | 1.76 | 199 |
| stroke 14 | 39 % → 69 % | 88.9 px | 0.23 | 1.75 | 192 |
| stroke 15 | 39 % → 62 % | 83.3 px | 0.23 | 1.58 | 237 |
| stroke 16 | 38 % → 55 % | 87.9 px | 0.23 | 1.43 | 264 |
| stroke 17 | 43 % → 48 % | 90.0 px | 0.23 | 1.12 | 244 |
| stroke 18 | 42 % → 42 % | 102.6 px | 0.23 | 1.00 | 191 |

Numbers say: wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #25 Yellow heavy flat stroke — own sheet
own sheet 600 × 600 · Heavy acrylic · 110 px · 4.5 s

![Brush Artist · Refs · #25 Yellow heavy flat stroke — own sheet](Brush-Artist-Refs-25-Yellow-heavy-flat-stroke-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 18 % → 18 % | 104.2 px | 0.17 | 0.98 | 1062 |

## Brush Artist · Refs · #27 Orange impasto swatch — own sheet
own sheet 600 × 600 · Heavy acrylic · 60 px · 5.5 s

![Brush Artist · Refs · #27 Orange impasto swatch — own sheet](Brush-Artist-Refs-27-Orange-impasto-swatch-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 8 % → 21 % | 61.8 px | 0.33 | 2.60 | 100 |
| stroke 2 | 7 % → 33 % | 62.5 px | 0.33 | 4.67 | 64 |
| stroke 3 | 25 % → 36 % | 245.4 px | 0.33 | 1.40 | 54 |
| stroke 4 | 10 % → 12 % | 69.5 px | 0.33 | 1.25 | 93 |
| stroke 5 | 17 % → 33 % | 63.5 px | 0.33 | 1.90 | 104 |
| stroke 6 | 18 % → 31 % | 145.0 px | 0.33 | 1.79 | 88 |
| stroke 7 | 8 % → 15 % | 70.2 px | 0.33 | 1.86 | 77 |
| stroke 8 | 33 % → 34 % | 337.0 px | 0.33 | 1.04 | 87 |
| stroke 9 | 38 % → 37 % | 185.4 px | 0.33 | 0.98 | 95 |
| stroke 10 | 33 % → 33 % | 304.7 px | 0.33 | 0.98 | 110 |

Numbers say: wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #28 Miles Davis black lines — own sheet
own sheet 600 × 600 · Ink · 22 px · 9.2 s

![Brush Artist · Refs · #28 Miles Davis black lines — own sheet](Brush-Artist-Refs-28-Miles-Davis-black-lines-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 22 % → 32 % | 36.4 px | 0.88 | 1.42 | 247 |
| stroke 2 | 28 % → 48 % | 38.1 px | 0.88 | 1.73 | 183 |
| stroke 3 | 39 % → 44 % | 75.0 px | 0.88 | 1.12 | 159 |
| stroke 4 | 42 % → 48 % | 83.5 px | 0.88 | 1.15 | 243 |
| stroke 5 | 55 % → 55 % | 109.6 px | 0.88 | 1.00 | 299 |

Numbers say: wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #29 Shrigley magenta asterisk — own sheet
own sheet 600 × 600 · Watercolor · 70 px · 8.7 s

![Brush Artist · Refs · #29 Shrigley magenta asterisk — own sheet](Brush-Artist-Refs-29-Shrigley-magenta-asterisk-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 13 % → 37 % | 46.6 px | 0.72 | 2.85 | 401 |
| stroke 2 | 12 % → 12 % | 87.1 px | 0.71 | 1.00 | 360 |
| stroke 3 | 28 % → 37 % | 100.9 px | 0.72 | 1.31 | 252 |
| stroke 4 | 23 % → 23 % | 163.9 px | 0.71 | 1.02 | 331 |

Numbers say: wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #30 Red gouache face patch — own sheet
own sheet 600 × 600 · Gouache · 60 px · 17.2 s

![Brush Artist · Refs · #30 Red gouache face patch — own sheet](Brush-Artist-Refs-30-Red-gouache-face-patch-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 12 % → 37 % | 51.5 px | 0.53 | 3.23 | 234 |
| stroke 2 | 15 % → 40 % | 74.5 px | 0.53 | 2.72 | 215 |
| stroke 3 | 24 % → 50 % | 115.9 px | 0.53 | 2.06 | 209 |
| stroke 4 | 27 % → 51 % | 134.0 px | 0.53 | 1.93 | 244 |
| stroke 5 | 34 % → 60 % | 159.9 px | 0.53 | 1.77 | 226 |
| stroke 6 | 35 % → 61 % | 178.2 px | 0.53 | 1.76 | 242 |
| stroke 7 | 34 % → 59 % | 160.8 px | 0.53 | 1.73 | 287 |
| stroke 8 | 34 % → 56 % | 162.4 px | 0.53 | 1.65 | 282 |
| stroke 9 | 36 % → 60 % | 173.0 px | 0.53 | 1.66 | 240 |
| stroke 10 | 38 % → 62 % | 196.7 px | 0.53 | 1.64 | 211 |
| stroke 11 | 37 % → 61 % | 182.4 px | 0.53 | 1.66 | 206 |
| stroke 12 | 36 % → 58 % | 178.3 px | 0.53 | 1.62 | 225 |
| stroke 13 | 33 % → 46 % | 156.5 px | 0.53 | 1.39 | 203 |
| stroke 14 | 33 % → 41 % | 157.6 px | 0.53 | 1.25 | 296 |
| stroke 15 | 33 % → 37 % | 153.3 px | 0.53 | 1.12 | 225 |
| stroke 16 | 39 % → 39 % | 184.8 px | 0.53 | 0.99 | 234 |

Numbers say: wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #31 Warhol blotted line — own sheet
own sheet 600 × 600 · Ink · 6 px · 7.2 s

![Brush Artist · Refs · #31 Warhol blotted line — own sheet](Brush-Artist-Refs-31-Warhol-blotted-line-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 21 % → 42 % | 15.7 px | 0.82 | 1.98 | 121 |
| stroke 2 | 17 % → 23 % | 15.8 px | 0.82 | 1.34 | 117 |
| stroke 3 | 24 % → 25 % | 25.0 px | 0.82 | 1.02 | 96 |
| stroke 4 | 31 % → 40 % | 31.7 px | 0.82 | 1.28 | 87 |
| stroke 5 | 35 % → 43 % | 36.3 px | 0.82 | 1.23 | 107 |
| stroke 6 | 32 % → 33 % | 26.5 px | 0.81 | 1.03 | 107 |

Numbers say: wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #32 Thick orange swipes — own sheet
own sheet 600 × 600 · Heavy acrylic · 90 px · 5.7 s

![Brush Artist · Refs · #32 Thick orange swipes — own sheet](Brush-Artist-Refs-32-Thick-orange-swipes-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 14 % → 27 % | 86.0 px | 0.03 | 1.90 | 479 |
| stroke 2 | 26 % → 38 % | 176.9 px | 0.03 | 1.43 | 479 |
| stroke 3 | 28 % → 27 % | 177.5 px | 0.03 | 0.98 | 397 |

Numbers say: wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #33 Red wet-in-wet band — own sheet
own sheet 600 × 600 · Watercolor · 80 px · 13.7 s

![Brush Artist · Refs · #33 Red wet-in-wet band — own sheet](Brush-Artist-Refs-33-Red-wet-in-wet-band-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 23 % → 56 % | 88.2 px | 0.62 | 2.41 | 635 |
| stroke 2 | 30 % → 51 % | 243.8 px | 0.62 | 1.69 | 136 |
| stroke 3 | 37 % → 53 % | 355.7 px | 0.62 | 1.45 | 134 |
| stroke 4 | 42 % → 60 % | 410.7 px | 0.63 | 1.41 | 158 |
| stroke 5 | 42 % → 54 % | 352.8 px | 0.62 | 1.31 | 170 |
| stroke 6 | 42 % → 46 % | 320.2 px | 0.61 | 1.10 | 168 |

Numbers say: wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #34 Magenta oil patches — own sheet
own sheet 600 × 600 · Oil · 60 px · 6.2 s

![Brush Artist · Refs · #34 Magenta oil patches — own sheet](Brush-Artist-Refs-34-Magenta-oil-patches-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 9 % → 42 % | 61.9 px | 0.13 | 4.82 | 180 |
| stroke 2 | 9 % → 29 % | 62.8 px | 0.13 | 3.15 | 116 |
| stroke 3 | 7 % → 35 % | 62.3 px | 0.13 | 4.71 | 109 |
| stroke 4 | 16 % → 20 % | 132.0 px | 0.12 | 1.27 | 89 |
| stroke 5 | 23 % → 33 % | 124.6 px | 0.13 | 1.43 | 111 |
| stroke 6 | 20 % → 38 % | 171.4 px | 0.13 | 1.90 | 100 |
| stroke 7 | 30 % → 35 % | 237.9 px | 0.13 | 1.18 | 128 |
| stroke 8 | 33 % → 39 % | 235.0 px | 0.13 | 1.18 | 134 |
| stroke 9 | 25 % → 26 % | 159.7 px | 0.13 | 1.07 | 140 |
| stroke 10 | 29 % → 29 % | 257.2 px | 0.13 | 1.00 | 85 |
| stroke 11 | 36 % → 36 % | 324.6 px | 0.13 | 1.00 | 129 |
| stroke 12 | 26 % → 26 % | 184.4 px | 0.13 | 1.00 | 92 |

Numbers say: wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #35 Red band with runs — own sheet
own sheet 600 × 600 · Watercolor · 70 px · 8.2 s

![Brush Artist · Refs · #35 Red band with runs — own sheet](Brush-Artist-Refs-35-Red-band-with-runs-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 21 % → 32 % | 77.5 px | 0.50 | 1.54 | 362 |

Numbers say: wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #36 Magenta letters flat brush — own sheet
own sheet 600 × 600 · Gouache · 36 px · 18.1 s

![Brush Artist · Refs · #36 Magenta letters flat brush — own sheet](Brush-Artist-Refs-36-Magenta-letters-flat-brush-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 20 % → 39 % | 59.1 px | 0.50 | 1.95 | 56 |
| stroke 2 | 20 % → 32 % | 46.7 px | 0.50 | 1.59 | 44 |
| stroke 3 | 29 % → 54 % | 86.9 px | 0.50 | 1.86 | 37 |
| stroke 4 | 26 % → 44 % | 51.2 px | 0.50 | 1.67 | 147 |
| stroke 5 | 33 % → 55 % | 96.1 px | 0.50 | 1.67 | 129 |
| stroke 6 | 42 % → 56 % | 242.5 px | 0.50 | 1.33 | 39 |
| stroke 7 | 30 % → 44 % | 56.7 px | 0.50 | 1.45 | 168 |
| stroke 8 | 31 % → 53 % | 98.5 px | 0.50 | 1.68 | 99 |
| stroke 9 | 38 % → 51 % | 158.3 px | 0.50 | 1.33 | 33 |
| stroke 10 | 37 % → 63 % | 106.7 px | 0.50 | 1.72 | 113 |
| stroke 11 | 39 % → 62 % | 225.9 px | 0.50 | 1.58 | 24 |
| stroke 12 | 43 % → 56 % | 81.8 px | 0.50 | 1.29 | 143 |
| stroke 13 | 33 % → 46 % | 117.7 px | 0.50 | 1.43 | 66 |
| stroke 14 | 35 % → 52 % | 134.5 px | 0.50 | 1.47 | 72 |
| stroke 15 | 38 % → 56 % | 108.5 px | 0.50 | 1.49 | 115 |
| stroke 16 | 41 % → 50 % | 231.8 px | 0.50 | 1.23 | 23 |
| stroke 17 | 44 % → 52 % | 81.6 px | 0.50 | 1.19 | 210 |
| stroke 18 | 27 % → 36 % | 97.6 px | 0.50 | 1.35 | 65 |
| stroke 19 | 40 % → 39 % | 117.2 px | 0.50 | 0.96 | 78 |
| stroke 20 | 45 % → 45 % | 132.3 px | 0.50 | 0.98 | 71 |
| stroke 21 | 41 % → 39 % | 78.6 px | 0.50 | 0.96 | 140 |

Numbers say: wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #37 Oil still life dabs — own sheet
own sheet 600 × 600 · Oil · 40 px · 6.7 s

![Brush Artist · Refs · #37 Oil still life dabs — own sheet](Brush-Artist-Refs-37-Oil-still-life-dabs-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 7 % → 7 % | 44.1 px | 0.39 | 1.00 | 81 |
| stroke 2 | 6 % → 27 % | 44.4 px | 0.39 | 4.43 | 51 |
| stroke 3 | 12 % → 36 % | 92.6 px | 0.39 | 3.01 | 34 |
| stroke 4 | 9 % → 9 % | 42.7 px | 0.39 | 1.00 | 92 |
| stroke 5 | 6 % → 10 % | 43.2 px | 0.39 | 1.71 | 60 |
| stroke 6 | 13 % → 31 % | 83.4 px | 0.39 | 2.32 | 84 |
| stroke 7 | 11 % → 24 % | 115.5 px | 0.39 | 2.18 | 32 |
| stroke 8 | 8 % → 14 % | 89.6 px | 0.39 | 1.63 | 25 |
| stroke 9 | 13 % → 14 % | 68.1 px | 0.38 | 1.09 | 94 |
| stroke 10 | 21 % → 25 % | 106.5 px | 0.39 | 1.20 | 119 |
| stroke 11 | 24 % → 28 % | 201.6 px | 0.39 | 1.17 | 47 |
| stroke 12 | 21 % → 21 % | 227.4 px | 0.39 | 1.01 | 51 |
| stroke 13 | 16 % → 16 % | 167.7 px | 0.40 | 1.00 | 23 |
| stroke 14 | 16 % → 16 % | 132.7 px | 0.39 | 1.00 | 41 |

Numbers say: wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #38 Sanguine drawing — own sheet
own sheet 600 × 600 · Pastel · 6 px · 4.7 s

![Brush Artist · Refs · #38 Sanguine drawing — own sheet](Brush-Artist-Refs-38-Sanguine-drawing-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 3 % → 14 % | 2.9 px | 0.57 | 5.29 | 12 |
| stroke 2 | 3 % → 7 % | 2.9 px | 0.57 | 2.89 | 10 |
| stroke 3 | 3 % → 9 % | 2.9 px | 0.57 | 3.40 | 20 |
| stroke 4 | 2 % → 17 % | 2.7 px | 0.57 | 7.20 | 13 |
| stroke 5 | 2 % → 7 % | 2.7 px | 0.57 | 3.03 | 31 |
| stroke 6 | 3 % → 19 % | 3.4 px | 0.57 | 6.31 | 16 |
| stroke 7 | 5 % → 14 % | 5.2 px | 0.57 | 3.07 | 14 |
| stroke 8 | 4 % → 16 % | 4.7 px | 0.57 | 3.79 | 12 |
| stroke 9 | 3 % → 7 % | 2.9 px | 0.57 | 2.66 | 21 |
| stroke 10 | 4 % → 16 % | 4.7 px | 0.57 | 3.83 | 26 |
| stroke 11 | 3 % → 4 % | 2.9 px | 0.57 | 1.61 | 20 |
| stroke 12 | 4 % → 15 % | 4.8 px | 0.57 | 3.58 | 17 |
| stroke 13 | 8 % → 17 % | 8.9 px | 0.57 | 2.23 | 15 |
| stroke 14 | 4 % → 14 % | 4.9 px | 0.57 | 3.19 | 28 |
| stroke 15 | 9 % → 18 % | 10.7 px | 0.57 | 1.86 | 18 |
| stroke 16 | 6 % → 16 % | 6.6 px | 0.57 | 2.71 | 11 |
| stroke 17 | 4 % → 9 % | 4.4 px | 0.57 | 2.25 | 12 |
| stroke 18 | 3 % → 5 % | 2.9 px | 0.57 | 1.85 | 13 |
| stroke 19 | 6 % → 16 % | 6.9 px | 0.57 | 2.68 | 13 |
| stroke 20 | 8 % → 14 % | 9.2 px | 0.57 | 1.70 | 15 |
| stroke 21 | 4 % → 4 % | 4.3 px | 0.57 | 1.00 | 11 |
| stroke 22 | 8 % → 13 % | 8.6 px | 0.57 | 1.79 | 14 |
| stroke 23 | 7 % → 12 % | 8.3 px | 0.57 | 1.61 | 20 |
| stroke 24 | 4 % → 7 % | 4.7 px | 0.57 | 1.71 | 25 |
| stroke 25 | 8 % → 14 % | 8.7 px | 0.57 | 1.84 | 21 |
| stroke 26 | 6 % → 8 % | 6.5 px | 0.57 | 1.34 | 7 |
| stroke 27 | 4 % → 4 % | 4.3 px | 0.57 | 1.10 | 13 |
| stroke 28 | 7 % → 11 % | 8.2 px | 0.57 | 1.59 | 14 |
| stroke 29 | 8 % → 17 % | 8.8 px | 0.57 | 2.21 | 12 |
| stroke 30 | 13 % → 17 % | 14.9 px | 0.57 | 1.29 | 21 |
| stroke 31 | 5 % → 6 % | 5.4 px | 0.57 | 1.29 | 13 |
| stroke 32 | 10 % → 13 % | 11.8 px | 0.57 | 1.24 | 13 |
| stroke 33 | 7 % → 8 % | 8.5 px | 0.57 | 1.07 | 18 |
| stroke 34 | 11 % → 14 % | 12.0 px | 0.57 | 1.36 | 23 |
| stroke 35 | 9 % → 14 % | 10.0 px | 0.57 | 1.61 | 21 |
| stroke 36 | 10 % → 13 % | 11.4 px | 0.57 | 1.26 | 14 |
| stroke 37 | 9 % → 16 % | 10.5 px | 0.57 | 1.71 | 17 |
| stroke 38 | 13 % → 19 % | 14.8 px | 0.57 | 1.48 | 16 |
| stroke 39 | 14 % → 17 % | 15.7 px | 0.57 | 1.21 | 21 |
| stroke 40 | 6 % → 7 % | 7.2 px | 0.57 | 1.14 | 18 |
| stroke 41 | 16 % → 16 % | 17.7 px | 0.57 | 1.01 | 29 |
| stroke 42 | 14 % → 16 % | 15.2 px | 0.57 | 1.17 | 19 |
| stroke 43 | 10 % → 12 % | 11.6 px | 0.57 | 1.17 | 36 |
| stroke 44 | 12 % → 15 % | 14.3 px | 0.57 | 1.22 | 22 |
| stroke 45 | 2 % → 2 % | 2.7 px | 0.57 | 1.00 | 16 |
| stroke 46 | 16 % → 16 % | 18.5 px | 0.57 | 1.00 | 17 |
| stroke 47 | 13 % → 13 % | 15.0 px | 0.57 | 1.00 | 19 |
| stroke 48 | 12 % → 13 % | 14.3 px | 0.57 | 1.07 | 14 |
| stroke 49 | 19 % → 19 % | 21.5 px | 0.57 | 1.00 | 14 |
| stroke 50 | 10 % → 10 % | 11.6 px | 0.57 | 1.00 | 13 |

Numbers say: wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #39 Very thick impasto — own sheet
own sheet 600 × 600 · Heavy acrylic · 60 px · 6.8 s

![Brush Artist · Refs · #39 Very thick impasto — own sheet](Brush-Artist-Refs-39-Very-thick-impasto-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 26 % → 37 % | 59.6 px | 0.43 | 1.42 | 383 |
| stroke 2 | 31 % → 48 % | 93.9 px | 0.44 | 1.54 | 365 |
| stroke 3 | 37 % → 49 % | 124.6 px | 0.43 | 1.33 | 348 |
| stroke 4 | 31 % → 44 % | 90.9 px | 0.44 | 1.41 | 373 |
| stroke 5 | 42 % → 41 % | 104.2 px | 0.44 | 0.98 | 405 |

Numbers say: wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #40 Watercolour blooms — own sheet
own sheet 600 × 600 · Watercolor · 90 px · 9.7 s

![Brush Artist · Refs · #40 Watercolour blooms — own sheet](Brush-Artist-Refs-40-Watercolour-blooms-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 21 % → 25 % | 92.4 px | 0.13 | 1.19 | 937 |

## Brush Artist · Refs · #41 Coloured pencil hatching — own sheet
own sheet 600 × 600 · Pastel · 4 px · 3.5 s

![Brush Artist · Refs · #41 Coloured pencil hatching — own sheet](Brush-Artist-Refs-41-Coloured-pencil-hatching-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 3 % → 13 % | 2.2 px | 0.35 | 4.64 | 9 |
| stroke 2 | 3 % → 7 % | 2.3 px | 0.35 | 2.29 | 7 |
| stroke 3 | 2 % → 11 % | 1.9 px | 0.35 | 4.38 | 6 |
| stroke 4 | 3 % → 19 % | 2.1 px | 0.35 | 6.73 | 5 |
| stroke 5 | 4 % → 7 % | 2.9 px | 0.35 | 1.83 | 12 |
| stroke 6 | 3 % → 13 % | 2.3 px | 0.35 | 4.19 | 10 |
| stroke 7 | 3 % → 15 % | 2.6 px | 0.35 | 4.43 | 12 |
| stroke 8 | 3 % → 12 % | 2.1 px | 0.35 | 4.20 | 8 |
| stroke 9 | 5 % → 11 % | 3.6 px | 0.35 | 2.27 | 7 |
| stroke 10 | 5 % → 15 % | 3.8 px | 0.35 | 2.99 | 6 |
| stroke 11 | 4 % → 13 % | 3.0 px | 0.35 | 3.28 | 8 |
| stroke 12 | 3 % → 3 % | 2.1 px | 0.35 | 1.00 | 8 |
| stroke 13 | 7 % → 17 % | 5.2 px | 0.35 | 2.45 | 6 |
| stroke 14 | 3 % → 13 % | 2.4 px | 0.35 | 4.19 | 6 |
| stroke 15 | 6 % → 12 % | 4.4 px | 0.35 | 2.09 | 6 |
| stroke 16 | 7 % → 11 % | 5.1 px | 0.35 | 1.61 | 5 |
| stroke 17 | 3 % → 3 % | 2.1 px | 0.35 | 1.00 | 5 |
| stroke 18 | 5 % → 8 % | 3.6 px | 0.35 | 1.65 | 7 |
| stroke 19 | 5 % → 13 % | 3.8 px | 0.35 | 2.72 | 6 |
| stroke 20 | 5 % → 14 % | 3.7 px | 0.35 | 2.92 | 5 |
| stroke 21 | 4 % → 13 % | 3.2 px | 0.35 | 3.20 | 12 |
| stroke 22 | 9 % → 16 % | 6.8 px | 0.35 | 1.77 | 5 |
| stroke 23 | 9 % → 13 % | 6.5 px | 0.35 | 1.55 | 9 |
| stroke 24 | 6 % → 14 % | 4.7 px | 0.35 | 2.18 | 10 |
| stroke 25 | 5 % → 10 % | 3.5 px | 0.35 | 2.27 | 5 |
| stroke 26 | 3 % → 6 % | 2.7 px | 0.35 | 1.81 | 8 |
| stroke 27 | 3 % → 7 % | 2.3 px | 0.35 | 2.26 | 6 |
| stroke 28 | 6 % → 10 % | 4.5 px | 0.35 | 1.70 | 5 |
| stroke 29 | 3 % → 13 % | 2.4 px | 0.35 | 4.21 | 6 |
| stroke 30 | 6 % → 9 % | 4.4 px | 0.35 | 1.46 | 11 |
| stroke 31 | 7 % → 14 % | 5.1 px | 0.35 | 2.14 | 7 |
| stroke 32 | 3 % → 6 % | 2.5 px | 0.35 | 1.79 | 5 |
| stroke 33 | 6 % → 11 % | 5.0 px | 0.35 | 1.67 | 4 |
| stroke 34 | 3 % → 6 % | 2.6 px | 0.35 | 1.73 | 5 |
| stroke 35 | 7 % → 14 % | 5.0 px | 0.35 | 2.09 | 6 |
| stroke 36 | 5 % → 5 % | 3.7 px | 0.35 | 1.01 | 10 |
| stroke 37 | 7 % → 15 % | 5.2 px | 0.35 | 2.15 | 5 |
| stroke 38 | 8 % → 13 % | 5.8 px | 0.35 | 1.66 | 6 |
| stroke 39 | 7 % → 11 % | 5.1 px | 0.35 | 1.67 | 5 |
| stroke 40 | 8 % → 18 % | 6.2 px | 0.35 | 2.21 | 6 |
| stroke 41 | 9 % → 13 % | 6.9 px | 0.35 | 1.48 | 5 |
| stroke 42 | 10 % → 17 % | 7.7 px | 0.35 | 1.73 | 7 |
| stroke 43 | 5 % → 9 % | 3.9 px | 0.35 | 1.66 | 5 |
| stroke 44 | 10 % → 13 % | 7.3 px | 0.35 | 1.40 | 5 |
| stroke 45 | 13 % → 18 % | 9.9 px | 0.35 | 1.35 | 10 |
| stroke 46 | 5 % → 7 % | 3.6 px | 0.34 | 1.41 | 4 |
| stroke 47 | 11 % → 13 % | 8.0 px | 0.35 | 1.20 | 6 |
| stroke 48 | 12 % → 16 % | 9.2 px | 0.35 | 1.34 | 5 |
| stroke 49 | 6 % → 9 % | 4.2 px | 0.35 | 1.66 | 8 |
| stroke 50 | 7 % → 7 % | 5.2 px | 0.34 | 1.00 | 4 |
| stroke 51 | 8 % → 15 % | 6.4 px | 0.35 | 1.74 | 5 |
| stroke 52 | 12 % → 14 % | 9.1 px | 0.35 | 1.19 | 5 |
| stroke 53 | 11 % → 14 % | 8.1 px | 0.35 | 1.36 | 5 |
| stroke 54 | 10 % → 14 % | 7.4 px | 0.35 | 1.47 | 5 |
| stroke 55 | 11 % → 14 % | 8.2 px | 0.35 | 1.33 | 5 |
| stroke 56 | 11 % → 12 % | 8.4 px | 0.35 | 1.11 | 4 |
| stroke 57 | 9 % → 13 % | 7.1 px | 0.35 | 1.37 | 5 |
| stroke 58 | 10 % → 11 % | 7.7 px | 0.35 | 1.14 | 8 |
| stroke 59 | 11 % → 13 % | 8.4 px | 0.35 | 1.18 | 10 |
| stroke 60 | 16 % → 20 % | 11.9 px | 0.35 | 1.26 | 5 |
| stroke 61 | 19 % → 20 % | 14.5 px | 0.35 | 1.04 | 10 |
| stroke 62 | 10 % → 10 % | 7.3 px | 0.35 | 1.00 | 5 |
| stroke 63 | 11 % → 12 % | 8.7 px | 0.35 | 1.07 | 5 |
| stroke 64 | 14 % → 14 % | 10.7 px | 0.35 | 1.02 | 9 |
| stroke 65 | 15 % → 15 % | 11.5 px | 0.35 | 1.00 | 4 |
| stroke 66 | 14 % → 14 % | 10.7 px | 0.35 | 1.00 | 7 |
| stroke 67 | 12 % → 12 % | 8.8 px | 0.35 | 1.06 | 9 |
| stroke 68 | 5 % → 9 % | 3.6 px | 0.35 | 1.88 | 4 |
| stroke 69 | 5 % → 5 % | 4.1 px | 0.35 | 1.00 | 5 |
| stroke 70 | 10 % → 13 % | 7.4 px | 0.35 | 1.28 | 4 |
| stroke 71 | 9 % → 11 % | 7.1 px | 0.35 | 1.15 | 7 |
| stroke 72 | 5 % → 7 % | 4.2 px | 0.35 | 1.23 | 8 |
| stroke 73 | 12 % → 12 % | 9.3 px | 0.35 | 1.00 | 5 |
| stroke 74 | 14 % → 14 % | 10.8 px | 0.35 | 1.00 | 10 |
| stroke 75 | 15 % → 15 % | 11.4 px | 0.35 | 1.00 | 7 |
| stroke 76 | 14 % → 14 % | 10.5 px | 0.35 | 1.00 | 5 |
| stroke 77 | 7 % → 10 % | 5.4 px | 0.35 | 1.34 | 4 |
| stroke 78 | 9 % → 9 % | 7.0 px | 0.35 | 1.00 | 5 |
| stroke 79 | 7 % → 7 % | 5.7 px | 0.35 | 1.00 | 6 |
| stroke 80 | 11 % → 11 % | 8.3 px | 0.35 | 1.00 | 9 |

Numbers say: wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #42 Oil pastel shaggy — own sheet
own sheet 600 × 600 · Pastel · 18 px · 3.7 s

![Brush Artist · Refs · #42 Oil pastel shaggy — own sheet](Brush-Artist-Refs-42-Oil-pastel-shaggy-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 5 % → 27 % | 8.0 px | 0.28 | 5.73 | 14 |
| stroke 2 | 5 % → 24 % | 8.6 px | 0.28 | 4.69 | 16 |
| stroke 3 | 5 % → 29 % | 8.9 px | 0.28 | 5.42 | 15 |
| stroke 4 | 5 % → 11 % | 8.8 px | 0.28 | 2.08 | 16 |
| stroke 5 | 6 % → 11 % | 9.9 px | 0.28 | 1.85 | 11 |
| stroke 6 | 8 % → 37 % | 13.9 px | 0.29 | 4.44 | 13 |
| stroke 7 | 11 % → 31 % | 17.6 px | 0.28 | 2.90 | 11 |
| stroke 8 | 7 % → 38 % | 11.4 px | 0.28 | 5.55 | 13 |
| stroke 9 | 8 % → 21 % | 13.9 px | 0.28 | 2.53 | 10 |
| stroke 10 | 8 % → 18 % | 13.2 px | 0.28 | 2.32 | 13 |
| stroke 11 | 6 % → 27 % | 9.4 px | 0.28 | 4.74 | 14 |
| stroke 12 | 8 % → 19 % | 13.6 px | 0.28 | 2.29 | 18 |
| stroke 13 | 13 % → 24 % | 21.0 px | 0.28 | 1.92 | 16 |
| stroke 14 | 5 % → 23 % | 7.9 px | 0.28 | 4.77 | 11 |
| stroke 15 | 5 % → 24 % | 9.0 px | 0.29 | 4.38 | 11 |
| stroke 16 | 9 % → 21 % | 15.7 px | 0.29 | 2.18 | 20 |
| stroke 17 | 17 % → 39 % | 27.9 px | 0.29 | 2.34 | 11 |
| stroke 18 | 14 % → 25 % | 22.8 px | 0.29 | 1.79 | 15 |
| stroke 19 | 15 % → 32 % | 24.9 px | 0.28 | 2.09 | 10 |
| stroke 20 | 21 % → 39 % | 35.1 px | 0.28 | 1.85 | 16 |
| stroke 21 | 9 % → 16 % | 14.4 px | 0.28 | 1.88 | 12 |
| stroke 22 | 14 % → 17 % | 23.9 px | 0.28 | 1.20 | 11 |
| stroke 23 | 12 % → 17 % | 20.6 px | 0.29 | 1.34 | 14 |
| stroke 24 | 18 % → 26 % | 30.0 px | 0.29 | 1.44 | 13 |
| stroke 25 | 20 % → 34 % | 32.6 px | 0.28 | 1.74 | 19 |
| stroke 26 | 6 % → 14 % | 9.2 px | 0.28 | 2.43 | 15 |
| stroke 27 | 18 % → 26 % | 30.4 px | 0.29 | 1.41 | 10 |
| stroke 28 | 14 % → 24 % | 23.7 px | 0.28 | 1.68 | 17 |
| stroke 29 | 9 % → 27 % | 14.9 px | 0.29 | 3.01 | 13 |
| stroke 30 | 15 % → 36 % | 24.9 px | 0.29 | 2.43 | 17 |
| stroke 31 | 14 % → 17 % | 23.3 px | 0.28 | 1.23 | 11 |
| stroke 32 | 16 % → 29 % | 27.0 px | 0.29 | 1.82 | 13 |
| stroke 33 | 15 % → 16 % | 24.5 px | 0.29 | 1.09 | 14 |
| stroke 34 | 19 % → 27 % | 31.4 px | 0.28 | 1.44 | 16 |
| stroke 35 | 26 % → 36 % | 42.5 px | 0.28 | 1.40 | 12 |
| stroke 36 | 25 % → 34 % | 41.0 px | 0.28 | 1.36 | 10 |
| stroke 37 | 12 % → 12 % | 19.3 px | 0.28 | 1.03 | 11 |
| stroke 38 | 19 % → 25 % | 31.7 px | 0.28 | 1.30 | 10 |
| stroke 39 | 16 % → 22 % | 27.3 px | 0.28 | 1.37 | 19 |
| stroke 40 | 22 % → 31 % | 36.6 px | 0.28 | 1.38 | 10 |
| stroke 41 | 32 % → 36 % | 53.1 px | 0.28 | 1.12 | 12 |
| stroke 42 | 23 % → 30 % | 38.1 px | 0.29 | 1.29 | 11 |
| stroke 43 | 12 % → 12 % | 20.3 px | 0.28 | 1.00 | 16 |
| stroke 44 | 30 % → 37 % | 48.9 px | 0.28 | 1.26 | 13 |
| stroke 45 | 16 % → 16 % | 26.2 px | 0.28 | 1.00 | 11 |
| stroke 46 | 29 % → 34 % | 47.9 px | 0.29 | 1.15 | 20 |
| stroke 47 | 38 % → 41 % | 62.0 px | 0.28 | 1.10 | 12 |
| stroke 48 | 29 % → 36 % | 47.8 px | 0.29 | 1.27 | 10 |
| stroke 49 | 27 % → 30 % | 45.1 px | 0.29 | 1.11 | 11 |
| stroke 50 | 38 % → 40 % | 63.4 px | 0.28 | 1.06 | 11 |
| stroke 51 | 16 % → 16 % | 26.0 px | 0.28 | 1.00 | 16 |
| stroke 52 | 37 % → 38 % | 62.4 px | 0.29 | 1.01 | 15 |
| stroke 53 | 22 % → 26 % | 36.9 px | 0.28 | 1.18 | 12 |
| stroke 54 | 17 % → 19 % | 29.0 px | 0.29 | 1.09 | 11 |
| stroke 55 | 15 % → 15 % | 25.0 px | 0.28 | 1.00 | 21 |
| stroke 56 | 13 % → 14 % | 21.6 px | 0.28 | 1.08 | 16 |
| stroke 57 | 23 % → 23 % | 37.7 px | 0.29 | 1.00 | 14 |
| stroke 58 | 28 % → 29 % | 46.1 px | 0.28 | 1.05 | 16 |
| stroke 59 | 40 % → 40 % | 67.3 px | 0.28 | 1.00 | 17 |
| stroke 60 | 22 % → 22 % | 35.6 px | 0.28 | 1.00 | 15 |

Numbers say: wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #43 Dragged black ink blocks — own sheet
own sheet 600 × 600 · Gouache · 70 px · 12.5 s

![Brush Artist · Refs · #43 Dragged black ink blocks — own sheet](Brush-Artist-Refs-43-Dragged-black-ink-blocks-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 29 % → 29 % | 66.4 px | 0.42 | 1.00 | 580 |
| stroke 2 | 30 % → 31 % | 105.8 px | 0.42 | 1.02 | 641 |
| stroke 3 | 37 % → 36 % | 132.0 px | 0.42 | 0.99 | 569 |
| stroke 4 | 37 % → 34 % | 128.9 px | 0.42 | 0.93 | 593 |
| stroke 5 | 44 % → 30 % | 103.8 px | 0.42 | 0.66 | 636 |

## Brush Artist · Refs · #44 Blue looping ribbon — own sheet
own sheet 600 × 600 · Oil · 80 px · 6.8 s

![Brush Artist · Refs · #44 Blue looping ribbon — own sheet](Brush-Artist-Refs-44-Blue-looping-ribbon-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 32 % → 32 % | 42.2 px | 0.78 | 1.00 | 3479 |

## Brush Artist · Refs · #45 Soft pastel pepper — own sheet
own sheet 600 × 600 · Pastel · 40 px · 6.1 s

![Brush Artist · Refs · #45 Soft pastel pepper — own sheet](Brush-Artist-Refs-45-Soft-pastel-pepper-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 10 % → 40 % | 11.3 px | 0.49 | 3.87 | 474 |
| stroke 2 | 18 % → 34 % | 21.3 px | 0.49 | 1.90 | 430 |
| stroke 3 | 25 % → 38 % | 17.6 px | 0.49 | 1.48 | 417 |
| stroke 4 | 24 % → 36 % | 30.5 px | 0.49 | 1.46 | 452 |
| stroke 5 | 30 % → 30 % | 21.2 px | 0.49 | 1.00 | 298 |
| stroke 6 | 39 % → 46 % | 24.6 px | 0.49 | 1.20 | 383 |
| stroke 7 | 41 % → 45 % | 22.6 px | 0.49 | 1.11 | 451 |
| stroke 8 | 45 % → 45 % | 45.8 px | 0.49 | 1.00 | 404 |

Numbers say: wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #46 Red-brown ink lips — own sheet
own sheet 600 × 600 · Watercolor · 50 px · 7.6 s

![Brush Artist · Refs · #46 Red-brown ink lips — own sheet](Brush-Artist-Refs-46-Red-brown-ink-lips-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 12 % → 23 % | 51.9 px | 0.60 | 1.87 | 173 |
| stroke 2 | 16 % → 26 % | 68.2 px | 0.55 | 1.67 | 190 |

Numbers say: wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #47 Pink knife slabs — own sheet
own sheet 600 × 600 · Heavy acrylic · 90 px · 6.7 s

![Brush Artist · Refs · #47 Pink knife slabs — own sheet](Brush-Artist-Refs-47-Pink-knife-slabs-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 17 % → 32 % | 83.2 px | 0.11 | 1.94 | 508 |
| stroke 2 | 29 % → 43 % | 165.7 px | 0.11 | 1.46 | 546 |
| stroke 3 | 29 % → 43 % | 165.6 px | 0.11 | 1.47 | 492 |
| stroke 4 | 39 % → 38 % | 165.6 px | 0.11 | 0.98 | 403 |

Numbers say: wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #48 Black bands with drips — own sheet
own sheet 600 × 600 · Gouache · 70 px · 15.3 s

![Brush Artist · Refs · #48 Black bands with drips — own sheet](Brush-Artist-Refs-48-Black-bands-with-drips-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 23 % → 36 % | 58.8 px | 0.39 | 1.58 | 650 |
| stroke 2 | 34 % → 47 % | 108.3 px | 0.39 | 1.41 | 661 |
| stroke 3 | 36 % → 48 % | 112.5 px | 0.39 | 1.34 | 640 |
| stroke 4 | 38 % → 36 % | 111.4 px | 0.39 | 0.95 | 654 |

Numbers say: wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #49 Magenta letters round brush — own sheet
own sheet 600 × 600 · Ink · 30 px · 14.6 s

![Brush Artist · Refs · #49 Magenta letters round brush — own sheet](Brush-Artist-Refs-49-Magenta-letters-round-brush-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 27 % → 46 % | 64.3 px | 0.52 | 1.69 | 43 |
| stroke 2 | 29 % → 40 % | 52.5 px | 0.53 | 1.39 | 46 |
| stroke 3 | 41 % → 67 % | 96.4 px | 0.52 | 1.64 | 45 |
| stroke 4 | 34 % → 52 % | 53.7 px | 0.52 | 1.55 | 151 |
| stroke 5 | 40 % → 66 % | 94.7 px | 0.52 | 1.65 | 102 |
| stroke 6 | 54 % → 70 % | 231.1 px | 0.52 | 1.29 | 23 |
| stroke 7 | 41 % → 56 % | 63.9 px | 0.52 | 1.35 | 173 |
| stroke 8 | 36 % → 61 % | 91.9 px | 0.53 | 1.72 | 94 |
| stroke 9 | 49 % → 60 % | 152.9 px | 0.53 | 1.24 | 47 |
| stroke 10 | 42 % → 72 % | 100.4 px | 0.52 | 1.71 | 84 |
| stroke 11 | 52 % → 72 % | 219.5 px | 0.52 | 1.39 | 17 |
| stroke 12 | 53 % → 68 % | 82.2 px | 0.52 | 1.29 | 162 |
| stroke 13 | 42 % → 54 % | 116.0 px | 0.53 | 1.29 | 59 |
| stroke 14 | 45 % → 69 % | 131.9 px | 0.53 | 1.52 | 48 |
| stroke 15 | 43 % → 63 % | 102.4 px | 0.52 | 1.46 | 120 |
| stroke 16 | 52 % → 61 % | 220.2 px | 0.52 | 1.18 | 35 |
| stroke 17 | 53 % → 64 % | 82.2 px | 0.52 | 1.19 | 156 |
| stroke 18 | 36 % → 44 % | 99.6 px | 0.52 | 1.21 | 56 |
| stroke 19 | 54 % → 53 % | 123.8 px | 0.52 | 0.99 | 43 |
| stroke 20 | 54 % → 54 % | 125.3 px | 0.52 | 1.00 | 51 |
| stroke 21 | 49 % → 49 % | 81.3 px | 0.52 | 1.00 | 99 |

Numbers say: wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #50 Thick swipes on photo — own sheet
own sheet 600 × 600 · Heavy acrylic · 40 px · 4.1 s

![Brush Artist · Refs · #50 Thick swipes on photo — own sheet](Brush-Artist-Refs-50-Thick-swipes-on-photo-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 9 % → 21 % | 42.6 px | 0.33 | 2.35 | 45 |
| stroke 2 | 9 % → 16 % | 42.4 px | 0.33 | 1.79 | 36 |
| stroke 3 | 10 % → 11 % | 41.8 px | 0.33 | 1.06 | 57 |
| stroke 4 | 11 % → 18 % | 42.6 px | 0.33 | 1.64 | 43 |
| stroke 5 | 11 % → 10 % | 41.8 px | 0.33 | 0.95 | 56 |
| stroke 6 | 17 % → 21 % | 97.3 px | 0.32 | 1.20 | 31 |
| stroke 7 | 22 % → 26 % | 92.7 px | 0.33 | 1.18 | 77 |
| stroke 8 | 21 % → 21 % | 119.6 px | 0.33 | 0.97 | 40 |
| stroke 9 | 9 % → 10 % | 42.0 px | 0.32 | 1.09 | 59 |
| stroke 10 | 22 % → 21 % | 73.6 px | 0.32 | 0.96 | 56 |
| stroke 11 | 9 % → 8 % | 42.6 px | 0.33 | 0.95 | 44 |
| stroke 12 | 17 % → 16 % | 93.0 px | 0.33 | 0.96 | 25 |

Numbers say: wet paint spreads well beyond the stroke.

## Brush Artist · Ink — dry brush — own sheet
own sheet 600 × 600 · Gouache · 30 px · 5.1 s

![Brush Artist · Ink — dry brush — own sheet](Brush-Artist-Ink-dry-brush-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| ear | 13 % → 4 % | 16.7 px | 0.82 | 0.32 | 930 |
| drag0 | 14 % → 16 % | 25.0 px | 0.82 | 1.22 | 225 |
| drag1 | 17 % → 18 % | 35.3 px | 0.82 | 1.02 | 166 |
| drag2 | 20 % → 18 % | 45.7 px | 0.82 | 0.91 | 157 |
| drag3 | 22 % → 19 % | 56.9 px | 0.82 | 0.84 | 168 |

## Brush Artist · Watercolour — blue — own sheet
own sheet 600 × 600 · Watercolor · 40 px · 16.8 s

![Brush Artist · Watercolour — blue — own sheet](Brush-Artist-Watercolour-blue-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| s0 | 7 % → 23 % | 28.4 px | 0.25 | 3.20 | 60 |
| s1 | 5 % → 32 % | 9.9 px | 0.38 | 5.84 | 67 |
| s2 | 10 % → 18 % | 43.5 px | 0.19 | 1.75 | 60 |
| s3 | 9 % → 17 % | 26.3 px | 0.28 | 1.85 | 76 |
| s4 | 14 % → 29 % | 37.9 px | 0.36 | 2.11 | 85 |
| s5 | 19 % → 29 % | 38.9 px | 0.37 | 1.51 | 67 |
| s6 | 17 % → 21 % | 47.6 px | 0.27 | 1.22 | 115 |
| s7 | 24 % → 35 % | 31.9 px | 0.37 | 1.44 | 77 |
| s8 | 20 % → 23 % | 77.5 px | 0.27 | 1.18 | 79 |

Numbers say: wet paint spreads well beyond the stroke.

## Brush Artist · Charcoal — stick — own sheet
own sheet 600 × 600 · Charcoal · 28 px · 1.8 s

![Brush Artist · Charcoal — stick — own sheet](Brush-Artist-Charcoal-stick-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| finger0 | 9 % → 18 % | 15.5 px | 0.83 | 2.01 | 59 |
| tip0 | 8 % → 14 % | 22.1 px | 0.83 | 1.75 | 15 |
| finger1 | 17 % → 29 % | 29.4 px | 0.83 | 1.74 | 38 |
| tip1 | 15 % → 21 % | 39.1 px | 0.83 | 1.42 | 16 |
| finger2 | 17 % → 25 % | 29.5 px | 0.83 | 1.53 | 46 |
| tip2 | 14 % → 20 % | 39.0 px | 0.83 | 1.41 | 16 |
| finger3 | 16 % → 19 % | 29.3 px | 0.83 | 1.16 | 51 |
| tip3 | 15 % → 15 % | 39.0 px | 0.83 | 1.00 | 18 |
| cig0 | 25 % → 35 % | 54.8 px | 0.83 | 1.41 | 12 |
| cig1 | 26 % → 35 % | 58.8 px | 0.83 | 1.32 | 12 |
| cig2 | 28 % → 35 % | 63.2 px | 0.83 | 1.22 | 14 |
| cig3 | 30 % → 34 % | 67.3 px | 0.83 | 1.14 | 20 |
| cig4 | 32 % → 34 % | 71.5 px | 0.83 | 1.06 | 17 |
| cig5 | 34 % → 34 % | 75.3 px | 0.83 | 1.00 | 11 |

Numbers say: wet paint spreads well beyond the stroke.

