![All brushes](contact.png)

# Brush Lab — 241 brushes · 8 Nov 2026 at 13:45

Every sheet: 1500 × 600, ten strokes in a 5 × 2 grid — 1. light line · 2. heavy line · 3. pressure swell · 4. fast wave · 5. slow wave · 6. spiral · 7. loop · 8. tilted · 9. over the wet one · 10. long, no reload (cell 8 holds «tilted» and «over the wet one» crossed). The CPU reference of Mamay's paint engine; the wet layer settles 20 s at the end.

Columns: **covered** = share of the cell with paint right after the stroke → after settling; **width** = painted area of the stroke ÷ its length (px); **dark** = mean darkness of the painted pixels above the paper's own grain (0 = paper, 1 = black); **spread** = how far wet paint went beyond the stroke (1.0 = stayed); **ms** = the stroke on the CPU; long stroke: paint in each quarter of its length (it should run out: wet → streaks → dry tail).

## Ink Line
Ink · 12 px · 26.9 s

![Ink Line](Ink-Line.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 1 % → 4 % | 4.3 px | 0.55 | 2.45 | 36 |
| heavy line | 5 % → 6 % | 15.7 px | 0.68 | 1.14 | 73 |
| pressure swell | 3 % → 4 % | 11.3 px | 0.64 | 1.40 | 41 |
| fast wave | 10 % → 11 % | 11.2 px | 0.59 | 1.11 | 138 |
| slow wave | 8 % → 10 % | 9.6 px | 0.57 | 1.16 | 145 |
| spiral | 14 % → 15 % | 8.9 px | 0.49 | 1.07 | 249 |
| loop | 8 % → 9 % | 10.6 px | 0.61 | 1.15 | 129 |
| tilted | 5 % → 5 % | 14.3 px | 0.64 | 1.05 | 65 |
| over the wet one | 10 % → 11 % | 12.5 px | 0.64 | 1.15 | 66 |
| long, no reload | 18 % → 17 % | 8.1 px | 0.47 | 0.96 | 355 | quarters: 0.22 → 0.09 → 0.04 → 0.02

Numbers say: light vs heavy: width 4.3 → 15.7 px, dark 0.55 → 0.68; wet paint spreads well beyond the stroke.

## Dense Ink
Ink · 14 px · 27.5 s

![Dense Ink](Dense-Ink.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 5 % → 7 % | 15.2 px | 0.72 | 1.27 | 47 |
| heavy line | 7 % → 7 % | 19.1 px | 0.73 | 1.09 | 77 |
| pressure swell | 5 % → 6 % | 17.9 px | 0.72 | 1.18 | 50 |
| fast wave | 13 % → 13 % | 15.2 px | 0.69 | 1.01 | 161 |
| slow wave | 12 % → 12 % | 13.5 px | 0.67 | 1.04 | 195 |
| spiral | 18 % → 15 % | 12.2 px | 0.65 | 0.80 | 265 |
| loop | 11 % → 12 % | 14.8 px | 0.69 | 1.08 | 118 |
| tilted | 5 % → 6 % | 14.5 px | 0.72 | 1.07 | 66 |
| over the wet one | 12 % → 13 % | 17.7 px | 0.72 | 1.12 | 66 |
| long, no reload | 23 % → 15 % | 10.1 px | 0.64 | 0.66 | 353 | quarters: 0.30 → 0.12 → 0.04 → 0.02

Numbers say: light vs heavy: width 15.2 → 19.1 px, dark 0.72 → 0.73.

## Transparent Wash
Watercolor · 22 px · 28.1 s

![Transparent Wash](Transparent-Wash.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 2 % → 5 % | 6.9 px | 0.27 | 2.26 | 31 |
| heavy line | 7 % → 9 % | 20.4 px | 0.27 | 1.23 | 58 |
| pressure swell | 4 % → 6 % | 15.2 px | 0.28 | 1.54 | 32 |
| fast wave | 14 % → 16 % | 16.1 px | 0.20 | 1.17 | 130 |
| slow wave | 12 % → 15 % | 13.7 px | 0.21 | 1.28 | 214 |
| spiral | 18 % → 22 % | 11.9 px | 0.16 | 1.22 | 224 |
| loop | 11 % → 13 % | 14.5 px | 0.22 | 1.20 | 103 |
| tilted | 8 % → 8 % | 21.1 px | 0.24 | 1.06 | 63 |
| over the wet one | 13 % → 16 % | 16.4 px | 0.24 | 1.19 | 65 |
| long, no reload | 26 % → 32 % | 11.6 px | 0.13 | 1.22 | 329 | quarters: 0.11 → 0.04 → 0.02 → 0.01

Numbers say: light vs heavy: width 6.9 → 20.4 px, dark 0.27 → 0.27; wet paint spreads well beyond the stroke.

## Dry Brush
Gouache · 24 px · 26.0 s

![Dry Brush](Dry-Brush.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 5 % → 1 % | 13.8 px | 0.65 | 0.11 | 62 |
| heavy line | 6 % → 0 % | 18.4 px | 0.65 | 0.02 | 97 |
| pressure swell | 5 % → 0 % | 18.1 px | 0.65 | 0.09 | 51 |
| fast wave | 6 % → 1 % | 6.9 px | 0.65 | 0.08 | 175 |
| slow wave | 7 % → 0 % | 7.8 px | 0.65 | 0.07 | 268 |
| spiral | 7 % → 1 % | 4.4 px | 0.65 | 0.08 | 253 |
| loop | 9 % → 0 % | 12.2 px | 0.65 | 0.05 | 148 |
| tilted | 4 % → 3 % | 10.3 px | 0.65 | 0.89 | 82 |
| over the wet one | 9 % → 1 % | 14.3 px | 0.65 | 0.12 | 78 |
| long, no reload | 6 % → 1 % | 2.7 px | 0.65 | 0.15 | 348 | quarters: 0.12 → 0.00 → 0.00 → 0.00

Numbers say: light vs heavy: width 13.8 → 18.4 px, dark 0.65 → 0.65.

## Wax Crayon
Wax · 8 px · 10.2 s

![Wax Crayon](Wax-Crayon.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 1 % → 1 % | 2.5 px | 0.71 | 1.00 | 27 |
| heavy line | 1 % → 1 % | 3.9 px | 0.69 | 1.00 | 14 |
| pressure swell | 1 % → 1 % | 3.3 px | 0.70 | 1.00 | 15 |
| fast wave | 3 % → 3 % | 3.5 px | 0.69 | 1.00 | 44 |
| slow wave | 3 % → 3 % | 3.4 px | 0.70 | 1.00 | 35 |
| spiral | 5 % → 5 % | 3.3 px | 0.70 | 1.00 | 69 |
| loop | 3 % → 3 % | 3.3 px | 0.70 | 1.00 | 34 |
| tilted | 2 % → 2 % | 5.6 px | 0.68 | 1.00 | 24 |
| over the wet one | 3 % → 3 % | 3.6 px | 0.68 | 1.00 | 22 |
| long, no reload | 7 % → 7 % | 3.3 px | 0.70 | 1.00 | 148 | quarters: 0.06 → 0.06 → 0.06 → 0.06

Numbers say: light vs heavy: width 2.5 → 3.9 px, dark 0.71 → 0.69; the long stroke does not run out of paint.

## Oil Pastel
Wax · 12 px · 10.5 s

![Oil Pastel](Oil-Pastel.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 1 % → 1 % | 4.0 px | 0.68 | 1.00 | 31 |
| heavy line | 2 % → 2 % | 6.5 px | 0.68 | 1.00 | 29 |
| pressure swell | 2 % → 2 % | 5.7 px | 0.69 | 1.00 | 27 |
| fast wave | 5 % → 5 % | 5.7 px | 0.68 | 1.00 | 81 |
| slow wave | 5 % → 5 % | 5.5 px | 0.68 | 1.00 | 67 |
| spiral | 8 % → 8 % | 5.5 px | 0.68 | 1.00 | 132 |
| loop | 4 % → 4 % | 5.6 px | 0.68 | 1.00 | 65 |
| tilted | 2 % → 2 % | 6.8 px | 0.68 | 1.00 | 45 |
| over the wet one | 5 % → 5 % | 5.8 px | 0.68 | 1.00 | 25 |
| long, no reload | 13 % → 13 % | 5.6 px | 0.68 | 1.00 | 233 | quarters: 0.10 → 0.09 → 0.10 → 0.10

Numbers say: light vs heavy: width 4.0 → 6.5 px, dark 0.68 → 0.68; the long stroke does not run out of paint.

## Charcoal
Charcoal · 5 px · 10.3 s

![Charcoal](Charcoal.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 1 % → 1 % | 2.0 px | 0.74 | 1.00 | 21 |
| heavy line | 1 % → 1 % | 3.0 px | 0.74 | 1.00 | 12 |
| pressure swell | 1 % → 1 % | 2.7 px | 0.74 | 1.00 | 9 |
| fast wave | 2 % → 2 % | 2.7 px | 0.73 | 1.00 | 45 |
| slow wave | 2 % → 2 % | 2.6 px | 0.74 | 1.00 | 30 |
| spiral | 4 % → 4 % | 2.5 px | 0.74 | 1.00 | 61 |
| loop | 2 % → 2 % | 2.6 px | 0.74 | 1.00 | 44 |
| tilted | 2 % → 2 % | 4.3 px | 0.72 | 1.00 | 24 |
| over the wet one | 2 % → 2 % | 2.4 px | 0.72 | 1.00 | 9 |
| long, no reload | 6 % → 6 % | 2.7 px | 0.73 | 1.00 | 130 | quarters: 0.05 → 0.05 → 0.05 → 0.05

Numbers say: light vs heavy: width 2.0 → 3.0 px, dark 0.74 → 0.74; the long stroke does not run out of paint.

## Impasto
Heavy acrylic · 22 px · 15.5 s

![Impasto](Impasto.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 8 % → 8 % | 24.1 px | 0.72 | 0.93 | 61 |
| heavy line | 10 % → 9 % | 28.8 px | 0.70 | 0.94 | 100 |
| pressure swell | 7 % → 7 % | 28.1 px | 0.72 | 0.94 | 81 |
| fast wave | 20 % → 13 % | 23.4 px | 0.71 | 0.64 | 176 |
| slow wave | 21 % → 14 % | 24.5 px | 0.71 | 0.66 | 291 |
| spiral | 30 % → 14 % | 19.9 px | 0.71 | 0.46 | 279 |
| loop | 18 % → 14 % | 23.9 px | 0.71 | 0.77 | 170 |
| tilted | 8 % → 8 % | 21.7 px | 0.70 | 1.00 | 90 |
| over the wet one | 17 % → 15 % | 25.4 px | 0.70 | 0.91 | 84 |
| long, no reload | 33 % → 14 % | 14.9 px | 0.71 | 0.42 | 397 | quarters: 0.38 → 0.21 → 0.10 → 0.03

Numbers say: light vs heavy: width 24.1 → 28.8 px, dark 0.72 → 0.70.

## Oil Round
Oil · 18 px · 18.8 s

![Oil Round](Oil-Round.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 2 % → 2 % | 7.2 px | 0.75 | 1.00 | 50 |
| heavy line | 7 % → 7 % | 19.3 px | 0.73 | 1.00 | 83 |
| pressure swell | 4 % → 4 % | 13.7 px | 0.72 | 1.00 | 47 |
| fast wave | 11 % → 11 % | 12.8 px | 0.65 | 1.00 | 165 |
| slow wave | 8 % → 8 % | 9.0 px | 0.57 | 1.00 | 208 |
| spiral | 10 % → 10 % | 6.6 px | 0.50 | 1.00 | 235 |
| loop | 6 % → 6 % | 7.2 px | 0.45 | 1.00 | 151 |
| tilted | 4 % → 4 % | 10.1 px | 0.52 | 1.00 | 75 |
| over the wet one | 6 % → 6 % | 7.6 px | 0.52 | 1.00 | 61 |
| long, no reload | 15 % → 15 % | 6.9 px | 0.42 | 1.00 | 319 | quarters: 0.09 → 0.08 → 0.07 → 0.06

Numbers say: light vs heavy: width 7.2 → 19.3 px, dark 0.75 → 0.73.

## Palette Knife
Oil · 20 px · 18.0 s

![Palette Knife](Palette-Knife.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 8 % → 8 % | 21.9 px | 0.67 | 1.00 | 32 |
| heavy line | 8 % → 8 % | 22.5 px | 0.74 | 1.00 | 19 |
| pressure swell | 6 % → 6 % | 22.3 px | 0.74 | 1.00 | 15 |
| fast wave | 16 % → 16 % | 18.9 px | 0.50 | 1.00 | 28 |
| slow wave | 17 % → 17 % | 19.9 px | 0.43 | 1.00 | 43 |
| spiral | 17 % → 17 % | 11.3 px | 0.46 | 1.00 | 44 |
| loop | 16 % → 16 % | 21.0 px | 0.59 | 1.00 | 31 |
| tilted | 5 % → 5 % | 15.0 px | 0.72 | 1.00 | 29 |
| over the wet one | 13 % → 13 % | 21.0 px | 0.72 | 1.00 | 22 |
| long, no reload | 16 % → 16 % | 7.2 px | 0.49 | 1.00 | 62 | quarters: 0.29 → 0.05 → 0.00 → 0.00

Numbers say: light vs heavy: width 21.9 → 22.5 px, dark 0.67 → 0.74; pressure barely changes the width.

## Water
Watercolor · 20 px · 40.2 s · over bands of wet oil paint and oil pastel in turn (it works on paint already there: look at what it does to the bands; covered counts the bands too)

![Water](Water.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 25 % → 27 % | 73.8 px | 0.80 | 1.06 | 29 |
| heavy line | 24 % → 25 % | 69.8 px | 0.81 | 1.04 | 61 |
| pressure swell | 24 % → 25 % | 89.6 px | 0.81 | 1.03 | 38 |
| fast wave | 24 % → 26 % | 27.7 px | 0.81 | 1.07 | 114 |
| slow wave | 24 % → 25 % | 27.8 px | 0.81 | 1.06 | 153 |
| spiral | 24 % → 26 % | 15.9 px | 0.81 | 1.07 | 176 |
| loop | 24 % → 25 % | 31.1 px | 0.81 | 1.03 | 97 |
| tilted | 24 % → 24 % | 67.0 px | 0.81 | 1.00 | 67 |
| over the wet one | 24 % → 25 % | 0.0 px | 0.81 | 1.06 | 52 |
| long, no reload | 24 % → 26 % | 10.7 px | 0.81 | 1.08 | 308 | quarters: 0.21 → 0.27 → 0.18 → 0.27

Numbers say: light vs heavy: width 73.8 → 69.8 px, dark 0.80 → 0.81; pressure barely changes the width; the long stroke does not run out of paint.

## Blender
Pastel · 16 px · 23.0 s · over bands of wet oil paint and oil pastel in turn (it works on paint already there: look at what it does to the bands; covered counts the bands too)

![Blender](Blender.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 24 % → 24 % | 70.7 px | 0.81 | 1.00 | 25 |
| heavy line | 25 % → 25 % | 72.1 px | 0.80 | 1.00 | 41 |
| pressure swell | 24 % → 24 % | 91.3 px | 0.81 | 1.00 | 18 |
| fast wave | 26 % → 26 % | 30.0 px | 0.79 | 1.00 | 74 |
| slow wave | 26 % → 26 % | 29.9 px | 0.80 | 1.00 | 98 |
| spiral | 28 % → 28 % | 18.7 px | 0.77 | 1.00 | 110 |
| loop | 25 % → 25 % | 33.0 px | 0.80 | 1.00 | 85 |
| tilted | 25 % → 25 % | 70.1 px | 0.79 | 1.00 | 49 |
| over the wet one | 26 % → 26 % | 1.8 px | 0.79 | 1.00 | 31 |
| long, no reload | 30 % → 30 % | 13.7 px | 0.76 | 1.00 | 208 | quarters: 0.20 → 0.28 → 0.23 → 0.30

Numbers say: light vs heavy: width 70.7 → 72.1 px, dark 0.81 → 0.80; pressure barely changes the width; the long stroke does not run out of paint.

## Eraser
Eraser · 16 px · 22.9 s · over bands of wet oil paint and oil pastel in turn (it works on paint already there: look at what it does to the bands; covered counts the bands too)

![Eraser](Eraser.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 24 % → 24 % | 69.6 px | 0.82 | 1.00 | 35 |
| heavy line | 23 % → 23 % | 67.9 px | 0.82 | 1.00 | 34 |
| pressure swell | 23 % → 23 % | 87.3 px | 0.82 | 1.00 | 27 |
| fast wave | 22 % → 22 % | 25.7 px | 0.82 | 1.00 | 88 |
| slow wave | 22 % → 22 % | 25.7 px | 0.82 | 1.00 | 110 |
| spiral | 22 % → 22 % | 14.4 px | 0.82 | 1.00 | 124 |
| loop | 22 % → 22 % | 28.6 px | 0.82 | 1.00 | 73 |
| tilted | 23 % → 23 % | 65.1 px | 0.82 | 1.00 | 45 |
| over the wet one | 23 % → 23 % | 0.0 px | 0.82 | 1.00 | 38 |
| long, no reload | 20 % → 20 % | 8.9 px | 0.82 | 1.00 | 206 | quarters: 0.15 → 0.20 → 0.15 → 0.20

Numbers say: light vs heavy: width 69.6 → 67.9 px, dark 0.82 → 0.82; pressure barely changes the width; the long stroke does not run out of paint.

## Fan
Gouache · 30 px · 32.8 s

![Fan](Fan.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 9 % → 3 % | 25.6 px | 0.63 | 0.37 | 21 |
| heavy line | 11 % → 4 % | 30.9 px | 0.63 | 0.39 | 70 |
| pressure swell | 8 % → 5 % | 31.7 px | 0.63 | 0.55 | 30 |
| fast wave | 17 % → 5 % | 20.2 px | 0.63 | 0.26 | 105 |
| slow wave | 18 % → 5 % | 21.0 px | 0.63 | 0.25 | 193 |
| spiral | 24 % → 5 % | 15.5 px | 0.63 | 0.19 | 186 |
| loop | 17 % → 5 % | 22.7 px | 0.63 | 0.28 | 107 |
| tilted | 5 % → 6 % | 15.0 px | 0.63 | 1.05 | 44 |
| over the wet one | 16 % → 8 % | 29.7 px | 0.63 | 0.49 | 60 |
| long, no reload | 22 % → 5 % | 9.9 px | 0.63 | 0.22 | 293 | quarters: 0.29 → 0.07 → 0.01 → 0.00

Numbers say: light vs heavy: width 25.6 → 30.9 px, dark 0.63 → 0.63.

## Sponge
Gouache · 30 px · 33.1 s

![Sponge](Sponge.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 4 % → 0 % | 11.3 px | 0.62 | 0.12 | 48 |
| heavy line | 12 % → 2 % | 35.4 px | 0.62 | 0.14 | 78 |
| pressure swell | 7 % → 2 % | 27.9 px | 0.62 | 0.28 | 47 |
| fast wave | 20 % → 4 % | 23.2 px | 0.62 | 0.19 | 128 |
| slow wave | 21 % → 4 % | 23.8 px | 0.62 | 0.18 | 278 |
| spiral | 28 % → 4 % | 18.3 px | 0.62 | 0.14 | 220 |
| loop | 18 % → 5 % | 23.0 px | 0.62 | 0.29 | 131 |
| tilted | 7 % → 7 % | 18.2 px | 0.62 | 1.04 | 107 |
| over the wet one | 16 % → 6 % | 27.8 px | 0.62 | 0.37 | 65 |
| long, no reload | 29 % → 5 % | 12.9 px | 0.62 | 0.17 | 364 | quarters: 0.29 → 0.13 → 0.07 → 0.04

Numbers say: light vs heavy: width 11.3 → 35.4 px, dark 0.62 → 0.62.

## Ink — sumi brush
Watercolour 1.00 · 22 px · 33.2 s

![Ink — sumi brush](Ink-sumi-brush.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 8 % → 9 % | 23.9 px | 0.87 | 1.13 | 74 |
| heavy line | 12 % → 13 % | 36.2 px | 0.86 | 1.01 | 76 |
| pressure swell | 10 % → 10 % | 36.1 px | 0.87 | 1.04 | 54 |
| fast wave | 27 % → 27 % | 31.0 px | 0.82 | 1.00 | 180 |
| slow wave | 27 % → 28 % | 31.2 px | 0.82 | 1.02 | 295 |
| spiral | 38 % → 36 % | 25.2 px | 0.75 | 0.95 | 326 |
| loop | 22 % → 23 % | 29.0 px | 0.84 | 1.01 | 177 |
| tilted | 9 % → 9 % | 25.7 px | 0.86 | 1.00 | 92 |
| over the wet one | 20 % → 20 % | 30.0 px | 0.86 | 1.02 | 71 |
| long, no reload | 46 % → 41 % | 20.7 px | 0.70 | 0.90 | 526 | quarters: 0.57 → 0.42 → 0.24 → 0.15

Numbers say: light vs heavy: width 23.9 → 36.2 px, dark 0.87 → 0.86.

## Ink — wash
Watercolour 1.00 · 40 px · 38.0 s

![Ink — wash](Ink-wash.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 13 % → 13 % | 37.3 px | 0.42 | 1.02 | 87 |
| heavy line | 19 % → 19 % | 55.2 px | 0.35 | 1.01 | 113 |
| pressure swell | 13 % → 13 % | 48.2 px | 0.41 | 1.02 | 80 |
| fast wave | 41 % → 42 % | 47.8 px | 0.32 | 1.02 | 270 |
| slow wave | 39 % → 40 % | 45.3 px | 0.42 | 1.02 | 429 |
| spiral | 60 % → 62 % | 39.7 px | 0.33 | 1.02 | 420 |
| loop | 34 % → 34 % | 43.8 px | 0.39 | 1.01 | 198 |
| tilted | 15 % → 15 % | 40.7 px | 0.43 | 1.01 | 120 |
| over the wet one | 30 % → 31 % | 43.4 px | 0.43 | 1.02 | 92 |
| long, no reload | 71 % → 75 % | 32.0 px | 0.31 | 1.05 | 620 | quarters: 0.40 → 0.29 → 0.19 → 0.12

Numbers say: light vs heavy: width 37.3 → 55.2 px, dark 0.42 → 0.35.

## Ink — dry brush
Ink 1.00 · 30 px · 27.9 s

![Ink — dry brush](Ink-dry-brush.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 5 % → 5 % | 14.9 px | 0.82 | 0.88 | 116 |
| heavy line | 7 % → 6 % | 19.4 px | 0.82 | 0.87 | 163 |
| pressure swell | 5 % → 5 % | 18.9 px | 0.81 | 0.96 | 109 |
| fast wave | 12 % → 7 % | 13.4 px | 0.80 | 0.65 | 332 |
| slow wave | 12 % → 8 % | 14.1 px | 0.81 | 0.62 | 521 |
| spiral | 16 % → 8 % | 10.8 px | 0.80 | 0.47 | 428 |
| loop | 11 % → 9 % | 14.5 px | 0.79 | 0.77 | 267 |
| tilted | 5 % → 6 % | 15.0 px | 0.81 | 1.08 | 130 |
| over the wet one | 12 % → 11 % | 18.4 px | 0.81 | 0.94 | 107 |
| long, no reload | 21 % → 10 % | 9.2 px | 0.77 | 0.47 | 652 | quarters: 0.28 → 0.10 → 0.03 → 0.01

Numbers say: light vs heavy: width 14.9 → 19.4 px, dark 0.82 → 0.82.

## Ink — nib
Watercolour 1.00 · 5 px · 26.6 s

![Ink — nib](Ink-nib.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 2 % → 5 % | 5.5 px | 0.89 | 2.46 | 44 |
| heavy line | 2 % → 5 % | 6.4 px | 0.89 | 2.34 | 29 |
| pressure swell | 2 % → 4 % | 6.2 px | 0.89 | 2.53 | 34 |
| fast wave | 5 % → 8 % | 5.9 px | 0.89 | 1.63 | 90 |
| slow wave | 5 % → 8 % | 5.7 px | 0.89 | 1.70 | 83 |
| spiral | 8 % → 11 % | 5.0 px | 0.87 | 1.41 | 132 |
| loop | 4 % → 8 % | 5.7 px | 0.89 | 1.74 | 64 |
| tilted | 4 % → 4 % | 10.3 px | 0.89 | 1.02 | 29 |
| over the wet one | 6 % → 9 % | 6.1 px | 0.89 | 1.61 | 26 |
| long, no reload | 9 % → 12 % | 4.2 px | 0.85 | 1.30 | 203 | quarters: 0.24 → 0.11 → 0.07 → 0.05

Numbers say: light vs heavy: width 5.5 → 6.4 px, dark 0.89 → 0.89; wet paint spreads well beyond the stroke.

## 0.45 · Dry brush
Gouache 0.91 · Ink 0.07 · 34 px · 36.0 s

![0.45 · Dry brush](0-45-Dry-brush.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 8 % → 2 % | 22.9 px | 0.68 | 0.26 | 134 |
| heavy line | 10 % → 5 % | 27.8 px | 0.68 | 0.52 | 168 |
| pressure swell | 7 % → 4 % | 26.5 px | 0.68 | 0.59 | 123 |
| fast wave | 19 % → 6 % | 21.4 px | 0.68 | 0.33 | 353 |
| slow wave | 20 % → 7 % | 23.0 px | 0.68 | 0.38 | 597 |
| spiral | 27 % → 8 % | 17.6 px | 0.68 | 0.29 | 610 |
| loop | 18 % → 9 % | 23.0 px | 0.68 | 0.51 | 299 |
| tilted | 8 % → 8 % | 21.8 px | 0.68 | 1.02 | 150 |
| over the wet one | 17 % → 12 % | 25.0 px | 0.68 | 0.73 | 148 |
| long, no reload | 34 % → 9 % | 15.3 px | 0.68 | 0.28 | 975 | quarters: 0.37 → 0.26 → 0.19 → 0.17

Numbers say: light vs heavy: width 22.9 → 27.8 px, dark 0.68 → 0.68.

## Dry pastel
Pastel 1.00 · 26 px · 12.1 s

![Dry pastel](Dry-pastel.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 3 % → 3 % | 8.2 px | 0.37 | 1.00 | 40 |
| heavy line | 5 % → 5 % | 13.1 px | 0.39 | 1.00 | 37 |
| pressure swell | 3 % → 3 % | 11.5 px | 0.39 | 1.00 | 26 |
| fast wave | 10 % → 10 % | 11.8 px | 0.39 | 1.00 | 118 |
| slow wave | 10 % → 10 % | 11.1 px | 0.39 | 1.00 | 171 |
| spiral | 14 % → 14 % | 9.1 px | 0.38 | 1.00 | 146 |
| loop | 7 % → 7 % | 9.5 px | 0.38 | 1.00 | 105 |
| tilted | 3 % → 3 % | 7.5 px | 0.39 | 1.00 | 60 |
| over the wet one | 6 % → 6 % | 10.6 px | 0.39 | 1.00 | 41 |
| long, no reload | 17 % → 17 % | 7.6 px | 0.38 | 1.00 | 257 | quarters: 0.08 → 0.07 → 0.07 → 0.07

Numbers say: light vs heavy: width 8.2 → 13.1 px, dark 0.37 → 0.39; the long stroke does not run out of paint.

## 0.45 · Charcoal
Charcoal 1.00 · 18 px · 11.7 s

![0.45 · Charcoal](0-45-Charcoal.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 2 % → 2 % | 5.4 px | 0.79 | 1.00 | 14 |
| heavy line | 3 % → 3 % | 8.0 px | 0.79 | 1.00 | 23 |
| pressure swell | 2 % → 2 % | 7.8 px | 0.80 | 1.00 | 13 |
| fast wave | 8 % → 8 % | 8.8 px | 0.80 | 1.00 | 66 |
| slow wave | 6 % → 6 % | 7.3 px | 0.80 | 1.00 | 72 |
| spiral | 10 % → 10 % | 6.7 px | 0.80 | 1.00 | 88 |
| loop | 6 % → 6 % | 8.2 px | 0.80 | 1.00 | 39 |
| tilted | 3 % → 3 % | 7.2 px | 0.79 | 1.00 | 22 |
| over the wet one | 5 % → 5 % | 7.4 px | 0.79 | 1.00 | 25 |
| long, no reload | 17 % → 17 % | 7.8 px | 0.80 | 1.00 | 137 | quarters: 0.15 → 0.16 → 0.16 → 0.16

Numbers say: light vs heavy: width 5.4 → 8.0 px, dark 0.79 → 0.79; the long stroke does not run out of paint.

## Watercolour — wash
Watercolour 1.00 · 50 px · 38.1 s

![Watercolour — wash](Watercolour-wash.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 16 % → 16 % | 45.5 px | 0.22 | 1.01 | 129 |
| heavy line | 22 % → 22 % | 64.9 px | 0.19 | 1.00 | 154 |
| pressure swell | 15 % → 15 % | 56.1 px | 0.22 | 1.01 | 89 |
| fast wave | 48 % → 49 % | 55.5 px | 0.19 | 1.01 | 345 |
| slow wave | 46 % → 46 % | 53.3 px | 0.24 | 1.00 | 541 |
| spiral | 66 % → 66 % | 43.7 px | 0.21 | 1.00 | 556 |
| loop | 40 % → 40 % | 51.4 px | 0.22 | 1.00 | 289 |
| tilted | 18 % → 18 % | 49.7 px | 0.23 | 1.00 | 195 |
| over the wet one | 36 % → 36 % | 49.6 px | 0.23 | 1.01 | 141 |
| long, no reload | 84 % → 84 % | 37.7 px | 0.20 | 1.00 | 902 | quarters: 0.24 → 0.20 → 0.16 → 0.12

Numbers say: light vs heavy: width 45.5 → 64.9 px, dark 0.22 → 0.19.

## Watercolour — wet-in-wet
Watercolour 1.00 · 44 px · 39.2 s

![Watercolour — wet-in-wet](Watercolour-wet-in-wet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 13 % → 21 % | 37.4 px | 0.32 | 1.63 | 97 |
| heavy line | 19 % → 22 % | 54.7 px | 0.34 | 1.17 | 151 |
| pressure swell | 12 % → 17 % | 45.7 px | 0.36 | 1.36 | 84 |
| fast wave | 42 % → 49 % | 48.5 px | 0.33 | 1.16 | 283 |
| slow wave | 40 % → 48 % | 45.7 px | 0.41 | 1.22 | 445 |
| spiral | 63 % → 69 % | 41.3 px | 0.37 | 1.11 | 457 |
| loop | 34 % → 41 % | 44.0 px | 0.37 | 1.21 | 229 |
| tilted | 16 % → 17 % | 44.6 px | 0.36 | 1.05 | 156 |
| over the wet one | 32 % → 40 % | 44.4 px | 0.36 | 1.26 | 113 |
| long, no reload | 79 % → 87 % | 35.3 px | 0.36 | 1.11 | 643 | quarters: 0.40 → 0.37 → 0.33 → 0.26

Numbers say: light vs heavy: width 37.4 → 54.7 px, dark 0.32 → 0.34; wet paint spreads well beyond the stroke.

## Watercolour — glaze
Watercolour 1.00 · 38 px · 34.1 s

![Watercolour — glaze](Watercolour-glaze.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 13 % → 13 % | 36.6 px | 0.07 | 1.02 | 99 |
| heavy line | 19 % → 19 % | 55.4 px | 0.07 | 1.00 | 108 |
| pressure swell | 13 % → 13 % | 47.0 px | 0.07 | 1.02 | 75 |
| fast wave | 39 % → 40 % | 45.6 px | 0.07 | 1.01 | 250 |
| slow wave | 37 % → 37 % | 42.8 px | 0.07 | 1.01 | 390 |
| spiral | 59 % → 60 % | 38.8 px | 0.06 | 1.01 | 430 |
| loop | 33 % → 33 % | 42.6 px | 0.07 | 1.00 | 211 |
| tilted | 14 % → 14 % | 40.1 px | 0.07 | 1.00 | 147 |
| over the wet one | 30 % → 30 % | 42.3 px | 0.07 | 1.01 | 112 |
| long, no reload | 69 % → 70 % | 30.9 px | 0.06 | 1.01 | 627 | quarters: 0.06 → 0.05 → 0.03 → 0.02

Numbers say: light vs heavy: width 36.6 → 55.4 px, dark 0.07 → 0.07.

## Watercolour — granulating
Watercolour 1.00 · 44 px · 35.2 s

![Watercolour — granulating](Watercolour-granulating.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 14 % → 14 % | 41.4 px | 0.35 | 1.01 | 101 |
| heavy line | 21 % → 21 % | 60.4 px | 0.31 | 1.00 | 143 |
| pressure swell | 14 % → 14 % | 52.2 px | 0.34 | 1.01 | 79 |
| fast wave | 45 % → 45 % | 51.7 px | 0.29 | 1.01 | 275 |
| slow wave | 42 % → 42 % | 48.2 px | 0.35 | 1.01 | 474 |
| spiral | 62 % → 63 % | 41.0 px | 0.30 | 1.01 | 522 |
| loop | 37 % → 37 % | 47.6 px | 0.33 | 1.00 | 228 |
| tilted | 16 % → 16 % | 45.5 px | 0.36 | 1.00 | 157 |
| over the wet one | 33 % → 33 % | 46.2 px | 0.36 | 1.01 | 130 |
| long, no reload | 75 % → 76 % | 33.6 px | 0.29 | 1.01 | 696 | quarters: 0.34 → 0.26 → 0.20 → 0.14

Numbers say: light vs heavy: width 41.4 → 60.4 px, dark 0.35 → 0.31.

## Watercolour — dry brush
Watercolour 1.00 · 36 px · 29.5 s

![Watercolour — dry brush](Watercolour-dry-brush.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 10 % → 9 % | 27.8 px | 0.17 | 0.99 | 105 |
| heavy line | 14 % → 12 % | 39.3 px | 0.16 | 0.92 | 141 |
| pressure swell | 11 % → 10 % | 39.6 px | 0.16 | 0.95 | 89 |
| fast wave | 27 % → 20 % | 31.3 px | 0.13 | 0.74 | 334 |
| slow wave | 25 % → 17 % | 28.9 px | 0.14 | 0.70 | 607 |
| spiral | 34 % → 19 % | 22.6 px | 0.13 | 0.56 | 543 |
| loop | 21 % → 18 % | 27.7 px | 0.14 | 0.85 | 279 |
| tilted | 10 % → 10 % | 28.5 px | 0.16 | 1.01 | 156 |
| over the wet one | 21 % → 20 % | 31.0 px | 0.16 | 0.95 | 137 |
| long, no reload | 35 % → 19 % | 15.9 px | 0.14 | 0.54 | 782 | quarters: 0.09 → 0.03 → 0.01 → 0.00

Numbers say: light vs heavy: width 27.8 → 39.3 px, dark 0.17 → 0.16.

## Gouache
Gouache 1.00 · 30 px · 32.1 s

![Gouache](Gouache.png)

A light paint: laid on a grey sheet (on white it cannot be seen); **dark** = how far it is from the grey either way.

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 8 % → 5 % | 23.3 px | 0.29 | 0.61 | 93 |
| heavy line | 12 % → 5 % | 35.6 px | 0.28 | 0.41 | 113 |
| pressure swell | 10 % → 5 % | 36.2 px | 0.28 | 0.49 | 89 |
| fast wave | 22 % → 6 % | 25.0 px | 0.28 | 0.27 | 279 |
| slow wave | 22 % → 7 % | 25.9 px | 0.28 | 0.30 | 451 |
| spiral | 28 % → 7 % | 18.5 px | 0.28 | 0.23 | 419 |
| loop | 18 % → 7 % | 23.7 px | 0.28 | 0.37 | 215 |
| tilted | 9 % → 9 % | 24.0 px | 0.28 | 1.01 | 136 |
| over the wet one | 19 % → 12 % | 28.7 px | 0.28 | 0.62 | 156 |
| long, no reload | 27 % → 8 % | 12.2 px | 0.28 | 0.31 | 547 | quarters: 0.01 → 0.02 → 0.02 → 0.02

Numbers say: light vs heavy: width 23.3 → 35.6 px, dark 0.29 → 0.28; the long stroke does not run out of paint.

## Oil — alla prima
Oil 0.89 · Oil glaze 0.11 · 30 px · 15.3 s

![Oil — alla prima](Oil-alla-prima.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 9 % → 9 % | 27.5 px | 0.49 | 1.00 | 115 |
| heavy line | 10 % → 10 % | 28.7 px | 0.50 | 1.00 | 128 |
| pressure swell | 7 % → 7 % | 27.5 px | 0.50 | 1.00 | 86 |
| fast wave | 22 % → 22 % | 25.5 px | 0.50 | 1.00 | 305 |
| slow wave | 25 % → 25 % | 29.0 px | 0.50 | 1.00 | 507 |
| spiral | 37 % → 37 % | 24.5 px | 0.49 | 1.00 | 452 |
| loop | 21 % → 21 % | 27.5 px | 0.50 | 1.00 | 254 |
| tilted | 10 % → 10 % | 26.8 px | 0.50 | 1.00 | 128 |
| over the wet one | 19 % → 19 % | 27.7 px | 0.50 | 1.00 | 110 |
| long, no reload | 46 % → 46 % | 20.5 px | 0.47 | 1.00 | 699 | quarters: 0.31 → 0.25 → 0.22 → 0.18

Numbers say: light vs heavy: width 27.5 → 28.7 px, dark 0.49 → 0.50; pressure barely changes the width.

## Oil — impasto
Oil heavy 1.00 · 34 px · 16.4 s

![Oil — impasto](Oil-impasto.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 8 % → 8 % | 24.0 px | 0.22 | 1.00 | 139 |
| heavy line | 12 % → 12 % | 35.3 px | 0.22 | 1.00 | 167 |
| pressure swell | 9 % → 9 % | 33.1 px | 0.23 | 1.00 | 96 |
| fast wave | 29 % → 29 % | 33.7 px | 0.22 | 1.00 | 364 |
| slow wave | 30 % → 30 % | 34.6 px | 0.22 | 1.00 | 583 |
| spiral | 47 % → 47 % | 31.3 px | 0.21 | 1.00 | 597 |
| loop | 25 % → 25 % | 32.5 px | 0.22 | 1.00 | 349 |
| tilted | 11 % → 11 % | 31.8 px | 0.24 | 1.00 | 173 |
| over the wet one | 21 % → 21 % | 26.8 px | 0.24 | 1.00 | 129 |
| long, no reload | 54 % → 54 % | 24.4 px | 0.20 | 1.00 | 962 | quarters: 0.16 → 0.14 → 0.11 → 0.09

Numbers say: light vs heavy: width 24.0 → 35.3 px, dark 0.22 → 0.22.

## Oil — glaze
Oil glaze 1.00 · 40 px · 15.8 s

![Oil — glaze](Oil-glaze.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 9 % → 9 % | 27.0 px | 0.50 | 1.00 | 121 |
| heavy line | 13 % → 13 % | 38.3 px | 0.49 | 1.00 | 135 |
| pressure swell | 10 % → 10 % | 36.6 px | 0.50 | 1.00 | 81 |
| fast wave | 29 % → 29 % | 33.5 px | 0.49 | 1.00 | 275 |
| slow wave | 30 % → 30 % | 34.6 px | 0.50 | 1.00 | 497 |
| spiral | 46 % → 46 % | 30.1 px | 0.49 | 1.00 | 445 |
| loop | 24 % → 24 % | 31.4 px | 0.50 | 1.00 | 304 |
| tilted | 11 % → 11 % | 30.4 px | 0.50 | 1.00 | 146 |
| over the wet one | 23 % → 23 % | 32.5 px | 0.50 | 1.00 | 117 |
| long, no reload | 52 % → 52 % | 23.5 px | 0.49 | 1.00 | 664 | quarters: 0.34 → 0.30 → 0.27 → 0.22

Numbers say: light vs heavy: width 27.0 → 38.3 px, dark 0.50 → 0.49.

## Oil — scumble
Oil 1.00 · 36 px · 15.1 s

![Oil — scumble](Oil-scumble.png)

A light paint: laid on a grey sheet (on white it cannot be seen); **dark** = how far it is from the grey either way.

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 5 % → 5 % | 13.1 px | 0.08 | 1.00 | 148 |
| heavy line | 6 % → 6 % | 17.3 px | 0.26 | 1.00 | 132 |
| pressure swell | 7 % → 7 % | 26.1 px | 0.19 | 1.00 | 86 |
| fast wave | 18 % → 18 % | 21.3 px | 0.18 | 1.00 | 396 |
| slow wave | 23 % → 23 % | 26.7 px | 0.17 | 1.00 | 635 |
| spiral | 30 % → 30 % | 20.0 px | 0.15 | 1.00 | 632 |
| loop | 18 % → 18 % | 23.0 px | 0.16 | 1.00 | 289 |
| tilted | 10 % → 10 % | 26.6 px | 0.22 | 1.00 | 162 |
| over the wet one | 16 % → 16 % | 18.6 px | 0.22 | 1.00 | 147 |
| long, no reload | 32 % → 32 % | 14.6 px | 0.13 | 1.00 | 869 | quarters: 0.01 → 0.00 → 0.00 → 0.00

Numbers say: light vs heavy: width 13.1 → 17.3 px, dark 0.08 → 0.26.

## Acrylic — heavy body
Impasto 0.98 · 30 px · 15.0 s

![Acrylic — heavy body](Acrylic-heavy-body.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 9 % → 7 % | 25.4 px | 0.52 | 0.83 | 88 |
| heavy line | 8 % → 7 % | 24.6 px | 0.52 | 0.88 | 111 |
| pressure swell | 8 % → 7 % | 28.6 px | 0.53 | 0.89 | 63 |
| fast wave | 17 % → 13 % | 19.4 px | 0.52 | 0.78 | 242 |
| slow wave | 19 % → 15 % | 21.6 px | 0.52 | 0.79 | 427 |
| spiral | 24 % → 15 % | 15.8 px | 0.52 | 0.61 | 398 |
| loop | 17 % → 13 % | 22.2 px | 0.52 | 0.78 | 160 |
| tilted | 8 % → 8 % | 23.3 px | 0.53 | 0.99 | 120 |
| over the wet one | 18 % → 15 % | 25.6 px | 0.53 | 0.85 | 114 |
| long, no reload | 31 % → 18 % | 14.0 px | 0.52 | 0.58 | 579 | quarters: 0.26 → 0.16 → 0.11 → 0.09

Numbers say: light vs heavy: width 25.4 → 24.6 px, dark 0.52 → 0.52; pressure barely changes the width.

## Acrylic — fluid
Watercolour 1.00 · 36 px · 32.3 s

![Acrylic — fluid](Acrylic-fluid.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 12 % → 12 % | 33.6 px | 0.24 | 1.01 | 83 |
| heavy line | 18 % → 17 % | 50.9 px | 0.21 | 0.99 | 94 |
| pressure swell | 12 % → 12 % | 45.5 px | 0.23 | 1.01 | 70 |
| fast wave | 39 % → 39 % | 45.1 px | 0.19 | 0.99 | 236 |
| slow wave | 35 % → 35 % | 40.9 px | 0.22 | 1.00 | 360 |
| spiral | 55 % → 54 % | 36.4 px | 0.19 | 0.98 | 379 |
| loop | 31 % → 31 % | 40.0 px | 0.21 | 1.00 | 194 |
| tilted | 13 % → 13 % | 36.0 px | 0.24 | 1.00 | 149 |
| over the wet one | 28 % → 28 % | 42.4 px | 0.24 | 1.01 | 98 |
| long, no reload | 61 % → 58 % | 27.4 px | 0.19 | 0.95 | 668 | quarters: 0.20 → 0.14 → 0.09 → 0.06

Numbers say: light vs heavy: width 33.6 → 50.9 px, dark 0.24 → 0.21.

## Acrylic — palette knife
Impasto 1.00 · 42 px · 19.8 s

![Acrylic — palette knife](Acrylic-palette-knife.png)

A light paint: laid on a grey sheet (on white it cannot be seen); **dark** = how far it is from the grey either way.

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 15 % → 15 % | 44.0 px | 0.39 | 0.98 | 34 |
| heavy line | 15 % → 15 % | 44.3 px | 0.40 | 0.98 | 28 |
| pressure swell | 12 % → 12 % | 43.6 px | 0.42 | 0.99 | 18 |
| fast wave | 36 % → 20 % | 42.0 px | 0.37 | 0.55 | 79 |
| slow wave | 37 % → 21 % | 42.7 px | 0.37 | 0.57 | 192 |
| spiral | 47 % → 18 % | 30.7 px | 0.37 | 0.39 | 156 |
| loop | 32 % → 24 % | 41.3 px | 0.36 | 0.77 | 69 |
| tilted | 12 % → 12 % | 33.7 px | 0.39 | 1.00 | 30 |
| over the wet one | 26 % → 25 % | 39.8 px | 0.39 | 0.97 | 35 |
| long, no reload | 53 % → 20 % | 23.7 px | 0.35 | 0.39 | 176 | quarters: 0.00 → 0.00 → 0.00 → 0.01

Numbers say: light vs heavy: width 44.0 → 44.3 px, dark 0.39 → 0.40; pressure barely changes the width; the long stroke does not run out of paint.

## Finger on oil
Oil 1.00 · 30 px · 12.9 s

![Finger on oil](Finger-on-oil.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 6 % → 6 % | 16.8 px | 0.23 | 1.00 | 74 |
| heavy line | 9 % → 9 % | 27.6 px | 0.28 | 1.00 | 76 |
| pressure swell | 7 % → 7 % | 25.3 px | 0.35 | 1.00 | 55 |
| fast wave | 15 % → 15 % | 17.0 px | 0.12 | 1.00 | 135 |
| slow wave | 16 % → 16 % | 18.6 px | 0.24 | 1.00 | 294 |
| spiral | 28 % → 28 % | 18.2 px | 0.24 | 1.00 | 229 |
| loop | 19 % → 19 % | 24.9 px | 0.28 | 1.00 | 131 |
| tilted | 9 % → 9 % | 26.4 px | 0.28 | 1.00 | 83 |
| over the wet one | 16 % → 16 % | 19.6 px | 0.28 | 1.00 | 55 |
| long, no reload | 36 % → 36 % | 15.9 px | 0.22 | 1.00 | 350 | quarters: 0.12 → 0.11 → 0.07 → 0.04

Numbers say: light vs heavy: width 16.8 → 27.6 px, dark 0.23 → 0.28.

## Palette knife — oil
Oil heavy 0.93 · Impasto 0.07 · 44 px · 19.2 s

![Palette knife — oil](Palette-knife-oil.png)

A light paint: laid on a grey sheet (on white it cannot be seen); **dark** = how far it is from the grey either way.

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 16 % → 14 % | 45.7 px | 0.37 | 0.91 | 36 |
| heavy line | 16 % → 16 % | 46.3 px | 0.38 | 0.98 | 33 |
| pressure swell | 12 % → 12 % | 45.2 px | 0.38 | 0.99 | 15 |
| fast wave | 39 % → 35 % | 44.9 px | 0.35 | 0.89 | 79 |
| slow wave | 39 % → 36 % | 45.4 px | 0.35 | 0.92 | 139 |
| spiral | 62 % → 37 % | 40.7 px | 0.35 | 0.60 | 173 |
| loop | 34 % → 31 % | 43.8 px | 0.36 | 0.92 | 67 |
| tilted | 13 % → 13 % | 36.6 px | 0.37 | 1.00 | 32 |
| over the wet one | 28 % → 27 % | 40.8 px | 0.37 | 0.97 | 46 |
| long, no reload | 74 % → 40 % | 33.0 px | 0.34 | 0.54 | 207 | quarters: 0.00 → 0.00 → 0.01 → 0.01

Numbers say: light vs heavy: width 45.7 → 46.3 px, dark 0.37 → 0.38; pressure barely changes the width; the long stroke does not run out of paint.

## 0.45 · Sponge
Watercolour 0.93 · Ink 0.07 · 46 px · 35.4 s

![0.45 · Sponge](0-45-Sponge.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 27 % → 24 % | 77.5 px | 0.13 | 0.91 | 74 |
| heavy line | 32 % → 28 % | 92.0 px | 0.13 | 0.89 | 94 |
| pressure swell | 24 % → 22 % | 90.9 px | 0.13 | 0.91 | 63 |
| fast wave | 60 % → 54 % | 69.8 px | 0.12 | 0.90 | 230 |
| slow wave | 63 % → 59 % | 72.4 px | 0.17 | 0.94 | 372 |
| spiral | 77 % → 74 % | 51.0 px | 0.16 | 0.96 | 345 |
| loop | 54 % → 51 % | 70.4 px | 0.15 | 0.94 | 184 |
| tilted | 17 % → 17 % | 47.9 px | 0.17 | 1.01 | 125 |
| over the wet one | 45 % → 42 % | 76.8 px | 0.17 | 0.93 | 86 |
| long, no reload | 94 % → 90 % | 42.3 px | 0.17 | 0.96 | 515 | quarters: 0.18 → 0.18 → 0.17 → 0.14

Numbers say: light vs heavy: width 77.5 → 92.0 px, dark 0.13 → 0.13.

## 0.45 · Eraser
Watercolour 1.00 · 30 px · 20.7 s · over bands of wet oil paint and oil pastel in turn (it works on paint already there: look at what it does to the bands; covered counts the bands too)

![0.45 · Eraser](0-45-Eraser.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 24 % → 24 % | 69.2 px | 0.82 | 1.00 | 48 |
| heavy line | 23 % → 23 % | 67.4 px | 0.82 | 1.00 | 52 |
| pressure swell | 23 % → 23 % | 86.8 px | 0.82 | 1.00 | 40 |
| fast wave | 21 % → 21 % | 24.7 px | 0.81 | 1.00 | 135 |
| slow wave | 20 % → 20 % | 23.5 px | 0.82 | 1.00 | 213 |
| spiral | 20 % → 20 % | 13.5 px | 0.79 | 1.00 | 218 |
| loop | 21 % → 21 % | 27.8 px | 0.80 | 1.00 | 125 |
| tilted | 23 % → 23 % | 64.8 px | 0.81 | 1.00 | 52 |
| over the wet one | 22 % → 22 % | 0.0 px | 0.81 | 1.00 | 50 |
| long, no reload | 17 % → 17 % | 7.5 px | 0.79 | 1.00 | 303 | quarters: 0.13 → 0.16 → 0.13 → 0.17

Numbers say: light vs heavy: width 69.2 → 67.4 px, dark 0.82 → 0.82; pressure barely changes the width; the long stroke does not run out of paint.

## Lift wet paint
Watercolour 1.00 · 30 px · 20.5 s · over bands of wet oil paint and oil pastel in turn (it works on paint already there: look at what it does to the bands; covered counts the bands too)

![Lift wet paint](Lift-wet-paint.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 24 % → 24 % | 70.1 px | 0.82 | 1.00 | 33 |
| heavy line | 24 % → 24 % | 69.8 px | 0.82 | 1.00 | 42 |
| pressure swell | 24 % → 24 % | 89.6 px | 0.82 | 1.00 | 30 |
| fast wave | 24 % → 24 % | 27.7 px | 0.82 | 1.00 | 147 |
| slow wave | 24 % → 24 % | 27.7 px | 0.82 | 1.00 | 179 |
| spiral | 24 % → 24 % | 15.9 px | 0.82 | 1.00 | 170 |
| loop | 24 % → 24 % | 31.1 px | 0.82 | 1.00 | 89 |
| tilted | 24 % → 24 % | 66.8 px | 0.82 | 1.00 | 67 |
| over the wet one | 24 % → 24 % | 0.0 px | 0.82 | 1.00 | 48 |
| long, no reload | 24 % → 24 % | 10.7 px | 0.82 | 1.00 | 244 | quarters: 0.18 → 0.24 → 0.17 → 0.24

Numbers say: light vs heavy: width 70.1 → 69.8 px, dark 0.82 → 0.82; pressure barely changes the width; the long stroke does not run out of paint.

## Sgraffito
Watercolour 1.00 · 10 px · 21.1 s · over bands of wet oil paint and oil pastel in turn (it works on paint already there: look at what it does to the bands; covered counts the bands too)

![Sgraffito](Sgraffito.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 24 % → 24 % | 69.9 px | 0.81 | 1.00 | 5 |
| heavy line | 24 % → 24 % | 69.8 px | 0.82 | 1.00 | 9 |
| pressure swell | 24 % → 24 % | 89.6 px | 0.82 | 1.00 | 6 |
| fast wave | 24 % → 24 % | 27.7 px | 0.82 | 1.00 | 30 |
| slow wave | 24 % → 24 % | 27.7 px | 0.82 | 1.00 | 24 |
| spiral | 24 % → 24 % | 15.9 px | 0.82 | 1.00 | 56 |
| loop | 24 % → 24 % | 31.1 px | 0.82 | 1.00 | 21 |
| tilted | 24 % → 24 % | 66.9 px | 0.82 | 1.00 | 7 |
| over the wet one | 24 % → 24 % | 0.0 px | 0.82 | 1.00 | 8 |
| long, no reload | 24 % → 24 % | 10.6 px | 0.82 | 1.00 | 68 | quarters: 0.17 → 0.24 → 0.17 → 0.24

Numbers say: light vs heavy: width 69.9 → 69.8 px, dark 0.81 → 0.82; pressure barely changes the width; the long stroke does not run out of paint.

## Brush Artist · Refs · #01 Henry Ward peach cloud
Gouache 1.00 · 44 px · 28.8 s

![Brush Artist · Refs · #01 Henry Ward peach cloud](Brush-Artist-Refs-01-Henry-Ward-peach-cloud.png)

A light paint: laid on a grey sheet (on white it cannot be seen); **dark** = how far it is from the grey either way.

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 5 % → 0 % | 13.4 px | 0.00 | 0.00 | 114 |
| heavy line | 8 % → 0 % | 22.4 px | 0.32 | 0.01 | 124 |
| pressure swell | 7 % → 3 % | 24.8 px | 0.33 | 0.40 | 108 |
| fast wave | 31 % → 3 % | 36.2 px | 0.27 | 0.09 | 391 |
| slow wave | 20 % → 2 % | 23.3 px | 0.32 | 0.10 | 757 |
| spiral | 33 % → 2 % | 21.6 px | 0.35 | 0.07 | 692 |
| loop | 17 % → 0 % | 22.4 px | 0.32 | 0.01 | 314 |
| tilted | 12 % → 11 % | 32.7 px | 0.25 | 0.97 | 212 |
| over the wet one | 16 % → 2 % | 12.9 px | 0.25 | 0.10 | 140 |
| long, no reload | 30 % → 2 % | 13.6 px | 0.32 | 0.08 | 890 | quarters: 0.03 → 0.03 → 0.03 → 0.03

Numbers say: light vs heavy: width 13.4 → 22.4 px, dark 0.00 → 0.32; the long stroke does not run out of paint.

## Brush Artist · Refs · #02 Henry Ward cream strokes
Gouache 1.00 · 46 px · 32.2 s

![Brush Artist · Refs · #02 Henry Ward cream strokes](Brush-Artist-Refs-02-Henry-Ward-cream-strokes.png)

A light paint: laid on a grey sheet (on white it cannot be seen); **dark** = how far it is from the grey either way.

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 5 % → 0 % | 14.3 px | 0.00 | 0.00 | 134 |
| heavy line | 8 % → 2 % | 24.6 px | 0.41 | 0.22 | 156 |
| pressure swell | 7 % → 3 % | 27.7 px | 0.41 | 0.38 | 116 |
| fast wave | 30 % → 4 % | 34.5 px | 0.36 | 0.15 | 397 |
| slow wave | 21 % → 5 % | 24.3 px | 0.39 | 0.21 | 659 |
| spiral | 43 % → 4 % | 28.4 px | 0.40 | 0.10 | 657 |
| loop | 19 % → 1 % | 24.8 px | 0.39 | 0.04 | 340 |
| tilted | 12 % → 12 % | 33.1 px | 0.34 | 0.98 | 210 |
| over the wet one | 17 % → 1 % | 13.0 px | 0.34 | 0.05 | 130 |
| long, no reload | 25 % → 4 % | 11.1 px | 0.41 | 0.17 | 821 | quarters: 0.03 → 0.04 → 0.03 → 0.04

Numbers say: light vs heavy: width 14.3 → 24.6 px, dark 0.00 → 0.41; the long stroke does not run out of paint.

## Brush Artist · Refs · #03 Henry Ward navy contours
Impasto 1.00 · 22 px · 14.2 s

![Brush Artist · Refs · #03 Henry Ward navy contours](Brush-Artist-Refs-03-Henry-Ward-navy-contours.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 7 % → 6 % | 19.4 px | 0.72 | 0.90 | 67 |
| heavy line | 6 % → 6 % | 18.3 px | 0.71 | 0.92 | 91 |
| pressure swell | 5 % → 5 % | 20.1 px | 0.75 | 0.89 | 53 |
| fast wave | 16 % → 11 % | 18.3 px | 0.76 | 0.71 | 224 |
| slow wave | 18 % → 14 % | 20.5 px | 0.72 | 0.78 | 340 |
| spiral | 28 % → 13 % | 18.3 px | 0.68 | 0.47 | 321 |
| loop | 13 % → 11 % | 17.0 px | 0.71 | 0.83 | 165 |
| tilted | 7 % → 7 % | 20.7 px | 0.73 | 0.99 | 96 |
| over the wet one | 15 % → 13 % | 20.4 px | 0.73 | 0.88 | 80 |
| long, no reload | 32 % → 13 % | 14.4 px | 0.71 | 0.41 | 533 | quarters: 0.33 → 0.27 → 0.19 → 0.08

Numbers say: light vs heavy: width 19.4 → 18.3 px, dark 0.72 → 0.71; pressure barely changes the width.

## Brush Artist · Refs · #04 Henry Ward grey cloud
Gouache 1.00 · 50 px · 32.4 s

![Brush Artist · Refs · #04 Henry Ward grey cloud](Brush-Artist-Refs-04-Henry-Ward-grey-cloud.png)

A light paint: laid on a grey sheet (on white it cannot be seen); **dark** = how far it is from the grey either way.

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 5 % → 0 % | 14.6 px | 0.00 | 0.00 | 90 |
| heavy line | 10 % → 2 % | 28.3 px | 0.31 | 0.25 | 139 |
| pressure swell | 7 % → 2 % | 24.5 px | 0.31 | 0.36 | 115 |
| fast wave | 32 % → 4 % | 37.5 px | 0.24 | 0.14 | 448 |
| slow wave | 23 % → 2 % | 26.3 px | 0.33 | 0.10 | 718 |
| spiral | 47 % → 3 % | 30.8 px | 0.37 | 0.06 | 706 |
| loop | 19 % → 0 % | 25.2 px | 0.00 | 0.00 | 344 |
| tilted | 12 % → 12 % | 33.3 px | 0.24 | 0.98 | 252 |
| over the wet one | 17 % → 3 % | 14.1 px | 0.24 | 0.17 | 163 |
| long, no reload | 22 % → 4 % | 9.9 px | 0.34 | 0.17 | 1331 | quarters: 0.03 → 0.04 → 0.04 → 0.04

Numbers say: light vs heavy: width 14.6 → 28.3 px, dark 0.00 → 0.31; the long stroke does not run out of paint.

## Brush Artist · Refs · #05 Henry Ward green in rust loops
Impasto 1.00 · 20 px · 14.9 s

![Brush Artist · Refs · #05 Henry Ward green in rust loops](Brush-Artist-Refs-05-Henry-Ward-green-in-rust-loops.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 6 % → 6 % | 18.5 px | 0.56 | 0.88 | 56 |
| heavy line | 8 % → 7 % | 22.1 px | 0.56 | 0.87 | 85 |
| pressure swell | 4 % → 4 % | 16.1 px | 0.58 | 0.93 | 66 |
| fast wave | 16 % → 10 % | 17.9 px | 0.56 | 0.67 | 181 |
| slow wave | 16 % → 12 % | 19.1 px | 0.56 | 0.74 | 254 |
| spiral | 24 % → 11 % | 16.1 px | 0.53 | 0.46 | 340 |
| loop | 15 % → 12 % | 19.7 px | 0.56 | 0.79 | 149 |
| tilted | 7 % → 7 % | 19.8 px | 0.58 | 0.99 | 106 |
| over the wet one | 14 % → 12 % | 18.1 px | 0.58 | 0.85 | 92 |
| long, no reload | 28 % → 12 % | 12.6 px | 0.55 | 0.41 | 436 | quarters: 0.23 → 0.17 → 0.11 → 0.04

Numbers say: light vs heavy: width 18.5 → 22.1 px, dark 0.56 → 0.56.

## Brush Artist · Refs · #06 Henry Ward scrubbed grey
Gouache 1.00 · 50 px · 32.3 s

![Brush Artist · Refs · #06 Henry Ward scrubbed grey](Brush-Artist-Refs-06-Henry-Ward-scrubbed-grey.png)

A light paint: laid on a grey sheet (on white it cannot be seen); **dark** = how far it is from the grey either way.

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 5 % → 0 % | 14.6 px | 0.00 | 0.00 | 129 |
| heavy line | 10 % → 2 % | 28.3 px | 0.33 | 0.25 | 150 |
| pressure swell | 7 % → 2 % | 24.5 px | 0.33 | 0.36 | 113 |
| fast wave | 32 % → 4 % | 37.5 px | 0.25 | 0.14 | 420 |
| slow wave | 23 % → 2 % | 26.3 px | 0.34 | 0.10 | 784 |
| spiral | 47 % → 3 % | 30.8 px | 0.38 | 0.06 | 895 |
| loop | 19 % → 0 % | 25.2 px | 0.00 | 0.00 | 445 |
| tilted | 12 % → 12 % | 33.3 px | 0.25 | 0.98 | 273 |
| over the wet one | 17 % → 3 % | 14.1 px | 0.25 | 0.17 | 166 |
| long, no reload | 22 % → 4 % | 9.9 px | 0.36 | 0.17 | 1128 | quarters: 0.03 → 0.04 → 0.04 → 0.04

Numbers say: light vs heavy: width 14.6 → 28.3 px, dark 0.00 → 0.33; the long stroke does not run out of paint.

## Brush Artist · Refs · #07 Henry Ward blue L + black zigzag
Impasto 1.00 · 34 px · 17.8 s

![Brush Artist · Refs · #07 Henry Ward blue L + black zigzag](Brush-Artist-Refs-07-Henry-Ward-blue-L-black-zigzag.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 10 % → 9 % | 30.2 px | 0.59 | 0.86 | 109 |
| heavy line | 11 % → 10 % | 30.8 px | 0.59 | 0.93 | 104 |
| pressure swell | 8 % → 8 % | 31.6 px | 0.59 | 0.92 | 83 |
| fast wave | 25 % → 19 % | 28.8 px | 0.60 | 0.77 | 273 |
| slow wave | 26 % → 20 % | 29.7 px | 0.57 | 0.76 | 409 |
| spiral | 44 % → 23 % | 29.1 px | 0.54 | 0.52 | 602 |
| loop | 24 % → 19 % | 30.4 px | 0.57 | 0.80 | 273 |
| tilted | 11 % → 11 % | 29.8 px | 0.61 | 1.00 | 167 |
| over the wet one | 22 % → 20 % | 32.0 px | 0.61 | 0.90 | 150 |
| long, no reload | 50 % → 23 % | 22.5 px | 0.57 | 0.46 | 829 | quarters: 0.36 → 0.31 → 0.21 → 0.10

Numbers say: light vs heavy: width 30.2 → 30.8 px, dark 0.59 → 0.59; pressure barely changes the width.

## Brush Artist · Refs · #08 Henry Ward olive bands
Gouache 1.00 · 34 px · 24.3 s

![Brush Artist · Refs · #08 Henry Ward olive bands](Brush-Artist-Refs-08-Henry-Ward-olive-bands.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 2 % → 0 % | 5.8 px | 0.00 | 0.00 | 61 |
| heavy line | 7 % → 1 % | 19.2 px | 0.61 | 0.15 | 137 |
| pressure swell | 5 % → 1 % | 19.1 px | 0.61 | 0.20 | 81 |
| fast wave | 18 % → 1 % | 21.1 px | 0.59 | 0.04 | 370 |
| slow wave | 16 % → 0 % | 18.3 px | 0.63 | 0.02 | 471 |
| spiral | 27 % → 0 % | 17.5 px | 0.52 | 0.01 | 507 |
| loop | 10 % → 1 % | 13.5 px | 0.61 | 0.12 | 291 |
| tilted | 7 % → 7 % | 20.5 px | 0.65 | 0.92 | 181 |
| over the wet one | 11 % → 1 % | 9.8 px | 0.65 | 0.12 | 139 |
| long, no reload | 23 % → 2 % | 10.4 px | 0.53 | 0.10 | 776 | quarters: 0.21 → 0.11 → 0.12 → 0.08

Numbers say: light vs heavy: width 5.8 → 19.2 px, dark 0.00 → 0.61.

## Brush Artist · Refs · #09 Henry Ward white loops
Gouache 1.00 · 46 px · 34.1 s

![Brush Artist · Refs · #09 Henry Ward white loops](Brush-Artist-Refs-09-Henry-Ward-white-loops.png)

A light paint: laid on a grey sheet (on white it cannot be seen); **dark** = how far it is from the grey either way.

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 5 % → 0 % | 14.3 px | 0.00 | 0.00 | 137 |
| heavy line | 8 % → 2 % | 24.6 px | 0.43 | 0.22 | 150 |
| pressure swell | 7 % → 3 % | 27.7 px | 0.43 | 0.38 | 112 |
| fast wave | 30 % → 4 % | 34.5 px | 0.38 | 0.15 | 511 |
| slow wave | 21 % → 5 % | 24.3 px | 0.40 | 0.21 | 755 |
| spiral | 43 % → 4 % | 28.4 px | 0.41 | 0.10 | 818 |
| loop | 19 % → 1 % | 24.8 px | 0.41 | 0.04 | 438 |
| tilted | 12 % → 12 % | 33.1 px | 0.37 | 0.98 | 346 |
| over the wet one | 17 % → 1 % | 13.0 px | 0.37 | 0.05 | 150 |
| long, no reload | 25 % → 4 % | 11.1 px | 0.41 | 0.17 | 919 | quarters: 0.03 → 0.04 → 0.04 → 0.04

Numbers say: light vs heavy: width 14.3 → 24.6 px, dark 0.00 → 0.43; the long stroke does not run out of paint.

## Brush Artist · Refs · #10 Henry Ward maroon loops
Impasto 1.00 · 30 px · 16.9 s

![Brush Artist · Refs · #10 Henry Ward maroon loops](Brush-Artist-Refs-10-Henry-Ward-maroon-loops.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 10 % → 8 % | 27.9 px | 0.73 | 0.88 | 108 |
| heavy line | 11 % → 10 % | 32.1 px | 0.73 | 0.90 | 111 |
| pressure swell | 8 % → 7 % | 29.7 px | 0.74 | 0.91 | 65 |
| fast wave | 23 % → 17 % | 26.5 px | 0.76 | 0.76 | 300 |
| slow wave | 22 % → 19 % | 25.9 px | 0.72 | 0.85 | 458 |
| spiral | 37 % → 18 % | 24.2 px | 0.72 | 0.50 | 518 |
| loop | 17 % → 15 % | 22.1 px | 0.73 | 0.86 | 245 |
| tilted | 10 % → 10 % | 27.6 px | 0.73 | 1.00 | 151 |
| over the wet one | 19 % → 17 % | 26.8 px | 0.73 | 0.86 | 144 |
| long, no reload | 40 % → 17 % | 18.0 px | 0.71 | 0.43 | 735 | quarters: 0.38 → 0.33 → 0.27 → 0.18

Numbers say: light vs heavy: width 27.9 → 32.1 px, dark 0.73 → 0.73.

## Brush Artist · Refs · #11 Henry Ward purple spun balls
Impasto 1.00 · 36 px · 17.5 s

![Brush Artist · Refs · #11 Henry Ward purple spun balls](Brush-Artist-Refs-11-Henry-Ward-purple-spun-balls.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 11 % → 10 % | 31.5 px | 0.74 | 0.93 | 110 |
| heavy line | 11 % → 10 % | 30.5 px | 0.74 | 0.95 | 154 |
| pressure swell | 10 % → 9 % | 36.4 px | 0.75 | 0.92 | 90 |
| fast wave | 27 % → 21 % | 31.1 px | 0.74 | 0.78 | 346 |
| slow wave | 30 % → 24 % | 34.6 px | 0.73 | 0.82 | 577 |
| spiral | 40 % → 24 % | 26.5 px | 0.70 | 0.59 | 587 |
| loop | 24 % → 21 % | 30.7 px | 0.75 | 0.90 | 298 |
| tilted | 10 % → 10 % | 28.5 px | 0.73 | 1.00 | 147 |
| over the wet one | 22 % → 20 % | 33.9 px | 0.73 | 0.91 | 147 |
| long, no reload | 53 % → 25 % | 23.9 px | 0.74 | 0.46 | 733 | quarters: 0.50 → 0.45 → 0.38 → 0.27

Numbers say: light vs heavy: width 31.5 → 30.5 px, dark 0.74 → 0.74; pressure barely changes the width.

## Brush Artist · Refs · #12 Henry Ward black-olive cage
Gouache 1.00 · 28 px · 24.3 s

![Brush Artist · Refs · #12 Henry Ward black-olive cage](Brush-Artist-Refs-12-Henry-Ward-black-olive-cage.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 2 % → 0 % | 6.3 px | 0.00 | 0.00 | 79 |
| heavy line | 6 % → 1 % | 16.9 px | 0.64 | 0.21 | 128 |
| pressure swell | 5 % → 1 % | 17.2 px | 0.64 | 0.22 | 82 |
| fast wave | 14 % → 0 % | 16.6 px | 0.00 | 0.00 | 257 |
| slow wave | 14 % → 1 % | 15.6 px | 0.64 | 0.07 | 421 |
| spiral | 18 % → 0 % | 11.7 px | 0.63 | 0.02 | 428 |
| loop | 11 % → 1 % | 14.3 px | 0.63 | 0.10 | 207 |
| tilted | 6 % → 6 % | 17.8 px | 0.68 | 0.92 | 102 |
| over the wet one | 10 % → 0 % | 9.7 px | 0.68 | 0.04 | 89 |
| long, no reload | 18 % → 2 % | 8.0 px | 0.59 | 0.12 | 524 | quarters: 0.15 → 0.12 → 0.06 → 0.02

Numbers say: light vs heavy: width 6.3 → 16.9 px, dark 0.00 → 0.64.

## Brush Artist · Refs · #13 Henry Ward blue streaky form
Gouache 1.00 · 50 px · 31.0 s

![Brush Artist · Refs · #13 Henry Ward blue streaky form](Brush-Artist-Refs-13-Henry-Ward-blue-streaky-form.png)

A light paint: laid on a grey sheet (on white it cannot be seen); **dark** = how far it is from the grey either way.

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 5 % → 0 % | 14.6 px | 0.00 | 0.00 | 155 |
| heavy line | 10 % → 2 % | 28.3 px | 0.33 | 0.25 | 179 |
| pressure swell | 7 % → 2 % | 24.5 px | 0.33 | 0.36 | 113 |
| fast wave | 32 % → 4 % | 37.5 px | 0.25 | 0.14 | 479 |
| slow wave | 23 % → 2 % | 26.3 px | 0.34 | 0.10 | 597 |
| spiral | 47 % → 3 % | 30.8 px | 0.38 | 0.06 | 759 |
| loop | 19 % → 0 % | 25.2 px | 0.00 | 0.00 | 293 |
| tilted | 12 % → 12 % | 33.3 px | 0.25 | 0.98 | 241 |
| over the wet one | 17 % → 3 % | 14.1 px | 0.25 | 0.17 | 151 |
| long, no reload | 22 % → 4 % | 9.9 px | 0.35 | 0.17 | 862 | quarters: 0.03 → 0.04 → 0.04 → 0.04

Numbers say: light vs heavy: width 14.6 → 28.3 px, dark 0.00 → 0.33; the long stroke does not run out of paint.

## Brush Artist · Refs · #14 Henry Ward olive totem
Impasto 1.00 · 48 px · 19.4 s

![Brush Artist · Refs · #14 Henry Ward olive totem](Brush-Artist-Refs-14-Henry-Ward-olive-totem.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 15 % → 14 % | 44.4 px | 0.31 | 0.91 | 172 |
| heavy line | 16 % → 15 % | 46.3 px | 0.31 | 0.95 | 157 |
| pressure swell | 12 % → 11 % | 44.0 px | 0.31 | 0.93 | 141 |
| fast wave | 36 % → 28 % | 41.7 px | 0.36 | 0.78 | 409 |
| slow wave | 37 % → 32 % | 42.3 px | 0.30 | 0.87 | 679 |
| spiral | 59 % → 35 % | 38.7 px | 0.28 | 0.59 | 669 |
| loop | 30 % → 27 % | 39.1 px | 0.29 | 0.89 | 314 |
| tilted | 13 % → 13 % | 36.4 px | 0.33 | 1.00 | 205 |
| over the wet one | 28 % → 25 % | 40.5 px | 0.33 | 0.92 | 182 |
| long, no reload | 61 % → 31 % | 27.3 px | 0.27 | 0.52 | 899 | quarters: 0.20 → 0.15 → 0.09 → 0.04

Numbers say: light vs heavy: width 44.4 → 46.3 px, dark 0.31 → 0.31; pressure barely changes the width.

## Brush Artist · Refs · #15 Ultramarine brush script
Ink 1.00 · 4 px · 23.4 s

![Brush Artist · Refs · #15 Ultramarine brush script](Brush-Artist-Refs-15-Ultramarine-brush-script.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 1 % → 3 % | 2.1 px | 0.55 | 3.99 | 28 |
| heavy line | 5 % → 5 % | 15.6 px | 0.62 | 1.00 | 34 |
| pressure swell | 3 % → 4 % | 11.0 px | 0.62 | 1.21 | 29 |
| fast wave | 9 % → 7 % | 10.2 px | 0.54 | 0.81 | 95 |
| slow wave | 8 % → 7 % | 8.8 px | 0.53 | 0.89 | 92 |
| spiral | 11 % → 8 % | 7.3 px | 0.53 | 0.68 | 148 |
| loop | 7 % → 7 % | 9.4 px | 0.54 | 0.96 | 81 |
| tilted | 3 % → 3 % | 7.4 px | 0.64 | 1.04 | 36 |
| over the wet one | 7 % → 7 % | 10.7 px | 0.64 | 1.08 | 41 |
| long, no reload | 16 % → 7 % | 7.1 px | 0.51 | 0.47 | 232 | quarters: 0.14 → 0.04 → 0.01 → 0.00

Numbers say: light vs heavy: width 2.1 → 15.6 px, dark 0.55 → 0.62; wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #18 Blue oil-stick scribbles
Pastel 1.00 · 10 px · 10.5 s

![Brush Artist · Refs · #18 Blue oil-stick scribbles](Brush-Artist-Refs-18-Blue-oil-stick-scribbles.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 1 % → 1 % | 2.9 px | 0.53 | 1.00 | 19 |
| heavy line | 2 % → 2 % | 6.0 px | 0.53 | 1.00 | 33 |
| pressure swell | 1 % → 1 % | 5.5 px | 0.52 | 1.00 | 17 |
| fast wave | 5 % → 5 % | 5.3 px | 0.53 | 1.00 | 61 |
| slow wave | 4 % → 4 % | 5.2 px | 0.53 | 1.00 | 57 |
| spiral | 7 % → 7 % | 4.4 px | 0.52 | 1.00 | 84 |
| loop | 4 % → 4 % | 4.6 px | 0.52 | 1.00 | 78 |
| tilted | 2 % → 2 % | 4.4 px | 0.53 | 1.00 | 39 |
| over the wet one | 3 % → 3 % | 4.8 px | 0.53 | 1.00 | 28 |
| long, no reload | 9 % → 9 % | 4.2 px | 0.52 | 1.00 | 157 | quarters: 0.05 → 0.05 → 0.06 → 0.06

Numbers say: light vs heavy: width 2.9 → 6.0 px, dark 0.53 → 0.53; the long stroke does not run out of paint.

## Brush Artist · Refs · #20 Orange-red crayon scribble
Pastel 1.00 · 14 px · 10.7 s

![Brush Artist · Refs · #20 Orange-red crayon scribble](Brush-Artist-Refs-20-Orange-red-crayon-scribble.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 1 % → 1 % | 3.8 px | 0.53 | 1.00 | 19 |
| heavy line | 3 % → 3 % | 8.0 px | 0.53 | 1.00 | 23 |
| pressure swell | 2 % → 2 % | 7.6 px | 0.55 | 1.00 | 18 |
| fast wave | 6 % → 6 % | 7.3 px | 0.56 | 1.00 | 131 |
| slow wave | 6 % → 6 % | 6.9 px | 0.53 | 1.00 | 71 |
| spiral | 9 % → 9 % | 6.0 px | 0.54 | 1.00 | 117 |
| loop | 5 % → 5 % | 6.1 px | 0.54 | 1.00 | 51 |
| tilted | 2 % → 2 % | 5.6 px | 0.55 | 1.00 | 26 |
| over the wet one | 4 % → 4 % | 6.2 px | 0.55 | 1.00 | 22 |
| long, no reload | 12 % → 12 % | 5.4 px | 0.53 | 1.00 | 159 | quarters: 0.07 → 0.07 → 0.07 → 0.07

Numbers say: light vs heavy: width 3.8 → 8.0 px, dark 0.53 → 0.53; the long stroke does not run out of paint.

## Brush Artist · Refs · #21 Gritty black contours
Gouache 1.00 · 12 px · 19.3 s

![Brush Artist · Refs · #21 Gritty black contours](Brush-Artist-Refs-21-Gritty-black-contours.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 1 % → 0 % | 3.2 px | 0.00 | 0.00 | 56 |
| heavy line | 2 % → 0 % | 6.0 px | 0.00 | 0.00 | 115 |
| pressure swell | 1 % → 0 % | 5.6 px | 0.00 | 0.00 | 84 |
| fast wave | 4 % → 0 % | 4.9 px | 0.00 | 0.00 | 188 |
| slow wave | 4 % → 0 % | 5.1 px | 0.81 | 0.01 | 193 |
| spiral | 7 % → 0 % | 4.6 px | 0.75 | 0.03 | 341 |
| loop | 4 % → 0 % | 5.5 px | 0.80 | 0.09 | 181 |
| tilted | 3 % → 2 % | 7.7 px | 0.66 | 0.84 | 107 |
| over the wet one | 3 % → 0 % | 2.1 px | 0.66 | 0.01 | 78 |
| long, no reload | 5 % → 0 % | 2.2 px | 0.76 | 0.00 | 504 | quarters: 0.07 → 0.03 → 0.03 → 0.02

Numbers say: light vs heavy: width 3.2 → 6.0 px, dark 0.00 → 0.00.

## Brush Artist · Refs · #22 Bold black brush poster
Ink 1.00 · 20 px · 27.3 s

![Brush Artist · Refs · #22 Bold black brush poster](Brush-Artist-Refs-22-Bold-black-brush-poster.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 4 % → 5 % | 10.3 px | 0.79 | 1.52 | 27 |
| heavy line | 15 % → 14 % | 42.6 px | 0.88 | 0.99 | 97 |
| pressure swell | 9 % → 9 % | 33.6 px | 0.87 | 1.03 | 42 |
| fast wave | 28 % → 27 % | 32.3 px | 0.88 | 0.98 | 153 |
| slow wave | 23 % → 23 % | 27.0 px | 0.87 | 0.98 | 201 |
| spiral | 35 % → 32 % | 23.0 px | 0.87 | 0.92 | 274 |
| loop | 22 % → 22 % | 28.2 px | 0.88 | 1.00 | 125 |
| tilted | 9 % → 9 % | 24.2 px | 0.88 | 1.00 | 85 |
| over the wet one | 20 % → 20 % | 30.8 px | 0.88 | 1.00 | 63 |
| long, no reload | 48 % → 38 % | 21.3 px | 0.85 | 0.79 | 393 | quarters: 0.56 → 0.45 → 0.35 → 0.26

Numbers say: light vs heavy: width 10.3 → 42.6 px, dark 0.79 → 0.88; wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #23 Dry white on orange + black line
Gouache 1.00 · 50 px · 23.0 s

![Brush Artist · Refs · #23 Dry white on orange + black line](Brush-Artist-Refs-23-Dry-white-on-orange-black-line.png)

A light paint: laid on a grey sheet (on white it cannot be seen); **dark** = how far it is from the grey either way.

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 3 % → 0 % | 9.9 px | 0.00 | 0.00 | 75 |
| heavy line | 9 % → 2 % | 26.8 px | 0.42 | 0.20 | 189 |
| pressure swell | 7 % → 0 % | 24.9 px | 0.41 | 0.03 | 136 |
| fast wave | 25 % → 0 % | 28.6 px | 0.00 | 0.00 | 391 |
| slow wave | 24 % → 1 % | 27.6 px | 0.40 | 0.02 | 647 |
| spiral | 33 % → 1 % | 21.5 px | 0.40 | 0.02 | 587 |
| loop | 20 % → 0 % | 26.0 px | 0.39 | 0.00 | 311 |
| tilted | 10 % → 9 % | 28.2 px | 0.38 | 0.93 | 205 |
| over the wet one | 15 % → 1 % | 13.1 px | 0.38 | 0.05 | 185 |
| long, no reload | 30 % → 4 % | 13.5 px | 0.40 | 0.12 | 815 | quarters: 0.02 → 0.03 → 0.03 → 0.03

Numbers say: light vs heavy: width 9.9 → 26.8 px, dark 0.00 → 0.42; the long stroke does not run out of paint.

## Brush Artist · Refs · #24 Picasso flat oil
Oil 0.89 · Oil glaze 0.11 · 34 px · 15.0 s

![Brush Artist · Refs · #24 Picasso flat oil](Brush-Artist-Refs-24-Picasso-flat-oil.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 10 % → 10 % | 28.8 px | 0.39 | 1.00 | 125 |
| heavy line | 11 % → 11 % | 32.5 px | 0.39 | 1.00 | 163 |
| pressure swell | 8 % → 8 % | 31.7 px | 0.38 | 1.00 | 89 |
| fast wave | 30 % → 30 % | 35.2 px | 0.39 | 1.00 | 379 |
| slow wave | 28 % → 28 % | 32.8 px | 0.38 | 1.00 | 651 |
| spiral | 42 % → 42 % | 27.8 px | 0.38 | 1.00 | 592 |
| loop | 22 % → 22 % | 28.8 px | 0.40 | 1.00 | 333 |
| tilted | 11 % → 11 % | 31.3 px | 0.41 | 1.00 | 280 |
| over the wet one | 20 % → 20 % | 25.3 px | 0.41 | 1.00 | 150 |
| long, no reload | 58 % → 58 % | 26.0 px | 0.32 | 1.00 | 896 | quarters: 0.23 → 0.22 → 0.19 → 0.17

Numbers say: light vs heavy: width 28.8 → 32.5 px, dark 0.39 → 0.39.

## Brush Artist · Refs · #25 Yellow heavy flat stroke
Impasto 1.00 · 110 px · 35.2 s

![Brush Artist · Refs · #25 Yellow heavy flat stroke](Brush-Artist-Refs-25-Yellow-heavy-flat-stroke.png)

A light paint: laid on a grey sheet (on white it cannot be seen); **dark** = how far it is from the grey either way.

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 35 % → 35 % | 101.0 px | 0.31 | 1.00 | 440 |
| heavy line | 36 % → 35 % | 104.1 px | 0.31 | 0.97 | 465 |
| pressure swell | 28 % → 29 % | 104.0 px | 0.28 | 1.05 | 333 |
| fast wave | 72 % → 75 % | 82.8 px | 0.25 | 1.04 | 1520 |
| slow wave | 72 % → 71 % | 83.7 px | 0.30 | 0.98 | 2135 |
| spiral | 86 % → 81 % | 56.5 px | 0.30 | 0.94 | 2072 |
| loop | 64 % → 63 % | 82.7 px | 0.31 | 0.99 | 947 |
| tilted | 25 % → 25 % | 70.3 px | 0.28 | 1.00 | 581 |
| over the wet one | 55 % → 53 % | 83.3 px | 0.28 | 0.97 | 457 |
| long, no reload | 98 % → 96 % | 43.9 px | 0.31 | 0.98 | 2846 | quarters: 0.00 → 0.00 → 0.00 → 0.00

Numbers say: light vs heavy: width 101.0 → 104.1 px, dark 0.31 → 0.31; pressure barely changes the width; the long stroke does not run out of paint.

## Brush Artist · Refs · #27 Orange impasto swatch
Impasto 1.00 · 60 px · 22.6 s

![Brush Artist · Refs · #27 Orange impasto swatch](Brush-Artist-Refs-27-Orange-impasto-swatch.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 18 % → 18 % | 52.9 px | 0.34 | 0.97 | 219 |
| heavy line | 21 % → 20 % | 60.0 px | 0.34 | 0.95 | 178 |
| pressure swell | 15 % → 15 % | 57.8 px | 0.36 | 0.97 | 284 |
| fast wave | 48 % → 46 % | 55.2 px | 0.37 | 0.97 | 699 |
| slow wave | 46 % → 45 % | 53.6 px | 0.33 | 0.97 | 910 |
| spiral | 68 % → 61 % | 45.1 px | 0.34 | 0.89 | 840 |
| loop | 40 % → 39 % | 51.8 px | 0.33 | 0.97 | 443 |
| tilted | 16 % → 16 % | 43.7 px | 0.35 | 1.00 | 268 |
| over the wet one | 34 % → 32 % | 50.0 px | 0.35 | 0.97 | 234 |
| long, no reload | 84 % → 76 % | 37.8 px | 0.32 | 0.90 | 1307 | quarters: 0.30 → 0.29 → 0.28 → 0.25

Numbers say: light vs heavy: width 52.9 → 60.0 px, dark 0.34 → 0.34.

## Brush Artist · Refs · #28 Miles Davis black lines
Ink 1.00 · 22 px · 27.5 s

![Brush Artist · Refs · #28 Miles Davis black lines](Brush-Artist-Refs-28-Miles-Davis-black-lines.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 4 % → 6 % | 12.3 px | 0.80 | 1.40 | 32 |
| heavy line | 16 % → 16 % | 45.9 px | 0.88 | 0.99 | 176 |
| pressure swell | 10 % → 10 % | 36.7 px | 0.87 | 1.03 | 41 |
| fast wave | 29 % → 29 % | 33.8 px | 0.88 | 0.99 | 146 |
| slow wave | 27 % → 26 % | 30.7 px | 0.88 | 0.99 | 238 |
| spiral | 39 % → 36 % | 25.4 px | 0.87 | 0.93 | 228 |
| loop | 24 % → 24 % | 31.0 px | 0.88 | 1.00 | 139 |
| tilted | 9 % → 9 % | 26.0 px | 0.88 | 1.01 | 65 |
| over the wet one | 21 % → 21 % | 32.9 px | 0.88 | 1.00 | 66 |
| long, no reload | 53 % → 45 % | 23.9 px | 0.85 | 0.83 | 348 | quarters: 0.61 → 0.53 → 0.41 → 0.31

Numbers say: light vs heavy: width 12.3 → 45.9 px, dark 0.80 → 0.88.

## Brush Artist · Refs · #29 Shrigley magenta asterisk
Watercolour 1.00 · 70 px · 30.6 s

![Brush Artist · Refs · #29 Shrigley magenta asterisk](Brush-Artist-Refs-29-Shrigley-magenta-asterisk.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 10 % → 13 % | 28.0 px | 0.61 | 1.39 | 59 |
| heavy line | 17 % → 18 % | 50.3 px | 0.61 | 1.04 | 223 |
| pressure swell | 11 % → 13 % | 41.1 px | 0.62 | 1.14 | 80 |
| fast wave | 38 % → 38 % | 43.8 px | 0.60 | 1.01 | 290 |
| slow wave | 35 % → 39 % | 41.0 px | 0.62 | 1.11 | 529 |
| spiral | 61 % → 61 % | 40.0 px | 0.60 | 1.01 | 439 |
| loop | 31 % → 32 % | 40.2 px | 0.61 | 1.03 | 244 |
| tilted | 18 % → 18 % | 49.0 px | 0.61 | 1.00 | 186 |
| over the wet one | 31 % → 34 % | 38.5 px | 0.61 | 1.08 | 99 |
| long, no reload | 75 % → 76 % | 33.6 px | 0.60 | 1.01 | 707 | quarters: 0.53 → 0.50 → 0.48 → 0.45

Numbers say: light vs heavy: width 28.0 → 50.3 px, dark 0.61 → 0.61; the long stroke does not run out of paint.

## Brush Artist · Refs · #30 Red gouache face patch
Gouache 1.00 · 60 px · 38.6 s

![Brush Artist · Refs · #30 Red gouache face patch](Brush-Artist-Refs-30-Red-gouache-face-patch.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 16 % → 14 % | 45.5 px | 0.49 | 0.87 | 188 |
| heavy line | 25 % → 19 % | 71.4 px | 0.49 | 0.78 | 244 |
| pressure swell | 20 % → 17 % | 74.8 px | 0.50 | 0.84 | 144 |
| fast wave | 48 % → 28 % | 55.1 px | 0.51 | 0.58 | 486 |
| slow wave | 50 % → 31 % | 57.3 px | 0.48 | 0.62 | 712 |
| spiral | 59 % → 30 % | 39.0 px | 0.48 | 0.50 | 784 |
| loop | 40 % → 28 % | 51.4 px | 0.48 | 0.71 | 402 |
| tilted | 17 % → 17 % | 46.7 px | 0.50 | 1.00 | 262 |
| over the wet one | 37 % → 32 % | 55.9 px | 0.50 | 0.87 | 202 |
| long, no reload | 66 % → 28 % | 29.6 px | 0.46 | 0.42 | 1388 | quarters: 0.40 → 0.36 → 0.31 → 0.26

Numbers say: light vs heavy: width 45.5 → 71.4 px, dark 0.49 → 0.49.

## Brush Artist · Refs · #31 Warhol blotted line
Ink 1.00 · 6 px · 21.2 s

![Brush Artist · Refs · #31 Warhol blotted line](Brush-Artist-Refs-31-Warhol-blotted-line.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 1 % → 4 % | 3.0 px | 0.72 | 3.49 | 27 |
| heavy line | 7 % → 7 % | 19.5 px | 0.84 | 0.98 | 51 |
| pressure swell | 4 % → 4 % | 14.2 px | 0.82 | 1.18 | 31 |
| fast wave | 12 % → 9 % | 13.6 px | 0.81 | 0.73 | 90 |
| slow wave | 11 % → 9 % | 12.3 px | 0.80 | 0.80 | 93 |
| spiral | 15 % → 9 % | 10.0 px | 0.79 | 0.58 | 161 |
| loop | 10 % → 9 % | 12.6 px | 0.80 | 0.94 | 84 |
| tilted | 4 % → 4 % | 11.0 px | 0.83 | 1.03 | 40 |
| over the wet one | 9 % → 9 % | 14.0 px | 0.83 | 1.05 | 39 |
| long, no reload | 21 % → 10 % | 9.5 px | 0.78 | 0.45 | 267 | quarters: 0.25 → 0.13 → 0.05 → 0.01

Numbers say: light vs heavy: width 3.0 → 19.5 px, dark 0.72 → 0.84; wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #32 Thick orange swipes
Impasto 1.00 · 90 px · 30.7 s

![Brush Artist · Refs · #32 Thick orange swipes](Brush-Artist-Refs-32-Thick-orange-swipes.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 29 % → 28 % | 83.5 px | 0.37 | 0.99 | 302 |
| heavy line | 30 % → 29 % | 86.8 px | 0.37 | 0.97 | 304 |
| pressure swell | 23 % → 23 % | 84.8 px | 0.38 | 1.01 | 241 |
| fast wave | 64 % → 65 % | 74.2 px | 0.39 | 1.02 | 842 |
| slow wave | 64 % → 62 % | 73.9 px | 0.37 | 0.97 | 1407 |
| spiral | 80 % → 75 % | 52.6 px | 0.35 | 0.94 | 1678 |
| loop | 56 % → 55 % | 73.0 px | 0.36 | 0.97 | 842 |
| tilted | 21 % → 21 % | 58.8 px | 0.38 | 1.00 | 513 |
| over the wet one | 46 % → 45 % | 70.6 px | 0.38 | 0.96 | 400 |
| long, no reload | 95 % → 92 % | 42.8 px | 0.36 | 0.97 | 2519 | quarters: 0.35 → 0.35 → 0.35 → 0.34

Numbers say: light vs heavy: width 83.5 → 86.8 px, dark 0.37 → 0.37; pressure barely changes the width; the long stroke does not run out of paint.

## Brush Artist · Refs · #33 Red wet-in-wet band
Watercolour 1.00 · 80 px · 46.3 s

![Brush Artist · Refs · #33 Red wet-in-wet band](Brush-Artist-Refs-33-Red-wet-in-wet-band.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 24 % → 42 % | 69.3 px | 0.54 | 1.75 | 144 |
| heavy line | 33 % → 48 % | 96.9 px | 0.55 | 1.45 | 235 |
| pressure swell | 19 % → 30 % | 72.1 px | 0.57 | 1.56 | 134 |
| fast wave | 65 % → 79 % | 75.5 px | 0.60 | 1.21 | 469 |
| slow wave | 61 % → 78 % | 70.5 px | 0.63 | 1.28 | 813 |
| spiral | 77 % → 89 % | 50.8 px | 0.64 | 1.15 | 938 |
| loop | 54 % → 67 % | 70.5 px | 0.62 | 1.23 | 461 |
| tilted | 28 % → 30 % | 78.0 px | 0.58 | 1.09 | 334 |
| over the wet one | 55 % → 79 % | 76.7 px | 0.58 | 1.43 | 212 |
| long, no reload | 96 % → 99 % | 42.9 px | 0.66 | 1.04 | 1369 | quarters: 0.68 → 0.68 → 0.68 → 0.64

Numbers say: light vs heavy: width 69.3 → 96.9 px, dark 0.54 → 0.55; the long stroke does not run out of paint; wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #34 Magenta oil patches
Oil 0.89 · Oil glaze 0.11 · 60 px · 18.2 s

![Brush Artist · Refs · #34 Magenta oil patches](Brush-Artist-Refs-34-Magenta-oil-patches.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 18 % → 18 % | 51.4 px | 0.61 | 1.00 | 225 |
| heavy line | 19 % → 19 % | 55.1 px | 0.61 | 1.00 | 244 |
| pressure swell | 15 % → 15 % | 54.6 px | 0.61 | 1.01 | 176 |
| fast wave | 44 % → 45 % | 51.1 px | 0.61 | 1.02 | 655 |
| slow wave | 45 % → 45 % | 52.4 px | 0.61 | 1.00 | 1089 |
| spiral | 68 % → 68 % | 44.9 px | 0.58 | 1.00 | 1101 |
| loop | 42 % → 42 % | 54.2 px | 0.61 | 1.00 | 569 |
| tilted | 17 % → 17 % | 46.3 px | 0.61 | 1.00 | 341 |
| over the wet one | 34 % → 34 % | 48.4 px | 0.61 | 1.00 | 260 |
| long, no reload | 83 % → 83 % | 37.1 px | 0.59 | 1.00 | 1587 | quarters: 0.54 → 0.54 → 0.53 → 0.47

Numbers say: light vs heavy: width 51.4 → 55.1 px, dark 0.61 → 0.61; pressure barely changes the width; the long stroke does not run out of paint.

## Brush Artist · Refs · #35 Red band with runs
Watercolour 1.00 · 70 px · 47.6 s

![Brush Artist · Refs · #35 Red band with runs](Brush-Artist-Refs-35-Red-band-with-runs.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 40 % → 45 % | 115.3 px | 0.42 | 1.14 | 173 |
| heavy line | 45 % → 50 % | 132.0 px | 0.42 | 1.09 | 265 |
| pressure swell | 20 % → 28 % | 76.7 px | 0.48 | 1.37 | 164 |
| fast wave | 66 % → 76 % | 76.8 px | 0.49 | 1.14 | 532 |
| slow wave | 65 % → 76 % | 75.6 px | 0.52 | 1.16 | 1019 |
| spiral | 86 % → 94 % | 56.9 px | 0.53 | 1.09 | 754 |
| loop | 79 % → 88 % | 102.7 px | 0.49 | 1.11 | 356 |
| tilted | 50 % → 51 % | 139.1 px | 0.47 | 1.02 | 221 |
| over the wet one | 78 % → 84 % | 77.5 px | 0.47 | 1.09 | 182 |
| long, no reload | 96 % → 100 % | 43.2 px | 0.58 | 1.04 | 1086 | quarters: 0.59 → 0.60 → 0.59 → 0.56

Numbers say: light vs heavy: width 115.3 → 132.0 px, dark 0.42 → 0.42; the long stroke does not run out of paint.

## Brush Artist · Refs · #36 Magenta letters flat brush
Gouache 1.00 · 36 px · 32.0 s

![Brush Artist · Refs · #36 Magenta letters flat brush](Brush-Artist-Refs-36-Magenta-letters-flat-brush.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 10 % → 10 % | 29.6 px | 0.45 | 0.94 | 110 |
| heavy line | 16 % → 13 % | 47.5 px | 0.45 | 0.78 | 128 |
| pressure swell | 13 % → 11 % | 48.4 px | 0.47 | 0.85 | 97 |
| fast wave | 34 % → 16 % | 39.3 px | 0.47 | 0.48 | 261 |
| slow wave | 35 % → 20 % | 40.5 px | 0.45 | 0.57 | 409 |
| spiral | 46 % → 19 % | 30.6 px | 0.44 | 0.41 | 434 |
| loop | 27 % → 18 % | 35.0 px | 0.45 | 0.67 | 223 |
| tilted | 12 % → 12 % | 32.8 px | 0.47 | 1.00 | 129 |
| over the wet one | 26 % → 22 % | 38.5 px | 0.47 | 0.88 | 116 |
| long, no reload | 49 % → 19 % | 22.0 px | 0.44 | 0.39 | 657 | quarters: 0.30 → 0.27 → 0.22 → 0.18

Numbers say: light vs heavy: width 29.6 → 47.5 px, dark 0.45 → 0.45.

## Brush Artist · Refs · #37 Oil still life dabs
Oil 0.89 · Oil glaze 0.11 · 40 px · 15.9 s

![Brush Artist · Refs · #37 Oil still life dabs](Brush-Artist-Refs-37-Oil-still-life-dabs.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 11 % → 11 % | 32.1 px | 0.36 | 1.00 | 258 |
| heavy line | 12 % → 12 % | 36.1 px | 0.39 | 1.00 | 133 |
| pressure swell | 10 % → 10 % | 39.3 px | 0.40 | 1.00 | 215 |
| fast wave | 30 % → 30 % | 35.0 px | 0.39 | 1.00 | 399 |
| slow wave | 35 % → 35 % | 40.6 px | 0.37 | 1.00 | 668 |
| spiral | 52 % → 52 % | 34.4 px | 0.38 | 1.00 | 599 |
| loop | 29 % → 29 % | 36.9 px | 0.39 | 1.00 | 328 |
| tilted | 12 % → 12 % | 34.7 px | 0.41 | 1.00 | 182 |
| over the wet one | 23 % → 23 % | 30.6 px | 0.41 | 1.00 | 145 |
| long, no reload | 59 % → 59 % | 26.6 px | 0.31 | 1.00 | 917 | quarters: 0.23 → 0.22 → 0.20 → 0.17

Numbers say: light vs heavy: width 32.1 → 36.1 px, dark 0.36 → 0.39.

## Brush Artist · Refs · #38 Sanguine drawing
Pastel 1.00 · 6 px · 9.0 s

![Brush Artist · Refs · #38 Sanguine drawing](Brush-Artist-Refs-38-Sanguine-drawing.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 1 % → 1 % | 2.1 px | 0.61 | 1.00 | 12 |
| heavy line | 1 % → 1 % | 3.9 px | 0.61 | 1.00 | 11 |
| pressure swell | 1 % → 1 % | 3.8 px | 0.61 | 1.00 | 8 |
| fast wave | 3 % → 3 % | 3.4 px | 0.61 | 1.00 | 50 |
| slow wave | 3 % → 3 % | 3.4 px | 0.61 | 1.00 | 34 |
| spiral | 4 % → 4 % | 2.8 px | 0.61 | 1.00 | 83 |
| loop | 2 % → 2 % | 3.1 px | 0.61 | 1.00 | 94 |
| tilted | 1 % → 1 % | 3.4 px | 0.61 | 1.00 | 12 |
| over the wet one | 2 % → 2 % | 2.9 px | 0.61 | 1.00 | 17 |
| long, no reload | 6 % → 6 % | 2.7 px | 0.61 | 1.00 | 116 | quarters: 0.04 → 0.04 → 0.04 → 0.04

Numbers say: light vs heavy: width 2.1 → 3.9 px, dark 0.61 → 0.61; the long stroke does not run out of paint.

## Brush Artist · Refs · #39 Very thick impasto
Impasto 1.00 · 60 px · 20.8 s

![Brush Artist · Refs · #39 Very thick impasto](Brush-Artist-Refs-39-Very-thick-impasto.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 18 % → 18 % | 53.1 px | 0.61 | 0.97 | 177 |
| heavy line | 21 % → 20 % | 60.0 px | 0.62 | 0.96 | 179 |
| pressure swell | 15 % → 15 % | 58.1 px | 0.62 | 0.97 | 152 |
| fast wave | 48 % → 47 % | 55.3 px | 0.63 | 0.98 | 558 |
| slow wave | 47 % → 45 % | 53.9 px | 0.61 | 0.97 | 820 |
| spiral | 69 % → 63 % | 45.3 px | 0.61 | 0.92 | 866 |
| loop | 40 % → 39 % | 52.1 px | 0.61 | 0.97 | 416 |
| tilted | 16 % → 16 % | 43.8 px | 0.62 | 1.00 | 275 |
| over the wet one | 34 % → 33 % | 50.1 px | 0.62 | 0.97 | 202 |
| long, no reload | 85 % → 79 % | 38.0 px | 0.60 | 0.93 | 1375 | quarters: 0.56 → 0.55 → 0.54 → 0.51

Numbers say: light vs heavy: width 53.1 → 60.0 px, dark 0.61 → 0.62; the long stroke does not run out of paint.

## Brush Artist · Refs · #40 Watercolour blooms
Watercolour 1.00 · 90 px · 49.4 s

![Brush Artist · Refs · #40 Watercolour blooms](Brush-Artist-Refs-40-Watercolour-blooms.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 27 % → 47 % | 78.4 px | 0.08 | 1.72 | 163 |
| heavy line | 38 % → 51 % | 110.0 px | 0.09 | 1.36 | 272 |
| pressure swell | 24 % → 39 % | 91.8 px | 0.09 | 1.61 | 175 |
| fast wave | 68 % → 82 % | 78.3 px | 0.11 | 1.21 | 572 |
| slow wave | 68 % → 81 % | 79.1 px | 0.15 | 1.18 | 950 |
| spiral | 81 % → 92 % | 53.5 px | 0.14 | 1.14 | 878 |
| loop | 58 % → 72 % | 75.3 px | 0.13 | 1.24 | 503 |
| tilted | 34 % → 36 % | 94.8 px | 0.11 | 1.07 | 286 |
| over the wet one | 62 % → 81 % | 78.2 px | 0.11 | 1.31 | 219 |
| long, no reload | 97 % → 100 % | 43.6 px | 0.17 | 1.03 | 1317 | quarters: 0.21 → 0.20 → 0.17 → 0.13

Numbers say: light vs heavy: width 78.4 → 110.0 px, dark 0.08 → 0.09; wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #41 Coloured pencil hatching
Pastel 1.00 · 4 px · 8.7 s

![Brush Artist · Refs · #41 Coloured pencil hatching](Brush-Artist-Refs-41-Coloured-pencil-hatching.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 1 % → 1 % | 1.6 px | 0.43 | 1.00 | 6 |
| heavy line | 1 % → 1 % | 2.9 px | 0.43 | 1.00 | 11 |
| pressure swell | 1 % → 1 % | 2.8 px | 0.43 | 1.00 | 5 |
| fast wave | 2 % → 2 % | 2.5 px | 0.43 | 1.00 | 20 |
| slow wave | 2 % → 2 % | 2.5 px | 0.43 | 1.00 | 23 |
| spiral | 3 % → 3 % | 2.1 px | 0.43 | 1.00 | 44 |
| loop | 2 % → 2 % | 2.3 px | 0.43 | 1.00 | 16 |
| tilted | 1 % → 1 % | 3.0 px | 0.43 | 1.00 | 9 |
| over the wet one | 2 % → 2 % | 2.3 px | 0.43 | 1.00 | 14 |
| long, no reload | 5 % → 5 % | 2.0 px | 0.42 | 1.00 | 86 | quarters: 0.02 → 0.02 → 0.02 → 0.02

Numbers say: light vs heavy: width 1.6 → 2.9 px, dark 0.43 → 0.43; the long stroke does not run out of paint.

## Brush Artist · Refs · #42 Oil pastel shaggy
Pastel 1.00 · 18 px · 9.1 s

![Brush Artist · Refs · #42 Oil pastel shaggy](Brush-Artist-Refs-42-Oil-pastel-shaggy.png)

A light paint: laid on a grey sheet (on white it cannot be seen); **dark** = how far it is from the grey either way.

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 2 % → 2 % | 4.7 px | 0.36 | 1.00 | 20 |
| heavy line | 3 % → 3 % | 10.0 px | 0.36 | 1.00 | 17 |
| pressure swell | 2 % → 2 % | 9.3 px | 0.34 | 1.00 | 15 |
| fast wave | 8 % → 8 % | 9.2 px | 0.32 | 1.00 | 60 |
| slow wave | 7 % → 7 % | 8.6 px | 0.37 | 1.00 | 76 |
| spiral | 11 % → 11 % | 7.5 px | 0.36 | 1.00 | 120 |
| loop | 6 % → 6 % | 7.8 px | 0.35 | 1.00 | 62 |
| tilted | 2 % → 2 % | 6.5 px | 0.33 | 1.00 | 32 |
| over the wet one | 5 % → 5 % | 7.6 px | 0.33 | 1.00 | 23 |
| long, no reload | 15 % → 15 % | 6.5 px | 0.37 | 1.00 | 269 | quarters: 0.00 → 0.00 → 0.00 → 0.00

Numbers say: light vs heavy: width 4.7 → 10.0 px, dark 0.36 → 0.36; the long stroke does not run out of paint.

## Brush Artist · Refs · #43 Dragged black ink blocks
Gouache 1.00 · 70 px · 25.3 s

![Brush Artist · Refs · #43 Dragged black ink blocks](Brush-Artist-Refs-43-Dragged-black-ink-blocks.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 5 % → 0 % | 14.8 px | 0.00 | 0.00 | 92 |
| heavy line | 14 % → 4 % | 40.5 px | 0.66 | 0.27 | 344 |
| pressure swell | 11 % → 4 % | 42.1 px | 0.65 | 0.33 | 170 |
| fast wave | 38 % → 1 % | 43.8 px | 0.66 | 0.03 | 599 |
| slow wave | 32 % → 2 % | 36.6 px | 0.57 | 0.05 | 862 |
| spiral | 51 % → 4 % | 33.4 px | 0.54 | 0.07 | 883 |
| loop | 30 % → 2 % | 38.3 px | 0.62 | 0.06 | 455 |
| tilted | 13 % → 13 % | 37.0 px | 0.66 | 0.95 | 251 |
| over the wet one | 21 % → 2 % | 22.9 px | 0.66 | 0.10 | 208 |
| long, no reload | 44 % → 7 % | 19.8 px | 0.66 | 0.16 | 1356 | quarters: 0.47 → 0.37 → 0.18 → 0.13

Numbers say: light vs heavy: width 14.8 → 40.5 px, dark 0.00 → 0.66.

## Brush Artist · Refs · #44 Blue looping ribbon
Oil 1.00 · 80 px · 24.9 s

![Brush Artist · Refs · #44 Blue looping ribbon](Brush-Artist-Refs-44-Blue-looping-ribbon.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 25 % → 26 % | 73.1 px | 0.72 | 1.04 | 278 |
| heavy line | 27 % → 27 % | 77.7 px | 0.71 | 1.00 | 295 |
| pressure swell | 20 % → 21 % | 76.5 px | 0.71 | 1.03 | 214 |
| fast wave | 62 % → 64 % | 71.4 px | 0.71 | 1.04 | 813 |
| slow wave | 58 % → 58 % | 67.4 px | 0.70 | 1.00 | 1274 |
| spiral | 76 % → 77 % | 50.3 px | 0.69 | 1.00 | 1389 |
| loop | 53 % → 53 % | 69.2 px | 0.69 | 1.00 | 704 |
| tilted | 20 % → 20 % | 56.1 px | 0.74 | 1.00 | 391 |
| over the wet one | 41 % → 41 % | 58.7 px | 0.74 | 1.00 | 284 |
| long, no reload | 90 % → 90 % | 40.1 px | 0.69 | 1.00 | 1908 | quarters: 0.67 → 0.68 → 0.66 → 0.59

Numbers say: light vs heavy: width 73.1 → 77.7 px, dark 0.72 → 0.71; pressure barely changes the width; the long stroke does not run out of paint.

## Brush Artist · Refs · #45 Soft pastel pepper
Pastel 1.00 · 40 px · 10.0 s

![Brush Artist · Refs · #45 Soft pastel pepper](Brush-Artist-Refs-45-Soft-pastel-pepper.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 4 % → 4 % | 11.0 px | 0.53 | 1.00 | 51 |
| heavy line | 7 % → 7 % | 21.2 px | 0.53 | 1.00 | 37 |
| pressure swell | 5 % → 5 % | 19.0 px | 0.55 | 1.00 | 31 |
| fast wave | 17 % → 17 % | 19.3 px | 0.56 | 1.00 | 128 |
| slow wave | 16 % → 16 % | 18.0 px | 0.54 | 1.00 | 191 |
| spiral | 23 % → 23 % | 15.4 px | 0.54 | 1.00 | 203 |
| loop | 12 % → 12 % | 15.4 px | 0.54 | 1.00 | 103 |
| tilted | 4 % → 4 % | 11.4 px | 0.55 | 1.00 | 54 |
| over the wet one | 10 % → 10 % | 16.7 px | 0.55 | 1.00 | 52 |
| long, no reload | 28 % → 28 % | 12.6 px | 0.53 | 1.00 | 307 | quarters: 0.17 → 0.16 → 0.17 → 0.17

Numbers say: light vs heavy: width 11.0 → 21.2 px, dark 0.53 → 0.53; the long stroke does not run out of paint.

## Brush Artist · Refs · #46 Red-brown ink lips
Watercolour 1.00 · 50 px · 42.0 s

![Brush Artist · Refs · #46 Red-brown ink lips](Brush-Artist-Refs-46-Red-brown-ink-lips.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 15 % → 31 % | 43.9 px | 0.59 | 2.04 | 62 |
| heavy line | 22 % → 35 % | 63.4 px | 0.60 | 1.58 | 97 |
| pressure swell | 13 % → 22 % | 50.3 px | 0.63 | 1.64 | 67 |
| fast wave | 43 % → 64 % | 49.7 px | 0.64 | 1.50 | 220 |
| slow wave | 42 % → 63 % | 49.1 px | 0.67 | 1.49 | 393 |
| spiral | 65 % → 79 % | 42.6 px | 0.69 | 1.22 | 367 |
| loop | 38 % → 55 % | 48.8 px | 0.67 | 1.47 | 202 |
| tilted | 21 % → 23 % | 58.2 px | 0.60 | 1.11 | 127 |
| over the wet one | 42 % → 63 % | 58.5 px | 0.60 | 1.51 | 113 |
| long, no reload | 78 % → 95 % | 35.1 px | 0.70 | 1.21 | 528 | quarters: 0.71 → 0.71 → 0.69 → 0.65

Numbers say: light vs heavy: width 43.9 → 63.4 px, dark 0.59 → 0.60; the long stroke does not run out of paint; wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #47 Pink knife slabs
Impasto 1.00 · 90 px · 29.3 s

![Brush Artist · Refs · #47 Pink knife slabs](Brush-Artist-Refs-47-Pink-knife-slabs.png)

A light paint: laid on a grey sheet (on white it cannot be seen); **dark** = how far it is from the grey either way.

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 27 % → 26 % | 78.7 px | 0.29 | 0.97 | 195 |
| heavy line | 29 % → 28 % | 84.6 px | 0.29 | 0.96 | 226 |
| pressure swell | 22 % → 22 % | 81.2 px | 0.26 | 1.01 | 164 |
| fast wave | 62 % → 61 % | 71.8 px | 0.24 | 0.98 | 627 |
| slow wave | 62 % → 58 % | 71.5 px | 0.28 | 0.94 | 941 |
| spiral | 75 % → 60 % | 49.3 px | 0.28 | 0.80 | 1056 |
| loop | 56 % → 54 % | 72.1 px | 0.29 | 0.97 | 549 |
| tilted | 22 % → 22 % | 60.2 px | 0.25 | 1.00 | 455 |
| over the wet one | 46 % → 44 % | 69.3 px | 0.25 | 0.96 | 563 |
| long, no reload | 93 % → 77 % | 41.9 px | 0.26 | 0.83 | 1631 | quarters: 0.00 → 0.00 → 0.00 → 0.00

Numbers say: light vs heavy: width 78.7 → 84.6 px, dark 0.29 → 0.29; pressure barely changes the width; the long stroke does not run out of paint.

## Brush Artist · Refs · #48 Black bands with drips
Gouache 1.00 · 70 px · 52.1 s

![Brush Artist · Refs · #48 Black bands with drips](Brush-Artist-Refs-48-Black-bands-with-drips.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 28 % → 23 % | 80.2 px | 0.63 | 0.82 | 185 |
| heavy line | 35 % → 26 % | 100.7 px | 0.64 | 0.75 | 243 |
| pressure swell | 25 % → 21 % | 93.8 px | 0.63 | 0.85 | 169 |
| fast wave | 63 % → 41 % | 72.9 px | 0.63 | 0.64 | 565 |
| slow wave | 62 % → 41 % | 71.5 px | 0.63 | 0.66 | 1299 |
| spiral | 69 % → 40 % | 45.7 px | 0.61 | 0.57 | 1020 |
| loop | 54 % → 40 % | 69.9 px | 0.63 | 0.74 | 484 |
| tilted | 29 % → 29 % | 80.5 px | 0.62 | 1.01 | 301 |
| over the wet one | 59 % → 48 % | 82.9 px | 0.62 | 0.82 | 218 |
| long, no reload | 78 % → 37 % | 34.9 px | 0.61 | 0.47 | 1445 | quarters: 0.58 → 0.54 → 0.47 → 0.39

Numbers say: light vs heavy: width 80.2 → 100.7 px, dark 0.63 → 0.64.

## Brush Artist · Refs · #49 Magenta letters round brush
Ink 1.00 · 30 px · 32.9 s

![Brush Artist · Refs · #49 Magenta letters round brush](Brush-Artist-Refs-49-Magenta-letters-round-brush.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 6 % → 8 % | 18.1 px | 0.49 | 1.21 | 32 |
| heavy line | 21 % → 20 % | 60.3 px | 0.51 | 0.98 | 112 |
| pressure swell | 13 % → 13 % | 47.1 px | 0.51 | 1.01 | 89 |
| fast wave | 38 % → 38 % | 44.0 px | 0.51 | 1.00 | 423 |
| slow wave | 34 % → 34 % | 39.4 px | 0.51 | 0.99 | 290 |
| spiral | 49 % → 48 % | 32.6 px | 0.51 | 0.96 | 334 |
| loop | 30 % → 30 % | 38.3 px | 0.51 | 1.00 | 149 |
| tilted | 11 % → 12 % | 32.0 px | 0.52 | 1.00 | 114 |
| over the wet one | 27 % → 27 % | 42.2 px | 0.52 | 1.01 | 95 |
| long, no reload | 63 % → 56 % | 28.2 px | 0.50 | 0.90 | 440 | quarters: 0.42 → 0.37 → 0.30 → 0.25

Numbers say: light vs heavy: width 18.1 → 60.3 px, dark 0.49 → 0.51.

## Brush Artist · Refs · #50 Thick swipes on photo
Impasto 1.00 · 40 px · 17.7 s

![Brush Artist · Refs · #50 Thick swipes on photo](Brush-Artist-Refs-50-Thick-swipes-on-photo.png)

A light paint: laid on a grey sheet (on white it cannot be seen); **dark** = how far it is from the grey either way.

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 13 % → 13 % | 38.6 px | 0.27 | 0.95 | 114 |
| heavy line | 14 % → 13 % | 40.0 px | 0.27 | 0.96 | 108 |
| pressure swell | 11 % → 10 % | 40.1 px | 0.24 | 0.95 | 116 |
| fast wave | 35 % → 31 % | 40.1 px | 0.24 | 0.89 | 402 |
| slow wave | 34 % → 32 % | 39.5 px | 0.26 | 0.93 | 743 |
| spiral | 58 % → 46 % | 38.5 px | 0.29 | 0.79 | 540 |
| loop | 29 % → 28 % | 37.4 px | 0.26 | 0.96 | 309 |
| tilted | 12 % → 12 % | 33.6 px | 0.22 | 1.00 | 163 |
| over the wet one | 25 % → 24 % | 36.7 px | 0.22 | 0.96 | 130 |
| long, no reload | 68 % → 46 % | 30.4 px | 0.26 | 0.68 | 989 | quarters: 0.00 → 0.00 → 0.00 → 0.00

Numbers say: light vs heavy: width 38.6 → 40.0 px, dark 0.27 → 0.27; pressure barely changes the width.

## Brush Artist · Refs · Drag #e8b4a8
Gouache 1.00 · 40 px · 17.1 s

![Brush Artist · Refs · Drag #e8b4a8](Brush-Artist-Refs-Drag-e8b4a8.png)

A light paint: laid on a grey sheet (on white it cannot be seen); **dark** = how far it is from the grey either way.

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 3 % → 0 % | 9.3 px | 0.00 | 0.00 | 98 |
| heavy line | 6 % → 0 % | 16.2 px | 0.34 | 0.01 | 139 |
| pressure swell | 3 % → 0 % | 12.9 px | 0.00 | 0.00 | 91 |
| fast wave | 16 % → 0 % | 18.1 px | 0.00 | 0.00 | 343 |
| slow wave | 13 % → 0 % | 15.0 px | 0.00 | 0.00 | 795 |
| spiral | 20 % → 0 % | 13.4 px | 0.00 | 0.00 | 523 |
| loop | 13 % → 0 % | 17.1 px | 0.00 | 0.00 | 243 |
| tilted | 6 % → 5 % | 16.8 px | 0.00 | 0.77 | 141 |
| over the wet one | 7 % → 0 % | 1.8 px | 0.00 | 0.00 | 103 |
| long, no reload | 10 % → 0 % | 4.6 px | 0.00 | 0.00 | 625 | quarters: 0.02 → 0.02 → 0.02 → 0.02

Numbers say: light vs heavy: width 9.3 → 16.2 px, dark 0.00 → 0.34; the long stroke does not run out of paint.

## Brush Artist · Refs · Drag #e8e4e0
Gouache 1.00 · 40 px · 20.1 s

![Brush Artist · Refs · Drag #e8e4e0](Brush-Artist-Refs-Drag-e8e4e0.png)

A light paint: laid on a grey sheet (on white it cannot be seen); **dark** = how far it is from the grey either way.

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 3 % → 0 % | 9.3 px | 0.00 | 0.00 | 121 |
| heavy line | 6 % → 0 % | 16.2 px | 0.43 | 0.01 | 120 |
| pressure swell | 3 % → 0 % | 12.9 px | 0.00 | 0.00 | 84 |
| fast wave | 16 % → 0 % | 18.1 px | 0.00 | 0.00 | 349 |
| slow wave | 13 % → 0 % | 15.0 px | 0.00 | 0.00 | 621 |
| spiral | 20 % → 0 % | 13.4 px | 0.00 | 0.00 | 607 |
| loop | 13 % → 0 % | 17.1 px | 0.00 | 0.00 | 261 |
| tilted | 6 % → 5 % | 16.8 px | 0.00 | 0.77 | 135 |
| over the wet one | 7 % → 0 % | 1.8 px | 0.00 | 0.00 | 113 |
| long, no reload | 10 % → 0 % | 4.6 px | 0.00 | 0.00 | 798 | quarters: 0.02 → 0.02 → 0.02 → 0.02

Numbers say: light vs heavy: width 9.3 → 16.2 px, dark 0.00 → 0.43; the long stroke does not run out of paint.

## Brush Artist · Refs · Finger
Pastel 1.00 · 36 px · 23.7 s · over bands of wet oil paint and oil pastel in turn (it works on paint already there: look at what it does to the bands; covered counts the bands too)

![Brush Artist · Refs · Finger](Brush-Artist-Refs-Finger.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 26 % → 26 % | 74.4 px | 0.80 | 1.00 | 55 |
| heavy line | 27 % → 27 % | 79.3 px | 0.80 | 1.00 | 47 |
| pressure swell | 26 % → 26 % | 98.0 px | 0.80 | 1.00 | 38 |
| fast wave | 33 % → 33 % | 38.0 px | 0.78 | 1.00 | 139 |
| slow wave | 31 % → 31 % | 36.3 px | 0.78 | 1.00 | 219 |
| spiral | 38 % → 38 % | 25.3 px | 0.76 | 1.00 | 249 |
| loop | 31 % → 31 % | 39.5 px | 0.79 | 1.00 | 113 |
| tilted | 26 % → 26 % | 73.5 px | 0.78 | 1.00 | 77 |
| over the wet one | 29 % → 29 % | 7.5 px | 0.78 | 1.00 | 65 |
| long, no reload | 39 % → 39 % | 17.4 px | 0.76 | 1.00 | 364 | quarters: 0.24 → 0.36 → 0.32 → 0.37

Numbers say: light vs heavy: width 74.4 → 79.3 px, dark 0.80 → 0.80; pressure barely changes the width; the long stroke does not run out of paint.

## Brush Artist · Ink — wash
Watercolour 1.00 · 38 px · 37.2 s

![Brush Artist · Ink — wash](Brush-Artist-Ink-wash.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 11 % → 11 % | 31.6 px | 0.39 | 1.04 | 56 |
| heavy line | 19 % → 19 % | 54.3 px | 0.32 | 1.03 | 100 |
| pressure swell | 12 % → 13 % | 45.2 px | 0.37 | 1.04 | 53 |
| fast wave | 39 % → 41 % | 45.5 px | 0.31 | 1.04 | 215 |
| slow wave | 37 % → 38 % | 42.9 px | 0.37 | 1.03 | 364 |
| spiral | 58 % → 61 % | 38.6 px | 0.31 | 1.04 | 316 |
| loop | 32 % → 33 % | 41.9 px | 0.35 | 1.02 | 241 |
| tilted | 13 % → 14 % | 37.0 px | 0.38 | 1.04 | 132 |
| over the wet one | 29 % → 30 % | 42.8 px | 0.38 | 1.04 | 110 |
| long, no reload | 67 % → 72 % | 30.0 px | 0.29 | 1.07 | 779 | quarters: 0.34 → 0.27 → 0.19 → 0.12

Numbers say: light vs heavy: width 31.6 → 54.3 px, dark 0.39 → 0.32.

## Brush Artist · Ink — brush line
Ink 1.00 · 16 px · 32.8 s

![Brush Artist · Ink — brush line](Brush-Artist-Ink-brush-line.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 3 % → 5 % | 8.2 px | 0.77 | 1.72 | 39 |
| heavy line | 12 % → 12 % | 35.2 px | 0.88 | 0.99 | 78 |
| pressure swell | 8 % → 8 % | 28.5 px | 0.86 | 1.06 | 60 |
| fast wave | 24 % → 24 % | 28.2 px | 0.87 | 0.98 | 180 |
| slow wave | 20 % → 20 % | 23.7 px | 0.87 | 0.97 | 215 |
| spiral | 31 % → 27 % | 20.3 px | 0.86 | 0.87 | 292 |
| loop | 19 % → 19 % | 24.3 px | 0.87 | 0.99 | 203 |
| tilted | 8 % → 8 % | 21.2 px | 0.88 | 1.01 | 132 |
| over the wet one | 17 % → 17 % | 26.2 px | 0.88 | 1.01 | 112 |
| long, no reload | 44 % → 31 % | 19.7 px | 0.84 | 0.70 | 556 | quarters: 0.51 → 0.41 → 0.30 → 0.20

Numbers say: light vs heavy: width 8.2 → 35.2 px, dark 0.77 → 0.88; wet paint spreads well beyond the stroke.

## Brush Artist · Ink — dry brush
Gouache 1.00 · 30 px · 25.3 s

![Brush Artist · Ink — dry brush](Brush-Artist-Ink-dry-brush.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 2 % → 0 % | 5.7 px | 0.00 | 0.00 | 57 |
| heavy line | 4 % → 0 % | 10.2 px | 0.77 | 0.01 | 149 |
| pressure swell | 4 % → 0 % | 14.1 px | 0.77 | 0.06 | 80 |
| fast wave | 12 % → 0 % | 14.0 px | 0.77 | 0.00 | 389 |
| slow wave | 10 % → 0 % | 11.9 px | 0.77 | 0.00 | 625 |
| spiral | 17 % → 0 % | 11.1 px | 0.77 | 0.00 | 541 |
| loop | 9 % → 0 % | 11.2 px | 0.77 | 0.01 | 233 |
| tilted | 5 % → 4 % | 13.5 px | 0.77 | 0.89 | 111 |
| over the wet one | 7 % → 0 % | 5.9 px | 0.77 | 0.00 | 82 |
| long, no reload | 14 % → 1 % | 6.5 px | 0.77 | 0.08 | 693 | quarters: 0.21 → 0.14 → 0.10 → 0.07

Numbers say: light vs heavy: width 5.7 → 10.2 px, dark 0.00 → 0.77.

## Brush Artist · Watercolour — blue
Watercolour 0.93 · Ink 0.07 · 40 px · 33.0 s

![Brush Artist · Watercolour — blue](Brush-Artist-Watercolour-blue.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 6 % → 11 % | 16.2 px | 0.29 | 1.88 | 78 |
| heavy line | 11 % → 13 % | 31.9 px | 0.29 | 1.17 | 113 |
| pressure swell | 7 % → 9 % | 25.7 px | 0.30 | 1.38 | 47 |
| fast wave | 24 % → 27 % | 28.2 px | 0.29 | 1.12 | 211 |
| slow wave | 23 % → 32 % | 26.4 px | 0.31 | 1.41 | 217 |
| spiral | 39 % → 47 % | 25.6 px | 0.29 | 1.21 | 263 |
| loop | 20 % → 25 % | 25.7 px | 0.30 | 1.25 | 149 |
| tilted | 12 % → 12 % | 34.0 px | 0.30 | 1.00 | 108 |
| over the wet one | 21 % → 25 % | 25.2 px | 0.30 | 1.19 | 84 |
| long, no reload | 53 % → 59 % | 23.6 px | 0.30 | 1.12 | 446 | quarters: 0.23 → 0.21 → 0.19 → 0.16

Numbers say: light vs heavy: width 16.2 → 31.9 px, dark 0.29 → 0.29; wet paint spreads well beyond the stroke.

## Brush Artist · Watercolour — violet
Watercolour 0.93 · Ink 0.07 · 40 px · 31.7 s

![Brush Artist · Watercolour — violet](Brush-Artist-Watercolour-violet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 6 % → 11 % | 16.2 px | 0.36 | 1.88 | 29 |
| heavy line | 11 % → 13 % | 31.9 px | 0.37 | 1.17 | 93 |
| pressure swell | 7 % → 9 % | 25.7 px | 0.38 | 1.38 | 35 |
| fast wave | 24 % → 27 % | 28.2 px | 0.38 | 1.12 | 165 |
| slow wave | 23 % → 32 % | 26.4 px | 0.39 | 1.41 | 277 |
| spiral | 39 % → 47 % | 25.6 px | 0.37 | 1.21 | 279 |
| loop | 20 % → 25 % | 25.7 px | 0.38 | 1.25 | 213 |
| tilted | 12 % → 12 % | 34.0 px | 0.38 | 1.00 | 136 |
| over the wet one | 21 % → 25 % | 25.2 px | 0.38 | 1.19 | 53 |
| long, no reload | 53 % → 59 % | 23.6 px | 0.38 | 1.12 | 546 | quarters: 0.28 → 0.27 → 0.24 → 0.21

Numbers say: light vs heavy: width 16.2 → 31.9 px, dark 0.36 → 0.37; wet paint spreads well beyond the stroke.

## Brush Artist · Watercolour — teal
Watercolour 0.93 · Ink 0.07 · 40 px · 31.2 s

![Brush Artist · Watercolour — teal](Brush-Artist-Watercolour-teal.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 6 % → 11 % | 16.2 px | 0.23 | 1.88 | 42 |
| heavy line | 11 % → 13 % | 31.9 px | 0.23 | 1.17 | 110 |
| pressure swell | 7 % → 9 % | 25.7 px | 0.24 | 1.38 | 54 |
| fast wave | 24 % → 27 % | 28.2 px | 0.23 | 1.12 | 275 |
| slow wave | 23 % → 32 % | 26.4 px | 0.25 | 1.41 | 325 |
| spiral | 39 % → 47 % | 25.6 px | 0.23 | 1.21 | 445 |
| loop | 20 % → 25 % | 25.7 px | 0.24 | 1.25 | 232 |
| tilted | 12 % → 12 % | 34.0 px | 0.24 | 1.00 | 124 |
| over the wet one | 21 % → 25 % | 25.2 px | 0.24 | 1.19 | 76 |
| long, no reload | 53 % → 59 % | 23.6 px | 0.24 | 1.12 | 395 | quarters: 0.18 → 0.16 → 0.15 → 0.13

Numbers say: light vs heavy: width 16.2 → 31.9 px, dark 0.23 → 0.23; wet paint spreads well beyond the stroke.

## Brush Artist · Gouache
Gouache 1.00 · 30 px · 34.1 s

![Brush Artist · Gouache](Brush-Artist-Gouache.png)

A light paint: laid on a grey sheet (on white it cannot be seen); **dark** = how far it is from the grey either way.

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 8 % → 8 % | 24.4 px | 0.27 | 0.97 | 86 |
| heavy line | 15 % → 12 % | 42.8 px | 0.27 | 0.78 | 156 |
| pressure swell | 11 % → 9 % | 41.0 px | 0.27 | 0.85 | 64 |
| fast wave | 30 % → 14 % | 34.9 px | 0.26 | 0.45 | 296 |
| slow wave | 29 % → 14 % | 34.0 px | 0.26 | 0.47 | 587 |
| spiral | 40 % → 14 % | 26.6 px | 0.26 | 0.35 | 462 |
| loop | 24 % → 15 % | 30.6 px | 0.26 | 0.62 | 207 |
| tilted | 10 % → 10 % | 27.4 px | 0.27 | 1.01 | 123 |
| over the wet one | 22 % → 19 % | 32.9 px | 0.27 | 0.89 | 109 |
| long, no reload | 43 % → 15 % | 19.1 px | 0.26 | 0.35 | 692 | quarters: 0.01 → 0.01 → 0.01 → 0.01

Numbers say: light vs heavy: width 24.4 → 42.8 px, dark 0.27 → 0.27; the long stroke does not run out of paint.

## Brush Artist · Oil — bristle
Oil 0.89 · Oil glaze 0.11 · 30 px · 18.7 s

![Brush Artist · Oil — bristle](Brush-Artist-Oil-bristle.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 10 % → 10 % | 28.5 px | 0.53 | 1.00 | 111 |
| heavy line | 11 % → 11 % | 32.4 px | 0.54 | 1.00 | 156 |
| pressure swell | 8 % → 8 % | 31.8 px | 0.54 | 1.00 | 174 |
| fast wave | 28 % → 28 % | 32.0 px | 0.54 | 1.00 | 281 |
| slow wave | 27 % → 27 % | 31.6 px | 0.54 | 1.00 | 764 |
| spiral | 48 % → 48 % | 31.3 px | 0.53 | 1.00 | 769 |
| loop | 22 % → 22 % | 28.9 px | 0.54 | 1.00 | 447 |
| tilted | 11 % → 11 % | 29.9 px | 0.54 | 1.00 | 213 |
| over the wet one | 21 % → 21 % | 29.6 px | 0.54 | 1.00 | 185 |
| long, no reload | 55 % → 55 % | 24.7 px | 0.52 | 1.00 | 887 | quarters: 0.35 → 0.33 → 0.31 → 0.29

Numbers say: light vs heavy: width 28.5 → 32.4 px, dark 0.53 → 0.54.

## Brush Artist · Charcoal — stick
Charcoal 0.78 · Pastel 0.22 · 28 px · 13.2 s

![Brush Artist · Charcoal — stick](Brush-Artist-Charcoal-stick.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 5 % → 5 % | 15.2 px | 0.85 | 1.00 | 21 |
| heavy line | 8 % → 8 % | 24.2 px | 0.85 | 1.00 | 32 |
| pressure swell | 5 % → 5 % | 19.3 px | 0.85 | 1.00 | 25 |
| fast wave | 19 % → 19 % | 21.5 px | 0.85 | 1.00 | 124 |
| slow wave | 18 % → 18 % | 21.1 px | 0.85 | 1.00 | 240 |
| spiral | 25 % → 25 % | 16.3 px | 0.85 | 1.00 | 206 |
| loop | 16 % → 16 % | 20.2 px | 0.85 | 1.00 | 90 |
| tilted | 6 % → 6 % | 17.3 px | 0.85 | 1.00 | 31 |
| over the wet one | 14 % → 14 % | 20.5 px | 0.85 | 1.00 | 47 |
| long, no reload | 41 % → 41 % | 18.5 px | 0.85 | 1.00 | 208 | quarters: 0.39 → 0.39 → 0.39 → 0.39

Numbers say: light vs heavy: width 15.2 → 24.2 px, dark 0.85 → 0.85; the long stroke does not run out of paint.

## Brush Artist · Charcoal — stick B
Charcoal 0.78 · Pastel 0.22 · 36 px · 10.7 s

![Brush Artist · Charcoal — stick B](Brush-Artist-Charcoal-stick-B.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 7 % → 7 % | 19.2 px | 0.85 | 1.00 | 54 |
| heavy line | 10 % → 10 % | 30.5 px | 0.85 | 1.00 | 99 |
| pressure swell | 7 % → 7 % | 24.5 px | 0.85 | 1.00 | 32 |
| fast wave | 24 % → 24 % | 27.6 px | 0.85 | 1.00 | 196 |
| slow wave | 23 % → 23 % | 26.6 px | 0.85 | 1.00 | 248 |
| spiral | 35 % → 35 % | 23.2 px | 0.85 | 1.00 | 205 |
| loop | 19 % → 19 % | 25.2 px | 0.85 | 1.00 | 72 |
| tilted | 7 % → 7 % | 20.3 px | 0.85 | 1.00 | 41 |
| over the wet one | 17 % → 17 % | 25.9 px | 0.85 | 1.00 | 36 |
| long, no reload | 50 % → 50 % | 22.6 px | 0.85 | 1.00 | 264 | quarters: 0.47 → 0.47 → 0.47 → 0.47

Numbers say: light vs heavy: width 19.2 → 30.5 px, dark 0.85 → 0.85; the long stroke does not run out of paint.

## Brush Artist · Charcoal — stick C
Charcoal 0.78 · Pastel 0.22 · 22 px · 8.7 s

![Brush Artist · Charcoal — stick C](Brush-Artist-Charcoal-stick-C.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 4 % → 4 % | 12.2 px | 0.85 | 1.00 | 18 |
| heavy line | 7 % → 7 % | 19.4 px | 0.85 | 1.00 | 22 |
| pressure swell | 4 % → 4 % | 14.3 px | 0.85 | 1.00 | 17 |
| fast wave | 15 % → 15 % | 17.1 px | 0.85 | 1.00 | 56 |
| slow wave | 15 % → 15 % | 17.0 px | 0.85 | 1.00 | 95 |
| spiral | 20 % → 20 % | 13.3 px | 0.85 | 1.00 | 76 |
| loop | 12 % → 12 % | 16.1 px | 0.85 | 1.00 | 40 |
| tilted | 5 % → 5 % | 15.1 px | 0.85 | 1.00 | 19 |
| over the wet one | 11 % → 11 % | 16.8 px | 0.85 | 1.00 | 19 |
| long, no reload | 34 % → 34 % | 15.3 px | 0.85 | 1.00 | 100 | quarters: 0.33 → 0.32 → 0.32 → 0.32

Numbers say: light vs heavy: width 12.2 → 19.4 px, dark 0.85 → 0.85; the long stroke does not run out of paint.

## Oil · Henry Ward · Loaded flat
Oil 1.00 · 46 px · 14.7 s

![Oil · Henry Ward · Loaded flat](Oil-Henry-Ward-Loaded-flat.png)

A light paint: laid on a grey sheet (on white it cannot be seen); **dark** = how far it is from the grey either way.

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 8 % → 8 % | 22.5 px | 0.30 | 1.00 | 184 |
| heavy line | 15 % → 15 % | 43.4 px | 0.37 | 1.00 | 180 |
| pressure swell | 11 % → 11 % | 41.0 px | 0.32 | 1.00 | 169 |
| fast wave | 32 % → 33 % | 37.5 px | 0.29 | 1.00 | 411 |
| slow wave | 26 % → 26 % | 30.2 px | 0.35 | 1.00 | 647 |
| spiral | 51 % → 51 % | 33.5 px | 0.30 | 1.00 | 725 |
| loop | 28 % → 28 % | 36.3 px | 0.34 | 1.00 | 360 |
| tilted | 13 % → 13 % | 37.3 px | 0.30 | 1.00 | 217 |
| over the wet one | 27 % → 27 % | 37.1 px | 0.30 | 1.00 | 172 |
| long, no reload | 48 % → 48 % | 21.5 px | 0.30 | 1.00 | 1012 | quarters: 0.00 → 0.00 → 0.00 → 0.00

Numbers say: light vs heavy: width 22.5 → 43.4 px, dark 0.30 → 0.37; the long stroke does not run out of paint.

## Oil · Henry Ward · Dry scrub
Oil 1.00 · 50 px · 14.0 s

![Oil · Henry Ward · Dry scrub](Oil-Henry-Ward-Dry-scrub.png)

A light paint: laid on a grey sheet (on white it cannot be seen); **dark** = how far it is from the grey either way.

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 5 % → 5 % | 15.0 px | 0.17 | 1.00 | 166 |
| heavy line | 9 % → 9 % | 25.4 px | 0.23 | 1.00 | 160 |
| pressure swell | 7 % → 7 % | 27.5 px | 0.25 | 1.00 | 108 |
| fast wave | 26 % → 26 % | 30.2 px | 0.23 | 1.01 | 409 |
| slow wave | 26 % → 26 % | 29.6 px | 0.25 | 1.00 | 700 |
| spiral | 45 % → 45 % | 29.8 px | 0.20 | 1.00 | 713 |
| loop | 20 % → 20 % | 26.1 px | 0.24 | 1.00 | 332 |
| tilted | 13 % → 13 % | 35.4 px | 0.21 | 1.00 | 218 |
| over the wet one | 18 % → 18 % | 14.3 px | 0.21 | 1.00 | 147 |
| long, no reload | 31 % → 31 % | 13.7 px | 0.19 | 1.00 | 893 | quarters: 0.00 → 0.00 → 0.00 → 0.00

Numbers say: light vs heavy: width 15.0 → 25.4 px, dark 0.17 → 0.23; the long stroke does not run out of paint.

## Oil · Henry Ward · Dirty contour
Oil 1.00 · 24 px · 12.5 s

![Oil · Henry Ward · Dirty contour](Oil-Henry-Ward-Dirty-contour.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 8 % → 8 % | 22.0 px | 0.74 | 1.00 | 86 |
| heavy line | 8 % → 8 % | 24.5 px | 0.74 | 1.00 | 98 |
| pressure swell | 7 % → 7 % | 27.1 px | 0.77 | 1.00 | 74 |
| fast wave | 19 % → 19 % | 22.1 px | 0.79 | 1.00 | 229 |
| slow wave | 21 % → 21 % | 24.2 px | 0.75 | 1.00 | 391 |
| spiral | 31 % → 31 % | 20.7 px | 0.75 | 1.00 | 437 |
| loop | 17 % → 17 % | 21.6 px | 0.76 | 1.00 | 217 |
| tilted | 9 % → 9 % | 26.2 px | 0.76 | 1.00 | 118 |
| over the wet one | 18 % → 18 % | 22.7 px | 0.76 | 1.00 | 110 |
| long, no reload | 41 % → 41 % | 18.4 px | 0.69 | 1.00 | 618 | quarters: 0.41 → 0.35 → 0.28 → 0.23

Numbers say: light vs heavy: width 22.0 → 24.5 px, dark 0.74 → 0.74.

## Oil · Henry Ward · Wet drag
Oil 1.00 · 44 px · 14.7 s

![Oil · Henry Ward · Wet drag](Oil-Henry-Ward-Wet-drag.png)

A light paint: laid on a grey sheet (on white it cannot be seen); **dark** = how far it is from the grey either way.

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 9 % → 9 % | 24.7 px | 0.20 | 1.00 | 123 |
| heavy line | 10 % → 10 % | 28.4 px | 0.35 | 1.00 | 145 |
| pressure swell | 10 % → 10 % | 36.9 px | 0.29 | 1.00 | 109 |
| fast wave | 30 % → 30 % | 34.1 px | 0.25 | 1.00 | 377 |
| slow wave | 32 % → 32 % | 36.5 px | 0.28 | 1.00 | 661 |
| spiral | 52 % → 52 % | 34.6 px | 0.28 | 1.00 | 692 |
| loop | 22 % → 22 % | 28.9 px | 0.31 | 1.00 | 306 |
| tilted | 12 % → 12 % | 34.6 px | 0.27 | 1.00 | 192 |
| over the wet one | 24 % → 24 % | 32.9 px | 0.27 | 1.00 | 151 |
| long, no reload | 55 % → 55 % | 24.6 px | 0.29 | 1.00 | 945 | quarters: 0.00 → 0.00 → 0.00 → 0.00

Numbers say: light vs heavy: width 24.7 → 28.4 px, dark 0.20 → 0.35; the long stroke does not run out of paint.

## Oil · Henry Ward · Thin veil
Oil 0.81 · Ink 0.19 · 56 px · 38.6 s

![Oil · Henry Ward · Thin veil](Oil-Henry-Ward-Thin-veil.png)

A light paint: laid on a grey sheet (on white it cannot be seen); **dark** = how far it is from the grey either way.

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 6 % → 4 % | 18.8 px | 0.08 | 0.66 | 141 |
| heavy line | 12 % → 12 % | 36.0 px | 0.28 | 0.94 | 182 |
| pressure swell | 10 % → 9 % | 38.2 px | 0.18 | 0.89 | 134 |
| fast wave | 39 % → 32 % | 44.6 px | 0.13 | 0.82 | 540 |
| slow wave | 36 % → 33 % | 42.2 px | 0.17 | 0.91 | 824 |
| spiral | 61 % → 50 % | 40.4 px | 0.15 | 0.81 | 895 |
| loop | 28 % → 23 % | 36.3 px | 0.15 | 0.83 | 471 |
| tilted | 15 % → 15 % | 41.7 px | 0.15 | 1.01 | 303 |
| over the wet one | 24 % → 22 % | 26.1 px | 0.15 | 0.89 | 266 |
| long, no reload | 56 % → 44 % | 24.9 px | 0.15 | 0.79 | 1358 | quarters: 0.01 → 0.01 → 0.01 → 0.01

Numbers say: light vs heavy: width 18.8 → 36.0 px, dark 0.08 → 0.28; the long stroke does not run out of paint.

## Oil · Henry Ward · Ground
Gouache 1.00 · 160 px · 83.2 s

![Oil · Henry Ward · Ground](Oil-Henry-Ward-Ground.png)

A light paint: laid on a grey sheet (on white it cannot be seen); **dark** = how far it is from the grey either way.

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 51 % → 46 % | 148.3 px | 0.37 | 0.89 | 679 |
| heavy line | 52 % → 47 % | 151.5 px | 0.37 | 0.91 | 805 |
| pressure swell | 41 % → 45 % | 154.8 px | 0.36 | 1.10 | 582 |
| fast wave | 85 % → 86 % | 97.8 px | 0.36 | 1.01 | 2208 |
| slow wave | 86 % → 73 % | 99.2 px | 0.37 | 0.86 | 4307 |
| spiral | 88 % → 69 % | 58.3 px | 0.36 | 0.77 | 6325 |
| loop | 75 % → 69 % | 97.0 px | 0.37 | 0.92 | 1970 |
| tilted | 39 % → 39 % | 107.5 px | 0.37 | 1.00 | 1125 |
| over the wet one | 76 % → 71 % | 104.6 px | 0.37 | 0.93 | 1002 |
| long, no reload | 98 % → 87 % | 44.0 px | 0.37 | 0.88 | 8208 | quarters: 0.00 → 0.00 → 0.00 → 0.00

Numbers say: light vs heavy: width 148.3 → 151.5 px, dark 0.37 → 0.37; pressure barely changes the width.

## Oil · Henry Ward · HW #02 cream over wet olive
Oil 0.81 · Ink 0.19 · 56 px · 40.8 s

![Oil · Henry Ward · HW #02 cream over wet olive](Oil-Henry-Ward-HW-02-cream-over-wet-olive.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 6 % → 4 % | 18.8 px | 0.62 | 0.66 | 142 |
| heavy line | 12 % → 12 % | 36.0 px | 0.67 | 0.94 | 204 |
| pressure swell | 10 % → 9 % | 38.2 px | 0.64 | 0.89 | 142 |
| fast wave | 39 % → 32 % | 44.6 px | 0.68 | 0.82 | 488 |
| slow wave | 36 % → 33 % | 42.2 px | 0.66 | 0.91 | 849 |
| spiral | 61 % → 50 % | 40.4 px | 0.57 | 0.81 | 874 |
| loop | 28 % → 23 % | 36.3 px | 0.60 | 0.83 | 486 |
| tilted | 15 % → 15 % | 41.7 px | 0.69 | 1.01 | 274 |
| over the wet one | 24 % → 22 % | 26.1 px | 0.69 | 0.89 | 242 |
| long, no reload | 56 % → 44 % | 24.9 px | 0.56 | 0.79 | 1482 | quarters: 0.40 → 0.25 → 0.23 → 0.22

Numbers say: light vs heavy: width 18.8 → 36.0 px, dark 0.62 → 0.67.

## Oil · Henry Ward · HW #04 grey arcs over ochre
Oil 1.00 · 46 px · 19.1 s

![Oil · Henry Ward · HW #04 grey arcs over ochre](Oil-Henry-Ward-HW-04-grey-arcs-over-ochre.png)

A light paint: laid on a grey sheet (on white it cannot be seen); **dark** = how far it is from the grey either way.

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 8 % → 8 % | 22.5 px | 0.22 | 1.00 | 129 |
| heavy line | 15 % → 15 % | 43.4 px | 0.28 | 1.00 | 151 |
| pressure swell | 11 % → 11 % | 41.0 px | 0.23 | 1.00 | 111 |
| fast wave | 32 % → 33 % | 37.5 px | 0.21 | 1.00 | 405 |
| slow wave | 26 % → 26 % | 30.2 px | 0.26 | 1.00 | 658 |
| spiral | 51 % → 51 % | 33.5 px | 0.23 | 1.00 | 776 |
| loop | 28 % → 28 % | 36.3 px | 0.25 | 1.00 | 371 |
| tilted | 13 % → 13 % | 37.3 px | 0.23 | 1.00 | 271 |
| over the wet one | 27 % → 27 % | 37.1 px | 0.23 | 1.00 | 237 |
| long, no reload | 48 % → 48 % | 21.5 px | 0.24 | 1.00 | 1144 | quarters: 0.00 → 0.00 → 0.00 → 0.01

Numbers say: light vs heavy: width 22.5 → 43.4 px, dark 0.22 → 0.28; the long stroke does not run out of paint.

## Oil · Henry Ward · HW #09 white arches over wet blue-grey
Oil 1.00 · 46 px · 19.4 s

![Oil · Henry Ward · HW #09 white arches over wet blue-grey](Oil-Henry-Ward-HW-09-white-arches-over-wet-blue-grey.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 8 % → 8 % | 22.5 px | 0.33 | 1.00 | 120 |
| heavy line | 15 % → 15 % | 43.4 px | 0.36 | 1.00 | 156 |
| pressure swell | 11 % → 11 % | 41.0 px | 0.42 | 1.00 | 150 |
| fast wave | 32 % → 33 % | 37.5 px | 0.37 | 1.00 | 464 |
| slow wave | 26 % → 26 % | 30.2 px | 0.34 | 1.00 | 761 |
| spiral | 51 % → 51 % | 33.5 px | 0.30 | 1.00 | 896 |
| loop | 28 % → 28 % | 36.3 px | 0.35 | 1.00 | 451 |
| tilted | 13 % → 13 % | 37.3 px | 0.38 | 1.00 | 272 |
| over the wet one | 27 % → 27 % | 37.1 px | 0.38 | 1.00 | 301 |
| long, no reload | 48 % → 48 % | 21.5 px | 0.30 | 1.00 | 1476 | quarters: 0.25 → 0.15 → 0.13 → 0.10

Numbers say: light vs heavy: width 22.5 → 43.4 px, dark 0.33 → 0.36.

## Oil · Henry Ward · HW #03 navy contours over wet band
Oil 1.00 · 46 px · 19.5 s

![Oil · Henry Ward · HW #03 navy contours over wet band](Oil-Henry-Ward-HW-03-navy-contours-over-wet-band.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 8 % → 8 % | 22.5 px | 0.35 | 1.00 | 120 |
| heavy line | 15 % → 15 % | 43.4 px | 0.38 | 1.00 | 201 |
| pressure swell | 11 % → 11 % | 41.0 px | 0.44 | 1.00 | 181 |
| fast wave | 32 % → 33 % | 37.5 px | 0.39 | 1.00 | 482 |
| slow wave | 26 % → 26 % | 30.2 px | 0.36 | 1.00 | 731 |
| spiral | 51 % → 51 % | 33.5 px | 0.32 | 1.00 | 864 |
| loop | 28 % → 28 % | 36.3 px | 0.37 | 1.00 | 387 |
| tilted | 13 % → 13 % | 37.3 px | 0.40 | 1.00 | 362 |
| over the wet one | 27 % → 27 % | 37.1 px | 0.40 | 1.00 | 282 |
| long, no reload | 48 % → 48 % | 21.5 px | 0.32 | 1.00 | 1546 | quarters: 0.26 → 0.16 → 0.14 → 0.10

Numbers say: light vs heavy: width 22.5 → 43.4 px, dark 0.35 → 0.38.

## Oil · Henry Ward · HW #01 peach cloud and legs over teal
Oil 1.00 · 46 px · 19.7 s

![Oil · Henry Ward · HW #01 peach cloud and legs over teal](Oil-Henry-Ward-HW-01-peach-cloud-and-legs-over-teal.png)

A light paint: laid on a grey sheet (on white it cannot be seen); **dark** = how far it is from the grey either way.

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 8 % → 8 % | 22.5 px | 0.23 | 1.00 | 145 |
| heavy line | 15 % → 15 % | 43.4 px | 0.29 | 1.00 | 203 |
| pressure swell | 11 % → 11 % | 41.0 px | 0.24 | 1.00 | 157 |
| fast wave | 32 % → 33 % | 37.5 px | 0.22 | 1.00 | 487 |
| slow wave | 26 % → 26 % | 30.2 px | 0.27 | 1.00 | 764 |
| spiral | 51 % → 51 % | 33.5 px | 0.24 | 1.00 | 1091 |
| loop | 28 % → 28 % | 36.3 px | 0.26 | 1.00 | 586 |
| tilted | 13 % → 13 % | 37.3 px | 0.24 | 1.00 | 289 |
| over the wet one | 27 % → 27 % | 37.1 px | 0.24 | 1.00 | 241 |
| long, no reload | 48 % → 48 % | 21.5 px | 0.24 | 1.00 | 1723 | quarters: 0.00 → 0.00 → 0.00 → 0.00

Numbers say: light vs heavy: width 22.5 → 43.4 px, dark 0.23 → 0.29; the long stroke does not run out of paint.

## Oil · Henry Ward · HW #05 rust, pink, green-black
Oil 1.00 · 46 px · 19.5 s

![Oil · Henry Ward · HW #05 rust, pink, green-black](Oil-Henry-Ward-HW-05-rust-pink-green-black.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 8 % → 8 % | 22.5 px | 0.56 | 1.00 | 161 |
| heavy line | 15 % → 15 % | 43.4 px | 0.56 | 1.00 | 178 |
| pressure swell | 11 % → 11 % | 41.0 px | 0.62 | 1.00 | 147 |
| fast wave | 32 % → 33 % | 37.5 px | 0.58 | 1.00 | 480 |
| slow wave | 26 % → 26 % | 30.2 px | 0.57 | 1.00 | 749 |
| spiral | 51 % → 51 % | 33.5 px | 0.53 | 1.00 | 911 |
| loop | 28 % → 28 % | 36.3 px | 0.57 | 1.00 | 582 |
| tilted | 13 % → 13 % | 37.3 px | 0.59 | 1.00 | 286 |
| over the wet one | 27 % → 27 % | 37.1 px | 0.59 | 1.00 | 258 |
| long, no reload | 48 % → 48 % | 21.5 px | 0.53 | 1.00 | 1870 | quarters: 0.40 → 0.27 → 0.25 → 0.18

Numbers say: light vs heavy: width 22.5 → 43.4 px, dark 0.56 → 0.56.

## Oil · Henry Ward · HW #07 blue L and zigzag on lilac
Oil 1.00 · 50 px · 18.8 s

![Oil · Henry Ward · HW #07 blue L and zigzag on lilac](Oil-Henry-Ward-HW-07-blue-L-and-zigzag-on-lilac.png)

A light paint: laid on a grey sheet (on white it cannot be seen); **dark** = how far it is from the grey either way.

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 5 % → 5 % | 15.0 px | 0.21 | 1.00 | 150 |
| heavy line | 9 % → 9 % | 25.4 px | 0.27 | 1.00 | 195 |
| pressure swell | 7 % → 7 % | 27.5 px | 0.29 | 1.00 | 141 |
| fast wave | 26 % → 26 % | 30.2 px | 0.27 | 1.01 | 548 |
| slow wave | 26 % → 26 % | 29.6 px | 0.28 | 1.00 | 833 |
| spiral | 45 % → 45 % | 29.8 px | 0.23 | 1.00 | 1081 |
| loop | 20 % → 20 % | 26.1 px | 0.28 | 1.00 | 660 |
| tilted | 13 % → 13 % | 35.4 px | 0.25 | 1.00 | 410 |
| over the wet one | 18 % → 18 % | 14.3 px | 0.25 | 1.00 | 276 |
| long, no reload | 31 % → 31 % | 13.7 px | 0.23 | 1.00 | 1744 | quarters: 0.00 → 0.00 → 0.00 → 0.00

Numbers say: light vs heavy: width 15.0 → 25.4 px, dark 0.21 → 0.27; the long stroke does not run out of paint.

## Oil · Henry Ward · HW #08 crown and dark oval
Oil 1.00 · 46 px · 19.5 s

![Oil · Henry Ward · HW #08 crown and dark oval](Oil-Henry-Ward-HW-08-crown-and-dark-oval.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 8 % → 8 % | 22.5 px | 0.21 | 1.00 | 150 |
| heavy line | 15 % → 15 % | 43.4 px | 0.24 | 1.00 | 189 |
| pressure swell | 11 % → 11 % | 41.0 px | 0.30 | 1.00 | 128 |
| fast wave | 32 % → 33 % | 37.5 px | 0.26 | 1.00 | 543 |
| slow wave | 26 % → 26 % | 30.2 px | 0.22 | 1.00 | 1080 |
| spiral | 51 % → 51 % | 33.5 px | 0.19 | 1.00 | 1082 |
| loop | 28 % → 28 % | 36.3 px | 0.23 | 1.00 | 669 |
| tilted | 13 % → 13 % | 37.3 px | 0.27 | 1.00 | 427 |
| over the wet one | 27 % → 27 % | 37.1 px | 0.27 | 1.00 | 385 |
| long, no reload | 48 % → 48 % | 21.5 px | 0.19 | 1.00 | 1763 | quarters: 0.16 → 0.09 → 0.08 → 0.06

Numbers say: light vs heavy: width 22.5 → 43.4 px, dark 0.21 → 0.24.

## Oil · Henry Ward · HW #10 green block over maroon
Oil 1.00 · 46 px · 19.7 s

![Oil · Henry Ward · HW #10 green block over maroon](Oil-Henry-Ward-HW-10-green-block-over-maroon.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 8 % → 8 % | 22.5 px | 0.19 | 1.00 | 157 |
| heavy line | 15 % → 15 % | 43.4 px | 0.21 | 1.00 | 203 |
| pressure swell | 11 % → 11 % | 41.0 px | 0.27 | 1.00 | 133 |
| fast wave | 32 % → 33 % | 37.5 px | 0.24 | 1.00 | 438 |
| slow wave | 26 % → 26 % | 30.2 px | 0.19 | 1.00 | 655 |
| spiral | 51 % → 51 % | 33.5 px | 0.17 | 1.00 | 716 |
| loop | 28 % → 28 % | 36.3 px | 0.21 | 1.00 | 482 |
| tilted | 13 % → 13 % | 37.3 px | 0.24 | 1.00 | 213 |
| over the wet one | 27 % → 27 % | 37.1 px | 0.24 | 1.00 | 154 |
| long, no reload | 48 % → 48 % | 21.5 px | 0.17 | 1.00 | 1270 | quarters: 0.14 → 0.09 → 0.08 → 0.06

Numbers say: light vs heavy: width 22.5 → 43.4 px, dark 0.19 → 0.21.

## Oil · Henry Ward · HW #11 cream mass and purple balls
Oil 1.00 · 46 px · 21.4 s

![Oil · Henry Ward · HW #11 cream mass and purple balls](Oil-Henry-Ward-HW-11-cream-mass-and-purple-balls.png)

A light paint: laid on a grey sheet (on white it cannot be seen); **dark** = how far it is from the grey either way.

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 8 % → 8 % | 22.5 px | 0.29 | 1.00 | 181 |
| heavy line | 15 % → 15 % | 43.4 px | 0.36 | 1.00 | 193 |
| pressure swell | 11 % → 11 % | 41.0 px | 0.31 | 1.00 | 125 |
| fast wave | 32 % → 33 % | 37.5 px | 0.28 | 1.00 | 475 |
| slow wave | 26 % → 26 % | 30.2 px | 0.34 | 1.00 | 716 |
| spiral | 51 % → 51 % | 33.5 px | 0.29 | 1.00 | 817 |
| loop | 28 % → 28 % | 36.3 px | 0.33 | 1.00 | 387 |
| tilted | 13 % → 13 % | 37.3 px | 0.29 | 1.00 | 260 |
| over the wet one | 27 % → 27 % | 37.1 px | 0.29 | 1.00 | 234 |
| long, no reload | 48 % → 48 % | 21.5 px | 0.29 | 1.00 | 1617 | quarters: 0.00 → 0.00 → 0.00 → 0.00

Numbers say: light vs heavy: width 22.5 → 43.4 px, dark 0.29 → 0.36; the long stroke does not run out of paint.

## Oil · Henry Ward · HW #13 blue scrub under red
Oil 1.00 · 46 px · 21.6 s

![Oil · Henry Ward · HW #13 blue scrub under red](Oil-Henry-Ward-HW-13-blue-scrub-under-red.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 8 % → 8 % | 22.5 px | 0.65 | 1.00 | 139 |
| heavy line | 15 % → 15 % | 43.4 px | 0.64 | 1.00 | 185 |
| pressure swell | 11 % → 11 % | 41.0 px | 0.70 | 1.00 | 125 |
| fast wave | 32 % → 33 % | 37.5 px | 0.66 | 1.00 | 541 |
| slow wave | 26 % → 26 % | 30.2 px | 0.65 | 1.00 | 740 |
| spiral | 51 % → 51 % | 33.5 px | 0.62 | 1.00 | 805 |
| loop | 28 % → 28 % | 36.3 px | 0.66 | 1.00 | 393 |
| tilted | 13 % → 13 % | 37.3 px | 0.67 | 1.00 | 266 |
| over the wet one | 27 % → 27 % | 37.1 px | 0.67 | 1.00 | 241 |
| long, no reload | 48 % → 48 % | 21.5 px | 0.62 | 1.00 | 1637 | quarters: 0.45 → 0.32 → 0.29 → 0.22

Numbers say: light vs heavy: width 22.5 → 43.4 px, dark 0.65 → 0.64.

## Oil · Henry Ward · HW #14 olive totem on dark
Oil 1.00 · 46 px · 21.9 s

![Oil · Henry Ward · HW #14 olive totem on dark](Oil-Henry-Ward-HW-14-olive-totem-on-dark.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 8 % → 8 % | 22.5 px | 0.28 | 1.00 | 126 |
| heavy line | 15 % → 15 % | 43.4 px | 0.31 | 1.00 | 158 |
| pressure swell | 11 % → 11 % | 41.0 px | 0.36 | 1.00 | 178 |
| fast wave | 32 % → 33 % | 37.5 px | 0.32 | 1.00 | 463 |
| slow wave | 26 % → 26 % | 30.2 px | 0.28 | 1.00 | 754 |
| spiral | 51 % → 51 % | 33.5 px | 0.25 | 1.00 | 779 |
| loop | 28 % → 28 % | 36.3 px | 0.30 | 1.00 | 497 |
| tilted | 13 % → 13 % | 37.3 px | 0.33 | 1.00 | 240 |
| over the wet one | 27 % → 27 % | 37.1 px | 0.33 | 1.00 | 317 |
| long, no reload | 48 % → 48 % | 21.5 px | 0.25 | 1.00 | 1706 | quarters: 0.21 → 0.13 → 0.11 → 0.08

Numbers say: light vs heavy: width 22.5 → 43.4 px, dark 0.28 → 0.31.

## Oil · Henry Ward · Ground #2b2f1c
Gouache 1.00 · 160 px · 77.3 s

![Oil · Henry Ward · Ground #2b2f1c](Oil-Henry-Ward-Ground-2b2f1c.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 51 % → 46 % | 148.3 px | 0.52 | 0.89 | 675 |
| heavy line | 52 % → 47 % | 151.5 px | 0.52 | 0.91 | 861 |
| pressure swell | 41 % → 45 % | 154.8 px | 0.52 | 1.10 | 599 |
| fast wave | 85 % → 86 % | 97.8 px | 0.52 | 1.01 | 3375 |
| slow wave | 86 % → 73 % | 99.2 px | 0.52 | 0.86 | 7225 |
| spiral | 88 % → 69 % | 58.3 px | 0.52 | 0.77 | 5765 |
| loop | 75 % → 69 % | 97.0 px | 0.52 | 0.92 | 2970 |
| tilted | 39 % → 39 % | 107.5 px | 0.52 | 1.00 | 1130 |
| over the wet one | 76 % → 71 % | 104.6 px | 0.52 | 0.93 | 884 |
| long, no reload | 98 % → 87 % | 44.0 px | 0.52 | 0.88 | 5221 | quarters: 0.52 → 0.52 → 0.52 → 0.50

Numbers say: light vs heavy: width 148.3 → 151.5 px, dark 0.52 → 0.52; pressure barely changes the width; the long stroke does not run out of paint.

## Oil · Henry Ward · Thin veil #2b3a44
Oil 0.81 · Ink 0.19 · 56 px · 41.2 s

![Oil · Henry Ward · Thin veil #2b3a44](Oil-Henry-Ward-Thin-veil-2b3a44.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 6 % → 4 % | 18.8 px | 0.62 | 0.66 | 163 |
| heavy line | 12 % → 12 % | 36.0 px | 0.67 | 0.94 | 244 |
| pressure swell | 10 % → 9 % | 38.2 px | 0.64 | 0.89 | 176 |
| fast wave | 39 % → 32 % | 44.6 px | 0.68 | 0.82 | 536 |
| slow wave | 36 % → 33 % | 42.2 px | 0.66 | 0.91 | 1024 |
| spiral | 61 % → 50 % | 40.4 px | 0.57 | 0.81 | 1407 |
| loop | 28 % → 23 % | 36.3 px | 0.60 | 0.83 | 1026 |
| tilted | 15 % → 15 % | 41.7 px | 0.69 | 1.01 | 539 |
| over the wet one | 24 % → 22 % | 26.1 px | 0.69 | 0.89 | 321 |
| long, no reload | 56 % → 44 % | 24.9 px | 0.56 | 0.79 | 2057 | quarters: 0.40 → 0.25 → 0.23 → 0.22

Numbers say: light vs heavy: width 18.8 → 36.0 px, dark 0.62 → 0.67.

## Oil · Henry Ward · Loaded flat #ece6c0
Oil 1.00 · 46 px · 23.2 s

![Oil · Henry Ward · Loaded flat #ece6c0](Oil-Henry-Ward-Loaded-flat-ece6c0.png)

A light paint: laid on a grey sheet (on white it cannot be seen); **dark** = how far it is from the grey either way.

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 8 % → 8 % | 22.5 px | 0.32 | 1.00 | 123 |
| heavy line | 15 % → 15 % | 43.4 px | 0.39 | 1.00 | 204 |
| pressure swell | 11 % → 11 % | 41.0 px | 0.34 | 1.00 | 127 |
| fast wave | 32 % → 33 % | 37.5 px | 0.31 | 1.00 | 438 |
| slow wave | 26 % → 26 % | 30.2 px | 0.36 | 1.00 | 931 |
| spiral | 51 % → 51 % | 33.5 px | 0.32 | 1.00 | 1186 |
| loop | 28 % → 28 % | 36.3 px | 0.36 | 1.00 | 569 |
| tilted | 13 % → 13 % | 37.3 px | 0.32 | 1.00 | 378 |
| over the wet one | 27 % → 27 % | 37.1 px | 0.32 | 1.00 | 340 |
| long, no reload | 48 % → 48 % | 21.5 px | 0.31 | 1.00 | 2360 | quarters: 0.00 → 0.00 → 0.00 → 0.00

Numbers say: light vs heavy: width 22.5 → 43.4 px, dark 0.32 → 0.39; the long stroke does not run out of paint.

## Oil · Henry Ward · Dry scrub #ece6c0
Oil 1.00 · 50 px · 22.2 s

![Oil · Henry Ward · Dry scrub #ece6c0](Oil-Henry-Ward-Dry-scrub-ece6c0.png)

A light paint: laid on a grey sheet (on white it cannot be seen); **dark** = how far it is from the grey either way.

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 5 % → 5 % | 15.0 px | 0.19 | 1.00 | 253 |
| heavy line | 9 % → 9 % | 25.4 px | 0.25 | 1.00 | 357 |
| pressure swell | 7 % → 7 % | 27.5 px | 0.27 | 1.00 | 229 |
| fast wave | 26 % → 26 % | 30.2 px | 0.25 | 1.01 | 787 |
| slow wave | 26 % → 26 % | 29.6 px | 0.26 | 1.00 | 1287 |
| spiral | 45 % → 45 % | 29.8 px | 0.21 | 1.00 | 1216 |
| loop | 20 % → 20 % | 26.1 px | 0.26 | 1.00 | 555 |
| tilted | 13 % → 13 % | 35.4 px | 0.22 | 1.00 | 257 |
| over the wet one | 18 % → 18 % | 14.3 px | 0.22 | 1.00 | 280 |
| long, no reload | 31 % → 31 % | 13.7 px | 0.21 | 1.00 | 1504 | quarters: 0.00 → 0.00 → 0.00 → 0.00

Numbers say: light vs heavy: width 15.0 → 25.4 px, dark 0.19 → 0.25; the long stroke does not run out of paint.

## Oil · Henry Ward · Ground #8a6a20
Gouache 1.00 · 160 px · 72.9 s

![Oil · Henry Ward · Ground #8a6a20](Oil-Henry-Ward-Ground-8a6a20.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 51 % → 46 % | 148.3 px | 0.32 | 0.89 | 1271 |
| heavy line | 52 % → 47 % | 151.5 px | 0.32 | 0.91 | 1300 |
| pressure swell | 41 % → 45 % | 154.8 px | 0.32 | 1.10 | 924 |
| fast wave | 85 % → 86 % | 97.8 px | 0.33 | 1.01 | 3995 |
| slow wave | 86 % → 73 % | 99.2 px | 0.32 | 0.86 | 5129 |
| spiral | 88 % → 69 % | 58.3 px | 0.32 | 0.77 | 3424 |
| loop | 75 % → 69 % | 97.0 px | 0.32 | 0.92 | 1764 |
| tilted | 39 % → 39 % | 107.5 px | 0.32 | 1.00 | 1073 |
| over the wet one | 76 % → 71 % | 104.6 px | 0.32 | 0.93 | 863 |
| long, no reload | 98 % → 87 % | 44.0 px | 0.32 | 0.88 | 5058 | quarters: 0.32 → 0.32 → 0.32 → 0.29

Numbers say: light vs heavy: width 148.3 → 151.5 px, dark 0.32 → 0.32; pressure barely changes the width; the long stroke does not run out of paint.

## Oil · Henry Ward · Loaded flat #b8bcc0
Oil 1.00 · 46 px · 20.9 s

![Oil · Henry Ward · Loaded flat #b8bcc0](Oil-Henry-Ward-Loaded-flat-b8bcc0.png)

A light paint: laid on a grey sheet (on white it cannot be seen); **dark** = how far it is from the grey either way.

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 8 % → 8 % | 22.5 px | 0.22 | 1.00 | 233 |
| heavy line | 15 % → 15 % | 43.4 px | 0.28 | 1.00 | 273 |
| pressure swell | 11 % → 11 % | 41.0 px | 0.23 | 1.00 | 234 |
| fast wave | 32 % → 33 % | 37.5 px | 0.21 | 1.00 | 672 |
| slow wave | 26 % → 26 % | 30.2 px | 0.26 | 1.00 | 918 |
| spiral | 51 % → 51 % | 33.5 px | 0.23 | 1.00 | 1194 |
| loop | 28 % → 28 % | 36.3 px | 0.25 | 1.00 | 683 |
| tilted | 13 % → 13 % | 37.3 px | 0.23 | 1.00 | 344 |
| over the wet one | 27 % → 27 % | 37.1 px | 0.23 | 1.00 | 367 |
| long, no reload | 48 % → 48 % | 21.5 px | 0.24 | 1.00 | 1756 | quarters: 0.00 → 0.00 → 0.00 → 0.01

Numbers say: light vs heavy: width 22.5 → 43.4 px, dark 0.22 → 0.28; the long stroke does not run out of paint.

## Oil · Henry Ward · Dry scrub #c8ccd0
Oil 1.00 · 50 px · 18.1 s

![Oil · Henry Ward · Dry scrub #c8ccd0](Oil-Henry-Ward-Dry-scrub-c8ccd0.png)

A light paint: laid on a grey sheet (on white it cannot be seen); **dark** = how far it is from the grey either way.

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 5 % → 5 % | 15.0 px | 0.15 | 1.00 | 180 |
| heavy line | 9 % → 9 % | 25.4 px | 0.20 | 1.00 | 298 |
| pressure swell | 7 % → 7 % | 27.5 px | 0.22 | 1.00 | 193 |
| fast wave | 26 % → 26 % | 30.2 px | 0.19 | 1.01 | 774 |
| slow wave | 26 % → 26 % | 29.6 px | 0.21 | 1.00 | 1235 |
| spiral | 45 % → 45 % | 29.8 px | 0.17 | 1.00 | 1120 |
| loop | 20 % → 20 % | 26.1 px | 0.21 | 1.00 | 648 |
| tilted | 13 % → 13 % | 35.4 px | 0.17 | 1.00 | 438 |
| over the wet one | 18 % → 18 % | 14.3 px | 0.17 | 1.00 | 226 |
| long, no reload | 31 % → 31 % | 13.7 px | 0.16 | 1.00 | 1089 | quarters: 0.00 → 0.00 → 0.00 → 0.00

Numbers say: light vs heavy: width 15.0 → 25.4 px, dark 0.15 → 0.20; the long stroke does not run out of paint.

## Oil · Henry Ward · Wet drag #9ea4aa
Oil 1.00 · 44 px · 18.6 s

![Oil · Henry Ward · Wet drag #9ea4aa](Oil-Henry-Ward-Wet-drag-9ea4aa.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 9 % → 9 % | 24.7 px | 0.14 | 1.00 | 280 |
| heavy line | 10 % → 10 % | 28.4 px | 0.23 | 1.00 | 267 |
| pressure swell | 10 % → 10 % | 36.9 px | 0.21 | 1.00 | 177 |
| fast wave | 30 % → 30 % | 34.1 px | 0.27 | 1.00 | 761 |
| slow wave | 32 % → 32 % | 36.5 px | 0.18 | 1.00 | 1083 |
| spiral | 52 % → 52 % | 34.6 px | 0.13 | 1.00 | 1279 |
| loop | 22 % → 22 % | 28.9 px | 0.19 | 1.00 | 626 |
| tilted | 12 % → 12 % | 34.6 px | 0.25 | 1.00 | 321 |
| over the wet one | 24 % → 24 % | 32.9 px | 0.25 | 1.00 | 214 |
| long, no reload | 55 % → 55 % | 24.6 px | 0.14 | 1.00 | 1110 | quarters: 0.13 → 0.09 → 0.07 → 0.05

Numbers say: light vs heavy: width 24.7 → 28.4 px, dark 0.14 → 0.23.

## Oil · Henry Ward · Ground #e8b4a8
Gouache 1.00 · 160 px · 72.8 s

![Oil · Henry Ward · Ground #e8b4a8](Oil-Henry-Ward-Ground-e8b4a8.png)

A light paint: laid on a grey sheet (on white it cannot be seen); **dark** = how far it is from the grey either way.

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 51 % → 46 % | 148.3 px | 0.30 | 0.89 | 1231 |
| heavy line | 52 % → 47 % | 151.5 px | 0.30 | 0.91 | 1246 |
| pressure swell | 41 % → 45 % | 154.8 px | 0.30 | 1.10 | 1062 |
| fast wave | 85 % → 86 % | 97.8 px | 0.29 | 1.01 | 2548 |
| slow wave | 86 % → 73 % | 99.2 px | 0.30 | 0.86 | 3685 |
| spiral | 88 % → 69 % | 58.3 px | 0.30 | 0.77 | 3453 |
| loop | 75 % → 69 % | 97.0 px | 0.30 | 0.92 | 1753 |
| tilted | 39 % → 39 % | 107.5 px | 0.30 | 1.00 | 1006 |
| over the wet one | 76 % → 71 % | 104.6 px | 0.30 | 0.93 | 842 |
| long, no reload | 98 % → 87 % | 44.0 px | 0.30 | 0.88 | 4986 | quarters: 0.00 → 0.00 → 0.00 → 0.00

Numbers say: light vs heavy: width 148.3 → 151.5 px, dark 0.30 → 0.30; pressure barely changes the width.

## Oil · Henry Ward · Loaded flat #6e7f90
Oil 1.00 · 46 px · 16.5 s

![Oil · Henry Ward · Loaded flat #6e7f90](Oil-Henry-Ward-Loaded-flat-6e7f90.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 8 % → 8 % | 22.5 px | 0.33 | 1.00 | 256 |
| heavy line | 15 % → 15 % | 43.4 px | 0.36 | 1.00 | 313 |
| pressure swell | 11 % → 11 % | 41.0 px | 0.42 | 1.00 | 202 |
| fast wave | 32 % → 33 % | 37.5 px | 0.37 | 1.00 | 1006 |
| slow wave | 26 % → 26 % | 30.2 px | 0.34 | 1.00 | 837 |
| spiral | 51 % → 51 % | 33.5 px | 0.30 | 1.00 | 825 |
| loop | 28 % → 28 % | 36.3 px | 0.35 | 1.00 | 400 |
| tilted | 13 % → 13 % | 37.3 px | 0.38 | 1.00 | 258 |
| over the wet one | 27 % → 27 % | 37.1 px | 0.38 | 1.00 | 186 |
| long, no reload | 48 % → 48 % | 21.5 px | 0.30 | 1.00 | 971 | quarters: 0.25 → 0.15 → 0.13 → 0.10

Numbers say: light vs heavy: width 22.5 → 43.4 px, dark 0.33 → 0.36.

## Oil · Henry Ward · Loaded flat #f6f6f2
Oil 1.00 · 46 px · 15.0 s

![Oil · Henry Ward · Loaded flat #f6f6f2](Oil-Henry-Ward-Loaded-flat-f6f6f2.png)

A light paint: laid on a grey sheet (on white it cannot be seen); **dark** = how far it is from the grey either way.

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 8 % → 8 % | 22.5 px | 0.36 | 1.00 | 131 |
| heavy line | 15 % → 15 % | 43.4 px | 0.43 | 1.00 | 175 |
| pressure swell | 11 % → 11 % | 41.0 px | 0.38 | 1.00 | 114 |
| fast wave | 32 % → 33 % | 37.5 px | 0.34 | 1.00 | 438 |
| slow wave | 26 % → 26 % | 30.2 px | 0.40 | 1.00 | 649 |
| spiral | 51 % → 51 % | 33.5 px | 0.35 | 1.00 | 760 |
| loop | 28 % → 28 % | 36.3 px | 0.39 | 1.00 | 384 |
| tilted | 13 % → 13 % | 37.3 px | 0.36 | 1.00 | 241 |
| over the wet one | 27 % → 27 % | 37.1 px | 0.36 | 1.00 | 182 |
| long, no reload | 48 % → 48 % | 21.5 px | 0.34 | 1.00 | 1042 | quarters: 0.00 → 0.00 → 0.00 → 0.00

Numbers say: light vs heavy: width 22.5 → 43.4 px, dark 0.36 → 0.43; the long stroke does not run out of paint.

## Oil · Henry Ward · Dry scrub #f6f6f2
Oil 1.00 · 50 px · 13.8 s

![Oil · Henry Ward · Dry scrub #f6f6f2](Oil-Henry-Ward-Dry-scrub-f6f6f2.png)

A light paint: laid on a grey sheet (on white it cannot be seen); **dark** = how far it is from the grey either way.

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 5 % → 5 % | 15.0 px | 0.22 | 1.00 | 112 |
| heavy line | 9 % → 9 % | 25.4 px | 0.28 | 1.00 | 167 |
| pressure swell | 7 % → 7 % | 27.5 px | 0.30 | 1.00 | 114 |
| fast wave | 26 % → 26 % | 30.2 px | 0.28 | 1.01 | 418 |
| slow wave | 26 % → 26 % | 29.6 px | 0.29 | 1.00 | 686 |
| spiral | 45 % → 45 % | 29.8 px | 0.24 | 1.00 | 729 |
| loop | 20 % → 20 % | 26.1 px | 0.29 | 1.00 | 371 |
| tilted | 13 % → 13 % | 35.4 px | 0.26 | 1.00 | 242 |
| over the wet one | 18 % → 18 % | 14.3 px | 0.26 | 1.00 | 159 |
| long, no reload | 31 % → 31 % | 13.7 px | 0.24 | 1.00 | 927 | quarters: 0.00 → 0.00 → 0.00 → 0.00

Numbers say: light vs heavy: width 15.0 → 25.4 px, dark 0.22 → 0.28; the long stroke does not run out of paint.

## Oil · Henry Ward · Ground #e8e2da
Gouache 1.00 · 160 px · 74.1 s

![Oil · Henry Ward · Ground #e8e2da](Oil-Henry-Ward-Ground-e8e2da.png)

A light paint: laid on a grey sheet (on white it cannot be seen); **dark** = how far it is from the grey either way.

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 51 % → 46 % | 148.3 px | 0.38 | 0.89 | 680 |
| heavy line | 52 % → 47 % | 151.5 px | 0.38 | 0.91 | 761 |
| pressure swell | 41 % → 45 % | 154.8 px | 0.38 | 1.10 | 583 |
| fast wave | 85 % → 86 % | 97.8 px | 0.37 | 1.01 | 2192 |
| slow wave | 86 % → 73 % | 99.2 px | 0.38 | 0.86 | 3573 |
| spiral | 88 % → 69 % | 58.3 px | 0.38 | 0.77 | 3347 |
| loop | 75 % → 69 % | 97.0 px | 0.38 | 0.92 | 1621 |
| tilted | 39 % → 39 % | 107.5 px | 0.38 | 1.00 | 1016 |
| over the wet one | 76 % → 71 % | 104.6 px | 0.38 | 0.93 | 801 |
| long, no reload | 98 % → 87 % | 44.0 px | 0.38 | 0.88 | 4878 | quarters: 0.00 → 0.00 → 0.00 → 0.00

Numbers say: light vs heavy: width 148.3 → 151.5 px, dark 0.38 → 0.38; pressure barely changes the width.

## Oil · Henry Ward · Loaded flat #6a7a80
Oil 1.00 · 46 px · 14.3 s

![Oil · Henry Ward · Loaded flat #6a7a80](Oil-Henry-Ward-Loaded-flat-6a7a80.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 8 % → 8 % | 22.5 px | 0.35 | 1.00 | 139 |
| heavy line | 15 % → 15 % | 43.4 px | 0.38 | 1.00 | 164 |
| pressure swell | 11 % → 11 % | 41.0 px | 0.44 | 1.00 | 144 |
| fast wave | 32 % → 33 % | 37.5 px | 0.39 | 1.00 | 434 |
| slow wave | 26 % → 26 % | 30.2 px | 0.36 | 1.00 | 641 |
| spiral | 51 % → 51 % | 33.5 px | 0.32 | 1.00 | 750 |
| loop | 28 % → 28 % | 36.3 px | 0.37 | 1.00 | 402 |
| tilted | 13 % → 13 % | 37.3 px | 0.40 | 1.00 | 216 |
| over the wet one | 27 % → 27 % | 37.1 px | 0.40 | 1.00 | 183 |
| long, no reload | 48 % → 48 % | 21.5 px | 0.32 | 1.00 | 1006 | quarters: 0.26 → 0.16 → 0.14 → 0.10

Numbers say: light vs heavy: width 22.5 → 43.4 px, dark 0.35 → 0.38.

## Oil · Henry Ward · Loaded flat #5a1810
Oil 1.00 · 46 px · 14.2 s

![Oil · Henry Ward · Loaded flat #5a1810](Oil-Henry-Ward-Loaded-flat-5a1810.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 8 % → 8 % | 22.5 px | 0.74 | 1.00 | 150 |
| heavy line | 15 % → 15 % | 43.4 px | 0.71 | 1.00 | 166 |
| pressure swell | 11 % → 11 % | 41.0 px | 0.78 | 1.00 | 110 |
| fast wave | 32 % → 33 % | 37.5 px | 0.74 | 1.00 | 466 |
| slow wave | 26 % → 26 % | 30.2 px | 0.74 | 1.00 | 656 |
| spiral | 51 % → 51 % | 33.5 px | 0.70 | 1.00 | 762 |
| loop | 28 % → 28 % | 36.3 px | 0.74 | 1.00 | 358 |
| tilted | 13 % → 13 % | 37.3 px | 0.75 | 1.00 | 211 |
| over the wet one | 27 % → 27 % | 37.1 px | 0.75 | 1.00 | 167 |
| long, no reload | 48 % → 48 % | 21.5 px | 0.70 | 1.00 | 966 | quarters: 0.51 → 0.37 → 0.34 → 0.25

Numbers say: light vs heavy: width 22.5 → 43.4 px, dark 0.74 → 0.71.

## Oil · Henry Ward · Dirty contour #1c2240
Oil 1.00 · 24 px · 12.0 s

![Oil · Henry Ward · Dirty contour #1c2240](Oil-Henry-Ward-Dirty-contour-1c2240.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 8 % → 8 % | 22.0 px | 0.74 | 1.00 | 85 |
| heavy line | 8 % → 8 % | 24.5 px | 0.74 | 1.00 | 81 |
| pressure swell | 7 % → 7 % | 27.1 px | 0.77 | 1.00 | 69 |
| fast wave | 19 % → 19 % | 22.1 px | 0.79 | 1.00 | 255 |
| slow wave | 21 % → 21 % | 24.2 px | 0.75 | 1.00 | 437 |
| spiral | 31 % → 31 % | 20.7 px | 0.75 | 1.00 | 428 |
| loop | 17 % → 17 % | 21.6 px | 0.76 | 1.00 | 241 |
| tilted | 9 % → 9 % | 26.2 px | 0.76 | 1.00 | 133 |
| over the wet one | 18 % → 18 % | 22.7 px | 0.76 | 1.00 | 111 |
| long, no reload | 41 % → 41 % | 18.4 px | 0.69 | 1.00 | 632 | quarters: 0.41 → 0.35 → 0.28 → 0.23

Numbers say: light vs heavy: width 22.0 → 24.5 px, dark 0.74 → 0.74.

## Oil · Henry Ward · Ground #22403f
Gouache 1.00 · 160 px · 80.0 s

![Oil · Henry Ward · Ground #22403f](Oil-Henry-Ward-Ground-22403f.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 51 % → 46 % | 148.3 px | 0.48 | 0.89 | 672 |
| heavy line | 52 % → 47 % | 151.5 px | 0.48 | 0.91 | 816 |
| pressure swell | 41 % → 45 % | 154.8 px | 0.48 | 1.10 | 597 |
| fast wave | 85 % → 86 % | 97.8 px | 0.48 | 1.01 | 2152 |
| slow wave | 86 % → 73 % | 99.2 px | 0.48 | 0.86 | 3688 |
| spiral | 88 % → 69 % | 58.3 px | 0.48 | 0.77 | 3396 |
| loop | 75 % → 69 % | 97.0 px | 0.48 | 0.92 | 1697 |
| tilted | 39 % → 39 % | 107.5 px | 0.48 | 1.00 | 1012 |
| over the wet one | 76 % → 71 % | 104.6 px | 0.48 | 0.93 | 897 |
| long, no reload | 98 % → 87 % | 44.0 px | 0.48 | 0.88 | 5292 | quarters: 0.48 → 0.48 → 0.48 → 0.46

Numbers say: light vs heavy: width 148.3 → 151.5 px, dark 0.48 → 0.48; pressure barely changes the width; the long stroke does not run out of paint.

## Oil · Henry Ward · Loaded flat #f0b89a
Oil 1.00 · 46 px · 14.2 s

![Oil · Henry Ward · Loaded flat #f0b89a](Oil-Henry-Ward-Loaded-flat-f0b89a.png)

A light paint: laid on a grey sheet (on white it cannot be seen); **dark** = how far it is from the grey either way.

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 8 % → 8 % | 22.5 px | 0.23 | 1.00 | 131 |
| heavy line | 15 % → 15 % | 43.4 px | 0.29 | 1.00 | 170 |
| pressure swell | 11 % → 11 % | 41.0 px | 0.24 | 1.00 | 118 |
| fast wave | 32 % → 33 % | 37.5 px | 0.22 | 1.00 | 410 |
| slow wave | 26 % → 26 % | 30.2 px | 0.27 | 1.00 | 620 |
| spiral | 51 % → 51 % | 33.5 px | 0.24 | 1.00 | 712 |
| loop | 28 % → 28 % | 36.3 px | 0.26 | 1.00 | 367 |
| tilted | 13 % → 13 % | 37.3 px | 0.24 | 1.00 | 203 |
| over the wet one | 27 % → 27 % | 37.1 px | 0.24 | 1.00 | 171 |
| long, no reload | 48 % → 48 % | 21.5 px | 0.24 | 1.00 | 952 | quarters: 0.00 → 0.00 → 0.00 → 0.00

Numbers say: light vs heavy: width 22.5 → 43.4 px, dark 0.23 → 0.29; the long stroke does not run out of paint.

## Oil · Henry Ward · Dry scrub #f0b89a
Oil 1.00 · 50 px · 13.3 s

![Oil · Henry Ward · Dry scrub #f0b89a](Oil-Henry-Ward-Dry-scrub-f0b89a.png)

A light paint: laid on a grey sheet (on white it cannot be seen); **dark** = how far it is from the grey either way.

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 5 % → 5 % | 15.0 px | 0.13 | 1.00 | 124 |
| heavy line | 9 % → 9 % | 25.4 px | 0.18 | 1.00 | 154 |
| pressure swell | 7 % → 7 % | 27.5 px | 0.19 | 1.00 | 103 |
| fast wave | 26 % → 26 % | 30.2 px | 0.17 | 1.01 | 401 |
| slow wave | 26 % → 26 % | 29.6 px | 0.19 | 1.00 | 662 |
| spiral | 45 % → 45 % | 29.8 px | 0.15 | 1.00 | 716 |
| loop | 20 % → 20 % | 26.1 px | 0.19 | 1.00 | 357 |
| tilted | 13 % → 13 % | 35.4 px | 0.14 | 1.00 | 208 |
| over the wet one | 18 % → 18 % | 14.3 px | 0.14 | 1.00 | 167 |
| long, no reload | 31 % → 31 % | 13.7 px | 0.14 | 1.00 | 889 | quarters: 0.00 → 0.00 → 0.00 → 0.00

Numbers say: light vs heavy: width 15.0 → 25.4 px, dark 0.13 → 0.18; the long stroke does not run out of paint.

## Oil · Henry Ward · Dirty contour #1c2238
Oil 1.00 · 24 px · 12.1 s

![Oil · Henry Ward · Dirty contour #1c2238](Oil-Henry-Ward-Dirty-contour-1c2238.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 8 % → 8 % | 22.0 px | 0.75 | 1.00 | 78 |
| heavy line | 8 % → 8 % | 24.5 px | 0.74 | 1.00 | 93 |
| pressure swell | 7 % → 7 % | 27.1 px | 0.77 | 1.00 | 81 |
| fast wave | 19 % → 19 % | 22.1 px | 0.80 | 1.00 | 234 |
| slow wave | 21 % → 21 % | 24.2 px | 0.75 | 1.00 | 402 |
| spiral | 31 % → 31 % | 20.7 px | 0.75 | 1.00 | 448 |
| loop | 17 % → 17 % | 21.6 px | 0.76 | 1.00 | 209 |
| tilted | 9 % → 9 % | 26.2 px | 0.76 | 1.00 | 116 |
| over the wet one | 18 % → 18 % | 22.7 px | 0.76 | 1.00 | 102 |
| long, no reload | 41 % → 41 % | 18.4 px | 0.69 | 1.00 | 652 | quarters: 0.42 → 0.35 → 0.28 → 0.23

Numbers say: light vs heavy: width 22.0 → 24.5 px, dark 0.75 → 0.74.

## Oil · Henry Ward · Ground #ece8e2
Gouache 1.00 · 160 px · 83.7 s

![Oil · Henry Ward · Ground #ece8e2](Oil-Henry-Ward-Ground-ece8e2.png)

A light paint: laid on a grey sheet (on white it cannot be seen); **dark** = how far it is from the grey either way.

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 51 % → 46 % | 148.3 px | 0.39 | 0.89 | 625 |
| heavy line | 52 % → 47 % | 151.5 px | 0.39 | 0.91 | 761 |
| pressure swell | 41 % → 45 % | 154.8 px | 0.39 | 1.10 | 538 |
| fast wave | 85 % → 86 % | 97.8 px | 0.38 | 1.01 | 2054 |
| slow wave | 86 % → 73 % | 99.2 px | 0.39 | 0.86 | 3495 |
| spiral | 88 % → 69 % | 58.3 px | 0.39 | 0.77 | 3252 |
| loop | 75 % → 69 % | 97.0 px | 0.39 | 0.92 | 1622 |
| tilted | 39 % → 39 % | 107.5 px | 0.39 | 1.00 | 955 |
| over the wet one | 76 % → 71 % | 104.6 px | 0.39 | 0.93 | 1022 |
| long, no reload | 98 % → 87 % | 44.0 px | 0.39 | 0.88 | 5168 | quarters: 0.00 → 0.00 → 0.00 → 0.00

Numbers say: light vs heavy: width 148.3 → 151.5 px, dark 0.39 → 0.39; pressure barely changes the width.

## Oil · Henry Ward · Loaded flat #a03c1c
Oil 1.00 · 46 px · 14.4 s

![Oil · Henry Ward · Loaded flat #a03c1c](Oil-Henry-Ward-Loaded-flat-a03c1c.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 8 % → 8 % | 22.5 px | 0.56 | 1.00 | 143 |
| heavy line | 15 % → 15 % | 43.4 px | 0.56 | 1.00 | 157 |
| pressure swell | 11 % → 11 % | 41.0 px | 0.62 | 1.00 | 116 |
| fast wave | 32 % → 33 % | 37.5 px | 0.58 | 1.00 | 410 |
| slow wave | 26 % → 26 % | 30.2 px | 0.57 | 1.00 | 662 |
| spiral | 51 % → 51 % | 33.5 px | 0.53 | 1.00 | 713 |
| loop | 28 % → 28 % | 36.3 px | 0.57 | 1.00 | 354 |
| tilted | 13 % → 13 % | 37.3 px | 0.59 | 1.00 | 223 |
| over the wet one | 27 % → 27 % | 37.1 px | 0.59 | 1.00 | 172 |
| long, no reload | 48 % → 48 % | 21.5 px | 0.53 | 1.00 | 984 | quarters: 0.40 → 0.27 → 0.25 → 0.18

Numbers say: light vs heavy: width 22.5 → 43.4 px, dark 0.56 → 0.56.

## Oil · Henry Ward · Dirty contour #1f3a2c
Oil 1.00 · 24 px · 12.2 s

![Oil · Henry Ward · Dirty contour #1f3a2c](Oil-Henry-Ward-Dirty-contour-1f3a2c.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 8 % → 8 % | 22.0 px | 0.68 | 1.00 | 79 |
| heavy line | 8 % → 8 % | 24.5 px | 0.67 | 1.00 | 91 |
| pressure swell | 7 % → 7 % | 27.1 px | 0.70 | 1.00 | 82 |
| fast wave | 19 % → 19 % | 22.1 px | 0.72 | 1.00 | 284 |
| slow wave | 21 % → 21 % | 24.2 px | 0.68 | 1.00 | 407 |
| spiral | 31 % → 31 % | 20.7 px | 0.67 | 1.00 | 427 |
| loop | 17 % → 17 % | 21.6 px | 0.69 | 1.00 | 214 |
| tilted | 9 % → 9 % | 26.2 px | 0.70 | 1.00 | 115 |
| over the wet one | 18 % → 18 % | 22.7 px | 0.70 | 1.00 | 109 |
| long, no reload | 41 % → 41 % | 18.4 px | 0.61 | 1.00 | 722 | quarters: 0.38 → 0.31 → 0.24 → 0.19

Numbers say: light vs heavy: width 22.0 → 24.5 px, dark 0.68 → 0.67.

## Oil · Henry Ward · Loaded flat #ecc8c8
Oil 1.00 · 46 px · 14.1 s

![Oil · Henry Ward · Loaded flat #ecc8c8](Oil-Henry-Ward-Loaded-flat-ecc8c8.png)

A light paint: laid on a grey sheet (on white it cannot be seen); **dark** = how far it is from the grey either way.

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 8 % → 8 % | 22.5 px | 0.27 | 1.00 | 131 |
| heavy line | 15 % → 15 % | 43.4 px | 0.34 | 1.00 | 153 |
| pressure swell | 11 % → 11 % | 41.0 px | 0.28 | 1.00 | 121 |
| fast wave | 32 % → 33 % | 37.5 px | 0.26 | 1.00 | 365 |
| slow wave | 26 % → 26 % | 30.2 px | 0.31 | 1.00 | 576 |
| spiral | 51 % → 51 % | 33.5 px | 0.27 | 1.00 | 693 |
| loop | 28 % → 28 % | 36.3 px | 0.30 | 1.00 | 396 |
| tilted | 13 % → 13 % | 37.3 px | 0.27 | 1.00 | 208 |
| over the wet one | 27 % → 27 % | 37.1 px | 0.27 | 1.00 | 169 |
| long, no reload | 48 % → 48 % | 21.5 px | 0.28 | 1.00 | 953 | quarters: 0.00 → 0.00 → 0.00 → 0.00

Numbers say: light vs heavy: width 22.5 → 43.4 px, dark 0.27 → 0.34; the long stroke does not run out of paint.

## Oil · Henry Ward · Loaded flat #62c8e8
Oil 1.00 · 46 px · 14.0 s

![Oil · Henry Ward · Loaded flat #62c8e8](Oil-Henry-Ward-Loaded-flat-62c8e8.png)

A light paint: laid on a grey sheet (on white it cannot be seen); **dark** = how far it is from the grey either way.

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 8 % → 8 % | 22.5 px | 0.18 | 1.00 | 127 |
| heavy line | 15 % → 15 % | 43.4 px | 0.23 | 1.00 | 162 |
| pressure swell | 11 % → 11 % | 41.0 px | 0.18 | 1.00 | 122 |
| fast wave | 32 % → 33 % | 37.5 px | 0.16 | 1.00 | 456 |
| slow wave | 26 % → 26 % | 30.2 px | 0.21 | 1.00 | 622 |
| spiral | 51 % → 51 % | 33.5 px | 0.19 | 1.00 | 718 |
| loop | 28 % → 28 % | 36.3 px | 0.20 | 1.00 | 369 |
| tilted | 13 % → 13 % | 37.3 px | 0.18 | 1.00 | 207 |
| over the wet one | 27 % → 27 % | 37.1 px | 0.18 | 1.00 | 170 |
| long, no reload | 48 % → 48 % | 21.5 px | 0.19 | 1.00 | 946 | quarters: 0.01 → 0.01 → 0.01 → 0.01

Numbers say: light vs heavy: width 22.5 → 43.4 px, dark 0.18 → 0.23; the long stroke does not run out of paint.

## Oil · Henry Ward · Loaded flat #0f2018
Oil 1.00 · 46 px · 14.3 s

![Oil · Henry Ward · Loaded flat #0f2018](Oil-Henry-Ward-Loaded-flat-0f2018.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 8 % → 8 % | 22.5 px | 0.78 | 1.00 | 137 |
| heavy line | 15 % → 15 % | 43.4 px | 0.75 | 1.00 | 155 |
| pressure swell | 11 % → 11 % | 41.0 px | 0.82 | 1.00 | 113 |
| fast wave | 32 % → 33 % | 37.5 px | 0.78 | 1.00 | 408 |
| slow wave | 26 % → 26 % | 30.2 px | 0.77 | 1.00 | 647 |
| spiral | 51 % → 51 % | 33.5 px | 0.74 | 1.00 | 691 |
| loop | 28 % → 28 % | 36.3 px | 0.78 | 1.00 | 376 |
| tilted | 13 % → 13 % | 37.3 px | 0.79 | 1.00 | 217 |
| over the wet one | 27 % → 27 % | 37.1 px | 0.79 | 1.00 | 170 |
| long, no reload | 48 % → 48 % | 21.5 px | 0.75 | 1.00 | 986 | quarters: 0.53 → 0.39 → 0.36 → 0.27

Numbers say: light vs heavy: width 22.5 → 43.4 px, dark 0.78 → 0.75.

## Oil · Henry Ward · Ground #e6e2ee
Gouache 1.00 · 160 px · 91.1 s

![Oil · Henry Ward · Ground #e6e2ee](Oil-Henry-Ward-Ground-e6e2ee.png)

A light paint: laid on a grey sheet (on white it cannot be seen); **dark** = how far it is from the grey either way.

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 51 % → 46 % | 148.3 px | 0.39 | 0.89 | 663 |
| heavy line | 52 % → 47 % | 151.5 px | 0.39 | 0.91 | 871 |
| pressure swell | 41 % → 45 % | 154.8 px | 0.38 | 1.10 | 577 |
| fast wave | 85 % → 86 % | 97.8 px | 0.37 | 1.01 | 2085 |
| slow wave | 86 % → 73 % | 99.2 px | 0.38 | 0.86 | 3997 |
| spiral | 88 % → 69 % | 58.3 px | 0.38 | 0.77 | 5180 |
| loop | 75 % → 69 % | 97.0 px | 0.38 | 0.92 | 1865 |
| tilted | 39 % → 39 % | 107.5 px | 0.38 | 1.00 | 1497 |
| over the wet one | 76 % → 71 % | 104.6 px | 0.38 | 0.93 | 2118 |
| long, no reload | 98 % → 87 % | 44.0 px | 0.38 | 0.88 | 7784 | quarters: 0.00 → 0.00 → 0.00 → 0.00

Numbers say: light vs heavy: width 148.3 → 151.5 px, dark 0.39 → 0.39; pressure barely changes the width.

## Oil · Henry Ward · Dry scrub #f2f0f6
Oil 1.00 · 50 px · 15.2 s

![Oil · Henry Ward · Dry scrub #f2f0f6](Oil-Henry-Ward-Dry-scrub-f2f0f6.png)

A light paint: laid on a grey sheet (on white it cannot be seen); **dark** = how far it is from the grey either way.

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 5 % → 5 % | 15.0 px | 0.21 | 1.00 | 132 |
| heavy line | 9 % → 9 % | 25.4 px | 0.27 | 1.00 | 198 |
| pressure swell | 7 % → 7 % | 27.5 px | 0.29 | 1.00 | 118 |
| fast wave | 26 % → 26 % | 30.2 px | 0.27 | 1.01 | 370 |
| slow wave | 26 % → 26 % | 29.6 px | 0.28 | 1.00 | 610 |
| spiral | 45 % → 45 % | 29.8 px | 0.23 | 1.00 | 703 |
| loop | 20 % → 20 % | 26.1 px | 0.28 | 1.00 | 322 |
| tilted | 13 % → 13 % | 35.4 px | 0.25 | 1.00 | 211 |
| over the wet one | 18 % → 18 % | 14.3 px | 0.25 | 1.00 | 167 |
| long, no reload | 31 % → 31 % | 13.7 px | 0.23 | 1.00 | 855 | quarters: 0.00 → 0.00 → 0.00 → 0.00

Numbers say: light vs heavy: width 15.0 → 25.4 px, dark 0.21 → 0.27; the long stroke does not run out of paint.

## Oil · Henry Ward · Dirty contour #1e4a78
Oil 1.00 · 24 px · 15.2 s

![Oil · Henry Ward · Dirty contour #1e4a78](Oil-Henry-Ward-Dirty-contour-1e4a78.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 8 % → 8 % | 22.0 px | 0.62 | 1.00 | 101 |
| heavy line | 8 % → 8 % | 24.5 px | 0.61 | 1.00 | 94 |
| pressure swell | 7 % → 7 % | 27.1 px | 0.64 | 1.00 | 72 |
| fast wave | 19 % → 19 % | 22.1 px | 0.65 | 1.00 | 228 |
| slow wave | 21 % → 21 % | 24.2 px | 0.61 | 1.00 | 406 |
| spiral | 31 % → 31 % | 20.7 px | 0.60 | 1.00 | 446 |
| loop | 17 % → 17 % | 21.6 px | 0.62 | 1.00 | 255 |
| tilted | 9 % → 9 % | 26.2 px | 0.63 | 1.00 | 138 |
| over the wet one | 18 % → 18 % | 22.7 px | 0.63 | 1.00 | 105 |
| long, no reload | 41 % → 41 % | 18.4 px | 0.53 | 1.00 | 694 | quarters: 0.34 → 0.27 → 0.21 → 0.16

Numbers say: light vs heavy: width 22.0 → 24.5 px, dark 0.62 → 0.61.

## Oil · Henry Ward · Dirty contour #141414
Oil 1.00 · 24 px · 15.1 s

![Oil · Henry Ward · Dirty contour #141414](Oil-Henry-Ward-Dirty-contour-141414.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 8 % → 8 % | 22.0 px | 0.81 | 1.00 | 86 |
| heavy line | 8 % → 8 % | 24.5 px | 0.80 | 1.00 | 98 |
| pressure swell | 7 % → 7 % | 27.1 px | 0.84 | 1.00 | 72 |
| fast wave | 19 % → 19 % | 22.1 px | 0.85 | 1.00 | 255 |
| slow wave | 21 % → 21 % | 24.2 px | 0.83 | 1.00 | 412 |
| spiral | 31 % → 31 % | 20.7 px | 0.83 | 1.00 | 510 |
| loop | 17 % → 17 % | 21.6 px | 0.82 | 1.00 | 228 |
| tilted | 9 % → 9 % | 26.2 px | 0.82 | 1.00 | 114 |
| over the wet one | 18 % → 18 % | 22.7 px | 0.82 | 1.00 | 117 |
| long, no reload | 41 % → 41 % | 18.4 px | 0.78 | 1.00 | 711 | quarters: 0.45 → 0.39 → 0.33 → 0.27

Numbers say: light vs heavy: width 22.0 → 24.5 px, dark 0.81 → 0.80.

## Oil · Henry Ward · Dry scrub #c89038
Oil 1.00 · 50 px · 18.4 s

![Oil · Henry Ward · Dry scrub #c89038](Oil-Henry-Ward-Dry-scrub-c89038.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 5 % → 5 % | 15.0 px | 0.17 | 1.00 | 145 |
| heavy line | 9 % → 9 % | 25.4 px | 0.21 | 1.00 | 171 |
| pressure swell | 7 % → 7 % | 27.5 px | 0.24 | 1.00 | 116 |
| fast wave | 26 % → 26 % | 30.2 px | 0.29 | 1.01 | 449 |
| slow wave | 26 % → 26 % | 29.6 px | 0.20 | 1.00 | 781 |
| spiral | 45 % → 45 % | 29.8 px | 0.18 | 1.00 | 952 |
| loop | 20 % → 20 % | 26.1 px | 0.20 | 1.00 | 427 |
| tilted | 13 % → 13 % | 35.4 px | 0.30 | 1.00 | 403 |
| over the wet one | 18 % → 18 % | 14.3 px | 0.30 | 1.00 | 284 |
| long, no reload | 31 % → 31 % | 13.7 px | 0.21 | 1.00 | 1460 | quarters: 0.08 → 0.07 → 0.06 → 0.06

Numbers say: light vs heavy: width 15.0 → 25.4 px, dark 0.17 → 0.21.

## Oil · Henry Ward · Ground #efe8b8
Gouache 1.00 · 160 px · 95.1 s

![Oil · Henry Ward · Ground #efe8b8](Oil-Henry-Ward-Ground-efe8b8.png)

A light paint: laid on a grey sheet (on white it cannot be seen); **dark** = how far it is from the grey either way.

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 51 % → 46 % | 148.3 px | 0.39 | 0.89 | 796 |
| heavy line | 52 % → 47 % | 151.5 px | 0.39 | 0.91 | 1017 |
| pressure swell | 41 % → 45 % | 154.8 px | 0.38 | 1.10 | 1096 |
| fast wave | 85 % → 86 % | 97.8 px | 0.38 | 1.01 | 2798 |
| slow wave | 86 % → 73 % | 99.2 px | 0.39 | 0.86 | 5281 |
| spiral | 88 % → 69 % | 58.3 px | 0.38 | 0.77 | 5148 |
| loop | 75 % → 69 % | 97.0 px | 0.39 | 0.92 | 2611 |
| tilted | 39 % → 39 % | 107.5 px | 0.38 | 1.00 | 1218 |
| over the wet one | 76 % → 71 % | 104.6 px | 0.38 | 0.93 | 1403 |
| long, no reload | 98 % → 87 % | 44.0 px | 0.38 | 0.88 | 7630 | quarters: 0.00 → 0.00 → 0.00 → 0.00

Numbers say: light vs heavy: width 148.3 → 151.5 px, dark 0.39 → 0.39; pressure barely changes the width.

## Oil · Henry Ward · Loaded flat #a89ac8
Oil 1.00 · 46 px · 21.2 s

![Oil · Henry Ward · Loaded flat #a89ac8](Oil-Henry-Ward-Loaded-flat-a89ac8.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 8 % → 8 % | 22.5 px | 0.21 | 1.00 | 257 |
| heavy line | 15 % → 15 % | 43.4 px | 0.24 | 1.00 | 216 |
| pressure swell | 11 % → 11 % | 41.0 px | 0.30 | 1.00 | 237 |
| fast wave | 32 % → 33 % | 37.5 px | 0.26 | 1.00 | 882 |
| slow wave | 26 % → 26 % | 30.2 px | 0.22 | 1.00 | 674 |
| spiral | 51 % → 51 % | 33.5 px | 0.19 | 1.00 | 734 |
| loop | 28 % → 28 % | 36.3 px | 0.23 | 1.00 | 434 |
| tilted | 13 % → 13 % | 37.3 px | 0.27 | 1.00 | 333 |
| over the wet one | 27 % → 27 % | 37.1 px | 0.27 | 1.00 | 231 |
| long, no reload | 48 % → 48 % | 21.5 px | 0.19 | 1.00 | 1602 | quarters: 0.16 → 0.09 → 0.08 → 0.06

Numbers say: light vs heavy: width 22.5 → 43.4 px, dark 0.21 → 0.24.

## Oil · Henry Ward · Dirty contour #2a2418
Oil 1.00 · 24 px · 18.2 s

![Oil · Henry Ward · Dirty contour #2a2418](Oil-Henry-Ward-Dirty-contour-2a2418.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 8 % → 8 % | 22.0 px | 0.74 | 1.00 | 169 |
| heavy line | 8 % → 8 % | 24.5 px | 0.73 | 1.00 | 129 |
| pressure swell | 7 % → 7 % | 27.1 px | 0.76 | 1.00 | 72 |
| fast wave | 19 % → 19 % | 22.1 px | 0.77 | 1.00 | 257 |
| slow wave | 21 % → 21 % | 24.2 px | 0.74 | 1.00 | 415 |
| spiral | 31 % → 31 % | 20.7 px | 0.74 | 1.00 | 525 |
| loop | 17 % → 17 % | 21.6 px | 0.75 | 1.00 | 323 |
| tilted | 9 % → 9 % | 26.2 px | 0.75 | 1.00 | 129 |
| over the wet one | 18 % → 18 % | 22.7 px | 0.75 | 1.00 | 115 |
| long, no reload | 41 % → 41 % | 18.4 px | 0.68 | 1.00 | 1061 | quarters: 0.41 → 0.34 → 0.28 → 0.22

Numbers say: light vs heavy: width 22.0 → 24.5 px, dark 0.74 → 0.73.

## Oil · Henry Ward · Loaded flat #2a2418
Oil 1.00 · 46 px · 21.8 s

![Oil · Henry Ward · Loaded flat #2a2418](Oil-Henry-Ward-Loaded-flat-2a2418.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 8 % → 8 % | 22.5 px | 0.73 | 1.00 | 131 |
| heavy line | 15 % → 15 % | 43.4 px | 0.71 | 1.00 | 175 |
| pressure swell | 11 % → 11 % | 41.0 px | 0.77 | 1.00 | 127 |
| fast wave | 32 % → 33 % | 37.5 px | 0.74 | 1.00 | 448 |
| slow wave | 26 % → 26 % | 30.2 px | 0.72 | 1.00 | 989 |
| spiral | 51 % → 51 % | 33.5 px | 0.69 | 1.00 | 918 |
| loop | 28 % → 28 % | 36.3 px | 0.73 | 1.00 | 626 |
| tilted | 13 % → 13 % | 37.3 px | 0.74 | 1.00 | 465 |
| over the wet one | 27 % → 27 % | 37.1 px | 0.74 | 1.00 | 381 |
| long, no reload | 48 % → 48 % | 21.5 px | 0.70 | 1.00 | 2274 | quarters: 0.51 → 0.36 → 0.33 → 0.24

Numbers say: light vs heavy: width 22.5 → 43.4 px, dark 0.73 → 0.71.

## Oil · Henry Ward · Dry scrub #efeee6
Oil 1.00 · 50 px · 20.8 s

![Oil · Henry Ward · Dry scrub #efeee6](Oil-Henry-Ward-Dry-scrub-efeee6.png)

A light paint: laid on a grey sheet (on white it cannot be seen); **dark** = how far it is from the grey either way.

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 5 % → 5 % | 15.0 px | 0.20 | 1.00 | 126 |
| heavy line | 9 % → 9 % | 25.4 px | 0.27 | 1.00 | 158 |
| pressure swell | 7 % → 7 % | 27.5 px | 0.29 | 1.00 | 116 |
| fast wave | 26 % → 26 % | 30.2 px | 0.27 | 1.01 | 563 |
| slow wave | 26 % → 26 % | 29.6 px | 0.28 | 1.00 | 770 |
| spiral | 45 % → 45 % | 29.8 px | 0.23 | 1.00 | 1136 |
| loop | 20 % → 20 % | 26.1 px | 0.28 | 1.00 | 676 |
| tilted | 13 % → 13 % | 35.4 px | 0.25 | 1.00 | 362 |
| over the wet one | 18 % → 18 % | 14.3 px | 0.25 | 1.00 | 471 |
| long, no reload | 31 % → 31 % | 13.7 px | 0.22 | 1.00 | 1482 | quarters: 0.00 → 0.00 → 0.00 → 0.00

Numbers say: light vs heavy: width 15.0 → 25.4 px, dark 0.20 → 0.27; the long stroke does not run out of paint.

## Oil · Henry Ward · Ground #e6e2f0
Gouache 1.00 · 160 px · 91.4 s

![Oil · Henry Ward · Ground #e6e2f0](Oil-Henry-Ward-Ground-e6e2f0.png)

A light paint: laid on a grey sheet (on white it cannot be seen); **dark** = how far it is from the grey either way.

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 51 % → 46 % | 148.3 px | 0.39 | 0.89 | 1335 |
| heavy line | 52 % → 47 % | 151.5 px | 0.39 | 0.91 | 1307 |
| pressure swell | 41 % → 45 % | 154.8 px | 0.38 | 1.10 | 867 |
| fast wave | 85 % → 86 % | 97.8 px | 0.37 | 1.01 | 3302 |
| slow wave | 86 % → 73 % | 99.2 px | 0.38 | 0.86 | 5537 |
| spiral | 88 % → 69 % | 58.3 px | 0.38 | 0.77 | 5106 |
| loop | 75 % → 69 % | 97.0 px | 0.38 | 0.92 | 2855 |
| tilted | 39 % → 39 % | 107.5 px | 0.38 | 1.00 | 1733 |
| over the wet one | 76 % → 71 % | 104.6 px | 0.38 | 0.93 | 969 |
| long, no reload | 98 % → 87 % | 44.0 px | 0.38 | 0.88 | 5745 | quarters: 0.00 → 0.00 → 0.00 → 0.00

Numbers say: light vs heavy: width 148.3 → 151.5 px, dark 0.39 → 0.39; pressure barely changes the width.

## Oil · Henry Ward · Loaded flat #a8b84a
Oil 1.00 · 46 px · 22.3 s

![Oil · Henry Ward · Loaded flat #a8b84a](Oil-Henry-Ward-Loaded-flat-a8b84a.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 8 % → 8 % | 22.5 px | 0.19 | 1.00 | 143 |
| heavy line | 15 % → 15 % | 43.4 px | 0.21 | 1.00 | 212 |
| pressure swell | 11 % → 11 % | 41.0 px | 0.27 | 1.00 | 191 |
| fast wave | 32 % → 33 % | 37.5 px | 0.24 | 1.00 | 679 |
| slow wave | 26 % → 26 % | 30.2 px | 0.19 | 1.00 | 1088 |
| spiral | 51 % → 51 % | 33.5 px | 0.17 | 1.00 | 813 |
| loop | 28 % → 28 % | 36.3 px | 0.21 | 1.00 | 502 |
| tilted | 13 % → 13 % | 37.3 px | 0.24 | 1.00 | 326 |
| over the wet one | 27 % → 27 % | 37.1 px | 0.24 | 1.00 | 262 |
| long, no reload | 48 % → 48 % | 21.5 px | 0.17 | 1.00 | 1750 | quarters: 0.14 → 0.09 → 0.08 → 0.06

Numbers say: light vs heavy: width 22.5 → 43.4 px, dark 0.19 → 0.21.

## Oil · Henry Ward · Thin veil #5a8a6a
Oil 0.81 · Ink 0.19 · 56 px · 41.3 s

![Oil · Henry Ward · Thin veil #5a8a6a](Oil-Henry-Ward-Thin-veil-5a8a6a.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 6 % → 4 % | 18.8 px | 0.25 | 0.66 | 197 |
| heavy line | 12 % → 12 % | 36.0 px | 0.39 | 0.94 | 262 |
| pressure swell | 10 % → 9 % | 38.2 px | 0.32 | 0.89 | 197 |
| fast wave | 39 % → 32 % | 44.6 px | 0.36 | 0.82 | 756 |
| slow wave | 36 % → 33 % | 42.2 px | 0.33 | 0.91 | 1125 |
| spiral | 61 % → 50 % | 40.4 px | 0.25 | 0.81 | 1476 |
| loop | 28 % → 23 % | 36.3 px | 0.26 | 0.83 | 627 |
| tilted | 15 % → 15 % | 41.7 px | 0.39 | 1.01 | 379 |
| over the wet one | 24 % → 22 % | 26.1 px | 0.39 | 0.89 | 365 |
| long, no reload | 56 % → 44 % | 24.9 px | 0.24 | 0.79 | 1577 | quarters: 0.20 → 0.10 → 0.09 → 0.09

Numbers say: light vs heavy: width 18.8 → 36.0 px, dark 0.25 → 0.39.

## Oil · Henry Ward · Loaded flat #4a1420
Oil 1.00 · 46 px · 22.6 s

![Oil · Henry Ward · Loaded flat #4a1420](Oil-Henry-Ward-Loaded-flat-4a1420.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 8 % → 8 % | 22.5 px | 0.76 | 1.00 | 182 |
| heavy line | 15 % → 15 % | 43.4 px | 0.73 | 1.00 | 221 |
| pressure swell | 11 % → 11 % | 41.0 px | 0.80 | 1.00 | 166 |
| fast wave | 32 % → 33 % | 37.5 px | 0.76 | 1.00 | 739 |
| slow wave | 26 % → 26 % | 30.2 px | 0.75 | 1.00 | 935 |
| spiral | 51 % → 51 % | 33.5 px | 0.72 | 1.00 | 965 |
| loop | 28 % → 28 % | 36.3 px | 0.76 | 1.00 | 646 |
| tilted | 13 % → 13 % | 37.3 px | 0.76 | 1.00 | 387 |
| over the wet one | 27 % → 27 % | 37.1 px | 0.76 | 1.00 | 245 |
| long, no reload | 48 % → 48 % | 21.5 px | 0.72 | 1.00 | 1690 | quarters: 0.52 → 0.37 → 0.35 → 0.26

Numbers say: light vs heavy: width 22.5 → 43.4 px, dark 0.76 → 0.73.

## Oil · Henry Ward · Dirty contour #2a0a10
Oil 1.00 · 24 px · 18.9 s

![Oil · Henry Ward · Dirty contour #2a0a10](Oil-Henry-Ward-Dirty-contour-2a0a10.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 8 % → 8 % | 22.0 px | 0.82 | 1.00 | 123 |
| heavy line | 8 % → 8 % | 24.5 px | 0.81 | 1.00 | 128 |
| pressure swell | 7 % → 7 % | 27.1 px | 0.84 | 1.00 | 82 |
| fast wave | 19 % → 19 % | 22.1 px | 0.85 | 1.00 | 292 |
| slow wave | 21 % → 21 % | 24.2 px | 0.83 | 1.00 | 743 |
| spiral | 31 % → 31 % | 20.7 px | 0.83 | 1.00 | 774 |
| loop | 17 % → 17 % | 21.6 px | 0.83 | 1.00 | 397 |
| tilted | 9 % → 9 % | 26.2 px | 0.82 | 1.00 | 148 |
| over the wet one | 18 % → 18 % | 22.7 px | 0.82 | 1.00 | 166 |
| long, no reload | 41 % → 41 % | 18.4 px | 0.79 | 1.00 | 838 | quarters: 0.46 → 0.39 → 0.33 → 0.28

Numbers say: light vs heavy: width 22.0 → 24.5 px, dark 0.82 → 0.81.

## Oil · Henry Ward · Dry scrub #c0506a
Oil 1.00 · 50 px · 21.5 s

![Oil · Henry Ward · Dry scrub #c0506a](Oil-Henry-Ward-Dry-scrub-c0506a.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 5 % → 5 % | 15.0 px | 0.34 | 1.00 | 157 |
| heavy line | 9 % → 9 % | 25.4 px | 0.37 | 1.00 | 238 |
| pressure swell | 7 % → 7 % | 27.5 px | 0.41 | 1.00 | 153 |
| fast wave | 26 % → 26 % | 30.2 px | 0.46 | 1.01 | 643 |
| slow wave | 26 % → 26 % | 29.6 px | 0.37 | 1.00 | 1150 |
| spiral | 45 % → 45 % | 29.8 px | 0.33 | 1.00 | 1121 |
| loop | 20 % → 20 % | 26.1 px | 0.38 | 1.00 | 476 |
| tilted | 13 % → 13 % | 35.4 px | 0.47 | 1.00 | 362 |
| over the wet one | 18 % → 18 % | 14.3 px | 0.47 | 1.00 | 277 |
| long, no reload | 31 % → 31 % | 13.7 px | 0.39 | 1.00 | 1540 | quarters: 0.14 → 0.13 → 0.12 → 0.11

Numbers say: light vs heavy: width 15.0 → 25.4 px, dark 0.34 → 0.37.

## Oil · Henry Ward · Ground #d8d4c8
Gouache 1.00 · 160 px · 85.9 s

![Oil · Henry Ward · Ground #d8d4c8](Oil-Henry-Ward-Ground-d8d4c8.png)

A light paint: laid on a grey sheet (on white it cannot be seen); **dark** = how far it is from the grey either way.

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 51 % → 46 % | 148.3 px | 0.35 | 0.89 | 1190 |
| heavy line | 52 % → 47 % | 151.5 px | 0.35 | 0.91 | 1263 |
| pressure swell | 41 % → 45 % | 154.8 px | 0.35 | 1.10 | 1136 |
| fast wave | 85 % → 86 % | 97.8 px | 0.34 | 1.01 | 3461 |
| slow wave | 86 % → 73 % | 99.2 px | 0.35 | 0.86 | 4028 |
| spiral | 88 % → 69 % | 58.3 px | 0.35 | 0.77 | 4205 |
| loop | 75 % → 69 % | 97.0 px | 0.35 | 0.92 | 2195 |
| tilted | 39 % → 39 % | 107.5 px | 0.35 | 1.00 | 1584 |
| over the wet one | 76 % → 71 % | 104.6 px | 0.35 | 0.93 | 1327 |
| long, no reload | 98 % → 87 % | 44.0 px | 0.35 | 0.88 | 7829 | quarters: 0.00 → 0.00 → 0.00 → 0.00

Numbers say: light vs heavy: width 148.3 → 151.5 px, dark 0.35 → 0.35; pressure barely changes the width.

## Oil · Henry Ward · Loaded flat #e8d8b0
Oil 1.00 · 46 px · 17.6 s

![Oil · Henry Ward · Loaded flat #e8d8b0](Oil-Henry-Ward-Loaded-flat-e8d8b0.png)

A light paint: laid on a grey sheet (on white it cannot be seen); **dark** = how far it is from the grey either way.

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 8 % → 8 % | 22.5 px | 0.29 | 1.00 | 180 |
| heavy line | 15 % → 15 % | 43.4 px | 0.36 | 1.00 | 303 |
| pressure swell | 11 % → 11 % | 41.0 px | 0.31 | 1.00 | 178 |
| fast wave | 32 % → 33 % | 37.5 px | 0.28 | 1.00 | 720 |
| slow wave | 26 % → 26 % | 30.2 px | 0.34 | 1.00 | 918 |
| spiral | 51 % → 51 % | 33.5 px | 0.29 | 1.00 | 799 |
| loop | 28 % → 28 % | 36.3 px | 0.33 | 1.00 | 397 |
| tilted | 13 % → 13 % | 37.3 px | 0.29 | 1.00 | 207 |
| over the wet one | 27 % → 27 % | 37.1 px | 0.29 | 1.00 | 167 |
| long, no reload | 48 % → 48 % | 21.5 px | 0.29 | 1.00 | 998 | quarters: 0.00 → 0.00 → 0.00 → 0.00

Numbers say: light vs heavy: width 22.5 → 43.4 px, dark 0.29 → 0.36; the long stroke does not run out of paint.

## Oil · Henry Ward · Dry scrub #f2ead0
Oil 1.00 · 50 px · 16.6 s

![Oil · Henry Ward · Dry scrub #f2ead0](Oil-Henry-Ward-Dry-scrub-f2ead0.png)

A light paint: laid on a grey sheet (on white it cannot be seen); **dark** = how far it is from the grey either way.

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 5 % → 5 % | 15.0 px | 0.20 | 1.00 | 230 |
| heavy line | 9 % → 9 % | 25.4 px | 0.26 | 1.00 | 324 |
| pressure swell | 7 % → 7 % | 27.5 px | 0.28 | 1.00 | 181 |
| fast wave | 26 % → 26 % | 30.2 px | 0.26 | 1.01 | 526 |
| slow wave | 26 % → 26 % | 29.6 px | 0.27 | 1.00 | 740 |
| spiral | 45 % → 45 % | 29.8 px | 0.22 | 1.00 | 880 |
| loop | 20 % → 20 % | 26.1 px | 0.27 | 1.00 | 333 |
| tilted | 13 % → 13 % | 35.4 px | 0.24 | 1.00 | 227 |
| over the wet one | 18 % → 18 % | 14.3 px | 0.24 | 1.00 | 154 |
| long, no reload | 31 % → 31 % | 13.7 px | 0.22 | 1.00 | 1057 | quarters: 0.00 → 0.00 → 0.00 → 0.00

Numbers say: light vs heavy: width 15.0 → 25.4 px, dark 0.20 → 0.26; the long stroke does not run out of paint.

## Oil · Henry Ward · Loaded flat #2a1428
Oil 1.00 · 46 px · 17.4 s

![Oil · Henry Ward · Loaded flat #2a1428](Oil-Henry-Ward-Loaded-flat-2a1428.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 8 % → 8 % | 22.5 px | 0.79 | 1.00 | 233 |
| heavy line | 15 % → 15 % | 43.4 px | 0.75 | 1.00 | 310 |
| pressure swell | 11 % → 11 % | 41.0 px | 0.82 | 1.00 | 220 |
| fast wave | 32 % → 33 % | 37.5 px | 0.78 | 1.00 | 500 |
| slow wave | 26 % → 26 % | 30.2 px | 0.77 | 1.00 | 697 |
| spiral | 51 % → 51 % | 33.5 px | 0.74 | 1.00 | 897 |
| loop | 28 % → 28 % | 36.3 px | 0.78 | 1.00 | 371 |
| tilted | 13 % → 13 % | 37.3 px | 0.79 | 1.00 | 198 |
| over the wet one | 27 % → 27 % | 37.1 px | 0.79 | 1.00 | 180 |
| long, no reload | 48 % → 48 % | 21.5 px | 0.75 | 1.00 | 1251 | quarters: 0.54 → 0.38 → 0.36 → 0.26

Numbers say: light vs heavy: width 22.5 → 43.4 px, dark 0.79 → 0.75.

## Oil · Henry Ward · Ground #e8e4e0
Gouache 1.00 · 160 px · 79.8 s

![Oil · Henry Ward · Ground #e8e4e0](Oil-Henry-Ward-Ground-e8e4e0.png)

A light paint: laid on a grey sheet (on white it cannot be seen); **dark** = how far it is from the grey either way.

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 51 % → 46 % | 148.3 px | 0.39 | 0.89 | 683 |
| heavy line | 52 % → 47 % | 151.5 px | 0.39 | 0.91 | 759 |
| pressure swell | 41 % → 45 % | 154.8 px | 0.38 | 1.10 | 546 |
| fast wave | 85 % → 86 % | 97.8 px | 0.37 | 1.01 | 2501 |
| slow wave | 86 % → 73 % | 99.2 px | 0.38 | 0.86 | 4279 |
| spiral | 88 % → 69 % | 58.3 px | 0.38 | 0.77 | 4970 |
| loop | 75 % → 69 % | 97.0 px | 0.39 | 0.92 | 2946 |
| tilted | 39 % → 39 % | 107.5 px | 0.38 | 1.00 | 1301 |
| over the wet one | 76 % → 71 % | 104.6 px | 0.38 | 0.93 | 1045 |
| long, no reload | 98 % → 87 % | 44.0 px | 0.38 | 0.88 | 8387 | quarters: 0.00 → 0.00 → 0.00 → 0.00

Numbers say: light vs heavy: width 148.3 → 151.5 px, dark 0.39 → 0.39; pressure barely changes the width.

## Oil · Henry Ward · Loaded flat #8a2a18
Oil 1.00 · 46 px · 17.7 s

![Oil · Henry Ward · Loaded flat #8a2a18](Oil-Henry-Ward-Loaded-flat-8a2a18.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 8 % → 8 % | 22.5 px | 0.65 | 1.00 | 122 |
| heavy line | 15 % → 15 % | 43.4 px | 0.64 | 1.00 | 166 |
| pressure swell | 11 % → 11 % | 41.0 px | 0.70 | 1.00 | 197 |
| fast wave | 32 % → 33 % | 37.5 px | 0.66 | 1.00 | 443 |
| slow wave | 26 % → 26 % | 30.2 px | 0.65 | 1.00 | 625 |
| spiral | 51 % → 51 % | 33.5 px | 0.62 | 1.00 | 731 |
| loop | 28 % → 28 % | 36.3 px | 0.66 | 1.00 | 473 |
| tilted | 13 % → 13 % | 37.3 px | 0.67 | 1.00 | 217 |
| over the wet one | 27 % → 27 % | 37.1 px | 0.67 | 1.00 | 172 |
| long, no reload | 48 % → 48 % | 21.5 px | 0.62 | 1.00 | 1338 | quarters: 0.45 → 0.32 → 0.29 → 0.22

Numbers say: light vs heavy: width 22.5 → 43.4 px, dark 0.65 → 0.64.

## Oil · Henry Ward · Loaded flat #a8c8dc
Oil 1.00 · 46 px · 22.8 s

![Oil · Henry Ward · Loaded flat #a8c8dc](Oil-Henry-Ward-Loaded-flat-a8c8dc.png)

A light paint: laid on a grey sheet (on white it cannot be seen); **dark** = how far it is from the grey either way.

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 8 % → 8 % | 22.5 px | 0.24 | 1.00 | 148 |
| heavy line | 15 % → 15 % | 43.4 px | 0.30 | 1.00 | 203 |
| pressure swell | 11 % → 11 % | 41.0 px | 0.24 | 1.00 | 151 |
| fast wave | 32 % → 33 % | 37.5 px | 0.23 | 1.00 | 677 |
| slow wave | 26 % → 26 % | 30.2 px | 0.28 | 1.00 | 1063 |
| spiral | 51 % → 51 % | 33.5 px | 0.25 | 1.00 | 1213 |
| loop | 28 % → 28 % | 36.3 px | 0.27 | 1.00 | 616 |
| tilted | 13 % → 13 % | 37.3 px | 0.24 | 1.00 | 357 |
| over the wet one | 27 % → 27 % | 37.1 px | 0.24 | 1.00 | 348 |
| long, no reload | 48 % → 48 % | 21.5 px | 0.25 | 1.00 | 1733 | quarters: 0.00 → 0.00 → 0.00 → 0.00

Numbers say: light vs heavy: width 22.5 → 43.4 px, dark 0.24 → 0.30; the long stroke does not run out of paint.

## Oil · Henry Ward · Dry scrub #d8e8f0
Oil 1.00 · 50 px · 21.9 s

![Oil · Henry Ward · Dry scrub #d8e8f0](Oil-Henry-Ward-Dry-scrub-d8e8f0.png)

A light paint: laid on a grey sheet (on white it cannot be seen); **dark** = how far it is from the grey either way.

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 5 % → 5 % | 15.0 px | 0.19 | 1.00 | 141 |
| heavy line | 9 % → 9 % | 25.4 px | 0.25 | 1.00 | 162 |
| pressure swell | 7 % → 7 % | 27.5 px | 0.27 | 1.00 | 164 |
| fast wave | 26 % → 26 % | 30.2 px | 0.25 | 1.01 | 759 |
| slow wave | 26 % → 26 % | 29.6 px | 0.26 | 1.00 | 1218 |
| spiral | 45 % → 45 % | 29.8 px | 0.21 | 1.00 | 1180 |
| loop | 20 % → 20 % | 26.1 px | 0.26 | 1.00 | 528 |
| tilted | 13 % → 13 % | 35.4 px | 0.23 | 1.00 | 373 |
| over the wet one | 18 % → 18 % | 14.3 px | 0.23 | 1.00 | 306 |
| long, no reload | 31 % → 31 % | 13.7 px | 0.21 | 1.00 | 1617 | quarters: 0.00 → 0.00 → 0.00 → 0.00

Numbers say: light vs heavy: width 15.0 → 25.4 px, dark 0.19 → 0.25; the long stroke does not run out of paint.

## Oil · Henry Ward · Ground #3a3a34
Gouache 1.00 · 160 px · 78.2 s

![Oil · Henry Ward · Ground #3a3a34](Oil-Henry-Ward-Ground-3a3a34.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 51 % → 46 % | 148.3 px | 0.47 | 0.89 | 1033 |
| heavy line | 52 % → 47 % | 151.5 px | 0.47 | 0.91 | 1157 |
| pressure swell | 41 % → 45 % | 154.8 px | 0.48 | 1.10 | 948 |
| fast wave | 85 % → 86 % | 97.8 px | 0.48 | 1.01 | 3340 |
| slow wave | 86 % → 73 % | 99.2 px | 0.47 | 0.86 | 5533 |
| spiral | 88 % → 69 % | 58.3 px | 0.48 | 0.77 | 5534 |
| loop | 75 % → 69 % | 97.0 px | 0.47 | 0.92 | 1656 |
| tilted | 39 % → 39 % | 107.5 px | 0.47 | 1.00 | 1114 |
| over the wet one | 76 % → 71 % | 104.6 px | 0.47 | 0.93 | 918 |
| long, no reload | 98 % → 87 % | 44.0 px | 0.47 | 0.88 | 5618 | quarters: 0.47 → 0.47 → 0.47 → 0.45

Numbers say: light vs heavy: width 148.3 → 151.5 px, dark 0.47 → 0.47; pressure barely changes the width; the long stroke does not run out of paint.

## Oil · Henry Ward · Loaded flat #8a906a
Oil 1.00 · 46 px · 23.5 s

![Oil · Henry Ward · Loaded flat #8a906a](Oil-Henry-Ward-Loaded-flat-8a906a.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 8 % → 8 % | 22.5 px | 0.28 | 1.00 | 165 |
| heavy line | 15 % → 15 % | 43.4 px | 0.31 | 1.00 | 252 |
| pressure swell | 11 % → 11 % | 41.0 px | 0.36 | 1.00 | 209 |
| fast wave | 32 % → 33 % | 37.5 px | 0.32 | 1.00 | 618 |
| slow wave | 26 % → 26 % | 30.2 px | 0.28 | 1.00 | 1064 |
| spiral | 51 % → 51 % | 33.5 px | 0.25 | 1.00 | 1126 |
| loop | 28 % → 28 % | 36.3 px | 0.30 | 1.00 | 638 |
| tilted | 13 % → 13 % | 37.3 px | 0.33 | 1.00 | 491 |
| over the wet one | 27 % → 27 % | 37.1 px | 0.33 | 1.00 | 286 |
| long, no reload | 48 % → 48 % | 21.5 px | 0.25 | 1.00 | 1460 | quarters: 0.21 → 0.13 → 0.11 → 0.08

Numbers say: light vs heavy: width 22.5 → 43.4 px, dark 0.28 → 0.31.

## Oil · Henry Ward · Loaded flat #7a8458
Oil 1.00 · 46 px · 22.5 s

![Oil · Henry Ward · Loaded flat #7a8458](Oil-Henry-Ward-Loaded-flat-7a8458.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 8 % → 8 % | 22.5 px | 0.32 | 1.00 | 212 |
| heavy line | 15 % → 15 % | 43.4 px | 0.36 | 1.00 | 255 |
| pressure swell | 11 % → 11 % | 41.0 px | 0.41 | 1.00 | 235 |
| fast wave | 32 % → 33 % | 37.5 px | 0.37 | 1.00 | 643 |
| slow wave | 26 % → 26 % | 30.2 px | 0.33 | 1.00 | 1034 |
| spiral | 51 % → 51 % | 33.5 px | 0.30 | 1.00 | 1305 |
| loop | 28 % → 28 % | 36.3 px | 0.34 | 1.00 | 429 |
| tilted | 13 % → 13 % | 37.3 px | 0.38 | 1.00 | 249 |
| over the wet one | 27 % → 27 % | 37.1 px | 0.38 | 1.00 | 263 |
| long, no reload | 48 % → 48 % | 21.5 px | 0.29 | 1.00 | 1408 | quarters: 0.24 → 0.15 → 0.13 → 0.09

Numbers say: light vs heavy: width 22.5 → 43.4 px, dark 0.32 → 0.36.

## Oil · Henry Ward · Dry scrub #a8ae88
Oil 1.00 · 50 px · 18.9 s

![Oil · Henry Ward · Dry scrub #a8ae88](Oil-Henry-Ward-Dry-scrub-a8ae88.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 5 % → 5 % | 15.0 px | 0.11 | 1.00 | 189 |
| heavy line | 9 % → 9 % | 25.4 px | 0.14 | 1.00 | 187 |
| pressure swell | 7 % → 7 % | 27.5 px | 0.16 | 1.00 | 142 |
| fast wave | 26 % → 26 % | 30.2 px | 0.22 | 1.01 | 928 |
| slow wave | 26 % → 26 % | 29.6 px | 0.13 | 1.00 | 1278 |
| spiral | 45 % → 45 % | 29.8 px | 0.12 | 1.00 | 1321 |
| loop | 20 % → 20 % | 26.1 px | 0.12 | 1.00 | 584 |
| tilted | 13 % → 13 % | 35.4 px | 0.23 | 1.00 | 399 |
| over the wet one | 18 % → 18 % | 14.3 px | 0.23 | 1.00 | 260 |
| long, no reload | 31 % → 31 % | 13.7 px | 0.14 | 1.00 | 1536 | quarters: 0.05 → 0.05 → 0.04 → 0.04

Numbers say: light vs heavy: width 15.0 → 25.4 px, dark 0.11 → 0.14; the long stroke does not run out of paint.

## v3 · Any shape · K stamp
Gouache 1.00 · 48 px · 39.8 s

![v3 · Any shape · K stamp](v3-Any-shape-K-stamp.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 20 % → 19 % | 59.0 px | 0.40 | 0.93 | 379 |
| heavy line | 20 % → 19 % | 59.1 px | 0.40 | 0.94 | 338 |
| pressure swell | 12 % → 11 % | 43.7 px | 0.40 | 0.98 | 257 |
| fast wave | 42 % → 34 % | 48.2 px | 0.40 | 0.83 | 538 |
| slow wave | 42 % → 34 % | 48.3 px | 0.40 | 0.82 | 821 |
| spiral | 66 % → 44 % | 43.5 px | 0.40 | 0.67 | 884 |
| loop | 37 % → 34 % | 48.2 px | 0.40 | 0.91 | 474 |
| tilted | 15 % → 15 % | 42.0 px | 0.40 | 1.01 | 270 |
| over the wet one | 33 % → 32 % | 51.3 px | 0.40 | 0.95 | 218 |
| long, no reload | 81 % → 47 % | 36.3 px | 0.40 | 0.58 | 1807 | quarters: 0.35 → 0.34 → 0.32 → 0.28

Numbers say: light vs heavy: width 59.0 → 59.1 px, dark 0.40 → 0.40; pressure barely changes the width.

## v3 · Any shape · K of hairs
Oil 1.00 · 48 px · 17.2 s

![v3 · Any shape · K of hairs](v3-Any-shape-K-of-hairs.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 18 % → 18 % | 51.8 px | 0.40 | 1.00 | 246 |
| heavy line | 27 % → 27 % | 78.4 px | 0.46 | 1.00 | 267 |
| pressure swell | 16 % → 16 % | 58.4 px | 0.47 | 1.01 | 190 |
| fast wave | 49 % → 51 % | 56.8 px | 0.44 | 1.04 | 656 |
| slow wave | 50 % → 50 % | 57.8 px | 0.48 | 1.00 | 776 |
| spiral | 67 % → 67 % | 44.1 px | 0.45 | 1.00 | 688 |
| loop | 45 % → 45 % | 58.8 px | 0.48 | 1.00 | 333 |
| tilted | 16 % → 16 % | 45.8 px | 0.46 | 1.00 | 191 |
| over the wet one | 39 % → 39 % | 62.3 px | 0.46 | 1.01 | 158 |
| long, no reload | 84 % → 84 % | 37.8 px | 0.43 | 1.00 | 978 | quarters: 0.48 → 0.46 → 0.33 → 0.26

Numbers say: light vs heavy: width 51.8 → 78.4 px, dark 0.40 → 0.46.

## v3 · Any shape · Star stamp
Gouache 1.00 · 44 px · 34.2 s

![v3 · Any shape · Star stamp](v3-Any-shape-Star-stamp.png)

A light paint: laid on a grey sheet (on white it cannot be seen); **dark** = how far it is from the grey either way.

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 13 % → 11 % | 37.9 px | 0.36 | 0.84 | 151 |
| heavy line | 13 % → 12 % | 38.4 px | 0.36 | 0.87 | 119 |
| pressure swell | 10 % → 10 % | 39.2 px | 0.36 | 0.93 | 91 |
| fast wave | 33 % → 28 % | 38.0 px | 0.36 | 0.84 | 251 |
| slow wave | 33 % → 27 % | 38.4 px | 0.35 | 0.80 | 446 |
| spiral | 56 % → 41 % | 37.2 px | 0.35 | 0.73 | 437 |
| loop | 28 % → 25 % | 36.0 px | 0.36 | 0.88 | 254 |
| tilted | 13 % → 13 % | 37.0 px | 0.36 | 1.01 | 137 |
| over the wet one | 26 % → 24 % | 36.5 px | 0.36 | 0.91 | 125 |
| long, no reload | 68 % → 45 % | 30.4 px | 0.35 | 0.67 | 792 | quarters: 0.01 → 0.01 → 0.01 → 0.01

Numbers say: light vs heavy: width 37.9 → 38.4 px, dark 0.36 → 0.36; pressure barely changes the width; the long stroke does not run out of paint.

## v3 · Any shape · Star of hairs
Oil 1.00 · 44 px · 15.8 s

![v3 · Any shape · Star of hairs](v3-Any-shape-Star-of-hairs.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 15 % → 15 % | 43.7 px | 0.34 | 1.00 | 133 |
| heavy line | 23 % → 23 % | 67.9 px | 0.33 | 1.00 | 162 |
| pressure swell | 14 % → 14 % | 53.1 px | 0.35 | 1.00 | 89 |
| fast wave | 45 % → 46 % | 52.0 px | 0.32 | 1.01 | 332 |
| slow wave | 44 % → 44 % | 50.7 px | 0.33 | 1.00 | 572 |
| spiral | 63 % → 63 % | 41.7 px | 0.32 | 1.00 | 586 |
| loop | 39 % → 39 % | 50.4 px | 0.33 | 1.00 | 276 |
| tilted | 14 % → 14 % | 39.1 px | 0.34 | 1.00 | 165 |
| over the wet one | 34 % → 34 % | 55.5 px | 0.34 | 1.00 | 153 |
| long, no reload | 78 % → 78 % | 35.1 px | 0.30 | 1.00 | 888 | quarters: 0.32 → 0.28 → 0.23 → 0.17

Numbers say: light vs heavy: width 43.7 → 67.9 px, dark 0.34 → 0.33.

## v3 · Any shape · Rag
Oil 1.00 · 60 px · 19.1 s

![v3 · Any shape · Rag](v3-Any-shape-Rag.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 22 % → 25 % | 64.2 px | 0.16 | 1.12 | 162 |
| heavy line | 38 % → 38 % | 111.5 px | 0.29 | 1.00 | 254 |
| pressure swell | 25 % → 26 % | 94.4 px | 0.24 | 1.02 | 170 |
| fast wave | 68 % → 73 % | 78.9 px | 0.26 | 1.07 | 595 |
| slow wave | 71 % → 71 % | 82.3 px | 0.27 | 1.00 | 1185 |
| spiral | 81 % → 81 % | 53.5 px | 0.28 | 1.00 | 1156 |
| loop | 61 % → 62 % | 79.6 px | 0.29 | 1.00 | 629 |
| tilted | 22 % → 22 % | 61.1 px | 0.26 | 1.00 | 338 |
| over the wet one | 51 % → 52 % | 80.5 px | 0.26 | 1.03 | 242 |
| long, no reload | 94 % → 94 % | 42.3 px | 0.29 | 1.00 | 1541 | quarters: 0.35 → 0.32 → 0.27 → 0.21

Numbers say: light vs heavy: width 64.2 → 111.5 px, dark 0.16 → 0.29.

## v3 · Any shape · Dry oil on canvas
Oil 1.00 · 40 px · 13.0 s

![v3 · Any shape · Dry oil on canvas](v3-Any-shape-Dry-oil-on-canvas.png)

A light paint: laid on a grey sheet (on white it cannot be seen); **dark** = how far it is from the grey either way.

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 5 % → 5 % | 13.3 px | 0.14 | 1.00 | 88 |
| heavy line | 8 % → 8 % | 23.7 px | 0.35 | 1.00 | 105 |
| pressure swell | 9 % → 9 % | 32.2 px | 0.27 | 1.00 | 90 |
| fast wave | 27 % → 27 % | 31.7 px | 0.25 | 1.00 | 312 |
| slow wave | 26 % → 26 % | 30.5 px | 0.24 | 1.00 | 449 |
| spiral | 45 % → 45 % | 29.7 px | 0.25 | 1.00 | 540 |
| loop | 21 % → 21 % | 27.3 px | 0.24 | 1.00 | 219 |
| tilted | 9 % → 9 % | 26.3 px | 0.24 | 1.00 | 109 |
| over the wet one | 18 % → 18 % | 23.1 px | 0.24 | 1.00 | 95 |
| long, no reload | 41 % → 41 % | 18.2 px | 0.21 | 1.00 | 603 | quarters: 0.00 → 0.00 → 0.00 → 0.00

Numbers say: light vs heavy: width 13.3 → 23.7 px, dark 0.14 → 0.35; the long stroke does not run out of paint.

## v3 · Any shape · Two colours streaks
Oil 1.00 · 44 px · 13.6 s

![v3 · Any shape · Two colours streaks](v3-Any-shape-Two-colours-streaks.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 14 % → 14 % | 39.6 px | 0.35 | 1.00 | 106 |
| heavy line | 16 % → 16 % | 46.1 px | 0.31 | 1.00 | 113 |
| pressure swell | 11 % → 11 % | 42.9 px | 0.39 | 1.00 | 86 |
| fast wave | 37 % → 37 % | 43.1 px | 0.34 | 1.00 | 301 |
| slow wave | 35 % → 35 % | 40.7 px | 0.31 | 1.00 | 486 |
| spiral | 61 % → 61 % | 40.4 px | 0.35 | 1.00 | 524 |
| loop | 32 % → 32 % | 41.1 px | 0.32 | 1.00 | 258 |
| tilted | 13 % → 13 % | 37.2 px | 0.36 | 1.00 | 165 |
| over the wet one | 27 % → 27 % | 39.3 px | 0.36 | 1.00 | 123 |
| long, no reload | 73 % → 73 % | 32.6 px | 0.31 | 1.00 | 743 | quarters: 0.29 → 0.28 → 0.24 → 0.18

Numbers say: light vs heavy: width 39.6 → 46.1 px, dark 0.35 → 0.31.

## Brush Artist · Refs · #01 Henry Ward peach cloud — own sheet
own sheet 600 × 600 · Gouache 1.00 · 44 px · 10.0 s

![Brush Artist · Refs · #01 Henry Ward peach cloud — own sheet](Brush-Artist-Refs-01-Henry-Ward-peach-cloud-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 5 % → 16 % | 15.6 px | 0.53 | 2.97 | 105 |
| stroke 2 | 11 % → 29 % | 35.1 px | 0.54 | 2.71 | 130 |
| stroke 3 | 16 % → 31 % | 45.4 px | 0.54 | 2.00 | 117 |
| stroke 4 | 21 % → 34 % | 68.0 px | 0.54 | 1.63 | 135 |
| stroke 5 | 21 % → 31 % | 60.5 px | 0.54 | 1.48 | 127 |
| stroke 6 | 20 % → 24 % | 61.5 px | 0.54 | 1.21 | 142 |
| stroke 7 | 9 % → 33 % | 22.9 px | 0.53 | 3.58 | 116 |
| stroke 8 | 14 % → 32 % | 34.7 px | 0.53 | 2.28 | 140 |
| stroke 9 | 13 % → 33 % | 33.9 px | 0.53 | 2.47 | 138 |
| stroke 10 | 13 % → 34 % | 35.3 px | 0.53 | 2.57 | 120 |
| stroke 11 | 14 % → 36 % | 40.5 px | 0.54 | 2.53 | 127 |
| stroke 12 | 14 % → 39 % | 42.4 px | 0.54 | 2.76 | 99 |
| stroke 13 | 19 % → 42 % | 54.8 px | 0.54 | 2.23 | 133 |
| stroke 14 | 27 % → 44 % | 77.4 px | 0.54 | 1.63 | 164 |
| stroke 15 | 30 % → 48 % | 88.5 px | 0.53 | 1.60 | 113 |
| stroke 16 | 35 % → 48 % | 104.8 px | 0.53 | 1.39 | 154 |
| stroke 17 | 35 % → 50 % | 98.5 px | 0.53 | 1.41 | 132 |
| stroke 18 | 41 % → 49 % | 117.6 px | 0.53 | 1.21 | 147 |
| stroke 19 | 41 % → 49 % | 116.0 px | 0.54 | 1.18 | 130 |
| stroke 20 | 43 % → 46 % | 123.0 px | 0.54 | 1.07 | 157 |
| stroke 21 | 43 % → 42 % | 125.4 px | 0.54 | 0.96 | 166 |
| stroke 22 | 45 % → 42 % | 131.2 px | 0.54 | 0.94 | 145 |
| stroke 23 | 49 % → 43 % | 139.0 px | 0.54 | 0.88 | 146 |
| stroke 24 | 52 % → 45 % | 156.2 px | 0.54 | 0.86 | 100 |

Numbers say: wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #02 Henry Ward cream strokes — own sheet
own sheet 600 × 600 · Gouache 1.00 · 46 px · 6.6 s

![Brush Artist · Refs · #02 Henry Ward cream strokes — own sheet](Brush-Artist-Refs-02-Henry-Ward-cream-strokes-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 9 % → 2 % | 17.7 px | 0.65 | 0.26 | 173 |
| stroke 2 | 15 % → 6 % | 39.4 px | 0.66 | 0.41 | 183 |
| stroke 3 | 19 % → 22 % | 48.9 px | 0.64 | 1.15 | 199 |
| stroke 4 | 23 % → 22 % | 56.7 px | 0.64 | 0.97 | 218 |
| stroke 5 | 24 % → 27 % | 59.0 px | 0.64 | 1.11 | 186 |
| stroke 6 | 18 % → 16 % | 43.4 px | 0.64 | 0.88 | 203 |
| stroke 7 | 21 % → 10 % | 53.1 px | 0.64 | 0.48 | 181 |

## Brush Artist · Refs · #03 Henry Ward navy contours — own sheet
own sheet 600 × 600 · Impasto 1.00 · 22 px · 2.4 s

![Brush Artist · Refs · #03 Henry Ward navy contours — own sheet](Brush-Artist-Refs-03-Henry-Ward-navy-contours-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 10 % → 15 % | 20.0 px | 0.70 | 1.51 | 107 |
| stroke 2 | 16 % → 19 % | 22.1 px | 0.70 | 1.19 | 89 |
| stroke 3 | 20 % → 20 % | 29.5 px | 0.71 | 0.99 | 129 |
| stroke 4 | 19 % → 17 % | 43.6 px | 0.71 | 0.89 | 155 |

Numbers say: wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #04 Henry Ward grey cloud — own sheet
own sheet 600 × 600 · Gouache 1.00 · 50 px · 10.3 s

![Brush Artist · Refs · #04 Henry Ward grey cloud — own sheet](Brush-Artist-Refs-04-Henry-Ward-grey-cloud-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 5 % → 21 % | 15.7 px | 0.32 | 3.88 | 149 |
| stroke 2 | 14 % → 21 % | 40.2 px | 0.31 | 1.53 | 190 |
| stroke 3 | 21 % → 22 % | 59.7 px | 0.31 | 1.05 | 191 |
| stroke 4 | 27 % → 23 % | 79.5 px | 0.31 | 0.84 | 215 |
| stroke 5 | 27 % → 26 % | 83.3 px | 0.31 | 0.94 | 188 |
| stroke 6 | 33 % → 30 % | 109.0 px | 0.31 | 0.89 | 184 |
| stroke 7 | 34 % → 36 % | 100.8 px | 0.30 | 1.03 | 189 |
| stroke 8 | 38 % → 38 % | 112.6 px | 0.30 | 0.99 | 191 |
| stroke 9 | 32 % → 39 % | 94.9 px | 0.31 | 1.23 | 155 |
| stroke 10 | 33 % → 39 % | 106.9 px | 0.31 | 1.19 | 177 |
| stroke 11 | 34 % → 36 % | 96.9 px | 0.31 | 1.05 | 211 |
| stroke 12 | 32 % → 34 % | 96.3 px | 0.30 | 1.06 | 146 |
| stroke 13 | 27 % → 38 % | 78.1 px | 0.31 | 1.38 | 160 |
| stroke 14 | 34 % → 38 % | 100.7 px | 0.31 | 1.11 | 226 |
| stroke 15 | 35 % → 37 % | 100.1 px | 0.31 | 1.07 | 173 |
| stroke 16 | 38 % → 36 % | 116.5 px | 0.31 | 0.93 | 248 |
| stroke 17 | 39 % → 31 % | 112.7 px | 0.31 | 0.79 | 212 |
| stroke 18 | 40 % → 28 % | 133.2 px | 0.31 | 0.70 | 229 |
| stroke 19 | 38 % → 24 % | 113.0 px | 0.32 | 0.63 | 203 |
| stroke 20 | 40 % → 23 % | 125.2 px | 0.32 | 0.57 | 271 |

Numbers say: wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #05 Henry Ward green in rust loops — own sheet
own sheet 600 × 600 · Impasto 1.00 · 20 px · 2.1 s

![Brush Artist · Refs · #05 Henry Ward green in rust loops — own sheet](Brush-Artist-Refs-05-Henry-Ward-green-in-rust-loops-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 11 % → 16 % | 19.1 px | 0.02 | 1.49 | 104 |
| stroke 2 | 12 % → 10 % | 24.0 px | 0.02 | 0.86 | 147 |
| stroke 3 | 20 % → 17 % | 35.4 px | 0.02 | 0.89 | 116 |

## Brush Artist · Refs · #06 Henry Ward scrubbed grey — own sheet
own sheet 600 × 600 · Gouache 1.00 · 50 px · 11.2 s

![Brush Artist · Refs · #06 Henry Ward scrubbed grey — own sheet](Brush-Artist-Refs-06-Henry-Ward-scrubbed-grey-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 6 % → 24 % | 15.9 px | 0.32 | 3.69 | 168 |
| stroke 2 | 16 % → 25 % | 41.5 px | 0.31 | 1.58 | 183 |
| stroke 3 | 21 % → 23 % | 64.7 px | 0.31 | 1.10 | 167 |
| stroke 4 | 25 % → 24 % | 78.0 px | 0.31 | 0.96 | 200 |
| stroke 5 | 31 % → 30 % | 92.8 px | 0.31 | 0.97 | 175 |
| stroke 6 | 38 % → 31 % | 115.7 px | 0.31 | 0.81 | 188 |
| stroke 7 | 36 % → 35 % | 103.6 px | 0.31 | 0.98 | 197 |
| stroke 8 | 40 % → 36 % | 125.1 px | 0.31 | 0.90 | 172 |
| stroke 9 | 35 % → 37 % | 107.6 px | 0.31 | 1.06 | 159 |
| stroke 10 | 34 % → 38 % | 111.3 px | 0.31 | 1.10 | 159 |
| stroke 11 | 35 % → 37 % | 101.5 px | 0.31 | 1.06 | 186 |
| stroke 12 | 33 % → 35 % | 99.4 px | 0.31 | 1.08 | 149 |
| stroke 13 | 24 % → 37 % | 69.3 px | 0.31 | 1.53 | 178 |
| stroke 14 | 30 % → 39 % | 88.5 px | 0.31 | 1.30 | 240 |
| stroke 15 | 33 % → 44 % | 95.1 px | 0.32 | 1.34 | 182 |
| stroke 16 | 35 % → 45 % | 111.8 px | 0.32 | 1.28 | 208 |
| stroke 17 | 37 % → 42 % | 110.5 px | 0.32 | 1.12 | 215 |
| stroke 18 | 41 % → 40 % | 123.6 px | 0.32 | 0.98 | 208 |
| stroke 19 | 38 % → 35 % | 112.0 px | 0.32 | 0.93 | 198 |
| stroke 20 | 38 % → 34 % | 117.9 px | 0.32 | 0.90 | 223 |
| stroke 21 | 40 % → 30 % | 116.2 px | 0.33 | 0.75 | 251 |
| stroke 22 | 39 % → 28 % | 127.1 px | 0.33 | 0.73 | 196 |

Numbers say: wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #07 Henry Ward blue L + black zigzag — own sheet
own sheet 600 × 600 · Impasto 1.00 · 34 px · 1.9 s

![Brush Artist · Refs · #07 Henry Ward blue L + black zigzag — own sheet](Brush-Artist-Refs-07-Henry-Ward-blue-L-black-zigzag-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 13 % → 15 % | 31.2 px | 0.58 | 1.09 | 109 |
| stroke 2 | 15 % → 14 % | 37.7 px | 0.58 | 0.90 | 85 |

## Brush Artist · Refs · #08 Henry Ward olive bands — own sheet
own sheet 600 × 600 · Gouache 1.00 · 34 px · 5.3 s

![Brush Artist · Refs · #08 Henry Ward olive bands — own sheet](Brush-Artist-Refs-08-Henry-Ward-olive-bands-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 8 % → 4 % | 15.7 px | 0.58 | 0.53 | 129 |
| stroke 2 | 12 % → 4 % | 28.0 px | 0.58 | 0.35 | 155 |
| stroke 3 | 13 % → 11 % | 27.5 px | 0.58 | 0.87 | 167 |
| stroke 4 | 17 % → 10 % | 37.3 px | 0.58 | 0.57 | 207 |
| stroke 5 | 22 % → 13 % | 45.2 px | 0.56 | 0.59 | 177 |
| stroke 6 | 16 % → 6 % | 30.5 px | 0.54 | 0.40 | 169 |

## Brush Artist · Refs · #09 Henry Ward white loops — own sheet
own sheet 600 × 600 · Gouache 1.00 · 46 px · 6.6 s

![Brush Artist · Refs · #09 Henry Ward white loops — own sheet](Brush-Artist-Refs-09-Henry-Ward-white-loops-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 23 % → 0 % | 12.1 px | 0.06 | 0.00 | 867 |
| stroke 2 | 27 % → 0 % | 27.4 px | 0.07 | 0.00 | 1045 |
| stroke 3 | 34 % → 0 % | 31.4 px | 0.07 | 0.00 | 1031 |
| stroke 4 | 8 % → 0 % | 18.4 px | 0.00 | 0.00 | 219 |
| stroke 5 | 5 % → 0 % | 14.8 px | 0.06 | 0.00 | 169 |
| stroke 6 | 5 % → 0 % | 13.8 px | 0.08 | 0.00 | 185 |
| stroke 7 | 10 % → 0 % | 26.8 px | 0.08 | 0.00 | 194 |
| stroke 8 | 5 % → 0 % | 8.2 px | 0.00 | 0.00 | 157 |

## Brush Artist · Refs · #10 Henry Ward maroon loops — own sheet
own sheet 600 × 600 · Impasto 1.00 · 30 px · 3.4 s

![Brush Artist · Refs · #10 Henry Ward maroon loops — own sheet](Brush-Artist-Refs-10-Henry-Ward-maroon-loops-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 12 % → 26 % | 28.9 px | 0.72 | 2.25 | 236 |
| stroke 2 | 23 % → 39 % | 51.0 px | 0.72 | 1.74 | 129 |
| stroke 3 | 30 % → 36 % | 59.6 px | 0.72 | 1.20 | 197 |
| stroke 4 | 40 % → 38 % | 91.4 px | 0.72 | 0.94 | 119 |
| stroke 5 | 33 % → 29 % | 82.1 px | 0.71 | 0.89 | 172 |

Numbers say: wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #11 Henry Ward purple spun balls — own sheet
own sheet 600 × 600 · Impasto 1.00 · 36 px · 2.8 s

![Brush Artist · Refs · #11 Henry Ward purple spun balls — own sheet](Brush-Artist-Refs-11-Henry-Ward-purple-spun-balls-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 22 % → 31 % | 24.4 px | 0.69 | 1.42 | 267 |
| stroke 2 | 31 % → 44 % | 34.3 px | 0.69 | 1.39 | 218 |
| stroke 3 | 34 % → 33 % | 37.7 px | 0.69 | 0.97 | 289 |

## Brush Artist · Refs · #12 Henry Ward black-olive cage — own sheet
own sheet 600 × 600 · Gouache 1.00 · 28 px · 5.0 s

![Brush Artist · Refs · #12 Henry Ward black-olive cage — own sheet](Brush-Artist-Refs-12-Henry-Ward-black-olive-cage-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 9 % → 10 % | 17.0 px | 0.58 | 1.15 | 216 |
| stroke 2 | 7 % → 10 % | 15.8 px | 0.58 | 1.46 | 188 |
| stroke 3 | 18 % → 13 % | 28.0 px | 0.58 | 0.72 | 248 |
| stroke 4 | 20 % → 14 % | 39.4 px | 0.59 | 0.70 | 140 |
| stroke 5 | 18 % → 7 % | 33.8 px | 0.58 | 0.40 | 135 |
| stroke 6 | 29 % → 15 % | 54.8 px | 0.58 | 0.52 | 170 |

## Brush Artist · Refs · #13 Henry Ward blue streaky form — own sheet
own sheet 600 × 600 · Gouache 1.00 · 50 px · 8.9 s

![Brush Artist · Refs · #13 Henry Ward blue streaky form — own sheet](Brush-Artist-Refs-13-Henry-Ward-blue-streaky-form-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 5 % → 0 % | 15.9 px | 0.00 | 0.00 | 172 |
| stroke 2 | 13 % → 0 % | 40.6 px | 0.00 | 0.00 | 186 |
| stroke 3 | 22 % → 0 % | 62.3 px | 0.00 | 0.00 | 197 |
| stroke 4 | 24 % → 0 % | 78.4 px | 0.00 | 0.00 | 227 |
| stroke 5 | 31 % → 0 % | 90.1 px | 0.00 | 0.00 | 208 |
| stroke 6 | 37 % → 0 % | 105.3 px | 0.00 | 0.00 | 191 |
| stroke 7 | 36 % → 0 % | 107.2 px | 0.00 | 0.00 | 190 |
| stroke 8 | 40 % → 0 % | 120.3 px | 0.00 | 0.00 | 167 |
| stroke 9 | 33 % → 0 % | 102.9 px | 0.00 | 0.00 | 194 |
| stroke 10 | 32 % → 0 % | 105.4 px | 0.00 | 0.00 | 182 |
| stroke 11 | 30 % → 0 % | 92.1 px | 0.00 | 0.00 | 190 |
| stroke 12 | 26 % → 0 % | 78.3 px | 0.00 | 0.00 | 142 |
| stroke 13 | 24 % → 0 % | 74.8 px | 0.00 | 0.00 | 197 |
| stroke 14 | 29 % → 0 % | 84.9 px | 0.00 | 0.00 | 209 |
| stroke 15 | 30 % → 0 % | 86.3 px | 0.00 | 0.00 | 177 |
| stroke 16 | 35 % → 0 % | 104.8 px | 0.00 | 0.00 | 219 |
| stroke 17 | 41 % → 0 % | 103.0 px | 0.00 | 0.00 | 186 |
| stroke 18 | 49 % → 0 % | 117.7 px | 0.00 | 0.00 | 229 |
| stroke 19 | 51 % → 0 % | 104.2 px | 0.00 | 0.00 | 188 |
| stroke 20 | 60 % → 0 % | 115.5 px | 0.00 | 0.00 | 208 |
| stroke 21 | 7 % → 0 % | 15.0 px | 0.00 | 0.00 | 172 |
| stroke 22 | 6 % → 0 % | 18.5 px | 0.00 | 0.00 | 180 |
| stroke 23 | 11 % → 0 % | 35.1 px | 0.00 | 0.00 | 194 |
| stroke 24 | 4 % → 0 % | 11.0 px | 0.00 | 0.00 | 136 |
| stroke 25 | 4 % → 0 % | 9.1 px | 0.00 | 0.00 | 137 |

## Brush Artist · Refs · #14 Henry Ward olive totem — own sheet
own sheet 600 × 600 · Impasto 1.00 · 48 px · 6.5 s

![Brush Artist · Refs · #14 Henry Ward olive totem — own sheet](Brush-Artist-Refs-14-Henry-Ward-olive-totem-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 18 % → 46 % | 46.6 px | 0.38 | 2.57 | 126 |
| stroke 2 | 20 % → 50 % | 61.7 px | 0.38 | 2.53 | 123 |
| stroke 3 | 27 % → 52 % | 93.9 px | 0.39 | 1.89 | 106 |
| stroke 4 | 30 % → 54 % | 110.9 px | 0.39 | 1.82 | 126 |
| stroke 5 | 38 % → 63 % | 134.1 px | 0.39 | 1.64 | 95 |
| stroke 6 | 38 % → 64 % | 149.8 px | 0.39 | 1.67 | 133 |
| stroke 7 | 35 % → 60 % | 119.1 px | 0.39 | 1.70 | 140 |
| stroke 8 | 37 % → 62 % | 141.6 px | 0.39 | 1.67 | 127 |
| stroke 9 | 38 % → 62 % | 131.6 px | 0.39 | 1.64 | 141 |
| stroke 10 | 37 % → 61 % | 136.5 px | 0.39 | 1.65 | 150 |
| stroke 11 | 38 % → 64 % | 136.7 px | 0.39 | 1.66 | 121 |
| stroke 12 | 38 % → 64 % | 143.5 px | 0.38 | 1.68 | 130 |
| stroke 13 | 37 % → 66 % | 129.3 px | 0.39 | 1.78 | 123 |
| stroke 14 | 36 % → 61 % | 131.1 px | 0.39 | 1.70 | 164 |
| stroke 15 | 39 % → 65 % | 134.4 px | 0.39 | 1.66 | 125 |
| stroke 16 | 38 % → 63 % | 136.6 px | 0.39 | 1.67 | 158 |
| stroke 17 | 37 % → 61 % | 124.1 px | 0.39 | 1.64 | 132 |
| stroke 18 | 40 % → 65 % | 152.2 px | 0.39 | 1.63 | 130 |
| stroke 19 | 38 % → 58 % | 131.3 px | 0.39 | 1.54 | 121 |
| stroke 20 | 40 % → 53 % | 142.6 px | 0.39 | 1.31 | 171 |
| stroke 21 | 46 % → 53 % | 136.0 px | 0.39 | 1.15 | 127 |
| stroke 22 | 53 % → 51 % | 143.0 px | 0.39 | 0.97 | 146 |

Numbers say: wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #15 Ultramarine brush script — own sheet
own sheet 600 × 600 · Ink 1.00 · 4 px · 8.2 s

![Brush Artist · Refs · #15 Ultramarine brush script — own sheet](Brush-Artist-Refs-15-Ultramarine-brush-script-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 40 % → 42 % | 9.0 px | 0.65 | 1.05 | 50 |
| stroke 2 | 41 % → 43 % | 9.0 px | 0.67 | 1.07 | 43 |
| stroke 3 | 39 % → 42 % | 9.4 px | 0.72 | 1.08 | 27 |
| stroke 4 | 42 % → 46 % | 10.2 px | 0.74 | 1.10 | 16 |
| stroke 5 | 46 % → 49 % | 10.1 px | 0.72 | 1.06 | 28 |
| stroke 6 | 43 % → 45 % | 9.7 px | 0.65 | 1.05 | 69 |
| stroke 7 | 44 % → 47 % | 9.3 px | 0.72 | 1.08 | 32 |
| stroke 8 | 37 % → 39 % | 8.9 px | 0.65 | 1.06 | 59 |
| stroke 9 | 39 % → 42 % | 9.1 px | 0.70 | 1.07 | 48 |
| stroke 10 | 35 % → 37 % | 9.6 px | 0.66 | 1.05 | 46 |
| stroke 11 | 44 % → 47 % | 9.9 px | 0.69 | 1.06 | 53 |
| stroke 12 | 39 % → 41 % | 9.4 px | 0.65 | 1.06 | 50 |
| stroke 13 | 45 % → 46 % | 10.1 px | 0.69 | 1.04 | 29 |
| stroke 14 | 37 % → 40 % | 9.6 px | 0.71 | 1.07 | 28 |
| stroke 15 | 37 % → 38 % | 9.0 px | 0.67 | 1.05 | 54 |
| stroke 16 | 42 % → 45 % | 9.4 px | 0.70 | 1.06 | 28 |
| stroke 17 | 41 % → 45 % | 7.1 px | 0.71 | 1.09 | 49 |
| stroke 18 | 43 % → 45 % | 9.3 px | 0.73 | 1.05 | 31 |
| stroke 19 | 40 % → 42 % | 9.0 px | 0.65 | 1.06 | 70 |
| stroke 20 | 42 % → 44 % | 9.7 px | 0.69 | 1.06 | 33 |
| stroke 21 | 39 % → 42 % | 9.6 px | 0.69 | 1.07 | 41 |
| stroke 22 | 44 % → 46 % | 8.9 px | 0.65 | 1.06 | 50 |
| stroke 23 | 38 % → 42 % | 9.5 px | 0.72 | 1.10 | 18 |
| stroke 24 | 39 % → 42 % | 9.1 px | 0.73 | 1.06 | 39 |
| stroke 25 | 41 % → 44 % | 10.0 px | 0.71 | 1.06 | 27 |
| stroke 26 | 45 % → 47 % | 9.1 px | 0.66 | 1.04 | 42 |
| stroke 27 | 43 % → 45 % | 9.0 px | 0.62 | 1.05 | 57 |
| stroke 28 | 45 % → 47 % | 9.3 px | 0.70 | 1.06 | 42 |
| stroke 29 | 35 % → 38 % | 10.4 px | 0.69 | 1.08 | 25 |
| stroke 30 | 39 % → 40 % | 8.5 px | 0.70 | 1.04 | 31 |
| stroke 31 | 43 % → 46 % | 10.4 px | 0.74 | 1.07 | 19 |
| stroke 32 | 41 % → 45 % | 9.3 px | 0.70 | 1.09 | 23 |
| stroke 33 | 35 % → 40 % | 10.9 px | 0.73 | 1.13 | 25 |
| stroke 34 | 41 % → 45 % | 10.1 px | 0.74 | 1.09 | 18 |
| stroke 35 | 36 % → 38 % | 9.4 px | 0.67 | 1.06 | 53 |

## Brush Artist · Refs · #18 Blue oil-stick scribbles — own sheet
own sheet 600 × 600 · Pastel 1.00 · 10 px · 3.0 s

![Brush Artist · Refs · #18 Blue oil-stick scribbles — own sheet](Brush-Artist-Refs-18-Blue-oil-stick-scribbles-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 16 % → 32 % | 3.9 px | 0.49 | 2.03 | 146 |
| stroke 2 | 13 % → 37 % | 3.6 px | 0.49 | 2.75 | 195 |
| stroke 3 | 16 % → 26 % | 5.8 px | 0.49 | 1.64 | 208 |
| stroke 4 | 15 % → 29 % | 7.9 px | 0.49 | 1.91 | 172 |
| stroke 5 | 29 % → 34 % | 8.5 px | 0.49 | 1.18 | 162 |
| stroke 6 | 26 % → 26 % | 9.4 px | 0.49 | 1.02 | 144 |
| stroke 7 | 26 % → 32 % | 8.4 px | 0.49 | 1.24 | 176 |
| stroke 8 | 30 % → 30 % | 17.0 px | 0.49 | 1.00 | 179 |

Numbers say: wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #20 Orange-red crayon scribble — own sheet
own sheet 600 × 600 · Pastel 1.00 · 14 px · 2.7 s

![Brush Artist · Refs · #20 Orange-red crayon scribble — own sheet](Brush-Artist-Refs-20-Orange-red-crayon-scribble-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 8 % → 19 % | 5.5 px | 0.59 | 2.47 | 193 |
| stroke 2 | 9 % → 22 % | 6.6 px | 0.60 | 2.50 | 180 |
| stroke 3 | 13 % → 21 % | 8.3 px | 0.60 | 1.65 | 199 |
| stroke 4 | 24 % → 32 % | 8.8 px | 0.60 | 1.36 | 193 |
| stroke 5 | 28 % → 28 % | 7.9 px | 0.59 | 1.00 | 162 |
| stroke 6 | 22 % → 22 % | 16.4 px | 0.60 | 1.00 | 174 |

Numbers say: wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #21 Gritty black contours — own sheet
own sheet 600 × 600 · Gouache 1.00 · 12 px · 3.8 s

![Brush Artist · Refs · #21 Gritty black contours — own sheet](Brush-Artist-Refs-21-Gritty-black-contours-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 6 % → 4 % | 6.2 px | 0.36 | 0.68 | 141 |
| stroke 2 | 5 % → 2 % | 7.9 px | 0.36 | 0.47 | 194 |
| stroke 3 | 9 % → 2 % | 7.8 px | 0.37 | 0.17 | 109 |
| stroke 4 | 9 % → 3 % | 10.9 px | 0.36 | 0.36 | 127 |
| stroke 5 | 10 % → 4 % | 12.7 px | 0.35 | 0.35 | 93 |

## Brush Artist · Refs · #22 Bold black brush poster — own sheet
own sheet 600 × 600 · Ink 1.00 · 20 px · 4.7 s

![Brush Artist · Refs · #22 Bold black brush poster — own sheet](Brush-Artist-Refs-22-Bold-black-brush-poster-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 24 % → 28 % | 38.8 px | 0.95 | 1.18 | 105 |
| stroke 2 | 28 % → 39 % | 42.9 px | 0.94 | 1.38 | 28 |
| stroke 3 | 30 % → 30 % | 46.0 px | 0.94 | 1.00 | 47 |
| stroke 4 | 30 % → 41 % | 57.8 px | 0.94 | 1.41 | 50 |
| stroke 5 | 27 % → 27 % | 46.3 px | 0.93 | 1.00 | 86 |

## Brush Artist · Refs · #23 Dry white on orange + black line — own sheet
own sheet 600 × 600 · Gouache 1.00 · 50 px · 7.3 s

![Brush Artist · Refs · #23 Dry white on orange + black line — own sheet](Brush-Artist-Refs-23-Dry-white-on-orange-black-line-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 4 % → 11 % | 14.5 px | 0.38 | 2.70 | 113 |
| stroke 2 | 8 % → 10 % | 26.7 px | 0.38 | 1.35 | 152 |
| stroke 3 | 13 % → 11 % | 49.0 px | 0.38 | 0.81 | 129 |
| stroke 4 | 17 % → 12 % | 68.6 px | 0.38 | 0.67 | 151 |
| stroke 5 | 23 % → 13 % | 85.0 px | 0.38 | 0.55 | 150 |
| stroke 6 | 26 % → 14 % | 106.9 px | 0.38 | 0.53 | 140 |
| stroke 7 | 23 % → 13 % | 86.4 px | 0.38 | 0.57 | 129 |
| stroke 8 | 22 % → 12 % | 87.4 px | 0.38 | 0.53 | 159 |
| stroke 9 | 19 % → 11 % | 69.7 px | 0.38 | 0.60 | 151 |
| stroke 10 | 18 % → 11 % | 68.9 px | 0.38 | 0.63 | 152 |
| stroke 11 | 20 % → 11 % | 73.3 px | 0.38 | 0.56 | 137 |
| stroke 12 | 19 % → 12 % | 72.9 px | 0.38 | 0.65 | 135 |
| stroke 13 | 20 % → 14 % | 75.6 px | 0.38 | 0.70 | 145 |
| stroke 14 | 21 % → 14 % | 84.0 px | 0.38 | 0.64 | 165 |
| stroke 15 | 21 % → 13 % | 79.6 px | 0.38 | 0.62 | 118 |
| stroke 16 | 22 % → 11 % | 87.4 px | 0.38 | 0.52 | 147 |
| stroke 17 | 22 % → 9 % | 76.2 px | 0.38 | 0.40 | 132 |
| stroke 18 | 27 % → 9 % | 99.3 px | 0.38 | 0.34 | 133 |

Numbers say: wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #24 Picasso flat oil — own sheet
own sheet 600 × 600 · Oil 0.89 · Oil glaze 0.11 · 34 px · 5.1 s

![Brush Artist · Refs · #24 Picasso flat oil — own sheet](Brush-Artist-Refs-24-Picasso-flat-oil-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 14 % → 44 % | 30.0 px | 0.22 | 3.11 | 127 |
| stroke 2 | 19 % → 47 % | 44.5 px | 0.23 | 2.49 | 145 |
| stroke 3 | 27 % → 56 % | 59.7 px | 0.23 | 2.06 | 121 |
| stroke 4 | 37 % → 62 % | 82.9 px | 0.23 | 1.69 | 152 |
| stroke 5 | 41 % → 68 % | 91.2 px | 0.22 | 1.64 | 129 |
| stroke 6 | 42 % → 63 % | 96.5 px | 0.22 | 1.52 | 128 |
| stroke 7 | 42 % → 63 % | 87.5 px | 0.23 | 1.51 | 118 |
| stroke 8 | 42 % → 63 % | 101.6 px | 0.23 | 1.50 | 143 |
| stroke 9 | 34 % → 60 % | 74.4 px | 0.23 | 1.76 | 124 |
| stroke 10 | 38 % → 58 % | 89.8 px | 0.23 | 1.55 | 150 |
| stroke 11 | 35 % → 56 % | 74.6 px | 0.24 | 1.61 | 131 |
| stroke 12 | 37 % → 58 % | 88.3 px | 0.24 | 1.56 | 153 |
| stroke 13 | 35 % → 64 % | 77.9 px | 0.25 | 1.81 | 155 |
| stroke 14 | 36 % → 66 % | 82.0 px | 0.24 | 1.82 | 149 |
| stroke 15 | 36 % → 60 % | 76.0 px | 0.24 | 1.67 | 143 |
| stroke 16 | 36 % → 52 % | 83.2 px | 0.24 | 1.46 | 154 |
| stroke 17 | 41 % → 47 % | 86.1 px | 0.24 | 1.15 | 161 |
| stroke 18 | 42 % → 42 % | 101.0 px | 0.24 | 1.00 | 209 |

Numbers say: wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #25 Yellow heavy flat stroke — own sheet
own sheet 600 × 600 · Impasto 1.00 · 110 px · 2.7 s

![Brush Artist · Refs · #25 Yellow heavy flat stroke — own sheet](Brush-Artist-Refs-25-Yellow-heavy-flat-stroke-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 18 % → 18 % | 103.7 px | 0.16 | 0.98 | 638 |

## Brush Artist · Refs · #27 Orange impasto swatch — own sheet
own sheet 600 × 600 · Impasto 1.00 · 60 px · 2.9 s

![Brush Artist · Refs · #27 Orange impasto swatch — own sheet](Brush-Artist-Refs-27-Orange-impasto-swatch-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 8 % → 21 % | 58.4 px | 0.32 | 2.66 | 77 |
| stroke 2 | 7 % → 33 % | 62.2 px | 0.32 | 4.61 | 42 |
| stroke 3 | 25 % → 34 % | 238.0 px | 0.32 | 1.41 | 49 |
| stroke 4 | 10 % → 12 % | 69.5 px | 0.34 | 1.26 | 75 |
| stroke 5 | 17 % → 32 % | 61.8 px | 0.31 | 1.90 | 72 |
| stroke 6 | 17 % → 31 % | 143.7 px | 0.32 | 1.77 | 67 |
| stroke 7 | 8 % → 14 % | 68.6 px | 0.31 | 1.88 | 58 |
| stroke 8 | 32 % → 33 % | 328.8 px | 0.32 | 1.04 | 52 |
| stroke 9 | 37 % → 36 % | 182.9 px | 0.32 | 0.97 | 69 |
| stroke 10 | 33 % → 32 % | 298.6 px | 0.32 | 0.97 | 50 |

Numbers say: wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #28 Miles Davis black lines — own sheet
own sheet 600 × 600 · Ink 1.00 · 22 px · 5.5 s

![Brush Artist · Refs · #28 Miles Davis black lines — own sheet](Brush-Artist-Refs-28-Miles-Davis-black-lines-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 22 % → 31 % | 36.1 px | 0.88 | 1.42 | 161 |
| stroke 2 | 26 % → 47 % | 35.8 px | 0.88 | 1.79 | 117 |
| stroke 3 | 38 % → 42 % | 73.3 px | 0.88 | 1.11 | 97 |
| stroke 4 | 41 % → 47 % | 81.4 px | 0.88 | 1.16 | 150 |
| stroke 5 | 54 % → 54 % | 108.2 px | 0.88 | 1.00 | 118 |

Numbers say: wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #29 Shrigley magenta asterisk — own sheet
own sheet 600 × 600 · Watercolour 1.00 · 70 px · 5.6 s

![Brush Artist · Refs · #29 Shrigley magenta asterisk — own sheet](Brush-Artist-Refs-29-Shrigley-magenta-asterisk-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 13 % → 37 % | 46.6 px | 0.67 | 2.86 | 174 |
| stroke 2 | 12 % → 12 % | 87.1 px | 0.67 | 1.00 | 179 |
| stroke 3 | 28 % → 37 % | 100.9 px | 0.67 | 1.31 | 184 |
| stroke 4 | 23 % → 23 % | 164.0 px | 0.67 | 1.02 | 185 |

Numbers say: wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #30 Red gouache face patch — own sheet
own sheet 600 × 600 · Gouache 1.00 · 60 px · 11.2 s

![Brush Artist · Refs · #30 Red gouache face patch — own sheet](Brush-Artist-Refs-30-Red-gouache-face-patch-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 11 % → 37 % | 50.6 px | 0.54 | 3.29 | 163 |
| stroke 2 | 15 % → 41 % | 74.2 px | 0.54 | 2.74 | 150 |
| stroke 3 | 24 % → 50 % | 115.1 px | 0.54 | 2.08 | 187 |
| stroke 4 | 26 % → 52 % | 133.4 px | 0.54 | 1.95 | 187 |
| stroke 5 | 34 % → 60 % | 160.6 px | 0.54 | 1.77 | 181 |
| stroke 6 | 35 % → 61 % | 178.6 px | 0.54 | 1.76 | 188 |
| stroke 7 | 35 % → 59 % | 164.2 px | 0.54 | 1.70 | 170 |
| stroke 8 | 34 % → 56 % | 162.3 px | 0.54 | 1.66 | 200 |
| stroke 9 | 36 % → 60 % | 172.7 px | 0.53 | 1.66 | 161 |
| stroke 10 | 38 % → 62 % | 196.7 px | 0.53 | 1.64 | 183 |
| stroke 11 | 37 % → 61 % | 181.6 px | 0.53 | 1.67 | 179 |
| stroke 12 | 36 % → 58 % | 179.8 px | 0.53 | 1.60 | 203 |
| stroke 13 | 33 % → 46 % | 157.0 px | 0.53 | 1.38 | 181 |
| stroke 14 | 33 % → 41 % | 159.9 px | 0.53 | 1.24 | 197 |
| stroke 15 | 33 % → 37 % | 153.6 px | 0.53 | 1.12 | 185 |
| stroke 16 | 39 % → 39 % | 186.3 px | 0.53 | 0.98 | 158 |

Numbers say: wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #31 Warhol blotted line — own sheet
own sheet 600 × 600 · Ink 1.00 · 6 px · 4.4 s

![Brush Artist · Refs · #31 Warhol blotted line — own sheet](Brush-Artist-Refs-31-Warhol-blotted-line-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 22 % → 43 % | 16.5 px | 0.83 | 1.94 | 72 |
| stroke 2 | 17 % → 23 % | 15.7 px | 0.81 | 1.35 | 68 |
| stroke 3 | 24 % → 25 % | 24.9 px | 0.81 | 1.03 | 75 |
| stroke 4 | 32 % → 41 % | 32.7 px | 0.83 | 1.28 | 49 |
| stroke 5 | 37 % → 45 % | 38.1 px | 0.83 | 1.21 | 71 |
| stroke 6 | 34 % → 35 % | 27.8 px | 0.81 | 1.03 | 69 |

Numbers say: wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #32 Thick orange swipes — own sheet
own sheet 600 × 600 · Impasto 1.00 · 90 px · 3.4 s

![Brush Artist · Refs · #32 Thick orange swipes — own sheet](Brush-Artist-Refs-32-Thick-orange-swipes-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 14 % → 27 % | 86.6 px | 0.02 | 1.89 | 329 |
| stroke 2 | 26 % → 37 % | 177.9 px | 0.02 | 1.41 | 298 |
| stroke 3 | 27 % → 27 % | 176.1 px | 0.02 | 0.98 | 331 |

Numbers say: wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #33 Red wet-in-wet band — own sheet
own sheet 600 × 600 · Watercolour 1.00 · 80 px · 9.8 s

![Brush Artist · Refs · #33 Red wet-in-wet band — own sheet](Brush-Artist-Refs-33-Red-wet-in-wet-band-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 22 % → 57 % | 83.4 px | 0.61 | 2.61 | 364 |
| stroke 2 | 28 % → 51 % | 228.4 px | 0.62 | 1.82 | 144 |
| stroke 3 | 34 % → 53 % | 330.0 px | 0.61 | 1.57 | 104 |
| stroke 4 | 40 % → 60 % | 389.9 px | 0.62 | 1.51 | 94 |
| stroke 5 | 40 % → 55 % | 339.4 px | 0.61 | 1.38 | 120 |
| stroke 6 | 41 % → 48 % | 310.3 px | 0.59 | 1.18 | 134 |

Numbers say: wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #34 Magenta oil patches — own sheet
own sheet 600 × 600 · Oil 0.89 · Oil glaze 0.11 · 60 px · 3.3 s

![Brush Artist · Refs · #34 Magenta oil patches — own sheet](Brush-Artist-Refs-34-Magenta-oil-patches-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 8 % → 39 % | 57.1 px | 0.13 | 4.77 | 86 |
| stroke 2 | 8 % → 28 % | 56.8 px | 0.14 | 3.32 | 70 |
| stroke 3 | 7 % → 32 % | 58.6 px | 0.13 | 4.60 | 76 |
| stroke 4 | 15 % → 19 % | 122.2 px | 0.12 | 1.26 | 70 |
| stroke 5 | 21 % → 30 % | 112.2 px | 0.13 | 1.45 | 86 |
| stroke 6 | 19 % → 36 % | 159.7 px | 0.13 | 1.91 | 60 |
| stroke 7 | 28 % → 33 % | 226.6 px | 0.13 | 1.17 | 72 |
| stroke 8 | 30 % → 37 % | 213.6 px | 0.13 | 1.21 | 98 |
| stroke 9 | 23 % → 25 % | 147.9 px | 0.14 | 1.07 | 102 |
| stroke 10 | 27 % → 27 % | 240.6 px | 0.14 | 1.00 | 71 |
| stroke 11 | 33 % → 33 % | 297.2 px | 0.13 | 1.00 | 83 |
| stroke 12 | 24 % → 24 % | 173.6 px | 0.13 | 1.00 | 71 |

Numbers say: wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #35 Red band with runs — own sheet
own sheet 600 × 600 · Watercolour 1.00 · 70 px · 7.6 s

![Brush Artist · Refs · #35 Red band with runs — own sheet](Brush-Artist-Refs-35-Red-band-with-runs-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 37 % → 47 % | 140.3 px | 0.45 | 1.27 | 310 |

## Brush Artist · Refs · #36 Magenta letters flat brush — own sheet
own sheet 600 × 600 · Gouache 1.00 · 36 px · 10.3 s

![Brush Artist · Refs · #36 Magenta letters flat brush — own sheet](Brush-Artist-Refs-36-Magenta-letters-flat-brush-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 20 % → 38 % | 58.3 px | 0.50 | 1.95 | 35 |
| stroke 2 | 20 % → 31 % | 45.2 px | 0.51 | 1.54 | 30 |
| stroke 3 | 28 % → 52 % | 84.6 px | 0.50 | 1.83 | 31 |
| stroke 4 | 26 % → 44 % | 50.3 px | 0.51 | 1.69 | 86 |
| stroke 5 | 33 % → 54 % | 96.3 px | 0.50 | 1.63 | 79 |
| stroke 6 | 43 % → 56 % | 246.0 px | 0.49 | 1.30 | 19 |
| stroke 7 | 30 % → 43 % | 56.6 px | 0.50 | 1.43 | 108 |
| stroke 8 | 31 % → 52 % | 97.7 px | 0.51 | 1.66 | 54 |
| stroke 9 | 38 % → 50 % | 158.2 px | 0.51 | 1.31 | 24 |
| stroke 10 | 37 % → 62 % | 107.5 px | 0.50 | 1.68 | 85 |
| stroke 11 | 39 % → 61 % | 225.6 px | 0.49 | 1.55 | 20 |
| stroke 12 | 44 % → 55 % | 82.9 px | 0.50 | 1.26 | 101 |
| stroke 13 | 31 % → 45 % | 113.5 px | 0.51 | 1.43 | 38 |
| stroke 14 | 34 % → 50 % | 129.9 px | 0.51 | 1.47 | 42 |
| stroke 15 | 36 % → 54 % | 105.5 px | 0.50 | 1.49 | 65 |
| stroke 16 | 39 % → 47 % | 221.7 px | 0.50 | 1.23 | 13 |
| stroke 17 | 43 % → 51 % | 81.6 px | 0.50 | 1.18 | 119 |
| stroke 18 | 26 % → 35 % | 95.6 px | 0.50 | 1.34 | 30 |
| stroke 19 | 39 % → 37 % | 112.8 px | 0.50 | 0.97 | 43 |
| stroke 20 | 45 % → 44 % | 129.9 px | 0.51 | 0.98 | 29 |
| stroke 21 | 40 % → 38 % | 78.2 px | 0.50 | 0.94 | 88 |

Numbers say: wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #37 Oil still life dabs — own sheet
own sheet 600 × 600 · Oil 0.89 · Oil glaze 0.11 · 40 px · 2.4 s

![Brush Artist · Refs · #37 Oil still life dabs — own sheet](Brush-Artist-Refs-37-Oil-still-life-dabs-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 6 % → 6 % | 38.2 px | 0.37 | 1.00 | 27 |
| stroke 2 | 6 % → 26 % | 39.8 px | 0.40 | 4.69 | 33 |
| stroke 3 | 11 % → 33 % | 86.6 px | 0.39 | 3.00 | 17 |
| stroke 4 | 8 % → 8 % | 39.3 px | 0.37 | 1.00 | 42 |
| stroke 5 | 6 % → 10 % | 43.2 px | 0.38 | 1.67 | 19 |
| stroke 6 | 13 % → 29 % | 80.2 px | 0.40 | 2.26 | 25 |
| stroke 7 | 11 % → 22 % | 113.9 px | 0.38 | 2.08 | 15 |
| stroke 8 | 8 % → 13 % | 85.3 px | 0.38 | 1.59 | 14 |
| stroke 9 | 12 % → 13 % | 61.1 px | 0.36 | 1.12 | 30 |
| stroke 10 | 20 % → 24 % | 100.4 px | 0.40 | 1.20 | 31 |
| stroke 11 | 23 % → 27 % | 194.4 px | 0.41 | 1.15 | 13 |
| stroke 12 | 20 % → 20 % | 212.5 px | 0.39 | 1.00 | 11 |
| stroke 13 | 15 % → 15 % | 150.5 px | 0.42 | 1.00 | 14 |
| stroke 14 | 15 % → 15 % | 121.2 px | 0.38 | 1.00 | 17 |

Numbers say: wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #38 Sanguine drawing — own sheet
own sheet 600 × 600 · Pastel 1.00 · 6 px · 2.1 s

![Brush Artist · Refs · #38 Sanguine drawing — own sheet](Brush-Artist-Refs-38-Sanguine-drawing-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 3 % → 15 % | 3.3 px | 0.57 | 4.99 | 3 |
| stroke 2 | 3 % → 8 % | 2.9 px | 0.57 | 3.03 | 5 |
| stroke 3 | 3 % → 9 % | 3.3 px | 0.57 | 3.13 | 3 |
| stroke 4 | 2 % → 18 % | 2.8 px | 0.57 | 7.17 | 7 |
| stroke 5 | 3 % → 7 % | 2.9 px | 0.57 | 2.87 | 3 |
| stroke 6 | 3 % → 19 % | 3.5 px | 0.57 | 6.36 | 7 |
| stroke 7 | 5 % → 15 % | 5.3 px | 0.57 | 3.13 | 3 |
| stroke 8 | 4 % → 16 % | 4.8 px | 0.57 | 3.71 | 7 |
| stroke 9 | 3 % → 8 % | 3.4 px | 0.57 | 2.52 | 5 |
| stroke 10 | 4 % → 16 % | 4.9 px | 0.57 | 3.75 | 3 |
| stroke 11 | 3 % → 4 % | 3.0 px | 0.57 | 1.63 | 3 |
| stroke 12 | 4 % → 16 % | 4.7 px | 0.57 | 3.75 | 4 |
| stroke 13 | 8 % → 18 % | 9.2 px | 0.57 | 2.20 | 5 |
| stroke 14 | 5 % → 14 % | 5.3 px | 0.57 | 2.95 | 3 |
| stroke 15 | 9 % → 18 % | 10.7 px | 0.57 | 1.88 | 7 |
| stroke 16 | 6 % → 16 % | 7.0 px | 0.57 | 2.64 | 3 |
| stroke 17 | 4 % → 9 % | 5.0 px | 0.57 | 2.12 | 7 |
| stroke 18 | 3 % → 5 % | 3.1 px | 0.57 | 1.89 | 4 |
| stroke 19 | 6 % → 17 % | 7.4 px | 0.57 | 2.68 | 5 |
| stroke 20 | 9 % → 14 % | 9.8 px | 0.57 | 1.66 | 6 |
| stroke 21 | 4 % → 4 % | 4.6 px | 0.57 | 1.00 | 3 |
| stroke 22 | 8 % → 14 % | 9.2 px | 0.57 | 1.71 | 7 |
| stroke 23 | 8 % → 12 % | 8.7 px | 0.57 | 1.63 | 3 |
| stroke 24 | 4 % → 8 % | 5.0 px | 0.57 | 1.72 | 3 |
| stroke 25 | 8 % → 15 % | 9.3 px | 0.57 | 1.87 | 5 |
| stroke 26 | 6 % → 8 % | 6.9 px | 0.57 | 1.32 | 3 |
| stroke 27 | 4 % → 5 % | 4.8 px | 0.57 | 1.07 | 4 |
| stroke 28 | 8 % → 13 % | 8.9 px | 0.57 | 1.61 | 3 |
| stroke 29 | 8 % → 17 % | 9.0 px | 0.57 | 2.18 | 6 |
| stroke 30 | 13 % → 17 % | 15.2 px | 0.57 | 1.29 | 3 |
| stroke 31 | 5 % → 7 % | 6.0 px | 0.57 | 1.24 | 3 |
| stroke 32 | 11 % → 14 % | 12.9 px | 0.57 | 1.23 | 6 |
| stroke 33 | 8 % → 9 % | 9.5 px | 0.57 | 1.06 | 7 |
| stroke 34 | 11 % → 14 % | 12.3 px | 0.57 | 1.34 | 4 |
| stroke 35 | 9 % → 15 % | 10.7 px | 0.57 | 1.57 | 4 |
| stroke 36 | 10 % → 13 % | 11.9 px | 0.57 | 1.26 | 3 |
| stroke 37 | 10 % → 16 % | 11.4 px | 0.57 | 1.63 | 7 |
| stroke 38 | 14 % → 20 % | 15.3 px | 0.57 | 1.46 | 7 |
| stroke 39 | 14 % → 17 % | 16.5 px | 0.57 | 1.20 | 3 |
| stroke 40 | 6 % → 7 % | 7.3 px | 0.57 | 1.15 | 8 |
| stroke 41 | 16 % → 16 % | 18.2 px | 0.57 | 1.01 | 4 |
| stroke 42 | 14 % → 16 % | 16.1 px | 0.57 | 1.15 | 3 |
| stroke 43 | 11 % → 13 % | 13.0 px | 0.57 | 1.16 | 9 |
| stroke 44 | 13 % → 16 % | 15.2 px | 0.57 | 1.19 | 8 |
| stroke 45 | 2 % → 2 % | 2.8 px | 0.56 | 1.00 | 8 |
| stroke 46 | 17 % → 17 % | 18.9 px | 0.57 | 1.00 | 8 |
| stroke 47 | 14 % → 14 % | 15.9 px | 0.57 | 1.00 | 8 |
| stroke 48 | 13 % → 14 % | 14.7 px | 0.57 | 1.06 | 9 |
| stroke 49 | 19 % → 19 % | 21.8 px | 0.57 | 1.00 | 8 |
| stroke 50 | 11 % → 11 % | 12.2 px | 0.57 | 1.00 | 3 |

Numbers say: wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #39 Very thick impasto — own sheet
own sheet 600 × 600 · Impasto 1.00 · 60 px · 4.1 s

![Brush Artist · Refs · #39 Very thick impasto — own sheet](Brush-Artist-Refs-39-Very-thick-impasto-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 24 % → 35 % | 55.6 px | 0.43 | 1.44 | 257 |
| stroke 2 | 30 % → 46 % | 91.2 px | 0.43 | 1.52 | 249 |
| stroke 3 | 37 % → 48 % | 123.1 px | 0.44 | 1.31 | 269 |
| stroke 4 | 31 % → 43 % | 90.2 px | 0.43 | 1.39 | 294 |
| stroke 5 | 41 % → 39 % | 102.0 px | 0.43 | 0.97 | 281 |

Numbers say: wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #40 Watercolour blooms — own sheet
own sheet 600 × 600 · Watercolour 1.00 · 90 px · 8.0 s

![Brush Artist · Refs · #40 Watercolour blooms — own sheet](Brush-Artist-Refs-40-Watercolour-blooms-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 21 % → 27 % | 92.8 px | 0.12 | 1.28 | 713 |

## Brush Artist · Refs · #41 Coloured pencil hatching — own sheet
own sheet 600 × 600 · Pastel 1.00 · 4 px · 2.4 s

![Brush Artist · Refs · #41 Coloured pencil hatching — own sheet](Brush-Artist-Refs-41-Coloured-pencil-hatching-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 3 % → 15 % | 2.3 px | 0.35 | 5.04 | 3 |
| stroke 2 | 3 % → 8 % | 2.5 px | 0.35 | 2.34 | 3 |
| stroke 3 | 3 % → 12 % | 2.2 px | 0.35 | 4.03 | 5 |
| stroke 4 | 3 % → 20 % | 2.4 px | 0.35 | 6.35 | 5 |
| stroke 5 | 4 % → 8 % | 3.5 px | 0.35 | 1.78 | 2 |
| stroke 6 | 3 % → 14 % | 2.3 px | 0.35 | 4.57 | 5 |
| stroke 7 | 4 % → 17 % | 3.0 px | 0.35 | 4.34 | 2 |
| stroke 8 | 3 % → 13 % | 2.4 px | 0.35 | 4.14 | 4 |
| stroke 9 | 5 % → 12 % | 4.1 px | 0.35 | 2.18 | 5 |
| stroke 10 | 6 % → 17 % | 4.4 px | 0.35 | 2.92 | 2 |
| stroke 11 | 4 % → 14 % | 3.2 px | 0.35 | 3.38 | 5 |
| stroke 12 | 3 % → 3 % | 2.2 px | 0.35 | 1.00 | 4 |
| stroke 13 | 8 % → 19 % | 6.0 px | 0.35 | 2.35 | 2 |
| stroke 14 | 4 % → 15 % | 2.7 px | 0.35 | 4.14 | 3 |
| stroke 15 | 6 % → 13 % | 4.6 px | 0.35 | 2.12 | 4 |
| stroke 16 | 7 % → 12 % | 5.6 px | 0.35 | 1.63 | 4 |
| stroke 17 | 3 % → 3 % | 2.4 px | 0.35 | 1.00 | 6 |
| stroke 18 | 5 % → 9 % | 4.0 px | 0.36 | 1.63 | 2 |
| stroke 19 | 5 % → 14 % | 4.0 px | 0.35 | 2.72 | 3 |
| stroke 20 | 6 % → 16 % | 4.2 px | 0.35 | 2.94 | 2 |
| stroke 21 | 5 % → 15 % | 3.6 px | 0.35 | 3.13 | 4 |
| stroke 22 | 10 % → 18 % | 7.7 px | 0.35 | 1.77 | 2 |
| stroke 23 | 10 % → 15 % | 7.2 px | 0.35 | 1.54 | 3 |
| stroke 24 | 7 % → 15 % | 5.3 px | 0.35 | 2.12 | 2 |
| stroke 25 | 5 % → 12 % | 4.0 px | 0.35 | 2.27 | 4 |
| stroke 26 | 4 % → 7 % | 3.1 px | 0.35 | 1.79 | 5 |
| stroke 27 | 3 % → 8 % | 2.6 px | 0.35 | 2.35 | 2 |
| stroke 28 | 7 % → 11 % | 5.2 px | 0.36 | 1.68 | 4 |
| stroke 29 | 3 % → 15 % | 2.6 px | 0.35 | 4.48 | 5 |
| stroke 30 | 7 % → 10 % | 5.2 px | 0.35 | 1.40 | 2 |
| stroke 31 | 7 % → 16 % | 5.8 px | 0.35 | 2.09 | 3 |
| stroke 32 | 3 % → 6 % | 2.4 px | 0.36 | 1.93 | 2 |
| stroke 33 | 8 % → 13 % | 5.9 px | 0.35 | 1.65 | 3 |
| stroke 34 | 3 % → 6 % | 2.6 px | 0.35 | 1.71 | 5 |
| stroke 35 | 7 % → 15 % | 5.4 px | 0.35 | 2.11 | 2 |
| stroke 36 | 5 % → 5 % | 4.0 px | 0.35 | 1.01 | 5 |
| stroke 37 | 8 % → 16 % | 5.9 px | 0.35 | 2.07 | 2 |
| stroke 38 | 8 % → 14 % | 6.2 px | 0.35 | 1.71 | 5 |
| stroke 39 | 7 % → 12 % | 5.4 px | 0.35 | 1.65 | 6 |
| stroke 40 | 9 % → 20 % | 6.7 px | 0.36 | 2.23 | 2 |
| stroke 41 | 10 % → 15 % | 7.7 px | 0.35 | 1.46 | 3 |
| stroke 42 | 11 % → 19 % | 8.5 px | 0.36 | 1.73 | 2 |
| stroke 43 | 5 % → 9 % | 4.1 px | 0.35 | 1.66 | 5 |
| stroke 44 | 11 % → 15 % | 8.5 px | 0.36 | 1.41 | 2 |
| stroke 45 | 14 % → 19 % | 10.5 px | 0.35 | 1.37 | 5 |
| stroke 46 | 5 % → 7 % | 4.0 px | 0.35 | 1.38 | 2 |
| stroke 47 | 11 % → 14 % | 8.7 px | 0.36 | 1.21 | 6 |
| stroke 48 | 13 % → 18 % | 10.0 px | 0.36 | 1.36 | 2 |
| stroke 49 | 6 % → 9 % | 4.3 px | 0.35 | 1.65 | 5 |
| stroke 50 | 7 % → 7 % | 5.6 px | 0.35 | 1.00 | 2 |
| stroke 51 | 10 % → 16 % | 7.4 px | 0.36 | 1.67 | 5 |
| stroke 52 | 14 % → 16 % | 10.5 px | 0.35 | 1.19 | 2 |
| stroke 53 | 12 % → 16 % | 9.0 px | 0.35 | 1.35 | 2 |
| stroke 54 | 11 % → 16 % | 8.5 px | 0.35 | 1.46 | 3 |
| stroke 55 | 12 % → 16 % | 9.0 px | 0.35 | 1.34 | 4 |
| stroke 56 | 12 % → 13 % | 9.0 px | 0.35 | 1.11 | 2 |
| stroke 57 | 11 % → 14 % | 8.2 px | 0.36 | 1.31 | 3 |
| stroke 58 | 11 % → 12 % | 8.6 px | 0.35 | 1.12 | 3 |
| stroke 59 | 13 % → 15 % | 9.8 px | 0.35 | 1.16 | 2 |
| stroke 60 | 17 % → 22 % | 13.1 px | 0.35 | 1.26 | 5 |
| stroke 61 | 21 % → 22 % | 15.6 px | 0.35 | 1.05 | 5 |
| stroke 62 | 10 % → 10 % | 7.5 px | 0.35 | 1.00 | 2 |
| stroke 63 | 12 % → 13 % | 9.5 px | 0.35 | 1.09 | 5 |
| stroke 64 | 16 % → 17 % | 12.4 px | 0.35 | 1.02 | 2 |
| stroke 65 | 17 % → 17 % | 12.7 px | 0.35 | 1.00 | 4 |
| stroke 66 | 15 % → 15 % | 11.9 px | 0.35 | 1.00 | 3 |
| stroke 67 | 13 % → 14 % | 9.9 px | 0.35 | 1.06 | 2 |
| stroke 68 | 5 % → 10 % | 4.1 px | 0.35 | 1.90 | 2 |
| stroke 69 | 6 % → 6 % | 4.3 px | 0.35 | 1.00 | 2 |
| stroke 70 | 11 % → 14 % | 8.5 px | 0.35 | 1.28 | 2 |
| stroke 71 | 10 % → 12 % | 7.7 px | 0.35 | 1.17 | 2 |
| stroke 72 | 6 % → 7 % | 4.5 px | 0.35 | 1.26 | 4 |
| stroke 73 | 14 % → 14 % | 10.4 px | 0.35 | 1.00 | 2 |
| stroke 74 | 16 % → 16 % | 12.3 px | 0.35 | 1.00 | 4 |
| stroke 75 | 17 % → 17 % | 13.1 px | 0.35 | 1.00 | 3 |
| stroke 76 | 15 % → 15 % | 11.7 px | 0.36 | 1.00 | 2 |
| stroke 77 | 8 % → 10 % | 6.0 px | 0.35 | 1.32 | 3 |
| stroke 78 | 10 % → 10 % | 7.5 px | 0.35 | 1.00 | 4 |
| stroke 79 | 8 % → 8 % | 6.2 px | 0.35 | 1.00 | 5 |
| stroke 80 | 12 % → 12 % | 9.1 px | 0.36 | 1.00 | 3 |

Numbers say: wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #42 Oil pastel shaggy — own sheet
own sheet 600 × 600 · Pastel 1.00 · 18 px · 2.6 s

![Brush Artist · Refs · #42 Oil pastel shaggy — own sheet](Brush-Artist-Refs-42-Oil-pastel-shaggy-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 5 % → 27 % | 8.5 px | 0.27 | 5.25 | 9 |
| stroke 2 | 5 % → 24 % | 7.8 px | 0.29 | 5.02 | 6 |
| stroke 3 | 5 % → 29 % | 8.8 px | 0.28 | 5.49 | 6 |
| stroke 4 | 5 % → 11 % | 9.1 px | 0.26 | 1.99 | 10 |
| stroke 5 | 6 % → 11 % | 10.2 px | 0.26 | 1.77 | 7 |
| stroke 6 | 8 % → 36 % | 13.4 px | 0.28 | 4.52 | 6 |
| stroke 7 | 11 % → 30 % | 18.0 px | 0.28 | 2.79 | 12 |
| stroke 8 | 7 % → 37 % | 10.8 px | 0.28 | 5.63 | 6 |
| stroke 9 | 8 % → 21 % | 13.4 px | 0.28 | 2.61 | 10 |
| stroke 10 | 8 % → 18 % | 13.2 px | 0.29 | 2.30 | 10 |
| stroke 11 | 5 % → 26 % | 8.8 px | 0.28 | 4.89 | 6 |
| stroke 12 | 8 % → 19 % | 13.1 px | 0.28 | 2.33 | 7 |
| stroke 13 | 12 % → 23 % | 20.4 px | 0.28 | 1.91 | 12 |
| stroke 14 | 5 % → 22 % | 7.6 px | 0.28 | 4.76 | 10 |
| stroke 15 | 6 % → 24 % | 9.1 px | 0.28 | 4.28 | 6 |
| stroke 16 | 9 % → 21 % | 15.5 px | 0.29 | 2.21 | 12 |
| stroke 17 | 16 % → 37 % | 26.3 px | 0.28 | 2.36 | 6 |
| stroke 18 | 14 % → 25 % | 22.6 px | 0.28 | 1.82 | 12 |
| stroke 19 | 14 % → 30 % | 23.7 px | 0.28 | 2.08 | 9 |
| stroke 20 | 21 % → 39 % | 35.4 px | 0.28 | 1.81 | 10 |
| stroke 21 | 9 % → 16 % | 14.2 px | 0.28 | 1.88 | 6 |
| stroke 22 | 14 % → 17 % | 23.1 px | 0.27 | 1.19 | 11 |
| stroke 23 | 12 % → 17 % | 20.4 px | 0.29 | 1.37 | 10 |
| stroke 24 | 18 % → 26 % | 30.0 px | 0.29 | 1.43 | 7 |
| stroke 25 | 19 % → 34 % | 32.1 px | 0.28 | 1.75 | 6 |
| stroke 26 | 5 % → 13 % | 8.8 px | 0.28 | 2.45 | 9 |
| stroke 27 | 18 % → 26 % | 30.3 px | 0.29 | 1.41 | 15 |
| stroke 28 | 14 % → 23 % | 23.2 px | 0.29 | 1.66 | 13 |
| stroke 29 | 9 % → 26 % | 14.2 px | 0.29 | 3.08 | 8 |
| stroke 30 | 15 % → 36 % | 24.5 px | 0.28 | 2.44 | 11 |
| stroke 31 | 13 % → 17 % | 22.3 px | 0.29 | 1.24 | 13 |
| stroke 32 | 16 % → 29 % | 26.3 px | 0.29 | 1.82 | 6 |
| stroke 33 | 15 % → 16 % | 24.3 px | 0.28 | 1.09 | 8 |
| stroke 34 | 19 % → 27 % | 31.4 px | 0.28 | 1.44 | 12 |
| stroke 35 | 25 % → 35 % | 40.9 px | 0.28 | 1.39 | 9 |
| stroke 36 | 24 % → 33 % | 40.2 px | 0.28 | 1.34 | 6 |
| stroke 37 | 11 % → 12 % | 18.4 px | 0.28 | 1.04 | 15 |
| stroke 38 | 19 % → 24 % | 30.7 px | 0.29 | 1.31 | 8 |
| stroke 39 | 16 % → 22 % | 27.0 px | 0.27 | 1.35 | 13 |
| stroke 40 | 21 % → 29 % | 34.9 px | 0.28 | 1.37 | 10 |
| stroke 41 | 31 % → 34 % | 51.2 px | 0.28 | 1.12 | 10 |
| stroke 42 | 23 % → 29 % | 37.9 px | 0.28 | 1.28 | 6 |
| stroke 43 | 12 % → 12 % | 20.2 px | 0.28 | 1.00 | 15 |
| stroke 44 | 29 % → 36 % | 48.3 px | 0.28 | 1.24 | 6 |
| stroke 45 | 16 % → 16 % | 25.6 px | 0.27 | 1.00 | 6 |
| stroke 46 | 28 % → 33 % | 46.9 px | 0.28 | 1.15 | 12 |
| stroke 47 | 37 % → 41 % | 61.6 px | 0.28 | 1.09 | 6 |
| stroke 48 | 28 % → 35 % | 47.2 px | 0.28 | 1.26 | 8 |
| stroke 49 | 27 % → 30 % | 43.8 px | 0.29 | 1.11 | 9 |
| stroke 50 | 37 % → 40 % | 61.8 px | 0.28 | 1.07 | 8 |
| stroke 51 | 15 % → 15 % | 25.8 px | 0.28 | 1.00 | 11 |
| stroke 52 | 37 % → 37 % | 61.4 px | 0.28 | 1.01 | 8 |
| stroke 53 | 22 % → 26 % | 35.6 px | 0.29 | 1.20 | 6 |
| stroke 54 | 17 % → 19 % | 29.0 px | 0.29 | 1.10 | 8 |
| stroke 55 | 15 % → 15 % | 24.6 px | 0.29 | 1.00 | 12 |
| stroke 56 | 13 % → 14 % | 21.3 px | 0.27 | 1.08 | 9 |
| stroke 57 | 23 % → 23 % | 38.0 px | 0.29 | 1.00 | 6 |
| stroke 58 | 26 % → 28 % | 43.7 px | 0.28 | 1.06 | 10 |
| stroke 59 | 40 % → 40 % | 66.1 px | 0.28 | 1.00 | 10 |
| stroke 60 | 21 % → 21 % | 34.4 px | 0.29 | 1.00 | 6 |

Numbers say: wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #43 Dragged black ink blocks — own sheet
own sheet 600 × 600 · Gouache 1.00 · 70 px · 6.2 s

![Brush Artist · Refs · #43 Dragged black ink blocks — own sheet](Brush-Artist-Refs-43-Dragged-black-ink-blocks-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 11 % → 4 % | 24.9 px | 0.46 | 0.40 | 323 |
| stroke 2 | 10 % → 8 % | 35.4 px | 0.46 | 0.82 | 385 |
| stroke 3 | 18 % → 14 % | 66.1 px | 0.46 | 0.77 | 382 |
| stroke 4 | 22 % → 11 % | 75.0 px | 0.43 | 0.53 | 440 |
| stroke 5 | 31 % → 13 % | 72.0 px | 0.43 | 0.43 | 398 |

## Brush Artist · Refs · #44 Blue looping ribbon — own sheet
own sheet 600 × 600 · Oil 1.00 · 80 px · 4.4 s

![Brush Artist · Refs · #44 Blue looping ribbon — own sheet](Brush-Artist-Refs-44-Blue-looping-ribbon-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 32 % → 32 % | 42.1 px | 0.78 | 1.00 | 2392 |

## Brush Artist · Refs · #45 Soft pastel pepper — own sheet
own sheet 600 × 600 · Pastel 1.00 · 40 px · 4.5 s

![Brush Artist · Refs · #45 Soft pastel pepper — own sheet](Brush-Artist-Refs-45-Soft-pastel-pepper-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 10 % → 38 % | 11.3 px | 0.50 | 3.71 | 279 |
| stroke 2 | 18 % → 33 % | 20.7 px | 0.50 | 1.88 | 266 |
| stroke 3 | 25 % → 36 % | 16.9 px | 0.50 | 1.46 | 274 |
| stroke 4 | 24 % → 34 % | 29.4 px | 0.50 | 1.45 | 332 |
| stroke 5 | 30 % → 30 % | 20.9 px | 0.49 | 1.00 | 228 |
| stroke 6 | 35 % → 44 % | 22.7 px | 0.50 | 1.24 | 300 |
| stroke 7 | 39 % → 43 % | 21.3 px | 0.50 | 1.11 | 415 |
| stroke 8 | 43 % → 43 % | 43.7 px | 0.50 | 1.00 | 492 |

Numbers say: wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #46 Red-brown ink lips — own sheet
own sheet 600 × 600 · Watercolour 1.00 · 50 px · 7.7 s

![Brush Artist · Refs · #46 Red-brown ink lips — own sheet](Brush-Artist-Refs-46-Red-brown-ink-lips-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 13 % → 26 % | 54.5 px | 0.56 | 1.96 | 100 |
| stroke 2 | 17 % → 31 % | 72.4 px | 0.53 | 1.89 | 77 |

Numbers say: wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #47 Pink knife slabs — own sheet
own sheet 600 × 600 · Impasto 1.00 · 90 px · 4.3 s

![Brush Artist · Refs · #47 Pink knife slabs — own sheet](Brush-Artist-Refs-47-Pink-knife-slabs-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 16 % → 32 % | 81.5 px | 0.10 | 1.97 | 268 |
| stroke 2 | 29 % → 42 % | 165.6 px | 0.11 | 1.45 | 253 |
| stroke 3 | 29 % → 43 % | 165.1 px | 0.13 | 1.47 | 340 |
| stroke 4 | 39 % → 38 % | 165.8 px | 0.14 | 0.97 | 298 |

Numbers say: wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #48 Black bands with drips — own sheet
own sheet 600 × 600 · Gouache 1.00 · 70 px · 12.4 s

![Brush Artist · Refs · #48 Black bands with drips — own sheet](Brush-Artist-Refs-48-Black-bands-with-drips-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 28 % → 40 % | 72.6 px | 0.38 | 1.43 | 468 |
| stroke 2 | 43 % → 55 % | 137.3 px | 0.38 | 1.30 | 412 |
| stroke 3 | 45 % → 56 % | 141.4 px | 0.38 | 1.23 | 611 |
| stroke 4 | 48 % → 45 % | 139.2 px | 0.37 | 0.94 | 560 |

## Brush Artist · Refs · #49 Magenta letters round brush — own sheet
own sheet 600 × 600 · Ink 1.00 · 30 px · 10.1 s

![Brush Artist · Refs · #49 Magenta letters round brush — own sheet](Brush-Artist-Refs-49-Magenta-letters-round-brush-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 27 % → 46 % | 64.7 px | 0.52 | 1.68 | 33 |
| stroke 2 | 29 % → 41 % | 53.0 px | 0.53 | 1.40 | 28 |
| stroke 3 | 42 % → 68 % | 98.0 px | 0.52 | 1.62 | 31 |
| stroke 4 | 33 % → 52 % | 53.5 px | 0.52 | 1.56 | 110 |
| stroke 5 | 41 % → 66 % | 97.1 px | 0.52 | 1.62 | 67 |
| stroke 6 | 56 % → 72 % | 237.9 px | 0.52 | 1.28 | 15 |
| stroke 7 | 42 % → 58 % | 65.1 px | 0.52 | 1.36 | 104 |
| stroke 8 | 36 % → 61 % | 92.6 px | 0.53 | 1.71 | 70 |
| stroke 9 | 50 % → 62 % | 156.5 px | 0.52 | 1.24 | 25 |
| stroke 10 | 43 % → 73 % | 102.9 px | 0.52 | 1.68 | 77 |
| stroke 11 | 52 % → 72 % | 221.9 px | 0.52 | 1.39 | 19 |
| stroke 12 | 54 % → 70 % | 84.9 px | 0.52 | 1.28 | 112 |
| stroke 13 | 42 % → 53 % | 116.2 px | 0.53 | 1.27 | 38 |
| stroke 14 | 45 % → 68 % | 131.6 px | 0.53 | 1.52 | 39 |
| stroke 15 | 43 % → 63 % | 101.8 px | 0.52 | 1.47 | 80 |
| stroke 16 | 52 % → 61 % | 220.3 px | 0.52 | 1.19 | 21 |
| stroke 17 | 53 % → 64 % | 82.3 px | 0.52 | 1.19 | 124 |
| stroke 18 | 36 % → 43 % | 98.8 px | 0.53 | 1.20 | 32 |
| stroke 19 | 53 % → 52 % | 122.0 px | 0.52 | 0.99 | 32 |
| stroke 20 | 55 % → 55 % | 127.4 px | 0.52 | 1.00 | 35 |
| stroke 21 | 49 % → 49 % | 80.4 px | 0.52 | 1.00 | 93 |

Numbers say: wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #50 Thick swipes on photo — own sheet
own sheet 600 × 600 · Impasto 1.00 · 40 px · 3.1 s

![Brush Artist · Refs · #50 Thick swipes on photo — own sheet](Brush-Artist-Refs-50-Thick-swipes-on-photo-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 9 % → 21 % | 43.0 px | 0.35 | 2.32 | 31 |
| stroke 2 | 9 % → 16 % | 42.2 px | 0.34 | 1.82 | 27 |
| stroke 3 | 10 % → 11 % | 42.0 px | 0.32 | 1.06 | 46 |
| stroke 4 | 11 % → 18 % | 44.0 px | 0.35 | 1.60 | 32 |
| stroke 5 | 11 % → 10 % | 42.2 px | 0.34 | 0.94 | 37 |
| stroke 6 | 17 % → 21 % | 99.5 px | 0.35 | 1.19 | 30 |
| stroke 7 | 22 % → 26 % | 92.9 px | 0.35 | 1.18 | 55 |
| stroke 8 | 21 % → 20 % | 119.7 px | 0.35 | 0.96 | 40 |
| stroke 9 | 10 % → 11 % | 43.0 px | 0.30 | 1.11 | 46 |
| stroke 10 | 22 % → 22 % | 75.4 px | 0.35 | 0.96 | 58 |
| stroke 11 | 8 % → 8 % | 41.8 px | 0.36 | 0.95 | 41 |
| stroke 12 | 17 % → 16 % | 94.4 px | 0.35 | 0.96 | 29 |

Numbers say: wet paint spreads well beyond the stroke.

## Brush Artist · Ink — dry brush — own sheet
own sheet 600 × 600 · Gouache 1.00 · 30 px · 3.2 s

![Brush Artist · Ink — dry brush — own sheet](Brush-Artist-Ink-dry-brush-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| ear | 8 % → 2 % | 9.7 px | 0.85 | 0.22 | 563 |
| drag0 | 4 % → 6 % | 7.6 px | 0.85 | 1.51 | 132 |
| drag1 | 7 % → 7 % | 15.1 px | 0.85 | 0.89 | 93 |
| drag2 | 10 % → 7 % | 22.1 px | 0.85 | 0.71 | 83 |
| drag3 | 12 % → 7 % | 30.1 px | 0.85 | 0.60 | 67 |

Numbers say: wet paint spreads well beyond the stroke.

## Brush Artist · Watercolour — blue — own sheet
own sheet 600 × 600 · Watercolour 0.93 · Ink 0.07 · 40 px · 11.8 s

![Brush Artist · Watercolour — blue — own sheet](Brush-Artist-Watercolour-blue-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| s0 | 7 % → 24 % | 28.8 px | 0.30 | 3.32 | 44 |
| s1 | 6 % → 33 % | 10.1 px | 0.37 | 6.00 | 50 |
| s2 | 10 % → 19 % | 44.2 px | 0.26 | 1.81 | 37 |
| s3 | 10 % → 18 % | 26.7 px | 0.31 | 1.92 | 55 |
| s4 | 14 % → 30 % | 38.6 px | 0.36 | 2.16 | 57 |
| s5 | 19 % → 29 % | 39.3 px | 0.37 | 1.54 | 45 |
| s6 | 18 % → 22 % | 48.7 px | 0.31 | 1.25 | 51 |
| s7 | 25 % → 36 % | 32.7 px | 0.37 | 1.46 | 44 |
| s8 | 21 % → 25 % | 79.8 px | 0.30 | 1.20 | 63 |

Numbers say: wet paint spreads well beyond the stroke.

## Brush Artist · Charcoal — stick — own sheet
own sheet 600 × 600 · Charcoal 0.78 · Pastel 0.22 · 28 px · 1.4 s

![Brush Artist · Charcoal — stick — own sheet](Brush-Artist-Charcoal-stick-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| finger0 | 12 % → 25 % | 21.2 px | 0.83 | 2.03 | 45 |
| tip0 | 13 % → 21 % | 33.8 px | 0.83 | 1.70 | 9 |
| finger1 | 23 % → 41 % | 40.4 px | 0.83 | 1.77 | 50 |
| tip1 | 21 % → 29 % | 57.3 px | 0.83 | 1.38 | 8 |
| finger2 | 25 % → 37 % | 43.8 px | 0.83 | 1.49 | 44 |
| tip2 | 21 % → 29 % | 55.7 px | 0.83 | 1.40 | 12 |
| finger3 | 24 % → 27 % | 42.7 px | 0.83 | 1.14 | 41 |
| tip3 | 20 % → 20 % | 54.1 px | 0.83 | 1.00 | 11 |
| cig0 | 34 % → 47 % | 75.0 px | 0.83 | 1.39 | 16 |
| cig1 | 36 % → 47 % | 80.5 px | 0.83 | 1.30 | 12 |
| cig2 | 39 % → 47 % | 86.7 px | 0.83 | 1.20 | 16 |
| cig3 | 41 % → 47 % | 91.3 px | 0.83 | 1.14 | 16 |
| cig4 | 44 % → 46 % | 97.5 px | 0.83 | 1.06 | 19 |
| cig5 | 46 % → 46 % | 102.9 px | 0.83 | 1.00 | 14 |

Numbers say: wet paint spreads well beyond the stroke.

## Oil · Henry Ward · HW #02 cream over wet olive — own sheet
own sheet 600 × 600 · Oil 0.81 · Ink 0.19 · 56 px · 30.0 s

![Oil · Henry Ward · HW #02 cream over wet olive — own sheet](Oil-Henry-Ward-HW-02-cream-over-wet-olive-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 67 % → 28 % | 84.7 px | 0.38 | 0.41 | 1379 |
| stroke 2 | 77 % → 38 % | 141.4 px | 0.45 | 0.49 | 2054 |
| stroke 3 | 80 % → 51 % | 167.2 px | 0.41 | 0.64 | 2358 |
| stroke 4 | 81 % → 57 % | 170.2 px | 0.43 | 0.70 | 2539 |
| stroke 5 | 79 % → 50 % | 168.1 px | 0.44 | 0.63 | 2536 |
| stroke 6 | 80 % → 48 % | 167.5 px | 0.48 | 0.60 | 2523 |
| stroke 7 | 81 % → 35 % | 171.2 px | 0.48 | 0.43 | 2056 |
| stroke 8 | 92 % → 24 % | 168.8 px | 0.47 | 0.26 | 2206 |
| stroke 9 | 100 % → 9 % | 115.6 px | 0.33 | 0.09 | 1544 |
| stroke 10 | 9 % → 43 % | 37.2 px | 0.41 | 4.53 | 260 |
| stroke 11 | 16 % → 58 % | 64.6 px | 0.43 | 3.67 | 309 |
| stroke 12 | 5 % → 34 % | 23.2 px | 0.48 | 6.36 | 145 |
| stroke 13 | 26 % → 48 % | 104.6 px | 0.41 | 1.82 | 206 |
| stroke 14 | 32 % → 50 % | 115.3 px | 0.41 | 1.57 | 231 |
| stroke 15 | 39 % → 58 % | 144.4 px | 0.42 | 1.50 | 234 |
| stroke 16 | 45 % → 68 % | 227.5 px | 0.42 | 1.50 | 170 |
| stroke 17 | 32 % → 55 % | 115.5 px | 0.45 | 1.71 | 209 |
| stroke 18 | 31 % → 59 % | 120.6 px | 0.44 | 1.93 | 206 |
| stroke 19 | 31 % → 54 % | 146.3 px | 0.44 | 1.71 | 149 |
| stroke 20 | 31 % → 37 % | 121.1 px | 0.49 | 1.18 | 217 |
| stroke 21 | 32 % → 33 % | 114.5 px | 0.49 | 1.03 | 282 |
| stroke 22 | 43 % → 43 % | 142.5 px | 0.41 | 1.02 | 251 |
| stroke 23 | 51 % → 55 % | 184.7 px | 0.41 | 1.07 | 243 |
| stroke 24 | 52 % → 56 % | 227.1 px | 0.45 | 1.08 | 164 |
| stroke 25 | 52 % → 52 % | 195.7 px | 0.45 | 1.01 | 250 |
| stroke 26 | 35 % → 34 % | 145.2 px | 0.49 | 0.98 | 258 |

Numbers say: wet paint spreads well beyond the stroke.

## Oil · Henry Ward · HW #04 grey arcs over ochre — own sheet
own sheet 600 × 600 · Oil 1.00 · 46 px · 30.4 s

![Oil · Henry Ward · HW #04 grey arcs over ochre — own sheet](Oil-Henry-Ward-HW-04-grey-arcs-over-ochre-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 76 % → 41 % | 82.7 px | 0.20 | 0.54 | 1375 |
| stroke 2 | 87 % → 55 % | 143.0 px | 0.20 | 0.64 | 2071 |
| stroke 3 | 88 % → 77 % | 154.8 px | 0.19 | 0.87 | 2280 |
| stroke 4 | 88 % → 59 % | 154.7 px | 0.19 | 0.67 | 2568 |
| stroke 5 | 87 % → 38 % | 152.6 px | 0.16 | 0.43 | 2398 |
| stroke 6 | 85 % → 24 % | 149.8 px | 0.12 | 0.28 | 2583 |
| stroke 7 | 87 % → 30 % | 154.7 px | 0.10 | 0.35 | 2092 |
| stroke 8 | 90 % → 27 % | 149.9 px | 0.10 | 0.30 | 2371 |
| stroke 9 | 100 % → 24 % | 104.1 px | 0.10 | 0.24 | 1627 |
| stroke 10 | 10 % → 68 % | 37.2 px | 0.20 | 6.86 | 214 |
| stroke 11 | 17 % → 57 % | 59.0 px | 0.19 | 3.35 | 243 |
| stroke 12 | 19 % → 52 % | 70.5 px | 0.17 | 2.78 | 144 |
| stroke 13 | 33 % → 66 % | 90.2 px | 0.20 | 2.02 | 363 |
| stroke 14 | 39 % → 64 % | 150.1 px | 0.19 | 1.65 | 269 |
| stroke 15 | 39 % → 58 % | 135.8 px | 0.19 | 1.47 | 316 |
| stroke 16 | 45 % → 59 % | 168.0 px | 0.19 | 1.31 | 205 |
| stroke 17 | 50 % → 65 % | 187.7 px | 0.19 | 1.30 | 280 |
| stroke 18 | 50 % → 60 % | 171.7 px | 0.19 | 1.20 | 208 |
| stroke 19 | 57 % → 67 % | 185.6 px | 0.20 | 1.19 | 348 |
| stroke 20 | 59 % → 71 % | 183.3 px | 0.20 | 1.20 | 351 |
| stroke 21 | 63 % → 75 % | 205.4 px | 0.20 | 1.18 | 322 |
| stroke 22 | 34 % → 48 % | 122.0 px | 0.17 | 1.44 | 216 |
| stroke 23 | 57 % → 64 % | 206.6 px | 0.19 | 1.13 | 332 |
| stroke 24 | 74 % → 79 % | 283.8 px | 0.20 | 1.06 | 174 |
| stroke 25 | 52 % → 60 % | 179.8 px | 0.18 | 1.14 | 249 |
| stroke 26 | 72 % → 74 % | 250.9 px | 0.19 | 1.03 | 251 |
| stroke 27 | 19 % → 27 % | 60.1 px | 0.13 | 1.37 | 152 |
| stroke 28 | 19 % → 36 % | 67.4 px | 0.10 | 1.91 | 152 |
| stroke 29 | 21 % → 31 % | 86.1 px | 0.11 | 1.46 | 112 |
| stroke 30 | 30 % → 30 % | 87.6 px | 0.10 | 1.00 | 222 |

Numbers say: wet paint spreads well beyond the stroke.

## Oil · Henry Ward · HW #09 white arches over wet blue-grey — own sheet
own sheet 600 × 600 · Oil 1.00 · 46 px · 31.2 s

![Oil · Henry Ward · HW #09 white arches over wet blue-grey — own sheet](Oil-Henry-Ward-HW-09-white-arches-over-wet-blue-grey-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 79 % → 0 % | 81.3 px | 0.10 | 0.00 | 1388 |
| stroke 2 | 86 % → 5 % | 141.4 px | 0.09 | 0.06 | 2043 |
| stroke 3 | 87 % → 22 % | 154.6 px | 0.09 | 0.26 | 2244 |
| stroke 4 | 88 % → 39 % | 157.2 px | 0.09 | 0.45 | 2512 |
| stroke 5 | 85 % → 54 % | 150.6 px | 0.10 | 0.64 | 2467 |
| stroke 6 | 86 % → 63 % | 148.5 px | 0.10 | 0.73 | 2524 |
| stroke 7 | 87 % → 64 % | 152.0 px | 0.11 | 0.74 | 2093 |
| stroke 8 | 89 % → 58 % | 151.3 px | 0.13 | 0.65 | 2140 |
| stroke 9 | 100 % → 50 % | 99.7 px | 0.17 | 0.50 | 1499 |
| stroke 10 | 8 % → 53 % | 30.0 px | 0.11 | 6.96 | 402 |
| stroke 11 | 17 % → 64 % | 31.1 px | 0.11 | 3.79 | 435 |
| stroke 12 | 19 % → 61 % | 35.0 px | 0.11 | 3.15 | 496 |
| stroke 13 | 27 % → 75 % | 60.7 px | 0.12 | 2.73 | 307 |
| stroke 14 | 31 % → 69 % | 22.1 px | 0.12 | 2.26 | 527 |
| stroke 15 | 39 % → 74 % | 108.1 px | 0.11 | 1.92 | 374 |
| stroke 16 | 48 % → 67 % | 142.9 px | 0.12 | 1.41 | 340 |
| stroke 17 | 57 % → 85 % | 162.7 px | 0.11 | 1.50 | 315 |
| stroke 18 | 49 % → 68 % | 132.3 px | 0.11 | 1.41 | 473 |
| stroke 19 | 53 % → 65 % | 163.9 px | 0.11 | 1.21 | 324 |
| stroke 20 | 49 % → 69 % | 128.4 px | 0.11 | 1.40 | 487 |
| stroke 21 | 39 % → 56 % | 99.1 px | 0.10 | 1.45 | 326 |
| stroke 22 | 50 % → 57 % | 135.0 px | 0.10 | 1.14 | 411 |
| stroke 23 | 69 % → 75 % | 216.7 px | 0.11 | 1.09 | 541 |
| stroke 24 | 66 % → 69 % | 210.9 px | 0.10 | 1.05 | 208 |
| stroke 25 | 57 % → 63 % | 159.9 px | 0.11 | 1.11 | 266 |
| stroke 26 | 64 % → 72 % | 244.9 px | 0.13 | 1.14 | 179 |
| stroke 27 | 52 % → 58 % | 127.1 px | 0.13 | 1.11 | 379 |
| stroke 28 | 59 % → 59 % | 136.6 px | 0.14 | 1.00 | 244 |

Numbers say: wet paint spreads well beyond the stroke.

## Oil · Henry Ward · HW #03 navy contours over wet band — own sheet
own sheet 600 × 600 · Oil 1.00 · 46 px · 24.8 s

![Oil · Henry Ward · HW #03 navy contours over wet band — own sheet](Oil-Henry-Ward-HW-03-navy-contours-over-wet-band-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 78 % → 19 % | 78.7 px | 0.74 | 0.24 | 1313 |
| stroke 2 | 87 % → 23 % | 145.7 px | 0.72 | 0.26 | 2075 |
| stroke 3 | 85 % → 28 % | 150.3 px | 0.63 | 0.33 | 2344 |
| stroke 4 | 86 % → 38 % | 150.8 px | 0.56 | 0.45 | 2493 |
| stroke 5 | 85 % → 42 % | 150.1 px | 0.49 | 0.50 | 2591 |
| stroke 6 | 87 % → 35 % | 153.4 px | 0.52 | 0.40 | 2379 |
| stroke 7 | 87 % → 22 % | 150.0 px | 0.57 | 0.25 | 1837 |
| stroke 8 | 89 % → 9 % | 150.6 px | 0.72 | 0.10 | 2250 |
| stroke 9 | 100 % → 3 % | 104.1 px | 0.71 | 0.03 | 1529 |
| stroke 10 | 9 % → 40 % | 39.4 px | 0.52 | 4.31 | 122 |
| stroke 11 | 18 % → 50 % | 68.5 px | 0.49 | 2.76 | 136 |
| stroke 12 | 22 % → 43 % | 79.1 px | 0.48 | 1.96 | 144 |
| stroke 13 | 26 % → 41 % | 90.5 px | 0.52 | 1.58 | 190 |
| stroke 14 | 15 % → 32 % | 48.7 px | 0.74 | 2.18 | 74 |
| stroke 15 | 19 % → 32 % | 67.7 px | 0.73 | 1.70 | 92 |
| stroke 16 | 28 % → 29 % | 62.6 px | 0.57 | 1.04 | 396 |
| stroke 17 | 32 % → 32 % | 84.0 px | 0.57 | 1.00 | 310 |

Numbers say: wet paint spreads well beyond the stroke.

## Oil · Henry Ward · HW #01 peach cloud and legs over teal — own sheet
own sheet 600 × 600 · Oil 1.00 · 46 px · 27.9 s

![Oil · Henry Ward · HW #01 peach cloud and legs over teal — own sheet](Oil-Henry-Ward-HW-01-peach-cloud-and-legs-over-teal-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 81 % → 40 % | 88.3 px | 0.39 | 0.50 | 1570 |
| stroke 2 | 86 % → 48 % | 146.6 px | 0.40 | 0.57 | 2136 |
| stroke 3 | 86 % → 62 % | 150.8 px | 0.39 | 0.72 | 2380 |
| stroke 4 | 88 % → 58 % | 152.6 px | 0.39 | 0.66 | 2684 |
| stroke 5 | 85 % → 47 % | 150.6 px | 0.37 | 0.56 | 2601 |
| stroke 6 | 87 % → 34 % | 151.3 px | 0.36 | 0.39 | 2192 |
| stroke 7 | 87 % → 26 % | 154.5 px | 0.30 | 0.30 | 1987 |
| stroke 8 | 92 % → 23 % | 150.7 px | 0.23 | 0.25 | 2259 |
| stroke 9 | 100 % → 26 % | 103.2 px | 0.18 | 0.26 | 1736 |
| stroke 10 | 17 % → 51 % | 39.5 px | 0.39 | 3.04 | 203 |
| stroke 11 | 21 % → 58 % | 72.4 px | 0.40 | 2.76 | 183 |
| stroke 12 | 28 % → 63 % | 98.6 px | 0.40 | 2.23 | 194 |
| stroke 13 | 39 % → 75 % | 135.9 px | 0.40 | 1.94 | 179 |
| stroke 14 | 38 % → 69 % | 125.1 px | 0.39 | 1.79 | 173 |
| stroke 15 | 43 % → 70 % | 165.0 px | 0.39 | 1.62 | 107 |
| stroke 16 | 38 % → 62 % | 138.5 px | 0.39 | 1.61 | 151 |
| stroke 17 | 49 % → 52 % | 133.6 px | 0.39 | 1.07 | 246 |
| stroke 18 | 60 % → 63 % | 239.7 px | 0.40 | 1.05 | 138 |
| stroke 19 | 53 % → 63 % | 214.5 px | 0.39 | 1.20 | 128 |
| stroke 20 | 47 % → 72 % | 160.8 px | 0.39 | 1.52 | 211 |
| stroke 21 | 27 % → 42 % | 88.8 px | 0.35 | 1.54 | 168 |
| stroke 22 | 48 % → 64 % | 168.3 px | 0.35 | 1.33 | 187 |
| stroke 23 | 45 % → 59 % | 140.7 px | 0.35 | 1.30 | 202 |
| stroke 24 | 51 % → 62 % | 188.1 px | 0.37 | 1.20 | 131 |
| stroke 25 | 44 % → 57 % | 155.8 px | 0.37 | 1.30 | 135 |
| stroke 26 | 35 % → 39 % | 121.8 px | 0.37 | 1.11 | 135 |
| stroke 27 | 26 % → 29 % | 49.8 px | 0.24 | 1.15 | 146 |
| stroke 28 | 24 % → 24 % | 48.7 px | 0.22 | 1.00 | 134 |

Numbers say: wet paint spreads well beyond the stroke.

## Oil · Henry Ward · HW #05 rust, pink, green-black — own sheet
own sheet 600 × 600 · Oil 1.00 · 46 px · 28.8 s

![Oil · Henry Ward · HW #05 rust, pink, green-black — own sheet](Oil-Henry-Ward-HW-05-rust-pink-green-black-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 80 % → 45 % | 83.9 px | 0.60 | 0.56 | 1578 |
| stroke 2 | 87 % → 51 % | 148.1 px | 0.61 | 0.58 | 2011 |
| stroke 3 | 85 % → 61 % | 150.8 px | 0.50 | 0.72 | 2395 |
| stroke 4 | 87 % → 53 % | 151.4 px | 0.35 | 0.61 | 2554 |
| stroke 5 | 87 % → 43 % | 153.5 px | 0.24 | 0.50 | 2577 |
| stroke 6 | 86 % → 43 % | 149.1 px | 0.50 | 0.50 | 2077 |
| stroke 7 | 87 % → 51 % | 150.7 px | 0.68 | 0.59 | 2037 |
| stroke 8 | 91 % → 52 % | 150.2 px | 0.69 | 0.57 | 2192 |
| stroke 9 | 100 % → 45 % | 100.6 px | 0.68 | 0.45 | 1669 |
| stroke 10 | 16 % → 60 % | 39.6 px | 0.61 | 3.71 | 187 |
| stroke 11 | 22 % → 52 % | 64.8 px | 0.61 | 2.39 | 226 |
| stroke 12 | 32 % → 61 % | 105.7 px | 0.56 | 1.94 | 225 |
| stroke 13 | 34 % → 52 % | 110.3 px | 0.60 | 1.50 | 272 |
| stroke 14 | 40 % → 78 % | 159.5 px | 0.49 | 1.95 | 137 |
| stroke 15 | 35 % → 58 % | 124.0 px | 0.46 | 1.66 | 226 |
| stroke 16 | 65 % → 69 % | 237.5 px | 0.62 | 1.07 | 76 |
| stroke 17 | 63 % → 66 % | 196.2 px | 0.62 | 1.05 | 94 |
| stroke 18 | 63 % → 70 % | 206.8 px | 0.60 | 1.11 | 125 |
| stroke 19 | 60 % → 75 % | 261.3 px | 0.54 | 1.25 | 65 |
| stroke 20 | 49 % → 73 % | 182.3 px | 0.46 | 1.50 | 125 |
| stroke 21 | 34 % → 53 % | 107.1 px | 0.32 | 1.55 | 224 |
| stroke 22 | 42 % → 57 % | 135.4 px | 0.33 | 1.37 | 226 |
| stroke 23 | 48 % → 64 % | 181.5 px | 0.26 | 1.35 | 133 |
| stroke 24 | 34 % → 54 % | 134.7 px | 0.28 | 1.58 | 113 |
| stroke 25 | 33 % → 52 % | 108.6 px | 0.32 | 1.61 | 182 |
| stroke 26 | 37 % → 61 % | 146.2 px | 0.37 | 1.64 | 139 |
| stroke 27 | 24 % → 41 % | 44.5 px | 0.40 | 1.73 | 204 |
| stroke 28 | 26 % → 55 % | 14.9 px | 0.50 | 2.11 | 202 |
| stroke 29 | 28 % → 51 % | 91.2 px | 0.57 | 1.77 | 247 |
| stroke 30 | 35 % → 58 % | 108.5 px | 0.66 | 1.66 | 196 |
| stroke 31 | 40 % → 59 % | 134.3 px | 0.70 | 1.47 | 210 |
| stroke 32 | 43 % → 63 % | 156.9 px | 0.78 | 1.46 | 138 |
| stroke 33 | 46 % → 57 % | 138.2 px | 0.69 | 1.24 | 216 |
| stroke 34 | 63 % → 63 % | 162.6 px | 0.69 | 1.00 | 256 |

Numbers say: wet paint spreads well beyond the stroke.

## Oil · Henry Ward · HW #07 blue L and zigzag on lilac — own sheet
own sheet 600 × 600 · Oil 1.00 · 50 px · 25.8 s

![Oil · Henry Ward · HW #07 blue L and zigzag on lilac — own sheet](Oil-Henry-Ward-HW-07-blue-L-and-zigzag-on-lilac-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 73 % → 21 % | 81.9 px | 0.08 | 0.29 | 1526 |
| stroke 2 | 84 % → 20 % | 147.6 px | 0.20 | 0.23 | 2140 |
| stroke 3 | 84 % → 28 % | 157.0 px | 0.36 | 0.33 | 2358 |
| stroke 4 | 85 % → 28 % | 159.8 px | 0.53 | 0.33 | 2575 |
| stroke 5 | 84 % → 38 % | 157.3 px | 0.39 | 0.45 | 2489 |
| stroke 6 | 85 % → 40 % | 163.3 px | 0.32 | 0.47 | 2011 |
| stroke 7 | 84 % → 44 % | 157.7 px | 0.16 | 0.53 | 1947 |
| stroke 8 | 93 % → 38 % | 156.9 px | 0.15 | 0.41 | 2206 |
| stroke 9 | 100 % → 38 % | 109.4 px | 0.06 | 0.38 | 1600 |
| stroke 10 | 5 % → 20 % | 12.8 px | 0.14 | 3.58 | 193 |
| stroke 11 | 11 % → 21 % | 34.7 px | 0.30 | 1.96 | 240 |
| stroke 12 | 13 % → 37 % | 46.0 px | 0.43 | 2.88 | 132 |
| stroke 13 | 6 % → 36 % | 24.4 px | 0.40 | 5.57 | 193 |
| stroke 14 | 12 % → 41 % | 40.4 px | 0.33 | 3.50 | 253 |
| stroke 15 | 14 % → 44 % | 52.4 px | 0.18 | 3.13 | 185 |
| stroke 16 | 19 % → 37 % | 53.5 px | 0.15 | 1.92 | 283 |
| stroke 17 | 35 % → 42 % | 81.8 px | 0.14 | 1.20 | 211 |
| stroke 18 | 30 % → 41 % | 101.4 px | 0.23 | 1.36 | 158 |
| stroke 19 | 43 % → 48 % | 161.7 px | 0.15 | 1.11 | 119 |
| stroke 20 | 33 % → 33 % | 72.9 px | 0.38 | 1.00 | 357 |
| stroke 21 | 25 % → 37 % | 133.9 px | 0.29 | 1.48 | 88 |
| stroke 22 | 35 % → 43 % | 178.3 px | 0.25 | 1.22 | 111 |
| stroke 23 | 36 % → 44 % | 232.3 px | 0.27 | 1.25 | 65 |
| stroke 24 | 42 % → 50 % | 239.4 px | 0.24 | 1.19 | 52 |
| stroke 25 | 41 % → 42 % | 199.1 px | 0.22 | 1.03 | 82 |
| stroke 26 | 43 % → 43 % | 240.9 px | 0.21 | 1.00 | 74 |

Numbers say: wet paint spreads well beyond the stroke.

## Oil · Henry Ward · HW #08 crown and dark oval — own sheet
own sheet 600 × 600 · Oil 1.00 · 46 px · 23.8 s

![Oil · Henry Ward · HW #08 crown and dark oval — own sheet](Oil-Henry-Ward-HW-08-crown-and-dark-oval-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 79 % → 0 % | 82.1 px | 0.00 | 0.00 | 1562 |
| stroke 2 | 87 % → 0 % | 144.8 px | 0.00 | 0.00 | 2285 |
| stroke 3 | 87 % → 0 % | 150.8 px | 0.00 | 0.00 | 2607 |
| stroke 4 | 88 % → 5 % | 154.6 px | 0.12 | 0.06 | 2151 |
| stroke 5 | 86 % → 12 % | 151.0 px | 0.14 | 0.14 | 2217 |
| stroke 6 | 88 % → 18 % | 155.2 px | 0.16 | 0.21 | 1966 |
| stroke 7 | 88 % → 13 % | 151.1 px | 0.17 | 0.14 | 1852 |
| stroke 8 | 93 % → 4 % | 149.4 px | 0.17 | 0.05 | 1812 |
| stroke 9 | 100 % → 0 % | 101.5 px | 0.20 | 0.00 | 1418 |
| stroke 10 | 15 % → 0 % | 41.0 px | 0.00 | 0.00 | 151 |
| stroke 11 | 20 % → 0 % | 66.2 px | 0.00 | 0.00 | 121 |
| stroke 12 | 22 % → 0 % | 81.6 px | 0.00 | 0.00 | 145 |
| stroke 13 | 33 % → 0 % | 132.8 px | 0.00 | 0.00 | 133 |
| stroke 14 | 38 % → 0 % | 153.7 px | 0.00 | 0.00 | 136 |
| stroke 15 | 30 % → 0 % | 117.1 px | 0.18 | 0.01 | 144 |
| stroke 16 | 10 % → 9 % | 25.5 px | 0.16 | 0.90 | 363 |
| stroke 17 | 23 % → 16 % | 77.6 px | 0.15 | 0.69 | 174 |
| stroke 18 | 30 % → 21 % | 114.9 px | 0.16 | 0.69 | 139 |
| stroke 19 | 42 % → 24 % | 162.0 px | 0.16 | 0.57 | 108 |
| stroke 20 | 44 % → 21 % | 160.9 px | 0.17 | 0.48 | 135 |
| stroke 21 | 49 % → 23 % | 231.0 px | 0.17 | 0.46 | 78 |
| stroke 22 | 43 % → 18 % | 211.3 px | 0.16 | 0.41 | 75 |
| stroke 23 | 7 % → 19 % | 25.5 px | 0.16 | 2.91 | 165 |
| stroke 24 | 11 % → 25 % | 48.6 px | 0.16 | 2.14 | 86 |
| stroke 25 | 18 % → 28 % | 85.3 px | 0.16 | 1.56 | 69 |
| stroke 26 | 20 % → 24 % | 76.9 px | 0.16 | 1.24 | 128 |
| stroke 27 | 20 % → 20 % | 97.4 px | 0.17 | 1.00 | 87 |

Numbers say: wet paint spreads well beyond the stroke.

## Oil · Henry Ward · HW #10 green block over maroon — own sheet
own sheet 600 × 600 · Oil 1.00 · 46 px · 25.1 s

![Oil · Henry Ward · HW #10 green block over maroon — own sheet](Oil-Henry-Ward-HW-10-green-block-over-maroon-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 79 % → 21 % | 84.6 px | 0.22 | 0.26 | 1558 |
| stroke 2 | 87 % → 24 % | 144.2 px | 0.23 | 0.28 | 2370 |
| stroke 3 | 86 % → 36 % | 151.0 px | 0.42 | 0.42 | 2186 |
| stroke 4 | 88 % → 44 % | 154.5 px | 0.61 | 0.50 | 2226 |
| stroke 5 | 86 % → 49 % | 150.9 px | 0.74 | 0.57 | 2074 |
| stroke 6 | 87 % → 43 % | 154.1 px | 0.71 | 0.50 | 1922 |
| stroke 7 | 88 % → 36 % | 150.8 px | 0.60 | 0.41 | 1682 |
| stroke 8 | 91 % → 30 % | 149.7 px | 0.47 | 0.33 | 1909 |
| stroke 9 | 100 % → 27 % | 100.6 px | 0.37 | 0.27 | 1349 |
| stroke 10 | 11 % → 42 % | 39.5 px | 0.24 | 3.85 | 178 |
| stroke 11 | 14 % → 44 % | 54.3 px | 0.24 | 3.18 | 82 |
| stroke 12 | 20 % → 44 % | 75.8 px | 0.28 | 2.20 | 109 |
| stroke 13 | 27 % → 66 % | 143.2 px | 0.40 | 2.47 | 65 |
| stroke 14 | 23 % → 56 % | 89.9 px | 0.53 | 2.39 | 139 |
| stroke 15 | 36 % → 36 % | 121.4 px | 0.23 | 1.01 | 104 |
| stroke 16 | 45 % → 59 % | 209.1 px | 0.38 | 1.29 | 140 |
| stroke 17 | 34 % → 60 % | 143.6 px | 0.50 | 1.75 | 138 |
| stroke 18 | 30 % → 61 % | 113.8 px | 0.61 | 2.02 | 137 |
| stroke 19 | 29 % → 52 % | 101.1 px | 0.60 | 1.79 | 202 |
| stroke 20 | 33 % → 57 % | 114.4 px | 0.68 | 1.76 | 137 |
| stroke 21 | 37 % → 64 % | 138.0 px | 0.75 | 1.73 | 122 |
| stroke 22 | 34 % → 59 % | 132.2 px | 0.73 | 1.76 | 104 |
| stroke 23 | 38 % → 68 % | 172.0 px | 0.70 | 1.81 | 82 |
| stroke 24 | 29 % → 53 % | 103.7 px | 0.65 | 1.81 | 105 |
| stroke 25 | 38 % → 45 % | 93.4 px | 0.61 | 1.17 | 325 |
| stroke 26 | 31 % → 52 % | 131.8 px | 0.55 | 1.68 | 68 |
| stroke 27 | 37 % → 53 % | 144.0 px | 0.57 | 1.42 | 84 |
| stroke 28 | 28 % → 36 % | 87.2 px | 0.47 | 1.28 | 119 |
| stroke 29 | 37 % → 37 % | 95.4 px | 0.37 | 1.00 | 82 |

Numbers say: wet paint spreads well beyond the stroke.

## Oil · Henry Ward · HW #11 cream mass and purple balls — own sheet
own sheet 600 × 600 · Oil 1.00 · 46 px · 23.5 s

![Oil · Henry Ward · HW #11 cream mass and purple balls — own sheet](Oil-Henry-Ward-HW-11-cream-mass-and-purple-balls-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 75 % → 21 % | 77.1 px | 0.06 | 0.28 | 1799 |
| stroke 2 | 87 % → 27 % | 148.7 px | 0.05 | 0.31 | 2049 |
| stroke 3 | 85 % → 40 % | 150.6 px | 0.06 | 0.47 | 2066 |
| stroke 4 | 88 % → 43 % | 154.8 px | 0.05 | 0.49 | 2182 |
| stroke 5 | 87 % → 41 % | 150.5 px | 0.06 | 0.47 | 2136 |
| stroke 6 | 87 % → 44 % | 151.9 px | 0.32 | 0.51 | 1758 |
| stroke 7 | 87 % → 45 % | 149.9 px | 0.58 | 0.52 | 1710 |
| stroke 8 | 91 % → 36 % | 150.3 px | 0.72 | 0.40 | 1921 |
| stroke 9 | 100 % → 25 % | 103.2 px | 0.72 | 0.25 | 1432 |
| stroke 10 | 12 % → 37 % | 39.3 px | 0.05 | 3.12 | 97 |
| stroke 11 | 16 % → 46 % | 66.8 px | 0.06 | 2.77 | 80 |
| stroke 12 | 25 % → 54 % | 106.7 px | 0.06 | 2.18 | 92 |
| stroke 13 | 24 % → 54 % | 90.3 px | 0.05 | 2.25 | 138 |
| stroke 14 | 25 % → 45 % | 82.7 px | 0.05 | 1.84 | 185 |
| stroke 15 | 23 % → 45 % | 81.4 px | 0.07 | 1.97 | 164 |
| stroke 16 | 22 % → 45 % | 73.1 px | 0.08 | 2.08 | 176 |
| stroke 17 | 25 % → 63 % | 109.1 px | 0.27 | 2.49 | 93 |
| stroke 18 | 35 % → 68 % | 138.1 px | 0.34 | 1.92 | 99 |
| stroke 19 | 31 % → 34 % | 99.6 px | 0.05 | 1.10 | 125 |
| stroke 20 | 55 % → 62 % | 231.8 px | 0.06 | 1.13 | 80 |
| stroke 21 | 55 % → 59 % | 204.7 px | 0.05 | 1.08 | 92 |
| stroke 22 | 59 % → 61 % | 222.6 px | 0.05 | 1.04 | 93 |
| stroke 23 | 41 % → 51 % | 145.8 px | 0.18 | 1.24 | 116 |
| stroke 24 | 29 % → 42 % | 44.0 px | 0.56 | 1.44 | 226 |
| stroke 25 | 48 % → 61 % | 73.0 px | 0.53 | 1.27 | 239 |
| stroke 26 | 45 % → 45 % | 68.4 px | 0.52 | 1.00 | 245 |

Numbers say: wet paint spreads well beyond the stroke.

## Oil · Henry Ward · HW #13 blue scrub under red — own sheet
own sheet 600 × 600 · Oil 1.00 · 46 px · 27.1 s

![Oil · Henry Ward · HW #13 blue scrub under red — own sheet](Oil-Henry-Ward-HW-13-blue-scrub-under-red-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 80 % → 0 % | 87.5 px | 0.00 | 0.00 | 1252 |
| stroke 2 | 86 % → 0 % | 146.5 px | 0.12 | 0.00 | 1859 |
| stroke 3 | 87 % → 14 % | 151.1 px | 0.05 | 0.16 | 1744 |
| stroke 4 | 87 % → 25 % | 150.4 px | 0.06 | 0.29 | 1437 |
| stroke 5 | 87 % → 45 % | 151.2 px | 0.07 | 0.52 | 1473 |
| stroke 6 | 87 % → 44 % | 152.7 px | 0.09 | 0.51 | 1549 |
| stroke 7 | 87 % → 57 % | 153.9 px | 0.09 | 0.65 | 1351 |
| stroke 8 | 93 % → 52 % | 153.7 px | 0.10 | 0.56 | 2603 |
| stroke 9 | 100 % → 55 % | 104.1 px | 0.09 | 0.55 | 2011 |
| stroke 10 | 17 % → 0 % | 36.7 px | 0.00 | 0.00 | 184 |
| stroke 11 | 22 % → 0 % | 64.7 px | 0.00 | 0.00 | 194 |
| stroke 12 | 28 % → 3 % | 101.5 px | 0.05 | 0.12 | 181 |
| stroke 13 | 33 % → 6 % | 105.2 px | 0.05 | 0.20 | 244 |
| stroke 14 | 33 % → 23 % | 118.5 px | 0.06 | 0.71 | 207 |
| stroke 15 | 12 % → 28 % | 41.6 px | 0.06 | 2.41 | 180 |
| stroke 16 | 21 % → 46 % | 75.1 px | 0.07 | 2.19 | 180 |
| stroke 17 | 20 % → 44 % | 62.9 px | 0.08 | 2.25 | 221 |
| stroke 18 | 27 % → 48 % | 97.8 px | 0.08 | 1.79 | 180 |
| stroke 19 | 33 % → 58 % | 123.2 px | 0.09 | 1.75 | 200 |
| stroke 20 | 21 % → 55 % | 66.4 px | 0.09 | 2.64 | 356 |
| stroke 21 | 26 % → 52 % | 77.0 px | 0.10 | 1.97 | 354 |
| stroke 22 | 34 % → 52 % | 86.4 px | 0.10 | 1.53 | 406 |
| stroke 23 | 28 % → 31 % | 97.2 px | 0.06 | 1.09 | 371 |
| stroke 24 | 49 % → 51 % | 207.8 px | 0.06 | 1.06 | 180 |
| stroke 25 | 58 % → 65 % | 234.7 px | 0.07 | 1.11 | 194 |
| stroke 26 | 57 % → 64 % | 190.7 px | 0.09 | 1.11 | 291 |
| stroke 27 | 52 % → 56 % | 160.7 px | 0.09 | 1.08 | 303 |
| stroke 28 | 60 % → 60 % | 130.4 px | 0.09 | 1.00 | 297 |

Numbers say: wet paint spreads well beyond the stroke.

## Oil · Henry Ward · HW #14 olive totem on dark — own sheet
own sheet 600 × 600 · Oil 1.00 · 46 px · 40.9 s

![Oil · Henry Ward · HW #14 olive totem on dark — own sheet](Oil-Henry-Ward-HW-14-olive-totem-on-dark-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 79 % → 8 % | 80.7 px | 0.19 | 0.10 | 1178 |
| stroke 2 | 86 % → 20 % | 140.4 px | 0.22 | 0.23 | 1413 |
| stroke 3 | 87 % → 33 % | 150.3 px | 0.22 | 0.37 | 1359 |
| stroke 4 | 88 % → 38 % | 156.0 px | 0.22 | 0.44 | 1632 |
| stroke 5 | 87 % → 33 % | 151.5 px | 0.23 | 0.38 | 1526 |
| stroke 6 | 87 % → 35 % | 148.9 px | 0.21 | 0.40 | 1986 |
| stroke 7 | 88 % → 40 % | 151.4 px | 0.20 | 0.46 | 2482 |
| stroke 8 | 96 % → 32 % | 155.7 px | 0.20 | 0.33 | 2154 |
| stroke 9 | 100 % → 22 % | 101.5 px | 0.20 | 0.22 | 1606 |
| stroke 10 | 11 % → 56 % | 36.4 px | 0.22 | 5.16 | 452 |
| stroke 11 | 20 % → 54 % | 4.3 px | 0.21 | 2.77 | 4686 |
| stroke 12 | 25 % → 60 % | 18.5 px | 0.22 | 2.38 | 954 |
| stroke 13 | 30 % → 65 % | 10.4 px | 0.21 | 2.20 | 1179 |
| stroke 14 | 31 % → 63 % | 9.2 px | 0.21 | 2.01 | 1334 |
| stroke 15 | 26 % → 56 % | 2.0 px | 0.21 | 2.11 | 8755 |
| stroke 16 | 26 % → 57 % | 21.3 px | 0.20 | 2.21 | 233 |
| stroke 17 | 20 % → 29 % | 8.9 px | 0.22 | 1.42 | 173 |
| stroke 18 | 24 % → 37 % | 74.5 px | 0.22 | 1.55 | 188 |
| stroke 19 | 34 % → 49 % | 130.9 px | 0.22 | 1.44 | 136 |
| stroke 20 | 41 % → 50 % | 157.2 px | 0.22 | 1.23 | 153 |
| stroke 21 | 50 % → 55 % | 205.9 px | 0.22 | 1.09 | 136 |
| stroke 22 | 26 % → 44 % | 87.8 px | 0.21 | 1.68 | 246 |
| stroke 23 | 33 % → 44 % | 118.5 px | 0.20 | 1.32 | 240 |
| stroke 24 | 36 % → 43 % | 127.6 px | 0.20 | 1.21 | 254 |
| stroke 25 | 42 % → 46 % | 156.2 px | 0.21 | 1.10 | 139 |
| stroke 26 | 41 % → 41 % | 153.8 px | 0.22 | 1.00 | 170 |
| stroke 27 | 46 % → 50 % | 187.4 px | 0.22 | 1.08 | 120 |
| stroke 28 | 55 % → 55 % | 225.1 px | 0.21 | 1.00 | 158 |
| stroke 29 | 50 % → 50 % | 195.8 px | 0.20 | 1.00 | 158 |

Numbers say: wet paint spreads well beyond the stroke.

