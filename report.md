![All brushes](contact.png)

# Brush Lab — 143 brushes · 3 Nov 2026 at 14:53

Every sheet: 1500 × 600, ten strokes in a 5 × 2 grid — 1. light line · 2. heavy line · 3. pressure swell · 4. fast wave · 5. slow wave · 6. spiral · 7. loop · 8. tilted · 9. over the wet one · 10. long, no reload (cell 8 holds «tilted» and «over the wet one» crossed). The CPU reference of Mamay's paint engine; the wet layer settles 20 s at the end.

Columns: **covered** = share of the cell with paint right after the stroke → after settling; **width** = painted area of the stroke ÷ its length (px); **dark** = mean darkness of the painted pixels above the paper's own grain (0 = paper, 1 = black); **spread** = how far wet paint went beyond the stroke (1.0 = stayed); **ms** = the stroke on the CPU; long stroke: paint in each quarter of its length (it should run out: wet → streaks → dry tail).

## Ink Line
Ink · 12 px · 22.3 s

![Ink Line](Ink-Line.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 1 % → 4 % | 4.3 px | 0.55 | 2.44 | 36 |
| heavy line | 5 % → 6 % | 15.7 px | 0.68 | 1.13 | 54 |
| pressure swell | 3 % → 4 % | 11.3 px | 0.64 | 1.40 | 23 |
| fast wave | 10 % → 11 % | 11.2 px | 0.59 | 1.11 | 98 |
| slow wave | 8 % → 10 % | 9.6 px | 0.57 | 1.16 | 100 |
| spiral | 14 % → 15 % | 8.9 px | 0.50 | 1.07 | 182 |
| loop | 8 % → 9 % | 10.6 px | 0.61 | 1.16 | 84 |
| tilted | 5 % → 5 % | 14.4 px | 0.65 | 1.05 | 46 |
| over the wet one | 10 % → 11 % | 12.5 px | 0.65 | 1.15 | 45 |
| long, no reload | 18 % → 17 % | 8.1 px | 0.47 | 0.96 | 245 | quarters: 0.22 → 0.09 → 0.04 → 0.02

Numbers say: light vs heavy: width 4.3 → 15.7 px, dark 0.55 → 0.68; wet paint spreads well beyond the stroke.

## Dense Ink
Ink · 14 px · 22.3 s

![Dense Ink](Dense-Ink.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 5 % → 7 % | 15.2 px | 0.72 | 1.26 | 34 |
| heavy line | 7 % → 7 % | 19.1 px | 0.73 | 1.09 | 64 |
| pressure swell | 5 % → 6 % | 17.9 px | 0.72 | 1.17 | 33 |
| fast wave | 13 % → 13 % | 15.3 px | 0.69 | 1.01 | 127 |
| slow wave | 12 % → 12 % | 13.6 px | 0.67 | 1.04 | 157 |
| spiral | 18 % → 15 % | 12.2 px | 0.65 | 0.80 | 183 |
| loop | 11 % → 12 % | 14.8 px | 0.69 | 1.08 | 97 |
| tilted | 5 % → 6 % | 14.6 px | 0.72 | 1.07 | 49 |
| over the wet one | 12 % → 13 % | 17.7 px | 0.72 | 1.11 | 47 |
| long, no reload | 23 % → 15 % | 10.1 px | 0.64 | 0.66 | 294 | quarters: 0.30 → 0.12 → 0.04 → 0.02

Numbers say: light vs heavy: width 15.2 → 19.1 px, dark 0.72 → 0.73.

## Transparent Wash
Watercolor · 22 px · 23.1 s

![Transparent Wash](Transparent-Wash.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 2 % → 5 % | 6.9 px | 0.27 | 2.25 | 29 |
| heavy line | 7 % → 9 % | 20.4 px | 0.27 | 1.22 | 52 |
| pressure swell | 4 % → 6 % | 15.2 px | 0.28 | 1.54 | 31 |
| fast wave | 14 % → 16 % | 16.1 px | 0.20 | 1.17 | 105 |
| slow wave | 12 % → 15 % | 13.7 px | 0.21 | 1.28 | 168 |
| spiral | 18 % → 22 % | 11.9 px | 0.16 | 1.23 | 134 |
| loop | 11 % → 13 % | 14.5 px | 0.22 | 1.20 | 81 |
| tilted | 8 % → 8 % | 21.1 px | 0.24 | 1.06 | 50 |
| over the wet one | 13 % → 16 % | 16.4 px | 0.24 | 1.18 | 45 |
| long, no reload | 26 % → 32 % | 11.6 px | 0.13 | 1.22 | 249 | quarters: 0.11 → 0.04 → 0.02 → 0.01

Numbers say: light vs heavy: width 6.9 → 20.4 px, dark 0.27 → 0.27; wet paint spreads well beyond the stroke.

## Dry Brush
Gouache · 24 px · 18.9 s

![Dry Brush](Dry-Brush.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 5 % → 0 % | 14.0 px | 0.65 | 0.09 | 41 |
| heavy line | 6 % → 0 % | 18.6 px | 0.65 | 0.02 | 70 |
| pressure swell | 5 % → 0 % | 18.2 px | 0.65 | 0.08 | 53 |
| fast wave | 6 % → 1 % | 7.3 px | 0.65 | 0.08 | 136 |
| slow wave | 7 % → 0 % | 8.1 px | 0.65 | 0.06 | 230 |
| spiral | 7 % → 0 % | 4.6 px | 0.65 | 0.07 | 196 |
| loop | 10 % → 0 % | 12.4 px | 0.65 | 0.04 | 115 |
| tilted | 4 % → 3 % | 10.6 px | 0.65 | 0.88 | 65 |
| over the wet one | 9 % → 1 % | 14.5 px | 0.65 | 0.12 | 57 |
| long, no reload | 6 % → 1 % | 2.9 px | 0.65 | 0.14 | 306 | quarters: 0.12 → 0.00 → 0.00 → 0.00

Numbers say: light vs heavy: width 14.0 → 18.6 px, dark 0.65 → 0.65.

## Wax Crayon
Wax · 8 px · 8.8 s

![Wax Crayon](Wax-Crayon.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 1 % → 1 % | 2.5 px | 0.71 | 1.00 | 18 |
| heavy line | 1 % → 1 % | 3.9 px | 0.69 | 1.00 | 10 |
| pressure swell | 1 % → 1 % | 3.3 px | 0.70 | 1.00 | 11 |
| fast wave | 3 % → 3 % | 3.5 px | 0.69 | 1.00 | 49 |
| slow wave | 3 % → 3 % | 3.4 px | 0.70 | 1.00 | 32 |
| spiral | 5 % → 5 % | 3.3 px | 0.70 | 1.00 | 69 |
| loop | 3 % → 3 % | 3.3 px | 0.70 | 1.00 | 41 |
| tilted | 2 % → 2 % | 5.6 px | 0.68 | 1.00 | 17 |
| over the wet one | 3 % → 3 % | 3.6 px | 0.68 | 1.00 | 14 |
| long, no reload | 7 % → 7 % | 3.3 px | 0.70 | 1.00 | 141 | quarters: 0.06 → 0.06 → 0.06 → 0.06

Numbers say: light vs heavy: width 2.5 → 3.9 px, dark 0.71 → 0.69; the long stroke does not run out of paint.

## Oil Pastel
Wax · 12 px · 8.8 s

![Oil Pastel](Oil-Pastel.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 1 % → 1 % | 4.0 px | 0.68 | 1.00 | 18 |
| heavy line | 2 % → 2 % | 6.5 px | 0.68 | 1.00 | 21 |
| pressure swell | 2 % → 2 % | 5.7 px | 0.69 | 1.00 | 15 |
| fast wave | 5 % → 5 % | 5.7 px | 0.68 | 1.00 | 52 |
| slow wave | 5 % → 5 % | 5.5 px | 0.68 | 1.00 | 55 |
| spiral | 8 % → 8 % | 5.5 px | 0.68 | 1.00 | 107 |
| loop | 4 % → 4 % | 5.6 px | 0.68 | 1.00 | 51 |
| tilted | 2 % → 2 % | 6.8 px | 0.68 | 1.00 | 31 |
| over the wet one | 5 % → 5 % | 5.8 px | 0.68 | 1.00 | 26 |
| long, no reload | 13 % → 13 % | 5.6 px | 0.68 | 1.00 | 149 | quarters: 0.10 → 0.09 → 0.10 → 0.10

Numbers say: light vs heavy: width 4.0 → 6.5 px, dark 0.68 → 0.68; the long stroke does not run out of paint.

## Charcoal
Charcoal · 5 px · 8.7 s

![Charcoal](Charcoal.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 1 % → 1 % | 2.0 px | 0.74 | 1.00 | 14 |
| heavy line | 1 % → 1 % | 3.0 px | 0.74 | 1.00 | 6 |
| pressure swell | 1 % → 1 % | 2.7 px | 0.74 | 1.00 | 11 |
| fast wave | 2 % → 2 % | 2.7 px | 0.73 | 1.00 | 42 |
| slow wave | 2 % → 2 % | 2.6 px | 0.74 | 1.00 | 27 |
| spiral | 4 % → 4 % | 2.5 px | 0.74 | 1.00 | 52 |
| loop | 2 % → 2 % | 2.6 px | 0.74 | 1.00 | 22 |
| tilted | 2 % → 2 % | 4.3 px | 0.72 | 1.00 | 9 |
| over the wet one | 2 % → 2 % | 2.4 px | 0.72 | 1.00 | 14 |
| long, no reload | 6 % → 6 % | 2.7 px | 0.73 | 1.00 | 82 | quarters: 0.05 → 0.05 → 0.05 → 0.05

Numbers say: light vs heavy: width 2.0 → 3.0 px, dark 0.74 → 0.74; the long stroke does not run out of paint.

## Impasto
Heavy acrylic · 22 px · 12.7 s

![Impasto](Impasto.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 8 % → 8 % | 24.1 px | 0.71 | 0.93 | 42 |
| heavy line | 10 % → 9 % | 28.8 px | 0.70 | 0.94 | 76 |
| pressure swell | 7 % → 7 % | 28.1 px | 0.72 | 0.94 | 45 |
| fast wave | 20 % → 13 % | 23.5 px | 0.71 | 0.64 | 128 |
| slow wave | 21 % → 14 % | 24.5 px | 0.71 | 0.66 | 212 |
| spiral | 30 % → 14 % | 20.0 px | 0.71 | 0.46 | 256 |
| loop | 18 % → 14 % | 23.9 px | 0.71 | 0.77 | 114 |
| tilted | 8 % → 8 % | 21.8 px | 0.70 | 1.00 | 63 |
| over the wet one | 17 % → 15 % | 25.4 px | 0.70 | 0.91 | 60 |
| long, no reload | 34 % → 14 % | 15.2 px | 0.71 | 0.41 | 324 | quarters: 0.38 → 0.21 → 0.10 → 0.03

Numbers say: light vs heavy: width 24.1 → 28.8 px, dark 0.71 → 0.70.

## Oil Round
Oil · 18 px · 16.0 s

![Oil Round](Oil-Round.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 2 % → 2 % | 7.2 px | 0.75 | 1.00 | 37 |
| heavy line | 7 % → 7 % | 19.3 px | 0.73 | 1.00 | 72 |
| pressure swell | 4 % → 4 % | 13.7 px | 0.72 | 1.00 | 32 |
| fast wave | 11 % → 11 % | 12.7 px | 0.65 | 1.00 | 135 |
| slow wave | 8 % → 8 % | 9.0 px | 0.57 | 1.00 | 145 |
| spiral | 10 % → 10 % | 6.6 px | 0.50 | 1.00 | 186 |
| loop | 5 % → 5 % | 7.1 px | 0.45 | 1.00 | 89 |
| tilted | 4 % → 4 % | 10.1 px | 0.52 | 1.00 | 56 |
| over the wet one | 6 % → 6 % | 7.4 px | 0.52 | 1.00 | 48 |
| long, no reload | 15 % → 15 % | 6.8 px | 0.42 | 1.00 | 277 | quarters: 0.08 → 0.08 → 0.07 → 0.06

Numbers say: light vs heavy: width 7.2 → 19.3 px, dark 0.75 → 0.73.

## Palette Knife
Oil · 20 px · 15.5 s

![Palette Knife](Palette-Knife.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 8 % → 8 % | 21.9 px | 0.67 | 1.00 | 17 |
| heavy line | 8 % → 8 % | 22.5 px | 0.73 | 1.00 | 13 |
| pressure swell | 6 % → 6 % | 22.4 px | 0.74 | 1.00 | 7 |
| fast wave | 17 % → 17 % | 19.3 px | 0.49 | 1.00 | 17 |
| slow wave | 17 % → 17 % | 19.9 px | 0.43 | 1.00 | 28 |
| spiral | 18 % → 18 % | 11.7 px | 0.45 | 1.00 | 35 |
| loop | 16 % → 16 % | 21.0 px | 0.58 | 1.00 | 18 |
| tilted | 5 % → 5 % | 15.0 px | 0.72 | 1.00 | 12 |
| over the wet one | 13 % → 13 % | 21.0 px | 0.72 | 1.00 | 8 |
| long, no reload | 17 % → 17 % | 7.5 px | 0.47 | 1.00 | 61 | quarters: 0.29 → 0.05 → 0.00 → 0.00

Numbers say: light vs heavy: width 21.9 → 22.5 px, dark 0.67 → 0.73; pressure barely changes the width.

## Water
Watercolor · 20 px · 31.7 s · over bands of wet oil paint and oil pastel in turn (it works on paint already there: look at what it does to the bands; covered counts the bands too)

![Water](Water.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 25 % → 27 % | 73.8 px | 0.80 | 1.06 | 17 |
| heavy line | 24 % → 25 % | 69.8 px | 0.81 | 1.04 | 50 |
| pressure swell | 24 % → 25 % | 89.6 px | 0.81 | 1.03 | 30 |
| fast wave | 24 % → 26 % | 27.7 px | 0.81 | 1.07 | 97 |
| slow wave | 24 % → 25 % | 27.7 px | 0.81 | 1.06 | 126 |
| spiral | 24 % → 26 % | 15.9 px | 0.81 | 1.07 | 150 |
| loop | 24 % → 25 % | 31.1 px | 0.81 | 1.03 | 78 |
| tilted | 24 % → 24 % | 67.0 px | 0.81 | 1.00 | 52 |
| over the wet one | 24 % → 25 % | 0.0 px | 0.81 | 1.06 | 39 |
| long, no reload | 24 % → 26 % | 10.7 px | 0.81 | 1.08 | 228 | quarters: 0.21 → 0.27 → 0.18 → 0.27

Numbers say: light vs heavy: width 73.8 → 69.8 px, dark 0.80 → 0.81; pressure barely changes the width; the long stroke does not run out of paint.

## Blender
Pastel · 16 px · 18.8 s · over bands of wet oil paint and oil pastel in turn (it works on paint already there: look at what it does to the bands; covered counts the bands too)

![Blender](Blender.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 24 % → 24 % | 70.7 px | 0.81 | 1.00 | 16 |
| heavy line | 25 % → 25 % | 72.1 px | 0.80 | 1.00 | 30 |
| pressure swell | 24 % → 24 % | 91.3 px | 0.81 | 1.00 | 13 |
| fast wave | 26 % → 26 % | 30.0 px | 0.79 | 1.00 | 69 |
| slow wave | 26 % → 26 % | 29.9 px | 0.80 | 1.00 | 71 |
| spiral | 28 % → 28 % | 18.7 px | 0.77 | 1.00 | 97 |
| loop | 25 % → 25 % | 32.9 px | 0.80 | 1.00 | 50 |
| tilted | 25 % → 25 % | 70.1 px | 0.79 | 1.00 | 38 |
| over the wet one | 26 % → 26 % | 1.8 px | 0.79 | 1.00 | 24 |
| long, no reload | 30 % → 30 % | 13.7 px | 0.76 | 1.00 | 142 | quarters: 0.20 → 0.28 → 0.23 → 0.30

Numbers say: light vs heavy: width 70.7 → 72.1 px, dark 0.81 → 0.80; pressure barely changes the width; the long stroke does not run out of paint.

## Eraser
Eraser · 16 px · 18.2 s · over bands of wet oil paint and oil pastel in turn (it works on paint already there: look at what it does to the bands; covered counts the bands too)

![Eraser](Eraser.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 24 % → 24 % | 69.5 px | 0.82 | 1.00 | 25 |
| heavy line | 23 % → 23 % | 67.9 px | 0.82 | 1.00 | 26 |
| pressure swell | 23 % → 23 % | 87.3 px | 0.82 | 1.00 | 18 |
| fast wave | 22 % → 22 % | 25.7 px | 0.82 | 1.00 | 58 |
| slow wave | 22 % → 22 % | 25.7 px | 0.82 | 1.00 | 75 |
| spiral | 22 % → 22 % | 14.4 px | 0.82 | 1.00 | 103 |
| loop | 22 % → 22 % | 28.6 px | 0.82 | 1.00 | 59 |
| tilted | 23 % → 23 % | 65.1 px | 0.82 | 1.00 | 32 |
| over the wet one | 23 % → 23 % | 0.0 px | 0.82 | 1.00 | 24 |
| long, no reload | 20 % → 20 % | 8.9 px | 0.82 | 1.00 | 160 | quarters: 0.15 → 0.20 → 0.15 → 0.20

Numbers say: light vs heavy: width 69.5 → 67.9 px, dark 0.82 → 0.82; pressure barely changes the width; the long stroke does not run out of paint.

## Fan
Gouache · 30 px · 26.6 s

![Fan](Fan.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 9 % → 3 % | 25.7 px | 0.63 | 0.37 | 28 |
| heavy line | 11 % → 4 % | 31.0 px | 0.63 | 0.39 | 55 |
| pressure swell | 8 % → 5 % | 31.7 px | 0.63 | 0.55 | 26 |
| fast wave | 18 % → 5 % | 20.3 px | 0.63 | 0.26 | 86 |
| slow wave | 18 % → 5 % | 21.1 px | 0.63 | 0.25 | 149 |
| spiral | 24 % → 5 % | 15.8 px | 0.63 | 0.20 | 148 |
| loop | 17 % → 5 % | 22.7 px | 0.63 | 0.29 | 94 |
| tilted | 5 % → 6 % | 15.1 px | 0.63 | 1.05 | 32 |
| over the wet one | 16 % → 8 % | 29.8 px | 0.63 | 0.50 | 40 |
| long, no reload | 23 % → 5 % | 10.1 px | 0.63 | 0.22 | 241 | quarters: 0.29 → 0.07 → 0.01 → 0.00

Numbers say: light vs heavy: width 25.7 → 31.0 px, dark 0.63 → 0.63.

## Sponge
Gouache · 30 px · 26.3 s

![Sponge](Sponge.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 4 % → 0 % | 11.4 px | 0.62 | 0.12 | 35 |
| heavy line | 12 % → 2 % | 35.4 px | 0.62 | 0.14 | 51 |
| pressure swell | 7 % → 2 % | 27.9 px | 0.62 | 0.27 | 38 |
| fast wave | 20 % → 4 % | 23.2 px | 0.62 | 0.19 | 105 |
| slow wave | 21 % → 4 % | 23.7 px | 0.62 | 0.18 | 205 |
| spiral | 28 % → 4 % | 18.3 px | 0.62 | 0.14 | 166 |
| loop | 18 % → 5 % | 23.0 px | 0.62 | 0.29 | 111 |
| tilted | 7 % → 7 % | 18.2 px | 0.62 | 1.04 | 79 |
| over the wet one | 16 % → 6 % | 27.8 px | 0.62 | 0.37 | 47 |
| long, no reload | 29 % → 5 % | 12.9 px | 0.62 | 0.17 | 248 | quarters: 0.29 → 0.13 → 0.07 → 0.04

Numbers say: light vs heavy: width 11.4 → 35.4 px, dark 0.62 → 0.62.

## Ink — sumi brush
Watercolor · 22 px · 24.4 s

![Ink — sumi brush](Ink-sumi-brush.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 6 % → 6 % | 18.4 px | 0.43 | 0.99 | 53 |
| heavy line | 10 % → 10 % | 30.2 px | 0.37 | 0.99 | 60 |
| pressure swell | 7 % → 7 % | 27.7 px | 0.42 | 0.99 | 43 |
| fast wave | 20 % → 16 % | 23.6 px | 0.31 | 0.79 | 147 |
| slow wave | 19 % → 17 % | 22.4 px | 0.36 | 0.89 | 220 |
| spiral | 29 % → 20 % | 18.9 px | 0.31 | 0.71 | 241 |
| loop | 17 % → 17 % | 22.4 px | 0.35 | 0.97 | 133 |
| tilted | 6 % → 7 % | 16.4 px | 0.39 | 1.16 | 68 |
| over the wet one | 16 % → 15 % | 28.0 px | 0.39 | 0.95 | 64 |
| long, no reload | 34 % → 23 % | 15.1 px | 0.31 | 0.68 | 380 | quarters: 0.22 → 0.10 → 0.06 → 0.04

Numbers say: light vs heavy: width 18.4 → 30.2 px, dark 0.43 → 0.37.

## Ink — wash
Watercolor · 40 px · 27.6 s

![Ink — wash](Ink-wash.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 7 % → 9 % | 20.6 px | 0.05 | 1.21 | 62 |
| heavy line | 10 % → 12 % | 30.2 px | 0.04 | 1.11 | 71 |
| pressure swell | 7 % → 8 % | 25.9 px | 0.05 | 1.20 | 52 |
| fast wave | 21 % → 23 % | 24.7 px | 0.04 | 1.07 | 176 |
| slow wave | 20 % → 23 % | 23.5 px | 0.06 | 1.15 | 285 |
| spiral | 33 % → 35 % | 21.8 px | 0.05 | 1.05 | 289 |
| loop | 19 % → 22 % | 24.0 px | 0.05 | 1.17 | 157 |
| tilted | 7 % → 8 % | 19.6 px | 0.06 | 1.20 | 107 |
| over the wet one | 17 % → 19 % | 28.3 px | 0.06 | 1.11 | 72 |
| long, no reload | 38 % → 40 % | 17.1 px | 0.05 | 1.04 | 429 | quarters: 0.04 → 0.03 → 0.02 → 0.01

Numbers say: light vs heavy: width 20.6 → 30.2 px, dark 0.05 → 0.04.

## Ink — dry brush
Ink · 30 px · 22.2 s

![Ink — dry brush](Ink-dry-brush.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 9 % → 7 % | 25.2 px | 0.81 | 0.79 | 72 |
| heavy line | 10 % → 8 % | 29.6 px | 0.80 | 0.76 | 113 |
| pressure swell | 7 % → 6 % | 27.9 px | 0.81 | 0.85 | 65 |
| fast wave | 21 % → 8 % | 24.2 px | 0.79 | 0.40 | 210 |
| slow wave | 18 % → 7 % | 20.3 px | 0.79 | 0.39 | 350 |
| spiral | 24 % → 8 % | 15.6 px | 0.78 | 0.34 | 337 |
| loop | 19 % → 8 % | 24.3 px | 0.78 | 0.45 | 185 |
| tilted | 8 % → 8 % | 22.2 px | 0.78 | 1.02 | 106 |
| over the wet one | 17 % → 14 % | 25.9 px | 0.78 | 0.81 | 85 |
| long, no reload | 20 % → 8 % | 9.1 px | 0.79 | 0.41 | 484 | quarters: 0.32 → 0.02 → 0.00 → 0.00

Numbers say: light vs heavy: width 25.2 → 29.6 px, dark 0.81 → 0.80.

## Ink — nib
Watercolor · 5 px · 20.7 s

![Ink — nib](Ink-nib.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 1 % → 2 % | 4.3 px | 0.71 | 1.15 | 24 |
| heavy line | 2 % → 2 % | 5.0 px | 0.73 | 1.15 | 18 |
| pressure swell | 1 % → 2 % | 4.8 px | 0.74 | 1.19 | 21 |
| fast wave | 4 % → 3 % | 4.1 px | 0.65 | 0.96 | 51 |
| slow wave | 4 % → 4 % | 4.1 px | 0.65 | 1.06 | 54 |
| spiral | 5 % → 4 % | 3.4 px | 0.60 | 0.84 | 103 |
| loop | 3 % → 3 % | 4.1 px | 0.66 | 1.07 | 46 |
| tilted | 2 % → 2 % | 5.3 px | 0.63 | 1.22 | 23 |
| over the wet one | 4 % → 4 % | 5.8 px | 0.63 | 0.95 | 16 |
| long, no reload | 7 % → 5 % | 3.1 px | 0.60 | 0.70 | 120 | quarters: 0.09 → 0.04 → 0.02 → 0.02

Numbers say: light vs heavy: width 4.3 → 5.0 px, dark 0.71 → 0.73.

## 0.45 · Dry brush
Gouache · 34 px · 23.0 s

![0.45 · Dry brush](0-45-Dry-brush.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 10 % → 3 % | 29.4 px | 0.67 | 0.29 | 97 |
| heavy line | 11 % → 3 % | 31.6 px | 0.67 | 0.30 | 111 |
| pressure swell | 8 % → 3 % | 31.5 px | 0.67 | 0.41 | 77 |
| fast wave | 19 % → 3 % | 22.5 px | 0.67 | 0.18 | 275 |
| slow wave | 20 % → 4 % | 23.2 px | 0.67 | 0.18 | 429 |
| spiral | 21 % → 3 % | 14.1 px | 0.67 | 0.16 | 421 |
| loop | 20 % → 4 % | 26.1 px | 0.67 | 0.20 | 230 |
| tilted | 9 % → 8 % | 24.0 px | 0.67 | 0.98 | 128 |
| over the wet one | 19 % → 6 % | 28.2 px | 0.67 | 0.34 | 116 |
| long, no reload | 20 % → 4 % | 9.1 px | 0.67 | 0.19 | 604 | quarters: 0.36 → 0.10 → 0.00 → 0.00

Numbers say: light vs heavy: width 29.4 → 31.6 px, dark 0.67 → 0.67; pressure barely changes the width.

## Dry pastel
Pastel · 26 px · 9.6 s

![Dry pastel](Dry-pastel.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 3 % → 3 % | 8.3 px | 0.38 | 1.00 | 25 |
| heavy line | 5 % → 5 % | 13.2 px | 0.39 | 1.00 | 26 |
| pressure swell | 3 % → 3 % | 11.7 px | 0.38 | 1.00 | 20 |
| fast wave | 10 % → 10 % | 11.9 px | 0.39 | 1.00 | 90 |
| slow wave | 10 % → 10 % | 11.3 px | 0.39 | 1.00 | 135 |
| spiral | 15 % → 15 % | 9.6 px | 0.39 | 1.00 | 129 |
| loop | 7 % → 7 % | 9.4 px | 0.39 | 1.00 | 71 |
| tilted | 3 % → 3 % | 8.3 px | 0.38 | 1.00 | 38 |
| over the wet one | 7 % → 7 % | 11.1 px | 0.38 | 1.00 | 32 |
| long, no reload | 18 % → 18 % | 8.2 px | 0.39 | 1.00 | 193 | quarters: 0.08 → 0.08 → 0.08 → 0.07

Numbers say: light vs heavy: width 8.3 → 13.2 px, dark 0.38 → 0.39; the long stroke does not run out of paint.

## 0.45 · Charcoal
Charcoal · 18 px · 9.2 s

![0.45 · Charcoal](0-45-Charcoal.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 2 % → 2 % | 6.5 px | 0.80 | 1.00 | 15 |
| heavy line | 3 % → 3 % | 9.2 px | 0.80 | 1.00 | 15 |
| pressure swell | 2 % → 2 % | 8.8 px | 0.80 | 1.00 | 8 |
| fast wave | 7 % → 7 % | 8.5 px | 0.80 | 1.00 | 35 |
| slow wave | 7 % → 7 % | 8.0 px | 0.80 | 1.00 | 54 |
| spiral | 12 % → 12 % | 7.9 px | 0.80 | 1.00 | 61 |
| loop | 6 % → 6 % | 8.1 px | 0.80 | 1.00 | 37 |
| tilted | 3 % → 3 % | 7.5 px | 0.80 | 1.00 | 22 |
| over the wet one | 6 % → 6 % | 7.9 px | 0.80 | 1.00 | 13 |
| long, no reload | 17 % → 17 % | 7.8 px | 0.80 | 1.00 | 80 | quarters: 0.15 → 0.16 → 0.15 → 0.16

Numbers say: light vs heavy: width 6.5 → 9.2 px, dark 0.80 → 0.80; the long stroke does not run out of paint.

## Watercolour — wash
Watercolor · 50 px · 28.4 s

![Watercolour — wash](Watercolour-wash.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 8 % → 9 % | 23.5 px | 0.01 | 1.13 | 84 |
| heavy line | 13 % → 14 % | 37.2 px | 0.01 | 1.07 | 101 |
| pressure swell | 8 % → 9 % | 28.6 px | 0.01 | 1.12 | 73 |
| fast wave | 25 % → 27 % | 28.9 px | 0.01 | 1.10 | 224 |
| slow wave | 25 % → 28 % | 28.5 px | 0.01 | 1.13 | 392 |
| spiral | 38 % → 43 % | 25.1 px | 0.01 | 1.12 | 414 |
| loop | 22 % → 25 % | 28.3 px | 0.01 | 1.14 | 210 |
| tilted | 10 % → 11 % | 26.7 px | 0.01 | 1.13 | 143 |
| over the wet one | 20 % → 22 % | 29.3 px | 0.01 | 1.09 | 98 |
| long, no reload | 44 % → 49 % | 19.7 px | 0.01 | 1.12 | 731 | quarters: 0.01 → 0.01 → 0.00 → 0.00

Numbers say: light vs heavy: width 23.5 → 37.2 px, dark 0.01 → 0.01.

## Watercolour — wet-in-wet
Watercolor · 44 px · 27.0 s

![Watercolour — wet-in-wet](Watercolour-wet-in-wet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 7 % → 8 % | 19.2 px | 0.01 | 1.23 | 66 |
| heavy line | 11 % → 12 % | 30.8 px | 0.01 | 1.16 | 86 |
| pressure swell | 7 % → 8 % | 24.7 px | 0.01 | 1.19 | 60 |
| fast wave | 22 % → 26 % | 25.8 px | 0.01 | 1.15 | 195 |
| slow wave | 22 % → 25 % | 25.1 px | 0.01 | 1.17 | 319 |
| spiral | 35 % → 41 % | 23.1 px | 0.01 | 1.17 | 330 |
| loop | 19 % → 23 % | 25.2 px | 0.01 | 1.17 | 172 |
| tilted | 8 % → 9 % | 21.2 px | 0.01 | 1.15 | 116 |
| over the wet one | 16 % → 18 % | 24.7 px | 0.01 | 1.12 | 82 |
| long, no reload | 41 % → 48 % | 18.3 px | 0.01 | 1.18 | 471 | quarters: 0.01 → 0.00 → 0.00 → 0.00

Numbers say: light vs heavy: width 19.2 → 30.8 px, dark 0.01 → 0.01.

## Watercolour — glaze
Watercolor · 38 px · 25.7 s

![Watercolour — glaze](Watercolour-glaze.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 7 % → 8 % | 19.2 px | 0.01 | 1.17 | 68 |
| heavy line | 11 % → 13 % | 32.3 px | 0.01 | 1.15 | 74 |
| pressure swell | 6 % → 8 % | 23.9 px | 0.01 | 1.21 | 50 |
| fast wave | 19 % → 22 % | 22.3 px | 0.01 | 1.14 | 163 |
| slow wave | 19 % → 22 % | 21.9 px | 0.01 | 1.16 | 280 |
| spiral | 30 % → 32 % | 19.9 px | 0.01 | 1.06 | 292 |
| loop | 18 % → 22 % | 23.8 px | 0.01 | 1.20 | 154 |
| tilted | 7 % → 8 % | 19.2 px | 0.01 | 1.18 | 95 |
| over the wet one | 16 % → 18 % | 25.9 px | 0.01 | 1.14 | 71 |
| long, no reload | 34 % → 36 % | 15.4 px | 0.01 | 1.04 | 404 | quarters: 0.01 → 0.00 → 0.00 → 0.00

Numbers say: light vs heavy: width 19.2 → 32.3 px, dark 0.01 → 0.01.

## Watercolour — granulating
Watercolor · 44 px · 25.9 s

![Watercolour — granulating](Watercolour-granulating.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 7 % → 7 % | 19.3 px | 0.01 | 1.05 | 67 |
| heavy line | 11 % → 11 % | 31.0 px | 0.01 | 1.02 | 84 |
| pressure swell | 7 % → 7 % | 25.9 px | 0.01 | 1.05 | 54 |
| fast wave | 21 % → 20 % | 24.0 px | 0.01 | 0.99 | 212 |
| slow wave | 21 % → 21 % | 24.3 px | 0.02 | 1.02 | 308 |
| spiral | 34 % → 35 % | 22.5 px | 0.01 | 1.03 | 324 |
| loop | 17 % → 18 % | 22.5 px | 0.02 | 1.04 | 160 |
| tilted | 8 % → 8 % | 22.0 px | 0.02 | 1.08 | 110 |
| over the wet one | 17 % → 18 % | 26.4 px | 0.02 | 1.04 | 81 |
| long, no reload | 39 % → 39 % | 17.4 px | 0.02 | 1.01 | 472 | quarters: 0.01 → 0.01 → 0.01 → 0.00

Numbers say: light vs heavy: width 19.3 → 31.0 px, dark 0.01 → 0.01.

## Watercolour — dry brush
Watercolor · 36 px · 22.9 s

![Watercolour — dry brush](Watercolour-dry-brush.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 5 % → 5 % | 15.5 px | 0.06 | 0.88 | 86 |
| heavy line | 9 % → 7 % | 24.9 px | 0.05 | 0.80 | 91 |
| pressure swell | 6 % → 5 % | 22.3 px | 0.06 | 0.89 | 65 |
| fast wave | 19 % → 11 % | 21.9 px | 0.04 | 0.58 | 242 |
| slow wave | 18 % → 10 % | 20.6 px | 0.05 | 0.55 | 378 |
| spiral | 23 % → 11 % | 15.2 px | 0.04 | 0.46 | 397 |
| loop | 15 % → 11 % | 19.5 px | 0.05 | 0.73 | 201 |
| tilted | 7 % → 7 % | 18.2 px | 0.05 | 1.08 | 112 |
| over the wet one | 14 % → 13 % | 21.8 px | 0.05 | 0.88 | 98 |
| long, no reload | 21 % → 12 % | 9.6 px | 0.05 | 0.57 | 579 | quarters: 0.02 → 0.01 → 0.00 → 0.00

Numbers say: light vs heavy: width 15.5 → 24.9 px, dark 0.06 → 0.05.

## Gouache
Gouache · 30 px · 23.3 s

![Gouache](Gouache.png)

A light paint: laid on a grey sheet (on white it cannot be seen); **dark** = how far it is from the grey either way.

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 8 % → 5 % | 24.4 px | 0.14 | 0.64 | 67 |
| heavy line | 14 % → 6 % | 39.7 px | 0.14 | 0.47 | 66 |
| pressure swell | 10 % → 6 % | 38.6 px | 0.14 | 0.60 | 62 |
| fast wave | 28 % → 7 % | 32.2 px | 0.14 | 0.25 | 187 |
| slow wave | 27 % → 8 % | 31.4 px | 0.14 | 0.29 | 340 |
| spiral | 38 % → 8 % | 24.8 px | 0.14 | 0.22 | 314 |
| loop | 22 % → 8 % | 28.6 px | 0.14 | 0.35 | 159 |
| tilted | 9 % → 9 % | 23.8 px | 0.14 | 1.01 | 102 |
| over the wet one | 20 % → 13 % | 31.1 px | 0.14 | 0.66 | 75 |
| long, no reload | 40 % → 9 % | 17.9 px | 0.14 | 0.24 | 452 | quarters: 0.07 → 0.04 → 0.01 → 0.01

Numbers say: light vs heavy: width 24.4 → 39.7 px, dark 0.14 → 0.14.

## Oil — alla prima
Oil · 30 px · 19.6 s

![Oil — alla prima](Oil-alla-prima.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 9 % → 9 % | 27.6 px | 0.51 | 1.00 | 87 |
| heavy line | 10 % → 10 % | 30.3 px | 0.51 | 1.00 | 90 |
| pressure swell | 8 % → 8 % | 29.8 px | 0.53 | 1.00 | 61 |
| fast wave | 24 % → 24 % | 28.1 px | 0.51 | 1.00 | 209 |
| slow wave | 26 % → 26 % | 29.5 px | 0.51 | 1.00 | 362 |
| spiral | 40 % → 40 % | 26.4 px | 0.50 | 1.00 | 355 |
| loop | 21 % → 21 % | 27.6 px | 0.52 | 1.00 | 186 |
| tilted | 11 % → 11 % | 30.4 px | 0.51 | 1.00 | 106 |
| over the wet one | 20 % → 20 % | 26.5 px | 0.51 | 1.00 | 86 |
| long, no reload | 49 % → 49 % | 22.0 px | 0.50 | 1.00 | 522 | quarters: 0.32 → 0.28 → 0.25 → 0.22

Numbers say: light vs heavy: width 27.6 → 30.3 px, dark 0.51 → 0.51; pressure barely changes the width.

## Oil — impasto
Oil · 34 px · 17.8 s

![Oil — impasto](Oil-impasto.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 12 % → 12 % | 33.4 px | 0.25 | 1.00 | 88 |
| heavy line | 12 % → 12 % | 36.3 px | 0.25 | 1.00 | 95 |
| pressure swell | 10 % → 10 % | 35.9 px | 0.26 | 1.00 | 74 |
| fast wave | 30 % → 30 % | 35.1 px | 0.25 | 1.00 | 249 |
| slow wave | 31 % → 31 % | 35.7 px | 0.25 | 1.00 | 415 |
| spiral | 52 % → 52 % | 34.0 px | 0.23 | 1.00 | 446 |
| loop | 26 % → 26 % | 33.7 px | 0.24 | 1.00 | 218 |
| tilted | 12 % → 12 % | 32.8 px | 0.26 | 1.00 | 130 |
| over the wet one | 23 % → 23 % | 31.9 px | 0.26 | 1.00 | 106 |
| long, no reload | 60 % → 60 % | 26.9 px | 0.22 | 1.00 | 628 | quarters: 0.18 → 0.16 → 0.13 → 0.10

Numbers say: light vs heavy: width 33.4 → 36.3 px, dark 0.25 → 0.25; pressure barely changes the width.

## Oil — glaze
Oil · 40 px · 13.9 s

![Oil — glaze](Oil-glaze.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 9 % → 9 % | 25.4 px | 0.50 | 1.00 | 88 |
| heavy line | 13 % → 13 % | 36.3 px | 0.49 | 1.00 | 108 |
| pressure swell | 9 % → 9 % | 35.3 px | 0.50 | 1.00 | 79 |
| fast wave | 26 % → 26 % | 30.1 px | 0.48 | 1.00 | 263 |
| slow wave | 29 % → 29 % | 33.7 px | 0.49 | 1.00 | 425 |
| spiral | 44 % → 44 % | 29.0 px | 0.49 | 1.00 | 419 |
| loop | 23 % → 23 % | 30.2 px | 0.50 | 1.00 | 220 |
| tilted | 10 % → 10 % | 28.9 px | 0.50 | 1.00 | 127 |
| over the wet one | 22 % → 22 % | 31.6 px | 0.50 | 1.00 | 96 |
| long, no reload | 51 % → 51 % | 22.7 px | 0.49 | 1.00 | 626 | quarters: 0.33 → 0.29 → 0.26 → 0.22

Numbers say: light vs heavy: width 25.4 → 36.3 px, dark 0.50 → 0.49.

## Oil — scumble
Oil · 36 px · 18.5 s

![Oil — scumble](Oil-scumble.png)

A light paint: laid on a grey sheet (on white it cannot be seen); **dark** = how far it is from the grey either way.

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 11 % → 11 % | 33.1 px | 0.08 | 1.00 | 104 |
| heavy line | 12 % → 12 % | 36.1 px | 0.07 | 1.00 | 123 |
| pressure swell | 9 % → 9 % | 35.5 px | 0.07 | 1.00 | 85 |
| fast wave | 26 % → 26 % | 29.6 px | 0.06 | 1.00 | 295 |
| slow wave | 27 % → 27 % | 30.9 px | 0.05 | 1.00 | 511 |
| spiral | 41 % → 41 % | 27.1 px | 0.04 | 1.00 | 526 |
| loop | 24 % → 24 % | 30.6 px | 0.06 | 1.00 | 267 |
| tilted | 11 % → 11 % | 30.4 px | 0.07 | 1.00 | 152 |
| over the wet one | 22 % → 22 % | 31.4 px | 0.07 | 1.00 | 129 |
| long, no reload | 45 % → 45 % | 20.3 px | 0.04 | 1.00 | 767 | quarters: 0.04 → 0.02 → 0.01 → 0.00

Numbers say: light vs heavy: width 33.1 → 36.1 px, dark 0.08 → 0.07; pressure barely changes the width.

## Acrylic — heavy body
Heavy acrylic · 30 px · 13.4 s

![Acrylic — heavy body](Acrylic-heavy-body.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 10 % → 9 % | 28.9 px | 0.51 | 0.91 | 82 |
| heavy line | 11 % → 10 % | 31.1 px | 0.51 | 0.93 | 82 |
| pressure swell | 8 % → 8 % | 30.7 px | 0.53 | 0.94 | 63 |
| fast wave | 23 % → 15 % | 26.5 px | 0.52 | 0.64 | 205 |
| slow wave | 24 % → 16 % | 27.7 px | 0.51 | 0.65 | 339 |
| spiral | 35 % → 15 % | 23.3 px | 0.51 | 0.43 | 347 |
| loop | 21 % → 16 % | 26.9 px | 0.51 | 0.76 | 182 |
| tilted | 9 % → 9 % | 24.9 px | 0.52 | 0.99 | 105 |
| over the wet one | 19 % → 17 % | 27.7 px | 0.52 | 0.89 | 82 |
| long, no reload | 39 % → 16 % | 17.3 px | 0.51 | 0.41 | 490 | quarters: 0.29 → 0.20 → 0.12 → 0.04

Numbers say: light vs heavy: width 28.9 → 31.1 px, dark 0.51 → 0.51; pressure barely changes the width.

## Acrylic — fluid
Watercolor · 36 px · 25.7 s

![Acrylic — fluid](Acrylic-fluid.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 8 % → 8 % | 22.6 px | 0.06 | 1.03 | 62 |
| heavy line | 12 % → 12 % | 35.0 px | 0.05 | 0.99 | 72 |
| pressure swell | 7 % → 7 % | 27.4 px | 0.06 | 0.99 | 52 |
| fast wave | 25 % → 24 % | 28.7 px | 0.05 | 0.95 | 180 |
| slow wave | 23 % → 23 % | 26.9 px | 0.06 | 1.01 | 310 |
| spiral | 36 % → 35 % | 23.6 px | 0.05 | 0.97 | 307 |
| loop | 21 % → 22 % | 27.2 px | 0.06 | 1.03 | 160 |
| tilted | 8 % → 9 % | 22.5 px | 0.06 | 1.12 | 95 |
| over the wet one | 19 % → 19 % | 30.7 px | 0.06 | 1.01 | 70 |
| long, no reload | 41 % → 40 % | 18.3 px | 0.05 | 0.98 | 437 | quarters: 0.04 → 0.03 → 0.02 → 0.01

Numbers say: light vs heavy: width 22.6 → 35.0 px, dark 0.06 → 0.05.

## Acrylic — palette knife
Heavy acrylic · 42 px · 18.7 s

![Acrylic — palette knife](Acrylic-palette-knife.png)

A light paint: laid on a grey sheet (on white it cannot be seen); **dark** = how far it is from the grey either way.

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 15 % → 15 % | 44.0 px | 0.06 | 0.98 | 20 |
| heavy line | 15 % → 15 % | 44.2 px | 0.05 | 0.97 | 20 |
| pressure swell | 12 % → 12 % | 43.5 px | 0.07 | 0.99 | 10 |
| fast wave | 36 % → 20 % | 41.9 px | 0.06 | 0.56 | 47 |
| slow wave | 37 % → 21 % | 42.6 px | 0.06 | 0.57 | 90 |
| spiral | 50 % → 18 % | 32.8 px | 0.07 | 0.37 | 80 |
| loop | 32 % → 24 % | 41.2 px | 0.06 | 0.75 | 40 |
| tilted | 12 % → 12 % | 33.6 px | 0.06 | 1.00 | 19 |
| over the wet one | 26 % → 25 % | 39.7 px | 0.06 | 0.97 | 16 |
| long, no reload | 57 % → 21 % | 25.7 px | 0.06 | 0.36 | 125 | quarters: 0.04 → 0.02 → 0.00 → 0.00

Numbers say: light vs heavy: width 44.0 → 44.2 px, dark 0.06 → 0.05; pressure barely changes the width.

## Finger on oil
Oil · 30 px · 12.3 s

![Finger on oil](Finger-on-oil.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 8 % → 8 % | 23.7 px | 0.40 | 1.00 | 49 |
| heavy line | 13 % → 13 % | 36.5 px | 0.38 | 1.00 | 68 |
| pressure swell | 9 % → 9 % | 33.3 px | 0.41 | 1.00 | 41 |
| fast wave | 22 % → 22 % | 26.0 px | 0.35 | 1.00 | 126 |
| slow wave | 24 % → 24 % | 27.8 px | 0.35 | 1.00 | 206 |
| spiral | 36 % → 36 % | 23.5 px | 0.27 | 1.00 | 199 |
| loop | 21 % → 21 % | 27.3 px | 0.36 | 1.00 | 103 |
| tilted | 9 % → 9 % | 26.4 px | 0.39 | 1.00 | 70 |
| over the wet one | 20 % → 20 % | 29.3 px | 0.39 | 1.00 | 52 |
| long, no reload | 36 % → 36 % | 16.3 px | 0.26 | 1.00 | 298 | quarters: 0.23 → 0.11 → 0.05 → 0.02

Numbers say: light vs heavy: width 23.7 → 36.5 px, dark 0.40 → 0.38.

## Palette knife — oil
Oil · 44 px · 17.9 s

![Palette knife — oil](Palette-knife-oil.png)

A light paint: laid on a grey sheet (on white it cannot be seen); **dark** = how far it is from the grey either way.

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 16 % → 16 % | 45.6 px | 0.12 | 1.00 | 21 |
| heavy line | 16 % → 16 % | 46.3 px | 0.11 | 1.00 | 22 |
| pressure swell | 12 % → 12 % | 45.2 px | 0.12 | 1.00 | 8 |
| fast wave | 39 % → 39 % | 44.9 px | 0.11 | 1.00 | 45 |
| slow wave | 39 % → 39 % | 45.4 px | 0.11 | 1.00 | 92 |
| spiral | 62 % → 62 % | 40.9 px | 0.08 | 1.00 | 90 |
| loop | 34 % → 34 % | 43.8 px | 0.11 | 1.00 | 36 |
| tilted | 13 % → 13 % | 36.6 px | 0.11 | 1.00 | 18 |
| over the wet one | 28 % → 28 % | 40.8 px | 0.11 | 1.00 | 21 |
| long, no reload | 74 % → 74 % | 33.1 px | 0.08 | 1.00 | 152 | quarters: 0.10 → 0.07 → 0.05 → 0.04

Numbers say: light vs heavy: width 45.6 → 46.3 px, dark 0.12 → 0.11; pressure barely changes the width.

## 0.45 · Sponge
Watercolor · 46 px · 20.4 s

![0.45 · Sponge](0-45-Sponge.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 9 % → 0 % | 26.5 px | 0.00 | 0.00 | 44 |
| heavy line | 12 % → 0 % | 35.5 px | 0.00 | 0.00 | 73 |
| pressure swell | 8 % → 0 % | 30.7 px | 0.01 | 0.05 | 43 |
| fast wave | 18 % → 0 % | 20.4 px | 0.01 | 0.02 | 125 |
| slow wave | 25 % → 3 % | 29.0 px | 0.02 | 0.14 | 255 |
| spiral | 31 % → 5 % | 20.2 px | 0.02 | 0.17 | 246 |
| loop | 21 % → 2 % | 27.1 px | 0.02 | 0.12 | 125 |
| tilted | 8 % → 10 % | 23.1 px | 0.05 | 1.17 | 104 |
| over the wet one | 19 % → 6 % | 29.5 px | 0.05 | 0.31 | 61 |
| long, no reload | 36 % → 8 % | 16.1 px | 0.02 | 0.22 | 356 | quarters: 0.01 → 0.01 → 0.01 → 0.01

Numbers say: light vs heavy: width 26.5 → 35.5 px, dark 0.00 → 0.00.

## 0.45 · Eraser
Eraser · 30 px · 18.2 s · over bands of wet oil paint and oil pastel in turn (it works on paint already there: look at what it does to the bands; covered counts the bands too)

![0.45 · Eraser](0-45-Eraser.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 24 % → 24 % | 69.2 px | 0.82 | 1.00 | 34 |
| heavy line | 23 % → 23 % | 67.4 px | 0.81 | 1.00 | 49 |
| pressure swell | 23 % → 23 % | 86.7 px | 0.82 | 1.00 | 30 |
| fast wave | 21 % → 21 % | 24.7 px | 0.81 | 1.00 | 119 |
| slow wave | 20 % → 20 % | 23.5 px | 0.82 | 1.00 | 187 |
| spiral | 20 % → 20 % | 13.5 px | 0.79 | 1.00 | 215 |
| loop | 21 % → 21 % | 27.8 px | 0.80 | 1.00 | 105 |
| tilted | 23 % → 23 % | 64.8 px | 0.81 | 1.00 | 49 |
| over the wet one | 22 % → 22 % | 0.0 px | 0.81 | 1.00 | 42 |
| long, no reload | 17 % → 17 % | 7.5 px | 0.79 | 1.00 | 276 | quarters: 0.13 → 0.16 → 0.13 → 0.17

Numbers say: light vs heavy: width 69.2 → 67.4 px, dark 0.82 → 0.81; pressure barely changes the width; the long stroke does not run out of paint.

## Lift wet paint
Eraser · 30 px · 17.8 s · over bands of wet oil paint and oil pastel in turn (it works on paint already there: look at what it does to the bands; covered counts the bands too)

![Lift wet paint](Lift-wet-paint.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 24 % → 24 % | 70.1 px | 0.82 | 1.00 | 26 |
| heavy line | 24 % → 24 % | 69.8 px | 0.82 | 1.00 | 32 |
| pressure swell | 24 % → 24 % | 89.5 px | 0.82 | 1.00 | 24 |
| fast wave | 24 % → 24 % | 27.7 px | 0.82 | 1.00 | 87 |
| slow wave | 24 % → 24 % | 27.7 px | 0.82 | 1.00 | 150 |
| spiral | 24 % → 24 % | 15.9 px | 0.82 | 1.00 | 155 |
| loop | 24 % → 24 % | 31.1 px | 0.82 | 1.00 | 80 |
| tilted | 24 % → 24 % | 66.8 px | 0.82 | 1.00 | 45 |
| over the wet one | 24 % → 24 % | 0.0 px | 0.82 | 1.00 | 38 |
| long, no reload | 24 % → 24 % | 10.7 px | 0.82 | 1.00 | 219 | quarters: 0.18 → 0.24 → 0.17 → 0.24

Numbers say: light vs heavy: width 70.1 → 69.8 px, dark 0.82 → 0.82; pressure barely changes the width; the long stroke does not run out of paint.

## Sgraffito
Eraser · 10 px · 17.2 s · over bands of wet oil paint and oil pastel in turn (it works on paint already there: look at what it does to the bands; covered counts the bands too)

![Sgraffito](Sgraffito.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 24 % → 24 % | 69.5 px | 0.81 | 1.00 | 5 |
| heavy line | 24 % → 24 % | 69.5 px | 0.82 | 1.00 | 8 |
| pressure swell | 24 % → 24 % | 89.5 px | 0.82 | 1.00 | 6 |
| fast wave | 24 % → 24 % | 27.4 px | 0.82 | 1.00 | 17 |
| slow wave | 24 % → 24 % | 27.4 px | 0.81 | 1.00 | 17 |
| spiral | 24 % → 24 % | 15.7 px | 0.81 | 1.00 | 28 |
| loop | 24 % → 24 % | 30.9 px | 0.82 | 1.00 | 16 |
| tilted | 24 % → 24 % | 66.6 px | 0.82 | 1.00 | 8 |
| over the wet one | 24 % → 24 % | 0.0 px | 0.82 | 1.00 | 5 |
| long, no reload | 24 % → 24 % | 10.6 px | 0.82 | 1.00 | 44 | quarters: 0.17 → 0.24 → 0.17 → 0.24

Numbers say: light vs heavy: width 69.5 → 69.5 px, dark 0.81 → 0.82; pressure barely changes the width; the long stroke does not run out of paint.

## Brush Artist · Refs · #01 Henry Ward peach cloud
Gouache · 44 px · 25.7 s

![Brush Artist · Refs · #01 Henry Ward peach cloud](Brush-Artist-Refs-01-Henry-Ward-peach-cloud.png)

A light paint: laid on a grey sheet (on white it cannot be seen); **dark** = how far it is from the grey either way.

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 14 % → 7 % | 41.5 px | 0.10 | 0.49 | 121 |
| heavy line | 16 % → 9 % | 45.0 px | 0.10 | 0.58 | 128 |
| pressure swell | 12 % → 7 % | 43.4 px | 0.10 | 0.64 | 93 |
| fast wave | 37 % → 11 % | 42.2 px | 0.10 | 0.29 | 336 |
| slow wave | 36 % → 11 % | 41.9 px | 0.10 | 0.30 | 575 |
| spiral | 57 % → 11 % | 37.7 px | 0.10 | 0.20 | 564 |
| loop | 31 % → 12 % | 40.5 px | 0.10 | 0.38 | 300 |
| tilted | 12 % → 13 % | 34.7 px | 0.10 | 1.01 | 157 |
| over the wet one | 26 % → 18 % | 39.2 px | 0.10 | 0.66 | 138 |
| long, no reload | 64 % → 15 % | 28.8 px | 0.10 | 0.23 | 814 | quarters: 0.07 → 0.04 → 0.01 → 0.00

Numbers say: light vs heavy: width 41.5 → 45.0 px, dark 0.10 → 0.10; pressure barely changes the width.

## Brush Artist · Refs · #02 Henry Ward cream strokes
Gouache · 46 px · 25.5 s

![Brush Artist · Refs · #02 Henry Ward cream strokes](Brush-Artist-Refs-02-Henry-Ward-cream-strokes.png)

A light paint: laid on a grey sheet (on white it cannot be seen); **dark** = how far it is from the grey either way.

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 13 % → 6 % | 38.3 px | 0.03 | 0.44 | 128 |
| heavy line | 14 % → 9 % | 41.9 px | 0.03 | 0.63 | 146 |
| pressure swell | 11 % → 8 % | 40.3 px | 0.03 | 0.71 | 92 |
| fast wave | 34 % → 10 % | 39.6 px | 0.03 | 0.30 | 347 |
| slow wave | 34 % → 11 % | 39.4 px | 0.03 | 0.31 | 591 |
| spiral | 55 % → 12 % | 36.6 px | 0.03 | 0.21 | 592 |
| loop | 30 % → 12 % | 38.7 px | 0.03 | 0.39 | 304 |
| tilted | 12 % → 13 % | 34.8 px | 0.03 | 1.01 | 169 |
| over the wet one | 26 % → 18 % | 36.5 px | 0.03 | 0.69 | 136 |
| long, no reload | 62 % → 14 % | 28.0 px | 0.03 | 0.23 | 863 | quarters: 0.02 → 0.02 → 0.01 → 0.00

Numbers say: light vs heavy: width 38.3 → 41.9 px, dark 0.03 → 0.03; pressure barely changes the width.

## Brush Artist · Refs · #03 Henry Ward navy contours
Heavy acrylic · 22 px · 12.9 s

![Brush Artist · Refs · #03 Henry Ward navy contours](Brush-Artist-Refs-03-Henry-Ward-navy-contours.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 7 % → 7 % | 21.5 px | 0.70 | 0.94 | 64 |
| heavy line | 8 % → 8 % | 23.4 px | 0.70 | 0.95 | 72 |
| pressure swell | 6 % → 6 % | 23.2 px | 0.73 | 0.94 | 52 |
| fast wave | 19 % → 12 % | 21.8 px | 0.72 | 0.66 | 179 |
| slow wave | 19 % → 13 % | 22.4 px | 0.72 | 0.69 | 275 |
| spiral | 30 % → 13 % | 19.5 px | 0.72 | 0.45 | 287 |
| loop | 17 % → 13 % | 21.4 px | 0.72 | 0.81 | 152 |
| tilted | 8 % → 8 % | 22.6 px | 0.71 | 1.00 | 81 |
| over the wet one | 16 % → 14 % | 21.2 px | 0.71 | 0.89 | 69 |
| long, no reload | 34 % → 14 % | 15.1 px | 0.72 | 0.40 | 426 | quarters: 0.35 → 0.29 → 0.20 → 0.08

Numbers say: light vs heavy: width 21.5 → 23.4 px, dark 0.70 → 0.70; pressure barely changes the width.

## Brush Artist · Refs · #04 Henry Ward grey cloud
Gouache · 50 px · 27.2 s

![Brush Artist · Refs · #04 Henry Ward grey cloud](Brush-Artist-Refs-04-Henry-Ward-grey-cloud.png)

A light paint: laid on a grey sheet (on white it cannot be seen); **dark** = how far it is from the grey either way.

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 15 % → 6 % | 44.3 px | 0.10 | 0.41 | 142 |
| heavy line | 17 % → 10 % | 48.4 px | 0.10 | 0.59 | 148 |
| pressure swell | 12 % → 8 % | 46.7 px | 0.10 | 0.67 | 107 |
| fast wave | 39 % → 11 % | 44.9 px | 0.10 | 0.29 | 370 |
| slow wave | 39 % → 12 % | 44.8 px | 0.10 | 0.30 | 648 |
| spiral | 58 % → 13 % | 38.1 px | 0.10 | 0.23 | 798 |
| loop | 34 % → 13 % | 44.1 px | 0.10 | 0.39 | 358 |
| tilted | 14 % → 14 % | 37.8 px | 0.10 | 1.01 | 179 |
| over the wet one | 29 % → 20 % | 41.9 px | 0.10 | 0.69 | 155 |
| long, no reload | 68 % → 16 % | 30.6 px | 0.10 | 0.23 | 908 | quarters: 0.08 → 0.04 → 0.01 → 0.00

Numbers say: light vs heavy: width 44.3 → 48.4 px, dark 0.10 → 0.10; pressure barely changes the width.

## Brush Artist · Refs · #05 Henry Ward green in rust loops
Heavy acrylic · 20 px · 12.5 s

![Brush Artist · Refs · #05 Henry Ward green in rust loops](Brush-Artist-Refs-05-Henry-Ward-green-in-rust-loops.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 7 % → 6 % | 19.5 px | 0.55 | 0.94 | 69 |
| heavy line | 7 % → 7 % | 21.2 px | 0.55 | 0.94 | 67 |
| pressure swell | 6 % → 5 % | 21.5 px | 0.57 | 0.92 | 45 |
| fast wave | 17 % → 11 % | 19.7 px | 0.56 | 0.64 | 168 |
| slow wave | 18 % → 12 % | 20.3 px | 0.56 | 0.66 | 237 |
| spiral | 27 % → 12 % | 17.9 px | 0.55 | 0.42 | 299 |
| loop | 15 % → 12 % | 19.5 px | 0.55 | 0.80 | 153 |
| tilted | 8 % → 8 % | 21.7 px | 0.56 | 1.00 | 76 |
| over the wet one | 15 % → 13 % | 19.1 px | 0.56 | 0.87 | 64 |
| long, no reload | 30 % → 12 % | 13.4 px | 0.56 | 0.39 | 400 | quarters: 0.25 → 0.18 → 0.10 → 0.02

Numbers say: light vs heavy: width 19.5 → 21.2 px, dark 0.55 → 0.55; pressure barely changes the width.

## Brush Artist · Refs · #06 Henry Ward scrubbed grey
Gouache · 50 px · 26.3 s

![Brush Artist · Refs · #06 Henry Ward scrubbed grey](Brush-Artist-Refs-06-Henry-Ward-scrubbed-grey.png)

A light paint: laid on a grey sheet (on white it cannot be seen); **dark** = how far it is from the grey either way.

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 15 % → 6 % | 44.3 px | 0.09 | 0.41 | 139 |
| heavy line | 17 % → 10 % | 48.4 px | 0.09 | 0.59 | 146 |
| pressure swell | 12 % → 8 % | 46.7 px | 0.09 | 0.67 | 114 |
| fast wave | 39 % → 11 % | 44.9 px | 0.09 | 0.29 | 403 |
| slow wave | 39 % → 12 % | 44.8 px | 0.09 | 0.30 | 656 |
| spiral | 58 % → 13 % | 38.1 px | 0.09 | 0.23 | 703 |
| loop | 34 % → 13 % | 44.1 px | 0.09 | 0.39 | 438 |
| tilted | 14 % → 14 % | 37.8 px | 0.09 | 1.01 | 196 |
| over the wet one | 29 % → 20 % | 41.9 px | 0.09 | 0.69 | 154 |
| long, no reload | 68 % → 16 % | 30.6 px | 0.08 | 0.23 | 1021 | quarters: 0.06 → 0.04 → 0.01 → 0.00

Numbers say: light vs heavy: width 44.3 → 48.4 px, dark 0.09 → 0.09; pressure barely changes the width.

## Brush Artist · Refs · #07 Henry Ward blue L + black zigzag
Heavy acrylic · 34 px · 14.4 s

![Brush Artist · Refs · #07 Henry Ward blue L + black zigzag](Brush-Artist-Refs-07-Henry-Ward-blue-L-black-zigzag.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 11 % → 11 % | 33.1 px | 0.57 | 0.93 | 86 |
| heavy line | 12 % → 11 % | 35.7 px | 0.57 | 0.93 | 97 |
| pressure swell | 9 % → 9 % | 35.2 px | 0.59 | 0.94 | 61 |
| fast wave | 29 % → 20 % | 33.6 px | 0.59 | 0.69 | 230 |
| slow wave | 30 % → 21 % | 34.1 px | 0.58 | 0.73 | 401 |
| spiral | 47 % → 22 % | 31.3 px | 0.58 | 0.46 | 384 |
| loop | 25 % → 21 % | 32.7 px | 0.58 | 0.82 | 200 |
| tilted | 11 % → 11 % | 29.8 px | 0.58 | 1.00 | 114 |
| over the wet one | 22 % → 20 % | 31.7 px | 0.58 | 0.91 | 96 |
| long, no reload | 53 % → 22 % | 23.8 px | 0.59 | 0.42 | 519 | quarters: 0.40 → 0.32 → 0.21 → 0.10

Numbers say: light vs heavy: width 33.1 → 35.7 px, dark 0.57 → 0.57; pressure barely changes the width.

## Brush Artist · Refs · #08 Henry Ward olive bands
Gouache · 34 px · 21.4 s

![Brush Artist · Refs · #08 Henry Ward olive bands](Brush-Artist-Refs-08-Henry-Ward-olive-bands.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 9 % → 2 % | 24.9 px | 0.57 | 0.29 | 59 |
| heavy line | 12 % → 3 % | 34.0 px | 0.57 | 0.23 | 126 |
| pressure swell | 8 % → 3 % | 31.1 px | 0.57 | 0.39 | 76 |
| fast wave | 26 % → 4 % | 29.5 px | 0.57 | 0.16 | 231 |
| slow wave | 25 % → 4 % | 29.0 px | 0.57 | 0.16 | 457 |
| spiral | 39 % → 4 % | 25.7 px | 0.57 | 0.10 | 375 |
| loop | 22 % → 5 % | 28.9 px | 0.57 | 0.21 | 230 |
| tilted | 10 % → 10 % | 29.0 px | 0.57 | 0.98 | 117 |
| over the wet one | 21 % → 8 % | 28.5 px | 0.57 | 0.40 | 101 |
| long, no reload | 44 % → 6 % | 19.9 px | 0.57 | 0.13 | 585 | quarters: 0.35 → 0.26 → 0.16 → 0.08

Numbers say: light vs heavy: width 24.9 → 34.0 px, dark 0.57 → 0.57.

## Brush Artist · Refs · #09 Henry Ward white loops
Gouache · 46 px · 26.6 s

![Brush Artist · Refs · #09 Henry Ward white loops](Brush-Artist-Refs-09-Henry-Ward-white-loops.png)

A light paint: laid on a grey sheet (on white it cannot be seen); **dark** = how far it is from the grey either way.

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 13 % → 6 % | 38.3 px | 0.01 | 0.44 | 121 |
| heavy line | 14 % → 9 % | 41.9 px | 0.01 | 0.63 | 133 |
| pressure swell | 11 % → 8 % | 40.3 px | 0.01 | 0.71 | 95 |
| fast wave | 34 % → 10 % | 39.6 px | 0.01 | 0.30 | 364 |
| slow wave | 34 % → 11 % | 39.4 px | 0.01 | 0.31 | 625 |
| spiral | 55 % → 12 % | 36.6 px | 0.01 | 0.21 | 574 |
| loop | 30 % → 12 % | 38.7 px | 0.01 | 0.39 | 306 |
| tilted | 12 % → 13 % | 34.8 px | 0.01 | 1.01 | 154 |
| over the wet one | 26 % → 18 % | 36.5 px | 0.01 | 0.69 | 139 |
| long, no reload | 62 % → 14 % | 28.0 px | 0.02 | 0.23 | 867 | quarters: 0.01 → 0.02 → 0.01 → 0.00

Numbers say: light vs heavy: width 38.3 → 41.9 px, dark 0.01 → 0.01; pressure barely changes the width.

## Brush Artist · Refs · #10 Henry Ward maroon loops
Heavy acrylic · 30 px · 13.5 s

![Brush Artist · Refs · #10 Henry Ward maroon loops](Brush-Artist-Refs-10-Henry-Ward-maroon-loops.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 10 % → 9 % | 28.0 px | 0.70 | 0.94 | 91 |
| heavy line | 10 % → 10 % | 30.2 px | 0.69 | 0.95 | 127 |
| pressure swell | 8 % → 8 % | 30.0 px | 0.73 | 0.94 | 87 |
| fast wave | 24 % → 17 % | 28.3 px | 0.73 | 0.71 | 200 |
| slow wave | 25 % → 18 % | 29.0 px | 0.73 | 0.73 | 340 |
| spiral | 39 % → 18 % | 26.0 px | 0.72 | 0.47 | 345 |
| loop | 21 % → 18 % | 27.6 px | 0.72 | 0.85 | 200 |
| tilted | 10 % → 10 % | 27.9 px | 0.72 | 1.00 | 97 |
| over the wet one | 20 % → 18 % | 26.8 px | 0.72 | 0.91 | 92 |
| long, no reload | 46 % → 18 % | 20.6 px | 0.73 | 0.40 | 482 | quarters: 0.44 → 0.38 → 0.31 → 0.22

Numbers say: light vs heavy: width 28.0 → 30.2 px, dark 0.70 → 0.69; pressure barely changes the width.

## Brush Artist · Refs · #11 Henry Ward purple spun balls
Heavy acrylic · 36 px · 15.1 s

![Brush Artist · Refs · #11 Henry Ward purple spun balls](Brush-Artist-Refs-11-Henry-Ward-purple-spun-balls.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 12 % → 11 % | 34.1 px | 0.70 | 0.96 | 129 |
| heavy line | 13 % → 12 % | 36.6 px | 0.70 | 0.96 | 96 |
| pressure swell | 10 % → 9 % | 36.2 px | 0.74 | 0.95 | 76 |
| fast wave | 30 % → 23 % | 34.6 px | 0.73 | 0.75 | 242 |
| slow wave | 30 % → 24 % | 35.0 px | 0.73 | 0.79 | 388 |
| spiral | 49 % → 25 % | 32.3 px | 0.73 | 0.50 | 425 |
| loop | 26 % → 23 % | 33.4 px | 0.73 | 0.88 | 260 |
| tilted | 11 % → 11 % | 31.2 px | 0.72 | 1.00 | 120 |
| over the wet one | 23 % → 21 % | 32.1 px | 0.72 | 0.93 | 108 |
| long, no reload | 55 % → 24 % | 24.8 px | 0.73 | 0.44 | 608 | quarters: 0.51 → 0.46 → 0.39 → 0.28

Numbers say: light vs heavy: width 34.1 → 36.6 px, dark 0.70 → 0.70; pressure barely changes the width.

## Brush Artist · Refs · #12 Henry Ward black-olive cage
Gouache · 28 px · 20.8 s

![Brush Artist · Refs · #12 Henry Ward black-olive cage](Brush-Artist-Refs-12-Henry-Ward-black-olive-cage.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 7 % → 3 % | 21.0 px | 0.61 | 0.36 | 48 |
| heavy line | 9 % → 4 % | 26.2 px | 0.62 | 0.42 | 109 |
| pressure swell | 6 % → 4 % | 24.0 px | 0.62 | 0.62 | 58 |
| fast wave | 21 % → 4 % | 23.8 px | 0.62 | 0.20 | 203 |
| slow wave | 20 % → 4 % | 23.3 px | 0.62 | 0.21 | 329 |
| spiral | 32 % → 5 % | 21.4 px | 0.62 | 0.14 | 325 |
| loop | 18 % → 5 % | 22.8 px | 0.62 | 0.29 | 170 |
| tilted | 9 % → 9 % | 25.8 px | 0.62 | 0.97 | 93 |
| over the wet one | 17 % → 8 % | 21.8 px | 0.62 | 0.47 | 79 |
| long, no reload | 39 % → 6 % | 17.4 px | 0.62 | 0.15 | 496 | quarters: 0.32 → 0.26 → 0.19 → 0.10

Numbers say: light vs heavy: width 21.0 → 26.2 px, dark 0.61 → 0.62.

## Brush Artist · Refs · #13 Henry Ward blue streaky form
Gouache · 50 px · 26.8 s

![Brush Artist · Refs · #13 Henry Ward blue streaky form](Brush-Artist-Refs-13-Henry-Ward-blue-streaky-form.png)

A light paint: laid on a grey sheet (on white it cannot be seen); **dark** = how far it is from the grey either way.

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 15 % → 6 % | 44.3 px | 0.09 | 0.41 | 145 |
| heavy line | 17 % → 10 % | 48.4 px | 0.09 | 0.59 | 152 |
| pressure swell | 12 % → 8 % | 46.7 px | 0.09 | 0.67 | 97 |
| fast wave | 39 % → 11 % | 44.9 px | 0.09 | 0.29 | 398 |
| slow wave | 39 % → 12 % | 44.8 px | 0.09 | 0.30 | 651 |
| spiral | 58 % → 13 % | 38.1 px | 0.09 | 0.23 | 655 |
| loop | 34 % → 13 % | 44.1 px | 0.09 | 0.39 | 331 |
| tilted | 14 % → 14 % | 37.8 px | 0.09 | 1.01 | 195 |
| over the wet one | 29 % → 20 % | 41.9 px | 0.09 | 0.69 | 144 |
| long, no reload | 68 % → 16 % | 30.6 px | 0.09 | 0.23 | 954 | quarters: 0.07 → 0.04 → 0.01 → 0.00

Numbers say: light vs heavy: width 44.3 → 48.4 px, dark 0.09 → 0.09; pressure barely changes the width.

## Brush Artist · Refs · #14 Henry Ward olive totem
Heavy acrylic · 48 px · 16.5 s

![Brush Artist · Refs · #14 Henry Ward olive totem](Brush-Artist-Refs-14-Henry-Ward-olive-totem.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 15 % → 15 % | 44.8 px | 0.31 | 0.94 | 125 |
| heavy line | 16 % → 16 % | 47.7 px | 0.31 | 0.95 | 132 |
| pressure swell | 13 % → 12 % | 47.0 px | 0.32 | 0.95 | 93 |
| fast wave | 38 % → 30 % | 43.9 px | 0.30 | 0.79 | 334 |
| slow wave | 39 % → 31 % | 44.5 px | 0.30 | 0.81 | 584 |
| spiral | 58 % → 32 % | 38.1 px | 0.30 | 0.55 | 564 |
| loop | 33 % → 29 % | 42.6 px | 0.30 | 0.89 | 288 |
| tilted | 13 % → 13 % | 37.5 px | 0.31 | 1.00 | 177 |
| over the wet one | 28 % → 26 % | 41.1 px | 0.31 | 0.93 | 135 |
| long, no reload | 67 % → 33 % | 30.3 px | 0.30 | 0.49 | 797 | quarters: 0.25 → 0.18 → 0.10 → 0.03

Numbers say: light vs heavy: width 44.8 → 47.7 px, dark 0.31 → 0.31; pressure barely changes the width.

## Brush Artist · Refs · #15 Ultramarine brush script
Ink · 10 px · 22.4 s

![Brush Artist · Refs · #15 Ultramarine brush script](Brush-Artist-Refs-15-Ultramarine-brush-script.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 2 % → 5 % | 5.0 px | 0.53 | 2.62 | 34 |
| heavy line | 10 % → 10 % | 29.6 px | 0.66 | 1.00 | 75 |
| pressure swell | 6 % → 6 % | 20.8 px | 0.68 | 1.12 | 42 |
| fast wave | 18 % → 17 % | 20.2 px | 0.59 | 0.95 | 141 |
| slow wave | 14 % → 14 % | 16.1 px | 0.59 | 1.00 | 144 |
| spiral | 22 % → 18 % | 14.5 px | 0.54 | 0.82 | 224 |
| loop | 13 % → 14 % | 17.4 px | 0.61 | 1.02 | 120 |
| tilted | 6 % → 6 % | 15.5 px | 0.68 | 1.01 | 55 |
| over the wet one | 13 % → 13 % | 20.5 px | 0.68 | 1.04 | 59 |
| long, no reload | 33 % → 20 % | 14.8 px | 0.52 | 0.59 | 329 | quarters: 0.30 → 0.14 → 0.05 → 0.02

Numbers say: light vs heavy: width 5.0 → 29.6 px, dark 0.53 → 0.66; wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #18 Blue oil-stick scribbles
Pastel · 10 px · 9.0 s

![Brush Artist · Refs · #18 Blue oil-stick scribbles](Brush-Artist-Refs-18-Blue-oil-stick-scribbles.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 1 % → 1 % | 2.3 px | 0.51 | 1.00 | 24 |
| heavy line | 3 % → 3 % | 7.5 px | 0.53 | 1.00 | 23 |
| pressure swell | 2 % → 2 % | 6.0 px | 0.53 | 1.00 | 15 |
| fast wave | 5 % → 5 % | 5.9 px | 0.53 | 1.00 | 55 |
| slow wave | 4 % → 4 % | 5.2 px | 0.52 | 1.00 | 52 |
| spiral | 8 % → 8 % | 5.2 px | 0.52 | 1.00 | 77 |
| loop | 4 % → 4 % | 5.4 px | 0.52 | 1.00 | 37 |
| tilted | 2 % → 2 % | 5.6 px | 0.52 | 1.00 | 24 |
| over the wet one | 4 % → 4 % | 5.8 px | 0.52 | 1.00 | 21 |
| long, no reload | 12 % → 12 % | 5.4 px | 0.53 | 1.00 | 120 | quarters: 0.07 → 0.07 → 0.07 → 0.07

Numbers say: light vs heavy: width 2.3 → 7.5 px, dark 0.51 → 0.53; the long stroke does not run out of paint.

## Brush Artist · Refs · #20 Orange-red crayon scribble
Pastel · 14 px · 9.0 s

![Brush Artist · Refs · #20 Orange-red crayon scribble](Brush-Artist-Refs-20-Orange-red-crayon-scribble.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 1 % → 1 % | 3.0 px | 0.53 | 1.00 | 14 |
| heavy line | 4 % → 4 % | 10.9 px | 0.53 | 1.00 | 22 |
| pressure swell | 2 % → 2 % | 9.1 px | 0.53 | 1.00 | 16 |
| fast wave | 8 % → 8 % | 8.9 px | 0.53 | 1.00 | 55 |
| slow wave | 7 % → 7 % | 7.6 px | 0.53 | 1.00 | 62 |
| spiral | 11 % → 11 % | 7.2 px | 0.53 | 1.00 | 90 |
| loop | 6 % → 6 % | 7.5 px | 0.53 | 1.00 | 48 |
| tilted | 2 % → 2 % | 6.7 px | 0.53 | 1.00 | 27 |
| over the wet one | 5 % → 5 % | 8.2 px | 0.53 | 1.00 | 22 |
| long, no reload | 15 % → 15 % | 6.9 px | 0.53 | 1.00 | 166 | quarters: 0.09 → 0.09 → 0.09 → 0.09

Numbers say: light vs heavy: width 3.0 → 10.9 px, dark 0.53 → 0.53; the long stroke does not run out of paint.

## Brush Artist · Refs · #21 Gritty black contours
Gouache · 12 px · 18.4 s

![Brush Artist · Refs · #21 Gritty black contours](Brush-Artist-Refs-21-Gritty-black-contours.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 3 % → 0 % | 8.8 px | 0.79 | 0.14 | 49 |
| heavy line | 4 % → 0 % | 11.9 px | 0.79 | 0.10 | 87 |
| pressure swell | 3 % → 0 % | 11.7 px | 0.79 | 0.16 | 48 |
| fast wave | 7 % → 1 % | 8.4 px | 0.79 | 0.10 | 188 |
| slow wave | 8 % → 1 % | 8.9 px | 0.79 | 0.09 | 171 |
| spiral | 9 % → 1 % | 5.9 px | 0.79 | 0.10 | 295 |
| loop | 8 % → 1 % | 9.9 px | 0.79 | 0.09 | 157 |
| tilted | 4 % → 4 % | 10.9 px | 0.79 | 0.91 | 71 |
| over the wet one | 7 % → 1 % | 9.7 px | 0.79 | 0.18 | 76 |
| long, no reload | 7 % → 1 % | 3.3 px | 0.79 | 0.12 | 413 | quarters: 0.20 → 0.07 → 0.00 → 0.00

Numbers say: light vs heavy: width 8.8 → 11.9 px, dark 0.79 → 0.79.

## Brush Artist · Refs · #22 Bold black brush poster
Ink · 20 px · 23.8 s

![Brush Artist · Refs · #22 Bold black brush poster](Brush-Artist-Refs-22-Bold-black-brush-poster.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 3 % → 5 % | 9.5 px | 0.79 | 1.63 | 27 |
| heavy line | 15 % → 15 % | 44.6 px | 0.88 | 0.99 | 83 |
| pressure swell | 9 % → 9 % | 31.9 px | 0.87 | 1.04 | 48 |
| fast wave | 27 % → 26 % | 31.2 px | 0.87 | 0.98 | 136 |
| slow wave | 22 % → 21 % | 25.2 px | 0.87 | 0.98 | 201 |
| spiral | 34 % → 32 % | 22.2 px | 0.87 | 0.94 | 220 |
| loop | 20 % → 20 % | 26.2 px | 0.88 | 1.00 | 124 |
| tilted | 8 % → 8 % | 22.7 px | 0.88 | 1.01 | 66 |
| over the wet one | 19 % → 19 % | 30.5 px | 0.88 | 1.00 | 53 |
| long, no reload | 45 % → 38 % | 20.2 px | 0.86 | 0.84 | 346 | quarters: 0.54 → 0.45 → 0.35 → 0.27

Numbers say: light vs heavy: width 9.5 → 44.6 px, dark 0.79 → 0.88; wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #23 Dry white on orange + black line
Gouache · 50 px · 22.1 s

![Brush Artist · Refs · #23 Dry white on orange + black line](Brush-Artist-Refs-23-Dry-white-on-orange-black-line.png)

A light paint: laid on a grey sheet (on white it cannot be seen); **dark** = how far it is from the grey either way.

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 12 % → 2 % | 35.5 px | 0.01 | 0.15 | 75 |
| heavy line | 16 % → 2 % | 47.1 px | 0.01 | 0.12 | 201 |
| pressure swell | 11 % → 2 % | 42.9 px | 0.01 | 0.20 | 110 |
| fast wave | 35 % → 3 % | 40.0 px | 0.00 | 0.10 | 363 |
| slow wave | 34 % → 4 % | 39.1 px | 0.00 | 0.10 | 583 |
| spiral | 49 % → 4 % | 32.5 px | 0.00 | 0.08 | 564 |
| loop | 30 % → 4 % | 39.2 px | 0.00 | 0.13 | 321 |
| tilted | 13 % → 12 % | 35.4 px | 0.01 | 0.98 | 172 |
| over the wet one | 26 % → 8 % | 38.1 px | 0.01 | 0.29 | 140 |
| long, no reload | 58 % → 5 % | 25.9 px | 0.01 | 0.09 | 889 | quarters: 0.01 → 0.01 → 0.00 → 0.00

Numbers say: light vs heavy: width 35.5 → 47.1 px, dark 0.01 → 0.01.

## Brush Artist · Refs · #24 Picasso flat oil
Oil · 34 px · 18.2 s

![Brush Artist · Refs · #24 Picasso flat oil](Brush-Artist-Refs-24-Picasso-flat-oil.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 11 % → 11 % | 32.2 px | 0.39 | 1.00 | 101 |
| heavy line | 12 % → 12 % | 35.0 px | 0.39 | 1.00 | 119 |
| pressure swell | 9 % → 9 % | 34.4 px | 0.41 | 1.00 | 82 |
| fast wave | 30 % → 30 % | 34.2 px | 0.41 | 1.00 | 271 |
| slow wave | 30 % → 30 % | 34.9 px | 0.41 | 1.00 | 480 |
| spiral | 51 % → 51 % | 33.7 px | 0.40 | 1.00 | 494 |
| loop | 25 % → 25 % | 32.6 px | 0.41 | 1.00 | 248 |
| tilted | 11 % → 11 % | 32.0 px | 0.41 | 1.00 | 131 |
| over the wet one | 22 % → 22 % | 30.7 px | 0.41 | 1.00 | 120 |
| long, no reload | 61 % → 61 % | 27.6 px | 0.39 | 1.00 | 719 | quarters: 0.28 → 0.28 → 0.26 → 0.24

Numbers say: light vs heavy: width 32.2 → 35.0 px, dark 0.39 → 0.39; pressure barely changes the width.

## Brush Artist · Refs · #25 Yellow heavy flat stroke
Heavy acrylic · 110 px · 31.5 s

![Brush Artist · Refs · #25 Yellow heavy flat stroke](Brush-Artist-Refs-25-Yellow-heavy-flat-stroke.png)

A light paint: laid on a grey sheet (on white it cannot be seen); **dark** = how far it is from the grey either way.

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 35 % → 36 % | 101.3 px | 0.17 | 1.02 | 362 |
| heavy line | 36 % → 35 % | 105.0 px | 0.17 | 0.97 | 377 |
| pressure swell | 28 % → 29 % | 105.4 px | 0.17 | 1.04 | 251 |
| fast wave | 72 % → 76 % | 83.8 px | 0.17 | 1.05 | 957 |
| slow wave | 73 % → 72 % | 84.7 px | 0.18 | 0.98 | 1679 |
| spiral | 86 % → 83 % | 56.7 px | 0.17 | 0.97 | 1670 |
| loop | 65 % → 64 % | 83.6 px | 0.17 | 0.99 | 847 |
| tilted | 26 % → 26 % | 71.5 px | 0.17 | 1.00 | 457 |
| over the wet one | 55 % → 54 % | 83.1 px | 0.17 | 0.97 | 401 |
| long, no reload | 98 % → 97 % | 44.1 px | 0.17 | 0.99 | 2329 | quarters: 0.18 → 0.17 → 0.17 → 0.16

Numbers say: light vs heavy: width 101.3 → 105.0 px, dark 0.17 → 0.17; pressure barely changes the width; the long stroke does not run out of paint.

## Brush Artist · Refs · #27 Orange impasto swatch
Heavy acrylic · 60 px · 23.0 s

![Brush Artist · Refs · #27 Orange impasto swatch](Brush-Artist-Refs-27-Orange-impasto-swatch.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 20 % → 19 % | 56.7 px | 0.35 | 0.97 | 171 |
| heavy line | 20 % → 20 % | 59.3 px | 0.35 | 0.97 | 169 |
| pressure swell | 16 % → 15 % | 59.6 px | 0.36 | 0.97 | 118 |
| fast wave | 48 % → 46 % | 55.0 px | 0.35 | 0.98 | 432 |
| slow wave | 48 % → 47 % | 55.8 px | 0.36 | 0.98 | 753 |
| spiral | 69 % → 62 % | 45.5 px | 0.35 | 0.91 | 745 |
| loop | 42 % → 40 % | 53.8 px | 0.35 | 0.97 | 393 |
| tilted | 16 % → 16 % | 44.0 px | 0.36 | 1.00 | 221 |
| over the wet one | 34 % → 33 % | 50.6 px | 0.36 | 0.97 | 178 |
| long, no reload | 85 % → 75 % | 38.1 px | 0.35 | 0.88 | 1115 | quarters: 0.33 → 0.31 → 0.29 → 0.26

Numbers say: light vs heavy: width 56.7 → 59.3 px, dark 0.35 → 0.35; pressure barely changes the width.

## Brush Artist · Refs · #28 Miles Davis black lines
Ink · 22 px · 24.3 s

![Brush Artist · Refs · #28 Miles Davis black lines](Brush-Artist-Refs-28-Miles-Davis-black-lines.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 4 % → 6 % | 12.2 px | 0.81 | 1.48 | 36 |
| heavy line | 17 % → 17 % | 49.1 px | 0.88 | 0.99 | 82 |
| pressure swell | 10 % → 10 % | 35.9 px | 0.87 | 1.03 | 46 |
| fast wave | 30 % → 30 % | 35.0 px | 0.87 | 0.98 | 140 |
| slow wave | 25 % → 25 % | 28.5 px | 0.87 | 0.99 | 220 |
| spiral | 38 % → 37 % | 25.3 px | 0.87 | 0.96 | 242 |
| loop | 23 % → 23 % | 29.4 px | 0.88 | 1.00 | 131 |
| tilted | 9 % → 9 % | 25.0 px | 0.88 | 1.01 | 64 |
| over the wet one | 21 % → 21 % | 34.1 px | 0.88 | 1.00 | 58 |
| long, no reload | 51 % → 43 % | 22.7 px | 0.86 | 0.85 | 348 | quarters: 0.59 → 0.51 → 0.40 → 0.31

Numbers say: light vs heavy: width 12.2 → 49.1 px, dark 0.81 → 0.88.

## Brush Artist · Refs · #29 Shrigley magenta asterisk
Watercolor · 70 px · 28.6 s

![Brush Artist · Refs · #29 Shrigley magenta asterisk](Brush-Artist-Refs-29-Shrigley-magenta-asterisk.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 10 % → 13 % | 27.9 px | 0.22 | 1.36 | 47 |
| heavy line | 17 % → 18 % | 50.0 px | 0.22 | 1.03 | 120 |
| pressure swell | 11 % → 12 % | 40.9 px | 0.24 | 1.13 | 74 |
| fast wave | 38 % → 38 % | 43.4 px | 0.20 | 1.01 | 244 |
| slow wave | 35 % → 39 % | 40.8 px | 0.24 | 1.10 | 397 |
| spiral | 60 % → 61 % | 39.8 px | 0.20 | 1.01 | 386 |
| loop | 31 % → 32 % | 40.0 px | 0.23 | 1.03 | 218 |
| tilted | 17 % → 18 % | 48.6 px | 0.24 | 1.01 | 176 |
| over the wet one | 31 % → 34 % | 38.7 px | 0.24 | 1.08 | 93 |
| long, no reload | 74 % → 75 % | 33.1 px | 0.20 | 1.01 | 594 | quarters: 0.22 → 0.17 → 0.14 → 0.11

Numbers say: light vs heavy: width 27.9 → 50.0 px, dark 0.22 → 0.22.

## Brush Artist · Refs · #30 Red gouache face patch
Gouache · 60 px · 32.8 s

![Brush Artist · Refs · #30 Red gouache face patch](Brush-Artist-Refs-30-Red-gouache-face-patch.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 16 % → 15 % | 46.9 px | 0.49 | 0.91 | 130 |
| heavy line | 25 % → 20 % | 73.8 px | 0.49 | 0.80 | 180 |
| pressure swell | 19 % → 17 % | 72.6 px | 0.49 | 0.86 | 136 |
| fast wave | 48 % → 28 % | 55.1 px | 0.49 | 0.58 | 376 |
| slow wave | 48 % → 28 % | 55.3 px | 0.49 | 0.59 | 813 |
| spiral | 59 % → 28 % | 39.1 px | 0.49 | 0.48 | 654 |
| loop | 40 % → 29 % | 51.3 px | 0.49 | 0.74 | 319 |
| tilted | 16 % → 16 % | 45.7 px | 0.49 | 1.01 | 206 |
| over the wet one | 36 % → 32 % | 55.3 px | 0.49 | 0.88 | 158 |
| long, no reload | 67 % → 30 % | 30.0 px | 0.49 | 0.45 | 929 | quarters: 0.43 → 0.38 → 0.32 → 0.26

Numbers say: light vs heavy: width 46.9 → 73.8 px, dark 0.49 → 0.49.

## Brush Artist · Refs · #31 Warhol blotted line
Ink · 6 px · 19.6 s

![Brush Artist · Refs · #31 Warhol blotted line](Brush-Artist-Refs-31-Warhol-blotted-line.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 1 % → 3 % | 2.6 px | 0.75 | 3.30 | 27 |
| heavy line | 7 % → 7 % | 20.6 px | 0.83 | 0.97 | 47 |
| pressure swell | 4 % → 4 % | 14.8 px | 0.84 | 1.12 | 30 |
| fast wave | 12 % → 9 % | 13.8 px | 0.82 | 0.77 | 90 |
| slow wave | 10 % → 8 % | 11.2 px | 0.80 | 0.85 | 95 |
| spiral | 15 % → 9 % | 9.7 px | 0.80 | 0.58 | 164 |
| loop | 9 % → 9 % | 11.9 px | 0.80 | 0.94 | 83 |
| tilted | 3 % → 3 % | 8.6 px | 0.84 | 1.04 | 41 |
| over the wet one | 8 % → 8 % | 14.5 px | 0.84 | 1.02 | 40 |
| long, no reload | 21 % → 9 % | 9.6 px | 0.78 | 0.43 | 252 | quarters: 0.25 → 0.13 → 0.05 → 0.01

Numbers say: light vs heavy: width 2.6 → 20.6 px, dark 0.75 → 0.83; wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #32 Thick orange swipes
Heavy acrylic · 90 px · 27.0 s

![Brush Artist · Refs · #32 Thick orange swipes](Brush-Artist-Refs-32-Thick-orange-swipes.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 29 % → 29 % | 82.9 px | 0.38 | 1.00 | 256 |
| heavy line | 30 % → 29 % | 86.3 px | 0.38 | 0.97 | 264 |
| pressure swell | 23 % → 23 % | 86.5 px | 0.38 | 1.01 | 201 |
| fast wave | 63 % → 65 % | 73.1 px | 0.38 | 1.03 | 702 |
| slow wave | 64 % → 63 % | 73.5 px | 0.39 | 0.98 | 1217 |
| spiral | 79 % → 77 % | 52.2 px | 0.38 | 0.98 | 1180 |
| loop | 57 % → 56 % | 73.4 px | 0.38 | 0.99 | 622 |
| tilted | 21 % → 21 % | 59.3 px | 0.38 | 1.00 | 315 |
| over the wet one | 47 % → 45 % | 70.7 px | 0.38 | 0.97 | 276 |
| long, no reload | 95 % → 93 % | 42.7 px | 0.38 | 0.98 | 1725 | quarters: 0.38 → 0.38 → 0.37 → 0.35

Numbers say: light vs heavy: width 82.9 → 86.3 px, dark 0.38 → 0.38; pressure barely changes the width; the long stroke does not run out of paint.

## Brush Artist · Refs · #33 Red wet-in-wet band
Watercolor · 80 px · 34.8 s

![Brush Artist · Refs · #33 Red wet-in-wet band](Brush-Artist-Refs-33-Red-wet-in-wet-band.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 22 % → 22 % | 64.0 px | 0.36 | 1.02 | 118 |
| heavy line | 34 % → 33 % | 97.7 px | 0.33 | 0.99 | 226 |
| pressure swell | 22 % → 23 % | 82.8 px | 0.36 | 1.04 | 137 |
| fast wave | 64 % → 67 % | 74.4 px | 0.31 | 1.05 | 432 |
| slow wave | 63 % → 63 % | 72.3 px | 0.44 | 1.00 | 724 |
| spiral | 77 % → 77 % | 50.6 px | 0.41 | 1.01 | 701 |
| loop | 54 % → 55 % | 70.5 px | 0.38 | 1.00 | 369 |
| tilted | 24 % → 24 % | 65.8 px | 0.40 | 1.01 | 242 |
| over the wet one | 49 % → 52 % | 70.0 px | 0.40 | 1.06 | 163 |
| long, no reload | 95 % → 96 % | 42.7 px | 0.40 | 1.01 | 1030 | quarters: 0.49 → 0.46 → 0.40 → 0.29

Numbers say: light vs heavy: width 64.0 → 97.7 px, dark 0.36 → 0.33.

## Brush Artist · Refs · #34 Magenta oil patches
Oil · 60 px · 21.0 s

![Brush Artist · Refs · #34 Magenta oil patches](Brush-Artist-Refs-34-Magenta-oil-patches.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 19 % → 19 % | 55.6 px | 0.59 | 1.00 | 180 |
| heavy line | 21 % → 21 % | 59.7 px | 0.59 | 1.00 | 203 |
| pressure swell | 16 % → 16 % | 58.8 px | 0.62 | 1.01 | 142 |
| fast wave | 48 % → 49 % | 55.4 px | 0.62 | 1.02 | 475 |
| slow wave | 48 % → 48 % | 55.8 px | 0.62 | 1.00 | 841 |
| spiral | 70 % → 70 % | 46.3 px | 0.62 | 1.00 | 882 |
| loop | 42 % → 42 % | 54.2 px | 0.62 | 1.00 | 455 |
| tilted | 17 % → 17 % | 46.8 px | 0.62 | 1.00 | 247 |
| over the wet one | 35 % → 35 % | 50.0 px | 0.62 | 1.00 | 194 |
| long, no reload | 86 % → 86 % | 38.7 px | 0.62 | 1.00 | 1275 | quarters: 0.59 → 0.58 → 0.57 → 0.52

Numbers say: light vs heavy: width 55.6 → 59.7 px, dark 0.59 → 0.59; pressure barely changes the width; the long stroke does not run out of paint.

## Brush Artist · Refs · #35 Red band with runs
Watercolor · 70 px · 33.3 s

![Brush Artist · Refs · #35 Red band with runs](Brush-Artist-Refs-35-Red-band-with-runs.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 19 % → 21 % | 56.2 px | 0.31 | 1.06 | 99 |
| heavy line | 30 % → 29 % | 86.9 px | 0.30 | 0.98 | 177 |
| pressure swell | 19 % → 20 % | 73.0 px | 0.33 | 1.03 | 110 |
| fast wave | 59 % → 60 % | 68.3 px | 0.28 | 1.01 | 332 |
| slow wave | 57 % → 58 % | 66.0 px | 0.39 | 1.01 | 565 |
| spiral | 73 % → 74 % | 48.4 px | 0.36 | 1.00 | 550 |
| loop | 50 % → 51 % | 64.8 px | 0.34 | 1.02 | 296 |
| tilted | 21 % → 21 % | 59.1 px | 0.36 | 1.00 | 217 |
| over the wet one | 44 % → 47 % | 63.5 px | 0.36 | 1.08 | 139 |
| long, no reload | 93 % → 94 % | 41.8 px | 0.35 | 1.01 | 839 | quarters: 0.42 → 0.40 → 0.34 → 0.25

Numbers say: light vs heavy: width 56.2 → 86.9 px, dark 0.31 → 0.30.

## Brush Artist · Refs · #36 Magenta letters flat brush
Gouache · 36 px · 29.6 s

![Brush Artist · Refs · #36 Magenta letters flat brush](Brush-Artist-Refs-36-Magenta-letters-flat-brush.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 10 % → 10 % | 29.0 px | 0.45 | 0.98 | 72 |
| heavy line | 17 % → 14 % | 49.1 px | 0.45 | 0.85 | 97 |
| pressure swell | 13 % → 12 % | 49.4 px | 0.45 | 0.89 | 69 |
| fast wave | 35 % → 19 % | 40.3 px | 0.45 | 0.54 | 210 |
| slow wave | 35 % → 19 % | 39.9 px | 0.45 | 0.54 | 358 |
| spiral | 46 % → 19 % | 30.4 px | 0.45 | 0.42 | 349 |
| loop | 27 % → 20 % | 35.3 px | 0.45 | 0.72 | 182 |
| tilted | 11 % → 11 % | 29.8 px | 0.45 | 1.00 | 105 |
| over the wet one | 24 % → 22 % | 38.1 px | 0.45 | 0.92 | 92 |
| long, no reload | 46 % → 19 % | 20.8 px | 0.45 | 0.40 | 517 | quarters: 0.29 → 0.25 → 0.22 → 0.18

Numbers say: light vs heavy: width 29.0 → 49.1 px, dark 0.45 → 0.45.

## Brush Artist · Refs · #37 Oil still life dabs
Oil · 40 px · 18.3 s

![Brush Artist · Refs · #37 Oil still life dabs](Brush-Artist-Refs-37-Oil-still-life-dabs.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 13 % → 13 % | 37.9 px | 0.39 | 1.00 | 133 |
| heavy line | 14 % → 14 % | 41.1 px | 0.38 | 1.00 | 129 |
| pressure swell | 11 % → 11 % | 40.2 px | 0.40 | 1.00 | 94 |
| fast wave | 34 % → 34 % | 39.8 px | 0.40 | 1.00 | 322 |
| slow wave | 35 % → 35 % | 40.2 px | 0.39 | 1.00 | 560 |
| spiral | 59 % → 59 % | 38.7 px | 0.38 | 1.00 | 677 |
| loop | 29 % → 29 % | 37.8 px | 0.39 | 1.00 | 292 |
| tilted | 13 % → 13 % | 35.8 px | 0.39 | 1.00 | 160 |
| over the wet one | 26 % → 26 % | 35.6 px | 0.39 | 1.00 | 131 |
| long, no reload | 69 % → 69 % | 30.9 px | 0.37 | 1.00 | 835 | quarters: 0.31 → 0.30 → 0.28 → 0.24

Numbers say: light vs heavy: width 37.9 → 41.1 px, dark 0.39 → 0.38; pressure barely changes the width.

## Brush Artist · Refs · #38 Sanguine drawing
Pastel · 6 px · 8.3 s

![Brush Artist · Refs · #38 Sanguine drawing](Brush-Artist-Refs-38-Sanguine-drawing.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 1 % → 1 % | 1.6 px | 0.60 | 1.00 | 16 |
| heavy line | 2 % → 2 % | 4.7 px | 0.62 | 1.00 | 19 |
| pressure swell | 1 % → 1 % | 3.7 px | 0.62 | 1.00 | 14 |
| fast wave | 3 % → 3 % | 3.9 px | 0.61 | 1.00 | 30 |
| slow wave | 3 % → 3 % | 3.4 px | 0.61 | 1.00 | 30 |
| spiral | 5 % → 5 % | 3.4 px | 0.61 | 1.00 | 56 |
| loop | 3 % → 3 % | 3.5 px | 0.61 | 1.00 | 39 |
| tilted | 1 % → 1 % | 4.1 px | 0.62 | 1.00 | 18 |
| over the wet one | 3 % → 3 % | 3.5 px | 0.62 | 1.00 | 14 |
| long, no reload | 8 % → 8 % | 3.7 px | 0.61 | 1.00 | 75 | quarters: 0.06 → 0.06 → 0.06 → 0.06

Numbers say: light vs heavy: width 1.6 → 4.7 px, dark 0.60 → 0.62; the long stroke does not run out of paint.

## Brush Artist · Refs · #39 Very thick impasto
Heavy acrylic · 60 px · 21.4 s

![Brush Artist · Refs · #39 Very thick impasto](Brush-Artist-Refs-39-Very-thick-impasto.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 20 % → 19 % | 56.8 px | 0.61 | 0.97 | 168 |
| heavy line | 20 % → 20 % | 59.4 px | 0.61 | 0.97 | 178 |
| pressure swell | 16 % → 15 % | 59.6 px | 0.62 | 0.97 | 123 |
| fast wave | 48 % → 47 % | 55.2 px | 0.62 | 0.98 | 418 |
| slow wave | 48 % → 47 % | 56.0 px | 0.62 | 0.98 | 712 |
| spiral | 69 % → 65 % | 45.6 px | 0.62 | 0.93 | 725 |
| loop | 42 % → 41 % | 54.0 px | 0.62 | 0.97 | 365 |
| tilted | 16 % → 16 % | 44.0 px | 0.62 | 1.00 | 198 |
| over the wet one | 34 % → 33 % | 50.7 px | 0.62 | 0.97 | 175 |
| long, no reload | 85 % → 79 % | 38.3 px | 0.62 | 0.93 | 1027 | quarters: 0.58 → 0.57 → 0.55 → 0.52

Numbers say: light vs heavy: width 56.8 → 59.4 px, dark 0.61 → 0.61; pressure barely changes the width; the long stroke does not run out of paint.

## Brush Artist · Refs · #40 Watercolour blooms
Watercolor · 90 px · 38.0 s

![Brush Artist · Refs · #40 Watercolour blooms](Brush-Artist-Refs-40-Watercolour-blooms.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 25 % → 26 % | 72.6 px | 0.39 | 1.04 | 144 |
| heavy line | 38 % → 37 % | 109.5 px | 0.36 | 0.99 | 271 |
| pressure swell | 25 % → 26 % | 92.7 px | 0.40 | 1.06 | 159 |
| fast wave | 69 % → 73 % | 80.1 px | 0.36 | 1.05 | 492 |
| slow wave | 68 % → 68 % | 78.2 px | 0.48 | 1.00 | 831 |
| spiral | 80 % → 80 % | 52.6 px | 0.46 | 1.01 | 813 |
| loop | 59 % → 59 % | 75.9 px | 0.43 | 1.01 | 431 |
| tilted | 27 % → 27 % | 74.8 px | 0.43 | 1.00 | 304 |
| over the wet one | 54 % → 58 % | 76.9 px | 0.43 | 1.06 | 187 |
| long, no reload | 97 % → 98 % | 43.3 px | 0.46 | 1.01 | 1209 | quarters: 0.55 → 0.53 → 0.47 → 0.35

Numbers say: light vs heavy: width 72.6 → 109.5 px, dark 0.39 → 0.36.

## Brush Artist · Refs · #41 Coloured pencil hatching
Pastel · 4 px · 8.1 s

![Brush Artist · Refs · #41 Coloured pencil hatching](Brush-Artist-Refs-41-Coloured-pencil-hatching.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 0 % → 0 % | 1.3 px | 0.41 | 1.00 | 10 |
| heavy line | 1 % → 1 % | 3.5 px | 0.43 | 1.00 | 13 |
| pressure swell | 1 % → 1 % | 2.4 px | 0.44 | 1.00 | 10 |
| fast wave | 2 % → 2 % | 2.7 px | 0.42 | 1.00 | 25 |
| slow wave | 2 % → 2 % | 2.4 px | 0.42 | 1.00 | 23 |
| spiral | 4 % → 4 % | 2.5 px | 0.42 | 1.00 | 42 |
| loop | 2 % → 2 % | 2.6 px | 0.43 | 1.00 | 21 |
| tilted | 1 % → 1 % | 3.6 px | 0.42 | 1.00 | 13 |
| over the wet one | 2 % → 2 % | 2.8 px | 0.42 | 1.00 | 8 |
| long, no reload | 6 % → 6 % | 2.8 px | 0.43 | 1.00 | 64 | quarters: 0.03 → 0.03 → 0.03 → 0.03

Numbers say: light vs heavy: width 1.3 → 3.5 px, dark 0.41 → 0.43; the long stroke does not run out of paint.

## Brush Artist · Refs · #42 Oil pastel shaggy
Pastel · 18 px · 8.5 s

![Brush Artist · Refs · #42 Oil pastel shaggy](Brush-Artist-Refs-42-Oil-pastel-shaggy.png)

A light paint: laid on a grey sheet (on white it cannot be seen); **dark** = how far it is from the grey either way.

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 1 % → 1 % | 3.9 px | 0.07 | 1.00 | 16 |
| heavy line | 5 % → 5 % | 14.5 px | 0.08 | 1.00 | 21 |
| pressure swell | 3 % → 3 % | 11.1 px | 0.08 | 1.00 | 18 |
| fast wave | 10 % → 10 % | 11.2 px | 0.08 | 1.00 | 63 |
| slow wave | 8 % → 8 % | 9.5 px | 0.07 | 1.00 | 71 |
| spiral | 14 % → 14 % | 9.0 px | 0.08 | 1.00 | 94 |
| loop | 7 % → 7 % | 9.5 px | 0.08 | 1.00 | 52 |
| tilted | 3 % → 3 % | 8.3 px | 0.07 | 1.00 | 27 |
| over the wet one | 7 % → 7 % | 10.9 px | 0.07 | 1.00 | 24 |
| long, no reload | 19 % → 19 % | 8.5 px | 0.08 | 1.00 | 140 | quarters: 0.02 → 0.02 → 0.02 → 0.02

Numbers say: light vs heavy: width 3.9 → 14.5 px, dark 0.07 → 0.08; the long stroke does not run out of paint.

## Brush Artist · Refs · #43 Dragged black ink blocks
Gouache · 70 px · 27.6 s

![Brush Artist · Refs · #43 Dragged black ink blocks](Brush-Artist-Refs-43-Dragged-black-ink-blocks.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 19 % → 6 % | 55.7 px | 0.57 | 0.31 | 111 |
| heavy line | 24 % → 9 % | 69.2 px | 0.57 | 0.39 | 305 |
| pressure swell | 17 % → 9 % | 63.9 px | 0.57 | 0.54 | 164 |
| fast wave | 51 % → 12 % | 59.4 px | 0.57 | 0.23 | 525 |
| slow wave | 50 % → 10 % | 58.2 px | 0.57 | 0.21 | 880 |
| spiral | 65 % → 14 % | 42.6 px | 0.57 | 0.22 | 889 |
| loop | 45 % → 13 % | 58.3 px | 0.57 | 0.28 | 475 |
| tilted | 17 % → 17 % | 47.2 px | 0.57 | 0.98 | 265 |
| over the wet one | 37 % → 21 % | 55.6 px | 0.57 | 0.57 | 218 |
| long, no reload | 82 % → 17 % | 36.6 px | 0.57 | 0.21 | 1326 | quarters: 0.54 → 0.52 → 0.47 → 0.39

Numbers say: light vs heavy: width 55.7 → 69.2 px, dark 0.57 → 0.57.

## Brush Artist · Refs · #44 Blue looping ribbon
Oil · 80 px · 23.9 s

![Brush Artist · Refs · #44 Blue looping ribbon](Brush-Artist-Refs-44-Blue-looping-ribbon.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 26 % → 27 % | 74.8 px | 0.71 | 1.04 | 249 |
| heavy line | 27 % → 27 % | 79.6 px | 0.71 | 1.00 | 270 |
| pressure swell | 21 % → 21 % | 78.1 px | 0.72 | 1.03 | 195 |
| fast wave | 61 % → 64 % | 70.3 px | 0.73 | 1.05 | 710 |
| slow wave | 61 % → 61 % | 70.0 px | 0.73 | 1.00 | 1210 |
| spiral | 78 % → 78 % | 51.3 px | 0.73 | 1.00 | 1221 |
| loop | 54 % → 54 % | 69.7 px | 0.72 | 1.00 | 636 |
| tilted | 20 % → 20 % | 57.2 px | 0.71 | 1.00 | 335 |
| over the wet one | 44 % → 44 % | 64.9 px | 0.71 | 1.00 | 291 |
| long, no reload | 96 % → 96 % | 42.8 px | 0.73 | 1.00 | 1770 | quarters: 0.72 → 0.72 → 0.72 → 0.69

Numbers say: light vs heavy: width 74.8 → 79.6 px, dark 0.71 → 0.71; pressure barely changes the width; the long stroke does not run out of paint.

## Brush Artist · Refs · #45 Soft pastel pepper
Pastel · 40 px · 9.2 s

![Brush Artist · Refs · #45 Soft pastel pepper](Brush-Artist-Refs-45-Soft-pastel-pepper.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 3 % → 3 % | 7.9 px | 0.53 | 1.00 | 33 |
| heavy line | 11 % → 11 % | 31.1 px | 0.53 | 1.00 | 46 |
| pressure swell | 6 % → 6 % | 23.3 px | 0.53 | 1.00 | 29 |
| fast wave | 21 % → 21 % | 23.8 px | 0.53 | 1.00 | 109 |
| slow wave | 17 % → 17 % | 20.0 px | 0.53 | 1.00 | 197 |
| spiral | 29 % → 29 % | 19.0 px | 0.53 | 1.00 | 190 |
| loop | 15 % → 15 % | 19.5 px | 0.53 | 1.00 | 94 |
| tilted | 5 % → 5 % | 15.2 px | 0.53 | 1.00 | 54 |
| over the wet one | 13 % → 13 % | 22.2 px | 0.53 | 1.00 | 47 |
| long, no reload | 38 % → 38 % | 16.8 px | 0.53 | 1.00 | 269 | quarters: 0.23 → 0.22 → 0.22 → 0.23

Numbers say: light vs heavy: width 7.9 → 31.1 px, dark 0.53 → 0.53; the long stroke does not run out of paint.

## Brush Artist · Refs · #46 Red-brown ink lips
Watercolor · 70 px · 33.0 s

![Brush Artist · Refs · #46 Red-brown ink lips](Brush-Artist-Refs-46-Red-brown-ink-lips.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 19 % → 20 % | 56.2 px | 0.54 | 1.01 | 100 |
| heavy line | 30 % → 30 % | 86.9 px | 0.48 | 0.99 | 180 |
| pressure swell | 19 % → 20 % | 73.0 px | 0.53 | 1.03 | 107 |
| fast wave | 59 % → 61 % | 68.3 px | 0.46 | 1.04 | 329 |
| slow wave | 57 % → 57 % | 66.0 px | 0.60 | 1.00 | 585 |
| spiral | 73 % → 74 % | 48.4 px | 0.56 | 1.00 | 571 |
| loop | 50 % → 50 % | 64.8 px | 0.55 | 1.00 | 277 |
| tilted | 21 % → 21 % | 59.1 px | 0.56 | 1.01 | 204 |
| over the wet one | 44 % → 46 % | 63.7 px | 0.56 | 1.05 | 128 |
| long, no reload | 93 % → 94 % | 41.8 px | 0.55 | 1.01 | 882 | quarters: 0.64 → 0.61 → 0.54 → 0.41

Numbers say: light vs heavy: width 56.2 → 86.9 px, dark 0.54 → 0.48.

## Brush Artist · Refs · #47 Pink knife slabs
Heavy acrylic · 90 px · 24.6 s

![Brush Artist · Refs · #47 Pink knife slabs](Brush-Artist-Refs-47-Pink-knife-slabs.png)

A light paint: laid on a grey sheet (on white it cannot be seen); **dark** = how far it is from the grey either way.

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 28 % → 27 % | 81.0 px | 0.17 | 0.97 | 185 |
| heavy line | 29 % → 28 % | 83.4 px | 0.17 | 0.97 | 210 |
| pressure swell | 22 % → 22 % | 83.4 px | 0.18 | 1.01 | 134 |
| fast wave | 61 % → 60 % | 70.1 px | 0.17 | 0.98 | 515 |
| slow wave | 61 % → 59 % | 70.9 px | 0.17 | 0.96 | 894 |
| spiral | 76 % → 58 % | 50.0 px | 0.16 | 0.76 | 834 |
| loop | 55 % → 54 % | 71.7 px | 0.17 | 0.97 | 463 |
| tilted | 21 % → 21 % | 59.3 px | 0.17 | 1.00 | 247 |
| over the wet one | 46 % → 44 % | 67.9 px | 0.17 | 0.96 | 204 |
| long, no reload | 92 % → 76 % | 41.3 px | 0.16 | 0.83 | 1198 | quarters: 0.18 → 0.16 → 0.14 → 0.09

Numbers say: light vs heavy: width 81.0 → 83.4 px, dark 0.17 → 0.17; pressure barely changes the width.

## Brush Artist · Refs · #48 Black bands with drips
Gouache · 70 px · 37.3 s

![Brush Artist · Refs · #48 Black bands with drips](Brush-Artist-Refs-48-Black-bands-with-drips.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 19 % → 18 % | 54.6 px | 0.69 | 0.93 | 167 |
| heavy line | 29 % → 24 % | 83.0 px | 0.69 | 0.84 | 236 |
| pressure swell | 23 % → 21 % | 86.1 px | 0.69 | 0.92 | 152 |
| fast wave | 53 % → 36 % | 61.8 px | 0.69 | 0.68 | 493 |
| slow wave | 53 % → 36 % | 61.7 px | 0.69 | 0.67 | 837 |
| spiral | 64 % → 35 % | 41.9 px | 0.69 | 0.55 | 791 |
| loop | 45 % → 36 % | 57.8 px | 0.69 | 0.81 | 420 |
| tilted | 19 % → 19 % | 52.3 px | 0.69 | 1.00 | 250 |
| over the wet one | 41 % → 38 % | 62.4 px | 0.69 | 0.92 | 194 |
| long, no reload | 74 % → 37 % | 33.3 px | 0.69 | 0.50 | 1156 | quarters: 0.64 → 0.61 → 0.54 → 0.45

Numbers say: light vs heavy: width 54.6 → 83.0 px, dark 0.69 → 0.69.

## Brush Artist · Refs · #49 Magenta letters round brush
Ink · 30 px · 26.9 s

![Brush Artist · Refs · #49 Magenta letters round brush](Brush-Artist-Refs-49-Magenta-letters-round-brush.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 6 % → 8 % | 17.5 px | 0.50 | 1.28 | 36 |
| heavy line | 21 % → 21 % | 62.0 px | 0.51 | 0.99 | 105 |
| pressure swell | 12 % → 13 % | 46.3 px | 0.52 | 1.01 | 55 |
| fast wave | 38 % → 38 % | 44.3 px | 0.51 | 0.99 | 162 |
| slow wave | 32 % → 31 % | 36.4 px | 0.51 | 0.99 | 286 |
| spiral | 50 % → 48 % | 32.8 px | 0.51 | 0.97 | 287 |
| loop | 29 % → 29 % | 37.6 px | 0.51 | 1.00 | 147 |
| tilted | 11 % → 11 % | 30.7 px | 0.52 | 1.01 | 76 |
| over the wet one | 26 % → 26 % | 42.1 px | 0.52 | 1.01 | 71 |
| long, no reload | 61 % → 56 % | 27.5 px | 0.51 | 0.92 | 453 | quarters: 0.41 → 0.36 → 0.30 → 0.25

Numbers say: light vs heavy: width 17.5 → 62.0 px, dark 0.50 → 0.51.

## Brush Artist · Refs · #50 Thick swipes on photo
Heavy acrylic · 40 px · 16.0 s

![Brush Artist · Refs · #50 Thick swipes on photo](Brush-Artist-Refs-50-Thick-swipes-on-photo.png)

A light paint: laid on a grey sheet (on white it cannot be seen); **dark** = how far it is from the grey either way.

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 13 % → 13 % | 38.0 px | 0.21 | 0.96 | 103 |
| heavy line | 14 % → 13 % | 40.1 px | 0.21 | 0.96 | 114 |
| pressure swell | 11 % → 10 % | 40.1 px | 0.22 | 0.95 | 76 |
| fast wave | 33 % → 31 % | 38.3 px | 0.21 | 0.93 | 259 |
| slow wave | 34 % → 32 % | 39.1 px | 0.20 | 0.95 | 460 |
| spiral | 58 % → 47 % | 38.5 px | 0.20 | 0.80 | 448 |
| loop | 28 % → 27 % | 36.8 px | 0.20 | 0.95 | 232 |
| tilted | 12 % → 12 % | 34.0 px | 0.22 | 1.00 | 126 |
| over the wet one | 25 % → 24 % | 35.2 px | 0.22 | 0.95 | 101 |
| long, no reload | 66 % → 46 % | 29.5 px | 0.20 | 0.70 | 654 | quarters: 0.16 → 0.13 → 0.11 → 0.07

Numbers say: light vs heavy: width 38.0 → 40.1 px, dark 0.21 → 0.21; pressure barely changes the width.

## Brush Artist · Ink — wash
Watercolor · 38 px · 28.0 s

![Brush Artist · Ink — wash](Brush-Artist-Ink-wash.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 11 % → 11 % | 31.6 px | 0.39 | 1.03 | 52 |
| heavy line | 19 % → 19 % | 54.3 px | 0.32 | 1.03 | 87 |
| pressure swell | 12 % → 12 % | 45.1 px | 0.37 | 1.04 | 53 |
| fast wave | 39 % → 41 % | 44.7 px | 0.30 | 1.05 | 167 |
| slow wave | 37 % → 38 % | 42.6 px | 0.37 | 1.04 | 286 |
| spiral | 57 % → 60 % | 37.9 px | 0.30 | 1.04 | 294 |
| loop | 32 % → 33 % | 41.8 px | 0.35 | 1.02 | 147 |
| tilted | 13 % → 14 % | 36.8 px | 0.38 | 1.04 | 94 |
| over the wet one | 29 % → 30 % | 42.8 px | 0.38 | 1.04 | 67 |
| long, no reload | 65 % → 70 % | 29.2 px | 0.29 | 1.08 | 436 | quarters: 0.34 → 0.26 → 0.18 → 0.12

Numbers say: light vs heavy: width 31.6 → 54.3 px, dark 0.39 → 0.32.

## Brush Artist · Ink — brush line
Ink · 16 px · 24.0 s

![Brush Artist · Ink — brush line](Brush-Artist-Ink-brush-line.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 3 % → 5 % | 7.7 px | 0.78 | 1.80 | 92 |
| heavy line | 13 % → 13 % | 39.0 px | 0.88 | 0.99 | 77 |
| pressure swell | 8 % → 8 % | 28.4 px | 0.87 | 1.05 | 43 |
| fast wave | 24 % → 23 % | 27.6 px | 0.87 | 0.96 | 123 |
| slow wave | 19 % → 19 % | 22.5 px | 0.87 | 0.97 | 160 |
| spiral | 30 % → 27 % | 19.9 px | 0.86 | 0.90 | 217 |
| loop | 18 % → 18 % | 23.4 px | 0.88 | 1.00 | 117 |
| tilted | 7 % → 7 % | 20.1 px | 0.88 | 1.01 | 54 |
| over the wet one | 17 % → 17 % | 26.8 px | 0.88 | 1.00 | 56 |
| long, no reload | 42 % → 31 % | 18.8 px | 0.85 | 0.73 | 338 | quarters: 0.49 → 0.40 → 0.30 → 0.21

Numbers say: light vs heavy: width 7.7 → 39.0 px, dark 0.78 → 0.88; wet paint spreads well beyond the stroke.

## Brush Artist · Ink — dry brush
Gouache · 30 px · 19.7 s

![Brush Artist · Ink — dry brush](Brush-Artist-Ink-dry-brush.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 8 % → 1 % | 21.9 px | 0.71 | 0.13 | 59 |
| heavy line | 10 % → 1 % | 27.7 px | 0.71 | 0.11 | 120 |
| pressure swell | 7 % → 2 % | 25.7 px | 0.71 | 0.23 | 70 |
| fast wave | 21 % → 2 % | 24.3 px | 0.71 | 0.10 | 200 |
| slow wave | 21 % → 2 % | 23.9 px | 0.71 | 0.09 | 345 |
| spiral | 31 % → 2 % | 20.4 px | 0.71 | 0.07 | 339 |
| loop | 18 % → 2 % | 23.9 px | 0.71 | 0.13 | 190 |
| tilted | 9 % → 8 % | 24.3 px | 0.71 | 0.96 | 95 |
| over the wet one | 17 % → 4 % | 22.9 px | 0.71 | 0.25 | 86 |
| long, no reload | 31 % → 3 % | 13.7 px | 0.71 | 0.09 | 544 | quarters: 0.38 → 0.31 → 0.21 → 0.08

Numbers say: light vs heavy: width 21.9 → 27.7 px, dark 0.71 → 0.71.

## Brush Artist · Watercolour — blue
Watercolor · 40 px · 24.7 s

![Brush Artist · Watercolour — blue](Brush-Artist-Watercolour-blue.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 6 % → 10 % | 16.7 px | 0.27 | 1.71 | 30 |
| heavy line | 11 % → 12 % | 31.4 px | 0.27 | 1.13 | 59 |
| pressure swell | 7 % → 9 % | 25.4 px | 0.29 | 1.33 | 36 |
| fast wave | 24 % → 25 % | 27.6 px | 0.25 | 1.06 | 127 |
| slow wave | 22 % → 27 % | 25.8 px | 0.28 | 1.22 | 205 |
| spiral | 38 % → 41 % | 25.0 px | 0.24 | 1.09 | 203 |
| loop | 19 % → 22 % | 25.2 px | 0.28 | 1.13 | 105 |
| tilted | 12 % → 12 % | 33.1 px | 0.28 | 1.00 | 99 |
| over the wet one | 21 % → 24 % | 24.7 px | 0.28 | 1.15 | 51 |
| long, no reload | 51 % → 54 % | 22.8 px | 0.23 | 1.05 | 316 | quarters: 0.20 → 0.15 → 0.11 → 0.09

Numbers say: light vs heavy: width 16.7 → 31.4 px, dark 0.27 → 0.27; wet paint spreads well beyond the stroke.

## Brush Artist · Watercolour — violet
Watercolor · 40 px · 24.3 s

![Brush Artist · Watercolour — violet](Brush-Artist-Watercolour-violet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 6 % → 10 % | 16.7 px | 0.18 | 1.71 | 29 |
| heavy line | 11 % → 12 % | 31.4 px | 0.18 | 1.13 | 57 |
| pressure swell | 7 % → 9 % | 25.4 px | 0.19 | 1.33 | 33 |
| fast wave | 24 % → 25 % | 27.6 px | 0.17 | 1.06 | 125 |
| slow wave | 22 % → 27 % | 25.8 px | 0.19 | 1.22 | 204 |
| spiral | 38 % → 41 % | 25.0 px | 0.16 | 1.09 | 207 |
| loop | 19 % → 22 % | 25.2 px | 0.19 | 1.13 | 119 |
| tilted | 12 % → 12 % | 33.1 px | 0.19 | 1.00 | 85 |
| over the wet one | 21 % → 24 % | 24.7 px | 0.19 | 1.15 | 50 |
| long, no reload | 51 % → 54 % | 22.8 px | 0.16 | 1.05 | 330 | quarters: 0.13 → 0.10 → 0.08 → 0.06

Numbers say: light vs heavy: width 16.7 → 31.4 px, dark 0.18 → 0.18; wet paint spreads well beyond the stroke.

## Brush Artist · Watercolour — teal
Watercolor · 40 px · 25.0 s

![Brush Artist · Watercolour — teal](Brush-Artist-Watercolour-teal.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 6 % → 10 % | 16.7 px | 0.29 | 1.71 | 26 |
| heavy line | 11 % → 12 % | 31.4 px | 0.29 | 1.13 | 66 |
| pressure swell | 7 % → 9 % | 25.4 px | 0.31 | 1.33 | 37 |
| fast wave | 24 % → 25 % | 27.6 px | 0.27 | 1.06 | 127 |
| slow wave | 22 % → 27 % | 25.8 px | 0.30 | 1.22 | 204 |
| spiral | 38 % → 41 % | 25.0 px | 0.26 | 1.09 | 210 |
| loop | 19 % → 22 % | 25.2 px | 0.30 | 1.13 | 110 |
| tilted | 12 % → 12 % | 33.1 px | 0.30 | 1.00 | 91 |
| over the wet one | 21 % → 24 % | 24.7 px | 0.30 | 1.15 | 51 |
| long, no reload | 51 % → 54 % | 22.8 px | 0.25 | 1.05 | 316 | quarters: 0.21 → 0.16 → 0.12 → 0.09

Numbers say: light vs heavy: width 16.7 → 31.4 px, dark 0.29 → 0.29; wet paint spreads well beyond the stroke.

## Brush Artist · Gouache
Gouache · 30 px · 27.8 s

![Brush Artist · Gouache](Brush-Artist-Gouache.png)

A light paint: laid on a grey sheet (on white it cannot be seen); **dark** = how far it is from the grey either way.

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 8 % → 8 % | 24.4 px | 0.16 | 0.97 | 70 |
| heavy line | 15 % → 11 % | 42.8 px | 0.16 | 0.78 | 75 |
| pressure swell | 11 % → 9 % | 41.0 px | 0.16 | 0.84 | 49 |
| fast wave | 30 % → 13 % | 34.4 px | 0.16 | 0.45 | 172 |
| slow wave | 29 % → 14 % | 33.9 px | 0.16 | 0.46 | 306 |
| spiral | 40 % → 14 % | 26.6 px | 0.16 | 0.35 | 300 |
| loop | 23 % → 15 % | 30.4 px | 0.16 | 0.62 | 156 |
| tilted | 10 % → 10 % | 27.1 px | 0.16 | 1.01 | 121 |
| over the wet one | 21 % → 19 % | 32.8 px | 0.16 | 0.89 | 94 |
| long, no reload | 43 % → 15 % | 19.1 px | 0.16 | 0.35 | 411 | quarters: 0.10 → 0.07 → 0.04 → 0.02

Numbers say: light vs heavy: width 24.4 → 42.8 px, dark 0.16 → 0.16.

## Brush Artist · Oil — bristle
Oil · 30 px · 16.9 s

![Brush Artist · Oil — bristle](Brush-Artist-Oil-bristle.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 9 % → 9 % | 26.2 px | 0.54 | 1.00 | 91 |
| heavy line | 10 % → 10 % | 28.5 px | 0.54 | 1.00 | 147 |
| pressure swell | 8 % → 8 % | 28.2 px | 0.55 | 1.00 | 86 |
| fast wave | 24 % → 24 % | 27.3 px | 0.55 | 1.00 | 259 |
| slow wave | 24 % → 24 % | 28.2 px | 0.55 | 1.00 | 449 |
| spiral | 39 % → 39 % | 25.6 px | 0.54 | 1.00 | 436 |
| loop | 20 % → 20 % | 26.2 px | 0.54 | 1.00 | 220 |
| tilted | 11 % → 11 % | 29.9 px | 0.54 | 1.00 | 136 |
| over the wet one | 20 % → 20 % | 25.2 px | 0.54 | 1.00 | 106 |
| long, no reload | 50 % → 50 % | 22.4 px | 0.54 | 1.00 | 653 | quarters: 0.32 → 0.30 → 0.29 → 0.28

Numbers say: light vs heavy: width 26.2 → 28.5 px, dark 0.54 → 0.54; pressure barely changes the width; the long stroke does not run out of paint.

## Brush Artist · Charcoal — stick
Charcoal · 30 px · 9.0 s

![Brush Artist · Charcoal — stick](Brush-Artist-Charcoal-stick.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 3 % → 3 % | 8.5 px | 0.84 | 1.00 | 21 |
| heavy line | 9 % → 9 % | 26.2 px | 0.85 | 1.00 | 38 |
| pressure swell | 5 % → 5 % | 19.2 px | 0.85 | 1.00 | 18 |
| fast wave | 18 % → 18 % | 20.2 px | 0.85 | 1.00 | 51 |
| slow wave | 15 % → 15 % | 17.4 px | 0.85 | 1.00 | 79 |
| spiral | 27 % → 27 % | 17.5 px | 0.85 | 1.00 | 72 |
| loop | 14 % → 14 % | 18.0 px | 0.85 | 1.00 | 39 |
| tilted | 5 % → 5 % | 15.2 px | 0.85 | 1.00 | 26 |
| over the wet one | 12 % → 12 % | 19.3 px | 0.85 | 1.00 | 20 |
| long, no reload | 39 % → 39 % | 17.3 px | 0.85 | 1.00 | 132 | quarters: 0.37 → 0.35 → 0.36 → 0.37

Numbers say: light vs heavy: width 8.5 → 26.2 px, dark 0.84 → 0.85; the long stroke does not run out of paint.

## Brush Artist · Refs · #01 Henry Ward peach cloud — own sheet
own sheet 600 × 600 · Gouache · 44 px · 12.1 s

![Brush Artist · Refs · #01 Henry Ward peach cloud — own sheet](Brush-Artist-Refs-01-Henry-Ward-peach-cloud-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 34 % → 41 % | 44.5 px | 0.11 | 1.19 | 137 |
| stroke 2 | 40 % → 55 % | 65.0 px | 0.11 | 1.36 | 129 |
| stroke 3 | 44 % → 65 % | 58.0 px | 0.11 | 1.47 | 136 |
| stroke 4 | 48 % → 61 % | 78.4 px | 0.11 | 1.27 | 127 |
| stroke 5 | 40 % → 61 % | 54.6 px | 0.11 | 1.50 | 147 |
| stroke 6 | 48 % → 49 % | 71.2 px | 0.11 | 1.02 | 126 |
| stroke 7 | 32 % → 57 % | 44.2 px | 0.10 | 1.80 | 128 |
| stroke 8 | 37 % → 60 % | 47.8 px | 0.10 | 1.63 | 160 |
| stroke 9 | 45 % → 67 % | 56.7 px | 0.10 | 1.46 | 151 |
| stroke 10 | 51 % → 72 % | 63.7 px | 0.10 | 1.42 | 147 |
| stroke 11 | 52 % → 75 % | 72.1 px | 0.10 | 1.43 | 136 |
| stroke 12 | 61 % → 87 % | 83.3 px | 0.10 | 1.42 | 152 |
| stroke 13 | 61 % → 84 % | 80.5 px | 0.11 | 1.39 | 147 |
| stroke 14 | 59 % → 84 % | 76.8 px | 0.11 | 1.42 | 137 |
| stroke 15 | 66 % → 86 % | 89.4 px | 0.11 | 1.30 | 142 |
| stroke 16 | 71 % → 89 % | 99.9 px | 0.11 | 1.24 | 137 |
| stroke 17 | 68 % → 85 % | 84.6 px | 0.11 | 1.25 | 145 |
| stroke 18 | 70 % → 85 % | 91.7 px | 0.11 | 1.22 | 137 |
| stroke 19 | 73 % → 85 % | 90.1 px | 0.11 | 1.17 | 141 |
| stroke 20 | 73 % → 82 % | 95.7 px | 0.11 | 1.14 | 151 |
| stroke 21 | 73 % → 77 % | 97.6 px | 0.11 | 1.06 | 152 |
| stroke 22 | 75 % → 78 % | 101.1 px | 0.11 | 1.04 | 146 |
| stroke 23 | 74 % → 74 % | 94.8 px | 0.11 | 0.99 | 141 |
| stroke 24 | 79 % → 78 % | 106.5 px | 0.11 | 0.98 | 124 |

Numbers say: wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #02 Henry Ward cream strokes — own sheet
own sheet 600 × 600 · Gouache · 46 px · 7.2 s

![Brush Artist · Refs · #02 Henry Ward cream strokes — own sheet](Brush-Artist-Refs-02-Henry-Ward-cream-strokes-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 32 % → 29 % | 41.1 px | 0.03 | 0.93 | 197 |
| stroke 2 | 35 % → 28 % | 50.1 px | 0.03 | 0.80 | 190 |
| stroke 3 | 30 % → 33 % | 41.5 px | 0.03 | 1.10 | 211 |
| stroke 4 | 36 % → 49 % | 50.3 px | 0.03 | 1.35 | 207 |
| stroke 5 | 53 % → 47 % | 69.0 px | 0.03 | 0.89 | 207 |
| stroke 6 | 34 % → 42 % | 41.1 px | 0.03 | 1.24 | 189 |
| stroke 7 | 46 % → 40 % | 59.1 px | 0.03 | 0.87 | 186 |

## Brush Artist · Refs · #03 Henry Ward navy contours — own sheet
own sheet 600 × 600 · Heavy acrylic · 22 px · 2.4 s

![Brush Artist · Refs · #03 Henry Ward navy contours — own sheet](Brush-Artist-Refs-03-Henry-Ward-navy-contours-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 15 % → 20 % | 23.1 px | 0.75 | 1.28 | 101 |
| stroke 2 | 28 % → 30 % | 26.3 px | 0.75 | 1.09 | 85 |
| stroke 3 | 28 % → 28 % | 29.4 px | 0.75 | 0.99 | 121 |
| stroke 4 | 26 % → 24 % | 45.9 px | 0.75 | 0.92 | 129 |

## Brush Artist · Refs · #04 Henry Ward grey cloud — own sheet
own sheet 600 × 600 · Gouache · 50 px · 12.2 s

![Brush Artist · Refs · #04 Henry Ward grey cloud — own sheet](Brush-Artist-Refs-04-Henry-Ward-grey-cloud-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 31 % → 57 % | 47.2 px | 0.12 | 1.82 | 189 |
| stroke 2 | 37 % → 61 % | 57.0 px | 0.12 | 1.65 | 217 |
| stroke 3 | 57 % → 79 % | 78.8 px | 0.12 | 1.38 | 199 |
| stroke 4 | 58 % → 82 % | 86.4 px | 0.12 | 1.42 | 214 |
| stroke 5 | 60 % → 85 % | 89.6 px | 0.12 | 1.41 | 196 |
| stroke 6 | 61 % → 88 % | 97.1 px | 0.12 | 1.45 | 193 |
| stroke 7 | 59 % → 83 % | 86.6 px | 0.12 | 1.41 | 198 |
| stroke 8 | 56 % → 83 % | 84.7 px | 0.12 | 1.49 | 201 |
| stroke 9 | 58 % → 85 % | 86.7 px | 0.12 | 1.46 | 205 |
| stroke 10 | 61 % → 87 % | 97.0 px | 0.12 | 1.44 | 194 |
| stroke 11 | 61 % → 85 % | 82.2 px | 0.12 | 1.40 | 199 |
| stroke 12 | 62 % → 85 % | 93.6 px | 0.12 | 1.38 | 195 |
| stroke 13 | 61 % → 85 % | 83.0 px | 0.12 | 1.40 | 190 |
| stroke 14 | 60 % → 83 % | 92.2 px | 0.12 | 1.39 | 215 |
| stroke 15 | 58 % → 82 % | 86.1 px | 0.12 | 1.40 | 211 |
| stroke 16 | 60 % → 83 % | 95.0 px | 0.12 | 1.38 | 207 |
| stroke 17 | 59 % → 83 % | 82.7 px | 0.12 | 1.42 | 191 |
| stroke 18 | 60 % → 81 % | 95.6 px | 0.12 | 1.36 | 188 |
| stroke 19 | 59 % → 60 % | 87.8 px | 0.12 | 1.01 | 193 |
| stroke 20 | 61 % → 58 % | 98.5 px | 0.12 | 0.96 | 212 |

Numbers say: wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #05 Henry Ward green in rust loops — own sheet
own sheet 600 × 600 · Heavy acrylic · 20 px · 2.2 s

![Brush Artist · Refs · #05 Henry Ward green in rust loops — own sheet](Brush-Artist-Refs-05-Henry-Ward-green-in-rust-loops-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 16 % → 24 % | 20.9 px | 0.57 | 1.48 | 112 |
| stroke 2 | 15 % → 13 % | 22.7 px | 0.58 | 0.90 | 136 |
| stroke 3 | 25 % → 24 % | 37.1 px | 0.58 | 0.94 | 111 |

## Brush Artist · Refs · #06 Henry Ward scrubbed grey — own sheet
own sheet 600 × 600 · Gouache · 50 px · 13.3 s

![Brush Artist · Refs · #06 Henry Ward scrubbed grey — own sheet](Brush-Artist-Refs-06-Henry-Ward-scrubbed-grey-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 33 % → 56 % | 47.0 px | 0.10 | 1.68 | 202 |
| stroke 2 | 41 % → 62 % | 63.4 px | 0.10 | 1.53 | 192 |
| stroke 3 | 57 % → 88 % | 83.9 px | 0.10 | 1.53 | 197 |
| stroke 4 | 58 % → 87 % | 91.7 px | 0.10 | 1.51 | 193 |
| stroke 5 | 55 % → 85 % | 81.9 px | 0.10 | 1.56 | 192 |
| stroke 6 | 59 % → 85 % | 91.8 px | 0.10 | 1.44 | 195 |
| stroke 7 | 60 % → 83 % | 86.9 px | 0.10 | 1.39 | 206 |
| stroke 8 | 61 % → 87 % | 97.1 px | 0.10 | 1.43 | 201 |
| stroke 9 | 59 % → 87 % | 86.6 px | 0.10 | 1.48 | 188 |
| stroke 10 | 58 % → 88 % | 94.3 px | 0.10 | 1.50 | 200 |
| stroke 11 | 58 % → 83 % | 84.2 px | 0.10 | 1.43 | 189 |
| stroke 12 | 57 % → 82 % | 92.4 px | 0.10 | 1.43 | 196 |
| stroke 13 | 57 % → 82 % | 81.1 px | 0.10 | 1.45 | 205 |
| stroke 14 | 55 % → 83 % | 83.9 px | 0.10 | 1.49 | 203 |
| stroke 15 | 57 % → 84 % | 81.4 px | 0.10 | 1.47 | 199 |
| stroke 16 | 62 % → 89 % | 95.3 px | 0.10 | 1.44 | 173 |
| stroke 17 | 60 % → 85 % | 87.3 px | 0.10 | 1.43 | 197 |
| stroke 18 | 60 % → 84 % | 94.3 px | 0.10 | 1.39 | 204 |
| stroke 19 | 56 % → 84 % | 85.7 px | 0.10 | 1.49 | 201 |
| stroke 20 | 57 % → 82 % | 92.3 px | 0.10 | 1.44 | 204 |
| stroke 21 | 57 % → 65 % | 82.8 px | 0.10 | 1.15 | 204 |
| stroke 22 | 61 % → 59 % | 97.1 px | 0.10 | 0.96 | 180 |

Numbers say: wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #07 Henry Ward blue L + black zigzag — own sheet
own sheet 600 × 600 · Heavy acrylic · 34 px · 1.8 s

![Brush Artist · Refs · #07 Henry Ward blue L + black zigzag — own sheet](Brush-Artist-Refs-07-Henry-Ward-blue-L-black-zigzag-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 30 % → 31 % | 35.6 px | 0.63 | 1.05 | 110 |
| stroke 2 | 31 % → 29 % | 38.6 px | 0.63 | 0.94 | 79 |

## Brush Artist · Refs · #08 Henry Ward olive bands — own sheet
own sheet 600 × 600 · Gouache · 34 px · 5.1 s

![Brush Artist · Refs · #08 Henry Ward olive bands — own sheet](Brush-Artist-Refs-08-Henry-Ward-olive-bands-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 33 % → 19 % | 32.4 px | 0.61 | 0.58 | 154 |
| stroke 2 | 37 % → 20 % | 44.5 px | 0.61 | 0.52 | 153 |
| stroke 3 | 31 % → 23 % | 32.5 px | 0.61 | 0.75 | 156 |
| stroke 4 | 38 % → 37 % | 44.4 px | 0.61 | 0.98 | 162 |
| stroke 5 | 50 % → 35 % | 52.6 px | 0.61 | 0.71 | 160 |
| stroke 6 | 36 % → 22 % | 32.4 px | 0.61 | 0.61 | 152 |

## Brush Artist · Refs · #09 Henry Ward white loops — own sheet
own sheet 600 × 600 · Gouache · 46 px · 6.9 s

![Brush Artist · Refs · #09 Henry Ward white loops — own sheet](Brush-Artist-Refs-09-Henry-Ward-white-loops-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 48 % → 32 % | 15.3 px | 0.02 | 0.67 | 938 |
| stroke 2 | 51 % → 37 % | 36.0 px | 0.02 | 0.71 | 979 |
| stroke 3 | 59 % → 44 % | 34.2 px | 0.02 | 0.75 | 905 |

## Brush Artist · Refs · #10 Henry Ward maroon loops — own sheet
own sheet 600 × 600 · Heavy acrylic · 30 px · 2.8 s

![Brush Artist · Refs · #10 Henry Ward maroon loops — own sheet](Brush-Artist-Refs-10-Henry-Ward-maroon-loops-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 16 % → 33 % | 28.6 px | 0.77 | 2.07 | 185 |
| stroke 2 | 29 % → 47 % | 46.0 px | 0.77 | 1.60 | 105 |
| stroke 3 | 40 % → 50 % | 54.7 px | 0.77 | 1.24 | 141 |
| stroke 4 | 45 % → 43 % | 64.1 px | 0.77 | 0.96 | 97 |
| stroke 5 | 41 % → 38 % | 70.6 px | 0.77 | 0.93 | 128 |

Numbers say: wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #11 Henry Ward purple spun balls — own sheet
own sheet 600 × 600 · Heavy acrylic · 36 px · 3.0 s

![Brush Artist · Refs · #11 Henry Ward purple spun balls — own sheet](Brush-Artist-Refs-11-Henry-Ward-purple-spun-balls-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 35 % → 43 % | 17.2 px | 0.79 | 1.23 | 309 |
| stroke 2 | 45 % → 52 % | 21.9 px | 0.79 | 1.15 | 305 |
| stroke 3 | 45 % → 43 % | 21.8 px | 0.80 | 0.96 | 308 |

## Brush Artist · Refs · #12 Henry Ward black-olive cage — own sheet
own sheet 600 × 600 · Gouache · 28 px · 5.1 s

![Brush Artist · Refs · #12 Henry Ward black-olive cage — own sheet](Brush-Artist-Refs-12-Henry-Ward-black-olive-cage-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 18 % → 22 % | 24.3 px | 0.65 | 1.24 | 207 |
| stroke 2 | 16 % → 26 % | 27.8 px | 0.65 | 1.61 | 165 |
| stroke 3 | 34 % → 34 % | 40.4 px | 0.65 | 1.00 | 210 |
| stroke 4 | 34 % → 34 % | 42.9 px | 0.65 | 1.02 | 114 |
| stroke 5 | 34 % → 21 % | 43.2 px | 0.65 | 0.60 | 122 |
| stroke 6 | 52 % → 37 % | 67.4 px | 0.65 | 0.72 | 151 |

Numbers say: wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #13 Henry Ward blue streaky form — own sheet
own sheet 600 × 600 · Gouache · 50 px · 12.8 s

![Brush Artist · Refs · #13 Henry Ward blue streaky form — own sheet](Brush-Artist-Refs-13-Henry-Ward-blue-streaky-form-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 33 % → 60 % | 47.1 px | 0.10 | 1.83 | 198 |
| stroke 2 | 41 % → 63 % | 65.3 px | 0.10 | 1.56 | 201 |
| stroke 3 | 58 % → 85 % | 82.4 px | 0.10 | 1.46 | 199 |
| stroke 4 | 58 % → 87 % | 95.9 px | 0.10 | 1.49 | 185 |
| stroke 5 | 59 % → 85 % | 84.5 px | 0.10 | 1.44 | 188 |
| stroke 6 | 55 % → 81 % | 84.9 px | 0.10 | 1.47 | 203 |
| stroke 7 | 60 % → 84 % | 89.8 px | 0.10 | 1.40 | 200 |
| stroke 8 | 61 % → 84 % | 95.3 px | 0.10 | 1.37 | 192 |
| stroke 9 | 61 % → 86 % | 92.6 px | 0.10 | 1.42 | 191 |
| stroke 10 | 62 % → 87 % | 101.2 px | 0.10 | 1.40 | 182 |
| stroke 11 | 57 % → 85 % | 85.8 px | 0.10 | 1.49 | 191 |
| stroke 12 | 57 % → 80 % | 89.7 px | 0.10 | 1.42 | 202 |
| stroke 13 | 60 % → 86 % | 88.2 px | 0.10 | 1.44 | 184 |
| stroke 14 | 53 % → 81 % | 82.7 px | 0.10 | 1.53 | 188 |
| stroke 15 | 56 % → 82 % | 79.8 px | 0.10 | 1.48 | 195 |
| stroke 16 | 55 % → 83 % | 89.3 px | 0.10 | 1.51 | 192 |
| stroke 17 | 60 % → 83 % | 91.6 px | 0.10 | 1.40 | 189 |
| stroke 18 | 60 % → 80 % | 94.0 px | 0.10 | 1.34 | 197 |
| stroke 19 | 66 % → 77 % | 82.9 px | 0.10 | 1.16 | 203 |
| stroke 20 | 77 % → 74 % | 91.8 px | 0.10 | 0.97 | 202 |

Numbers say: wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #14 Henry Ward olive totem — own sheet
own sheet 600 × 600 · Heavy acrylic · 48 px · 6.1 s

![Brush Artist · Refs · #14 Henry Ward olive totem — own sheet](Brush-Artist-Refs-14-Henry-Ward-olive-totem-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 31 % → 50 % | 46.9 px | 0.33 | 1.58 | 127 |
| stroke 2 | 36 % → 62 % | 64.3 px | 0.33 | 1.71 | 115 |
| stroke 3 | 54 % → 76 % | 79.7 px | 0.34 | 1.42 | 125 |
| stroke 4 | 50 % → 73 % | 88.4 px | 0.34 | 1.46 | 122 |
| stroke 5 | 56 % → 78 % | 83.2 px | 0.33 | 1.39 | 122 |
| stroke 6 | 54 % → 81 % | 96.5 px | 0.34 | 1.50 | 107 |
| stroke 7 | 52 % → 75 % | 74.2 px | 0.34 | 1.45 | 117 |
| stroke 8 | 51 % → 77 % | 90.4 px | 0.34 | 1.53 | 128 |
| stroke 9 | 56 % → 81 % | 82.9 px | 0.34 | 1.44 | 100 |
| stroke 10 | 56 % → 78 % | 94.7 px | 0.34 | 1.40 | 108 |
| stroke 11 | 57 % → 79 % | 90.0 px | 0.34 | 1.38 | 103 |
| stroke 12 | 53 % → 80 % | 90.4 px | 0.34 | 1.53 | 127 |
| stroke 13 | 55 % → 83 % | 82.0 px | 0.34 | 1.51 | 108 |
| stroke 14 | 52 % → 76 % | 86.9 px | 0.34 | 1.48 | 138 |
| stroke 15 | 58 % → 82 % | 85.5 px | 0.34 | 1.41 | 119 |
| stroke 16 | 54 % → 80 % | 89.8 px | 0.34 | 1.47 | 128 |
| stroke 17 | 53 % → 78 % | 77.7 px | 0.34 | 1.45 | 126 |
| stroke 18 | 57 % → 84 % | 100.3 px | 0.34 | 1.47 | 112 |
| stroke 19 | 57 % → 80 % | 86.5 px | 0.34 | 1.41 | 116 |
| stroke 20 | 55 % → 76 % | 95.2 px | 0.34 | 1.40 | 123 |
| stroke 21 | 52 % → 67 % | 83.7 px | 0.34 | 1.30 | 120 |
| stroke 22 | 60 % → 59 % | 94.0 px | 0.34 | 0.98 | 111 |

Numbers say: wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #15 Ultramarine brush script — own sheet
own sheet 600 × 600 · Ink · 10 px · 8.6 s

![Brush Artist · Refs · #15 Ultramarine brush script — own sheet](Brush-Artist-Refs-15-Ultramarine-brush-script-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 69 % → 72 % | 17.0 px | 0.70 | 1.05 | 59 |
| stroke 2 | 70 % → 72 % | 16.6 px | 0.69 | 1.04 | 76 |
| stroke 3 | 70 % → 74 % | 17.4 px | 0.69 | 1.05 | 61 |
| stroke 4 | 71 % → 72 % | 16.3 px | 0.66 | 1.01 | 88 |
| stroke 5 | 66 % → 69 % | 15.7 px | 0.67 | 1.04 | 91 |
| stroke 6 | 67 % → 71 % | 18.5 px | 0.70 | 1.05 | 46 |
| stroke 7 | 69 % → 71 % | 15.9 px | 0.67 | 1.04 | 82 |
| stroke 8 | 69 % → 71 % | 17.6 px | 0.70 | 1.02 | 59 |
| stroke 9 | 67 % → 70 % | 16.5 px | 0.68 | 1.05 | 65 |
| stroke 10 | 65 % → 69 % | 17.1 px | 0.69 | 1.05 | 63 |
| stroke 11 | 72 % → 75 % | 17.5 px | 0.69 | 1.04 | 57 |
| stroke 12 | 68 % → 69 % | 15.8 px | 0.67 | 1.01 | 92 |
| stroke 13 | 66 % → 69 % | 15.7 px | 0.67 | 1.04 | 96 |
| stroke 14 | 67 % → 71 % | 18.2 px | 0.70 | 1.05 | 43 |
| stroke 15 | 69 % → 73 % | 18.8 px | 0.71 | 1.05 | 46 |
| stroke 16 | 68 % → 72 % | 17.4 px | 0.70 | 1.04 | 59 |
| stroke 17 | 68 % → 69 % | 18.1 px | 0.70 | 1.02 | 45 |
| stroke 18 | 68 % → 71 % | 17.2 px | 0.70 | 1.05 | 64 |
| stroke 19 | 66 % → 71 % | 18.9 px | 0.71 | 1.07 | 45 |
| stroke 20 | 68 % → 72 % | 18.8 px | 0.71 | 1.06 | 50 |
| stroke 21 | 70 % → 73 % | 16.0 px | 0.67 | 1.03 | 94 |
| stroke 22 | 77 % → 79 % | 12.6 px | 0.70 | 1.02 | 84 |
| stroke 23 | 67 % → 71 % | 16.9 px | 0.70 | 1.05 | 60 |
| stroke 24 | 66 % → 69 % | 17.9 px | 0.71 | 1.05 | 51 |
| stroke 25 | 69 % → 72 % | 16.5 px | 0.68 | 1.04 | 79 |
| stroke 26 | 70 % → 71 % | 15.8 px | 0.66 | 1.01 | 91 |

## Brush Artist · Refs · #18 Blue oil-stick scribbles — own sheet
own sheet 600 × 600 · Pastel · 10 px · 2.7 s

![Brush Artist · Refs · #18 Blue oil-stick scribbles — own sheet](Brush-Artist-Refs-18-Blue-oil-stick-scribbles-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 23 % → 46 % | 4.8 px | 0.53 | 2.02 | 111 |
| stroke 2 | 20 % → 51 % | 4.5 px | 0.53 | 2.51 | 133 |
| stroke 3 | 23 % → 36 % | 7.3 px | 0.53 | 1.58 | 185 |
| stroke 4 | 21 % → 40 % | 9.7 px | 0.53 | 1.91 | 162 |
| stroke 5 | 40 % → 46 % | 9.7 px | 0.53 | 1.15 | 134 |
| stroke 6 | 38 % → 38 % | 11.7 px | 0.53 | 1.01 | 128 |
| stroke 7 | 35 % → 44 % | 9.4 px | 0.53 | 1.26 | 100 |
| stroke 8 | 41 % → 41 % | 20.3 px | 0.53 | 1.00 | 134 |

Numbers say: wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #20 Orange-red crayon scribble — own sheet
own sheet 600 × 600 · Pastel · 14 px · 2.5 s

![Brush Artist · Refs · #20 Orange-red crayon scribble — own sheet](Brush-Artist-Refs-20-Orange-red-crayon-scribble-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 11 % → 25 % | 6.9 px | 0.53 | 2.30 | 153 |
| stroke 2 | 13 % → 32 % | 8.2 px | 0.53 | 2.47 | 147 |
| stroke 3 | 19 % → 31 % | 10.4 px | 0.53 | 1.60 | 125 |
| stroke 4 | 35 % → 44 % | 10.5 px | 0.53 | 1.25 | 131 |
| stroke 5 | 40 % → 40 % | 8.7 px | 0.53 | 1.00 | 148 |
| stroke 6 | 31 % → 31 % | 20.1 px | 0.53 | 1.00 | 171 |

Numbers say: wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #21 Gritty black contours — own sheet
own sheet 600 × 600 · Gouache · 12 px · 3.8 s

![Brush Artist · Refs · #21 Gritty black contours — own sheet](Brush-Artist-Refs-21-Gritty-black-contours-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 12 % → 9 % | 10.5 px | 0.80 | 0.73 | 130 |
| stroke 2 | 10 % → 6 % | 14.0 px | 0.80 | 0.62 | 146 |
| stroke 3 | 18 % → 5 % | 12.4 px | 0.80 | 0.28 | 107 |
| stroke 4 | 19 % → 9 % | 18.3 px | 0.80 | 0.47 | 118 |
| stroke 5 | 19 % → 10 % | 17.9 px | 0.80 | 0.50 | 71 |

## Brush Artist · Refs · #22 Bold black brush poster — own sheet
own sheet 600 × 600 · Ink · 20 px · 4.5 s

![Brush Artist · Refs · #22 Bold black brush poster — own sheet](Brush-Artist-Refs-22-Bold-black-brush-poster-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 34 % → 37 % | 36.3 px | 0.89 | 1.10 | 96 |
| stroke 2 | 55 % → 66 % | 36.9 px | 0.89 | 1.21 | 22 |
| stroke 3 | 49 % → 49 % | 40.5 px | 0.89 | 1.00 | 43 |
| stroke 4 | 36 % → 43 % | 45.3 px | 0.89 | 1.20 | 49 |
| stroke 5 | 35 % → 35 % | 40.5 px | 0.89 | 1.00 | 72 |

## Brush Artist · Refs · #23 Dry white on orange + black line — own sheet
own sheet 600 × 600 · Gouache · 50 px · 8.9 s

![Brush Artist · Refs · #23 Dry white on orange + black line — own sheet](Brush-Artist-Refs-23-Dry-white-on-orange-black-line-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 27 % → 48 % | 44.6 px | 0.00 | 1.80 | 149 |
| stroke 2 | 31 % → 48 % | 53.8 px | 0.00 | 1.56 | 162 |
| stroke 3 | 51 % → 69 % | 82.3 px | 0.00 | 1.37 | 139 |
| stroke 4 | 48 % → 65 % | 88.2 px | 0.00 | 1.35 | 144 |
| stroke 5 | 50 % → 54 % | 77.2 px | 0.01 | 1.08 | 143 |
| stroke 6 | 49 % → 59 % | 93.8 px | 0.01 | 1.20 | 137 |
| stroke 7 | 40 % → 57 % | 67.1 px | 0.01 | 1.43 | 141 |
| stroke 8 | 42 % → 54 % | 74.9 px | 0.01 | 1.30 | 141 |
| stroke 9 | 51 % → 67 % | 83.8 px | 0.01 | 1.31 | 133 |
| stroke 10 | 54 % → 71 % | 96.9 px | 0.01 | 1.31 | 156 |
| stroke 11 | 49 % → 69 % | 81.3 px | 0.01 | 1.40 | 143 |
| stroke 12 | 49 % → 65 % | 89.0 px | 0.01 | 1.31 | 156 |
| stroke 13 | 52 % → 63 % | 84.9 px | 0.01 | 1.20 | 141 |
| stroke 14 | 49 % → 62 % | 90.3 px | 0.01 | 1.27 | 159 |
| stroke 15 | 49 % → 66 % | 79.4 px | 0.01 | 1.34 | 134 |
| stroke 16 | 46 % → 62 % | 85.5 px | 0.01 | 1.35 | 146 |
| stroke 17 | 47 % → 52 % | 77.5 px | 0.01 | 1.12 | 148 |
| stroke 18 | 56 % → 50 % | 103.2 px | 0.01 | 0.90 | 129 |

Numbers say: wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #24 Picasso flat oil — own sheet
own sheet 600 × 600 · Oil · 34 px · 4.9 s

![Brush Artist · Refs · #24 Picasso flat oil — own sheet](Brush-Artist-Refs-24-Picasso-flat-oil-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 35 % → 60 % | 34.6 px | 0.41 | 1.73 | 123 |
| stroke 2 | 40 % → 66 % | 47.1 px | 0.42 | 1.65 | 118 |
| stroke 3 | 56 % → 84 % | 59.7 px | 0.42 | 1.50 | 125 |
| stroke 4 | 56 % → 82 % | 63.9 px | 0.42 | 1.47 | 125 |
| stroke 5 | 55 % → 86 % | 59.9 px | 0.42 | 1.56 | 128 |
| stroke 6 | 56 % → 85 % | 66.3 px | 0.42 | 1.52 | 119 |
| stroke 7 | 60 % → 75 % | 59.1 px | 0.42 | 1.23 | 122 |
| stroke 8 | 56 % → 72 % | 71.1 px | 0.42 | 1.28 | 126 |
| stroke 9 | 42 % → 67 % | 43.8 px | 0.41 | 1.61 | 119 |
| stroke 10 | 46 % → 69 % | 56.7 px | 0.42 | 1.49 | 117 |
| stroke 11 | 59 % → 73 % | 60.6 px | 0.42 | 1.24 | 125 |
| stroke 12 | 59 % → 78 % | 72.3 px | 0.42 | 1.31 | 116 |
| stroke 13 | 47 % → 72 % | 50.2 px | 0.41 | 1.55 | 122 |
| stroke 14 | 48 % → 75 % | 55.1 px | 0.41 | 1.54 | 122 |
| stroke 15 | 53 % → 82 % | 53.5 px | 0.42 | 1.56 | 116 |
| stroke 16 | 49 % → 78 % | 58.9 px | 0.42 | 1.59 | 125 |
| stroke 17 | 60 % → 71 % | 59.6 px | 0.42 | 1.18 | 123 |
| stroke 18 | 56 % → 56 % | 71.0 px | 0.42 | 1.00 | 116 |

Numbers say: wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #25 Yellow heavy flat stroke — own sheet
own sheet 600 × 600 · Heavy acrylic · 110 px · 2.5 s

![Brush Artist · Refs · #25 Yellow heavy flat stroke — own sheet](Brush-Artist-Refs-25-Yellow-heavy-flat-stroke-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 35 % → 35 % | 104.2 px | 0.17 | 0.98 | 595 |

## Brush Artist · Refs · #27 Orange impasto swatch — own sheet
own sheet 600 × 600 · Heavy acrylic · 60 px · 2.8 s

![Brush Artist · Refs · #27 Orange impasto swatch — own sheet](Brush-Artist-Refs-27-Orange-impasto-swatch-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 23 % → 29 % | 61.8 px | 0.37 | 1.29 | 69 |
| stroke 2 | 19 % → 40 % | 62.5 px | 0.37 | 2.07 | 43 |
| stroke 3 | 26 % → 38 % | 94.9 px | 0.37 | 1.48 | 37 |
| stroke 4 | 22 % → 22 % | 62.5 px | 0.36 | 0.96 | 57 |
| stroke 5 | 32 % → 41 % | 62.2 px | 0.36 | 1.28 | 68 |
| stroke 6 | 39 % → 40 % | 112.2 px | 0.36 | 1.02 | 53 |
| stroke 7 | 19 % → 21 % | 63.8 px | 0.36 | 1.11 | 43 |
| stroke 8 | 42 % → 40 % | 143.3 px | 0.36 | 0.97 | 41 |
| stroke 9 | 49 % → 48 % | 97.7 px | 0.37 | 0.97 | 72 |
| stroke 10 | 28 % → 27 % | 87.2 px | 0.36 | 0.96 | 43 |

Numbers say: wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #28 Miles Davis black lines — own sheet
own sheet 600 × 600 · Ink · 22 px · 5.4 s

![Brush Artist · Refs · #28 Miles Davis black lines — own sheet](Brush-Artist-Refs-28-Miles-Davis-black-lines-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 29 % → 36 % | 36.4 px | 0.89 | 1.26 | 161 |
| stroke 2 | 37 % → 57 % | 36.0 px | 0.89 | 1.52 | 123 |
| stroke 3 | 47 % → 48 % | 66.3 px | 0.89 | 1.02 | 102 |
| stroke 4 | 49 % → 58 % | 76.4 px | 0.89 | 1.16 | 156 |
| stroke 5 | 63 % → 64 % | 95.0 px | 0.89 | 1.00 | 121 |

Numbers say: wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #29 Shrigley magenta asterisk — own sheet
own sheet 600 × 600 · Watercolor · 70 px · 5.4 s

![Brush Artist · Refs · #29 Shrigley magenta asterisk — own sheet](Brush-Artist-Refs-29-Shrigley-magenta-asterisk-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 25 % → 44 % | 46.3 px | 0.26 | 1.77 | 163 |
| stroke 2 | 17 % → 17 % | 86.2 px | 0.24 | 1.00 | 166 |
| stroke 3 | 37 % → 43 % | 69.3 px | 0.26 | 1.17 | 290 |
| stroke 4 | 32 % → 33 % | 162.7 px | 0.24 | 1.02 | 177 |

Numbers say: wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #30 Red gouache face patch — own sheet
own sheet 600 × 600 · Gouache · 60 px · 10.2 s

![Brush Artist · Refs · #30 Red gouache face patch — own sheet](Brush-Artist-Refs-30-Red-gouache-face-patch-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 27 % → 51 % | 51.5 px | 0.59 | 1.89 | 144 |
| stroke 2 | 33 % → 57 % | 74.5 px | 0.59 | 1.74 | 146 |
| stroke 3 | 50 % → 77 % | 99.1 px | 0.59 | 1.54 | 138 |
| stroke 4 | 50 % → 77 % | 110.7 px | 0.59 | 1.54 | 156 |
| stroke 5 | 49 % → 78 % | 97.1 px | 0.59 | 1.61 | 157 |
| stroke 6 | 50 % → 80 % | 112.2 px | 0.59 | 1.59 | 146 |
| stroke 7 | 51 % → 78 % | 101.2 px | 0.59 | 1.53 | 145 |
| stroke 8 | 49 % → 76 % | 103.7 px | 0.59 | 1.55 | 164 |
| stroke 9 | 52 % → 80 % | 104.6 px | 0.59 | 1.53 | 140 |
| stroke 10 | 54 % → 76 % | 123.0 px | 0.59 | 1.39 | 138 |
| stroke 11 | 52 % → 74 % | 107.4 px | 0.59 | 1.43 | 145 |
| stroke 12 | 50 % → 74 % | 109.1 px | 0.59 | 1.48 | 155 |
| stroke 13 | 45 % → 72 % | 87.5 px | 0.59 | 1.61 | 157 |
| stroke 14 | 45 % → 63 % | 95.7 px | 0.59 | 1.42 | 294 |
| stroke 15 | 48 % → 58 % | 92.1 px | 0.59 | 1.21 | 171 |
| stroke 16 | 55 % → 54 % | 122.4 px | 0.59 | 0.99 | 143 |

Numbers say: wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #31 Warhol blotted line — own sheet
own sheet 600 × 600 · Ink · 6 px · 4.2 s

![Brush Artist · Refs · #31 Warhol blotted line — own sheet](Brush-Artist-Refs-31-Warhol-blotted-line-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 24 % → 47 % | 15.7 px | 0.83 | 1.93 | 61 |
| stroke 2 | 19 % → 24 % | 15.8 px | 0.83 | 1.27 | 59 |
| stroke 3 | 27 % → 27 % | 24.7 px | 0.82 | 1.02 | 64 |
| stroke 4 | 31 % → 41 % | 27.9 px | 0.83 | 1.32 | 44 |
| stroke 5 | 38 % → 46 % | 34.7 px | 0.83 | 1.22 | 59 |
| stroke 6 | 35 % → 36 % | 25.2 px | 0.82 | 1.03 | 67 |

Numbers say: wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #32 Thick orange swipes — own sheet
own sheet 600 × 600 · Heavy acrylic · 90 px · 3.3 s

![Brush Artist · Refs · #32 Thick orange swipes — own sheet](Brush-Artist-Refs-32-Thick-orange-swipes-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 28 % → 28 % | 86.0 px | 0.39 | 1.00 | 281 |
| stroke 2 | 29 % → 32 % | 89.3 px | 0.39 | 1.13 | 276 |
| stroke 3 | 32 % → 32 % | 102.9 px | 0.39 | 0.98 | 252 |

## Brush Artist · Refs · #33 Red wet-in-wet band — own sheet
own sheet 600 × 600 · Watercolor · 80 px · 6.8 s

![Brush Artist · Refs · #33 Red wet-in-wet band — own sheet](Brush-Artist-Refs-33-Red-wet-in-wet-band-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 46 % → 64 % | 93.0 px | 0.37 | 1.41 | 411 |
| stroke 2 | 52 % → 66 % | 188.8 px | 0.40 | 1.26 | 100 |
| stroke 3 | 63 % → 76 % | 242.1 px | 0.41 | 1.21 | 101 |
| stroke 4 | 65 % → 75 % | 237.4 px | 0.38 | 1.16 | 93 |
| stroke 5 | 60 % → 72 % | 212.8 px | 0.39 | 1.20 | 117 |
| stroke 6 | 63 % → 63 % | 219.4 px | 0.39 | 1.00 | 114 |

## Brush Artist · Refs · #34 Magenta oil patches — own sheet
own sheet 600 × 600 · Oil · 60 px · 4.1 s

![Brush Artist · Refs · #34 Magenta oil patches — own sheet](Brush-Artist-Refs-34-Magenta-oil-patches-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 24 % → 44 % | 61.9 px | 0.62 | 1.86 | 85 |
| stroke 2 | 22 % → 37 % | 62.8 px | 0.62 | 1.68 | 65 |
| stroke 3 | 21 % → 52 % | 62.3 px | 0.62 | 2.42 | 58 |
| stroke 4 | 31 % → 31 % | 97.0 px | 0.62 | 1.00 | 57 |
| stroke 5 | 28 % → 40 % | 61.7 px | 0.62 | 1.46 | 85 |
| stroke 6 | 27 % → 45 % | 80.2 px | 0.62 | 1.65 | 62 |
| stroke 7 | 29 % → 41 % | 82.2 px | 0.62 | 1.42 | 67 |
| stroke 8 | 52 % → 56 % | 134.7 px | 0.62 | 1.07 | 80 |
| stroke 9 | 34 % → 39 % | 87.4 px | 0.62 | 1.13 | 87 |
| stroke 10 | 48 % → 48 % | 152.6 px | 0.62 | 1.00 | 59 |
| stroke 11 | 61 % → 61 % | 185.1 px | 0.62 | 1.00 | 58 |
| stroke 12 | 35 % → 35 % | 104.1 px | 0.62 | 1.00 | 65 |

Numbers say: wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #35 Red band with runs — own sheet
own sheet 600 × 600 · Watercolor · 70 px · 4.1 s

![Brush Artist · Refs · #35 Red band with runs — own sheet](Brush-Artist-Refs-35-Red-band-with-runs-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 42 % → 42 % | 84.9 px | 0.33 | 0.99 | 289 |

## Brush Artist · Refs · #36 Magenta letters flat brush — own sheet
own sheet 600 × 600 · Gouache · 36 px · 9.2 s

![Brush Artist · Refs · #36 Magenta letters flat brush — own sheet](Brush-Artist-Refs-36-Magenta-letters-flat-brush-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 46 % → 46 % | 59.1 px | 0.50 | 1.00 | 28 |
| stroke 2 | 38 % → 48 % | 39.7 px | 0.50 | 1.25 | 31 |
| stroke 3 | 56 % → 63 % | 72.2 px | 0.50 | 1.12 | 29 |
| stroke 4 | 45 % → 53 % | 44.9 px | 0.50 | 1.19 | 98 |
| stroke 5 | 41 % → 52 % | 61.1 px | 0.50 | 1.29 | 65 |
| stroke 6 | 78 % → 76 % | 153.6 px | 0.50 | 0.97 | 16 |
| stroke 7 | 43 % → 50 % | 42.1 px | 0.50 | 1.15 | 99 |
| stroke 8 | 39 % → 59 % | 63.5 px | 0.50 | 1.52 | 62 |
| stroke 9 | 54 % → 53 % | 82.8 px | 0.50 | 0.98 | 24 |
| stroke 10 | 42 % → 61 % | 63.1 px | 0.50 | 1.44 | 60 |
| stroke 11 | 78 % → 77 % | 153.6 px | 0.50 | 0.98 | 17 |
| stroke 12 | 58 % → 68 % | 57.2 px | 0.50 | 1.17 | 101 |
| stroke 13 | 43 % → 50 % | 58.9 px | 0.50 | 1.18 | 27 |
| stroke 14 | 52 % → 73 % | 74.9 px | 0.50 | 1.40 | 29 |
| stroke 15 | 44 % → 52 % | 66.5 px | 0.50 | 1.18 | 64 |
| stroke 16 | 78 % → 76 % | 153.3 px | 0.50 | 0.98 | 12 |
| stroke 17 | 53 % → 61 % | 51.3 px | 0.50 | 1.15 | 104 |
| stroke 18 | 40 % → 47 % | 54.9 px | 0.50 | 1.17 | 41 |
| stroke 19 | 65 % → 63 % | 81.6 px | 0.50 | 0.97 | 26 |
| stroke 20 | 56 % → 54 % | 70.5 px | 0.50 | 0.97 | 31 |
| stroke 21 | 47 % → 46 % | 53.9 px | 0.50 | 0.96 | 89 |

Numbers say: wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #37 Oil still life dabs — own sheet
own sheet 600 × 600 · Oil · 40 px · 3.2 s

![Brush Artist · Refs · #37 Oil still life dabs — own sheet](Brush-Artist-Refs-37-Oil-still-life-dabs-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 20 % → 20 % | 44.0 px | 0.39 | 1.00 | 24 |
| stroke 2 | 18 % → 48 % | 44.4 px | 0.40 | 2.65 | 20 |
| stroke 3 | 23 % → 48 % | 59.8 px | 0.40 | 2.12 | 16 |
| stroke 4 | 22 % → 22 % | 42.7 px | 0.39 | 1.00 | 33 |
| stroke 5 | 17 % → 18 % | 43.2 px | 0.38 | 1.04 | 19 |
| stroke 6 | 37 % → 45 % | 83.3 px | 0.40 | 1.24 | 24 |
| stroke 7 | 16 % → 27 % | 54.8 px | 0.38 | 1.71 | 13 |
| stroke 8 | 14 % → 29 % | 47.9 px | 0.38 | 2.08 | 9 |
| stroke 9 | 23 % → 23 % | 43.9 px | 0.39 | 1.00 | 34 |
| stroke 10 | 31 % → 37 % | 58.3 px | 0.39 | 1.18 | 30 |
| stroke 11 | 39 % → 39 % | 109.7 px | 0.39 | 1.00 | 17 |
| stroke 12 | 31 % → 31 % | 109.5 px | 0.38 | 1.00 | 12 |
| stroke 13 | 17 % → 17 % | 59.0 px | 0.37 | 1.00 | 12 |
| stroke 14 | 35 % → 35 % | 91.9 px | 0.39 | 1.00 | 14 |

Numbers say: wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #38 Sanguine drawing — own sheet
own sheet 600 × 600 · Pastel · 6 px · 2.0 s

![Brush Artist · Refs · #38 Sanguine drawing — own sheet](Brush-Artist-Refs-38-Sanguine-drawing-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 4 % → 16 % | 3.4 px | 0.61 | 4.44 | 3 |
| stroke 2 | 4 % → 8 % | 3.4 px | 0.61 | 2.27 | 6 |
| stroke 3 | 4 % → 10 % | 3.4 px | 0.61 | 2.77 | 4 |
| stroke 4 | 4 % → 22 % | 3.3 px | 0.61 | 6.14 | 3 |
| stroke 5 | 3 % → 9 % | 3.2 px | 0.61 | 2.68 | 5 |
| stroke 6 | 4 % → 24 % | 3.7 px | 0.61 | 6.04 | 3 |
| stroke 7 | 6 % → 17 % | 5.7 px | 0.61 | 2.80 | 7 |
| stroke 8 | 5 % → 18 % | 4.8 px | 0.61 | 3.39 | 3 |
| stroke 9 | 4 % → 9 % | 3.6 px | 0.61 | 2.20 | 6 |
| stroke 10 | 5 % → 19 % | 4.6 px | 0.61 | 3.82 | 3 |
| stroke 11 | 4 % → 5 % | 3.4 px | 0.61 | 1.48 | 7 |
| stroke 12 | 6 % → 18 % | 5.3 px | 0.61 | 3.15 | 3 |
| stroke 13 | 10 % → 21 % | 9.3 px | 0.61 | 2.08 | 7 |
| stroke 14 | 6 % → 17 % | 5.2 px | 0.61 | 2.97 | 3 |
| stroke 15 | 12 % → 21 % | 11.2 px | 0.61 | 1.70 | 7 |
| stroke 16 | 7 % → 19 % | 6.5 px | 0.61 | 2.72 | 3 |
| stroke 17 | 5 % → 11 % | 4.5 px | 0.61 | 2.14 | 7 |
| stroke 18 | 4 % → 6 % | 3.4 px | 0.61 | 1.67 | 3 |
| stroke 19 | 7 % → 20 % | 6.9 px | 0.61 | 2.71 | 6 |
| stroke 20 | 10 % → 17 % | 9.2 px | 0.61 | 1.71 | 3 |
| stroke 21 | 5 % → 5 % | 4.8 px | 0.61 | 1.00 | 3 |
| stroke 22 | 10 % → 16 % | 9.2 px | 0.61 | 1.65 | 5 |
| stroke 23 | 8 % → 13 % | 7.8 px | 0.61 | 1.52 | 3 |
| stroke 24 | 5 % → 8 % | 4.6 px | 0.61 | 1.53 | 6 |
| stroke 25 | 10 % → 18 % | 8.7 px | 0.61 | 1.88 | 7 |
| stroke 26 | 7 % → 9 % | 6.3 px | 0.61 | 1.26 | 3 |
| stroke 27 | 5 % → 5 % | 4.5 px | 0.61 | 1.04 | 3 |
| stroke 28 | 9 % → 14 % | 8.5 px | 0.61 | 1.55 | 6 |
| stroke 29 | 9 % → 20 % | 8.6 px | 0.61 | 2.13 | 6 |
| stroke 30 | 17 % → 21 % | 15.2 px | 0.61 | 1.25 | 3 |
| stroke 31 | 7 % → 8 % | 6.2 px | 0.61 | 1.21 | 7 |
| stroke 32 | 14 % → 16 % | 12.6 px | 0.61 | 1.14 | 3 |
| stroke 33 | 9 % → 9 % | 7.9 px | 0.61 | 1.05 | 6 |
| stroke 34 | 13 % → 17 % | 12.1 px | 0.61 | 1.29 | 3 |
| stroke 35 | 11 % → 17 % | 10.3 px | 0.61 | 1.54 | 6 |
| stroke 36 | 13 % → 16 % | 11.5 px | 0.61 | 1.26 | 4 |
| stroke 37 | 13 % → 21 % | 11.9 px | 0.61 | 1.63 | 3 |
| stroke 38 | 17 % → 25 % | 15.0 px | 0.61 | 1.50 | 5 |
| stroke 39 | 18 % → 22 % | 16.5 px | 0.61 | 1.20 | 3 |
| stroke 40 | 7 % → 8 % | 6.1 px | 0.61 | 1.15 | 4 |
| stroke 41 | 19 % → 19 % | 17.9 px | 0.61 | 1.00 | 5 |
| stroke 42 | 17 % → 19 % | 15.1 px | 0.61 | 1.15 | 3 |
| stroke 43 | 13 % → 15 % | 12.1 px | 0.61 | 1.17 | 4 |
| stroke 44 | 15 % → 18 % | 13.7 px | 0.61 | 1.23 | 3 |
| stroke 45 | 3 % → 3 % | 3.1 px | 0.61 | 1.00 | 7 |
| stroke 46 | 20 % → 20 % | 18.3 px | 0.61 | 1.00 | 7 |
| stroke 47 | 16 % → 16 % | 15.0 px | 0.61 | 1.00 | 4 |
| stroke 48 | 15 % → 16 % | 14.4 px | 0.61 | 1.03 | 4 |
| stroke 49 | 24 % → 24 % | 21.9 px | 0.61 | 1.00 | 7 |
| stroke 50 | 12 % → 12 % | 11.3 px | 0.61 | 1.00 | 7 |

Numbers say: wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #39 Very thick impasto — own sheet
own sheet 600 × 600 · Heavy acrylic · 60 px · 4.0 s

![Brush Artist · Refs · #39 Very thick impasto — own sheet](Brush-Artist-Refs-39-Very-thick-impasto-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 38 % → 37 % | 59.5 px | 0.63 | 0.97 | 258 |
| stroke 2 | 37 % → 40 % | 59.6 px | 0.63 | 1.08 | 252 |
| stroke 3 | 40 % → 39 % | 72.0 px | 0.63 | 0.97 | 238 |
| stroke 4 | 39 % → 38 % | 59.6 px | 0.63 | 0.97 | 247 |
| stroke 5 | 35 % → 34 % | 59.7 px | 0.63 | 0.97 | 260 |

## Brush Artist · Refs · #40 Watercolour blooms — own sheet
own sheet 600 × 600 · Watercolor · 90 px · 5.3 s

![Brush Artist · Refs · #40 Watercolour blooms — own sheet](Brush-Artist-Refs-40-Watercolour-blooms-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 41 % → 41 % | 99.1 px | 0.42 | 1.00 | 788 |

## Brush Artist · Refs · #41 Coloured pencil hatching — own sheet
own sheet 600 × 600 · Pastel · 4 px · 2.3 s

![Brush Artist · Refs · #41 Coloured pencil hatching — own sheet](Brush-Artist-Refs-41-Coloured-pencil-hatching-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 4 % → 17 % | 2.6 px | 0.43 | 4.08 | 3 |
| stroke 2 | 4 % → 9 % | 2.8 px | 0.41 | 1.99 | 5 |
| stroke 3 | 4 % → 13 % | 2.3 px | 0.42 | 3.64 | 2 |
| stroke 4 | 4 % → 23 % | 2.7 px | 0.43 | 5.54 | 2 |
| stroke 5 | 5 % → 8 % | 3.4 px | 0.42 | 1.47 | 2 |
| stroke 6 | 4 % → 16 % | 2.7 px | 0.43 | 3.71 | 5 |
| stroke 7 | 5 % → 17 % | 2.9 px | 0.42 | 3.80 | 4 |
| stroke 8 | 4 % → 14 % | 2.5 px | 0.43 | 3.50 | 5 |
| stroke 9 | 6 % → 13 % | 3.9 px | 0.42 | 2.17 | 5 |
| stroke 10 | 6 % → 19 % | 3.7 px | 0.43 | 3.26 | 4 |
| stroke 11 | 5 % → 15 % | 3.2 px | 0.42 | 3.01 | 5 |
| stroke 12 | 4 % → 4 % | 2.5 px | 0.42 | 1.00 | 4 |
| stroke 13 | 9 % → 20 % | 5.5 px | 0.42 | 2.23 | 4 |
| stroke 14 | 4 % → 17 % | 2.7 px | 0.42 | 4.02 | 5 |
| stroke 15 | 8 % → 15 % | 5.1 px | 0.42 | 1.88 | 2 |
| stroke 16 | 9 % → 13 % | 5.6 px | 0.42 | 1.46 | 2 |
| stroke 17 | 4 % → 4 % | 2.6 px | 0.42 | 1.00 | 2 |
| stroke 18 | 6 % → 10 % | 3.9 px | 0.43 | 1.61 | 5 |
| stroke 19 | 7 % → 16 % | 4.4 px | 0.42 | 2.34 | 3 |
| stroke 20 | 6 % → 18 % | 4.0 px | 0.43 | 2.88 | 5 |
| stroke 21 | 5 % → 18 % | 3.5 px | 0.42 | 3.33 | 2 |
| stroke 22 | 11 % → 20 % | 7.2 px | 0.43 | 1.80 | 5 |
| stroke 23 | 11 % → 16 % | 7.1 px | 0.42 | 1.42 | 2 |
| stroke 24 | 8 % → 17 % | 4.9 px | 0.42 | 2.17 | 9 |
| stroke 25 | 6 % → 12 % | 3.9 px | 0.43 | 2.04 | 3 |
| stroke 26 | 5 % → 6 % | 2.9 px | 0.42 | 1.41 | 2 |
| stroke 27 | 4 % → 8 % | 2.7 px | 0.42 | 1.93 | 2 |
| stroke 28 | 7 % → 11 % | 4.4 px | 0.42 | 1.56 | 5 |
| stroke 29 | 4 % → 17 % | 2.7 px | 0.43 | 3.84 | 2 |
| stroke 30 | 7 % → 11 % | 4.6 px | 0.42 | 1.48 | 2 |
| stroke 31 | 8 % → 18 % | 5.4 px | 0.42 | 2.10 | 2 |
| stroke 32 | 4 % → 8 % | 2.8 px | 0.42 | 1.83 | 2 |
| stroke 33 | 8 % → 13 % | 4.9 px | 0.43 | 1.72 | 7 |
| stroke 34 | 5 % → 7 % | 3.0 px | 0.42 | 1.53 | 2 |
| stroke 35 | 8 % → 16 % | 5.1 px | 0.42 | 2.05 | 4 |
| stroke 36 | 6 % → 6 % | 4.1 px | 0.42 | 1.00 | 4 |
| stroke 37 | 9 % → 17 % | 5.4 px | 0.42 | 2.00 | 4 |
| stroke 38 | 10 % → 16 % | 6.3 px | 0.42 | 1.60 | 7 |
| stroke 39 | 9 % → 14 % | 5.8 px | 0.42 | 1.56 | 3 |
| stroke 40 | 9 % → 22 % | 5.9 px | 0.43 | 2.29 | 2 |
| stroke 41 | 11 % → 15 % | 6.9 px | 0.42 | 1.39 | 2 |
| stroke 42 | 12 % → 21 % | 7.5 px | 0.42 | 1.76 | 5 |
| stroke 43 | 6 % → 10 % | 3.8 px | 0.42 | 1.64 | 3 |
| stroke 44 | 12 % → 17 % | 7.9 px | 0.43 | 1.36 | 4 |
| stroke 45 | 16 % → 21 % | 10.0 px | 0.42 | 1.36 | 2 |
| stroke 46 | 6 % → 8 % | 3.9 px | 0.42 | 1.26 | 5 |
| stroke 47 | 13 % → 16 % | 8.2 px | 0.42 | 1.19 | 2 |
| stroke 48 | 15 % → 20 % | 9.4 px | 0.43 | 1.34 | 2 |
| stroke 49 | 6 % → 11 % | 3.9 px | 0.42 | 1.81 | 2 |
| stroke 50 | 9 % → 9 % | 5.5 px | 0.42 | 1.00 | 5 |
| stroke 51 | 11 % → 20 % | 7.2 px | 0.42 | 1.78 | 3 |
| stroke 52 | 15 % → 18 % | 9.6 px | 0.43 | 1.21 | 2 |
| stroke 53 | 13 % → 18 % | 8.2 px | 0.43 | 1.36 | 2 |
| stroke 54 | 12 % → 18 % | 7.6 px | 0.43 | 1.49 | 5 |
| stroke 55 | 13 % → 17 % | 8.3 px | 0.43 | 1.29 | 2 |
| stroke 56 | 14 % → 15 % | 8.7 px | 0.42 | 1.10 | 2 |
| stroke 57 | 12 % → 17 % | 7.7 px | 0.42 | 1.39 | 4 |
| stroke 58 | 13 % → 15 % | 8.5 px | 0.42 | 1.14 | 2 |
| stroke 59 | 14 % → 16 % | 9.0 px | 0.43 | 1.14 | 2 |
| stroke 60 | 19 % → 24 % | 11.9 px | 0.42 | 1.27 | 2 |
| stroke 61 | 24 % → 25 % | 15.2 px | 0.42 | 1.02 | 2 |
| stroke 62 | 12 % → 12 % | 7.5 px | 0.42 | 1.00 | 2 |
| stroke 63 | 14 % → 14 % | 8.7 px | 0.43 | 1.06 | 4 |
| stroke 64 | 19 % → 19 % | 11.7 px | 0.43 | 1.02 | 2 |
| stroke 65 | 20 % → 20 % | 12.8 px | 0.42 | 1.00 | 2 |
| stroke 66 | 16 % → 16 % | 10.6 px | 0.42 | 1.00 | 5 |
| stroke 67 | 15 % → 15 % | 9.2 px | 0.43 | 1.05 | 2 |
| stroke 68 | 6 % → 11 % | 3.7 px | 0.42 | 1.88 | 4 |
| stroke 69 | 7 % → 7 % | 4.7 px | 0.42 | 1.00 | 2 |
| stroke 70 | 12 % → 16 % | 7.8 px | 0.43 | 1.27 | 2 |
| stroke 71 | 12 % → 14 % | 7.2 px | 0.42 | 1.17 | 4 |
| stroke 72 | 7 % → 8 % | 4.5 px | 0.41 | 1.18 | 2 |
| stroke 73 | 16 % → 16 % | 10.2 px | 0.42 | 1.00 | 5 |
| stroke 74 | 18 % → 18 % | 11.0 px | 0.43 | 1.00 | 5 |
| stroke 75 | 19 % → 19 % | 11.9 px | 0.43 | 1.00 | 2 |
| stroke 76 | 17 % → 17 % | 10.4 px | 0.43 | 1.00 | 6 |
| stroke 77 | 8 % → 11 % | 5.0 px | 0.42 | 1.40 | 2 |
| stroke 78 | 12 % → 12 % | 7.7 px | 0.42 | 1.00 | 2 |
| stroke 79 | 9 % → 9 % | 5.9 px | 0.42 | 1.00 | 2 |
| stroke 80 | 13 % → 13 % | 8.5 px | 0.42 | 1.00 | 2 |

Numbers say: wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #42 Oil pastel shaggy — own sheet
own sheet 600 × 600 · Pastel · 18 px · 2.5 s

![Brush Artist · Refs · #42 Oil pastel shaggy — own sheet](Brush-Artist-Refs-42-Oil-pastel-shaggy-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 11 % → 24 % | 9.8 px | 0.07 | 2.16 | 11 |
| stroke 2 | 12 % → 30 % | 10.4 px | 0.08 | 2.53 | 5 |
| stroke 3 | 12 % → 39 % | 10.6 px | 0.08 | 3.24 | 10 |
| stroke 4 | 12 % → 25 % | 10.7 px | 0.07 | 2.07 | 7 |
| stroke 5 | 14 % → 25 % | 12.0 px | 0.07 | 1.83 | 6 |
| stroke 6 | 12 % → 38 % | 10.7 px | 0.08 | 3.08 | 7 |
| stroke 7 | 17 % → 47 % | 15.1 px | 0.08 | 2.75 | 9 |
| stroke 8 | 13 % → 53 % | 11.5 px | 0.08 | 3.97 | 6 |
| stroke 9 | 16 % → 27 % | 13.7 px | 0.07 | 1.72 | 8 |
| stroke 10 | 13 % → 23 % | 11.1 px | 0.07 | 1.81 | 6 |
| stroke 11 | 12 % → 33 % | 10.4 px | 0.08 | 2.77 | 7 |
| stroke 12 | 17 % → 24 % | 14.6 px | 0.07 | 1.40 | 10 |
| stroke 13 | 22 % → 35 % | 19.6 px | 0.08 | 1.59 | 7 |
| stroke 14 | 11 % → 25 % | 9.9 px | 0.07 | 2.22 | 6 |
| stroke 15 | 12 % → 44 % | 10.6 px | 0.08 | 3.55 | 7 |
| stroke 16 | 19 % → 41 % | 16.8 px | 0.08 | 2.13 | 11 |
| stroke 17 | 26 % → 47 % | 22.2 px | 0.07 | 1.83 | 11 |
| stroke 18 | 29 % → 42 % | 25.5 px | 0.08 | 1.44 | 8 |
| stroke 19 | 27 % → 48 % | 23.0 px | 0.08 | 1.80 | 5 |
| stroke 20 | 28 % → 50 % | 24.1 px | 0.07 | 1.79 | 7 |
| stroke 21 | 17 % → 24 % | 14.6 px | 0.08 | 1.43 | 11 |
| stroke 22 | 16 % → 19 % | 14.4 px | 0.07 | 1.15 | 6 |
| stroke 23 | 24 % → 32 % | 20.5 px | 0.08 | 1.37 | 8 |
| stroke 24 | 36 % → 43 % | 31.2 px | 0.08 | 1.21 | 5 |
| stroke 25 | 24 % → 40 % | 20.6 px | 0.07 | 1.69 | 7 |
| stroke 26 | 13 % → 26 % | 11.0 px | 0.07 | 2.01 | 10 |
| stroke 27 | 37 % → 43 % | 32.8 px | 0.08 | 1.16 | 8 |
| stroke 28 | 22 % → 36 % | 19.7 px | 0.08 | 1.62 | 8 |
| stroke 29 | 13 % → 36 % | 11.0 px | 0.08 | 2.82 | 5 |
| stroke 30 | 16 % → 46 % | 14.3 px | 0.08 | 2.80 | 7 |
| stroke 31 | 18 % → 18 % | 16.1 px | 0.07 | 1.00 | 6 |
| stroke 32 | 23 % → 40 % | 20.4 px | 0.08 | 1.71 | 8 |
| stroke 33 | 25 % → 25 % | 21.3 px | 0.08 | 1.02 | 10 |
| stroke 34 | 35 % → 43 % | 30.6 px | 0.08 | 1.21 | 6 |
| stroke 35 | 36 % → 45 % | 30.9 px | 0.08 | 1.27 | 6 |
| stroke 36 | 31 % → 32 % | 26.4 px | 0.07 | 1.04 | 9 |
| stroke 37 | 25 % → 25 % | 21.3 px | 0.07 | 1.00 | 9 |
| stroke 38 | 35 % → 41 % | 29.8 px | 0.08 | 1.19 | 6 |
| stroke 39 | 18 % → 29 % | 15.6 px | 0.07 | 1.65 | 6 |
| stroke 40 | 42 % → 50 % | 36.1 px | 0.08 | 1.20 | 11 |
| stroke 41 | 39 % → 41 % | 34.3 px | 0.07 | 1.04 | 9 |
| stroke 42 | 25 % → 35 % | 22.0 px | 0.08 | 1.41 | 8 |
| stroke 43 | 18 % → 18 % | 15.4 px | 0.07 | 1.00 | 6 |
| stroke 44 | 35 % → 47 % | 30.0 px | 0.07 | 1.35 | 6 |
| stroke 45 | 30 % → 30 % | 26.1 px | 0.07 | 1.00 | 9 |
| stroke 46 | 48 % → 54 % | 41.7 px | 0.08 | 1.12 | 9 |
| stroke 47 | 45 % → 54 % | 39.3 px | 0.08 | 1.18 | 6 |
| stroke 48 | 32 % → 36 % | 28.0 px | 0.08 | 1.13 | 6 |
| stroke 49 | 39 % → 41 % | 33.6 px | 0.08 | 1.07 | 11 |
| stroke 50 | 47 % → 50 % | 40.8 px | 0.07 | 1.08 | 9 |
| stroke 51 | 23 % → 23 % | 20.3 px | 0.08 | 1.00 | 11 |
| stroke 52 | 44 % → 44 % | 38.7 px | 0.08 | 1.00 | 11 |
| stroke 53 | 27 % → 28 % | 23.5 px | 0.08 | 1.02 | 6 |
| stroke 54 | 34 % → 37 % | 29.5 px | 0.08 | 1.11 | 6 |
| stroke 55 | 20 % → 20 % | 17.3 px | 0.08 | 1.00 | 9 |
| stroke 56 | 26 % → 26 % | 22.1 px | 0.07 | 1.00 | 8 |
| stroke 57 | 44 % → 44 % | 38.1 px | 0.08 | 1.00 | 6 |
| stroke 58 | 36 % → 36 % | 30.9 px | 0.07 | 1.00 | 7 |
| stroke 59 | 60 % → 60 % | 52.7 px | 0.08 | 1.00 | 5 |
| stroke 60 | 23 % → 23 % | 19.5 px | 0.08 | 1.00 | 9 |

Numbers say: wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #43 Dragged black ink blocks — own sheet
own sheet 600 × 600 · Gouache · 70 px · 7.1 s

![Brush Artist · Refs · #43 Dragged black ink blocks — own sheet](Brush-Artist-Refs-43-Dragged-black-ink-blocks-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 46 % → 29 % | 66.8 px | 0.64 | 0.62 | 405 |
| stroke 2 | 35 % → 22 % | 66.5 px | 0.64 | 0.62 | 431 |
| stroke 3 | 36 % → 25 % | 67.8 px | 0.64 | 0.70 | 441 |
| stroke 4 | 39 % → 24 % | 71.8 px | 0.64 | 0.60 | 422 |
| stroke 5 | 43 % → 29 % | 66.7 px | 0.64 | 0.66 | 410 |

## Brush Artist · Refs · #44 Blue looping ribbon — own sheet
own sheet 600 × 600 · Oil · 80 px · 5.2 s

![Brush Artist · Refs · #44 Blue looping ribbon — own sheet](Brush-Artist-Refs-44-Blue-looping-ribbon-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 48 % → 48 % | 42.2 px | 0.73 | 1.00 | 2267 |

## Brush Artist · Refs · #45 Soft pastel pepper — own sheet
own sheet 600 × 600 · Pastel · 40 px · 2.9 s

![Brush Artist · Refs · #45 Soft pastel pepper — own sheet](Brush-Artist-Refs-45-Soft-pastel-pepper-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 19 % → 41 % | 14.2 px | 0.54 | 2.19 | 294 |
| stroke 2 | 32 % → 47 % | 25.6 px | 0.54 | 1.48 | 278 |
| stroke 3 | 42 % → 53 % | 17.4 px | 0.54 | 1.25 | 251 |
| stroke 4 | 39 % → 45 % | 34.6 px | 0.54 | 1.14 | 284 |
| stroke 5 | 47 % → 47 % | 17.6 px | 0.54 | 1.00 | 192 |

Numbers say: wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #46 Red-brown ink lips — own sheet
own sheet 600 × 600 · Watercolor · 70 px · 4.4 s

![Brush Artist · Refs · #46 Red-brown ink lips — own sheet](Brush-Artist-Refs-46-Red-brown-ink-lips-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 31 % → 45 % | 81.3 px | 0.58 | 1.42 | 202 |
| stroke 2 | 47 % → 47 % | 124.7 px | 0.57 | 1.00 | 167 |

## Brush Artist · Refs · #47 Pink knife slabs — own sheet
own sheet 600 × 600 · Heavy acrylic · 90 px · 3.9 s

![Brush Artist · Refs · #47 Pink knife slabs — own sheet](Brush-Artist-Refs-47-Pink-knife-slabs-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 28 % → 34 % | 83.2 px | 0.18 | 1.18 | 254 |
| stroke 2 | 36 % → 41 % | 106.4 px | 0.18 | 1.13 | 240 |
| stroke 3 | 36 % → 41 % | 106.3 px | 0.18 | 1.14 | 257 |
| stroke 4 | 37 % → 36 % | 106.4 px | 0.18 | 0.97 | 255 |

## Brush Artist · Refs · #48 Black bands with drips — own sheet
own sheet 600 × 600 · Gouache · 70 px · 7.0 s

![Brush Artist · Refs · #48 Black bands with drips — own sheet](Brush-Artist-Refs-48-Black-bands-with-drips-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 33 % → 30 % | 59.2 px | 0.80 | 0.91 | 432 |
| stroke 2 | 35 % → 32 % | 58.2 px | 0.80 | 0.92 | 453 |
| stroke 3 | 33 % → 31 % | 58.3 px | 0.80 | 0.94 | 437 |
| stroke 4 | 33 % → 32 % | 58.2 px | 0.80 | 0.95 | 417 |

## Brush Artist · Refs · #49 Magenta letters round brush — own sheet
own sheet 600 × 600 · Ink · 30 px · 6.4 s

![Brush Artist · Refs · #49 Magenta letters round brush — own sheet](Brush-Artist-Refs-49-Magenta-letters-round-brush-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 61 % → 65 % | 64.3 px | 0.52 | 1.06 | 27 |
| stroke 2 | 59 % → 63 % | 52.0 px | 0.53 | 1.07 | 30 |
| stroke 3 | 71 % → 80 % | 74.2 px | 0.53 | 1.13 | 27 |
| stroke 4 | 54 % → 64 % | 48.0 px | 0.52 | 1.18 | 108 |
| stroke 5 | 48 % → 65 % | 63.0 px | 0.52 | 1.35 | 67 |
| stroke 6 | 93 % → 94 % | 141.0 px | 0.53 | 1.01 | 15 |
| stroke 7 | 61 % → 70 % | 51.9 px | 0.52 | 1.14 | 108 |
| stroke 8 | 44 % → 72 % | 63.4 px | 0.53 | 1.61 | 62 |
| stroke 9 | 71 % → 71 % | 86.0 px | 0.53 | 1.00 | 25 |
| stroke 10 | 51 % → 72 % | 66.5 px | 0.52 | 1.42 | 74 |
| stroke 11 | 93 % → 94 % | 140.9 px | 0.53 | 1.01 | 16 |
| stroke 12 | 71 % → 83 % | 60.6 px | 0.52 | 1.18 | 108 |
| stroke 13 | 61 % → 65 % | 67.4 px | 0.53 | 1.05 | 28 |
| stroke 14 | 69 % → 92 % | 78.6 px | 0.53 | 1.33 | 31 |
| stroke 15 | 52 % → 63 % | 68.8 px | 0.52 | 1.20 | 68 |
| stroke 16 | 93 % → 93 % | 140.9 px | 0.53 | 1.00 | 15 |
| stroke 17 | 68 % → 76 % | 58.1 px | 0.52 | 1.12 | 113 |
| stroke 18 | 59 % → 62 % | 64.6 px | 0.52 | 1.05 | 30 |
| stroke 19 | 81 % → 80 % | 82.3 px | 0.53 | 0.99 | 29 |
| stroke 20 | 71 % → 70 % | 72.0 px | 0.52 | 1.00 | 26 |
| stroke 21 | 59 % → 59 % | 61.0 px | 0.52 | 1.00 | 77 |

Numbers say: wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #50 Thick swipes on photo — own sheet
own sheet 600 × 600 · Heavy acrylic · 40 px · 2.3 s

![Brush Artist · Refs · #50 Thick swipes on photo — own sheet](Brush-Artist-Refs-50-Thick-swipes-on-photo-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 24 % → 27 % | 42.6 px | 0.23 | 1.12 | 30 |
| stroke 2 | 21 % → 28 % | 42.4 px | 0.23 | 1.33 | 24 |
| stroke 3 | 26 % → 24 % | 41.8 px | 0.23 | 0.95 | 36 |
| stroke 4 | 26 % → 24 % | 42.6 px | 0.23 | 0.94 | 30 |
| stroke 5 | 24 % → 22 % | 41.8 px | 0.23 | 0.95 | 30 |
| stroke 6 | 21 % → 19 % | 42.9 px | 0.22 | 0.94 | 25 |
| stroke 7 | 36 % → 37 % | 59.4 px | 0.23 | 1.02 | 34 |
| stroke 8 | 34 % → 33 % | 66.7 px | 0.23 | 0.97 | 28 |
| stroke 9 | 25 % → 23 % | 42.0 px | 0.23 | 0.95 | 30 |
| stroke 10 | 28 % → 27 % | 42.2 px | 0.22 | 0.95 | 38 |
| stroke 11 | 23 % → 21 % | 42.6 px | 0.23 | 0.95 | 29 |
| stroke 12 | 24 % → 23 % | 53.2 px | 0.22 | 0.95 | 19 |

## Brush Artist · Ink — dry brush — own sheet
own sheet 600 × 600 · Gouache · 30 px · 2.5 s

![Brush Artist · Ink — dry brush — own sheet](Brush-Artist-Ink-dry-brush-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| ear | 17 % → 4 % | 16.4 px | 0.77 | 0.25 | 435 |
| drag0 | 20 % → 24 % | 25.1 px | 0.77 | 1.21 | 104 |
| drag1 | 25 % → 25 % | 34.4 px | 0.77 | 1.02 | 95 |
| drag2 | 28 % → 26 % | 42.3 px | 0.77 | 0.92 | 85 |
| drag3 | 30 % → 26 % | 50.6 px | 0.77 | 0.87 | 62 |

