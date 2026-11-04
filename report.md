![All brushes](contact.png)

# Brush Lab — 180 brushes · 4 Nov 2026 at 21:40

Every sheet: 1500 × 600, ten strokes in a 5 × 2 grid — 1. light line · 2. heavy line · 3. pressure swell · 4. fast wave · 5. slow wave · 6. spiral · 7. loop · 8. tilted · 9. over the wet one · 10. long, no reload (cell 8 holds «tilted» and «over the wet one» crossed). The CPU reference of Mamay's paint engine; the wet layer settles 20 s at the end.

Columns: **covered** = share of the cell with paint right after the stroke → after settling; **width** = painted area of the stroke ÷ its length (px); **dark** = mean darkness of the painted pixels above the paper's own grain (0 = paper, 1 = black); **spread** = how far wet paint went beyond the stroke (1.0 = stayed); **ms** = the stroke on the CPU; long stroke: paint in each quarter of its length (it should run out: wet → streaks → dry tail).

## Ink Line
Ink · 12 px · 24.3 s

![Ink Line](Ink-Line.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 1 % → 4 % | 4.3 px | 0.55 | 2.45 | 94 |
| heavy line | 5 % → 6 % | 15.7 px | 0.68 | 1.14 | 55 |
| pressure swell | 3 % → 4 % | 11.3 px | 0.64 | 1.40 | 44 |
| fast wave | 10 % → 11 % | 11.2 px | 0.59 | 1.11 | 137 |
| slow wave | 8 % → 10 % | 9.6 px | 0.57 | 1.16 | 133 |
| spiral | 14 % → 15 % | 8.9 px | 0.49 | 1.07 | 209 |
| loop | 8 % → 9 % | 10.6 px | 0.61 | 1.15 | 131 |
| tilted | 5 % → 5 % | 14.3 px | 0.64 | 1.05 | 64 |
| over the wet one | 10 % → 11 % | 12.5 px | 0.64 | 1.15 | 49 |
| long, no reload | 18 % → 17 % | 8.1 px | 0.47 | 0.96 | 330 | quarters: 0.22 → 0.09 → 0.04 → 0.02

Numbers say: light vs heavy: width 4.3 → 15.7 px, dark 0.55 → 0.68; wet paint spreads well beyond the stroke.

## Dense Ink
Ink · 14 px · 24.6 s

![Dense Ink](Dense-Ink.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 5 % → 7 % | 15.2 px | 0.72 | 1.27 | 104 |
| heavy line | 7 % → 7 % | 19.1 px | 0.73 | 1.09 | 62 |
| pressure swell | 5 % → 6 % | 17.9 px | 0.72 | 1.18 | 51 |
| fast wave | 13 % → 13 % | 15.2 px | 0.69 | 1.01 | 143 |
| slow wave | 12 % → 12 % | 13.5 px | 0.67 | 1.04 | 118 |
| spiral | 18 % → 15 % | 12.2 px | 0.65 | 0.80 | 223 |
| loop | 11 % → 12 % | 14.8 px | 0.69 | 1.08 | 125 |
| tilted | 5 % → 6 % | 14.5 px | 0.72 | 1.07 | 90 |
| over the wet one | 12 % → 13 % | 17.7 px | 0.72 | 1.12 | 56 |
| long, no reload | 23 % → 15 % | 10.1 px | 0.64 | 0.66 | 321 | quarters: 0.30 → 0.12 → 0.04 → 0.02

Numbers say: light vs heavy: width 15.2 → 19.1 px, dark 0.72 → 0.73.

## Transparent Wash
Watercolor · 22 px · 25.4 s

![Transparent Wash](Transparent-Wash.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 2 % → 5 % | 6.9 px | 0.27 | 2.26 | 82 |
| heavy line | 7 % → 9 % | 20.4 px | 0.27 | 1.23 | 48 |
| pressure swell | 4 % → 6 % | 15.2 px | 0.28 | 1.54 | 37 |
| fast wave | 14 % → 16 % | 16.1 px | 0.20 | 1.17 | 133 |
| slow wave | 12 % → 15 % | 13.7 px | 0.21 | 1.28 | 163 |
| spiral | 18 % → 22 % | 11.9 px | 0.16 | 1.22 | 170 |
| loop | 11 % → 13 % | 14.5 px | 0.22 | 1.20 | 110 |
| tilted | 8 % → 8 % | 21.1 px | 0.24 | 1.06 | 63 |
| over the wet one | 13 % → 16 % | 16.4 px | 0.24 | 1.19 | 67 |
| long, no reload | 26 % → 32 % | 11.6 px | 0.13 | 1.22 | 332 | quarters: 0.11 → 0.04 → 0.02 → 0.01

Numbers say: light vs heavy: width 6.9 → 20.4 px, dark 0.27 → 0.27; wet paint spreads well beyond the stroke.

## Dry Brush
Gouache · 24 px · 23.2 s

![Dry Brush](Dry-Brush.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 5 % → 1 % | 13.8 px | 0.65 | 0.11 | 157 |
| heavy line | 6 % → 0 % | 18.4 px | 0.65 | 0.02 | 70 |
| pressure swell | 5 % → 0 % | 18.1 px | 0.65 | 0.09 | 53 |
| fast wave | 6 % → 1 % | 6.9 px | 0.65 | 0.08 | 161 |
| slow wave | 7 % → 0 % | 7.8 px | 0.65 | 0.07 | 222 |
| spiral | 7 % → 1 % | 4.4 px | 0.65 | 0.08 | 266 |
| loop | 9 % → 0 % | 12.2 px | 0.65 | 0.05 | 140 |
| tilted | 4 % → 3 % | 10.3 px | 0.65 | 0.89 | 49 |
| over the wet one | 9 % → 1 % | 14.3 px | 0.65 | 0.12 | 58 |
| long, no reload | 6 % → 1 % | 2.7 px | 0.65 | 0.15 | 333 | quarters: 0.12 → 0.00 → 0.00 → 0.00

Numbers say: light vs heavy: width 13.8 → 18.4 px, dark 0.65 → 0.65.

## Wax Crayon
Wax · 8 px · 9.9 s

![Wax Crayon](Wax-Crayon.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 1 % → 1 % | 2.5 px | 0.71 | 1.00 | 77 |
| heavy line | 1 % → 1 % | 3.9 px | 0.69 | 1.00 | 15 |
| pressure swell | 1 % → 1 % | 3.3 px | 0.70 | 1.00 | 10 |
| fast wave | 3 % → 3 % | 3.5 px | 0.69 | 1.00 | 49 |
| slow wave | 3 % → 3 % | 3.4 px | 0.70 | 1.00 | 52 |
| spiral | 5 % → 5 % | 3.3 px | 0.70 | 1.00 | 110 |
| loop | 3 % → 3 % | 3.3 px | 0.70 | 1.00 | 48 |
| tilted | 2 % → 2 % | 5.6 px | 0.68 | 1.00 | 32 |
| over the wet one | 3 % → 3 % | 3.6 px | 0.68 | 1.00 | 14 |
| long, no reload | 7 % → 7 % | 3.3 px | 0.70 | 1.00 | 122 | quarters: 0.06 → 0.06 → 0.06 → 0.06

Numbers say: light vs heavy: width 2.5 → 3.9 px, dark 0.71 → 0.69; the long stroke does not run out of paint.

## Oil Pastel
Wax · 12 px · 10.1 s

![Oil Pastel](Oil-Pastel.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 1 % → 1 % | 4.0 px | 0.68 | 1.00 | 88 |
| heavy line | 2 % → 2 % | 6.5 px | 0.68 | 1.00 | 27 |
| pressure swell | 2 % → 2 % | 5.7 px | 0.69 | 1.00 | 13 |
| fast wave | 5 % → 5 % | 5.7 px | 0.68 | 1.00 | 79 |
| slow wave | 5 % → 5 % | 5.5 px | 0.68 | 1.00 | 63 |
| spiral | 8 % → 8 % | 5.5 px | 0.68 | 1.00 | 146 |
| loop | 4 % → 4 % | 5.6 px | 0.68 | 1.00 | 63 |
| tilted | 2 % → 2 % | 6.8 px | 0.68 | 1.00 | 42 |
| over the wet one | 5 % → 5 % | 5.8 px | 0.68 | 1.00 | 29 |
| long, no reload | 13 % → 13 % | 5.6 px | 0.68 | 1.00 | 157 | quarters: 0.10 → 0.09 → 0.10 → 0.10

Numbers say: light vs heavy: width 4.0 → 6.5 px, dark 0.68 → 0.68; the long stroke does not run out of paint.

## Charcoal
Charcoal · 5 px · 9.5 s

![Charcoal](Charcoal.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 1 % → 1 % | 2.0 px | 0.74 | 1.00 | 63 |
| heavy line | 1 % → 1 % | 3.0 px | 0.74 | 1.00 | 8 |
| pressure swell | 1 % → 1 % | 2.7 px | 0.74 | 1.00 | 5 |
| fast wave | 2 % → 2 % | 2.7 px | 0.73 | 1.00 | 30 |
| slow wave | 2 % → 2 % | 2.6 px | 0.74 | 1.00 | 31 |
| spiral | 4 % → 4 % | 2.5 px | 0.74 | 1.00 | 68 |
| loop | 2 % → 2 % | 2.6 px | 0.74 | 1.00 | 21 |
| tilted | 2 % → 2 % | 4.3 px | 0.72 | 1.00 | 25 |
| over the wet one | 2 % → 2 % | 2.4 px | 0.72 | 1.00 | 10 |
| long, no reload | 6 % → 6 % | 2.7 px | 0.73 | 1.00 | 64 | quarters: 0.05 → 0.05 → 0.05 → 0.05

Numbers say: light vs heavy: width 2.0 → 3.0 px, dark 0.74 → 0.74; the long stroke does not run out of paint.

## Impasto
Heavy acrylic · 22 px · 14.9 s

![Impasto](Impasto.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 8 % → 8 % | 24.1 px | 0.71 | 0.93 | 140 |
| heavy line | 10 % → 9 % | 28.8 px | 0.69 | 0.94 | 93 |
| pressure swell | 7 % → 7 % | 28.1 px | 0.72 | 0.94 | 63 |
| fast wave | 20 % → 13 % | 23.4 px | 0.71 | 0.64 | 195 |
| slow wave | 21 % → 14 % | 24.5 px | 0.71 | 0.66 | 270 |
| spiral | 30 % → 14 % | 19.9 px | 0.71 | 0.46 | 275 |
| loop | 18 % → 14 % | 23.9 px | 0.71 | 0.77 | 153 |
| tilted | 8 % → 8 % | 21.7 px | 0.70 | 1.00 | 69 |
| over the wet one | 17 % → 15 % | 25.4 px | 0.70 | 0.91 | 70 |
| long, no reload | 33 % → 14 % | 14.9 px | 0.71 | 0.42 | 405 | quarters: 0.38 → 0.21 → 0.10 → 0.03

Numbers say: light vs heavy: width 24.1 → 28.8 px, dark 0.71 → 0.69.

## Oil Round
Oil · 18 px · 17.3 s

![Oil Round](Oil-Round.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 2 % → 2 % | 7.2 px | 0.75 | 1.00 | 189 |
| heavy line | 7 % → 7 % | 19.3 px | 0.73 | 1.00 | 61 |
| pressure swell | 4 % → 4 % | 13.7 px | 0.72 | 1.00 | 48 |
| fast wave | 11 % → 11 % | 12.8 px | 0.65 | 1.00 | 161 |
| slow wave | 8 % → 8 % | 9.0 px | 0.57 | 1.00 | 165 |
| spiral | 10 % → 10 % | 6.6 px | 0.50 | 1.00 | 233 |
| loop | 6 % → 6 % | 7.2 px | 0.45 | 1.00 | 121 |
| tilted | 4 % → 4 % | 10.1 px | 0.52 | 1.00 | 91 |
| over the wet one | 6 % → 6 % | 7.6 px | 0.52 | 1.00 | 56 |
| long, no reload | 15 % → 15 % | 6.9 px | 0.42 | 1.00 | 382 | quarters: 0.09 → 0.08 → 0.07 → 0.06

Numbers say: light vs heavy: width 7.2 → 19.3 px, dark 0.75 → 0.73.

## Palette Knife
Oil · 20 px · 16.6 s

![Palette Knife](Palette-Knife.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 8 % → 8 % | 21.9 px | 0.67 | 1.00 | 118 |
| heavy line | 8 % → 8 % | 22.5 px | 0.73 | 1.00 | 14 |
| pressure swell | 6 % → 6 % | 22.3 px | 0.74 | 1.00 | 8 |
| fast wave | 16 % → 16 % | 18.9 px | 0.50 | 1.00 | 32 |
| slow wave | 17 % → 17 % | 19.9 px | 0.43 | 1.00 | 55 |
| spiral | 17 % → 17 % | 11.3 px | 0.46 | 1.00 | 57 |
| loop | 16 % → 16 % | 21.0 px | 0.59 | 1.00 | 28 |
| tilted | 5 % → 5 % | 15.0 px | 0.72 | 1.00 | 11 |
| over the wet one | 13 % → 13 % | 21.0 px | 0.72 | 1.00 | 21 |
| long, no reload | 16 % → 16 % | 7.2 px | 0.49 | 1.00 | 69 | quarters: 0.29 → 0.05 → 0.00 → 0.00

Numbers say: light vs heavy: width 21.9 → 22.5 px, dark 0.67 → 0.73; pressure barely changes the width.

## Water
Watercolor · 20 px · 33.6 s · over bands of wet oil paint and oil pastel in turn (it works on paint already there: look at what it does to the bands; covered counts the bands too)

![Water](Water.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 25 % → 27 % | 73.8 px | 0.80 | 1.06 | 21 |
| heavy line | 24 % → 25 % | 69.8 px | 0.81 | 1.04 | 53 |
| pressure swell | 24 % → 25 % | 89.6 px | 0.81 | 1.03 | 34 |
| fast wave | 24 % → 26 % | 27.7 px | 0.81 | 1.07 | 100 |
| slow wave | 24 % → 25 % | 27.8 px | 0.81 | 1.06 | 143 |
| spiral | 24 % → 26 % | 15.9 px | 0.81 | 1.07 | 167 |
| loop | 24 % → 25 % | 31.1 px | 0.81 | 1.03 | 99 |
| tilted | 24 % → 24 % | 67.0 px | 0.81 | 1.00 | 53 |
| over the wet one | 24 % → 25 % | 0.0 px | 0.81 | 1.06 | 47 |
| long, no reload | 24 % → 26 % | 10.7 px | 0.81 | 1.08 | 263 | quarters: 0.21 → 0.27 → 0.18 → 0.27

Numbers say: light vs heavy: width 73.8 → 69.8 px, dark 0.80 → 0.81; pressure barely changes the width; the long stroke does not run out of paint.

## Blender
Pastel · 16 px · 19.1 s · over bands of wet oil paint and oil pastel in turn (it works on paint already there: look at what it does to the bands; covered counts the bands too)

![Blender](Blender.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 24 % → 24 % | 70.7 px | 0.81 | 1.00 | 26 |
| heavy line | 25 % → 25 % | 72.1 px | 0.80 | 1.00 | 30 |
| pressure swell | 24 % → 24 % | 91.3 px | 0.81 | 1.00 | 22 |
| fast wave | 26 % → 26 % | 30.0 px | 0.79 | 1.00 | 77 |
| slow wave | 26 % → 26 % | 29.9 px | 0.79 | 1.00 | 83 |
| spiral | 28 % → 28 % | 18.7 px | 0.77 | 1.00 | 104 |
| loop | 25 % → 25 % | 33.0 px | 0.80 | 1.00 | 52 |
| tilted | 25 % → 25 % | 70.1 px | 0.79 | 1.00 | 34 |
| over the wet one | 26 % → 26 % | 1.8 px | 0.79 | 1.00 | 27 |
| long, no reload | 30 % → 30 % | 13.7 px | 0.76 | 1.00 | 172 | quarters: 0.20 → 0.28 → 0.23 → 0.30

Numbers say: light vs heavy: width 70.7 → 72.1 px, dark 0.81 → 0.80; pressure barely changes the width; the long stroke does not run out of paint.

## Eraser
Eraser · 16 px · 19.2 s · over bands of wet oil paint and oil pastel in turn (it works on paint already there: look at what it does to the bands; covered counts the bands too)

![Eraser](Eraser.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 24 % → 24 % | 69.6 px | 0.82 | 1.00 | 15 |
| heavy line | 23 % → 23 % | 67.9 px | 0.82 | 1.00 | 26 |
| pressure swell | 23 % → 23 % | 87.3 px | 0.82 | 1.00 | 35 |
| fast wave | 22 % → 22 % | 25.7 px | 0.82 | 1.00 | 75 |
| slow wave | 22 % → 22 % | 25.7 px | 0.82 | 1.00 | 63 |
| spiral | 22 % → 22 % | 14.4 px | 0.82 | 1.00 | 119 |
| loop | 22 % → 22 % | 28.6 px | 0.82 | 1.00 | 57 |
| tilted | 23 % → 23 % | 65.1 px | 0.82 | 1.00 | 40 |
| over the wet one | 23 % → 23 % | 0.0 px | 0.82 | 1.00 | 33 |
| long, no reload | 20 % → 20 % | 8.9 px | 0.82 | 1.00 | 173 | quarters: 0.15 → 0.20 → 0.15 → 0.20

Numbers say: light vs heavy: width 69.6 → 67.9 px, dark 0.82 → 0.82; pressure barely changes the width; the long stroke does not run out of paint.

## Fan
Gouache · 30 px · 27.4 s

![Fan](Fan.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 9 % → 3 % | 25.6 px | 0.63 | 0.37 | 33 |
| heavy line | 11 % → 4 % | 30.9 px | 0.63 | 0.39 | 44 |
| pressure swell | 8 % → 5 % | 31.7 px | 0.63 | 0.55 | 36 |
| fast wave | 17 % → 5 % | 20.2 px | 0.63 | 0.26 | 93 |
| slow wave | 18 % → 5 % | 21.0 px | 0.63 | 0.25 | 178 |
| spiral | 24 % → 5 % | 15.5 px | 0.63 | 0.19 | 162 |
| loop | 17 % → 5 % | 22.7 px | 0.63 | 0.28 | 77 |
| tilted | 5 % → 6 % | 15.0 px | 0.63 | 1.05 | 35 |
| over the wet one | 16 % → 8 % | 29.7 px | 0.63 | 0.49 | 37 |
| long, no reload | 22 % → 5 % | 9.9 px | 0.63 | 0.22 | 252 | quarters: 0.29 → 0.07 → 0.01 → 0.00

Numbers say: light vs heavy: width 25.6 → 30.9 px, dark 0.63 → 0.63.

## Sponge
Gouache · 30 px · 28.3 s

![Sponge](Sponge.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 4 % → 0 % | 11.3 px | 0.62 | 0.12 | 36 |
| heavy line | 12 % → 2 % | 35.4 px | 0.62 | 0.14 | 59 |
| pressure swell | 7 % → 2 % | 27.9 px | 0.62 | 0.28 | 35 |
| fast wave | 20 % → 4 % | 23.2 px | 0.62 | 0.19 | 118 |
| slow wave | 21 % → 4 % | 23.8 px | 0.62 | 0.18 | 204 |
| spiral | 28 % → 4 % | 18.3 px | 0.62 | 0.14 | 179 |
| loop | 18 % → 5 % | 23.0 px | 0.62 | 0.29 | 97 |
| tilted | 7 % → 7 % | 18.2 px | 0.62 | 1.04 | 78 |
| over the wet one | 16 % → 6 % | 27.8 px | 0.62 | 0.37 | 51 |
| long, no reload | 29 % → 5 % | 12.9 px | 0.62 | 0.17 | 256 | quarters: 0.29 → 0.13 → 0.07 → 0.04

Numbers say: light vs heavy: width 11.3 → 35.4 px, dark 0.62 → 0.62.

## Ink — sumi brush
Watercolour 1.00 · 22 px · 26.8 s

![Ink — sumi brush](Ink-sumi-brush.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 8 % → 9 % | 23.9 px | 0.87 | 1.12 | 57 |
| heavy line | 13 % → 13 % | 38.1 px | 0.86 | 1.00 | 58 |
| pressure swell | 9 % → 10 % | 34.5 px | 0.87 | 1.05 | 41 |
| fast wave | 28 % → 28 % | 32.5 px | 0.81 | 1.00 | 154 |
| slow wave | 26 % → 26 % | 29.6 px | 0.82 | 1.02 | 234 |
| spiral | 38 % → 37 % | 25.3 px | 0.74 | 0.96 | 252 |
| loop | 22 % → 22 % | 28.5 px | 0.85 | 1.02 | 120 |
| tilted | 9 % → 9 % | 25.3 px | 0.86 | 1.01 | 64 |
| over the wet one | 20 % → 21 % | 30.7 px | 0.86 | 1.03 | 69 |
| long, no reload | 45 % → 40 % | 20.1 px | 0.70 | 0.89 | 360 | quarters: 0.55 → 0.40 → 0.23 → 0.14

Numbers say: light vs heavy: width 23.9 → 38.1 px, dark 0.87 → 0.86.

## Ink — wash
Watercolour 1.00 · 40 px · 30.1 s

![Ink — wash](Ink-wash.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 13 % → 13 % | 37.3 px | 0.42 | 1.02 | 59 |
| heavy line | 19 % → 19 % | 55.2 px | 0.35 | 1.01 | 78 |
| pressure swell | 13 % → 13 % | 48.2 px | 0.41 | 1.02 | 54 |
| fast wave | 41 % → 42 % | 47.8 px | 0.32 | 1.02 | 187 |
| slow wave | 39 % → 40 % | 45.3 px | 0.42 | 1.02 | 322 |
| spiral | 60 % → 62 % | 39.7 px | 0.33 | 1.02 | 310 |
| loop | 34 % → 34 % | 43.8 px | 0.39 | 1.01 | 179 |
| tilted | 15 % → 15 % | 40.7 px | 0.43 | 1.01 | 97 |
| over the wet one | 30 % → 31 % | 43.4 px | 0.43 | 1.02 | 83 |
| long, no reload | 71 % → 75 % | 32.0 px | 0.31 | 1.05 | 490 | quarters: 0.40 → 0.29 → 0.19 → 0.12

Numbers say: light vs heavy: width 37.3 → 55.2 px, dark 0.42 → 0.35.

## Ink — dry brush
Ink 1.00 · 30 px · 22.6 s

![Ink — dry brush](Ink-dry-brush.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 6 % → 5 % | 16.8 px | 0.82 | 0.87 | 65 |
| heavy line | 6 % → 5 % | 18.6 px | 0.82 | 0.78 | 114 |
| pressure swell | 5 % → 4 % | 18.0 px | 0.83 | 0.88 | 65 |
| fast wave | 11 % → 7 % | 13.2 px | 0.80 | 0.60 | 207 |
| slow wave | 12 % → 7 % | 13.5 px | 0.80 | 0.56 | 348 |
| spiral | 18 % → 7 % | 11.6 px | 0.78 | 0.41 | 347 |
| loop | 11 % → 7 % | 14.2 px | 0.79 | 0.66 | 166 |
| tilted | 6 % → 6 % | 16.3 px | 0.80 | 1.06 | 111 |
| over the wet one | 12 % → 11 % | 17.4 px | 0.80 | 0.93 | 88 |
| long, no reload | 19 % → 8 % | 8.4 px | 0.77 | 0.42 | 487 | quarters: 0.25 → 0.08 → 0.02 → 0.01

Numbers say: light vs heavy: width 16.8 → 18.6 px, dark 0.82 → 0.82; pressure barely changes the width.

## Ink — nib
Watercolour 1.00 · 5 px · 22.1 s

![Ink — nib](Ink-nib.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 2 % → 5 % | 5.5 px | 0.89 | 2.46 | 20 |
| heavy line | 2 % → 5 % | 6.4 px | 0.89 | 2.34 | 20 |
| pressure swell | 2 % → 4 % | 6.2 px | 0.89 | 2.53 | 12 |
| fast wave | 5 % → 8 % | 5.9 px | 0.89 | 1.63 | 63 |
| slow wave | 5 % → 8 % | 5.7 px | 0.89 | 1.70 | 52 |
| spiral | 8 % → 11 % | 5.0 px | 0.87 | 1.41 | 103 |
| loop | 4 % → 8 % | 5.7 px | 0.89 | 1.74 | 57 |
| tilted | 4 % → 4 % | 10.3 px | 0.89 | 1.02 | 30 |
| over the wet one | 6 % → 9 % | 6.1 px | 0.89 | 1.61 | 22 |
| long, no reload | 9 % → 12 % | 4.2 px | 0.85 | 1.30 | 173 | quarters: 0.24 → 0.11 → 0.07 → 0.05

Numbers say: light vs heavy: width 5.5 → 6.4 px, dark 0.89 → 0.89; wet paint spreads well beyond the stroke.

## 0.45 · Dry brush
Gouache 0.91 · Ink 0.07 · 34 px · 26.6 s

![0.45 · Dry brush](0-45-Dry-brush.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 8 % → 4 % | 24.2 px | 0.68 | 0.51 | 102 |
| heavy line | 9 % → 5 % | 25.9 px | 0.68 | 0.52 | 107 |
| pressure swell | 7 % → 4 % | 26.7 px | 0.68 | 0.62 | 80 |
| fast wave | 16 % → 5 % | 18.8 px | 0.68 | 0.31 | 266 |
| slow wave | 19 % → 6 % | 22.1 px | 0.68 | 0.33 | 472 |
| spiral | 26 % → 6 % | 17.1 px | 0.68 | 0.23 | 470 |
| loop | 16 % → 7 % | 21.2 px | 0.68 | 0.41 | 240 |
| tilted | 8 % → 8 % | 22.8 px | 0.68 | 1.02 | 135 |
| over the wet one | 17 % → 12 % | 24.3 px | 0.68 | 0.69 | 123 |
| long, no reload | 28 % → 7 % | 12.7 px | 0.68 | 0.25 | 667 | quarters: 0.33 → 0.22 → 0.14 → 0.12

Numbers say: light vs heavy: width 24.2 → 25.9 px, dark 0.68 → 0.68; pressure barely changes the width.

## Dry pastel
Pastel 1.00 · 26 px · 9.8 s

![Dry pastel](Dry-pastel.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 3 % → 3 % | 8.1 px | 0.38 | 1.00 | 24 |
| heavy line | 4 % → 4 % | 12.8 px | 0.39 | 1.00 | 29 |
| pressure swell | 3 % → 3 % | 11.7 px | 0.38 | 1.00 | 24 |
| fast wave | 10 % → 10 % | 11.8 px | 0.39 | 1.00 | 81 |
| slow wave | 10 % → 10 % | 11.3 px | 0.39 | 1.00 | 154 |
| spiral | 14 % → 14 % | 9.5 px | 0.38 | 1.00 | 140 |
| loop | 7 % → 7 % | 9.3 px | 0.39 | 1.00 | 72 |
| tilted | 3 % → 3 % | 8.3 px | 0.38 | 1.00 | 45 |
| over the wet one | 7 % → 7 % | 10.7 px | 0.38 | 1.00 | 37 |
| long, no reload | 18 % → 18 % | 8.2 px | 0.39 | 1.00 | 220 | quarters: 0.08 → 0.08 → 0.08 → 0.07

Numbers say: light vs heavy: width 8.1 → 12.8 px, dark 0.38 → 0.39; the long stroke does not run out of paint.

## 0.45 · Charcoal
Charcoal 1.00 · 18 px · 9.6 s

![0.45 · Charcoal](0-45-Charcoal.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 2 % → 2 % | 6.5 px | 0.80 | 1.00 | 21 |
| heavy line | 3 % → 3 % | 9.2 px | 0.80 | 1.00 | 25 |
| pressure swell | 2 % → 2 % | 8.8 px | 0.80 | 1.00 | 8 |
| fast wave | 7 % → 7 % | 8.5 px | 0.80 | 1.00 | 49 |
| slow wave | 7 % → 7 % | 8.0 px | 0.80 | 1.00 | 54 |
| spiral | 12 % → 12 % | 7.9 px | 0.80 | 1.00 | 70 |
| loop | 6 % → 6 % | 8.1 px | 0.80 | 1.00 | 40 |
| tilted | 3 % → 3 % | 7.5 px | 0.80 | 1.00 | 24 |
| over the wet one | 6 % → 6 % | 7.8 px | 0.80 | 1.00 | 20 |
| long, no reload | 17 % → 17 % | 7.7 px | 0.80 | 1.00 | 112 | quarters: 0.15 → 0.16 → 0.15 → 0.16

Numbers say: light vs heavy: width 6.5 → 9.2 px, dark 0.80 → 0.80; the long stroke does not run out of paint.

## Watercolour — wash
Watercolour 1.00 · 50 px · 31.8 s

![Watercolour — wash](Watercolour-wash.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 16 % → 16 % | 45.5 px | 0.22 | 1.01 | 89 |
| heavy line | 22 % → 22 % | 64.9 px | 0.19 | 1.00 | 119 |
| pressure swell | 15 % → 15 % | 56.1 px | 0.22 | 1.01 | 74 |
| fast wave | 48 % → 49 % | 55.5 px | 0.19 | 1.01 | 281 |
| slow wave | 46 % → 46 % | 53.3 px | 0.24 | 1.00 | 463 |
| spiral | 66 % → 66 % | 43.7 px | 0.21 | 1.00 | 450 |
| loop | 40 % → 40 % | 51.4 px | 0.22 | 1.00 | 238 |
| tilted | 18 % → 18 % | 49.7 px | 0.23 | 1.00 | 168 |
| over the wet one | 36 % → 36 % | 49.6 px | 0.23 | 1.01 | 97 |
| long, no reload | 84 % → 84 % | 37.7 px | 0.20 | 1.00 | 774 | quarters: 0.24 → 0.20 → 0.16 → 0.12

Numbers say: light vs heavy: width 45.5 → 64.9 px, dark 0.22 → 0.19.

## Watercolour — wet-in-wet
Watercolour 1.00 · 44 px · 33.7 s

![Watercolour — wet-in-wet](Watercolour-wet-in-wet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 13 % → 21 % | 38.4 px | 0.32 | 1.58 | 77 |
| heavy line | 19 % → 22 % | 54.6 px | 0.34 | 1.17 | 97 |
| pressure swell | 12 % → 17 % | 46.5 px | 0.35 | 1.34 | 77 |
| fast wave | 41 % → 49 % | 47.7 px | 0.33 | 1.19 | 224 |
| slow wave | 40 % → 48 % | 46.2 px | 0.40 | 1.21 | 389 |
| spiral | 63 % → 69 % | 41.5 px | 0.37 | 1.10 | 396 |
| loop | 34 % → 41 % | 44.4 px | 0.37 | 1.20 | 212 |
| tilted | 15 % → 16 % | 41.5 px | 0.36 | 1.06 | 134 |
| over the wet one | 31 % → 40 % | 44.1 px | 0.36 | 1.31 | 101 |
| long, no reload | 78 % → 87 % | 34.8 px | 0.36 | 1.12 | 552 | quarters: 0.40 → 0.37 → 0.32 → 0.26

Numbers say: light vs heavy: width 38.4 → 54.6 px, dark 0.32 → 0.34; wet paint spreads well beyond the stroke.

## Watercolour — glaze
Watercolour 1.00 · 38 px · 29.5 s

![Watercolour — glaze](Watercolour-glaze.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 13 % → 13 % | 36.6 px | 0.07 | 1.02 | 79 |
| heavy line | 19 % → 19 % | 55.4 px | 0.07 | 1.00 | 87 |
| pressure swell | 13 % → 13 % | 47.0 px | 0.07 | 1.02 | 68 |
| fast wave | 39 % → 40 % | 45.6 px | 0.07 | 1.01 | 207 |
| slow wave | 37 % → 37 % | 42.8 px | 0.07 | 1.01 | 334 |
| spiral | 59 % → 60 % | 38.8 px | 0.06 | 1.01 | 351 |
| loop | 33 % → 33 % | 42.6 px | 0.07 | 1.00 | 163 |
| tilted | 14 % → 14 % | 40.1 px | 0.07 | 1.00 | 118 |
| over the wet one | 30 % → 30 % | 42.3 px | 0.07 | 1.01 | 76 |
| long, no reload | 69 % → 70 % | 30.9 px | 0.06 | 1.01 | 499 | quarters: 0.06 → 0.05 → 0.03 → 0.02

Numbers say: light vs heavy: width 36.6 → 55.4 px, dark 0.07 → 0.07.

## Watercolour — granulating
Watercolour 1.00 · 44 px · 30.3 s

![Watercolour — granulating](Watercolour-granulating.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 14 % → 14 % | 41.4 px | 0.35 | 1.01 | 91 |
| heavy line | 21 % → 21 % | 60.4 px | 0.31 | 1.00 | 102 |
| pressure swell | 14 % → 14 % | 52.2 px | 0.34 | 1.01 | 75 |
| fast wave | 45 % → 45 % | 51.7 px | 0.29 | 1.01 | 233 |
| slow wave | 42 % → 42 % | 48.2 px | 0.35 | 1.01 | 383 |
| spiral | 62 % → 63 % | 41.0 px | 0.30 | 1.01 | 372 |
| loop | 37 % → 37 % | 47.6 px | 0.33 | 1.00 | 211 |
| tilted | 16 % → 16 % | 45.5 px | 0.36 | 1.00 | 142 |
| over the wet one | 33 % → 33 % | 46.2 px | 0.36 | 1.01 | 96 |
| long, no reload | 75 % → 76 % | 33.6 px | 0.29 | 1.01 | 564 | quarters: 0.34 → 0.26 → 0.20 → 0.14

Numbers say: light vs heavy: width 41.4 → 60.4 px, dark 0.35 → 0.31.

## Watercolour — dry brush
Watercolour 1.00 · 36 px · 25.0 s

![Watercolour — dry brush](Watercolour-dry-brush.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 10 % → 10 % | 27.9 px | 0.17 | 1.01 | 86 |
| heavy line | 14 % → 13 % | 39.9 px | 0.16 | 0.93 | 112 |
| pressure swell | 11 % → 11 % | 40.3 px | 0.16 | 0.98 | 76 |
| fast wave | 27 % → 20 % | 30.7 px | 0.13 | 0.74 | 214 |
| slow wave | 24 % → 17 % | 28.0 px | 0.14 | 0.71 | 414 |
| spiral | 34 % → 20 % | 22.4 px | 0.13 | 0.58 | 398 |
| loop | 21 % → 18 % | 27.1 px | 0.14 | 0.86 | 221 |
| tilted | 10 % → 10 % | 28.5 px | 0.17 | 1.00 | 106 |
| over the wet one | 21 % → 20 % | 31.3 px | 0.17 | 0.95 | 115 |
| long, no reload | 36 % → 19 % | 16.0 px | 0.14 | 0.54 | 615 | quarters: 0.09 → 0.03 → 0.01 → 0.00

Numbers say: light vs heavy: width 27.9 → 39.9 px, dark 0.17 → 0.16.

## Gouache
Gouache 1.00 · 30 px · 27.0 s

![Gouache](Gouache.png)

A light paint: laid on a grey sheet (on white it cannot be seen); **dark** = how far it is from the grey either way.

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 8 % → 4 % | 23.8 px | 0.28 | 0.49 | 69 |
| heavy line | 13 % → 4 % | 36.9 px | 0.28 | 0.33 | 82 |
| pressure swell | 10 % → 4 % | 36.7 px | 0.28 | 0.42 | 58 |
| fast wave | 24 % → 5 % | 27.4 px | 0.28 | 0.21 | 311 |
| slow wave | 24 % → 6 % | 27.5 px | 0.28 | 0.25 | 344 |
| spiral | 32 % → 6 % | 21.3 px | 0.28 | 0.18 | 352 |
| loop | 20 % → 6 % | 25.8 px | 0.28 | 0.30 | 168 |
| tilted | 9 % → 9 % | 25.0 px | 0.27 | 1.01 | 111 |
| over the wet one | 20 % → 10 % | 29.5 px | 0.27 | 0.52 | 78 |
| long, no reload | 34 % → 7 % | 15.1 px | 0.27 | 0.22 | 460 | quarters: 0.01 → 0.01 → 0.02 → 0.02

Numbers say: light vs heavy: width 23.8 → 36.9 px, dark 0.28 → 0.28; the long stroke does not run out of paint.

## Oil — alla prima
Oil 0.89 · Oil glaze 0.11 · 30 px · 12.8 s

![Oil — alla prima](Oil-alla-prima.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 9 % → 9 % | 26.4 px | 0.50 | 1.00 | 75 |
| heavy line | 9 % → 9 % | 27.4 px | 0.49 | 1.00 | 86 |
| pressure swell | 8 % → 8 % | 28.7 px | 0.50 | 1.00 | 78 |
| fast wave | 22 % → 22 % | 24.9 px | 0.47 | 1.00 | 215 |
| slow wave | 23 % → 23 % | 26.8 px | 0.50 | 1.00 | 370 |
| spiral | 36 % → 36 % | 23.8 px | 0.49 | 1.00 | 371 |
| loop | 19 % → 19 % | 25.2 px | 0.50 | 1.00 | 189 |
| tilted | 11 % → 11 % | 29.8 px | 0.50 | 1.00 | 103 |
| over the wet one | 20 % → 20 % | 25.0 px | 0.50 | 1.00 | 83 |
| long, no reload | 42 % → 42 % | 19.0 px | 0.47 | 1.00 | 524 | quarters: 0.29 → 0.23 → 0.21 → 0.17

Numbers say: light vs heavy: width 26.4 → 27.4 px, dark 0.50 → 0.49; pressure barely changes the width.

## Oil — impasto
Oil heavy 1.00 · 34 px · 17.5 s

![Oil — impasto](Oil-impasto.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 11 % → 11 % | 30.5 px | 0.23 | 1.00 | 93 |
| heavy line | 12 % → 12 % | 34.5 px | 0.23 | 1.00 | 110 |
| pressure swell | 9 % → 9 % | 34.4 px | 0.24 | 1.00 | 85 |
| fast wave | 27 % → 27 % | 30.8 px | 0.22 | 1.00 | 276 |
| slow wave | 30 % → 30 % | 34.5 px | 0.22 | 1.00 | 454 |
| spiral | 44 % → 44 % | 29.1 px | 0.21 | 1.00 | 431 |
| loop | 24 % → 24 % | 31.5 px | 0.22 | 1.00 | 237 |
| tilted | 12 % → 12 % | 32.6 px | 0.24 | 1.00 | 131 |
| over the wet one | 23 % → 23 % | 30.4 px | 0.24 | 1.00 | 108 |
| long, no reload | 49 % → 49 % | 22.0 px | 0.21 | 1.00 | 628 | quarters: 0.16 → 0.12 → 0.09 → 0.07

Numbers say: light vs heavy: width 30.5 → 34.5 px, dark 0.23 → 0.23.

## Oil — glaze
Oil glaze 1.00 · 40 px · 14.1 s

![Oil — glaze](Oil-glaze.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 9 % → 9 % | 27.0 px | 0.50 | 1.00 | 93 |
| heavy line | 13 % → 13 % | 38.3 px | 0.49 | 1.00 | 109 |
| pressure swell | 10 % → 10 % | 36.6 px | 0.50 | 1.00 | 73 |
| fast wave | 29 % → 29 % | 33.5 px | 0.49 | 1.00 | 242 |
| slow wave | 30 % → 30 % | 34.6 px | 0.50 | 1.00 | 432 |
| spiral | 46 % → 46 % | 30.1 px | 0.49 | 1.00 | 451 |
| loop | 24 % → 24 % | 31.4 px | 0.50 | 1.00 | 219 |
| tilted | 11 % → 11 % | 30.4 px | 0.50 | 1.00 | 122 |
| over the wet one | 23 % → 23 % | 32.5 px | 0.50 | 1.00 | 103 |
| long, no reload | 52 % → 52 % | 23.5 px | 0.49 | 1.00 | 636 | quarters: 0.34 → 0.30 → 0.27 → 0.22

Numbers say: light vs heavy: width 27.0 → 38.3 px, dark 0.50 → 0.49.

## Oil — scumble
Oil 1.00 · 36 px · 13.6 s

![Oil — scumble](Oil-scumble.png)

A light paint: laid on a grey sheet (on white it cannot be seen); **dark** = how far it is from the grey either way.

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 9 % → 9 % | 25.5 px | 0.25 | 1.00 | 106 |
| heavy line | 9 % → 9 % | 25.5 px | 0.24 | 1.00 | 113 |
| pressure swell | 8 % → 8 % | 29.6 px | 0.23 | 1.00 | 89 |
| fast wave | 17 % → 17 % | 19.9 px | 0.16 | 1.00 | 294 |
| slow wave | 21 % → 21 % | 24.1 px | 0.18 | 1.00 | 511 |
| spiral | 28 % → 28 % | 18.8 px | 0.14 | 1.00 | 484 |
| loop | 17 % → 17 % | 22.0 px | 0.20 | 1.00 | 246 |
| tilted | 10 % → 10 % | 27.8 px | 0.24 | 1.00 | 144 |
| over the wet one | 19 % → 19 % | 25.1 px | 0.24 | 1.00 | 134 |
| long, no reload | 30 % → 30 % | 13.3 px | 0.13 | 1.00 | 729 | quarters: 0.00 → 0.00 → 0.00 → 0.00

Numbers say: light vs heavy: width 25.5 → 25.5 px, dark 0.25 → 0.24; pressure barely changes the width.

## Acrylic — heavy body
Impasto 0.98 · 30 px · 13.5 s

![Acrylic — heavy body](Acrylic-heavy-body.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 9 % → 7 % | 26.7 px | 0.51 | 0.80 | 82 |
| heavy line | 10 % → 8 % | 29.1 px | 0.51 | 0.81 | 88 |
| pressure swell | 8 % → 7 % | 29.1 px | 0.53 | 0.88 | 66 |
| fast wave | 20 % → 11 % | 22.9 px | 0.52 | 0.57 | 232 |
| slow wave | 21 % → 14 % | 24.7 px | 0.52 | 0.65 | 368 |
| spiral | 30 % → 13 % | 19.6 px | 0.52 | 0.45 | 449 |
| loop | 18 % → 12 % | 23.5 px | 0.52 | 0.66 | 181 |
| tilted | 8 % → 8 % | 22.4 px | 0.52 | 0.99 | 105 |
| over the wet one | 17 % → 15 % | 25.8 px | 0.52 | 0.86 | 88 |
| long, no reload | 30 % → 16 % | 13.4 px | 0.52 | 0.52 | 507 | quarters: 0.25 → 0.14 → 0.09 → 0.07

Numbers say: light vs heavy: width 26.7 → 29.1 px, dark 0.51 → 0.51; pressure barely changes the width.

## Acrylic — fluid
Watercolour 1.00 · 36 px · 29.2 s

![Acrylic — fluid](Acrylic-fluid.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 12 % → 12 % | 34.8 px | 0.24 | 1.01 | 70 |
| heavy line | 18 % → 18 % | 52.6 px | 0.21 | 0.99 | 84 |
| pressure swell | 12 % → 12 % | 45.4 px | 0.23 | 1.00 | 60 |
| fast wave | 38 % → 38 % | 44.1 px | 0.19 | 0.98 | 190 |
| slow wave | 35 % → 35 % | 40.5 px | 0.22 | 1.00 | 325 |
| spiral | 55 % → 53 % | 36.0 px | 0.19 | 0.98 | 339 |
| loop | 31 % → 31 % | 40.2 px | 0.21 | 1.00 | 171 |
| tilted | 12 % → 12 % | 34.2 px | 0.24 | 1.00 | 114 |
| over the wet one | 27 % → 28 % | 42.3 px | 0.24 | 1.02 | 81 |
| long, no reload | 61 % → 58 % | 27.6 px | 0.19 | 0.95 | 469 | quarters: 0.20 → 0.14 → 0.09 → 0.06

Numbers say: light vs heavy: width 34.8 → 52.6 px, dark 0.24 → 0.21.

## Acrylic — palette knife
Impasto 1.00 · 42 px · 17.7 s

![Acrylic — palette knife](Acrylic-palette-knife.png)

A light paint: laid on a grey sheet (on white it cannot be seen); **dark** = how far it is from the grey either way.

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 15 % → 15 % | 44.0 px | 0.39 | 0.98 | 33 |
| heavy line | 15 % → 15 % | 44.2 px | 0.40 | 0.98 | 37 |
| pressure swell | 12 % → 11 % | 43.5 px | 0.42 | 0.99 | 13 |
| fast wave | 36 % → 20 % | 41.9 px | 0.37 | 0.55 | 65 |
| slow wave | 37 % → 21 % | 42.7 px | 0.37 | 0.57 | 107 |
| spiral | 47 % → 18 % | 30.7 px | 0.37 | 0.39 | 121 |
| loop | 32 % → 24 % | 41.2 px | 0.36 | 0.77 | 69 |
| tilted | 12 % → 12 % | 33.6 px | 0.39 | 1.00 | 33 |
| over the wet one | 26 % → 25 % | 39.8 px | 0.39 | 0.97 | 30 |
| long, no reload | 53 % → 20 % | 23.6 px | 0.35 | 0.38 | 156 | quarters: 0.00 → 0.00 → 0.00 → 0.01

Numbers say: light vs heavy: width 44.0 → 44.2 px, dark 0.39 → 0.40; pressure barely changes the width; the long stroke does not run out of paint.

## Finger on oil
Oil 1.00 · 30 px · 11.7 s

![Finger on oil](Finger-on-oil.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 6 % → 6 % | 16.4 px | 0.36 | 1.00 | 39 |
| heavy line | 9 % → 9 % | 24.7 px | 0.32 | 1.00 | 59 |
| pressure swell | 6 % → 6 % | 22.3 px | 0.38 | 1.00 | 41 |
| fast wave | 11 % → 11 % | 12.5 px | 0.27 | 1.00 | 102 |
| slow wave | 15 % → 15 % | 17.7 px | 0.31 | 1.00 | 197 |
| spiral | 20 % → 20 % | 13.1 px | 0.27 | 1.00 | 196 |
| loop | 13 % → 13 % | 16.9 px | 0.31 | 1.00 | 99 |
| tilted | 9 % → 9 % | 23.8 px | 0.34 | 1.00 | 83 |
| over the wet one | 16 % → 16 % | 20.4 px | 0.34 | 1.00 | 46 |
| long, no reload | 23 % → 23 % | 10.4 px | 0.26 | 1.00 | 284 | quarters: 0.15 → 0.06 → 0.03 → 0.02

Numbers say: light vs heavy: width 16.4 → 24.7 px, dark 0.36 → 0.32.

## Palette knife — oil
Oil heavy 0.93 · Impasto 0.07 · 44 px · 16.9 s

![Palette knife — oil](Palette-knife-oil.png)

A light paint: laid on a grey sheet (on white it cannot be seen); **dark** = how far it is from the grey either way.

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 16 % → 14 % | 45.7 px | 0.37 | 0.90 | 35 |
| heavy line | 16 % → 16 % | 46.3 px | 0.38 | 0.98 | 36 |
| pressure swell | 12 % → 12 % | 45.2 px | 0.38 | 0.99 | 10 |
| fast wave | 39 % → 34 % | 44.9 px | 0.35 | 0.89 | 67 |
| slow wave | 39 % → 36 % | 45.4 px | 0.35 | 0.91 | 125 |
| spiral | 62 % → 37 % | 40.7 px | 0.35 | 0.60 | 128 |
| loop | 34 % → 31 % | 43.7 px | 0.36 | 0.92 | 69 |
| tilted | 13 % → 13 % | 36.6 px | 0.37 | 1.00 | 29 |
| over the wet one | 28 % → 27 % | 40.8 px | 0.37 | 0.97 | 30 |
| long, no reload | 74 % → 39 % | 33.0 px | 0.34 | 0.53 | 151 | quarters: 0.00 → 0.00 → 0.01 → 0.01

Numbers say: light vs heavy: width 45.7 → 46.3 px, dark 0.37 → 0.38; pressure barely changes the width; the long stroke does not run out of paint.

## 0.45 · Sponge
Watercolour 0.93 · Ink 0.07 · 46 px · 31.2 s

![0.45 · Sponge](0-45-Sponge.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 27 % → 25 % | 78.2 px | 0.12 | 0.95 | 46 |
| heavy line | 32 % → 29 % | 91.9 px | 0.12 | 0.92 | 71 |
| pressure swell | 24 % → 21 % | 90.6 px | 0.12 | 0.88 | 51 |
| fast wave | 59 % → 55 % | 68.5 px | 0.12 | 0.92 | 148 |
| slow wave | 61 % → 58 % | 70.4 px | 0.17 | 0.95 | 268 |
| spiral | 77 % → 75 % | 50.7 px | 0.16 | 0.97 | 273 |
| loop | 53 % → 51 % | 69.1 px | 0.14 | 0.95 | 143 |
| tilted | 18 % → 18 % | 50.7 px | 0.17 | 1.00 | 95 |
| over the wet one | 45 % → 42 % | 73.6 px | 0.17 | 0.94 | 65 |
| long, no reload | 94 % → 89 % | 42.0 px | 0.17 | 0.95 | 416 | quarters: 0.17 → 0.18 → 0.16 → 0.14

Numbers say: light vs heavy: width 78.2 → 91.9 px, dark 0.12 → 0.12.

## 0.45 · Eraser
Watercolour 1.00 · 30 px · 18.4 s · over bands of wet oil paint and oil pastel in turn (it works on paint already there: look at what it does to the bands; covered counts the bands too)

![0.45 · Eraser](0-45-Eraser.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 24 % → 24 % | 69.2 px | 0.82 | 1.00 | 35 |
| heavy line | 23 % → 23 % | 67.4 px | 0.81 | 1.00 | 48 |
| pressure swell | 23 % → 23 % | 86.8 px | 0.82 | 1.00 | 33 |
| fast wave | 21 % → 21 % | 24.7 px | 0.81 | 1.00 | 125 |
| slow wave | 20 % → 20 % | 23.5 px | 0.82 | 1.00 | 184 |
| spiral | 20 % → 20 % | 13.5 px | 0.79 | 1.00 | 210 |
| loop | 21 % → 21 % | 27.8 px | 0.80 | 1.00 | 81 |
| tilted | 23 % → 23 % | 64.8 px | 0.81 | 1.00 | 51 |
| over the wet one | 22 % → 22 % | 0.0 px | 0.81 | 1.00 | 42 |
| long, no reload | 17 % → 17 % | 7.5 px | 0.79 | 1.00 | 261 | quarters: 0.13 → 0.16 → 0.13 → 0.17

Numbers say: light vs heavy: width 69.2 → 67.4 px, dark 0.82 → 0.81; pressure barely changes the width; the long stroke does not run out of paint.

## Lift wet paint
Watercolour 1.00 · 30 px · 18.2 s · over bands of wet oil paint and oil pastel in turn (it works on paint already there: look at what it does to the bands; covered counts the bands too)

![Lift wet paint](Lift-wet-paint.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 24 % → 24 % | 70.1 px | 0.82 | 1.00 | 32 |
| heavy line | 24 % → 24 % | 69.8 px | 0.82 | 1.00 | 39 |
| pressure swell | 24 % → 24 % | 89.6 px | 0.82 | 1.00 | 30 |
| fast wave | 24 % → 24 % | 27.7 px | 0.82 | 1.00 | 86 |
| slow wave | 24 % → 24 % | 27.7 px | 0.82 | 1.00 | 146 |
| spiral | 24 % → 24 % | 15.9 px | 0.82 | 1.00 | 155 |
| loop | 24 % → 24 % | 31.1 px | 0.82 | 1.00 | 84 |
| tilted | 24 % → 24 % | 66.8 px | 0.82 | 1.00 | 45 |
| over the wet one | 24 % → 24 % | 0.0 px | 0.82 | 1.00 | 47 |
| long, no reload | 24 % → 24 % | 10.7 px | 0.82 | 1.00 | 227 | quarters: 0.18 → 0.24 → 0.17 → 0.24

Numbers say: light vs heavy: width 70.1 → 69.8 px, dark 0.82 → 0.82; pressure barely changes the width; the long stroke does not run out of paint.

## Sgraffito
Watercolour 1.00 · 10 px · 18.4 s · over bands of wet oil paint and oil pastel in turn (it works on paint already there: look at what it does to the bands; covered counts the bands too)

![Sgraffito](Sgraffito.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 24 % → 24 % | 69.9 px | 0.81 | 1.00 | 11 |
| heavy line | 24 % → 24 % | 69.8 px | 0.82 | 1.00 | 5 |
| pressure swell | 24 % → 24 % | 89.6 px | 0.82 | 1.00 | 3 |
| fast wave | 24 % → 24 % | 27.7 px | 0.82 | 1.00 | 15 |
| slow wave | 24 % → 24 % | 27.7 px | 0.82 | 1.00 | 19 |
| spiral | 24 % → 24 % | 15.9 px | 0.82 | 1.00 | 34 |
| loop | 24 % → 24 % | 31.1 px | 0.82 | 1.00 | 19 |
| tilted | 24 % → 24 % | 66.9 px | 0.82 | 1.00 | 10 |
| over the wet one | 24 % → 24 % | 0.0 px | 0.82 | 1.00 | 8 |
| long, no reload | 24 % → 24 % | 10.6 px | 0.82 | 1.00 | 45 | quarters: 0.17 → 0.24 → 0.17 → 0.24

Numbers say: light vs heavy: width 69.9 → 69.8 px, dark 0.81 → 0.82; pressure barely changes the width; the long stroke does not run out of paint.

## Brush Artist · Refs · #01 Henry Ward peach cloud
Gouache 1.00 · 44 px · 30.3 s

![Brush Artist · Refs · #01 Henry Ward peach cloud](Brush-Artist-Refs-01-Henry-Ward-peach-cloud.png)

A light paint: laid on a grey sheet (on white it cannot be seen); **dark** = how far it is from the grey either way.

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 14 % → 6 % | 39.4 px | 0.34 | 0.45 | 109 |
| heavy line | 14 % → 8 % | 41.4 px | 0.34 | 0.58 | 139 |
| pressure swell | 10 % → 8 % | 38.0 px | 0.34 | 0.77 | 97 |
| fast wave | 28 % → 4 % | 32.5 px | 0.34 | 0.16 | 305 |
| slow wave | 30 % → 10 % | 34.7 px | 0.34 | 0.33 | 564 |
| spiral | 39 % → 8 % | 25.9 px | 0.34 | 0.21 | 495 |
| loop | 26 % → 8 % | 33.7 px | 0.34 | 0.32 | 291 |
| tilted | 12 % → 12 % | 34.2 px | 0.34 | 0.97 | 154 |
| over the wet one | 25 % → 15 % | 34.9 px | 0.34 | 0.60 | 137 |
| long, no reload | 27 % → 12 % | 12.1 px | 0.33 | 0.44 | 679 | quarters: 0.01 → 0.03 → 0.03 → 0.03

Numbers say: light vs heavy: width 39.4 → 41.4 px, dark 0.34 → 0.34; pressure barely changes the width; the long stroke does not run out of paint.

## Brush Artist · Refs · #02 Henry Ward cream strokes
Gouache 1.00 · 46 px · 29.9 s

![Brush Artist · Refs · #02 Henry Ward cream strokes](Brush-Artist-Refs-02-Henry-Ward-cream-strokes.png)

A light paint: laid on a grey sheet (on white it cannot be seen); **dark** = how far it is from the grey either way.

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 10 % → 4 % | 29.4 px | 0.42 | 0.44 | 115 |
| heavy line | 12 % → 6 % | 35.0 px | 0.42 | 0.48 | 127 |
| pressure swell | 9 % → 6 % | 33.6 px | 0.43 | 0.65 | 92 |
| fast wave | 23 % → 3 % | 26.4 px | 0.42 | 0.14 | 285 |
| slow wave | 26 % → 9 % | 30.0 px | 0.42 | 0.35 | 567 |
| spiral | 31 % → 6 % | 20.5 px | 0.42 | 0.20 | 543 |
| loop | 23 % → 7 % | 29.6 px | 0.42 | 0.29 | 286 |
| tilted | 12 % → 12 % | 34.7 px | 0.42 | 0.99 | 160 |
| over the wet one | 23 % → 11 % | 30.0 px | 0.42 | 0.50 | 131 |
| long, no reload | 25 % → 9 % | 11.0 px | 0.42 | 0.37 | 704 | quarters: 0.01 → 0.02 → 0.03 → 0.03

Numbers say: light vs heavy: width 29.4 → 35.0 px, dark 0.42 → 0.42; the long stroke does not run out of paint.

## Brush Artist · Refs · #03 Henry Ward navy contours
Impasto 1.00 · 22 px · 12.6 s

![Brush Artist · Refs · #03 Henry Ward navy contours](Brush-Artist-Refs-03-Henry-Ward-navy-contours.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 7 % → 6 % | 19.4 px | 0.69 | 0.90 | 64 |
| heavy line | 7 % → 7 % | 21.1 px | 0.69 | 0.91 | 66 |
| pressure swell | 5 % → 5 % | 20.5 px | 0.74 | 0.91 | 54 |
| fast wave | 16 % → 11 % | 18.6 px | 0.73 | 0.71 | 166 |
| slow wave | 17 % → 12 % | 19.5 px | 0.73 | 0.74 | 267 |
| spiral | 25 % → 13 % | 16.3 px | 0.73 | 0.51 | 311 |
| loop | 14 % → 12 % | 18.6 px | 0.72 | 0.81 | 149 |
| tilted | 8 % → 8 % | 22.6 px | 0.72 | 1.00 | 87 |
| over the wet one | 15 % → 13 % | 19.0 px | 0.72 | 0.87 | 74 |
| long, no reload | 30 % → 13 % | 13.4 px | 0.73 | 0.42 | 428 | quarters: 0.31 → 0.25 → 0.19 → 0.11

Numbers say: light vs heavy: width 19.4 → 21.1 px, dark 0.69 → 0.69; pressure barely changes the width.

## Brush Artist · Refs · #04 Henry Ward grey cloud
Gouache 1.00 · 50 px · 32.9 s

![Brush Artist · Refs · #04 Henry Ward grey cloud](Brush-Artist-Refs-04-Henry-Ward-grey-cloud.png)

A light paint: laid on a grey sheet (on white it cannot be seen); **dark** = how far it is from the grey either way.

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 10 % → 7 % | 29.4 px | 0.34 | 0.71 | 129 |
| heavy line | 12 % → 8 % | 34.1 px | 0.34 | 0.65 | 137 |
| pressure swell | 10 % → 6 % | 36.0 px | 0.34 | 0.64 | 102 |
| fast wave | 19 % → 8 % | 22.4 px | 0.34 | 0.41 | 341 |
| slow wave | 27 % → 12 % | 30.8 px | 0.34 | 0.45 | 614 |
| spiral | 25 % → 11 % | 16.7 px | 0.34 | 0.42 | 570 |
| loop | 20 % → 11 % | 25.5 px | 0.34 | 0.56 | 324 |
| tilted | 12 % → 12 % | 33.9 px | 0.34 | 0.99 | 211 |
| over the wet one | 23 % → 17 % | 29.0 px | 0.34 | 0.76 | 157 |
| long, no reload | 29 % → 13 % | 12.9 px | 0.34 | 0.44 | 942 | quarters: 0.01 → 0.02 → 0.02 → 0.02

Numbers say: light vs heavy: width 29.4 → 34.1 px, dark 0.34 → 0.34; the long stroke does not run out of paint.

## Brush Artist · Refs · #05 Henry Ward green in rust loops
Impasto 1.00 · 20 px · 12.8 s

![Brush Artist · Refs · #05 Henry Ward green in rust loops](Brush-Artist-Refs-05-Henry-Ward-green-in-rust-loops.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 7 % → 6 % | 18.9 px | 0.55 | 0.91 | 68 |
| heavy line | 7 % → 7 % | 20.7 px | 0.55 | 0.93 | 65 |
| pressure swell | 6 % → 5 % | 20.9 px | 0.57 | 0.91 | 53 |
| fast wave | 16 % → 11 % | 18.8 px | 0.56 | 0.69 | 178 |
| slow wave | 17 % → 12 % | 19.7 px | 0.56 | 0.69 | 245 |
| spiral | 25 % → 12 % | 16.8 px | 0.56 | 0.47 | 303 |
| loop | 14 % → 12 % | 18.8 px | 0.56 | 0.82 | 169 |
| tilted | 8 % → 8 % | 21.8 px | 0.55 | 0.99 | 94 |
| over the wet one | 14 % → 13 % | 18.6 px | 0.55 | 0.88 | 72 |
| long, no reload | 30 % → 12 % | 13.3 px | 0.56 | 0.41 | 441 | quarters: 0.24 → 0.18 → 0.11 → 0.04

Numbers say: light vs heavy: width 18.9 → 20.7 px, dark 0.55 → 0.55; pressure barely changes the width.

## Brush Artist · Refs · #06 Henry Ward scrubbed grey
Gouache 1.00 · 50 px · 33.4 s

![Brush Artist · Refs · #06 Henry Ward scrubbed grey](Brush-Artist-Refs-06-Henry-Ward-scrubbed-grey.png)

A light paint: laid on a grey sheet (on white it cannot be seen); **dark** = how far it is from the grey either way.

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 10 % → 7 % | 29.4 px | 0.35 | 0.71 | 131 |
| heavy line | 12 % → 8 % | 34.1 px | 0.35 | 0.65 | 153 |
| pressure swell | 10 % → 6 % | 36.0 px | 0.36 | 0.64 | 155 |
| fast wave | 19 % → 8 % | 22.4 px | 0.35 | 0.41 | 349 |
| slow wave | 27 % → 12 % | 30.8 px | 0.35 | 0.45 | 673 |
| spiral | 25 % → 11 % | 16.7 px | 0.35 | 0.42 | 608 |
| loop | 20 % → 11 % | 25.5 px | 0.35 | 0.56 | 332 |
| tilted | 12 % → 12 % | 33.9 px | 0.35 | 0.99 | 176 |
| over the wet one | 23 % → 17 % | 29.0 px | 0.35 | 0.76 | 134 |
| long, no reload | 29 % → 13 % | 12.9 px | 0.35 | 0.44 | 854 | quarters: 0.01 → 0.02 → 0.02 → 0.02

Numbers say: light vs heavy: width 29.4 → 34.1 px, dark 0.35 → 0.35; the long stroke does not run out of paint.

## Brush Artist · Refs · #07 Henry Ward blue L + black zigzag
Impasto 1.00 · 34 px · 15.1 s

![Brush Artist · Refs · #07 Henry Ward blue L + black zigzag](Brush-Artist-Refs-07-Henry-Ward-blue-L-black-zigzag.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 11 % → 9 % | 31.5 px | 0.57 | 0.87 | 93 |
| heavy line | 12 % → 10 % | 33.7 px | 0.57 | 0.89 | 122 |
| pressure swell | 9 % → 8 % | 33.3 px | 0.60 | 0.90 | 71 |
| fast wave | 26 % → 19 % | 30.6 px | 0.59 | 0.71 | 306 |
| slow wave | 27 % → 20 % | 31.5 px | 0.59 | 0.74 | 502 |
| spiral | 41 % → 21 % | 27.3 px | 0.59 | 0.52 | 427 |
| loop | 23 % → 18 % | 30.2 px | 0.59 | 0.78 | 231 |
| tilted | 11 % → 11 % | 30.2 px | 0.58 | 1.00 | 110 |
| over the wet one | 22 % → 19 % | 29.8 px | 0.58 | 0.89 | 108 |
| long, no reload | 48 % → 22 % | 21.4 px | 0.59 | 0.46 | 615 | quarters: 0.37 → 0.28 → 0.21 → 0.12

Numbers say: light vs heavy: width 31.5 → 33.7 px, dark 0.57 → 0.57; pressure barely changes the width.

## Brush Artist · Refs · #08 Henry Ward olive bands
Gouache 1.00 · 34 px · 22.3 s

![Brush Artist · Refs · #08 Henry Ward olive bands](Brush-Artist-Refs-08-Henry-Ward-olive-bands.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 4 % → 0 % | 10.7 px | 0.61 | 0.09 | 59 |
| heavy line | 7 % → 1 % | 21.4 px | 0.61 | 0.07 | 147 |
| pressure swell | 5 % → 1 % | 20.4 px | 0.61 | 0.16 | 55 |
| fast wave | 10 % → 1 % | 11.7 px | 0.61 | 0.08 | 217 |
| slow wave | 15 % → 1 % | 17.1 px | 0.61 | 0.09 | 498 |
| spiral | 21 % → 1 % | 13.6 px | 0.61 | 0.04 | 439 |
| loop | 13 % → 2 % | 17.3 px | 0.61 | 0.12 | 205 |
| tilted | 7 % → 7 % | 20.7 px | 0.61 | 0.97 | 114 |
| over the wet one | 14 % → 3 % | 18.8 px | 0.61 | 0.24 | 100 |
| long, no reload | 21 % → 2 % | 9.6 px | 0.61 | 0.07 | 579 | quarters: 0.24 → 0.14 → 0.08 → 0.06

Numbers say: light vs heavy: width 10.7 → 21.4 px, dark 0.61 → 0.61.

## Brush Artist · Refs · #09 Henry Ward white loops
Gouache 1.00 · 46 px · 31.0 s

![Brush Artist · Refs · #09 Henry Ward white loops](Brush-Artist-Refs-09-Henry-Ward-white-loops.png)

A light paint: laid on a grey sheet (on white it cannot be seen); **dark** = how far it is from the grey either way.

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 10 % → 4 % | 29.4 px | 0.45 | 0.44 | 122 |
| heavy line | 12 % → 6 % | 35.0 px | 0.45 | 0.48 | 135 |
| pressure swell | 9 % → 6 % | 33.6 px | 0.45 | 0.65 | 110 |
| fast wave | 23 % → 3 % | 26.4 px | 0.45 | 0.14 | 286 |
| slow wave | 26 % → 9 % | 30.0 px | 0.44 | 0.35 | 575 |
| spiral | 31 % → 6 % | 20.5 px | 0.44 | 0.20 | 550 |
| loop | 23 % → 7 % | 29.6 px | 0.44 | 0.29 | 281 |
| tilted | 12 % → 12 % | 34.7 px | 0.45 | 0.99 | 167 |
| over the wet one | 23 % → 11 % | 30.0 px | 0.45 | 0.50 | 152 |
| long, no reload | 25 % → 9 % | 11.0 px | 0.44 | 0.37 | 668 | quarters: 0.01 → 0.02 → 0.03 → 0.03

Numbers say: light vs heavy: width 29.4 → 35.0 px, dark 0.45 → 0.45; the long stroke does not run out of paint.

## Brush Artist · Refs · #10 Henry Ward maroon loops
Impasto 1.00 · 30 px · 14.1 s

![Brush Artist · Refs · #10 Henry Ward maroon loops](Brush-Artist-Refs-10-Henry-Ward-maroon-loops.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 9 % → 8 % | 26.6 px | 0.70 | 0.91 | 78 |
| heavy line | 10 % → 9 % | 28.7 px | 0.70 | 0.93 | 80 |
| pressure swell | 8 % → 7 % | 28.3 px | 0.74 | 0.92 | 66 |
| fast wave | 23 % → 16 % | 26.2 px | 0.73 | 0.72 | 235 |
| slow wave | 24 % → 18 % | 27.4 px | 0.73 | 0.76 | 357 |
| spiral | 36 % → 18 % | 23.6 px | 0.73 | 0.52 | 363 |
| loop | 20 % → 17 % | 26.0 px | 0.73 | 0.83 | 195 |
| tilted | 10 % → 10 % | 28.0 px | 0.72 | 1.00 | 103 |
| over the wet one | 19 % → 17 % | 25.5 px | 0.72 | 0.91 | 85 |
| long, no reload | 42 % → 19 % | 19.0 px | 0.73 | 0.44 | 521 | quarters: 0.42 → 0.35 → 0.29 → 0.22

Numbers say: light vs heavy: width 26.6 → 28.7 px, dark 0.70 → 0.70; pressure barely changes the width.

## Brush Artist · Refs · #11 Henry Ward purple spun balls
Impasto 1.00 · 36 px · 15.8 s

![Brush Artist · Refs · #11 Henry Ward purple spun balls](Brush-Artist-Refs-11-Henry-Ward-purple-spun-balls.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 11 % → 11 % | 32.8 px | 0.70 | 0.93 | 98 |
| heavy line | 12 % → 11 % | 34.9 px | 0.70 | 0.94 | 108 |
| pressure swell | 9 % → 9 % | 35.0 px | 0.75 | 0.94 | 82 |
| fast wave | 27 % → 22 % | 31.5 px | 0.75 | 0.80 | 245 |
| slow wave | 28 % → 23 % | 32.8 px | 0.75 | 0.82 | 444 |
| spiral | 44 % → 25 % | 29.1 px | 0.74 | 0.56 | 435 |
| loop | 24 % → 21 % | 31.2 px | 0.74 | 0.87 | 223 |
| tilted | 11 % → 11 % | 30.2 px | 0.73 | 1.00 | 120 |
| over the wet one | 22 % → 20 % | 31.0 px | 0.73 | 0.92 | 106 |
| long, no reload | 50 % → 25 % | 22.6 px | 0.75 | 0.49 | 632 | quarters: 0.50 → 0.42 → 0.36 → 0.28

Numbers say: light vs heavy: width 32.8 → 34.9 px, dark 0.70 → 0.70; pressure barely changes the width.

## Brush Artist · Refs · #12 Henry Ward black-olive cage
Gouache 1.00 · 28 px · 22.7 s

![Brush Artist · Refs · #12 Henry Ward black-olive cage](Brush-Artist-Refs-12-Henry-Ward-black-olive-cage.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 4 % → 0 % | 11.3 px | 0.64 | 0.09 | 52 |
| heavy line | 7 % → 1 % | 18.9 px | 0.64 | 0.08 | 119 |
| pressure swell | 5 % → 1 % | 17.5 px | 0.64 | 0.17 | 58 |
| fast wave | 9 % → 1 % | 10.5 px | 0.64 | 0.12 | 181 |
| slow wave | 13 % → 1 % | 15.0 px | 0.64 | 0.09 | 311 |
| spiral | 19 % → 1 % | 12.4 px | 0.64 | 0.06 | 343 |
| loop | 12 % → 2 % | 14.9 px | 0.64 | 0.14 | 179 |
| tilted | 6 % → 6 % | 17.9 px | 0.64 | 0.96 | 86 |
| over the wet one | 12 % → 3 % | 16.6 px | 0.64 | 0.26 | 165 |
| long, no reload | 20 % → 2 % | 9.0 px | 0.64 | 0.08 | 505 | quarters: 0.23 → 0.14 → 0.09 → 0.07

Numbers say: light vs heavy: width 11.3 → 18.9 px, dark 0.64 → 0.64.

## Brush Artist · Refs · #13 Henry Ward blue streaky form
Gouache 1.00 · 50 px · 33.5 s

![Brush Artist · Refs · #13 Henry Ward blue streaky form](Brush-Artist-Refs-13-Henry-Ward-blue-streaky-form.png)

A light paint: laid on a grey sheet (on white it cannot be seen); **dark** = how far it is from the grey either way.

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 10 % → 7 % | 29.4 px | 0.35 | 0.71 | 130 |
| heavy line | 12 % → 8 % | 34.1 px | 0.35 | 0.65 | 139 |
| pressure swell | 10 % → 6 % | 36.0 px | 0.35 | 0.64 | 99 |
| fast wave | 19 % → 8 % | 22.4 px | 0.35 | 0.41 | 347 |
| slow wave | 27 % → 12 % | 30.8 px | 0.35 | 0.45 | 619 |
| spiral | 25 % → 11 % | 16.7 px | 0.35 | 0.42 | 605 |
| loop | 20 % → 11 % | 25.5 px | 0.35 | 0.56 | 320 |
| tilted | 12 % → 12 % | 33.9 px | 0.35 | 0.99 | 206 |
| over the wet one | 23 % → 17 % | 29.0 px | 0.35 | 0.76 | 304 |
| long, no reload | 29 % → 13 % | 12.9 px | 0.35 | 0.44 | 939 | quarters: 0.01 → 0.02 → 0.02 → 0.02

Numbers say: light vs heavy: width 29.4 → 34.1 px, dark 0.35 → 0.35; the long stroke does not run out of paint.

## Brush Artist · Refs · #14 Henry Ward olive totem
Impasto 1.00 · 48 px · 18.5 s

![Brush Artist · Refs · #14 Henry Ward olive totem](Brush-Artist-Refs-14-Henry-Ward-olive-totem.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 15 % → 14 % | 44.1 px | 0.30 | 0.93 | 153 |
| heavy line | 16 % → 15 % | 46.7 px | 0.30 | 0.94 | 141 |
| pressure swell | 12 % → 12 % | 46.2 px | 0.32 | 0.95 | 102 |
| fast wave | 37 % → 30 % | 43.1 px | 0.30 | 0.80 | 401 |
| slow wave | 38 % → 31 % | 44.4 px | 0.30 | 0.82 | 578 |
| spiral | 55 % → 31 % | 36.4 px | 0.30 | 0.57 | 635 |
| loop | 32 % → 28 % | 42.0 px | 0.30 | 0.88 | 322 |
| tilted | 13 % → 13 % | 37.2 px | 0.31 | 1.00 | 173 |
| over the wet one | 28 % → 26 % | 40.5 px | 0.31 | 0.93 | 242 |
| long, no reload | 66 % → 33 % | 29.4 px | 0.30 | 0.51 | 814 | quarters: 0.25 → 0.18 → 0.10 → 0.05

Numbers say: light vs heavy: width 44.1 → 46.7 px, dark 0.30 → 0.30; pressure barely changes the width.

## Brush Artist · Refs · #15 Ultramarine brush script
Ink 1.00 · 4 px · 22.5 s

![Brush Artist · Refs · #15 Ultramarine brush script](Brush-Artist-Refs-15-Ultramarine-brush-script.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 1 % → 3 % | 2.2 px | 0.55 | 3.90 | 40 |
| heavy line | 6 % → 6 % | 16.7 px | 0.58 | 0.99 | 40 |
| pressure swell | 3 % → 4 % | 12.1 px | 0.64 | 1.15 | 32 |
| fast wave | 9 % → 7 % | 10.6 px | 0.54 | 0.81 | 105 |
| slow wave | 7 % → 7 % | 8.4 px | 0.54 | 0.93 | 66 |
| spiral | 11 % → 7 % | 7.2 px | 0.52 | 0.66 | 195 |
| loop | 7 % → 7 % | 9.2 px | 0.53 | 0.98 | 75 |
| tilted | 3 % → 3 % | 8.2 px | 0.62 | 1.02 | 51 |
| over the wet one | 7 % → 7 % | 11.5 px | 0.62 | 1.06 | 24 |
| long, no reload | 16 % → 8 % | 7.3 px | 0.50 | 0.48 | 229 | quarters: 0.15 → 0.04 → 0.01 → 0.00

Numbers say: light vs heavy: width 2.2 → 16.7 px, dark 0.55 → 0.58; wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #18 Blue oil-stick scribbles
Pastel 1.00 · 10 px · 10.3 s

![Brush Artist · Refs · #18 Blue oil-stick scribbles](Brush-Artist-Refs-18-Blue-oil-stick-scribbles.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 1 % → 1 % | 2.9 px | 0.52 | 1.00 | 26 |
| heavy line | 2 % → 2 % | 5.5 px | 0.53 | 1.00 | 21 |
| pressure swell | 1 % → 1 % | 5.0 px | 0.53 | 1.00 | 13 |
| fast wave | 4 % → 4 % | 4.8 px | 0.53 | 1.00 | 73 |
| slow wave | 4 % → 4 % | 4.4 px | 0.53 | 1.00 | 48 |
| spiral | 7 % → 7 % | 4.5 px | 0.52 | 1.00 | 84 |
| loop | 3 % → 3 % | 4.5 px | 0.52 | 1.00 | 50 |
| tilted | 2 % → 2 % | 4.8 px | 0.53 | 1.00 | 25 |
| over the wet one | 3 % → 3 % | 4.7 px | 0.53 | 1.00 | 21 |
| long, no reload | 10 % → 10 % | 4.4 px | 0.53 | 1.00 | 177 | quarters: 0.06 → 0.06 → 0.06 → 0.06

Numbers say: light vs heavy: width 2.9 → 5.5 px, dark 0.52 → 0.53; the long stroke does not run out of paint.

## Brush Artist · Refs · #20 Orange-red crayon scribble
Pastel 1.00 · 14 px · 10.5 s

![Brush Artist · Refs · #20 Orange-red crayon scribble](Brush-Artist-Refs-20-Orange-red-crayon-scribble.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 1 % → 1 % | 4.0 px | 0.53 | 1.00 | 12 |
| heavy line | 3 % → 3 % | 8.0 px | 0.53 | 1.00 | 27 |
| pressure swell | 2 % → 2 % | 7.6 px | 0.53 | 1.00 | 13 |
| fast wave | 6 % → 6 % | 7.2 px | 0.53 | 1.00 | 56 |
| slow wave | 6 % → 6 % | 6.6 px | 0.53 | 1.00 | 76 |
| spiral | 9 % → 9 % | 6.2 px | 0.53 | 1.00 | 107 |
| loop | 5 % → 5 % | 6.2 px | 0.53 | 1.00 | 65 |
| tilted | 2 % → 2 % | 5.6 px | 0.53 | 1.00 | 25 |
| over the wet one | 4 % → 4 % | 6.6 px | 0.53 | 1.00 | 21 |
| long, no reload | 13 % → 13 % | 5.7 px | 0.53 | 1.00 | 169 | quarters: 0.07 → 0.07 → 0.08 → 0.08

Numbers say: light vs heavy: width 4.0 → 8.0 px, dark 0.53 → 0.53; the long stroke does not run out of paint.

## Brush Artist · Refs · #21 Gritty black contours
Gouache 1.00 · 12 px · 17.1 s

![Brush Artist · Refs · #21 Gritty black contours](Brush-Artist-Refs-21-Gritty-black-contours.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 1 % → 0 % | 2.8 px | 0.81 | 0.02 | 70 |
| heavy line | 2 % → 0 % | 6.1 px | 0.00 | 0.00 | 85 |
| pressure swell | 2 % → 0 % | 6.2 px | 0.81 | 0.03 | 67 |
| fast wave | 2 % → 0 % | 2.3 px | 0.00 | 0.00 | 206 |
| slow wave | 4 % → 0 % | 4.1 px | 0.81 | 0.02 | 176 |
| spiral | 4 % → 0 % | 2.9 px | 0.81 | 0.01 | 363 |
| loop | 3 % → 0 % | 4.3 px | 0.81 | 0.01 | 192 |
| tilted | 3 % → 2 % | 7.1 px | 0.81 | 0.89 | 81 |
| over the wet one | 4 % → 0 % | 5.1 px | 0.81 | 0.04 | 87 |
| long, no reload | 5 % → 0 % | 2.2 px | 0.81 | 0.01 | 477 | quarters: 0.10 → 0.04 → 0.03 → 0.02

Numbers say: light vs heavy: width 2.8 → 6.1 px, dark 0.81 → 0.00.

## Brush Artist · Refs · #22 Bold black brush poster
Ink 1.00 · 20 px · 26.5 s

![Brush Artist · Refs · #22 Bold black brush poster](Brush-Artist-Refs-22-Bold-black-brush-poster.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 3 % → 5 % | 9.6 px | 0.79 | 1.64 | 38 |
| heavy line | 15 % → 15 % | 44.6 px | 0.88 | 0.99 | 94 |
| pressure swell | 9 % → 9 % | 31.9 px | 0.87 | 1.04 | 50 |
| fast wave | 27 % → 27 % | 31.7 px | 0.87 | 0.98 | 166 |
| slow wave | 22 % → 22 % | 25.3 px | 0.87 | 0.99 | 329 |
| spiral | 34 % → 32 % | 22.4 px | 0.87 | 0.94 | 255 |
| loop | 20 % → 20 % | 26.3 px | 0.88 | 1.00 | 189 |
| tilted | 8 % → 8 % | 23.1 px | 0.88 | 1.01 | 74 |
| over the wet one | 19 % → 19 % | 30.3 px | 0.88 | 1.00 | 59 |
| long, no reload | 45 % → 38 % | 20.3 px | 0.86 | 0.83 | 374 | quarters: 0.54 → 0.45 → 0.35 → 0.26

Numbers say: light vs heavy: width 9.6 → 44.6 px, dark 0.79 → 0.88; wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #23 Dry white on orange + black line
Gouache 1.00 · 50 px · 21.5 s

![Brush Artist · Refs · #23 Dry white on orange + black line](Brush-Artist-Refs-23-Dry-white-on-orange-black-line.png)

A light paint: laid on a grey sheet (on white it cannot be seen); **dark** = how far it is from the grey either way.

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 6 % → 0 % | 17.3 px | 0.00 | 0.00 | 108 |
| heavy line | 10 % → 0 % | 29.7 px | 0.41 | 0.00 | 228 |
| pressure swell | 7 % → 0 % | 27.2 px | 0.41 | 0.02 | 111 |
| fast wave | 13 % → 0 % | 15.3 px | 0.41 | 0.01 | 375 |
| slow wave | 20 % → 0 % | 22.8 px | 0.40 | 0.02 | 605 |
| spiral | 23 % → 0 % | 15.4 px | 0.40 | 0.01 | 614 |
| loop | 17 % → 0 % | 22.5 px | 0.40 | 0.03 | 305 |
| tilted | 9 % → 8 % | 24.0 px | 0.40 | 0.93 | 161 |
| over the wet one | 17 % → 1 % | 23.3 px | 0.40 | 0.08 | 179 |
| long, no reload | 27 % → 1 % | 12.2 px | 0.40 | 0.03 | 868 | quarters: 0.02 → 0.03 → 0.03 → 0.03

Numbers say: light vs heavy: width 17.3 → 29.7 px, dark 0.00 → 0.41; the long stroke does not run out of paint.

## Brush Artist · Refs · #24 Picasso flat oil
Oil 0.89 · Oil glaze 0.11 · 34 px · 18.2 s

![Brush Artist · Refs · #24 Picasso flat oil](Brush-Artist-Refs-24-Picasso-flat-oil.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 10 % → 10 % | 28.0 px | 0.38 | 1.00 | 125 |
| heavy line | 10 % → 10 % | 30.4 px | 0.39 | 1.00 | 104 |
| pressure swell | 8 % → 8 % | 29.5 px | 0.41 | 1.00 | 103 |
| fast wave | 25 % → 25 % | 29.0 px | 0.41 | 1.00 | 307 |
| slow wave | 27 % → 27 % | 30.6 px | 0.40 | 1.00 | 531 |
| spiral | 41 % → 41 % | 27.3 px | 0.40 | 1.00 | 514 |
| loop | 22 % → 22 % | 28.2 px | 0.40 | 1.00 | 268 |
| tilted | 11 % → 11 % | 31.3 px | 0.39 | 1.00 | 133 |
| over the wet one | 21 % → 21 % | 26.9 px | 0.39 | 1.00 | 144 |
| long, no reload | 51 % → 51 % | 22.9 px | 0.40 | 1.00 | 740 | quarters: 0.25 → 0.23 → 0.21 → 0.20

Numbers say: light vs heavy: width 28.0 → 30.4 px, dark 0.38 → 0.39; pressure barely changes the width.

## Brush Artist · Refs · #25 Yellow heavy flat stroke
Impasto 1.00 · 110 px · 32.3 s

![Brush Artist · Refs · #25 Yellow heavy flat stroke](Brush-Artist-Refs-25-Yellow-heavy-flat-stroke.png)

A light paint: laid on a grey sheet (on white it cannot be seen); **dark** = how far it is from the grey either way.

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 35 % → 36 % | 101.5 px | 0.30 | 1.02 | 504 |
| heavy line | 36 % → 35 % | 105.1 px | 0.31 | 0.97 | 447 |
| pressure swell | 28 % → 29 % | 105.5 px | 0.30 | 1.04 | 323 |
| fast wave | 73 % → 76 % | 83.8 px | 0.31 | 1.05 | 1021 |
| slow wave | 73 % → 72 % | 84.7 px | 0.30 | 0.98 | 1920 |
| spiral | 86 % → 83 % | 56.7 px | 0.29 | 0.97 | 1791 |
| loop | 65 % → 64 % | 83.6 px | 0.31 | 0.99 | 902 |
| tilted | 26 % → 26 % | 71.5 px | 0.30 | 1.00 | 490 |
| over the wet one | 55 % → 54 % | 83.2 px | 0.30 | 0.97 | 412 |
| long, no reload | 98 % → 97 % | 44.1 px | 0.30 | 0.99 | 2477 | quarters: 0.00 → 0.00 → 0.00 → 0.00

Numbers say: light vs heavy: width 101.5 → 105.1 px, dark 0.30 → 0.31; pressure barely changes the width; the long stroke does not run out of paint.

## Brush Artist · Refs · #27 Orange impasto swatch
Impasto 1.00 · 60 px · 20.2 s

![Brush Artist · Refs · #27 Orange impasto swatch](Brush-Artist-Refs-27-Orange-impasto-swatch.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 20 % → 19 % | 56.9 px | 0.34 | 0.97 | 221 |
| heavy line | 20 % → 20 % | 59.5 px | 0.34 | 0.97 | 211 |
| pressure swell | 16 % → 15 % | 59.6 px | 0.36 | 0.97 | 153 |
| fast wave | 48 % → 47 % | 55.1 px | 0.35 | 0.98 | 491 |
| slow wave | 48 % → 47 % | 55.9 px | 0.35 | 0.98 | 932 |
| spiral | 69 % → 62 % | 45.5 px | 0.34 | 0.91 | 868 |
| loop | 42 % → 40 % | 53.9 px | 0.35 | 0.97 | 403 |
| tilted | 16 % → 16 % | 44.0 px | 0.35 | 1.00 | 216 |
| over the wet one | 34 % → 33 % | 50.9 px | 0.35 | 0.96 | 189 |
| long, no reload | 85 % → 75 % | 38.1 px | 0.35 | 0.88 | 1137 | quarters: 0.33 → 0.31 → 0.30 → 0.26

Numbers say: light vs heavy: width 56.9 → 59.5 px, dark 0.34 → 0.34; pressure barely changes the width.

## Brush Artist · Refs · #28 Miles Davis black lines
Ink 1.00 · 22 px · 26.1 s

![Brush Artist · Refs · #28 Miles Davis black lines](Brush-Artist-Refs-28-Miles-Davis-black-lines.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 4 % → 6 % | 12.2 px | 0.81 | 1.49 | 35 |
| heavy line | 17 % → 17 % | 49.0 px | 0.88 | 0.99 | 99 |
| pressure swell | 10 % → 10 % | 35.9 px | 0.87 | 1.03 | 47 |
| fast wave | 31 % → 30 % | 35.4 px | 0.87 | 0.98 | 222 |
| slow wave | 25 % → 25 % | 28.7 px | 0.87 | 0.99 | 217 |
| spiral | 39 % → 37 % | 25.5 px | 0.87 | 0.95 | 226 |
| loop | 23 % → 23 % | 29.6 px | 0.88 | 1.00 | 122 |
| tilted | 9 % → 9 % | 25.3 px | 0.88 | 1.01 | 65 |
| over the wet one | 21 % → 21 % | 34.1 px | 0.88 | 1.01 | 56 |
| long, no reload | 51 % → 43 % | 22.9 px | 0.86 | 0.84 | 359 | quarters: 0.59 → 0.51 → 0.40 → 0.31

Numbers say: light vs heavy: width 12.2 → 49.0 px, dark 0.81 → 0.88.

## Brush Artist · Refs · #29 Shrigley magenta asterisk
Watercolour 1.00 · 70 px · 29.4 s

![Brush Artist · Refs · #29 Shrigley magenta asterisk](Brush-Artist-Refs-29-Shrigley-magenta-asterisk.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 10 % → 13 % | 28.0 px | 0.61 | 1.39 | 64 |
| heavy line | 17 % → 18 % | 50.3 px | 0.61 | 1.04 | 132 |
| pressure swell | 11 % → 13 % | 41.1 px | 0.62 | 1.14 | 89 |
| fast wave | 38 % → 38 % | 43.8 px | 0.60 | 1.01 | 283 |
| slow wave | 35 % → 39 % | 41.0 px | 0.62 | 1.11 | 418 |
| spiral | 61 % → 61 % | 40.0 px | 0.60 | 1.01 | 421 |
| loop | 31 % → 32 % | 40.2 px | 0.61 | 1.03 | 222 |
| tilted | 18 % → 18 % | 49.0 px | 0.61 | 1.00 | 194 |
| over the wet one | 31 % → 34 % | 38.5 px | 0.61 | 1.08 | 108 |
| long, no reload | 75 % → 76 % | 33.6 px | 0.60 | 1.01 | 667 | quarters: 0.53 → 0.50 → 0.48 → 0.45

Numbers say: light vs heavy: width 28.0 → 50.3 px, dark 0.61 → 0.61; the long stroke does not run out of paint.

## Brush Artist · Refs · #30 Red gouache face patch
Gouache 1.00 · 60 px · 36.0 s

![Brush Artist · Refs · #30 Red gouache face patch](Brush-Artist-Refs-30-Red-gouache-face-patch.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 16 % → 15 % | 47.0 px | 0.49 | 0.91 | 144 |
| heavy line | 25 % → 20 % | 73.9 px | 0.49 | 0.80 | 209 |
| pressure swell | 19 % → 17 % | 72.6 px | 0.49 | 0.86 | 136 |
| fast wave | 49 % → 28 % | 56.1 px | 0.49 | 0.58 | 413 |
| slow wave | 48 % → 28 % | 55.4 px | 0.49 | 0.59 | 705 |
| spiral | 60 % → 28 % | 39.3 px | 0.49 | 0.47 | 672 |
| loop | 40 % → 29 % | 51.6 px | 0.49 | 0.74 | 354 |
| tilted | 16 % → 17 % | 46.0 px | 0.49 | 1.00 | 210 |
| over the wet one | 36 % → 32 % | 55.3 px | 0.49 | 0.89 | 165 |
| long, no reload | 67 % → 30 % | 30.0 px | 0.49 | 0.44 | 967 | quarters: 0.43 → 0.39 → 0.32 → 0.26

Numbers say: light vs heavy: width 47.0 → 73.9 px, dark 0.49 → 0.49.

## Brush Artist · Refs · #31 Warhol blotted line
Ink 1.00 · 6 px · 20.1 s

![Brush Artist · Refs · #31 Warhol blotted line](Brush-Artist-Refs-31-Warhol-blotted-line.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 1 % → 3 % | 2.7 px | 0.75 | 3.31 | 32 |
| heavy line | 7 % → 7 % | 20.7 px | 0.83 | 0.98 | 45 |
| pressure swell | 4 % → 4 % | 14.8 px | 0.84 | 1.12 | 37 |
| fast wave | 12 % → 9 % | 13.9 px | 0.82 | 0.76 | 101 |
| slow wave | 10 % → 8 % | 11.2 px | 0.80 | 0.84 | 110 |
| spiral | 15 % → 8 % | 9.7 px | 0.80 | 0.58 | 182 |
| loop | 9 % → 9 % | 11.9 px | 0.80 | 0.93 | 86 |
| tilted | 3 % → 3 % | 8.8 px | 0.84 | 1.03 | 41 |
| over the wet one | 8 % → 8 % | 14.4 px | 0.84 | 1.02 | 45 |
| long, no reload | 21 % → 9 % | 9.5 px | 0.78 | 0.43 | 273 | quarters: 0.25 → 0.13 → 0.04 → 0.01

Numbers say: light vs heavy: width 2.7 → 20.7 px, dark 0.75 → 0.83; wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #32 Thick orange swipes
Impasto 1.00 · 90 px · 28.2 s

![Brush Artist · Refs · #32 Thick orange swipes](Brush-Artist-Refs-32-Thick-orange-swipes.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 29 % → 29 % | 83.2 px | 0.37 | 1.00 | 280 |
| heavy line | 30 % → 29 % | 86.5 px | 0.38 | 0.97 | 301 |
| pressure swell | 23 % → 23 % | 86.6 px | 0.38 | 1.01 | 206 |
| fast wave | 63 % → 65 % | 73.1 px | 0.38 | 1.03 | 762 |
| slow wave | 64 % → 63 % | 73.5 px | 0.38 | 0.98 | 1286 |
| spiral | 79 % → 77 % | 52.2 px | 0.38 | 0.98 | 1255 |
| loop | 57 % → 56 % | 73.4 px | 0.38 | 0.99 | 642 |
| tilted | 21 % → 21 % | 59.3 px | 0.38 | 1.00 | 355 |
| over the wet one | 47 % → 45 % | 71.0 px | 0.38 | 0.97 | 297 |
| long, no reload | 95 % → 93 % | 42.8 px | 0.38 | 0.98 | 1757 | quarters: 0.38 → 0.38 → 0.37 → 0.35

Numbers say: light vs heavy: width 83.2 → 86.5 px, dark 0.37 → 0.38; pressure barely changes the width; the long stroke does not run out of paint.

## Brush Artist · Refs · #33 Red wet-in-wet band
Watercolour 1.00 · 80 px · 44.3 s

![Brush Artist · Refs · #33 Red wet-in-wet band](Brush-Artist-Refs-33-Red-wet-in-wet-band.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 24 % → 42 % | 69.9 px | 0.53 | 1.73 | 130 |
| heavy line | 34 % → 50 % | 97.7 px | 0.54 | 1.48 | 225 |
| pressure swell | 20 % → 30 % | 73.7 px | 0.57 | 1.54 | 135 |
| fast wave | 65 % → 80 % | 75.4 px | 0.61 | 1.22 | 444 |
| slow wave | 61 % → 78 % | 70.0 px | 0.63 | 1.29 | 757 |
| spiral | 78 % → 89 % | 51.5 px | 0.64 | 1.15 | 740 |
| loop | 54 % → 68 % | 70.2 px | 0.62 | 1.25 | 385 |
| tilted | 28 % → 30 % | 77.1 px | 0.57 | 1.08 | 276 |
| over the wet one | 55 % → 79 % | 75.2 px | 0.57 | 1.45 | 193 |
| long, no reload | 96 % → 99 % | 43.2 px | 0.66 | 1.03 | 1081 | quarters: 0.68 → 0.68 → 0.68 → 0.63

Numbers say: light vs heavy: width 69.9 → 97.7 px, dark 0.53 → 0.54; the long stroke does not run out of paint; wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #34 Magenta oil patches
Oil 0.89 · Oil glaze 0.11 · 60 px · 20.1 s

![Brush Artist · Refs · #34 Magenta oil patches](Brush-Artist-Refs-34-Magenta-oil-patches.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 18 % → 18 % | 52.7 px | 0.60 | 1.01 | 178 |
| heavy line | 20 % → 20 % | 57.0 px | 0.61 | 1.00 | 207 |
| pressure swell | 15 % → 15 % | 55.7 px | 0.62 | 1.01 | 134 |
| fast wave | 48 % → 48 % | 55.0 px | 0.61 | 1.02 | 502 |
| slow wave | 48 % → 48 % | 55.7 px | 0.61 | 1.00 | 843 |
| spiral | 71 % → 71 % | 46.8 px | 0.61 | 1.00 | 854 |
| loop | 41 % → 41 % | 53.3 px | 0.61 | 1.00 | 437 |
| tilted | 16 % → 16 % | 46.0 px | 0.60 | 1.00 | 248 |
| over the wet one | 34 % → 34 % | 47.8 px | 0.60 | 1.00 | 215 |
| long, no reload | 83 % → 83 % | 37.1 px | 0.61 | 1.00 | 1200 | quarters: 0.57 → 0.56 → 0.54 → 0.47

Numbers say: light vs heavy: width 52.7 → 57.0 px, dark 0.60 → 0.61; pressure barely changes the width.

## Brush Artist · Refs · #35 Red band with runs
Watercolour 1.00 · 70 px · 46.0 s

![Brush Artist · Refs · #35 Red band with runs](Brush-Artist-Refs-35-Red-band-with-runs.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 40 % → 45 % | 115.4 px | 0.42 | 1.14 | 142 |
| heavy line | 46 % → 51 % | 133.2 px | 0.42 | 1.12 | 211 |
| pressure swell | 21 % → 28 % | 77.8 px | 0.48 | 1.36 | 128 |
| fast wave | 67 % → 77 % | 77.5 px | 0.49 | 1.14 | 456 |
| slow wave | 65 % → 75 % | 75.0 px | 0.52 | 1.16 | 791 |
| spiral | 87 % → 94 % | 57.4 px | 0.53 | 1.09 | 642 |
| loop | 79 % → 88 % | 102.3 px | 0.48 | 1.11 | 344 |
| tilted | 50 % → 50 % | 138.2 px | 0.47 | 1.02 | 261 |
| over the wet one | 77 % → 84 % | 76.2 px | 0.47 | 1.10 | 166 |
| long, no reload | 97 % → 100 % | 43.5 px | 0.58 | 1.03 | 984 | quarters: 0.60 → 0.60 → 0.59 → 0.56

Numbers say: light vs heavy: width 115.4 → 133.2 px, dark 0.42 → 0.42; the long stroke does not run out of paint.

## Brush Artist · Refs · #36 Magenta letters flat brush
Gouache 1.00 · 36 px · 31.2 s

![Brush Artist · Refs · #36 Magenta letters flat brush](Brush-Artist-Refs-36-Magenta-letters-flat-brush.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 10 % → 10 % | 29.0 px | 0.45 | 0.98 | 74 |
| heavy line | 17 % → 14 % | 49.0 px | 0.45 | 0.85 | 103 |
| pressure swell | 13 % → 12 % | 49.3 px | 0.45 | 0.89 | 73 |
| fast wave | 35 % → 19 % | 40.9 px | 0.45 | 0.54 | 212 |
| slow wave | 35 % → 19 % | 40.0 px | 0.45 | 0.54 | 362 |
| spiral | 46 % → 19 % | 30.4 px | 0.45 | 0.42 | 346 |
| loop | 27 % → 20 % | 35.4 px | 0.45 | 0.72 | 180 |
| tilted | 11 % → 11 % | 30.0 px | 0.45 | 1.00 | 97 |
| over the wet one | 24 % → 23 % | 38.1 px | 0.45 | 0.93 | 83 |
| long, no reload | 46 % → 19 % | 20.8 px | 0.45 | 0.40 | 563 | quarters: 0.29 → 0.26 → 0.22 → 0.18

Numbers say: light vs heavy: width 29.0 → 49.0 px, dark 0.45 → 0.45.

## Brush Artist · Refs · #37 Oil still life dabs
Oil 0.89 · Oil glaze 0.11 · 40 px · 17.6 s

![Brush Artist · Refs · #37 Oil still life dabs](Brush-Artist-Refs-37-Oil-still-life-dabs.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 12 % → 12 % | 35.4 px | 0.36 | 1.00 | 118 |
| heavy line | 13 % → 13 % | 38.6 px | 0.36 | 1.00 | 136 |
| pressure swell | 10 % → 10 % | 37.8 px | 0.40 | 1.00 | 101 |
| fast wave | 31 % → 31 % | 36.3 px | 0.39 | 1.00 | 329 |
| slow wave | 33 % → 33 % | 38.0 px | 0.39 | 1.00 | 570 |
| spiral | 51 % → 51 % | 33.9 px | 0.38 | 1.00 | 628 |
| loop | 27 % → 27 % | 35.4 px | 0.39 | 1.00 | 344 |
| tilted | 13 % → 13 % | 35.5 px | 0.38 | 1.00 | 166 |
| over the wet one | 25 % → 25 % | 33.6 px | 0.38 | 1.00 | 158 |
| long, no reload | 61 % → 61 % | 27.2 px | 0.38 | 1.00 | 833 | quarters: 0.29 → 0.26 → 0.24 → 0.21

Numbers say: light vs heavy: width 35.4 → 38.6 px, dark 0.36 → 0.36; pressure barely changes the width.

## Brush Artist · Refs · #38 Sanguine drawing
Pastel 1.00 · 6 px · 8.9 s

![Brush Artist · Refs · #38 Sanguine drawing](Brush-Artist-Refs-38-Sanguine-drawing.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 1 % → 1 % | 2.0 px | 0.61 | 1.00 | 16 |
| heavy line | 1 % → 1 % | 3.5 px | 0.62 | 1.00 | 12 |
| pressure swell | 1 % → 1 % | 3.3 px | 0.62 | 1.00 | 12 |
| fast wave | 3 % → 3 % | 3.2 px | 0.61 | 1.00 | 37 |
| slow wave | 3 % → 3 % | 3.0 px | 0.61 | 1.00 | 63 |
| spiral | 4 % → 4 % | 2.9 px | 0.61 | 1.00 | 65 |
| loop | 2 % → 2 % | 3.0 px | 0.61 | 1.00 | 35 |
| tilted | 1 % → 1 % | 3.4 px | 0.62 | 1.00 | 12 |
| over the wet one | 2 % → 2 % | 2.9 px | 0.62 | 1.00 | 10 |
| long, no reload | 7 % → 7 % | 3.0 px | 0.61 | 1.00 | 100 | quarters: 0.04 → 0.05 → 0.05 → 0.05

Numbers say: light vs heavy: width 2.0 → 3.5 px, dark 0.61 → 0.62; the long stroke does not run out of paint.

## Brush Artist · Refs · #39 Very thick impasto
Impasto 1.00 · 60 px · 19.9 s

![Brush Artist · Refs · #39 Very thick impasto](Brush-Artist-Refs-39-Very-thick-impasto.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 20 % → 19 % | 57.0 px | 0.60 | 0.97 | 170 |
| heavy line | 21 % → 20 % | 59.6 px | 0.60 | 0.97 | 168 |
| pressure swell | 16 % → 15 % | 59.7 px | 0.63 | 0.97 | 127 |
| fast wave | 48 % → 47 % | 55.2 px | 0.62 | 0.98 | 441 |
| slow wave | 49 % → 47 % | 56.1 px | 0.62 | 0.98 | 663 |
| spiral | 69 % → 65 % | 45.6 px | 0.62 | 0.93 | 775 |
| loop | 42 % → 41 % | 54.0 px | 0.62 | 0.97 | 419 |
| tilted | 16 % → 16 % | 44.1 px | 0.61 | 1.00 | 223 |
| over the wet one | 34 % → 33 % | 51.0 px | 0.61 | 0.97 | 178 |
| long, no reload | 85 % → 79 % | 38.3 px | 0.62 | 0.93 | 1058 | quarters: 0.58 → 0.57 → 0.55 → 0.52

Numbers say: light vs heavy: width 57.0 → 59.6 px, dark 0.60 → 0.60; pressure barely changes the width; the long stroke does not run out of paint.

## Brush Artist · Refs · #40 Watercolour blooms
Watercolour 1.00 · 90 px · 45.8 s

![Brush Artist · Refs · #40 Watercolour blooms](Brush-Artist-Refs-40-Watercolour-blooms.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 27 % → 46 % | 79.5 px | 0.08 | 1.69 | 167 |
| heavy line | 39 % → 53 % | 112.7 px | 0.09 | 1.36 | 259 |
| pressure swell | 26 % → 40 % | 98.0 px | 0.09 | 1.54 | 166 |
| fast wave | 68 % → 82 % | 78.6 px | 0.11 | 1.21 | 543 |
| slow wave | 68 % → 81 % | 78.9 px | 0.15 | 1.19 | 1094 |
| spiral | 83 % → 93 % | 54.4 px | 0.15 | 1.13 | 934 |
| loop | 59 % → 72 % | 75.9 px | 0.13 | 1.24 | 494 |
| tilted | 33 % → 36 % | 93.0 px | 0.12 | 1.07 | 329 |
| over the wet one | 61 % → 81 % | 77.1 px | 0.12 | 1.33 | 225 |
| long, no reload | 98 % → 100 % | 43.9 px | 0.17 | 1.02 | 1359 | quarters: 0.21 → 0.20 → 0.17 → 0.12

Numbers say: light vs heavy: width 79.5 → 112.7 px, dark 0.08 → 0.09; wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #41 Coloured pencil hatching
Pastel 1.00 · 4 px · 8.4 s

![Brush Artist · Refs · #41 Coloured pencil hatching](Brush-Artist-Refs-41-Coloured-pencil-hatching.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 1 % → 1 % | 1.6 px | 0.42 | 1.00 | 9 |
| heavy line | 1 % → 1 % | 2.6 px | 0.43 | 1.00 | 14 |
| pressure swell | 1 % → 1 % | 2.1 px | 0.43 | 1.00 | 6 |
| fast wave | 2 % → 2 % | 2.2 px | 0.42 | 1.00 | 28 |
| slow wave | 2 % → 2 % | 2.1 px | 0.43 | 1.00 | 36 |
| spiral | 3 % → 3 % | 2.1 px | 0.43 | 1.00 | 46 |
| loop | 2 % → 2 % | 2.2 px | 0.43 | 1.00 | 25 |
| tilted | 1 % → 1 % | 3.0 px | 0.42 | 1.00 | 15 |
| over the wet one | 2 % → 2 % | 2.2 px | 0.42 | 1.00 | 15 |
| long, no reload | 5 % → 5 % | 2.3 px | 0.43 | 1.00 | 70 | quarters: 0.02 → 0.02 → 0.02 → 0.03

Numbers say: light vs heavy: width 1.6 → 2.6 px, dark 0.42 → 0.43; the long stroke does not run out of paint.

## Brush Artist · Refs · #42 Oil pastel shaggy
Pastel 1.00 · 18 px · 9.1 s

![Brush Artist · Refs · #42 Oil pastel shaggy](Brush-Artist-Refs-42-Oil-pastel-shaggy.png)

A light paint: laid on a grey sheet (on white it cannot be seen); **dark** = how far it is from the grey either way.

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 2 % → 2 % | 5.1 px | 0.35 | 1.00 | 23 |
| heavy line | 4 % → 4 % | 10.7 px | 0.36 | 1.00 | 22 |
| pressure swell | 3 % → 3 % | 9.5 px | 0.36 | 1.00 | 15 |
| fast wave | 8 % → 8 % | 9.0 px | 0.36 | 1.00 | 64 |
| slow wave | 7 % → 7 % | 8.2 px | 0.36 | 1.00 | 93 |
| spiral | 12 % → 12 % | 7.8 px | 0.36 | 1.00 | 107 |
| loop | 6 % → 6 % | 7.9 px | 0.36 | 1.00 | 59 |
| tilted | 2 % → 2 % | 6.9 px | 0.36 | 1.00 | 29 |
| over the wet one | 6 % → 6 % | 8.5 px | 0.36 | 1.00 | 26 |
| long, no reload | 15 % → 15 % | 6.9 px | 0.36 | 1.00 | 159 | quarters: 0.00 → 0.00 → 0.00 → 0.00

Numbers say: light vs heavy: width 5.1 → 10.7 px, dark 0.35 → 0.36; the long stroke does not run out of paint.

## Brush Artist · Refs · #43 Dragged black ink blocks
Gouache 1.00 · 70 px · 25.6 s

![Brush Artist · Refs · #43 Dragged black ink blocks](Brush-Artist-Refs-43-Dragged-black-ink-blocks.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 10 % → 1 % | 30.5 px | 0.65 | 0.09 | 110 |
| heavy line | 17 % → 2 % | 48.7 px | 0.65 | 0.13 | 288 |
| pressure swell | 12 % → 3 % | 44.8 px | 0.65 | 0.25 | 160 |
| fast wave | 27 % → 3 % | 30.9 px | 0.65 | 0.12 | 478 |
| slow wave | 34 % → 4 % | 38.7 px | 0.65 | 0.12 | 814 |
| spiral | 43 % → 4 % | 28.2 px | 0.65 | 0.10 | 824 |
| loop | 31 % → 4 % | 39.7 px | 0.65 | 0.14 | 434 |
| tilted | 13 % → 13 % | 37.6 px | 0.65 | 0.99 | 328 |
| over the wet one | 28 % → 10 % | 40.7 px | 0.65 | 0.37 | 330 |
| long, no reload | 48 % → 7 % | 21.6 px | 0.65 | 0.15 | 1158 | quarters: 0.49 → 0.38 → 0.30 → 0.22

Numbers say: light vs heavy: width 30.5 → 48.7 px, dark 0.65 → 0.65.

## Brush Artist · Refs · #44 Blue looping ribbon
Oil 1.00 · 80 px · 24.0 s

![Brush Artist · Refs · #44 Blue looping ribbon](Brush-Artist-Refs-44-Blue-looping-ribbon.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 25 % → 26 % | 72.8 px | 0.70 | 1.04 | 267 |
| heavy line | 27 % → 27 % | 78.1 px | 0.69 | 1.00 | 305 |
| pressure swell | 20 % → 21 % | 76.2 px | 0.72 | 1.03 | 202 |
| fast wave | 62 % → 64 % | 71.1 px | 0.72 | 1.04 | 740 |
| slow wave | 62 % → 62 % | 72.0 px | 0.73 | 1.00 | 1259 |
| spiral | 76 % → 77 % | 50.4 px | 0.72 | 1.00 | 1223 |
| loop | 55 % → 55 % | 70.7 px | 0.72 | 1.00 | 669 |
| tilted | 20 % → 20 % | 56.9 px | 0.71 | 1.00 | 521 |
| over the wet one | 43 % → 43 % | 63.7 px | 0.71 | 1.00 | 292 |
| long, no reload | 93 % → 93 % | 41.6 px | 0.73 | 1.00 | 1873 | quarters: 0.72 → 0.71 → 0.71 → 0.64

Numbers say: light vs heavy: width 72.8 → 78.1 px, dark 0.70 → 0.69; pressure barely changes the width; the long stroke does not run out of paint.

## Brush Artist · Refs · #45 Soft pastel pepper
Pastel 1.00 · 40 px · 10.0 s

![Brush Artist · Refs · #45 Soft pastel pepper](Brush-Artist-Refs-45-Soft-pastel-pepper.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 4 % → 4 % | 11.3 px | 0.53 | 1.00 | 47 |
| heavy line | 8 % → 8 % | 23.0 px | 0.53 | 1.00 | 38 |
| pressure swell | 5 % → 5 % | 19.5 px | 0.53 | 1.00 | 34 |
| fast wave | 17 % → 17 % | 19.4 px | 0.53 | 1.00 | 104 |
| slow wave | 15 % → 15 % | 17.1 px | 0.53 | 1.00 | 222 |
| spiral | 25 % → 25 % | 16.3 px | 0.53 | 1.00 | 215 |
| loop | 12 % → 12 % | 16.1 px | 0.53 | 1.00 | 102 |
| tilted | 5 % → 5 % | 12.8 px | 0.53 | 1.00 | 60 |
| over the wet one | 11 % → 11 % | 17.7 px | 0.53 | 1.00 | 47 |
| long, no reload | 30 % → 30 % | 13.6 px | 0.53 | 1.00 | 298 | quarters: 0.18 → 0.18 → 0.18 → 0.18

Numbers say: light vs heavy: width 11.3 → 23.0 px, dark 0.53 → 0.53; the long stroke does not run out of paint.

## Brush Artist · Refs · #46 Red-brown ink lips
Watercolour 1.00 · 50 px · 38.2 s

![Brush Artist · Refs · #46 Red-brown ink lips](Brush-Artist-Refs-46-Red-brown-ink-lips.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 15 % → 31 % | 43.2 px | 0.58 | 2.07 | 60 |
| heavy line | 22 % → 36 % | 62.9 px | 0.60 | 1.64 | 115 |
| pressure swell | 13 % → 22 % | 47.7 px | 0.64 | 1.71 | 66 |
| fast wave | 41 % → 64 % | 47.9 px | 0.64 | 1.55 | 221 |
| slow wave | 41 % → 63 % | 46.9 px | 0.67 | 1.54 | 464 |
| spiral | 65 % → 79 % | 42.7 px | 0.69 | 1.23 | 385 |
| loop | 37 % → 56 % | 47.7 px | 0.66 | 1.51 | 189 |
| tilted | 20 % → 23 % | 56.2 px | 0.60 | 1.12 | 154 |
| over the wet one | 41 % → 63 % | 57.1 px | 0.60 | 1.55 | 90 |
| long, no reload | 80 % → 96 % | 35.8 px | 0.70 | 1.20 | 560 | quarters: 0.71 → 0.71 → 0.70 → 0.65

Numbers say: light vs heavy: width 43.2 → 62.9 px, dark 0.58 → 0.60; the long stroke does not run out of paint; wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #47 Pink knife slabs
Impasto 1.00 · 90 px · 26.1 s

![Brush Artist · Refs · #47 Pink knife slabs](Brush-Artist-Refs-47-Pink-knife-slabs.png)

A light paint: laid on a grey sheet (on white it cannot be seen); **dark** = how far it is from the grey either way.

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 28 % → 27 % | 81.2 px | 0.29 | 0.97 | 185 |
| heavy line | 29 % → 28 % | 83.6 px | 0.29 | 0.97 | 224 |
| pressure swell | 22 % → 22 % | 83.5 px | 0.29 | 1.01 | 155 |
| fast wave | 61 % → 60 % | 70.3 px | 0.28 | 0.99 | 522 |
| slow wave | 61 % → 59 % | 71.0 px | 0.27 | 0.96 | 1215 |
| spiral | 76 % → 57 % | 50.1 px | 0.27 | 0.76 | 907 |
| loop | 55 % → 54 % | 71.7 px | 0.28 | 0.97 | 497 |
| tilted | 21 % → 21 % | 59.3 px | 0.29 | 1.00 | 280 |
| over the wet one | 46 % → 44 % | 68.1 px | 0.29 | 0.96 | 234 |
| long, no reload | 92 % → 76 % | 41.4 px | 0.26 | 0.83 | 1266 | quarters: 0.00 → 0.00 → 0.00 → 0.00

Numbers say: light vs heavy: width 81.2 → 83.6 px, dark 0.29 → 0.29; pressure barely changes the width; the long stroke does not run out of paint.

## Brush Artist · Refs · #48 Black bands with drips
Gouache 1.00 · 70 px · 41.0 s

![Brush Artist · Refs · #48 Black bands with drips](Brush-Artist-Refs-48-Black-bands-with-drips.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 27 % → 24 % | 79.0 px | 0.64 | 0.87 | 161 |
| heavy line | 35 % → 29 % | 102.8 px | 0.64 | 0.82 | 244 |
| pressure swell | 25 % → 22 % | 91.9 px | 0.64 | 0.89 | 160 |
| fast wave | 64 % → 43 % | 74.0 px | 0.64 | 0.67 | 495 |
| slow wave | 61 % → 41 % | 70.7 px | 0.64 | 0.67 | 820 |
| spiral | 69 % → 39 % | 45.7 px | 0.64 | 0.56 | 792 |
| loop | 54 % → 42 % | 70.4 px | 0.64 | 0.77 | 437 |
| tilted | 29 % → 29 % | 80.7 px | 0.64 | 1.00 | 259 |
| over the wet one | 58 % → 49 % | 80.4 px | 0.64 | 0.85 | 214 |
| long, no reload | 78 % → 39 % | 34.9 px | 0.64 | 0.50 | 1140 | quarters: 0.61 → 0.57 → 0.51 → 0.42

Numbers say: light vs heavy: width 79.0 → 102.8 px, dark 0.64 → 0.64.

## Brush Artist · Refs · #49 Magenta letters round brush
Ink 1.00 · 30 px · 28.0 s

![Brush Artist · Refs · #49 Magenta letters round brush](Brush-Artist-Refs-49-Magenta-letters-round-brush.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 6 % → 8 % | 17.4 px | 0.50 | 1.29 | 39 |
| heavy line | 21 % → 21 % | 61.9 px | 0.51 | 0.99 | 105 |
| pressure swell | 12 % → 13 % | 46.3 px | 0.52 | 1.02 | 57 |
| fast wave | 39 % → 38 % | 44.8 px | 0.51 | 0.99 | 174 |
| slow wave | 32 % → 31 % | 36.7 px | 0.51 | 0.99 | 296 |
| spiral | 50 % → 49 % | 33.2 px | 0.51 | 0.97 | 284 |
| loop | 29 % → 29 % | 37.8 px | 0.51 | 1.00 | 150 |
| tilted | 11 % → 11 % | 30.9 px | 0.52 | 1.01 | 80 |
| over the wet one | 26 % → 26 % | 42.0 px | 0.52 | 1.01 | 73 |
| long, no reload | 62 % → 56 % | 27.7 px | 0.50 | 0.91 | 439 | quarters: 0.41 → 0.36 → 0.30 → 0.25

Numbers say: light vs heavy: width 17.4 → 61.9 px, dark 0.50 → 0.51.

## Brush Artist · Refs · #50 Thick swipes on photo
Impasto 1.00 · 40 px · 16.0 s

![Brush Artist · Refs · #50 Thick swipes on photo](Brush-Artist-Refs-50-Thick-swipes-on-photo.png)

A light paint: laid on a grey sheet (on white it cannot be seen); **dark** = how far it is from the grey either way.

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 13 % → 13 % | 38.1 px | 0.27 | 0.96 | 103 |
| heavy line | 14 % → 13 % | 40.2 px | 0.27 | 0.96 | 114 |
| pressure swell | 11 % → 10 % | 40.1 px | 0.25 | 0.95 | 83 |
| fast wave | 33 % → 31 % | 38.4 px | 0.25 | 0.93 | 272 |
| slow wave | 34 % → 32 % | 39.1 px | 0.26 | 0.95 | 469 |
| spiral | 58 % → 46 % | 38.5 px | 0.25 | 0.79 | 497 |
| loop | 28 % → 27 % | 36.9 px | 0.26 | 0.95 | 266 |
| tilted | 12 % → 12 % | 34.1 px | 0.26 | 1.00 | 135 |
| over the wet one | 25 % → 24 % | 35.3 px | 0.26 | 0.95 | 118 |
| long, no reload | 66 % → 46 % | 29.5 px | 0.24 | 0.69 | 719 | quarters: 0.00 → 0.00 → 0.00 → 0.00

Numbers say: light vs heavy: width 38.1 → 40.2 px, dark 0.27 → 0.27; pressure barely changes the width; the long stroke does not run out of paint.

## Brush Artist · Refs · Drag #e8b4a8
Gouache 1.00 · 40 px · 19.8 s

![Brush Artist · Refs · Drag #e8b4a8](Brush-Artist-Refs-Drag-e8b4a8.png)

A light paint: laid on a grey sheet (on white it cannot be seen); **dark** = how far it is from the grey either way.

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 4 % → 0 % | 12.7 px | 0.35 | 0.03 | 103 |
| heavy line | 5 % → 0 % | 14.4 px | 0.34 | 0.03 | 112 |
| pressure swell | 4 % → 0 % | 15.5 px | 0.34 | 0.07 | 86 |
| fast wave | 6 % → 0 % | 6.4 px | 0.34 | 0.05 | 252 |
| slow wave | 12 % → 0 % | 13.8 px | 0.34 | 0.02 | 443 |
| spiral | 10 % → 0 % | 6.6 px | 0.34 | 0.05 | 442 |
| loop | 8 % → 1 % | 10.3 px | 0.34 | 0.09 | 235 |
| tilted | 6 % → 5 % | 16.1 px | 0.34 | 0.90 | 137 |
| over the wet one | 10 % → 1 % | 12.4 px | 0.34 | 0.15 | 118 |
| long, no reload | 9 % → 1 % | 4.0 px | 0.34 | 0.10 | 603 | quarters: 0.01 → 0.01 → 0.02 → 0.02

Numbers say: light vs heavy: width 12.7 → 14.4 px, dark 0.35 → 0.34; the long stroke does not run out of paint.

## Brush Artist · Refs · Drag #e8e4e0
Gouache 1.00 · 40 px · 19.8 s

![Brush Artist · Refs · Drag #e8e4e0](Brush-Artist-Refs-Drag-e8e4e0.png)

A light paint: laid on a grey sheet (on white it cannot be seen); **dark** = how far it is from the grey either way.

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 4 % → 0 % | 12.7 px | 0.43 | 0.03 | 99 |
| heavy line | 5 % → 0 % | 14.4 px | 0.43 | 0.03 | 105 |
| pressure swell | 4 % → 0 % | 15.5 px | 0.43 | 0.07 | 94 |
| fast wave | 6 % → 0 % | 6.4 px | 0.43 | 0.05 | 254 |
| slow wave | 12 % → 0 % | 13.8 px | 0.42 | 0.02 | 479 |
| spiral | 10 % → 0 % | 6.6 px | 0.42 | 0.05 | 437 |
| loop | 8 % → 1 % | 10.3 px | 0.42 | 0.09 | 231 |
| tilted | 6 % → 5 % | 16.1 px | 0.42 | 0.90 | 132 |
| over the wet one | 10 % → 1 % | 12.4 px | 0.42 | 0.15 | 111 |
| long, no reload | 9 % → 1 % | 4.0 px | 0.42 | 0.10 | 630 | quarters: 0.01 → 0.02 → 0.02 → 0.02

Numbers say: light vs heavy: width 12.7 → 14.4 px, dark 0.43 → 0.43; the long stroke does not run out of paint.

## Brush Artist · Refs · Finger
Pastel 1.00 · 36 px · 19.1 s · over bands of wet oil paint and oil pastel in turn (it works on paint already there: look at what it does to the bands; covered counts the bands too)

![Brush Artist · Refs · Finger](Brush-Artist-Refs-Finger.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 25 % → 25 % | 73.8 px | 0.80 | 1.00 | 43 |
| heavy line | 27 % → 27 % | 78.6 px | 0.80 | 1.00 | 56 |
| pressure swell | 26 % → 26 % | 97.7 px | 0.80 | 1.00 | 40 |
| fast wave | 32 % → 32 % | 37.3 px | 0.78 | 1.00 | 115 |
| slow wave | 31 % → 31 % | 36.3 px | 0.78 | 1.00 | 197 |
| spiral | 38 % → 38 % | 25.2 px | 0.76 | 1.00 | 205 |
| loop | 30 % → 30 % | 39.5 px | 0.78 | 1.00 | 110 |
| tilted | 26 % → 26 % | 73.4 px | 0.78 | 1.00 | 64 |
| over the wet one | 29 % → 29 % | 6.8 px | 0.78 | 1.00 | 46 |
| long, no reload | 41 % → 41 % | 18.2 px | 0.76 | 1.00 | 278 | quarters: 0.25 → 0.37 → 0.34 → 0.39

Numbers say: light vs heavy: width 73.8 → 78.6 px, dark 0.80 → 0.80; pressure barely changes the width; the long stroke does not run out of paint.

## Brush Artist · Ink — wash
Watercolour 1.00 · 38 px · 29.1 s

![Brush Artist · Ink — wash](Brush-Artist-Ink-wash.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 11 % → 11 % | 31.6 px | 0.39 | 1.04 | 53 |
| heavy line | 19 % → 19 % | 54.3 px | 0.32 | 1.03 | 92 |
| pressure swell | 12 % → 13 % | 45.2 px | 0.37 | 1.04 | 62 |
| fast wave | 39 % → 41 % | 45.5 px | 0.31 | 1.04 | 173 |
| slow wave | 37 % → 38 % | 42.9 px | 0.37 | 1.03 | 303 |
| spiral | 58 % → 61 % | 38.6 px | 0.31 | 1.04 | 293 |
| loop | 32 % → 33 % | 41.9 px | 0.35 | 1.02 | 163 |
| tilted | 13 % → 14 % | 37.0 px | 0.38 | 1.04 | 113 |
| over the wet one | 29 % → 30 % | 42.8 px | 0.38 | 1.04 | 77 |
| long, no reload | 67 % → 72 % | 30.0 px | 0.29 | 1.07 | 448 | quarters: 0.34 → 0.27 → 0.19 → 0.12

Numbers say: light vs heavy: width 31.6 → 54.3 px, dark 0.39 → 0.32.

## Brush Artist · Ink — brush line
Ink 1.00 · 16 px · 24.8 s

![Brush Artist · Ink — brush line](Brush-Artist-Ink-brush-line.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 3 % → 5 % | 7.7 px | 0.78 | 1.81 | 35 |
| heavy line | 13 % → 13 % | 38.9 px | 0.88 | 0.99 | 75 |
| pressure swell | 8 % → 8 % | 28.4 px | 0.87 | 1.05 | 52 |
| fast wave | 24 % → 23 % | 28.0 px | 0.87 | 0.96 | 137 |
| slow wave | 20 % → 19 % | 22.6 px | 0.87 | 0.97 | 170 |
| spiral | 30 % → 27 % | 20.1 px | 0.86 | 0.89 | 240 |
| loop | 18 % → 18 % | 23.6 px | 0.88 | 1.00 | 129 |
| tilted | 7 % → 7 % | 20.5 px | 0.88 | 1.01 | 55 |
| over the wet one | 17 % → 17 % | 26.8 px | 0.88 | 1.00 | 59 |
| long, no reload | 42 % → 30 % | 18.9 px | 0.85 | 0.71 | 329 | quarters: 0.49 → 0.40 → 0.30 → 0.20

Numbers say: light vs heavy: width 7.7 → 38.9 px, dark 0.78 → 0.88; wet paint spreads well beyond the stroke.

## Brush Artist · Ink — dry brush
Gouache 1.00 · 30 px · 19.4 s

![Brush Artist · Ink — dry brush](Brush-Artist-Ink-dry-brush.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 3 % → 0 % | 9.8 px | 0.00 | 0.00 | 51 |
| heavy line | 6 % → 0 % | 16.0 px | 0.77 | 0.01 | 112 |
| pressure swell | 4 % → 0 % | 15.4 px | 0.77 | 0.05 | 73 |
| fast wave | 7 % → 0 % | 8.5 px | 0.77 | 0.05 | 187 |
| slow wave | 11 % → 0 % | 12.3 px | 0.77 | 0.03 | 340 |
| spiral | 14 % → 0 % | 9.0 px | 0.77 | 0.03 | 313 |
| loop | 9 % → 1 % | 12.0 px | 0.77 | 0.05 | 182 |
| tilted | 6 % → 5 % | 15.8 px | 0.77 | 0.94 | 99 |
| over the wet one | 10 % → 1 % | 13.2 px | 0.77 | 0.14 | 136 |
| long, no reload | 15 % → 1 % | 6.6 px | 0.77 | 0.05 | 487 | quarters: 0.23 → 0.13 → 0.09 → 0.08

Numbers say: light vs heavy: width 9.8 → 16.0 px, dark 0.00 → 0.77.

## Brush Artist · Watercolour — blue
Watercolour 0.93 · Ink 0.07 · 40 px · 26.7 s

![Brush Artist · Watercolour — blue](Brush-Artist-Watercolour-blue.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 6 % → 11 % | 16.2 px | 0.29 | 1.88 | 31 |
| heavy line | 11 % → 13 % | 31.9 px | 0.29 | 1.17 | 59 |
| pressure swell | 7 % → 9 % | 25.7 px | 0.30 | 1.38 | 43 |
| fast wave | 24 % → 27 % | 28.2 px | 0.29 | 1.12 | 124 |
| slow wave | 23 % → 32 % | 26.4 px | 0.31 | 1.41 | 220 |
| spiral | 39 % → 47 % | 25.6 px | 0.29 | 1.21 | 217 |
| loop | 20 % → 25 % | 25.7 px | 0.30 | 1.25 | 108 |
| tilted | 12 % → 12 % | 34.0 px | 0.30 | 1.00 | 87 |
| over the wet one | 21 % → 25 % | 25.2 px | 0.30 | 1.19 | 52 |
| long, no reload | 53 % → 59 % | 23.6 px | 0.30 | 1.12 | 342 | quarters: 0.23 → 0.21 → 0.19 → 0.16

Numbers say: light vs heavy: width 16.2 → 31.9 px, dark 0.29 → 0.29; wet paint spreads well beyond the stroke.

## Brush Artist · Watercolour — violet
Watercolour 0.93 · Ink 0.07 · 40 px · 26.7 s

![Brush Artist · Watercolour — violet](Brush-Artist-Watercolour-violet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 6 % → 11 % | 16.2 px | 0.36 | 1.88 | 28 |
| heavy line | 11 % → 13 % | 31.9 px | 0.37 | 1.17 | 60 |
| pressure swell | 7 % → 9 % | 25.7 px | 0.38 | 1.38 | 43 |
| fast wave | 24 % → 27 % | 28.2 px | 0.38 | 1.12 | 135 |
| slow wave | 23 % → 32 % | 26.4 px | 0.39 | 1.41 | 218 |
| spiral | 39 % → 47 % | 25.6 px | 0.37 | 1.21 | 211 |
| loop | 20 % → 25 % | 25.7 px | 0.38 | 1.25 | 115 |
| tilted | 12 % → 12 % | 34.0 px | 0.38 | 1.00 | 89 |
| over the wet one | 21 % → 25 % | 25.2 px | 0.38 | 1.19 | 58 |
| long, no reload | 53 % → 59 % | 23.6 px | 0.38 | 1.12 | 381 | quarters: 0.28 → 0.27 → 0.24 → 0.21

Numbers say: light vs heavy: width 16.2 → 31.9 px, dark 0.36 → 0.37; wet paint spreads well beyond the stroke.

## Brush Artist · Watercolour — teal
Watercolour 0.93 · Ink 0.07 · 40 px · 26.4 s

![Brush Artist · Watercolour — teal](Brush-Artist-Watercolour-teal.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 6 % → 11 % | 16.2 px | 0.23 | 1.88 | 27 |
| heavy line | 11 % → 13 % | 31.9 px | 0.23 | 1.17 | 73 |
| pressure swell | 7 % → 9 % | 25.7 px | 0.24 | 1.38 | 36 |
| fast wave | 24 % → 27 % | 28.2 px | 0.23 | 1.12 | 131 |
| slow wave | 23 % → 32 % | 26.4 px | 0.25 | 1.41 | 223 |
| spiral | 39 % → 47 % | 25.6 px | 0.23 | 1.21 | 215 |
| loop | 20 % → 25 % | 25.7 px | 0.24 | 1.25 | 116 |
| tilted | 12 % → 12 % | 34.0 px | 0.24 | 1.00 | 87 |
| over the wet one | 21 % → 25 % | 25.2 px | 0.24 | 1.19 | 64 |
| long, no reload | 53 % → 59 % | 23.6 px | 0.24 | 1.12 | 338 | quarters: 0.18 → 0.16 → 0.15 → 0.13

Numbers say: light vs heavy: width 16.2 → 31.9 px, dark 0.23 → 0.23; wet paint spreads well beyond the stroke.

## Brush Artist · Gouache
Gouache 1.00 · 30 px · 28.8 s

![Brush Artist · Gouache](Brush-Artist-Gouache.png)

A light paint: laid on a grey sheet (on white it cannot be seen); **dark** = how far it is from the grey either way.

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 8 % → 8 % | 24.4 px | 0.27 | 0.97 | 68 |
| heavy line | 15 % → 12 % | 42.8 px | 0.27 | 0.78 | 80 |
| pressure swell | 11 % → 9 % | 41.0 px | 0.27 | 0.85 | 54 |
| fast wave | 30 % → 14 % | 34.9 px | 0.26 | 0.45 | 192 |
| slow wave | 29 % → 14 % | 34.0 px | 0.26 | 0.47 | 299 |
| spiral | 40 % → 14 % | 26.6 px | 0.26 | 0.35 | 298 |
| loop | 24 % → 15 % | 30.6 px | 0.26 | 0.62 | 159 |
| tilted | 10 % → 10 % | 27.4 px | 0.27 | 1.01 | 85 |
| over the wet one | 22 % → 19 % | 32.9 px | 0.27 | 0.89 | 63 |
| long, no reload | 43 % → 15 % | 19.1 px | 0.26 | 0.35 | 417 | quarters: 0.01 → 0.01 → 0.01 → 0.01

Numbers say: light vs heavy: width 24.4 → 42.8 px, dark 0.27 → 0.27; the long stroke does not run out of paint.

## Brush Artist · Oil — bristle
Oil 0.89 · Oil glaze 0.11 · 30 px · 12.9 s

![Brush Artist · Oil — bristle](Brush-Artist-Oil-bristle.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 9 % → 9 % | 26.3 px | 0.53 | 1.00 | 89 |
| heavy line | 10 % → 10 % | 28.6 px | 0.54 | 1.00 | 103 |
| pressure swell | 8 % → 8 % | 28.2 px | 0.55 | 1.00 | 113 |
| fast wave | 24 % → 24 % | 27.3 px | 0.55 | 1.00 | 319 |
| slow wave | 25 % → 25 % | 28.3 px | 0.55 | 1.00 | 437 |
| spiral | 39 % → 39 % | 25.6 px | 0.54 | 1.00 | 434 |
| loop | 20 % → 20 % | 26.3 px | 0.54 | 1.00 | 212 |
| tilted | 11 % → 11 % | 29.9 px | 0.52 | 1.00 | 128 |
| over the wet one | 20 % → 20 % | 25.5 px | 0.52 | 1.00 | 109 |
| long, no reload | 50 % → 50 % | 22.4 px | 0.54 | 1.00 | 652 | quarters: 0.32 → 0.30 → 0.29 → 0.28

Numbers say: light vs heavy: width 26.3 → 28.6 px, dark 0.53 → 0.54; pressure barely changes the width; the long stroke does not run out of paint.

## Brush Artist · Charcoal — stick
Charcoal 0.78 · Pastel 0.22 · 28 px · 9.5 s

![Brush Artist · Charcoal — stick](Brush-Artist-Charcoal-stick.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 5 % → 5 % | 15.3 px | 0.85 | 1.00 | 14 |
| heavy line | 8 % → 8 % | 23.3 px | 0.85 | 1.00 | 29 |
| pressure swell | 5 % → 5 % | 19.8 px | 0.85 | 1.00 | 25 |
| fast wave | 18 % → 18 % | 20.7 px | 0.85 | 1.00 | 71 |
| slow wave | 17 % → 17 % | 19.5 px | 0.85 | 1.00 | 100 |
| spiral | 29 % → 29 % | 19.3 px | 0.85 | 1.00 | 94 |
| loop | 15 % → 15 % | 19.3 px | 0.85 | 1.00 | 49 |
| tilted | 6 % → 6 % | 16.6 px | 0.85 | 1.00 | 37 |
| over the wet one | 13 % → 13 % | 19.8 px | 0.85 | 1.00 | 30 |
| long, no reload | 41 % → 41 % | 18.2 px | 0.85 | 1.00 | 152 | quarters: 0.38 → 0.38 → 0.38 → 0.38

Numbers say: light vs heavy: width 15.3 → 23.3 px, dark 0.85 → 0.85; the long stroke does not run out of paint.

## Brush Artist · Charcoal — stick B
Charcoal 0.78 · Pastel 0.22 · 36 px · 9.4 s

![Brush Artist · Charcoal — stick B](Brush-Artist-Charcoal-stick-B.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 7 % → 7 % | 19.8 px | 0.85 | 1.00 | 21 |
| heavy line | 10 % → 10 % | 30.4 px | 0.85 | 1.00 | 30 |
| pressure swell | 7 % → 7 % | 25.9 px | 0.85 | 1.00 | 24 |
| fast wave | 23 % → 23 % | 26.8 px | 0.85 | 1.00 | 93 |
| slow wave | 22 % → 22 % | 25.5 px | 0.85 | 1.00 | 149 |
| spiral | 38 % → 38 % | 25.4 px | 0.85 | 1.00 | 130 |
| loop | 19 % → 19 % | 25.0 px | 0.85 | 1.00 | 74 |
| tilted | 7 % → 7 % | 20.4 px | 0.85 | 1.00 | 42 |
| over the wet one | 17 % → 17 % | 25.9 px | 0.85 | 1.00 | 30 |
| long, no reload | 51 % → 51 % | 22.6 px | 0.85 | 1.00 | 223 | quarters: 0.47 → 0.47 → 0.47 → 0.47

Numbers say: light vs heavy: width 19.8 → 30.4 px, dark 0.85 → 0.85; the long stroke does not run out of paint.

## Brush Artist · Charcoal — stick C
Charcoal 0.78 · Pastel 0.22 · 22 px · 8.9 s

![Brush Artist · Charcoal — stick C](Brush-Artist-Charcoal-stick-C.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 4 % → 4 % | 12.6 px | 0.85 | 1.00 | 15 |
| heavy line | 7 % → 7 % | 19.0 px | 0.85 | 1.00 | 14 |
| pressure swell | 4 % → 4 % | 16.2 px | 0.85 | 1.00 | 13 |
| fast wave | 15 % → 15 % | 16.9 px | 0.85 | 1.00 | 44 |
| slow wave | 14 % → 14 % | 15.8 px | 0.85 | 1.00 | 80 |
| spiral | 24 % → 24 % | 15.7 px | 0.85 | 1.00 | 63 |
| loop | 12 % → 12 % | 15.9 px | 0.85 | 1.00 | 39 |
| tilted | 5 % → 5 % | 14.4 px | 0.85 | 1.00 | 24 |
| over the wet one | 11 % → 11 % | 16.1 px | 0.85 | 1.00 | 19 |
| long, no reload | 34 % → 34 % | 15.2 px | 0.85 | 1.00 | 108 | quarters: 0.32 → 0.32 → 0.32 → 0.32

Numbers say: light vs heavy: width 12.6 → 19.0 px, dark 0.85 → 0.85; the long stroke does not run out of paint.

## Oil · Henry Ward · Loaded flat
Oil 1.00 · 46 px · 18.8 s

![Oil · Henry Ward · Loaded flat](Oil-Henry-Ward-Loaded-flat.png)

A light paint: laid on a grey sheet (on white it cannot be seen); **dark** = how far it is from the grey either way.

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 12 % → 12 % | 34.0 px | 0.31 | 1.00 | 133 |
| heavy line | 12 % → 12 % | 36.0 px | 0.31 | 1.00 | 163 |
| pressure swell | 10 % → 10 % | 38.2 px | 0.29 | 1.00 | 126 |
| fast wave | 26 % → 26 % | 29.9 px | 0.22 | 1.01 | 381 |
| slow wave | 32 % → 32 % | 37.3 px | 0.25 | 1.00 | 631 |
| spiral | 41 % → 41 % | 26.8 px | 0.23 | 1.00 | 609 |
| loop | 24 % → 24 % | 30.7 px | 0.28 | 1.00 | 329 |
| tilted | 12 % → 12 % | 34.5 px | 0.30 | 1.00 | 181 |
| over the wet one | 24 % → 24 % | 31.8 px | 0.30 | 1.00 | 147 |
| long, no reload | 45 % → 45 % | 20.1 px | 0.20 | 1.00 | 871 | quarters: 0.00 → 0.00 → 0.00 → 0.00

Numbers say: light vs heavy: width 34.0 → 36.0 px, dark 0.31 → 0.31; pressure barely changes the width; the long stroke does not run out of paint.

## Oil · Henry Ward · Dry scrub
Oil 1.00 · 50 px · 17.7 s

![Oil · Henry Ward · Dry scrub](Oil-Henry-Ward-Dry-scrub.png)

A light paint: laid on a grey sheet (on white it cannot be seen); **dark** = how far it is from the grey either way.

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 9 % → 9 % | 25.9 px | 0.24 | 1.00 | 140 |
| heavy line | 12 % → 12 % | 36.3 px | 0.23 | 1.00 | 162 |
| pressure swell | 10 % → 10 % | 37.0 px | 0.22 | 1.00 | 105 |
| fast wave | 24 % → 24 % | 27.4 px | 0.11 | 1.01 | 349 |
| slow wave | 32 % → 32 % | 37.1 px | 0.16 | 1.00 | 647 |
| spiral | 37 % → 37 % | 24.2 px | 0.14 | 1.00 | 648 |
| loop | 25 % → 25 % | 32.0 px | 0.16 | 1.00 | 342 |
| tilted | 12 % → 12 % | 33.6 px | 0.23 | 1.00 | 202 |
| over the wet one | 23 % → 23 % | 31.8 px | 0.23 | 1.00 | 159 |
| long, no reload | 31 % → 31 % | 13.7 px | 0.16 | 1.00 | 856 | quarters: 0.00 → 0.00 → 0.00 → 0.00

Numbers say: light vs heavy: width 25.9 → 36.3 px, dark 0.24 → 0.23; the long stroke does not run out of paint.

## Oil · Henry Ward · Dirty contour
Oil 1.00 · 24 px · 16.9 s

![Oil · Henry Ward · Dirty contour](Oil-Henry-Ward-Dirty-contour.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 8 % → 8 % | 24.0 px | 0.74 | 1.00 | 83 |
| heavy line | 9 % → 9 % | 26.3 px | 0.75 | 1.00 | 91 |
| pressure swell | 7 % → 7 % | 26.0 px | 0.77 | 1.00 | 67 |
| fast wave | 18 % → 18 % | 21.3 px | 0.75 | 1.00 | 197 |
| slow wave | 22 % → 22 % | 25.4 px | 0.76 | 1.00 | 380 |
| spiral | 34 % → 34 % | 22.4 px | 0.71 | 1.00 | 378 |
| loop | 18 % → 18 % | 23.5 px | 0.75 | 1.00 | 211 |
| tilted | 9 % → 9 % | 25.6 px | 0.76 | 1.00 | 106 |
| over the wet one | 18 % → 18 % | 23.7 px | 0.76 | 1.00 | 93 |
| long, no reload | 38 % → 38 % | 16.9 px | 0.72 | 1.00 | 545 | quarters: 0.42 → 0.33 → 0.26 → 0.21

Numbers say: light vs heavy: width 24.0 → 26.3 px, dark 0.74 → 0.75; pressure barely changes the width.

## Oil · Henry Ward · Wet drag
Oil 1.00 · 44 px · 14.8 s

![Oil · Henry Ward · Wet drag](Oil-Henry-Ward-Wet-drag.png)

A light paint: laid on a grey sheet (on white it cannot be seen); **dark** = how far it is from the grey either way.

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 13 % → 13 % | 38.7 px | 0.26 | 1.00 | 140 |
| heavy line | 15 % → 15 % | 42.3 px | 0.27 | 1.00 | 153 |
| pressure swell | 11 % → 11 % | 41.9 px | 0.26 | 1.00 | 102 |
| fast wave | 33 % → 33 % | 37.6 px | 0.21 | 1.00 | 352 |
| slow wave | 36 % → 36 % | 41.4 px | 0.22 | 1.00 | 613 |
| spiral | 50 % → 50 % | 32.8 px | 0.19 | 1.00 | 611 |
| loop | 30 % → 30 % | 38.8 px | 0.23 | 1.00 | 328 |
| tilted | 14 % → 14 % | 37.9 px | 0.28 | 1.00 | 182 |
| over the wet one | 27 % → 27 % | 36.5 px | 0.28 | 1.00 | 150 |
| long, no reload | 58 % → 58 % | 25.9 px | 0.18 | 1.00 | 893 | quarters: 0.00 → 0.00 → 0.00 → 0.00

Numbers say: light vs heavy: width 38.7 → 42.3 px, dark 0.26 → 0.27; pressure barely changes the width; the long stroke does not run out of paint.

## Oil · Henry Ward · Thin veil
Oil 0.81 · Ink 0.19 · 56 px · 31.9 s

![Oil · Henry Ward · Thin veil](Oil-Henry-Ward-Thin-veil.png)

A light paint: laid on a grey sheet (on white it cannot be seen); **dark** = how far it is from the grey either way.

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 16 % → 16 % | 46.5 px | 0.21 | 0.98 | 155 |
| heavy line | 17 % → 17 % | 50.6 px | 0.23 | 0.98 | 186 |
| pressure swell | 14 % → 13 % | 51.4 px | 0.24 | 0.97 | 132 |
| fast wave | 34 % → 23 % | 39.0 px | 0.17 | 0.68 | 417 |
| slow wave | 46 % → 39 % | 52.6 px | 0.17 | 0.87 | 792 |
| spiral | 53 % → 37 % | 34.9 px | 0.18 | 0.70 | 742 |
| loop | 36 % → 32 % | 46.1 px | 0.18 | 0.89 | 384 |
| tilted | 16 % → 16 % | 43.5 px | 0.24 | 1.02 | 238 |
| over the wet one | 31 % → 30 % | 43.9 px | 0.24 | 0.97 | 206 |
| long, no reload | 55 % → 43 % | 24.7 px | 0.16 | 0.78 | 1116 | quarters: 0.00 → 0.01 → 0.01 → 0.00

Numbers say: light vs heavy: width 46.5 → 50.6 px, dark 0.21 → 0.23; pressure barely changes the width; the long stroke does not run out of paint.

## Oil · Henry Ward · Ground
Gouache 1.00 · 160 px · 63.9 s

![Oil · Henry Ward · Ground](Oil-Henry-Ward-Ground.png)

A light paint: laid on a grey sheet (on white it cannot be seen); **dark** = how far it is from the grey either way.

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 51 % → 47 % | 149.0 px | 0.37 | 0.92 | 638 |
| heavy line | 52 % → 48 % | 152.0 px | 0.37 | 0.91 | 756 |
| pressure swell | 43 % → 46 % | 160.0 px | 0.37 | 1.08 | 504 |
| fast wave | 84 % → 84 % | 96.8 px | 0.37 | 1.00 | 1793 |
| slow wave | 85 % → 72 % | 98.6 px | 0.37 | 0.85 | 3247 |
| spiral | 89 % → 68 % | 58.5 px | 0.36 | 0.77 | 3045 |
| loop | 76 % → 70 % | 98.3 px | 0.37 | 0.92 | 1563 |
| tilted | 38 % → 38 % | 105.4 px | 0.37 | 1.00 | 891 |
| over the wet one | 76 % → 71 % | 105.8 px | 0.37 | 0.93 | 739 |
| long, no reload | 97 % → 86 % | 43.5 px | 0.36 | 0.89 | 4377 | quarters: 0.00 → 0.00 → 0.00 → 0.00

Numbers say: light vs heavy: width 149.0 → 152.0 px, dark 0.37 → 0.37; pressure barely changes the width.

## Oil · Henry Ward · HW #02 cream over wet olive
Oil 0.81 · Ink 0.19 · 56 px · 31.2 s

![Oil · Henry Ward · HW #02 cream over wet olive](Oil-Henry-Ward-HW-02-cream-over-wet-olive.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 16 % → 16 % | 46.5 px | 0.66 | 0.98 | 164 |
| heavy line | 17 % → 17 % | 50.6 px | 0.66 | 0.98 | 175 |
| pressure swell | 14 % → 13 % | 51.4 px | 0.66 | 0.97 | 129 |
| fast wave | 34 % → 23 % | 39.0 px | 0.64 | 0.68 | 416 |
| slow wave | 46 % → 39 % | 52.6 px | 0.64 | 0.87 | 796 |
| spiral | 53 % → 37 % | 34.9 px | 0.64 | 0.70 | 679 |
| loop | 36 % → 32 % | 46.1 px | 0.65 | 0.89 | 411 |
| tilted | 16 % → 16 % | 43.5 px | 0.66 | 1.02 | 222 |
| over the wet one | 31 % → 30 % | 43.9 px | 0.66 | 0.97 | 185 |
| long, no reload | 55 % → 43 % | 24.7 px | 0.64 | 0.78 | 1085 | quarters: 0.55 → 0.38 → 0.23 → 0.16

Numbers say: light vs heavy: width 46.5 → 50.6 px, dark 0.66 → 0.66; pressure barely changes the width.

## Oil · Henry Ward · HW #04 grey arcs over ochre
Oil 1.00 · 46 px · 19.0 s

![Oil · Henry Ward · HW #04 grey arcs over ochre](Oil-Henry-Ward-HW-04-grey-arcs-over-ochre.png)

A light paint: laid on a grey sheet (on white it cannot be seen); **dark** = how far it is from the grey either way.

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 12 % → 12 % | 34.0 px | 0.24 | 1.00 | 131 |
| heavy line | 12 % → 12 % | 36.0 px | 0.24 | 1.00 | 143 |
| pressure swell | 10 % → 10 % | 38.2 px | 0.22 | 1.00 | 107 |
| fast wave | 26 % → 26 % | 29.9 px | 0.18 | 1.01 | 355 |
| slow wave | 32 % → 32 % | 37.3 px | 0.20 | 1.00 | 777 |
| spiral | 41 % → 41 % | 26.8 px | 0.19 | 1.00 | 627 |
| loop | 24 % → 24 % | 30.7 px | 0.22 | 1.00 | 345 |
| tilted | 12 % → 12 % | 34.5 px | 0.23 | 1.00 | 178 |
| over the wet one | 24 % → 24 % | 31.8 px | 0.23 | 1.00 | 150 |
| long, no reload | 45 % → 45 % | 20.1 px | 0.16 | 1.00 | 896 | quarters: 0.00 → 0.00 → 0.01 → 0.00

Numbers say: light vs heavy: width 34.0 → 36.0 px, dark 0.24 → 0.24; pressure barely changes the width; the long stroke does not run out of paint.

## Oil · Henry Ward · HW #09 white arches over wet blue-grey
Oil 1.00 · 46 px · 19.2 s

![Oil · Henry Ward · HW #09 white arches over wet blue-grey](Oil-Henry-Ward-HW-09-white-arches-over-wet-blue-grey.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 12 % → 12 % | 34.0 px | 0.40 | 1.00 | 141 |
| heavy line | 12 % → 12 % | 36.0 px | 0.40 | 1.00 | 146 |
| pressure swell | 10 % → 10 % | 38.2 px | 0.40 | 1.00 | 120 |
| fast wave | 26 % → 26 % | 29.9 px | 0.34 | 1.01 | 361 |
| slow wave | 32 % → 32 % | 37.3 px | 0.34 | 1.00 | 699 |
| spiral | 41 % → 41 % | 26.8 px | 0.33 | 1.00 | 625 |
| loop | 24 % → 24 % | 30.7 px | 0.37 | 1.00 | 308 |
| tilted | 12 % → 12 % | 34.5 px | 0.39 | 1.00 | 178 |
| over the wet one | 24 % → 24 % | 31.8 px | 0.39 | 1.00 | 143 |
| long, no reload | 45 % → 45 % | 20.1 px | 0.32 | 1.00 | 882 | quarters: 0.27 → 0.16 → 0.11 → 0.08

Numbers say: light vs heavy: width 34.0 → 36.0 px, dark 0.40 → 0.40; pressure barely changes the width.

## Oil · Henry Ward · HW #03 navy contours over wet band
Oil 1.00 · 46 px · 19.0 s

![Oil · Henry Ward · HW #03 navy contours over wet band](Oil-Henry-Ward-HW-03-navy-contours-over-wet-band.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 12 % → 12 % | 34.0 px | 0.42 | 1.00 | 134 |
| heavy line | 12 % → 12 % | 36.0 px | 0.42 | 1.00 | 142 |
| pressure swell | 10 % → 10 % | 38.2 px | 0.42 | 1.00 | 102 |
| fast wave | 26 % → 26 % | 29.9 px | 0.36 | 1.01 | 362 |
| slow wave | 32 % → 32 % | 37.3 px | 0.36 | 1.00 | 658 |
| spiral | 41 % → 41 % | 26.8 px | 0.35 | 1.00 | 624 |
| loop | 24 % → 24 % | 30.7 px | 0.39 | 1.00 | 317 |
| tilted | 12 % → 12 % | 34.5 px | 0.41 | 1.00 | 186 |
| over the wet one | 24 % → 24 % | 31.8 px | 0.41 | 1.00 | 173 |
| long, no reload | 45 % → 45 % | 20.1 px | 0.34 | 1.00 | 914 | quarters: 0.29 → 0.17 → 0.12 → 0.09

Numbers say: light vs heavy: width 34.0 → 36.0 px, dark 0.42 → 0.42; pressure barely changes the width.

## Oil · Henry Ward · Ground #2b2f1c
Gouache 1.00 · 160 px · 63.7 s

![Oil · Henry Ward · Ground #2b2f1c](Oil-Henry-Ward-Ground-2b2f1c.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 51 % → 47 % | 149.0 px | 0.52 | 0.92 | 680 |
| heavy line | 52 % → 48 % | 152.0 px | 0.52 | 0.91 | 745 |
| pressure swell | 43 % → 46 % | 160.0 px | 0.52 | 1.08 | 549 |
| fast wave | 84 % → 84 % | 96.8 px | 0.52 | 1.00 | 1796 |
| slow wave | 85 % → 72 % | 98.6 px | 0.52 | 0.85 | 3239 |
| spiral | 89 % → 68 % | 58.5 px | 0.52 | 0.77 | 3116 |
| loop | 76 % → 70 % | 98.3 px | 0.52 | 0.92 | 1700 |
| tilted | 38 % → 38 % | 105.4 px | 0.52 | 1.00 | 831 |
| over the wet one | 76 % → 71 % | 105.8 px | 0.52 | 0.93 | 715 |
| long, no reload | 97 % → 86 % | 43.5 px | 0.52 | 0.89 | 4368 | quarters: 0.52 → 0.52 → 0.51 → 0.48

Numbers say: light vs heavy: width 149.0 → 152.0 px, dark 0.52 → 0.52; pressure barely changes the width; the long stroke does not run out of paint.

## Oil · Henry Ward · Thin veil #2b3a44
Oil 0.81 · Ink 0.19 · 56 px · 31.4 s

![Oil · Henry Ward · Thin veil #2b3a44](Oil-Henry-Ward-Thin-veil-2b3a44.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 16 % → 16 % | 46.5 px | 0.66 | 0.98 | 166 |
| heavy line | 17 % → 17 % | 50.6 px | 0.66 | 0.98 | 196 |
| pressure swell | 14 % → 13 % | 51.4 px | 0.66 | 0.97 | 151 |
| fast wave | 34 % → 23 % | 39.0 px | 0.64 | 0.68 | 429 |
| slow wave | 46 % → 39 % | 52.6 px | 0.64 | 0.87 | 840 |
| spiral | 53 % → 37 % | 34.9 px | 0.64 | 0.70 | 787 |
| loop | 36 % → 32 % | 46.1 px | 0.65 | 0.89 | 418 |
| tilted | 16 % → 16 % | 43.5 px | 0.66 | 1.02 | 246 |
| over the wet one | 31 % → 30 % | 43.9 px | 0.66 | 0.97 | 205 |
| long, no reload | 55 % → 43 % | 24.7 px | 0.64 | 0.78 | 1176 | quarters: 0.55 → 0.38 → 0.23 → 0.16

Numbers say: light vs heavy: width 46.5 → 50.6 px, dark 0.66 → 0.66; pressure barely changes the width.

## Oil · Henry Ward · Loaded flat #ece6c0
Oil 1.00 · 46 px · 19.4 s

![Oil · Henry Ward · Loaded flat #ece6c0](Oil-Henry-Ward-Loaded-flat-ece6c0.png)

A light paint: laid on a grey sheet (on white it cannot be seen); **dark** = how far it is from the grey either way.

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 12 % → 12 % | 34.0 px | 0.32 | 1.00 | 148 |
| heavy line | 12 % → 12 % | 36.0 px | 0.32 | 1.00 | 142 |
| pressure swell | 10 % → 10 % | 38.2 px | 0.30 | 1.00 | 116 |
| fast wave | 26 % → 26 % | 29.9 px | 0.23 | 1.01 | 364 |
| slow wave | 32 % → 32 % | 37.3 px | 0.25 | 1.00 | 644 |
| spiral | 41 % → 41 % | 26.8 px | 0.23 | 1.00 | 647 |
| loop | 24 % → 24 % | 30.7 px | 0.28 | 1.00 | 328 |
| tilted | 12 % → 12 % | 34.5 px | 0.31 | 1.00 | 183 |
| over the wet one | 24 % → 24 % | 31.8 px | 0.31 | 1.00 | 149 |
| long, no reload | 45 % → 45 % | 20.1 px | 0.20 | 1.00 | 895 | quarters: 0.00 → 0.00 → 0.00 → 0.00

Numbers say: light vs heavy: width 34.0 → 36.0 px, dark 0.32 → 0.32; pressure barely changes the width; the long stroke does not run out of paint.

## Oil · Henry Ward · Dry scrub #ece6c0
Oil 1.00 · 50 px · 18.2 s

![Oil · Henry Ward · Dry scrub #ece6c0](Oil-Henry-Ward-Dry-scrub-ece6c0.png)

A light paint: laid on a grey sheet (on white it cannot be seen); **dark** = how far it is from the grey either way.

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 9 % → 9 % | 25.9 px | 0.25 | 1.00 | 139 |
| heavy line | 12 % → 12 % | 36.3 px | 0.24 | 1.00 | 152 |
| pressure swell | 10 % → 10 % | 37.0 px | 0.23 | 1.00 | 104 |
| fast wave | 24 % → 24 % | 27.4 px | 0.11 | 1.01 | 351 |
| slow wave | 32 % → 32 % | 37.1 px | 0.17 | 1.00 | 675 |
| spiral | 37 % → 37 % | 24.2 px | 0.14 | 1.00 | 675 |
| loop | 25 % → 25 % | 32.0 px | 0.17 | 1.00 | 334 |
| tilted | 12 % → 12 % | 33.6 px | 0.24 | 1.00 | 206 |
| over the wet one | 23 % → 23 % | 31.8 px | 0.24 | 1.00 | 159 |
| long, no reload | 31 % → 31 % | 13.7 px | 0.16 | 1.00 | 846 | quarters: 0.00 → 0.00 → 0.00 → 0.00

Numbers say: light vs heavy: width 25.9 → 36.3 px, dark 0.25 → 0.24; the long stroke does not run out of paint.

## Oil · Henry Ward · Ground #8a6a20
Gouache 1.00 · 160 px · 63.2 s

![Oil · Henry Ward · Ground #8a6a20](Oil-Henry-Ward-Ground-8a6a20.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 51 % → 47 % | 149.0 px | 0.32 | 0.92 | 648 |
| heavy line | 52 % → 48 % | 152.0 px | 0.32 | 0.91 | 721 |
| pressure swell | 43 % → 46 % | 160.0 px | 0.32 | 1.08 | 525 |
| fast wave | 84 % → 84 % | 96.8 px | 0.32 | 1.00 | 1842 |
| slow wave | 85 % → 72 % | 98.6 px | 0.32 | 0.85 | 3005 |
| spiral | 89 % → 68 % | 58.5 px | 0.32 | 0.77 | 3026 |
| loop | 76 % → 70 % | 98.3 px | 0.32 | 0.92 | 1716 |
| tilted | 38 % → 38 % | 105.4 px | 0.32 | 1.00 | 880 |
| over the wet one | 76 % → 71 % | 105.8 px | 0.32 | 0.93 | 710 |
| long, no reload | 97 % → 86 % | 43.5 px | 0.32 | 0.89 | 4416 | quarters: 0.32 → 0.32 → 0.32 → 0.28

Numbers say: light vs heavy: width 149.0 → 152.0 px, dark 0.32 → 0.32; pressure barely changes the width; the long stroke does not run out of paint.

## Oil · Henry Ward · Loaded flat #b8bcc0
Oil 1.00 · 46 px · 18.7 s

![Oil · Henry Ward · Loaded flat #b8bcc0](Oil-Henry-Ward-Loaded-flat-b8bcc0.png)

A light paint: laid on a grey sheet (on white it cannot be seen); **dark** = how far it is from the grey either way.

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 12 % → 12 % | 34.0 px | 0.24 | 1.00 | 152 |
| heavy line | 12 % → 12 % | 36.0 px | 0.24 | 1.00 | 141 |
| pressure swell | 10 % → 10 % | 38.2 px | 0.22 | 1.00 | 107 |
| fast wave | 26 % → 26 % | 29.9 px | 0.18 | 1.01 | 380 |
| slow wave | 32 % → 32 % | 37.3 px | 0.20 | 1.00 | 646 |
| spiral | 41 % → 41 % | 26.8 px | 0.19 | 1.00 | 682 |
| loop | 24 % → 24 % | 30.7 px | 0.22 | 1.00 | 317 |
| tilted | 12 % → 12 % | 34.5 px | 0.23 | 1.00 | 186 |
| over the wet one | 24 % → 24 % | 31.8 px | 0.23 | 1.00 | 148 |
| long, no reload | 45 % → 45 % | 20.1 px | 0.16 | 1.00 | 864 | quarters: 0.00 → 0.00 → 0.01 → 0.00

Numbers say: light vs heavy: width 34.0 → 36.0 px, dark 0.24 → 0.24; pressure barely changes the width; the long stroke does not run out of paint.

## Oil · Henry Ward · Dry scrub #c8ccd0
Oil 1.00 · 50 px · 17.8 s

![Oil · Henry Ward · Dry scrub #c8ccd0](Oil-Henry-Ward-Dry-scrub-c8ccd0.png)

A light paint: laid on a grey sheet (on white it cannot be seen); **dark** = how far it is from the grey either way.

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 9 % → 9 % | 25.9 px | 0.23 | 1.00 | 146 |
| heavy line | 12 % → 12 % | 36.3 px | 0.22 | 1.00 | 147 |
| pressure swell | 10 % → 10 % | 37.0 px | 0.21 | 1.00 | 105 |
| fast wave | 24 % → 24 % | 27.4 px | 0.11 | 1.01 | 359 |
| slow wave | 32 % → 32 % | 37.1 px | 0.15 | 1.00 | 634 |
| spiral | 37 % → 37 % | 24.2 px | 0.13 | 1.00 | 658 |
| loop | 25 % → 25 % | 32.0 px | 0.15 | 1.00 | 319 |
| tilted | 12 % → 12 % | 33.6 px | 0.21 | 1.00 | 199 |
| over the wet one | 23 % → 23 % | 31.8 px | 0.21 | 1.00 | 152 |
| long, no reload | 31 % → 31 % | 13.7 px | 0.15 | 1.00 | 837 | quarters: 0.00 → 0.00 → 0.00 → 0.00

Numbers say: light vs heavy: width 25.9 → 36.3 px, dark 0.23 → 0.22; the long stroke does not run out of paint.

## Oil · Henry Ward · Wet drag #9ea4aa
Oil 1.00 · 44 px · 14.8 s

![Oil · Henry Ward · Wet drag #9ea4aa](Oil-Henry-Ward-Wet-drag-9ea4aa.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 13 % → 13 % | 38.7 px | 0.21 | 1.00 | 126 |
| heavy line | 15 % → 15 % | 42.3 px | 0.22 | 1.00 | 140 |
| pressure swell | 11 % → 11 % | 41.9 px | 0.22 | 1.00 | 102 |
| fast wave | 33 % → 33 % | 37.6 px | 0.19 | 1.00 | 360 |
| slow wave | 36 % → 36 % | 41.4 px | 0.20 | 1.00 | 607 |
| spiral | 50 % → 50 % | 32.8 px | 0.17 | 1.00 | 594 |
| loop | 30 % → 30 % | 38.8 px | 0.20 | 1.00 | 326 |
| tilted | 14 % → 14 % | 37.9 px | 0.22 | 1.00 | 166 |
| over the wet one | 27 % → 27 % | 36.5 px | 0.22 | 1.00 | 149 |
| long, no reload | 58 % → 58 % | 25.9 px | 0.17 | 1.00 | 874 | quarters: 0.17 → 0.12 → 0.09 → 0.06

Numbers say: light vs heavy: width 38.7 → 42.3 px, dark 0.21 → 0.22; pressure barely changes the width.

## Oil · Henry Ward · Ground #e8b4a8
Gouache 1.00 · 160 px · 63.2 s

![Oil · Henry Ward · Ground #e8b4a8](Oil-Henry-Ward-Ground-e8b4a8.png)

A light paint: laid on a grey sheet (on white it cannot be seen); **dark** = how far it is from the grey either way.

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 51 % → 47 % | 149.0 px | 0.30 | 0.92 | 618 |
| heavy line | 52 % → 48 % | 152.0 px | 0.31 | 0.91 | 721 |
| pressure swell | 43 % → 46 % | 160.0 px | 0.31 | 1.08 | 497 |
| fast wave | 84 % → 84 % | 96.8 px | 0.31 | 1.00 | 1716 |
| slow wave | 85 % → 72 % | 98.6 px | 0.30 | 0.85 | 3519 |
| spiral | 89 % → 68 % | 58.5 px | 0.30 | 0.77 | 3101 |
| loop | 76 % → 70 % | 98.3 px | 0.31 | 0.92 | 1633 |
| tilted | 38 % → 38 % | 105.4 px | 0.31 | 1.00 | 905 |
| over the wet one | 76 % → 71 % | 105.8 px | 0.31 | 0.93 | 731 |
| long, no reload | 97 % → 86 % | 43.5 px | 0.30 | 0.89 | 4538 | quarters: 0.00 → 0.00 → 0.00 → 0.00

Numbers say: light vs heavy: width 149.0 → 152.0 px, dark 0.30 → 0.31; pressure barely changes the width.

## Oil · Henry Ward · Loaded flat #6e7f90
Oil 1.00 · 46 px · 18.6 s

![Oil · Henry Ward · Loaded flat #6e7f90](Oil-Henry-Ward-Loaded-flat-6e7f90.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 12 % → 12 % | 34.0 px | 0.40 | 1.00 | 137 |
| heavy line | 12 % → 12 % | 36.0 px | 0.40 | 1.00 | 151 |
| pressure swell | 10 % → 10 % | 38.2 px | 0.40 | 1.00 | 105 |
| fast wave | 26 % → 26 % | 29.9 px | 0.34 | 1.01 | 360 |
| slow wave | 32 % → 32 % | 37.3 px | 0.34 | 1.00 | 642 |
| spiral | 41 % → 41 % | 26.8 px | 0.33 | 1.00 | 618 |
| loop | 24 % → 24 % | 30.7 px | 0.37 | 1.00 | 308 |
| tilted | 12 % → 12 % | 34.5 px | 0.39 | 1.00 | 173 |
| over the wet one | 24 % → 24 % | 31.8 px | 0.39 | 1.00 | 149 |
| long, no reload | 45 % → 45 % | 20.1 px | 0.32 | 1.00 | 906 | quarters: 0.27 → 0.16 → 0.11 → 0.08

Numbers say: light vs heavy: width 34.0 → 36.0 px, dark 0.40 → 0.40; pressure barely changes the width.

## Oil · Henry Ward · Loaded flat #f6f6f2
Oil 1.00 · 46 px · 18.9 s

![Oil · Henry Ward · Loaded flat #f6f6f2](Oil-Henry-Ward-Loaded-flat-f6f6f2.png)

A light paint: laid on a grey sheet (on white it cannot be seen); **dark** = how far it is from the grey either way.

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 12 % → 12 % | 34.0 px | 0.33 | 1.00 | 134 |
| heavy line | 12 % → 12 % | 36.0 px | 0.34 | 1.00 | 143 |
| pressure swell | 10 % → 10 % | 38.2 px | 0.31 | 1.00 | 107 |
| fast wave | 26 % → 26 % | 29.9 px | 0.24 | 1.01 | 361 |
| slow wave | 32 % → 32 % | 37.3 px | 0.26 | 1.00 | 611 |
| spiral | 41 % → 41 % | 26.8 px | 0.24 | 1.00 | 621 |
| loop | 24 % → 24 % | 30.7 px | 0.30 | 1.00 | 301 |
| tilted | 12 % → 12 % | 34.5 px | 0.33 | 1.00 | 219 |
| over the wet one | 24 % → 24 % | 31.8 px | 0.33 | 1.00 | 159 |
| long, no reload | 45 % → 45 % | 20.1 px | 0.21 | 1.00 | 940 | quarters: 0.00 → 0.00 → 0.00 → 0.00

Numbers say: light vs heavy: width 34.0 → 36.0 px, dark 0.33 → 0.34; pressure barely changes the width; the long stroke does not run out of paint.

## Oil · Henry Ward · Dry scrub #f6f6f2
Oil 1.00 · 50 px · 17.8 s

![Oil · Henry Ward · Dry scrub #f6f6f2](Oil-Henry-Ward-Dry-scrub-f6f6f2.png)

A light paint: laid on a grey sheet (on white it cannot be seen); **dark** = how far it is from the grey either way.

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 9 % → 9 % | 25.9 px | 0.26 | 1.00 | 133 |
| heavy line | 12 % → 12 % | 36.3 px | 0.25 | 1.00 | 150 |
| pressure swell | 10 % → 10 % | 37.0 px | 0.24 | 1.00 | 113 |
| fast wave | 24 % → 24 % | 27.4 px | 0.12 | 1.01 | 377 |
| slow wave | 32 % → 32 % | 37.1 px | 0.17 | 1.00 | 687 |
| spiral | 37 % → 37 % | 24.2 px | 0.14 | 1.00 | 655 |
| loop | 25 % → 25 % | 32.0 px | 0.17 | 1.00 | 343 |
| tilted | 12 % → 12 % | 33.6 px | 0.24 | 1.00 | 205 |
| over the wet one | 23 % → 23 % | 31.8 px | 0.24 | 1.00 | 164 |
| long, no reload | 31 % → 31 % | 13.7 px | 0.17 | 1.00 | 852 | quarters: 0.00 → 0.00 → 0.00 → 0.00

Numbers say: light vs heavy: width 25.9 → 36.3 px, dark 0.26 → 0.25; the long stroke does not run out of paint.

## Oil · Henry Ward · Ground #e8e2da
Gouache 1.00 · 160 px · 62.1 s

![Oil · Henry Ward · Ground #e8e2da](Oil-Henry-Ward-Ground-e8e2da.png)

A light paint: laid on a grey sheet (on white it cannot be seen); **dark** = how far it is from the grey either way.

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 51 % → 47 % | 149.0 px | 0.38 | 0.92 | 673 |
| heavy line | 52 % → 48 % | 152.0 px | 0.38 | 0.91 | 770 |
| pressure swell | 43 % → 46 % | 160.0 px | 0.38 | 1.08 | 530 |
| fast wave | 84 % → 84 % | 96.8 px | 0.38 | 1.00 | 1791 |
| slow wave | 85 % → 72 % | 98.6 px | 0.38 | 0.85 | 3148 |
| spiral | 89 % → 68 % | 58.5 px | 0.37 | 0.77 | 3130 |
| loop | 76 % → 70 % | 98.3 px | 0.38 | 0.92 | 1699 |
| tilted | 38 % → 38 % | 105.4 px | 0.38 | 1.00 | 894 |
| over the wet one | 76 % → 71 % | 105.8 px | 0.38 | 0.93 | 742 |
| long, no reload | 97 % → 86 % | 43.5 px | 0.37 | 0.89 | 4193 | quarters: 0.00 → 0.00 → 0.00 → 0.00

Numbers say: light vs heavy: width 149.0 → 152.0 px, dark 0.38 → 0.38; pressure barely changes the width.

## Oil · Henry Ward · Loaded flat #6a7a80
Oil 1.00 · 46 px · 18.8 s

![Oil · Henry Ward · Loaded flat #6a7a80](Oil-Henry-Ward-Loaded-flat-6a7a80.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 12 % → 12 % | 34.0 px | 0.42 | 1.00 | 147 |
| heavy line | 12 % → 12 % | 36.0 px | 0.42 | 1.00 | 148 |
| pressure swell | 10 % → 10 % | 38.2 px | 0.42 | 1.00 | 110 |
| fast wave | 26 % → 26 % | 29.9 px | 0.36 | 1.01 | 369 |
| slow wave | 32 % → 32 % | 37.3 px | 0.36 | 1.00 | 660 |
| spiral | 41 % → 41 % | 26.8 px | 0.35 | 1.00 | 638 |
| loop | 24 % → 24 % | 30.7 px | 0.39 | 1.00 | 325 |
| tilted | 12 % → 12 % | 34.5 px | 0.41 | 1.00 | 178 |
| over the wet one | 24 % → 24 % | 31.8 px | 0.41 | 1.00 | 145 |
| long, no reload | 45 % → 45 % | 20.1 px | 0.34 | 1.00 | 860 | quarters: 0.29 → 0.17 → 0.12 → 0.09

Numbers say: light vs heavy: width 34.0 → 36.0 px, dark 0.42 → 0.42; pressure barely changes the width.

## Oil · Henry Ward · Loaded flat #5a1810
Oil 1.00 · 46 px · 19.0 s

![Oil · Henry Ward · Loaded flat #5a1810](Oil-Henry-Ward-Loaded-flat-5a1810.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 12 % → 12 % | 34.0 px | 0.76 | 1.00 | 128 |
| heavy line | 12 % → 12 % | 36.0 px | 0.76 | 1.00 | 146 |
| pressure swell | 10 % → 10 % | 38.2 px | 0.77 | 1.00 | 111 |
| fast wave | 26 % → 26 % | 29.9 px | 0.75 | 1.01 | 376 |
| slow wave | 32 % → 32 % | 37.3 px | 0.74 | 1.00 | 648 |
| spiral | 41 % → 41 % | 26.8 px | 0.74 | 1.00 | 635 |
| loop | 24 % → 24 % | 30.7 px | 0.76 | 1.00 | 314 |
| tilted | 12 % → 12 % | 34.5 px | 0.76 | 1.00 | 186 |
| over the wet one | 24 % → 24 % | 31.8 px | 0.76 | 1.00 | 163 |
| long, no reload | 45 % → 45 % | 20.1 px | 0.74 | 1.00 | 920 | quarters: 0.52 → 0.39 → 0.31 → 0.25

Numbers say: light vs heavy: width 34.0 → 36.0 px, dark 0.76 → 0.76; pressure barely changes the width.

## Oil · Henry Ward · Dirty contour #1c2240
Oil 1.00 · 24 px · 17.0 s

![Oil · Henry Ward · Dirty contour #1c2240](Oil-Henry-Ward-Dirty-contour-1c2240.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 8 % → 8 % | 24.0 px | 0.74 | 1.00 | 83 |
| heavy line | 9 % → 9 % | 26.3 px | 0.75 | 1.00 | 97 |
| pressure swell | 7 % → 7 % | 26.0 px | 0.77 | 1.00 | 62 |
| fast wave | 18 % → 18 % | 21.3 px | 0.75 | 1.00 | 213 |
| slow wave | 22 % → 22 % | 25.4 px | 0.76 | 1.00 | 369 |
| spiral | 34 % → 34 % | 22.4 px | 0.71 | 1.00 | 379 |
| loop | 18 % → 18 % | 23.5 px | 0.75 | 1.00 | 215 |
| tilted | 9 % → 9 % | 25.6 px | 0.76 | 1.00 | 106 |
| over the wet one | 18 % → 18 % | 23.7 px | 0.76 | 1.00 | 99 |
| long, no reload | 38 % → 38 % | 16.9 px | 0.72 | 1.00 | 581 | quarters: 0.42 → 0.33 → 0.26 → 0.21

Numbers say: light vs heavy: width 24.0 → 26.3 px, dark 0.74 → 0.75; pressure barely changes the width.

## Brush Artist · Refs · #01 Henry Ward peach cloud — own sheet
own sheet 600 × 600 · Gouache 1.00 · 44 px · 13.1 s

![Brush Artist · Refs · #01 Henry Ward peach cloud — own sheet](Brush-Artist-Refs-01-Henry-Ward-peach-cloud-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 13 % → 32 % | 36.6 px | 0.57 | 2.51 | 136 |
| stroke 2 | 21 % → 49 % | 70.5 px | 0.57 | 2.28 | 126 |
| stroke 3 | 25 % → 46 % | 72.9 px | 0.57 | 1.84 | 125 |
| stroke 4 | 26 % → 50 % | 85.4 px | 0.57 | 1.90 | 139 |
| stroke 5 | 26 % → 46 % | 75.4 px | 0.57 | 1.78 | 143 |
| stroke 6 | 26 % → 35 % | 80.3 px | 0.57 | 1.33 | 127 |
| stroke 7 | 15 % → 53 % | 37.9 px | 0.57 | 3.47 | 139 |
| stroke 8 | 18 % → 49 % | 45.5 px | 0.57 | 2.72 | 153 |
| stroke 9 | 21 % → 50 % | 54.8 px | 0.57 | 2.36 | 139 |
| stroke 10 | 23 % → 51 % | 62.1 px | 0.57 | 2.20 | 140 |
| stroke 11 | 26 % → 54 % | 72.3 px | 0.57 | 2.10 | 148 |
| stroke 12 | 29 % → 56 % | 86.7 px | 0.57 | 1.95 | 133 |
| stroke 13 | 37 % → 59 % | 108.1 px | 0.57 | 1.58 | 139 |
| stroke 14 | 40 % → 61 % | 114.5 px | 0.57 | 1.52 | 151 |
| stroke 15 | 53 % → 67 % | 156.1 px | 0.57 | 1.27 | 150 |
| stroke 16 | 55 % → 68 % | 166.0 px | 0.57 | 1.23 | 139 |
| stroke 17 | 56 % → 69 % | 157.1 px | 0.57 | 1.23 | 141 |
| stroke 18 | 57 % → 68 % | 165.7 px | 0.57 | 1.18 | 133 |
| stroke 19 | 59 % → 66 % | 164.5 px | 0.57 | 1.13 | 136 |
| stroke 20 | 58 % → 63 % | 167.9 px | 0.57 | 1.09 | 144 |
| stroke 21 | 58 % → 60 % | 168.2 px | 0.57 | 1.04 | 138 |
| stroke 22 | 59 % → 61 % | 173.0 px | 0.57 | 1.03 | 252 |
| stroke 23 | 59 % → 59 % | 168.1 px | 0.57 | 1.01 | 153 |
| stroke 24 | 63 % → 62 % | 187.8 px | 0.57 | 1.00 | 139 |

Numbers say: wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #02 Henry Ward cream strokes — own sheet
own sheet 600 × 600 · Gouache 1.00 · 46 px · 7.4 s

![Brush Artist · Refs · #02 Henry Ward cream strokes — own sheet](Brush-Artist-Refs-02-Henry-Ward-cream-strokes-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 14 % → 15 % | 29.6 px | 0.66 | 1.04 | 179 |
| stroke 2 | 21 % → 17 % | 55.3 px | 0.66 | 0.82 | 192 |
| stroke 3 | 21 % → 21 % | 52.3 px | 0.66 | 1.02 | 193 |
| stroke 4 | 22 % → 19 % | 53.7 px | 0.66 | 0.87 | 210 |
| stroke 5 | 27 % → 23 % | 67.5 px | 0.66 | 0.84 | 203 |
| stroke 6 | 22 % → 20 % | 52.9 px | 0.66 | 0.89 | 190 |
| stroke 7 | 22 % → 13 % | 55.9 px | 0.65 | 0.59 | 186 |

## Brush Artist · Refs · #03 Henry Ward navy contours — own sheet
own sheet 600 × 600 · Impasto 1.00 · 22 px · 2.6 s

![Brush Artist · Refs · #03 Henry Ward navy contours — own sheet](Brush-Artist-Refs-03-Henry-Ward-navy-contours-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 10 % → 15 % | 20.3 px | 0.69 | 1.51 | 105 |
| stroke 2 | 18 % → 20 % | 25.7 px | 0.69 | 1.12 | 95 |
| stroke 3 | 21 % → 21 % | 30.8 px | 0.69 | 1.00 | 116 |
| stroke 4 | 20 % → 18 % | 45.1 px | 0.69 | 0.89 | 159 |

Numbers say: wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #04 Henry Ward grey cloud — own sheet
own sheet 600 × 600 · Gouache 1.00 · 50 px · 12.0 s

![Brush Artist · Refs · #04 Henry Ward grey cloud — own sheet](Brush-Artist-Refs-04-Henry-Ward-grey-cloud-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 9 % → 38 % | 26.9 px | 0.39 | 4.15 | 176 |
| stroke 2 | 14 % → 40 % | 39.8 px | 0.39 | 2.86 | 194 |
| stroke 3 | 20 % → 46 % | 55.7 px | 0.39 | 2.29 | 204 |
| stroke 4 | 24 % → 48 % | 71.2 px | 0.39 | 1.98 | 231 |
| stroke 5 | 30 % → 54 % | 91.4 px | 0.39 | 1.81 | 232 |
| stroke 6 | 31 % → 56 % | 101.9 px | 0.39 | 1.80 | 187 |
| stroke 7 | 36 % → 64 % | 106.4 px | 0.39 | 1.75 | 189 |
| stroke 8 | 37 % → 64 % | 111.3 px | 0.39 | 1.70 | 192 |
| stroke 9 | 34 % → 63 % | 102.7 px | 0.39 | 1.83 | 170 |
| stroke 10 | 37 % → 63 % | 119.8 px | 0.39 | 1.68 | 165 |
| stroke 11 | 36 % → 62 % | 102.3 px | 0.39 | 1.71 | 188 |
| stroke 12 | 37 % → 62 % | 111.4 px | 0.39 | 1.68 | 174 |
| stroke 13 | 37 % → 64 % | 106.7 px | 0.39 | 1.71 | 173 |
| stroke 14 | 37 % → 64 % | 110.5 px | 0.39 | 1.72 | 183 |
| stroke 15 | 36 % → 58 % | 104.3 px | 0.39 | 1.61 | 178 |
| stroke 16 | 39 % → 56 % | 118.4 px | 0.39 | 1.44 | 179 |
| stroke 17 | 37 % → 48 % | 106.1 px | 0.39 | 1.30 | 175 |
| stroke 18 | 37 % → 45 % | 122.7 px | 0.39 | 1.21 | 173 |
| stroke 19 | 36 % → 38 % | 108.5 px | 0.39 | 1.04 | 147 |
| stroke 20 | 40 % → 38 % | 124.7 px | 0.39 | 0.95 | 190 |

Numbers say: wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #05 Henry Ward green in rust loops — own sheet
own sheet 600 × 600 · Impasto 1.00 · 20 px · 2.2 s

![Brush Artist · Refs · #05 Henry Ward green in rust loops — own sheet](Brush-Artist-Refs-05-Henry-Ward-green-in-rust-loops-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 11 % → 18 % | 20.2 px | 0.02 | 1.55 | 139 |
| stroke 2 | 12 % → 11 % | 22.7 px | 0.03 | 0.92 | 136 |
| stroke 3 | 22 % → 20 % | 40.1 px | 0.03 | 0.92 | 129 |

Numbers say: wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #06 Henry Ward scrubbed grey — own sheet
own sheet 600 × 600 · Gouache 1.00 · 50 px · 12.8 s

![Brush Artist · Refs · #06 Henry Ward scrubbed grey — own sheet](Brush-Artist-Refs-06-Henry-Ward-scrubbed-grey-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 11 % → 42 % | 26.1 px | 0.39 | 3.97 | 185 |
| stroke 2 | 14 % → 45 % | 37.2 px | 0.39 | 3.19 | 185 |
| stroke 3 | 20 % → 47 % | 60.7 px | 0.39 | 2.39 | 176 |
| stroke 4 | 23 % → 48 % | 71.6 px | 0.39 | 2.12 | 168 |
| stroke 5 | 31 % → 61 % | 94.0 px | 0.39 | 1.95 | 186 |
| stroke 6 | 35 % → 61 % | 108.4 px | 0.39 | 1.73 | 179 |
| stroke 7 | 38 % → 64 % | 108.4 px | 0.39 | 1.69 | 180 |
| stroke 8 | 40 % → 64 % | 125.9 px | 0.39 | 1.62 | 167 |
| stroke 9 | 36 % → 63 % | 111.8 px | 0.39 | 1.74 | 168 |
| stroke 10 | 36 % → 61 % | 117.7 px | 0.39 | 1.70 | 168 |
| stroke 11 | 38 % → 63 % | 110.7 px | 0.39 | 1.66 | 175 |
| stroke 12 | 40 % → 63 % | 121.3 px | 0.39 | 1.58 | 182 |
| stroke 13 | 37 % → 63 % | 103.7 px | 0.39 | 1.74 | 192 |
| stroke 14 | 36 % → 63 % | 104.4 px | 0.39 | 1.78 | 301 |
| stroke 15 | 36 % → 64 % | 103.4 px | 0.39 | 1.77 | 187 |
| stroke 16 | 36 % → 61 % | 116.7 px | 0.39 | 1.67 | 166 |
| stroke 17 | 35 % → 54 % | 104.7 px | 0.39 | 1.53 | 194 |
| stroke 18 | 37 % → 52 % | 111.9 px | 0.39 | 1.40 | 191 |
| stroke 19 | 36 % → 48 % | 108.1 px | 0.39 | 1.31 | 188 |
| stroke 20 | 38 % → 46 % | 118.2 px | 0.39 | 1.21 | 189 |
| stroke 21 | 37 % → 38 % | 106.6 px | 0.39 | 1.04 | 175 |
| stroke 22 | 35 % → 34 % | 116.6 px | 0.39 | 0.96 | 175 |

Numbers say: wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #07 Henry Ward blue L + black zigzag — own sheet
own sheet 600 × 600 · Impasto 1.00 · 34 px · 1.8 s

![Brush Artist · Refs · #07 Henry Ward blue L + black zigzag — own sheet](Brush-Artist-Refs-07-Henry-Ward-blue-L-black-zigzag-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 14 % → 16 % | 32.3 px | 0.59 | 1.12 | 111 |
| stroke 2 | 16 % → 14 % | 39.3 px | 0.59 | 0.90 | 80 |

## Brush Artist · Refs · #08 Henry Ward olive bands — own sheet
own sheet 600 × 600 · Gouache 1.00 · 34 px · 4.8 s

![Brush Artist · Refs · #08 Henry Ward olive bands — own sheet](Brush-Artist-Refs-08-Henry-Ward-olive-bands-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 10 % → 8 % | 20.0 px | 0.58 | 0.79 | 150 |
| stroke 2 | 16 % → 10 % | 37.0 px | 0.58 | 0.58 | 153 |
| stroke 3 | 15 % → 14 % | 31.4 px | 0.58 | 0.93 | 143 |
| stroke 4 | 16 % → 11 % | 35.7 px | 0.58 | 0.68 | 163 |
| stroke 5 | 24 % → 14 % | 48.5 px | 0.58 | 0.61 | 153 |
| stroke 6 | 15 % → 8 % | 29.2 px | 0.58 | 0.52 | 147 |

## Brush Artist · Refs · #09 Henry Ward white loops — own sheet
own sheet 600 × 600 · Gouache 1.00 · 46 px · 6.6 s

![Brush Artist · Refs · #09 Henry Ward white loops — own sheet](Brush-Artist-Refs-09-Henry-Ward-white-loops-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 17 % → 4 % | 8.9 px | 0.06 | 0.22 | 717 |
| stroke 2 | 17 % → 3 % | 17.3 px | 0.07 | 0.15 | 788 |
| stroke 3 | 24 % → 2 % | 22.7 px | 0.07 | 0.10 | 688 |
| stroke 4 | 3 % → 1 % | 7.6 px | 0.06 | 0.32 | 131 |
| stroke 5 | 3 % → 1 % | 7.5 px | 0.07 | 0.40 | 141 |
| stroke 6 | 3 % → 2 % | 7.9 px | 0.07 | 0.85 | 128 |
| stroke 7 | 5 % → 2 % | 13.9 px | 0.07 | 0.46 | 137 |
| stroke 8 | 4 % → 1 % | 7.3 px | 0.06 | 0.35 | 152 |

## Brush Artist · Refs · #10 Henry Ward maroon loops — own sheet
own sheet 600 × 600 · Impasto 1.00 · 30 px · 2.8 s

![Brush Artist · Refs · #10 Henry Ward maroon loops — own sheet](Brush-Artist-Refs-10-Henry-Ward-maroon-loops-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 11 % → 26 % | 26.6 px | 0.72 | 2.43 | 196 |
| stroke 2 | 21 % → 39 % | 46.5 px | 0.71 | 1.87 | 114 |
| stroke 3 | 28 % → 35 % | 55.9 px | 0.72 | 1.27 | 143 |
| stroke 4 | 39 % → 38 % | 87.9 px | 0.72 | 0.97 | 95 |
| stroke 5 | 32 % → 29 % | 80.9 px | 0.72 | 0.91 | 130 |

Numbers say: wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #11 Henry Ward purple spun balls — own sheet
own sheet 600 × 600 · Impasto 1.00 · 36 px · 2.5 s

![Brush Artist · Refs · #11 Henry Ward purple spun balls — own sheet](Brush-Artist-Refs-11-Henry-Ward-purple-spun-balls-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 24 % → 34 % | 26.4 px | 0.68 | 1.41 | 199 |
| stroke 2 | 35 % → 45 % | 38.0 px | 0.68 | 1.31 | 209 |
| stroke 3 | 35 % → 34 % | 39.0 px | 0.68 | 0.96 | 207 |

## Brush Artist · Refs · #12 Henry Ward black-olive cage — own sheet
own sheet 600 × 600 · Gouache 1.00 · 28 px · 4.7 s

![Brush Artist · Refs · #12 Henry Ward black-olive cage — own sheet](Brush-Artist-Refs-12-Henry-Ward-black-olive-cage-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 8 % → 9 % | 14.8 px | 0.59 | 1.19 | 177 |
| stroke 2 | 8 % → 11 % | 18.8 px | 0.59 | 1.36 | 164 |
| stroke 3 | 17 % → 14 % | 26.6 px | 0.59 | 0.84 | 200 |
| stroke 4 | 17 % → 12 % | 34.7 px | 0.59 | 0.66 | 114 |
| stroke 5 | 16 % → 9 % | 30.1 px | 0.59 | 0.53 | 123 |
| stroke 6 | 26 % → 13 % | 50.0 px | 0.59 | 0.48 | 148 |

## Brush Artist · Refs · #13 Henry Ward blue streaky form — own sheet
own sheet 600 × 600 · Gouache 1.00 · 50 px · 10.8 s

![Brush Artist · Refs · #13 Henry Ward blue streaky form — own sheet](Brush-Artist-Refs-13-Henry-Ward-blue-streaky-form-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 9 % → 2 % | 26.6 px | 0.03 | 0.26 | 181 |
| stroke 2 | 13 % → 2 % | 38.6 px | 0.03 | 0.17 | 180 |
| stroke 3 | 21 % → 2 % | 60.7 px | 0.03 | 0.11 | 185 |
| stroke 4 | 23 % → 2 % | 75.5 px | 0.03 | 0.09 | 166 |
| stroke 5 | 33 % → 2 % | 94.8 px | 0.03 | 0.07 | 180 |
| stroke 6 | 35 % → 2 % | 100.0 px | 0.03 | 0.06 | 187 |
| stroke 7 | 36 % → 3 % | 106.9 px | 0.04 | 0.08 | 203 |
| stroke 8 | 39 % → 2 % | 117.8 px | 0.04 | 0.06 | 182 |
| stroke 9 | 36 % → 2 % | 111.1 px | 0.04 | 0.06 | 174 |
| stroke 10 | 37 % → 2 % | 121.1 px | 0.04 | 0.06 | 167 |
| stroke 11 | 35 % → 1 % | 108.4 px | 0.04 | 0.04 | 181 |
| stroke 12 | 36 % → 1 % | 106.5 px | 0.04 | 0.04 | 187 |
| stroke 13 | 35 % → 2 % | 108.2 px | 0.04 | 0.06 | 172 |
| stroke 14 | 34 % → 2 % | 101.1 px | 0.04 | 0.06 | 193 |
| stroke 15 | 33 % → 2 % | 94.0 px | 0.04 | 0.07 | 191 |
| stroke 16 | 37 % → 2 % | 109.2 px | 0.04 | 0.06 | 184 |
| stroke 17 | 43 % → 2 % | 106.3 px | 0.04 | 0.04 | 169 |
| stroke 18 | 47 % → 2 % | 114.1 px | 0.04 | 0.03 | 191 |
| stroke 19 | 50 % → 2 % | 101.3 px | 0.04 | 0.04 | 184 |
| stroke 20 | 56 % → 2 % | 107.5 px | 0.04 | 0.03 | 181 |
| stroke 21 | 4 % → 1 % | 7.9 px | 0.04 | 0.34 | 152 |
| stroke 22 | 3 % → 2 % | 7.8 px | 0.03 | 0.77 | 135 |
| stroke 23 | 5 % → 2 % | 14.6 px | 0.03 | 0.46 | 126 |
| stroke 24 | 4 % → 1 % | 9.9 px | 0.04 | 0.40 | 139 |
| stroke 25 | 4 % → 2 % | 11.5 px | 0.04 | 0.52 | 151 |

## Brush Artist · Refs · #14 Henry Ward olive totem — own sheet
own sheet 600 × 600 · Impasto 1.00 · 48 px · 6.3 s

![Brush Artist · Refs · #14 Henry Ward olive totem — own sheet](Brush-Artist-Refs-14-Henry-Ward-olive-totem-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 18 % → 46 % | 45.8 px | 0.37 | 2.63 | 126 |
| stroke 2 | 21 % → 50 % | 64.3 px | 0.37 | 2.44 | 122 |
| stroke 3 | 29 % → 52 % | 100.3 px | 0.37 | 1.78 | 129 |
| stroke 4 | 30 % → 54 % | 112.7 px | 0.37 | 1.81 | 126 |
| stroke 5 | 39 % → 63 % | 134.6 px | 0.37 | 1.64 | 112 |
| stroke 6 | 39 % → 65 % | 150.1 px | 0.37 | 1.68 | 115 |
| stroke 7 | 37 % → 61 % | 123.6 px | 0.37 | 1.67 | 126 |
| stroke 8 | 37 % → 63 % | 141.6 px | 0.37 | 1.70 | 117 |
| stroke 9 | 37 % → 63 % | 129.7 px | 0.37 | 1.68 | 118 |
| stroke 10 | 38 % → 62 % | 140.9 px | 0.37 | 1.62 | 118 |
| stroke 11 | 40 % → 65 % | 143.5 px | 0.37 | 1.61 | 123 |
| stroke 12 | 38 % → 65 % | 143.4 px | 0.37 | 1.71 | 131 |
| stroke 13 | 38 % → 66 % | 134.6 px | 0.37 | 1.74 | 113 |
| stroke 14 | 37 % → 62 % | 134.4 px | 0.37 | 1.69 | 134 |
| stroke 15 | 40 % → 66 % | 136.6 px | 0.37 | 1.65 | 112 |
| stroke 16 | 38 % → 63 % | 137.8 px | 0.37 | 1.67 | 130 |
| stroke 17 | 37 % → 62 % | 125.2 px | 0.37 | 1.66 | 135 |
| stroke 18 | 40 % → 66 % | 154.7 px | 0.37 | 1.64 | 112 |
| stroke 19 | 40 % → 60 % | 137.7 px | 0.37 | 1.52 | 129 |
| stroke 20 | 40 % → 55 % | 143.4 px | 0.37 | 1.35 | 129 |
| stroke 21 | 46 % → 55 % | 136.7 px | 0.37 | 1.18 | 106 |
| stroke 22 | 54 % → 53 % | 146.5 px | 0.37 | 0.99 | 113 |

Numbers say: wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #15 Ultramarine brush script — own sheet
own sheet 600 × 600 · Ink 1.00 · 4 px · 8.0 s

![Brush Artist · Refs · #15 Ultramarine brush script — own sheet](Brush-Artist-Refs-15-Ultramarine-brush-script-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 40 % → 42 % | 8.9 px | 0.66 | 1.05 | 45 |
| stroke 2 | 40 % → 42 % | 8.9 px | 0.66 | 1.06 | 43 |
| stroke 3 | 40 % → 42 % | 9.5 px | 0.74 | 1.06 | 24 |
| stroke 4 | 42 % → 45 % | 10.1 px | 0.74 | 1.09 | 18 |
| stroke 5 | 44 % → 48 % | 9.7 px | 0.73 | 1.09 | 24 |
| stroke 6 | 42 % → 44 % | 9.5 px | 0.65 | 1.05 | 50 |
| stroke 7 | 43 % → 47 % | 9.2 px | 0.72 | 1.08 | 21 |
| stroke 8 | 38 % → 41 % | 9.3 px | 0.68 | 1.05 | 35 |
| stroke 9 | 40 % → 42 % | 9.2 px | 0.69 | 1.06 | 42 |
| stroke 10 | 36 % → 38 % | 9.9 px | 0.68 | 1.05 | 37 |
| stroke 11 | 42 % → 45 % | 9.6 px | 0.70 | 1.06 | 32 |
| stroke 12 | 39 % → 41 % | 9.4 px | 0.66 | 1.06 | 42 |
| stroke 13 | 45 % → 48 % | 10.2 px | 0.71 | 1.06 | 24 |
| stroke 14 | 38 % → 41 % | 9.8 px | 0.72 | 1.07 | 21 |
| stroke 15 | 37 % → 39 % | 9.1 px | 0.69 | 1.06 | 51 |
| stroke 16 | 42 % → 45 % | 9.4 px | 0.72 | 1.06 | 22 |
| stroke 17 | 41 % → 44 % | 7.1 px | 0.71 | 1.08 | 35 |
| stroke 18 | 43 % → 45 % | 9.2 px | 0.73 | 1.06 | 22 |
| stroke 19 | 39 % → 41 % | 8.9 px | 0.66 | 1.05 | 43 |
| stroke 20 | 41 % → 43 % | 9.4 px | 0.71 | 1.06 | 28 |
| stroke 21 | 41 % → 43 % | 9.9 px | 0.70 | 1.06 | 32 |
| stroke 22 | 42 % → 45 % | 8.5 px | 0.65 | 1.06 | 57 |
| stroke 23 | 40 % → 43 % | 10.1 px | 0.73 | 1.08 | 21 |
| stroke 24 | 38 % → 41 % | 8.8 px | 0.73 | 1.07 | 29 |
| stroke 25 | 41 % → 43 % | 9.8 px | 0.72 | 1.07 | 25 |
| stroke 26 | 46 % → 49 % | 9.3 px | 0.68 | 1.05 | 43 |
| stroke 27 | 43 % → 45 % | 8.8 px | 0.63 | 1.05 | 50 |
| stroke 28 | 44 % → 46 % | 9.1 px | 0.70 | 1.06 | 35 |
| stroke 29 | 36 % → 39 % | 10.6 px | 0.72 | 1.08 | 21 |
| stroke 30 | 39 % → 41 % | 8.7 px | 0.71 | 1.04 | 32 |
| stroke 31 | 43 % → 46 % | 10.3 px | 0.75 | 1.08 | 19 |
| stroke 32 | 42 % → 46 % | 9.5 px | 0.73 | 1.09 | 25 |
| stroke 33 | 35 % → 38 % | 10.9 px | 0.72 | 1.08 | 19 |
| stroke 34 | 40 % → 43 % | 9.8 px | 0.73 | 1.08 | 20 |
| stroke 35 | 36 % → 37 % | 9.4 px | 0.65 | 1.05 | 46 |

## Brush Artist · Refs · #18 Blue oil-stick scribbles — own sheet
own sheet 600 × 600 · Pastel 1.00 · 10 px · 2.7 s

![Brush Artist · Refs · #18 Blue oil-stick scribbles — own sheet](Brush-Artist-Refs-18-Blue-oil-stick-scribbles-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 15 % → 31 % | 3.8 px | 0.49 | 2.11 | 133 |
| stroke 2 | 13 % → 37 % | 3.6 px | 0.49 | 2.73 | 140 |
| stroke 3 | 16 % → 26 % | 5.8 px | 0.49 | 1.66 | 135 |
| stroke 4 | 15 % → 29 % | 8.0 px | 0.49 | 1.88 | 142 |
| stroke 5 | 29 % → 34 % | 8.4 px | 0.49 | 1.19 | 141 |
| stroke 6 | 25 % → 26 % | 9.4 px | 0.49 | 1.02 | 103 |
| stroke 7 | 26 % → 32 % | 8.3 px | 0.49 | 1.24 | 130 |
| stroke 8 | 30 % → 30 % | 17.0 px | 0.49 | 1.00 | 143 |

Numbers say: wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #20 Orange-red crayon scribble — own sheet
own sheet 600 × 600 · Pastel 1.00 · 14 px · 2.5 s

![Brush Artist · Refs · #20 Orange-red crayon scribble — own sheet](Brush-Artist-Refs-20-Orange-red-crayon-scribble-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 8 % → 18 % | 5.5 px | 0.59 | 2.46 | 161 |
| stroke 2 | 9 % → 23 % | 6.8 px | 0.59 | 2.48 | 137 |
| stroke 3 | 13 % → 21 % | 8.5 px | 0.59 | 1.64 | 141 |
| stroke 4 | 24 % → 32 % | 8.9 px | 0.59 | 1.34 | 140 |
| stroke 5 | 27 % → 27 % | 7.7 px | 0.59 | 1.00 | 133 |
| stroke 6 | 22 % → 22 % | 16.8 px | 0.59 | 1.00 | 141 |

Numbers say: wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #21 Gritty black contours — own sheet
own sheet 600 × 600 · Gouache 1.00 · 12 px · 3.6 s

![Brush Artist · Refs · #21 Gritty black contours — own sheet](Brush-Artist-Refs-21-Gritty-black-contours-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 4 % → 3 % | 4.9 px | 0.37 | 0.70 | 135 |
| stroke 2 | 5 % → 2 % | 7.6 px | 0.37 | 0.43 | 150 |
| stroke 3 | 7 % → 2 % | 5.9 px | 0.37 | 0.26 | 108 |
| stroke 4 | 8 % → 3 % | 9.8 px | 0.37 | 0.40 | 120 |
| stroke 5 | 10 % → 3 % | 11.9 px | 0.37 | 0.34 | 70 |

## Brush Artist · Refs · #22 Bold black brush poster — own sheet
own sheet 600 × 600 · Ink 1.00 · 20 px · 4.9 s

![Brush Artist · Refs · #22 Bold black brush poster — own sheet](Brush-Artist-Refs-22-Bold-black-brush-poster-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 22 % → 27 % | 36.3 px | 0.94 | 1.20 | 97 |
| stroke 2 | 27 % → 37 % | 41.4 px | 0.94 | 1.37 | 24 |
| stroke 3 | 28 % → 29 % | 43.6 px | 0.94 | 1.00 | 47 |
| stroke 4 | 27 % → 39 % | 53.7 px | 0.94 | 1.43 | 58 |
| stroke 5 | 25 % → 25 % | 42.9 px | 0.94 | 1.00 | 88 |

## Brush Artist · Refs · #23 Dry white on orange + black line — own sheet
own sheet 600 × 600 · Gouache 1.00 · 50 px · 7.5 s

![Brush Artist · Refs · #23 Dry white on orange + black line — own sheet](Brush-Artist-Refs-23-Dry-white-on-orange-black-line-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 6 % → 11 % | 22.3 px | 0.40 | 1.71 | 137 |
| stroke 2 | 9 % → 10 % | 31.8 px | 0.40 | 1.10 | 154 |
| stroke 3 | 13 % → 11 % | 48.0 px | 0.40 | 0.82 | 129 |
| stroke 4 | 15 % → 12 % | 59.0 px | 0.40 | 0.80 | 126 |
| stroke 5 | 21 % → 14 % | 75.7 px | 0.40 | 0.67 | 124 |
| stroke 6 | 21 % → 16 % | 88.3 px | 0.40 | 0.77 | 131 |
| stroke 7 | 17 % → 15 % | 65.6 px | 0.39 | 0.87 | 131 |
| stroke 8 | 18 % → 14 % | 70.7 px | 0.39 | 0.79 | 132 |
| stroke 9 | 18 % → 15 % | 68.7 px | 0.39 | 0.83 | 132 |
| stroke 10 | 18 % → 15 % | 69.0 px | 0.39 | 0.87 | 130 |
| stroke 11 | 20 % → 17 % | 74.8 px | 0.39 | 0.85 | 129 |
| stroke 12 | 21 % → 17 % | 80.3 px | 0.39 | 0.81 | 139 |
| stroke 13 | 21 % → 19 % | 77.7 px | 0.39 | 0.89 | 120 |
| stroke 14 | 20 % → 19 % | 81.1 px | 0.39 | 0.91 | 144 |
| stroke 15 | 20 % → 16 % | 73.7 px | 0.39 | 0.80 | 132 |
| stroke 16 | 20 % → 14 % | 80.1 px | 0.39 | 0.70 | 138 |
| stroke 17 | 20 % → 13 % | 71.5 px | 0.39 | 0.61 | 128 |
| stroke 18 | 24 % → 13 % | 86.5 px | 0.39 | 0.55 | 138 |

Numbers say: wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #24 Picasso flat oil — own sheet
own sheet 600 × 600 · Oil 0.89 · Oil glaze 0.11 · 34 px · 4.8 s

![Brush Artist · Refs · #24 Picasso flat oil — own sheet](Brush-Artist-Refs-24-Picasso-flat-oil-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 14 % → 42 % | 29.4 px | 0.22 | 3.06 | 121 |
| stroke 2 | 18 % → 46 % | 41.9 px | 0.22 | 2.57 | 125 |
| stroke 3 | 26 % → 56 % | 57.4 px | 0.22 | 2.14 | 122 |
| stroke 4 | 35 % → 62 % | 77.7 px | 0.22 | 1.79 | 125 |
| stroke 5 | 40 % → 67 % | 89.3 px | 0.21 | 1.66 | 124 |
| stroke 6 | 41 % → 62 % | 96.0 px | 0.21 | 1.50 | 126 |
| stroke 7 | 41 % → 61 % | 87.0 px | 0.21 | 1.48 | 115 |
| stroke 8 | 41 % → 61 % | 99.6 px | 0.22 | 1.49 | 135 |
| stroke 9 | 34 % → 57 % | 73.4 px | 0.22 | 1.70 | 117 |
| stroke 10 | 35 % → 56 % | 84.6 px | 0.22 | 1.59 | 122 |
| stroke 11 | 33 % → 55 % | 70.2 px | 0.22 | 1.66 | 129 |
| stroke 12 | 35 % → 55 % | 82.8 px | 0.22 | 1.57 | 122 |
| stroke 13 | 34 % → 62 % | 74.8 px | 0.22 | 1.81 | 124 |
| stroke 14 | 36 % → 63 % | 80.8 px | 0.22 | 1.78 | 125 |
| stroke 15 | 34 % → 57 % | 71.9 px | 0.21 | 1.67 | 122 |
| stroke 16 | 34 % → 50 % | 78.6 px | 0.21 | 1.46 | 133 |
| stroke 17 | 39 % → 44 % | 81.0 px | 0.21 | 1.14 | 127 |
| stroke 18 | 39 % → 39 % | 93.8 px | 0.21 | 1.00 | 120 |

Numbers say: wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #25 Yellow heavy flat stroke — own sheet
own sheet 600 × 600 · Impasto 1.00 · 110 px · 2.7 s

![Brush Artist · Refs · #25 Yellow heavy flat stroke — own sheet](Brush-Artist-Refs-25-Yellow-heavy-flat-stroke-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 18 % → 18 % | 104.3 px | 0.17 | 0.98 | 615 |

## Brush Artist · Refs · #27 Orange impasto swatch — own sheet
own sheet 600 × 600 · Impasto 1.00 · 60 px · 3.0 s

![Brush Artist · Refs · #27 Orange impasto swatch — own sheet](Brush-Artist-Refs-27-Orange-impasto-swatch-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 8 % → 21 % | 61.8 px | 0.33 | 2.60 | 65 |
| stroke 2 | 7 % → 33 % | 62.6 px | 0.33 | 4.67 | 44 |
| stroke 3 | 25 % → 36 % | 245.8 px | 0.33 | 1.40 | 33 |
| stroke 4 | 10 % → 12 % | 69.8 px | 0.33 | 1.25 | 60 |
| stroke 5 | 17 % → 33 % | 63.5 px | 0.33 | 1.90 | 68 |
| stroke 6 | 18 % → 32 % | 145.3 px | 0.33 | 1.79 | 57 |
| stroke 7 | 8 % → 15 % | 70.4 px | 0.33 | 1.87 | 47 |
| stroke 8 | 33 % → 34 % | 337.7 px | 0.33 | 1.04 | 50 |
| stroke 9 | 38 % → 37 % | 185.5 px | 0.33 | 0.98 | 65 |
| stroke 10 | 34 % → 33 % | 305.4 px | 0.33 | 0.98 | 46 |

Numbers say: wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #28 Miles Davis black lines — own sheet
own sheet 600 × 600 · Ink 1.00 · 22 px · 5.6 s

![Brush Artist · Refs · #28 Miles Davis black lines — own sheet](Brush-Artist-Refs-28-Miles-Davis-black-lines-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 22 % → 32 % | 36.5 px | 0.88 | 1.42 | 152 |
| stroke 2 | 28 % → 49 % | 38.2 px | 0.88 | 1.73 | 119 |
| stroke 3 | 39 % → 44 % | 75.1 px | 0.88 | 1.12 | 107 |
| stroke 4 | 42 % → 48 % | 83.7 px | 0.88 | 1.15 | 149 |
| stroke 5 | 55 % → 55 % | 109.8 px | 0.88 | 1.00 | 116 |

Numbers say: wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #29 Shrigley magenta asterisk — own sheet
own sheet 600 × 600 · Watercolour 1.00 · 70 px · 5.8 s

![Brush Artist · Refs · #29 Shrigley magenta asterisk — own sheet](Brush-Artist-Refs-29-Shrigley-magenta-asterisk-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 13 % → 37 % | 46.6 px | 0.67 | 2.86 | 262 |
| stroke 2 | 12 % → 12 % | 87.1 px | 0.67 | 1.00 | 201 |
| stroke 3 | 28 % → 37 % | 100.9 px | 0.67 | 1.31 | 182 |
| stroke 4 | 23 % → 23 % | 164.0 px | 0.67 | 1.02 | 183 |

Numbers say: wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #30 Red gouache face patch — own sheet
own sheet 600 × 600 · Gouache 1.00 · 60 px · 10.4 s

![Brush Artist · Refs · #30 Red gouache face patch — own sheet](Brush-Artist-Refs-30-Red-gouache-face-patch-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 12 % → 37 % | 51.5 px | 0.54 | 3.23 | 153 |
| stroke 2 | 15 % → 40 % | 74.5 px | 0.54 | 2.72 | 155 |
| stroke 3 | 24 % → 50 % | 115.9 px | 0.54 | 2.06 | 153 |
| stroke 4 | 27 % → 52 % | 134.1 px | 0.54 | 1.94 | 163 |
| stroke 5 | 34 % → 60 % | 159.9 px | 0.54 | 1.77 | 156 |
| stroke 6 | 35 % → 61 % | 178.3 px | 0.54 | 1.76 | 154 |
| stroke 7 | 34 % → 59 % | 160.9 px | 0.54 | 1.73 | 163 |
| stroke 8 | 34 % → 56 % | 162.5 px | 0.54 | 1.66 | 161 |
| stroke 9 | 36 % → 60 % | 173.1 px | 0.54 | 1.66 | 146 |
| stroke 10 | 38 % → 62 % | 196.8 px | 0.54 | 1.64 | 153 |
| stroke 11 | 37 % → 61 % | 182.4 px | 0.54 | 1.66 | 153 |
| stroke 12 | 36 % → 58 % | 178.3 px | 0.54 | 1.62 | 156 |
| stroke 13 | 33 % → 46 % | 156.5 px | 0.54 | 1.39 | 163 |
| stroke 14 | 33 % → 41 % | 157.6 px | 0.54 | 1.25 | 186 |
| stroke 15 | 33 % → 37 % | 153.4 px | 0.54 | 1.12 | 180 |
| stroke 16 | 39 % → 39 % | 184.9 px | 0.54 | 0.99 | 154 |

Numbers say: wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #31 Warhol blotted line — own sheet
own sheet 600 × 600 · Ink 1.00 · 6 px · 4.5 s

![Brush Artist · Refs · #31 Warhol blotted line — own sheet](Brush-Artist-Refs-31-Warhol-blotted-line-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 21 % → 42 % | 15.8 px | 0.82 | 1.98 | 77 |
| stroke 2 | 17 % → 23 % | 15.9 px | 0.82 | 1.34 | 68 |
| stroke 3 | 24 % → 25 % | 25.1 px | 0.81 | 1.02 | 66 |
| stroke 4 | 31 % → 40 % | 31.8 px | 0.82 | 1.28 | 47 |
| stroke 5 | 35 % → 44 % | 36.4 px | 0.82 | 1.23 | 65 |
| stroke 6 | 32 % → 33 % | 26.7 px | 0.81 | 1.03 | 65 |

Numbers say: wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #32 Thick orange swipes — own sheet
own sheet 600 × 600 · Impasto 1.00 · 90 px · 3.3 s

![Brush Artist · Refs · #32 Thick orange swipes — own sheet](Brush-Artist-Refs-32-Thick-orange-swipes-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 14 % → 27 % | 86.1 px | 0.03 | 1.90 | 298 |
| stroke 2 | 26 % → 38 % | 177.0 px | 0.03 | 1.43 | 287 |
| stroke 3 | 28 % → 27 % | 177.6 px | 0.03 | 0.98 | 272 |

Numbers say: wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #33 Red wet-in-wet band — own sheet
own sheet 600 × 600 · Watercolour 1.00 · 80 px · 9.0 s

![Brush Artist · Refs · #33 Red wet-in-wet band — own sheet](Brush-Artist-Refs-33-Red-wet-in-wet-band-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 24 % → 59 % | 89.6 px | 0.61 | 2.52 | 387 |
| stroke 2 | 30 % → 53 % | 244.8 px | 0.62 | 1.76 | 107 |
| stroke 3 | 37 % → 55 % | 358.4 px | 0.61 | 1.49 | 101 |
| stroke 4 | 43 % → 62 % | 415.9 px | 0.62 | 1.44 | 106 |
| stroke 5 | 43 % → 57 % | 361.3 px | 0.61 | 1.33 | 109 |
| stroke 6 | 44 % → 49 % | 333.3 px | 0.60 | 1.13 | 121 |

Numbers say: wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #34 Magenta oil patches — own sheet
own sheet 600 × 600 · Oil 0.89 · Oil glaze 0.11 · 60 px · 3.1 s

![Brush Artist · Refs · #34 Magenta oil patches — own sheet](Brush-Artist-Refs-34-Magenta-oil-patches-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 8 % → 40 % | 58.6 px | 0.12 | 4.85 | 98 |
| stroke 2 | 9 % → 28 % | 59.5 px | 0.13 | 3.22 | 87 |
| stroke 3 | 7 % → 34 % | 59.0 px | 0.12 | 4.77 | 72 |
| stroke 4 | 15 % → 20 % | 125.3 px | 0.12 | 1.27 | 55 |
| stroke 5 | 22 % → 32 % | 118.3 px | 0.12 | 1.44 | 86 |
| stroke 6 | 19 % → 36 % | 164.2 px | 0.12 | 1.88 | 71 |
| stroke 7 | 28 % → 33 % | 224.7 px | 0.12 | 1.19 | 71 |
| stroke 8 | 32 % → 38 % | 223.8 px | 0.12 | 1.19 | 88 |
| stroke 9 | 24 % → 26 % | 155.3 px | 0.12 | 1.07 | 83 |
| stroke 10 | 28 % → 28 % | 246.0 px | 0.12 | 1.00 | 63 |
| stroke 11 | 35 % → 35 % | 309.4 px | 0.12 | 1.00 | 55 |
| stroke 12 | 25 % → 25 % | 177.1 px | 0.12 | 1.00 | 63 |

Numbers say: wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #35 Red band with runs — own sheet
own sheet 600 × 600 · Watercolour 1.00 · 70 px · 6.9 s

![Brush Artist · Refs · #35 Red band with runs — own sheet](Brush-Artist-Refs-35-Red-band-with-runs-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 37 % → 51 % | 138.9 px | 0.44 | 1.38 | 336 |

## Brush Artist · Refs · #36 Magenta letters flat brush — own sheet
own sheet 600 × 600 · Gouache 1.00 · 36 px · 10.1 s

![Brush Artist · Refs · #36 Magenta letters flat brush — own sheet](Brush-Artist-Refs-36-Magenta-letters-flat-brush-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 20 % → 39 % | 59.0 px | 0.50 | 1.95 | 33 |
| stroke 2 | 20 % → 32 % | 46.6 px | 0.50 | 1.59 | 37 |
| stroke 3 | 29 % → 54 % | 86.8 px | 0.50 | 1.86 | 28 |
| stroke 4 | 26 % → 44 % | 51.2 px | 0.50 | 1.67 | 104 |
| stroke 5 | 33 % → 55 % | 96.1 px | 0.50 | 1.67 | 65 |
| stroke 6 | 42 % → 56 % | 242.4 px | 0.50 | 1.33 | 15 |
| stroke 7 | 30 % → 44 % | 56.7 px | 0.50 | 1.45 | 106 |
| stroke 8 | 31 % → 53 % | 98.5 px | 0.50 | 1.68 | 57 |
| stroke 9 | 38 % → 51 % | 158.3 px | 0.50 | 1.33 | 27 |
| stroke 10 | 37 % → 63 % | 106.7 px | 0.50 | 1.72 | 69 |
| stroke 11 | 39 % → 62 % | 225.9 px | 0.50 | 1.58 | 13 |
| stroke 12 | 43 % → 56 % | 81.9 px | 0.50 | 1.29 | 115 |
| stroke 13 | 32 % → 46 % | 117.6 px | 0.50 | 1.43 | 31 |
| stroke 14 | 35 % → 52 % | 134.4 px | 0.50 | 1.47 | 28 |
| stroke 15 | 38 % → 56 % | 108.5 px | 0.50 | 1.49 | 75 |
| stroke 16 | 41 % → 50 % | 232.0 px | 0.50 | 1.23 | 15 |
| stroke 17 | 44 % → 52 % | 81.7 px | 0.50 | 1.19 | 106 |
| stroke 18 | 27 % → 36 % | 97.5 px | 0.50 | 1.35 | 32 |
| stroke 19 | 40 % → 39 % | 117.0 px | 0.50 | 0.96 | 45 |
| stroke 20 | 45 % → 45 % | 132.2 px | 0.50 | 0.99 | 26 |
| stroke 21 | 41 % → 39 % | 78.6 px | 0.50 | 0.96 | 81 |

Numbers say: wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #37 Oil still life dabs — own sheet
own sheet 600 × 600 · Oil 0.89 · Oil glaze 0.11 · 40 px · 2.5 s

![Brush Artist · Refs · #37 Oil still life dabs — own sheet](Brush-Artist-Refs-37-Oil-still-life-dabs-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 7 % → 7 % | 42.1 px | 0.38 | 1.00 | 38 |
| stroke 2 | 6 % → 27 % | 42.8 px | 0.38 | 4.44 | 21 |
| stroke 3 | 11 % → 34 % | 88.7 px | 0.38 | 3.01 | 24 |
| stroke 4 | 9 % → 9 % | 41.0 px | 0.38 | 1.00 | 37 |
| stroke 5 | 6 % → 10 % | 41.0 px | 0.38 | 1.73 | 21 |
| stroke 6 | 13 % → 30 % | 80.6 px | 0.38 | 2.32 | 29 |
| stroke 7 | 10 % → 23 % | 110.5 px | 0.38 | 2.21 | 10 |
| stroke 8 | 8 % → 13 % | 86.6 px | 0.38 | 1.62 | 13 |
| stroke 9 | 12 % → 13 % | 65.1 px | 0.37 | 1.08 | 30 |
| stroke 10 | 20 % → 24 % | 102.6 px | 0.38 | 1.20 | 35 |
| stroke 11 | 24 % → 27 % | 195.5 px | 0.39 | 1.17 | 18 |
| stroke 12 | 20 % → 21 % | 220.2 px | 0.39 | 1.01 | 15 |
| stroke 13 | 16 % → 16 % | 162.7 px | 0.39 | 1.00 | 12 |
| stroke 14 | 16 % → 16 % | 127.3 px | 0.38 | 1.00 | 20 |

Numbers say: wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #38 Sanguine drawing — own sheet
own sheet 600 × 600 · Pastel 1.00 · 6 px · 2.0 s

![Brush Artist · Refs · #38 Sanguine drawing — own sheet](Brush-Artist-Refs-38-Sanguine-drawing-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 3 % → 14 % | 2.9 px | 0.57 | 5.30 | 9 |
| stroke 2 | 3 % → 7 % | 2.9 px | 0.58 | 2.89 | 4 |
| stroke 3 | 3 % → 9 % | 2.9 px | 0.57 | 3.40 | 5 |
| stroke 4 | 2 % → 17 % | 2.7 px | 0.57 | 7.20 | 7 |
| stroke 5 | 2 % → 7 % | 2.7 px | 0.57 | 3.03 | 3 |
| stroke 6 | 3 % → 19 % | 3.4 px | 0.57 | 6.31 | 6 |
| stroke 7 | 5 % → 14 % | 5.2 px | 0.57 | 3.07 | 5 |
| stroke 8 | 4 % → 16 % | 4.7 px | 0.57 | 3.79 | 7 |
| stroke 9 | 3 % → 7 % | 2.9 px | 0.57 | 2.66 | 4 |
| stroke 10 | 4 % → 16 % | 4.7 px | 0.57 | 3.83 | 7 |
| stroke 11 | 3 % → 4 % | 2.9 px | 0.57 | 1.61 | 5 |
| stroke 12 | 4 % → 15 % | 4.8 px | 0.57 | 3.58 | 6 |
| stroke 13 | 8 % → 17 % | 8.9 px | 0.57 | 2.23 | 3 |
| stroke 14 | 4 % → 14 % | 4.9 px | 0.57 | 3.19 | 8 |
| stroke 15 | 9 % → 18 % | 10.7 px | 0.57 | 1.86 | 4 |
| stroke 16 | 6 % → 16 % | 6.6 px | 0.57 | 2.71 | 7 |
| stroke 17 | 4 % → 9 % | 4.4 px | 0.57 | 2.25 | 7 |
| stroke 18 | 3 % → 5 % | 2.9 px | 0.57 | 1.85 | 4 |
| stroke 19 | 6 % → 16 % | 6.9 px | 0.57 | 2.68 | 6 |
| stroke 20 | 8 % → 14 % | 9.2 px | 0.57 | 1.70 | 4 |
| stroke 21 | 4 % → 4 % | 4.3 px | 0.57 | 1.00 | 6 |
| stroke 22 | 8 % → 13 % | 8.6 px | 0.57 | 1.79 | 3 |
| stroke 23 | 7 % → 12 % | 8.3 px | 0.57 | 1.61 | 5 |
| stroke 24 | 4 % → 7 % | 4.7 px | 0.57 | 1.71 | 4 |
| stroke 25 | 8 % → 14 % | 8.7 px | 0.57 | 1.84 | 4 |
| stroke 26 | 6 % → 8 % | 6.5 px | 0.57 | 1.34 | 6 |
| stroke 27 | 4 % → 4 % | 4.3 px | 0.57 | 1.10 | 3 |
| stroke 28 | 7 % → 11 % | 8.2 px | 0.57 | 1.59 | 7 |
| stroke 29 | 8 % → 17 % | 8.8 px | 0.57 | 2.21 | 4 |
| stroke 30 | 13 % → 17 % | 14.9 px | 0.57 | 1.29 | 3 |
| stroke 31 | 5 % → 6 % | 5.4 px | 0.57 | 1.29 | 6 |
| stroke 32 | 10 % → 13 % | 11.8 px | 0.57 | 1.24 | 3 |
| stroke 33 | 7 % → 8 % | 8.5 px | 0.57 | 1.07 | 6 |
| stroke 34 | 11 % → 14 % | 12.0 px | 0.57 | 1.36 | 4 |
| stroke 35 | 9 % → 14 % | 10.0 px | 0.57 | 1.61 | 7 |
| stroke 36 | 10 % → 13 % | 11.4 px | 0.57 | 1.26 | 3 |
| stroke 37 | 9 % → 16 % | 10.5 px | 0.57 | 1.71 | 5 |
| stroke 38 | 13 % → 19 % | 14.8 px | 0.57 | 1.48 | 5 |
| stroke 39 | 14 % → 17 % | 15.7 px | 0.57 | 1.21 | 3 |
| stroke 40 | 6 % → 7 % | 7.2 px | 0.57 | 1.14 | 6 |
| stroke 41 | 16 % → 16 % | 17.7 px | 0.57 | 1.01 | 5 |
| stroke 42 | 14 % → 16 % | 15.2 px | 0.57 | 1.17 | 4 |
| stroke 43 | 10 % → 12 % | 11.6 px | 0.57 | 1.17 | 6 |
| stroke 44 | 12 % → 15 % | 14.3 px | 0.57 | 1.22 | 4 |
| stroke 45 | 2 % → 2 % | 2.7 px | 0.57 | 1.00 | 5 |
| stroke 46 | 16 % → 16 % | 18.5 px | 0.57 | 1.00 | 4 |
| stroke 47 | 13 % → 13 % | 15.0 px | 0.57 | 1.00 | 4 |
| stroke 48 | 12 % → 13 % | 14.3 px | 0.57 | 1.07 | 6 |
| stroke 49 | 19 % → 19 % | 21.5 px | 0.57 | 1.00 | 4 |
| stroke 50 | 10 % → 10 % | 11.6 px | 0.57 | 1.00 | 3 |

Numbers say: wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #39 Very thick impasto — own sheet
own sheet 600 × 600 · Impasto 1.00 · 60 px · 4.1 s

![Brush Artist · Refs · #39 Very thick impasto — own sheet](Brush-Artist-Refs-39-Very-thick-impasto-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 26 % → 37 % | 59.6 px | 0.43 | 1.42 | 255 |
| stroke 2 | 31 % → 48 % | 93.9 px | 0.44 | 1.54 | 268 |
| stroke 3 | 37 % → 49 % | 124.6 px | 0.43 | 1.33 | 250 |
| stroke 4 | 31 % → 44 % | 90.9 px | 0.44 | 1.41 | 278 |
| stroke 5 | 42 % → 41 % | 104.2 px | 0.44 | 0.98 | 261 |

Numbers say: wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #40 Watercolour blooms — own sheet
own sheet 600 × 600 · Watercolour 1.00 · 90 px · 7.1 s

![Brush Artist · Refs · #40 Watercolour blooms — own sheet](Brush-Artist-Refs-40-Watercolour-blooms-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 22 % → 28 % | 95.0 px | 0.12 | 1.31 | 747 |

## Brush Artist · Refs · #41 Coloured pencil hatching — own sheet
own sheet 600 × 600 · Pastel 1.00 · 4 px · 2.4 s

![Brush Artist · Refs · #41 Coloured pencil hatching — own sheet](Brush-Artist-Refs-41-Coloured-pencil-hatching-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 3 % → 13 % | 2.2 px | 0.35 | 4.64 | 4 |
| stroke 2 | 3 % → 7 % | 2.3 px | 0.35 | 2.29 | 3 |
| stroke 3 | 2 % → 11 % | 1.9 px | 0.35 | 4.38 | 2 |
| stroke 4 | 3 % → 19 % | 2.1 px | 0.35 | 6.73 | 2 |
| stroke 5 | 4 % → 7 % | 2.9 px | 0.35 | 1.83 | 4 |
| stroke 6 | 3 % → 13 % | 2.3 px | 0.35 | 4.19 | 2 |
| stroke 7 | 3 % → 15 % | 2.6 px | 0.35 | 4.43 | 2 |
| stroke 8 | 3 % → 12 % | 2.1 px | 0.35 | 4.20 | 3 |
| stroke 9 | 5 % → 11 % | 3.6 px | 0.35 | 2.27 | 5 |
| stroke 10 | 5 % → 15 % | 3.8 px | 0.35 | 2.99 | 2 |
| stroke 11 | 4 % → 13 % | 3.0 px | 0.35 | 3.28 | 4 |
| stroke 12 | 3 % → 3 % | 2.1 px | 0.35 | 1.00 | 2 |
| stroke 13 | 7 % → 17 % | 5.2 px | 0.35 | 2.45 | 5 |
| stroke 14 | 3 % → 13 % | 2.4 px | 0.35 | 4.19 | 3 |
| stroke 15 | 6 % → 12 % | 4.4 px | 0.35 | 2.09 | 2 |
| stroke 16 | 7 % → 11 % | 5.1 px | 0.35 | 1.61 | 5 |
| stroke 17 | 3 % → 3 % | 2.1 px | 0.35 | 1.00 | 5 |
| stroke 18 | 5 % → 8 % | 3.6 px | 0.35 | 1.65 | 3 |
| stroke 19 | 5 % → 13 % | 3.8 px | 0.35 | 2.72 | 5 |
| stroke 20 | 5 % → 14 % | 3.7 px | 0.35 | 2.92 | 3 |
| stroke 21 | 4 % → 13 % | 3.2 px | 0.35 | 3.20 | 2 |
| stroke 22 | 9 % → 16 % | 6.8 px | 0.35 | 1.77 | 3 |
| stroke 23 | 9 % → 13 % | 6.5 px | 0.35 | 1.55 | 6 |
| stroke 24 | 6 % → 14 % | 4.7 px | 0.35 | 2.18 | 8 |
| stroke 25 | 5 % → 10 % | 3.5 px | 0.35 | 2.27 | 2 |
| stroke 26 | 3 % → 6 % | 2.7 px | 0.35 | 1.81 | 2 |
| stroke 27 | 3 % → 7 % | 2.3 px | 0.35 | 2.26 | 2 |
| stroke 28 | 6 % → 10 % | 4.5 px | 0.35 | 1.70 | 5 |
| stroke 29 | 3 % → 13 % | 2.4 px | 0.35 | 4.21 | 3 |
| stroke 30 | 6 % → 9 % | 4.4 px | 0.35 | 1.46 | 3 |
| stroke 31 | 7 % → 14 % | 5.1 px | 0.35 | 2.14 | 2 |
| stroke 32 | 3 % → 6 % | 2.5 px | 0.35 | 1.78 | 3 |
| stroke 33 | 6 % → 11 % | 5.0 px | 0.35 | 1.67 | 2 |
| stroke 34 | 3 % → 6 % | 2.6 px | 0.35 | 1.73 | 8 |
| stroke 35 | 7 % → 14 % | 5.0 px | 0.35 | 2.09 | 3 |
| stroke 36 | 5 % → 5 % | 3.7 px | 0.35 | 1.01 | 3 |
| stroke 37 | 7 % → 15 % | 5.2 px | 0.35 | 2.15 | 3 |
| stroke 38 | 8 % → 13 % | 5.8 px | 0.35 | 1.66 | 2 |
| stroke 39 | 7 % → 11 % | 5.1 px | 0.35 | 1.67 | 2 |
| stroke 40 | 8 % → 18 % | 6.2 px | 0.35 | 2.21 | 5 |
| stroke 41 | 9 % → 13 % | 6.9 px | 0.35 | 1.48 | 5 |
| stroke 42 | 10 % → 17 % | 7.7 px | 0.35 | 1.73 | 2 |
| stroke 43 | 5 % → 9 % | 3.9 px | 0.35 | 1.66 | 10 |
| stroke 44 | 10 % → 13 % | 7.3 px | 0.35 | 1.40 | 2 |
| stroke 45 | 13 % → 18 % | 9.9 px | 0.35 | 1.35 | 3 |
| stroke 46 | 5 % → 7 % | 3.6 px | 0.34 | 1.41 | 6 |
| stroke 47 | 11 % → 13 % | 8.0 px | 0.35 | 1.20 | 2 |
| stroke 48 | 12 % → 16 % | 9.2 px | 0.35 | 1.34 | 2 |
| stroke 49 | 6 % → 9 % | 4.2 px | 0.35 | 1.65 | 7 |
| stroke 50 | 7 % → 7 % | 5.2 px | 0.34 | 1.00 | 2 |
| stroke 51 | 8 % → 15 % | 6.4 px | 0.35 | 1.74 | 3 |
| stroke 52 | 12 % → 14 % | 9.1 px | 0.35 | 1.19 | 3 |
| stroke 53 | 11 % → 14 % | 8.1 px | 0.35 | 1.36 | 4 |
| stroke 54 | 10 % → 14 % | 7.4 px | 0.35 | 1.47 | 5 |
| stroke 55 | 11 % → 14 % | 8.2 px | 0.35 | 1.33 | 2 |
| stroke 56 | 11 % → 12 % | 8.4 px | 0.35 | 1.11 | 7 |
| stroke 57 | 9 % → 13 % | 7.1 px | 0.35 | 1.37 | 6 |
| stroke 58 | 10 % → 11 % | 7.7 px | 0.35 | 1.14 | 3 |
| stroke 59 | 11 % → 13 % | 8.4 px | 0.35 | 1.18 | 3 |
| stroke 60 | 16 % → 20 % | 11.9 px | 0.35 | 1.26 | 2 |
| stroke 61 | 19 % → 20 % | 14.5 px | 0.35 | 1.04 | 3 |
| stroke 62 | 10 % → 10 % | 7.3 px | 0.35 | 1.00 | 2 |
| stroke 63 | 11 % → 12 % | 8.7 px | 0.35 | 1.07 | 3 |
| stroke 64 | 14 % → 14 % | 10.7 px | 0.35 | 1.02 | 2 |
| stroke 65 | 15 % → 15 % | 11.5 px | 0.35 | 1.00 | 3 |
| stroke 66 | 14 % → 14 % | 10.7 px | 0.35 | 1.00 | 7 |
| stroke 67 | 12 % → 12 % | 8.8 px | 0.35 | 1.06 | 3 |
| stroke 68 | 5 % → 9 % | 3.6 px | 0.35 | 1.88 | 3 |
| stroke 69 | 5 % → 5 % | 4.1 px | 0.35 | 1.00 | 5 |
| stroke 70 | 10 % → 13 % | 7.4 px | 0.35 | 1.28 | 3 |
| stroke 71 | 9 % → 11 % | 7.1 px | 0.35 | 1.15 | 2 |
| stroke 72 | 5 % → 7 % | 4.2 px | 0.35 | 1.23 | 5 |
| stroke 73 | 12 % → 12 % | 9.3 px | 0.35 | 1.00 | 7 |
| stroke 74 | 14 % → 14 % | 10.8 px | 0.35 | 1.00 | 5 |
| stroke 75 | 15 % → 15 % | 11.4 px | 0.35 | 1.00 | 3 |
| stroke 76 | 14 % → 14 % | 10.5 px | 0.35 | 1.00 | 5 |
| stroke 77 | 7 % → 10 % | 5.4 px | 0.35 | 1.34 | 6 |
| stroke 78 | 9 % → 9 % | 7.0 px | 0.35 | 1.00 | 4 |
| stroke 79 | 7 % → 7 % | 5.7 px | 0.35 | 1.00 | 2 |
| stroke 80 | 11 % → 11 % | 8.3 px | 0.35 | 1.00 | 4 |

Numbers say: wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #42 Oil pastel shaggy — own sheet
own sheet 600 × 600 · Pastel 1.00 · 18 px · 2.6 s

![Brush Artist · Refs · #42 Oil pastel shaggy — own sheet](Brush-Artist-Refs-42-Oil-pastel-shaggy-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 5 % → 27 % | 8.0 px | 0.28 | 5.73 | 6 |
| stroke 2 | 5 % → 24 % | 8.6 px | 0.28 | 4.69 | 13 |
| stroke 3 | 5 % → 29 % | 8.9 px | 0.28 | 5.42 | 8 |
| stroke 4 | 5 % → 11 % | 8.8 px | 0.28 | 2.08 | 9 |
| stroke 5 | 6 % → 11 % | 9.9 px | 0.28 | 1.85 | 11 |
| stroke 6 | 8 % → 37 % | 13.9 px | 0.29 | 4.44 | 6 |
| stroke 7 | 11 % → 31 % | 17.6 px | 0.28 | 2.90 | 18 |
| stroke 8 | 7 % → 38 % | 11.4 px | 0.28 | 5.55 | 14 |
| stroke 9 | 8 % → 21 % | 13.9 px | 0.28 | 2.53 | 6 |
| stroke 10 | 8 % → 18 % | 13.2 px | 0.28 | 2.32 | 9 |
| stroke 11 | 6 % → 27 % | 9.4 px | 0.28 | 4.74 | 10 |
| stroke 12 | 8 % → 19 % | 13.6 px | 0.28 | 2.29 | 10 |
| stroke 13 | 13 % → 24 % | 21.0 px | 0.28 | 1.92 | 12 |
| stroke 14 | 5 % → 23 % | 7.9 px | 0.28 | 4.77 | 8 |
| stroke 15 | 5 % → 24 % | 9.0 px | 0.29 | 4.38 | 9 |
| stroke 16 | 9 % → 21 % | 15.7 px | 0.29 | 2.18 | 12 |
| stroke 17 | 17 % → 39 % | 28.0 px | 0.29 | 2.34 | 13 |
| stroke 18 | 14 % → 25 % | 22.8 px | 0.29 | 1.79 | 6 |
| stroke 19 | 15 % → 32 % | 24.9 px | 0.28 | 2.09 | 8 |
| stroke 20 | 21 % → 39 % | 35.1 px | 0.28 | 1.85 | 6 |
| stroke 21 | 9 % → 16 % | 14.4 px | 0.28 | 1.88 | 17 |
| stroke 22 | 14 % → 17 % | 23.9 px | 0.28 | 1.20 | 7 |
| stroke 23 | 12 % → 17 % | 20.6 px | 0.29 | 1.34 | 9 |
| stroke 24 | 18 % → 26 % | 30.0 px | 0.29 | 1.44 | 11 |
| stroke 25 | 20 % → 34 % | 32.6 px | 0.28 | 1.74 | 7 |
| stroke 26 | 6 % → 14 % | 9.2 px | 0.28 | 2.43 | 6 |
| stroke 27 | 18 % → 26 % | 30.5 px | 0.29 | 1.41 | 9 |
| stroke 28 | 14 % → 24 % | 23.7 px | 0.28 | 1.68 | 12 |
| stroke 29 | 9 % → 27 % | 14.9 px | 0.29 | 3.01 | 6 |
| stroke 30 | 15 % → 36 % | 25.0 px | 0.29 | 2.43 | 10 |
| stroke 31 | 14 % → 17 % | 23.3 px | 0.28 | 1.23 | 10 |
| stroke 32 | 16 % → 29 % | 27.0 px | 0.29 | 1.82 | 11 |
| stroke 33 | 15 % → 16 % | 24.5 px | 0.29 | 1.09 | 12 |
| stroke 34 | 19 % → 27 % | 31.4 px | 0.28 | 1.44 | 6 |
| stroke 35 | 26 % → 36 % | 42.6 px | 0.28 | 1.40 | 6 |
| stroke 36 | 25 % → 34 % | 41.0 px | 0.28 | 1.36 | 13 |
| stroke 37 | 12 % → 12 % | 19.3 px | 0.28 | 1.03 | 6 |
| stroke 38 | 19 % → 25 % | 31.7 px | 0.28 | 1.30 | 6 |
| stroke 39 | 16 % → 22 % | 27.3 px | 0.28 | 1.37 | 12 |
| stroke 40 | 22 % → 31 % | 36.6 px | 0.28 | 1.38 | 14 |
| stroke 41 | 32 % → 36 % | 53.1 px | 0.28 | 1.12 | 11 |
| stroke 42 | 23 % → 30 % | 38.2 px | 0.29 | 1.29 | 7 |
| stroke 43 | 12 % → 12 % | 20.3 px | 0.28 | 1.00 | 6 |
| stroke 44 | 30 % → 37 % | 48.9 px | 0.28 | 1.26 | 9 |
| stroke 45 | 16 % → 16 % | 26.2 px | 0.28 | 1.00 | 8 |
| stroke 46 | 29 % → 34 % | 48.0 px | 0.29 | 1.15 | 6 |
| stroke 47 | 38 % → 41 % | 62.0 px | 0.28 | 1.10 | 7 |
| stroke 48 | 29 % → 36 % | 47.8 px | 0.29 | 1.27 | 12 |
| stroke 49 | 27 % → 30 % | 45.1 px | 0.29 | 1.11 | 6 |
| stroke 50 | 38 % → 40 % | 63.4 px | 0.28 | 1.06 | 11 |
| stroke 51 | 16 % → 16 % | 26.1 px | 0.28 | 1.00 | 10 |
| stroke 52 | 37 % → 38 % | 62.4 px | 0.29 | 1.01 | 7 |
| stroke 53 | 22 % → 26 % | 36.9 px | 0.28 | 1.18 | 6 |
| stroke 54 | 17 % → 19 % | 29.1 px | 0.29 | 1.09 | 11 |
| stroke 55 | 15 % → 15 % | 25.0 px | 0.28 | 1.00 | 12 |
| stroke 56 | 13 % → 14 % | 21.6 px | 0.28 | 1.08 | 8 |
| stroke 57 | 23 % → 23 % | 37.7 px | 0.29 | 1.00 | 9 |
| stroke 58 | 28 % → 29 % | 46.1 px | 0.28 | 1.05 | 9 |
| stroke 59 | 40 % → 40 % | 67.3 px | 0.28 | 1.00 | 13 |
| stroke 60 | 22 % → 22 % | 35.6 px | 0.28 | 1.00 | 7 |

Numbers say: wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #43 Dragged black ink blocks — own sheet
own sheet 600 × 600 · Gouache 1.00 · 70 px · 6.4 s

![Brush Artist · Refs · #43 Dragged black ink blocks — own sheet](Brush-Artist-Refs-43-Dragged-black-ink-blocks-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 15 % → 8 % | 35.8 px | 0.46 | 0.54 | 349 |
| stroke 2 | 18 % → 13 % | 62.1 px | 0.46 | 0.75 | 360 |
| stroke 3 | 19 % → 14 % | 68.8 px | 0.46 | 0.75 | 381 |
| stroke 4 | 19 % → 13 % | 67.6 px | 0.46 | 0.65 | 372 |
| stroke 5 | 26 % → 14 % | 61.7 px | 0.46 | 0.54 | 380 |

## Brush Artist · Refs · #44 Blue looping ribbon — own sheet
own sheet 600 × 600 · Oil 1.00 · 80 px · 4.5 s

![Brush Artist · Refs · #44 Blue looping ribbon — own sheet](Brush-Artist-Refs-44-Blue-looping-ribbon-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 32 % → 32 % | 42.0 px | 0.78 | 1.00 | 2392 |

## Brush Artist · Refs · #45 Soft pastel pepper — own sheet
own sheet 600 × 600 · Pastel 1.00 · 40 px · 4.2 s

![Brush Artist · Refs · #45 Soft pastel pepper — own sheet](Brush-Artist-Refs-45-Soft-pastel-pepper-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 10 % → 39 % | 11.3 px | 0.49 | 3.75 | 322 |
| stroke 2 | 18 % → 34 % | 21.3 px | 0.49 | 1.87 | 295 |
| stroke 3 | 25 % → 37 % | 17.6 px | 0.49 | 1.46 | 255 |
| stroke 4 | 24 % → 35 % | 30.5 px | 0.49 | 1.43 | 309 |
| stroke 5 | 30 % → 30 % | 21.2 px | 0.49 | 1.00 | 304 |
| stroke 6 | 36 % → 44 % | 23.0 px | 0.48 | 1.23 | 271 |
| stroke 7 | 39 % → 43 % | 21.6 px | 0.48 | 1.10 | 323 |
| stroke 8 | 44 % → 44 % | 44.4 px | 0.49 | 1.00 | 297 |

Numbers say: wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #46 Red-brown ink lips — own sheet
own sheet 600 × 600 · Watercolour 1.00 · 50 px · 6.1 s

![Brush Artist · Refs · #46 Red-brown ink lips — own sheet](Brush-Artist-Refs-46-Red-brown-ink-lips-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 13 % → 29 % | 55.7 px | 0.55 | 2.17 | 100 |
| stroke 2 | 18 % → 36 % | 81.1 px | 0.50 | 1.95 | 94 |

Numbers say: wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #47 Pink knife slabs — own sheet
own sheet 600 × 600 · Impasto 1.00 · 90 px · 4.0 s

![Brush Artist · Refs · #47 Pink knife slabs — own sheet](Brush-Artist-Refs-47-Pink-knife-slabs-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 17 % → 32 % | 83.2 px | 0.11 | 1.94 | 276 |
| stroke 2 | 29 % → 43 % | 165.8 px | 0.11 | 1.46 | 282 |
| stroke 3 | 29 % → 43 % | 165.7 px | 0.11 | 1.47 | 251 |
| stroke 4 | 39 % → 38 % | 165.7 px | 0.11 | 0.98 | 267 |

Numbers say: wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #48 Black bands with drips — own sheet
own sheet 600 × 600 · Gouache 1.00 · 70 px · 10.0 s

![Brush Artist · Refs · #48 Black bands with drips — own sheet](Brush-Artist-Refs-48-Black-bands-with-drips-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 28 % → 41 % | 73.2 px | 0.39 | 1.46 | 449 |
| stroke 2 | 43 % → 57 % | 137.5 px | 0.39 | 1.33 | 444 |
| stroke 3 | 45 % → 57 % | 141.4 px | 0.39 | 1.27 | 470 |
| stroke 4 | 48 % → 46 % | 140.3 px | 0.39 | 0.96 | 460 |

## Brush Artist · Refs · #49 Magenta letters round brush — own sheet
own sheet 600 × 600 · Ink 1.00 · 30 px · 8.6 s

![Brush Artist · Refs · #49 Magenta letters round brush — own sheet](Brush-Artist-Refs-49-Magenta-letters-round-brush-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 27 % → 46 % | 64.3 px | 0.52 | 1.70 | 30 |
| stroke 2 | 29 % → 40 % | 52.5 px | 0.53 | 1.40 | 31 |
| stroke 3 | 41 % → 67 % | 96.3 px | 0.52 | 1.64 | 33 |
| stroke 4 | 34 % → 52 % | 53.7 px | 0.52 | 1.55 | 107 |
| stroke 5 | 40 % → 66 % | 94.7 px | 0.52 | 1.65 | 71 |
| stroke 6 | 54 % → 70 % | 231.2 px | 0.52 | 1.29 | 14 |
| stroke 7 | 41 % → 56 % | 63.9 px | 0.52 | 1.35 | 104 |
| stroke 8 | 36 % → 61 % | 91.9 px | 0.53 | 1.73 | 69 |
| stroke 9 | 49 % → 60 % | 152.9 px | 0.53 | 1.24 | 28 |
| stroke 10 | 42 % → 72 % | 100.4 px | 0.52 | 1.71 | 69 |
| stroke 11 | 52 % → 72 % | 219.8 px | 0.52 | 1.39 | 16 |
| stroke 12 | 53 % → 68 % | 82.2 px | 0.52 | 1.29 | 106 |
| stroke 13 | 42 % → 54 % | 115.9 px | 0.53 | 1.29 | 34 |
| stroke 14 | 45 % → 69 % | 131.7 px | 0.53 | 1.52 | 38 |
| stroke 15 | 43 % → 63 % | 102.4 px | 0.52 | 1.46 | 69 |
| stroke 16 | 52 % → 61 % | 220.3 px | 0.52 | 1.18 | 20 |
| stroke 17 | 53 % → 64 % | 82.2 px | 0.52 | 1.19 | 121 |
| stroke 18 | 36 % → 44 % | 99.6 px | 0.52 | 1.22 | 38 |
| stroke 19 | 54 % → 53 % | 123.7 px | 0.52 | 0.99 | 33 |
| stroke 20 | 54 % → 54 % | 125.3 px | 0.52 | 1.00 | 27 |
| stroke 21 | 49 % → 49 % | 81.3 px | 0.52 | 1.00 | 80 |

Numbers say: wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #50 Thick swipes on photo — own sheet
own sheet 600 × 600 · Impasto 1.00 · 40 px · 2.7 s

![Brush Artist · Refs · #50 Thick swipes on photo — own sheet](Brush-Artist-Refs-50-Thick-swipes-on-photo-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 9 % → 21 % | 42.8 px | 0.33 | 2.35 | 33 |
| stroke 2 | 9 % → 16 % | 42.5 px | 0.33 | 1.79 | 29 |
| stroke 3 | 10 % → 11 % | 41.9 px | 0.33 | 1.07 | 47 |
| stroke 4 | 11 % → 18 % | 42.7 px | 0.33 | 1.64 | 39 |
| stroke 5 | 11 % → 10 % | 41.9 px | 0.33 | 0.95 | 32 |
| stroke 6 | 17 % → 21 % | 97.7 px | 0.32 | 1.20 | 25 |
| stroke 7 | 22 % → 26 % | 92.8 px | 0.33 | 1.18 | 39 |
| stroke 8 | 21 % → 21 % | 119.9 px | 0.33 | 0.97 | 32 |
| stroke 9 | 9 % → 10 % | 42.1 px | 0.32 | 1.09 | 33 |
| stroke 10 | 22 % → 21 % | 73.6 px | 0.32 | 0.96 | 44 |
| stroke 11 | 9 % → 8 % | 42.7 px | 0.33 | 0.95 | 32 |
| stroke 12 | 17 % → 16 % | 93.2 px | 0.33 | 0.96 | 24 |

Numbers say: wet paint spreads well beyond the stroke.

## Brush Artist · Ink — dry brush — own sheet
own sheet 600 × 600 · Gouache 1.00 · 30 px · 2.8 s

![Brush Artist · Ink — dry brush — own sheet](Brush-Artist-Ink-dry-brush-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| ear | 6 % → 2 % | 7.0 px | 0.86 | 0.34 | 396 |
| drag0 | 6 % → 9 % | 11.3 px | 0.86 | 1.42 | 114 |
| drag1 | 9 % → 9 % | 18.5 px | 0.86 | 1.02 | 98 |
| drag2 | 11 % → 10 % | 25.6 px | 0.86 | 0.85 | 72 |
| drag3 | 13 % → 10 % | 32.8 px | 0.86 | 0.77 | 67 |

## Brush Artist · Watercolour — blue — own sheet
own sheet 600 × 600 · Watercolour 0.93 · Ink 0.07 · 40 px · 8.8 s

![Brush Artist · Watercolour — blue — own sheet](Brush-Artist-Watercolour-blue-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| s0 | 7 % → 24 % | 28.8 px | 0.30 | 3.32 | 42 |
| s1 | 6 % → 33 % | 10.1 px | 0.37 | 6.00 | 41 |
| s2 | 10 % → 19 % | 44.2 px | 0.26 | 1.81 | 31 |
| s3 | 10 % → 18 % | 26.7 px | 0.31 | 1.92 | 48 |
| s4 | 14 % → 30 % | 38.6 px | 0.36 | 2.16 | 63 |
| s5 | 19 % → 29 % | 39.3 px | 0.37 | 1.54 | 45 |
| s6 | 18 % → 22 % | 48.7 px | 0.31 | 1.25 | 51 |
| s7 | 25 % → 36 % | 32.7 px | 0.37 | 1.46 | 38 |
| s8 | 21 % → 25 % | 79.8 px | 0.30 | 1.20 | 43 |

Numbers say: wet paint spreads well beyond the stroke.

## Brush Artist · Charcoal — stick — own sheet
own sheet 600 × 600 · Charcoal 0.78 · Pastel 0.22 · 28 px · 1.1 s

![Brush Artist · Charcoal — stick — own sheet](Brush-Artist-Charcoal-stick-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| finger0 | 12 % → 25 % | 21.7 px | 0.83 | 2.02 | 39 |
| tip0 | 12 % → 21 % | 33.4 px | 0.83 | 1.69 | 13 |
| finger1 | 23 % → 40 % | 41.1 px | 0.83 | 1.71 | 30 |
| tip1 | 21 % → 29 % | 56.0 px | 0.83 | 1.41 | 7 |
| finger2 | 23 % → 35 % | 41.3 px | 0.83 | 1.53 | 34 |
| tip2 | 21 % → 29 % | 56.0 px | 0.83 | 1.41 | 14 |
| finger3 | 23 % → 27 % | 41.6 px | 0.83 | 1.15 | 31 |
| tip3 | 21 % → 21 % | 56.3 px | 0.83 | 1.00 | 7 |
| cig0 | 33 % → 46 % | 73.2 px | 0.83 | 1.40 | 16 |
| cig1 | 35 % → 46 % | 78.8 px | 0.83 | 1.29 | 19 |
| cig2 | 38 % → 46 % | 84.4 px | 0.83 | 1.21 | 16 |
| cig3 | 40 % → 46 % | 90.0 px | 0.83 | 1.13 | 13 |
| cig4 | 43 % → 45 % | 95.5 px | 0.83 | 1.06 | 15 |
| cig5 | 45 % → 45 % | 101.1 px | 0.83 | 1.00 | 15 |

Numbers say: wet paint spreads well beyond the stroke.

## Oil · Henry Ward · HW #02 cream over wet olive — own sheet
own sheet 600 × 600 · Oil 0.81 · Ink 0.19 · 56 px · 18.7 s

![Oil · Henry Ward · HW #02 cream over wet olive — own sheet](Oil-Henry-Ward-HW-02-cream-over-wet-olive-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 65 % → 28 % | 78.9 px | 0.26 | 0.43 | 1231 |
| stroke 2 | 79 % → 40 % | 144.9 px | 0.34 | 0.51 | 1590 |
| stroke 3 | 82 % → 57 % | 170.5 px | 0.31 | 0.69 | 1575 |
| stroke 4 | 81 % → 64 % | 169.5 px | 0.33 | 0.79 | 1523 |
| stroke 5 | 82 % → 55 % | 170.6 px | 0.37 | 0.67 | 1375 |
| stroke 6 | 81 % → 52 % | 173.4 px | 0.38 | 0.65 | 1278 |
| stroke 7 | 81 % → 39 % | 170.6 px | 0.38 | 0.48 | 1217 |
| stroke 8 | 93 % → 28 % | 169.8 px | 0.32 | 0.30 | 1203 |
| stroke 9 | 100 % → 18 % | 123.5 px | 0.15 | 0.18 | 952 |
| stroke 10 | 12 % → 45 % | 49.3 px | 0.32 | 3.62 | 149 |
| stroke 11 | 23 % → 65 % | 93.7 px | 0.34 | 2.81 | 165 |
| stroke 12 | 11 % → 38 % | 49.1 px | 0.37 | 3.38 | 118 |
| stroke 13 | 29 % → 50 % | 115.4 px | 0.30 | 1.72 | 116 |
| stroke 14 | 36 % → 54 % | 130.5 px | 0.31 | 1.50 | 145 |
| stroke 15 | 44 % → 66 % | 163.4 px | 0.32 | 1.49 | 150 |
| stroke 16 | 53 % → 77 % | 263.9 px | 0.32 | 1.46 | 103 |
| stroke 17 | 36 % → 61 % | 129.9 px | 0.38 | 1.67 | 139 |
| stroke 18 | 34 % → 64 % | 135.1 px | 0.37 | 1.86 | 116 |
| stroke 19 | 38 % → 60 % | 176.9 px | 0.35 | 1.58 | 102 |
| stroke 20 | 33 % → 42 % | 129.3 px | 0.38 | 1.27 | 131 |
| stroke 21 | 33 % → 37 % | 116.7 px | 0.38 | 1.15 | 167 |
| stroke 22 | 44 % → 46 % | 149.0 px | 0.31 | 1.04 | 179 |
| stroke 23 | 57 % → 59 % | 205.6 px | 0.31 | 1.04 | 173 |
| stroke 24 | 55 % → 61 % | 242.2 px | 0.38 | 1.11 | 109 |
| stroke 25 | 55 % → 56 % | 207.1 px | 0.38 | 1.03 | 161 |
| stroke 26 | 39 % → 39 % | 163.3 px | 0.38 | 0.99 | 161 |

Numbers say: wet paint spreads well beyond the stroke.

## Oil · Henry Ward · HW #04 grey arcs over ochre — own sheet
own sheet 600 × 600 · Oil 1.00 · 46 px · 18.5 s

![Oil · Henry Ward · HW #04 grey arcs over ochre — own sheet](Oil-Henry-Ward-HW-04-grey-arcs-over-ochre-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 76 % → 38 % | 82.2 px | 0.18 | 0.51 | 1271 |
| stroke 2 | 87 % → 53 % | 143.6 px | 0.19 | 0.61 | 1593 |
| stroke 3 | 88 % → 77 % | 156.0 px | 0.19 | 0.87 | 1562 |
| stroke 4 | 88 % → 61 % | 154.9 px | 0.18 | 0.70 | 1458 |
| stroke 5 | 88 % → 46 % | 154.1 px | 0.15 | 0.52 | 1405 |
| stroke 6 | 86 % → 31 % | 151.2 px | 0.12 | 0.36 | 1231 |
| stroke 7 | 88 % → 36 % | 155.5 px | 0.11 | 0.42 | 1224 |
| stroke 8 | 90 % → 29 % | 150.8 px | 0.11 | 0.32 | 1226 |
| stroke 9 | 100 % → 24 % | 104.1 px | 0.11 | 0.24 | 939 |
| stroke 10 | 10 % → 69 % | 36.0 px | 0.19 | 7.12 | 131 |
| stroke 11 | 16 % → 58 % | 56.7 px | 0.18 | 3.51 | 158 |
| stroke 12 | 19 % → 56 % | 74.1 px | 0.16 | 2.88 | 99 |
| stroke 13 | 32 % → 67 % | 88.9 px | 0.18 | 2.06 | 205 |
| stroke 14 | 36 % → 65 % | 140.1 px | 0.18 | 1.78 | 148 |
| stroke 15 | 37 % → 58 % | 128.0 px | 0.18 | 1.57 | 205 |
| stroke 16 | 43 % → 60 % | 159.5 px | 0.17 | 1.39 | 116 |
| stroke 17 | 48 % → 65 % | 178.7 px | 0.18 | 1.37 | 183 |
| stroke 18 | 48 % → 61 % | 165.9 px | 0.17 | 1.25 | 137 |
| stroke 19 | 54 % → 68 % | 178.1 px | 0.18 | 1.25 | 205 |
| stroke 20 | 57 % → 72 % | 176.4 px | 0.18 | 1.26 | 193 |
| stroke 21 | 61 % → 75 % | 196.3 px | 0.18 | 1.24 | 168 |
| stroke 22 | 34 % → 55 % | 124.1 px | 0.17 | 1.62 | 143 |
| stroke 23 | 57 % → 66 % | 206.1 px | 0.18 | 1.17 | 195 |
| stroke 24 | 74 % → 79 % | 284.2 px | 0.18 | 1.07 | 118 |
| stroke 25 | 55 % → 66 % | 187.4 px | 0.17 | 1.21 | 171 |
| stroke 26 | 73 % → 76 % | 255.1 px | 0.18 | 1.04 | 134 |
| stroke 27 | 27 % → 35 % | 82.4 px | 0.12 | 1.31 | 111 |
| stroke 28 | 26 % → 44 % | 91.9 px | 0.11 | 1.71 | 102 |
| stroke 29 | 25 % → 34 % | 99.9 px | 0.11 | 1.39 | 74 |
| stroke 30 | 32 % → 32 % | 94.0 px | 0.11 | 1.00 | 117 |

Numbers say: wet paint spreads well beyond the stroke.

## Oil · Henry Ward · HW #09 white arches over wet blue-grey — own sheet
own sheet 600 × 600 · Oil 1.00 · 46 px · 18.7 s

![Oil · Henry Ward · HW #09 white arches over wet blue-grey — own sheet](Oil-Henry-Ward-HW-09-white-arches-over-wet-blue-grey-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 79 % → 0 % | 80.8 px | 0.20 | 0.00 | 1198 |
| stroke 2 | 87 % → 6 % | 142.0 px | 0.11 | 0.06 | 1590 |
| stroke 3 | 87 % → 22 % | 155.8 px | 0.11 | 0.25 | 1540 |
| stroke 4 | 88 % → 38 % | 157.5 px | 0.11 | 0.43 | 1420 |
| stroke 5 | 86 % → 52 % | 152.0 px | 0.12 | 0.61 | 1345 |
| stroke 6 | 87 % → 62 % | 149.6 px | 0.12 | 0.71 | 1184 |
| stroke 7 | 87 % → 64 % | 152.7 px | 0.13 | 0.73 | 1183 |
| stroke 8 | 89 % → 57 % | 152.3 px | 0.16 | 0.63 | 1183 |
| stroke 9 | 100 % → 48 % | 99.6 px | 0.19 | 0.48 | 900 |
| stroke 10 | 7 % → 51 % | 28.2 px | 0.14 | 7.22 | 190 |
| stroke 11 | 15 % → 62 % | 28.6 px | 0.14 | 4.01 | 264 |
| stroke 12 | 18 % → 59 % | 32.8 px | 0.14 | 3.26 | 322 |
| stroke 13 | 25 % → 72 % | 55.7 px | 0.14 | 2.86 | 215 |
| stroke 14 | 28 % → 68 % | 19.9 px | 0.15 | 2.45 | 360 |
| stroke 15 | 35 % → 72 % | 98.2 px | 0.14 | 2.06 | 249 |
| stroke 16 | 44 % → 67 % | 131.2 px | 0.14 | 1.52 | 179 |
| stroke 17 | 55 % → 83 % | 157.4 px | 0.14 | 1.52 | 181 |
| stroke 18 | 47 % → 67 % | 128.8 px | 0.14 | 1.42 | 250 |
| stroke 19 | 52 % → 64 % | 160.9 px | 0.14 | 1.22 | 211 |
| stroke 20 | 48 % → 67 % | 123.9 px | 0.14 | 1.41 | 255 |
| stroke 21 | 35 % → 54 % | 89.8 px | 0.12 | 1.55 | 173 |
| stroke 22 | 47 % → 56 % | 125.1 px | 0.13 | 1.20 | 211 |
| stroke 23 | 65 % → 72 % | 205.0 px | 0.13 | 1.11 | 249 |
| stroke 24 | 63 % → 67 % | 202.0 px | 0.12 | 1.07 | 134 |
| stroke 25 | 55 % → 62 % | 155.1 px | 0.14 | 1.13 | 170 |
| stroke 26 | 61 % → 70 % | 235.4 px | 0.16 | 1.15 | 102 |
| stroke 27 | 52 % → 57 % | 126.6 px | 0.15 | 1.09 | 164 |
| stroke 28 | 56 % → 56 % | 130.0 px | 0.17 | 1.00 | 125 |

Numbers say: wet paint spreads well beyond the stroke.

## Oil · Henry Ward · HW #03 navy contours over wet band — own sheet
own sheet 600 × 600 · Oil 1.00 · 46 px · 15.0 s

![Oil · Henry Ward · HW #03 navy contours over wet band — own sheet](Oil-Henry-Ward-HW-03-navy-contours-over-wet-band-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 77 % → 17 % | 78.3 px | 0.75 | 0.23 | 1158 |
| stroke 2 | 87 % → 22 % | 146.2 px | 0.73 | 0.25 | 1563 |
| stroke 3 | 86 % → 27 % | 151.4 px | 0.65 | 0.32 | 1549 |
| stroke 4 | 86 % → 39 % | 151.1 px | 0.58 | 0.45 | 1400 |
| stroke 5 | 85 % → 42 % | 151.4 px | 0.52 | 0.49 | 1316 |
| stroke 6 | 88 % → 35 % | 154.6 px | 0.55 | 0.39 | 1175 |
| stroke 7 | 88 % → 22 % | 150.7 px | 0.60 | 0.25 | 1185 |
| stroke 8 | 89 % → 9 % | 151.4 px | 0.72 | 0.10 | 1182 |
| stroke 9 | 100 % → 3 % | 104.1 px | 0.73 | 0.03 | 934 |
| stroke 10 | 9 % → 41 % | 39.2 px | 0.55 | 4.41 | 67 |
| stroke 11 | 18 % → 49 % | 67.7 px | 0.53 | 2.72 | 86 |
| stroke 12 | 22 % → 43 % | 78.6 px | 0.51 | 1.96 | 96 |
| stroke 13 | 26 % → 41 % | 89.0 px | 0.54 | 1.59 | 108 |
| stroke 14 | 13 % → 30 % | 41.2 px | 0.75 | 2.37 | 44 |
| stroke 15 | 17 % → 31 % | 62.7 px | 0.74 | 1.76 | 63 |
| stroke 16 | 27 % → 28 % | 61.8 px | 0.59 | 1.04 | 252 |
| stroke 17 | 31 % → 31 % | 81.3 px | 0.59 | 1.00 | 175 |

Numbers say: wet paint spreads well beyond the stroke.

