![All brushes](contact.png)

# Brush Lab — 297 brushes · 8 Nov 2026 at 23:50

Every sheet: 1500 × 600, ten strokes in a 5 × 2 grid — 1. light line · 2. heavy line · 3. pressure swell · 4. fast wave · 5. slow wave · 6. spiral · 7. loop · 8. tilted · 9. over the wet one · 10. long, no reload (cell 8 holds «tilted» and «over the wet one» crossed). The CPU reference of Mamay's paint engine; the wet layer settles 20 s at the end.

Columns: **covered** = share of the cell with paint right after the stroke → after settling; **width** = painted area of the stroke ÷ its length (px); **dark** = mean darkness of the painted pixels above the paper's own grain (0 = paper, 1 = black); **spread** = how far wet paint went beyond the stroke (1.0 = stayed); **ms** = the stroke on the CPU; long stroke: paint in each quarter of its length (it should run out: wet → streaks → dry tail).

## Ink Line
Ink · 12 px · 24.7 s

![Ink Line](Ink-Line.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 1 % → 4 % | 4.3 px | 0.55 | 2.45 | 44 |
| heavy line | 5 % → 6 % | 15.7 px | 0.68 | 1.14 | 65 |
| pressure swell | 3 % → 4 % | 11.3 px | 0.64 | 1.40 | 32 |
| fast wave | 10 % → 11 % | 11.2 px | 0.59 | 1.11 | 104 |
| slow wave | 8 % → 10 % | 9.6 px | 0.57 | 1.16 | 137 |
| spiral | 14 % → 15 % | 8.9 px | 0.49 | 1.07 | 174 |
| loop | 8 % → 9 % | 10.6 px | 0.61 | 1.15 | 96 |
| tilted | 5 % → 5 % | 14.3 px | 0.64 | 1.05 | 56 |
| over the wet one | 10 % → 11 % | 12.5 px | 0.64 | 1.15 | 45 |
| long, no reload | 18 % → 17 % | 8.1 px | 0.47 | 0.96 | 360 | quarters: 0.22 → 0.09 → 0.04 → 0.02

Numbers say: light vs heavy: width 4.3 → 15.7 px, dark 0.55 → 0.68; wet paint spreads well beyond the stroke.

## Dense Ink
Ink · 14 px · 25.5 s

![Dense Ink](Dense-Ink.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 5 % → 7 % | 15.2 px | 0.72 | 1.27 | 41 |
| heavy line | 7 % → 7 % | 19.1 px | 0.73 | 1.09 | 69 |
| pressure swell | 5 % → 6 % | 17.9 px | 0.72 | 1.18 | 68 |
| fast wave | 13 % → 13 % | 15.2 px | 0.69 | 1.01 | 127 |
| slow wave | 12 % → 12 % | 13.5 px | 0.67 | 1.04 | 154 |
| spiral | 18 % → 15 % | 12.2 px | 0.65 | 0.80 | 223 |
| loop | 11 % → 12 % | 14.8 px | 0.69 | 1.08 | 114 |
| tilted | 5 % → 6 % | 14.5 px | 0.72 | 1.07 | 60 |
| over the wet one | 12 % → 13 % | 17.7 px | 0.72 | 1.12 | 56 |
| long, no reload | 23 % → 15 % | 10.1 px | 0.64 | 0.66 | 355 | quarters: 0.30 → 0.12 → 0.04 → 0.02

Numbers say: light vs heavy: width 15.2 → 19.1 px, dark 0.72 → 0.73.

## Transparent Wash
Watercolor · 22 px · 26.1 s

![Transparent Wash](Transparent-Wash.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 2 % → 5 % | 6.9 px | 0.27 | 2.26 | 27 |
| heavy line | 7 % → 9 % | 20.4 px | 0.27 | 1.23 | 60 |
| pressure swell | 4 % → 6 % | 15.2 px | 0.28 | 1.54 | 31 |
| fast wave | 14 % → 16 % | 16.1 px | 0.20 | 1.17 | 109 |
| slow wave | 12 % → 15 % | 13.7 px | 0.21 | 1.28 | 203 |
| spiral | 18 % → 22 % | 11.9 px | 0.16 | 1.22 | 165 |
| loop | 11 % → 13 % | 14.5 px | 0.22 | 1.20 | 95 |
| tilted | 8 % → 8 % | 21.1 px | 0.24 | 1.06 | 59 |
| over the wet one | 13 % → 16 % | 16.4 px | 0.24 | 1.19 | 44 |
| long, no reload | 26 % → 32 % | 11.6 px | 0.13 | 1.22 | 375 | quarters: 0.11 → 0.04 → 0.02 → 0.01

Numbers say: light vs heavy: width 6.9 → 20.4 px, dark 0.27 → 0.27; wet paint spreads well beyond the stroke.

## Dry Brush
Gouache · 24 px · 24.4 s

![Dry Brush](Dry-Brush.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 5 % → 1 % | 13.8 px | 0.65 | 0.11 | 56 |
| heavy line | 6 % → 0 % | 18.4 px | 0.65 | 0.02 | 90 |
| pressure swell | 5 % → 0 % | 18.1 px | 0.65 | 0.09 | 50 |
| fast wave | 6 % → 1 % | 6.9 px | 0.65 | 0.08 | 189 |
| slow wave | 7 % → 0 % | 7.8 px | 0.65 | 0.07 | 227 |
| spiral | 7 % → 1 % | 4.4 px | 0.65 | 0.08 | 233 |
| loop | 9 % → 0 % | 12.2 px | 0.65 | 0.05 | 126 |
| tilted | 4 % → 3 % | 10.3 px | 0.65 | 0.89 | 79 |
| over the wet one | 9 % → 1 % | 14.3 px | 0.65 | 0.12 | 71 |
| long, no reload | 6 % → 1 % | 2.7 px | 0.65 | 0.15 | 322 | quarters: 0.12 → 0.00 → 0.00 → 0.00

Numbers say: light vs heavy: width 13.8 → 18.4 px, dark 0.65 → 0.65.

## Wax Crayon
Wax · 8 px · 9.9 s

![Wax Crayon](Wax-Crayon.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 1 % → 1 % | 2.5 px | 0.71 | 1.00 | 30 |
| heavy line | 1 % → 1 % | 3.9 px | 0.69 | 1.00 | 37 |
| pressure swell | 1 % → 1 % | 3.3 px | 0.70 | 1.00 | 9 |
| fast wave | 3 % → 3 % | 3.5 px | 0.69 | 1.00 | 32 |
| slow wave | 3 % → 3 % | 3.4 px | 0.70 | 1.00 | 42 |
| spiral | 5 % → 5 % | 3.3 px | 0.70 | 1.00 | 75 |
| loop | 3 % → 3 % | 3.3 px | 0.70 | 1.00 | 33 |
| tilted | 2 % → 2 % | 5.6 px | 0.68 | 1.00 | 45 |
| over the wet one | 3 % → 3 % | 3.6 px | 0.68 | 1.00 | 21 |
| long, no reload | 7 % → 7 % | 3.3 px | 0.70 | 1.00 | 158 | quarters: 0.06 → 0.06 → 0.06 → 0.06

Numbers say: light vs heavy: width 2.5 → 3.9 px, dark 0.71 → 0.69; the long stroke does not run out of paint.

## Oil Pastel
Wax · 12 px · 9.9 s

![Oil Pastel](Oil-Pastel.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 1 % → 1 % | 4.0 px | 0.68 | 1.00 | 18 |
| heavy line | 2 % → 2 % | 6.5 px | 0.68 | 1.00 | 43 |
| pressure swell | 2 % → 2 % | 5.7 px | 0.69 | 1.00 | 16 |
| fast wave | 5 % → 5 % | 5.7 px | 0.68 | 1.00 | 50 |
| slow wave | 5 % → 5 % | 5.5 px | 0.68 | 1.00 | 48 |
| spiral | 8 % → 8 % | 5.5 px | 0.68 | 1.00 | 95 |
| loop | 4 % → 4 % | 5.6 px | 0.68 | 1.00 | 46 |
| tilted | 2 % → 2 % | 6.8 px | 0.68 | 1.00 | 38 |
| over the wet one | 5 % → 5 % | 5.8 px | 0.68 | 1.00 | 27 |
| long, no reload | 13 % → 13 % | 5.6 px | 0.68 | 1.00 | 184 | quarters: 0.10 → 0.09 → 0.10 → 0.10

Numbers say: light vs heavy: width 4.0 → 6.5 px, dark 0.68 → 0.68; the long stroke does not run out of paint.

## Charcoal
Charcoal · 5 px · 9.4 s

![Charcoal](Charcoal.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 1 % → 1 % | 2.0 px | 0.74 | 1.00 | 13 |
| heavy line | 1 % → 1 % | 3.0 px | 0.74 | 1.00 | 19 |
| pressure swell | 1 % → 1 % | 2.7 px | 0.74 | 1.00 | 5 |
| fast wave | 2 % → 2 % | 2.7 px | 0.73 | 1.00 | 24 |
| slow wave | 2 % → 2 % | 2.6 px | 0.74 | 1.00 | 29 |
| spiral | 4 % → 4 % | 2.5 px | 0.74 | 1.00 | 66 |
| loop | 2 % → 2 % | 2.6 px | 0.74 | 1.00 | 23 |
| tilted | 2 % → 2 % | 4.3 px | 0.72 | 1.00 | 21 |
| over the wet one | 2 % → 2 % | 2.4 px | 0.72 | 1.00 | 14 |
| long, no reload | 6 % → 6 % | 2.7 px | 0.73 | 1.00 | 84 | quarters: 0.05 → 0.05 → 0.05 → 0.05

Numbers say: light vs heavy: width 2.0 → 3.0 px, dark 0.74 → 0.74; the long stroke does not run out of paint.

## Impasto
Heavy acrylic · 22 px · 15.3 s

![Impasto](Impasto.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 8 % → 8 % | 24.1 px | 0.72 | 0.93 | 41 |
| heavy line | 10 % → 9 % | 28.8 px | 0.70 | 0.94 | 87 |
| pressure swell | 7 % → 7 % | 28.1 px | 0.72 | 0.94 | 50 |
| fast wave | 20 % → 13 % | 23.4 px | 0.71 | 0.64 | 160 |
| slow wave | 21 % → 14 % | 24.5 px | 0.71 | 0.66 | 279 |
| spiral | 30 % → 14 % | 19.9 px | 0.71 | 0.46 | 299 |
| loop | 18 % → 14 % | 23.9 px | 0.71 | 0.77 | 154 |
| tilted | 8 % → 8 % | 21.7 px | 0.70 | 1.00 | 78 |
| over the wet one | 17 % → 15 % | 25.4 px | 0.70 | 0.91 | 75 |
| long, no reload | 33 % → 14 % | 14.9 px | 0.71 | 0.42 | 364 | quarters: 0.38 → 0.21 → 0.10 → 0.03

Numbers say: light vs heavy: width 24.1 → 28.8 px, dark 0.72 → 0.70.

## Oil Round
Oil · 18 px · 17.7 s

![Oil Round](Oil-Round.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 2 % → 2 % | 7.2 px | 0.75 | 1.00 | 41 |
| heavy line | 7 % → 7 % | 19.3 px | 0.73 | 1.00 | 64 |
| pressure swell | 4 % → 4 % | 13.7 px | 0.72 | 1.00 | 34 |
| fast wave | 11 % → 11 % | 12.8 px | 0.65 | 1.00 | 121 |
| slow wave | 8 % → 8 % | 9.0 px | 0.57 | 1.00 | 167 |
| spiral | 10 % → 10 % | 6.6 px | 0.50 | 1.00 | 238 |
| loop | 6 % → 6 % | 7.2 px | 0.45 | 1.00 | 98 |
| tilted | 4 % → 4 % | 10.1 px | 0.52 | 1.00 | 57 |
| over the wet one | 6 % → 6 % | 7.6 px | 0.52 | 1.00 | 56 |
| long, no reload | 15 % → 15 % | 6.9 px | 0.42 | 1.00 | 324 | quarters: 0.09 → 0.08 → 0.07 → 0.06

Numbers say: light vs heavy: width 7.2 → 19.3 px, dark 0.75 → 0.73.

## Palette Knife
Oil · 20 px · 17.3 s

![Palette Knife](Palette-Knife.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 8 % → 8 % | 21.9 px | 0.67 | 1.00 | 29 |
| heavy line | 8 % → 8 % | 22.5 px | 0.74 | 1.00 | 15 |
| pressure swell | 6 % → 6 % | 22.3 px | 0.74 | 1.00 | 6 |
| fast wave | 16 % → 16 % | 18.9 px | 0.50 | 1.00 | 48 |
| slow wave | 17 % → 17 % | 19.9 px | 0.43 | 1.00 | 33 |
| spiral | 17 % → 17 % | 11.3 px | 0.46 | 1.00 | 56 |
| loop | 16 % → 16 % | 21.0 px | 0.59 | 1.00 | 22 |
| tilted | 5 % → 5 % | 15.0 px | 0.72 | 1.00 | 9 |
| over the wet one | 13 % → 13 % | 21.0 px | 0.72 | 1.00 | 14 |
| long, no reload | 16 % → 16 % | 7.2 px | 0.49 | 1.00 | 57 | quarters: 0.29 → 0.05 → 0.00 → 0.00

Numbers say: light vs heavy: width 21.9 → 22.5 px, dark 0.67 → 0.74; pressure barely changes the width.

## Water
Watercolor · 20 px · 37.9 s · over bands of wet oil paint and oil pastel in turn (it works on paint already there: look at what it does to the bands; covered counts the bands too)

![Water](Water.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 25 % → 27 % | 73.8 px | 0.80 | 1.06 | 25 |
| heavy line | 24 % → 25 % | 69.8 px | 0.81 | 1.04 | 61 |
| pressure swell | 24 % → 25 % | 89.6 px | 0.81 | 1.03 | 39 |
| fast wave | 24 % → 26 % | 27.7 px | 0.81 | 1.07 | 156 |
| slow wave | 24 % → 25 % | 27.8 px | 0.81 | 1.06 | 142 |
| spiral | 24 % → 26 % | 15.9 px | 0.81 | 1.07 | 206 |
| loop | 24 % → 25 % | 31.1 px | 0.81 | 1.03 | 89 |
| tilted | 24 % → 24 % | 67.0 px | 0.81 | 1.00 | 56 |
| over the wet one | 24 % → 25 % | 0.0 px | 0.81 | 1.06 | 37 |
| long, no reload | 24 % → 26 % | 10.7 px | 0.81 | 1.08 | 256 | quarters: 0.21 → 0.27 → 0.18 → 0.27

Numbers say: light vs heavy: width 73.8 → 69.8 px, dark 0.80 → 0.81; pressure barely changes the width; the long stroke does not run out of paint.

## Blender
Pastel · 16 px · 21.5 s · over bands of wet oil paint and oil pastel in turn (it works on paint already there: look at what it does to the bands; covered counts the bands too)

![Blender](Blender.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 24 % → 24 % | 70.7 px | 0.81 | 1.00 | 25 |
| heavy line | 25 % → 25 % | 72.1 px | 0.80 | 1.00 | 40 |
| pressure swell | 24 % → 24 % | 91.3 px | 0.81 | 1.00 | 26 |
| fast wave | 26 % → 26 % | 30.0 px | 0.79 | 1.00 | 93 |
| slow wave | 26 % → 26 % | 29.9 px | 0.80 | 1.00 | 114 |
| spiral | 28 % → 28 % | 18.7 px | 0.77 | 1.00 | 110 |
| loop | 25 % → 25 % | 33.0 px | 0.80 | 1.00 | 89 |
| tilted | 25 % → 25 % | 70.1 px | 0.79 | 1.00 | 43 |
| over the wet one | 26 % → 26 % | 1.8 px | 0.79 | 1.00 | 41 |
| long, no reload | 30 % → 30 % | 13.7 px | 0.76 | 1.00 | 299 | quarters: 0.20 → 0.28 → 0.23 → 0.30

Numbers say: light vs heavy: width 70.7 → 72.1 px, dark 0.81 → 0.80; pressure barely changes the width; the long stroke does not run out of paint.

## Eraser
Eraser · 16 px · 21.7 s · over bands of wet oil paint and oil pastel in turn (it works on paint already there: look at what it does to the bands; covered counts the bands too)

![Eraser](Eraser.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 24 % → 24 % | 69.6 px | 0.82 | 1.00 | 22 |
| heavy line | 23 % → 23 % | 67.9 px | 0.82 | 1.00 | 34 |
| pressure swell | 23 % → 23 % | 87.3 px | 0.82 | 1.00 | 21 |
| fast wave | 22 % → 22 % | 25.7 px | 0.82 | 1.00 | 105 |
| slow wave | 22 % → 22 % | 25.7 px | 0.82 | 1.00 | 120 |
| spiral | 22 % → 22 % | 14.4 px | 0.82 | 1.00 | 104 |
| loop | 22 % → 22 % | 28.6 px | 0.82 | 1.00 | 86 |
| tilted | 23 % → 23 % | 65.1 px | 0.82 | 1.00 | 40 |
| over the wet one | 23 % → 23 % | 0.0 px | 0.82 | 1.00 | 42 |
| long, no reload | 20 % → 20 % | 8.9 px | 0.82 | 1.00 | 280 | quarters: 0.15 → 0.20 → 0.15 → 0.20

Numbers say: light vs heavy: width 69.6 → 67.9 px, dark 0.82 → 0.82; pressure barely changes the width; the long stroke does not run out of paint.

## Fan
Gouache · 30 px · 31.7 s

![Fan](Fan.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 9 % → 3 % | 25.6 px | 0.63 | 0.37 | 45 |
| heavy line | 11 % → 4 % | 30.9 px | 0.63 | 0.39 | 49 |
| pressure swell | 8 % → 5 % | 31.7 px | 0.63 | 0.55 | 31 |
| fast wave | 17 % → 5 % | 20.2 px | 0.63 | 0.26 | 119 |
| slow wave | 18 % → 5 % | 21.0 px | 0.63 | 0.25 | 174 |
| spiral | 24 % → 5 % | 15.5 px | 0.63 | 0.19 | 156 |
| loop | 17 % → 5 % | 22.7 px | 0.63 | 0.28 | 93 |
| tilted | 5 % → 6 % | 15.0 px | 0.63 | 1.05 | 35 |
| over the wet one | 16 % → 8 % | 29.7 px | 0.63 | 0.49 | 39 |
| long, no reload | 22 % → 5 % | 9.9 px | 0.63 | 0.22 | 232 | quarters: 0.29 → 0.07 → 0.01 → 0.00

Numbers say: light vs heavy: width 25.6 → 30.9 px, dark 0.63 → 0.63.

## Sponge
Gouache · 30 px · 30.8 s

![Sponge](Sponge.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 4 % → 0 % | 11.3 px | 0.62 | 0.12 | 38 |
| heavy line | 12 % → 2 % | 35.4 px | 0.62 | 0.14 | 72 |
| pressure swell | 7 % → 2 % | 27.9 px | 0.62 | 0.28 | 36 |
| fast wave | 20 % → 4 % | 23.2 px | 0.62 | 0.19 | 119 |
| slow wave | 21 % → 4 % | 23.8 px | 0.62 | 0.18 | 246 |
| spiral | 28 % → 4 % | 18.3 px | 0.62 | 0.14 | 192 |
| loop | 18 % → 5 % | 23.0 px | 0.62 | 0.29 | 94 |
| tilted | 7 % → 7 % | 18.2 px | 0.62 | 1.04 | 83 |
| over the wet one | 16 % → 6 % | 27.8 px | 0.62 | 0.37 | 47 |
| long, no reload | 29 % → 5 % | 12.9 px | 0.62 | 0.17 | 292 | quarters: 0.29 → 0.13 → 0.07 → 0.04

Numbers say: light vs heavy: width 11.3 → 35.4 px, dark 0.62 → 0.62.

## Ink — sumi brush
Watercolour 1.00 · 22 px · 31.6 s

![Ink — sumi brush](Ink-sumi-brush.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 8 % → 9 % | 23.9 px | 0.87 | 1.13 | 65 |
| heavy line | 12 % → 13 % | 36.2 px | 0.86 | 1.01 | 56 |
| pressure swell | 10 % → 10 % | 36.1 px | 0.87 | 1.04 | 45 |
| fast wave | 27 % → 27 % | 31.0 px | 0.82 | 1.00 | 179 |
| slow wave | 27 % → 28 % | 31.2 px | 0.82 | 1.02 | 271 |
| spiral | 38 % → 36 % | 25.2 px | 0.75 | 0.95 | 263 |
| loop | 22 % → 23 % | 29.0 px | 0.84 | 1.01 | 137 |
| tilted | 9 % → 9 % | 25.7 px | 0.86 | 1.00 | 77 |
| over the wet one | 20 % → 20 % | 30.0 px | 0.86 | 1.02 | 68 |
| long, no reload | 46 % → 41 % | 20.7 px | 0.70 | 0.90 | 517 | quarters: 0.57 → 0.42 → 0.24 → 0.15

Numbers say: light vs heavy: width 23.9 → 36.2 px, dark 0.87 → 0.86.

## Ink — wash
Watercolour 1.00 · 40 px · 34.6 s

![Ink — wash](Ink-wash.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 13 % → 13 % | 37.3 px | 0.42 | 1.02 | 81 |
| heavy line | 19 % → 19 % | 55.2 px | 0.35 | 1.01 | 80 |
| pressure swell | 13 % → 13 % | 48.2 px | 0.41 | 1.02 | 75 |
| fast wave | 41 % → 42 % | 47.8 px | 0.32 | 1.02 | 225 |
| slow wave | 39 % → 40 % | 45.3 px | 0.42 | 1.02 | 373 |
| spiral | 60 % → 62 % | 39.7 px | 0.33 | 1.02 | 363 |
| loop | 34 % → 34 % | 43.8 px | 0.39 | 1.01 | 387 |
| tilted | 15 % → 15 % | 40.7 px | 0.43 | 1.01 | 161 |
| over the wet one | 30 % → 31 % | 43.4 px | 0.43 | 1.02 | 93 |
| long, no reload | 71 % → 75 % | 32.0 px | 0.31 | 1.05 | 829 | quarters: 0.40 → 0.29 → 0.19 → 0.12

Numbers say: light vs heavy: width 37.3 → 55.2 px, dark 0.42 → 0.35.

## Ink — dry brush
Ink 1.00 · 30 px · 27.1 s

![Ink — dry brush](Ink-dry-brush.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 5 % → 5 % | 14.9 px | 0.82 | 0.88 | 88 |
| heavy line | 7 % → 6 % | 19.4 px | 0.82 | 0.87 | 226 |
| pressure swell | 5 % → 5 % | 18.9 px | 0.81 | 0.96 | 108 |
| fast wave | 12 % → 7 % | 13.4 px | 0.80 | 0.65 | 287 |
| slow wave | 12 % → 8 % | 14.1 px | 0.81 | 0.62 | 458 |
| spiral | 16 % → 8 % | 10.8 px | 0.80 | 0.47 | 491 |
| loop | 11 % → 9 % | 14.5 px | 0.79 | 0.77 | 450 |
| tilted | 5 % → 6 % | 15.0 px | 0.81 | 1.08 | 165 |
| over the wet one | 12 % → 11 % | 18.4 px | 0.81 | 0.94 | 119 |
| long, no reload | 21 % → 10 % | 9.2 px | 0.77 | 0.47 | 971 | quarters: 0.28 → 0.10 → 0.03 → 0.01

Numbers say: light vs heavy: width 14.9 → 19.4 px, dark 0.82 → 0.82.

## Ink — nib
Watercolour 1.00 · 5 px · 25.6 s

![Ink — nib](Ink-nib.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 2 % → 5 % | 5.5 px | 0.89 | 2.46 | 30 |
| heavy line | 2 % → 5 % | 6.4 px | 0.89 | 2.34 | 26 |
| pressure swell | 2 % → 4 % | 6.2 px | 0.89 | 2.53 | 23 |
| fast wave | 5 % → 8 % | 5.9 px | 0.89 | 1.63 | 80 |
| slow wave | 5 % → 8 % | 5.7 px | 0.89 | 1.70 | 76 |
| spiral | 8 % → 11 % | 5.0 px | 0.87 | 1.41 | 139 |
| loop | 4 % → 8 % | 5.7 px | 0.89 | 1.74 | 100 |
| tilted | 4 % → 4 % | 10.3 px | 0.89 | 1.02 | 56 |
| over the wet one | 6 % → 9 % | 6.1 px | 0.89 | 1.61 | 43 |
| long, no reload | 9 % → 12 % | 4.2 px | 0.85 | 1.30 | 197 | quarters: 0.24 → 0.11 → 0.07 → 0.05

Numbers say: light vs heavy: width 5.5 → 6.4 px, dark 0.89 → 0.89; wet paint spreads well beyond the stroke.

## 0.45 · Dry brush
Gouache 0.91 · Ink 0.07 · 34 px · 33.8 s

![0.45 · Dry brush](0-45-Dry-brush.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 8 % → 2 % | 22.9 px | 0.68 | 0.26 | 103 |
| heavy line | 10 % → 5 % | 27.8 px | 0.68 | 0.52 | 175 |
| pressure swell | 7 % → 4 % | 26.5 px | 0.68 | 0.59 | 108 |
| fast wave | 19 % → 6 % | 21.4 px | 0.68 | 0.33 | 345 |
| slow wave | 20 % → 7 % | 23.0 px | 0.68 | 0.38 | 814 |
| spiral | 27 % → 8 % | 17.6 px | 0.68 | 0.29 | 624 |
| loop | 18 % → 9 % | 23.0 px | 0.68 | 0.51 | 442 |
| tilted | 8 % → 8 % | 21.8 px | 0.68 | 1.02 | 145 |
| over the wet one | 17 % → 12 % | 25.0 px | 0.68 | 0.73 | 114 |
| long, no reload | 34 % → 9 % | 15.3 px | 0.68 | 0.28 | 735 | quarters: 0.37 → 0.26 → 0.19 → 0.17

Numbers say: light vs heavy: width 22.9 → 27.8 px, dark 0.68 → 0.68.

## Dry pastel
Pastel 1.00 · 26 px · 11.9 s

![Dry pastel](Dry-pastel.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 3 % → 3 % | 8.2 px | 0.37 | 1.00 | 54 |
| heavy line | 5 % → 5 % | 13.1 px | 0.39 | 1.00 | 65 |
| pressure swell | 3 % → 3 % | 11.5 px | 0.39 | 1.00 | 22 |
| fast wave | 10 % → 10 % | 11.8 px | 0.39 | 1.00 | 141 |
| slow wave | 10 % → 10 % | 11.1 px | 0.39 | 1.00 | 189 |
| spiral | 14 % → 14 % | 9.1 px | 0.38 | 1.00 | 234 |
| loop | 7 % → 7 % | 9.5 px | 0.38 | 1.00 | 123 |
| tilted | 3 % → 3 % | 7.5 px | 0.39 | 1.00 | 72 |
| over the wet one | 6 % → 6 % | 10.6 px | 0.39 | 1.00 | 38 |
| long, no reload | 17 % → 17 % | 7.6 px | 0.38 | 1.00 | 213 | quarters: 0.08 → 0.07 → 0.07 → 0.07

Numbers say: light vs heavy: width 8.2 → 13.1 px, dark 0.37 → 0.39; the long stroke does not run out of paint.

## 0.45 · Charcoal
Charcoal 1.00 · 18 px · 11.3 s

![0.45 · Charcoal](0-45-Charcoal.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 2 % → 2 % | 5.4 px | 0.79 | 1.00 | 22 |
| heavy line | 3 % → 3 % | 8.0 px | 0.79 | 1.00 | 24 |
| pressure swell | 2 % → 2 % | 7.8 px | 0.80 | 1.00 | 19 |
| fast wave | 8 % → 8 % | 8.8 px | 0.80 | 1.00 | 65 |
| slow wave | 6 % → 6 % | 7.3 px | 0.80 | 1.00 | 80 |
| spiral | 10 % → 10 % | 6.7 px | 0.80 | 1.00 | 150 |
| loop | 6 % → 6 % | 8.2 px | 0.80 | 1.00 | 60 |
| tilted | 3 % → 3 % | 7.2 px | 0.79 | 1.00 | 34 |
| over the wet one | 5 % → 5 % | 7.4 px | 0.79 | 1.00 | 30 |
| long, no reload | 17 % → 17 % | 7.8 px | 0.80 | 1.00 | 120 | quarters: 0.15 → 0.16 → 0.16 → 0.16

Numbers say: light vs heavy: width 5.4 → 8.0 px, dark 0.79 → 0.79; the long stroke does not run out of paint.

## Watercolour — wash
Watercolour 1.00 · 50 px · 35.5 s

![Watercolour — wash](Watercolour-wash.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 16 % → 16 % | 45.5 px | 0.22 | 1.01 | 118 |
| heavy line | 22 % → 22 % | 64.9 px | 0.19 | 1.00 | 133 |
| pressure swell | 15 % → 15 % | 56.1 px | 0.22 | 1.01 | 126 |
| fast wave | 48 % → 49 % | 55.5 px | 0.19 | 1.01 | 429 |
| slow wave | 46 % → 46 % | 53.3 px | 0.24 | 1.00 | 456 |
| spiral | 66 % → 66 % | 43.7 px | 0.21 | 1.00 | 504 |
| loop | 40 % → 40 % | 51.4 px | 0.22 | 1.00 | 245 |
| tilted | 18 % → 18 % | 49.7 px | 0.23 | 1.00 | 174 |
| over the wet one | 36 % → 36 % | 49.6 px | 0.23 | 1.01 | 109 |
| long, no reload | 84 % → 84 % | 37.7 px | 0.20 | 1.00 | 672 | quarters: 0.24 → 0.20 → 0.16 → 0.12

Numbers say: light vs heavy: width 45.5 → 64.9 px, dark 0.22 → 0.19.

## Watercolour — wet-in-wet
Watercolour 1.00 · 44 px · 37.7 s

![Watercolour — wet-in-wet](Watercolour-wet-in-wet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 13 % → 21 % | 37.4 px | 0.32 | 1.63 | 105 |
| heavy line | 19 % → 22 % | 54.7 px | 0.34 | 1.17 | 136 |
| pressure swell | 12 % → 17 % | 45.7 px | 0.36 | 1.36 | 75 |
| fast wave | 42 % → 49 % | 48.5 px | 0.33 | 1.16 | 238 |
| slow wave | 40 % → 48 % | 45.7 px | 0.41 | 1.22 | 349 |
| spiral | 63 % → 69 % | 41.3 px | 0.37 | 1.11 | 385 |
| loop | 34 % → 41 % | 44.0 px | 0.37 | 1.21 | 196 |
| tilted | 16 % → 17 % | 44.6 px | 0.36 | 1.05 | 150 |
| over the wet one | 32 % → 40 % | 44.4 px | 0.36 | 1.26 | 95 |
| long, no reload | 79 % → 87 % | 35.3 px | 0.36 | 1.11 | 575 | quarters: 0.40 → 0.37 → 0.33 → 0.26

Numbers say: light vs heavy: width 37.4 → 54.7 px, dark 0.32 → 0.34; wet paint spreads well beyond the stroke.

## Watercolour — glaze
Watercolour 1.00 · 38 px · 32.1 s

![Watercolour — glaze](Watercolour-glaze.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 13 % → 13 % | 36.6 px | 0.07 | 1.02 | 70 |
| heavy line | 19 % → 19 % | 55.4 px | 0.07 | 1.00 | 93 |
| pressure swell | 13 % → 13 % | 47.0 px | 0.07 | 1.02 | 60 |
| fast wave | 39 % → 40 % | 45.6 px | 0.07 | 1.01 | 226 |
| slow wave | 37 % → 37 % | 42.8 px | 0.07 | 1.01 | 304 |
| spiral | 59 % → 60 % | 38.8 px | 0.06 | 1.01 | 348 |
| loop | 33 % → 33 % | 42.6 px | 0.07 | 1.00 | 165 |
| tilted | 14 % → 14 % | 40.1 px | 0.07 | 1.00 | 111 |
| over the wet one | 30 % → 30 % | 42.3 px | 0.07 | 1.01 | 81 |
| long, no reload | 69 % → 70 % | 30.9 px | 0.06 | 1.01 | 535 | quarters: 0.06 → 0.05 → 0.03 → 0.02

Numbers say: light vs heavy: width 36.6 → 55.4 px, dark 0.07 → 0.07.

## Watercolour — granulating
Watercolour 1.00 · 44 px · 33.6 s

![Watercolour — granulating](Watercolour-granulating.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 14 % → 14 % | 41.4 px | 0.35 | 1.01 | 76 |
| heavy line | 21 % → 21 % | 60.4 px | 0.31 | 1.00 | 101 |
| pressure swell | 14 % → 14 % | 52.2 px | 0.34 | 1.01 | 84 |
| fast wave | 45 % → 45 % | 51.7 px | 0.29 | 1.01 | 231 |
| slow wave | 42 % → 42 % | 48.2 px | 0.35 | 1.01 | 401 |
| spiral | 62 % → 63 % | 41.0 px | 0.30 | 1.01 | 391 |
| loop | 37 % → 37 % | 47.6 px | 0.33 | 1.00 | 201 |
| tilted | 16 % → 16 % | 45.5 px | 0.36 | 1.00 | 139 |
| over the wet one | 33 % → 33 % | 46.2 px | 0.36 | 1.01 | 117 |
| long, no reload | 75 % → 76 % | 33.6 px | 0.29 | 1.01 | 531 | quarters: 0.34 → 0.26 → 0.20 → 0.14

Numbers say: light vs heavy: width 41.4 → 60.4 px, dark 0.35 → 0.31.

## Watercolour — dry brush
Watercolour 1.00 · 36 px · 27.4 s

![Watercolour — dry brush](Watercolour-dry-brush.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 10 % → 9 % | 27.8 px | 0.17 | 0.99 | 105 |
| heavy line | 14 % → 12 % | 39.3 px | 0.16 | 0.92 | 108 |
| pressure swell | 11 % → 10 % | 39.6 px | 0.16 | 0.95 | 72 |
| fast wave | 27 % → 20 % | 31.3 px | 0.13 | 0.74 | 333 |
| slow wave | 25 % → 17 % | 28.9 px | 0.14 | 0.70 | 467 |
| spiral | 34 % → 19 % | 22.6 px | 0.13 | 0.56 | 395 |
| loop | 21 % → 18 % | 27.7 px | 0.14 | 0.85 | 209 |
| tilted | 10 % → 10 % | 28.5 px | 0.16 | 1.01 | 148 |
| over the wet one | 21 % → 20 % | 31.0 px | 0.16 | 0.95 | 119 |
| long, no reload | 35 % → 19 % | 15.9 px | 0.14 | 0.54 | 568 | quarters: 0.09 → 0.03 → 0.01 → 0.00

Numbers say: light vs heavy: width 27.8 → 39.3 px, dark 0.17 → 0.16.

## Gouache
Gouache 1.00 · 30 px · 30.5 s

![Gouache](Gouache.png)

A light paint: laid on a grey sheet (on white it cannot be seen); **dark** = how far it is from the grey either way.

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 8 % → 5 % | 23.3 px | 0.29 | 0.61 | 85 |
| heavy line | 12 % → 5 % | 35.6 px | 0.28 | 0.41 | 97 |
| pressure swell | 10 % → 5 % | 36.2 px | 0.28 | 0.49 | 62 |
| fast wave | 22 % → 6 % | 25.0 px | 0.28 | 0.27 | 216 |
| slow wave | 22 % → 7 % | 25.9 px | 0.28 | 0.30 | 412 |
| spiral | 28 % → 7 % | 18.5 px | 0.28 | 0.23 | 412 |
| loop | 18 % → 7 % | 23.7 px | 0.28 | 0.37 | 184 |
| tilted | 9 % → 9 % | 24.0 px | 0.28 | 1.01 | 103 |
| over the wet one | 19 % → 12 % | 28.7 px | 0.28 | 0.62 | 94 |
| long, no reload | 27 % → 8 % | 12.2 px | 0.28 | 0.31 | 611 | quarters: 0.01 → 0.02 → 0.02 → 0.02

Numbers say: light vs heavy: width 23.3 → 35.6 px, dark 0.29 → 0.28; the long stroke does not run out of paint.

## Oil — alla prima
Oil 0.89 · Oil glaze 0.11 · 30 px · 14.7 s

![Oil — alla prima](Oil-alla-prima.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 9 % → 9 % | 27.5 px | 0.49 | 1.00 | 98 |
| heavy line | 10 % → 10 % | 28.7 px | 0.50 | 1.00 | 104 |
| pressure swell | 7 % → 7 % | 27.5 px | 0.50 | 1.00 | 65 |
| fast wave | 22 % → 22 % | 25.5 px | 0.50 | 1.00 | 228 |
| slow wave | 25 % → 25 % | 29.0 px | 0.50 | 1.00 | 449 |
| spiral | 37 % → 37 % | 24.5 px | 0.49 | 1.00 | 391 |
| loop | 21 % → 21 % | 27.5 px | 0.50 | 1.00 | 264 |
| tilted | 10 % → 10 % | 26.8 px | 0.50 | 1.00 | 136 |
| over the wet one | 19 % → 19 % | 27.7 px | 0.50 | 1.00 | 103 |
| long, no reload | 46 % → 46 % | 20.5 px | 0.47 | 1.00 | 556 | quarters: 0.31 → 0.25 → 0.22 → 0.18

Numbers say: light vs heavy: width 27.5 → 28.7 px, dark 0.49 → 0.50; pressure barely changes the width.

## Oil — impasto
Oil heavy 1.00 · 34 px · 16.3 s

![Oil — impasto](Oil-impasto.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 8 % → 8 % | 24.0 px | 0.22 | 1.00 | 126 |
| heavy line | 12 % → 12 % | 35.3 px | 0.22 | 1.00 | 110 |
| pressure swell | 9 % → 9 % | 33.1 px | 0.23 | 1.00 | 83 |
| fast wave | 29 % → 29 % | 33.7 px | 0.22 | 1.00 | 309 |
| slow wave | 30 % → 30 % | 34.6 px | 0.22 | 1.00 | 485 |
| spiral | 47 % → 47 % | 31.3 px | 0.21 | 1.00 | 568 |
| loop | 25 % → 25 % | 32.5 px | 0.22 | 1.00 | 275 |
| tilted | 11 % → 11 % | 31.8 px | 0.24 | 1.00 | 125 |
| over the wet one | 21 % → 21 % | 26.8 px | 0.24 | 1.00 | 113 |
| long, no reload | 54 % → 54 % | 24.4 px | 0.20 | 1.00 | 700 | quarters: 0.16 → 0.14 → 0.11 → 0.09

Numbers say: light vs heavy: width 24.0 → 35.3 px, dark 0.22 → 0.22.

## Oil — glaze
Oil glaze 1.00 · 40 px · 16.7 s

![Oil — glaze](Oil-glaze.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 9 % → 9 % | 27.0 px | 0.50 | 1.00 | 96 |
| heavy line | 13 % → 13 % | 38.3 px | 0.49 | 1.00 | 151 |
| pressure swell | 10 % → 10 % | 36.6 px | 0.50 | 1.00 | 115 |
| fast wave | 29 % → 29 % | 33.5 px | 0.49 | 1.00 | 293 |
| slow wave | 30 % → 30 % | 34.6 px | 0.50 | 1.00 | 533 |
| spiral | 46 % → 46 % | 30.1 px | 0.49 | 1.00 | 524 |
| loop | 24 % → 24 % | 31.4 px | 0.50 | 1.00 | 514 |
| tilted | 11 % → 11 % | 30.4 px | 0.50 | 1.00 | 151 |
| over the wet one | 23 % → 23 % | 32.5 px | 0.50 | 1.00 | 144 |
| long, no reload | 52 % → 52 % | 23.5 px | 0.49 | 1.00 | 796 | quarters: 0.34 → 0.30 → 0.27 → 0.22

Numbers say: light vs heavy: width 27.0 → 38.3 px, dark 0.50 → 0.49.

## Oil — scumble
Oil 1.00 · 36 px · 15.9 s

![Oil — scumble](Oil-scumble.png)

A light paint: laid on a grey sheet (on white it cannot be seen); **dark** = how far it is from the grey either way.

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 5 % → 5 % | 13.1 px | 0.08 | 1.00 | 132 |
| heavy line | 6 % → 6 % | 17.3 px | 0.26 | 1.00 | 135 |
| pressure swell | 7 % → 7 % | 26.1 px | 0.19 | 1.00 | 117 |
| fast wave | 18 % → 18 % | 21.3 px | 0.18 | 1.00 | 376 |
| slow wave | 23 % → 23 % | 26.7 px | 0.17 | 1.00 | 694 |
| spiral | 30 % → 30 % | 20.0 px | 0.15 | 1.00 | 784 |
| loop | 18 % → 18 % | 23.0 px | 0.16 | 1.00 | 412 |
| tilted | 10 % → 10 % | 26.6 px | 0.22 | 1.00 | 208 |
| over the wet one | 16 % → 16 % | 18.6 px | 0.22 | 1.00 | 205 |
| long, no reload | 32 % → 32 % | 14.6 px | 0.13 | 1.00 | 1081 | quarters: 0.01 → 0.00 → 0.00 → 0.00

Numbers say: light vs heavy: width 13.1 → 17.3 px, dark 0.08 → 0.26.

## Acrylic — heavy body
Impasto 0.98 · 30 px · 15.0 s

![Acrylic — heavy body](Acrylic-heavy-body.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 9 % → 7 % | 25.4 px | 0.52 | 0.83 | 124 |
| heavy line | 8 % → 7 % | 24.6 px | 0.52 | 0.88 | 157 |
| pressure swell | 8 % → 7 % | 28.6 px | 0.53 | 0.89 | 83 |
| fast wave | 17 % → 13 % | 19.4 px | 0.52 | 0.78 | 276 |
| slow wave | 19 % → 15 % | 21.6 px | 0.52 | 0.79 | 396 |
| spiral | 24 % → 15 % | 15.8 px | 0.52 | 0.61 | 441 |
| loop | 17 % → 13 % | 22.2 px | 0.52 | 0.78 | 216 |
| tilted | 8 % → 8 % | 23.3 px | 0.53 | 0.99 | 129 |
| over the wet one | 18 % → 15 % | 25.6 px | 0.53 | 0.85 | 111 |
| long, no reload | 31 % → 18 % | 14.0 px | 0.52 | 0.58 | 663 | quarters: 0.26 → 0.16 → 0.11 → 0.09

Numbers say: light vs heavy: width 25.4 → 24.6 px, dark 0.52 → 0.52; pressure barely changes the width.

## Acrylic — fluid
Watercolour 1.00 · 36 px · 32.2 s

![Acrylic — fluid](Acrylic-fluid.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 12 % → 12 % | 33.6 px | 0.24 | 1.01 | 81 |
| heavy line | 18 % → 17 % | 50.9 px | 0.21 | 0.99 | 99 |
| pressure swell | 12 % → 12 % | 45.5 px | 0.23 | 1.01 | 58 |
| fast wave | 39 % → 39 % | 45.1 px | 0.19 | 0.99 | 233 |
| slow wave | 35 % → 35 % | 40.9 px | 0.22 | 1.00 | 395 |
| spiral | 55 % → 54 % | 36.4 px | 0.19 | 0.98 | 390 |
| loop | 31 % → 31 % | 40.0 px | 0.21 | 1.00 | 177 |
| tilted | 13 % → 13 % | 36.0 px | 0.24 | 1.00 | 111 |
| over the wet one | 28 % → 28 % | 42.4 px | 0.24 | 1.01 | 85 |
| long, no reload | 61 % → 58 % | 27.4 px | 0.19 | 0.95 | 494 | quarters: 0.20 → 0.14 → 0.09 → 0.06

Numbers say: light vs heavy: width 33.6 → 50.9 px, dark 0.24 → 0.21.

## Acrylic — palette knife
Impasto 1.00 · 42 px · 20.8 s

![Acrylic — palette knife](Acrylic-palette-knife.png)

A light paint: laid on a grey sheet (on white it cannot be seen); **dark** = how far it is from the grey either way.

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 15 % → 15 % | 44.0 px | 0.39 | 0.98 | 34 |
| heavy line | 15 % → 15 % | 44.3 px | 0.40 | 0.98 | 32 |
| pressure swell | 12 % → 12 % | 43.6 px | 0.42 | 0.99 | 14 |
| fast wave | 36 % → 20 % | 42.0 px | 0.37 | 0.55 | 78 |
| slow wave | 37 % → 21 % | 42.7 px | 0.37 | 0.57 | 140 |
| spiral | 47 % → 18 % | 30.7 px | 0.37 | 0.39 | 121 |
| loop | 32 % → 24 % | 41.3 px | 0.36 | 0.77 | 68 |
| tilted | 12 % → 12 % | 33.7 px | 0.39 | 1.00 | 32 |
| over the wet one | 26 % → 25 % | 39.8 px | 0.39 | 0.97 | 35 |
| long, no reload | 53 % → 20 % | 23.7 px | 0.35 | 0.39 | 145 | quarters: 0.00 → 0.00 → 0.00 → 0.01

Numbers say: light vs heavy: width 44.0 → 44.3 px, dark 0.39 → 0.40; pressure barely changes the width; the long stroke does not run out of paint.

## Finger on oil
Oil 1.00 · 30 px · 12.9 s

![Finger on oil](Finger-on-oil.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 6 % → 6 % | 16.8 px | 0.23 | 1.00 | 42 |
| heavy line | 9 % → 9 % | 27.6 px | 0.28 | 1.00 | 72 |
| pressure swell | 7 % → 7 % | 25.3 px | 0.35 | 1.00 | 49 |
| fast wave | 15 % → 15 % | 17.0 px | 0.12 | 1.00 | 157 |
| slow wave | 16 % → 16 % | 18.6 px | 0.24 | 1.00 | 244 |
| spiral | 28 % → 28 % | 18.2 px | 0.24 | 1.00 | 217 |
| loop | 19 % → 19 % | 24.9 px | 0.28 | 1.00 | 134 |
| tilted | 9 % → 9 % | 26.4 px | 0.28 | 1.00 | 85 |
| over the wet one | 16 % → 16 % | 19.6 px | 0.28 | 1.00 | 73 |
| long, no reload | 36 % → 36 % | 15.9 px | 0.22 | 1.00 | 328 | quarters: 0.12 → 0.11 → 0.07 → 0.04

Numbers say: light vs heavy: width 16.8 → 27.6 px, dark 0.23 → 0.28.

## Palette knife — oil
Oil heavy 0.93 · Impasto 0.07 · 44 px · 18.9 s

![Palette knife — oil](Palette-knife-oil.png)

A light paint: laid on a grey sheet (on white it cannot be seen); **dark** = how far it is from the grey either way.

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 16 % → 14 % | 45.7 px | 0.37 | 0.91 | 35 |
| heavy line | 16 % → 16 % | 46.3 px | 0.38 | 0.98 | 33 |
| pressure swell | 12 % → 12 % | 45.2 px | 0.38 | 0.99 | 10 |
| fast wave | 39 % → 35 % | 44.9 px | 0.35 | 0.89 | 89 |
| slow wave | 39 % → 36 % | 45.4 px | 0.35 | 0.92 | 128 |
| spiral | 62 % → 37 % | 40.7 px | 0.35 | 0.60 | 134 |
| loop | 34 % → 31 % | 43.8 px | 0.36 | 0.92 | 81 |
| tilted | 13 % → 13 % | 36.6 px | 0.37 | 1.00 | 32 |
| over the wet one | 28 % → 27 % | 40.8 px | 0.37 | 0.97 | 36 |
| long, no reload | 74 % → 40 % | 33.0 px | 0.34 | 0.54 | 182 | quarters: 0.00 → 0.00 → 0.01 → 0.01

Numbers say: light vs heavy: width 45.7 → 46.3 px, dark 0.37 → 0.38; pressure barely changes the width; the long stroke does not run out of paint.

## 0.45 · Sponge
Watercolour 0.93 · Ink 0.07 · 46 px · 35.1 s

![0.45 · Sponge](0-45-Sponge.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 27 % → 24 % | 77.5 px | 0.13 | 0.91 | 61 |
| heavy line | 32 % → 28 % | 92.0 px | 0.13 | 0.89 | 88 |
| pressure swell | 24 % → 22 % | 90.9 px | 0.13 | 0.91 | 66 |
| fast wave | 60 % → 54 % | 69.8 px | 0.12 | 0.90 | 194 |
| slow wave | 63 % → 59 % | 72.4 px | 0.17 | 0.94 | 441 |
| spiral | 77 % → 74 % | 51.0 px | 0.16 | 0.96 | 367 |
| loop | 54 % → 51 % | 70.4 px | 0.15 | 0.94 | 147 |
| tilted | 17 % → 17 % | 47.9 px | 0.17 | 1.01 | 120 |
| over the wet one | 45 % → 42 % | 76.8 px | 0.17 | 0.93 | 71 |
| long, no reload | 94 % → 90 % | 42.3 px | 0.17 | 0.96 | 500 | quarters: 0.18 → 0.18 → 0.17 → 0.14

Numbers say: light vs heavy: width 77.5 → 92.0 px, dark 0.13 → 0.13.

## 0.45 · Eraser
Watercolour 1.00 · 30 px · 22.0 s · over bands of wet oil paint and oil pastel in turn (it works on paint already there: look at what it does to the bands; covered counts the bands too)

![0.45 · Eraser](0-45-Eraser.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 24 % → 24 % | 69.2 px | 0.82 | 1.00 | 42 |
| heavy line | 23 % → 23 % | 67.4 px | 0.82 | 1.00 | 52 |
| pressure swell | 23 % → 23 % | 86.8 px | 0.82 | 1.00 | 39 |
| fast wave | 21 % → 21 % | 24.7 px | 0.81 | 1.00 | 123 |
| slow wave | 20 % → 20 % | 23.5 px | 0.82 | 1.00 | 193 |
| spiral | 20 % → 20 % | 13.5 px | 0.79 | 1.00 | 190 |
| loop | 21 % → 21 % | 27.8 px | 0.80 | 1.00 | 103 |
| tilted | 23 % → 23 % | 64.8 px | 0.81 | 1.00 | 66 |
| over the wet one | 22 % → 22 % | 0.0 px | 0.81 | 1.00 | 53 |
| long, no reload | 17 % → 17 % | 7.5 px | 0.79 | 1.00 | 299 | quarters: 0.13 → 0.16 → 0.13 → 0.17

Numbers say: light vs heavy: width 69.2 → 67.4 px, dark 0.82 → 0.82; pressure barely changes the width; the long stroke does not run out of paint.

## Lift wet paint
Watercolour 1.00 · 30 px · 21.5 s · over bands of wet oil paint and oil pastel in turn (it works on paint already there: look at what it does to the bands; covered counts the bands too)

![Lift wet paint](Lift-wet-paint.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 24 % → 24 % | 70.1 px | 0.82 | 1.00 | 35 |
| heavy line | 24 % → 24 % | 69.8 px | 0.82 | 1.00 | 45 |
| pressure swell | 24 % → 24 % | 89.6 px | 0.82 | 1.00 | 24 |
| fast wave | 24 % → 24 % | 27.7 px | 0.82 | 1.00 | 91 |
| slow wave | 24 % → 24 % | 27.7 px | 0.82 | 1.00 | 160 |
| spiral | 24 % → 24 % | 15.9 px | 0.82 | 1.00 | 150 |
| loop | 24 % → 24 % | 31.1 px | 0.82 | 1.00 | 89 |
| tilted | 24 % → 24 % | 66.8 px | 0.82 | 1.00 | 50 |
| over the wet one | 24 % → 24 % | 0.0 px | 0.82 | 1.00 | 55 |
| long, no reload | 24 % → 24 % | 10.7 px | 0.82 | 1.00 | 232 | quarters: 0.18 → 0.24 → 0.17 → 0.24

Numbers say: light vs heavy: width 70.1 → 69.8 px, dark 0.82 → 0.82; pressure barely changes the width; the long stroke does not run out of paint.

## Sgraffito
Watercolour 1.00 · 10 px · 21.9 s · over bands of wet oil paint and oil pastel in turn (it works on paint already there: look at what it does to the bands; covered counts the bands too)

![Sgraffito](Sgraffito.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 24 % → 24 % | 69.9 px | 0.81 | 1.00 | 9 |
| heavy line | 24 % → 24 % | 69.8 px | 0.82 | 1.00 | 6 |
| pressure swell | 24 % → 24 % | 89.6 px | 0.82 | 1.00 | 6 |
| fast wave | 24 % → 24 % | 27.7 px | 0.82 | 1.00 | 21 |
| slow wave | 24 % → 24 % | 27.7 px | 0.82 | 1.00 | 22 |
| spiral | 24 % → 24 % | 15.9 px | 0.82 | 1.00 | 42 |
| loop | 24 % → 24 % | 31.1 px | 0.82 | 1.00 | 30 |
| tilted | 24 % → 24 % | 66.9 px | 0.82 | 1.00 | 7 |
| over the wet one | 24 % → 24 % | 0.0 px | 0.82 | 1.00 | 6 |
| long, no reload | 24 % → 24 % | 10.6 px | 0.82 | 1.00 | 85 | quarters: 0.17 → 0.24 → 0.17 → 0.24

Numbers say: light vs heavy: width 69.9 → 69.8 px, dark 0.81 → 0.82; pressure barely changes the width; the long stroke does not run out of paint.

## Brush Artist · Refs · #01 Henry Ward peach cloud
Gouache 1.00 · 44 px · 28.6 s

![Brush Artist · Refs · #01 Henry Ward peach cloud](Brush-Artist-Refs-01-Henry-Ward-peach-cloud.png)

A light paint: laid on a grey sheet (on white it cannot be seen); **dark** = how far it is from the grey either way.

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 5 % → 0 % | 13.4 px | 0.00 | 0.00 | 160 |
| heavy line | 8 % → 0 % | 22.4 px | 0.32 | 0.01 | 154 |
| pressure swell | 7 % → 3 % | 24.8 px | 0.33 | 0.40 | 102 |
| fast wave | 31 % → 3 % | 36.2 px | 0.27 | 0.09 | 396 |
| slow wave | 20 % → 2 % | 23.3 px | 0.32 | 0.10 | 591 |
| spiral | 33 % → 2 % | 21.6 px | 0.35 | 0.07 | 617 |
| loop | 17 % → 0 % | 22.4 px | 0.32 | 0.01 | 318 |
| tilted | 12 % → 11 % | 32.7 px | 0.25 | 0.97 | 233 |
| over the wet one | 16 % → 2 % | 12.9 px | 0.25 | 0.10 | 273 |
| long, no reload | 30 % → 2 % | 13.6 px | 0.32 | 0.08 | 942 | quarters: 0.03 → 0.03 → 0.03 → 0.03

Numbers say: light vs heavy: width 13.4 → 22.4 px, dark 0.00 → 0.32; the long stroke does not run out of paint.

## Brush Artist · Refs · #02 Henry Ward cream strokes
Gouache 1.00 · 46 px · 31.5 s

![Brush Artist · Refs · #02 Henry Ward cream strokes](Brush-Artist-Refs-02-Henry-Ward-cream-strokes.png)

A light paint: laid on a grey sheet (on white it cannot be seen); **dark** = how far it is from the grey either way.

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 5 % → 0 % | 14.3 px | 0.00 | 0.00 | 132 |
| heavy line | 8 % → 2 % | 24.6 px | 0.41 | 0.22 | 154 |
| pressure swell | 7 % → 3 % | 27.7 px | 0.41 | 0.38 | 96 |
| fast wave | 30 % → 4 % | 34.5 px | 0.36 | 0.15 | 432 |
| slow wave | 21 % → 5 % | 24.3 px | 0.39 | 0.21 | 617 |
| spiral | 43 % → 4 % | 28.4 px | 0.40 | 0.10 | 699 |
| loop | 19 % → 1 % | 24.8 px | 0.39 | 0.04 | 385 |
| tilted | 12 % → 12 % | 33.1 px | 0.34 | 0.98 | 215 |
| over the wet one | 17 % → 1 % | 13.0 px | 0.34 | 0.05 | 172 |
| long, no reload | 25 % → 4 % | 11.1 px | 0.41 | 0.17 | 874 | quarters: 0.03 → 0.04 → 0.03 → 0.04

Numbers say: light vs heavy: width 14.3 → 24.6 px, dark 0.00 → 0.41; the long stroke does not run out of paint.

## Brush Artist · Refs · #03 Henry Ward navy contours
Impasto 1.00 · 22 px · 16.1 s

![Brush Artist · Refs · #03 Henry Ward navy contours](Brush-Artist-Refs-03-Henry-Ward-navy-contours.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 7 % → 6 % | 19.4 px | 0.72 | 0.90 | 150 |
| heavy line | 6 % → 6 % | 18.3 px | 0.71 | 0.92 | 85 |
| pressure swell | 5 % → 5 % | 20.1 px | 0.75 | 0.89 | 63 |
| fast wave | 16 % → 11 % | 18.3 px | 0.76 | 0.71 | 215 |
| slow wave | 18 % → 14 % | 20.5 px | 0.72 | 0.78 | 444 |
| spiral | 28 % → 13 % | 18.3 px | 0.68 | 0.47 | 479 |
| loop | 13 % → 11 % | 17.0 px | 0.71 | 0.83 | 186 |
| tilted | 7 % → 7 % | 20.7 px | 0.73 | 0.99 | 113 |
| over the wet one | 15 % → 13 % | 20.4 px | 0.73 | 0.88 | 107 |
| long, no reload | 32 % → 13 % | 14.4 px | 0.71 | 0.41 | 697 | quarters: 0.33 → 0.27 → 0.19 → 0.08

Numbers say: light vs heavy: width 19.4 → 18.3 px, dark 0.72 → 0.71; pressure barely changes the width.

## Brush Artist · Refs · #04 Henry Ward grey cloud
Gouache 1.00 · 50 px · 31.7 s

![Brush Artist · Refs · #04 Henry Ward grey cloud](Brush-Artist-Refs-04-Henry-Ward-grey-cloud.png)

A light paint: laid on a grey sheet (on white it cannot be seen); **dark** = how far it is from the grey either way.

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 5 % → 0 % | 14.6 px | 0.00 | 0.00 | 199 |
| heavy line | 10 % → 2 % | 28.3 px | 0.31 | 0.25 | 228 |
| pressure swell | 7 % → 2 % | 24.5 px | 0.31 | 0.36 | 96 |
| fast wave | 32 % → 4 % | 37.5 px | 0.24 | 0.14 | 493 |
| slow wave | 23 % → 2 % | 26.3 px | 0.33 | 0.10 | 670 |
| spiral | 47 % → 3 % | 30.8 px | 0.37 | 0.06 | 764 |
| loop | 19 % → 0 % | 25.2 px | 0.00 | 0.00 | 409 |
| tilted | 12 % → 12 % | 33.3 px | 0.24 | 0.98 | 257 |
| over the wet one | 17 % → 3 % | 14.1 px | 0.24 | 0.17 | 139 |
| long, no reload | 22 % → 4 % | 9.9 px | 0.34 | 0.17 | 871 | quarters: 0.03 → 0.04 → 0.04 → 0.04

Numbers say: light vs heavy: width 14.6 → 28.3 px, dark 0.00 → 0.31; the long stroke does not run out of paint.

## Brush Artist · Refs · #05 Henry Ward green in rust loops
Impasto 1.00 · 20 px · 13.8 s

![Brush Artist · Refs · #05 Henry Ward green in rust loops](Brush-Artist-Refs-05-Henry-Ward-green-in-rust-loops.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 6 % → 6 % | 18.5 px | 0.56 | 0.88 | 101 |
| heavy line | 8 % → 7 % | 22.1 px | 0.56 | 0.87 | 95 |
| pressure swell | 4 % → 4 % | 16.1 px | 0.58 | 0.93 | 63 |
| fast wave | 16 % → 10 % | 17.9 px | 0.56 | 0.67 | 232 |
| slow wave | 16 % → 12 % | 19.1 px | 0.56 | 0.74 | 251 |
| spiral | 24 % → 11 % | 16.1 px | 0.53 | 0.46 | 323 |
| loop | 15 % → 12 % | 19.7 px | 0.56 | 0.79 | 174 |
| tilted | 7 % → 7 % | 19.8 px | 0.58 | 0.99 | 84 |
| over the wet one | 14 % → 12 % | 18.1 px | 0.58 | 0.85 | 84 |
| long, no reload | 28 % → 12 % | 12.6 px | 0.55 | 0.41 | 555 | quarters: 0.23 → 0.17 → 0.11 → 0.04

Numbers say: light vs heavy: width 18.5 → 22.1 px, dark 0.56 → 0.56.

## Brush Artist · Refs · #06 Henry Ward scrubbed grey
Gouache 1.00 · 50 px · 31.6 s

![Brush Artist · Refs · #06 Henry Ward scrubbed grey](Brush-Artist-Refs-06-Henry-Ward-scrubbed-grey.png)

A light paint: laid on a grey sheet (on white it cannot be seen); **dark** = how far it is from the grey either way.

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 5 % → 0 % | 14.6 px | 0.00 | 0.00 | 133 |
| heavy line | 10 % → 2 % | 28.3 px | 0.33 | 0.25 | 226 |
| pressure swell | 7 % → 2 % | 24.5 px | 0.33 | 0.36 | 112 |
| fast wave | 32 % → 4 % | 37.5 px | 0.25 | 0.14 | 524 |
| slow wave | 23 % → 2 % | 26.3 px | 0.34 | 0.10 | 639 |
| spiral | 47 % → 3 % | 30.8 px | 0.38 | 0.06 | 672 |
| loop | 19 % → 0 % | 25.2 px | 0.00 | 0.00 | 327 |
| tilted | 12 % → 12 % | 33.3 px | 0.25 | 0.98 | 277 |
| over the wet one | 17 % → 3 % | 14.1 px | 0.25 | 0.17 | 151 |
| long, no reload | 22 % → 4 % | 9.9 px | 0.36 | 0.17 | 819 | quarters: 0.03 → 0.04 → 0.04 → 0.04

Numbers say: light vs heavy: width 14.6 → 28.3 px, dark 0.00 → 0.33; the long stroke does not run out of paint.

## Brush Artist · Refs · #07 Henry Ward blue L + black zigzag
Impasto 1.00 · 34 px · 17.3 s

![Brush Artist · Refs · #07 Henry Ward blue L + black zigzag](Brush-Artist-Refs-07-Henry-Ward-blue-L-black-zigzag.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 10 % → 9 % | 30.2 px | 0.59 | 0.86 | 101 |
| heavy line | 11 % → 10 % | 30.8 px | 0.59 | 0.93 | 144 |
| pressure swell | 8 % → 8 % | 31.6 px | 0.59 | 0.92 | 141 |
| fast wave | 25 % → 19 % | 28.8 px | 0.60 | 0.77 | 316 |
| slow wave | 26 % → 20 % | 29.7 px | 0.57 | 0.76 | 478 |
| spiral | 44 % → 23 % | 29.1 px | 0.54 | 0.52 | 474 |
| loop | 24 % → 19 % | 30.4 px | 0.57 | 0.80 | 285 |
| tilted | 11 % → 11 % | 29.8 px | 0.61 | 1.00 | 121 |
| over the wet one | 22 % → 20 % | 32.0 px | 0.61 | 0.90 | 114 |
| long, no reload | 50 % → 23 % | 22.5 px | 0.57 | 0.46 | 686 | quarters: 0.36 → 0.31 → 0.21 → 0.10

Numbers say: light vs heavy: width 30.2 → 30.8 px, dark 0.59 → 0.59; pressure barely changes the width.

## Brush Artist · Refs · #08 Henry Ward olive bands
Gouache 1.00 · 34 px · 24.2 s

![Brush Artist · Refs · #08 Henry Ward olive bands](Brush-Artist-Refs-08-Henry-Ward-olive-bands.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 2 % → 0 % | 5.8 px | 0.00 | 0.00 | 54 |
| heavy line | 7 % → 1 % | 19.2 px | 0.61 | 0.15 | 171 |
| pressure swell | 5 % → 1 % | 19.1 px | 0.61 | 0.20 | 77 |
| fast wave | 18 % → 1 % | 21.1 px | 0.59 | 0.04 | 288 |
| slow wave | 16 % → 0 % | 18.3 px | 0.63 | 0.02 | 498 |
| spiral | 27 % → 0 % | 17.5 px | 0.52 | 0.01 | 407 |
| loop | 10 % → 1 % | 13.5 px | 0.61 | 0.12 | 216 |
| tilted | 7 % → 7 % | 20.5 px | 0.65 | 0.92 | 161 |
| over the wet one | 11 % → 1 % | 9.8 px | 0.65 | 0.12 | 125 |
| long, no reload | 23 % → 2 % | 10.4 px | 0.53 | 0.10 | 581 | quarters: 0.21 → 0.11 → 0.12 → 0.08

Numbers say: light vs heavy: width 5.8 → 19.2 px, dark 0.00 → 0.61.

## Brush Artist · Refs · #09 Henry Ward white loops
Gouache 1.00 · 46 px · 32.6 s

![Brush Artist · Refs · #09 Henry Ward white loops](Brush-Artist-Refs-09-Henry-Ward-white-loops.png)

A light paint: laid on a grey sheet (on white it cannot be seen); **dark** = how far it is from the grey either way.

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 5 % → 0 % | 14.3 px | 0.00 | 0.00 | 130 |
| heavy line | 8 % → 2 % | 24.6 px | 0.43 | 0.22 | 134 |
| pressure swell | 7 % → 3 % | 27.7 px | 0.43 | 0.38 | 99 |
| fast wave | 30 % → 4 % | 34.5 px | 0.38 | 0.15 | 399 |
| slow wave | 21 % → 5 % | 24.3 px | 0.40 | 0.21 | 606 |
| spiral | 43 % → 4 % | 28.4 px | 0.41 | 0.10 | 802 |
| loop | 19 % → 1 % | 24.8 px | 0.41 | 0.04 | 327 |
| tilted | 12 % → 12 % | 33.1 px | 0.37 | 0.98 | 229 |
| over the wet one | 17 % → 1 % | 13.0 px | 0.37 | 0.05 | 174 |
| long, no reload | 25 % → 4 % | 11.1 px | 0.41 | 0.17 | 941 | quarters: 0.03 → 0.04 → 0.04 → 0.04

Numbers say: light vs heavy: width 14.3 → 24.6 px, dark 0.00 → 0.43; the long stroke does not run out of paint.

## Brush Artist · Refs · #10 Henry Ward maroon loops
Impasto 1.00 · 30 px · 16.5 s

![Brush Artist · Refs · #10 Henry Ward maroon loops](Brush-Artist-Refs-10-Henry-Ward-maroon-loops.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 10 % → 8 % | 27.9 px | 0.73 | 0.88 | 114 |
| heavy line | 11 % → 10 % | 32.1 px | 0.73 | 0.90 | 109 |
| pressure swell | 8 % → 7 % | 29.7 px | 0.74 | 0.91 | 75 |
| fast wave | 23 % → 17 % | 26.5 px | 0.76 | 0.76 | 225 |
| slow wave | 22 % → 19 % | 25.9 px | 0.72 | 0.85 | 422 |
| spiral | 37 % → 18 % | 24.2 px | 0.72 | 0.50 | 392 |
| loop | 17 % → 15 % | 22.1 px | 0.73 | 0.86 | 265 |
| tilted | 10 % → 10 % | 27.6 px | 0.73 | 1.00 | 124 |
| over the wet one | 19 % → 17 % | 26.8 px | 0.73 | 0.86 | 100 |
| long, no reload | 40 % → 17 % | 18.0 px | 0.71 | 0.43 | 600 | quarters: 0.38 → 0.33 → 0.27 → 0.18

Numbers say: light vs heavy: width 27.9 → 32.1 px, dark 0.73 → 0.73.

## Brush Artist · Refs · #11 Henry Ward purple spun balls
Impasto 1.00 · 36 px · 18.7 s

![Brush Artist · Refs · #11 Henry Ward purple spun balls](Brush-Artist-Refs-11-Henry-Ward-purple-spun-balls.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 11 % → 10 % | 31.5 px | 0.74 | 0.93 | 90 |
| heavy line | 11 % → 10 % | 30.5 px | 0.74 | 0.95 | 96 |
| pressure swell | 10 % → 9 % | 36.4 px | 0.75 | 0.92 | 82 |
| fast wave | 27 % → 21 % | 31.1 px | 0.74 | 0.78 | 324 |
| slow wave | 30 % → 24 % | 34.6 px | 0.73 | 0.82 | 547 |
| spiral | 40 % → 24 % | 26.5 px | 0.70 | 0.59 | 662 |
| loop | 24 % → 21 % | 30.7 px | 0.75 | 0.90 | 267 |
| tilted | 10 % → 10 % | 28.5 px | 0.73 | 1.00 | 155 |
| over the wet one | 22 % → 20 % | 33.9 px | 0.73 | 0.91 | 138 |
| long, no reload | 53 % → 25 % | 23.9 px | 0.74 | 0.46 | 888 | quarters: 0.50 → 0.45 → 0.38 → 0.27

Numbers say: light vs heavy: width 31.5 → 30.5 px, dark 0.74 → 0.74; pressure barely changes the width.

## Brush Artist · Refs · #12 Henry Ward black-olive cage
Gouache 1.00 · 28 px · 24.9 s

![Brush Artist · Refs · #12 Henry Ward black-olive cage](Brush-Artist-Refs-12-Henry-Ward-black-olive-cage.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 2 % → 0 % | 6.3 px | 0.00 | 0.00 | 48 |
| heavy line | 6 % → 1 % | 16.9 px | 0.64 | 0.21 | 124 |
| pressure swell | 5 % → 1 % | 17.2 px | 0.64 | 0.22 | 73 |
| fast wave | 14 % → 0 % | 16.6 px | 0.00 | 0.00 | 343 |
| slow wave | 14 % → 1 % | 15.6 px | 0.64 | 0.07 | 429 |
| spiral | 18 % → 0 % | 11.7 px | 0.63 | 0.02 | 482 |
| loop | 11 % → 1 % | 14.3 px | 0.63 | 0.10 | 423 |
| tilted | 6 % → 6 % | 17.8 px | 0.68 | 0.92 | 131 |
| over the wet one | 10 % → 0 % | 9.7 px | 0.68 | 0.04 | 91 |
| long, no reload | 18 % → 2 % | 8.0 px | 0.59 | 0.12 | 824 | quarters: 0.15 → 0.12 → 0.06 → 0.02

Numbers say: light vs heavy: width 6.3 → 16.9 px, dark 0.00 → 0.64.

## Brush Artist · Refs · #13 Henry Ward blue streaky form
Gouache 1.00 · 50 px · 33.4 s

![Brush Artist · Refs · #13 Henry Ward blue streaky form](Brush-Artist-Refs-13-Henry-Ward-blue-streaky-form.png)

A light paint: laid on a grey sheet (on white it cannot be seen); **dark** = how far it is from the grey either way.

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 5 % → 0 % | 14.6 px | 0.00 | 0.00 | 161 |
| heavy line | 10 % → 2 % | 28.3 px | 0.33 | 0.25 | 162 |
| pressure swell | 7 % → 2 % | 24.5 px | 0.33 | 0.36 | 121 |
| fast wave | 32 % → 4 % | 37.5 px | 0.25 | 0.14 | 470 |
| slow wave | 23 % → 2 % | 26.3 px | 0.34 | 0.10 | 740 |
| spiral | 47 % → 3 % | 30.8 px | 0.38 | 0.06 | 1249 |
| loop | 19 % → 0 % | 25.2 px | 0.00 | 0.00 | 320 |
| tilted | 12 % → 12 % | 33.3 px | 0.25 | 0.98 | 284 |
| over the wet one | 17 % → 3 % | 14.1 px | 0.25 | 0.17 | 251 |
| long, no reload | 22 % → 4 % | 9.9 px | 0.35 | 0.17 | 1103 | quarters: 0.03 → 0.04 → 0.04 → 0.04

Numbers say: light vs heavy: width 14.6 → 28.3 px, dark 0.00 → 0.33; the long stroke does not run out of paint.

## Brush Artist · Refs · #14 Henry Ward olive totem
Impasto 1.00 · 48 px · 21.6 s

![Brush Artist · Refs · #14 Henry Ward olive totem](Brush-Artist-Refs-14-Henry-Ward-olive-totem.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 15 % → 14 % | 44.4 px | 0.31 | 0.91 | 170 |
| heavy line | 16 % → 15 % | 46.3 px | 0.31 | 0.95 | 169 |
| pressure swell | 12 % → 11 % | 44.0 px | 0.31 | 0.93 | 125 |
| fast wave | 36 % → 28 % | 41.7 px | 0.36 | 0.78 | 465 |
| slow wave | 37 % → 32 % | 42.3 px | 0.30 | 0.87 | 1010 |
| spiral | 59 % → 35 % | 38.7 px | 0.28 | 0.59 | 801 |
| loop | 30 % → 27 % | 39.1 px | 0.29 | 0.89 | 594 |
| tilted | 13 % → 13 % | 36.4 px | 0.33 | 1.00 | 214 |
| over the wet one | 28 % → 25 % | 40.5 px | 0.33 | 0.92 | 165 |
| long, no reload | 61 % → 31 % | 27.3 px | 0.27 | 0.52 | 1067 | quarters: 0.20 → 0.15 → 0.09 → 0.04

Numbers say: light vs heavy: width 44.4 → 46.3 px, dark 0.31 → 0.31; pressure barely changes the width.

## Brush Artist · Refs · #15 Ultramarine brush script
Ink 1.00 · 4 px · 24.7 s

![Brush Artist · Refs · #15 Ultramarine brush script](Brush-Artist-Refs-15-Ultramarine-brush-script.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 1 % → 3 % | 2.1 px | 0.55 | 3.99 | 40 |
| heavy line | 5 % → 5 % | 15.6 px | 0.62 | 1.00 | 124 |
| pressure swell | 3 % → 4 % | 11.0 px | 0.62 | 1.21 | 31 |
| fast wave | 9 % → 7 % | 10.2 px | 0.54 | 0.81 | 77 |
| slow wave | 8 % → 7 % | 8.8 px | 0.53 | 0.89 | 96 |
| spiral | 11 % → 8 % | 7.3 px | 0.53 | 0.68 | 276 |
| loop | 7 % → 7 % | 9.4 px | 0.54 | 0.96 | 139 |
| tilted | 3 % → 3 % | 7.4 px | 0.64 | 1.04 | 39 |
| over the wet one | 7 % → 7 % | 10.7 px | 0.64 | 1.08 | 40 |
| long, no reload | 16 % → 7 % | 7.1 px | 0.51 | 0.47 | 204 | quarters: 0.14 → 0.04 → 0.01 → 0.00

Numbers say: light vs heavy: width 2.1 → 15.6 px, dark 0.55 → 0.62; wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #18 Blue oil-stick scribbles
Pastel 1.00 · 10 px · 10.8 s

![Brush Artist · Refs · #18 Blue oil-stick scribbles](Brush-Artist-Refs-18-Blue-oil-stick-scribbles.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 1 % → 1 % | 2.9 px | 0.53 | 1.00 | 16 |
| heavy line | 2 % → 2 % | 6.0 px | 0.53 | 1.00 | 28 |
| pressure swell | 1 % → 1 % | 5.5 px | 0.52 | 1.00 | 16 |
| fast wave | 5 % → 5 % | 5.3 px | 0.53 | 1.00 | 136 |
| slow wave | 4 % → 4 % | 5.2 px | 0.53 | 1.00 | 79 |
| spiral | 7 % → 7 % | 4.4 px | 0.52 | 1.00 | 126 |
| loop | 4 % → 4 % | 4.6 px | 0.52 | 1.00 | 93 |
| tilted | 2 % → 2 % | 4.4 px | 0.53 | 1.00 | 69 |
| over the wet one | 3 % → 3 % | 4.8 px | 0.53 | 1.00 | 49 |
| long, no reload | 9 % → 9 % | 4.2 px | 0.52 | 1.00 | 176 | quarters: 0.05 → 0.05 → 0.06 → 0.06

Numbers say: light vs heavy: width 2.9 → 6.0 px, dark 0.53 → 0.53; the long stroke does not run out of paint.

## Brush Artist · Refs · #20 Orange-red crayon scribble
Pastel 1.00 · 14 px · 10.5 s

![Brush Artist · Refs · #20 Orange-red crayon scribble](Brush-Artist-Refs-20-Orange-red-crayon-scribble.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 1 % → 1 % | 3.8 px | 0.53 | 1.00 | 19 |
| heavy line | 3 % → 3 % | 8.0 px | 0.53 | 1.00 | 24 |
| pressure swell | 2 % → 2 % | 7.6 px | 0.55 | 1.00 | 20 |
| fast wave | 6 % → 6 % | 7.3 px | 0.56 | 1.00 | 64 |
| slow wave | 6 % → 6 % | 6.9 px | 0.53 | 1.00 | 62 |
| spiral | 9 % → 9 % | 6.0 px | 0.54 | 1.00 | 136 |
| loop | 5 % → 5 % | 6.1 px | 0.54 | 1.00 | 53 |
| tilted | 2 % → 2 % | 5.6 px | 0.55 | 1.00 | 28 |
| over the wet one | 4 % → 4 % | 6.2 px | 0.55 | 1.00 | 24 |
| long, no reload | 12 % → 12 % | 5.4 px | 0.53 | 1.00 | 160 | quarters: 0.07 → 0.07 → 0.07 → 0.07

Numbers say: light vs heavy: width 3.8 → 8.0 px, dark 0.53 → 0.53; the long stroke does not run out of paint.

## Brush Artist · Refs · #21 Gritty black contours
Gouache 1.00 · 12 px · 20.9 s

![Brush Artist · Refs · #21 Gritty black contours](Brush-Artist-Refs-21-Gritty-black-contours.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 1 % → 0 % | 3.2 px | 0.00 | 0.00 | 47 |
| heavy line | 2 % → 0 % | 6.0 px | 0.00 | 0.00 | 140 |
| pressure swell | 1 % → 0 % | 5.6 px | 0.00 | 0.00 | 62 |
| fast wave | 4 % → 0 % | 4.9 px | 0.00 | 0.00 | 194 |
| slow wave | 4 % → 0 % | 5.1 px | 0.81 | 0.01 | 197 |
| spiral | 7 % → 0 % | 4.6 px | 0.75 | 0.03 | 424 |
| loop | 4 % → 0 % | 5.5 px | 0.80 | 0.09 | 296 |
| tilted | 3 % → 2 % | 7.7 px | 0.66 | 0.84 | 160 |
| over the wet one | 3 % → 0 % | 2.1 px | 0.66 | 0.01 | 140 |
| long, no reload | 5 % → 0 % | 2.2 px | 0.76 | 0.00 | 471 | quarters: 0.07 → 0.03 → 0.03 → 0.02

Numbers say: light vs heavy: width 3.2 → 6.0 px, dark 0.00 → 0.00.

## Brush Artist · Refs · #22 Bold black brush poster
Ink 1.00 · 20 px · 29.6 s

![Brush Artist · Refs · #22 Bold black brush poster](Brush-Artist-Refs-22-Bold-black-brush-poster.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 4 % → 5 % | 10.3 px | 0.79 | 1.52 | 34 |
| heavy line | 15 % → 14 % | 42.6 px | 0.88 | 0.99 | 84 |
| pressure swell | 9 % → 9 % | 33.6 px | 0.87 | 1.03 | 60 |
| fast wave | 28 % → 27 % | 32.3 px | 0.88 | 0.98 | 206 |
| slow wave | 23 % → 23 % | 27.0 px | 0.87 | 0.98 | 338 |
| spiral | 35 % → 32 % | 23.0 px | 0.87 | 0.92 | 398 |
| loop | 22 % → 22 % | 28.2 px | 0.88 | 1.00 | 130 |
| tilted | 9 % → 9 % | 24.2 px | 0.88 | 1.00 | 76 |
| over the wet one | 20 % → 20 % | 30.8 px | 0.88 | 1.00 | 69 |
| long, no reload | 48 % → 38 % | 21.3 px | 0.85 | 0.79 | 440 | quarters: 0.56 → 0.45 → 0.35 → 0.26

Numbers say: light vs heavy: width 10.3 → 42.6 px, dark 0.79 → 0.88; wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #23 Dry white on orange + black line
Gouache 1.00 · 50 px · 25.4 s

![Brush Artist · Refs · #23 Dry white on orange + black line](Brush-Artist-Refs-23-Dry-white-on-orange-black-line.png)

A light paint: laid on a grey sheet (on white it cannot be seen); **dark** = how far it is from the grey either way.

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 3 % → 0 % | 9.9 px | 0.00 | 0.00 | 124 |
| heavy line | 9 % → 2 % | 26.8 px | 0.42 | 0.20 | 312 |
| pressure swell | 7 % → 0 % | 24.9 px | 0.41 | 0.03 | 111 |
| fast wave | 25 % → 0 % | 28.6 px | 0.00 | 0.00 | 372 |
| slow wave | 24 % → 1 % | 27.6 px | 0.40 | 0.02 | 684 |
| spiral | 33 % → 1 % | 21.5 px | 0.40 | 0.02 | 668 |
| loop | 20 % → 0 % | 26.0 px | 0.39 | 0.00 | 380 |
| tilted | 10 % → 9 % | 28.2 px | 0.38 | 0.93 | 403 |
| over the wet one | 15 % → 1 % | 13.1 px | 0.38 | 0.05 | 188 |
| long, no reload | 30 % → 4 % | 13.5 px | 0.40 | 0.12 | 1132 | quarters: 0.02 → 0.03 → 0.03 → 0.03

Numbers say: light vs heavy: width 9.9 → 26.8 px, dark 0.00 → 0.42; the long stroke does not run out of paint.

## Brush Artist · Refs · #24 Picasso flat oil
Oil 0.89 · Oil glaze 0.11 · 34 px · 17.0 s

![Brush Artist · Refs · #24 Picasso flat oil](Brush-Artist-Refs-24-Picasso-flat-oil.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 10 % → 10 % | 28.8 px | 0.39 | 1.00 | 121 |
| heavy line | 11 % → 11 % | 32.5 px | 0.39 | 1.00 | 195 |
| pressure swell | 8 % → 8 % | 31.7 px | 0.38 | 1.00 | 172 |
| fast wave | 30 % → 30 % | 35.2 px | 0.39 | 1.00 | 321 |
| slow wave | 28 % → 28 % | 32.8 px | 0.38 | 1.00 | 507 |
| spiral | 42 % → 42 % | 27.8 px | 0.38 | 1.00 | 558 |
| loop | 22 % → 22 % | 28.8 px | 0.40 | 1.00 | 333 |
| tilted | 11 % → 11 % | 31.3 px | 0.41 | 1.00 | 223 |
| over the wet one | 20 % → 20 % | 25.3 px | 0.41 | 1.00 | 158 |
| long, no reload | 58 % → 58 % | 26.0 px | 0.32 | 1.00 | 971 | quarters: 0.23 → 0.22 → 0.19 → 0.17

Numbers say: light vs heavy: width 28.8 → 32.5 px, dark 0.39 → 0.39.

## Brush Artist · Refs · #25 Yellow heavy flat stroke
Impasto 1.00 · 110 px · 40.5 s

![Brush Artist · Refs · #25 Yellow heavy flat stroke](Brush-Artist-Refs-25-Yellow-heavy-flat-stroke.png)

A light paint: laid on a grey sheet (on white it cannot be seen); **dark** = how far it is from the grey either way.

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 35 % → 35 % | 101.0 px | 0.31 | 1.00 | 389 |
| heavy line | 36 % → 35 % | 104.1 px | 0.31 | 0.97 | 433 |
| pressure swell | 28 % → 29 % | 104.0 px | 0.28 | 1.05 | 418 |
| fast wave | 72 % → 75 % | 82.8 px | 0.25 | 1.04 | 1342 |
| slow wave | 72 % → 71 % | 83.7 px | 0.30 | 0.98 | 2699 |
| spiral | 86 % → 81 % | 56.5 px | 0.30 | 0.94 | 2967 |
| loop | 64 % → 63 % | 82.7 px | 0.31 | 0.99 | 1097 |
| tilted | 25 % → 25 % | 70.3 px | 0.28 | 1.00 | 557 |
| over the wet one | 55 % → 53 % | 83.3 px | 0.28 | 0.97 | 548 |
| long, no reload | 98 % → 96 % | 43.9 px | 0.31 | 0.98 | 3513 | quarters: 0.00 → 0.00 → 0.00 → 0.00

Numbers say: light vs heavy: width 101.0 → 104.1 px, dark 0.31 → 0.31; pressure barely changes the width; the long stroke does not run out of paint.

## Brush Artist · Refs · #27 Orange impasto swatch
Impasto 1.00 · 60 px · 24.7 s

![Brush Artist · Refs · #27 Orange impasto swatch](Brush-Artist-Refs-27-Orange-impasto-swatch.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 18 % → 18 % | 52.9 px | 0.34 | 0.97 | 170 |
| heavy line | 21 % → 20 % | 60.0 px | 0.34 | 0.95 | 181 |
| pressure swell | 15 % → 15 % | 57.8 px | 0.36 | 0.97 | 162 |
| fast wave | 48 % → 46 % | 55.2 px | 0.37 | 0.97 | 699 |
| slow wave | 46 % → 45 % | 53.6 px | 0.33 | 0.97 | 924 |
| spiral | 68 % → 61 % | 45.1 px | 0.34 | 0.89 | 1301 |
| loop | 40 % → 39 % | 51.8 px | 0.33 | 0.97 | 528 |
| tilted | 16 % → 16 % | 43.7 px | 0.35 | 1.00 | 305 |
| over the wet one | 34 % → 32 % | 50.0 px | 0.35 | 0.97 | 399 |
| long, no reload | 84 % → 76 % | 37.8 px | 0.32 | 0.90 | 1691 | quarters: 0.30 → 0.29 → 0.28 → 0.25

Numbers say: light vs heavy: width 52.9 → 60.0 px, dark 0.34 → 0.34.

## Brush Artist · Refs · #28 Miles Davis black lines
Ink 1.00 · 22 px · 31.4 s

![Brush Artist · Refs · #28 Miles Davis black lines](Brush-Artist-Refs-28-Miles-Davis-black-lines.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 4 % → 6 % | 12.3 px | 0.80 | 1.40 | 49 |
| heavy line | 16 % → 16 % | 45.9 px | 0.88 | 0.99 | 132 |
| pressure swell | 10 % → 10 % | 36.7 px | 0.87 | 1.03 | 75 |
| fast wave | 29 % → 29 % | 33.8 px | 0.88 | 0.99 | 177 |
| slow wave | 27 % → 26 % | 30.7 px | 0.88 | 0.99 | 262 |
| spiral | 39 % → 36 % | 25.4 px | 0.87 | 0.93 | 326 |
| loop | 24 % → 24 % | 31.0 px | 0.88 | 1.00 | 160 |
| tilted | 9 % → 9 % | 26.0 px | 0.88 | 1.01 | 81 |
| over the wet one | 21 % → 21 % | 32.9 px | 0.88 | 1.00 | 109 |
| long, no reload | 53 % → 45 % | 23.9 px | 0.85 | 0.83 | 501 | quarters: 0.61 → 0.53 → 0.41 → 0.31

Numbers say: light vs heavy: width 12.3 → 45.9 px, dark 0.80 → 0.88.

## Brush Artist · Refs · #29 Shrigley magenta asterisk
Watercolour 1.00 · 70 px · 35.8 s

![Brush Artist · Refs · #29 Shrigley magenta asterisk](Brush-Artist-Refs-29-Shrigley-magenta-asterisk.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 10 % → 13 % | 28.0 px | 0.61 | 1.39 | 42 |
| heavy line | 17 % → 18 % | 50.3 px | 0.61 | 1.04 | 184 |
| pressure swell | 11 % → 13 % | 41.1 px | 0.62 | 1.14 | 83 |
| fast wave | 38 % → 38 % | 43.8 px | 0.60 | 1.01 | 293 |
| slow wave | 35 % → 39 % | 41.0 px | 0.62 | 1.11 | 502 |
| spiral | 61 % → 61 % | 40.0 px | 0.60 | 1.01 | 496 |
| loop | 31 % → 32 % | 40.2 px | 0.61 | 1.03 | 413 |
| tilted | 18 % → 18 % | 49.0 px | 0.61 | 1.00 | 206 |
| over the wet one | 31 % → 34 % | 38.5 px | 0.61 | 1.08 | 105 |
| long, no reload | 75 % → 76 % | 33.6 px | 0.60 | 1.01 | 713 | quarters: 0.53 → 0.50 → 0.48 → 0.45

Numbers say: light vs heavy: width 28.0 → 50.3 px, dark 0.61 → 0.61; the long stroke does not run out of paint.

## Brush Artist · Refs · #30 Red gouache face patch
Gouache 1.00 · 60 px · 45.1 s

![Brush Artist · Refs · #30 Red gouache face patch](Brush-Artist-Refs-30-Red-gouache-face-patch.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 16 % → 14 % | 45.5 px | 0.49 | 0.87 | 245 |
| heavy line | 25 % → 19 % | 71.4 px | 0.49 | 0.78 | 198 |
| pressure swell | 20 % → 17 % | 74.8 px | 0.50 | 0.84 | 148 |
| fast wave | 48 % → 28 % | 55.1 px | 0.51 | 0.58 | 487 |
| slow wave | 50 % → 31 % | 57.3 px | 0.48 | 0.62 | 730 |
| spiral | 59 % → 30 % | 39.0 px | 0.48 | 0.50 | 805 |
| loop | 40 % → 28 % | 51.4 px | 0.48 | 0.71 | 818 |
| tilted | 17 % → 17 % | 46.7 px | 0.50 | 1.00 | 286 |
| over the wet one | 37 % → 32 % | 55.9 px | 0.50 | 0.87 | 210 |
| long, no reload | 66 % → 28 % | 29.6 px | 0.46 | 0.42 | 1230 | quarters: 0.40 → 0.36 → 0.31 → 0.26

Numbers say: light vs heavy: width 45.5 → 71.4 px, dark 0.49 → 0.49.

## Brush Artist · Refs · #31 Warhol blotted line
Ink 1.00 · 6 px · 24.3 s

![Brush Artist · Refs · #31 Warhol blotted line](Brush-Artist-Refs-31-Warhol-blotted-line.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 1 % → 4 % | 3.0 px | 0.72 | 3.49 | 26 |
| heavy line | 7 % → 7 % | 19.5 px | 0.84 | 0.98 | 67 |
| pressure swell | 4 % → 4 % | 14.2 px | 0.82 | 1.18 | 27 |
| fast wave | 12 % → 9 % | 13.6 px | 0.81 | 0.73 | 133 |
| slow wave | 11 % → 9 % | 12.3 px | 0.80 | 0.80 | 100 |
| spiral | 15 % → 9 % | 10.0 px | 0.79 | 0.58 | 179 |
| loop | 10 % → 9 % | 12.6 px | 0.80 | 0.94 | 90 |
| tilted | 4 % → 4 % | 11.0 px | 0.83 | 1.03 | 43 |
| over the wet one | 9 % → 9 % | 14.0 px | 0.83 | 1.05 | 44 |
| long, no reload | 21 % → 10 % | 9.5 px | 0.78 | 0.45 | 329 | quarters: 0.25 → 0.13 → 0.05 → 0.01

Numbers say: light vs heavy: width 3.0 → 19.5 px, dark 0.72 → 0.84; wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #32 Thick orange swipes
Impasto 1.00 · 90 px · 36.0 s

![Brush Artist · Refs · #32 Thick orange swipes](Brush-Artist-Refs-32-Thick-orange-swipes.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 29 % → 28 % | 83.5 px | 0.37 | 0.99 | 426 |
| heavy line | 30 % → 29 % | 86.8 px | 0.37 | 0.97 | 297 |
| pressure swell | 23 % → 23 % | 84.8 px | 0.38 | 1.01 | 277 |
| fast wave | 64 % → 65 % | 74.2 px | 0.39 | 1.02 | 870 |
| slow wave | 64 % → 62 % | 73.9 px | 0.37 | 0.97 | 1508 |
| spiral | 80 % → 75 % | 52.6 px | 0.35 | 0.94 | 1687 |
| loop | 56 % → 55 % | 73.0 px | 0.36 | 0.97 | 921 |
| tilted | 21 % → 21 % | 58.8 px | 0.38 | 1.00 | 515 |
| over the wet one | 46 % → 45 % | 70.6 px | 0.38 | 0.96 | 409 |
| long, no reload | 95 % → 92 % | 42.8 px | 0.36 | 0.97 | 3226 | quarters: 0.35 → 0.35 → 0.35 → 0.34

Numbers say: light vs heavy: width 83.5 → 86.8 px, dark 0.37 → 0.37; pressure barely changes the width; the long stroke does not run out of paint.

## Brush Artist · Refs · #33 Red wet-in-wet band
Watercolour 1.00 · 80 px · 52.8 s

![Brush Artist · Refs · #33 Red wet-in-wet band](Brush-Artist-Refs-33-Red-wet-in-wet-band.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 24 % → 42 % | 69.3 px | 0.54 | 1.75 | 147 |
| heavy line | 33 % → 48 % | 96.9 px | 0.55 | 1.45 | 221 |
| pressure swell | 19 % → 30 % | 72.1 px | 0.57 | 1.56 | 144 |
| fast wave | 65 % → 79 % | 75.5 px | 0.60 | 1.21 | 736 |
| slow wave | 61 % → 78 % | 70.5 px | 0.63 | 1.28 | 916 |
| spiral | 77 % → 89 % | 50.8 px | 0.64 | 1.15 | 898 |
| loop | 54 % → 67 % | 70.5 px | 0.62 | 1.23 | 483 |
| tilted | 28 % → 30 % | 78.0 px | 0.58 | 1.09 | 287 |
| over the wet one | 55 % → 79 % | 76.7 px | 0.58 | 1.43 | 243 |
| long, no reload | 96 % → 99 % | 42.9 px | 0.66 | 1.04 | 1261 | quarters: 0.68 → 0.68 → 0.68 → 0.64

Numbers say: light vs heavy: width 69.3 → 96.9 px, dark 0.54 → 0.55; the long stroke does not run out of paint; wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #34 Magenta oil patches
Oil 0.89 · Oil glaze 0.11 · 60 px · 21.2 s

![Brush Artist · Refs · #34 Magenta oil patches](Brush-Artist-Refs-34-Magenta-oil-patches.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 18 % → 18 % | 51.4 px | 0.61 | 1.00 | 213 |
| heavy line | 19 % → 19 % | 55.1 px | 0.61 | 1.00 | 255 |
| pressure swell | 15 % → 15 % | 54.6 px | 0.61 | 1.01 | 205 |
| fast wave | 44 % → 45 % | 51.1 px | 0.61 | 1.02 | 829 |
| slow wave | 45 % → 45 % | 52.4 px | 0.61 | 1.00 | 1266 |
| spiral | 68 % → 68 % | 44.9 px | 0.58 | 1.00 | 1449 |
| loop | 42 % → 42 % | 54.2 px | 0.61 | 1.00 | 572 |
| tilted | 17 % → 17 % | 46.3 px | 0.61 | 1.00 | 409 |
| over the wet one | 34 % → 34 % | 48.4 px | 0.61 | 1.00 | 400 |
| long, no reload | 83 % → 83 % | 37.1 px | 0.59 | 1.00 | 2280 | quarters: 0.54 → 0.54 → 0.53 → 0.47

Numbers say: light vs heavy: width 51.4 → 55.1 px, dark 0.61 → 0.61; pressure barely changes the width; the long stroke does not run out of paint.

## Brush Artist · Refs · #35 Red band with runs
Watercolour 1.00 · 70 px · 52.9 s

![Brush Artist · Refs · #35 Red band with runs](Brush-Artist-Refs-35-Red-band-with-runs.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 40 % → 45 % | 115.3 px | 0.42 | 1.14 | 153 |
| heavy line | 45 % → 50 % | 132.0 px | 0.42 | 1.09 | 373 |
| pressure swell | 20 % → 28 % | 76.7 px | 0.48 | 1.37 | 150 |
| fast wave | 66 % → 76 % | 76.8 px | 0.49 | 1.14 | 959 |
| slow wave | 65 % → 76 % | 75.6 px | 0.52 | 1.16 | 936 |
| spiral | 86 % → 94 % | 56.9 px | 0.53 | 1.09 | 1055 |
| loop | 79 % → 88 % | 102.7 px | 0.49 | 1.11 | 378 |
| tilted | 50 % → 51 % | 139.1 px | 0.47 | 1.02 | 223 |
| over the wet one | 78 % → 84 % | 77.5 px | 0.47 | 1.09 | 169 |
| long, no reload | 96 % → 100 % | 43.2 px | 0.58 | 1.04 | 1088 | quarters: 0.59 → 0.60 → 0.59 → 0.56

Numbers say: light vs heavy: width 115.3 → 132.0 px, dark 0.42 → 0.42; the long stroke does not run out of paint.

## Brush Artist · Refs · #36 Magenta letters flat brush
Gouache 1.00 · 36 px · 37.1 s

![Brush Artist · Refs · #36 Magenta letters flat brush](Brush-Artist-Refs-36-Magenta-letters-flat-brush.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 10 % → 10 % | 29.6 px | 0.45 | 0.94 | 88 |
| heavy line | 16 % → 13 % | 47.5 px | 0.45 | 0.78 | 123 |
| pressure swell | 13 % → 11 % | 48.4 px | 0.47 | 0.85 | 240 |
| fast wave | 34 % → 16 % | 39.3 px | 0.47 | 0.48 | 260 |
| slow wave | 35 % → 20 % | 40.5 px | 0.45 | 0.57 | 471 |
| spiral | 46 % → 19 % | 30.6 px | 0.44 | 0.41 | 486 |
| loop | 27 % → 18 % | 35.0 px | 0.45 | 0.67 | 385 |
| tilted | 12 % → 12 % | 32.8 px | 0.47 | 1.00 | 137 |
| over the wet one | 26 % → 22 % | 38.5 px | 0.47 | 0.88 | 117 |
| long, no reload | 49 % → 19 % | 22.0 px | 0.44 | 0.39 | 629 | quarters: 0.30 → 0.27 → 0.22 → 0.18

Numbers say: light vs heavy: width 29.6 → 47.5 px, dark 0.45 → 0.45.

## Brush Artist · Refs · #37 Oil still life dabs
Oil 0.89 · Oil glaze 0.11 · 40 px · 17.4 s

![Brush Artist · Refs · #37 Oil still life dabs](Brush-Artist-Refs-37-Oil-still-life-dabs.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 11 % → 11 % | 32.1 px | 0.36 | 1.00 | 204 |
| heavy line | 12 % → 12 % | 36.1 px | 0.39 | 1.00 | 137 |
| pressure swell | 10 % → 10 % | 39.3 px | 0.40 | 1.00 | 231 |
| fast wave | 30 % → 30 % | 35.0 px | 0.39 | 1.00 | 501 |
| slow wave | 35 % → 35 % | 40.6 px | 0.37 | 1.00 | 657 |
| spiral | 52 % → 52 % | 34.4 px | 0.38 | 1.00 | 639 |
| loop | 29 % → 29 % | 36.9 px | 0.39 | 1.00 | 356 |
| tilted | 12 % → 12 % | 34.7 px | 0.41 | 1.00 | 188 |
| over the wet one | 23 % → 23 % | 30.6 px | 0.41 | 1.00 | 151 |
| long, no reload | 59 % → 59 % | 26.6 px | 0.31 | 1.00 | 1000 | quarters: 0.23 → 0.22 → 0.20 → 0.17

Numbers say: light vs heavy: width 32.1 → 36.1 px, dark 0.36 → 0.39.

## Brush Artist · Refs · #38 Sanguine drawing
Pastel 1.00 · 6 px · 9.9 s

![Brush Artist · Refs · #38 Sanguine drawing](Brush-Artist-Refs-38-Sanguine-drawing.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 1 % → 1 % | 2.1 px | 0.61 | 1.00 | 15 |
| heavy line | 1 % → 1 % | 3.9 px | 0.61 | 1.00 | 25 |
| pressure swell | 1 % → 1 % | 3.8 px | 0.61 | 1.00 | 13 |
| fast wave | 3 % → 3 % | 3.4 px | 0.61 | 1.00 | 37 |
| slow wave | 3 % → 3 % | 3.4 px | 0.61 | 1.00 | 38 |
| spiral | 4 % → 4 % | 2.8 px | 0.61 | 1.00 | 89 |
| loop | 2 % → 2 % | 3.1 px | 0.61 | 1.00 | 31 |
| tilted | 1 % → 1 % | 3.4 px | 0.61 | 1.00 | 22 |
| over the wet one | 2 % → 2 % | 2.9 px | 0.61 | 1.00 | 18 |
| long, no reload | 6 % → 6 % | 2.7 px | 0.61 | 1.00 | 86 | quarters: 0.04 → 0.04 → 0.04 → 0.04

Numbers say: light vs heavy: width 2.1 → 3.9 px, dark 0.61 → 0.61; the long stroke does not run out of paint.

## Brush Artist · Refs · #39 Very thick impasto
Impasto 1.00 · 60 px · 24.3 s

![Brush Artist · Refs · #39 Very thick impasto](Brush-Artist-Refs-39-Very-thick-impasto.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 18 % → 18 % | 53.1 px | 0.61 | 0.97 | 196 |
| heavy line | 21 % → 20 % | 60.0 px | 0.62 | 0.96 | 187 |
| pressure swell | 15 % → 15 % | 58.1 px | 0.62 | 0.97 | 170 |
| fast wave | 48 % → 47 % | 55.3 px | 0.63 | 0.98 | 556 |
| slow wave | 47 % → 45 % | 53.9 px | 0.61 | 0.97 | 961 |
| spiral | 69 % → 63 % | 45.3 px | 0.61 | 0.92 | 1092 |
| loop | 40 % → 39 % | 52.1 px | 0.61 | 0.97 | 492 |
| tilted | 16 % → 16 % | 43.8 px | 0.62 | 1.00 | 499 |
| over the wet one | 34 % → 33 % | 50.1 px | 0.62 | 0.97 | 250 |
| long, no reload | 85 % → 79 % | 38.0 px | 0.60 | 0.93 | 1865 | quarters: 0.56 → 0.55 → 0.54 → 0.51

Numbers say: light vs heavy: width 53.1 → 60.0 px, dark 0.61 → 0.62; the long stroke does not run out of paint.

## Brush Artist · Refs · #40 Watercolour blooms
Watercolour 1.00 · 90 px · 52.6 s

![Brush Artist · Refs · #40 Watercolour blooms](Brush-Artist-Refs-40-Watercolour-blooms.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 27 % → 47 % | 78.4 px | 0.08 | 1.72 | 191 |
| heavy line | 38 % → 51 % | 110.0 px | 0.09 | 1.36 | 319 |
| pressure swell | 24 % → 39 % | 91.8 px | 0.09 | 1.61 | 222 |
| fast wave | 68 % → 82 % | 78.3 px | 0.11 | 1.21 | 636 |
| slow wave | 68 % → 81 % | 79.1 px | 0.15 | 1.18 | 1787 |
| spiral | 81 % → 92 % | 53.5 px | 0.14 | 1.14 | 941 |
| loop | 58 % → 72 % | 75.3 px | 0.13 | 1.24 | 536 |
| tilted | 34 % → 36 % | 94.8 px | 0.11 | 1.07 | 332 |
| over the wet one | 62 % → 81 % | 78.2 px | 0.11 | 1.31 | 261 |
| long, no reload | 97 % → 100 % | 43.6 px | 0.17 | 1.03 | 1692 | quarters: 0.21 → 0.20 → 0.17 → 0.13

Numbers say: light vs heavy: width 78.4 → 110.0 px, dark 0.08 → 0.09; wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #41 Coloured pencil hatching
Pastel 1.00 · 4 px · 10.2 s

![Brush Artist · Refs · #41 Coloured pencil hatching](Brush-Artist-Refs-41-Coloured-pencil-hatching.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 1 % → 1 % | 1.6 px | 0.43 | 1.00 | 16 |
| heavy line | 1 % → 1 % | 2.9 px | 0.43 | 1.00 | 10 |
| pressure swell | 1 % → 1 % | 2.8 px | 0.43 | 1.00 | 14 |
| fast wave | 2 % → 2 % | 2.5 px | 0.43 | 1.00 | 32 |
| slow wave | 2 % → 2 % | 2.5 px | 0.43 | 1.00 | 27 |
| spiral | 3 % → 3 % | 2.1 px | 0.43 | 1.00 | 81 |
| loop | 2 % → 2 % | 2.3 px | 0.43 | 1.00 | 36 |
| tilted | 1 % → 1 % | 3.0 px | 0.43 | 1.00 | 51 |
| over the wet one | 2 % → 2 % | 2.3 px | 0.43 | 1.00 | 37 |
| long, no reload | 5 % → 5 % | 2.0 px | 0.42 | 1.00 | 145 | quarters: 0.02 → 0.02 → 0.02 → 0.02

Numbers say: light vs heavy: width 1.6 → 2.9 px, dark 0.43 → 0.43; the long stroke does not run out of paint.

## Brush Artist · Refs · #42 Oil pastel shaggy
Pastel 1.00 · 18 px · 10.9 s

![Brush Artist · Refs · #42 Oil pastel shaggy](Brush-Artist-Refs-42-Oil-pastel-shaggy.png)

A light paint: laid on a grey sheet (on white it cannot be seen); **dark** = how far it is from the grey either way.

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 2 % → 2 % | 4.7 px | 0.36 | 1.00 | 16 |
| heavy line | 3 % → 3 % | 10.0 px | 0.36 | 1.00 | 40 |
| pressure swell | 2 % → 2 % | 9.3 px | 0.34 | 1.00 | 37 |
| fast wave | 8 % → 8 % | 9.2 px | 0.32 | 1.00 | 214 |
| slow wave | 7 % → 7 % | 8.6 px | 0.37 | 1.00 | 177 |
| spiral | 11 % → 11 % | 7.5 px | 0.36 | 1.00 | 123 |
| loop | 6 % → 6 % | 7.8 px | 0.35 | 1.00 | 53 |
| tilted | 2 % → 2 % | 6.5 px | 0.33 | 1.00 | 31 |
| over the wet one | 5 % → 5 % | 7.6 px | 0.33 | 1.00 | 24 |
| long, no reload | 15 % → 15 % | 6.5 px | 0.37 | 1.00 | 180 | quarters: 0.00 → 0.00 → 0.00 → 0.00

Numbers say: light vs heavy: width 4.7 → 10.0 px, dark 0.36 → 0.36; the long stroke does not run out of paint.

## Brush Artist · Refs · #43 Dragged black ink blocks
Gouache 1.00 · 70 px · 27.1 s

![Brush Artist · Refs · #43 Dragged black ink blocks](Brush-Artist-Refs-43-Dragged-black-ink-blocks.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 5 % → 0 % | 14.8 px | 0.00 | 0.00 | 110 |
| heavy line | 14 % → 4 % | 40.5 px | 0.66 | 0.27 | 286 |
| pressure swell | 11 % → 4 % | 42.1 px | 0.65 | 0.33 | 160 |
| fast wave | 38 % → 1 % | 43.8 px | 0.66 | 0.03 | 654 |
| slow wave | 32 % → 2 % | 36.6 px | 0.57 | 0.05 | 981 |
| spiral | 51 % → 4 % | 33.4 px | 0.54 | 0.07 | 1357 |
| loop | 30 % → 2 % | 38.3 px | 0.62 | 0.06 | 491 |
| tilted | 13 % → 13 % | 37.0 px | 0.66 | 0.95 | 349 |
| over the wet one | 21 % → 2 % | 22.9 px | 0.66 | 0.10 | 313 |
| long, no reload | 44 % → 7 % | 19.8 px | 0.66 | 0.16 | 1217 | quarters: 0.47 → 0.37 → 0.18 → 0.13

Numbers say: light vs heavy: width 14.8 → 40.5 px, dark 0.00 → 0.66.

## Brush Artist · Refs · #44 Blue looping ribbon
Oil 1.00 · 80 px · 27.9 s

![Brush Artist · Refs · #44 Blue looping ribbon](Brush-Artist-Refs-44-Blue-looping-ribbon.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 25 % → 26 % | 73.1 px | 0.72 | 1.04 | 277 |
| heavy line | 27 % → 27 % | 77.7 px | 0.71 | 1.00 | 298 |
| pressure swell | 20 % → 21 % | 76.5 px | 0.71 | 1.03 | 242 |
| fast wave | 62 % → 64 % | 71.4 px | 0.71 | 1.04 | 1002 |
| slow wave | 58 % → 58 % | 67.4 px | 0.70 | 1.00 | 1507 |
| spiral | 76 % → 77 % | 50.3 px | 0.69 | 1.00 | 1899 |
| loop | 53 % → 53 % | 69.2 px | 0.69 | 1.00 | 1076 |
| tilted | 20 % → 20 % | 56.1 px | 0.74 | 1.00 | 396 |
| over the wet one | 41 % → 41 % | 58.7 px | 0.74 | 1.00 | 323 |
| long, no reload | 90 % → 90 % | 40.1 px | 0.69 | 1.00 | 2213 | quarters: 0.67 → 0.68 → 0.66 → 0.59

Numbers say: light vs heavy: width 73.1 → 77.7 px, dark 0.72 → 0.71; pressure barely changes the width; the long stroke does not run out of paint.

## Brush Artist · Refs · #45 Soft pastel pepper
Pastel 1.00 · 40 px · 11.2 s

![Brush Artist · Refs · #45 Soft pastel pepper](Brush-Artist-Refs-45-Soft-pastel-pepper.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 4 % → 4 % | 11.0 px | 0.53 | 1.00 | 71 |
| heavy line | 7 % → 7 % | 21.2 px | 0.53 | 1.00 | 52 |
| pressure swell | 5 % → 5 % | 19.0 px | 0.55 | 1.00 | 49 |
| fast wave | 17 % → 17 % | 19.3 px | 0.56 | 1.00 | 157 |
| slow wave | 16 % → 16 % | 18.0 px | 0.54 | 1.00 | 422 |
| spiral | 23 % → 23 % | 15.4 px | 0.54 | 1.00 | 249 |
| loop | 12 % → 12 % | 15.4 px | 0.54 | 1.00 | 122 |
| tilted | 4 % → 4 % | 11.4 px | 0.55 | 1.00 | 73 |
| over the wet one | 10 % → 10 % | 16.7 px | 0.55 | 1.00 | 70 |
| long, no reload | 28 % → 28 % | 12.6 px | 0.53 | 1.00 | 507 | quarters: 0.17 → 0.16 → 0.17 → 0.17

Numbers say: light vs heavy: width 11.0 → 21.2 px, dark 0.53 → 0.53; the long stroke does not run out of paint.

## Brush Artist · Refs · #46 Red-brown ink lips
Watercolour 1.00 · 50 px · 42.9 s

![Brush Artist · Refs · #46 Red-brown ink lips](Brush-Artist-Refs-46-Red-brown-ink-lips.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 15 % → 31 % | 43.9 px | 0.59 | 2.04 | 76 |
| heavy line | 22 % → 35 % | 63.4 px | 0.60 | 1.58 | 253 |
| pressure swell | 13 % → 22 % | 50.3 px | 0.63 | 1.64 | 73 |
| fast wave | 43 % → 64 % | 49.7 px | 0.64 | 1.50 | 317 |
| slow wave | 42 % → 63 % | 49.1 px | 0.67 | 1.49 | 522 |
| spiral | 65 % → 79 % | 42.6 px | 0.69 | 1.22 | 417 |
| loop | 38 % → 55 % | 48.8 px | 0.67 | 1.47 | 231 |
| tilted | 21 % → 23 % | 58.2 px | 0.60 | 1.11 | 119 |
| over the wet one | 42 % → 63 % | 58.5 px | 0.60 | 1.51 | 101 |
| long, no reload | 78 % → 95 % | 35.1 px | 0.70 | 1.21 | 657 | quarters: 0.71 → 0.71 → 0.69 → 0.65

Numbers say: light vs heavy: width 43.9 → 63.4 px, dark 0.59 → 0.60; the long stroke does not run out of paint; wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #47 Pink knife slabs
Impasto 1.00 · 90 px · 29.3 s

![Brush Artist · Refs · #47 Pink knife slabs](Brush-Artist-Refs-47-Pink-knife-slabs.png)

A light paint: laid on a grey sheet (on white it cannot be seen); **dark** = how far it is from the grey either way.

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 27 % → 26 % | 78.7 px | 0.29 | 0.97 | 238 |
| heavy line | 29 % → 28 % | 84.6 px | 0.29 | 0.96 | 314 |
| pressure swell | 22 % → 22 % | 81.2 px | 0.26 | 1.01 | 251 |
| fast wave | 62 % → 61 % | 71.8 px | 0.24 | 0.98 | 869 |
| slow wave | 62 % → 58 % | 71.5 px | 0.28 | 0.94 | 1046 |
| spiral | 75 % → 60 % | 49.3 px | 0.28 | 0.80 | 1195 |
| loop | 56 % → 54 % | 72.1 px | 0.29 | 0.97 | 544 |
| tilted | 22 % → 22 % | 60.2 px | 0.25 | 1.00 | 463 |
| over the wet one | 46 % → 44 % | 69.3 px | 0.25 | 0.96 | 293 |
| long, no reload | 93 % → 77 % | 41.9 px | 0.26 | 0.83 | 2009 | quarters: 0.00 → 0.00 → 0.00 → 0.00

Numbers say: light vs heavy: width 78.7 → 84.6 px, dark 0.29 → 0.29; pressure barely changes the width; the long stroke does not run out of paint.

## Brush Artist · Refs · #48 Black bands with drips
Gouache 1.00 · 70 px · 48.7 s

![Brush Artist · Refs · #48 Black bands with drips](Brush-Artist-Refs-48-Black-bands-with-drips.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 28 % → 23 % | 80.2 px | 0.63 | 0.82 | 205 |
| heavy line | 35 % → 26 % | 100.7 px | 0.64 | 0.75 | 248 |
| pressure swell | 25 % → 21 % | 93.8 px | 0.63 | 0.85 | 172 |
| fast wave | 63 % → 41 % | 72.9 px | 0.63 | 0.64 | 597 |
| slow wave | 62 % → 41 % | 71.5 px | 0.63 | 0.66 | 1150 |
| spiral | 69 % → 40 % | 45.7 px | 0.61 | 0.57 | 1221 |
| loop | 54 % → 40 % | 69.9 px | 0.63 | 0.74 | 543 |
| tilted | 29 % → 29 % | 80.5 px | 0.62 | 1.01 | 347 |
| over the wet one | 59 % → 48 % | 82.9 px | 0.62 | 0.82 | 265 |
| long, no reload | 78 % → 37 % | 34.9 px | 0.61 | 0.47 | 1425 | quarters: 0.58 → 0.54 → 0.47 → 0.39

Numbers say: light vs heavy: width 80.2 → 100.7 px, dark 0.63 → 0.64.

## Brush Artist · Refs · #49 Magenta letters round brush
Ink 1.00 · 30 px · 31.5 s

![Brush Artist · Refs · #49 Magenta letters round brush](Brush-Artist-Refs-49-Magenta-letters-round-brush.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 6 % → 8 % | 18.1 px | 0.49 | 1.21 | 40 |
| heavy line | 21 % → 20 % | 60.3 px | 0.51 | 0.98 | 104 |
| pressure swell | 13 % → 13 % | 47.1 px | 0.51 | 1.01 | 61 |
| fast wave | 38 % → 38 % | 44.0 px | 0.51 | 1.00 | 266 |
| slow wave | 34 % → 34 % | 39.4 px | 0.51 | 0.99 | 306 |
| spiral | 49 % → 48 % | 32.6 px | 0.51 | 0.96 | 360 |
| loop | 30 % → 30 % | 38.3 px | 0.51 | 1.00 | 228 |
| tilted | 11 % → 12 % | 32.0 px | 0.52 | 1.00 | 83 |
| over the wet one | 27 % → 27 % | 42.2 px | 0.52 | 1.01 | 79 |
| long, no reload | 63 % → 56 % | 28.2 px | 0.50 | 0.90 | 513 | quarters: 0.42 → 0.37 → 0.30 → 0.25

Numbers say: light vs heavy: width 18.1 → 60.3 px, dark 0.49 → 0.51.

## Brush Artist · Refs · #50 Thick swipes on photo
Impasto 1.00 · 40 px · 18.3 s

![Brush Artist · Refs · #50 Thick swipes on photo](Brush-Artist-Refs-50-Thick-swipes-on-photo.png)

A light paint: laid on a grey sheet (on white it cannot be seen); **dark** = how far it is from the grey either way.

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 13 % → 13 % | 38.6 px | 0.27 | 0.95 | 133 |
| heavy line | 14 % → 13 % | 40.0 px | 0.27 | 0.96 | 121 |
| pressure swell | 11 % → 10 % | 40.1 px | 0.24 | 0.95 | 86 |
| fast wave | 35 % → 31 % | 40.1 px | 0.24 | 0.89 | 344 |
| slow wave | 34 % → 32 % | 39.5 px | 0.26 | 0.93 | 683 |
| spiral | 58 % → 46 % | 38.5 px | 0.29 | 0.79 | 613 |
| loop | 29 % → 28 % | 37.4 px | 0.26 | 0.96 | 308 |
| tilted | 12 % → 12 % | 33.6 px | 0.22 | 1.00 | 201 |
| over the wet one | 25 % → 24 % | 36.7 px | 0.22 | 0.96 | 153 |
| long, no reload | 68 % → 46 % | 30.4 px | 0.26 | 0.68 | 1046 | quarters: 0.00 → 0.00 → 0.00 → 0.00

Numbers say: light vs heavy: width 38.6 → 40.0 px, dark 0.27 → 0.27; pressure barely changes the width.

## Brush Artist · Refs · Drag #e8b4a8
Gouache 1.00 · 40 px · 16.8 s

![Brush Artist · Refs · Drag #e8b4a8](Brush-Artist-Refs-Drag-e8b4a8.png)

A light paint: laid on a grey sheet (on white it cannot be seen); **dark** = how far it is from the grey either way.

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 3 % → 0 % | 9.3 px | 0.00 | 0.00 | 122 |
| heavy line | 6 % → 0 % | 16.2 px | 0.34 | 0.01 | 143 |
| pressure swell | 3 % → 0 % | 12.9 px | 0.00 | 0.00 | 79 |
| fast wave | 16 % → 0 % | 18.1 px | 0.00 | 0.00 | 380 |
| slow wave | 13 % → 0 % | 15.0 px | 0.00 | 0.00 | 650 |
| spiral | 20 % → 0 % | 13.4 px | 0.00 | 0.00 | 537 |
| loop | 13 % → 0 % | 17.1 px | 0.00 | 0.00 | 323 |
| tilted | 6 % → 5 % | 16.8 px | 0.00 | 0.77 | 148 |
| over the wet one | 7 % → 0 % | 1.8 px | 0.00 | 0.00 | 103 |
| long, no reload | 10 % → 0 % | 4.6 px | 0.00 | 0.00 | 642 | quarters: 0.02 → 0.02 → 0.02 → 0.02

Numbers say: light vs heavy: width 9.3 → 16.2 px, dark 0.00 → 0.34; the long stroke does not run out of paint.

## Brush Artist · Refs · Drag #e8e4e0
Gouache 1.00 · 40 px · 18.2 s

![Brush Artist · Refs · Drag #e8e4e0](Brush-Artist-Refs-Drag-e8e4e0.png)

A light paint: laid on a grey sheet (on white it cannot be seen); **dark** = how far it is from the grey either way.

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 3 % → 0 % | 9.3 px | 0.00 | 0.00 | 99 |
| heavy line | 6 % → 0 % | 16.2 px | 0.43 | 0.01 | 137 |
| pressure swell | 3 % → 0 % | 12.9 px | 0.00 | 0.00 | 86 |
| fast wave | 16 % → 0 % | 18.1 px | 0.00 | 0.00 | 335 |
| slow wave | 13 % → 0 % | 15.0 px | 0.00 | 0.00 | 499 |
| spiral | 20 % → 0 % | 13.4 px | 0.00 | 0.00 | 502 |
| loop | 13 % → 0 % | 17.1 px | 0.00 | 0.00 | 245 |
| tilted | 6 % → 5 % | 16.8 px | 0.00 | 0.77 | 134 |
| over the wet one | 7 % → 0 % | 1.8 px | 0.00 | 0.00 | 99 |
| long, no reload | 10 % → 0 % | 4.6 px | 0.00 | 0.00 | 610 | quarters: 0.02 → 0.02 → 0.02 → 0.02

Numbers say: light vs heavy: width 9.3 → 16.2 px, dark 0.00 → 0.43; the long stroke does not run out of paint.

## Brush Artist · Refs · Finger
Pastel 1.00 · 36 px · 21.5 s · over bands of wet oil paint and oil pastel in turn (it works on paint already there: look at what it does to the bands; covered counts the bands too)

![Brush Artist · Refs · Finger](Brush-Artist-Refs-Finger.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 26 % → 26 % | 74.4 px | 0.80 | 1.00 | 42 |
| heavy line | 27 % → 27 % | 79.3 px | 0.80 | 1.00 | 42 |
| pressure swell | 26 % → 26 % | 98.0 px | 0.80 | 1.00 | 41 |
| fast wave | 33 % → 33 % | 38.0 px | 0.78 | 1.00 | 113 |
| slow wave | 31 % → 31 % | 36.3 px | 0.78 | 1.00 | 205 |
| spiral | 38 % → 38 % | 25.3 px | 0.76 | 1.00 | 204 |
| loop | 31 % → 31 % | 39.5 px | 0.79 | 1.00 | 104 |
| tilted | 26 % → 26 % | 73.5 px | 0.78 | 1.00 | 58 |
| over the wet one | 29 % → 29 % | 7.5 px | 0.78 | 1.00 | 50 |
| long, no reload | 39 % → 39 % | 17.4 px | 0.76 | 1.00 | 280 | quarters: 0.24 → 0.36 → 0.32 → 0.37

Numbers say: light vs heavy: width 74.4 → 79.3 px, dark 0.80 → 0.80; pressure barely changes the width; the long stroke does not run out of paint.

## Brush Artist · Ink — wash
Watercolour 1.00 · 38 px · 33.9 s

![Brush Artist · Ink — wash](Brush-Artist-Ink-wash.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 11 % → 11 % | 31.6 px | 0.39 | 1.04 | 54 |
| heavy line | 19 % → 19 % | 54.3 px | 0.32 | 1.03 | 109 |
| pressure swell | 12 % → 13 % | 45.2 px | 0.37 | 1.04 | 62 |
| fast wave | 39 % → 41 % | 45.5 px | 0.31 | 1.04 | 185 |
| slow wave | 37 % → 38 % | 42.9 px | 0.37 | 1.03 | 385 |
| spiral | 58 % → 61 % | 38.6 px | 0.31 | 1.04 | 309 |
| loop | 32 % → 33 % | 41.9 px | 0.35 | 1.02 | 161 |
| tilted | 13 % → 14 % | 37.0 px | 0.38 | 1.04 | 94 |
| over the wet one | 29 % → 30 % | 42.8 px | 0.38 | 1.04 | 71 |
| long, no reload | 67 % → 72 % | 30.0 px | 0.29 | 1.07 | 513 | quarters: 0.34 → 0.27 → 0.19 → 0.12

Numbers say: light vs heavy: width 31.6 → 54.3 px, dark 0.39 → 0.32.

## Brush Artist · Ink — brush line
Ink 1.00 · 16 px · 29.3 s

![Brush Artist · Ink — brush line](Brush-Artist-Ink-brush-line.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 3 % → 5 % | 8.2 px | 0.77 | 1.72 | 32 |
| heavy line | 12 % → 12 % | 35.2 px | 0.88 | 0.99 | 83 |
| pressure swell | 8 % → 8 % | 28.5 px | 0.86 | 1.06 | 51 |
| fast wave | 24 % → 24 % | 28.2 px | 0.87 | 0.98 | 132 |
| slow wave | 20 % → 20 % | 23.7 px | 0.87 | 0.97 | 167 |
| spiral | 31 % → 27 % | 20.3 px | 0.86 | 0.87 | 298 |
| loop | 19 % → 19 % | 24.3 px | 0.87 | 0.99 | 145 |
| tilted | 8 % → 8 % | 21.2 px | 0.88 | 1.01 | 91 |
| over the wet one | 17 % → 17 % | 26.2 px | 0.88 | 1.01 | 75 |
| long, no reload | 44 % → 31 % | 19.7 px | 0.84 | 0.70 | 418 | quarters: 0.51 → 0.41 → 0.30 → 0.20

Numbers say: light vs heavy: width 8.2 → 35.2 px, dark 0.77 → 0.88; wet paint spreads well beyond the stroke.

## Brush Artist · Ink — dry brush
Gouache 1.00 · 30 px · 21.7 s

![Brush Artist · Ink — dry brush](Brush-Artist-Ink-dry-brush.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 2 % → 0 % | 5.7 px | 0.00 | 0.00 | 46 |
| heavy line | 4 % → 0 % | 10.2 px | 0.77 | 0.01 | 106 |
| pressure swell | 4 % → 0 % | 14.1 px | 0.77 | 0.06 | 69 |
| fast wave | 12 % → 0 % | 14.0 px | 0.77 | 0.00 | 342 |
| slow wave | 10 % → 0 % | 11.9 px | 0.77 | 0.00 | 444 |
| spiral | 17 % → 0 % | 11.1 px | 0.77 | 0.00 | 453 |
| loop | 9 % → 0 % | 11.2 px | 0.77 | 0.01 | 320 |
| tilted | 5 % → 4 % | 13.5 px | 0.77 | 0.89 | 117 |
| over the wet one | 7 % → 0 % | 5.9 px | 0.77 | 0.00 | 94 |
| long, no reload | 14 % → 1 % | 6.5 px | 0.77 | 0.08 | 1069 | quarters: 0.21 → 0.14 → 0.10 → 0.07

Numbers say: light vs heavy: width 5.7 → 10.2 px, dark 0.00 → 0.77.

## Brush Artist · Watercolour — blue
Watercolour 0.93 · Ink 0.07 · 40 px · 31.8 s

![Brush Artist · Watercolour — blue](Brush-Artist-Watercolour-blue.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 6 % → 11 % | 16.2 px | 0.29 | 1.88 | 38 |
| heavy line | 11 % → 13 % | 31.9 px | 0.29 | 1.17 | 85 |
| pressure swell | 7 % → 9 % | 25.7 px | 0.30 | 1.38 | 59 |
| fast wave | 24 % → 27 % | 28.2 px | 0.29 | 1.12 | 149 |
| slow wave | 23 % → 32 % | 26.4 px | 0.31 | 1.41 | 323 |
| spiral | 39 % → 47 % | 25.6 px | 0.29 | 1.21 | 268 |
| loop | 20 % → 25 % | 25.7 px | 0.30 | 1.25 | 135 |
| tilted | 12 % → 12 % | 34.0 px | 0.30 | 1.00 | 133 |
| over the wet one | 21 % → 25 % | 25.2 px | 0.30 | 1.19 | 129 |
| long, no reload | 53 % → 59 % | 23.6 px | 0.30 | 1.12 | 333 | quarters: 0.23 → 0.21 → 0.19 → 0.16

Numbers say: light vs heavy: width 16.2 → 31.9 px, dark 0.29 → 0.29; wet paint spreads well beyond the stroke.

## Brush Artist · Watercolour — violet
Watercolour 0.93 · Ink 0.07 · 40 px · 31.3 s

![Brush Artist · Watercolour — violet](Brush-Artist-Watercolour-violet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 6 % → 11 % | 16.2 px | 0.36 | 1.88 | 34 |
| heavy line | 11 % → 13 % | 31.9 px | 0.37 | 1.17 | 63 |
| pressure swell | 7 % → 9 % | 25.7 px | 0.38 | 1.38 | 37 |
| fast wave | 24 % → 27 % | 28.2 px | 0.38 | 1.12 | 129 |
| slow wave | 23 % → 32 % | 26.4 px | 0.39 | 1.41 | 262 |
| spiral | 39 % → 47 % | 25.6 px | 0.37 | 1.21 | 294 |
| loop | 20 % → 25 % | 25.7 px | 0.38 | 1.25 | 134 |
| tilted | 12 % → 12 % | 34.0 px | 0.38 | 1.00 | 95 |
| over the wet one | 21 % → 25 % | 25.2 px | 0.38 | 1.19 | 81 |
| long, no reload | 53 % → 59 % | 23.6 px | 0.38 | 1.12 | 463 | quarters: 0.28 → 0.27 → 0.24 → 0.21

Numbers say: light vs heavy: width 16.2 → 31.9 px, dark 0.36 → 0.37; wet paint spreads well beyond the stroke.

## Brush Artist · Watercolour — teal
Watercolour 0.93 · Ink 0.07 · 40 px · 30.2 s

![Brush Artist · Watercolour — teal](Brush-Artist-Watercolour-teal.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 6 % → 11 % | 16.2 px | 0.23 | 1.88 | 33 |
| heavy line | 11 % → 13 % | 31.9 px | 0.23 | 1.17 | 65 |
| pressure swell | 7 % → 9 % | 25.7 px | 0.24 | 1.38 | 42 |
| fast wave | 24 % → 27 % | 28.2 px | 0.23 | 1.12 | 217 |
| slow wave | 23 % → 32 % | 26.4 px | 0.25 | 1.41 | 327 |
| spiral | 39 % → 47 % | 25.6 px | 0.23 | 1.21 | 183 |
| loop | 20 % → 25 % | 25.7 px | 0.24 | 1.25 | 129 |
| tilted | 12 % → 12 % | 34.0 px | 0.24 | 1.00 | 127 |
| over the wet one | 21 % → 25 % | 25.2 px | 0.24 | 1.19 | 63 |
| long, no reload | 53 % → 59 % | 23.6 px | 0.24 | 1.12 | 438 | quarters: 0.18 → 0.16 → 0.15 → 0.13

Numbers say: light vs heavy: width 16.2 → 31.9 px, dark 0.23 → 0.23; wet paint spreads well beyond the stroke.

## Brush Artist · Gouache
Gouache 1.00 · 30 px · 33.5 s

![Brush Artist · Gouache](Brush-Artist-Gouache.png)

A light paint: laid on a grey sheet (on white it cannot be seen); **dark** = how far it is from the grey either way.

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 8 % → 8 % | 24.4 px | 0.27 | 0.97 | 60 |
| heavy line | 15 % → 12 % | 42.8 px | 0.27 | 0.78 | 130 |
| pressure swell | 11 % → 9 % | 41.0 px | 0.27 | 0.85 | 93 |
| fast wave | 30 % → 14 % | 34.9 px | 0.26 | 0.45 | 283 |
| slow wave | 29 % → 14 % | 34.0 px | 0.26 | 0.47 | 335 |
| spiral | 40 % → 14 % | 26.6 px | 0.26 | 0.35 | 391 |
| loop | 24 % → 15 % | 30.6 px | 0.26 | 0.62 | 222 |
| tilted | 10 % → 10 % | 27.4 px | 0.27 | 1.01 | 102 |
| over the wet one | 22 % → 19 % | 32.9 px | 0.27 | 0.89 | 97 |
| long, no reload | 43 % → 15 % | 19.1 px | 0.26 | 0.35 | 754 | quarters: 0.01 → 0.01 → 0.01 → 0.01

Numbers say: light vs heavy: width 24.4 → 42.8 px, dark 0.27 → 0.27; the long stroke does not run out of paint.

## Brush Artist · Oil — bristle
Oil 0.89 · Oil glaze 0.11 · 30 px · 15.9 s

![Brush Artist · Oil — bristle](Brush-Artist-Oil-bristle.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 10 % → 10 % | 28.5 px | 0.53 | 1.00 | 175 |
| heavy line | 11 % → 11 % | 32.4 px | 0.54 | 1.00 | 176 |
| pressure swell | 8 % → 8 % | 31.8 px | 0.54 | 1.00 | 72 |
| fast wave | 28 % → 28 % | 32.0 px | 0.54 | 1.00 | 293 |
| slow wave | 27 % → 27 % | 31.6 px | 0.54 | 1.00 | 546 |
| spiral | 48 % → 48 % | 31.3 px | 0.53 | 1.00 | 524 |
| loop | 22 % → 22 % | 28.9 px | 0.54 | 1.00 | 353 |
| tilted | 11 % → 11 % | 29.9 px | 0.54 | 1.00 | 163 |
| over the wet one | 21 % → 21 % | 29.6 px | 0.54 | 1.00 | 130 |
| long, no reload | 55 % → 55 % | 24.7 px | 0.52 | 1.00 | 848 | quarters: 0.35 → 0.33 → 0.31 → 0.29

Numbers say: light vs heavy: width 28.5 → 32.4 px, dark 0.53 → 0.54.

## Brush Artist · Charcoal — stick
Charcoal 0.78 · Pastel 0.22 · 28 px · 11.8 s

![Brush Artist · Charcoal — stick](Brush-Artist-Charcoal-stick.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 5 % → 5 % | 15.2 px | 0.85 | 1.00 | 27 |
| heavy line | 8 % → 8 % | 24.2 px | 0.85 | 1.00 | 26 |
| pressure swell | 5 % → 5 % | 19.3 px | 0.85 | 1.00 | 14 |
| fast wave | 19 % → 19 % | 21.5 px | 0.85 | 1.00 | 88 |
| slow wave | 18 % → 18 % | 21.1 px | 0.85 | 1.00 | 127 |
| spiral | 25 % → 25 % | 16.3 px | 0.85 | 1.00 | 124 |
| loop | 16 % → 16 % | 20.2 px | 0.85 | 1.00 | 114 |
| tilted | 6 % → 6 % | 17.3 px | 0.85 | 1.00 | 26 |
| over the wet one | 14 % → 14 % | 20.5 px | 0.85 | 1.00 | 28 |
| long, no reload | 41 % → 41 % | 18.5 px | 0.85 | 1.00 | 161 | quarters: 0.39 → 0.39 → 0.39 → 0.39

Numbers say: light vs heavy: width 15.2 → 24.2 px, dark 0.85 → 0.85; the long stroke does not run out of paint.

## Brush Artist · Charcoal — stick B
Charcoal 0.78 · Pastel 0.22 · 36 px · 11.2 s

![Brush Artist · Charcoal — stick B](Brush-Artist-Charcoal-stick-B.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 7 % → 7 % | 19.2 px | 0.85 | 1.00 | 30 |
| heavy line | 10 % → 10 % | 30.5 px | 0.85 | 1.00 | 41 |
| pressure swell | 7 % → 7 % | 24.5 px | 0.85 | 1.00 | 29 |
| fast wave | 24 % → 24 % | 27.6 px | 0.85 | 1.00 | 154 |
| slow wave | 23 % → 23 % | 26.6 px | 0.85 | 1.00 | 249 |
| spiral | 35 % → 35 % | 23.2 px | 0.85 | 1.00 | 212 |
| loop | 19 % → 19 % | 25.2 px | 0.85 | 1.00 | 94 |
| tilted | 7 % → 7 % | 20.3 px | 0.85 | 1.00 | 31 |
| over the wet one | 17 % → 17 % | 25.9 px | 0.85 | 1.00 | 50 |
| long, no reload | 50 % → 50 % | 22.6 px | 0.85 | 1.00 | 221 | quarters: 0.47 → 0.47 → 0.47 → 0.47

Numbers say: light vs heavy: width 19.2 → 30.5 px, dark 0.85 → 0.85; the long stroke does not run out of paint.

## Brush Artist · Charcoal — stick C
Charcoal 0.78 · Pastel 0.22 · 22 px · 9.9 s

![Brush Artist · Charcoal — stick C](Brush-Artist-Charcoal-stick-C.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 4 % → 4 % | 12.2 px | 0.85 | 1.00 | 11 |
| heavy line | 7 % → 7 % | 19.4 px | 0.85 | 1.00 | 23 |
| pressure swell | 4 % → 4 % | 14.3 px | 0.85 | 1.00 | 10 |
| fast wave | 15 % → 15 % | 17.1 px | 0.85 | 1.00 | 52 |
| slow wave | 15 % → 15 % | 17.0 px | 0.85 | 1.00 | 91 |
| spiral | 20 % → 20 % | 13.3 px | 0.85 | 1.00 | 86 |
| loop | 12 % → 12 % | 16.1 px | 0.85 | 1.00 | 45 |
| tilted | 5 % → 5 % | 15.1 px | 0.85 | 1.00 | 21 |
| over the wet one | 11 % → 11 % | 16.8 px | 0.85 | 1.00 | 28 |
| long, no reload | 34 % → 34 % | 15.3 px | 0.85 | 1.00 | 141 | quarters: 0.33 → 0.32 → 0.32 → 0.32

Numbers say: light vs heavy: width 12.2 → 19.4 px, dark 0.85 → 0.85; the long stroke does not run out of paint.

## Oil · Henry Ward · Loaded flat
Gouache 1.00 + turpentine 35 % · 84 px · 44.2 s

![Oil · Henry Ward · Loaded flat](Oil-Henry-Ward-Loaded-flat.png)

A light paint: laid on a grey sheet (on white it cannot be seen); **dark** = how far it is from the grey either way.

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 11 % → 3 % | 30.6 px | 0.39 | 0.24 | 241 |
| heavy line | 15 % → 12 % | 42.2 px | 0.39 | 0.82 | 292 |
| pressure swell | 15 % → 9 % | 58.0 px | 0.36 | 0.57 | 250 |
| fast wave | 48 % → 28 % | 55.7 px | 0.32 | 0.58 | 756 |
| slow wave | 42 % → 28 % | 48.3 px | 0.36 | 0.67 | 1265 |
| spiral | 63 % → 33 % | 41.5 px | 0.37 | 0.53 | 1335 |
| loop | 39 % → 22 % | 50.4 px | 0.35 | 0.55 | 732 |
| tilted | 19 % → 19 % | 53.0 px | 0.33 | 1.01 | 512 |
| over the wet one | 32 % → 28 % | 36.9 px | 0.33 | 0.88 | 262 |
| long, no reload | 61 % → 31 % | 27.3 px | 0.36 | 0.52 | 1717 | quarters: 0.00 → 0.01 → 0.01 → 0.02

Numbers say: light vs heavy: width 30.6 → 42.2 px, dark 0.39 → 0.39; the long stroke does not run out of paint.

## Oil · Henry Ward · Dry scrub
Gouache 1.00 + turpentine 20 % · 90 px · 35.5 s

![Oil · Henry Ward · Dry scrub](Oil-Henry-Ward-Dry-scrub.png)

A light paint: laid on a grey sheet (on white it cannot be seen); **dark** = how far it is from the grey either way.

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 8 % → 0 % | 21.9 px | 0.00 | 0.00 | 230 |
| heavy line | 14 % → 4 % | 40.9 px | 0.36 | 0.26 | 290 |
| pressure swell | 13 % → 2 % | 47.2 px | 0.32 | 0.14 | 210 |
| fast wave | 53 % → 15 % | 61.0 px | 0.28 | 0.28 | 886 |
| slow wave | 34 % → 12 % | 38.9 px | 0.35 | 0.34 | 1327 |
| spiral | 70 % → 5 % | 46.3 px | 0.33 | 0.07 | 1537 |
| loop | 30 % → 2 % | 39.3 px | 0.31 | 0.07 | 764 |
| tilted | 19 % → 19 % | 53.5 px | 0.27 | 1.01 | 498 |
| over the wet one | 25 % → 9 % | 16.9 px | 0.27 | 0.35 | 249 |
| long, no reload | 43 % → 3 % | 19.5 px | 0.34 | 0.07 | 1747 | quarters: 0.04 → 0.03 → 0.04 → 0.05

Numbers say: light vs heavy: width 21.9 → 40.9 px, dark 0.00 → 0.36; the long stroke does not run out of paint.

## Oil · Henry Ward · Dirty contour
Gouache 1.00 + turpentine 35 % · 34 px · 39.7 s

![Oil · Henry Ward · Dirty contour](Oil-Henry-Ward-Dirty-contour.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 11 % → 4 % | 30.7 px | 0.58 | 0.42 | 116 |
| heavy line | 24 % → 16 % | 69.3 px | 0.58 | 0.67 | 199 |
| pressure swell | 15 % → 11 % | 54.9 px | 0.60 | 0.72 | 131 |
| fast wave | 43 % → 19 % | 50.1 px | 0.59 | 0.44 | 536 |
| slow wave | 41 % → 24 % | 47.5 px | 0.57 | 0.58 | 862 |
| spiral | 59 % → 24 % | 39.1 px | 0.55 | 0.41 | 967 |
| loop | 37 % → 23 % | 47.5 px | 0.56 | 0.64 | 431 |
| tilted | 14 % → 14 % | 37.9 px | 0.61 | 1.01 | 219 |
| over the wet one | 32 % → 27 % | 52.1 px | 0.61 | 0.84 | 179 |
| long, no reload | 72 % → 28 % | 32.4 px | 0.58 | 0.39 | 1081 | quarters: 0.53 → 0.50 → 0.42 → 0.33

Numbers say: light vs heavy: width 30.7 → 69.3 px, dark 0.58 → 0.58.

## Oil · Henry Ward · Wet drag
Ink 1.00 + turpentine 65 % · 80 px · 41.4 s

![Oil · Henry Ward · Wet drag](Oil-Henry-Ward-Wet-drag.png)

A light paint: laid on a grey sheet (on white it cannot be seen); **dark** = how far it is from the grey either way.

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 8 % → 0 % | 23.9 px | 0.03 | 0.04 | 155 |
| heavy line | 20 % → 20 % | 58.7 px | 0.06 | 0.98 | 302 |
| pressure swell | 17 % → 12 % | 61.9 px | 0.06 | 0.73 | 231 |
| fast wave | 45 % → 40 % | 52.1 px | 0.06 | 0.89 | 596 |
| slow wave | 55 % → 54 % | 64.0 px | 0.06 | 0.97 | 1105 |
| spiral | 73 % → 63 % | 48.5 px | 0.07 | 0.86 | 1416 |
| loop | 47 % → 43 % | 60.5 px | 0.06 | 0.93 | 615 |
| tilted | 20 % → 20 % | 54.5 px | 0.07 | 1.02 | 420 |
| over the wet one | 32 % → 31 % | 34.7 px | 0.07 | 0.98 | 239 |
| long, no reload | 88 % → 84 % | 39.4 px | 0.06 | 0.96 | 1779 | quarters: 0.05 → 0.06 → 0.06 → 0.05

Numbers say: light vs heavy: width 23.9 → 58.7 px, dark 0.03 → 0.06; the long stroke does not run out of paint.

## Oil · Henry Ward · Thin veil
Watercolour 0.93 · Ink 0.07 + turpentine 80 % · 96 px · 41.4 s

![Oil · Henry Ward · Thin veil](Oil-Henry-Ward-Thin-veil.png)

A light paint: laid on a grey sheet (on white it cannot be seen); **dark** = how far it is from the grey either way.

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 3 % → 4 % | 9.5 px | 0.04 | 1.09 | 252 |
| heavy line | 17 % → 20 % | 50.1 px | 0.10 | 1.13 | 265 |
| pressure swell | 12 % → 14 % | 44.3 px | 0.09 | 1.21 | 244 |
| fast wave | 47 % → 54 % | 54.4 px | 0.10 | 1.14 | 880 |
| slow wave | 48 % → 55 % | 54.9 px | 0.10 | 1.16 | 1471 |
| spiral | 65 % → 70 % | 42.6 px | 0.10 | 1.09 | 1550 |
| loop | 40 % → 48 % | 52.2 px | 0.10 | 1.19 | 745 |
| tilted | 18 % → 19 % | 50.9 px | 0.10 | 1.03 | 540 |
| over the wet one | 28 % → 31 % | 28.0 px | 0.10 | 1.11 | 245 |
| long, no reload | 62 % → 78 % | 27.6 px | 0.09 | 1.26 | 2104 | quarters: 0.09 → 0.09 → 0.07 → 0.05

Numbers say: light vs heavy: width 9.5 → 50.1 px, dark 0.04 → 0.10.

## Oil · Henry Ward · Ground
Ink 0.65 · Watercolour 0.35 + turpentine 75 % · 160 px · 71.9 s

![Oil · Henry Ward · Ground](Oil-Henry-Ward-Ground.png)

A light paint: laid on a grey sheet (on white it cannot be seen); **dark** = how far it is from the grey either way.

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 51 % → 56 % | 148.0 px | 0.06 | 1.10 | 527 |
| heavy line | 53 % → 52 % | 153.8 px | 0.06 | 0.98 | 1242 |
| pressure swell | 41 % → 50 % | 155.4 px | 0.05 | 1.21 | 616 |
| fast wave | 87 % → 93 % | 101.1 px | 0.05 | 1.06 | 2039 |
| slow wave | 88 % → 86 % | 101.4 px | 0.04 | 0.98 | 3541 |
| spiral | 93 % → 92 % | 61.6 px | 0.04 | 0.99 | 3835 |
| loop | 78 % → 78 % | 101.0 px | 0.04 | 1.00 | 1705 |
| tilted | 40 % → 40 % | 110.6 px | 0.05 | 1.01 | 933 |
| over the wet one | 77 % → 79 % | 104.0 px | 0.05 | 1.03 | 926 |
| long, no reload | 99 % → 100 % | 44.6 px | 0.04 | 1.00 | 5881 | quarters: 0.01 → 0.02 → 0.04 → 0.07

Numbers say: light vs heavy: width 148.0 → 153.8 px, dark 0.06 → 0.06; pressure barely changes the width; the long stroke does not run out of paint.

## Oil · Henry Ward · HW #02 cream over wet olive
Watercolour 0.93 · Ink 0.07 + turpentine 80 % · 96 px · 43.7 s

![Oil · Henry Ward · HW #02 cream over wet olive](Oil-Henry-Ward-HW-02-cream-over-wet-olive.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 3 % → 4 % | 9.5 px | 0.03 | 1.09 | 251 |
| heavy line | 17 % → 20 % | 50.1 px | 0.11 | 1.13 | 357 |
| pressure swell | 12 % → 14 % | 44.3 px | 0.13 | 1.21 | 236 |
| fast wave | 47 % → 54 % | 54.4 px | 0.10 | 1.14 | 819 |
| slow wave | 48 % → 55 % | 54.9 px | 0.10 | 1.16 | 1396 |
| spiral | 65 % → 70 % | 42.6 px | 0.10 | 1.09 | 1465 |
| loop | 40 % → 48 % | 52.2 px | 0.08 | 1.19 | 696 |
| tilted | 18 % → 19 % | 50.9 px | 0.15 | 1.03 | 605 |
| over the wet one | 28 % → 31 % | 28.0 px | 0.15 | 1.11 | 349 |
| long, no reload | 62 % → 78 % | 27.6 px | 0.11 | 1.26 | 2148 | quarters: 0.13 → 0.10 → 0.07 → 0.06

Numbers say: light vs heavy: width 9.5 → 50.1 px, dark 0.03 → 0.11.

## Oil · Henry Ward · HW #04 grey arcs over ochre
Gouache 1.00 + turpentine 35 % · 84 px · 44.8 s

![Oil · Henry Ward · HW #04 grey arcs over ochre](Oil-Henry-Ward-HW-04-grey-arcs-over-ochre.png)

A light paint: laid on a grey sheet (on white it cannot be seen); **dark** = how far it is from the grey either way.

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 8 % → 0 % | 24.3 px | 0.00 | 0.00 | 243 |
| heavy line | 19 % → 16 % | 54.3 px | 0.34 | 0.84 | 287 |
| pressure swell | 15 % → 12 % | 55.4 px | 0.29 | 0.83 | 271 |
| fast wave | 47 % → 36 % | 54.9 px | 0.24 | 0.77 | 894 |
| slow wave | 47 % → 28 % | 54.4 px | 0.28 | 0.60 | 1512 |
| spiral | 64 % → 29 % | 42.2 px | 0.24 | 0.46 | 1573 |
| loop | 38 % → 18 % | 49.3 px | 0.25 | 0.47 | 807 |
| tilted | 18 % → 19 % | 51.5 px | 0.23 | 1.00 | 447 |
| over the wet one | 36 % → 26 % | 48.2 px | 0.23 | 0.73 | 298 |
| long, no reload | 61 % → 34 % | 27.4 px | 0.23 | 0.56 | 1874 | quarters: 0.00 → 0.01 → 0.01 → 0.02

Numbers say: light vs heavy: width 24.3 → 54.3 px, dark 0.00 → 0.34; the long stroke does not run out of paint.

## Oil · Henry Ward · HW #09 white arches over wet blue-grey
Gouache 1.00 + turpentine 35 % · 84 px · 44.8 s

![Oil · Henry Ward · HW #09 white arches over wet blue-grey](Oil-Henry-Ward-HW-09-white-arches-over-wet-blue-grey.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 11 % → 3 % | 30.6 px | 0.19 | 0.24 | 210 |
| heavy line | 15 % → 12 % | 42.2 px | 0.26 | 0.82 | 348 |
| pressure swell | 15 % → 9 % | 58.0 px | 0.33 | 0.57 | 190 |
| fast wave | 48 % → 28 % | 55.7 px | 0.37 | 0.58 | 930 |
| slow wave | 42 % → 28 % | 48.3 px | 0.28 | 0.67 | 1550 |
| spiral | 63 % → 33 % | 41.5 px | 0.36 | 0.53 | 1583 |
| loop | 39 % → 22 % | 50.4 px | 0.29 | 0.55 | 715 |
| tilted | 19 % → 19 % | 53.0 px | 0.35 | 1.01 | 436 |
| over the wet one | 32 % → 28 % | 36.9 px | 0.35 | 0.88 | 410 |
| long, no reload | 61 % → 31 % | 27.3 px | 0.36 | 0.52 | 2408 | quarters: 0.31 → 0.20 → 0.14 → 0.10

Numbers say: light vs heavy: width 30.6 → 42.2 px, dark 0.19 → 0.26.

## Oil · Henry Ward · HW #03 navy contours over wet band
Gouache 1.00 + turpentine 35 % · 84 px · 44.7 s

![Oil · Henry Ward · HW #03 navy contours over wet band](Oil-Henry-Ward-HW-03-navy-contours-over-wet-band.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 11 % → 3 % | 30.6 px | 0.21 | 0.24 | 279 |
| heavy line | 15 % → 12 % | 42.2 px | 0.27 | 0.82 | 261 |
| pressure swell | 15 % → 9 % | 58.0 px | 0.35 | 0.57 | 236 |
| fast wave | 48 % → 28 % | 55.7 px | 0.39 | 0.58 | 754 |
| slow wave | 42 % → 28 % | 48.3 px | 0.30 | 0.67 | 1279 |
| spiral | 63 % → 33 % | 41.5 px | 0.37 | 0.53 | 1555 |
| loop | 39 % → 22 % | 50.4 px | 0.30 | 0.55 | 783 |
| tilted | 19 % → 19 % | 53.0 px | 0.37 | 1.01 | 558 |
| over the wet one | 32 % → 28 % | 36.9 px | 0.37 | 0.88 | 258 |
| long, no reload | 61 % → 31 % | 27.3 px | 0.38 | 0.52 | 1686 | quarters: 0.32 → 0.21 → 0.15 → 0.10

Numbers say: light vs heavy: width 30.6 → 42.2 px, dark 0.21 → 0.27.

## Oil · Henry Ward · HW #01 peach cloud and legs over teal
Gouache 1.00 + turpentine 35 % · 84 px · 47.8 s

![Oil · Henry Ward · HW #01 peach cloud and legs over teal](Oil-Henry-Ward-HW-01-peach-cloud-and-legs-over-teal.png)

A light paint: laid on a grey sheet (on white it cannot be seen); **dark** = how far it is from the grey either way.

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 8 % → 0 % | 24.3 px | 0.00 | 0.00 | 221 |
| heavy line | 19 % → 16 % | 54.3 px | 0.34 | 0.84 | 389 |
| pressure swell | 15 % → 12 % | 55.4 px | 0.30 | 0.83 | 219 |
| fast wave | 47 % → 36 % | 54.9 px | 0.25 | 0.77 | 906 |
| slow wave | 47 % → 28 % | 54.4 px | 0.28 | 0.60 | 1472 |
| spiral | 64 % → 29 % | 42.2 px | 0.24 | 0.46 | 1547 |
| loop | 38 % → 18 % | 49.3 px | 0.26 | 0.47 | 872 |
| tilted | 18 % → 19 % | 51.5 px | 0.24 | 1.00 | 487 |
| over the wet one | 36 % → 26 % | 48.2 px | 0.24 | 0.73 | 293 |
| long, no reload | 61 % → 34 % | 27.4 px | 0.24 | 0.56 | 1957 | quarters: 0.00 → 0.01 → 0.01 → 0.02

Numbers say: light vs heavy: width 24.3 → 54.3 px, dark 0.00 → 0.34; the long stroke does not run out of paint.

## Oil · Henry Ward · HW #05 rust, pink, green-black
Gouache 1.00 + turpentine 35 % · 84 px · 46.8 s

![Oil · Henry Ward · HW #05 rust, pink, green-black](Oil-Henry-Ward-HW-05-rust-pink-green-black.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 11 % → 3 % | 30.6 px | 0.37 | 0.24 | 222 |
| heavy line | 15 % → 12 % | 42.2 px | 0.44 | 0.82 | 273 |
| pressure swell | 15 % → 9 % | 58.0 px | 0.50 | 0.57 | 213 |
| fast wave | 48 % → 28 % | 55.7 px | 0.53 | 0.58 | 803 |
| slow wave | 42 % → 28 % | 48.3 px | 0.46 | 0.67 | 1445 |
| spiral | 63 % → 33 % | 41.5 px | 0.53 | 0.53 | 1576 |
| loop | 39 % → 22 % | 50.4 px | 0.47 | 0.55 | 660 |
| tilted | 19 % → 19 % | 53.0 px | 0.51 | 1.01 | 459 |
| over the wet one | 32 % → 28 % | 36.9 px | 0.51 | 0.88 | 316 |
| long, no reload | 61 % → 31 % | 27.3 px | 0.54 | 0.52 | 1729 | quarters: 0.46 → 0.33 → 0.27 → 0.19

Numbers say: light vs heavy: width 30.6 → 42.2 px, dark 0.37 → 0.44.

## Oil · Henry Ward · HW #07 blue L and zigzag on lilac
Gouache 1.00 + turpentine 20 % · 90 px · 37.9 s

![Oil · Henry Ward · HW #07 blue L and zigzag on lilac](Oil-Henry-Ward-HW-07-blue-L-and-zigzag-on-lilac.png)

A light paint: laid on a grey sheet (on white it cannot be seen); **dark** = how far it is from the grey either way.

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 8 % → 0 % | 23.4 px | 0.00 | 0.00 | 273 |
| heavy line | 17 % → 5 % | 49.3 px | 0.38 | 0.27 | 320 |
| pressure swell | 15 % → 5 % | 55.6 px | 0.36 | 0.33 | 264 |
| fast wave | 51 % → 8 % | 59.4 px | 0.32 | 0.16 | 1026 |
| slow wave | 40 % → 7 % | 45.7 px | 0.34 | 0.19 | 1556 |
| spiral | 68 % → 8 % | 44.5 px | 0.29 | 0.12 | 1728 |
| loop | 34 % → 1 % | 43.6 px | 0.29 | 0.03 | 632 |
| tilted | 18 % → 19 % | 51.6 px | 0.30 | 1.00 | 481 |
| over the wet one | 27 % → 6 % | 24.7 px | 0.30 | 0.23 | 267 |
| long, no reload | 52 % → 8 % | 23.4 px | 0.29 | 0.14 | 1775 | quarters: 0.04 → 0.02 → 0.03 → 0.05

Numbers say: light vs heavy: width 23.4 → 49.3 px, dark 0.00 → 0.38; the long stroke does not run out of paint.

## Oil · Henry Ward · HW #08 crown and dark oval
Gouache 1.00 + turpentine 35 % · 84 px · 51.2 s

![Oil · Henry Ward · HW #08 crown and dark oval](Oil-Henry-Ward-HW-08-crown-and-dark-oval.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 22 % → 2 % | 63.8 px | 0.10 | 0.08 | 302 |
| heavy line | 31 % → 15 % | 91.2 px | 0.13 | 0.48 | 546 |
| pressure swell | 25 % → 11 % | 94.1 px | 0.18 | 0.44 | 295 |
| fast wave | 66 % → 37 % | 76.2 px | 0.24 | 0.56 | 1083 |
| slow wave | 56 % → 32 % | 65.1 px | 0.15 | 0.57 | 2078 |
| spiral | 67 % → 30 % | 44.1 px | 0.22 | 0.44 | 1826 |
| loop | 50 % → 25 % | 65.1 px | 0.13 | 0.51 | 928 |
| tilted | 22 % → 22 % | 62.6 px | 0.21 | 1.00 | 480 |
| over the wet one | 49 % → 35 % | 74.9 px | 0.21 | 0.71 | 557 |
| long, no reload | 90 % → 44 % | 40.3 px | 0.25 | 0.49 | 2458 | quarters: 0.23 → 0.22 → 0.13 → 0.07

Numbers say: light vs heavy: width 63.8 → 91.2 px, dark 0.10 → 0.13.

## Oil · Henry Ward · HW #10 green block over maroon
Gouache 1.00 + turpentine 35 % · 84 px · 50.4 s

![Oil · Henry Ward · HW #10 green block over maroon](Oil-Henry-Ward-HW-10-green-block-over-maroon.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 22 % → 2 % | 63.8 px | 0.08 | 0.08 | 277 |
| heavy line | 31 % → 15 % | 91.2 px | 0.11 | 0.48 | 539 |
| pressure swell | 25 % → 11 % | 94.1 px | 0.16 | 0.44 | 284 |
| fast wave | 66 % → 37 % | 76.2 px | 0.21 | 0.56 | 1136 |
| slow wave | 56 % → 32 % | 65.1 px | 0.13 | 0.57 | 1992 |
| spiral | 67 % → 30 % | 44.1 px | 0.20 | 0.44 | 1833 |
| loop | 50 % → 25 % | 65.1 px | 0.12 | 0.51 | 970 |
| tilted | 22 % → 22 % | 62.6 px | 0.19 | 1.00 | 497 |
| over the wet one | 49 % → 35 % | 74.9 px | 0.19 | 0.71 | 518 |
| long, no reload | 90 % → 44 % | 40.3 px | 0.22 | 0.49 | 2773 | quarters: 0.21 → 0.20 → 0.12 → 0.07

Numbers say: light vs heavy: width 63.8 → 91.2 px, dark 0.08 → 0.11.

## Oil · Henry Ward · HW #11 cream mass and purple balls
Gouache 1.00 + turpentine 35 % · 84 px · 45.9 s

![Oil · Henry Ward · HW #11 cream mass and purple balls](Oil-Henry-Ward-HW-11-cream-mass-and-purple-balls.png)

A light paint: laid on a grey sheet (on white it cannot be seen); **dark** = how far it is from the grey either way.

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 11 % → 3 % | 30.6 px | 0.42 | 0.24 | 207 |
| heavy line | 15 % → 12 % | 42.2 px | 0.40 | 0.82 | 321 |
| pressure swell | 15 % → 9 % | 58.0 px | 0.31 | 0.57 | 218 |
| fast wave | 48 % → 28 % | 55.7 px | 0.28 | 0.58 | 741 |
| slow wave | 42 % → 28 % | 48.3 px | 0.34 | 0.67 | 1249 |
| spiral | 63 % → 33 % | 41.5 px | 0.28 | 0.53 | 1655 |
| loop | 39 % → 22 % | 50.4 px | 0.32 | 0.55 | 765 |
| tilted | 19 % → 19 % | 53.0 px | 0.30 | 1.01 | 477 |
| over the wet one | 32 % → 28 % | 36.9 px | 0.30 | 0.88 | 309 |
| long, no reload | 61 % → 31 % | 27.3 px | 0.28 | 0.52 | 1703 | quarters: 0.00 → 0.01 → 0.01 → 0.02

Numbers say: light vs heavy: width 30.6 → 42.2 px, dark 0.42 → 0.40; the long stroke does not run out of paint.

## Oil · Henry Ward · HW #13 blue scrub under red
Gouache 1.00 + turpentine 35 % · 84 px · 46.7 s

![Oil · Henry Ward · HW #13 blue scrub under red](Oil-Henry-Ward-HW-13-blue-scrub-under-red.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 8 % → 0 % | 24.3 px | 0.00 | 0.00 | 211 |
| heavy line | 19 % → 16 % | 54.3 px | 0.50 | 0.84 | 335 |
| pressure swell | 15 % → 12 % | 55.4 px | 0.52 | 0.83 | 213 |
| fast wave | 47 % → 36 % | 54.9 px | 0.56 | 0.77 | 1088 |
| slow wave | 47 % → 28 % | 54.4 px | 0.54 | 0.60 | 1564 |
| spiral | 64 % → 29 % | 42.2 px | 0.57 | 0.46 | 1824 |
| loop | 38 % → 18 % | 49.3 px | 0.55 | 0.47 | 836 |
| tilted | 18 % → 19 % | 51.5 px | 0.57 | 1.00 | 442 |
| over the wet one | 36 % → 26 % | 48.2 px | 0.57 | 0.73 | 397 |
| long, no reload | 61 % → 34 % | 27.4 px | 0.57 | 0.56 | 1715 | quarters: 0.50 → 0.40 → 0.31 → 0.15

Numbers say: light vs heavy: width 24.3 → 54.3 px, dark 0.00 → 0.50.

## Oil · Henry Ward · HW #14 olive totem on dark
Gouache 1.00 + turpentine 35 % · 84 px · 51.5 s

![Oil · Henry Ward · HW #14 olive totem on dark](Oil-Henry-Ward-HW-14-olive-totem-on-dark.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 22 % → 2 % | 63.8 px | 0.15 | 0.08 | 367 |
| heavy line | 31 % → 15 % | 91.2 px | 0.18 | 0.48 | 410 |
| pressure swell | 25 % → 11 % | 94.1 px | 0.23 | 0.44 | 420 |
| fast wave | 66 % → 37 % | 76.2 px | 0.29 | 0.56 | 1160 |
| slow wave | 56 % → 32 % | 65.1 px | 0.20 | 0.57 | 1910 |
| spiral | 67 % → 30 % | 44.1 px | 0.27 | 0.44 | 1977 |
| loop | 50 % → 25 % | 65.1 px | 0.19 | 0.51 | 1120 |
| tilted | 22 % → 22 % | 62.6 px | 0.26 | 1.00 | 457 |
| over the wet one | 49 % → 35 % | 74.9 px | 0.26 | 0.71 | 454 |
| long, no reload | 90 % → 44 % | 40.3 px | 0.30 | 0.49 | 2611 | quarters: 0.28 → 0.27 → 0.17 → 0.09

Numbers say: light vs heavy: width 63.8 → 91.2 px, dark 0.15 → 0.18.

## Oil · Henry Ward · Ground #2b2f1c flat
Ink 0.65 · Watercolour 0.35 + turpentine 75 % · 160 px · 72.9 s

![Oil · Henry Ward · Ground #2b2f1c flat](Oil-Henry-Ward-Ground-2b2f1c-flat.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 51 % → 56 % | 148.0 px | 0.47 | 1.10 | 530 |
| heavy line | 53 % → 52 % | 153.8 px | 0.52 | 0.98 | 1039 |
| pressure swell | 41 % → 50 % | 155.4 px | 0.53 | 1.21 | 631 |
| fast wave | 87 % → 93 % | 101.1 px | 0.57 | 1.06 | 2510 |
| slow wave | 88 % → 86 % | 101.4 px | 0.60 | 0.98 | 4551 |
| spiral | 93 % → 92 % | 61.6 px | 0.57 | 0.99 | 3629 |
| loop | 78 % → 78 % | 101.0 px | 0.58 | 1.00 | 1811 |
| tilted | 40 % → 40 % | 110.6 px | 0.56 | 1.01 | 1179 |
| over the wet one | 77 % → 79 % | 104.0 px | 0.56 | 1.03 | 711 |
| long, no reload | 99 % → 100 % | 44.6 px | 0.60 | 1.00 | 5118 | quarters: 0.72 → 0.68 → 0.60 → 0.45

Numbers say: light vs heavy: width 148.0 → 153.8 px, dark 0.47 → 0.52; pressure barely changes the width.

## Oil · Henry Ward · Thin veil #2b3a44 flat
Watercolour 0.93 · Ink 0.07 + turpentine 80 % · 96 px · 45.2 s

![Oil · Henry Ward · Thin veil #2b3a44 flat](Oil-Henry-Ward-Thin-veil-2b3a44-flat.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 3 % → 4 % | 9.5 px | 0.03 | 1.09 | 191 |
| heavy line | 17 % → 20 % | 50.1 px | 0.11 | 1.13 | 283 |
| pressure swell | 12 % → 14 % | 44.3 px | 0.13 | 1.21 | 325 |
| fast wave | 47 % → 54 % | 54.4 px | 0.10 | 1.14 | 892 |
| slow wave | 48 % → 55 % | 54.9 px | 0.10 | 1.16 | 1575 |
| spiral | 65 % → 70 % | 42.6 px | 0.10 | 1.09 | 1603 |
| loop | 40 % → 48 % | 52.2 px | 0.08 | 1.19 | 658 |
| tilted | 18 % → 19 % | 50.9 px | 0.15 | 1.03 | 571 |
| over the wet one | 28 % → 31 % | 28.0 px | 0.15 | 1.11 | 286 |
| long, no reload | 62 % → 78 % | 27.6 px | 0.11 | 1.26 | 2236 | quarters: 0.13 → 0.10 → 0.07 → 0.06

Numbers say: light vs heavy: width 9.5 → 50.1 px, dark 0.03 → 0.11.

## Oil · Henry Ward · Loaded flat #ece6c0 flat
Gouache 1.00 + turpentine 30 % · 84 px · 46.5 s

![Oil · Henry Ward · Loaded flat #ece6c0 flat](Oil-Henry-Ward-Loaded-flat-ece6c0-flat.png)

A light paint: laid on a grey sheet (on white it cannot be seen); **dark** = how far it is from the grey either way.

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 11 % → 3 % | 30.7 px | 0.43 | 0.24 | 196 |
| heavy line | 15 % → 12 % | 42.2 px | 0.42 | 0.83 | 523 |
| pressure swell | 15 % → 9 % | 58.1 px | 0.33 | 0.58 | 209 |
| fast wave | 48 % → 29 % | 55.7 px | 0.30 | 0.61 | 776 |
| slow wave | 42 % → 28 % | 48.3 px | 0.37 | 0.68 | 1320 |
| spiral | 63 % → 34 % | 41.5 px | 0.31 | 0.54 | 1485 |
| loop | 39 % → 22 % | 50.7 px | 0.34 | 0.57 | 643 |
| tilted | 19 % → 19 % | 53.1 px | 0.33 | 1.00 | 441 |
| over the wet one | 32 % → 28 % | 36.9 px | 0.33 | 0.88 | 305 |
| long, no reload | 61 % → 32 % | 27.3 px | 0.30 | 0.53 | 1486 | quarters: 0.00 → 0.01 → 0.02 → 0.02

Numbers say: light vs heavy: width 30.7 → 42.2 px, dark 0.43 → 0.42; the long stroke does not run out of paint.

## Oil · Henry Ward · Dry scrub #ece6c0 filbert
Gouache 1.00 + turpentine 20 % · 90 px · 38.2 s

![Oil · Henry Ward · Dry scrub #ece6c0 filbert](Oil-Henry-Ward-Dry-scrub-ece6c0-filbert.png)

A light paint: laid on a grey sheet (on white it cannot be seen); **dark** = how far it is from the grey either way.

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 8 % → 0 % | 23.4 px | 0.00 | 0.00 | 282 |
| heavy line | 17 % → 5 % | 49.3 px | 0.37 | 0.27 | 339 |
| pressure swell | 15 % → 5 % | 55.6 px | 0.35 | 0.33 | 219 |
| fast wave | 51 % → 8 % | 59.4 px | 0.30 | 0.16 | 886 |
| slow wave | 40 % → 7 % | 45.7 px | 0.33 | 0.19 | 1383 |
| spiral | 68 % → 8 % | 44.5 px | 0.27 | 0.12 | 1449 |
| loop | 34 % → 1 % | 43.6 px | 0.28 | 0.03 | 691 |
| tilted | 18 % → 19 % | 51.6 px | 0.28 | 1.00 | 563 |
| over the wet one | 27 % → 6 % | 24.7 px | 0.28 | 0.23 | 299 |
| long, no reload | 52 % → 8 % | 23.4 px | 0.27 | 0.14 | 1801 | quarters: 0.04 → 0.02 → 0.03 → 0.05

Numbers say: light vs heavy: width 23.4 → 49.3 px, dark 0.00 → 0.37; the long stroke does not run out of paint.

## Oil · Henry Ward · Ground #8a6a20 flat
Ink 0.65 · Watercolour 0.35 + turpentine 75 % · 160 px · 70.8 s

![Oil · Henry Ward · Ground #8a6a20 flat](Oil-Henry-Ward-Ground-8a6a20-flat.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 51 % → 56 % | 148.0 px | 0.17 | 1.10 | 557 |
| heavy line | 53 % → 52 % | 153.8 px | 0.18 | 0.98 | 907 |
| pressure swell | 41 % → 50 % | 155.4 px | 0.19 | 1.21 | 710 |
| fast wave | 87 % → 93 % | 101.1 px | 0.21 | 1.06 | 2348 |
| slow wave | 88 % → 86 % | 101.4 px | 0.23 | 0.98 | 3370 |
| spiral | 93 % → 92 % | 61.6 px | 0.23 | 0.99 | 4415 |
| loop | 78 % → 78 % | 101.0 px | 0.22 | 1.00 | 2206 |
| tilted | 40 % → 40 % | 110.6 px | 0.22 | 1.01 | 1315 |
| over the wet one | 77 % → 79 % | 104.0 px | 0.22 | 1.03 | 1121 |
| long, no reload | 99 % → 100 % | 44.6 px | 0.23 | 1.00 | 5638 | quarters: 0.30 → 0.27 → 0.21 → 0.16

Numbers say: light vs heavy: width 148.0 → 153.8 px, dark 0.17 → 0.18; pressure barely changes the width.

## Oil · Henry Ward · Loaded flat #b8bcc0 filbert
Gouache 1.00 + turpentine 35 % · 84 px · 44.0 s

![Oil · Henry Ward · Loaded flat #b8bcc0 filbert](Oil-Henry-Ward-Loaded-flat-b8bcc0-filbert.png)

A light paint: laid on a grey sheet (on white it cannot be seen); **dark** = how far it is from the grey either way.

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 8 % → 0 % | 24.3 px | 0.00 | 0.00 | 256 |
| heavy line | 19 % → 16 % | 54.3 px | 0.34 | 0.84 | 375 |
| pressure swell | 15 % → 12 % | 55.4 px | 0.29 | 0.83 | 236 |
| fast wave | 47 % → 36 % | 54.9 px | 0.24 | 0.77 | 796 |
| slow wave | 47 % → 28 % | 54.4 px | 0.28 | 0.60 | 1739 |
| spiral | 64 % → 29 % | 42.2 px | 0.24 | 0.46 | 2006 |
| loop | 38 % → 18 % | 49.3 px | 0.25 | 0.47 | 1346 |
| tilted | 18 % → 19 % | 51.5 px | 0.23 | 1.00 | 370 |
| over the wet one | 36 % → 26 % | 48.2 px | 0.23 | 0.73 | 297 |
| long, no reload | 61 % → 34 % | 27.4 px | 0.23 | 0.56 | 2407 | quarters: 0.00 → 0.01 → 0.01 → 0.02

Numbers say: light vs heavy: width 24.3 → 54.3 px, dark 0.00 → 0.34; the long stroke does not run out of paint.

## Oil · Henry Ward · Dry scrub #c8ccd0 worn
Gouache 1.00 + turpentine 20 % · 90 px · 35.6 s

![Oil · Henry Ward · Dry scrub #c8ccd0 worn](Oil-Henry-Ward-Dry-scrub-c8ccd0-worn.png)

A light paint: laid on a grey sheet (on white it cannot be seen); **dark** = how far it is from the grey either way.

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 17 % → 0 % | 48.2 px | 0.00 | 0.00 | 280 |
| heavy line | 30 % → 0 % | 85.8 px | 0.28 | 0.01 | 456 |
| pressure swell | 21 % → 6 % | 77.1 px | 0.29 | 0.28 | 645 |
| fast wave | 68 % → 7 % | 78.5 px | 0.21 | 0.10 | 1396 |
| slow wave | 51 % → 4 % | 58.7 px | 0.26 | 0.07 | 2347 |
| spiral | 72 % → 9 % | 47.6 px | 0.22 | 0.13 | 1857 |
| loop | 51 % → 1 % | 66.3 px | 0.25 | 0.01 | 1281 |
| tilted | 20 % → 20 % | 56.8 px | 0.21 | 1.00 | 575 |
| over the wet one | 41 % → 7 % | 56.6 px | 0.21 | 0.16 | 590 |
| long, no reload | 79 % → 0 % | 35.4 px | 0.17 | 0.00 | 2318 | quarters: 0.01 → 0.01 → 0.01 → 0.02

Numbers say: light vs heavy: width 48.2 → 85.8 px, dark 0.00 → 0.28; the long stroke does not run out of paint.

## Oil · Henry Ward · Wet drag #9ea4aa flat
Ink 1.00 + turpentine 65 % · 80 px · 43.0 s

![Oil · Henry Ward · Wet drag #9ea4aa flat](Oil-Henry-Ward-Wet-drag-9ea4aa-flat.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 8 % → 0 % | 23.9 px | 0.03 | 0.04 | 158 |
| heavy line | 20 % → 20 % | 58.7 px | 0.07 | 0.98 | 363 |
| pressure swell | 17 % → 12 % | 61.9 px | 0.06 | 0.73 | 312 |
| fast wave | 45 % → 40 % | 52.1 px | 0.07 | 0.89 | 731 |
| slow wave | 55 % → 54 % | 64.0 px | 0.07 | 0.97 | 1744 |
| spiral | 73 % → 63 % | 48.5 px | 0.07 | 0.86 | 2040 |
| loop | 47 % → 43 % | 60.5 px | 0.07 | 0.93 | 533 |
| tilted | 20 % → 20 % | 54.5 px | 0.09 | 1.02 | 578 |
| over the wet one | 32 % → 31 % | 34.7 px | 0.09 | 0.98 | 252 |
| long, no reload | 88 % → 84 % | 39.4 px | 0.07 | 0.96 | 2394 | quarters: 0.08 → 0.08 → 0.06 → 0.05

Numbers say: light vs heavy: width 23.9 → 58.7 px, dark 0.03 → 0.07.

## Oil · Henry Ward · Ground #e8b4a8 flat
Ink 0.65 · Watercolour 0.35 + turpentine 75 % · 160 px · 71.5 s

![Oil · Henry Ward · Ground #e8b4a8 flat](Oil-Henry-Ward-Ground-e8b4a8-flat.png)

A light paint: laid on a grey sheet (on white it cannot be seen); **dark** = how far it is from the grey either way.

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 51 % → 56 % | 148.0 px | 0.06 | 1.10 | 595 |
| heavy line | 53 % → 52 % | 153.8 px | 0.05 | 0.98 | 1570 |
| pressure swell | 41 % → 50 % | 155.4 px | 0.05 | 1.21 | 585 |
| fast wave | 87 % → 93 % | 101.1 px | 0.04 | 1.06 | 2841 |
| slow wave | 88 % → 86 % | 101.4 px | 0.04 | 0.98 | 4345 |
| spiral | 93 % → 92 % | 61.6 px | 0.04 | 0.99 | 3247 |
| loop | 78 % → 78 % | 101.0 px | 0.04 | 1.00 | 1535 |
| tilted | 40 % → 40 % | 110.6 px | 0.04 | 1.01 | 953 |
| over the wet one | 77 % → 79 % | 104.0 px | 0.04 | 1.03 | 808 |
| long, no reload | 99 % → 100 % | 44.6 px | 0.04 | 1.00 | 5123 | quarters: 0.00 → 0.01 → 0.04 → 0.06

Numbers say: light vs heavy: width 148.0 → 153.8 px, dark 0.06 → 0.05; pressure barely changes the width; the long stroke does not run out of paint.

## Oil · Henry Ward · Loaded flat #6e7f90 flat
Gouache 1.00 + turpentine 35 % · 84 px · 44.6 s

![Oil · Henry Ward · Loaded flat #6e7f90 flat](Oil-Henry-Ward-Loaded-flat-6e7f90-flat.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 11 % → 3 % | 30.6 px | 0.19 | 0.24 | 350 |
| heavy line | 15 % → 12 % | 42.2 px | 0.26 | 0.82 | 482 |
| pressure swell | 15 % → 9 % | 58.0 px | 0.33 | 0.57 | 313 |
| fast wave | 48 % → 28 % | 55.7 px | 0.37 | 0.58 | 979 |
| slow wave | 42 % → 28 % | 48.3 px | 0.28 | 0.67 | 1505 |
| spiral | 63 % → 33 % | 41.5 px | 0.36 | 0.53 | 1308 |
| loop | 39 % → 22 % | 50.4 px | 0.29 | 0.55 | 638 |
| tilted | 19 % → 19 % | 53.0 px | 0.35 | 1.01 | 403 |
| over the wet one | 32 % → 28 % | 36.9 px | 0.35 | 0.88 | 265 |
| long, no reload | 61 % → 31 % | 27.3 px | 0.36 | 0.52 | 1462 | quarters: 0.31 → 0.20 → 0.14 → 0.10

Numbers say: light vs heavy: width 30.6 → 42.2 px, dark 0.19 → 0.26.

## Oil · Henry Ward · Loaded flat #f6f6f2 filbert
Gouache 1.00 + turpentine 30 % · 84 px · 44.1 s

![Oil · Henry Ward · Loaded flat #f6f6f2 filbert](Oil-Henry-Ward-Loaded-flat-f6f6f2-filbert.png)

A light paint: laid on a grey sheet (on white it cannot be seen); **dark** = how far it is from the grey either way.

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 8 % → 0 % | 24.4 px | 0.00 | 0.00 | 248 |
| heavy line | 19 % → 16 % | 54.2 px | 0.43 | 0.84 | 322 |
| pressure swell | 15 % → 12 % | 55.2 px | 0.38 | 0.84 | 220 |
| fast wave | 48 % → 38 % | 54.9 px | 0.35 | 0.79 | 828 |
| slow wave | 47 % → 29 % | 54.3 px | 0.37 | 0.61 | 1369 |
| spiral | 64 % → 30 % | 42.3 px | 0.34 | 0.46 | 1533 |
| loop | 38 % → 19 % | 49.6 px | 0.35 | 0.49 | 700 |
| tilted | 18 % → 19 % | 51.6 px | 0.35 | 1.00 | 397 |
| over the wet one | 36 % → 26 % | 48.4 px | 0.35 | 0.74 | 308 |
| long, no reload | 61 % → 35 % | 27.3 px | 0.34 | 0.57 | 1756 | quarters: 0.00 → 0.01 → 0.02 → 0.03

Numbers say: light vs heavy: width 24.4 → 54.2 px, dark 0.00 → 0.43; the long stroke does not run out of paint.

## Oil · Henry Ward · Dry scrub #f6f6f2 filbert
Gouache 1.00 + turpentine 20 % · 90 px · 36.7 s

![Oil · Henry Ward · Dry scrub #f6f6f2 filbert](Oil-Henry-Ward-Dry-scrub-f6f6f2-filbert.png)

A light paint: laid on a grey sheet (on white it cannot be seen); **dark** = how far it is from the grey either way.

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 8 % → 0 % | 23.4 px | 0.00 | 0.00 | 233 |
| heavy line | 17 % → 5 % | 49.3 px | 0.38 | 0.27 | 302 |
| pressure swell | 15 % → 5 % | 55.6 px | 0.36 | 0.33 | 218 |
| fast wave | 51 % → 8 % | 59.4 px | 0.32 | 0.16 | 853 |
| slow wave | 40 % → 7 % | 45.7 px | 0.34 | 0.19 | 1516 |
| spiral | 68 % → 8 % | 44.5 px | 0.30 | 0.12 | 1320 |
| loop | 34 % → 1 % | 43.6 px | 0.30 | 0.03 | 673 |
| tilted | 18 % → 19 % | 51.6 px | 0.30 | 1.00 | 401 |
| over the wet one | 27 % → 6 % | 24.7 px | 0.30 | 0.23 | 330 |
| long, no reload | 52 % → 8 % | 23.4 px | 0.30 | 0.14 | 1746 | quarters: 0.04 → 0.02 → 0.03 → 0.05

Numbers say: light vs heavy: width 23.4 → 49.3 px, dark 0.00 → 0.38; the long stroke does not run out of paint.

## Oil · Henry Ward · Ground #e8e2da flat
Gouache 1.00 + turpentine 30 % · 160 px · 77.9 s

![Oil · Henry Ward · Ground #e8e2da flat](Oil-Henry-Ward-Ground-e8e2da-flat.png)

A light paint: laid on a grey sheet (on white it cannot be seen); **dark** = how far it is from the grey either way.

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 51 % → 43 % | 148.1 px | 0.37 | 0.84 | 764 |
| heavy line | 52 % → 45 % | 151.1 px | 0.37 | 0.87 | 935 |
| pressure swell | 41 % → 43 % | 154.5 px | 0.36 | 1.04 | 597 |
| fast wave | 85 % → 83 % | 97.9 px | 0.36 | 0.98 | 2445 |
| slow wave | 86 % → 70 % | 99.3 px | 0.37 | 0.81 | 3908 |
| spiral | 89 % → 64 % | 58.5 px | 0.36 | 0.72 | 5119 |
| loop | 75 % → 67 % | 97.0 px | 0.37 | 0.89 | 2703 |
| tilted | 38 % → 38 % | 107.0 px | 0.37 | 1.00 | 1145 |
| over the wet one | 76 % → 69 % | 104.8 px | 0.37 | 0.90 | 955 |
| long, no reload | 99 % → 85 % | 44.3 px | 0.36 | 0.86 | 5727 | quarters: 0.00 → 0.00 → 0.00 → 0.00

Numbers say: light vs heavy: width 148.1 → 151.1 px, dark 0.37 → 0.37; pressure barely changes the width.

## Oil · Henry Ward · Loaded flat #6a7a80 flat
Gouache 1.00 + turpentine 35 % · 84 px · 45.8 s

![Oil · Henry Ward · Loaded flat #6a7a80 flat](Oil-Henry-Ward-Loaded-flat-6a7a80-flat.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 11 % → 3 % | 30.6 px | 0.21 | 0.24 | 204 |
| heavy line | 15 % → 12 % | 42.2 px | 0.27 | 0.82 | 269 |
| pressure swell | 15 % → 9 % | 58.0 px | 0.35 | 0.57 | 233 |
| fast wave | 48 % → 28 % | 55.7 px | 0.39 | 0.58 | 775 |
| slow wave | 42 % → 28 % | 48.3 px | 0.30 | 0.67 | 1442 |
| spiral | 63 % → 33 % | 41.5 px | 0.37 | 0.53 | 1700 |
| loop | 39 % → 22 % | 50.4 px | 0.30 | 0.55 | 1068 |
| tilted | 19 % → 19 % | 53.0 px | 0.37 | 1.01 | 468 |
| over the wet one | 32 % → 28 % | 36.9 px | 0.37 | 0.88 | 347 |
| long, no reload | 61 % → 31 % | 27.3 px | 0.38 | 0.52 | 1884 | quarters: 0.32 → 0.21 → 0.15 → 0.10

Numbers say: light vs heavy: width 30.6 → 42.2 px, dark 0.21 → 0.27.

## Oil · Henry Ward · Loaded flat #5a1810 flat
Gouache 1.00 + turpentine 35 % · 84 px · 45.5 s

![Oil · Henry Ward · Loaded flat #5a1810 flat](Oil-Henry-Ward-Loaded-flat-5a1810-flat.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 11 % → 3 % | 30.6 px | 0.53 | 0.24 | 194 |
| heavy line | 15 % → 12 % | 42.2 px | 0.59 | 0.82 | 276 |
| pressure swell | 15 % → 9 % | 58.0 px | 0.61 | 0.57 | 203 |
| fast wave | 48 % → 28 % | 55.7 px | 0.64 | 0.58 | 690 |
| slow wave | 42 % → 28 % | 48.3 px | 0.60 | 0.67 | 1461 |
| spiral | 63 % → 33 % | 41.5 px | 0.63 | 0.53 | 2416 |
| loop | 39 % → 22 % | 50.4 px | 0.60 | 0.55 | 887 |
| tilted | 19 % → 19 % | 53.0 px | 0.63 | 1.01 | 465 |
| over the wet one | 32 % → 28 % | 36.9 px | 0.63 | 0.88 | 515 |
| long, no reload | 61 % → 31 % | 27.3 px | 0.64 | 0.52 | 1715 | quarters: 0.56 → 0.42 → 0.34 → 0.24

Numbers say: light vs heavy: width 30.6 → 42.2 px, dark 0.53 → 0.59.

## Oil · Henry Ward · Dirty contour #1c2240 flat
Gouache 1.00 + turpentine 35 % · 34 px · 41.1 s

![Oil · Henry Ward · Dirty contour #1c2240 flat](Oil-Henry-Ward-Dirty-contour-1c2240-flat.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 11 % → 4 % | 30.7 px | 0.53 | 0.42 | 82 |
| heavy line | 24 % → 16 % | 69.3 px | 0.54 | 0.67 | 204 |
| pressure swell | 15 % → 11 % | 54.9 px | 0.58 | 0.72 | 176 |
| fast wave | 43 % → 19 % | 50.1 px | 0.63 | 0.44 | 571 |
| slow wave | 41 % → 24 % | 47.5 px | 0.59 | 0.58 | 990 |
| spiral | 59 % → 24 % | 39.1 px | 0.60 | 0.41 | 861 |
| loop | 37 % → 23 % | 47.5 px | 0.57 | 0.64 | 769 |
| tilted | 14 % → 14 % | 37.9 px | 0.63 | 1.01 | 174 |
| over the wet one | 32 % → 27 % | 52.1 px | 0.63 | 0.84 | 200 |
| long, no reload | 72 % → 28 % | 32.4 px | 0.62 | 0.39 | 1187 | quarters: 0.57 → 0.54 → 0.46 → 0.37

Numbers say: light vs heavy: width 30.7 → 69.3 px, dark 0.53 → 0.54.

## Oil · Henry Ward · Ground #22403f flat
Ink 0.65 · Watercolour 0.35 + turpentine 75 % · 160 px · 72.9 s

![Oil · Henry Ward · Ground #22403f flat](Oil-Henry-Ward-Ground-22403f-flat.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 51 % → 56 % | 148.0 px | 0.37 | 1.10 | 643 |
| heavy line | 53 % → 52 % | 153.8 px | 0.41 | 0.98 | 1235 |
| pressure swell | 41 % → 50 % | 155.4 px | 0.42 | 1.21 | 751 |
| fast wave | 87 % → 93 % | 101.1 px | 0.47 | 1.06 | 2938 |
| slow wave | 88 % → 86 % | 101.4 px | 0.50 | 0.98 | 3461 |
| spiral | 93 % → 92 % | 61.6 px | 0.48 | 0.99 | 3548 |
| loop | 78 % → 78 % | 101.0 px | 0.48 | 1.00 | 1664 |
| tilted | 40 % → 40 % | 110.6 px | 0.46 | 1.01 | 1017 |
| over the wet one | 77 % → 79 % | 104.0 px | 0.46 | 1.03 | 846 |
| long, no reload | 99 % → 100 % | 44.6 px | 0.49 | 1.00 | 5932 | quarters: 0.62 → 0.57 → 0.47 → 0.35

Numbers say: light vs heavy: width 148.0 → 153.8 px, dark 0.37 → 0.41; pressure barely changes the width.

## Oil · Henry Ward · Loaded flat #f0b89a filbert
Gouache 1.00 + turpentine 35 % · 84 px · 44.6 s

![Oil · Henry Ward · Loaded flat #f0b89a filbert](Oil-Henry-Ward-Loaded-flat-f0b89a-filbert.png)

A light paint: laid on a grey sheet (on white it cannot be seen); **dark** = how far it is from the grey either way.

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 8 % → 0 % | 24.3 px | 0.00 | 0.00 | 247 |
| heavy line | 19 % → 16 % | 54.3 px | 0.34 | 0.84 | 323 |
| pressure swell | 15 % → 12 % | 55.4 px | 0.30 | 0.83 | 218 |
| fast wave | 47 % → 36 % | 54.9 px | 0.25 | 0.77 | 917 |
| slow wave | 47 % → 28 % | 54.4 px | 0.28 | 0.60 | 1375 |
| spiral | 64 % → 29 % | 42.2 px | 0.24 | 0.46 | 1459 |
| loop | 38 % → 18 % | 49.3 px | 0.26 | 0.47 | 703 |
| tilted | 18 % → 19 % | 51.5 px | 0.24 | 1.00 | 377 |
| over the wet one | 36 % → 26 % | 48.2 px | 0.24 | 0.73 | 326 |
| long, no reload | 61 % → 34 % | 27.4 px | 0.24 | 0.56 | 2005 | quarters: 0.00 → 0.01 → 0.01 → 0.02

Numbers say: light vs heavy: width 24.3 → 54.3 px, dark 0.00 → 0.34; the long stroke does not run out of paint.

## Oil · Henry Ward · Dry scrub #f0b89a filbert
Gouache 1.00 + turpentine 20 % · 90 px · 36.6 s

![Oil · Henry Ward · Dry scrub #f0b89a filbert](Oil-Henry-Ward-Dry-scrub-f0b89a-filbert.png)

A light paint: laid on a grey sheet (on white it cannot be seen); **dark** = how far it is from the grey either way.

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 8 % → 0 % | 23.4 px | 0.00 | 0.00 | 300 |
| heavy line | 17 % → 5 % | 49.4 px | 0.34 | 0.28 | 322 |
| pressure swell | 15 % → 5 % | 55.6 px | 0.30 | 0.32 | 229 |
| fast wave | 51 % → 8 % | 59.4 px | 0.25 | 0.15 | 837 |
| slow wave | 40 % → 7 % | 45.8 px | 0.27 | 0.18 | 1525 |
| spiral | 68 % → 8 % | 44.6 px | 0.20 | 0.12 | 1381 |
| loop | 34 % → 1 % | 43.6 px | 0.22 | 0.03 | 746 |
| tilted | 18 % → 19 % | 51.6 px | 0.21 | 1.00 | 442 |
| over the wet one | 27 % → 6 % | 24.7 px | 0.21 | 0.22 | 306 |
| long, no reload | 52 % → 7 % | 23.4 px | 0.21 | 0.14 | 2155 | quarters: 0.03 → 0.02 → 0.02 → 0.04

Numbers say: light vs heavy: width 23.4 → 49.4 px, dark 0.00 → 0.34; the long stroke does not run out of paint.

## Oil · Henry Ward · Dirty contour #1c2238 flat
Gouache 1.00 + turpentine 35 % · 34 px · 39.1 s

![Oil · Henry Ward · Dirty contour #1c2238 flat](Oil-Henry-Ward-Dirty-contour-1c2238-flat.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 11 % → 4 % | 30.7 px | 0.53 | 0.42 | 117 |
| heavy line | 24 % → 16 % | 69.3 px | 0.54 | 0.67 | 199 |
| pressure swell | 15 % → 11 % | 54.9 px | 0.58 | 0.72 | 130 |
| fast wave | 43 % → 19 % | 50.1 px | 0.63 | 0.44 | 445 |
| slow wave | 41 % → 24 % | 47.5 px | 0.59 | 0.58 | 744 |
| spiral | 59 % → 24 % | 39.1 px | 0.60 | 0.41 | 752 |
| loop | 37 % → 23 % | 47.5 px | 0.57 | 0.64 | 400 |
| tilted | 14 % → 14 % | 37.9 px | 0.63 | 1.01 | 239 |
| over the wet one | 32 % → 27 % | 52.1 px | 0.63 | 0.84 | 211 |
| long, no reload | 72 % → 28 % | 32.4 px | 0.62 | 0.39 | 1591 | quarters: 0.57 → 0.54 → 0.46 → 0.37

Numbers say: light vs heavy: width 30.7 → 69.3 px, dark 0.53 → 0.54.

## Oil · Henry Ward · Ground #ece8e2 flat
Gouache 1.00 + turpentine 30 % · 160 px · 74.9 s

![Oil · Henry Ward · Ground #ece8e2 flat](Oil-Henry-Ward-Ground-ece8e2-flat.png)

A light paint: laid on a grey sheet (on white it cannot be seen); **dark** = how far it is from the grey either way.

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 51 % → 43 % | 148.1 px | 0.37 | 0.84 | 731 |
| heavy line | 52 % → 45 % | 151.1 px | 0.38 | 0.87 | 852 |
| pressure swell | 41 % → 43 % | 154.5 px | 0.37 | 1.04 | 715 |
| fast wave | 85 % → 83 % | 97.9 px | 0.37 | 0.98 | 2785 |
| slow wave | 86 % → 70 % | 99.3 px | 0.37 | 0.81 | 4896 |
| spiral | 89 % → 64 % | 58.5 px | 0.37 | 0.72 | 3654 |
| loop | 75 % → 67 % | 97.0 px | 0.38 | 0.89 | 1965 |
| tilted | 38 % → 38 % | 107.0 px | 0.37 | 1.00 | 1043 |
| over the wet one | 76 % → 69 % | 104.8 px | 0.37 | 0.90 | 1006 |
| long, no reload | 99 % → 85 % | 44.3 px | 0.37 | 0.86 | 5918 | quarters: 0.00 → 0.00 → 0.00 → 0.00

Numbers say: light vs heavy: width 148.1 → 151.1 px, dark 0.37 → 0.38; pressure barely changes the width.

## Oil · Henry Ward · Loaded flat #a03c1c flat
Gouache 1.00 + turpentine 35 % · 84 px · 45.0 s

![Oil · Henry Ward · Loaded flat #a03c1c flat](Oil-Henry-Ward-Loaded-flat-a03c1c-flat.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 11 % → 3 % | 30.6 px | 0.37 | 0.24 | 294 |
| heavy line | 15 % → 12 % | 42.2 px | 0.44 | 0.82 | 377 |
| pressure swell | 15 % → 9 % | 58.0 px | 0.50 | 0.57 | 269 |
| fast wave | 48 % → 28 % | 55.7 px | 0.53 | 0.58 | 799 |
| slow wave | 42 % → 28 % | 48.3 px | 0.46 | 0.67 | 1193 |
| spiral | 63 % → 33 % | 41.5 px | 0.53 | 0.53 | 1470 |
| loop | 39 % → 22 % | 50.4 px | 0.47 | 0.55 | 674 |
| tilted | 19 % → 19 % | 53.0 px | 0.51 | 1.01 | 467 |
| over the wet one | 32 % → 28 % | 36.9 px | 0.51 | 0.88 | 275 |
| long, no reload | 61 % → 31 % | 27.3 px | 0.54 | 0.52 | 1593 | quarters: 0.46 → 0.33 → 0.27 → 0.19

Numbers say: light vs heavy: width 30.6 → 42.2 px, dark 0.37 → 0.44.

## Oil · Henry Ward · Dirty contour #1f3a2c flat
Gouache 1.00 + turpentine 35 % · 34 px · 39.8 s

![Oil · Henry Ward · Dirty contour #1f3a2c flat](Oil-Henry-Ward-Dirty-contour-1f3a2c-flat.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 11 % → 4 % | 30.7 px | 0.47 | 0.42 | 157 |
| heavy line | 24 % → 16 % | 69.3 px | 0.48 | 0.67 | 216 |
| pressure swell | 15 % → 11 % | 54.9 px | 0.53 | 0.72 | 134 |
| fast wave | 43 % → 19 % | 50.1 px | 0.58 | 0.44 | 420 |
| slow wave | 41 % → 24 % | 47.5 px | 0.53 | 0.58 | 737 |
| spiral | 59 % → 24 % | 39.1 px | 0.54 | 0.41 | 769 |
| loop | 37 % → 23 % | 47.5 px | 0.51 | 0.64 | 423 |
| tilted | 14 % → 14 % | 37.9 px | 0.58 | 1.01 | 201 |
| over the wet one | 32 % → 27 % | 52.1 px | 0.58 | 0.84 | 180 |
| long, no reload | 72 % → 28 % | 32.4 px | 0.56 | 0.39 | 1175 | quarters: 0.52 → 0.48 → 0.40 → 0.31

Numbers say: light vs heavy: width 30.7 → 69.3 px, dark 0.47 → 0.48.

## Oil · Henry Ward · Loaded flat #ecc8c8 worn
Gouache 1.00 + turpentine 35 % · 84 px · 47.0 s

![Oil · Henry Ward · Loaded flat #ecc8c8 worn](Oil-Henry-Ward-Loaded-flat-ecc8c8-worn.png)

A light paint: laid on a grey sheet (on white it cannot be seen); **dark** = how far it is from the grey either way.

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 22 % → 2 % | 63.8 px | 0.30 | 0.08 | 336 |
| heavy line | 31 % → 15 % | 91.2 px | 0.33 | 0.48 | 388 |
| pressure swell | 25 % → 11 % | 94.1 px | 0.30 | 0.44 | 278 |
| fast wave | 66 % → 37 % | 76.2 px | 0.25 | 0.56 | 1194 |
| slow wave | 56 % → 32 % | 65.1 px | 0.31 | 0.57 | 1761 |
| spiral | 67 % → 30 % | 44.1 px | 0.26 | 0.44 | 1693 |
| loop | 50 % → 25 % | 65.1 px | 0.30 | 0.51 | 834 |
| tilted | 22 % → 22 % | 62.6 px | 0.26 | 1.00 | 526 |
| over the wet one | 49 % → 35 % | 74.9 px | 0.26 | 0.71 | 460 |
| long, no reload | 90 % → 44 % | 40.3 px | 0.24 | 0.49 | 2232 | quarters: 0.00 → 0.00 → 0.01 → 0.01

Numbers say: light vs heavy: width 63.8 → 91.2 px, dark 0.30 → 0.33; the long stroke does not run out of paint.

## Oil · Henry Ward · Loaded flat #62c8e8 flat
Gouache 1.00 + turpentine 35 % · 84 px · 44.0 s

![Oil · Henry Ward · Loaded flat #62c8e8 flat](Oil-Henry-Ward-Loaded-flat-62c8e8-flat.png)

A light paint: laid on a grey sheet (on white it cannot be seen); **dark** = how far it is from the grey either way.

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 11 % → 3 % | 30.6 px | 0.34 | 0.24 | 236 |
| heavy line | 15 % → 12 % | 42.2 px | 0.30 | 0.82 | 275 |
| pressure swell | 15 % → 9 % | 58.0 px | 0.21 | 0.57 | 193 |
| fast wave | 48 % → 28 % | 55.7 px | 0.17 | 0.58 | 752 |
| slow wave | 42 % → 28 % | 48.3 px | 0.25 | 0.67 | 1183 |
| spiral | 63 % → 33 % | 41.5 px | 0.18 | 0.53 | 1516 |
| loop | 39 % → 22 % | 50.4 px | 0.23 | 0.55 | 631 |
| tilted | 19 % → 19 % | 53.0 px | 0.20 | 1.01 | 449 |
| over the wet one | 32 % → 28 % | 36.9 px | 0.20 | 0.88 | 327 |
| long, no reload | 61 % → 31 % | 27.3 px | 0.18 | 0.52 | 1677 | quarters: 0.00 → 0.01 → 0.01 → 0.01

Numbers say: light vs heavy: width 30.6 → 42.2 px, dark 0.34 → 0.30; the long stroke does not run out of paint.

## Oil · Henry Ward · Loaded flat #0f2018 flat
Gouache 1.00 + turpentine 35 % · 84 px · 42.3 s

![Oil · Henry Ward · Loaded flat #0f2018 flat](Oil-Henry-Ward-Loaded-flat-0f2018-flat.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 11 % → 3 % | 30.6 px | 0.55 | 0.24 | 195 |
| heavy line | 15 % → 12 % | 42.2 px | 0.61 | 0.82 | 255 |
| pressure swell | 15 % → 9 % | 58.0 px | 0.66 | 0.57 | 205 |
| fast wave | 48 % → 28 % | 55.7 px | 0.68 | 0.58 | 801 |
| slow wave | 42 % → 28 % | 48.3 px | 0.63 | 0.67 | 1742 |
| spiral | 63 % → 33 % | 41.5 px | 0.68 | 0.53 | 1660 |
| loop | 39 % → 22 % | 50.4 px | 0.63 | 0.55 | 783 |
| tilted | 19 % → 19 % | 53.0 px | 0.67 | 1.01 | 464 |
| over the wet one | 32 % → 28 % | 36.9 px | 0.67 | 0.88 | 312 |
| long, no reload | 61 % → 31 % | 27.3 px | 0.69 | 0.52 | 1450 | quarters: 0.60 → 0.46 → 0.38 → 0.27

Numbers say: light vs heavy: width 30.6 → 42.2 px, dark 0.55 → 0.61.

## Oil · Henry Ward · Ground #e6e2ee flat
Gouache 1.00 + turpentine 30 % · 160 px · 77.5 s

![Oil · Henry Ward · Ground #e6e2ee flat](Oil-Henry-Ward-Ground-e6e2ee-flat.png)

A light paint: laid on a grey sheet (on white it cannot be seen); **dark** = how far it is from the grey either way.

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 51 % → 43 % | 148.1 px | 0.37 | 0.84 | 873 |
| heavy line | 52 % → 45 % | 151.1 px | 0.37 | 0.87 | 1031 |
| pressure swell | 41 % → 43 % | 154.5 px | 0.37 | 1.04 | 756 |
| fast wave | 85 % → 83 % | 97.9 px | 0.36 | 0.98 | 2595 |
| slow wave | 86 % → 70 % | 99.3 px | 0.37 | 0.81 | 4679 |
| spiral | 89 % → 64 % | 58.5 px | 0.37 | 0.72 | 3433 |
| loop | 75 % → 67 % | 97.0 px | 0.37 | 0.89 | 1686 |
| tilted | 38 % → 38 % | 107.0 px | 0.37 | 1.00 | 1019 |
| over the wet one | 76 % → 69 % | 104.8 px | 0.37 | 0.90 | 924 |
| long, no reload | 99 % → 85 % | 44.3 px | 0.36 | 0.86 | 5248 | quarters: 0.00 → 0.00 → 0.00 → 0.00

Numbers say: light vs heavy: width 148.1 → 151.1 px, dark 0.37 → 0.37; pressure barely changes the width.

## Oil · Henry Ward · Dry scrub #f2f0f6 filbert
Gouache 1.00 + turpentine 20 % · 90 px · 36.0 s

![Oil · Henry Ward · Dry scrub #f2f0f6 filbert](Oil-Henry-Ward-Dry-scrub-f2f0f6-filbert.png)

A light paint: laid on a grey sheet (on white it cannot be seen); **dark** = how far it is from the grey either way.

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 8 % → 0 % | 23.4 px | 0.00 | 0.00 | 236 |
| heavy line | 17 % → 5 % | 49.3 px | 0.38 | 0.27 | 423 |
| pressure swell | 15 % → 5 % | 55.6 px | 0.36 | 0.33 | 263 |
| fast wave | 51 % → 8 % | 59.4 px | 0.32 | 0.16 | 1056 |
| slow wave | 40 % → 7 % | 45.7 px | 0.34 | 0.19 | 1557 |
| spiral | 68 % → 8 % | 44.5 px | 0.29 | 0.12 | 1519 |
| loop | 34 % → 1 % | 43.6 px | 0.29 | 0.03 | 1184 |
| tilted | 18 % → 19 % | 51.6 px | 0.30 | 1.00 | 384 |
| over the wet one | 27 % → 6 % | 24.7 px | 0.30 | 0.23 | 272 |
| long, no reload | 52 % → 8 % | 23.4 px | 0.29 | 0.14 | 1856 | quarters: 0.04 → 0.02 → 0.03 → 0.05

Numbers say: light vs heavy: width 23.4 → 49.3 px, dark 0.00 → 0.38; the long stroke does not run out of paint.

## Oil · Henry Ward · Dirty contour #1e4a78 flat
Gouache 1.00 + turpentine 35 % · 34 px · 37.4 s

![Oil · Henry Ward · Dirty contour #1e4a78 flat](Oil-Henry-Ward-Dirty-contour-1e4a78-flat.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 11 % → 4 % | 30.7 px | 0.41 | 0.42 | 111 |
| heavy line | 24 % → 16 % | 69.3 px | 0.43 | 0.67 | 235 |
| pressure swell | 15 % → 11 % | 54.9 px | 0.47 | 0.72 | 166 |
| fast wave | 43 % → 19 % | 50.1 px | 0.53 | 0.44 | 472 |
| slow wave | 41 % → 24 % | 47.5 px | 0.48 | 0.58 | 1274 |
| spiral | 59 % → 24 % | 39.1 px | 0.49 | 0.41 | 720 |
| loop | 37 % → 23 % | 47.5 px | 0.46 | 0.64 | 625 |
| tilted | 14 % → 14 % | 37.9 px | 0.53 | 1.01 | 187 |
| over the wet one | 32 % → 27 % | 52.1 px | 0.53 | 0.84 | 195 |
| long, no reload | 72 % → 28 % | 32.4 px | 0.51 | 0.39 | 1077 | quarters: 0.47 → 0.43 → 0.34 → 0.25

Numbers say: light vs heavy: width 30.7 → 69.3 px, dark 0.41 → 0.43.

## Oil · Henry Ward · Dirty contour #141414 flat
Gouache 1.00 + turpentine 35 % · 34 px · 35.3 s

![Oil · Henry Ward · Dirty contour #141414 flat](Oil-Henry-Ward-Dirty-contour-141414-flat.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 11 % → 4 % | 30.7 px | 0.60 | 0.42 | 214 |
| heavy line | 24 % → 16 % | 69.3 px | 0.61 | 0.67 | 211 |
| pressure swell | 15 % → 11 % | 54.9 px | 0.64 | 0.72 | 124 |
| fast wave | 43 % → 19 % | 50.1 px | 0.68 | 0.44 | 414 |
| slow wave | 41 % → 24 % | 47.5 px | 0.65 | 0.58 | 655 |
| spiral | 59 % → 24 % | 39.1 px | 0.65 | 0.41 | 687 |
| loop | 37 % → 23 % | 47.5 px | 0.63 | 0.64 | 373 |
| tilted | 14 % → 14 % | 37.9 px | 0.67 | 1.01 | 194 |
| over the wet one | 32 % → 27 % | 52.1 px | 0.67 | 0.84 | 172 |
| long, no reload | 72 % → 28 % | 32.4 px | 0.67 | 0.39 | 1134 | quarters: 0.61 → 0.59 → 0.51 → 0.42

Numbers say: light vs heavy: width 30.7 → 69.3 px, dark 0.60 → 0.61.

## Oil · Henry Ward · Dry scrub #c89038 filbert
Gouache 1.00 + turpentine 20 % · 90 px · 32.2 s

![Oil · Henry Ward · Dry scrub #c89038 filbert](Oil-Henry-Ward-Dry-scrub-c89038-filbert.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 8 % → 0 % | 23.4 px | 0.00 | 0.00 | 258 |
| heavy line | 17 % → 5 % | 49.4 px | 0.12 | 0.28 | 304 |
| pressure swell | 15 % → 5 % | 55.6 px | 0.17 | 0.32 | 205 |
| fast wave | 51 % → 8 % | 59.4 px | 0.21 | 0.15 | 807 |
| slow wave | 40 % → 7 % | 45.8 px | 0.18 | 0.18 | 1335 |
| spiral | 68 % → 8 % | 44.6 px | 0.29 | 0.12 | 1391 |
| loop | 34 % → 1 % | 43.6 px | 0.23 | 0.03 | 709 |
| tilted | 18 % → 19 % | 51.6 px | 0.26 | 1.00 | 376 |
| over the wet one | 27 % → 6 % | 24.7 px | 0.26 | 0.22 | 260 |
| long, no reload | 52 % → 7 % | 23.4 px | 0.27 | 0.14 | 1679 | quarters: 0.09 → 0.14 → 0.10 → 0.04

Numbers say: light vs heavy: width 23.4 → 49.4 px, dark 0.00 → 0.12.

## Oil · Henry Ward · Ground #efe8b8 flat
Gouache 1.00 + turpentine 30 % · 160 px · 89.7 s

![Oil · Henry Ward · Ground #efe8b8 flat](Oil-Henry-Ward-Ground-efe8b8-flat.png)

A light paint: laid on a grey sheet (on white it cannot be seen); **dark** = how far it is from the grey either way.

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 51 % → 43 % | 148.1 px | 0.37 | 0.84 | 697 |
| heavy line | 52 % → 45 % | 151.1 px | 0.37 | 0.87 | 867 |
| pressure swell | 41 % → 43 % | 154.5 px | 0.37 | 1.04 | 562 |
| fast wave | 85 % → 83 % | 97.9 px | 0.36 | 0.98 | 2321 |
| slow wave | 86 % → 70 % | 99.3 px | 0.37 | 0.81 | 3722 |
| spiral | 89 % → 64 % | 58.5 px | 0.37 | 0.72 | 3507 |
| loop | 75 % → 67 % | 97.0 px | 0.37 | 0.89 | 1660 |
| tilted | 38 % → 38 % | 107.0 px | 0.37 | 1.00 | 1035 |
| over the wet one | 76 % → 69 % | 104.8 px | 0.37 | 0.90 | 847 |
| long, no reload | 99 % → 85 % | 44.3 px | 0.36 | 0.86 | 5103 | quarters: 0.00 → 0.00 → 0.00 → 0.00

Numbers say: light vs heavy: width 148.1 → 151.1 px, dark 0.37 → 0.37; pressure barely changes the width.

## Oil · Henry Ward · Loaded flat #a89ac8 worn
Gouache 1.00 + turpentine 35 % · 84 px · 43.3 s

![Oil · Henry Ward · Loaded flat #a89ac8 worn](Oil-Henry-Ward-Loaded-flat-a89ac8-worn.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 22 % → 2 % | 63.8 px | 0.10 | 0.08 | 263 |
| heavy line | 31 % → 15 % | 91.2 px | 0.13 | 0.48 | 387 |
| pressure swell | 25 % → 11 % | 94.1 px | 0.18 | 0.44 | 310 |
| fast wave | 66 % → 37 % | 76.2 px | 0.24 | 0.56 | 1088 |
| slow wave | 56 % → 32 % | 65.1 px | 0.15 | 0.57 | 1617 |
| spiral | 67 % → 30 % | 44.1 px | 0.22 | 0.44 | 1553 |
| loop | 50 % → 25 % | 65.1 px | 0.13 | 0.51 | 785 |
| tilted | 22 % → 22 % | 62.6 px | 0.21 | 1.00 | 450 |
| over the wet one | 49 % → 35 % | 74.9 px | 0.21 | 0.71 | 406 |
| long, no reload | 90 % → 44 % | 40.3 px | 0.25 | 0.49 | 1966 | quarters: 0.23 → 0.22 → 0.13 → 0.07

Numbers say: light vs heavy: width 63.8 → 91.2 px, dark 0.10 → 0.13.

## Oil · Henry Ward · Dirty contour #2a2418 flat
Gouache 1.00 + turpentine 35 % · 34 px · 35.6 s

![Oil · Henry Ward · Dirty contour #2a2418 flat](Oil-Henry-Ward-Dirty-contour-2a2418-flat.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 11 % → 4 % | 30.7 px | 0.52 | 0.42 | 99 |
| heavy line | 24 % → 16 % | 69.3 px | 0.54 | 0.67 | 244 |
| pressure swell | 15 % → 11 % | 54.9 px | 0.57 | 0.72 | 155 |
| fast wave | 43 % → 19 % | 50.1 px | 0.62 | 0.44 | 439 |
| slow wave | 41 % → 24 % | 47.5 px | 0.58 | 0.58 | 748 |
| spiral | 59 % → 24 % | 39.1 px | 0.59 | 0.41 | 765 |
| loop | 37 % → 23 % | 47.5 px | 0.57 | 0.64 | 395 |
| tilted | 14 % → 14 % | 37.9 px | 0.62 | 1.01 | 187 |
| over the wet one | 32 % → 27 % | 52.1 px | 0.62 | 0.84 | 202 |
| long, no reload | 72 % → 28 % | 32.4 px | 0.61 | 0.39 | 1068 | quarters: 0.56 → 0.53 → 0.45 → 0.36

Numbers say: light vs heavy: width 30.7 → 69.3 px, dark 0.52 → 0.54.

## Oil · Henry Ward · Loaded flat #2a2418 filbert
Gouache 1.00 + turpentine 35 % · 84 px · 53.7 s

![Oil · Henry Ward · Loaded flat #2a2418 filbert](Oil-Henry-Ward-Loaded-flat-2a2418-filbert.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 8 % → 0 % | 24.3 px | 0.00 | 0.00 | 211 |
| heavy line | 19 % → 16 % | 54.3 px | 0.55 | 0.84 | 292 |
| pressure swell | 15 % → 12 % | 55.4 px | 0.58 | 0.83 | 215 |
| fast wave | 47 % → 36 % | 54.9 px | 0.62 | 0.77 | 763 |
| slow wave | 47 % → 28 % | 54.4 px | 0.60 | 0.60 | 1216 |
| spiral | 64 % → 29 % | 42.2 px | 0.64 | 0.46 | 1266 |
| loop | 38 % → 18 % | 49.3 px | 0.62 | 0.47 | 660 |
| tilted | 18 % → 19 % | 51.5 px | 0.63 | 1.00 | 361 |
| over the wet one | 36 % → 26 % | 48.2 px | 0.63 | 0.73 | 314 |
| long, no reload | 61 % → 34 % | 27.4 px | 0.63 | 0.56 | 1581 | quarters: 0.56 → 0.45 → 0.35 → 0.17

Numbers say: light vs heavy: width 24.3 → 54.3 px, dark 0.00 → 0.55.

## Oil · Henry Ward · Dry scrub #efeee6 worn
Gouache 1.00 + turpentine 20 % · 90 px · 31.2 s

![Oil · Henry Ward · Dry scrub #efeee6 worn](Oil-Henry-Ward-Dry-scrub-efeee6-worn.png)

A light paint: laid on a grey sheet (on white it cannot be seen); **dark** = how far it is from the grey either way.

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 17 % → 0 % | 48.2 px | 0.00 | 0.00 | 246 |
| heavy line | 30 % → 0 % | 85.8 px | 0.32 | 0.01 | 400 |
| pressure swell | 21 % → 6 % | 77.1 px | 0.31 | 0.28 | 296 |
| fast wave | 68 % → 7 % | 78.5 px | 0.26 | 0.10 | 1102 |
| slow wave | 51 % → 4 % | 58.7 px | 0.29 | 0.07 | 1600 |
| spiral | 72 % → 10 % | 47.6 px | 0.26 | 0.13 | 1682 |
| loop | 51 % → 1 % | 66.3 px | 0.28 | 0.01 | 851 |
| tilted | 20 % → 20 % | 56.8 px | 0.26 | 1.00 | 442 |
| over the wet one | 41 % → 7 % | 56.6 px | 0.26 | 0.17 | 334 |
| long, no reload | 79 % → 0 % | 35.4 px | 0.23 | 0.00 | 1925 | quarters: 0.01 → 0.02 → 0.01 → 0.02

Numbers say: light vs heavy: width 48.2 → 85.8 px, dark 0.00 → 0.32; the long stroke does not run out of paint.

## Oil · Henry Ward · Ground #e6e2f0 flat
Gouache 1.00 + turpentine 30 % · 160 px · 96.3 s

![Oil · Henry Ward · Ground #e6e2f0 flat](Oil-Henry-Ward-Ground-e6e2f0-flat.png)

A light paint: laid on a grey sheet (on white it cannot be seen); **dark** = how far it is from the grey either way.

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 51 % → 43 % | 148.1 px | 0.37 | 0.84 | 699 |
| heavy line | 52 % → 45 % | 151.1 px | 0.37 | 0.87 | 795 |
| pressure swell | 41 % → 43 % | 154.5 px | 0.37 | 1.04 | 614 |
| fast wave | 85 % → 83 % | 97.9 px | 0.36 | 0.98 | 2187 |
| slow wave | 86 % → 70 % | 99.3 px | 0.37 | 0.81 | 3753 |
| spiral | 89 % → 64 % | 58.5 px | 0.37 | 0.72 | 3396 |
| loop | 75 % → 67 % | 97.0 px | 0.37 | 0.89 | 1745 |
| tilted | 38 % → 38 % | 107.0 px | 0.37 | 1.00 | 1061 |
| over the wet one | 76 % → 69 % | 104.8 px | 0.37 | 0.90 | 860 |
| long, no reload | 99 % → 85 % | 44.3 px | 0.36 | 0.86 | 17077 | quarters: 0.00 → 0.00 → 0.00 → 0.00

Numbers say: light vs heavy: width 148.1 → 151.1 px, dark 0.37 → 0.37; pressure barely changes the width.

## Oil · Henry Ward · Loaded flat #a8b84a worn
Gouache 1.00 + turpentine 35 % · 84 px · 66.2 s

![Oil · Henry Ward · Loaded flat #a8b84a worn](Oil-Henry-Ward-Loaded-flat-a8b84a-worn.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 22 % → 2 % | 63.8 px | 0.08 | 0.08 | 269 |
| heavy line | 31 % → 15 % | 91.2 px | 0.11 | 0.48 | 387 |
| pressure swell | 25 % → 11 % | 94.1 px | 0.16 | 0.44 | 281 |
| fast wave | 66 % → 37 % | 76.2 px | 0.21 | 0.56 | 1038 |
| slow wave | 56 % → 32 % | 65.1 px | 0.13 | 0.57 | 1576 |
| spiral | 67 % → 30 % | 44.1 px | 0.20 | 0.44 | 1579 |
| loop | 50 % → 25 % | 65.1 px | 0.12 | 0.51 | 819 |
| tilted | 22 % → 22 % | 62.6 px | 0.19 | 1.00 | 447 |
| over the wet one | 49 % → 35 % | 74.9 px | 0.19 | 0.71 | 414 |
| long, no reload | 90 % → 44 % | 40.3 px | 0.22 | 0.49 | 1990 | quarters: 0.21 → 0.20 → 0.12 → 0.07

Numbers say: light vs heavy: width 63.8 → 91.2 px, dark 0.08 → 0.11.

## Oil · Henry Ward · Thin veil #5a8a6a flat
Watercolour 0.93 · Ink 0.07 + turpentine 80 % · 96 px · 60.4 s

![Oil · Henry Ward · Thin veil #5a8a6a flat](Oil-Henry-Ward-Thin-veil-5a8a6a-flat.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 3 % → 4 % | 9.5 px | 0.02 | 1.09 | 182 |
| heavy line | 17 % → 20 % | 50.1 px | 0.06 | 1.13 | 273 |
| pressure swell | 12 % → 14 % | 44.3 px | 0.06 | 1.21 | 202 |
| fast wave | 47 % → 54 % | 54.4 px | 0.06 | 1.14 | 816 |
| slow wave | 48 % → 55 % | 54.9 px | 0.06 | 1.16 | 1326 |
| spiral | 65 % → 70 % | 42.6 px | 0.06 | 1.09 | 1426 |
| loop | 40 % → 48 % | 52.2 px | 0.05 | 1.19 | 690 |
| tilted | 18 % → 19 % | 50.9 px | 0.07 | 1.03 | 511 |
| over the wet one | 28 % → 31 % | 28.0 px | 0.07 | 1.11 | 267 |
| long, no reload | 62 % → 78 % | 27.6 px | 0.06 | 1.26 | 1923 | quarters: 0.06 → 0.06 → 0.04 → 0.03

Numbers say: light vs heavy: width 9.5 → 50.1 px, dark 0.02 → 0.06.

## Oil · Henry Ward · Loaded flat #4a1420 worn
Gouache 1.00 + turpentine 35 % · 84 px · 69.7 s

![Oil · Henry Ward · Loaded flat #4a1420 worn](Oil-Henry-Ward-Loaded-flat-4a1420-worn.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 22 % → 2 % | 63.8 px | 0.49 | 0.08 | 282 |
| heavy line | 31 % → 15 % | 91.2 px | 0.51 | 0.48 | 377 |
| pressure swell | 25 % → 11 % | 94.1 px | 0.52 | 0.44 | 297 |
| fast wave | 66 % → 37 % | 76.2 px | 0.55 | 0.56 | 962 |
| slow wave | 56 % → 32 % | 65.1 px | 0.52 | 0.57 | 1612 |
| spiral | 67 % → 30 % | 44.1 px | 0.54 | 0.44 | 1518 |
| loop | 50 % → 25 % | 65.1 px | 0.50 | 0.51 | 854 |
| tilted | 22 % → 22 % | 62.6 px | 0.54 | 1.00 | 441 |
| over the wet one | 49 % → 35 % | 74.9 px | 0.54 | 0.71 | 476 |
| long, no reload | 90 % → 44 % | 40.3 px | 0.56 | 0.49 | 5589 | quarters: 0.55 → 0.54 → 0.48 → 0.41

Numbers say: light vs heavy: width 63.8 → 91.2 px, dark 0.49 → 0.51.

## Oil · Henry Ward · Dirty contour #2a0a10 flat
Gouache 1.00 + turpentine 35 % · 34 px · 62.1 s

![Oil · Henry Ward · Dirty contour #2a0a10 flat](Oil-Henry-Ward-Dirty-contour-2a0a10-flat.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 11 % → 4 % | 30.7 px | 0.62 | 0.42 | 95 |
| heavy line | 24 % → 16 % | 69.3 px | 0.63 | 0.67 | 204 |
| pressure swell | 15 % → 11 % | 54.9 px | 0.64 | 0.72 | 140 |
| fast wave | 43 % → 19 % | 50.1 px | 0.67 | 0.44 | 502 |
| slow wave | 41 % → 24 % | 47.5 px | 0.65 | 0.58 | 1922 |
| spiral | 59 % → 24 % | 39.1 px | 0.65 | 0.41 | 2500 |
| loop | 37 % → 23 % | 47.5 px | 0.64 | 0.64 | 926 |
| tilted | 14 % → 14 % | 37.9 px | 0.66 | 1.01 | 740 |
| over the wet one | 32 % → 27 % | 52.1 px | 0.66 | 0.84 | 725 |
| long, no reload | 72 % → 28 % | 32.4 px | 0.66 | 0.39 | 1718 | quarters: 0.61 → 0.58 → 0.50 → 0.41

Numbers say: light vs heavy: width 30.7 → 69.3 px, dark 0.62 → 0.63.

## Oil · Henry Ward · Dry scrub #c0506a worn
Gouache 1.00 + turpentine 20 % · 90 px · 56.6 s

![Oil · Henry Ward · Dry scrub #c0506a worn](Oil-Henry-Ward-Dry-scrub-c0506a-worn.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 17 % → 0 % | 48.2 px | 0.00 | 0.00 | 839 |
| heavy line | 30 % → 0 % | 85.8 px | 0.26 | 0.01 | 753 |
| pressure swell | 21 % → 6 % | 77.1 px | 0.26 | 0.28 | 1340 |
| fast wave | 68 % → 7 % | 78.5 px | 0.34 | 0.10 | 2899 |
| slow wave | 51 % → 4 % | 58.7 px | 0.28 | 0.07 | 6764 |
| spiral | 72 % → 9 % | 47.6 px | 0.35 | 0.13 | 2947 |
| loop | 51 % → 1 % | 66.3 px | 0.26 | 0.01 | 1376 |
| tilted | 20 % → 20 % | 56.8 px | 0.34 | 1.00 | 1194 |
| over the wet one | 41 % → 7 % | 56.6 px | 0.34 | 0.16 | 558 |
| long, no reload | 79 % → 0 % | 35.4 px | 0.38 | 0.00 | 2546 | quarters: 0.21 → 0.16 → 0.16 → 0.11

Numbers say: light vs heavy: width 48.2 → 85.8 px, dark 0.00 → 0.26.

## Oil · Henry Ward · Ground #d8d4c8 flat
Ink 0.65 · Watercolour 0.35 + turpentine 75 % · 160 px · 93.2 s

![Oil · Henry Ward · Ground #d8d4c8 flat](Oil-Henry-Ward-Ground-d8d4c8-flat.png)

A light paint: laid on a grey sheet (on white it cannot be seen); **dark** = how far it is from the grey either way.

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 51 % → 56 % | 148.0 px | 0.06 | 1.10 | 1257 |
| heavy line | 53 % → 52 % | 153.8 px | 0.06 | 0.98 | 3951 |
| pressure swell | 41 % → 50 % | 155.4 px | 0.06 | 1.21 | 1089 |
| fast wave | 87 % → 93 % | 101.1 px | 0.05 | 1.06 | 7011 |
| slow wave | 88 % → 86 % | 101.4 px | 0.04 | 0.98 | 5020 |
| spiral | 93 % → 92 % | 61.6 px | 0.04 | 0.99 | 5339 |
| loop | 78 % → 78 % | 101.0 px | 0.04 | 1.00 | 2967 |
| tilted | 40 % → 40 % | 110.6 px | 0.05 | 1.01 | 1329 |
| over the wet one | 77 % → 79 % | 104.0 px | 0.05 | 1.03 | 1754 |
| long, no reload | 99 % → 100 % | 44.6 px | 0.04 | 1.00 | 7455 | quarters: 0.01 → 0.02 → 0.04 → 0.07

Numbers say: light vs heavy: width 148.0 → 153.8 px, dark 0.06 → 0.06; pressure barely changes the width; the long stroke does not run out of paint.

## Oil · Henry Ward · Loaded flat #e8d8b0 flat
Gouache 1.00 + turpentine 35 % · 84 px · 60.3 s

![Oil · Henry Ward · Loaded flat #e8d8b0 flat](Oil-Henry-Ward-Loaded-flat-e8d8b0-flat.png)

A light paint: laid on a grey sheet (on white it cannot be seen); **dark** = how far it is from the grey either way.

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 11 % → 3 % | 30.6 px | 0.42 | 0.24 | 465 |
| heavy line | 15 % → 12 % | 42.2 px | 0.40 | 0.82 | 586 |
| pressure swell | 15 % → 9 % | 58.0 px | 0.31 | 0.57 | 777 |
| fast wave | 48 % → 28 % | 55.7 px | 0.28 | 0.58 | 1068 |
| slow wave | 42 % → 28 % | 48.3 px | 0.34 | 0.67 | 2308 |
| spiral | 63 % → 33 % | 41.5 px | 0.28 | 0.53 | 2146 |
| loop | 39 % → 22 % | 50.4 px | 0.32 | 0.55 | 1256 |
| tilted | 19 % → 19 % | 53.0 px | 0.30 | 1.01 | 585 |
| over the wet one | 32 % → 28 % | 36.9 px | 0.30 | 0.88 | 353 |
| long, no reload | 61 % → 31 % | 27.3 px | 0.28 | 0.52 | 2922 | quarters: 0.00 → 0.01 → 0.01 → 0.02

Numbers say: light vs heavy: width 30.6 → 42.2 px, dark 0.42 → 0.40; the long stroke does not run out of paint.

## Oil · Henry Ward · Dry scrub #f2ead0 filbert
Gouache 1.00 + turpentine 20 % · 90 px · 46.7 s

![Oil · Henry Ward · Dry scrub #f2ead0 filbert](Oil-Henry-Ward-Dry-scrub-f2ead0-filbert.png)

A light paint: laid on a grey sheet (on white it cannot be seen); **dark** = how far it is from the grey either way.

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 8 % → 0 % | 23.4 px | 0.00 | 0.00 | 281 |
| heavy line | 17 % → 5 % | 49.3 px | 0.38 | 0.27 | 574 |
| pressure swell | 15 % → 5 % | 55.6 px | 0.35 | 0.33 | 388 |
| fast wave | 51 % → 8 % | 59.4 px | 0.31 | 0.16 | 1230 |
| slow wave | 40 % → 7 % | 45.7 px | 0.33 | 0.19 | 2704 |
| spiral | 68 % → 8 % | 44.5 px | 0.28 | 0.12 | 1834 |
| loop | 34 % → 1 % | 43.6 px | 0.28 | 0.03 | 1433 |
| tilted | 18 % → 19 % | 51.6 px | 0.28 | 1.00 | 867 |
| over the wet one | 27 % → 6 % | 24.7 px | 0.28 | 0.23 | 361 |
| long, no reload | 52 % → 8 % | 23.4 px | 0.28 | 0.14 | 3514 | quarters: 0.04 → 0.02 → 0.03 → 0.05

Numbers say: light vs heavy: width 23.4 → 49.3 px, dark 0.00 → 0.38; the long stroke does not run out of paint.

## Oil · Henry Ward · Loaded flat #2a1428 flat
Gouache 1.00 + turpentine 35 % · 84 px · 48.3 s

![Oil · Henry Ward · Loaded flat #2a1428 flat](Oil-Henry-Ward-Loaded-flat-2a1428-flat.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 11 % → 3 % | 30.6 px | 0.55 | 0.24 | 382 |
| heavy line | 15 % → 12 % | 42.2 px | 0.61 | 0.82 | 461 |
| pressure swell | 15 % → 9 % | 58.0 px | 0.66 | 0.57 | 339 |
| fast wave | 48 % → 28 % | 55.7 px | 0.68 | 0.58 | 1639 |
| slow wave | 42 % → 28 % | 48.3 px | 0.63 | 0.67 | 1466 |
| spiral | 63 % → 33 % | 41.5 px | 0.68 | 0.53 | 1556 |
| loop | 39 % → 22 % | 50.4 px | 0.63 | 0.55 | 716 |
| tilted | 19 % → 19 % | 53.0 px | 0.67 | 1.01 | 415 |
| over the wet one | 32 % → 28 % | 36.9 px | 0.67 | 0.88 | 282 |
| long, no reload | 61 % → 31 % | 27.3 px | 0.68 | 0.52 | 1868 | quarters: 0.60 → 0.46 → 0.38 → 0.27

Numbers say: light vs heavy: width 30.6 → 42.2 px, dark 0.55 → 0.61.

## Oil · Henry Ward · Ground #e8e4e0 flat
Gouache 1.00 + turpentine 30 % · 160 px · 82.2 s

![Oil · Henry Ward · Ground #e8e4e0 flat](Oil-Henry-Ward-Ground-e8e4e0-flat.png)

A light paint: laid on a grey sheet (on white it cannot be seen); **dark** = how far it is from the grey either way.

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 51 % → 43 % | 148.1 px | 0.37 | 0.84 | 1533 |
| heavy line | 52 % → 45 % | 151.1 px | 0.37 | 0.87 | 1676 |
| pressure swell | 41 % → 43 % | 154.5 px | 0.37 | 1.04 | 1414 |
| fast wave | 85 % → 83 % | 97.9 px | 0.36 | 0.98 | 2530 |
| slow wave | 86 % → 70 % | 99.3 px | 0.37 | 0.81 | 4171 |
| spiral | 89 % → 64 % | 58.5 px | 0.37 | 0.72 | 4154 |
| loop | 75 % → 67 % | 97.0 px | 0.37 | 0.89 | 1878 |
| tilted | 38 % → 38 % | 107.0 px | 0.37 | 1.00 | 1045 |
| over the wet one | 76 % → 69 % | 104.8 px | 0.37 | 0.90 | 1000 |
| long, no reload | 99 % → 85 % | 44.3 px | 0.36 | 0.86 | 6742 | quarters: 0.00 → 0.00 → 0.00 → 0.00

Numbers say: light vs heavy: width 148.1 → 151.1 px, dark 0.37 → 0.37; pressure barely changes the width.

## Oil · Henry Ward · Loaded flat #8a2a18 filbert
Gouache 1.00 + turpentine 35 % · 84 px · 47.6 s

![Oil · Henry Ward · Loaded flat #8a2a18 filbert](Oil-Henry-Ward-Loaded-flat-8a2a18-filbert.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 8 % → 0 % | 24.3 px | 0.00 | 0.00 | 433 |
| heavy line | 19 % → 16 % | 54.3 px | 0.50 | 0.84 | 675 |
| pressure swell | 15 % → 12 % | 55.4 px | 0.52 | 0.83 | 494 |
| fast wave | 47 % → 36 % | 54.9 px | 0.56 | 0.77 | 1678 |
| slow wave | 47 % → 28 % | 54.4 px | 0.54 | 0.60 | 1342 |
| spiral | 64 % → 29 % | 42.2 px | 0.57 | 0.46 | 1396 |
| loop | 38 % → 18 % | 49.3 px | 0.55 | 0.47 | 667 |
| tilted | 18 % → 19 % | 51.5 px | 0.57 | 1.00 | 372 |
| over the wet one | 36 % → 26 % | 48.2 px | 0.57 | 0.73 | 300 |
| long, no reload | 61 % → 34 % | 27.4 px | 0.57 | 0.56 | 1985 | quarters: 0.50 → 0.40 → 0.31 → 0.15

Numbers say: light vs heavy: width 24.3 → 54.3 px, dark 0.00 → 0.50.

## Oil · Henry Ward · Loaded flat #a8c8dc filbert
Gouache 1.00 + turpentine 35 % · 84 px · 44.7 s

![Oil · Henry Ward · Loaded flat #a8c8dc filbert](Oil-Henry-Ward-Loaded-flat-a8c8dc-filbert.png)

A light paint: laid on a grey sheet (on white it cannot be seen); **dark** = how far it is from the grey either way.

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 8 % → 0 % | 24.3 px | 0.00 | 0.00 | 267 |
| heavy line | 19 % → 16 % | 54.3 px | 0.35 | 0.84 | 307 |
| pressure swell | 15 % → 12 % | 55.4 px | 0.30 | 0.83 | 245 |
| fast wave | 47 % → 36 % | 54.9 px | 0.26 | 0.77 | 791 |
| slow wave | 47 % → 28 % | 54.4 px | 0.29 | 0.60 | 1360 |
| spiral | 64 % → 29 % | 42.2 px | 0.25 | 0.46 | 1555 |
| loop | 38 % → 18 % | 49.3 px | 0.26 | 0.47 | 902 |
| tilted | 18 % → 19 % | 51.5 px | 0.24 | 1.00 | 429 |
| over the wet one | 36 % → 26 % | 48.2 px | 0.24 | 0.73 | 316 |
| long, no reload | 61 % → 34 % | 27.4 px | 0.25 | 0.56 | 1696 | quarters: 0.00 → 0.01 → 0.01 → 0.02

Numbers say: light vs heavy: width 24.3 → 54.3 px, dark 0.00 → 0.35; the long stroke does not run out of paint.

## Oil · Henry Ward · Dry scrub #d8e8f0 filbert
Gouache 1.00 + turpentine 20 % · 90 px · 37.3 s

![Oil · Henry Ward · Dry scrub #d8e8f0 filbert](Oil-Henry-Ward-Dry-scrub-d8e8f0-filbert.png)

A light paint: laid on a grey sheet (on white it cannot be seen); **dark** = how far it is from the grey either way.

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 8 % → 0 % | 23.4 px | 0.00 | 0.00 | 223 |
| heavy line | 17 % → 5 % | 49.3 px | 0.38 | 0.27 | 308 |
| pressure swell | 15 % → 5 % | 55.6 px | 0.35 | 0.33 | 208 |
| fast wave | 51 % → 8 % | 59.4 px | 0.30 | 0.16 | 859 |
| slow wave | 40 % → 7 % | 45.7 px | 0.33 | 0.19 | 1605 |
| spiral | 68 % → 8 % | 44.5 px | 0.27 | 0.12 | 1670 |
| loop | 34 % → 1 % | 43.6 px | 0.28 | 0.03 | 684 |
| tilted | 18 % → 19 % | 51.6 px | 0.28 | 1.00 | 406 |
| over the wet one | 27 % → 6 % | 24.7 px | 0.28 | 0.23 | 294 |
| long, no reload | 52 % → 8 % | 23.4 px | 0.28 | 0.14 | 1701 | quarters: 0.04 → 0.02 → 0.03 → 0.05

Numbers say: light vs heavy: width 23.4 → 49.3 px, dark 0.00 → 0.38; the long stroke does not run out of paint.

## Oil · Henry Ward · Ground #3a3a34 flat
Ink 0.65 · Watercolour 0.35 + turpentine 75 % · 160 px · 70.2 s

![Oil · Henry Ward · Ground #3a3a34 flat](Oil-Henry-Ward-Ground-3a3a34-flat.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 51 % → 56 % | 148.0 px | 0.36 | 1.10 | 540 |
| heavy line | 53 % → 52 % | 153.8 px | 0.40 | 0.98 | 864 |
| pressure swell | 41 % → 50 % | 155.4 px | 0.41 | 1.21 | 697 |
| fast wave | 87 % → 93 % | 101.1 px | 0.45 | 1.06 | 2180 |
| slow wave | 88 % → 86 % | 101.4 px | 0.49 | 0.98 | 3367 |
| spiral | 93 % → 92 % | 61.6 px | 0.47 | 0.99 | 3173 |
| loop | 78 % → 78 % | 101.0 px | 0.47 | 1.00 | 1710 |
| tilted | 40 % → 40 % | 110.6 px | 0.45 | 1.01 | 960 |
| over the wet one | 77 % → 79 % | 104.0 px | 0.45 | 1.03 | 1098 |
| long, no reload | 99 % → 100 % | 44.6 px | 0.48 | 1.00 | 6018 | quarters: 0.62 → 0.57 → 0.47 → 0.34

Numbers say: light vs heavy: width 148.0 → 153.8 px, dark 0.36 → 0.40; pressure barely changes the width.

## Oil · Henry Ward · Loaded flat #8a906a worn
Gouache 1.00 + turpentine 35 % · 84 px · 50.7 s

![Oil · Henry Ward · Loaded flat #8a906a worn](Oil-Henry-Ward-Loaded-flat-8a906a-worn.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 22 % → 2 % | 63.8 px | 0.15 | 0.08 | 286 |
| heavy line | 31 % → 15 % | 91.2 px | 0.18 | 0.48 | 389 |
| pressure swell | 25 % → 11 % | 94.1 px | 0.23 | 0.44 | 282 |
| fast wave | 66 % → 37 % | 76.2 px | 0.29 | 0.56 | 1182 |
| slow wave | 56 % → 32 % | 65.1 px | 0.20 | 0.57 | 1910 |
| spiral | 67 % → 30 % | 44.1 px | 0.27 | 0.44 | 1823 |
| loop | 50 % → 25 % | 65.1 px | 0.19 | 0.51 | 955 |
| tilted | 22 % → 22 % | 62.6 px | 0.26 | 1.00 | 470 |
| over the wet one | 49 % → 35 % | 74.9 px | 0.26 | 0.71 | 488 |
| long, no reload | 90 % → 44 % | 40.3 px | 0.30 | 0.49 | 2361 | quarters: 0.28 → 0.27 → 0.17 → 0.09

Numbers say: light vs heavy: width 63.8 → 91.2 px, dark 0.15 → 0.18.

## Oil · Henry Ward · Loaded flat #7a8458 flat
Gouache 1.00 + turpentine 35 % · 84 px · 45.0 s

![Oil · Henry Ward · Loaded flat #7a8458 flat](Oil-Henry-Ward-Loaded-flat-7a8458-flat.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 11 % → 3 % | 30.6 px | 0.18 | 0.24 | 219 |
| heavy line | 15 % → 12 % | 42.2 px | 0.25 | 0.82 | 264 |
| pressure swell | 15 % → 9 % | 58.0 px | 0.32 | 0.57 | 215 |
| fast wave | 48 % → 28 % | 55.7 px | 0.37 | 0.58 | 895 |
| slow wave | 42 % → 28 % | 48.3 px | 0.28 | 0.67 | 1375 |
| spiral | 63 % → 33 % | 41.5 px | 0.35 | 0.53 | 1529 |
| loop | 39 % → 22 % | 50.4 px | 0.28 | 0.55 | 789 |
| tilted | 19 % → 19 % | 53.0 px | 0.35 | 1.01 | 710 |
| over the wet one | 32 % → 28 % | 36.9 px | 0.35 | 0.88 | 279 |
| long, no reload | 61 % → 31 % | 27.3 px | 0.36 | 0.52 | 1825 | quarters: 0.30 → 0.19 → 0.14 → 0.10

Numbers say: light vs heavy: width 30.6 → 42.2 px, dark 0.18 → 0.25.

## Oil · Henry Ward · Dry scrub #a8ae88 filbert
Gouache 1.00 + turpentine 20 % · 90 px · 38.6 s

![Oil · Henry Ward · Dry scrub #a8ae88 filbert](Oil-Henry-Ward-Dry-scrub-a8ae88-filbert.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 8 % → 0 % | 23.4 px | 0.00 | 0.00 | 238 |
| heavy line | 17 % → 5 % | 49.4 px | 0.06 | 0.28 | 312 |
| pressure swell | 15 % → 5 % | 55.6 px | 0.12 | 0.32 | 252 |
| fast wave | 51 % → 8 % | 59.4 px | 0.16 | 0.15 | 1024 |
| slow wave | 40 % → 7 % | 45.8 px | 0.13 | 0.18 | 1589 |
| spiral | 68 % → 8 % | 44.6 px | 0.24 | 0.12 | 1513 |
| loop | 34 % → 1 % | 43.6 px | 0.18 | 0.03 | 752 |
| tilted | 18 % → 19 % | 51.6 px | 0.21 | 1.00 | 960 |
| over the wet one | 27 % → 6 % | 24.7 px | 0.21 | 0.22 | 299 |
| long, no reload | 52 % → 7 % | 23.4 px | 0.22 | 0.14 | 2038 | quarters: 0.06 → 0.10 → 0.07 → 0.03

Numbers say: light vs heavy: width 23.4 → 49.4 px, dark 0.00 → 0.06.

## Surface test · Under SmoothPanel
Gouache 1.00 + turpentine 30 % · 60 px · 39.9 s

![Surface test · Under SmoothPanel](Surface-test-Under-SmoothPanel.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 7 % → 1 % | 21.3 px | 0.46 | 0.13 | 203 |
| heavy line | 14 % → 13 % | 39.2 px | 0.47 | 0.96 | 183 |
| pressure swell | 12 % → 10 % | 44.6 px | 0.47 | 0.87 | 177 |
| fast wave | 35 % → 22 % | 41.0 px | 0.49 | 0.63 | 536 |
| slow wave | 30 % → 21 % | 35.0 px | 0.46 | 0.68 | 861 |
| spiral | 59 % → 26 % | 39.0 px | 0.43 | 0.44 | 897 |
| loop | 29 % → 19 % | 37.7 px | 0.46 | 0.67 | 451 |
| tilted | 15 % → 15 % | 42.0 px | 0.49 | 1.01 | 299 |
| over the wet one | 29 % → 26 % | 38.7 px | 0.49 | 0.91 | 211 |
| long, no reload | 47 % → 27 % | 21.0 px | 0.47 | 0.58 | 1127 | quarters: 0.33 → 0.20 → 0.18 → 0.13

Numbers say: light vs heavy: width 21.3 → 39.2 px, dark 0.46 → 0.47.

## Surface test · Oil 0% SmoothPanel
Oil 1.00 · 70 px · 24.7 s

![Surface test · Oil 0% SmoothPanel](Surface-test-Oil-0-SmoothPanel.png)

A light paint: laid on a grey sheet (on white it cannot be seen); **dark** = how far it is from the grey either way.

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 9 % → 10 % | 26.7 px | 0.29 | 1.04 | 175 |
| heavy line | 15 % → 15 % | 44.4 px | 0.36 | 1.00 | 330 |
| pressure swell | 14 % → 14 % | 51.5 px | 0.33 | 1.02 | 337 |
| fast wave | 41 % → 43 % | 47.9 px | 0.31 | 1.03 | 722 |
| slow wave | 40 % → 40 % | 45.8 px | 0.37 | 1.00 | 1074 |
| spiral | 58 % → 58 % | 38.0 px | 0.32 | 1.00 | 1184 |
| loop | 39 % → 39 % | 50.7 px | 0.35 | 1.00 | 708 |
| tilted | 17 % → 17 % | 47.4 px | 0.31 | 1.00 | 390 |
| over the wet one | 32 % → 32 % | 41.9 px | 0.31 | 1.00 | 341 |
| long, no reload | 66 % → 66 % | 29.4 px | 0.31 | 1.00 | 1762 | quarters: 0.00 → 0.00 → 0.00 → 0.00

Numbers say: light vs heavy: width 26.7 → 44.4 px, dark 0.29 → 0.36; the long stroke does not run out of paint.

## Surface test · Oil 40% SmoothPanel
Gouache 1.00 + turpentine 40 % · 70 px · 42.5 s

![Surface test · Oil 40% SmoothPanel](Surface-test-Oil-40-SmoothPanel.png)

A light paint: laid on a grey sheet (on white it cannot be seen); **dark** = how far it is from the grey either way.

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 9 % → 3 % | 27.0 px | 0.41 | 0.29 | 207 |
| heavy line | 14 % → 14 % | 42.1 px | 0.40 | 0.98 | 261 |
| pressure swell | 14 % → 12 % | 53.8 px | 0.38 | 0.85 | 202 |
| fast wave | 39 % → 27 % | 45.5 px | 0.32 | 0.68 | 642 |
| slow wave | 32 % → 21 % | 37.5 px | 0.38 | 0.63 | 979 |
| spiral | 56 % → 31 % | 36.7 px | 0.36 | 0.56 | 1099 |
| loop | 34 % → 21 % | 44.3 px | 0.36 | 0.62 | 513 |
| tilted | 17 % → 17 % | 47.7 px | 0.36 | 1.00 | 290 |
| over the wet one | 35 % → 30 % | 49.5 px | 0.36 | 0.85 | 335 |
| long, no reload | 55 % → 33 % | 24.8 px | 0.37 | 0.59 | 1608 | quarters: 0.00 → 0.01 → 0.01 → 0.02

Numbers say: light vs heavy: width 27.0 → 42.1 px, dark 0.41 → 0.40; the long stroke does not run out of paint.

## Surface test · Oil 80% SmoothPanel
Watercolour 0.93 · Ink 0.07 + turpentine 80 % · 70 px · 38.7 s

![Surface test · Oil 80% SmoothPanel](Surface-test-Oil-80-SmoothPanel.png)

A light paint: laid on a grey sheet (on white it cannot be seen); **dark** = how far it is from the grey either way.

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 6 % → 8 % | 18.1 px | 0.08 | 1.30 | 145 |
| heavy line | 15 % → 21 % | 44.9 px | 0.09 | 1.34 | 224 |
| pressure swell | 13 % → 17 % | 49.0 px | 0.09 | 1.27 | 163 |
| fast wave | 37 % → 43 % | 42.7 px | 0.10 | 1.16 | 561 |
| slow wave | 34 % → 44 % | 38.8 px | 0.10 | 1.30 | 996 |
| spiral | 49 % → 61 % | 32.6 px | 0.09 | 1.23 | 1059 |
| loop | 34 % → 40 % | 43.4 px | 0.09 | 1.21 | 527 |
| tilted | 16 % → 16 % | 44.3 px | 0.10 | 1.03 | 358 |
| over the wet one | 32 % → 39 % | 45.7 px | 0.10 | 1.21 | 253 |
| long, no reload | 51 % → 66 % | 22.8 px | 0.09 | 1.29 | 1459 | quarters: 0.09 → 0.09 → 0.06 → 0.03

Numbers say: light vs heavy: width 18.1 → 44.9 px, dark 0.08 → 0.09.

## Surface test · Dry scrub SmoothPanel
Gouache 1.00 + turpentine 20 % · 70 px · 34.4 s

![Surface test · Dry scrub SmoothPanel](Surface-test-Dry-scrub-SmoothPanel.png)

A light paint: laid on a grey sheet (on white it cannot be seen); **dark** = how far it is from the grey either way.

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 13 % → 0 % | 36.5 px | 0.00 | 0.00 | 234 |
| heavy line | 28 % → 3 % | 81.3 px | 0.33 | 0.09 | 290 |
| pressure swell | 18 % → 7 % | 68.3 px | 0.35 | 0.38 | 275 |
| fast wave | 61 % → 24 % | 70.6 px | 0.28 | 0.39 | 1052 |
| slow wave | 43 % → 15 % | 49.5 px | 0.32 | 0.36 | 1420 |
| spiral | 69 % → 13 % | 45.3 px | 0.32 | 0.18 | 1522 |
| loop | 44 % → 3 % | 57.5 px | 0.29 | 0.07 | 760 |
| tilted | 16 % → 16 % | 44.4 px | 0.28 | 1.00 | 349 |
| over the wet one | 35 % → 13 % | 52.3 px | 0.28 | 0.36 | 327 |
| long, no reload | 87 % → 19 % | 39.1 px | 0.31 | 0.22 | 1758 | quarters: 0.00 → 0.01 → 0.01 → 0.02

Numbers say: light vs heavy: width 36.5 → 81.3 px, dark 0.00 → 0.33; the long stroke does not run out of paint.

## Surface test · Watercolour SmoothPanel
Watercolour 1.00 + water 40 % · 60 px · 31.8 s

![Surface test · Watercolour SmoothPanel](Surface-test-Watercolour-SmoothPanel.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 8 % → 14 % | 24.2 px | 0.37 | 1.67 | 62 |
| heavy line | 16 % → 19 % | 47.6 px | 0.38 | 1.17 | 135 |
| pressure swell | 10 % → 13 % | 37.5 px | 0.40 | 1.26 | 92 |
| fast wave | 36 % → 39 % | 41.1 px | 0.36 | 1.11 | 273 |
| slow wave | 33 % → 38 % | 38.1 px | 0.37 | 1.16 | 486 |
| spiral | 56 % → 59 % | 36.9 px | 0.32 | 1.05 | 376 |
| loop | 28 % → 33 % | 36.8 px | 0.39 | 1.15 | 293 |
| tilted | 18 % → 18 % | 51.2 px | 0.37 | 1.00 | 154 |
| over the wet one | 30 % → 33 % | 33.0 px | 0.37 | 1.09 | 150 |
| long, no reload | 73 % → 75 % | 32.5 px | 0.31 | 1.04 | 633 | quarters: 0.35 → 0.28 → 0.22 → 0.16

Numbers say: light vs heavy: width 24.2 → 47.6 px, dark 0.37 → 0.38; wet paint spreads well beyond the stroke.

## Surface test · Surface test · smooth panel
Gouache 1.00 + turpentine 40 % · 70 px · 44.0 s

![Surface test · Surface test · smooth panel](Surface-test-Surface-test-smooth-panel.png)

A light paint: laid on a grey sheet (on white it cannot be seen); **dark** = how far it is from the grey either way.

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 9 % → 3 % | 27.0 px | 0.41 | 0.29 | 173 |
| heavy line | 14 % → 14 % | 42.1 px | 0.40 | 0.98 | 278 |
| pressure swell | 14 % → 12 % | 53.8 px | 0.38 | 0.85 | 173 |
| fast wave | 39 % → 27 % | 45.5 px | 0.32 | 0.68 | 776 |
| slow wave | 32 % → 21 % | 37.5 px | 0.38 | 0.63 | 1344 |
| spiral | 56 % → 31 % | 36.7 px | 0.36 | 0.56 | 1243 |
| loop | 34 % → 21 % | 44.3 px | 0.36 | 0.62 | 615 |
| tilted | 17 % → 17 % | 47.7 px | 0.36 | 1.00 | 389 |
| over the wet one | 35 % → 30 % | 49.5 px | 0.36 | 0.85 | 267 |
| long, no reload | 55 % → 33 % | 24.8 px | 0.37 | 0.59 | 1562 | quarters: 0.00 → 0.01 → 0.01 → 0.02

Numbers say: light vs heavy: width 27.0 → 42.1 px, dark 0.41 → 0.40; the long stroke does not run out of paint.

## Surface test · Under Paper
Gouache 1.00 + turpentine 30 % · 60 px · 40.2 s

![Surface test · Under Paper](Surface-test-Under-Paper.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 7 % → 1 % | 21.2 px | 0.46 | 0.12 | 164 |
| heavy line | 13 % → 13 % | 38.9 px | 0.46 | 0.94 | 226 |
| pressure swell | 12 % → 10 % | 44.4 px | 0.47 | 0.86 | 201 |
| fast wave | 35 % → 20 % | 40.3 px | 0.49 | 0.56 | 537 |
| slow wave | 30 % → 19 % | 34.5 px | 0.46 | 0.65 | 996 |
| spiral | 54 % → 25 % | 35.9 px | 0.42 | 0.46 | 1027 |
| loop | 29 % → 19 % | 37.3 px | 0.45 | 0.66 | 500 |
| tilted | 15 % → 15 % | 41.8 px | 0.49 | 1.01 | 326 |
| over the wet one | 29 % → 25 % | 38.8 px | 0.49 | 0.88 | 261 |
| long, no reload | 43 % → 25 % | 19.1 px | 0.47 | 0.59 | 1181 | quarters: 0.33 → 0.19 → 0.16 → 0.12

Numbers say: light vs heavy: width 21.2 → 38.9 px, dark 0.46 → 0.46.

## Surface test · Oil 0% Paper
Oil 1.00 · 70 px · 25.1 s

![Surface test · Oil 0% Paper](Surface-test-Oil-0-Paper.png)

A light paint: laid on a grey sheet (on white it cannot be seen); **dark** = how far it is from the grey either way.

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 9 % → 9 % | 26.7 px | 0.29 | 1.03 | 191 |
| heavy line | 15 % → 15 % | 44.6 px | 0.36 | 1.00 | 266 |
| pressure swell | 14 % → 14 % | 51.4 px | 0.33 | 1.02 | 206 |
| fast wave | 41 % → 42 % | 47.2 px | 0.30 | 1.03 | 794 |
| slow wave | 39 % → 39 % | 45.4 px | 0.37 | 1.00 | 1137 |
| spiral | 55 % → 55 % | 36.5 px | 0.32 | 1.00 | 1250 |
| loop | 39 % → 39 % | 50.6 px | 0.35 | 1.00 | 625 |
| tilted | 17 % → 17 % | 47.1 px | 0.31 | 1.00 | 855 |
| over the wet one | 32 % → 32 % | 41.9 px | 0.31 | 1.00 | 310 |
| long, no reload | 64 % → 64 % | 28.6 px | 0.30 | 1.00 | 1775 | quarters: 0.00 → 0.00 → 0.00 → 0.00

Numbers say: light vs heavy: width 26.7 → 44.6 px, dark 0.29 → 0.36; the long stroke does not run out of paint.

## Surface test · Oil 40% Paper
Gouache 1.00 + turpentine 40 % · 70 px · 44.3 s

![Surface test · Oil 40% Paper](Surface-test-Oil-40-Paper.png)

A light paint: laid on a grey sheet (on white it cannot be seen); **dark** = how far it is from the grey either way.

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 9 % → 3 % | 26.8 px | 0.40 | 0.29 | 185 |
| heavy line | 15 % → 14 % | 42.3 px | 0.39 | 0.97 | 328 |
| pressure swell | 14 % → 12 % | 53.1 px | 0.38 | 0.85 | 169 |
| fast wave | 39 % → 25 % | 44.7 px | 0.32 | 0.63 | 718 |
| slow wave | 31 % → 20 % | 36.0 px | 0.38 | 0.65 | 1074 |
| spiral | 52 % → 29 % | 34.1 px | 0.36 | 0.56 | 1158 |
| loop | 34 % → 21 % | 43.5 px | 0.36 | 0.62 | 541 |
| tilted | 17 % → 17 % | 46.2 px | 0.35 | 1.02 | 385 |
| over the wet one | 35 % → 29 % | 50.4 px | 0.35 | 0.85 | 245 |
| long, no reload | 51 % → 33 % | 23.0 px | 0.37 | 0.65 | 1391 | quarters: 0.00 → 0.01 → 0.02 → 0.02

Numbers say: light vs heavy: width 26.8 → 42.3 px, dark 0.40 → 0.39; the long stroke does not run out of paint.

## Surface test · Oil 80% Paper
Watercolour 0.93 · Ink 0.07 + turpentine 80 % · 70 px · 40.6 s

![Surface test · Oil 80% Paper](Surface-test-Oil-80-Paper.png)

A light paint: laid on a grey sheet (on white it cannot be seen); **dark** = how far it is from the grey either way.

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 6 % → 8 % | 18.0 px | 0.08 | 1.30 | 132 |
| heavy line | 15 % → 20 % | 44.5 px | 0.09 | 1.34 | 224 |
| pressure swell | 13 % → 16 % | 48.3 px | 0.09 | 1.28 | 136 |
| fast wave | 36 % → 43 % | 41.6 px | 0.10 | 1.19 | 652 |
| slow wave | 32 % → 43 % | 36.9 px | 0.10 | 1.34 | 1064 |
| spiral | 46 % → 59 % | 30.3 px | 0.09 | 1.28 | 1099 |
| loop | 33 % → 40 % | 42.4 px | 0.09 | 1.22 | 508 |
| tilted | 15 % → 16 % | 42.0 px | 0.10 | 1.07 | 315 |
| over the wet one | 32 % → 39 % | 47.5 px | 0.10 | 1.20 | 220 |
| long, no reload | 46 % → 63 % | 20.8 px | 0.09 | 1.37 | 1345 | quarters: 0.09 → 0.09 → 0.05 → 0.03

Numbers say: light vs heavy: width 18.0 → 44.5 px, dark 0.08 → 0.09.

## Surface test · Dry scrub Paper
Gouache 1.00 + turpentine 20 % · 70 px · 35.9 s

![Surface test · Dry scrub Paper](Surface-test-Dry-scrub-Paper.png)

A light paint: laid on a grey sheet (on white it cannot be seen); **dark** = how far it is from the grey either way.

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 13 % → 0 % | 36.5 px | 0.00 | 0.00 | 277 |
| heavy line | 28 % → 2 % | 81.2 px | 0.33 | 0.07 | 312 |
| pressure swell | 18 % → 7 % | 67.0 px | 0.35 | 0.37 | 280 |
| fast wave | 60 % → 18 % | 69.3 px | 0.28 | 0.30 | 944 |
| slow wave | 42 % → 11 % | 48.8 px | 0.32 | 0.26 | 1367 |
| spiral | 67 % → 9 % | 44.3 px | 0.33 | 0.14 | 1536 |
| loop | 44 % → 2 % | 57.5 px | 0.29 | 0.05 | 835 |
| tilted | 16 % → 16 % | 44.0 px | 0.28 | 1.00 | 320 |
| over the wet one | 35 % → 10 % | 52.3 px | 0.28 | 0.30 | 424 |
| long, no reload | 81 % → 18 % | 36.1 px | 0.31 | 0.22 | 1870 | quarters: 0.00 → 0.01 → 0.02 → 0.03

Numbers say: light vs heavy: width 36.5 → 81.2 px, dark 0.00 → 0.33; the long stroke does not run out of paint.

## Surface test · Watercolour Paper
Watercolour 1.00 + water 40 % · 60 px · 33.6 s

![Surface test · Watercolour Paper](Surface-test-Watercolour-Paper.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 8 % → 14 % | 24.1 px | 0.37 | 1.67 | 44 |
| heavy line | 16 % → 19 % | 47.6 px | 0.38 | 1.17 | 158 |
| pressure swell | 10 % → 13 % | 37.5 px | 0.39 | 1.26 | 81 |
| fast wave | 35 % → 39 % | 41.0 px | 0.35 | 1.10 | 233 |
| slow wave | 33 % → 37 % | 37.9 px | 0.36 | 1.14 | 443 |
| spiral | 55 % → 58 % | 36.4 px | 0.31 | 1.05 | 350 |
| loop | 28 % → 32 % | 36.7 px | 0.38 | 1.14 | 243 |
| tilted | 18 % → 18 % | 50.8 px | 0.37 | 1.00 | 187 |
| over the wet one | 30 % → 33 % | 33.2 px | 0.37 | 1.08 | 122 |
| long, no reload | 69 % → 72 % | 31.1 px | 0.30 | 1.04 | 582 | quarters: 0.35 → 0.25 → 0.20 → 0.15

Numbers say: light vs heavy: width 24.1 → 47.6 px, dark 0.37 → 0.38; wet paint spreads well beyond the stroke.

## Surface test · Surface test · paper
Gouache 1.00 + turpentine 40 % · 70 px · 43.6 s

![Surface test · Surface test · paper](Surface-test-Surface-test-paper.png)

A light paint: laid on a grey sheet (on white it cannot be seen); **dark** = how far it is from the grey either way.

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 9 % → 3 % | 26.8 px | 0.40 | 0.29 | 204 |
| heavy line | 15 % → 14 % | 42.3 px | 0.39 | 0.97 | 266 |
| pressure swell | 14 % → 12 % | 53.1 px | 0.38 | 0.85 | 253 |
| fast wave | 39 % → 25 % | 44.7 px | 0.32 | 0.63 | 632 |
| slow wave | 31 % → 20 % | 36.0 px | 0.38 | 0.65 | 1004 |
| spiral | 52 % → 29 % | 34.1 px | 0.36 | 0.56 | 1084 |
| loop | 34 % → 21 % | 43.5 px | 0.36 | 0.62 | 521 |
| tilted | 17 % → 17 % | 46.2 px | 0.35 | 1.02 | 340 |
| over the wet one | 35 % → 29 % | 50.4 px | 0.35 | 0.85 | 241 |
| long, no reload | 51 % → 33 % | 23.0 px | 0.37 | 0.65 | 1522 | quarters: 0.00 → 0.01 → 0.02 → 0.02

Numbers say: light vs heavy: width 26.8 → 42.3 px, dark 0.40 → 0.39; the long stroke does not run out of paint.

## Surface test · Under FineCanvas
Gouache 1.00 + turpentine 30 % · 60 px · 41.0 s

![Surface test · Under FineCanvas](Surface-test-Under-FineCanvas.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 7 % → 1 % | 21.3 px | 0.46 | 0.13 | 157 |
| heavy line | 13 % → 13 % | 39.2 px | 0.46 | 0.95 | 191 |
| pressure swell | 12 % → 10 % | 44.6 px | 0.47 | 0.87 | 156 |
| fast wave | 35 % → 22 % | 41.0 px | 0.49 | 0.62 | 579 |
| slow wave | 30 % → 21 % | 35.1 px | 0.46 | 0.68 | 909 |
| spiral | 58 % → 27 % | 38.6 px | 0.43 | 0.46 | 921 |
| loop | 29 % → 19 % | 37.7 px | 0.46 | 0.67 | 402 |
| tilted | 15 % → 15 % | 42.0 px | 0.49 | 1.01 | 306 |
| over the wet one | 29 % → 26 % | 38.7 px | 0.49 | 0.91 | 209 |
| long, no reload | 46 % → 27 % | 20.6 px | 0.47 | 0.58 | 1320 | quarters: 0.33 → 0.20 → 0.18 → 0.13

Numbers say: light vs heavy: width 21.3 → 39.2 px, dark 0.46 → 0.46.

## Surface test · Oil 0% FineCanvas
Oil 1.00 · 70 px · 26.4 s

![Surface test · Oil 0% FineCanvas](Surface-test-Oil-0-FineCanvas.png)

A light paint: laid on a grey sheet (on white it cannot be seen); **dark** = how far it is from the grey either way.

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 9 % → 10 % | 26.6 px | 0.29 | 1.04 | 211 |
| heavy line | 15 % → 15 % | 44.5 px | 0.36 | 1.00 | 223 |
| pressure swell | 14 % → 14 % | 51.5 px | 0.33 | 1.02 | 257 |
| fast wave | 41 % → 43 % | 47.9 px | 0.31 | 1.03 | 723 |
| slow wave | 40 % → 40 % | 45.7 px | 0.37 | 1.00 | 1207 |
| spiral | 57 % → 57 % | 37.8 px | 0.32 | 1.00 | 1471 |
| loop | 39 % → 39 % | 50.9 px | 0.35 | 1.00 | 583 |
| tilted | 17 % → 17 % | 47.3 px | 0.31 | 1.00 | 451 |
| over the wet one | 32 % → 32 % | 41.9 px | 0.31 | 1.00 | 279 |
| long, no reload | 65 % → 65 % | 29.3 px | 0.31 | 1.00 | 1676 | quarters: 0.00 → 0.00 → 0.00 → 0.00

Numbers say: light vs heavy: width 26.6 → 44.5 px, dark 0.29 → 0.36; the long stroke does not run out of paint.

## Surface test · Oil 40% FineCanvas
Gouache 1.00 + turpentine 40 % · 70 px · 44.5 s

![Surface test · Oil 40% FineCanvas](Surface-test-Oil-40-FineCanvas.png)

A light paint: laid on a grey sheet (on white it cannot be seen); **dark** = how far it is from the grey either way.

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 9 % → 3 % | 27.0 px | 0.41 | 0.29 | 173 |
| heavy line | 15 % → 14 % | 42.1 px | 0.40 | 0.98 | 280 |
| pressure swell | 14 % → 12 % | 53.8 px | 0.38 | 0.85 | 197 |
| fast wave | 39 % → 27 % | 45.5 px | 0.32 | 0.68 | 709 |
| slow wave | 32 % → 21 % | 37.2 px | 0.38 | 0.65 | 1144 |
| spiral | 55 % → 30 % | 36.3 px | 0.36 | 0.55 | 1338 |
| loop | 34 % → 21 % | 44.3 px | 0.36 | 0.62 | 622 |
| tilted | 17 % → 17 % | 47.8 px | 0.36 | 1.00 | 336 |
| over the wet one | 35 % → 30 % | 49.5 px | 0.36 | 0.86 | 364 |
| long, no reload | 55 % → 34 % | 24.5 px | 0.37 | 0.62 | 1492 | quarters: 0.00 → 0.01 → 0.01 → 0.02

Numbers say: light vs heavy: width 27.0 → 42.1 px, dark 0.41 → 0.40; the long stroke does not run out of paint.

## Surface test · Oil 80% FineCanvas
Watercolour 0.93 · Ink 0.07 + turpentine 80 % · 70 px · 41.3 s

![Surface test · Oil 80% FineCanvas](Surface-test-Oil-80-FineCanvas.png)

A light paint: laid on a grey sheet (on white it cannot be seen); **dark** = how far it is from the grey either way.

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 6 % → 8 % | 18.1 px | 0.08 | 1.30 | 273 |
| heavy line | 15 % → 21 % | 44.9 px | 0.09 | 1.34 | 271 |
| pressure swell | 13 % → 17 % | 49.0 px | 0.09 | 1.27 | 220 |
| fast wave | 37 % → 43 % | 42.7 px | 0.10 | 1.16 | 715 |
| slow wave | 34 % → 44 % | 38.8 px | 0.10 | 1.30 | 980 |
| spiral | 49 % → 60 % | 32.3 px | 0.09 | 1.23 | 1699 |
| loop | 34 % → 40 % | 43.4 px | 0.09 | 1.21 | 486 |
| tilted | 16 % → 16 % | 44.2 px | 0.10 | 1.03 | 317 |
| over the wet one | 32 % → 39 % | 45.8 px | 0.10 | 1.21 | 248 |
| long, no reload | 51 % → 65 % | 22.7 px | 0.09 | 1.29 | 1332 | quarters: 0.09 → 0.09 → 0.06 → 0.03

Numbers say: light vs heavy: width 18.1 → 44.9 px, dark 0.08 → 0.09.

## Surface test · Dry scrub FineCanvas
Gouache 1.00 + turpentine 20 % · 70 px · 35.6 s

![Surface test · Dry scrub FineCanvas](Surface-test-Dry-scrub-FineCanvas.png)

A light paint: laid on a grey sheet (on white it cannot be seen); **dark** = how far it is from the grey either way.

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 13 % → 0 % | 36.6 px | 0.00 | 0.00 | 210 |
| heavy line | 28 % → 3 % | 81.3 px | 0.33 | 0.09 | 359 |
| pressure swell | 18 % → 7 % | 68.3 px | 0.35 | 0.38 | 272 |
| fast wave | 61 % → 23 % | 70.6 px | 0.28 | 0.38 | 1522 |
| slow wave | 43 % → 15 % | 49.5 px | 0.32 | 0.36 | 1261 |
| spiral | 69 % → 12 % | 45.3 px | 0.32 | 0.18 | 1379 |
| loop | 44 % → 3 % | 57.5 px | 0.29 | 0.07 | 630 |
| tilted | 16 % → 16 % | 44.5 px | 0.28 | 1.00 | 355 |
| over the wet one | 35 % → 13 % | 52.3 px | 0.28 | 0.36 | 279 |
| long, no reload | 87 % → 19 % | 38.9 px | 0.31 | 0.22 | 1703 | quarters: 0.00 → 0.01 → 0.01 → 0.02

Numbers say: light vs heavy: width 36.6 → 81.3 px, dark 0.00 → 0.33; the long stroke does not run out of paint.

## Surface test · Watercolour FineCanvas
Watercolour 1.00 + water 40 % · 60 px · 32.8 s

![Surface test · Watercolour FineCanvas](Surface-test-Watercolour-FineCanvas.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 8 % → 14 % | 24.2 px | 0.37 | 1.67 | 83 |
| heavy line | 16 % → 19 % | 47.6 px | 0.38 | 1.17 | 121 |
| pressure swell | 10 % → 13 % | 37.6 px | 0.40 | 1.26 | 82 |
| fast wave | 36 % → 40 % | 41.2 px | 0.36 | 1.11 | 311 |
| slow wave | 33 % → 38 % | 38.1 px | 0.37 | 1.16 | 417 |
| spiral | 56 % → 59 % | 36.9 px | 0.32 | 1.05 | 388 |
| loop | 28 % → 33 % | 36.8 px | 0.39 | 1.15 | 196 |
| tilted | 18 % → 18 % | 51.2 px | 0.37 | 1.00 | 141 |
| over the wet one | 30 % → 33 % | 33.1 px | 0.37 | 1.09 | 132 |
| long, no reload | 72 % → 75 % | 32.5 px | 0.31 | 1.04 | 641 | quarters: 0.35 → 0.28 → 0.22 → 0.16

Numbers say: light vs heavy: width 24.2 → 47.6 px, dark 0.37 → 0.38; wet paint spreads well beyond the stroke.

## Surface test · Surface test · fine canvas
Gouache 1.00 + turpentine 40 % · 70 px · 42.4 s

![Surface test · Surface test · fine canvas](Surface-test-Surface-test-fine-canvas.png)

A light paint: laid on a grey sheet (on white it cannot be seen); **dark** = how far it is from the grey either way.

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 9 % → 3 % | 27.0 px | 0.41 | 0.29 | 156 |
| heavy line | 15 % → 14 % | 42.1 px | 0.40 | 0.98 | 229 |
| pressure swell | 14 % → 12 % | 53.8 px | 0.38 | 0.85 | 157 |
| fast wave | 39 % → 27 % | 45.5 px | 0.32 | 0.68 | 613 |
| slow wave | 32 % → 21 % | 37.2 px | 0.38 | 0.65 | 946 |
| spiral | 55 % → 30 % | 36.3 px | 0.36 | 0.55 | 1088 |
| loop | 34 % → 21 % | 44.3 px | 0.36 | 0.62 | 663 |
| tilted | 17 % → 17 % | 47.8 px | 0.36 | 1.00 | 300 |
| over the wet one | 35 % → 30 % | 49.5 px | 0.36 | 0.86 | 305 |
| long, no reload | 55 % → 34 % | 24.5 px | 0.37 | 0.62 | 1335 | quarters: 0.00 → 0.01 → 0.01 → 0.02

Numbers say: light vs heavy: width 27.0 → 42.1 px, dark 0.41 → 0.40; the long stroke does not run out of paint.

## Surface test · Under CoarseLinen
Gouache 1.00 + turpentine 30 % · 60 px · 40.4 s

![Surface test · Under CoarseLinen](Surface-test-Under-CoarseLinen.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 7 % → 1 % | 21.2 px | 0.46 | 0.13 | 157 |
| heavy line | 13 % → 13 % | 39.1 px | 0.46 | 0.95 | 194 |
| pressure swell | 12 % → 10 % | 44.5 px | 0.47 | 0.87 | 144 |
| fast wave | 35 % → 21 % | 40.8 px | 0.49 | 0.60 | 565 |
| slow wave | 30 % → 20 % | 35.0 px | 0.46 | 0.67 | 863 |
| spiral | 57 % → 27 % | 37.6 px | 0.43 | 0.47 | 963 |
| loop | 29 % → 19 % | 37.6 px | 0.46 | 0.66 | 624 |
| tilted | 15 % → 15 % | 41.9 px | 0.49 | 1.01 | 287 |
| over the wet one | 29 % → 26 % | 38.8 px | 0.49 | 0.91 | 224 |
| long, no reload | 45 % → 26 % | 20.2 px | 0.47 | 0.59 | 1191 | quarters: 0.33 → 0.20 → 0.18 → 0.12

Numbers say: light vs heavy: width 21.2 → 39.1 px, dark 0.46 → 0.46.

## Surface test · Oil 0% CoarseLinen
Oil 1.00 · 70 px · 23.8 s

![Surface test · Oil 0% CoarseLinen](Surface-test-Oil-0-CoarseLinen.png)

A light paint: laid on a grey sheet (on white it cannot be seen); **dark** = how far it is from the grey either way.

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 9 % → 9 % | 26.7 px | 0.29 | 1.03 | 185 |
| heavy line | 15 % → 15 % | 44.5 px | 0.36 | 1.00 | 247 |
| pressure swell | 14 % → 14 % | 51.4 px | 0.33 | 1.02 | 187 |
| fast wave | 41 % → 42 % | 47.8 px | 0.31 | 1.03 | 724 |
| slow wave | 40 % → 40 % | 45.7 px | 0.37 | 1.00 | 1090 |
| spiral | 57 % → 57 % | 37.3 px | 0.32 | 1.00 | 1249 |
| loop | 39 % → 39 % | 50.9 px | 0.35 | 1.00 | 611 |
| tilted | 17 % → 17 % | 47.2 px | 0.31 | 1.00 | 740 |
| over the wet one | 32 % → 32 % | 41.9 px | 0.31 | 1.00 | 276 |
| long, no reload | 65 % → 65 % | 29.2 px | 0.31 | 1.00 | 1620 | quarters: 0.00 → 0.00 → 0.00 → 0.00

Numbers say: light vs heavy: width 26.7 → 44.5 px, dark 0.29 → 0.36; the long stroke does not run out of paint.

## Surface test · Oil 40% CoarseLinen
Gouache 1.00 + turpentine 40 % · 70 px · 42.8 s

![Surface test · Oil 40% CoarseLinen](Surface-test-Oil-40-CoarseLinen.png)

A light paint: laid on a grey sheet (on white it cannot be seen); **dark** = how far it is from the grey either way.

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 9 % → 3 % | 27.0 px | 0.41 | 0.29 | 189 |
| heavy line | 15 % → 14 % | 42.2 px | 0.40 | 0.98 | 289 |
| pressure swell | 14 % → 12 % | 53.5 px | 0.38 | 0.86 | 213 |
| fast wave | 39 % → 26 % | 45.4 px | 0.32 | 0.67 | 644 |
| slow wave | 32 % → 21 % | 37.1 px | 0.38 | 0.65 | 1032 |
| spiral | 54 % → 30 % | 35.5 px | 0.36 | 0.56 | 1350 |
| loop | 34 % → 21 % | 44.0 px | 0.36 | 0.62 | 500 |
| tilted | 17 % → 17 % | 47.5 px | 0.36 | 1.01 | 357 |
| over the wet one | 35 % → 30 % | 49.8 px | 0.36 | 0.86 | 259 |
| long, no reload | 54 % → 35 % | 24.0 px | 0.37 | 0.65 | 1530 | quarters: 0.00 → 0.01 → 0.01 → 0.02

Numbers say: light vs heavy: width 27.0 → 42.2 px, dark 0.41 → 0.40; the long stroke does not run out of paint.

## Surface test · Oil 80% CoarseLinen
Watercolour 0.93 · Ink 0.07 + turpentine 80 % · 70 px · 38.5 s

![Surface test · Oil 80% CoarseLinen](Surface-test-Oil-80-CoarseLinen.png)

A light paint: laid on a grey sheet (on white it cannot be seen); **dark** = how far it is from the grey either way.

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 6 % → 8 % | 18.2 px | 0.08 | 1.30 | 173 |
| heavy line | 15 % → 21 % | 44.9 px | 0.09 | 1.34 | 272 |
| pressure swell | 13 % → 17 % | 48.9 px | 0.09 | 1.27 | 155 |
| fast wave | 37 % → 43 % | 42.6 px | 0.10 | 1.16 | 572 |
| slow wave | 33 % → 44 % | 38.4 px | 0.10 | 1.31 | 957 |
| spiral | 48 % → 60 % | 31.7 px | 0.09 | 1.25 | 1146 |
| loop | 33 % → 40 % | 43.2 px | 0.09 | 1.21 | 628 |
| tilted | 16 % → 16 % | 43.7 px | 0.10 | 1.04 | 415 |
| over the wet one | 32 % → 39 % | 46.3 px | 0.10 | 1.21 | 218 |
| long, no reload | 49 % → 65 % | 22.1 px | 0.09 | 1.32 | 1600 | quarters: 0.09 → 0.09 → 0.06 → 0.03

Numbers say: light vs heavy: width 18.2 → 44.9 px, dark 0.08 → 0.09.

## Surface test · Dry scrub CoarseLinen
Gouache 1.00 + turpentine 20 % · 70 px · 35.0 s

![Surface test · Dry scrub CoarseLinen](Surface-test-Dry-scrub-CoarseLinen.png)

A light paint: laid on a grey sheet (on white it cannot be seen); **dark** = how far it is from the grey either way.

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 13 % → 0 % | 36.6 px | 0.00 | 0.00 | 203 |
| heavy line | 28 % → 2 % | 81.3 px | 0.33 | 0.08 | 300 |
| pressure swell | 18 % → 7 % | 68.2 px | 0.35 | 0.37 | 228 |
| fast wave | 61 % → 22 % | 70.3 px | 0.28 | 0.36 | 893 |
| slow wave | 43 % → 14 % | 49.4 px | 0.32 | 0.33 | 1438 |
| spiral | 68 % → 11 % | 45.0 px | 0.32 | 0.16 | 1562 |
| loop | 44 % → 3 % | 57.5 px | 0.29 | 0.07 | 708 |
| tilted | 16 % → 16 % | 44.4 px | 0.28 | 1.00 | 426 |
| over the wet one | 35 % → 12 % | 52.3 px | 0.28 | 0.34 | 370 |
| long, no reload | 85 % → 18 % | 37.9 px | 0.31 | 0.22 | 2370 | quarters: 0.00 → 0.01 → 0.01 → 0.02

Numbers say: light vs heavy: width 36.6 → 81.3 px, dark 0.00 → 0.33; the long stroke does not run out of paint.

## Surface test · Watercolour CoarseLinen
Watercolour 1.00 + water 40 % · 60 px · 31.3 s

![Surface test · Watercolour CoarseLinen](Surface-test-Watercolour-CoarseLinen.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 8 % → 14 % | 24.2 px | 0.37 | 1.67 | 82 |
| heavy line | 16 % → 19 % | 47.7 px | 0.38 | 1.17 | 162 |
| pressure swell | 10 % → 13 % | 37.5 px | 0.40 | 1.26 | 87 |
| fast wave | 36 % → 39 % | 41.1 px | 0.36 | 1.11 | 287 |
| slow wave | 33 % → 38 % | 38.1 px | 0.37 | 1.15 | 648 |
| spiral | 56 % → 58 % | 36.8 px | 0.32 | 1.05 | 566 |
| loop | 28 % → 33 % | 36.8 px | 0.39 | 1.15 | 280 |
| tilted | 18 % → 18 % | 51.1 px | 0.37 | 1.00 | 178 |
| over the wet one | 30 % → 33 % | 33.1 px | 0.37 | 1.09 | 121 |
| long, no reload | 71 % → 74 % | 32.0 px | 0.31 | 1.04 | 775 | quarters: 0.35 → 0.27 → 0.22 → 0.16

Numbers say: light vs heavy: width 24.2 → 47.7 px, dark 0.37 → 0.38; wet paint spreads well beyond the stroke.

## Surface test · Surface test · coarse linen
Gouache 1.00 + turpentine 40 % · 70 px · 42.6 s

![Surface test · Surface test · coarse linen](Surface-test-Surface-test-coarse-linen.png)

A light paint: laid on a grey sheet (on white it cannot be seen); **dark** = how far it is from the grey either way.

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 9 % → 3 % | 27.0 px | 0.41 | 0.29 | 273 |
| heavy line | 15 % → 14 % | 42.2 px | 0.40 | 0.98 | 309 |
| pressure swell | 14 % → 12 % | 53.5 px | 0.38 | 0.86 | 239 |
| fast wave | 39 % → 26 % | 45.4 px | 0.32 | 0.67 | 772 |
| slow wave | 32 % → 21 % | 37.1 px | 0.38 | 0.65 | 1189 |
| spiral | 54 % → 30 % | 35.5 px | 0.36 | 0.56 | 1221 |
| loop | 34 % → 21 % | 44.0 px | 0.36 | 0.62 | 574 |
| tilted | 17 % → 17 % | 47.5 px | 0.36 | 1.01 | 297 |
| over the wet one | 35 % → 30 % | 49.8 px | 0.36 | 0.86 | 257 |
| long, no reload | 54 % → 35 % | 24.0 px | 0.37 | 0.65 | 1286 | quarters: 0.00 → 0.01 → 0.01 → 0.02

Numbers say: light vs heavy: width 27.0 → 42.2 px, dark 0.41 → 0.40; the long stroke does not run out of paint.

## v3 · Any shape · K stamp
Gouache 1.00 · 48 px · 44.4 s

![v3 · Any shape · K stamp](v3-Any-shape-K-stamp.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 20 % → 18 % | 59.0 px | 0.40 | 0.91 | 247 |
| heavy line | 20 % → 19 % | 59.2 px | 0.40 | 0.95 | 270 |
| pressure swell | 12 % → 11 % | 43.7 px | 0.40 | 0.98 | 242 |
| fast wave | 42 % → 34 % | 48.2 px | 0.40 | 0.82 | 609 |
| slow wave | 42 % → 33 % | 48.3 px | 0.40 | 0.80 | 1025 |
| spiral | 66 % → 49 % | 43.6 px | 0.40 | 0.74 | 1449 |
| loop | 37 % → 33 % | 48.2 px | 0.40 | 0.90 | 468 |
| tilted | 15 % → 15 % | 42.0 px | 0.40 | 1.01 | 253 |
| over the wet one | 33 % → 31 % | 51.2 px | 0.40 | 0.94 | 223 |
| long, no reload | 81 % → 51 % | 36.5 px | 0.40 | 0.63 | 1346 | quarters: 0.35 → 0.35 → 0.33 → 0.31

Numbers say: light vs heavy: width 59.0 → 59.2 px, dark 0.40 → 0.40; pressure barely changes the width; the long stroke does not run out of paint.

## v3 · Any shape · K of hairs
Oil 1.00 · 48 px · 16.3 s

![v3 · Any shape · K of hairs](v3-Any-shape-K-of-hairs.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 18 % → 18 % | 51.3 px | 0.40 | 1.00 | 166 |
| heavy line | 27 % → 27 % | 78.5 px | 0.46 | 1.00 | 207 |
| pressure swell | 16 % → 16 % | 58.2 px | 0.47 | 1.01 | 147 |
| fast wave | 49 % → 51 % | 57.1 px | 0.45 | 1.04 | 425 |
| slow wave | 50 % → 50 % | 58.1 px | 0.48 | 1.00 | 802 |
| spiral | 68 % → 68 % | 44.6 px | 0.45 | 1.00 | 957 |
| loop | 46 % → 46 % | 59.0 px | 0.48 | 1.00 | 435 |
| tilted | 16 % → 16 % | 45.9 px | 0.46 | 1.00 | 171 |
| over the wet one | 39 % → 39 % | 62.7 px | 0.46 | 1.01 | 153 |
| long, no reload | 85 % → 85 % | 38.0 px | 0.43 | 1.00 | 957 | quarters: 0.48 → 0.45 → 0.34 → 0.27

Numbers say: light vs heavy: width 51.3 → 78.5 px, dark 0.40 → 0.46.

## v3 · Any shape · Star stamp
Gouache 1.00 · 44 px · 36.8 s

![v3 · Any shape · Star stamp](v3-Any-shape-Star-stamp.png)

A light paint: laid on a grey sheet (on white it cannot be seen); **dark** = how far it is from the grey either way.

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 13 % → 10 % | 37.9 px | 0.36 | 0.79 | 109 |
| heavy line | 13 % → 12 % | 38.5 px | 0.36 | 0.88 | 114 |
| pressure swell | 10 % → 10 % | 39.2 px | 0.36 | 0.93 | 78 |
| fast wave | 33 % → 27 % | 38.0 px | 0.36 | 0.83 | 312 |
| slow wave | 33 % → 26 % | 38.4 px | 0.35 | 0.79 | 455 |
| spiral | 56 % → 42 % | 37.3 px | 0.35 | 0.75 | 428 |
| loop | 28 % → 24 % | 36.0 px | 0.36 | 0.88 | 239 |
| tilted | 13 % → 13 % | 36.9 px | 0.36 | 1.01 | 129 |
| over the wet one | 26 % → 23 % | 36.3 px | 0.36 | 0.89 | 100 |
| long, no reload | 68 % → 47 % | 30.5 px | 0.35 | 0.70 | 666 | quarters: 0.01 → 0.01 → 0.01 → 0.01

Numbers say: light vs heavy: width 37.9 → 38.5 px, dark 0.36 → 0.36; pressure barely changes the width; the long stroke does not run out of paint.

## v3 · Any shape · Star of hairs
Oil 1.00 · 44 px · 14.0 s

![v3 · Any shape · Star of hairs](v3-Any-shape-Star-of-hairs.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 15 % → 15 % | 43.7 px | 0.34 | 1.00 | 123 |
| heavy line | 23 % → 23 % | 68.0 px | 0.32 | 1.00 | 155 |
| pressure swell | 14 % → 14 % | 53.2 px | 0.35 | 1.00 | 106 |
| fast wave | 45 % → 46 % | 52.0 px | 0.32 | 1.01 | 338 |
| slow wave | 44 % → 44 % | 51.0 px | 0.33 | 1.00 | 572 |
| spiral | 64 % → 64 % | 41.9 px | 0.32 | 1.00 | 560 |
| loop | 39 % → 39 % | 50.6 px | 0.34 | 1.00 | 285 |
| tilted | 14 % → 14 % | 39.2 px | 0.34 | 1.00 | 161 |
| over the wet one | 34 % → 34 % | 55.5 px | 0.34 | 1.00 | 138 |
| long, no reload | 79 % → 79 % | 35.3 px | 0.30 | 1.00 | 831 | quarters: 0.32 → 0.29 → 0.24 → 0.17

Numbers say: light vs heavy: width 43.7 → 68.0 px, dark 0.34 → 0.32.

## v3 · Any shape · Rag
Oil 1.00 · 60 px · 20.1 s

![v3 · Any shape · Rag](v3-Any-shape-Rag.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 22 % → 24 % | 62.8 px | 0.16 | 1.12 | 158 |
| heavy line | 38 % → 38 % | 111.4 px | 0.29 | 1.00 | 277 |
| pressure swell | 25 % → 26 % | 93.9 px | 0.23 | 1.02 | 159 |
| fast wave | 68 % → 73 % | 79.1 px | 0.26 | 1.07 | 606 |
| slow wave | 71 % → 71 % | 82.1 px | 0.27 | 1.00 | 1023 |
| spiral | 82 % → 82 % | 53.9 px | 0.28 | 1.00 | 983 |
| loop | 61 % → 61 % | 79.5 px | 0.29 | 1.00 | 488 |
| tilted | 22 % → 22 % | 61.2 px | 0.26 | 1.00 | 262 |
| over the wet one | 51 % → 52 % | 80.3 px | 0.26 | 1.03 | 218 |
| long, no reload | 94 % → 94 % | 42.2 px | 0.29 | 1.00 | 1504 | quarters: 0.35 → 0.32 → 0.27 → 0.21

Numbers say: light vs heavy: width 62.8 → 111.4 px, dark 0.16 → 0.29.

## v3 · Any shape · Dry oil on canvas
Oil 1.00 · 40 px · 13.3 s

![v3 · Any shape · Dry oil on canvas](v3-Any-shape-Dry-oil-on-canvas.png)

A light paint: laid on a grey sheet (on white it cannot be seen); **dark** = how far it is from the grey either way.

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 5 % → 5 % | 13.4 px | 0.14 | 1.00 | 89 |
| heavy line | 8 % → 8 % | 23.6 px | 0.35 | 1.00 | 93 |
| pressure swell | 9 % → 9 % | 32.6 px | 0.27 | 1.00 | 67 |
| fast wave | 27 % → 27 % | 31.8 px | 0.25 | 1.00 | 241 |
| slow wave | 26 % → 26 % | 30.4 px | 0.24 | 1.00 | 411 |
| spiral | 46 % → 46 % | 30.2 px | 0.24 | 1.00 | 446 |
| loop | 21 % → 21 % | 27.4 px | 0.24 | 1.00 | 205 |
| tilted | 9 % → 9 % | 26.5 px | 0.23 | 1.00 | 102 |
| over the wet one | 18 % → 18 % | 23.1 px | 0.23 | 1.00 | 100 |
| long, no reload | 41 % → 41 % | 18.3 px | 0.21 | 1.00 | 539 | quarters: 0.00 → 0.00 → 0.01 → 0.00

Numbers say: light vs heavy: width 13.4 → 23.6 px, dark 0.14 → 0.35; the long stroke does not run out of paint.

## v3 · Any shape · Two colours streaks
Oil 1.00 · 44 px · 14.9 s

![v3 · Any shape · Two colours streaks](v3-Any-shape-Two-colours-streaks.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 14 % → 14 % | 39.7 px | 0.35 | 1.00 | 106 |
| heavy line | 16 % → 16 % | 46.1 px | 0.30 | 1.00 | 114 |
| pressure swell | 11 % → 11 % | 42.7 px | 0.39 | 1.00 | 96 |
| fast wave | 37 % → 37 % | 43.1 px | 0.34 | 1.00 | 318 |
| slow wave | 36 % → 36 % | 41.1 px | 0.30 | 1.00 | 475 |
| spiral | 62 % → 62 % | 40.6 px | 0.35 | 1.00 | 529 |
| loop | 32 % → 32 % | 41.1 px | 0.32 | 1.00 | 286 |
| tilted | 13 % → 13 % | 37.2 px | 0.36 | 1.00 | 169 |
| over the wet one | 27 % → 27 % | 39.1 px | 0.36 | 1.00 | 136 |
| long, no reload | 73 % → 73 % | 32.8 px | 0.32 | 1.00 | 823 | quarters: 0.29 → 0.28 → 0.25 → 0.20

Numbers say: light vs heavy: width 39.7 → 46.1 px, dark 0.35 → 0.30.

## Watercolour · Wash
Watercolour 1.00 + water 65 % · 60 px · 45.6 s

![Watercolour · Wash](Watercolour-Wash.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 15 % → 18 % | 43.3 px | 0.14 | 1.23 | 105 |
| heavy line | 30 % → 30 % | 86.5 px | 0.13 | 1.01 | 206 |
| pressure swell | 18 % → 19 % | 68.1 px | 0.16 | 1.06 | 145 |
| fast wave | 57 % → 59 % | 65.8 px | 0.13 | 1.04 | 489 |
| slow wave | 53 % → 55 % | 61.7 px | 0.14 | 1.02 | 761 |
| spiral | 70 % → 71 % | 46.4 px | 0.11 | 1.01 | 812 |
| loop | 46 % → 48 % | 60.0 px | 0.13 | 1.03 | 388 |
| tilted | 21 % → 21 % | 57.6 px | 0.15 | 1.01 | 454 |
| over the wet one | 42 % → 45 % | 60.4 px | 0.15 | 1.06 | 301 |
| long, no reload | 89 % → 91 % | 39.7 px | 0.09 | 1.03 | 1255 | quarters: 0.14 → 0.11 → 0.07 → 0.04

Numbers say: light vs heavy: width 43.3 → 86.5 px, dark 0.14 → 0.13.

## Watercolour · Wet-in-wet
Watercolour 1.00 + water 80 % · 60 px · 57.6 s

![Watercolour · Wet-in-wet](Watercolour-Wet-in-wet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 13 % → 30 % | 37.6 px | 0.17 | 2.31 | 87 |
| heavy line | 25 % → 38 % | 73.7 px | 0.19 | 1.52 | 173 |
| pressure swell | 16 % → 28 % | 58.1 px | 0.22 | 1.78 | 130 |
| fast wave | 49 % → 73 % | 56.2 px | 0.20 | 1.49 | 430 |
| slow wave | 47 % → 69 % | 54.7 px | 0.22 | 1.46 | 702 |
| spiral | 67 % → 80 % | 44.3 px | 0.18 | 1.19 | 881 |
| loop | 43 % → 60 % | 55.3 px | 0.23 | 1.40 | 554 |
| tilted | 20 % → 21 % | 55.9 px | 0.18 | 1.03 | 240 |
| over the wet one | 40 % → 64 % | 56.1 px | 0.18 | 1.58 | 191 |
| long, no reload | 85 % → 97 % | 37.9 px | 0.18 | 1.15 | 1134 | quarters: 0.31 → 0.22 → 0.15 → 0.09

Numbers say: light vs heavy: width 37.6 → 73.7 px, dark 0.17 → 0.19; wet paint spreads well beyond the stroke.

## Watercolour · Glaze
Watercolour 1.00 + water 75 % · 50 px · 46.4 s

![Watercolour · Glaze](Watercolour-Glaze.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 13 % → 16 % | 38.2 px | 0.03 | 1.25 | 84 |
| heavy line | 26 % → 27 % | 74.7 px | 0.03 | 1.04 | 165 |
| pressure swell | 16 % → 18 % | 60.2 px | 0.03 | 1.09 | 126 |
| fast wave | 50 % → 54 % | 58.2 px | 0.03 | 1.08 | 748 |
| slow wave | 47 % → 50 % | 53.9 px | 0.03 | 1.07 | 607 |
| spiral | 63 % → 67 % | 41.9 px | 0.02 | 1.05 | 744 |
| loop | 42 % → 44 % | 54.2 px | 0.03 | 1.05 | 337 |
| tilted | 17 % → 17 % | 47.1 px | 0.03 | 1.03 | 227 |
| over the wet one | 37 % → 40 % | 57.4 px | 0.03 | 1.08 | 191 |
| long, no reload | 80 % → 87 % | 35.7 px | 0.02 | 1.09 | 1282 | quarters: 0.04 → 0.02 → 0.01 → 0.01

Numbers say: light vs heavy: width 38.2 → 74.7 px, dark 0.03 → 0.03.

## Watercolour · Granulating
Watercolour 1.00 + water 60 % · 56 px · 47.8 s

![Watercolour · Granulating](Watercolour-Granulating.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 14 % → 17 % | 40.6 px | 0.20 | 1.23 | 166 |
| heavy line | 28 % → 28 % | 80.2 px | 0.18 | 1.01 | 319 |
| pressure swell | 17 % → 18 % | 63.0 px | 0.23 | 1.05 | 208 |
| fast wave | 53 % → 55 % | 61.2 px | 0.18 | 1.04 | 491 |
| slow wave | 51 % → 52 % | 59.0 px | 0.19 | 1.03 | 797 |
| spiral | 68 % → 69 % | 44.8 px | 0.15 | 1.01 | 821 |
| loop | 45 % → 46 % | 58.1 px | 0.20 | 1.03 | 404 |
| tilted | 20 % → 20 % | 54.6 px | 0.21 | 1.01 | 274 |
| over the wet one | 40 % → 42 % | 57.6 px | 0.21 | 1.05 | 250 |
| long, no reload | 88 % → 90 % | 39.4 px | 0.15 | 1.02 | 1734 | quarters: 0.22 → 0.17 → 0.11 → 0.06

Numbers say: light vs heavy: width 40.6 → 80.2 px, dark 0.20 → 0.18.

## Watercolour · Dry brush
Watercolour 1.00 + water 35 % · 44 px · 38.9 s

![Watercolour · Dry brush](Watercolour-Dry-brush.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 5 % → 2 % | 15.8 px | 0.01 | 0.29 | 61 |
| heavy line | 20 % → 20 % | 56.8 px | 0.09 | 1.00 | 146 |
| pressure swell | 14 % → 14 % | 51.9 px | 0.08 | 1.02 | 94 |
| fast wave | 47 % → 47 % | 54.1 px | 0.03 | 0.99 | 359 |
| slow wave | 35 % → 35 % | 40.0 px | 0.04 | 1.00 | 598 |
| spiral | 61 % → 62 % | 40.4 px | 0.02 | 1.01 | 690 |
| loop | 32 % → 30 % | 41.6 px | 0.02 | 0.92 | 300 |
| tilted | 11 % → 12 % | 31.3 px | 0.04 | 1.05 | 215 |
| over the wet one | 25 % → 26 % | 38.4 px | 0.04 | 1.04 | 261 |
| long, no reload | 69 % → 64 % | 31.1 px | 0.02 | 0.93 | 908 | quarters: 0.01 → 0.01 → 0.01 → 0.02

Numbers say: light vs heavy: width 15.8 → 56.8 px, dark 0.01 → 0.09; the long stroke does not run out of paint.

## Watercolour · Runs
Watercolour 1.00 + water 80 % · 60 px · 64.7 s

![Watercolour · Runs](Watercolour-Runs.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 26 % → 35 % | 74.7 px | 0.34 | 1.37 | 113 |
| heavy line | 39 % → 42 % | 114.3 px | 0.38 | 1.06 | 224 |
| pressure swell | 17 % → 28 % | 64.3 px | 0.41 | 1.61 | 166 |
| fast wave | 64 % → 74 % | 73.9 px | 0.40 | 1.16 | 630 |
| slow wave | 57 % → 68 % | 65.4 px | 0.42 | 1.21 | 904 |
| spiral | 74 % → 82 % | 48.6 px | 0.42 | 1.12 | 1243 |
| loop | 60 % → 69 % | 78.3 px | 0.41 | 1.14 | 641 |
| tilted | 30 % → 30 % | 82.4 px | 0.37 | 1.02 | 274 |
| over the wet one | 55 % → 67 % | 70.2 px | 0.37 | 1.23 | 188 |
| long, no reload | 90 % → 99 % | 40.5 px | 0.43 | 1.09 | 1209 | quarters: 0.57 → 0.50 → 0.41 → 0.27

Numbers say: light vs heavy: width 74.7 → 114.3 px, dark 0.34 → 0.38; wet paint spreads well beyond the stroke.

## Watercolour · Two-tone
Watercolour 1.00 + water 60 % · 56 px · 57.0 s

![Watercolour · Two-tone](Watercolour-Two-tone.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 15 % → 18 % | 43.8 px | 0.55 | 1.19 | 128 |
| heavy line | 30 % → 30 % | 85.9 px | 0.57 | 1.01 | 267 |
| pressure swell | 18 % → 18 % | 66.0 px | 0.57 | 1.05 | 219 |
| fast wave | 56 % → 58 % | 64.6 px | 0.52 | 1.04 | 573 |
| slow wave | 52 % → 54 % | 60.6 px | 0.56 | 1.02 | 1082 |
| spiral | 69 % → 70 % | 45.7 px | 0.31 | 1.01 | 1235 |
| loop | 47 % → 48 % | 61.1 px | 0.53 | 1.02 | 355 |
| tilted | 19 % → 19 % | 53.0 px | 0.53 | 1.01 | 215 |
| over the wet one | 41 % → 43 % | 61.9 px | 0.53 | 1.05 | 185 |
| long, no reload | 87 % → 90 % | 39.1 px | 0.18 | 1.03 | 1494 | quarters: 0.25 → 0.22 → 0.15 → 0.09

Numbers say: light vs heavy: width 43.8 → 85.9 px, dark 0.55 → 0.57.

## Watercolour · SH blue
Watercolour 1.00 + water 30 % · 46 px · 41.2 s

![Watercolour · SH blue](Watercolour-SH-blue.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 6 % → 13 % | 18.7 px | 0.39 | 1.99 | 74 |
| heavy line | 13 % → 17 % | 37.9 px | 0.41 | 1.29 | 133 |
| pressure swell | 8 % → 12 % | 29.8 px | 0.45 | 1.45 | 78 |
| fast wave | 29 % → 34 % | 33.0 px | 0.45 | 1.20 | 401 |
| slow wave | 26 % → 32 % | 30.0 px | 0.39 | 1.23 | 311 |
| spiral | 44 % → 50 % | 29.0 px | 0.31 | 1.13 | 330 |
| loop | 23 % → 29 % | 29.3 px | 0.41 | 1.27 | 169 |
| tilted | 15 % → 15 % | 42.1 px | 0.39 | 1.00 | 114 |
| over the wet one | 25 % → 29 % | 27.7 px | 0.39 | 1.17 | 107 |
| long, no reload | 59 % → 63 % | 26.4 px | 0.30 | 1.08 | 703 | quarters: 0.31 → 0.23 → 0.17 → 0.12

Numbers say: light vs heavy: width 18.7 → 37.9 px, dark 0.39 → 0.41; wet paint spreads well beyond the stroke.

## Watercolour · SH violet
Watercolour 1.00 + water 30 % · 46 px · 42.5 s

![Watercolour · SH violet](Watercolour-SH-violet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 6 % → 13 % | 18.7 px | 0.59 | 1.99 | 77 |
| heavy line | 13 % → 17 % | 37.9 px | 0.60 | 1.29 | 171 |
| pressure swell | 8 % → 12 % | 29.8 px | 0.62 | 1.45 | 83 |
| fast wave | 29 % → 34 % | 33.0 px | 0.63 | 1.20 | 247 |
| slow wave | 26 % → 32 % | 30.0 px | 0.59 | 1.23 | 335 |
| spiral | 44 % → 50 % | 29.0 px | 0.53 | 1.13 | 361 |
| loop | 23 % → 29 % | 29.3 px | 0.60 | 1.27 | 198 |
| tilted | 15 % → 15 % | 42.1 px | 0.58 | 1.00 | 139 |
| over the wet one | 25 % → 29 % | 27.7 px | 0.58 | 1.17 | 125 |
| long, no reload | 59 % → 63 % | 26.4 px | 0.51 | 1.08 | 690 | quarters: 0.45 → 0.38 → 0.32 → 0.24

Numbers say: light vs heavy: width 18.7 → 37.9 px, dark 0.59 → 0.60; wet paint spreads well beyond the stroke.

## Watercolour · SH teal
Watercolour 1.00 + water 30 % · 46 px · 46.3 s

![Watercolour · SH teal](Watercolour-SH-teal.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 6 % → 13 % | 18.7 px | 0.21 | 1.99 | 51 |
| heavy line | 13 % → 17 % | 37.9 px | 0.22 | 1.29 | 109 |
| pressure swell | 8 % → 12 % | 29.8 px | 0.25 | 1.45 | 65 |
| fast wave | 29 % → 34 % | 33.0 px | 0.25 | 1.20 | 245 |
| slow wave | 26 % → 32 % | 30.0 px | 0.21 | 1.23 | 389 |
| spiral | 44 % → 50 % | 29.0 px | 0.16 | 1.13 | 350 |
| loop | 23 % → 29 % | 29.3 px | 0.22 | 1.27 | 305 |
| tilted | 15 % → 15 % | 42.1 px | 0.21 | 1.00 | 223 |
| over the wet one | 25 % → 29 % | 27.7 px | 0.21 | 1.17 | 173 |
| long, no reload | 59 % → 63 % | 26.4 px | 0.16 | 1.08 | 1256 | quarters: 0.16 → 0.12 → 0.09 → 0.07

Numbers say: light vs heavy: width 18.7 → 37.9 px, dark 0.21 → 0.22; wet paint spreads well beyond the stroke.

## Watercolour · #16 Shrigley strokes
Watercolour 1.00 + water 30 % · 46 px · 50.8 s

![Watercolour · #16 Shrigley strokes](Watercolour-16-Shrigley-strokes.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 6 % → 13 % | 18.7 px | 0.39 | 1.99 | 53 |
| heavy line | 13 % → 17 % | 37.9 px | 0.41 | 1.29 | 119 |
| pressure swell | 8 % → 12 % | 29.8 px | 0.45 | 1.45 | 84 |
| fast wave | 29 % → 34 % | 33.0 px | 0.45 | 1.20 | 359 |
| slow wave | 26 % → 32 % | 30.0 px | 0.39 | 1.23 | 551 |
| spiral | 44 % → 50 % | 29.0 px | 0.31 | 1.13 | 459 |
| loop | 23 % → 29 % | 29.3 px | 0.41 | 1.27 | 439 |
| tilted | 15 % → 15 % | 42.1 px | 0.39 | 1.00 | 181 |
| over the wet one | 25 % → 29 % | 27.7 px | 0.39 | 1.17 | 536 |
| long, no reload | 59 % → 63 % | 26.4 px | 0.30 | 1.08 | 1119 | quarters: 0.31 → 0.23 → 0.17 → 0.12

Numbers say: light vs heavy: width 18.7 → 37.9 px, dark 0.39 → 0.41; wet paint spreads well beyond the stroke.

## Watercolour · #29 Shrigley asterisk
Watercolour 1.00 + water 50 % · 70 px · 69.0 s

![Watercolour · #29 Shrigley asterisk](Watercolour-29-Shrigley-asterisk.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 20 % → 23 % | 57.6 px | 0.60 | 1.15 | 177 |
| heavy line | 39 % → 39 % | 112.5 px | 0.62 | 1.00 | 857 |
| pressure swell | 24 % → 25 % | 88.7 px | 0.61 | 1.06 | 336 |
| fast wave | 68 % → 72 % | 78.7 px | 0.61 | 1.06 | 2255 |
| slow wave | 64 % → 65 % | 74.5 px | 0.62 | 1.01 | 1759 |
| spiral | 77 % → 77 % | 50.8 px | 0.57 | 1.00 | 1691 |
| loop | 57 % → 58 % | 74.3 px | 0.60 | 1.01 | 1042 |
| tilted | 24 % → 24 % | 67.8 px | 0.60 | 1.00 | 505 |
| over the wet one | 53 % → 55 % | 78.8 px | 0.60 | 1.05 | 464 |
| long, no reload | 93 % → 94 % | 41.7 px | 0.55 | 1.01 | 2322 | quarters: 0.57 → 0.56 → 0.54 → 0.46

Numbers say: light vs heavy: width 57.6 → 112.5 px, dark 0.60 → 0.62.

## Watercolour · Pink flame
Watercolour 1.00 + water 80 % · 60 px · 71.5 s

![Watercolour · Pink flame](Watercolour-Pink-flame.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 31 % → 58 % | 88.7 px | 0.04 | 1.91 | 142 |
| heavy line | 35 % → 48 % | 101.7 px | 0.08 | 1.37 | 388 |
| pressure swell | 17 % → 41 % | 62.7 px | 0.08 | 2.48 | 493 |
| fast wave | 64 % → 95 % | 74.3 px | 0.09 | 1.48 | 1027 |
| slow wave | 64 % → 80 % | 74.2 px | 0.09 | 1.24 | 1226 |
| spiral | 77 % → 80 % | 50.5 px | 0.10 | 1.04 | 1567 |
| loop | 56 % → 71 % | 72.8 px | 0.10 | 1.27 | 706 |
| tilted | 29 % → 29 % | 79.8 px | 0.08 | 1.03 | 374 |
| over the wet one | 56 % → 76 % | 77.4 px | 0.08 | 1.35 | 308 |
| long, no reload | 89 % → 95 % | 39.7 px | 0.10 | 1.07 | 1666 | quarters: 0.15 → 0.12 → 0.08 → 0.04

Numbers say: light vs heavy: width 88.7 → 101.7 px, dark 0.04 → 0.08; wet paint spreads well beyond the stroke.

## Watercolour · #33 Red band, pink flames
Watercolour 1.00 + water 60 % · 90 px · 75.1 s

![Watercolour · #33 Red band, pink flames](Watercolour-33-Red-band-pink-flames.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 28 % → 48 % | 82.7 px | 0.43 | 1.70 | 896 |
| heavy line | 45 % → 57 % | 129.7 px | 0.49 | 1.27 | 1046 |
| pressure swell | 27 % → 46 % | 100.3 px | 0.46 | 1.71 | 405 |
| fast wave | 71 % → 86 % | 82.6 px | 0.57 | 1.20 | 1326 |
| slow wave | 72 % → 83 % | 83.7 px | 0.56 | 1.14 | 2421 |
| spiral | 85 % → 95 % | 56.1 px | 0.55 | 1.12 | 2059 |
| loop | 62 % → 79 % | 80.7 px | 0.54 | 1.27 | 965 |
| tilted | 37 % → 39 % | 104.3 px | 0.51 | 1.04 | 561 |
| over the wet one | 66 % → 87 % | 80.3 px | 0.51 | 1.32 | 393 |
| long, no reload | 96 % → 100 % | 42.9 px | 0.59 | 1.04 | 2801 | quarters: 0.66 → 0.64 → 0.61 → 0.49

Numbers say: light vs heavy: width 82.7 → 129.7 px, dark 0.43 → 0.49; wet paint spreads well beyond the stroke.

## Watercolour · #35 Red band with runs
Watercolour 1.00 + water 75 % · 80 px · 74.9 s

![Watercolour · #35 Red band with runs](Watercolour-35-Red-band-with-runs.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 37 % → 51 % | 107.7 px | 0.15 | 1.39 | 323 |
| heavy line | 50 % → 56 % | 145.0 px | 0.30 | 1.11 | 513 |
| pressure swell | 20 % → 33 % | 76.7 px | 0.22 | 1.63 | 309 |
| fast wave | 69 % → 80 % | 79.9 px | 0.36 | 1.16 | 1500 |
| slow wave | 70 % → 78 % | 80.8 px | 0.42 | 1.12 | 2139 |
| spiral | 88 % → 95 % | 57.8 px | 0.16 | 1.08 | 1784 |
| loop | 72 % → 86 % | 93.8 px | 0.35 | 1.18 | 791 |
| tilted | 47 % → 47 % | 129.9 px | 0.31 | 1.01 | 531 |
| over the wet one | 73 % → 86 % | 73.0 px | 0.31 | 1.18 | 480 |
| long, no reload | 94 % → 100 % | 42.4 px | 0.27 | 1.06 | 5507 | quarters: 0.41 → 0.32 → 0.23 → 0.13

Numbers say: light vs heavy: width 107.7 → 145.0 px, dark 0.15 → 0.30; wet paint spreads well beyond the stroke.

## Watercolour · Sepia wash
Watercolour 1.00 + water 60 % · 80 px · 68.1 s

![Watercolour · Sepia wash](Watercolour-Sepia-wash.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 18 % → 36 % | 53.2 px | 0.19 | 1.94 | 196 |
| heavy line | 34 % → 45 % | 98.0 px | 0.20 | 1.34 | 442 |
| pressure swell | 21 % → 33 % | 76.9 px | 0.21 | 1.61 | 336 |
| fast wave | 62 % → 82 % | 72.0 px | 0.24 | 1.32 | 1128 |
| slow wave | 60 % → 76 % | 69.6 px | 0.23 | 1.26 | 1604 |
| spiral | 76 % → 85 % | 50.2 px | 0.21 | 1.12 | 1616 |
| loop | 54 % → 66 % | 69.9 px | 0.24 | 1.23 | 741 |
| tilted | 26 % → 27 % | 72.6 px | 0.22 | 1.04 | 546 |
| over the wet one | 51 % → 74 % | 70.8 px | 0.22 | 1.45 | 508 |
| long, no reload | 94 % → 99 % | 42.3 px | 0.23 | 1.05 | 2302 | quarters: 0.34 → 0.26 → 0.20 → 0.14

Numbers say: light vs heavy: width 53.2 → 98.0 px, dark 0.19 → 0.20; wet paint spreads well beyond the stroke.

## Watercolour · #40 Olive and sepia blooms
Watercolour 1.00 + water 55 % · 90 px · 69.1 s

![Watercolour · #40 Olive and sepia blooms](Watercolour-40-Olive-and-sepia-blooms.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 20 % → 38 % | 59.3 px | 0.19 | 1.86 | 264 |
| heavy line | 37 % → 48 % | 107.5 px | 0.21 | 1.29 | 531 |
| pressure swell | 23 % → 37 % | 87.2 px | 0.22 | 1.59 | 295 |
| fast wave | 67 % → 86 % | 77.7 px | 0.25 | 1.28 | 982 |
| slow wave | 66 % → 80 % | 76.0 px | 0.24 | 1.22 | 1718 |
| spiral | 79 % → 88 % | 52.2 px | 0.22 | 1.11 | 1743 |
| loop | 58 % → 69 % | 74.7 px | 0.25 | 1.19 | 1143 |
| tilted | 29 % → 30 % | 81.1 px | 0.22 | 1.04 | 548 |
| over the wet one | 57 % → 79 % | 77.9 px | 0.22 | 1.39 | 495 |
| long, no reload | 96 % → 99 % | 43.0 px | 0.23 | 1.04 | 4925 | quarters: 0.34 → 0.28 → 0.21 → 0.15

Numbers say: light vs heavy: width 59.3 → 107.5 px, dark 0.19 → 0.21; wet paint spreads well beyond the stroke.

## Watercolour · #46 Lips on wet paper
Watercolour 1.00 + water 65 % · 50 px · 55.7 s

![Watercolour · #46 Lips on wet paper](Watercolour-46-Lips-on-wet-paper.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 11 % → 28 % | 32.3 px | 0.61 | 2.48 | 105 |
| heavy line | 22 % → 35 % | 64.7 px | 0.64 | 1.56 | 231 |
| pressure swell | 13 % → 25 % | 49.9 px | 0.63 | 1.86 | 213 |
| fast wave | 44 % → 68 % | 50.6 px | 0.65 | 1.56 | 490 |
| slow wave | 41 % → 64 % | 47.8 px | 0.65 | 1.54 | 740 |
| spiral | 64 % → 77 % | 42.2 px | 0.67 | 1.20 | 1032 |
| loop | 37 % → 56 % | 47.7 px | 0.66 | 1.51 | 431 |
| tilted | 18 % → 19 % | 50.4 px | 0.62 | 1.05 | 264 |
| over the wet one | 36 % → 58 % | 50.8 px | 0.62 | 1.59 | 173 |
| long, no reload | 79 % → 96 % | 35.5 px | 0.66 | 1.21 | 1577 | quarters: 0.72 → 0.71 → 0.67 → 0.57

Numbers say: light vs heavy: width 32.3 → 64.7 px, dark 0.61 → 0.64; wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #01 Henry Ward peach cloud — own sheet
own sheet 600 × 600 · Gouache 1.00 · 44 px · 18.0 s

![Brush Artist · Refs · #01 Henry Ward peach cloud — own sheet](Brush-Artist-Refs-01-Henry-Ward-peach-cloud-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 5 % → 16 % | 15.6 px | 0.53 | 2.97 | 206 |
| stroke 2 | 11 % → 29 % | 35.1 px | 0.54 | 2.71 | 183 |
| stroke 3 | 16 % → 31 % | 45.4 px | 0.54 | 2.00 | 217 |
| stroke 4 | 21 % → 34 % | 68.0 px | 0.54 | 1.63 | 239 |
| stroke 5 | 21 % → 31 % | 60.5 px | 0.54 | 1.48 | 175 |
| stroke 6 | 20 % → 24 % | 61.5 px | 0.54 | 1.21 | 150 |
| stroke 7 | 9 % → 33 % | 22.9 px | 0.53 | 3.58 | 161 |
| stroke 8 | 14 % → 32 % | 34.7 px | 0.53 | 2.28 | 186 |
| stroke 9 | 13 % → 33 % | 33.9 px | 0.53 | 2.47 | 155 |
| stroke 10 | 13 % → 34 % | 35.3 px | 0.53 | 2.57 | 134 |
| stroke 11 | 14 % → 36 % | 40.5 px | 0.54 | 2.53 | 174 |
| stroke 12 | 14 % → 39 % | 42.4 px | 0.54 | 2.76 | 118 |
| stroke 13 | 19 % → 42 % | 54.8 px | 0.54 | 2.23 | 181 |
| stroke 14 | 27 % → 44 % | 77.4 px | 0.54 | 1.63 | 198 |
| stroke 15 | 30 % → 48 % | 88.5 px | 0.53 | 1.60 | 200 |
| stroke 16 | 35 % → 48 % | 104.8 px | 0.53 | 1.39 | 240 |
| stroke 17 | 35 % → 50 % | 98.5 px | 0.53 | 1.41 | 184 |
| stroke 18 | 41 % → 49 % | 117.6 px | 0.53 | 1.21 | 260 |
| stroke 19 | 41 % → 49 % | 116.0 px | 0.54 | 1.18 | 356 |
| stroke 20 | 43 % → 46 % | 123.0 px | 0.54 | 1.07 | 378 |
| stroke 21 | 43 % → 42 % | 125.4 px | 0.54 | 0.96 | 238 |
| stroke 22 | 45 % → 42 % | 131.2 px | 0.54 | 0.94 | 222 |
| stroke 23 | 49 % → 43 % | 139.0 px | 0.54 | 0.88 | 212 |
| stroke 24 | 52 % → 45 % | 156.2 px | 0.54 | 0.86 | 141 |

Numbers say: wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #02 Henry Ward cream strokes — own sheet
own sheet 600 × 600 · Gouache 1.00 · 46 px · 14.0 s

![Brush Artist · Refs · #02 Henry Ward cream strokes — own sheet](Brush-Artist-Refs-02-Henry-Ward-cream-strokes-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 9 % → 2 % | 17.7 px | 0.65 | 0.26 | 304 |
| stroke 2 | 15 % → 6 % | 39.4 px | 0.66 | 0.41 | 458 |
| stroke 3 | 19 % → 22 % | 48.9 px | 0.64 | 1.15 | 309 |
| stroke 4 | 23 % → 22 % | 56.7 px | 0.64 | 0.97 | 308 |
| stroke 5 | 24 % → 27 % | 59.0 px | 0.64 | 1.11 | 301 |
| stroke 6 | 18 % → 16 % | 43.4 px | 0.64 | 0.88 | 269 |
| stroke 7 | 21 % → 10 % | 53.1 px | 0.64 | 0.48 | 273 |

## Brush Artist · Refs · #03 Henry Ward navy contours — own sheet
own sheet 600 × 600 · Impasto 1.00 · 22 px · 5.6 s

![Brush Artist · Refs · #03 Henry Ward navy contours — own sheet](Brush-Artist-Refs-03-Henry-Ward-navy-contours-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 10 % → 15 % | 20.0 px | 0.70 | 1.51 | 174 |
| stroke 2 | 16 % → 19 % | 22.1 px | 0.70 | 1.19 | 198 |
| stroke 3 | 20 % → 20 % | 29.5 px | 0.71 | 0.99 | 260 |
| stroke 4 | 19 % → 17 % | 43.6 px | 0.71 | 0.89 | 452 |

Numbers say: wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #04 Henry Ward grey cloud — own sheet
own sheet 600 × 600 · Gouache 1.00 · 50 px · 15.7 s

![Brush Artist · Refs · #04 Henry Ward grey cloud — own sheet](Brush-Artist-Refs-04-Henry-Ward-grey-cloud-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 5 % → 21 % | 15.7 px | 0.32 | 3.88 | 359 |
| stroke 2 | 14 % → 21 % | 40.2 px | 0.31 | 1.53 | 326 |
| stroke 3 | 21 % → 22 % | 59.7 px | 0.31 | 1.05 | 658 |
| stroke 4 | 27 % → 23 % | 79.5 px | 0.31 | 0.84 | 949 |
| stroke 5 | 27 % → 26 % | 83.3 px | 0.31 | 0.94 | 392 |
| stroke 6 | 33 % → 30 % | 109.0 px | 0.31 | 0.89 | 318 |
| stroke 7 | 34 % → 36 % | 100.8 px | 0.30 | 1.03 | 358 |
| stroke 8 | 38 % → 38 % | 112.6 px | 0.30 | 0.99 | 613 |
| stroke 9 | 32 % → 39 % | 94.9 px | 0.31 | 1.23 | 330 |
| stroke 10 | 33 % → 39 % | 106.9 px | 0.31 | 1.19 | 262 |
| stroke 11 | 34 % → 36 % | 96.9 px | 0.31 | 1.05 | 443 |
| stroke 12 | 32 % → 34 % | 96.3 px | 0.30 | 1.06 | 558 |
| stroke 13 | 27 % → 38 % | 78.1 px | 0.31 | 1.38 | 401 |
| stroke 14 | 34 % → 38 % | 100.7 px | 0.31 | 1.11 | 508 |
| stroke 15 | 35 % → 37 % | 100.1 px | 0.31 | 1.07 | 376 |
| stroke 16 | 38 % → 36 % | 116.5 px | 0.31 | 0.93 | 328 |
| stroke 17 | 39 % → 31 % | 112.7 px | 0.31 | 0.79 | 282 |
| stroke 18 | 40 % → 28 % | 133.2 px | 0.31 | 0.70 | 201 |
| stroke 19 | 38 % → 24 % | 113.0 px | 0.32 | 0.63 | 240 |
| stroke 20 | 40 % → 23 % | 125.2 px | 0.32 | 0.57 | 220 |

Numbers say: wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #05 Henry Ward green in rust loops — own sheet
own sheet 600 × 600 · Impasto 1.00 · 20 px · 4.8 s

![Brush Artist · Refs · #05 Henry Ward green in rust loops — own sheet](Brush-Artist-Refs-05-Henry-Ward-green-in-rust-loops-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 11 % → 16 % | 19.1 px | 0.02 | 1.49 | 177 |
| stroke 2 | 12 % → 10 % | 24.0 px | 0.02 | 0.86 | 275 |
| stroke 3 | 20 % → 17 % | 35.4 px | 0.02 | 0.89 | 337 |

## Brush Artist · Refs · #06 Henry Ward scrubbed grey — own sheet
own sheet 600 × 600 · Gouache 1.00 · 50 px · 14.2 s

![Brush Artist · Refs · #06 Henry Ward scrubbed grey — own sheet](Brush-Artist-Refs-06-Henry-Ward-scrubbed-grey-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 6 % → 24 % | 15.9 px | 0.32 | 3.69 | 309 |
| stroke 2 | 16 % → 25 % | 41.5 px | 0.31 | 1.58 | 462 |
| stroke 3 | 21 % → 23 % | 64.7 px | 0.31 | 1.10 | 262 |
| stroke 4 | 25 % → 24 % | 78.0 px | 0.31 | 0.96 | 357 |
| stroke 5 | 31 % → 30 % | 92.8 px | 0.31 | 0.97 | 397 |
| stroke 6 | 38 % → 31 % | 115.7 px | 0.31 | 0.81 | 650 |
| stroke 7 | 36 % → 35 % | 103.6 px | 0.31 | 0.98 | 471 |
| stroke 8 | 40 % → 36 % | 125.1 px | 0.31 | 0.90 | 327 |
| stroke 9 | 35 % → 37 % | 107.6 px | 0.31 | 1.06 | 379 |
| stroke 10 | 34 % → 38 % | 111.3 px | 0.31 | 1.10 | 358 |
| stroke 11 | 35 % → 37 % | 101.5 px | 0.31 | 1.06 | 336 |
| stroke 12 | 33 % → 35 % | 99.4 px | 0.31 | 1.08 | 201 |
| stroke 13 | 24 % → 37 % | 69.3 px | 0.31 | 1.53 | 184 |
| stroke 14 | 30 % → 39 % | 88.5 px | 0.31 | 1.30 | 262 |
| stroke 15 | 33 % → 44 % | 95.1 px | 0.32 | 1.34 | 195 |
| stroke 16 | 35 % → 45 % | 111.8 px | 0.32 | 1.28 | 209 |
| stroke 17 | 37 % → 42 % | 110.5 px | 0.32 | 1.12 | 191 |
| stroke 18 | 41 % → 40 % | 123.6 px | 0.32 | 0.98 | 202 |
| stroke 19 | 38 % → 35 % | 112.0 px | 0.32 | 0.93 | 194 |
| stroke 20 | 38 % → 34 % | 117.9 px | 0.32 | 0.90 | 235 |
| stroke 21 | 40 % → 30 % | 116.2 px | 0.33 | 0.75 | 271 |
| stroke 22 | 39 % → 28 % | 127.1 px | 0.33 | 0.73 | 198 |

Numbers say: wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #07 Henry Ward blue L + black zigzag — own sheet
own sheet 600 × 600 · Impasto 1.00 · 34 px · 2.8 s

![Brush Artist · Refs · #07 Henry Ward blue L + black zigzag — own sheet](Brush-Artist-Refs-07-Henry-Ward-blue-L-black-zigzag-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 13 % → 15 % | 31.2 px | 0.58 | 1.09 | 176 |
| stroke 2 | 15 % → 14 % | 37.7 px | 0.58 | 0.90 | 162 |

## Brush Artist · Refs · #08 Henry Ward olive bands — own sheet
own sheet 600 × 600 · Gouache 1.00 · 34 px · 5.1 s

![Brush Artist · Refs · #08 Henry Ward olive bands — own sheet](Brush-Artist-Refs-08-Henry-Ward-olive-bands-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 8 % → 4 % | 15.7 px | 0.58 | 0.53 | 128 |
| stroke 2 | 12 % → 4 % | 28.0 px | 0.58 | 0.35 | 160 |
| stroke 3 | 13 % → 11 % | 27.5 px | 0.58 | 0.87 | 152 |
| stroke 4 | 17 % → 10 % | 37.3 px | 0.58 | 0.57 | 197 |
| stroke 5 | 22 % → 13 % | 45.2 px | 0.56 | 0.59 | 199 |
| stroke 6 | 16 % → 6 % | 30.5 px | 0.54 | 0.40 | 212 |

## Brush Artist · Refs · #09 Henry Ward white loops — own sheet
own sheet 600 × 600 · Gouache 1.00 · 46 px · 6.8 s

![Brush Artist · Refs · #09 Henry Ward white loops — own sheet](Brush-Artist-Refs-09-Henry-Ward-white-loops-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 23 % → 0 % | 12.1 px | 0.06 | 0.00 | 836 |
| stroke 2 | 27 % → 0 % | 27.4 px | 0.07 | 0.00 | 985 |
| stroke 3 | 34 % → 0 % | 31.4 px | 0.07 | 0.00 | 900 |
| stroke 4 | 8 % → 0 % | 18.4 px | 0.00 | 0.00 | 174 |
| stroke 5 | 5 % → 0 % | 14.8 px | 0.06 | 0.00 | 176 |
| stroke 6 | 5 % → 0 % | 13.8 px | 0.08 | 0.00 | 173 |
| stroke 7 | 10 % → 0 % | 26.8 px | 0.08 | 0.00 | 179 |
| stroke 8 | 5 % → 0 % | 8.2 px | 0.00 | 0.00 | 212 |

## Brush Artist · Refs · #10 Henry Ward maroon loops — own sheet
own sheet 600 × 600 · Impasto 1.00 · 30 px · 3.1 s

![Brush Artist · Refs · #10 Henry Ward maroon loops — own sheet](Brush-Artist-Refs-10-Henry-Ward-maroon-loops-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 12 % → 26 % | 28.9 px | 0.72 | 2.25 | 216 |
| stroke 2 | 23 % → 39 % | 51.0 px | 0.72 | 1.74 | 121 |
| stroke 3 | 30 % → 36 % | 59.6 px | 0.72 | 1.20 | 175 |
| stroke 4 | 40 % → 38 % | 91.4 px | 0.72 | 0.94 | 131 |
| stroke 5 | 33 % → 29 % | 82.1 px | 0.71 | 0.89 | 155 |

Numbers say: wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #11 Henry Ward purple spun balls — own sheet
own sheet 600 × 600 · Impasto 1.00 · 36 px · 3.3 s

![Brush Artist · Refs · #11 Henry Ward purple spun balls — own sheet](Brush-Artist-Refs-11-Henry-Ward-purple-spun-balls-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 22 % → 31 % | 24.4 px | 0.69 | 1.42 | 221 |
| stroke 2 | 31 % → 44 % | 34.3 px | 0.69 | 1.39 | 219 |
| stroke 3 | 34 % → 33 % | 37.7 px | 0.69 | 0.97 | 253 |

## Brush Artist · Refs · #12 Henry Ward black-olive cage — own sheet
own sheet 600 × 600 · Gouache 1.00 · 28 px · 5.9 s

![Brush Artist · Refs · #12 Henry Ward black-olive cage — own sheet](Brush-Artist-Refs-12-Henry-Ward-black-olive-cage-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 9 % → 10 % | 17.0 px | 0.58 | 1.15 | 222 |
| stroke 2 | 7 % → 10 % | 15.8 px | 0.58 | 1.46 | 208 |
| stroke 3 | 18 % → 13 % | 28.0 px | 0.58 | 0.72 | 249 |
| stroke 4 | 20 % → 14 % | 39.4 px | 0.59 | 0.70 | 338 |
| stroke 5 | 18 % → 7 % | 33.8 px | 0.58 | 0.40 | 216 |
| stroke 6 | 29 % → 15 % | 54.8 px | 0.58 | 0.52 | 214 |

## Brush Artist · Refs · #13 Henry Ward blue streaky form — own sheet
own sheet 600 × 600 · Gouache 1.00 · 50 px · 9.3 s

![Brush Artist · Refs · #13 Henry Ward blue streaky form — own sheet](Brush-Artist-Refs-13-Henry-Ward-blue-streaky-form-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 5 % → 0 % | 15.9 px | 0.00 | 0.00 | 184 |
| stroke 2 | 13 % → 0 % | 40.6 px | 0.00 | 0.00 | 221 |
| stroke 3 | 22 % → 0 % | 62.3 px | 0.00 | 0.00 | 197 |
| stroke 4 | 24 % → 0 % | 78.4 px | 0.00 | 0.00 | 215 |
| stroke 5 | 31 % → 0 % | 90.1 px | 0.00 | 0.00 | 234 |
| stroke 6 | 37 % → 0 % | 105.3 px | 0.00 | 0.00 | 297 |
| stroke 7 | 36 % → 0 % | 107.2 px | 0.00 | 0.00 | 230 |
| stroke 8 | 40 % → 0 % | 120.3 px | 0.00 | 0.00 | 278 |
| stroke 9 | 33 % → 0 % | 102.9 px | 0.00 | 0.00 | 225 |
| stroke 10 | 32 % → 0 % | 105.4 px | 0.00 | 0.00 | 217 |
| stroke 11 | 30 % → 0 % | 92.1 px | 0.00 | 0.00 | 194 |
| stroke 12 | 26 % → 0 % | 78.3 px | 0.00 | 0.00 | 168 |
| stroke 13 | 24 % → 0 % | 74.8 px | 0.00 | 0.00 | 162 |
| stroke 14 | 29 % → 0 % | 84.9 px | 0.00 | 0.00 | 256 |
| stroke 15 | 30 % → 0 % | 86.3 px | 0.00 | 0.00 | 170 |
| stroke 16 | 35 % → 0 % | 104.8 px | 0.00 | 0.00 | 223 |
| stroke 17 | 41 % → 0 % | 103.0 px | 0.00 | 0.00 | 177 |
| stroke 18 | 49 % → 0 % | 117.7 px | 0.00 | 0.00 | 198 |
| stroke 19 | 51 % → 0 % | 104.2 px | 0.00 | 0.00 | 198 |
| stroke 20 | 60 % → 0 % | 115.5 px | 0.00 | 0.00 | 228 |
| stroke 21 | 7 % → 0 % | 15.0 px | 0.00 | 0.00 | 167 |
| stroke 22 | 6 % → 0 % | 18.5 px | 0.00 | 0.00 | 188 |
| stroke 23 | 11 % → 0 % | 35.1 px | 0.00 | 0.00 | 165 |
| stroke 24 | 4 % → 0 % | 11.0 px | 0.00 | 0.00 | 147 |
| stroke 25 | 4 % → 0 % | 9.1 px | 0.00 | 0.00 | 165 |

## Brush Artist · Refs · #14 Henry Ward olive totem — own sheet
own sheet 600 × 600 · Impasto 1.00 · 48 px · 7.2 s

![Brush Artist · Refs · #14 Henry Ward olive totem — own sheet](Brush-Artist-Refs-14-Henry-Ward-olive-totem-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 18 % → 46 % | 46.6 px | 0.38 | 2.57 | 146 |
| stroke 2 | 20 % → 50 % | 61.7 px | 0.38 | 2.53 | 176 |
| stroke 3 | 27 % → 52 % | 93.9 px | 0.39 | 1.89 | 197 |
| stroke 4 | 30 % → 54 % | 110.9 px | 0.39 | 1.82 | 148 |
| stroke 5 | 38 % → 63 % | 134.1 px | 0.39 | 1.64 | 162 |
| stroke 6 | 38 % → 64 % | 149.8 px | 0.39 | 1.67 | 168 |
| stroke 7 | 35 % → 60 % | 119.1 px | 0.39 | 1.70 | 141 |
| stroke 8 | 37 % → 62 % | 141.6 px | 0.39 | 1.67 | 268 |
| stroke 9 | 38 % → 62 % | 131.6 px | 0.39 | 1.64 | 161 |
| stroke 10 | 37 % → 61 % | 136.5 px | 0.39 | 1.65 | 177 |
| stroke 11 | 38 % → 64 % | 136.7 px | 0.39 | 1.66 | 134 |
| stroke 12 | 38 % → 64 % | 143.5 px | 0.38 | 1.68 | 145 |
| stroke 13 | 37 % → 66 % | 129.3 px | 0.39 | 1.78 | 126 |
| stroke 14 | 36 % → 61 % | 131.1 px | 0.39 | 1.70 | 165 |
| stroke 15 | 39 % → 65 % | 134.4 px | 0.39 | 1.66 | 128 |
| stroke 16 | 38 % → 63 % | 136.6 px | 0.39 | 1.67 | 148 |
| stroke 17 | 37 % → 61 % | 124.1 px | 0.39 | 1.64 | 183 |
| stroke 18 | 40 % → 65 % | 152.2 px | 0.39 | 1.63 | 138 |
| stroke 19 | 38 % → 58 % | 131.3 px | 0.39 | 1.54 | 124 |
| stroke 20 | 40 % → 53 % | 142.6 px | 0.39 | 1.31 | 155 |
| stroke 21 | 46 % → 53 % | 136.0 px | 0.39 | 1.15 | 124 |
| stroke 22 | 53 % → 51 % | 143.0 px | 0.39 | 0.97 | 137 |

Numbers say: wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #15 Ultramarine brush script — own sheet
own sheet 600 × 600 · Ink 1.00 · 4 px · 8.1 s

![Brush Artist · Refs · #15 Ultramarine brush script — own sheet](Brush-Artist-Refs-15-Ultramarine-brush-script-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 40 % → 42 % | 9.0 px | 0.65 | 1.05 | 38 |
| stroke 2 | 41 % → 43 % | 9.0 px | 0.67 | 1.07 | 47 |
| stroke 3 | 39 % → 42 % | 9.4 px | 0.72 | 1.08 | 38 |
| stroke 4 | 42 % → 46 % | 10.2 px | 0.74 | 1.10 | 21 |
| stroke 5 | 46 % → 49 % | 10.1 px | 0.72 | 1.06 | 36 |
| stroke 6 | 43 % → 45 % | 9.7 px | 0.65 | 1.05 | 57 |
| stroke 7 | 44 % → 47 % | 9.3 px | 0.72 | 1.08 | 25 |
| stroke 8 | 37 % → 39 % | 8.9 px | 0.65 | 1.06 | 50 |
| stroke 9 | 39 % → 42 % | 9.1 px | 0.70 | 1.07 | 48 |
| stroke 10 | 35 % → 37 % | 9.6 px | 0.66 | 1.05 | 42 |
| stroke 11 | 44 % → 47 % | 9.9 px | 0.69 | 1.06 | 35 |
| stroke 12 | 39 % → 41 % | 9.4 px | 0.65 | 1.06 | 42 |
| stroke 13 | 45 % → 46 % | 10.1 px | 0.69 | 1.04 | 28 |
| stroke 14 | 37 % → 40 % | 9.6 px | 0.71 | 1.07 | 24 |
| stroke 15 | 37 % → 38 % | 9.0 px | 0.67 | 1.05 | 37 |
| stroke 16 | 42 % → 45 % | 9.4 px | 0.70 | 1.06 | 23 |
| stroke 17 | 41 % → 45 % | 7.1 px | 0.71 | 1.09 | 41 |
| stroke 18 | 43 % → 45 % | 9.3 px | 0.73 | 1.05 | 19 |
| stroke 19 | 40 % → 42 % | 9.0 px | 0.65 | 1.06 | 42 |
| stroke 20 | 42 % → 44 % | 9.7 px | 0.69 | 1.06 | 34 |
| stroke 21 | 39 % → 42 % | 9.6 px | 0.69 | 1.07 | 31 |
| stroke 22 | 44 % → 46 % | 8.9 px | 0.65 | 1.06 | 48 |
| stroke 23 | 38 % → 42 % | 9.5 px | 0.72 | 1.10 | 27 |
| stroke 24 | 39 % → 42 % | 9.1 px | 0.73 | 1.06 | 32 |
| stroke 25 | 41 % → 44 % | 10.0 px | 0.71 | 1.06 | 30 |
| stroke 26 | 45 % → 47 % | 9.1 px | 0.66 | 1.04 | 37 |
| stroke 27 | 43 % → 45 % | 9.0 px | 0.62 | 1.05 | 68 |
| stroke 28 | 45 % → 47 % | 9.3 px | 0.70 | 1.06 | 44 |
| stroke 29 | 35 % → 38 % | 10.4 px | 0.69 | 1.08 | 28 |
| stroke 30 | 39 % → 40 % | 8.5 px | 0.70 | 1.04 | 32 |
| stroke 31 | 43 % → 46 % | 10.4 px | 0.74 | 1.07 | 24 |
| stroke 32 | 41 % → 45 % | 9.3 px | 0.70 | 1.09 | 25 |
| stroke 33 | 35 % → 40 % | 10.9 px | 0.73 | 1.13 | 45 |
| stroke 34 | 41 % → 45 % | 10.1 px | 0.74 | 1.09 | 28 |
| stroke 35 | 36 % → 38 % | 9.4 px | 0.67 | 1.06 | 47 |

## Brush Artist · Refs · #18 Blue oil-stick scribbles — own sheet
own sheet 600 × 600 · Pastel 1.00 · 10 px · 2.9 s

![Brush Artist · Refs · #18 Blue oil-stick scribbles — own sheet](Brush-Artist-Refs-18-Blue-oil-stick-scribbles-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 16 % → 32 % | 3.9 px | 0.49 | 2.03 | 113 |
| stroke 2 | 13 % → 37 % | 3.6 px | 0.49 | 2.75 | 145 |
| stroke 3 | 16 % → 26 % | 5.8 px | 0.49 | 1.64 | 165 |
| stroke 4 | 15 % → 29 % | 7.9 px | 0.49 | 1.91 | 179 |
| stroke 5 | 29 % → 34 % | 8.5 px | 0.49 | 1.18 | 138 |
| stroke 6 | 26 % → 26 % | 9.4 px | 0.49 | 1.02 | 131 |
| stroke 7 | 26 % → 32 % | 8.4 px | 0.49 | 1.24 | 153 |
| stroke 8 | 30 % → 30 % | 17.0 px | 0.49 | 1.00 | 174 |

Numbers say: wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #20 Orange-red crayon scribble — own sheet
own sheet 600 × 600 · Pastel 1.00 · 14 px · 2.7 s

![Brush Artist · Refs · #20 Orange-red crayon scribble — own sheet](Brush-Artist-Refs-20-Orange-red-crayon-scribble-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 8 % → 19 % | 5.5 px | 0.59 | 2.47 | 175 |
| stroke 2 | 9 % → 22 % | 6.6 px | 0.60 | 2.50 | 145 |
| stroke 3 | 13 % → 21 % | 8.3 px | 0.60 | 1.65 | 153 |
| stroke 4 | 24 % → 32 % | 8.8 px | 0.60 | 1.36 | 161 |
| stroke 5 | 28 % → 28 % | 7.9 px | 0.59 | 1.00 | 144 |
| stroke 6 | 22 % → 22 % | 16.4 px | 0.60 | 1.00 | 154 |

Numbers say: wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #21 Gritty black contours — own sheet
own sheet 600 × 600 · Gouache 1.00 · 12 px · 3.8 s

![Brush Artist · Refs · #21 Gritty black contours — own sheet](Brush-Artist-Refs-21-Gritty-black-contours-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 6 % → 4 % | 6.2 px | 0.36 | 0.68 | 142 |
| stroke 2 | 5 % → 2 % | 7.9 px | 0.36 | 0.47 | 171 |
| stroke 3 | 9 % → 2 % | 7.8 px | 0.37 | 0.17 | 118 |
| stroke 4 | 9 % → 3 % | 10.9 px | 0.36 | 0.36 | 133 |
| stroke 5 | 10 % → 4 % | 12.7 px | 0.35 | 0.35 | 86 |

## Brush Artist · Refs · #22 Bold black brush poster — own sheet
own sheet 600 × 600 · Ink 1.00 · 20 px · 5.0 s

![Brush Artist · Refs · #22 Bold black brush poster — own sheet](Brush-Artist-Refs-22-Bold-black-brush-poster-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 24 % → 28 % | 38.8 px | 0.95 | 1.18 | 103 |
| stroke 2 | 28 % → 39 % | 42.9 px | 0.94 | 1.38 | 27 |
| stroke 3 | 30 % → 30 % | 46.0 px | 0.94 | 1.00 | 46 |
| stroke 4 | 30 % → 41 % | 57.8 px | 0.94 | 1.41 | 65 |
| stroke 5 | 27 % → 27 % | 46.3 px | 0.93 | 1.00 | 85 |

## Brush Artist · Refs · #23 Dry white on orange + black line — own sheet
own sheet 600 × 600 · Gouache 1.00 · 50 px · 8.4 s

![Brush Artist · Refs · #23 Dry white on orange + black line — own sheet](Brush-Artist-Refs-23-Dry-white-on-orange-black-line-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 4 % → 11 % | 14.5 px | 0.38 | 2.70 | 114 |
| stroke 2 | 8 % → 10 % | 26.7 px | 0.38 | 1.35 | 142 |
| stroke 3 | 13 % → 11 % | 49.0 px | 0.38 | 0.81 | 135 |
| stroke 4 | 17 % → 12 % | 68.6 px | 0.38 | 0.67 | 146 |
| stroke 5 | 23 % → 13 % | 85.0 px | 0.38 | 0.55 | 149 |
| stroke 6 | 26 % → 14 % | 106.9 px | 0.38 | 0.53 | 140 |
| stroke 7 | 23 % → 13 % | 86.4 px | 0.38 | 0.57 | 131 |
| stroke 8 | 22 % → 12 % | 87.4 px | 0.38 | 0.53 | 144 |
| stroke 9 | 19 % → 11 % | 69.7 px | 0.38 | 0.60 | 126 |
| stroke 10 | 18 % → 11 % | 68.9 px | 0.38 | 0.63 | 123 |
| stroke 11 | 20 % → 11 % | 73.3 px | 0.38 | 0.56 | 144 |
| stroke 12 | 19 % → 12 % | 72.9 px | 0.38 | 0.65 | 125 |
| stroke 13 | 20 % → 14 % | 75.6 px | 0.38 | 0.70 | 129 |
| stroke 14 | 21 % → 14 % | 84.0 px | 0.38 | 0.64 | 213 |
| stroke 15 | 21 % → 13 % | 79.6 px | 0.38 | 0.62 | 147 |
| stroke 16 | 22 % → 11 % | 87.4 px | 0.38 | 0.52 | 190 |
| stroke 17 | 22 % → 9 % | 76.2 px | 0.38 | 0.40 | 186 |
| stroke 18 | 27 % → 9 % | 99.3 px | 0.38 | 0.34 | 176 |

Numbers say: wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #24 Picasso flat oil — own sheet
own sheet 600 × 600 · Oil 0.89 · Oil glaze 0.11 · 34 px · 5.6 s

![Brush Artist · Refs · #24 Picasso flat oil — own sheet](Brush-Artist-Refs-24-Picasso-flat-oil-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 14 % → 44 % | 30.0 px | 0.22 | 3.11 | 135 |
| stroke 2 | 19 % → 47 % | 44.5 px | 0.23 | 2.49 | 124 |
| stroke 3 | 27 % → 56 % | 59.7 px | 0.23 | 2.06 | 138 |
| stroke 4 | 37 % → 62 % | 82.9 px | 0.23 | 1.69 | 146 |
| stroke 5 | 41 % → 68 % | 91.2 px | 0.22 | 1.64 | 149 |
| stroke 6 | 42 % → 63 % | 96.5 px | 0.22 | 1.52 | 140 |
| stroke 7 | 42 % → 63 % | 87.5 px | 0.23 | 1.51 | 121 |
| stroke 8 | 42 % → 63 % | 101.6 px | 0.23 | 1.50 | 132 |
| stroke 9 | 34 % → 60 % | 74.4 px | 0.23 | 1.76 | 126 |
| stroke 10 | 38 % → 58 % | 89.8 px | 0.23 | 1.55 | 137 |
| stroke 11 | 35 % → 56 % | 74.6 px | 0.24 | 1.61 | 133 |
| stroke 12 | 37 % → 58 % | 88.3 px | 0.24 | 1.56 | 142 |
| stroke 13 | 35 % → 64 % | 77.9 px | 0.25 | 1.81 | 135 |
| stroke 14 | 36 % → 66 % | 82.0 px | 0.24 | 1.82 | 184 |
| stroke 15 | 36 % → 60 % | 76.0 px | 0.24 | 1.67 | 184 |
| stroke 16 | 36 % → 52 % | 83.2 px | 0.24 | 1.46 | 222 |
| stroke 17 | 41 % → 47 % | 86.1 px | 0.24 | 1.15 | 176 |
| stroke 18 | 42 % → 42 % | 101.0 px | 0.24 | 1.00 | 199 |

Numbers say: wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #25 Yellow heavy flat stroke — own sheet
own sheet 600 × 600 · Impasto 1.00 · 110 px · 3.1 s

![Brush Artist · Refs · #25 Yellow heavy flat stroke — own sheet](Brush-Artist-Refs-25-Yellow-heavy-flat-stroke-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 18 % → 18 % | 103.7 px | 0.16 | 0.98 | 651 |

## Brush Artist · Refs · #27 Orange impasto swatch — own sheet
own sheet 600 × 600 · Impasto 1.00 · 60 px · 3.4 s

![Brush Artist · Refs · #27 Orange impasto swatch — own sheet](Brush-Artist-Refs-27-Orange-impasto-swatch-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 8 % → 21 % | 58.4 px | 0.32 | 2.66 | 65 |
| stroke 2 | 7 % → 33 % | 62.2 px | 0.32 | 4.61 | 49 |
| stroke 3 | 25 % → 34 % | 238.0 px | 0.32 | 1.41 | 41 |
| stroke 4 | 10 % → 12 % | 69.5 px | 0.34 | 1.26 | 70 |
| stroke 5 | 17 % → 32 % | 61.8 px | 0.31 | 1.90 | 65 |
| stroke 6 | 17 % → 31 % | 143.7 px | 0.32 | 1.77 | 61 |
| stroke 7 | 8 % → 14 % | 68.6 px | 0.31 | 1.88 | 45 |
| stroke 8 | 32 % → 33 % | 328.8 px | 0.32 | 1.04 | 52 |
| stroke 9 | 37 % → 36 % | 182.9 px | 0.32 | 0.97 | 69 |
| stroke 10 | 33 % → 32 % | 298.6 px | 0.32 | 0.97 | 53 |

Numbers say: wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #28 Miles Davis black lines — own sheet
own sheet 600 × 600 · Ink 1.00 · 22 px · 6.4 s

![Brush Artist · Refs · #28 Miles Davis black lines — own sheet](Brush-Artist-Refs-28-Miles-Davis-black-lines-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 22 % → 31 % | 36.1 px | 0.88 | 1.42 | 163 |
| stroke 2 | 26 % → 47 % | 35.8 px | 0.88 | 1.79 | 154 |
| stroke 3 | 38 % → 42 % | 73.3 px | 0.88 | 1.11 | 104 |
| stroke 4 | 41 % → 47 % | 81.4 px | 0.88 | 1.16 | 231 |
| stroke 5 | 54 % → 54 % | 108.2 px | 0.88 | 1.00 | 167 |

Numbers say: wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #29 Shrigley magenta asterisk — own sheet
own sheet 600 × 600 · Watercolour 1.00 · 70 px · 7.0 s

![Brush Artist · Refs · #29 Shrigley magenta asterisk — own sheet](Brush-Artist-Refs-29-Shrigley-magenta-asterisk-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 13 % → 37 % | 46.6 px | 0.67 | 2.86 | 232 |
| stroke 2 | 12 % → 12 % | 87.1 px | 0.67 | 1.00 | 212 |
| stroke 3 | 28 % → 37 % | 100.9 px | 0.67 | 1.31 | 204 |
| stroke 4 | 23 % → 23 % | 164.0 px | 0.67 | 1.02 | 204 |

Numbers say: wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #30 Red gouache face patch — own sheet
own sheet 600 × 600 · Gouache 1.00 · 60 px · 13.8 s

![Brush Artist · Refs · #30 Red gouache face patch — own sheet](Brush-Artist-Refs-30-Red-gouache-face-patch-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 11 % → 37 % | 50.6 px | 0.54 | 3.29 | 160 |
| stroke 2 | 15 % → 41 % | 74.2 px | 0.54 | 2.74 | 166 |
| stroke 3 | 24 % → 50 % | 115.1 px | 0.54 | 2.08 | 314 |
| stroke 4 | 26 % → 52 % | 133.4 px | 0.54 | 1.95 | 340 |
| stroke 5 | 34 % → 60 % | 160.6 px | 0.54 | 1.77 | 227 |
| stroke 6 | 35 % → 61 % | 178.6 px | 0.54 | 1.76 | 230 |
| stroke 7 | 35 % → 59 % | 164.2 px | 0.54 | 1.70 | 237 |
| stroke 8 | 34 % → 56 % | 162.3 px | 0.54 | 1.66 | 278 |
| stroke 9 | 36 % → 60 % | 172.7 px | 0.53 | 1.66 | 212 |
| stroke 10 | 38 % → 62 % | 196.7 px | 0.53 | 1.64 | 201 |
| stroke 11 | 37 % → 61 % | 181.6 px | 0.53 | 1.67 | 193 |
| stroke 12 | 36 % → 58 % | 179.8 px | 0.53 | 1.60 | 214 |
| stroke 13 | 33 % → 46 % | 157.0 px | 0.53 | 1.38 | 202 |
| stroke 14 | 33 % → 41 % | 159.9 px | 0.53 | 1.24 | 252 |
| stroke 15 | 33 % → 37 % | 153.6 px | 0.53 | 1.12 | 287 |
| stroke 16 | 39 % → 39 % | 186.3 px | 0.53 | 0.98 | 279 |

Numbers say: wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #31 Warhol blotted line — own sheet
own sheet 600 × 600 · Ink 1.00 · 6 px · 5.6 s

![Brush Artist · Refs · #31 Warhol blotted line — own sheet](Brush-Artist-Refs-31-Warhol-blotted-line-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 22 % → 43 % | 16.5 px | 0.83 | 1.94 | 87 |
| stroke 2 | 17 % → 23 % | 15.7 px | 0.81 | 1.35 | 80 |
| stroke 3 | 24 % → 25 % | 24.9 px | 0.81 | 1.03 | 85 |
| stroke 4 | 32 % → 41 % | 32.7 px | 0.83 | 1.28 | 51 |
| stroke 5 | 37 % → 45 % | 38.1 px | 0.83 | 1.21 | 70 |
| stroke 6 | 34 % → 35 % | 27.8 px | 0.81 | 1.03 | 89 |

Numbers say: wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #32 Thick orange swipes — own sheet
own sheet 600 × 600 · Impasto 1.00 · 90 px · 4.3 s

![Brush Artist · Refs · #32 Thick orange swipes — own sheet](Brush-Artist-Refs-32-Thick-orange-swipes-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 14 % → 27 % | 86.6 px | 0.02 | 1.89 | 363 |
| stroke 2 | 26 % → 37 % | 177.9 px | 0.02 | 1.41 | 375 |
| stroke 3 | 27 % → 27 % | 176.1 px | 0.02 | 0.98 | 459 |

Numbers say: wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #33 Red wet-in-wet band — own sheet
own sheet 600 × 600 · Watercolour 1.00 · 80 px · 11.9 s

![Brush Artist · Refs · #33 Red wet-in-wet band — own sheet](Brush-Artist-Refs-33-Red-wet-in-wet-band-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 22 % → 57 % | 83.4 px | 0.61 | 2.61 | 489 |
| stroke 2 | 28 % → 51 % | 228.4 px | 0.62 | 1.82 | 116 |
| stroke 3 | 34 % → 53 % | 330.0 px | 0.61 | 1.57 | 158 |
| stroke 4 | 40 % → 60 % | 389.9 px | 0.62 | 1.51 | 102 |
| stroke 5 | 40 % → 55 % | 339.4 px | 0.61 | 1.38 | 162 |
| stroke 6 | 41 % → 48 % | 310.3 px | 0.59 | 1.18 | 146 |

Numbers say: wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #34 Magenta oil patches — own sheet
own sheet 600 × 600 · Oil 0.89 · Oil glaze 0.11 · 60 px · 4.3 s

![Brush Artist · Refs · #34 Magenta oil patches — own sheet](Brush-Artist-Refs-34-Magenta-oil-patches-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 8 % → 39 % | 57.1 px | 0.13 | 4.77 | 121 |
| stroke 2 | 8 % → 28 % | 56.8 px | 0.14 | 3.32 | 84 |
| stroke 3 | 7 % → 32 % | 58.6 px | 0.13 | 4.60 | 92 |
| stroke 4 | 15 % → 19 % | 122.2 px | 0.12 | 1.26 | 60 |
| stroke 5 | 21 % → 30 % | 112.2 px | 0.13 | 1.45 | 122 |
| stroke 6 | 19 % → 36 % | 159.7 px | 0.13 | 1.91 | 111 |
| stroke 7 | 28 % → 33 % | 226.6 px | 0.13 | 1.17 | 132 |
| stroke 8 | 30 % → 37 % | 213.6 px | 0.13 | 1.21 | 131 |
| stroke 9 | 23 % → 25 % | 147.9 px | 0.14 | 1.07 | 114 |
| stroke 10 | 27 % → 27 % | 240.6 px | 0.14 | 1.00 | 84 |
| stroke 11 | 33 % → 33 % | 297.2 px | 0.13 | 1.00 | 83 |
| stroke 12 | 24 % → 24 % | 173.6 px | 0.13 | 1.00 | 69 |

Numbers say: wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #35 Red band with runs — own sheet
own sheet 600 × 600 · Watercolour 1.00 · 70 px · 9.2 s

![Brush Artist · Refs · #35 Red band with runs — own sheet](Brush-Artist-Refs-35-Red-band-with-runs-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 37 % → 47 % | 140.3 px | 0.45 | 1.27 | 337 |

## Brush Artist · Refs · #36 Magenta letters flat brush — own sheet
own sheet 600 × 600 · Gouache 1.00 · 36 px · 12.4 s

![Brush Artist · Refs · #36 Magenta letters flat brush — own sheet](Brush-Artist-Refs-36-Magenta-letters-flat-brush-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 20 % → 38 % | 58.3 px | 0.50 | 1.95 | 39 |
| stroke 2 | 20 % → 31 % | 45.2 px | 0.51 | 1.54 | 38 |
| stroke 3 | 28 % → 52 % | 84.6 px | 0.50 | 1.83 | 43 |
| stroke 4 | 26 % → 44 % | 50.3 px | 0.51 | 1.69 | 147 |
| stroke 5 | 33 % → 54 % | 96.3 px | 0.50 | 1.63 | 85 |
| stroke 6 | 43 % → 56 % | 246.0 px | 0.49 | 1.30 | 27 |
| stroke 7 | 30 % → 43 % | 56.6 px | 0.50 | 1.43 | 246 |
| stroke 8 | 31 % → 52 % | 97.7 px | 0.51 | 1.66 | 110 |
| stroke 9 | 38 % → 50 % | 158.2 px | 0.51 | 1.31 | 27 |
| stroke 10 | 37 % → 62 % | 107.5 px | 0.50 | 1.68 | 120 |
| stroke 11 | 39 % → 61 % | 225.6 px | 0.49 | 1.55 | 23 |
| stroke 12 | 44 % → 55 % | 82.9 px | 0.50 | 1.26 | 127 |
| stroke 13 | 31 % → 45 % | 113.5 px | 0.51 | 1.43 | 37 |
| stroke 14 | 34 % → 50 % | 129.9 px | 0.51 | 1.47 | 40 |
| stroke 15 | 36 % → 54 % | 105.5 px | 0.50 | 1.49 | 81 |
| stroke 16 | 39 % → 47 % | 221.7 px | 0.50 | 1.23 | 30 |
| stroke 17 | 43 % → 51 % | 81.6 px | 0.50 | 1.18 | 151 |
| stroke 18 | 26 % → 35 % | 95.6 px | 0.50 | 1.34 | 66 |
| stroke 19 | 39 % → 37 % | 112.8 px | 0.50 | 0.97 | 66 |
| stroke 20 | 45 % → 44 % | 129.9 px | 0.51 | 0.98 | 79 |
| stroke 21 | 40 % → 38 % | 78.2 px | 0.50 | 0.94 | 156 |

Numbers say: wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #37 Oil still life dabs — own sheet
own sheet 600 × 600 · Oil 0.89 · Oil glaze 0.11 · 40 px · 3.2 s

![Brush Artist · Refs · #37 Oil still life dabs — own sheet](Brush-Artist-Refs-37-Oil-still-life-dabs-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 6 % → 6 % | 38.2 px | 0.37 | 1.00 | 35 |
| stroke 2 | 6 % → 26 % | 39.8 px | 0.40 | 4.69 | 23 |
| stroke 3 | 11 % → 33 % | 86.6 px | 0.39 | 3.00 | 19 |
| stroke 4 | 8 % → 8 % | 39.3 px | 0.37 | 1.00 | 47 |
| stroke 5 | 6 % → 10 % | 43.2 px | 0.38 | 1.67 | 29 |
| stroke 6 | 13 % → 29 % | 80.2 px | 0.40 | 2.26 | 39 |
| stroke 7 | 11 % → 22 % | 113.9 px | 0.38 | 2.08 | 26 |
| stroke 8 | 8 % → 13 % | 85.3 px | 0.38 | 1.59 | 18 |
| stroke 9 | 12 % → 13 % | 61.1 px | 0.36 | 1.12 | 45 |
| stroke 10 | 20 % → 24 % | 100.4 px | 0.40 | 1.20 | 74 |
| stroke 11 | 23 % → 27 % | 194.4 px | 0.41 | 1.15 | 48 |
| stroke 12 | 20 % → 20 % | 212.5 px | 0.39 | 1.00 | 41 |
| stroke 13 | 15 % → 15 % | 150.5 px | 0.42 | 1.00 | 69 |
| stroke 14 | 15 % → 15 % | 121.2 px | 0.38 | 1.00 | 36 |

Numbers say: wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #38 Sanguine drawing — own sheet
own sheet 600 × 600 · Pastel 1.00 · 6 px · 2.6 s

![Brush Artist · Refs · #38 Sanguine drawing — own sheet](Brush-Artist-Refs-38-Sanguine-drawing-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 3 % → 15 % | 3.3 px | 0.57 | 4.99 | 12 |
| stroke 2 | 3 % → 8 % | 2.9 px | 0.57 | 3.03 | 6 |
| stroke 3 | 3 % → 9 % | 3.3 px | 0.57 | 3.13 | 13 |
| stroke 4 | 2 % → 18 % | 2.8 px | 0.57 | 7.17 | 4 |
| stroke 5 | 3 % → 7 % | 2.9 px | 0.57 | 2.87 | 16 |
| stroke 6 | 3 % → 19 % | 3.5 px | 0.57 | 6.36 | 7 |
| stroke 7 | 5 % → 15 % | 5.3 px | 0.57 | 3.13 | 9 |
| stroke 8 | 4 % → 16 % | 4.8 px | 0.57 | 3.71 | 4 |
| stroke 9 | 3 % → 8 % | 3.4 px | 0.57 | 2.52 | 4 |
| stroke 10 | 4 % → 16 % | 4.9 px | 0.57 | 3.75 | 8 |
| stroke 11 | 3 % → 4 % | 3.0 px | 0.57 | 1.63 | 4 |
| stroke 12 | 4 % → 16 % | 4.7 px | 0.57 | 3.75 | 5 |
| stroke 13 | 8 % → 18 % | 9.2 px | 0.57 | 2.20 | 12 |
| stroke 14 | 5 % → 14 % | 5.3 px | 0.57 | 2.95 | 9 |
| stroke 15 | 9 % → 18 % | 10.7 px | 0.57 | 1.88 | 8 |
| stroke 16 | 6 % → 16 % | 7.0 px | 0.57 | 2.64 | 5 |
| stroke 17 | 4 % → 9 % | 5.0 px | 0.57 | 2.12 | 4 |
| stroke 18 | 3 % → 5 % | 3.1 px | 0.57 | 1.89 | 6 |
| stroke 19 | 6 % → 17 % | 7.4 px | 0.57 | 2.68 | 16 |
| stroke 20 | 9 % → 14 % | 9.8 px | 0.57 | 1.66 | 18 |
| stroke 21 | 4 % → 4 % | 4.6 px | 0.57 | 1.00 | 6 |
| stroke 22 | 8 % → 14 % | 9.2 px | 0.57 | 1.71 | 9 |
| stroke 23 | 8 % → 12 % | 8.7 px | 0.57 | 1.63 | 16 |
| stroke 24 | 4 % → 8 % | 5.0 px | 0.57 | 1.72 | 6 |
| stroke 25 | 8 % → 15 % | 9.3 px | 0.57 | 1.87 | 20 |
| stroke 26 | 6 % → 8 % | 6.9 px | 0.57 | 1.32 | 22 |
| stroke 27 | 4 % → 5 % | 4.8 px | 0.57 | 1.07 | 19 |
| stroke 28 | 8 % → 13 % | 8.9 px | 0.57 | 1.61 | 14 |
| stroke 29 | 8 % → 17 % | 9.0 px | 0.57 | 2.18 | 8 |
| stroke 30 | 13 % → 17 % | 15.2 px | 0.57 | 1.29 | 5 |
| stroke 31 | 5 % → 7 % | 6.0 px | 0.57 | 1.24 | 6 |
| stroke 32 | 11 % → 14 % | 12.9 px | 0.57 | 1.23 | 7 |
| stroke 33 | 8 % → 9 % | 9.5 px | 0.57 | 1.06 | 19 |
| stroke 34 | 11 % → 14 % | 12.3 px | 0.57 | 1.34 | 6 |
| stroke 35 | 9 % → 15 % | 10.7 px | 0.57 | 1.57 | 32 |
| stroke 36 | 10 % → 13 % | 11.9 px | 0.57 | 1.26 | 8 |
| stroke 37 | 10 % → 16 % | 11.4 px | 0.57 | 1.63 | 11 |
| stroke 38 | 14 % → 20 % | 15.3 px | 0.57 | 1.46 | 15 |
| stroke 39 | 14 % → 17 % | 16.5 px | 0.57 | 1.20 | 5 |
| stroke 40 | 6 % → 7 % | 7.3 px | 0.57 | 1.15 | 7 |
| stroke 41 | 16 % → 16 % | 18.2 px | 0.57 | 1.01 | 5 |
| stroke 42 | 14 % → 16 % | 16.1 px | 0.57 | 1.15 | 5 |
| stroke 43 | 11 % → 13 % | 13.0 px | 0.57 | 1.16 | 7 |
| stroke 44 | 13 % → 16 % | 15.2 px | 0.57 | 1.19 | 5 |
| stroke 45 | 2 % → 2 % | 2.8 px | 0.56 | 1.00 | 6 |
| stroke 46 | 17 % → 17 % | 18.9 px | 0.57 | 1.00 | 6 |
| stroke 47 | 14 % → 14 % | 15.9 px | 0.57 | 1.00 | 7 |
| stroke 48 | 13 % → 14 % | 14.7 px | 0.57 | 1.06 | 7 |
| stroke 49 | 19 % → 19 % | 21.8 px | 0.57 | 1.00 | 10 |
| stroke 50 | 11 % → 11 % | 12.2 px | 0.57 | 1.00 | 13 |

Numbers say: wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #39 Very thick impasto — own sheet
own sheet 600 × 600 · Impasto 1.00 · 60 px · 5.5 s

![Brush Artist · Refs · #39 Very thick impasto — own sheet](Brush-Artist-Refs-39-Very-thick-impasto-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 24 % → 35 % | 55.6 px | 0.43 | 1.44 | 612 |
| stroke 2 | 30 % → 46 % | 91.2 px | 0.43 | 1.52 | 325 |
| stroke 3 | 37 % → 48 % | 123.1 px | 0.44 | 1.31 | 333 |
| stroke 4 | 31 % → 43 % | 90.2 px | 0.43 | 1.39 | 381 |
| stroke 5 | 41 % → 39 % | 102.0 px | 0.43 | 0.97 | 334 |

Numbers say: wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #40 Watercolour blooms — own sheet
own sheet 600 × 600 · Watercolour 1.00 · 90 px · 9.2 s

![Brush Artist · Refs · #40 Watercolour blooms — own sheet](Brush-Artist-Refs-40-Watercolour-blooms-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 21 % → 27 % | 92.8 px | 0.12 | 1.28 | 862 |

## Brush Artist · Refs · #41 Coloured pencil hatching — own sheet
own sheet 600 × 600 · Pastel 1.00 · 4 px · 3.5 s

![Brush Artist · Refs · #41 Coloured pencil hatching — own sheet](Brush-Artist-Refs-41-Coloured-pencil-hatching-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 3 % → 15 % | 2.3 px | 0.35 | 5.04 | 3 |
| stroke 2 | 3 % → 8 % | 2.5 px | 0.35 | 2.34 | 9 |
| stroke 3 | 3 % → 12 % | 2.2 px | 0.35 | 4.03 | 3 |
| stroke 4 | 3 % → 20 % | 2.4 px | 0.35 | 6.35 | 3 |
| stroke 5 | 4 % → 8 % | 3.5 px | 0.35 | 1.78 | 7 |
| stroke 6 | 3 % → 14 % | 2.3 px | 0.35 | 4.57 | 6 |
| stroke 7 | 4 % → 17 % | 3.0 px | 0.35 | 4.34 | 5 |
| stroke 8 | 3 % → 13 % | 2.4 px | 0.35 | 4.14 | 6 |
| stroke 9 | 5 % → 12 % | 4.1 px | 0.35 | 2.18 | 5 |
| stroke 10 | 6 % → 17 % | 4.4 px | 0.35 | 2.92 | 3 |
| stroke 11 | 4 % → 14 % | 3.2 px | 0.35 | 3.38 | 2 |
| stroke 12 | 3 % → 3 % | 2.2 px | 0.35 | 1.00 | 5 |
| stroke 13 | 8 % → 19 % | 6.0 px | 0.35 | 2.35 | 2 |
| stroke 14 | 4 % → 15 % | 2.7 px | 0.35 | 4.14 | 5 |
| stroke 15 | 6 % → 13 % | 4.6 px | 0.35 | 2.12 | 2 |
| stroke 16 | 7 % → 12 % | 5.6 px | 0.35 | 1.63 | 4 |
| stroke 17 | 3 % → 3 % | 2.4 px | 0.35 | 1.00 | 12 |
| stroke 18 | 5 % → 9 % | 4.0 px | 0.36 | 1.63 | 9 |
| stroke 19 | 5 % → 14 % | 4.0 px | 0.35 | 2.72 | 5 |
| stroke 20 | 6 % → 16 % | 4.2 px | 0.35 | 2.94 | 3 |
| stroke 21 | 5 % → 15 % | 3.6 px | 0.35 | 3.13 | 17 |
| stroke 22 | 10 % → 18 % | 7.7 px | 0.35 | 1.77 | 5 |
| stroke 23 | 10 % → 15 % | 7.2 px | 0.35 | 1.54 | 8 |
| stroke 24 | 7 % → 15 % | 5.3 px | 0.35 | 2.12 | 6 |
| stroke 25 | 5 % → 12 % | 4.0 px | 0.35 | 2.27 | 9 |
| stroke 26 | 4 % → 7 % | 3.1 px | 0.35 | 1.79 | 4 |
| stroke 27 | 3 % → 8 % | 2.6 px | 0.35 | 2.35 | 2 |
| stroke 28 | 7 % → 11 % | 5.2 px | 0.36 | 1.68 | 10 |
| stroke 29 | 3 % → 15 % | 2.6 px | 0.35 | 4.48 | 6 |
| stroke 30 | 7 % → 10 % | 5.2 px | 0.35 | 1.40 | 2 |
| stroke 31 | 7 % → 16 % | 5.8 px | 0.35 | 2.09 | 5 |
| stroke 32 | 3 % → 6 % | 2.4 px | 0.36 | 1.93 | 11 |
| stroke 33 | 8 % → 13 % | 5.9 px | 0.35 | 1.65 | 7 |
| stroke 34 | 3 % → 6 % | 2.6 px | 0.35 | 1.71 | 4 |
| stroke 35 | 7 % → 15 % | 5.4 px | 0.35 | 2.11 | 5 |
| stroke 36 | 5 % → 5 % | 4.0 px | 0.35 | 1.01 | 4 |
| stroke 37 | 8 % → 16 % | 5.9 px | 0.35 | 2.07 | 2 |
| stroke 38 | 8 % → 14 % | 6.2 px | 0.35 | 1.71 | 8 |
| stroke 39 | 7 % → 12 % | 5.4 px | 0.35 | 1.65 | 5 |
| stroke 40 | 9 % → 20 % | 6.7 px | 0.36 | 2.23 | 10 |
| stroke 41 | 10 % → 15 % | 7.7 px | 0.35 | 1.46 | 5 |
| stroke 42 | 11 % → 19 % | 8.5 px | 0.36 | 1.73 | 3 |
| stroke 43 | 5 % → 9 % | 4.1 px | 0.35 | 1.66 | 10 |
| stroke 44 | 11 % → 15 % | 8.5 px | 0.36 | 1.41 | 11 |
| stroke 45 | 14 % → 19 % | 10.5 px | 0.35 | 1.37 | 9 |
| stroke 46 | 5 % → 7 % | 4.0 px | 0.35 | 1.38 | 4 |
| stroke 47 | 11 % → 14 % | 8.7 px | 0.36 | 1.21 | 2 |
| stroke 48 | 13 % → 18 % | 10.0 px | 0.36 | 1.36 | 12 |
| stroke 49 | 6 % → 9 % | 4.3 px | 0.35 | 1.65 | 4 |
| stroke 50 | 7 % → 7 % | 5.6 px | 0.35 | 1.00 | 5 |
| stroke 51 | 10 % → 16 % | 7.4 px | 0.36 | 1.67 | 5 |
| stroke 52 | 14 % → 16 % | 10.5 px | 0.35 | 1.19 | 7 |
| stroke 53 | 12 % → 16 % | 9.0 px | 0.35 | 1.35 | 5 |
| stroke 54 | 11 % → 16 % | 8.5 px | 0.35 | 1.46 | 9 |
| stroke 55 | 12 % → 16 % | 9.0 px | 0.35 | 1.34 | 2 |
| stroke 56 | 12 % → 13 % | 9.0 px | 0.35 | 1.11 | 6 |
| stroke 57 | 11 % → 14 % | 8.2 px | 0.36 | 1.31 | 3 |
| stroke 58 | 11 % → 12 % | 8.6 px | 0.35 | 1.12 | 7 |
| stroke 59 | 13 % → 15 % | 9.8 px | 0.35 | 1.16 | 4 |
| stroke 60 | 17 % → 22 % | 13.1 px | 0.35 | 1.26 | 11 |
| stroke 61 | 21 % → 22 % | 15.6 px | 0.35 | 1.05 | 6 |
| stroke 62 | 10 % → 10 % | 7.5 px | 0.35 | 1.00 | 2 |
| stroke 63 | 12 % → 13 % | 9.5 px | 0.35 | 1.09 | 5 |
| stroke 64 | 16 % → 17 % | 12.4 px | 0.35 | 1.02 | 5 |
| stroke 65 | 17 % → 17 % | 12.7 px | 0.35 | 1.00 | 9 |
| stroke 66 | 15 % → 15 % | 11.9 px | 0.35 | 1.00 | 3 |
| stroke 67 | 13 % → 14 % | 9.9 px | 0.35 | 1.06 | 11 |
| stroke 68 | 5 % → 10 % | 4.1 px | 0.35 | 1.90 | 5 |
| stroke 69 | 6 % → 6 % | 4.3 px | 0.35 | 1.00 | 3 |
| stroke 70 | 11 % → 14 % | 8.5 px | 0.35 | 1.28 | 2 |
| stroke 71 | 10 % → 12 % | 7.7 px | 0.35 | 1.17 | 3 |
| stroke 72 | 6 % → 7 % | 4.5 px | 0.35 | 1.26 | 2 |
| stroke 73 | 14 % → 14 % | 10.4 px | 0.35 | 1.00 | 8 |
| stroke 74 | 16 % → 16 % | 12.3 px | 0.35 | 1.00 | 3 |
| stroke 75 | 17 % → 17 % | 13.1 px | 0.35 | 1.00 | 5 |
| stroke 76 | 15 % → 15 % | 11.7 px | 0.36 | 1.00 | 5 |
| stroke 77 | 8 % → 10 % | 6.0 px | 0.35 | 1.32 | 4 |
| stroke 78 | 10 % → 10 % | 7.5 px | 0.35 | 1.00 | 9 |
| stroke 79 | 8 % → 8 % | 6.2 px | 0.35 | 1.00 | 9 |
| stroke 80 | 12 % → 12 % | 9.1 px | 0.36 | 1.00 | 5 |

Numbers say: wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #42 Oil pastel shaggy — own sheet
own sheet 600 × 600 · Pastel 1.00 · 18 px · 3.5 s

![Brush Artist · Refs · #42 Oil pastel shaggy — own sheet](Brush-Artist-Refs-42-Oil-pastel-shaggy-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 5 % → 27 % | 8.5 px | 0.27 | 5.25 | 16 |
| stroke 2 | 5 % → 24 % | 7.8 px | 0.29 | 5.02 | 6 |
| stroke 3 | 5 % → 29 % | 8.8 px | 0.28 | 5.49 | 16 |
| stroke 4 | 5 % → 11 % | 9.1 px | 0.26 | 1.99 | 18 |
| stroke 5 | 6 % → 11 % | 10.2 px | 0.26 | 1.77 | 11 |
| stroke 6 | 8 % → 36 % | 13.4 px | 0.28 | 4.52 | 11 |
| stroke 7 | 11 % → 30 % | 18.0 px | 0.28 | 2.79 | 7 |
| stroke 8 | 7 % → 37 % | 10.8 px | 0.28 | 5.63 | 18 |
| stroke 9 | 8 % → 21 % | 13.4 px | 0.28 | 2.61 | 16 |
| stroke 10 | 8 % → 18 % | 13.2 px | 0.29 | 2.30 | 11 |
| stroke 11 | 5 % → 26 % | 8.8 px | 0.28 | 4.89 | 11 |
| stroke 12 | 8 % → 19 % | 13.1 px | 0.28 | 2.33 | 12 |
| stroke 13 | 12 % → 23 % | 20.4 px | 0.28 | 1.91 | 21 |
| stroke 14 | 5 % → 22 % | 7.6 px | 0.28 | 4.76 | 18 |
| stroke 15 | 6 % → 24 % | 9.1 px | 0.28 | 4.28 | 10 |
| stroke 16 | 9 % → 21 % | 15.5 px | 0.29 | 2.21 | 12 |
| stroke 17 | 16 % → 37 % | 26.3 px | 0.28 | 2.36 | 19 |
| stroke 18 | 14 % → 25 % | 22.6 px | 0.28 | 1.82 | 19 |
| stroke 19 | 14 % → 30 % | 23.7 px | 0.28 | 2.08 | 8 |
| stroke 20 | 21 % → 39 % | 35.4 px | 0.28 | 1.81 | 12 |
| stroke 21 | 9 % → 16 % | 14.2 px | 0.28 | 1.88 | 11 |
| stroke 22 | 14 % → 17 % | 23.1 px | 0.27 | 1.19 | 20 |
| stroke 23 | 12 % → 17 % | 20.4 px | 0.29 | 1.37 | 10 |
| stroke 24 | 18 % → 26 % | 30.0 px | 0.29 | 1.43 | 9 |
| stroke 25 | 19 % → 34 % | 32.1 px | 0.28 | 1.75 | 10 |
| stroke 26 | 5 % → 13 % | 8.8 px | 0.28 | 2.45 | 8 |
| stroke 27 | 18 % → 26 % | 30.3 px | 0.29 | 1.41 | 6 |
| stroke 28 | 14 % → 23 % | 23.2 px | 0.29 | 1.66 | 13 |
| stroke 29 | 9 % → 26 % | 14.2 px | 0.29 | 3.08 | 8 |
| stroke 30 | 15 % → 36 % | 24.5 px | 0.28 | 2.44 | 13 |
| stroke 31 | 13 % → 17 % | 22.3 px | 0.29 | 1.24 | 11 |
| stroke 32 | 16 % → 29 % | 26.3 px | 0.29 | 1.82 | 10 |
| stroke 33 | 15 % → 16 % | 24.3 px | 0.28 | 1.09 | 13 |
| stroke 34 | 19 % → 27 % | 31.4 px | 0.28 | 1.44 | 12 |
| stroke 35 | 25 % → 35 % | 40.9 px | 0.28 | 1.39 | 12 |
| stroke 36 | 24 % → 33 % | 40.2 px | 0.28 | 1.34 | 14 |
| stroke 37 | 11 % → 12 % | 18.4 px | 0.28 | 1.04 | 12 |
| stroke 38 | 19 % → 24 % | 30.7 px | 0.29 | 1.31 | 8 |
| stroke 39 | 16 % → 22 % | 27.0 px | 0.27 | 1.35 | 9 |
| stroke 40 | 21 % → 29 % | 34.9 px | 0.28 | 1.37 | 13 |
| stroke 41 | 31 % → 34 % | 51.2 px | 0.28 | 1.12 | 11 |
| stroke 42 | 23 % → 29 % | 37.9 px | 0.28 | 1.28 | 15 |
| stroke 43 | 12 % → 12 % | 20.2 px | 0.28 | 1.00 | 13 |
| stroke 44 | 29 % → 36 % | 48.3 px | 0.28 | 1.24 | 15 |
| stroke 45 | 16 % → 16 % | 25.6 px | 0.27 | 1.00 | 9 |
| stroke 46 | 28 % → 33 % | 46.9 px | 0.28 | 1.15 | 7 |
| stroke 47 | 37 % → 41 % | 61.6 px | 0.28 | 1.09 | 12 |
| stroke 48 | 28 % → 35 % | 47.2 px | 0.28 | 1.26 | 11 |
| stroke 49 | 27 % → 30 % | 43.8 px | 0.29 | 1.11 | 12 |
| stroke 50 | 37 % → 40 % | 61.8 px | 0.28 | 1.07 | 10 |
| stroke 51 | 15 % → 15 % | 25.8 px | 0.28 | 1.00 | 9 |
| stroke 52 | 37 % → 37 % | 61.4 px | 0.28 | 1.01 | 11 |
| stroke 53 | 22 % → 26 % | 35.6 px | 0.29 | 1.20 | 15 |
| stroke 54 | 17 % → 19 % | 29.0 px | 0.29 | 1.10 | 13 |
| stroke 55 | 15 % → 15 % | 24.6 px | 0.29 | 1.00 | 13 |
| stroke 56 | 13 % → 14 % | 21.3 px | 0.27 | 1.08 | 12 |
| stroke 57 | 23 % → 23 % | 38.0 px | 0.29 | 1.00 | 13 |
| stroke 58 | 26 % → 28 % | 43.7 px | 0.28 | 1.06 | 15 |
| stroke 59 | 40 % → 40 % | 66.1 px | 0.28 | 1.00 | 12 |
| stroke 60 | 21 % → 21 % | 34.4 px | 0.29 | 1.00 | 12 |

Numbers say: wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #43 Dragged black ink blocks — own sheet
own sheet 600 × 600 · Gouache 1.00 · 70 px · 7.1 s

![Brush Artist · Refs · #43 Dragged black ink blocks — own sheet](Brush-Artist-Refs-43-Dragged-black-ink-blocks-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 11 % → 4 % | 24.9 px | 0.46 | 0.40 | 500 |
| stroke 2 | 10 % → 8 % | 35.4 px | 0.46 | 0.82 | 832 |
| stroke 3 | 18 % → 14 % | 66.1 px | 0.46 | 0.77 | 386 |
| stroke 4 | 22 % → 11 % | 75.0 px | 0.43 | 0.53 | 417 |
| stroke 5 | 31 % → 13 % | 72.0 px | 0.43 | 0.43 | 404 |

## Brush Artist · Refs · #44 Blue looping ribbon — own sheet
own sheet 600 × 600 · Oil 1.00 · 80 px · 5.3 s

![Brush Artist · Refs · #44 Blue looping ribbon — own sheet](Brush-Artist-Refs-44-Blue-looping-ribbon-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 32 % → 32 % | 42.1 px | 0.78 | 1.00 | 3088 |

## Brush Artist · Refs · #45 Soft pastel pepper — own sheet
own sheet 600 × 600 · Pastel 1.00 · 40 px · 4.6 s

![Brush Artist · Refs · #45 Soft pastel pepper — own sheet](Brush-Artist-Refs-45-Soft-pastel-pepper-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 10 % → 38 % | 11.3 px | 0.50 | 3.71 | 294 |
| stroke 2 | 18 % → 33 % | 20.7 px | 0.50 | 1.88 | 328 |
| stroke 3 | 25 % → 36 % | 16.9 px | 0.50 | 1.46 | 278 |
| stroke 4 | 24 % → 34 % | 29.4 px | 0.50 | 1.45 | 303 |
| stroke 5 | 30 % → 30 % | 20.9 px | 0.49 | 1.00 | 253 |
| stroke 6 | 35 % → 44 % | 22.7 px | 0.50 | 1.24 | 313 |
| stroke 7 | 39 % → 43 % | 21.3 px | 0.50 | 1.11 | 479 |
| stroke 8 | 43 % → 43 % | 43.7 px | 0.50 | 1.00 | 397 |

Numbers say: wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #46 Red-brown ink lips — own sheet
own sheet 600 × 600 · Watercolour 1.00 · 50 px · 7.8 s

![Brush Artist · Refs · #46 Red-brown ink lips — own sheet](Brush-Artist-Refs-46-Red-brown-ink-lips-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 13 % → 26 % | 54.5 px | 0.56 | 1.96 | 103 |
| stroke 2 | 17 % → 31 % | 72.4 px | 0.53 | 1.89 | 85 |

Numbers say: wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #47 Pink knife slabs — own sheet
own sheet 600 × 600 · Impasto 1.00 · 90 px · 4.4 s

![Brush Artist · Refs · #47 Pink knife slabs — own sheet](Brush-Artist-Refs-47-Pink-knife-slabs-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 16 % → 32 % | 81.5 px | 0.10 | 1.97 | 246 |
| stroke 2 | 29 % → 42 % | 165.6 px | 0.11 | 1.45 | 300 |
| stroke 3 | 29 % → 43 % | 165.1 px | 0.13 | 1.47 | 376 |
| stroke 4 | 39 % → 38 % | 165.8 px | 0.14 | 0.97 | 334 |

Numbers say: wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #48 Black bands with drips — own sheet
own sheet 600 × 600 · Gouache 1.00 · 70 px · 11.7 s

![Brush Artist · Refs · #48 Black bands with drips — own sheet](Brush-Artist-Refs-48-Black-bands-with-drips-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 28 % → 40 % | 72.6 px | 0.38 | 1.43 | 543 |
| stroke 2 | 43 % → 55 % | 137.3 px | 0.38 | 1.30 | 424 |
| stroke 3 | 45 % → 56 % | 141.4 px | 0.38 | 1.23 | 516 |
| stroke 4 | 48 % → 45 % | 139.2 px | 0.37 | 0.94 | 573 |

## Brush Artist · Refs · #49 Magenta letters round brush — own sheet
own sheet 600 × 600 · Ink 1.00 · 30 px · 9.6 s

![Brush Artist · Refs · #49 Magenta letters round brush — own sheet](Brush-Artist-Refs-49-Magenta-letters-round-brush-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 27 % → 46 % | 64.7 px | 0.52 | 1.68 | 34 |
| stroke 2 | 29 % → 41 % | 53.0 px | 0.53 | 1.40 | 30 |
| stroke 3 | 42 % → 68 % | 98.0 px | 0.52 | 1.62 | 37 |
| stroke 4 | 33 % → 52 % | 53.5 px | 0.52 | 1.56 | 113 |
| stroke 5 | 41 % → 66 % | 97.1 px | 0.52 | 1.62 | 71 |
| stroke 6 | 56 % → 72 % | 237.9 px | 0.52 | 1.28 | 19 |
| stroke 7 | 42 % → 58 % | 65.1 px | 0.52 | 1.36 | 113 |
| stroke 8 | 36 % → 61 % | 92.6 px | 0.53 | 1.71 | 61 |
| stroke 9 | 50 % → 62 % | 156.5 px | 0.52 | 1.24 | 23 |
| stroke 10 | 43 % → 73 % | 102.9 px | 0.52 | 1.68 | 68 |
| stroke 11 | 52 % → 72 % | 221.9 px | 0.52 | 1.39 | 15 |
| stroke 12 | 54 % → 70 % | 84.9 px | 0.52 | 1.28 | 111 |
| stroke 13 | 42 % → 53 % | 116.2 px | 0.53 | 1.27 | 31 |
| stroke 14 | 45 % → 68 % | 131.6 px | 0.53 | 1.52 | 33 |
| stroke 15 | 43 % → 63 % | 101.8 px | 0.52 | 1.47 | 66 |
| stroke 16 | 52 % → 61 % | 220.3 px | 0.52 | 1.19 | 17 |
| stroke 17 | 53 % → 64 % | 82.3 px | 0.52 | 1.19 | 106 |
| stroke 18 | 36 % → 43 % | 98.8 px | 0.53 | 1.20 | 49 |
| stroke 19 | 53 % → 52 % | 122.0 px | 0.52 | 0.99 | 34 |
| stroke 20 | 55 % → 55 % | 127.4 px | 0.52 | 1.00 | 52 |
| stroke 21 | 49 % → 49 % | 80.4 px | 0.52 | 1.00 | 102 |

Numbers say: wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #50 Thick swipes on photo — own sheet
own sheet 600 × 600 · Impasto 1.00 · 40 px · 2.9 s

![Brush Artist · Refs · #50 Thick swipes on photo — own sheet](Brush-Artist-Refs-50-Thick-swipes-on-photo-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 9 % → 21 % | 43.0 px | 0.35 | 2.32 | 32 |
| stroke 2 | 9 % → 16 % | 42.2 px | 0.34 | 1.82 | 29 |
| stroke 3 | 10 % → 11 % | 42.0 px | 0.32 | 1.06 | 49 |
| stroke 4 | 11 % → 18 % | 44.0 px | 0.35 | 1.60 | 43 |
| stroke 5 | 11 % → 10 % | 42.2 px | 0.34 | 0.94 | 36 |
| stroke 6 | 17 % → 21 % | 99.5 px | 0.35 | 1.19 | 27 |
| stroke 7 | 22 % → 26 % | 92.9 px | 0.35 | 1.18 | 45 |
| stroke 8 | 21 % → 20 % | 119.7 px | 0.35 | 0.96 | 38 |
| stroke 9 | 10 % → 11 % | 43.0 px | 0.30 | 1.11 | 39 |
| stroke 10 | 22 % → 22 % | 75.4 px | 0.35 | 0.96 | 42 |
| stroke 11 | 8 % → 8 % | 41.8 px | 0.36 | 0.95 | 32 |
| stroke 12 | 17 % → 16 % | 94.4 px | 0.35 | 0.96 | 19 |

Numbers say: wet paint spreads well beyond the stroke.

## Brush Artist · Ink — dry brush — own sheet
own sheet 600 × 600 · Gouache 1.00 · 30 px · 3.0 s

![Brush Artist · Ink — dry brush — own sheet](Brush-Artist-Ink-dry-brush-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| ear | 8 % → 2 % | 9.7 px | 0.85 | 0.22 | 435 |
| drag0 | 4 % → 6 % | 7.6 px | 0.85 | 1.51 | 112 |
| drag1 | 7 % → 7 % | 15.1 px | 0.85 | 0.89 | 101 |
| drag2 | 10 % → 7 % | 22.1 px | 0.85 | 0.71 | 89 |
| drag3 | 12 % → 7 % | 30.1 px | 0.85 | 0.60 | 63 |

Numbers say: wet paint spreads well beyond the stroke.

## Brush Artist · Watercolour — blue — own sheet
own sheet 600 × 600 · Watercolour 0.93 · Ink 0.07 · 40 px · 10.8 s

![Brush Artist · Watercolour — blue — own sheet](Brush-Artist-Watercolour-blue-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| s0 | 7 % → 24 % | 28.8 px | 0.30 | 3.32 | 38 |
| s1 | 6 % → 33 % | 10.1 px | 0.37 | 6.00 | 33 |
| s2 | 10 % → 19 % | 44.2 px | 0.26 | 1.81 | 33 |
| s3 | 10 % → 18 % | 26.7 px | 0.31 | 1.92 | 44 |
| s4 | 14 % → 30 % | 38.6 px | 0.36 | 2.16 | 63 |
| s5 | 19 % → 29 % | 39.3 px | 0.37 | 1.54 | 49 |
| s6 | 18 % → 22 % | 48.7 px | 0.31 | 1.25 | 48 |
| s7 | 25 % → 36 % | 32.7 px | 0.37 | 1.46 | 39 |
| s8 | 21 % → 25 % | 79.8 px | 0.30 | 1.20 | 40 |

Numbers say: wet paint spreads well beyond the stroke.

## Brush Artist · Charcoal — stick — own sheet
own sheet 600 × 600 · Charcoal 0.78 · Pastel 0.22 · 28 px · 1.2 s

![Brush Artist · Charcoal — stick — own sheet](Brush-Artist-Charcoal-stick-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| finger0 | 12 % → 25 % | 21.2 px | 0.83 | 2.03 | 31 |
| tip0 | 13 % → 21 % | 33.8 px | 0.83 | 1.70 | 8 |
| finger1 | 23 % → 41 % | 40.4 px | 0.83 | 1.77 | 38 |
| tip1 | 21 % → 29 % | 57.3 px | 0.83 | 1.38 | 12 |
| finger2 | 25 % → 37 % | 43.8 px | 0.83 | 1.49 | 34 |
| tip2 | 21 % → 29 % | 55.7 px | 0.83 | 1.40 | 10 |
| finger3 | 24 % → 27 % | 42.7 px | 0.83 | 1.14 | 30 |
| tip3 | 20 % → 20 % | 54.1 px | 0.83 | 1.00 | 11 |
| cig0 | 34 % → 47 % | 75.0 px | 0.83 | 1.39 | 10 |
| cig1 | 36 % → 47 % | 80.5 px | 0.83 | 1.30 | 13 |
| cig2 | 39 % → 47 % | 86.7 px | 0.83 | 1.20 | 14 |
| cig3 | 41 % → 47 % | 91.3 px | 0.83 | 1.14 | 16 |
| cig4 | 44 % → 46 % | 97.5 px | 0.83 | 1.06 | 14 |
| cig5 | 46 % → 46 % | 102.9 px | 0.83 | 1.00 | 14 |

Numbers say: wet paint spreads well beyond the stroke.

## Oil · Henry Ward · HW #02 cream over wet olive — own sheet
own sheet 600 × 600 · Watercolour 0.93 · Ink 0.07 + turpentine 80 % · 96 px · 37.6 s

![Oil · Henry Ward · HW #02 cream over wet olive — own sheet](Oil-Henry-Ward-HW-02-cream-over-wet-olive-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 44 % → 44 % | 86.0 px | 0.59 | 0.98 | 1801 |
| stroke 2 | 56 % → 50 % | 144.3 px | 0.56 | 0.89 | 2071 |
| stroke 3 | 65 % → 50 % | 205.6 px | 0.57 | 0.76 | 2315 |
| stroke 4 | 69 % → 50 % | 241.1 px | 0.58 | 0.73 | 2538 |
| stroke 5 | 69 % → 57 % | 240.7 px | 0.58 | 0.82 | 2513 |
| stroke 6 | 68 % → 46 % | 240.2 px | 0.56 | 0.67 | 2178 |
| stroke 7 | 77 % → 35 % | 239.6 px | 0.58 | 0.46 | 2095 |
| stroke 8 | 94 % → 29 % | 239.8 px | 0.60 | 0.31 | 2681 |
| stroke 9 | 100 % → 27 % | 192.3 px | 0.59 | 0.27 | 1862 |
| stroke 10 | 6 % → 49 % | 43.6 px | 0.57 | 8.17 | 254 |
| stroke 11 | 12 % → 54 % | 77.4 px | 0.58 | 4.68 | 385 |
| stroke 12 | 10 % → 39 % | 88.7 px | 0.57 | 4.07 | 173 |
| stroke 13 | 28 % → 50 % | 121.1 px | 0.56 | 1.82 | 436 |
| stroke 14 | 30 % → 50 % | 173.8 px | 0.57 | 1.68 | 549 |
| stroke 15 | 30 % → 48 % | 203.1 px | 0.57 | 1.61 | 328 |
| stroke 16 | 35 % → 47 % | 179.3 px | 0.58 | 1.34 | 562 |
| stroke 17 | 39 % → 55 % | 261.0 px | 0.58 | 1.39 | 465 |
| stroke 18 | 43 % → 55 % | 303.5 px | 0.58 | 1.28 | 520 |
| stroke 19 | 40 % → 50 % | 348.7 px | 0.56 | 1.22 | 219 |
| stroke 20 | 35 % → 40 % | 289.4 px | 0.57 | 1.14 | 234 |
| stroke 21 | 39 % → 37 % | 196.3 px | 0.57 | 0.95 | 416 |
| stroke 22 | 53 % → 50 % | 462.2 px | 0.57 | 0.94 | 240 |
| stroke 23 | 50 % → 47 % | 340.3 px | 0.58 | 0.94 | 513 |
| stroke 24 | 57 % → 54 % | 374.9 px | 0.58 | 0.95 | 393 |
| stroke 25 | 61 % → 58 % | 538.5 px | 0.57 | 0.96 | 199 |
| stroke 26 | 42 % → 39 % | 335.5 px | 0.57 | 0.93 | 359 |

Numbers say: wet paint spreads well beyond the stroke.

## Oil · Henry Ward · HW #04 grey arcs over ochre — own sheet
own sheet 600 × 600 · Gouache 1.00 + turpentine 35 % · 84 px · 43.9 s

![Oil · Henry Ward · HW #04 grey arcs over ochre — own sheet](Oil-Henry-Ward-HW-04-grey-arcs-over-ochre-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 47 % → 54 % | 79.1 px | 0.39 | 1.15 | 1768 |
| stroke 2 | 63 % → 63 % | 149.2 px | 0.39 | 1.01 | 2066 |
| stroke 3 | 70 % → 56 % | 209.4 px | 0.39 | 0.80 | 2226 |
| stroke 4 | 71 % → 62 % | 217.9 px | 0.33 | 0.88 | 2628 |
| stroke 5 | 71 % → 61 % | 218.3 px | 0.27 | 0.86 | 2387 |
| stroke 6 | 71 % → 49 % | 217.0 px | 0.20 | 0.69 | 2263 |
| stroke 7 | 75 % → 37 % | 218.9 px | 0.08 | 0.50 | 2153 |
| stroke 8 | 94 % → 39 % | 218.4 px | 0.02 | 0.42 | 2722 |
| stroke 9 | 100 % → 36 % | 167.6 px | 0.02 | 0.36 | 1717 |
| stroke 10 | 11 % → 64 % | 62.2 px | 0.28 | 5.98 | 460 |
| stroke 11 | 15 % → 56 % | 78.3 px | 0.29 | 3.68 | 589 |
| stroke 12 | 18 % → 57 % | 119.7 px | 0.30 | 3.10 | 414 |
| stroke 13 | 27 % → 60 % | 164.0 px | 0.35 | 2.28 | 369 |
| stroke 14 | 26 % → 64 % | 216.3 px | 0.29 | 2.48 | 329 |
| stroke 15 | 32 % → 58 % | 243.9 px | 0.36 | 1.84 | 278 |
| stroke 16 | 28 % → 55 % | 137.0 px | 0.31 | 1.97 | 861 |
| stroke 17 | 45 % → 58 % | 191.1 px | 0.39 | 1.29 | 596 |
| stroke 18 | 39 % → 55 % | 183.6 px | 0.34 | 1.41 | 621 |
| stroke 19 | 48 % → 56 % | 219.7 px | 0.38 | 1.16 | 526 |
| stroke 20 | 44 % → 58 % | 336.6 px | 0.32 | 1.33 | 569 |
| stroke 21 | 45 % → 60 % | 292.3 px | 0.29 | 1.33 | 710 |
| stroke 22 | 50 % → 65 % | 340.3 px | 0.28 | 1.30 | 522 |
| stroke 23 | 52 % → 57 % | 255.3 px | 0.33 | 1.10 | 809 |
| stroke 24 | 51 % → 57 % | 264.0 px | 0.32 | 1.10 | 636 |
| stroke 25 | 54 % → 55 % | 316.4 px | 0.34 | 1.02 | 607 |
| stroke 26 | 50 % → 56 % | 264.1 px | 0.31 | 1.10 | 727 |
| stroke 27 | 36 % → 49 % | 201.0 px | 0.20 | 1.39 | 398 |
| stroke 28 | 34 % → 44 % | 232.6 px | 0.13 | 1.27 | 323 |
| stroke 29 | 34 % → 39 % | 207.7 px | 0.10 | 1.15 | 391 |
| stroke 30 | 40 % → 39 % | 183.7 px | 0.02 | 0.98 | 229 |

Numbers say: wet paint spreads well beyond the stroke.

## Oil · Henry Ward · HW #09 white arches over wet blue-grey — own sheet
own sheet 600 × 600 · Gouache 1.00 + turpentine 35 % · 84 px · 48.6 s

![Oil · Henry Ward · HW #09 white arches over wet blue-grey — own sheet](Oil-Henry-Ward-HW-09-white-arches-over-wet-blue-grey-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 47 % → 18 % | 81.2 px | 0.15 | 0.38 | 1671 |
| stroke 2 | 62 % → 30 % | 144.0 px | 0.15 | 0.49 | 2256 |
| stroke 3 | 70 % → 38 % | 206.7 px | 0.15 | 0.54 | 2353 |
| stroke 4 | 71 % → 50 % | 217.4 px | 0.15 | 0.70 | 2524 |
| stroke 5 | 71 % → 62 % | 219.0 px | 0.15 | 0.88 | 2339 |
| stroke 6 | 71 % → 63 % | 217.3 px | 0.15 | 0.89 | 2272 |
| stroke 7 | 75 % → 58 % | 218.8 px | 0.14 | 0.77 | 2640 |
| stroke 8 | 93 % → 56 % | 218.7 px | 0.14 | 0.60 | 2472 |
| stroke 9 | 100 % → 52 % | 167.6 px | 0.13 | 0.52 | 1886 |
| stroke 10 | 8 % → 46 % | 21.0 px | 0.15 | 6.12 | 872 |
| stroke 11 | 15 % → 53 % | 34.6 px | 0.15 | 3.61 | 772 |
| stroke 12 | 16 % → 55 % | 50.1 px | 0.15 | 3.39 | 670 |
| stroke 13 | 18 % → 60 % | 60.1 px | 0.15 | 3.37 | 517 |
| stroke 14 | 20 % → 59 % | 29.3 px | 0.14 | 2.90 | 873 |
| stroke 15 | 26 % → 55 % | 114.0 px | 0.15 | 2.15 | 661 |
| stroke 16 | 36 % → 65 % | 187.9 px | 0.15 | 1.78 | 826 |
| stroke 17 | 36 % → 49 % | 130.9 px | 0.16 | 1.39 | 725 |
| stroke 18 | 43 % → 55 % | 172.7 px | 0.15 | 1.26 | 1105 |
| stroke 19 | 48 % → 55 % | 197.9 px | 0.16 | 1.14 | 738 |
| stroke 20 | 51 % → 59 % | 208.7 px | 0.15 | 1.16 | 1141 |
| stroke 21 | 52 % → 55 % | 194.9 px | 0.14 | 1.04 | 996 |
| stroke 22 | 61 % → 65 % | 362.9 px | 0.15 | 1.06 | 748 |
| stroke 23 | 58 % → 58 % | 268.9 px | 0.15 | 1.00 | 732 |
| stroke 24 | 60 % → 62 % | 327.8 px | 0.15 | 1.03 | 611 |
| stroke 25 | 69 % → 70 % | 480.3 px | 0.14 | 1.03 | 289 |
| stroke 26 | 58 % → 58 % | 288.3 px | 0.14 | 1.01 | 717 |
| stroke 27 | 58 % → 59 % | 381.8 px | 0.14 | 1.02 | 393 |
| stroke 28 | 62 % → 56 % | 242.8 px | 0.14 | 0.90 | 478 |

Numbers say: wet paint spreads well beyond the stroke.

## Oil · Henry Ward · HW #03 navy contours over wet band — own sheet
own sheet 600 × 600 · Gouache 1.00 + turpentine 35 % · 84 px · 30.1 s

![Oil · Henry Ward · HW #03 navy contours over wet band — own sheet](Oil-Henry-Ward-HW-03-navy-contours-over-wet-band-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 50 % → 37 % | 87.6 px | 0.65 | 0.73 | 1422 |
| stroke 2 | 61 % → 41 % | 145.4 px | 0.61 | 0.68 | 1891 |
| stroke 3 | 69 % → 43 % | 202.2 px | 0.58 | 0.62 | 2173 |
| stroke 4 | 71 % → 48 % | 218.6 px | 0.57 | 0.68 | 2420 |
| stroke 5 | 71 % → 51 % | 217.2 px | 0.58 | 0.72 | 2059 |
| stroke 6 | 71 % → 39 % | 222.3 px | 0.56 | 0.54 | 1959 |
| stroke 7 | 74 % → 29 % | 218.0 px | 0.56 | 0.39 | 1795 |
| stroke 8 | 95 % → 23 % | 218.1 px | 0.62 | 0.24 | 2526 |
| stroke 9 | 100 % → 17 % | 170.3 px | 0.66 | 0.17 | 1623 |
| stroke 10 | 7 % → 45 % | 47.5 px | 0.57 | 6.55 | 318 |
| stroke 11 | 12 % → 52 % | 114.2 px | 0.58 | 4.26 | 170 |
| stroke 12 | 20 % → 52 % | 186.7 px | 0.56 | 2.61 | 147 |
| stroke 13 | 18 % → 41 % | 158.3 px | 0.56 | 2.20 | 214 |
| stroke 14 | 18 % → 48 % | 157.3 px | 0.63 | 2.61 | 121 |
| stroke 15 | 27 % → 47 % | 217.1 px | 0.60 | 1.77 | 210 |
| stroke 16 | 37 % → 37 % | 109.6 px | 0.57 | 0.99 | 883 |
| stroke 17 | 42 % → 38 % | 151.9 px | 0.58 | 0.91 | 702 |

Numbers say: wet paint spreads well beyond the stroke.

## Oil · Henry Ward · HW #01 peach cloud and legs over teal — own sheet
own sheet 600 × 600 · Gouache 1.00 + turpentine 35 % · 84 px · 37.5 s

![Oil · Henry Ward · HW #01 peach cloud and legs over teal — own sheet](Oil-Henry-Ward-HW-01-peach-cloud-and-legs-over-teal-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 50 % → 45 % | 88.9 px | 0.52 | 0.89 | 1752 |
| stroke 2 | 62 % → 53 % | 146.9 px | 0.54 | 0.86 | 2148 |
| stroke 3 | 69 % → 56 % | 203.4 px | 0.54 | 0.81 | 2230 |
| stroke 4 | 72 % → 61 % | 220.2 px | 0.54 | 0.86 | 2433 |
| stroke 5 | 70 % → 52 % | 218.3 px | 0.53 | 0.74 | 2379 |
| stroke 6 | 71 % → 50 % | 218.2 px | 0.46 | 0.70 | 2239 |
| stroke 7 | 77 % → 45 % | 222.3 px | 0.33 | 0.59 | 2508 |
| stroke 8 | 95 % → 40 % | 219.1 px | 0.24 | 0.42 | 2354 |
| stroke 9 | 100 % → 37 % | 170.3 px | 0.11 | 0.37 | 1929 |
| stroke 10 | 13 % → 52 % | 48.3 px | 0.54 | 4.09 | 347 |
| stroke 11 | 21 % → 55 % | 94.4 px | 0.54 | 2.57 | 445 |
| stroke 12 | 22 % → 57 % | 116.2 px | 0.54 | 2.56 | 290 |
| stroke 13 | 30 % → 61 % | 155.2 px | 0.54 | 2.01 | 369 |
| stroke 14 | 46 % → 52 % | 175.2 px | 0.54 | 1.13 | 609 |
| stroke 15 | 38 % → 56 % | 188.0 px | 0.54 | 1.46 | 398 |
| stroke 16 | 38 % → 60 % | 201.9 px | 0.54 | 1.58 | 635 |
| stroke 17 | 33 % → 52 % | 178.8 px | 0.43 | 1.59 | 382 |
| stroke 18 | 38 % → 55 % | 323.6 px | 0.43 | 1.44 | 293 |
| stroke 19 | 49 % → 70 % | 405.9 px | 0.43 | 1.41 | 288 |
| stroke 20 | 49 % → 69 % | 374.2 px | 0.43 | 1.43 | 385 |
| stroke 21 | 44 % → 57 % | 362.1 px | 0.44 | 1.29 | 378 |
| stroke 22 | 42 % → 50 % | 293.1 px | 0.44 | 1.18 | 245 |
| stroke 23 | 41 % → 46 % | 144.4 px | 0.24 | 1.14 | 229 |
| stroke 24 | 48 % → 44 % | 180.0 px | 0.23 | 0.90 | 277 |

Numbers say: wet paint spreads well beyond the stroke.

## Oil · Henry Ward · HW #05 rust, pink, green-black — own sheet
own sheet 600 × 600 · Gouache 1.00 + turpentine 35 % · 84 px · 37.0 s

![Oil · Henry Ward · HW #05 rust, pink, green-black — own sheet](Oil-Henry-Ward-HW-05-rust-pink-green-black-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 49 % → 53 % | 83.9 px | 0.58 | 1.08 | 1446 |
| stroke 2 | 63 % → 60 % | 148.0 px | 0.49 | 0.96 | 2022 |
| stroke 3 | 69 % → 60 % | 207.2 px | 0.40 | 0.88 | 2103 |
| stroke 4 | 71 % → 68 % | 218.5 px | 0.34 | 0.96 | 2373 |
| stroke 5 | 71 % → 67 % | 220.5 px | 0.35 | 0.94 | 2046 |
| stroke 6 | 70 % → 63 % | 216.1 px | 0.35 | 0.90 | 2019 |
| stroke 7 | 74 % → 53 % | 217.7 px | 0.39 | 0.72 | 1906 |
| stroke 8 | 93 % → 50 % | 217.2 px | 0.49 | 0.53 | 2632 |
| stroke 9 | 100 % → 42 % | 167.6 px | 0.69 | 0.42 | 1523 |
| stroke 10 | 15 % → 57 % | 53.7 px | 0.56 | 3.76 | 348 |
| stroke 11 | 22 % → 62 % | 94.0 px | 0.44 | 2.78 | 391 |
| stroke 12 | 26 % → 62 % | 137.0 px | 0.40 | 2.37 | 358 |
| stroke 13 | 31 % → 65 % | 163.8 px | 0.36 | 2.10 | 415 |
| stroke 14 | 48 % → 59 % | 216.8 px | 0.50 | 1.23 | 266 |
| stroke 15 | 42 % → 63 % | 211.5 px | 0.42 | 1.49 | 346 |
| stroke 16 | 38 % → 65 % | 254.1 px | 0.36 | 1.73 | 226 |
| stroke 17 | 43 % → 68 % | 221.3 px | 0.34 | 1.58 | 709 |
| stroke 18 | 45 % → 68 % | 242.7 px | 0.35 | 1.52 | 845 |
| stroke 19 | 43 % → 63 % | 217.8 px | 0.36 | 1.45 | 631 |
| stroke 20 | 48 % → 62 % | 354.6 px | 0.39 | 1.30 | 169 |
| stroke 21 | 50 % → 61 % | 363.4 px | 0.40 | 1.23 | 231 |
| stroke 22 | 51 % → 63 % | 424.5 px | 0.41 | 1.24 | 192 |
| stroke 23 | 46 % → 56 % | 264.4 px | 0.35 | 1.21 | 508 |
| stroke 24 | 47 % → 49 % | 223.8 px | 0.46 | 1.04 | 413 |
| stroke 25 | 52 % → 49 % | 184.5 px | 0.56 | 0.93 | 311 |

Numbers say: wet paint spreads well beyond the stroke.

## Oil · Henry Ward · HW #07 blue L and zigzag on lilac — own sheet
own sheet 600 × 600 · Gouache 1.00 + turpentine 20 % · 90 px · 39.6 s

![Oil · Henry Ward · HW #07 blue L and zigzag on lilac — own sheet](Oil-Henry-Ward-HW-07-blue-L-and-zigzag-on-lilac-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 45 % → 29 % | 81.5 px | 0.28 | 0.64 | 1392 |
| stroke 2 | 58 % → 39 % | 140.1 px | 0.36 | 0.67 | 1920 |
| stroke 3 | 67 % → 67 % | 204.7 px | 0.37 | 1.00 | 1991 |
| stroke 4 | 70 % → 51 % | 231.5 px | 0.35 | 0.72 | 2206 |
| stroke 5 | 69 % → 60 % | 227.8 px | 0.33 | 0.87 | 2004 |
| stroke 6 | 69 % → 61 % | 227.3 px | 0.31 | 0.90 | 1878 |
| stroke 7 | 75 % → 56 % | 228.0 px | 0.26 | 0.75 | 1841 |
| stroke 8 | 96 % → 50 % | 229.1 px | 0.19 | 0.52 | 2689 |
| stroke 9 | 100 % → 54 % | 182.6 px | 0.16 | 0.54 | 1679 |
| stroke 10 | 12 % → 33 % | 33.5 px | 0.30 | 2.69 | 427 |
| stroke 11 | 22 % → 41 % | 73.6 px | 0.38 | 1.90 | 663 |
| stroke 12 | 21 % → 42 % | 75.1 px | 0.38 | 2.02 | 514 |
| stroke 13 | 23 % → 46 % | 87.9 px | 0.37 | 2.05 | 484 |
| stroke 14 | 28 % → 49 % | 127.2 px | 0.35 | 1.75 | 549 |
| stroke 15 | 30 % → 55 % | 150.9 px | 0.33 | 1.81 | 441 |
| stroke 16 | 36 % → 61 % | 160.5 px | 0.33 | 1.70 | 684 |
| stroke 17 | 34 % → 62 % | 168.7 px | 0.31 | 1.85 | 521 |
| stroke 18 | 43 % → 61 % | 187.9 px | 0.29 | 1.42 | 587 |
| stroke 19 | 46 % → 56 % | 189.0 px | 0.26 | 1.20 | 503 |
| stroke 20 | 52 % → 55 % | 202.0 px | 0.22 | 1.04 | 633 |
| stroke 21 | 62 % → 51 % | 203.4 px | 0.19 | 0.82 | 588 |
| stroke 22 | 71 % → 50 % | 219.7 px | 0.17 | 0.71 | 486 |
| stroke 23 | 61 % → 53 % | 339.8 px | 0.29 | 0.86 | 367 |
| stroke 24 | 73 % → 55 % | 481.2 px | 0.23 | 0.76 | 276 |
| stroke 25 | 67 % → 52 % | 251.0 px | 0.33 | 0.78 | 575 |
| stroke 26 | 67 % → 60 % | 725.7 px | 0.29 | 0.90 | 205 |
| stroke 27 | 75 % → 63 % | 714.6 px | 0.28 | 0.84 | 190 |
| stroke 28 | 75 % → 62 % | 562.8 px | 0.28 | 0.83 | 313 |
| stroke 29 | 74 % → 62 % | 653.2 px | 0.28 | 0.83 | 178 |
| stroke 30 | 78 % → 64 % | 607.6 px | 0.28 | 0.82 | 352 |
| stroke 31 | 78 % → 64 % | 1158.0 px | 0.26 | 0.82 | 133 |

Numbers say: wet paint spreads well beyond the stroke.

## Oil · Henry Ward · HW #08 crown and dark oval — own sheet
own sheet 600 × 600 · Gouache 1.00 + turpentine 35 % · 84 px · 28.9 s

![Oil · Henry Ward · HW #08 crown and dark oval — own sheet](Oil-Henry-Ward-HW-08-crown-and-dark-oval-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 50 % → 0 % | 88.5 px | 0.00 | 0.00 | 1762 |
| stroke 2 | 61 % → 0 % | 142.2 px | 0.00 | 0.00 | 1873 |
| stroke 3 | 70 % → 3 % | 206.2 px | 0.09 | 0.04 | 2001 |
| stroke 4 | 72 % → 7 % | 223.5 px | 0.08 | 0.10 | 2102 |
| stroke 5 | 71 % → 13 % | 220.0 px | 0.08 | 0.18 | 2470 |
| stroke 6 | 70 % → 13 % | 219.6 px | 0.08 | 0.18 | 1968 |
| stroke 7 | 74 % → 13 % | 217.8 px | 0.08 | 0.18 | 1920 |
| stroke 8 | 94 % → 13 % | 217.3 px | 0.08 | 0.14 | 2356 |
| stroke 9 | 100 % → 9 % | 166.8 px | 0.09 | 0.09 | 1554 |
| stroke 10 | 19 % → 0 % | 78.0 px | 0.00 | 0.00 | 380 |
| stroke 11 | 31 % → 1 % | 159.4 px | 0.08 | 0.03 | 555 |
| stroke 12 | 35 % → 3 % | 220.7 px | 0.09 | 0.09 | 503 |
| stroke 13 | 33 % → 9 % | 99.9 px | 0.08 | 0.27 | 727 |
| stroke 14 | 41 % → 12 % | 298.0 px | 0.08 | 0.30 | 445 |
| stroke 15 | 42 % → 12 % | 346.6 px | 0.08 | 0.29 | 367 |
| stroke 16 | 41 % → 12 % | 334.3 px | 0.08 | 0.30 | 386 |
| stroke 17 | 44 % → 14 % | 281.7 px | 0.08 | 0.31 | 331 |
| stroke 18 | 11 % → 13 % | 97.1 px | 0.08 | 1.19 | 393 |
| stroke 19 | 22 % → 13 % | 191.6 px | 0.08 | 0.57 | 405 |
| stroke 20 | 28 % → 13 % | 212.5 px | 0.08 | 0.47 | 405 |

## Oil · Henry Ward · HW #10 green block over maroon — own sheet
own sheet 600 × 600 · Gouache 1.00 + turpentine 35 % · 84 px · 35.8 s

![Oil · Henry Ward · HW #10 green block over maroon — own sheet](Oil-Henry-Ward-HW-10-green-block-over-maroon-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 50 % → 39 % | 86.8 px | 0.17 | 0.79 | 1327 |
| stroke 2 | 61 % → 44 % | 141.4 px | 0.30 | 0.72 | 1828 |
| stroke 3 | 70 % → 48 % | 209.0 px | 0.41 | 0.69 | 2100 |
| stroke 4 | 71 % → 55 % | 218.3 px | 0.49 | 0.77 | 2571 |
| stroke 5 | 70 % → 57 % | 215.7 px | 0.58 | 0.81 | 2145 |
| stroke 6 | 71 % → 54 % | 218.8 px | 0.62 | 0.76 | 1952 |
| stroke 7 | 75 % → 45 % | 219.0 px | 0.63 | 0.59 | 2134 |
| stroke 8 | 93 % → 40 % | 217.8 px | 0.61 | 0.43 | 2186 |
| stroke 9 | 100 % → 30 % | 172.0 px | 0.54 | 0.30 | 1723 |
| stroke 10 | 14 % → 44 % | 78.5 px | 0.22 | 3.20 | 242 |
| stroke 11 | 24 % → 46 % | 155.7 px | 0.34 | 1.95 | 291 |
| stroke 12 | 26 % → 53 % | 227.1 px | 0.46 | 2.01 | 398 |
| stroke 13 | 39 % → 47 % | 260.6 px | 0.31 | 1.19 | 244 |
| stroke 14 | 34 % → 51 % | 275.3 px | 0.38 | 1.50 | 323 |
| stroke 15 | 29 % → 53 % | 259.7 px | 0.44 | 1.85 | 210 |
| stroke 16 | 29 % → 53 % | 208.5 px | 0.47 | 1.81 | 585 |
| stroke 17 | 33 % → 56 % | 221.2 px | 0.54 | 1.70 | 612 |
| stroke 18 | 36 % → 56 % | 248.9 px | 0.60 | 1.58 | 484 |
| stroke 19 | 38 % → 53 % | 272.6 px | 0.62 | 1.41 | 328 |
| stroke 20 | 37 % → 49 % | 265.3 px | 0.63 | 1.33 | 592 |
| stroke 21 | 42 % → 46 % | 156.1 px | 0.50 | 1.08 | 890 |
| stroke 22 | 41 % → 46 % | 332.1 px | 0.63 | 1.11 | 367 |
| stroke 23 | 45 % → 43 % | 280.7 px | 0.62 | 0.94 | 534 |
| stroke 24 | 50 % → 36 % | 278.5 px | 0.58 | 0.72 | 339 |

Numbers say: wet paint spreads well beyond the stroke.

## Oil · Henry Ward · HW #11 cream mass and purple balls — own sheet
own sheet 600 × 600 · Gouache 1.00 + turpentine 35 % · 84 px · 38.0 s

![Oil · Henry Ward · HW #11 cream mass and purple balls — own sheet](Oil-Henry-Ward-HW-11-cream-mass-and-purple-balls-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 49 % → 41 % | 83.5 px | 0.10 | 0.84 | 1700 |
| stroke 2 | 62 % → 44 % | 147.7 px | 0.11 | 0.71 | 2045 |
| stroke 3 | 70 % → 46 % | 210.2 px | 0.12 | 0.66 | 2160 |
| stroke 4 | 71 % → 49 % | 221.0 px | 0.12 | 0.69 | 2987 |
| stroke 5 | 71 % → 48 % | 217.6 px | 0.20 | 0.68 | 2372 |
| stroke 6 | 70 % → 48 % | 216.5 px | 0.29 | 0.69 | 2325 |
| stroke 7 | 76 % → 40 % | 221.8 px | 0.35 | 0.52 | 2263 |
| stroke 8 | 94 % → 36 % | 219.3 px | 0.43 | 0.39 | 2529 |
| stroke 9 | 100 % → 37 % | 171.2 px | 0.54 | 0.37 | 1967 |
| stroke 10 | 14 % → 44 % | 59.6 px | 0.11 | 3.12 | 302 |
| stroke 11 | 20 % → 44 % | 104.4 px | 0.11 | 2.25 | 344 |
| stroke 12 | 24 % → 46 % | 133.1 px | 0.12 | 1.95 | 340 |
| stroke 13 | 27 % → 48 % | 172.1 px | 0.11 | 1.76 | 322 |
| stroke 14 | 30 % → 48 % | 199.1 px | 0.14 | 1.63 | 334 |
| stroke 15 | 30 % → 48 % | 182.9 px | 0.18 | 1.60 | 281 |
| stroke 16 | 31 % → 50 % | 206.4 px | 0.26 | 1.62 | 456 |
| stroke 17 | 29 % → 48 % | 184.9 px | 0.29 | 1.66 | 373 |
| stroke 18 | 44 % → 44 % | 225.6 px | 0.11 | 1.00 | 335 |
| stroke 19 | 46 % → 45 % | 268.8 px | 0.11 | 0.99 | 316 |
| stroke 20 | 49 % → 47 % | 340.5 px | 0.11 | 0.96 | 517 |
| stroke 21 | 52 % → 49 % | 408.4 px | 0.12 | 0.95 | 402 |
| stroke 22 | 48 % → 48 % | 336.3 px | 0.15 | 1.00 | 304 |
| stroke 23 | 38 % → 49 % | 254.7 px | 0.24 | 1.29 | 399 |
| stroke 24 | 34 % → 49 % | 239.4 px | 0.27 | 1.45 | 381 |
| stroke 25 | 41 % → 48 % | 115.7 px | 0.34 | 1.17 | 495 |
| stroke 26 | 53 % → 54 % | 157.2 px | 0.34 | 1.02 | 484 |
| stroke 27 | 51 % → 47 % | 132.4 px | 0.33 | 0.93 | 585 |

Numbers say: wet paint spreads well beyond the stroke.

## Oil · Henry Ward · HW #13 blue scrub under red — own sheet
own sheet 600 × 600 · Gouache 1.00 + turpentine 35 % · 84 px · 38.1 s

![Oil · Henry Ward · HW #13 blue scrub under red — own sheet](Oil-Henry-Ward-HW-13-blue-scrub-under-red-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 49 % → 10 % | 83.9 px | 0.06 | 0.20 | 1308 |
| stroke 2 | 61 % → 23 % | 142.5 px | 0.06 | 0.37 | 1831 |
| stroke 3 | 69 % → 30 % | 204.0 px | 0.06 | 0.43 | 2061 |
| stroke 4 | 71 % → 40 % | 220.1 px | 0.06 | 0.56 | 2217 |
| stroke 5 | 70 % → 55 % | 216.6 px | 0.06 | 0.79 | 2173 |
| stroke 6 | 71 % → 64 % | 220.3 px | 0.06 | 0.90 | 1970 |
| stroke 7 | 75 % → 64 % | 216.2 px | 0.06 | 0.86 | 2012 |
| stroke 8 | 95 % → 66 % | 222.8 px | 0.06 | 0.70 | 2351 |
| stroke 9 | 100 % → 70 % | 165.9 px | 0.06 | 0.70 | 1681 |
| stroke 10 | 15 % → 12 % | 55.6 px | 0.07 | 0.81 | 360 |
| stroke 11 | 18 % → 28 % | 108.8 px | 0.05 | 1.54 | 267 |
| stroke 12 | 19 % → 30 % | 117.2 px | 0.05 | 1.55 | 267 |
| stroke 13 | 9 % → 33 % | 43.7 px | 0.06 | 3.67 | 436 |
| stroke 14 | 19 % → 45 % | 99.3 px | 0.05 | 2.39 | 565 |
| stroke 15 | 27 % → 54 % | 140.4 px | 0.06 | 2.04 | 344 |
| stroke 16 | 34 % → 61 % | 175.7 px | 0.06 | 1.78 | 367 |
| stroke 17 | 37 % → 66 % | 196.9 px | 0.06 | 1.75 | 405 |
| stroke 18 | 39 % → 64 % | 176.2 px | 0.06 | 1.65 | 447 |
| stroke 19 | 44 % → 64 % | 182.0 px | 0.06 | 1.46 | 481 |
| stroke 20 | 55 % → 66 % | 204.4 px | 0.06 | 1.21 | 382 |
| stroke 21 | 68 % → 71 % | 206.1 px | 0.05 | 1.04 | 443 |
| stroke 22 | 42 % → 39 % | 225.8 px | 0.06 | 0.93 | 424 |
| stroke 23 | 55 % → 51 % | 279.9 px | 0.06 | 0.94 | 409 |
| stroke 24 | 59 % → 56 % | 339.8 px | 0.06 | 0.94 | 355 |
| stroke 25 | 66 % → 63 % | 324.7 px | 0.06 | 0.96 | 492 |
| stroke 26 | 68 % → 66 % | 351.4 px | 0.06 | 0.96 | 526 |
| stroke 27 | 67 % → 64 % | 322.4 px | 0.06 | 0.97 | 495 |
| stroke 28 | 70 % → 66 % | 288.6 px | 0.06 | 0.95 | 549 |
| stroke 29 | 72 % → 67 % | 281.7 px | 0.06 | 0.93 | 415 |

Numbers say: wet paint spreads well beyond the stroke.

## Oil · Henry Ward · HW #14 olive totem on dark — own sheet
own sheet 600 × 600 · Gouache 1.00 + turpentine 35 % · 84 px · 43.8 s

![Oil · Henry Ward · HW #14 olive totem on dark — own sheet](Oil-Henry-Ward-HW-14-olive-totem-on-dark-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 47 % → 42 % | 78.9 px | 0.38 | 0.89 | 1645 |
| stroke 2 | 62 % → 50 % | 146.1 px | 0.40 | 0.80 | 2252 |
| stroke 3 | 70 % → 48 % | 208.2 px | 0.41 | 0.68 | 2361 |
| stroke 4 | 71 % → 55 % | 219.4 px | 0.41 | 0.77 | 2724 |
| stroke 5 | 71 % → 60 % | 217.3 px | 0.40 | 0.85 | 2477 |
| stroke 6 | 71 % → 56 % | 216.7 px | 0.41 | 0.80 | 2540 |
| stroke 7 | 74 % → 45 % | 219.2 px | 0.40 | 0.62 | 2241 |
| stroke 8 | 94 % → 46 % | 217.9 px | 0.39 | 0.49 | 2232 |
| stroke 9 | 100 % → 42 % | 172.0 px | 0.39 | 0.42 | 1726 |
| stroke 10 | 22 % → 69 % | 90.9 px | 0.40 | 3.21 | 616 |
| stroke 11 | 28 % → 72 % | 119.1 px | 0.40 | 2.58 | 595 |
| stroke 12 | 44 % → 63 % | 183.0 px | 0.40 | 1.42 | 646 |
| stroke 13 | 39 % → 48 % | 189.5 px | 0.41 | 1.25 | 578 |
| stroke 14 | 46 % → 52 % | 263.5 px | 0.40 | 1.14 | 551 |
| stroke 15 | 50 % → 57 % | 270.2 px | 0.40 | 1.15 | 563 |
| stroke 16 | 38 % → 49 % | 211.6 px | 0.40 | 1.28 | 447 |
| stroke 17 | 36 % → 44 % | 183.0 px | 0.39 | 1.23 | 382 |
| stroke 18 | 43 % → 46 % | 202.6 px | 0.39 | 1.06 | 413 |
| stroke 19 | 53 % → 50 % | 286.6 px | 0.41 | 0.94 | 343 |
| stroke 20 | 51 % → 51 % | 316.0 px | 0.41 | 0.99 | 549 |
| stroke 21 | 55 % → 55 % | 361.8 px | 0.41 | 0.99 | 613 |
| stroke 22 | 59 % → 59 % | 398.7 px | 0.40 | 0.99 | 605 |
| stroke 23 | 62 % → 60 % | 403.3 px | 0.40 | 0.96 | 406 |
| stroke 24 | 58 % → 55 % | 398.9 px | 0.41 | 0.95 | 269 |
| stroke 25 | 53 % → 51 % | 348.1 px | 0.40 | 0.95 | 457 |
| stroke 26 | 48 % → 44 % | 297.3 px | 0.40 | 0.92 | 576 |
| stroke 27 | 49 % → 44 % | 239.3 px | 0.39 | 0.91 | 470 |

Numbers say: wet paint spreads well beyond the stroke.

## Surface test · Surface test · smooth panel — own sheet
own sheet 600 × 600 · Gouache 1.00 + turpentine 40 % · 70 px · 11.9 s

![Surface test · Surface test · smooth panel — own sheet](Surface-test-Surface-test-smooth-panel-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 12 % → 42 % | 33.5 px | 0.35 | 3.51 | 326 |
| stroke 2 | 17 % → 39 % | 53.3 px | 0.32 | 2.31 | 355 |
| stroke 3 | 19 % → 28 % | 60.6 px | 0.28 | 1.49 | 424 |
| stroke 4 | 31 % → 19 % | 70.2 px | 0.27 | 0.62 | 439 |
| stroke 5 | 18 % → 35 % | 46.2 px | 0.54 | 1.94 | 387 |
| stroke 6 | 28 % → 43 % | 94.2 px | 0.39 | 1.53 | 456 |
| stroke 7 | 28 % → 36 % | 91.4 px | 0.35 | 1.31 | 459 |
| stroke 8 | 38 % → 37 % | 127.3 px | 0.16 | 0.96 | 486 |
| stroke 9 | 45 % → 25 % | 123.5 px | 0.18 | 0.55 | 172 |

Numbers say: wet paint spreads well beyond the stroke.

## Surface test · Surface test · paper — own sheet
own sheet 600 × 600 · Gouache 1.00 + turpentine 40 % · 70 px · 12.1 s

![Surface test · Surface test · paper — own sheet](Surface-test-Surface-test-paper-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 11 % → 41 % | 32.4 px | 0.34 | 3.54 | 414 |
| stroke 2 | 16 % → 37 % | 51.9 px | 0.31 | 2.29 | 363 |
| stroke 3 | 19 % → 27 % | 59.1 px | 0.27 | 1.47 | 345 |
| stroke 4 | 30 % → 19 % | 69.2 px | 0.26 | 0.61 | 353 |
| stroke 5 | 18 % → 35 % | 46.0 px | 0.53 | 1.93 | 460 |
| stroke 6 | 28 % → 43 % | 93.1 px | 0.38 | 1.53 | 379 |
| stroke 7 | 27 % → 34 % | 90.3 px | 0.34 | 1.26 | 323 |
| stroke 8 | 38 % → 35 % | 126.9 px | 0.14 | 0.92 | 635 |
| stroke 9 | 45 % → 23 % | 123.3 px | 0.16 | 0.51 | 186 |

Numbers say: wet paint spreads well beyond the stroke.

## Surface test · Surface test · fine canvas — own sheet
own sheet 600 × 600 · Gouache 1.00 + turpentine 40 % · 70 px · 12.1 s

![Surface test · Surface test · fine canvas — own sheet](Surface-test-Surface-test-fine-canvas-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 12 % → 42 % | 33.6 px | 0.35 | 3.50 | 372 |
| stroke 2 | 17 % → 39 % | 53.3 px | 0.32 | 2.31 | 314 |
| stroke 3 | 19 % → 28 % | 60.7 px | 0.28 | 1.48 | 358 |
| stroke 4 | 31 % → 19 % | 70.3 px | 0.27 | 0.62 | 475 |
| stroke 5 | 18 % → 35 % | 46.2 px | 0.54 | 1.94 | 387 |
| stroke 6 | 28 % → 43 % | 94.1 px | 0.39 | 1.53 | 384 |
| stroke 7 | 28 % → 36 % | 91.4 px | 0.35 | 1.31 | 430 |
| stroke 8 | 39 % → 37 % | 127.3 px | 0.16 | 0.96 | 571 |
| stroke 9 | 45 % → 25 % | 123.6 px | 0.18 | 0.55 | 171 |

Numbers say: wet paint spreads well beyond the stroke.

## Surface test · Surface test · coarse linen — own sheet
own sheet 600 × 600 · Gouache 1.00 + turpentine 40 % · 70 px · 11.9 s

![Surface test · Surface test · coarse linen — own sheet](Surface-test-Surface-test-coarse-linen-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 12 % → 41 % | 33.4 px | 0.35 | 3.50 | 417 |
| stroke 2 | 17 % → 38 % | 52.7 px | 0.32 | 2.31 | 414 |
| stroke 3 | 19 % → 28 % | 60.1 px | 0.28 | 1.47 | 437 |
| stroke 4 | 31 % → 19 % | 70.3 px | 0.26 | 0.61 | 396 |
| stroke 5 | 18 % → 35 % | 46.2 px | 0.54 | 1.93 | 526 |
| stroke 6 | 28 % → 43 % | 93.8 px | 0.38 | 1.52 | 510 |
| stroke 7 | 28 % → 36 % | 91.2 px | 0.35 | 1.29 | 349 |
| stroke 8 | 38 % → 36 % | 127.3 px | 0.15 | 0.95 | 642 |
| stroke 9 | 45 % → 24 % | 123.5 px | 0.17 | 0.54 | 211 |

Numbers say: wet paint spreads well beyond the stroke.

## Watercolour · #16 Shrigley strokes — own sheet
own sheet 600 × 600 · Watercolour 1.00 + water 30 % · 46 px · 11.9 s

![Watercolour · #16 Shrigley strokes — own sheet](Watercolour-16-Shrigley-strokes-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| s0 | 7 % → 30 % | 33.9 px | 0.40 | 4.00 | 70 |
| s1 | 6 % → 38 % | 11.8 px | 0.54 | 6.54 | 93 |
| s2 | 12 % → 24 % | 60.3 px | 0.30 | 1.98 | 102 |
| s3 | 11 % → 25 % | 32.6 px | 0.49 | 2.31 | 105 |
| s4 | 15 % → 35 % | 46.0 px | 0.50 | 2.30 | 93 |
| s5 | 21 % → 33 % | 47.5 px | 0.53 | 1.60 | 89 |
| s6 | 20 % → 27 % | 61.4 px | 0.43 | 1.33 | 108 |
| s7 | 29 % → 43 % | 44.7 px | 0.53 | 1.51 | 75 |
| s8 | 24 % → 30 % | 108.9 px | 0.40 | 1.25 | 85 |

Numbers say: wet paint spreads well beyond the stroke.

## Watercolour · #29 Shrigley asterisk — own sheet
own sheet 600 × 600 · Watercolour 1.00 + water 50 % · 70 px · 15.4 s

![Watercolour · #29 Shrigley asterisk — own sheet](Watercolour-29-Shrigley-asterisk-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 28 % → 63 % | 98.2 px | 0.65 | 2.25 | 456 |
| stroke 2 | 24 % → 24 % | 170.9 px | 0.65 | 1.00 | 550 |
| stroke 3 | 50 % → 63 % | 179.7 px | 0.66 | 1.24 | 613 |
| stroke 4 | 42 % → 42 % | 300.0 px | 0.65 | 1.00 | 524 |

Numbers say: wet paint spreads well beyond the stroke.

## Watercolour · #33 Red band, pink flames — own sheet
own sheet 600 × 600 · Watercolour 1.00 + water 60 % · 90 px · 21.4 s

![Watercolour · #33 Red band, pink flames — own sheet](Watercolour-33-Red-band-pink-flames-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 25 % → 62 % | 101.7 px | 0.35 | 2.49 | 806 |
| stroke 2 | 29 % → 65 % | 179.9 px | 0.29 | 2.27 | 115 |
| stroke 3 | 32 % → 62 % | 250.9 px | 0.29 | 1.92 | 183 |
| stroke 4 | 37 % → 66 % | 300.7 px | 0.28 | 1.80 | 218 |
| stroke 5 | 36 % → 68 % | 342.1 px | 0.26 | 1.88 | 113 |
| stroke 6 | 38 % → 64 % | 301.6 px | 0.26 | 1.67 | 129 |
| stroke 7 | 47 % → 65 % | 263.1 px | 0.24 | 1.39 | 107 |

Numbers say: wet paint spreads well beyond the stroke.

## Watercolour · #35 Red band with runs — own sheet
own sheet 600 × 600 · Watercolour 1.00 + water 75 % · 80 px · 15.1 s

![Watercolour · #35 Red band with runs — own sheet](Watercolour-35-Red-band-with-runs-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 37 % → 48 % | 147.3 px | 0.20 | 1.27 | 648 |

## Watercolour · #40 Olive and sepia blooms — own sheet
own sheet 600 × 600 · Watercolour 1.00 + water 55 % · 90 px · 19.9 s

![Watercolour · #40 Olive and sepia blooms — own sheet](Watercolour-40-Olive-and-sepia-blooms-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 27 % → 58 % | 94.6 px | 0.21 | 2.14 | 1403 |
| stroke 2 | 47 % → 62 % | 150.8 px | 0.22 | 1.31 | 935 |

Numbers say: wet paint spreads well beyond the stroke.

## Watercolour · #46 Lips on wet paper — own sheet
own sheet 600 × 600 · Watercolour 1.00 + water 65 % · 50 px · 12.6 s

![Watercolour · #46 Lips on wet paper — own sheet](Watercolour-46-Lips-on-wet-paper-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 13 % → 31 % | 56.0 px | 0.53 | 2.32 | 234 |
| stroke 2 | 15 % → 32 % | 63.8 px | 0.52 | 2.20 | 106 |

Numbers say: wet paint spreads well beyond the stroke.

