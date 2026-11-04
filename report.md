![All brushes](contact.png)

# Brush Lab — 150 brushes · 4 Nov 2026 at 21:12

Every sheet: 1500 × 600, ten strokes in a 5 × 2 grid — 1. light line · 2. heavy line · 3. pressure swell · 4. fast wave · 5. slow wave · 6. spiral · 7. loop · 8. tilted · 9. over the wet one · 10. long, no reload (cell 8 holds «tilted» and «over the wet one» crossed). The CPU reference of Mamay's paint engine; the wet layer settles 20 s at the end.

Columns: **covered** = share of the cell with paint right after the stroke → after settling; **width** = painted area of the stroke ÷ its length (px); **dark** = mean darkness of the painted pixels above the paper's own grain (0 = paper, 1 = black); **spread** = how far wet paint went beyond the stroke (1.0 = stayed); **ms** = the stroke on the CPU; long stroke: paint in each quarter of its length (it should run out: wet → streaks → dry tail).

## Ink Line
Ink · 12 px · 33.6 s

![Ink Line](Ink-Line.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 1 % → 4 % | 4.3 px | 0.55 | 2.45 | 149 |
| heavy line | 5 % → 6 % | 15.7 px | 0.68 | 1.14 | 80 |
| pressure swell | 3 % → 4 % | 11.3 px | 0.64 | 1.40 | 54 |
| fast wave | 10 % → 11 % | 11.2 px | 0.59 | 1.11 | 164 |
| slow wave | 8 % → 10 % | 9.6 px | 0.57 | 1.16 | 168 |
| spiral | 14 % → 15 % | 8.9 px | 0.49 | 1.07 | 276 |
| loop | 8 % → 9 % | 10.6 px | 0.61 | 1.15 | 133 |
| tilted | 5 % → 5 % | 14.3 px | 0.64 | 1.05 | 70 |
| over the wet one | 10 % → 11 % | 12.5 px | 0.64 | 1.15 | 81 |
| long, no reload | 18 % → 17 % | 8.1 px | 0.47 | 0.96 | 432 | quarters: 0.22 → 0.09 → 0.04 → 0.02

Numbers say: light vs heavy: width 4.3 → 15.7 px, dark 0.55 → 0.68; wet paint spreads well beyond the stroke.

## Dense Ink
Ink · 14 px · 34.8 s

![Dense Ink](Dense-Ink.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 5 % → 7 % | 15.2 px | 0.72 | 1.27 | 150 |
| heavy line | 7 % → 7 % | 19.1 px | 0.73 | 1.09 | 93 |
| pressure swell | 5 % → 6 % | 17.9 px | 0.72 | 1.18 | 53 |
| fast wave | 13 % → 13 % | 15.2 px | 0.69 | 1.01 | 191 |
| slow wave | 12 % → 12 % | 13.5 px | 0.67 | 1.04 | 198 |
| spiral | 18 % → 15 % | 12.2 px | 0.65 | 0.80 | 344 |
| loop | 11 % → 12 % | 14.8 px | 0.69 | 1.08 | 183 |
| tilted | 5 % → 6 % | 14.5 px | 0.72 | 1.07 | 128 |
| over the wet one | 12 % → 13 % | 17.7 px | 0.72 | 1.12 | 71 |
| long, no reload | 23 % → 15 % | 10.1 px | 0.64 | 0.66 | 490 | quarters: 0.30 → 0.12 → 0.04 → 0.02

Numbers say: light vs heavy: width 15.2 → 19.1 px, dark 0.72 → 0.73.

## Transparent Wash
Watercolor · 22 px · 35.6 s

![Transparent Wash](Transparent-Wash.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 2 % → 5 % | 6.9 px | 0.27 | 2.26 | 63 |
| heavy line | 7 % → 9 % | 20.4 px | 0.27 | 1.23 | 77 |
| pressure swell | 4 % → 6 % | 15.2 px | 0.28 | 1.54 | 51 |
| fast wave | 14 % → 16 % | 16.1 px | 0.20 | 1.17 | 171 |
| slow wave | 12 % → 15 % | 13.7 px | 0.21 | 1.28 | 245 |
| spiral | 18 % → 22 % | 11.9 px | 0.16 | 1.22 | 257 |
| loop | 11 % → 13 % | 14.5 px | 0.22 | 1.20 | 145 |
| tilted | 8 % → 8 % | 21.1 px | 0.24 | 1.06 | 84 |
| over the wet one | 13 % → 16 % | 16.4 px | 0.24 | 1.19 | 64 |
| long, no reload | 26 % → 32 % | 11.6 px | 0.13 | 1.22 | 434 | quarters: 0.11 → 0.04 → 0.02 → 0.01

Numbers say: light vs heavy: width 6.9 → 20.4 px, dark 0.27 → 0.27; wet paint spreads well beyond the stroke.

## Dry Brush
Gouache · 24 px · 33.3 s

![Dry Brush](Dry-Brush.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 5 % → 1 % | 13.8 px | 0.65 | 0.11 | 153 |
| heavy line | 6 % → 0 % | 18.4 px | 0.65 | 0.02 | 127 |
| pressure swell | 5 % → 0 % | 18.1 px | 0.65 | 0.09 | 75 |
| fast wave | 6 % → 1 % | 6.9 px | 0.65 | 0.08 | 184 |
| slow wave | 7 % → 0 % | 7.8 px | 0.65 | 0.07 | 340 |
| spiral | 7 % → 1 % | 4.4 px | 0.65 | 0.08 | 358 |
| loop | 9 % → 0 % | 12.2 px | 0.65 | 0.05 | 167 |
| tilted | 4 % → 3 % | 10.3 px | 0.65 | 0.89 | 102 |
| over the wet one | 9 % → 1 % | 14.3 px | 0.65 | 0.12 | 86 |
| long, no reload | 6 % → 1 % | 2.7 px | 0.65 | 0.15 | 490 | quarters: 0.12 → 0.00 → 0.00 → 0.00

Numbers say: light vs heavy: width 13.8 → 18.4 px, dark 0.65 → 0.65.

## Wax Crayon
Wax · 8 px · 12.7 s

![Wax Crayon](Wax-Crayon.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 1 % → 1 % | 2.5 px | 0.71 | 1.00 | 128 |
| heavy line | 1 % → 1 % | 3.9 px | 0.69 | 1.00 | 21 |
| pressure swell | 1 % → 1 % | 3.3 px | 0.70 | 1.00 | 14 |
| fast wave | 3 % → 3 % | 3.5 px | 0.69 | 1.00 | 54 |
| slow wave | 3 % → 3 % | 3.4 px | 0.70 | 1.00 | 48 |
| spiral | 5 % → 5 % | 3.3 px | 0.70 | 1.00 | 105 |
| loop | 3 % → 3 % | 3.3 px | 0.70 | 1.00 | 40 |
| tilted | 2 % → 2 % | 5.6 px | 0.68 | 1.00 | 52 |
| over the wet one | 3 % → 3 % | 3.6 px | 0.68 | 1.00 | 25 |
| long, no reload | 7 % → 7 % | 3.3 px | 0.70 | 1.00 | 188 | quarters: 0.06 → 0.06 → 0.06 → 0.06

Numbers say: light vs heavy: width 2.5 → 3.9 px, dark 0.71 → 0.69; the long stroke does not run out of paint.

## Oil Pastel
Wax · 12 px · 13.5 s

![Oil Pastel](Oil-Pastel.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 1 % → 1 % | 4.0 px | 0.68 | 1.00 | 129 |
| heavy line | 2 % → 2 % | 6.5 px | 0.68 | 1.00 | 43 |
| pressure swell | 2 % → 2 % | 5.7 px | 0.69 | 1.00 | 23 |
| fast wave | 5 % → 5 % | 5.7 px | 0.68 | 1.00 | 90 |
| slow wave | 5 % → 5 % | 5.5 px | 0.68 | 1.00 | 71 |
| spiral | 8 % → 8 % | 5.5 px | 0.68 | 1.00 | 153 |
| loop | 4 % → 4 % | 5.6 px | 0.68 | 1.00 | 88 |
| tilted | 2 % → 2 % | 6.8 px | 0.68 | 1.00 | 55 |
| over the wet one | 5 % → 5 % | 5.8 px | 0.68 | 1.00 | 45 |
| long, no reload | 13 % → 13 % | 5.6 px | 0.68 | 1.00 | 232 | quarters: 0.10 → 0.09 → 0.10 → 0.10

Numbers say: light vs heavy: width 4.0 → 6.5 px, dark 0.68 → 0.68; the long stroke does not run out of paint.

## Charcoal
Charcoal · 5 px · 12.7 s

![Charcoal](Charcoal.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 1 % → 1 % | 2.0 px | 0.74 | 1.00 | 108 |
| heavy line | 1 % → 1 % | 3.0 px | 0.74 | 1.00 | 20 |
| pressure swell | 1 % → 1 % | 2.7 px | 0.74 | 1.00 | 11 |
| fast wave | 2 % → 2 % | 2.7 px | 0.73 | 1.00 | 49 |
| slow wave | 2 % → 2 % | 2.6 px | 0.74 | 1.00 | 25 |
| spiral | 4 % → 4 % | 2.5 px | 0.74 | 1.00 | 81 |
| loop | 2 % → 2 % | 2.6 px | 0.74 | 1.00 | 48 |
| tilted | 2 % → 2 % | 4.3 px | 0.72 | 1.00 | 32 |
| over the wet one | 2 % → 2 % | 2.4 px | 0.72 | 1.00 | 17 |
| long, no reload | 6 % → 6 % | 2.7 px | 0.73 | 1.00 | 127 | quarters: 0.05 → 0.05 → 0.05 → 0.05

Numbers say: light vs heavy: width 2.0 → 3.0 px, dark 0.74 → 0.74; the long stroke does not run out of paint.

## Impasto
Heavy acrylic · 22 px · 20.7 s

![Impasto](Impasto.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 8 % → 8 % | 24.1 px | 0.71 | 0.93 | 203 |
| heavy line | 10 % → 9 % | 28.8 px | 0.69 | 0.94 | 118 |
| pressure swell | 7 % → 7 % | 28.1 px | 0.72 | 0.94 | 81 |
| fast wave | 20 % → 13 % | 23.4 px | 0.71 | 0.64 | 217 |
| slow wave | 21 % → 14 % | 24.5 px | 0.71 | 0.66 | 331 |
| spiral | 30 % → 14 % | 19.9 px | 0.71 | 0.46 | 428 |
| loop | 18 % → 14 % | 23.9 px | 0.71 | 0.77 | 206 |
| tilted | 8 % → 8 % | 21.7 px | 0.70 | 1.00 | 100 |
| over the wet one | 17 % → 15 % | 25.4 px | 0.70 | 0.91 | 84 |
| long, no reload | 33 % → 14 % | 14.9 px | 0.71 | 0.42 | 599 | quarters: 0.38 → 0.21 → 0.10 → 0.03

Numbers say: light vs heavy: width 24.1 → 28.8 px, dark 0.71 → 0.69.

## Oil Round
Oil · 18 px · 23.8 s

![Oil Round](Oil-Round.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 2 % → 2 % | 7.2 px | 0.75 | 1.00 | 187 |
| heavy line | 7 % → 7 % | 19.3 px | 0.73 | 1.00 | 89 |
| pressure swell | 4 % → 4 % | 13.7 px | 0.72 | 1.00 | 57 |
| fast wave | 11 % → 11 % | 12.8 px | 0.65 | 1.00 | 195 |
| slow wave | 8 % → 8 % | 9.0 px | 0.57 | 1.00 | 250 |
| spiral | 10 % → 10 % | 6.6 px | 0.50 | 1.00 | 318 |
| loop | 6 % → 6 % | 7.2 px | 0.45 | 1.00 | 152 |
| tilted | 4 % → 4 % | 10.1 px | 0.52 | 1.00 | 80 |
| over the wet one | 6 % → 6 % | 7.6 px | 0.52 | 1.00 | 74 |
| long, no reload | 15 % → 15 % | 6.9 px | 0.42 | 1.00 | 442 | quarters: 0.09 → 0.08 → 0.07 → 0.06

Numbers say: light vs heavy: width 7.2 → 19.3 px, dark 0.75 → 0.73.

## Palette Knife
Oil · 20 px · 23.0 s

![Palette Knife](Palette-Knife.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 8 % → 8 % | 21.9 px | 0.67 | 1.00 | 136 |
| heavy line | 8 % → 8 % | 22.5 px | 0.73 | 1.00 | 14 |
| pressure swell | 6 % → 6 % | 22.3 px | 0.74 | 1.00 | 12 |
| fast wave | 16 % → 16 % | 18.9 px | 0.50 | 1.00 | 43 |
| slow wave | 17 % → 17 % | 19.9 px | 0.43 | 1.00 | 68 |
| spiral | 17 % → 17 % | 11.3 px | 0.46 | 1.00 | 76 |
| loop | 16 % → 16 % | 21.0 px | 0.59 | 1.00 | 38 |
| tilted | 5 % → 5 % | 15.0 px | 0.72 | 1.00 | 18 |
| over the wet one | 13 % → 13 % | 21.0 px | 0.72 | 1.00 | 17 |
| long, no reload | 16 % → 16 % | 7.2 px | 0.49 | 1.00 | 75 | quarters: 0.29 → 0.05 → 0.00 → 0.00

Numbers say: light vs heavy: width 21.9 → 22.5 px, dark 0.67 → 0.73; pressure barely changes the width.

## Water
Watercolor · 20 px · 50.7 s · over bands of wet oil paint and oil pastel in turn (it works on paint already there: look at what it does to the bands; covered counts the bands too)

![Water](Water.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 25 % → 27 % | 73.8 px | 0.80 | 1.06 | 31 |
| heavy line | 24 % → 25 % | 69.8 px | 0.81 | 1.04 | 76 |
| pressure swell | 24 % → 25 % | 89.6 px | 0.81 | 1.03 | 47 |
| fast wave | 24 % → 26 % | 27.7 px | 0.81 | 1.07 | 151 |
| slow wave | 24 % → 25 % | 27.8 px | 0.81 | 1.06 | 179 |
| spiral | 24 % → 26 % | 15.9 px | 0.81 | 1.07 | 263 |
| loop | 24 % → 25 % | 31.1 px | 0.81 | 1.03 | 123 |
| tilted | 24 % → 24 % | 67.0 px | 0.81 | 1.00 | 93 |
| over the wet one | 24 % → 25 % | 0.0 px | 0.81 | 1.06 | 81 |
| long, no reload | 24 % → 26 % | 10.7 px | 0.81 | 1.08 | 377 | quarters: 0.21 → 0.27 → 0.18 → 0.27

Numbers say: light vs heavy: width 73.8 → 69.8 px, dark 0.80 → 0.81; pressure barely changes the width; the long stroke does not run out of paint.

## Blender
Pastel · 16 px · 28.6 s · over bands of wet oil paint and oil pastel in turn (it works on paint already there: look at what it does to the bands; covered counts the bands too)

![Blender](Blender.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 24 % → 24 % | 70.7 px | 0.81 | 1.00 | 23 |
| heavy line | 25 % → 25 % | 72.1 px | 0.80 | 1.00 | 50 |
| pressure swell | 24 % → 24 % | 91.3 px | 0.81 | 1.00 | 32 |
| fast wave | 26 % → 26 % | 30.0 px | 0.79 | 1.00 | 93 |
| slow wave | 26 % → 26 % | 29.9 px | 0.79 | 1.00 | 111 |
| spiral | 28 % → 28 % | 18.7 px | 0.77 | 1.00 | 151 |
| loop | 25 % → 25 % | 33.0 px | 0.80 | 1.00 | 89 |
| tilted | 25 % → 25 % | 70.1 px | 0.79 | 1.00 | 50 |
| over the wet one | 26 % → 26 % | 1.8 px | 0.79 | 1.00 | 39 |
| long, no reload | 30 % → 30 % | 13.7 px | 0.76 | 1.00 | 245 | quarters: 0.20 → 0.28 → 0.23 → 0.30

Numbers say: light vs heavy: width 70.7 → 72.1 px, dark 0.81 → 0.80; pressure barely changes the width; the long stroke does not run out of paint.

## Eraser
Eraser · 16 px · 28.0 s · over bands of wet oil paint and oil pastel in turn (it works on paint already there: look at what it does to the bands; covered counts the bands too)

![Eraser](Eraser.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 24 % → 24 % | 69.6 px | 0.82 | 1.00 | 49 |
| heavy line | 23 % → 23 % | 67.9 px | 0.82 | 1.00 | 42 |
| pressure swell | 23 % → 23 % | 87.3 px | 0.82 | 1.00 | 36 |
| fast wave | 22 % → 22 % | 25.7 px | 0.82 | 1.00 | 88 |
| slow wave | 22 % → 22 % | 25.7 px | 0.82 | 1.00 | 121 |
| spiral | 22 % → 22 % | 14.4 px | 0.82 | 1.00 | 169 |
| loop | 22 % → 22 % | 28.6 px | 0.82 | 1.00 | 91 |
| tilted | 23 % → 23 % | 65.1 px | 0.82 | 1.00 | 60 |
| over the wet one | 23 % → 23 % | 0.0 px | 0.82 | 1.00 | 37 |
| long, no reload | 20 % → 20 % | 8.9 px | 0.82 | 1.00 | 279 | quarters: 0.15 → 0.20 → 0.15 → 0.20

Numbers say: light vs heavy: width 69.6 → 67.9 px, dark 0.82 → 0.82; pressure barely changes the width; the long stroke does not run out of paint.

## Fan
Gouache · 30 px · 41.6 s

![Fan](Fan.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 9 % → 3 % | 25.6 px | 0.63 | 0.37 | 39 |
| heavy line | 11 % → 4 % | 30.9 px | 0.63 | 0.39 | 73 |
| pressure swell | 8 % → 5 % | 31.7 px | 0.63 | 0.55 | 42 |
| fast wave | 17 % → 5 % | 20.2 px | 0.63 | 0.26 | 168 |
| slow wave | 18 % → 5 % | 21.0 px | 0.63 | 0.25 | 288 |
| spiral | 24 % → 5 % | 15.5 px | 0.63 | 0.19 | 287 |
| loop | 17 % → 5 % | 22.7 px | 0.63 | 0.28 | 144 |
| tilted | 5 % → 6 % | 15.0 px | 0.63 | 1.05 | 57 |
| over the wet one | 16 % → 8 % | 29.7 px | 0.63 | 0.49 | 65 |
| long, no reload | 22 % → 5 % | 9.9 px | 0.63 | 0.22 | 356 | quarters: 0.29 → 0.07 → 0.01 → 0.00

Numbers say: light vs heavy: width 25.6 → 30.9 px, dark 0.63 → 0.63.

## Sponge
Gouache · 30 px · 41.6 s

![Sponge](Sponge.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 4 % → 0 % | 11.3 px | 0.62 | 0.12 | 51 |
| heavy line | 12 % → 2 % | 35.4 px | 0.62 | 0.14 | 91 |
| pressure swell | 7 % → 2 % | 27.9 px | 0.62 | 0.28 | 52 |
| fast wave | 20 % → 4 % | 23.2 px | 0.62 | 0.19 | 203 |
| slow wave | 21 % → 4 % | 23.8 px | 0.62 | 0.18 | 386 |
| spiral | 28 % → 4 % | 18.3 px | 0.62 | 0.14 | 272 |
| loop | 18 % → 5 % | 23.0 px | 0.62 | 0.29 | 200 |
| tilted | 7 % → 7 % | 18.2 px | 0.62 | 1.04 | 124 |
| over the wet one | 16 % → 6 % | 27.8 px | 0.62 | 0.37 | 73 |
| long, no reload | 29 % → 5 % | 12.9 px | 0.62 | 0.17 | 450 | quarters: 0.29 → 0.13 → 0.07 → 0.04

Numbers say: light vs heavy: width 11.3 → 35.4 px, dark 0.62 → 0.62.

## Ink — sumi brush
Watercolour 1.00 · 22 px · 42.1 s

![Ink — sumi brush](Ink-sumi-brush.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 8 % → 9 % | 23.9 px | 0.87 | 1.12 | 91 |
| heavy line | 13 % → 13 % | 38.1 px | 0.86 | 1.00 | 93 |
| pressure swell | 9 % → 10 % | 34.5 px | 0.87 | 1.05 | 88 |
| fast wave | 28 % → 28 % | 32.5 px | 0.81 | 1.00 | 235 |
| slow wave | 26 % → 26 % | 29.6 px | 0.82 | 1.02 | 311 |
| spiral | 38 % → 37 % | 25.3 px | 0.74 | 0.96 | 408 |
| loop | 22 % → 22 % | 28.5 px | 0.85 | 1.02 | 211 |
| tilted | 9 % → 9 % | 25.3 px | 0.86 | 1.01 | 104 |
| over the wet one | 20 % → 21 % | 30.7 px | 0.86 | 1.03 | 90 |
| long, no reload | 45 % → 40 % | 20.1 px | 0.70 | 0.89 | 584 | quarters: 0.55 → 0.40 → 0.23 → 0.14

Numbers say: light vs heavy: width 23.9 → 38.1 px, dark 0.87 → 0.86.

## Ink — wash
Watercolour 1.00 · 40 px · 49.0 s

![Ink — wash](Ink-wash.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 13 % → 13 % | 37.3 px | 0.42 | 1.02 | 98 |
| heavy line | 19 % → 19 % | 55.2 px | 0.35 | 1.01 | 129 |
| pressure swell | 13 % → 13 % | 48.2 px | 0.41 | 1.02 | 92 |
| fast wave | 41 % → 42 % | 47.8 px | 0.32 | 1.02 | 322 |
| slow wave | 39 % → 40 % | 45.3 px | 0.42 | 1.02 | 546 |
| spiral | 60 % → 62 % | 39.7 px | 0.33 | 1.02 | 513 |
| loop | 34 % → 34 % | 43.8 px | 0.39 | 1.01 | 261 |
| tilted | 15 % → 15 % | 40.7 px | 0.43 | 1.01 | 163 |
| over the wet one | 30 % → 31 % | 43.4 px | 0.43 | 1.02 | 112 |
| long, no reload | 71 % → 75 % | 32.0 px | 0.31 | 1.05 | 871 | quarters: 0.40 → 0.29 → 0.19 → 0.12

Numbers say: light vs heavy: width 37.3 → 55.2 px, dark 0.42 → 0.35.

## Ink — dry brush
Ink 1.00 · 30 px · 34.9 s

![Ink — dry brush](Ink-dry-brush.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 6 % → 5 % | 16.8 px | 0.82 | 0.87 | 122 |
| heavy line | 6 % → 5 % | 18.6 px | 0.82 | 0.78 | 178 |
| pressure swell | 5 % → 4 % | 18.0 px | 0.83 | 0.88 | 118 |
| fast wave | 11 % → 7 % | 13.2 px | 0.80 | 0.60 | 348 |
| slow wave | 12 % → 7 % | 13.5 px | 0.80 | 0.56 | 546 |
| spiral | 18 % → 7 % | 11.6 px | 0.78 | 0.41 | 543 |
| loop | 11 % → 7 % | 14.2 px | 0.79 | 0.66 | 279 |
| tilted | 6 % → 6 % | 16.3 px | 0.80 | 1.06 | 180 |
| over the wet one | 12 % → 11 % | 17.4 px | 0.80 | 0.93 | 141 |
| long, no reload | 19 % → 8 % | 8.4 px | 0.77 | 0.42 | 785 | quarters: 0.25 → 0.08 → 0.02 → 0.01

Numbers say: light vs heavy: width 16.8 → 18.6 px, dark 0.82 → 0.82; pressure barely changes the width.

## Ink — nib
Watercolour 1.00 · 5 px · 34.3 s

![Ink — nib](Ink-nib.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 2 % → 5 % | 5.5 px | 0.89 | 2.46 | 39 |
| heavy line | 2 % → 5 % | 6.4 px | 0.89 | 2.34 | 34 |
| pressure swell | 2 % → 4 % | 6.2 px | 0.89 | 2.53 | 31 |
| fast wave | 5 % → 8 % | 5.9 px | 0.89 | 1.63 | 102 |
| slow wave | 5 % → 8 % | 5.7 px | 0.89 | 1.70 | 100 |
| spiral | 8 % → 11 % | 5.0 px | 0.87 | 1.41 | 157 |
| loop | 4 % → 8 % | 5.7 px | 0.89 | 1.74 | 89 |
| tilted | 4 % → 4 % | 10.3 px | 0.89 | 1.02 | 44 |
| over the wet one | 6 % → 9 % | 6.1 px | 0.89 | 1.61 | 44 |
| long, no reload | 9 % → 12 % | 4.2 px | 0.85 | 1.30 | 244 | quarters: 0.24 → 0.11 → 0.07 → 0.05

Numbers say: light vs heavy: width 5.5 → 6.4 px, dark 0.89 → 0.89; wet paint spreads well beyond the stroke.

## 0.45 · Dry brush
Gouache 0.91 · Ink 0.07 · 34 px · 42.1 s

![0.45 · Dry brush](0-45-Dry-brush.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 8 % → 4 % | 24.2 px | 0.68 | 0.51 | 166 |
| heavy line | 9 % → 5 % | 25.9 px | 0.68 | 0.52 | 167 |
| pressure swell | 7 % → 5 % | 26.7 px | 0.68 | 0.66 | 110 |
| fast wave | 16 % → 5 % | 18.8 px | 0.68 | 0.31 | 500 |
| slow wave | 19 % → 7 % | 22.1 px | 0.68 | 0.37 | 719 |
| spiral | 26 % → 6 % | 17.1 px | 0.68 | 0.23 | 709 |
| loop | 16 % → 7 % | 21.2 px | 0.68 | 0.41 | 403 |
| tilted | 8 % → 8 % | 22.8 px | 0.68 | 1.02 | 227 |
| over the wet one | 17 % → 12 % | 24.3 px | 0.68 | 0.69 | 177 |
| long, no reload | 28 % → 7 % | 12.7 px | 0.68 | 0.25 | 1082 | quarters: 0.33 → 0.22 → 0.14 → 0.12

Numbers say: light vs heavy: width 24.2 → 25.9 px, dark 0.68 → 0.68; pressure barely changes the width.

## Dry pastel
Pastel 1.00 · 26 px · 15.1 s

![Dry pastel](Dry-pastel.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 3 % → 3 % | 8.1 px | 0.38 | 1.00 | 43 |
| heavy line | 4 % → 4 % | 12.8 px | 0.39 | 1.00 | 56 |
| pressure swell | 3 % → 3 % | 11.7 px | 0.38 | 1.00 | 41 |
| fast wave | 10 % → 10 % | 11.8 px | 0.39 | 1.00 | 135 |
| slow wave | 10 % → 10 % | 11.3 px | 0.39 | 1.00 | 244 |
| spiral | 14 % → 14 % | 9.5 px | 0.38 | 1.00 | 236 |
| loop | 7 % → 7 % | 9.3 px | 0.39 | 1.00 | 119 |
| tilted | 3 % → 3 % | 8.3 px | 0.38 | 1.00 | 63 |
| over the wet one | 7 % → 7 % | 10.7 px | 0.38 | 1.00 | 48 |
| long, no reload | 18 % → 18 % | 8.2 px | 0.39 | 1.00 | 341 | quarters: 0.08 → 0.08 → 0.08 → 0.07

Numbers say: light vs heavy: width 8.1 → 12.8 px, dark 0.38 → 0.39; the long stroke does not run out of paint.

## 0.45 · Charcoal
Charcoal 1.00 · 18 px · 14.3 s

![0.45 · Charcoal](0-45-Charcoal.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 2 % → 2 % | 6.5 px | 0.80 | 1.00 | 24 |
| heavy line | 3 % → 3 % | 9.2 px | 0.80 | 1.00 | 25 |
| pressure swell | 2 % → 2 % | 8.8 px | 0.80 | 1.00 | 21 |
| fast wave | 7 % → 7 % | 8.5 px | 0.80 | 1.00 | 68 |
| slow wave | 7 % → 7 % | 8.0 px | 0.80 | 1.00 | 78 |
| spiral | 12 % → 12 % | 7.9 px | 0.80 | 1.00 | 105 |
| loop | 6 % → 6 % | 8.1 px | 0.80 | 1.00 | 63 |
| tilted | 3 % → 3 % | 7.5 px | 0.80 | 1.00 | 47 |
| over the wet one | 6 % → 6 % | 7.8 px | 0.80 | 1.00 | 21 |
| long, no reload | 17 % → 17 % | 7.7 px | 0.80 | 1.00 | 157 | quarters: 0.15 → 0.16 → 0.15 → 0.16

Numbers say: light vs heavy: width 6.5 → 9.2 px, dark 0.80 → 0.80; the long stroke does not run out of paint.

## Watercolour — wash
Watercolour 1.00 · 50 px · 55.7 s

![Watercolour — wash](Watercolour-wash.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 16 % → 16 % | 45.5 px | 0.22 | 1.01 | 168 |
| heavy line | 22 % → 22 % | 64.9 px | 0.19 | 1.00 | 385 |
| pressure swell | 15 % → 15 % | 56.1 px | 0.22 | 1.01 | 123 |
| fast wave | 48 % → 49 % | 55.5 px | 0.19 | 1.01 | 458 |
| slow wave | 46 % → 46 % | 53.3 px | 0.24 | 1.00 | 816 |
| spiral | 66 % → 66 % | 43.7 px | 0.21 | 1.00 | 777 |
| loop | 40 % → 40 % | 51.4 px | 0.22 | 1.00 | 409 |
| tilted | 18 % → 18 % | 49.7 px | 0.23 | 1.00 | 299 |
| over the wet one | 36 % → 36 % | 49.6 px | 0.23 | 1.01 | 189 |
| long, no reload | 84 % → 84 % | 37.7 px | 0.20 | 1.00 | 1127 | quarters: 0.24 → 0.20 → 0.16 → 0.12

Numbers say: light vs heavy: width 45.5 → 64.9 px, dark 0.22 → 0.19.

## Watercolour — wet-in-wet
Watercolour 1.00 · 44 px · 57.1 s

![Watercolour — wet-in-wet](Watercolour-wet-in-wet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 13 % → 21 % | 38.4 px | 0.32 | 1.58 | 139 |
| heavy line | 19 % → 22 % | 54.6 px | 0.34 | 1.17 | 250 |
| pressure swell | 12 % → 17 % | 46.5 px | 0.35 | 1.34 | 116 |
| fast wave | 41 % → 49 % | 47.7 px | 0.33 | 1.19 | 418 |
| slow wave | 40 % → 48 % | 46.2 px | 0.40 | 1.21 | 602 |
| spiral | 63 % → 69 % | 41.5 px | 0.37 | 1.10 | 608 |
| loop | 34 % → 41 % | 44.4 px | 0.37 | 1.20 | 343 |
| tilted | 15 % → 16 % | 41.5 px | 0.36 | 1.06 | 217 |
| over the wet one | 31 % → 40 % | 44.1 px | 0.36 | 1.31 | 159 |
| long, no reload | 78 % → 87 % | 34.8 px | 0.36 | 1.12 | 964 | quarters: 0.40 → 0.37 → 0.32 → 0.26

Numbers say: light vs heavy: width 38.4 → 54.6 px, dark 0.32 → 0.34; wet paint spreads well beyond the stroke.

## Watercolour — glaze
Watercolour 1.00 · 38 px · 49.5 s

![Watercolour — glaze](Watercolour-glaze.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 13 % → 13 % | 36.6 px | 0.07 | 1.02 | 123 |
| heavy line | 19 % → 19 % | 55.4 px | 0.07 | 1.00 | 157 |
| pressure swell | 13 % → 13 % | 47.0 px | 0.07 | 1.02 | 102 |
| fast wave | 39 % → 40 % | 45.6 px | 0.07 | 1.01 | 303 |
| slow wave | 37 % → 37 % | 42.8 px | 0.07 | 1.01 | 571 |
| spiral | 59 % → 60 % | 38.8 px | 0.06 | 1.01 | 587 |
| loop | 33 % → 33 % | 42.6 px | 0.07 | 1.00 | 274 |
| tilted | 14 % → 14 % | 40.1 px | 0.07 | 1.00 | 187 |
| over the wet one | 30 % → 30 % | 42.3 px | 0.07 | 1.01 | 142 |
| long, no reload | 69 % → 70 % | 30.9 px | 0.06 | 1.01 | 1021 | quarters: 0.06 → 0.05 → 0.03 → 0.02

Numbers say: light vs heavy: width 36.6 → 55.4 px, dark 0.07 → 0.07.

## Watercolour — granulating
Watercolour 1.00 · 44 px · 53.1 s

![Watercolour — granulating](Watercolour-granulating.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 14 % → 14 % | 41.4 px | 0.35 | 1.01 | 143 |
| heavy line | 21 % → 21 % | 60.4 px | 0.31 | 1.00 | 185 |
| pressure swell | 14 % → 14 % | 52.2 px | 0.34 | 1.01 | 110 |
| fast wave | 45 % → 45 % | 51.7 px | 0.29 | 1.01 | 435 |
| slow wave | 42 % → 42 % | 48.2 px | 0.35 | 1.01 | 677 |
| spiral | 62 % → 63 % | 41.0 px | 0.30 | 1.01 | 671 |
| loop | 37 % → 37 % | 47.6 px | 0.33 | 1.00 | 340 |
| tilted | 16 % → 16 % | 45.5 px | 0.36 | 1.00 | 330 |
| over the wet one | 33 % → 33 % | 46.2 px | 0.36 | 1.01 | 167 |
| long, no reload | 75 % → 76 % | 33.6 px | 0.29 | 1.01 | 1000 | quarters: 0.34 → 0.26 → 0.20 → 0.14

Numbers say: light vs heavy: width 41.4 → 60.4 px, dark 0.35 → 0.31.

## Watercolour — dry brush
Watercolour 1.00 · 36 px · 43.4 s

![Watercolour — dry brush](Watercolour-dry-brush.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 10 % → 10 % | 27.9 px | 0.17 | 1.01 | 146 |
| heavy line | 14 % → 13 % | 39.9 px | 0.16 | 0.93 | 261 |
| pressure swell | 11 % → 11 % | 40.3 px | 0.16 | 0.98 | 145 |
| fast wave | 27 % → 20 % | 30.7 px | 0.13 | 0.74 | 438 |
| slow wave | 24 % → 17 % | 28.0 px | 0.14 | 0.71 | 687 |
| spiral | 34 % → 20 % | 22.4 px | 0.13 | 0.58 | 664 |
| loop | 21 % → 18 % | 27.1 px | 0.14 | 0.86 | 486 |
| tilted | 10 % → 10 % | 28.5 px | 0.17 | 1.00 | 295 |
| over the wet one | 21 % → 20 % | 31.3 px | 0.17 | 0.95 | 183 |
| long, no reload | 36 % → 19 % | 16.0 px | 0.14 | 0.54 | 1007 | quarters: 0.09 → 0.03 → 0.01 → 0.00

Numbers say: light vs heavy: width 27.9 → 39.9 px, dark 0.17 → 0.16.

## Gouache
Gouache 1.00 · 30 px · 46.7 s

![Gouache](Gouache.png)

A light paint: laid on a grey sheet (on white it cannot be seen); **dark** = how far it is from the grey either way.

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 8 % → 4 % | 23.8 px | 0.28 | 0.49 | 124 |
| heavy line | 13 % → 4 % | 36.9 px | 0.28 | 0.33 | 157 |
| pressure swell | 10 % → 4 % | 36.7 px | 0.28 | 0.42 | 105 |
| fast wave | 24 % → 5 % | 27.4 px | 0.28 | 0.21 | 330 |
| slow wave | 24 % → 6 % | 27.5 px | 0.28 | 0.25 | 546 |
| spiral | 32 % → 6 % | 21.3 px | 0.28 | 0.18 | 716 |
| loop | 20 % → 6 % | 25.8 px | 0.28 | 0.30 | 317 |
| tilted | 9 % → 9 % | 25.0 px | 0.27 | 1.01 | 176 |
| over the wet one | 20 % → 10 % | 29.5 px | 0.27 | 0.52 | 151 |
| long, no reload | 34 % → 7 % | 15.1 px | 0.27 | 0.22 | 870 | quarters: 0.01 → 0.01 → 0.02 → 0.02

Numbers say: light vs heavy: width 23.8 → 36.9 px, dark 0.28 → 0.28; the long stroke does not run out of paint.

## Oil — alla prima
Oil 0.89 · Oil glaze 0.11 · 30 px · 22.6 s

![Oil — alla prima](Oil-alla-prima.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 9 % → 9 % | 26.4 px | 0.50 | 1.00 | 139 |
| heavy line | 9 % → 9 % | 27.4 px | 0.49 | 1.00 | 146 |
| pressure swell | 8 % → 8 % | 28.7 px | 0.50 | 1.00 | 101 |
| fast wave | 22 % → 22 % | 24.9 px | 0.47 | 1.00 | 354 |
| slow wave | 23 % → 23 % | 26.8 px | 0.50 | 1.00 | 614 |
| spiral | 36 % → 36 % | 23.8 px | 0.49 | 1.00 | 624 |
| loop | 19 % → 19 % | 25.2 px | 0.50 | 1.00 | 427 |
| tilted | 11 % → 11 % | 29.8 px | 0.50 | 1.00 | 275 |
| over the wet one | 20 % → 20 % | 25.0 px | 0.50 | 1.00 | 215 |
| long, no reload | 42 % → 42 % | 19.0 px | 0.47 | 1.00 | 972 | quarters: 0.29 → 0.23 → 0.21 → 0.17

Numbers say: light vs heavy: width 26.4 → 27.4 px, dark 0.50 → 0.49; pressure barely changes the width.

## Oil — impasto
Oil heavy 1.00 · 34 px · 30.7 s

![Oil — impasto](Oil-impasto.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 11 % → 11 % | 30.5 px | 0.23 | 1.00 | 188 |
| heavy line | 12 % → 12 % | 34.5 px | 0.23 | 1.00 | 165 |
| pressure swell | 9 % → 9 % | 34.4 px | 0.24 | 1.00 | 118 |
| fast wave | 27 % → 27 % | 30.8 px | 0.22 | 1.00 | 425 |
| slow wave | 30 % → 30 % | 34.5 px | 0.22 | 1.00 | 773 |
| spiral | 44 % → 44 % | 29.1 px | 0.21 | 1.00 | 962 |
| loop | 24 % → 24 % | 31.5 px | 0.22 | 1.00 | 512 |
| tilted | 12 % → 12 % | 32.6 px | 0.24 | 1.00 | 239 |
| over the wet one | 23 % → 23 % | 30.4 px | 0.24 | 1.00 | 233 |
| long, no reload | 49 % → 49 % | 22.0 px | 0.21 | 1.00 | 1128 | quarters: 0.16 → 0.12 → 0.09 → 0.07

Numbers say: light vs heavy: width 30.5 → 34.5 px, dark 0.23 → 0.23.

## Oil — glaze
Oil glaze 1.00 · 40 px · 25.1 s

![Oil — glaze](Oil-glaze.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 9 % → 9 % | 27.0 px | 0.50 | 1.00 | 152 |
| heavy line | 13 % → 13 % | 38.3 px | 0.49 | 1.00 | 182 |
| pressure swell | 10 % → 10 % | 36.6 px | 0.50 | 1.00 | 142 |
| fast wave | 29 % → 29 % | 33.5 px | 0.49 | 1.00 | 489 |
| slow wave | 30 % → 30 % | 34.6 px | 0.50 | 1.00 | 820 |
| spiral | 46 % → 46 % | 30.1 px | 0.49 | 1.00 | 787 |
| loop | 24 % → 24 % | 31.4 px | 0.50 | 1.00 | 377 |
| tilted | 11 % → 11 % | 30.4 px | 0.50 | 1.00 | 212 |
| over the wet one | 23 % → 23 % | 32.5 px | 0.50 | 1.00 | 201 |
| long, no reload | 52 % → 52 % | 23.5 px | 0.49 | 1.00 | 1192 | quarters: 0.34 → 0.30 → 0.27 → 0.22

Numbers say: light vs heavy: width 27.0 → 38.3 px, dark 0.50 → 0.49.

## Oil — scumble
Oil 1.00 · 36 px · 23.6 s

![Oil — scumble](Oil-scumble.png)

A light paint: laid on a grey sheet (on white it cannot be seen); **dark** = how far it is from the grey either way.

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 9 % → 9 % | 25.5 px | 0.25 | 1.00 | 251 |
| heavy line | 9 % → 9 % | 25.5 px | 0.24 | 1.00 | 251 |
| pressure swell | 8 % → 8 % | 29.6 px | 0.23 | 1.00 | 157 |
| fast wave | 17 % → 17 % | 19.9 px | 0.16 | 1.00 | 518 |
| slow wave | 21 % → 21 % | 24.1 px | 0.18 | 1.00 | 938 |
| spiral | 28 % → 28 % | 18.8 px | 0.14 | 1.00 | 880 |
| loop | 17 % → 17 % | 22.0 px | 0.20 | 1.00 | 468 |
| tilted | 10 % → 10 % | 27.8 px | 0.24 | 1.00 | 268 |
| over the wet one | 19 % → 19 % | 25.1 px | 0.24 | 1.00 | 202 |
| long, no reload | 30 % → 30 % | 13.3 px | 0.13 | 1.00 | 1276 | quarters: 0.00 → 0.00 → 0.00 → 0.00

Numbers say: light vs heavy: width 25.5 → 25.5 px, dark 0.25 → 0.24; pressure barely changes the width.

## Acrylic — heavy body
Impasto 0.98 · 30 px · 23.2 s

![Acrylic — heavy body](Acrylic-heavy-body.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 9 % → 7 % | 26.7 px | 0.51 | 0.80 | 151 |
| heavy line | 10 % → 8 % | 29.1 px | 0.51 | 0.81 | 170 |
| pressure swell | 8 % → 7 % | 29.1 px | 0.53 | 0.88 | 113 |
| fast wave | 20 % → 11 % | 22.9 px | 0.52 | 0.57 | 483 |
| slow wave | 21 % → 14 % | 24.7 px | 0.52 | 0.65 | 646 |
| spiral | 30 % → 13 % | 19.6 px | 0.52 | 0.45 | 799 |
| loop | 18 % → 12 % | 23.5 px | 0.52 | 0.66 | 372 |
| tilted | 8 % → 8 % | 22.4 px | 0.52 | 0.99 | 189 |
| over the wet one | 17 % → 15 % | 25.8 px | 0.52 | 0.86 | 184 |
| long, no reload | 30 % → 16 % | 13.4 px | 0.52 | 0.52 | 1000 | quarters: 0.25 → 0.14 → 0.09 → 0.07

Numbers say: light vs heavy: width 26.7 → 29.1 px, dark 0.51 → 0.51; pressure barely changes the width.

## Acrylic — fluid
Watercolour 1.00 · 36 px · 46.5 s

![Acrylic — fluid](Acrylic-fluid.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 12 % → 12 % | 34.8 px | 0.24 | 1.01 | 139 |
| heavy line | 18 % → 18 % | 52.6 px | 0.21 | 0.99 | 171 |
| pressure swell | 12 % → 12 % | 45.4 px | 0.23 | 1.00 | 104 |
| fast wave | 38 % → 38 % | 44.1 px | 0.19 | 0.98 | 290 |
| slow wave | 35 % → 35 % | 40.5 px | 0.22 | 1.00 | 569 |
| spiral | 55 % → 53 % | 36.0 px | 0.19 | 0.98 | 569 |
| loop | 31 % → 31 % | 40.2 px | 0.21 | 1.00 | 317 |
| tilted | 12 % → 12 % | 34.2 px | 0.24 | 1.00 | 164 |
| over the wet one | 27 % → 28 % | 42.3 px | 0.24 | 1.02 | 138 |
| long, no reload | 61 % → 58 % | 27.6 px | 0.19 | 0.95 | 829 | quarters: 0.20 → 0.14 → 0.09 → 0.06

Numbers say: light vs heavy: width 34.8 → 52.6 px, dark 0.24 → 0.21.

## Acrylic — palette knife
Impasto 1.00 · 42 px · 29.1 s

![Acrylic — palette knife](Acrylic-palette-knife.png)

A light paint: laid on a grey sheet (on white it cannot be seen); **dark** = how far it is from the grey either way.

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 15 % → 15 % | 44.0 px | 0.39 | 0.98 | 58 |
| heavy line | 15 % → 15 % | 44.2 px | 0.40 | 0.98 | 55 |
| pressure swell | 12 % → 11 % | 43.5 px | 0.42 | 0.99 | 19 |
| fast wave | 36 % → 20 % | 41.9 px | 0.37 | 0.55 | 108 |
| slow wave | 37 % → 21 % | 42.7 px | 0.37 | 0.57 | 213 |
| spiral | 47 % → 18 % | 30.7 px | 0.37 | 0.39 | 198 |
| loop | 32 % → 24 % | 41.2 px | 0.36 | 0.77 | 154 |
| tilted | 12 % → 12 % | 33.6 px | 0.39 | 1.00 | 48 |
| over the wet one | 26 % → 25 % | 39.8 px | 0.39 | 0.97 | 47 |
| long, no reload | 53 % → 20 % | 23.6 px | 0.35 | 0.38 | 271 | quarters: 0.00 → 0.00 → 0.00 → 0.01

Numbers say: light vs heavy: width 44.0 → 44.2 px, dark 0.39 → 0.40; pressure barely changes the width; the long stroke does not run out of paint.

## Finger on oil
Oil 1.00 · 30 px · 19.7 s

![Finger on oil](Finger-on-oil.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 6 % → 6 % | 16.4 px | 0.36 | 1.00 | 104 |
| heavy line | 9 % → 9 % | 24.7 px | 0.32 | 1.00 | 98 |
| pressure swell | 6 % → 6 % | 22.3 px | 0.38 | 1.00 | 78 |
| fast wave | 11 % → 11 % | 12.5 px | 0.27 | 1.00 | 190 |
| slow wave | 15 % → 15 % | 17.7 px | 0.31 | 1.00 | 403 |
| spiral | 20 % → 20 % | 13.1 px | 0.27 | 1.00 | 348 |
| loop | 13 % → 13 % | 16.9 px | 0.31 | 1.00 | 168 |
| tilted | 9 % → 9 % | 23.8 px | 0.34 | 1.00 | 121 |
| over the wet one | 16 % → 16 % | 20.4 px | 0.34 | 1.00 | 76 |
| long, no reload | 23 % → 23 % | 10.4 px | 0.26 | 1.00 | 460 | quarters: 0.15 → 0.06 → 0.03 → 0.02

Numbers say: light vs heavy: width 16.4 → 24.7 px, dark 0.36 → 0.32.

## Palette knife — oil
Oil heavy 0.93 · Impasto 0.07 · 44 px · 27.9 s

![Palette knife — oil](Palette-knife-oil.png)

A light paint: laid on a grey sheet (on white it cannot be seen); **dark** = how far it is from the grey either way.

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 16 % → 14 % | 45.7 px | 0.37 | 0.90 | 59 |
| heavy line | 16 % → 16 % | 46.3 px | 0.38 | 0.98 | 64 |
| pressure swell | 12 % → 12 % | 45.2 px | 0.38 | 0.99 | 24 |
| fast wave | 39 % → 34 % | 44.9 px | 0.35 | 0.89 | 112 |
| slow wave | 39 % → 36 % | 45.4 px | 0.35 | 0.91 | 210 |
| spiral | 62 % → 37 % | 40.7 px | 0.35 | 0.60 | 274 |
| loop | 34 % → 31 % | 43.7 px | 0.36 | 0.92 | 119 |
| tilted | 13 % → 13 % | 36.6 px | 0.37 | 1.00 | 48 |
| over the wet one | 28 % → 27 % | 40.8 px | 0.37 | 0.97 | 58 |
| long, no reload | 74 % → 39 % | 33.0 px | 0.34 | 0.53 | 324 | quarters: 0.00 → 0.00 → 0.01 → 0.01

Numbers say: light vs heavy: width 45.7 → 46.3 px, dark 0.37 → 0.38; pressure barely changes the width; the long stroke does not run out of paint.

## 0.45 · Sponge
Watercolour 0.93 · Ink 0.07 · 46 px · 48.3 s

![0.45 · Sponge](0-45-Sponge.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 27 % → 25 % | 78.2 px | 0.12 | 0.95 | 100 |
| heavy line | 32 % → 29 % | 91.9 px | 0.12 | 0.92 | 149 |
| pressure swell | 24 % → 21 % | 90.6 px | 0.12 | 0.88 | 79 |
| fast wave | 59 % → 55 % | 68.5 px | 0.12 | 0.92 | 324 |
| slow wave | 61 % → 58 % | 70.4 px | 0.17 | 0.95 | 527 |
| spiral | 77 % → 75 % | 50.7 px | 0.16 | 0.97 | 558 |
| loop | 53 % → 51 % | 69.1 px | 0.14 | 0.95 | 296 |
| tilted | 18 % → 18 % | 50.7 px | 0.17 | 1.00 | 200 |
| over the wet one | 45 % → 42 % | 73.6 px | 0.17 | 0.94 | 139 |
| long, no reload | 94 % → 89 % | 42.0 px | 0.17 | 0.95 | 760 | quarters: 0.17 → 0.18 → 0.16 → 0.14

Numbers say: light vs heavy: width 78.2 → 91.9 px, dark 0.12 → 0.12.

## 0.45 · Eraser
Watercolour 1.00 · 30 px · 30.4 s · over bands of wet oil paint and oil pastel in turn (it works on paint already there: look at what it does to the bands; covered counts the bands too)

![0.45 · Eraser](0-45-Eraser.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 24 % → 24 % | 69.2 px | 0.82 | 1.00 | 79 |
| heavy line | 23 % → 23 % | 67.4 px | 0.81 | 1.00 | 80 |
| pressure swell | 23 % → 23 % | 86.8 px | 0.82 | 1.00 | 64 |
| fast wave | 21 % → 21 % | 24.7 px | 0.81 | 1.00 | 194 |
| slow wave | 20 % → 20 % | 23.5 px | 0.82 | 1.00 | 362 |
| spiral | 20 % → 20 % | 13.5 px | 0.79 | 1.00 | 389 |
| loop | 21 % → 21 % | 27.8 px | 0.80 | 1.00 | 163 |
| tilted | 23 % → 23 % | 64.8 px | 0.81 | 1.00 | 91 |
| over the wet one | 22 % → 22 % | 0.0 px | 0.81 | 1.00 | 80 |
| long, no reload | 17 % → 17 % | 7.5 px | 0.79 | 1.00 | 471 | quarters: 0.13 → 0.16 → 0.13 → 0.17

Numbers say: light vs heavy: width 69.2 → 67.4 px, dark 0.82 → 0.81; pressure barely changes the width; the long stroke does not run out of paint.

## Lift wet paint
Watercolour 1.00 · 30 px · 30.0 s · over bands of wet oil paint and oil pastel in turn (it works on paint already there: look at what it does to the bands; covered counts the bands too)

![Lift wet paint](Lift-wet-paint.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 24 % → 24 % | 70.1 px | 0.82 | 1.00 | 56 |
| heavy line | 24 % → 24 % | 69.8 px | 0.82 | 1.00 | 83 |
| pressure swell | 24 % → 24 % | 89.6 px | 0.82 | 1.00 | 51 |
| fast wave | 24 % → 24 % | 27.7 px | 0.82 | 1.00 | 161 |
| slow wave | 24 % → 24 % | 27.7 px | 0.82 | 1.00 | 315 |
| spiral | 24 % → 24 % | 15.9 px | 0.82 | 1.00 | 269 |
| loop | 24 % → 24 % | 31.1 px | 0.82 | 1.00 | 134 |
| tilted | 24 % → 24 % | 66.8 px | 0.82 | 1.00 | 77 |
| over the wet one | 24 % → 24 % | 0.0 px | 0.82 | 1.00 | 62 |
| long, no reload | 24 % → 24 % | 10.7 px | 0.82 | 1.00 | 403 | quarters: 0.18 → 0.24 → 0.17 → 0.24

Numbers say: light vs heavy: width 70.1 → 69.8 px, dark 0.82 → 0.82; pressure barely changes the width; the long stroke does not run out of paint.

## Sgraffito
Watercolour 1.00 · 10 px · 30.6 s · over bands of wet oil paint and oil pastel in turn (it works on paint already there: look at what it does to the bands; covered counts the bands too)

![Sgraffito](Sgraffito.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 24 % → 24 % | 69.9 px | 0.81 | 1.00 | 23 |
| heavy line | 24 % → 24 % | 69.8 px | 0.82 | 1.00 | 16 |
| pressure swell | 24 % → 24 % | 89.6 px | 0.82 | 1.00 | 15 |
| fast wave | 24 % → 24 % | 27.7 px | 0.82 | 1.00 | 50 |
| slow wave | 24 % → 24 % | 27.7 px | 0.82 | 1.00 | 44 |
| spiral | 24 % → 24 % | 15.9 px | 0.82 | 1.00 | 75 |
| loop | 24 % → 24 % | 31.1 px | 0.82 | 1.00 | 31 |
| tilted | 24 % → 24 % | 66.9 px | 0.82 | 1.00 | 28 |
| over the wet one | 24 % → 24 % | 0.0 px | 0.82 | 1.00 | 25 |
| long, no reload | 24 % → 24 % | 10.6 px | 0.82 | 1.00 | 92 | quarters: 0.17 → 0.24 → 0.17 → 0.24

Numbers say: light vs heavy: width 69.9 → 69.8 px, dark 0.81 → 0.82; pressure barely changes the width; the long stroke does not run out of paint.

## Brush Artist · Refs · #01 Henry Ward peach cloud
Gouache 1.00 · 44 px · 47.2 s

![Brush Artist · Refs · #01 Henry Ward peach cloud](Brush-Artist-Refs-01-Henry-Ward-peach-cloud.png)

A light paint: laid on a grey sheet (on white it cannot be seen); **dark** = how far it is from the grey either way.

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 14 % → 6 % | 39.4 px | 0.34 | 0.45 | 200 |
| heavy line | 14 % → 8 % | 41.4 px | 0.34 | 0.58 | 250 |
| pressure swell | 10 % → 8 % | 38.0 px | 0.34 | 0.77 | 167 |
| fast wave | 28 % → 4 % | 32.5 px | 0.34 | 0.16 | 572 |
| slow wave | 30 % → 10 % | 34.7 px | 0.34 | 0.33 | 1121 |
| spiral | 39 % → 8 % | 25.9 px | 0.34 | 0.21 | 951 |
| loop | 26 % → 8 % | 33.7 px | 0.34 | 0.32 | 492 |
| tilted | 12 % → 12 % | 34.2 px | 0.34 | 0.97 | 297 |
| over the wet one | 25 % → 15 % | 34.9 px | 0.34 | 0.60 | 239 |
| long, no reload | 27 % → 12 % | 12.1 px | 0.33 | 0.44 | 1162 | quarters: 0.01 → 0.03 → 0.03 → 0.03

Numbers say: light vs heavy: width 39.4 → 41.4 px, dark 0.34 → 0.34; pressure barely changes the width; the long stroke does not run out of paint.

## Brush Artist · Refs · #02 Henry Ward cream strokes
Gouache 1.00 · 46 px · 46.5 s

![Brush Artist · Refs · #02 Henry Ward cream strokes](Brush-Artist-Refs-02-Henry-Ward-cream-strokes.png)

A light paint: laid on a grey sheet (on white it cannot be seen); **dark** = how far it is from the grey either way.

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 10 % → 4 % | 29.4 px | 0.42 | 0.44 | 244 |
| heavy line | 12 % → 6 % | 35.0 px | 0.42 | 0.48 | 270 |
| pressure swell | 9 % → 6 % | 33.6 px | 0.43 | 0.65 | 179 |
| fast wave | 23 % → 3 % | 26.4 px | 0.42 | 0.14 | 565 |
| slow wave | 26 % → 9 % | 30.0 px | 0.42 | 0.35 | 1053 |
| spiral | 31 % → 6 % | 20.5 px | 0.42 | 0.20 | 896 |
| loop | 23 % → 7 % | 29.6 px | 0.42 | 0.29 | 457 |
| tilted | 12 % → 12 % | 34.7 px | 0.42 | 0.99 | 277 |
| over the wet one | 23 % → 11 % | 30.0 px | 0.42 | 0.50 | 223 |
| long, no reload | 25 % → 9 % | 11.0 px | 0.42 | 0.37 | 1330 | quarters: 0.01 → 0.02 → 0.03 → 0.03

Numbers say: light vs heavy: width 29.4 → 35.0 px, dark 0.42 → 0.42; the long stroke does not run out of paint.

## Brush Artist · Refs · #03 Henry Ward navy contours
Impasto 1.00 · 22 px · 20.6 s

![Brush Artist · Refs · #03 Henry Ward navy contours](Brush-Artist-Refs-03-Henry-Ward-navy-contours.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 7 % → 6 % | 19.4 px | 0.69 | 0.90 | 99 |
| heavy line | 7 % → 7 % | 21.1 px | 0.69 | 0.91 | 109 |
| pressure swell | 5 % → 5 % | 20.5 px | 0.74 | 0.91 | 79 |
| fast wave | 16 % → 11 % | 18.6 px | 0.73 | 0.71 | 293 |
| slow wave | 17 % → 12 % | 19.5 px | 0.73 | 0.74 | 457 |
| spiral | 25 % → 13 % | 16.3 px | 0.73 | 0.51 | 497 |
| loop | 14 % → 12 % | 18.6 px | 0.72 | 0.81 | 269 |
| tilted | 8 % → 8 % | 22.6 px | 0.72 | 1.00 | 139 |
| over the wet one | 15 % → 13 % | 19.0 px | 0.72 | 0.87 | 127 |
| long, no reload | 30 % → 13 % | 13.4 px | 0.73 | 0.42 | 726 | quarters: 0.31 → 0.25 → 0.19 → 0.11

Numbers say: light vs heavy: width 19.4 → 21.1 px, dark 0.69 → 0.69; pressure barely changes the width.

## Brush Artist · Refs · #04 Henry Ward grey cloud
Gouache 1.00 · 50 px · 47.9 s

![Brush Artist · Refs · #04 Henry Ward grey cloud](Brush-Artist-Refs-04-Henry-Ward-grey-cloud.png)

A light paint: laid on a grey sheet (on white it cannot be seen); **dark** = how far it is from the grey either way.

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 10 % → 7 % | 29.4 px | 0.34 | 0.71 | 221 |
| heavy line | 12 % → 8 % | 34.1 px | 0.34 | 0.65 | 261 |
| pressure swell | 10 % → 6 % | 36.0 px | 0.34 | 0.64 | 165 |
| fast wave | 19 % → 8 % | 22.4 px | 0.34 | 0.41 | 611 |
| slow wave | 27 % → 12 % | 30.8 px | 0.34 | 0.45 | 1054 |
| spiral | 25 % → 11 % | 16.7 px | 0.34 | 0.42 | 1107 |
| loop | 20 % → 11 % | 25.5 px | 0.34 | 0.56 | 509 |
| tilted | 12 % → 12 % | 33.9 px | 0.34 | 0.99 | 260 |
| over the wet one | 23 % → 17 % | 29.0 px | 0.34 | 0.76 | 230 |
| long, no reload | 29 % → 13 % | 12.9 px | 0.34 | 0.44 | 1311 | quarters: 0.01 → 0.02 → 0.02 → 0.02

Numbers say: light vs heavy: width 29.4 → 34.1 px, dark 0.34 → 0.34; the long stroke does not run out of paint.

## Brush Artist · Refs · #05 Henry Ward green in rust loops
Impasto 1.00 · 20 px · 19.8 s

![Brush Artist · Refs · #05 Henry Ward green in rust loops](Brush-Artist-Refs-05-Henry-Ward-green-in-rust-loops.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 7 % → 6 % | 18.9 px | 0.55 | 0.91 | 100 |
| heavy line | 7 % → 7 % | 20.7 px | 0.55 | 0.93 | 98 |
| pressure swell | 6 % → 5 % | 20.9 px | 0.57 | 0.91 | 98 |
| fast wave | 16 % → 11 % | 18.8 px | 0.56 | 0.69 | 278 |
| slow wave | 17 % → 12 % | 19.7 px | 0.56 | 0.69 | 462 |
| spiral | 25 % → 12 % | 16.8 px | 0.56 | 0.47 | 506 |
| loop | 14 % → 12 % | 18.8 px | 0.56 | 0.82 | 277 |
| tilted | 8 % → 8 % | 21.8 px | 0.55 | 0.99 | 121 |
| over the wet one | 14 % → 13 % | 18.6 px | 0.55 | 0.88 | 119 |
| long, no reload | 30 % → 12 % | 13.3 px | 0.56 | 0.41 | 698 | quarters: 0.24 → 0.18 → 0.11 → 0.04

Numbers say: light vs heavy: width 18.9 → 20.7 px, dark 0.55 → 0.55; pressure barely changes the width.

## Brush Artist · Refs · #06 Henry Ward scrubbed grey
Gouache 1.00 · 50 px · 46.8 s

![Brush Artist · Refs · #06 Henry Ward scrubbed grey](Brush-Artist-Refs-06-Henry-Ward-scrubbed-grey.png)

A light paint: laid on a grey sheet (on white it cannot be seen); **dark** = how far it is from the grey either way.

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 10 % → 7 % | 29.4 px | 0.35 | 0.71 | 211 |
| heavy line | 12 % → 8 % | 34.1 px | 0.35 | 0.65 | 220 |
| pressure swell | 10 % → 6 % | 36.0 px | 0.36 | 0.64 | 163 |
| fast wave | 19 % → 8 % | 22.4 px | 0.35 | 0.41 | 536 |
| slow wave | 27 % → 12 % | 30.8 px | 0.35 | 0.45 | 1054 |
| spiral | 25 % → 11 % | 16.7 px | 0.35 | 0.42 | 961 |
| loop | 20 % → 11 % | 25.5 px | 0.35 | 0.56 | 484 |
| tilted | 12 % → 12 % | 33.9 px | 0.35 | 0.99 | 257 |
| over the wet one | 23 % → 17 % | 29.0 px | 0.35 | 0.76 | 233 |
| long, no reload | 29 % → 13 % | 12.9 px | 0.35 | 0.44 | 1210 | quarters: 0.01 → 0.02 → 0.02 → 0.02

Numbers say: light vs heavy: width 29.4 → 34.1 px, dark 0.35 → 0.35; the long stroke does not run out of paint.

## Brush Artist · Refs · #07 Henry Ward blue L + black zigzag
Impasto 1.00 · 34 px · 22.4 s

![Brush Artist · Refs · #07 Henry Ward blue L + black zigzag](Brush-Artist-Refs-07-Henry-Ward-blue-L-black-zigzag.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 11 % → 9 % | 31.5 px | 0.57 | 0.87 | 154 |
| heavy line | 12 % → 10 % | 33.7 px | 0.57 | 0.89 | 170 |
| pressure swell | 9 % → 8 % | 33.3 px | 0.60 | 0.90 | 116 |
| fast wave | 26 % → 19 % | 30.6 px | 0.59 | 0.71 | 376 |
| slow wave | 27 % → 20 % | 31.5 px | 0.59 | 0.74 | 625 |
| spiral | 41 % → 21 % | 27.3 px | 0.59 | 0.52 | 651 |
| loop | 23 % → 18 % | 30.2 px | 0.59 | 0.78 | 344 |
| tilted | 11 % → 11 % | 30.2 px | 0.58 | 1.00 | 167 |
| over the wet one | 22 % → 19 % | 29.8 px | 0.58 | 0.89 | 149 |
| long, no reload | 48 % → 22 % | 21.4 px | 0.59 | 0.46 | 968 | quarters: 0.37 → 0.28 → 0.21 → 0.12

Numbers say: light vs heavy: width 31.5 → 33.7 px, dark 0.57 → 0.57; pressure barely changes the width.

## Brush Artist · Refs · #08 Henry Ward olive bands
Gouache 1.00 · 34 px · 32.7 s

![Brush Artist · Refs · #08 Henry Ward olive bands](Brush-Artist-Refs-08-Henry-Ward-olive-bands.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 4 % → 0 % | 10.7 px | 0.61 | 0.09 | 92 |
| heavy line | 7 % → 1 % | 21.4 px | 0.61 | 0.07 | 204 |
| pressure swell | 5 % → 1 % | 20.4 px | 0.61 | 0.16 | 252 |
| fast wave | 10 % → 1 % | 11.7 px | 0.61 | 0.08 | 361 |
| slow wave | 15 % → 1 % | 17.1 px | 0.61 | 0.09 | 648 |
| spiral | 21 % → 1 % | 13.6 px | 0.61 | 0.04 | 623 |
| loop | 13 % → 2 % | 17.3 px | 0.61 | 0.12 | 298 |
| tilted | 7 % → 7 % | 20.7 px | 0.61 | 0.97 | 162 |
| over the wet one | 14 % → 3 % | 18.8 px | 0.61 | 0.24 | 156 |
| long, no reload | 21 % → 2 % | 9.6 px | 0.61 | 0.07 | 886 | quarters: 0.24 → 0.14 → 0.08 → 0.06

Numbers say: light vs heavy: width 10.7 → 21.4 px, dark 0.61 → 0.61.

## Brush Artist · Refs · #09 Henry Ward white loops
Gouache 1.00 · 46 px · 43.8 s

![Brush Artist · Refs · #09 Henry Ward white loops](Brush-Artist-Refs-09-Henry-Ward-white-loops.png)

A light paint: laid on a grey sheet (on white it cannot be seen); **dark** = how far it is from the grey either way.

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 10 % → 4 % | 29.4 px | 0.45 | 0.44 | 204 |
| heavy line | 12 % → 6 % | 35.0 px | 0.45 | 0.48 | 216 |
| pressure swell | 9 % → 6 % | 33.6 px | 0.45 | 0.65 | 136 |
| fast wave | 23 % → 3 % | 26.4 px | 0.45 | 0.14 | 483 |
| slow wave | 26 % → 9 % | 30.0 px | 0.44 | 0.35 | 837 |
| spiral | 31 % → 6 % | 20.5 px | 0.44 | 0.20 | 840 |
| loop | 23 % → 7 % | 29.6 px | 0.44 | 0.29 | 465 |
| tilted | 12 % → 12 % | 34.7 px | 0.45 | 0.99 | 284 |
| over the wet one | 23 % → 11 % | 30.0 px | 0.45 | 0.50 | 206 |
| long, no reload | 25 % → 9 % | 11.0 px | 0.44 | 0.37 | 1069 | quarters: 0.01 → 0.02 → 0.03 → 0.03

Numbers say: light vs heavy: width 29.4 → 35.0 px, dark 0.45 → 0.45; the long stroke does not run out of paint.

## Brush Artist · Refs · #10 Henry Ward maroon loops
Impasto 1.00 · 30 px · 21.4 s

![Brush Artist · Refs · #10 Henry Ward maroon loops](Brush-Artist-Refs-10-Henry-Ward-maroon-loops.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 9 % → 8 % | 26.6 px | 0.70 | 0.91 | 133 |
| heavy line | 10 % → 9 % | 28.7 px | 0.70 | 0.93 | 121 |
| pressure swell | 8 % → 7 % | 28.3 px | 0.74 | 0.92 | 138 |
| fast wave | 23 % → 16 % | 26.2 px | 0.73 | 0.72 | 339 |
| slow wave | 24 % → 18 % | 27.4 px | 0.73 | 0.76 | 601 |
| spiral | 36 % → 18 % | 23.6 px | 0.73 | 0.52 | 605 |
| loop | 20 % → 17 % | 26.0 px | 0.73 | 0.83 | 304 |
| tilted | 10 % → 10 % | 28.0 px | 0.72 | 1.00 | 159 |
| over the wet one | 19 % → 17 % | 25.5 px | 0.72 | 0.91 | 126 |
| long, no reload | 42 % → 19 % | 19.0 px | 0.73 | 0.44 | 750 | quarters: 0.42 → 0.35 → 0.29 → 0.22

Numbers say: light vs heavy: width 26.6 → 28.7 px, dark 0.70 → 0.70; pressure barely changes the width.

## Brush Artist · Refs · #11 Henry Ward purple spun balls
Impasto 1.00 · 36 px · 22.0 s

![Brush Artist · Refs · #11 Henry Ward purple spun balls](Brush-Artist-Refs-11-Henry-Ward-purple-spun-balls.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 11 % → 11 % | 32.8 px | 0.70 | 0.93 | 166 |
| heavy line | 12 % → 11 % | 34.9 px | 0.70 | 0.94 | 148 |
| pressure swell | 9 % → 9 % | 35.0 px | 0.75 | 0.94 | 110 |
| fast wave | 27 % → 22 % | 31.5 px | 0.75 | 0.80 | 398 |
| slow wave | 28 % → 23 % | 32.8 px | 0.75 | 0.82 | 638 |
| spiral | 44 % → 25 % | 29.1 px | 0.74 | 0.56 | 673 |
| loop | 24 % → 21 % | 31.2 px | 0.74 | 0.87 | 315 |
| tilted | 11 % → 11 % | 30.2 px | 0.73 | 1.00 | 165 |
| over the wet one | 22 % → 20 % | 31.0 px | 0.73 | 0.92 | 147 |
| long, no reload | 50 % → 25 % | 22.6 px | 0.75 | 0.49 | 900 | quarters: 0.50 → 0.42 → 0.36 → 0.28

Numbers say: light vs heavy: width 32.8 → 34.9 px, dark 0.70 → 0.70; pressure barely changes the width.

## Brush Artist · Refs · #12 Henry Ward black-olive cage
Gouache 1.00 · 28 px · 31.4 s

![Brush Artist · Refs · #12 Henry Ward black-olive cage](Brush-Artist-Refs-12-Henry-Ward-black-olive-cage.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 4 % → 0 % | 11.3 px | 0.64 | 0.09 | 77 |
| heavy line | 7 % → 1 % | 18.9 px | 0.64 | 0.08 | 148 |
| pressure swell | 5 % → 1 % | 17.5 px | 0.64 | 0.17 | 84 |
| fast wave | 9 % → 1 % | 10.5 px | 0.64 | 0.12 | 277 |
| slow wave | 13 % → 1 % | 15.0 px | 0.64 | 0.09 | 472 |
| spiral | 19 % → 1 % | 12.4 px | 0.64 | 0.06 | 505 |
| loop | 12 % → 2 % | 14.9 px | 0.64 | 0.14 | 270 |
| tilted | 6 % → 6 % | 17.9 px | 0.64 | 0.96 | 126 |
| over the wet one | 12 % → 3 % | 16.6 px | 0.64 | 0.26 | 104 |
| long, no reload | 20 % → 2 % | 9.0 px | 0.64 | 0.08 | 638 | quarters: 0.23 → 0.14 → 0.09 → 0.07

Numbers say: light vs heavy: width 11.3 → 18.9 px, dark 0.64 → 0.64.

## Brush Artist · Refs · #13 Henry Ward blue streaky form
Gouache 1.00 · 50 px · 46.5 s

![Brush Artist · Refs · #13 Henry Ward blue streaky form](Brush-Artist-Refs-13-Henry-Ward-blue-streaky-form.png)

A light paint: laid on a grey sheet (on white it cannot be seen); **dark** = how far it is from the grey either way.

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 10 % → 7 % | 29.4 px | 0.35 | 0.71 | 221 |
| heavy line | 12 % → 8 % | 34.1 px | 0.35 | 0.65 | 213 |
| pressure swell | 10 % → 6 % | 36.0 px | 0.35 | 0.64 | 152 |
| fast wave | 19 % → 8 % | 22.4 px | 0.35 | 0.41 | 566 |
| slow wave | 27 % → 12 % | 30.8 px | 0.35 | 0.45 | 927 |
| spiral | 25 % → 11 % | 16.7 px | 0.35 | 0.42 | 888 |
| loop | 20 % → 11 % | 25.5 px | 0.35 | 0.56 | 568 |
| tilted | 12 % → 12 % | 33.9 px | 0.35 | 0.99 | 266 |
| over the wet one | 23 % → 17 % | 29.0 px | 0.35 | 0.76 | 215 |
| long, no reload | 29 % → 13 % | 12.9 px | 0.35 | 0.44 | 1220 | quarters: 0.01 → 0.02 → 0.02 → 0.02

Numbers say: light vs heavy: width 29.4 → 34.1 px, dark 0.35 → 0.35; the long stroke does not run out of paint.

## Brush Artist · Refs · #14 Henry Ward olive totem
Impasto 1.00 · 48 px · 25.1 s

![Brush Artist · Refs · #14 Henry Ward olive totem](Brush-Artist-Refs-14-Henry-Ward-olive-totem.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 15 % → 14 % | 44.1 px | 0.30 | 0.93 | 192 |
| heavy line | 16 % → 15 % | 46.7 px | 0.30 | 0.94 | 200 |
| pressure swell | 12 % → 12 % | 46.2 px | 0.32 | 0.95 | 157 |
| fast wave | 37 % → 30 % | 43.1 px | 0.30 | 0.80 | 531 |
| slow wave | 38 % → 31 % | 44.4 px | 0.30 | 0.82 | 919 |
| spiral | 55 % → 31 % | 36.4 px | 0.30 | 0.57 | 901 |
| loop | 32 % → 28 % | 42.0 px | 0.30 | 0.88 | 495 |
| tilted | 13 % → 13 % | 37.2 px | 0.31 | 1.00 | 232 |
| over the wet one | 28 % → 26 % | 40.5 px | 0.31 | 0.93 | 201 |
| long, no reload | 66 % → 33 % | 29.4 px | 0.30 | 0.51 | 1272 | quarters: 0.25 → 0.18 → 0.10 → 0.05

Numbers say: light vs heavy: width 44.1 → 46.7 px, dark 0.30 → 0.30; pressure barely changes the width.

## Brush Artist · Refs · #15 Ultramarine brush script
Ink 1.00 · 4 px · 31.1 s

![Brush Artist · Refs · #15 Ultramarine brush script](Brush-Artist-Refs-15-Ultramarine-brush-script.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 1 % → 3 % | 2.2 px | 0.55 | 3.90 | 43 |
| heavy line | 6 % → 6 % | 16.7 px | 0.58 | 0.99 | 59 |
| pressure swell | 3 % → 4 % | 12.1 px | 0.64 | 1.15 | 37 |
| fast wave | 9 % → 7 % | 10.6 px | 0.54 | 0.81 | 124 |
| slow wave | 7 % → 7 % | 8.4 px | 0.54 | 0.93 | 114 |
| spiral | 11 % → 7 % | 7.2 px | 0.52 | 0.66 | 218 |
| loop | 7 % → 7 % | 9.2 px | 0.53 | 0.98 | 84 |
| tilted | 3 % → 3 % | 8.2 px | 0.62 | 1.02 | 52 |
| over the wet one | 7 % → 7 % | 11.5 px | 0.62 | 1.06 | 48 |
| long, no reload | 16 % → 8 % | 7.3 px | 0.50 | 0.48 | 309 | quarters: 0.15 → 0.04 → 0.01 → 0.00

Numbers say: light vs heavy: width 2.2 → 16.7 px, dark 0.55 → 0.58; wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #18 Blue oil-stick scribbles
Pastel 1.00 · 10 px · 13.5 s

![Brush Artist · Refs · #18 Blue oil-stick scribbles](Brush-Artist-Refs-18-Blue-oil-stick-scribbles.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 1 % → 1 % | 2.9 px | 0.52 | 1.00 | 23 |
| heavy line | 2 % → 2 % | 5.5 px | 0.53 | 1.00 | 34 |
| pressure swell | 1 % → 1 % | 5.0 px | 0.53 | 1.00 | 24 |
| fast wave | 4 % → 4 % | 4.8 px | 0.53 | 1.00 | 88 |
| slow wave | 4 % → 4 % | 4.4 px | 0.53 | 1.00 | 74 |
| spiral | 7 % → 7 % | 4.5 px | 0.52 | 1.00 | 141 |
| loop | 3 % → 3 % | 4.5 px | 0.52 | 1.00 | 70 |
| tilted | 2 % → 2 % | 4.8 px | 0.53 | 1.00 | 47 |
| over the wet one | 3 % → 3 % | 4.7 px | 0.53 | 1.00 | 29 |
| long, no reload | 10 % → 10 % | 4.4 px | 0.53 | 1.00 | 215 | quarters: 0.06 → 0.06 → 0.06 → 0.06

Numbers say: light vs heavy: width 2.9 → 5.5 px, dark 0.52 → 0.53; the long stroke does not run out of paint.

## Brush Artist · Refs · #20 Orange-red crayon scribble
Pastel 1.00 · 14 px · 14.1 s

![Brush Artist · Refs · #20 Orange-red crayon scribble](Brush-Artist-Refs-20-Orange-red-crayon-scribble.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 1 % → 1 % | 4.0 px | 0.53 | 1.00 | 34 |
| heavy line | 3 % → 3 % | 8.0 px | 0.53 | 1.00 | 39 |
| pressure swell | 2 % → 2 % | 7.6 px | 0.53 | 1.00 | 27 |
| fast wave | 6 % → 6 % | 7.2 px | 0.53 | 1.00 | 81 |
| slow wave | 6 % → 6 % | 6.6 px | 0.53 | 1.00 | 104 |
| spiral | 9 % → 9 % | 6.2 px | 0.53 | 1.00 | 146 |
| loop | 5 % → 5 % | 6.2 px | 0.53 | 1.00 | 95 |
| tilted | 2 % → 2 % | 5.6 px | 0.53 | 1.00 | 39 |
| over the wet one | 4 % → 4 % | 6.6 px | 0.53 | 1.00 | 30 |
| long, no reload | 13 % → 13 % | 5.7 px | 0.53 | 1.00 | 218 | quarters: 0.07 → 0.07 → 0.08 → 0.08

Numbers say: light vs heavy: width 4.0 → 8.0 px, dark 0.53 → 0.53; the long stroke does not run out of paint.

## Brush Artist · Refs · #21 Gritty black contours
Gouache 1.00 · 12 px · 23.8 s

![Brush Artist · Refs · #21 Gritty black contours](Brush-Artist-Refs-21-Gritty-black-contours.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 1 % → 0 % | 2.8 px | 0.81 | 0.02 | 69 |
| heavy line | 2 % → 0 % | 6.1 px | 0.00 | 0.00 | 128 |
| pressure swell | 2 % → 0 % | 6.2 px | 0.81 | 0.03 | 82 |
| fast wave | 2 % → 0 % | 2.3 px | 0.00 | 0.00 | 251 |
| slow wave | 4 % → 0 % | 4.1 px | 0.81 | 0.02 | 288 |
| spiral | 4 % → 0 % | 2.9 px | 0.81 | 0.01 | 427 |
| loop | 3 % → 0 % | 4.3 px | 0.81 | 0.01 | 246 |
| tilted | 3 % → 2 % | 7.1 px | 0.81 | 0.89 | 123 |
| over the wet one | 4 % → 0 % | 5.1 px | 0.81 | 0.04 | 98 |
| long, no reload | 5 % → 0 % | 2.2 px | 0.81 | 0.01 | 614 | quarters: 0.10 → 0.04 → 0.03 → 0.02

Numbers say: light vs heavy: width 2.8 → 6.1 px, dark 0.81 → 0.00.

## Brush Artist · Refs · #22 Bold black brush poster
Ink 1.00 · 20 px · 37.8 s

![Brush Artist · Refs · #22 Bold black brush poster](Brush-Artist-Refs-22-Bold-black-brush-poster.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 3 % → 5 % | 9.6 px | 0.79 | 1.64 | 60 |
| heavy line | 15 % → 15 % | 44.6 px | 0.88 | 0.99 | 119 |
| pressure swell | 9 % → 9 % | 31.9 px | 0.87 | 1.04 | 72 |
| fast wave | 27 % → 27 % | 31.7 px | 0.87 | 0.98 | 228 |
| slow wave | 22 % → 22 % | 25.3 px | 0.87 | 0.99 | 367 |
| spiral | 34 % → 32 % | 22.4 px | 0.87 | 0.94 | 365 |
| loop | 20 % → 20 % | 26.3 px | 0.88 | 1.00 | 228 |
| tilted | 8 % → 8 % | 23.1 px | 0.88 | 1.01 | 83 |
| over the wet one | 19 % → 19 % | 30.3 px | 0.88 | 1.00 | 70 |
| long, no reload | 45 % → 38 % | 20.3 px | 0.86 | 0.83 | 522 | quarters: 0.54 → 0.45 → 0.35 → 0.26

Numbers say: light vs heavy: width 9.6 → 44.6 px, dark 0.79 → 0.88; wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #23 Dry white on orange + black line
Gouache 1.00 · 50 px · 30.7 s

![Brush Artist · Refs · #23 Dry white on orange + black line](Brush-Artist-Refs-23-Dry-white-on-orange-black-line.png)

A light paint: laid on a grey sheet (on white it cannot be seen); **dark** = how far it is from the grey either way.

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 6 % → 0 % | 17.3 px | 0.00 | 0.00 | 129 |
| heavy line | 10 % → 0 % | 29.7 px | 0.41 | 0.00 | 293 |
| pressure swell | 7 % → 0 % | 27.2 px | 0.41 | 0.02 | 151 |
| fast wave | 13 % → 0 % | 15.3 px | 0.41 | 0.01 | 530 |
| slow wave | 20 % → 0 % | 22.8 px | 0.40 | 0.02 | 900 |
| spiral | 23 % → 0 % | 15.4 px | 0.40 | 0.01 | 765 |
| loop | 17 % → 0 % | 22.5 px | 0.40 | 0.03 | 418 |
| tilted | 9 % → 8 % | 24.0 px | 0.40 | 0.93 | 261 |
| over the wet one | 17 % → 1 % | 23.3 px | 0.40 | 0.08 | 272 |
| long, no reload | 27 % → 1 % | 12.2 px | 0.40 | 0.03 | 1208 | quarters: 0.02 → 0.03 → 0.03 → 0.03

Numbers say: light vs heavy: width 17.3 → 29.7 px, dark 0.00 → 0.41; the long stroke does not run out of paint.

## Brush Artist · Refs · #24 Picasso flat oil
Oil 0.89 · Oil glaze 0.11 · 34 px · 26.4 s

![Brush Artist · Refs · #24 Picasso flat oil](Brush-Artist-Refs-24-Picasso-flat-oil.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 10 % → 10 % | 28.0 px | 0.38 | 1.00 | 159 |
| heavy line | 10 % → 10 % | 30.4 px | 0.39 | 1.00 | 161 |
| pressure swell | 8 % → 8 % | 29.5 px | 0.41 | 1.00 | 106 |
| fast wave | 25 % → 25 % | 29.0 px | 0.41 | 1.00 | 427 |
| slow wave | 27 % → 27 % | 30.6 px | 0.40 | 1.00 | 773 |
| spiral | 41 % → 41 % | 27.3 px | 0.40 | 1.00 | 696 |
| loop | 22 % → 22 % | 28.2 px | 0.40 | 1.00 | 379 |
| tilted | 11 % → 11 % | 31.3 px | 0.39 | 1.00 | 218 |
| over the wet one | 21 % → 21 % | 26.9 px | 0.39 | 1.00 | 176 |
| long, no reload | 51 % → 51 % | 22.9 px | 0.40 | 1.00 | 1017 | quarters: 0.25 → 0.23 → 0.21 → 0.20

Numbers say: light vs heavy: width 28.0 → 30.4 px, dark 0.38 → 0.39; pressure barely changes the width.

## Brush Artist · Refs · #25 Yellow heavy flat stroke
Impasto 1.00 · 110 px · 47.1 s

![Brush Artist · Refs · #25 Yellow heavy flat stroke](Brush-Artist-Refs-25-Yellow-heavy-flat-stroke.png)

A light paint: laid on a grey sheet (on white it cannot be seen); **dark** = how far it is from the grey either way.

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 35 % → 36 % | 101.5 px | 0.30 | 1.02 | 568 |
| heavy line | 36 % → 35 % | 105.1 px | 0.31 | 0.97 | 596 |
| pressure swell | 28 % → 29 % | 105.5 px | 0.30 | 1.04 | 394 |
| fast wave | 73 % → 76 % | 83.8 px | 0.31 | 1.05 | 1483 |
| slow wave | 73 % → 72 % | 84.7 px | 0.30 | 0.98 | 2642 |
| spiral | 86 % → 83 % | 56.7 px | 0.29 | 0.97 | 2752 |
| loop | 65 % → 64 % | 83.6 px | 0.31 | 0.99 | 1422 |
| tilted | 26 % → 26 % | 71.5 px | 0.30 | 1.00 | 740 |
| over the wet one | 55 % → 54 % | 83.2 px | 0.30 | 0.97 | 622 |
| long, no reload | 98 % → 97 % | 44.1 px | 0.30 | 0.99 | 3827 | quarters: 0.00 → 0.00 → 0.00 → 0.00

Numbers say: light vs heavy: width 101.5 → 105.1 px, dark 0.30 → 0.31; pressure barely changes the width; the long stroke does not run out of paint.

## Brush Artist · Refs · #27 Orange impasto swatch
Impasto 1.00 · 60 px · 28.6 s

![Brush Artist · Refs · #27 Orange impasto swatch](Brush-Artist-Refs-27-Orange-impasto-swatch.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 20 % → 19 % | 56.9 px | 0.34 | 0.97 | 267 |
| heavy line | 20 % → 20 % | 59.5 px | 0.34 | 0.97 | 296 |
| pressure swell | 16 % → 15 % | 59.6 px | 0.36 | 0.97 | 205 |
| fast wave | 48 % → 47 % | 55.1 px | 0.35 | 0.98 | 632 |
| slow wave | 48 % → 47 % | 55.9 px | 0.35 | 0.98 | 1171 |
| spiral | 69 % → 62 % | 45.5 px | 0.34 | 0.91 | 1126 |
| loop | 42 % → 40 % | 53.9 px | 0.35 | 0.97 | 601 |
| tilted | 16 % → 16 % | 44.0 px | 0.35 | 1.00 | 320 |
| over the wet one | 34 % → 33 % | 50.9 px | 0.35 | 0.96 | 281 |
| long, no reload | 85 % → 75 % | 38.1 px | 0.35 | 0.88 | 1775 | quarters: 0.33 → 0.31 → 0.30 → 0.26

Numbers say: light vs heavy: width 56.9 → 59.5 px, dark 0.34 → 0.34; pressure barely changes the width.

## Brush Artist · Refs · #28 Miles Davis black lines
Ink 1.00 · 22 px · 39.0 s

![Brush Artist · Refs · #28 Miles Davis black lines](Brush-Artist-Refs-28-Miles-Davis-black-lines.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 4 % → 6 % | 12.2 px | 0.81 | 1.49 | 48 |
| heavy line | 17 % → 17 % | 49.0 px | 0.88 | 0.99 | 117 |
| pressure swell | 10 % → 10 % | 35.9 px | 0.87 | 1.03 | 68 |
| fast wave | 31 % → 30 % | 35.4 px | 0.87 | 0.98 | 209 |
| slow wave | 25 % → 25 % | 28.7 px | 0.87 | 0.99 | 334 |
| spiral | 39 % → 37 % | 25.5 px | 0.87 | 0.95 | 371 |
| loop | 23 % → 23 % | 29.6 px | 0.88 | 1.00 | 178 |
| tilted | 9 % → 9 % | 25.3 px | 0.88 | 1.01 | 89 |
| over the wet one | 21 % → 21 % | 34.1 px | 0.88 | 1.01 | 102 |
| long, no reload | 51 % → 43 % | 22.9 px | 0.86 | 0.84 | 551 | quarters: 0.59 → 0.51 → 0.40 → 0.31

Numbers say: light vs heavy: width 12.2 → 49.0 px, dark 0.81 → 0.88.

## Brush Artist · Refs · #29 Shrigley magenta asterisk
Watercolour 1.00 · 70 px · 43.4 s

![Brush Artist · Refs · #29 Shrigley magenta asterisk](Brush-Artist-Refs-29-Shrigley-magenta-asterisk.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 10 % → 13 % | 28.0 px | 0.61 | 1.39 | 75 |
| heavy line | 17 % → 18 % | 50.3 px | 0.61 | 1.04 | 198 |
| pressure swell | 11 % → 13 % | 41.1 px | 0.62 | 1.14 | 127 |
| fast wave | 38 % → 38 % | 43.8 px | 0.60 | 1.01 | 382 |
| slow wave | 35 % → 39 % | 41.0 px | 0.62 | 1.11 | 592 |
| spiral | 61 % → 61 % | 40.0 px | 0.60 | 1.01 | 628 |
| loop | 31 % → 32 % | 40.2 px | 0.61 | 1.03 | 336 |
| tilted | 18 % → 18 % | 49.0 px | 0.61 | 1.00 | 286 |
| over the wet one | 31 % → 34 % | 38.5 px | 0.61 | 1.08 | 165 |
| long, no reload | 75 % → 76 % | 33.6 px | 0.60 | 1.01 | 1021 | quarters: 0.53 → 0.50 → 0.48 → 0.45

Numbers say: light vs heavy: width 28.0 → 50.3 px, dark 0.61 → 0.61; the long stroke does not run out of paint.

## Brush Artist · Refs · #30 Red gouache face patch
Gouache 1.00 · 60 px · 53.7 s

![Brush Artist · Refs · #30 Red gouache face patch](Brush-Artist-Refs-30-Red-gouache-face-patch.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 16 % → 15 % | 47.0 px | 0.49 | 0.91 | 181 |
| heavy line | 25 % → 20 % | 73.9 px | 0.49 | 0.80 | 310 |
| pressure swell | 19 % → 17 % | 72.6 px | 0.49 | 0.86 | 186 |
| fast wave | 49 % → 28 % | 56.1 px | 0.49 | 0.58 | 680 |
| slow wave | 48 % → 28 % | 55.4 px | 0.49 | 0.59 | 1095 |
| spiral | 60 % → 28 % | 39.3 px | 0.49 | 0.47 | 1021 |
| loop | 40 % → 29 % | 51.6 px | 0.49 | 0.74 | 503 |
| tilted | 16 % → 17 % | 46.0 px | 0.49 | 1.00 | 320 |
| over the wet one | 36 % → 32 % | 55.3 px | 0.49 | 0.89 | 256 |
| long, no reload | 67 % → 30 % | 30.0 px | 0.49 | 0.44 | 1472 | quarters: 0.43 → 0.39 → 0.32 → 0.26

Numbers say: light vs heavy: width 47.0 → 73.9 px, dark 0.49 → 0.49.

## Brush Artist · Refs · #31 Warhol blotted line
Ink 1.00 · 6 px · 29.7 s

![Brush Artist · Refs · #31 Warhol blotted line](Brush-Artist-Refs-31-Warhol-blotted-line.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 1 % → 3 % | 2.7 px | 0.75 | 3.31 | 45 |
| heavy line | 7 % → 7 % | 20.7 px | 0.83 | 0.98 | 79 |
| pressure swell | 4 % → 4 % | 14.8 px | 0.84 | 1.12 | 61 |
| fast wave | 12 % → 9 % | 13.9 px | 0.82 | 0.76 | 167 |
| slow wave | 10 % → 8 % | 11.2 px | 0.80 | 0.84 | 144 |
| spiral | 15 % → 8 % | 9.7 px | 0.80 | 0.58 | 244 |
| loop | 9 % → 9 % | 11.9 px | 0.80 | 0.93 | 135 |
| tilted | 3 % → 3 % | 8.8 px | 0.84 | 1.03 | 55 |
| over the wet one | 8 % → 8 % | 14.4 px | 0.84 | 1.02 | 62 |
| long, no reload | 21 % → 9 % | 9.5 px | 0.78 | 0.43 | 368 | quarters: 0.25 → 0.13 → 0.04 → 0.01

Numbers say: light vs heavy: width 2.7 → 20.7 px, dark 0.75 → 0.83; wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #32 Thick orange swipes
Impasto 1.00 · 90 px · 41.3 s

![Brush Artist · Refs · #32 Thick orange swipes](Brush-Artist-Refs-32-Thick-orange-swipes.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 29 % → 29 % | 83.2 px | 0.37 | 1.00 | 404 |
| heavy line | 30 % → 29 % | 86.5 px | 0.38 | 0.97 | 482 |
| pressure swell | 23 % → 23 % | 86.6 px | 0.38 | 1.01 | 332 |
| fast wave | 63 % → 65 % | 73.1 px | 0.38 | 1.03 | 1110 |
| slow wave | 64 % → 63 % | 73.5 px | 0.38 | 0.98 | 1948 |
| spiral | 79 % → 77 % | 52.2 px | 0.38 | 0.98 | 1951 |
| loop | 57 % → 56 % | 73.4 px | 0.38 | 0.99 | 970 |
| tilted | 21 % → 21 % | 59.3 px | 0.38 | 1.00 | 508 |
| over the wet one | 47 % → 45 % | 71.0 px | 0.38 | 0.97 | 444 |
| long, no reload | 95 % → 93 % | 42.8 px | 0.38 | 0.98 | 2674 | quarters: 0.38 → 0.38 → 0.37 → 0.35

Numbers say: light vs heavy: width 83.2 → 86.5 px, dark 0.37 → 0.38; pressure barely changes the width; the long stroke does not run out of paint.

## Brush Artist · Refs · #33 Red wet-in-wet band
Watercolour 1.00 · 80 px · 61.2 s

![Brush Artist · Refs · #33 Red wet-in-wet band](Brush-Artist-Refs-33-Red-wet-in-wet-band.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 24 % → 42 % | 69.9 px | 0.53 | 1.73 | 187 |
| heavy line | 34 % → 50 % | 97.7 px | 0.54 | 1.48 | 343 |
| pressure swell | 20 % → 30 % | 73.7 px | 0.57 | 1.54 | 225 |
| fast wave | 65 % → 80 % | 75.4 px | 0.61 | 1.22 | 742 |
| slow wave | 61 % → 78 % | 70.0 px | 0.63 | 1.29 | 1186 |
| spiral | 78 % → 89 % | 51.5 px | 0.64 | 1.15 | 1153 |
| loop | 54 % → 68 % | 70.2 px | 0.62 | 1.25 | 588 |
| tilted | 28 % → 30 % | 77.1 px | 0.57 | 1.08 | 415 |
| over the wet one | 55 % → 79 % | 75.2 px | 0.57 | 1.45 | 270 |
| long, no reload | 96 % → 99 % | 43.2 px | 0.66 | 1.03 | 1786 | quarters: 0.68 → 0.68 → 0.68 → 0.63

Numbers say: light vs heavy: width 69.9 → 97.7 px, dark 0.53 → 0.54; the long stroke does not run out of paint; wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #34 Magenta oil patches
Oil 0.89 · Oil glaze 0.11 · 60 px · 29.6 s

![Brush Artist · Refs · #34 Magenta oil patches](Brush-Artist-Refs-34-Magenta-oil-patches.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 18 % → 18 % | 52.7 px | 0.60 | 1.01 | 275 |
| heavy line | 20 % → 20 % | 57.0 px | 0.61 | 1.00 | 314 |
| pressure swell | 15 % → 15 % | 55.7 px | 0.62 | 1.01 | 234 |
| fast wave | 48 % → 48 % | 55.0 px | 0.61 | 1.02 | 798 |
| slow wave | 48 % → 48 % | 55.7 px | 0.61 | 1.00 | 1278 |
| spiral | 71 % → 71 % | 46.8 px | 0.61 | 1.00 | 1294 |
| loop | 41 % → 41 % | 53.3 px | 0.61 | 1.00 | 675 |
| tilted | 16 % → 16 % | 46.0 px | 0.60 | 1.00 | 342 |
| over the wet one | 34 % → 34 % | 47.8 px | 0.60 | 1.00 | 326 |
| long, no reload | 83 % → 83 % | 37.1 px | 0.61 | 1.00 | 1832 | quarters: 0.57 → 0.56 → 0.54 → 0.47

Numbers say: light vs heavy: width 52.7 → 57.0 px, dark 0.60 → 0.61; pressure barely changes the width.

## Brush Artist · Refs · #35 Red band with runs
Watercolour 1.00 · 70 px · 61.2 s

![Brush Artist · Refs · #35 Red band with runs](Brush-Artist-Refs-35-Red-band-with-runs.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 40 % → 45 % | 115.4 px | 0.42 | 1.14 | 203 |
| heavy line | 46 % → 51 % | 133.2 px | 0.42 | 1.12 | 342 |
| pressure swell | 21 % → 28 % | 77.8 px | 0.48 | 1.36 | 220 |
| fast wave | 67 % → 77 % | 77.5 px | 0.49 | 1.14 | 740 |
| slow wave | 65 % → 75 % | 75.0 px | 0.52 | 1.16 | 1145 |
| spiral | 87 % → 94 % | 57.4 px | 0.53 | 1.09 | 1104 |
| loop | 79 % → 88 % | 102.3 px | 0.48 | 1.11 | 565 |
| tilted | 50 % → 50 % | 138.2 px | 0.47 | 1.02 | 363 |
| over the wet one | 77 % → 84 % | 76.2 px | 0.47 | 1.10 | 281 |
| long, no reload | 97 % → 100 % | 43.5 px | 0.58 | 1.03 | 1475 | quarters: 0.60 → 0.60 → 0.59 → 0.56

Numbers say: light vs heavy: width 115.4 → 133.2 px, dark 0.42 → 0.42; the long stroke does not run out of paint.

## Brush Artist · Refs · #36 Magenta letters flat brush
Gouache 1.00 · 36 px · 43.6 s

![Brush Artist · Refs · #36 Magenta letters flat brush](Brush-Artist-Refs-36-Magenta-letters-flat-brush.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 10 % → 10 % | 29.0 px | 0.45 | 0.98 | 104 |
| heavy line | 17 % → 14 % | 49.0 px | 0.45 | 0.85 | 153 |
| pressure swell | 13 % → 12 % | 49.3 px | 0.45 | 0.89 | 111 |
| fast wave | 35 % → 19 % | 40.9 px | 0.45 | 0.54 | 321 |
| slow wave | 35 % → 19 % | 40.0 px | 0.45 | 0.54 | 505 |
| spiral | 46 % → 19 % | 30.4 px | 0.45 | 0.42 | 558 |
| loop | 27 % → 20 % | 35.4 px | 0.45 | 0.72 | 284 |
| tilted | 11 % → 11 % | 30.0 px | 0.45 | 1.00 | 170 |
| over the wet one | 24 % → 23 % | 38.1 px | 0.45 | 0.93 | 148 |
| long, no reload | 46 % → 19 % | 20.8 px | 0.45 | 0.40 | 809 | quarters: 0.29 → 0.26 → 0.22 → 0.18

Numbers say: light vs heavy: width 29.0 → 49.0 px, dark 0.45 → 0.45.

## Brush Artist · Refs · #37 Oil still life dabs
Oil 0.89 · Oil glaze 0.11 · 40 px · 26.4 s

![Brush Artist · Refs · #37 Oil still life dabs](Brush-Artist-Refs-37-Oil-still-life-dabs.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 12 % → 12 % | 35.4 px | 0.36 | 1.00 | 194 |
| heavy line | 13 % → 13 % | 38.6 px | 0.36 | 1.00 | 223 |
| pressure swell | 10 % → 10 % | 37.8 px | 0.40 | 1.00 | 173 |
| fast wave | 31 % → 31 % | 36.3 px | 0.39 | 1.00 | 510 |
| slow wave | 33 % → 33 % | 38.0 px | 0.39 | 1.00 | 919 |
| spiral | 51 % → 51 % | 33.9 px | 0.38 | 1.00 | 854 |
| loop | 27 % → 27 % | 35.4 px | 0.39 | 1.00 | 437 |
| tilted | 13 % → 13 % | 35.5 px | 0.38 | 1.00 | 231 |
| over the wet one | 25 % → 25 % | 33.6 px | 0.38 | 1.00 | 203 |
| long, no reload | 61 % → 61 % | 27.2 px | 0.38 | 1.00 | 1258 | quarters: 0.29 → 0.26 → 0.24 → 0.21

Numbers say: light vs heavy: width 35.4 → 38.6 px, dark 0.36 → 0.36; pressure barely changes the width.

## Brush Artist · Refs · #38 Sanguine drawing
Pastel 1.00 · 6 px · 12.8 s

![Brush Artist · Refs · #38 Sanguine drawing](Brush-Artist-Refs-38-Sanguine-drawing.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 1 % → 1 % | 2.0 px | 0.61 | 1.00 | 22 |
| heavy line | 1 % → 1 % | 3.5 px | 0.62 | 1.00 | 24 |
| pressure swell | 1 % → 1 % | 3.3 px | 0.62 | 1.00 | 15 |
| fast wave | 3 % → 3 % | 3.2 px | 0.61 | 1.00 | 64 |
| slow wave | 3 % → 3 % | 3.0 px | 0.61 | 1.00 | 53 |
| spiral | 4 % → 4 % | 2.9 px | 0.61 | 1.00 | 117 |
| loop | 2 % → 2 % | 3.0 px | 0.61 | 1.00 | 40 |
| tilted | 1 % → 1 % | 3.4 px | 0.62 | 1.00 | 26 |
| over the wet one | 2 % → 2 % | 2.9 px | 0.62 | 1.00 | 22 |
| long, no reload | 7 % → 7 % | 3.0 px | 0.61 | 1.00 | 158 | quarters: 0.04 → 0.05 → 0.05 → 0.05

Numbers say: light vs heavy: width 2.0 → 3.5 px, dark 0.61 → 0.62; the long stroke does not run out of paint.

## Brush Artist · Refs · #39 Very thick impasto
Impasto 1.00 · 60 px · 28.1 s

![Brush Artist · Refs · #39 Very thick impasto](Brush-Artist-Refs-39-Very-thick-impasto.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 20 % → 19 % | 57.0 px | 0.60 | 0.97 | 242 |
| heavy line | 21 % → 20 % | 59.6 px | 0.60 | 0.97 | 275 |
| pressure swell | 16 % → 15 % | 59.7 px | 0.63 | 0.97 | 201 |
| fast wave | 48 % → 47 % | 55.2 px | 0.62 | 0.98 | 677 |
| slow wave | 49 % → 47 % | 56.1 px | 0.62 | 0.98 | 1156 |
| spiral | 69 % → 65 % | 45.6 px | 0.62 | 0.93 | 1174 |
| loop | 42 % → 41 % | 54.0 px | 0.62 | 0.97 | 676 |
| tilted | 16 % → 16 % | 44.1 px | 0.61 | 1.00 | 381 |
| over the wet one | 34 % → 33 % | 51.0 px | 0.61 | 0.97 | 296 |
| long, no reload | 85 % → 79 % | 38.3 px | 0.62 | 0.93 | 1769 | quarters: 0.58 → 0.57 → 0.55 → 0.52

Numbers say: light vs heavy: width 57.0 → 59.6 px, dark 0.60 → 0.60; pressure barely changes the width; the long stroke does not run out of paint.

## Brush Artist · Refs · #40 Watercolour blooms
Watercolour 1.00 · 90 px · 58.4 s

![Brush Artist · Refs · #40 Watercolour blooms](Brush-Artist-Refs-40-Watercolour-blooms.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 27 % → 46 % | 79.5 px | 0.08 | 1.69 | 250 |
| heavy line | 39 % → 53 % | 112.7 px | 0.09 | 1.36 | 435 |
| pressure swell | 26 % → 40 % | 98.0 px | 0.09 | 1.54 | 268 |
| fast wave | 68 % → 82 % | 78.6 px | 0.11 | 1.21 | 865 |
| slow wave | 68 % → 81 % | 78.9 px | 0.15 | 1.19 | 1572 |
| spiral | 83 % → 93 % | 54.4 px | 0.15 | 1.13 | 1411 |
| loop | 59 % → 72 % | 75.9 px | 0.13 | 1.24 | 769 |
| tilted | 33 % → 36 % | 93.0 px | 0.12 | 1.07 | 507 |
| over the wet one | 61 % → 81 % | 77.1 px | 0.12 | 1.33 | 341 |
| long, no reload | 98 % → 100 % | 43.9 px | 0.17 | 1.02 | 1887 | quarters: 0.21 → 0.20 → 0.17 → 0.12

Numbers say: light vs heavy: width 79.5 → 112.7 px, dark 0.08 → 0.09; wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #41 Coloured pencil hatching
Pastel 1.00 · 4 px · 13.2 s

![Brush Artist · Refs · #41 Coloured pencil hatching](Brush-Artist-Refs-41-Coloured-pencil-hatching.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 1 % → 1 % | 1.6 px | 0.42 | 1.00 | 14 |
| heavy line | 1 % → 1 % | 2.6 px | 0.43 | 1.00 | 14 |
| pressure swell | 1 % → 1 % | 2.1 px | 0.43 | 1.00 | 17 |
| fast wave | 2 % → 2 % | 2.2 px | 0.42 | 1.00 | 50 |
| slow wave | 2 % → 2 % | 2.1 px | 0.43 | 1.00 | 43 |
| spiral | 3 % → 3 % | 2.1 px | 0.43 | 1.00 | 89 |
| loop | 2 % → 2 % | 2.2 px | 0.43 | 1.00 | 50 |
| tilted | 1 % → 1 % | 3.0 px | 0.42 | 1.00 | 19 |
| over the wet one | 2 % → 2 % | 2.2 px | 0.42 | 1.00 | 12 |
| long, no reload | 5 % → 5 % | 2.3 px | 0.43 | 1.00 | 148 | quarters: 0.02 → 0.02 → 0.02 → 0.03

Numbers say: light vs heavy: width 1.6 → 2.6 px, dark 0.42 → 0.43; the long stroke does not run out of paint.

## Brush Artist · Refs · #42 Oil pastel shaggy
Pastel 1.00 · 18 px · 13.9 s

![Brush Artist · Refs · #42 Oil pastel shaggy](Brush-Artist-Refs-42-Oil-pastel-shaggy.png)

A light paint: laid on a grey sheet (on white it cannot be seen); **dark** = how far it is from the grey either way.

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 2 % → 2 % | 5.1 px | 0.35 | 1.00 | 28 |
| heavy line | 4 % → 4 % | 10.7 px | 0.36 | 1.00 | 39 |
| pressure swell | 3 % → 3 % | 9.5 px | 0.36 | 1.00 | 25 |
| fast wave | 8 % → 8 % | 9.0 px | 0.36 | 1.00 | 92 |
| slow wave | 7 % → 7 % | 8.2 px | 0.36 | 1.00 | 115 |
| spiral | 12 % → 12 % | 7.8 px | 0.36 | 1.00 | 149 |
| loop | 6 % → 6 % | 7.9 px | 0.36 | 1.00 | 73 |
| tilted | 2 % → 2 % | 6.9 px | 0.36 | 1.00 | 43 |
| over the wet one | 6 % → 6 % | 8.5 px | 0.36 | 1.00 | 33 |
| long, no reload | 15 % → 15 % | 6.9 px | 0.36 | 1.00 | 244 | quarters: 0.00 → 0.00 → 0.00 → 0.00

Numbers say: light vs heavy: width 5.1 → 10.7 px, dark 0.35 → 0.36; the long stroke does not run out of paint.

## Brush Artist · Refs · #43 Dragged black ink blocks
Gouache 1.00 · 70 px · 31.3 s

![Brush Artist · Refs · #43 Dragged black ink blocks](Brush-Artist-Refs-43-Dragged-black-ink-blocks.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 10 % → 1 % | 30.5 px | 0.65 | 0.09 | 214 |
| heavy line | 17 % → 2 % | 48.7 px | 0.65 | 0.13 | 459 |
| pressure swell | 12 % → 3 % | 44.8 px | 0.65 | 0.25 | 303 |
| fast wave | 27 % → 3 % | 30.9 px | 0.65 | 0.12 | 750 |
| slow wave | 34 % → 4 % | 38.7 px | 0.65 | 0.12 | 1149 |
| spiral | 43 % → 4 % | 28.2 px | 0.65 | 0.10 | 846 |
| loop | 31 % → 4 % | 39.7 px | 0.65 | 0.14 | 441 |
| tilted | 13 % → 13 % | 37.6 px | 0.65 | 0.99 | 258 |
| over the wet one | 28 % → 10 % | 40.7 px | 0.65 | 0.37 | 214 |
| long, no reload | 48 % → 7 % | 21.6 px | 0.65 | 0.15 | 1183 | quarters: 0.49 → 0.38 → 0.30 → 0.22

Numbers say: light vs heavy: width 30.5 → 48.7 px, dark 0.65 → 0.65.

## Brush Artist · Refs · #44 Blue looping ribbon
Oil 1.00 · 80 px · 29.8 s

![Brush Artist · Refs · #44 Blue looping ribbon](Brush-Artist-Refs-44-Blue-looping-ribbon.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 25 % → 26 % | 72.8 px | 0.70 | 1.04 | 466 |
| heavy line | 27 % → 27 % | 78.1 px | 0.69 | 1.00 | 469 |
| pressure swell | 20 % → 21 % | 76.2 px | 0.72 | 1.03 | 310 |
| fast wave | 62 % → 64 % | 71.1 px | 0.72 | 1.04 | 1112 |
| slow wave | 62 % → 62 % | 72.0 px | 0.73 | 1.00 | 2421 |
| spiral | 76 % → 77 % | 50.4 px | 0.72 | 1.00 | 1290 |
| loop | 55 % → 55 % | 70.7 px | 0.72 | 1.00 | 683 |
| tilted | 20 % → 20 % | 56.9 px | 0.71 | 1.00 | 352 |
| over the wet one | 43 % → 43 % | 63.7 px | 0.71 | 1.00 | 291 |
| long, no reload | 93 % → 93 % | 41.6 px | 0.73 | 1.00 | 2027 | quarters: 0.72 → 0.71 → 0.71 → 0.64

Numbers say: light vs heavy: width 72.8 → 78.1 px, dark 0.70 → 0.69; pressure barely changes the width; the long stroke does not run out of paint.

## Brush Artist · Refs · #45 Soft pastel pepper
Pastel 1.00 · 40 px · 11.7 s

![Brush Artist · Refs · #45 Soft pastel pepper](Brush-Artist-Refs-45-Soft-pastel-pepper.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 4 % → 4 % | 11.3 px | 0.53 | 1.00 | 76 |
| heavy line | 8 % → 8 % | 23.0 px | 0.53 | 1.00 | 48 |
| pressure swell | 5 % → 5 % | 19.5 px | 0.53 | 1.00 | 35 |
| fast wave | 17 % → 17 % | 19.4 px | 0.53 | 1.00 | 131 |
| slow wave | 15 % → 15 % | 17.1 px | 0.53 | 1.00 | 214 |
| spiral | 25 % → 25 % | 16.3 px | 0.53 | 1.00 | 216 |
| loop | 12 % → 12 % | 16.1 px | 0.53 | 1.00 | 110 |
| tilted | 5 % → 5 % | 12.8 px | 0.53 | 1.00 | 78 |
| over the wet one | 11 % → 11 % | 17.7 px | 0.53 | 1.00 | 49 |
| long, no reload | 30 % → 30 % | 13.6 px | 0.53 | 1.00 | 295 | quarters: 0.18 → 0.18 → 0.18 → 0.18

Numbers say: light vs heavy: width 11.3 → 23.0 px, dark 0.53 → 0.53; the long stroke does not run out of paint.

## Brush Artist · Refs · #46 Red-brown ink lips
Watercolour 1.00 · 50 px · 44.6 s

![Brush Artist · Refs · #46 Red-brown ink lips](Brush-Artist-Refs-46-Red-brown-ink-lips.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 15 % → 31 % | 43.2 px | 0.58 | 2.07 | 66 |
| heavy line | 22 % → 36 % | 62.9 px | 0.60 | 1.64 | 110 |
| pressure swell | 13 % → 22 % | 47.7 px | 0.64 | 1.71 | 70 |
| fast wave | 41 % → 64 % | 47.9 px | 0.64 | 1.55 | 233 |
| slow wave | 41 % → 63 % | 46.9 px | 0.67 | 1.54 | 404 |
| spiral | 65 % → 79 % | 42.7 px | 0.69 | 1.23 | 390 |
| loop | 37 % → 56 % | 47.7 px | 0.66 | 1.51 | 212 |
| tilted | 20 % → 23 % | 56.2 px | 0.60 | 1.12 | 292 |
| over the wet one | 41 % → 63 % | 57.1 px | 0.60 | 1.55 | 178 |
| long, no reload | 80 % → 96 % | 35.8 px | 0.70 | 1.20 | 734 | quarters: 0.71 → 0.71 → 0.70 → 0.65

Numbers say: light vs heavy: width 43.2 → 62.9 px, dark 0.58 → 0.60; the long stroke does not run out of paint; wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #47 Pink knife slabs
Impasto 1.00 · 90 px · 30.6 s

![Brush Artist · Refs · #47 Pink knife slabs](Brush-Artist-Refs-47-Pink-knife-slabs.png)

A light paint: laid on a grey sheet (on white it cannot be seen); **dark** = how far it is from the grey either way.

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 28 % → 27 % | 81.2 px | 0.29 | 0.97 | 207 |
| heavy line | 29 % → 28 % | 83.6 px | 0.29 | 0.97 | 238 |
| pressure swell | 22 % → 22 % | 83.5 px | 0.29 | 1.01 | 162 |
| fast wave | 61 % → 60 % | 70.3 px | 0.28 | 0.99 | 554 |
| slow wave | 61 % → 59 % | 71.0 px | 0.27 | 0.96 | 985 |
| spiral | 76 % → 57 % | 50.1 px | 0.27 | 0.76 | 967 |
| loop | 55 % → 54 % | 71.7 px | 0.28 | 0.97 | 678 |
| tilted | 21 % → 21 % | 59.3 px | 0.29 | 1.00 | 435 |
| over the wet one | 46 % → 44 % | 68.1 px | 0.29 | 0.96 | 261 |
| long, no reload | 92 % → 76 % | 41.4 px | 0.26 | 0.83 | 1599 | quarters: 0.00 → 0.00 → 0.00 → 0.00

Numbers say: light vs heavy: width 81.2 → 83.6 px, dark 0.29 → 0.29; pressure barely changes the width; the long stroke does not run out of paint.

## Brush Artist · Refs · #48 Black bands with drips
Gouache 1.00 · 70 px · 48.1 s

![Brush Artist · Refs · #48 Black bands with drips](Brush-Artist-Refs-48-Black-bands-with-drips.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 27 % → 24 % | 79.0 px | 0.64 | 0.87 | 194 |
| heavy line | 35 % → 29 % | 102.8 px | 0.64 | 0.82 | 287 |
| pressure swell | 25 % → 22 % | 91.9 px | 0.64 | 0.89 | 674 |
| fast wave | 64 % → 43 % | 74.0 px | 0.64 | 0.67 | 624 |
| slow wave | 61 % → 41 % | 70.7 px | 0.64 | 0.67 | 1002 |
| spiral | 69 % → 39 % | 45.7 px | 0.64 | 0.56 | 1073 |
| loop | 54 % → 42 % | 70.4 px | 0.64 | 0.77 | 536 |
| tilted | 29 % → 29 % | 80.7 px | 0.64 | 1.00 | 286 |
| over the wet one | 58 % → 49 % | 80.4 px | 0.64 | 0.85 | 218 |
| long, no reload | 78 % → 39 % | 34.9 px | 0.64 | 0.50 | 1298 | quarters: 0.61 → 0.57 → 0.51 → 0.42

Numbers say: light vs heavy: width 79.0 → 102.8 px, dark 0.64 → 0.64.

## Brush Artist · Refs · #49 Magenta letters round brush
Ink 1.00 · 30 px · 34.7 s

![Brush Artist · Refs · #49 Magenta letters round brush](Brush-Artist-Refs-49-Magenta-letters-round-brush.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 6 % → 8 % | 17.4 px | 0.50 | 1.29 | 41 |
| heavy line | 21 % → 21 % | 61.9 px | 0.51 | 0.99 | 121 |
| pressure swell | 12 % → 13 % | 46.3 px | 0.52 | 1.02 | 81 |
| fast wave | 39 % → 38 % | 44.8 px | 0.51 | 0.99 | 412 |
| slow wave | 32 % → 31 % | 36.7 px | 0.51 | 0.99 | 356 |
| spiral | 50 % → 49 % | 33.2 px | 0.51 | 0.97 | 426 |
| loop | 29 % → 29 % | 37.8 px | 0.51 | 1.00 | 163 |
| tilted | 11 % → 11 % | 30.9 px | 0.52 | 1.01 | 76 |
| over the wet one | 26 % → 26 % | 42.0 px | 0.52 | 1.01 | 91 |
| long, no reload | 62 % → 56 % | 27.7 px | 0.50 | 0.91 | 626 | quarters: 0.41 → 0.36 → 0.30 → 0.25

Numbers say: light vs heavy: width 17.4 → 61.9 px, dark 0.50 → 0.51.

## Brush Artist · Refs · #50 Thick swipes on photo
Impasto 1.00 · 40 px · 19.0 s

![Brush Artist · Refs · #50 Thick swipes on photo](Brush-Artist-Refs-50-Thick-swipes-on-photo.png)

A light paint: laid on a grey sheet (on white it cannot be seen); **dark** = how far it is from the grey either way.

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 13 % → 13 % | 38.1 px | 0.27 | 0.96 | 154 |
| heavy line | 14 % → 13 % | 40.2 px | 0.27 | 0.96 | 129 |
| pressure swell | 11 % → 10 % | 40.1 px | 0.25 | 0.95 | 93 |
| fast wave | 33 % → 31 % | 38.4 px | 0.25 | 0.93 | 302 |
| slow wave | 34 % → 32 % | 39.1 px | 0.26 | 0.95 | 663 |
| spiral | 58 % → 46 % | 38.5 px | 0.25 | 0.79 | 612 |
| loop | 28 % → 27 % | 36.9 px | 0.26 | 0.95 | 317 |
| tilted | 12 % → 12 % | 34.1 px | 0.26 | 1.00 | 149 |
| over the wet one | 25 % → 24 % | 35.3 px | 0.26 | 0.95 | 138 |
| long, no reload | 66 % → 46 % | 29.5 px | 0.24 | 0.69 | 795 | quarters: 0.00 → 0.00 → 0.00 → 0.00

Numbers say: light vs heavy: width 38.1 → 40.2 px, dark 0.27 → 0.27; pressure barely changes the width; the long stroke does not run out of paint.

## Brush Artist · Refs · Drag #e8b4a8
Gouache 1.00 · 40 px · 23.2 s

![Brush Artist · Refs · Drag #e8b4a8](Brush-Artist-Refs-Drag-e8b4a8.png)

A light paint: laid on a grey sheet (on white it cannot be seen); **dark** = how far it is from the grey either way.

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 4 % → 0 % | 12.7 px | 0.35 | 0.03 | 129 |
| heavy line | 5 % → 0 % | 14.4 px | 0.34 | 0.03 | 117 |
| pressure swell | 4 % → 0 % | 15.5 px | 0.34 | 0.07 | 101 |
| fast wave | 6 % → 0 % | 6.4 px | 0.34 | 0.05 | 271 |
| slow wave | 12 % → 0 % | 13.8 px | 0.34 | 0.02 | 502 |
| spiral | 10 % → 0 % | 6.6 px | 0.34 | 0.05 | 498 |
| loop | 8 % → 1 % | 10.3 px | 0.34 | 0.09 | 376 |
| tilted | 6 % → 5 % | 16.1 px | 0.34 | 0.90 | 167 |
| over the wet one | 10 % → 1 % | 12.4 px | 0.34 | 0.15 | 153 |
| long, no reload | 9 % → 1 % | 4.0 px | 0.34 | 0.10 | 651 | quarters: 0.01 → 0.01 → 0.02 → 0.02

Numbers say: light vs heavy: width 12.7 → 14.4 px, dark 0.35 → 0.34; the long stroke does not run out of paint.

## Brush Artist · Refs · Drag #e8e4e0
Gouache 1.00 · 40 px · 23.1 s

![Brush Artist · Refs · Drag #e8e4e0](Brush-Artist-Refs-Drag-e8e4e0.png)

A light paint: laid on a grey sheet (on white it cannot be seen); **dark** = how far it is from the grey either way.

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 4 % → 0 % | 12.7 px | 0.43 | 0.03 | 109 |
| heavy line | 5 % → 0 % | 14.4 px | 0.43 | 0.03 | 104 |
| pressure swell | 4 % → 0 % | 15.5 px | 0.43 | 0.07 | 104 |
| fast wave | 6 % → 0 % | 6.4 px | 0.43 | 0.05 | 318 |
| slow wave | 12 % → 0 % | 13.8 px | 0.42 | 0.02 | 508 |
| spiral | 10 % → 0 % | 6.6 px | 0.42 | 0.05 | 487 |
| loop | 8 % → 1 % | 10.3 px | 0.42 | 0.09 | 269 |
| tilted | 6 % → 5 % | 16.1 px | 0.42 | 0.90 | 150 |
| over the wet one | 10 % → 1 % | 12.4 px | 0.42 | 0.15 | 106 |
| long, no reload | 9 % → 1 % | 4.0 px | 0.42 | 0.10 | 649 | quarters: 0.01 → 0.02 → 0.02 → 0.02

Numbers say: light vs heavy: width 12.7 → 14.4 px, dark 0.43 → 0.43; the long stroke does not run out of paint.

## Brush Artist · Refs · Finger
Pastel 1.00 · 36 px · 23.0 s · over bands of wet oil paint and oil pastel in turn (it works on paint already there: look at what it does to the bands; covered counts the bands too)

![Brush Artist · Refs · Finger](Brush-Artist-Refs-Finger.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 25 % → 25 % | 73.8 px | 0.80 | 1.00 | 49 |
| heavy line | 27 % → 27 % | 78.6 px | 0.80 | 1.00 | 67 |
| pressure swell | 26 % → 26 % | 97.7 px | 0.80 | 1.00 | 36 |
| fast wave | 32 % → 32 % | 37.3 px | 0.78 | 1.00 | 134 |
| slow wave | 31 % → 31 % | 36.3 px | 0.78 | 1.00 | 251 |
| spiral | 38 % → 38 % | 25.2 px | 0.76 | 1.00 | 230 |
| loop | 30 % → 30 % | 39.5 px | 0.78 | 1.00 | 120 |
| tilted | 26 % → 26 % | 73.4 px | 0.78 | 1.00 | 81 |
| over the wet one | 29 % → 29 % | 6.8 px | 0.78 | 1.00 | 48 |
| long, no reload | 41 % → 41 % | 18.2 px | 0.76 | 1.00 | 307 | quarters: 0.25 → 0.37 → 0.34 → 0.39

Numbers say: light vs heavy: width 73.8 → 78.6 px, dark 0.80 → 0.80; pressure barely changes the width; the long stroke does not run out of paint.

## Brush Artist · Ink — wash
Watercolour 1.00 · 38 px · 34.0 s

![Brush Artist · Ink — wash](Brush-Artist-Ink-wash.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 11 % → 11 % | 31.6 px | 0.39 | 1.04 | 70 |
| heavy line | 19 % → 19 % | 54.3 px | 0.32 | 1.03 | 125 |
| pressure swell | 12 % → 13 % | 45.2 px | 0.37 | 1.04 | 62 |
| fast wave | 39 % → 41 % | 45.5 px | 0.31 | 1.04 | 206 |
| slow wave | 37 % → 38 % | 42.9 px | 0.37 | 1.03 | 364 |
| spiral | 58 % → 61 % | 38.6 px | 0.31 | 1.04 | 385 |
| loop | 32 % → 33 % | 41.9 px | 0.35 | 1.02 | 160 |
| tilted | 13 % → 14 % | 37.0 px | 0.38 | 1.04 | 105 |
| over the wet one | 29 % → 30 % | 42.8 px | 0.38 | 1.04 | 92 |
| long, no reload | 67 % → 72 % | 30.0 px | 0.29 | 1.07 | 668 | quarters: 0.34 → 0.27 → 0.19 → 0.12

Numbers say: light vs heavy: width 31.6 → 54.3 px, dark 0.39 → 0.32.

## Brush Artist · Ink — brush line
Ink 1.00 · 16 px · 28.8 s

![Brush Artist · Ink — brush line](Brush-Artist-Ink-brush-line.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 3 % → 5 % | 7.7 px | 0.78 | 1.81 | 42 |
| heavy line | 13 % → 13 % | 38.9 px | 0.88 | 0.99 | 104 |
| pressure swell | 8 % → 8 % | 28.4 px | 0.87 | 1.05 | 47 |
| fast wave | 24 % → 23 % | 28.0 px | 0.87 | 0.96 | 146 |
| slow wave | 20 % → 19 % | 22.6 px | 0.87 | 0.97 | 164 |
| spiral | 30 % → 27 % | 20.1 px | 0.86 | 0.89 | 284 |
| loop | 18 % → 18 % | 23.6 px | 0.88 | 1.00 | 141 |
| tilted | 7 % → 7 % | 20.5 px | 0.88 | 1.01 | 82 |
| over the wet one | 17 % → 17 % | 26.8 px | 0.88 | 1.00 | 76 |
| long, no reload | 42 % → 30 % | 18.9 px | 0.85 | 0.71 | 395 | quarters: 0.49 → 0.40 → 0.30 → 0.20

Numbers say: light vs heavy: width 7.7 → 38.9 px, dark 0.78 → 0.88; wet paint spreads well beyond the stroke.

## Brush Artist · Ink — dry brush
Gouache 1.00 · 30 px · 22.6 s

![Brush Artist · Ink — dry brush](Brush-Artist-Ink-dry-brush.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 3 % → 0 % | 9.8 px | 0.00 | 0.00 | 45 |
| heavy line | 6 % → 0 % | 16.0 px | 0.77 | 0.01 | 122 |
| pressure swell | 4 % → 0 % | 15.4 px | 0.77 | 0.05 | 62 |
| fast wave | 7 % → 0 % | 8.5 px | 0.77 | 0.05 | 248 |
| slow wave | 11 % → 0 % | 12.3 px | 0.77 | 0.03 | 446 |
| spiral | 14 % → 0 % | 9.0 px | 0.77 | 0.03 | 331 |
| loop | 9 % → 1 % | 12.0 px | 0.77 | 0.05 | 179 |
| tilted | 6 % → 5 % | 15.8 px | 0.77 | 0.94 | 134 |
| over the wet one | 10 % → 1 % | 13.2 px | 0.77 | 0.14 | 134 |
| long, no reload | 15 % → 1 % | 6.6 px | 0.77 | 0.05 | 577 | quarters: 0.23 → 0.13 → 0.09 → 0.08

Numbers say: light vs heavy: width 9.8 → 16.0 px, dark 0.00 → 0.77.

## Brush Artist · Watercolour — blue
Watercolour 0.93 · Ink 0.07 · 40 px · 32.2 s

![Brush Artist · Watercolour — blue](Brush-Artist-Watercolour-blue.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 6 % → 11 % | 16.2 px | 0.29 | 1.88 | 32 |
| heavy line | 11 % → 13 % | 31.9 px | 0.29 | 1.17 | 105 |
| pressure swell | 7 % → 9 % | 25.7 px | 0.30 | 1.38 | 52 |
| fast wave | 24 % → 27 % | 28.2 px | 0.29 | 1.12 | 163 |
| slow wave | 23 % → 32 % | 26.4 px | 0.31 | 1.41 | 246 |
| spiral | 39 % → 47 % | 25.6 px | 0.29 | 1.21 | 246 |
| loop | 20 % → 25 % | 25.7 px | 0.30 | 1.25 | 154 |
| tilted | 12 % → 12 % | 34.0 px | 0.30 | 1.00 | 108 |
| over the wet one | 21 % → 25 % | 25.2 px | 0.30 | 1.19 | 65 |
| long, no reload | 53 % → 59 % | 23.6 px | 0.30 | 1.12 | 412 | quarters: 0.23 → 0.21 → 0.19 → 0.16

Numbers say: light vs heavy: width 16.2 → 31.9 px, dark 0.29 → 0.29; wet paint spreads well beyond the stroke.

## Brush Artist · Watercolour — violet
Watercolour 0.93 · Ink 0.07 · 40 px · 32.8 s

![Brush Artist · Watercolour — violet](Brush-Artist-Watercolour-violet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 6 % → 11 % | 16.2 px | 0.36 | 1.88 | 39 |
| heavy line | 11 % → 13 % | 31.9 px | 0.37 | 1.17 | 74 |
| pressure swell | 7 % → 9 % | 25.7 px | 0.38 | 1.38 | 55 |
| fast wave | 24 % → 27 % | 28.2 px | 0.38 | 1.12 | 160 |
| slow wave | 23 % → 32 % | 26.4 px | 0.39 | 1.41 | 273 |
| spiral | 39 % → 47 % | 25.6 px | 0.37 | 1.21 | 274 |
| loop | 20 % → 25 % | 25.7 px | 0.38 | 1.25 | 131 |
| tilted | 12 % → 12 % | 34.0 px | 0.38 | 1.00 | 106 |
| over the wet one | 21 % → 25 % | 25.2 px | 0.38 | 1.19 | 64 |
| long, no reload | 53 % → 59 % | 23.6 px | 0.38 | 1.12 | 423 | quarters: 0.28 → 0.27 → 0.24 → 0.21

Numbers say: light vs heavy: width 16.2 → 31.9 px, dark 0.36 → 0.37; wet paint spreads well beyond the stroke.

## Brush Artist · Watercolour — teal
Watercolour 0.93 · Ink 0.07 · 40 px · 33.7 s

![Brush Artist · Watercolour — teal](Brush-Artist-Watercolour-teal.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 6 % → 11 % | 16.2 px | 0.23 | 1.88 | 47 |
| heavy line | 11 % → 13 % | 31.9 px | 0.23 | 1.17 | 72 |
| pressure swell | 7 % → 9 % | 25.7 px | 0.24 | 1.38 | 46 |
| fast wave | 24 % → 27 % | 28.2 px | 0.23 | 1.12 | 154 |
| slow wave | 23 % → 32 % | 26.4 px | 0.25 | 1.41 | 247 |
| spiral | 39 % → 47 % | 25.6 px | 0.23 | 1.21 | 297 |
| loop | 20 % → 25 % | 25.7 px | 0.24 | 1.25 | 131 |
| tilted | 12 % → 12 % | 34.0 px | 0.24 | 1.00 | 113 |
| over the wet one | 21 % → 25 % | 25.2 px | 0.24 | 1.19 | 80 |
| long, no reload | 53 % → 59 % | 23.6 px | 0.24 | 1.12 | 431 | quarters: 0.18 → 0.16 → 0.15 → 0.13

Numbers say: light vs heavy: width 16.2 → 31.9 px, dark 0.23 → 0.23; wet paint spreads well beyond the stroke.

## Brush Artist · Gouache
Gouache 1.00 · 30 px · 38.3 s

![Brush Artist · Gouache](Brush-Artist-Gouache.png)

A light paint: laid on a grey sheet (on white it cannot be seen); **dark** = how far it is from the grey either way.

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 8 % → 8 % | 24.4 px | 0.27 | 0.97 | 89 |
| heavy line | 15 % → 12 % | 42.8 px | 0.27 | 0.78 | 114 |
| pressure swell | 11 % → 9 % | 41.0 px | 0.27 | 0.85 | 67 |
| fast wave | 30 % → 14 % | 34.9 px | 0.26 | 0.45 | 229 |
| slow wave | 29 % → 14 % | 34.0 px | 0.26 | 0.47 | 407 |
| spiral | 40 % → 14 % | 26.6 px | 0.26 | 0.35 | 365 |
| loop | 24 % → 15 % | 30.6 px | 0.26 | 0.62 | 193 |
| tilted | 10 % → 10 % | 27.4 px | 0.27 | 1.01 | 132 |
| over the wet one | 22 % → 19 % | 32.9 px | 0.27 | 0.89 | 70 |
| long, no reload | 43 % → 15 % | 19.1 px | 0.26 | 0.35 | 537 | quarters: 0.01 → 0.01 → 0.01 → 0.01

Numbers say: light vs heavy: width 24.4 → 42.8 px, dark 0.27 → 0.27; the long stroke does not run out of paint.

## Brush Artist · Oil — bristle
Oil 0.89 · Oil glaze 0.11 · 30 px · 15.1 s

![Brush Artist · Oil — bristle](Brush-Artist-Oil-bristle.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 9 % → 9 % | 26.3 px | 0.53 | 1.00 | 111 |
| heavy line | 10 % → 10 % | 28.6 px | 0.54 | 1.00 | 126 |
| pressure swell | 8 % → 8 % | 28.2 px | 0.55 | 1.00 | 110 |
| fast wave | 24 % → 24 % | 27.3 px | 0.55 | 1.00 | 327 |
| slow wave | 25 % → 25 % | 28.3 px | 0.55 | 1.00 | 588 |
| spiral | 39 % → 39 % | 25.6 px | 0.54 | 1.00 | 529 |
| loop | 20 % → 20 % | 26.3 px | 0.54 | 1.00 | 281 |
| tilted | 11 % → 11 % | 29.9 px | 0.52 | 1.00 | 141 |
| over the wet one | 20 % → 20 % | 25.5 px | 0.52 | 1.00 | 110 |
| long, no reload | 50 % → 50 % | 22.4 px | 0.54 | 1.00 | 761 | quarters: 0.32 → 0.30 → 0.29 → 0.28

Numbers say: light vs heavy: width 26.3 → 28.6 px, dark 0.53 → 0.54; pressure barely changes the width; the long stroke does not run out of paint.

## Brush Artist · Charcoal — stick
Charcoal 0.78 · Pastel 0.22 · 28 px · 10.9 s

![Brush Artist · Charcoal — stick](Brush-Artist-Charcoal-stick.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 5 % → 5 % | 15.3 px | 0.85 | 1.00 | 29 |
| heavy line | 8 % → 8 % | 23.3 px | 0.85 | 1.00 | 31 |
| pressure swell | 5 % → 5 % | 19.8 px | 0.85 | 1.00 | 21 |
| fast wave | 18 % → 18 % | 20.7 px | 0.85 | 1.00 | 149 |
| slow wave | 17 % → 17 % | 19.5 px | 0.85 | 1.00 | 119 |
| spiral | 29 % → 29 % | 19.3 px | 0.85 | 1.00 | 119 |
| loop | 15 % → 15 % | 19.3 px | 0.85 | 1.00 | 62 |
| tilted | 6 % → 6 % | 16.6 px | 0.85 | 1.00 | 36 |
| over the wet one | 13 % → 13 % | 19.8 px | 0.85 | 1.00 | 18 |
| long, no reload | 41 % → 41 % | 18.2 px | 0.85 | 1.00 | 202 | quarters: 0.38 → 0.38 → 0.38 → 0.38

Numbers say: light vs heavy: width 15.3 → 23.3 px, dark 0.85 → 0.85; the long stroke does not run out of paint.

## Brush Artist · Charcoal — stick B
Charcoal 0.78 · Pastel 0.22 · 36 px · 11.5 s

![Brush Artist · Charcoal — stick B](Brush-Artist-Charcoal-stick-B.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 7 % → 7 % | 19.8 px | 0.85 | 1.00 | 24 |
| heavy line | 10 % → 10 % | 30.4 px | 0.85 | 1.00 | 43 |
| pressure swell | 7 % → 7 % | 25.9 px | 0.85 | 1.00 | 38 |
| fast wave | 23 % → 23 % | 26.8 px | 0.85 | 1.00 | 96 |
| slow wave | 22 % → 22 % | 25.5 px | 0.85 | 1.00 | 160 |
| spiral | 38 % → 38 % | 25.4 px | 0.85 | 1.00 | 190 |
| loop | 19 % → 19 % | 25.0 px | 0.85 | 1.00 | 96 |
| tilted | 7 % → 7 % | 20.4 px | 0.85 | 1.00 | 48 |
| over the wet one | 17 % → 17 % | 25.9 px | 0.85 | 1.00 | 36 |
| long, no reload | 51 % → 51 % | 22.6 px | 0.85 | 1.00 | 227 | quarters: 0.47 → 0.47 → 0.47 → 0.47

Numbers say: light vs heavy: width 19.8 → 30.4 px, dark 0.85 → 0.85; the long stroke does not run out of paint.

## Brush Artist · Charcoal — stick C
Charcoal 0.78 · Pastel 0.22 · 22 px · 11.1 s

![Brush Artist · Charcoal — stick C](Brush-Artist-Charcoal-stick-C.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 4 % → 4 % | 12.6 px | 0.85 | 1.00 | 17 |
| heavy line | 7 % → 7 % | 19.0 px | 0.85 | 1.00 | 30 |
| pressure swell | 4 % → 4 % | 16.2 px | 0.85 | 1.00 | 13 |
| fast wave | 15 % → 15 % | 16.9 px | 0.85 | 1.00 | 65 |
| slow wave | 14 % → 14 % | 15.8 px | 0.85 | 1.00 | 88 |
| spiral | 24 % → 24 % | 15.7 px | 0.85 | 1.00 | 122 |
| loop | 12 % → 12 % | 15.9 px | 0.85 | 1.00 | 40 |
| tilted | 5 % → 5 % | 14.4 px | 0.85 | 1.00 | 25 |
| over the wet one | 11 % → 11 % | 16.1 px | 0.85 | 1.00 | 22 |
| long, no reload | 34 % → 34 % | 15.2 px | 0.85 | 1.00 | 152 | quarters: 0.32 → 0.32 → 0.32 → 0.32

Numbers say: light vs heavy: width 12.6 → 19.0 px, dark 0.85 → 0.85; the long stroke does not run out of paint.

## Brush Artist · Refs · #01 Henry Ward peach cloud — own sheet
own sheet 600 × 600 · Gouache 1.00 · 44 px · 16.8 s

![Brush Artist · Refs · #01 Henry Ward peach cloud — own sheet](Brush-Artist-Refs-01-Henry-Ward-peach-cloud-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 13 % → 32 % | 36.6 px | 0.57 | 2.51 | 159 |
| stroke 2 | 21 % → 49 % | 70.5 px | 0.57 | 2.28 | 153 |
| stroke 3 | 25 % → 46 % | 72.9 px | 0.57 | 1.84 | 120 |
| stroke 4 | 26 % → 50 % | 85.4 px | 0.57 | 1.90 | 131 |
| stroke 5 | 26 % → 46 % | 75.4 px | 0.57 | 1.78 | 173 |
| stroke 6 | 26 % → 35 % | 80.3 px | 0.57 | 1.33 | 124 |
| stroke 7 | 15 % → 53 % | 37.9 px | 0.57 | 3.47 | 119 |
| stroke 8 | 18 % → 49 % | 45.5 px | 0.57 | 2.72 | 184 |
| stroke 9 | 21 % → 50 % | 54.8 px | 0.57 | 2.36 | 177 |
| stroke 10 | 23 % → 51 % | 62.1 px | 0.57 | 2.20 | 153 |
| stroke 11 | 26 % → 54 % | 72.3 px | 0.57 | 2.10 | 160 |
| stroke 12 | 29 % → 56 % | 86.7 px | 0.57 | 1.95 | 142 |
| stroke 13 | 37 % → 59 % | 108.1 px | 0.57 | 1.58 | 188 |
| stroke 14 | 40 % → 61 % | 114.5 px | 0.57 | 1.52 | 151 |
| stroke 15 | 53 % → 67 % | 156.1 px | 0.57 | 1.27 | 166 |
| stroke 16 | 55 % → 68 % | 166.0 px | 0.57 | 1.23 | 149 |
| stroke 17 | 56 % → 69 % | 157.1 px | 0.57 | 1.23 | 196 |
| stroke 18 | 57 % → 68 % | 165.7 px | 0.57 | 1.18 | 167 |
| stroke 19 | 59 % → 66 % | 164.5 px | 0.57 | 1.13 | 188 |
| stroke 20 | 58 % → 63 % | 167.9 px | 0.57 | 1.09 | 154 |
| stroke 21 | 58 % → 60 % | 168.2 px | 0.57 | 1.04 | 177 |
| stroke 22 | 59 % → 61 % | 173.0 px | 0.57 | 1.03 | 454 |
| stroke 23 | 59 % → 59 % | 168.1 px | 0.57 | 1.01 | 193 |
| stroke 24 | 63 % → 62 % | 187.8 px | 0.57 | 1.00 | 194 |

Numbers say: wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #02 Henry Ward cream strokes — own sheet
own sheet 600 × 600 · Gouache 1.00 · 46 px · 9.6 s

![Brush Artist · Refs · #02 Henry Ward cream strokes — own sheet](Brush-Artist-Refs-02-Henry-Ward-cream-strokes-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 14 % → 15 % | 29.6 px | 0.66 | 1.04 | 227 |
| stroke 2 | 21 % → 17 % | 55.3 px | 0.66 | 0.82 | 185 |
| stroke 3 | 21 % → 21 % | 52.3 px | 0.66 | 1.02 | 219 |
| stroke 4 | 22 % → 19 % | 53.7 px | 0.66 | 0.87 | 227 |
| stroke 5 | 27 % → 23 % | 67.5 px | 0.66 | 0.84 | 186 |
| stroke 6 | 22 % → 20 % | 52.9 px | 0.66 | 0.89 | 187 |
| stroke 7 | 22 % → 13 % | 55.9 px | 0.65 | 0.59 | 201 |

## Brush Artist · Refs · #03 Henry Ward navy contours — own sheet
own sheet 600 × 600 · Impasto 1.00 · 22 px · 2.9 s

![Brush Artist · Refs · #03 Henry Ward navy contours — own sheet](Brush-Artist-Refs-03-Henry-Ward-navy-contours-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 10 % → 15 % | 20.3 px | 0.69 | 1.51 | 124 |
| stroke 2 | 18 % → 20 % | 25.7 px | 0.69 | 1.12 | 117 |
| stroke 3 | 21 % → 21 % | 30.8 px | 0.69 | 1.00 | 117 |
| stroke 4 | 20 % → 18 % | 45.1 px | 0.69 | 0.89 | 162 |

Numbers say: wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #04 Henry Ward grey cloud — own sheet
own sheet 600 × 600 · Gouache 1.00 · 50 px · 17.1 s

![Brush Artist · Refs · #04 Henry Ward grey cloud — own sheet](Brush-Artist-Refs-04-Henry-Ward-grey-cloud-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 9 % → 38 % | 26.9 px | 0.39 | 4.15 | 203 |
| stroke 2 | 14 % → 40 % | 39.8 px | 0.39 | 2.86 | 236 |
| stroke 3 | 20 % → 46 % | 55.7 px | 0.39 | 2.29 | 182 |
| stroke 4 | 24 % → 48 % | 71.2 px | 0.39 | 1.98 | 230 |
| stroke 5 | 30 % → 54 % | 91.4 px | 0.39 | 1.81 | 234 |
| stroke 6 | 31 % → 56 % | 101.9 px | 0.39 | 1.80 | 205 |
| stroke 7 | 36 % → 64 % | 106.4 px | 0.39 | 1.75 | 283 |
| stroke 8 | 37 % → 64 % | 111.3 px | 0.39 | 1.70 | 233 |
| stroke 9 | 34 % → 63 % | 102.7 px | 0.39 | 1.83 | 228 |
| stroke 10 | 37 % → 63 % | 119.8 px | 0.39 | 1.68 | 224 |
| stroke 11 | 36 % → 62 % | 102.3 px | 0.39 | 1.71 | 551 |
| stroke 12 | 37 % → 62 % | 111.4 px | 0.39 | 1.68 | 311 |
| stroke 13 | 37 % → 64 % | 106.7 px | 0.39 | 1.71 | 271 |
| stroke 14 | 37 % → 64 % | 110.5 px | 0.39 | 1.72 | 330 |
| stroke 15 | 36 % → 58 % | 104.3 px | 0.39 | 1.61 | 294 |
| stroke 16 | 39 % → 56 % | 118.4 px | 0.39 | 1.44 | 273 |
| stroke 17 | 37 % → 48 % | 106.1 px | 0.39 | 1.30 | 252 |
| stroke 18 | 37 % → 45 % | 122.7 px | 0.39 | 1.21 | 241 |
| stroke 19 | 36 % → 38 % | 108.5 px | 0.39 | 1.04 | 261 |
| stroke 20 | 40 % → 38 % | 124.7 px | 0.39 | 0.95 | 254 |

Numbers say: wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #05 Henry Ward green in rust loops — own sheet
own sheet 600 × 600 · Impasto 1.00 · 20 px · 3.2 s

![Brush Artist · Refs · #05 Henry Ward green in rust loops — own sheet](Brush-Artist-Refs-05-Henry-Ward-green-in-rust-loops-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 11 % → 18 % | 20.2 px | 0.02 | 1.55 | 118 |
| stroke 2 | 12 % → 11 % | 22.7 px | 0.03 | 0.92 | 228 |
| stroke 3 | 22 % → 20 % | 40.1 px | 0.03 | 0.92 | 129 |

Numbers say: wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #06 Henry Ward scrubbed grey — own sheet
own sheet 600 × 600 · Gouache 1.00 · 50 px · 19.4 s

![Brush Artist · Refs · #06 Henry Ward scrubbed grey — own sheet](Brush-Artist-Refs-06-Henry-Ward-scrubbed-grey-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 11 % → 42 % | 26.1 px | 0.39 | 3.97 | 306 |
| stroke 2 | 14 % → 45 % | 37.2 px | 0.39 | 3.19 | 315 |
| stroke 3 | 20 % → 47 % | 60.7 px | 0.39 | 2.39 | 243 |
| stroke 4 | 23 % → 48 % | 71.6 px | 0.39 | 2.12 | 250 |
| stroke 5 | 31 % → 61 % | 94.0 px | 0.39 | 1.95 | 246 |
| stroke 6 | 35 % → 61 % | 108.4 px | 0.39 | 1.73 | 256 |
| stroke 7 | 38 % → 64 % | 108.4 px | 0.39 | 1.69 | 270 |
| stroke 8 | 40 % → 64 % | 125.9 px | 0.39 | 1.62 | 251 |
| stroke 9 | 36 % → 63 % | 111.8 px | 0.39 | 1.74 | 207 |
| stroke 10 | 36 % → 61 % | 117.7 px | 0.39 | 1.70 | 252 |
| stroke 11 | 38 % → 63 % | 110.7 px | 0.39 | 1.66 | 305 |
| stroke 12 | 40 % → 63 % | 121.3 px | 0.39 | 1.58 | 274 |
| stroke 13 | 37 % → 63 % | 103.7 px | 0.39 | 1.74 | 293 |
| stroke 14 | 36 % → 63 % | 104.4 px | 0.39 | 1.78 | 287 |
| stroke 15 | 36 % → 64 % | 103.4 px | 0.39 | 1.77 | 260 |
| stroke 16 | 36 % → 61 % | 116.7 px | 0.39 | 1.67 | 257 |
| stroke 17 | 35 % → 54 % | 104.7 px | 0.39 | 1.53 | 272 |
| stroke 18 | 37 % → 52 % | 111.9 px | 0.39 | 1.40 | 265 |
| stroke 19 | 36 % → 48 % | 108.1 px | 0.39 | 1.31 | 269 |
| stroke 20 | 38 % → 46 % | 118.2 px | 0.39 | 1.21 | 254 |
| stroke 21 | 37 % → 38 % | 106.6 px | 0.39 | 1.04 | 257 |
| stroke 22 | 35 % → 34 % | 116.6 px | 0.39 | 0.96 | 253 |

Numbers say: wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #07 Henry Ward blue L + black zigzag — own sheet
own sheet 600 × 600 · Impasto 1.00 · 34 px · 2.8 s

![Brush Artist · Refs · #07 Henry Ward blue L + black zigzag — own sheet](Brush-Artist-Refs-07-Henry-Ward-blue-L-black-zigzag-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 14 % → 16 % | 32.3 px | 0.59 | 1.12 | 211 |
| stroke 2 | 16 % → 14 % | 39.3 px | 0.59 | 0.90 | 114 |

## Brush Artist · Refs · #08 Henry Ward olive bands — own sheet
own sheet 600 × 600 · Gouache 1.00 · 34 px · 7.1 s

![Brush Artist · Refs · #08 Henry Ward olive bands — own sheet](Brush-Artist-Refs-08-Henry-Ward-olive-bands-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 10 % → 8 % | 20.0 px | 0.58 | 0.79 | 271 |
| stroke 2 | 16 % → 10 % | 37.0 px | 0.58 | 0.58 | 207 |
| stroke 3 | 15 % → 14 % | 31.4 px | 0.58 | 0.93 | 212 |
| stroke 4 | 16 % → 11 % | 35.7 px | 0.58 | 0.68 | 234 |
| stroke 5 | 24 % → 14 % | 48.5 px | 0.58 | 0.61 | 217 |
| stroke 6 | 15 % → 8 % | 29.2 px | 0.58 | 0.52 | 204 |

## Brush Artist · Refs · #09 Henry Ward white loops — own sheet
own sheet 600 × 600 · Gouache 1.00 · 46 px · 9.7 s

![Brush Artist · Refs · #09 Henry Ward white loops — own sheet](Brush-Artist-Refs-09-Henry-Ward-white-loops-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 17 % → 4 % | 8.9 px | 0.06 | 0.22 | 1036 |
| stroke 2 | 17 % → 3 % | 17.3 px | 0.07 | 0.15 | 1208 |
| stroke 3 | 24 % → 2 % | 22.7 px | 0.07 | 0.10 | 1138 |
| stroke 4 | 3 % → 1 % | 7.6 px | 0.06 | 0.32 | 219 |
| stroke 5 | 3 % → 1 % | 7.5 px | 0.07 | 0.40 | 201 |
| stroke 6 | 3 % → 2 % | 7.9 px | 0.07 | 0.85 | 188 |
| stroke 7 | 5 % → 2 % | 13.9 px | 0.07 | 0.46 | 185 |
| stroke 8 | 4 % → 1 % | 7.3 px | 0.06 | 0.35 | 222 |

## Brush Artist · Refs · #10 Henry Ward maroon loops — own sheet
own sheet 600 × 600 · Impasto 1.00 · 30 px · 4.1 s

![Brush Artist · Refs · #10 Henry Ward maroon loops — own sheet](Brush-Artist-Refs-10-Henry-Ward-maroon-loops-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 11 % → 26 % | 26.6 px | 0.72 | 2.43 | 273 |
| stroke 2 | 21 % → 39 % | 46.5 px | 0.71 | 1.87 | 127 |
| stroke 3 | 28 % → 35 % | 55.9 px | 0.72 | 1.27 | 215 |
| stroke 4 | 39 % → 38 % | 87.9 px | 0.72 | 0.97 | 140 |
| stroke 5 | 32 % → 29 % | 80.9 px | 0.72 | 0.91 | 212 |

Numbers say: wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #11 Henry Ward purple spun balls — own sheet
own sheet 600 × 600 · Impasto 1.00 · 36 px · 3.6 s

![Brush Artist · Refs · #11 Henry Ward purple spun balls — own sheet](Brush-Artist-Refs-11-Henry-Ward-purple-spun-balls-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 24 % → 34 % | 26.4 px | 0.68 | 1.41 | 305 |
| stroke 2 | 35 % → 45 % | 38.0 px | 0.68 | 1.31 | 298 |
| stroke 3 | 35 % → 34 % | 39.0 px | 0.68 | 0.96 | 319 |

## Brush Artist · Refs · #12 Henry Ward black-olive cage — own sheet
own sheet 600 × 600 · Gouache 1.00 · 28 px · 6.9 s

![Brush Artist · Refs · #12 Henry Ward black-olive cage — own sheet](Brush-Artist-Refs-12-Henry-Ward-black-olive-cage-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 8 % → 9 % | 14.8 px | 0.59 | 1.19 | 275 |
| stroke 2 | 8 % → 11 % | 18.8 px | 0.59 | 1.36 | 215 |
| stroke 3 | 17 % → 14 % | 26.6 px | 0.59 | 0.84 | 262 |
| stroke 4 | 17 % → 12 % | 34.7 px | 0.59 | 0.66 | 160 |
| stroke 5 | 16 % → 9 % | 30.1 px | 0.59 | 0.53 | 162 |
| stroke 6 | 26 % → 13 % | 50.0 px | 0.59 | 0.48 | 217 |

## Brush Artist · Refs · #13 Henry Ward blue streaky form — own sheet
own sheet 600 × 600 · Gouache 1.00 · 50 px · 16.1 s

![Brush Artist · Refs · #13 Henry Ward blue streaky form — own sheet](Brush-Artist-Refs-13-Henry-Ward-blue-streaky-form-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 9 % → 2 % | 26.6 px | 0.03 | 0.26 | 252 |
| stroke 2 | 13 % → 2 % | 38.6 px | 0.03 | 0.17 | 259 |
| stroke 3 | 21 % → 2 % | 60.7 px | 0.03 | 0.11 | 285 |
| stroke 4 | 23 % → 2 % | 75.5 px | 0.03 | 0.09 | 233 |
| stroke 5 | 33 % → 2 % | 94.8 px | 0.03 | 0.07 | 270 |
| stroke 6 | 35 % → 2 % | 100.0 px | 0.03 | 0.06 | 274 |
| stroke 7 | 36 % → 3 % | 106.9 px | 0.04 | 0.08 | 264 |
| stroke 8 | 39 % → 2 % | 117.8 px | 0.04 | 0.06 | 270 |
| stroke 9 | 36 % → 2 % | 111.1 px | 0.04 | 0.06 | 252 |
| stroke 10 | 37 % → 2 % | 121.1 px | 0.04 | 0.06 | 250 |
| stroke 11 | 35 % → 1 % | 108.4 px | 0.04 | 0.04 | 257 |
| stroke 12 | 36 % → 1 % | 106.5 px | 0.04 | 0.04 | 316 |
| stroke 13 | 35 % → 2 % | 108.2 px | 0.04 | 0.06 | 245 |
| stroke 14 | 34 % → 2 % | 101.1 px | 0.04 | 0.06 | 285 |
| stroke 15 | 33 % → 2 % | 94.0 px | 0.04 | 0.07 | 263 |
| stroke 16 | 37 % → 2 % | 109.2 px | 0.04 | 0.06 | 259 |
| stroke 17 | 43 % → 2 % | 106.3 px | 0.04 | 0.04 | 266 |
| stroke 18 | 47 % → 2 % | 114.1 px | 0.04 | 0.03 | 287 |
| stroke 19 | 50 % → 2 % | 101.3 px | 0.04 | 0.04 | 296 |
| stroke 20 | 56 % → 2 % | 107.5 px | 0.04 | 0.03 | 314 |
| stroke 21 | 4 % → 1 % | 7.9 px | 0.04 | 0.34 | 524 |
| stroke 22 | 3 % → 2 % | 7.8 px | 0.03 | 0.77 | 260 |
| stroke 23 | 5 % → 2 % | 14.6 px | 0.03 | 0.46 | 304 |
| stroke 24 | 4 % → 1 % | 9.9 px | 0.04 | 0.40 | 201 |
| stroke 25 | 4 % → 2 % | 11.5 px | 0.04 | 0.52 | 193 |

## Brush Artist · Refs · #14 Henry Ward olive totem — own sheet
own sheet 600 × 600 · Impasto 1.00 · 48 px · 9.1 s

![Brush Artist · Refs · #14 Henry Ward olive totem — own sheet](Brush-Artist-Refs-14-Henry-Ward-olive-totem-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 18 % → 46 % | 45.8 px | 0.37 | 2.63 | 189 |
| stroke 2 | 21 % → 50 % | 64.3 px | 0.37 | 2.44 | 181 |
| stroke 3 | 29 % → 52 % | 100.3 px | 0.37 | 1.78 | 176 |
| stroke 4 | 30 % → 54 % | 112.7 px | 0.37 | 1.81 | 168 |
| stroke 5 | 39 % → 63 % | 134.6 px | 0.37 | 1.64 | 165 |
| stroke 6 | 39 % → 65 % | 150.1 px | 0.37 | 1.68 | 161 |
| stroke 7 | 37 % → 61 % | 123.6 px | 0.37 | 1.67 | 166 |
| stroke 8 | 37 % → 63 % | 141.6 px | 0.37 | 1.70 | 162 |
| stroke 9 | 37 % → 63 % | 129.7 px | 0.37 | 1.68 | 165 |
| stroke 10 | 38 % → 62 % | 140.9 px | 0.37 | 1.62 | 175 |
| stroke 11 | 40 % → 65 % | 143.5 px | 0.37 | 1.61 | 174 |
| stroke 12 | 38 % → 65 % | 143.4 px | 0.37 | 1.71 | 170 |
| stroke 13 | 38 % → 66 % | 134.6 px | 0.37 | 1.74 | 160 |
| stroke 14 | 37 % → 62 % | 134.4 px | 0.37 | 1.69 | 193 |
| stroke 15 | 40 % → 66 % | 136.6 px | 0.37 | 1.65 | 178 |
| stroke 16 | 38 % → 63 % | 137.8 px | 0.37 | 1.67 | 186 |
| stroke 17 | 37 % → 62 % | 125.2 px | 0.37 | 1.66 | 165 |
| stroke 18 | 40 % → 66 % | 154.7 px | 0.37 | 1.64 | 193 |
| stroke 19 | 40 % → 60 % | 137.7 px | 0.37 | 1.52 | 196 |
| stroke 20 | 40 % → 55 % | 143.4 px | 0.37 | 1.35 | 188 |
| stroke 21 | 46 % → 55 % | 136.7 px | 0.37 | 1.18 | 177 |
| stroke 22 | 54 % → 53 % | 146.5 px | 0.37 | 0.99 | 162 |

Numbers say: wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #15 Ultramarine brush script — own sheet
own sheet 600 × 600 · Ink 1.00 · 4 px · 12.1 s

![Brush Artist · Refs · #15 Ultramarine brush script — own sheet](Brush-Artist-Refs-15-Ultramarine-brush-script-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 40 % → 42 % | 8.9 px | 0.66 | 1.05 | 62 |
| stroke 2 | 40 % → 42 % | 8.9 px | 0.66 | 1.06 | 74 |
| stroke 3 | 40 % → 42 % | 9.5 px | 0.74 | 1.06 | 32 |
| stroke 4 | 42 % → 45 % | 10.1 px | 0.74 | 1.09 | 28 |
| stroke 5 | 44 % → 48 % | 9.7 px | 0.73 | 1.09 | 34 |
| stroke 6 | 42 % → 44 % | 9.5 px | 0.65 | 1.05 | 70 |
| stroke 7 | 43 % → 47 % | 9.2 px | 0.72 | 1.08 | 46 |
| stroke 8 | 38 % → 41 % | 9.3 px | 0.68 | 1.05 | 58 |
| stroke 9 | 40 % → 42 % | 9.2 px | 0.69 | 1.06 | 64 |
| stroke 10 | 36 % → 38 % | 9.9 px | 0.68 | 1.05 | 59 |
| stroke 11 | 42 % → 45 % | 9.6 px | 0.70 | 1.06 | 49 |
| stroke 12 | 39 % → 41 % | 9.4 px | 0.66 | 1.06 | 71 |
| stroke 13 | 45 % → 48 % | 10.2 px | 0.71 | 1.06 | 55 |
| stroke 14 | 38 % → 41 % | 9.8 px | 0.72 | 1.07 | 40 |
| stroke 15 | 37 % → 39 % | 9.1 px | 0.69 | 1.06 | 56 |
| stroke 16 | 42 % → 45 % | 9.4 px | 0.72 | 1.06 | 38 |
| stroke 17 | 41 % → 44 % | 7.1 px | 0.71 | 1.08 | 60 |
| stroke 18 | 43 % → 45 % | 9.2 px | 0.73 | 1.06 | 35 |
| stroke 19 | 39 % → 41 % | 8.9 px | 0.66 | 1.05 | 77 |
| stroke 20 | 41 % → 43 % | 9.4 px | 0.71 | 1.06 | 47 |
| stroke 21 | 41 % → 43 % | 9.9 px | 0.70 | 1.06 | 42 |
| stroke 22 | 42 % → 45 % | 8.5 px | 0.65 | 1.06 | 81 |
| stroke 23 | 40 % → 43 % | 10.1 px | 0.73 | 1.08 | 31 |
| stroke 24 | 38 % → 41 % | 8.8 px | 0.73 | 1.07 | 37 |
| stroke 25 | 41 % → 43 % | 9.8 px | 0.72 | 1.07 | 35 |
| stroke 26 | 46 % → 49 % | 9.3 px | 0.68 | 1.05 | 65 |
| stroke 27 | 43 % → 45 % | 8.8 px | 0.63 | 1.05 | 83 |
| stroke 28 | 44 % → 46 % | 9.1 px | 0.70 | 1.06 | 56 |
| stroke 29 | 36 % → 39 % | 10.6 px | 0.72 | 1.08 | 39 |
| stroke 30 | 39 % → 41 % | 8.7 px | 0.71 | 1.04 | 56 |
| stroke 31 | 43 % → 46 % | 10.3 px | 0.75 | 1.08 | 30 |
| stroke 32 | 42 % → 46 % | 9.5 px | 0.73 | 1.09 | 39 |
| stroke 33 | 35 % → 38 % | 10.9 px | 0.72 | 1.08 | 27 |
| stroke 34 | 40 % → 43 % | 9.8 px | 0.73 | 1.08 | 27 |
| stroke 35 | 36 % → 37 % | 9.4 px | 0.65 | 1.05 | 63 |

## Brush Artist · Refs · #18 Blue oil-stick scribbles — own sheet
own sheet 600 × 600 · Pastel 1.00 · 10 px · 4.3 s

![Brush Artist · Refs · #18 Blue oil-stick scribbles — own sheet](Brush-Artist-Refs-18-Blue-oil-stick-scribbles-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 15 % → 31 % | 3.8 px | 0.49 | 2.11 | 193 |
| stroke 2 | 13 % → 37 % | 3.6 px | 0.49 | 2.73 | 224 |
| stroke 3 | 16 % → 26 % | 5.8 px | 0.49 | 1.66 | 249 |
| stroke 4 | 15 % → 29 % | 8.0 px | 0.49 | 1.88 | 267 |
| stroke 5 | 29 % → 34 % | 8.4 px | 0.49 | 1.19 | 246 |
| stroke 6 | 25 % → 26 % | 9.4 px | 0.49 | 1.02 | 200 |
| stroke 7 | 26 % → 32 % | 8.3 px | 0.49 | 1.24 | 240 |
| stroke 8 | 30 % → 30 % | 17.0 px | 0.49 | 1.00 | 250 |

Numbers say: wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #20 Orange-red crayon scribble — own sheet
own sheet 600 × 600 · Pastel 1.00 · 14 px · 3.9 s

![Brush Artist · Refs · #20 Orange-red crayon scribble — own sheet](Brush-Artist-Refs-20-Orange-red-crayon-scribble-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 8 % → 18 % | 5.5 px | 0.59 | 2.46 | 266 |
| stroke 2 | 9 % → 23 % | 6.8 px | 0.59 | 2.48 | 212 |
| stroke 3 | 13 % → 21 % | 8.5 px | 0.59 | 1.64 | 245 |
| stroke 4 | 24 % → 32 % | 8.9 px | 0.59 | 1.34 | 276 |
| stroke 5 | 27 % → 27 % | 7.7 px | 0.59 | 1.00 | 232 |
| stroke 6 | 22 % → 22 % | 16.8 px | 0.59 | 1.00 | 247 |

Numbers say: wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #21 Gritty black contours — own sheet
own sheet 600 × 600 · Gouache 1.00 · 12 px · 5.9 s

![Brush Artist · Refs · #21 Gritty black contours — own sheet](Brush-Artist-Refs-21-Gritty-black-contours-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 4 % → 3 % | 4.9 px | 0.37 | 0.70 | 189 |
| stroke 2 | 5 % → 2 % | 7.6 px | 0.37 | 0.43 | 240 |
| stroke 3 | 7 % → 2 % | 5.9 px | 0.37 | 0.26 | 149 |
| stroke 4 | 8 % → 3 % | 9.8 px | 0.37 | 0.40 | 161 |
| stroke 5 | 10 % → 3 % | 11.9 px | 0.37 | 0.34 | 108 |

## Brush Artist · Refs · #22 Bold black brush poster — own sheet
own sheet 600 × 600 · Ink 1.00 · 20 px · 7.5 s

![Brush Artist · Refs · #22 Bold black brush poster — own sheet](Brush-Artist-Refs-22-Bold-black-brush-poster-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 22 % → 27 % | 36.3 px | 0.94 | 1.20 | 138 |
| stroke 2 | 27 % → 37 % | 41.4 px | 0.94 | 1.37 | 33 |
| stroke 3 | 28 % → 29 % | 43.6 px | 0.94 | 1.00 | 61 |
| stroke 4 | 27 % → 39 % | 53.7 px | 0.94 | 1.43 | 95 |
| stroke 5 | 25 % → 25 % | 42.9 px | 0.94 | 1.00 | 113 |

## Brush Artist · Refs · #23 Dry white on orange + black line — own sheet
own sheet 600 × 600 · Gouache 1.00 · 50 px · 10.6 s

![Brush Artist · Refs · #23 Dry white on orange + black line — own sheet](Brush-Artist-Refs-23-Dry-white-on-orange-black-line-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 6 % → 11 % | 22.3 px | 0.40 | 1.71 | 188 |
| stroke 2 | 9 % → 10 % | 31.8 px | 0.40 | 1.10 | 207 |
| stroke 3 | 13 % → 11 % | 48.0 px | 0.40 | 0.82 | 181 |
| stroke 4 | 15 % → 12 % | 59.0 px | 0.40 | 0.80 | 179 |
| stroke 5 | 21 % → 14 % | 75.7 px | 0.40 | 0.67 | 193 |
| stroke 6 | 21 % → 16 % | 88.3 px | 0.40 | 0.77 | 201 |
| stroke 7 | 17 % → 15 % | 65.6 px | 0.39 | 0.87 | 169 |
| stroke 8 | 18 % → 14 % | 70.7 px | 0.39 | 0.79 | 234 |
| stroke 9 | 18 % → 15 % | 68.7 px | 0.39 | 0.83 | 228 |
| stroke 10 | 18 % → 15 % | 69.0 px | 0.39 | 0.87 | 222 |
| stroke 11 | 20 % → 17 % | 74.8 px | 0.39 | 0.85 | 228 |
| stroke 12 | 21 % → 17 % | 80.3 px | 0.39 | 0.81 | 193 |
| stroke 13 | 21 % → 19 % | 77.7 px | 0.39 | 0.89 | 243 |
| stroke 14 | 20 % → 19 % | 81.1 px | 0.39 | 0.91 | 265 |
| stroke 15 | 20 % → 16 % | 73.7 px | 0.39 | 0.80 | 180 |
| stroke 16 | 20 % → 14 % | 80.1 px | 0.39 | 0.70 | 249 |
| stroke 17 | 20 % → 13 % | 71.5 px | 0.39 | 0.61 | 193 |
| stroke 18 | 24 % → 13 % | 86.5 px | 0.39 | 0.55 | 192 |

Numbers say: wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #24 Picasso flat oil — own sheet
own sheet 600 × 600 · Oil 0.89 · Oil glaze 0.11 · 34 px · 7.5 s

![Brush Artist · Refs · #24 Picasso flat oil — own sheet](Brush-Artist-Refs-24-Picasso-flat-oil-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 14 % → 42 % | 29.4 px | 0.22 | 3.06 | 174 |
| stroke 2 | 18 % → 46 % | 41.9 px | 0.22 | 2.57 | 184 |
| stroke 3 | 26 % → 56 % | 57.4 px | 0.22 | 2.14 | 163 |
| stroke 4 | 35 % → 62 % | 77.7 px | 0.22 | 1.79 | 175 |
| stroke 5 | 40 % → 67 % | 89.3 px | 0.21 | 1.66 | 178 |
| stroke 6 | 41 % → 62 % | 96.0 px | 0.21 | 1.50 | 177 |
| stroke 7 | 41 % → 61 % | 87.0 px | 0.21 | 1.48 | 178 |
| stroke 8 | 41 % → 61 % | 99.6 px | 0.22 | 1.49 | 180 |
| stroke 9 | 34 % → 57 % | 73.4 px | 0.22 | 1.70 | 195 |
| stroke 10 | 35 % → 56 % | 84.6 px | 0.22 | 1.59 | 201 |
| stroke 11 | 33 % → 55 % | 70.2 px | 0.22 | 1.66 | 325 |
| stroke 12 | 35 % → 55 % | 82.8 px | 0.22 | 1.57 | 206 |
| stroke 13 | 34 % → 62 % | 74.8 px | 0.22 | 1.81 | 185 |
| stroke 14 | 36 % → 63 % | 80.8 px | 0.22 | 1.78 | 390 |
| stroke 15 | 34 % → 57 % | 71.9 px | 0.21 | 1.67 | 160 |
| stroke 16 | 34 % → 50 % | 78.6 px | 0.21 | 1.46 | 379 |
| stroke 17 | 39 % → 44 % | 81.0 px | 0.21 | 1.14 | 220 |
| stroke 18 | 39 % → 39 % | 93.8 px | 0.21 | 1.00 | 172 |

Numbers say: wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #25 Yellow heavy flat stroke — own sheet
own sheet 600 × 600 · Impasto 1.00 · 110 px · 4.7 s

![Brush Artist · Refs · #25 Yellow heavy flat stroke — own sheet](Brush-Artist-Refs-25-Yellow-heavy-flat-stroke-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 18 % → 18 % | 104.3 px | 0.17 | 0.98 | 962 |

## Brush Artist · Refs · #27 Orange impasto swatch — own sheet
own sheet 600 × 600 · Impasto 1.00 · 60 px · 4.5 s

![Brush Artist · Refs · #27 Orange impasto swatch — own sheet](Brush-Artist-Refs-27-Orange-impasto-swatch-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 8 % → 21 % | 61.8 px | 0.33 | 2.60 | 106 |
| stroke 2 | 7 % → 33 % | 62.6 px | 0.33 | 4.67 | 102 |
| stroke 3 | 25 % → 36 % | 245.8 px | 0.33 | 1.40 | 72 |
| stroke 4 | 10 % → 12 % | 69.8 px | 0.33 | 1.25 | 121 |
| stroke 5 | 17 % → 33 % | 63.5 px | 0.33 | 1.90 | 91 |
| stroke 6 | 18 % → 32 % | 145.3 px | 0.33 | 1.79 | 79 |
| stroke 7 | 8 % → 15 % | 70.4 px | 0.33 | 1.87 | 67 |
| stroke 8 | 33 % → 34 % | 337.7 px | 0.33 | 1.04 | 66 |
| stroke 9 | 38 % → 37 % | 185.5 px | 0.33 | 0.98 | 160 |
| stroke 10 | 34 % → 33 % | 305.4 px | 0.33 | 0.98 | 71 |

Numbers say: wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #28 Miles Davis black lines — own sheet
own sheet 600 × 600 · Ink 1.00 · 22 px · 7.0 s

![Brush Artist · Refs · #28 Miles Davis black lines — own sheet](Brush-Artist-Refs-28-Miles-Davis-black-lines-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 22 % → 32 % | 36.5 px | 0.88 | 1.42 | 232 |
| stroke 2 | 28 % → 49 % | 38.2 px | 0.88 | 1.73 | 185 |
| stroke 3 | 39 % → 44 % | 75.1 px | 0.88 | 1.12 | 138 |
| stroke 4 | 42 % → 48 % | 83.7 px | 0.88 | 1.15 | 221 |
| stroke 5 | 55 % → 55 % | 109.8 px | 0.88 | 1.00 | 165 |

Numbers say: wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #29 Shrigley magenta asterisk — own sheet
own sheet 600 × 600 · Watercolour 1.00 · 70 px · 6.8 s

![Brush Artist · Refs · #29 Shrigley magenta asterisk — own sheet](Brush-Artist-Refs-29-Shrigley-magenta-asterisk-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 13 % → 37 % | 46.6 px | 0.67 | 2.86 | 302 |
| stroke 2 | 12 % → 12 % | 87.1 px | 0.67 | 1.00 | 231 |
| stroke 3 | 28 % → 37 % | 100.9 px | 0.67 | 1.31 | 262 |
| stroke 4 | 23 % → 23 % | 164.0 px | 0.67 | 1.02 | 288 |

Numbers say: wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #30 Red gouache face patch — own sheet
own sheet 600 × 600 · Gouache 1.00 · 60 px · 12.2 s

![Brush Artist · Refs · #30 Red gouache face patch — own sheet](Brush-Artist-Refs-30-Red-gouache-face-patch-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 12 % → 37 % | 51.5 px | 0.54 | 3.23 | 207 |
| stroke 2 | 15 % → 40 % | 74.5 px | 0.54 | 2.72 | 222 |
| stroke 3 | 24 % → 50 % | 115.9 px | 0.54 | 2.06 | 218 |
| stroke 4 | 27 % → 52 % | 134.1 px | 0.54 | 1.94 | 231 |
| stroke 5 | 34 % → 60 % | 159.9 px | 0.54 | 1.77 | 256 |
| stroke 6 | 35 % → 61 % | 178.3 px | 0.54 | 1.76 | 321 |
| stroke 7 | 34 % → 59 % | 160.9 px | 0.54 | 1.73 | 193 |
| stroke 8 | 34 % → 56 % | 162.5 px | 0.54 | 1.66 | 208 |
| stroke 9 | 36 % → 60 % | 173.1 px | 0.54 | 1.66 | 150 |
| stroke 10 | 38 % → 62 % | 196.8 px | 0.54 | 1.64 | 175 |
| stroke 11 | 37 % → 61 % | 182.4 px | 0.54 | 1.66 | 168 |
| stroke 12 | 36 % → 58 % | 178.3 px | 0.54 | 1.62 | 180 |
| stroke 13 | 33 % → 46 % | 156.5 px | 0.54 | 1.39 | 159 |
| stroke 14 | 33 % → 41 % | 157.6 px | 0.54 | 1.25 | 228 |
| stroke 15 | 33 % → 37 % | 153.4 px | 0.54 | 1.12 | 186 |
| stroke 16 | 39 % → 39 % | 184.9 px | 0.54 | 0.99 | 167 |

Numbers say: wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #31 Warhol blotted line — own sheet
own sheet 600 × 600 · Ink 1.00 · 6 px · 5.2 s

![Brush Artist · Refs · #31 Warhol blotted line — own sheet](Brush-Artist-Refs-31-Warhol-blotted-line-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 21 % → 42 % | 15.8 px | 0.82 | 1.98 | 101 |
| stroke 2 | 17 % → 23 % | 15.9 px | 0.82 | 1.34 | 89 |
| stroke 3 | 24 % → 25 % | 25.1 px | 0.81 | 1.02 | 111 |
| stroke 4 | 31 % → 40 % | 31.8 px | 0.82 | 1.28 | 68 |
| stroke 5 | 35 % → 44 % | 36.4 px | 0.82 | 1.23 | 89 |
| stroke 6 | 32 % → 33 % | 26.7 px | 0.81 | 1.03 | 118 |

Numbers say: wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #32 Thick orange swipes — own sheet
own sheet 600 × 600 · Impasto 1.00 · 90 px · 4.0 s

![Brush Artist · Refs · #32 Thick orange swipes — own sheet](Brush-Artist-Refs-32-Thick-orange-swipes-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 14 % → 27 % | 86.1 px | 0.03 | 1.90 | 477 |
| stroke 2 | 26 % → 38 % | 177.0 px | 0.03 | 1.43 | 501 |
| stroke 3 | 28 % → 27 % | 177.6 px | 0.03 | 0.98 | 325 |

Numbers say: wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #33 Red wet-in-wet band — own sheet
own sheet 600 × 600 · Watercolour 1.00 · 80 px · 10.1 s

![Brush Artist · Refs · #33 Red wet-in-wet band — own sheet](Brush-Artist-Refs-33-Red-wet-in-wet-band-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 24 % → 59 % | 89.6 px | 0.61 | 2.52 | 587 |
| stroke 2 | 30 % → 53 % | 244.8 px | 0.62 | 1.76 | 132 |
| stroke 3 | 37 % → 55 % | 358.4 px | 0.61 | 1.49 | 133 |
| stroke 4 | 43 % → 62 % | 415.9 px | 0.62 | 1.44 | 98 |
| stroke 5 | 43 % → 57 % | 361.3 px | 0.61 | 1.33 | 127 |
| stroke 6 | 44 % → 49 % | 333.3 px | 0.60 | 1.13 | 135 |

Numbers say: wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #34 Magenta oil patches — own sheet
own sheet 600 × 600 · Oil 0.89 · Oil glaze 0.11 · 60 px · 3.6 s

![Brush Artist · Refs · #34 Magenta oil patches — own sheet](Brush-Artist-Refs-34-Magenta-oil-patches-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 8 % → 40 % | 58.6 px | 0.12 | 4.85 | 146 |
| stroke 2 | 9 % → 28 % | 59.5 px | 0.13 | 3.22 | 86 |
| stroke 3 | 7 % → 34 % | 59.0 px | 0.12 | 4.77 | 76 |
| stroke 4 | 15 % → 20 % | 125.3 px | 0.12 | 1.27 | 58 |
| stroke 5 | 22 % → 32 % | 118.3 px | 0.12 | 1.44 | 95 |
| stroke 6 | 19 % → 36 % | 164.2 px | 0.12 | 1.88 | 70 |
| stroke 7 | 28 % → 33 % | 224.7 px | 0.12 | 1.19 | 71 |
| stroke 8 | 32 % → 38 % | 223.8 px | 0.12 | 1.19 | 116 |
| stroke 9 | 24 % → 26 % | 155.3 px | 0.12 | 1.07 | 95 |
| stroke 10 | 28 % → 28 % | 246.0 px | 0.12 | 1.00 | 72 |
| stroke 11 | 35 % → 35 % | 309.4 px | 0.12 | 1.00 | 71 |
| stroke 12 | 25 % → 25 % | 177.1 px | 0.12 | 1.00 | 75 |

Numbers say: wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #35 Red band with runs — own sheet
own sheet 600 × 600 · Watercolour 1.00 · 70 px · 7.5 s

![Brush Artist · Refs · #35 Red band with runs — own sheet](Brush-Artist-Refs-35-Red-band-with-runs-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 37 % → 51 % | 138.9 px | 0.44 | 1.38 | 426 |

## Brush Artist · Refs · #36 Magenta letters flat brush — own sheet
own sheet 600 × 600 · Gouache 1.00 · 36 px · 11.3 s

![Brush Artist · Refs · #36 Magenta letters flat brush — own sheet](Brush-Artist-Refs-36-Magenta-letters-flat-brush-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 20 % → 39 % | 59.0 px | 0.50 | 1.95 | 31 |
| stroke 2 | 20 % → 32 % | 46.6 px | 0.50 | 1.59 | 28 |
| stroke 3 | 29 % → 54 % | 86.8 px | 0.50 | 1.86 | 35 |
| stroke 4 | 26 % → 44 % | 51.2 px | 0.50 | 1.67 | 99 |
| stroke 5 | 33 % → 55 % | 96.1 px | 0.50 | 1.67 | 68 |
| stroke 6 | 42 % → 56 % | 242.4 px | 0.50 | 1.33 | 19 |
| stroke 7 | 30 % → 44 % | 56.7 px | 0.50 | 1.45 | 112 |
| stroke 8 | 31 % → 53 % | 98.5 px | 0.50 | 1.68 | 75 |
| stroke 9 | 38 % → 51 % | 158.3 px | 0.50 | 1.33 | 27 |
| stroke 10 | 37 % → 63 % | 106.7 px | 0.50 | 1.72 | 73 |
| stroke 11 | 39 % → 62 % | 225.9 px | 0.50 | 1.58 | 17 |
| stroke 12 | 43 % → 56 % | 81.9 px | 0.50 | 1.29 | 125 |
| stroke 13 | 32 % → 46 % | 117.6 px | 0.50 | 1.43 | 31 |
| stroke 14 | 35 % → 52 % | 134.4 px | 0.50 | 1.47 | 27 |
| stroke 15 | 38 % → 56 % | 108.5 px | 0.50 | 1.49 | 68 |
| stroke 16 | 41 % → 50 % | 232.0 px | 0.50 | 1.23 | 22 |
| stroke 17 | 44 % → 52 % | 81.7 px | 0.50 | 1.19 | 130 |
| stroke 18 | 27 % → 36 % | 97.5 px | 0.50 | 1.35 | 37 |
| stroke 19 | 40 % → 39 % | 117.0 px | 0.50 | 0.96 | 34 |
| stroke 20 | 45 % → 45 % | 132.2 px | 0.50 | 0.99 | 41 |
| stroke 21 | 41 % → 39 % | 78.6 px | 0.50 | 0.96 | 92 |

Numbers say: wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #37 Oil still life dabs — own sheet
own sheet 600 × 600 · Oil 0.89 · Oil glaze 0.11 · 40 px · 2.6 s

![Brush Artist · Refs · #37 Oil still life dabs — own sheet](Brush-Artist-Refs-37-Oil-still-life-dabs-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 7 % → 7 % | 42.1 px | 0.38 | 1.00 | 28 |
| stroke 2 | 6 % → 27 % | 42.8 px | 0.38 | 4.44 | 16 |
| stroke 3 | 11 % → 34 % | 88.7 px | 0.38 | 3.01 | 17 |
| stroke 4 | 9 % → 9 % | 41.0 px | 0.38 | 1.00 | 33 |
| stroke 5 | 6 % → 10 % | 41.0 px | 0.38 | 1.73 | 23 |
| stroke 6 | 13 % → 30 % | 80.6 px | 0.38 | 2.32 | 25 |
| stroke 7 | 10 % → 23 % | 110.5 px | 0.38 | 2.21 | 9 |
| stroke 8 | 8 % → 13 % | 86.6 px | 0.38 | 1.62 | 20 |
| stroke 9 | 12 % → 13 % | 65.1 px | 0.37 | 1.08 | 34 |
| stroke 10 | 20 % → 24 % | 102.6 px | 0.38 | 1.20 | 42 |
| stroke 11 | 24 % → 27 % | 195.5 px | 0.39 | 1.17 | 16 |
| stroke 12 | 20 % → 21 % | 220.2 px | 0.39 | 1.01 | 9 |
| stroke 13 | 16 % → 16 % | 162.7 px | 0.39 | 1.00 | 14 |
| stroke 14 | 16 % → 16 % | 127.3 px | 0.38 | 1.00 | 17 |

Numbers say: wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #38 Sanguine drawing — own sheet
own sheet 600 × 600 · Pastel 1.00 · 6 px · 2.2 s

![Brush Artist · Refs · #38 Sanguine drawing — own sheet](Brush-Artist-Refs-38-Sanguine-drawing-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 3 % → 14 % | 2.9 px | 0.57 | 5.30 | 4 |
| stroke 2 | 3 % → 7 % | 2.9 px | 0.58 | 2.89 | 5 |
| stroke 3 | 3 % → 9 % | 2.9 px | 0.57 | 3.40 | 6 |
| stroke 4 | 2 % → 17 % | 2.7 px | 0.57 | 7.20 | 7 |
| stroke 5 | 2 % → 7 % | 2.7 px | 0.57 | 3.03 | 5 |
| stroke 6 | 3 % → 19 % | 3.4 px | 0.57 | 6.31 | 7 |
| stroke 7 | 5 % → 14 % | 5.2 px | 0.57 | 3.07 | 4 |
| stroke 8 | 4 % → 16 % | 4.7 px | 0.57 | 3.79 | 4 |
| stroke 9 | 3 % → 7 % | 2.9 px | 0.57 | 2.66 | 4 |
| stroke 10 | 4 % → 16 % | 4.7 px | 0.57 | 3.83 | 8 |
| stroke 11 | 3 % → 4 % | 2.9 px | 0.57 | 1.61 | 8 |
| stroke 12 | 4 % → 15 % | 4.8 px | 0.57 | 3.58 | 8 |
| stroke 13 | 8 % → 17 % | 8.9 px | 0.57 | 2.23 | 5 |
| stroke 14 | 4 % → 14 % | 4.9 px | 0.57 | 3.19 | 4 |
| stroke 15 | 9 % → 18 % | 10.7 px | 0.57 | 1.86 | 4 |
| stroke 16 | 6 % → 16 % | 6.6 px | 0.57 | 2.71 | 14 |
| stroke 17 | 4 % → 9 % | 4.4 px | 0.57 | 2.25 | 7 |
| stroke 18 | 3 % → 5 % | 2.9 px | 0.57 | 1.85 | 4 |
| stroke 19 | 6 % → 16 % | 6.9 px | 0.57 | 2.68 | 8 |
| stroke 20 | 8 % → 14 % | 9.2 px | 0.57 | 1.70 | 6 |
| stroke 21 | 4 % → 4 % | 4.3 px | 0.57 | 1.00 | 7 |
| stroke 22 | 8 % → 13 % | 8.6 px | 0.57 | 1.79 | 4 |
| stroke 23 | 7 % → 12 % | 8.3 px | 0.57 | 1.61 | 7 |
| stroke 24 | 4 % → 7 % | 4.7 px | 0.57 | 1.71 | 3 |
| stroke 25 | 8 % → 14 % | 8.7 px | 0.57 | 1.84 | 7 |
| stroke 26 | 6 % → 8 % | 6.5 px | 0.57 | 1.34 | 7 |
| stroke 27 | 4 % → 4 % | 4.3 px | 0.57 | 1.10 | 7 |
| stroke 28 | 7 % → 11 % | 8.2 px | 0.57 | 1.59 | 6 |
| stroke 29 | 8 % → 17 % | 8.8 px | 0.57 | 2.21 | 4 |
| stroke 30 | 13 % → 17 % | 14.9 px | 0.57 | 1.29 | 4 |
| stroke 31 | 5 % → 6 % | 5.4 px | 0.57 | 1.29 | 6 |
| stroke 32 | 10 % → 13 % | 11.8 px | 0.57 | 1.24 | 6 |
| stroke 33 | 7 % → 8 % | 8.5 px | 0.57 | 1.07 | 4 |
| stroke 34 | 11 % → 14 % | 12.0 px | 0.57 | 1.36 | 5 |
| stroke 35 | 9 % → 14 % | 10.0 px | 0.57 | 1.61 | 4 |
| stroke 36 | 10 % → 13 % | 11.4 px | 0.57 | 1.26 | 6 |
| stroke 37 | 9 % → 16 % | 10.5 px | 0.57 | 1.71 | 4 |
| stroke 38 | 13 % → 19 % | 14.8 px | 0.57 | 1.48 | 7 |
| stroke 39 | 14 % → 17 % | 15.7 px | 0.57 | 1.21 | 4 |
| stroke 40 | 6 % → 7 % | 7.2 px | 0.57 | 1.14 | 5 |
| stroke 41 | 16 % → 16 % | 17.7 px | 0.57 | 1.01 | 4 |
| stroke 42 | 14 % → 16 % | 15.2 px | 0.57 | 1.17 | 7 |
| stroke 43 | 10 % → 12 % | 11.6 px | 0.57 | 1.17 | 4 |
| stroke 44 | 12 % → 15 % | 14.3 px | 0.57 | 1.22 | 6 |
| stroke 45 | 2 % → 2 % | 2.7 px | 0.57 | 1.00 | 4 |
| stroke 46 | 16 % → 16 % | 18.5 px | 0.57 | 1.00 | 5 |
| stroke 47 | 13 % → 13 % | 15.0 px | 0.57 | 1.00 | 5 |
| stroke 48 | 12 % → 13 % | 14.3 px | 0.57 | 1.07 | 4 |
| stroke 49 | 19 % → 19 % | 21.5 px | 0.57 | 1.00 | 7 |
| stroke 50 | 10 % → 10 % | 11.6 px | 0.57 | 1.00 | 5 |

Numbers say: wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #39 Very thick impasto — own sheet
own sheet 600 × 600 · Impasto 1.00 · 60 px · 4.7 s

![Brush Artist · Refs · #39 Very thick impasto — own sheet](Brush-Artist-Refs-39-Very-thick-impasto-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 26 % → 37 % | 59.6 px | 0.43 | 1.42 | 267 |
| stroke 2 | 31 % → 48 % | 93.9 px | 0.44 | 1.54 | 298 |
| stroke 3 | 37 % → 49 % | 124.6 px | 0.43 | 1.33 | 273 |
| stroke 4 | 31 % → 44 % | 90.9 px | 0.44 | 1.41 | 274 |
| stroke 5 | 42 % → 41 % | 104.2 px | 0.44 | 0.98 | 285 |

Numbers say: wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #40 Watercolour blooms — own sheet
own sheet 600 × 600 · Watercolour 1.00 · 90 px · 8.1 s

![Brush Artist · Refs · #40 Watercolour blooms — own sheet](Brush-Artist-Refs-40-Watercolour-blooms-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 22 % → 28 % | 95.0 px | 0.12 | 1.31 | 811 |

## Brush Artist · Refs · #41 Coloured pencil hatching — own sheet
own sheet 600 × 600 · Pastel 1.00 · 4 px · 2.9 s

![Brush Artist · Refs · #41 Coloured pencil hatching — own sheet](Brush-Artist-Refs-41-Coloured-pencil-hatching-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 3 % → 13 % | 2.2 px | 0.35 | 4.64 | 6 |
| stroke 2 | 3 % → 7 % | 2.3 px | 0.35 | 2.29 | 4 |
| stroke 3 | 2 % → 11 % | 1.9 px | 0.35 | 4.38 | 4 |
| stroke 4 | 3 % → 19 % | 2.1 px | 0.35 | 6.73 | 3 |
| stroke 5 | 4 % → 7 % | 2.9 px | 0.35 | 1.83 | 7 |
| stroke 6 | 3 % → 13 % | 2.3 px | 0.35 | 4.19 | 9 |
| stroke 7 | 3 % → 15 % | 2.6 px | 0.35 | 4.43 | 5 |
| stroke 8 | 3 % → 12 % | 2.1 px | 0.35 | 4.20 | 7 |
| stroke 9 | 5 % → 11 % | 3.6 px | 0.35 | 2.27 | 4 |
| stroke 10 | 5 % → 15 % | 3.8 px | 0.35 | 2.99 | 6 |
| stroke 11 | 4 % → 13 % | 3.0 px | 0.35 | 3.28 | 4 |
| stroke 12 | 3 % → 3 % | 2.1 px | 0.35 | 1.00 | 5 |
| stroke 13 | 7 % → 17 % | 5.2 px | 0.35 | 2.45 | 3 |
| stroke 14 | 3 % → 13 % | 2.4 px | 0.35 | 4.19 | 3 |
| stroke 15 | 6 % → 12 % | 4.4 px | 0.35 | 2.09 | 4 |
| stroke 16 | 7 % → 11 % | 5.1 px | 0.35 | 1.61 | 5 |
| stroke 17 | 3 % → 3 % | 2.1 px | 0.35 | 1.00 | 5 |
| stroke 18 | 5 % → 8 % | 3.6 px | 0.35 | 1.65 | 3 |
| stroke 19 | 5 % → 13 % | 3.8 px | 0.35 | 2.72 | 6 |
| stroke 20 | 5 % → 14 % | 3.7 px | 0.35 | 2.92 | 7 |
| stroke 21 | 4 % → 13 % | 3.2 px | 0.35 | 3.20 | 6 |
| stroke 22 | 9 % → 16 % | 6.8 px | 0.35 | 1.77 | 5 |
| stroke 23 | 9 % → 13 % | 6.5 px | 0.35 | 1.55 | 3 |
| stroke 24 | 6 % → 14 % | 4.7 px | 0.35 | 2.18 | 5 |
| stroke 25 | 5 % → 10 % | 3.5 px | 0.35 | 2.27 | 3 |
| stroke 26 | 3 % → 6 % | 2.7 px | 0.35 | 1.81 | 5 |
| stroke 27 | 3 % → 7 % | 2.3 px | 0.35 | 2.26 | 5 |
| stroke 28 | 6 % → 10 % | 4.5 px | 0.35 | 1.70 | 5 |
| stroke 29 | 3 % → 13 % | 2.4 px | 0.35 | 4.21 | 5 |
| stroke 30 | 6 % → 9 % | 4.4 px | 0.35 | 1.46 | 3 |
| stroke 31 | 7 % → 14 % | 5.1 px | 0.35 | 2.14 | 3 |
| stroke 32 | 3 % → 6 % | 2.5 px | 0.35 | 1.78 | 5 |
| stroke 33 | 6 % → 11 % | 5.0 px | 0.35 | 1.67 | 3 |
| stroke 34 | 3 % → 6 % | 2.6 px | 0.35 | 1.73 | 5 |
| stroke 35 | 7 % → 14 % | 5.0 px | 0.35 | 2.09 | 3 |
| stroke 36 | 5 % → 5 % | 3.7 px | 0.35 | 1.01 | 4 |
| stroke 37 | 7 % → 15 % | 5.2 px | 0.35 | 2.15 | 3 |
| stroke 38 | 8 % → 13 % | 5.8 px | 0.35 | 1.66 | 5 |
| stroke 39 | 7 % → 11 % | 5.1 px | 0.35 | 1.67 | 3 |
| stroke 40 | 8 % → 18 % | 6.2 px | 0.35 | 2.21 | 5 |
| stroke 41 | 9 % → 13 % | 6.9 px | 0.35 | 1.48 | 3 |
| stroke 42 | 10 % → 17 % | 7.7 px | 0.35 | 1.73 | 5 |
| stroke 43 | 5 % → 9 % | 3.9 px | 0.35 | 1.66 | 4 |
| stroke 44 | 10 % → 13 % | 7.3 px | 0.35 | 1.40 | 5 |
| stroke 45 | 13 % → 18 % | 9.9 px | 0.35 | 1.35 | 6 |
| stroke 46 | 5 % → 7 % | 3.6 px | 0.34 | 1.41 | 2 |
| stroke 47 | 11 % → 13 % | 8.0 px | 0.35 | 1.20 | 3 |
| stroke 48 | 12 % → 16 % | 9.2 px | 0.35 | 1.34 | 3 |
| stroke 49 | 6 % → 9 % | 4.2 px | 0.35 | 1.65 | 8 |
| stroke 50 | 7 % → 7 % | 5.2 px | 0.34 | 1.00 | 4 |
| stroke 51 | 8 % → 15 % | 6.4 px | 0.35 | 1.74 | 4 |
| stroke 52 | 12 % → 14 % | 9.1 px | 0.35 | 1.19 | 5 |
| stroke 53 | 11 % → 14 % | 8.1 px | 0.35 | 1.36 | 5 |
| stroke 54 | 10 % → 14 % | 7.4 px | 0.35 | 1.47 | 3 |
| stroke 55 | 11 % → 14 % | 8.2 px | 0.35 | 1.33 | 7 |
| stroke 56 | 11 % → 12 % | 8.4 px | 0.35 | 1.11 | 6 |
| stroke 57 | 9 % → 13 % | 7.1 px | 0.35 | 1.37 | 3 |
| stroke 58 | 10 % → 11 % | 7.7 px | 0.35 | 1.14 | 2 |
| stroke 59 | 11 % → 13 % | 8.4 px | 0.35 | 1.18 | 3 |
| stroke 60 | 16 % → 20 % | 11.9 px | 0.35 | 1.26 | 3 |
| stroke 61 | 19 % → 20 % | 14.5 px | 0.35 | 1.04 | 4 |
| stroke 62 | 10 % → 10 % | 7.3 px | 0.35 | 1.00 | 6 |
| stroke 63 | 11 % → 12 % | 8.7 px | 0.35 | 1.07 | 7 |
| stroke 64 | 14 % → 14 % | 10.7 px | 0.35 | 1.02 | 4 |
| stroke 65 | 15 % → 15 % | 11.5 px | 0.35 | 1.00 | 5 |
| stroke 66 | 14 % → 14 % | 10.7 px | 0.35 | 1.00 | 5 |
| stroke 67 | 12 % → 12 % | 8.8 px | 0.35 | 1.06 | 3 |
| stroke 68 | 5 % → 9 % | 3.6 px | 0.35 | 1.88 | 3 |
| stroke 69 | 5 % → 5 % | 4.1 px | 0.35 | 1.00 | 5 |
| stroke 70 | 10 % → 13 % | 7.4 px | 0.35 | 1.28 | 4 |
| stroke 71 | 9 % → 11 % | 7.1 px | 0.35 | 1.15 | 3 |
| stroke 72 | 5 % → 7 % | 4.2 px | 0.35 | 1.23 | 5 |
| stroke 73 | 12 % → 12 % | 9.3 px | 0.35 | 1.00 | 3 |
| stroke 74 | 14 % → 14 % | 10.8 px | 0.35 | 1.00 | 5 |
| stroke 75 | 15 % → 15 % | 11.4 px | 0.35 | 1.00 | 3 |
| stroke 76 | 14 % → 14 % | 10.5 px | 0.35 | 1.00 | 3 |
| stroke 77 | 7 % → 10 % | 5.4 px | 0.35 | 1.34 | 3 |
| stroke 78 | 9 % → 9 % | 7.0 px | 0.35 | 1.00 | 6 |
| stroke 79 | 7 % → 7 % | 5.7 px | 0.35 | 1.00 | 5 |
| stroke 80 | 11 % → 11 % | 8.3 px | 0.35 | 1.00 | 6 |

Numbers say: wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #42 Oil pastel shaggy — own sheet
own sheet 600 × 600 · Pastel 1.00 · 18 px · 2.9 s

![Brush Artist · Refs · #42 Oil pastel shaggy — own sheet](Brush-Artist-Refs-42-Oil-pastel-shaggy-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 5 % → 27 % | 8.0 px | 0.28 | 5.73 | 13 |
| stroke 2 | 5 % → 24 % | 8.6 px | 0.28 | 4.69 | 15 |
| stroke 3 | 5 % → 29 % | 8.9 px | 0.28 | 5.42 | 11 |
| stroke 4 | 5 % → 11 % | 8.8 px | 0.28 | 2.08 | 6 |
| stroke 5 | 6 % → 11 % | 9.9 px | 0.28 | 1.85 | 14 |
| stroke 6 | 8 % → 37 % | 13.9 px | 0.29 | 4.44 | 8 |
| stroke 7 | 11 % → 31 % | 17.6 px | 0.28 | 2.90 | 7 |
| stroke 8 | 7 % → 38 % | 11.4 px | 0.28 | 5.55 | 8 |
| stroke 9 | 8 % → 21 % | 13.9 px | 0.28 | 2.53 | 11 |
| stroke 10 | 8 % → 18 % | 13.2 px | 0.28 | 2.32 | 10 |
| stroke 11 | 6 % → 27 % | 9.4 px | 0.28 | 4.74 | 7 |
| stroke 12 | 8 % → 19 % | 13.6 px | 0.28 | 2.29 | 6 |
| stroke 13 | 13 % → 24 % | 21.0 px | 0.28 | 1.92 | 12 |
| stroke 14 | 5 % → 23 % | 7.9 px | 0.28 | 4.77 | 6 |
| stroke 15 | 5 % → 24 % | 9.0 px | 0.29 | 4.38 | 10 |
| stroke 16 | 9 % → 21 % | 15.7 px | 0.29 | 2.18 | 10 |
| stroke 17 | 17 % → 39 % | 28.0 px | 0.29 | 2.34 | 9 |
| stroke 18 | 14 % → 25 % | 22.8 px | 0.29 | 1.79 | 11 |
| stroke 19 | 15 % → 32 % | 24.9 px | 0.28 | 2.09 | 6 |
| stroke 20 | 21 % → 39 % | 35.1 px | 0.28 | 1.85 | 8 |
| stroke 21 | 9 % → 16 % | 14.4 px | 0.28 | 1.88 | 12 |
| stroke 22 | 14 % → 17 % | 23.9 px | 0.28 | 1.20 | 6 |
| stroke 23 | 12 % → 17 % | 20.6 px | 0.29 | 1.34 | 6 |
| stroke 24 | 18 % → 26 % | 30.0 px | 0.29 | 1.44 | 11 |
| stroke 25 | 20 % → 34 % | 32.6 px | 0.28 | 1.74 | 6 |
| stroke 26 | 6 % → 14 % | 9.2 px | 0.28 | 2.43 | 12 |
| stroke 27 | 18 % → 26 % | 30.5 px | 0.29 | 1.41 | 12 |
| stroke 28 | 14 % → 24 % | 23.7 px | 0.28 | 1.68 | 9 |
| stroke 29 | 9 % → 27 % | 14.9 px | 0.29 | 3.01 | 9 |
| stroke 30 | 15 % → 36 % | 25.0 px | 0.29 | 2.43 | 12 |
| stroke 31 | 14 % → 17 % | 23.3 px | 0.28 | 1.23 | 13 |
| stroke 32 | 16 % → 29 % | 27.0 px | 0.29 | 1.82 | 10 |
| stroke 33 | 15 % → 16 % | 24.5 px | 0.29 | 1.09 | 15 |
| stroke 34 | 19 % → 27 % | 31.4 px | 0.28 | 1.44 | 12 |
| stroke 35 | 26 % → 36 % | 42.6 px | 0.28 | 1.40 | 6 |
| stroke 36 | 25 % → 34 % | 41.0 px | 0.28 | 1.36 | 19 |
| stroke 37 | 12 % → 12 % | 19.3 px | 0.28 | 1.03 | 11 |
| stroke 38 | 19 % → 25 % | 31.7 px | 0.28 | 1.30 | 11 |
| stroke 39 | 16 % → 22 % | 27.3 px | 0.28 | 1.37 | 6 |
| stroke 40 | 22 % → 31 % | 36.6 px | 0.28 | 1.38 | 7 |
| stroke 41 | 32 % → 36 % | 53.1 px | 0.28 | 1.12 | 9 |
| stroke 42 | 23 % → 30 % | 38.2 px | 0.29 | 1.29 | 8 |
| stroke 43 | 12 % → 12 % | 20.3 px | 0.28 | 1.00 | 9 |
| stroke 44 | 30 % → 37 % | 48.9 px | 0.28 | 1.26 | 7 |
| stroke 45 | 16 % → 16 % | 26.2 px | 0.28 | 1.00 | 7 |
| stroke 46 | 29 % → 34 % | 48.0 px | 0.29 | 1.15 | 12 |
| stroke 47 | 38 % → 41 % | 62.0 px | 0.28 | 1.10 | 17 |
| stroke 48 | 29 % → 36 % | 47.8 px | 0.29 | 1.27 | 28 |
| stroke 49 | 27 % → 30 % | 45.1 px | 0.29 | 1.11 | 13 |
| stroke 50 | 38 % → 40 % | 63.4 px | 0.28 | 1.06 | 7 |
| stroke 51 | 16 % → 16 % | 26.1 px | 0.28 | 1.00 | 9 |
| stroke 52 | 37 % → 38 % | 62.4 px | 0.29 | 1.01 | 9 |
| stroke 53 | 22 % → 26 % | 36.9 px | 0.28 | 1.18 | 9 |
| stroke 54 | 17 % → 19 % | 29.1 px | 0.29 | 1.09 | 6 |
| stroke 55 | 15 % → 15 % | 25.0 px | 0.28 | 1.00 | 11 |
| stroke 56 | 13 % → 14 % | 21.6 px | 0.28 | 1.08 | 6 |
| stroke 57 | 23 % → 23 % | 37.7 px | 0.29 | 1.00 | 6 |
| stroke 58 | 28 % → 29 % | 46.1 px | 0.28 | 1.05 | 32 |
| stroke 59 | 40 % → 40 % | 67.3 px | 0.28 | 1.00 | 13 |
| stroke 60 | 22 % → 22 % | 35.6 px | 0.28 | 1.00 | 26 |

Numbers say: wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #43 Dragged black ink blocks — own sheet
own sheet 600 × 600 · Gouache 1.00 · 70 px · 7.8 s

![Brush Artist · Refs · #43 Dragged black ink blocks — own sheet](Brush-Artist-Refs-43-Dragged-black-ink-blocks-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 15 % → 8 % | 35.8 px | 0.46 | 0.54 | 384 |
| stroke 2 | 18 % → 13 % | 62.1 px | 0.46 | 0.75 | 470 |
| stroke 3 | 19 % → 14 % | 68.8 px | 0.46 | 0.75 | 488 |
| stroke 4 | 19 % → 13 % | 67.6 px | 0.46 | 0.65 | 490 |
| stroke 5 | 26 % → 14 % | 61.7 px | 0.46 | 0.54 | 555 |

## Brush Artist · Refs · #44 Blue looping ribbon — own sheet
own sheet 600 × 600 · Oil 1.00 · 80 px · 5.4 s

![Brush Artist · Refs · #44 Blue looping ribbon — own sheet](Brush-Artist-Refs-44-Blue-looping-ribbon-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 32 % → 32 % | 42.0 px | 0.78 | 1.00 | 2861 |

## Brush Artist · Refs · #45 Soft pastel pepper — own sheet
own sheet 600 × 600 · Pastel 1.00 · 40 px · 5.0 s

![Brush Artist · Refs · #45 Soft pastel pepper — own sheet](Brush-Artist-Refs-45-Soft-pastel-pepper-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 10 % → 39 % | 11.3 px | 0.49 | 3.75 | 373 |
| stroke 2 | 18 % → 34 % | 21.3 px | 0.49 | 1.87 | 358 |
| stroke 3 | 25 % → 37 % | 17.6 px | 0.49 | 1.46 | 590 |
| stroke 4 | 24 % → 35 % | 30.5 px | 0.49 | 1.43 | 319 |
| stroke 5 | 30 % → 30 % | 21.2 px | 0.49 | 1.00 | 197 |
| stroke 6 | 36 % → 44 % | 23.0 px | 0.48 | 1.23 | 342 |
| stroke 7 | 39 % → 43 % | 21.6 px | 0.48 | 1.10 | 328 |
| stroke 8 | 44 % → 44 % | 44.4 px | 0.49 | 1.00 | 422 |

Numbers say: wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #46 Red-brown ink lips — own sheet
own sheet 600 × 600 · Watercolour 1.00 · 50 px · 6.8 s

![Brush Artist · Refs · #46 Red-brown ink lips — own sheet](Brush-Artist-Refs-46-Red-brown-ink-lips-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 13 % → 29 % | 55.7 px | 0.55 | 2.17 | 99 |
| stroke 2 | 18 % → 36 % | 81.1 px | 0.50 | 1.95 | 126 |

Numbers say: wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #47 Pink knife slabs — own sheet
own sheet 600 × 600 · Impasto 1.00 · 90 px · 4.6 s

![Brush Artist · Refs · #47 Pink knife slabs — own sheet](Brush-Artist-Refs-47-Pink-knife-slabs-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 17 % → 32 % | 83.2 px | 0.11 | 1.94 | 458 |
| stroke 2 | 29 % → 43 % | 165.8 px | 0.11 | 1.46 | 272 |
| stroke 3 | 29 % → 43 % | 165.7 px | 0.11 | 1.47 | 308 |
| stroke 4 | 39 % → 38 % | 165.7 px | 0.11 | 0.98 | 281 |

Numbers say: wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #48 Black bands with drips — own sheet
own sheet 600 × 600 · Gouache 1.00 · 70 px · 10.5 s

![Brush Artist · Refs · #48 Black bands with drips — own sheet](Brush-Artist-Refs-48-Black-bands-with-drips-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 28 % → 41 % | 73.2 px | 0.39 | 1.46 | 688 |
| stroke 2 | 43 % → 57 % | 137.5 px | 0.39 | 1.33 | 567 |
| stroke 3 | 45 % → 57 % | 141.4 px | 0.39 | 1.27 | 447 |
| stroke 4 | 48 % → 46 % | 140.3 px | 0.39 | 0.96 | 566 |

## Brush Artist · Refs · #49 Magenta letters round brush — own sheet
own sheet 600 × 600 · Ink 1.00 · 30 px · 8.7 s

![Brush Artist · Refs · #49 Magenta letters round brush — own sheet](Brush-Artist-Refs-49-Magenta-letters-round-brush-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 27 % → 46 % | 64.3 px | 0.52 | 1.70 | 35 |
| stroke 2 | 29 % → 40 % | 52.5 px | 0.53 | 1.40 | 38 |
| stroke 3 | 41 % → 67 % | 96.3 px | 0.52 | 1.64 | 48 |
| stroke 4 | 34 % → 52 % | 53.7 px | 0.52 | 1.55 | 240 |
| stroke 5 | 40 % → 66 % | 94.7 px | 0.52 | 1.65 | 74 |
| stroke 6 | 54 % → 70 % | 231.2 px | 0.52 | 1.29 | 14 |
| stroke 7 | 41 % → 56 % | 63.9 px | 0.52 | 1.35 | 114 |
| stroke 8 | 36 % → 61 % | 91.9 px | 0.53 | 1.73 | 71 |
| stroke 9 | 49 % → 60 % | 152.9 px | 0.53 | 1.24 | 26 |
| stroke 10 | 42 % → 72 % | 100.4 px | 0.52 | 1.71 | 78 |
| stroke 11 | 52 % → 72 % | 219.8 px | 0.52 | 1.39 | 15 |
| stroke 12 | 53 % → 68 % | 82.2 px | 0.52 | 1.29 | 112 |
| stroke 13 | 42 % → 54 % | 115.9 px | 0.53 | 1.29 | 33 |
| stroke 14 | 45 % → 69 % | 131.7 px | 0.53 | 1.52 | 28 |
| stroke 15 | 43 % → 63 % | 102.4 px | 0.52 | 1.46 | 70 |
| stroke 16 | 52 % → 61 % | 220.3 px | 0.52 | 1.18 | 12 |
| stroke 17 | 53 % → 64 % | 82.2 px | 0.52 | 1.19 | 124 |
| stroke 18 | 36 % → 44 % | 99.6 px | 0.52 | 1.22 | 37 |
| stroke 19 | 54 % → 53 % | 123.7 px | 0.52 | 0.99 | 31 |
| stroke 20 | 54 % → 54 % | 125.3 px | 0.52 | 1.00 | 31 |
| stroke 21 | 49 % → 49 % | 81.3 px | 0.52 | 1.00 | 85 |

Numbers say: wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #50 Thick swipes on photo — own sheet
own sheet 600 × 600 · Impasto 1.00 · 40 px · 3.0 s

![Brush Artist · Refs · #50 Thick swipes on photo — own sheet](Brush-Artist-Refs-50-Thick-swipes-on-photo-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 9 % → 21 % | 42.8 px | 0.33 | 2.35 | 45 |
| stroke 2 | 9 % → 16 % | 42.5 px | 0.33 | 1.79 | 79 |
| stroke 3 | 10 % → 11 % | 41.9 px | 0.33 | 1.07 | 64 |
| stroke 4 | 11 % → 18 % | 42.7 px | 0.33 | 1.64 | 48 |
| stroke 5 | 11 % → 10 % | 41.9 px | 0.33 | 0.95 | 35 |
| stroke 6 | 17 % → 21 % | 97.7 px | 0.32 | 1.20 | 23 |
| stroke 7 | 22 % → 26 % | 92.8 px | 0.33 | 1.18 | 40 |
| stroke 8 | 21 % → 21 % | 119.9 px | 0.33 | 0.97 | 27 |
| stroke 9 | 9 % → 10 % | 42.1 px | 0.32 | 1.09 | 34 |
| stroke 10 | 22 % → 21 % | 73.6 px | 0.32 | 0.96 | 35 |
| stroke 11 | 9 % → 8 % | 42.7 px | 0.33 | 0.95 | 28 |
| stroke 12 | 17 % → 16 % | 93.2 px | 0.33 | 0.96 | 23 |

Numbers say: wet paint spreads well beyond the stroke.

## Brush Artist · Ink — dry brush — own sheet
own sheet 600 × 600 · Gouache 1.00 · 30 px · 2.9 s

![Brush Artist · Ink — dry brush — own sheet](Brush-Artist-Ink-dry-brush-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| ear | 6 % → 2 % | 7.0 px | 0.86 | 0.34 | 422 |
| drag0 | 6 % → 9 % | 11.3 px | 0.86 | 1.42 | 92 |
| drag1 | 9 % → 9 % | 18.5 px | 0.86 | 1.02 | 103 |
| drag2 | 11 % → 10 % | 25.6 px | 0.86 | 0.85 | 84 |
| drag3 | 13 % → 10 % | 32.8 px | 0.86 | 0.77 | 65 |

## Brush Artist · Watercolour — blue — own sheet
own sheet 600 × 600 · Watercolour 0.93 · Ink 0.07 · 40 px · 8.4 s

![Brush Artist · Watercolour — blue — own sheet](Brush-Artist-Watercolour-blue-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| s0 | 7 % → 24 % | 28.8 px | 0.30 | 3.32 | 39 |
| s1 | 6 % → 33 % | 10.1 px | 0.37 | 6.00 | 61 |
| s2 | 10 % → 19 % | 44.2 px | 0.26 | 1.81 | 35 |
| s3 | 10 % → 18 % | 26.7 px | 0.31 | 1.92 | 47 |
| s4 | 14 % → 30 % | 38.6 px | 0.36 | 2.16 | 56 |
| s5 | 19 % → 29 % | 39.3 px | 0.37 | 1.54 | 55 |
| s6 | 18 % → 22 % | 48.7 px | 0.31 | 1.25 | 78 |
| s7 | 25 % → 36 % | 32.7 px | 0.37 | 1.46 | 35 |
| s8 | 21 % → 25 % | 79.8 px | 0.30 | 1.20 | 37 |

Numbers say: wet paint spreads well beyond the stroke.

## Brush Artist · Charcoal — stick — own sheet
own sheet 600 × 600 · Charcoal 0.78 · Pastel 0.22 · 28 px · 1.4 s

![Brush Artist · Charcoal — stick — own sheet](Brush-Artist-Charcoal-stick-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| finger0 | 12 % → 25 % | 21.7 px | 0.83 | 2.02 | 39 |
| tip0 | 12 % → 21 % | 33.4 px | 0.83 | 1.69 | 17 |
| finger1 | 23 % → 40 % | 41.1 px | 0.83 | 1.71 | 63 |
| tip1 | 21 % → 29 % | 56.0 px | 0.83 | 1.41 | 21 |
| finger2 | 23 % → 35 % | 41.3 px | 0.83 | 1.53 | 47 |
| tip2 | 21 % → 29 % | 56.0 px | 0.83 | 1.41 | 12 |
| finger3 | 23 % → 27 % | 41.6 px | 0.83 | 1.15 | 46 |
| tip3 | 21 % → 21 % | 56.3 px | 0.83 | 1.00 | 13 |
| cig0 | 33 % → 46 % | 73.2 px | 0.83 | 1.40 | 14 |
| cig1 | 35 % → 46 % | 78.8 px | 0.83 | 1.29 | 15 |
| cig2 | 38 % → 46 % | 84.4 px | 0.83 | 1.21 | 21 |
| cig3 | 40 % → 46 % | 90.0 px | 0.83 | 1.13 | 15 |
| cig4 | 43 % → 45 % | 95.5 px | 0.83 | 1.06 | 15 |
| cig5 | 45 % → 45 % | 101.1 px | 0.83 | 1.00 | 16 |

Numbers say: wet paint spreads well beyond the stroke.

