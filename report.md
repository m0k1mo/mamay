![All brushes](contact.png)

# Brush Lab — 150 brushes · 4 Nov 2026 at 20:23

Every sheet: 1500 × 600, ten strokes in a 5 × 2 grid — 1. light line · 2. heavy line · 3. pressure swell · 4. fast wave · 5. slow wave · 6. spiral · 7. loop · 8. tilted · 9. over the wet one · 10. long, no reload (cell 8 holds «tilted» and «over the wet one» crossed). The CPU reference of Mamay's paint engine; the wet layer settles 20 s at the end.

Columns: **covered** = share of the cell with paint right after the stroke → after settling; **width** = painted area of the stroke ÷ its length (px); **dark** = mean darkness of the painted pixels above the paper's own grain (0 = paper, 1 = black); **spread** = how far wet paint went beyond the stroke (1.0 = stayed); **ms** = the stroke on the CPU; long stroke: paint in each quarter of its length (it should run out: wet → streaks → dry tail).

## Ink Line
Ink · 12 px · 25.5 s

![Ink Line](Ink-Line.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 1 % → 4 % | 4.3 px | 0.55 | 2.45 | 60 |
| heavy line | 5 % → 6 % | 15.7 px | 0.68 | 1.14 | 91 |
| pressure swell | 3 % → 4 % | 11.3 px | 0.64 | 1.40 | 39 |
| fast wave | 10 % → 11 % | 11.2 px | 0.59 | 1.11 | 141 |
| slow wave | 8 % → 10 % | 9.6 px | 0.57 | 1.16 | 105 |
| spiral | 14 % → 15 % | 8.9 px | 0.49 | 1.07 | 171 |
| loop | 8 % → 9 % | 10.6 px | 0.61 | 1.15 | 89 |
| tilted | 5 % → 5 % | 14.3 px | 0.64 | 1.05 | 70 |
| over the wet one | 10 % → 11 % | 12.5 px | 0.64 | 1.15 | 31 |
| long, no reload | 18 % → 17 % | 8.1 px | 0.47 | 0.96 | 252 | quarters: 0.22 → 0.09 → 0.04 → 0.02

Numbers say: light vs heavy: width 4.3 → 15.7 px, dark 0.55 → 0.68; wet paint spreads well beyond the stroke.

## Dense Ink
Ink · 14 px · 25.9 s

![Dense Ink](Dense-Ink.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 5 % → 7 % | 15.2 px | 0.72 | 1.27 | 77 |
| heavy line | 7 % → 7 % | 19.1 px | 0.73 | 1.09 | 91 |
| pressure swell | 5 % → 6 % | 17.9 px | 0.72 | 1.18 | 70 |
| fast wave | 13 % → 13 % | 15.2 px | 0.69 | 1.01 | 160 |
| slow wave | 12 % → 12 % | 13.5 px | 0.67 | 1.04 | 154 |
| spiral | 18 % → 15 % | 12.2 px | 0.65 | 0.80 | 192 |
| loop | 11 % → 12 % | 14.8 px | 0.69 | 1.08 | 117 |
| tilted | 5 % → 6 % | 14.5 px | 0.72 | 1.07 | 58 |
| over the wet one | 12 % → 13 % | 17.7 px | 0.72 | 1.12 | 45 |
| long, no reload | 23 % → 15 % | 10.1 px | 0.64 | 0.66 | 285 | quarters: 0.30 → 0.12 → 0.04 → 0.02

Numbers say: light vs heavy: width 15.2 → 19.1 px, dark 0.72 → 0.73.

## Transparent Wash
Watercolor · 22 px · 26.7 s

![Transparent Wash](Transparent-Wash.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 2 % → 5 % | 6.9 px | 0.27 | 2.26 | 25 |
| heavy line | 7 % → 9 % | 20.4 px | 0.27 | 1.23 | 64 |
| pressure swell | 4 % → 6 % | 15.2 px | 0.28 | 1.54 | 54 |
| fast wave | 14 % → 16 % | 16.1 px | 0.20 | 1.17 | 140 |
| slow wave | 12 % → 15 % | 13.7 px | 0.21 | 1.28 | 180 |
| spiral | 18 % → 22 % | 11.9 px | 0.16 | 1.22 | 154 |
| loop | 11 % → 13 % | 14.5 px | 0.22 | 1.20 | 100 |
| tilted | 8 % → 8 % | 21.1 px | 0.24 | 1.06 | 46 |
| over the wet one | 13 % → 16 % | 16.4 px | 0.24 | 1.19 | 47 |
| long, no reload | 26 % → 32 % | 11.6 px | 0.13 | 1.22 | 251 | quarters: 0.11 → 0.04 → 0.02 → 0.01

Numbers say: light vs heavy: width 6.9 → 20.4 px, dark 0.27 → 0.27; wet paint spreads well beyond the stroke.

## Dry Brush
Gouache · 24 px · 25.3 s

![Dry Brush](Dry-Brush.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 5 % → 1 % | 13.8 px | 0.65 | 0.11 | 67 |
| heavy line | 6 % → 0 % | 18.4 px | 0.65 | 0.02 | 94 |
| pressure swell | 5 % → 0 % | 18.1 px | 0.65 | 0.09 | 87 |
| fast wave | 6 % → 1 % | 6.9 px | 0.65 | 0.08 | 130 |
| slow wave | 7 % → 0 % | 7.8 px | 0.65 | 0.07 | 212 |
| spiral | 7 % → 1 % | 4.4 px | 0.65 | 0.08 | 201 |
| loop | 9 % → 0 % | 12.2 px | 0.65 | 0.05 | 99 |
| tilted | 4 % → 3 % | 10.3 px | 0.65 | 0.89 | 67 |
| over the wet one | 9 % → 1 % | 14.3 px | 0.65 | 0.12 | 54 |
| long, no reload | 6 % → 1 % | 2.7 px | 0.65 | 0.15 | 309 | quarters: 0.12 → 0.00 → 0.00 → 0.00

Numbers say: light vs heavy: width 13.8 → 18.4 px, dark 0.65 → 0.65.

## Wax Crayon
Wax · 8 px · 9.5 s

![Wax Crayon](Wax-Crayon.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 1 % → 1 % | 2.5 px | 0.71 | 1.00 | 37 |
| heavy line | 1 % → 1 % | 3.9 px | 0.69 | 1.00 | 17 |
| pressure swell | 1 % → 1 % | 3.3 px | 0.70 | 1.00 | 26 |
| fast wave | 3 % → 3 % | 3.5 px | 0.69 | 1.00 | 62 |
| slow wave | 3 % → 3 % | 3.4 px | 0.70 | 1.00 | 61 |
| spiral | 5 % → 5 % | 3.3 px | 0.70 | 1.00 | 98 |
| loop | 3 % → 3 % | 3.3 px | 0.70 | 1.00 | 34 |
| tilted | 2 % → 2 % | 5.6 px | 0.68 | 1.00 | 46 |
| over the wet one | 3 % → 3 % | 3.6 px | 0.68 | 1.00 | 15 |
| long, no reload | 7 % → 7 % | 3.3 px | 0.70 | 1.00 | 127 | quarters: 0.06 → 0.06 → 0.06 → 0.06

Numbers say: light vs heavy: width 2.5 → 3.9 px, dark 0.71 → 0.69; the long stroke does not run out of paint.

## Oil Pastel
Wax · 12 px · 10.1 s

![Oil Pastel](Oil-Pastel.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 1 % → 1 % | 4.0 px | 0.68 | 1.00 | 42 |
| heavy line | 2 % → 2 % | 6.5 px | 0.68 | 1.00 | 35 |
| pressure swell | 2 % → 2 % | 5.7 px | 0.69 | 1.00 | 29 |
| fast wave | 5 % → 5 % | 5.7 px | 0.68 | 1.00 | 98 |
| slow wave | 5 % → 5 % | 5.5 px | 0.68 | 1.00 | 65 |
| spiral | 8 % → 8 % | 5.5 px | 0.68 | 1.00 | 130 |
| loop | 4 % → 4 % | 5.6 px | 0.68 | 1.00 | 97 |
| tilted | 2 % → 2 % | 6.8 px | 0.68 | 1.00 | 41 |
| over the wet one | 5 % → 5 % | 5.8 px | 0.68 | 1.00 | 32 |
| long, no reload | 13 % → 13 % | 5.6 px | 0.68 | 1.00 | 172 | quarters: 0.10 → 0.09 → 0.10 → 0.10

Numbers say: light vs heavy: width 4.0 → 6.5 px, dark 0.68 → 0.68; the long stroke does not run out of paint.

## Charcoal
Charcoal · 5 px · 9.3 s

![Charcoal](Charcoal.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 1 % → 1 % | 2.0 px | 0.74 | 1.00 | 32 |
| heavy line | 1 % → 1 % | 3.0 px | 0.74 | 1.00 | 8 |
| pressure swell | 1 % → 1 % | 2.7 px | 0.74 | 1.00 | 17 |
| fast wave | 2 % → 2 % | 2.7 px | 0.73 | 1.00 | 37 |
| slow wave | 2 % → 2 % | 2.6 px | 0.74 | 1.00 | 42 |
| spiral | 4 % → 4 % | 2.5 px | 0.74 | 1.00 | 79 |
| loop | 2 % → 2 % | 2.6 px | 0.74 | 1.00 | 26 |
| tilted | 2 % → 2 % | 4.3 px | 0.72 | 1.00 | 24 |
| over the wet one | 2 % → 2 % | 2.4 px | 0.72 | 1.00 | 15 |
| long, no reload | 6 % → 6 % | 2.7 px | 0.73 | 1.00 | 91 | quarters: 0.05 → 0.05 → 0.05 → 0.05

Numbers say: light vs heavy: width 2.0 → 3.0 px, dark 0.74 → 0.74; the long stroke does not run out of paint.

## Impasto
Heavy acrylic · 22 px · 14.6 s

![Impasto](Impasto.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 8 % → 8 % | 24.1 px | 0.71 | 0.93 | 76 |
| heavy line | 10 % → 9 % | 28.8 px | 0.69 | 0.94 | 122 |
| pressure swell | 7 % → 7 % | 28.1 px | 0.72 | 0.94 | 64 |
| fast wave | 20 % → 13 % | 23.4 px | 0.71 | 0.64 | 222 |
| slow wave | 21 % → 14 % | 24.5 px | 0.71 | 0.66 | 380 |
| spiral | 30 % → 14 % | 19.9 px | 0.71 | 0.46 | 283 |
| loop | 18 % → 14 % | 23.9 px | 0.71 | 0.77 | 128 |
| tilted | 8 % → 8 % | 21.7 px | 0.70 | 1.00 | 78 |
| over the wet one | 17 % → 15 % | 25.4 px | 0.70 | 0.91 | 61 |
| long, no reload | 33 % → 14 % | 14.9 px | 0.71 | 0.42 | 382 | quarters: 0.38 → 0.21 → 0.10 → 0.03

Numbers say: light vs heavy: width 24.1 → 28.8 px, dark 0.71 → 0.69.

## Oil Round
Oil · 18 px · 17.5 s

![Oil Round](Oil-Round.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 2 % → 2 % | 7.2 px | 0.75 | 1.00 | 39 |
| heavy line | 7 % → 7 % | 19.3 px | 0.73 | 1.00 | 89 |
| pressure swell | 4 % → 4 % | 13.7 px | 0.72 | 1.00 | 60 |
| fast wave | 11 % → 11 % | 12.8 px | 0.65 | 1.00 | 177 |
| slow wave | 8 % → 8 % | 9.0 px | 0.57 | 1.00 | 187 |
| spiral | 10 % → 10 % | 6.6 px | 0.50 | 1.00 | 213 |
| loop | 6 % → 6 % | 7.2 px | 0.45 | 1.00 | 105 |
| tilted | 4 % → 4 % | 10.1 px | 0.52 | 1.00 | 49 |
| over the wet one | 6 % → 6 % | 7.6 px | 0.52 | 1.00 | 51 |
| long, no reload | 15 % → 15 % | 6.9 px | 0.42 | 1.00 | 302 | quarters: 0.09 → 0.08 → 0.07 → 0.06

Numbers say: light vs heavy: width 7.2 → 19.3 px, dark 0.75 → 0.73.

## Palette Knife
Oil · 20 px · 16.6 s

![Palette Knife](Palette-Knife.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 8 % → 8 % | 21.9 px | 0.67 | 1.00 | 45 |
| heavy line | 8 % → 8 % | 22.5 px | 0.73 | 1.00 | 25 |
| pressure swell | 6 % → 6 % | 22.3 px | 0.74 | 1.00 | 7 |
| fast wave | 16 % → 16 % | 18.9 px | 0.50 | 1.00 | 29 |
| slow wave | 17 % → 17 % | 19.9 px | 0.43 | 1.00 | 43 |
| spiral | 17 % → 17 % | 11.3 px | 0.46 | 1.00 | 49 |
| loop | 16 % → 16 % | 21.0 px | 0.59 | 1.00 | 19 |
| tilted | 5 % → 5 % | 15.0 px | 0.72 | 1.00 | 8 |
| over the wet one | 13 % → 13 % | 21.0 px | 0.72 | 1.00 | 17 |
| long, no reload | 16 % → 16 % | 7.2 px | 0.49 | 1.00 | 45 | quarters: 0.29 → 0.05 → 0.00 → 0.00

Numbers say: light vs heavy: width 21.9 → 22.5 px, dark 0.67 → 0.73; pressure barely changes the width.

## Water
Watercolor · 20 px · 36.8 s · over bands of wet oil paint and oil pastel in turn (it works on paint already there: look at what it does to the bands; covered counts the bands too)

![Water](Water.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 25 % → 27 % | 73.8 px | 0.80 | 1.06 | 28 |
| heavy line | 24 % → 25 % | 69.8 px | 0.81 | 1.04 | 50 |
| pressure swell | 24 % → 25 % | 89.6 px | 0.81 | 1.03 | 23 |
| fast wave | 24 % → 26 % | 27.7 px | 0.81 | 1.07 | 110 |
| slow wave | 24 % → 25 % | 27.8 px | 0.81 | 1.06 | 144 |
| spiral | 24 % → 26 % | 15.9 px | 0.81 | 1.07 | 166 |
| loop | 24 % → 25 % | 31.1 px | 0.81 | 1.03 | 99 |
| tilted | 24 % → 24 % | 67.0 px | 0.81 | 1.00 | 60 |
| over the wet one | 24 % → 25 % | 0.0 px | 0.81 | 1.06 | 34 |
| long, no reload | 24 % → 26 % | 10.7 px | 0.81 | 1.08 | 390 | quarters: 0.21 → 0.27 → 0.18 → 0.27

Numbers say: light vs heavy: width 73.8 → 69.8 px, dark 0.80 → 0.81; pressure barely changes the width; the long stroke does not run out of paint.

## Blender
Pastel · 16 px · 22.3 s · over bands of wet oil paint and oil pastel in turn (it works on paint already there: look at what it does to the bands; covered counts the bands too)

![Blender](Blender.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 24 % → 24 % | 70.7 px | 0.81 | 1.00 | 16 |
| heavy line | 25 % → 25 % | 72.1 px | 0.80 | 1.00 | 33 |
| pressure swell | 24 % → 24 % | 91.3 px | 0.81 | 1.00 | 19 |
| fast wave | 26 % → 26 % | 30.0 px | 0.79 | 1.00 | 69 |
| slow wave | 26 % → 26 % | 29.9 px | 0.79 | 1.00 | 92 |
| spiral | 28 % → 28 % | 18.7 px | 0.77 | 1.00 | 115 |
| loop | 25 % → 25 % | 33.0 px | 0.80 | 1.00 | 85 |
| tilted | 25 % → 25 % | 70.1 px | 0.79 | 1.00 | 55 |
| over the wet one | 26 % → 26 % | 1.8 px | 0.79 | 1.00 | 27 |
| long, no reload | 30 % → 30 % | 13.7 px | 0.76 | 1.00 | 146 | quarters: 0.20 → 0.28 → 0.23 → 0.30

Numbers say: light vs heavy: width 70.7 → 72.1 px, dark 0.81 → 0.80; pressure barely changes the width; the long stroke does not run out of paint.

## Eraser
Eraser · 16 px · 21.8 s · over bands of wet oil paint and oil pastel in turn (it works on paint already there: look at what it does to the bands; covered counts the bands too)

![Eraser](Eraser.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 24 % → 24 % | 69.6 px | 0.82 | 1.00 | 23 |
| heavy line | 23 % → 23 % | 67.9 px | 0.82 | 1.00 | 20 |
| pressure swell | 23 % → 23 % | 87.3 px | 0.82 | 1.00 | 23 |
| fast wave | 22 % → 22 % | 25.7 px | 0.82 | 1.00 | 68 |
| slow wave | 22 % → 22 % | 25.7 px | 0.82 | 1.00 | 77 |
| spiral | 22 % → 22 % | 14.4 px | 0.82 | 1.00 | 128 |
| loop | 22 % → 22 % | 28.6 px | 0.82 | 1.00 | 64 |
| tilted | 23 % → 23 % | 65.1 px | 0.82 | 1.00 | 37 |
| over the wet one | 23 % → 23 % | 0.0 px | 0.82 | 1.00 | 28 |
| long, no reload | 20 % → 20 % | 8.9 px | 0.82 | 1.00 | 192 | quarters: 0.15 → 0.20 → 0.15 → 0.20

Numbers say: light vs heavy: width 69.6 → 67.9 px, dark 0.82 → 0.82; pressure barely changes the width; the long stroke does not run out of paint.

## Fan
Gouache · 30 px · 31.1 s

![Fan](Fan.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 9 % → 3 % | 25.6 px | 0.63 | 0.37 | 24 |
| heavy line | 11 % → 4 % | 30.9 px | 0.63 | 0.39 | 41 |
| pressure swell | 8 % → 5 % | 31.7 px | 0.63 | 0.55 | 36 |
| fast wave | 17 % → 5 % | 20.2 px | 0.63 | 0.26 | 113 |
| slow wave | 18 % → 5 % | 21.0 px | 0.63 | 0.25 | 161 |
| spiral | 24 % → 5 % | 15.5 px | 0.63 | 0.19 | 164 |
| loop | 17 % → 5 % | 22.7 px | 0.63 | 0.28 | 150 |
| tilted | 5 % → 6 % | 15.0 px | 0.63 | 1.05 | 42 |
| over the wet one | 16 % → 8 % | 29.7 px | 0.63 | 0.49 | 56 |
| long, no reload | 22 % → 5 % | 9.9 px | 0.63 | 0.22 | 340 | quarters: 0.29 → 0.07 → 0.01 → 0.00

Numbers say: light vs heavy: width 25.6 → 30.9 px, dark 0.63 → 0.63.

## Sponge
Gouache · 30 px · 30.8 s

![Sponge](Sponge.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 4 % → 0 % | 11.3 px | 0.62 | 0.12 | 36 |
| heavy line | 12 % → 2 % | 35.4 px | 0.62 | 0.14 | 55 |
| pressure swell | 7 % → 2 % | 27.9 px | 0.62 | 0.28 | 38 |
| fast wave | 20 % → 4 % | 23.2 px | 0.62 | 0.19 | 121 |
| slow wave | 21 % → 4 % | 23.8 px | 0.62 | 0.18 | 495 |
| spiral | 28 % → 4 % | 18.3 px | 0.62 | 0.14 | 229 |
| loop | 18 % → 5 % | 23.0 px | 0.62 | 0.29 | 147 |
| tilted | 7 % → 7 % | 18.2 px | 0.62 | 1.04 | 115 |
| over the wet one | 16 % → 6 % | 27.8 px | 0.62 | 0.37 | 57 |
| long, no reload | 29 % → 5 % | 12.9 px | 0.62 | 0.17 | 392 | quarters: 0.29 → 0.13 → 0.07 → 0.04

Numbers say: light vs heavy: width 11.3 → 35.4 px, dark 0.62 → 0.62.

## Ink — sumi brush
Watercolour 1.00 · 22 px · 30.9 s

![Ink — sumi brush](Ink-sumi-brush.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 8 % → 9 % | 23.9 px | 0.87 | 1.12 | 63 |
| heavy line | 13 % → 13 % | 38.1 px | 0.86 | 1.00 | 65 |
| pressure swell | 9 % → 10 % | 34.5 px | 0.87 | 1.05 | 46 |
| fast wave | 28 % → 28 % | 32.5 px | 0.81 | 1.00 | 168 |
| slow wave | 26 % → 26 % | 29.6 px | 0.82 | 1.02 | 341 |
| spiral | 38 % → 37 % | 25.3 px | 0.74 | 0.96 | 330 |
| loop | 22 % → 22 % | 28.5 px | 0.85 | 1.02 | 191 |
| tilted | 9 % → 9 % | 25.3 px | 0.86 | 1.01 | 96 |
| over the wet one | 20 % → 21 % | 30.7 px | 0.86 | 1.03 | 88 |
| long, no reload | 45 % → 40 % | 20.1 px | 0.70 | 0.89 | 491 | quarters: 0.55 → 0.40 → 0.23 → 0.14

Numbers say: light vs heavy: width 23.9 → 38.1 px, dark 0.87 → 0.86.

## Ink — wash
Watercolour 1.00 · 40 px · 33.1 s

![Ink — wash](Ink-wash.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 13 % → 13 % | 37.3 px | 0.42 | 1.02 | 85 |
| heavy line | 19 % → 19 % | 55.2 px | 0.35 | 1.01 | 112 |
| pressure swell | 13 % → 13 % | 48.2 px | 0.41 | 1.02 | 108 |
| fast wave | 41 % → 42 % | 47.8 px | 0.32 | 1.02 | 249 |
| slow wave | 39 % → 40 % | 45.3 px | 0.42 | 1.02 | 429 |
| spiral | 60 % → 62 % | 39.7 px | 0.33 | 1.02 | 430 |
| loop | 34 % → 34 % | 43.8 px | 0.39 | 1.01 | 236 |
| tilted | 15 % → 15 % | 40.7 px | 0.43 | 1.01 | 114 |
| over the wet one | 30 % → 31 % | 43.4 px | 0.43 | 1.02 | 80 |
| long, no reload | 71 % → 75 % | 32.0 px | 0.31 | 1.05 | 498 | quarters: 0.40 → 0.29 → 0.19 → 0.12

Numbers say: light vs heavy: width 37.3 → 55.2 px, dark 0.42 → 0.35.

## Ink — dry brush
Ink 1.00 · 30 px · 24.9 s

![Ink — dry brush](Ink-dry-brush.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 6 % → 5 % | 16.8 px | 0.82 | 0.87 | 95 |
| heavy line | 6 % → 5 % | 18.6 px | 0.82 | 0.78 | 168 |
| pressure swell | 5 % → 4 % | 18.0 px | 0.83 | 0.88 | 96 |
| fast wave | 11 % → 7 % | 13.2 px | 0.80 | 0.60 | 266 |
| slow wave | 12 % → 7 % | 13.5 px | 0.80 | 0.56 | 459 |
| spiral | 18 % → 7 % | 11.6 px | 0.78 | 0.41 | 467 |
| loop | 11 % → 7 % | 14.2 px | 0.79 | 0.66 | 225 |
| tilted | 6 % → 6 % | 16.3 px | 0.80 | 1.06 | 118 |
| over the wet one | 12 % → 11 % | 17.4 px | 0.80 | 0.93 | 92 |
| long, no reload | 19 % → 8 % | 8.4 px | 0.77 | 0.42 | 552 | quarters: 0.25 → 0.08 → 0.02 → 0.01

Numbers say: light vs heavy: width 16.8 → 18.6 px, dark 0.82 → 0.82; pressure barely changes the width.

## Ink — nib
Watercolour 1.00 · 5 px · 24.5 s

![Ink — nib](Ink-nib.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 2 % → 5 % | 5.5 px | 0.89 | 2.46 | 33 |
| heavy line | 2 % → 5 % | 6.4 px | 0.89 | 2.34 | 43 |
| pressure swell | 2 % → 4 % | 6.2 px | 0.89 | 2.53 | 22 |
| fast wave | 5 % → 8 % | 5.9 px | 0.89 | 1.63 | 76 |
| slow wave | 5 % → 8 % | 5.7 px | 0.89 | 1.70 | 84 |
| spiral | 8 % → 11 % | 5.0 px | 0.87 | 1.41 | 132 |
| loop | 4 % → 8 % | 5.7 px | 0.89 | 1.74 | 76 |
| tilted | 4 % → 4 % | 10.3 px | 0.89 | 1.02 | 30 |
| over the wet one | 6 % → 9 % | 6.1 px | 0.89 | 1.61 | 45 |
| long, no reload | 9 % → 12 % | 4.2 px | 0.85 | 1.30 | 162 | quarters: 0.24 → 0.11 → 0.07 → 0.05

Numbers say: light vs heavy: width 5.5 → 6.4 px, dark 0.89 → 0.89; wet paint spreads well beyond the stroke.

## 0.45 · Dry brush
Gouache 0.91 · Ink 0.07 · 34 px · 29.3 s

![0.45 · Dry brush](0-45-Dry-brush.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 8 % → 5 % | 24.2 px | 0.68 | 0.56 | 167 |
| heavy line | 9 % → 5 % | 25.9 px | 0.68 | 0.55 | 157 |
| pressure swell | 7 % → 4 % | 26.7 px | 0.68 | 0.62 | 117 |
| fast wave | 16 % → 5 % | 18.8 px | 0.68 | 0.31 | 373 |
| slow wave | 19 % → 6 % | 22.1 px | 0.68 | 0.33 | 593 |
| spiral | 26 % → 6 % | 17.1 px | 0.68 | 0.23 | 498 |
| loop | 16 % → 7 % | 21.2 px | 0.68 | 0.41 | 255 |
| tilted | 8 % → 8 % | 22.8 px | 0.68 | 1.02 | 140 |
| over the wet one | 17 % → 12 % | 24.3 px | 0.68 | 0.69 | 111 |
| long, no reload | 28 % → 7 % | 12.7 px | 0.68 | 0.25 | 701 | quarters: 0.33 → 0.22 → 0.14 → 0.12

Numbers say: light vs heavy: width 24.2 → 25.9 px, dark 0.68 → 0.68; pressure barely changes the width.

## Dry pastel
Pastel 1.00 · 26 px · 10.6 s

![Dry pastel](Dry-pastel.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 3 % → 3 % | 8.1 px | 0.38 | 1.00 | 44 |
| heavy line | 4 % → 4 % | 12.8 px | 0.39 | 1.00 | 43 |
| pressure swell | 3 % → 3 % | 11.7 px | 0.38 | 1.00 | 38 |
| fast wave | 10 % → 10 % | 11.8 px | 0.39 | 1.00 | 116 |
| slow wave | 10 % → 10 % | 11.3 px | 0.39 | 1.00 | 150 |
| spiral | 14 % → 14 % | 9.5 px | 0.38 | 1.00 | 136 |
| loop | 7 % → 7 % | 9.3 px | 0.39 | 1.00 | 84 |
| tilted | 3 % → 3 % | 8.3 px | 0.38 | 1.00 | 33 |
| over the wet one | 7 % → 7 % | 10.7 px | 0.38 | 1.00 | 34 |
| long, no reload | 18 % → 18 % | 8.2 px | 0.39 | 1.00 | 235 | quarters: 0.08 → 0.08 → 0.08 → 0.07

Numbers say: light vs heavy: width 8.1 → 12.8 px, dark 0.38 → 0.39; the long stroke does not run out of paint.

## 0.45 · Charcoal
Charcoal 1.00 · 18 px · 10.1 s

![0.45 · Charcoal](0-45-Charcoal.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 2 % → 2 % | 6.5 px | 0.80 | 1.00 | 33 |
| heavy line | 3 % → 3 % | 9.2 px | 0.80 | 1.00 | 28 |
| pressure swell | 2 % → 2 % | 8.8 px | 0.80 | 1.00 | 16 |
| fast wave | 7 % → 7 % | 8.5 px | 0.80 | 1.00 | 46 |
| slow wave | 7 % → 7 % | 8.0 px | 0.80 | 1.00 | 65 |
| spiral | 12 % → 12 % | 7.9 px | 0.80 | 1.00 | 70 |
| loop | 6 % → 6 % | 8.1 px | 0.80 | 1.00 | 38 |
| tilted | 3 % → 3 % | 7.5 px | 0.80 | 1.00 | 37 |
| over the wet one | 6 % → 6 % | 7.8 px | 0.80 | 1.00 | 22 |
| long, no reload | 17 % → 17 % | 7.7 px | 0.80 | 1.00 | 112 | quarters: 0.15 → 0.16 → 0.15 → 0.16

Numbers say: light vs heavy: width 6.5 → 9.2 px, dark 0.80 → 0.80; the long stroke does not run out of paint.

## Watercolour — wash
Watercolour 1.00 · 50 px · 35.1 s

![Watercolour — wash](Watercolour-wash.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 16 % → 16 % | 45.5 px | 0.22 | 1.01 | 90 |
| heavy line | 22 % → 22 % | 64.9 px | 0.19 | 1.00 | 133 |
| pressure swell | 15 % → 15 % | 56.1 px | 0.22 | 1.01 | 80 |
| fast wave | 48 % → 49 % | 55.5 px | 0.19 | 1.01 | 276 |
| slow wave | 46 % → 46 % | 53.3 px | 0.24 | 1.00 | 486 |
| spiral | 66 % → 66 % | 43.7 px | 0.21 | 1.00 | 429 |
| loop | 40 % → 40 % | 51.4 px | 0.22 | 1.00 | 257 |
| tilted | 18 % → 18 % | 49.7 px | 0.23 | 1.00 | 274 |
| over the wet one | 36 % → 36 % | 49.6 px | 0.23 | 1.01 | 117 |
| long, no reload | 84 % → 84 % | 37.7 px | 0.20 | 1.00 | 716 | quarters: 0.24 → 0.20 → 0.16 → 0.12

Numbers say: light vs heavy: width 45.5 → 64.9 px, dark 0.22 → 0.19.

## Watercolour — wet-in-wet
Watercolour 1.00 · 44 px · 36.4 s

![Watercolour — wet-in-wet](Watercolour-wet-in-wet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 13 % → 21 % | 38.4 px | 0.32 | 1.58 | 90 |
| heavy line | 19 % → 22 % | 54.6 px | 0.34 | 1.17 | 109 |
| pressure swell | 12 % → 17 % | 46.5 px | 0.35 | 1.34 | 61 |
| fast wave | 41 % → 49 % | 47.7 px | 0.33 | 1.19 | 233 |
| slow wave | 40 % → 48 % | 46.2 px | 0.40 | 1.21 | 373 |
| spiral | 63 % → 69 % | 41.5 px | 0.37 | 1.10 | 437 |
| loop | 34 % → 41 % | 44.4 px | 0.37 | 1.20 | 217 |
| tilted | 15 % → 16 % | 41.5 px | 0.36 | 1.06 | 141 |
| over the wet one | 31 % → 40 % | 44.1 px | 0.36 | 1.31 | 88 |
| long, no reload | 78 % → 87 % | 34.8 px | 0.36 | 1.12 | 589 | quarters: 0.40 → 0.37 → 0.32 → 0.26

Numbers say: light vs heavy: width 38.4 → 54.6 px, dark 0.32 → 0.34; wet paint spreads well beyond the stroke.

## Watercolour — glaze
Watercolour 1.00 · 38 px · 31.8 s

![Watercolour — glaze](Watercolour-glaze.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 13 % → 13 % | 36.6 px | 0.07 | 1.02 | 72 |
| heavy line | 19 % → 19 % | 55.4 px | 0.07 | 1.00 | 88 |
| pressure swell | 13 % → 13 % | 47.0 px | 0.07 | 1.02 | 64 |
| fast wave | 39 % → 40 % | 45.6 px | 0.07 | 1.01 | 209 |
| slow wave | 37 % → 37 % | 42.8 px | 0.07 | 1.01 | 467 |
| spiral | 59 % → 60 % | 38.8 px | 0.06 | 1.01 | 374 |
| loop | 33 % → 33 % | 42.6 px | 0.07 | 1.00 | 193 |
| tilted | 14 % → 14 % | 40.1 px | 0.07 | 1.00 | 127 |
| over the wet one | 30 % → 30 % | 42.3 px | 0.07 | 1.01 | 89 |
| long, no reload | 69 % → 70 % | 30.9 px | 0.06 | 1.01 | 501 | quarters: 0.06 → 0.05 → 0.03 → 0.02

Numbers say: light vs heavy: width 36.6 → 55.4 px, dark 0.07 → 0.07.

## Watercolour — granulating
Watercolour 1.00 · 44 px · 32.8 s

![Watercolour — granulating](Watercolour-granulating.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 14 % → 14 % | 41.4 px | 0.35 | 1.01 | 91 |
| heavy line | 21 % → 21 % | 60.4 px | 0.31 | 1.00 | 107 |
| pressure swell | 14 % → 14 % | 52.2 px | 0.34 | 1.01 | 71 |
| fast wave | 45 % → 45 % | 51.7 px | 0.29 | 1.01 | 239 |
| slow wave | 42 % → 42 % | 48.2 px | 0.35 | 1.01 | 519 |
| spiral | 62 % → 63 % | 41.0 px | 0.30 | 1.01 | 397 |
| loop | 37 % → 37 % | 47.6 px | 0.33 | 1.00 | 211 |
| tilted | 16 % → 16 % | 45.5 px | 0.36 | 1.00 | 130 |
| over the wet one | 33 % → 33 % | 46.2 px | 0.36 | 1.01 | 92 |
| long, no reload | 75 % → 76 % | 33.6 px | 0.29 | 1.01 | 576 | quarters: 0.34 → 0.26 → 0.20 → 0.14

Numbers say: light vs heavy: width 41.4 → 60.4 px, dark 0.35 → 0.31.

## Watercolour — dry brush
Watercolour 1.00 · 36 px · 27.0 s

![Watercolour — dry brush](Watercolour-dry-brush.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 10 % → 10 % | 27.9 px | 0.17 | 1.01 | 88 |
| heavy line | 14 % → 13 % | 39.9 px | 0.16 | 0.93 | 103 |
| pressure swell | 11 % → 11 % | 40.3 px | 0.16 | 0.98 | 63 |
| fast wave | 27 % → 20 % | 30.7 px | 0.13 | 0.74 | 377 |
| slow wave | 24 % → 17 % | 28.0 px | 0.14 | 0.71 | 409 |
| spiral | 34 % → 20 % | 22.4 px | 0.13 | 0.58 | 418 |
| loop | 21 % → 18 % | 27.1 px | 0.14 | 0.86 | 246 |
| tilted | 10 % → 10 % | 28.5 px | 0.17 | 1.00 | 123 |
| over the wet one | 21 % → 20 % | 31.3 px | 0.17 | 0.95 | 101 |
| long, no reload | 36 % → 19 % | 16.0 px | 0.14 | 0.54 | 579 | quarters: 0.09 → 0.03 → 0.01 → 0.00

Numbers say: light vs heavy: width 27.9 → 39.9 px, dark 0.17 → 0.16.

## Gouache
Gouache 1.00 · 30 px · 29.4 s

![Gouache](Gouache.png)

A light paint: laid on a grey sheet (on white it cannot be seen); **dark** = how far it is from the grey either way.

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 8 % → 4 % | 23.8 px | 0.28 | 0.49 | 77 |
| heavy line | 13 % → 4 % | 36.9 px | 0.28 | 0.33 | 91 |
| pressure swell | 10 % → 4 % | 36.7 px | 0.28 | 0.42 | 71 |
| fast wave | 24 % → 5 % | 27.4 px | 0.28 | 0.21 | 202 |
| slow wave | 24 % → 6 % | 27.5 px | 0.28 | 0.25 | 351 |
| spiral | 32 % → 6 % | 21.3 px | 0.28 | 0.18 | 366 |
| loop | 20 % → 6 % | 25.8 px | 0.28 | 0.30 | 173 |
| tilted | 9 % → 9 % | 25.0 px | 0.27 | 1.01 | 102 |
| over the wet one | 20 % → 10 % | 29.5 px | 0.27 | 0.52 | 95 |
| long, no reload | 34 % → 7 % | 15.1 px | 0.27 | 0.22 | 464 | quarters: 0.01 → 0.01 → 0.02 → 0.02

Numbers say: light vs heavy: width 23.8 → 36.9 px, dark 0.28 → 0.28; the long stroke does not run out of paint.

## Oil — alla prima
Oil 0.89 · Oil glaze 0.11 · 30 px · 13.6 s

![Oil — alla prima](Oil-alla-prima.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 9 % → 9 % | 26.4 px | 0.50 | 1.00 | 82 |
| heavy line | 9 % → 9 % | 27.4 px | 0.49 | 1.00 | 87 |
| pressure swell | 8 % → 8 % | 28.7 px | 0.50 | 1.00 | 69 |
| fast wave | 22 % → 22 % | 24.9 px | 0.47 | 1.00 | 199 |
| slow wave | 23 % → 23 % | 26.8 px | 0.50 | 1.00 | 374 |
| spiral | 36 % → 36 % | 23.8 px | 0.49 | 1.00 | 368 |
| loop | 19 % → 19 % | 25.2 px | 0.50 | 1.00 | 198 |
| tilted | 11 % → 11 % | 29.8 px | 0.50 | 1.00 | 113 |
| over the wet one | 20 % → 20 % | 25.0 px | 0.50 | 1.00 | 90 |
| long, no reload | 42 % → 42 % | 19.0 px | 0.47 | 1.00 | 551 | quarters: 0.29 → 0.23 → 0.21 → 0.17

Numbers say: light vs heavy: width 26.4 → 27.4 px, dark 0.50 → 0.49; pressure barely changes the width.

## Oil — impasto
Oil heavy 1.00 · 34 px · 18.6 s

![Oil — impasto](Oil-impasto.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 11 % → 11 % | 30.5 px | 0.23 | 1.00 | 84 |
| heavy line | 12 % → 12 % | 34.5 px | 0.23 | 1.00 | 108 |
| pressure swell | 9 % → 9 % | 34.4 px | 0.24 | 1.00 | 80 |
| fast wave | 27 % → 27 % | 30.8 px | 0.22 | 1.00 | 264 |
| slow wave | 30 % → 30 % | 34.5 px | 0.22 | 1.00 | 484 |
| spiral | 44 % → 44 % | 29.1 px | 0.21 | 1.00 | 442 |
| loop | 24 % → 24 % | 31.5 px | 0.22 | 1.00 | 232 |
| tilted | 12 % → 12 % | 32.6 px | 0.24 | 1.00 | 142 |
| over the wet one | 23 % → 23 % | 30.4 px | 0.24 | 1.00 | 102 |
| long, no reload | 49 % → 49 % | 22.0 px | 0.21 | 1.00 | 657 | quarters: 0.16 → 0.12 → 0.09 → 0.07

Numbers say: light vs heavy: width 30.5 → 34.5 px, dark 0.23 → 0.23.

## Oil — glaze
Oil glaze 1.00 · 40 px · 15.5 s

![Oil — glaze](Oil-glaze.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 9 % → 9 % | 27.0 px | 0.50 | 1.00 | 102 |
| heavy line | 13 % → 13 % | 38.3 px | 0.49 | 1.00 | 117 |
| pressure swell | 10 % → 10 % | 36.6 px | 0.50 | 1.00 | 83 |
| fast wave | 29 % → 29 % | 33.5 px | 0.49 | 1.00 | 235 |
| slow wave | 30 % → 30 % | 34.6 px | 0.50 | 1.00 | 401 |
| spiral | 46 % → 46 % | 30.1 px | 0.49 | 1.00 | 437 |
| loop | 24 % → 24 % | 31.4 px | 0.50 | 1.00 | 226 |
| tilted | 11 % → 11 % | 30.4 px | 0.50 | 1.00 | 126 |
| over the wet one | 23 % → 23 % | 32.5 px | 0.50 | 1.00 | 102 |
| long, no reload | 52 % → 52 % | 23.5 px | 0.49 | 1.00 | 649 | quarters: 0.34 → 0.30 → 0.27 → 0.22

Numbers say: light vs heavy: width 27.0 → 38.3 px, dark 0.50 → 0.49.

## Oil — scumble
Oil 1.00 · 36 px · 15.0 s

![Oil — scumble](Oil-scumble.png)

A light paint: laid on a grey sheet (on white it cannot be seen); **dark** = how far it is from the grey either way.

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 9 % → 9 % | 25.5 px | 0.25 | 1.00 | 100 |
| heavy line | 9 % → 9 % | 25.5 px | 0.24 | 1.00 | 134 |
| pressure swell | 8 % → 8 % | 29.6 px | 0.23 | 1.00 | 88 |
| fast wave | 17 % → 17 % | 19.9 px | 0.16 | 1.00 | 293 |
| slow wave | 21 % → 21 % | 24.1 px | 0.18 | 1.00 | 560 |
| spiral | 28 % → 28 % | 18.8 px | 0.14 | 1.00 | 513 |
| loop | 17 % → 17 % | 22.0 px | 0.20 | 1.00 | 287 |
| tilted | 10 % → 10 % | 27.8 px | 0.24 | 1.00 | 152 |
| over the wet one | 19 % → 19 % | 25.1 px | 0.24 | 1.00 | 175 |
| long, no reload | 30 % → 30 % | 13.3 px | 0.13 | 1.00 | 922 | quarters: 0.00 → 0.00 → 0.00 → 0.00

Numbers say: light vs heavy: width 25.5 → 25.5 px, dark 0.25 → 0.24; pressure barely changes the width.

## Acrylic — heavy body
Impasto 0.98 · 30 px · 15.1 s

![Acrylic — heavy body](Acrylic-heavy-body.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 9 % → 7 % | 26.7 px | 0.51 | 0.80 | 110 |
| heavy line | 10 % → 8 % | 29.1 px | 0.51 | 0.81 | 117 |
| pressure swell | 8 % → 7 % | 29.1 px | 0.53 | 0.88 | 88 |
| fast wave | 20 % → 11 % | 22.9 px | 0.52 | 0.57 | 265 |
| slow wave | 21 % → 14 % | 24.7 px | 0.52 | 0.65 | 394 |
| spiral | 30 % → 13 % | 19.6 px | 0.52 | 0.45 | 421 |
| loop | 18 % → 12 % | 23.5 px | 0.52 | 0.66 | 215 |
| tilted | 8 % → 8 % | 22.4 px | 0.52 | 0.99 | 115 |
| over the wet one | 17 % → 15 % | 25.8 px | 0.52 | 0.86 | 104 |
| long, no reload | 30 % → 16 % | 13.4 px | 0.52 | 0.52 | 515 | quarters: 0.25 → 0.14 → 0.09 → 0.07

Numbers say: light vs heavy: width 26.7 → 29.1 px, dark 0.51 → 0.51; pressure barely changes the width.

## Acrylic — fluid
Watercolour 1.00 · 36 px · 30.9 s

![Acrylic — fluid](Acrylic-fluid.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 12 % → 12 % | 34.8 px | 0.24 | 1.01 | 85 |
| heavy line | 18 % → 18 % | 52.6 px | 0.21 | 0.99 | 84 |
| pressure swell | 12 % → 12 % | 45.4 px | 0.23 | 1.00 | 76 |
| fast wave | 38 % → 38 % | 44.1 px | 0.19 | 0.98 | 213 |
| slow wave | 35 % → 35 % | 40.5 px | 0.22 | 1.00 | 333 |
| spiral | 55 % → 53 % | 36.0 px | 0.19 | 0.98 | 330 |
| loop | 31 % → 31 % | 40.2 px | 0.21 | 1.00 | 215 |
| tilted | 12 % → 12 % | 34.2 px | 0.24 | 1.00 | 121 |
| over the wet one | 27 % → 28 % | 42.3 px | 0.24 | 1.02 | 104 |
| long, no reload | 61 % → 58 % | 27.6 px | 0.19 | 0.95 | 594 | quarters: 0.20 → 0.14 → 0.09 → 0.06

Numbers say: light vs heavy: width 34.8 → 52.6 px, dark 0.24 → 0.21.

## Acrylic — palette knife
Impasto 1.00 · 42 px · 19.5 s

![Acrylic — palette knife](Acrylic-palette-knife.png)

A light paint: laid on a grey sheet (on white it cannot be seen); **dark** = how far it is from the grey either way.

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 15 % → 15 % | 44.0 px | 0.39 | 0.98 | 31 |
| heavy line | 15 % → 15 % | 44.2 px | 0.40 | 0.98 | 31 |
| pressure swell | 12 % → 11 % | 43.5 px | 0.42 | 0.99 | 9 |
| fast wave | 36 % → 20 % | 41.9 px | 0.37 | 0.55 | 72 |
| slow wave | 37 % → 21 % | 42.7 px | 0.37 | 0.57 | 117 |
| spiral | 47 % → 18 % | 30.7 px | 0.37 | 0.39 | 177 |
| loop | 32 % → 24 % | 41.2 px | 0.36 | 0.77 | 91 |
| tilted | 12 % → 12 % | 33.6 px | 0.39 | 1.00 | 41 |
| over the wet one | 26 % → 25 % | 39.8 px | 0.39 | 0.97 | 45 |
| long, no reload | 53 % → 20 % | 23.6 px | 0.35 | 0.38 | 222 | quarters: 0.00 → 0.00 → 0.00 → 0.01

Numbers say: light vs heavy: width 44.0 → 44.2 px, dark 0.39 → 0.40; pressure barely changes the width; the long stroke does not run out of paint.

## Finger on oil
Oil 1.00 · 30 px · 13.2 s

![Finger on oil](Finger-on-oil.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 6 % → 6 % | 16.4 px | 0.36 | 1.00 | 52 |
| heavy line | 9 % → 9 % | 24.7 px | 0.32 | 1.00 | 66 |
| pressure swell | 6 % → 6 % | 22.3 px | 0.38 | 1.00 | 41 |
| fast wave | 11 % → 11 % | 12.5 px | 0.27 | 1.00 | 158 |
| slow wave | 15 % → 15 % | 17.7 px | 0.31 | 1.00 | 266 |
| spiral | 20 % → 20 % | 13.1 px | 0.27 | 1.00 | 271 |
| loop | 13 % → 13 % | 16.9 px | 0.31 | 1.00 | 130 |
| tilted | 9 % → 9 % | 23.8 px | 0.34 | 1.00 | 91 |
| over the wet one | 16 % → 16 % | 20.4 px | 0.34 | 1.00 | 62 |
| long, no reload | 23 % → 23 % | 10.4 px | 0.26 | 1.00 | 357 | quarters: 0.15 → 0.06 → 0.03 → 0.02

Numbers say: light vs heavy: width 16.4 → 24.7 px, dark 0.36 → 0.32.

## Palette knife — oil
Oil heavy 0.93 · Impasto 0.07 · 44 px · 19.2 s

![Palette knife — oil](Palette-knife-oil.png)

A light paint: laid on a grey sheet (on white it cannot be seen); **dark** = how far it is from the grey either way.

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 16 % → 14 % | 45.7 px | 0.37 | 0.90 | 40 |
| heavy line | 16 % → 16 % | 46.3 px | 0.38 | 0.98 | 47 |
| pressure swell | 12 % → 12 % | 45.2 px | 0.38 | 0.99 | 18 |
| fast wave | 39 % → 34 % | 44.9 px | 0.35 | 0.89 | 108 |
| slow wave | 39 % → 36 % | 45.4 px | 0.35 | 0.91 | 169 |
| spiral | 62 % → 37 % | 40.7 px | 0.35 | 0.60 | 191 |
| loop | 34 % → 31 % | 43.7 px | 0.36 | 0.92 | 98 |
| tilted | 13 % → 13 % | 36.6 px | 0.37 | 1.00 | 39 |
| over the wet one | 28 % → 27 % | 40.8 px | 0.37 | 0.97 | 45 |
| long, no reload | 74 % → 39 % | 33.0 px | 0.34 | 0.53 | 182 | quarters: 0.00 → 0.00 → 0.01 → 0.01

Numbers say: light vs heavy: width 45.7 → 46.3 px, dark 0.37 → 0.38; pressure barely changes the width; the long stroke does not run out of paint.

## 0.45 · Sponge
Watercolour 0.93 · Ink 0.07 · 46 px · 32.4 s

![0.45 · Sponge](0-45-Sponge.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 27 % → 25 % | 78.2 px | 0.12 | 0.95 | 66 |
| heavy line | 32 % → 29 % | 91.9 px | 0.12 | 0.92 | 109 |
| pressure swell | 24 % → 21 % | 90.6 px | 0.12 | 0.88 | 61 |
| fast wave | 59 % → 55 % | 68.5 px | 0.12 | 0.92 | 219 |
| slow wave | 61 % → 58 % | 70.4 px | 0.17 | 0.95 | 348 |
| spiral | 77 % → 75 % | 50.7 px | 0.16 | 0.97 | 310 |
| loop | 53 % → 51 % | 69.1 px | 0.14 | 0.95 | 153 |
| tilted | 18 % → 18 % | 50.7 px | 0.17 | 1.00 | 98 |
| over the wet one | 45 % → 42 % | 73.6 px | 0.17 | 0.94 | 70 |
| long, no reload | 94 % → 89 % | 42.0 px | 0.17 | 0.95 | 448 | quarters: 0.17 → 0.18 → 0.16 → 0.14

Numbers say: light vs heavy: width 78.2 → 91.9 px, dark 0.12 → 0.12.

## 0.45 · Eraser
Watercolour 1.00 · 30 px · 20.4 s · over bands of wet oil paint and oil pastel in turn (it works on paint already there: look at what it does to the bands; covered counts the bands too)

![0.45 · Eraser](0-45-Eraser.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 24 % → 24 % | 69.2 px | 0.82 | 1.00 | 46 |
| heavy line | 23 % → 23 % | 67.4 px | 0.81 | 1.00 | 47 |
| pressure swell | 23 % → 23 % | 86.8 px | 0.82 | 1.00 | 35 |
| fast wave | 21 % → 21 % | 24.7 px | 0.81 | 1.00 | 121 |
| slow wave | 20 % → 20 % | 23.5 px | 0.82 | 1.00 | 195 |
| spiral | 20 % → 20 % | 13.5 px | 0.79 | 1.00 | 224 |
| loop | 21 % → 21 % | 27.8 px | 0.80 | 1.00 | 113 |
| tilted | 23 % → 23 % | 64.8 px | 0.81 | 1.00 | 57 |
| over the wet one | 22 % → 22 % | 0.0 px | 0.81 | 1.00 | 50 |
| long, no reload | 17 % → 17 % | 7.5 px | 0.79 | 1.00 | 324 | quarters: 0.13 → 0.16 → 0.13 → 0.17

Numbers say: light vs heavy: width 69.2 → 67.4 px, dark 0.82 → 0.81; pressure barely changes the width; the long stroke does not run out of paint.

## Lift wet paint
Watercolour 1.00 · 30 px · 19.9 s · over bands of wet oil paint and oil pastel in turn (it works on paint already there: look at what it does to the bands; covered counts the bands too)

![Lift wet paint](Lift-wet-paint.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 24 % → 24 % | 70.1 px | 0.82 | 1.00 | 47 |
| heavy line | 24 % → 24 % | 69.8 px | 0.82 | 1.00 | 35 |
| pressure swell | 24 % → 24 % | 89.6 px | 0.82 | 1.00 | 32 |
| fast wave | 24 % → 24 % | 27.7 px | 0.82 | 1.00 | 93 |
| slow wave | 24 % → 24 % | 27.7 px | 0.82 | 1.00 | 170 |
| spiral | 24 % → 24 % | 15.9 px | 0.82 | 1.00 | 158 |
| loop | 24 % → 24 % | 31.1 px | 0.82 | 1.00 | 91 |
| tilted | 24 % → 24 % | 66.8 px | 0.82 | 1.00 | 57 |
| over the wet one | 24 % → 24 % | 0.0 px | 0.82 | 1.00 | 39 |
| long, no reload | 24 % → 24 % | 10.7 px | 0.82 | 1.00 | 269 | quarters: 0.18 → 0.24 → 0.17 → 0.24

Numbers say: light vs heavy: width 70.1 → 69.8 px, dark 0.82 → 0.82; pressure barely changes the width; the long stroke does not run out of paint.

## Sgraffito
Watercolour 1.00 · 10 px · 20.0 s · over bands of wet oil paint and oil pastel in turn (it works on paint already there: look at what it does to the bands; covered counts the bands too)

![Sgraffito](Sgraffito.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 24 % → 24 % | 69.9 px | 0.81 | 1.00 | 8 |
| heavy line | 24 % → 24 % | 69.8 px | 0.82 | 1.00 | 7 |
| pressure swell | 24 % → 24 % | 89.6 px | 0.82 | 1.00 | 6 |
| fast wave | 24 % → 24 % | 27.7 px | 0.82 | 1.00 | 26 |
| slow wave | 24 % → 24 % | 27.7 px | 0.82 | 1.00 | 17 |
| spiral | 24 % → 24 % | 15.9 px | 0.82 | 1.00 | 44 |
| loop | 24 % → 24 % | 31.1 px | 0.82 | 1.00 | 26 |
| tilted | 24 % → 24 % | 66.9 px | 0.82 | 1.00 | 5 |
| over the wet one | 24 % → 24 % | 0.0 px | 0.82 | 1.00 | 12 |
| long, no reload | 24 % → 24 % | 10.6 px | 0.82 | 1.00 | 52 | quarters: 0.17 → 0.24 → 0.17 → 0.24

Numbers say: light vs heavy: width 69.9 → 69.8 px, dark 0.81 → 0.82; pressure barely changes the width; the long stroke does not run out of paint.

## Brush Artist · Refs · #01 Henry Ward peach cloud
Gouache 1.00 · 44 px · 31.7 s

![Brush Artist · Refs · #01 Henry Ward peach cloud](Brush-Artist-Refs-01-Henry-Ward-peach-cloud.png)

A light paint: laid on a grey sheet (on white it cannot be seen); **dark** = how far it is from the grey either way.

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 12 % → 7 % | 34.3 px | 0.33 | 0.62 | 166 |
| heavy line | 13 % → 8 % | 37.7 px | 0.33 | 0.61 | 158 |
| pressure swell | 10 % → 7 % | 37.0 px | 0.34 | 0.71 | 117 |
| fast wave | 26 % → 8 % | 29.9 px | 0.33 | 0.32 | 323 |
| slow wave | 28 % → 11 % | 32.4 px | 0.33 | 0.38 | 608 |
| spiral | 40 % → 10 % | 26.2 px | 0.33 | 0.24 | 578 |
| loop | 25 % → 10 % | 31.9 px | 0.33 | 0.40 | 295 |
| tilted | 12 % → 12 % | 34.0 px | 0.33 | 0.99 | 170 |
| over the wet one | 24 % → 17 % | 32.3 px | 0.33 | 0.73 | 244 |
| long, no reload | 37 % → 12 % | 16.5 px | 0.33 | 0.33 | 803 | quarters: 0.01 → 0.02 → 0.03 → 0.03

Numbers say: light vs heavy: width 34.3 → 37.7 px, dark 0.33 → 0.33; pressure barely changes the width; the long stroke does not run out of paint.

## Brush Artist · Refs · #02 Henry Ward cream strokes
Gouache 1.00 · 46 px · 31.3 s

![Brush Artist · Refs · #02 Henry Ward cream strokes](Brush-Artist-Refs-02-Henry-Ward-cream-strokes.png)

A light paint: laid on a grey sheet (on white it cannot be seen); **dark** = how far it is from the grey either way.

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 12 % → 6 % | 35.0 px | 0.41 | 0.51 | 155 |
| heavy line | 13 % → 7 % | 37.4 px | 0.41 | 0.56 | 152 |
| pressure swell | 10 % → 6 % | 36.7 px | 0.42 | 0.66 | 103 |
| fast wave | 24 % → 7 % | 27.8 px | 0.41 | 0.30 | 358 |
| slow wave | 28 % → 9 % | 31.9 px | 0.41 | 0.34 | 615 |
| spiral | 39 % → 9 % | 25.7 px | 0.41 | 0.23 | 605 |
| loop | 25 % → 9 % | 31.8 px | 0.41 | 0.38 | 329 |
| tilted | 12 % → 12 % | 33.8 px | 0.41 | 0.99 | 186 |
| over the wet one | 24 % → 16 % | 32.5 px | 0.41 | 0.69 | 153 |
| long, no reload | 36 % → 11 % | 16.3 px | 0.41 | 0.30 | 814 | quarters: 0.01 → 0.02 → 0.03 → 0.03

Numbers say: light vs heavy: width 35.0 → 37.4 px, dark 0.41 → 0.41; pressure barely changes the width; the long stroke does not run out of paint.

## Brush Artist · Refs · #03 Henry Ward navy contours
Impasto 1.00 · 22 px · 13.8 s

![Brush Artist · Refs · #03 Henry Ward navy contours](Brush-Artist-Refs-03-Henry-Ward-navy-contours.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 7 % → 7 % | 21.6 px | 0.70 | 0.94 | 69 |
| heavy line | 8 % → 8 % | 23.6 px | 0.70 | 0.95 | 90 |
| pressure swell | 6 % → 6 % | 23.2 px | 0.73 | 0.94 | 161 |
| fast wave | 19 % → 12 % | 21.8 px | 0.72 | 0.65 | 185 |
| slow wave | 19 % → 13 % | 22.5 px | 0.72 | 0.68 | 303 |
| spiral | 29 % → 13 % | 19.4 px | 0.72 | 0.45 | 292 |
| loop | 17 % → 13 % | 21.5 px | 0.72 | 0.81 | 166 |
| tilted | 8 % → 8 % | 22.7 px | 0.71 | 1.00 | 96 |
| over the wet one | 16 % → 14 % | 21.4 px | 0.71 | 0.89 | 74 |
| long, no reload | 33 % → 13 % | 14.6 px | 0.72 | 0.41 | 449 | quarters: 0.36 → 0.29 → 0.19 → 0.06

Numbers say: light vs heavy: width 21.6 → 23.6 px, dark 0.70 → 0.70; pressure barely changes the width.

## Brush Artist · Refs · #04 Henry Ward grey cloud
Gouache 1.00 · 50 px · 32.7 s

![Brush Artist · Refs · #04 Henry Ward grey cloud](Brush-Artist-Refs-04-Henry-Ward-grey-cloud.png)

A light paint: laid on a grey sheet (on white it cannot be seen); **dark** = how far it is from the grey either way.

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 14 % → 9 % | 40.3 px | 0.32 | 0.65 | 138 |
| heavy line | 15 % → 9 % | 43.2 px | 0.32 | 0.63 | 172 |
| pressure swell | 11 % → 8 % | 41.9 px | 0.32 | 0.73 | 104 |
| fast wave | 26 % → 8 % | 29.7 px | 0.32 | 0.33 | 364 |
| slow wave | 32 % → 12 % | 37.2 px | 0.32 | 0.37 | 687 |
| spiral | 42 % → 11 % | 27.7 px | 0.32 | 0.27 | 658 |
| loop | 29 % → 12 % | 37.0 px | 0.32 | 0.41 | 343 |
| tilted | 13 % → 13 % | 37.0 px | 0.32 | 0.99 | 190 |
| over the wet one | 26 % → 20 % | 36.8 px | 0.32 | 0.75 | 152 |
| long, no reload | 42 % → 14 % | 18.7 px | 0.32 | 0.34 | 865 | quarters: 0.01 → 0.02 → 0.03 → 0.03

Numbers say: light vs heavy: width 40.3 → 43.2 px, dark 0.32 → 0.32; pressure barely changes the width; the long stroke does not run out of paint.

## Brush Artist · Refs · #05 Henry Ward green in rust loops
Impasto 1.00 · 20 px · 12.8 s

![Brush Artist · Refs · #05 Henry Ward green in rust loops](Brush-Artist-Refs-05-Henry-Ward-green-in-rust-loops.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 7 % → 6 % | 19.5 px | 0.55 | 0.94 | 68 |
| heavy line | 7 % → 7 % | 21.4 px | 0.55 | 0.94 | 80 |
| pressure swell | 6 % → 5 % | 21.5 px | 0.57 | 0.92 | 57 |
| fast wave | 17 % → 11 % | 19.8 px | 0.56 | 0.64 | 179 |
| slow wave | 18 % → 12 % | 20.4 px | 0.56 | 0.65 | 259 |
| spiral | 27 % → 11 % | 17.7 px | 0.55 | 0.42 | 301 |
| loop | 15 % → 12 % | 19.5 px | 0.55 | 0.80 | 162 |
| tilted | 8 % → 8 % | 21.7 px | 0.56 | 1.00 | 79 |
| over the wet one | 15 % → 13 % | 19.3 px | 0.56 | 0.86 | 84 |
| long, no reload | 29 % → 12 % | 12.8 px | 0.56 | 0.40 | 424 | quarters: 0.25 → 0.18 → 0.09 → 0.02

Numbers say: light vs heavy: width 19.5 → 21.4 px, dark 0.55 → 0.55; pressure barely changes the width.

## Brush Artist · Refs · #06 Henry Ward scrubbed grey
Gouache 1.00 · 50 px · 33.0 s

![Brush Artist · Refs · #06 Henry Ward scrubbed grey](Brush-Artist-Refs-06-Henry-Ward-scrubbed-grey.png)

A light paint: laid on a grey sheet (on white it cannot be seen); **dark** = how far it is from the grey either way.

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 14 % → 9 % | 40.3 px | 0.34 | 0.65 | 136 |
| heavy line | 15 % → 9 % | 43.2 px | 0.34 | 0.63 | 147 |
| pressure swell | 11 % → 8 % | 41.9 px | 0.34 | 0.73 | 102 |
| fast wave | 26 % → 8 % | 29.7 px | 0.34 | 0.33 | 370 |
| slow wave | 32 % → 12 % | 37.2 px | 0.34 | 0.37 | 645 |
| spiral | 42 % → 11 % | 27.7 px | 0.34 | 0.27 | 640 |
| loop | 29 % → 12 % | 37.0 px | 0.34 | 0.41 | 330 |
| tilted | 13 % → 13 % | 37.0 px | 0.34 | 0.99 | 200 |
| over the wet one | 26 % → 20 % | 36.8 px | 0.34 | 0.75 | 166 |
| long, no reload | 42 % → 14 % | 18.7 px | 0.33 | 0.34 | 867 | quarters: 0.01 → 0.02 → 0.03 → 0.03

Numbers say: light vs heavy: width 40.3 → 43.2 px, dark 0.34 → 0.34; pressure barely changes the width; the long stroke does not run out of paint.

## Brush Artist · Refs · #07 Henry Ward blue L + black zigzag
Impasto 1.00 · 34 px · 15.1 s

![Brush Artist · Refs · #07 Henry Ward blue L + black zigzag](Brush-Artist-Refs-07-Henry-Ward-blue-L-black-zigzag.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 11 % → 11 % | 33.2 px | 0.58 | 0.93 | 104 |
| heavy line | 12 % → 12 % | 35.9 px | 0.58 | 0.93 | 98 |
| pressure swell | 9 % → 9 % | 35.3 px | 0.59 | 0.94 | 69 |
| fast wave | 29 % → 20 % | 33.7 px | 0.59 | 0.68 | 230 |
| slow wave | 30 % → 21 % | 34.2 px | 0.58 | 0.72 | 404 |
| spiral | 47 % → 22 % | 31.2 px | 0.58 | 0.45 | 444 |
| loop | 25 % → 21 % | 32.7 px | 0.58 | 0.82 | 228 |
| tilted | 11 % → 11 % | 30.0 px | 0.58 | 1.00 | 117 |
| over the wet one | 22 % → 20 % | 31.8 px | 0.58 | 0.91 | 91 |
| long, no reload | 53 % → 22 % | 23.5 px | 0.59 | 0.42 | 598 | quarters: 0.40 → 0.32 → 0.21 → 0.09

Numbers say: light vs heavy: width 33.2 → 35.9 px, dark 0.58 → 0.58; pressure barely changes the width.

## Brush Artist · Refs · #08 Henry Ward olive bands
Gouache 1.00 · 34 px · 21.6 s

![Brush Artist · Refs · #08 Henry Ward olive bands](Brush-Artist-Refs-08-Henry-Ward-olive-bands.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 4 % → 0 % | 10.7 px | 0.61 | 0.09 | 68 |
| heavy line | 7 % → 1 % | 21.4 px | 0.61 | 0.07 | 138 |
| pressure swell | 5 % → 1 % | 20.4 px | 0.61 | 0.16 | 81 |
| fast wave | 10 % → 1 % | 11.7 px | 0.61 | 0.08 | 221 |
| slow wave | 15 % → 1 % | 17.1 px | 0.61 | 0.09 | 374 |
| spiral | 21 % → 1 % | 13.6 px | 0.61 | 0.04 | 377 |
| loop | 13 % → 2 % | 17.3 px | 0.61 | 0.12 | 212 |
| tilted | 7 % → 7 % | 20.7 px | 0.61 | 0.97 | 101 |
| over the wet one | 14 % → 3 % | 18.8 px | 0.61 | 0.24 | 93 |
| long, no reload | 21 % → 2 % | 9.6 px | 0.61 | 0.07 | 571 | quarters: 0.24 → 0.14 → 0.08 → 0.06

Numbers say: light vs heavy: width 10.7 → 21.4 px, dark 0.61 → 0.61.

## Brush Artist · Refs · #09 Henry Ward white loops
Gouache 1.00 · 46 px · 31.8 s

![Brush Artist · Refs · #09 Henry Ward white loops](Brush-Artist-Refs-09-Henry-Ward-white-loops.png)

A light paint: laid on a grey sheet (on white it cannot be seen); **dark** = how far it is from the grey either way.

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 12 % → 6 % | 35.0 px | 0.44 | 0.51 | 123 |
| heavy line | 13 % → 7 % | 37.4 px | 0.44 | 0.56 | 173 |
| pressure swell | 10 % → 6 % | 36.7 px | 0.44 | 0.66 | 98 |
| fast wave | 24 % → 7 % | 27.8 px | 0.43 | 0.30 | 357 |
| slow wave | 28 % → 9 % | 31.9 px | 0.43 | 0.34 | 619 |
| spiral | 39 % → 9 % | 25.7 px | 0.43 | 0.23 | 575 |
| loop | 25 % → 9 % | 31.8 px | 0.43 | 0.38 | 320 |
| tilted | 12 % → 12 % | 33.8 px | 0.43 | 0.99 | 167 |
| over the wet one | 24 % → 16 % | 32.5 px | 0.43 | 0.69 | 139 |
| long, no reload | 36 % → 11 % | 16.3 px | 0.43 | 0.30 | 784 | quarters: 0.01 → 0.03 → 0.03 → 0.03

Numbers say: light vs heavy: width 35.0 → 37.4 px, dark 0.44 → 0.44; pressure barely changes the width; the long stroke does not run out of paint.

## Brush Artist · Refs · #10 Henry Ward maroon loops
Impasto 1.00 · 30 px · 15.2 s

![Brush Artist · Refs · #10 Henry Ward maroon loops](Brush-Artist-Refs-10-Henry-Ward-maroon-loops.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 10 % → 9 % | 28.1 px | 0.71 | 0.94 | 82 |
| heavy line | 10 % → 10 % | 30.3 px | 0.71 | 0.95 | 98 |
| pressure swell | 8 % → 8 % | 30.0 px | 0.73 | 0.94 | 61 |
| fast wave | 25 % → 17 % | 28.3 px | 0.73 | 0.70 | 219 |
| slow wave | 25 % → 18 % | 29.0 px | 0.73 | 0.73 | 353 |
| spiral | 39 % → 18 % | 25.9 px | 0.72 | 0.47 | 354 |
| loop | 21 % → 18 % | 27.6 px | 0.73 | 0.85 | 187 |
| tilted | 10 % → 10 % | 27.9 px | 0.72 | 1.00 | 113 |
| over the wet one | 20 % → 18 % | 27.0 px | 0.72 | 0.91 | 90 |
| long, no reload | 45 % → 18 % | 20.2 px | 0.73 | 0.41 | 501 | quarters: 0.44 → 0.38 → 0.30 → 0.21

Numbers say: light vs heavy: width 28.1 → 30.3 px, dark 0.71 → 0.71; pressure barely changes the width.

## Brush Artist · Refs · #11 Henry Ward purple spun balls
Impasto 1.00 · 36 px · 15.4 s

![Brush Artist · Refs · #11 Henry Ward purple spun balls](Brush-Artist-Refs-11-Henry-Ward-purple-spun-balls.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 12 % → 11 % | 34.2 px | 0.71 | 0.96 | 102 |
| heavy line | 13 % → 12 % | 36.7 px | 0.71 | 0.95 | 92 |
| pressure swell | 10 % → 9 % | 36.2 px | 0.74 | 0.95 | 77 |
| fast wave | 30 % → 22 % | 34.6 px | 0.73 | 0.75 | 233 |
| slow wave | 30 % → 24 % | 35.1 px | 0.73 | 0.79 | 449 |
| spiral | 49 % → 24 % | 32.3 px | 0.73 | 0.50 | 467 |
| loop | 26 % → 23 % | 33.4 px | 0.73 | 0.88 | 232 |
| tilted | 11 % → 11 % | 31.2 px | 0.73 | 1.00 | 119 |
| over the wet one | 23 % → 21 % | 32.3 px | 0.73 | 0.93 | 105 |
| long, no reload | 55 % → 24 % | 24.6 px | 0.73 | 0.44 | 660 | quarters: 0.51 → 0.47 → 0.38 → 0.27

Numbers say: light vs heavy: width 34.2 → 36.7 px, dark 0.71 → 0.71; pressure barely changes the width.

## Brush Artist · Refs · #12 Henry Ward black-olive cage
Gouache 1.00 · 28 px · 21.9 s

![Brush Artist · Refs · #12 Henry Ward black-olive cage](Brush-Artist-Refs-12-Henry-Ward-black-olive-cage.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 4 % → 0 % | 11.3 px | 0.64 | 0.09 | 55 |
| heavy line | 7 % → 1 % | 18.9 px | 0.64 | 0.08 | 115 |
| pressure swell | 5 % → 1 % | 17.5 px | 0.64 | 0.17 | 62 |
| fast wave | 9 % → 1 % | 10.5 px | 0.64 | 0.12 | 167 |
| slow wave | 13 % → 1 % | 15.0 px | 0.64 | 0.09 | 338 |
| spiral | 19 % → 1 % | 12.4 px | 0.64 | 0.06 | 411 |
| loop | 12 % → 2 % | 14.9 px | 0.64 | 0.14 | 154 |
| tilted | 6 % → 6 % | 17.9 px | 0.64 | 0.96 | 103 |
| over the wet one | 12 % → 3 % | 16.6 px | 0.64 | 0.26 | 92 |
| long, no reload | 20 % → 2 % | 9.0 px | 0.64 | 0.08 | 499 | quarters: 0.23 → 0.14 → 0.09 → 0.07

Numbers say: light vs heavy: width 11.3 → 18.9 px, dark 0.64 → 0.64.

## Brush Artist · Refs · #13 Henry Ward blue streaky form
Gouache 1.00 · 50 px · 33.4 s

![Brush Artist · Refs · #13 Henry Ward blue streaky form](Brush-Artist-Refs-13-Henry-Ward-blue-streaky-form.png)

A light paint: laid on a grey sheet (on white it cannot be seen); **dark** = how far it is from the grey either way.

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 14 % → 9 % | 40.3 px | 0.34 | 0.65 | 151 |
| heavy line | 15 % → 9 % | 43.2 px | 0.34 | 0.63 | 145 |
| pressure swell | 11 % → 8 % | 41.9 px | 0.34 | 0.73 | 105 |
| fast wave | 26 % → 8 % | 29.7 px | 0.34 | 0.33 | 352 |
| slow wave | 32 % → 12 % | 37.2 px | 0.34 | 0.37 | 684 |
| spiral | 42 % → 11 % | 27.7 px | 0.34 | 0.27 | 671 |
| loop | 29 % → 12 % | 37.0 px | 0.33 | 0.41 | 355 |
| tilted | 13 % → 13 % | 37.0 px | 0.34 | 0.99 | 219 |
| over the wet one | 26 % → 20 % | 36.8 px | 0.34 | 0.75 | 166 |
| long, no reload | 42 % → 14 % | 18.7 px | 0.33 | 0.34 | 887 | quarters: 0.01 → 0.02 → 0.03 → 0.03

Numbers say: light vs heavy: width 40.3 → 43.2 px, dark 0.34 → 0.34; pressure barely changes the width; the long stroke does not run out of paint.

## Brush Artist · Refs · #14 Henry Ward olive totem
Impasto 1.00 · 48 px · 17.9 s

![Brush Artist · Refs · #14 Henry Ward olive totem](Brush-Artist-Refs-14-Henry-Ward-olive-totem.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 15 % → 15 % | 44.9 px | 0.31 | 0.95 | 145 |
| heavy line | 16 % → 16 % | 47.8 px | 0.31 | 0.95 | 150 |
| pressure swell | 13 % → 12 % | 47.1 px | 0.32 | 0.95 | 107 |
| fast wave | 38 % → 30 % | 44.0 px | 0.30 | 0.78 | 352 |
| slow wave | 39 % → 31 % | 44.6 px | 0.30 | 0.81 | 580 |
| spiral | 58 % → 32 % | 38.1 px | 0.30 | 0.55 | 601 |
| loop | 33 % → 29 % | 42.7 px | 0.30 | 0.89 | 325 |
| tilted | 13 % → 13 % | 37.5 px | 0.31 | 1.00 | 187 |
| over the wet one | 28 % → 26 % | 41.3 px | 0.31 | 0.93 | 154 |
| long, no reload | 67 % → 33 % | 30.1 px | 0.30 | 0.49 | 928 | quarters: 0.25 → 0.18 → 0.09 → 0.03

Numbers say: light vs heavy: width 44.9 → 47.8 px, dark 0.31 → 0.31; pressure barely changes the width.

## Brush Artist · Refs · #15 Ultramarine brush script
Ink 1.00 · 4 px · 22.0 s

![Brush Artist · Refs · #15 Ultramarine brush script](Brush-Artist-Refs-15-Ultramarine-brush-script.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 1 % → 3 % | 2.2 px | 0.55 | 3.90 | 23 |
| heavy line | 6 % → 6 % | 16.7 px | 0.58 | 0.99 | 43 |
| pressure swell | 3 % → 4 % | 12.1 px | 0.64 | 1.15 | 31 |
| fast wave | 9 % → 7 % | 10.6 px | 0.54 | 0.81 | 70 |
| slow wave | 7 % → 7 % | 8.4 px | 0.54 | 0.93 | 78 |
| spiral | 11 % → 7 % | 7.2 px | 0.52 | 0.66 | 152 |
| loop | 7 % → 7 % | 9.2 px | 0.53 | 0.98 | 65 |
| tilted | 3 % → 3 % | 8.2 px | 0.62 | 1.02 | 34 |
| over the wet one | 7 % → 7 % | 11.5 px | 0.62 | 1.06 | 25 |
| long, no reload | 16 % → 8 % | 7.3 px | 0.50 | 0.48 | 225 | quarters: 0.15 → 0.04 → 0.01 → 0.00

Numbers say: light vs heavy: width 2.2 → 16.7 px, dark 0.55 → 0.58; wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #18 Blue oil-stick scribbles
Pastel 1.00 · 10 px · 9.4 s

![Brush Artist · Refs · #18 Blue oil-stick scribbles](Brush-Artist-Refs-18-Blue-oil-stick-scribbles.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 1 % → 1 % | 2.9 px | 0.52 | 1.00 | 17 |
| heavy line | 2 % → 2 % | 5.5 px | 0.53 | 1.00 | 30 |
| pressure swell | 1 % → 1 % | 5.0 px | 0.53 | 1.00 | 16 |
| fast wave | 4 % → 4 % | 4.8 px | 0.53 | 1.00 | 55 |
| slow wave | 4 % → 4 % | 4.4 px | 0.53 | 1.00 | 59 |
| spiral | 7 % → 7 % | 4.5 px | 0.52 | 1.00 | 109 |
| loop | 3 % → 3 % | 4.5 px | 0.52 | 1.00 | 38 |
| tilted | 2 % → 2 % | 4.8 px | 0.53 | 1.00 | 35 |
| over the wet one | 3 % → 3 % | 4.7 px | 0.53 | 1.00 | 16 |
| long, no reload | 10 % → 10 % | 4.4 px | 0.53 | 1.00 | 138 | quarters: 0.06 → 0.06 → 0.06 → 0.06

Numbers say: light vs heavy: width 2.9 → 5.5 px, dark 0.52 → 0.53; the long stroke does not run out of paint.

## Brush Artist · Refs · #20 Orange-red crayon scribble
Pastel 1.00 · 14 px · 9.7 s

![Brush Artist · Refs · #20 Orange-red crayon scribble](Brush-Artist-Refs-20-Orange-red-crayon-scribble.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 1 % → 1 % | 4.0 px | 0.53 | 1.00 | 19 |
| heavy line | 3 % → 3 % | 8.0 px | 0.53 | 1.00 | 22 |
| pressure swell | 2 % → 2 % | 7.6 px | 0.53 | 1.00 | 18 |
| fast wave | 6 % → 6 % | 7.2 px | 0.53 | 1.00 | 41 |
| slow wave | 6 % → 6 % | 6.6 px | 0.53 | 1.00 | 62 |
| spiral | 9 % → 9 % | 6.2 px | 0.53 | 1.00 | 94 |
| loop | 5 % → 5 % | 6.2 px | 0.53 | 1.00 | 60 |
| tilted | 2 % → 2 % | 5.6 px | 0.53 | 1.00 | 61 |
| over the wet one | 4 % → 4 % | 6.6 px | 0.53 | 1.00 | 16 |
| long, no reload | 13 % → 13 % | 5.7 px | 0.53 | 1.00 | 160 | quarters: 0.07 → 0.07 → 0.08 → 0.08

Numbers say: light vs heavy: width 4.0 → 8.0 px, dark 0.53 → 0.53; the long stroke does not run out of paint.

## Brush Artist · Refs · #21 Gritty black contours
Gouache 1.00 · 12 px · 16.6 s

![Brush Artist · Refs · #21 Gritty black contours](Brush-Artist-Refs-21-Gritty-black-contours.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 1 % → 0 % | 2.8 px | 0.81 | 0.02 | 48 |
| heavy line | 2 % → 0 % | 6.1 px | 0.00 | 0.00 | 92 |
| pressure swell | 2 % → 0 % | 6.2 px | 0.81 | 0.03 | 66 |
| fast wave | 2 % → 0 % | 2.3 px | 0.00 | 0.00 | 170 |
| slow wave | 4 % → 0 % | 4.1 px | 0.81 | 0.02 | 191 |
| spiral | 4 % → 0 % | 2.9 px | 0.81 | 0.01 | 302 |
| loop | 3 % → 0 % | 4.3 px | 0.81 | 0.01 | 159 |
| tilted | 3 % → 2 % | 7.1 px | 0.81 | 0.89 | 79 |
| over the wet one | 4 % → 0 % | 5.1 px | 0.81 | 0.04 | 87 |
| long, no reload | 5 % → 0 % | 2.2 px | 0.81 | 0.01 | 462 | quarters: 0.10 → 0.04 → 0.03 → 0.02

Numbers say: light vs heavy: width 2.8 → 6.1 px, dark 0.81 → 0.00.

## Brush Artist · Refs · #22 Bold black brush poster
Ink 1.00 · 20 px · 26.8 s

![Brush Artist · Refs · #22 Bold black brush poster](Brush-Artist-Refs-22-Bold-black-brush-poster.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 3 % → 5 % | 9.6 px | 0.79 | 1.64 | 34 |
| heavy line | 15 % → 15 % | 44.6 px | 0.88 | 0.99 | 91 |
| pressure swell | 9 % → 9 % | 31.9 px | 0.87 | 1.04 | 39 |
| fast wave | 27 % → 27 % | 31.7 px | 0.87 | 0.98 | 159 |
| slow wave | 22 % → 22 % | 25.3 px | 0.87 | 0.99 | 215 |
| spiral | 34 % → 32 % | 22.4 px | 0.87 | 0.94 | 244 |
| loop | 20 % → 20 % | 26.3 px | 0.88 | 1.00 | 136 |
| tilted | 8 % → 8 % | 23.1 px | 0.88 | 1.01 | 62 |
| over the wet one | 19 % → 19 % | 30.3 px | 0.88 | 1.00 | 56 |
| long, no reload | 45 % → 38 % | 20.3 px | 0.86 | 0.83 | 360 | quarters: 0.54 → 0.45 → 0.35 → 0.26

Numbers say: light vs heavy: width 9.6 → 44.6 px, dark 0.79 → 0.88; wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #23 Dry white on orange + black line
Gouache 1.00 · 50 px · 20.3 s

![Brush Artist · Refs · #23 Dry white on orange + black line](Brush-Artist-Refs-23-Dry-white-on-orange-black-line.png)

A light paint: laid on a grey sheet (on white it cannot be seen); **dark** = how far it is from the grey either way.

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 6 % → 0 % | 17.3 px | 0.00 | 0.00 | 79 |
| heavy line | 10 % → 0 % | 29.7 px | 0.41 | 0.00 | 209 |
| pressure swell | 7 % → 0 % | 27.2 px | 0.41 | 0.02 | 118 |
| fast wave | 13 % → 0 % | 15.3 px | 0.41 | 0.01 | 333 |
| slow wave | 20 % → 0 % | 22.8 px | 0.40 | 0.02 | 503 |
| spiral | 23 % → 0 % | 15.4 px | 0.40 | 0.01 | 556 |
| loop | 17 % → 0 % | 22.5 px | 0.40 | 0.03 | 286 |
| tilted | 9 % → 8 % | 24.0 px | 0.40 | 0.93 | 163 |
| over the wet one | 17 % → 1 % | 23.3 px | 0.40 | 0.08 | 144 |
| long, no reload | 27 % → 1 % | 12.2 px | 0.40 | 0.03 | 755 | quarters: 0.02 → 0.03 → 0.03 → 0.03

Numbers say: light vs heavy: width 17.3 → 29.7 px, dark 0.00 → 0.41; the long stroke does not run out of paint.

## Brush Artist · Refs · #24 Picasso flat oil
Oil 0.89 · Oil glaze 0.11 · 34 px · 14.1 s

![Brush Artist · Refs · #24 Picasso flat oil](Brush-Artist-Refs-24-Picasso-flat-oil.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 11 % → 11 % | 32.4 px | 0.40 | 1.00 | 136 |
| heavy line | 12 % → 12 % | 35.2 px | 0.39 | 1.00 | 115 |
| pressure swell | 9 % → 9 % | 34.5 px | 0.41 | 1.00 | 84 |
| fast wave | 30 % → 30 % | 34.2 px | 0.41 | 1.00 | 299 |
| slow wave | 30 % → 30 % | 35.0 px | 0.41 | 1.00 | 524 |
| spiral | 51 % → 51 % | 33.8 px | 0.39 | 1.00 | 538 |
| loop | 25 % → 25 % | 32.6 px | 0.40 | 1.00 | 255 |
| tilted | 11 % → 11 % | 32.1 px | 0.40 | 1.00 | 147 |
| over the wet one | 23 % → 23 % | 30.8 px | 0.40 | 1.00 | 127 |
| long, no reload | 62 % → 62 % | 27.6 px | 0.39 | 1.00 | 759 | quarters: 0.28 → 0.27 → 0.26 → 0.24

Numbers say: light vs heavy: width 32.4 → 35.2 px, dark 0.40 → 0.39; pressure barely changes the width.

## Brush Artist · Refs · #25 Yellow heavy flat stroke
Impasto 1.00 · 110 px · 34.7 s

![Brush Artist · Refs · #25 Yellow heavy flat stroke](Brush-Artist-Refs-25-Yellow-heavy-flat-stroke.png)

A light paint: laid on a grey sheet (on white it cannot be seen); **dark** = how far it is from the grey either way.

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 35 % → 36 % | 101.5 px | 0.30 | 1.02 | 363 |
| heavy line | 36 % → 35 % | 105.1 px | 0.31 | 0.97 | 407 |
| pressure swell | 28 % → 29 % | 105.5 px | 0.30 | 1.04 | 282 |
| fast wave | 73 % → 76 % | 83.8 px | 0.31 | 1.05 | 1030 |
| slow wave | 73 % → 72 % | 84.7 px | 0.30 | 0.98 | 1695 |
| spiral | 86 % → 83 % | 56.7 px | 0.29 | 0.97 | 1804 |
| loop | 65 % → 64 % | 83.6 px | 0.31 | 0.99 | 903 |
| tilted | 26 % → 26 % | 71.5 px | 0.30 | 1.00 | 522 |
| over the wet one | 55 % → 54 % | 83.2 px | 0.30 | 0.97 | 397 |
| long, no reload | 98 % → 97 % | 44.1 px | 0.30 | 0.99 | 2544 | quarters: 0.00 → 0.00 → 0.00 → 0.00

Numbers say: light vs heavy: width 101.5 → 105.1 px, dark 0.30 → 0.31; pressure barely changes the width; the long stroke does not run out of paint.

## Brush Artist · Refs · #27 Orange impasto swatch
Impasto 1.00 · 60 px · 20.4 s

![Brush Artist · Refs · #27 Orange impasto swatch](Brush-Artist-Refs-27-Orange-impasto-swatch.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 20 % → 19 % | 56.9 px | 0.34 | 0.97 | 175 |
| heavy line | 20 % → 20 % | 59.5 px | 0.34 | 0.97 | 174 |
| pressure swell | 16 % → 15 % | 59.6 px | 0.36 | 0.97 | 138 |
| fast wave | 48 % → 47 % | 55.1 px | 0.35 | 0.98 | 488 |
| slow wave | 48 % → 47 % | 55.9 px | 0.35 | 0.98 | 751 |
| spiral | 69 % → 62 % | 45.5 px | 0.34 | 0.91 | 820 |
| loop | 42 % → 40 % | 53.9 px | 0.35 | 0.97 | 444 |
| tilted | 16 % → 16 % | 44.0 px | 0.35 | 1.00 | 211 |
| over the wet one | 34 % → 33 % | 50.9 px | 0.35 | 0.96 | 188 |
| long, no reload | 85 % → 75 % | 38.1 px | 0.35 | 0.88 | 1147 | quarters: 0.33 → 0.31 → 0.30 → 0.26

Numbers say: light vs heavy: width 56.9 → 59.5 px, dark 0.34 → 0.34; pressure barely changes the width.

## Brush Artist · Refs · #28 Miles Davis black lines
Ink 1.00 · 22 px · 27.7 s

![Brush Artist · Refs · #28 Miles Davis black lines](Brush-Artist-Refs-28-Miles-Davis-black-lines.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 4 % → 6 % | 12.2 px | 0.81 | 1.49 | 33 |
| heavy line | 17 % → 17 % | 49.0 px | 0.88 | 0.99 | 79 |
| pressure swell | 10 % → 10 % | 35.9 px | 0.87 | 1.03 | 44 |
| fast wave | 31 % → 30 % | 35.4 px | 0.87 | 0.98 | 151 |
| slow wave | 25 % → 25 % | 28.7 px | 0.87 | 0.99 | 219 |
| spiral | 39 % → 37 % | 25.5 px | 0.87 | 0.95 | 341 |
| loop | 23 % → 23 % | 29.6 px | 0.88 | 1.00 | 139 |
| tilted | 9 % → 9 % | 25.3 px | 0.88 | 1.01 | 67 |
| over the wet one | 21 % → 21 % | 34.1 px | 0.88 | 1.01 | 62 |
| long, no reload | 51 % → 43 % | 22.9 px | 0.86 | 0.84 | 344 | quarters: 0.59 → 0.51 → 0.40 → 0.31

Numbers say: light vs heavy: width 12.2 → 49.0 px, dark 0.81 → 0.88.

## Brush Artist · Refs · #29 Shrigley magenta asterisk
Watercolour 1.00 · 70 px · 31.4 s

![Brush Artist · Refs · #29 Shrigley magenta asterisk](Brush-Artist-Refs-29-Shrigley-magenta-asterisk.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 10 % → 13 % | 28.0 px | 0.61 | 1.39 | 46 |
| heavy line | 17 % → 18 % | 50.3 px | 0.61 | 1.04 | 134 |
| pressure swell | 11 % → 13 % | 41.1 px | 0.62 | 1.14 | 64 |
| fast wave | 38 % → 38 % | 43.8 px | 0.60 | 1.01 | 251 |
| slow wave | 35 % → 39 % | 41.0 px | 0.62 | 1.11 | 401 |
| spiral | 61 % → 61 % | 40.0 px | 0.60 | 1.01 | 416 |
| loop | 31 % → 32 % | 40.2 px | 0.61 | 1.03 | 222 |
| tilted | 18 % → 18 % | 49.0 px | 0.61 | 1.00 | 198 |
| over the wet one | 31 % → 34 % | 38.5 px | 0.61 | 1.08 | 110 |
| long, no reload | 75 % → 76 % | 33.6 px | 0.60 | 1.01 | 654 | quarters: 0.53 → 0.50 → 0.48 → 0.45

Numbers say: light vs heavy: width 28.0 → 50.3 px, dark 0.61 → 0.61; the long stroke does not run out of paint.

## Brush Artist · Refs · #30 Red gouache face patch
Gouache 1.00 · 60 px · 39.1 s

![Brush Artist · Refs · #30 Red gouache face patch](Brush-Artist-Refs-30-Red-gouache-face-patch.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 16 % → 15 % | 47.0 px | 0.49 | 0.91 | 156 |
| heavy line | 25 % → 20 % | 73.9 px | 0.49 | 0.80 | 215 |
| pressure swell | 19 % → 17 % | 72.6 px | 0.49 | 0.86 | 134 |
| fast wave | 49 % → 28 % | 56.1 px | 0.49 | 0.58 | 432 |
| slow wave | 48 % → 28 % | 55.4 px | 0.49 | 0.59 | 724 |
| spiral | 60 % → 28 % | 39.3 px | 0.49 | 0.47 | 708 |
| loop | 40 % → 29 % | 51.6 px | 0.49 | 0.74 | 363 |
| tilted | 16 % → 17 % | 46.0 px | 0.49 | 1.00 | 228 |
| over the wet one | 36 % → 32 % | 55.3 px | 0.49 | 0.89 | 179 |
| long, no reload | 67 % → 30 % | 30.0 px | 0.49 | 0.44 | 1025 | quarters: 0.43 → 0.39 → 0.32 → 0.26

Numbers say: light vs heavy: width 47.0 → 73.9 px, dark 0.49 → 0.49.

## Brush Artist · Refs · #31 Warhol blotted line
Ink 1.00 · 6 px · 21.6 s

![Brush Artist · Refs · #31 Warhol blotted line](Brush-Artist-Refs-31-Warhol-blotted-line.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 1 % → 3 % | 2.7 px | 0.75 | 3.31 | 32 |
| heavy line | 7 % → 7 % | 20.7 px | 0.83 | 0.98 | 43 |
| pressure swell | 4 % → 4 % | 14.8 px | 0.84 | 1.12 | 29 |
| fast wave | 12 % → 9 % | 13.9 px | 0.82 | 0.76 | 90 |
| slow wave | 10 % → 8 % | 11.2 px | 0.80 | 0.84 | 108 |
| spiral | 15 % → 8 % | 9.7 px | 0.80 | 0.58 | 182 |
| loop | 9 % → 9 % | 11.9 px | 0.80 | 0.93 | 104 |
| tilted | 3 % → 3 % | 8.8 px | 0.84 | 1.03 | 43 |
| over the wet one | 8 % → 8 % | 14.4 px | 0.84 | 1.02 | 41 |
| long, no reload | 21 % → 9 % | 9.5 px | 0.78 | 0.43 | 259 | quarters: 0.25 → 0.13 → 0.04 → 0.01

Numbers say: light vs heavy: width 2.7 → 20.7 px, dark 0.75 → 0.83; wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #32 Thick orange swipes
Impasto 1.00 · 90 px · 31.2 s

![Brush Artist · Refs · #32 Thick orange swipes](Brush-Artist-Refs-32-Thick-orange-swipes.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 29 % → 29 % | 83.2 px | 0.37 | 1.00 | 284 |
| heavy line | 30 % → 29 % | 86.5 px | 0.38 | 0.97 | 316 |
| pressure swell | 23 % → 23 % | 86.6 px | 0.38 | 1.01 | 227 |
| fast wave | 63 % → 65 % | 73.1 px | 0.38 | 1.03 | 756 |
| slow wave | 64 % → 63 % | 73.5 px | 0.38 | 0.98 | 1380 |
| spiral | 79 % → 77 % | 52.2 px | 0.38 | 0.98 | 1268 |
| loop | 57 % → 56 % | 73.4 px | 0.38 | 0.99 | 787 |
| tilted | 21 % → 21 % | 59.3 px | 0.38 | 1.00 | 384 |
| over the wet one | 47 % → 45 % | 71.0 px | 0.38 | 0.97 | 307 |
| long, no reload | 95 % → 93 % | 42.8 px | 0.38 | 0.98 | 2668 | quarters: 0.38 → 0.38 → 0.37 → 0.35

Numbers say: light vs heavy: width 83.2 → 86.5 px, dark 0.37 → 0.38; pressure barely changes the width; the long stroke does not run out of paint.

## Brush Artist · Refs · #33 Red wet-in-wet band
Watercolour 1.00 · 80 px · 47.2 s

![Brush Artist · Refs · #33 Red wet-in-wet band](Brush-Artist-Refs-33-Red-wet-in-wet-band.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 24 % → 42 % | 69.9 px | 0.53 | 1.73 | 144 |
| heavy line | 34 % → 50 % | 97.7 px | 0.54 | 1.48 | 245 |
| pressure swell | 20 % → 30 % | 73.7 px | 0.57 | 1.54 | 168 |
| fast wave | 65 % → 80 % | 75.4 px | 0.61 | 1.22 | 469 |
| slow wave | 61 % → 78 % | 70.0 px | 0.63 | 1.29 | 834 |
| spiral | 78 % → 89 % | 51.5 px | 0.64 | 1.15 | 905 |
| loop | 54 % → 68 % | 70.2 px | 0.62 | 1.25 | 411 |
| tilted | 28 % → 30 % | 77.1 px | 0.57 | 1.08 | 355 |
| over the wet one | 55 % → 79 % | 75.2 px | 0.57 | 1.45 | 249 |
| long, no reload | 96 % → 99 % | 43.2 px | 0.66 | 1.03 | 1375 | quarters: 0.68 → 0.68 → 0.68 → 0.63

Numbers say: light vs heavy: width 69.9 → 97.7 px, dark 0.53 → 0.54; the long stroke does not run out of paint; wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #34 Magenta oil patches
Oil 0.89 · Oil glaze 0.11 · 60 px · 22.8 s

![Brush Artist · Refs · #34 Magenta oil patches](Brush-Artist-Refs-34-Magenta-oil-patches.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 19 % → 19 % | 55.9 px | 0.61 | 1.00 | 189 |
| heavy line | 21 % → 21 % | 59.9 px | 0.61 | 1.00 | 217 |
| pressure swell | 16 % → 16 % | 58.9 px | 0.62 | 1.01 | 139 |
| fast wave | 48 % → 49 % | 55.4 px | 0.62 | 1.02 | 576 |
| slow wave | 48 % → 48 % | 55.8 px | 0.62 | 1.00 | 903 |
| spiral | 70 % → 70 % | 46.3 px | 0.62 | 1.00 | 939 |
| loop | 42 % → 42 % | 54.3 px | 0.62 | 1.00 | 504 |
| tilted | 17 % → 17 % | 46.9 px | 0.61 | 1.00 | 246 |
| over the wet one | 35 % → 35 % | 50.1 px | 0.61 | 1.00 | 207 |
| long, no reload | 86 % → 86 % | 38.7 px | 0.62 | 1.00 | 1827 | quarters: 0.59 → 0.58 → 0.57 → 0.52

Numbers say: light vs heavy: width 55.9 → 59.9 px, dark 0.61 → 0.61; pressure barely changes the width; the long stroke does not run out of paint.

## Brush Artist · Refs · #35 Red band with runs
Watercolour 1.00 · 70 px · 49.5 s

![Brush Artist · Refs · #35 Red band with runs](Brush-Artist-Refs-35-Red-band-with-runs.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 40 % → 45 % | 115.4 px | 0.42 | 1.14 | 144 |
| heavy line | 46 % → 51 % | 133.2 px | 0.42 | 1.12 | 223 |
| pressure swell | 21 % → 28 % | 77.8 px | 0.48 | 1.36 | 151 |
| fast wave | 67 % → 77 % | 77.5 px | 0.49 | 1.14 | 677 |
| slow wave | 65 % → 75 % | 75.0 px | 0.52 | 1.16 | 1046 |
| spiral | 87 % → 94 % | 57.4 px | 0.53 | 1.09 | 727 |
| loop | 79 % → 88 % | 102.3 px | 0.48 | 1.11 | 463 |
| tilted | 50 % → 50 % | 138.2 px | 0.47 | 1.02 | 285 |
| over the wet one | 77 % → 84 % | 76.2 px | 0.47 | 1.10 | 308 |
| long, no reload | 97 % → 100 % | 43.5 px | 0.58 | 1.03 | 1063 | quarters: 0.60 → 0.60 → 0.59 → 0.56

Numbers say: light vs heavy: width 115.4 → 133.2 px, dark 0.42 → 0.42; the long stroke does not run out of paint.

## Brush Artist · Refs · #36 Magenta letters flat brush
Gouache 1.00 · 36 px · 34.4 s

![Brush Artist · Refs · #36 Magenta letters flat brush](Brush-Artist-Refs-36-Magenta-letters-flat-brush.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 10 % → 10 % | 29.0 px | 0.45 | 0.98 | 77 |
| heavy line | 17 % → 14 % | 49.0 px | 0.45 | 0.85 | 111 |
| pressure swell | 13 % → 12 % | 49.3 px | 0.45 | 0.89 | 87 |
| fast wave | 35 % → 19 % | 40.9 px | 0.45 | 0.54 | 263 |
| slow wave | 35 % → 19 % | 40.0 px | 0.45 | 0.54 | 471 |
| spiral | 46 % → 19 % | 30.4 px | 0.45 | 0.42 | 463 |
| loop | 27 % → 20 % | 35.4 px | 0.45 | 0.72 | 192 |
| tilted | 11 % → 11 % | 30.0 px | 0.45 | 1.00 | 104 |
| over the wet one | 24 % → 23 % | 38.1 px | 0.45 | 0.93 | 120 |
| long, no reload | 46 % → 19 % | 20.8 px | 0.45 | 0.40 | 668 | quarters: 0.29 → 0.26 → 0.22 → 0.18

Numbers say: light vs heavy: width 29.0 → 49.0 px, dark 0.45 → 0.45.

## Brush Artist · Refs · #37 Oil still life dabs
Oil 0.89 · Oil glaze 0.11 · 40 px · 15.4 s

![Brush Artist · Refs · #37 Oil still life dabs](Brush-Artist-Refs-37-Oil-still-life-dabs.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 13 % → 13 % | 38.0 px | 0.38 | 1.00 | 135 |
| heavy line | 14 % → 14 % | 41.1 px | 0.38 | 1.00 | 138 |
| pressure swell | 11 % → 11 % | 40.2 px | 0.40 | 1.00 | 113 |
| fast wave | 34 % → 35 % | 39.9 px | 0.39 | 1.00 | 423 |
| slow wave | 35 % → 35 % | 40.2 px | 0.39 | 1.00 | 758 |
| spiral | 59 % → 59 % | 38.7 px | 0.38 | 1.00 | 882 |
| loop | 29 % → 29 % | 37.8 px | 0.39 | 1.00 | 324 |
| tilted | 13 % → 13 % | 36.3 px | 0.39 | 1.00 | 177 |
| over the wet one | 26 % → 26 % | 35.8 px | 0.39 | 1.00 | 142 |
| long, no reload | 69 % → 69 % | 30.9 px | 0.37 | 1.00 | 948 | quarters: 0.31 → 0.30 → 0.27 → 0.24

Numbers say: light vs heavy: width 38.0 → 41.1 px, dark 0.38 → 0.38; pressure barely changes the width.

## Brush Artist · Refs · #38 Sanguine drawing
Pastel 1.00 · 6 px · 9.6 s

![Brush Artist · Refs · #38 Sanguine drawing](Brush-Artist-Refs-38-Sanguine-drawing.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 1 % → 1 % | 2.0 px | 0.61 | 1.00 | 9 |
| heavy line | 1 % → 1 % | 3.5 px | 0.62 | 1.00 | 17 |
| pressure swell | 1 % → 1 % | 3.3 px | 0.62 | 1.00 | 8 |
| fast wave | 3 % → 3 % | 3.2 px | 0.61 | 1.00 | 53 |
| slow wave | 3 % → 3 % | 3.0 px | 0.61 | 1.00 | 51 |
| spiral | 4 % → 4 % | 2.9 px | 0.61 | 1.00 | 104 |
| loop | 2 % → 2 % | 3.0 px | 0.61 | 1.00 | 50 |
| tilted | 1 % → 1 % | 3.4 px | 0.62 | 1.00 | 24 |
| over the wet one | 2 % → 2 % | 2.9 px | 0.62 | 1.00 | 24 |
| long, no reload | 7 % → 7 % | 3.0 px | 0.61 | 1.00 | 192 | quarters: 0.04 → 0.05 → 0.05 → 0.05

Numbers say: light vs heavy: width 2.0 → 3.5 px, dark 0.61 → 0.62; the long stroke does not run out of paint.

## Brush Artist · Refs · #39 Very thick impasto
Impasto 1.00 · 60 px · 21.4 s

![Brush Artist · Refs · #39 Very thick impasto](Brush-Artist-Refs-39-Very-thick-impasto.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 20 % → 19 % | 57.0 px | 0.60 | 0.97 | 190 |
| heavy line | 21 % → 20 % | 59.6 px | 0.60 | 0.97 | 192 |
| pressure swell | 16 % → 15 % | 59.7 px | 0.63 | 0.97 | 122 |
| fast wave | 48 % → 47 % | 55.2 px | 0.62 | 0.98 | 466 |
| slow wave | 49 % → 47 % | 56.1 px | 0.62 | 0.98 | 766 |
| spiral | 69 % → 65 % | 45.6 px | 0.62 | 0.93 | 769 |
| loop | 42 % → 41 % | 54.0 px | 0.62 | 0.97 | 438 |
| tilted | 16 % → 16 % | 44.1 px | 0.61 | 1.00 | 222 |
| over the wet one | 34 % → 33 % | 51.0 px | 0.61 | 0.97 | 182 |
| long, no reload | 85 % → 79 % | 38.3 px | 0.62 | 0.93 | 1174 | quarters: 0.58 → 0.57 → 0.55 → 0.52

Numbers say: light vs heavy: width 57.0 → 59.6 px, dark 0.60 → 0.60; pressure barely changes the width; the long stroke does not run out of paint.

## Brush Artist · Refs · #40 Watercolour blooms
Watercolour 1.00 · 90 px · 48.5 s

![Brush Artist · Refs · #40 Watercolour blooms](Brush-Artist-Refs-40-Watercolour-blooms.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 27 % → 46 % | 79.5 px | 0.08 | 1.69 | 158 |
| heavy line | 39 % → 53 % | 112.7 px | 0.09 | 1.36 | 298 |
| pressure swell | 26 % → 40 % | 98.0 px | 0.09 | 1.54 | 171 |
| fast wave | 68 % → 82 % | 78.6 px | 0.11 | 1.21 | 570 |
| slow wave | 68 % → 81 % | 78.9 px | 0.15 | 1.19 | 969 |
| spiral | 83 % → 93 % | 54.4 px | 0.15 | 1.13 | 935 |
| loop | 59 % → 72 % | 75.9 px | 0.13 | 1.24 | 489 |
| tilted | 33 % → 36 % | 93.0 px | 0.12 | 1.07 | 323 |
| over the wet one | 61 % → 81 % | 77.1 px | 0.12 | 1.33 | 208 |
| long, no reload | 98 % → 100 % | 43.9 px | 0.17 | 1.02 | 1371 | quarters: 0.21 → 0.20 → 0.17 → 0.12

Numbers say: light vs heavy: width 79.5 → 112.7 px, dark 0.08 → 0.09; wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #41 Coloured pencil hatching
Pastel 1.00 · 4 px · 8.8 s

![Brush Artist · Refs · #41 Coloured pencil hatching](Brush-Artist-Refs-41-Coloured-pencil-hatching.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 1 % → 1 % | 1.6 px | 0.42 | 1.00 | 6 |
| heavy line | 1 % → 1 % | 2.6 px | 0.43 | 1.00 | 12 |
| pressure swell | 1 % → 1 % | 2.1 px | 0.43 | 1.00 | 10 |
| fast wave | 2 % → 2 % | 2.2 px | 0.42 | 1.00 | 42 |
| slow wave | 2 % → 2 % | 2.1 px | 0.43 | 1.00 | 33 |
| spiral | 3 % → 3 % | 2.1 px | 0.43 | 1.00 | 50 |
| loop | 2 % → 2 % | 2.2 px | 0.43 | 1.00 | 24 |
| tilted | 1 % → 1 % | 3.0 px | 0.42 | 1.00 | 19 |
| over the wet one | 2 % → 2 % | 2.2 px | 0.42 | 1.00 | 8 |
| long, no reload | 5 % → 5 % | 2.3 px | 0.43 | 1.00 | 72 | quarters: 0.02 → 0.02 → 0.02 → 0.03

Numbers say: light vs heavy: width 1.6 → 2.6 px, dark 0.42 → 0.43; the long stroke does not run out of paint.

## Brush Artist · Refs · #42 Oil pastel shaggy
Pastel 1.00 · 18 px · 9.2 s

![Brush Artist · Refs · #42 Oil pastel shaggy](Brush-Artist-Refs-42-Oil-pastel-shaggy.png)

A light paint: laid on a grey sheet (on white it cannot be seen); **dark** = how far it is from the grey either way.

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 2 % → 2 % | 5.1 px | 0.35 | 1.00 | 15 |
| heavy line | 4 % → 4 % | 10.7 px | 0.36 | 1.00 | 28 |
| pressure swell | 3 % → 3 % | 9.5 px | 0.36 | 1.00 | 12 |
| fast wave | 8 % → 8 % | 9.0 px | 0.36 | 1.00 | 63 |
| slow wave | 7 % → 7 % | 8.2 px | 0.36 | 1.00 | 77 |
| spiral | 12 % → 12 % | 7.8 px | 0.36 | 1.00 | 86 |
| loop | 6 % → 6 % | 7.9 px | 0.36 | 1.00 | 51 |
| tilted | 2 % → 2 % | 6.9 px | 0.36 | 1.00 | 34 |
| over the wet one | 6 % → 6 % | 8.5 px | 0.36 | 1.00 | 37 |
| long, no reload | 15 % → 15 % | 6.9 px | 0.36 | 1.00 | 163 | quarters: 0.00 → 0.00 → 0.00 → 0.00

Numbers say: light vs heavy: width 5.1 → 10.7 px, dark 0.35 → 0.36; the long stroke does not run out of paint.

## Brush Artist · Refs · #43 Dragged black ink blocks
Gouache 1.00 · 70 px · 27.2 s

![Brush Artist · Refs · #43 Dragged black ink blocks](Brush-Artist-Refs-43-Dragged-black-ink-blocks.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 10 % → 1 % | 30.5 px | 0.65 | 0.09 | 104 |
| heavy line | 17 % → 2 % | 48.7 px | 0.65 | 0.13 | 301 |
| pressure swell | 12 % → 3 % | 44.8 px | 0.65 | 0.25 | 153 |
| fast wave | 27 % → 3 % | 30.9 px | 0.65 | 0.12 | 471 |
| slow wave | 34 % → 4 % | 38.7 px | 0.65 | 0.12 | 881 |
| spiral | 43 % → 4 % | 28.2 px | 0.65 | 0.10 | 808 |
| loop | 31 % → 4 % | 39.7 px | 0.65 | 0.14 | 823 |
| tilted | 13 % → 13 % | 37.6 px | 0.65 | 0.99 | 277 |
| over the wet one | 28 % → 10 % | 40.7 px | 0.65 | 0.37 | 208 |
| long, no reload | 48 % → 7 % | 21.6 px | 0.65 | 0.15 | 1181 | quarters: 0.49 → 0.38 → 0.30 → 0.22

Numbers say: light vs heavy: width 30.5 → 48.7 px, dark 0.65 → 0.65.

## Brush Artist · Refs · #44 Blue looping ribbon
Oil 1.00 · 80 px · 26.5 s

![Brush Artist · Refs · #44 Blue looping ribbon](Brush-Artist-Refs-44-Blue-looping-ribbon.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 26 % → 27 % | 75.0 px | 0.72 | 1.04 | 227 |
| heavy line | 27 % → 27 % | 79.7 px | 0.72 | 1.00 | 279 |
| pressure swell | 21 % → 22 % | 78.2 px | 0.72 | 1.03 | 194 |
| fast wave | 61 % → 64 % | 70.3 px | 0.73 | 1.05 | 761 |
| slow wave | 61 % → 61 % | 70.0 px | 0.73 | 1.00 | 1323 |
| spiral | 78 % → 78 % | 51.3 px | 0.73 | 1.00 | 1581 |
| loop | 54 % → 54 % | 69.7 px | 0.73 | 1.00 | 1422 |
| tilted | 21 % → 21 % | 57.3 px | 0.72 | 1.00 | 373 |
| over the wet one | 44 % → 44 % | 64.9 px | 0.72 | 1.00 | 323 |
| long, no reload | 96 % → 96 % | 42.8 px | 0.73 | 1.00 | 1846 | quarters: 0.72 → 0.73 → 0.73 → 0.69

Numbers say: light vs heavy: width 75.0 → 79.7 px, dark 0.72 → 0.72; pressure barely changes the width; the long stroke does not run out of paint.

## Brush Artist · Refs · #45 Soft pastel pepper
Pastel 1.00 · 40 px · 11.3 s

![Brush Artist · Refs · #45 Soft pastel pepper](Brush-Artist-Refs-45-Soft-pastel-pepper.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 4 % → 4 % | 11.3 px | 0.53 | 1.00 | 44 |
| heavy line | 8 % → 8 % | 23.0 px | 0.53 | 1.00 | 51 |
| pressure swell | 5 % → 5 % | 19.5 px | 0.53 | 1.00 | 35 |
| fast wave | 17 % → 17 % | 19.4 px | 0.53 | 1.00 | 121 |
| slow wave | 15 % → 15 % | 17.1 px | 0.53 | 1.00 | 225 |
| spiral | 25 % → 25 % | 16.3 px | 0.53 | 1.00 | 220 |
| loop | 12 % → 12 % | 16.1 px | 0.53 | 1.00 | 109 |
| tilted | 5 % → 5 % | 12.8 px | 0.53 | 1.00 | 64 |
| over the wet one | 11 % → 11 % | 17.7 px | 0.53 | 1.00 | 41 |
| long, no reload | 30 % → 30 % | 13.6 px | 0.53 | 1.00 | 319 | quarters: 0.18 → 0.18 → 0.18 → 0.18

Numbers say: light vs heavy: width 11.3 → 23.0 px, dark 0.53 → 0.53; the long stroke does not run out of paint.

## Brush Artist · Refs · #46 Red-brown ink lips
Watercolour 1.00 · 50 px · 40.5 s

![Brush Artist · Refs · #46 Red-brown ink lips](Brush-Artist-Refs-46-Red-brown-ink-lips.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 15 % → 31 % | 43.2 px | 0.58 | 2.07 | 65 |
| heavy line | 22 % → 36 % | 62.9 px | 0.60 | 1.64 | 92 |
| pressure swell | 13 % → 22 % | 47.7 px | 0.64 | 1.71 | 69 |
| fast wave | 41 % → 64 % | 47.9 px | 0.64 | 1.55 | 234 |
| slow wave | 41 % → 63 % | 46.9 px | 0.67 | 1.54 | 618 |
| spiral | 65 % → 79 % | 42.7 px | 0.69 | 1.23 | 721 |
| loop | 37 % → 56 % | 47.7 px | 0.66 | 1.51 | 215 |
| tilted | 20 % → 23 % | 56.2 px | 0.60 | 1.12 | 141 |
| over the wet one | 41 % → 63 % | 57.1 px | 0.60 | 1.55 | 85 |
| long, no reload | 80 % → 96 % | 35.8 px | 0.70 | 1.20 | 567 | quarters: 0.71 → 0.71 → 0.70 → 0.65

Numbers say: light vs heavy: width 43.2 → 62.9 px, dark 0.58 → 0.60; the long stroke does not run out of paint; wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #47 Pink knife slabs
Impasto 1.00 · 90 px · 28.7 s

![Brush Artist · Refs · #47 Pink knife slabs](Brush-Artist-Refs-47-Pink-knife-slabs.png)

A light paint: laid on a grey sheet (on white it cannot be seen); **dark** = how far it is from the grey either way.

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 28 % → 27 % | 81.2 px | 0.29 | 0.97 | 181 |
| heavy line | 29 % → 28 % | 83.6 px | 0.29 | 0.97 | 241 |
| pressure swell | 22 % → 22 % | 83.5 px | 0.29 | 1.01 | 180 |
| fast wave | 61 % → 60 % | 70.3 px | 0.28 | 0.99 | 1062 |
| slow wave | 61 % → 59 % | 71.0 px | 0.27 | 0.96 | 1398 |
| spiral | 76 % → 57 % | 50.1 px | 0.27 | 0.76 | 968 |
| loop | 55 % → 54 % | 71.7 px | 0.28 | 0.97 | 449 |
| tilted | 21 % → 21 % | 59.3 px | 0.29 | 1.00 | 260 |
| over the wet one | 46 % → 44 % | 68.1 px | 0.29 | 0.96 | 212 |
| long, no reload | 92 % → 76 % | 41.4 px | 0.26 | 0.83 | 1259 | quarters: 0.00 → 0.00 → 0.00 → 0.00

Numbers say: light vs heavy: width 81.2 → 83.6 px, dark 0.29 → 0.29; pressure barely changes the width; the long stroke does not run out of paint.

## Brush Artist · Refs · #48 Black bands with drips
Gouache 1.00 · 70 px · 42.9 s

![Brush Artist · Refs · #48 Black bands with drips](Brush-Artist-Refs-48-Black-bands-with-drips.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 27 % → 24 % | 79.0 px | 0.64 | 0.87 | 175 |
| heavy line | 35 % → 29 % | 102.8 px | 0.64 | 0.82 | 243 |
| pressure swell | 25 % → 22 % | 91.9 px | 0.64 | 0.89 | 161 |
| fast wave | 64 % → 43 % | 74.0 px | 0.64 | 0.67 | 485 |
| slow wave | 61 % → 41 % | 70.7 px | 0.64 | 0.67 | 825 |
| spiral | 69 % → 39 % | 45.7 px | 0.64 | 0.56 | 879 |
| loop | 54 % → 42 % | 70.4 px | 0.64 | 0.77 | 446 |
| tilted | 29 % → 29 % | 80.7 px | 0.64 | 1.00 | 268 |
| over the wet one | 58 % → 49 % | 80.4 px | 0.64 | 0.85 | 214 |
| long, no reload | 78 % → 39 % | 34.9 px | 0.64 | 0.50 | 1252 | quarters: 0.61 → 0.57 → 0.51 → 0.42

Numbers say: light vs heavy: width 79.0 → 102.8 px, dark 0.64 → 0.64.

## Brush Artist · Refs · #49 Magenta letters round brush
Ink 1.00 · 30 px · 29.6 s

![Brush Artist · Refs · #49 Magenta letters round brush](Brush-Artist-Refs-49-Magenta-letters-round-brush.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 6 % → 8 % | 17.4 px | 0.50 | 1.29 | 36 |
| heavy line | 21 % → 21 % | 61.9 px | 0.51 | 0.99 | 117 |
| pressure swell | 12 % → 13 % | 46.3 px | 0.52 | 1.02 | 61 |
| fast wave | 39 % → 38 % | 44.8 px | 0.51 | 0.99 | 177 |
| slow wave | 32 % → 31 % | 36.7 px | 0.51 | 0.99 | 299 |
| spiral | 50 % → 49 % | 33.2 px | 0.51 | 0.97 | 283 |
| loop | 29 % → 29 % | 37.8 px | 0.51 | 1.00 | 160 |
| tilted | 11 % → 11 % | 30.9 px | 0.52 | 1.01 | 87 |
| over the wet one | 26 % → 26 % | 42.0 px | 0.52 | 1.01 | 69 |
| long, no reload | 62 % → 56 % | 27.7 px | 0.50 | 0.91 | 761 | quarters: 0.41 → 0.36 → 0.30 → 0.25

Numbers say: light vs heavy: width 17.4 → 61.9 px, dark 0.50 → 0.51.

## Brush Artist · Refs · #50 Thick swipes on photo
Impasto 1.00 · 40 px · 17.1 s

![Brush Artist · Refs · #50 Thick swipes on photo](Brush-Artist-Refs-50-Thick-swipes-on-photo.png)

A light paint: laid on a grey sheet (on white it cannot be seen); **dark** = how far it is from the grey either way.

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 13 % → 13 % | 38.1 px | 0.27 | 0.96 | 109 |
| heavy line | 14 % → 13 % | 40.2 px | 0.27 | 0.96 | 104 |
| pressure swell | 11 % → 10 % | 40.1 px | 0.25 | 0.95 | 80 |
| fast wave | 33 % → 31 % | 38.4 px | 0.25 | 0.93 | 287 |
| slow wave | 34 % → 32 % | 39.1 px | 0.26 | 0.95 | 462 |
| spiral | 58 % → 46 % | 38.5 px | 0.25 | 0.79 | 471 |
| loop | 28 % → 27 % | 36.9 px | 0.26 | 0.95 | 242 |
| tilted | 12 % → 12 % | 34.1 px | 0.26 | 1.00 | 140 |
| over the wet one | 25 % → 24 % | 35.3 px | 0.26 | 0.95 | 110 |
| long, no reload | 66 % → 46 % | 29.5 px | 0.24 | 0.69 | 757 | quarters: 0.00 → 0.00 → 0.00 → 0.00

Numbers say: light vs heavy: width 38.1 → 40.2 px, dark 0.27 → 0.27; pressure barely changes the width; the long stroke does not run out of paint.

## Brush Artist · Refs · Drag #e8b4a8
Gouache 1.00 · 40 px · 20.7 s

![Brush Artist · Refs · Drag #e8b4a8](Brush-Artist-Refs-Drag-e8b4a8.png)

A light paint: laid on a grey sheet (on white it cannot be seen); **dark** = how far it is from the grey either way.

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 4 % → 0 % | 12.7 px | 0.35 | 0.03 | 92 |
| heavy line | 5 % → 0 % | 14.4 px | 0.34 | 0.03 | 154 |
| pressure swell | 4 % → 0 % | 15.5 px | 0.34 | 0.07 | 247 |
| fast wave | 6 % → 0 % | 6.4 px | 0.34 | 0.05 | 262 |
| slow wave | 12 % → 0 % | 13.8 px | 0.34 | 0.02 | 634 |
| spiral | 10 % → 0 % | 6.6 px | 0.34 | 0.05 | 432 |
| loop | 8 % → 1 % | 10.3 px | 0.34 | 0.09 | 279 |
| tilted | 6 % → 5 % | 16.1 px | 0.34 | 0.90 | 151 |
| over the wet one | 10 % → 1 % | 12.4 px | 0.34 | 0.15 | 134 |
| long, no reload | 9 % → 1 % | 4.0 px | 0.34 | 0.10 | 576 | quarters: 0.01 → 0.01 → 0.02 → 0.02

Numbers say: light vs heavy: width 12.7 → 14.4 px, dark 0.35 → 0.34; the long stroke does not run out of paint.

## Brush Artist · Refs · Drag #e8e4e0
Gouache 1.00 · 40 px · 20.2 s

![Brush Artist · Refs · Drag #e8e4e0](Brush-Artist-Refs-Drag-e8e4e0.png)

A light paint: laid on a grey sheet (on white it cannot be seen); **dark** = how far it is from the grey either way.

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 4 % → 0 % | 12.7 px | 0.43 | 0.03 | 95 |
| heavy line | 5 % → 0 % | 14.4 px | 0.43 | 0.03 | 104 |
| pressure swell | 4 % → 0 % | 15.5 px | 0.43 | 0.07 | 83 |
| fast wave | 6 % → 0 % | 6.4 px | 0.43 | 0.05 | 367 |
| slow wave | 12 % → 0 % | 13.8 px | 0.42 | 0.02 | 544 |
| spiral | 10 % → 0 % | 6.6 px | 0.42 | 0.05 | 437 |
| loop | 8 % → 1 % | 10.3 px | 0.42 | 0.09 | 220 |
| tilted | 6 % → 5 % | 16.1 px | 0.42 | 0.90 | 143 |
| over the wet one | 10 % → 1 % | 12.4 px | 0.42 | 0.15 | 106 |
| long, no reload | 9 % → 1 % | 4.0 px | 0.42 | 0.10 | 590 | quarters: 0.01 → 0.02 → 0.02 → 0.02

Numbers say: light vs heavy: width 12.7 → 14.4 px, dark 0.43 → 0.43; the long stroke does not run out of paint.

## Brush Artist · Refs · Finger
Pastel 1.00 · 36 px · 20.0 s · over bands of wet oil paint and oil pastel in turn (it works on paint already there: look at what it does to the bands; covered counts the bands too)

![Brush Artist · Refs · Finger](Brush-Artist-Refs-Finger.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 25 % → 25 % | 73.8 px | 0.80 | 1.00 | 86 |
| heavy line | 27 % → 27 % | 78.6 px | 0.80 | 1.00 | 50 |
| pressure swell | 26 % → 26 % | 97.7 px | 0.80 | 1.00 | 37 |
| fast wave | 32 % → 32 % | 37.3 px | 0.78 | 1.00 | 118 |
| slow wave | 31 % → 31 % | 36.3 px | 0.78 | 1.00 | 194 |
| spiral | 38 % → 38 % | 25.2 px | 0.76 | 1.00 | 244 |
| loop | 30 % → 30 % | 39.5 px | 0.78 | 1.00 | 103 |
| tilted | 26 % → 26 % | 73.4 px | 0.78 | 1.00 | 77 |
| over the wet one | 29 % → 29 % | 6.8 px | 0.78 | 1.00 | 47 |
| long, no reload | 41 % → 41 % | 18.2 px | 0.76 | 1.00 | 312 | quarters: 0.25 → 0.37 → 0.34 → 0.39

Numbers say: light vs heavy: width 73.8 → 78.6 px, dark 0.80 → 0.80; pressure barely changes the width; the long stroke does not run out of paint.

## Brush Artist · Ink — wash
Watercolour 1.00 · 38 px · 31.0 s

![Brush Artist · Ink — wash](Brush-Artist-Ink-wash.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 11 % → 11 % | 31.6 px | 0.39 | 1.04 | 52 |
| heavy line | 19 % → 19 % | 54.3 px | 0.32 | 1.03 | 93 |
| pressure swell | 12 % → 13 % | 45.2 px | 0.37 | 1.04 | 77 |
| fast wave | 39 % → 41 % | 45.5 px | 0.31 | 1.04 | 227 |
| slow wave | 37 % → 38 % | 42.9 px | 0.37 | 1.03 | 309 |
| spiral | 58 % → 61 % | 38.6 px | 0.31 | 1.04 | 314 |
| loop | 32 % → 33 % | 41.9 px | 0.35 | 1.02 | 177 |
| tilted | 13 % → 14 % | 37.0 px | 0.38 | 1.04 | 100 |
| over the wet one | 29 % → 30 % | 42.8 px | 0.38 | 1.04 | 85 |
| long, no reload | 67 % → 72 % | 30.0 px | 0.29 | 1.07 | 461 | quarters: 0.34 → 0.27 → 0.19 → 0.12

Numbers say: light vs heavy: width 31.6 → 54.3 px, dark 0.39 → 0.32.

## Brush Artist · Ink — brush line
Ink 1.00 · 16 px · 25.1 s

![Brush Artist · Ink — brush line](Brush-Artist-Ink-brush-line.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 3 % → 5 % | 7.7 px | 0.78 | 1.81 | 56 |
| heavy line | 13 % → 13 % | 38.9 px | 0.88 | 0.99 | 93 |
| pressure swell | 8 % → 8 % | 28.4 px | 0.87 | 1.05 | 47 |
| fast wave | 24 % → 23 % | 28.0 px | 0.87 | 0.96 | 136 |
| slow wave | 20 % → 19 % | 22.6 px | 0.87 | 0.97 | 171 |
| spiral | 30 % → 27 % | 20.1 px | 0.86 | 0.89 | 229 |
| loop | 18 % → 18 % | 23.6 px | 0.88 | 1.00 | 128 |
| tilted | 7 % → 7 % | 20.5 px | 0.88 | 1.01 | 59 |
| over the wet one | 17 % → 17 % | 26.8 px | 0.88 | 1.00 | 42 |
| long, no reload | 42 % → 30 % | 18.9 px | 0.85 | 0.71 | 346 | quarters: 0.49 → 0.40 → 0.30 → 0.20

Numbers say: light vs heavy: width 7.7 → 38.9 px, dark 0.78 → 0.88; wet paint spreads well beyond the stroke.

## Brush Artist · Ink — dry brush
Gouache 1.00 · 30 px · 19.7 s

![Brush Artist · Ink — dry brush](Brush-Artist-Ink-dry-brush.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 3 % → 0 % | 9.8 px | 0.00 | 0.00 | 46 |
| heavy line | 6 % → 0 % | 16.0 px | 0.77 | 0.01 | 108 |
| pressure swell | 4 % → 0 % | 15.4 px | 0.77 | 0.05 | 71 |
| fast wave | 7 % → 0 % | 8.5 px | 0.77 | 0.05 | 182 |
| slow wave | 11 % → 0 % | 12.3 px | 0.77 | 0.03 | 336 |
| spiral | 14 % → 0 % | 9.0 px | 0.77 | 0.03 | 329 |
| loop | 9 % → 1 % | 12.0 px | 0.77 | 0.05 | 158 |
| tilted | 6 % → 5 % | 15.8 px | 0.77 | 0.94 | 91 |
| over the wet one | 10 % → 1 % | 13.2 px | 0.77 | 0.14 | 76 |
| long, no reload | 15 % → 1 % | 6.6 px | 0.77 | 0.05 | 451 | quarters: 0.23 → 0.13 → 0.09 → 0.08

Numbers say: light vs heavy: width 9.8 → 16.0 px, dark 0.00 → 0.77.

## Brush Artist · Watercolour — blue
Watercolour 0.93 · Ink 0.07 · 40 px · 28.4 s

![Brush Artist · Watercolour — blue](Brush-Artist-Watercolour-blue.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 6 % → 11 % | 16.2 px | 0.29 | 1.88 | 26 |
| heavy line | 11 % → 13 % | 31.9 px | 0.29 | 1.17 | 63 |
| pressure swell | 7 % → 9 % | 25.7 px | 0.30 | 1.38 | 41 |
| fast wave | 24 % → 27 % | 28.2 px | 0.29 | 1.12 | 130 |
| slow wave | 23 % → 32 % | 26.4 px | 0.31 | 1.41 | 210 |
| spiral | 39 % → 47 % | 25.6 px | 0.29 | 1.21 | 207 |
| loop | 20 % → 25 % | 25.7 px | 0.30 | 1.25 | 109 |
| tilted | 12 % → 12 % | 34.0 px | 0.30 | 1.00 | 79 |
| over the wet one | 21 % → 25 % | 25.2 px | 0.30 | 1.19 | 55 |
| long, no reload | 53 % → 59 % | 23.6 px | 0.30 | 1.12 | 339 | quarters: 0.23 → 0.21 → 0.19 → 0.16

Numbers say: light vs heavy: width 16.2 → 31.9 px, dark 0.29 → 0.29; wet paint spreads well beyond the stroke.

## Brush Artist · Watercolour — violet
Watercolour 0.93 · Ink 0.07 · 40 px · 28.6 s

![Brush Artist · Watercolour — violet](Brush-Artist-Watercolour-violet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 6 % → 11 % | 16.2 px | 0.36 | 1.88 | 28 |
| heavy line | 11 % → 13 % | 31.9 px | 0.37 | 1.17 | 67 |
| pressure swell | 7 % → 9 % | 25.7 px | 0.38 | 1.38 | 40 |
| fast wave | 24 % → 27 % | 28.2 px | 0.38 | 1.12 | 124 |
| slow wave | 23 % → 32 % | 26.4 px | 0.39 | 1.41 | 206 |
| spiral | 39 % → 47 % | 25.6 px | 0.37 | 1.21 | 211 |
| loop | 20 % → 25 % | 25.7 px | 0.38 | 1.25 | 106 |
| tilted | 12 % → 12 % | 34.0 px | 0.38 | 1.00 | 81 |
| over the wet one | 21 % → 25 % | 25.2 px | 0.38 | 1.19 | 51 |
| long, no reload | 53 % → 59 % | 23.6 px | 0.38 | 1.12 | 333 | quarters: 0.28 → 0.27 → 0.24 → 0.21

Numbers say: light vs heavy: width 16.2 → 31.9 px, dark 0.36 → 0.37; wet paint spreads well beyond the stroke.

## Brush Artist · Watercolour — teal
Watercolour 0.93 · Ink 0.07 · 40 px · 29.8 s

![Brush Artist · Watercolour — teal](Brush-Artist-Watercolour-teal.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 6 % → 11 % | 16.2 px | 0.23 | 1.88 | 27 |
| heavy line | 11 % → 13 % | 31.9 px | 0.23 | 1.17 | 61 |
| pressure swell | 7 % → 9 % | 25.7 px | 0.24 | 1.38 | 40 |
| fast wave | 24 % → 27 % | 28.2 px | 0.23 | 1.12 | 135 |
| slow wave | 23 % → 32 % | 26.4 px | 0.25 | 1.41 | 209 |
| spiral | 39 % → 47 % | 25.6 px | 0.23 | 1.21 | 200 |
| loop | 20 % → 25 % | 25.7 px | 0.24 | 1.25 | 112 |
| tilted | 12 % → 12 % | 34.0 px | 0.24 | 1.00 | 86 |
| over the wet one | 21 % → 25 % | 25.2 px | 0.24 | 1.19 | 52 |
| long, no reload | 53 % → 59 % | 23.6 px | 0.24 | 1.12 | 436 | quarters: 0.18 → 0.16 → 0.15 → 0.13

Numbers say: light vs heavy: width 16.2 → 31.9 px, dark 0.23 → 0.23; wet paint spreads well beyond the stroke.

## Brush Artist · Gouache
Gouache 1.00 · 30 px · 31.9 s

![Brush Artist · Gouache](Brush-Artist-Gouache.png)

A light paint: laid on a grey sheet (on white it cannot be seen); **dark** = how far it is from the grey either way.

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 8 % → 8 % | 24.4 px | 0.27 | 0.97 | 58 |
| heavy line | 15 % → 12 % | 42.8 px | 0.27 | 0.78 | 84 |
| pressure swell | 11 % → 9 % | 41.0 px | 0.27 | 0.85 | 56 |
| fast wave | 30 % → 14 % | 34.9 px | 0.26 | 0.45 | 183 |
| slow wave | 29 % → 14 % | 34.0 px | 0.26 | 0.47 | 297 |
| spiral | 40 % → 14 % | 26.6 px | 0.26 | 0.35 | 387 |
| loop | 24 % → 15 % | 30.6 px | 0.26 | 0.62 | 182 |
| tilted | 10 % → 10 % | 27.4 px | 0.27 | 1.01 | 95 |
| over the wet one | 22 % → 19 % | 32.9 px | 0.27 | 0.89 | 71 |
| long, no reload | 43 % → 15 % | 19.1 px | 0.26 | 0.35 | 493 | quarters: 0.01 → 0.01 → 0.01 → 0.01

Numbers say: light vs heavy: width 24.4 → 42.8 px, dark 0.27 → 0.27; the long stroke does not run out of paint.

## Brush Artist · Oil — bristle
Oil 0.89 · Oil glaze 0.11 · 30 px · 14.3 s

![Brush Artist · Oil — bristle](Brush-Artist-Oil-bristle.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 9 % → 9 % | 26.3 px | 0.53 | 1.00 | 101 |
| heavy line | 10 % → 10 % | 28.6 px | 0.54 | 1.00 | 100 |
| pressure swell | 8 % → 8 % | 28.2 px | 0.55 | 1.00 | 71 |
| fast wave | 24 % → 24 % | 27.3 px | 0.55 | 1.00 | 324 |
| slow wave | 25 % → 25 % | 28.3 px | 0.55 | 1.00 | 571 |
| spiral | 39 % → 39 % | 25.6 px | 0.54 | 1.00 | 714 |
| loop | 20 % → 20 % | 26.3 px | 0.54 | 1.00 | 246 |
| tilted | 11 % → 11 % | 29.9 px | 0.52 | 1.00 | 154 |
| over the wet one | 20 % → 20 % | 25.5 px | 0.52 | 1.00 | 128 |
| long, no reload | 50 % → 50 % | 22.4 px | 0.54 | 1.00 | 764 | quarters: 0.32 → 0.30 → 0.29 → 0.28

Numbers say: light vs heavy: width 26.3 → 28.6 px, dark 0.53 → 0.54; pressure barely changes the width; the long stroke does not run out of paint.

## Brush Artist · Charcoal — stick
Charcoal 0.78 · Pastel 0.22 · 28 px · 10.4 s

![Brush Artist · Charcoal — stick](Brush-Artist-Charcoal-stick.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 5 % → 5 % | 15.3 px | 0.85 | 1.00 | 18 |
| heavy line | 8 % → 8 % | 23.3 px | 0.85 | 1.00 | 24 |
| pressure swell | 5 % → 5 % | 19.8 px | 0.85 | 1.00 | 17 |
| fast wave | 18 % → 18 % | 20.7 px | 0.85 | 1.00 | 67 |
| slow wave | 17 % → 17 % | 19.5 px | 0.85 | 1.00 | 127 |
| spiral | 29 % → 29 % | 19.3 px | 0.85 | 1.00 | 109 |
| loop | 15 % → 15 % | 19.3 px | 0.85 | 1.00 | 55 |
| tilted | 6 % → 6 % | 16.6 px | 0.85 | 1.00 | 34 |
| over the wet one | 13 % → 13 % | 19.8 px | 0.85 | 1.00 | 49 |
| long, no reload | 41 % → 41 % | 18.2 px | 0.85 | 1.00 | 158 | quarters: 0.38 → 0.38 → 0.38 → 0.38

Numbers say: light vs heavy: width 15.3 → 23.3 px, dark 0.85 → 0.85; the long stroke does not run out of paint.

## Brush Artist · Charcoal — stick B
Charcoal 0.78 · Pastel 0.22 · 36 px · 10.3 s

![Brush Artist · Charcoal — stick B](Brush-Artist-Charcoal-stick-B.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 7 % → 7 % | 19.8 px | 0.85 | 1.00 | 29 |
| heavy line | 10 % → 10 % | 30.4 px | 0.85 | 1.00 | 38 |
| pressure swell | 7 % → 7 % | 25.9 px | 0.85 | 1.00 | 27 |
| fast wave | 23 % → 23 % | 26.8 px | 0.85 | 1.00 | 93 |
| slow wave | 22 % → 22 % | 25.5 px | 0.85 | 1.00 | 145 |
| spiral | 38 % → 38 % | 25.4 px | 0.85 | 1.00 | 139 |
| loop | 19 % → 19 % | 25.0 px | 0.85 | 1.00 | 82 |
| tilted | 7 % → 7 % | 20.4 px | 0.85 | 1.00 | 47 |
| over the wet one | 17 % → 17 % | 25.9 px | 0.85 | 1.00 | 33 |
| long, no reload | 51 % → 51 % | 22.6 px | 0.85 | 1.00 | 296 | quarters: 0.47 → 0.47 → 0.47 → 0.47

Numbers say: light vs heavy: width 19.8 → 30.4 px, dark 0.85 → 0.85; the long stroke does not run out of paint.

## Brush Artist · Charcoal — stick C
Charcoal 0.78 · Pastel 0.22 · 22 px · 9.8 s

![Brush Artist · Charcoal — stick C](Brush-Artist-Charcoal-stick-C.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 4 % → 4 % | 12.6 px | 0.85 | 1.00 | 14 |
| heavy line | 7 % → 7 % | 19.0 px | 0.85 | 1.00 | 31 |
| pressure swell | 4 % → 4 % | 16.2 px | 0.85 | 1.00 | 17 |
| fast wave | 15 % → 15 % | 16.9 px | 0.85 | 1.00 | 47 |
| slow wave | 14 % → 14 % | 15.8 px | 0.85 | 1.00 | 64 |
| spiral | 24 % → 24 % | 15.7 px | 0.85 | 1.00 | 95 |
| loop | 12 % → 12 % | 15.9 px | 0.85 | 1.00 | 45 |
| tilted | 5 % → 5 % | 14.4 px | 0.85 | 1.00 | 25 |
| over the wet one | 11 % → 11 % | 16.1 px | 0.85 | 1.00 | 22 |
| long, no reload | 34 % → 34 % | 15.2 px | 0.85 | 1.00 | 140 | quarters: 0.32 → 0.32 → 0.32 → 0.32

Numbers say: light vs heavy: width 12.6 → 19.0 px, dark 0.85 → 0.85; the long stroke does not run out of paint.

## Brush Artist · Refs · #01 Henry Ward peach cloud — own sheet
own sheet 600 × 600 · Gouache 1.00 · 44 px · 14.7 s

![Brush Artist · Refs · #01 Henry Ward peach cloud — own sheet](Brush-Artist-Refs-01-Henry-Ward-peach-cloud-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 13 % → 33 % | 36.9 px | 0.57 | 2.58 | 146 |
| stroke 2 | 22 % → 52 % | 71.2 px | 0.57 | 2.40 | 141 |
| stroke 3 | 25 % → 49 % | 72.6 px | 0.57 | 1.98 | 145 |
| stroke 4 | 27 % → 53 % | 87.8 px | 0.57 | 1.99 | 161 |
| stroke 5 | 26 % → 48 % | 75.1 px | 0.57 | 1.84 | 149 |
| stroke 6 | 27 % → 36 % | 81.4 px | 0.57 | 1.36 | 128 |
| stroke 7 | 14 % → 51 % | 35.9 px | 0.58 | 3.56 | 187 |
| stroke 8 | 18 % → 48 % | 43.9 px | 0.58 | 2.75 | 178 |
| stroke 9 | 20 % → 49 % | 51.6 px | 0.58 | 2.44 | 157 |
| stroke 10 | 23 % → 50 % | 61.7 px | 0.58 | 2.16 | 158 |
| stroke 11 | 25 % → 52 % | 71.2 px | 0.58 | 2.08 | 244 |
| stroke 12 | 28 % → 55 % | 83.9 px | 0.58 | 1.97 | 198 |
| stroke 13 | 35 % → 58 % | 101.5 px | 0.58 | 1.65 | 187 |
| stroke 14 | 39 % → 60 % | 111.4 px | 0.58 | 1.54 | 177 |
| stroke 15 | 52 % → 65 % | 154.2 px | 0.58 | 1.25 | 168 |
| stroke 16 | 53 % → 66 % | 161.7 px | 0.58 | 1.23 | 147 |
| stroke 17 | 54 % → 67 % | 152.5 px | 0.58 | 1.24 | 226 |
| stroke 18 | 56 % → 66 % | 161.6 px | 0.58 | 1.19 | 157 |
| stroke 19 | 57 % → 65 % | 160.8 px | 0.58 | 1.13 | 135 |
| stroke 20 | 57 % → 61 % | 162.8 px | 0.58 | 1.09 | 144 |
| stroke 21 | 56 % → 58 % | 162.6 px | 0.58 | 1.04 | 164 |
| stroke 22 | 58 % → 59 % | 169.3 px | 0.58 | 1.02 | 163 |
| stroke 23 | 58 % → 56 % | 164.4 px | 0.58 | 0.98 | 140 |
| stroke 24 | 61 % → 59 % | 183.3 px | 0.58 | 0.96 | 133 |

Numbers say: wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #02 Henry Ward cream strokes — own sheet
own sheet 600 × 600 · Gouache 1.00 · 46 px · 8.4 s

![Brush Artist · Refs · #02 Henry Ward cream strokes — own sheet](Brush-Artist-Refs-02-Henry-Ward-cream-strokes-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 16 % → 22 % | 33.6 px | 0.67 | 1.35 | 217 |
| stroke 2 | 24 % → 25 % | 64.1 px | 0.67 | 1.04 | 207 |
| stroke 3 | 24 % → 31 % | 60.5 px | 0.67 | 1.30 | 198 |
| stroke 4 | 25 % → 28 % | 62.7 px | 0.67 | 1.09 | 234 |
| stroke 5 | 32 % → 35 % | 79.4 px | 0.67 | 1.07 | 249 |
| stroke 6 | 25 % → 29 % | 61.3 px | 0.67 | 1.15 | 199 |
| stroke 7 | 26 % → 19 % | 65.3 px | 0.67 | 0.75 | 275 |

## Brush Artist · Refs · #03 Henry Ward navy contours — own sheet
own sheet 600 × 600 · Impasto 1.00 · 22 px · 2.8 s

![Brush Artist · Refs · #03 Henry Ward navy contours — own sheet](Brush-Artist-Refs-03-Henry-Ward-navy-contours-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 11 % → 18 % | 23.1 px | 0.69 | 1.56 | 144 |
| stroke 2 | 20 % → 23 % | 28.3 px | 0.69 | 1.14 | 104 |
| stroke 3 | 23 % → 23 % | 33.4 px | 0.69 | 1.01 | 161 |
| stroke 4 | 23 % → 21 % | 50.8 px | 0.69 | 0.92 | 160 |

Numbers say: wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #04 Henry Ward grey cloud — own sheet
own sheet 600 × 600 · Gouache 1.00 · 50 px · 14.3 s

![Brush Artist · Refs · #04 Henry Ward grey cloud — own sheet](Brush-Artist-Refs-04-Henry-Ward-grey-cloud-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 14 % → 46 % | 39.8 px | 0.39 | 3.40 | 184 |
| stroke 2 | 18 % → 48 % | 51.1 px | 0.39 | 2.71 | 201 |
| stroke 3 | 25 % → 55 % | 70.3 px | 0.39 | 2.19 | 209 |
| stroke 4 | 30 % → 58 % | 87.7 px | 0.39 | 1.93 | 238 |
| stroke 5 | 36 % → 65 % | 109.9 px | 0.39 | 1.78 | 197 |
| stroke 6 | 38 % → 68 % | 124.6 px | 0.39 | 1.79 | 199 |
| stroke 7 | 44 % → 76 % | 130.0 px | 0.39 | 1.71 | 205 |
| stroke 8 | 45 % → 76 % | 133.8 px | 0.39 | 1.69 | 204 |
| stroke 9 | 44 % → 76 % | 131.3 px | 0.39 | 1.74 | 250 |
| stroke 10 | 46 % → 76 % | 147.6 px | 0.39 | 1.66 | 228 |
| stroke 11 | 44 % → 76 % | 125.8 px | 0.39 | 1.71 | 210 |
| stroke 12 | 47 % → 76 % | 141.7 px | 0.39 | 1.62 | 220 |
| stroke 13 | 46 % → 76 % | 132.6 px | 0.39 | 1.65 | 245 |
| stroke 14 | 46 % → 76 % | 136.3 px | 0.39 | 1.67 | 253 |
| stroke 15 | 45 % → 71 % | 129.5 px | 0.39 | 1.57 | 249 |
| stroke 16 | 47 % → 68 % | 143.5 px | 0.39 | 1.44 | 276 |
| stroke 17 | 46 % → 59 % | 131.6 px | 0.39 | 1.29 | 233 |
| stroke 18 | 44 % → 54 % | 146.8 px | 0.39 | 1.23 | 225 |
| stroke 19 | 44 % → 46 % | 132.5 px | 0.39 | 1.03 | 300 |
| stroke 20 | 47 % → 45 % | 146.8 px | 0.39 | 0.97 | 222 |

Numbers say: wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #05 Henry Ward green in rust loops — own sheet
own sheet 600 × 600 · Impasto 1.00 · 20 px · 2.4 s

![Brush Artist · Refs · #05 Henry Ward green in rust loops — own sheet](Brush-Artist-Refs-05-Henry-Ward-green-in-rust-loops-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 12 % → 19 % | 20.9 px | 0.02 | 1.60 | 119 |
| stroke 2 | 12 % → 11 % | 23.5 px | 0.02 | 0.93 | 152 |
| stroke 3 | 23 % → 21 % | 41.5 px | 0.02 | 0.93 | 127 |

Numbers say: wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #06 Henry Ward scrubbed grey — own sheet
own sheet 600 × 600 · Gouache 1.00 · 50 px · 15.7 s

![Brush Artist · Refs · #06 Henry Ward scrubbed grey — own sheet](Brush-Artist-Refs-06-Henry-Ward-scrubbed-grey-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 16 % → 51 % | 39.1 px | 0.39 | 3.19 | 232 |
| stroke 2 | 20 % → 53 % | 52.4 px | 0.39 | 2.70 | 190 |
| stroke 3 | 26 % → 57 % | 79.5 px | 0.39 | 2.20 | 190 |
| stroke 4 | 28 % → 58 % | 89.9 px | 0.39 | 2.02 | 243 |
| stroke 5 | 41 % → 72 % | 121.8 px | 0.39 | 1.78 | 251 |
| stroke 6 | 44 % → 73 % | 133.4 px | 0.39 | 1.66 | 236 |
| stroke 7 | 45 % → 75 % | 128.9 px | 0.39 | 1.67 | 249 |
| stroke 8 | 46 % → 76 % | 147.1 px | 0.39 | 1.63 | 280 |
| stroke 9 | 45 % → 75 % | 137.2 px | 0.39 | 1.69 | 225 |
| stroke 10 | 43 % → 75 % | 141.2 px | 0.39 | 1.73 | 220 |
| stroke 11 | 45 % → 76 % | 131.3 px | 0.39 | 1.69 | 307 |
| stroke 12 | 47 % → 76 % | 142.9 px | 0.39 | 1.62 | 231 |
| stroke 13 | 45 % → 75 % | 126.7 px | 0.39 | 1.69 | 193 |
| stroke 14 | 42 % → 75 % | 124.6 px | 0.39 | 1.77 | 217 |
| stroke 15 | 43 % → 76 % | 123.5 px | 0.39 | 1.76 | 209 |
| stroke 16 | 46 % → 75 % | 146.8 px | 0.39 | 1.63 | 232 |
| stroke 17 | 45 % → 67 % | 134.8 px | 0.39 | 1.48 | 232 |
| stroke 18 | 46 % → 64 % | 139.5 px | 0.39 | 1.39 | 229 |
| stroke 19 | 44 % → 59 % | 131.3 px | 0.39 | 1.34 | 212 |
| stroke 20 | 46 % → 57 % | 142.0 px | 0.39 | 1.24 | 206 |
| stroke 21 | 46 % → 48 % | 132.2 px | 0.39 | 1.04 | 232 |
| stroke 22 | 44 % → 43 % | 146.5 px | 0.39 | 0.96 | 185 |

Numbers say: wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #07 Henry Ward blue L + black zigzag — own sheet
own sheet 600 × 600 · Impasto 1.00 · 34 px · 2.1 s

![Brush Artist · Refs · #07 Henry Ward blue L + black zigzag — own sheet](Brush-Artist-Refs-07-Henry-Ward-blue-L-black-zigzag-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 15 % → 18 % | 35.6 px | 0.59 | 1.14 | 124 |
| stroke 2 | 17 % → 16 % | 42.9 px | 0.59 | 0.93 | 80 |

## Brush Artist · Refs · #08 Henry Ward olive bands — own sheet
own sheet 600 × 600 · Gouache 1.00 · 34 px · 5.8 s

![Brush Artist · Refs · #08 Henry Ward olive bands — own sheet](Brush-Artist-Refs-08-Henry-Ward-olive-bands-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 10 % → 8 % | 20.0 px | 0.58 | 0.79 | 150 |
| stroke 2 | 16 % → 10 % | 37.0 px | 0.58 | 0.58 | 153 |
| stroke 3 | 15 % → 14 % | 31.4 px | 0.58 | 0.93 | 197 |
| stroke 4 | 16 % → 11 % | 35.7 px | 0.58 | 0.68 | 203 |
| stroke 5 | 24 % → 14 % | 48.5 px | 0.58 | 0.61 | 183 |
| stroke 6 | 15 % → 8 % | 29.2 px | 0.58 | 0.52 | 206 |

## Brush Artist · Refs · #09 Henry Ward white loops — own sheet
own sheet 600 × 600 · Gouache 1.00 · 46 px · 8.4 s

![Brush Artist · Refs · #09 Henry Ward white loops — own sheet](Brush-Artist-Refs-09-Henry-Ward-white-loops-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 22 % → 4 % | 11.8 px | 0.06 | 0.16 | 1116 |
| stroke 2 | 25 % → 2 % | 24.7 px | 0.06 | 0.10 | 1278 |
| stroke 3 | 32 % → 2 % | 29.6 px | 0.06 | 0.07 | 986 |
| stroke 4 | 3 % → 1 % | 7.5 px | 0.05 | 0.33 | 151 |
| stroke 5 | 3 % → 1 % | 7.4 px | 0.06 | 0.40 | 171 |
| stroke 6 | 3 % → 2 % | 7.9 px | 0.06 | 0.84 | 143 |
| stroke 7 | 5 % → 2 % | 13.9 px | 0.06 | 0.46 | 164 |
| stroke 8 | 4 % → 1 % | 7.3 px | 0.05 | 0.35 | 198 |

## Brush Artist · Refs · #10 Henry Ward maroon loops — own sheet
own sheet 600 × 600 · Impasto 1.00 · 30 px · 3.6 s

![Brush Artist · Refs · #10 Henry Ward maroon loops — own sheet](Brush-Artist-Refs-10-Henry-Ward-maroon-loops-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 12 % → 28 % | 28.7 px | 0.72 | 2.39 | 267 |
| stroke 2 | 22 % → 40 % | 48.5 px | 0.72 | 1.87 | 157 |
| stroke 3 | 29 % → 37 % | 58.5 px | 0.72 | 1.27 | 185 |
| stroke 4 | 41 % → 39 % | 92.8 px | 0.72 | 0.96 | 128 |
| stroke 5 | 34 % → 32 % | 85.8 px | 0.72 | 0.93 | 164 |

Numbers say: wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #11 Henry Ward purple spun balls — own sheet
own sheet 600 × 600 · Impasto 1.00 · 36 px · 3.0 s

![Brush Artist · Refs · #11 Henry Ward purple spun balls — own sheet](Brush-Artist-Refs-11-Henry-Ward-purple-spun-balls-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 24 % → 35 % | 26.5 px | 0.68 | 1.43 | 242 |
| stroke 2 | 35 % → 46 % | 38.2 px | 0.68 | 1.33 | 265 |
| stroke 3 | 36 % → 34 % | 39.2 px | 0.68 | 0.97 | 354 |

## Brush Artist · Refs · #12 Henry Ward black-olive cage — own sheet
own sheet 600 × 600 · Gouache 1.00 · 28 px · 5.4 s

![Brush Artist · Refs · #12 Henry Ward black-olive cage — own sheet](Brush-Artist-Refs-12-Henry-Ward-black-olive-cage-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 8 % → 9 % | 14.8 px | 0.59 | 1.19 | 192 |
| stroke 2 | 8 % → 11 % | 18.8 px | 0.59 | 1.36 | 175 |
| stroke 3 | 17 % → 14 % | 26.6 px | 0.59 | 0.84 | 208 |
| stroke 4 | 17 % → 12 % | 34.7 px | 0.59 | 0.66 | 121 |
| stroke 5 | 16 % → 9 % | 30.1 px | 0.59 | 0.53 | 122 |
| stroke 6 | 26 % → 13 % | 50.0 px | 0.59 | 0.48 | 171 |

## Brush Artist · Refs · #13 Henry Ward blue streaky form — own sheet
own sheet 600 × 600 · Gouache 1.00 · 50 px · 11.8 s

![Brush Artist · Refs · #13 Henry Ward blue streaky form — own sheet](Brush-Artist-Refs-13-Henry-Ward-blue-streaky-form-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 13 % → 2 % | 39.9 px | 0.04 | 0.18 | 235 |
| stroke 2 | 18 % → 2 % | 54.5 px | 0.04 | 0.13 | 231 |
| stroke 3 | 28 % → 2 % | 81.0 px | 0.04 | 0.09 | 236 |
| stroke 4 | 30 % → 2 % | 96.2 px | 0.04 | 0.07 | 224 |
| stroke 5 | 43 % → 2 % | 125.2 px | 0.04 | 0.06 | 222 |
| stroke 6 | 44 % → 2 % | 124.7 px | 0.04 | 0.05 | 244 |
| stroke 7 | 45 % → 3 % | 132.1 px | 0.04 | 0.07 | 219 |
| stroke 8 | 47 % → 2 % | 143.3 px | 0.05 | 0.05 | 215 |
| stroke 9 | 46 % → 2 % | 141.7 px | 0.05 | 0.05 | 210 |
| stroke 10 | 45 % → 2 % | 148.8 px | 0.05 | 0.05 | 223 |
| stroke 11 | 42 % → 1 % | 130.3 px | 0.05 | 0.03 | 233 |
| stroke 12 | 45 % → 1 % | 134.7 px | 0.05 | 0.03 | 246 |
| stroke 13 | 44 % → 2 % | 137.5 px | 0.05 | 0.05 | 209 |
| stroke 14 | 42 % → 2 % | 125.0 px | 0.05 | 0.05 | 247 |
| stroke 15 | 42 % → 2 % | 121.4 px | 0.05 | 0.05 | 247 |
| stroke 16 | 46 % → 2 % | 137.1 px | 0.05 | 0.05 | 196 |
| stroke 17 | 54 % → 1 % | 135.6 px | 0.04 | 0.03 | 207 |
| stroke 18 | 58 % → 1 % | 139.8 px | 0.04 | 0.02 | 249 |
| stroke 19 | 62 % → 2 % | 125.9 px | 0.04 | 0.03 | 241 |
| stroke 20 | 73 % → 2 % | 138.7 px | 0.04 | 0.02 | 244 |
| stroke 21 | 4 % → 1 % | 7.9 px | 0.04 | 0.34 | 135 |
| stroke 22 | 3 % → 2 % | 7.9 px | 0.04 | 0.82 | 146 |
| stroke 23 | 5 % → 2 % | 14.6 px | 0.04 | 0.49 | 130 |
| stroke 24 | 4 % → 1 % | 9.8 px | 0.05 | 0.42 | 149 |
| stroke 25 | 5 % → 2 % | 11.7 px | 0.05 | 0.50 | 161 |

## Brush Artist · Refs · #14 Henry Ward olive totem — own sheet
own sheet 600 × 600 · Impasto 1.00 · 48 px · 7.2 s

![Brush Artist · Refs · #14 Henry Ward olive totem — own sheet](Brush-Artist-Refs-14-Henry-Ward-olive-totem-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 18 % → 46 % | 46.9 px | 0.38 | 2.58 | 152 |
| stroke 2 | 21 % → 50 % | 64.4 px | 0.38 | 2.45 | 154 |
| stroke 3 | 29 % → 52 % | 100.7 px | 0.38 | 1.78 | 136 |
| stroke 4 | 30 % → 55 % | 113.8 px | 0.38 | 1.80 | 148 |
| stroke 5 | 39 % → 64 % | 135.7 px | 0.38 | 1.63 | 126 |
| stroke 6 | 39 % → 65 % | 150.5 px | 0.38 | 1.68 | 125 |
| stroke 7 | 37 % → 61 % | 124.4 px | 0.38 | 1.66 | 132 |
| stroke 8 | 37 % → 63 % | 142.5 px | 0.38 | 1.69 | 141 |
| stroke 9 | 38 % → 63 % | 131.0 px | 0.38 | 1.67 | 153 |
| stroke 10 | 38 % → 62 % | 141.2 px | 0.38 | 1.62 | 145 |
| stroke 11 | 40 % → 65 % | 143.9 px | 0.38 | 1.61 | 132 |
| stroke 12 | 38 % → 65 % | 144.3 px | 0.38 | 1.70 | 144 |
| stroke 13 | 39 % → 67 % | 135.6 px | 0.38 | 1.73 | 117 |
| stroke 14 | 37 % → 62 % | 134.7 px | 0.38 | 1.69 | 153 |
| stroke 15 | 40 % → 66 % | 137.0 px | 0.38 | 1.65 | 138 |
| stroke 16 | 38 % → 64 % | 138.9 px | 0.38 | 1.66 | 164 |
| stroke 17 | 38 % → 62 % | 126.3 px | 0.38 | 1.65 | 153 |
| stroke 18 | 40 % → 66 % | 155.0 px | 0.38 | 1.64 | 153 |
| stroke 19 | 40 % → 60 % | 138.1 px | 0.38 | 1.52 | 153 |
| stroke 20 | 41 % → 55 % | 144.5 px | 0.38 | 1.34 | 153 |
| stroke 21 | 46 % → 55 % | 137.8 px | 0.38 | 1.18 | 150 |
| stroke 22 | 54 % → 53 % | 146.8 px | 0.38 | 0.99 | 142 |

Numbers say: wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #15 Ultramarine brush script — own sheet
own sheet 600 × 600 · Ink 1.00 · 4 px · 9.1 s

![Brush Artist · Refs · #15 Ultramarine brush script — own sheet](Brush-Artist-Refs-15-Ultramarine-brush-script-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 40 % → 42 % | 8.9 px | 0.66 | 1.05 | 52 |
| stroke 2 | 40 % → 42 % | 8.9 px | 0.66 | 1.06 | 42 |
| stroke 3 | 40 % → 42 % | 9.5 px | 0.74 | 1.06 | 36 |
| stroke 4 | 42 % → 45 % | 10.1 px | 0.74 | 1.09 | 21 |
| stroke 5 | 44 % → 48 % | 9.7 px | 0.73 | 1.09 | 37 |
| stroke 6 | 42 % → 44 % | 9.5 px | 0.65 | 1.05 | 53 |
| stroke 7 | 43 % → 47 % | 9.2 px | 0.72 | 1.08 | 42 |
| stroke 8 | 38 % → 41 % | 9.3 px | 0.68 | 1.05 | 46 |
| stroke 9 | 40 % → 42 % | 9.2 px | 0.69 | 1.06 | 47 |
| stroke 10 | 36 % → 38 % | 9.9 px | 0.68 | 1.05 | 59 |
| stroke 11 | 42 % → 45 % | 9.6 px | 0.70 | 1.06 | 40 |
| stroke 12 | 39 % → 41 % | 9.4 px | 0.66 | 1.06 | 71 |
| stroke 13 | 45 % → 48 % | 10.2 px | 0.71 | 1.06 | 38 |
| stroke 14 | 38 % → 41 % | 9.8 px | 0.72 | 1.07 | 20 |
| stroke 15 | 37 % → 39 % | 9.1 px | 0.69 | 1.06 | 47 |
| stroke 16 | 42 % → 45 % | 9.4 px | 0.72 | 1.06 | 36 |
| stroke 17 | 41 % → 44 % | 7.1 px | 0.71 | 1.08 | 52 |
| stroke 18 | 43 % → 45 % | 9.2 px | 0.73 | 1.06 | 27 |
| stroke 19 | 39 % → 41 % | 8.9 px | 0.66 | 1.05 | 69 |
| stroke 20 | 41 % → 43 % | 9.4 px | 0.71 | 1.06 | 45 |
| stroke 21 | 41 % → 43 % | 9.9 px | 0.70 | 1.06 | 41 |
| stroke 22 | 42 % → 45 % | 8.5 px | 0.65 | 1.06 | 77 |
| stroke 23 | 40 % → 43 % | 10.1 px | 0.73 | 1.08 | 33 |
| stroke 24 | 38 % → 41 % | 8.8 px | 0.73 | 1.07 | 36 |
| stroke 25 | 41 % → 43 % | 9.8 px | 0.72 | 1.07 | 44 |
| stroke 26 | 46 % → 49 % | 9.3 px | 0.68 | 1.05 | 53 |
| stroke 27 | 43 % → 45 % | 8.8 px | 0.63 | 1.05 | 72 |
| stroke 28 | 44 % → 46 % | 9.1 px | 0.70 | 1.06 | 44 |
| stroke 29 | 36 % → 39 % | 10.6 px | 0.72 | 1.08 | 21 |
| stroke 30 | 39 % → 41 % | 8.7 px | 0.71 | 1.04 | 46 |
| stroke 31 | 43 % → 46 % | 10.3 px | 0.75 | 1.08 | 21 |
| stroke 32 | 42 % → 46 % | 9.5 px | 0.73 | 1.09 | 25 |
| stroke 33 | 35 % → 38 % | 10.9 px | 0.72 | 1.08 | 27 |
| stroke 34 | 40 % → 43 % | 9.8 px | 0.73 | 1.08 | 24 |
| stroke 35 | 36 % → 37 % | 9.4 px | 0.65 | 1.05 | 49 |

## Brush Artist · Refs · #18 Blue oil-stick scribbles — own sheet
own sheet 600 × 600 · Pastel 1.00 · 10 px · 3.5 s

![Brush Artist · Refs · #18 Blue oil-stick scribbles — own sheet](Brush-Artist-Refs-18-Blue-oil-stick-scribbles-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 15 % → 31 % | 3.8 px | 0.49 | 2.11 | 184 |
| stroke 2 | 13 % → 37 % | 3.6 px | 0.49 | 2.73 | 214 |
| stroke 3 | 16 % → 26 % | 5.8 px | 0.49 | 1.66 | 195 |
| stroke 4 | 15 % → 29 % | 8.0 px | 0.49 | 1.88 | 256 |
| stroke 5 | 29 % → 34 % | 8.4 px | 0.49 | 1.19 | 177 |
| stroke 6 | 25 % → 26 % | 9.4 px | 0.49 | 1.02 | 168 |
| stroke 7 | 26 % → 32 % | 8.3 px | 0.49 | 1.24 | 179 |
| stroke 8 | 30 % → 30 % | 17.0 px | 0.49 | 1.00 | 229 |

Numbers say: wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #20 Orange-red crayon scribble — own sheet
own sheet 600 × 600 · Pastel 1.00 · 14 px · 3.2 s

![Brush Artist · Refs · #20 Orange-red crayon scribble — own sheet](Brush-Artist-Refs-20-Orange-red-crayon-scribble-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 8 % → 18 % | 5.5 px | 0.59 | 2.46 | 237 |
| stroke 2 | 9 % → 23 % | 6.8 px | 0.59 | 2.48 | 232 |
| stroke 3 | 13 % → 21 % | 8.5 px | 0.59 | 1.64 | 182 |
| stroke 4 | 24 % → 32 % | 8.9 px | 0.59 | 1.34 | 209 |
| stroke 5 | 27 % → 27 % | 7.7 px | 0.59 | 1.00 | 202 |
| stroke 6 | 22 % → 22 % | 16.8 px | 0.59 | 1.00 | 201 |

Numbers say: wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #21 Gritty black contours — own sheet
own sheet 600 × 600 · Gouache 1.00 · 12 px · 4.2 s

![Brush Artist · Refs · #21 Gritty black contours — own sheet](Brush-Artist-Refs-21-Gritty-black-contours-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 4 % → 3 % | 4.9 px | 0.37 | 0.70 | 166 |
| stroke 2 | 5 % → 2 % | 7.6 px | 0.37 | 0.43 | 183 |
| stroke 3 | 7 % → 2 % | 5.9 px | 0.37 | 0.26 | 102 |
| stroke 4 | 8 % → 3 % | 9.8 px | 0.37 | 0.40 | 130 |
| stroke 5 | 10 % → 3 % | 11.9 px | 0.37 | 0.34 | 91 |

## Brush Artist · Refs · #22 Bold black brush poster — own sheet
own sheet 600 × 600 · Ink 1.00 · 20 px · 5.3 s

![Brush Artist · Refs · #22 Bold black brush poster — own sheet](Brush-Artist-Refs-22-Bold-black-brush-poster-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 22 % → 27 % | 36.3 px | 0.94 | 1.20 | 117 |
| stroke 2 | 27 % → 37 % | 41.4 px | 0.94 | 1.37 | 26 |
| stroke 3 | 28 % → 29 % | 43.6 px | 0.94 | 1.00 | 52 |
| stroke 4 | 27 % → 39 % | 53.7 px | 0.94 | 1.43 | 58 |
| stroke 5 | 25 % → 25 % | 42.9 px | 0.94 | 1.00 | 83 |

## Brush Artist · Refs · #23 Dry white on orange + black line — own sheet
own sheet 600 × 600 · Gouache 1.00 · 50 px · 8.1 s

![Brush Artist · Refs · #23 Dry white on orange + black line — own sheet](Brush-Artist-Refs-23-Dry-white-on-orange-black-line-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 6 % → 11 % | 22.3 px | 0.40 | 1.71 | 157 |
| stroke 2 | 9 % → 10 % | 31.8 px | 0.40 | 1.10 | 151 |
| stroke 3 | 13 % → 11 % | 48.0 px | 0.40 | 0.82 | 142 |
| stroke 4 | 15 % → 12 % | 59.0 px | 0.40 | 0.80 | 153 |
| stroke 5 | 21 % → 14 % | 75.7 px | 0.40 | 0.67 | 132 |
| stroke 6 | 21 % → 16 % | 88.3 px | 0.40 | 0.77 | 150 |
| stroke 7 | 17 % → 15 % | 65.6 px | 0.39 | 0.87 | 141 |
| stroke 8 | 18 % → 14 % | 70.7 px | 0.39 | 0.79 | 151 |
| stroke 9 | 18 % → 15 % | 68.7 px | 0.39 | 0.83 | 155 |
| stroke 10 | 18 % → 15 % | 69.0 px | 0.39 | 0.87 | 184 |
| stroke 11 | 20 % → 17 % | 74.8 px | 0.39 | 0.85 | 140 |
| stroke 12 | 21 % → 17 % | 80.3 px | 0.39 | 0.81 | 121 |
| stroke 13 | 21 % → 19 % | 77.7 px | 0.39 | 0.89 | 125 |
| stroke 14 | 20 % → 19 % | 81.1 px | 0.39 | 0.91 | 171 |
| stroke 15 | 20 % → 16 % | 73.7 px | 0.39 | 0.80 | 139 |
| stroke 16 | 20 % → 14 % | 80.1 px | 0.39 | 0.70 | 147 |
| stroke 17 | 20 % → 13 % | 71.5 px | 0.39 | 0.61 | 145 |
| stroke 18 | 24 % → 13 % | 86.5 px | 0.39 | 0.55 | 138 |

Numbers say: wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #24 Picasso flat oil — own sheet
own sheet 600 × 600 · Oil 0.89 · Oil glaze 0.11 · 34 px · 5.4 s

![Brush Artist · Refs · #24 Picasso flat oil — own sheet](Brush-Artist-Refs-24-Picasso-flat-oil-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 16 % → 45 % | 34.7 px | 0.23 | 2.74 | 136 |
| stroke 2 | 20 % → 49 % | 47.2 px | 0.23 | 2.40 | 134 |
| stroke 3 | 29 % → 59 % | 62.6 px | 0.23 | 2.07 | 161 |
| stroke 4 | 37 % → 65 % | 83.2 px | 0.23 | 1.76 | 154 |
| stroke 5 | 43 % → 71 % | 94.5 px | 0.23 | 1.65 | 126 |
| stroke 6 | 44 % → 66 % | 102.2 px | 0.23 | 1.50 | 161 |
| stroke 7 | 45 % → 66 % | 94.9 px | 0.23 | 1.46 | 140 |
| stroke 8 | 44 % → 66 % | 107.0 px | 0.23 | 1.50 | 145 |
| stroke 9 | 37 % → 62 % | 81.5 px | 0.23 | 1.68 | 144 |
| stroke 10 | 39 % → 62 % | 93.1 px | 0.23 | 1.58 | 142 |
| stroke 11 | 37 % → 60 % | 78.6 px | 0.23 | 1.62 | 160 |
| stroke 12 | 38 % → 61 % | 91.1 px | 0.23 | 1.60 | 147 |
| stroke 13 | 38 % → 68 % | 84.4 px | 0.23 | 1.76 | 129 |
| stroke 14 | 39 % → 69 % | 88.9 px | 0.23 | 1.75 | 139 |
| stroke 15 | 39 % → 62 % | 83.3 px | 0.23 | 1.58 | 136 |
| stroke 16 | 38 % → 55 % | 88.0 px | 0.23 | 1.43 | 170 |
| stroke 17 | 43 % → 48 % | 90.0 px | 0.23 | 1.12 | 129 |
| stroke 18 | 42 % → 42 % | 102.7 px | 0.23 | 1.00 | 156 |

Numbers say: wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #25 Yellow heavy flat stroke — own sheet
own sheet 600 × 600 · Impasto 1.00 · 110 px · 3.1 s

![Brush Artist · Refs · #25 Yellow heavy flat stroke — own sheet](Brush-Artist-Refs-25-Yellow-heavy-flat-stroke-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 18 % → 18 % | 104.3 px | 0.17 | 0.98 | 735 |

## Brush Artist · Refs · #27 Orange impasto swatch — own sheet
own sheet 600 × 600 · Impasto 1.00 · 60 px · 3.2 s

![Brush Artist · Refs · #27 Orange impasto swatch — own sheet](Brush-Artist-Refs-27-Orange-impasto-swatch-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 8 % → 21 % | 61.8 px | 0.33 | 2.60 | 74 |
| stroke 2 | 7 % → 33 % | 62.6 px | 0.33 | 4.67 | 60 |
| stroke 3 | 25 % → 36 % | 245.8 px | 0.33 | 1.40 | 37 |
| stroke 4 | 10 % → 12 % | 69.8 px | 0.33 | 1.25 | 69 |
| stroke 5 | 17 % → 33 % | 63.5 px | 0.33 | 1.90 | 76 |
| stroke 6 | 18 % → 32 % | 145.3 px | 0.33 | 1.79 | 67 |
| stroke 7 | 8 % → 15 % | 70.4 px | 0.33 | 1.87 | 57 |
| stroke 8 | 33 % → 34 % | 337.7 px | 0.33 | 1.04 | 47 |
| stroke 9 | 38 % → 37 % | 185.5 px | 0.33 | 0.98 | 73 |
| stroke 10 | 34 % → 33 % | 305.4 px | 0.33 | 0.98 | 46 |

Numbers say: wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #28 Miles Davis black lines — own sheet
own sheet 600 × 600 · Ink 1.00 · 22 px · 6.4 s

![Brush Artist · Refs · #28 Miles Davis black lines — own sheet](Brush-Artist-Refs-28-Miles-Davis-black-lines-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 22 % → 32 % | 36.5 px | 0.88 | 1.42 | 194 |
| stroke 2 | 28 % → 49 % | 38.2 px | 0.88 | 1.73 | 140 |
| stroke 3 | 39 % → 44 % | 75.1 px | 0.88 | 1.12 | 113 |
| stroke 4 | 42 % → 48 % | 83.7 px | 0.88 | 1.15 | 167 |
| stroke 5 | 55 % → 55 % | 109.8 px | 0.88 | 1.00 | 140 |

Numbers say: wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #29 Shrigley magenta asterisk — own sheet
own sheet 600 × 600 · Watercolour 1.00 · 70 px · 6.3 s

![Brush Artist · Refs · #29 Shrigley magenta asterisk — own sheet](Brush-Artist-Refs-29-Shrigley-magenta-asterisk-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 13 % → 37 % | 46.6 px | 0.67 | 2.86 | 221 |
| stroke 2 | 12 % → 12 % | 87.1 px | 0.67 | 1.00 | 181 |
| stroke 3 | 28 % → 37 % | 100.9 px | 0.67 | 1.31 | 188 |
| stroke 4 | 23 % → 23 % | 164.0 px | 0.67 | 1.02 | 198 |

Numbers say: wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #30 Red gouache face patch — own sheet
own sheet 600 × 600 · Gouache 1.00 · 60 px · 12.1 s

![Brush Artist · Refs · #30 Red gouache face patch — own sheet](Brush-Artist-Refs-30-Red-gouache-face-patch-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 12 % → 37 % | 51.5 px | 0.54 | 3.23 | 157 |
| stroke 2 | 15 % → 40 % | 74.5 px | 0.54 | 2.72 | 173 |
| stroke 3 | 24 % → 50 % | 115.9 px | 0.54 | 2.06 | 155 |
| stroke 4 | 27 % → 52 % | 134.1 px | 0.54 | 1.94 | 156 |
| stroke 5 | 34 % → 60 % | 159.9 px | 0.54 | 1.77 | 219 |
| stroke 6 | 35 % → 61 % | 178.3 px | 0.54 | 1.76 | 171 |
| stroke 7 | 34 % → 59 % | 160.9 px | 0.54 | 1.73 | 163 |
| stroke 8 | 34 % → 56 % | 162.5 px | 0.54 | 1.66 | 171 |
| stroke 9 | 36 % → 60 % | 173.1 px | 0.54 | 1.66 | 189 |
| stroke 10 | 38 % → 62 % | 196.8 px | 0.54 | 1.64 | 173 |
| stroke 11 | 37 % → 61 % | 182.4 px | 0.54 | 1.66 | 182 |
| stroke 12 | 36 % → 58 % | 178.3 px | 0.54 | 1.62 | 196 |
| stroke 13 | 33 % → 46 % | 156.5 px | 0.54 | 1.39 | 190 |
| stroke 14 | 33 % → 41 % | 157.6 px | 0.54 | 1.25 | 212 |
| stroke 15 | 33 % → 37 % | 153.4 px | 0.54 | 1.12 | 211 |
| stroke 16 | 39 % → 39 % | 184.9 px | 0.54 | 0.99 | 183 |

Numbers say: wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #31 Warhol blotted line — own sheet
own sheet 600 × 600 · Ink 1.00 · 6 px · 5.2 s

![Brush Artist · Refs · #31 Warhol blotted line — own sheet](Brush-Artist-Refs-31-Warhol-blotted-line-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 21 % → 42 % | 15.8 px | 0.82 | 1.98 | 96 |
| stroke 2 | 17 % → 23 % | 15.9 px | 0.82 | 1.34 | 74 |
| stroke 3 | 24 % → 25 % | 25.1 px | 0.81 | 1.02 | 79 |
| stroke 4 | 31 % → 40 % | 31.8 px | 0.82 | 1.28 | 55 |
| stroke 5 | 35 % → 44 % | 36.4 px | 0.82 | 1.23 | 72 |
| stroke 6 | 32 % → 33 % | 26.7 px | 0.81 | 1.03 | 81 |

Numbers say: wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #32 Thick orange swipes — own sheet
own sheet 600 × 600 · Impasto 1.00 · 90 px · 3.6 s

![Brush Artist · Refs · #32 Thick orange swipes — own sheet](Brush-Artist-Refs-32-Thick-orange-swipes-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 14 % → 27 % | 86.1 px | 0.03 | 1.90 | 348 |
| stroke 2 | 26 % → 38 % | 177.0 px | 0.03 | 1.43 | 312 |
| stroke 3 | 28 % → 27 % | 177.6 px | 0.03 | 0.98 | 298 |

Numbers say: wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #33 Red wet-in-wet band — own sheet
own sheet 600 × 600 · Watercolour 1.00 · 80 px · 9.3 s

![Brush Artist · Refs · #33 Red wet-in-wet band — own sheet](Brush-Artist-Refs-33-Red-wet-in-wet-band-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 24 % → 58 % | 89.6 px | 0.62 | 2.46 | 410 |
| stroke 2 | 30 % → 52 % | 245.5 px | 0.63 | 1.72 | 119 |
| stroke 3 | 37 % → 54 % | 358.6 px | 0.62 | 1.46 | 111 |
| stroke 4 | 43 % → 61 % | 414.5 px | 0.63 | 1.42 | 106 |
| stroke 5 | 42 % → 56 % | 356.1 px | 0.63 | 1.32 | 150 |
| stroke 6 | 43 % → 48 % | 327.4 px | 0.61 | 1.12 | 138 |

Numbers say: wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #34 Magenta oil patches — own sheet
own sheet 600 × 600 · Oil 0.89 · Oil glaze 0.11 · 60 px · 4.6 s

![Brush Artist · Refs · #34 Magenta oil patches — own sheet](Brush-Artist-Refs-34-Magenta-oil-patches-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 9 % → 42 % | 62.0 px | 0.13 | 4.82 | 76 |
| stroke 2 | 9 % → 29 % | 62.8 px | 0.13 | 3.15 | 69 |
| stroke 3 | 7 % → 35 % | 62.4 px | 0.13 | 4.71 | 94 |
| stroke 4 | 16 % → 20 % | 132.1 px | 0.12 | 1.27 | 70 |
| stroke 5 | 23 % → 33 % | 124.6 px | 0.13 | 1.43 | 109 |
| stroke 6 | 20 % → 38 % | 171.6 px | 0.13 | 1.90 | 53 |
| stroke 7 | 30 % → 35 % | 238.0 px | 0.13 | 1.18 | 64 |
| stroke 8 | 33 % → 39 % | 235.2 px | 0.13 | 1.18 | 93 |
| stroke 9 | 25 % → 26 % | 159.9 px | 0.13 | 1.07 | 107 |
| stroke 10 | 29 % → 29 % | 257.6 px | 0.13 | 1.00 | 58 |
| stroke 11 | 36 % → 36 % | 324.9 px | 0.13 | 1.00 | 69 |
| stroke 12 | 26 % → 26 % | 184.7 px | 0.13 | 1.00 | 65 |

Numbers say: wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #35 Red band with runs — own sheet
own sheet 600 × 600 · Watercolour 1.00 · 70 px · 6.5 s

![Brush Artist · Refs · #35 Red band with runs — own sheet](Brush-Artist-Refs-35-Red-band-with-runs-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 37 % → 41 % | 138.9 px | 0.50 | 1.12 | 361 |

## Brush Artist · Refs · #36 Magenta letters flat brush — own sheet
own sheet 600 × 600 · Gouache 1.00 · 36 px · 11.4 s

![Brush Artist · Refs · #36 Magenta letters flat brush — own sheet](Brush-Artist-Refs-36-Magenta-letters-flat-brush-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 20 % → 39 % | 59.0 px | 0.50 | 1.95 | 33 |
| stroke 2 | 20 % → 32 % | 46.6 px | 0.50 | 1.59 | 36 |
| stroke 3 | 29 % → 54 % | 86.8 px | 0.50 | 1.86 | 35 |
| stroke 4 | 26 % → 44 % | 51.2 px | 0.50 | 1.67 | 123 |
| stroke 5 | 33 % → 55 % | 96.1 px | 0.50 | 1.67 | 79 |
| stroke 6 | 42 % → 56 % | 242.4 px | 0.50 | 1.33 | 16 |
| stroke 7 | 30 % → 44 % | 56.7 px | 0.50 | 1.45 | 127 |
| stroke 8 | 31 % → 53 % | 98.5 px | 0.50 | 1.68 | 66 |
| stroke 9 | 38 % → 51 % | 158.3 px | 0.50 | 1.33 | 32 |
| stroke 10 | 37 % → 63 % | 106.7 px | 0.50 | 1.72 | 91 |
| stroke 11 | 39 % → 62 % | 225.9 px | 0.50 | 1.58 | 17 |
| stroke 12 | 43 % → 56 % | 81.9 px | 0.50 | 1.29 | 126 |
| stroke 13 | 32 % → 46 % | 117.6 px | 0.50 | 1.43 | 36 |
| stroke 14 | 35 % → 52 % | 134.4 px | 0.50 | 1.47 | 40 |
| stroke 15 | 38 % → 56 % | 108.5 px | 0.50 | 1.49 | 90 |
| stroke 16 | 41 % → 50 % | 232.0 px | 0.50 | 1.23 | 18 |
| stroke 17 | 44 % → 52 % | 81.7 px | 0.50 | 1.19 | 137 |
| stroke 18 | 27 % → 36 % | 97.5 px | 0.50 | 1.35 | 36 |
| stroke 19 | 40 % → 39 % | 117.0 px | 0.50 | 0.96 | 35 |
| stroke 20 | 45 % → 45 % | 132.2 px | 0.50 | 0.99 | 33 |
| stroke 21 | 41 % → 39 % | 78.6 px | 0.50 | 0.96 | 74 |

Numbers say: wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #37 Oil still life dabs — own sheet
own sheet 600 × 600 · Oil 0.89 · Oil glaze 0.11 · 40 px · 4.0 s

![Brush Artist · Refs · #37 Oil still life dabs — own sheet](Brush-Artist-Refs-37-Oil-still-life-dabs-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 7 % → 7 % | 44.2 px | 0.39 | 1.00 | 27 |
| stroke 2 | 6 % → 28 % | 44.5 px | 0.39 | 4.43 | 21 |
| stroke 3 | 12 % → 36 % | 92.9 px | 0.39 | 3.00 | 19 |
| stroke 4 | 9 % → 9 % | 42.8 px | 0.39 | 1.00 | 49 |
| stroke 5 | 6 % → 10 % | 43.2 px | 0.39 | 1.72 | 40 |
| stroke 6 | 13 % → 31 % | 83.6 px | 0.39 | 2.32 | 34 |
| stroke 7 | 11 % → 24 % | 115.9 px | 0.39 | 2.18 | 15 |
| stroke 8 | 8 % → 14 % | 90.0 px | 0.39 | 1.63 | 15 |
| stroke 9 | 13 % → 14 % | 68.1 px | 0.38 | 1.09 | 43 |
| stroke 10 | 21 % → 25 % | 106.6 px | 0.39 | 1.20 | 48 |
| stroke 11 | 24 % → 28 % | 201.8 px | 0.39 | 1.17 | 28 |
| stroke 12 | 21 % → 21 % | 228.5 px | 0.39 | 1.01 | 12 |
| stroke 13 | 16 % → 16 % | 168.0 px | 0.40 | 1.00 | 18 |
| stroke 14 | 17 % → 17 % | 133.3 px | 0.39 | 1.00 | 21 |

Numbers say: wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #38 Sanguine drawing — own sheet
own sheet 600 × 600 · Pastel 1.00 · 6 px · 2.5 s

![Brush Artist · Refs · #38 Sanguine drawing — own sheet](Brush-Artist-Refs-38-Sanguine-drawing-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 3 % → 14 % | 2.9 px | 0.57 | 5.30 | 5 |
| stroke 2 | 3 % → 7 % | 2.9 px | 0.58 | 2.89 | 15 |
| stroke 3 | 3 % → 9 % | 2.9 px | 0.57 | 3.40 | 23 |
| stroke 4 | 2 % → 17 % | 2.7 px | 0.57 | 7.20 | 8 |
| stroke 5 | 2 % → 7 % | 2.7 px | 0.57 | 3.03 | 7 |
| stroke 6 | 3 % → 19 % | 3.4 px | 0.57 | 6.31 | 23 |
| stroke 7 | 5 % → 14 % | 5.2 px | 0.57 | 3.07 | 6 |
| stroke 8 | 4 % → 16 % | 4.7 px | 0.57 | 3.79 | 6 |
| stroke 9 | 3 % → 7 % | 2.9 px | 0.57 | 2.66 | 9 |
| stroke 10 | 4 % → 16 % | 4.7 px | 0.57 | 3.83 | 4 |
| stroke 11 | 3 % → 4 % | 2.9 px | 0.57 | 1.61 | 5 |
| stroke 12 | 4 % → 15 % | 4.8 px | 0.57 | 3.58 | 3 |
| stroke 13 | 8 % → 17 % | 8.9 px | 0.57 | 2.23 | 3 |
| stroke 14 | 4 % → 14 % | 4.9 px | 0.57 | 3.19 | 3 |
| stroke 15 | 9 % → 18 % | 10.7 px | 0.57 | 1.86 | 5 |
| stroke 16 | 6 % → 16 % | 6.6 px | 0.57 | 2.71 | 11 |
| stroke 17 | 4 % → 9 % | 4.4 px | 0.57 | 2.25 | 6 |
| stroke 18 | 3 % → 5 % | 2.9 px | 0.57 | 1.85 | 7 |
| stroke 19 | 6 % → 16 % | 6.9 px | 0.57 | 2.68 | 5 |
| stroke 20 | 8 % → 14 % | 9.2 px | 0.57 | 1.70 | 5 |
| stroke 21 | 4 % → 4 % | 4.3 px | 0.57 | 1.00 | 6 |
| stroke 22 | 8 % → 13 % | 8.6 px | 0.57 | 1.79 | 8 |
| stroke 23 | 7 % → 12 % | 8.3 px | 0.57 | 1.61 | 7 |
| stroke 24 | 4 % → 7 % | 4.7 px | 0.57 | 1.71 | 7 |
| stroke 25 | 8 % → 14 % | 8.7 px | 0.57 | 1.84 | 6 |
| stroke 26 | 6 % → 8 % | 6.5 px | 0.57 | 1.34 | 7 |
| stroke 27 | 4 % → 4 % | 4.3 px | 0.57 | 1.10 | 5 |
| stroke 28 | 7 % → 11 % | 8.2 px | 0.57 | 1.59 | 5 |
| stroke 29 | 8 % → 17 % | 8.8 px | 0.57 | 2.21 | 4 |
| stroke 30 | 13 % → 17 % | 14.9 px | 0.57 | 1.29 | 6 |
| stroke 31 | 5 % → 6 % | 5.4 px | 0.57 | 1.29 | 5 |
| stroke 32 | 10 % → 13 % | 11.8 px | 0.57 | 1.24 | 5 |
| stroke 33 | 7 % → 8 % | 8.5 px | 0.57 | 1.07 | 5 |
| stroke 34 | 11 % → 14 % | 12.0 px | 0.57 | 1.36 | 8 |
| stroke 35 | 9 % → 14 % | 10.0 px | 0.57 | 1.61 | 6 |
| stroke 36 | 10 % → 13 % | 11.4 px | 0.57 | 1.26 | 5 |
| stroke 37 | 9 % → 16 % | 10.5 px | 0.57 | 1.71 | 9 |
| stroke 38 | 13 % → 19 % | 14.8 px | 0.57 | 1.48 | 8 |
| stroke 39 | 14 % → 17 % | 15.7 px | 0.57 | 1.21 | 4 |
| stroke 40 | 6 % → 7 % | 7.2 px | 0.57 | 1.14 | 3 |
| stroke 41 | 16 % → 16 % | 17.7 px | 0.57 | 1.01 | 7 |
| stroke 42 | 14 % → 16 % | 15.2 px | 0.57 | 1.17 | 6 |
| stroke 43 | 10 % → 12 % | 11.6 px | 0.57 | 1.17 | 7 |
| stroke 44 | 12 % → 15 % | 14.3 px | 0.57 | 1.22 | 7 |
| stroke 45 | 2 % → 2 % | 2.7 px | 0.57 | 1.00 | 4 |
| stroke 46 | 16 % → 16 % | 18.5 px | 0.57 | 1.00 | 8 |
| stroke 47 | 13 % → 13 % | 15.0 px | 0.57 | 1.00 | 7 |
| stroke 48 | 12 % → 13 % | 14.3 px | 0.57 | 1.07 | 4 |
| stroke 49 | 19 % → 19 % | 21.5 px | 0.57 | 1.00 | 4 |
| stroke 50 | 10 % → 10 % | 11.6 px | 0.57 | 1.00 | 6 |

Numbers say: wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #39 Very thick impasto — own sheet
own sheet 600 × 600 · Impasto 1.00 · 60 px · 4.9 s

![Brush Artist · Refs · #39 Very thick impasto — own sheet](Brush-Artist-Refs-39-Very-thick-impasto-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 26 % → 37 % | 59.6 px | 0.43 | 1.42 | 295 |
| stroke 2 | 31 % → 48 % | 93.9 px | 0.44 | 1.54 | 342 |
| stroke 3 | 37 % → 49 % | 124.6 px | 0.43 | 1.33 | 296 |
| stroke 4 | 31 % → 44 % | 90.9 px | 0.44 | 1.41 | 342 |
| stroke 5 | 42 % → 41 % | 104.2 px | 0.44 | 0.98 | 318 |

Numbers say: wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #40 Watercolour blooms — own sheet
own sheet 600 × 600 · Watercolour 1.00 · 90 px · 7.2 s

![Brush Artist · Refs · #40 Watercolour blooms — own sheet](Brush-Artist-Refs-40-Watercolour-blooms-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 22 % → 27 % | 95.0 px | 0.12 | 1.26 | 910 |

## Brush Artist · Refs · #41 Coloured pencil hatching — own sheet
own sheet 600 × 600 · Pastel 1.00 · 4 px · 2.8 s

![Brush Artist · Refs · #41 Coloured pencil hatching — own sheet](Brush-Artist-Refs-41-Coloured-pencil-hatching-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 3 % → 13 % | 2.2 px | 0.35 | 4.64 | 5 |
| stroke 2 | 3 % → 7 % | 2.3 px | 0.35 | 2.29 | 4 |
| stroke 3 | 2 % → 11 % | 1.9 px | 0.35 | 4.38 | 4 |
| stroke 4 | 3 % → 19 % | 2.1 px | 0.35 | 6.73 | 4 |
| stroke 5 | 4 % → 7 % | 2.9 px | 0.35 | 1.83 | 5 |
| stroke 6 | 3 % → 13 % | 2.3 px | 0.35 | 4.19 | 4 |
| stroke 7 | 3 % → 15 % | 2.6 px | 0.35 | 4.43 | 3 |
| stroke 8 | 3 % → 12 % | 2.1 px | 0.35 | 4.20 | 5 |
| stroke 9 | 5 % → 11 % | 3.6 px | 0.35 | 2.27 | 4 |
| stroke 10 | 5 % → 15 % | 3.8 px | 0.35 | 2.99 | 4 |
| stroke 11 | 4 % → 13 % | 3.0 px | 0.35 | 3.28 | 4 |
| stroke 12 | 3 % → 3 % | 2.1 px | 0.35 | 1.00 | 5 |
| stroke 13 | 7 % → 17 % | 5.2 px | 0.35 | 2.45 | 4 |
| stroke 14 | 3 % → 13 % | 2.4 px | 0.35 | 4.19 | 3 |
| stroke 15 | 6 % → 12 % | 4.4 px | 0.35 | 2.09 | 5 |
| stroke 16 | 7 % → 11 % | 5.1 px | 0.35 | 1.61 | 5 |
| stroke 17 | 3 % → 3 % | 2.1 px | 0.35 | 1.00 | 4 |
| stroke 18 | 5 % → 8 % | 3.6 px | 0.35 | 1.65 | 5 |
| stroke 19 | 5 % → 13 % | 3.8 px | 0.35 | 2.72 | 4 |
| stroke 20 | 5 % → 14 % | 3.7 px | 0.35 | 2.92 | 5 |
| stroke 21 | 4 % → 13 % | 3.2 px | 0.35 | 3.20 | 3 |
| stroke 22 | 9 % → 16 % | 6.8 px | 0.35 | 1.77 | 8 |
| stroke 23 | 9 % → 13 % | 6.5 px | 0.35 | 1.55 | 4 |
| stroke 24 | 6 % → 14 % | 4.7 px | 0.35 | 2.18 | 9 |
| stroke 25 | 5 % → 10 % | 3.5 px | 0.35 | 2.27 | 5 |
| stroke 26 | 3 % → 6 % | 2.7 px | 0.35 | 1.81 | 4 |
| stroke 27 | 3 % → 7 % | 2.3 px | 0.35 | 2.26 | 7 |
| stroke 28 | 6 % → 10 % | 4.5 px | 0.35 | 1.70 | 7 |
| stroke 29 | 3 % → 13 % | 2.4 px | 0.35 | 4.21 | 5 |
| stroke 30 | 6 % → 9 % | 4.4 px | 0.35 | 1.46 | 9 |
| stroke 31 | 7 % → 14 % | 5.1 px | 0.35 | 2.14 | 6 |
| stroke 32 | 3 % → 6 % | 2.5 px | 0.35 | 1.78 | 5 |
| stroke 33 | 6 % → 11 % | 5.0 px | 0.35 | 1.67 | 5 |
| stroke 34 | 3 % → 6 % | 2.6 px | 0.35 | 1.73 | 5 |
| stroke 35 | 7 % → 14 % | 5.0 px | 0.35 | 2.09 | 4 |
| stroke 36 | 5 % → 5 % | 3.7 px | 0.35 | 1.01 | 5 |
| stroke 37 | 7 % → 15 % | 5.2 px | 0.35 | 2.15 | 5 |
| stroke 38 | 8 % → 13 % | 5.8 px | 0.35 | 1.66 | 5 |
| stroke 39 | 7 % → 11 % | 5.1 px | 0.35 | 1.67 | 6 |
| stroke 40 | 8 % → 18 % | 6.2 px | 0.35 | 2.21 | 7 |
| stroke 41 | 9 % → 13 % | 6.9 px | 0.35 | 1.48 | 9 |
| stroke 42 | 10 % → 17 % | 7.7 px | 0.35 | 1.73 | 4 |
| stroke 43 | 5 % → 9 % | 3.9 px | 0.35 | 1.66 | 4 |
| stroke 44 | 10 % → 13 % | 7.3 px | 0.35 | 1.40 | 4 |
| stroke 45 | 13 % → 18 % | 9.9 px | 0.35 | 1.35 | 5 |
| stroke 46 | 5 % → 7 % | 3.6 px | 0.34 | 1.41 | 3 |
| stroke 47 | 11 % → 13 % | 8.0 px | 0.35 | 1.20 | 4 |
| stroke 48 | 12 % → 16 % | 9.2 px | 0.35 | 1.34 | 8 |
| stroke 49 | 6 % → 9 % | 4.2 px | 0.35 | 1.65 | 5 |
| stroke 50 | 7 % → 7 % | 5.2 px | 0.34 | 1.00 | 6 |
| stroke 51 | 8 % → 15 % | 6.4 px | 0.35 | 1.74 | 4 |
| stroke 52 | 12 % → 14 % | 9.1 px | 0.35 | 1.19 | 5 |
| stroke 53 | 11 % → 14 % | 8.1 px | 0.35 | 1.36 | 3 |
| stroke 54 | 10 % → 14 % | 7.4 px | 0.35 | 1.47 | 4 |
| stroke 55 | 11 % → 14 % | 8.2 px | 0.35 | 1.33 | 5 |
| stroke 56 | 11 % → 12 % | 8.4 px | 0.35 | 1.11 | 5 |
| stroke 57 | 9 % → 13 % | 7.1 px | 0.35 | 1.37 | 5 |
| stroke 58 | 10 % → 11 % | 7.7 px | 0.35 | 1.14 | 4 |
| stroke 59 | 11 % → 13 % | 8.4 px | 0.35 | 1.18 | 5 |
| stroke 60 | 16 % → 20 % | 11.9 px | 0.35 | 1.26 | 3 |
| stroke 61 | 19 % → 20 % | 14.5 px | 0.35 | 1.04 | 5 |
| stroke 62 | 10 % → 10 % | 7.3 px | 0.35 | 1.00 | 2 |
| stroke 63 | 11 % → 12 % | 8.7 px | 0.35 | 1.07 | 3 |
| stroke 64 | 14 % → 14 % | 10.7 px | 0.35 | 1.02 | 5 |
| stroke 65 | 15 % → 15 % | 11.5 px | 0.35 | 1.00 | 7 |
| stroke 66 | 14 % → 14 % | 10.7 px | 0.35 | 1.00 | 3 |
| stroke 67 | 12 % → 12 % | 8.8 px | 0.35 | 1.06 | 6 |
| stroke 68 | 5 % → 9 % | 3.6 px | 0.35 | 1.88 | 7 |
| stroke 69 | 5 % → 5 % | 4.1 px | 0.35 | 1.00 | 4 |
| stroke 70 | 10 % → 13 % | 7.4 px | 0.35 | 1.28 | 5 |
| stroke 71 | 9 % → 11 % | 7.1 px | 0.35 | 1.15 | 4 |
| stroke 72 | 5 % → 7 % | 4.2 px | 0.35 | 1.23 | 6 |
| stroke 73 | 12 % → 12 % | 9.3 px | 0.35 | 1.00 | 6 |
| stroke 74 | 14 % → 14 % | 10.8 px | 0.35 | 1.00 | 5 |
| stroke 75 | 15 % → 15 % | 11.4 px | 0.35 | 1.00 | 3 |
| stroke 76 | 14 % → 14 % | 10.5 px | 0.35 | 1.00 | 5 |
| stroke 77 | 7 % → 10 % | 5.4 px | 0.35 | 1.34 | 6 |
| stroke 78 | 9 % → 9 % | 7.0 px | 0.35 | 1.00 | 5 |
| stroke 79 | 7 % → 7 % | 5.7 px | 0.35 | 1.00 | 2 |
| stroke 80 | 11 % → 11 % | 8.3 px | 0.35 | 1.00 | 6 |

Numbers say: wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #42 Oil pastel shaggy — own sheet
own sheet 600 × 600 · Pastel 1.00 · 18 px · 3.0 s

![Brush Artist · Refs · #42 Oil pastel shaggy — own sheet](Brush-Artist-Refs-42-Oil-pastel-shaggy-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 5 % → 27 % | 8.0 px | 0.28 | 5.73 | 9 |
| stroke 2 | 5 % → 24 % | 8.6 px | 0.28 | 4.69 | 11 |
| stroke 3 | 5 % → 29 % | 8.9 px | 0.28 | 5.42 | 8 |
| stroke 4 | 5 % → 11 % | 8.8 px | 0.28 | 2.08 | 10 |
| stroke 5 | 6 % → 11 % | 9.9 px | 0.28 | 1.85 | 8 |
| stroke 6 | 8 % → 37 % | 13.9 px | 0.29 | 4.44 | 10 |
| stroke 7 | 11 % → 31 % | 17.6 px | 0.28 | 2.90 | 10 |
| stroke 8 | 7 % → 38 % | 11.4 px | 0.28 | 5.55 | 16 |
| stroke 9 | 8 % → 21 % | 13.9 px | 0.28 | 2.53 | 9 |
| stroke 10 | 8 % → 18 % | 13.2 px | 0.28 | 2.32 | 15 |
| stroke 11 | 6 % → 27 % | 9.4 px | 0.28 | 4.74 | 12 |
| stroke 12 | 8 % → 19 % | 13.6 px | 0.28 | 2.29 | 14 |
| stroke 13 | 13 % → 24 % | 21.0 px | 0.28 | 1.92 | 17 |
| stroke 14 | 5 % → 23 % | 7.9 px | 0.28 | 4.77 | 15 |
| stroke 15 | 5 % → 24 % | 9.0 px | 0.29 | 4.38 | 15 |
| stroke 16 | 9 % → 21 % | 15.7 px | 0.29 | 2.18 | 9 |
| stroke 17 | 17 % → 39 % | 28.0 px | 0.29 | 2.34 | 11 |
| stroke 18 | 14 % → 25 % | 22.8 px | 0.29 | 1.79 | 11 |
| stroke 19 | 15 % → 32 % | 24.9 px | 0.28 | 2.09 | 13 |
| stroke 20 | 21 % → 39 % | 35.1 px | 0.28 | 1.85 | 10 |
| stroke 21 | 9 % → 16 % | 14.4 px | 0.28 | 1.88 | 12 |
| stroke 22 | 14 % → 17 % | 23.9 px | 0.28 | 1.20 | 8 |
| stroke 23 | 12 % → 17 % | 20.6 px | 0.29 | 1.34 | 9 |
| stroke 24 | 18 % → 26 % | 30.0 px | 0.29 | 1.44 | 9 |
| stroke 25 | 20 % → 34 % | 32.6 px | 0.28 | 1.74 | 9 |
| stroke 26 | 6 % → 14 % | 9.2 px | 0.28 | 2.43 | 9 |
| stroke 27 | 18 % → 26 % | 30.5 px | 0.29 | 1.41 | 10 |
| stroke 28 | 14 % → 24 % | 23.7 px | 0.28 | 1.68 | 7 |
| stroke 29 | 9 % → 27 % | 14.9 px | 0.29 | 3.01 | 12 |
| stroke 30 | 15 % → 36 % | 25.0 px | 0.29 | 2.43 | 11 |
| stroke 31 | 14 % → 17 % | 23.3 px | 0.28 | 1.23 | 12 |
| stroke 32 | 16 % → 29 % | 27.0 px | 0.29 | 1.82 | 10 |
| stroke 33 | 15 % → 16 % | 24.5 px | 0.29 | 1.09 | 9 |
| stroke 34 | 19 % → 27 % | 31.4 px | 0.28 | 1.44 | 8 |
| stroke 35 | 26 % → 36 % | 42.6 px | 0.28 | 1.40 | 11 |
| stroke 36 | 25 % → 34 % | 41.0 px | 0.28 | 1.36 | 13 |
| stroke 37 | 12 % → 12 % | 19.3 px | 0.28 | 1.03 | 16 |
| stroke 38 | 19 % → 25 % | 31.7 px | 0.28 | 1.30 | 11 |
| stroke 39 | 16 % → 22 % | 27.3 px | 0.28 | 1.37 | 9 |
| stroke 40 | 22 % → 31 % | 36.6 px | 0.28 | 1.38 | 12 |
| stroke 41 | 32 % → 36 % | 53.1 px | 0.28 | 1.12 | 8 |
| stroke 42 | 23 % → 30 % | 38.2 px | 0.29 | 1.29 | 17 |
| stroke 43 | 12 % → 12 % | 20.3 px | 0.28 | 1.00 | 12 |
| stroke 44 | 30 % → 37 % | 48.9 px | 0.28 | 1.26 | 9 |
| stroke 45 | 16 % → 16 % | 26.2 px | 0.28 | 1.00 | 7 |
| stroke 46 | 29 % → 34 % | 48.0 px | 0.29 | 1.15 | 8 |
| stroke 47 | 38 % → 41 % | 62.0 px | 0.28 | 1.10 | 12 |
| stroke 48 | 29 % → 36 % | 47.8 px | 0.29 | 1.27 | 9 |
| stroke 49 | 27 % → 30 % | 45.1 px | 0.29 | 1.11 | 10 |
| stroke 50 | 38 % → 40 % | 63.4 px | 0.28 | 1.06 | 8 |
| stroke 51 | 16 % → 16 % | 26.1 px | 0.28 | 1.00 | 9 |
| stroke 52 | 37 % → 38 % | 62.4 px | 0.29 | 1.01 | 6 |
| stroke 53 | 22 % → 26 % | 36.9 px | 0.28 | 1.18 | 8 |
| stroke 54 | 17 % → 19 % | 29.1 px | 0.29 | 1.09 | 6 |
| stroke 55 | 15 % → 15 % | 25.0 px | 0.28 | 1.00 | 13 |
| stroke 56 | 13 % → 14 % | 21.6 px | 0.28 | 1.08 | 10 |
| stroke 57 | 23 % → 23 % | 37.7 px | 0.29 | 1.00 | 13 |
| stroke 58 | 28 % → 29 % | 46.1 px | 0.28 | 1.05 | 10 |
| stroke 59 | 40 % → 40 % | 67.3 px | 0.28 | 1.00 | 11 |
| stroke 60 | 22 % → 22 % | 35.6 px | 0.28 | 1.00 | 9 |

Numbers say: wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #43 Dragged black ink blocks — own sheet
own sheet 600 × 600 · Gouache 1.00 · 70 px · 7.4 s

![Brush Artist · Refs · #43 Dragged black ink blocks — own sheet](Brush-Artist-Refs-43-Dragged-black-ink-blocks-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 15 % → 8 % | 35.8 px | 0.46 | 0.54 | 423 |
| stroke 2 | 18 % → 13 % | 62.1 px | 0.46 | 0.75 | 487 |
| stroke 3 | 19 % → 14 % | 68.8 px | 0.46 | 0.75 | 379 |
| stroke 4 | 19 % → 13 % | 67.6 px | 0.46 | 0.65 | 458 |
| stroke 5 | 26 % → 14 % | 61.7 px | 0.46 | 0.54 | 399 |

## Brush Artist · Refs · #44 Blue looping ribbon — own sheet
own sheet 600 × 600 · Oil 1.00 · 80 px · 5.1 s

![Brush Artist · Refs · #44 Blue looping ribbon — own sheet](Brush-Artist-Refs-44-Blue-looping-ribbon-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 32 % → 32 % | 42.2 px | 0.78 | 1.00 | 2864 |

## Brush Artist · Refs · #45 Soft pastel pepper — own sheet
own sheet 600 × 600 · Pastel 1.00 · 40 px · 4.7 s

![Brush Artist · Refs · #45 Soft pastel pepper — own sheet](Brush-Artist-Refs-45-Soft-pastel-pepper-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 10 % → 39 % | 11.3 px | 0.49 | 3.75 | 295 |
| stroke 2 | 18 % → 34 % | 21.3 px | 0.49 | 1.87 | 370 |
| stroke 3 | 25 % → 37 % | 17.6 px | 0.49 | 1.46 | 349 |
| stroke 4 | 24 % → 35 % | 30.5 px | 0.49 | 1.43 | 398 |
| stroke 5 | 30 % → 30 % | 21.2 px | 0.49 | 1.00 | 203 |
| stroke 6 | 36 % → 44 % | 23.0 px | 0.48 | 1.23 | 340 |
| stroke 7 | 39 % → 43 % | 21.6 px | 0.48 | 1.10 | 444 |
| stroke 8 | 44 % → 44 % | 44.4 px | 0.49 | 1.00 | 295 |

Numbers say: wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #46 Red-brown ink lips — own sheet
own sheet 600 × 600 · Watercolour 1.00 · 50 px · 5.4 s

![Brush Artist · Refs · #46 Red-brown ink lips — own sheet](Brush-Artist-Refs-46-Red-brown-ink-lips-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 13 % → 27 % | 55.7 px | 0.59 | 2.00 | 114 |
| stroke 2 | 19 % → 33 % | 82.1 px | 0.54 | 1.76 | 112 |

Numbers say: wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #47 Pink knife slabs — own sheet
own sheet 600 × 600 · Impasto 1.00 · 90 px · 4.7 s

![Brush Artist · Refs · #47 Pink knife slabs — own sheet](Brush-Artist-Refs-47-Pink-knife-slabs-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 17 % → 32 % | 83.2 px | 0.11 | 1.94 | 299 |
| stroke 2 | 29 % → 43 % | 165.8 px | 0.11 | 1.46 | 337 |
| stroke 3 | 29 % → 43 % | 165.7 px | 0.11 | 1.47 | 311 |
| stroke 4 | 39 % → 38 % | 165.7 px | 0.11 | 0.98 | 386 |

Numbers say: wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #48 Black bands with drips — own sheet
own sheet 600 × 600 · Gouache 1.00 · 70 px · 8.7 s

![Brush Artist · Refs · #48 Black bands with drips — own sheet](Brush-Artist-Refs-48-Black-bands-with-drips-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 28 % → 41 % | 73.2 px | 0.39 | 1.46 | 515 |
| stroke 2 | 43 % → 57 % | 137.5 px | 0.39 | 1.33 | 503 |
| stroke 3 | 45 % → 57 % | 141.4 px | 0.39 | 1.27 | 505 |
| stroke 4 | 48 % → 46 % | 140.3 px | 0.39 | 0.96 | 468 |

## Brush Artist · Refs · #49 Magenta letters round brush — own sheet
own sheet 600 × 600 · Ink 1.00 · 30 px · 7.6 s

![Brush Artist · Refs · #49 Magenta letters round brush — own sheet](Brush-Artist-Refs-49-Magenta-letters-round-brush-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 27 % → 46 % | 64.3 px | 0.52 | 1.70 | 32 |
| stroke 2 | 29 % → 40 % | 52.5 px | 0.53 | 1.40 | 37 |
| stroke 3 | 41 % → 67 % | 96.3 px | 0.52 | 1.64 | 47 |
| stroke 4 | 34 % → 52 % | 53.7 px | 0.52 | 1.55 | 159 |
| stroke 5 | 40 % → 66 % | 94.7 px | 0.52 | 1.65 | 76 |
| stroke 6 | 54 % → 70 % | 231.2 px | 0.52 | 1.29 | 22 |
| stroke 7 | 41 % → 56 % | 63.9 px | 0.52 | 1.35 | 114 |
| stroke 8 | 36 % → 61 % | 91.9 px | 0.53 | 1.73 | 69 |
| stroke 9 | 49 % → 60 % | 152.9 px | 0.53 | 1.24 | 24 |
| stroke 10 | 42 % → 72 % | 100.4 px | 0.52 | 1.71 | 79 |
| stroke 11 | 52 % → 72 % | 219.8 px | 0.52 | 1.39 | 19 |
| stroke 12 | 53 % → 68 % | 82.2 px | 0.52 | 1.29 | 126 |
| stroke 13 | 42 % → 54 % | 115.9 px | 0.53 | 1.29 | 30 |
| stroke 14 | 45 % → 69 % | 131.7 px | 0.53 | 1.52 | 29 |
| stroke 15 | 43 % → 63 % | 102.4 px | 0.52 | 1.46 | 88 |
| stroke 16 | 52 % → 61 % | 220.3 px | 0.52 | 1.18 | 14 |
| stroke 17 | 53 % → 64 % | 82.2 px | 0.52 | 1.19 | 121 |
| stroke 18 | 36 % → 44 % | 99.6 px | 0.52 | 1.22 | 28 |
| stroke 19 | 54 % → 53 % | 123.7 px | 0.52 | 0.99 | 79 |
| stroke 20 | 54 % → 54 % | 125.3 px | 0.52 | 1.00 | 30 |
| stroke 21 | 49 % → 49 % | 81.3 px | 0.52 | 1.00 | 86 |

Numbers say: wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #50 Thick swipes on photo — own sheet
own sheet 600 × 600 · Impasto 1.00 · 40 px · 2.7 s

![Brush Artist · Refs · #50 Thick swipes on photo — own sheet](Brush-Artist-Refs-50-Thick-swipes-on-photo-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 9 % → 21 % | 42.8 px | 0.33 | 2.35 | 43 |
| stroke 2 | 9 % → 16 % | 42.5 px | 0.33 | 1.79 | 34 |
| stroke 3 | 10 % → 11 % | 41.9 px | 0.33 | 1.07 | 51 |
| stroke 4 | 11 % → 18 % | 42.7 px | 0.33 | 1.64 | 36 |
| stroke 5 | 11 % → 10 % | 41.9 px | 0.33 | 0.95 | 36 |
| stroke 6 | 17 % → 21 % | 97.7 px | 0.32 | 1.20 | 29 |
| stroke 7 | 22 % → 26 % | 92.8 px | 0.33 | 1.18 | 41 |
| stroke 8 | 21 % → 21 % | 119.9 px | 0.33 | 0.97 | 32 |
| stroke 9 | 9 % → 10 % | 42.1 px | 0.32 | 1.09 | 37 |
| stroke 10 | 22 % → 21 % | 73.6 px | 0.32 | 0.96 | 90 |
| stroke 11 | 9 % → 8 % | 42.7 px | 0.33 | 0.95 | 34 |
| stroke 12 | 17 % → 16 % | 93.2 px | 0.33 | 0.96 | 27 |

Numbers say: wet paint spreads well beyond the stroke.

## Brush Artist · Ink — dry brush — own sheet
own sheet 600 × 600 · Gouache 1.00 · 30 px · 2.5 s

![Brush Artist · Ink — dry brush — own sheet](Brush-Artist-Ink-dry-brush-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| ear | 6 % → 2 % | 7.0 px | 0.86 | 0.34 | 451 |
| drag0 | 6 % → 9 % | 11.3 px | 0.86 | 1.42 | 115 |
| drag1 | 9 % → 9 % | 18.5 px | 0.86 | 1.02 | 87 |
| drag2 | 11 % → 10 % | 25.6 px | 0.86 | 0.85 | 71 |
| drag3 | 13 % → 10 % | 32.8 px | 0.86 | 0.77 | 56 |

## Brush Artist · Watercolour — blue — own sheet
own sheet 600 × 600 · Watercolour 0.93 · Ink 0.07 · 40 px · 6.9 s

![Brush Artist · Watercolour — blue — own sheet](Brush-Artist-Watercolour-blue-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| s0 | 7 % → 24 % | 28.8 px | 0.30 | 3.32 | 42 |
| s1 | 6 % → 33 % | 10.1 px | 0.37 | 6.00 | 101 |
| s2 | 10 % → 19 % | 44.2 px | 0.26 | 1.81 | 38 |
| s3 | 10 % → 18 % | 26.7 px | 0.31 | 1.92 | 39 |
| s4 | 14 % → 30 % | 38.6 px | 0.36 | 2.16 | 42 |
| s5 | 19 % → 29 % | 39.3 px | 0.37 | 1.54 | 41 |
| s6 | 18 % → 22 % | 48.7 px | 0.31 | 1.25 | 39 |
| s7 | 25 % → 36 % | 32.7 px | 0.37 | 1.46 | 27 |
| s8 | 21 % → 25 % | 79.8 px | 0.30 | 1.20 | 34 |

Numbers say: wet paint spreads well beyond the stroke.

## Brush Artist · Charcoal — stick — own sheet
own sheet 600 × 600 · Charcoal 0.78 · Pastel 0.22 · 28 px · 1.2 s

![Brush Artist · Charcoal — stick — own sheet](Brush-Artist-Charcoal-stick-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| finger0 | 12 % → 25 % | 21.7 px | 0.83 | 2.02 | 59 |
| tip0 | 12 % → 21 % | 33.4 px | 0.83 | 1.69 | 7 |
| finger1 | 23 % → 40 % | 41.1 px | 0.83 | 1.71 | 36 |
| tip1 | 21 % → 29 % | 56.0 px | 0.83 | 1.41 | 9 |
| finger2 | 23 % → 35 % | 41.3 px | 0.83 | 1.53 | 33 |
| tip2 | 21 % → 29 % | 56.0 px | 0.83 | 1.41 | 13 |
| finger3 | 23 % → 27 % | 41.6 px | 0.83 | 1.15 | 36 |
| tip3 | 21 % → 21 % | 56.3 px | 0.83 | 1.00 | 13 |
| cig0 | 33 % → 46 % | 73.2 px | 0.83 | 1.40 | 15 |
| cig1 | 35 % → 46 % | 78.8 px | 0.83 | 1.29 | 20 |
| cig2 | 38 % → 46 % | 84.4 px | 0.83 | 1.21 | 17 |
| cig3 | 40 % → 46 % | 90.0 px | 0.83 | 1.13 | 12 |
| cig4 | 43 % → 45 % | 95.5 px | 0.83 | 1.06 | 16 |
| cig5 | 45 % → 45 % | 101.1 px | 0.83 | 1.00 | 12 |

Numbers say: wet paint spreads well beyond the stroke.

