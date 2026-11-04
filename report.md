![All brushes](contact.png)

# Brush Lab — 150 brushes · Nov 4, 2026 at 7:07 AM

Every sheet: 1500 × 600, ten strokes in a 5 × 2 grid — 1. light line · 2. heavy line · 3. pressure swell · 4. fast wave · 5. slow wave · 6. spiral · 7. loop · 8. tilted · 9. over the wet one · 10. long, no reload (cell 8 holds «tilted» and «over the wet one» crossed). The CPU reference of Mamay's paint engine; the wet layer settles 20 s at the end.

Columns: **covered** = share of the cell with paint right after the stroke → after settling; **width** = painted area of the stroke ÷ its length (px); **dark** = mean darkness of the painted pixels above the paper's own grain (0 = paper, 1 = black); **spread** = how far wet paint went beyond the stroke (1.0 = stayed); **ms** = the stroke on the CPU; long stroke: paint in each quarter of its length (it should run out: wet → streaks → dry tail).

## Ink Line
Ink · 12 px · 30.4 s

![Ink Line](Ink-Line.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 1 % → 4 % | 4.3 px | 0.55 | 2.44 | 97 |
| heavy line | 5 % → 6 % | 15.7 px | 0.68 | 1.13 | 81 |
| pressure swell | 3 % → 4 % | 11.3 px | 0.64 | 1.40 | 55 |
| fast wave | 10 % → 11 % | 11.2 px | 0.59 | 1.11 | 149 |
| slow wave | 8 % → 10 % | 9.6 px | 0.57 | 1.16 | 143 |
| spiral | 14 % → 15 % | 8.9 px | 0.50 | 1.07 | 286 |
| loop | 8 % → 9 % | 10.6 px | 0.61 | 1.16 | 226 |
| tilted | 5 % → 5 % | 14.4 px | 0.65 | 1.05 | 101 |
| over the wet one | 10 % → 11 % | 12.5 px | 0.65 | 1.15 | 77 |
| long, no reload | 18 % → 17 % | 8.1 px | 0.47 | 0.96 | 391 | quarters: 0.22 → 0.09 → 0.04 → 0.02

Numbers say: light vs heavy: width 4.3 → 15.7 px, dark 0.55 → 0.68; wet paint spreads well beyond the stroke.

## Dense Ink
Ink · 14 px · 31.0 s

![Dense Ink](Dense-Ink.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 5 % → 7 % | 15.2 px | 0.72 | 1.26 | 106 |
| heavy line | 7 % → 7 % | 19.1 px | 0.73 | 1.09 | 92 |
| pressure swell | 5 % → 6 % | 17.9 px | 0.72 | 1.17 | 68 |
| fast wave | 13 % → 13 % | 15.3 px | 0.69 | 1.01 | 159 |
| slow wave | 12 % → 12 % | 13.6 px | 0.67 | 1.04 | 203 |
| spiral | 18 % → 15 % | 12.2 px | 0.65 | 0.80 | 317 |
| loop | 11 % → 12 % | 14.8 px | 0.69 | 1.08 | 205 |
| tilted | 5 % → 6 % | 14.6 px | 0.72 | 1.07 | 103 |
| over the wet one | 12 % → 13 % | 17.7 px | 0.72 | 1.11 | 97 |
| long, no reload | 23 % → 15 % | 10.1 px | 0.64 | 0.66 | 446 | quarters: 0.30 → 0.12 → 0.04 → 0.02

Numbers say: light vs heavy: width 15.2 → 19.1 px, dark 0.72 → 0.73.

## Transparent Wash
Watercolor · 22 px · 32.5 s

![Transparent Wash](Transparent-Wash.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 2 % → 5 % | 6.9 px | 0.27 | 2.25 | 91 |
| heavy line | 7 % → 9 % | 20.4 px | 0.27 | 1.22 | 87 |
| pressure swell | 4 % → 6 % | 15.2 px | 0.28 | 1.54 | 54 |
| fast wave | 14 % → 16 % | 16.1 px | 0.20 | 1.17 | 156 |
| slow wave | 12 % → 15 % | 13.7 px | 0.21 | 1.28 | 242 |
| spiral | 18 % → 22 % | 11.9 px | 0.16 | 1.23 | 217 |
| loop | 11 % → 13 % | 14.5 px | 0.22 | 1.20 | 137 |
| tilted | 8 % → 8 % | 21.1 px | 0.24 | 1.06 | 100 |
| over the wet one | 13 % → 16 % | 16.4 px | 0.24 | 1.18 | 62 |
| long, no reload | 26 % → 32 % | 11.6 px | 0.13 | 1.22 | 368 | quarters: 0.11 → 0.04 → 0.02 → 0.01

Numbers say: light vs heavy: width 6.9 → 20.4 px, dark 0.27 → 0.27; wet paint spreads well beyond the stroke.

## Dry Brush
Gouache · 24 px · 27.8 s

![Dry Brush](Dry-Brush.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 5 % → 0 % | 14.0 px | 0.65 | 0.09 | 84 |
| heavy line | 6 % → 0 % | 18.6 px | 0.65 | 0.02 | 176 |
| pressure swell | 5 % → 0 % | 18.2 px | 0.65 | 0.08 | 67 |
| fast wave | 6 % → 1 % | 7.3 px | 0.65 | 0.08 | 272 |
| slow wave | 7 % → 0 % | 8.1 px | 0.65 | 0.06 | 339 |
| spiral | 7 % → 0 % | 4.6 px | 0.65 | 0.07 | 417 |
| loop | 10 % → 0 % | 12.4 px | 0.65 | 0.04 | 177 |
| tilted | 4 % → 3 % | 10.6 px | 0.65 | 0.88 | 95 |
| over the wet one | 9 % → 1 % | 14.5 px | 0.65 | 0.12 | 85 |
| long, no reload | 6 % → 1 % | 2.9 px | 0.65 | 0.14 | 456 | quarters: 0.12 → 0.00 → 0.00 → 0.00

Numbers say: light vs heavy: width 14.0 → 18.6 px, dark 0.65 → 0.65.

## Wax Crayon
Wax · 8 px · 13.7 s

![Wax Crayon](Wax-Crayon.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 1 % → 1 % | 2.5 px | 0.71 | 1.00 | 24 |
| heavy line | 1 % → 1 % | 3.9 px | 0.69 | 1.00 | 34 |
| pressure swell | 1 % → 1 % | 3.3 px | 0.70 | 1.00 | 14 |
| fast wave | 3 % → 3 % | 3.5 px | 0.69 | 1.00 | 64 |
| slow wave | 3 % → 3 % | 3.4 px | 0.70 | 1.00 | 75 |
| spiral | 5 % → 5 % | 3.3 px | 0.70 | 1.00 | 112 |
| loop | 3 % → 3 % | 3.3 px | 0.70 | 1.00 | 52 |
| tilted | 2 % → 2 % | 5.6 px | 0.68 | 1.00 | 44 |
| over the wet one | 3 % → 3 % | 3.6 px | 0.68 | 1.00 | 20 |
| long, no reload | 7 % → 7 % | 3.3 px | 0.70 | 1.00 | 151 | quarters: 0.06 → 0.06 → 0.06 → 0.06

Numbers say: light vs heavy: width 2.5 → 3.9 px, dark 0.71 → 0.69; the long stroke does not run out of paint.

## Oil Pastel
Wax · 12 px · 13.3 s

![Oil Pastel](Oil-Pastel.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 1 % → 1 % | 4.0 px | 0.68 | 1.00 | 26 |
| heavy line | 2 % → 2 % | 6.5 px | 0.68 | 1.00 | 41 |
| pressure swell | 2 % → 2 % | 5.7 px | 0.69 | 1.00 | 28 |
| fast wave | 5 % → 5 % | 5.7 px | 0.68 | 1.00 | 103 |
| slow wave | 5 % → 5 % | 5.5 px | 0.68 | 1.00 | 83 |
| spiral | 8 % → 8 % | 5.5 px | 0.68 | 1.00 | 143 |
| loop | 4 % → 4 % | 5.6 px | 0.68 | 1.00 | 67 |
| tilted | 2 % → 2 % | 6.8 px | 0.68 | 1.00 | 60 |
| over the wet one | 5 % → 5 % | 5.8 px | 0.68 | 1.00 | 40 |
| long, no reload | 13 % → 13 % | 5.6 px | 0.68 | 1.00 | 280 | quarters: 0.10 → 0.09 → 0.10 → 0.10

Numbers say: light vs heavy: width 4.0 → 6.5 px, dark 0.68 → 0.68; the long stroke does not run out of paint.

## Charcoal
Charcoal · 5 px · 14.3 s

![Charcoal](Charcoal.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 1 % → 1 % | 2.0 px | 0.74 | 1.00 | 28 |
| heavy line | 1 % → 1 % | 3.0 px | 0.74 | 1.00 | 17 |
| pressure swell | 1 % → 1 % | 2.7 px | 0.74 | 1.00 | 9 |
| fast wave | 2 % → 2 % | 2.7 px | 0.73 | 1.00 | 39 |
| slow wave | 2 % → 2 % | 2.6 px | 0.74 | 1.00 | 29 |
| spiral | 4 % → 4 % | 2.5 px | 0.74 | 1.00 | 64 |
| loop | 2 % → 2 % | 2.6 px | 0.74 | 1.00 | 31 |
| tilted | 2 % → 2 % | 4.3 px | 0.72 | 1.00 | 23 |
| over the wet one | 2 % → 2 % | 2.4 px | 0.72 | 1.00 | 12 |
| long, no reload | 6 % → 6 % | 2.7 px | 0.73 | 1.00 | 90 | quarters: 0.05 → 0.05 → 0.05 → 0.05

Numbers say: light vs heavy: width 2.0 → 3.0 px, dark 0.74 → 0.74; the long stroke does not run out of paint.

## Impasto
Heavy acrylic · 22 px · 20.8 s

![Impasto](Impasto.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 8 % → 8 % | 24.1 px | 0.71 | 0.93 | 85 |
| heavy line | 10 % → 9 % | 28.8 px | 0.70 | 0.94 | 120 |
| pressure swell | 7 % → 7 % | 28.1 px | 0.72 | 0.94 | 67 |
| fast wave | 20 % → 13 % | 23.5 px | 0.71 | 0.64 | 203 |
| slow wave | 21 % → 14 % | 24.5 px | 0.71 | 0.66 | 323 |
| spiral | 30 % → 14 % | 20.0 px | 0.71 | 0.46 | 656 |
| loop | 18 % → 14 % | 23.9 px | 0.71 | 0.77 | 315 |
| tilted | 8 % → 8 % | 21.8 px | 0.70 | 1.00 | 201 |
| over the wet one | 17 % → 15 % | 25.4 px | 0.70 | 0.91 | 170 |
| long, no reload | 34 % → 14 % | 15.2 px | 0.71 | 0.41 | 635 | quarters: 0.38 → 0.21 → 0.10 → 0.03

Numbers say: light vs heavy: width 24.1 → 28.8 px, dark 0.71 → 0.70.

## Oil Round
Oil · 18 px · 22.6 s

![Oil Round](Oil-Round.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 2 % → 2 % | 7.2 px | 0.75 | 1.00 | 57 |
| heavy line | 7 % → 7 % | 19.3 px | 0.73 | 1.00 | 128 |
| pressure swell | 4 % → 4 % | 13.7 px | 0.72 | 1.00 | 58 |
| fast wave | 11 % → 11 % | 12.7 px | 0.65 | 1.00 | 208 |
| slow wave | 8 % → 8 % | 9.0 px | 0.57 | 1.00 | 240 |
| spiral | 10 % → 10 % | 6.6 px | 0.50 | 1.00 | 295 |
| loop | 5 % → 5 % | 7.1 px | 0.45 | 1.00 | 167 |
| tilted | 4 % → 4 % | 10.1 px | 0.52 | 1.00 | 88 |
| over the wet one | 6 % → 6 % | 7.4 px | 0.52 | 1.00 | 73 |
| long, no reload | 15 % → 15 % | 6.8 px | 0.42 | 1.00 | 455 | quarters: 0.08 → 0.08 → 0.07 → 0.06

Numbers say: light vs heavy: width 7.2 → 19.3 px, dark 0.75 → 0.73.

## Palette Knife
Oil · 20 px · 22.1 s

![Palette Knife](Palette-Knife.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 8 % → 8 % | 21.9 px | 0.67 | 1.00 | 36 |
| heavy line | 8 % → 8 % | 22.5 px | 0.73 | 1.00 | 15 |
| pressure swell | 6 % → 6 % | 22.4 px | 0.74 | 1.00 | 8 |
| fast wave | 17 % → 17 % | 19.3 px | 0.49 | 1.00 | 42 |
| slow wave | 17 % → 17 % | 19.9 px | 0.43 | 1.00 | 54 |
| spiral | 18 % → 18 % | 11.7 px | 0.45 | 1.00 | 65 |
| loop | 16 % → 16 % | 21.0 px | 0.58 | 1.00 | 33 |
| tilted | 5 % → 5 % | 15.0 px | 0.72 | 1.00 | 14 |
| over the wet one | 13 % → 13 % | 21.0 px | 0.72 | 1.00 | 13 |
| long, no reload | 17 % → 17 % | 7.5 px | 0.47 | 1.00 | 85 | quarters: 0.29 → 0.05 → 0.00 → 0.00

Numbers say: light vs heavy: width 21.9 → 22.5 px, dark 0.67 → 0.73; pressure barely changes the width.

## Water
Watercolor · 20 px · 42.2 s · over bands of wet oil paint and oil pastel in turn (it works on paint already there: look at what it does to the bands; covered counts the bands too)

![Water](Water.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 25 % → 27 % | 73.8 px | 0.80 | 1.06 | 37 |
| heavy line | 24 % → 25 % | 69.8 px | 0.81 | 1.04 | 79 |
| pressure swell | 24 % → 25 % | 89.6 px | 0.81 | 1.03 | 45 |
| fast wave | 24 % → 26 % | 27.7 px | 0.81 | 1.07 | 153 |
| slow wave | 24 % → 25 % | 27.7 px | 0.81 | 1.06 | 188 |
| spiral | 24 % → 26 % | 15.9 px | 0.81 | 1.07 | 252 |
| loop | 24 % → 25 % | 31.1 px | 0.81 | 1.03 | 148 |
| tilted | 24 % → 24 % | 67.0 px | 0.81 | 1.00 | 109 |
| over the wet one | 24 % → 25 % | 0.0 px | 0.81 | 1.06 | 110 |
| long, no reload | 24 % → 26 % | 10.7 px | 0.81 | 1.08 | 406 | quarters: 0.21 → 0.27 → 0.18 → 0.27

Numbers say: light vs heavy: width 73.8 → 69.8 px, dark 0.80 → 0.81; pressure barely changes the width; the long stroke does not run out of paint.

## Blender
Pastel · 16 px · 23.5 s · over bands of wet oil paint and oil pastel in turn (it works on paint already there: look at what it does to the bands; covered counts the bands too)

![Blender](Blender.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 24 % → 24 % | 70.7 px | 0.81 | 1.00 | 25 |
| heavy line | 25 % → 25 % | 72.1 px | 0.80 | 1.00 | 39 |
| pressure swell | 24 % → 24 % | 91.3 px | 0.81 | 1.00 | 29 |
| fast wave | 26 % → 26 % | 30.0 px | 0.79 | 1.00 | 115 |
| slow wave | 26 % → 26 % | 29.9 px | 0.80 | 1.00 | 133 |
| spiral | 28 % → 28 % | 18.7 px | 0.77 | 1.00 | 145 |
| loop | 25 % → 25 % | 32.9 px | 0.80 | 1.00 | 78 |
| tilted | 25 % → 25 % | 70.1 px | 0.79 | 1.00 | 65 |
| over the wet one | 26 % → 26 % | 1.8 px | 0.79 | 1.00 | 41 |
| long, no reload | 30 % → 30 % | 13.7 px | 0.76 | 1.00 | 240 | quarters: 0.20 → 0.28 → 0.23 → 0.30

Numbers say: light vs heavy: width 70.7 → 72.1 px, dark 0.81 → 0.80; pressure barely changes the width; the long stroke does not run out of paint.

## Eraser
Eraser · 16 px · 23.1 s · over bands of wet oil paint and oil pastel in turn (it works on paint already there: look at what it does to the bands; covered counts the bands too)

![Eraser](Eraser.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 24 % → 24 % | 69.5 px | 0.82 | 1.00 | 39 |
| heavy line | 23 % → 23 % | 67.9 px | 0.82 | 1.00 | 36 |
| pressure swell | 23 % → 23 % | 87.3 px | 0.82 | 1.00 | 33 |
| fast wave | 22 % → 22 % | 25.7 px | 0.82 | 1.00 | 92 |
| slow wave | 22 % → 22 % | 25.7 px | 0.82 | 1.00 | 108 |
| spiral | 22 % → 22 % | 14.4 px | 0.82 | 1.00 | 166 |
| loop | 22 % → 22 % | 28.6 px | 0.82 | 1.00 | 93 |
| tilted | 23 % → 23 % | 65.1 px | 0.82 | 1.00 | 59 |
| over the wet one | 23 % → 23 % | 0.0 px | 0.82 | 1.00 | 36 |
| long, no reload | 20 % → 20 % | 8.9 px | 0.82 | 1.00 | 221 | quarters: 0.15 → 0.20 → 0.15 → 0.20

Numbers say: light vs heavy: width 69.5 → 67.9 px, dark 0.82 → 0.82; pressure barely changes the width; the long stroke does not run out of paint.

## Fan
Gouache · 30 px · 44.0 s

![Fan](Fan.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 9 % → 3 % | 25.7 px | 0.63 | 0.37 | 60 |
| heavy line | 11 % → 4 % | 31.0 px | 0.63 | 0.39 | 65 |
| pressure swell | 8 % → 5 % | 31.7 px | 0.63 | 0.55 | 37 |
| fast wave | 18 % → 5 % | 20.3 px | 0.63 | 0.26 | 129 |
| slow wave | 18 % → 5 % | 21.1 px | 0.63 | 0.25 | 245 |
| spiral | 24 % → 5 % | 15.8 px | 0.63 | 0.20 | 238 |
| loop | 17 % → 5 % | 22.7 px | 0.63 | 0.29 | 152 |
| tilted | 5 % → 6 % | 15.1 px | 0.63 | 1.05 | 50 |
| over the wet one | 16 % → 8 % | 29.8 px | 0.63 | 0.50 | 64 |
| long, no reload | 23 % → 5 % | 10.1 px | 0.63 | 0.22 | 504 | quarters: 0.29 → 0.07 → 0.01 → 0.00

Numbers say: light vs heavy: width 25.7 → 31.0 px, dark 0.63 → 0.63.

## Sponge
Gouache · 30 px · 43.3 s

![Sponge](Sponge.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 4 % → 0 % | 11.4 px | 0.62 | 0.12 | 98 |
| heavy line | 12 % → 2 % | 35.4 px | 0.62 | 0.14 | 83 |
| pressure swell | 7 % → 2 % | 27.9 px | 0.62 | 0.27 | 58 |
| fast wave | 20 % → 4 % | 23.2 px | 0.62 | 0.19 | 186 |
| slow wave | 21 % → 4 % | 23.7 px | 0.62 | 0.18 | 310 |
| spiral | 28 % → 4 % | 18.3 px | 0.62 | 0.14 | 251 |
| loop | 18 % → 5 % | 23.0 px | 0.62 | 0.29 | 148 |
| tilted | 7 % → 7 % | 18.2 px | 0.62 | 1.04 | 148 |
| over the wet one | 16 % → 6 % | 27.8 px | 0.62 | 0.37 | 95 |
| long, no reload | 29 % → 5 % | 12.9 px | 0.62 | 0.17 | 712 | quarters: 0.29 → 0.13 → 0.07 → 0.04

Numbers say: light vs heavy: width 11.4 → 35.4 px, dark 0.62 → 0.62.

## Ink — sumi brush
Watercolor · 22 px · 46.8 s

![Ink — sumi brush](Ink-sumi-brush.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 8 % → 9 % | 23.9 px | 0.87 | 1.12 | 79 |
| heavy line | 13 % → 13 % | 38.1 px | 0.87 | 1.01 | 79 |
| pressure swell | 9 % → 10 % | 34.5 px | 0.87 | 1.04 | 62 |
| fast wave | 28 % → 28 % | 32.6 px | 0.85 | 1.00 | 253 |
| slow wave | 26 % → 26 % | 29.8 px | 0.86 | 1.02 | 368 |
| spiral | 39 % → 38 % | 25.5 px | 0.81 | 0.99 | 446 |
| loop | 22 % → 22 % | 28.6 px | 0.87 | 1.02 | 438 |
| tilted | 9 % → 9 % | 25.4 px | 0.87 | 1.00 | 114 |
| over the wet one | 20 % → 21 % | 30.6 px | 0.87 | 1.03 | 79 |
| long, no reload | 45 % → 43 % | 20.3 px | 0.76 | 0.95 | 1129 | quarters: 0.56 → 0.45 → 0.30 → 0.20

Numbers say: light vs heavy: width 23.9 → 38.1 px, dark 0.87 → 0.87.

## Ink — wash
Watercolor · 40 px · 44.5 s

![Ink — wash](Ink-wash.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 13 % → 13 % | 37.6 px | 0.77 | 1.01 | 121 |
| heavy line | 19 % → 19 % | 55.6 px | 0.72 | 1.00 | 127 |
| pressure swell | 13 % → 13 % | 48.6 px | 0.76 | 1.01 | 93 |
| fast wave | 42 % → 42 % | 48.3 px | 0.69 | 1.01 | 285 |
| slow wave | 40 % → 40 % | 45.8 px | 0.75 | 1.01 | 705 |
| spiral | 61 % → 62 % | 40.3 px | 0.69 | 1.01 | 784 |
| loop | 34 % → 34 % | 44.0 px | 0.75 | 1.00 | 203 |
| tilted | 15 % → 15 % | 41.2 px | 0.76 | 1.00 | 127 |
| over the wet one | 30 % → 31 % | 43.4 px | 0.76 | 1.02 | 98 |
| long, no reload | 74 % → 75 % | 33.1 px | 0.64 | 1.02 | 639 | quarters: 0.68 → 0.60 → 0.47 → 0.33

Numbers say: light vs heavy: width 37.6 → 55.6 px, dark 0.77 → 0.72.

## Ink — dry brush
Ink · 30 px · 30.1 s

![Ink — dry brush](Ink-dry-brush.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 9 % → 7 % | 25.4 px | 0.81 | 0.78 | 120 |
| heavy line | 10 % → 8 % | 29.9 px | 0.79 | 0.75 | 156 |
| pressure swell | 7 % → 6 % | 28.1 px | 0.81 | 0.84 | 122 |
| fast wave | 21 % → 8 % | 24.3 px | 0.79 | 0.40 | 383 |
| slow wave | 17 % → 7 % | 20.2 px | 0.79 | 0.39 | 769 |
| spiral | 23 % → 8 % | 15.4 px | 0.78 | 0.34 | 669 |
| loop | 19 % → 8 % | 24.4 px | 0.78 | 0.44 | 263 |
| tilted | 8 % → 8 % | 22.7 px | 0.78 | 1.02 | 176 |
| over the wet one | 17 % → 14 % | 25.9 px | 0.78 | 0.81 | 120 |
| long, no reload | 20 % → 8 % | 9.0 px | 0.79 | 0.42 | 621 | quarters: 0.32 → 0.02 → 0.00 → 0.00

Numbers say: light vs heavy: width 25.4 → 29.9 px, dark 0.81 → 0.79.

## Ink — nib
Watercolor · 5 px · 27.9 s

![Ink — nib](Ink-nib.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 2 % → 5 % | 5.5 px | 0.89 | 2.46 | 48 |
| heavy line | 2 % → 5 % | 6.4 px | 0.89 | 2.33 | 33 |
| pressure swell | 2 % → 4 % | 6.2 px | 0.89 | 2.52 | 32 |
| fast wave | 5 % → 8 % | 6.0 px | 0.89 | 1.62 | 79 |
| slow wave | 5 % → 8 % | 5.7 px | 0.89 | 1.69 | 75 |
| spiral | 8 % → 11 % | 5.0 px | 0.88 | 1.40 | 180 |
| loop | 4 % → 8 % | 5.7 px | 0.89 | 1.73 | 85 |
| tilted | 4 % → 4 % | 10.3 px | 0.89 | 1.02 | 34 |
| over the wet one | 6 % → 9 % | 6.1 px | 0.89 | 1.61 | 45 |
| long, no reload | 10 % → 12 % | 4.3 px | 0.86 | 1.29 | 190 | quarters: 0.24 → 0.11 → 0.07 → 0.05

Numbers say: light vs heavy: width 5.5 → 6.4 px, dark 0.89 → 0.89; wet paint spreads well beyond the stroke.

## 0.45 · Dry brush
Gouache · 34 px · 31.3 s

![0.45 · Dry brush](0-45-Dry-brush.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 8 % → 2 % | 23.2 px | 0.68 | 0.30 | 194 |
| heavy line | 8 % → 3 % | 24.3 px | 0.68 | 0.32 | 207 |
| pressure swell | 7 % → 3 % | 25.6 px | 0.68 | 0.42 | 134 |
| fast wave | 14 % → 3 % | 15.7 px | 0.68 | 0.22 | 408 |
| slow wave | 16 % → 3 % | 18.7 px | 0.68 | 0.20 | 613 |
| spiral | 20 % → 3 % | 13.4 px | 0.68 | 0.15 | 825 |
| loop | 14 % → 4 % | 18.3 px | 0.68 | 0.26 | 292 |
| tilted | 7 % → 7 % | 18.9 px | 0.68 | 1.01 | 164 |
| over the wet one | 15 % → 6 % | 23.1 px | 0.68 | 0.43 | 175 |
| long, no reload | 21 % → 4 % | 9.4 px | 0.68 | 0.18 | 1564 | quarters: 0.28 → 0.14 → 0.07 → 0.03

Numbers say: light vs heavy: width 23.2 → 24.3 px, dark 0.68 → 0.68; pressure barely changes the width.

## Dry pastel
Pastel · 26 px · 14.7 s

![Dry pastel](Dry-pastel.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 3 % → 3 % | 8.3 px | 0.38 | 1.00 | 42 |
| heavy line | 5 % → 5 % | 13.2 px | 0.39 | 1.00 | 39 |
| pressure swell | 3 % → 3 % | 11.7 px | 0.38 | 1.00 | 39 |
| fast wave | 10 % → 10 % | 11.9 px | 0.39 | 1.00 | 135 |
| slow wave | 10 % → 10 % | 11.3 px | 0.39 | 1.00 | 260 |
| spiral | 15 % → 15 % | 9.6 px | 0.39 | 1.00 | 266 |
| loop | 7 % → 7 % | 9.4 px | 0.39 | 1.00 | 97 |
| tilted | 3 % → 3 % | 8.3 px | 0.38 | 1.00 | 46 |
| over the wet one | 7 % → 7 % | 11.1 px | 0.38 | 1.00 | 42 |
| long, no reload | 18 % → 18 % | 8.2 px | 0.39 | 1.00 | 267 | quarters: 0.08 → 0.08 → 0.08 → 0.07

Numbers say: light vs heavy: width 8.3 → 13.2 px, dark 0.38 → 0.39; the long stroke does not run out of paint.

## 0.45 · Charcoal
Charcoal · 18 px · 12.5 s

![0.45 · Charcoal](0-45-Charcoal.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 2 % → 2 % | 6.5 px | 0.80 | 1.00 | 32 |
| heavy line | 3 % → 3 % | 9.2 px | 0.80 | 1.00 | 32 |
| pressure swell | 2 % → 2 % | 8.8 px | 0.80 | 1.00 | 25 |
| fast wave | 7 % → 7 % | 8.5 px | 0.80 | 1.00 | 81 |
| slow wave | 7 % → 7 % | 8.0 px | 0.80 | 1.00 | 100 |
| spiral | 12 % → 12 % | 7.9 px | 0.80 | 1.00 | 77 |
| loop | 6 % → 6 % | 8.1 px | 0.80 | 1.00 | 41 |
| tilted | 3 % → 3 % | 7.5 px | 0.80 | 1.00 | 38 |
| over the wet one | 6 % → 6 % | 7.9 px | 0.80 | 1.00 | 24 |
| long, no reload | 17 % → 17 % | 7.8 px | 0.80 | 1.00 | 153 | quarters: 0.15 → 0.16 → 0.15 → 0.16

Numbers say: light vs heavy: width 6.5 → 9.2 px, dark 0.80 → 0.80; the long stroke does not run out of paint.

## Watercolour — wash
Watercolor · 50 px · 43.2 s

![Watercolour — wash](Watercolour-wash.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 16 % → 16 % | 45.5 px | 0.22 | 1.00 | 107 |
| heavy line | 22 % → 22 % | 64.9 px | 0.19 | 1.00 | 125 |
| pressure swell | 15 % → 15 % | 56.1 px | 0.22 | 1.01 | 84 |
| fast wave | 48 % → 49 % | 55.6 px | 0.19 | 1.01 | 291 |
| slow wave | 46 % → 46 % | 53.3 px | 0.24 | 1.00 | 785 |
| spiral | 66 % → 66 % | 43.7 px | 0.21 | 1.00 | 709 |
| loop | 40 % → 40 % | 51.4 px | 0.22 | 1.00 | 277 |
| tilted | 18 % → 18 % | 49.7 px | 0.23 | 1.00 | 175 |
| over the wet one | 36 % → 36 % | 49.6 px | 0.23 | 1.01 | 106 |
| long, no reload | 84 % → 84 % | 37.7 px | 0.20 | 1.00 | 682 | quarters: 0.24 → 0.20 → 0.16 → 0.12

Numbers say: light vs heavy: width 45.5 → 64.9 px, dark 0.22 → 0.19.

## Watercolour — wet-in-wet
Watercolor · 44 px · 43.8 s

![Watercolour — wet-in-wet](Watercolour-wet-in-wet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 13 % → 19 % | 38.4 px | 0.34 | 1.43 | 115 |
| heavy line | 19 % → 20 % | 54.6 px | 0.36 | 1.05 | 102 |
| pressure swell | 12 % → 15 % | 46.5 px | 0.37 | 1.22 | 66 |
| fast wave | 41 % → 45 % | 47.7 px | 0.35 | 1.09 | 233 |
| slow wave | 40 % → 45 % | 46.2 px | 0.42 | 1.12 | 397 |
| spiral | 63 % → 67 % | 41.5 px | 0.38 | 1.06 | 495 |
| loop | 34 % → 37 % | 44.4 px | 0.40 | 1.09 | 254 |
| tilted | 15 % → 16 % | 41.5 px | 0.38 | 1.06 | 152 |
| over the wet one | 31 % → 37 % | 43.9 px | 0.38 | 1.21 | 88 |
| long, no reload | 78 % → 84 % | 34.8 px | 0.37 | 1.08 | 897 | quarters: 0.39 → 0.37 → 0.32 → 0.26

Numbers say: light vs heavy: width 38.4 → 54.6 px, dark 0.34 → 0.36.

## Watercolour — glaze
Watercolor · 38 px · 39.4 s

![Watercolour — glaze](Watercolour-glaze.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 13 % → 13 % | 36.6 px | 0.07 | 1.01 | 95 |
| heavy line | 19 % → 19 % | 55.4 px | 0.07 | 1.00 | 117 |
| pressure swell | 13 % → 13 % | 47.0 px | 0.07 | 1.01 | 90 |
| fast wave | 40 % → 40 % | 45.6 px | 0.07 | 1.01 | 230 |
| slow wave | 37 % → 37 % | 42.8 px | 0.07 | 1.01 | 507 |
| spiral | 59 % → 60 % | 38.8 px | 0.06 | 1.01 | 561 |
| loop | 33 % → 33 % | 42.6 px | 0.07 | 1.00 | 205 |
| tilted | 14 % → 14 % | 40.1 px | 0.07 | 1.00 | 152 |
| over the wet one | 30 % → 30 % | 42.3 px | 0.07 | 1.01 | 116 |
| long, no reload | 69 % → 70 % | 30.9 px | 0.06 | 1.01 | 655 | quarters: 0.06 → 0.05 → 0.03 → 0.02

Numbers say: light vs heavy: width 36.6 → 55.4 px, dark 0.07 → 0.07.

## Watercolour — granulating
Watercolor · 44 px · 43.2 s

![Watercolour — granulating](Watercolour-granulating.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 14 % → 14 % | 41.4 px | 0.35 | 1.00 | 105 |
| heavy line | 21 % → 21 % | 60.4 px | 0.31 | 1.00 | 130 |
| pressure swell | 14 % → 14 % | 52.2 px | 0.34 | 1.01 | 71 |
| fast wave | 45 % → 45 % | 51.7 px | 0.29 | 1.01 | 365 |
| slow wave | 42 % → 42 % | 48.2 px | 0.35 | 1.01 | 484 |
| spiral | 62 % → 63 % | 41.0 px | 0.30 | 1.01 | 445 |
| loop | 37 % → 37 % | 47.6 px | 0.33 | 1.00 | 251 |
| tilted | 16 % → 16 % | 45.5 px | 0.35 | 1.00 | 167 |
| over the wet one | 33 % → 33 % | 46.2 px | 0.35 | 1.01 | 145 |
| long, no reload | 75 % → 76 % | 33.6 px | 0.29 | 1.01 | 1063 | quarters: 0.34 → 0.26 → 0.20 → 0.14

Numbers say: light vs heavy: width 41.4 → 60.4 px, dark 0.35 → 0.31.

## Watercolour — dry brush
Watercolor · 36 px · 35.9 s

![Watercolour — dry brush](Watercolour-dry-brush.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 10 % → 10 % | 28.0 px | 0.17 | 1.01 | 124 |
| heavy line | 14 % → 13 % | 40.1 px | 0.16 | 0.93 | 157 |
| pressure swell | 11 % → 11 % | 40.5 px | 0.16 | 0.98 | 105 |
| fast wave | 27 % → 20 % | 30.8 px | 0.13 | 0.74 | 503 |
| slow wave | 24 % → 17 % | 28.1 px | 0.14 | 0.71 | 643 |
| spiral | 34 % → 20 % | 22.4 px | 0.13 | 0.57 | 568 |
| loop | 21 % → 18 % | 27.2 px | 0.14 | 0.86 | 276 |
| tilted | 10 % → 10 % | 28.6 px | 0.16 | 1.00 | 159 |
| over the wet one | 22 % → 20 % | 31.4 px | 0.16 | 0.95 | 150 |
| long, no reload | 36 % → 19 % | 16.1 px | 0.14 | 0.54 | 882 | quarters: 0.09 → 0.03 → 0.01 → 0.00

Numbers say: light vs heavy: width 28.0 → 40.1 px, dark 0.17 → 0.16.

## Gouache
Gouache · 30 px · 33.8 s

![Gouache](Gouache.png)

A light paint: laid on a grey sheet (on white it cannot be seen); **dark** = how far it is from the grey either way.

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 8 % → 6 % | 24.7 px | 0.28 | 0.66 | 104 |
| heavy line | 14 % → 7 % | 39.8 px | 0.28 | 0.49 | 149 |
| pressure swell | 10 % → 6 % | 38.8 px | 0.28 | 0.62 | 103 |
| fast wave | 28 % → 8 % | 32.8 px | 0.28 | 0.27 | 398 |
| slow wave | 27 % → 8 % | 31.6 px | 0.28 | 0.30 | 467 |
| spiral | 38 % → 8 % | 25.0 px | 0.28 | 0.22 | 491 |
| loop | 22 % → 8 % | 28.8 px | 0.28 | 0.36 | 215 |
| tilted | 9 % → 9 % | 24.6 px | 0.27 | 1.00 | 177 |
| over the wet one | 20 % → 13 % | 31.0 px | 0.27 | 0.67 | 115 |
| long, no reload | 40 % → 10 % | 17.9 px | 0.27 | 0.24 | 657 | quarters: 0.01 → 0.01 → 0.02 → 0.02

Numbers say: light vs heavy: width 24.7 → 39.8 px, dark 0.28 → 0.28; the long stroke does not run out of paint.

## Oil — alla prima
Oil · 30 px · 20.6 s

![Oil — alla prima](Oil-alla-prima.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 10 % → 10 % | 28.5 px | 0.51 | 1.00 | 88 |
| heavy line | 11 % → 11 % | 31.2 px | 0.51 | 1.00 | 116 |
| pressure swell | 8 % → 8 % | 30.9 px | 0.53 | 1.00 | 87 |
| fast wave | 26 % → 26 % | 29.5 px | 0.52 | 1.00 | 255 |
| slow wave | 26 % → 26 % | 30.2 px | 0.52 | 1.00 | 412 |
| spiral | 41 % → 41 % | 27.0 px | 0.51 | 1.00 | 558 |
| loop | 22 % → 22 % | 28.0 px | 0.52 | 1.00 | 304 |
| tilted | 11 % → 11 % | 31.9 px | 0.52 | 1.00 | 159 |
| over the wet one | 21 % → 21 % | 27.5 px | 0.52 | 1.00 | 111 |
| long, no reload | 50 % → 50 % | 22.5 px | 0.50 | 1.00 | 589 | quarters: 0.33 → 0.30 → 0.26 → 0.23

Numbers say: light vs heavy: width 28.5 → 31.2 px, dark 0.51 → 0.51; pressure barely changes the width.

## Oil — impasto
Oil · 34 px · 21.4 s

![Oil — impasto](Oil-impasto.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 12 % → 12 % | 34.5 px | 0.23 | 1.00 | 167 |
| heavy line | 13 % → 13 % | 37.4 px | 0.23 | 1.00 | 106 |
| pressure swell | 10 % → 10 % | 37.1 px | 0.25 | 1.00 | 90 |
| fast wave | 28 % → 28 % | 31.9 px | 0.23 | 1.00 | 336 |
| slow wave | 30 % → 30 % | 34.3 px | 0.23 | 1.00 | 804 |
| spiral | 46 % → 46 % | 30.3 px | 0.22 | 1.00 | 675 |
| loop | 25 % → 25 % | 32.2 px | 0.24 | 1.00 | 262 |
| tilted | 12 % → 12 % | 33.4 px | 0.24 | 1.00 | 149 |
| over the wet one | 24 % → 24 % | 32.6 px | 0.24 | 1.00 | 128 |
| long, no reload | 51 % → 51 % | 22.7 px | 0.22 | 1.00 | 756 | quarters: 0.17 → 0.13 → 0.10 → 0.08

Numbers say: light vs heavy: width 34.5 → 37.4 px, dark 0.23 → 0.23; pressure barely changes the width.

## Oil — glaze
Oil · 40 px · 17.7 s

![Oil — glaze](Oil-glaze.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 9 % → 9 % | 27.0 px | 0.50 | 1.00 | 143 |
| heavy line | 13 % → 13 % | 38.2 px | 0.49 | 1.00 | 111 |
| pressure swell | 10 % → 10 % | 36.6 px | 0.50 | 1.00 | 86 |
| fast wave | 29 % → 29 % | 33.5 px | 0.49 | 1.00 | 348 |
| slow wave | 30 % → 30 % | 34.5 px | 0.50 | 1.00 | 718 |
| spiral | 46 % → 46 % | 30.0 px | 0.49 | 1.00 | 774 |
| loop | 24 % → 24 % | 31.4 px | 0.50 | 1.00 | 251 |
| tilted | 11 % → 11 % | 30.3 px | 0.50 | 1.00 | 140 |
| over the wet one | 22 % → 22 % | 32.5 px | 0.50 | 1.00 | 121 |
| long, no reload | 52 % → 52 % | 23.5 px | 0.49 | 1.00 | 745 | quarters: 0.34 → 0.30 → 0.27 → 0.22

Numbers say: light vs heavy: width 27.0 → 38.2 px, dark 0.50 → 0.49.

## Oil — scumble
Oil · 36 px · 19.2 s

![Oil — scumble](Oil-scumble.png)

A light paint: laid on a grey sheet (on white it cannot be seen); **dark** = how far it is from the grey either way.

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 10 % → 10 % | 27.7 px | 0.28 | 1.00 | 150 |
| heavy line | 9 % → 9 % | 27.2 px | 0.27 | 1.00 | 142 |
| pressure swell | 9 % → 9 % | 32.2 px | 0.26 | 1.00 | 105 |
| fast wave | 18 % → 18 % | 21.0 px | 0.22 | 1.00 | 341 |
| slow wave | 22 % → 22 % | 25.5 px | 0.21 | 1.00 | 564 |
| spiral | 32 % → 32 % | 20.9 px | 0.17 | 1.00 | 739 |
| loop | 18 % → 18 % | 23.1 px | 0.23 | 1.00 | 294 |
| tilted | 10 % → 10 % | 27.2 px | 0.25 | 1.00 | 158 |
| over the wet one | 20 % → 20 % | 27.5 px | 0.25 | 1.00 | 169 |
| long, no reload | 35 % → 35 % | 15.5 px | 0.15 | 1.00 | 827 | quarters: 0.00 → 0.00 → 0.00 → 0.00

Numbers say: light vs heavy: width 27.7 → 27.2 px, dark 0.28 → 0.27; pressure barely changes the width.

## Acrylic — heavy body
Heavy acrylic · 30 px · 15.2 s

![Acrylic — heavy body](Acrylic-heavy-body.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 10 % → 9 % | 30.0 px | 0.51 | 0.92 | 121 |
| heavy line | 11 % → 10 % | 32.1 px | 0.51 | 0.93 | 99 |
| pressure swell | 9 % → 8 % | 31.9 px | 0.53 | 0.94 | 74 |
| fast wave | 23 % → 15 % | 27.1 px | 0.51 | 0.62 | 247 |
| slow wave | 24 % → 16 % | 28.1 px | 0.51 | 0.65 | 523 |
| spiral | 36 % → 15 % | 23.5 px | 0.51 | 0.42 | 432 |
| loop | 21 % → 16 % | 27.1 px | 0.51 | 0.76 | 222 |
| tilted | 9 % → 9 % | 26.2 px | 0.51 | 1.00 | 119 |
| over the wet one | 20 % → 18 % | 28.4 px | 0.51 | 0.90 | 96 |
| long, no reload | 39 % → 15 % | 17.4 px | 0.51 | 0.40 | 634 | quarters: 0.30 → 0.19 → 0.11 → 0.04

Numbers say: light vs heavy: width 30.0 → 32.1 px, dark 0.51 → 0.51; pressure barely changes the width.

## Acrylic — fluid
Watercolor · 36 px · 32.5 s

![Acrylic — fluid](Acrylic-fluid.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 12 % → 12 % | 34.8 px | 0.24 | 1.01 | 73 |
| heavy line | 18 % → 18 % | 52.6 px | 0.21 | 0.99 | 79 |
| pressure swell | 12 % → 12 % | 45.4 px | 0.23 | 1.00 | 63 |
| fast wave | 38 % → 38 % | 44.1 px | 0.19 | 0.98 | 194 |
| slow wave | 35 % → 35 % | 40.5 px | 0.22 | 1.00 | 364 |
| spiral | 55 % → 53 % | 36.0 px | 0.19 | 0.98 | 425 |
| loop | 31 % → 31 % | 40.2 px | 0.21 | 1.00 | 178 |
| tilted | 12 % → 12 % | 34.2 px | 0.24 | 1.00 | 128 |
| over the wet one | 27 % → 28 % | 42.3 px | 0.24 | 1.01 | 121 |
| long, no reload | 61 % → 58 % | 27.6 px | 0.19 | 0.95 | 513 | quarters: 0.20 → 0.14 → 0.09 → 0.06

Numbers say: light vs heavy: width 34.8 → 52.6 px, dark 0.24 → 0.21.

## Acrylic — palette knife
Heavy acrylic · 42 px · 17.6 s

![Acrylic — palette knife](Acrylic-palette-knife.png)

A light paint: laid on a grey sheet (on white it cannot be seen); **dark** = how far it is from the grey either way.

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 16 % → 15 % | 45.6 px | 0.39 | 0.98 | 41 |
| heavy line | 16 % → 15 % | 45.8 px | 0.40 | 0.98 | 40 |
| pressure swell | 12 % → 12 % | 45.6 px | 0.42 | 0.99 | 14 |
| fast wave | 37 % → 20 % | 42.6 px | 0.37 | 0.55 | 92 |
| slow wave | 37 % → 21 % | 43.2 px | 0.37 | 0.57 | 128 |
| spiral | 50 % → 18 % | 32.8 px | 0.37 | 0.37 | 121 |
| loop | 32 % → 24 % | 41.2 px | 0.36 | 0.75 | 65 |
| tilted | 13 % → 13 % | 35.1 px | 0.39 | 1.00 | 26 |
| over the wet one | 27 % → 27 % | 41.3 px | 0.39 | 0.97 | 45 |
| long, no reload | 57 % → 21 % | 25.6 px | 0.35 | 0.36 | 167 | quarters: 0.00 → 0.00 → 0.00 → 0.01

Numbers say: light vs heavy: width 45.6 → 45.8 px, dark 0.39 → 0.40; pressure barely changes the width; the long stroke does not run out of paint.

## Finger on oil
Oil · 30 px · 13.5 s

![Finger on oil](Finger-on-oil.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 6 % → 6 % | 16.8 px | 0.40 | 1.00 | 46 |
| heavy line | 7 % → 7 % | 21.5 px | 0.39 | 1.00 | 56 |
| pressure swell | 6 % → 6 % | 22.3 px | 0.40 | 1.00 | 42 |
| fast wave | 12 % → 12 % | 13.6 px | 0.37 | 1.00 | 128 |
| slow wave | 17 % → 17 % | 19.5 px | 0.36 | 1.00 | 226 |
| spiral | 22 % → 22 % | 14.3 px | 0.34 | 1.00 | 231 |
| loop | 13 % → 13 % | 16.6 px | 0.37 | 1.00 | 149 |
| tilted | 8 % → 8 % | 21.4 px | 0.39 | 1.00 | 104 |
| over the wet one | 15 % → 15 % | 20.3 px | 0.39 | 1.00 | 72 |
| long, no reload | 22 % → 22 % | 10.0 px | 0.33 | 1.00 | 326 | quarters: 0.14 → 0.08 → 0.06 → 0.04

Numbers say: light vs heavy: width 16.8 → 21.5 px, dark 0.40 → 0.39.

## Palette knife — oil
Oil · 44 px · 17.4 s

![Palette knife — oil](Palette-knife-oil.png)

A light paint: laid on a grey sheet (on white it cannot be seen); **dark** = how far it is from the grey either way.

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 16 % → 16 % | 47.4 px | 0.36 | 1.00 | 62 |
| heavy line | 17 % → 17 % | 48.1 px | 0.39 | 1.00 | 43 |
| pressure swell | 13 % → 13 % | 47.5 px | 0.39 | 1.00 | 20 |
| fast wave | 39 % → 40 % | 45.6 px | 0.35 | 1.01 | 97 |
| slow wave | 40 % → 40 % | 46.1 px | 0.35 | 1.00 | 128 |
| spiral | 63 % → 63 % | 41.3 px | 0.27 | 1.00 | 134 |
| loop | 34 % → 34 % | 43.8 px | 0.36 | 1.00 | 65 |
| tilted | 14 % → 14 % | 38.3 px | 0.38 | 1.00 | 27 |
| over the wet one | 29 % → 29 % | 42.5 px | 0.38 | 1.00 | 34 |
| long, no reload | 75 % → 75 % | 33.4 px | 0.25 | 1.00 | 173 | quarters: 0.00 → 0.00 → 0.00 → 0.00

Numbers say: light vs heavy: width 47.4 → 48.1 px, dark 0.36 → 0.39; pressure barely changes the width; the long stroke does not run out of paint.

## 0.45 · Sponge
Watercolor · 46 px · 32.0 s

![0.45 · Sponge](0-45-Sponge.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 27 % → 18 % | 78.2 px | 0.09 | 0.67 | 74 |
| heavy line | 32 % → 25 % | 91.7 px | 0.09 | 0.78 | 94 |
| pressure swell | 24 % → 17 % | 90.3 px | 0.11 | 0.71 | 45 |
| fast wave | 59 % → 43 % | 68.1 px | 0.10 | 0.73 | 150 |
| slow wave | 59 % → 48 % | 68.5 px | 0.13 | 0.80 | 262 |
| spiral | 75 % → 57 % | 49.3 px | 0.12 | 0.76 | 263 |
| loop | 53 % → 43 % | 68.6 px | 0.11 | 0.81 | 153 |
| tilted | 18 % → 18 % | 49.4 px | 0.15 | 1.00 | 109 |
| over the wet one | 44 % → 37 % | 74.4 px | 0.15 | 0.84 | 69 |
| long, no reload | 89 % → 71 % | 39.9 px | 0.13 | 0.79 | 392 | quarters: 0.13 → 0.12 → 0.10 → 0.07

Numbers say: light vs heavy: width 78.2 → 91.7 px, dark 0.09 → 0.09.

## 0.45 · Eraser
Eraser · 30 px · 18.9 s · over bands of wet oil paint and oil pastel in turn (it works on paint already there: look at what it does to the bands; covered counts the bands too)

![0.45 · Eraser](0-45-Eraser.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 24 % → 24 % | 69.2 px | 0.82 | 1.00 | 41 |
| heavy line | 23 % → 23 % | 67.4 px | 0.81 | 1.00 | 50 |
| pressure swell | 23 % → 23 % | 86.7 px | 0.82 | 1.00 | 38 |
| fast wave | 21 % → 21 % | 24.7 px | 0.81 | 1.00 | 143 |
| slow wave | 20 % → 20 % | 23.5 px | 0.82 | 1.00 | 239 |
| spiral | 20 % → 20 % | 13.5 px | 0.79 | 1.00 | 222 |
| loop | 21 % → 21 % | 27.8 px | 0.80 | 1.00 | 112 |
| tilted | 23 % → 23 % | 64.8 px | 0.81 | 1.00 | 58 |
| over the wet one | 22 % → 22 % | 0.0 px | 0.81 | 1.00 | 52 |
| long, no reload | 17 % → 17 % | 7.5 px | 0.79 | 1.00 | 307 | quarters: 0.13 → 0.16 → 0.13 → 0.17

Numbers say: light vs heavy: width 69.2 → 67.4 px, dark 0.82 → 0.81; pressure barely changes the width; the long stroke does not run out of paint.

## Lift wet paint
Eraser · 30 px · 19.9 s · over bands of wet oil paint and oil pastel in turn (it works on paint already there: look at what it does to the bands; covered counts the bands too)

![Lift wet paint](Lift-wet-paint.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 24 % → 24 % | 70.1 px | 0.82 | 1.00 | 33 |
| heavy line | 24 % → 24 % | 69.8 px | 0.82 | 1.00 | 42 |
| pressure swell | 24 % → 24 % | 89.5 px | 0.82 | 1.00 | 31 |
| fast wave | 24 % → 24 % | 27.7 px | 0.82 | 1.00 | 102 |
| slow wave | 24 % → 24 % | 27.7 px | 0.82 | 1.00 | 166 |
| spiral | 24 % → 24 % | 15.9 px | 0.82 | 1.00 | 160 |
| loop | 24 % → 24 % | 31.1 px | 0.82 | 1.00 | 91 |
| tilted | 24 % → 24 % | 66.8 px | 0.82 | 1.00 | 54 |
| over the wet one | 24 % → 24 % | 0.0 px | 0.82 | 1.00 | 54 |
| long, no reload | 24 % → 24 % | 10.7 px | 0.82 | 1.00 | 345 | quarters: 0.18 → 0.24 → 0.17 → 0.24

Numbers say: light vs heavy: width 70.1 → 69.8 px, dark 0.82 → 0.82; pressure barely changes the width; the long stroke does not run out of paint.

## Sgraffito
Eraser · 10 px · 18.9 s · over bands of wet oil paint and oil pastel in turn (it works on paint already there: look at what it does to the bands; covered counts the bands too)

![Sgraffito](Sgraffito.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 24 % → 24 % | 69.5 px | 0.81 | 1.00 | 8 |
| heavy line | 24 % → 24 % | 69.5 px | 0.82 | 1.00 | 10 |
| pressure swell | 24 % → 24 % | 89.5 px | 0.82 | 1.00 | 7 |
| fast wave | 24 % → 24 % | 27.4 px | 0.82 | 1.00 | 19 |
| slow wave | 24 % → 24 % | 27.4 px | 0.81 | 1.00 | 19 |
| spiral | 24 % → 24 % | 15.7 px | 0.81 | 1.00 | 33 |
| loop | 24 % → 24 % | 30.9 px | 0.82 | 1.00 | 18 |
| tilted | 24 % → 24 % | 66.6 px | 0.82 | 1.00 | 7 |
| over the wet one | 24 % → 24 % | 0.0 px | 0.82 | 1.00 | 7 |
| long, no reload | 24 % → 24 % | 10.6 px | 0.82 | 1.00 | 46 | quarters: 0.17 → 0.24 → 0.17 → 0.24

Numbers say: light vs heavy: width 69.5 → 69.5 px, dark 0.81 → 0.82; pressure barely changes the width; the long stroke does not run out of paint.

## Brush Artist · Refs · #01 Henry Ward peach cloud
Gouache · 44 px · 34.7 s

![Brush Artist · Refs · #01 Henry Ward peach cloud](Brush-Artist-Refs-01-Henry-Ward-peach-cloud.png)

A light paint: laid on a grey sheet (on white it cannot be seen); **dark** = how far it is from the grey either way.

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 13 % → 9 % | 37.9 px | 0.33 | 0.68 | 145 |
| heavy line | 14 % → 10 % | 41.1 px | 0.33 | 0.74 | 148 |
| pressure swell | 11 % → 9 % | 41.0 px | 0.33 | 0.80 | 108 |
| fast wave | 25 % → 13 % | 29.2 px | 0.33 | 0.51 | 467 |
| slow wave | 30 % → 15 % | 34.6 px | 0.33 | 0.50 | 653 |
| spiral | 41 % → 16 % | 27.0 px | 0.33 | 0.39 | 619 |
| loop | 25 % → 16 % | 33.0 px | 0.33 | 0.61 | 335 |
| tilted | 11 % → 11 % | 31.3 px | 0.33 | 1.00 | 176 |
| over the wet one | 24 % → 20 % | 36.1 px | 0.33 | 0.85 | 148 |
| long, no reload | 44 % → 18 % | 19.8 px | 0.33 | 0.41 | 849 | quarters: 0.01 → 0.02 → 0.02 → 0.02

Numbers say: light vs heavy: width 37.9 → 41.1 px, dark 0.33 → 0.33; pressure barely changes the width; the long stroke does not run out of paint.

## Brush Artist · Refs · #02 Henry Ward cream strokes
Gouache · 46 px · 38.5 s

![Brush Artist · Refs · #02 Henry Ward cream strokes](Brush-Artist-Refs-02-Henry-Ward-cream-strokes.png)

A light paint: laid on a grey sheet (on white it cannot be seen); **dark** = how far it is from the grey either way.

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 13 % → 10 % | 37.9 px | 0.41 | 0.73 | 218 |
| heavy line | 14 % → 12 % | 40.9 px | 0.41 | 0.82 | 158 |
| pressure swell | 11 % → 10 % | 41.1 px | 0.42 | 0.88 | 115 |
| fast wave | 25 % → 13 % | 28.7 px | 0.41 | 0.51 | 391 |
| slow wave | 29 % → 15 % | 34.0 px | 0.41 | 0.51 | 672 |
| spiral | 40 % → 16 % | 26.6 px | 0.41 | 0.40 | 659 |
| loop | 25 % → 16 % | 32.6 px | 0.41 | 0.64 | 333 |
| tilted | 11 % → 11 % | 30.7 px | 0.41 | 1.00 | 183 |
| over the wet one | 24 % → 21 % | 36.1 px | 0.41 | 0.86 | 154 |
| long, no reload | 44 % → 19 % | 19.6 px | 0.41 | 0.43 | 1254 | quarters: 0.01 → 0.02 → 0.03 → 0.03

Numbers say: light vs heavy: width 37.9 → 40.9 px, dark 0.41 → 0.41; pressure barely changes the width; the long stroke does not run out of paint.

## Brush Artist · Refs · #03 Henry Ward navy contours
Heavy acrylic · 22 px · 17.7 s

![Brush Artist · Refs · #03 Henry Ward navy contours](Brush-Artist-Refs-03-Henry-Ward-navy-contours.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 8 % → 7 % | 22.1 px | 0.70 | 0.94 | 73 |
| heavy line | 8 % → 8 % | 24.0 px | 0.70 | 0.95 | 73 |
| pressure swell | 6 % → 6 % | 23.8 px | 0.73 | 0.94 | 56 |
| fast wave | 19 % → 12 % | 22.0 px | 0.72 | 0.65 | 186 |
| slow wave | 20 % → 13 % | 22.6 px | 0.72 | 0.68 | 292 |
| spiral | 30 % → 13 % | 19.6 px | 0.72 | 0.45 | 311 |
| loop | 17 % → 13 % | 21.5 px | 0.72 | 0.81 | 162 |
| tilted | 8 % → 8 % | 23.2 px | 0.72 | 1.00 | 91 |
| over the wet one | 16 % → 14 % | 21.8 px | 0.72 | 0.90 | 79 |
| long, no reload | 34 % → 13 % | 15.1 px | 0.72 | 0.40 | 456 | quarters: 0.35 → 0.29 → 0.19 → 0.08

Numbers say: light vs heavy: width 22.1 → 24.0 px, dark 0.70 → 0.70; pressure barely changes the width.

## Brush Artist · Refs · #04 Henry Ward grey cloud
Gouache · 50 px · 42.9 s

![Brush Artist · Refs · #04 Henry Ward grey cloud](Brush-Artist-Refs-04-Henry-Ward-grey-cloud.png)

A light paint: laid on a grey sheet (on white it cannot be seen); **dark** = how far it is from the grey either way.

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 15 % → 11 % | 43.6 px | 0.32 | 0.73 | 166 |
| heavy line | 16 % → 13 % | 46.9 px | 0.32 | 0.79 | 194 |
| pressure swell | 12 % → 10 % | 46.8 px | 0.32 | 0.84 | 162 |
| fast wave | 29 % → 15 % | 32.9 px | 0.32 | 0.52 | 471 |
| slow wave | 34 % → 17 % | 39.2 px | 0.32 | 0.51 | 887 |
| spiral | 44 % → 18 % | 28.7 px | 0.32 | 0.42 | 961 |
| loop | 29 % → 18 % | 37.7 px | 0.32 | 0.62 | 710 |
| tilted | 12 % → 12 % | 34.2 px | 0.32 | 1.00 | 391 |
| over the wet one | 27 % → 23 % | 41.1 px | 0.32 | 0.86 | 831 |
| long, no reload | 49 % → 21 % | 21.8 px | 0.32 | 0.44 | 1414 | quarters: 0.01 → 0.02 → 0.02 → 0.03

Numbers say: light vs heavy: width 43.6 → 46.9 px, dark 0.32 → 0.32; pressure barely changes the width; the long stroke does not run out of paint.

## Brush Artist · Refs · #05 Henry Ward green in rust loops
Heavy acrylic · 20 px · 22.9 s

![Brush Artist · Refs · #05 Henry Ward green in rust loops](Brush-Artist-Refs-05-Henry-Ward-green-in-rust-loops.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 7 % → 6 % | 19.9 px | 0.55 | 0.94 | 140 |
| heavy line | 7 % → 7 % | 21.7 px | 0.55 | 0.94 | 186 |
| pressure swell | 6 % → 5 % | 22.0 px | 0.57 | 0.92 | 130 |
| fast wave | 17 % → 11 % | 19.9 px | 0.56 | 0.64 | 356 |
| slow wave | 18 % → 12 % | 20.5 px | 0.55 | 0.66 | 1218 |
| spiral | 27 % → 11 % | 17.9 px | 0.55 | 0.42 | 491 |
| loop | 15 % → 12 % | 19.5 px | 0.55 | 0.79 | 227 |
| tilted | 8 % → 8 % | 22.1 px | 0.56 | 1.00 | 137 |
| over the wet one | 15 % → 13 % | 19.7 px | 0.56 | 0.87 | 107 |
| long, no reload | 30 % → 12 % | 13.4 px | 0.56 | 0.39 | 671 | quarters: 0.25 → 0.18 → 0.10 → 0.02

Numbers say: light vs heavy: width 19.9 → 21.7 px, dark 0.55 → 0.55; pressure barely changes the width.

## Brush Artist · Refs · #06 Henry Ward scrubbed grey
Gouache · 50 px · 37.3 s

![Brush Artist · Refs · #06 Henry Ward scrubbed grey](Brush-Artist-Refs-06-Henry-Ward-scrubbed-grey.png)

A light paint: laid on a grey sheet (on white it cannot be seen); **dark** = how far it is from the grey either way.

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 15 % → 11 % | 43.6 px | 0.34 | 0.73 | 199 |
| heavy line | 16 % → 13 % | 46.9 px | 0.34 | 0.79 | 251 |
| pressure swell | 12 % → 10 % | 46.8 px | 0.34 | 0.84 | 180 |
| fast wave | 29 % → 15 % | 32.9 px | 0.34 | 0.52 | 547 |
| slow wave | 34 % → 17 % | 39.2 px | 0.34 | 0.51 | 1072 |
| spiral | 44 % → 18 % | 28.7 px | 0.34 | 0.42 | 1022 |
| loop | 29 % → 18 % | 37.7 px | 0.34 | 0.62 | 393 |
| tilted | 12 % → 12 % | 34.2 px | 0.34 | 1.00 | 203 |
| over the wet one | 27 % → 23 % | 41.1 px | 0.34 | 0.86 | 168 |
| long, no reload | 49 % → 21 % | 21.8 px | 0.34 | 0.44 | 1028 | quarters: 0.01 → 0.02 → 0.02 → 0.03

Numbers say: light vs heavy: width 43.6 → 46.9 px, dark 0.34 → 0.34; pressure barely changes the width; the long stroke does not run out of paint.

## Brush Artist · Refs · #07 Henry Ward blue L + black zigzag
Heavy acrylic · 34 px · 15.6 s

![Brush Artist · Refs · #07 Henry Ward blue L + black zigzag](Brush-Artist-Refs-07-Henry-Ward-blue-L-black-zigzag.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 12 % → 11 % | 34.2 px | 0.58 | 0.93 | 97 |
| heavy line | 13 % → 12 % | 36.9 px | 0.58 | 0.93 | 101 |
| pressure swell | 10 % → 9 % | 36.6 px | 0.59 | 0.94 | 73 |
| fast wave | 30 % → 20 % | 34.1 px | 0.58 | 0.69 | 251 |
| slow wave | 30 % → 22 % | 34.6 px | 0.58 | 0.73 | 442 |
| spiral | 48 % → 22 % | 31.5 px | 0.58 | 0.46 | 439 |
| loop | 25 % → 21 % | 32.7 px | 0.58 | 0.82 | 223 |
| tilted | 11 % → 11 % | 31.0 px | 0.58 | 1.00 | 150 |
| over the wet one | 23 % → 21 % | 32.8 px | 0.58 | 0.91 | 133 |
| long, no reload | 53 % → 22 % | 23.9 px | 0.58 | 0.41 | 888 | quarters: 0.40 → 0.32 → 0.21 → 0.10

Numbers say: light vs heavy: width 34.2 → 36.9 px, dark 0.58 → 0.58; pressure barely changes the width.

## Brush Artist · Refs · #08 Henry Ward olive bands
Gouache · 34 px · 24.5 s

![Brush Artist · Refs · #08 Henry Ward olive bands](Brush-Artist-Refs-08-Henry-Ward-olive-bands.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 4 % → 0 % | 12.2 px | 0.61 | 0.04 | 64 |
| heavy line | 7 % → 0 % | 19.3 px | 0.61 | 0.02 | 135 |
| pressure swell | 5 % → 0 % | 18.7 px | 0.61 | 0.03 | 80 |
| fast wave | 10 % → 0 % | 11.1 px | 0.61 | 0.02 | 241 |
| slow wave | 15 % → 1 % | 17.0 px | 0.61 | 0.06 | 433 |
| spiral | 19 % → 1 % | 12.7 px | 0.61 | 0.03 | 410 |
| loop | 12 % → 1 % | 15.3 px | 0.61 | 0.09 | 216 |
| tilted | 5 % → 5 % | 15.1 px | 0.61 | 0.96 | 114 |
| over the wet one | 11 % → 2 % | 16.9 px | 0.61 | 0.22 | 128 |
| long, no reload | 22 % → 2 % | 9.8 px | 0.61 | 0.09 | 753 | quarters: 0.21 → 0.15 → 0.11 → 0.09

Numbers say: light vs heavy: width 12.2 → 19.3 px, dark 0.61 → 0.61.

## Brush Artist · Refs · #09 Henry Ward white loops
Gouache · 46 px · 40.0 s

![Brush Artist · Refs · #09 Henry Ward white loops](Brush-Artist-Refs-09-Henry-Ward-white-loops.png)

A light paint: laid on a grey sheet (on white it cannot be seen); **dark** = how far it is from the grey either way.

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 13 % → 10 % | 37.9 px | 0.44 | 0.73 | 147 |
| heavy line | 14 % → 12 % | 40.9 px | 0.44 | 0.82 | 152 |
| pressure swell | 11 % → 10 % | 41.1 px | 0.44 | 0.88 | 152 |
| fast wave | 25 % → 13 % | 28.7 px | 0.43 | 0.51 | 519 |
| slow wave | 29 % → 15 % | 34.0 px | 0.43 | 0.51 | 669 |
| spiral | 40 % → 16 % | 26.6 px | 0.43 | 0.40 | 631 |
| loop | 25 % → 16 % | 32.6 px | 0.43 | 0.64 | 455 |
| tilted | 11 % → 11 % | 30.7 px | 0.44 | 1.00 | 246 |
| over the wet one | 24 % → 21 % | 36.1 px | 0.44 | 0.86 | 241 |
| long, no reload | 44 % → 19 % | 19.6 px | 0.43 | 0.43 | 1057 | quarters: 0.01 → 0.02 → 0.03 → 0.03

Numbers say: light vs heavy: width 37.9 → 40.9 px, dark 0.44 → 0.44; pressure barely changes the width; the long stroke does not run out of paint.

## Brush Artist · Refs · #10 Henry Ward maroon loops
Heavy acrylic · 30 px · 18.4 s

![Brush Artist · Refs · #10 Henry Ward maroon loops](Brush-Artist-Refs-10-Henry-Ward-maroon-loops.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 10 % → 9 % | 28.8 px | 0.71 | 0.95 | 88 |
| heavy line | 11 % → 10 % | 31.2 px | 0.71 | 0.95 | 88 |
| pressure swell | 8 % → 8 % | 31.1 px | 0.73 | 0.95 | 63 |
| fast wave | 25 % → 18 % | 28.7 px | 0.72 | 0.71 | 265 |
| slow wave | 25 % → 19 % | 29.4 px | 0.72 | 0.73 | 585 |
| spiral | 40 % → 19 % | 26.2 px | 0.72 | 0.47 | 549 |
| loop | 21 % → 18 % | 27.6 px | 0.72 | 0.85 | 318 |
| tilted | 10 % → 10 % | 28.7 px | 0.72 | 1.00 | 129 |
| over the wet one | 20 % → 18 % | 27.7 px | 0.72 | 0.91 | 109 |
| long, no reload | 46 % → 18 % | 20.7 px | 0.72 | 0.40 | 616 | quarters: 0.44 → 0.38 → 0.30 → 0.22

Numbers say: light vs heavy: width 28.8 → 31.2 px, dark 0.71 → 0.71; pressure barely changes the width.

## Brush Artist · Refs · #11 Henry Ward purple spun balls
Heavy acrylic · 36 px · 19.6 s

![Brush Artist · Refs · #11 Henry Ward purple spun balls](Brush-Artist-Refs-11-Henry-Ward-purple-spun-balls.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 12 % → 12 % | 35.3 px | 0.71 | 0.96 | 126 |
| heavy line | 13 % → 12 % | 37.9 px | 0.71 | 0.96 | 119 |
| pressure swell | 10 % → 10 % | 37.7 px | 0.74 | 0.96 | 108 |
| fast wave | 30 % → 23 % | 35.1 px | 0.73 | 0.75 | 352 |
| slow wave | 31 % → 24 % | 35.5 px | 0.73 | 0.79 | 526 |
| spiral | 49 % → 25 % | 32.6 px | 0.73 | 0.50 | 564 |
| loop | 26 % → 23 % | 33.4 px | 0.73 | 0.88 | 397 |
| tilted | 12 % → 12 % | 32.4 px | 0.73 | 1.00 | 205 |
| over the wet one | 24 % → 22 % | 33.5 px | 0.73 | 0.93 | 145 |
| long, no reload | 56 % → 24 % | 24.9 px | 0.73 | 0.44 | 1439 | quarters: 0.51 → 0.46 → 0.39 → 0.29

Numbers say: light vs heavy: width 35.3 → 37.9 px, dark 0.71 → 0.71; pressure barely changes the width.

## Brush Artist · Refs · #12 Henry Ward black-olive cage
Gouache · 28 px · 23.7 s

![Brush Artist · Refs · #12 Henry Ward black-olive cage](Brush-Artist-Refs-12-Henry-Ward-black-olive-cage.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 3 % → 0 % | 10.1 px | 0.65 | 0.08 | 86 |
| heavy line | 5 % → 0 % | 15.3 px | 0.65 | 0.08 | 220 |
| pressure swell | 4 % → 0 % | 14.9 px | 0.65 | 0.10 | 88 |
| fast wave | 8 % → 0 % | 8.9 px | 0.65 | 0.04 | 281 |
| slow wave | 12 % → 1 % | 13.6 px | 0.65 | 0.09 | 357 |
| spiral | 16 % → 1 % | 10.4 px | 0.65 | 0.04 | 347 |
| loop | 9 % → 2 % | 12.3 px | 0.65 | 0.17 | 208 |
| tilted | 5 % → 4 % | 13.0 px | 0.65 | 0.95 | 116 |
| over the wet one | 9 % → 3 % | 13.2 px | 0.65 | 0.27 | 87 |
| long, no reload | 18 % → 2 % | 8.3 px | 0.65 | 0.12 | 737 | quarters: 0.19 → 0.14 → 0.11 → 0.10

Numbers say: light vs heavy: width 10.1 → 15.3 px, dark 0.65 → 0.65.

## Brush Artist · Refs · #13 Henry Ward blue streaky form
Gouache · 50 px · 34.8 s

![Brush Artist · Refs · #13 Henry Ward blue streaky form](Brush-Artist-Refs-13-Henry-Ward-blue-streaky-form.png)

A light paint: laid on a grey sheet (on white it cannot be seen); **dark** = how far it is from the grey either way.

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 15 % → 11 % | 43.6 px | 0.34 | 0.73 | 271 |
| heavy line | 16 % → 13 % | 46.9 px | 0.34 | 0.79 | 170 |
| pressure swell | 12 % → 10 % | 46.8 px | 0.34 | 0.84 | 119 |
| fast wave | 29 % → 15 % | 32.9 px | 0.34 | 0.52 | 412 |
| slow wave | 34 % → 17 % | 39.2 px | 0.34 | 0.51 | 781 |
| spiral | 44 % → 18 % | 28.7 px | 0.34 | 0.42 | 712 |
| loop | 29 % → 18 % | 37.7 px | 0.34 | 0.62 | 369 |
| tilted | 12 % → 12 % | 34.2 px | 0.34 | 1.00 | 249 |
| over the wet one | 27 % → 23 % | 41.1 px | 0.34 | 0.86 | 178 |
| long, no reload | 49 % → 21 % | 21.8 px | 0.33 | 0.44 | 1390 | quarters: 0.01 → 0.02 → 0.02 → 0.03

Numbers say: light vs heavy: width 43.6 → 46.9 px, dark 0.34 → 0.34; pressure barely changes the width; the long stroke does not run out of paint.

## Brush Artist · Refs · #14 Henry Ward olive totem
Heavy acrylic · 48 px · 18.1 s

![Brush Artist · Refs · #14 Henry Ward olive totem](Brush-Artist-Refs-14-Henry-Ward-olive-totem.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 16 % → 15 % | 46.8 px | 0.31 | 0.95 | 191 |
| heavy line | 17 % → 16 % | 49.8 px | 0.31 | 0.95 | 142 |
| pressure swell | 13 % → 13 % | 49.6 px | 0.32 | 0.96 | 104 |
| fast wave | 39 % → 31 % | 44.9 px | 0.30 | 0.79 | 369 |
| slow wave | 39 % → 32 % | 45.4 px | 0.30 | 0.81 | 625 |
| spiral | 59 % → 32 % | 38.7 px | 0.30 | 0.55 | 670 |
| loop | 33 % → 29 % | 42.7 px | 0.30 | 0.89 | 347 |
| tilted | 14 % → 14 % | 39.5 px | 0.31 | 1.00 | 180 |
| over the wet one | 30 % → 28 % | 43.3 px | 0.31 | 0.94 | 143 |
| long, no reload | 68 % → 33 % | 30.6 px | 0.30 | 0.48 | 905 | quarters: 0.25 → 0.18 → 0.09 → 0.04

Numbers say: light vs heavy: width 46.8 → 49.8 px, dark 0.31 → 0.31; pressure barely changes the width.

## Brush Artist · Refs · #15 Ultramarine brush script
Ink · 4 px · 20.5 s

![Brush Artist · Refs · #15 Ultramarine brush script](Brush-Artist-Refs-15-Ultramarine-brush-script.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 1 % → 3 % | 2.2 px | 0.55 | 3.90 | 26 |
| heavy line | 6 % → 6 % | 16.7 px | 0.58 | 0.99 | 48 |
| pressure swell | 3 % → 4 % | 12.1 px | 0.64 | 1.15 | 31 |
| fast wave | 9 % → 7 % | 10.6 px | 0.54 | 0.81 | 127 |
| slow wave | 7 % → 7 % | 8.4 px | 0.54 | 0.93 | 119 |
| spiral | 11 % → 7 % | 7.2 px | 0.52 | 0.66 | 180 |
| loop | 7 % → 7 % | 9.2 px | 0.53 | 0.98 | 80 |
| tilted | 3 % → 3 % | 8.2 px | 0.62 | 1.02 | 44 |
| over the wet one | 7 % → 7 % | 11.5 px | 0.62 | 1.05 | 37 |
| long, no reload | 16 % → 8 % | 7.3 px | 0.50 | 0.48 | 228 | quarters: 0.15 → 0.04 → 0.01 → 0.00

Numbers say: light vs heavy: width 2.2 → 16.7 px, dark 0.55 → 0.58; wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #18 Blue oil-stick scribbles
Pastel · 10 px · 10.0 s

![Brush Artist · Refs · #18 Blue oil-stick scribbles](Brush-Artist-Refs-18-Blue-oil-stick-scribbles.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 1 % → 1 % | 2.9 px | 0.52 | 1.00 | 22 |
| heavy line | 2 % → 2 % | 5.5 px | 0.53 | 1.00 | 25 |
| pressure swell | 1 % → 1 % | 5.0 px | 0.53 | 1.00 | 17 |
| fast wave | 4 % → 4 % | 4.8 px | 0.53 | 1.00 | 62 |
| slow wave | 4 % → 4 % | 4.4 px | 0.53 | 1.00 | 58 |
| spiral | 7 % → 7 % | 4.5 px | 0.52 | 1.00 | 105 |
| loop | 3 % → 3 % | 4.5 px | 0.52 | 1.00 | 52 |
| tilted | 2 % → 2 % | 4.7 px | 0.53 | 1.00 | 30 |
| over the wet one | 3 % → 3 % | 4.7 px | 0.53 | 1.00 | 25 |
| long, no reload | 10 % → 10 % | 4.4 px | 0.53 | 1.00 | 159 | quarters: 0.06 → 0.06 → 0.06 → 0.06

Numbers say: light vs heavy: width 2.9 → 5.5 px, dark 0.52 → 0.53; the long stroke does not run out of paint.

## Brush Artist · Refs · #20 Orange-red crayon scribble
Pastel · 14 px · 10.0 s

![Brush Artist · Refs · #20 Orange-red crayon scribble](Brush-Artist-Refs-20-Orange-red-crayon-scribble.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 1 % → 1 % | 4.0 px | 0.53 | 1.00 | 24 |
| heavy line | 3 % → 3 % | 8.0 px | 0.53 | 1.00 | 25 |
| pressure swell | 2 % → 2 % | 7.6 px | 0.53 | 1.00 | 18 |
| fast wave | 6 % → 6 % | 7.2 px | 0.53 | 1.00 | 65 |
| slow wave | 6 % → 6 % | 6.6 px | 0.53 | 1.00 | 68 |
| spiral | 9 % → 9 % | 6.2 px | 0.53 | 1.00 | 110 |
| loop | 5 % → 5 % | 6.2 px | 0.53 | 1.00 | 55 |
| tilted | 2 % → 2 % | 5.6 px | 0.53 | 1.00 | 30 |
| over the wet one | 4 % → 4 % | 6.6 px | 0.53 | 1.00 | 28 |
| long, no reload | 13 % → 13 % | 5.7 px | 0.53 | 1.00 | 160 | quarters: 0.07 → 0.07 → 0.08 → 0.08

Numbers say: light vs heavy: width 4.0 → 8.0 px, dark 0.53 → 0.53; the long stroke does not run out of paint.

## Brush Artist · Refs · #21 Gritty black contours
Gouache · 12 px · 19.4 s

![Brush Artist · Refs · #21 Gritty black contours](Brush-Artist-Refs-21-Gritty-black-contours.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 1 % → 0 % | 3.3 px | 0.81 | 0.08 | 57 |
| heavy line | 2 % → 0 % | 5.2 px | 0.81 | 0.03 | 103 |
| pressure swell | 1 % → 0 % | 5.4 px | 0.81 | 0.04 | 61 |
| fast wave | 2 % → 0 % | 2.7 px | 0.81 | 0.01 | 188 |
| slow wave | 4 % → 0 % | 4.4 px | 0.81 | 0.04 | 195 |
| spiral | 5 % → 0 % | 3.1 px | 0.81 | 0.02 | 359 |
| loop | 3 % → 0 % | 4.1 px | 0.81 | 0.02 | 239 |
| tilted | 2 % → 2 % | 4.8 px | 0.81 | 0.93 | 98 |
| over the wet one | 3 % → 0 % | 4.7 px | 0.81 | 0.11 | 84 |
| long, no reload | 6 % → 0 % | 2.7 px | 0.81 | 0.06 | 490 | quarters: 0.09 → 0.06 → 0.05 → 0.04

Numbers say: light vs heavy: width 3.3 → 5.2 px, dark 0.81 → 0.81.

## Brush Artist · Refs · #22 Bold black brush poster
Ink · 20 px · 25.9 s

![Brush Artist · Refs · #22 Bold black brush poster](Brush-Artist-Refs-22-Bold-black-brush-poster.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 3 % → 5 % | 9.6 px | 0.79 | 1.64 | 45 |
| heavy line | 15 % → 15 % | 44.6 px | 0.88 | 0.99 | 123 |
| pressure swell | 9 % → 9 % | 31.9 px | 0.87 | 1.04 | 50 |
| fast wave | 27 % → 27 % | 31.7 px | 0.87 | 0.98 | 143 |
| slow wave | 22 % → 22 % | 25.4 px | 0.87 | 0.98 | 212 |
| spiral | 34 % → 32 % | 22.4 px | 0.87 | 0.94 | 257 |
| loop | 20 % → 20 % | 26.4 px | 0.88 | 1.00 | 129 |
| tilted | 8 % → 8 % | 23.1 px | 0.88 | 1.01 | 69 |
| over the wet one | 19 % → 19 % | 30.4 px | 0.88 | 1.00 | 66 |
| long, no reload | 45 % → 38 % | 20.3 px | 0.86 | 0.83 | 366 | quarters: 0.54 → 0.45 → 0.35 → 0.26

Numbers say: light vs heavy: width 9.6 → 44.6 px, dark 0.79 → 0.88; wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #23 Dry white on orange + black line
Gouache · 50 px · 22.3 s

![Brush Artist · Refs · #23 Dry white on orange + black line](Brush-Artist-Refs-23-Dry-white-on-orange-black-line.png)

A light paint: laid on a grey sheet (on white it cannot be seen); **dark** = how far it is from the grey either way.

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 5 % → 0 % | 15.7 px | 0.42 | 0.02 | 83 |
| heavy line | 9 % → 0 % | 25.3 px | 0.42 | 0.00 | 207 |
| pressure swell | 6 % → 0 % | 23.8 px | 0.41 | 0.00 | 115 |
| fast wave | 12 % → 0 % | 13.7 px | 0.41 | 0.01 | 350 |
| slow wave | 19 % → 0 % | 21.6 px | 0.41 | 0.02 | 621 |
| spiral | 24 % → 0 % | 15.6 px | 0.40 | 0.01 | 600 |
| loop | 15 % → 1 % | 19.8 px | 0.40 | 0.04 | 332 |
| tilted | 6 % → 6 % | 17.5 px | 0.40 | 0.94 | 177 |
| over the wet one | 14 % → 1 % | 20.6 px | 0.40 | 0.09 | 156 |
| long, no reload | 27 % → 1 % | 12.3 px | 0.40 | 0.05 | 1111 | quarters: 0.02 → 0.03 → 0.03 → 0.03

Numbers say: light vs heavy: width 15.7 → 25.3 px, dark 0.42 → 0.42; the long stroke does not run out of paint.

## Brush Artist · Refs · #24 Picasso flat oil
Oil · 34 px · 20.3 s

![Brush Artist · Refs · #24 Picasso flat oil](Brush-Artist-Refs-24-Picasso-flat-oil.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 11 % → 12 % | 33.4 px | 0.40 | 1.00 | 116 |
| heavy line | 12 % → 13 % | 36.2 px | 0.40 | 1.00 | 135 |
| pressure swell | 10 % → 10 % | 35.8 px | 0.41 | 1.00 | 91 |
| fast wave | 30 % → 30 % | 34.6 px | 0.41 | 1.00 | 320 |
| slow wave | 31 % → 31 % | 35.4 px | 0.40 | 1.00 | 559 |
| spiral | 52 % → 52 % | 34.0 px | 0.40 | 1.00 | 549 |
| loop | 25 % → 25 % | 32.7 px | 0.41 | 1.00 | 281 |
| tilted | 12 % → 12 % | 33.0 px | 0.40 | 1.00 | 171 |
| over the wet one | 23 % → 23 % | 31.9 px | 0.40 | 1.00 | 132 |
| long, no reload | 62 % → 62 % | 27.7 px | 0.39 | 1.00 | 834 | quarters: 0.28 → 0.27 → 0.26 → 0.24

Numbers say: light vs heavy: width 33.4 → 36.2 px, dark 0.40 → 0.40; pressure barely changes the width; the long stroke does not run out of paint.

## Brush Artist · Refs · #25 Yellow heavy flat stroke
Heavy acrylic · 110 px · 36.1 s

![Brush Artist · Refs · #25 Yellow heavy flat stroke](Brush-Artist-Refs-25-Yellow-heavy-flat-stroke.png)

A light paint: laid on a grey sheet (on white it cannot be seen); **dark** = how far it is from the grey either way.

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 38 % → 39 % | 109.9 px | 0.30 | 1.02 | 361 |
| heavy line | 39 % → 39 % | 114.6 px | 0.30 | 0.98 | 401 |
| pressure swell | 31 % → 32 % | 115.0 px | 0.30 | 1.05 | 282 |
| fast wave | 75 % → 78 % | 86.6 px | 0.30 | 1.04 | 1136 |
| slow wave | 76 % → 74 % | 87.5 px | 0.30 | 0.98 | 1797 |
| spiral | 87 % → 83 % | 57.1 px | 0.29 | 0.96 | 2834 |
| loop | 65 % → 64 % | 83.7 px | 0.30 | 0.99 | 1202 |
| tilted | 29 % → 29 % | 81.2 px | 0.30 | 1.00 | 473 |
| over the wet one | 62 % → 61 % | 91.1 px | 0.30 | 0.98 | 408 |
| long, no reload | 100 % → 99 % | 44.7 px | 0.29 | 0.99 | 2823 | quarters: 0.00 → 0.00 → 0.00 → 0.00

Numbers say: light vs heavy: width 109.9 → 114.6 px, dark 0.30 → 0.30; pressure barely changes the width.

## Brush Artist · Refs · #27 Orange impasto swatch
Heavy acrylic · 60 px · 26.8 s

![Brush Artist · Refs · #27 Orange impasto swatch](Brush-Artist-Refs-27-Orange-impasto-swatch.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 21 % → 21 % | 59.7 px | 0.35 | 1.00 | 175 |
| heavy line | 22 % → 22 % | 62.5 px | 0.35 | 1.00 | 185 |
| pressure swell | 17 % → 17 % | 63.2 px | 0.36 | 1.01 | 157 |
| fast wave | 49 % → 48 % | 56.3 px | 0.35 | 0.98 | 511 |
| slow wave | 49 % → 48 % | 57.1 px | 0.35 | 0.98 | 799 |
| spiral | 70 % → 63 % | 46.1 px | 0.34 | 0.91 | 779 |
| loop | 42 % → 40 % | 53.9 px | 0.35 | 0.97 | 687 |
| tilted | 17 % → 17 % | 46.9 px | 0.35 | 1.00 | 439 |
| over the wet one | 36 % → 36 % | 53.9 px | 0.35 | 1.00 | 185 |
| long, no reload | 86 % → 76 % | 38.6 px | 0.35 | 0.88 | 1525 | quarters: 0.33 → 0.31 → 0.29 → 0.27

Numbers say: light vs heavy: width 59.7 → 62.5 px, dark 0.35 → 0.35; pressure barely changes the width.

## Brush Artist · Refs · #28 Miles Davis black lines
Ink · 22 px · 26.8 s

![Brush Artist · Refs · #28 Miles Davis black lines](Brush-Artist-Refs-28-Miles-Davis-black-lines.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 4 % → 6 % | 12.3 px | 0.81 | 1.49 | 35 |
| heavy line | 17 % → 17 % | 49.0 px | 0.88 | 0.99 | 82 |
| pressure swell | 10 % → 10 % | 35.9 px | 0.87 | 1.03 | 58 |
| fast wave | 31 % → 30 % | 35.5 px | 0.87 | 0.98 | 172 |
| slow wave | 25 % → 25 % | 28.7 px | 0.87 | 0.99 | 219 |
| spiral | 39 % → 37 % | 25.5 px | 0.87 | 0.95 | 242 |
| loop | 23 % → 23 % | 29.6 px | 0.88 | 1.00 | 124 |
| tilted | 9 % → 9 % | 25.3 px | 0.88 | 1.01 | 86 |
| over the wet one | 21 % → 21 % | 34.1 px | 0.88 | 1.00 | 63 |
| long, no reload | 51 % → 43 % | 22.9 px | 0.86 | 0.84 | 449 | quarters: 0.59 → 0.51 → 0.40 → 0.31

Numbers say: light vs heavy: width 12.3 → 49.0 px, dark 0.81 → 0.88.

## Brush Artist · Refs · #29 Shrigley magenta asterisk
Watercolor · 70 px · 31.1 s

![Brush Artist · Refs · #29 Shrigley magenta asterisk](Brush-Artist-Refs-29-Shrigley-magenta-asterisk.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 10 % → 13 % | 28.0 px | 0.65 | 1.36 | 56 |
| heavy line | 17 % → 18 % | 50.3 px | 0.64 | 1.03 | 125 |
| pressure swell | 11 % → 12 % | 41.1 px | 0.65 | 1.13 | 72 |
| fast wave | 38 % → 38 % | 43.8 px | 0.64 | 1.01 | 247 |
| slow wave | 35 % → 39 % | 41.0 px | 0.65 | 1.10 | 445 |
| spiral | 61 % → 61 % | 40.0 px | 0.64 | 1.01 | 397 |
| loop | 31 % → 32 % | 40.2 px | 0.65 | 1.03 | 213 |
| tilted | 18 % → 18 % | 49.0 px | 0.65 | 1.00 | 188 |
| over the wet one | 31 % → 34 % | 38.4 px | 0.65 | 1.07 | 134 |
| long, no reload | 75 % → 75 % | 33.6 px | 0.64 | 1.00 | 630 | quarters: 0.55 → 0.53 → 0.52 → 0.49

Numbers say: light vs heavy: width 28.0 → 50.3 px, dark 0.65 → 0.64; the long stroke does not run out of paint.

## Brush Artist · Refs · #30 Red gouache face patch
Gouache · 60 px · 34.8 s

![Brush Artist · Refs · #30 Red gouache face patch](Brush-Artist-Refs-30-Red-gouache-face-patch.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 16 % → 15 % | 47.0 px | 0.49 | 0.91 | 138 |
| heavy line | 25 % → 20 % | 74.0 px | 0.49 | 0.80 | 206 |
| pressure swell | 19 % → 17 % | 72.7 px | 0.49 | 0.86 | 136 |
| fast wave | 49 % → 28 % | 56.2 px | 0.49 | 0.58 | 411 |
| slow wave | 48 % → 28 % | 55.4 px | 0.49 | 0.59 | 715 |
| spiral | 60 % → 28 % | 39.4 px | 0.49 | 0.47 | 729 |
| loop | 40 % → 29 % | 51.6 px | 0.49 | 0.74 | 357 |
| tilted | 16 % → 17 % | 46.0 px | 0.49 | 1.00 | 216 |
| over the wet one | 36 % → 32 % | 55.3 px | 0.49 | 0.89 | 211 |
| long, no reload | 67 % → 30 % | 30.1 px | 0.49 | 0.44 | 1093 | quarters: 0.43 → 0.39 → 0.32 → 0.26

Numbers say: light vs heavy: width 47.0 → 74.0 px, dark 0.49 → 0.49.

## Brush Artist · Refs · #31 Warhol blotted line
Ink · 6 px · 20.0 s

![Brush Artist · Refs · #31 Warhol blotted line](Brush-Artist-Refs-31-Warhol-blotted-line.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 1 % → 3 % | 2.7 px | 0.75 | 3.30 | 31 |
| heavy line | 7 % → 7 % | 20.7 px | 0.83 | 0.98 | 57 |
| pressure swell | 4 % → 4 % | 14.8 px | 0.84 | 1.12 | 34 |
| fast wave | 12 % → 9 % | 13.9 px | 0.82 | 0.76 | 109 |
| slow wave | 10 % → 8 % | 11.2 px | 0.80 | 0.84 | 108 |
| spiral | 15 % → 8 % | 9.7 px | 0.80 | 0.57 | 193 |
| loop | 9 % → 9 % | 11.9 px | 0.80 | 0.93 | 98 |
| tilted | 3 % → 3 % | 8.8 px | 0.84 | 1.03 | 43 |
| over the wet one | 8 % → 8 % | 14.4 px | 0.84 | 1.02 | 46 |
| long, no reload | 21 % → 9 % | 9.6 px | 0.78 | 0.43 | 293 | quarters: 0.25 → 0.13 → 0.05 → 0.01

Numbers say: light vs heavy: width 2.7 → 20.7 px, dark 0.75 → 0.83; wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #32 Thick orange swipes
Heavy acrylic · 90 px · 33.2 s

![Brush Artist · Refs · #32 Thick orange swipes](Brush-Artist-Refs-32-Thick-orange-swipes.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 31 % → 32 % | 89.3 px | 0.38 | 1.03 | 276 |
| heavy line | 32 % → 31 % | 92.9 px | 0.38 | 0.98 | 298 |
| pressure swell | 25 % → 26 % | 93.5 px | 0.39 | 1.04 | 237 |
| fast wave | 65 % → 67 % | 75.6 px | 0.38 | 1.02 | 950 |
| slow wave | 66 % → 65 % | 76.0 px | 0.38 | 0.98 | 1285 |
| spiral | 80 % → 78 % | 52.8 px | 0.38 | 0.98 | 1266 |
| loop | 57 % → 56 % | 73.4 px | 0.38 | 0.99 | 783 |
| tilted | 24 % → 24 % | 66.2 px | 0.38 | 1.00 | 410 |
| over the wet one | 51 % → 51 % | 77.2 px | 0.38 | 0.99 | 291 |
| long, no reload | 97 % → 95 % | 43.4 px | 0.38 | 0.98 | 1838 | quarters: 0.38 → 0.38 → 0.37 → 0.37

Numbers say: light vs heavy: width 89.3 → 92.9 px, dark 0.38 → 0.38; pressure barely changes the width; the long stroke does not run out of paint.

## Brush Artist · Refs · #33 Red wet-in-wet band
Watercolor · 80 px · 46.1 s

![Brush Artist · Refs · #33 Red wet-in-wet band](Brush-Artist-Refs-33-Red-wet-in-wet-band.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 19 % → 31 % | 55.6 px | 0.58 | 1.61 | 167 |
| heavy line | 29 % → 39 % | 83.7 px | 0.59 | 1.35 | 237 |
| pressure swell | 19 % → 27 % | 71.5 px | 0.61 | 1.42 | 121 |
| fast wave | 58 % → 74 % | 67.5 px | 0.61 | 1.27 | 392 |
| slow wave | 57 % → 72 % | 65.7 px | 0.63 | 1.26 | 675 |
| spiral | 75 % → 84 % | 49.6 px | 0.64 | 1.12 | 831 |
| loop | 51 % → 63 % | 66.4 px | 0.63 | 1.22 | 341 |
| tilted | 24 % → 25 % | 66.3 px | 0.60 | 1.03 | 244 |
| over the wet one | 48 % → 67 % | 66.7 px | 0.60 | 1.40 | 191 |
| long, no reload | 95 % → 99 % | 42.6 px | 0.66 | 1.04 | 1357 | quarters: 0.68 → 0.68 → 0.68 → 0.64

Numbers say: light vs heavy: width 55.6 → 83.7 px, dark 0.58 → 0.59; the long stroke does not run out of paint; wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #34 Magenta oil patches
Oil · 60 px · 24.2 s

![Brush Artist · Refs · #34 Magenta oil patches](Brush-Artist-Refs-34-Magenta-oil-patches.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 20 % → 20 % | 58.8 px | 0.61 | 1.01 | 258 |
| heavy line | 22 % → 22 % | 63.1 px | 0.61 | 1.00 | 214 |
| pressure swell | 17 % → 17 % | 62.7 px | 0.62 | 1.01 | 149 |
| fast wave | 49 % → 50 % | 56.7 px | 0.62 | 1.02 | 542 |
| slow wave | 49 % → 49 % | 57.1 px | 0.62 | 1.00 | 926 |
| spiral | 71 % → 71 % | 46.9 px | 0.61 | 1.00 | 958 |
| loop | 42 % → 42 % | 54.3 px | 0.62 | 1.00 | 782 |
| tilted | 18 % → 18 % | 49.8 px | 0.61 | 1.00 | 402 |
| over the wet one | 37 % → 37 % | 53.2 px | 0.61 | 1.00 | 371 |
| long, no reload | 88 % → 88 % | 39.2 px | 0.62 | 1.00 | 1471 | quarters: 0.59 → 0.58 → 0.56 → 0.54

Numbers say: light vs heavy: width 58.8 → 63.1 px, dark 0.61 → 0.61; pressure barely changes the width; the long stroke does not run out of paint.

## Brush Artist · Refs · #35 Red band with runs
Watercolor · 70 px · 45.4 s

![Brush Artist · Refs · #35 Red band with runs](Brush-Artist-Refs-35-Red-band-with-runs.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 17 % → 35 % | 48.3 px | 0.47 | 2.10 | 115 |
| heavy line | 25 % → 43 % | 73.9 px | 0.48 | 1.70 | 201 |
| pressure swell | 17 % → 25 % | 63.0 px | 0.53 | 1.50 | 129 |
| fast wave | 54 % → 73 % | 61.9 px | 0.51 | 1.37 | 417 |
| slow wave | 52 % → 72 % | 59.8 px | 0.54 | 1.38 | 1030 |
| spiral | 72 % → 90 % | 47.4 px | 0.55 | 1.25 | 675 |
| loop | 47 % → 75 % | 61.4 px | 0.50 | 1.59 | 358 |
| tilted | 21 % → 22 % | 58.1 px | 0.49 | 1.06 | 246 |
| over the wet one | 43 % → 73 % | 62.1 px | 0.49 | 1.69 | 170 |
| long, no reload | 92 % → 98 % | 41.5 px | 0.58 | 1.06 | 1025 | quarters: 0.60 → 0.60 → 0.59 → 0.57

Numbers say: light vs heavy: width 48.3 → 73.9 px, dark 0.47 → 0.48; the long stroke does not run out of paint; wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #36 Magenta letters flat brush
Gouache · 36 px · 31.3 s

![Brush Artist · Refs · #36 Magenta letters flat brush](Brush-Artist-Refs-36-Magenta-letters-flat-brush.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 10 % → 10 % | 29.1 px | 0.45 | 0.98 | 81 |
| heavy line | 17 % → 14 % | 49.1 px | 0.45 | 0.85 | 97 |
| pressure swell | 13 % → 12 % | 49.4 px | 0.45 | 0.89 | 69 |
| fast wave | 35 % → 19 % | 41.0 px | 0.45 | 0.54 | 219 |
| slow wave | 35 % → 19 % | 40.0 px | 0.45 | 0.54 | 390 |
| spiral | 46 % → 19 % | 30.5 px | 0.45 | 0.42 | 381 |
| loop | 27 % → 20 % | 35.4 px | 0.45 | 0.72 | 257 |
| tilted | 11 % → 11 % | 30.0 px | 0.45 | 1.00 | 101 |
| over the wet one | 24 % → 23 % | 38.1 px | 0.45 | 0.92 | 94 |
| long, no reload | 47 % → 19 % | 20.9 px | 0.45 | 0.40 | 531 | quarters: 0.29 → 0.26 → 0.22 → 0.18

Numbers say: light vs heavy: width 29.1 → 49.1 px, dark 0.45 → 0.45.

## Brush Artist · Refs · #37 Oil still life dabs
Oil · 40 px · 20.4 s

![Brush Artist · Refs · #37 Oil still life dabs](Brush-Artist-Refs-37-Oil-still-life-dabs.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 14 % → 14 % | 39.4 px | 0.39 | 1.00 | 130 |
| heavy line | 15 % → 15 % | 42.6 px | 0.39 | 1.00 | 204 |
| pressure swell | 11 % → 11 % | 42.0 px | 0.40 | 1.00 | 150 |
| fast wave | 35 % → 35 % | 40.4 px | 0.39 | 1.00 | 424 |
| slow wave | 35 % → 35 % | 40.8 px | 0.39 | 1.00 | 620 |
| spiral | 59 % → 59 % | 39.1 px | 0.38 | 1.00 | 619 |
| loop | 29 % → 29 % | 37.8 px | 0.39 | 1.00 | 327 |
| tilted | 13 % → 14 % | 37.6 px | 0.39 | 1.00 | 182 |
| over the wet one | 27 % → 27 % | 37.3 px | 0.39 | 1.00 | 152 |
| long, no reload | 69 % → 69 % | 31.1 px | 0.37 | 1.00 | 890 | quarters: 0.31 → 0.30 → 0.28 → 0.25

Numbers say: light vs heavy: width 39.4 → 42.6 px, dark 0.39 → 0.39; pressure barely changes the width.

## Brush Artist · Refs · #38 Sanguine drawing
Pastel · 6 px · 9.1 s

![Brush Artist · Refs · #38 Sanguine drawing](Brush-Artist-Refs-38-Sanguine-drawing.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 1 % → 1 % | 2.0 px | 0.61 | 1.00 | 22 |
| heavy line | 1 % → 1 % | 3.5 px | 0.62 | 1.00 | 18 |
| pressure swell | 1 % → 1 % | 3.3 px | 0.62 | 1.00 | 12 |
| fast wave | 3 % → 3 % | 3.2 px | 0.61 | 1.00 | 41 |
| slow wave | 3 % → 3 % | 3.0 px | 0.61 | 1.00 | 39 |
| spiral | 4 % → 4 % | 2.9 px | 0.61 | 1.00 | 68 |
| loop | 2 % → 2 % | 3.0 px | 0.61 | 1.00 | 36 |
| tilted | 1 % → 1 % | 3.4 px | 0.62 | 1.00 | 20 |
| over the wet one | 2 % → 2 % | 2.9 px | 0.62 | 1.00 | 17 |
| long, no reload | 7 % → 7 % | 3.0 px | 0.61 | 1.00 | 104 | quarters: 0.04 → 0.05 → 0.05 → 0.05

Numbers say: light vs heavy: width 2.0 → 3.5 px, dark 0.61 → 0.62; the long stroke does not run out of paint.

## Brush Artist · Refs · #39 Very thick impasto
Heavy acrylic · 60 px · 27.8 s

![Brush Artist · Refs · #39 Very thick impasto](Brush-Artist-Refs-39-Very-thick-impasto.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 21 % → 21 % | 59.8 px | 0.61 | 1.02 | 177 |
| heavy line | 22 % → 22 % | 62.6 px | 0.61 | 1.02 | 180 |
| pressure swell | 17 % → 17 % | 63.3 px | 0.63 | 1.03 | 133 |
| fast wave | 49 % → 48 % | 56.4 px | 0.62 | 0.99 | 501 |
| slow wave | 50 % → 49 % | 57.3 px | 0.62 | 0.98 | 1133 |
| spiral | 70 % → 66 % | 46.3 px | 0.62 | 0.94 | 793 |
| loop | 42 % → 41 % | 54.0 px | 0.62 | 0.97 | 412 |
| tilted | 17 % → 17 % | 46.9 px | 0.62 | 1.00 | 235 |
| over the wet one | 36 % → 37 % | 54.0 px | 0.62 | 1.02 | 199 |
| long, no reload | 87 % → 80 % | 38.8 px | 0.62 | 0.93 | 1172 | quarters: 0.58 → 0.57 → 0.55 → 0.53

Numbers say: light vs heavy: width 59.8 → 62.6 px, dark 0.61 → 0.61; pressure barely changes the width; the long stroke does not run out of paint.

## Brush Artist · Refs · #40 Watercolour blooms
Watercolor · 90 px · 50.5 s

![Brush Artist · Refs · #40 Watercolour blooms](Brush-Artist-Refs-40-Watercolour-blooms.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 22 % → 34 % | 63.3 px | 0.10 | 1.54 | 141 |
| heavy line | 33 % → 42 % | 94.9 px | 0.11 | 1.28 | 232 |
| pressure swell | 22 % → 30 % | 84.1 px | 0.12 | 1.34 | 147 |
| fast wave | 64 % → 79 % | 73.9 px | 0.11 | 1.23 | 480 |
| slow wave | 63 % → 76 % | 72.4 px | 0.16 | 1.21 | 818 |
| spiral | 79 % → 87 % | 52.1 px | 0.15 | 1.10 | 796 |
| loop | 56 % → 66 % | 72.5 px | 0.13 | 1.18 | 445 |
| tilted | 26 % → 27 % | 73.1 px | 0.13 | 1.03 | 295 |
| over the wet one | 53 % → 72 % | 73.8 px | 0.13 | 1.36 | 206 |
| long, no reload | 97 % → 100 % | 43.6 px | 0.17 | 1.02 | 1196 | quarters: 0.21 → 0.19 → 0.17 → 0.13

Numbers say: light vs heavy: width 63.3 → 94.9 px, dark 0.10 → 0.11; wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #41 Coloured pencil hatching
Pastel · 4 px · 8.9 s

![Brush Artist · Refs · #41 Coloured pencil hatching](Brush-Artist-Refs-41-Coloured-pencil-hatching.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 1 % → 1 % | 1.6 px | 0.42 | 1.00 | 13 |
| heavy line | 1 % → 1 % | 2.6 px | 0.43 | 1.00 | 12 |
| pressure swell | 1 % → 1 % | 2.1 px | 0.43 | 1.00 | 9 |
| fast wave | 2 % → 2 % | 2.2 px | 0.42 | 1.00 | 29 |
| slow wave | 2 % → 2 % | 2.1 px | 0.43 | 1.00 | 29 |
| spiral | 3 % → 3 % | 2.1 px | 0.43 | 1.00 | 53 |
| loop | 2 % → 2 % | 2.2 px | 0.43 | 1.00 | 29 |
| tilted | 1 % → 1 % | 3.0 px | 0.42 | 1.00 | 15 |
| over the wet one | 2 % → 2 % | 2.2 px | 0.42 | 1.00 | 12 |
| long, no reload | 5 % → 5 % | 2.3 px | 0.43 | 1.00 | 76 | quarters: 0.02 → 0.02 → 0.02 → 0.03

Numbers say: light vs heavy: width 1.6 → 2.6 px, dark 0.42 → 0.43; the long stroke does not run out of paint.

## Brush Artist · Refs · #42 Oil pastel shaggy
Pastel · 18 px · 11.2 s

![Brush Artist · Refs · #42 Oil pastel shaggy](Brush-Artist-Refs-42-Oil-pastel-shaggy.png)

A light paint: laid on a grey sheet (on white it cannot be seen); **dark** = how far it is from the grey either way.

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 2 % → 2 % | 5.1 px | 0.35 | 1.00 | 20 |
| heavy line | 4 % → 4 % | 10.7 px | 0.36 | 1.00 | 26 |
| pressure swell | 3 % → 3 % | 9.5 px | 0.36 | 1.00 | 21 |
| fast wave | 8 % → 8 % | 9.0 px | 0.36 | 1.00 | 72 |
| slow wave | 7 % → 7 % | 8.2 px | 0.36 | 1.00 | 93 |
| spiral | 12 % → 12 % | 7.7 px | 0.36 | 1.00 | 120 |
| loop | 6 % → 6 % | 7.9 px | 0.36 | 1.00 | 58 |
| tilted | 2 % → 2 % | 6.9 px | 0.36 | 1.00 | 32 |
| over the wet one | 6 % → 6 % | 8.5 px | 0.36 | 1.00 | 27 |
| long, no reload | 15 % → 15 % | 6.9 px | 0.36 | 1.00 | 168 | quarters: 0.00 → 0.00 → 0.00 → 0.00

Numbers say: light vs heavy: width 5.1 → 10.7 px, dark 0.35 → 0.36; the long stroke does not run out of paint.

## Brush Artist · Refs · #43 Dragged black ink blocks
Gouache · 70 px · 28.2 s

![Brush Artist · Refs · #43 Dragged black ink blocks](Brush-Artist-Refs-43-Dragged-black-ink-blocks.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 11 % → 0 % | 31.1 px | 0.65 | 0.03 | 119 |
| heavy line | 16 % → 1 % | 46.9 px | 0.65 | 0.08 | 306 |
| pressure swell | 12 % → 1 % | 44.8 px | 0.65 | 0.11 | 179 |
| fast wave | 22 % → 2 % | 25.8 px | 0.65 | 0.09 | 561 |
| slow wave | 34 % → 4 % | 39.7 px | 0.65 | 0.13 | 904 |
| spiral | 40 % → 4 % | 26.3 px | 0.65 | 0.11 | 879 |
| loop | 28 % → 4 % | 36.5 px | 0.65 | 0.14 | 469 |
| tilted | 10 % → 10 % | 28.3 px | 0.65 | 0.98 | 257 |
| over the wet one | 24 % → 9 % | 40.0 px | 0.65 | 0.36 | 224 |
| long, no reload | 47 % → 8 % | 20.9 px | 0.65 | 0.16 | 1490 | quarters: 0.45 → 0.36 → 0.28 → 0.23

Numbers say: light vs heavy: width 31.1 → 46.9 px, dark 0.65 → 0.65.

## Brush Artist · Refs · #44 Blue looping ribbon
Oil · 80 px · 27.6 s

![Brush Artist · Refs · #44 Blue looping ribbon](Brush-Artist-Refs-44-Blue-looping-ribbon.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 28 % → 29 % | 80.0 px | 0.72 | 1.04 | 279 |
| heavy line | 29 % → 29 % | 85.0 px | 0.72 | 1.00 | 313 |
| pressure swell | 23 % → 23 % | 84.4 px | 0.72 | 1.03 | 241 |
| fast wave | 63 % → 65 % | 72.4 px | 0.72 | 1.04 | 792 |
| slow wave | 62 % → 62 % | 72.1 px | 0.73 | 1.00 | 1290 |
| spiral | 79 % → 79 % | 51.9 px | 0.72 | 1.00 | 1297 |
| loop | 54 % → 54 % | 69.7 px | 0.73 | 1.00 | 739 |
| tilted | 22 % → 22 % | 62.4 px | 0.72 | 1.00 | 372 |
| over the wet one | 47 % → 48 % | 70.0 px | 0.72 | 1.01 | 419 |
| long, no reload | 97 % → 97 % | 43.5 px | 0.73 | 1.00 | 2097 | quarters: 0.72 → 0.72 → 0.72 → 0.72

Numbers say: light vs heavy: width 80.0 → 85.0 px, dark 0.72 → 0.72; pressure barely changes the width; the long stroke does not run out of paint.

## Brush Artist · Refs · #45 Soft pastel pepper
Pastel · 40 px · 12.0 s

![Brush Artist · Refs · #45 Soft pastel pepper](Brush-Artist-Refs-45-Soft-pastel-pepper.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 4 % → 4 % | 11.3 px | 0.53 | 1.00 | 55 |
| heavy line | 8 % → 8 % | 23.0 px | 0.53 | 1.00 | 54 |
| pressure swell | 5 % → 5 % | 19.5 px | 0.53 | 1.00 | 41 |
| fast wave | 17 % → 17 % | 19.4 px | 0.53 | 1.00 | 172 |
| slow wave | 15 % → 15 % | 17.1 px | 0.53 | 1.00 | 237 |
| spiral | 25 % → 25 % | 16.3 px | 0.53 | 1.00 | 249 |
| loop | 12 % → 12 % | 16.1 px | 0.53 | 1.00 | 121 |
| tilted | 5 % → 5 % | 12.8 px | 0.53 | 1.00 | 64 |
| over the wet one | 11 % → 11 % | 17.7 px | 0.53 | 1.00 | 54 |
| long, no reload | 30 % → 30 % | 13.6 px | 0.53 | 1.00 | 341 | quarters: 0.18 → 0.18 → 0.18 → 0.18

Numbers say: light vs heavy: width 11.3 → 23.0 px, dark 0.53 → 0.53; the long stroke does not run out of paint.

## Brush Artist · Refs · #46 Red-brown ink lips
Watercolor · 50 px · 41.4 s

![Brush Artist · Refs · #46 Red-brown ink lips](Brush-Artist-Refs-46-Red-brown-ink-lips.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 12 % → 24 % | 33.6 px | 0.66 | 2.04 | 62 |
| heavy line | 19 % → 30 % | 54.1 px | 0.64 | 1.62 | 107 |
| pressure swell | 12 % → 21 % | 43.7 px | 0.67 | 1.76 | 69 |
| fast wave | 40 % → 61 % | 46.7 px | 0.66 | 1.50 | 228 |
| slow wave | 39 % → 59 % | 44.6 px | 0.68 | 1.54 | 394 |
| spiral | 63 % → 76 % | 41.7 px | 0.70 | 1.20 | 381 |
| loop | 35 % → 52 % | 44.9 px | 0.67 | 1.51 | 316 |
| tilted | 16 % → 17 % | 43.6 px | 0.66 | 1.07 | 173 |
| over the wet one | 33 % → 52 % | 47.6 px | 0.66 | 1.58 | 146 |
| long, no reload | 79 % → 95 % | 35.4 px | 0.70 | 1.21 | 733 | quarters: 0.71 → 0.71 → 0.70 → 0.65

Numbers say: light vs heavy: width 33.6 → 54.1 px, dark 0.66 → 0.64; the long stroke does not run out of paint; wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #47 Pink knife slabs
Heavy acrylic · 90 px · 30.7 s

![Brush Artist · Refs · #47 Pink knife slabs](Brush-Artist-Refs-47-Pink-knife-slabs.png)

A light paint: laid on a grey sheet (on white it cannot be seen); **dark** = how far it is from the grey either way.

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 30 % → 30 % | 88.0 px | 0.29 | 0.98 | 205 |
| heavy line | 31 % → 30 % | 90.3 px | 0.29 | 0.97 | 234 |
| pressure swell | 24 % → 25 % | 91.2 px | 0.28 | 1.01 | 152 |
| fast wave | 63 % → 62 % | 73.0 px | 0.28 | 0.98 | 544 |
| slow wave | 64 % → 61 % | 73.7 px | 0.27 | 0.96 | 1003 |
| spiral | 77 % → 59 % | 50.8 px | 0.27 | 0.76 | 1368 |
| loop | 55 % → 54 % | 71.8 px | 0.28 | 0.97 | 701 |
| tilted | 24 % → 24 % | 66.3 px | 0.29 | 1.00 | 352 |
| over the wet one | 51 % → 49 % | 74.8 px | 0.29 | 0.97 | 290 |
| long, no reload | 94 % → 78 % | 42.1 px | 0.26 | 0.83 | 1536 | quarters: 0.00 → 0.00 → 0.00 → 0.00

Numbers say: light vs heavy: width 88.0 → 90.3 px, dark 0.29 → 0.29; pressure barely changes the width; the long stroke does not run out of paint.

## Brush Artist · Refs · #48 Black bands with drips
Gouache · 70 px · 43.7 s

![Brush Artist · Refs · #48 Black bands with drips](Brush-Artist-Refs-48-Black-bands-with-drips.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 19 % → 18 % | 54.7 px | 0.68 | 0.94 | 244 |
| heavy line | 29 % → 24 % | 83.1 px | 0.68 | 0.85 | 246 |
| pressure swell | 23 % → 21 % | 86.1 px | 0.68 | 0.92 | 167 |
| fast wave | 54 % → 37 % | 62.8 px | 0.68 | 0.67 | 519 |
| slow wave | 54 % → 36 % | 61.9 px | 0.68 | 0.67 | 1060 |
| spiral | 64 % → 35 % | 42.2 px | 0.68 | 0.54 | 917 |
| loop | 45 % → 37 % | 58.1 px | 0.68 | 0.82 | 529 |
| tilted | 19 % → 19 % | 52.5 px | 0.68 | 1.00 | 266 |
| over the wet one | 41 % → 38 % | 62.5 px | 0.68 | 0.92 | 236 |
| long, no reload | 74 % → 37 % | 33.4 px | 0.68 | 0.50 | 1205 | quarters: 0.64 → 0.61 → 0.54 → 0.44

Numbers say: light vs heavy: width 54.7 → 83.1 px, dark 0.68 → 0.68.

## Brush Artist · Refs · #49 Magenta letters round brush
Ink · 30 px · 30.5 s

![Brush Artist · Refs · #49 Magenta letters round brush](Brush-Artist-Refs-49-Magenta-letters-round-brush.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 6 % → 8 % | 17.5 px | 0.50 | 1.29 | 44 |
| heavy line | 21 % → 21 % | 62.0 px | 0.51 | 0.99 | 106 |
| pressure swell | 12 % → 13 % | 46.3 px | 0.52 | 1.02 | 62 |
| fast wave | 39 % → 38 % | 44.8 px | 0.51 | 0.99 | 190 |
| slow wave | 32 % → 31 % | 36.7 px | 0.51 | 0.99 | 307 |
| spiral | 50 % → 49 % | 33.2 px | 0.51 | 0.97 | 528 |
| loop | 29 % → 29 % | 37.8 px | 0.51 | 1.00 | 253 |
| tilted | 11 % → 11 % | 31.0 px | 0.52 | 1.01 | 87 |
| over the wet one | 26 % → 26 % | 42.0 px | 0.52 | 1.01 | 75 |
| long, no reload | 62 % → 56 % | 27.7 px | 0.50 | 0.91 | 455 | quarters: 0.41 → 0.36 → 0.30 → 0.25

Numbers say: light vs heavy: width 17.5 → 62.0 px, dark 0.50 → 0.51.

## Brush Artist · Refs · #50 Thick swipes on photo
Heavy acrylic · 40 px · 22.8 s

![Brush Artist · Refs · #50 Thick swipes on photo](Brush-Artist-Refs-50-Thick-swipes-on-photo.png)

A light paint: laid on a grey sheet (on white it cannot be seen); **dark** = how far it is from the grey either way.

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 14 % → 13 % | 39.4 px | 0.26 | 0.99 | 162 |
| heavy line | 14 % → 14 % | 41.6 px | 0.26 | 0.98 | 168 |
| pressure swell | 11 % → 11 % | 41.9 px | 0.25 | 0.99 | 120 |
| fast wave | 34 % → 31 % | 38.9 px | 0.25 | 0.93 | 431 |
| slow wave | 34 % → 33 % | 39.7 px | 0.26 | 0.95 | 617 |
| spiral | 59 % → 47 % | 38.9 px | 0.25 | 0.80 | 591 |
| loop | 28 % → 27 % | 36.9 px | 0.26 | 0.95 | 277 |
| tilted | 13 % → 13 % | 35.4 px | 0.26 | 1.00 | 137 |
| over the wet one | 26 % → 25 % | 36.8 px | 0.26 | 0.98 | 120 |
| long, no reload | 66 % → 46 % | 29.8 px | 0.24 | 0.69 | 734 | quarters: 0.00 → 0.00 → 0.00 → 0.00

Numbers say: light vs heavy: width 39.4 → 41.6 px, dark 0.26 → 0.26; pressure barely changes the width; the long stroke does not run out of paint.

## Brush Artist · Refs · Drag #e8b4a8
Gouache · 40 px · 18.7 s

![Brush Artist · Refs · Drag #e8b4a8](Brush-Artist-Refs-Drag-e8b4a8.png)

A light paint: laid on a grey sheet (on white it cannot be seen); **dark** = how far it is from the grey either way.

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 2 % → 0 % | 5.0 px | 0.00 | 0.00 | 110 |
| heavy line | 3 % → 0 % | 8.7 px | 0.00 | 0.00 | 121 |
| pressure swell | 2 % → 0 % | 9.1 px | 0.00 | 0.00 | 81 |
| fast wave | 3 % → 0 % | 3.4 px | 0.00 | 0.00 | 263 |
| slow wave | 9 % → 0 % | 10.9 px | 0.00 | 0.00 | 508 |
| spiral | 10 % → 0 % | 6.9 px | 0.00 | 0.00 | 478 |
| loop | 6 % → 0 % | 7.9 px | 0.34 | 0.01 | 256 |
| tilted | 2 % → 2 % | 6.3 px | 0.34 | 0.89 | 132 |
| over the wet one | 5 % → 0 % | 8.2 px | 0.34 | 0.02 | 119 |
| long, no reload | 12 % → 0 % | 5.4 px | 0.34 | 0.01 | 695 | quarters: 0.01 → 0.01 → 0.01 → 0.01

Numbers say: light vs heavy: width 5.0 → 8.7 px, dark 0.00 → 0.00; the long stroke does not run out of paint.

## Brush Artist · Refs · Drag #e8e4e0
Gouache · 40 px · 19.3 s

![Brush Artist · Refs · Drag #e8e4e0](Brush-Artist-Refs-Drag-e8e4e0.png)

A light paint: laid on a grey sheet (on white it cannot be seen); **dark** = how far it is from the grey either way.

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 2 % → 0 % | 5.0 px | 0.00 | 0.00 | 97 |
| heavy line | 3 % → 0 % | 8.7 px | 0.00 | 0.00 | 118 |
| pressure swell | 2 % → 0 % | 9.1 px | 0.00 | 0.00 | 77 |
| fast wave | 3 % → 0 % | 3.4 px | 0.00 | 0.00 | 410 |
| slow wave | 9 % → 0 % | 10.9 px | 0.00 | 0.00 | 557 |
| spiral | 10 % → 0 % | 6.9 px | 0.00 | 0.00 | 502 |
| loop | 6 % → 0 % | 7.9 px | 0.42 | 0.01 | 243 |
| tilted | 2 % → 2 % | 6.3 px | 0.42 | 0.89 | 136 |
| over the wet one | 5 % → 0 % | 8.2 px | 0.42 | 0.02 | 126 |
| long, no reload | 12 % → 0 % | 5.4 px | 0.43 | 0.01 | 701 | quarters: 0.01 → 0.01 → 0.01 → 0.01

Numbers say: light vs heavy: width 5.0 → 8.7 px, dark 0.00 → 0.00; the long stroke does not run out of paint.

## Brush Artist · Refs · Finger
Pastel · 36 px · 20.4 s · over bands of wet oil paint and oil pastel in turn (it works on paint already there: look at what it does to the bands; covered counts the bands too)

![Brush Artist · Refs · Finger](Brush-Artist-Refs-Finger.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 25 % → 25 % | 73.9 px | 0.80 | 1.00 | 46 |
| heavy line | 27 % → 27 % | 78.5 px | 0.80 | 1.00 | 54 |
| pressure swell | 26 % → 26 % | 97.7 px | 0.80 | 1.00 | 40 |
| fast wave | 32 % → 32 % | 37.1 px | 0.78 | 1.00 | 131 |
| slow wave | 31 % → 31 % | 36.2 px | 0.78 | 1.00 | 253 |
| spiral | 38 % → 38 % | 25.0 px | 0.76 | 1.00 | 221 |
| loop | 30 % → 30 % | 39.4 px | 0.78 | 1.00 | 116 |
| tilted | 26 % → 26 % | 73.4 px | 0.79 | 1.00 | 64 |
| over the wet one | 29 % → 29 % | 6.7 px | 0.79 | 1.00 | 57 |
| long, no reload | 40 % → 40 % | 18.0 px | 0.75 | 1.00 | 310 | quarters: 0.25 → 0.36 → 0.33 → 0.38

Numbers say: light vs heavy: width 73.9 → 78.5 px, dark 0.80 → 0.80; pressure barely changes the width; the long stroke does not run out of paint.

## Brush Artist · Ink — wash
Watercolor · 38 px · 31.4 s

![Brush Artist · Ink — wash](Brush-Artist-Ink-wash.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 11 % → 11 % | 31.6 px | 0.38 | 1.04 | 61 |
| heavy line | 19 % → 19 % | 54.3 px | 0.32 | 1.03 | 94 |
| pressure swell | 12 % → 12 % | 45.1 px | 0.36 | 1.04 | 60 |
| fast wave | 39 % → 41 % | 45.5 px | 0.30 | 1.04 | 191 |
| slow wave | 37 % → 38 % | 42.9 px | 0.37 | 1.03 | 418 |
| spiral | 58 % → 60 % | 38.5 px | 0.30 | 1.04 | 442 |
| loop | 32 % → 33 % | 41.9 px | 0.35 | 1.02 | 177 |
| tilted | 13 % → 14 % | 36.9 px | 0.38 | 1.04 | 101 |
| over the wet one | 29 % → 30 % | 42.7 px | 0.38 | 1.04 | 77 |
| long, no reload | 67 % → 71 % | 29.9 px | 0.29 | 1.07 | 450 | quarters: 0.33 → 0.26 → 0.19 → 0.12

Numbers say: light vs heavy: width 31.6 → 54.3 px, dark 0.38 → 0.32.

## Brush Artist · Ink — brush line
Ink · 16 px · 24.4 s

![Brush Artist · Ink — brush line](Brush-Artist-Ink-brush-line.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 3 % → 5 % | 7.7 px | 0.78 | 1.81 | 36 |
| heavy line | 13 % → 13 % | 39.0 px | 0.88 | 0.99 | 81 |
| pressure swell | 8 % → 8 % | 28.4 px | 0.87 | 1.05 | 46 |
| fast wave | 24 % → 23 % | 28.0 px | 0.87 | 0.96 | 141 |
| slow wave | 20 % → 19 % | 22.6 px | 0.87 | 0.97 | 172 |
| spiral | 30 % → 27 % | 20.1 px | 0.86 | 0.89 | 245 |
| loop | 18 % → 18 % | 23.6 px | 0.88 | 1.00 | 122 |
| tilted | 7 % → 7 % | 20.5 px | 0.88 | 1.01 | 67 |
| over the wet one | 17 % → 17 % | 26.8 px | 0.88 | 1.00 | 58 |
| long, no reload | 42 % → 30 % | 18.9 px | 0.85 | 0.71 | 538 | quarters: 0.49 → 0.40 → 0.30 → 0.20

Numbers say: light vs heavy: width 7.7 → 39.0 px, dark 0.78 → 0.88; wet paint spreads well beyond the stroke.

## Brush Artist · Ink — dry brush
Gouache · 30 px · 18.8 s

![Brush Artist · Ink — dry brush](Brush-Artist-Ink-dry-brush.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 3 % → 0 % | 9.2 px | 0.77 | 0.00 | 55 |
| heavy line | 5 % → 0 % | 14.0 px | 0.00 | 0.00 | 121 |
| pressure swell | 4 % → 0 % | 13.5 px | 0.77 | 0.01 | 80 |
| fast wave | 7 % → 0 % | 8.0 px | 0.77 | 0.00 | 205 |
| slow wave | 11 % → 0 % | 12.2 px | 0.77 | 0.01 | 380 |
| spiral | 14 % → 0 % | 9.2 px | 0.77 | 0.01 | 411 |
| loop | 9 % → 0 % | 11.1 px | 0.77 | 0.02 | 249 |
| tilted | 4 % → 4 % | 11.2 px | 0.77 | 0.94 | 143 |
| over the wet one | 8 % → 1 % | 12.2 px | 0.77 | 0.10 | 104 |
| long, no reload | 16 % → 1 % | 7.2 px | 0.77 | 0.03 | 520 | quarters: 0.21 → 0.15 → 0.12 → 0.11

Numbers say: light vs heavy: width 9.2 → 14.0 px, dark 0.77 → 0.00.

## Brush Artist · Watercolour — blue
Watercolor · 40 px · 27.0 s

![Brush Artist · Watercolour — blue](Brush-Artist-Watercolour-blue.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 6 % → 10 % | 16.7 px | 0.25 | 1.71 | 30 |
| heavy line | 11 % → 12 % | 31.5 px | 0.25 | 1.13 | 64 |
| pressure swell | 7 % → 9 % | 25.4 px | 0.26 | 1.32 | 38 |
| fast wave | 24 % → 25 % | 27.8 px | 0.24 | 1.06 | 134 |
| slow wave | 22 % → 27 % | 25.9 px | 0.26 | 1.22 | 227 |
| spiral | 38 % → 41 % | 25.2 px | 0.22 | 1.08 | 224 |
| loop | 20 % → 22 % | 25.3 px | 0.26 | 1.13 | 169 |
| tilted | 12 % → 12 % | 33.3 px | 0.26 | 1.00 | 136 |
| over the wet one | 21 % → 24 % | 24.7 px | 0.26 | 1.15 | 85 |
| long, no reload | 52 % → 54 % | 23.1 px | 0.22 | 1.04 | 339 | quarters: 0.18 → 0.14 → 0.11 → 0.08

Numbers say: light vs heavy: width 16.7 → 31.5 px, dark 0.25 → 0.25; wet paint spreads well beyond the stroke.

## Brush Artist · Watercolour — violet
Watercolor · 40 px · 27.5 s

![Brush Artist · Watercolour — violet](Brush-Artist-Watercolour-violet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 6 % → 10 % | 16.7 px | 0.40 | 1.71 | 31 |
| heavy line | 11 % → 12 % | 31.5 px | 0.40 | 1.13 | 66 |
| pressure swell | 7 % → 9 % | 25.4 px | 0.41 | 1.32 | 41 |
| fast wave | 24 % → 25 % | 27.8 px | 0.38 | 1.06 | 233 |
| slow wave | 22 % → 27 % | 25.9 px | 0.41 | 1.22 | 357 |
| spiral | 38 % → 41 % | 25.2 px | 0.36 | 1.08 | 225 |
| loop | 20 % → 22 % | 25.3 px | 0.40 | 1.13 | 116 |
| tilted | 12 % → 12 % | 33.3 px | 0.40 | 1.00 | 93 |
| over the wet one | 21 % → 24 % | 24.7 px | 0.40 | 1.15 | 55 |
| long, no reload | 52 % → 54 % | 23.1 px | 0.34 | 1.04 | 365 | quarters: 0.28 → 0.22 → 0.18 → 0.14

Numbers say: light vs heavy: width 16.7 → 31.5 px, dark 0.40 → 0.40; wet paint spreads well beyond the stroke.

## Brush Artist · Watercolour — teal
Watercolor · 40 px · 26.8 s

![Brush Artist · Watercolour — teal](Brush-Artist-Watercolour-teal.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 6 % → 10 % | 16.7 px | 0.16 | 1.71 | 32 |
| heavy line | 11 % → 12 % | 31.5 px | 0.16 | 1.13 | 108 |
| pressure swell | 7 % → 9 % | 25.4 px | 0.17 | 1.32 | 71 |
| fast wave | 24 % → 25 % | 27.8 px | 0.15 | 1.06 | 242 |
| slow wave | 22 % → 27 % | 25.9 px | 0.17 | 1.22 | 222 |
| spiral | 38 % → 41 % | 25.2 px | 0.15 | 1.08 | 257 |
| loop | 20 % → 22 % | 25.3 px | 0.16 | 1.13 | 113 |
| tilted | 12 % → 12 % | 33.3 px | 0.16 | 1.00 | 95 |
| over the wet one | 21 % → 24 % | 24.7 px | 0.16 | 1.15 | 63 |
| long, no reload | 52 % → 54 % | 23.1 px | 0.14 | 1.04 | 481 | quarters: 0.11 → 0.09 → 0.07 → 0.06

Numbers say: light vs heavy: width 16.7 → 31.5 px, dark 0.16 → 0.16; wet paint spreads well beyond the stroke.

## Brush Artist · Gouache
Gouache · 30 px · 29.3 s

![Brush Artist · Gouache](Brush-Artist-Gouache.png)

A light paint: laid on a grey sheet (on white it cannot be seen); **dark** = how far it is from the grey either way.

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 8 % → 8 % | 24.4 px | 0.27 | 0.97 | 65 |
| heavy line | 15 % → 12 % | 42.9 px | 0.27 | 0.78 | 83 |
| pressure swell | 11 % → 9 % | 41.1 px | 0.27 | 0.85 | 56 |
| fast wave | 30 % → 14 % | 35.0 px | 0.26 | 0.45 | 186 |
| slow wave | 29 % → 14 % | 34.0 px | 0.26 | 0.47 | 333 |
| spiral | 40 % → 14 % | 26.7 px | 0.26 | 0.35 | 312 |
| loop | 24 % → 15 % | 30.6 px | 0.26 | 0.62 | 166 |
| tilted | 10 % → 10 % | 27.5 px | 0.27 | 1.01 | 99 |
| over the wet one | 22 % → 19 % | 32.8 px | 0.27 | 0.89 | 110 |
| long, no reload | 43 % → 15 % | 19.1 px | 0.26 | 0.35 | 466 | quarters: 0.01 → 0.01 → 0.01 → 0.01

Numbers say: light vs heavy: width 24.4 → 42.9 px, dark 0.27 → 0.27; the long stroke does not run out of paint.

## Brush Artist · Oil — bristle
Oil · 30 px · 18.7 s

![Brush Artist · Oil — bristle](Brush-Artist-Oil-bristle.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 9 % → 9 % | 27.1 px | 0.54 | 1.00 | 105 |
| heavy line | 10 % → 10 % | 29.4 px | 0.54 | 1.00 | 113 |
| pressure swell | 8 % → 8 % | 29.3 px | 0.55 | 1.00 | 80 |
| fast wave | 24 % → 24 % | 27.6 px | 0.55 | 1.00 | 287 |
| slow wave | 25 % → 25 % | 28.6 px | 0.55 | 1.00 | 490 |
| spiral | 39 % → 39 % | 25.8 px | 0.54 | 1.00 | 538 |
| loop | 20 % → 20 % | 26.3 px | 0.54 | 1.00 | 261 |
| tilted | 11 % → 11 % | 30.6 px | 0.53 | 1.00 | 200 |
| over the wet one | 20 % → 20 % | 26.4 px | 0.53 | 1.00 | 166 |
| long, no reload | 50 % → 50 % | 22.5 px | 0.54 | 1.00 | 726 | quarters: 0.32 → 0.30 → 0.29 → 0.28

Numbers say: light vs heavy: width 27.1 → 29.4 px, dark 0.54 → 0.54; pressure barely changes the width; the long stroke does not run out of paint.

## Brush Artist · Charcoal — stick
Charcoal · 28 px · 9.7 s

![Brush Artist · Charcoal — stick](Brush-Artist-Charcoal-stick.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 3 % → 3 % | 8.4 px | 0.85 | 1.00 | 18 |
| heavy line | 6 % → 6 % | 17.8 px | 0.85 | 1.00 | 21 |
| pressure swell | 4 % → 4 % | 13.9 px | 0.85 | 1.00 | 15 |
| fast wave | 12 % → 12 % | 14.0 px | 0.85 | 1.00 | 47 |
| slow wave | 11 % → 11 % | 12.5 px | 0.85 | 1.00 | 86 |
| spiral | 19 % → 19 % | 12.7 px | 0.85 | 1.00 | 81 |
| loop | 10 % → 10 % | 12.8 px | 0.85 | 1.00 | 41 |
| tilted | 4 % → 4 % | 10.9 px | 0.85 | 1.00 | 35 |
| over the wet one | 9 % → 9 % | 13.5 px | 0.85 | 1.00 | 20 |
| long, no reload | 27 % → 27 % | 12.2 px | 0.85 | 1.00 | 121 | quarters: 0.26 → 0.25 → 0.26 → 0.27

Numbers say: light vs heavy: width 8.4 → 17.8 px, dark 0.85 → 0.85; the long stroke does not run out of paint.

## Brush Artist · Charcoal — stick B
Charcoal · 36 px · 10.0 s

![Brush Artist · Charcoal — stick B](Brush-Artist-Charcoal-stick-B.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 4 % → 4 % | 10.5 px | 0.85 | 1.00 | 24 |
| heavy line | 7 % → 7 % | 21.1 px | 0.85 | 1.00 | 32 |
| pressure swell | 4 % → 4 % | 16.5 px | 0.85 | 1.00 | 21 |
| fast wave | 15 % → 15 % | 16.8 px | 0.85 | 1.00 | 64 |
| slow wave | 13 % → 13 % | 14.7 px | 0.85 | 1.00 | 109 |
| spiral | 23 % → 23 % | 15.0 px | 0.85 | 1.00 | 117 |
| loop | 11 % → 11 % | 14.8 px | 0.85 | 1.00 | 56 |
| tilted | 4 % → 4 % | 12.3 px | 0.85 | 1.00 | 40 |
| over the wet one | 10 % → 10 % | 15.9 px | 0.85 | 1.00 | 28 |
| long, no reload | 31 % → 31 % | 13.9 px | 0.85 | 1.00 | 160 | quarters: 0.30 → 0.28 → 0.29 → 0.30

Numbers say: light vs heavy: width 10.5 → 21.1 px, dark 0.85 → 0.85; the long stroke does not run out of paint.

## Brush Artist · Charcoal — stick C
Charcoal · 22 px · 9.4 s

![Brush Artist · Charcoal — stick C](Brush-Artist-Charcoal-stick-C.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 2 % → 2 % | 6.9 px | 0.85 | 1.00 | 17 |
| heavy line | 5 % → 5 % | 15.3 px | 0.85 | 1.00 | 17 |
| pressure swell | 3 % → 3 % | 12.2 px | 0.85 | 1.00 | 12 |
| fast wave | 10 % → 10 % | 12.1 px | 0.85 | 1.00 | 40 |
| slow wave | 9 % → 9 % | 10.8 px | 0.85 | 1.00 | 66 |
| spiral | 17 % → 17 % | 11.0 px | 0.85 | 1.00 | 86 |
| loop | 9 % → 9 % | 11.4 px | 0.85 | 1.00 | 38 |
| tilted | 4 % → 4 % | 9.9 px | 0.85 | 1.00 | 26 |
| over the wet one | 8 % → 8 % | 11.7 px | 0.85 | 1.00 | 17 |
| long, no reload | 24 % → 24 % | 11.0 px | 0.85 | 1.00 | 100 | quarters: 0.24 → 0.22 → 0.23 → 0.24

Numbers say: light vs heavy: width 6.9 → 15.3 px, dark 0.85 → 0.85; the long stroke does not run out of paint.

## Brush Artist · Refs · #01 Henry Ward peach cloud — own sheet
own sheet 600 × 600 · Gouache · 44 px · 14.5 s

![Brush Artist · Refs · #01 Henry Ward peach cloud — own sheet](Brush-Artist-Refs-01-Henry-Ward-peach-cloud-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 14 % → 39 % | 40.5 px | 0.59 | 2.74 | 270 |
| stroke 2 | 24 % → 58 % | 79.5 px | 0.59 | 2.40 | 190 |
| stroke 3 | 28 % → 56 % | 81.3 px | 0.59 | 2.01 | 151 |
| stroke 4 | 30 % → 63 % | 99.7 px | 0.59 | 2.05 | 139 |
| stroke 5 | 30 % → 55 % | 86.0 px | 0.59 | 1.86 | 153 |
| stroke 6 | 30 % → 42 % | 91.1 px | 0.59 | 1.42 | 139 |
| stroke 7 | 16 % → 53 % | 38.9 px | 0.59 | 3.38 | 145 |
| stroke 8 | 18 % → 49 % | 44.8 px | 0.59 | 2.76 | 159 |
| stroke 9 | 21 % → 50 % | 54.2 px | 0.59 | 2.39 | 172 |
| stroke 10 | 23 % → 51 % | 61.9 px | 0.59 | 2.21 | 162 |
| stroke 11 | 25 % → 54 % | 72.0 px | 0.59 | 2.11 | 157 |
| stroke 12 | 29 % → 56 % | 88.0 px | 0.59 | 1.92 | 145 |
| stroke 13 | 37 % → 59 % | 108.0 px | 0.59 | 1.59 | 171 |
| stroke 14 | 40 % → 61 % | 113.8 px | 0.59 | 1.54 | 157 |
| stroke 15 | 53 % → 67 % | 156.4 px | 0.59 | 1.27 | 154 |
| stroke 16 | 54 % → 68 % | 164.9 px | 0.59 | 1.24 | 161 |
| stroke 17 | 55 % → 69 % | 155.8 px | 0.59 | 1.24 | 158 |
| stroke 18 | 57 % → 67 % | 164.8 px | 0.59 | 1.19 | 156 |
| stroke 19 | 58 % → 66 % | 163.9 px | 0.59 | 1.13 | 171 |
| stroke 20 | 58 % → 63 % | 167.5 px | 0.59 | 1.09 | 167 |
| stroke 21 | 58 % → 60 % | 168.2 px | 0.59 | 1.04 | 195 |
| stroke 22 | 59 % → 61 % | 173.1 px | 0.59 | 1.03 | 170 |
| stroke 23 | 59 % → 59 % | 167.7 px | 0.59 | 1.00 | 163 |
| stroke 24 | 63 % → 62 % | 187.3 px | 0.59 | 0.99 | 142 |

Numbers say: wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #02 Henry Ward cream strokes — own sheet
own sheet 600 × 600 · Gouache · 46 px · 9.2 s

![Brush Artist · Refs · #02 Henry Ward cream strokes — own sheet](Brush-Artist-Refs-02-Henry-Ward-cream-strokes-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 18 % → 32 % | 37.3 px | 0.70 | 1.77 | 333 |
| stroke 2 | 28 % → 37 % | 72.5 px | 0.70 | 1.34 | 225 |
| stroke 3 | 27 % → 44 % | 68.7 px | 0.71 | 1.64 | 208 |
| stroke 4 | 29 % → 41 % | 71.2 px | 0.71 | 1.42 | 218 |
| stroke 5 | 35 % → 45 % | 85.0 px | 0.71 | 1.29 | 211 |
| stroke 6 | 28 % → 39 % | 66.8 px | 0.70 | 1.42 | 299 |
| stroke 7 | 29 % → 27 % | 74.4 px | 0.70 | 0.92 | 242 |

Numbers say: wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #03 Henry Ward navy contours — own sheet
own sheet 600 × 600 · Heavy acrylic · 22 px · 3.0 s

![Brush Artist · Refs · #03 Henry Ward navy contours — own sheet](Brush-Artist-Refs-03-Henry-Ward-navy-contours-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 12 % → 18 % | 23.4 px | 0.69 | 1.57 | 152 |
| stroke 2 | 20 % → 23 % | 28.6 px | 0.69 | 1.15 | 100 |
| stroke 3 | 23 % → 23 % | 33.7 px | 0.69 | 1.01 | 132 |
| stroke 4 | 23 % → 21 % | 51.1 px | 0.69 | 0.92 | 147 |

Numbers say: wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #04 Henry Ward grey cloud — own sheet
own sheet 600 × 600 · Gouache · 50 px · 15.0 s

![Brush Artist · Refs · #04 Henry Ward grey cloud — own sheet](Brush-Artist-Refs-04-Henry-Ward-grey-cloud-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 14 % → 48 % | 42.2 px | 0.40 | 3.32 | 228 |
| stroke 2 | 19 % → 50 % | 53.3 px | 0.40 | 2.68 | 225 |
| stroke 3 | 27 % → 57 % | 75.3 px | 0.40 | 2.11 | 220 |
| stroke 4 | 30 % → 60 % | 88.0 px | 0.40 | 1.98 | 218 |
| stroke 5 | 36 % → 66 % | 110.1 px | 0.40 | 1.83 | 214 |
| stroke 6 | 40 % → 70 % | 129.7 px | 0.40 | 1.77 | 202 |
| stroke 7 | 46 % → 77 % | 134.2 px | 0.40 | 1.67 | 225 |
| stroke 8 | 45 % → 77 % | 133.7 px | 0.40 | 1.70 | 219 |
| stroke 9 | 45 % → 77 % | 133.8 px | 0.40 | 1.72 | 212 |
| stroke 10 | 46 % → 77 % | 148.0 px | 0.40 | 1.67 | 204 |
| stroke 11 | 46 % → 77 % | 130.7 px | 0.40 | 1.67 | 212 |
| stroke 12 | 47 % → 76 % | 141.7 px | 0.40 | 1.63 | 213 |
| stroke 13 | 46 % → 77 % | 131.3 px | 0.40 | 1.67 | 209 |
| stroke 14 | 47 % → 77 % | 139.7 px | 0.40 | 1.64 | 219 |
| stroke 15 | 46 % → 72 % | 133.2 px | 0.40 | 1.56 | 216 |
| stroke 16 | 47 % → 70 % | 143.4 px | 0.40 | 1.47 | 214 |
| stroke 17 | 45 % → 61 % | 130.9 px | 0.40 | 1.33 | 210 |
| stroke 18 | 45 % → 56 % | 149.2 px | 0.40 | 1.24 | 192 |
| stroke 19 | 46 % → 47 % | 136.3 px | 0.40 | 1.03 | 207 |
| stroke 20 | 47 % → 46 % | 148.0 px | 0.40 | 0.99 | 228 |

Numbers say: wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #05 Henry Ward green in rust loops — own sheet
own sheet 600 × 600 · Heavy acrylic · 20 px · 2.2 s

![Brush Artist · Refs · #05 Henry Ward green in rust loops — own sheet](Brush-Artist-Refs-05-Henry-Ward-green-in-rust-loops-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 12 % → 19 % | 21.2 px | 0.02 | 1.61 | 111 |
| stroke 2 | 12 % → 11 % | 23.7 px | 0.02 | 0.93 | 146 |
| stroke 3 | 23 % → 22 % | 41.7 px | 0.02 | 0.93 | 122 |

Numbers say: wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #06 Henry Ward scrubbed grey — own sheet
own sheet 600 × 600 · Gouache · 50 px · 16.9 s

![Brush Artist · Refs · #06 Henry Ward scrubbed grey — own sheet](Brush-Artist-Refs-06-Henry-Ward-scrubbed-grey-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 17 % → 54 % | 42.0 px | 0.40 | 3.16 | 208 |
| stroke 2 | 22 % → 56 % | 58.8 px | 0.40 | 2.55 | 218 |
| stroke 3 | 28 % → 61 % | 87.1 px | 0.40 | 2.13 | 211 |
| stroke 4 | 29 % → 61 % | 92.8 px | 0.40 | 2.06 | 201 |
| stroke 5 | 42 % → 75 % | 127.0 px | 0.40 | 1.78 | 208 |
| stroke 6 | 45 % → 76 % | 138.6 px | 0.40 | 1.67 | 229 |
| stroke 7 | 47 % → 77 % | 133.9 px | 0.40 | 1.64 | 275 |
| stroke 8 | 47 % → 77 % | 147.9 px | 0.40 | 1.65 | 251 |
| stroke 9 | 45 % → 77 % | 137.9 px | 0.40 | 1.71 | 216 |
| stroke 10 | 45 % → 77 % | 147.0 px | 0.40 | 1.70 | 200 |
| stroke 11 | 46 % → 77 % | 136.1 px | 0.40 | 1.66 | 210 |
| stroke 12 | 47 % → 77 % | 143.2 px | 0.40 | 1.64 | 214 |
| stroke 13 | 45 % → 77 % | 127.5 px | 0.40 | 1.71 | 216 |
| stroke 14 | 44 % → 76 % | 130.2 px | 0.40 | 1.72 | 217 |
| stroke 15 | 45 % → 77 % | 128.6 px | 0.40 | 1.71 | 220 |
| stroke 16 | 46 % → 77 % | 146.4 px | 0.40 | 1.68 | 202 |
| stroke 17 | 45 % → 70 % | 134.2 px | 0.40 | 1.55 | 220 |
| stroke 18 | 47 % → 67 % | 141.3 px | 0.40 | 1.44 | 281 |
| stroke 19 | 45 % → 61 % | 134.0 px | 0.40 | 1.36 | 293 |
| stroke 20 | 45 % → 59 % | 141.3 px | 0.40 | 1.30 | 294 |
| stroke 21 | 45 % → 50 % | 131.4 px | 0.40 | 1.11 | 219 |
| stroke 22 | 46 % → 45 % | 151.0 px | 0.40 | 0.99 | 200 |

Numbers say: wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #07 Henry Ward blue L + black zigzag — own sheet
own sheet 600 × 600 · Heavy acrylic · 34 px · 2.0 s

![Brush Artist · Refs · #07 Henry Ward blue L + black zigzag — own sheet](Brush-Artist-Refs-07-Henry-Ward-blue-L-black-zigzag-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 16 % → 17 % | 36.5 px | 0.59 | 1.11 | 111 |
| stroke 2 | 18 % → 17 % | 44.0 px | 0.59 | 0.93 | 83 |

## Brush Artist · Refs · #08 Henry Ward olive bands — own sheet
own sheet 600 × 600 · Gouache · 34 px · 5.6 s

![Brush Artist · Refs · #08 Henry Ward olive bands — own sheet](Brush-Artist-Refs-08-Henry-Ward-olive-bands-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 9 % → 7 % | 17.9 px | 0.59 | 0.82 | 157 |
| stroke 2 | 15 % → 9 % | 32.8 px | 0.59 | 0.63 | 156 |
| stroke 3 | 13 % → 13 % | 26.4 px | 0.59 | 1.02 | 161 |
| stroke 4 | 15 % → 11 % | 31.5 px | 0.59 | 0.78 | 166 |
| stroke 5 | 20 % → 14 % | 40.1 px | 0.59 | 0.71 | 164 |
| stroke 6 | 13 % → 7 % | 24.2 px | 0.59 | 0.52 | 155 |

## Brush Artist · Refs · #09 Henry Ward white loops — own sheet
own sheet 600 × 600 · Gouache · 46 px · 9.4 s

![Brush Artist · Refs · #09 Henry Ward white loops — own sheet](Brush-Artist-Refs-09-Henry-Ward-white-loops-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 23 % → 4 % | 12.2 px | 0.07 | 0.17 | 1335 |
| stroke 2 | 26 % → 4 % | 26.2 px | 0.07 | 0.14 | 1640 |
| stroke 3 | 34 % → 4 % | 31.4 px | 0.07 | 0.12 | 953 |
| stroke 4 | 3 % → 1 % | 6.1 px | 0.06 | 0.22 | 232 |
| stroke 5 | 4 % → 2 % | 12.1 px | 0.08 | 0.38 | 163 |
| stroke 6 | 7 % → 4 % | 18.2 px | 0.07 | 0.65 | 163 |
| stroke 7 | 14 % → 4 % | 36.3 px | 0.07 | 0.31 | 176 |
| stroke 8 | 2 % → 0 % | 3.0 px | 0.05 | 0.06 | 155 |

## Brush Artist · Refs · #10 Henry Ward maroon loops — own sheet
own sheet 600 × 600 · Heavy acrylic · 30 px · 3.6 s

![Brush Artist · Refs · #10 Henry Ward maroon loops — own sheet](Brush-Artist-Refs-10-Henry-Ward-maroon-loops-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 12 % → 28 % | 29.0 px | 0.72 | 2.41 | 358 |
| stroke 2 | 22 % → 41 % | 49.1 px | 0.72 | 1.87 | 208 |
| stroke 3 | 29 % → 37 % | 59.1 px | 0.72 | 1.27 | 256 |
| stroke 4 | 42 % → 41 % | 95.0 px | 0.72 | 0.96 | 177 |
| stroke 5 | 35 % → 32 % | 87.1 px | 0.72 | 0.93 | 148 |

Numbers say: wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #11 Henry Ward purple spun balls — own sheet
own sheet 600 × 600 · Heavy acrylic · 36 px · 2.7 s

![Brush Artist · Refs · #11 Henry Ward purple spun balls — own sheet](Brush-Artist-Refs-11-Henry-Ward-purple-spun-balls-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 24 % → 35 % | 26.9 px | 0.68 | 1.44 | 232 |
| stroke 2 | 35 % → 47 % | 38.6 px | 0.68 | 1.34 | 228 |
| stroke 3 | 36 % → 35 % | 39.8 px | 0.68 | 0.97 | 223 |

## Brush Artist · Refs · #12 Henry Ward black-olive cage — own sheet
own sheet 600 × 600 · Gouache · 28 px · 5.4 s

![Brush Artist · Refs · #12 Henry Ward black-olive cage — own sheet](Brush-Artist-Refs-12-Henry-Ward-black-olive-cage-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 7 % → 12 % | 13.4 px | 0.60 | 1.68 | 201 |
| stroke 2 | 7 % → 12 % | 16.3 px | 0.60 | 1.80 | 173 |
| stroke 3 | 15 % → 16 % | 24.2 px | 0.60 | 1.03 | 298 |
| stroke 4 | 16 % → 15 % | 32.2 px | 0.60 | 0.92 | 169 |
| stroke 5 | 16 % → 11 % | 29.0 px | 0.60 | 0.68 | 165 |
| stroke 6 | 25 % → 16 % | 48.3 px | 0.60 | 0.65 | 220 |

Numbers say: wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #13 Henry Ward blue streaky form — own sheet
own sheet 600 × 600 · Gouache · 50 px · 13.1 s

![Brush Artist · Refs · #13 Henry Ward blue streaky form — own sheet](Brush-Artist-Refs-13-Henry-Ward-blue-streaky-form-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 14 % → 8 % | 42.7 px | 0.04 | 0.56 | 209 |
| stroke 2 | 20 % → 7 % | 61.3 px | 0.04 | 0.36 | 285 |
| stroke 3 | 31 % → 8 % | 88.7 px | 0.04 | 0.25 | 279 |
| stroke 4 | 31 % → 7 % | 99.6 px | 0.04 | 0.23 | 263 |
| stroke 5 | 45 % → 8 % | 130.2 px | 0.04 | 0.18 | 303 |
| stroke 6 | 45 % → 9 % | 129.6 px | 0.04 | 0.20 | 324 |
| stroke 7 | 46 % → 10 % | 136.7 px | 0.04 | 0.22 | 214 |
| stroke 8 | 47 % → 8 % | 143.3 px | 0.03 | 0.18 | 211 |
| stroke 9 | 46 % → 7 % | 142.0 px | 0.03 | 0.16 | 205 |
| stroke 10 | 46 % → 7 % | 152.6 px | 0.03 | 0.16 | 197 |
| stroke 11 | 44 % → 5 % | 136.4 px | 0.03 | 0.11 | 202 |
| stroke 12 | 45 % → 6 % | 135.8 px | 0.03 | 0.14 | 230 |
| stroke 13 | 45 % → 7 % | 138.8 px | 0.04 | 0.17 | 197 |
| stroke 14 | 43 % → 7 % | 129.4 px | 0.04 | 0.16 | 215 |
| stroke 15 | 44 % → 7 % | 125.8 px | 0.04 | 0.17 | 223 |
| stroke 16 | 46 % → 7 % | 137.2 px | 0.04 | 0.16 | 210 |
| stroke 17 | 55 % → 4 % | 137.1 px | 0.04 | 0.08 | 209 |
| stroke 18 | 58 % → 4 % | 140.1 px | 0.04 | 0.08 | 220 |
| stroke 19 | 64 % → 5 % | 130.9 px | 0.04 | 0.08 | 211 |
| stroke 20 | 72 % → 5 % | 137.6 px | 0.04 | 0.08 | 238 |
| stroke 21 | 1 % → 0 % | 2.9 px | 0.04 | 0.02 | 138 |
| stroke 22 | 12 % → 7 % | 34.1 px | 0.04 | 0.61 | 193 |
| stroke 23 | 23 % → 8 % | 70.4 px | 0.04 | 0.35 | 167 |
| stroke 24 | 14 % → 5 % | 38.0 px | 0.03 | 0.35 | 189 |
| stroke 25 | 18 % → 6 % | 46.1 px | 0.04 | 0.31 | 178 |

## Brush Artist · Refs · #14 Henry Ward olive totem — own sheet
own sheet 600 × 600 · Heavy acrylic · 48 px · 6.9 s

![Brush Artist · Refs · #14 Henry Ward olive totem — own sheet](Brush-Artist-Refs-14-Henry-Ward-olive-totem-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 19 % → 49 % | 48.9 px | 0.38 | 2.60 | 179 |
| stroke 2 | 22 % → 53 % | 67.8 px | 0.38 | 2.44 | 136 |
| stroke 3 | 31 % → 54 % | 105.7 px | 0.38 | 1.76 | 162 |
| stroke 4 | 32 % → 57 % | 120.2 px | 0.38 | 1.77 | 197 |
| stroke 5 | 41 % → 66 % | 143.0 px | 0.38 | 1.60 | 161 |
| stroke 6 | 41 % → 67 % | 158.1 px | 0.38 | 1.65 | 162 |
| stroke 7 | 39 % → 63 % | 130.7 px | 0.38 | 1.63 | 122 |
| stroke 8 | 39 % → 65 % | 147.7 px | 0.38 | 1.68 | 121 |
| stroke 9 | 39 % → 64 % | 134.6 px | 0.38 | 1.66 | 118 |
| stroke 10 | 39 % → 63 % | 143.8 px | 0.37 | 1.63 | 130 |
| stroke 11 | 41 % → 66 % | 147.3 px | 0.38 | 1.61 | 119 |
| stroke 12 | 39 % → 67 % | 148.5 px | 0.38 | 1.70 | 120 |
| stroke 13 | 40 % → 69 % | 141.8 px | 0.38 | 1.71 | 117 |
| stroke 14 | 38 % → 64 % | 139.1 px | 0.38 | 1.68 | 137 |
| stroke 15 | 41 % → 68 % | 141.2 px | 0.38 | 1.64 | 118 |
| stroke 16 | 40 % → 66 % | 143.5 px | 0.38 | 1.66 | 131 |
| stroke 17 | 39 % → 64 % | 131.8 px | 0.38 | 1.64 | 131 |
| stroke 18 | 42 % → 69 % | 160.9 px | 0.38 | 1.64 | 131 |
| stroke 19 | 41 % → 63 % | 143.3 px | 0.37 | 1.53 | 122 |
| stroke 20 | 42 % → 57 % | 149.6 px | 0.37 | 1.35 | 134 |
| stroke 21 | 48 % → 57 % | 142.8 px | 0.37 | 1.19 | 120 |
| stroke 22 | 56 % → 56 % | 152.7 px | 0.37 | 0.99 | 126 |

Numbers say: wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #15 Ultramarine brush script — own sheet
own sheet 600 × 600 · Ink · 4 px · 8.5 s

![Brush Artist · Refs · #15 Ultramarine brush script — own sheet](Brush-Artist-Refs-15-Ultramarine-brush-script-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 40 % → 42 % | 8.9 px | 0.66 | 1.05 | 56 |
| stroke 2 | 40 % → 42 % | 8.9 px | 0.66 | 1.06 | 50 |
| stroke 3 | 40 % → 42 % | 9.5 px | 0.74 | 1.06 | 26 |
| stroke 4 | 42 % → 45 % | 10.1 px | 0.74 | 1.08 | 16 |
| stroke 5 | 44 % → 48 % | 9.7 px | 0.73 | 1.08 | 25 |
| stroke 6 | 42 % → 44 % | 9.5 px | 0.65 | 1.05 | 51 |
| stroke 7 | 43 % → 47 % | 9.2 px | 0.72 | 1.08 | 30 |
| stroke 8 | 38 % → 41 % | 9.3 px | 0.68 | 1.05 | 43 |
| stroke 9 | 40 % → 42 % | 9.2 px | 0.69 | 1.06 | 44 |
| stroke 10 | 36 % → 38 % | 9.9 px | 0.68 | 1.05 | 45 |
| stroke 11 | 42 % → 45 % | 9.6 px | 0.70 | 1.06 | 42 |
| stroke 12 | 39 % → 41 % | 9.4 px | 0.66 | 1.05 | 46 |
| stroke 13 | 45 % → 48 % | 10.2 px | 0.71 | 1.06 | 29 |
| stroke 14 | 38 % → 41 % | 9.9 px | 0.73 | 1.07 | 23 |
| stroke 15 | 37 % → 39 % | 9.1 px | 0.69 | 1.06 | 44 |
| stroke 16 | 42 % → 45 % | 9.4 px | 0.72 | 1.06 | 30 |
| stroke 17 | 41 % → 44 % | 7.1 px | 0.71 | 1.08 | 42 |
| stroke 18 | 43 % → 45 % | 9.2 px | 0.73 | 1.06 | 25 |
| stroke 19 | 39 % → 41 % | 8.9 px | 0.66 | 1.05 | 56 |
| stroke 20 | 41 % → 43 % | 9.4 px | 0.71 | 1.06 | 34 |
| stroke 21 | 40 % → 43 % | 9.9 px | 0.70 | 1.06 | 36 |
| stroke 22 | 42 % → 44 % | 8.5 px | 0.65 | 1.05 | 55 |
| stroke 23 | 40 % → 43 % | 10.1 px | 0.73 | 1.07 | 22 |
| stroke 24 | 38 % → 41 % | 8.8 px | 0.73 | 1.07 | 31 |
| stroke 25 | 41 % → 43 % | 9.8 px | 0.72 | 1.07 | 29 |
| stroke 26 | 46 % → 49 % | 9.3 px | 0.68 | 1.05 | 46 |
| stroke 27 | 43 % → 45 % | 8.8 px | 0.63 | 1.05 | 64 |
| stroke 28 | 44 % → 46 % | 9.1 px | 0.70 | 1.06 | 40 |
| stroke 29 | 36 % → 39 % | 10.6 px | 0.72 | 1.08 | 25 |
| stroke 30 | 39 % → 41 % | 8.7 px | 0.71 | 1.04 | 40 |
| stroke 31 | 43 % → 46 % | 10.3 px | 0.75 | 1.07 | 19 |
| stroke 32 | 42 % → 46 % | 9.5 px | 0.73 | 1.09 | 27 |
| stroke 33 | 35 % → 38 % | 10.9 px | 0.72 | 1.08 | 24 |
| stroke 34 | 40 % → 43 % | 9.8 px | 0.73 | 1.08 | 24 |
| stroke 35 | 36 % → 37 % | 9.4 px | 0.65 | 1.05 | 49 |

## Brush Artist · Refs · #18 Blue oil-stick scribbles — own sheet
own sheet 600 × 600 · Pastel · 10 px · 3.0 s

![Brush Artist · Refs · #18 Blue oil-stick scribbles — own sheet](Brush-Artist-Refs-18-Blue-oil-stick-scribbles-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 15 % → 31 % | 3.8 px | 0.49 | 2.11 | 147 |
| stroke 2 | 13 % → 37 % | 3.6 px | 0.49 | 2.73 | 172 |
| stroke 3 | 16 % → 26 % | 5.8 px | 0.49 | 1.66 | 186 |
| stroke 4 | 15 % → 29 % | 8.0 px | 0.49 | 1.88 | 175 |
| stroke 5 | 29 % → 34 % | 8.4 px | 0.49 | 1.19 | 145 |
| stroke 6 | 25 % → 26 % | 9.4 px | 0.49 | 1.02 | 129 |
| stroke 7 | 26 % → 32 % | 8.3 px | 0.49 | 1.24 | 156 |
| stroke 8 | 30 % → 30 % | 17.0 px | 0.49 | 1.00 | 182 |

Numbers say: wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #20 Orange-red crayon scribble — own sheet
own sheet 600 × 600 · Pastel · 14 px · 3.1 s

![Brush Artist · Refs · #20 Orange-red crayon scribble — own sheet](Brush-Artist-Refs-20-Orange-red-crayon-scribble-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 8 % → 18 % | 5.5 px | 0.59 | 2.46 | 192 |
| stroke 2 | 9 % → 23 % | 6.8 px | 0.59 | 2.48 | 164 |
| stroke 3 | 13 % → 21 % | 8.5 px | 0.59 | 1.64 | 155 |
| stroke 4 | 24 % → 32 % | 8.9 px | 0.59 | 1.34 | 176 |
| stroke 5 | 27 % → 27 % | 7.7 px | 0.59 | 1.00 | 163 |
| stroke 6 | 22 % → 22 % | 16.8 px | 0.59 | 1.00 | 183 |

Numbers say: wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #21 Gritty black contours — own sheet
own sheet 600 × 600 · Gouache · 12 px · 4.1 s

![Brush Artist · Refs · #21 Gritty black contours — own sheet](Brush-Artist-Refs-21-Gritty-black-contours-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 4 % → 5 % | 4.7 px | 0.37 | 1.13 | 207 |
| stroke 2 | 4 % → 3 % | 7.3 px | 0.37 | 0.60 | 226 |
| stroke 3 | 7 % → 4 % | 6.2 px | 0.37 | 0.56 | 155 |
| stroke 4 | 9 % → 4 % | 10.7 px | 0.37 | 0.51 | 146 |
| stroke 5 | 10 % → 4 % | 12.7 px | 0.37 | 0.42 | 87 |

## Brush Artist · Refs · #22 Bold black brush poster — own sheet
own sheet 600 × 600 · Ink · 20 px · 4.8 s

![Brush Artist · Refs · #22 Bold black brush poster — own sheet](Brush-Artist-Refs-22-Bold-black-brush-poster-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 22 % → 27 % | 36.4 px | 0.94 | 1.20 | 131 |
| stroke 2 | 27 % → 37 % | 41.5 px | 0.95 | 1.36 | 24 |
| stroke 3 | 28 % → 28 % | 43.6 px | 0.95 | 1.00 | 44 |
| stroke 4 | 27 % → 39 % | 53.8 px | 0.94 | 1.42 | 66 |
| stroke 5 | 25 % → 25 % | 43.0 px | 0.94 | 1.00 | 78 |

## Brush Artist · Refs · #23 Dry white on orange + black line — own sheet
own sheet 600 × 600 · Gouache · 50 px · 7.8 s

![Brush Artist · Refs · #23 Dry white on orange + black line — own sheet](Brush-Artist-Refs-23-Dry-white-on-orange-black-line-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 5 % → 10 % | 18.7 px | 0.42 | 1.89 | 171 |
| stroke 2 | 7 % → 9 % | 24.3 px | 0.42 | 1.35 | 156 |
| stroke 3 | 10 % → 10 % | 39.0 px | 0.42 | 0.92 | 144 |
| stroke 4 | 12 % → 11 % | 45.8 px | 0.42 | 0.95 | 148 |
| stroke 5 | 17 % → 14 % | 60.0 px | 0.42 | 0.82 | 143 |
| stroke 6 | 17 % → 15 % | 70.6 px | 0.42 | 0.86 | 138 |
| stroke 7 | 14 % → 14 % | 52.6 px | 0.41 | 1.00 | 140 |
| stroke 8 | 14 % → 13 % | 55.2 px | 0.41 | 0.91 | 152 |
| stroke 9 | 15 % → 14 % | 54.3 px | 0.41 | 0.93 | 143 |
| stroke 10 | 14 % → 14 % | 56.6 px | 0.41 | 0.97 | 140 |
| stroke 11 | 16 % → 15 % | 60.6 px | 0.41 | 0.92 | 150 |
| stroke 12 | 16 % → 15 % | 63.4 px | 0.41 | 0.94 | 152 |
| stroke 13 | 17 % → 16 % | 61.2 px | 0.41 | 0.97 | 144 |
| stroke 14 | 16 % → 16 % | 63.9 px | 0.41 | 0.97 | 152 |
| stroke 15 | 16 % → 14 % | 59.9 px | 0.41 | 0.87 | 140 |
| stroke 16 | 15 % → 12 % | 61.4 px | 0.41 | 0.78 | 145 |
| stroke 17 | 16 % → 11 % | 56.7 px | 0.41 | 0.68 | 145 |
| stroke 18 | 19 % → 11 % | 69.3 px | 0.41 | 0.60 | 128 |

Numbers say: wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #24 Picasso flat oil — own sheet
own sheet 600 × 600 · Oil · 34 px · 6.2 s

![Brush Artist · Refs · #24 Picasso flat oil — own sheet](Brush-Artist-Refs-24-Picasso-flat-oil-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 17 % → 46 % | 35.6 px | 0.23 | 2.73 | 121 |
| stroke 2 | 21 % → 49 % | 48.5 px | 0.24 | 2.38 | 139 |
| stroke 3 | 29 % → 60 % | 64.2 px | 0.23 | 2.05 | 133 |
| stroke 4 | 38 % → 66 % | 85.1 px | 0.23 | 1.75 | 138 |
| stroke 5 | 44 % → 72 % | 97.2 px | 0.23 | 1.63 | 127 |
| stroke 6 | 45 % → 67 % | 104.5 px | 0.23 | 1.50 | 130 |
| stroke 7 | 46 % → 68 % | 97.4 px | 0.23 | 1.46 | 122 |
| stroke 8 | 45 % → 68 % | 109.1 px | 0.23 | 1.51 | 139 |
| stroke 9 | 38 % → 64 % | 83.4 px | 0.23 | 1.69 | 127 |
| stroke 10 | 40 % → 63 % | 95.6 px | 0.23 | 1.58 | 137 |
| stroke 11 | 38 % → 62 % | 81.6 px | 0.23 | 1.62 | 134 |
| stroke 12 | 40 % → 63 % | 94.7 px | 0.23 | 1.60 | 136 |
| stroke 13 | 40 % → 70 % | 87.1 px | 0.23 | 1.76 | 134 |
| stroke 14 | 41 % → 71 % | 92.4 px | 0.23 | 1.74 | 141 |
| stroke 15 | 41 % → 64 % | 86.1 px | 0.23 | 1.58 | 133 |
| stroke 16 | 39 % → 56 % | 91.3 px | 0.23 | 1.43 | 140 |
| stroke 17 | 45 % → 50 % | 93.3 px | 0.23 | 1.12 | 127 |
| stroke 18 | 44 % → 44 % | 106.7 px | 0.23 | 1.00 | 132 |

Numbers say: wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #25 Yellow heavy flat stroke — own sheet
own sheet 600 × 600 · Heavy acrylic · 110 px · 2.8 s

![Brush Artist · Refs · #25 Yellow heavy flat stroke — own sheet](Brush-Artist-Refs-25-Yellow-heavy-flat-stroke-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 19 % → 19 % | 110.5 px | 0.18 | 0.98 | 621 |

## Brush Artist · Refs · #27 Orange impasto swatch — own sheet
own sheet 600 × 600 · Heavy acrylic · 60 px · 4.3 s

![Brush Artist · Refs · #27 Orange impasto swatch — own sheet](Brush-Artist-Refs-27-Orange-impasto-swatch-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 9 % → 29 % | 68.9 px | 0.35 | 3.19 | 73 |
| stroke 2 | 8 % → 41 % | 72.3 px | 0.34 | 4.94 | 48 |
| stroke 3 | 29 % → 45 % | 285.3 px | 0.35 | 1.52 | 41 |
| stroke 4 | 11 % → 15 % | 77.4 px | 0.34 | 1.39 | 62 |
| stroke 5 | 17 % → 33 % | 63.6 px | 0.33 | 1.90 | 76 |
| stroke 6 | 20 % → 40 % | 166.9 px | 0.34 | 1.96 | 60 |
| stroke 7 | 9 % → 18 % | 80.4 px | 0.34 | 2.03 | 45 |
| stroke 8 | 38 % → 44 % | 387.7 px | 0.34 | 1.16 | 41 |
| stroke 9 | 40 % → 40 % | 195.9 px | 0.34 | 1.00 | 68 |
| stroke 10 | 36 % → 38 % | 330.2 px | 0.33 | 1.03 | 48 |

Numbers say: wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #28 Miles Davis black lines — own sheet
own sheet 600 × 600 · Ink · 22 px · 6.1 s

![Brush Artist · Refs · #28 Miles Davis black lines — own sheet](Brush-Artist-Refs-28-Miles-Davis-black-lines-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 22 % → 32 % | 36.6 px | 0.88 | 1.42 | 165 |
| stroke 2 | 28 % → 49 % | 38.3 px | 0.88 | 1.73 | 122 |
| stroke 3 | 39 % → 44 % | 75.1 px | 0.88 | 1.12 | 100 |
| stroke 4 | 42 % → 48 % | 83.7 px | 0.88 | 1.15 | 162 |
| stroke 5 | 55 % → 55 % | 109.9 px | 0.88 | 1.00 | 119 |

Numbers say: wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #29 Shrigley magenta asterisk — own sheet
own sheet 600 × 600 · Watercolor · 70 px · 6.0 s

![Brush Artist · Refs · #29 Shrigley magenta asterisk — own sheet](Brush-Artist-Refs-29-Shrigley-magenta-asterisk-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 13 % → 37 % | 46.6 px | 0.72 | 2.85 | 161 |
| stroke 2 | 12 % → 12 % | 87.1 px | 0.71 | 1.00 | 172 |
| stroke 3 | 28 % → 37 % | 100.9 px | 0.72 | 1.31 | 255 |
| stroke 4 | 23 % → 23 % | 163.9 px | 0.71 | 1.02 | 252 |

Numbers say: wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #30 Red gouache face patch — own sheet
own sheet 600 × 600 · Gouache · 60 px · 10.6 s

![Brush Artist · Refs · #30 Red gouache face patch — own sheet](Brush-Artist-Refs-30-Red-gouache-face-patch-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 12 % → 37 % | 51.5 px | 0.53 | 3.22 | 175 |
| stroke 2 | 15 % → 40 % | 74.6 px | 0.53 | 2.72 | 196 |
| stroke 3 | 24 % → 50 % | 116.0 px | 0.53 | 2.06 | 190 |
| stroke 4 | 27 % → 51 % | 134.1 px | 0.53 | 1.93 | 183 |
| stroke 5 | 34 % → 60 % | 159.9 px | 0.53 | 1.77 | 152 |
| stroke 6 | 35 % → 61 % | 178.3 px | 0.53 | 1.76 | 154 |
| stroke 7 | 34 % → 59 % | 160.9 px | 0.54 | 1.73 | 152 |
| stroke 8 | 34 % → 56 % | 162.5 px | 0.53 | 1.65 | 165 |
| stroke 9 | 36 % → 60 % | 173.1 px | 0.53 | 1.66 | 146 |
| stroke 10 | 38 % → 62 % | 196.8 px | 0.53 | 1.63 | 140 |
| stroke 11 | 37 % → 61 % | 182.5 px | 0.53 | 1.66 | 142 |
| stroke 12 | 36 % → 58 % | 178.3 px | 0.53 | 1.62 | 153 |
| stroke 13 | 33 % → 46 % | 156.5 px | 0.53 | 1.39 | 147 |
| stroke 14 | 33 % → 41 % | 157.7 px | 0.53 | 1.25 | 174 |
| stroke 15 | 33 % → 37 % | 153.4 px | 0.53 | 1.12 | 164 |
| stroke 16 | 39 % → 39 % | 184.9 px | 0.53 | 0.99 | 138 |

Numbers say: wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #31 Warhol blotted line — own sheet
own sheet 600 × 600 · Ink · 6 px · 4.4 s

![Brush Artist · Refs · #31 Warhol blotted line — own sheet](Brush-Artist-Refs-31-Warhol-blotted-line-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 21 % → 42 % | 15.8 px | 0.82 | 1.98 | 81 |
| stroke 2 | 17 % → 23 % | 15.9 px | 0.82 | 1.34 | 72 |
| stroke 3 | 24 % → 25 % | 25.1 px | 0.81 | 1.02 | 78 |
| stroke 4 | 31 % → 40 % | 31.9 px | 0.82 | 1.28 | 51 |
| stroke 5 | 35 % → 44 % | 36.4 px | 0.82 | 1.23 | 71 |
| stroke 6 | 32 % → 33 % | 26.7 px | 0.81 | 1.03 | 69 |

Numbers say: wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #32 Thick orange swipes — own sheet
own sheet 600 × 600 · Heavy acrylic · 90 px · 3.4 s

![Brush Artist · Refs · #32 Thick orange swipes — own sheet](Brush-Artist-Refs-32-Thick-orange-swipes-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 15 % → 29 % | 91.7 px | 0.03 | 1.91 | 294 |
| stroke 2 | 28 % → 40 % | 188.8 px | 0.03 | 1.44 | 301 |
| stroke 3 | 30 % → 29 % | 190.2 px | 0.03 | 0.98 | 282 |

Numbers say: wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #33 Red wet-in-wet band — own sheet
own sheet 600 × 600 · Watercolor · 80 px · 8.7 s

![Brush Artist · Refs · #33 Red wet-in-wet band — own sheet](Brush-Artist-Refs-33-Red-wet-in-wet-band-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 23 % → 57 % | 88.2 px | 0.61 | 2.46 | 329 |
| stroke 2 | 30 % → 52 % | 243.9 px | 0.61 | 1.73 | 88 |
| stroke 3 | 37 % → 54 % | 356.6 px | 0.61 | 1.47 | 90 |
| stroke 4 | 42 % → 61 % | 412.6 px | 0.62 | 1.43 | 84 |
| stroke 5 | 42 % → 55 % | 354.2 px | 0.61 | 1.33 | 100 |
| stroke 6 | 42 % → 47 % | 321.5 px | 0.60 | 1.11 | 102 |

Numbers say: wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #34 Magenta oil patches — own sheet
own sheet 600 × 600 · Oil · 60 px · 4.7 s

![Brush Artist · Refs · #34 Magenta oil patches — own sheet](Brush-Artist-Refs-34-Magenta-oil-patches-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 10 % → 46 % | 68.9 px | 0.13 | 4.68 | 86 |
| stroke 2 | 11 % → 32 % | 71.2 px | 0.13 | 3.02 | 72 |
| stroke 3 | 9 % → 40 % | 71.5 px | 0.13 | 4.71 | 68 |
| stroke 4 | 18 % → 25 % | 149.6 px | 0.13 | 1.37 | 57 |
| stroke 5 | 27 % → 39 % | 145.1 px | 0.12 | 1.43 | 89 |
| stroke 6 | 22 % → 41 % | 187.6 px | 0.13 | 1.86 | 60 |
| stroke 7 | 34 % → 40 % | 268.4 px | 0.13 | 1.18 | 72 |
| stroke 8 | 36 % → 43 % | 256.5 px | 0.13 | 1.19 | 85 |
| stroke 9 | 26 % → 28 % | 170.2 px | 0.13 | 1.08 | 89 |
| stroke 10 | 31 % → 31 % | 275.9 px | 0.13 | 1.00 | 63 |
| stroke 11 | 40 % → 40 % | 359.9 px | 0.13 | 1.00 | 59 |
| stroke 12 | 29 % → 29 % | 205.9 px | 0.13 | 1.00 | 67 |

Numbers say: wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #35 Red band with runs — own sheet
own sheet 600 × 600 · Watercolor · 70 px · 5.9 s

![Brush Artist · Refs · #35 Red band with runs — own sheet](Brush-Artist-Refs-35-Red-band-with-runs-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 21 % → 38 % | 77.5 px | 0.46 | 1.84 | 287 |

Numbers say: wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #36 Magenta letters flat brush — own sheet
own sheet 600 × 600 · Gouache · 36 px · 10.1 s

![Brush Artist · Refs · #36 Magenta letters flat brush — own sheet](Brush-Artist-Refs-36-Magenta-letters-flat-brush-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 20 % → 39 % | 59.1 px | 0.50 | 1.95 | 45 |
| stroke 2 | 20 % → 32 % | 46.7 px | 0.50 | 1.59 | 41 |
| stroke 3 | 29 % → 54 % | 86.9 px | 0.50 | 1.86 | 39 |
| stroke 4 | 26 % → 44 % | 51.3 px | 0.50 | 1.67 | 132 |
| stroke 5 | 33 % → 55 % | 96.2 px | 0.50 | 1.67 | 69 |
| stroke 6 | 42 % → 56 % | 242.7 px | 0.50 | 1.33 | 15 |
| stroke 7 | 30 % → 44 % | 56.8 px | 0.50 | 1.45 | 107 |
| stroke 8 | 31 % → 53 % | 98.5 px | 0.50 | 1.68 | 62 |
| stroke 9 | 38 % → 51 % | 158.3 px | 0.50 | 1.33 | 24 |
| stroke 10 | 37 % → 64 % | 106.7 px | 0.50 | 1.72 | 69 |
| stroke 11 | 39 % → 62 % | 225.8 px | 0.50 | 1.58 | 15 |
| stroke 12 | 43 % → 56 % | 81.9 px | 0.50 | 1.29 | 107 |
| stroke 13 | 33 % → 46 % | 117.7 px | 0.50 | 1.43 | 30 |
| stroke 14 | 35 % → 52 % | 134.5 px | 0.50 | 1.47 | 29 |
| stroke 15 | 38 % → 56 % | 108.6 px | 0.50 | 1.49 | 71 |
| stroke 16 | 41 % → 50 % | 232.0 px | 0.50 | 1.23 | 15 |
| stroke 17 | 44 % → 52 % | 81.7 px | 0.50 | 1.19 | 106 |
| stroke 18 | 27 % → 36 % | 97.6 px | 0.50 | 1.35 | 30 |
| stroke 19 | 40 % → 39 % | 117.2 px | 0.50 | 0.96 | 28 |
| stroke 20 | 45 % → 45 % | 132.3 px | 0.50 | 0.99 | 29 |
| stroke 21 | 41 % → 39 % | 78.7 px | 0.50 | 0.96 | 81 |

Numbers say: wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #37 Oil still life dabs — own sheet
own sheet 600 × 600 · Oil · 40 px · 3.8 s

![Brush Artist · Refs · #37 Oil still life dabs — own sheet](Brush-Artist-Refs-37-Oil-still-life-dabs-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 8 % → 8 % | 50.5 px | 0.39 | 1.01 | 30 |
| stroke 2 | 7 % → 30 % | 52.7 px | 0.39 | 4.05 | 22 |
| stroke 3 | 14 % → 39 % | 109.5 px | 0.39 | 2.81 | 19 |
| stroke 4 | 10 % → 10 % | 47.7 px | 0.39 | 1.01 | 37 |
| stroke 5 | 7 % → 13 % | 51.7 px | 0.39 | 1.78 | 21 |
| stroke 6 | 14 % → 33 % | 90.8 px | 0.39 | 2.32 | 38 |
| stroke 7 | 13 % → 29 % | 144.0 px | 0.39 | 2.16 | 13 |
| stroke 8 | 11 % → 18 % | 117.7 px | 0.39 | 1.62 | 16 |
| stroke 9 | 15 % → 17 % | 79.1 px | 0.38 | 1.09 | 36 |
| stroke 10 | 23 % → 29 % | 117.3 px | 0.38 | 1.28 | 37 |
| stroke 11 | 27 % → 33 % | 223.3 px | 0.39 | 1.23 | 22 |
| stroke 12 | 23 % → 25 % | 253.7 px | 0.39 | 1.07 | 13 |
| stroke 13 | 19 % → 19 % | 189.1 px | 0.40 | 1.01 | 14 |
| stroke 14 | 20 % → 20 % | 163.8 px | 0.39 | 1.01 | 18 |

Numbers say: wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #38 Sanguine drawing — own sheet
own sheet 600 × 600 · Pastel · 6 px · 2.1 s

![Brush Artist · Refs · #38 Sanguine drawing — own sheet](Brush-Artist-Refs-38-Sanguine-drawing-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 3 % → 14 % | 2.9 px | 0.57 | 5.29 | 7 |
| stroke 2 | 3 % → 7 % | 2.9 px | 0.57 | 2.89 | 6 |
| stroke 3 | 3 % → 9 % | 2.9 px | 0.57 | 3.40 | 6 |
| stroke 4 | 2 % → 17 % | 2.7 px | 0.57 | 7.20 | 6 |
| stroke 5 | 2 % → 7 % | 2.7 px | 0.57 | 3.03 | 6 |
| stroke 6 | 3 % → 19 % | 3.4 px | 0.57 | 6.31 | 8 |
| stroke 7 | 5 % → 14 % | 5.2 px | 0.57 | 3.07 | 6 |
| stroke 8 | 4 % → 16 % | 4.7 px | 0.57 | 3.79 | 6 |
| stroke 9 | 3 % → 7 % | 2.9 px | 0.57 | 2.66 | 6 |
| stroke 10 | 4 % → 16 % | 4.7 px | 0.57 | 3.83 | 6 |
| stroke 11 | 3 % → 4 % | 2.9 px | 0.57 | 1.61 | 6 |
| stroke 12 | 4 % → 15 % | 4.8 px | 0.57 | 3.58 | 6 |
| stroke 13 | 8 % → 17 % | 8.9 px | 0.57 | 2.23 | 8 |
| stroke 14 | 4 % → 14 % | 4.9 px | 0.57 | 3.19 | 6 |
| stroke 15 | 9 % → 18 % | 10.7 px | 0.57 | 1.86 | 6 |
| stroke 16 | 6 % → 16 % | 6.6 px | 0.57 | 2.71 | 6 |
| stroke 17 | 4 % → 9 % | 4.4 px | 0.57 | 2.25 | 6 |
| stroke 18 | 3 % → 5 % | 2.9 px | 0.57 | 1.85 | 6 |
| stroke 19 | 6 % → 16 % | 6.9 px | 0.57 | 2.68 | 6 |
| stroke 20 | 8 % → 14 % | 9.2 px | 0.57 | 1.70 | 6 |
| stroke 21 | 4 % → 4 % | 4.3 px | 0.57 | 1.00 | 6 |
| stroke 22 | 8 % → 13 % | 8.6 px | 0.57 | 1.79 | 6 |
| stroke 23 | 7 % → 12 % | 8.3 px | 0.57 | 1.61 | 6 |
| stroke 24 | 4 % → 7 % | 4.7 px | 0.57 | 1.71 | 6 |
| stroke 25 | 8 % → 14 % | 8.7 px | 0.57 | 1.84 | 6 |
| stroke 26 | 6 % → 8 % | 6.5 px | 0.57 | 1.34 | 6 |
| stroke 27 | 4 % → 4 % | 4.3 px | 0.57 | 1.10 | 6 |
| stroke 28 | 7 % → 11 % | 8.2 px | 0.57 | 1.59 | 8 |
| stroke 29 | 8 % → 17 % | 8.8 px | 0.57 | 2.21 | 6 |
| stroke 30 | 13 % → 17 % | 14.9 px | 0.57 | 1.29 | 6 |
| stroke 31 | 5 % → 6 % | 5.4 px | 0.57 | 1.29 | 6 |
| stroke 32 | 10 % → 13 % | 11.8 px | 0.57 | 1.24 | 6 |
| stroke 33 | 7 % → 8 % | 8.5 px | 0.57 | 1.07 | 6 |
| stroke 34 | 11 % → 14 % | 12.0 px | 0.57 | 1.36 | 6 |
| stroke 35 | 9 % → 14 % | 10.0 px | 0.57 | 1.61 | 8 |
| stroke 36 | 10 % → 13 % | 11.4 px | 0.57 | 1.26 | 6 |
| stroke 37 | 9 % → 16 % | 10.5 px | 0.57 | 1.71 | 6 |
| stroke 38 | 13 % → 19 % | 14.8 px | 0.57 | 1.48 | 6 |
| stroke 39 | 14 % → 17 % | 15.7 px | 0.57 | 1.21 | 6 |
| stroke 40 | 6 % → 7 % | 7.2 px | 0.57 | 1.14 | 6 |
| stroke 41 | 16 % → 16 % | 17.7 px | 0.57 | 1.01 | 6 |
| stroke 42 | 14 % → 16 % | 15.2 px | 0.57 | 1.17 | 9 |
| stroke 43 | 10 % → 12 % | 11.6 px | 0.57 | 1.17 | 6 |
| stroke 44 | 12 % → 15 % | 14.3 px | 0.57 | 1.22 | 6 |
| stroke 45 | 2 % → 2 % | 2.7 px | 0.57 | 1.00 | 6 |
| stroke 46 | 16 % → 16 % | 18.5 px | 0.57 | 1.00 | 6 |
| stroke 47 | 13 % → 13 % | 15.0 px | 0.57 | 1.00 | 6 |
| stroke 48 | 12 % → 13 % | 14.3 px | 0.57 | 1.07 | 6 |
| stroke 49 | 19 % → 19 % | 21.5 px | 0.57 | 1.00 | 8 |
| stroke 50 | 10 % → 10 % | 11.6 px | 0.57 | 1.00 | 6 |

Numbers say: wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #39 Very thick impasto — own sheet
own sheet 600 × 600 · Heavy acrylic · 60 px · 5.6 s

![Brush Artist · Refs · #39 Very thick impasto — own sheet](Brush-Artist-Refs-39-Very-thick-impasto-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 27 % → 39 % | 61.5 px | 0.43 | 1.45 | 262 |
| stroke 2 | 32 % → 50 % | 96.9 px | 0.44 | 1.56 | 269 |
| stroke 3 | 38 % → 52 % | 128.8 px | 0.44 | 1.35 | 237 |
| stroke 4 | 32 % → 46 % | 93.6 px | 0.44 | 1.43 | 306 |
| stroke 5 | 43 % → 43 % | 108.0 px | 0.44 | 0.99 | 258 |

Numbers say: wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #40 Watercolour blooms — own sheet
own sheet 600 × 600 · Watercolor · 90 px · 6.6 s

![Brush Artist · Refs · #40 Watercolour blooms — own sheet](Brush-Artist-Refs-40-Watercolour-blooms-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 21 % → 25 % | 92.4 px | 0.13 | 1.20 | 678 |

## Brush Artist · Refs · #41 Coloured pencil hatching — own sheet
own sheet 600 × 600 · Pastel · 4 px · 2.9 s

![Brush Artist · Refs · #41 Coloured pencil hatching — own sheet](Brush-Artist-Refs-41-Coloured-pencil-hatching-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 3 % → 13 % | 2.2 px | 0.35 | 4.64 | 5 |
| stroke 2 | 3 % → 7 % | 2.3 px | 0.35 | 2.29 | 4 |
| stroke 3 | 2 % → 11 % | 1.9 px | 0.35 | 4.38 | 4 |
| stroke 4 | 3 % → 19 % | 2.1 px | 0.35 | 6.73 | 4 |
| stroke 5 | 4 % → 7 % | 2.9 px | 0.35 | 1.83 | 4 |
| stroke 6 | 3 % → 13 % | 2.3 px | 0.35 | 4.19 | 5 |
| stroke 7 | 3 % → 15 % | 2.6 px | 0.35 | 4.43 | 4 |
| stroke 8 | 3 % → 12 % | 2.1 px | 0.35 | 4.20 | 4 |
| stroke 9 | 5 % → 11 % | 3.6 px | 0.35 | 2.27 | 4 |
| stroke 10 | 5 % → 15 % | 3.8 px | 0.35 | 2.99 | 4 |
| stroke 11 | 4 % → 13 % | 3.0 px | 0.35 | 3.28 | 4 |
| stroke 12 | 3 % → 3 % | 2.1 px | 0.35 | 1.00 | 4 |
| stroke 13 | 7 % → 17 % | 5.2 px | 0.35 | 2.45 | 4 |
| stroke 14 | 3 % → 13 % | 2.4 px | 0.35 | 4.19 | 4 |
| stroke 15 | 6 % → 12 % | 4.4 px | 0.35 | 2.09 | 4 |
| stroke 16 | 7 % → 11 % | 5.1 px | 0.35 | 1.61 | 4 |
| stroke 17 | 3 % → 3 % | 2.1 px | 0.35 | 1.00 | 4 |
| stroke 18 | 5 % → 8 % | 3.6 px | 0.35 | 1.65 | 4 |
| stroke 19 | 5 % → 13 % | 3.8 px | 0.35 | 2.72 | 4 |
| stroke 20 | 5 % → 14 % | 3.7 px | 0.35 | 2.92 | 4 |
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
| stroke 32 | 3 % → 6 % | 2.5 px | 0.35 | 1.79 | 4 |
| stroke 33 | 6 % → 11 % | 5.0 px | 0.35 | 1.67 | 4 |
| stroke 34 | 3 % → 6 % | 2.6 px | 0.35 | 1.73 | 4 |
| stroke 35 | 7 % → 14 % | 5.0 px | 0.35 | 2.09 | 5 |
| stroke 36 | 5 % → 5 % | 3.7 px | 0.35 | 1.01 | 6 |
| stroke 37 | 7 % → 15 % | 5.2 px | 0.35 | 2.15 | 4 |
| stroke 38 | 8 % → 13 % | 5.8 px | 0.35 | 1.66 | 4 |
| stroke 39 | 7 % → 11 % | 5.1 px | 0.35 | 1.67 | 5 |
| stroke 40 | 8 % → 18 % | 6.2 px | 0.35 | 2.21 | 7 |
| stroke 41 | 9 % → 13 % | 6.9 px | 0.35 | 1.48 | 5 |
| stroke 42 | 10 % → 17 % | 7.7 px | 0.35 | 1.73 | 6 |
| stroke 43 | 5 % → 9 % | 3.9 px | 0.35 | 1.66 | 10 |
| stroke 44 | 10 % → 13 % | 7.3 px | 0.35 | 1.40 | 8 |
| stroke 45 | 13 % → 18 % | 9.9 px | 0.35 | 1.35 | 6 |
| stroke 46 | 5 % → 7 % | 3.6 px | 0.34 | 1.41 | 7 |
| stroke 47 | 11 % → 13 % | 8.0 px | 0.35 | 1.20 | 5 |
| stroke 48 | 12 % → 16 % | 9.2 px | 0.35 | 1.34 | 6 |
| stroke 49 | 6 % → 9 % | 4.2 px | 0.35 | 1.66 | 6 |
| stroke 50 | 7 % → 7 % | 5.2 px | 0.34 | 1.00 | 4 |
| stroke 51 | 8 % → 15 % | 6.4 px | 0.35 | 1.74 | 6 |
| stroke 52 | 12 % → 14 % | 9.1 px | 0.35 | 1.19 | 6 |
| stroke 53 | 11 % → 14 % | 8.1 px | 0.35 | 1.36 | 7 |
| stroke 54 | 10 % → 14 % | 7.4 px | 0.35 | 1.47 | 6 |
| stroke 55 | 11 % → 14 % | 8.2 px | 0.35 | 1.33 | 5 |
| stroke 56 | 11 % → 12 % | 8.4 px | 0.35 | 1.11 | 5 |
| stroke 57 | 9 % → 13 % | 7.1 px | 0.35 | 1.37 | 9 |
| stroke 58 | 10 % → 11 % | 7.7 px | 0.35 | 1.14 | 6 |
| stroke 59 | 11 % → 13 % | 8.4 px | 0.35 | 1.18 | 6 |
| stroke 60 | 16 % → 20 % | 11.9 px | 0.35 | 1.26 | 6 |
| stroke 61 | 19 % → 20 % | 14.5 px | 0.35 | 1.04 | 5 |
| stroke 62 | 10 % → 10 % | 7.3 px | 0.35 | 1.00 | 7 |
| stroke 63 | 11 % → 12 % | 8.7 px | 0.35 | 1.07 | 8 |
| stroke 64 | 14 % → 14 % | 10.7 px | 0.35 | 1.02 | 6 |
| stroke 65 | 15 % → 15 % | 11.5 px | 0.35 | 1.00 | 5 |
| stroke 66 | 14 % → 14 % | 10.7 px | 0.35 | 1.00 | 6 |
| stroke 67 | 12 % → 12 % | 8.8 px | 0.35 | 1.06 | 5 |
| stroke 68 | 5 % → 9 % | 3.6 px | 0.35 | 1.88 | 6 |
| stroke 69 | 5 % → 5 % | 4.1 px | 0.35 | 1.00 | 7 |
| stroke 70 | 10 % → 13 % | 7.4 px | 0.35 | 1.28 | 5 |
| stroke 71 | 9 % → 11 % | 7.1 px | 0.35 | 1.15 | 5 |
| stroke 72 | 5 % → 7 % | 4.2 px | 0.35 | 1.23 | 14 |
| stroke 73 | 12 % → 12 % | 9.3 px | 0.35 | 1.00 | 6 |
| stroke 74 | 14 % → 14 % | 10.8 px | 0.35 | 1.00 | 5 |
| stroke 75 | 15 % → 15 % | 11.4 px | 0.35 | 1.00 | 5 |
| stroke 76 | 14 % → 14 % | 10.5 px | 0.35 | 1.00 | 6 |
| stroke 77 | 7 % → 10 % | 5.4 px | 0.35 | 1.34 | 7 |
| stroke 78 | 9 % → 9 % | 7.0 px | 0.35 | 1.00 | 6 |
| stroke 79 | 7 % → 7 % | 5.7 px | 0.35 | 1.00 | 5 |
| stroke 80 | 11 % → 11 % | 8.3 px | 0.35 | 1.00 | 7 |

Numbers say: wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #42 Oil pastel shaggy — own sheet
own sheet 600 × 600 · Pastel · 18 px · 2.8 s

![Brush Artist · Refs · #42 Oil pastel shaggy — own sheet](Brush-Artist-Refs-42-Oil-pastel-shaggy-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 5 % → 27 % | 8.0 px | 0.28 | 5.73 | 13 |
| stroke 2 | 5 % → 24 % | 8.6 px | 0.28 | 4.69 | 13 |
| stroke 3 | 5 % → 29 % | 8.9 px | 0.28 | 5.42 | 18 |
| stroke 4 | 5 % → 11 % | 8.8 px | 0.28 | 2.08 | 9 |
| stroke 5 | 6 % → 11 % | 9.9 px | 0.28 | 1.85 | 10 |
| stroke 6 | 8 % → 37 % | 13.9 px | 0.29 | 4.44 | 9 |
| stroke 7 | 11 % → 31 % | 17.6 px | 0.28 | 2.90 | 10 |
| stroke 8 | 7 % → 38 % | 11.4 px | 0.28 | 5.55 | 9 |
| stroke 9 | 8 % → 21 % | 13.9 px | 0.28 | 2.53 | 10 |
| stroke 10 | 8 % → 18 % | 13.2 px | 0.28 | 2.32 | 10 |
| stroke 11 | 6 % → 27 % | 9.4 px | 0.28 | 4.74 | 10 |
| stroke 12 | 8 % → 19 % | 13.6 px | 0.28 | 2.29 | 10 |
| stroke 13 | 13 % → 24 % | 21.0 px | 0.28 | 1.92 | 10 |
| stroke 14 | 5 % → 23 % | 7.9 px | 0.28 | 4.77 | 10 |
| stroke 15 | 5 % → 24 % | 9.0 px | 0.29 | 4.38 | 10 |
| stroke 16 | 9 % → 21 % | 15.7 px | 0.29 | 2.18 | 9 |
| stroke 17 | 17 % → 39 % | 27.9 px | 0.29 | 2.34 | 12 |
| stroke 18 | 14 % → 25 % | 22.8 px | 0.29 | 1.79 | 10 |
| stroke 19 | 15 % → 32 % | 24.9 px | 0.28 | 2.09 | 10 |
| stroke 20 | 21 % → 39 % | 35.1 px | 0.28 | 1.85 | 9 |
| stroke 21 | 9 % → 16 % | 14.4 px | 0.28 | 1.88 | 10 |
| stroke 22 | 14 % → 17 % | 23.9 px | 0.28 | 1.20 | 10 |
| stroke 23 | 12 % → 17 % | 20.6 px | 0.29 | 1.34 | 10 |
| stroke 24 | 18 % → 26 % | 30.0 px | 0.29 | 1.44 | 9 |
| stroke 25 | 20 % → 34 % | 32.6 px | 0.28 | 1.74 | 9 |
| stroke 26 | 6 % → 14 % | 9.2 px | 0.28 | 2.43 | 10 |
| stroke 27 | 18 % → 26 % | 30.4 px | 0.29 | 1.41 | 10 |
| stroke 28 | 14 % → 24 % | 23.7 px | 0.28 | 1.68 | 9 |
| stroke 29 | 9 % → 27 % | 14.9 px | 0.29 | 3.01 | 10 |
| stroke 30 | 15 % → 36 % | 24.9 px | 0.29 | 2.43 | 10 |
| stroke 31 | 14 % → 17 % | 23.3 px | 0.28 | 1.23 | 10 |
| stroke 32 | 16 % → 29 % | 27.0 px | 0.29 | 1.82 | 10 |
| stroke 33 | 15 % → 16 % | 24.5 px | 0.29 | 1.09 | 9 |
| stroke 34 | 19 % → 27 % | 31.4 px | 0.28 | 1.44 | 12 |
| stroke 35 | 26 % → 36 % | 42.5 px | 0.28 | 1.40 | 10 |
| stroke 36 | 25 % → 34 % | 41.0 px | 0.28 | 1.36 | 9 |
| stroke 37 | 12 % → 12 % | 19.3 px | 0.28 | 1.03 | 10 |
| stroke 38 | 19 % → 25 % | 31.7 px | 0.28 | 1.30 | 10 |
| stroke 39 | 16 % → 22 % | 27.3 px | 0.28 | 1.37 | 10 |
| stroke 40 | 22 % → 31 % | 36.6 px | 0.28 | 1.38 | 12 |
| stroke 41 | 32 % → 36 % | 53.1 px | 0.28 | 1.12 | 11 |
| stroke 42 | 23 % → 30 % | 38.1 px | 0.29 | 1.29 | 9 |
| stroke 43 | 12 % → 12 % | 20.3 px | 0.28 | 1.00 | 9 |
| stroke 44 | 30 % → 37 % | 48.9 px | 0.28 | 1.26 | 9 |
| stroke 45 | 16 % → 16 % | 26.2 px | 0.28 | 1.00 | 9 |
| stroke 46 | 29 % → 34 % | 47.9 px | 0.29 | 1.15 | 9 |
| stroke 47 | 38 % → 41 % | 62.0 px | 0.28 | 1.10 | 9 |
| stroke 48 | 29 % → 36 % | 47.8 px | 0.29 | 1.27 | 9 |
| stroke 49 | 27 % → 30 % | 45.1 px | 0.29 | 1.11 | 9 |
| stroke 50 | 38 % → 40 % | 63.4 px | 0.28 | 1.06 | 10 |
| stroke 51 | 16 % → 16 % | 26.0 px | 0.28 | 1.00 | 9 |
| stroke 52 | 37 % → 38 % | 62.4 px | 0.29 | 1.01 | 9 |
| stroke 53 | 22 % → 26 % | 36.9 px | 0.28 | 1.18 | 9 |
| stroke 54 | 17 % → 19 % | 29.0 px | 0.29 | 1.09 | 9 |
| stroke 55 | 15 % → 15 % | 25.0 px | 0.28 | 1.00 | 9 |
| stroke 56 | 13 % → 14 % | 21.6 px | 0.28 | 1.08 | 9 |
| stroke 57 | 23 % → 23 % | 37.7 px | 0.29 | 1.00 | 9 |
| stroke 58 | 28 % → 29 % | 46.1 px | 0.28 | 1.05 | 9 |
| stroke 59 | 40 % → 40 % | 67.3 px | 0.28 | 1.00 | 9 |
| stroke 60 | 22 % → 22 % | 35.6 px | 0.28 | 1.00 | 9 |

Numbers say: wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #43 Dragged black ink blocks — own sheet
own sheet 600 × 600 · Gouache · 70 px · 7.2 s

![Brush Artist · Refs · #43 Dragged black ink blocks — own sheet](Brush-Artist-Refs-43-Dragged-black-ink-blocks-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 16 % → 12 % | 37.3 px | 0.46 | 0.73 | 404 |
| stroke 2 | 16 % → 13 % | 58.0 px | 0.46 | 0.78 | 462 |
| stroke 3 | 20 % → 16 % | 72.4 px | 0.46 | 0.79 | 474 |
| stroke 4 | 20 % → 16 % | 70.6 px | 0.46 | 0.77 | 405 |
| stroke 5 | 24 % → 14 % | 56.0 px | 0.46 | 0.57 | 440 |

## Brush Artist · Refs · #44 Blue looping ribbon — own sheet
own sheet 600 × 600 · Oil · 80 px · 5.5 s

![Brush Artist · Refs · #44 Blue looping ribbon — own sheet](Brush-Artist-Refs-44-Blue-looping-ribbon-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 32 % → 32 % | 42.2 px | 0.78 | 1.00 | 2603 |

## Brush Artist · Refs · #45 Soft pastel pepper — own sheet
own sheet 600 × 600 · Pastel · 40 px · 4.2 s

![Brush Artist · Refs · #45 Soft pastel pepper — own sheet](Brush-Artist-Refs-45-Soft-pastel-pepper-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 10 % → 39 % | 11.3 px | 0.48 | 3.73 | 322 |
| stroke 2 | 18 % → 34 % | 21.3 px | 0.49 | 1.86 | 315 |
| stroke 3 | 25 % → 37 % | 17.6 px | 0.49 | 1.45 | 301 |
| stroke 4 | 24 % → 35 % | 30.5 px | 0.49 | 1.42 | 327 |
| stroke 5 | 30 % → 30 % | 21.2 px | 0.49 | 1.00 | 210 |
| stroke 6 | 35 % → 44 % | 22.5 px | 0.48 | 1.25 | 299 |
| stroke 7 | 39 % → 43 % | 21.4 px | 0.48 | 1.10 | 343 |
| stroke 8 | 44 % → 44 % | 44.2 px | 0.48 | 1.00 | 310 |

Numbers say: wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #46 Red-brown ink lips — own sheet
own sheet 600 × 600 · Watercolor · 50 px · 5.0 s

![Brush Artist · Refs · #46 Red-brown ink lips — own sheet](Brush-Artist-Refs-46-Red-brown-ink-lips-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 12 % → 24 % | 51.9 px | 0.59 | 1.91 | 89 |
| stroke 2 | 16 % → 27 % | 68.1 px | 0.54 | 1.74 | 72 |

Numbers say: wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #47 Pink knife slabs — own sheet
own sheet 600 × 600 · Heavy acrylic · 90 px · 4.6 s

![Brush Artist · Refs · #47 Pink knife slabs — own sheet](Brush-Artist-Refs-47-Pink-knife-slabs-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 18 % → 34 % | 88.7 px | 0.11 | 1.95 | 260 |
| stroke 2 | 31 % → 46 % | 176.8 px | 0.11 | 1.47 | 262 |
| stroke 3 | 31 % → 46 % | 176.8 px | 0.11 | 1.47 | 249 |
| stroke 4 | 42 % → 41 % | 176.8 px | 0.11 | 0.98 | 252 |

Numbers say: wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #48 Black bands with drips — own sheet
own sheet 600 × 600 · Gouache · 70 px · 10.7 s

![Brush Artist · Refs · #48 Black bands with drips — own sheet](Brush-Artist-Refs-48-Black-bands-with-drips-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 23 % → 36 % | 59.0 px | 0.39 | 1.58 | 419 |
| stroke 2 | 34 % → 48 % | 108.7 px | 0.39 | 1.41 | 429 |
| stroke 3 | 36 % → 48 % | 112.8 px | 0.39 | 1.34 | 453 |
| stroke 4 | 38 % → 36 % | 111.8 px | 0.39 | 0.95 | 572 |

Numbers say: wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #49 Magenta letters round brush — own sheet
own sheet 600 × 600 · Ink · 30 px · 10.1 s

![Brush Artist · Refs · #49 Magenta letters round brush — own sheet](Brush-Artist-Refs-49-Magenta-letters-round-brush-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 27 % → 46 % | 64.3 px | 0.52 | 1.69 | 32 |
| stroke 2 | 29 % → 40 % | 52.5 px | 0.53 | 1.39 | 30 |
| stroke 3 | 41 % → 67 % | 96.4 px | 0.52 | 1.64 | 28 |
| stroke 4 | 34 % → 52 % | 53.7 px | 0.52 | 1.55 | 102 |
| stroke 5 | 40 % → 66 % | 94.8 px | 0.52 | 1.65 | 70 |
| stroke 6 | 54 % → 70 % | 231.2 px | 0.52 | 1.29 | 15 |
| stroke 7 | 41 % → 56 % | 63.9 px | 0.52 | 1.35 | 106 |
| stroke 8 | 36 % → 61 % | 91.9 px | 0.53 | 1.72 | 63 |
| stroke 9 | 49 % → 60 % | 152.9 px | 0.53 | 1.24 | 26 |
| stroke 10 | 42 % → 72 % | 100.5 px | 0.52 | 1.71 | 84 |
| stroke 11 | 52 % → 72 % | 219.5 px | 0.52 | 1.39 | 22 |
| stroke 12 | 53 % → 68 % | 82.2 px | 0.52 | 1.29 | 183 |
| stroke 13 | 42 % → 54 % | 116.0 px | 0.53 | 1.29 | 44 |
| stroke 14 | 45 % → 69 % | 131.9 px | 0.53 | 1.52 | 45 |
| stroke 15 | 43 % → 63 % | 102.4 px | 0.52 | 1.46 | 109 |
| stroke 16 | 52 % → 61 % | 220.2 px | 0.52 | 1.18 | 24 |
| stroke 17 | 53 % → 64 % | 82.3 px | 0.52 | 1.19 | 181 |
| stroke 18 | 36 % → 44 % | 99.6 px | 0.52 | 1.21 | 51 |
| stroke 19 | 54 % → 53 % | 123.8 px | 0.52 | 0.99 | 50 |
| stroke 20 | 54 % → 54 % | 125.3 px | 0.52 | 1.00 | 46 |
| stroke 21 | 49 % → 49 % | 81.3 px | 0.52 | 1.00 | 97 |

Numbers say: wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #50 Thick swipes on photo — own sheet
own sheet 600 × 600 · Heavy acrylic · 40 px · 4.9 s

![Brush Artist · Refs · #50 Thick swipes on photo — own sheet](Brush-Artist-Refs-50-Thick-swipes-on-photo-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 10 % → 26 % | 46.9 px | 0.32 | 2.58 | 34 |
| stroke 2 | 10 % → 20 % | 48.1 px | 0.31 | 1.93 | 27 |
| stroke 3 | 11 % → 13 % | 45.4 px | 0.32 | 1.16 | 39 |
| stroke 4 | 12 % → 25 % | 47.6 px | 0.32 | 2.05 | 31 |
| stroke 5 | 12 % → 13 % | 46.0 px | 0.32 | 1.07 | 35 |
| stroke 6 | 19 % → 25 % | 109.7 px | 0.31 | 1.30 | 24 |
| stroke 7 | 24 % → 31 % | 102.1 px | 0.32 | 1.29 | 37 |
| stroke 8 | 24 % → 25 % | 134.5 px | 0.32 | 1.03 | 30 |
| stroke 9 | 12 % → 14 % | 52.6 px | 0.31 | 1.20 | 36 |
| stroke 10 | 26 % → 28 % | 88.4 px | 0.31 | 1.08 | 64 |
| stroke 11 | 9 % → 10 % | 47.2 px | 0.32 | 1.09 | 53 |
| stroke 12 | 18 % → 19 % | 100.0 px | 0.32 | 1.07 | 28 |

Numbers say: wet paint spreads well beyond the stroke.

## Brush Artist · Ink — dry brush — own sheet
own sheet 600 × 600 · Gouache · 30 px · 2.9 s

![Brush Artist · Ink — dry brush — own sheet](Brush-Artist-Ink-dry-brush-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| ear | 6 % → 3 % | 7.8 px | 0.86 | 0.44 | 451 |
| drag0 | 6 % → 8 % | 10.2 px | 0.86 | 1.39 | 119 |
| drag1 | 8 % → 8 % | 16.5 px | 0.86 | 1.02 | 102 |
| drag2 | 10 % → 9 % | 22.5 px | 0.86 | 0.87 | 83 |
| drag3 | 12 % → 9 % | 29.4 px | 0.86 | 0.78 | 65 |

## Brush Artist · Watercolour — blue — own sheet
own sheet 600 × 600 · Watercolor · 40 px · 9.9 s

![Brush Artist · Watercolour — blue — own sheet](Brush-Artist-Watercolour-blue-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| s0 | 7 % → 23 % | 28.4 px | 0.25 | 3.20 | 41 |
| s1 | 5 % → 32 % | 9.9 px | 0.38 | 5.85 | 38 |
| s2 | 10 % → 18 % | 43.5 px | 0.19 | 1.75 | 37 |
| s3 | 9 % → 17 % | 26.3 px | 0.28 | 1.85 | 45 |
| s4 | 14 % → 29 % | 37.9 px | 0.36 | 2.11 | 54 |
| s5 | 19 % → 29 % | 38.9 px | 0.37 | 1.52 | 49 |
| s6 | 17 % → 21 % | 47.6 px | 0.27 | 1.22 | 53 |
| s7 | 24 % → 35 % | 31.9 px | 0.37 | 1.44 | 40 |
| s8 | 20 % → 24 % | 77.5 px | 0.27 | 1.18 | 45 |

Numbers say: wet paint spreads well beyond the stroke.

## Brush Artist · Charcoal — stick — own sheet
own sheet 600 × 600 · Charcoal · 28 px · 1.1 s

![Brush Artist · Charcoal — stick — own sheet](Brush-Artist-Charcoal-stick-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| finger0 | 9 % → 18 % | 15.5 px | 0.83 | 2.01 | 28 |
| tip0 | 8 % → 14 % | 22.1 px | 0.83 | 1.75 | 8 |
| finger1 | 17 % → 29 % | 29.4 px | 0.83 | 1.74 | 26 |
| tip1 | 15 % → 21 % | 39.1 px | 0.83 | 1.42 | 10 |
| finger2 | 17 % → 25 % | 29.5 px | 0.83 | 1.53 | 25 |
| tip2 | 14 % → 20 % | 39.0 px | 0.83 | 1.41 | 9 |
| finger3 | 16 % → 19 % | 29.3 px | 0.83 | 1.16 | 24 |
| tip3 | 15 % → 15 % | 39.0 px | 0.83 | 1.00 | 8 |
| cig0 | 25 % → 35 % | 54.8 px | 0.83 | 1.41 | 13 |
| cig1 | 26 % → 35 % | 58.8 px | 0.83 | 1.32 | 9 |
| cig2 | 28 % → 35 % | 63.2 px | 0.83 | 1.22 | 9 |
| cig3 | 30 % → 34 % | 67.3 px | 0.83 | 1.14 | 9 |
| cig4 | 32 % → 34 % | 71.5 px | 0.83 | 1.06 | 9 |
| cig5 | 34 % → 34 % | 75.3 px | 0.83 | 1.00 | 10 |

Numbers say: wet paint spreads well beyond the stroke.

