![All brushes](contact.png)

# Brush Lab — 148 brushes · Nov 3, 2026 at 8:57 PM

Every sheet: 1500 × 600, ten strokes in a 5 × 2 grid — 1. light line · 2. heavy line · 3. pressure swell · 4. fast wave · 5. slow wave · 6. spiral · 7. loop · 8. tilted · 9. over the wet one · 10. long, no reload (cell 8 holds «tilted» and «over the wet one» crossed). The CPU reference of Mamay's paint engine; the wet layer settles 20 s at the end.

Columns: **covered** = share of the cell with paint right after the stroke → after settling; **width** = painted area of the stroke ÷ its length (px); **dark** = mean darkness of the painted pixels above the paper's own grain (0 = paper, 1 = black); **spread** = how far wet paint went beyond the stroke (1.0 = stayed); **ms** = the stroke on the CPU; long stroke: paint in each quarter of its length (it should run out: wet → streaks → dry tail).

## Ink Line
Ink · 12 px · 22.2 s

![Ink Line](Ink-Line.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 1 % → 4 % | 4.3 px | 0.55 | 2.44 | 36 |
| heavy line | 5 % → 6 % | 15.7 px | 0.68 | 1.13 | 66 |
| pressure swell | 3 % → 4 % | 11.3 px | 0.64 | 1.40 | 38 |
| fast wave | 10 % → 11 % | 11.2 px | 0.59 | 1.11 | 122 |
| slow wave | 8 % → 10 % | 9.6 px | 0.57 | 1.16 | 115 |
| spiral | 14 % → 15 % | 8.9 px | 0.50 | 1.07 | 200 |
| loop | 8 % → 9 % | 10.6 px | 0.61 | 1.16 | 105 |
| tilted | 5 % → 5 % | 14.4 px | 0.65 | 1.05 | 53 |
| over the wet one | 10 % → 11 % | 12.5 px | 0.65 | 1.15 | 50 |
| long, no reload | 18 % → 17 % | 8.1 px | 0.47 | 0.96 | 300 | quarters: 0.22 → 0.09 → 0.04 → 0.02

Numbers say: light vs heavy: width 4.3 → 15.7 px, dark 0.55 → 0.68; wet paint spreads well beyond the stroke.

## Dense Ink
Ink · 14 px · 22.6 s

![Dense Ink](Dense-Ink.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 5 % → 7 % | 15.2 px | 0.72 | 1.26 | 46 |
| heavy line | 7 % → 7 % | 19.1 px | 0.73 | 1.09 | 76 |
| pressure swell | 5 % → 6 % | 17.9 px | 0.72 | 1.17 | 44 |
| fast wave | 13 % → 13 % | 15.3 px | 0.69 | 1.01 | 135 |
| slow wave | 12 % → 12 % | 13.6 px | 0.67 | 1.04 | 146 |
| spiral | 18 % → 15 % | 12.2 px | 0.65 | 0.80 | 229 |
| loop | 11 % → 12 % | 14.8 px | 0.69 | 1.08 | 118 |
| tilted | 5 % → 6 % | 14.6 px | 0.72 | 1.07 | 61 |
| over the wet one | 12 % → 13 % | 17.7 px | 0.72 | 1.11 | 54 |
| long, no reload | 23 % → 15 % | 10.1 px | 0.64 | 0.66 | 329 | quarters: 0.30 → 0.12 → 0.04 → 0.02

Numbers say: light vs heavy: width 15.2 → 19.1 px, dark 0.72 → 0.73.

## Transparent Wash
Watercolor · 22 px · 23.1 s

![Transparent Wash](Transparent-Wash.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 2 % → 5 % | 6.9 px | 0.27 | 2.25 | 33 |
| heavy line | 7 % → 9 % | 20.4 px | 0.27 | 1.22 | 60 |
| pressure swell | 4 % → 6 % | 15.2 px | 0.28 | 1.54 | 34 |
| fast wave | 14 % → 16 % | 16.1 px | 0.20 | 1.17 | 116 |
| slow wave | 12 % → 15 % | 13.7 px | 0.21 | 1.28 | 168 |
| spiral | 18 % → 22 % | 11.9 px | 0.16 | 1.23 | 178 |
| loop | 11 % → 13 % | 14.5 px | 0.22 | 1.20 | 99 |
| tilted | 8 % → 8 % | 21.1 px | 0.24 | 1.06 | 58 |
| over the wet one | 13 % → 16 % | 16.4 px | 0.24 | 1.18 | 45 |
| long, no reload | 26 % → 32 % | 11.6 px | 0.13 | 1.22 | 278 | quarters: 0.11 → 0.04 → 0.02 → 0.01

Numbers say: light vs heavy: width 6.9 → 20.4 px, dark 0.27 → 0.27; wet paint spreads well beyond the stroke.

## Dry Brush
Gouache · 24 px · 19.6 s

![Dry Brush](Dry-Brush.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 5 % → 0 % | 14.0 px | 0.65 | 0.09 | 56 |
| heavy line | 6 % → 0 % | 18.6 px | 0.65 | 0.02 | 96 |
| pressure swell | 5 % → 0 % | 18.2 px | 0.65 | 0.08 | 70 |
| fast wave | 6 % → 1 % | 7.3 px | 0.65 | 0.08 | 156 |
| slow wave | 7 % → 0 % | 8.1 px | 0.65 | 0.06 | 255 |
| spiral | 7 % → 0 % | 4.6 px | 0.65 | 0.07 | 241 |
| loop | 10 % → 0 % | 12.4 px | 0.65 | 0.04 | 224 |
| tilted | 4 % → 3 % | 10.6 px | 0.65 | 0.88 | 115 |
| over the wet one | 9 % → 1 % | 14.5 px | 0.65 | 0.12 | 122 |
| long, no reload | 6 % → 1 % | 2.9 px | 0.65 | 0.14 | 335 | quarters: 0.12 → 0.00 → 0.00 → 0.00

Numbers say: light vs heavy: width 14.0 → 18.6 px, dark 0.65 → 0.65.

## Wax Crayon
Wax · 8 px · 10.2 s

![Wax Crayon](Wax-Crayon.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 1 % → 1 % | 2.5 px | 0.71 | 1.00 | 19 |
| heavy line | 1 % → 1 % | 3.9 px | 0.69 | 1.00 | 19 |
| pressure swell | 1 % → 1 % | 3.3 px | 0.70 | 1.00 | 20 |
| fast wave | 3 % → 3 % | 3.5 px | 0.69 | 1.00 | 56 |
| slow wave | 3 % → 3 % | 3.4 px | 0.70 | 1.00 | 39 |
| spiral | 5 % → 5 % | 3.3 px | 0.70 | 1.00 | 78 |
| loop | 3 % → 3 % | 3.3 px | 0.70 | 1.00 | 41 |
| tilted | 2 % → 2 % | 5.6 px | 0.68 | 1.00 | 31 |
| over the wet one | 3 % → 3 % | 3.6 px | 0.68 | 1.00 | 17 |
| long, no reload | 7 % → 7 % | 3.3 px | 0.70 | 1.00 | 105 | quarters: 0.06 → 0.06 → 0.06 → 0.06

Numbers say: light vs heavy: width 2.5 → 3.9 px, dark 0.71 → 0.69; the long stroke does not run out of paint.

## Oil Pastel
Wax · 12 px · 10.4 s

![Oil Pastel](Oil-Pastel.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 1 % → 1 % | 4.0 px | 0.68 | 1.00 | 32 |
| heavy line | 2 % → 2 % | 6.5 px | 0.68 | 1.00 | 28 |
| pressure swell | 2 % → 2 % | 5.7 px | 0.69 | 1.00 | 18 |
| fast wave | 5 % → 5 % | 5.7 px | 0.68 | 1.00 | 60 |
| slow wave | 5 % → 5 % | 5.5 px | 0.68 | 1.00 | 59 |
| spiral | 8 % → 8 % | 5.5 px | 0.68 | 1.00 | 104 |
| loop | 4 % → 4 % | 5.6 px | 0.68 | 1.00 | 57 |
| tilted | 2 % → 2 % | 6.8 px | 0.68 | 1.00 | 44 |
| over the wet one | 5 % → 5 % | 5.8 px | 0.68 | 1.00 | 24 |
| long, no reload | 13 % → 13 % | 5.6 px | 0.68 | 1.00 | 152 | quarters: 0.10 → 0.09 → 0.10 → 0.10

Numbers say: light vs heavy: width 4.0 → 6.5 px, dark 0.68 → 0.68; the long stroke does not run out of paint.

## Charcoal
Charcoal · 5 px · 9.2 s

![Charcoal](Charcoal.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 1 % → 1 % | 2.0 px | 0.74 | 1.00 | 10 |
| heavy line | 1 % → 1 % | 3.0 px | 0.74 | 1.00 | 11 |
| pressure swell | 1 % → 1 % | 2.7 px | 0.74 | 1.00 | 8 |
| fast wave | 2 % → 2 % | 2.7 px | 0.73 | 1.00 | 28 |
| slow wave | 2 % → 2 % | 2.6 px | 0.74 | 1.00 | 37 |
| spiral | 4 % → 4 % | 2.5 px | 0.74 | 1.00 | 66 |
| loop | 2 % → 2 % | 2.6 px | 0.74 | 1.00 | 35 |
| tilted | 2 % → 2 % | 4.3 px | 0.72 | 1.00 | 20 |
| over the wet one | 2 % → 2 % | 2.4 px | 0.72 | 1.00 | 14 |
| long, no reload | 6 % → 6 % | 2.7 px | 0.73 | 1.00 | 105 | quarters: 0.05 → 0.05 → 0.05 → 0.05

Numbers say: light vs heavy: width 2.0 → 3.0 px, dark 0.74 → 0.74; the long stroke does not run out of paint.

## Impasto
Heavy acrylic · 22 px · 14.2 s

![Impasto](Impasto.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 8 % → 8 % | 24.1 px | 0.71 | 0.93 | 42 |
| heavy line | 10 % → 9 % | 28.8 px | 0.70 | 0.94 | 115 |
| pressure swell | 7 % → 7 % | 28.1 px | 0.72 | 0.94 | 61 |
| fast wave | 20 % → 13 % | 23.5 px | 0.71 | 0.64 | 210 |
| slow wave | 21 % → 14 % | 24.5 px | 0.71 | 0.66 | 346 |
| spiral | 30 % → 14 % | 20.0 px | 0.71 | 0.46 | 275 |
| loop | 18 % → 14 % | 23.9 px | 0.71 | 0.77 | 145 |
| tilted | 8 % → 8 % | 21.8 px | 0.70 | 1.00 | 78 |
| over the wet one | 17 % → 15 % | 25.4 px | 0.70 | 0.91 | 66 |
| long, no reload | 34 % → 14 % | 15.2 px | 0.71 | 0.41 | 372 | quarters: 0.38 → 0.21 → 0.10 → 0.03

Numbers say: light vs heavy: width 24.1 → 28.8 px, dark 0.71 → 0.70.

## Oil Round
Oil · 18 px · 15.8 s

![Oil Round](Oil-Round.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 2 % → 2 % | 7.2 px | 0.75 | 1.00 | 34 |
| heavy line | 7 % → 7 % | 19.3 px | 0.73 | 1.00 | 69 |
| pressure swell | 4 % → 4 % | 13.7 px | 0.72 | 1.00 | 40 |
| fast wave | 11 % → 11 % | 12.7 px | 0.65 | 1.00 | 134 |
| slow wave | 8 % → 8 % | 9.0 px | 0.57 | 1.00 | 163 |
| spiral | 10 % → 10 % | 6.6 px | 0.50 | 1.00 | 205 |
| loop | 5 % → 5 % | 7.1 px | 0.45 | 1.00 | 109 |
| tilted | 4 % → 4 % | 10.1 px | 0.52 | 1.00 | 61 |
| over the wet one | 6 % → 6 % | 7.4 px | 0.52 | 1.00 | 53 |
| long, no reload | 15 % → 15 % | 6.8 px | 0.42 | 1.00 | 431 | quarters: 0.08 → 0.08 → 0.07 → 0.06

Numbers say: light vs heavy: width 7.2 → 19.3 px, dark 0.75 → 0.73.

## Palette Knife
Oil · 20 px · 15.3 s

![Palette Knife](Palette-Knife.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 8 % → 8 % | 21.9 px | 0.67 | 1.00 | 9 |
| heavy line | 8 % → 8 % | 22.5 px | 0.73 | 1.00 | 13 |
| pressure swell | 6 % → 6 % | 22.4 px | 0.74 | 1.00 | 6 |
| fast wave | 17 % → 17 % | 19.3 px | 0.49 | 1.00 | 26 |
| slow wave | 17 % → 17 % | 19.9 px | 0.43 | 1.00 | 34 |
| spiral | 18 % → 18 % | 11.7 px | 0.45 | 1.00 | 43 |
| loop | 16 % → 16 % | 21.0 px | 0.58 | 1.00 | 22 |
| tilted | 5 % → 5 % | 15.0 px | 0.72 | 1.00 | 9 |
| over the wet one | 13 % → 13 % | 21.0 px | 0.72 | 1.00 | 10 |
| long, no reload | 17 % → 17 % | 7.5 px | 0.47 | 1.00 | 59 | quarters: 0.29 → 0.05 → 0.00 → 0.00

Numbers say: light vs heavy: width 21.9 → 22.5 px, dark 0.67 → 0.73; pressure barely changes the width.

## Water
Watercolor · 20 px · 31.1 s · over bands of wet oil paint and oil pastel in turn (it works on paint already there: look at what it does to the bands; covered counts the bands too)

![Water](Water.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 25 % → 27 % | 73.8 px | 0.80 | 1.06 | 24 |
| heavy line | 24 % → 25 % | 69.8 px | 0.81 | 1.04 | 53 |
| pressure swell | 24 % → 25 % | 89.6 px | 0.81 | 1.03 | 31 |
| fast wave | 24 % → 26 % | 27.7 px | 0.81 | 1.07 | 102 |
| slow wave | 24 % → 25 % | 27.7 px | 0.81 | 1.06 | 138 |
| spiral | 24 % → 26 % | 15.9 px | 0.81 | 1.07 | 161 |
| loop | 24 % → 25 % | 31.1 px | 0.81 | 1.03 | 86 |
| tilted | 24 % → 24 % | 67.0 px | 0.81 | 1.00 | 55 |
| over the wet one | 24 % → 25 % | 0.0 px | 0.81 | 1.06 | 41 |
| long, no reload | 24 % → 26 % | 10.7 px | 0.81 | 1.08 | 249 | quarters: 0.21 → 0.27 → 0.18 → 0.27

Numbers say: light vs heavy: width 73.8 → 69.8 px, dark 0.80 → 0.81; pressure barely changes the width; the long stroke does not run out of paint.

## Blender
Pastel · 16 px · 19.0 s · over bands of wet oil paint and oil pastel in turn (it works on paint already there: look at what it does to the bands; covered counts the bands too)

![Blender](Blender.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 24 % → 24 % | 70.7 px | 0.81 | 1.00 | 21 |
| heavy line | 25 % → 25 % | 72.1 px | 0.80 | 1.00 | 33 |
| pressure swell | 24 % → 24 % | 91.3 px | 0.81 | 1.00 | 22 |
| fast wave | 26 % → 26 % | 30.0 px | 0.79 | 1.00 | 75 |
| slow wave | 26 % → 26 % | 29.9 px | 0.80 | 1.00 | 87 |
| spiral | 28 % → 28 % | 18.7 px | 0.77 | 1.00 | 116 |
| loop | 25 % → 25 % | 32.9 px | 0.80 | 1.00 | 68 |
| tilted | 25 % → 25 % | 70.1 px | 0.79 | 1.00 | 42 |
| over the wet one | 26 % → 26 % | 1.8 px | 0.79 | 1.00 | 31 |
| long, no reload | 30 % → 30 % | 13.7 px | 0.76 | 1.00 | 186 | quarters: 0.20 → 0.28 → 0.23 → 0.30

Numbers say: light vs heavy: width 70.7 → 72.1 px, dark 0.81 → 0.80; pressure barely changes the width; the long stroke does not run out of paint.

## Eraser
Eraser · 16 px · 18.8 s · over bands of wet oil paint and oil pastel in turn (it works on paint already there: look at what it does to the bands; covered counts the bands too)

![Eraser](Eraser.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 24 % → 24 % | 69.5 px | 0.82 | 1.00 | 25 |
| heavy line | 23 % → 23 % | 67.9 px | 0.82 | 1.00 | 33 |
| pressure swell | 23 % → 23 % | 87.3 px | 0.82 | 1.00 | 23 |
| fast wave | 22 % → 22 % | 25.7 px | 0.82 | 1.00 | 76 |
| slow wave | 22 % → 22 % | 25.7 px | 0.82 | 1.00 | 88 |
| spiral | 22 % → 22 % | 14.4 px | 0.82 | 1.00 | 119 |
| loop | 22 % → 22 % | 28.6 px | 0.82 | 1.00 | 69 |
| tilted | 23 % → 23 % | 65.1 px | 0.82 | 1.00 | 41 |
| over the wet one | 23 % → 23 % | 0.0 px | 0.82 | 1.00 | 32 |
| long, no reload | 20 % → 20 % | 8.9 px | 0.82 | 1.00 | 190 | quarters: 0.15 → 0.20 → 0.15 → 0.20

Numbers say: light vs heavy: width 69.5 → 67.9 px, dark 0.82 → 0.82; pressure barely changes the width; the long stroke does not run out of paint.

## Fan
Gouache · 30 px · 26.7 s

![Fan](Fan.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 9 % → 3 % | 25.7 px | 0.63 | 0.37 | 28 |
| heavy line | 11 % → 4 % | 31.0 px | 0.63 | 0.39 | 50 |
| pressure swell | 8 % → 5 % | 31.7 px | 0.63 | 0.55 | 32 |
| fast wave | 18 % → 5 % | 20.3 px | 0.63 | 0.26 | 99 |
| slow wave | 18 % → 5 % | 21.1 px | 0.63 | 0.25 | 165 |
| spiral | 24 % → 5 % | 15.8 px | 0.63 | 0.20 | 156 |
| loop | 17 % → 5 % | 22.7 px | 0.63 | 0.29 | 89 |
| tilted | 5 % → 6 % | 15.1 px | 0.63 | 1.05 | 37 |
| over the wet one | 16 % → 8 % | 29.8 px | 0.63 | 0.50 | 66 |
| long, no reload | 23 % → 5 % | 10.1 px | 0.63 | 0.22 | 295 | quarters: 0.29 → 0.07 → 0.01 → 0.00

Numbers say: light vs heavy: width 25.7 → 31.0 px, dark 0.63 → 0.63.

## Sponge
Gouache · 30 px · 26.7 s

![Sponge](Sponge.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 4 % → 0 % | 11.4 px | 0.62 | 0.12 | 33 |
| heavy line | 12 % → 2 % | 35.4 px | 0.62 | 0.14 | 59 |
| pressure swell | 7 % → 2 % | 27.9 px | 0.62 | 0.27 | 44 |
| fast wave | 20 % → 4 % | 23.2 px | 0.62 | 0.19 | 118 |
| slow wave | 21 % → 4 % | 23.7 px | 0.62 | 0.18 | 217 |
| spiral | 28 % → 4 % | 18.3 px | 0.62 | 0.14 | 185 |
| loop | 18 % → 5 % | 23.0 px | 0.62 | 0.29 | 101 |
| tilted | 7 % → 7 % | 18.2 px | 0.62 | 1.04 | 83 |
| over the wet one | 16 % → 6 % | 27.8 px | 0.62 | 0.37 | 70 |
| long, no reload | 29 % → 5 % | 12.9 px | 0.62 | 0.17 | 367 | quarters: 0.29 → 0.13 → 0.07 → 0.04

Numbers say: light vs heavy: width 11.4 → 35.4 px, dark 0.62 → 0.62.

## Ink — sumi brush
Watercolor · 22 px · 27.8 s

![Ink — sumi brush](Ink-sumi-brush.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 8 % → 9 % | 23.8 px | 0.77 | 1.13 | 61 |
| heavy line | 13 % → 13 % | 38.0 px | 0.72 | 1.01 | 61 |
| pressure swell | 9 % → 10 % | 34.5 px | 0.75 | 1.05 | 46 |
| fast wave | 27 % → 28 % | 31.7 px | 0.58 | 1.03 | 161 |
| slow wave | 25 % → 26 % | 29.0 px | 0.61 | 1.05 | 242 |
| spiral | 37 % → 38 % | 24.3 px | 0.51 | 1.03 | 264 |
| loop | 22 % → 22 % | 28.2 px | 0.66 | 1.03 | 186 |
| tilted | 9 % → 9 % | 24.7 px | 0.73 | 1.03 | 86 |
| over the wet one | 20 % → 21 % | 31.1 px | 0.73 | 1.03 | 62 |
| long, no reload | 42 % → 43 % | 18.9 px | 0.46 | 1.02 | 392 | quarters: 0.47 → 0.23 → 0.11 → 0.06

Numbers say: light vs heavy: width 23.8 → 38.0 px, dark 0.77 → 0.72.

## Ink — wash
Watercolor · 40 px · 30.4 s

![Ink — wash](Ink-wash.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 13 % → 13 % | 36.5 px | 0.17 | 1.04 | 65 |
| heavy line | 18 % → 19 % | 53.5 px | 0.13 | 1.04 | 88 |
| pressure swell | 12 % → 13 % | 46.6 px | 0.16 | 1.05 | 58 |
| fast wave | 40 % → 42 % | 45.9 px | 0.12 | 1.06 | 182 |
| slow wave | 38 % → 40 % | 43.6 px | 0.17 | 1.06 | 305 |
| spiral | 58 % → 62 % | 38.5 px | 0.12 | 1.06 | 327 |
| loop | 33 % → 34 % | 42.9 px | 0.15 | 1.03 | 229 |
| tilted | 14 % → 14 % | 38.1 px | 0.17 | 1.03 | 99 |
| over the wet one | 29 % → 31 % | 43.2 px | 0.17 | 1.06 | 82 |
| long, no reload | 66 % → 75 % | 29.8 px | 0.12 | 1.12 | 457 | quarters: 0.16 → 0.11 → 0.07 → 0.04

Numbers say: light vs heavy: width 36.5 → 53.5 px, dark 0.17 → 0.13.

## Ink — dry brush
Ink · 30 px · 21.6 s

![Ink — dry brush](Ink-dry-brush.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 9 % → 7 % | 25.2 px | 0.81 | 0.79 | 80 |
| heavy line | 10 % → 8 % | 29.6 px | 0.80 | 0.76 | 122 |
| pressure swell | 7 % → 6 % | 27.9 px | 0.81 | 0.85 | 75 |
| fast wave | 21 % → 8 % | 24.2 px | 0.79 | 0.40 | 210 |
| slow wave | 18 % → 7 % | 20.3 px | 0.79 | 0.39 | 354 |
| spiral | 24 % → 8 % | 15.6 px | 0.78 | 0.34 | 380 |
| loop | 19 % → 8 % | 24.3 px | 0.78 | 0.45 | 258 |
| tilted | 8 % → 8 % | 22.2 px | 0.78 | 1.02 | 170 |
| over the wet one | 17 % → 14 % | 25.9 px | 0.78 | 0.81 | 85 |
| long, no reload | 20 % → 8 % | 9.1 px | 0.79 | 0.41 | 507 | quarters: 0.32 → 0.02 → 0.00 → 0.00

Numbers say: light vs heavy: width 25.2 → 29.6 px, dark 0.81 → 0.80.

## Ink — nib
Watercolor · 5 px · 20.5 s

![Ink — nib](Ink-nib.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 2 % → 5 % | 5.4 px | 0.86 | 2.45 | 25 |
| heavy line | 2 % → 5 % | 6.4 px | 0.86 | 2.33 | 48 |
| pressure swell | 2 % → 4 % | 6.2 px | 0.86 | 2.52 | 25 |
| fast wave | 5 % → 8 % | 5.8 px | 0.82 | 1.65 | 87 |
| slow wave | 5 % → 8 % | 5.6 px | 0.82 | 1.73 | 63 |
| spiral | 7 % → 11 % | 4.8 px | 0.75 | 1.45 | 112 |
| loop | 4 % → 8 % | 5.6 px | 0.84 | 1.75 | 60 |
| tilted | 4 % → 4 % | 10.1 px | 0.85 | 1.04 | 34 |
| over the wet one | 6 % → 9 % | 6.3 px | 0.85 | 1.61 | 29 |
| long, no reload | 9 % → 12 % | 4.0 px | 0.70 | 1.37 | 161 | quarters: 0.23 → 0.08 → 0.04 → 0.02

Numbers say: light vs heavy: width 5.4 → 6.4 px, dark 0.86 → 0.86; wet paint spreads well beyond the stroke.

## 0.45 · Dry brush
Gouache · 34 px · 22.0 s

![0.45 · Dry brush](0-45-Dry-brush.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 10 % → 3 % | 29.4 px | 0.67 | 0.27 | 103 |
| heavy line | 11 % → 3 % | 31.6 px | 0.67 | 0.29 | 114 |
| pressure swell | 8 % → 3 % | 31.5 px | 0.67 | 0.41 | 82 |
| fast wave | 19 % → 3 % | 22.5 px | 0.67 | 0.18 | 292 |
| slow wave | 20 % → 4 % | 23.2 px | 0.67 | 0.18 | 477 |
| spiral | 21 % → 3 % | 14.1 px | 0.67 | 0.16 | 468 |
| loop | 20 % → 4 % | 26.1 px | 0.67 | 0.20 | 250 |
| tilted | 9 % → 8 % | 24.0 px | 0.67 | 0.98 | 135 |
| over the wet one | 19 % → 6 % | 28.2 px | 0.67 | 0.34 | 155 |
| long, no reload | 20 % → 4 % | 9.1 px | 0.67 | 0.19 | 946 | quarters: 0.36 → 0.10 → 0.00 → 0.00

Numbers say: light vs heavy: width 29.4 → 31.6 px, dark 0.67 → 0.67; pressure barely changes the width.

## Dry pastel
Pastel · 26 px · 9.7 s

![Dry pastel](Dry-pastel.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 3 % → 3 % | 8.3 px | 0.38 | 1.00 | 30 |
| heavy line | 5 % → 5 % | 13.2 px | 0.39 | 1.00 | 35 |
| pressure swell | 3 % → 3 % | 11.7 px | 0.38 | 1.00 | 25 |
| fast wave | 10 % → 10 % | 11.9 px | 0.39 | 1.00 | 84 |
| slow wave | 10 % → 10 % | 11.3 px | 0.39 | 1.00 | 149 |
| spiral | 15 % → 15 % | 9.6 px | 0.39 | 1.00 | 151 |
| loop | 7 % → 7 % | 9.4 px | 0.39 | 1.00 | 75 |
| tilted | 3 % → 3 % | 8.3 px | 0.38 | 1.00 | 41 |
| over the wet one | 7 % → 7 % | 11.1 px | 0.38 | 1.00 | 34 |
| long, no reload | 18 % → 18 % | 8.2 px | 0.39 | 1.00 | 207 | quarters: 0.08 → 0.08 → 0.08 → 0.07

Numbers say: light vs heavy: width 8.3 → 13.2 px, dark 0.38 → 0.39; the long stroke does not run out of paint.

## 0.45 · Charcoal
Charcoal · 18 px · 9.0 s

![0.45 · Charcoal](0-45-Charcoal.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 2 % → 2 % | 6.5 px | 0.80 | 1.00 | 17 |
| heavy line | 3 % → 3 % | 9.2 px | 0.80 | 1.00 | 18 |
| pressure swell | 2 % → 2 % | 8.8 px | 0.80 | 1.00 | 13 |
| fast wave | 7 % → 7 % | 8.5 px | 0.80 | 1.00 | 46 |
| slow wave | 7 % → 7 % | 8.0 px | 0.80 | 1.00 | 58 |
| spiral | 12 % → 12 % | 7.9 px | 0.80 | 1.00 | 74 |
| loop | 6 % → 6 % | 8.1 px | 0.80 | 1.00 | 37 |
| tilted | 3 % → 3 % | 7.5 px | 0.80 | 1.00 | 26 |
| over the wet one | 6 % → 6 % | 7.9 px | 0.80 | 1.00 | 17 |
| long, no reload | 17 % → 17 % | 7.8 px | 0.80 | 1.00 | 103 | quarters: 0.15 → 0.16 → 0.15 → 0.16

Numbers say: light vs heavy: width 6.5 → 9.2 px, dark 0.80 → 0.80; the long stroke does not run out of paint.

## Watercolour — wash
Watercolor · 50 px · 32.3 s

![Watercolour — wash](Watercolour-wash.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 15 % → 16 % | 43.3 px | 0.03 | 1.05 | 90 |
| heavy line | 21 % → 22 % | 62.1 px | 0.03 | 1.04 | 116 |
| pressure swell | 14 % → 15 % | 54.3 px | 0.03 | 1.04 | 82 |
| fast wave | 47 % → 49 % | 53.8 px | 0.02 | 1.04 | 255 |
| slow wave | 45 % → 46 % | 52.0 px | 0.04 | 1.03 | 444 |
| spiral | 64 % → 66 % | 42.5 px | 0.03 | 1.03 | 431 |
| loop | 39 % → 40 % | 50.3 px | 0.03 | 1.02 | 220 |
| tilted | 17 % → 17 % | 47.3 px | 0.04 | 1.03 | 233 |
| over the wet one | 35 % → 36 % | 49.0 px | 0.04 | 1.04 | 145 |
| long, no reload | 79 % → 84 % | 35.5 px | 0.03 | 1.06 | 711 | quarters: 0.04 → 0.03 → 0.02 → 0.01

Numbers say: light vs heavy: width 43.3 → 62.1 px, dark 0.03 → 0.03.

## Watercolour — wet-in-wet
Watercolor · 44 px · 33.6 s

![Watercolour — wet-in-wet](Watercolour-wet-in-wet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 13 % → 19 % | 36.6 px | 0.05 | 1.51 | 70 |
| heavy line | 18 % → 20 % | 52.4 px | 0.05 | 1.09 | 91 |
| pressure swell | 12 % → 15 % | 44.9 px | 0.06 | 1.26 | 81 |
| fast wave | 40 % → 45 % | 45.9 px | 0.05 | 1.13 | 287 |
| slow wave | 39 % → 45 % | 45.0 px | 0.07 | 1.15 | 343 |
| spiral | 62 % → 67 % | 40.8 px | 0.06 | 1.08 | 348 |
| loop | 33 % → 37 % | 43.2 px | 0.06 | 1.12 | 178 |
| tilted | 14 % → 14 % | 39.1 px | 0.06 | 1.03 | 124 |
| over the wet one | 29 % → 37 % | 41.7 px | 0.06 | 1.28 | 84 |
| long, no reload | 75 % → 84 % | 33.6 px | 0.06 | 1.12 | 503 | quarters: 0.07 → 0.06 → 0.04 → 0.03

Numbers say: light vs heavy: width 36.6 → 52.4 px, dark 0.05 → 0.05; wet paint spreads well beyond the stroke.

## Watercolour — glaze
Watercolor · 38 px · 30.8 s

![Watercolour — glaze](Watercolour-glaze.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 12 % → 13 % | 35.2 px | 0.03 | 1.05 | 72 |
| heavy line | 18 % → 19 % | 52.2 px | 0.02 | 1.06 | 78 |
| pressure swell | 12 % → 13 % | 44.6 px | 0.02 | 1.07 | 54 |
| fast wave | 37 % → 40 % | 42.4 px | 0.02 | 1.08 | 180 |
| slow wave | 35 % → 37 % | 40.2 px | 0.02 | 1.08 | 312 |
| spiral | 54 % → 59 % | 35.9 px | 0.02 | 1.09 | 304 |
| loop | 32 % → 33 % | 40.8 px | 0.02 | 1.05 | 158 |
| tilted | 13 % → 14 % | 37.0 px | 0.03 | 1.03 | 101 |
| over the wet one | 28 % → 30 % | 41.7 px | 0.03 | 1.06 | 72 |
| long, no reload | 60 % → 69 % | 26.8 px | 0.02 | 1.15 | 454 | quarters: 0.02 → 0.01 → 0.01 → 0.00

Numbers say: light vs heavy: width 35.2 → 52.2 px, dark 0.03 → 0.02.

## Watercolour — granulating
Watercolor · 44 px · 31.2 s

![Watercolour — granulating](Watercolour-granulating.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 14 % → 14 % | 40.5 px | 0.05 | 1.03 | 147 |
| heavy line | 20 % → 21 % | 59.2 px | 0.04 | 1.02 | 144 |
| pressure swell | 14 % → 14 % | 51.3 px | 0.05 | 1.02 | 75 |
| fast wave | 44 % → 45 % | 50.3 px | 0.04 | 1.04 | 230 |
| slow wave | 40 % → 42 % | 46.0 px | 0.06 | 1.06 | 356 |
| spiral | 59 % → 63 % | 38.7 px | 0.04 | 1.07 | 362 |
| loop | 36 % → 37 % | 46.9 px | 0.05 | 1.02 | 193 |
| tilted | 15 % → 16 % | 43.1 px | 0.06 | 1.03 | 136 |
| over the wet one | 32 % → 33 % | 46.6 px | 0.06 | 1.04 | 90 |
| long, no reload | 68 % → 76 % | 30.3 px | 0.04 | 1.12 | 536 | quarters: 0.06 → 0.04 → 0.02 → 0.02

Numbers say: light vs heavy: width 40.5 → 59.2 px, dark 0.05 → 0.04.

## Watercolour — dry brush
Watercolor · 36 px · 25.0 s

![Watercolour — dry brush](Watercolour-dry-brush.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 9 % → 9 % | 24.9 px | 0.07 | 1.09 | 96 |
| heavy line | 13 % → 13 % | 36.7 px | 0.06 | 0.99 | 100 |
| pressure swell | 10 % → 10 % | 36.4 px | 0.06 | 1.04 | 70 |
| fast wave | 24 % → 19 % | 27.3 px | 0.05 | 0.82 | 241 |
| slow wave | 22 % → 17 % | 25.2 px | 0.05 | 0.78 | 409 |
| spiral | 29 % → 20 % | 19.3 px | 0.05 | 0.67 | 404 |
| loop | 19 % → 18 % | 24.6 px | 0.05 | 0.94 | 296 |
| tilted | 9 % → 10 % | 24.3 px | 0.06 | 1.10 | 118 |
| over the wet one | 20 % → 20 % | 31.7 px | 0.06 | 0.99 | 102 |
| long, no reload | 28 % → 19 % | 12.4 px | 0.05 | 0.70 | 589 | quarters: 0.03 → 0.01 → 0.00 → 0.00

Numbers say: light vs heavy: width 24.9 → 36.7 px, dark 0.07 → 0.06.

## Gouache
Gouache · 30 px · 23.4 s

![Gouache](Gouache.png)

A light paint: laid on a grey sheet (on white it cannot be seen); **dark** = how far it is from the grey either way.

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 8 % → 5 % | 24.4 px | 0.28 | 0.64 | 67 |
| heavy line | 14 % → 6 % | 39.7 px | 0.28 | 0.47 | 81 |
| pressure swell | 10 % → 6 % | 38.6 px | 0.28 | 0.60 | 55 |
| fast wave | 28 % → 7 % | 32.2 px | 0.28 | 0.25 | 190 |
| slow wave | 27 % → 8 % | 31.4 px | 0.28 | 0.29 | 418 |
| spiral | 38 % → 8 % | 24.8 px | 0.27 | 0.22 | 336 |
| loop | 22 % → 8 % | 28.6 px | 0.28 | 0.35 | 170 |
| tilted | 9 % → 9 % | 23.8 px | 0.27 | 1.01 | 90 |
| over the wet one | 20 % → 13 % | 31.1 px | 0.27 | 0.66 | 75 |
| long, no reload | 40 % → 9 % | 17.9 px | 0.27 | 0.24 | 458 | quarters: 0.01 → 0.01 → 0.02 → 0.02

Numbers say: light vs heavy: width 24.4 → 39.7 px, dark 0.28 → 0.28; the long stroke does not run out of paint.

## Oil — alla prima
Oil · 30 px · 13.2 s

![Oil — alla prima](Oil-alla-prima.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 10 % → 10 % | 27.6 px | 0.51 | 1.00 | 81 |
| heavy line | 10 % → 10 % | 30.4 px | 0.51 | 1.00 | 83 |
| pressure swell | 8 % → 8 % | 29.9 px | 0.53 | 1.00 | 59 |
| fast wave | 24 % → 24 % | 28.1 px | 0.51 | 1.00 | 206 |
| slow wave | 26 % → 26 % | 29.6 px | 0.51 | 1.00 | 351 |
| spiral | 40 % → 40 % | 26.4 px | 0.51 | 1.00 | 357 |
| loop | 21 % → 21 % | 27.7 px | 0.52 | 1.00 | 179 |
| tilted | 11 % → 11 % | 30.4 px | 0.51 | 1.00 | 104 |
| over the wet one | 20 % → 20 % | 26.6 px | 0.51 | 1.00 | 85 |
| long, no reload | 49 % → 49 % | 22.0 px | 0.50 | 1.00 | 661 | quarters: 0.32 → 0.29 → 0.26 → 0.22

Numbers say: light vs heavy: width 27.6 → 30.4 px, dark 0.51 → 0.51; pressure barely changes the width.

## Oil — impasto
Oil · 34 px · 17.8 s

![Oil — impasto](Oil-impasto.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 12 % → 12 % | 33.5 px | 0.24 | 1.00 | 97 |
| heavy line | 13 % → 13 % | 36.4 px | 0.23 | 1.00 | 102 |
| pressure swell | 10 % → 10 % | 35.9 px | 0.26 | 1.00 | 72 |
| fast wave | 30 % → 30 % | 35.1 px | 0.24 | 1.00 | 253 |
| slow wave | 31 % → 31 % | 35.8 px | 0.24 | 1.00 | 442 |
| spiral | 52 % → 52 % | 34.1 px | 0.22 | 1.00 | 431 |
| loop | 26 % → 26 % | 33.7 px | 0.24 | 1.00 | 227 |
| tilted | 12 % → 12 % | 32.8 px | 0.24 | 1.00 | 175 |
| over the wet one | 23 % → 23 % | 32.0 px | 0.24 | 1.00 | 162 |
| long, no reload | 60 % → 60 % | 27.0 px | 0.22 | 1.00 | 800 | quarters: 0.18 → 0.16 → 0.13 → 0.10

Numbers say: light vs heavy: width 33.5 → 36.4 px, dark 0.24 → 0.23; pressure barely changes the width.

## Oil — glaze
Oil · 40 px · 15.0 s

![Oil — glaze](Oil-glaze.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 9 % → 9 % | 25.4 px | 0.50 | 1.00 | 85 |
| heavy line | 13 % → 13 % | 36.3 px | 0.49 | 1.00 | 105 |
| pressure swell | 9 % → 9 % | 35.3 px | 0.50 | 1.00 | 72 |
| fast wave | 26 % → 26 % | 30.1 px | 0.48 | 1.00 | 253 |
| slow wave | 29 % → 29 % | 33.7 px | 0.49 | 1.00 | 409 |
| spiral | 44 % → 44 % | 29.0 px | 0.49 | 1.00 | 401 |
| loop | 23 % → 23 % | 30.2 px | 0.50 | 1.00 | 212 |
| tilted | 10 % → 10 % | 28.9 px | 0.50 | 1.00 | 176 |
| over the wet one | 22 % → 22 % | 31.6 px | 0.50 | 1.00 | 142 |
| long, no reload | 51 % → 51 % | 22.7 px | 0.49 | 1.00 | 944 | quarters: 0.33 → 0.29 → 0.26 → 0.22

Numbers say: light vs heavy: width 25.4 → 36.3 px, dark 0.50 → 0.49.

## Oil — scumble
Oil · 36 px · 14.4 s

![Oil — scumble](Oil-scumble.png)

A light paint: laid on a grey sheet (on white it cannot be seen); **dark** = how far it is from the grey either way.

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 11 % → 11 % | 33.1 px | 0.28 | 1.00 | 116 |
| heavy line | 12 % → 12 % | 36.1 px | 0.28 | 1.00 | 125 |
| pressure swell | 9 % → 9 % | 35.5 px | 0.28 | 1.00 | 91 |
| fast wave | 26 % → 26 % | 29.6 px | 0.19 | 1.00 | 316 |
| slow wave | 27 % → 27 % | 30.9 px | 0.18 | 1.00 | 525 |
| spiral | 41 % → 41 % | 27.1 px | 0.13 | 1.00 | 547 |
| loop | 24 % → 24 % | 30.7 px | 0.20 | 1.00 | 368 |
| tilted | 11 % → 11 % | 30.5 px | 0.25 | 1.00 | 209 |
| over the wet one | 22 % → 22 % | 31.5 px | 0.25 | 1.00 | 169 |
| long, no reload | 45 % → 45 % | 20.3 px | 0.12 | 1.00 | 777 | quarters: 0.00 → 0.00 → 0.00 → 0.00

Numbers say: light vs heavy: width 33.1 → 36.1 px, dark 0.28 → 0.28; pressure barely changes the width.

## Acrylic — heavy body
Heavy acrylic · 30 px · 16.6 s

![Acrylic — heavy body](Acrylic-heavy-body.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 10 % → 9 % | 29.0 px | 0.51 | 0.90 | 87 |
| heavy line | 11 % → 10 % | 31.2 px | 0.51 | 0.92 | 89 |
| pressure swell | 8 % → 8 % | 30.8 px | 0.53 | 0.94 | 95 |
| fast wave | 23 % → 15 % | 26.5 px | 0.52 | 0.64 | 298 |
| slow wave | 24 % → 16 % | 27.8 px | 0.51 | 0.64 | 500 |
| spiral | 35 % → 15 % | 23.3 px | 0.51 | 0.43 | 370 |
| loop | 21 % → 16 % | 26.9 px | 0.51 | 0.76 | 198 |
| tilted | 9 % → 9 % | 24.9 px | 0.51 | 0.99 | 107 |
| over the wet one | 19 % → 17 % | 27.8 px | 0.51 | 0.89 | 92 |
| long, no reload | 39 % → 16 % | 17.3 px | 0.51 | 0.41 | 536 | quarters: 0.29 → 0.20 → 0.12 → 0.04

Numbers say: light vs heavy: width 29.0 → 31.2 px, dark 0.51 → 0.51; pressure barely changes the width.

## Acrylic — fluid
Watercolor · 36 px · 29.3 s

![Acrylic — fluid](Acrylic-fluid.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 12 % → 12 % | 34.3 px | 0.08 | 1.02 | 93 |
| heavy line | 18 % → 18 % | 51.6 px | 0.07 | 1.01 | 74 |
| pressure swell | 12 % → 12 % | 44.8 px | 0.08 | 1.01 | 54 |
| fast wave | 37 % → 38 % | 42.6 px | 0.07 | 1.02 | 180 |
| slow wave | 34 % → 35 % | 39.2 px | 0.07 | 1.03 | 307 |
| spiral | 52 % → 53 % | 34.2 px | 0.07 | 1.03 | 315 |
| loop | 30 % → 31 % | 39.4 px | 0.07 | 1.02 | 166 |
| tilted | 12 % → 12 % | 32.6 px | 0.08 | 1.04 | 93 |
| over the wet one | 27 % → 28 % | 43.2 px | 0.08 | 1.02 | 73 |
| long, no reload | 56 % → 58 % | 25.3 px | 0.06 | 1.04 | 444 | quarters: 0.06 → 0.05 → 0.03 → 0.02

Numbers say: light vs heavy: width 34.3 → 51.6 px, dark 0.08 → 0.07.

## Acrylic — palette knife
Heavy acrylic · 42 px · 19.3 s

![Acrylic — palette knife](Acrylic-palette-knife.png)

A light paint: laid on a grey sheet (on white it cannot be seen); **dark** = how far it is from the grey either way.

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 15 % → 15 % | 44.0 px | 0.39 | 0.98 | 25 |
| heavy line | 15 % → 15 % | 44.2 px | 0.40 | 0.97 | 24 |
| pressure swell | 12 % → 12 % | 43.5 px | 0.42 | 0.99 | 11 |
| fast wave | 36 % → 20 % | 41.9 px | 0.36 | 0.56 | 69 |
| slow wave | 37 % → 21 % | 42.6 px | 0.37 | 0.57 | 123 |
| spiral | 50 % → 18 % | 32.7 px | 0.37 | 0.37 | 92 |
| loop | 32 % → 24 % | 41.2 px | 0.36 | 0.75 | 52 |
| tilted | 12 % → 12 % | 33.6 px | 0.39 | 1.00 | 22 |
| over the wet one | 26 % → 25 % | 39.7 px | 0.39 | 0.97 | 23 |
| long, no reload | 57 % → 21 % | 25.6 px | 0.34 | 0.36 | 123 | quarters: 0.00 → 0.00 → 0.00 → 0.01

Numbers say: light vs heavy: width 44.0 → 44.2 px, dark 0.39 → 0.40; pressure barely changes the width; the long stroke does not run out of paint.

## Finger on oil
Oil · 30 px · 14.0 s

![Finger on oil](Finger-on-oil.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 8 % → 8 % | 23.8 px | 0.41 | 1.00 | 46 |
| heavy line | 13 % → 13 % | 36.6 px | 0.39 | 1.00 | 63 |
| pressure swell | 9 % → 9 % | 33.4 px | 0.41 | 1.00 | 40 |
| fast wave | 22 % → 22 % | 26.0 px | 0.35 | 1.00 | 132 |
| slow wave | 24 % → 24 % | 27.9 px | 0.35 | 1.00 | 211 |
| spiral | 36 % → 36 % | 23.5 px | 0.28 | 1.00 | 211 |
| loop | 21 % → 21 % | 27.4 px | 0.36 | 1.00 | 108 |
| tilted | 10 % → 10 % | 26.5 px | 0.40 | 1.00 | 77 |
| over the wet one | 20 % → 20 % | 29.4 px | 0.40 | 1.00 | 51 |
| long, no reload | 37 % → 37 % | 16.4 px | 0.26 | 1.00 | 314 | quarters: 0.23 → 0.11 → 0.05 → 0.02

Numbers say: light vs heavy: width 23.8 → 36.6 px, dark 0.41 → 0.39.

## Palette knife — oil
Oil · 44 px · 16.6 s

![Palette knife — oil](Palette-knife-oil.png)

A light paint: laid on a grey sheet (on white it cannot be seen); **dark** = how far it is from the grey either way.

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 16 % → 16 % | 45.6 px | 0.36 | 1.00 | 25 |
| heavy line | 16 % → 16 % | 46.3 px | 0.38 | 1.00 | 24 |
| pressure swell | 12 % → 12 % | 45.2 px | 0.38 | 1.00 | 11 |
| fast wave | 39 % → 39 % | 44.9 px | 0.34 | 1.01 | 60 |
| slow wave | 39 % → 39 % | 45.4 px | 0.35 | 1.00 | 96 |
| spiral | 62 % → 62 % | 40.9 px | 0.27 | 1.00 | 108 |
| loop | 34 % → 34 % | 43.8 px | 0.35 | 1.00 | 53 |
| tilted | 13 % → 13 % | 36.6 px | 0.37 | 1.00 | 23 |
| over the wet one | 28 % → 28 % | 40.8 px | 0.37 | 1.00 | 25 |
| long, no reload | 74 % → 74 % | 33.1 px | 0.25 | 1.00 | 144 | quarters: 0.00 → 0.00 → 0.00 → 0.00

Numbers say: light vs heavy: width 45.6 → 46.3 px, dark 0.36 → 0.38; pressure barely changes the width; the long stroke does not run out of paint.

## 0.45 · Sponge
Watercolor · 46 px · 29.1 s

![0.45 · Sponge](0-45-Sponge.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 23 % → 15 % | 66.4 px | 0.02 | 0.67 | 51 |
| heavy line | 28 % → 23 % | 81.1 px | 0.02 | 0.81 | 70 |
| pressure swell | 20 % → 16 % | 76.7 px | 0.03 | 0.76 | 45 |
| fast wave | 46 % → 32 % | 53.0 px | 0.03 | 0.70 | 149 |
| slow wave | 53 % → 46 % | 60.7 px | 0.04 | 0.87 | 261 |
| spiral | 65 % → 53 % | 42.6 px | 0.04 | 0.82 | 281 |
| loop | 46 % → 40 % | 60.1 px | 0.04 | 0.86 | 158 |
| tilted | 16 % → 17 % | 43.8 px | 0.05 | 1.07 | 106 |
| over the wet one | 40 % → 35 % | 67.3 px | 0.05 | 0.89 | 96 |
| long, no reload | 74 % → 65 % | 33.2 px | 0.04 | 0.88 | 475 | quarters: 0.05 → 0.04 → 0.03 → 0.02

Numbers say: light vs heavy: width 66.4 → 81.1 px, dark 0.02 → 0.02.

## 0.45 · Eraser
Eraser · 30 px · 18.9 s · over bands of wet oil paint and oil pastel in turn (it works on paint already there: look at what it does to the bands; covered counts the bands too)

![0.45 · Eraser](0-45-Eraser.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 24 % → 24 % | 69.2 px | 0.82 | 1.00 | 41 |
| heavy line | 23 % → 23 % | 67.4 px | 0.81 | 1.00 | 64 |
| pressure swell | 23 % → 23 % | 86.7 px | 0.82 | 1.00 | 37 |
| fast wave | 21 % → 21 % | 24.7 px | 0.81 | 1.00 | 126 |
| slow wave | 20 % → 20 % | 23.5 px | 0.82 | 1.00 | 214 |
| spiral | 20 % → 20 % | 13.5 px | 0.79 | 1.00 | 293 |
| loop | 21 % → 21 % | 27.8 px | 0.80 | 1.00 | 136 |
| tilted | 23 % → 23 % | 64.8 px | 0.81 | 1.00 | 82 |
| over the wet one | 22 % → 22 % | 0.0 px | 0.81 | 1.00 | 62 |
| long, no reload | 17 % → 17 % | 7.5 px | 0.79 | 1.00 | 307 | quarters: 0.13 → 0.16 → 0.13 → 0.17

Numbers say: light vs heavy: width 69.2 → 67.4 px, dark 0.82 → 0.81; pressure barely changes the width; the long stroke does not run out of paint.

## Lift wet paint
Eraser · 30 px · 18.8 s · over bands of wet oil paint and oil pastel in turn (it works on paint already there: look at what it does to the bands; covered counts the bands too)

![Lift wet paint](Lift-wet-paint.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 24 % → 24 % | 70.1 px | 0.82 | 1.00 | 41 |
| heavy line | 24 % → 24 % | 69.8 px | 0.82 | 1.00 | 50 |
| pressure swell | 24 % → 24 % | 89.5 px | 0.82 | 1.00 | 39 |
| fast wave | 24 % → 24 % | 27.7 px | 0.82 | 1.00 | 128 |
| slow wave | 24 % → 24 % | 27.7 px | 0.82 | 1.00 | 162 |
| spiral | 24 % → 24 % | 15.9 px | 0.82 | 1.00 | 161 |
| loop | 24 % → 24 % | 31.1 px | 0.82 | 1.00 | 90 |
| tilted | 24 % → 24 % | 66.8 px | 0.82 | 1.00 | 49 |
| over the wet one | 24 % → 24 % | 0.0 px | 0.82 | 1.00 | 41 |
| long, no reload | 24 % → 24 % | 10.7 px | 0.82 | 1.00 | 245 | quarters: 0.18 → 0.24 → 0.17 → 0.24

Numbers say: light vs heavy: width 70.1 → 69.8 px, dark 0.82 → 0.82; pressure barely changes the width; the long stroke does not run out of paint.

## Sgraffito
Eraser · 10 px · 18.2 s · over bands of wet oil paint and oil pastel in turn (it works on paint already there: look at what it does to the bands; covered counts the bands too)

![Sgraffito](Sgraffito.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 24 % → 24 % | 69.5 px | 0.81 | 1.00 | 8 |
| heavy line | 24 % → 24 % | 69.5 px | 0.82 | 1.00 | 8 |
| pressure swell | 24 % → 24 % | 89.5 px | 0.82 | 1.00 | 5 |
| fast wave | 24 % → 24 % | 27.4 px | 0.82 | 1.00 | 18 |
| slow wave | 24 % → 24 % | 27.4 px | 0.81 | 1.00 | 18 |
| spiral | 24 % → 24 % | 15.7 px | 0.81 | 1.00 | 32 |
| loop | 24 % → 24 % | 30.9 px | 0.82 | 1.00 | 17 |
| tilted | 24 % → 24 % | 66.6 px | 0.82 | 1.00 | 8 |
| over the wet one | 24 % → 24 % | 0.0 px | 0.82 | 1.00 | 7 |
| long, no reload | 24 % → 24 % | 10.6 px | 0.82 | 1.00 | 48 | quarters: 0.17 → 0.24 → 0.17 → 0.24

Numbers say: light vs heavy: width 69.5 → 69.5 px, dark 0.81 → 0.82; pressure barely changes the width; the long stroke does not run out of paint.

## Brush Artist · Refs · #01 Henry Ward peach cloud
Gouache · 44 px · 32.6 s

![Brush Artist · Refs · #01 Henry Ward peach cloud](Brush-Artist-Refs-01-Henry-Ward-peach-cloud.png)

A light paint: laid on a grey sheet (on white it cannot be seen); **dark** = how far it is from the grey either way.

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 15 % → 12 % | 42.2 px | 0.32 | 0.80 | 132 |
| heavy line | 16 % → 13 % | 45.5 px | 0.32 | 0.84 | 141 |
| pressure swell | 12 % → 10 % | 44.0 px | 0.32 | 0.87 | 131 |
| fast wave | 37 % → 18 % | 43.1 px | 0.32 | 0.48 | 481 |
| slow wave | 37 % → 18 % | 43.1 px | 0.32 | 0.48 | 619 |
| spiral | 59 % → 19 % | 39.1 px | 0.32 | 0.32 | 622 |
| loop | 32 % → 19 % | 41.3 px | 0.32 | 0.60 | 317 |
| tilted | 13 % → 13 % | 36.7 px | 0.32 | 0.99 | 176 |
| over the wet one | 27 % → 23 % | 38.9 px | 0.32 | 0.85 | 142 |
| long, no reload | 69 % → 20 % | 30.8 px | 0.32 | 0.29 | 868 | quarters: 0.01 → 0.01 → 0.01 → 0.02

Numbers say: light vs heavy: width 42.2 → 45.5 px, dark 0.32 → 0.32; pressure barely changes the width; the long stroke does not run out of paint.

## Brush Artist · Refs · #02 Henry Ward cream strokes
Gouache · 46 px · 31.2 s

![Brush Artist · Refs · #02 Henry Ward cream strokes](Brush-Artist-Refs-02-Henry-Ward-cream-strokes.png)

A light paint: laid on a grey sheet (on white it cannot be seen); **dark** = how far it is from the grey either way.

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 14 % → 13 % | 40.8 px | 0.41 | 0.90 | 134 |
| heavy line | 15 % → 14 % | 43.9 px | 0.41 | 0.92 | 140 |
| pressure swell | 11 % → 11 % | 42.8 px | 0.41 | 0.94 | 102 |
| fast wave | 36 % → 18 % | 41.0 px | 0.40 | 0.50 | 383 |
| slow wave | 36 % → 18 % | 41.1 px | 0.40 | 0.49 | 620 |
| spiral | 58 % → 19 % | 38.1 px | 0.40 | 0.33 | 601 |
| loop | 31 % → 20 % | 39.7 px | 0.40 | 0.64 | 316 |
| tilted | 13 % → 13 % | 36.9 px | 0.41 | 0.99 | 211 |
| over the wet one | 27 % → 23 % | 37.9 px | 0.41 | 0.86 | 189 |
| long, no reload | 67 % → 21 % | 30.1 px | 0.40 | 0.31 | 894 | quarters: 0.01 → 0.01 → 0.01 → 0.02

Numbers say: light vs heavy: width 40.8 → 43.9 px, dark 0.41 → 0.41; pressure barely changes the width; the long stroke does not run out of paint.

## Brush Artist · Refs · #03 Henry Ward navy contours
Heavy acrylic · 22 px · 12.9 s

![Brush Artist · Refs · #03 Henry Ward navy contours](Brush-Artist-Refs-03-Henry-Ward-navy-contours.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 7 % → 7 % | 21.6 px | 0.70 | 0.94 | 73 |
| heavy line | 8 % → 8 % | 23.5 px | 0.70 | 0.95 | 75 |
| pressure swell | 6 % → 6 % | 23.2 px | 0.73 | 0.94 | 51 |
| fast wave | 19 % → 12 % | 21.8 px | 0.72 | 0.66 | 179 |
| slow wave | 19 % → 13 % | 22.5 px | 0.72 | 0.69 | 282 |
| spiral | 30 % → 13 % | 19.5 px | 0.72 | 0.45 | 298 |
| loop | 17 % → 13 % | 21.5 px | 0.72 | 0.81 | 161 |
| tilted | 8 % → 8 % | 22.6 px | 0.71 | 1.00 | 87 |
| over the wet one | 16 % → 14 % | 21.4 px | 0.71 | 0.89 | 74 |
| long, no reload | 34 % → 13 % | 15.1 px | 0.72 | 0.40 | 436 | quarters: 0.35 → 0.29 → 0.20 → 0.08

Numbers say: light vs heavy: width 21.6 → 23.5 px, dark 0.70 → 0.70; pressure barely changes the width.

## Brush Artist · Refs · #04 Henry Ward grey cloud
Gouache · 50 px · 33.0 s

![Brush Artist · Refs · #04 Henry Ward grey cloud](Brush-Artist-Refs-04-Henry-Ward-grey-cloud.png)

A light paint: laid on a grey sheet (on white it cannot be seen); **dark** = how far it is from the grey either way.

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 16 % → 14 % | 46.7 px | 0.31 | 0.85 | 156 |
| heavy line | 17 % → 15 % | 50.2 px | 0.31 | 0.89 | 162 |
| pressure swell | 13 % → 12 % | 48.7 px | 0.31 | 0.91 | 115 |
| fast wave | 40 % → 20 % | 46.5 px | 0.31 | 0.50 | 411 |
| slow wave | 40 % → 20 % | 46.5 px | 0.31 | 0.49 | 864 |
| spiral | 61 % → 21 % | 40.0 px | 0.31 | 0.34 | 790 |
| loop | 35 % → 22 % | 45.2 px | 0.31 | 0.64 | 360 |
| tilted | 14 % → 14 % | 40.0 px | 0.31 | 0.99 | 211 |
| over the wet one | 30 % → 26 % | 42.8 px | 0.31 | 0.87 | 175 |
| long, no reload | 73 % → 23 % | 32.7 px | 0.31 | 0.31 | 1459 | quarters: 0.01 → 0.01 → 0.01 → 0.02

Numbers say: light vs heavy: width 46.7 → 50.2 px, dark 0.31 → 0.31; pressure barely changes the width; the long stroke does not run out of paint.

## Brush Artist · Refs · #05 Henry Ward green in rust loops
Heavy acrylic · 20 px · 13.9 s

![Brush Artist · Refs · #05 Henry Ward green in rust loops](Brush-Artist-Refs-05-Henry-Ward-green-in-rust-loops.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 7 % → 6 % | 19.5 px | 0.55 | 0.94 | 69 |
| heavy line | 7 % → 7 % | 21.4 px | 0.55 | 0.94 | 122 |
| pressure swell | 6 % → 5 % | 21.5 px | 0.57 | 0.92 | 85 |
| fast wave | 17 % → 11 % | 19.8 px | 0.56 | 0.64 | 322 |
| slow wave | 18 % → 12 % | 20.4 px | 0.56 | 0.66 | 429 |
| spiral | 27 % → 11 % | 17.9 px | 0.55 | 0.42 | 389 |
| loop | 15 % → 12 % | 19.5 px | 0.55 | 0.80 | 163 |
| tilted | 8 % → 8 % | 21.7 px | 0.56 | 1.00 | 87 |
| over the wet one | 15 % → 13 % | 19.3 px | 0.56 | 0.87 | 74 |
| long, no reload | 30 % → 12 % | 13.4 px | 0.56 | 0.39 | 553 | quarters: 0.25 → 0.18 → 0.10 → 0.02

Numbers say: light vs heavy: width 19.5 → 21.4 px, dark 0.55 → 0.55; pressure barely changes the width.

## Brush Artist · Refs · #06 Henry Ward scrubbed grey
Gouache · 50 px · 31.6 s

![Brush Artist · Refs · #06 Henry Ward scrubbed grey](Brush-Artist-Refs-06-Henry-Ward-scrubbed-grey.png)

A light paint: laid on a grey sheet (on white it cannot be seen); **dark** = how far it is from the grey either way.

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 16 % → 14 % | 46.7 px | 0.33 | 0.85 | 149 |
| heavy line | 17 % → 15 % | 50.2 px | 0.33 | 0.89 | 156 |
| pressure swell | 13 % → 12 % | 48.7 px | 0.33 | 0.91 | 149 |
| fast wave | 40 % → 20 % | 46.5 px | 0.33 | 0.50 | 422 |
| slow wave | 40 % → 20 % | 46.5 px | 0.33 | 0.49 | 709 |
| spiral | 61 % → 21 % | 40.0 px | 0.33 | 0.34 | 729 |
| loop | 35 % → 22 % | 45.2 px | 0.32 | 0.64 | 362 |
| tilted | 14 % → 14 % | 40.0 px | 0.33 | 0.99 | 193 |
| over the wet one | 30 % → 26 % | 42.8 px | 0.33 | 0.87 | 164 |
| long, no reload | 73 % → 23 % | 32.7 px | 0.32 | 0.31 | 995 | quarters: 0.01 → 0.01 → 0.01 → 0.02

Numbers say: light vs heavy: width 46.7 → 50.2 px, dark 0.33 → 0.33; pressure barely changes the width; the long stroke does not run out of paint.

## Brush Artist · Refs · #07 Henry Ward blue L + black zigzag
Heavy acrylic · 34 px · 15.0 s

![Brush Artist · Refs · #07 Henry Ward blue L + black zigzag](Brush-Artist-Refs-07-Henry-Ward-blue-L-black-zigzag.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 11 % → 11 % | 33.2 px | 0.57 | 0.93 | 93 |
| heavy line | 12 % → 12 % | 35.8 px | 0.57 | 0.93 | 96 |
| pressure swell | 9 % → 9 % | 35.2 px | 0.59 | 0.94 | 69 |
| fast wave | 29 % → 20 % | 33.6 px | 0.59 | 0.69 | 237 |
| slow wave | 30 % → 21 % | 34.2 px | 0.58 | 0.72 | 412 |
| spiral | 47 % → 22 % | 31.3 px | 0.58 | 0.46 | 412 |
| loop | 25 % → 21 % | 32.7 px | 0.58 | 0.82 | 249 |
| tilted | 11 % → 11 % | 29.9 px | 0.58 | 1.00 | 157 |
| over the wet one | 22 % → 20 % | 31.8 px | 0.58 | 0.91 | 132 |
| long, no reload | 53 % → 22 % | 23.8 px | 0.59 | 0.42 | 686 | quarters: 0.40 → 0.32 → 0.21 → 0.10

Numbers say: light vs heavy: width 33.2 → 35.8 px, dark 0.57 → 0.57; pressure barely changes the width.

## Brush Artist · Refs · #08 Henry Ward olive bands
Gouache · 34 px · 21.6 s

![Brush Artist · Refs · #08 Henry Ward olive bands](Brush-Artist-Refs-08-Henry-Ward-olive-bands.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 8 % → 2 % | 24.7 px | 0.57 | 0.27 | 69 |
| heavy line | 12 % → 3 % | 33.9 px | 0.57 | 0.22 | 134 |
| pressure swell | 8 % → 3 % | 30.8 px | 0.57 | 0.38 | 77 |
| fast wave | 25 % → 4 % | 29.2 px | 0.57 | 0.15 | 250 |
| slow wave | 25 % → 4 % | 28.9 px | 0.57 | 0.15 | 426 |
| spiral | 39 % → 4 % | 25.7 px | 0.57 | 0.10 | 420 |
| loop | 22 % → 5 % | 28.8 px | 0.57 | 0.21 | 222 |
| tilted | 10 % → 10 % | 28.6 px | 0.57 | 0.98 | 118 |
| over the wet one | 20 % → 8 % | 28.3 px | 0.57 | 0.40 | 101 |
| long, no reload | 45 % → 6 % | 20.0 px | 0.57 | 0.13 | 707 | quarters: 0.35 → 0.27 → 0.17 → 0.08

Numbers say: light vs heavy: width 24.7 → 33.9 px, dark 0.57 → 0.57.

## Brush Artist · Refs · #09 Henry Ward white loops
Gouache · 46 px · 30.6 s

![Brush Artist · Refs · #09 Henry Ward white loops](Brush-Artist-Refs-09-Henry-Ward-white-loops.png)

A light paint: laid on a grey sheet (on white it cannot be seen); **dark** = how far it is from the grey either way.

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 14 % → 13 % | 40.8 px | 0.43 | 0.90 | 136 |
| heavy line | 15 % → 14 % | 43.9 px | 0.43 | 0.92 | 199 |
| pressure swell | 11 % → 11 % | 42.8 px | 0.44 | 0.94 | 141 |
| fast wave | 36 % → 18 % | 41.0 px | 0.43 | 0.50 | 381 |
| slow wave | 36 % → 18 % | 41.1 px | 0.43 | 0.49 | 628 |
| spiral | 58 % → 19 % | 38.1 px | 0.42 | 0.33 | 630 |
| loop | 31 % → 20 % | 39.7 px | 0.42 | 0.64 | 319 |
| tilted | 13 % → 13 % | 36.9 px | 0.43 | 0.99 | 170 |
| over the wet one | 27 % → 23 % | 37.9 px | 0.43 | 0.86 | 148 |
| long, no reload | 67 % → 21 % | 30.1 px | 0.42 | 0.31 | 897 | quarters: 0.01 → 0.01 → 0.01 → 0.02

Numbers say: light vs heavy: width 40.8 → 43.9 px, dark 0.43 → 0.43; pressure barely changes the width; the long stroke does not run out of paint.

## Brush Artist · Refs · #10 Henry Ward maroon loops
Heavy acrylic · 30 px · 14.2 s

![Brush Artist · Refs · #10 Henry Ward maroon loops](Brush-Artist-Refs-10-Henry-Ward-maroon-loops.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 10 % → 9 % | 28.0 px | 0.71 | 0.94 | 81 |
| heavy line | 10 % → 10 % | 30.3 px | 0.71 | 0.95 | 92 |
| pressure swell | 8 % → 8 % | 30.0 px | 0.73 | 0.94 | 59 |
| fast wave | 25 % → 17 % | 28.3 px | 0.73 | 0.71 | 215 |
| slow wave | 25 % → 18 % | 29.0 px | 0.73 | 0.73 | 365 |
| spiral | 39 % → 18 % | 26.0 px | 0.72 | 0.47 | 363 |
| loop | 21 % → 18 % | 27.6 px | 0.72 | 0.85 | 187 |
| tilted | 10 % → 10 % | 27.9 px | 0.72 | 1.00 | 104 |
| over the wet one | 20 % → 18 % | 27.0 px | 0.72 | 0.91 | 85 |
| long, no reload | 46 % → 18 % | 20.6 px | 0.73 | 0.40 | 515 | quarters: 0.44 → 0.38 → 0.31 → 0.22

Numbers say: light vs heavy: width 28.0 → 30.3 px, dark 0.71 → 0.71; pressure barely changes the width.

## Brush Artist · Refs · #11 Henry Ward purple spun balls
Heavy acrylic · 36 px · 15.0 s

![Brush Artist · Refs · #11 Henry Ward purple spun balls](Brush-Artist-Refs-11-Henry-Ward-purple-spun-balls.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 12 % → 11 % | 34.2 px | 0.71 | 0.96 | 133 |
| heavy line | 13 % → 12 % | 36.7 px | 0.71 | 0.95 | 105 |
| pressure swell | 10 % → 9 % | 36.2 px | 0.74 | 0.95 | 78 |
| fast wave | 30 % → 23 % | 34.6 px | 0.73 | 0.75 | 257 |
| slow wave | 30 % → 24 % | 35.0 px | 0.73 | 0.79 | 441 |
| spiral | 49 % → 25 % | 32.3 px | 0.73 | 0.50 | 438 |
| loop | 26 % → 23 % | 33.4 px | 0.73 | 0.88 | 229 |
| tilted | 11 % → 11 % | 31.2 px | 0.72 | 1.00 | 127 |
| over the wet one | 23 % → 21 % | 32.3 px | 0.72 | 0.93 | 103 |
| long, no reload | 55 % → 24 % | 24.8 px | 0.73 | 0.44 | 620 | quarters: 0.51 → 0.46 → 0.39 → 0.28

Numbers say: light vs heavy: width 34.2 → 36.7 px, dark 0.71 → 0.71; pressure barely changes the width.

## Brush Artist · Refs · #12 Henry Ward black-olive cage
Gouache · 28 px · 21.9 s

![Brush Artist · Refs · #12 Henry Ward black-olive cage](Brush-Artist-Refs-12-Henry-Ward-black-olive-cage.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 7 % → 3 % | 20.9 px | 0.61 | 0.35 | 54 |
| heavy line | 9 % → 4 % | 26.1 px | 0.61 | 0.41 | 112 |
| pressure swell | 6 % → 4 % | 23.9 px | 0.61 | 0.61 | 65 |
| fast wave | 20 % → 4 % | 23.7 px | 0.61 | 0.19 | 210 |
| slow wave | 20 % → 4 % | 23.3 px | 0.61 | 0.21 | 357 |
| spiral | 32 % → 4 % | 21.4 px | 0.61 | 0.14 | 461 |
| loop | 18 % → 5 % | 22.8 px | 0.61 | 0.28 | 275 |
| tilted | 9 % → 9 % | 25.4 px | 0.61 | 0.98 | 98 |
| over the wet one | 17 % → 8 % | 21.8 px | 0.61 | 0.46 | 86 |
| long, no reload | 39 % → 6 % | 17.6 px | 0.61 | 0.15 | 520 | quarters: 0.31 → 0.26 → 0.19 → 0.10

Numbers say: light vs heavy: width 20.9 → 26.1 px, dark 0.61 → 0.61.

## Brush Artist · Refs · #13 Henry Ward blue streaky form
Gouache · 50 px · 43.0 s

![Brush Artist · Refs · #13 Henry Ward blue streaky form](Brush-Artist-Refs-13-Henry-Ward-blue-streaky-form.png)

A light paint: laid on a grey sheet (on white it cannot be seen); **dark** = how far it is from the grey either way.

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 16 % → 14 % | 46.7 px | 0.33 | 0.85 | 148 |
| heavy line | 17 % → 15 % | 50.2 px | 0.33 | 0.89 | 154 |
| pressure swell | 13 % → 12 % | 48.7 px | 0.33 | 0.91 | 112 |
| fast wave | 40 % → 20 % | 46.5 px | 0.33 | 0.50 | 399 |
| slow wave | 40 % → 20 % | 46.5 px | 0.33 | 0.49 | 685 |
| spiral | 61 % → 21 % | 40.0 px | 0.32 | 0.34 | 689 |
| loop | 35 % → 22 % | 45.2 px | 0.32 | 0.64 | 475 |
| tilted | 14 % → 14 % | 40.0 px | 0.33 | 0.99 | 321 |
| over the wet one | 30 % → 26 % | 42.8 px | 0.33 | 0.87 | 200 |
| long, no reload | 73 % → 23 % | 32.7 px | 0.32 | 0.31 | 1202 | quarters: 0.01 → 0.01 → 0.01 → 0.02

Numbers say: light vs heavy: width 46.7 → 50.2 px, dark 0.33 → 0.33; pressure barely changes the width; the long stroke does not run out of paint.

## Brush Artist · Refs · #14 Henry Ward olive totem
Heavy acrylic · 48 px · 22.3 s

![Brush Artist · Refs · #14 Henry Ward olive totem](Brush-Artist-Refs-14-Henry-Ward-olive-totem.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 15 % → 15 % | 44.8 px | 0.31 | 0.94 | 136 |
| heavy line | 16 % → 16 % | 47.7 px | 0.31 | 0.95 | 140 |
| pressure swell | 13 % → 12 % | 47.0 px | 0.32 | 0.95 | 100 |
| fast wave | 38 % → 30 % | 43.9 px | 0.30 | 0.79 | 348 |
| slow wave | 39 % → 31 % | 44.6 px | 0.30 | 0.81 | 598 |
| spiral | 58 % → 32 % | 38.2 px | 0.30 | 0.55 | 586 |
| loop | 33 % → 29 % | 42.7 px | 0.30 | 0.89 | 311 |
| tilted | 13 % → 13 % | 37.5 px | 0.31 | 1.00 | 168 |
| over the wet one | 28 % → 26 % | 41.2 px | 0.31 | 0.93 | 147 |
| long, no reload | 68 % → 33 % | 30.3 px | 0.30 | 0.49 | 998 | quarters: 0.25 → 0.18 → 0.10 → 0.03

Numbers say: light vs heavy: width 44.8 → 47.7 px, dark 0.31 → 0.31; pressure barely changes the width.

## Brush Artist · Refs · #15 Ultramarine brush script
Ink · 4 px · 29.9 s

![Brush Artist · Refs · #15 Ultramarine brush script](Brush-Artist-Refs-15-Ultramarine-brush-script.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 1 % → 3 % | 2.2 px | 0.55 | 3.86 | 58 |
| heavy line | 6 % → 6 % | 16.6 px | 0.58 | 0.99 | 127 |
| pressure swell | 3 % → 4 % | 12.0 px | 0.64 | 1.15 | 54 |
| fast wave | 9 % → 7 % | 10.5 px | 0.55 | 0.82 | 156 |
| slow wave | 7 % → 7 % | 8.4 px | 0.54 | 0.93 | 142 |
| spiral | 11 % → 7 % | 7.2 px | 0.52 | 0.68 | 272 |
| loop | 7 % → 7 % | 9.2 px | 0.53 | 0.99 | 157 |
| tilted | 3 % → 3 % | 8.0 px | 0.62 | 1.02 | 73 |
| over the wet one | 7 % → 7 % | 11.4 px | 0.62 | 1.05 | 72 |
| long, no reload | 16 % → 8 % | 7.3 px | 0.50 | 0.49 | 330 | quarters: 0.14 → 0.04 → 0.01 → 0.00

Numbers say: light vs heavy: width 2.2 → 16.6 px, dark 0.55 → 0.58; wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #18 Blue oil-stick scribbles
Pastel · 10 px · 13.3 s

![Brush Artist · Refs · #18 Blue oil-stick scribbles](Brush-Artist-Refs-18-Blue-oil-stick-scribbles.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 1 % → 1 % | 2.9 px | 0.52 | 1.00 | 39 |
| heavy line | 2 % → 2 % | 5.5 px | 0.53 | 1.00 | 40 |
| pressure swell | 1 % → 1 % | 5.0 px | 0.53 | 1.00 | 30 |
| fast wave | 4 % → 4 % | 4.8 px | 0.53 | 1.00 | 93 |
| slow wave | 4 % → 4 % | 4.4 px | 0.53 | 1.00 | 89 |
| spiral | 7 % → 7 % | 4.5 px | 0.52 | 1.00 | 161 |
| loop | 3 % → 3 % | 4.5 px | 0.52 | 1.00 | 88 |
| tilted | 2 % → 2 % | 4.7 px | 0.53 | 1.00 | 43 |
| over the wet one | 3 % → 3 % | 4.7 px | 0.53 | 1.00 | 33 |
| long, no reload | 10 % → 10 % | 4.4 px | 0.53 | 1.00 | 230 | quarters: 0.06 → 0.06 → 0.06 → 0.06

Numbers say: light vs heavy: width 2.9 → 5.5 px, dark 0.52 → 0.53; the long stroke does not run out of paint.

## Brush Artist · Refs · #20 Orange-red crayon scribble
Pastel · 14 px · 14.3 s

![Brush Artist · Refs · #20 Orange-red crayon scribble](Brush-Artist-Refs-20-Orange-red-crayon-scribble.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 1 % → 1 % | 4.0 px | 0.53 | 1.00 | 54 |
| heavy line | 3 % → 3 % | 8.0 px | 0.53 | 1.00 | 30 |
| pressure swell | 2 % → 2 % | 7.6 px | 0.53 | 1.00 | 24 |
| fast wave | 6 % → 6 % | 7.2 px | 0.53 | 1.00 | 106 |
| slow wave | 6 % → 6 % | 6.6 px | 0.53 | 1.00 | 112 |
| spiral | 9 % → 9 % | 6.2 px | 0.53 | 1.00 | 157 |
| loop | 5 % → 5 % | 6.2 px | 0.53 | 1.00 | 94 |
| tilted | 2 % → 2 % | 5.6 px | 0.53 | 1.00 | 55 |
| over the wet one | 4 % → 4 % | 6.6 px | 0.53 | 1.00 | 45 |
| long, no reload | 13 % → 13 % | 5.7 px | 0.53 | 1.00 | 277 | quarters: 0.07 → 0.07 → 0.08 → 0.08

Numbers say: light vs heavy: width 4.0 → 8.0 px, dark 0.53 → 0.53; the long stroke does not run out of paint.

## Brush Artist · Refs · #21 Gritty black contours
Gouache · 12 px · 24.4 s

![Brush Artist · Refs · #21 Gritty black contours](Brush-Artist-Refs-21-Gritty-black-contours.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 3 % → 0 % | 8.8 px | 0.79 | 0.12 | 87 |
| heavy line | 4 % → 0 % | 11.9 px | 0.79 | 0.10 | 130 |
| pressure swell | 3 % → 0 % | 11.6 px | 0.79 | 0.15 | 129 |
| fast wave | 7 % → 1 % | 8.5 px | 0.79 | 0.10 | 420 |
| slow wave | 8 % → 1 % | 9.0 px | 0.79 | 0.09 | 348 |
| spiral | 9 % → 1 % | 6.0 px | 0.79 | 0.10 | 452 |
| loop | 8 % → 1 % | 9.9 px | 0.79 | 0.09 | 277 |
| tilted | 4 % → 4 % | 10.8 px | 0.79 | 0.90 | 105 |
| over the wet one | 7 % → 1 % | 9.7 px | 0.79 | 0.17 | 91 |
| long, no reload | 7 % → 1 % | 3.3 px | 0.79 | 0.12 | 548 | quarters: 0.20 → 0.07 → 0.00 → 0.00

Numbers say: light vs heavy: width 8.8 → 11.9 px, dark 0.79 → 0.79.

## Brush Artist · Refs · #22 Bold black brush poster
Ink · 20 px · 32.6 s

![Brush Artist · Refs · #22 Bold black brush poster](Brush-Artist-Refs-22-Bold-black-brush-poster.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 3 % → 5 % | 9.5 px | 0.79 | 1.63 | 70 |
| heavy line | 15 % → 15 % | 44.6 px | 0.88 | 0.99 | 121 |
| pressure swell | 9 % → 9 % | 31.9 px | 0.87 | 1.04 | 89 |
| fast wave | 27 % → 26 % | 31.2 px | 0.87 | 0.98 | 261 |
| slow wave | 22 % → 21 % | 25.2 px | 0.87 | 0.98 | 395 |
| spiral | 34 % → 32 % | 22.2 px | 0.87 | 0.94 | 321 |
| loop | 20 % → 20 % | 26.2 px | 0.88 | 1.00 | 172 |
| tilted | 8 % → 8 % | 22.7 px | 0.88 | 1.01 | 76 |
| over the wet one | 19 % → 19 % | 30.5 px | 0.88 | 1.00 | 67 |
| long, no reload | 45 % → 38 % | 20.2 px | 0.86 | 0.84 | 417 | quarters: 0.54 → 0.45 → 0.35 → 0.27

Numbers say: light vs heavy: width 9.5 → 44.6 px, dark 0.79 → 0.88; wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #23 Dry white on orange + black line
Gouache · 50 px · 28.8 s

![Brush Artist · Refs · #23 Dry white on orange + black line](Brush-Artist-Refs-23-Dry-white-on-orange-black-line.png)

A light paint: laid on a grey sheet (on white it cannot be seen); **dark** = how far it is from the grey either way.

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 12 % → 2 % | 35.1 px | 0.39 | 0.13 | 138 |
| heavy line | 16 % → 2 % | 46.9 px | 0.39 | 0.11 | 227 |
| pressure swell | 11 % → 2 % | 42.6 px | 0.39 | 0.19 | 130 |
| fast wave | 34 % → 3 % | 39.7 px | 0.39 | 0.09 | 438 |
| slow wave | 34 % → 3 % | 39.0 px | 0.39 | 0.10 | 785 |
| spiral | 49 % → 4 % | 32.6 px | 0.38 | 0.07 | 815 |
| loop | 30 % → 4 % | 39.1 px | 0.38 | 0.12 | 594 |
| tilted | 13 % → 12 % | 34.9 px | 0.38 | 0.98 | 324 |
| over the wet one | 26 % → 7 % | 38.0 px | 0.38 | 0.27 | 200 |
| long, no reload | 58 % → 5 % | 26.1 px | 0.38 | 0.09 | 1066 | quarters: 0.02 → 0.02 → 0.03 → 0.04

Numbers say: light vs heavy: width 35.1 → 46.9 px, dark 0.39 → 0.39; the long stroke does not run out of paint.

## Brush Artist · Refs · #24 Picasso flat oil
Oil · 34 px · 20.8 s

![Brush Artist · Refs · #24 Picasso flat oil](Brush-Artist-Refs-24-Picasso-flat-oil.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 11 % → 11 % | 32.4 px | 0.40 | 1.00 | 153 |
| heavy line | 12 % → 12 % | 35.2 px | 0.40 | 1.00 | 143 |
| pressure swell | 9 % → 9 % | 34.4 px | 0.41 | 1.00 | 110 |
| fast wave | 30 % → 30 % | 34.2 px | 0.41 | 1.00 | 368 |
| slow wave | 30 % → 30 % | 35.0 px | 0.41 | 1.00 | 624 |
| spiral | 51 % → 51 % | 33.8 px | 0.40 | 1.00 | 998 |
| loop | 25 % → 25 % | 32.6 px | 0.41 | 1.00 | 530 |
| tilted | 11 % → 11 % | 32.0 px | 0.41 | 1.00 | 188 |
| over the wet one | 23 % → 23 % | 30.8 px | 0.41 | 1.00 | 149 |
| long, no reload | 62 % → 62 % | 27.6 px | 0.39 | 1.00 | 1012 | quarters: 0.28 → 0.28 → 0.26 → 0.24

Numbers say: light vs heavy: width 32.4 → 35.2 px, dark 0.40 → 0.40; pressure barely changes the width.

## Brush Artist · Refs · #25 Yellow heavy flat stroke
Heavy acrylic · 110 px · 47.0 s

![Brush Artist · Refs · #25 Yellow heavy flat stroke](Brush-Artist-Refs-25-Yellow-heavy-flat-stroke.png)

A light paint: laid on a grey sheet (on white it cannot be seen); **dark** = how far it is from the grey either way.

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 35 % → 36 % | 101.5 px | 0.30 | 1.02 | 477 |
| heavy line | 36 % → 35 % | 105.1 px | 0.31 | 0.97 | 595 |
| pressure swell | 28 % → 29 % | 105.4 px | 0.30 | 1.04 | 319 |
| fast wave | 73 % → 76 % | 83.8 px | 0.31 | 1.05 | 1231 |
| slow wave | 73 % → 72 % | 84.7 px | 0.30 | 0.98 | 2374 |
| spiral | 86 % → 83 % | 56.7 px | 0.29 | 0.97 | 4408 |
| loop | 65 % → 64 % | 83.6 px | 0.31 | 0.99 | 1017 |
| tilted | 26 % → 26 % | 71.5 px | 0.30 | 1.00 | 516 |
| over the wet one | 55 % → 54 % | 83.2 px | 0.30 | 0.97 | 459 |
| long, no reload | 98 % → 97 % | 44.1 px | 0.29 | 0.99 | 2660 | quarters: 0.00 → 0.00 → 0.00 → 0.00

Numbers say: light vs heavy: width 101.5 → 105.1 px, dark 0.30 → 0.31; pressure barely changes the width; the long stroke does not run out of paint.

## Brush Artist · Refs · #27 Orange impasto swatch
Heavy acrylic · 60 px · 27.0 s

![Brush Artist · Refs · #27 Orange impasto swatch](Brush-Artist-Refs-27-Orange-impasto-swatch.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 20 % → 19 % | 56.8 px | 0.34 | 0.97 | 210 |
| heavy line | 20 % → 20 % | 59.5 px | 0.34 | 0.97 | 231 |
| pressure swell | 16 % → 15 % | 59.6 px | 0.36 | 0.97 | 134 |
| fast wave | 48 % → 46 % | 55.0 px | 0.35 | 0.98 | 592 |
| slow wave | 48 % → 47 % | 55.9 px | 0.35 | 0.98 | 1246 |
| spiral | 69 % → 62 % | 45.5 px | 0.34 | 0.91 | 2042 |
| loop | 42 % → 40 % | 53.9 px | 0.35 | 0.97 | 574 |
| tilted | 16 % → 16 % | 44.0 px | 0.35 | 1.00 | 240 |
| over the wet one | 34 % → 33 % | 50.9 px | 0.35 | 0.96 | 204 |
| long, no reload | 85 % → 75 % | 38.1 px | 0.35 | 0.88 | 1188 | quarters: 0.33 → 0.31 → 0.29 → 0.26

Numbers say: light vs heavy: width 56.8 → 59.5 px, dark 0.34 → 0.34; pressure barely changes the width.

## Brush Artist · Refs · #28 Miles Davis black lines
Ink · 22 px · 30.8 s

![Brush Artist · Refs · #28 Miles Davis black lines](Brush-Artist-Refs-28-Miles-Davis-black-lines.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 4 % → 6 % | 12.2 px | 0.81 | 1.48 | 54 |
| heavy line | 17 % → 17 % | 49.1 px | 0.88 | 0.99 | 111 |
| pressure swell | 10 % → 10 % | 35.9 px | 0.87 | 1.03 | 51 |
| fast wave | 30 % → 30 % | 35.0 px | 0.87 | 0.98 | 157 |
| slow wave | 25 % → 25 % | 28.5 px | 0.87 | 0.99 | 235 |
| spiral | 38 % → 37 % | 25.3 px | 0.87 | 0.96 | 256 |
| loop | 23 % → 23 % | 29.4 px | 0.88 | 1.00 | 138 |
| tilted | 9 % → 9 % | 25.0 px | 0.88 | 1.01 | 72 |
| over the wet one | 21 % → 21 % | 34.1 px | 0.88 | 1.00 | 63 |
| long, no reload | 51 % → 43 % | 22.7 px | 0.86 | 0.85 | 384 | quarters: 0.59 → 0.51 → 0.40 → 0.31

Numbers say: light vs heavy: width 12.2 → 49.1 px, dark 0.81 → 0.88.

## Brush Artist · Refs · #29 Shrigley magenta asterisk
Watercolor · 70 px · 37.9 s

![Brush Artist · Refs · #29 Shrigley magenta asterisk](Brush-Artist-Refs-29-Shrigley-magenta-asterisk.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 10 % → 13 % | 28.0 px | 0.65 | 1.36 | 66 |
| heavy line | 17 % → 18 % | 50.3 px | 0.64 | 1.03 | 155 |
| pressure swell | 11 % → 12 % | 41.1 px | 0.65 | 1.13 | 93 |
| fast wave | 38 % → 38 % | 43.7 px | 0.64 | 1.00 | 432 |
| slow wave | 35 % → 39 % | 41.0 px | 0.65 | 1.10 | 732 |
| spiral | 61 % → 61 % | 40.0 px | 0.64 | 1.01 | 553 |
| loop | 31 % → 32 % | 40.2 px | 0.65 | 1.03 | 251 |
| tilted | 18 % → 18 % | 49.0 px | 0.65 | 1.00 | 251 |
| over the wet one | 31 % → 34 % | 38.4 px | 0.65 | 1.07 | 113 |
| long, no reload | 75 % → 75 % | 33.5 px | 0.64 | 1.00 | 688 | quarters: 0.55 → 0.53 → 0.52 → 0.49

Numbers say: light vs heavy: width 28.0 → 50.3 px, dark 0.65 → 0.64; the long stroke does not run out of paint.

## Brush Artist · Refs · #30 Red gouache face patch
Gouache · 60 px · 46.6 s

![Brush Artist · Refs · #30 Red gouache face patch](Brush-Artist-Refs-30-Red-gouache-face-patch.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 16 % → 15 % | 46.9 px | 0.49 | 0.91 | 171 |
| heavy line | 25 % → 20 % | 73.8 px | 0.49 | 0.80 | 247 |
| pressure swell | 19 % → 17 % | 72.6 px | 0.49 | 0.86 | 148 |
| fast wave | 48 % → 28 % | 55.1 px | 0.49 | 0.58 | 748 |
| slow wave | 48 % → 28 % | 55.3 px | 0.49 | 0.59 | 806 |
| spiral | 59 % → 28 % | 39.1 px | 0.49 | 0.48 | 1036 |
| loop | 40 % → 29 % | 51.3 px | 0.49 | 0.74 | 424 |
| tilted | 16 % → 16 % | 45.7 px | 0.49 | 1.01 | 262 |
| over the wet one | 36 % → 32 % | 55.3 px | 0.49 | 0.88 | 179 |
| long, no reload | 67 % → 30 % | 30.0 px | 0.49 | 0.45 | 1106 | quarters: 0.43 → 0.38 → 0.32 → 0.26

Numbers say: light vs heavy: width 46.9 → 73.8 px, dark 0.49 → 0.49.

## Brush Artist · Refs · #31 Warhol blotted line
Ink · 6 px · 25.8 s

![Brush Artist · Refs · #31 Warhol blotted line](Brush-Artist-Refs-31-Warhol-blotted-line.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 1 % → 3 % | 2.6 px | 0.75 | 3.30 | 49 |
| heavy line | 7 % → 7 % | 20.6 px | 0.83 | 0.97 | 95 |
| pressure swell | 4 % → 4 % | 14.8 px | 0.84 | 1.12 | 43 |
| fast wave | 12 % → 9 % | 13.8 px | 0.82 | 0.77 | 122 |
| slow wave | 10 % → 8 % | 11.2 px | 0.80 | 0.85 | 142 |
| spiral | 15 % → 9 % | 9.7 px | 0.80 | 0.58 | 259 |
| loop | 9 % → 9 % | 11.9 px | 0.80 | 0.94 | 137 |
| tilted | 3 % → 3 % | 8.6 px | 0.84 | 1.04 | 49 |
| over the wet one | 8 % → 8 % | 14.5 px | 0.84 | 1.02 | 50 |
| long, no reload | 21 % → 9 % | 9.6 px | 0.78 | 0.43 | 321 | quarters: 0.25 → 0.13 → 0.05 → 0.01

Numbers say: light vs heavy: width 2.6 → 20.6 px, dark 0.75 → 0.83; wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #32 Thick orange swipes
Heavy acrylic · 90 px · 40.9 s

![Brush Artist · Refs · #32 Thick orange swipes](Brush-Artist-Refs-32-Thick-orange-swipes.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 29 % → 29 % | 83.1 px | 0.38 | 1.00 | 362 |
| heavy line | 30 % → 29 % | 86.4 px | 0.38 | 0.97 | 399 |
| pressure swell | 23 % → 23 % | 86.5 px | 0.38 | 1.01 | 291 |
| fast wave | 63 % → 65 % | 73.1 px | 0.38 | 1.03 | 1286 |
| slow wave | 64 % → 63 % | 73.5 px | 0.38 | 0.98 | 1844 |
| spiral | 79 % → 77 % | 52.2 px | 0.38 | 0.98 | 1557 |
| loop | 57 % → 56 % | 73.4 px | 0.38 | 0.99 | 838 |
| tilted | 21 % → 21 % | 59.3 px | 0.38 | 1.00 | 731 |
| over the wet one | 47 % → 45 % | 71.0 px | 0.38 | 0.97 | 622 |
| long, no reload | 95 % → 93 % | 42.8 px | 0.38 | 0.97 | 3358 | quarters: 0.38 → 0.38 → 0.37 → 0.35

Numbers say: light vs heavy: width 83.1 → 86.4 px, dark 0.38 → 0.38; pressure barely changes the width; the long stroke does not run out of paint.

## Brush Artist · Refs · #33 Red wet-in-wet band
Watercolor · 80 px · 61.6 s

![Brush Artist · Refs · #33 Red wet-in-wet band](Brush-Artist-Refs-33-Red-wet-in-wet-band.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 19 % → 30 % | 55.6 px | 0.59 | 1.58 | 180 |
| heavy line | 29 % → 38 % | 83.7 px | 0.59 | 1.33 | 253 |
| pressure swell | 19 % → 27 % | 71.5 px | 0.61 | 1.40 | 152 |
| fast wave | 58 % → 73 % | 67.4 px | 0.61 | 1.26 | 482 |
| slow wave | 57 % → 71 % | 65.7 px | 0.63 | 1.25 | 862 |
| spiral | 75 % → 84 % | 49.5 px | 0.64 | 1.12 | 1377 |
| loop | 51 % → 62 % | 66.4 px | 0.63 | 1.21 | 408 |
| tilted | 24 % → 25 % | 66.3 px | 0.60 | 1.03 | 444 |
| over the wet one | 48 % → 66 % | 66.6 px | 0.60 | 1.38 | 203 |
| long, no reload | 95 % → 99 % | 42.4 px | 0.66 | 1.05 | 1161 | quarters: 0.68 → 0.68 → 0.68 → 0.63

Numbers say: light vs heavy: width 55.6 → 83.7 px, dark 0.59 → 0.59; the long stroke does not run out of paint; wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #34 Magenta oil patches
Oil · 60 px · 28.4 s

![Brush Artist · Refs · #34 Magenta oil patches](Brush-Artist-Refs-34-Magenta-oil-patches.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 19 % → 19 % | 55.8 px | 0.61 | 1.00 | 239 |
| heavy line | 21 % → 21 % | 59.9 px | 0.61 | 1.00 | 263 |
| pressure swell | 16 % → 16 % | 58.9 px | 0.62 | 1.01 | 242 |
| fast wave | 48 % → 49 % | 55.4 px | 0.62 | 1.02 | 755 |
| slow wave | 48 % → 48 % | 55.8 px | 0.62 | 1.00 | 1280 |
| spiral | 70 % → 70 % | 46.3 px | 0.62 | 1.00 | 1162 |
| loop | 42 % → 42 % | 54.3 px | 0.62 | 1.00 | 593 |
| tilted | 17 % → 17 % | 46.8 px | 0.61 | 1.00 | 467 |
| over the wet one | 35 % → 35 % | 50.1 px | 0.61 | 1.00 | 418 |
| long, no reload | 86 % → 86 % | 38.7 px | 0.62 | 1.00 | 1858 | quarters: 0.59 → 0.58 → 0.57 → 0.52

Numbers say: light vs heavy: width 55.8 → 59.9 px, dark 0.61 → 0.61; pressure barely changes the width; the long stroke does not run out of paint.

## Brush Artist · Refs · #35 Red band with runs
Watercolor · 70 px · 64.0 s

![Brush Artist · Refs · #35 Red band with runs](Brush-Artist-Refs-35-Red-band-with-runs.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 17 % → 32 % | 48.3 px | 0.49 | 1.91 | 179 |
| heavy line | 25 % → 39 % | 73.9 px | 0.51 | 1.55 | 309 |
| pressure swell | 17 % → 25 % | 63.0 px | 0.55 | 1.47 | 144 |
| fast wave | 54 % → 72 % | 61.8 px | 0.52 | 1.34 | 461 |
| slow wave | 52 % → 70 % | 59.8 px | 0.55 | 1.35 | 810 |
| spiral | 72 % → 88 % | 47.3 px | 0.56 | 1.22 | 819 |
| loop | 47 % → 68 % | 61.0 px | 0.53 | 1.44 | 433 |
| tilted | 21 % → 22 % | 57.7 px | 0.51 | 1.06 | 243 |
| over the wet one | 43 % → 67 % | 62.0 px | 0.51 | 1.57 | 393 |
| long, no reload | 92 % → 98 % | 41.3 px | 0.59 | 1.07 | 1170 | quarters: 0.60 → 0.60 → 0.59 → 0.56

Numbers say: light vs heavy: width 48.3 → 73.9 px, dark 0.49 → 0.51; the long stroke does not run out of paint; wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #36 Magenta letters flat brush
Gouache · 36 px · 46.6 s

![Brush Artist · Refs · #36 Magenta letters flat brush](Brush-Artist-Refs-36-Magenta-letters-flat-brush.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 10 % → 10 % | 29.0 px | 0.45 | 0.98 | 102 |
| heavy line | 17 % → 14 % | 49.1 px | 0.45 | 0.85 | 120 |
| pressure swell | 13 % → 12 % | 49.4 px | 0.45 | 0.89 | 96 |
| fast wave | 35 % → 19 % | 40.3 px | 0.45 | 0.54 | 264 |
| slow wave | 35 % → 19 % | 39.9 px | 0.45 | 0.54 | 837 |
| spiral | 46 % → 19 % | 30.4 px | 0.45 | 0.42 | 505 |
| loop | 27 % → 20 % | 35.3 px | 0.45 | 0.72 | 245 |
| tilted | 11 % → 11 % | 29.8 px | 0.45 | 1.00 | 132 |
| over the wet one | 24 % → 22 % | 38.1 px | 0.45 | 0.92 | 125 |
| long, no reload | 46 % → 19 % | 20.8 px | 0.45 | 0.40 | 656 | quarters: 0.29 → 0.25 → 0.22 → 0.18

Numbers say: light vs heavy: width 29.0 → 49.1 px, dark 0.45 → 0.45.

## Brush Artist · Refs · #37 Oil still life dabs
Oil · 40 px · 23.9 s

![Brush Artist · Refs · #37 Oil still life dabs](Brush-Artist-Refs-37-Oil-still-life-dabs.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 13 % → 13 % | 38.0 px | 0.38 | 1.00 | 205 |
| heavy line | 14 % → 14 % | 41.1 px | 0.38 | 1.00 | 257 |
| pressure swell | 11 % → 11 % | 40.2 px | 0.40 | 1.00 | 188 |
| fast wave | 34 % → 34 % | 39.8 px | 0.39 | 1.00 | 778 |
| slow wave | 35 % → 35 % | 40.2 px | 0.39 | 1.00 | 935 |
| spiral | 59 % → 59 % | 38.7 px | 0.38 | 1.00 | 831 |
| loop | 29 % → 29 % | 37.8 px | 0.39 | 1.00 | 498 |
| tilted | 13 % → 13 % | 36.3 px | 0.39 | 1.00 | 260 |
| over the wet one | 26 % → 26 % | 35.8 px | 0.39 | 1.00 | 196 |
| long, no reload | 69 % → 69 % | 30.9 px | 0.37 | 1.00 | 1277 | quarters: 0.31 → 0.30 → 0.28 → 0.24

Numbers say: light vs heavy: width 38.0 → 41.1 px, dark 0.38 → 0.38; pressure barely changes the width.

## Brush Artist · Refs · #38 Sanguine drawing
Pastel · 6 px · 12.9 s

![Brush Artist · Refs · #38 Sanguine drawing](Brush-Artist-Refs-38-Sanguine-drawing.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 1 % → 1 % | 2.0 px | 0.61 | 1.00 | 29 |
| heavy line | 1 % → 1 % | 3.5 px | 0.62 | 1.00 | 30 |
| pressure swell | 1 % → 1 % | 3.3 px | 0.62 | 1.00 | 37 |
| fast wave | 3 % → 3 % | 3.2 px | 0.61 | 1.00 | 54 |
| slow wave | 3 % → 3 % | 3.0 px | 0.61 | 1.00 | 56 |
| spiral | 4 % → 4 % | 2.9 px | 0.61 | 1.00 | 127 |
| loop | 2 % → 2 % | 3.0 px | 0.61 | 1.00 | 74 |
| tilted | 1 % → 1 % | 3.4 px | 0.62 | 1.00 | 31 |
| over the wet one | 2 % → 2 % | 2.9 px | 0.62 | 1.00 | 28 |
| long, no reload | 7 % → 7 % | 3.0 px | 0.61 | 1.00 | 212 | quarters: 0.04 → 0.05 → 0.05 → 0.05

Numbers say: light vs heavy: width 2.0 → 3.5 px, dark 0.61 → 0.62; the long stroke does not run out of paint.

## Brush Artist · Refs · #39 Very thick impasto
Heavy acrylic · 60 px · 28.7 s

![Brush Artist · Refs · #39 Very thick impasto](Brush-Artist-Refs-39-Very-thick-impasto.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 20 % → 19 % | 56.9 px | 0.60 | 0.97 | 212 |
| heavy line | 21 % → 20 % | 59.6 px | 0.60 | 0.97 | 221 |
| pressure swell | 16 % → 15 % | 59.7 px | 0.62 | 0.97 | 172 |
| fast wave | 48 % → 47 % | 55.2 px | 0.62 | 0.98 | 574 |
| slow wave | 49 % → 47 % | 56.0 px | 0.62 | 0.98 | 1115 |
| spiral | 69 % → 65 % | 45.6 px | 0.62 | 0.93 | 1056 |
| loop | 42 % → 41 % | 54.0 px | 0.62 | 0.97 | 536 |
| tilted | 16 % → 16 % | 44.0 px | 0.61 | 1.00 | 298 |
| over the wet one | 34 % → 33 % | 51.0 px | 0.61 | 0.97 | 233 |
| long, no reload | 85 % → 79 % | 38.3 px | 0.62 | 0.92 | 2140 | quarters: 0.58 → 0.57 → 0.55 → 0.52

Numbers say: light vs heavy: width 56.9 → 59.6 px, dark 0.60 → 0.60; pressure barely changes the width; the long stroke does not run out of paint.

## Brush Artist · Refs · #40 Watercolour blooms
Watercolor · 90 px · 63.0 s

![Brush Artist · Refs · #40 Watercolour blooms](Brush-Artist-Refs-40-Watercolour-blooms.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 22 % → 33 % | 63.3 px | 0.10 | 1.51 | 189 |
| heavy line | 33 % → 41 % | 94.9 px | 0.11 | 1.26 | 294 |
| pressure swell | 22 % → 30 % | 84.1 px | 0.12 | 1.33 | 287 |
| fast wave | 64 % → 78 % | 73.9 px | 0.11 | 1.22 | 872 |
| slow wave | 63 % → 75 % | 72.3 px | 0.16 | 1.20 | 1003 |
| spiral | 79 % → 86 % | 52.0 px | 0.15 | 1.09 | 1007 |
| loop | 56 % → 65 % | 72.5 px | 0.13 | 1.17 | 518 |
| tilted | 26 % → 27 % | 73.1 px | 0.13 | 1.03 | 371 |
| over the wet one | 53 % → 71 % | 73.8 px | 0.13 | 1.35 | 234 |
| long, no reload | 97 % → 100 % | 43.4 px | 0.16 | 1.03 | 2045 | quarters: 0.21 → 0.19 → 0.16 → 0.12

Numbers say: light vs heavy: width 63.3 → 94.9 px, dark 0.10 → 0.11; wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #41 Coloured pencil hatching
Pastel · 4 px · 11.9 s

![Brush Artist · Refs · #41 Coloured pencil hatching](Brush-Artist-Refs-41-Coloured-pencil-hatching.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 1 % → 1 % | 1.6 px | 0.42 | 1.00 | 30 |
| heavy line | 1 % → 1 % | 2.6 px | 0.43 | 1.00 | 22 |
| pressure swell | 1 % → 1 % | 2.1 px | 0.43 | 1.00 | 17 |
| fast wave | 2 % → 2 % | 2.2 px | 0.42 | 1.00 | 56 |
| slow wave | 2 % → 2 % | 2.1 px | 0.43 | 1.00 | 62 |
| spiral | 3 % → 3 % | 2.1 px | 0.43 | 1.00 | 64 |
| loop | 2 % → 2 % | 2.2 px | 0.43 | 1.00 | 37 |
| tilted | 1 % → 1 % | 3.0 px | 0.42 | 1.00 | 20 |
| over the wet one | 2 % → 2 % | 2.2 px | 0.42 | 1.00 | 12 |
| long, no reload | 5 % → 5 % | 2.3 px | 0.43 | 1.00 | 95 | quarters: 0.02 → 0.02 → 0.02 → 0.03

Numbers say: light vs heavy: width 1.6 → 2.6 px, dark 0.42 → 0.43; the long stroke does not run out of paint.

## Brush Artist · Refs · #42 Oil pastel shaggy
Pastel · 18 px · 12.3 s

![Brush Artist · Refs · #42 Oil pastel shaggy](Brush-Artist-Refs-42-Oil-pastel-shaggy.png)

A light paint: laid on a grey sheet (on white it cannot be seen); **dark** = how far it is from the grey either way.

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 2 % → 2 % | 5.1 px | 0.35 | 1.00 | 28 |
| heavy line | 4 % → 4 % | 10.7 px | 0.36 | 1.00 | 38 |
| pressure swell | 3 % → 3 % | 9.5 px | 0.36 | 1.00 | 29 |
| fast wave | 8 % → 8 % | 9.0 px | 0.36 | 1.00 | 108 |
| slow wave | 7 % → 7 % | 8.2 px | 0.36 | 1.00 | 147 |
| spiral | 12 % → 12 % | 7.7 px | 0.36 | 1.00 | 203 |
| loop | 6 % → 6 % | 7.9 px | 0.36 | 1.00 | 79 |
| tilted | 2 % → 2 % | 6.9 px | 0.36 | 1.00 | 43 |
| over the wet one | 6 % → 6 % | 8.5 px | 0.36 | 1.00 | 34 |
| long, no reload | 15 % → 15 % | 6.9 px | 0.36 | 1.00 | 227 | quarters: 0.00 → 0.00 → 0.00 → 0.00

Numbers say: light vs heavy: width 5.1 → 10.7 px, dark 0.35 → 0.36; the long stroke does not run out of paint.

## Brush Artist · Refs · #43 Dragged black ink blocks
Gouache · 70 px · 40.6 s

![Brush Artist · Refs · #43 Dragged black ink blocks](Brush-Artist-Refs-43-Dragged-black-ink-blocks.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 19 % → 5 % | 54.9 px | 0.57 | 0.28 | 188 |
| heavy line | 24 % → 9 % | 69.0 px | 0.57 | 0.38 | 403 |
| pressure swell | 17 % → 9 % | 63.4 px | 0.57 | 0.53 | 213 |
| fast wave | 51 % → 11 % | 58.7 px | 0.57 | 0.21 | 750 |
| slow wave | 50 % → 10 % | 58.1 px | 0.57 | 0.20 | 1420 |
| spiral | 65 % → 14 % | 42.6 px | 0.57 | 0.22 | 1265 |
| loop | 45 % → 12 % | 58.1 px | 0.57 | 0.27 | 610 |
| tilted | 17 % → 16 % | 46.4 px | 0.57 | 0.98 | 324 |
| over the wet one | 37 % → 20 % | 55.6 px | 0.57 | 0.56 | 284 |
| long, no reload | 82 % → 17 % | 36.6 px | 0.57 | 0.21 | 1691 | quarters: 0.54 → 0.52 → 0.47 → 0.40

Numbers say: light vs heavy: width 54.9 → 69.0 px, dark 0.57 → 0.57.

## Brush Artist · Refs · #44 Blue looping ribbon
Oil · 80 px · 35.1 s

![Brush Artist · Refs · #44 Blue looping ribbon](Brush-Artist-Refs-44-Blue-looping-ribbon.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 26 % → 27 % | 74.9 px | 0.72 | 1.04 | 352 |
| heavy line | 27 % → 27 % | 79.6 px | 0.72 | 1.00 | 402 |
| pressure swell | 21 % → 21 % | 78.1 px | 0.72 | 1.03 | 357 |
| fast wave | 61 % → 64 % | 70.3 px | 0.73 | 1.05 | 1281 |
| slow wave | 61 % → 61 % | 70.0 px | 0.73 | 1.00 | 1683 |
| spiral | 78 % → 78 % | 51.3 px | 0.73 | 1.00 | 1657 |
| loop | 54 % → 54 % | 69.7 px | 0.73 | 1.00 | 852 |
| tilted | 21 % → 21 % | 57.3 px | 0.72 | 1.00 | 452 |
| over the wet one | 44 % → 44 % | 64.9 px | 0.72 | 1.00 | 377 |
| long, no reload | 96 % → 96 % | 42.8 px | 0.73 | 1.00 | 2741 | quarters: 0.72 → 0.73 → 0.73 → 0.69

Numbers say: light vs heavy: width 74.9 → 79.6 px, dark 0.72 → 0.72; pressure barely changes the width; the long stroke does not run out of paint.

## Brush Artist · Refs · #45 Soft pastel pepper
Pastel · 40 px · 13.7 s

![Brush Artist · Refs · #45 Soft pastel pepper](Brush-Artist-Refs-45-Soft-pastel-pepper.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 4 % → 4 % | 11.3 px | 0.53 | 1.00 | 71 |
| heavy line | 8 % → 8 % | 23.0 px | 0.53 | 1.00 | 65 |
| pressure swell | 5 % → 5 % | 19.5 px | 0.53 | 1.00 | 63 |
| fast wave | 17 % → 17 % | 19.4 px | 0.53 | 1.00 | 155 |
| slow wave | 15 % → 15 % | 17.1 px | 0.53 | 1.00 | 292 |
| spiral | 25 % → 25 % | 16.3 px | 0.53 | 1.00 | 286 |
| loop | 12 % → 12 % | 16.1 px | 0.53 | 1.00 | 144 |
| tilted | 5 % → 5 % | 12.8 px | 0.53 | 1.00 | 77 |
| over the wet one | 11 % → 11 % | 17.7 px | 0.53 | 1.00 | 71 |
| long, no reload | 30 % → 30 % | 13.6 px | 0.53 | 1.00 | 591 | quarters: 0.18 → 0.18 → 0.18 → 0.18

Numbers say: light vs heavy: width 11.3 → 23.0 px, dark 0.53 → 0.53; the long stroke does not run out of paint.

## Brush Artist · Refs · #46 Red-brown ink lips
Watercolor · 50 px · 47.3 s

![Brush Artist · Refs · #46 Red-brown ink lips](Brush-Artist-Refs-46-Red-brown-ink-lips.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 12 % → 23 % | 33.6 px | 0.67 | 2.00 | 73 |
| heavy line | 19 % → 30 % | 54.1 px | 0.65 | 1.59 | 147 |
| pressure swell | 12 % → 20 % | 43.7 px | 0.67 | 1.73 | 80 |
| fast wave | 40 % → 60 % | 46.7 px | 0.66 | 1.48 | 292 |
| slow wave | 39 % → 58 % | 44.6 px | 0.69 | 1.52 | 606 |
| spiral | 63 % → 75 % | 41.6 px | 0.70 | 1.19 | 460 |
| loop | 35 % → 51 % | 44.9 px | 0.68 | 1.48 | 248 |
| tilted | 16 % → 17 % | 43.6 px | 0.67 | 1.07 | 163 |
| over the wet one | 33 % → 51 % | 47.6 px | 0.67 | 1.55 | 118 |
| long, no reload | 78 % → 95 % | 35.2 px | 0.70 | 1.21 | 666 | quarters: 0.71 → 0.71 → 0.70 → 0.64

Numbers say: light vs heavy: width 33.6 → 54.1 px, dark 0.67 → 0.65; the long stroke does not run out of paint; wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #47 Pink knife slabs
Heavy acrylic · 90 px · 32.2 s

![Brush Artist · Refs · #47 Pink knife slabs](Brush-Artist-Refs-47-Pink-knife-slabs.png)

A light paint: laid on a grey sheet (on white it cannot be seen); **dark** = how far it is from the grey either way.

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 32 % → 31 % | 91.8 px | 0.29 | 0.99 | 92 |
| heavy line | 32 % → 31 % | 91.8 px | 0.29 | 0.99 | 90 |
| pressure swell | 24 % → 25 % | 90.4 px | 0.28 | 1.04 | 28 |
| fast wave | 66 % → 57 % | 76.4 px | 0.26 | 0.86 | 186 |
| slow wave | 67 % → 59 % | 77.6 px | 0.26 | 0.87 | 301 |
| spiral | 67 % → 41 % | 44.4 px | 0.26 | 0.61 | 431 |
| loop | 60 % → 54 % | 77.8 px | 0.27 | 0.89 | 243 |
| tilted | 20 % → 20 % | 56.2 px | 0.28 | 1.00 | 57 |
| over the wet one | 48 % → 47 % | 77.0 px | 0.28 | 0.99 | 85 |
| long, no reload | 94 % → 61 % | 42.0 px | 0.25 | 0.65 | 388 | quarters: 0.00 → 0.00 → 0.00 → 0.00

Numbers say: light vs heavy: width 91.8 → 91.8 px, dark 0.29 → 0.29; pressure barely changes the width; the long stroke does not run out of paint.

## Brush Artist · Refs · #48 Black bands with drips
Gouache · 70 px · 51.0 s

![Brush Artist · Refs · #48 Black bands with drips](Brush-Artist-Refs-48-Black-bands-with-drips.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 19 % → 18 % | 54.6 px | 0.69 | 0.93 | 236 |
| heavy line | 29 % → 24 % | 83.0 px | 0.69 | 0.84 | 318 |
| pressure swell | 23 % → 21 % | 86.1 px | 0.69 | 0.92 | 200 |
| fast wave | 53 % → 36 % | 61.8 px | 0.69 | 0.68 | 999 |
| slow wave | 53 % → 36 % | 61.7 px | 0.69 | 0.67 | 1076 |
| spiral | 64 % → 35 % | 41.9 px | 0.69 | 0.55 | 1077 |
| loop | 45 % → 36 % | 57.8 px | 0.69 | 0.81 | 604 |
| tilted | 19 % → 19 % | 52.3 px | 0.69 | 1.00 | 325 |
| over the wet one | 41 % → 38 % | 62.4 px | 0.69 | 0.92 | 255 |
| long, no reload | 74 % → 37 % | 33.3 px | 0.69 | 0.50 | 2173 | quarters: 0.64 → 0.61 → 0.54 → 0.45

Numbers say: light vs heavy: width 54.6 → 83.0 px, dark 0.69 → 0.69.

## Brush Artist · Refs · #49 Magenta letters round brush
Ink · 30 px · 37.2 s

![Brush Artist · Refs · #49 Magenta letters round brush](Brush-Artist-Refs-49-Magenta-letters-round-brush.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 6 % → 8 % | 17.5 px | 0.50 | 1.28 | 43 |
| heavy line | 21 % → 21 % | 62.0 px | 0.51 | 0.99 | 107 |
| pressure swell | 12 % → 13 % | 46.3 px | 0.52 | 1.01 | 79 |
| fast wave | 38 % → 38 % | 44.3 px | 0.51 | 0.99 | 196 |
| slow wave | 32 % → 31 % | 36.4 px | 0.51 | 0.99 | 306 |
| spiral | 50 % → 48 % | 32.8 px | 0.51 | 0.97 | 398 |
| loop | 29 % → 29 % | 37.6 px | 0.51 | 1.00 | 176 |
| tilted | 11 % → 11 % | 30.7 px | 0.52 | 1.01 | 84 |
| over the wet one | 26 % → 26 % | 42.1 px | 0.52 | 1.01 | 80 |
| long, no reload | 61 % → 56 % | 27.5 px | 0.51 | 0.92 | 502 | quarters: 0.41 → 0.36 → 0.30 → 0.25

Numbers say: light vs heavy: width 17.5 → 62.0 px, dark 0.50 → 0.51.

## Brush Artist · Refs · #50 Thick swipes on photo
Heavy acrylic · 40 px · 25.1 s

![Brush Artist · Refs · #50 Thick swipes on photo](Brush-Artist-Refs-50-Thick-swipes-on-photo.png)

A light paint: laid on a grey sheet (on white it cannot be seen); **dark** = how far it is from the grey either way.

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 13 % → 13 % | 38.1 px | 0.26 | 0.96 | 123 |
| heavy line | 14 % → 13 % | 40.2 px | 0.27 | 0.96 | 116 |
| pressure swell | 11 % → 10 % | 40.1 px | 0.25 | 0.95 | 105 |
| fast wave | 33 % → 31 % | 38.3 px | 0.25 | 0.93 | 323 |
| slow wave | 34 % → 32 % | 39.1 px | 0.26 | 0.95 | 689 |
| spiral | 58 % → 47 % | 38.5 px | 0.24 | 0.80 | 667 |
| loop | 28 % → 27 % | 36.9 px | 0.26 | 0.95 | 352 |
| tilted | 12 % → 12 % | 34.0 px | 0.26 | 1.00 | 171 |
| over the wet one | 25 % → 24 % | 35.3 px | 0.26 | 0.95 | 170 |
| long, no reload | 66 % → 46 % | 29.6 px | 0.24 | 0.69 | 1321 | quarters: 0.00 → 0.00 → 0.00 → 0.00

Numbers say: light vs heavy: width 38.1 → 40.2 px, dark 0.26 → 0.27; pressure barely changes the width; the long stroke does not run out of paint.

## Brush Artist · Refs · Finger
Pastel · 36 px · 25.8 s · over bands of wet oil paint and oil pastel in turn (it works on paint already there: look at what it does to the bands; covered counts the bands too)

![Brush Artist · Refs · Finger](Brush-Artist-Refs-Finger.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 27 % → 27 % | 79.5 px | 0.78 | 1.00 | 78 |
| heavy line | 30 % → 30 % | 87.1 px | 0.76 | 1.00 | 98 |
| pressure swell | 28 % → 28 % | 103.6 px | 0.78 | 1.00 | 55 |
| fast wave | 36 % → 36 % | 41.8 px | 0.72 | 1.00 | 150 |
| slow wave | 35 % → 35 % | 40.3 px | 0.72 | 1.00 | 270 |
| spiral | 43 % → 43 % | 28.7 px | 0.68 | 1.00 | 247 |
| loop | 33 % → 33 % | 42.9 px | 0.73 | 1.00 | 127 |
| tilted | 28 % → 28 % | 77.0 px | 0.74 | 1.00 | 69 |
| over the wet one | 32 % → 32 % | 13.1 px | 0.74 | 1.00 | 61 |
| long, no reload | 48 % → 48 % | 21.5 px | 0.66 | 1.00 | 343 | quarters: 0.33 → 0.35 → 0.33 → 0.37

Numbers say: light vs heavy: width 79.5 → 87.1 px, dark 0.78 → 0.76; pressure barely changes the width; the long stroke does not run out of paint.

## Brush Artist · Ink — wash
Watercolor · 38 px · 41.4 s

![Brush Artist · Ink — wash](Brush-Artist-Ink-wash.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 11 % → 11 % | 31.6 px | 0.38 | 1.03 | 84 |
| heavy line | 19 % → 19 % | 54.3 px | 0.32 | 1.03 | 128 |
| pressure swell | 12 % → 12 % | 45.1 px | 0.36 | 1.04 | 89 |
| fast wave | 39 % → 41 % | 44.7 px | 0.30 | 1.05 | 247 |
| slow wave | 37 % → 38 % | 42.6 px | 0.37 | 1.04 | 405 |
| spiral | 57 % → 60 % | 37.9 px | 0.30 | 1.04 | 382 |
| loop | 32 % → 33 % | 41.8 px | 0.34 | 1.02 | 219 |
| tilted | 13 % → 14 % | 36.8 px | 0.38 | 1.04 | 137 |
| over the wet one | 29 % → 30 % | 42.8 px | 0.38 | 1.04 | 98 |
| long, no reload | 65 % → 70 % | 29.2 px | 0.29 | 1.08 | 769 | quarters: 0.33 → 0.26 → 0.18 → 0.11

Numbers say: light vs heavy: width 31.6 → 54.3 px, dark 0.38 → 0.32.

## Brush Artist · Ink — brush line
Ink · 16 px · 31.9 s

![Brush Artist · Ink — brush line](Brush-Artist-Ink-brush-line.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 3 % → 5 % | 7.7 px | 0.78 | 1.80 | 58 |
| heavy line | 13 % → 13 % | 39.0 px | 0.88 | 0.99 | 93 |
| pressure swell | 8 % → 8 % | 28.4 px | 0.87 | 1.05 | 60 |
| fast wave | 24 % → 23 % | 27.6 px | 0.87 | 0.96 | 178 |
| slow wave | 19 % → 19 % | 22.5 px | 0.87 | 0.97 | 248 |
| spiral | 30 % → 27 % | 19.9 px | 0.86 | 0.90 | 340 |
| loop | 18 % → 18 % | 23.4 px | 0.88 | 1.00 | 164 |
| tilted | 7 % → 7 % | 20.1 px | 0.88 | 1.01 | 69 |
| over the wet one | 17 % → 17 % | 26.8 px | 0.88 | 1.00 | 100 |
| long, no reload | 42 % → 31 % | 18.8 px | 0.85 | 0.73 | 634 | quarters: 0.49 → 0.40 → 0.30 → 0.21

Numbers say: light vs heavy: width 7.7 → 39.0 px, dark 0.78 → 0.88; wet paint spreads well beyond the stroke.

## Brush Artist · Ink — dry brush
Gouache · 30 px · 28.0 s

![Brush Artist · Ink — dry brush](Brush-Artist-Ink-dry-brush.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 7 % → 1 % | 21.8 px | 0.71 | 0.11 | 82 |
| heavy line | 10 % → 1 % | 27.7 px | 0.71 | 0.10 | 162 |
| pressure swell | 7 % → 2 % | 25.5 px | 0.71 | 0.23 | 80 |
| fast wave | 21 % → 2 % | 24.2 px | 0.71 | 0.09 | 408 |
| slow wave | 21 % → 2 % | 23.9 px | 0.71 | 0.08 | 697 |
| spiral | 31 % → 2 % | 20.6 px | 0.71 | 0.06 | 485 |
| loop | 18 % → 2 % | 23.9 px | 0.71 | 0.13 | 256 |
| tilted | 9 % → 8 % | 24.1 px | 0.71 | 0.96 | 147 |
| over the wet one | 17 % → 4 % | 22.8 px | 0.71 | 0.24 | 115 |
| long, no reload | 31 % → 3 % | 14.0 px | 0.71 | 0.09 | 701 | quarters: 0.38 → 0.32 → 0.22 → 0.09

Numbers say: light vs heavy: width 21.8 → 27.7 px, dark 0.71 → 0.71.

## Brush Artist · Watercolour — blue
Watercolor · 40 px · 37.2 s

![Brush Artist · Watercolour — blue](Brush-Artist-Watercolour-blue.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 6 % → 10 % | 16.7 px | 0.25 | 1.70 | 45 |
| heavy line | 11 % → 12 % | 31.5 px | 0.25 | 1.13 | 131 |
| pressure swell | 7 % → 9 % | 25.4 px | 0.26 | 1.32 | 70 |
| fast wave | 24 % → 25 % | 27.8 px | 0.24 | 1.05 | 195 |
| slow wave | 22 % → 27 % | 25.9 px | 0.26 | 1.22 | 287 |
| spiral | 38 % → 41 % | 25.1 px | 0.22 | 1.08 | 293 |
| loop | 20 % → 22 % | 25.3 px | 0.26 | 1.13 | 143 |
| tilted | 12 % → 12 % | 33.3 px | 0.26 | 1.00 | 125 |
| over the wet one | 21 % → 24 % | 24.7 px | 0.26 | 1.15 | 74 |
| long, no reload | 51 % → 54 % | 23.0 px | 0.22 | 1.04 | 553 | quarters: 0.18 → 0.14 → 0.11 → 0.08

Numbers say: light vs heavy: width 16.7 → 31.5 px, dark 0.25 → 0.25; wet paint spreads well beyond the stroke.

## Brush Artist · Watercolour — violet
Watercolor · 40 px · 36.2 s

![Brush Artist · Watercolour — violet](Brush-Artist-Watercolour-violet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 6 % → 10 % | 16.7 px | 0.40 | 1.70 | 33 |
| heavy line | 11 % → 12 % | 31.5 px | 0.40 | 1.13 | 72 |
| pressure swell | 7 % → 9 % | 25.4 px | 0.41 | 1.32 | 43 |
| fast wave | 24 % → 25 % | 27.8 px | 0.38 | 1.05 | 167 |
| slow wave | 22 % → 27 % | 25.9 px | 0.40 | 1.22 | 260 |
| spiral | 38 % → 41 % | 25.1 px | 0.36 | 1.08 | 288 |
| loop | 20 % → 22 % | 25.3 px | 0.40 | 1.13 | 197 |
| tilted | 12 % → 12 % | 33.3 px | 0.40 | 1.00 | 155 |
| over the wet one | 21 % → 24 % | 24.7 px | 0.40 | 1.15 | 95 |
| long, no reload | 51 % → 54 % | 23.0 px | 0.34 | 1.04 | 442 | quarters: 0.28 → 0.22 → 0.17 → 0.14

Numbers say: light vs heavy: width 16.7 → 31.5 px, dark 0.40 → 0.40; wet paint spreads well beyond the stroke.

## Brush Artist · Watercolour — teal
Watercolor · 40 px · 34.7 s

![Brush Artist · Watercolour — teal](Brush-Artist-Watercolour-teal.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 6 % → 10 % | 16.7 px | 0.16 | 1.70 | 48 |
| heavy line | 11 % → 12 % | 31.5 px | 0.16 | 1.13 | 123 |
| pressure swell | 7 % → 9 % | 25.4 px | 0.17 | 1.32 | 61 |
| fast wave | 24 % → 25 % | 27.8 px | 0.15 | 1.05 | 198 |
| slow wave | 22 % → 27 % | 25.9 px | 0.17 | 1.22 | 282 |
| spiral | 38 % → 41 % | 25.1 px | 0.15 | 1.08 | 279 |
| loop | 20 % → 22 % | 25.3 px | 0.16 | 1.13 | 150 |
| tilted | 12 % → 12 % | 33.3 px | 0.16 | 1.00 | 115 |
| over the wet one | 21 % → 24 % | 24.7 px | 0.16 | 1.15 | 70 |
| long, no reload | 51 % → 54 % | 23.0 px | 0.14 | 1.04 | 449 | quarters: 0.11 → 0.09 → 0.07 → 0.06

Numbers say: light vs heavy: width 16.7 → 31.5 px, dark 0.16 → 0.16; wet paint spreads well beyond the stroke.

## Brush Artist · Gouache
Gouache · 30 px · 37.4 s

![Brush Artist · Gouache](Brush-Artist-Gouache.png)

A light paint: laid on a grey sheet (on white it cannot be seen); **dark** = how far it is from the grey either way.

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 8 % → 8 % | 24.4 px | 0.27 | 0.97 | 68 |
| heavy line | 15 % → 11 % | 42.8 px | 0.27 | 0.78 | 87 |
| pressure swell | 11 % → 9 % | 41.0 px | 0.27 | 0.84 | 86 |
| fast wave | 30 % → 13 % | 34.4 px | 0.26 | 0.45 | 337 |
| slow wave | 29 % → 14 % | 33.9 px | 0.26 | 0.46 | 364 |
| spiral | 40 % → 14 % | 26.6 px | 0.26 | 0.35 | 352 |
| loop | 23 % → 15 % | 30.4 px | 0.26 | 0.62 | 178 |
| tilted | 10 % → 10 % | 27.1 px | 0.26 | 1.01 | 88 |
| over the wet one | 21 % → 19 % | 32.8 px | 0.26 | 0.89 | 80 |
| long, no reload | 43 % → 15 % | 19.1 px | 0.26 | 0.35 | 485 | quarters: 0.01 → 0.01 → 0.01 → 0.01

Numbers say: light vs heavy: width 24.4 → 42.8 px, dark 0.27 → 0.27; the long stroke does not run out of paint.

## Brush Artist · Oil — bristle
Oil · 30 px · 19.6 s

![Brush Artist · Oil — bristle](Brush-Artist-Oil-bristle.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 9 % → 9 % | 26.3 px | 0.54 | 1.00 | 113 |
| heavy line | 10 % → 10 % | 28.6 px | 0.54 | 1.00 | 131 |
| pressure swell | 8 % → 8 % | 28.2 px | 0.55 | 1.00 | 85 |
| fast wave | 24 % → 24 % | 27.3 px | 0.55 | 1.00 | 339 |
| slow wave | 25 % → 25 % | 28.3 px | 0.55 | 1.00 | 517 |
| spiral | 39 % → 39 % | 25.6 px | 0.54 | 1.00 | 663 |
| loop | 20 % → 20 % | 26.3 px | 0.54 | 1.00 | 288 |
| tilted | 11 % → 11 % | 29.9 px | 0.53 | 1.00 | 183 |
| over the wet one | 20 % → 20 % | 25.5 px | 0.53 | 1.00 | 133 |
| long, no reload | 50 % → 50 % | 22.4 px | 0.54 | 1.00 | 988 | quarters: 0.32 → 0.30 → 0.29 → 0.28

Numbers say: light vs heavy: width 26.3 → 28.6 px, dark 0.54 → 0.54; pressure barely changes the width; the long stroke does not run out of paint.

## Brush Artist · Charcoal — stick
Charcoal · 28 px · 12.5 s

![Brush Artist · Charcoal — stick](Brush-Artist-Charcoal-stick.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 3 % → 3 % | 8.4 px | 0.85 | 1.00 | 37 |
| heavy line | 6 % → 6 % | 17.8 px | 0.85 | 1.00 | 24 |
| pressure swell | 4 % → 4 % | 13.9 px | 0.85 | 1.00 | 23 |
| fast wave | 12 % → 12 % | 14.0 px | 0.85 | 1.00 | 68 |
| slow wave | 11 % → 11 % | 12.5 px | 0.85 | 1.00 | 107 |
| spiral | 19 % → 19 % | 12.7 px | 0.85 | 1.00 | 103 |
| loop | 10 % → 10 % | 12.8 px | 0.85 | 1.00 | 67 |
| tilted | 4 % → 4 % | 10.9 px | 0.85 | 1.00 | 41 |
| over the wet one | 9 % → 9 % | 13.5 px | 0.85 | 1.00 | 26 |
| long, no reload | 27 % → 27 % | 12.2 px | 0.85 | 1.00 | 213 | quarters: 0.26 → 0.25 → 0.26 → 0.27

Numbers say: light vs heavy: width 8.4 → 17.8 px, dark 0.85 → 0.85; the long stroke does not run out of paint.

## Brush Artist · Charcoal — stick B
Charcoal · 36 px · 13.0 s

![Brush Artist · Charcoal — stick B](Brush-Artist-Charcoal-stick-B.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 4 % → 4 % | 10.5 px | 0.85 | 1.00 | 48 |
| heavy line | 7 % → 7 % | 21.1 px | 0.85 | 1.00 | 40 |
| pressure swell | 4 % → 4 % | 16.5 px | 0.85 | 1.00 | 22 |
| fast wave | 15 % → 15 % | 16.8 px | 0.85 | 1.00 | 77 |
| slow wave | 13 % → 13 % | 14.7 px | 0.85 | 1.00 | 119 |
| spiral | 23 % → 23 % | 15.0 px | 0.85 | 1.00 | 140 |
| loop | 11 % → 11 % | 14.8 px | 0.85 | 1.00 | 69 |
| tilted | 4 % → 4 % | 12.3 px | 0.85 | 1.00 | 65 |
| over the wet one | 10 % → 10 % | 15.9 px | 0.85 | 1.00 | 29 |
| long, no reload | 31 % → 31 % | 13.9 px | 0.85 | 1.00 | 298 | quarters: 0.30 → 0.28 → 0.29 → 0.30

Numbers say: light vs heavy: width 10.5 → 21.1 px, dark 0.85 → 0.85; the long stroke does not run out of paint.

## Brush Artist · Charcoal — stick C
Charcoal · 22 px · 12.6 s

![Brush Artist · Charcoal — stick C](Brush-Artist-Charcoal-stick-C.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 2 % → 2 % | 6.9 px | 0.85 | 1.00 | 42 |
| heavy line | 5 % → 5 % | 15.3 px | 0.85 | 1.00 | 17 |
| pressure swell | 3 % → 3 % | 12.2 px | 0.85 | 1.00 | 13 |
| fast wave | 10 % → 10 % | 12.1 px | 0.85 | 1.00 | 45 |
| slow wave | 9 % → 9 % | 10.8 px | 0.85 | 1.00 | 121 |
| spiral | 17 % → 17 % | 11.0 px | 0.85 | 1.00 | 100 |
| loop | 9 % → 9 % | 11.4 px | 0.85 | 1.00 | 59 |
| tilted | 4 % → 4 % | 9.9 px | 0.85 | 1.00 | 49 |
| over the wet one | 8 % → 8 % | 11.7 px | 0.85 | 1.00 | 27 |
| long, no reload | 24 % → 24 % | 11.0 px | 0.85 | 1.00 | 137 | quarters: 0.24 → 0.22 → 0.23 → 0.24

Numbers say: light vs heavy: width 6.9 → 15.3 px, dark 0.85 → 0.85; the long stroke does not run out of paint.

## Brush Artist · Refs · #01 Henry Ward peach cloud — own sheet
own sheet 600 × 600 · Gouache · 44 px · 20.3 s

![Brush Artist · Refs · #01 Henry Ward peach cloud — own sheet](Brush-Artist-Refs-01-Henry-Ward-peach-cloud-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 16 % → 43 % | 45.1 px | 0.59 | 2.70 | 232 |
| stroke 2 | 27 % → 63 % | 88.6 px | 0.59 | 2.33 | 152 |
| stroke 3 | 31 % → 62 % | 90.6 px | 0.59 | 1.99 | 198 |
| stroke 4 | 34 % → 68 % | 109.8 px | 0.59 | 2.03 | 169 |
| stroke 5 | 33 % → 59 % | 95.9 px | 0.59 | 1.80 | 169 |
| stroke 6 | 33 % → 46 % | 100.5 px | 0.59 | 1.40 | 175 |
| stroke 7 | 18 % → 54 % | 44.9 px | 0.60 | 2.99 | 161 |
| stroke 8 | 19 % → 50 % | 48.5 px | 0.60 | 2.61 | 184 |
| stroke 9 | 23 % → 51 % | 58.2 px | 0.60 | 2.27 | 261 |
| stroke 10 | 25 % → 52 % | 67.0 px | 0.60 | 2.08 | 250 |
| stroke 11 | 27 % → 55 % | 77.1 px | 0.60 | 2.00 | 286 |
| stroke 12 | 31 % → 57 % | 93.0 px | 0.60 | 1.85 | 266 |
| stroke 13 | 39 % → 60 % | 113.7 px | 0.60 | 1.53 | 301 |
| stroke 14 | 41 % → 62 % | 118.3 px | 0.60 | 1.50 | 197 |
| stroke 15 | 55 % → 68 % | 163.9 px | 0.59 | 1.23 | 227 |
| stroke 16 | 57 % → 69 % | 171.7 px | 0.59 | 1.22 | 218 |
| stroke 17 | 57 % → 70 % | 160.2 px | 0.60 | 1.22 | 219 |
| stroke 18 | 58 % → 68 % | 169.1 px | 0.60 | 1.17 | 198 |
| stroke 19 | 60 % → 67 % | 167.7 px | 0.59 | 1.12 | 252 |
| stroke 20 | 59 % → 64 % | 170.4 px | 0.59 | 1.08 | 246 |
| stroke 21 | 59 % → 61 % | 171.3 px | 0.59 | 1.03 | 258 |
| stroke 22 | 60 % → 62 % | 176.0 px | 0.59 | 1.03 | 251 |
| stroke 23 | 60 % → 60 % | 171.0 px | 0.59 | 1.00 | 248 |
| stroke 24 | 64 % → 63 % | 190.6 px | 0.59 | 1.00 | 220 |

Numbers say: wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #02 Henry Ward cream strokes — own sheet
own sheet 600 × 600 · Gouache · 46 px · 12.7 s

![Brush Artist · Refs · #02 Henry Ward cream strokes — own sheet](Brush-Artist-Refs-02-Henry-Ward-cream-strokes-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 21 % → 39 % | 42.9 px | 0.71 | 1.87 | 285 |
| stroke 2 | 32 % → 45 % | 84.2 px | 0.71 | 1.40 | 254 |
| stroke 3 | 31 % → 52 % | 79.7 px | 0.72 | 1.68 | 225 |
| stroke 4 | 34 % → 49 % | 83.3 px | 0.71 | 1.45 | 263 |
| stroke 5 | 39 % → 52 % | 96.5 px | 0.72 | 1.33 | 244 |
| stroke 6 | 32 % → 46 % | 76.7 px | 0.71 | 1.47 | 355 |
| stroke 7 | 34 % → 32 % | 86.2 px | 0.71 | 0.95 | 403 |

Numbers say: wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #03 Henry Ward navy contours — own sheet
own sheet 600 × 600 · Heavy acrylic · 22 px · 3.4 s

![Brush Artist · Refs · #03 Henry Ward navy contours — own sheet](Brush-Artist-Refs-03-Henry-Ward-navy-contours-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 11 % → 18 % | 23.1 px | 0.69 | 1.56 | 136 |
| stroke 2 | 20 % → 23 % | 28.3 px | 0.69 | 1.14 | 118 |
| stroke 3 | 23 % → 23 % | 33.4 px | 0.69 | 1.01 | 157 |
| stroke 4 | 23 % → 21 % | 50.8 px | 0.69 | 0.92 | 187 |

Numbers say: wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #04 Henry Ward grey cloud — own sheet
own sheet 600 × 600 · Gouache · 50 px · 20.1 s

![Brush Artist · Refs · #04 Henry Ward grey cloud — own sheet](Brush-Artist-Refs-04-Henry-Ward-grey-cloud-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 17 % → 49 % | 48.9 px | 0.40 | 2.96 | 371 |
| stroke 2 | 20 % → 51 % | 57.9 px | 0.40 | 2.54 | 296 |
| stroke 3 | 29 % → 58 % | 81.5 px | 0.40 | 2.00 | 304 |
| stroke 4 | 32 % → 62 % | 93.4 px | 0.40 | 1.92 | 356 |
| stroke 5 | 38 % → 68 % | 116.0 px | 0.40 | 1.78 | 367 |
| stroke 6 | 41 % → 72 % | 135.7 px | 0.40 | 1.74 | 259 |
| stroke 7 | 48 % → 78 % | 140.2 px | 0.40 | 1.63 | 305 |
| stroke 8 | 46 % → 78 % | 137.7 px | 0.40 | 1.68 | 286 |
| stroke 9 | 47 % → 78 % | 142.1 px | 0.40 | 1.65 | 271 |
| stroke 10 | 48 % → 78 % | 153.4 px | 0.40 | 1.64 | 286 |
| stroke 11 | 48 % → 78 % | 135.7 px | 0.40 | 1.63 | 303 |
| stroke 12 | 49 % → 78 % | 147.0 px | 0.40 | 1.60 | 344 |
| stroke 13 | 48 % → 78 % | 137.3 px | 0.40 | 1.63 | 273 |
| stroke 14 | 49 % → 78 % | 144.8 px | 0.40 | 1.61 | 242 |
| stroke 15 | 49 % → 74 % | 140.0 px | 0.40 | 1.52 | 275 |
| stroke 16 | 49 % → 71 % | 148.6 px | 0.40 | 1.46 | 250 |
| stroke 17 | 48 % → 62 % | 137.0 px | 0.40 | 1.31 | 278 |
| stroke 18 | 47 % → 58 % | 154.0 px | 0.40 | 1.24 | 259 |
| stroke 19 | 48 % → 48 % | 142.0 px | 0.40 | 1.02 | 306 |
| stroke 20 | 48 % → 48 % | 152.3 px | 0.40 | 0.99 | 299 |

Numbers say: wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #05 Henry Ward green in rust loops — own sheet
own sheet 600 × 600 · Heavy acrylic · 20 px · 3.5 s

![Brush Artist · Refs · #05 Henry Ward green in rust loops — own sheet](Brush-Artist-Refs-05-Henry-Ward-green-in-rust-loops-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 12 % → 19 % | 20.9 px | 0.02 | 1.60 | 151 |
| stroke 2 | 12 % → 11 % | 23.5 px | 0.02 | 0.93 | 194 |
| stroke 3 | 23 % → 21 % | 41.5 px | 0.02 | 0.93 | 159 |

Numbers say: wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #06 Henry Ward scrubbed grey — own sheet
own sheet 600 × 600 · Gouache · 50 px · 21.4 s

![Brush Artist · Refs · #06 Henry Ward scrubbed grey — own sheet](Brush-Artist-Refs-06-Henry-Ward-scrubbed-grey-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 20 % → 56 % | 48.6 px | 0.40 | 2.83 | 366 |
| stroke 2 | 24 % → 58 % | 64.3 px | 0.40 | 2.41 | 493 |
| stroke 3 | 31 % → 63 % | 93.7 px | 0.40 | 2.04 | 384 |
| stroke 4 | 31 % → 63 % | 98.4 px | 0.40 | 2.01 | 397 |
| stroke 5 | 45 % → 78 % | 136.2 px | 0.40 | 1.71 | 300 |
| stroke 6 | 48 % → 78 % | 145.5 px | 0.40 | 1.64 | 312 |
| stroke 7 | 49 % → 78 % | 139.4 px | 0.40 | 1.61 | 295 |
| stroke 8 | 48 % → 78 % | 152.1 px | 0.40 | 1.63 | 304 |
| stroke 9 | 47 % → 78 % | 144.8 px | 0.40 | 1.67 | 336 |
| stroke 10 | 47 % → 79 % | 152.5 px | 0.40 | 1.68 | 337 |
| stroke 11 | 48 % → 79 % | 141.3 px | 0.40 | 1.63 | 345 |
| stroke 12 | 48 % → 79 % | 147.5 px | 0.40 | 1.63 | 343 |
| stroke 13 | 47 % → 78 % | 133.4 px | 0.40 | 1.66 | 338 |
| stroke 14 | 46 % → 78 % | 135.2 px | 0.40 | 1.69 | 369 |
| stroke 15 | 47 % → 78 % | 134.5 px | 0.40 | 1.67 | 221 |
| stroke 16 | 48 % → 78 % | 152.3 px | 0.40 | 1.65 | 205 |
| stroke 17 | 48 % → 72 % | 141.4 px | 0.40 | 1.52 | 204 |
| stroke 18 | 49 % → 70 % | 147.0 px | 0.40 | 1.43 | 203 |
| stroke 19 | 47 % → 63 % | 139.2 px | 0.40 | 1.36 | 219 |
| stroke 20 | 47 % → 61 % | 146.4 px | 0.40 | 1.30 | 224 |
| stroke 21 | 47 % → 52 % | 137.0 px | 0.40 | 1.10 | 213 |
| stroke 22 | 47 % → 47 % | 156.1 px | 0.40 | 0.99 | 193 |

Numbers say: wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #07 Henry Ward blue L + black zigzag — own sheet
own sheet 600 × 600 · Heavy acrylic · 34 px · 3.0 s

![Brush Artist · Refs · #07 Henry Ward blue L + black zigzag — own sheet](Brush-Artist-Refs-07-Henry-Ward-blue-L-black-zigzag-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 15 % → 17 % | 35.6 px | 0.59 | 1.14 | 175 |
| stroke 2 | 17 % → 16 % | 42.8 px | 0.59 | 0.93 | 102 |

## Brush Artist · Refs · #08 Henry Ward olive bands — own sheet
own sheet 600 × 600 · Gouache · 34 px · 6.5 s

![Brush Artist · Refs · #08 Henry Ward olive bands — own sheet](Brush-Artist-Refs-08-Henry-Ward-olive-bands-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 16 % → 16 % | 32.3 px | 0.57 | 1.03 | 261 |
| stroke 2 | 27 % → 21 % | 61.7 px | 0.57 | 0.76 | 284 |
| stroke 3 | 24 % → 29 % | 50.1 px | 0.57 | 1.23 | 224 |
| stroke 4 | 28 % → 26 % | 61.0 px | 0.57 | 0.91 | 181 |
| stroke 5 | 36 % → 31 % | 73.5 px | 0.57 | 0.87 | 173 |
| stroke 6 | 25 % → 15 % | 46.3 px | 0.57 | 0.61 | 164 |

## Brush Artist · Refs · #09 Henry Ward white loops — own sheet
own sheet 600 × 600 · Gouache · 46 px · 11.2 s

![Brush Artist · Refs · #09 Henry Ward white loops — own sheet](Brush-Artist-Refs-09-Henry-Ward-white-loops-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 29 % → 42 % | 15.7 px | 0.16 | 1.41 | 996 |
| stroke 2 | 37 % → 36 % | 36.9 px | 0.17 | 0.97 | 1120 |
| stroke 3 | 43 % → 38 % | 39.6 px | 0.17 | 0.88 | 1068 |

## Brush Artist · Refs · #10 Henry Ward maroon loops — own sheet
own sheet 600 × 600 · Heavy acrylic · 30 px · 4.6 s

![Brush Artist · Refs · #10 Henry Ward maroon loops — own sheet](Brush-Artist-Refs-10-Henry-Ward-maroon-loops-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 12 % → 28 % | 28.7 px | 0.72 | 2.39 | 408 |
| stroke 2 | 22 % → 40 % | 48.5 px | 0.72 | 1.87 | 211 |
| stroke 3 | 29 % → 37 % | 58.5 px | 0.72 | 1.27 | 284 |
| stroke 4 | 41 % → 39 % | 92.8 px | 0.72 | 0.96 | 162 |
| stroke 5 | 34 % → 32 % | 85.8 px | 0.72 | 0.93 | 261 |

Numbers say: wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #11 Henry Ward purple spun balls — own sheet
own sheet 600 × 600 · Heavy acrylic · 36 px · 3.7 s

![Brush Artist · Refs · #11 Henry Ward purple spun balls — own sheet](Brush-Artist-Refs-11-Henry-Ward-purple-spun-balls-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 24 % → 35 % | 26.5 px | 0.68 | 1.43 | 306 |
| stroke 2 | 35 % → 46 % | 38.2 px | 0.68 | 1.33 | 304 |
| stroke 3 | 36 % → 34 % | 39.2 px | 0.68 | 0.97 | 396 |

## Brush Artist · Refs · #12 Henry Ward black-olive cage — own sheet
own sheet 600 × 600 · Gouache · 28 px · 8.6 s

![Brush Artist · Refs · #12 Henry Ward black-olive cage — own sheet](Brush-Artist-Refs-12-Henry-Ward-black-olive-cage-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 13 % → 21 % | 24.3 px | 0.59 | 1.64 | 261 |
| stroke 2 | 13 % → 22 % | 29.9 px | 0.59 | 1.76 | 246 |
| stroke 3 | 27 % → 28 % | 43.0 px | 0.59 | 1.04 | 336 |
| stroke 4 | 28 % → 27 % | 55.3 px | 0.59 | 0.98 | 189 |
| stroke 5 | 28 % → 18 % | 51.1 px | 0.59 | 0.65 | 182 |
| stroke 6 | 44 % → 30 % | 84.4 px | 0.59 | 0.68 | 245 |

Numbers say: wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #13 Henry Ward blue streaky form — own sheet
own sheet 600 × 600 · Gouache · 50 px · 25.4 s

![Brush Artist · Refs · #13 Henry Ward blue streaky form — own sheet](Brush-Artist-Refs-13-Henry-Ward-blue-streaky-form-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 16 % → 48 % | 48.7 px | 0.05 | 3.02 | 252 |
| stroke 2 | 22 % → 52 % | 67.0 px | 0.05 | 2.38 | 259 |
| stroke 3 | 33 % → 64 % | 95.7 px | 0.05 | 1.93 | 296 |
| stroke 4 | 33 % → 64 % | 105.8 px | 0.05 | 1.96 | 296 |
| stroke 5 | 48 % → 78 % | 138.8 px | 0.05 | 1.64 | 247 |
| stroke 6 | 47 % → 79 % | 135.4 px | 0.05 | 1.66 | 288 |
| stroke 7 | 49 % → 78 % | 144.3 px | 0.05 | 1.60 | 297 |
| stroke 8 | 49 % → 78 % | 149.4 px | 0.05 | 1.58 | 530 |
| stroke 9 | 48 % → 78 % | 150.1 px | 0.05 | 1.61 | 440 |
| stroke 10 | 48 % → 78 % | 159.4 px | 0.05 | 1.60 | 492 |
| stroke 11 | 46 % → 78 % | 142.9 px | 0.05 | 1.67 | 423 |
| stroke 12 | 48 % → 78 % | 142.7 px | 0.05 | 1.63 | 389 |
| stroke 13 | 47 % → 77 % | 145.1 px | 0.05 | 1.66 | 332 |
| stroke 14 | 45 % → 77 % | 134.5 px | 0.05 | 1.71 | 340 |
| stroke 15 | 46 % → 76 % | 132.5 px | 0.06 | 1.65 | 401 |
| stroke 16 | 48 % → 75 % | 142.0 px | 0.06 | 1.58 | 380 |
| stroke 17 | 58 % → 75 % | 144.8 px | 0.06 | 1.29 | 378 |
| stroke 18 | 60 % → 75 % | 145.4 px | 0.06 | 1.25 | 317 |
| stroke 19 | 67 % → 74 % | 136.1 px | 0.06 | 1.11 | 331 |
| stroke 20 | 75 % → 74 % | 143.2 px | 0.06 | 0.99 | 317 |

Numbers say: wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #14 Henry Ward olive totem — own sheet
own sheet 600 × 600 · Heavy acrylic · 48 px · 11.4 s

![Brush Artist · Refs · #14 Henry Ward olive totem — own sheet](Brush-Artist-Refs-14-Henry-Ward-olive-totem-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 18 % → 46 % | 46.9 px | 0.38 | 2.58 | 207 |
| stroke 2 | 21 % → 50 % | 64.3 px | 0.38 | 2.44 | 177 |
| stroke 3 | 29 % → 52 % | 100.6 px | 0.38 | 1.78 | 153 |
| stroke 4 | 30 % → 54 % | 113.7 px | 0.38 | 1.80 | 151 |
| stroke 5 | 39 % → 63 % | 135.6 px | 0.38 | 1.63 | 191 |
| stroke 6 | 39 % → 65 % | 150.4 px | 0.38 | 1.68 | 184 |
| stroke 7 | 37 % → 61 % | 124.3 px | 0.38 | 1.66 | 166 |
| stroke 8 | 37 % → 63 % | 142.4 px | 0.38 | 1.69 | 167 |
| stroke 9 | 38 % → 63 % | 130.9 px | 0.38 | 1.67 | 161 |
| stroke 10 | 38 % → 62 % | 141.0 px | 0.38 | 1.62 | 220 |
| stroke 11 | 40 % → 65 % | 143.7 px | 0.38 | 1.60 | 205 |
| stroke 12 | 38 % → 65 % | 144.2 px | 0.38 | 1.70 | 333 |
| stroke 13 | 39 % → 66 % | 135.5 px | 0.38 | 1.72 | 320 |
| stroke 14 | 37 % → 62 % | 134.5 px | 0.38 | 1.68 | 340 |
| stroke 15 | 40 % → 66 % | 136.9 px | 0.38 | 1.65 | 339 |
| stroke 16 | 38 % → 64 % | 138.8 px | 0.38 | 1.66 | 325 |
| stroke 17 | 38 % → 62 % | 126.2 px | 0.38 | 1.65 | 284 |
| stroke 18 | 40 % → 66 % | 154.9 px | 0.38 | 1.64 | 312 |
| stroke 19 | 40 % → 60 % | 137.9 px | 0.38 | 1.52 | 231 |
| stroke 20 | 41 % → 55 % | 144.4 px | 0.38 | 1.34 | 273 |
| stroke 21 | 46 % → 55 % | 137.7 px | 0.38 | 1.18 | 236 |
| stroke 22 | 54 % → 53 % | 146.7 px | 0.38 | 0.99 | 205 |

Numbers say: wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #15 Ultramarine brush script — own sheet
own sheet 600 × 600 · Ink · 4 px · 15.0 s

![Brush Artist · Refs · #15 Ultramarine brush script — own sheet](Brush-Artist-Refs-15-Ultramarine-brush-script-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 39 % → 42 % | 8.9 px | 0.67 | 1.05 | 85 |
| stroke 2 | 40 % → 42 % | 8.8 px | 0.66 | 1.06 | 78 |
| stroke 3 | 40 % → 42 % | 9.5 px | 0.73 | 1.06 | 41 |
| stroke 4 | 42 % → 45 % | 10.1 px | 0.74 | 1.08 | 27 |
| stroke 5 | 44 % → 48 % | 9.7 px | 0.73 | 1.08 | 46 |
| stroke 6 | 42 % → 44 % | 9.4 px | 0.65 | 1.04 | 109 |
| stroke 7 | 43 % → 46 % | 9.2 px | 0.72 | 1.08 | 60 |
| stroke 8 | 38 % → 40 % | 9.2 px | 0.68 | 1.06 | 75 |
| stroke 9 | 40 % → 42 % | 9.2 px | 0.69 | 1.06 | 69 |
| stroke 10 | 36 % → 38 % | 9.8 px | 0.68 | 1.05 | 79 |
| stroke 11 | 42 % → 45 % | 9.5 px | 0.70 | 1.06 | 57 |
| stroke 12 | 39 % → 41 % | 9.4 px | 0.66 | 1.05 | 91 |
| stroke 13 | 45 % → 48 % | 10.2 px | 0.71 | 1.06 | 84 |
| stroke 14 | 38 % → 41 % | 9.8 px | 0.72 | 1.06 | 38 |
| stroke 15 | 37 % → 39 % | 9.1 px | 0.69 | 1.06 | 70 |
| stroke 16 | 42 % → 45 % | 9.4 px | 0.72 | 1.06 | 51 |
| stroke 17 | 41 % → 44 % | 7.1 px | 0.71 | 1.08 | 86 |
| stroke 18 | 43 % → 45 % | 9.2 px | 0.73 | 1.06 | 48 |
| stroke 19 | 39 % → 41 % | 8.8 px | 0.66 | 1.05 | 98 |
| stroke 20 | 40 % → 43 % | 9.4 px | 0.71 | 1.06 | 48 |
| stroke 21 | 40 % → 43 % | 9.9 px | 0.70 | 1.06 | 44 |
| stroke 22 | 42 % → 44 % | 8.4 px | 0.65 | 1.06 | 84 |
| stroke 23 | 40 % → 43 % | 10.1 px | 0.73 | 1.07 | 35 |
| stroke 24 | 38 % → 40 % | 8.7 px | 0.73 | 1.07 | 42 |
| stroke 25 | 40 % → 43 % | 9.8 px | 0.72 | 1.07 | 53 |
| stroke 26 | 46 % → 48 % | 9.2 px | 0.68 | 1.05 | 60 |
| stroke 27 | 42 % → 45 % | 8.8 px | 0.63 | 1.05 | 84 |
| stroke 28 | 44 % → 46 % | 9.1 px | 0.70 | 1.06 | 54 |
| stroke 29 | 36 % → 39 % | 10.6 px | 0.72 | 1.08 | 39 |
| stroke 30 | 39 % → 40 % | 8.6 px | 0.71 | 1.04 | 47 |
| stroke 31 | 43 % → 46 % | 10.3 px | 0.75 | 1.07 | 29 |
| stroke 32 | 42 % → 45 % | 9.4 px | 0.73 | 1.09 | 41 |
| stroke 33 | 35 % → 38 % | 10.8 px | 0.72 | 1.08 | 34 |
| stroke 34 | 40 % → 43 % | 9.7 px | 0.73 | 1.07 | 54 |
| stroke 35 | 35 % → 37 % | 9.3 px | 0.65 | 1.05 | 90 |

## Brush Artist · Refs · #18 Blue oil-stick scribbles — own sheet
own sheet 600 × 600 · Pastel · 10 px · 5.5 s

![Brush Artist · Refs · #18 Blue oil-stick scribbles — own sheet](Brush-Artist-Refs-18-Blue-oil-stick-scribbles-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 15 % → 31 % | 3.8 px | 0.49 | 2.11 | 219 |
| stroke 2 | 13 % → 37 % | 3.6 px | 0.49 | 2.73 | 277 |
| stroke 3 | 16 % → 26 % | 5.8 px | 0.49 | 1.66 | 310 |
| stroke 4 | 15 % → 29 % | 8.0 px | 0.49 | 1.88 | 276 |
| stroke 5 | 29 % → 34 % | 8.4 px | 0.49 | 1.19 | 234 |
| stroke 6 | 25 % → 26 % | 9.4 px | 0.49 | 1.02 | 217 |
| stroke 7 | 26 % → 32 % | 8.3 px | 0.49 | 1.24 | 249 |
| stroke 8 | 30 % → 30 % | 17.0 px | 0.49 | 1.00 | 262 |

Numbers say: wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #20 Orange-red crayon scribble — own sheet
own sheet 600 × 600 · Pastel · 14 px · 5.3 s

![Brush Artist · Refs · #20 Orange-red crayon scribble — own sheet](Brush-Artist-Refs-20-Orange-red-crayon-scribble-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 8 % → 18 % | 5.5 px | 0.59 | 2.46 | 467 |
| stroke 2 | 9 % → 23 % | 6.8 px | 0.59 | 2.48 | 413 |
| stroke 3 | 13 % → 21 % | 8.5 px | 0.59 | 1.64 | 341 |
| stroke 4 | 24 % → 32 % | 8.9 px | 0.59 | 1.34 | 432 |
| stroke 5 | 27 % → 27 % | 7.7 px | 0.59 | 1.00 | 370 |
| stroke 6 | 22 % → 22 % | 16.8 px | 0.59 | 1.00 | 325 |

Numbers say: wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #21 Gritty black contours — own sheet
own sheet 600 × 600 · Gouache · 12 px · 6.4 s

![Brush Artist · Refs · #21 Gritty black contours — own sheet](Brush-Artist-Refs-21-Gritty-black-contours-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 10 % → 8 % | 10.6 px | 0.36 | 0.84 | 256 |
| stroke 2 | 9 % → 5 % | 15.4 px | 0.36 | 0.57 | 313 |
| stroke 3 | 14 % → 4 % | 12.9 px | 0.36 | 0.28 | 193 |
| stroke 4 | 16 % → 8 % | 19.7 px | 0.36 | 0.50 | 197 |
| stroke 5 | 18 % → 8 % | 21.5 px | 0.36 | 0.47 | 117 |

## Brush Artist · Refs · #22 Bold black brush poster — own sheet
own sheet 600 × 600 · Ink · 20 px · 7.7 s

![Brush Artist · Refs · #22 Bold black brush poster — own sheet](Brush-Artist-Refs-22-Bold-black-brush-poster-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 22 % → 27 % | 36.3 px | 0.94 | 1.20 | 154 |
| stroke 2 | 27 % → 37 % | 41.4 px | 0.95 | 1.36 | 37 |
| stroke 3 | 28 % → 28 % | 43.6 px | 0.94 | 1.00 | 56 |
| stroke 4 | 27 % → 39 % | 53.8 px | 0.94 | 1.42 | 76 |
| stroke 5 | 25 % → 25 % | 42.9 px | 0.94 | 1.00 | 145 |

## Brush Artist · Refs · #23 Dry white on orange + black line — own sheet
own sheet 600 × 600 · Gouache · 50 px · 15.2 s

![Brush Artist · Refs · #23 Dry white on orange + black line — own sheet](Brush-Artist-Refs-23-Dry-white-on-orange-black-line-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 13 % → 35 % | 44.0 px | 0.44 | 2.78 | 253 |
| stroke 2 | 15 % → 32 % | 53.3 px | 0.44 | 2.13 | 276 |
| stroke 3 | 22 % → 35 % | 82.6 px | 0.44 | 1.59 | 254 |
| stroke 4 | 24 % → 39 % | 95.4 px | 0.44 | 1.61 | 262 |
| stroke 5 | 35 % → 47 % | 126.2 px | 0.44 | 1.36 | 296 |
| stroke 6 | 36 % → 51 % | 146.8 px | 0.44 | 1.43 | 231 |
| stroke 7 | 31 % → 50 % | 118.1 px | 0.44 | 1.61 | 252 |
| stroke 8 | 31 % → 48 % | 122.2 px | 0.44 | 1.52 | 251 |
| stroke 9 | 31 % → 48 % | 117.4 px | 0.44 | 1.54 | 234 |
| stroke 10 | 32 % → 49 % | 127.1 px | 0.43 | 1.51 | 238 |
| stroke 11 | 35 % → 51 % | 129.9 px | 0.43 | 1.48 | 206 |
| stroke 12 | 35 % → 50 % | 135.5 px | 0.44 | 1.45 | 297 |
| stroke 13 | 36 % → 53 % | 134.7 px | 0.43 | 1.45 | 398 |
| stroke 14 | 35 % → 52 % | 137.7 px | 0.43 | 1.48 | 395 |
| stroke 15 | 35 % → 47 % | 132.2 px | 0.43 | 1.33 | 306 |
| stroke 16 | 34 % → 41 % | 135.8 px | 0.43 | 1.19 | 278 |
| stroke 17 | 34 % → 34 % | 119.2 px | 0.43 | 1.01 | 330 |
| stroke 18 | 41 % → 36 % | 149.1 px | 0.43 | 0.88 | 230 |

Numbers say: wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #24 Picasso flat oil — own sheet
own sheet 600 × 600 · Oil · 34 px · 8.2 s

![Brush Artist · Refs · #24 Picasso flat oil — own sheet](Brush-Artist-Refs-24-Picasso-flat-oil-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 16 % → 45 % | 34.7 px | 0.23 | 2.74 | 218 |
| stroke 2 | 20 % → 48 % | 47.2 px | 0.24 | 2.40 | 179 |
| stroke 3 | 29 % → 59 % | 62.5 px | 0.23 | 2.07 | 175 |
| stroke 4 | 37 % → 65 % | 83.1 px | 0.23 | 1.76 | 201 |
| stroke 5 | 43 % → 71 % | 94.5 px | 0.23 | 1.65 | 190 |
| stroke 6 | 44 % → 66 % | 102.1 px | 0.23 | 1.50 | 184 |
| stroke 7 | 45 % → 66 % | 94.8 px | 0.23 | 1.46 | 286 |
| stroke 8 | 44 % → 66 % | 106.9 px | 0.23 | 1.50 | 329 |
| stroke 9 | 37 % → 62 % | 81.5 px | 0.23 | 1.67 | 300 |
| stroke 10 | 39 % → 62 % | 93.1 px | 0.23 | 1.58 | 288 |
| stroke 11 | 37 % → 60 % | 78.6 px | 0.23 | 1.62 | 253 |
| stroke 12 | 38 % → 61 % | 91.1 px | 0.23 | 1.60 | 264 |
| stroke 13 | 38 % → 67 % | 84.4 px | 0.23 | 1.76 | 239 |
| stroke 14 | 39 % → 69 % | 88.9 px | 0.23 | 1.75 | 255 |
| stroke 15 | 39 % → 62 % | 83.3 px | 0.23 | 1.58 | 230 |
| stroke 16 | 38 % → 55 % | 87.9 px | 0.23 | 1.43 | 218 |
| stroke 17 | 43 % → 48 % | 90.0 px | 0.23 | 1.12 | 196 |
| stroke 18 | 42 % → 42 % | 102.6 px | 0.23 | 1.00 | 204 |

Numbers say: wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #25 Yellow heavy flat stroke — own sheet
own sheet 600 × 600 · Heavy acrylic · 110 px · 4.7 s

![Brush Artist · Refs · #25 Yellow heavy flat stroke — own sheet](Brush-Artist-Refs-25-Yellow-heavy-flat-stroke-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 18 % → 18 % | 104.2 px | 0.17 | 0.98 | 1407 |

## Brush Artist · Refs · #27 Orange impasto swatch — own sheet
own sheet 600 × 600 · Heavy acrylic · 60 px · 4.5 s

![Brush Artist · Refs · #27 Orange impasto swatch — own sheet](Brush-Artist-Refs-27-Orange-impasto-swatch-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 8 % → 21 % | 61.8 px | 0.33 | 2.60 | 104 |
| stroke 2 | 7 % → 33 % | 62.5 px | 0.33 | 4.67 | 66 |
| stroke 3 | 25 % → 36 % | 245.4 px | 0.33 | 1.40 | 50 |
| stroke 4 | 10 % → 12 % | 69.5 px | 0.33 | 1.25 | 93 |
| stroke 5 | 17 % → 33 % | 63.5 px | 0.33 | 1.90 | 95 |
| stroke 6 | 18 % → 31 % | 145.0 px | 0.33 | 1.79 | 112 |
| stroke 7 | 8 % → 15 % | 70.2 px | 0.33 | 1.86 | 89 |
| stroke 8 | 33 % → 34 % | 337.0 px | 0.33 | 1.04 | 64 |
| stroke 9 | 38 % → 37 % | 185.4 px | 0.33 | 0.98 | 92 |
| stroke 10 | 33 % → 33 % | 304.7 px | 0.33 | 0.98 | 74 |

Numbers say: wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #28 Miles Davis black lines — own sheet
own sheet 600 × 600 · Ink · 22 px · 10.0 s

![Brush Artist · Refs · #28 Miles Davis black lines — own sheet](Brush-Artist-Refs-28-Miles-Davis-black-lines-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 22 % → 32 % | 36.4 px | 0.88 | 1.42 | 226 |
| stroke 2 | 28 % → 48 % | 38.1 px | 0.88 | 1.73 | 175 |
| stroke 3 | 39 % → 44 % | 75.0 px | 0.88 | 1.12 | 166 |
| stroke 4 | 42 % → 48 % | 83.5 px | 0.88 | 1.15 | 268 |
| stroke 5 | 55 % → 55 % | 109.6 px | 0.88 | 1.00 | 186 |

Numbers say: wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #29 Shrigley magenta asterisk — own sheet
own sheet 600 × 600 · Watercolor · 70 px · 10.3 s

![Brush Artist · Refs · #29 Shrigley magenta asterisk — own sheet](Brush-Artist-Refs-29-Shrigley-magenta-asterisk-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 13 % → 37 % | 46.6 px | 0.72 | 2.85 | 249 |
| stroke 2 | 12 % → 12 % | 87.1 px | 0.71 | 1.00 | 234 |
| stroke 3 | 28 % → 37 % | 100.9 px | 0.72 | 1.31 | 233 |
| stroke 4 | 23 % → 23 % | 163.9 px | 0.71 | 1.02 | 251 |

Numbers say: wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #30 Red gouache face patch — own sheet
own sheet 600 × 600 · Gouache · 60 px · 19.4 s

![Brush Artist · Refs · #30 Red gouache face patch — own sheet](Brush-Artist-Refs-30-Red-gouache-face-patch-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 12 % → 37 % | 51.5 px | 0.53 | 3.23 | 275 |
| stroke 2 | 15 % → 40 % | 74.5 px | 0.53 | 2.72 | 214 |
| stroke 3 | 24 % → 50 % | 115.9 px | 0.53 | 2.06 | 183 |
| stroke 4 | 27 % → 51 % | 134.0 px | 0.53 | 1.93 | 229 |
| stroke 5 | 34 % → 60 % | 159.9 px | 0.53 | 1.77 | 289 |
| stroke 6 | 35 % → 61 % | 178.2 px | 0.53 | 1.76 | 244 |
| stroke 7 | 34 % → 59 % | 160.8 px | 0.53 | 1.73 | 337 |
| stroke 8 | 34 % → 56 % | 162.4 px | 0.53 | 1.65 | 703 |
| stroke 9 | 36 % → 60 % | 173.0 px | 0.53 | 1.66 | 362 |
| stroke 10 | 38 % → 62 % | 196.7 px | 0.53 | 1.64 | 395 |
| stroke 11 | 37 % → 61 % | 182.4 px | 0.53 | 1.66 | 363 |
| stroke 12 | 36 % → 58 % | 178.3 px | 0.53 | 1.62 | 341 |
| stroke 13 | 33 % → 46 % | 156.5 px | 0.53 | 1.39 | 220 |
| stroke 14 | 33 % → 41 % | 157.6 px | 0.53 | 1.25 | 258 |
| stroke 15 | 33 % → 37 % | 153.3 px | 0.53 | 1.12 | 267 |
| stroke 16 | 39 % → 39 % | 184.8 px | 0.53 | 0.99 | 268 |

Numbers say: wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #31 Warhol blotted line — own sheet
own sheet 600 × 600 · Ink · 6 px · 6.4 s

![Brush Artist · Refs · #31 Warhol blotted line — own sheet](Brush-Artist-Refs-31-Warhol-blotted-line-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 21 % → 42 % | 15.7 px | 0.82 | 1.98 | 176 |
| stroke 2 | 17 % → 23 % | 15.8 px | 0.82 | 1.34 | 111 |
| stroke 3 | 24 % → 25 % | 25.0 px | 0.82 | 1.02 | 100 |
| stroke 4 | 31 % → 40 % | 31.7 px | 0.82 | 1.28 | 62 |
| stroke 5 | 35 % → 43 % | 36.3 px | 0.82 | 1.23 | 133 |
| stroke 6 | 32 % → 33 % | 26.5 px | 0.81 | 1.03 | 107 |

Numbers say: wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #32 Thick orange swipes — own sheet
own sheet 600 × 600 · Heavy acrylic · 90 px · 4.7 s

![Brush Artist · Refs · #32 Thick orange swipes — own sheet](Brush-Artist-Refs-32-Thick-orange-swipes-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 14 % → 27 % | 86.0 px | 0.03 | 1.90 | 545 |
| stroke 2 | 26 % → 38 % | 176.9 px | 0.03 | 1.43 | 456 |
| stroke 3 | 28 % → 27 % | 177.5 px | 0.03 | 0.98 | 300 |

Numbers say: wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #33 Red wet-in-wet band — own sheet
own sheet 600 × 600 · Watercolor · 80 px · 13.6 s

![Brush Artist · Refs · #33 Red wet-in-wet band — own sheet](Brush-Artist-Refs-33-Red-wet-in-wet-band-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 23 % → 56 % | 88.2 px | 0.62 | 2.41 | 406 |
| stroke 2 | 30 % → 51 % | 243.8 px | 0.62 | 1.69 | 120 |
| stroke 3 | 37 % → 53 % | 355.7 px | 0.62 | 1.45 | 214 |
| stroke 4 | 42 % → 60 % | 410.7 px | 0.63 | 1.41 | 196 |
| stroke 5 | 42 % → 54 % | 352.8 px | 0.62 | 1.31 | 261 |
| stroke 6 | 42 % → 46 % | 320.2 px | 0.61 | 1.10 | 437 |

Numbers say: wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #34 Magenta oil patches — own sheet
own sheet 600 × 600 · Oil · 60 px · 8.1 s

![Brush Artist · Refs · #34 Magenta oil patches — own sheet](Brush-Artist-Refs-34-Magenta-oil-patches-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 9 % → 42 % | 61.9 px | 0.13 | 4.82 | 205 |
| stroke 2 | 9 % → 29 % | 62.8 px | 0.13 | 3.15 | 246 |
| stroke 3 | 7 % → 35 % | 62.3 px | 0.13 | 4.71 | 172 |
| stroke 4 | 16 % → 20 % | 132.0 px | 0.12 | 1.27 | 145 |
| stroke 5 | 23 % → 33 % | 124.6 px | 0.13 | 1.43 | 197 |
| stroke 6 | 20 % → 38 % | 171.4 px | 0.13 | 1.90 | 177 |
| stroke 7 | 30 % → 35 % | 237.9 px | 0.13 | 1.18 | 164 |
| stroke 8 | 33 % → 39 % | 235.0 px | 0.13 | 1.18 | 317 |
| stroke 9 | 25 % → 26 % | 159.7 px | 0.13 | 1.07 | 393 |
| stroke 10 | 29 % → 29 % | 257.2 px | 0.13 | 1.00 | 280 |
| stroke 11 | 36 % → 36 % | 324.6 px | 0.13 | 1.00 | 136 |
| stroke 12 | 26 % → 26 % | 184.4 px | 0.13 | 1.00 | 139 |

Numbers say: wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #35 Red band with runs — own sheet
own sheet 600 × 600 · Watercolor · 70 px · 6.6 s

![Brush Artist · Refs · #35 Red band with runs — own sheet](Brush-Artist-Refs-35-Red-band-with-runs-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 21 % → 32 % | 77.5 px | 0.50 | 1.54 | 436 |

Numbers say: wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #36 Magenta letters flat brush — own sheet
own sheet 600 × 600 · Gouache · 36 px · 14.4 s

![Brush Artist · Refs · #36 Magenta letters flat brush — own sheet](Brush-Artist-Refs-36-Magenta-letters-flat-brush-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 20 % → 39 % | 59.1 px | 0.50 | 1.95 | 37 |
| stroke 2 | 20 % → 32 % | 46.7 px | 0.50 | 1.59 | 34 |
| stroke 3 | 29 % → 54 % | 86.9 px | 0.50 | 1.86 | 29 |
| stroke 4 | 26 % → 44 % | 51.2 px | 0.50 | 1.67 | 138 |
| stroke 5 | 33 % → 55 % | 96.1 px | 0.50 | 1.67 | 138 |
| stroke 6 | 42 % → 56 % | 242.5 px | 0.50 | 1.33 | 31 |
| stroke 7 | 30 % → 44 % | 56.7 px | 0.50 | 1.45 | 116 |
| stroke 8 | 31 % → 53 % | 98.5 px | 0.50 | 1.68 | 70 |
| stroke 9 | 38 % → 51 % | 158.3 px | 0.50 | 1.33 | 36 |
| stroke 10 | 37 % → 63 % | 106.7 px | 0.50 | 1.72 | 115 |
| stroke 11 | 39 % → 62 % | 225.9 px | 0.50 | 1.58 | 20 |
| stroke 12 | 43 % → 56 % | 81.8 px | 0.50 | 1.29 | 143 |
| stroke 13 | 33 % → 46 % | 117.7 px | 0.50 | 1.43 | 34 |
| stroke 14 | 35 % → 52 % | 134.5 px | 0.50 | 1.47 | 30 |
| stroke 15 | 38 % → 56 % | 108.5 px | 0.50 | 1.49 | 82 |
| stroke 16 | 41 % → 50 % | 231.8 px | 0.50 | 1.23 | 16 |
| stroke 17 | 44 % → 52 % | 81.6 px | 0.50 | 1.19 | 155 |
| stroke 18 | 27 % → 36 % | 97.6 px | 0.50 | 1.35 | 50 |
| stroke 19 | 40 % → 39 % | 117.2 px | 0.50 | 0.96 | 38 |
| stroke 20 | 45 % → 45 % | 132.3 px | 0.50 | 0.98 | 28 |
| stroke 21 | 41 % → 39 % | 78.6 px | 0.50 | 0.96 | 95 |

Numbers say: wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #37 Oil still life dabs — own sheet
own sheet 600 × 600 · Oil · 40 px · 4.8 s

![Brush Artist · Refs · #37 Oil still life dabs — own sheet](Brush-Artist-Refs-37-Oil-still-life-dabs-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 7 % → 7 % | 44.1 px | 0.39 | 1.00 | 53 |
| stroke 2 | 6 % → 27 % | 44.4 px | 0.39 | 4.43 | 29 |
| stroke 3 | 12 % → 36 % | 92.6 px | 0.39 | 3.01 | 19 |
| stroke 4 | 9 % → 9 % | 42.7 px | 0.39 | 1.00 | 40 |
| stroke 5 | 6 % → 10 % | 43.2 px | 0.39 | 1.71 | 20 |
| stroke 6 | 13 % → 31 % | 83.4 px | 0.39 | 2.32 | 29 |
| stroke 7 | 11 % → 24 % | 115.5 px | 0.39 | 2.18 | 30 |
| stroke 8 | 8 % → 14 % | 89.6 px | 0.39 | 1.63 | 16 |
| stroke 9 | 13 % → 14 % | 68.1 px | 0.38 | 1.09 | 34 |
| stroke 10 | 21 % → 25 % | 106.5 px | 0.39 | 1.20 | 39 |
| stroke 11 | 24 % → 28 % | 201.6 px | 0.39 | 1.17 | 38 |
| stroke 12 | 21 % → 21 % | 227.4 px | 0.39 | 1.01 | 16 |
| stroke 13 | 16 % → 16 % | 167.7 px | 0.40 | 1.00 | 26 |
| stroke 14 | 16 % → 16 % | 132.7 px | 0.39 | 1.00 | 24 |

Numbers say: wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #38 Sanguine drawing — own sheet
own sheet 600 × 600 · Pastel · 6 px · 2.7 s

![Brush Artist · Refs · #38 Sanguine drawing — own sheet](Brush-Artist-Refs-38-Sanguine-drawing-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 3 % → 14 % | 2.9 px | 0.57 | 5.29 | 9 |
| stroke 2 | 3 % → 7 % | 2.9 px | 0.57 | 2.89 | 9 |
| stroke 3 | 3 % → 9 % | 2.9 px | 0.57 | 3.40 | 7 |
| stroke 4 | 2 % → 17 % | 2.7 px | 0.57 | 7.20 | 8 |
| stroke 5 | 2 % → 7 % | 2.7 px | 0.57 | 3.03 | 6 |
| stroke 6 | 3 % → 19 % | 3.4 px | 0.57 | 6.31 | 7 |
| stroke 7 | 5 % → 14 % | 5.2 px | 0.57 | 3.07 | 7 |
| stroke 8 | 4 % → 16 % | 4.7 px | 0.57 | 3.79 | 6 |
| stroke 9 | 3 % → 7 % | 2.9 px | 0.57 | 2.66 | 8 |
| stroke 10 | 4 % → 16 % | 4.7 px | 0.57 | 3.83 | 6 |
| stroke 11 | 3 % → 4 % | 2.9 px | 0.57 | 1.61 | 6 |
| stroke 12 | 4 % → 15 % | 4.8 px | 0.57 | 3.58 | 6 |
| stroke 13 | 8 % → 17 % | 8.9 px | 0.57 | 2.23 | 6 |
| stroke 14 | 4 % → 14 % | 4.9 px | 0.57 | 3.19 | 6 |
| stroke 15 | 9 % → 18 % | 10.7 px | 0.57 | 1.86 | 6 |
| stroke 16 | 6 % → 16 % | 6.6 px | 0.57 | 2.71 | 6 |
| stroke 17 | 4 % → 9 % | 4.4 px | 0.57 | 2.25 | 6 |
| stroke 18 | 3 % → 5 % | 2.9 px | 0.57 | 1.85 | 6 |
| stroke 19 | 6 % → 16 % | 6.9 px | 0.57 | 2.68 | 6 |
| stroke 20 | 8 % → 14 % | 9.2 px | 0.57 | 1.70 | 6 |
| stroke 21 | 4 % → 4 % | 4.3 px | 0.57 | 1.00 | 7 |
| stroke 22 | 8 % → 13 % | 8.6 px | 0.57 | 1.79 | 7 |
| stroke 23 | 7 % → 12 % | 8.3 px | 0.57 | 1.61 | 8 |
| stroke 24 | 4 % → 7 % | 4.7 px | 0.57 | 1.71 | 7 |
| stroke 25 | 8 % → 14 % | 8.7 px | 0.57 | 1.84 | 11 |
| stroke 26 | 6 % → 8 % | 6.5 px | 0.57 | 1.34 | 10 |
| stroke 27 | 4 % → 4 % | 4.3 px | 0.57 | 1.10 | 6 |
| stroke 28 | 7 % → 11 % | 8.2 px | 0.57 | 1.59 | 6 |
| stroke 29 | 8 % → 17 % | 8.8 px | 0.57 | 2.21 | 7 |
| stroke 30 | 13 % → 17 % | 14.9 px | 0.57 | 1.29 | 7 |
| stroke 31 | 5 % → 6 % | 5.4 px | 0.57 | 1.29 | 6 |
| stroke 32 | 10 % → 13 % | 11.8 px | 0.57 | 1.24 | 7 |
| stroke 33 | 7 % → 8 % | 8.5 px | 0.57 | 1.07 | 6 |
| stroke 34 | 11 % → 14 % | 12.0 px | 0.57 | 1.36 | 6 |
| stroke 35 | 9 % → 14 % | 10.0 px | 0.57 | 1.61 | 6 |
| stroke 36 | 10 % → 13 % | 11.4 px | 0.57 | 1.26 | 6 |
| stroke 37 | 9 % → 16 % | 10.5 px | 0.57 | 1.71 | 6 |
| stroke 38 | 13 % → 19 % | 14.8 px | 0.57 | 1.48 | 7 |
| stroke 39 | 14 % → 17 % | 15.7 px | 0.57 | 1.21 | 6 |
| stroke 40 | 6 % → 7 % | 7.2 px | 0.57 | 1.14 | 6 |
| stroke 41 | 16 % → 16 % | 17.7 px | 0.57 | 1.01 | 7 |
| stroke 42 | 14 % → 16 % | 15.2 px | 0.57 | 1.17 | 7 |
| stroke 43 | 10 % → 12 % | 11.6 px | 0.57 | 1.17 | 11 |
| stroke 44 | 12 % → 15 % | 14.3 px | 0.57 | 1.22 | 7 |
| stroke 45 | 2 % → 2 % | 2.7 px | 0.57 | 1.00 | 10 |
| stroke 46 | 16 % → 16 % | 18.5 px | 0.57 | 1.00 | 9 |
| stroke 47 | 13 % → 13 % | 15.0 px | 0.57 | 1.00 | 8 |
| stroke 48 | 12 % → 13 % | 14.3 px | 0.57 | 1.07 | 11 |
| stroke 49 | 19 % → 19 % | 21.5 px | 0.57 | 1.00 | 15 |
| stroke 50 | 10 % → 10 % | 11.6 px | 0.57 | 1.00 | 11 |

Numbers say: wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #39 Very thick impasto — own sheet
own sheet 600 × 600 · Heavy acrylic · 60 px · 6.9 s

![Brush Artist · Refs · #39 Very thick impasto — own sheet](Brush-Artist-Refs-39-Very-thick-impasto-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 26 % → 37 % | 59.6 px | 0.43 | 1.42 | 563 |
| stroke 2 | 31 % → 48 % | 93.9 px | 0.44 | 1.54 | 548 |
| stroke 3 | 37 % → 49 % | 124.6 px | 0.43 | 1.33 | 453 |
| stroke 4 | 31 % → 44 % | 90.9 px | 0.44 | 1.41 | 446 |
| stroke 5 | 42 % → 41 % | 104.2 px | 0.44 | 0.98 | 413 |

Numbers say: wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #40 Watercolour blooms — own sheet
own sheet 600 × 600 · Watercolor · 90 px · 8.5 s

![Brush Artist · Refs · #40 Watercolour blooms — own sheet](Brush-Artist-Refs-40-Watercolour-blooms-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 21 % → 25 % | 92.4 px | 0.13 | 1.19 | 1058 |

## Brush Artist · Refs · #41 Coloured pencil hatching — own sheet
own sheet 600 × 600 · Pastel · 4 px · 3.2 s

![Brush Artist · Refs · #41 Coloured pencil hatching — own sheet](Brush-Artist-Refs-41-Coloured-pencil-hatching-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 3 % → 13 % | 2.2 px | 0.35 | 4.64 | 11 |
| stroke 2 | 3 % → 7 % | 2.3 px | 0.35 | 2.29 | 5 |
| stroke 3 | 2 % → 11 % | 1.9 px | 0.35 | 4.38 | 10 |
| stroke 4 | 3 % → 19 % | 2.1 px | 0.35 | 6.73 | 6 |
| stroke 5 | 4 % → 7 % | 2.9 px | 0.35 | 1.83 | 5 |
| stroke 6 | 3 % → 13 % | 2.3 px | 0.35 | 4.19 | 7 |
| stroke 7 | 3 % → 15 % | 2.6 px | 0.35 | 4.43 | 4 |
| stroke 8 | 3 % → 12 % | 2.1 px | 0.35 | 4.20 | 7 |
| stroke 9 | 5 % → 11 % | 3.6 px | 0.35 | 2.27 | 4 |
| stroke 10 | 5 % → 15 % | 3.8 px | 0.35 | 2.99 | 9 |
| stroke 11 | 4 % → 13 % | 3.0 px | 0.35 | 3.28 | 4 |
| stroke 12 | 3 % → 3 % | 2.1 px | 0.35 | 1.00 | 4 |
| stroke 13 | 7 % → 17 % | 5.2 px | 0.35 | 2.45 | 5 |
| stroke 14 | 3 % → 13 % | 2.4 px | 0.35 | 4.19 | 9 |
| stroke 15 | 6 % → 12 % | 4.4 px | 0.35 | 2.09 | 5 |
| stroke 16 | 7 % → 11 % | 5.1 px | 0.35 | 1.61 | 4 |
| stroke 17 | 3 % → 3 % | 2.1 px | 0.35 | 1.00 | 8 |
| stroke 18 | 5 % → 8 % | 3.6 px | 0.35 | 1.65 | 5 |
| stroke 19 | 5 % → 13 % | 3.8 px | 0.35 | 2.72 | 4 |
| stroke 20 | 5 % → 14 % | 3.7 px | 0.35 | 2.92 | 4 |
| stroke 21 | 4 % → 13 % | 3.2 px | 0.35 | 3.20 | 4 |
| stroke 22 | 9 % → 16 % | 6.8 px | 0.35 | 1.77 | 4 |
| stroke 23 | 9 % → 13 % | 6.5 px | 0.35 | 1.55 | 6 |
| stroke 24 | 6 % → 14 % | 4.7 px | 0.35 | 2.18 | 6 |
| stroke 25 | 5 % → 10 % | 3.5 px | 0.35 | 2.27 | 5 |
| stroke 26 | 3 % → 6 % | 2.7 px | 0.35 | 1.81 | 5 |
| stroke 27 | 3 % → 7 % | 2.3 px | 0.35 | 2.26 | 8 |
| stroke 28 | 6 % → 10 % | 4.5 px | 0.35 | 1.70 | 6 |
| stroke 29 | 3 % → 13 % | 2.4 px | 0.35 | 4.21 | 6 |
| stroke 30 | 6 % → 9 % | 4.4 px | 0.35 | 1.46 | 7 |
| stroke 31 | 7 % → 14 % | 5.1 px | 0.35 | 2.14 | 5 |
| stroke 32 | 3 % → 6 % | 2.5 px | 0.35 | 1.79 | 5 |
| stroke 33 | 6 % → 11 % | 5.0 px | 0.35 | 1.67 | 5 |
| stroke 34 | 3 % → 6 % | 2.6 px | 0.35 | 1.73 | 5 |
| stroke 35 | 7 % → 14 % | 5.0 px | 0.35 | 2.09 | 8 |
| stroke 36 | 5 % → 5 % | 3.7 px | 0.35 | 1.01 | 9 |
| stroke 37 | 7 % → 15 % | 5.2 px | 0.35 | 2.15 | 5 |
| stroke 38 | 8 % → 13 % | 5.8 px | 0.35 | 1.66 | 5 |
| stroke 39 | 7 % → 11 % | 5.1 px | 0.35 | 1.67 | 5 |
| stroke 40 | 8 % → 18 % | 6.2 px | 0.35 | 2.21 | 5 |
| stroke 41 | 9 % → 13 % | 6.9 px | 0.35 | 1.48 | 8 |
| stroke 42 | 10 % → 17 % | 7.7 px | 0.35 | 1.73 | 5 |
| stroke 43 | 5 % → 9 % | 3.9 px | 0.35 | 1.66 | 5 |
| stroke 44 | 10 % → 13 % | 7.3 px | 0.35 | 1.40 | 4 |
| stroke 45 | 13 % → 18 % | 9.9 px | 0.35 | 1.35 | 8 |
| stroke 46 | 5 % → 7 % | 3.6 px | 0.34 | 1.41 | 6 |
| stroke 47 | 11 % → 13 % | 8.0 px | 0.35 | 1.20 | 7 |
| stroke 48 | 12 % → 16 % | 9.2 px | 0.35 | 1.34 | 7 |
| stroke 49 | 6 % → 9 % | 4.2 px | 0.35 | 1.66 | 4 |
| stroke 50 | 7 % → 7 % | 5.2 px | 0.34 | 1.00 | 6 |
| stroke 51 | 8 % → 15 % | 6.4 px | 0.35 | 1.74 | 7 |
| stroke 52 | 12 % → 14 % | 9.1 px | 0.35 | 1.19 | 5 |
| stroke 53 | 11 % → 14 % | 8.1 px | 0.35 | 1.36 | 5 |
| stroke 54 | 10 % → 14 % | 7.4 px | 0.35 | 1.47 | 6 |
| stroke 55 | 11 % → 14 % | 8.2 px | 0.35 | 1.33 | 5 |
| stroke 56 | 11 % → 12 % | 8.4 px | 0.35 | 1.11 | 5 |
| stroke 57 | 9 % → 13 % | 7.1 px | 0.35 | 1.37 | 5 |
| stroke 58 | 10 % → 11 % | 7.7 px | 0.35 | 1.14 | 4 |
| stroke 59 | 11 % → 13 % | 8.4 px | 0.35 | 1.18 | 4 |
| stroke 60 | 16 % → 20 % | 11.9 px | 0.35 | 1.26 | 5 |
| stroke 61 | 19 % → 20 % | 14.5 px | 0.35 | 1.04 | 6 |
| stroke 62 | 10 % → 10 % | 7.3 px | 0.35 | 1.00 | 5 |
| stroke 63 | 11 % → 12 % | 8.7 px | 0.35 | 1.07 | 5 |
| stroke 64 | 14 % → 14 % | 10.7 px | 0.35 | 1.02 | 5 |
| stroke 65 | 15 % → 15 % | 11.5 px | 0.35 | 1.00 | 6 |
| stroke 66 | 14 % → 14 % | 10.7 px | 0.35 | 1.00 | 5 |
| stroke 67 | 12 % → 12 % | 8.8 px | 0.35 | 1.06 | 5 |
| stroke 68 | 5 % → 9 % | 3.6 px | 0.35 | 1.88 | 5 |
| stroke 69 | 5 % → 5 % | 4.1 px | 0.35 | 1.00 | 5 |
| stroke 70 | 10 % → 13 % | 7.4 px | 0.35 | 1.28 | 5 |
| stroke 71 | 9 % → 11 % | 7.1 px | 0.35 | 1.15 | 5 |
| stroke 72 | 5 % → 7 % | 4.2 px | 0.35 | 1.23 | 6 |
| stroke 73 | 12 % → 12 % | 9.3 px | 0.35 | 1.00 | 4 |
| stroke 74 | 14 % → 14 % | 10.8 px | 0.35 | 1.00 | 4 |
| stroke 75 | 15 % → 15 % | 11.4 px | 0.35 | 1.00 | 5 |
| stroke 76 | 14 % → 14 % | 10.5 px | 0.35 | 1.00 | 5 |
| stroke 77 | 7 % → 10 % | 5.4 px | 0.35 | 1.34 | 5 |
| stroke 78 | 9 % → 9 % | 7.0 px | 0.35 | 1.00 | 7 |
| stroke 79 | 7 % → 7 % | 5.7 px | 0.35 | 1.00 | 5 |
| stroke 80 | 11 % → 11 % | 8.3 px | 0.35 | 1.00 | 5 |

Numbers say: wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #42 Oil pastel shaggy — own sheet
own sheet 600 × 600 · Pastel · 18 px · 3.1 s

![Brush Artist · Refs · #42 Oil pastel shaggy — own sheet](Brush-Artist-Refs-42-Oil-pastel-shaggy-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 5 % → 27 % | 8.0 px | 0.28 | 5.73 | 14 |
| stroke 2 | 5 % → 24 % | 8.6 px | 0.28 | 4.69 | 12 |
| stroke 3 | 5 % → 29 % | 8.9 px | 0.28 | 5.42 | 11 |
| stroke 4 | 5 % → 11 % | 8.8 px | 0.28 | 2.08 | 10 |
| stroke 5 | 6 % → 11 % | 9.9 px | 0.28 | 1.85 | 11 |
| stroke 6 | 8 % → 37 % | 13.9 px | 0.29 | 4.44 | 10 |
| stroke 7 | 11 % → 31 % | 17.6 px | 0.28 | 2.90 | 10 |
| stroke 8 | 7 % → 38 % | 11.4 px | 0.28 | 5.55 | 11 |
| stroke 9 | 8 % → 21 % | 13.9 px | 0.28 | 2.53 | 10 |
| stroke 10 | 8 % → 18 % | 13.2 px | 0.28 | 2.32 | 10 |
| stroke 11 | 6 % → 27 % | 9.4 px | 0.28 | 4.74 | 10 |
| stroke 12 | 8 % → 19 % | 13.6 px | 0.28 | 2.29 | 10 |
| stroke 13 | 13 % → 24 % | 21.0 px | 0.28 | 1.92 | 12 |
| stroke 14 | 5 % → 23 % | 7.9 px | 0.28 | 4.77 | 17 |
| stroke 15 | 5 % → 24 % | 9.0 px | 0.29 | 4.38 | 14 |
| stroke 16 | 9 % → 21 % | 15.7 px | 0.29 | 2.18 | 29 |
| stroke 17 | 17 % → 39 % | 27.9 px | 0.29 | 2.34 | 14 |
| stroke 18 | 14 % → 25 % | 22.8 px | 0.29 | 1.79 | 12 |
| stroke 19 | 15 % → 32 % | 24.9 px | 0.28 | 2.09 | 14 |
| stroke 20 | 21 % → 39 % | 35.1 px | 0.28 | 1.85 | 10 |
| stroke 21 | 9 % → 16 % | 14.4 px | 0.28 | 1.88 | 17 |
| stroke 22 | 14 % → 17 % | 23.9 px | 0.28 | 1.20 | 15 |
| stroke 23 | 12 % → 17 % | 20.6 px | 0.29 | 1.34 | 10 |
| stroke 24 | 18 % → 26 % | 30.0 px | 0.29 | 1.44 | 12 |
| stroke 25 | 20 % → 34 % | 32.6 px | 0.28 | 1.74 | 12 |
| stroke 26 | 6 % → 14 % | 9.2 px | 0.28 | 2.43 | 14 |
| stroke 27 | 18 % → 26 % | 30.4 px | 0.29 | 1.41 | 10 |
| stroke 28 | 14 % → 24 % | 23.7 px | 0.28 | 1.68 | 12 |
| stroke 29 | 9 % → 27 % | 14.9 px | 0.29 | 3.01 | 14 |
| stroke 30 | 15 % → 36 % | 24.9 px | 0.29 | 2.43 | 12 |
| stroke 31 | 14 % → 17 % | 23.3 px | 0.28 | 1.23 | 13 |
| stroke 32 | 16 % → 29 % | 27.0 px | 0.29 | 1.82 | 10 |
| stroke 33 | 15 % → 16 % | 24.5 px | 0.29 | 1.09 | 11 |
| stroke 34 | 19 % → 27 % | 31.4 px | 0.28 | 1.44 | 11 |
| stroke 35 | 26 % → 36 % | 42.5 px | 0.28 | 1.40 | 11 |
| stroke 36 | 25 % → 34 % | 41.0 px | 0.28 | 1.36 | 11 |
| stroke 37 | 12 % → 12 % | 19.3 px | 0.28 | 1.03 | 12 |
| stroke 38 | 19 % → 25 % | 31.7 px | 0.28 | 1.30 | 11 |
| stroke 39 | 16 % → 22 % | 27.3 px | 0.28 | 1.37 | 14 |
| stroke 40 | 22 % → 31 % | 36.6 px | 0.28 | 1.38 | 11 |
| stroke 41 | 32 % → 36 % | 53.1 px | 0.28 | 1.12 | 12 |
| stroke 42 | 23 % → 30 % | 38.1 px | 0.29 | 1.29 | 12 |
| stroke 43 | 12 % → 12 % | 20.3 px | 0.28 | 1.00 | 14 |
| stroke 44 | 30 % → 37 % | 48.9 px | 0.28 | 1.26 | 11 |
| stroke 45 | 16 % → 16 % | 26.2 px | 0.28 | 1.00 | 16 |
| stroke 46 | 29 % → 34 % | 47.9 px | 0.29 | 1.15 | 10 |
| stroke 47 | 38 % → 41 % | 62.0 px | 0.28 | 1.10 | 10 |
| stroke 48 | 29 % → 36 % | 47.8 px | 0.29 | 1.27 | 15 |
| stroke 49 | 27 % → 30 % | 45.1 px | 0.29 | 1.11 | 16 |
| stroke 50 | 38 % → 40 % | 63.4 px | 0.28 | 1.06 | 10 |
| stroke 51 | 16 % → 16 % | 26.0 px | 0.28 | 1.00 | 22 |
| stroke 52 | 37 % → 38 % | 62.4 px | 0.29 | 1.01 | 13 |
| stroke 53 | 22 % → 26 % | 36.9 px | 0.28 | 1.18 | 14 |
| stroke 54 | 17 % → 19 % | 29.0 px | 0.29 | 1.09 | 18 |
| stroke 55 | 15 % → 15 % | 25.0 px | 0.28 | 1.00 | 21 |
| stroke 56 | 13 % → 14 % | 21.6 px | 0.28 | 1.08 | 13 |
| stroke 57 | 23 % → 23 % | 37.7 px | 0.29 | 1.00 | 13 |
| stroke 58 | 28 % → 29 % | 46.1 px | 0.28 | 1.05 | 10 |
| stroke 59 | 40 % → 40 % | 67.3 px | 0.28 | 1.00 | 14 |
| stroke 60 | 22 % → 22 % | 35.6 px | 0.28 | 1.00 | 16 |

Numbers say: wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #43 Dragged black ink blocks — own sheet
own sheet 600 × 600 · Gouache · 70 px · 9.5 s

![Brush Artist · Refs · #43 Dragged black ink blocks — own sheet](Brush-Artist-Refs-43-Dragged-black-ink-blocks-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 29 % → 29 % | 66.4 px | 0.42 | 1.00 | 429 |
| stroke 2 | 30 % → 31 % | 105.8 px | 0.42 | 1.02 | 419 |
| stroke 3 | 37 % → 36 % | 132.0 px | 0.42 | 0.99 | 406 |
| stroke 4 | 37 % → 34 % | 128.9 px | 0.42 | 0.93 | 414 |
| stroke 5 | 44 % → 30 % | 103.8 px | 0.42 | 0.66 | 513 |

## Brush Artist · Refs · #44 Blue looping ribbon — own sheet
own sheet 600 × 600 · Oil · 80 px · 5.4 s

![Brush Artist · Refs · #44 Blue looping ribbon — own sheet](Brush-Artist-Refs-44-Blue-looping-ribbon-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 32 % → 32 % | 42.2 px | 0.78 | 1.00 | 2425 |

## Brush Artist · Refs · #45 Soft pastel pepper — own sheet
own sheet 600 × 600 · Pastel · 40 px · 5.0 s

![Brush Artist · Refs · #45 Soft pastel pepper — own sheet](Brush-Artist-Refs-45-Soft-pastel-pepper-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 10 % → 40 % | 11.3 px | 0.49 | 3.87 | 325 |
| stroke 2 | 18 % → 34 % | 21.3 px | 0.49 | 1.90 | 322 |
| stroke 3 | 25 % → 38 % | 17.6 px | 0.49 | 1.48 | 294 |
| stroke 4 | 24 % → 36 % | 30.5 px | 0.49 | 1.46 | 332 |
| stroke 5 | 30 % → 30 % | 21.2 px | 0.49 | 1.00 | 237 |
| stroke 6 | 39 % → 46 % | 24.6 px | 0.49 | 1.20 | 314 |
| stroke 7 | 41 % → 45 % | 22.6 px | 0.49 | 1.11 | 435 |
| stroke 8 | 45 % → 45 % | 45.8 px | 0.49 | 1.00 | 371 |

Numbers say: wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #46 Red-brown ink lips — own sheet
own sheet 600 × 600 · Watercolor · 50 px · 5.9 s

![Brush Artist · Refs · #46 Red-brown ink lips — own sheet](Brush-Artist-Refs-46-Red-brown-ink-lips-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 12 % → 23 % | 51.9 px | 0.60 | 1.87 | 120 |
| stroke 2 | 16 % → 26 % | 68.2 px | 0.55 | 1.67 | 82 |

Numbers say: wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #47 Pink knife slabs — own sheet
own sheet 600 × 600 · Heavy acrylic · 90 px · 5.8 s

![Brush Artist · Refs · #47 Pink knife slabs — own sheet](Brush-Artist-Refs-47-Pink-knife-slabs-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 18 % → 36 % | 92.3 px | 0.11 | 1.98 | 60 |
| stroke 2 | 32 % → 48 % | 184.6 px | 0.11 | 1.49 | 52 |
| stroke 3 | 33 % → 48 % | 185.4 px | 0.11 | 1.48 | 60 |
| stroke 4 | 44 % → 43 % | 185.4 px | 0.11 | 0.99 | 64 |

Numbers say: wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #48 Black bands with drips — own sheet
own sheet 600 × 600 · Gouache · 70 px · 10.9 s

![Brush Artist · Refs · #48 Black bands with drips — own sheet](Brush-Artist-Refs-48-Black-bands-with-drips-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 23 % → 36 % | 58.8 px | 0.39 | 1.58 | 559 |
| stroke 2 | 34 % → 47 % | 108.3 px | 0.39 | 1.41 | 532 |
| stroke 3 | 36 % → 48 % | 112.5 px | 0.39 | 1.34 | 430 |
| stroke 4 | 38 % → 36 % | 111.4 px | 0.39 | 0.95 | 434 |

Numbers say: wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #49 Magenta letters round brush — own sheet
own sheet 600 × 600 · Ink · 30 px · 10.4 s

![Brush Artist · Refs · #49 Magenta letters round brush — own sheet](Brush-Artist-Refs-49-Magenta-letters-round-brush-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 27 % → 46 % | 64.3 px | 0.52 | 1.69 | 42 |
| stroke 2 | 29 % → 40 % | 52.5 px | 0.53 | 1.39 | 30 |
| stroke 3 | 41 % → 67 % | 96.4 px | 0.52 | 1.64 | 29 |
| stroke 4 | 34 % → 52 % | 53.7 px | 0.52 | 1.55 | 99 |
| stroke 5 | 40 % → 66 % | 94.7 px | 0.52 | 1.65 | 65 |
| stroke 6 | 54 % → 70 % | 231.1 px | 0.52 | 1.29 | 15 |
| stroke 7 | 41 % → 56 % | 63.9 px | 0.52 | 1.35 | 102 |
| stroke 8 | 36 % → 61 % | 91.9 px | 0.53 | 1.72 | 60 |
| stroke 9 | 49 % → 60 % | 152.9 px | 0.53 | 1.24 | 26 |
| stroke 10 | 42 % → 72 % | 100.4 px | 0.52 | 1.71 | 79 |
| stroke 11 | 52 % → 72 % | 219.5 px | 0.52 | 1.39 | 14 |
| stroke 12 | 53 % → 68 % | 82.2 px | 0.52 | 1.29 | 100 |
| stroke 13 | 42 % → 54 % | 116.0 px | 0.53 | 1.29 | 29 |
| stroke 14 | 45 % → 69 % | 131.9 px | 0.53 | 1.52 | 35 |
| stroke 15 | 43 % → 63 % | 102.4 px | 0.52 | 1.46 | 86 |
| stroke 16 | 52 % → 61 % | 220.2 px | 0.52 | 1.18 | 20 |
| stroke 17 | 53 % → 64 % | 82.2 px | 0.52 | 1.19 | 121 |
| stroke 18 | 36 % → 44 % | 99.6 px | 0.52 | 1.21 | 32 |
| stroke 19 | 54 % → 53 % | 123.8 px | 0.52 | 0.99 | 30 |
| stroke 20 | 54 % → 54 % | 125.3 px | 0.52 | 1.00 | 33 |
| stroke 21 | 49 % → 49 % | 81.3 px | 0.52 | 1.00 | 109 |

Numbers say: wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #50 Thick swipes on photo — own sheet
own sheet 600 × 600 · Heavy acrylic · 40 px · 3.0 s

![Brush Artist · Refs · #50 Thick swipes on photo — own sheet](Brush-Artist-Refs-50-Thick-swipes-on-photo-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 9 % → 21 % | 42.6 px | 0.33 | 2.35 | 49 |
| stroke 2 | 9 % → 16 % | 42.4 px | 0.33 | 1.79 | 29 |
| stroke 3 | 10 % → 11 % | 41.8 px | 0.33 | 1.06 | 39 |
| stroke 4 | 11 % → 18 % | 42.6 px | 0.33 | 1.64 | 33 |
| stroke 5 | 11 % → 10 % | 41.8 px | 0.33 | 0.95 | 32 |
| stroke 6 | 17 % → 21 % | 97.3 px | 0.32 | 1.20 | 24 |
| stroke 7 | 22 % → 26 % | 92.7 px | 0.33 | 1.18 | 37 |
| stroke 8 | 21 % → 21 % | 119.6 px | 0.33 | 0.97 | 29 |
| stroke 9 | 9 % → 10 % | 42.0 px | 0.32 | 1.09 | 35 |
| stroke 10 | 22 % → 21 % | 73.6 px | 0.32 | 0.96 | 37 |
| stroke 11 | 9 % → 8 % | 42.6 px | 0.33 | 0.95 | 30 |
| stroke 12 | 17 % → 16 % | 93.0 px | 0.33 | 0.96 | 21 |

Numbers say: wet paint spreads well beyond the stroke.

## Brush Artist · Ink — dry brush — own sheet
own sheet 600 × 600 · Gouache · 30 px · 3.5 s

![Brush Artist · Ink — dry brush — own sheet](Brush-Artist-Ink-dry-brush-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| ear | 13 % → 4 % | 16.7 px | 0.82 | 0.32 | 683 |
| drag0 | 14 % → 16 % | 25.0 px | 0.82 | 1.22 | 174 |
| drag1 | 17 % → 18 % | 35.3 px | 0.82 | 1.02 | 168 |
| drag2 | 20 % → 18 % | 45.7 px | 0.82 | 0.91 | 126 |
| drag3 | 22 % → 19 % | 56.9 px | 0.82 | 0.84 | 94 |

## Brush Artist · Watercolour — blue — own sheet
own sheet 600 × 600 · Watercolor · 40 px · 10.3 s

![Brush Artist · Watercolour — blue — own sheet](Brush-Artist-Watercolour-blue-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| s0 | 7 % → 23 % | 28.4 px | 0.25 | 3.20 | 42 |
| s1 | 5 % → 32 % | 9.9 px | 0.38 | 5.84 | 39 |
| s2 | 10 % → 18 % | 43.5 px | 0.19 | 1.75 | 50 |
| s3 | 9 % → 17 % | 26.3 px | 0.28 | 1.85 | 72 |
| s4 | 14 % → 29 % | 37.9 px | 0.36 | 2.11 | 80 |
| s5 | 19 % → 29 % | 38.9 px | 0.37 | 1.51 | 50 |
| s6 | 17 % → 21 % | 47.6 px | 0.27 | 1.22 | 50 |
| s7 | 24 % → 35 % | 31.9 px | 0.37 | 1.44 | 41 |
| s8 | 20 % → 23 % | 77.5 px | 0.27 | 1.18 | 53 |

Numbers say: wet paint spreads well beyond the stroke.

## Brush Artist · Charcoal — stick — own sheet
own sheet 600 × 600 · Charcoal · 28 px · 1.1 s

![Brush Artist · Charcoal — stick — own sheet](Brush-Artist-Charcoal-stick-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| finger0 | 9 % → 18 % | 15.5 px | 0.83 | 2.01 | 32 |
| tip0 | 8 % → 14 % | 22.1 px | 0.83 | 1.75 | 8 |
| finger1 | 17 % → 29 % | 29.4 px | 0.83 | 1.74 | 27 |
| tip1 | 15 % → 21 % | 39.1 px | 0.83 | 1.42 | 8 |
| finger2 | 17 % → 25 % | 29.5 px | 0.83 | 1.53 | 26 |
| tip2 | 14 % → 20 % | 39.0 px | 0.83 | 1.41 | 8 |
| finger3 | 16 % → 19 % | 29.3 px | 0.83 | 1.16 | 25 |
| tip3 | 15 % → 15 % | 39.0 px | 0.83 | 1.00 | 8 |
| cig0 | 25 % → 35 % | 54.8 px | 0.83 | 1.41 | 9 |
| cig1 | 26 % → 35 % | 58.8 px | 0.83 | 1.32 | 9 |
| cig2 | 28 % → 35 % | 63.2 px | 0.83 | 1.22 | 9 |
| cig3 | 30 % → 34 % | 67.3 px | 0.83 | 1.14 | 9 |
| cig4 | 32 % → 34 % | 71.5 px | 0.83 | 1.06 | 9 |
| cig5 | 34 % → 34 % | 75.3 px | 0.83 | 1.00 | 9 |

Numbers say: wet paint spreads well beyond the stroke.

