![All brushes](contact.png)

# Brush Lab — 150 brushes · Nov 4, 2026 at 6:05 PM

Every sheet: 1500 × 600, ten strokes in a 5 × 2 grid — 1. light line · 2. heavy line · 3. pressure swell · 4. fast wave · 5. slow wave · 6. spiral · 7. loop · 8. tilted · 9. over the wet one · 10. long, no reload (cell 8 holds «tilted» and «over the wet one» crossed). The CPU reference of Mamay's paint engine; the wet layer settles 20 s at the end.

Columns: **covered** = share of the cell with paint right after the stroke → after settling; **width** = painted area of the stroke ÷ its length (px); **dark** = mean darkness of the painted pixels above the paper's own grain (0 = paper, 1 = black); **spread** = how far wet paint went beyond the stroke (1.0 = stayed); **ms** = the stroke on the CPU; long stroke: paint in each quarter of its length (it should run out: wet → streaks → dry tail).

## Ink Line
Ink · 12 px · 28.0 s

![Ink Line](Ink-Line.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 1 % → 4 % | 4.3 px | 0.55 | 2.45 | 75 |
| heavy line | 5 % → 6 % | 15.7 px | 0.68 | 1.14 | 79 |
| pressure swell | 3 % → 4 % | 11.3 px | 0.64 | 1.40 | 43 |
| fast wave | 10 % → 11 % | 11.2 px | 0.59 | 1.11 | 132 |
| slow wave | 8 % → 10 % | 9.6 px | 0.57 | 1.16 | 117 |
| spiral | 14 % → 15 % | 8.9 px | 0.49 | 1.07 | 214 |
| loop | 8 % → 9 % | 10.6 px | 0.61 | 1.15 | 201 |
| tilted | 5 % → 5 % | 14.3 px | 0.64 | 1.05 | 82 |
| over the wet one | 10 % → 11 % | 12.5 px | 0.64 | 1.15 | 77 |
| long, no reload | 18 % → 17 % | 8.1 px | 0.47 | 0.96 | 945 | quarters: 0.22 → 0.09 → 0.04 → 0.02

Numbers say: light vs heavy: width 4.3 → 15.7 px, dark 0.55 → 0.68; wet paint spreads well beyond the stroke.

## Dense Ink
Ink · 14 px · 28.6 s

![Dense Ink](Dense-Ink.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 5 % → 7 % | 15.2 px | 0.72 | 1.27 | 87 |
| heavy line | 7 % → 7 % | 19.1 px | 0.73 | 1.09 | 85 |
| pressure swell | 5 % → 6 % | 17.9 px | 0.72 | 1.18 | 48 |
| fast wave | 13 % → 13 % | 15.2 px | 0.69 | 1.01 | 141 |
| slow wave | 12 % → 12 % | 13.5 px | 0.67 | 1.04 | 150 |
| spiral | 18 % → 15 % | 12.2 px | 0.65 | 0.80 | 242 |
| loop | 11 % → 12 % | 14.8 px | 0.69 | 1.08 | 131 |
| tilted | 5 % → 6 % | 14.5 px | 0.72 | 1.07 | 107 |
| over the wet one | 12 % → 13 % | 17.7 px | 0.72 | 1.12 | 92 |
| long, no reload | 23 % → 15 % | 10.1 px | 0.64 | 0.66 | 1208 | quarters: 0.30 → 0.12 → 0.04 → 0.02

Numbers say: light vs heavy: width 15.2 → 19.1 px, dark 0.72 → 0.73.

## Transparent Wash
Watercolor · 22 px · 29.1 s

![Transparent Wash](Transparent-Wash.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 2 % → 5 % | 6.9 px | 0.27 | 2.26 | 68 |
| heavy line | 7 % → 9 % | 20.4 px | 0.27 | 1.23 | 70 |
| pressure swell | 4 % → 6 % | 15.2 px | 0.28 | 1.54 | 36 |
| fast wave | 14 % → 16 % | 16.1 px | 0.20 | 1.17 | 117 |
| slow wave | 12 % → 15 % | 13.7 px | 0.21 | 1.28 | 176 |
| spiral | 18 % → 22 % | 11.9 px | 0.16 | 1.22 | 181 |
| loop | 11 % → 13 % | 14.5 px | 0.22 | 1.20 | 207 |
| tilted | 8 % → 8 % | 21.1 px | 0.24 | 1.06 | 111 |
| over the wet one | 13 % → 16 % | 16.4 px | 0.24 | 1.19 | 89 |
| long, no reload | 26 % → 32 % | 11.6 px | 0.13 | 1.22 | 944 | quarters: 0.11 → 0.04 → 0.02 → 0.01

Numbers say: light vs heavy: width 6.9 → 20.4 px, dark 0.27 → 0.27; wet paint spreads well beyond the stroke.

## Dry Brush
Gouache · 24 px · 24.6 s

![Dry Brush](Dry-Brush.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 5 % → 1 % | 13.8 px | 0.65 | 0.11 | 47 |
| heavy line | 6 % → 0 % | 18.4 px | 0.65 | 0.02 | 90 |
| pressure swell | 5 % → 0 % | 18.1 px | 0.65 | 0.09 | 53 |
| fast wave | 6 % → 1 % | 6.9 px | 0.65 | 0.08 | 186 |
| slow wave | 7 % → 0 % | 7.8 px | 0.65 | 0.07 | 261 |
| spiral | 7 % → 1 % | 4.4 px | 0.65 | 0.08 | 273 |
| loop | 9 % → 0 % | 12.2 px | 0.65 | 0.05 | 155 |
| tilted | 4 % → 3 % | 10.3 px | 0.65 | 0.89 | 119 |
| over the wet one | 9 % → 1 % | 14.3 px | 0.65 | 0.12 | 85 |
| long, no reload | 6 % → 1 % | 2.7 px | 0.65 | 0.15 | 364 | quarters: 0.12 → 0.00 → 0.00 → 0.00

Numbers say: light vs heavy: width 13.8 → 18.4 px, dark 0.65 → 0.65.

## Wax Crayon
Wax · 8 px · 10.2 s

![Wax Crayon](Wax-Crayon.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 1 % → 1 % | 2.5 px | 0.71 | 1.00 | 17 |
| heavy line | 1 % → 1 % | 3.9 px | 0.69 | 1.00 | 18 |
| pressure swell | 1 % → 1 % | 3.3 px | 0.70 | 1.00 | 14 |
| fast wave | 3 % → 3 % | 3.5 px | 0.69 | 1.00 | 42 |
| slow wave | 3 % → 3 % | 3.4 px | 0.70 | 1.00 | 40 |
| spiral | 5 % → 5 % | 3.3 px | 0.70 | 1.00 | 79 |
| loop | 3 % → 3 % | 3.3 px | 0.70 | 1.00 | 78 |
| tilted | 2 % → 2 % | 5.6 px | 0.68 | 1.00 | 46 |
| over the wet one | 3 % → 3 % | 3.6 px | 0.68 | 1.00 | 27 |
| long, no reload | 7 % → 7 % | 3.3 px | 0.70 | 1.00 | 108 | quarters: 0.06 → 0.06 → 0.06 → 0.06

Numbers say: light vs heavy: width 2.5 → 3.9 px, dark 0.71 → 0.69; the long stroke does not run out of paint.

## Oil Pastel
Wax · 12 px · 10.5 s

![Oil Pastel](Oil-Pastel.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 1 % → 1 % | 4.0 px | 0.68 | 1.00 | 21 |
| heavy line | 2 % → 2 % | 6.5 px | 0.68 | 1.00 | 29 |
| pressure swell | 2 % → 2 % | 5.7 px | 0.69 | 1.00 | 18 |
| fast wave | 5 % → 5 % | 5.7 px | 0.68 | 1.00 | 61 |
| slow wave | 5 % → 5 % | 5.5 px | 0.68 | 1.00 | 75 |
| spiral | 8 % → 8 % | 5.5 px | 0.68 | 1.00 | 151 |
| loop | 4 % → 4 % | 5.6 px | 0.68 | 1.00 | 61 |
| tilted | 2 % → 2 % | 6.8 px | 0.68 | 1.00 | 42 |
| over the wet one | 5 % → 5 % | 5.8 px | 0.68 | 1.00 | 27 |
| long, no reload | 13 % → 13 % | 5.6 px | 0.68 | 1.00 | 161 | quarters: 0.10 → 0.09 → 0.10 → 0.10

Numbers say: light vs heavy: width 4.0 → 6.5 px, dark 0.68 → 0.68; the long stroke does not run out of paint.

## Charcoal
Charcoal · 5 px · 10.8 s

![Charcoal](Charcoal.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 1 % → 1 % | 2.0 px | 0.74 | 1.00 | 15 |
| heavy line | 1 % → 1 % | 3.0 px | 0.74 | 1.00 | 12 |
| pressure swell | 1 % → 1 % | 2.7 px | 0.74 | 1.00 | 10 |
| fast wave | 2 % → 2 % | 2.7 px | 0.73 | 1.00 | 36 |
| slow wave | 2 % → 2 % | 2.6 px | 0.74 | 1.00 | 31 |
| spiral | 4 % → 4 % | 2.5 px | 0.74 | 1.00 | 68 |
| loop | 2 % → 2 % | 2.6 px | 0.74 | 1.00 | 33 |
| tilted | 2 % → 2 % | 4.3 px | 0.72 | 1.00 | 19 |
| over the wet one | 2 % → 2 % | 2.4 px | 0.72 | 1.00 | 12 |
| long, no reload | 6 % → 6 % | 2.7 px | 0.73 | 1.00 | 85 | quarters: 0.05 → 0.05 → 0.05 → 0.05

Numbers say: light vs heavy: width 2.0 → 3.0 px, dark 0.74 → 0.74; the long stroke does not run out of paint.

## Impasto
Heavy acrylic · 22 px · 16.2 s

![Impasto](Impasto.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 8 % → 8 % | 24.1 px | 0.71 | 0.93 | 58 |
| heavy line | 10 % → 9 % | 28.8 px | 0.69 | 0.94 | 113 |
| pressure swell | 7 % → 7 % | 28.1 px | 0.72 | 0.94 | 56 |
| fast wave | 20 % → 13 % | 23.4 px | 0.71 | 0.64 | 184 |
| slow wave | 21 % → 14 % | 24.5 px | 0.71 | 0.66 | 326 |
| spiral | 30 % → 14 % | 19.9 px | 0.71 | 0.46 | 304 |
| loop | 18 % → 14 % | 23.9 px | 0.71 | 0.77 | 211 |
| tilted | 8 % → 8 % | 21.7 px | 0.70 | 1.00 | 86 |
| over the wet one | 17 % → 15 % | 25.4 px | 0.70 | 0.91 | 74 |
| long, no reload | 33 % → 14 % | 14.9 px | 0.71 | 0.42 | 565 | quarters: 0.38 → 0.21 → 0.10 → 0.03

Numbers say: light vs heavy: width 24.1 → 28.8 px, dark 0.71 → 0.69.

## Oil Round
Oil · 18 px · 17.5 s

![Oil Round](Oil-Round.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 2 % → 2 % | 7.2 px | 0.75 | 1.00 | 56 |
| heavy line | 7 % → 7 % | 19.3 px | 0.73 | 1.00 | 74 |
| pressure swell | 4 % → 4 % | 13.7 px | 0.72 | 1.00 | 44 |
| fast wave | 11 % → 11 % | 12.8 px | 0.65 | 1.00 | 157 |
| slow wave | 8 % → 8 % | 9.0 px | 0.57 | 1.00 | 174 |
| spiral | 10 % → 10 % | 6.6 px | 0.50 | 1.00 | 225 |
| loop | 6 % → 6 % | 7.2 px | 0.45 | 1.00 | 122 |
| tilted | 4 % → 4 % | 10.1 px | 0.52 | 1.00 | 66 |
| over the wet one | 6 % → 6 % | 7.6 px | 0.52 | 1.00 | 58 |
| long, no reload | 15 % → 15 % | 6.9 px | 0.42 | 1.00 | 347 | quarters: 0.09 → 0.08 → 0.07 → 0.06

Numbers say: light vs heavy: width 7.2 → 19.3 px, dark 0.75 → 0.73.

## Palette Knife
Oil · 20 px · 17.3 s

![Palette Knife](Palette-Knife.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 8 % → 8 % | 21.9 px | 0.67 | 1.00 | 19 |
| heavy line | 8 % → 8 % | 22.5 px | 0.73 | 1.00 | 14 |
| pressure swell | 6 % → 6 % | 22.3 px | 0.74 | 1.00 | 7 |
| fast wave | 16 % → 16 % | 18.9 px | 0.50 | 1.00 | 26 |
| slow wave | 17 % → 17 % | 19.9 px | 0.43 | 1.00 | 38 |
| spiral | 17 % → 17 % | 11.3 px | 0.46 | 1.00 | 44 |
| loop | 16 % → 16 % | 21.0 px | 0.59 | 1.00 | 23 |
| tilted | 5 % → 5 % | 15.0 px | 0.72 | 1.00 | 11 |
| over the wet one | 13 % → 13 % | 21.0 px | 0.72 | 1.00 | 11 |
| long, no reload | 16 % → 16 % | 7.2 px | 0.49 | 1.00 | 81 | quarters: 0.29 → 0.05 → 0.00 → 0.00

Numbers say: light vs heavy: width 21.9 → 22.5 px, dark 0.67 → 0.73; pressure barely changes the width.

## Water
Watercolor · 20 px · 36.2 s · over bands of wet oil paint and oil pastel in turn (it works on paint already there: look at what it does to the bands; covered counts the bands too)

![Water](Water.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 25 % → 27 % | 73.8 px | 0.80 | 1.06 | 26 |
| heavy line | 24 % → 25 % | 69.8 px | 0.81 | 1.04 | 68 |
| pressure swell | 24 % → 25 % | 89.6 px | 0.81 | 1.03 | 35 |
| fast wave | 24 % → 26 % | 27.7 px | 0.81 | 1.07 | 111 |
| slow wave | 24 % → 25 % | 27.8 px | 0.81 | 1.06 | 157 |
| spiral | 24 % → 26 % | 15.9 px | 0.81 | 1.07 | 174 |
| loop | 24 % → 25 % | 31.1 px | 0.81 | 1.03 | 94 |
| tilted | 24 % → 24 % | 67.0 px | 0.81 | 1.00 | 61 |
| over the wet one | 24 % → 25 % | 0.0 px | 0.81 | 1.06 | 47 |
| long, no reload | 24 % → 26 % | 10.7 px | 0.81 | 1.08 | 277 | quarters: 0.21 → 0.27 → 0.18 → 0.27

Numbers say: light vs heavy: width 73.8 → 69.8 px, dark 0.80 → 0.81; pressure barely changes the width; the long stroke does not run out of paint.

## Blender
Pastel · 16 px · 21.5 s · over bands of wet oil paint and oil pastel in turn (it works on paint already there: look at what it does to the bands; covered counts the bands too)

![Blender](Blender.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 24 % → 24 % | 70.7 px | 0.81 | 1.00 | 27 |
| heavy line | 25 % → 25 % | 72.1 px | 0.80 | 1.00 | 38 |
| pressure swell | 24 % → 24 % | 91.3 px | 0.81 | 1.00 | 22 |
| fast wave | 26 % → 26 % | 30.0 px | 0.79 | 1.00 | 80 |
| slow wave | 26 % → 26 % | 29.9 px | 0.79 | 1.00 | 90 |
| spiral | 28 % → 28 % | 18.7 px | 0.77 | 1.00 | 122 |
| loop | 25 % → 25 % | 33.0 px | 0.80 | 1.00 | 67 |
| tilted | 25 % → 25 % | 70.1 px | 0.79 | 1.00 | 43 |
| over the wet one | 26 % → 26 % | 1.8 px | 0.79 | 1.00 | 32 |
| long, no reload | 30 % → 30 % | 13.7 px | 0.76 | 1.00 | 271 | quarters: 0.20 → 0.28 → 0.23 → 0.30

Numbers say: light vs heavy: width 70.7 → 72.1 px, dark 0.81 → 0.80; pressure barely changes the width; the long stroke does not run out of paint.

## Eraser
Eraser · 16 px · 22.0 s · over bands of wet oil paint and oil pastel in turn (it works on paint already there: look at what it does to the bands; covered counts the bands too)

![Eraser](Eraser.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 24 % → 24 % | 69.6 px | 0.82 | 1.00 | 25 |
| heavy line | 23 % → 23 % | 67.9 px | 0.82 | 1.00 | 34 |
| pressure swell | 23 % → 23 % | 87.3 px | 0.82 | 1.00 | 24 |
| fast wave | 22 % → 22 % | 25.7 px | 0.82 | 1.00 | 80 |
| slow wave | 22 % → 22 % | 25.7 px | 0.82 | 1.00 | 123 |
| spiral | 22 % → 22 % | 14.4 px | 0.82 | 1.00 | 122 |
| loop | 22 % → 22 % | 28.6 px | 0.82 | 1.00 | 74 |
| tilted | 23 % → 23 % | 65.1 px | 0.82 | 1.00 | 43 |
| over the wet one | 23 % → 23 % | 0.0 px | 0.82 | 1.00 | 34 |
| long, no reload | 20 % → 20 % | 8.9 px | 0.82 | 1.00 | 208 | quarters: 0.15 → 0.20 → 0.15 → 0.20

Numbers say: light vs heavy: width 69.6 → 67.9 px, dark 0.82 → 0.82; pressure barely changes the width; the long stroke does not run out of paint.

## Fan
Gouache · 30 px · 29.8 s

![Fan](Fan.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 9 % → 3 % | 25.6 px | 0.63 | 0.37 | 34 |
| heavy line | 11 % → 4 % | 30.9 px | 0.63 | 0.39 | 52 |
| pressure swell | 8 % → 5 % | 31.7 px | 0.63 | 0.55 | 49 |
| fast wave | 17 % → 5 % | 20.2 px | 0.63 | 0.26 | 120 |
| slow wave | 18 % → 5 % | 21.0 px | 0.63 | 0.25 | 225 |
| spiral | 24 % → 5 % | 15.5 px | 0.63 | 0.19 | 215 |
| loop | 17 % → 5 % | 22.7 px | 0.63 | 0.28 | 107 |
| tilted | 5 % → 6 % | 15.0 px | 0.63 | 1.05 | 46 |
| over the wet one | 16 % → 8 % | 29.7 px | 0.63 | 0.49 | 47 |
| long, no reload | 22 % → 5 % | 9.9 px | 0.63 | 0.22 | 269 | quarters: 0.29 → 0.07 → 0.01 → 0.00

Numbers say: light vs heavy: width 25.6 → 30.9 px, dark 0.63 → 0.63.

## Sponge
Gouache · 30 px · 29.3 s

![Sponge](Sponge.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 4 % → 0 % | 11.3 px | 0.62 | 0.12 | 52 |
| heavy line | 12 % → 2 % | 35.4 px | 0.62 | 0.14 | 75 |
| pressure swell | 7 % → 2 % | 27.9 px | 0.62 | 0.28 | 62 |
| fast wave | 20 % → 4 % | 23.2 px | 0.62 | 0.19 | 154 |
| slow wave | 21 % → 4 % | 23.8 px | 0.62 | 0.18 | 235 |
| spiral | 28 % → 4 % | 18.3 px | 0.62 | 0.14 | 218 |
| loop | 18 % → 5 % | 23.0 px | 0.62 | 0.29 | 106 |
| tilted | 7 % → 7 % | 18.2 px | 0.62 | 1.04 | 120 |
| over the wet one | 16 % → 6 % | 27.8 px | 0.62 | 0.37 | 58 |
| long, no reload | 29 % → 5 % | 12.9 px | 0.62 | 0.17 | 295 | quarters: 0.29 → 0.13 → 0.07 → 0.04

Numbers say: light vs heavy: width 11.3 → 35.4 px, dark 0.62 → 0.62.

## Ink — sumi brush
Watercolour 1.00 · 22 px · 30.4 s

![Ink — sumi brush](Ink-sumi-brush.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 8 % → 9 % | 23.9 px | 0.87 | 1.12 | 67 |
| heavy line | 13 % → 13 % | 38.1 px | 0.86 | 1.00 | 83 |
| pressure swell | 9 % → 10 % | 34.5 px | 0.87 | 1.05 | 61 |
| fast wave | 28 % → 28 % | 32.5 px | 0.81 | 1.00 | 190 |
| slow wave | 26 % → 26 % | 29.6 px | 0.82 | 1.02 | 260 |
| spiral | 38 % → 37 % | 25.3 px | 0.74 | 0.96 | 304 |
| loop | 22 % → 22 % | 28.5 px | 0.85 | 1.02 | 152 |
| tilted | 9 % → 9 % | 25.3 px | 0.86 | 1.01 | 73 |
| over the wet one | 20 % → 21 % | 30.7 px | 0.86 | 1.03 | 71 |
| long, no reload | 45 % → 40 % | 20.1 px | 0.70 | 0.89 | 406 | quarters: 0.55 → 0.40 → 0.23 → 0.14

Numbers say: light vs heavy: width 23.9 → 38.1 px, dark 0.87 → 0.86.

## Ink — wash
Watercolour 1.00 · 40 px · 35.8 s

![Ink — wash](Ink-wash.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 13 % → 13 % | 37.3 px | 0.42 | 1.02 | 84 |
| heavy line | 19 % → 19 % | 55.2 px | 0.35 | 1.01 | 85 |
| pressure swell | 13 % → 13 % | 48.2 px | 0.41 | 1.02 | 69 |
| fast wave | 41 % → 42 % | 47.8 px | 0.32 | 1.02 | 194 |
| slow wave | 39 % → 40 % | 45.3 px | 0.42 | 1.02 | 373 |
| spiral | 60 % → 62 % | 39.7 px | 0.33 | 1.02 | 360 |
| loop | 34 % → 34 % | 43.8 px | 0.39 | 1.01 | 294 |
| tilted | 15 % → 15 % | 40.7 px | 0.43 | 1.01 | 123 |
| over the wet one | 30 % → 31 % | 43.4 px | 0.43 | 1.02 | 76 |
| long, no reload | 71 % → 75 % | 32.0 px | 0.31 | 1.05 | 486 | quarters: 0.40 → 0.29 → 0.19 → 0.12

Numbers say: light vs heavy: width 37.3 → 55.2 px, dark 0.42 → 0.35.

## Ink — dry brush
Ink 1.00 · 30 px · 24.2 s

![Ink — dry brush](Ink-dry-brush.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 6 % → 5 % | 17.4 px | 0.83 | 0.88 | 98 |
| heavy line | 7 % → 6 % | 19.1 px | 0.82 | 0.85 | 139 |
| pressure swell | 5 % → 5 % | 18.8 px | 0.83 | 0.94 | 89 |
| fast wave | 12 % → 7 % | 14.3 px | 0.81 | 0.59 | 230 |
| slow wave | 12 % → 7 % | 13.6 px | 0.81 | 0.59 | 489 |
| spiral | 18 % → 8 % | 12.1 px | 0.80 | 0.43 | 373 |
| loop | 11 % → 8 % | 14.6 px | 0.80 | 0.72 | 196 |
| tilted | 6 % → 6 % | 16.3 px | 0.81 | 1.06 | 126 |
| over the wet one | 12 % → 12 % | 18.0 px | 0.81 | 0.94 | 92 |
| long, no reload | 20 % → 9 % | 9.0 px | 0.78 | 0.42 | 689 | quarters: 0.26 → 0.09 → 0.03 → 0.01

Numbers say: light vs heavy: width 17.4 → 19.1 px, dark 0.83 → 0.82; pressure barely changes the width.

## Ink — nib
Watercolour 1.00 · 5 px · 22.8 s

![Ink — nib](Ink-nib.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 2 % → 5 % | 5.5 px | 0.89 | 2.46 | 31 |
| heavy line | 2 % → 5 % | 6.4 px | 0.89 | 2.34 | 27 |
| pressure swell | 2 % → 4 % | 6.2 px | 0.89 | 2.53 | 20 |
| fast wave | 5 % → 8 % | 5.9 px | 0.89 | 1.63 | 78 |
| slow wave | 5 % → 8 % | 5.7 px | 0.89 | 1.70 | 108 |
| spiral | 8 % → 11 % | 5.0 px | 0.87 | 1.41 | 117 |
| loop | 4 % → 8 % | 5.7 px | 0.89 | 1.74 | 58 |
| tilted | 4 % → 4 % | 10.3 px | 0.89 | 1.02 | 30 |
| over the wet one | 6 % → 9 % | 6.1 px | 0.89 | 1.61 | 30 |
| long, no reload | 9 % → 12 % | 4.2 px | 0.85 | 1.30 | 169 | quarters: 0.24 → 0.11 → 0.07 → 0.05

Numbers say: light vs heavy: width 5.5 → 6.4 px, dark 0.89 → 0.89; wet paint spreads well beyond the stroke.

## 0.45 · Dry brush
Gouache 0.91 · Ink 0.07 · 34 px · 33.8 s

![0.45 · Dry brush](0-45-Dry-brush.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 9 % → 5 % | 26.6 px | 0.68 | 0.56 | 190 |
| heavy line | 10 % → 5 % | 28.5 px | 0.68 | 0.56 | 125 |
| pressure swell | 8 % → 5 % | 28.8 px | 0.68 | 0.67 | 108 |
| fast wave | 18 % → 6 % | 20.6 px | 0.68 | 0.33 | 433 |
| slow wave | 21 % → 7 % | 23.7 px | 0.68 | 0.35 | 1226 |
| spiral | 29 % → 7 % | 19.0 px | 0.68 | 0.24 | 734 |
| loop | 18 % → 8 % | 23.1 px | 0.68 | 0.42 | 305 |
| tilted | 8 % → 8 % | 22.8 px | 0.68 | 1.02 | 185 |
| over the wet one | 18 % → 13 % | 26.5 px | 0.68 | 0.72 | 134 |
| long, no reload | 31 % → 9 % | 13.8 px | 0.68 | 0.28 | 1067 | quarters: 0.36 → 0.23 → 0.16 → 0.12

Numbers say: light vs heavy: width 26.6 → 28.5 px, dark 0.68 → 0.68; pressure barely changes the width.

## Dry pastel
Pastel 1.00 · 26 px · 13.1 s

![Dry pastel](Dry-pastel.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 3 % → 3 % | 8.3 px | 0.38 | 1.00 | 46 |
| heavy line | 5 % → 5 % | 13.2 px | 0.39 | 1.00 | 66 |
| pressure swell | 3 % → 3 % | 11.7 px | 0.38 | 1.00 | 26 |
| fast wave | 10 % → 10 % | 11.9 px | 0.39 | 1.00 | 91 |
| slow wave | 10 % → 10 % | 11.3 px | 0.39 | 1.00 | 217 |
| spiral | 15 % → 15 % | 9.6 px | 0.39 | 1.00 | 241 |
| loop | 7 % → 7 % | 9.4 px | 0.39 | 1.00 | 114 |
| tilted | 3 % → 3 % | 8.3 px | 0.38 | 1.00 | 48 |
| over the wet one | 7 % → 7 % | 11.1 px | 0.38 | 1.00 | 37 |
| long, no reload | 18 % → 18 % | 8.2 px | 0.39 | 1.00 | 492 | quarters: 0.08 → 0.08 → 0.08 → 0.07

Numbers say: light vs heavy: width 8.3 → 13.2 px, dark 0.38 → 0.39; the long stroke does not run out of paint.

## 0.45 · Charcoal
Charcoal 1.00 · 18 px · 12.0 s

![0.45 · Charcoal](0-45-Charcoal.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 2 % → 2 % | 6.5 px | 0.80 | 1.00 | 20 |
| heavy line | 3 % → 3 % | 9.2 px | 0.80 | 1.00 | 19 |
| pressure swell | 2 % → 2 % | 8.8 px | 0.80 | 1.00 | 13 |
| fast wave | 7 % → 7 % | 8.5 px | 0.80 | 1.00 | 47 |
| slow wave | 7 % → 7 % | 8.0 px | 0.80 | 1.00 | 67 |
| spiral | 12 % → 12 % | 7.9 px | 0.80 | 1.00 | 85 |
| loop | 6 % → 6 % | 8.1 px | 0.80 | 1.00 | 38 |
| tilted | 3 % → 3 % | 7.5 px | 0.80 | 1.00 | 28 |
| over the wet one | 6 % → 6 % | 7.9 px | 0.80 | 1.00 | 20 |
| long, no reload | 17 % → 17 % | 7.8 px | 0.80 | 1.00 | 127 | quarters: 0.15 → 0.16 → 0.15 → 0.16

Numbers say: light vs heavy: width 6.5 → 9.2 px, dark 0.80 → 0.80; the long stroke does not run out of paint.

## Watercolour — wash
Watercolour 1.00 · 50 px · 40.5 s

![Watercolour — wash](Watercolour-wash.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 16 % → 16 % | 45.5 px | 0.22 | 1.01 | 135 |
| heavy line | 22 % → 22 % | 64.9 px | 0.19 | 1.00 | 129 |
| pressure swell | 15 % → 15 % | 56.1 px | 0.22 | 1.01 | 85 |
| fast wave | 48 % → 49 % | 55.5 px | 0.19 | 1.01 | 347 |
| slow wave | 46 % → 46 % | 53.3 px | 0.24 | 1.00 | 703 |
| spiral | 66 % → 66 % | 43.7 px | 0.21 | 1.00 | 550 |
| loop | 40 % → 40 % | 51.4 px | 0.22 | 1.00 | 349 |
| tilted | 18 % → 18 % | 49.7 px | 0.23 | 1.00 | 195 |
| over the wet one | 36 % → 36 % | 49.6 px | 0.23 | 1.01 | 117 |
| long, no reload | 84 % → 84 % | 37.7 px | 0.20 | 1.00 | 812 | quarters: 0.24 → 0.20 → 0.16 → 0.12

Numbers say: light vs heavy: width 45.5 → 64.9 px, dark 0.22 → 0.19.

## Watercolour — wet-in-wet
Watercolour 1.00 · 44 px · 40.3 s

![Watercolour — wet-in-wet](Watercolour-wet-in-wet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 13 % → 21 % | 38.4 px | 0.32 | 1.58 | 122 |
| heavy line | 19 % → 22 % | 54.6 px | 0.34 | 1.17 | 118 |
| pressure swell | 12 % → 17 % | 46.5 px | 0.35 | 1.34 | 72 |
| fast wave | 41 % → 49 % | 47.7 px | 0.33 | 1.19 | 373 |
| slow wave | 40 % → 48 % | 46.2 px | 0.40 | 1.21 | 476 |
| spiral | 63 % → 69 % | 41.5 px | 0.37 | 1.10 | 485 |
| loop | 34 % → 41 % | 44.4 px | 0.37 | 1.20 | 205 |
| tilted | 15 % → 16 % | 41.5 px | 0.36 | 1.06 | 160 |
| over the wet one | 31 % → 40 % | 44.1 px | 0.36 | 1.31 | 122 |
| long, no reload | 78 % → 87 % | 34.8 px | 0.36 | 1.12 | 709 | quarters: 0.40 → 0.37 → 0.32 → 0.26

Numbers say: light vs heavy: width 38.4 → 54.6 px, dark 0.32 → 0.34; wet paint spreads well beyond the stroke.

## Watercolour — glaze
Watercolour 1.00 · 38 px · 33.7 s

![Watercolour — glaze](Watercolour-glaze.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 13 % → 13 % | 36.6 px | 0.07 | 1.02 | 86 |
| heavy line | 19 % → 19 % | 55.4 px | 0.07 | 1.00 | 106 |
| pressure swell | 13 % → 13 % | 47.0 px | 0.07 | 1.02 | 59 |
| fast wave | 39 % → 40 % | 45.6 px | 0.07 | 1.01 | 202 |
| slow wave | 37 % → 37 % | 42.8 px | 0.07 | 1.01 | 533 |
| spiral | 59 % → 60 % | 38.8 px | 0.06 | 1.01 | 397 |
| loop | 33 % → 33 % | 42.6 px | 0.07 | 1.00 | 188 |
| tilted | 14 % → 14 % | 40.1 px | 0.07 | 1.00 | 114 |
| over the wet one | 30 % → 30 % | 42.3 px | 0.07 | 1.01 | 78 |
| long, no reload | 69 % → 70 % | 30.9 px | 0.06 | 1.01 | 526 | quarters: 0.06 → 0.05 → 0.03 → 0.02

Numbers say: light vs heavy: width 36.6 → 55.4 px, dark 0.07 → 0.07.

## Watercolour — granulating
Watercolour 1.00 · 44 px · 36.6 s

![Watercolour — granulating](Watercolour-granulating.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 14 % → 14 % | 41.4 px | 0.35 | 1.01 | 90 |
| heavy line | 21 % → 21 % | 60.4 px | 0.31 | 1.00 | 96 |
| pressure swell | 14 % → 14 % | 52.2 px | 0.34 | 1.01 | 79 |
| fast wave | 45 % → 45 % | 51.7 px | 0.29 | 1.01 | 272 |
| slow wave | 42 % → 42 % | 48.2 px | 0.35 | 1.01 | 455 |
| spiral | 62 % → 63 % | 41.0 px | 0.30 | 1.01 | 448 |
| loop | 37 % → 37 % | 47.6 px | 0.33 | 1.00 | 369 |
| tilted | 16 % → 16 % | 45.5 px | 0.36 | 1.00 | 135 |
| over the wet one | 33 % → 33 % | 46.2 px | 0.36 | 1.01 | 96 |
| long, no reload | 75 % → 76 % | 33.6 px | 0.29 | 1.01 | 583 | quarters: 0.34 → 0.26 → 0.20 → 0.14

Numbers say: light vs heavy: width 41.4 → 60.4 px, dark 0.35 → 0.31.

## Watercolour — dry brush
Watercolour 1.00 · 36 px · 29.3 s

![Watercolour — dry brush](Watercolour-dry-brush.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 10 % → 10 % | 27.9 px | 0.17 | 1.01 | 115 |
| heavy line | 14 % → 13 % | 39.9 px | 0.16 | 0.93 | 104 |
| pressure swell | 11 % → 11 % | 40.3 px | 0.16 | 0.98 | 82 |
| fast wave | 27 % → 20 % | 30.7 px | 0.13 | 0.74 | 253 |
| slow wave | 24 % → 17 % | 28.0 px | 0.14 | 0.71 | 475 |
| spiral | 34 % → 20 % | 22.4 px | 0.13 | 0.58 | 436 |
| loop | 21 % → 18 % | 27.1 px | 0.14 | 0.86 | 235 |
| tilted | 10 % → 10 % | 28.5 px | 0.17 | 1.00 | 169 |
| over the wet one | 21 % → 20 % | 31.3 px | 0.17 | 0.95 | 111 |
| long, no reload | 36 % → 19 % | 16.0 px | 0.14 | 0.54 | 718 | quarters: 0.09 → 0.03 → 0.01 → 0.00

Numbers say: light vs heavy: width 27.9 → 39.9 px, dark 0.17 → 0.16.

## Gouache
Gouache 1.00 · 30 px · 31.8 s

![Gouache](Gouache.png)

A light paint: laid on a grey sheet (on white it cannot be seen); **dark** = how far it is from the grey either way.

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 8 % → 5 % | 23.4 px | 0.29 | 0.59 | 83 |
| heavy line | 12 % → 5 % | 35.8 px | 0.28 | 0.40 | 104 |
| pressure swell | 10 % → 5 % | 36.3 px | 0.28 | 0.49 | 77 |
| fast wave | 23 % → 6 % | 26.0 px | 0.28 | 0.25 | 283 |
| slow wave | 23 % → 7 % | 26.1 px | 0.28 | 0.30 | 362 |
| spiral | 29 % → 6 % | 18.9 px | 0.28 | 0.22 | 357 |
| loop | 19 % → 7 % | 24.1 px | 0.28 | 0.36 | 190 |
| tilted | 9 % → 9 % | 24.2 px | 0.28 | 1.01 | 168 |
| over the wet one | 19 % → 12 % | 28.8 px | 0.28 | 0.61 | 155 |
| long, no reload | 28 % → 8 % | 12.7 px | 0.28 | 0.30 | 768 | quarters: 0.01 → 0.02 → 0.02 → 0.02

Numbers say: light vs heavy: width 23.4 → 35.8 px, dark 0.29 → 0.28; the long stroke does not run out of paint.

## Oil — alla prima
Oil 0.89 · Oil glaze 0.11 · 30 px · 14.5 s

![Oil — alla prima](Oil-alla-prima.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 9 % → 9 % | 26.4 px | 0.49 | 1.00 | 97 |
| heavy line | 9 % → 9 % | 27.4 px | 0.48 | 1.00 | 100 |
| pressure swell | 8 % → 8 % | 28.8 px | 0.51 | 1.00 | 64 |
| fast wave | 22 % → 22 % | 24.9 px | 0.49 | 1.00 | 233 |
| slow wave | 23 % → 23 % | 26.9 px | 0.50 | 1.00 | 373 |
| spiral | 36 % → 36 % | 23.4 px | 0.49 | 1.00 | 524 |
| loop | 19 % → 19 % | 25.2 px | 0.50 | 1.00 | 303 |
| tilted | 11 % → 11 % | 29.8 px | 0.50 | 1.00 | 119 |
| over the wet one | 20 % → 20 % | 25.1 px | 0.50 | 1.00 | 137 |
| long, no reload | 42 % → 42 % | 18.7 px | 0.49 | 1.00 | 563 | quarters: 0.29 → 0.23 → 0.21 → 0.17

Numbers say: light vs heavy: width 26.4 → 27.4 px, dark 0.49 → 0.48; pressure barely changes the width.

## Oil — impasto
Oil heavy 1.00 · 34 px · 16.5 s

![Oil — impasto](Oil-impasto.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 12 % → 12 % | 33.5 px | 0.23 | 1.00 | 115 |
| heavy line | 13 % → 13 % | 36.4 px | 0.23 | 1.00 | 141 |
| pressure swell | 10 % → 10 % | 35.9 px | 0.25 | 1.00 | 80 |
| fast wave | 29 % → 29 % | 33.0 px | 0.22 | 1.00 | 290 |
| slow wave | 30 % → 30 % | 34.3 px | 0.23 | 1.00 | 474 |
| spiral | 47 % → 47 % | 31.0 px | 0.21 | 1.00 | 793 |
| loop | 25 % → 25 % | 32.7 px | 0.23 | 1.00 | 267 |
| tilted | 12 % → 12 % | 32.6 px | 0.24 | 1.00 | 164 |
| over the wet one | 23 % → 23 % | 31.8 px | 0.24 | 1.00 | 115 |
| long, no reload | 52 % → 52 % | 23.4 px | 0.21 | 1.00 | 699 | quarters: 0.18 → 0.13 → 0.10 → 0.08

Numbers say: light vs heavy: width 33.5 → 36.4 px, dark 0.23 → 0.23; pressure barely changes the width.

## Oil — glaze
Oil glaze 1.00 · 40 px · 16.8 s

![Oil — glaze](Oil-glaze.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 9 % → 9 % | 27.0 px | 0.50 | 1.00 | 111 |
| heavy line | 13 % → 13 % | 38.3 px | 0.49 | 1.00 | 138 |
| pressure swell | 10 % → 10 % | 36.6 px | 0.50 | 1.00 | 95 |
| fast wave | 29 % → 29 % | 33.5 px | 0.49 | 1.00 | 308 |
| slow wave | 30 % → 30 % | 34.6 px | 0.50 | 1.00 | 484 |
| spiral | 46 % → 46 % | 30.1 px | 0.49 | 1.00 | 466 |
| loop | 24 % → 24 % | 31.4 px | 0.50 | 1.00 | 233 |
| tilted | 11 % → 11 % | 30.4 px | 0.50 | 1.00 | 136 |
| over the wet one | 23 % → 23 % | 32.5 px | 0.50 | 1.00 | 105 |
| long, no reload | 52 % → 52 % | 23.5 px | 0.49 | 1.00 | 1038 | quarters: 0.34 → 0.30 → 0.27 → 0.22

Numbers say: light vs heavy: width 27.0 → 38.3 px, dark 0.50 → 0.49.

## Oil — scumble
Oil 1.00 · 36 px · 16.0 s

![Oil — scumble](Oil-scumble.png)

A light paint: laid on a grey sheet (on white it cannot be seen); **dark** = how far it is from the grey either way.

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 10 % → 10 % | 28.6 px | 0.26 | 1.00 | 155 |
| heavy line | 10 % → 10 % | 28.1 px | 0.26 | 1.00 | 174 |
| pressure swell | 9 % → 9 % | 32.0 px | 0.26 | 1.00 | 129 |
| fast wave | 20 % → 20 % | 23.1 px | 0.16 | 1.00 | 400 |
| slow wave | 23 % → 23 % | 26.1 px | 0.19 | 1.00 | 628 |
| spiral | 32 % → 32 % | 21.3 px | 0.14 | 1.00 | 663 |
| loop | 19 % → 19 % | 24.5 px | 0.20 | 1.00 | 310 |
| tilted | 10 % → 10 % | 27.6 px | 0.25 | 1.00 | 161 |
| over the wet one | 20 % → 20 % | 28.0 px | 0.25 | 1.00 | 136 |
| long, no reload | 33 % → 33 % | 14.7 px | 0.14 | 1.00 | 819 | quarters: 0.00 → 0.00 → 0.00 → 0.00

Numbers say: light vs heavy: width 28.6 → 28.1 px, dark 0.26 → 0.26; pressure barely changes the width.

## Acrylic — heavy body
Impasto 0.98 · 30 px · 15.1 s

![Acrylic — heavy body](Acrylic-heavy-body.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 9 % → 8 % | 26.5 px | 0.51 | 0.87 | 116 |
| heavy line | 10 % → 9 % | 28.6 px | 0.51 | 0.87 | 100 |
| pressure swell | 8 % → 7 % | 29.2 px | 0.53 | 0.91 | 81 |
| fast wave | 19 % → 13 % | 22.3 px | 0.52 | 0.65 | 300 |
| slow wave | 20 % → 15 % | 23.1 px | 0.52 | 0.76 | 424 |
| spiral | 27 % → 15 % | 18.0 px | 0.52 | 0.54 | 397 |
| loop | 17 % → 13 % | 22.3 px | 0.52 | 0.77 | 232 |
| tilted | 8 % → 8 % | 22.5 px | 0.52 | 0.99 | 108 |
| over the wet one | 17 % → 15 % | 25.2 px | 0.52 | 0.87 | 103 |
| long, no reload | 30 % → 17 % | 13.6 px | 0.52 | 0.56 | 574 | quarters: 0.25 → 0.15 → 0.11 → 0.08

Numbers say: light vs heavy: width 26.5 → 28.6 px, dark 0.51 → 0.51; pressure barely changes the width.

## Acrylic — fluid
Watercolour 1.00 · 36 px · 32.1 s

![Acrylic — fluid](Acrylic-fluid.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 12 % → 12 % | 34.8 px | 0.24 | 1.01 | 99 |
| heavy line | 18 % → 18 % | 52.6 px | 0.21 | 0.99 | 111 |
| pressure swell | 12 % → 12 % | 45.4 px | 0.23 | 1.00 | 60 |
| fast wave | 38 % → 38 % | 44.1 px | 0.19 | 0.98 | 228 |
| slow wave | 35 % → 35 % | 40.5 px | 0.22 | 1.00 | 368 |
| spiral | 55 % → 53 % | 36.0 px | 0.19 | 0.98 | 355 |
| loop | 31 % → 31 % | 40.2 px | 0.21 | 1.00 | 173 |
| tilted | 12 % → 12 % | 34.2 px | 0.24 | 1.00 | 105 |
| over the wet one | 27 % → 28 % | 42.3 px | 0.24 | 1.02 | 78 |
| long, no reload | 61 % → 58 % | 27.6 px | 0.19 | 0.95 | 471 | quarters: 0.20 → 0.14 → 0.09 → 0.06

Numbers say: light vs heavy: width 34.8 → 52.6 px, dark 0.24 → 0.21.

## Acrylic — palette knife
Impasto 1.00 · 42 px · 21.2 s

![Acrylic — palette knife](Acrylic-palette-knife.png)

A light paint: laid on a grey sheet (on white it cannot be seen); **dark** = how far it is from the grey either way.

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 15 % → 15 % | 44.0 px | 0.39 | 0.98 | 50 |
| heavy line | 15 % → 15 % | 44.2 px | 0.40 | 0.98 | 33 |
| pressure swell | 12 % → 11 % | 43.5 px | 0.42 | 0.99 | 15 |
| fast wave | 36 % → 20 % | 41.9 px | 0.37 | 0.55 | 68 |
| slow wave | 37 % → 21 % | 42.7 px | 0.37 | 0.57 | 118 |
| spiral | 47 % → 18 % | 30.7 px | 0.37 | 0.39 | 124 |
| loop | 32 % → 24 % | 41.2 px | 0.36 | 0.77 | 67 |
| tilted | 12 % → 12 % | 33.6 px | 0.39 | 1.00 | 28 |
| over the wet one | 26 % → 25 % | 39.8 px | 0.39 | 0.97 | 33 |
| long, no reload | 53 % → 20 % | 23.6 px | 0.35 | 0.38 | 148 | quarters: 0.00 → 0.00 → 0.00 → 0.01

Numbers say: light vs heavy: width 44.0 → 44.2 px, dark 0.39 → 0.40; pressure barely changes the width; the long stroke does not run out of paint.

## Finger on oil
Oil 1.00 · 30 px · 13.0 s

![Finger on oil](Finger-on-oil.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 6 % → 6 % | 17.9 px | 0.36 | 1.00 | 54 |
| heavy line | 8 % → 8 % | 24.6 px | 0.34 | 1.00 | 57 |
| pressure swell | 6 % → 6 % | 22.4 px | 0.38 | 1.00 | 40 |
| fast wave | 10 % → 10 % | 12.0 px | 0.24 | 1.00 | 121 |
| slow wave | 15 % → 15 % | 17.6 px | 0.33 | 1.00 | 216 |
| spiral | 19 % → 19 % | 12.5 px | 0.27 | 1.00 | 198 |
| loop | 13 % → 13 % | 16.8 px | 0.32 | 1.00 | 140 |
| tilted | 8 % → 8 % | 23.6 px | 0.36 | 1.00 | 70 |
| over the wet one | 16 % → 16 % | 20.0 px | 0.36 | 1.00 | 47 |
| long, no reload | 21 % → 21 % | 9.5 px | 0.25 | 1.00 | 280 | quarters: 0.15 → 0.04 → 0.02 → 0.01

Numbers say: light vs heavy: width 17.9 → 24.6 px, dark 0.36 → 0.34.

## Palette knife — oil
Oil heavy 0.93 · Impasto 0.07 · 44 px · 20.0 s

![Palette knife — oil](Palette-knife-oil.png)

A light paint: laid on a grey sheet (on white it cannot be seen); **dark** = how far it is from the grey either way.

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 16 % → 14 % | 45.7 px | 0.37 | 0.90 | 47 |
| heavy line | 16 % → 16 % | 46.3 px | 0.38 | 0.98 | 38 |
| pressure swell | 12 % → 12 % | 45.2 px | 0.38 | 0.99 | 13 |
| fast wave | 39 % → 34 % | 44.9 px | 0.35 | 0.89 | 76 |
| slow wave | 39 % → 36 % | 45.4 px | 0.35 | 0.91 | 143 |
| spiral | 62 % → 37 % | 40.7 px | 0.35 | 0.60 | 155 |
| loop | 34 % → 31 % | 43.7 px | 0.36 | 0.92 | 114 |
| tilted | 13 % → 13 % | 36.6 px | 0.37 | 1.00 | 38 |
| over the wet one | 28 % → 27 % | 40.8 px | 0.37 | 0.97 | 37 |
| long, no reload | 74 % → 39 % | 33.0 px | 0.34 | 0.53 | 181 | quarters: 0.00 → 0.00 → 0.01 → 0.01

Numbers say: light vs heavy: width 45.7 → 46.3 px, dark 0.37 → 0.38; pressure barely changes the width; the long stroke does not run out of paint.

## 0.45 · Sponge
Watercolour 0.93 · Ink 0.07 · 46 px · 34.5 s

![0.45 · Sponge](0-45-Sponge.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 27 % → 25 % | 78.2 px | 0.12 | 0.95 | 67 |
| heavy line | 32 % → 29 % | 91.9 px | 0.12 | 0.92 | 95 |
| pressure swell | 24 % → 21 % | 90.6 px | 0.12 | 0.88 | 55 |
| fast wave | 59 % → 55 % | 68.5 px | 0.12 | 0.92 | 167 |
| slow wave | 61 % → 58 % | 70.4 px | 0.17 | 0.95 | 470 |
| spiral | 77 % → 75 % | 50.7 px | 0.16 | 0.97 | 505 |
| loop | 53 % → 51 % | 69.1 px | 0.14 | 0.95 | 152 |
| tilted | 18 % → 18 % | 50.7 px | 0.17 | 1.00 | 137 |
| over the wet one | 45 % → 42 % | 73.6 px | 0.17 | 0.94 | 63 |
| long, no reload | 94 % → 89 % | 42.0 px | 0.17 | 0.95 | 401 | quarters: 0.17 → 0.18 → 0.16 → 0.14

Numbers say: light vs heavy: width 78.2 → 91.9 px, dark 0.12 → 0.12.

## 0.45 · Eraser
Watercolour 1.00 · 30 px · 21.3 s · over bands of wet oil paint and oil pastel in turn (it works on paint already there: look at what it does to the bands; covered counts the bands too)

![0.45 · Eraser](0-45-Eraser.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 24 % → 24 % | 69.2 px | 0.82 | 1.00 | 48 |
| heavy line | 23 % → 23 % | 67.4 px | 0.81 | 1.00 | 51 |
| pressure swell | 23 % → 23 % | 86.8 px | 0.82 | 1.00 | 36 |
| fast wave | 21 % → 21 % | 24.7 px | 0.81 | 1.00 | 147 |
| slow wave | 20 % → 20 % | 23.5 px | 0.82 | 1.00 | 238 |
| spiral | 20 % → 20 % | 13.5 px | 0.79 | 1.00 | 244 |
| loop | 21 % → 21 % | 27.8 px | 0.80 | 1.00 | 136 |
| tilted | 23 % → 23 % | 64.8 px | 0.81 | 1.00 | 63 |
| over the wet one | 22 % → 22 % | 0.0 px | 0.81 | 1.00 | 79 |
| long, no reload | 17 % → 17 % | 7.5 px | 0.79 | 1.00 | 319 | quarters: 0.13 → 0.16 → 0.13 → 0.17

Numbers say: light vs heavy: width 69.2 → 67.4 px, dark 0.82 → 0.81; pressure barely changes the width; the long stroke does not run out of paint.

## Lift wet paint
Watercolour 1.00 · 30 px · 20.6 s · over bands of wet oil paint and oil pastel in turn (it works on paint already there: look at what it does to the bands; covered counts the bands too)

![Lift wet paint](Lift-wet-paint.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 24 % → 24 % | 70.1 px | 0.82 | 1.00 | 37 |
| heavy line | 24 % → 24 % | 69.8 px | 0.82 | 1.00 | 53 |
| pressure swell | 24 % → 24 % | 89.6 px | 0.82 | 1.00 | 31 |
| fast wave | 24 % → 24 % | 27.7 px | 0.82 | 1.00 | 110 |
| slow wave | 24 % → 24 % | 27.7 px | 0.82 | 1.00 | 190 |
| spiral | 24 % → 24 % | 15.9 px | 0.82 | 1.00 | 185 |
| loop | 24 % → 24 % | 31.1 px | 0.82 | 1.00 | 155 |
| tilted | 24 % → 24 % | 66.8 px | 0.82 | 1.00 | 84 |
| over the wet one | 24 % → 24 % | 0.0 px | 0.82 | 1.00 | 52 |
| long, no reload | 24 % → 24 % | 10.7 px | 0.82 | 1.00 | 268 | quarters: 0.18 → 0.24 → 0.17 → 0.24

Numbers say: light vs heavy: width 70.1 → 69.8 px, dark 0.82 → 0.82; pressure barely changes the width; the long stroke does not run out of paint.

## Sgraffito
Watercolour 1.00 · 10 px · 20.3 s · over bands of wet oil paint and oil pastel in turn (it works on paint already there: look at what it does to the bands; covered counts the bands too)

![Sgraffito](Sgraffito.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 24 % → 24 % | 69.9 px | 0.81 | 1.00 | 8 |
| heavy line | 24 % → 24 % | 69.8 px | 0.82 | 1.00 | 10 |
| pressure swell | 24 % → 24 % | 89.6 px | 0.82 | 1.00 | 12 |
| fast wave | 24 % → 24 % | 27.7 px | 0.82 | 1.00 | 33 |
| slow wave | 24 % → 24 % | 27.7 px | 0.82 | 1.00 | 39 |
| spiral | 24 % → 24 % | 15.9 px | 0.82 | 1.00 | 40 |
| loop | 24 % → 24 % | 31.1 px | 0.82 | 1.00 | 21 |
| tilted | 24 % → 24 % | 66.9 px | 0.82 | 1.00 | 8 |
| over the wet one | 24 % → 24 % | 0.0 px | 0.82 | 1.00 | 9 |
| long, no reload | 24 % → 24 % | 10.6 px | 0.82 | 1.00 | 63 | quarters: 0.17 → 0.24 → 0.17 → 0.24

Numbers say: light vs heavy: width 69.9 → 69.8 px, dark 0.81 → 0.82; pressure barely changes the width; the long stroke does not run out of paint.

## Brush Artist · Refs · #01 Henry Ward peach cloud
Gouache 1.00 · 44 px · 34.4 s

![Brush Artist · Refs · #01 Henry Ward peach cloud](Brush-Artist-Refs-01-Henry-Ward-peach-cloud.png)

A light paint: laid on a grey sheet (on white it cannot be seen); **dark** = how far it is from the grey either way.

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 12 % → 8 % | 36.2 px | 0.33 | 0.65 | 154 |
| heavy line | 14 % → 9 % | 39.8 px | 0.33 | 0.65 | 150 |
| pressure swell | 10 % → 8 % | 38.7 px | 0.33 | 0.73 | 130 |
| fast wave | 28 % → 7 % | 32.1 px | 0.33 | 0.26 | 430 |
| slow wave | 30 % → 12 % | 34.6 px | 0.33 | 0.39 | 749 |
| spiral | 43 % → 10 % | 28.2 px | 0.33 | 0.24 | 638 |
| loop | 26 % → 11 % | 33.8 px | 0.33 | 0.41 | 351 |
| tilted | 12 % → 12 % | 34.0 px | 0.33 | 0.99 | 263 |
| over the wet one | 24 % → 18 % | 33.9 px | 0.33 | 0.74 | 225 |
| long, no reload | 40 % → 13 % | 17.8 px | 0.33 | 0.32 | 913 | quarters: 0.01 → 0.02 → 0.02 → 0.03

Numbers say: light vs heavy: width 36.2 → 39.8 px, dark 0.33 → 0.33; pressure barely changes the width; the long stroke does not run out of paint.

## Brush Artist · Refs · #02 Henry Ward cream strokes
Gouache 1.00 · 46 px · 34.7 s

![Brush Artist · Refs · #02 Henry Ward cream strokes](Brush-Artist-Refs-02-Henry-Ward-cream-strokes.png)

A light paint: laid on a grey sheet (on white it cannot be seen); **dark** = how far it is from the grey either way.

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 13 % → 7 % | 38.6 px | 0.41 | 0.55 | 157 |
| heavy line | 14 % → 9 % | 41.1 px | 0.41 | 0.65 | 177 |
| pressure swell | 11 % → 8 % | 40.8 px | 0.41 | 0.78 | 117 |
| fast wave | 28 % → 7 % | 32.9 px | 0.41 | 0.25 | 502 |
| slow wave | 32 % → 11 % | 37.1 px | 0.41 | 0.34 | 750 |
| spiral | 44 % → 10 % | 28.9 px | 0.41 | 0.24 | 657 |
| loop | 27 % → 11 % | 34.8 px | 0.41 | 0.41 | 360 |
| tilted | 12 % → 12 % | 34.0 px | 0.41 | 0.99 | 206 |
| over the wet one | 25 % → 18 % | 35.5 px | 0.41 | 0.73 | 172 |
| long, no reload | 39 % → 13 % | 17.4 px | 0.41 | 0.35 | 944 | quarters: 0.01 → 0.02 → 0.03 → 0.03

Numbers say: light vs heavy: width 38.6 → 41.1 px, dark 0.41 → 0.41; pressure barely changes the width; the long stroke does not run out of paint.

## Brush Artist · Refs · #03 Henry Ward navy contours
Impasto 1.00 · 22 px · 15.8 s

![Brush Artist · Refs · #03 Henry Ward navy contours](Brush-Artist-Refs-03-Henry-Ward-navy-contours.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 7 % → 7 % | 21.6 px | 0.70 | 0.94 | 92 |
| heavy line | 8 % → 8 % | 23.6 px | 0.70 | 0.95 | 102 |
| pressure swell | 6 % → 6 % | 23.2 px | 0.73 | 0.94 | 64 |
| fast wave | 19 % → 12 % | 21.8 px | 0.72 | 0.65 | 240 |
| slow wave | 19 % → 13 % | 22.5 px | 0.72 | 0.68 | 343 |
| spiral | 29 % → 13 % | 19.4 px | 0.72 | 0.45 | 383 |
| loop | 17 % → 13 % | 21.5 px | 0.72 | 0.81 | 189 |
| tilted | 8 % → 8 % | 22.7 px | 0.71 | 1.00 | 148 |
| over the wet one | 16 % → 14 % | 21.4 px | 0.71 | 0.89 | 88 |
| long, no reload | 33 % → 13 % | 14.6 px | 0.72 | 0.41 | 523 | quarters: 0.36 → 0.29 → 0.19 → 0.06

Numbers say: light vs heavy: width 21.6 → 23.6 px, dark 0.70 → 0.70; pressure barely changes the width.

## Brush Artist · Refs · #04 Henry Ward grey cloud
Gouache 1.00 · 50 px · 38.8 s

![Brush Artist · Refs · #04 Henry Ward grey cloud](Brush-Artist-Refs-04-Henry-Ward-grey-cloud.png)

A light paint: laid on a grey sheet (on white it cannot be seen); **dark** = how far it is from the grey either way.

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 15 % → 9 % | 42.1 px | 0.32 | 0.61 | 185 |
| heavy line | 16 % → 10 % | 45.9 px | 0.32 | 0.63 | 187 |
| pressure swell | 12 % → 8 % | 46.0 px | 0.32 | 0.68 | 188 |
| fast wave | 32 % → 9 % | 37.1 px | 0.32 | 0.28 | 442 |
| slow wave | 36 % → 13 % | 42.2 px | 0.32 | 0.36 | 810 |
| spiral | 44 % → 12 % | 29.1 px | 0.32 | 0.27 | 738 |
| loop | 30 % → 12 % | 39.3 px | 0.32 | 0.41 | 380 |
| tilted | 13 % → 13 % | 37.1 px | 0.32 | 1.00 | 266 |
| over the wet one | 27 % → 20 % | 39.6 px | 0.32 | 0.74 | 359 |
| long, no reload | 47 % → 15 % | 21.1 px | 0.31 | 0.32 | 1990 | quarters: 0.01 → 0.02 → 0.03 → 0.03

Numbers say: light vs heavy: width 42.1 → 45.9 px, dark 0.32 → 0.32; pressure barely changes the width; the long stroke does not run out of paint.

## Brush Artist · Refs · #05 Henry Ward green in rust loops
Impasto 1.00 · 20 px · 15.5 s

![Brush Artist · Refs · #05 Henry Ward green in rust loops](Brush-Artist-Refs-05-Henry-Ward-green-in-rust-loops.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 7 % → 6 % | 19.5 px | 0.55 | 0.94 | 99 |
| heavy line | 7 % → 7 % | 21.4 px | 0.55 | 0.94 | 81 |
| pressure swell | 6 % → 5 % | 21.5 px | 0.57 | 0.92 | 62 |
| fast wave | 17 % → 11 % | 19.8 px | 0.56 | 0.64 | 206 |
| slow wave | 18 % → 12 % | 20.4 px | 0.56 | 0.65 | 298 |
| spiral | 27 % → 11 % | 17.7 px | 0.55 | 0.42 | 363 |
| loop | 15 % → 12 % | 19.5 px | 0.55 | 0.80 | 179 |
| tilted | 8 % → 8 % | 21.7 px | 0.56 | 1.00 | 93 |
| over the wet one | 15 % → 13 % | 19.3 px | 0.56 | 0.86 | 76 |
| long, no reload | 29 % → 12 % | 12.8 px | 0.56 | 0.40 | 526 | quarters: 0.25 → 0.18 → 0.09 → 0.02

Numbers say: light vs heavy: width 19.5 → 21.4 px, dark 0.55 → 0.55; pressure barely changes the width.

## Brush Artist · Refs · #06 Henry Ward scrubbed grey
Gouache 1.00 · 50 px · 38.3 s

![Brush Artist · Refs · #06 Henry Ward scrubbed grey](Brush-Artist-Refs-06-Henry-Ward-scrubbed-grey.png)

A light paint: laid on a grey sheet (on white it cannot be seen); **dark** = how far it is from the grey either way.

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 15 % → 9 % | 42.1 px | 0.33 | 0.61 | 168 |
| heavy line | 16 % → 10 % | 45.9 px | 0.33 | 0.63 | 156 |
| pressure swell | 12 % → 8 % | 46.0 px | 0.33 | 0.68 | 136 |
| fast wave | 32 % → 9 % | 37.1 px | 0.33 | 0.28 | 408 |
| slow wave | 36 % → 13 % | 42.2 px | 0.33 | 0.36 | 1049 |
| spiral | 44 % → 12 % | 29.1 px | 0.33 | 0.27 | 1678 |
| loop | 30 % → 12 % | 39.3 px | 0.33 | 0.41 | 383 |
| tilted | 13 % → 13 % | 37.1 px | 0.33 | 1.00 | 223 |
| over the wet one | 27 % → 20 % | 39.6 px | 0.33 | 0.74 | 176 |
| long, no reload | 47 % → 15 % | 21.1 px | 0.33 | 0.32 | 1028 | quarters: 0.01 → 0.02 → 0.03 → 0.03

Numbers say: light vs heavy: width 42.1 → 45.9 px, dark 0.33 → 0.33; pressure barely changes the width; the long stroke does not run out of paint.

## Brush Artist · Refs · #07 Henry Ward blue L + black zigzag
Impasto 1.00 · 34 px · 18.0 s

![Brush Artist · Refs · #07 Henry Ward blue L + black zigzag](Brush-Artist-Refs-07-Henry-Ward-blue-L-black-zigzag.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 11 % → 11 % | 33.2 px | 0.58 | 0.93 | 123 |
| heavy line | 12 % → 12 % | 35.9 px | 0.58 | 0.93 | 105 |
| pressure swell | 9 % → 9 % | 35.3 px | 0.59 | 0.94 | 74 |
| fast wave | 29 % → 20 % | 33.7 px | 0.59 | 0.68 | 331 |
| slow wave | 30 % → 21 % | 34.2 px | 0.58 | 0.72 | 618 |
| spiral | 47 % → 22 % | 31.2 px | 0.58 | 0.45 | 514 |
| loop | 25 % → 21 % | 32.7 px | 0.58 | 0.82 | 351 |
| tilted | 11 % → 11 % | 30.0 px | 0.58 | 1.00 | 161 |
| over the wet one | 22 % → 20 % | 31.8 px | 0.58 | 0.91 | 139 |
| long, no reload | 53 % → 22 % | 23.5 px | 0.59 | 0.42 | 694 | quarters: 0.40 → 0.32 → 0.21 → 0.09

Numbers say: light vs heavy: width 33.2 → 35.9 px, dark 0.58 → 0.58; pressure barely changes the width.

## Brush Artist · Refs · #08 Henry Ward olive bands
Gouache 1.00 · 34 px · 23.4 s

![Brush Artist · Refs · #08 Henry Ward olive bands](Brush-Artist-Refs-08-Henry-Ward-olive-bands.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 5 % → 0 % | 13.8 px | 0.61 | 0.06 | 93 |
| heavy line | 7 % → 0 % | 21.6 px | 0.61 | 0.07 | 151 |
| pressure swell | 5 % → 1 % | 20.5 px | 0.61 | 0.12 | 97 |
| fast wave | 11 % → 1 % | 12.2 px | 0.61 | 0.06 | 260 |
| slow wave | 15 % → 1 % | 17.5 px | 0.61 | 0.08 | 453 |
| spiral | 19 % → 1 % | 12.8 px | 0.61 | 0.05 | 444 |
| loop | 13 % → 2 % | 17.0 px | 0.61 | 0.12 | 237 |
| tilted | 7 % → 7 % | 19.9 px | 0.61 | 0.97 | 127 |
| over the wet one | 14 % → 3 % | 18.6 px | 0.61 | 0.25 | 113 |
| long, no reload | 21 % → 2 % | 9.2 px | 0.61 | 0.08 | 746 | quarters: 0.23 → 0.12 → 0.08 → 0.05

Numbers say: light vs heavy: width 13.8 → 21.6 px, dark 0.61 → 0.61.

## Brush Artist · Refs · #09 Henry Ward white loops
Gouache 1.00 · 46 px · 34.7 s

![Brush Artist · Refs · #09 Henry Ward white loops](Brush-Artist-Refs-09-Henry-Ward-white-loops.png)

A light paint: laid on a grey sheet (on white it cannot be seen); **dark** = how far it is from the grey either way.

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 13 % → 7 % | 38.6 px | 0.43 | 0.55 | 153 |
| heavy line | 14 % → 9 % | 41.1 px | 0.44 | 0.65 | 165 |
| pressure swell | 11 % → 8 % | 40.8 px | 0.44 | 0.78 | 110 |
| fast wave | 28 % → 7 % | 32.9 px | 0.43 | 0.25 | 371 |
| slow wave | 32 % → 11 % | 37.1 px | 0.43 | 0.34 | 705 |
| spiral | 44 % → 10 % | 28.9 px | 0.43 | 0.24 | 674 |
| loop | 27 % → 11 % | 34.8 px | 0.43 | 0.41 | 426 |
| tilted | 12 % → 12 % | 34.0 px | 0.43 | 0.99 | 252 |
| over the wet one | 25 % → 18 % | 35.5 px | 0.43 | 0.73 | 178 |
| long, no reload | 39 % → 13 % | 17.4 px | 0.43 | 0.35 | 957 | quarters: 0.01 → 0.02 → 0.03 → 0.03

Numbers say: light vs heavy: width 38.6 → 41.1 px, dark 0.43 → 0.44; pressure barely changes the width; the long stroke does not run out of paint.

## Brush Artist · Refs · #10 Henry Ward maroon loops
Impasto 1.00 · 30 px · 16.1 s

![Brush Artist · Refs · #10 Henry Ward maroon loops](Brush-Artist-Refs-10-Henry-Ward-maroon-loops.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 10 % → 9 % | 28.1 px | 0.71 | 0.94 | 93 |
| heavy line | 10 % → 10 % | 30.3 px | 0.71 | 0.95 | 96 |
| pressure swell | 8 % → 8 % | 30.0 px | 0.73 | 0.94 | 65 |
| fast wave | 25 % → 17 % | 28.3 px | 0.73 | 0.70 | 234 |
| slow wave | 25 % → 18 % | 29.0 px | 0.73 | 0.73 | 495 |
| spiral | 39 % → 18 % | 25.9 px | 0.72 | 0.47 | 460 |
| loop | 21 % → 18 % | 27.6 px | 0.73 | 0.85 | 310 |
| tilted | 10 % → 10 % | 27.9 px | 0.72 | 1.00 | 156 |
| over the wet one | 20 % → 18 % | 27.0 px | 0.72 | 0.91 | 130 |
| long, no reload | 45 % → 18 % | 20.2 px | 0.73 | 0.41 | 566 | quarters: 0.44 → 0.38 → 0.30 → 0.21

Numbers say: light vs heavy: width 28.1 → 30.3 px, dark 0.71 → 0.71; pressure barely changes the width.

## Brush Artist · Refs · #11 Henry Ward purple spun balls
Impasto 1.00 · 36 px · 17.8 s

![Brush Artist · Refs · #11 Henry Ward purple spun balls](Brush-Artist-Refs-11-Henry-Ward-purple-spun-balls.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 12 % → 11 % | 34.2 px | 0.71 | 0.96 | 225 |
| heavy line | 13 % → 12 % | 36.7 px | 0.71 | 0.95 | 167 |
| pressure swell | 10 % → 9 % | 36.2 px | 0.74 | 0.95 | 100 |
| fast wave | 30 % → 22 % | 34.6 px | 0.73 | 0.75 | 327 |
| slow wave | 30 % → 24 % | 35.1 px | 0.73 | 0.79 | 559 |
| spiral | 49 % → 24 % | 32.3 px | 0.73 | 0.50 | 539 |
| loop | 26 % → 23 % | 33.4 px | 0.73 | 0.88 | 279 |
| tilted | 11 % → 11 % | 31.2 px | 0.73 | 1.00 | 160 |
| over the wet one | 23 % → 21 % | 32.3 px | 0.73 | 0.93 | 125 |
| long, no reload | 55 % → 24 % | 24.6 px | 0.73 | 0.44 | 780 | quarters: 0.51 → 0.47 → 0.38 → 0.27

Numbers say: light vs heavy: width 34.2 → 36.7 px, dark 0.71 → 0.71; pressure barely changes the width.

## Brush Artist · Refs · #12 Henry Ward black-olive cage
Gouache 1.00 · 28 px · 24.1 s

![Brush Artist · Refs · #12 Henry Ward black-olive cage](Brush-Artist-Refs-12-Henry-Ward-black-olive-cage.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 5 % → 0 % | 13.6 px | 0.64 | 0.07 | 76 |
| heavy line | 6 % → 1 % | 18.9 px | 0.64 | 0.08 | 127 |
| pressure swell | 5 % → 1 % | 17.8 px | 0.64 | 0.18 | 69 |
| fast wave | 9 % → 1 % | 10.0 px | 0.65 | 0.11 | 215 |
| slow wave | 13 % → 1 % | 15.1 px | 0.64 | 0.09 | 417 |
| spiral | 17 % → 1 % | 11.0 px | 0.64 | 0.07 | 385 |
| loop | 11 % → 2 % | 14.3 px | 0.64 | 0.16 | 203 |
| tilted | 6 % → 6 % | 17.9 px | 0.64 | 0.97 | 110 |
| over the wet one | 12 % → 3 % | 16.3 px | 0.64 | 0.27 | 94 |
| long, no reload | 17 % → 2 % | 7.6 px | 0.64 | 0.10 | 549 | quarters: 0.22 → 0.11 → 0.06 → 0.04

Numbers say: light vs heavy: width 13.6 → 18.9 px, dark 0.64 → 0.64.

## Brush Artist · Refs · #13 Henry Ward blue streaky form
Gouache 1.00 · 50 px · 37.8 s

![Brush Artist · Refs · #13 Henry Ward blue streaky form](Brush-Artist-Refs-13-Henry-Ward-blue-streaky-form.png)

A light paint: laid on a grey sheet (on white it cannot be seen); **dark** = how far it is from the grey either way.

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 15 % → 9 % | 42.1 px | 0.33 | 0.61 | 168 |
| heavy line | 16 % → 10 % | 45.9 px | 0.33 | 0.63 | 176 |
| pressure swell | 12 % → 8 % | 46.0 px | 0.33 | 0.68 | 123 |
| fast wave | 32 % → 9 % | 37.1 px | 0.33 | 0.28 | 425 |
| slow wave | 36 % → 13 % | 42.2 px | 0.33 | 0.36 | 812 |
| spiral | 44 % → 12 % | 29.1 px | 0.33 | 0.27 | 812 |
| loop | 30 % → 12 % | 39.3 px | 0.33 | 0.41 | 654 |
| tilted | 13 % → 13 % | 37.1 px | 0.33 | 1.00 | 381 |
| over the wet one | 27 % → 20 % | 39.6 px | 0.33 | 0.74 | 187 |
| long, no reload | 47 % → 15 % | 21.1 px | 0.33 | 0.32 | 1100 | quarters: 0.01 → 0.02 → 0.03 → 0.03

Numbers say: light vs heavy: width 42.1 → 45.9 px, dark 0.33 → 0.33; pressure barely changes the width; the long stroke does not run out of paint.

## Brush Artist · Refs · #14 Henry Ward olive totem
Impasto 1.00 · 48 px · 21.7 s

![Brush Artist · Refs · #14 Henry Ward olive totem](Brush-Artist-Refs-14-Henry-Ward-olive-totem.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 15 % → 15 % | 44.9 px | 0.31 | 0.95 | 148 |
| heavy line | 16 % → 16 % | 47.8 px | 0.31 | 0.95 | 160 |
| pressure swell | 13 % → 12 % | 47.1 px | 0.32 | 0.95 | 116 |
| fast wave | 38 % → 30 % | 44.0 px | 0.30 | 0.78 | 422 |
| slow wave | 39 % → 31 % | 44.6 px | 0.30 | 0.81 | 704 |
| spiral | 58 % → 32 % | 38.1 px | 0.30 | 0.55 | 1186 |
| loop | 33 % → 29 % | 42.7 px | 0.30 | 0.89 | 693 |
| tilted | 13 % → 13 % | 37.5 px | 0.31 | 1.00 | 303 |
| over the wet one | 28 % → 26 % | 41.3 px | 0.31 | 0.93 | 146 |
| long, no reload | 67 % → 33 % | 30.1 px | 0.30 | 0.49 | 960 | quarters: 0.25 → 0.18 → 0.09 → 0.03

Numbers say: light vs heavy: width 44.9 → 47.8 px, dark 0.31 → 0.31; pressure barely changes the width.

## Brush Artist · Refs · #15 Ultramarine brush script
Ink 1.00 · 4 px · 21.7 s

![Brush Artist · Refs · #15 Ultramarine brush script](Brush-Artist-Refs-15-Ultramarine-brush-script.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 1 % → 3 % | 2.2 px | 0.55 | 3.90 | 30 |
| heavy line | 6 % → 6 % | 16.7 px | 0.58 | 0.99 | 49 |
| pressure swell | 3 % → 4 % | 12.1 px | 0.64 | 1.15 | 29 |
| fast wave | 9 % → 7 % | 10.6 px | 0.54 | 0.81 | 111 |
| slow wave | 7 % → 7 % | 8.4 px | 0.54 | 0.93 | 95 |
| spiral | 11 % → 7 % | 7.2 px | 0.52 | 0.66 | 162 |
| loop | 7 % → 7 % | 9.2 px | 0.53 | 0.98 | 83 |
| tilted | 3 % → 3 % | 8.2 px | 0.62 | 1.02 | 46 |
| over the wet one | 7 % → 7 % | 11.5 px | 0.62 | 1.06 | 38 |
| long, no reload | 16 % → 8 % | 7.3 px | 0.50 | 0.48 | 247 | quarters: 0.15 → 0.04 → 0.01 → 0.00

Numbers say: light vs heavy: width 2.2 → 16.7 px, dark 0.55 → 0.58; wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #18 Blue oil-stick scribbles
Pastel 1.00 · 10 px · 10.6 s

![Brush Artist · Refs · #18 Blue oil-stick scribbles](Brush-Artist-Refs-18-Blue-oil-stick-scribbles.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 1 % → 1 % | 2.9 px | 0.52 | 1.00 | 34 |
| heavy line | 2 % → 2 % | 5.5 px | 0.53 | 1.00 | 27 |
| pressure swell | 1 % → 1 % | 5.0 px | 0.53 | 1.00 | 18 |
| fast wave | 4 % → 4 % | 4.8 px | 0.53 | 1.00 | 70 |
| slow wave | 4 % → 4 % | 4.4 px | 0.53 | 1.00 | 60 |
| spiral | 7 % → 7 % | 4.5 px | 0.52 | 1.00 | 109 |
| loop | 3 % → 3 % | 4.5 px | 0.52 | 1.00 | 55 |
| tilted | 2 % → 2 % | 4.8 px | 0.53 | 1.00 | 51 |
| over the wet one | 3 % → 3 % | 4.7 px | 0.53 | 1.00 | 44 |
| long, no reload | 10 % → 10 % | 4.4 px | 0.53 | 1.00 | 192 | quarters: 0.06 → 0.06 → 0.06 → 0.06

Numbers say: light vs heavy: width 2.9 → 5.5 px, dark 0.52 → 0.53; the long stroke does not run out of paint.

## Brush Artist · Refs · #20 Orange-red crayon scribble
Pastel 1.00 · 14 px · 11.0 s

![Brush Artist · Refs · #20 Orange-red crayon scribble](Brush-Artist-Refs-20-Orange-red-crayon-scribble.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 1 % → 1 % | 4.0 px | 0.53 | 1.00 | 27 |
| heavy line | 3 % → 3 % | 8.0 px | 0.53 | 1.00 | 30 |
| pressure swell | 2 % → 2 % | 7.6 px | 0.53 | 1.00 | 26 |
| fast wave | 6 % → 6 % | 7.2 px | 0.53 | 1.00 | 76 |
| slow wave | 6 % → 6 % | 6.6 px | 0.53 | 1.00 | 75 |
| spiral | 9 % → 9 % | 6.2 px | 0.53 | 1.00 | 118 |
| loop | 5 % → 5 % | 6.2 px | 0.53 | 1.00 | 64 |
| tilted | 2 % → 2 % | 5.6 px | 0.53 | 1.00 | 46 |
| over the wet one | 4 % → 4 % | 6.6 px | 0.53 | 1.00 | 35 |
| long, no reload | 13 % → 13 % | 5.7 px | 0.53 | 1.00 | 278 | quarters: 0.07 → 0.07 → 0.08 → 0.08

Numbers say: light vs heavy: width 4.0 → 8.0 px, dark 0.53 → 0.53; the long stroke does not run out of paint.

## Brush Artist · Refs · #21 Gritty black contours
Gouache 1.00 · 12 px · 19.3 s

![Brush Artist · Refs · #21 Gritty black contours](Brush-Artist-Refs-21-Gritty-black-contours.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 1 % → 0 % | 3.9 px | 0.00 | 0.00 | 82 |
| heavy line | 2 % → 0 % | 6.4 px | 0.00 | 0.00 | 121 |
| pressure swell | 2 % → 0 % | 6.5 px | 0.81 | 0.02 | 68 |
| fast wave | 3 % → 0 % | 3.2 px | 0.00 | 0.00 | 219 |
| slow wave | 4 % → 0 % | 4.4 px | 0.81 | 0.02 | 213 |
| spiral | 4 % → 0 % | 3.0 px | 0.81 | 0.01 | 362 |
| loop | 4 % → 0 % | 4.6 px | 0.81 | 0.00 | 221 |
| tilted | 2 % → 2 % | 6.3 px | 0.81 | 0.88 | 134 |
| over the wet one | 4 % → 0 % | 5.3 px | 0.81 | 0.05 | 102 |
| long, no reload | 5 % → 0 % | 2.2 px | 0.81 | 0.02 | 565 | quarters: 0.10 → 0.04 → 0.03 → 0.02

Numbers say: light vs heavy: width 3.9 → 6.4 px, dark 0.00 → 0.00.

## Brush Artist · Refs · #22 Bold black brush poster
Ink 1.00 · 20 px · 28.3 s

![Brush Artist · Refs · #22 Bold black brush poster](Brush-Artist-Refs-22-Bold-black-brush-poster.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 3 % → 5 % | 9.6 px | 0.79 | 1.64 | 42 |
| heavy line | 15 % → 15 % | 44.6 px | 0.88 | 0.99 | 87 |
| pressure swell | 9 % → 9 % | 31.9 px | 0.87 | 1.04 | 61 |
| fast wave | 27 % → 27 % | 31.7 px | 0.87 | 0.98 | 205 |
| slow wave | 22 % → 22 % | 25.3 px | 0.87 | 0.99 | 227 |
| spiral | 34 % → 32 % | 22.4 px | 0.87 | 0.94 | 276 |
| loop | 20 % → 20 % | 26.3 px | 0.88 | 1.00 | 227 |
| tilted | 8 % → 8 % | 23.1 px | 0.88 | 1.01 | 67 |
| over the wet one | 19 % → 19 % | 30.3 px | 0.88 | 1.00 | 69 |
| long, no reload | 45 % → 38 % | 20.3 px | 0.86 | 0.83 | 454 | quarters: 0.54 → 0.45 → 0.35 → 0.26

Numbers say: light vs heavy: width 9.6 → 44.6 px, dark 0.79 → 0.88; wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #23 Dry white on orange + black line
Gouache 1.00 · 50 px · 22.3 s

![Brush Artist · Refs · #23 Dry white on orange + black line](Brush-Artist-Refs-23-Dry-white-on-orange-black-line.png)

A light paint: laid on a grey sheet (on white it cannot be seen); **dark** = how far it is from the grey either way.

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 6 % → 0 % | 18.3 px | 0.00 | 0.00 | 113 |
| heavy line | 11 % → 0 % | 31.4 px | 0.41 | 0.00 | 233 |
| pressure swell | 8 % → 0 % | 28.6 px | 0.41 | 0.01 | 134 |
| fast wave | 13 % → 0 % | 15.6 px | 0.40 | 0.01 | 363 |
| slow wave | 21 % → 0 % | 24.0 px | 0.40 | 0.01 | 673 |
| spiral | 24 % → 0 % | 15.9 px | 0.40 | 0.01 | 669 |
| loop | 18 % → 1 % | 22.7 px | 0.40 | 0.03 | 326 |
| tilted | 8 % → 8 % | 22.8 px | 0.40 | 0.95 | 194 |
| over the wet one | 17 % → 1 % | 25.1 px | 0.40 | 0.08 | 161 |
| long, no reload | 25 % → 1 % | 11.2 px | 0.40 | 0.03 | 1247 | quarters: 0.02 → 0.03 → 0.03 → 0.03

Numbers say: light vs heavy: width 18.3 → 31.4 px, dark 0.00 → 0.41; the long stroke does not run out of paint.

## Brush Artist · Refs · #24 Picasso flat oil
Oil 0.89 · Oil glaze 0.11 · 34 px · 15.7 s

![Brush Artist · Refs · #24 Picasso flat oil](Brush-Artist-Refs-24-Picasso-flat-oil.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 11 % → 11 % | 32.4 px | 0.40 | 1.00 | 147 |
| heavy line | 12 % → 12 % | 35.2 px | 0.39 | 1.00 | 126 |
| pressure swell | 9 % → 9 % | 34.5 px | 0.41 | 1.00 | 117 |
| fast wave | 30 % → 30 % | 34.2 px | 0.41 | 1.00 | 348 |
| slow wave | 30 % → 30 % | 35.0 px | 0.41 | 1.00 | 614 |
| spiral | 51 % → 51 % | 33.8 px | 0.39 | 1.00 | 555 |
| loop | 25 % → 25 % | 32.6 px | 0.40 | 1.00 | 289 |
| tilted | 11 % → 11 % | 32.1 px | 0.40 | 1.00 | 155 |
| over the wet one | 23 % → 23 % | 30.8 px | 0.40 | 1.00 | 131 |
| long, no reload | 62 % → 62 % | 27.6 px | 0.39 | 1.00 | 792 | quarters: 0.28 → 0.27 → 0.26 → 0.24

Numbers say: light vs heavy: width 32.4 → 35.2 px, dark 0.40 → 0.39; pressure barely changes the width.

## Brush Artist · Refs · #25 Yellow heavy flat stroke
Impasto 1.00 · 110 px · 38.6 s

![Brush Artist · Refs · #25 Yellow heavy flat stroke](Brush-Artist-Refs-25-Yellow-heavy-flat-stroke.png)

A light paint: laid on a grey sheet (on white it cannot be seen); **dark** = how far it is from the grey either way.

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 35 % → 36 % | 101.5 px | 0.30 | 1.02 | 496 |
| heavy line | 36 % → 35 % | 105.1 px | 0.31 | 0.97 | 384 |
| pressure swell | 28 % → 29 % | 105.5 px | 0.30 | 1.04 | 281 |
| fast wave | 73 % → 76 % | 83.8 px | 0.31 | 1.05 | 1362 |
| slow wave | 73 % → 72 % | 84.7 px | 0.30 | 0.98 | 1869 |
| spiral | 86 % → 83 % | 56.7 px | 0.29 | 0.97 | 1864 |
| loop | 65 % → 64 % | 83.6 px | 0.31 | 0.99 | 916 |
| tilted | 26 % → 26 % | 71.5 px | 0.30 | 1.00 | 620 |
| over the wet one | 55 % → 54 % | 83.2 px | 0.30 | 0.97 | 405 |
| long, no reload | 98 % → 97 % | 44.1 px | 0.30 | 0.99 | 4217 | quarters: 0.00 → 0.00 → 0.00 → 0.00

Numbers say: light vs heavy: width 101.5 → 105.1 px, dark 0.30 → 0.31; pressure barely changes the width; the long stroke does not run out of paint.

## Brush Artist · Refs · #27 Orange impasto swatch
Impasto 1.00 · 60 px · 24.0 s

![Brush Artist · Refs · #27 Orange impasto swatch](Brush-Artist-Refs-27-Orange-impasto-swatch.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 20 % → 19 % | 56.9 px | 0.34 | 0.97 | 194 |
| heavy line | 20 % → 20 % | 59.5 px | 0.34 | 0.97 | 178 |
| pressure swell | 16 % → 15 % | 59.6 px | 0.36 | 0.97 | 126 |
| fast wave | 48 % → 47 % | 55.1 px | 0.35 | 0.98 | 802 |
| slow wave | 48 % → 47 % | 55.9 px | 0.35 | 0.98 | 899 |
| spiral | 69 % → 62 % | 45.5 px | 0.34 | 0.91 | 831 |
| loop | 42 % → 40 % | 53.9 px | 0.35 | 0.97 | 448 |
| tilted | 16 % → 16 % | 44.0 px | 0.35 | 1.00 | 212 |
| over the wet one | 34 % → 33 % | 50.9 px | 0.35 | 0.96 | 196 |
| long, no reload | 85 % → 75 % | 38.1 px | 0.35 | 0.88 | 1214 | quarters: 0.33 → 0.31 → 0.30 → 0.26

Numbers say: light vs heavy: width 56.9 → 59.5 px, dark 0.34 → 0.34; pressure barely changes the width.

## Brush Artist · Refs · #28 Miles Davis black lines
Ink 1.00 · 22 px · 30.8 s

![Brush Artist · Refs · #28 Miles Davis black lines](Brush-Artist-Refs-28-Miles-Davis-black-lines.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 4 % → 6 % | 12.2 px | 0.81 | 1.49 | 48 |
| heavy line | 17 % → 17 % | 49.0 px | 0.88 | 0.99 | 87 |
| pressure swell | 10 % → 10 % | 35.9 px | 0.87 | 1.03 | 50 |
| fast wave | 31 % → 30 % | 35.4 px | 0.87 | 0.98 | 149 |
| slow wave | 25 % → 25 % | 28.7 px | 0.87 | 0.99 | 234 |
| spiral | 39 % → 37 % | 25.5 px | 0.87 | 0.95 | 273 |
| loop | 23 % → 23 % | 29.6 px | 0.88 | 1.00 | 210 |
| tilted | 9 % → 9 % | 25.3 px | 0.88 | 1.01 | 66 |
| over the wet one | 21 % → 21 % | 34.1 px | 0.88 | 1.01 | 60 |
| long, no reload | 51 % → 43 % | 22.9 px | 0.86 | 0.84 | 618 | quarters: 0.59 → 0.51 → 0.40 → 0.31

Numbers say: light vs heavy: width 12.2 → 49.0 px, dark 0.81 → 0.88.

## Brush Artist · Refs · #29 Shrigley magenta asterisk
Watercolour 1.00 · 70 px · 34.2 s

![Brush Artist · Refs · #29 Shrigley magenta asterisk](Brush-Artist-Refs-29-Shrigley-magenta-asterisk.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 10 % → 13 % | 28.0 px | 0.61 | 1.39 | 59 |
| heavy line | 17 % → 18 % | 50.3 px | 0.61 | 1.04 | 137 |
| pressure swell | 11 % → 13 % | 41.1 px | 0.62 | 1.14 | 80 |
| fast wave | 38 % → 38 % | 43.8 px | 0.60 | 1.01 | 324 |
| slow wave | 35 % → 39 % | 41.0 px | 0.62 | 1.11 | 482 |
| spiral | 61 % → 61 % | 40.0 px | 0.60 | 1.01 | 415 |
| loop | 31 % → 32 % | 40.2 px | 0.61 | 1.03 | 243 |
| tilted | 18 % → 18 % | 49.0 px | 0.61 | 1.00 | 239 |
| over the wet one | 31 % → 34 % | 38.5 px | 0.61 | 1.08 | 143 |
| long, no reload | 75 % → 76 % | 33.6 px | 0.60 | 1.01 | 654 | quarters: 0.53 → 0.50 → 0.48 → 0.45

Numbers say: light vs heavy: width 28.0 → 50.3 px, dark 0.61 → 0.61; the long stroke does not run out of paint.

## Brush Artist · Refs · #30 Red gouache face patch
Gouache 1.00 · 60 px · 41.7 s

![Brush Artist · Refs · #30 Red gouache face patch](Brush-Artist-Refs-30-Red-gouache-face-patch.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 16 % → 15 % | 47.0 px | 0.49 | 0.91 | 145 |
| heavy line | 25 % → 20 % | 73.9 px | 0.49 | 0.80 | 235 |
| pressure swell | 19 % → 17 % | 72.6 px | 0.49 | 0.86 | 147 |
| fast wave | 49 % → 28 % | 56.1 px | 0.49 | 0.58 | 519 |
| slow wave | 48 % → 28 % | 55.4 px | 0.49 | 0.59 | 774 |
| spiral | 60 % → 28 % | 39.3 px | 0.49 | 0.47 | 851 |
| loop | 40 % → 29 % | 51.6 px | 0.49 | 0.74 | 397 |
| tilted | 16 % → 17 % | 46.0 px | 0.49 | 1.00 | 254 |
| over the wet one | 36 % → 32 % | 55.3 px | 0.49 | 0.89 | 218 |
| long, no reload | 67 % → 30 % | 30.0 px | 0.49 | 0.44 | 1018 | quarters: 0.43 → 0.39 → 0.32 → 0.26

Numbers say: light vs heavy: width 47.0 → 73.9 px, dark 0.49 → 0.49.

## Brush Artist · Refs · #31 Warhol blotted line
Ink 1.00 · 6 px · 23.1 s

![Brush Artist · Refs · #31 Warhol blotted line](Brush-Artist-Refs-31-Warhol-blotted-line.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 1 % → 3 % | 2.7 px | 0.75 | 3.31 | 33 |
| heavy line | 7 % → 7 % | 20.7 px | 0.83 | 0.98 | 78 |
| pressure swell | 4 % → 4 % | 14.8 px | 0.84 | 1.12 | 39 |
| fast wave | 12 % → 9 % | 13.9 px | 0.82 | 0.76 | 134 |
| slow wave | 10 % → 8 % | 11.2 px | 0.80 | 0.84 | 118 |
| spiral | 15 % → 8 % | 9.7 px | 0.80 | 0.58 | 194 |
| loop | 9 % → 9 % | 11.9 px | 0.80 | 0.93 | 116 |
| tilted | 3 % → 3 % | 8.8 px | 0.84 | 1.03 | 72 |
| over the wet one | 8 % → 8 % | 14.4 px | 0.84 | 1.02 | 83 |
| long, no reload | 21 % → 9 % | 9.5 px | 0.78 | 0.43 | 290 | quarters: 0.25 → 0.13 → 0.04 → 0.01

Numbers say: light vs heavy: width 2.7 → 20.7 px, dark 0.75 → 0.83; wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #32 Thick orange swipes
Impasto 1.00 · 90 px · 36.4 s

![Brush Artist · Refs · #32 Thick orange swipes](Brush-Artist-Refs-32-Thick-orange-swipes.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 29 % → 29 % | 83.2 px | 0.37 | 1.00 | 402 |
| heavy line | 30 % → 29 % | 86.5 px | 0.38 | 0.97 | 333 |
| pressure swell | 23 % → 23 % | 86.6 px | 0.38 | 1.01 | 241 |
| fast wave | 63 % → 65 % | 73.1 px | 0.38 | 1.03 | 857 |
| slow wave | 64 % → 63 % | 73.5 px | 0.38 | 0.98 | 1742 |
| spiral | 79 % → 77 % | 52.2 px | 0.38 | 0.98 | 1583 |
| loop | 57 % → 56 % | 73.4 px | 0.38 | 0.99 | 1048 |
| tilted | 21 % → 21 % | 59.3 px | 0.38 | 1.00 | 487 |
| over the wet one | 47 % → 45 % | 71.0 px | 0.38 | 0.97 | 372 |
| long, no reload | 95 % → 93 % | 42.8 px | 0.38 | 0.98 | 2148 | quarters: 0.38 → 0.38 → 0.37 → 0.35

Numbers say: light vs heavy: width 83.2 → 86.5 px, dark 0.37 → 0.38; pressure barely changes the width; the long stroke does not run out of paint.

## Brush Artist · Refs · #33 Red wet-in-wet band
Watercolour 1.00 · 80 px · 56.4 s

![Brush Artist · Refs · #33 Red wet-in-wet band](Brush-Artist-Refs-33-Red-wet-in-wet-band.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 24 % → 42 % | 69.9 px | 0.53 | 1.73 | 152 |
| heavy line | 34 % → 50 % | 97.7 px | 0.54 | 1.48 | 259 |
| pressure swell | 20 % → 30 % | 73.7 px | 0.57 | 1.54 | 170 |
| fast wave | 65 % → 80 % | 75.4 px | 0.61 | 1.22 | 581 |
| slow wave | 61 % → 78 % | 70.0 px | 0.63 | 1.29 | 1158 |
| spiral | 78 % → 89 % | 51.5 px | 0.64 | 1.15 | 904 |
| loop | 54 % → 68 % | 70.2 px | 0.62 | 1.25 | 427 |
| tilted | 28 % → 30 % | 77.1 px | 0.57 | 1.08 | 361 |
| over the wet one | 55 % → 79 % | 75.2 px | 0.57 | 1.45 | 202 |
| long, no reload | 96 % → 99 % | 43.2 px | 0.66 | 1.03 | 1310 | quarters: 0.68 → 0.68 → 0.68 → 0.63

Numbers say: light vs heavy: width 69.9 → 97.7 px, dark 0.53 → 0.54; the long stroke does not run out of paint; wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #34 Magenta oil patches
Oil 0.89 · Oil glaze 0.11 · 60 px · 27.2 s

![Brush Artist · Refs · #34 Magenta oil patches](Brush-Artist-Refs-34-Magenta-oil-patches.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 19 % → 19 % | 55.9 px | 0.61 | 1.00 | 244 |
| heavy line | 21 % → 21 % | 59.9 px | 0.61 | 1.00 | 539 |
| pressure swell | 16 % → 16 % | 58.9 px | 0.62 | 1.01 | 158 |
| fast wave | 48 % → 49 % | 55.4 px | 0.62 | 1.02 | 550 |
| slow wave | 48 % → 48 % | 55.8 px | 0.62 | 1.00 | 1042 |
| spiral | 70 % → 70 % | 46.3 px | 0.62 | 1.00 | 1247 |
| loop | 42 % → 42 % | 54.3 px | 0.62 | 1.00 | 1016 |
| tilted | 17 % → 17 % | 46.9 px | 0.61 | 1.00 | 356 |
| over the wet one | 35 % → 35 % | 50.1 px | 0.61 | 1.00 | 250 |
| long, no reload | 86 % → 86 % | 38.7 px | 0.62 | 1.00 | 1679 | quarters: 0.59 → 0.58 → 0.57 → 0.52

Numbers say: light vs heavy: width 55.9 → 59.9 px, dark 0.61 → 0.61; pressure barely changes the width; the long stroke does not run out of paint.

## Brush Artist · Refs · #35 Red band with runs
Watercolour 1.00 · 70 px · 57.9 s

![Brush Artist · Refs · #35 Red band with runs](Brush-Artist-Refs-35-Red-band-with-runs.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 40 % → 45 % | 115.4 px | 0.42 | 1.14 | 169 |
| heavy line | 46 % → 51 % | 133.2 px | 0.42 | 1.12 | 289 |
| pressure swell | 21 % → 28 % | 77.8 px | 0.48 | 1.36 | 171 |
| fast wave | 67 % → 77 % | 77.5 px | 0.49 | 1.14 | 733 |
| slow wave | 65 % → 75 % | 75.0 px | 0.52 | 1.16 | 1077 |
| spiral | 87 % → 94 % | 57.4 px | 0.53 | 1.09 | 806 |
| loop | 79 % → 88 % | 102.3 px | 0.48 | 1.11 | 418 |
| tilted | 50 % → 50 % | 138.2 px | 0.47 | 1.02 | 279 |
| over the wet one | 77 % → 84 % | 76.2 px | 0.47 | 1.10 | 242 |
| long, no reload | 97 % → 100 % | 43.5 px | 0.58 | 1.03 | 1361 | quarters: 0.60 → 0.60 → 0.59 → 0.56

Numbers say: light vs heavy: width 115.4 → 133.2 px, dark 0.42 → 0.42; the long stroke does not run out of paint.

## Brush Artist · Refs · #36 Magenta letters flat brush
Gouache 1.00 · 36 px · 38.2 s

![Brush Artist · Refs · #36 Magenta letters flat brush](Brush-Artist-Refs-36-Magenta-letters-flat-brush.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 10 % → 10 % | 29.0 px | 0.45 | 0.98 | 84 |
| heavy line | 17 % → 14 % | 49.0 px | 0.45 | 0.85 | 119 |
| pressure swell | 13 % → 12 % | 49.3 px | 0.45 | 0.89 | 76 |
| fast wave | 35 % → 19 % | 40.9 px | 0.45 | 0.54 | 250 |
| slow wave | 35 % → 19 % | 40.0 px | 0.45 | 0.54 | 426 |
| spiral | 46 % → 19 % | 30.4 px | 0.45 | 0.42 | 456 |
| loop | 27 % → 20 % | 35.4 px | 0.45 | 0.72 | 245 |
| tilted | 11 % → 11 % | 30.0 px | 0.45 | 1.00 | 158 |
| over the wet one | 24 % → 23 % | 38.1 px | 0.45 | 0.93 | 111 |
| long, no reload | 46 % → 19 % | 20.8 px | 0.45 | 0.40 | 681 | quarters: 0.29 → 0.26 → 0.22 → 0.18

Numbers say: light vs heavy: width 29.0 → 49.0 px, dark 0.45 → 0.45.

## Brush Artist · Refs · #37 Oil still life dabs
Oil 0.89 · Oil glaze 0.11 · 40 px · 18.6 s

![Brush Artist · Refs · #37 Oil still life dabs](Brush-Artist-Refs-37-Oil-still-life-dabs.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 13 % → 13 % | 38.0 px | 0.38 | 1.00 | 159 |
| heavy line | 14 % → 14 % | 41.1 px | 0.38 | 1.00 | 181 |
| pressure swell | 11 % → 11 % | 40.2 px | 0.40 | 1.00 | 134 |
| fast wave | 34 % → 35 % | 39.9 px | 0.39 | 1.00 | 428 |
| slow wave | 35 % → 35 % | 40.2 px | 0.39 | 1.00 | 806 |
| spiral | 59 % → 59 % | 38.7 px | 0.38 | 1.00 | 744 |
| loop | 29 % → 29 % | 37.8 px | 0.39 | 1.00 | 426 |
| tilted | 13 % → 13 % | 36.3 px | 0.39 | 1.00 | 228 |
| over the wet one | 26 % → 26 % | 35.8 px | 0.39 | 1.00 | 270 |
| long, no reload | 69 % → 69 % | 30.9 px | 0.37 | 1.00 | 1467 | quarters: 0.31 → 0.30 → 0.27 → 0.24

Numbers say: light vs heavy: width 38.0 → 41.1 px, dark 0.38 → 0.38; pressure barely changes the width.

## Brush Artist · Refs · #38 Sanguine drawing
Pastel 1.00 · 6 px · 11.0 s

![Brush Artist · Refs · #38 Sanguine drawing](Brush-Artist-Refs-38-Sanguine-drawing.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 1 % → 1 % | 2.0 px | 0.61 | 1.00 | 54 |
| heavy line | 1 % → 1 % | 3.5 px | 0.62 | 1.00 | 25 |
| pressure swell | 1 % → 1 % | 3.3 px | 0.62 | 1.00 | 16 |
| fast wave | 3 % → 3 % | 3.2 px | 0.61 | 1.00 | 43 |
| slow wave | 3 % → 3 % | 3.0 px | 0.61 | 1.00 | 44 |
| spiral | 4 % → 4 % | 2.9 px | 0.61 | 1.00 | 81 |
| loop | 2 % → 2 % | 3.0 px | 0.61 | 1.00 | 82 |
| tilted | 1 % → 1 % | 3.4 px | 0.62 | 1.00 | 27 |
| over the wet one | 2 % → 2 % | 2.9 px | 0.62 | 1.00 | 18 |
| long, no reload | 7 % → 7 % | 3.0 px | 0.61 | 1.00 | 127 | quarters: 0.04 → 0.05 → 0.05 → 0.05

Numbers say: light vs heavy: width 2.0 → 3.5 px, dark 0.61 → 0.62; the long stroke does not run out of paint.

## Brush Artist · Refs · #39 Very thick impasto
Impasto 1.00 · 60 px · 26.9 s

![Brush Artist · Refs · #39 Very thick impasto](Brush-Artist-Refs-39-Very-thick-impasto.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 20 % → 19 % | 57.0 px | 0.60 | 0.97 | 193 |
| heavy line | 21 % → 20 % | 59.6 px | 0.60 | 0.97 | 298 |
| pressure swell | 16 % → 15 % | 59.7 px | 0.63 | 0.97 | 222 |
| fast wave | 48 % → 47 % | 55.2 px | 0.62 | 0.98 | 527 |
| slow wave | 49 % → 47 % | 56.1 px | 0.62 | 0.98 | 1053 |
| spiral | 69 % → 65 % | 45.6 px | 0.62 | 0.93 | 1179 |
| loop | 42 % → 41 % | 54.0 px | 0.62 | 0.97 | 516 |
| tilted | 16 % → 16 % | 44.1 px | 0.61 | 1.00 | 326 |
| over the wet one | 34 % → 33 % | 51.0 px | 0.61 | 0.97 | 221 |
| long, no reload | 85 % → 79 % | 38.3 px | 0.62 | 0.93 | 1266 | quarters: 0.58 → 0.57 → 0.55 → 0.52

Numbers say: light vs heavy: width 57.0 → 59.6 px, dark 0.60 → 0.60; pressure barely changes the width; the long stroke does not run out of paint.

## Brush Artist · Refs · #40 Watercolour blooms
Watercolour 1.00 · 90 px · 59.6 s

![Brush Artist · Refs · #40 Watercolour blooms](Brush-Artist-Refs-40-Watercolour-blooms.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 27 % → 46 % | 79.5 px | 0.08 | 1.69 | 301 |
| heavy line | 39 % → 53 % | 112.7 px | 0.09 | 1.36 | 336 |
| pressure swell | 26 % → 40 % | 98.0 px | 0.09 | 1.54 | 171 |
| fast wave | 68 % → 82 % | 78.6 px | 0.11 | 1.21 | 730 |
| slow wave | 68 % → 81 % | 78.9 px | 0.15 | 1.19 | 1040 |
| spiral | 83 % → 93 % | 54.4 px | 0.15 | 1.13 | 2052 |
| loop | 59 % → 72 % | 75.9 px | 0.13 | 1.24 | 849 |
| tilted | 33 % → 36 % | 93.0 px | 0.12 | 1.07 | 378 |
| over the wet one | 61 % → 81 % | 77.1 px | 0.12 | 1.33 | 251 |
| long, no reload | 98 % → 100 % | 43.9 px | 0.17 | 1.02 | 1580 | quarters: 0.21 → 0.20 → 0.17 → 0.12

Numbers say: light vs heavy: width 79.5 → 112.7 px, dark 0.08 → 0.09; wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #41 Coloured pencil hatching
Pastel 1.00 · 4 px · 11.6 s

![Brush Artist · Refs · #41 Coloured pencil hatching](Brush-Artist-Refs-41-Coloured-pencil-hatching.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 1 % → 1 % | 1.6 px | 0.42 | 1.00 | 12 |
| heavy line | 1 % → 1 % | 2.6 px | 0.43 | 1.00 | 13 |
| pressure swell | 1 % → 1 % | 2.1 px | 0.43 | 1.00 | 14 |
| fast wave | 2 % → 2 % | 2.2 px | 0.42 | 1.00 | 54 |
| slow wave | 2 % → 2 % | 2.1 px | 0.43 | 1.00 | 43 |
| spiral | 3 % → 3 % | 2.1 px | 0.43 | 1.00 | 110 |
| loop | 2 % → 2 % | 2.2 px | 0.43 | 1.00 | 85 |
| tilted | 1 % → 1 % | 3.0 px | 0.42 | 1.00 | 30 |
| over the wet one | 2 % → 2 % | 2.2 px | 0.42 | 1.00 | 24 |
| long, no reload | 5 % → 5 % | 2.3 px | 0.43 | 1.00 | 149 | quarters: 0.02 → 0.02 → 0.02 → 0.03

Numbers say: light vs heavy: width 1.6 → 2.6 px, dark 0.42 → 0.43; the long stroke does not run out of paint.

## Brush Artist · Refs · #42 Oil pastel shaggy
Pastel 1.00 · 18 px · 11.6 s

![Brush Artist · Refs · #42 Oil pastel shaggy](Brush-Artist-Refs-42-Oil-pastel-shaggy.png)

A light paint: laid on a grey sheet (on white it cannot be seen); **dark** = how far it is from the grey either way.

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 2 % → 2 % | 5.1 px | 0.35 | 1.00 | 35 |
| heavy line | 4 % → 4 % | 10.7 px | 0.36 | 1.00 | 30 |
| pressure swell | 3 % → 3 % | 9.5 px | 0.36 | 1.00 | 22 |
| fast wave | 8 % → 8 % | 9.0 px | 0.36 | 1.00 | 74 |
| slow wave | 7 % → 7 % | 8.2 px | 0.36 | 1.00 | 133 |
| spiral | 12 % → 12 % | 7.8 px | 0.36 | 1.00 | 350 |
| loop | 6 % → 6 % | 7.9 px | 0.36 | 1.00 | 122 |
| tilted | 2 % → 2 % | 6.9 px | 0.36 | 1.00 | 37 |
| over the wet one | 6 % → 6 % | 8.5 px | 0.36 | 1.00 | 32 |
| long, no reload | 15 % → 15 % | 6.9 px | 0.36 | 1.00 | 192 | quarters: 0.00 → 0.00 → 0.00 → 0.00

Numbers say: light vs heavy: width 5.1 → 10.7 px, dark 0.35 → 0.36; the long stroke does not run out of paint.

## Brush Artist · Refs · #43 Dragged black ink blocks
Gouache 1.00 · 70 px · 30.2 s

![Brush Artist · Refs · #43 Dragged black ink blocks](Brush-Artist-Refs-43-Dragged-black-ink-blocks.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 12 % → 1 % | 34.2 px | 0.65 | 0.09 | 145 |
| heavy line | 17 % → 2 % | 50.0 px | 0.65 | 0.12 | 675 |
| pressure swell | 12 % → 3 % | 46.4 px | 0.65 | 0.23 | 193 |
| fast wave | 25 % → 3 % | 29.3 px | 0.65 | 0.11 | 560 |
| slow wave | 34 % → 4 % | 39.6 px | 0.65 | 0.12 | 1048 |
| spiral | 38 % → 5 % | 25.0 px | 0.65 | 0.12 | 918 |
| loop | 29 % → 4 % | 38.2 px | 0.65 | 0.15 | 496 |
| tilted | 13 % → 13 % | 37.5 px | 0.65 | 0.98 | 340 |
| over the wet one | 28 % → 10 % | 40.5 px | 0.65 | 0.37 | 218 |
| long, no reload | 44 % → 7 % | 19.9 px | 0.65 | 0.16 | 1856 | quarters: 0.48 → 0.36 → 0.27 → 0.18

Numbers say: light vs heavy: width 34.2 → 50.0 px, dark 0.65 → 0.65.

## Brush Artist · Refs · #44 Blue looping ribbon
Oil 1.00 · 80 px · 28.1 s

![Brush Artist · Refs · #44 Blue looping ribbon](Brush-Artist-Refs-44-Blue-looping-ribbon.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 26 % → 27 % | 75.0 px | 0.72 | 1.04 | 303 |
| heavy line | 27 % → 27 % | 79.7 px | 0.72 | 1.00 | 294 |
| pressure swell | 21 % → 22 % | 78.2 px | 0.72 | 1.03 | 212 |
| fast wave | 61 % → 64 % | 70.3 px | 0.73 | 1.05 | 808 |
| slow wave | 61 % → 61 % | 70.0 px | 0.73 | 1.00 | 1500 |
| spiral | 78 % → 78 % | 51.3 px | 0.73 | 1.00 | 1701 |
| loop | 54 % → 54 % | 69.7 px | 0.73 | 1.00 | 769 |
| tilted | 21 % → 21 % | 57.3 px | 0.72 | 1.00 | 384 |
| over the wet one | 44 % → 44 % | 64.9 px | 0.72 | 1.00 | 394 |
| long, no reload | 96 % → 96 % | 42.8 px | 0.73 | 1.00 | 1998 | quarters: 0.72 → 0.73 → 0.73 → 0.69

Numbers say: light vs heavy: width 75.0 → 79.7 px, dark 0.72 → 0.72; pressure barely changes the width; the long stroke does not run out of paint.

## Brush Artist · Refs · #45 Soft pastel pepper
Pastel 1.00 · 40 px · 11.4 s

![Brush Artist · Refs · #45 Soft pastel pepper](Brush-Artist-Refs-45-Soft-pastel-pepper.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 4 % → 4 % | 11.3 px | 0.53 | 1.00 | 49 |
| heavy line | 8 % → 8 % | 23.0 px | 0.53 | 1.00 | 52 |
| pressure swell | 5 % → 5 % | 19.5 px | 0.53 | 1.00 | 39 |
| fast wave | 17 % → 17 % | 19.4 px | 0.53 | 1.00 | 138 |
| slow wave | 15 % → 15 % | 17.1 px | 0.53 | 1.00 | 232 |
| spiral | 25 % → 25 % | 16.3 px | 0.53 | 1.00 | 237 |
| loop | 12 % → 12 % | 16.1 px | 0.53 | 1.00 | 125 |
| tilted | 5 % → 5 % | 12.8 px | 0.53 | 1.00 | 64 |
| over the wet one | 11 % → 11 % | 17.7 px | 0.53 | 1.00 | 53 |
| long, no reload | 30 % → 30 % | 13.6 px | 0.53 | 1.00 | 420 | quarters: 0.18 → 0.18 → 0.18 → 0.18

Numbers say: light vs heavy: width 11.3 → 23.0 px, dark 0.53 → 0.53; the long stroke does not run out of paint.

## Brush Artist · Refs · #46 Red-brown ink lips
Watercolour 1.00 · 50 px · 47.4 s

![Brush Artist · Refs · #46 Red-brown ink lips](Brush-Artist-Refs-46-Red-brown-ink-lips.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 15 % → 31 % | 43.2 px | 0.58 | 2.07 | 76 |
| heavy line | 22 % → 36 % | 62.9 px | 0.60 | 1.64 | 113 |
| pressure swell | 13 % → 22 % | 47.7 px | 0.64 | 1.71 | 111 |
| fast wave | 41 % → 64 % | 47.9 px | 0.64 | 1.55 | 270 |
| slow wave | 41 % → 63 % | 46.9 px | 0.67 | 1.54 | 433 |
| spiral | 65 % → 79 % | 42.7 px | 0.69 | 1.23 | 439 |
| loop | 37 % → 56 % | 47.7 px | 0.66 | 1.51 | 226 |
| tilted | 20 % → 23 % | 56.2 px | 0.60 | 1.12 | 177 |
| over the wet one | 41 % → 63 % | 57.1 px | 0.60 | 1.55 | 108 |
| long, no reload | 80 % → 96 % | 35.8 px | 0.70 | 1.20 | 623 | quarters: 0.71 → 0.71 → 0.70 → 0.65

Numbers say: light vs heavy: width 43.2 → 62.9 px, dark 0.58 → 0.60; the long stroke does not run out of paint; wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #47 Pink knife slabs
Impasto 1.00 · 90 px · 35.0 s

![Brush Artist · Refs · #47 Pink knife slabs](Brush-Artist-Refs-47-Pink-knife-slabs.png)

A light paint: laid on a grey sheet (on white it cannot be seen); **dark** = how far it is from the grey either way.

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 28 % → 27 % | 81.2 px | 0.29 | 0.97 | 278 |
| heavy line | 29 % → 28 % | 83.6 px | 0.29 | 0.97 | 270 |
| pressure swell | 22 % → 22 % | 83.5 px | 0.29 | 1.01 | 161 |
| fast wave | 61 % → 60 % | 70.3 px | 0.28 | 0.99 | 533 |
| slow wave | 61 % → 59 % | 71.0 px | 0.27 | 0.96 | 975 |
| spiral | 76 % → 57 % | 50.1 px | 0.27 | 0.76 | 1038 |
| loop | 55 % → 54 % | 71.7 px | 0.28 | 0.97 | 502 |
| tilted | 21 % → 21 % | 59.3 px | 0.29 | 1.00 | 290 |
| over the wet one | 46 % → 44 % | 68.1 px | 0.29 | 0.96 | 210 |
| long, no reload | 92 % → 76 % | 41.4 px | 0.26 | 0.83 | 1446 | quarters: 0.00 → 0.00 → 0.00 → 0.00

Numbers say: light vs heavy: width 81.2 → 83.6 px, dark 0.29 → 0.29; pressure barely changes the width; the long stroke does not run out of paint.

## Brush Artist · Refs · #48 Black bands with drips
Gouache 1.00 · 70 px · 51.1 s

![Brush Artist · Refs · #48 Black bands with drips](Brush-Artist-Refs-48-Black-bands-with-drips.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 27 % → 24 % | 79.0 px | 0.64 | 0.87 | 212 |
| heavy line | 35 % → 29 % | 102.8 px | 0.64 | 0.82 | 305 |
| pressure swell | 25 % → 22 % | 91.9 px | 0.64 | 0.89 | 184 |
| fast wave | 64 % → 43 % | 74.0 px | 0.64 | 0.67 | 552 |
| slow wave | 61 % → 41 % | 70.7 px | 0.64 | 0.67 | 1232 |
| spiral | 69 % → 39 % | 45.7 px | 0.64 | 0.56 | 1305 |
| loop | 54 % → 42 % | 70.4 px | 0.64 | 0.77 | 552 |
| tilted | 29 % → 29 % | 80.7 px | 0.64 | 1.00 | 324 |
| over the wet one | 58 % → 49 % | 80.4 px | 0.64 | 0.85 | 450 |
| long, no reload | 78 % → 39 % | 34.9 px | 0.64 | 0.50 | 1903 | quarters: 0.61 → 0.57 → 0.51 → 0.42

Numbers say: light vs heavy: width 79.0 → 102.8 px, dark 0.64 → 0.64.

## Brush Artist · Refs · #49 Magenta letters round brush
Ink 1.00 · 30 px · 34.9 s

![Brush Artist · Refs · #49 Magenta letters round brush](Brush-Artist-Refs-49-Magenta-letters-round-brush.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 6 % → 8 % | 17.4 px | 0.50 | 1.29 | 60 |
| heavy line | 21 % → 21 % | 61.9 px | 0.51 | 0.99 | 145 |
| pressure swell | 12 % → 13 % | 46.3 px | 0.52 | 1.02 | 93 |
| fast wave | 39 % → 38 % | 44.8 px | 0.51 | 0.99 | 299 |
| slow wave | 32 % → 31 % | 36.7 px | 0.51 | 0.99 | 332 |
| spiral | 50 % → 49 % | 33.2 px | 0.51 | 0.97 | 341 |
| loop | 29 % → 29 % | 37.8 px | 0.51 | 1.00 | 187 |
| tilted | 11 % → 11 % | 30.9 px | 0.52 | 1.01 | 94 |
| over the wet one | 26 % → 26 % | 42.0 px | 0.52 | 1.01 | 81 |
| long, no reload | 62 % → 56 % | 27.7 px | 0.50 | 0.91 | 499 | quarters: 0.41 → 0.36 → 0.30 → 0.25

Numbers say: light vs heavy: width 17.4 → 61.9 px, dark 0.50 → 0.51.

## Brush Artist · Refs · #50 Thick swipes on photo
Impasto 1.00 · 40 px · 22.0 s

![Brush Artist · Refs · #50 Thick swipes on photo](Brush-Artist-Refs-50-Thick-swipes-on-photo.png)

A light paint: laid on a grey sheet (on white it cannot be seen); **dark** = how far it is from the grey either way.

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 13 % → 13 % | 38.1 px | 0.27 | 0.96 | 193 |
| heavy line | 14 % → 13 % | 40.2 px | 0.27 | 0.96 | 200 |
| pressure swell | 11 % → 10 % | 40.1 px | 0.25 | 0.95 | 105 |
| fast wave | 33 % → 31 % | 38.4 px | 0.25 | 0.93 | 378 |
| slow wave | 34 % → 32 % | 39.1 px | 0.26 | 0.95 | 721 |
| spiral | 58 % → 46 % | 38.5 px | 0.25 | 0.79 | 848 |
| loop | 28 % → 27 % | 36.9 px | 0.26 | 0.95 | 288 |
| tilted | 12 % → 12 % | 34.1 px | 0.26 | 1.00 | 189 |
| over the wet one | 25 % → 24 % | 35.3 px | 0.26 | 0.95 | 147 |
| long, no reload | 66 % → 46 % | 29.5 px | 0.24 | 0.69 | 854 | quarters: 0.00 → 0.00 → 0.00 → 0.00

Numbers say: light vs heavy: width 38.1 → 40.2 px, dark 0.27 → 0.27; pressure barely changes the width; the long stroke does not run out of paint.

## Brush Artist · Refs · Drag #e8b4a8
Gouache 1.00 · 40 px · 24.5 s

![Brush Artist · Refs · Drag #e8b4a8](Brush-Artist-Refs-Drag-e8b4a8.png)

A light paint: laid on a grey sheet (on white it cannot be seen); **dark** = how far it is from the grey either way.

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 4 % → 0 % | 10.5 px | 0.35 | 0.02 | 136 |
| heavy line | 5 % → 0 % | 15.3 px | 0.34 | 0.02 | 191 |
| pressure swell | 4 % → 0 % | 16.3 px | 0.35 | 0.05 | 118 |
| fast wave | 3 % → 0 % | 4.0 px | 0.35 | 0.05 | 319 |
| slow wave | 10 % → 0 % | 11.5 px | 0.34 | 0.03 | 575 |
| spiral | 10 % → 0 % | 6.4 px | 0.35 | 0.04 | 621 |
| loop | 8 % → 1 % | 10.4 px | 0.34 | 0.07 | 355 |
| tilted | 6 % → 5 % | 16.0 px | 0.34 | 0.87 | 189 |
| over the wet one | 10 % → 1 % | 12.3 px | 0.34 | 0.11 | 138 |
| long, no reload | 9 % → 1 % | 4.0 px | 0.34 | 0.09 | 801 | quarters: 0.01 → 0.01 → 0.01 → 0.01

Numbers say: light vs heavy: width 10.5 → 15.3 px, dark 0.35 → 0.34; the long stroke does not run out of paint.

## Brush Artist · Refs · Drag #e8e4e0
Gouache 1.00 · 40 px · 26.4 s

![Brush Artist · Refs · Drag #e8e4e0](Brush-Artist-Refs-Drag-e8e4e0.png)

A light paint: laid on a grey sheet (on white it cannot be seen); **dark** = how far it is from the grey either way.

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 4 % → 0 % | 10.5 px | 0.44 | 0.02 | 129 |
| heavy line | 5 % → 0 % | 15.3 px | 0.43 | 0.02 | 190 |
| pressure swell | 4 % → 0 % | 16.3 px | 0.43 | 0.05 | 129 |
| fast wave | 3 % → 0 % | 4.0 px | 0.44 | 0.05 | 293 |
| slow wave | 10 % → 0 % | 11.5 px | 0.43 | 0.03 | 580 |
| spiral | 10 % → 0 % | 6.4 px | 0.43 | 0.04 | 582 |
| loop | 8 % → 1 % | 10.4 px | 0.42 | 0.07 | 398 |
| tilted | 6 % → 5 % | 16.0 px | 0.42 | 0.87 | 390 |
| over the wet one | 10 % → 1 % | 12.3 px | 0.42 | 0.11 | 185 |
| long, no reload | 9 % → 1 % | 4.0 px | 0.43 | 0.09 | 1001 | quarters: 0.01 → 0.01 → 0.02 → 0.02

Numbers say: light vs heavy: width 10.5 → 15.3 px, dark 0.44 → 0.43; the long stroke does not run out of paint.

## Brush Artist · Refs · Finger
Pastel 1.00 · 36 px · 26.1 s · over bands of wet oil paint and oil pastel in turn (it works on paint already there: look at what it does to the bands; covered counts the bands too)

![Brush Artist · Refs · Finger](Brush-Artist-Refs-Finger.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 25 % → 25 % | 73.8 px | 0.80 | 1.00 | 62 |
| heavy line | 27 % → 27 % | 78.6 px | 0.80 | 1.00 | 101 |
| pressure swell | 26 % → 26 % | 97.7 px | 0.80 | 1.00 | 60 |
| fast wave | 32 % → 32 % | 37.3 px | 0.78 | 1.00 | 160 |
| slow wave | 31 % → 31 % | 36.3 px | 0.78 | 1.00 | 251 |
| spiral | 38 % → 38 % | 25.2 px | 0.76 | 1.00 | 283 |
| loop | 30 % → 30 % | 39.5 px | 0.78 | 1.00 | 154 |
| tilted | 26 % → 26 % | 73.4 px | 0.78 | 1.00 | 74 |
| over the wet one | 29 % → 29 % | 6.8 px | 0.78 | 1.00 | 73 |
| long, no reload | 41 % → 41 % | 18.2 px | 0.76 | 1.00 | 509 | quarters: 0.25 → 0.37 → 0.34 → 0.39

Numbers say: light vs heavy: width 73.8 → 78.6 px, dark 0.80 → 0.80; pressure barely changes the width; the long stroke does not run out of paint.

## Brush Artist · Ink — wash
Watercolour 1.00 · 38 px · 36.1 s

![Brush Artist · Ink — wash](Brush-Artist-Ink-wash.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 11 % → 11 % | 31.6 px | 0.39 | 1.04 | 106 |
| heavy line | 19 % → 19 % | 54.3 px | 0.32 | 1.03 | 118 |
| pressure swell | 12 % → 13 % | 45.2 px | 0.37 | 1.04 | 66 |
| fast wave | 39 % → 41 % | 45.5 px | 0.31 | 1.04 | 209 |
| slow wave | 37 % → 38 % | 42.9 px | 0.37 | 1.03 | 403 |
| spiral | 58 % → 61 % | 38.6 px | 0.31 | 1.04 | 365 |
| loop | 32 % → 33 % | 41.9 px | 0.35 | 1.02 | 249 |
| tilted | 13 % → 14 % | 37.0 px | 0.38 | 1.04 | 125 |
| over the wet one | 29 % → 30 % | 42.8 px | 0.38 | 1.04 | 100 |
| long, no reload | 67 % → 72 % | 30.0 px | 0.29 | 1.07 | 897 | quarters: 0.34 → 0.27 → 0.19 → 0.12

Numbers say: light vs heavy: width 31.6 → 54.3 px, dark 0.39 → 0.32.

## Brush Artist · Ink — brush line
Ink 1.00 · 16 px · 27.0 s

![Brush Artist · Ink — brush line](Brush-Artist-Ink-brush-line.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 3 % → 5 % | 7.7 px | 0.78 | 1.81 | 50 |
| heavy line | 13 % → 13 % | 38.9 px | 0.88 | 0.99 | 85 |
| pressure swell | 8 % → 8 % | 28.4 px | 0.87 | 1.05 | 53 |
| fast wave | 24 % → 23 % | 28.0 px | 0.87 | 0.96 | 165 |
| slow wave | 20 % → 19 % | 22.6 px | 0.87 | 0.97 | 183 |
| spiral | 30 % → 27 % | 20.1 px | 0.86 | 0.89 | 278 |
| loop | 18 % → 18 % | 23.6 px | 0.88 | 1.00 | 131 |
| tilted | 7 % → 7 % | 20.5 px | 0.88 | 1.01 | 76 |
| over the wet one | 17 % → 17 % | 26.8 px | 0.88 | 1.00 | 85 |
| long, no reload | 42 % → 30 % | 18.9 px | 0.85 | 0.71 | 425 | quarters: 0.49 → 0.40 → 0.30 → 0.20

Numbers say: light vs heavy: width 7.7 → 38.9 px, dark 0.78 → 0.88; wet paint spreads well beyond the stroke.

## Brush Artist · Ink — dry brush
Gouache 1.00 · 30 px · 21.6 s

![Brush Artist · Ink — dry brush](Brush-Artist-Ink-dry-brush.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 4 % → 0 % | 10.2 px | 0.00 | 0.00 | 69 |
| heavy line | 6 % → 0 % | 16.9 px | 0.77 | 0.01 | 124 |
| pressure swell | 4 % → 0 % | 16.2 px | 0.77 | 0.05 | 79 |
| fast wave | 7 % → 0 % | 7.8 px | 0.77 | 0.05 | 221 |
| slow wave | 11 % → 0 % | 12.7 px | 0.77 | 0.03 | 489 |
| spiral | 13 % → 0 % | 8.7 px | 0.77 | 0.03 | 451 |
| loop | 9 % → 1 % | 11.8 px | 0.77 | 0.06 | 267 |
| tilted | 5 % → 5 % | 15.3 px | 0.77 | 0.94 | 169 |
| over the wet one | 10 % → 1 % | 14.0 px | 0.77 | 0.14 | 156 |
| long, no reload | 13 % → 1 % | 5.9 px | 0.77 | 0.06 | 578 | quarters: 0.23 → 0.11 → 0.07 → 0.05

Numbers say: light vs heavy: width 10.2 → 16.9 px, dark 0.00 → 0.77.

## Brush Artist · Watercolour — blue
Watercolour 0.93 · Ink 0.07 · 40 px · 31.3 s

![Brush Artist · Watercolour — blue](Brush-Artist-Watercolour-blue.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 6 % → 11 % | 16.2 px | 0.29 | 1.88 | 34 |
| heavy line | 11 % → 13 % | 31.9 px | 0.29 | 1.17 | 68 |
| pressure swell | 7 % → 9 % | 25.7 px | 0.30 | 1.38 | 41 |
| fast wave | 24 % → 27 % | 28.2 px | 0.29 | 1.12 | 155 |
| slow wave | 23 % → 32 % | 26.4 px | 0.31 | 1.41 | 235 |
| spiral | 39 % → 47 % | 25.6 px | 0.29 | 1.21 | 242 |
| loop | 20 % → 25 % | 25.7 px | 0.30 | 1.25 | 123 |
| tilted | 12 % → 12 % | 34.0 px | 0.30 | 1.00 | 91 |
| over the wet one | 21 % → 25 % | 25.2 px | 0.30 | 1.19 | 69 |
| long, no reload | 53 % → 59 % | 23.6 px | 0.30 | 1.12 | 421 | quarters: 0.23 → 0.21 → 0.19 → 0.16

Numbers say: light vs heavy: width 16.2 → 31.9 px, dark 0.29 → 0.29; wet paint spreads well beyond the stroke.

## Brush Artist · Watercolour — violet
Watercolour 0.93 · Ink 0.07 · 40 px · 30.5 s

![Brush Artist · Watercolour — violet](Brush-Artist-Watercolour-violet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 6 % → 11 % | 16.2 px | 0.36 | 1.88 | 32 |
| heavy line | 11 % → 13 % | 31.9 px | 0.37 | 1.17 | 67 |
| pressure swell | 7 % → 9 % | 25.7 px | 0.38 | 1.38 | 40 |
| fast wave | 24 % → 27 % | 28.2 px | 0.38 | 1.12 | 143 |
| slow wave | 23 % → 32 % | 26.4 px | 0.39 | 1.41 | 239 |
| spiral | 39 % → 47 % | 25.6 px | 0.37 | 1.21 | 264 |
| loop | 20 % → 25 % | 25.7 px | 0.38 | 1.25 | 114 |
| tilted | 12 % → 12 % | 34.0 px | 0.38 | 1.00 | 106 |
| over the wet one | 21 % → 25 % | 25.2 px | 0.38 | 1.19 | 64 |
| long, no reload | 53 % → 59 % | 23.6 px | 0.38 | 1.12 | 477 | quarters: 0.28 → 0.27 → 0.24 → 0.21

Numbers say: light vs heavy: width 16.2 → 31.9 px, dark 0.36 → 0.37; wet paint spreads well beyond the stroke.

## Brush Artist · Watercolour — teal
Watercolour 0.93 · Ink 0.07 · 40 px · 30.7 s

![Brush Artist · Watercolour — teal](Brush-Artist-Watercolour-teal.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 6 % → 11 % | 16.2 px | 0.23 | 1.88 | 30 |
| heavy line | 11 % → 13 % | 31.9 px | 0.23 | 1.17 | 71 |
| pressure swell | 7 % → 9 % | 25.7 px | 0.24 | 1.38 | 46 |
| fast wave | 24 % → 27 % | 28.2 px | 0.23 | 1.12 | 135 |
| slow wave | 23 % → 32 % | 26.4 px | 0.25 | 1.41 | 247 |
| spiral | 39 % → 47 % | 25.6 px | 0.23 | 1.21 | 260 |
| loop | 20 % → 25 % | 25.7 px | 0.24 | 1.25 | 208 |
| tilted | 12 % → 12 % | 34.0 px | 0.24 | 1.00 | 122 |
| over the wet one | 21 % → 25 % | 25.2 px | 0.24 | 1.19 | 78 |
| long, no reload | 53 % → 59 % | 23.6 px | 0.24 | 1.12 | 366 | quarters: 0.18 → 0.16 → 0.15 → 0.13

Numbers say: light vs heavy: width 16.2 → 31.9 px, dark 0.23 → 0.23; wet paint spreads well beyond the stroke.

## Brush Artist · Gouache
Gouache 1.00 · 30 px · 33.9 s

![Brush Artist · Gouache](Brush-Artist-Gouache.png)

A light paint: laid on a grey sheet (on white it cannot be seen); **dark** = how far it is from the grey either way.

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 8 % → 8 % | 24.4 px | 0.27 | 0.97 | 122 |
| heavy line | 15 % → 12 % | 42.8 px | 0.27 | 0.78 | 134 |
| pressure swell | 11 % → 9 % | 41.0 px | 0.27 | 0.85 | 77 |
| fast wave | 30 % → 14 % | 34.9 px | 0.26 | 0.45 | 195 |
| slow wave | 29 % → 14 % | 34.0 px | 0.26 | 0.47 | 327 |
| spiral | 40 % → 14 % | 26.6 px | 0.26 | 0.35 | 354 |
| loop | 24 % → 15 % | 30.6 px | 0.26 | 0.62 | 188 |
| tilted | 10 % → 10 % | 27.4 px | 0.27 | 1.01 | 99 |
| over the wet one | 22 % → 19 % | 32.9 px | 0.27 | 0.89 | 81 |
| long, no reload | 43 % → 15 % | 19.1 px | 0.26 | 0.35 | 469 | quarters: 0.01 → 0.01 → 0.01 → 0.01

Numbers say: light vs heavy: width 24.4 → 42.8 px, dark 0.27 → 0.27; the long stroke does not run out of paint.

## Brush Artist · Oil — bristle
Oil 0.89 · Oil glaze 0.11 · 30 px · 16.8 s

![Brush Artist · Oil — bristle](Brush-Artist-Oil-bristle.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 9 % → 9 % | 26.3 px | 0.53 | 1.00 | 136 |
| heavy line | 10 % → 10 % | 28.6 px | 0.54 | 1.00 | 187 |
| pressure swell | 8 % → 8 % | 28.2 px | 0.55 | 1.00 | 114 |
| fast wave | 24 % → 24 % | 27.3 px | 0.55 | 1.00 | 341 |
| slow wave | 25 % → 25 % | 28.3 px | 0.55 | 1.00 | 488 |
| spiral | 39 % → 39 % | 25.6 px | 0.54 | 1.00 | 508 |
| loop | 20 % → 20 % | 26.3 px | 0.54 | 1.00 | 251 |
| tilted | 11 % → 11 % | 29.9 px | 0.52 | 1.00 | 135 |
| over the wet one | 20 % → 20 % | 25.5 px | 0.52 | 1.00 | 123 |
| long, no reload | 50 % → 50 % | 22.4 px | 0.54 | 1.00 | 800 | quarters: 0.32 → 0.30 → 0.29 → 0.28

Numbers say: light vs heavy: width 26.3 → 28.6 px, dark 0.53 → 0.54; pressure barely changes the width; the long stroke does not run out of paint.

## Brush Artist · Charcoal — stick
Charcoal 0.78 · Pastel 0.22 · 28 px · 11.6 s

![Brush Artist · Charcoal — stick](Brush-Artist-Charcoal-stick.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 5 % → 5 % | 15.3 px | 0.85 | 1.00 | 21 |
| heavy line | 8 % → 8 % | 23.3 px | 0.85 | 1.00 | 28 |
| pressure swell | 5 % → 5 % | 19.8 px | 0.85 | 1.00 | 18 |
| fast wave | 18 % → 18 % | 20.7 px | 0.85 | 1.00 | 66 |
| slow wave | 17 % → 17 % | 19.5 px | 0.85 | 1.00 | 113 |
| spiral | 29 % → 29 % | 19.3 px | 0.85 | 1.00 | 106 |
| loop | 15 % → 15 % | 19.3 px | 0.85 | 1.00 | 61 |
| tilted | 6 % → 6 % | 16.6 px | 0.85 | 1.00 | 36 |
| over the wet one | 13 % → 13 % | 19.8 px | 0.85 | 1.00 | 31 |
| long, no reload | 41 % → 41 % | 18.2 px | 0.85 | 1.00 | 187 | quarters: 0.38 → 0.38 → 0.38 → 0.38

Numbers say: light vs heavy: width 15.3 → 23.3 px, dark 0.85 → 0.85; the long stroke does not run out of paint.

## Brush Artist · Charcoal — stick B
Charcoal 0.78 · Pastel 0.22 · 36 px · 11.5 s

![Brush Artist · Charcoal — stick B](Brush-Artist-Charcoal-stick-B.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 7 % → 7 % | 19.8 px | 0.85 | 1.00 | 47 |
| heavy line | 10 % → 10 % | 30.4 px | 0.85 | 1.00 | 77 |
| pressure swell | 7 % → 7 % | 25.9 px | 0.85 | 1.00 | 28 |
| fast wave | 23 % → 23 % | 26.8 px | 0.85 | 1.00 | 109 |
| slow wave | 22 % → 22 % | 25.5 px | 0.85 | 1.00 | 194 |
| spiral | 38 % → 38 % | 25.4 px | 0.85 | 1.00 | 202 |
| loop | 19 % → 19 % | 25.0 px | 0.85 | 1.00 | 83 |
| tilted | 7 % → 7 % | 20.4 px | 0.85 | 1.00 | 44 |
| over the wet one | 17 % → 17 % | 25.9 px | 0.85 | 1.00 | 40 |
| long, no reload | 51 % → 51 % | 22.6 px | 0.85 | 1.00 | 260 | quarters: 0.47 → 0.47 → 0.47 → 0.47

Numbers say: light vs heavy: width 19.8 → 30.4 px, dark 0.85 → 0.85; the long stroke does not run out of paint.

## Brush Artist · Charcoal — stick C
Charcoal 0.78 · Pastel 0.22 · 22 px · 10.5 s

![Brush Artist · Charcoal — stick C](Brush-Artist-Charcoal-stick-C.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 4 % → 4 % | 12.6 px | 0.85 | 1.00 | 42 |
| heavy line | 7 % → 7 % | 19.0 px | 0.85 | 1.00 | 25 |
| pressure swell | 4 % → 4 % | 16.2 px | 0.85 | 1.00 | 15 |
| fast wave | 15 % → 15 % | 16.9 px | 0.85 | 1.00 | 52 |
| slow wave | 14 % → 14 % | 15.8 px | 0.85 | 1.00 | 79 |
| spiral | 24 % → 24 % | 15.7 px | 0.85 | 1.00 | 90 |
| loop | 12 % → 12 % | 15.9 px | 0.85 | 1.00 | 44 |
| tilted | 5 % → 5 % | 14.4 px | 0.85 | 1.00 | 33 |
| over the wet one | 11 % → 11 % | 16.1 px | 0.85 | 1.00 | 27 |
| long, no reload | 34 % → 34 % | 15.2 px | 0.85 | 1.00 | 135 | quarters: 0.32 → 0.32 → 0.32 → 0.32

Numbers say: light vs heavy: width 12.6 → 19.0 px, dark 0.85 → 0.85; the long stroke does not run out of paint.

## Brush Artist · Refs · #01 Henry Ward peach cloud — own sheet
own sheet 600 × 600 · Gouache 1.00 · 44 px · 14.7 s

![Brush Artist · Refs · #01 Henry Ward peach cloud — own sheet](Brush-Artist-Refs-01-Henry-Ward-peach-cloud-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 13 % → 34 % | 38.3 px | 0.57 | 2.57 | 182 |
| stroke 2 | 23 % → 53 % | 74.1 px | 0.57 | 2.37 | 152 |
| stroke 3 | 26 % → 51 % | 75.8 px | 0.57 | 1.95 | 139 |
| stroke 4 | 28 % → 55 % | 92.1 px | 0.57 | 1.97 | 208 |
| stroke 5 | 27 % → 50 % | 79.2 px | 0.57 | 1.81 | 164 |
| stroke 6 | 28 % → 38 % | 85.4 px | 0.57 | 1.35 | 145 |
| stroke 7 | 15 % → 51 % | 37.8 px | 0.58 | 3.39 | 151 |
| stroke 8 | 18 % → 48 % | 44.6 px | 0.58 | 2.71 | 154 |
| stroke 9 | 20 % → 49 % | 52.4 px | 0.58 | 2.41 | 164 |
| stroke 10 | 23 % → 50 % | 62.0 px | 0.58 | 2.15 | 161 |
| stroke 11 | 25 % → 53 % | 71.5 px | 0.58 | 2.08 | 154 |
| stroke 12 | 28 % → 55 % | 85.0 px | 0.58 | 1.95 | 146 |
| stroke 13 | 36 % → 58 % | 104.6 px | 0.58 | 1.61 | 153 |
| stroke 14 | 39 % → 60 % | 112.5 px | 0.58 | 1.52 | 154 |
| stroke 15 | 53 % → 65 % | 155.8 px | 0.58 | 1.24 | 156 |
| stroke 16 | 54 % → 66 % | 163.0 px | 0.58 | 1.22 | 159 |
| stroke 17 | 55 % → 67 % | 153.8 px | 0.58 | 1.23 | 156 |
| stroke 18 | 56 % → 66 % | 163.3 px | 0.58 | 1.18 | 160 |
| stroke 19 | 58 % → 65 % | 162.3 px | 0.58 | 1.12 | 153 |
| stroke 20 | 57 % → 62 % | 164.4 px | 0.58 | 1.08 | 155 |
| stroke 21 | 57 % → 58 % | 165.4 px | 0.58 | 1.03 | 188 |
| stroke 22 | 59 % → 59 % | 170.8 px | 0.58 | 1.01 | 177 |
| stroke 23 | 58 % → 57 % | 165.8 px | 0.58 | 0.98 | 174 |
| stroke 24 | 62 % → 60 % | 184.9 px | 0.58 | 0.97 | 178 |

Numbers say: wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #02 Henry Ward cream strokes — own sheet
own sheet 600 × 600 · Gouache 1.00 · 46 px · 9.2 s

![Brush Artist · Refs · #02 Henry Ward cream strokes — own sheet](Brush-Artist-Refs-02-Henry-Ward-cream-strokes-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 18 % → 25 % | 37.0 px | 0.67 | 1.40 | 256 |
| stroke 2 | 27 % → 29 % | 70.3 px | 0.67 | 1.08 | 233 |
| stroke 3 | 26 % → 35 % | 66.2 px | 0.67 | 1.34 | 222 |
| stroke 4 | 28 % → 32 % | 68.9 px | 0.67 | 1.13 | 223 |
| stroke 5 | 34 % → 38 % | 83.6 px | 0.67 | 1.10 | 216 |
| stroke 6 | 27 % → 32 % | 65.9 px | 0.67 | 1.18 | 227 |
| stroke 7 | 28 % → 22 % | 71.8 px | 0.66 | 0.76 | 207 |

## Brush Artist · Refs · #03 Henry Ward navy contours — own sheet
own sheet 600 × 600 · Impasto 1.00 · 22 px · 3.5 s

![Brush Artist · Refs · #03 Henry Ward navy contours — own sheet](Brush-Artist-Refs-03-Henry-Ward-navy-contours-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 11 % → 18 % | 23.1 px | 0.69 | 1.56 | 147 |
| stroke 2 | 20 % → 23 % | 28.3 px | 0.69 | 1.14 | 129 |
| stroke 3 | 23 % → 23 % | 33.4 px | 0.69 | 1.01 | 150 |
| stroke 4 | 23 % → 21 % | 50.8 px | 0.69 | 0.92 | 186 |

Numbers say: wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #04 Henry Ward grey cloud — own sheet
own sheet 600 × 600 · Gouache 1.00 · 50 px · 15.2 s

![Brush Artist · Refs · #04 Henry Ward grey cloud — own sheet](Brush-Artist-Refs-04-Henry-Ward-grey-cloud-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 14 % → 46 % | 42.4 px | 0.39 | 3.19 | 410 |
| stroke 2 | 18 % → 48 % | 52.8 px | 0.39 | 2.62 | 241 |
| stroke 3 | 26 % → 55 % | 73.7 px | 0.39 | 2.09 | 248 |
| stroke 4 | 31 % → 58 % | 89.1 px | 0.39 | 1.91 | 228 |
| stroke 5 | 37 % → 65 % | 111.3 px | 0.39 | 1.76 | 222 |
| stroke 6 | 39 % → 68 % | 126.9 px | 0.39 | 1.76 | 202 |
| stroke 7 | 45 % → 76 % | 132.6 px | 0.39 | 1.68 | 225 |
| stroke 8 | 45 % → 76 % | 134.2 px | 0.39 | 1.68 | 228 |
| stroke 9 | 45 % → 76 % | 134.0 px | 0.39 | 1.70 | 208 |
| stroke 10 | 46 % → 76 % | 148.4 px | 0.39 | 1.65 | 215 |
| stroke 11 | 45 % → 76 % | 128.4 px | 0.39 | 1.68 | 211 |
| stroke 12 | 47 % → 76 % | 142.4 px | 0.39 | 1.61 | 208 |
| stroke 13 | 47 % → 77 % | 133.2 px | 0.39 | 1.64 | 220 |
| stroke 14 | 46 % → 77 % | 137.6 px | 0.39 | 1.66 | 217 |
| stroke 15 | 46 % → 71 % | 132.1 px | 0.39 | 1.54 | 228 |
| stroke 16 | 47 % → 68 % | 143.8 px | 0.39 | 1.44 | 239 |
| stroke 17 | 46 % → 59 % | 132.2 px | 0.39 | 1.28 | 220 |
| stroke 18 | 45 % → 54 % | 147.5 px | 0.39 | 1.22 | 199 |
| stroke 19 | 45 % → 46 % | 135.3 px | 0.39 | 1.01 | 214 |
| stroke 20 | 47 % → 45 % | 147.7 px | 0.39 | 0.97 | 212 |

Numbers say: wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #05 Henry Ward green in rust loops — own sheet
own sheet 600 × 600 · Impasto 1.00 · 20 px · 2.5 s

![Brush Artist · Refs · #05 Henry Ward green in rust loops — own sheet](Brush-Artist-Refs-05-Henry-Ward-green-in-rust-loops-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 12 % → 19 % | 20.9 px | 0.02 | 1.60 | 135 |
| stroke 2 | 12 % → 11 % | 23.5 px | 0.02 | 0.93 | 171 |
| stroke 3 | 23 % → 21 % | 41.5 px | 0.02 | 0.93 | 154 |

Numbers say: wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #06 Henry Ward scrubbed grey — own sheet
own sheet 600 × 600 · Gouache 1.00 · 50 px · 16.1 s

![Brush Artist · Refs · #06 Henry Ward scrubbed grey — own sheet](Brush-Artist-Refs-06-Henry-Ward-scrubbed-grey-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 17 % → 51 % | 41.8 px | 0.39 | 2.99 | 219 |
| stroke 2 | 21 % → 53 % | 55.2 px | 0.39 | 2.58 | 222 |
| stroke 3 | 27 % → 57 % | 83.3 px | 0.39 | 2.11 | 208 |
| stroke 4 | 29 % → 58 % | 91.3 px | 0.39 | 2.00 | 208 |
| stroke 5 | 42 % → 72 % | 125.2 px | 0.39 | 1.74 | 228 |
| stroke 6 | 44 % → 73 % | 135.5 px | 0.39 | 1.64 | 217 |
| stroke 7 | 46 % → 76 % | 132.0 px | 0.39 | 1.65 | 223 |
| stroke 8 | 47 % → 76 % | 148.4 px | 0.39 | 1.62 | 227 |
| stroke 9 | 45 % → 76 % | 139.0 px | 0.39 | 1.68 | 243 |
| stroke 10 | 44 % → 75 % | 143.9 px | 0.39 | 1.70 | 210 |
| stroke 11 | 46 % → 76 % | 134.3 px | 0.39 | 1.65 | 216 |
| stroke 12 | 47 % → 76 % | 143.8 px | 0.39 | 1.60 | 212 |
| stroke 13 | 45 % → 75 % | 128.2 px | 0.39 | 1.66 | 233 |
| stroke 14 | 43 % → 75 % | 127.0 px | 0.39 | 1.73 | 238 |
| stroke 15 | 44 % → 76 % | 126.7 px | 0.39 | 1.71 | 214 |
| stroke 16 | 46 % → 74 % | 148.1 px | 0.39 | 1.60 | 252 |
| stroke 17 | 46 % → 66 % | 136.3 px | 0.39 | 1.45 | 235 |
| stroke 18 | 47 % → 64 % | 140.7 px | 0.39 | 1.37 | 215 |
| stroke 19 | 45 % → 58 % | 133.6 px | 0.39 | 1.29 | 223 |
| stroke 20 | 46 % → 56 % | 142.5 px | 0.39 | 1.22 | 209 |
| stroke 21 | 46 % → 47 % | 133.1 px | 0.39 | 1.02 | 216 |
| stroke 22 | 45 % → 42 % | 148.2 px | 0.39 | 0.93 | 316 |

Numbers say: wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #07 Henry Ward blue L + black zigzag — own sheet
own sheet 600 × 600 · Impasto 1.00 · 34 px · 2.2 s

![Brush Artist · Refs · #07 Henry Ward blue L + black zigzag — own sheet](Brush-Artist-Refs-07-Henry-Ward-blue-L-black-zigzag-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 15 % → 18 % | 35.6 px | 0.59 | 1.14 | 182 |
| stroke 2 | 17 % → 16 % | 42.9 px | 0.59 | 0.93 | 88 |

## Brush Artist · Refs · #08 Henry Ward olive bands — own sheet
own sheet 600 × 600 · Gouache 1.00 · 34 px · 6.0 s

![Brush Artist · Refs · #08 Henry Ward olive bands — own sheet](Brush-Artist-Refs-08-Henry-Ward-olive-bands-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 10 % → 7 % | 19.4 px | 0.58 | 0.73 | 160 |
| stroke 2 | 16 % → 9 % | 35.4 px | 0.58 | 0.55 | 175 |
| stroke 3 | 14 % → 13 % | 30.4 px | 0.58 | 0.88 | 187 |
| stroke 4 | 16 % → 10 % | 34.3 px | 0.58 | 0.65 | 181 |
| stroke 5 | 23 % → 13 % | 46.7 px | 0.58 | 0.57 | 178 |
| stroke 6 | 15 % → 8 % | 28.4 px | 0.58 | 0.50 | 211 |

## Brush Artist · Refs · #09 Henry Ward white loops — own sheet
own sheet 600 × 600 · Gouache 1.00 · 46 px · 7.7 s

![Brush Artist · Refs · #09 Henry Ward white loops — own sheet](Brush-Artist-Refs-09-Henry-Ward-white-loops-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 23 % → 2 % | 12.2 px | 0.05 | 0.09 | 1056 |
| stroke 2 | 25 % → 1 % | 25.0 px | 0.06 | 0.05 | 1035 |
| stroke 3 | 33 % → 1 % | 30.5 px | 0.06 | 0.04 | 921 |
| stroke 4 | 2 % → 1 % | 4.5 px | 0.05 | 0.30 | 155 |
| stroke 5 | 2 % → 1 % | 4.7 px | 0.06 | 0.34 | 148 |
| stroke 6 | 2 % → 1 % | 4.8 px | 0.06 | 0.69 | 150 |
| stroke 7 | 3 % → 1 % | 8.7 px | 0.06 | 0.37 | 162 |
| stroke 8 | 3 % → 1 % | 4.4 px | 0.05 | 0.28 | 170 |

## Brush Artist · Refs · #10 Henry Ward maroon loops — own sheet
own sheet 600 × 600 · Impasto 1.00 · 30 px · 3.2 s

![Brush Artist · Refs · #10 Henry Ward maroon loops — own sheet](Brush-Artist-Refs-10-Henry-Ward-maroon-loops-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 12 % → 28 % | 28.7 px | 0.72 | 2.39 | 213 |
| stroke 2 | 22 % → 40 % | 48.5 px | 0.72 | 1.87 | 121 |
| stroke 3 | 29 % → 37 % | 58.5 px | 0.72 | 1.27 | 171 |
| stroke 4 | 41 % → 39 % | 92.8 px | 0.72 | 0.96 | 107 |
| stroke 5 | 34 % → 32 % | 85.8 px | 0.72 | 0.93 | 144 |

Numbers say: wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #11 Henry Ward purple spun balls — own sheet
own sheet 600 × 600 · Impasto 1.00 · 36 px · 3.0 s

![Brush Artist · Refs · #11 Henry Ward purple spun balls — own sheet](Brush-Artist-Refs-11-Henry-Ward-purple-spun-balls-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 24 % → 35 % | 26.5 px | 0.68 | 1.43 | 244 |
| stroke 2 | 35 % → 46 % | 38.2 px | 0.68 | 1.33 | 227 |
| stroke 3 | 36 % → 34 % | 39.2 px | 0.68 | 0.97 | 229 |

## Brush Artist · Refs · #12 Henry Ward black-olive cage — own sheet
own sheet 600 × 600 · Gouache 1.00 · 28 px · 5.7 s

![Brush Artist · Refs · #12 Henry Ward black-olive cage — own sheet](Brush-Artist-Refs-12-Henry-Ward-black-olive-cage-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 8 % → 9 % | 14.7 px | 0.59 | 1.18 | 215 |
| stroke 2 | 8 % → 11 % | 19.1 px | 0.59 | 1.34 | 188 |
| stroke 3 | 17 % → 14 % | 26.7 px | 0.59 | 0.83 | 236 |
| stroke 4 | 18 % → 11 % | 35.1 px | 0.59 | 0.64 | 128 |
| stroke 5 | 17 % → 9 % | 30.3 px | 0.59 | 0.53 | 129 |
| stroke 6 | 26 % → 12 % | 50.0 px | 0.59 | 0.47 | 219 |

## Brush Artist · Refs · #13 Henry Ward blue streaky form — own sheet
own sheet 600 × 600 · Gouache 1.00 · 50 px · 11.9 s

![Brush Artist · Refs · #13 Henry Ward blue streaky form — own sheet](Brush-Artist-Refs-13-Henry-Ward-blue-streaky-form-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 14 % → 1 % | 42.5 px | 0.04 | 0.08 | 204 |
| stroke 2 | 18 % → 1 % | 56.9 px | 0.04 | 0.06 | 295 |
| stroke 3 | 29 % → 1 % | 84.7 px | 0.04 | 0.04 | 278 |
| stroke 4 | 30 % → 1 % | 97.7 px | 0.04 | 0.03 | 205 |
| stroke 5 | 44 % → 1 % | 128.1 px | 0.04 | 0.03 | 226 |
| stroke 6 | 44 % → 1 % | 126.2 px | 0.04 | 0.02 | 283 |
| stroke 7 | 46 % → 2 % | 135.7 px | 0.05 | 0.03 | 315 |
| stroke 8 | 48 % → 1 % | 144.8 px | 0.05 | 0.02 | 289 |
| stroke 9 | 46 % → 1 % | 143.8 px | 0.05 | 0.02 | 250 |
| stroke 10 | 46 % → 1 % | 151.6 px | 0.05 | 0.02 | 228 |
| stroke 11 | 44 % → 1 % | 134.5 px | 0.05 | 0.01 | 221 |
| stroke 12 | 46 % → 1 % | 136.4 px | 0.05 | 0.02 | 230 |
| stroke 13 | 45 % → 1 % | 138.8 px | 0.05 | 0.03 | 193 |
| stroke 14 | 43 % → 1 % | 126.9 px | 0.05 | 0.03 | 208 |
| stroke 15 | 43 % → 1 % | 124.0 px | 0.05 | 0.03 | 208 |
| stroke 16 | 46 % → 1 % | 137.5 px | 0.05 | 0.02 | 209 |
| stroke 17 | 55 % → 1 % | 138.3 px | 0.04 | 0.01 | 213 |
| stroke 18 | 58 % → 1 % | 140.5 px | 0.04 | 0.01 | 208 |
| stroke 19 | 63 % → 1 % | 128.9 px | 0.04 | 0.01 | 216 |
| stroke 20 | 73 % → 1 % | 139.5 px | 0.04 | 0.01 | 214 |
| stroke 21 | 2 % → 1 % | 4.8 px | 0.05 | 0.30 | 149 |
| stroke 22 | 2 % → 1 % | 5.2 px | 0.04 | 0.58 | 151 |
| stroke 23 | 3 % → 1 % | 9.3 px | 0.04 | 0.36 | 135 |
| stroke 24 | 2 % → 1 % | 5.7 px | 0.05 | 0.36 | 154 |
| stroke 25 | 3 % → 1 % | 7.5 px | 0.05 | 0.43 | 154 |

## Brush Artist · Refs · #14 Henry Ward olive totem — own sheet
own sheet 600 × 600 · Impasto 1.00 · 48 px · 7.2 s

![Brush Artist · Refs · #14 Henry Ward olive totem — own sheet](Brush-Artist-Refs-14-Henry-Ward-olive-totem-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 18 % → 46 % | 46.9 px | 0.38 | 2.58 | 132 |
| stroke 2 | 21 % → 50 % | 64.4 px | 0.38 | 2.45 | 137 |
| stroke 3 | 29 % → 52 % | 100.7 px | 0.38 | 1.78 | 141 |
| stroke 4 | 30 % → 55 % | 113.8 px | 0.38 | 1.80 | 134 |
| stroke 5 | 39 % → 64 % | 135.7 px | 0.38 | 1.63 | 157 |
| stroke 6 | 39 % → 65 % | 150.5 px | 0.38 | 1.68 | 164 |
| stroke 7 | 37 % → 61 % | 124.4 px | 0.38 | 1.66 | 186 |
| stroke 8 | 37 % → 63 % | 142.5 px | 0.38 | 1.69 | 194 |
| stroke 9 | 38 % → 63 % | 131.0 px | 0.38 | 1.67 | 182 |
| stroke 10 | 38 % → 62 % | 141.2 px | 0.38 | 1.62 | 179 |
| stroke 11 | 40 % → 65 % | 143.9 px | 0.38 | 1.61 | 182 |
| stroke 12 | 38 % → 65 % | 144.3 px | 0.38 | 1.70 | 144 |
| stroke 13 | 39 % → 67 % | 135.6 px | 0.38 | 1.73 | 137 |
| stroke 14 | 37 % → 62 % | 134.7 px | 0.38 | 1.69 | 141 |
| stroke 15 | 40 % → 66 % | 137.0 px | 0.38 | 1.65 | 136 |
| stroke 16 | 38 % → 64 % | 138.9 px | 0.38 | 1.66 | 141 |
| stroke 17 | 38 % → 62 % | 126.3 px | 0.38 | 1.65 | 135 |
| stroke 18 | 40 % → 66 % | 155.0 px | 0.38 | 1.64 | 119 |
| stroke 19 | 40 % → 60 % | 138.1 px | 0.38 | 1.52 | 124 |
| stroke 20 | 41 % → 55 % | 144.5 px | 0.38 | 1.34 | 130 |
| stroke 21 | 46 % → 55 % | 137.8 px | 0.38 | 1.18 | 122 |
| stroke 22 | 54 % → 53 % | 146.8 px | 0.38 | 0.99 | 123 |

Numbers say: wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #15 Ultramarine brush script — own sheet
own sheet 600 × 600 · Ink 1.00 · 4 px · 8.5 s

![Brush Artist · Refs · #15 Ultramarine brush script — own sheet](Brush-Artist-Refs-15-Ultramarine-brush-script-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 40 % → 42 % | 8.9 px | 0.66 | 1.05 | 49 |
| stroke 2 | 40 % → 42 % | 8.9 px | 0.66 | 1.06 | 52 |
| stroke 3 | 40 % → 42 % | 9.5 px | 0.74 | 1.06 | 27 |
| stroke 4 | 42 % → 45 % | 10.1 px | 0.74 | 1.09 | 16 |
| stroke 5 | 44 % → 48 % | 9.7 px | 0.73 | 1.09 | 25 |
| stroke 6 | 42 % → 44 % | 9.5 px | 0.65 | 1.05 | 51 |
| stroke 7 | 43 % → 47 % | 9.2 px | 0.72 | 1.08 | 30 |
| stroke 8 | 38 % → 41 % | 9.3 px | 0.68 | 1.05 | 43 |
| stroke 9 | 40 % → 42 % | 9.2 px | 0.69 | 1.06 | 42 |
| stroke 10 | 36 % → 38 % | 9.9 px | 0.68 | 1.05 | 43 |
| stroke 11 | 42 % → 45 % | 9.6 px | 0.70 | 1.06 | 40 |
| stroke 12 | 39 % → 41 % | 9.4 px | 0.66 | 1.06 | 51 |
| stroke 13 | 45 % → 48 % | 10.2 px | 0.71 | 1.06 | 32 |
| stroke 14 | 38 % → 41 % | 9.8 px | 0.72 | 1.07 | 23 |
| stroke 15 | 37 % → 39 % | 9.1 px | 0.69 | 1.06 | 42 |
| stroke 16 | 42 % → 45 % | 9.4 px | 0.72 | 1.06 | 29 |
| stroke 17 | 41 % → 44 % | 7.1 px | 0.71 | 1.08 | 44 |
| stroke 18 | 43 % → 45 % | 9.2 px | 0.73 | 1.06 | 25 |
| stroke 19 | 39 % → 41 % | 8.9 px | 0.66 | 1.05 | 54 |
| stroke 20 | 41 % → 43 % | 9.4 px | 0.71 | 1.06 | 32 |
| stroke 21 | 41 % → 43 % | 9.9 px | 0.70 | 1.06 | 38 |
| stroke 22 | 42 % → 45 % | 8.5 px | 0.65 | 1.06 | 56 |
| stroke 23 | 40 % → 43 % | 10.1 px | 0.73 | 1.08 | 22 |
| stroke 24 | 38 % → 41 % | 8.8 px | 0.73 | 1.07 | 32 |
| stroke 25 | 41 % → 43 % | 9.8 px | 0.72 | 1.07 | 34 |
| stroke 26 | 46 % → 49 % | 9.3 px | 0.68 | 1.05 | 47 |
| stroke 27 | 43 % → 45 % | 8.8 px | 0.63 | 1.05 | 59 |
| stroke 28 | 44 % → 46 % | 9.1 px | 0.70 | 1.06 | 41 |
| stroke 29 | 36 % → 39 % | 10.6 px | 0.72 | 1.08 | 24 |
| stroke 30 | 39 % → 41 % | 8.7 px | 0.71 | 1.04 | 43 |
| stroke 31 | 43 % → 46 % | 10.3 px | 0.75 | 1.08 | 19 |
| stroke 32 | 42 % → 46 % | 9.5 px | 0.73 | 1.09 | 28 |
| stroke 33 | 35 % → 38 % | 10.9 px | 0.72 | 1.08 | 21 |
| stroke 34 | 40 % → 43 % | 9.8 px | 0.73 | 1.08 | 23 |
| stroke 35 | 36 % → 37 % | 9.4 px | 0.65 | 1.05 | 46 |

## Brush Artist · Refs · #18 Blue oil-stick scribbles — own sheet
own sheet 600 × 600 · Pastel 1.00 · 10 px · 3.2 s

![Brush Artist · Refs · #18 Blue oil-stick scribbles — own sheet](Brush-Artist-Refs-18-Blue-oil-stick-scribbles-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 15 % → 31 % | 3.8 px | 0.49 | 2.11 | 145 |
| stroke 2 | 13 % → 37 % | 3.6 px | 0.49 | 2.73 | 171 |
| stroke 3 | 16 % → 26 % | 5.8 px | 0.49 | 1.66 | 190 |
| stroke 4 | 15 % → 29 % | 8.0 px | 0.49 | 1.88 | 181 |
| stroke 5 | 29 % → 34 % | 8.4 px | 0.49 | 1.19 | 163 |
| stroke 6 | 25 % → 26 % | 9.4 px | 0.49 | 1.02 | 136 |
| stroke 7 | 26 % → 32 % | 8.3 px | 0.49 | 1.24 | 158 |
| stroke 8 | 30 % → 30 % | 17.0 px | 0.49 | 1.00 | 172 |

Numbers say: wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #20 Orange-red crayon scribble — own sheet
own sheet 600 × 600 · Pastel 1.00 · 14 px · 3.5 s

![Brush Artist · Refs · #20 Orange-red crayon scribble — own sheet](Brush-Artist-Refs-20-Orange-red-crayon-scribble-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 8 % → 18 % | 5.5 px | 0.59 | 2.46 | 200 |
| stroke 2 | 9 % → 23 % | 6.8 px | 0.59 | 2.48 | 187 |
| stroke 3 | 13 % → 21 % | 8.5 px | 0.59 | 1.64 | 173 |
| stroke 4 | 24 % → 32 % | 8.9 px | 0.59 | 1.34 | 180 |
| stroke 5 | 27 % → 27 % | 7.7 px | 0.59 | 1.00 | 169 |
| stroke 6 | 22 % → 22 % | 16.8 px | 0.59 | 1.00 | 186 |

Numbers say: wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #21 Gritty black contours — own sheet
own sheet 600 × 600 · Gouache 1.00 · 12 px · 4.7 s

![Brush Artist · Refs · #21 Gritty black contours — own sheet](Brush-Artist-Refs-21-Gritty-black-contours-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 4 % → 3 % | 4.9 px | 0.37 | 0.71 | 167 |
| stroke 2 | 5 % → 2 % | 7.5 px | 0.37 | 0.41 | 178 |
| stroke 3 | 7 % → 2 % | 5.9 px | 0.37 | 0.26 | 120 |
| stroke 4 | 8 % → 3 % | 9.8 px | 0.37 | 0.40 | 136 |
| stroke 5 | 10 % → 3 % | 11.9 px | 0.37 | 0.34 | 93 |

## Brush Artist · Refs · #22 Bold black brush poster — own sheet
own sheet 600 × 600 · Ink 1.00 · 20 px · 5.8 s

![Brush Artist · Refs · #22 Bold black brush poster — own sheet](Brush-Artist-Refs-22-Bold-black-brush-poster-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 22 % → 27 % | 36.3 px | 0.94 | 1.20 | 102 |
| stroke 2 | 27 % → 37 % | 41.4 px | 0.94 | 1.37 | 25 |
| stroke 3 | 28 % → 29 % | 43.6 px | 0.94 | 1.00 | 73 |
| stroke 4 | 27 % → 39 % | 53.7 px | 0.94 | 1.43 | 97 |
| stroke 5 | 25 % → 25 % | 42.9 px | 0.94 | 1.00 | 138 |

## Brush Artist · Refs · #23 Dry white on orange + black line — own sheet
own sheet 600 × 600 · Gouache 1.00 · 50 px · 8.2 s

![Brush Artist · Refs · #23 Dry white on orange + black line — own sheet](Brush-Artist-Refs-23-Dry-white-on-orange-black-line-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 7 % → 10 % | 24.0 px | 0.39 | 1.46 | 249 |
| stroke 2 | 9 % → 9 % | 33.1 px | 0.39 | 0.97 | 182 |
| stroke 3 | 14 % → 10 % | 51.0 px | 0.39 | 0.71 | 160 |
| stroke 4 | 16 % → 11 % | 61.7 px | 0.39 | 0.71 | 173 |
| stroke 5 | 22 % → 13 % | 79.6 px | 0.39 | 0.58 | 187 |
| stroke 6 | 22 % → 15 % | 91.6 px | 0.39 | 0.68 | 143 |
| stroke 7 | 18 % → 14 % | 68.2 px | 0.39 | 0.77 | 146 |
| stroke 8 | 19 % → 13 % | 72.3 px | 0.39 | 0.71 | 157 |
| stroke 9 | 19 % → 14 % | 71.6 px | 0.39 | 0.73 | 140 |
| stroke 10 | 19 % → 14 % | 73.5 px | 0.38 | 0.75 | 142 |
| stroke 11 | 21 % → 16 % | 79.2 px | 0.38 | 0.74 | 160 |
| stroke 12 | 22 % → 16 % | 83.6 px | 0.38 | 0.73 | 179 |
| stroke 13 | 22 % → 18 % | 81.5 px | 0.38 | 0.80 | 160 |
| stroke 14 | 21 % → 17 % | 84.1 px | 0.38 | 0.82 | 160 |
| stroke 15 | 21 % → 15 % | 76.8 px | 0.38 | 0.72 | 144 |
| stroke 16 | 21 % → 13 % | 82.3 px | 0.38 | 0.64 | 158 |
| stroke 17 | 21 % → 12 % | 74.1 px | 0.38 | 0.57 | 146 |
| stroke 18 | 25 % → 13 % | 90.7 px | 0.38 | 0.50 | 137 |

## Brush Artist · Refs · #24 Picasso flat oil — own sheet
own sheet 600 × 600 · Oil 0.89 · Oil glaze 0.11 · 34 px · 5.4 s

![Brush Artist · Refs · #24 Picasso flat oil — own sheet](Brush-Artist-Refs-24-Picasso-flat-oil-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 16 % → 45 % | 34.7 px | 0.23 | 2.74 | 133 |
| stroke 2 | 20 % → 49 % | 47.2 px | 0.23 | 2.40 | 131 |
| stroke 3 | 29 % → 59 % | 62.6 px | 0.23 | 2.07 | 128 |
| stroke 4 | 37 % → 65 % | 83.2 px | 0.23 | 1.76 | 133 |
| stroke 5 | 43 % → 71 % | 94.5 px | 0.23 | 1.65 | 129 |
| stroke 6 | 44 % → 66 % | 102.2 px | 0.23 | 1.50 | 140 |
| stroke 7 | 45 % → 66 % | 94.9 px | 0.23 | 1.46 | 135 |
| stroke 8 | 44 % → 66 % | 107.0 px | 0.23 | 1.50 | 142 |
| stroke 9 | 37 % → 62 % | 81.5 px | 0.23 | 1.68 | 139 |
| stroke 10 | 39 % → 62 % | 93.1 px | 0.23 | 1.58 | 139 |
| stroke 11 | 37 % → 60 % | 78.6 px | 0.23 | 1.62 | 129 |
| stroke 12 | 38 % → 61 % | 91.1 px | 0.23 | 1.60 | 130 |
| stroke 13 | 38 % → 68 % | 84.4 px | 0.23 | 1.76 | 135 |
| stroke 14 | 39 % → 69 % | 88.9 px | 0.23 | 1.75 | 142 |
| stroke 15 | 39 % → 62 % | 83.3 px | 0.23 | 1.58 | 132 |
| stroke 16 | 38 % → 55 % | 88.0 px | 0.23 | 1.43 | 137 |
| stroke 17 | 43 % → 48 % | 90.0 px | 0.23 | 1.12 | 141 |
| stroke 18 | 42 % → 42 % | 102.7 px | 0.23 | 1.00 | 179 |

Numbers say: wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #25 Yellow heavy flat stroke — own sheet
own sheet 600 × 600 · Impasto 1.00 · 110 px · 3.0 s

![Brush Artist · Refs · #25 Yellow heavy flat stroke — own sheet](Brush-Artist-Refs-25-Yellow-heavy-flat-stroke-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 18 % → 18 % | 104.3 px | 0.17 | 0.98 | 635 |

## Brush Artist · Refs · #27 Orange impasto swatch — own sheet
own sheet 600 × 600 · Impasto 1.00 · 60 px · 3.1 s

![Brush Artist · Refs · #27 Orange impasto swatch — own sheet](Brush-Artist-Refs-27-Orange-impasto-swatch-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 8 % → 21 % | 61.8 px | 0.33 | 2.60 | 70 |
| stroke 2 | 7 % → 33 % | 62.6 px | 0.33 | 4.67 | 53 |
| stroke 3 | 25 % → 36 % | 245.8 px | 0.33 | 1.40 | 38 |
| stroke 4 | 10 % → 12 % | 69.8 px | 0.33 | 1.25 | 63 |
| stroke 5 | 17 % → 33 % | 63.5 px | 0.33 | 1.90 | 68 |
| stroke 6 | 18 % → 32 % | 145.3 px | 0.33 | 1.79 | 59 |
| stroke 7 | 8 % → 15 % | 70.4 px | 0.33 | 1.87 | 48 |
| stroke 8 | 33 % → 34 % | 337.7 px | 0.33 | 1.04 | 42 |
| stroke 9 | 38 % → 37 % | 185.5 px | 0.33 | 0.98 | 73 |
| stroke 10 | 34 % → 33 % | 305.4 px | 0.33 | 0.98 | 50 |

Numbers say: wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #28 Miles Davis black lines — own sheet
own sheet 600 × 600 · Ink 1.00 · 22 px · 8.0 s

![Brush Artist · Refs · #28 Miles Davis black lines — own sheet](Brush-Artist-Refs-28-Miles-Davis-black-lines-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 22 % → 32 % | 36.5 px | 0.88 | 1.42 | 173 |
| stroke 2 | 28 % → 49 % | 38.2 px | 0.88 | 1.73 | 139 |
| stroke 3 | 39 % → 44 % | 75.1 px | 0.88 | 1.12 | 107 |
| stroke 4 | 42 % → 48 % | 83.7 px | 0.88 | 1.15 | 160 |
| stroke 5 | 55 % → 55 % | 109.8 px | 0.88 | 1.00 | 116 |

Numbers say: wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #29 Shrigley magenta asterisk — own sheet
own sheet 600 × 600 · Watercolour 1.00 · 70 px · 8.1 s

![Brush Artist · Refs · #29 Shrigley magenta asterisk — own sheet](Brush-Artist-Refs-29-Shrigley-magenta-asterisk-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 13 % → 37 % | 46.6 px | 0.67 | 2.86 | 162 |
| stroke 2 | 12 % → 12 % | 87.1 px | 0.67 | 1.00 | 171 |
| stroke 3 | 28 % → 37 % | 100.9 px | 0.67 | 1.31 | 178 |
| stroke 4 | 23 % → 23 % | 164.0 px | 0.67 | 1.02 | 183 |

Numbers say: wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #30 Red gouache face patch — own sheet
own sheet 600 × 600 · Gouache 1.00 · 60 px · 14.3 s

![Brush Artist · Refs · #30 Red gouache face patch — own sheet](Brush-Artist-Refs-30-Red-gouache-face-patch-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 12 % → 37 % | 51.5 px | 0.54 | 3.23 | 158 |
| stroke 2 | 15 % → 40 % | 74.5 px | 0.54 | 2.72 | 181 |
| stroke 3 | 24 % → 50 % | 115.9 px | 0.54 | 2.06 | 503 |
| stroke 4 | 27 % → 52 % | 134.1 px | 0.54 | 1.94 | 801 |
| stroke 5 | 34 % → 60 % | 159.9 px | 0.54 | 1.77 | 276 |
| stroke 6 | 35 % → 61 % | 178.3 px | 0.54 | 1.76 | 329 |
| stroke 7 | 34 % → 59 % | 160.9 px | 0.54 | 1.73 | 278 |
| stroke 8 | 34 % → 56 % | 162.5 px | 0.54 | 1.66 | 299 |
| stroke 9 | 36 % → 60 % | 173.1 px | 0.54 | 1.66 | 154 |
| stroke 10 | 38 % → 62 % | 196.8 px | 0.54 | 1.64 | 167 |
| stroke 11 | 37 % → 61 % | 182.4 px | 0.54 | 1.66 | 148 |
| stroke 12 | 36 % → 58 % | 178.3 px | 0.54 | 1.62 | 178 |
| stroke 13 | 33 % → 46 % | 156.5 px | 0.54 | 1.39 | 150 |
| stroke 14 | 33 % → 41 % | 157.6 px | 0.54 | 1.25 | 201 |
| stroke 15 | 33 % → 37 % | 153.4 px | 0.54 | 1.12 | 290 |
| stroke 16 | 39 % → 39 % | 184.9 px | 0.54 | 0.99 | 144 |

Numbers say: wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #31 Warhol blotted line — own sheet
own sheet 600 × 600 · Ink 1.00 · 6 px · 4.9 s

![Brush Artist · Refs · #31 Warhol blotted line — own sheet](Brush-Artist-Refs-31-Warhol-blotted-line-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 21 % → 42 % | 15.8 px | 0.82 | 1.98 | 94 |
| stroke 2 | 17 % → 23 % | 15.9 px | 0.82 | 1.34 | 75 |
| stroke 3 | 24 % → 25 % | 25.1 px | 0.81 | 1.02 | 78 |
| stroke 4 | 31 % → 40 % | 31.8 px | 0.82 | 1.28 | 51 |
| stroke 5 | 35 % → 44 % | 36.4 px | 0.82 | 1.23 | 87 |
| stroke 6 | 32 % → 33 % | 26.7 px | 0.81 | 1.03 | 146 |

Numbers say: wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #32 Thick orange swipes — own sheet
own sheet 600 × 600 · Impasto 1.00 · 90 px · 3.7 s

![Brush Artist · Refs · #32 Thick orange swipes — own sheet](Brush-Artist-Refs-32-Thick-orange-swipes-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 14 % → 27 % | 86.1 px | 0.03 | 1.90 | 361 |
| stroke 2 | 26 % → 38 % | 177.0 px | 0.03 | 1.43 | 304 |
| stroke 3 | 28 % → 27 % | 177.6 px | 0.03 | 0.98 | 301 |

Numbers say: wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #33 Red wet-in-wet band — own sheet
own sheet 600 × 600 · Watercolour 1.00 · 80 px · 9.8 s

![Brush Artist · Refs · #33 Red wet-in-wet band — own sheet](Brush-Artist-Refs-33-Red-wet-in-wet-band-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 24 % → 58 % | 89.6 px | 0.62 | 2.46 | 376 |
| stroke 2 | 30 % → 52 % | 245.5 px | 0.63 | 1.72 | 103 |
| stroke 3 | 37 % → 54 % | 358.6 px | 0.62 | 1.46 | 113 |
| stroke 4 | 43 % → 61 % | 414.5 px | 0.63 | 1.42 | 94 |
| stroke 5 | 42 % → 56 % | 356.1 px | 0.63 | 1.32 | 128 |
| stroke 6 | 43 % → 48 % | 327.4 px | 0.61 | 1.12 | 152 |

Numbers say: wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #34 Magenta oil patches — own sheet
own sheet 600 × 600 · Oil 0.89 · Oil glaze 0.11 · 60 px · 5.0 s

![Brush Artist · Refs · #34 Magenta oil patches — own sheet](Brush-Artist-Refs-34-Magenta-oil-patches-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 9 % → 42 % | 62.0 px | 0.13 | 4.82 | 86 |
| stroke 2 | 9 % → 29 % | 62.8 px | 0.13 | 3.15 | 70 |
| stroke 3 | 7 % → 35 % | 62.4 px | 0.13 | 4.71 | 63 |
| stroke 4 | 16 % → 20 % | 132.1 px | 0.12 | 1.27 | 62 |
| stroke 5 | 23 % → 33 % | 124.6 px | 0.13 | 1.43 | 106 |
| stroke 6 | 20 % → 38 % | 171.6 px | 0.13 | 1.90 | 61 |
| stroke 7 | 30 % → 35 % | 238.0 px | 0.13 | 1.18 | 70 |
| stroke 8 | 33 % → 39 % | 235.2 px | 0.13 | 1.18 | 87 |
| stroke 9 | 25 % → 26 % | 159.9 px | 0.13 | 1.07 | 88 |
| stroke 10 | 29 % → 29 % | 257.6 px | 0.13 | 1.00 | 66 |
| stroke 11 | 36 % → 36 % | 324.9 px | 0.13 | 1.00 | 66 |
| stroke 12 | 26 % → 26 % | 184.7 px | 0.13 | 1.00 | 68 |

Numbers say: wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #35 Red band with runs — own sheet
own sheet 600 × 600 · Watercolour 1.00 · 70 px · 6.3 s

![Brush Artist · Refs · #35 Red band with runs — own sheet](Brush-Artist-Refs-35-Red-band-with-runs-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 37 % → 41 % | 138.9 px | 0.50 | 1.12 | 363 |

## Brush Artist · Refs · #36 Magenta letters flat brush — own sheet
own sheet 600 × 600 · Gouache 1.00 · 36 px · 11.8 s

![Brush Artist · Refs · #36 Magenta letters flat brush — own sheet](Brush-Artist-Refs-36-Magenta-letters-flat-brush-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 20 % → 39 % | 59.0 px | 0.50 | 1.95 | 32 |
| stroke 2 | 20 % → 32 % | 46.6 px | 0.50 | 1.59 | 32 |
| stroke 3 | 29 % → 54 % | 86.8 px | 0.50 | 1.86 | 30 |
| stroke 4 | 26 % → 44 % | 51.2 px | 0.50 | 1.67 | 122 |
| stroke 5 | 33 % → 55 % | 96.1 px | 0.50 | 1.67 | 78 |
| stroke 6 | 42 % → 56 % | 242.4 px | 0.50 | 1.33 | 22 |
| stroke 7 | 30 % → 44 % | 56.7 px | 0.50 | 1.45 | 127 |
| stroke 8 | 31 % → 53 % | 98.5 px | 0.50 | 1.68 | 76 |
| stroke 9 | 38 % → 51 % | 158.3 px | 0.50 | 1.33 | 31 |
| stroke 10 | 37 % → 63 % | 106.7 px | 0.50 | 1.72 | 73 |
| stroke 11 | 39 % → 62 % | 225.9 px | 0.50 | 1.58 | 15 |
| stroke 12 | 43 % → 56 % | 81.9 px | 0.50 | 1.29 | 120 |
| stroke 13 | 32 % → 46 % | 117.6 px | 0.50 | 1.43 | 31 |
| stroke 14 | 35 % → 52 % | 134.4 px | 0.50 | 1.47 | 30 |
| stroke 15 | 38 % → 56 % | 108.5 px | 0.50 | 1.49 | 82 |
| stroke 16 | 41 % → 50 % | 232.0 px | 0.50 | 1.23 | 15 |
| stroke 17 | 44 % → 52 % | 81.7 px | 0.50 | 1.19 | 107 |
| stroke 18 | 27 % → 36 % | 97.5 px | 0.50 | 1.35 | 30 |
| stroke 19 | 40 % → 39 % | 117.0 px | 0.50 | 0.96 | 31 |
| stroke 20 | 45 % → 45 % | 132.2 px | 0.50 | 0.99 | 34 |
| stroke 21 | 41 % → 39 % | 78.6 px | 0.50 | 0.96 | 82 |

Numbers say: wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #37 Oil still life dabs — own sheet
own sheet 600 × 600 · Oil 0.89 · Oil glaze 0.11 · 40 px · 3.7 s

![Brush Artist · Refs · #37 Oil still life dabs — own sheet](Brush-Artist-Refs-37-Oil-still-life-dabs-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 7 % → 7 % | 44.2 px | 0.39 | 1.00 | 35 |
| stroke 2 | 6 % → 28 % | 44.5 px | 0.39 | 4.43 | 26 |
| stroke 3 | 12 % → 36 % | 92.9 px | 0.39 | 3.00 | 22 |
| stroke 4 | 9 % → 9 % | 42.8 px | 0.39 | 1.00 | 43 |
| stroke 5 | 6 % → 10 % | 43.2 px | 0.39 | 1.72 | 25 |
| stroke 6 | 13 % → 31 % | 83.6 px | 0.39 | 2.32 | 34 |
| stroke 7 | 11 % → 24 % | 115.9 px | 0.39 | 2.18 | 15 |
| stroke 8 | 8 % → 14 % | 90.0 px | 0.39 | 1.63 | 16 |
| stroke 9 | 13 % → 14 % | 68.1 px | 0.38 | 1.09 | 43 |
| stroke 10 | 21 % → 25 % | 106.6 px | 0.39 | 1.20 | 43 |
| stroke 11 | 24 % → 28 % | 201.8 px | 0.39 | 1.17 | 22 |
| stroke 12 | 21 % → 21 % | 228.5 px | 0.39 | 1.01 | 14 |
| stroke 13 | 16 % → 16 % | 168.0 px | 0.40 | 1.00 | 14 |
| stroke 14 | 17 % → 17 % | 133.3 px | 0.39 | 1.00 | 20 |

Numbers say: wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #38 Sanguine drawing — own sheet
own sheet 600 × 600 · Pastel 1.00 · 6 px · 2.4 s

![Brush Artist · Refs · #38 Sanguine drawing — own sheet](Brush-Artist-Refs-38-Sanguine-drawing-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 3 % → 14 % | 2.9 px | 0.57 | 5.30 | 8 |
| stroke 2 | 3 % → 7 % | 2.9 px | 0.58 | 2.89 | 7 |
| stroke 3 | 3 % → 9 % | 2.9 px | 0.57 | 3.40 | 8 |
| stroke 4 | 2 % → 17 % | 2.7 px | 0.57 | 7.20 | 8 |
| stroke 5 | 2 % → 7 % | 2.7 px | 0.57 | 3.03 | 6 |
| stroke 6 | 3 % → 19 % | 3.4 px | 0.57 | 6.31 | 7 |
| stroke 7 | 5 % → 14 % | 5.2 px | 0.57 | 3.07 | 6 |
| stroke 8 | 4 % → 16 % | 4.7 px | 0.57 | 3.79 | 7 |
| stroke 9 | 3 % → 7 % | 2.9 px | 0.57 | 2.66 | 8 |
| stroke 10 | 4 % → 16 % | 4.7 px | 0.57 | 3.83 | 7 |
| stroke 11 | 3 % → 4 % | 2.9 px | 0.57 | 1.61 | 7 |
| stroke 12 | 4 % → 15 % | 4.8 px | 0.57 | 3.58 | 7 |
| stroke 13 | 8 % → 17 % | 8.9 px | 0.57 | 2.23 | 6 |
| stroke 14 | 4 % → 14 % | 4.9 px | 0.57 | 3.19 | 7 |
| stroke 15 | 9 % → 18 % | 10.7 px | 0.57 | 1.86 | 7 |
| stroke 16 | 6 % → 16 % | 6.6 px | 0.57 | 2.71 | 10 |
| stroke 17 | 4 % → 9 % | 4.4 px | 0.57 | 2.25 | 13 |
| stroke 18 | 3 % → 5 % | 2.9 px | 0.57 | 1.85 | 8 |
| stroke 19 | 6 % → 16 % | 6.9 px | 0.57 | 2.68 | 7 |
| stroke 20 | 8 % → 14 % | 9.2 px | 0.57 | 1.70 | 7 |
| stroke 21 | 4 % → 4 % | 4.3 px | 0.57 | 1.00 | 6 |
| stroke 22 | 8 % → 13 % | 8.6 px | 0.57 | 1.79 | 6 |
| stroke 23 | 7 % → 12 % | 8.3 px | 0.57 | 1.61 | 7 |
| stroke 24 | 4 % → 7 % | 4.7 px | 0.57 | 1.71 | 7 |
| stroke 25 | 8 % → 14 % | 8.7 px | 0.57 | 1.84 | 7 |
| stroke 26 | 6 % → 8 % | 6.5 px | 0.57 | 1.34 | 6 |
| stroke 27 | 4 % → 4 % | 4.3 px | 0.57 | 1.10 | 7 |
| stroke 28 | 7 % → 11 % | 8.2 px | 0.57 | 1.59 | 10 |
| stroke 29 | 8 % → 17 % | 8.8 px | 0.57 | 2.21 | 7 |
| stroke 30 | 13 % → 17 % | 14.9 px | 0.57 | 1.29 | 7 |
| stroke 31 | 5 % → 6 % | 5.4 px | 0.57 | 1.29 | 7 |
| stroke 32 | 10 % → 13 % | 11.8 px | 0.57 | 1.24 | 7 |
| stroke 33 | 7 % → 8 % | 8.5 px | 0.57 | 1.07 | 7 |
| stroke 34 | 11 % → 14 % | 12.0 px | 0.57 | 1.36 | 8 |
| stroke 35 | 9 % → 14 % | 10.0 px | 0.57 | 1.61 | 6 |
| stroke 36 | 10 % → 13 % | 11.4 px | 0.57 | 1.26 | 7 |
| stroke 37 | 9 % → 16 % | 10.5 px | 0.57 | 1.71 | 7 |
| stroke 38 | 13 % → 19 % | 14.8 px | 0.57 | 1.48 | 7 |
| stroke 39 | 14 % → 17 % | 15.7 px | 0.57 | 1.21 | 7 |
| stroke 40 | 6 % → 7 % | 7.2 px | 0.57 | 1.14 | 6 |
| stroke 41 | 16 % → 16 % | 17.7 px | 0.57 | 1.01 | 7 |
| stroke 42 | 14 % → 16 % | 15.2 px | 0.57 | 1.17 | 7 |
| stroke 43 | 10 % → 12 % | 11.6 px | 0.57 | 1.17 | 6 |
| stroke 44 | 12 % → 15 % | 14.3 px | 0.57 | 1.22 | 7 |
| stroke 45 | 2 % → 2 % | 2.7 px | 0.57 | 1.00 | 7 |
| stroke 46 | 16 % → 16 % | 18.5 px | 0.57 | 1.00 | 6 |
| stroke 47 | 13 % → 13 % | 15.0 px | 0.57 | 1.00 | 7 |
| stroke 48 | 12 % → 13 % | 14.3 px | 0.57 | 1.07 | 9 |
| stroke 49 | 19 % → 19 % | 21.5 px | 0.57 | 1.00 | 7 |
| stroke 50 | 10 % → 10 % | 11.6 px | 0.57 | 1.00 | 7 |

Numbers say: wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #39 Very thick impasto — own sheet
own sheet 600 × 600 · Impasto 1.00 · 60 px · 5.1 s

![Brush Artist · Refs · #39 Very thick impasto — own sheet](Brush-Artist-Refs-39-Very-thick-impasto-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 26 % → 37 % | 59.6 px | 0.43 | 1.42 | 279 |
| stroke 2 | 31 % → 48 % | 93.9 px | 0.44 | 1.54 | 275 |
| stroke 3 | 37 % → 49 % | 124.6 px | 0.43 | 1.33 | 254 |
| stroke 4 | 31 % → 44 % | 90.9 px | 0.44 | 1.41 | 310 |
| stroke 5 | 42 % → 41 % | 104.2 px | 0.44 | 0.98 | 404 |

Numbers say: wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #40 Watercolour blooms — own sheet
own sheet 600 × 600 · Watercolour 1.00 · 90 px · 7.3 s

![Brush Artist · Refs · #40 Watercolour blooms — own sheet](Brush-Artist-Refs-40-Watercolour-blooms-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 22 % → 27 % | 95.0 px | 0.12 | 1.26 | 738 |

## Brush Artist · Refs · #41 Coloured pencil hatching — own sheet
own sheet 600 × 600 · Pastel 1.00 · 4 px · 2.6 s

![Brush Artist · Refs · #41 Coloured pencil hatching — own sheet](Brush-Artist-Refs-41-Coloured-pencil-hatching-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 3 % → 13 % | 2.2 px | 0.35 | 4.64 | 9 |
| stroke 2 | 3 % → 7 % | 2.3 px | 0.35 | 2.29 | 4 |
| stroke 3 | 2 % → 11 % | 1.9 px | 0.35 | 4.38 | 4 |
| stroke 4 | 3 % → 19 % | 2.1 px | 0.35 | 6.73 | 11 |
| stroke 5 | 4 % → 7 % | 2.9 px | 0.35 | 1.83 | 5 |
| stroke 6 | 3 % → 13 % | 2.3 px | 0.35 | 4.19 | 4 |
| stroke 7 | 3 % → 15 % | 2.6 px | 0.35 | 4.43 | 5 |
| stroke 8 | 3 % → 12 % | 2.1 px | 0.35 | 4.20 | 4 |
| stroke 9 | 5 % → 11 % | 3.6 px | 0.35 | 2.27 | 4 |
| stroke 10 | 5 % → 15 % | 3.8 px | 0.35 | 2.99 | 4 |
| stroke 11 | 4 % → 13 % | 3.0 px | 0.35 | 3.28 | 5 |
| stroke 12 | 3 % → 3 % | 2.1 px | 0.35 | 1.00 | 4 |
| stroke 13 | 7 % → 17 % | 5.2 px | 0.35 | 2.45 | 4 |
| stroke 14 | 3 % → 13 % | 2.4 px | 0.35 | 4.19 | 4 |
| stroke 15 | 6 % → 12 % | 4.4 px | 0.35 | 2.09 | 5 |
| stroke 16 | 7 % → 11 % | 5.1 px | 0.35 | 1.61 | 5 |
| stroke 17 | 3 % → 3 % | 2.1 px | 0.35 | 1.00 | 4 |
| stroke 18 | 5 % → 8 % | 3.6 px | 0.35 | 1.65 | 4 |
| stroke 19 | 5 % → 13 % | 3.8 px | 0.35 | 2.72 | 4 |
| stroke 20 | 5 % → 14 % | 3.7 px | 0.35 | 2.92 | 5 |
| stroke 21 | 4 % → 13 % | 3.2 px | 0.35 | 3.20 | 4 |
| stroke 22 | 9 % → 16 % | 6.8 px | 0.35 | 1.77 | 4 |
| stroke 23 | 9 % → 13 % | 6.5 px | 0.35 | 1.55 | 4 |
| stroke 24 | 6 % → 14 % | 4.7 px | 0.35 | 2.18 | 4 |
| stroke 25 | 5 % → 10 % | 3.5 px | 0.35 | 2.27 | 4 |
| stroke 26 | 3 % → 6 % | 2.7 px | 0.35 | 1.81 | 4 |
| stroke 27 | 3 % → 7 % | 2.3 px | 0.35 | 2.26 | 4 |
| stroke 28 | 6 % → 10 % | 4.5 px | 0.35 | 1.70 | 4 |
| stroke 29 | 3 % → 13 % | 2.4 px | 0.35 | 4.21 | 4 |
| stroke 30 | 6 % → 9 % | 4.4 px | 0.35 | 1.46 | 4 |
| stroke 31 | 7 % → 14 % | 5.1 px | 0.35 | 2.14 | 4 |
| stroke 32 | 3 % → 6 % | 2.5 px | 0.35 | 1.78 | 7 |
| stroke 33 | 6 % → 11 % | 5.0 px | 0.35 | 1.67 | 4 |
| stroke 34 | 3 % → 6 % | 2.6 px | 0.35 | 1.73 | 4 |
| stroke 35 | 7 % → 14 % | 5.0 px | 0.35 | 2.09 | 4 |
| stroke 36 | 5 % → 5 % | 3.7 px | 0.35 | 1.01 | 4 |
| stroke 37 | 7 % → 15 % | 5.2 px | 0.35 | 2.15 | 4 |
| stroke 38 | 8 % → 13 % | 5.8 px | 0.35 | 1.66 | 4 |
| stroke 39 | 7 % → 11 % | 5.1 px | 0.35 | 1.67 | 4 |
| stroke 40 | 8 % → 18 % | 6.2 px | 0.35 | 2.21 | 6 |
| stroke 41 | 9 % → 13 % | 6.9 px | 0.35 | 1.48 | 4 |
| stroke 42 | 10 % → 17 % | 7.7 px | 0.35 | 1.73 | 5 |
| stroke 43 | 5 % → 9 % | 3.9 px | 0.35 | 1.66 | 4 |
| stroke 44 | 10 % → 13 % | 7.3 px | 0.35 | 1.40 | 4 |
| stroke 45 | 13 % → 18 % | 9.9 px | 0.35 | 1.35 | 4 |
| stroke 46 | 5 % → 7 % | 3.6 px | 0.34 | 1.41 | 4 |
| stroke 47 | 11 % → 13 % | 8.0 px | 0.35 | 1.20 | 4 |
| stroke 48 | 12 % → 16 % | 9.2 px | 0.35 | 1.34 | 7 |
| stroke 49 | 6 % → 9 % | 4.2 px | 0.35 | 1.65 | 4 |
| stroke 50 | 7 % → 7 % | 5.2 px | 0.34 | 1.00 | 4 |
| stroke 51 | 8 % → 15 % | 6.4 px | 0.35 | 1.74 | 4 |
| stroke 52 | 12 % → 14 % | 9.1 px | 0.35 | 1.19 | 4 |
| stroke 53 | 11 % → 14 % | 8.1 px | 0.35 | 1.36 | 5 |
| stroke 54 | 10 % → 14 % | 7.4 px | 0.35 | 1.47 | 4 |
| stroke 55 | 11 % → 14 % | 8.2 px | 0.35 | 1.33 | 4 |
| stroke 56 | 11 % → 12 % | 8.4 px | 0.35 | 1.11 | 5 |
| stroke 57 | 9 % → 13 % | 7.1 px | 0.35 | 1.37 | 4 |
| stroke 58 | 10 % → 11 % | 7.7 px | 0.35 | 1.14 | 4 |
| stroke 59 | 11 % → 13 % | 8.4 px | 0.35 | 1.18 | 4 |
| stroke 60 | 16 % → 20 % | 11.9 px | 0.35 | 1.26 | 4 |
| stroke 61 | 19 % → 20 % | 14.5 px | 0.35 | 1.04 | 4 |
| stroke 62 | 10 % → 10 % | 7.3 px | 0.35 | 1.00 | 4 |
| stroke 63 | 11 % → 12 % | 8.7 px | 0.35 | 1.07 | 4 |
| stroke 64 | 14 % → 14 % | 10.7 px | 0.35 | 1.02 | 4 |
| stroke 65 | 15 % → 15 % | 11.5 px | 0.35 | 1.00 | 4 |
| stroke 66 | 14 % → 14 % | 10.7 px | 0.35 | 1.00 | 4 |
| stroke 67 | 12 % → 12 % | 8.8 px | 0.35 | 1.06 | 4 |
| stroke 68 | 5 % → 9 % | 3.6 px | 0.35 | 1.88 | 4 |
| stroke 69 | 5 % → 5 % | 4.1 px | 0.35 | 1.00 | 4 |
| stroke 70 | 10 % → 13 % | 7.4 px | 0.35 | 1.28 | 4 |
| stroke 71 | 9 % → 11 % | 7.1 px | 0.35 | 1.15 | 5 |
| stroke 72 | 5 % → 7 % | 4.2 px | 0.35 | 1.23 | 8 |
| stroke 73 | 12 % → 12 % | 9.3 px | 0.35 | 1.00 | 12 |
| stroke 74 | 14 % → 14 % | 10.8 px | 0.35 | 1.00 | 5 |
| stroke 75 | 15 % → 15 % | 11.4 px | 0.35 | 1.00 | 5 |
| stroke 76 | 14 % → 14 % | 10.5 px | 0.35 | 1.00 | 4 |
| stroke 77 | 7 % → 10 % | 5.4 px | 0.35 | 1.34 | 4 |
| stroke 78 | 9 % → 9 % | 7.0 px | 0.35 | 1.00 | 6 |
| stroke 79 | 7 % → 7 % | 5.7 px | 0.35 | 1.00 | 7 |
| stroke 80 | 11 % → 11 % | 8.3 px | 0.35 | 1.00 | 6 |

Numbers say: wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #42 Oil pastel shaggy — own sheet
own sheet 600 × 600 · Pastel 1.00 · 18 px · 2.6 s

![Brush Artist · Refs · #42 Oil pastel shaggy — own sheet](Brush-Artist-Refs-42-Oil-pastel-shaggy-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 5 % → 27 % | 8.0 px | 0.28 | 5.73 | 11 |
| stroke 2 | 5 % → 24 % | 8.6 px | 0.28 | 4.69 | 10 |
| stroke 3 | 5 % → 29 % | 8.9 px | 0.28 | 5.42 | 10 |
| stroke 4 | 5 % → 11 % | 8.8 px | 0.28 | 2.08 | 10 |
| stroke 5 | 6 % → 11 % | 9.9 px | 0.28 | 1.85 | 10 |
| stroke 6 | 8 % → 37 % | 13.9 px | 0.29 | 4.44 | 10 |
| stroke 7 | 11 % → 31 % | 17.6 px | 0.28 | 2.90 | 10 |
| stroke 8 | 7 % → 38 % | 11.4 px | 0.28 | 5.55 | 10 |
| stroke 9 | 8 % → 21 % | 13.9 px | 0.28 | 2.53 | 10 |
| stroke 10 | 8 % → 18 % | 13.2 px | 0.28 | 2.32 | 12 |
| stroke 11 | 6 % → 27 % | 9.4 px | 0.28 | 4.74 | 10 |
| stroke 12 | 8 % → 19 % | 13.6 px | 0.28 | 2.29 | 10 |
| stroke 13 | 13 % → 24 % | 21.0 px | 0.28 | 1.92 | 10 |
| stroke 14 | 5 % → 23 % | 7.9 px | 0.28 | 4.77 | 10 |
| stroke 15 | 5 % → 24 % | 9.0 px | 0.29 | 4.38 | 12 |
| stroke 16 | 9 % → 21 % | 15.7 px | 0.29 | 2.18 | 10 |
| stroke 17 | 17 % → 39 % | 28.0 px | 0.29 | 2.34 | 10 |
| stroke 18 | 14 % → 25 % | 22.8 px | 0.29 | 1.79 | 10 |
| stroke 19 | 15 % → 32 % | 24.9 px | 0.28 | 2.09 | 10 |
| stroke 20 | 21 % → 39 % | 35.1 px | 0.28 | 1.85 | 10 |
| stroke 21 | 9 % → 16 % | 14.4 px | 0.28 | 1.88 | 11 |
| stroke 22 | 14 % → 17 % | 23.9 px | 0.28 | 1.20 | 10 |
| stroke 23 | 12 % → 17 % | 20.6 px | 0.29 | 1.34 | 10 |
| stroke 24 | 18 % → 26 % | 30.0 px | 0.29 | 1.44 | 10 |
| stroke 25 | 20 % → 34 % | 32.6 px | 0.28 | 1.74 | 10 |
| stroke 26 | 6 % → 14 % | 9.2 px | 0.28 | 2.43 | 10 |
| stroke 27 | 18 % → 26 % | 30.5 px | 0.29 | 1.41 | 10 |
| stroke 28 | 14 % → 24 % | 23.7 px | 0.28 | 1.68 | 10 |
| stroke 29 | 9 % → 27 % | 14.9 px | 0.29 | 3.01 | 10 |
| stroke 30 | 15 % → 36 % | 25.0 px | 0.29 | 2.43 | 10 |
| stroke 31 | 14 % → 17 % | 23.3 px | 0.28 | 1.23 | 10 |
| stroke 32 | 16 % → 29 % | 27.0 px | 0.29 | 1.82 | 10 |
| stroke 33 | 15 % → 16 % | 24.5 px | 0.29 | 1.09 | 10 |
| stroke 34 | 19 % → 27 % | 31.4 px | 0.28 | 1.44 | 10 |
| stroke 35 | 26 % → 36 % | 42.6 px | 0.28 | 1.40 | 10 |
| stroke 36 | 25 % → 34 % | 41.0 px | 0.28 | 1.36 | 11 |
| stroke 37 | 12 % → 12 % | 19.3 px | 0.28 | 1.03 | 13 |
| stroke 38 | 19 % → 25 % | 31.7 px | 0.28 | 1.30 | 10 |
| stroke 39 | 16 % → 22 % | 27.3 px | 0.28 | 1.37 | 10 |
| stroke 40 | 22 % → 31 % | 36.6 px | 0.28 | 1.38 | 10 |
| stroke 41 | 32 % → 36 % | 53.1 px | 0.28 | 1.12 | 10 |
| stroke 42 | 23 % → 30 % | 38.2 px | 0.29 | 1.29 | 10 |
| stroke 43 | 12 % → 12 % | 20.3 px | 0.28 | 1.00 | 10 |
| stroke 44 | 30 % → 37 % | 48.9 px | 0.28 | 1.26 | 10 |
| stroke 45 | 16 % → 16 % | 26.2 px | 0.28 | 1.00 | 10 |
| stroke 46 | 29 % → 34 % | 48.0 px | 0.29 | 1.15 | 10 |
| stroke 47 | 38 % → 41 % | 62.0 px | 0.28 | 1.10 | 10 |
| stroke 48 | 29 % → 36 % | 47.8 px | 0.29 | 1.27 | 12 |
| stroke 49 | 27 % → 30 % | 45.1 px | 0.29 | 1.11 | 10 |
| stroke 50 | 38 % → 40 % | 63.4 px | 0.28 | 1.06 | 10 |
| stroke 51 | 16 % → 16 % | 26.1 px | 0.28 | 1.00 | 10 |
| stroke 52 | 37 % → 38 % | 62.4 px | 0.29 | 1.01 | 10 |
| stroke 53 | 22 % → 26 % | 36.9 px | 0.28 | 1.18 | 10 |
| stroke 54 | 17 % → 19 % | 29.1 px | 0.29 | 1.09 | 10 |
| stroke 55 | 15 % → 15 % | 25.0 px | 0.28 | 1.00 | 10 |
| stroke 56 | 13 % → 14 % | 21.6 px | 0.28 | 1.08 | 10 |
| stroke 57 | 23 % → 23 % | 37.7 px | 0.29 | 1.00 | 10 |
| stroke 58 | 28 % → 29 % | 46.1 px | 0.28 | 1.05 | 9 |
| stroke 59 | 40 % → 40 % | 67.3 px | 0.28 | 1.00 | 10 |
| stroke 60 | 22 % → 22 % | 35.6 px | 0.28 | 1.00 | 10 |

Numbers say: wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #43 Dragged black ink blocks — own sheet
own sheet 600 × 600 · Gouache 1.00 · 70 px · 7.4 s

![Brush Artist · Refs · #43 Dragged black ink blocks — own sheet](Brush-Artist-Refs-43-Dragged-black-ink-blocks-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 17 % → 9 % | 40.1 px | 0.44 | 0.50 | 386 |
| stroke 2 | 19 % → 13 % | 68.1 px | 0.44 | 0.70 | 425 |
| stroke 3 | 21 % → 15 % | 76.9 px | 0.44 | 0.68 | 388 |
| stroke 4 | 22 % → 13 % | 75.7 px | 0.44 | 0.59 | 393 |
| stroke 5 | 29 % → 14 % | 66.6 px | 0.44 | 0.50 | 433 |

## Brush Artist · Refs · #44 Blue looping ribbon — own sheet
own sheet 600 × 600 · Oil 1.00 · 80 px · 5.0 s

![Brush Artist · Refs · #44 Blue looping ribbon — own sheet](Brush-Artist-Refs-44-Blue-looping-ribbon-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 32 % → 32 % | 42.2 px | 0.78 | 1.00 | 2576 |

## Brush Artist · Refs · #45 Soft pastel pepper — own sheet
own sheet 600 × 600 · Pastel 1.00 · 40 px · 4.6 s

![Brush Artist · Refs · #45 Soft pastel pepper — own sheet](Brush-Artist-Refs-45-Soft-pastel-pepper-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 10 % → 39 % | 11.3 px | 0.49 | 3.75 | 350 |
| stroke 2 | 18 % → 34 % | 21.3 px | 0.49 | 1.87 | 317 |
| stroke 3 | 25 % → 37 % | 17.6 px | 0.49 | 1.46 | 318 |
| stroke 4 | 24 % → 35 % | 30.5 px | 0.49 | 1.43 | 354 |
| stroke 5 | 30 % → 30 % | 21.2 px | 0.49 | 1.00 | 225 |
| stroke 6 | 36 % → 44 % | 23.0 px | 0.48 | 1.23 | 333 |
| stroke 7 | 39 % → 43 % | 21.6 px | 0.48 | 1.10 | 376 |
| stroke 8 | 44 % → 44 % | 44.4 px | 0.49 | 1.00 | 342 |

Numbers say: wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #46 Red-brown ink lips — own sheet
own sheet 600 × 600 · Watercolour 1.00 · 50 px · 6.0 s

![Brush Artist · Refs · #46 Red-brown ink lips — own sheet](Brush-Artist-Refs-46-Red-brown-ink-lips-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 13 % → 27 % | 55.7 px | 0.59 | 2.00 | 104 |
| stroke 2 | 19 % → 33 % | 82.1 px | 0.54 | 1.76 | 155 |

Numbers say: wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #47 Pink knife slabs — own sheet
own sheet 600 × 600 · Impasto 1.00 · 90 px · 5.2 s

![Brush Artist · Refs · #47 Pink knife slabs — own sheet](Brush-Artist-Refs-47-Pink-knife-slabs-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 17 % → 32 % | 83.2 px | 0.11 | 1.94 | 295 |
| stroke 2 | 29 % → 43 % | 165.8 px | 0.11 | 1.46 | 442 |
| stroke 3 | 29 % → 43 % | 165.7 px | 0.11 | 1.47 | 425 |
| stroke 4 | 39 % → 38 % | 165.7 px | 0.11 | 0.98 | 308 |

Numbers say: wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #48 Black bands with drips — own sheet
own sheet 600 × 600 · Gouache 1.00 · 70 px · 13.8 s

![Brush Artist · Refs · #48 Black bands with drips — own sheet](Brush-Artist-Refs-48-Black-bands-with-drips-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 28 % → 41 % | 73.2 px | 0.39 | 1.46 | 777 |
| stroke 2 | 43 % → 57 % | 137.5 px | 0.39 | 1.33 | 602 |
| stroke 3 | 45 % → 57 % | 141.4 px | 0.39 | 1.27 | 466 |
| stroke 4 | 48 % → 46 % | 140.3 px | 0.39 | 0.96 | 476 |

## Brush Artist · Refs · #49 Magenta letters round brush — own sheet
own sheet 600 × 600 · Ink 1.00 · 30 px · 11.6 s

![Brush Artist · Refs · #49 Magenta letters round brush — own sheet](Brush-Artist-Refs-49-Magenta-letters-round-brush-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 27 % → 46 % | 64.3 px | 0.52 | 1.70 | 37 |
| stroke 2 | 29 % → 40 % | 52.5 px | 0.53 | 1.40 | 32 |
| stroke 3 | 41 % → 67 % | 96.3 px | 0.52 | 1.64 | 34 |
| stroke 4 | 34 % → 52 % | 53.7 px | 0.52 | 1.55 | 105 |
| stroke 5 | 40 % → 66 % | 94.7 px | 0.52 | 1.65 | 70 |
| stroke 6 | 54 % → 70 % | 231.2 px | 0.52 | 1.29 | 15 |
| stroke 7 | 41 % → 56 % | 63.9 px | 0.52 | 1.35 | 118 |
| stroke 8 | 36 % → 61 % | 91.9 px | 0.53 | 1.73 | 65 |
| stroke 9 | 49 % → 60 % | 152.9 px | 0.53 | 1.24 | 28 |
| stroke 10 | 42 % → 72 % | 100.4 px | 0.52 | 1.71 | 89 |
| stroke 11 | 52 % → 72 % | 219.8 px | 0.52 | 1.39 | 15 |
| stroke 12 | 53 % → 68 % | 82.2 px | 0.52 | 1.29 | 116 |
| stroke 13 | 42 % → 54 % | 115.9 px | 0.53 | 1.29 | 31 |
| stroke 14 | 45 % → 69 % | 131.7 px | 0.53 | 1.52 | 33 |
| stroke 15 | 43 % → 63 % | 102.4 px | 0.52 | 1.46 | 76 |
| stroke 16 | 52 % → 61 % | 220.3 px | 0.52 | 1.18 | 15 |
| stroke 17 | 53 % → 64 % | 82.2 px | 0.52 | 1.19 | 111 |
| stroke 18 | 36 % → 44 % | 99.6 px | 0.52 | 1.22 | 51 |
| stroke 19 | 54 % → 53 % | 123.7 px | 0.52 | 0.99 | 37 |
| stroke 20 | 54 % → 54 % | 125.3 px | 0.52 | 1.00 | 43 |
| stroke 21 | 49 % → 49 % | 81.3 px | 0.52 | 1.00 | 81 |

Numbers say: wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #50 Thick swipes on photo — own sheet
own sheet 600 × 600 · Impasto 1.00 · 40 px · 3.2 s

![Brush Artist · Refs · #50 Thick swipes on photo — own sheet](Brush-Artist-Refs-50-Thick-swipes-on-photo-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 9 % → 21 % | 42.8 px | 0.33 | 2.35 | 36 |
| stroke 2 | 9 % → 16 % | 42.5 px | 0.33 | 1.79 | 27 |
| stroke 3 | 10 % → 11 % | 41.9 px | 0.33 | 1.07 | 40 |
| stroke 4 | 11 % → 18 % | 42.7 px | 0.33 | 1.64 | 50 |
| stroke 5 | 11 % → 10 % | 41.9 px | 0.33 | 0.95 | 34 |
| stroke 6 | 17 % → 21 % | 97.7 px | 0.32 | 1.20 | 27 |
| stroke 7 | 22 % → 26 % | 92.8 px | 0.33 | 1.18 | 39 |
| stroke 8 | 21 % → 21 % | 119.9 px | 0.33 | 0.97 | 38 |
| stroke 9 | 9 % → 10 % | 42.1 px | 0.32 | 1.09 | 54 |
| stroke 10 | 22 % → 21 % | 73.6 px | 0.32 | 0.96 | 62 |
| stroke 11 | 9 % → 8 % | 42.7 px | 0.33 | 0.95 | 42 |
| stroke 12 | 17 % → 16 % | 93.2 px | 0.33 | 0.96 | 36 |

Numbers say: wet paint spreads well beyond the stroke.

## Brush Artist · Ink — dry brush — own sheet
own sheet 600 × 600 · Gouache 1.00 · 30 px · 3.4 s

![Brush Artist · Ink — dry brush — own sheet](Brush-Artist-Ink-dry-brush-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| ear | 4 % → 2 % | 5.6 px | 0.86 | 0.35 | 539 |
| drag0 | 6 % → 8 % | 10.8 px | 0.86 | 1.30 | 158 |
| drag1 | 8 % → 8 % | 17.0 px | 0.86 | 0.97 | 101 |
| drag2 | 10 % → 8 % | 23.4 px | 0.86 | 0.81 | 88 |
| drag3 | 12 % → 9 % | 30.5 px | 0.86 | 0.72 | 73 |

## Brush Artist · Watercolour — blue — own sheet
own sheet 600 × 600 · Watercolour 0.93 · Ink 0.07 · 40 px · 13.1 s

![Brush Artist · Watercolour — blue — own sheet](Brush-Artist-Watercolour-blue-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| s0 | 7 % → 24 % | 28.8 px | 0.30 | 3.32 | 101 |
| s1 | 6 % → 33 % | 10.1 px | 0.37 | 6.00 | 60 |
| s2 | 10 % → 19 % | 44.2 px | 0.26 | 1.81 | 49 |
| s3 | 10 % → 18 % | 26.7 px | 0.31 | 1.92 | 56 |
| s4 | 14 % → 30 % | 38.6 px | 0.36 | 2.16 | 65 |
| s5 | 19 % → 29 % | 39.3 px | 0.37 | 1.54 | 56 |
| s6 | 18 % → 22 % | 48.7 px | 0.31 | 1.25 | 65 |
| s7 | 25 % → 36 % | 32.7 px | 0.37 | 1.46 | 62 |
| s8 | 21 % → 25 % | 79.8 px | 0.30 | 1.20 | 75 |

Numbers say: wet paint spreads well beyond the stroke.

## Brush Artist · Charcoal — stick — own sheet
own sheet 600 × 600 · Charcoal 0.78 · Pastel 0.22 · 28 px · 1.3 s

![Brush Artist · Charcoal — stick — own sheet](Brush-Artist-Charcoal-stick-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| finger0 | 12 % → 25 % | 21.7 px | 0.83 | 2.02 | 56 |
| tip0 | 12 % → 21 % | 33.4 px | 0.83 | 1.69 | 11 |
| finger1 | 23 % → 40 % | 41.1 px | 0.83 | 1.71 | 39 |
| tip1 | 21 % → 29 % | 56.0 px | 0.83 | 1.41 | 11 |
| finger2 | 23 % → 35 % | 41.3 px | 0.83 | 1.53 | 36 |
| tip2 | 21 % → 29 % | 56.0 px | 0.83 | 1.41 | 14 |
| finger3 | 23 % → 27 % | 41.6 px | 0.83 | 1.15 | 46 |
| tip3 | 21 % → 21 % | 56.3 px | 0.83 | 1.00 | 11 |
| cig0 | 33 % → 46 % | 73.2 px | 0.83 | 1.40 | 13 |
| cig1 | 35 % → 46 % | 78.8 px | 0.83 | 1.29 | 16 |
| cig2 | 38 % → 46 % | 84.4 px | 0.83 | 1.21 | 15 |
| cig3 | 40 % → 46 % | 90.0 px | 0.83 | 1.13 | 15 |
| cig4 | 43 % → 45 % | 95.5 px | 0.83 | 1.06 | 15 |
| cig5 | 45 % → 45 % | 101.1 px | 0.83 | 1.00 | 14 |

Numbers say: wet paint spreads well beyond the stroke.

