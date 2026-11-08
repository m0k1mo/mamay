![All brushes](contact.png)

# Brush Lab — 241 brushes · 8 Nov 2026 at 14:06

Every sheet: 1500 × 600, ten strokes in a 5 × 2 grid — 1. light line · 2. heavy line · 3. pressure swell · 4. fast wave · 5. slow wave · 6. spiral · 7. loop · 8. tilted · 9. over the wet one · 10. long, no reload (cell 8 holds «tilted» and «over the wet one» crossed). The CPU reference of Mamay's paint engine; the wet layer settles 20 s at the end.

Columns: **covered** = share of the cell with paint right after the stroke → after settling; **width** = painted area of the stroke ÷ its length (px); **dark** = mean darkness of the painted pixels above the paper's own grain (0 = paper, 1 = black); **spread** = how far wet paint went beyond the stroke (1.0 = stayed); **ms** = the stroke on the CPU; long stroke: paint in each quarter of its length (it should run out: wet → streaks → dry tail).

## Ink Line
Ink · 12 px · 25.0 s

![Ink Line](Ink-Line.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 1 % → 4 % | 4.3 px | 0.55 | 2.45 | 110 |
| heavy line | 5 % → 6 % | 15.7 px | 0.68 | 1.14 | 82 |
| pressure swell | 3 % → 4 % | 11.3 px | 0.64 | 1.40 | 45 |
| fast wave | 10 % → 11 % | 11.2 px | 0.59 | 1.11 | 139 |
| slow wave | 8 % → 10 % | 9.6 px | 0.57 | 1.16 | 136 |
| spiral | 14 % → 15 % | 8.9 px | 0.49 | 1.07 | 168 |
| loop | 8 % → 9 % | 10.6 px | 0.61 | 1.15 | 114 |
| tilted | 5 % → 5 % | 14.3 px | 0.64 | 1.05 | 61 |
| over the wet one | 10 % → 11 % | 12.5 px | 0.64 | 1.15 | 49 |
| long, no reload | 18 % → 17 % | 8.1 px | 0.47 | 0.96 | 421 | quarters: 0.22 → 0.09 → 0.04 → 0.02

Numbers say: light vs heavy: width 4.3 → 15.7 px, dark 0.55 → 0.68; wet paint spreads well beyond the stroke.

## Dense Ink
Ink · 14 px · 25.6 s

![Dense Ink](Dense-Ink.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 5 % → 7 % | 15.2 px | 0.72 | 1.27 | 98 |
| heavy line | 7 % → 7 % | 19.1 px | 0.73 | 1.09 | 94 |
| pressure swell | 5 % → 6 % | 17.9 px | 0.72 | 1.18 | 62 |
| fast wave | 13 % → 13 % | 15.2 px | 0.69 | 1.01 | 161 |
| slow wave | 12 % → 12 % | 13.5 px | 0.67 | 1.04 | 162 |
| spiral | 18 % → 15 % | 12.2 px | 0.65 | 0.80 | 214 |
| loop | 11 % → 12 % | 14.8 px | 0.69 | 1.08 | 122 |
| tilted | 5 % → 6 % | 14.5 px | 0.72 | 1.07 | 67 |
| over the wet one | 12 % → 13 % | 17.7 px | 0.72 | 1.12 | 48 |
| long, no reload | 23 % → 15 % | 10.1 px | 0.64 | 0.66 | 383 | quarters: 0.30 → 0.12 → 0.04 → 0.02

Numbers say: light vs heavy: width 15.2 → 19.1 px, dark 0.72 → 0.73.

## Transparent Wash
Watercolor · 22 px · 26.5 s

![Transparent Wash](Transparent-Wash.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 2 % → 5 % | 6.9 px | 0.27 | 2.26 | 84 |
| heavy line | 7 % → 9 % | 20.4 px | 0.27 | 1.23 | 57 |
| pressure swell | 4 % → 6 % | 15.2 px | 0.28 | 1.54 | 36 |
| fast wave | 14 % → 16 % | 16.1 px | 0.20 | 1.17 | 135 |
| slow wave | 12 % → 15 % | 13.7 px | 0.21 | 1.28 | 200 |
| spiral | 18 % → 22 % | 11.9 px | 0.16 | 1.22 | 164 |
| loop | 11 % → 13 % | 14.5 px | 0.22 | 1.20 | 113 |
| tilted | 8 % → 8 % | 21.1 px | 0.24 | 1.06 | 74 |
| over the wet one | 13 % → 16 % | 16.4 px | 0.24 | 1.19 | 46 |
| long, no reload | 26 % → 32 % | 11.6 px | 0.13 | 1.22 | 342 | quarters: 0.11 → 0.04 → 0.02 → 0.01

Numbers say: light vs heavy: width 6.9 → 20.4 px, dark 0.27 → 0.27; wet paint spreads well beyond the stroke.

## Dry Brush
Gouache · 24 px · 24.5 s

![Dry Brush](Dry-Brush.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 5 % → 1 % | 13.8 px | 0.65 | 0.11 | 168 |
| heavy line | 6 % → 0 % | 18.4 px | 0.65 | 0.02 | 92 |
| pressure swell | 5 % → 0 % | 18.1 px | 0.65 | 0.09 | 57 |
| fast wave | 6 % → 1 % | 6.9 px | 0.65 | 0.08 | 126 |
| slow wave | 7 % → 0 % | 7.8 px | 0.65 | 0.07 | 217 |
| spiral | 7 % → 1 % | 4.4 px | 0.65 | 0.08 | 260 |
| loop | 9 % → 0 % | 12.2 px | 0.65 | 0.05 | 169 |
| tilted | 4 % → 3 % | 10.3 px | 0.65 | 0.89 | 71 |
| over the wet one | 9 % → 1 % | 14.3 px | 0.65 | 0.12 | 81 |
| long, no reload | 6 % → 1 % | 2.7 px | 0.65 | 0.15 | 320 | quarters: 0.12 → 0.00 → 0.00 → 0.00

Numbers say: light vs heavy: width 13.8 → 18.4 px, dark 0.65 → 0.65.

## Wax Crayon
Wax · 8 px · 10.1 s

![Wax Crayon](Wax-Crayon.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 1 % → 1 % | 2.5 px | 0.71 | 1.00 | 80 |
| heavy line | 1 % → 1 % | 3.9 px | 0.69 | 1.00 | 16 |
| pressure swell | 1 % → 1 % | 3.3 px | 0.70 | 1.00 | 21 |
| fast wave | 3 % → 3 % | 3.5 px | 0.69 | 1.00 | 52 |
| slow wave | 3 % → 3 % | 3.4 px | 0.70 | 1.00 | 36 |
| spiral | 5 % → 5 % | 3.3 px | 0.70 | 1.00 | 107 |
| loop | 3 % → 3 % | 3.3 px | 0.70 | 1.00 | 35 |
| tilted | 2 % → 2 % | 5.6 px | 0.68 | 1.00 | 30 |
| over the wet one | 3 % → 3 % | 3.6 px | 0.68 | 1.00 | 24 |
| long, no reload | 7 % → 7 % | 3.3 px | 0.70 | 1.00 | 147 | quarters: 0.06 → 0.06 → 0.06 → 0.06

Numbers say: light vs heavy: width 2.5 → 3.9 px, dark 0.71 → 0.69; the long stroke does not run out of paint.

## Oil Pastel
Wax · 12 px · 10.6 s

![Oil Pastel](Oil-Pastel.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 1 % → 1 % | 4.0 px | 0.68 | 1.00 | 89 |
| heavy line | 2 % → 2 % | 6.5 px | 0.68 | 1.00 | 28 |
| pressure swell | 2 % → 2 % | 5.7 px | 0.69 | 1.00 | 19 |
| fast wave | 5 % → 5 % | 5.7 px | 0.68 | 1.00 | 68 |
| slow wave | 5 % → 5 % | 5.5 px | 0.68 | 1.00 | 64 |
| spiral | 8 % → 8 % | 5.5 px | 0.68 | 1.00 | 153 |
| loop | 4 % → 4 % | 5.6 px | 0.68 | 1.00 | 78 |
| tilted | 2 % → 2 % | 6.8 px | 0.68 | 1.00 | 50 |
| over the wet one | 5 % → 5 % | 5.8 px | 0.68 | 1.00 | 22 |
| long, no reload | 13 % → 13 % | 5.6 px | 0.68 | 1.00 | 200 | quarters: 0.10 → 0.09 → 0.10 → 0.10

Numbers say: light vs heavy: width 4.0 → 6.5 px, dark 0.68 → 0.68; the long stroke does not run out of paint.

## Charcoal
Charcoal · 5 px · 10.3 s

![Charcoal](Charcoal.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 1 % → 1 % | 2.0 px | 0.74 | 1.00 | 44 |
| heavy line | 1 % → 1 % | 3.0 px | 0.74 | 1.00 | 7 |
| pressure swell | 1 % → 1 % | 2.7 px | 0.74 | 1.00 | 16 |
| fast wave | 2 % → 2 % | 2.7 px | 0.73 | 1.00 | 27 |
| slow wave | 2 % → 2 % | 2.6 px | 0.74 | 1.00 | 35 |
| spiral | 4 % → 4 % | 2.5 px | 0.74 | 1.00 | 117 |
| loop | 2 % → 2 % | 2.6 px | 0.74 | 1.00 | 53 |
| tilted | 2 % → 2 % | 4.3 px | 0.72 | 1.00 | 17 |
| over the wet one | 2 % → 2 % | 2.4 px | 0.72 | 1.00 | 8 |
| long, no reload | 6 % → 6 % | 2.7 px | 0.73 | 1.00 | 114 | quarters: 0.05 → 0.05 → 0.05 → 0.05

Numbers say: light vs heavy: width 2.0 → 3.0 px, dark 0.74 → 0.74; the long stroke does not run out of paint.

## Impasto
Heavy acrylic · 22 px · 15.5 s

![Impasto](Impasto.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 8 % → 8 % | 24.1 px | 0.72 | 0.93 | 163 |
| heavy line | 10 % → 9 % | 28.8 px | 0.70 | 0.94 | 91 |
| pressure swell | 7 % → 7 % | 28.1 px | 0.72 | 0.94 | 56 |
| fast wave | 20 % → 13 % | 23.4 px | 0.71 | 0.64 | 161 |
| slow wave | 21 % → 14 % | 24.5 px | 0.71 | 0.66 | 262 |
| spiral | 30 % → 14 % | 19.9 px | 0.71 | 0.46 | 288 |
| loop | 18 % → 14 % | 23.9 px | 0.71 | 0.77 | 139 |
| tilted | 8 % → 8 % | 21.7 px | 0.70 | 1.00 | 48 |
| over the wet one | 17 % → 15 % | 25.4 px | 0.70 | 0.91 | 105 |
| long, no reload | 33 % → 14 % | 14.9 px | 0.71 | 0.42 | 482 | quarters: 0.38 → 0.21 → 0.10 → 0.03

Numbers say: light vs heavy: width 24.1 → 28.8 px, dark 0.72 → 0.70.

## Oil Round
Oil · 18 px · 18.3 s

![Oil Round](Oil-Round.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 2 % → 2 % | 7.2 px | 0.75 | 1.00 | 130 |
| heavy line | 7 % → 7 % | 19.3 px | 0.73 | 1.00 | 80 |
| pressure swell | 4 % → 4 % | 13.7 px | 0.72 | 1.00 | 37 |
| fast wave | 11 % → 11 % | 12.8 px | 0.65 | 1.00 | 180 |
| slow wave | 8 % → 8 % | 9.0 px | 0.57 | 1.00 | 154 |
| spiral | 10 % → 10 % | 6.6 px | 0.50 | 1.00 | 278 |
| loop | 6 % → 6 % | 7.2 px | 0.45 | 1.00 | 125 |
| tilted | 4 % → 4 % | 10.1 px | 0.52 | 1.00 | 77 |
| over the wet one | 6 % → 6 % | 7.6 px | 0.52 | 1.00 | 57 |
| long, no reload | 15 % → 15 % | 6.9 px | 0.42 | 1.00 | 366 | quarters: 0.09 → 0.08 → 0.07 → 0.06

Numbers say: light vs heavy: width 7.2 → 19.3 px, dark 0.75 → 0.73.

## Palette Knife
Oil · 20 px · 17.5 s

![Palette Knife](Palette-Knife.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 8 % → 8 % | 21.9 px | 0.67 | 1.00 | 127 |
| heavy line | 8 % → 8 % | 22.5 px | 0.74 | 1.00 | 26 |
| pressure swell | 6 % → 6 % | 22.3 px | 0.74 | 1.00 | 8 |
| fast wave | 16 % → 16 % | 18.9 px | 0.50 | 1.00 | 40 |
| slow wave | 17 % → 17 % | 19.9 px | 0.43 | 1.00 | 58 |
| spiral | 17 % → 17 % | 11.3 px | 0.46 | 1.00 | 82 |
| loop | 16 % → 16 % | 21.0 px | 0.59 | 1.00 | 28 |
| tilted | 5 % → 5 % | 15.0 px | 0.72 | 1.00 | 17 |
| over the wet one | 13 % → 13 % | 21.0 px | 0.72 | 1.00 | 12 |
| long, no reload | 16 % → 16 % | 7.2 px | 0.49 | 1.00 | 80 | quarters: 0.29 → 0.05 → 0.00 → 0.00

Numbers say: light vs heavy: width 21.9 → 22.5 px, dark 0.67 → 0.74; pressure barely changes the width.

## Water
Watercolor · 20 px · 36.1 s · over bands of wet oil paint and oil pastel in turn (it works on paint already there: look at what it does to the bands; covered counts the bands too)

![Water](Water.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 25 % → 27 % | 73.8 px | 0.80 | 1.06 | 24 |
| heavy line | 24 % → 25 % | 69.8 px | 0.81 | 1.04 | 59 |
| pressure swell | 24 % → 25 % | 89.6 px | 0.81 | 1.03 | 39 |
| fast wave | 24 % → 26 % | 27.7 px | 0.81 | 1.07 | 99 |
| slow wave | 24 % → 25 % | 27.8 px | 0.81 | 1.06 | 147 |
| spiral | 24 % → 26 % | 15.9 px | 0.81 | 1.07 | 204 |
| loop | 24 % → 25 % | 31.1 px | 0.81 | 1.03 | 99 |
| tilted | 24 % → 24 % | 67.0 px | 0.81 | 1.00 | 66 |
| over the wet one | 24 % → 25 % | 0.0 px | 0.81 | 1.06 | 36 |
| long, no reload | 24 % → 26 % | 10.7 px | 0.81 | 1.08 | 266 | quarters: 0.21 → 0.27 → 0.18 → 0.27

Numbers say: light vs heavy: width 73.8 → 69.8 px, dark 0.80 → 0.81; pressure barely changes the width; the long stroke does not run out of paint.

## Blender
Pastel · 16 px · 20.9 s · over bands of wet oil paint and oil pastel in turn (it works on paint already there: look at what it does to the bands; covered counts the bands too)

![Blender](Blender.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 24 % → 24 % | 70.7 px | 0.81 | 1.00 | 20 |
| heavy line | 25 % → 25 % | 72.1 px | 0.80 | 1.00 | 32 |
| pressure swell | 24 % → 24 % | 91.3 px | 0.81 | 1.00 | 24 |
| fast wave | 26 % → 26 % | 30.0 px | 0.79 | 1.00 | 87 |
| slow wave | 26 % → 26 % | 29.9 px | 0.80 | 1.00 | 78 |
| spiral | 28 % → 28 % | 18.7 px | 0.77 | 1.00 | 239 |
| loop | 25 % → 25 % | 33.0 px | 0.80 | 1.00 | 71 |
| tilted | 25 % → 25 % | 70.1 px | 0.79 | 1.00 | 48 |
| over the wet one | 26 % → 26 % | 1.8 px | 0.79 | 1.00 | 29 |
| long, no reload | 30 % → 30 % | 13.7 px | 0.76 | 1.00 | 170 | quarters: 0.20 → 0.28 → 0.23 → 0.30

Numbers say: light vs heavy: width 70.7 → 72.1 px, dark 0.81 → 0.80; pressure barely changes the width; the long stroke does not run out of paint.

## Eraser
Eraser · 16 px · 20.6 s · over bands of wet oil paint and oil pastel in turn (it works on paint already there: look at what it does to the bands; covered counts the bands too)

![Eraser](Eraser.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 24 % → 24 % | 69.6 px | 0.82 | 1.00 | 30 |
| heavy line | 23 % → 23 % | 67.9 px | 0.82 | 1.00 | 48 |
| pressure swell | 23 % → 23 % | 87.3 px | 0.82 | 1.00 | 19 |
| fast wave | 22 % → 22 % | 25.7 px | 0.82 | 1.00 | 71 |
| slow wave | 22 % → 22 % | 25.7 px | 0.82 | 1.00 | 87 |
| spiral | 22 % → 22 % | 14.4 px | 0.82 | 1.00 | 95 |
| loop | 22 % → 22 % | 28.6 px | 0.82 | 1.00 | 59 |
| tilted | 23 % → 23 % | 65.1 px | 0.82 | 1.00 | 36 |
| over the wet one | 23 % → 23 % | 0.0 px | 0.82 | 1.00 | 27 |
| long, no reload | 20 % → 20 % | 8.9 px | 0.82 | 1.00 | 177 | quarters: 0.15 → 0.20 → 0.15 → 0.20

Numbers say: light vs heavy: width 69.6 → 67.9 px, dark 0.82 → 0.82; pressure barely changes the width; the long stroke does not run out of paint.

## Fan
Gouache · 30 px · 29.0 s

![Fan](Fan.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 9 % → 3 % | 25.6 px | 0.63 | 0.37 | 30 |
| heavy line | 11 % → 4 % | 30.9 px | 0.63 | 0.39 | 174 |
| pressure swell | 8 % → 5 % | 31.7 px | 0.63 | 0.55 | 30 |
| fast wave | 17 % → 5 % | 20.2 px | 0.63 | 0.26 | 117 |
| slow wave | 18 % → 5 % | 21.0 px | 0.63 | 0.25 | 178 |
| spiral | 24 % → 5 % | 15.5 px | 0.63 | 0.19 | 146 |
| loop | 17 % → 5 % | 22.7 px | 0.63 | 0.28 | 85 |
| tilted | 5 % → 6 % | 15.0 px | 0.63 | 1.05 | 57 |
| over the wet one | 16 % → 8 % | 29.7 px | 0.63 | 0.49 | 40 |
| long, no reload | 22 % → 5 % | 9.9 px | 0.63 | 0.22 | 224 | quarters: 0.29 → 0.07 → 0.01 → 0.00

Numbers say: light vs heavy: width 25.6 → 30.9 px, dark 0.63 → 0.63.

## Sponge
Gouache · 30 px · 28.8 s

![Sponge](Sponge.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 4 % → 0 % | 11.3 px | 0.62 | 0.12 | 31 |
| heavy line | 12 % → 2 % | 35.4 px | 0.62 | 0.14 | 55 |
| pressure swell | 7 % → 2 % | 27.9 px | 0.62 | 0.28 | 66 |
| fast wave | 20 % → 4 % | 23.2 px | 0.62 | 0.19 | 118 |
| slow wave | 21 % → 4 % | 23.8 px | 0.62 | 0.18 | 248 |
| spiral | 28 % → 4 % | 18.3 px | 0.62 | 0.14 | 229 |
| loop | 18 % → 5 % | 23.0 px | 0.62 | 0.29 | 113 |
| tilted | 7 % → 7 % | 18.2 px | 0.62 | 1.04 | 95 |
| over the wet one | 16 % → 6 % | 27.8 px | 0.62 | 0.37 | 56 |
| long, no reload | 29 % → 5 % | 12.9 px | 0.62 | 0.17 | 280 | quarters: 0.29 → 0.13 → 0.07 → 0.04

Numbers say: light vs heavy: width 11.3 → 35.4 px, dark 0.62 → 0.62.

## Ink — sumi brush
Watercolour 1.00 · 22 px · 29.1 s

![Ink — sumi brush](Ink-sumi-brush.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 8 % → 9 % | 23.9 px | 0.87 | 1.13 | 75 |
| heavy line | 12 % → 13 % | 36.2 px | 0.86 | 1.01 | 75 |
| pressure swell | 10 % → 10 % | 36.1 px | 0.87 | 1.04 | 54 |
| fast wave | 27 % → 27 % | 31.0 px | 0.82 | 1.00 | 175 |
| slow wave | 27 % → 28 % | 31.2 px | 0.82 | 1.02 | 227 |
| spiral | 38 % → 36 % | 25.2 px | 0.75 | 0.95 | 304 |
| loop | 22 % → 23 % | 29.0 px | 0.84 | 1.01 | 151 |
| tilted | 9 % → 9 % | 25.7 px | 0.86 | 1.00 | 65 |
| over the wet one | 20 % → 20 % | 30.0 px | 0.86 | 1.02 | 76 |
| long, no reload | 46 % → 41 % | 20.7 px | 0.70 | 0.90 | 374 | quarters: 0.57 → 0.42 → 0.24 → 0.15

Numbers say: light vs heavy: width 23.9 → 36.2 px, dark 0.87 → 0.86.

## Ink — wash
Watercolour 1.00 · 40 px · 34.2 s

![Ink — wash](Ink-wash.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 13 % → 13 % | 37.3 px | 0.42 | 1.02 | 78 |
| heavy line | 19 % → 19 % | 55.2 px | 0.35 | 1.01 | 93 |
| pressure swell | 13 % → 13 % | 48.2 px | 0.41 | 1.02 | 66 |
| fast wave | 41 % → 42 % | 47.8 px | 0.32 | 1.02 | 231 |
| slow wave | 39 % → 40 % | 45.3 px | 0.42 | 1.02 | 329 |
| spiral | 60 % → 62 % | 39.7 px | 0.33 | 1.02 | 355 |
| loop | 34 % → 34 % | 43.8 px | 0.39 | 1.01 | 198 |
| tilted | 15 % → 15 % | 40.7 px | 0.43 | 1.01 | 110 |
| over the wet one | 30 % → 31 % | 43.4 px | 0.43 | 1.02 | 96 |
| long, no reload | 71 % → 75 % | 32.0 px | 0.31 | 1.05 | 513 | quarters: 0.40 → 0.29 → 0.19 → 0.12

Numbers say: light vs heavy: width 37.3 → 55.2 px, dark 0.42 → 0.35.

## Ink — dry brush
Ink 1.00 · 30 px · 24.3 s

![Ink — dry brush](Ink-dry-brush.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 5 % → 5 % | 14.9 px | 0.82 | 0.88 | 94 |
| heavy line | 7 % → 6 % | 19.4 px | 0.82 | 0.87 | 148 |
| pressure swell | 5 % → 5 % | 18.9 px | 0.81 | 0.96 | 79 |
| fast wave | 12 % → 7 % | 13.4 px | 0.80 | 0.65 | 203 |
| slow wave | 12 % → 8 % | 14.1 px | 0.81 | 0.62 | 419 |
| spiral | 16 % → 8 % | 10.8 px | 0.80 | 0.47 | 499 |
| loop | 11 % → 9 % | 14.5 px | 0.79 | 0.77 | 187 |
| tilted | 5 % → 6 % | 15.0 px | 0.81 | 1.08 | 134 |
| over the wet one | 12 % → 11 % | 18.4 px | 0.81 | 0.94 | 101 |
| long, no reload | 21 % → 10 % | 9.2 px | 0.77 | 0.47 | 595 | quarters: 0.28 → 0.10 → 0.03 → 0.01

Numbers say: light vs heavy: width 14.9 → 19.4 px, dark 0.82 → 0.82.

## Ink — nib
Watercolour 1.00 · 5 px · 24.0 s

![Ink — nib](Ink-nib.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 2 % → 5 % | 5.5 px | 0.89 | 2.46 | 39 |
| heavy line | 2 % → 5 % | 6.4 px | 0.89 | 2.34 | 31 |
| pressure swell | 2 % → 4 % | 6.2 px | 0.89 | 2.53 | 14 |
| fast wave | 5 % → 8 % | 5.9 px | 0.89 | 1.63 | 56 |
| slow wave | 5 % → 8 % | 5.7 px | 0.89 | 1.70 | 51 |
| spiral | 8 % → 11 % | 5.0 px | 0.87 | 1.41 | 101 |
| loop | 4 % → 8 % | 5.7 px | 0.89 | 1.74 | 89 |
| tilted | 4 % → 4 % | 10.3 px | 0.89 | 1.02 | 25 |
| over the wet one | 6 % → 9 % | 6.1 px | 0.89 | 1.61 | 23 |
| long, no reload | 9 % → 12 % | 4.2 px | 0.85 | 1.30 | 202 | quarters: 0.24 → 0.11 → 0.07 → 0.05

Numbers say: light vs heavy: width 5.5 → 6.4 px, dark 0.89 → 0.89; wet paint spreads well beyond the stroke.

## 0.45 · Dry brush
Gouache 0.91 · Ink 0.07 · 34 px · 31.6 s

![0.45 · Dry brush](0-45-Dry-brush.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 8 % → 2 % | 22.9 px | 0.68 | 0.26 | 119 |
| heavy line | 10 % → 5 % | 27.8 px | 0.68 | 0.52 | 122 |
| pressure swell | 7 % → 4 % | 26.5 px | 0.68 | 0.59 | 96 |
| fast wave | 19 % → 6 % | 21.4 px | 0.68 | 0.33 | 409 |
| slow wave | 20 % → 7 % | 23.0 px | 0.68 | 0.38 | 490 |
| spiral | 27 % → 8 % | 17.6 px | 0.68 | 0.29 | 550 |
| loop | 18 % → 9 % | 23.0 px | 0.68 | 0.51 | 259 |
| tilted | 8 % → 8 % | 21.8 px | 0.68 | 1.02 | 144 |
| over the wet one | 17 % → 12 % | 25.0 px | 0.68 | 0.73 | 181 |
| long, no reload | 34 % → 9 % | 15.3 px | 0.68 | 0.28 | 728 | quarters: 0.37 → 0.26 → 0.19 → 0.17

Numbers say: light vs heavy: width 22.9 → 27.8 px, dark 0.68 → 0.68.

## Dry pastel
Pastel 1.00 · 26 px · 11.2 s

![Dry pastel](Dry-pastel.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 3 % → 3 % | 8.2 px | 0.37 | 1.00 | 27 |
| heavy line | 5 % → 5 % | 13.1 px | 0.39 | 1.00 | 41 |
| pressure swell | 3 % → 3 % | 11.5 px | 0.39 | 1.00 | 29 |
| fast wave | 10 % → 10 % | 11.8 px | 0.39 | 1.00 | 85 |
| slow wave | 10 % → 10 % | 11.1 px | 0.39 | 1.00 | 174 |
| spiral | 14 % → 14 % | 9.1 px | 0.38 | 1.00 | 157 |
| loop | 7 % → 7 % | 9.5 px | 0.38 | 1.00 | 81 |
| tilted | 3 % → 3 % | 7.5 px | 0.39 | 1.00 | 36 |
| over the wet one | 6 % → 6 % | 10.6 px | 0.39 | 1.00 | 49 |
| long, no reload | 17 % → 17 % | 7.6 px | 0.38 | 1.00 | 240 | quarters: 0.08 → 0.07 → 0.07 → 0.07

Numbers say: light vs heavy: width 8.2 → 13.1 px, dark 0.37 → 0.39; the long stroke does not run out of paint.

## 0.45 · Charcoal
Charcoal 1.00 · 18 px · 10.3 s

![0.45 · Charcoal](0-45-Charcoal.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 2 % → 2 % | 5.4 px | 0.79 | 1.00 | 16 |
| heavy line | 3 % → 3 % | 8.0 px | 0.79 | 1.00 | 18 |
| pressure swell | 2 % → 2 % | 7.8 px | 0.80 | 1.00 | 18 |
| fast wave | 8 % → 8 % | 8.8 px | 0.80 | 1.00 | 48 |
| slow wave | 6 % → 6 % | 7.3 px | 0.80 | 1.00 | 71 |
| spiral | 10 % → 10 % | 6.7 px | 0.80 | 1.00 | 74 |
| loop | 6 % → 6 % | 8.2 px | 0.80 | 1.00 | 27 |
| tilted | 3 % → 3 % | 7.2 px | 0.79 | 1.00 | 25 |
| over the wet one | 5 % → 5 % | 7.4 px | 0.79 | 1.00 | 14 |
| long, no reload | 17 % → 17 % | 7.8 px | 0.80 | 1.00 | 137 | quarters: 0.15 → 0.16 → 0.16 → 0.16

Numbers say: light vs heavy: width 5.4 → 8.0 px, dark 0.79 → 0.79; the long stroke does not run out of paint.

## Watercolour — wash
Watercolour 1.00 · 50 px · 40.8 s

![Watercolour — wash](Watercolour-wash.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 16 % → 16 % | 45.5 px | 0.22 | 1.01 | 99 |
| heavy line | 22 % → 22 % | 64.9 px | 0.19 | 1.00 | 117 |
| pressure swell | 15 % → 15 % | 56.1 px | 0.22 | 1.01 | 97 |
| fast wave | 48 % → 49 % | 55.5 px | 0.19 | 1.01 | 290 |
| slow wave | 46 % → 46 % | 53.3 px | 0.24 | 1.00 | 548 |
| spiral | 66 % → 66 % | 43.7 px | 0.21 | 1.00 | 505 |
| loop | 40 % → 40 % | 51.4 px | 0.22 | 1.00 | 264 |
| tilted | 18 % → 18 % | 49.7 px | 0.23 | 1.00 | 167 |
| over the wet one | 36 % → 36 % | 49.6 px | 0.23 | 1.01 | 118 |
| long, no reload | 84 % → 84 % | 37.7 px | 0.20 | 1.00 | 680 | quarters: 0.24 → 0.20 → 0.16 → 0.12

Numbers say: light vs heavy: width 45.5 → 64.9 px, dark 0.22 → 0.19.

## Watercolour — wet-in-wet
Watercolour 1.00 · 44 px · 42.4 s

![Watercolour — wet-in-wet](Watercolour-wet-in-wet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 13 % → 21 % | 37.4 px | 0.32 | 1.63 | 79 |
| heavy line | 19 % → 22 % | 54.7 px | 0.34 | 1.17 | 105 |
| pressure swell | 12 % → 17 % | 45.7 px | 0.36 | 1.36 | 92 |
| fast wave | 42 % → 49 % | 48.5 px | 0.33 | 1.16 | 246 |
| slow wave | 40 % → 48 % | 45.7 px | 0.41 | 1.22 | 465 |
| spiral | 63 % → 69 % | 41.3 px | 0.37 | 1.11 | 451 |
| loop | 34 % → 41 % | 44.0 px | 0.37 | 1.21 | 238 |
| tilted | 16 % → 17 % | 44.6 px | 0.36 | 1.05 | 160 |
| over the wet one | 32 % → 40 % | 44.4 px | 0.36 | 1.26 | 126 |
| long, no reload | 79 % → 87 % | 35.3 px | 0.36 | 1.11 | 579 | quarters: 0.40 → 0.37 → 0.33 → 0.26

Numbers say: light vs heavy: width 37.4 → 54.7 px, dark 0.32 → 0.34; wet paint spreads well beyond the stroke.

## Watercolour — glaze
Watercolour 1.00 · 38 px · 37.8 s

![Watercolour — glaze](Watercolour-glaze.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 13 % → 13 % | 36.6 px | 0.07 | 1.02 | 75 |
| heavy line | 19 % → 19 % | 55.4 px | 0.07 | 1.00 | 102 |
| pressure swell | 13 % → 13 % | 47.0 px | 0.07 | 1.02 | 85 |
| fast wave | 39 % → 40 % | 45.6 px | 0.07 | 1.01 | 241 |
| slow wave | 37 % → 37 % | 42.8 px | 0.07 | 1.01 | 377 |
| spiral | 59 % → 60 % | 38.8 px | 0.06 | 1.01 | 338 |
| loop | 33 % → 33 % | 42.6 px | 0.07 | 1.00 | 254 |
| tilted | 14 % → 14 % | 40.1 px | 0.07 | 1.00 | 123 |
| over the wet one | 30 % → 30 % | 42.3 px | 0.07 | 1.01 | 74 |
| long, no reload | 69 % → 70 % | 30.9 px | 0.06 | 1.01 | 681 | quarters: 0.06 → 0.05 → 0.03 → 0.02

Numbers say: light vs heavy: width 36.6 → 55.4 px, dark 0.07 → 0.07.

## Watercolour — granulating
Watercolour 1.00 · 44 px · 39.0 s

![Watercolour — granulating](Watercolour-granulating.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 14 % → 14 % | 41.4 px | 0.35 | 1.01 | 94 |
| heavy line | 21 % → 21 % | 60.4 px | 0.31 | 1.00 | 86 |
| pressure swell | 14 % → 14 % | 52.2 px | 0.34 | 1.01 | 74 |
| fast wave | 45 % → 45 % | 51.7 px | 0.29 | 1.01 | 247 |
| slow wave | 42 % → 42 % | 48.2 px | 0.35 | 1.01 | 470 |
| spiral | 62 % → 63 % | 41.0 px | 0.30 | 1.01 | 383 |
| loop | 37 % → 37 % | 47.6 px | 0.33 | 1.00 | 234 |
| tilted | 16 % → 16 % | 45.5 px | 0.36 | 1.00 | 135 |
| over the wet one | 33 % → 33 % | 46.2 px | 0.36 | 1.01 | 96 |
| long, no reload | 75 % → 76 % | 33.6 px | 0.29 | 1.01 | 598 | quarters: 0.34 → 0.26 → 0.20 → 0.14

Numbers say: light vs heavy: width 41.4 → 60.4 px, dark 0.35 → 0.31.

## Watercolour — dry brush
Watercolour 1.00 · 36 px · 32.4 s

![Watercolour — dry brush](Watercolour-dry-brush.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 10 % → 9 % | 27.8 px | 0.17 | 0.99 | 94 |
| heavy line | 14 % → 12 % | 39.3 px | 0.16 | 0.92 | 149 |
| pressure swell | 11 % → 10 % | 39.6 px | 0.16 | 0.95 | 77 |
| fast wave | 27 % → 20 % | 31.3 px | 0.13 | 0.74 | 296 |
| slow wave | 25 % → 17 % | 28.9 px | 0.14 | 0.70 | 552 |
| spiral | 34 % → 19 % | 22.6 px | 0.13 | 0.56 | 440 |
| loop | 21 % → 18 % | 27.7 px | 0.14 | 0.85 | 226 |
| tilted | 10 % → 10 % | 28.5 px | 0.16 | 1.01 | 137 |
| over the wet one | 21 % → 20 % | 31.0 px | 0.16 | 0.95 | 114 |
| long, no reload | 35 % → 19 % | 15.9 px | 0.14 | 0.54 | 594 | quarters: 0.09 → 0.03 → 0.01 → 0.00

Numbers say: light vs heavy: width 27.8 → 39.3 px, dark 0.17 → 0.16.

## Gouache
Gouache 1.00 · 30 px · 35.4 s

![Gouache](Gouache.png)

A light paint: laid on a grey sheet (on white it cannot be seen); **dark** = how far it is from the grey either way.

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 8 % → 5 % | 23.3 px | 0.29 | 0.61 | 91 |
| heavy line | 12 % → 5 % | 35.6 px | 0.28 | 0.41 | 106 |
| pressure swell | 10 % → 5 % | 36.2 px | 0.28 | 0.49 | 85 |
| fast wave | 22 % → 6 % | 25.0 px | 0.28 | 0.27 | 332 |
| slow wave | 22 % → 7 % | 25.9 px | 0.28 | 0.30 | 369 |
| spiral | 28 % → 7 % | 18.5 px | 0.28 | 0.23 | 371 |
| loop | 18 % → 7 % | 23.7 px | 0.28 | 0.37 | 203 |
| tilted | 9 % → 9 % | 24.0 px | 0.28 | 1.01 | 100 |
| over the wet one | 19 % → 12 % | 28.7 px | 0.28 | 0.62 | 123 |
| long, no reload | 27 % → 8 % | 12.2 px | 0.28 | 0.31 | 630 | quarters: 0.01 → 0.02 → 0.02 → 0.02

Numbers say: light vs heavy: width 23.3 → 35.6 px, dark 0.29 → 0.28; the long stroke does not run out of paint.

## Oil — alla prima
Oil 0.89 · Oil glaze 0.11 · 30 px · 18.0 s

![Oil — alla prima](Oil-alla-prima.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 9 % → 9 % | 27.5 px | 0.49 | 1.00 | 93 |
| heavy line | 10 % → 10 % | 28.7 px | 0.50 | 1.00 | 126 |
| pressure swell | 7 % → 7 % | 27.5 px | 0.50 | 1.00 | 75 |
| fast wave | 22 % → 22 % | 25.5 px | 0.50 | 1.00 | 267 |
| slow wave | 25 % → 25 % | 29.0 px | 0.50 | 1.00 | 502 |
| spiral | 37 % → 37 % | 24.5 px | 0.49 | 1.00 | 510 |
| loop | 21 % → 21 % | 27.5 px | 0.50 | 1.00 | 233 |
| tilted | 10 % → 10 % | 26.8 px | 0.50 | 1.00 | 132 |
| over the wet one | 19 % → 19 % | 27.7 px | 0.50 | 1.00 | 96 |
| long, no reload | 46 % → 46 % | 20.5 px | 0.47 | 1.00 | 569 | quarters: 0.31 → 0.25 → 0.22 → 0.18

Numbers say: light vs heavy: width 27.5 → 28.7 px, dark 0.49 → 0.50; pressure barely changes the width.

## Oil — impasto
Oil heavy 1.00 · 34 px · 20.2 s

![Oil — impasto](Oil-impasto.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 8 % → 8 % | 24.0 px | 0.22 | 1.00 | 116 |
| heavy line | 12 % → 12 % | 35.3 px | 0.22 | 1.00 | 201 |
| pressure swell | 9 % → 9 % | 33.1 px | 0.23 | 1.00 | 94 |
| fast wave | 29 % → 29 % | 33.7 px | 0.22 | 1.00 | 336 |
| slow wave | 30 % → 30 % | 34.6 px | 0.22 | 1.00 | 490 |
| spiral | 47 % → 47 % | 31.3 px | 0.21 | 1.00 | 577 |
| loop | 25 % → 25 % | 32.5 px | 0.22 | 1.00 | 259 |
| tilted | 11 % → 11 % | 31.8 px | 0.24 | 1.00 | 145 |
| over the wet one | 21 % → 21 % | 26.8 px | 0.24 | 1.00 | 110 |
| long, no reload | 54 % → 54 % | 24.4 px | 0.20 | 1.00 | 819 | quarters: 0.16 → 0.14 → 0.11 → 0.09

Numbers say: light vs heavy: width 24.0 → 35.3 px, dark 0.22 → 0.22.

## Oil — glaze
Oil glaze 1.00 · 40 px · 21.4 s

![Oil — glaze](Oil-glaze.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 9 % → 9 % | 27.0 px | 0.50 | 1.00 | 112 |
| heavy line | 13 % → 13 % | 38.3 px | 0.49 | 1.00 | 129 |
| pressure swell | 10 % → 10 % | 36.6 px | 0.50 | 1.00 | 95 |
| fast wave | 29 % → 29 % | 33.5 px | 0.49 | 1.00 | 418 |
| slow wave | 30 % → 30 % | 34.6 px | 0.50 | 1.00 | 1073 |
| spiral | 46 % → 46 % | 30.1 px | 0.49 | 1.00 | 810 |
| loop | 24 % → 24 % | 31.4 px | 0.50 | 1.00 | 283 |
| tilted | 11 % → 11 % | 30.4 px | 0.50 | 1.00 | 215 |
| over the wet one | 23 % → 23 % | 32.5 px | 0.50 | 1.00 | 236 |
| long, no reload | 52 % → 52 % | 23.5 px | 0.49 | 1.00 | 1863 | quarters: 0.34 → 0.30 → 0.27 → 0.22

Numbers say: light vs heavy: width 27.0 → 38.3 px, dark 0.50 → 0.49.

## Oil — scumble
Oil 1.00 · 36 px · 20.2 s

![Oil — scumble](Oil-scumble.png)

A light paint: laid on a grey sheet (on white it cannot be seen); **dark** = how far it is from the grey either way.

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 5 % → 5 % | 13.1 px | 0.08 | 1.00 | 120 |
| heavy line | 6 % → 6 % | 17.3 px | 0.26 | 1.00 | 225 |
| pressure swell | 7 % → 7 % | 26.1 px | 0.19 | 1.00 | 140 |
| fast wave | 18 % → 18 % | 21.3 px | 0.18 | 1.00 | 782 |
| slow wave | 23 % → 23 % | 26.7 px | 0.17 | 1.00 | 901 |
| spiral | 30 % → 30 % | 20.0 px | 0.15 | 1.00 | 722 |
| loop | 18 % → 18 % | 23.0 px | 0.16 | 1.00 | 449 |
| tilted | 10 % → 10 % | 26.6 px | 0.22 | 1.00 | 263 |
| over the wet one | 16 % → 16 % | 18.6 px | 0.22 | 1.00 | 441 |
| long, no reload | 32 % → 32 % | 14.6 px | 0.13 | 1.00 | 1384 | quarters: 0.01 → 0.00 → 0.00 → 0.00

Numbers say: light vs heavy: width 13.1 → 17.3 px, dark 0.08 → 0.26.

## Acrylic — heavy body
Impasto 0.98 · 30 px · 16.9 s

![Acrylic — heavy body](Acrylic-heavy-body.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 9 % → 7 % | 25.4 px | 0.52 | 0.83 | 154 |
| heavy line | 8 % → 7 % | 24.6 px | 0.52 | 0.88 | 141 |
| pressure swell | 8 % → 7 % | 28.6 px | 0.53 | 0.89 | 172 |
| fast wave | 17 % → 13 % | 19.4 px | 0.52 | 0.78 | 301 |
| slow wave | 19 % → 15 % | 21.6 px | 0.52 | 0.79 | 491 |
| spiral | 24 % → 15 % | 15.8 px | 0.52 | 0.61 | 555 |
| loop | 17 % → 13 % | 22.2 px | 0.52 | 0.78 | 281 |
| tilted | 8 % → 8 % | 23.3 px | 0.53 | 0.99 | 132 |
| over the wet one | 18 % → 15 % | 25.6 px | 0.53 | 0.85 | 118 |
| long, no reload | 31 % → 18 % | 14.0 px | 0.52 | 0.58 | 709 | quarters: 0.26 → 0.16 → 0.11 → 0.09

Numbers say: light vs heavy: width 25.4 → 24.6 px, dark 0.52 → 0.52; pressure barely changes the width.

## Acrylic — fluid
Watercolour 1.00 · 36 px · 35.1 s

![Acrylic — fluid](Acrylic-fluid.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 12 % → 12 % | 33.6 px | 0.24 | 1.01 | 108 |
| heavy line | 18 % → 17 % | 50.9 px | 0.21 | 0.99 | 176 |
| pressure swell | 12 % → 12 % | 45.5 px | 0.23 | 1.01 | 105 |
| fast wave | 39 % → 39 % | 45.1 px | 0.19 | 0.99 | 252 |
| slow wave | 35 % → 35 % | 40.9 px | 0.22 | 1.00 | 544 |
| spiral | 55 % → 54 % | 36.4 px | 0.19 | 0.98 | 393 |
| loop | 31 % → 31 % | 40.0 px | 0.21 | 1.00 | 181 |
| tilted | 13 % → 13 % | 36.0 px | 0.24 | 1.00 | 121 |
| over the wet one | 28 % → 28 % | 42.4 px | 0.24 | 1.01 | 75 |
| long, no reload | 61 % → 58 % | 27.4 px | 0.19 | 0.95 | 485 | quarters: 0.20 → 0.14 → 0.09 → 0.06

Numbers say: light vs heavy: width 33.6 → 50.9 px, dark 0.24 → 0.21.

## Acrylic — palette knife
Impasto 1.00 · 42 px · 20.8 s

![Acrylic — palette knife](Acrylic-palette-knife.png)

A light paint: laid on a grey sheet (on white it cannot be seen); **dark** = how far it is from the grey either way.

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 15 % → 15 % | 44.0 px | 0.39 | 0.98 | 37 |
| heavy line | 15 % → 15 % | 44.3 px | 0.40 | 0.98 | 38 |
| pressure swell | 12 % → 12 % | 43.6 px | 0.42 | 0.99 | 9 |
| fast wave | 36 % → 20 % | 42.0 px | 0.37 | 0.55 | 85 |
| slow wave | 37 % → 21 % | 42.7 px | 0.37 | 0.57 | 196 |
| spiral | 47 % → 18 % | 30.7 px | 0.37 | 0.39 | 126 |
| loop | 32 % → 24 % | 41.3 px | 0.36 | 0.77 | 110 |
| tilted | 12 % → 12 % | 33.7 px | 0.39 | 1.00 | 43 |
| over the wet one | 26 % → 25 % | 39.8 px | 0.39 | 0.97 | 44 |
| long, no reload | 53 % → 20 % | 23.7 px | 0.35 | 0.39 | 214 | quarters: 0.00 → 0.00 → 0.00 → 0.01

Numbers say: light vs heavy: width 44.0 → 44.3 px, dark 0.39 → 0.40; pressure barely changes the width; the long stroke does not run out of paint.

## Finger on oil
Oil 1.00 · 30 px · 13.8 s

![Finger on oil](Finger-on-oil.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 6 % → 6 % | 16.8 px | 0.23 | 1.00 | 51 |
| heavy line | 9 % → 9 % | 27.6 px | 0.28 | 1.00 | 64 |
| pressure swell | 7 % → 7 % | 25.3 px | 0.35 | 1.00 | 44 |
| fast wave | 15 % → 15 % | 17.0 px | 0.12 | 1.00 | 130 |
| slow wave | 16 % → 16 % | 18.6 px | 0.24 | 1.00 | 321 |
| spiral | 28 % → 28 % | 18.2 px | 0.24 | 1.00 | 225 |
| loop | 19 % → 19 % | 24.9 px | 0.28 | 1.00 | 130 |
| tilted | 9 % → 9 % | 26.4 px | 0.28 | 1.00 | 104 |
| over the wet one | 16 % → 16 % | 19.6 px | 0.28 | 1.00 | 54 |
| long, no reload | 36 % → 36 % | 15.9 px | 0.22 | 1.00 | 442 | quarters: 0.12 → 0.11 → 0.07 → 0.04

Numbers say: light vs heavy: width 16.8 → 27.6 px, dark 0.23 → 0.28.

## Palette knife — oil
Oil heavy 0.93 · Impasto 0.07 · 44 px · 20.6 s

![Palette knife — oil](Palette-knife-oil.png)

A light paint: laid on a grey sheet (on white it cannot be seen); **dark** = how far it is from the grey either way.

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 16 % → 14 % | 45.7 px | 0.37 | 0.91 | 30 |
| heavy line | 16 % → 16 % | 46.3 px | 0.38 | 0.98 | 46 |
| pressure swell | 12 % → 12 % | 45.2 px | 0.38 | 0.99 | 16 |
| fast wave | 39 % → 35 % | 44.9 px | 0.35 | 0.89 | 67 |
| slow wave | 39 % → 36 % | 45.4 px | 0.35 | 0.92 | 171 |
| spiral | 62 % → 37 % | 40.7 px | 0.35 | 0.60 | 199 |
| loop | 34 % → 31 % | 43.8 px | 0.36 | 0.92 | 108 |
| tilted | 13 % → 13 % | 36.6 px | 0.37 | 1.00 | 35 |
| over the wet one | 28 % → 27 % | 40.8 px | 0.37 | 0.97 | 37 |
| long, no reload | 74 % → 40 % | 33.0 px | 0.34 | 0.54 | 184 | quarters: 0.00 → 0.00 → 0.01 → 0.01

Numbers say: light vs heavy: width 45.7 → 46.3 px, dark 0.37 → 0.38; pressure barely changes the width; the long stroke does not run out of paint.

## 0.45 · Sponge
Watercolour 0.93 · Ink 0.07 · 46 px · 41.1 s

![0.45 · Sponge](0-45-Sponge.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 27 % → 24 % | 77.5 px | 0.13 | 0.91 | 79 |
| heavy line | 32 % → 28 % | 92.0 px | 0.13 | 0.89 | 130 |
| pressure swell | 24 % → 22 % | 90.9 px | 0.13 | 0.91 | 121 |
| fast wave | 60 % → 54 % | 69.8 px | 0.12 | 0.90 | 193 |
| slow wave | 63 % → 59 % | 72.4 px | 0.17 | 0.94 | 360 |
| spiral | 77 % → 74 % | 51.0 px | 0.16 | 0.96 | 395 |
| loop | 54 % → 51 % | 70.4 px | 0.15 | 0.94 | 174 |
| tilted | 17 % → 17 % | 47.9 px | 0.17 | 1.01 | 138 |
| over the wet one | 45 % → 42 % | 76.8 px | 0.17 | 0.93 | 82 |
| long, no reload | 94 % → 90 % | 42.3 px | 0.17 | 0.96 | 732 | quarters: 0.18 → 0.18 → 0.17 → 0.14

Numbers say: light vs heavy: width 77.5 → 92.0 px, dark 0.13 → 0.13.

## 0.45 · Eraser
Watercolour 1.00 · 30 px · 23.2 s · over bands of wet oil paint and oil pastel in turn (it works on paint already there: look at what it does to the bands; covered counts the bands too)

![0.45 · Eraser](0-45-Eraser.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 24 % → 24 % | 69.2 px | 0.82 | 1.00 | 29 |
| heavy line | 23 % → 23 % | 67.4 px | 0.82 | 1.00 | 54 |
| pressure swell | 23 % → 23 % | 86.8 px | 0.82 | 1.00 | 31 |
| fast wave | 21 % → 21 % | 24.7 px | 0.81 | 1.00 | 127 |
| slow wave | 20 % → 20 % | 23.5 px | 0.82 | 1.00 | 235 |
| spiral | 20 % → 20 % | 13.5 px | 0.79 | 1.00 | 216 |
| loop | 21 % → 21 % | 27.8 px | 0.80 | 1.00 | 112 |
| tilted | 23 % → 23 % | 64.8 px | 0.81 | 1.00 | 65 |
| over the wet one | 22 % → 22 % | 0.0 px | 0.81 | 1.00 | 62 |
| long, no reload | 17 % → 17 % | 7.5 px | 0.79 | 1.00 | 268 | quarters: 0.13 → 0.16 → 0.13 → 0.17

Numbers say: light vs heavy: width 69.2 → 67.4 px, dark 0.82 → 0.82; pressure barely changes the width; the long stroke does not run out of paint.

## Lift wet paint
Watercolour 1.00 · 30 px · 22.8 s · over bands of wet oil paint and oil pastel in turn (it works on paint already there: look at what it does to the bands; covered counts the bands too)

![Lift wet paint](Lift-wet-paint.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 24 % → 24 % | 70.1 px | 0.82 | 1.00 | 37 |
| heavy line | 24 % → 24 % | 69.8 px | 0.82 | 1.00 | 41 |
| pressure swell | 24 % → 24 % | 89.6 px | 0.82 | 1.00 | 35 |
| fast wave | 24 % → 24 % | 27.7 px | 0.82 | 1.00 | 110 |
| slow wave | 24 % → 24 % | 27.7 px | 0.82 | 1.00 | 161 |
| spiral | 24 % → 24 % | 15.9 px | 0.82 | 1.00 | 152 |
| loop | 24 % → 24 % | 31.1 px | 0.82 | 1.00 | 102 |
| tilted | 24 % → 24 % | 66.8 px | 0.82 | 1.00 | 38 |
| over the wet one | 24 % → 24 % | 0.0 px | 0.82 | 1.00 | 42 |
| long, no reload | 24 % → 24 % | 10.7 px | 0.82 | 1.00 | 252 | quarters: 0.18 → 0.24 → 0.17 → 0.24

Numbers say: light vs heavy: width 70.1 → 69.8 px, dark 0.82 → 0.82; pressure barely changes the width; the long stroke does not run out of paint.

## Sgraffito
Watercolour 1.00 · 10 px · 23.2 s · over bands of wet oil paint and oil pastel in turn (it works on paint already there: look at what it does to the bands; covered counts the bands too)

![Sgraffito](Sgraffito.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 24 % → 24 % | 69.9 px | 0.81 | 1.00 | 13 |
| heavy line | 24 % → 24 % | 69.8 px | 0.82 | 1.00 | 11 |
| pressure swell | 24 % → 24 % | 89.6 px | 0.82 | 1.00 | 9 |
| fast wave | 24 % → 24 % | 27.7 px | 0.82 | 1.00 | 21 |
| slow wave | 24 % → 24 % | 27.7 px | 0.82 | 1.00 | 31 |
| spiral | 24 % → 24 % | 15.9 px | 0.82 | 1.00 | 42 |
| loop | 24 % → 24 % | 31.1 px | 0.82 | 1.00 | 22 |
| tilted | 24 % → 24 % | 66.9 px | 0.82 | 1.00 | 13 |
| over the wet one | 24 % → 24 % | 0.0 px | 0.82 | 1.00 | 33 |
| long, no reload | 24 % → 24 % | 10.6 px | 0.82 | 1.00 | 75 | quarters: 0.17 → 0.24 → 0.17 → 0.24

Numbers say: light vs heavy: width 69.9 → 69.8 px, dark 0.81 → 0.82; pressure barely changes the width; the long stroke does not run out of paint.

## Brush Artist · Refs · #01 Henry Ward peach cloud
Gouache 1.00 · 44 px · 32.8 s

![Brush Artist · Refs · #01 Henry Ward peach cloud](Brush-Artist-Refs-01-Henry-Ward-peach-cloud.png)

A light paint: laid on a grey sheet (on white it cannot be seen); **dark** = how far it is from the grey either way.

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 5 % → 0 % | 13.4 px | 0.00 | 0.00 | 120 |
| heavy line | 8 % → 0 % | 22.4 px | 0.32 | 0.01 | 120 |
| pressure swell | 7 % → 3 % | 24.8 px | 0.33 | 0.40 | 87 |
| fast wave | 31 % → 3 % | 36.2 px | 0.27 | 0.09 | 412 |
| slow wave | 20 % → 2 % | 23.3 px | 0.32 | 0.10 | 611 |
| spiral | 33 % → 2 % | 21.6 px | 0.35 | 0.07 | 651 |
| loop | 17 % → 0 % | 22.4 px | 0.32 | 0.01 | 409 |
| tilted | 12 % → 11 % | 32.7 px | 0.25 | 0.97 | 259 |
| over the wet one | 16 % → 2 % | 12.9 px | 0.25 | 0.10 | 131 |
| long, no reload | 30 % → 2 % | 13.6 px | 0.32 | 0.08 | 967 | quarters: 0.03 → 0.03 → 0.03 → 0.03

Numbers say: light vs heavy: width 13.4 → 22.4 px, dark 0.00 → 0.32; the long stroke does not run out of paint.

## Brush Artist · Refs · #02 Henry Ward cream strokes
Gouache 1.00 · 46 px · 37.7 s

![Brush Artist · Refs · #02 Henry Ward cream strokes](Brush-Artist-Refs-02-Henry-Ward-cream-strokes.png)

A light paint: laid on a grey sheet (on white it cannot be seen); **dark** = how far it is from the grey either way.

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 5 % → 0 % | 14.3 px | 0.00 | 0.00 | 98 |
| heavy line | 8 % → 2 % | 24.6 px | 0.41 | 0.22 | 144 |
| pressure swell | 7 % → 3 % | 27.7 px | 0.41 | 0.38 | 125 |
| fast wave | 30 % → 4 % | 34.5 px | 0.36 | 0.15 | 431 |
| slow wave | 21 % → 5 % | 24.3 px | 0.39 | 0.21 | 688 |
| spiral | 43 % → 4 % | 28.4 px | 0.40 | 0.10 | 882 |
| loop | 19 % → 1 % | 24.8 px | 0.39 | 0.04 | 305 |
| tilted | 12 % → 12 % | 33.1 px | 0.34 | 0.98 | 265 |
| over the wet one | 17 % → 1 % | 13.0 px | 0.34 | 0.05 | 144 |
| long, no reload | 25 % → 4 % | 11.1 px | 0.41 | 0.17 | 919 | quarters: 0.03 → 0.04 → 0.03 → 0.04

Numbers say: light vs heavy: width 14.3 → 24.6 px, dark 0.00 → 0.41; the long stroke does not run out of paint.

## Brush Artist · Refs · #03 Henry Ward navy contours
Impasto 1.00 · 22 px · 17.2 s

![Brush Artist · Refs · #03 Henry Ward navy contours](Brush-Artist-Refs-03-Henry-Ward-navy-contours.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 7 % → 6 % | 19.4 px | 0.72 | 0.90 | 86 |
| heavy line | 6 % → 6 % | 18.3 px | 0.71 | 0.92 | 80 |
| pressure swell | 5 % → 5 % | 20.1 px | 0.75 | 0.89 | 57 |
| fast wave | 16 % → 11 % | 18.3 px | 0.76 | 0.71 | 224 |
| slow wave | 18 % → 14 % | 20.5 px | 0.72 | 0.78 | 334 |
| spiral | 28 % → 13 % | 18.3 px | 0.68 | 0.47 | 413 |
| loop | 13 % → 11 % | 17.0 px | 0.71 | 0.83 | 214 |
| tilted | 7 % → 7 % | 20.7 px | 0.73 | 0.99 | 101 |
| over the wet one | 15 % → 13 % | 20.4 px | 0.73 | 0.88 | 95 |
| long, no reload | 32 % → 13 % | 14.4 px | 0.71 | 0.41 | 567 | quarters: 0.33 → 0.27 → 0.19 → 0.08

Numbers say: light vs heavy: width 19.4 → 18.3 px, dark 0.72 → 0.71; pressure barely changes the width.

## Brush Artist · Refs · #04 Henry Ward grey cloud
Gouache 1.00 · 50 px · 39.6 s

![Brush Artist · Refs · #04 Henry Ward grey cloud](Brush-Artist-Refs-04-Henry-Ward-grey-cloud.png)

A light paint: laid on a grey sheet (on white it cannot be seen); **dark** = how far it is from the grey either way.

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 5 % → 0 % | 14.6 px | 0.00 | 0.00 | 142 |
| heavy line | 10 % → 2 % | 28.3 px | 0.31 | 0.25 | 218 |
| pressure swell | 7 % → 2 % | 24.5 px | 0.31 | 0.36 | 305 |
| fast wave | 32 % → 4 % | 37.5 px | 0.24 | 0.14 | 738 |
| slow wave | 23 % → 2 % | 26.3 px | 0.33 | 0.10 | 987 |
| spiral | 47 % → 3 % | 30.8 px | 0.37 | 0.06 | 871 |
| loop | 19 % → 0 % | 25.2 px | 0.00 | 0.00 | 340 |
| tilted | 12 % → 12 % | 33.3 px | 0.24 | 0.98 | 338 |
| over the wet one | 17 % → 3 % | 14.1 px | 0.24 | 0.17 | 189 |
| long, no reload | 22 % → 4 % | 9.9 px | 0.34 | 0.17 | 1509 | quarters: 0.03 → 0.04 → 0.04 → 0.04

Numbers say: light vs heavy: width 14.6 → 28.3 px, dark 0.00 → 0.31; the long stroke does not run out of paint.

## Brush Artist · Refs · #05 Henry Ward green in rust loops
Impasto 1.00 · 20 px · 20.4 s

![Brush Artist · Refs · #05 Henry Ward green in rust loops](Brush-Artist-Refs-05-Henry-Ward-green-in-rust-loops.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 6 % → 6 % | 18.5 px | 0.56 | 0.88 | 84 |
| heavy line | 8 % → 7 % | 22.1 px | 0.56 | 0.87 | 94 |
| pressure swell | 4 % → 4 % | 16.1 px | 0.58 | 0.93 | 183 |
| fast wave | 16 % → 10 % | 17.9 px | 0.56 | 0.67 | 310 |
| slow wave | 16 % → 12 % | 19.1 px | 0.56 | 0.74 | 470 |
| spiral | 24 % → 11 % | 16.1 px | 0.53 | 0.46 | 592 |
| loop | 15 % → 12 % | 19.7 px | 0.56 | 0.79 | 287 |
| tilted | 7 % → 7 % | 19.8 px | 0.58 | 0.99 | 149 |
| over the wet one | 14 % → 12 % | 18.1 px | 0.58 | 0.85 | 94 |
| long, no reload | 28 % → 12 % | 12.6 px | 0.55 | 0.41 | 841 | quarters: 0.23 → 0.17 → 0.11 → 0.04

Numbers say: light vs heavy: width 18.5 → 22.1 px, dark 0.56 → 0.56.

## Brush Artist · Refs · #06 Henry Ward scrubbed grey
Gouache 1.00 · 50 px · 40.0 s

![Brush Artist · Refs · #06 Henry Ward scrubbed grey](Brush-Artist-Refs-06-Henry-Ward-scrubbed-grey.png)

A light paint: laid on a grey sheet (on white it cannot be seen); **dark** = how far it is from the grey either way.

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 5 % → 0 % | 14.6 px | 0.00 | 0.00 | 202 |
| heavy line | 10 % → 2 % | 28.3 px | 0.33 | 0.25 | 194 |
| pressure swell | 7 % → 2 % | 24.5 px | 0.33 | 0.36 | 168 |
| fast wave | 32 % → 4 % | 37.5 px | 0.25 | 0.14 | 467 |
| slow wave | 23 % → 2 % | 26.3 px | 0.34 | 0.10 | 897 |
| spiral | 47 % → 3 % | 30.8 px | 0.38 | 0.06 | 1016 |
| loop | 19 % → 0 % | 25.2 px | 0.00 | 0.00 | 576 |
| tilted | 12 % → 12 % | 33.3 px | 0.25 | 0.98 | 460 |
| over the wet one | 17 % → 3 % | 14.1 px | 0.25 | 0.17 | 282 |
| long, no reload | 22 % → 4 % | 9.9 px | 0.36 | 0.17 | 1334 | quarters: 0.03 → 0.04 → 0.04 → 0.04

Numbers say: light vs heavy: width 14.6 → 28.3 px, dark 0.00 → 0.33; the long stroke does not run out of paint.

## Brush Artist · Refs · #07 Henry Ward blue L + black zigzag
Impasto 1.00 · 34 px · 22.4 s

![Brush Artist · Refs · #07 Henry Ward blue L + black zigzag](Brush-Artist-Refs-07-Henry-Ward-blue-L-black-zigzag.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 10 % → 9 % | 30.2 px | 0.59 | 0.86 | 125 |
| heavy line | 11 % → 10 % | 30.8 px | 0.59 | 0.93 | 220 |
| pressure swell | 8 % → 8 % | 31.6 px | 0.59 | 0.92 | 165 |
| fast wave | 25 % → 19 % | 28.8 px | 0.60 | 0.77 | 329 |
| slow wave | 26 % → 20 % | 29.7 px | 0.57 | 0.76 | 456 |
| spiral | 44 % → 23 % | 29.1 px | 0.54 | 0.52 | 461 |
| loop | 24 % → 19 % | 30.4 px | 0.57 | 0.80 | 424 |
| tilted | 11 % → 11 % | 29.8 px | 0.61 | 1.00 | 214 |
| over the wet one | 22 % → 20 % | 32.0 px | 0.61 | 0.90 | 162 |
| long, no reload | 50 % → 23 % | 22.5 px | 0.57 | 0.46 | 1184 | quarters: 0.36 → 0.31 → 0.21 → 0.10

Numbers say: light vs heavy: width 30.2 → 30.8 px, dark 0.59 → 0.59; pressure barely changes the width.

## Brush Artist · Refs · #08 Henry Ward olive bands
Gouache 1.00 · 34 px · 30.5 s

![Brush Artist · Refs · #08 Henry Ward olive bands](Brush-Artist-Refs-08-Henry-Ward-olive-bands.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 2 % → 0 % | 5.8 px | 0.00 | 0.00 | 64 |
| heavy line | 7 % → 1 % | 19.2 px | 0.61 | 0.15 | 274 |
| pressure swell | 5 % → 1 % | 19.1 px | 0.61 | 0.20 | 88 |
| fast wave | 18 % → 1 % | 21.1 px | 0.59 | 0.04 | 259 |
| slow wave | 16 % → 0 % | 18.3 px | 0.63 | 0.02 | 889 |
| spiral | 27 % → 0 % | 17.5 px | 0.52 | 0.01 | 832 |
| loop | 10 % → 1 % | 13.5 px | 0.61 | 0.12 | 362 |
| tilted | 7 % → 7 % | 20.5 px | 0.65 | 0.92 | 273 |
| over the wet one | 11 % → 1 % | 9.8 px | 0.65 | 0.12 | 229 |
| long, no reload | 23 % → 2 % | 10.4 px | 0.53 | 0.10 | 1245 | quarters: 0.21 → 0.11 → 0.12 → 0.08

Numbers say: light vs heavy: width 5.8 → 19.2 px, dark 0.00 → 0.61.

## Brush Artist · Refs · #09 Henry Ward white loops
Gouache 1.00 · 46 px · 42.4 s

![Brush Artist · Refs · #09 Henry Ward white loops](Brush-Artist-Refs-09-Henry-Ward-white-loops.png)

A light paint: laid on a grey sheet (on white it cannot be seen); **dark** = how far it is from the grey either way.

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 5 % → 0 % | 14.3 px | 0.00 | 0.00 | 132 |
| heavy line | 8 % → 2 % | 24.6 px | 0.43 | 0.22 | 149 |
| pressure swell | 7 % → 3 % | 27.7 px | 0.43 | 0.38 | 103 |
| fast wave | 30 % → 4 % | 34.5 px | 0.38 | 0.15 | 776 |
| slow wave | 21 % → 5 % | 24.3 px | 0.40 | 0.21 | 1058 |
| spiral | 43 % → 4 % | 28.4 px | 0.41 | 0.10 | 1450 |
| loop | 19 % → 1 % | 24.8 px | 0.41 | 0.04 | 617 |
| tilted | 12 % → 12 % | 33.1 px | 0.37 | 0.98 | 188 |
| over the wet one | 17 % → 1 % | 13.0 px | 0.37 | 0.05 | 184 |
| long, no reload | 25 % → 4 % | 11.1 px | 0.41 | 0.17 | 1459 | quarters: 0.03 → 0.04 → 0.04 → 0.04

Numbers say: light vs heavy: width 14.3 → 24.6 px, dark 0.00 → 0.43; the long stroke does not run out of paint.

## Brush Artist · Refs · #10 Henry Ward maroon loops
Impasto 1.00 · 30 px · 21.2 s

![Brush Artist · Refs · #10 Henry Ward maroon loops](Brush-Artist-Refs-10-Henry-Ward-maroon-loops.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 10 % → 8 % | 27.9 px | 0.73 | 0.88 | 143 |
| heavy line | 11 % → 10 % | 32.1 px | 0.73 | 0.90 | 225 |
| pressure swell | 8 % → 7 % | 29.7 px | 0.74 | 0.91 | 184 |
| fast wave | 23 % → 17 % | 26.5 px | 0.76 | 0.76 | 390 |
| slow wave | 22 % → 19 % | 25.9 px | 0.72 | 0.85 | 794 |
| spiral | 37 % → 18 % | 24.2 px | 0.72 | 0.50 | 845 |
| loop | 17 % → 15 % | 22.1 px | 0.73 | 0.86 | 417 |
| tilted | 10 % → 10 % | 27.6 px | 0.73 | 1.00 | 236 |
| over the wet one | 19 % → 17 % | 26.8 px | 0.73 | 0.86 | 192 |
| long, no reload | 40 % → 17 % | 18.0 px | 0.71 | 0.43 | 892 | quarters: 0.38 → 0.33 → 0.27 → 0.18

Numbers say: light vs heavy: width 27.9 → 32.1 px, dark 0.73 → 0.73.

## Brush Artist · Refs · #11 Henry Ward purple spun balls
Impasto 1.00 · 36 px · 21.6 s

![Brush Artist · Refs · #11 Henry Ward purple spun balls](Brush-Artist-Refs-11-Henry-Ward-purple-spun-balls.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 11 % → 10 % | 31.5 px | 0.74 | 0.93 | 208 |
| heavy line | 11 % → 10 % | 30.5 px | 0.74 | 0.95 | 170 |
| pressure swell | 10 % → 9 % | 36.4 px | 0.75 | 0.92 | 145 |
| fast wave | 27 % → 21 % | 31.1 px | 0.74 | 0.78 | 423 |
| slow wave | 30 % → 24 % | 34.6 px | 0.73 | 0.82 | 694 |
| spiral | 40 % → 24 % | 26.5 px | 0.70 | 0.59 | 732 |
| loop | 24 % → 21 % | 30.7 px | 0.75 | 0.90 | 588 |
| tilted | 10 % → 10 % | 28.5 px | 0.73 | 1.00 | 168 |
| over the wet one | 22 % → 20 % | 33.9 px | 0.73 | 0.91 | 140 |
| long, no reload | 53 % → 25 % | 23.9 px | 0.74 | 0.46 | 882 | quarters: 0.50 → 0.45 → 0.38 → 0.27

Numbers say: light vs heavy: width 31.5 → 30.5 px, dark 0.74 → 0.74; pressure barely changes the width.

## Brush Artist · Refs · #12 Henry Ward black-olive cage
Gouache 1.00 · 28 px · 29.1 s

![Brush Artist · Refs · #12 Henry Ward black-olive cage](Brush-Artist-Refs-12-Henry-Ward-black-olive-cage.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 2 % → 0 % | 6.3 px | 0.00 | 0.00 | 61 |
| heavy line | 6 % → 1 % | 16.9 px | 0.64 | 0.21 | 143 |
| pressure swell | 5 % → 1 % | 17.2 px | 0.64 | 0.22 | 107 |
| fast wave | 14 % → 0 % | 16.6 px | 0.00 | 0.00 | 516 |
| slow wave | 14 % → 1 % | 15.6 px | 0.64 | 0.07 | 395 |
| spiral | 18 % → 0 % | 11.7 px | 0.63 | 0.02 | 429 |
| loop | 11 % → 1 % | 14.3 px | 0.63 | 0.10 | 240 |
| tilted | 6 % → 6 % | 17.8 px | 0.68 | 0.92 | 143 |
| over the wet one | 10 % → 0 % | 9.7 px | 0.68 | 0.04 | 88 |
| long, no reload | 18 % → 2 % | 8.0 px | 0.59 | 0.12 | 642 | quarters: 0.15 → 0.12 → 0.06 → 0.02

Numbers say: light vs heavy: width 6.3 → 16.9 px, dark 0.00 → 0.64.

## Brush Artist · Refs · #13 Henry Ward blue streaky form
Gouache 1.00 · 50 px · 36.4 s

![Brush Artist · Refs · #13 Henry Ward blue streaky form](Brush-Artist-Refs-13-Henry-Ward-blue-streaky-form.png)

A light paint: laid on a grey sheet (on white it cannot be seen); **dark** = how far it is from the grey either way.

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 5 % → 0 % | 14.6 px | 0.00 | 0.00 | 369 |
| heavy line | 10 % → 2 % | 28.3 px | 0.33 | 0.25 | 154 |
| pressure swell | 7 % → 2 % | 24.5 px | 0.33 | 0.36 | 113 |
| fast wave | 32 % → 4 % | 37.5 px | 0.25 | 0.14 | 455 |
| slow wave | 23 % → 2 % | 26.3 px | 0.34 | 0.10 | 801 |
| spiral | 47 % → 3 % | 30.8 px | 0.38 | 0.06 | 957 |
| loop | 19 % → 0 % | 25.2 px | 0.00 | 0.00 | 469 |
| tilted | 12 % → 12 % | 33.3 px | 0.25 | 0.98 | 368 |
| over the wet one | 17 % → 3 % | 14.1 px | 0.25 | 0.17 | 243 |
| long, no reload | 22 % → 4 % | 9.9 px | 0.35 | 0.17 | 1377 | quarters: 0.03 → 0.04 → 0.04 → 0.04

Numbers say: light vs heavy: width 14.6 → 28.3 px, dark 0.00 → 0.33; the long stroke does not run out of paint.

## Brush Artist · Refs · #14 Henry Ward olive totem
Impasto 1.00 · 48 px · 25.4 s

![Brush Artist · Refs · #14 Henry Ward olive totem](Brush-Artist-Refs-14-Henry-Ward-olive-totem.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 15 % → 14 % | 44.4 px | 0.31 | 0.91 | 180 |
| heavy line | 16 % → 15 % | 46.3 px | 0.31 | 0.95 | 198 |
| pressure swell | 12 % → 11 % | 44.0 px | 0.31 | 0.93 | 154 |
| fast wave | 36 % → 28 % | 41.7 px | 0.36 | 0.78 | 466 |
| slow wave | 37 % → 32 % | 42.3 px | 0.30 | 0.87 | 657 |
| spiral | 59 % → 35 % | 38.7 px | 0.28 | 0.59 | 936 |
| loop | 30 % → 27 % | 39.1 px | 0.29 | 0.89 | 573 |
| tilted | 13 % → 13 % | 36.4 px | 0.33 | 1.00 | 220 |
| over the wet one | 28 % → 25 % | 40.5 px | 0.33 | 0.92 | 171 |
| long, no reload | 61 % → 31 % | 27.3 px | 0.27 | 0.52 | 1281 | quarters: 0.20 → 0.15 → 0.09 → 0.04

Numbers say: light vs heavy: width 44.4 → 46.3 px, dark 0.31 → 0.31; pressure barely changes the width.

## Brush Artist · Refs · #15 Ultramarine brush script
Ink 1.00 · 4 px · 28.5 s

![Brush Artist · Refs · #15 Ultramarine brush script](Brush-Artist-Refs-15-Ultramarine-brush-script.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 1 % → 3 % | 2.1 px | 0.55 | 3.99 | 32 |
| heavy line | 5 % → 5 % | 15.6 px | 0.62 | 1.00 | 47 |
| pressure swell | 3 % → 4 % | 11.0 px | 0.62 | 1.21 | 47 |
| fast wave | 9 % → 7 % | 10.2 px | 0.54 | 0.81 | 112 |
| slow wave | 8 % → 7 % | 8.8 px | 0.53 | 0.89 | 127 |
| spiral | 11 % → 8 % | 7.3 px | 0.53 | 0.68 | 195 |
| loop | 7 % → 7 % | 9.4 px | 0.54 | 0.96 | 102 |
| tilted | 3 % → 3 % | 7.4 px | 0.64 | 1.04 | 48 |
| over the wet one | 7 % → 7 % | 10.7 px | 0.64 | 1.08 | 43 |
| long, no reload | 16 % → 7 % | 7.1 px | 0.51 | 0.47 | 285 | quarters: 0.14 → 0.04 → 0.01 → 0.00

Numbers say: light vs heavy: width 2.1 → 15.6 px, dark 0.55 → 0.62; wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #18 Blue oil-stick scribbles
Pastel 1.00 · 10 px · 14.4 s

![Brush Artist · Refs · #18 Blue oil-stick scribbles](Brush-Artist-Refs-18-Blue-oil-stick-scribbles.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 1 % → 1 % | 2.9 px | 0.53 | 1.00 | 38 |
| heavy line | 2 % → 2 % | 6.0 px | 0.53 | 1.00 | 24 |
| pressure swell | 1 % → 1 % | 5.5 px | 0.52 | 1.00 | 20 |
| fast wave | 5 % → 5 % | 5.3 px | 0.53 | 1.00 | 132 |
| slow wave | 4 % → 4 % | 5.2 px | 0.53 | 1.00 | 99 |
| spiral | 7 % → 7 % | 4.4 px | 0.52 | 1.00 | 142 |
| loop | 4 % → 4 % | 4.6 px | 0.52 | 1.00 | 66 |
| tilted | 2 % → 2 % | 4.4 px | 0.53 | 1.00 | 34 |
| over the wet one | 3 % → 3 % | 4.8 px | 0.53 | 1.00 | 17 |
| long, no reload | 9 % → 9 % | 4.2 px | 0.52 | 1.00 | 285 | quarters: 0.05 → 0.05 → 0.06 → 0.06

Numbers say: light vs heavy: width 2.9 → 6.0 px, dark 0.53 → 0.53; the long stroke does not run out of paint.

## Brush Artist · Refs · #20 Orange-red crayon scribble
Pastel 1.00 · 14 px · 14.4 s

![Brush Artist · Refs · #20 Orange-red crayon scribble](Brush-Artist-Refs-20-Orange-red-crayon-scribble.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 1 % → 1 % | 3.8 px | 0.53 | 1.00 | 25 |
| heavy line | 3 % → 3 % | 8.0 px | 0.53 | 1.00 | 27 |
| pressure swell | 2 % → 2 % | 7.6 px | 0.55 | 1.00 | 19 |
| fast wave | 6 % → 6 % | 7.3 px | 0.56 | 1.00 | 89 |
| slow wave | 6 % → 6 % | 6.9 px | 0.53 | 1.00 | 104 |
| spiral | 9 % → 9 % | 6.0 px | 0.54 | 1.00 | 171 |
| loop | 5 % → 5 % | 6.1 px | 0.54 | 1.00 | 110 |
| tilted | 2 % → 2 % | 5.6 px | 0.55 | 1.00 | 57 |
| over the wet one | 4 % → 4 % | 6.2 px | 0.55 | 1.00 | 48 |
| long, no reload | 12 % → 12 % | 5.4 px | 0.53 | 1.00 | 215 | quarters: 0.07 → 0.07 → 0.07 → 0.07

Numbers say: light vs heavy: width 3.8 → 8.0 px, dark 0.53 → 0.53; the long stroke does not run out of paint.

## Brush Artist · Refs · #21 Gritty black contours
Gouache 1.00 · 12 px · 24.9 s

![Brush Artist · Refs · #21 Gritty black contours](Brush-Artist-Refs-21-Gritty-black-contours.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 1 % → 0 % | 3.2 px | 0.00 | 0.00 | 91 |
| heavy line | 2 % → 0 % | 6.0 px | 0.00 | 0.00 | 156 |
| pressure swell | 1 % → 0 % | 5.6 px | 0.00 | 0.00 | 90 |
| fast wave | 4 % → 0 % | 4.9 px | 0.00 | 0.00 | 519 |
| slow wave | 4 % → 0 % | 5.1 px | 0.81 | 0.01 | 324 |
| spiral | 7 % → 0 % | 4.6 px | 0.75 | 0.03 | 586 |
| loop | 4 % → 0 % | 5.5 px | 0.80 | 0.09 | 279 |
| tilted | 3 % → 2 % | 7.7 px | 0.66 | 0.84 | 121 |
| over the wet one | 3 % → 0 % | 2.1 px | 0.66 | 0.01 | 112 |
| long, no reload | 5 % → 0 % | 2.2 px | 0.76 | 0.00 | 608 | quarters: 0.07 → 0.03 → 0.03 → 0.02

Numbers say: light vs heavy: width 3.2 → 6.0 px, dark 0.00 → 0.00.

## Brush Artist · Refs · #22 Bold black brush poster
Ink 1.00 · 20 px · 54.5 s

![Brush Artist · Refs · #22 Bold black brush poster](Brush-Artist-Refs-22-Bold-black-brush-poster.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 4 % → 5 % | 10.3 px | 0.79 | 1.52 | 56 |
| heavy line | 15 % → 14 % | 42.6 px | 0.88 | 0.99 | 133 |
| pressure swell | 9 % → 9 % | 33.6 px | 0.87 | 1.03 | 81 |
| fast wave | 28 % → 27 % | 32.3 px | 0.88 | 0.98 | 306 |
| slow wave | 23 % → 23 % | 27.0 px | 0.87 | 0.98 | 445 |
| spiral | 35 % → 32 % | 23.0 px | 0.87 | 0.92 | 421 |
| loop | 22 % → 22 % | 28.2 px | 0.88 | 1.00 | 320 |
| tilted | 9 % → 9 % | 24.2 px | 0.88 | 1.00 | 112 |
| over the wet one | 20 % → 20 % | 30.8 px | 0.88 | 1.00 | 69 |
| long, no reload | 48 % → 38 % | 21.3 px | 0.85 | 0.79 | 408 | quarters: 0.56 → 0.45 → 0.35 → 0.26

Numbers say: light vs heavy: width 10.3 → 42.6 px, dark 0.79 → 0.88; wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #23 Dry white on orange + black line
Gouache 1.00 · 50 px · 47.6 s

![Brush Artist · Refs · #23 Dry white on orange + black line](Brush-Artist-Refs-23-Dry-white-on-orange-black-line.png)

A light paint: laid on a grey sheet (on white it cannot be seen); **dark** = how far it is from the grey either way.

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 3 % → 0 % | 9.9 px | 0.00 | 0.00 | 116 |
| heavy line | 9 % → 2 % | 26.8 px | 0.42 | 0.20 | 356 |
| pressure swell | 7 % → 0 % | 24.9 px | 0.41 | 0.03 | 289 |
| fast wave | 25 % → 0 % | 28.6 px | 0.00 | 0.00 | 473 |
| slow wave | 24 % → 1 % | 27.6 px | 0.40 | 0.02 | 709 |
| spiral | 33 % → 1 % | 21.5 px | 0.40 | 0.02 | 705 |
| loop | 20 % → 0 % | 26.0 px | 0.39 | 0.00 | 350 |
| tilted | 10 % → 9 % | 28.2 px | 0.38 | 0.93 | 291 |
| over the wet one | 15 % → 1 % | 13.1 px | 0.38 | 0.05 | 165 |
| long, no reload | 30 % → 4 % | 13.5 px | 0.40 | 0.12 | 1010 | quarters: 0.02 → 0.03 → 0.03 → 0.03

Numbers say: light vs heavy: width 9.9 → 26.8 px, dark 0.00 → 0.42; the long stroke does not run out of paint.

## Brush Artist · Refs · #24 Picasso flat oil
Oil 0.89 · Oil glaze 0.11 · 34 px · 20.6 s

![Brush Artist · Refs · #24 Picasso flat oil](Brush-Artist-Refs-24-Picasso-flat-oil.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 10 % → 10 % | 28.8 px | 0.39 | 1.00 | 355 |
| heavy line | 11 % → 11 % | 32.5 px | 0.39 | 1.00 | 201 |
| pressure swell | 8 % → 8 % | 31.7 px | 0.38 | 1.00 | 228 |
| fast wave | 30 % → 30 % | 35.2 px | 0.39 | 1.00 | 476 |
| slow wave | 28 % → 28 % | 32.8 px | 0.38 | 1.00 | 641 |
| spiral | 42 % → 42 % | 27.8 px | 0.38 | 1.00 | 629 |
| loop | 22 % → 22 % | 28.8 px | 0.40 | 1.00 | 343 |
| tilted | 11 % → 11 % | 31.3 px | 0.41 | 1.00 | 185 |
| over the wet one | 20 % → 20 % | 25.3 px | 0.41 | 1.00 | 157 |
| long, no reload | 58 % → 58 % | 26.0 px | 0.32 | 1.00 | 1159 | quarters: 0.23 → 0.22 → 0.19 → 0.17

Numbers say: light vs heavy: width 28.8 → 32.5 px, dark 0.39 → 0.39.

## Brush Artist · Refs · #25 Yellow heavy flat stroke
Impasto 1.00 · 110 px · 75.5 s

![Brush Artist · Refs · #25 Yellow heavy flat stroke](Brush-Artist-Refs-25-Yellow-heavy-flat-stroke.png)

A light paint: laid on a grey sheet (on white it cannot be seen); **dark** = how far it is from the grey either way.

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 35 % → 35 % | 101.0 px | 0.31 | 1.00 | 492 |
| heavy line | 36 % → 35 % | 104.1 px | 0.31 | 0.97 | 495 |
| pressure swell | 28 % → 29 % | 104.0 px | 0.28 | 1.05 | 344 |
| fast wave | 72 % → 75 % | 82.8 px | 0.25 | 1.04 | 1432 |
| slow wave | 72 % → 71 % | 83.7 px | 0.30 | 0.98 | 2684 |
| spiral | 86 % → 81 % | 56.5 px | 0.30 | 0.94 | 2501 |
| loop | 64 % → 63 % | 82.7 px | 0.31 | 0.99 | 1428 |
| tilted | 25 % → 25 % | 70.3 px | 0.28 | 1.00 | 2574 |
| over the wet one | 55 % → 53 % | 83.3 px | 0.28 | 0.97 | 1579 |
| long, no reload | 98 % → 96 % | 43.9 px | 0.31 | 0.98 | 15428 | quarters: 0.00 → 0.00 → 0.00 → 0.00

Numbers say: light vs heavy: width 101.0 → 104.1 px, dark 0.31 → 0.31; pressure barely changes the width; the long stroke does not run out of paint.

## Brush Artist · Refs · #27 Orange impasto swatch
Impasto 1.00 · 60 px · 47.7 s

![Brush Artist · Refs · #27 Orange impasto swatch](Brush-Artist-Refs-27-Orange-impasto-swatch.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 18 % → 18 % | 52.9 px | 0.34 | 0.97 | 219 |
| heavy line | 21 % → 20 % | 60.0 px | 0.34 | 0.95 | 212 |
| pressure swell | 15 % → 15 % | 57.8 px | 0.36 | 0.97 | 161 |
| fast wave | 48 % → 46 % | 55.2 px | 0.37 | 0.97 | 672 |
| slow wave | 46 % → 45 % | 53.6 px | 0.33 | 0.97 | 989 |
| spiral | 68 % → 61 % | 45.1 px | 0.34 | 0.89 | 1207 |
| loop | 40 % → 39 % | 51.8 px | 0.33 | 0.97 | 539 |
| tilted | 16 % → 16 % | 43.7 px | 0.35 | 1.00 | 357 |
| over the wet one | 34 % → 32 % | 50.0 px | 0.35 | 0.97 | 259 |
| long, no reload | 84 % → 76 % | 37.8 px | 0.32 | 0.90 | 1621 | quarters: 0.30 → 0.29 → 0.28 → 0.25

Numbers say: light vs heavy: width 52.9 → 60.0 px, dark 0.34 → 0.34.

## Brush Artist · Refs · #28 Miles Davis black lines
Ink 1.00 · 22 px · 57.7 s

![Brush Artist · Refs · #28 Miles Davis black lines](Brush-Artist-Refs-28-Miles-Davis-black-lines.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 4 % → 6 % | 12.3 px | 0.80 | 1.40 | 46 |
| heavy line | 16 % → 16 % | 45.9 px | 0.88 | 0.99 | 95 |
| pressure swell | 10 % → 10 % | 36.7 px | 0.87 | 1.03 | 50 |
| fast wave | 29 % → 29 % | 33.8 px | 0.88 | 0.99 | 156 |
| slow wave | 27 % → 26 % | 30.7 px | 0.88 | 0.99 | 279 |
| spiral | 39 % → 36 % | 25.4 px | 0.87 | 0.93 | 365 |
| loop | 24 % → 24 % | 31.0 px | 0.88 | 1.00 | 159 |
| tilted | 9 % → 9 % | 26.0 px | 0.88 | 1.01 | 99 |
| over the wet one | 21 % → 21 % | 32.9 px | 0.88 | 1.00 | 66 |
| long, no reload | 53 % → 45 % | 23.9 px | 0.85 | 0.83 | 427 | quarters: 0.61 → 0.53 → 0.41 → 0.31

Numbers say: light vs heavy: width 12.3 → 45.9 px, dark 0.80 → 0.88.

## Brush Artist · Refs · #29 Shrigley magenta asterisk
Watercolour 1.00 · 70 px · 68.9 s

![Brush Artist · Refs · #29 Shrigley magenta asterisk](Brush-Artist-Refs-29-Shrigley-magenta-asterisk.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 10 % → 13 % | 28.0 px | 0.61 | 1.39 | 66 |
| heavy line | 17 % → 18 % | 50.3 px | 0.61 | 1.04 | 151 |
| pressure swell | 11 % → 13 % | 41.1 px | 0.62 | 1.14 | 96 |
| fast wave | 38 % → 38 % | 43.8 px | 0.60 | 1.01 | 354 |
| slow wave | 35 % → 39 % | 41.0 px | 0.62 | 1.11 | 563 |
| spiral | 61 % → 61 % | 40.0 px | 0.60 | 1.01 | 540 |
| loop | 31 % → 32 % | 40.2 px | 0.61 | 1.03 | 246 |
| tilted | 18 % → 18 % | 49.0 px | 0.61 | 1.00 | 269 |
| over the wet one | 31 % → 34 % | 38.5 px | 0.61 | 1.08 | 112 |
| long, no reload | 75 % → 76 % | 33.6 px | 0.60 | 1.01 | 845 | quarters: 0.53 → 0.50 → 0.48 → 0.45

Numbers say: light vs heavy: width 28.0 → 50.3 px, dark 0.61 → 0.61; the long stroke does not run out of paint.

## Brush Artist · Refs · #30 Red gouache face patch
Gouache 1.00 · 60 px · 78.6 s

![Brush Artist · Refs · #30 Red gouache face patch](Brush-Artist-Refs-30-Red-gouache-face-patch.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 16 % → 14 % | 45.5 px | 0.49 | 0.87 | 207 |
| heavy line | 25 % → 19 % | 71.4 px | 0.49 | 0.78 | 278 |
| pressure swell | 20 % → 17 % | 74.8 px | 0.50 | 0.84 | 157 |
| fast wave | 48 % → 28 % | 55.1 px | 0.51 | 0.58 | 605 |
| slow wave | 50 % → 31 % | 57.3 px | 0.48 | 0.62 | 2417 |
| spiral | 59 % → 30 % | 39.0 px | 0.48 | 0.50 | 4725 |
| loop | 40 % → 28 % | 51.4 px | 0.48 | 0.71 | 5582 |
| tilted | 17 % → 17 % | 46.7 px | 0.50 | 1.00 | 422 |
| over the wet one | 37 % → 32 % | 55.9 px | 0.50 | 0.87 | 726 |
| long, no reload | 66 % → 28 % | 29.6 px | 0.46 | 0.42 | 2614 | quarters: 0.40 → 0.36 → 0.31 → 0.26

Numbers say: light vs heavy: width 45.5 → 71.4 px, dark 0.49 → 0.49.

## Brush Artist · Refs · #31 Warhol blotted line
Ink 1.00 · 6 px · 57.0 s

![Brush Artist · Refs · #31 Warhol blotted line](Brush-Artist-Refs-31-Warhol-blotted-line.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 1 % → 4 % | 3.0 px | 0.72 | 3.49 | 28 |
| heavy line | 7 % → 7 % | 19.5 px | 0.84 | 0.98 | 67 |
| pressure swell | 4 % → 4 % | 14.2 px | 0.82 | 1.18 | 51 |
| fast wave | 12 % → 9 % | 13.6 px | 0.81 | 0.73 | 237 |
| slow wave | 11 % → 9 % | 12.3 px | 0.80 | 0.80 | 529 |
| spiral | 15 % → 9 % | 10.0 px | 0.79 | 0.58 | 622 |
| loop | 10 % → 9 % | 12.6 px | 0.80 | 0.94 | 565 |
| tilted | 4 % → 4 % | 11.0 px | 0.83 | 1.03 | 634 |
| over the wet one | 9 % → 9 % | 14.0 px | 0.83 | 1.05 | 120 |
| long, no reload | 21 % → 10 % | 9.5 px | 0.78 | 0.45 | 4776 | quarters: 0.25 → 0.13 → 0.05 → 0.01

Numbers say: light vs heavy: width 3.0 → 19.5 px, dark 0.72 → 0.84; wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #32 Thick orange swipes
Impasto 1.00 · 90 px · 67.7 s

![Brush Artist · Refs · #32 Thick orange swipes](Brush-Artist-Refs-32-Thick-orange-swipes.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 29 % → 28 % | 83.5 px | 0.37 | 0.99 | 1035 |
| heavy line | 30 % → 29 % | 86.8 px | 0.37 | 0.97 | 917 |
| pressure swell | 23 % → 23 % | 84.8 px | 0.38 | 1.01 | 1514 |
| fast wave | 64 % → 65 % | 74.2 px | 0.39 | 1.02 | 5162 |
| slow wave | 64 % → 62 % | 73.9 px | 0.37 | 0.97 | 4479 |
| spiral | 80 % → 75 % | 52.6 px | 0.35 | 0.94 | 3766 |
| loop | 56 % → 55 % | 73.0 px | 0.36 | 0.97 | 1801 |
| tilted | 21 % → 21 % | 58.8 px | 0.38 | 1.00 | 997 |
| over the wet one | 46 % → 45 % | 70.6 px | 0.38 | 0.96 | 739 |
| long, no reload | 95 % → 92 % | 42.8 px | 0.36 | 0.97 | 4363 | quarters: 0.35 → 0.35 → 0.35 → 0.34

Numbers say: light vs heavy: width 83.5 → 86.8 px, dark 0.37 → 0.37; pressure barely changes the width; the long stroke does not run out of paint.

## Brush Artist · Refs · #33 Red wet-in-wet band
Watercolour 1.00 · 80 px · 82.5 s

![Brush Artist · Refs · #33 Red wet-in-wet band](Brush-Artist-Refs-33-Red-wet-in-wet-band.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 24 % → 42 % | 69.3 px | 0.54 | 1.75 | 441 |
| heavy line | 33 % → 48 % | 96.9 px | 0.55 | 1.45 | 1537 |
| pressure swell | 19 % → 30 % | 72.1 px | 0.57 | 1.56 | 1034 |
| fast wave | 65 % → 79 % | 75.5 px | 0.60 | 1.21 | 4574 |
| slow wave | 61 % → 78 % | 70.5 px | 0.63 | 1.28 | 1968 |
| spiral | 77 % → 89 % | 50.8 px | 0.64 | 1.15 | 1707 |
| loop | 54 % → 67 % | 70.5 px | 0.62 | 1.23 | 656 |
| tilted | 28 % → 30 % | 78.0 px | 0.58 | 1.09 | 753 |
| over the wet one | 55 % → 79 % | 76.7 px | 0.58 | 1.43 | 502 |
| long, no reload | 96 % → 99 % | 42.9 px | 0.66 | 1.04 | 1776 | quarters: 0.68 → 0.68 → 0.68 → 0.64

Numbers say: light vs heavy: width 69.3 → 96.9 px, dark 0.54 → 0.55; the long stroke does not run out of paint; wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #34 Magenta oil patches
Oil 0.89 · Oil glaze 0.11 · 60 px · 33.8 s

![Brush Artist · Refs · #34 Magenta oil patches](Brush-Artist-Refs-34-Magenta-oil-patches.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 18 % → 18 % | 51.4 px | 0.61 | 1.00 | 443 |
| heavy line | 19 % → 19 % | 55.1 px | 0.61 | 1.00 | 486 |
| pressure swell | 15 % → 15 % | 54.6 px | 0.61 | 1.01 | 266 |
| fast wave | 44 % → 45 % | 51.1 px | 0.61 | 1.02 | 1186 |
| slow wave | 45 % → 45 % | 52.4 px | 0.61 | 1.00 | 3125 |
| spiral | 68 % → 68 % | 44.9 px | 0.58 | 1.00 | 2229 |
| loop | 42 % → 42 % | 54.2 px | 0.61 | 1.00 | 846 |
| tilted | 17 % → 17 % | 46.3 px | 0.61 | 1.00 | 514 |
| over the wet one | 34 % → 34 % | 48.4 px | 0.61 | 1.00 | 364 |
| long, no reload | 83 % → 83 % | 37.1 px | 0.59 | 1.00 | 3349 | quarters: 0.54 → 0.54 → 0.53 → 0.47

Numbers say: light vs heavy: width 51.4 → 55.1 px, dark 0.61 → 0.61; pressure barely changes the width; the long stroke does not run out of paint.

## Brush Artist · Refs · #35 Red band with runs
Watercolour 1.00 · 70 px · 64.1 s

![Brush Artist · Refs · #35 Red band with runs](Brush-Artist-Refs-35-Red-band-with-runs.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 40 % → 45 % | 115.3 px | 0.42 | 1.14 | 272 |
| heavy line | 45 % → 50 % | 132.0 px | 0.42 | 1.09 | 377 |
| pressure swell | 20 % → 28 % | 76.7 px | 0.48 | 1.37 | 294 |
| fast wave | 66 % → 76 % | 76.8 px | 0.49 | 1.14 | 1739 |
| slow wave | 65 % → 76 % | 75.6 px | 0.52 | 1.16 | 1467 |
| spiral | 86 % → 94 % | 56.9 px | 0.53 | 1.09 | 1195 |
| loop | 79 % → 88 % | 102.7 px | 0.49 | 1.11 | 896 |
| tilted | 50 % → 51 % | 139.1 px | 0.47 | 1.02 | 890 |
| over the wet one | 78 % → 84 % | 77.5 px | 0.47 | 1.09 | 407 |
| long, no reload | 96 % → 100 % | 43.2 px | 0.58 | 1.04 | 1129 | quarters: 0.59 → 0.60 → 0.59 → 0.56

Numbers say: light vs heavy: width 115.3 → 132.0 px, dark 0.42 → 0.42; the long stroke does not run out of paint.

## Brush Artist · Refs · #36 Magenta letters flat brush
Gouache 1.00 · 36 px · 47.3 s

![Brush Artist · Refs · #36 Magenta letters flat brush](Brush-Artist-Refs-36-Magenta-letters-flat-brush.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 10 % → 10 % | 29.6 px | 0.45 | 0.94 | 208 |
| heavy line | 16 % → 13 % | 47.5 px | 0.45 | 0.78 | 451 |
| pressure swell | 13 % → 11 % | 48.4 px | 0.47 | 0.85 | 185 |
| fast wave | 34 % → 16 % | 39.3 px | 0.47 | 0.48 | 431 |
| slow wave | 35 % → 20 % | 40.5 px | 0.45 | 0.57 | 718 |
| spiral | 46 % → 19 % | 30.6 px | 0.44 | 0.41 | 1169 |
| loop | 27 % → 18 % | 35.0 px | 0.45 | 0.67 | 593 |
| tilted | 12 % → 12 % | 32.8 px | 0.47 | 1.00 | 541 |
| over the wet one | 26 % → 22 % | 38.5 px | 0.47 | 0.88 | 464 |
| long, no reload | 49 % → 19 % | 22.0 px | 0.44 | 0.39 | 1616 | quarters: 0.30 → 0.27 → 0.22 → 0.18

Numbers say: light vs heavy: width 29.6 → 47.5 px, dark 0.45 → 0.45.

## Brush Artist · Refs · #37 Oil still life dabs
Oil 0.89 · Oil glaze 0.11 · 40 px · 23.0 s

![Brush Artist · Refs · #37 Oil still life dabs](Brush-Artist-Refs-37-Oil-still-life-dabs.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 11 % → 11 % | 32.1 px | 0.36 | 1.00 | 193 |
| heavy line | 12 % → 12 % | 36.1 px | 0.39 | 1.00 | 261 |
| pressure swell | 10 % → 10 % | 39.3 px | 0.40 | 1.00 | 485 |
| fast wave | 30 % → 30 % | 35.0 px | 0.39 | 1.00 | 895 |
| slow wave | 35 % → 35 % | 40.6 px | 0.37 | 1.00 | 1577 |
| spiral | 52 % → 52 % | 34.4 px | 0.38 | 1.00 | 2336 |
| loop | 29 % → 29 % | 36.9 px | 0.39 | 1.00 | 679 |
| tilted | 12 % → 12 % | 34.7 px | 0.41 | 1.00 | 268 |
| over the wet one | 23 % → 23 % | 30.6 px | 0.41 | 1.00 | 532 |
| long, no reload | 59 % → 59 % | 26.6 px | 0.31 | 1.00 | 972 | quarters: 0.23 → 0.22 → 0.20 → 0.17

Numbers say: light vs heavy: width 32.1 → 36.1 px, dark 0.36 → 0.39.

## Brush Artist · Refs · #38 Sanguine drawing
Pastel 1.00 · 6 px · 11.8 s

![Brush Artist · Refs · #38 Sanguine drawing](Brush-Artist-Refs-38-Sanguine-drawing.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 1 % → 1 % | 2.1 px | 0.61 | 1.00 | 60 |
| heavy line | 1 % → 1 % | 3.9 px | 0.61 | 1.00 | 27 |
| pressure swell | 1 % → 1 % | 3.8 px | 0.61 | 1.00 | 13 |
| fast wave | 3 % → 3 % | 3.4 px | 0.61 | 1.00 | 136 |
| slow wave | 3 % → 3 % | 3.4 px | 0.61 | 1.00 | 92 |
| spiral | 4 % → 4 % | 2.8 px | 0.61 | 1.00 | 216 |
| loop | 2 % → 2 % | 3.1 px | 0.61 | 1.00 | 77 |
| tilted | 1 % → 1 % | 3.4 px | 0.61 | 1.00 | 27 |
| over the wet one | 2 % → 2 % | 2.9 px | 0.61 | 1.00 | 30 |
| long, no reload | 6 % → 6 % | 2.7 px | 0.61 | 1.00 | 116 | quarters: 0.04 → 0.04 → 0.04 → 0.04

Numbers say: light vs heavy: width 2.1 → 3.9 px, dark 0.61 → 0.61; the long stroke does not run out of paint.

## Brush Artist · Refs · #39 Very thick impasto
Impasto 1.00 · 60 px · 23.5 s

![Brush Artist · Refs · #39 Very thick impasto](Brush-Artist-Refs-39-Very-thick-impasto.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 18 % → 18 % | 53.1 px | 0.61 | 0.97 | 577 |
| heavy line | 21 % → 20 % | 60.0 px | 0.62 | 0.96 | 394 |
| pressure swell | 15 % → 15 % | 58.1 px | 0.62 | 0.97 | 180 |
| fast wave | 48 % → 47 % | 55.3 px | 0.63 | 0.98 | 590 |
| slow wave | 47 % → 45 % | 53.9 px | 0.61 | 0.97 | 830 |
| spiral | 69 % → 63 % | 45.3 px | 0.61 | 0.92 | 1010 |
| loop | 40 % → 39 % | 52.1 px | 0.61 | 0.97 | 445 |
| tilted | 16 % → 16 % | 43.8 px | 0.62 | 1.00 | 279 |
| over the wet one | 34 % → 33 % | 50.1 px | 0.62 | 0.97 | 208 |
| long, no reload | 85 % → 79 % | 38.0 px | 0.60 | 0.93 | 1477 | quarters: 0.56 → 0.55 → 0.54 → 0.51

Numbers say: light vs heavy: width 53.1 → 60.0 px, dark 0.61 → 0.62; the long stroke does not run out of paint.

## Brush Artist · Refs · #40 Watercolour blooms
Watercolour 1.00 · 90 px · 53.3 s

![Brush Artist · Refs · #40 Watercolour blooms](Brush-Artist-Refs-40-Watercolour-blooms.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 27 % → 47 % | 78.4 px | 0.08 | 1.72 | 200 |
| heavy line | 38 % → 51 % | 110.0 px | 0.09 | 1.36 | 289 |
| pressure swell | 24 % → 39 % | 91.8 px | 0.09 | 1.61 | 210 |
| fast wave | 68 % → 82 % | 78.3 px | 0.11 | 1.21 | 624 |
| slow wave | 68 % → 81 % | 79.1 px | 0.15 | 1.18 | 1110 |
| spiral | 81 % → 92 % | 53.5 px | 0.14 | 1.14 | 988 |
| loop | 58 % → 72 % | 75.3 px | 0.13 | 1.24 | 539 |
| tilted | 34 % → 36 % | 94.8 px | 0.11 | 1.07 | 368 |
| over the wet one | 62 % → 81 % | 78.2 px | 0.11 | 1.31 | 263 |
| long, no reload | 97 % → 100 % | 43.6 px | 0.17 | 1.03 | 1777 | quarters: 0.21 → 0.20 → 0.17 → 0.13

Numbers say: light vs heavy: width 78.4 → 110.0 px, dark 0.08 → 0.09; wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #41 Coloured pencil hatching
Pastel 1.00 · 4 px · 9.8 s

![Brush Artist · Refs · #41 Coloured pencil hatching](Brush-Artist-Refs-41-Coloured-pencil-hatching.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 1 % → 1 % | 1.6 px | 0.43 | 1.00 | 11 |
| heavy line | 1 % → 1 % | 2.9 px | 0.43 | 1.00 | 12 |
| pressure swell | 1 % → 1 % | 2.8 px | 0.43 | 1.00 | 9 |
| fast wave | 2 % → 2 % | 2.5 px | 0.43 | 1.00 | 32 |
| slow wave | 2 % → 2 % | 2.5 px | 0.43 | 1.00 | 52 |
| spiral | 3 % → 3 % | 2.1 px | 0.43 | 1.00 | 49 |
| loop | 2 % → 2 % | 2.3 px | 0.43 | 1.00 | 34 |
| tilted | 1 % → 1 % | 3.0 px | 0.43 | 1.00 | 16 |
| over the wet one | 2 % → 2 % | 2.3 px | 0.43 | 1.00 | 11 |
| long, no reload | 5 % → 5 % | 2.0 px | 0.42 | 1.00 | 78 | quarters: 0.02 → 0.02 → 0.02 → 0.02

Numbers say: light vs heavy: width 1.6 → 2.9 px, dark 0.43 → 0.43; the long stroke does not run out of paint.

## Brush Artist · Refs · #42 Oil pastel shaggy
Pastel 1.00 · 18 px · 10.5 s

![Brush Artist · Refs · #42 Oil pastel shaggy](Brush-Artist-Refs-42-Oil-pastel-shaggy.png)

A light paint: laid on a grey sheet (on white it cannot be seen); **dark** = how far it is from the grey either way.

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 2 % → 2 % | 4.7 px | 0.36 | 1.00 | 19 |
| heavy line | 3 % → 3 % | 10.0 px | 0.36 | 1.00 | 17 |
| pressure swell | 2 % → 2 % | 9.3 px | 0.34 | 1.00 | 24 |
| fast wave | 8 % → 8 % | 9.2 px | 0.32 | 1.00 | 82 |
| slow wave | 7 % → 7 % | 8.6 px | 0.37 | 1.00 | 95 |
| spiral | 11 % → 11 % | 7.5 px | 0.36 | 1.00 | 128 |
| loop | 6 % → 6 % | 7.8 px | 0.35 | 1.00 | 55 |
| tilted | 2 % → 2 % | 6.5 px | 0.33 | 1.00 | 57 |
| over the wet one | 5 % → 5 % | 7.6 px | 0.33 | 1.00 | 30 |
| long, no reload | 15 % → 15 % | 6.5 px | 0.37 | 1.00 | 155 | quarters: 0.00 → 0.00 → 0.00 → 0.00

Numbers say: light vs heavy: width 4.7 → 10.0 px, dark 0.36 → 0.36; the long stroke does not run out of paint.

## Brush Artist · Refs · #43 Dragged black ink blocks
Gouache 1.00 · 70 px · 27.8 s

![Brush Artist · Refs · #43 Dragged black ink blocks](Brush-Artist-Refs-43-Dragged-black-ink-blocks.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 5 % → 0 % | 14.8 px | 0.00 | 0.00 | 225 |
| heavy line | 14 % → 4 % | 40.5 px | 0.66 | 0.27 | 296 |
| pressure swell | 11 % → 4 % | 42.1 px | 0.65 | 0.33 | 181 |
| fast wave | 38 % → 1 % | 43.8 px | 0.66 | 0.03 | 575 |
| slow wave | 32 % → 2 % | 36.6 px | 0.57 | 0.05 | 1311 |
| spiral | 51 % → 4 % | 33.4 px | 0.54 | 0.07 | 1027 |
| loop | 30 % → 2 % | 38.3 px | 0.62 | 0.06 | 570 |
| tilted | 13 % → 13 % | 37.0 px | 0.66 | 0.95 | 301 |
| over the wet one | 21 % → 2 % | 22.9 px | 0.66 | 0.10 | 260 |
| long, no reload | 44 % → 7 % | 19.8 px | 0.66 | 0.16 | 1215 | quarters: 0.47 → 0.37 → 0.18 → 0.13

Numbers say: light vs heavy: width 14.8 → 40.5 px, dark 0.00 → 0.66.

## Brush Artist · Refs · #44 Blue looping ribbon
Oil 1.00 · 80 px · 28.2 s

![Brush Artist · Refs · #44 Blue looping ribbon](Brush-Artist-Refs-44-Blue-looping-ribbon.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 25 % → 26 % | 73.1 px | 0.72 | 1.04 | 254 |
| heavy line | 27 % → 27 % | 77.7 px | 0.71 | 1.00 | 336 |
| pressure swell | 20 % → 21 % | 76.5 px | 0.71 | 1.03 | 228 |
| fast wave | 62 % → 64 % | 71.4 px | 0.71 | 1.04 | 1340 |
| slow wave | 58 % → 58 % | 67.4 px | 0.70 | 1.00 | 1691 |
| spiral | 76 % → 77 % | 50.3 px | 0.69 | 1.00 | 2043 |
| loop | 53 % → 53 % | 69.2 px | 0.69 | 1.00 | 738 |
| tilted | 20 % → 20 % | 56.1 px | 0.74 | 1.00 | 380 |
| over the wet one | 41 % → 41 % | 58.7 px | 0.74 | 1.00 | 355 |
| long, no reload | 90 % → 90 % | 40.1 px | 0.69 | 1.00 | 1965 | quarters: 0.67 → 0.68 → 0.66 → 0.59

Numbers say: light vs heavy: width 73.1 → 77.7 px, dark 0.72 → 0.71; pressure barely changes the width; the long stroke does not run out of paint.

## Brush Artist · Refs · #45 Soft pastel pepper
Pastel 1.00 · 40 px · 11.2 s

![Brush Artist · Refs · #45 Soft pastel pepper](Brush-Artist-Refs-45-Soft-pastel-pepper.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 4 % → 4 % | 11.0 px | 0.53 | 1.00 | 105 |
| heavy line | 7 % → 7 % | 21.2 px | 0.53 | 1.00 | 71 |
| pressure swell | 5 % → 5 % | 19.0 px | 0.55 | 1.00 | 53 |
| fast wave | 17 % → 17 % | 19.3 px | 0.56 | 1.00 | 143 |
| slow wave | 16 % → 16 % | 18.0 px | 0.54 | 1.00 | 271 |
| spiral | 23 % → 23 % | 15.4 px | 0.54 | 1.00 | 311 |
| loop | 12 % → 12 % | 15.4 px | 0.54 | 1.00 | 145 |
| tilted | 4 % → 4 % | 11.4 px | 0.55 | 1.00 | 82 |
| over the wet one | 10 % → 10 % | 16.7 px | 0.55 | 1.00 | 74 |
| long, no reload | 28 % → 28 % | 12.6 px | 0.53 | 1.00 | 445 | quarters: 0.17 → 0.16 → 0.17 → 0.17

Numbers say: light vs heavy: width 11.0 → 21.2 px, dark 0.53 → 0.53; the long stroke does not run out of paint.

## Brush Artist · Refs · #46 Red-brown ink lips
Watercolour 1.00 · 50 px · 43.7 s

![Brush Artist · Refs · #46 Red-brown ink lips](Brush-Artist-Refs-46-Red-brown-ink-lips.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 15 % → 31 % | 43.9 px | 0.59 | 2.04 | 78 |
| heavy line | 22 % → 35 % | 63.4 px | 0.60 | 1.58 | 94 |
| pressure swell | 13 % → 22 % | 50.3 px | 0.63 | 1.64 | 87 |
| fast wave | 43 % → 64 % | 49.7 px | 0.64 | 1.50 | 210 |
| slow wave | 42 % → 63 % | 49.1 px | 0.67 | 1.49 | 539 |
| spiral | 65 % → 79 % | 42.6 px | 0.69 | 1.22 | 389 |
| loop | 38 % → 55 % | 48.8 px | 0.67 | 1.47 | 198 |
| tilted | 21 % → 23 % | 58.2 px | 0.60 | 1.11 | 124 |
| over the wet one | 42 % → 63 % | 58.5 px | 0.60 | 1.51 | 101 |
| long, no reload | 78 % → 95 % | 35.1 px | 0.70 | 1.21 | 618 | quarters: 0.71 → 0.71 → 0.69 → 0.65

Numbers say: light vs heavy: width 43.9 → 63.4 px, dark 0.59 → 0.60; the long stroke does not run out of paint; wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #47 Pink knife slabs
Impasto 1.00 · 90 px · 32.2 s

![Brush Artist · Refs · #47 Pink knife slabs](Brush-Artist-Refs-47-Pink-knife-slabs.png)

A light paint: laid on a grey sheet (on white it cannot be seen); **dark** = how far it is from the grey either way.

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 27 % → 26 % | 78.7 px | 0.29 | 0.97 | 245 |
| heavy line | 29 % → 28 % | 84.6 px | 0.29 | 0.96 | 336 |
| pressure swell | 22 % → 22 % | 81.2 px | 0.26 | 1.01 | 188 |
| fast wave | 62 % → 61 % | 71.8 px | 0.24 | 0.98 | 657 |
| slow wave | 62 % → 58 % | 71.5 px | 0.28 | 0.94 | 1019 |
| spiral | 75 % → 60 % | 49.3 px | 0.28 | 0.80 | 1112 |
| loop | 56 % → 54 % | 72.1 px | 0.29 | 0.97 | 667 |
| tilted | 22 % → 22 % | 60.2 px | 0.25 | 1.00 | 331 |
| over the wet one | 46 % → 44 % | 69.3 px | 0.25 | 0.96 | 313 |
| long, no reload | 93 % → 77 % | 41.9 px | 0.26 | 0.83 | 1629 | quarters: 0.00 → 0.00 → 0.00 → 0.00

Numbers say: light vs heavy: width 78.7 → 84.6 px, dark 0.29 → 0.29; pressure barely changes the width; the long stroke does not run out of paint.

## Brush Artist · Refs · #48 Black bands with drips
Gouache 1.00 · 70 px · 50.8 s

![Brush Artist · Refs · #48 Black bands with drips](Brush-Artist-Refs-48-Black-bands-with-drips.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 28 % → 23 % | 80.2 px | 0.63 | 0.82 | 181 |
| heavy line | 35 % → 26 % | 100.7 px | 0.64 | 0.75 | 291 |
| pressure swell | 25 % → 21 % | 93.8 px | 0.63 | 0.85 | 229 |
| fast wave | 63 % → 41 % | 72.9 px | 0.63 | 0.64 | 540 |
| slow wave | 62 % → 41 % | 71.5 px | 0.63 | 0.66 | 932 |
| spiral | 69 % → 40 % | 45.7 px | 0.61 | 0.57 | 929 |
| loop | 54 % → 40 % | 69.9 px | 0.63 | 0.74 | 519 |
| tilted | 29 % → 29 % | 80.5 px | 0.62 | 1.01 | 1298 |
| over the wet one | 59 % → 48 % | 82.9 px | 0.62 | 0.82 | 255 |
| long, no reload | 78 % → 37 % | 34.9 px | 0.61 | 0.47 | 1806 | quarters: 0.58 → 0.54 → 0.47 → 0.39

Numbers say: light vs heavy: width 80.2 → 100.7 px, dark 0.63 → 0.64.

## Brush Artist · Refs · #49 Magenta letters round brush
Ink 1.00 · 30 px · 33.5 s

![Brush Artist · Refs · #49 Magenta letters round brush](Brush-Artist-Refs-49-Magenta-letters-round-brush.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 6 % → 8 % | 18.1 px | 0.49 | 1.21 | 48 |
| heavy line | 21 % → 20 % | 60.3 px | 0.51 | 0.98 | 107 |
| pressure swell | 13 % → 13 % | 47.1 px | 0.51 | 1.01 | 68 |
| fast wave | 38 % → 38 % | 44.0 px | 0.51 | 1.00 | 175 |
| slow wave | 34 % → 34 % | 39.4 px | 0.51 | 0.99 | 290 |
| spiral | 49 % → 48 % | 32.6 px | 0.51 | 0.96 | 333 |
| loop | 30 % → 30 % | 38.3 px | 0.51 | 1.00 | 153 |
| tilted | 11 % → 12 % | 32.0 px | 0.52 | 1.00 | 102 |
| over the wet one | 27 % → 27 % | 42.2 px | 0.52 | 1.01 | 86 |
| long, no reload | 63 % → 56 % | 28.2 px | 0.50 | 0.90 | 567 | quarters: 0.42 → 0.37 → 0.30 → 0.25

Numbers say: light vs heavy: width 18.1 → 60.3 px, dark 0.49 → 0.51.

## Brush Artist · Refs · #50 Thick swipes on photo
Impasto 1.00 · 40 px · 19.8 s

![Brush Artist · Refs · #50 Thick swipes on photo](Brush-Artist-Refs-50-Thick-swipes-on-photo.png)

A light paint: laid on a grey sheet (on white it cannot be seen); **dark** = how far it is from the grey either way.

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 13 % → 13 % | 38.6 px | 0.27 | 0.95 | 138 |
| heavy line | 14 % → 13 % | 40.0 px | 0.27 | 0.96 | 115 |
| pressure swell | 11 % → 10 % | 40.1 px | 0.24 | 0.95 | 69 |
| fast wave | 35 % → 31 % | 40.1 px | 0.24 | 0.89 | 307 |
| slow wave | 34 % → 32 % | 39.5 px | 0.26 | 0.93 | 523 |
| spiral | 58 % → 46 % | 38.5 px | 0.29 | 0.79 | 520 |
| loop | 29 % → 28 % | 37.4 px | 0.26 | 0.96 | 287 |
| tilted | 12 % → 12 % | 33.6 px | 0.22 | 1.00 | 192 |
| over the wet one | 25 % → 24 % | 36.7 px | 0.22 | 0.96 | 171 |
| long, no reload | 68 % → 46 % | 30.4 px | 0.26 | 0.68 | 885 | quarters: 0.00 → 0.00 → 0.00 → 0.00

Numbers say: light vs heavy: width 38.6 → 40.0 px, dark 0.27 → 0.27; pressure barely changes the width.

## Brush Artist · Refs · Drag #e8b4a8
Gouache 1.00 · 40 px · 20.5 s

![Brush Artist · Refs · Drag #e8b4a8](Brush-Artist-Refs-Drag-e8b4a8.png)

A light paint: laid on a grey sheet (on white it cannot be seen); **dark** = how far it is from the grey either way.

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 3 % → 0 % | 9.3 px | 0.00 | 0.00 | 104 |
| heavy line | 6 % → 0 % | 16.2 px | 0.34 | 0.01 | 129 |
| pressure swell | 3 % → 0 % | 12.9 px | 0.00 | 0.00 | 89 |
| fast wave | 16 % → 0 % | 18.1 px | 0.00 | 0.00 | 317 |
| slow wave | 13 % → 0 % | 15.0 px | 0.00 | 0.00 | 528 |
| spiral | 20 % → 0 % | 13.4 px | 0.00 | 0.00 | 498 |
| loop | 13 % → 0 % | 17.1 px | 0.00 | 0.00 | 339 |
| tilted | 6 % → 5 % | 16.8 px | 0.00 | 0.77 | 142 |
| over the wet one | 7 % → 0 % | 1.8 px | 0.00 | 0.00 | 112 |
| long, no reload | 10 % → 0 % | 4.6 px | 0.00 | 0.00 | 736 | quarters: 0.02 → 0.02 → 0.02 → 0.02

Numbers say: light vs heavy: width 9.3 → 16.2 px, dark 0.00 → 0.34; the long stroke does not run out of paint.

## Brush Artist · Refs · Drag #e8e4e0
Gouache 1.00 · 40 px · 20.0 s

![Brush Artist · Refs · Drag #e8e4e0](Brush-Artist-Refs-Drag-e8e4e0.png)

A light paint: laid on a grey sheet (on white it cannot be seen); **dark** = how far it is from the grey either way.

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 3 % → 0 % | 9.3 px | 0.00 | 0.00 | 115 |
| heavy line | 6 % → 0 % | 16.2 px | 0.43 | 0.01 | 163 |
| pressure swell | 3 % → 0 % | 12.9 px | 0.00 | 0.00 | 99 |
| fast wave | 16 % → 0 % | 18.1 px | 0.00 | 0.00 | 469 |
| slow wave | 13 % → 0 % | 15.0 px | 0.00 | 0.00 | 788 |
| spiral | 20 % → 0 % | 13.4 px | 0.00 | 0.00 | 578 |
| loop | 13 % → 0 % | 17.1 px | 0.00 | 0.00 | 298 |
| tilted | 6 % → 5 % | 16.8 px | 0.00 | 0.77 | 292 |
| over the wet one | 7 % → 0 % | 1.8 px | 0.00 | 0.00 | 422 |
| long, no reload | 10 % → 0 % | 4.6 px | 0.00 | 0.00 | 840 | quarters: 0.02 → 0.02 → 0.02 → 0.02

Numbers say: light vs heavy: width 9.3 → 16.2 px, dark 0.00 → 0.43; the long stroke does not run out of paint.

## Brush Artist · Refs · Finger
Pastel 1.00 · 36 px · 22.6 s · over bands of wet oil paint and oil pastel in turn (it works on paint already there: look at what it does to the bands; covered counts the bands too)

![Brush Artist · Refs · Finger](Brush-Artist-Refs-Finger.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 26 % → 26 % | 74.4 px | 0.80 | 1.00 | 86 |
| heavy line | 27 % → 27 % | 79.3 px | 0.80 | 1.00 | 46 |
| pressure swell | 26 % → 26 % | 98.0 px | 0.80 | 1.00 | 39 |
| fast wave | 33 % → 33 % | 38.0 px | 0.78 | 1.00 | 129 |
| slow wave | 31 % → 31 % | 36.3 px | 0.78 | 1.00 | 244 |
| spiral | 38 % → 38 % | 25.3 px | 0.76 | 1.00 | 693 |
| loop | 31 % → 31 % | 39.5 px | 0.79 | 1.00 | 158 |
| tilted | 26 % → 26 % | 73.5 px | 0.78 | 1.00 | 62 |
| over the wet one | 29 % → 29 % | 7.5 px | 0.78 | 1.00 | 72 |
| long, no reload | 39 % → 39 % | 17.4 px | 0.76 | 1.00 | 447 | quarters: 0.24 → 0.36 → 0.32 → 0.37

Numbers say: light vs heavy: width 74.4 → 79.3 px, dark 0.80 → 0.80; pressure barely changes the width; the long stroke does not run out of paint.

## Brush Artist · Ink — wash
Watercolour 1.00 · 38 px · 35.1 s

![Brush Artist · Ink — wash](Brush-Artist-Ink-wash.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 11 % → 11 % | 31.6 px | 0.39 | 1.04 | 72 |
| heavy line | 19 % → 19 % | 54.3 px | 0.32 | 1.03 | 123 |
| pressure swell | 12 % → 13 % | 45.2 px | 0.37 | 1.04 | 53 |
| fast wave | 39 % → 41 % | 45.5 px | 0.31 | 1.04 | 200 |
| slow wave | 37 % → 38 % | 42.9 px | 0.37 | 1.03 | 377 |
| spiral | 58 % → 61 % | 38.6 px | 0.31 | 1.04 | 678 |
| loop | 32 % → 33 % | 41.9 px | 0.35 | 1.02 | 238 |
| tilted | 13 % → 14 % | 37.0 px | 0.38 | 1.04 | 130 |
| over the wet one | 29 % → 30 % | 42.8 px | 0.38 | 1.04 | 132 |
| long, no reload | 67 % → 72 % | 30.0 px | 0.29 | 1.07 | 529 | quarters: 0.34 → 0.27 → 0.19 → 0.12

Numbers say: light vs heavy: width 31.6 → 54.3 px, dark 0.39 → 0.32.

## Brush Artist · Ink — brush line
Ink 1.00 · 16 px · 28.9 s

![Brush Artist · Ink — brush line](Brush-Artist-Ink-brush-line.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 3 % → 5 % | 8.2 px | 0.77 | 1.72 | 50 |
| heavy line | 12 % → 12 % | 35.2 px | 0.88 | 0.99 | 100 |
| pressure swell | 8 % → 8 % | 28.5 px | 0.86 | 1.06 | 60 |
| fast wave | 24 % → 24 % | 28.2 px | 0.87 | 0.98 | 218 |
| slow wave | 20 % → 20 % | 23.7 px | 0.87 | 0.97 | 173 |
| spiral | 31 % → 27 % | 20.3 px | 0.86 | 0.87 | 340 |
| loop | 19 % → 19 % | 24.3 px | 0.87 | 0.99 | 135 |
| tilted | 8 % → 8 % | 21.2 px | 0.88 | 1.01 | 62 |
| over the wet one | 17 % → 17 % | 26.2 px | 0.88 | 1.01 | 56 |
| long, no reload | 44 % → 31 % | 19.7 px | 0.84 | 0.70 | 396 | quarters: 0.51 → 0.41 → 0.30 → 0.20

Numbers say: light vs heavy: width 8.2 → 35.2 px, dark 0.77 → 0.88; wet paint spreads well beyond the stroke.

## Brush Artist · Ink — dry brush
Gouache 1.00 · 30 px · 20.9 s

![Brush Artist · Ink — dry brush](Brush-Artist-Ink-dry-brush.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 2 % → 0 % | 5.7 px | 0.00 | 0.00 | 68 |
| heavy line | 4 % → 0 % | 10.2 px | 0.77 | 0.01 | 138 |
| pressure swell | 4 % → 0 % | 14.1 px | 0.77 | 0.06 | 96 |
| fast wave | 12 % → 0 % | 14.0 px | 0.77 | 0.00 | 231 |
| slow wave | 10 % → 0 % | 11.9 px | 0.77 | 0.00 | 380 |
| spiral | 17 % → 0 % | 11.1 px | 0.77 | 0.00 | 374 |
| loop | 9 % → 0 % | 11.2 px | 0.77 | 0.01 | 195 |
| tilted | 5 % → 4 % | 13.5 px | 0.77 | 0.89 | 107 |
| over the wet one | 7 % → 0 % | 5.9 px | 0.77 | 0.00 | 98 |
| long, no reload | 14 % → 1 % | 6.5 px | 0.77 | 0.08 | 569 | quarters: 0.21 → 0.14 → 0.10 → 0.07

Numbers say: light vs heavy: width 5.7 → 10.2 px, dark 0.00 → 0.77.

## Brush Artist · Watercolour — blue
Watercolour 0.93 · Ink 0.07 · 40 px · 30.8 s

![Brush Artist · Watercolour — blue](Brush-Artist-Watercolour-blue.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 6 % → 11 % | 16.2 px | 0.29 | 1.88 | 34 |
| heavy line | 11 % → 13 % | 31.9 px | 0.29 | 1.17 | 64 |
| pressure swell | 7 % → 9 % | 25.7 px | 0.30 | 1.38 | 57 |
| fast wave | 24 % → 27 % | 28.2 px | 0.29 | 1.12 | 140 |
| slow wave | 23 % → 32 % | 26.4 px | 0.31 | 1.41 | 271 |
| spiral | 39 % → 47 % | 25.6 px | 0.29 | 1.21 | 256 |
| loop | 20 % → 25 % | 25.7 px | 0.30 | 1.25 | 144 |
| tilted | 12 % → 12 % | 34.0 px | 0.30 | 1.00 | 73 |
| over the wet one | 21 % → 25 % | 25.2 px | 0.30 | 1.19 | 64 |
| long, no reload | 53 % → 59 % | 23.6 px | 0.30 | 1.12 | 377 | quarters: 0.23 → 0.21 → 0.19 → 0.16

Numbers say: light vs heavy: width 16.2 → 31.9 px, dark 0.29 → 0.29; wet paint spreads well beyond the stroke.

## Brush Artist · Watercolour — violet
Watercolour 0.93 · Ink 0.07 · 40 px · 29.9 s

![Brush Artist · Watercolour — violet](Brush-Artist-Watercolour-violet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 6 % → 11 % | 16.2 px | 0.36 | 1.88 | 30 |
| heavy line | 11 % → 13 % | 31.9 px | 0.37 | 1.17 | 66 |
| pressure swell | 7 % → 9 % | 25.7 px | 0.38 | 1.38 | 37 |
| fast wave | 24 % → 27 % | 28.2 px | 0.38 | 1.12 | 133 |
| slow wave | 23 % → 32 % | 26.4 px | 0.39 | 1.41 | 183 |
| spiral | 39 % → 47 % | 25.6 px | 0.37 | 1.21 | 223 |
| loop | 20 % → 25 % | 25.7 px | 0.38 | 1.25 | 110 |
| tilted | 12 % → 12 % | 34.0 px | 0.38 | 1.00 | 100 |
| over the wet one | 21 % → 25 % | 25.2 px | 0.38 | 1.19 | 93 |
| long, no reload | 53 % → 59 % | 23.6 px | 0.38 | 1.12 | 511 | quarters: 0.28 → 0.27 → 0.24 → 0.21

Numbers say: light vs heavy: width 16.2 → 31.9 px, dark 0.36 → 0.37; wet paint spreads well beyond the stroke.

## Brush Artist · Watercolour — teal
Watercolour 0.93 · Ink 0.07 · 40 px · 30.2 s

![Brush Artist · Watercolour — teal](Brush-Artist-Watercolour-teal.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 6 % → 11 % | 16.2 px | 0.23 | 1.88 | 31 |
| heavy line | 11 % → 13 % | 31.9 px | 0.23 | 1.17 | 78 |
| pressure swell | 7 % → 9 % | 25.7 px | 0.24 | 1.38 | 41 |
| fast wave | 24 % → 27 % | 28.2 px | 0.23 | 1.12 | 173 |
| slow wave | 23 % → 32 % | 26.4 px | 0.25 | 1.41 | 246 |
| spiral | 39 % → 47 % | 25.6 px | 0.23 | 1.21 | 221 |
| loop | 20 % → 25 % | 25.7 px | 0.24 | 1.25 | 158 |
| tilted | 12 % → 12 % | 34.0 px | 0.24 | 1.00 | 116 |
| over the wet one | 21 % → 25 % | 25.2 px | 0.24 | 1.19 | 73 |
| long, no reload | 53 % → 59 % | 23.6 px | 0.24 | 1.12 | 1292 | quarters: 0.18 → 0.16 → 0.15 → 0.13

Numbers say: light vs heavy: width 16.2 → 31.9 px, dark 0.23 → 0.23; wet paint spreads well beyond the stroke.

## Brush Artist · Gouache
Gouache 1.00 · 30 px · 32.9 s

![Brush Artist · Gouache](Brush-Artist-Gouache.png)

A light paint: laid on a grey sheet (on white it cannot be seen); **dark** = how far it is from the grey either way.

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 8 % → 8 % | 24.4 px | 0.27 | 0.97 | 76 |
| heavy line | 15 % → 12 % | 42.8 px | 0.27 | 0.78 | 89 |
| pressure swell | 11 % → 9 % | 41.0 px | 0.27 | 0.85 | 55 |
| fast wave | 30 % → 14 % | 34.9 px | 0.26 | 0.45 | 210 |
| slow wave | 29 % → 14 % | 34.0 px | 0.26 | 0.47 | 315 |
| spiral | 40 % → 14 % | 26.6 px | 0.26 | 0.35 | 400 |
| loop | 24 % → 15 % | 30.6 px | 0.26 | 0.62 | 200 |
| tilted | 10 % → 10 % | 27.4 px | 0.27 | 1.01 | 131 |
| over the wet one | 22 % → 19 % | 32.9 px | 0.27 | 0.89 | 135 |
| long, no reload | 43 % → 15 % | 19.1 px | 0.26 | 0.35 | 592 | quarters: 0.01 → 0.01 → 0.01 → 0.01

Numbers say: light vs heavy: width 24.4 → 42.8 px, dark 0.27 → 0.27; the long stroke does not run out of paint.

## Brush Artist · Oil — bristle
Oil 0.89 · Oil glaze 0.11 · 30 px · 16.5 s

![Brush Artist · Oil — bristle](Brush-Artist-Oil-bristle.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 10 % → 10 % | 28.5 px | 0.53 | 1.00 | 107 |
| heavy line | 11 % → 11 % | 32.4 px | 0.54 | 1.00 | 111 |
| pressure swell | 8 % → 8 % | 31.8 px | 0.54 | 1.00 | 73 |
| fast wave | 28 % → 28 % | 32.0 px | 0.54 | 1.00 | 336 |
| slow wave | 27 % → 27 % | 31.6 px | 0.54 | 1.00 | 490 |
| spiral | 48 % → 48 % | 31.3 px | 0.53 | 1.00 | 564 |
| loop | 22 % → 22 % | 28.9 px | 0.54 | 1.00 | 351 |
| tilted | 11 % → 11 % | 29.9 px | 0.54 | 1.00 | 184 |
| over the wet one | 21 % → 21 % | 29.6 px | 0.54 | 1.00 | 187 |
| long, no reload | 55 % → 55 % | 24.7 px | 0.52 | 1.00 | 1985 | quarters: 0.35 → 0.33 → 0.31 → 0.29

Numbers say: light vs heavy: width 28.5 → 32.4 px, dark 0.53 → 0.54.

## Brush Artist · Charcoal — stick
Charcoal 0.78 · Pastel 0.22 · 28 px · 12.0 s

![Brush Artist · Charcoal — stick](Brush-Artist-Charcoal-stick.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 5 % → 5 % | 15.2 px | 0.85 | 1.00 | 30 |
| heavy line | 8 % → 8 % | 24.2 px | 0.85 | 1.00 | 31 |
| pressure swell | 5 % → 5 % | 19.3 px | 0.85 | 1.00 | 20 |
| fast wave | 19 % → 19 % | 21.5 px | 0.85 | 1.00 | 55 |
| slow wave | 18 % → 18 % | 21.1 px | 0.85 | 1.00 | 105 |
| spiral | 25 % → 25 % | 16.3 px | 0.85 | 1.00 | 136 |
| loop | 16 % → 16 % | 20.2 px | 0.85 | 1.00 | 78 |
| tilted | 6 % → 6 % | 17.3 px | 0.85 | 1.00 | 32 |
| over the wet one | 14 % → 14 % | 20.5 px | 0.85 | 1.00 | 26 |
| long, no reload | 41 % → 41 % | 18.5 px | 0.85 | 1.00 | 218 | quarters: 0.39 → 0.39 → 0.39 → 0.39

Numbers say: light vs heavy: width 15.2 → 24.2 px, dark 0.85 → 0.85; the long stroke does not run out of paint.

## Brush Artist · Charcoal — stick B
Charcoal 0.78 · Pastel 0.22 · 36 px · 10.6 s

![Brush Artist · Charcoal — stick B](Brush-Artist-Charcoal-stick-B.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 7 % → 7 % | 19.2 px | 0.85 | 1.00 | 18 |
| heavy line | 10 % → 10 % | 30.5 px | 0.85 | 1.00 | 46 |
| pressure swell | 7 % → 7 % | 24.5 px | 0.85 | 1.00 | 24 |
| fast wave | 24 % → 24 % | 27.6 px | 0.85 | 1.00 | 105 |
| slow wave | 23 % → 23 % | 26.6 px | 0.85 | 1.00 | 170 |
| spiral | 35 % → 35 % | 23.2 px | 0.85 | 1.00 | 155 |
| loop | 19 % → 19 % | 25.2 px | 0.85 | 1.00 | 71 |
| tilted | 7 % → 7 % | 20.3 px | 0.85 | 1.00 | 39 |
| over the wet one | 17 % → 17 % | 25.9 px | 0.85 | 1.00 | 34 |
| long, no reload | 50 % → 50 % | 22.6 px | 0.85 | 1.00 | 233 | quarters: 0.47 → 0.47 → 0.47 → 0.47

Numbers say: light vs heavy: width 19.2 → 30.5 px, dark 0.85 → 0.85; the long stroke does not run out of paint.

## Brush Artist · Charcoal — stick C
Charcoal 0.78 · Pastel 0.22 · 22 px · 9.8 s

![Brush Artist · Charcoal — stick C](Brush-Artist-Charcoal-stick-C.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 4 % → 4 % | 12.2 px | 0.85 | 1.00 | 24 |
| heavy line | 7 % → 7 % | 19.4 px | 0.85 | 1.00 | 22 |
| pressure swell | 4 % → 4 % | 14.3 px | 0.85 | 1.00 | 22 |
| fast wave | 15 % → 15 % | 17.1 px | 0.85 | 1.00 | 39 |
| slow wave | 15 % → 15 % | 17.0 px | 0.85 | 1.00 | 78 |
| spiral | 20 % → 20 % | 13.3 px | 0.85 | 1.00 | 94 |
| loop | 12 % → 12 % | 16.1 px | 0.85 | 1.00 | 52 |
| tilted | 5 % → 5 % | 15.1 px | 0.85 | 1.00 | 62 |
| over the wet one | 11 % → 11 % | 16.8 px | 0.85 | 1.00 | 23 |
| long, no reload | 34 % → 34 % | 15.3 px | 0.85 | 1.00 | 157 | quarters: 0.33 → 0.32 → 0.32 → 0.32

Numbers say: light vs heavy: width 12.2 → 19.4 px, dark 0.85 → 0.85; the long stroke does not run out of paint.

## Oil · Henry Ward · Loaded flat
Oil 1.00 · 84 px · 26.7 s

![Oil · Henry Ward · Loaded flat](Oil-Henry-Ward-Loaded-flat.png)

A light paint: laid on a grey sheet (on white it cannot be seen); **dark** = how far it is from the grey either way.

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 18 % → 20 % | 53.2 px | 0.30 | 1.06 | 278 |
| heavy line | 21 % → 21 % | 61.0 px | 0.35 | 1.00 | 400 |
| pressure swell | 20 % → 21 % | 76.0 px | 0.34 | 1.05 | 261 |
| fast wave | 52 % → 55 % | 60.6 px | 0.30 | 1.05 | 1113 |
| slow wave | 55 % → 55 % | 63.3 px | 0.35 | 1.00 | 1547 |
| spiral | 75 % → 75 % | 49.5 px | 0.31 | 1.00 | 1648 |
| loop | 52 % → 52 % | 67.1 px | 0.34 | 1.00 | 835 |
| tilted | 21 % → 21 % | 58.4 px | 0.30 | 1.00 | 450 |
| over the wet one | 40 % → 40 % | 52.9 px | 0.30 | 1.00 | 334 |
| long, no reload | 78 % → 78 % | 35.2 px | 0.29 | 1.00 | 2058 | quarters: 0.00 → 0.00 → 0.00 → 0.00

Numbers say: light vs heavy: width 53.2 → 61.0 px, dark 0.30 → 0.35; the long stroke does not run out of paint.

## Oil · Henry Ward · Dry scrub
Oil 1.00 · 90 px · 20.5 s

![Oil · Henry Ward · Dry scrub](Oil-Henry-Ward-Dry-scrub.png)

A light paint: laid on a grey sheet (on white it cannot be seen); **dark** = how far it is from the grey either way.

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 8 % → 9 % | 21.9 px | 0.18 | 1.21 | 309 |
| heavy line | 14 % → 14 % | 42.1 px | 0.26 | 1.00 | 380 |
| pressure swell | 14 % → 15 % | 51.7 px | 0.24 | 1.09 | 330 |
| fast wave | 51 % → 53 % | 58.7 px | 0.27 | 1.04 | 978 |
| slow wave | 37 % → 37 % | 42.2 px | 0.27 | 1.00 | 1601 |
| spiral | 70 % → 70 % | 46.0 px | 0.22 | 1.00 | 1507 |
| loop | 36 % → 36 % | 46.7 px | 0.22 | 1.00 | 831 |
| tilted | 21 % → 21 % | 57.5 px | 0.21 | 1.00 | 445 |
| over the wet one | 29 % → 29 % | 22.2 px | 0.21 | 1.00 | 296 |
| long, no reload | 49 % → 49 % | 22.1 px | 0.22 | 1.00 | 1805 | quarters: 0.00 → 0.00 → 0.00 → 0.00

Numbers say: light vs heavy: width 21.9 → 42.1 px, dark 0.18 → 0.26.

## Oil · Henry Ward · Dirty contour
Oil 1.00 · 34 px · 14.8 s

![Oil · Henry Ward · Dirty contour](Oil-Henry-Ward-Dirty-contour.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 7 % → 7 % | 20.6 px | 0.72 | 1.00 | 125 |
| heavy line | 12 % → 12 % | 34.2 px | 0.74 | 1.00 | 124 |
| pressure swell | 9 % → 9 % | 35.2 px | 0.78 | 1.00 | 126 |
| fast wave | 28 % → 28 % | 32.5 px | 0.76 | 1.00 | 444 |
| slow wave | 31 % → 31 % | 35.2 px | 0.77 | 1.00 | 604 |
| spiral | 42 % → 42 % | 27.5 px | 0.74 | 1.00 | 625 |
| loop | 25 % → 25 % | 32.4 px | 0.76 | 1.00 | 358 |
| tilted | 12 % → 12 % | 32.3 px | 0.78 | 1.00 | 166 |
| over the wet one | 23 % → 23 % | 32.0 px | 0.78 | 1.00 | 151 |
| long, no reload | 50 % → 50 % | 22.6 px | 0.72 | 1.00 | 839 | quarters: 0.50 → 0.44 → 0.34 → 0.33

Numbers say: light vs heavy: width 20.6 → 34.2 px, dark 0.72 → 0.74.

## Oil · Henry Ward · Wet drag
Oil 1.00 · 80 px · 25.1 s

![Oil · Henry Ward · Wet drag](Oil-Henry-Ward-Wet-drag.png)

A light paint: laid on a grey sheet (on white it cannot be seen); **dark** = how far it is from the grey either way.

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 10 % → 10 % | 28.7 px | 0.23 | 1.03 | 348 |
| heavy line | 18 % → 18 % | 53.1 px | 0.34 | 1.00 | 303 |
| pressure swell | 17 % → 17 % | 62.6 px | 0.28 | 1.04 | 241 |
| fast wave | 48 % → 50 % | 55.6 px | 0.26 | 1.04 | 809 |
| slow wave | 53 % → 53 % | 61.7 px | 0.29 | 1.00 | 1452 |
| spiral | 71 % → 71 % | 46.6 px | 0.31 | 1.00 | 1621 |
| loop | 38 % → 38 % | 49.4 px | 0.25 | 1.00 | 652 |
| tilted | 19 % → 19 % | 52.3 px | 0.29 | 1.00 | 438 |
| over the wet one | 36 % → 36 % | 48.7 px | 0.29 | 1.00 | 330 |
| long, no reload | 78 % → 78 % | 34.8 px | 0.29 | 1.00 | 1992 | quarters: 0.00 → 0.00 → 0.00 → 0.00

Numbers say: light vs heavy: width 28.7 → 53.1 px, dark 0.23 → 0.34; the long stroke does not run out of paint.

## Oil · Henry Ward · Thin veil
Oil 0.81 · Ink 0.19 · 96 px · 56.8 s

![Oil · Henry Ward · Thin veil](Oil-Henry-Ward-Thin-veil.png)

A light paint: laid on a grey sheet (on white it cannot be seen); **dark** = how far it is from the grey either way.

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 9 % → 4 % | 24.9 px | 0.06 | 0.51 | 294 |
| heavy line | 22 % → 20 % | 65.2 px | 0.26 | 0.89 | 506 |
| pressure swell | 20 % → 18 % | 73.8 px | 0.19 | 0.91 | 267 |
| fast wave | 59 % → 58 % | 68.4 px | 0.15 | 0.98 | 1103 |
| slow wave | 58 % → 51 % | 67.1 px | 0.18 | 0.89 | 1789 |
| spiral | 83 % → 67 % | 55.0 px | 0.17 | 0.80 | 2148 |
| loop | 57 % → 49 % | 74.0 px | 0.12 | 0.85 | 786 |
| tilted | 23 % → 23 % | 63.1 px | 0.18 | 1.01 | 570 |
| over the wet one | 36 % → 34 % | 38.7 px | 0.18 | 0.93 | 337 |
| long, no reload | 82 % → 70 % | 36.7 px | 0.15 | 0.85 | 2727 | quarters: 0.00 → 0.01 → 0.01 → 0.01

Numbers say: light vs heavy: width 24.9 → 65.2 px, dark 0.06 → 0.26; the long stroke does not run out of paint.

## Oil · Henry Ward · Ground
Gouache 1.00 · 160 px · 88.9 s

![Oil · Henry Ward · Ground](Oil-Henry-Ward-Ground.png)

A light paint: laid on a grey sheet (on white it cannot be seen); **dark** = how far it is from the grey either way.

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 51 % → 46 % | 148.3 px | 0.37 | 0.89 | 787 |
| heavy line | 52 % → 47 % | 151.5 px | 0.37 | 0.91 | 858 |
| pressure swell | 41 % → 45 % | 154.8 px | 0.36 | 1.10 | 633 |
| fast wave | 85 % → 86 % | 97.8 px | 0.36 | 1.01 | 2659 |
| slow wave | 86 % → 73 % | 99.2 px | 0.37 | 0.86 | 4151 |
| spiral | 88 % → 69 % | 58.3 px | 0.36 | 0.77 | 4663 |
| loop | 75 % → 69 % | 97.0 px | 0.37 | 0.92 | 2034 |
| tilted | 39 % → 39 % | 107.5 px | 0.37 | 1.00 | 1201 |
| over the wet one | 76 % → 71 % | 104.6 px | 0.37 | 0.93 | 1160 |
| long, no reload | 98 % → 87 % | 44.0 px | 0.37 | 0.88 | 7331 | quarters: 0.00 → 0.00 → 0.00 → 0.00

Numbers say: light vs heavy: width 148.3 → 151.5 px, dark 0.37 → 0.37; pressure barely changes the width.

## Oil · Henry Ward · HW #02 cream over wet olive
Oil 0.81 · Ink 0.19 · 96 px · 56.4 s

![Oil · Henry Ward · HW #02 cream over wet olive](Oil-Henry-Ward-HW-02-cream-over-wet-olive.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 9 % → 4 % | 24.9 px | 0.60 | 0.51 | 268 |
| heavy line | 22 % → 20 % | 65.2 px | 0.66 | 0.89 | 391 |
| pressure swell | 20 % → 18 % | 73.8 px | 0.64 | 0.91 | 281 |
| fast wave | 59 % → 58 % | 68.4 px | 0.69 | 0.98 | 1033 |
| slow wave | 58 % → 51 % | 67.1 px | 0.65 | 0.89 | 2121 |
| spiral | 83 % → 67 % | 55.0 px | 0.60 | 0.80 | 1769 |
| loop | 57 % → 49 % | 74.0 px | 0.60 | 0.85 | 822 |
| tilted | 23 % → 23 % | 63.1 px | 0.69 | 1.01 | 580 |
| over the wet one | 36 % → 34 % | 38.7 px | 0.69 | 0.93 | 327 |
| long, no reload | 82 % → 70 % | 36.7 px | 0.57 | 0.85 | 3146 | quarters: 0.57 → 0.50 → 0.41 → 0.25

Numbers say: light vs heavy: width 24.9 → 65.2 px, dark 0.60 → 0.66.

## Oil · Henry Ward · HW #04 grey arcs over ochre
Oil 1.00 · 84 px · 28.1 s

![Oil · Henry Ward · HW #04 grey arcs over ochre](Oil-Henry-Ward-HW-04-grey-arcs-over-ochre.png)

A light paint: laid on a grey sheet (on white it cannot be seen); **dark** = how far it is from the grey either way.

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 18 % → 20 % | 53.2 px | 0.22 | 1.06 | 271 |
| heavy line | 21 % → 21 % | 61.0 px | 0.26 | 1.00 | 285 |
| pressure swell | 20 % → 21 % | 76.0 px | 0.27 | 1.05 | 240 |
| fast wave | 52 % → 55 % | 60.6 px | 0.21 | 1.05 | 967 |
| slow wave | 55 % → 55 % | 63.3 px | 0.26 | 1.00 | 1660 |
| spiral | 75 % → 75 % | 49.5 px | 0.25 | 1.00 | 1598 |
| loop | 52 % → 52 % | 67.1 px | 0.26 | 1.00 | 885 |
| tilted | 21 % → 21 % | 58.4 px | 0.21 | 1.00 | 440 |
| over the wet one | 40 % → 40 % | 52.9 px | 0.21 | 1.00 | 396 |
| long, no reload | 78 % → 78 % | 35.2 px | 0.22 | 1.00 | 2969 | quarters: 0.00 → 0.00 → 0.00 → 0.00

Numbers say: light vs heavy: width 53.2 → 61.0 px, dark 0.22 → 0.26; the long stroke does not run out of paint.

## Oil · Henry Ward · HW #09 white arches over wet blue-grey
Oil 1.00 · 84 px · 29.2 s

![Oil · Henry Ward · HW #09 white arches over wet blue-grey](Oil-Henry-Ward-HW-09-white-arches-over-wet-blue-grey.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 18 % → 20 % | 53.2 px | 0.30 | 1.06 | 551 |
| heavy line | 21 % → 21 % | 61.0 px | 0.35 | 1.00 | 343 |
| pressure swell | 20 % → 21 % | 76.0 px | 0.34 | 1.05 | 287 |
| fast wave | 52 % → 55 % | 60.6 px | 0.42 | 1.05 | 937 |
| slow wave | 55 % → 55 % | 63.3 px | 0.35 | 1.00 | 1586 |
| spiral | 75 % → 75 % | 49.5 px | 0.30 | 1.00 | 1782 |
| loop | 52 % → 52 % | 67.1 px | 0.36 | 1.00 | 777 |
| tilted | 21 % → 21 % | 58.4 px | 0.41 | 1.00 | 648 |
| over the wet one | 40 % → 40 % | 52.9 px | 0.41 | 1.00 | 767 |
| long, no reload | 78 % → 78 % | 35.2 px | 0.35 | 1.00 | 2295 | quarters: 0.40 → 0.33 → 0.25 → 0.15

Numbers say: light vs heavy: width 53.2 → 61.0 px, dark 0.30 → 0.35.

## Oil · Henry Ward · HW #03 navy contours over wet band
Oil 1.00 · 84 px · 30.2 s

![Oil · Henry Ward · HW #03 navy contours over wet band](Oil-Henry-Ward-HW-03-navy-contours-over-wet-band.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 18 % → 20 % | 53.2 px | 0.32 | 1.06 | 295 |
| heavy line | 21 % → 21 % | 61.0 px | 0.37 | 1.00 | 308 |
| pressure swell | 20 % → 21 % | 76.0 px | 0.36 | 1.05 | 250 |
| fast wave | 52 % → 55 % | 60.6 px | 0.44 | 1.05 | 959 |
| slow wave | 55 % → 55 % | 63.3 px | 0.37 | 1.00 | 1688 |
| spiral | 75 % → 75 % | 49.5 px | 0.32 | 1.00 | 1566 |
| loop | 52 % → 52 % | 67.1 px | 0.38 | 1.00 | 1607 |
| tilted | 21 % → 21 % | 58.4 px | 0.43 | 1.00 | 517 |
| over the wet one | 40 % → 40 % | 52.9 px | 0.43 | 1.00 | 372 |
| long, no reload | 78 % → 78 % | 35.2 px | 0.37 | 1.00 | 2150 | quarters: 0.42 → 0.35 → 0.27 → 0.16

Numbers say: light vs heavy: width 53.2 → 61.0 px, dark 0.32 → 0.37.

## Oil · Henry Ward · HW #01 peach cloud and legs over teal
Oil 1.00 · 84 px · 30.7 s

![Oil · Henry Ward · HW #01 peach cloud and legs over teal](Oil-Henry-Ward-HW-01-peach-cloud-and-legs-over-teal.png)

A light paint: laid on a grey sheet (on white it cannot be seen); **dark** = how far it is from the grey either way.

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 18 % → 20 % | 53.2 px | 0.23 | 1.06 | 293 |
| heavy line | 21 % → 21 % | 61.0 px | 0.27 | 1.00 | 252 |
| pressure swell | 20 % → 21 % | 76.0 px | 0.27 | 1.05 | 200 |
| fast wave | 52 % → 55 % | 60.6 px | 0.22 | 1.05 | 827 |
| slow wave | 55 % → 55 % | 63.3 px | 0.27 | 1.00 | 1578 |
| spiral | 75 % → 75 % | 49.5 px | 0.25 | 1.00 | 1549 |
| loop | 52 % → 52 % | 67.1 px | 0.26 | 1.00 | 1298 |
| tilted | 21 % → 21 % | 58.4 px | 0.22 | 1.00 | 505 |
| over the wet one | 40 % → 40 % | 52.9 px | 0.22 | 1.00 | 359 |
| long, no reload | 78 % → 78 % | 35.2 px | 0.22 | 1.00 | 2255 | quarters: 0.00 → 0.00 → 0.00 → 0.00

Numbers say: light vs heavy: width 53.2 → 61.0 px, dark 0.23 → 0.27; the long stroke does not run out of paint.

## Oil · Henry Ward · HW #05 rust, pink, green-black
Oil 1.00 · 84 px · 36.9 s

![Oil · Henry Ward · HW #05 rust, pink, green-black](Oil-Henry-Ward-HW-05-rust-pink-green-black.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 18 % → 20 % | 53.2 px | 0.53 | 1.06 | 293 |
| heavy line | 21 % → 21 % | 61.0 px | 0.57 | 1.00 | 316 |
| pressure swell | 20 % → 21 % | 76.0 px | 0.56 | 1.05 | 202 |
| fast wave | 52 % → 55 % | 60.6 px | 0.62 | 1.05 | 1671 |
| slow wave | 55 % → 55 % | 63.3 px | 0.58 | 1.00 | 1676 |
| spiral | 75 % → 75 % | 49.5 px | 0.53 | 1.00 | 1630 |
| loop | 52 % → 52 % | 67.1 px | 0.58 | 1.00 | 855 |
| tilted | 21 % → 21 % | 58.4 px | 0.60 | 1.00 | 539 |
| over the wet one | 40 % → 40 % | 52.9 px | 0.60 | 1.00 | 388 |
| long, no reload | 78 % → 78 % | 35.2 px | 0.57 | 1.00 | 2476 | quarters: 0.60 → 0.53 → 0.44 → 0.29

Numbers say: light vs heavy: width 53.2 → 61.0 px, dark 0.53 → 0.57.

## Oil · Henry Ward · HW #07 blue L and zigzag on lilac
Oil 1.00 · 90 px · 29.1 s

![Oil · Henry Ward · HW #07 blue L and zigzag on lilac](Oil-Henry-Ward-HW-07-blue-L-and-zigzag-on-lilac.png)

A light paint: laid on a grey sheet (on white it cannot be seen); **dark** = how far it is from the grey either way.

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 8 % → 9 % | 21.9 px | 0.21 | 1.21 | 280 |
| heavy line | 14 % → 14 % | 42.1 px | 0.30 | 1.00 | 363 |
| pressure swell | 14 % → 15 % | 51.7 px | 0.28 | 1.09 | 232 |
| fast wave | 51 % → 53 % | 58.7 px | 0.32 | 1.04 | 1098 |
| slow wave | 37 % → 37 % | 42.2 px | 0.31 | 1.00 | 1600 |
| spiral | 70 % → 70 % | 46.0 px | 0.25 | 1.00 | 1615 |
| loop | 36 % → 36 % | 46.7 px | 0.26 | 1.00 | 917 |
| tilted | 21 % → 21 % | 57.5 px | 0.25 | 1.00 | 438 |
| over the wet one | 29 % → 29 % | 22.2 px | 0.25 | 1.00 | 339 |
| long, no reload | 49 % → 49 % | 22.1 px | 0.26 | 1.00 | 2237 | quarters: 0.00 → 0.00 → 0.00 → 0.00

Numbers say: light vs heavy: width 21.9 → 42.1 px, dark 0.21 → 0.30.

## Oil · Henry Ward · HW #08 crown and dark oval
Oil 1.00 · 84 px · 36.7 s

![Oil · Henry Ward · HW #08 crown and dark oval](Oil-Henry-Ward-HW-08-crown-and-dark-oval.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 18 % → 20 % | 53.2 px | 0.19 | 1.06 | 338 |
| heavy line | 21 % → 21 % | 61.0 px | 0.24 | 1.00 | 416 |
| pressure swell | 20 % → 21 % | 76.0 px | 0.22 | 1.05 | 305 |
| fast wave | 52 % → 55 % | 60.6 px | 0.30 | 1.05 | 997 |
| slow wave | 55 % → 55 % | 63.3 px | 0.23 | 1.00 | 1659 |
| spiral | 75 % → 75 % | 49.5 px | 0.19 | 1.00 | 1955 |
| loop | 52 % → 52 % | 67.1 px | 0.23 | 1.00 | 1117 |
| tilted | 21 % → 21 % | 58.4 px | 0.30 | 1.00 | 587 |
| over the wet one | 40 % → 40 % | 52.9 px | 0.30 | 1.00 | 379 |
| long, no reload | 78 % → 78 % | 35.2 px | 0.23 | 1.00 | 2674 | quarters: 0.27 → 0.22 → 0.16 → 0.10

Numbers say: light vs heavy: width 53.2 → 61.0 px, dark 0.19 → 0.24.

## Oil · Henry Ward · HW #10 green block over maroon
Oil 1.00 · 84 px · 34.4 s

![Oil · Henry Ward · HW #10 green block over maroon](Oil-Henry-Ward-HW-10-green-block-over-maroon.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 18 % → 20 % | 53.2 px | 0.17 | 1.06 | 319 |
| heavy line | 21 % → 21 % | 61.0 px | 0.21 | 1.00 | 345 |
| pressure swell | 20 % → 21 % | 76.0 px | 0.19 | 1.05 | 351 |
| fast wave | 52 % → 55 % | 60.6 px | 0.27 | 1.05 | 1422 |
| slow wave | 55 % → 55 % | 63.3 px | 0.20 | 1.00 | 4886 |
| spiral | 75 % → 75 % | 49.5 px | 0.17 | 1.00 | 2360 |
| loop | 52 % → 52 % | 67.1 px | 0.21 | 1.00 | 1334 |
| tilted | 21 % → 21 % | 58.4 px | 0.27 | 1.00 | 642 |
| over the wet one | 40 % → 40 % | 52.9 px | 0.27 | 1.00 | 406 |
| long, no reload | 78 % → 78 % | 35.2 px | 0.21 | 1.00 | 2123 | quarters: 0.25 → 0.20 → 0.15 → 0.09

Numbers say: light vs heavy: width 53.2 → 61.0 px, dark 0.17 → 0.21.

## Oil · Henry Ward · HW #11 cream mass and purple balls
Oil 1.00 · 84 px · 34.9 s

![Oil · Henry Ward · HW #11 cream mass and purple balls](Oil-Henry-Ward-HW-11-cream-mass-and-purple-balls.png)

A light paint: laid on a grey sheet (on white it cannot be seen); **dark** = how far it is from the grey either way.

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 18 % → 20 % | 53.2 px | 0.29 | 1.06 | 385 |
| heavy line | 21 % → 21 % | 61.0 px | 0.34 | 1.00 | 564 |
| pressure swell | 20 % → 21 % | 76.0 px | 0.33 | 1.05 | 774 |
| fast wave | 52 % → 55 % | 60.6 px | 0.29 | 1.05 | 3380 |
| slow wave | 55 % → 55 % | 63.3 px | 0.33 | 1.00 | 2677 |
| spiral | 75 % → 75 % | 49.5 px | 0.30 | 1.00 | 2972 |
| loop | 52 % → 52 % | 67.1 px | 0.33 | 1.00 | 902 |
| tilted | 21 % → 21 % | 58.4 px | 0.29 | 1.00 | 447 |
| over the wet one | 40 % → 40 % | 52.9 px | 0.29 | 1.00 | 319 |
| long, no reload | 78 % → 78 % | 35.2 px | 0.28 | 1.00 | 2055 | quarters: 0.00 → 0.00 → 0.00 → 0.00

Numbers say: light vs heavy: width 53.2 → 61.0 px, dark 0.29 → 0.34; the long stroke does not run out of paint.

## Oil · Henry Ward · HW #13 blue scrub under red
Oil 1.00 · 84 px · 33.1 s

![Oil · Henry Ward · HW #13 blue scrub under red](Oil-Henry-Ward-HW-13-blue-scrub-under-red.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 18 % → 20 % | 53.2 px | 0.61 | 1.06 | 784 |
| heavy line | 21 % → 21 % | 61.0 px | 0.65 | 1.00 | 1489 |
| pressure swell | 20 % → 21 % | 76.0 px | 0.64 | 1.05 | 521 |
| fast wave | 52 % → 55 % | 60.6 px | 0.69 | 1.05 | 1787 |
| slow wave | 55 % → 55 % | 63.3 px | 0.66 | 1.00 | 2288 |
| spiral | 75 % → 75 % | 49.5 px | 0.62 | 1.00 | 2603 |
| loop | 52 % → 52 % | 67.1 px | 0.67 | 1.00 | 746 |
| tilted | 21 % → 21 % | 58.4 px | 0.68 | 1.00 | 451 |
| over the wet one | 40 % → 40 % | 52.9 px | 0.68 | 1.00 | 348 |
| long, no reload | 78 % → 78 % | 35.2 px | 0.66 | 1.00 | 2050 | quarters: 0.67 → 0.61 → 0.50 → 0.34

Numbers say: light vs heavy: width 53.2 → 61.0 px, dark 0.61 → 0.65.

## Oil · Henry Ward · HW #14 olive totem on dark
Oil 1.00 · 84 px · 34.8 s

![Oil · Henry Ward · HW #14 olive totem on dark](Oil-Henry-Ward-HW-14-olive-totem-on-dark.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 18 % → 20 % | 53.2 px | 0.25 | 1.06 | 767 |
| heavy line | 21 % → 21 % | 61.0 px | 0.30 | 1.00 | 1163 |
| pressure swell | 20 % → 21 % | 76.0 px | 0.29 | 1.05 | 622 |
| fast wave | 52 % → 55 % | 60.6 px | 0.36 | 1.05 | 1257 |
| slow wave | 55 % → 55 % | 63.3 px | 0.30 | 1.00 | 2382 |
| spiral | 75 % → 75 % | 49.5 px | 0.25 | 1.00 | 1928 |
| loop | 52 % → 52 % | 67.1 px | 0.31 | 1.00 | 741 |
| tilted | 21 % → 21 % | 58.4 px | 0.36 | 1.00 | 420 |
| over the wet one | 40 % → 40 % | 52.9 px | 0.36 | 1.00 | 376 |
| long, no reload | 78 % → 78 % | 35.2 px | 0.30 | 1.00 | 2238 | quarters: 0.34 → 0.28 → 0.21 → 0.13

Numbers say: light vs heavy: width 53.2 → 61.0 px, dark 0.25 → 0.30.

## Oil · Henry Ward · Ground #2b2f1c
Gouache 1.00 · 160 px · 83.4 s

![Oil · Henry Ward · Ground #2b2f1c](Oil-Henry-Ward-Ground-2b2f1c.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 51 % → 46 % | 148.3 px | 0.52 | 0.89 | 1166 |
| heavy line | 52 % → 47 % | 151.5 px | 0.52 | 0.91 | 1048 |
| pressure swell | 41 % → 45 % | 154.8 px | 0.52 | 1.10 | 574 |
| fast wave | 85 % → 86 % | 97.8 px | 0.52 | 1.01 | 2218 |
| slow wave | 86 % → 73 % | 99.2 px | 0.52 | 0.86 | 4267 |
| spiral | 88 % → 69 % | 58.3 px | 0.52 | 0.77 | 3613 |
| loop | 75 % → 69 % | 97.0 px | 0.52 | 0.92 | 2527 |
| tilted | 39 % → 39 % | 107.5 px | 0.52 | 1.00 | 1746 |
| over the wet one | 76 % → 71 % | 104.6 px | 0.52 | 0.93 | 1360 |
| long, no reload | 98 % → 87 % | 44.0 px | 0.52 | 0.88 | 5587 | quarters: 0.52 → 0.52 → 0.52 → 0.50

Numbers say: light vs heavy: width 148.3 → 151.5 px, dark 0.52 → 0.52; pressure barely changes the width; the long stroke does not run out of paint.

## Oil · Henry Ward · Thin veil #2b3a44
Oil 0.81 · Ink 0.19 · 96 px · 49.6 s

![Oil · Henry Ward · Thin veil #2b3a44](Oil-Henry-Ward-Thin-veil-2b3a44.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 9 % → 4 % | 24.9 px | 0.60 | 0.51 | 409 |
| heavy line | 22 % → 20 % | 65.2 px | 0.66 | 0.89 | 422 |
| pressure swell | 20 % → 18 % | 73.8 px | 0.64 | 0.91 | 266 |
| fast wave | 59 % → 58 % | 68.4 px | 0.69 | 0.98 | 1024 |
| slow wave | 58 % → 51 % | 67.1 px | 0.65 | 0.89 | 1625 |
| spiral | 83 % → 67 % | 55.0 px | 0.60 | 0.80 | 2030 |
| loop | 57 % → 49 % | 74.0 px | 0.60 | 0.85 | 853 |
| tilted | 23 % → 23 % | 63.1 px | 0.69 | 1.01 | 551 |
| over the wet one | 36 % → 34 % | 38.7 px | 0.69 | 0.93 | 348 |
| long, no reload | 82 % → 70 % | 36.7 px | 0.57 | 0.85 | 2703 | quarters: 0.57 → 0.50 → 0.41 → 0.25

Numbers say: light vs heavy: width 24.9 → 65.2 px, dark 0.60 → 0.66.

## Oil · Henry Ward · Loaded flat #ece6c0
Oil 1.00 · 84 px · 29.4 s

![Oil · Henry Ward · Loaded flat #ece6c0](Oil-Henry-Ward-Loaded-flat-ece6c0.png)

A light paint: laid on a grey sheet (on white it cannot be seen); **dark** = how far it is from the grey either way.

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 18 % → 20 % | 53.2 px | 0.31 | 1.06 | 285 |
| heavy line | 21 % → 21 % | 61.0 px | 0.37 | 1.00 | 307 |
| pressure swell | 20 % → 21 % | 76.0 px | 0.36 | 1.05 | 250 |
| fast wave | 52 % → 55 % | 60.6 px | 0.32 | 1.05 | 1004 |
| slow wave | 55 % → 55 % | 63.3 px | 0.36 | 1.00 | 1683 |
| spiral | 75 % → 75 % | 49.5 px | 0.32 | 1.00 | 1580 |
| loop | 52 % → 52 % | 67.1 px | 0.36 | 1.00 | 791 |
| tilted | 21 % → 21 % | 58.4 px | 0.32 | 1.00 | 513 |
| over the wet one | 40 % → 40 % | 52.9 px | 0.32 | 1.00 | 410 |
| long, no reload | 78 % → 78 % | 35.2 px | 0.31 | 1.00 | 2954 | quarters: 0.00 → 0.00 → 0.00 → 0.00

Numbers say: light vs heavy: width 53.2 → 61.0 px, dark 0.31 → 0.37; the long stroke does not run out of paint.

## Oil · Henry Ward · Dry scrub #ece6c0
Oil 1.00 · 90 px · 23.9 s

![Oil · Henry Ward · Dry scrub #ece6c0](Oil-Henry-Ward-Dry-scrub-ece6c0.png)

A light paint: laid on a grey sheet (on white it cannot be seen); **dark** = how far it is from the grey either way.

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 8 % → 9 % | 21.9 px | 0.19 | 1.21 | 284 |
| heavy line | 14 % → 14 % | 42.1 px | 0.27 | 1.00 | 372 |
| pressure swell | 14 % → 15 % | 51.7 px | 0.25 | 1.09 | 216 |
| fast wave | 51 % → 53 % | 58.7 px | 0.29 | 1.04 | 1052 |
| slow wave | 37 % → 37 % | 42.2 px | 0.29 | 1.00 | 1452 |
| spiral | 70 % → 70 % | 46.0 px | 0.23 | 1.00 | 1517 |
| loop | 36 % → 36 % | 46.7 px | 0.24 | 1.00 | 881 |
| tilted | 21 % → 21 % | 57.5 px | 0.22 | 1.00 | 485 |
| over the wet one | 29 % → 29 % | 22.2 px | 0.22 | 1.00 | 242 |
| long, no reload | 49 % → 49 % | 22.1 px | 0.24 | 1.00 | 1915 | quarters: 0.00 → 0.00 → 0.00 → 0.00

Numbers say: light vs heavy: width 21.9 → 42.1 px, dark 0.19 → 0.27.

## Oil · Henry Ward · Ground #8a6a20
Gouache 1.00 · 160 px · 82.0 s

![Oil · Henry Ward · Ground #8a6a20](Oil-Henry-Ward-Ground-8a6a20.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 51 % → 46 % | 148.3 px | 0.32 | 0.89 | 738 |
| heavy line | 52 % → 47 % | 151.5 px | 0.32 | 0.91 | 860 |
| pressure swell | 41 % → 45 % | 154.8 px | 0.32 | 1.10 | 643 |
| fast wave | 85 % → 86 % | 97.8 px | 0.33 | 1.01 | 2373 |
| slow wave | 86 % → 73 % | 99.2 px | 0.32 | 0.86 | 5064 |
| spiral | 88 % → 69 % | 58.3 px | 0.32 | 0.77 | 5453 |
| loop | 75 % → 69 % | 97.0 px | 0.32 | 0.92 | 1998 |
| tilted | 39 % → 39 % | 107.5 px | 0.32 | 1.00 | 1035 |
| over the wet one | 76 % → 71 % | 104.6 px | 0.32 | 0.93 | 889 |
| long, no reload | 98 % → 87 % | 44.0 px | 0.32 | 0.88 | 6472 | quarters: 0.32 → 0.32 → 0.32 → 0.29

Numbers say: light vs heavy: width 148.3 → 151.5 px, dark 0.32 → 0.32; pressure barely changes the width; the long stroke does not run out of paint.

## Oil · Henry Ward · Loaded flat #b8bcc0
Oil 1.00 · 84 px · 30.2 s

![Oil · Henry Ward · Loaded flat #b8bcc0](Oil-Henry-Ward-Loaded-flat-b8bcc0.png)

A light paint: laid on a grey sheet (on white it cannot be seen); **dark** = how far it is from the grey either way.

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 18 % → 20 % | 53.2 px | 0.22 | 1.06 | 420 |
| heavy line | 21 % → 21 % | 61.0 px | 0.26 | 1.00 | 425 |
| pressure swell | 20 % → 21 % | 76.0 px | 0.27 | 1.05 | 285 |
| fast wave | 52 % → 55 % | 60.6 px | 0.21 | 1.05 | 1372 |
| slow wave | 55 % → 55 % | 63.3 px | 0.26 | 1.00 | 2128 |
| spiral | 75 % → 75 % | 49.5 px | 0.25 | 1.00 | 2507 |
| loop | 52 % → 52 % | 67.1 px | 0.26 | 1.00 | 1049 |
| tilted | 21 % → 21 % | 58.4 px | 0.21 | 1.00 | 653 |
| over the wet one | 40 % → 40 % | 52.9 px | 0.21 | 1.00 | 461 |
| long, no reload | 78 % → 78 % | 35.2 px | 0.22 | 1.00 | 1970 | quarters: 0.00 → 0.00 → 0.00 → 0.00

Numbers say: light vs heavy: width 53.2 → 61.0 px, dark 0.22 → 0.26; the long stroke does not run out of paint.

## Oil · Henry Ward · Dry scrub #c8ccd0
Oil 1.00 · 90 px · 24.4 s

![Oil · Henry Ward · Dry scrub #c8ccd0](Oil-Henry-Ward-Dry-scrub-c8ccd0.png)

A light paint: laid on a grey sheet (on white it cannot be seen); **dark** = how far it is from the grey either way.

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 8 % → 9 % | 21.9 px | 0.15 | 1.21 | 300 |
| heavy line | 14 % → 14 % | 42.1 px | 0.22 | 1.00 | 545 |
| pressure swell | 14 % → 15 % | 51.7 px | 0.20 | 1.09 | 352 |
| fast wave | 51 % → 53 % | 58.7 px | 0.23 | 1.04 | 1247 |
| slow wave | 37 % → 37 % | 42.2 px | 0.24 | 1.00 | 2511 |
| spiral | 70 % → 70 % | 46.0 px | 0.19 | 1.00 | 2024 |
| loop | 36 % → 36 % | 46.7 px | 0.19 | 1.00 | 876 |
| tilted | 21 % → 21 % | 57.5 px | 0.17 | 1.00 | 437 |
| over the wet one | 29 % → 29 % | 22.2 px | 0.17 | 1.00 | 374 |
| long, no reload | 49 % → 49 % | 22.1 px | 0.20 | 1.00 | 1725 | quarters: 0.00 → 0.00 → 0.00 → 0.00

Numbers say: light vs heavy: width 21.9 → 42.1 px, dark 0.15 → 0.22.

## Oil · Henry Ward · Wet drag #9ea4aa
Oil 1.00 · 80 px · 26.9 s

![Oil · Henry Ward · Wet drag #9ea4aa](Oil-Henry-Ward-Wet-drag-9ea4aa.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 10 % → 10 % | 28.7 px | 0.14 | 1.03 | 343 |
| heavy line | 18 % → 18 % | 53.1 px | 0.22 | 1.00 | 447 |
| pressure swell | 17 % → 17 % | 62.6 px | 0.16 | 1.04 | 268 |
| fast wave | 48 % → 50 % | 55.6 px | 0.24 | 1.04 | 1409 |
| slow wave | 53 % → 53 % | 61.7 px | 0.21 | 1.00 | 2000 |
| spiral | 71 % → 71 % | 46.6 px | 0.17 | 1.00 | 1893 |
| loop | 38 % → 38 % | 49.4 px | 0.15 | 1.00 | 586 |
| tilted | 19 % → 19 % | 52.3 px | 0.27 | 1.00 | 415 |
| over the wet one | 36 % → 36 % | 48.7 px | 0.27 | 1.00 | 325 |
| long, no reload | 78 % → 78 % | 34.8 px | 0.17 | 1.00 | 1884 | quarters: 0.19 → 0.17 → 0.14 → 0.05

Numbers say: light vs heavy: width 28.7 → 53.1 px, dark 0.14 → 0.22.

## Oil · Henry Ward · Ground #e8b4a8
Gouache 1.00 · 160 px · 91.2 s

![Oil · Henry Ward · Ground #e8b4a8](Oil-Henry-Ward-Ground-e8b4a8.png)

A light paint: laid on a grey sheet (on white it cannot be seen); **dark** = how far it is from the grey either way.

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 51 % → 46 % | 148.3 px | 0.30 | 0.89 | 1364 |
| heavy line | 52 % → 47 % | 151.5 px | 0.30 | 0.91 | 1035 |
| pressure swell | 41 % → 45 % | 154.8 px | 0.30 | 1.10 | 800 |
| fast wave | 85 % → 86 % | 97.8 px | 0.29 | 1.01 | 2142 |
| slow wave | 86 % → 73 % | 99.2 px | 0.30 | 0.86 | 4630 |
| spiral | 88 % → 69 % | 58.3 px | 0.30 | 0.77 | 4229 |
| loop | 75 % → 69 % | 97.0 px | 0.30 | 0.92 | 1949 |
| tilted | 39 % → 39 % | 107.5 px | 0.30 | 1.00 | 1098 |
| over the wet one | 76 % → 71 % | 104.6 px | 0.30 | 0.93 | 895 |
| long, no reload | 98 % → 87 % | 44.0 px | 0.30 | 0.88 | 7219 | quarters: 0.00 → 0.00 → 0.00 → 0.00

Numbers say: light vs heavy: width 148.3 → 151.5 px, dark 0.30 → 0.30; pressure barely changes the width.

## Oil · Henry Ward · Loaded flat #6e7f90
Oil 1.00 · 84 px · 27.2 s

![Oil · Henry Ward · Loaded flat #6e7f90](Oil-Henry-Ward-Loaded-flat-6e7f90.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 18 % → 20 % | 53.2 px | 0.30 | 1.06 | 404 |
| heavy line | 21 % → 21 % | 61.0 px | 0.35 | 1.00 | 339 |
| pressure swell | 20 % → 21 % | 76.0 px | 0.34 | 1.05 | 260 |
| fast wave | 52 % → 55 % | 60.6 px | 0.42 | 1.05 | 847 |
| slow wave | 55 % → 55 % | 63.3 px | 0.35 | 1.00 | 1445 |
| spiral | 75 % → 75 % | 49.5 px | 0.30 | 1.00 | 1526 |
| loop | 52 % → 52 % | 67.1 px | 0.36 | 1.00 | 943 |
| tilted | 21 % → 21 % | 58.4 px | 0.41 | 1.00 | 541 |
| over the wet one | 40 % → 40 % | 52.9 px | 0.41 | 1.00 | 395 |
| long, no reload | 78 % → 78 % | 35.2 px | 0.35 | 1.00 | 2402 | quarters: 0.40 → 0.33 → 0.25 → 0.15

Numbers say: light vs heavy: width 53.2 → 61.0 px, dark 0.30 → 0.35.

## Oil · Henry Ward · Loaded flat #f6f6f2
Oil 1.00 · 84 px · 28.1 s

![Oil · Henry Ward · Loaded flat #f6f6f2](Oil-Henry-Ward-Loaded-flat-f6f6f2.png)

A light paint: laid on a grey sheet (on white it cannot be seen); **dark** = how far it is from the grey either way.

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 18 % → 20 % | 53.2 px | 0.34 | 1.06 | 278 |
| heavy line | 21 % → 21 % | 61.0 px | 0.41 | 1.00 | 295 |
| pressure swell | 20 % → 21 % | 76.0 px | 0.39 | 1.05 | 237 |
| fast wave | 52 % → 55 % | 60.6 px | 0.36 | 1.05 | 1469 |
| slow wave | 55 % → 55 % | 63.3 px | 0.40 | 1.00 | 1649 |
| spiral | 75 % → 75 % | 49.5 px | 0.35 | 1.00 | 1855 |
| loop | 52 % → 52 % | 67.1 px | 0.40 | 1.00 | 991 |
| tilted | 21 % → 21 % | 58.4 px | 0.36 | 1.00 | 478 |
| over the wet one | 40 % → 40 % | 52.9 px | 0.36 | 1.00 | 381 |
| long, no reload | 78 % → 78 % | 35.2 px | 0.35 | 1.00 | 2409 | quarters: 0.00 → 0.00 → 0.00 → 0.00

Numbers say: light vs heavy: width 53.2 → 61.0 px, dark 0.34 → 0.41; the long stroke does not run out of paint.

## Oil · Henry Ward · Dry scrub #f6f6f2
Oil 1.00 · 90 px · 21.5 s

![Oil · Henry Ward · Dry scrub #f6f6f2](Oil-Henry-Ward-Dry-scrub-f6f6f2.png)

A light paint: laid on a grey sheet (on white it cannot be seen); **dark** = how far it is from the grey either way.

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 8 % → 9 % | 21.9 px | 0.22 | 1.21 | 322 |
| heavy line | 14 % → 14 % | 42.1 px | 0.31 | 1.00 | 386 |
| pressure swell | 14 % → 15 % | 51.7 px | 0.28 | 1.09 | 209 |
| fast wave | 51 % → 53 % | 58.7 px | 0.33 | 1.04 | 979 |
| slow wave | 37 % → 37 % | 42.2 px | 0.32 | 1.00 | 1561 |
| spiral | 70 % → 70 % | 46.0 px | 0.26 | 1.00 | 1509 |
| loop | 36 % → 36 % | 46.7 px | 0.27 | 1.00 | 823 |
| tilted | 21 % → 21 % | 57.5 px | 0.26 | 1.00 | 529 |
| over the wet one | 29 % → 29 % | 22.2 px | 0.26 | 1.00 | 231 |
| long, no reload | 49 % → 49 % | 22.1 px | 0.26 | 1.00 | 2029 | quarters: 0.00 → 0.00 → 0.00 → 0.00

Numbers say: light vs heavy: width 21.9 → 42.1 px, dark 0.22 → 0.31.

## Oil · Henry Ward · Ground #e8e2da
Gouache 1.00 · 160 px · 90.6 s

![Oil · Henry Ward · Ground #e8e2da](Oil-Henry-Ward-Ground-e8e2da.png)

A light paint: laid on a grey sheet (on white it cannot be seen); **dark** = how far it is from the grey either way.

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 51 % → 46 % | 148.3 px | 0.38 | 0.89 | 734 |
| heavy line | 52 % → 47 % | 151.5 px | 0.38 | 0.91 | 904 |
| pressure swell | 41 % → 45 % | 154.8 px | 0.38 | 1.10 | 712 |
| fast wave | 85 % → 86 % | 97.8 px | 0.37 | 1.01 | 2323 |
| slow wave | 86 % → 73 % | 99.2 px | 0.38 | 0.86 | 5233 |
| spiral | 88 % → 69 % | 58.3 px | 0.38 | 0.77 | 4224 |
| loop | 75 % → 69 % | 97.0 px | 0.38 | 0.92 | 2746 |
| tilted | 39 % → 39 % | 107.5 px | 0.38 | 1.00 | 1235 |
| over the wet one | 76 % → 71 % | 104.6 px | 0.38 | 0.93 | 871 |
| long, no reload | 98 % → 87 % | 44.0 px | 0.38 | 0.88 | 5884 | quarters: 0.00 → 0.00 → 0.00 → 0.00

Numbers say: light vs heavy: width 148.3 → 151.5 px, dark 0.38 → 0.38; pressure barely changes the width.

## Oil · Henry Ward · Loaded flat #6a7a80
Oil 1.00 · 84 px · 29.3 s

![Oil · Henry Ward · Loaded flat #6a7a80](Oil-Henry-Ward-Loaded-flat-6a7a80.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 18 % → 20 % | 53.2 px | 0.32 | 1.06 | 351 |
| heavy line | 21 % → 21 % | 61.0 px | 0.37 | 1.00 | 415 |
| pressure swell | 20 % → 21 % | 76.0 px | 0.36 | 1.05 | 270 |
| fast wave | 52 % → 55 % | 60.6 px | 0.44 | 1.05 | 870 |
| slow wave | 55 % → 55 % | 63.3 px | 0.37 | 1.00 | 1525 |
| spiral | 75 % → 75 % | 49.5 px | 0.32 | 1.00 | 1988 |
| loop | 52 % → 52 % | 67.1 px | 0.38 | 1.00 | 1016 |
| tilted | 21 % → 21 % | 58.4 px | 0.43 | 1.00 | 613 |
| over the wet one | 40 % → 40 % | 52.9 px | 0.43 | 1.00 | 486 |
| long, no reload | 78 % → 78 % | 35.2 px | 0.37 | 1.00 | 2432 | quarters: 0.42 → 0.35 → 0.27 → 0.16

Numbers say: light vs heavy: width 53.2 → 61.0 px, dark 0.32 → 0.37.

## Oil · Henry Ward · Loaded flat #5a1810
Oil 1.00 · 84 px · 29.1 s

![Oil · Henry Ward · Loaded flat #5a1810](Oil-Henry-Ward-Loaded-flat-5a1810.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 18 % → 20 % | 53.2 px | 0.70 | 1.06 | 386 |
| heavy line | 21 % → 21 % | 61.0 px | 0.73 | 1.00 | 343 |
| pressure swell | 20 % → 21 % | 76.0 px | 0.72 | 1.05 | 229 |
| fast wave | 52 % → 55 % | 60.6 px | 0.77 | 1.05 | 899 |
| slow wave | 55 % → 55 % | 63.3 px | 0.75 | 1.00 | 1506 |
| spiral | 75 % → 75 % | 49.5 px | 0.70 | 1.00 | 2024 |
| loop | 52 % → 52 % | 67.1 px | 0.75 | 1.00 | 1005 |
| tilted | 21 % → 21 % | 58.4 px | 0.75 | 1.00 | 614 |
| over the wet one | 40 % → 40 % | 52.9 px | 0.75 | 1.00 | 548 |
| long, no reload | 78 % → 78 % | 35.2 px | 0.74 | 1.00 | 2319 | quarters: 0.75 → 0.69 → 0.58 → 0.39

Numbers say: light vs heavy: width 53.2 → 61.0 px, dark 0.70 → 0.73.

## Oil · Henry Ward · Dirty contour #1c2240
Oil 1.00 · 34 px · 16.6 s

![Oil · Henry Ward · Dirty contour #1c2240](Oil-Henry-Ward-Dirty-contour-1c2240.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 7 % → 7 % | 20.6 px | 0.72 | 1.00 | 107 |
| heavy line | 12 % → 12 % | 34.2 px | 0.74 | 1.00 | 141 |
| pressure swell | 9 % → 9 % | 35.2 px | 0.78 | 1.00 | 116 |
| fast wave | 28 % → 28 % | 32.5 px | 0.76 | 1.00 | 346 |
| slow wave | 31 % → 31 % | 35.2 px | 0.77 | 1.00 | 643 |
| spiral | 42 % → 42 % | 27.5 px | 0.74 | 1.00 | 679 |
| loop | 25 % → 25 % | 32.4 px | 0.76 | 1.00 | 312 |
| tilted | 12 % → 12 % | 32.3 px | 0.78 | 1.00 | 287 |
| over the wet one | 23 % → 23 % | 32.0 px | 0.78 | 1.00 | 161 |
| long, no reload | 50 % → 50 % | 22.6 px | 0.72 | 1.00 | 1144 | quarters: 0.50 → 0.44 → 0.34 → 0.33

Numbers say: light vs heavy: width 20.6 → 34.2 px, dark 0.72 → 0.74.

## Oil · Henry Ward · Ground #22403f
Gouache 1.00 · 160 px · 90.6 s

![Oil · Henry Ward · Ground #22403f](Oil-Henry-Ward-Ground-22403f.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 51 % → 46 % | 148.3 px | 0.48 | 0.89 | 952 |
| heavy line | 52 % → 47 % | 151.5 px | 0.48 | 0.91 | 1112 |
| pressure swell | 41 % → 45 % | 154.8 px | 0.48 | 1.10 | 754 |
| fast wave | 85 % → 86 % | 97.8 px | 0.48 | 1.01 | 2810 |
| slow wave | 86 % → 73 % | 99.2 px | 0.48 | 0.86 | 5797 |
| spiral | 88 % → 69 % | 58.3 px | 0.48 | 0.77 | 3906 |
| loop | 75 % → 69 % | 97.0 px | 0.48 | 0.92 | 2092 |
| tilted | 39 % → 39 % | 107.5 px | 0.48 | 1.00 | 1130 |
| over the wet one | 76 % → 71 % | 104.6 px | 0.48 | 0.93 | 1013 |
| long, no reload | 98 % → 87 % | 44.0 px | 0.48 | 0.88 | 10446 | quarters: 0.48 → 0.48 → 0.48 → 0.46

Numbers say: light vs heavy: width 148.3 → 151.5 px, dark 0.48 → 0.48; pressure barely changes the width; the long stroke does not run out of paint.

## Oil · Henry Ward · Loaded flat #f0b89a
Oil 1.00 · 84 px · 29.0 s

![Oil · Henry Ward · Loaded flat #f0b89a](Oil-Henry-Ward-Loaded-flat-f0b89a.png)

A light paint: laid on a grey sheet (on white it cannot be seen); **dark** = how far it is from the grey either way.

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 18 % → 20 % | 53.2 px | 0.23 | 1.06 | 295 |
| heavy line | 21 % → 21 % | 61.0 px | 0.27 | 1.00 | 360 |
| pressure swell | 20 % → 21 % | 76.0 px | 0.27 | 1.05 | 263 |
| fast wave | 52 % → 55 % | 60.6 px | 0.22 | 1.05 | 915 |
| slow wave | 55 % → 55 % | 63.3 px | 0.27 | 1.00 | 1790 |
| spiral | 75 % → 75 % | 49.5 px | 0.25 | 1.00 | 2258 |
| loop | 52 % → 52 % | 67.1 px | 0.26 | 1.00 | 1720 |
| tilted | 21 % → 21 % | 58.4 px | 0.22 | 1.00 | 565 |
| over the wet one | 40 % → 40 % | 52.9 px | 0.22 | 1.00 | 392 |
| long, no reload | 78 % → 78 % | 35.2 px | 0.22 | 1.00 | 2015 | quarters: 0.00 → 0.00 → 0.00 → 0.00

Numbers say: light vs heavy: width 53.2 → 61.0 px, dark 0.23 → 0.27; the long stroke does not run out of paint.

## Oil · Henry Ward · Dry scrub #f0b89a
Oil 1.00 · 90 px · 23.3 s

![Oil · Henry Ward · Dry scrub #f0b89a](Oil-Henry-Ward-Dry-scrub-f0b89a.png)

A light paint: laid on a grey sheet (on white it cannot be seen); **dark** = how far it is from the grey either way.

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 8 % → 9 % | 21.9 px | 0.13 | 1.21 | 290 |
| heavy line | 14 % → 14 % | 42.1 px | 0.19 | 1.00 | 424 |
| pressure swell | 14 % → 15 % | 51.7 px | 0.18 | 1.09 | 243 |
| fast wave | 51 % → 53 % | 58.7 px | 0.20 | 1.04 | 1233 |
| slow wave | 37 % → 37 % | 42.2 px | 0.21 | 1.00 | 2174 |
| spiral | 70 % → 70 % | 46.0 px | 0.17 | 1.00 | 2243 |
| loop | 36 % → 36 % | 46.7 px | 0.17 | 1.00 | 711 |
| tilted | 21 % → 21 % | 57.5 px | 0.14 | 1.00 | 449 |
| over the wet one | 29 % → 29 % | 22.2 px | 0.14 | 1.00 | 269 |
| long, no reload | 49 % → 49 % | 22.1 px | 0.18 | 1.00 | 1824 | quarters: 0.00 → 0.00 → 0.00 → 0.00

Numbers say: light vs heavy: width 21.9 → 42.1 px, dark 0.13 → 0.19.

## Oil · Henry Ward · Dirty contour #1c2238
Oil 1.00 · 34 px · 17.3 s

![Oil · Henry Ward · Dirty contour #1c2238](Oil-Henry-Ward-Dirty-contour-1c2238.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 7 % → 7 % | 20.6 px | 0.73 | 1.00 | 160 |
| heavy line | 12 % → 12 % | 34.2 px | 0.75 | 1.00 | 290 |
| pressure swell | 9 % → 9 % | 35.2 px | 0.78 | 1.00 | 144 |
| fast wave | 28 % → 28 % | 32.5 px | 0.76 | 1.00 | 865 |
| slow wave | 31 % → 31 % | 35.2 px | 0.78 | 1.00 | 866 |
| spiral | 42 % → 42 % | 27.5 px | 0.74 | 1.00 | 750 |
| loop | 25 % → 25 % | 32.4 px | 0.77 | 1.00 | 281 |
| tilted | 12 % → 12 % | 32.3 px | 0.78 | 1.00 | 149 |
| over the wet one | 23 % → 23 % | 32.0 px | 0.78 | 1.00 | 145 |
| long, no reload | 50 % → 50 % | 22.6 px | 0.72 | 1.00 | 895 | quarters: 0.50 → 0.45 → 0.34 → 0.33

Numbers say: light vs heavy: width 20.6 → 34.2 px, dark 0.73 → 0.75.

## Oil · Henry Ward · Ground #ece8e2
Gouache 1.00 · 160 px · 105.1 s

![Oil · Henry Ward · Ground #ece8e2](Oil-Henry-Ward-Ground-ece8e2.png)

A light paint: laid on a grey sheet (on white it cannot be seen); **dark** = how far it is from the grey either way.

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 51 % → 46 % | 148.3 px | 0.39 | 0.89 | 860 |
| heavy line | 52 % → 47 % | 151.5 px | 0.39 | 0.91 | 960 |
| pressure swell | 41 % → 45 % | 154.8 px | 0.39 | 1.10 | 681 |
| fast wave | 85 % → 86 % | 97.8 px | 0.38 | 1.01 | 3031 |
| slow wave | 86 % → 73 % | 99.2 px | 0.39 | 0.86 | 5063 |
| spiral | 88 % → 69 % | 58.3 px | 0.39 | 0.77 | 8092 |
| loop | 75 % → 69 % | 97.0 px | 0.39 | 0.92 | 3640 |
| tilted | 39 % → 39 % | 107.5 px | 0.39 | 1.00 | 2220 |
| over the wet one | 76 % → 71 % | 104.6 px | 0.39 | 0.93 | 1032 |
| long, no reload | 98 % → 87 % | 44.0 px | 0.39 | 0.88 | 7723 | quarters: 0.00 → 0.00 → 0.00 → 0.00

Numbers say: light vs heavy: width 148.3 → 151.5 px, dark 0.39 → 0.39; pressure barely changes the width.

## Oil · Henry Ward · Loaded flat #a03c1c
Oil 1.00 · 84 px · 38.1 s

![Oil · Henry Ward · Loaded flat #a03c1c](Oil-Henry-Ward-Loaded-flat-a03c1c.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 18 % → 20 % | 53.2 px | 0.53 | 1.06 | 288 |
| heavy line | 21 % → 21 % | 61.0 px | 0.57 | 1.00 | 327 |
| pressure swell | 20 % → 21 % | 76.0 px | 0.56 | 1.05 | 303 |
| fast wave | 52 % → 55 % | 60.6 px | 0.62 | 1.05 | 1000 |
| slow wave | 55 % → 55 % | 63.3 px | 0.58 | 1.00 | 2563 |
| spiral | 75 % → 75 % | 49.5 px | 0.53 | 1.00 | 1616 |
| loop | 52 % → 52 % | 67.1 px | 0.58 | 1.00 | 786 |
| tilted | 21 % → 21 % | 58.4 px | 0.60 | 1.00 | 648 |
| over the wet one | 40 % → 40 % | 52.9 px | 0.60 | 1.00 | 533 |
| long, no reload | 78 % → 78 % | 35.2 px | 0.57 | 1.00 | 3006 | quarters: 0.60 → 0.53 → 0.44 → 0.29

Numbers say: light vs heavy: width 53.2 → 61.0 px, dark 0.53 → 0.57.

## Oil · Henry Ward · Dirty contour #1f3a2c
Oil 1.00 · 34 px · 22.7 s

![Oil · Henry Ward · Dirty contour #1f3a2c](Oil-Henry-Ward-Dirty-contour-1f3a2c.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 7 % → 7 % | 20.6 px | 0.66 | 1.00 | 178 |
| heavy line | 12 % → 12 % | 34.2 px | 0.68 | 1.00 | 134 |
| pressure swell | 9 % → 9 % | 35.2 px | 0.71 | 1.00 | 185 |
| fast wave | 28 % → 28 % | 32.5 px | 0.69 | 1.00 | 875 |
| slow wave | 31 % → 31 % | 35.2 px | 0.71 | 1.00 | 604 |
| spiral | 42 % → 42 % | 27.5 px | 0.67 | 1.00 | 630 |
| loop | 25 % → 25 % | 32.4 px | 0.69 | 1.00 | 317 |
| tilted | 12 % → 12 % | 32.3 px | 0.71 | 1.00 | 166 |
| over the wet one | 23 % → 23 % | 32.0 px | 0.71 | 1.00 | 159 |
| long, no reload | 50 % → 50 % | 22.6 px | 0.64 | 1.00 | 1186 | quarters: 0.45 → 0.40 → 0.30 → 0.29

Numbers say: light vs heavy: width 20.6 → 34.2 px, dark 0.66 → 0.68.

## Oil · Henry Ward · Loaded flat #ecc8c8
Oil 1.00 · 84 px · 38.8 s

![Oil · Henry Ward · Loaded flat #ecc8c8](Oil-Henry-Ward-Loaded-flat-ecc8c8.png)

A light paint: laid on a grey sheet (on white it cannot be seen); **dark** = how far it is from the grey either way.

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 18 % → 20 % | 53.2 px | 0.27 | 1.06 | 282 |
| heavy line | 21 % → 21 % | 61.0 px | 0.31 | 1.00 | 313 |
| pressure swell | 20 % → 21 % | 76.0 px | 0.31 | 1.05 | 256 |
| fast wave | 52 % → 55 % | 60.6 px | 0.26 | 1.05 | 781 |
| slow wave | 55 % → 55 % | 63.3 px | 0.31 | 1.00 | 1835 |
| spiral | 75 % → 75 % | 49.5 px | 0.28 | 1.00 | 2152 |
| loop | 52 % → 52 % | 67.1 px | 0.31 | 1.00 | 1781 |
| tilted | 21 % → 21 % | 58.4 px | 0.26 | 1.00 | 1328 |
| over the wet one | 40 % → 40 % | 52.9 px | 0.26 | 1.00 | 983 |
| long, no reload | 78 % → 78 % | 35.2 px | 0.26 | 1.00 | 4795 | quarters: 0.00 → 0.00 → 0.00 → 0.00

Numbers say: light vs heavy: width 53.2 → 61.0 px, dark 0.27 → 0.31; the long stroke does not run out of paint.

## Oil · Henry Ward · Loaded flat #62c8e8
Oil 1.00 · 84 px · 39.3 s

![Oil · Henry Ward · Loaded flat #62c8e8](Oil-Henry-Ward-Loaded-flat-62c8e8.png)

A light paint: laid on a grey sheet (on white it cannot be seen); **dark** = how far it is from the grey either way.

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 18 % → 20 % | 53.2 px | 0.18 | 1.06 | 280 |
| heavy line | 21 % → 21 % | 61.0 px | 0.21 | 1.00 | 323 |
| pressure swell | 20 % → 21 % | 76.0 px | 0.21 | 1.05 | 312 |
| fast wave | 52 % → 55 % | 60.6 px | 0.16 | 1.05 | 1272 |
| slow wave | 55 % → 55 % | 63.3 px | 0.21 | 1.00 | 2009 |
| spiral | 75 % → 75 % | 49.5 px | 0.20 | 1.00 | 2815 |
| loop | 52 % → 52 % | 67.1 px | 0.20 | 1.00 | 2380 |
| tilted | 21 % → 21 % | 58.4 px | 0.16 | 1.00 | 1004 |
| over the wet one | 40 % → 40 % | 52.9 px | 0.16 | 1.00 | 519 |
| long, no reload | 78 % → 78 % | 35.2 px | 0.17 | 1.00 | 3727 | quarters: 0.00 → 0.00 → 0.01 → 0.00

Numbers say: light vs heavy: width 53.2 → 61.0 px, dark 0.18 → 0.21; the long stroke does not run out of paint.

## Oil · Henry Ward · Loaded flat #0f2018
Oil 1.00 · 84 px · 39.3 s

![Oil · Henry Ward · Loaded flat #0f2018](Oil-Henry-Ward-Loaded-flat-0f2018.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 18 % → 20 % | 53.2 px | 0.74 | 1.06 | 568 |
| heavy line | 21 % → 21 % | 61.0 px | 0.77 | 1.00 | 481 |
| pressure swell | 20 % → 21 % | 76.0 px | 0.76 | 1.05 | 297 |
| fast wave | 52 % → 55 % | 60.6 px | 0.81 | 1.05 | 1945 |
| slow wave | 55 % → 55 % | 63.3 px | 0.79 | 1.00 | 3017 |
| spiral | 75 % → 75 % | 49.5 px | 0.75 | 1.00 | 3279 |
| loop | 52 % → 52 % | 67.1 px | 0.79 | 1.00 | 1686 |
| tilted | 21 % → 21 % | 58.4 px | 0.79 | 1.00 | 937 |
| over the wet one | 40 % → 40 % | 52.9 px | 0.79 | 1.00 | 593 |
| long, no reload | 78 % → 78 % | 35.2 px | 0.79 | 1.00 | 3783 | quarters: 0.78 → 0.73 → 0.61 → 0.42

Numbers say: light vs heavy: width 53.2 → 61.0 px, dark 0.74 → 0.77.

## Oil · Henry Ward · Ground #e6e2ee
Gouache 1.00 · 160 px · 111.9 s

![Oil · Henry Ward · Ground #e6e2ee](Oil-Henry-Ward-Ground-e6e2ee.png)

A light paint: laid on a grey sheet (on white it cannot be seen); **dark** = how far it is from the grey either way.

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 51 % → 46 % | 148.3 px | 0.39 | 0.89 | 901 |
| heavy line | 52 % → 47 % | 151.5 px | 0.39 | 0.91 | 1125 |
| pressure swell | 41 % → 45 % | 154.8 px | 0.38 | 1.10 | 631 |
| fast wave | 85 % → 86 % | 97.8 px | 0.37 | 1.01 | 5183 |
| slow wave | 86 % → 73 % | 99.2 px | 0.38 | 0.86 | 7332 |
| spiral | 88 % → 69 % | 58.3 px | 0.38 | 0.77 | 3988 |
| loop | 75 % → 69 % | 97.0 px | 0.38 | 0.92 | 2810 |
| tilted | 39 % → 39 % | 107.5 px | 0.38 | 1.00 | 1027 |
| over the wet one | 76 % → 71 % | 104.6 px | 0.38 | 0.93 | 970 |
| long, no reload | 98 % → 87 % | 44.0 px | 0.38 | 0.88 | 5147 | quarters: 0.00 → 0.00 → 0.00 → 0.00

Numbers say: light vs heavy: width 148.3 → 151.5 px, dark 0.39 → 0.39; pressure barely changes the width.

## Oil · Henry Ward · Dry scrub #f2f0f6
Oil 1.00 · 90 px · 26.3 s

![Oil · Henry Ward · Dry scrub #f2f0f6](Oil-Henry-Ward-Dry-scrub-f2f0f6.png)

A light paint: laid on a grey sheet (on white it cannot be seen); **dark** = how far it is from the grey either way.

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 8 % → 9 % | 21.9 px | 0.21 | 1.21 | 486 |
| heavy line | 14 % → 14 % | 42.1 px | 0.30 | 1.00 | 515 |
| pressure swell | 14 % → 15 % | 51.7 px | 0.28 | 1.09 | 478 |
| fast wave | 51 % → 53 % | 58.7 px | 0.32 | 1.04 | 1815 |
| slow wave | 37 % → 37 % | 42.2 px | 0.31 | 1.00 | 2471 |
| spiral | 70 % → 70 % | 46.0 px | 0.25 | 1.00 | 2443 |
| loop | 36 % → 36 % | 46.7 px | 0.26 | 1.00 | 749 |
| tilted | 21 % → 21 % | 57.5 px | 0.25 | 1.00 | 511 |
| over the wet one | 29 % → 29 % | 22.2 px | 0.25 | 1.00 | 333 |
| long, no reload | 49 % → 49 % | 22.1 px | 0.26 | 1.00 | 2133 | quarters: 0.00 → 0.00 → 0.00 → 0.00

Numbers say: light vs heavy: width 21.9 → 42.1 px, dark 0.21 → 0.30.

## Oil · Henry Ward · Dirty contour #1e4a78
Oil 1.00 · 34 px · 16.2 s

![Oil · Henry Ward · Dirty contour #1e4a78](Oil-Henry-Ward-Dirty-contour-1e4a78.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 7 % → 7 % | 20.6 px | 0.60 | 1.00 | 105 |
| heavy line | 12 % → 12 % | 34.2 px | 0.62 | 1.00 | 132 |
| pressure swell | 9 % → 9 % | 35.2 px | 0.65 | 1.00 | 112 |
| fast wave | 28 % → 28 % | 32.5 px | 0.62 | 1.00 | 356 |
| slow wave | 31 % → 31 % | 35.2 px | 0.64 | 1.00 | 676 |
| spiral | 42 % → 42 % | 27.5 px | 0.60 | 1.00 | 821 |
| loop | 25 % → 25 % | 32.4 px | 0.63 | 1.00 | 477 |
| tilted | 12 % → 12 % | 32.3 px | 0.65 | 1.00 | 265 |
| over the wet one | 23 % → 23 % | 32.0 px | 0.65 | 1.00 | 212 |
| long, no reload | 50 % → 50 % | 22.6 px | 0.57 | 1.00 | 1202 | quarters: 0.41 → 0.36 → 0.26 → 0.25

Numbers say: light vs heavy: width 20.6 → 34.2 px, dark 0.60 → 0.62.

## Oil · Henry Ward · Dirty contour #141414
Oil 1.00 · 34 px · 16.4 s

![Oil · Henry Ward · Dirty contour #141414](Oil-Henry-Ward-Dirty-contour-141414.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 7 % → 7 % | 20.6 px | 0.79 | 1.00 | 120 |
| heavy line | 12 % → 12 % | 34.2 px | 0.81 | 1.00 | 145 |
| pressure swell | 9 % → 9 % | 35.2 px | 0.84 | 1.00 | 89 |
| fast wave | 28 % → 28 % | 32.5 px | 0.82 | 1.00 | 471 |
| slow wave | 31 % → 31 % | 35.2 px | 0.84 | 1.00 | 669 |
| spiral | 42 % → 42 % | 27.5 px | 0.81 | 1.00 | 1688 |
| loop | 25 % → 25 % | 32.4 px | 0.84 | 1.00 | 421 |
| tilted | 12 % → 12 % | 32.3 px | 0.84 | 1.00 | 360 |
| over the wet one | 23 % → 23 % | 32.0 px | 0.84 | 1.00 | 251 |
| long, no reload | 50 % → 50 % | 22.6 px | 0.80 | 1.00 | 1020 | quarters: 0.55 → 0.49 → 0.39 → 0.38

Numbers say: light vs heavy: width 20.6 → 34.2 px, dark 0.79 → 0.81.

## Oil · Henry Ward · Dry scrub #c89038
Oil 1.00 · 90 px · 19.0 s

![Oil · Henry Ward · Dry scrub #c89038](Oil-Henry-Ward-Dry-scrub-c89038.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 8 % → 9 % | 21.9 px | 0.18 | 1.21 | 269 |
| heavy line | 14 % → 14 % | 42.1 px | 0.23 | 1.00 | 330 |
| pressure swell | 14 % → 15 % | 51.7 px | 0.23 | 1.09 | 300 |
| fast wave | 51 % → 53 % | 58.7 px | 0.32 | 1.04 | 902 |
| slow wave | 37 % → 37 % | 42.2 px | 0.22 | 1.00 | 1387 |
| spiral | 70 % → 70 % | 46.0 px | 0.19 | 1.00 | 1405 |
| loop | 36 % → 36 % | 46.7 px | 0.21 | 1.00 | 744 |
| tilted | 21 % → 21 % | 57.5 px | 0.29 | 1.00 | 398 |
| over the wet one | 29 % → 29 % | 22.2 px | 0.29 | 1.00 | 283 |
| long, no reload | 49 % → 49 % | 22.1 px | 0.16 | 1.00 | 1675 | quarters: 0.10 → 0.09 → 0.08 → 0.05

Numbers say: light vs heavy: width 21.9 → 42.1 px, dark 0.18 → 0.23.

## Oil · Henry Ward · Ground #efe8b8
Gouache 1.00 · 160 px · 101.4 s

![Oil · Henry Ward · Ground #efe8b8](Oil-Henry-Ward-Ground-efe8b8.png)

A light paint: laid on a grey sheet (on white it cannot be seen); **dark** = how far it is from the grey either way.

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 51 % → 46 % | 148.3 px | 0.39 | 0.89 | 717 |
| heavy line | 52 % → 47 % | 151.5 px | 0.39 | 0.91 | 870 |
| pressure swell | 41 % → 45 % | 154.8 px | 0.38 | 1.10 | 600 |
| fast wave | 85 % → 86 % | 97.8 px | 0.38 | 1.01 | 2164 |
| slow wave | 86 % → 73 % | 99.2 px | 0.39 | 0.86 | 3611 |
| spiral | 88 % → 69 % | 58.3 px | 0.38 | 0.77 | 3693 |
| loop | 75 % → 69 % | 97.0 px | 0.39 | 0.92 | 2132 |
| tilted | 39 % → 39 % | 107.5 px | 0.38 | 1.00 | 1129 |
| over the wet one | 76 % → 71 % | 104.6 px | 0.38 | 0.93 | 1004 |
| long, no reload | 98 % → 87 % | 44.0 px | 0.38 | 0.88 | 7424 | quarters: 0.00 → 0.00 → 0.00 → 0.00

Numbers say: light vs heavy: width 148.3 → 151.5 px, dark 0.39 → 0.39; pressure barely changes the width.

## Oil · Henry Ward · Loaded flat #a89ac8
Oil 1.00 · 84 px · 26.2 s

![Oil · Henry Ward · Loaded flat #a89ac8](Oil-Henry-Ward-Loaded-flat-a89ac8.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 18 % → 20 % | 53.2 px | 0.19 | 1.06 | 283 |
| heavy line | 21 % → 21 % | 61.0 px | 0.24 | 1.00 | 324 |
| pressure swell | 20 % → 21 % | 76.0 px | 0.22 | 1.05 | 239 |
| fast wave | 52 % → 55 % | 60.6 px | 0.30 | 1.05 | 827 |
| slow wave | 55 % → 55 % | 63.3 px | 0.23 | 1.00 | 1453 |
| spiral | 75 % → 75 % | 49.5 px | 0.19 | 1.00 | 1489 |
| loop | 52 % → 52 % | 67.1 px | 0.23 | 1.00 | 770 |
| tilted | 21 % → 21 % | 58.4 px | 0.30 | 1.00 | 427 |
| over the wet one | 40 % → 40 % | 52.9 px | 0.30 | 1.00 | 349 |
| long, no reload | 78 % → 78 % | 35.2 px | 0.23 | 1.00 | 2335 | quarters: 0.27 → 0.22 → 0.16 → 0.10

Numbers say: light vs heavy: width 53.2 → 61.0 px, dark 0.19 → 0.24.

## Oil · Henry Ward · Dirty contour #2a2418
Oil 1.00 · 34 px · 14.2 s

![Oil · Henry Ward · Dirty contour #2a2418](Oil-Henry-Ward-Dirty-contour-2a2418.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 7 % → 7 % | 20.6 px | 0.72 | 1.00 | 107 |
| heavy line | 12 % → 12 % | 34.2 px | 0.74 | 1.00 | 138 |
| pressure swell | 9 % → 9 % | 35.2 px | 0.77 | 1.00 | 95 |
| fast wave | 28 % → 28 % | 32.5 px | 0.75 | 1.00 | 347 |
| slow wave | 31 % → 31 % | 35.2 px | 0.77 | 1.00 | 636 |
| spiral | 42 % → 42 % | 27.5 px | 0.73 | 1.00 | 574 |
| loop | 25 % → 25 % | 32.4 px | 0.75 | 1.00 | 285 |
| tilted | 12 % → 12 % | 32.3 px | 0.76 | 1.00 | 168 |
| over the wet one | 23 % → 23 % | 32.0 px | 0.76 | 1.00 | 147 |
| long, no reload | 50 % → 50 % | 22.6 px | 0.71 | 1.00 | 849 | quarters: 0.50 → 0.44 → 0.34 → 0.33

Numbers say: light vs heavy: width 20.6 → 34.2 px, dark 0.72 → 0.74.

## Oil · Henry Ward · Loaded flat #2a2418
Oil 1.00 · 84 px · 25.8 s

![Oil · Henry Ward · Loaded flat #2a2418](Oil-Henry-Ward-Loaded-flat-2a2418.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 18 % → 20 % | 53.2 px | 0.68 | 1.06 | 280 |
| heavy line | 21 % → 21 % | 61.0 px | 0.71 | 1.00 | 292 |
| pressure swell | 20 % → 21 % | 76.0 px | 0.72 | 1.05 | 217 |
| fast wave | 52 % → 55 % | 60.6 px | 0.77 | 1.05 | 807 |
| slow wave | 55 % → 55 % | 63.3 px | 0.74 | 1.00 | 1398 |
| spiral | 75 % → 75 % | 49.5 px | 0.70 | 1.00 | 1484 |
| loop | 52 % → 52 % | 67.1 px | 0.75 | 1.00 | 831 |
| tilted | 21 % → 21 % | 58.4 px | 0.75 | 1.00 | 467 |
| over the wet one | 40 % → 40 % | 52.9 px | 0.75 | 1.00 | 363 |
| long, no reload | 78 % → 78 % | 35.2 px | 0.74 | 1.00 | 1943 | quarters: 0.74 → 0.68 → 0.57 → 0.38

Numbers say: light vs heavy: width 53.2 → 61.0 px, dark 0.68 → 0.71.

## Oil · Henry Ward · Dry scrub #efeee6
Oil 1.00 · 90 px · 19.4 s

![Oil · Henry Ward · Dry scrub #efeee6](Oil-Henry-Ward-Dry-scrub-efeee6.png)

A light paint: laid on a grey sheet (on white it cannot be seen); **dark** = how far it is from the grey either way.

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 8 % → 9 % | 21.9 px | 0.21 | 1.21 | 220 |
| heavy line | 14 % → 14 % | 42.1 px | 0.29 | 1.00 | 301 |
| pressure swell | 14 % → 15 % | 51.7 px | 0.27 | 1.09 | 194 |
| fast wave | 51 % → 53 % | 58.7 px | 0.31 | 1.04 | 901 |
| slow wave | 37 % → 37 % | 42.2 px | 0.30 | 1.00 | 1289 |
| spiral | 70 % → 70 % | 46.0 px | 0.25 | 1.00 | 1463 |
| loop | 36 % → 36 % | 46.7 px | 0.26 | 1.00 | 693 |
| tilted | 21 % → 21 % | 57.5 px | 0.24 | 1.00 | 441 |
| over the wet one | 29 % → 29 % | 22.2 px | 0.24 | 1.00 | 303 |
| long, no reload | 49 % → 49 % | 22.1 px | 0.25 | 1.00 | 1751 | quarters: 0.00 → 0.00 → 0.00 → 0.00

Numbers say: light vs heavy: width 21.9 → 42.1 px, dark 0.21 → 0.29.

## Oil · Henry Ward · Ground #e6e2f0
Gouache 1.00 · 160 px · 103.4 s

![Oil · Henry Ward · Ground #e6e2f0](Oil-Henry-Ward-Ground-e6e2f0.png)

A light paint: laid on a grey sheet (on white it cannot be seen); **dark** = how far it is from the grey either way.

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 51 % → 46 % | 148.3 px | 0.39 | 0.89 | 655 |
| heavy line | 52 % → 47 % | 151.5 px | 0.39 | 0.91 | 754 |
| pressure swell | 41 % → 45 % | 154.8 px | 0.38 | 1.10 | 680 |
| fast wave | 85 % → 86 % | 97.8 px | 0.37 | 1.01 | 2262 |
| slow wave | 86 % → 73 % | 99.2 px | 0.38 | 0.86 | 4206 |
| spiral | 88 % → 69 % | 58.3 px | 0.38 | 0.77 | 3809 |
| loop | 75 % → 69 % | 97.0 px | 0.38 | 0.92 | 2715 |
| tilted | 39 % → 39 % | 107.5 px | 0.38 | 1.00 | 5632 |
| over the wet one | 76 % → 71 % | 104.6 px | 0.38 | 0.93 | 5626 |
| long, no reload | 98 % → 87 % | 44.0 px | 0.38 | 0.88 | 11741 | quarters: 0.00 → 0.00 → 0.00 → 0.00

Numbers say: light vs heavy: width 148.3 → 151.5 px, dark 0.39 → 0.39; pressure barely changes the width.

## Oil · Henry Ward · Loaded flat #a8b84a
Oil 1.00 · 84 px · 46.0 s

![Oil · Henry Ward · Loaded flat #a8b84a](Oil-Henry-Ward-Loaded-flat-a8b84a.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 18 % → 20 % | 53.2 px | 0.17 | 1.06 | 276 |
| heavy line | 21 % → 21 % | 61.0 px | 0.21 | 1.00 | 307 |
| pressure swell | 20 % → 21 % | 76.0 px | 0.19 | 1.05 | 225 |
| fast wave | 52 % → 55 % | 60.6 px | 0.27 | 1.05 | 888 |
| slow wave | 55 % → 55 % | 63.3 px | 0.20 | 1.00 | 1571 |
| spiral | 75 % → 75 % | 49.5 px | 0.17 | 1.00 | 1600 |
| loop | 52 % → 52 % | 67.1 px | 0.21 | 1.00 | 800 |
| tilted | 21 % → 21 % | 58.4 px | 0.27 | 1.00 | 447 |
| over the wet one | 40 % → 40 % | 52.9 px | 0.27 | 1.00 | 335 |
| long, no reload | 78 % → 78 % | 35.2 px | 0.21 | 1.00 | 3143 | quarters: 0.25 → 0.20 → 0.15 → 0.09

Numbers say: light vs heavy: width 53.2 → 61.0 px, dark 0.17 → 0.21.

## Oil · Henry Ward · Thin veil #5a8a6a
Oil 0.81 · Ink 0.19 · 96 px · 74.6 s

![Oil · Henry Ward · Thin veil #5a8a6a](Oil-Henry-Ward-Thin-veil-5a8a6a.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 9 % → 4 % | 24.9 px | 0.23 | 0.51 | 264 |
| heavy line | 22 % → 20 % | 65.2 px | 0.38 | 0.89 | 431 |
| pressure swell | 20 % → 18 % | 73.8 px | 0.32 | 0.91 | 247 |
| fast wave | 59 % → 58 % | 68.4 px | 0.40 | 0.98 | 1007 |
| slow wave | 58 % → 51 % | 67.1 px | 0.33 | 0.89 | 1758 |
| spiral | 83 % → 67 % | 55.0 px | 0.29 | 0.80 | 2161 |
| loop | 57 % → 49 % | 74.0 px | 0.26 | 0.85 | 1240 |
| tilted | 23 % → 23 % | 63.1 px | 0.41 | 1.01 | 552 |
| over the wet one | 36 % → 34 % | 38.7 px | 0.41 | 0.93 | 406 |
| long, no reload | 82 % → 70 % | 36.7 px | 0.25 | 0.85 | 10524 | quarters: 0.30 → 0.21 → 0.16 → 0.10

Numbers say: light vs heavy: width 24.9 → 65.2 px, dark 0.23 → 0.38.

## Oil · Henry Ward · Loaded flat #4a1420
Oil 1.00 · 84 px · 49.6 s

![Oil · Henry Ward · Loaded flat #4a1420](Oil-Henry-Ward-Loaded-flat-4a1420.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 18 % → 20 % | 53.2 px | 0.72 | 1.06 | 250 |
| heavy line | 21 % → 21 % | 61.0 px | 0.75 | 1.00 | 398 |
| pressure swell | 20 % → 21 % | 76.0 px | 0.74 | 1.05 | 287 |
| fast wave | 52 % → 55 % | 60.6 px | 0.79 | 1.05 | 851 |
| slow wave | 55 % → 55 % | 63.3 px | 0.77 | 1.00 | 1522 |
| spiral | 75 % → 75 % | 49.5 px | 0.72 | 1.00 | 2710 |
| loop | 52 % → 52 % | 67.1 px | 0.77 | 1.00 | 1010 |
| tilted | 21 % → 21 % | 58.4 px | 0.77 | 1.00 | 530 |
| over the wet one | 40 % → 40 % | 52.9 px | 0.77 | 1.00 | 366 |
| long, no reload | 78 % → 78 % | 35.2 px | 0.76 | 1.00 | 11979 | quarters: 0.77 → 0.71 → 0.59 → 0.41

Numbers say: light vs heavy: width 53.2 → 61.0 px, dark 0.72 → 0.75.

## Oil · Henry Ward · Dirty contour #2a0a10
Oil 1.00 · 34 px · 35.0 s

![Oil · Henry Ward · Dirty contour #2a0a10](Oil-Henry-Ward-Dirty-contour-2a0a10.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 7 % → 7 % | 20.6 px | 0.80 | 1.00 | 121 |
| heavy line | 12 % → 12 % | 34.2 px | 0.82 | 1.00 | 164 |
| pressure swell | 9 % → 9 % | 35.2 px | 0.85 | 1.00 | 85 |
| fast wave | 28 % → 28 % | 32.5 px | 0.82 | 1.00 | 564 |
| slow wave | 31 % → 31 % | 35.2 px | 0.85 | 1.00 | 1128 |
| spiral | 42 % → 42 % | 27.5 px | 0.82 | 1.00 | 794 |
| loop | 25 % → 25 % | 32.4 px | 0.84 | 1.00 | 370 |
| tilted | 12 % → 12 % | 32.3 px | 0.84 | 1.00 | 200 |
| over the wet one | 23 % → 23 % | 32.0 px | 0.84 | 1.00 | 162 |
| long, no reload | 50 % → 50 % | 22.6 px | 0.81 | 1.00 | 3171 | quarters: 0.55 → 0.50 → 0.39 → 0.39

Numbers say: light vs heavy: width 20.6 → 34.2 px, dark 0.80 → 0.82.

## Oil · Henry Ward · Dry scrub #c0506a
Oil 1.00 · 90 px · 43.6 s

![Oil · Henry Ward · Dry scrub #c0506a](Oil-Henry-Ward-Dry-scrub-c0506a.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 8 % → 9 % | 21.9 px | 0.35 | 1.21 | 434 |
| heavy line | 14 % → 14 % | 42.1 px | 0.40 | 1.00 | 659 |
| pressure swell | 14 % → 15 % | 51.7 px | 0.40 | 1.09 | 310 |
| fast wave | 51 % → 53 % | 58.7 px | 0.49 | 1.04 | 1034 |
| slow wave | 37 % → 37 % | 42.2 px | 0.40 | 1.00 | 4576 |
| spiral | 70 % → 70 % | 46.0 px | 0.38 | 1.00 | 8377 |
| loop | 36 % → 36 % | 46.7 px | 0.40 | 1.00 | 1637 |
| tilted | 21 % → 21 % | 57.5 px | 0.46 | 1.00 | 1087 |
| over the wet one | 29 % → 29 % | 22.2 px | 0.46 | 1.00 | 633 |
| long, no reload | 49 % → 49 % | 22.1 px | 0.31 | 1.00 | 3727 | quarters: 0.19 → 0.18 → 0.16 → 0.10

Numbers say: light vs heavy: width 21.9 → 42.1 px, dark 0.35 → 0.40.

## Oil · Henry Ward · Ground #d8d4c8
Gouache 1.00 · 160 px · 104.1 s

![Oil · Henry Ward · Ground #d8d4c8](Oil-Henry-Ward-Ground-d8d4c8.png)

A light paint: laid on a grey sheet (on white it cannot be seen); **dark** = how far it is from the grey either way.

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 51 % → 46 % | 148.3 px | 0.35 | 0.89 | 829 |
| heavy line | 52 % → 47 % | 151.5 px | 0.35 | 0.91 | 5241 |
| pressure swell | 41 % → 45 % | 154.8 px | 0.35 | 1.10 | 4206 |
| fast wave | 85 % → 86 % | 97.8 px | 0.34 | 1.01 | 5510 |
| slow wave | 86 % → 73 % | 99.2 px | 0.35 | 0.86 | 7491 |
| spiral | 88 % → 69 % | 58.3 px | 0.35 | 0.77 | 5578 |
| loop | 75 % → 69 % | 97.0 px | 0.35 | 0.92 | 2631 |
| tilted | 39 % → 39 % | 107.5 px | 0.35 | 1.00 | 1265 |
| over the wet one | 76 % → 71 % | 104.6 px | 0.35 | 0.93 | 1810 |
| long, no reload | 98 % → 87 % | 44.0 px | 0.35 | 0.88 | 6150 | quarters: 0.00 → 0.00 → 0.00 → 0.00

Numbers say: light vs heavy: width 148.3 → 151.5 px, dark 0.35 → 0.35; pressure barely changes the width.

## Oil · Henry Ward · Loaded flat #e8d8b0
Oil 1.00 · 84 px · 36.2 s

![Oil · Henry Ward · Loaded flat #e8d8b0](Oil-Henry-Ward-Loaded-flat-e8d8b0.png)

A light paint: laid on a grey sheet (on white it cannot be seen); **dark** = how far it is from the grey either way.

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 18 % → 20 % | 53.2 px | 0.29 | 1.06 | 484 |
| heavy line | 21 % → 21 % | 61.0 px | 0.34 | 1.00 | 508 |
| pressure swell | 20 % → 21 % | 76.0 px | 0.33 | 1.05 | 488 |
| fast wave | 52 % → 55 % | 60.6 px | 0.29 | 1.05 | 1678 |
| slow wave | 55 % → 55 % | 63.3 px | 0.33 | 1.00 | 2529 |
| spiral | 75 % → 75 % | 49.5 px | 0.30 | 1.00 | 2407 |
| loop | 52 % → 52 % | 67.1 px | 0.33 | 1.00 | 1129 |
| tilted | 21 % → 21 % | 58.4 px | 0.29 | 1.00 | 554 |
| over the wet one | 40 % → 40 % | 52.9 px | 0.29 | 1.00 | 670 |
| long, no reload | 78 % → 78 % | 35.2 px | 0.28 | 1.00 | 3972 | quarters: 0.00 → 0.00 → 0.00 → 0.00

Numbers say: light vs heavy: width 53.2 → 61.0 px, dark 0.29 → 0.34; the long stroke does not run out of paint.

## Oil · Henry Ward · Dry scrub #f2ead0
Oil 1.00 · 90 px · 29.1 s

![Oil · Henry Ward · Dry scrub #f2ead0](Oil-Henry-Ward-Dry-scrub-f2ead0.png)

A light paint: laid on a grey sheet (on white it cannot be seen); **dark** = how far it is from the grey either way.

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 8 % → 9 % | 21.9 px | 0.20 | 1.21 | 486 |
| heavy line | 14 % → 14 % | 42.1 px | 0.29 | 1.00 | 614 |
| pressure swell | 14 % → 15 % | 51.7 px | 0.26 | 1.09 | 366 |
| fast wave | 51 % → 53 % | 58.7 px | 0.30 | 1.04 | 1511 |
| slow wave | 37 % → 37 % | 42.2 px | 0.30 | 1.00 | 2404 |
| spiral | 70 % → 70 % | 46.0 px | 0.24 | 1.00 | 1979 |
| loop | 36 % → 36 % | 46.7 px | 0.25 | 1.00 | 1171 |
| tilted | 21 % → 21 % | 57.5 px | 0.24 | 1.00 | 1069 |
| over the wet one | 29 % → 29 % | 22.2 px | 0.24 | 1.00 | 456 |
| long, no reload | 49 % → 49 % | 22.1 px | 0.24 | 1.00 | 2537 | quarters: 0.00 → 0.00 → 0.00 → 0.00

Numbers say: light vs heavy: width 21.9 → 42.1 px, dark 0.20 → 0.29.

## Oil · Henry Ward · Loaded flat #2a1428
Oil 1.00 · 84 px · 34.3 s

![Oil · Henry Ward · Loaded flat #2a1428](Oil-Henry-Ward-Loaded-flat-2a1428.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 18 % → 20 % | 53.2 px | 0.74 | 1.06 | 558 |
| heavy line | 21 % → 21 % | 61.0 px | 0.77 | 1.00 | 566 |
| pressure swell | 20 % → 21 % | 76.0 px | 0.76 | 1.05 | 386 |
| fast wave | 52 % → 55 % | 60.6 px | 0.81 | 1.05 | 1371 |
| slow wave | 55 % → 55 % | 63.3 px | 0.79 | 1.00 | 2436 |
| spiral | 75 % → 75 % | 49.5 px | 0.75 | 1.00 | 2268 |
| loop | 52 % → 52 % | 67.1 px | 0.80 | 1.00 | 2006 |
| tilted | 21 % → 21 % | 58.4 px | 0.79 | 1.00 | 713 |
| over the wet one | 40 % → 40 % | 52.9 px | 0.79 | 1.00 | 443 |
| long, no reload | 78 % → 78 % | 35.2 px | 0.79 | 1.00 | 2951 | quarters: 0.79 → 0.73 → 0.61 → 0.42

Numbers say: light vs heavy: width 53.2 → 61.0 px, dark 0.74 → 0.77.

## Oil · Henry Ward · Ground #e8e4e0
Gouache 1.00 · 160 px · 81.6 s

![Oil · Henry Ward · Ground #e8e4e0](Oil-Henry-Ward-Ground-e8e4e0.png)

A light paint: laid on a grey sheet (on white it cannot be seen); **dark** = how far it is from the grey either way.

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 51 % → 46 % | 148.3 px | 0.39 | 0.89 | 1178 |
| heavy line | 52 % → 47 % | 151.5 px | 0.39 | 0.91 | 1393 |
| pressure swell | 41 % → 45 % | 154.8 px | 0.38 | 1.10 | 845 |
| fast wave | 85 % → 86 % | 97.8 px | 0.37 | 1.01 | 3141 |
| slow wave | 86 % → 73 % | 99.2 px | 0.38 | 0.86 | 5440 |
| spiral | 88 % → 69 % | 58.3 px | 0.38 | 0.77 | 3681 |
| loop | 75 % → 69 % | 97.0 px | 0.39 | 0.92 | 1879 |
| tilted | 39 % → 39 % | 107.5 px | 0.38 | 1.00 | 1077 |
| over the wet one | 76 % → 71 % | 104.6 px | 0.38 | 0.93 | 906 |
| long, no reload | 98 % → 87 % | 44.0 px | 0.38 | 0.88 | 5864 | quarters: 0.00 → 0.00 → 0.00 → 0.00

Numbers say: light vs heavy: width 148.3 → 151.5 px, dark 0.39 → 0.39; pressure barely changes the width.

## Oil · Henry Ward · Loaded flat #8a2a18
Oil 1.00 · 84 px · 30.3 s

![Oil · Henry Ward · Loaded flat #8a2a18](Oil-Henry-Ward-Loaded-flat-8a2a18.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 18 % → 20 % | 53.2 px | 0.61 | 1.06 | 456 |
| heavy line | 21 % → 21 % | 61.0 px | 0.65 | 1.00 | 991 |
| pressure swell | 20 % → 21 % | 76.0 px | 0.64 | 1.05 | 413 |
| fast wave | 52 % → 55 % | 60.6 px | 0.69 | 1.05 | 1146 |
| slow wave | 55 % → 55 % | 63.3 px | 0.66 | 1.00 | 2226 |
| spiral | 75 % → 75 % | 49.5 px | 0.62 | 1.00 | 1883 |
| loop | 52 % → 52 % | 67.1 px | 0.67 | 1.00 | 1316 |
| tilted | 21 % → 21 % | 58.4 px | 0.68 | 1.00 | 653 |
| over the wet one | 40 % → 40 % | 52.9 px | 0.68 | 1.00 | 392 |
| long, no reload | 78 % → 78 % | 35.2 px | 0.66 | 1.00 | 2407 | quarters: 0.67 → 0.61 → 0.50 → 0.34

Numbers say: light vs heavy: width 53.2 → 61.0 px, dark 0.61 → 0.65.

## Oil · Henry Ward · Loaded flat #a8c8dc
Oil 1.00 · 84 px · 28.9 s

![Oil · Henry Ward · Loaded flat #a8c8dc](Oil-Henry-Ward-Loaded-flat-a8c8dc.png)

A light paint: laid on a grey sheet (on white it cannot be seen); **dark** = how far it is from the grey either way.

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 18 % → 20 % | 53.2 px | 0.24 | 1.06 | 436 |
| heavy line | 21 % → 21 % | 61.0 px | 0.28 | 1.00 | 454 |
| pressure swell | 20 % → 21 % | 76.0 px | 0.28 | 1.05 | 318 |
| fast wave | 52 % → 55 % | 60.6 px | 0.23 | 1.05 | 1454 |
| slow wave | 55 % → 55 % | 63.3 px | 0.28 | 1.00 | 1875 |
| spiral | 75 % → 75 % | 49.5 px | 0.26 | 1.00 | 2664 |
| loop | 52 % → 52 % | 67.1 px | 0.27 | 1.00 | 1090 |
| tilted | 21 % → 21 % | 58.4 px | 0.23 | 1.00 | 506 |
| over the wet one | 40 % → 40 % | 52.9 px | 0.23 | 1.00 | 462 |
| long, no reload | 78 % → 78 % | 35.2 px | 0.23 | 1.00 | 2112 | quarters: 0.00 → 0.00 → 0.00 → 0.00

Numbers say: light vs heavy: width 53.2 → 61.0 px, dark 0.24 → 0.28; the long stroke does not run out of paint.

## Oil · Henry Ward · Dry scrub #d8e8f0
Oil 1.00 · 90 px · 20.1 s

![Oil · Henry Ward · Dry scrub #d8e8f0](Oil-Henry-Ward-Dry-scrub-d8e8f0.png)

A light paint: laid on a grey sheet (on white it cannot be seen); **dark** = how far it is from the grey either way.

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 8 % → 9 % | 21.9 px | 0.19 | 1.21 | 233 |
| heavy line | 14 % → 14 % | 42.1 px | 0.28 | 1.00 | 397 |
| pressure swell | 14 % → 15 % | 51.7 px | 0.25 | 1.09 | 207 |
| fast wave | 51 % → 53 % | 58.7 px | 0.29 | 1.04 | 1012 |
| slow wave | 37 % → 37 % | 42.2 px | 0.29 | 1.00 | 1333 |
| spiral | 70 % → 70 % | 46.0 px | 0.23 | 1.00 | 1484 |
| loop | 36 % → 36 % | 46.7 px | 0.24 | 1.00 | 719 |
| tilted | 21 % → 21 % | 57.5 px | 0.23 | 1.00 | 427 |
| over the wet one | 29 % → 29 % | 22.2 px | 0.23 | 1.00 | 271 |
| long, no reload | 49 % → 49 % | 22.1 px | 0.24 | 1.00 | 1778 | quarters: 0.00 → 0.00 → 0.00 → 0.00

Numbers say: light vs heavy: width 21.9 → 42.1 px, dark 0.19 → 0.28.

## Oil · Henry Ward · Ground #3a3a34
Gouache 1.00 · 160 px · 76.2 s

![Oil · Henry Ward · Ground #3a3a34](Oil-Henry-Ward-Ground-3a3a34.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 51 % → 46 % | 148.3 px | 0.47 | 0.89 | 804 |
| heavy line | 52 % → 47 % | 151.5 px | 0.47 | 0.91 | 874 |
| pressure swell | 41 % → 45 % | 154.8 px | 0.48 | 1.10 | 684 |
| fast wave | 85 % → 86 % | 97.8 px | 0.48 | 1.01 | 2330 |
| slow wave | 86 % → 73 % | 99.2 px | 0.47 | 0.86 | 3971 |
| spiral | 88 % → 69 % | 58.3 px | 0.48 | 0.77 | 4133 |
| loop | 75 % → 69 % | 97.0 px | 0.47 | 0.92 | 2371 |
| tilted | 39 % → 39 % | 107.5 px | 0.47 | 1.00 | 1071 |
| over the wet one | 76 % → 71 % | 104.6 px | 0.47 | 0.93 | 1032 |
| long, no reload | 98 % → 87 % | 44.0 px | 0.47 | 0.88 | 5444 | quarters: 0.47 → 0.47 → 0.47 → 0.45

Numbers say: light vs heavy: width 148.3 → 151.5 px, dark 0.47 → 0.47; pressure barely changes the width; the long stroke does not run out of paint.

## Oil · Henry Ward · Loaded flat #8a906a
Oil 1.00 · 84 px · 27.4 s

![Oil · Henry Ward · Loaded flat #8a906a](Oil-Henry-Ward-Loaded-flat-8a906a.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 18 % → 20 % | 53.2 px | 0.25 | 1.06 | 353 |
| heavy line | 21 % → 21 % | 61.0 px | 0.30 | 1.00 | 313 |
| pressure swell | 20 % → 21 % | 76.0 px | 0.29 | 1.05 | 236 |
| fast wave | 52 % → 55 % | 60.6 px | 0.36 | 1.05 | 925 |
| slow wave | 55 % → 55 % | 63.3 px | 0.30 | 1.00 | 1546 |
| spiral | 75 % → 75 % | 49.5 px | 0.25 | 1.00 | 1632 |
| loop | 52 % → 52 % | 67.1 px | 0.31 | 1.00 | 756 |
| tilted | 21 % → 21 % | 58.4 px | 0.36 | 1.00 | 452 |
| over the wet one | 40 % → 40 % | 52.9 px | 0.36 | 1.00 | 338 |
| long, no reload | 78 % → 78 % | 35.2 px | 0.30 | 1.00 | 2161 | quarters: 0.34 → 0.28 → 0.21 → 0.13

Numbers say: light vs heavy: width 53.2 → 61.0 px, dark 0.25 → 0.30.

## Oil · Henry Ward · Loaded flat #7a8458
Oil 1.00 · 84 px · 26.9 s

![Oil · Henry Ward · Loaded flat #7a8458](Oil-Henry-Ward-Loaded-flat-7a8458.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 18 % → 20 % | 53.2 px | 0.29 | 1.06 | 274 |
| heavy line | 21 % → 21 % | 61.0 px | 0.35 | 1.00 | 365 |
| pressure swell | 20 % → 21 % | 76.0 px | 0.33 | 1.05 | 225 |
| fast wave | 52 % → 55 % | 60.6 px | 0.41 | 1.05 | 817 |
| slow wave | 55 % → 55 % | 63.3 px | 0.35 | 1.00 | 1547 |
| spiral | 75 % → 75 % | 49.5 px | 0.29 | 1.00 | 1542 |
| loop | 52 % → 52 % | 67.1 px | 0.35 | 1.00 | 764 |
| tilted | 21 % → 21 % | 58.4 px | 0.40 | 1.00 | 485 |
| over the wet one | 40 % → 40 % | 52.9 px | 0.40 | 1.00 | 324 |
| long, no reload | 78 % → 78 % | 35.2 px | 0.34 | 1.00 | 2299 | quarters: 0.39 → 0.32 → 0.25 → 0.15

Numbers say: light vs heavy: width 53.2 → 61.0 px, dark 0.29 → 0.35.

## Oil · Henry Ward · Dry scrub #a8ae88
Oil 1.00 · 90 px · 21.6 s

![Oil · Henry Ward · Dry scrub #a8ae88](Oil-Henry-Ward-Dry-scrub-a8ae88.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 8 % → 9 % | 21.9 px | 0.11 | 1.21 | 260 |
| heavy line | 14 % → 14 % | 42.1 px | 0.16 | 1.00 | 313 |
| pressure swell | 14 % → 15 % | 51.7 px | 0.15 | 1.09 | 219 |
| fast wave | 51 % → 53 % | 58.7 px | 0.24 | 1.04 | 940 |
| slow wave | 37 % → 37 % | 42.2 px | 0.14 | 1.00 | 1367 |
| spiral | 70 % → 70 % | 46.0 px | 0.12 | 1.00 | 1555 |
| loop | 36 % → 36 % | 46.7 px | 0.13 | 1.00 | 755 |
| tilted | 21 % → 21 % | 57.5 px | 0.23 | 1.00 | 455 |
| over the wet one | 29 % → 29 % | 22.2 px | 0.23 | 1.00 | 538 |
| long, no reload | 49 % → 49 % | 22.1 px | 0.09 | 1.00 | 2258 | quarters: 0.06 → 0.05 → 0.04 → 0.03

Numbers say: light vs heavy: width 21.9 → 42.1 px, dark 0.11 → 0.16.

## v3 · Any shape · K stamp
Gouache 1.00 · 48 px · 43.3 s

![v3 · Any shape · K stamp](v3-Any-shape-K-stamp.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 20 % → 19 % | 59.0 px | 0.40 | 0.93 | 240 |
| heavy line | 20 % → 19 % | 59.1 px | 0.40 | 0.94 | 228 |
| pressure swell | 12 % → 11 % | 43.7 px | 0.40 | 0.98 | 158 |
| fast wave | 42 % → 34 % | 48.2 px | 0.40 | 0.83 | 590 |
| slow wave | 42 % → 34 % | 48.3 px | 0.40 | 0.82 | 944 |
| spiral | 66 % → 44 % | 43.5 px | 0.40 | 0.67 | 1311 |
| loop | 37 % → 34 % | 48.2 px | 0.40 | 0.91 | 703 |
| tilted | 15 % → 15 % | 42.0 px | 0.40 | 1.01 | 289 |
| over the wet one | 33 % → 32 % | 51.3 px | 0.40 | 0.95 | 303 |
| long, no reload | 81 % → 47 % | 36.3 px | 0.40 | 0.58 | 1451 | quarters: 0.35 → 0.34 → 0.32 → 0.28

Numbers say: light vs heavy: width 59.0 → 59.1 px, dark 0.40 → 0.40; pressure barely changes the width.

## v3 · Any shape · K of hairs
Oil 1.00 · 48 px · 17.9 s

![v3 · Any shape · K of hairs](v3-Any-shape-K-of-hairs.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 18 % → 18 % | 51.8 px | 0.40 | 1.00 | 171 |
| heavy line | 27 % → 27 % | 78.4 px | 0.46 | 1.00 | 164 |
| pressure swell | 16 % → 16 % | 58.4 px | 0.47 | 1.01 | 147 |
| fast wave | 49 % → 51 % | 56.8 px | 0.44 | 1.04 | 389 |
| slow wave | 50 % → 50 % | 57.8 px | 0.48 | 1.00 | 798 |
| spiral | 67 % → 67 % | 44.1 px | 0.45 | 1.00 | 738 |
| loop | 45 % → 45 % | 58.8 px | 0.48 | 1.00 | 394 |
| tilted | 16 % → 16 % | 45.8 px | 0.46 | 1.00 | 236 |
| over the wet one | 39 % → 39 % | 62.3 px | 0.46 | 1.01 | 289 |
| long, no reload | 84 % → 84 % | 37.8 px | 0.43 | 1.00 | 1177 | quarters: 0.48 → 0.46 → 0.33 → 0.26

Numbers say: light vs heavy: width 51.8 → 78.4 px, dark 0.40 → 0.46.

## v3 · Any shape · Star stamp
Gouache 1.00 · 44 px · 37.4 s

![v3 · Any shape · Star stamp](v3-Any-shape-Star-stamp.png)

A light paint: laid on a grey sheet (on white it cannot be seen); **dark** = how far it is from the grey either way.

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 13 % → 11 % | 37.9 px | 0.36 | 0.84 | 122 |
| heavy line | 13 % → 12 % | 38.4 px | 0.36 | 0.87 | 111 |
| pressure swell | 10 % → 10 % | 39.2 px | 0.36 | 0.93 | 107 |
| fast wave | 33 % → 28 % | 38.0 px | 0.36 | 0.84 | 303 |
| slow wave | 33 % → 27 % | 38.4 px | 0.35 | 0.80 | 541 |
| spiral | 56 % → 41 % | 37.2 px | 0.35 | 0.73 | 468 |
| loop | 28 % → 25 % | 36.0 px | 0.36 | 0.88 | 277 |
| tilted | 13 % → 13 % | 37.0 px | 0.36 | 1.01 | 135 |
| over the wet one | 26 % → 24 % | 36.5 px | 0.36 | 0.91 | 102 |
| long, no reload | 68 % → 45 % | 30.4 px | 0.35 | 0.67 | 639 | quarters: 0.01 → 0.01 → 0.01 → 0.01

Numbers say: light vs heavy: width 37.9 → 38.4 px, dark 0.36 → 0.36; pressure barely changes the width; the long stroke does not run out of paint.

## v3 · Any shape · Star of hairs
Oil 1.00 · 44 px · 15.8 s

![v3 · Any shape · Star of hairs](v3-Any-shape-Star-of-hairs.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 15 % → 15 % | 43.7 px | 0.34 | 1.00 | 165 |
| heavy line | 23 % → 23 % | 67.9 px | 0.33 | 1.00 | 178 |
| pressure swell | 14 % → 14 % | 53.1 px | 0.35 | 1.00 | 107 |
| fast wave | 45 % → 46 % | 52.0 px | 0.32 | 1.01 | 427 |
| slow wave | 44 % → 44 % | 50.7 px | 0.33 | 1.00 | 791 |
| spiral | 63 % → 63 % | 41.7 px | 0.32 | 1.00 | 704 |
| loop | 39 % → 39 % | 50.4 px | 0.33 | 1.00 | 282 |
| tilted | 14 % → 14 % | 39.1 px | 0.34 | 1.00 | 183 |
| over the wet one | 34 % → 34 % | 55.5 px | 0.34 | 1.00 | 149 |
| long, no reload | 78 % → 78 % | 35.1 px | 0.30 | 1.00 | 869 | quarters: 0.32 → 0.28 → 0.23 → 0.17

Numbers say: light vs heavy: width 43.7 → 67.9 px, dark 0.34 → 0.33.

## v3 · Any shape · Rag
Oil 1.00 · 60 px · 22.5 s

![v3 · Any shape · Rag](v3-Any-shape-Rag.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 22 % → 25 % | 64.2 px | 0.16 | 1.12 | 168 |
| heavy line | 38 % → 38 % | 111.5 px | 0.29 | 1.00 | 399 |
| pressure swell | 25 % → 26 % | 94.4 px | 0.24 | 1.02 | 161 |
| fast wave | 68 % → 73 % | 78.9 px | 0.26 | 1.07 | 656 |
| slow wave | 71 % → 71 % | 82.3 px | 0.27 | 1.00 | 1195 |
| spiral | 81 % → 81 % | 53.5 px | 0.28 | 1.00 | 998 |
| loop | 61 % → 62 % | 79.6 px | 0.29 | 1.00 | 553 |
| tilted | 22 % → 22 % | 61.1 px | 0.26 | 1.00 | 260 |
| over the wet one | 51 % → 52 % | 80.5 px | 0.26 | 1.03 | 270 |
| long, no reload | 94 % → 94 % | 42.3 px | 0.29 | 1.00 | 1770 | quarters: 0.35 → 0.32 → 0.27 → 0.21

Numbers say: light vs heavy: width 64.2 → 111.5 px, dark 0.16 → 0.29.

## v3 · Any shape · Dry oil on canvas
Oil 1.00 · 40 px · 15.1 s

![v3 · Any shape · Dry oil on canvas](v3-Any-shape-Dry-oil-on-canvas.png)

A light paint: laid on a grey sheet (on white it cannot be seen); **dark** = how far it is from the grey either way.

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 5 % → 5 % | 13.3 px | 0.14 | 1.00 | 80 |
| heavy line | 8 % → 8 % | 23.7 px | 0.35 | 1.00 | 89 |
| pressure swell | 9 % → 9 % | 32.2 px | 0.27 | 1.00 | 80 |
| fast wave | 27 % → 27 % | 31.7 px | 0.25 | 1.00 | 264 |
| slow wave | 26 % → 26 % | 30.5 px | 0.24 | 1.00 | 439 |
| spiral | 45 % → 45 % | 29.7 px | 0.25 | 1.00 | 422 |
| loop | 21 % → 21 % | 27.3 px | 0.24 | 1.00 | 217 |
| tilted | 9 % → 9 % | 26.3 px | 0.24 | 1.00 | 102 |
| over the wet one | 18 % → 18 % | 23.1 px | 0.24 | 1.00 | 88 |
| long, no reload | 41 % → 41 % | 18.2 px | 0.21 | 1.00 | 593 | quarters: 0.00 → 0.00 → 0.00 → 0.00

Numbers say: light vs heavy: width 13.3 → 23.7 px, dark 0.14 → 0.35; the long stroke does not run out of paint.

## v3 · Any shape · Two colours streaks
Oil 1.00 · 44 px · 16.8 s

![v3 · Any shape · Two colours streaks](v3-Any-shape-Two-colours-streaks.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 14 % → 14 % | 39.6 px | 0.35 | 1.00 | 125 |
| heavy line | 16 % → 16 % | 46.1 px | 0.31 | 1.00 | 120 |
| pressure swell | 11 % → 11 % | 42.9 px | 0.39 | 1.00 | 85 |
| fast wave | 37 % → 37 % | 43.1 px | 0.34 | 1.00 | 339 |
| slow wave | 35 % → 35 % | 40.7 px | 0.31 | 1.00 | 524 |
| spiral | 61 % → 61 % | 40.4 px | 0.35 | 1.00 | 541 |
| loop | 32 % → 32 % | 41.1 px | 0.32 | 1.00 | 271 |
| tilted | 13 % → 13 % | 37.2 px | 0.36 | 1.00 | 180 |
| over the wet one | 27 % → 27 % | 39.3 px | 0.36 | 1.00 | 174 |
| long, no reload | 73 % → 73 % | 32.6 px | 0.31 | 1.00 | 969 | quarters: 0.29 → 0.28 → 0.24 → 0.18

Numbers say: light vs heavy: width 39.6 → 46.1 px, dark 0.35 → 0.31.

## Brush Artist · Refs · #01 Henry Ward peach cloud — own sheet
own sheet 600 × 600 · Gouache 1.00 · 44 px · 12.6 s

![Brush Artist · Refs · #01 Henry Ward peach cloud — own sheet](Brush-Artist-Refs-01-Henry-Ward-peach-cloud-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 5 % → 16 % | 15.6 px | 0.53 | 2.97 | 126 |
| stroke 2 | 11 % → 29 % | 35.1 px | 0.54 | 2.71 | 137 |
| stroke 3 | 16 % → 31 % | 45.4 px | 0.54 | 2.00 | 155 |
| stroke 4 | 21 % → 34 % | 68.0 px | 0.54 | 1.63 | 151 |
| stroke 5 | 21 % → 31 % | 60.5 px | 0.54 | 1.48 | 129 |
| stroke 6 | 20 % → 24 % | 61.5 px | 0.54 | 1.21 | 131 |
| stroke 7 | 9 % → 33 % | 22.9 px | 0.53 | 3.58 | 131 |
| stroke 8 | 14 % → 32 % | 34.7 px | 0.53 | 2.28 | 135 |
| stroke 9 | 13 % → 33 % | 33.9 px | 0.53 | 2.47 | 135 |
| stroke 10 | 13 % → 34 % | 35.3 px | 0.53 | 2.57 | 125 |
| stroke 11 | 14 % → 36 % | 40.5 px | 0.54 | 2.53 | 149 |
| stroke 12 | 14 % → 39 % | 42.4 px | 0.54 | 2.76 | 104 |
| stroke 13 | 19 % → 42 % | 54.8 px | 0.54 | 2.23 | 126 |
| stroke 14 | 27 % → 44 % | 77.4 px | 0.54 | 1.63 | 200 |
| stroke 15 | 30 % → 48 % | 88.5 px | 0.53 | 1.60 | 149 |
| stroke 16 | 35 % → 48 % | 104.8 px | 0.53 | 1.39 | 163 |
| stroke 17 | 35 % → 50 % | 98.5 px | 0.53 | 1.41 | 171 |
| stroke 18 | 41 % → 49 % | 117.6 px | 0.53 | 1.21 | 154 |
| stroke 19 | 41 % → 49 % | 116.0 px | 0.54 | 1.18 | 168 |
| stroke 20 | 43 % → 46 % | 123.0 px | 0.54 | 1.07 | 220 |
| stroke 21 | 43 % → 42 % | 125.4 px | 0.54 | 0.96 | 213 |
| stroke 22 | 45 % → 42 % | 131.2 px | 0.54 | 0.94 | 171 |
| stroke 23 | 49 % → 43 % | 139.0 px | 0.54 | 0.88 | 139 |
| stroke 24 | 52 % → 45 % | 156.2 px | 0.54 | 0.86 | 135 |

Numbers say: wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #02 Henry Ward cream strokes — own sheet
own sheet 600 × 600 · Gouache 1.00 · 46 px · 8.8 s

![Brush Artist · Refs · #02 Henry Ward cream strokes — own sheet](Brush-Artist-Refs-02-Henry-Ward-cream-strokes-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 9 % → 2 % | 17.7 px | 0.65 | 0.26 | 213 |
| stroke 2 | 15 % → 6 % | 39.4 px | 0.66 | 0.41 | 208 |
| stroke 3 | 19 % → 22 % | 48.9 px | 0.64 | 1.15 | 199 |
| stroke 4 | 23 % → 22 % | 56.7 px | 0.64 | 0.97 | 277 |
| stroke 5 | 24 % → 27 % | 59.0 px | 0.64 | 1.11 | 289 |
| stroke 6 | 18 % → 16 % | 43.4 px | 0.64 | 0.88 | 283 |
| stroke 7 | 21 % → 10 % | 53.1 px | 0.64 | 0.48 | 252 |

## Brush Artist · Refs · #03 Henry Ward navy contours — own sheet
own sheet 600 × 600 · Impasto 1.00 · 22 px · 3.0 s

![Brush Artist · Refs · #03 Henry Ward navy contours — own sheet](Brush-Artist-Refs-03-Henry-Ward-navy-contours-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 10 % → 15 % | 20.0 px | 0.70 | 1.51 | 139 |
| stroke 2 | 16 % → 19 % | 22.1 px | 0.70 | 1.19 | 127 |
| stroke 3 | 20 % → 20 % | 29.5 px | 0.71 | 0.99 | 191 |
| stroke 4 | 19 % → 17 % | 43.6 px | 0.71 | 0.89 | 178 |

Numbers say: wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #04 Henry Ward grey cloud — own sheet
own sheet 600 × 600 · Gouache 1.00 · 50 px · 11.1 s

![Brush Artist · Refs · #04 Henry Ward grey cloud — own sheet](Brush-Artist-Refs-04-Henry-Ward-grey-cloud-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 5 % → 21 % | 15.7 px | 0.32 | 3.88 | 221 |
| stroke 2 | 14 % → 21 % | 40.2 px | 0.31 | 1.53 | 260 |
| stroke 3 | 21 % → 22 % | 59.7 px | 0.31 | 1.05 | 263 |
| stroke 4 | 27 % → 23 % | 79.5 px | 0.31 | 0.84 | 266 |
| stroke 5 | 27 % → 26 % | 83.3 px | 0.31 | 0.94 | 225 |
| stroke 6 | 33 % → 30 % | 109.0 px | 0.31 | 0.89 | 253 |
| stroke 7 | 34 % → 36 % | 100.8 px | 0.30 | 1.03 | 236 |
| stroke 8 | 38 % → 38 % | 112.6 px | 0.30 | 0.99 | 248 |
| stroke 9 | 32 % → 39 % | 94.9 px | 0.31 | 1.23 | 207 |
| stroke 10 | 33 % → 39 % | 106.9 px | 0.31 | 1.19 | 184 |
| stroke 11 | 34 % → 36 % | 96.9 px | 0.31 | 1.05 | 216 |
| stroke 12 | 32 % → 34 % | 96.3 px | 0.30 | 1.06 | 165 |
| stroke 13 | 27 % → 38 % | 78.1 px | 0.31 | 1.38 | 200 |
| stroke 14 | 34 % → 38 % | 100.7 px | 0.31 | 1.11 | 250 |
| stroke 15 | 35 % → 37 % | 100.1 px | 0.31 | 1.07 | 217 |
| stroke 16 | 38 % → 36 % | 116.5 px | 0.31 | 0.93 | 271 |
| stroke 17 | 39 % → 31 % | 112.7 px | 0.31 | 0.79 | 260 |
| stroke 18 | 40 % → 28 % | 133.2 px | 0.31 | 0.70 | 215 |
| stroke 19 | 38 % → 24 % | 113.0 px | 0.32 | 0.63 | 214 |
| stroke 20 | 40 % → 23 % | 125.2 px | 0.32 | 0.57 | 256 |

Numbers say: wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #05 Henry Ward green in rust loops — own sheet
own sheet 600 × 600 · Impasto 1.00 · 20 px · 2.6 s

![Brush Artist · Refs · #05 Henry Ward green in rust loops — own sheet](Brush-Artist-Refs-05-Henry-Ward-green-in-rust-loops-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 11 % → 16 % | 19.1 px | 0.02 | 1.49 | 120 |
| stroke 2 | 12 % → 10 % | 24.0 px | 0.02 | 0.86 | 162 |
| stroke 3 | 20 % → 17 % | 35.4 px | 0.02 | 0.89 | 145 |

## Brush Artist · Refs · #06 Henry Ward scrubbed grey — own sheet
own sheet 600 × 600 · Gouache 1.00 · 50 px · 12.1 s

![Brush Artist · Refs · #06 Henry Ward scrubbed grey — own sheet](Brush-Artist-Refs-06-Henry-Ward-scrubbed-grey-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 6 % → 24 % | 15.9 px | 0.32 | 3.69 | 226 |
| stroke 2 | 16 % → 25 % | 41.5 px | 0.31 | 1.58 | 236 |
| stroke 3 | 21 % → 23 % | 64.7 px | 0.31 | 1.10 | 198 |
| stroke 4 | 25 % → 24 % | 78.0 px | 0.31 | 0.96 | 254 |
| stroke 5 | 31 % → 30 % | 92.8 px | 0.31 | 0.97 | 251 |
| stroke 6 | 38 % → 31 % | 115.7 px | 0.31 | 0.81 | 240 |
| stroke 7 | 36 % → 35 % | 103.6 px | 0.31 | 0.98 | 216 |
| stroke 8 | 40 % → 36 % | 125.1 px | 0.31 | 0.90 | 240 |
| stroke 9 | 35 % → 37 % | 107.6 px | 0.31 | 1.06 | 209 |
| stroke 10 | 34 % → 38 % | 111.3 px | 0.31 | 1.10 | 206 |
| stroke 11 | 35 % → 37 % | 101.5 px | 0.31 | 1.06 | 266 |
| stroke 12 | 33 % → 35 % | 99.4 px | 0.31 | 1.08 | 189 |
| stroke 13 | 24 % → 37 % | 69.3 px | 0.31 | 1.53 | 221 |
| stroke 14 | 30 % → 39 % | 88.5 px | 0.31 | 1.30 | 246 |
| stroke 15 | 33 % → 44 % | 95.1 px | 0.32 | 1.34 | 205 |
| stroke 16 | 35 % → 45 % | 111.8 px | 0.32 | 1.28 | 261 |
| stroke 17 | 37 % → 42 % | 110.5 px | 0.32 | 1.12 | 174 |
| stroke 18 | 41 % → 40 % | 123.6 px | 0.32 | 0.98 | 228 |
| stroke 19 | 38 % → 35 % | 112.0 px | 0.32 | 0.93 | 188 |
| stroke 20 | 38 % → 34 % | 117.9 px | 0.32 | 0.90 | 324 |
| stroke 21 | 40 % → 30 % | 116.2 px | 0.33 | 0.75 | 216 |
| stroke 22 | 39 % → 28 % | 127.1 px | 0.33 | 0.73 | 184 |

Numbers say: wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #07 Henry Ward blue L + black zigzag — own sheet
own sheet 600 × 600 · Impasto 1.00 · 34 px · 2.2 s

![Brush Artist · Refs · #07 Henry Ward blue L + black zigzag — own sheet](Brush-Artist-Refs-07-Henry-Ward-blue-L-black-zigzag-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 13 % → 15 % | 31.2 px | 0.58 | 1.09 | 146 |
| stroke 2 | 15 % → 14 % | 37.7 px | 0.58 | 0.90 | 75 |

## Brush Artist · Refs · #08 Henry Ward olive bands — own sheet
own sheet 600 × 600 · Gouache 1.00 · 34 px · 5.6 s

![Brush Artist · Refs · #08 Henry Ward olive bands — own sheet](Brush-Artist-Refs-08-Henry-Ward-olive-bands-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 8 % → 4 % | 15.7 px | 0.58 | 0.53 | 158 |
| stroke 2 | 12 % → 4 % | 28.0 px | 0.58 | 0.35 | 153 |
| stroke 3 | 13 % → 11 % | 27.5 px | 0.58 | 0.87 | 213 |
| stroke 4 | 17 % → 10 % | 37.3 px | 0.58 | 0.57 | 263 |
| stroke 5 | 22 % → 13 % | 45.2 px | 0.56 | 0.59 | 210 |
| stroke 6 | 16 % → 6 % | 30.5 px | 0.54 | 0.40 | 226 |

## Brush Artist · Refs · #09 Henry Ward white loops — own sheet
own sheet 600 × 600 · Gouache 1.00 · 46 px · 6.9 s

![Brush Artist · Refs · #09 Henry Ward white loops — own sheet](Brush-Artist-Refs-09-Henry-Ward-white-loops-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 23 % → 0 % | 12.1 px | 0.06 | 0.00 | 952 |
| stroke 2 | 27 % → 0 % | 27.4 px | 0.07 | 0.00 | 1166 |
| stroke 3 | 34 % → 0 % | 31.4 px | 0.07 | 0.00 | 1245 |
| stroke 4 | 8 % → 0 % | 18.4 px | 0.00 | 0.00 | 184 |
| stroke 5 | 5 % → 0 % | 14.8 px | 0.06 | 0.00 | 157 |
| stroke 6 | 5 % → 0 % | 13.8 px | 0.08 | 0.00 | 153 |
| stroke 7 | 10 % → 0 % | 26.8 px | 0.08 | 0.00 | 150 |
| stroke 8 | 5 % → 0 % | 8.2 px | 0.00 | 0.00 | 184 |

## Brush Artist · Refs · #10 Henry Ward maroon loops — own sheet
own sheet 600 × 600 · Impasto 1.00 · 30 px · 3.5 s

![Brush Artist · Refs · #10 Henry Ward maroon loops — own sheet](Brush-Artist-Refs-10-Henry-Ward-maroon-loops-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 12 % → 26 % | 28.9 px | 0.72 | 2.25 | 248 |
| stroke 2 | 23 % → 39 % | 51.0 px | 0.72 | 1.74 | 167 |
| stroke 3 | 30 % → 36 % | 59.6 px | 0.72 | 1.20 | 184 |
| stroke 4 | 40 % → 38 % | 91.4 px | 0.72 | 0.94 | 126 |
| stroke 5 | 33 % → 29 % | 82.1 px | 0.71 | 0.89 | 185 |

Numbers say: wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #11 Henry Ward purple spun balls — own sheet
own sheet 600 × 600 · Impasto 1.00 · 36 px · 2.7 s

![Brush Artist · Refs · #11 Henry Ward purple spun balls — own sheet](Brush-Artist-Refs-11-Henry-Ward-purple-spun-balls-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 22 % → 31 % | 24.4 px | 0.69 | 1.42 | 239 |
| stroke 2 | 31 % → 44 % | 34.3 px | 0.69 | 1.39 | 232 |
| stroke 3 | 34 % → 33 % | 37.7 px | 0.69 | 0.97 | 259 |

## Brush Artist · Refs · #12 Henry Ward black-olive cage — own sheet
own sheet 600 × 600 · Gouache 1.00 · 28 px · 5.0 s

![Brush Artist · Refs · #12 Henry Ward black-olive cage — own sheet](Brush-Artist-Refs-12-Henry-Ward-black-olive-cage-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 9 % → 10 % | 17.0 px | 0.58 | 1.15 | 214 |
| stroke 2 | 7 % → 10 % | 15.8 px | 0.58 | 1.46 | 168 |
| stroke 3 | 18 % → 13 % | 28.0 px | 0.58 | 0.72 | 219 |
| stroke 4 | 20 % → 14 % | 39.4 px | 0.59 | 0.70 | 138 |
| stroke 5 | 18 % → 7 % | 33.8 px | 0.58 | 0.40 | 150 |
| stroke 6 | 29 % → 15 % | 54.8 px | 0.58 | 0.52 | 192 |

## Brush Artist · Refs · #13 Henry Ward blue streaky form — own sheet
own sheet 600 × 600 · Gouache 1.00 · 50 px · 8.8 s

![Brush Artist · Refs · #13 Henry Ward blue streaky form — own sheet](Brush-Artist-Refs-13-Henry-Ward-blue-streaky-form-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 5 % → 0 % | 15.9 px | 0.00 | 0.00 | 139 |
| stroke 2 | 13 % → 0 % | 40.6 px | 0.00 | 0.00 | 200 |
| stroke 3 | 22 % → 0 % | 62.3 px | 0.00 | 0.00 | 192 |
| stroke 4 | 24 % → 0 % | 78.4 px | 0.00 | 0.00 | 218 |
| stroke 5 | 31 % → 0 % | 90.1 px | 0.00 | 0.00 | 221 |
| stroke 6 | 37 % → 0 % | 105.3 px | 0.00 | 0.00 | 203 |
| stroke 7 | 36 % → 0 % | 107.2 px | 0.00 | 0.00 | 198 |
| stroke 8 | 40 % → 0 % | 120.3 px | 0.00 | 0.00 | 207 |
| stroke 9 | 33 % → 0 % | 102.9 px | 0.00 | 0.00 | 168 |
| stroke 10 | 32 % → 0 % | 105.4 px | 0.00 | 0.00 | 160 |
| stroke 11 | 30 % → 0 % | 92.1 px | 0.00 | 0.00 | 183 |
| stroke 12 | 26 % → 0 % | 78.3 px | 0.00 | 0.00 | 169 |
| stroke 13 | 24 % → 0 % | 74.8 px | 0.00 | 0.00 | 165 |
| stroke 14 | 29 % → 0 % | 84.9 px | 0.00 | 0.00 | 229 |
| stroke 15 | 30 % → 0 % | 86.3 px | 0.00 | 0.00 | 187 |
| stroke 16 | 35 % → 0 % | 104.8 px | 0.00 | 0.00 | 217 |
| stroke 17 | 41 % → 0 % | 103.0 px | 0.00 | 0.00 | 182 |
| stroke 18 | 49 % → 0 % | 117.7 px | 0.00 | 0.00 | 209 |
| stroke 19 | 51 % → 0 % | 104.2 px | 0.00 | 0.00 | 208 |
| stroke 20 | 60 % → 0 % | 115.5 px | 0.00 | 0.00 | 215 |
| stroke 21 | 7 % → 0 % | 15.0 px | 0.00 | 0.00 | 183 |
| stroke 22 | 6 % → 0 % | 18.5 px | 0.00 | 0.00 | 159 |
| stroke 23 | 11 % → 0 % | 35.1 px | 0.00 | 0.00 | 192 |
| stroke 24 | 4 % → 0 % | 11.0 px | 0.00 | 0.00 | 145 |
| stroke 25 | 4 % → 0 % | 9.1 px | 0.00 | 0.00 | 128 |

## Brush Artist · Refs · #14 Henry Ward olive totem — own sheet
own sheet 600 × 600 · Impasto 1.00 · 48 px · 6.8 s

![Brush Artist · Refs · #14 Henry Ward olive totem — own sheet](Brush-Artist-Refs-14-Henry-Ward-olive-totem-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 18 % → 46 % | 46.6 px | 0.38 | 2.57 | 133 |
| stroke 2 | 20 % → 50 % | 61.7 px | 0.38 | 2.53 | 136 |
| stroke 3 | 27 % → 52 % | 93.9 px | 0.39 | 1.89 | 169 |
| stroke 4 | 30 % → 54 % | 110.9 px | 0.39 | 1.82 | 148 |
| stroke 5 | 38 % → 63 % | 134.1 px | 0.39 | 1.64 | 131 |
| stroke 6 | 38 % → 64 % | 149.8 px | 0.39 | 1.67 | 135 |
| stroke 7 | 35 % → 60 % | 119.1 px | 0.39 | 1.70 | 133 |
| stroke 8 | 37 % → 62 % | 141.6 px | 0.39 | 1.67 | 131 |
| stroke 9 | 38 % → 62 % | 131.6 px | 0.39 | 1.64 | 143 |
| stroke 10 | 37 % → 61 % | 136.5 px | 0.39 | 1.65 | 144 |
| stroke 11 | 38 % → 64 % | 136.7 px | 0.39 | 1.66 | 121 |
| stroke 12 | 38 % → 64 % | 143.5 px | 0.38 | 1.68 | 152 |
| stroke 13 | 37 % → 66 % | 129.3 px | 0.39 | 1.78 | 122 |
| stroke 14 | 36 % → 61 % | 131.1 px | 0.39 | 1.70 | 162 |
| stroke 15 | 39 % → 65 % | 134.4 px | 0.39 | 1.66 | 126 |
| stroke 16 | 38 % → 63 % | 136.6 px | 0.39 | 1.67 | 227 |
| stroke 17 | 37 % → 61 % | 124.1 px | 0.39 | 1.64 | 148 |
| stroke 18 | 40 % → 65 % | 152.2 px | 0.39 | 1.63 | 143 |
| stroke 19 | 38 % → 58 % | 131.3 px | 0.39 | 1.54 | 137 |
| stroke 20 | 40 % → 53 % | 142.6 px | 0.39 | 1.31 | 164 |
| stroke 21 | 46 % → 53 % | 136.0 px | 0.39 | 1.15 | 140 |
| stroke 22 | 53 % → 51 % | 143.0 px | 0.39 | 0.97 | 143 |

Numbers say: wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #15 Ultramarine brush script — own sheet
own sheet 600 × 600 · Ink 1.00 · 4 px · 7.9 s

![Brush Artist · Refs · #15 Ultramarine brush script — own sheet](Brush-Artist-Refs-15-Ultramarine-brush-script-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 40 % → 42 % | 9.0 px | 0.65 | 1.05 | 50 |
| stroke 2 | 41 % → 43 % | 9.0 px | 0.67 | 1.07 | 53 |
| stroke 3 | 39 % → 42 % | 9.4 px | 0.72 | 1.08 | 25 |
| stroke 4 | 42 % → 46 % | 10.2 px | 0.74 | 1.10 | 15 |
| stroke 5 | 46 % → 49 % | 10.1 px | 0.72 | 1.06 | 22 |
| stroke 6 | 43 % → 45 % | 9.7 px | 0.65 | 1.05 | 45 |
| stroke 7 | 44 % → 47 % | 9.3 px | 0.72 | 1.08 | 28 |
| stroke 8 | 37 % → 39 % | 8.9 px | 0.65 | 1.06 | 38 |
| stroke 9 | 39 % → 42 % | 9.1 px | 0.70 | 1.07 | 42 |
| stroke 10 | 35 % → 37 % | 9.6 px | 0.66 | 1.05 | 45 |
| stroke 11 | 44 % → 47 % | 9.9 px | 0.69 | 1.06 | 35 |
| stroke 12 | 39 % → 41 % | 9.4 px | 0.65 | 1.06 | 45 |
| stroke 13 | 45 % → 46 % | 10.1 px | 0.69 | 1.04 | 21 |
| stroke 14 | 37 % → 40 % | 9.6 px | 0.71 | 1.07 | 26 |
| stroke 15 | 37 % → 38 % | 9.0 px | 0.67 | 1.05 | 39 |
| stroke 16 | 42 % → 45 % | 9.4 px | 0.70 | 1.06 | 28 |
| stroke 17 | 41 % → 45 % | 7.1 px | 0.71 | 1.09 | 35 |
| stroke 18 | 43 % → 45 % | 9.3 px | 0.73 | 1.05 | 26 |
| stroke 19 | 40 % → 42 % | 9.0 px | 0.65 | 1.06 | 51 |
| stroke 20 | 42 % → 44 % | 9.7 px | 0.69 | 1.06 | 34 |
| stroke 21 | 39 % → 42 % | 9.6 px | 0.69 | 1.07 | 32 |
| stroke 22 | 44 % → 46 % | 8.9 px | 0.65 | 1.06 | 56 |
| stroke 23 | 38 % → 42 % | 9.5 px | 0.72 | 1.10 | 22 |
| stroke 24 | 39 % → 42 % | 9.1 px | 0.73 | 1.06 | 28 |
| stroke 25 | 41 % → 44 % | 10.0 px | 0.71 | 1.06 | 28 |
| stroke 26 | 45 % → 47 % | 9.1 px | 0.66 | 1.04 | 33 |
| stroke 27 | 43 % → 45 % | 9.0 px | 0.62 | 1.05 | 51 |
| stroke 28 | 45 % → 47 % | 9.3 px | 0.70 | 1.06 | 36 |
| stroke 29 | 35 % → 38 % | 10.4 px | 0.69 | 1.08 | 16 |
| stroke 30 | 39 % → 40 % | 8.5 px | 0.70 | 1.04 | 30 |
| stroke 31 | 43 % → 46 % | 10.4 px | 0.74 | 1.07 | 13 |
| stroke 32 | 41 % → 45 % | 9.3 px | 0.70 | 1.09 | 22 |
| stroke 33 | 35 % → 40 % | 10.9 px | 0.73 | 1.13 | 19 |
| stroke 34 | 41 % → 45 % | 10.1 px | 0.74 | 1.09 | 23 |
| stroke 35 | 36 % → 38 % | 9.4 px | 0.67 | 1.06 | 45 |

## Brush Artist · Refs · #18 Blue oil-stick scribbles — own sheet
own sheet 600 × 600 · Pastel 1.00 · 10 px · 2.7 s

![Brush Artist · Refs · #18 Blue oil-stick scribbles — own sheet](Brush-Artist-Refs-18-Blue-oil-stick-scribbles-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 16 % → 32 % | 3.9 px | 0.49 | 2.03 | 129 |
| stroke 2 | 13 % → 37 % | 3.6 px | 0.49 | 2.75 | 117 |
| stroke 3 | 16 % → 26 % | 5.8 px | 0.49 | 1.64 | 150 |
| stroke 4 | 15 % → 29 % | 7.9 px | 0.49 | 1.91 | 167 |
| stroke 5 | 29 % → 34 % | 8.5 px | 0.49 | 1.18 | 144 |
| stroke 6 | 26 % → 26 % | 9.4 px | 0.49 | 1.02 | 133 |
| stroke 7 | 26 % → 32 % | 8.4 px | 0.49 | 1.24 | 148 |
| stroke 8 | 30 % → 30 % | 17.0 px | 0.49 | 1.00 | 156 |

Numbers say: wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #20 Orange-red crayon scribble — own sheet
own sheet 600 × 600 · Pastel 1.00 · 14 px · 2.7 s

![Brush Artist · Refs · #20 Orange-red crayon scribble — own sheet](Brush-Artist-Refs-20-Orange-red-crayon-scribble-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 8 % → 19 % | 5.5 px | 0.59 | 2.47 | 178 |
| stroke 2 | 9 % → 22 % | 6.6 px | 0.60 | 2.50 | 158 |
| stroke 3 | 13 % → 21 % | 8.3 px | 0.60 | 1.65 | 153 |
| stroke 4 | 24 % → 32 % | 8.8 px | 0.60 | 1.36 | 150 |
| stroke 5 | 28 % → 28 % | 7.9 px | 0.59 | 1.00 | 152 |
| stroke 6 | 22 % → 22 % | 16.4 px | 0.60 | 1.00 | 167 |

Numbers say: wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #21 Gritty black contours — own sheet
own sheet 600 × 600 · Gouache 1.00 · 12 px · 3.8 s

![Brush Artist · Refs · #21 Gritty black contours — own sheet](Brush-Artist-Refs-21-Gritty-black-contours-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 6 % → 4 % | 6.2 px | 0.36 | 0.68 | 130 |
| stroke 2 | 5 % → 2 % | 7.9 px | 0.36 | 0.47 | 166 |
| stroke 3 | 9 % → 2 % | 7.8 px | 0.37 | 0.17 | 116 |
| stroke 4 | 9 % → 3 % | 10.9 px | 0.36 | 0.36 | 122 |
| stroke 5 | 10 % → 4 % | 12.7 px | 0.35 | 0.35 | 101 |

## Brush Artist · Refs · #22 Bold black brush poster — own sheet
own sheet 600 × 600 · Ink 1.00 · 20 px · 4.7 s

![Brush Artist · Refs · #22 Bold black brush poster — own sheet](Brush-Artist-Refs-22-Bold-black-brush-poster-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 24 % → 28 % | 38.8 px | 0.95 | 1.18 | 101 |
| stroke 2 | 28 % → 39 % | 42.9 px | 0.94 | 1.38 | 25 |
| stroke 3 | 30 % → 30 % | 46.0 px | 0.94 | 1.00 | 41 |
| stroke 4 | 30 % → 41 % | 57.8 px | 0.94 | 1.41 | 53 |
| stroke 5 | 27 % → 27 % | 46.3 px | 0.93 | 1.00 | 74 |

## Brush Artist · Refs · #23 Dry white on orange + black line — own sheet
own sheet 600 × 600 · Gouache 1.00 · 50 px · 8.2 s

![Brush Artist · Refs · #23 Dry white on orange + black line — own sheet](Brush-Artist-Refs-23-Dry-white-on-orange-black-line-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 4 % → 11 % | 14.5 px | 0.38 | 2.70 | 121 |
| stroke 2 | 8 % → 10 % | 26.7 px | 0.38 | 1.35 | 147 |
| stroke 3 | 13 % → 11 % | 49.0 px | 0.38 | 0.81 | 129 |
| stroke 4 | 17 % → 12 % | 68.6 px | 0.38 | 0.67 | 148 |
| stroke 5 | 23 % → 13 % | 85.0 px | 0.38 | 0.55 | 149 |
| stroke 6 | 26 % → 14 % | 106.9 px | 0.38 | 0.53 | 169 |
| stroke 7 | 23 % → 13 % | 86.4 px | 0.38 | 0.57 | 120 |
| stroke 8 | 22 % → 12 % | 87.4 px | 0.38 | 0.53 | 161 |
| stroke 9 | 19 % → 11 % | 69.7 px | 0.38 | 0.60 | 123 |
| stroke 10 | 18 % → 11 % | 68.9 px | 0.38 | 0.63 | 135 |
| stroke 11 | 20 % → 11 % | 73.3 px | 0.38 | 0.56 | 161 |
| stroke 12 | 19 % → 12 % | 72.9 px | 0.38 | 0.65 | 131 |
| stroke 13 | 20 % → 14 % | 75.6 px | 0.38 | 0.70 | 213 |
| stroke 14 | 21 % → 14 % | 84.0 px | 0.38 | 0.64 | 194 |
| stroke 15 | 21 % → 13 % | 79.6 px | 0.38 | 0.62 | 130 |
| stroke 16 | 22 % → 11 % | 87.4 px | 0.38 | 0.52 | 148 |
| stroke 17 | 22 % → 9 % | 76.2 px | 0.38 | 0.40 | 141 |
| stroke 18 | 27 % → 9 % | 99.3 px | 0.38 | 0.34 | 141 |

Numbers say: wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #24 Picasso flat oil — own sheet
own sheet 600 × 600 · Oil 0.89 · Oil glaze 0.11 · 34 px · 5.3 s

![Brush Artist · Refs · #24 Picasso flat oil — own sheet](Brush-Artist-Refs-24-Picasso-flat-oil-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 14 % → 44 % | 30.0 px | 0.22 | 3.11 | 122 |
| stroke 2 | 19 % → 47 % | 44.5 px | 0.23 | 2.49 | 118 |
| stroke 3 | 27 % → 56 % | 59.7 px | 0.23 | 2.06 | 130 |
| stroke 4 | 37 % → 62 % | 82.9 px | 0.23 | 1.69 | 132 |
| stroke 5 | 41 % → 68 % | 91.2 px | 0.22 | 1.64 | 127 |
| stroke 6 | 42 % → 63 % | 96.5 px | 0.22 | 1.52 | 251 |
| stroke 7 | 42 % → 63 % | 87.5 px | 0.23 | 1.51 | 131 |
| stroke 8 | 42 % → 63 % | 101.6 px | 0.23 | 1.50 | 144 |
| stroke 9 | 34 % → 60 % | 74.4 px | 0.23 | 1.76 | 154 |
| stroke 10 | 38 % → 58 % | 89.8 px | 0.23 | 1.55 | 127 |
| stroke 11 | 35 % → 56 % | 74.6 px | 0.24 | 1.61 | 131 |
| stroke 12 | 37 % → 58 % | 88.3 px | 0.24 | 1.56 | 142 |
| stroke 13 | 35 % → 64 % | 77.9 px | 0.25 | 1.81 | 145 |
| stroke 14 | 36 % → 66 % | 82.0 px | 0.24 | 1.82 | 142 |
| stroke 15 | 36 % → 60 % | 76.0 px | 0.24 | 1.67 | 136 |
| stroke 16 | 36 % → 52 % | 83.2 px | 0.24 | 1.46 | 133 |
| stroke 17 | 41 % → 47 % | 86.1 px | 0.24 | 1.15 | 142 |
| stroke 18 | 42 % → 42 % | 101.0 px | 0.24 | 1.00 | 138 |

Numbers say: wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #25 Yellow heavy flat stroke — own sheet
own sheet 600 × 600 · Impasto 1.00 · 110 px · 2.7 s

![Brush Artist · Refs · #25 Yellow heavy flat stroke — own sheet](Brush-Artist-Refs-25-Yellow-heavy-flat-stroke-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 18 % → 18 % | 103.7 px | 0.16 | 0.98 | 650 |

## Brush Artist · Refs · #27 Orange impasto swatch — own sheet
own sheet 600 × 600 · Impasto 1.00 · 60 px · 3.0 s

![Brush Artist · Refs · #27 Orange impasto swatch — own sheet](Brush-Artist-Refs-27-Orange-impasto-swatch-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 8 % → 21 % | 58.4 px | 0.32 | 2.66 | 59 |
| stroke 2 | 7 % → 33 % | 62.2 px | 0.32 | 4.61 | 46 |
| stroke 3 | 25 % → 34 % | 238.0 px | 0.32 | 1.41 | 36 |
| stroke 4 | 10 % → 12 % | 69.5 px | 0.34 | 1.26 | 64 |
| stroke 5 | 17 % → 32 % | 61.8 px | 0.31 | 1.90 | 65 |
| stroke 6 | 17 % → 31 % | 143.7 px | 0.32 | 1.77 | 54 |
| stroke 7 | 8 % → 14 % | 68.6 px | 0.31 | 1.88 | 46 |
| stroke 8 | 32 % → 33 % | 328.8 px | 0.32 | 1.04 | 45 |
| stroke 9 | 37 % → 36 % | 182.9 px | 0.32 | 0.97 | 73 |
| stroke 10 | 33 % → 32 % | 298.6 px | 0.32 | 0.97 | 50 |

Numbers say: wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #28 Miles Davis black lines — own sheet
own sheet 600 × 600 · Ink 1.00 · 22 px · 6.2 s

![Brush Artist · Refs · #28 Miles Davis black lines — own sheet](Brush-Artist-Refs-28-Miles-Davis-black-lines-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 22 % → 31 % | 36.1 px | 0.88 | 1.42 | 157 |
| stroke 2 | 26 % → 47 % | 35.8 px | 0.88 | 1.79 | 122 |
| stroke 3 | 38 % → 42 % | 73.3 px | 0.88 | 1.11 | 91 |
| stroke 4 | 41 % → 47 % | 81.4 px | 0.88 | 1.16 | 140 |
| stroke 5 | 54 % → 54 % | 108.2 px | 0.88 | 1.00 | 121 |

Numbers say: wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #29 Shrigley magenta asterisk — own sheet
own sheet 600 × 600 · Watercolour 1.00 · 70 px · 6.3 s

![Brush Artist · Refs · #29 Shrigley magenta asterisk — own sheet](Brush-Artist-Refs-29-Shrigley-magenta-asterisk-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 13 % → 37 % | 46.6 px | 0.67 | 2.86 | 176 |
| stroke 2 | 12 % → 12 % | 87.1 px | 0.67 | 1.00 | 175 |
| stroke 3 | 28 % → 37 % | 100.9 px | 0.67 | 1.31 | 165 |
| stroke 4 | 23 % → 23 % | 164.0 px | 0.67 | 1.02 | 188 |

Numbers say: wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #30 Red gouache face patch — own sheet
own sheet 600 × 600 · Gouache 1.00 · 60 px · 12.5 s

![Brush Artist · Refs · #30 Red gouache face patch — own sheet](Brush-Artist-Refs-30-Red-gouache-face-patch-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 11 % → 37 % | 50.6 px | 0.54 | 3.29 | 152 |
| stroke 2 | 15 % → 41 % | 74.2 px | 0.54 | 2.74 | 151 |
| stroke 3 | 24 % → 50 % | 115.1 px | 0.54 | 2.08 | 197 |
| stroke 4 | 26 % → 52 % | 133.4 px | 0.54 | 1.95 | 206 |
| stroke 5 | 34 % → 60 % | 160.6 px | 0.54 | 1.77 | 169 |
| stroke 6 | 35 % → 61 % | 178.6 px | 0.54 | 1.76 | 179 |
| stroke 7 | 35 % → 59 % | 164.2 px | 0.54 | 1.70 | 232 |
| stroke 8 | 34 % → 56 % | 162.3 px | 0.54 | 1.66 | 266 |
| stroke 9 | 36 % → 60 % | 172.7 px | 0.53 | 1.66 | 317 |
| stroke 10 | 38 % → 62 % | 196.7 px | 0.53 | 1.64 | 224 |
| stroke 11 | 37 % → 61 % | 181.6 px | 0.53 | 1.67 | 191 |
| stroke 12 | 36 % → 58 % | 179.8 px | 0.53 | 1.60 | 196 |
| stroke 13 | 33 % → 46 % | 157.0 px | 0.53 | 1.38 | 202 |
| stroke 14 | 33 % → 41 % | 159.9 px | 0.53 | 1.24 | 271 |
| stroke 15 | 33 % → 37 % | 153.6 px | 0.53 | 1.12 | 203 |
| stroke 16 | 39 % → 39 % | 186.3 px | 0.53 | 0.98 | 193 |

Numbers say: wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #31 Warhol blotted line — own sheet
own sheet 600 × 600 · Ink 1.00 · 6 px · 5.1 s

![Brush Artist · Refs · #31 Warhol blotted line — own sheet](Brush-Artist-Refs-31-Warhol-blotted-line-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 22 % → 43 % | 16.5 px | 0.83 | 1.94 | 89 |
| stroke 2 | 17 % → 23 % | 15.7 px | 0.81 | 1.35 | 65 |
| stroke 3 | 24 % → 25 % | 24.9 px | 0.81 | 1.03 | 66 |
| stroke 4 | 32 % → 41 % | 32.7 px | 0.83 | 1.28 | 46 |
| stroke 5 | 37 % → 45 % | 38.1 px | 0.83 | 1.21 | 86 |
| stroke 6 | 34 % → 35 % | 27.8 px | 0.81 | 1.03 | 99 |

Numbers say: wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #32 Thick orange swipes — own sheet
own sheet 600 × 600 · Impasto 1.00 · 90 px · 4.1 s

![Brush Artist · Refs · #32 Thick orange swipes — own sheet](Brush-Artist-Refs-32-Thick-orange-swipes-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 14 % → 27 % | 86.6 px | 0.02 | 1.89 | 314 |
| stroke 2 | 26 % → 37 % | 177.9 px | 0.02 | 1.41 | 357 |
| stroke 3 | 27 % → 27 % | 176.1 px | 0.02 | 0.98 | 430 |

Numbers say: wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #33 Red wet-in-wet band — own sheet
own sheet 600 × 600 · Watercolour 1.00 · 80 px · 11.0 s

![Brush Artist · Refs · #33 Red wet-in-wet band — own sheet](Brush-Artist-Refs-33-Red-wet-in-wet-band-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 22 % → 57 % | 83.4 px | 0.61 | 2.61 | 372 |
| stroke 2 | 28 % → 51 % | 228.4 px | 0.62 | 1.82 | 202 |
| stroke 3 | 34 % → 53 % | 330.0 px | 0.61 | 1.57 | 117 |
| stroke 4 | 40 % → 60 % | 389.9 px | 0.62 | 1.51 | 116 |
| stroke 5 | 40 % → 55 % | 339.4 px | 0.61 | 1.38 | 128 |
| stroke 6 | 41 % → 48 % | 310.3 px | 0.59 | 1.18 | 155 |

Numbers say: wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #34 Magenta oil patches — own sheet
own sheet 600 × 600 · Oil 0.89 · Oil glaze 0.11 · 60 px · 4.1 s

![Brush Artist · Refs · #34 Magenta oil patches — own sheet](Brush-Artist-Refs-34-Magenta-oil-patches-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 8 % → 39 % | 57.1 px | 0.13 | 4.77 | 142 |
| stroke 2 | 8 % → 28 % | 56.8 px | 0.14 | 3.32 | 115 |
| stroke 3 | 7 % → 32 % | 58.6 px | 0.13 | 4.60 | 96 |
| stroke 4 | 15 % → 19 % | 122.2 px | 0.12 | 1.26 | 69 |
| stroke 5 | 21 % → 30 % | 112.2 px | 0.13 | 1.45 | 184 |
| stroke 6 | 19 % → 36 % | 159.7 px | 0.13 | 1.91 | 109 |
| stroke 7 | 28 % → 33 % | 226.6 px | 0.13 | 1.17 | 99 |
| stroke 8 | 30 % → 37 % | 213.6 px | 0.13 | 1.21 | 100 |
| stroke 9 | 23 % → 25 % | 147.9 px | 0.14 | 1.07 | 110 |
| stroke 10 | 27 % → 27 % | 240.6 px | 0.14 | 1.00 | 78 |
| stroke 11 | 33 % → 33 % | 297.2 px | 0.13 | 1.00 | 74 |
| stroke 12 | 24 % → 24 % | 173.6 px | 0.13 | 1.00 | 72 |

Numbers say: wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #35 Red band with runs — own sheet
own sheet 600 × 600 · Watercolour 1.00 · 70 px · 8.5 s

![Brush Artist · Refs · #35 Red band with runs — own sheet](Brush-Artist-Refs-35-Red-band-with-runs-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 37 % → 47 % | 140.3 px | 0.45 | 1.27 | 489 |

## Brush Artist · Refs · #36 Magenta letters flat brush — own sheet
own sheet 600 × 600 · Gouache 1.00 · 36 px · 11.2 s

![Brush Artist · Refs · #36 Magenta letters flat brush — own sheet](Brush-Artist-Refs-36-Magenta-letters-flat-brush-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 20 % → 38 % | 58.3 px | 0.50 | 1.95 | 34 |
| stroke 2 | 20 % → 31 % | 45.2 px | 0.51 | 1.54 | 38 |
| stroke 3 | 28 % → 52 % | 84.6 px | 0.50 | 1.83 | 39 |
| stroke 4 | 26 % → 44 % | 50.3 px | 0.51 | 1.69 | 134 |
| stroke 5 | 33 % → 54 % | 96.3 px | 0.50 | 1.63 | 87 |
| stroke 6 | 43 % → 56 % | 246.0 px | 0.49 | 1.30 | 18 |
| stroke 7 | 30 % → 43 % | 56.6 px | 0.50 | 1.43 | 121 |
| stroke 8 | 31 % → 52 % | 97.7 px | 0.51 | 1.66 | 89 |
| stroke 9 | 38 % → 50 % | 158.2 px | 0.51 | 1.31 | 30 |
| stroke 10 | 37 % → 62 % | 107.5 px | 0.50 | 1.68 | 101 |
| stroke 11 | 39 % → 61 % | 225.6 px | 0.49 | 1.55 | 16 |
| stroke 12 | 44 % → 55 % | 82.9 px | 0.50 | 1.26 | 118 |
| stroke 13 | 31 % → 45 % | 113.5 px | 0.51 | 1.43 | 54 |
| stroke 14 | 34 % → 50 % | 129.9 px | 0.51 | 1.47 | 40 |
| stroke 15 | 36 % → 54 % | 105.5 px | 0.50 | 1.49 | 75 |
| stroke 16 | 39 % → 47 % | 221.7 px | 0.50 | 1.23 | 20 |
| stroke 17 | 43 % → 51 % | 81.6 px | 0.50 | 1.18 | 135 |
| stroke 18 | 26 % → 35 % | 95.6 px | 0.50 | 1.34 | 36 |
| stroke 19 | 39 % → 37 % | 112.8 px | 0.50 | 0.97 | 36 |
| stroke 20 | 45 % → 44 % | 129.9 px | 0.51 | 0.98 | 37 |
| stroke 21 | 40 % → 38 % | 78.2 px | 0.50 | 0.94 | 105 |

Numbers say: wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #37 Oil still life dabs — own sheet
own sheet 600 × 600 · Oil 0.89 · Oil glaze 0.11 · 40 px · 2.7 s

![Brush Artist · Refs · #37 Oil still life dabs — own sheet](Brush-Artist-Refs-37-Oil-still-life-dabs-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 6 % → 6 % | 38.2 px | 0.37 | 1.00 | 29 |
| stroke 2 | 6 % → 26 % | 39.8 px | 0.40 | 4.69 | 25 |
| stroke 3 | 11 % → 33 % | 86.6 px | 0.39 | 3.00 | 19 |
| stroke 4 | 8 % → 8 % | 39.3 px | 0.37 | 1.00 | 46 |
| stroke 5 | 6 % → 10 % | 43.2 px | 0.38 | 1.67 | 26 |
| stroke 6 | 13 % → 29 % | 80.2 px | 0.40 | 2.26 | 37 |
| stroke 7 | 11 % → 22 % | 113.9 px | 0.38 | 2.08 | 17 |
| stroke 8 | 8 % → 13 % | 85.3 px | 0.38 | 1.59 | 13 |
| stroke 9 | 12 % → 13 % | 61.1 px | 0.36 | 1.12 | 35 |
| stroke 10 | 20 % → 24 % | 100.4 px | 0.40 | 1.20 | 44 |
| stroke 11 | 23 % → 27 % | 194.4 px | 0.41 | 1.15 | 19 |
| stroke 12 | 20 % → 20 % | 212.5 px | 0.39 | 1.00 | 15 |
| stroke 13 | 15 % → 15 % | 150.5 px | 0.42 | 1.00 | 18 |
| stroke 14 | 15 % → 15 % | 121.2 px | 0.38 | 1.00 | 23 |

Numbers say: wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #38 Sanguine drawing — own sheet
own sheet 600 × 600 · Pastel 1.00 · 6 px · 2.2 s

![Brush Artist · Refs · #38 Sanguine drawing — own sheet](Brush-Artist-Refs-38-Sanguine-drawing-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 3 % → 15 % | 3.3 px | 0.57 | 4.99 | 4 |
| stroke 2 | 3 % → 8 % | 2.9 px | 0.57 | 3.03 | 9 |
| stroke 3 | 3 % → 9 % | 3.3 px | 0.57 | 3.13 | 3 |
| stroke 4 | 2 % → 18 % | 2.8 px | 0.57 | 7.17 | 7 |
| stroke 5 | 3 % → 7 % | 2.9 px | 0.57 | 2.87 | 5 |
| stroke 6 | 3 % → 19 % | 3.5 px | 0.57 | 6.36 | 3 |
| stroke 7 | 5 % → 15 % | 5.3 px | 0.57 | 3.13 | 8 |
| stroke 8 | 4 % → 16 % | 4.8 px | 0.57 | 3.71 | 7 |
| stroke 9 | 3 % → 8 % | 3.4 px | 0.57 | 2.52 | 3 |
| stroke 10 | 4 % → 16 % | 4.9 px | 0.57 | 3.75 | 6 |
| stroke 11 | 3 % → 4 % | 3.0 px | 0.57 | 1.63 | 7 |
| stroke 12 | 4 % → 16 % | 4.7 px | 0.57 | 3.75 | 8 |
| stroke 13 | 8 % → 18 % | 9.2 px | 0.57 | 2.20 | 9 |
| stroke 14 | 5 % → 14 % | 5.3 px | 0.57 | 2.95 | 5 |
| stroke 15 | 9 % → 18 % | 10.7 px | 0.57 | 1.88 | 3 |
| stroke 16 | 6 % → 16 % | 7.0 px | 0.57 | 2.64 | 8 |
| stroke 17 | 4 % → 9 % | 5.0 px | 0.57 | 2.12 | 4 |
| stroke 18 | 3 % → 5 % | 3.1 px | 0.57 | 1.89 | 8 |
| stroke 19 | 6 % → 17 % | 7.4 px | 0.57 | 2.68 | 7 |
| stroke 20 | 9 % → 14 % | 9.8 px | 0.57 | 1.66 | 6 |
| stroke 21 | 4 % → 4 % | 4.6 px | 0.57 | 1.00 | 5 |
| stroke 22 | 8 % → 14 % | 9.2 px | 0.57 | 1.71 | 3 |
| stroke 23 | 8 % → 12 % | 8.7 px | 0.57 | 1.63 | 9 |
| stroke 24 | 4 % → 8 % | 5.0 px | 0.57 | 1.72 | 8 |
| stroke 25 | 8 % → 15 % | 9.3 px | 0.57 | 1.87 | 8 |
| stroke 26 | 6 % → 8 % | 6.9 px | 0.57 | 1.32 | 3 |
| stroke 27 | 4 % → 5 % | 4.8 px | 0.57 | 1.07 | 6 |
| stroke 28 | 8 % → 13 % | 8.9 px | 0.57 | 1.61 | 9 |
| stroke 29 | 8 % → 17 % | 9.0 px | 0.57 | 2.18 | 8 |
| stroke 30 | 13 % → 17 % | 15.2 px | 0.57 | 1.29 | 5 |
| stroke 31 | 5 % → 7 % | 6.0 px | 0.57 | 1.24 | 3 |
| stroke 32 | 11 % → 14 % | 12.9 px | 0.57 | 1.23 | 8 |
| stroke 33 | 8 % → 9 % | 9.5 px | 0.57 | 1.06 | 8 |
| stroke 34 | 11 % → 14 % | 12.3 px | 0.57 | 1.34 | 3 |
| stroke 35 | 9 % → 15 % | 10.7 px | 0.57 | 1.57 | 8 |
| stroke 36 | 10 % → 13 % | 11.9 px | 0.57 | 1.26 | 5 |
| stroke 37 | 10 % → 16 % | 11.4 px | 0.57 | 1.63 | 10 |
| stroke 38 | 14 % → 20 % | 15.3 px | 0.57 | 1.46 | 9 |
| stroke 39 | 14 % → 17 % | 16.5 px | 0.57 | 1.20 | 6 |
| stroke 40 | 6 % → 7 % | 7.3 px | 0.57 | 1.15 | 7 |
| stroke 41 | 16 % → 16 % | 18.2 px | 0.57 | 1.01 | 9 |
| stroke 42 | 14 % → 16 % | 16.1 px | 0.57 | 1.15 | 5 |
| stroke 43 | 11 % → 13 % | 13.0 px | 0.57 | 1.16 | 13 |
| stroke 44 | 13 % → 16 % | 15.2 px | 0.57 | 1.19 | 7 |
| stroke 45 | 2 % → 2 % | 2.8 px | 0.56 | 1.00 | 7 |
| stroke 46 | 17 % → 17 % | 18.9 px | 0.57 | 1.00 | 3 |
| stroke 47 | 14 % → 14 % | 15.9 px | 0.57 | 1.00 | 10 |
| stroke 48 | 13 % → 14 % | 14.7 px | 0.57 | 1.06 | 6 |
| stroke 49 | 19 % → 19 % | 21.8 px | 0.57 | 1.00 | 4 |
| stroke 50 | 11 % → 11 % | 12.2 px | 0.57 | 1.00 | 7 |

Numbers say: wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #39 Very thick impasto — own sheet
own sheet 600 × 600 · Impasto 1.00 · 60 px · 4.6 s

![Brush Artist · Refs · #39 Very thick impasto — own sheet](Brush-Artist-Refs-39-Very-thick-impasto-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 24 % → 35 % | 55.6 px | 0.43 | 1.44 | 308 |
| stroke 2 | 30 % → 46 % | 91.2 px | 0.43 | 1.52 | 310 |
| stroke 3 | 37 % → 48 % | 123.1 px | 0.44 | 1.31 | 337 |
| stroke 4 | 31 % → 43 % | 90.2 px | 0.43 | 1.39 | 330 |
| stroke 5 | 41 % → 39 % | 102.0 px | 0.43 | 0.97 | 280 |

Numbers say: wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #40 Watercolour blooms — own sheet
own sheet 600 × 600 · Watercolour 1.00 · 90 px · 8.9 s

![Brush Artist · Refs · #40 Watercolour blooms — own sheet](Brush-Artist-Refs-40-Watercolour-blooms-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 21 % → 27 % | 92.8 px | 0.12 | 1.28 | 798 |

## Brush Artist · Refs · #41 Coloured pencil hatching — own sheet
own sheet 600 × 600 · Pastel 1.00 · 4 px · 2.6 s

![Brush Artist · Refs · #41 Coloured pencil hatching — own sheet](Brush-Artist-Refs-41-Coloured-pencil-hatching-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 3 % → 15 % | 2.3 px | 0.35 | 5.04 | 4 |
| stroke 2 | 3 % → 8 % | 2.5 px | 0.35 | 2.34 | 2 |
| stroke 3 | 3 % → 12 % | 2.2 px | 0.35 | 4.03 | 3 |
| stroke 4 | 3 % → 20 % | 2.4 px | 0.35 | 6.35 | 10 |
| stroke 5 | 4 % → 8 % | 3.5 px | 0.35 | 1.78 | 7 |
| stroke 6 | 3 % → 14 % | 2.3 px | 0.35 | 4.57 | 3 |
| stroke 7 | 4 % → 17 % | 3.0 px | 0.35 | 4.34 | 8 |
| stroke 8 | 3 % → 13 % | 2.4 px | 0.35 | 4.14 | 2 |
| stroke 9 | 5 % → 12 % | 4.1 px | 0.35 | 2.18 | 7 |
| stroke 10 | 6 % → 17 % | 4.4 px | 0.35 | 2.92 | 5 |
| stroke 11 | 4 % → 14 % | 3.2 px | 0.35 | 3.38 | 13 |
| stroke 12 | 3 % → 3 % | 2.2 px | 0.35 | 1.00 | 9 |
| stroke 13 | 8 % → 19 % | 6.0 px | 0.35 | 2.35 | 8 |
| stroke 14 | 4 % → 15 % | 2.7 px | 0.35 | 4.14 | 4 |
| stroke 15 | 6 % → 13 % | 4.6 px | 0.35 | 2.12 | 5 |
| stroke 16 | 7 % → 12 % | 5.6 px | 0.35 | 1.63 | 7 |
| stroke 17 | 3 % → 3 % | 2.4 px | 0.35 | 1.00 | 5 |
| stroke 18 | 5 % → 9 % | 4.0 px | 0.36 | 1.63 | 8 |
| stroke 19 | 5 % → 14 % | 4.0 px | 0.35 | 2.72 | 2 |
| stroke 20 | 6 % → 16 % | 4.2 px | 0.35 | 2.94 | 5 |
| stroke 21 | 5 % → 15 % | 3.6 px | 0.35 | 3.13 | 7 |
| stroke 22 | 10 % → 18 % | 7.7 px | 0.35 | 1.77 | 5 |
| stroke 23 | 10 % → 15 % | 7.2 px | 0.35 | 1.54 | 11 |
| stroke 24 | 7 % → 15 % | 5.3 px | 0.35 | 2.12 | 8 |
| stroke 25 | 5 % → 12 % | 4.0 px | 0.35 | 2.27 | 8 |
| stroke 26 | 4 % → 7 % | 3.1 px | 0.35 | 1.79 | 3 |
| stroke 27 | 3 % → 8 % | 2.6 px | 0.35 | 2.35 | 2 |
| stroke 28 | 7 % → 11 % | 5.2 px | 0.36 | 1.68 | 5 |
| stroke 29 | 3 % → 15 % | 2.6 px | 0.35 | 4.48 | 7 |
| stroke 30 | 7 % → 10 % | 5.2 px | 0.35 | 1.40 | 5 |
| stroke 31 | 7 % → 16 % | 5.8 px | 0.35 | 2.09 | 5 |
| stroke 32 | 3 % → 6 % | 2.4 px | 0.36 | 1.93 | 5 |
| stroke 33 | 8 % → 13 % | 5.9 px | 0.35 | 1.65 | 6 |
| stroke 34 | 3 % → 6 % | 2.6 px | 0.35 | 1.71 | 8 |
| stroke 35 | 7 % → 15 % | 5.4 px | 0.35 | 2.11 | 3 |
| stroke 36 | 5 % → 5 % | 4.0 px | 0.35 | 1.01 | 6 |
| stroke 37 | 8 % → 16 % | 5.9 px | 0.35 | 2.07 | 8 |
| stroke 38 | 8 % → 14 % | 6.2 px | 0.35 | 1.71 | 4 |
| stroke 39 | 7 % → 12 % | 5.4 px | 0.35 | 1.65 | 2 |
| stroke 40 | 9 % → 20 % | 6.7 px | 0.36 | 2.23 | 6 |
| stroke 41 | 10 % → 15 % | 7.7 px | 0.35 | 1.46 | 5 |
| stroke 42 | 11 % → 19 % | 8.5 px | 0.36 | 1.73 | 3 |
| stroke 43 | 5 % → 9 % | 4.1 px | 0.35 | 1.66 | 5 |
| stroke 44 | 11 % → 15 % | 8.5 px | 0.36 | 1.41 | 5 |
| stroke 45 | 14 % → 19 % | 10.5 px | 0.35 | 1.37 | 6 |
| stroke 46 | 5 % → 7 % | 4.0 px | 0.35 | 1.38 | 5 |
| stroke 47 | 11 % → 14 % | 8.7 px | 0.36 | 1.21 | 7 |
| stroke 48 | 13 % → 18 % | 10.0 px | 0.36 | 1.36 | 2 |
| stroke 49 | 6 % → 9 % | 4.3 px | 0.35 | 1.65 | 5 |
| stroke 50 | 7 % → 7 % | 5.6 px | 0.35 | 1.00 | 3 |
| stroke 51 | 10 % → 16 % | 7.4 px | 0.36 | 1.67 | 4 |
| stroke 52 | 14 % → 16 % | 10.5 px | 0.35 | 1.19 | 11 |
| stroke 53 | 12 % → 16 % | 9.0 px | 0.35 | 1.35 | 4 |
| stroke 54 | 11 % → 16 % | 8.5 px | 0.35 | 1.46 | 6 |
| stroke 55 | 12 % → 16 % | 9.0 px | 0.35 | 1.34 | 5 |
| stroke 56 | 12 % → 13 % | 9.0 px | 0.35 | 1.11 | 4 |
| stroke 57 | 11 % → 14 % | 8.2 px | 0.36 | 1.31 | 6 |
| stroke 58 | 11 % → 12 % | 8.6 px | 0.35 | 1.12 | 3 |
| stroke 59 | 13 % → 15 % | 9.8 px | 0.35 | 1.16 | 7 |
| stroke 60 | 17 % → 22 % | 13.1 px | 0.35 | 1.26 | 6 |
| stroke 61 | 21 % → 22 % | 15.6 px | 0.35 | 1.05 | 2 |
| stroke 62 | 10 % → 10 % | 7.5 px | 0.35 | 1.00 | 6 |
| stroke 63 | 12 % → 13 % | 9.5 px | 0.35 | 1.09 | 3 |
| stroke 64 | 16 % → 17 % | 12.4 px | 0.35 | 1.02 | 6 |
| stroke 65 | 17 % → 17 % | 12.7 px | 0.35 | 1.00 | 5 |
| stroke 66 | 15 % → 15 % | 11.9 px | 0.35 | 1.00 | 3 |
| stroke 67 | 13 % → 14 % | 9.9 px | 0.35 | 1.06 | 9 |
| stroke 68 | 5 % → 10 % | 4.1 px | 0.35 | 1.90 | 4 |
| stroke 69 | 6 % → 6 % | 4.3 px | 0.35 | 1.00 | 2 |
| stroke 70 | 11 % → 14 % | 8.5 px | 0.35 | 1.28 | 4 |
| stroke 71 | 10 % → 12 % | 7.7 px | 0.35 | 1.17 | 5 |
| stroke 72 | 6 % → 7 % | 4.5 px | 0.35 | 1.26 | 3 |
| stroke 73 | 14 % → 14 % | 10.4 px | 0.35 | 1.00 | 5 |
| stroke 74 | 16 % → 16 % | 12.3 px | 0.35 | 1.00 | 5 |
| stroke 75 | 17 % → 17 % | 13.1 px | 0.35 | 1.00 | 4 |
| stroke 76 | 15 % → 15 % | 11.7 px | 0.36 | 1.00 | 5 |
| stroke 77 | 8 % → 10 % | 6.0 px | 0.35 | 1.32 | 3 |
| stroke 78 | 10 % → 10 % | 7.5 px | 0.35 | 1.00 | 5 |
| stroke 79 | 8 % → 8 % | 6.2 px | 0.35 | 1.00 | 3 |
| stroke 80 | 12 % → 12 % | 9.1 px | 0.36 | 1.00 | 3 |

Numbers say: wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #42 Oil pastel shaggy — own sheet
own sheet 600 × 600 · Pastel 1.00 · 18 px · 2.7 s

![Brush Artist · Refs · #42 Oil pastel shaggy — own sheet](Brush-Artist-Refs-42-Oil-pastel-shaggy-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 5 % → 27 % | 8.5 px | 0.27 | 5.25 | 11 |
| stroke 2 | 5 % → 24 % | 7.8 px | 0.29 | 5.02 | 9 |
| stroke 3 | 5 % → 29 % | 8.8 px | 0.28 | 5.49 | 10 |
| stroke 4 | 5 % → 11 % | 9.1 px | 0.26 | 1.99 | 11 |
| stroke 5 | 6 % → 11 % | 10.2 px | 0.26 | 1.77 | 9 |
| stroke 6 | 8 % → 36 % | 13.4 px | 0.28 | 4.52 | 7 |
| stroke 7 | 11 % → 30 % | 18.0 px | 0.28 | 2.79 | 11 |
| stroke 8 | 7 % → 37 % | 10.8 px | 0.28 | 5.63 | 9 |
| stroke 9 | 8 % → 21 % | 13.4 px | 0.28 | 2.61 | 11 |
| stroke 10 | 8 % → 18 % | 13.2 px | 0.29 | 2.30 | 12 |
| stroke 11 | 5 % → 26 % | 8.8 px | 0.28 | 4.89 | 9 |
| stroke 12 | 8 % → 19 % | 13.1 px | 0.28 | 2.33 | 10 |
| stroke 13 | 12 % → 23 % | 20.4 px | 0.28 | 1.91 | 10 |
| stroke 14 | 5 % → 22 % | 7.6 px | 0.28 | 4.76 | 11 |
| stroke 15 | 6 % → 24 % | 9.1 px | 0.28 | 4.28 | 10 |
| stroke 16 | 9 % → 21 % | 15.5 px | 0.29 | 2.21 | 7 |
| stroke 17 | 16 % → 37 % | 26.3 px | 0.28 | 2.36 | 9 |
| stroke 18 | 14 % → 25 % | 22.6 px | 0.28 | 1.82 | 9 |
| stroke 19 | 14 % → 30 % | 23.7 px | 0.28 | 2.08 | 10 |
| stroke 20 | 21 % → 39 % | 35.4 px | 0.28 | 1.81 | 10 |
| stroke 21 | 9 % → 16 % | 14.2 px | 0.28 | 1.88 | 10 |
| stroke 22 | 14 % → 17 % | 23.1 px | 0.27 | 1.19 | 9 |
| stroke 23 | 12 % → 17 % | 20.4 px | 0.29 | 1.37 | 11 |
| stroke 24 | 18 % → 26 % | 30.0 px | 0.29 | 1.43 | 11 |
| stroke 25 | 19 % → 34 % | 32.1 px | 0.28 | 1.75 | 10 |
| stroke 26 | 5 % → 13 % | 8.8 px | 0.28 | 2.45 | 8 |
| stroke 27 | 18 % → 26 % | 30.3 px | 0.29 | 1.41 | 10 |
| stroke 28 | 14 % → 23 % | 23.2 px | 0.29 | 1.66 | 9 |
| stroke 29 | 9 % → 26 % | 14.2 px | 0.29 | 3.08 | 11 |
| stroke 30 | 15 % → 36 % | 24.5 px | 0.28 | 2.44 | 10 |
| stroke 31 | 13 % → 17 % | 22.3 px | 0.29 | 1.24 | 9 |
| stroke 32 | 16 % → 29 % | 26.3 px | 0.29 | 1.82 | 6 |
| stroke 33 | 15 % → 16 % | 24.3 px | 0.28 | 1.09 | 11 |
| stroke 34 | 19 % → 27 % | 31.4 px | 0.28 | 1.44 | 11 |
| stroke 35 | 25 % → 35 % | 40.9 px | 0.28 | 1.39 | 8 |
| stroke 36 | 24 % → 33 % | 40.2 px | 0.28 | 1.34 | 9 |
| stroke 37 | 11 % → 12 % | 18.4 px | 0.28 | 1.04 | 12 |
| stroke 38 | 19 % → 24 % | 30.7 px | 0.29 | 1.31 | 8 |
| stroke 39 | 16 % → 22 % | 27.0 px | 0.27 | 1.35 | 9 |
| stroke 40 | 21 % → 29 % | 34.9 px | 0.28 | 1.37 | 12 |
| stroke 41 | 31 % → 34 % | 51.2 px | 0.28 | 1.12 | 10 |
| stroke 42 | 23 % → 29 % | 37.9 px | 0.28 | 1.28 | 12 |
| stroke 43 | 12 % → 12 % | 20.2 px | 0.28 | 1.00 | 9 |
| stroke 44 | 29 % → 36 % | 48.3 px | 0.28 | 1.24 | 9 |
| stroke 45 | 16 % → 16 % | 25.6 px | 0.27 | 1.00 | 11 |
| stroke 46 | 28 % → 33 % | 46.9 px | 0.28 | 1.15 | 11 |
| stroke 47 | 37 % → 41 % | 61.6 px | 0.28 | 1.09 | 7 |
| stroke 48 | 28 % → 35 % | 47.2 px | 0.28 | 1.26 | 9 |
| stroke 49 | 27 % → 30 % | 43.8 px | 0.29 | 1.11 | 10 |
| stroke 50 | 37 % → 40 % | 61.8 px | 0.28 | 1.07 | 9 |
| stroke 51 | 15 % → 15 % | 25.8 px | 0.28 | 1.00 | 6 |
| stroke 52 | 37 % → 37 % | 61.4 px | 0.28 | 1.01 | 9 |
| stroke 53 | 22 % → 26 % | 35.6 px | 0.29 | 1.20 | 13 |
| stroke 54 | 17 % → 19 % | 29.0 px | 0.29 | 1.10 | 10 |
| stroke 55 | 15 % → 15 % | 24.6 px | 0.29 | 1.00 | 8 |
| stroke 56 | 13 % → 14 % | 21.3 px | 0.27 | 1.08 | 9 |
| stroke 57 | 23 % → 23 % | 38.0 px | 0.29 | 1.00 | 8 |
| stroke 58 | 26 % → 28 % | 43.7 px | 0.28 | 1.06 | 10 |
| stroke 59 | 40 % → 40 % | 66.1 px | 0.28 | 1.00 | 9 |
| stroke 60 | 21 % → 21 % | 34.4 px | 0.29 | 1.00 | 6 |

Numbers say: wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #43 Dragged black ink blocks — own sheet
own sheet 600 × 600 · Gouache 1.00 · 70 px · 7.0 s

![Brush Artist · Refs · #43 Dragged black ink blocks — own sheet](Brush-Artist-Refs-43-Dragged-black-ink-blocks-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 11 % → 4 % | 24.9 px | 0.46 | 0.40 | 328 |
| stroke 2 | 10 % → 8 % | 35.4 px | 0.46 | 0.82 | 403 |
| stroke 3 | 18 % → 14 % | 66.1 px | 0.46 | 0.77 | 518 |
| stroke 4 | 22 % → 11 % | 75.0 px | 0.43 | 0.53 | 474 |
| stroke 5 | 31 % → 13 % | 72.0 px | 0.43 | 0.43 | 572 |

## Brush Artist · Refs · #44 Blue looping ribbon — own sheet
own sheet 600 × 600 · Oil 1.00 · 80 px · 5.2 s

![Brush Artist · Refs · #44 Blue looping ribbon — own sheet](Brush-Artist-Refs-44-Blue-looping-ribbon-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 32 % → 32 % | 42.1 px | 0.78 | 1.00 | 2884 |

## Brush Artist · Refs · #45 Soft pastel pepper — own sheet
own sheet 600 × 600 · Pastel 1.00 · 40 px · 5.0 s

![Brush Artist · Refs · #45 Soft pastel pepper — own sheet](Brush-Artist-Refs-45-Soft-pastel-pepper-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 10 % → 38 % | 11.3 px | 0.50 | 3.71 | 391 |
| stroke 2 | 18 % → 33 % | 20.7 px | 0.50 | 1.88 | 407 |
| stroke 3 | 25 % → 36 % | 16.9 px | 0.50 | 1.46 | 342 |
| stroke 4 | 24 % → 34 % | 29.4 px | 0.50 | 1.45 | 319 |
| stroke 5 | 30 % → 30 % | 20.9 px | 0.49 | 1.00 | 209 |
| stroke 6 | 35 % → 44 % | 22.7 px | 0.50 | 1.24 | 344 |
| stroke 7 | 39 % → 43 % | 21.3 px | 0.50 | 1.11 | 454 |
| stroke 8 | 43 % → 43 % | 43.7 px | 0.50 | 1.00 | 565 |

Numbers say: wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #46 Red-brown ink lips — own sheet
own sheet 600 × 600 · Watercolour 1.00 · 50 px · 7.9 s

![Brush Artist · Refs · #46 Red-brown ink lips — own sheet](Brush-Artist-Refs-46-Red-brown-ink-lips-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 13 % → 26 % | 54.5 px | 0.56 | 1.96 | 92 |
| stroke 2 | 17 % → 31 % | 72.4 px | 0.53 | 1.89 | 85 |

Numbers say: wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #47 Pink knife slabs — own sheet
own sheet 600 × 600 · Impasto 1.00 · 90 px · 4.8 s

![Brush Artist · Refs · #47 Pink knife slabs — own sheet](Brush-Artist-Refs-47-Pink-knife-slabs-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 16 % → 32 % | 81.5 px | 0.10 | 1.97 | 410 |
| stroke 2 | 29 % → 42 % | 165.6 px | 0.11 | 1.45 | 323 |
| stroke 3 | 29 % → 43 % | 165.1 px | 0.13 | 1.47 | 319 |
| stroke 4 | 39 % → 38 % | 165.8 px | 0.14 | 0.97 | 353 |

Numbers say: wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #48 Black bands with drips — own sheet
own sheet 600 × 600 · Gouache 1.00 · 70 px · 10.8 s

![Brush Artist · Refs · #48 Black bands with drips — own sheet](Brush-Artist-Refs-48-Black-bands-with-drips-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 28 % → 40 % | 72.6 px | 0.38 | 1.43 | 496 |
| stroke 2 | 43 % → 55 % | 137.3 px | 0.38 | 1.30 | 681 |
| stroke 3 | 45 % → 56 % | 141.4 px | 0.38 | 1.23 | 510 |
| stroke 4 | 48 % → 45 % | 139.2 px | 0.37 | 0.94 | 518 |

## Brush Artist · Refs · #49 Magenta letters round brush — own sheet
own sheet 600 × 600 · Ink 1.00 · 30 px · 9.1 s

![Brush Artist · Refs · #49 Magenta letters round brush — own sheet](Brush-Artist-Refs-49-Magenta-letters-round-brush-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 27 % → 46 % | 64.7 px | 0.52 | 1.68 | 30 |
| stroke 2 | 29 % → 41 % | 53.0 px | 0.53 | 1.40 | 47 |
| stroke 3 | 42 % → 68 % | 98.0 px | 0.52 | 1.62 | 30 |
| stroke 4 | 33 % → 52 % | 53.5 px | 0.52 | 1.56 | 107 |
| stroke 5 | 41 % → 66 % | 97.1 px | 0.52 | 1.62 | 95 |
| stroke 6 | 56 % → 72 % | 237.9 px | 0.52 | 1.28 | 27 |
| stroke 7 | 42 % → 58 % | 65.1 px | 0.52 | 1.36 | 187 |
| stroke 8 | 36 % → 61 % | 92.6 px | 0.53 | 1.71 | 102 |
| stroke 9 | 50 % → 62 % | 156.5 px | 0.52 | 1.24 | 29 |
| stroke 10 | 43 % → 73 % | 102.9 px | 0.52 | 1.68 | 81 |
| stroke 11 | 52 % → 72 % | 221.9 px | 0.52 | 1.39 | 15 |
| stroke 12 | 54 % → 70 % | 84.9 px | 0.52 | 1.28 | 108 |
| stroke 13 | 42 % → 53 % | 116.2 px | 0.53 | 1.27 | 41 |
| stroke 14 | 45 % → 68 % | 131.6 px | 0.53 | 1.52 | 29 |
| stroke 15 | 43 % → 63 % | 101.8 px | 0.52 | 1.47 | 68 |
| stroke 16 | 52 % → 61 % | 220.3 px | 0.52 | 1.19 | 16 |
| stroke 17 | 53 % → 64 % | 82.3 px | 0.52 | 1.19 | 107 |
| stroke 18 | 36 % → 43 % | 98.8 px | 0.53 | 1.20 | 35 |
| stroke 19 | 53 % → 52 % | 122.0 px | 0.52 | 0.99 | 29 |
| stroke 20 | 55 % → 55 % | 127.4 px | 0.52 | 1.00 | 35 |
| stroke 21 | 49 % → 49 % | 80.4 px | 0.52 | 1.00 | 85 |

Numbers say: wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #50 Thick swipes on photo — own sheet
own sheet 600 × 600 · Impasto 1.00 · 40 px · 2.8 s

![Brush Artist · Refs · #50 Thick swipes on photo — own sheet](Brush-Artist-Refs-50-Thick-swipes-on-photo-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 9 % → 21 % | 43.0 px | 0.35 | 2.32 | 64 |
| stroke 2 | 9 % → 16 % | 42.2 px | 0.34 | 1.82 | 36 |
| stroke 3 | 10 % → 11 % | 42.0 px | 0.32 | 1.06 | 58 |
| stroke 4 | 11 % → 18 % | 44.0 px | 0.35 | 1.60 | 34 |
| stroke 5 | 11 % → 10 % | 42.2 px | 0.34 | 0.94 | 34 |
| stroke 6 | 17 % → 21 % | 99.5 px | 0.35 | 1.19 | 28 |
| stroke 7 | 22 % → 26 % | 92.9 px | 0.35 | 1.18 | 38 |
| stroke 8 | 21 % → 20 % | 119.7 px | 0.35 | 0.96 | 32 |
| stroke 9 | 10 % → 11 % | 43.0 px | 0.30 | 1.11 | 43 |
| stroke 10 | 22 % → 22 % | 75.4 px | 0.35 | 0.96 | 41 |
| stroke 11 | 8 % → 8 % | 41.8 px | 0.36 | 0.95 | 29 |
| stroke 12 | 17 % → 16 % | 94.4 px | 0.35 | 0.96 | 25 |

Numbers say: wet paint spreads well beyond the stroke.

## Brush Artist · Ink — dry brush — own sheet
own sheet 600 × 600 · Gouache 1.00 · 30 px · 2.7 s

![Brush Artist · Ink — dry brush — own sheet](Brush-Artist-Ink-dry-brush-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| ear | 8 % → 2 % | 9.7 px | 0.85 | 0.22 | 431 |
| drag0 | 4 % → 6 % | 7.6 px | 0.85 | 1.51 | 109 |
| drag1 | 7 % → 7 % | 15.1 px | 0.85 | 0.89 | 88 |
| drag2 | 10 % → 7 % | 22.1 px | 0.85 | 0.71 | 82 |
| drag3 | 12 % → 7 % | 30.1 px | 0.85 | 0.60 | 60 |

Numbers say: wet paint spreads well beyond the stroke.

## Brush Artist · Watercolour — blue — own sheet
own sheet 600 × 600 · Watercolour 0.93 · Ink 0.07 · 40 px · 9.4 s

![Brush Artist · Watercolour — blue — own sheet](Brush-Artist-Watercolour-blue-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| s0 | 7 % → 24 % | 28.8 px | 0.30 | 3.32 | 41 |
| s1 | 6 % → 33 % | 10.1 px | 0.37 | 6.00 | 41 |
| s2 | 10 % → 19 % | 44.2 px | 0.26 | 1.81 | 36 |
| s3 | 10 % → 18 % | 26.7 px | 0.31 | 1.92 | 46 |
| s4 | 14 % → 30 % | 38.6 px | 0.36 | 2.16 | 59 |
| s5 | 19 % → 29 % | 39.3 px | 0.37 | 1.54 | 51 |
| s6 | 18 % → 22 % | 48.7 px | 0.31 | 1.25 | 52 |
| s7 | 25 % → 36 % | 32.7 px | 0.37 | 1.46 | 41 |
| s8 | 21 % → 25 % | 79.8 px | 0.30 | 1.20 | 48 |

Numbers say: wet paint spreads well beyond the stroke.

## Brush Artist · Charcoal — stick — own sheet
own sheet 600 × 600 · Charcoal 0.78 · Pastel 0.22 · 28 px · 1.2 s

![Brush Artist · Charcoal — stick — own sheet](Brush-Artist-Charcoal-stick-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| finger0 | 12 % → 25 % | 21.2 px | 0.83 | 2.03 | 32 |
| tip0 | 13 % → 21 % | 33.8 px | 0.83 | 1.70 | 11 |
| finger1 | 23 % → 41 % | 40.4 px | 0.83 | 1.77 | 32 |
| tip1 | 21 % → 29 % | 57.3 px | 0.83 | 1.38 | 10 |
| finger2 | 25 % → 37 % | 43.8 px | 0.83 | 1.49 | 32 |
| tip2 | 21 % → 29 % | 55.7 px | 0.83 | 1.40 | 7 |
| finger3 | 24 % → 27 % | 42.7 px | 0.83 | 1.14 | 27 |
| tip3 | 20 % → 20 % | 54.1 px | 0.83 | 1.00 | 13 |
| cig0 | 34 % → 47 % | 75.0 px | 0.83 | 1.39 | 11 |
| cig1 | 36 % → 47 % | 80.5 px | 0.83 | 1.30 | 15 |
| cig2 | 39 % → 47 % | 86.7 px | 0.83 | 1.20 | 13 |
| cig3 | 41 % → 47 % | 91.3 px | 0.83 | 1.14 | 17 |
| cig4 | 44 % → 46 % | 97.5 px | 0.83 | 1.06 | 12 |
| cig5 | 46 % → 46 % | 102.9 px | 0.83 | 1.00 | 12 |

Numbers say: wet paint spreads well beyond the stroke.

## Oil · Henry Ward · HW #02 cream over wet olive — own sheet
own sheet 600 × 600 · Oil 0.81 · Ink 0.19 · 96 px · 31.2 s

![Oil · Henry Ward · HW #02 cream over wet olive — own sheet](Oil-Henry-Ward-HW-02-cream-over-wet-olive-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 45 % → 51 % | 87.7 px | 0.45 | 1.13 | 1277 |
| stroke 2 | 57 % → 55 % | 143.1 px | 0.43 | 0.97 | 1649 |
| stroke 3 | 65 % → 57 % | 205.3 px | 0.45 | 0.88 | 1894 |
| stroke 4 | 68 % → 62 % | 239.1 px | 0.47 | 0.91 | 1836 |
| stroke 5 | 69 % → 68 % | 243.9 px | 0.47 | 0.99 | 1847 |
| stroke 6 | 68 % → 58 % | 238.3 px | 0.47 | 0.85 | 1663 |
| stroke 7 | 75 % → 75 % | 238.6 px | 0.48 | 1.00 | 1556 |
| stroke 8 | 95 % → 45 % | 239.7 px | 0.49 | 0.47 | 1853 |
| stroke 9 | 100 % → 38 % | 187.9 px | 0.46 | 0.38 | 1348 |
| stroke 10 | 10 % → 56 % | 52.8 px | 0.44 | 5.65 | 325 |
| stroke 11 | 17 % → 60 % | 111.4 px | 0.47 | 3.54 | 419 |
| stroke 12 | 10 % → 48 % | 67.0 px | 0.49 | 4.85 | 281 |
| stroke 13 | 31 % → 63 % | 190.4 px | 0.44 | 2.02 | 406 |
| stroke 14 | 33 % → 58 % | 171.9 px | 0.46 | 1.76 | 568 |
| stroke 15 | 32 % → 58 % | 196.1 px | 0.47 | 1.82 | 541 |
| stroke 16 | 31 % → 57 % | 312.6 px | 0.47 | 1.82 | 398 |
| stroke 17 | 39 % → 68 % | 231.0 px | 0.48 | 1.74 | 431 |
| stroke 18 | 43 % → 60 % | 313.4 px | 0.47 | 1.39 | 397 |
| stroke 19 | 44 % → 57 % | 376.3 px | 0.47 | 1.32 | 390 |
| stroke 20 | 45 % → 50 % | 271.0 px | 0.47 | 1.10 | 497 |
| stroke 21 | 48 % → 49 % | 236.9 px | 0.48 | 1.04 | 741 |
| stroke 22 | 54 % → 57 % | 237.0 px | 0.45 | 1.05 | 575 |
| stroke 23 | 56 % → 58 % | 317.6 px | 0.46 | 1.03 | 617 |
| stroke 24 | 67 % → 67 % | 524.6 px | 0.47 | 1.01 | 350 |
| stroke 25 | 62 % → 61 % | 369.4 px | 0.46 | 0.99 | 461 |
| stroke 26 | 50 % → 50 % | 301.9 px | 0.48 | 0.98 | 615 |

Numbers say: wet paint spreads well beyond the stroke.

## Oil · Henry Ward · HW #04 grey arcs over ochre — own sheet
own sheet 600 × 600 · Oil 1.00 · 84 px · 32.4 s

![Oil · Henry Ward · HW #04 grey arcs over ochre — own sheet](Oil-Henry-Ward-HW-04-grey-arcs-over-ochre-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 47 % → 70 % | 82.7 px | 0.20 | 1.48 | 1264 |
| stroke 2 | 62 % → 74 % | 143.0 px | 0.20 | 1.20 | 1666 |
| stroke 3 | 70 % → 69 % | 211.2 px | 0.20 | 0.98 | 1845 |
| stroke 4 | 71 % → 68 % | 221.8 px | 0.19 | 0.95 | 1831 |
| stroke 5 | 71 % → 60 % | 219.7 px | 0.18 | 0.84 | 1755 |
| stroke 6 | 70 % → 53 % | 216.9 px | 0.16 | 0.76 | 1661 |
| stroke 7 | 75 % → 40 % | 221.8 px | 0.13 | 0.53 | 1612 |
| stroke 8 | 93 % → 37 % | 216.9 px | 0.11 | 0.40 | 1905 |
| stroke 9 | 100 % → 39 % | 171.2 px | 0.11 | 0.39 | 1376 |
| stroke 10 | 13 % → 73 % | 69.1 px | 0.20 | 5.80 | 376 |
| stroke 11 | 19 % → 64 % | 99.1 px | 0.19 | 3.35 | 497 |
| stroke 12 | 28 % → 64 % | 201.2 px | 0.18 | 2.27 | 314 |
| stroke 13 | 37 % → 69 % | 146.9 px | 0.20 | 1.89 | 722 |
| stroke 14 | 38 % → 64 % | 243.4 px | 0.19 | 1.70 | 455 |
| stroke 15 | 44 % → 67 % | 197.8 px | 0.20 | 1.50 | 690 |
| stroke 16 | 46 % → 62 % | 322.6 px | 0.18 | 1.34 | 436 |
| stroke 17 | 48 % → 67 % | 254.9 px | 0.20 | 1.39 | 657 |
| stroke 18 | 47 % → 62 % | 296.2 px | 0.19 | 1.31 | 442 |
| stroke 19 | 53 % → 70 % | 260.1 px | 0.20 | 1.30 | 751 |
| stroke 20 | 52 % → 68 % | 261.9 px | 0.19 | 1.31 | 788 |
| stroke 21 | 55 % → 71 % | 295.0 px | 0.20 | 1.31 | 710 |
| stroke 22 | 46 % → 69 % | 302.4 px | 0.18 | 1.50 | 438 |
| stroke 23 | 50 % → 60 % | 274.3 px | 0.19 | 1.20 | 762 |
| stroke 24 | 61 % → 71 % | 428.1 px | 0.20 | 1.16 | 310 |
| stroke 25 | 53 % → 67 % | 321.8 px | 0.19 | 1.26 | 738 |
| stroke 26 | 61 % → 70 % | 391.4 px | 0.19 | 1.15 | 692 |
| stroke 27 | 37 % → 55 % | 217.1 px | 0.16 | 1.47 | 472 |
| stroke 28 | 29 % → 42 % | 186.5 px | 0.14 | 1.44 | 401 |
| stroke 29 | 36 % → 48 % | 241.2 px | 0.12 | 1.34 | 216 |
| stroke 30 | 37 % → 37 % | 171.7 px | 0.11 | 1.00 | 431 |

Numbers say: wet paint spreads well beyond the stroke.

## Oil · Henry Ward · HW #09 white arches over wet blue-grey — own sheet
own sheet 600 × 600 · Oil 1.00 · 84 px · 35.3 s

![Oil · Henry Ward · HW #09 white arches over wet blue-grey — own sheet](Oil-Henry-Ward-HW-09-white-arches-over-wet-blue-grey-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 48 % → 11 % | 81.3 px | 0.10 | 0.23 | 1240 |
| stroke 2 | 61 % → 23 % | 141.4 px | 0.10 | 0.37 | 1644 |
| stroke 3 | 70 % → 33 % | 211.1 px | 0.09 | 0.47 | 1807 |
| stroke 4 | 72 % → 44 % | 224.2 px | 0.09 | 0.62 | 1820 |
| stroke 5 | 70 % → 60 % | 217.7 px | 0.09 | 0.86 | 1770 |
| stroke 6 | 70 % → 69 % | 215.6 px | 0.10 | 0.98 | 1645 |
| stroke 7 | 74 % → 70 % | 219.0 px | 0.12 | 0.94 | 1567 |
| stroke 8 | 92 % → 71 % | 218.4 px | 0.13 | 0.77 | 1751 |
| stroke 9 | 100 % → 70 % | 166.7 px | 0.14 | 0.70 | 1368 |
| stroke 10 | 10 % → 54 % | 53.4 px | 0.11 | 5.44 | 559 |
| stroke 11 | 18 % → 59 % | 49.4 px | 0.11 | 3.34 | 716 |
| stroke 12 | 26 % → 60 % | 60.7 px | 0.11 | 2.34 | 941 |
| stroke 13 | 31 % → 68 % | 103.8 px | 0.11 | 2.22 | 640 |
| stroke 14 | 38 % → 70 % | 42.2 px | 0.12 | 1.83 | 929 |
| stroke 15 | 36 % → 61 % | 172.7 px | 0.11 | 1.70 | 965 |
| stroke 16 | 55 % → 73 % | 261.9 px | 0.12 | 1.33 | 868 |
| stroke 17 | 49 % → 72 % | 262.7 px | 0.12 | 1.46 | 821 |
| stroke 18 | 45 % → 62 % | 206.9 px | 0.12 | 1.37 | 1259 |
| stroke 19 | 56 % → 69 % | 256.4 px | 0.12 | 1.24 | 891 |
| stroke 20 | 45 % → 59 % | 198.9 px | 0.12 | 1.32 | 1220 |
| stroke 21 | 53 % → 60 % | 229.2 px | 0.11 | 1.13 | 914 |
| stroke 22 | 53 % → 57 % | 234.1 px | 0.12 | 1.07 | 1136 |
| stroke 23 | 55 % → 59 % | 294.2 px | 0.11 | 1.07 | 1096 |
| stroke 24 | 63 % → 69 % | 380.2 px | 0.11 | 1.09 | 361 |
| stroke 25 | 64 % → 69 % | 289.2 px | 0.12 | 1.07 | 471 |
| stroke 26 | 74 % → 79 % | 470.0 px | 0.12 | 1.07 | 456 |
| stroke 27 | 67 % → 71 % | 225.6 px | 0.12 | 1.06 | 536 |
| stroke 28 | 71 % → 71 % | 264.3 px | 0.13 | 1.00 | 558 |

Numbers say: wet paint spreads well beyond the stroke.

## Oil · Henry Ward · HW #03 navy contours over wet band — own sheet
own sheet 600 × 600 · Oil 1.00 · 84 px · 22.6 s

![Oil · Henry Ward · HW #03 navy contours over wet band — own sheet](Oil-Henry-Ward-HW-03-navy-contours-over-wet-band-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 47 % → 34 % | 78.7 px | 0.70 | 0.72 | 1151 |
| stroke 2 | 62 % → 39 % | 145.7 px | 0.63 | 0.63 | 1650 |
| stroke 3 | 69 % → 43 % | 203.2 px | 0.59 | 0.62 | 1887 |
| stroke 4 | 70 % → 47 % | 217.9 px | 0.54 | 0.67 | 1896 |
| stroke 5 | 70 % → 47 % | 217.2 px | 0.54 | 0.68 | 1824 |
| stroke 6 | 71 % → 39 % | 220.4 px | 0.52 | 0.55 | 1716 |
| stroke 7 | 74 % → 30 % | 217.1 px | 0.53 | 0.41 | 1610 |
| stroke 8 | 92 % → 24 % | 217.6 px | 0.56 | 0.26 | 1944 |
| stroke 9 | 100 % → 12 % | 171.1 px | 0.71 | 0.12 | 1391 |
| stroke 10 | 8 % → 52 % | 75.2 px | 0.55 | 6.95 | 234 |
| stroke 11 | 15 % → 49 % | 113.5 px | 0.54 | 3.28 | 265 |
| stroke 12 | 23 % → 48 % | 164.2 px | 0.54 | 2.12 | 314 |
| stroke 13 | 25 % → 39 % | 173.3 px | 0.52 | 1.55 | 400 |
| stroke 14 | 18 % → 43 % | 137.2 px | 0.69 | 2.41 | 161 |
| stroke 15 | 29 % → 44 % | 208.7 px | 0.64 | 1.49 | 193 |
| stroke 16 | 36 % → 39 % | 107.8 px | 0.57 | 1.07 | 650 |
| stroke 17 | 40 % → 40 % | 146.0 px | 0.57 | 1.00 | 512 |

Numbers say: wet paint spreads well beyond the stroke.

## Oil · Henry Ward · HW #01 peach cloud and legs over teal — own sheet
own sheet 600 × 600 · Oil 1.00 · 84 px · 27.4 s

![Oil · Henry Ward · HW #01 peach cloud and legs over teal — own sheet](Oil-Henry-Ward-HW-01-peach-cloud-and-legs-over-teal-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 50 % → 64 % | 88.3 px | 0.39 | 1.27 | 1312 |
| stroke 2 | 62 % → 67 % | 146.6 px | 0.40 | 1.09 | 1758 |
| stroke 3 | 69 % → 68 % | 202.8 px | 0.40 | 0.98 | 1807 |
| stroke 4 | 71 % → 70 % | 219.6 px | 0.40 | 0.99 | 1912 |
| stroke 5 | 70 % → 64 % | 217.6 px | 0.40 | 0.92 | 1742 |
| stroke 6 | 71 % → 56 % | 218.3 px | 0.38 | 0.79 | 1706 |
| stroke 7 | 76 % → 49 % | 221.6 px | 0.33 | 0.64 | 1659 |
| stroke 8 | 95 % → 43 % | 217.7 px | 0.31 | 0.45 | 1964 |
| stroke 9 | 100 % → 36 % | 170.3 px | 0.25 | 0.36 | 1535 |
| stroke 10 | 19 % → 65 % | 66.9 px | 0.39 | 3.40 | 524 |
| stroke 11 | 24 % → 67 % | 100.4 px | 0.40 | 2.75 | 426 |
| stroke 12 | 35 % → 68 % | 154.5 px | 0.40 | 1.96 | 479 |
| stroke 13 | 35 % → 70 % | 195.9 px | 0.40 | 1.97 | 467 |
| stroke 14 | 56 % → 66 % | 216.6 px | 0.40 | 1.19 | 660 |
| stroke 15 | 52 % → 68 % | 244.9 px | 0.40 | 1.30 | 426 |
| stroke 16 | 50 % → 70 % | 285.2 px | 0.40 | 1.41 | 449 |
| stroke 17 | 42 % → 61 % | 227.1 px | 0.37 | 1.47 | 374 |
| stroke 18 | 48 % → 64 % | 354.0 px | 0.37 | 1.34 | 422 |
| stroke 19 | 60 % → 80 % | 380.9 px | 0.37 | 1.33 | 303 |
| stroke 20 | 58 % → 79 % | 491.0 px | 0.37 | 1.36 | 399 |
| stroke 21 | 52 % → 65 % | 425.5 px | 0.37 | 1.25 | 373 |
| stroke 22 | 49 % → 55 % | 331.0 px | 0.36 | 1.13 | 344 |
| stroke 23 | 44 % → 51 % | 157.5 px | 0.31 | 1.16 | 238 |
| stroke 24 | 46 % → 46 % | 171.1 px | 0.30 | 1.00 | 197 |

Numbers say: wet paint spreads well beyond the stroke.

## Oil · Henry Ward · HW #05 rust, pink, green-black — own sheet
own sheet 600 × 600 · Oil 1.00 · 84 px · 27.3 s

![Oil · Henry Ward · HW #05 rust, pink, green-black — own sheet](Oil-Henry-Ward-HW-05-rust-pink-green-black-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 49 % → 62 % | 83.9 px | 0.62 | 1.28 | 1217 |
| stroke 2 | 63 % → 66 % | 148.1 px | 0.54 | 1.05 | 1664 |
| stroke 3 | 69 % → 69 % | 207.3 px | 0.43 | 1.00 | 1760 |
| stroke 4 | 71 % → 72 % | 218.5 px | 0.39 | 1.02 | 1841 |
| stroke 5 | 71 % → 69 % | 220.6 px | 0.39 | 0.98 | 1788 |
| stroke 6 | 70 % → 70 % | 216.1 px | 0.42 | 1.00 | 1684 |
| stroke 7 | 74 % → 61 % | 217.8 px | 0.45 | 0.83 | 1634 |
| stroke 8 | 93 % → 56 % | 217.2 px | 0.58 | 0.60 | 1835 |
| stroke 9 | 100 % → 47 % | 167.6 px | 0.73 | 0.47 | 1346 |
| stroke 10 | 19 % → 63 % | 56.8 px | 0.62 | 3.37 | 452 |
| stroke 11 | 27 % → 66 % | 113.0 px | 0.53 | 2.43 | 451 |
| stroke 12 | 34 % → 68 % | 172.9 px | 0.46 | 2.03 | 423 |
| stroke 13 | 36 % → 70 % | 202.9 px | 0.40 | 1.96 | 487 |
| stroke 14 | 55 % → 65 % | 248.2 px | 0.55 | 1.19 | 223 |
| stroke 15 | 48 % → 68 % | 239.8 px | 0.48 | 1.41 | 305 |
| stroke 16 | 37 % → 70 % | 250.6 px | 0.39 | 1.89 | 234 |
| stroke 17 | 39 % → 73 % | 221.7 px | 0.41 | 1.85 | 506 |
| stroke 18 | 39 % → 69 % | 209.3 px | 0.40 | 1.77 | 498 |
| stroke 19 | 38 % → 70 % | 189.5 px | 0.43 | 1.85 | 506 |
| stroke 20 | 48 % → 68 % | 316.2 px | 0.42 | 1.42 | 352 |
| stroke 21 | 52 % → 70 % | 446.1 px | 0.42 | 1.36 | 218 |
| stroke 22 | 53 % → 71 % | 473.3 px | 0.43 | 1.36 | 244 |
| stroke 23 | 48 % → 67 % | 280.1 px | 0.43 | 1.37 | 640 |
| stroke 24 | 49 % → 59 % | 231.5 px | 0.51 | 1.21 | 395 |
| stroke 25 | 53 % → 53 % | 195.0 px | 0.65 | 1.00 | 449 |

Numbers say: wet paint spreads well beyond the stroke.

## Oil · Henry Ward · HW #07 blue L and zigzag on lilac — own sheet
own sheet 600 × 600 · Oil 1.00 · 90 px · 29.4 s

![Oil · Henry Ward · HW #07 blue L and zigzag on lilac — own sheet](Oil-Henry-Ward-HW-07-blue-L-and-zigzag-on-lilac-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 44 % → 44 % | 79.5 px | 0.14 | 0.99 | 1176 |
| stroke 2 | 59 % → 54 % | 144.3 px | 0.20 | 0.93 | 1693 |
| stroke 3 | 67 % → 67 % | 203.8 px | 0.21 | 1.00 | 1794 |
| stroke 4 | 70 % → 66 % | 229.1 px | 0.20 | 0.94 | 1822 |
| stroke 5 | 69 % → 71 % | 226.5 px | 0.22 | 1.04 | 1848 |
| stroke 6 | 69 % → 79 % | 227.6 px | 0.19 | 1.15 | 1614 |
| stroke 7 | 75 % → 74 % | 228.4 px | 0.15 | 0.99 | 1697 |
| stroke 8 | 94 % → 72 % | 229.0 px | 0.12 | 0.77 | 1823 |
| stroke 9 | 100 % → 70 % | 177.3 px | 0.12 | 0.70 | 1375 |
| stroke 10 | 10 % → 48 % | 26.2 px | 0.17 | 5.08 | 455 |
| stroke 11 | 20 % → 54 % | 69.5 px | 0.20 | 2.67 | 483 |
| stroke 12 | 18 % → 58 % | 73.1 px | 0.21 | 3.27 | 412 |
| stroke 13 | 23 % → 60 % | 90.8 px | 0.21 | 2.64 | 513 |
| stroke 14 | 29 % → 63 % | 125.5 px | 0.20 | 2.17 | 596 |
| stroke 15 | 31 % → 66 % | 142.0 px | 0.20 | 2.11 | 442 |
| stroke 16 | 36 % → 71 % | 164.8 px | 0.22 | 2.00 | 695 |
| stroke 17 | 38 % → 78 % | 179.1 px | 0.19 | 2.04 | 571 |
| stroke 18 | 46 % → 78 % | 210.1 px | 0.18 | 1.69 | 574 |
| stroke 19 | 48 % → 75 % | 204.0 px | 0.16 | 1.57 | 547 |
| stroke 20 | 53 % → 73 % | 199.1 px | 0.14 | 1.39 | 580 |
| stroke 21 | 62 % → 72 % | 208.2 px | 0.12 | 1.17 | 578 |
| stroke 22 | 68 % → 70 % | 203.9 px | 0.12 | 1.04 | 653 |
| stroke 23 | 66 % → 68 % | 364.6 px | 0.18 | 1.04 | 299 |
| stroke 24 | 71 % → 74 % | 470.4 px | 0.14 | 1.03 | 221 |
| stroke 25 | 68 % → 69 % | 254.1 px | 0.19 | 1.01 | 663 |
| stroke 26 | 72 % → 73 % | 777.7 px | 0.19 | 1.02 | 206 |
| stroke 27 | 73 % → 74 % | 714.7 px | 0.18 | 1.02 | 217 |
| stroke 28 | 75 % → 76 % | 1010.2 px | 0.20 | 1.02 | 168 |
| stroke 29 | 78 % → 79 % | 944.7 px | 0.17 | 1.01 | 115 |
| stroke 30 | 80 % → 80 % | 666.0 px | 0.17 | 1.00 | 178 |
| stroke 31 | 80 % → 80 % | 766.3 px | 0.17 | 1.00 | 119 |

Numbers say: wet paint spreads well beyond the stroke.

## Oil · Henry Ward · HW #08 crown and dark oval — own sheet
own sheet 600 × 600 · Oil 1.00 · 84 px · 24.4 s

![Oil · Henry Ward · HW #08 crown and dark oval — own sheet](Oil-Henry-Ward-HW-08-crown-and-dark-oval-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 48 % → 0 % | 82.1 px | 0.00 | 0.00 | 1185 |
| stroke 2 | 62 % → 0 % | 144.8 px | 0.00 | 0.00 | 1582 |
| stroke 3 | 70 % → 70 % | 207.3 px | 0.17 | 1.00 | 1771 |
| stroke 4 | 72 % → 11 % | 221.7 px | 0.17 | 0.15 | 1844 |
| stroke 5 | 70 % → 17 % | 218.0 px | 0.16 | 0.25 | 1934 |
| stroke 6 | 71 % → 19 % | 222.2 px | 0.18 | 0.27 | 1663 |
| stroke 7 | 75 % → 21 % | 218.1 px | 0.18 | 0.28 | 1642 |
| stroke 8 | 95 % → 20 % | 216.4 px | 0.18 | 0.21 | 2139 |
| stroke 9 | 100 % → 15 % | 168.5 px | 0.18 | 0.15 | 1815 |
| stroke 10 | 17 % → 0 % | 68.7 px | 0.00 | 0.00 | 452 |
| stroke 11 | 24 % → 0 % | 109.8 px | 0.00 | 0.00 | 412 |
| stroke 12 | 28 % → 4 % | 166.9 px | 0.17 | 0.16 | 329 |
| stroke 13 | 21 % → 14 % | 64.6 px | 0.18 | 0.63 | 636 |
| stroke 14 | 29 % → 17 % | 220.7 px | 0.16 | 0.57 | 333 |
| stroke 15 | 31 % → 19 % | 245.1 px | 0.18 | 0.60 | 276 |
| stroke 16 | 34 % → 19 % | 269.4 px | 0.18 | 0.55 | 550 |
| stroke 17 | 40 % → 22 % | 241.1 px | 0.17 | 0.55 | 452 |
| stroke 18 | 8 % → 20 % | 71.9 px | 0.18 | 2.33 | 453 |
| stroke 19 | 14 % → 19 % | 118.1 px | 0.18 | 1.37 | 460 |
| stroke 20 | 21 % → 21 % | 157.6 px | 0.18 | 1.00 | 462 |

Numbers say: wet paint spreads well beyond the stroke.

## Oil · Henry Ward · HW #10 green block over maroon — own sheet
own sheet 600 × 600 · Oil 1.00 · 84 px · 28.2 s

![Oil · Henry Ward · HW #10 green block over maroon — own sheet](Oil-Henry-Ward-HW-10-green-block-over-maroon-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 50 % → 39 % | 88.2 px | 0.27 | 0.79 | 1214 |
| stroke 2 | 62 % → 44 % | 145.5 px | 0.42 | 0.70 | 1616 |
| stroke 3 | 69 % → 46 % | 203.5 px | 0.50 | 0.67 | 1765 |
| stroke 4 | 70 % → 51 % | 218.2 px | 0.60 | 0.72 | 1902 |
| stroke 5 | 71 % → 55 % | 216.6 px | 0.68 | 0.77 | 1829 |
| stroke 6 | 70 % → 51 % | 217.8 px | 0.70 | 0.72 | 1843 |
| stroke 7 | 76 % → 43 % | 221.8 px | 0.68 | 0.56 | 1918 |
| stroke 8 | 94 % → 39 % | 216.9 px | 0.66 | 0.42 | 2232 |
| stroke 9 | 100 % → 31 % | 165.8 px | 0.58 | 0.31 | 1540 |
| stroke 10 | 14 % → 43 % | 75.5 px | 0.33 | 3.09 | 243 |
| stroke 11 | 19 % → 44 % | 115.5 px | 0.44 | 2.35 | 332 |
| stroke 12 | 23 % → 51 % | 206.1 px | 0.53 | 2.25 | 226 |
| stroke 13 | 33 % → 45 % | 205.5 px | 0.39 | 1.36 | 283 |
| stroke 14 | 28 % → 49 % | 234.4 px | 0.50 | 1.77 | 449 |
| stroke 15 | 26 % → 51 % | 247.2 px | 0.53 | 1.94 | 362 |
| stroke 16 | 27 % → 51 % | 184.0 px | 0.60 | 1.92 | 626 |
| stroke 17 | 29 % → 52 % | 200.7 px | 0.62 | 1.78 | 501 |
| stroke 18 | 31 % → 55 % | 216.0 px | 0.67 | 1.79 | 395 |
| stroke 19 | 31 % → 51 % | 235.5 px | 0.70 | 1.63 | 279 |
| stroke 20 | 33 % → 44 % | 212.0 px | 0.69 | 1.35 | 380 |
| stroke 21 | 39 % → 44 % | 144.7 px | 0.59 | 1.12 | 631 |
| stroke 22 | 37 % → 43 % | 262.4 px | 0.68 | 1.14 | 248 |
| stroke 23 | 37 % → 41 % | 211.0 px | 0.67 | 1.10 | 357 |
| stroke 24 | 34 % → 34 % | 156.5 px | 0.61 | 1.00 | 315 |

Numbers say: wet paint spreads well beyond the stroke.

## Oil · Henry Ward · HW #11 cream mass and purple balls — own sheet
own sheet 600 × 600 · Oil 1.00 · 84 px · 28.9 s

![Oil · Henry Ward · HW #11 cream mass and purple balls — own sheet](Oil-Henry-Ward-HW-11-cream-mass-and-purple-balls-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 49 % → 51 % | 82.2 px | 0.05 | 1.06 | 1143 |
| stroke 2 | 62 % → 54 % | 146.8 px | 0.05 | 0.87 | 1575 |
| stroke 3 | 70 % → 56 % | 206.4 px | 0.05 | 0.80 | 1787 |
| stroke 4 | 71 % → 61 % | 223.1 px | 0.07 | 0.86 | 1846 |
| stroke 5 | 70 % → 62 % | 216.7 px | 0.19 | 0.88 | 1813 |
| stroke 6 | 70 % → 62 % | 217.7 px | 0.32 | 0.89 | 1976 |
| stroke 7 | 75 % → 53 % | 219.1 px | 0.39 | 0.71 | 1864 |
| stroke 8 | 97 % → 51 % | 219.7 px | 0.52 | 0.53 | 2254 |
| stroke 9 | 100 % → 47 % | 172.9 px | 0.69 | 0.47 | 1819 |
| stroke 10 | 17 % → 53 % | 71.2 px | 0.06 | 3.22 | 420 |
| stroke 11 | 22 % → 54 % | 103.3 px | 0.05 | 2.43 | 586 |
| stroke 12 | 28 % → 56 % | 162.6 px | 0.05 | 2.00 | 432 |
| stroke 13 | 34 % → 62 % | 225.7 px | 0.05 | 1.82 | 418 |
| stroke 14 | 35 % → 61 % | 236.8 px | 0.07 | 1.76 | 412 |
| stroke 15 | 34 % → 62 % | 217.1 px | 0.17 | 1.82 | 405 |
| stroke 16 | 35 % → 62 % | 199.9 px | 0.25 | 1.77 | 451 |
| stroke 17 | 36 % → 60 % | 240.3 px | 0.33 | 1.68 | 346 |
| stroke 18 | 52 % → 54 % | 291.8 px | 0.05 | 1.03 | 449 |
| stroke 19 | 53 % → 55 % | 298.2 px | 0.05 | 1.03 | 442 |
| stroke 20 | 55 % → 56 % | 422.8 px | 0.05 | 1.02 | 367 |
| stroke 21 | 60 % → 62 % | 421.2 px | 0.05 | 1.02 | 528 |
| stroke 22 | 59 % → 62 % | 423.8 px | 0.09 | 1.04 | 392 |
| stroke 23 | 48 % → 62 % | 312.7 px | 0.21 | 1.28 | 343 |
| stroke 24 | 38 % → 61 % | 257.9 px | 0.33 | 1.62 | 331 |
| stroke 25 | 49 % → 61 % | 138.0 px | 0.37 | 1.26 | 770 |
| stroke 26 | 63 % → 71 % | 185.5 px | 0.39 | 1.14 | 718 |
| stroke 27 | 62 % → 62 % | 161.3 px | 0.40 | 1.00 | 493 |

Numbers say: wet paint spreads well beyond the stroke.

## Oil · Henry Ward · HW #13 blue scrub under red — own sheet
own sheet 600 × 600 · Oil 1.00 · 84 px · 25.7 s

![Oil · Henry Ward · HW #13 blue scrub under red — own sheet](Oil-Henry-Ward-HW-13-blue-scrub-under-red-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 50 % → 11 % | 87.5 px | 0.12 | 0.21 | 1550 |
| stroke 2 | 62 % → 27 % | 146.5 px | 0.09 | 0.44 | 2207 |
| stroke 3 | 70 % → 38 % | 207.5 px | 0.08 | 0.54 | 2393 |
| stroke 4 | 71 % → 51 % | 217.4 px | 0.09 | 0.73 | 2284 |
| stroke 5 | 71 % → 67 % | 218.3 px | 0.09 | 0.94 | 2108 |
| stroke 6 | 71 % → 76 % | 219.7 px | 0.09 | 1.07 | 1883 |
| stroke 7 | 75 % → 76 % | 221.0 px | 0.09 | 1.01 | 1591 |
| stroke 8 | 95 % → 75 % | 220.8 px | 0.10 | 0.79 | 1560 |
| stroke 9 | 100 % → 74 % | 171.1 px | 0.10 | 0.74 | 1118 |
| stroke 10 | 16 % → 11 % | 57.2 px | 0.12 | 0.70 | 215 |
| stroke 11 | 24 % → 31 % | 121.3 px | 0.09 | 1.31 | 214 |
| stroke 12 | 29 % → 40 % | 179.1 px | 0.08 | 1.36 | 205 |
| stroke 13 | 12 % → 47 % | 62.9 px | 0.09 | 3.92 | 316 |
| stroke 14 | 20 % → 54 % | 103.8 px | 0.09 | 2.66 | 323 |
| stroke 15 | 34 % → 68 % | 177.0 px | 0.09 | 2.02 | 281 |
| stroke 16 | 42 % → 73 % | 205.3 px | 0.09 | 1.72 | 340 |
| stroke 17 | 45 % → 76 % | 221.1 px | 0.09 | 1.68 | 307 |
| stroke 18 | 47 % → 76 % | 234.6 px | 0.09 | 1.62 | 328 |
| stroke 19 | 50 % → 76 % | 225.5 px | 0.10 | 1.53 | 274 |
| stroke 20 | 57 % → 75 % | 231.9 px | 0.10 | 1.32 | 300 |
| stroke 21 | 68 % → 74 % | 214.0 px | 0.10 | 1.09 | 264 |
| stroke 22 | 49 % → 49 % | 265.7 px | 0.09 | 1.01 | 317 |
| stroke 23 | 57 % → 59 % | 289.7 px | 0.09 | 1.02 | 306 |
| stroke 24 | 66 % → 67 % | 340.6 px | 0.09 | 1.02 | 235 |
| stroke 25 | 73 % → 76 % | 367.9 px | 0.09 | 1.03 | 242 |
| stroke 26 | 74 % → 76 % | 364.9 px | 0.09 | 1.04 | 319 |
| stroke 27 | 73 % → 76 % | 358.1 px | 0.10 | 1.04 | 278 |
| stroke 28 | 74 % → 76 % | 310.9 px | 0.10 | 1.02 | 324 |
| stroke 29 | 75 % → 75 % | 261.7 px | 0.10 | 1.00 | 293 |

Numbers say: wet paint spreads well beyond the stroke.

## Oil · Henry Ward · HW #14 olive totem on dark — own sheet
own sheet 600 × 600 · Oil 1.00 · 84 px · 22.3 s

![Oil · Henry Ward · HW #14 olive totem on dark — own sheet](Oil-Henry-Ward-HW-14-olive-totem-on-dark-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 49 % → 41 % | 84.1 px | 0.24 | 0.83 | 1575 |
| stroke 2 | 63 % → 49 % | 150.1 px | 0.23 | 0.79 | 1969 |
| stroke 3 | 69 % → 50 % | 204.3 px | 0.24 | 0.72 | 2163 |
| stroke 4 | 71 % → 57 % | 218.6 px | 0.24 | 0.80 | 2116 |
| stroke 5 | 71 % → 63 % | 216.2 px | 0.24 | 0.90 | 1681 |
| stroke 6 | 71 % → 60 % | 217.8 px | 0.23 | 0.85 | 1438 |
| stroke 7 | 75 % → 48 % | 218.2 px | 0.22 | 0.64 | 1299 |
| stroke 8 | 95 % → 47 % | 220.1 px | 0.21 | 0.50 | 1380 |
| stroke 9 | 100 % → 43 % | 168.5 px | 0.21 | 0.43 | 940 |
| stroke 10 | 16 % → 66 % | 65.6 px | 0.23 | 4.24 | 386 |
| stroke 11 | 29 % → 74 % | 127.5 px | 0.23 | 2.57 | 293 |
| stroke 12 | 40 % → 66 % | 180.2 px | 0.23 | 1.66 | 274 |
| stroke 13 | 35 % → 35 % | 176.0 px | 0.24 | 1.00 | 286 |
| stroke 14 | 40 % → 51 % | 199.0 px | 0.24 | 1.28 | 294 |
| stroke 15 | 45 % → 57 % | 250.5 px | 0.24 | 1.26 | 234 |
| stroke 16 | 34 % → 53 % | 198.3 px | 0.23 | 1.55 | 294 |
| stroke 17 | 34 % → 48 % | 201.4 px | 0.22 | 1.44 | 241 |
| stroke 18 | 42 % → 48 % | 211.5 px | 0.22 | 1.13 | 305 |
| stroke 19 | 45 % → 50 % | 275.3 px | 0.24 | 1.11 | 259 |
| stroke 20 | 48 % → 54 % | 310.2 px | 0.24 | 1.12 | 323 |
| stroke 21 | 51 % → 57 % | 313.3 px | 0.24 | 1.12 | 256 |
| stroke 22 | 57 % → 62 % | 361.9 px | 0.24 | 1.08 | 195 |
| stroke 23 | 62 % → 63 % | 371.6 px | 0.24 | 1.02 | 238 |
| stroke 24 | 57 % → 57 % | 350.8 px | 0.23 | 1.02 | 193 |
| stroke 25 | 49 % → 50 % | 286.1 px | 0.23 | 1.01 | 236 |
| stroke 26 | 48 % → 48 % | 282.2 px | 0.22 | 1.00 | 268 |
| stroke 27 | 48 % → 48 % | 250.0 px | 0.22 | 1.00 | 204 |

Numbers say: wet paint spreads well beyond the stroke.

