![All brushes](contact.png)

# Brush Lab — 150 brushes · Nov 4, 2026 at 6:45 AM

Every sheet: 1500 × 600, ten strokes in a 5 × 2 grid — 1. light line · 2. heavy line · 3. pressure swell · 4. fast wave · 5. slow wave · 6. spiral · 7. loop · 8. tilted · 9. over the wet one · 10. long, no reload (cell 8 holds «tilted» and «over the wet one» crossed). The CPU reference of Mamay's paint engine; the wet layer settles 20 s at the end.

Columns: **covered** = share of the cell with paint right after the stroke → after settling; **width** = painted area of the stroke ÷ its length (px); **dark** = mean darkness of the painted pixels above the paper's own grain (0 = paper, 1 = black); **spread** = how far wet paint went beyond the stroke (1.0 = stayed); **ms** = the stroke on the CPU; long stroke: paint in each quarter of its length (it should run out: wet → streaks → dry tail).

## Ink Line
Ink · 12 px · 24.0 s

![Ink Line](Ink-Line.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 1 % → 4 % | 4.3 px | 0.55 | 2.44 | 41 |
| heavy line | 5 % → 6 % | 15.7 px | 0.68 | 1.13 | 64 |
| pressure swell | 3 % → 4 % | 11.3 px | 0.64 | 1.40 | 38 |
| fast wave | 10 % → 11 % | 11.2 px | 0.59 | 1.11 | 117 |
| slow wave | 8 % → 10 % | 9.6 px | 0.57 | 1.16 | 112 |
| spiral | 14 % → 15 % | 8.9 px | 0.50 | 1.07 | 236 |
| loop | 8 % → 9 % | 10.6 px | 0.61 | 1.16 | 142 |
| tilted | 5 % → 5 % | 14.4 px | 0.65 | 1.05 | 81 |
| over the wet one | 10 % → 11 % | 12.5 px | 0.65 | 1.15 | 67 |
| long, no reload | 18 % → 17 % | 8.1 px | 0.47 | 0.96 | 338 | quarters: 0.22 → 0.09 → 0.04 → 0.02

Numbers say: light vs heavy: width 4.3 → 15.7 px, dark 0.55 → 0.68; wet paint spreads well beyond the stroke.

## Dense Ink
Ink · 14 px · 24.7 s

![Dense Ink](Dense-Ink.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 5 % → 7 % | 15.2 px | 0.72 | 1.26 | 48 |
| heavy line | 7 % → 7 % | 19.1 px | 0.73 | 1.09 | 74 |
| pressure swell | 5 % → 6 % | 17.9 px | 0.72 | 1.17 | 45 |
| fast wave | 13 % → 13 % | 15.3 px | 0.69 | 1.01 | 132 |
| slow wave | 12 % → 12 % | 13.6 px | 0.67 | 1.04 | 149 |
| spiral | 18 % → 15 % | 12.2 px | 0.65 | 0.80 | 278 |
| loop | 11 % → 12 % | 14.8 px | 0.69 | 1.08 | 162 |
| tilted | 5 % → 6 % | 14.6 px | 0.72 | 1.07 | 96 |
| over the wet one | 12 % → 13 % | 17.7 px | 0.72 | 1.11 | 59 |
| long, no reload | 23 % → 15 % | 10.1 px | 0.64 | 0.66 | 339 | quarters: 0.30 → 0.12 → 0.04 → 0.02

Numbers say: light vs heavy: width 15.2 → 19.1 px, dark 0.72 → 0.73.

## Transparent Wash
Watercolor · 22 px · 25.5 s

![Transparent Wash](Transparent-Wash.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 2 % → 5 % | 6.9 px | 0.27 | 2.25 | 39 |
| heavy line | 7 % → 9 % | 20.4 px | 0.27 | 1.22 | 59 |
| pressure swell | 4 % → 6 % | 15.2 px | 0.28 | 1.54 | 35 |
| fast wave | 14 % → 16 % | 16.1 px | 0.20 | 1.17 | 115 |
| slow wave | 12 % → 15 % | 13.7 px | 0.21 | 1.28 | 174 |
| spiral | 18 % → 22 % | 11.9 px | 0.16 | 1.23 | 217 |
| loop | 11 % → 13 % | 14.5 px | 0.22 | 1.20 | 121 |
| tilted | 8 % → 8 % | 21.1 px | 0.24 | 1.06 | 79 |
| over the wet one | 13 % → 16 % | 16.4 px | 0.24 | 1.18 | 50 |
| long, no reload | 26 % → 32 % | 11.6 px | 0.13 | 1.22 | 308 | quarters: 0.11 → 0.04 → 0.02 → 0.01

Numbers say: light vs heavy: width 6.9 → 20.4 px, dark 0.27 → 0.27; wet paint spreads well beyond the stroke.

## Dry Brush
Gouache · 24 px · 23.8 s

![Dry Brush](Dry-Brush.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 5 % → 0 % | 14.0 px | 0.65 | 0.09 | 67 |
| heavy line | 6 % → 0 % | 18.6 px | 0.65 | 0.02 | 96 |
| pressure swell | 5 % → 0 % | 18.2 px | 0.65 | 0.08 | 50 |
| fast wave | 6 % → 1 % | 7.3 px | 0.65 | 0.08 | 147 |
| slow wave | 7 % → 0 % | 8.1 px | 0.65 | 0.06 | 250 |
| spiral | 7 % → 0 % | 4.6 px | 0.65 | 0.07 | 244 |
| loop | 10 % → 0 % | 12.4 px | 0.65 | 0.04 | 190 |
| tilted | 4 % → 3 % | 10.6 px | 0.65 | 0.88 | 104 |
| over the wet one | 9 % → 1 % | 14.5 px | 0.65 | 0.12 | 73 |
| long, no reload | 6 % → 1 % | 2.9 px | 0.65 | 0.14 | 360 | quarters: 0.12 → 0.00 → 0.00 → 0.00

Numbers say: light vs heavy: width 14.0 → 18.6 px, dark 0.65 → 0.65.

## Wax Crayon
Wax · 8 px · 10.2 s

![Wax Crayon](Wax-Crayon.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 1 % → 1 % | 2.5 px | 0.71 | 1.00 | 15 |
| heavy line | 1 % → 1 % | 3.9 px | 0.69 | 1.00 | 19 |
| pressure swell | 1 % → 1 % | 3.3 px | 0.70 | 1.00 | 12 |
| fast wave | 3 % → 3 % | 3.5 px | 0.69 | 1.00 | 47 |
| slow wave | 3 % → 3 % | 3.4 px | 0.70 | 1.00 | 40 |
| spiral | 5 % → 5 % | 3.3 px | 0.70 | 1.00 | 70 |
| loop | 3 % → 3 % | 3.3 px | 0.70 | 1.00 | 46 |
| tilted | 2 % → 2 % | 5.6 px | 0.68 | 1.00 | 31 |
| over the wet one | 3 % → 3 % | 3.6 px | 0.68 | 1.00 | 17 |
| long, no reload | 7 % → 7 % | 3.3 px | 0.70 | 1.00 | 106 | quarters: 0.06 → 0.06 → 0.06 → 0.06

Numbers say: light vs heavy: width 2.5 → 3.9 px, dark 0.71 → 0.69; the long stroke does not run out of paint.

## Oil Pastel
Wax · 12 px · 10.6 s

![Oil Pastel](Oil-Pastel.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 1 % → 1 % | 4.0 px | 0.68 | 1.00 | 20 |
| heavy line | 2 % → 2 % | 6.5 px | 0.68 | 1.00 | 29 |
| pressure swell | 2 % → 2 % | 5.7 px | 0.69 | 1.00 | 18 |
| fast wave | 5 % → 5 % | 5.7 px | 0.68 | 1.00 | 65 |
| slow wave | 5 % → 5 % | 5.5 px | 0.68 | 1.00 | 57 |
| spiral | 8 % → 8 % | 5.5 px | 0.68 | 1.00 | 101 |
| loop | 4 % → 4 % | 5.6 px | 0.68 | 1.00 | 51 |
| tilted | 2 % → 2 % | 6.8 px | 0.68 | 1.00 | 39 |
| over the wet one | 5 % → 5 % | 5.8 px | 0.68 | 1.00 | 25 |
| long, no reload | 13 % → 13 % | 5.6 px | 0.68 | 1.00 | 231 | quarters: 0.10 → 0.09 → 0.10 → 0.10

Numbers say: light vs heavy: width 4.0 → 6.5 px, dark 0.68 → 0.68; the long stroke does not run out of paint.

## Charcoal
Charcoal · 5 px · 13.6 s

![Charcoal](Charcoal.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 1 % → 1 % | 2.0 px | 0.74 | 1.00 | 27 |
| heavy line | 1 % → 1 % | 3.0 px | 0.74 | 1.00 | 15 |
| pressure swell | 1 % → 1 % | 2.7 px | 0.74 | 1.00 | 12 |
| fast wave | 2 % → 2 % | 2.7 px | 0.73 | 1.00 | 33 |
| slow wave | 2 % → 2 % | 2.6 px | 0.74 | 1.00 | 39 |
| spiral | 4 % → 4 % | 2.5 px | 0.74 | 1.00 | 66 |
| loop | 2 % → 2 % | 2.6 px | 0.74 | 1.00 | 44 |
| tilted | 2 % → 2 % | 4.3 px | 0.72 | 1.00 | 18 |
| over the wet one | 2 % → 2 % | 2.4 px | 0.72 | 1.00 | 16 |
| long, no reload | 6 % → 6 % | 2.7 px | 0.73 | 1.00 | 102 | quarters: 0.05 → 0.05 → 0.05 → 0.05

Numbers say: light vs heavy: width 2.0 → 3.0 px, dark 0.74 → 0.74; the long stroke does not run out of paint.

## Impasto
Heavy acrylic · 22 px · 20.8 s

![Impasto](Impasto.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 8 % → 8 % | 24.1 px | 0.71 | 0.93 | 67 |
| heavy line | 10 % → 9 % | 28.8 px | 0.70 | 0.94 | 124 |
| pressure swell | 7 % → 7 % | 28.1 px | 0.72 | 0.94 | 55 |
| fast wave | 20 % → 13 % | 23.5 px | 0.71 | 0.64 | 200 |
| slow wave | 21 % → 14 % | 24.5 px | 0.71 | 0.66 | 341 |
| spiral | 30 % → 14 % | 20.0 px | 0.71 | 0.46 | 475 |
| loop | 18 % → 14 % | 23.9 px | 0.71 | 0.77 | 307 |
| tilted | 8 % → 8 % | 21.8 px | 0.70 | 1.00 | 178 |
| over the wet one | 17 % → 15 % | 25.4 px | 0.70 | 0.91 | 140 |
| long, no reload | 34 % → 14 % | 15.2 px | 0.71 | 0.41 | 732 | quarters: 0.38 → 0.21 → 0.10 → 0.03

Numbers say: light vs heavy: width 24.1 → 28.8 px, dark 0.71 → 0.70.

## Oil Round
Oil · 18 px · 22.7 s

![Oil Round](Oil-Round.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 2 % → 2 % | 7.2 px | 0.75 | 1.00 | 80 |
| heavy line | 7 % → 7 % | 19.3 px | 0.73 | 1.00 | 90 |
| pressure swell | 4 % → 4 % | 13.7 px | 0.72 | 1.00 | 48 |
| fast wave | 11 % → 11 % | 12.7 px | 0.65 | 1.00 | 163 |
| slow wave | 8 % → 8 % | 9.0 px | 0.57 | 1.00 | 208 |
| spiral | 10 % → 10 % | 6.6 px | 0.50 | 1.00 | 259 |
| loop | 5 % → 5 % | 7.1 px | 0.45 | 1.00 | 118 |
| tilted | 4 % → 4 % | 10.1 px | 0.52 | 1.00 | 66 |
| over the wet one | 6 % → 6 % | 7.4 px | 0.52 | 1.00 | 74 |
| long, no reload | 15 % → 15 % | 6.8 px | 0.42 | 1.00 | 658 | quarters: 0.08 → 0.08 → 0.07 → 0.06

Numbers say: light vs heavy: width 7.2 → 19.3 px, dark 0.75 → 0.73.

## Palette Knife
Oil · 20 px · 21.8 s

![Palette Knife](Palette-Knife.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 8 % → 8 % | 21.9 px | 0.67 | 1.00 | 34 |
| heavy line | 8 % → 8 % | 22.5 px | 0.73 | 1.00 | 16 |
| pressure swell | 6 % → 6 % | 22.4 px | 0.74 | 1.00 | 6 |
| fast wave | 17 % → 17 % | 19.3 px | 0.49 | 1.00 | 27 |
| slow wave | 17 % → 17 % | 19.9 px | 0.43 | 1.00 | 40 |
| spiral | 18 % → 18 % | 11.7 px | 0.45 | 1.00 | 58 |
| loop | 16 % → 16 % | 21.0 px | 0.58 | 1.00 | 24 |
| tilted | 5 % → 5 % | 15.0 px | 0.72 | 1.00 | 12 |
| over the wet one | 13 % → 13 % | 21.0 px | 0.72 | 1.00 | 11 |
| long, no reload | 17 % → 17 % | 7.5 px | 0.47 | 1.00 | 121 | quarters: 0.29 → 0.05 → 0.00 → 0.00

Numbers say: light vs heavy: width 21.9 → 22.5 px, dark 0.67 → 0.73; pressure barely changes the width.

## Water
Watercolor · 20 px · 42.6 s · over bands of wet oil paint and oil pastel in turn (it works on paint already there: look at what it does to the bands; covered counts the bands too)

![Water](Water.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 25 % → 27 % | 73.8 px | 0.80 | 1.06 | 33 |
| heavy line | 24 % → 25 % | 69.8 px | 0.81 | 1.04 | 91 |
| pressure swell | 24 % → 25 % | 89.6 px | 0.81 | 1.03 | 55 |
| fast wave | 24 % → 26 % | 27.7 px | 0.81 | 1.07 | 157 |
| slow wave | 24 % → 25 % | 27.7 px | 0.81 | 1.06 | 220 |
| spiral | 24 % → 26 % | 15.9 px | 0.81 | 1.07 | 224 |
| loop | 24 % → 25 % | 31.1 px | 0.81 | 1.03 | 180 |
| tilted | 24 % → 24 % | 67.0 px | 0.81 | 1.00 | 101 |
| over the wet one | 24 % → 25 % | 0.0 px | 0.81 | 1.06 | 77 |
| long, no reload | 24 % → 26 % | 10.7 px | 0.81 | 1.08 | 314 | quarters: 0.21 → 0.27 → 0.18 → 0.27

Numbers say: light vs heavy: width 73.8 → 69.8 px, dark 0.80 → 0.81; pressure barely changes the width; the long stroke does not run out of paint.

## Blender
Pastel · 16 px · 25.8 s · over bands of wet oil paint and oil pastel in turn (it works on paint already there: look at what it does to the bands; covered counts the bands too)

![Blender](Blender.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 24 % → 24 % | 70.7 px | 0.81 | 1.00 | 29 |
| heavy line | 25 % → 25 % | 72.1 px | 0.80 | 1.00 | 41 |
| pressure swell | 24 % → 24 % | 91.3 px | 0.81 | 1.00 | 28 |
| fast wave | 26 % → 26 % | 30.0 px | 0.79 | 1.00 | 78 |
| slow wave | 26 % → 26 % | 29.9 px | 0.80 | 1.00 | 99 |
| spiral | 28 % → 28 % | 18.7 px | 0.77 | 1.00 | 137 |
| loop | 25 % → 25 % | 32.9 px | 0.80 | 1.00 | 92 |
| tilted | 25 % → 25 % | 70.1 px | 0.79 | 1.00 | 59 |
| over the wet one | 26 % → 26 % | 1.8 px | 0.79 | 1.00 | 40 |
| long, no reload | 30 % → 30 % | 13.7 px | 0.76 | 1.00 | 305 | quarters: 0.20 → 0.28 → 0.23 → 0.30

Numbers say: light vs heavy: width 70.7 → 72.1 px, dark 0.81 → 0.80; pressure barely changes the width; the long stroke does not run out of paint.

## Eraser
Eraser · 16 px · 25.7 s · over bands of wet oil paint and oil pastel in turn (it works on paint already there: look at what it does to the bands; covered counts the bands too)

![Eraser](Eraser.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 24 % → 24 % | 69.5 px | 0.82 | 1.00 | 40 |
| heavy line | 23 % → 23 % | 67.9 px | 0.82 | 1.00 | 41 |
| pressure swell | 23 % → 23 % | 87.3 px | 0.82 | 1.00 | 28 |
| fast wave | 22 % → 22 % | 25.7 px | 0.82 | 1.00 | 113 |
| slow wave | 22 % → 22 % | 25.7 px | 0.82 | 1.00 | 98 |
| spiral | 22 % → 22 % | 14.4 px | 0.82 | 1.00 | 143 |
| loop | 22 % → 22 % | 28.6 px | 0.82 | 1.00 | 91 |
| tilted | 23 % → 23 % | 65.1 px | 0.82 | 1.00 | 67 |
| over the wet one | 23 % → 23 % | 0.0 px | 0.82 | 1.00 | 45 |
| long, no reload | 20 % → 20 % | 8.9 px | 0.82 | 1.00 | 406 | quarters: 0.15 → 0.20 → 0.15 → 0.20

Numbers say: light vs heavy: width 69.5 → 67.9 px, dark 0.82 → 0.82; pressure barely changes the width; the long stroke does not run out of paint.

## Fan
Gouache · 30 px · 33.9 s

![Fan](Fan.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 9 % → 3 % | 25.7 px | 0.63 | 0.37 | 73 |
| heavy line | 11 % → 4 % | 31.0 px | 0.63 | 0.39 | 68 |
| pressure swell | 8 % → 5 % | 31.7 px | 0.63 | 0.55 | 34 |
| fast wave | 18 % → 5 % | 20.3 px | 0.63 | 0.26 | 122 |
| slow wave | 18 % → 5 % | 21.1 px | 0.63 | 0.25 | 188 |
| spiral | 24 % → 5 % | 15.8 px | 0.63 | 0.20 | 197 |
| loop | 17 % → 5 % | 22.7 px | 0.63 | 0.29 | 98 |
| tilted | 5 % → 6 % | 15.1 px | 0.63 | 1.05 | 60 |
| over the wet one | 16 % → 8 % | 29.8 px | 0.63 | 0.50 | 73 |
| long, no reload | 23 % → 5 % | 10.1 px | 0.63 | 0.22 | 500 | quarters: 0.29 → 0.07 → 0.01 → 0.00

Numbers say: light vs heavy: width 25.7 → 31.0 px, dark 0.63 → 0.63.

## Sponge
Gouache · 30 px · 33.8 s

![Sponge](Sponge.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 4 % → 0 % | 11.4 px | 0.62 | 0.12 | 56 |
| heavy line | 12 % → 2 % | 35.4 px | 0.62 | 0.14 | 126 |
| pressure swell | 7 % → 2 % | 27.9 px | 0.62 | 0.27 | 46 |
| fast wave | 20 % → 4 % | 23.2 px | 0.62 | 0.19 | 140 |
| slow wave | 21 % → 4 % | 23.7 px | 0.62 | 0.18 | 281 |
| spiral | 28 % → 4 % | 18.3 px | 0.62 | 0.14 | 234 |
| loop | 18 % → 5 % | 23.0 px | 0.62 | 0.29 | 114 |
| tilted | 7 % → 7 % | 18.2 px | 0.62 | 1.04 | 132 |
| over the wet one | 16 % → 6 % | 27.8 px | 0.62 | 0.37 | 74 |
| long, no reload | 29 % → 5 % | 12.9 px | 0.62 | 0.17 | 522 | quarters: 0.29 → 0.13 → 0.07 → 0.04

Numbers say: light vs heavy: width 11.4 → 35.4 px, dark 0.62 → 0.62.

## Ink — sumi brush
Watercolor · 22 px · 36.0 s

![Ink — sumi brush](Ink-sumi-brush.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 8 % → 9 % | 23.9 px | 0.87 | 1.12 | 89 |
| heavy line | 13 % → 13 % | 38.1 px | 0.87 | 1.01 | 70 |
| pressure swell | 9 % → 10 % | 34.5 px | 0.87 | 1.04 | 51 |
| fast wave | 28 % → 28 % | 32.6 px | 0.85 | 1.00 | 170 |
| slow wave | 26 % → 26 % | 29.8 px | 0.86 | 1.02 | 269 |
| spiral | 39 % → 38 % | 25.5 px | 0.81 | 0.99 | 366 |
| loop | 22 % → 22 % | 28.6 px | 0.87 | 1.02 | 200 |
| tilted | 9 % → 9 % | 25.4 px | 0.87 | 1.00 | 108 |
| over the wet one | 20 % → 21 % | 30.6 px | 0.87 | 1.03 | 105 |
| long, no reload | 45 % → 43 % | 20.3 px | 0.76 | 0.95 | 553 | quarters: 0.56 → 0.45 → 0.30 → 0.20

Numbers say: light vs heavy: width 23.9 → 38.1 px, dark 0.87 → 0.87.

## Ink — wash
Watercolor · 40 px · 46.2 s

![Ink — wash](Ink-wash.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 13 % → 13 % | 37.6 px | 0.77 | 1.01 | 92 |
| heavy line | 19 % → 19 % | 55.6 px | 0.72 | 1.00 | 197 |
| pressure swell | 13 % → 13 % | 48.6 px | 0.76 | 1.01 | 127 |
| fast wave | 42 % → 42 % | 48.3 px | 0.69 | 1.01 | 368 |
| slow wave | 40 % → 40 % | 45.8 px | 0.75 | 1.01 | 448 |
| spiral | 61 % → 62 % | 40.3 px | 0.69 | 1.01 | 443 |
| loop | 34 % → 34 % | 44.0 px | 0.75 | 1.00 | 225 |
| tilted | 15 % → 15 % | 41.2 px | 0.76 | 1.00 | 125 |
| over the wet one | 30 % → 31 % | 43.4 px | 0.76 | 1.02 | 112 |
| long, no reload | 74 % → 75 % | 33.1 px | 0.64 | 1.02 | 694 | quarters: 0.68 → 0.60 → 0.47 → 0.33

Numbers say: light vs heavy: width 37.6 → 55.6 px, dark 0.77 → 0.72.

## Ink — dry brush
Ink · 30 px · 31.0 s

![Ink — dry brush](Ink-dry-brush.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 9 % → 7 % | 25.4 px | 0.81 | 0.78 | 146 |
| heavy line | 10 % → 8 % | 29.9 px | 0.79 | 0.75 | 242 |
| pressure swell | 7 % → 6 % | 28.1 px | 0.81 | 0.84 | 164 |
| fast wave | 21 % → 8 % | 24.3 px | 0.79 | 0.40 | 354 |
| slow wave | 17 % → 7 % | 20.2 px | 0.79 | 0.39 | 526 |
| spiral | 23 % → 8 % | 15.4 px | 0.78 | 0.34 | 573 |
| loop | 19 % → 8 % | 24.4 px | 0.78 | 0.44 | 247 |
| tilted | 8 % → 8 % | 22.7 px | 0.78 | 1.02 | 151 |
| over the wet one | 17 % → 14 % | 25.9 px | 0.78 | 0.81 | 139 |
| long, no reload | 20 % → 8 % | 9.0 px | 0.79 | 0.42 | 779 | quarters: 0.32 → 0.02 → 0.00 → 0.00

Numbers say: light vs heavy: width 25.4 → 29.9 px, dark 0.81 → 0.79.

## Ink — nib
Watercolor · 5 px · 29.4 s

![Ink — nib](Ink-nib.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 2 % → 5 % | 5.5 px | 0.89 | 2.46 | 41 |
| heavy line | 2 % → 5 % | 6.4 px | 0.89 | 2.33 | 37 |
| pressure swell | 2 % → 4 % | 6.2 px | 0.89 | 2.52 | 23 |
| fast wave | 5 % → 8 % | 6.0 px | 0.89 | 1.62 | 104 |
| slow wave | 5 % → 8 % | 5.7 px | 0.89 | 1.69 | 86 |
| spiral | 8 % → 11 % | 5.0 px | 0.88 | 1.40 | 139 |
| loop | 4 % → 8 % | 5.7 px | 0.89 | 1.73 | 84 |
| tilted | 4 % → 4 % | 10.3 px | 0.89 | 1.02 | 42 |
| over the wet one | 6 % → 9 % | 6.1 px | 0.89 | 1.61 | 35 |
| long, no reload | 10 % → 12 % | 4.3 px | 0.86 | 1.29 | 234 | quarters: 0.24 → 0.11 → 0.07 → 0.05

Numbers say: light vs heavy: width 5.5 → 6.4 px, dark 0.89 → 0.89; wet paint spreads well beyond the stroke.

## 0.45 · Dry brush
Gouache · 34 px · 31.9 s

![0.45 · Dry brush](0-45-Dry-brush.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 8 % → 2 % | 23.2 px | 0.68 | 0.30 | 132 |
| heavy line | 8 % → 3 % | 24.3 px | 0.68 | 0.32 | 168 |
| pressure swell | 7 % → 3 % | 25.6 px | 0.68 | 0.42 | 191 |
| fast wave | 14 % → 3 % | 15.7 px | 0.68 | 0.22 | 547 |
| slow wave | 16 % → 3 % | 18.7 px | 0.68 | 0.20 | 798 |
| spiral | 20 % → 3 % | 13.4 px | 0.68 | 0.15 | 984 |
| loop | 14 % → 4 % | 18.3 px | 0.68 | 0.26 | 467 |
| tilted | 7 % → 7 % | 18.9 px | 0.68 | 1.01 | 224 |
| over the wet one | 15 % → 6 % | 23.1 px | 0.68 | 0.43 | 184 |
| long, no reload | 21 % → 4 % | 9.4 px | 0.68 | 0.18 | 1099 | quarters: 0.28 → 0.14 → 0.07 → 0.03

Numbers say: light vs heavy: width 23.2 → 24.3 px, dark 0.68 → 0.68; pressure barely changes the width.

## Dry pastel
Pastel · 26 px · 14.9 s

![Dry pastel](Dry-pastel.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 3 % → 3 % | 8.3 px | 0.38 | 1.00 | 64 |
| heavy line | 5 % → 5 % | 13.2 px | 0.39 | 1.00 | 58 |
| pressure swell | 3 % → 3 % | 11.7 px | 0.38 | 1.00 | 49 |
| fast wave | 10 % → 10 % | 11.9 px | 0.39 | 1.00 | 146 |
| slow wave | 10 % → 10 % | 11.3 px | 0.39 | 1.00 | 245 |
| spiral | 15 % → 15 % | 9.6 px | 0.39 | 1.00 | 270 |
| loop | 7 % → 7 % | 9.4 px | 0.39 | 1.00 | 104 |
| tilted | 3 % → 3 % | 8.3 px | 0.38 | 1.00 | 72 |
| over the wet one | 7 % → 7 % | 11.1 px | 0.38 | 1.00 | 66 |
| long, no reload | 18 % → 18 % | 8.2 px | 0.39 | 1.00 | 355 | quarters: 0.08 → 0.08 → 0.08 → 0.07

Numbers say: light vs heavy: width 8.3 → 13.2 px, dark 0.38 → 0.39; the long stroke does not run out of paint.

## 0.45 · Charcoal
Charcoal · 18 px · 11.4 s

![0.45 · Charcoal](0-45-Charcoal.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 2 % → 2 % | 6.5 px | 0.80 | 1.00 | 25 |
| heavy line | 3 % → 3 % | 9.2 px | 0.80 | 1.00 | 36 |
| pressure swell | 2 % → 2 % | 8.8 px | 0.80 | 1.00 | 15 |
| fast wave | 7 % → 7 % | 8.5 px | 0.80 | 1.00 | 45 |
| slow wave | 7 % → 7 % | 8.0 px | 0.80 | 1.00 | 73 |
| spiral | 12 % → 12 % | 7.9 px | 0.80 | 1.00 | 81 |
| loop | 6 % → 6 % | 8.1 px | 0.80 | 1.00 | 41 |
| tilted | 3 % → 3 % | 7.5 px | 0.80 | 1.00 | 33 |
| over the wet one | 6 % → 6 % | 7.9 px | 0.80 | 1.00 | 20 |
| long, no reload | 17 % → 17 % | 7.8 px | 0.80 | 1.00 | 167 | quarters: 0.15 → 0.16 → 0.15 → 0.16

Numbers say: light vs heavy: width 6.5 → 9.2 px, dark 0.80 → 0.80; the long stroke does not run out of paint.

## Watercolour — wash
Watercolor · 50 px · 40.6 s

![Watercolour — wash](Watercolour-wash.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 16 % → 16 % | 45.5 px | 0.22 | 1.00 | 126 |
| heavy line | 22 % → 22 % | 64.9 px | 0.19 | 1.00 | 151 |
| pressure swell | 15 % → 15 % | 56.1 px | 0.22 | 1.01 | 101 |
| fast wave | 48 % → 49 % | 55.6 px | 0.19 | 1.01 | 284 |
| slow wave | 46 % → 46 % | 53.3 px | 0.24 | 1.00 | 724 |
| spiral | 66 % → 66 % | 43.7 px | 0.21 | 1.00 | 523 |
| loop | 40 % → 40 % | 51.4 px | 0.22 | 1.00 | 268 |
| tilted | 18 % → 18 % | 49.7 px | 0.23 | 1.00 | 177 |
| over the wet one | 36 % → 36 % | 49.6 px | 0.23 | 1.01 | 108 |
| long, no reload | 84 % → 84 % | 37.7 px | 0.20 | 1.00 | 780 | quarters: 0.24 → 0.20 → 0.16 → 0.12

Numbers say: light vs heavy: width 45.5 → 64.9 px, dark 0.22 → 0.19.

## Watercolour — wet-in-wet
Watercolor · 44 px · 43.1 s

![Watercolour — wet-in-wet](Watercolour-wet-in-wet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 13 % → 19 % | 38.4 px | 0.34 | 1.43 | 106 |
| heavy line | 19 % → 20 % | 54.6 px | 0.36 | 1.05 | 111 |
| pressure swell | 12 % → 15 % | 46.5 px | 0.37 | 1.22 | 93 |
| fast wave | 41 % → 45 % | 47.7 px | 0.35 | 1.09 | 257 |
| slow wave | 40 % → 45 % | 46.2 px | 0.42 | 1.12 | 444 |
| spiral | 63 % → 67 % | 41.5 px | 0.38 | 1.06 | 417 |
| loop | 34 % → 37 % | 44.4 px | 0.40 | 1.09 | 189 |
| tilted | 15 % → 16 % | 41.5 px | 0.38 | 1.06 | 158 |
| over the wet one | 31 % → 37 % | 43.9 px | 0.38 | 1.21 | 150 |
| long, no reload | 78 % → 84 % | 34.8 px | 0.37 | 1.08 | 711 | quarters: 0.39 → 0.37 → 0.32 → 0.26

Numbers say: light vs heavy: width 38.4 → 54.6 px, dark 0.34 → 0.36.

## Watercolour — glaze
Watercolor · 38 px · 39.1 s

![Watercolour — glaze](Watercolour-glaze.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 13 % → 13 % | 36.6 px | 0.07 | 1.01 | 74 |
| heavy line | 19 % → 19 % | 55.4 px | 0.07 | 1.00 | 79 |
| pressure swell | 13 % → 13 % | 47.0 px | 0.07 | 1.01 | 69 |
| fast wave | 40 % → 40 % | 45.6 px | 0.07 | 1.01 | 263 |
| slow wave | 37 % → 37 % | 42.8 px | 0.07 | 1.01 | 518 |
| spiral | 59 % → 60 % | 38.8 px | 0.06 | 1.01 | 327 |
| loop | 33 % → 33 % | 42.6 px | 0.07 | 1.00 | 181 |
| tilted | 14 % → 14 % | 40.1 px | 0.07 | 1.00 | 154 |
| over the wet one | 30 % → 30 % | 42.3 px | 0.07 | 1.01 | 105 |
| long, no reload | 69 % → 70 % | 30.9 px | 0.06 | 1.01 | 536 | quarters: 0.06 → 0.05 → 0.03 → 0.02

Numbers say: light vs heavy: width 36.6 → 55.4 px, dark 0.07 → 0.07.

## Watercolour — granulating
Watercolor · 44 px · 48.1 s

![Watercolour — granulating](Watercolour-granulating.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 14 % → 14 % | 41.4 px | 0.35 | 1.00 | 156 |
| heavy line | 21 % → 21 % | 60.4 px | 0.31 | 1.00 | 154 |
| pressure swell | 14 % → 14 % | 52.2 px | 0.34 | 1.01 | 123 |
| fast wave | 45 % → 45 % | 51.7 px | 0.29 | 1.01 | 296 |
| slow wave | 42 % → 42 % | 48.2 px | 0.35 | 1.01 | 484 |
| spiral | 62 % → 63 % | 41.0 px | 0.30 | 1.01 | 494 |
| loop | 37 % → 37 % | 47.6 px | 0.33 | 1.00 | 305 |
| tilted | 16 % → 16 % | 45.5 px | 0.35 | 1.00 | 192 |
| over the wet one | 33 % → 33 % | 46.2 px | 0.35 | 1.01 | 143 |
| long, no reload | 75 % → 76 % | 33.6 px | 0.29 | 1.01 | 842 | quarters: 0.34 → 0.26 → 0.20 → 0.14

Numbers say: light vs heavy: width 41.4 → 60.4 px, dark 0.35 → 0.31.

## Watercolour — dry brush
Watercolor · 36 px · 40.6 s

![Watercolour — dry brush](Watercolour-dry-brush.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 10 % → 10 % | 28.0 px | 0.17 | 1.01 | 130 |
| heavy line | 14 % → 13 % | 40.1 px | 0.16 | 0.93 | 189 |
| pressure swell | 11 % → 11 % | 40.5 px | 0.16 | 0.98 | 88 |
| fast wave | 27 % → 20 % | 30.8 px | 0.13 | 0.74 | 1128 |
| slow wave | 24 % → 17 % | 28.1 px | 0.14 | 0.71 | 1033 |
| spiral | 34 % → 20 % | 22.4 px | 0.13 | 0.57 | 612 |
| loop | 21 % → 18 % | 27.2 px | 0.14 | 0.86 | 319 |
| tilted | 10 % → 10 % | 28.6 px | 0.16 | 1.00 | 192 |
| over the wet one | 22 % → 20 % | 31.4 px | 0.16 | 0.95 | 161 |
| long, no reload | 36 % → 19 % | 16.1 px | 0.14 | 0.54 | 872 | quarters: 0.09 → 0.03 → 0.01 → 0.00

Numbers say: light vs heavy: width 28.0 → 40.1 px, dark 0.17 → 0.16.

## Gouache
Gouache · 30 px · 38.1 s

![Gouache](Gouache.png)

A light paint: laid on a grey sheet (on white it cannot be seen); **dark** = how far it is from the grey either way.

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 8 % → 6 % | 24.7 px | 0.28 | 0.66 | 101 |
| heavy line | 14 % → 7 % | 39.8 px | 0.28 | 0.49 | 162 |
| pressure swell | 10 % → 6 % | 38.8 px | 0.28 | 0.62 | 252 |
| fast wave | 28 % → 8 % | 32.8 px | 0.28 | 0.27 | 464 |
| slow wave | 27 % → 8 % | 31.6 px | 0.28 | 0.30 | 508 |
| spiral | 38 % → 8 % | 25.0 px | 0.28 | 0.22 | 501 |
| loop | 22 % → 8 % | 28.8 px | 0.28 | 0.36 | 289 |
| tilted | 9 % → 9 % | 24.6 px | 0.27 | 1.00 | 162 |
| over the wet one | 20 % → 13 % | 31.0 px | 0.27 | 0.67 | 119 |
| long, no reload | 40 % → 10 % | 17.9 px | 0.27 | 0.24 | 986 | quarters: 0.01 → 0.01 → 0.02 → 0.02

Numbers say: light vs heavy: width 24.7 → 39.8 px, dark 0.28 → 0.28; the long stroke does not run out of paint.

## Oil — alla prima
Oil · 30 px · 27.0 s

![Oil — alla prima](Oil-alla-prima.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 10 % → 10 % | 28.5 px | 0.51 | 1.00 | 128 |
| heavy line | 11 % → 11 % | 31.2 px | 0.51 | 1.00 | 149 |
| pressure swell | 8 % → 8 % | 30.9 px | 0.53 | 1.00 | 109 |
| fast wave | 26 % → 26 % | 29.5 px | 0.52 | 1.00 | 323 |
| slow wave | 26 % → 26 % | 30.2 px | 0.52 | 1.00 | 911 |
| spiral | 41 % → 41 % | 27.0 px | 0.51 | 1.00 | 776 |
| loop | 22 % → 22 % | 28.0 px | 0.52 | 1.00 | 245 |
| tilted | 11 % → 11 % | 31.9 px | 0.52 | 1.00 | 158 |
| over the wet one | 21 % → 21 % | 27.5 px | 0.52 | 1.00 | 132 |
| long, no reload | 50 % → 50 % | 22.5 px | 0.50 | 1.00 | 817 | quarters: 0.33 → 0.30 → 0.26 → 0.23

Numbers say: light vs heavy: width 28.5 → 31.2 px, dark 0.51 → 0.51; pressure barely changes the width.

## Oil — impasto
Oil · 34 px · 28.1 s

![Oil — impasto](Oil-impasto.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 12 % → 12 % | 34.5 px | 0.23 | 1.00 | 153 |
| heavy line | 13 % → 13 % | 37.4 px | 0.23 | 1.00 | 147 |
| pressure swell | 10 % → 10 % | 37.1 px | 0.25 | 1.00 | 121 |
| fast wave | 28 % → 28 % | 31.9 px | 0.23 | 1.00 | 547 |
| slow wave | 30 % → 30 % | 34.3 px | 0.23 | 1.00 | 818 |
| spiral | 46 % → 46 % | 30.3 px | 0.22 | 1.00 | 642 |
| loop | 25 % → 25 % | 32.2 px | 0.24 | 1.00 | 341 |
| tilted | 12 % → 12 % | 33.4 px | 0.24 | 1.00 | 224 |
| over the wet one | 24 % → 24 % | 32.6 px | 0.24 | 1.00 | 185 |
| long, no reload | 51 % → 51 % | 22.7 px | 0.22 | 1.00 | 949 | quarters: 0.17 → 0.13 → 0.10 → 0.08

Numbers say: light vs heavy: width 34.5 → 37.4 px, dark 0.23 → 0.23; pressure barely changes the width.

## Oil — glaze
Oil · 40 px · 22.7 s

![Oil — glaze](Oil-glaze.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 9 % → 9 % | 27.0 px | 0.50 | 1.00 | 125 |
| heavy line | 13 % → 13 % | 38.2 px | 0.49 | 1.00 | 187 |
| pressure swell | 10 % → 10 % | 36.6 px | 0.50 | 1.00 | 183 |
| fast wave | 29 % → 29 % | 33.5 px | 0.49 | 1.00 | 530 |
| slow wave | 30 % → 30 % | 34.5 px | 0.50 | 1.00 | 838 |
| spiral | 46 % → 46 % | 30.0 px | 0.49 | 1.00 | 592 |
| loop | 24 % → 24 % | 31.4 px | 0.50 | 1.00 | 362 |
| tilted | 11 % → 11 % | 30.3 px | 0.50 | 1.00 | 199 |
| over the wet one | 22 % → 22 % | 32.5 px | 0.50 | 1.00 | 172 |
| long, no reload | 52 % → 52 % | 23.5 px | 0.49 | 1.00 | 976 | quarters: 0.34 → 0.30 → 0.27 → 0.22

Numbers say: light vs heavy: width 27.0 → 38.2 px, dark 0.50 → 0.49.

## Oil — scumble
Oil · 36 px · 28.8 s

![Oil — scumble](Oil-scumble.png)

A light paint: laid on a grey sheet (on white it cannot be seen); **dark** = how far it is from the grey either way.

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 10 % → 10 % | 27.7 px | 0.28 | 1.00 | 189 |
| heavy line | 9 % → 9 % | 27.2 px | 0.27 | 1.00 | 192 |
| pressure swell | 9 % → 9 % | 32.2 px | 0.26 | 1.00 | 163 |
| fast wave | 18 % → 18 % | 21.0 px | 0.22 | 1.00 | 504 |
| slow wave | 22 % → 22 % | 25.5 px | 0.21 | 1.00 | 799 |
| spiral | 32 % → 32 % | 20.9 px | 0.17 | 1.00 | 1037 |
| loop | 18 % → 18 % | 23.1 px | 0.23 | 1.00 | 587 |
| tilted | 10 % → 10 % | 27.2 px | 0.25 | 1.00 | 285 |
| over the wet one | 20 % → 20 % | 27.5 px | 0.25 | 1.00 | 244 |
| long, no reload | 35 % → 35 % | 15.5 px | 0.15 | 1.00 | 1282 | quarters: 0.00 → 0.00 → 0.00 → 0.00

Numbers say: light vs heavy: width 27.7 → 27.2 px, dark 0.28 → 0.27; pressure barely changes the width.

## Acrylic — heavy body
Heavy acrylic · 30 px · 24.2 s

![Acrylic — heavy body](Acrylic-heavy-body.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 10 % → 9 % | 30.0 px | 0.51 | 0.92 | 148 |
| heavy line | 11 % → 10 % | 32.1 px | 0.51 | 0.93 | 154 |
| pressure swell | 9 % → 8 % | 31.9 px | 0.53 | 0.94 | 106 |
| fast wave | 23 % → 15 % | 27.1 px | 0.51 | 0.62 | 324 |
| slow wave | 24 % → 16 % | 28.1 px | 0.51 | 0.65 | 678 |
| spiral | 36 % → 15 % | 23.5 px | 0.51 | 0.42 | 820 |
| loop | 21 % → 16 % | 27.1 px | 0.51 | 0.76 | 425 |
| tilted | 9 % → 9 % | 26.2 px | 0.51 | 1.00 | 178 |
| over the wet one | 20 % → 18 % | 28.4 px | 0.51 | 0.90 | 156 |
| long, no reload | 39 % → 15 % | 17.4 px | 0.51 | 0.40 | 792 | quarters: 0.30 → 0.19 → 0.11 → 0.04

Numbers say: light vs heavy: width 30.0 → 32.1 px, dark 0.51 → 0.51; pressure barely changes the width.

## Acrylic — fluid
Watercolor · 36 px · 45.7 s

![Acrylic — fluid](Acrylic-fluid.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 12 % → 12 % | 34.8 px | 0.24 | 1.01 | 134 |
| heavy line | 18 % → 18 % | 52.6 px | 0.21 | 0.99 | 195 |
| pressure swell | 12 % → 12 % | 45.4 px | 0.23 | 1.00 | 144 |
| fast wave | 38 % → 38 % | 44.1 px | 0.19 | 0.98 | 314 |
| slow wave | 35 % → 35 % | 40.5 px | 0.22 | 1.00 | 477 |
| spiral | 55 % → 53 % | 36.0 px | 0.19 | 0.98 | 822 |
| loop | 31 % → 31 % | 40.2 px | 0.21 | 1.00 | 482 |
| tilted | 12 % → 12 % | 34.2 px | 0.24 | 1.00 | 183 |
| over the wet one | 27 % → 28 % | 42.3 px | 0.24 | 1.01 | 101 |
| long, no reload | 61 % → 58 % | 27.6 px | 0.19 | 0.95 | 1039 | quarters: 0.20 → 0.14 → 0.09 → 0.06

Numbers say: light vs heavy: width 34.8 → 52.6 px, dark 0.24 → 0.21.

## Acrylic — palette knife
Heavy acrylic · 42 px · 23.0 s

![Acrylic — palette knife](Acrylic-palette-knife.png)

A light paint: laid on a grey sheet (on white it cannot be seen); **dark** = how far it is from the grey either way.

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 16 % → 15 % | 45.6 px | 0.39 | 0.98 | 55 |
| heavy line | 16 % → 15 % | 45.8 px | 0.40 | 0.98 | 40 |
| pressure swell | 12 % → 12 % | 45.6 px | 0.42 | 0.99 | 29 |
| fast wave | 37 % → 20 % | 42.6 px | 0.37 | 0.55 | 92 |
| slow wave | 37 % → 21 % | 43.2 px | 0.37 | 0.57 | 196 |
| spiral | 50 % → 18 % | 32.8 px | 0.37 | 0.37 | 140 |
| loop | 32 % → 24 % | 41.2 px | 0.36 | 0.75 | 85 |
| tilted | 13 % → 13 % | 35.1 px | 0.39 | 1.00 | 66 |
| over the wet one | 27 % → 27 % | 41.3 px | 0.39 | 0.97 | 71 |
| long, no reload | 57 % → 21 % | 25.6 px | 0.35 | 0.36 | 309 | quarters: 0.00 → 0.00 → 0.00 → 0.01

Numbers say: light vs heavy: width 45.6 → 45.8 px, dark 0.39 → 0.40; pressure barely changes the width; the long stroke does not run out of paint.

## Finger on oil
Oil · 30 px · 17.2 s

![Finger on oil](Finger-on-oil.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 6 % → 6 % | 16.8 px | 0.40 | 1.00 | 85 |
| heavy line | 7 % → 7 % | 21.5 px | 0.39 | 1.00 | 77 |
| pressure swell | 6 % → 6 % | 22.3 px | 0.40 | 1.00 | 51 |
| fast wave | 12 % → 12 % | 13.6 px | 0.37 | 1.00 | 163 |
| slow wave | 17 % → 17 % | 19.5 px | 0.36 | 1.00 | 396 |
| spiral | 22 % → 22 % | 14.3 px | 0.34 | 1.00 | 440 |
| loop | 13 % → 13 % | 16.6 px | 0.37 | 1.00 | 207 |
| tilted | 8 % → 8 % | 21.4 px | 0.39 | 1.00 | 133 |
| over the wet one | 15 % → 15 % | 20.3 px | 0.39 | 1.00 | 68 |
| long, no reload | 22 % → 22 % | 10.0 px | 0.33 | 1.00 | 394 | quarters: 0.14 → 0.08 → 0.06 → 0.04

Numbers say: light vs heavy: width 16.8 → 21.5 px, dark 0.40 → 0.39.

## Palette knife — oil
Oil · 44 px · 25.4 s

![Palette knife — oil](Palette-knife-oil.png)

A light paint: laid on a grey sheet (on white it cannot be seen); **dark** = how far it is from the grey either way.

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 16 % → 16 % | 47.4 px | 0.36 | 1.00 | 68 |
| heavy line | 17 % → 17 % | 48.1 px | 0.39 | 1.00 | 38 |
| pressure swell | 13 % → 13 % | 47.5 px | 0.39 | 1.00 | 13 |
| fast wave | 39 % → 40 % | 45.6 px | 0.35 | 1.01 | 102 |
| slow wave | 40 % → 40 % | 46.1 px | 0.35 | 1.00 | 184 |
| spiral | 63 % → 63 % | 41.3 px | 0.27 | 1.00 | 200 |
| loop | 34 % → 34 % | 43.8 px | 0.36 | 1.00 | 116 |
| tilted | 14 % → 14 % | 38.3 px | 0.38 | 1.00 | 34 |
| over the wet one | 29 % → 29 % | 42.5 px | 0.38 | 1.00 | 37 |
| long, no reload | 75 % → 75 % | 33.4 px | 0.25 | 1.00 | 189 | quarters: 0.00 → 0.00 → 0.00 → 0.00

Numbers say: light vs heavy: width 47.4 → 48.1 px, dark 0.36 → 0.39; pressure barely changes the width; the long stroke does not run out of paint.

## 0.45 · Sponge
Watercolor · 46 px · 48.2 s

![0.45 · Sponge](0-45-Sponge.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 27 % → 18 % | 78.2 px | 0.09 | 0.67 | 86 |
| heavy line | 32 % → 25 % | 91.7 px | 0.09 | 0.78 | 122 |
| pressure swell | 24 % → 17 % | 90.3 px | 0.11 | 0.71 | 68 |
| fast wave | 59 % → 43 % | 68.1 px | 0.10 | 0.73 | 219 |
| slow wave | 59 % → 48 % | 68.5 px | 0.13 | 0.80 | 378 |
| spiral | 75 % → 57 % | 49.3 px | 0.12 | 0.76 | 406 |
| loop | 53 % → 43 % | 68.6 px | 0.11 | 0.81 | 212 |
| tilted | 18 % → 18 % | 49.4 px | 0.15 | 1.00 | 239 |
| over the wet one | 44 % → 37 % | 74.4 px | 0.15 | 0.84 | 140 |
| long, no reload | 89 % → 71 % | 39.9 px | 0.13 | 0.79 | 616 | quarters: 0.13 → 0.12 → 0.10 → 0.07

Numbers say: light vs heavy: width 78.2 → 91.7 px, dark 0.09 → 0.09.

## 0.45 · Eraser
Eraser · 30 px · 28.8 s · over bands of wet oil paint and oil pastel in turn (it works on paint already there: look at what it does to the bands; covered counts the bands too)

![0.45 · Eraser](0-45-Eraser.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 24 % → 24 % | 69.2 px | 0.82 | 1.00 | 62 |
| heavy line | 23 % → 23 % | 67.4 px | 0.81 | 1.00 | 80 |
| pressure swell | 23 % → 23 % | 86.7 px | 0.82 | 1.00 | 70 |
| fast wave | 21 % → 21 % | 24.7 px | 0.81 | 1.00 | 192 |
| slow wave | 20 % → 20 % | 23.5 px | 0.82 | 1.00 | 425 |
| spiral | 20 % → 20 % | 13.5 px | 0.79 | 1.00 | 407 |
| loop | 21 % → 21 % | 27.8 px | 0.80 | 1.00 | 181 |
| tilted | 23 % → 23 % | 64.8 px | 0.81 | 1.00 | 97 |
| over the wet one | 22 % → 22 % | 0.0 px | 0.81 | 1.00 | 85 |
| long, no reload | 17 % → 17 % | 7.5 px | 0.79 | 1.00 | 420 | quarters: 0.13 → 0.16 → 0.13 → 0.17

Numbers say: light vs heavy: width 69.2 → 67.4 px, dark 0.82 → 0.81; pressure barely changes the width; the long stroke does not run out of paint.

## Lift wet paint
Eraser · 30 px · 29.6 s · over bands of wet oil paint and oil pastel in turn (it works on paint already there: look at what it does to the bands; covered counts the bands too)

![Lift wet paint](Lift-wet-paint.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 24 % → 24 % | 70.1 px | 0.82 | 1.00 | 45 |
| heavy line | 24 % → 24 % | 69.8 px | 0.82 | 1.00 | 67 |
| pressure swell | 24 % → 24 % | 89.5 px | 0.82 | 1.00 | 56 |
| fast wave | 24 % → 24 % | 27.7 px | 0.82 | 1.00 | 132 |
| slow wave | 24 % → 24 % | 27.7 px | 0.82 | 1.00 | 245 |
| spiral | 24 % → 24 % | 15.9 px | 0.82 | 1.00 | 241 |
| loop | 24 % → 24 % | 31.1 px | 0.82 | 1.00 | 140 |
| tilted | 24 % → 24 % | 66.8 px | 0.82 | 1.00 | 71 |
| over the wet one | 24 % → 24 % | 0.0 px | 0.82 | 1.00 | 61 |
| long, no reload | 24 % → 24 % | 10.7 px | 0.82 | 1.00 | 988 | quarters: 0.18 → 0.24 → 0.17 → 0.24

Numbers say: light vs heavy: width 70.1 → 69.8 px, dark 0.82 → 0.82; pressure barely changes the width; the long stroke does not run out of paint.

## Sgraffito
Eraser · 10 px · 28.5 s · over bands of wet oil paint and oil pastel in turn (it works on paint already there: look at what it does to the bands; covered counts the bands too)

![Sgraffito](Sgraffito.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 24 % → 24 % | 69.5 px | 0.81 | 1.00 | 55 |
| heavy line | 24 % → 24 % | 69.5 px | 0.82 | 1.00 | 21 |
| pressure swell | 24 % → 24 % | 89.5 px | 0.82 | 1.00 | 12 |
| fast wave | 24 % → 24 % | 27.4 px | 0.82 | 1.00 | 25 |
| slow wave | 24 % → 24 % | 27.4 px | 0.81 | 1.00 | 22 |
| spiral | 24 % → 24 % | 15.7 px | 0.81 | 1.00 | 61 |
| loop | 24 % → 24 % | 30.9 px | 0.82 | 1.00 | 26 |
| tilted | 24 % → 24 % | 66.6 px | 0.82 | 1.00 | 9 |
| over the wet one | 24 % → 24 % | 0.0 px | 0.82 | 1.00 | 10 |
| long, no reload | 24 % → 24 % | 10.6 px | 0.82 | 1.00 | 63 | quarters: 0.17 → 0.24 → 0.17 → 0.24

Numbers say: light vs heavy: width 69.5 → 69.5 px, dark 0.81 → 0.82; pressure barely changes the width; the long stroke does not run out of paint.

## Brush Artist · Refs · #01 Henry Ward peach cloud
Gouache · 44 px · 49.6 s

![Brush Artist · Refs · #01 Henry Ward peach cloud](Brush-Artist-Refs-01-Henry-Ward-peach-cloud.png)

A light paint: laid on a grey sheet (on white it cannot be seen); **dark** = how far it is from the grey either way.

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 13 % → 9 % | 37.9 px | 0.33 | 0.68 | 272 |
| heavy line | 14 % → 10 % | 41.1 px | 0.33 | 0.74 | 218 |
| pressure swell | 11 % → 9 % | 41.0 px | 0.33 | 0.80 | 148 |
| fast wave | 25 % → 13 % | 29.2 px | 0.33 | 0.51 | 490 |
| slow wave | 30 % → 15 % | 34.6 px | 0.33 | 0.50 | 930 |
| spiral | 41 % → 16 % | 27.0 px | 0.33 | 0.39 | 943 |
| loop | 25 % → 16 % | 33.0 px | 0.33 | 0.61 | 490 |
| tilted | 11 % → 11 % | 31.3 px | 0.33 | 1.00 | 351 |
| over the wet one | 24 % → 20 % | 36.1 px | 0.33 | 0.85 | 279 |
| long, no reload | 44 % → 18 % | 19.8 px | 0.33 | 0.41 | 1470 | quarters: 0.01 → 0.02 → 0.02 → 0.02

Numbers say: light vs heavy: width 37.9 → 41.1 px, dark 0.33 → 0.33; pressure barely changes the width; the long stroke does not run out of paint.

## Brush Artist · Refs · #02 Henry Ward cream strokes
Gouache · 46 px · 49.9 s

![Brush Artist · Refs · #02 Henry Ward cream strokes](Brush-Artist-Refs-02-Henry-Ward-cream-strokes.png)

A light paint: laid on a grey sheet (on white it cannot be seen); **dark** = how far it is from the grey either way.

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 13 % → 10 % | 37.9 px | 0.41 | 0.73 | 216 |
| heavy line | 14 % → 12 % | 40.9 px | 0.41 | 0.82 | 263 |
| pressure swell | 11 % → 10 % | 41.1 px | 0.42 | 0.88 | 159 |
| fast wave | 25 % → 13 % | 28.7 px | 0.41 | 0.51 | 556 |
| slow wave | 29 % → 15 % | 34.0 px | 0.41 | 0.51 | 936 |
| spiral | 40 % → 16 % | 26.6 px | 0.41 | 0.40 | 1229 |
| loop | 25 % → 16 % | 32.6 px | 0.41 | 0.64 | 512 |
| tilted | 11 % → 11 % | 30.7 px | 0.41 | 1.00 | 316 |
| over the wet one | 24 % → 21 % | 36.1 px | 0.41 | 0.86 | 283 |
| long, no reload | 44 % → 19 % | 19.6 px | 0.41 | 0.43 | 1415 | quarters: 0.01 → 0.02 → 0.03 → 0.03

Numbers say: light vs heavy: width 37.9 → 40.9 px, dark 0.41 → 0.41; pressure barely changes the width; the long stroke does not run out of paint.

## Brush Artist · Refs · #03 Henry Ward navy contours
Heavy acrylic · 22 px · 30.0 s

![Brush Artist · Refs · #03 Henry Ward navy contours](Brush-Artist-Refs-03-Henry-Ward-navy-contours.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 8 % → 7 % | 22.1 px | 0.70 | 0.94 | 111 |
| heavy line | 8 % → 8 % | 24.0 px | 0.70 | 0.95 | 107 |
| pressure swell | 6 % → 6 % | 23.8 px | 0.73 | 0.94 | 105 |
| fast wave | 19 % → 12 % | 22.0 px | 0.72 | 0.65 | 337 |
| slow wave | 20 % → 13 % | 22.6 px | 0.72 | 0.68 | 502 |
| spiral | 30 % → 13 % | 19.6 px | 0.72 | 0.45 | 483 |
| loop | 17 % → 13 % | 21.5 px | 0.72 | 0.81 | 304 |
| tilted | 8 % → 8 % | 23.2 px | 0.72 | 1.00 | 165 |
| over the wet one | 16 % → 14 % | 21.8 px | 0.72 | 0.90 | 98 |
| long, no reload | 34 % → 13 % | 15.1 px | 0.72 | 0.40 | 683 | quarters: 0.35 → 0.29 → 0.19 → 0.08

Numbers say: light vs heavy: width 22.1 → 24.0 px, dark 0.70 → 0.70; pressure barely changes the width.

## Brush Artist · Refs · #04 Henry Ward grey cloud
Gouache · 50 px · 54.1 s

![Brush Artist · Refs · #04 Henry Ward grey cloud](Brush-Artist-Refs-04-Henry-Ward-grey-cloud.png)

A light paint: laid on a grey sheet (on white it cannot be seen); **dark** = how far it is from the grey either way.

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 15 % → 11 % | 43.6 px | 0.32 | 0.73 | 252 |
| heavy line | 16 % → 13 % | 46.9 px | 0.32 | 0.79 | 258 |
| pressure swell | 12 % → 10 % | 46.8 px | 0.32 | 0.84 | 157 |
| fast wave | 29 % → 15 % | 32.9 px | 0.32 | 0.52 | 666 |
| slow wave | 34 % → 17 % | 39.2 px | 0.32 | 0.51 | 1087 |
| spiral | 44 % → 18 % | 28.7 px | 0.32 | 0.42 | 1133 |
| loop | 29 % → 18 % | 37.7 px | 0.32 | 0.62 | 792 |
| tilted | 12 % → 12 % | 34.2 px | 0.32 | 1.00 | 285 |
| over the wet one | 27 % → 23 % | 41.1 px | 0.32 | 0.86 | 263 |
| long, no reload | 49 % → 21 % | 21.8 px | 0.32 | 0.44 | 2566 | quarters: 0.01 → 0.02 → 0.02 → 0.03

Numbers say: light vs heavy: width 43.6 → 46.9 px, dark 0.32 → 0.32; pressure barely changes the width; the long stroke does not run out of paint.

## Brush Artist · Refs · #05 Henry Ward green in rust loops
Heavy acrylic · 20 px · 27.6 s

![Brush Artist · Refs · #05 Henry Ward green in rust loops](Brush-Artist-Refs-05-Henry-Ward-green-in-rust-loops.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 7 % → 6 % | 19.9 px | 0.55 | 0.94 | 128 |
| heavy line | 7 % → 7 % | 21.7 px | 0.55 | 0.94 | 217 |
| pressure swell | 6 % → 5 % | 22.0 px | 0.57 | 0.92 | 152 |
| fast wave | 17 % → 11 % | 19.9 px | 0.56 | 0.64 | 354 |
| slow wave | 18 % → 12 % | 20.5 px | 0.55 | 0.66 | 385 |
| spiral | 27 % → 11 % | 17.9 px | 0.55 | 0.42 | 473 |
| loop | 15 % → 12 % | 19.5 px | 0.55 | 0.79 | 330 |
| tilted | 8 % → 8 % | 22.1 px | 0.56 | 1.00 | 250 |
| over the wet one | 15 % → 13 % | 19.7 px | 0.56 | 0.87 | 201 |
| long, no reload | 30 % → 12 % | 13.4 px | 0.56 | 0.39 | 1196 | quarters: 0.25 → 0.18 → 0.10 → 0.02

Numbers say: light vs heavy: width 19.9 → 21.7 px, dark 0.55 → 0.55; pressure barely changes the width.

## Brush Artist · Refs · #06 Henry Ward scrubbed grey
Gouache · 50 px · 53.8 s

![Brush Artist · Refs · #06 Henry Ward scrubbed grey](Brush-Artist-Refs-06-Henry-Ward-scrubbed-grey.png)

A light paint: laid on a grey sheet (on white it cannot be seen); **dark** = how far it is from the grey either way.

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 15 % → 11 % | 43.6 px | 0.34 | 0.73 | 238 |
| heavy line | 16 % → 13 % | 46.9 px | 0.34 | 0.79 | 379 |
| pressure swell | 12 % → 10 % | 46.8 px | 0.34 | 0.84 | 330 |
| fast wave | 29 % → 15 % | 32.9 px | 0.34 | 0.52 | 1045 |
| slow wave | 34 % → 17 % | 39.2 px | 0.34 | 0.51 | 971 |
| spiral | 44 % → 18 % | 28.7 px | 0.34 | 0.42 | 1399 |
| loop | 29 % → 18 % | 37.7 px | 0.34 | 0.62 | 543 |
| tilted | 12 % → 12 % | 34.2 px | 0.34 | 1.00 | 323 |
| over the wet one | 27 % → 23 % | 41.1 px | 0.34 | 0.86 | 234 |
| long, no reload | 49 % → 21 % | 21.8 px | 0.34 | 0.44 | 1499 | quarters: 0.01 → 0.02 → 0.02 → 0.03

Numbers say: light vs heavy: width 43.6 → 46.9 px, dark 0.34 → 0.34; pressure barely changes the width; the long stroke does not run out of paint.

## Brush Artist · Refs · #07 Henry Ward blue L + black zigzag
Heavy acrylic · 34 px · 23.1 s

![Brush Artist · Refs · #07 Henry Ward blue L + black zigzag](Brush-Artist-Refs-07-Henry-Ward-blue-L-black-zigzag.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 12 % → 11 % | 34.2 px | 0.58 | 0.93 | 223 |
| heavy line | 13 % → 12 % | 36.9 px | 0.58 | 0.93 | 215 |
| pressure swell | 10 % → 9 % | 36.6 px | 0.59 | 0.94 | 146 |
| fast wave | 30 % → 20 % | 34.1 px | 0.58 | 0.69 | 372 |
| slow wave | 30 % → 22 % | 34.6 px | 0.58 | 0.73 | 617 |
| spiral | 48 % → 22 % | 31.5 px | 0.58 | 0.46 | 674 |
| loop | 25 % → 21 % | 32.7 px | 0.58 | 0.82 | 343 |
| tilted | 11 % → 11 % | 31.0 px | 0.58 | 1.00 | 192 |
| over the wet one | 23 % → 21 % | 32.8 px | 0.58 | 0.91 | 135 |
| long, no reload | 53 % → 22 % | 23.9 px | 0.58 | 0.41 | 1022 | quarters: 0.40 → 0.32 → 0.21 → 0.10

Numbers say: light vs heavy: width 34.2 → 36.9 px, dark 0.58 → 0.58; pressure barely changes the width.

## Brush Artist · Refs · #08 Henry Ward olive bands
Gouache · 34 px · 32.7 s

![Brush Artist · Refs · #08 Henry Ward olive bands](Brush-Artist-Refs-08-Henry-Ward-olive-bands.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 4 % → 0 % | 12.2 px | 0.61 | 0.04 | 86 |
| heavy line | 7 % → 0 % | 19.3 px | 0.61 | 0.02 | 177 |
| pressure swell | 5 % → 0 % | 18.7 px | 0.61 | 0.03 | 147 |
| fast wave | 10 % → 0 % | 11.1 px | 0.61 | 0.02 | 382 |
| slow wave | 15 % → 1 % | 17.0 px | 0.61 | 0.06 | 573 |
| spiral | 19 % → 1 % | 12.7 px | 0.61 | 0.03 | 634 |
| loop | 12 % → 1 % | 15.3 px | 0.61 | 0.09 | 456 |
| tilted | 5 % → 5 % | 15.1 px | 0.61 | 0.96 | 254 |
| over the wet one | 11 % → 2 % | 16.9 px | 0.61 | 0.22 | 176 |
| long, no reload | 22 % → 2 % | 9.8 px | 0.61 | 0.09 | 888 | quarters: 0.21 → 0.15 → 0.11 → 0.09

Numbers say: light vs heavy: width 12.2 → 19.3 px, dark 0.61 → 0.61.

## Brush Artist · Refs · #09 Henry Ward white loops
Gouache · 46 px · 50.8 s

![Brush Artist · Refs · #09 Henry Ward white loops](Brush-Artist-Refs-09-Henry-Ward-white-loops.png)

A light paint: laid on a grey sheet (on white it cannot be seen); **dark** = how far it is from the grey either way.

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 13 % → 10 % | 37.9 px | 0.44 | 0.73 | 253 |
| heavy line | 14 % → 12 % | 40.9 px | 0.44 | 0.82 | 275 |
| pressure swell | 11 % → 10 % | 41.1 px | 0.44 | 0.88 | 197 |
| fast wave | 25 % → 13 % | 28.7 px | 0.43 | 0.51 | 654 |
| slow wave | 29 % → 15 % | 34.0 px | 0.43 | 0.51 | 873 |
| spiral | 40 % → 16 % | 26.6 px | 0.43 | 0.40 | 955 |
| loop | 25 % → 16 % | 32.6 px | 0.43 | 0.64 | 475 |
| tilted | 11 % → 11 % | 30.7 px | 0.44 | 1.00 | 258 |
| over the wet one | 24 % → 21 % | 36.1 px | 0.44 | 0.86 | 259 |
| long, no reload | 44 % → 19 % | 19.6 px | 0.43 | 0.43 | 1940 | quarters: 0.01 → 0.02 → 0.03 → 0.03

Numbers say: light vs heavy: width 37.9 → 40.9 px, dark 0.44 → 0.44; pressure barely changes the width; the long stroke does not run out of paint.

## Brush Artist · Refs · #10 Henry Ward maroon loops
Heavy acrylic · 30 px · 23.7 s

![Brush Artist · Refs · #10 Henry Ward maroon loops](Brush-Artist-Refs-10-Henry-Ward-maroon-loops.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 10 % → 9 % | 28.8 px | 0.71 | 0.95 | 127 |
| heavy line | 11 % → 10 % | 31.2 px | 0.71 | 0.95 | 131 |
| pressure swell | 8 % → 8 % | 31.1 px | 0.73 | 0.95 | 121 |
| fast wave | 25 % → 18 % | 28.7 px | 0.72 | 0.71 | 334 |
| slow wave | 25 % → 19 % | 29.4 px | 0.72 | 0.73 | 535 |
| spiral | 40 % → 19 % | 26.2 px | 0.72 | 0.47 | 638 |
| loop | 21 % → 18 % | 27.6 px | 0.72 | 0.85 | 381 |
| tilted | 10 % → 10 % | 28.7 px | 0.72 | 1.00 | 160 |
| over the wet one | 20 % → 18 % | 27.7 px | 0.72 | 0.91 | 117 |
| long, no reload | 46 % → 18 % | 20.7 px | 0.72 | 0.40 | 737 | quarters: 0.44 → 0.38 → 0.30 → 0.22

Numbers say: light vs heavy: width 28.8 → 31.2 px, dark 0.71 → 0.71; pressure barely changes the width.

## Brush Artist · Refs · #11 Henry Ward purple spun balls
Heavy acrylic · 36 px · 25.6 s

![Brush Artist · Refs · #11 Henry Ward purple spun balls](Brush-Artist-Refs-11-Henry-Ward-purple-spun-balls.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 12 % → 12 % | 35.3 px | 0.71 | 0.96 | 290 |
| heavy line | 13 % → 12 % | 37.9 px | 0.71 | 0.96 | 257 |
| pressure swell | 10 % → 10 % | 37.7 px | 0.74 | 0.96 | 339 |
| fast wave | 30 % → 23 % | 35.1 px | 0.73 | 0.75 | 905 |
| slow wave | 31 % → 24 % | 35.5 px | 0.73 | 0.79 | 729 |
| spiral | 49 % → 25 % | 32.6 px | 0.73 | 0.50 | 626 |
| loop | 26 % → 23 % | 33.4 px | 0.73 | 0.88 | 347 |
| tilted | 12 % → 12 % | 32.4 px | 0.73 | 1.00 | 190 |
| over the wet one | 24 % → 22 % | 33.5 px | 0.73 | 0.93 | 169 |
| long, no reload | 56 % → 24 % | 24.9 px | 0.73 | 0.44 | 950 | quarters: 0.51 → 0.46 → 0.39 → 0.29

Numbers say: light vs heavy: width 35.3 → 37.9 px, dark 0.71 → 0.71; pressure barely changes the width.

## Brush Artist · Refs · #12 Henry Ward black-olive cage
Gouache · 28 px · 30.5 s

![Brush Artist · Refs · #12 Henry Ward black-olive cage](Brush-Artist-Refs-12-Henry-Ward-black-olive-cage.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 3 % → 0 % | 10.1 px | 0.65 | 0.08 | 137 |
| heavy line | 5 % → 0 % | 15.3 px | 0.65 | 0.08 | 184 |
| pressure swell | 4 % → 0 % | 14.9 px | 0.65 | 0.10 | 96 |
| fast wave | 8 % → 0 % | 8.9 px | 0.65 | 0.04 | 270 |
| slow wave | 12 % → 1 % | 13.6 px | 0.65 | 0.09 | 513 |
| spiral | 16 % → 1 % | 10.4 px | 0.65 | 0.04 | 444 |
| loop | 9 % → 2 % | 12.3 px | 0.65 | 0.17 | 237 |
| tilted | 5 % → 4 % | 13.0 px | 0.65 | 0.95 | 131 |
| over the wet one | 9 % → 3 % | 13.2 px | 0.65 | 0.27 | 142 |
| long, no reload | 18 % → 2 % | 8.3 px | 0.65 | 0.12 | 916 | quarters: 0.19 → 0.14 → 0.11 → 0.10

Numbers say: light vs heavy: width 10.1 → 15.3 px, dark 0.65 → 0.65.

## Brush Artist · Refs · #13 Henry Ward blue streaky form
Gouache · 50 px · 54.1 s

![Brush Artist · Refs · #13 Henry Ward blue streaky form](Brush-Artist-Refs-13-Henry-Ward-blue-streaky-form.png)

A light paint: laid on a grey sheet (on white it cannot be seen); **dark** = how far it is from the grey either way.

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 15 % → 11 % | 43.6 px | 0.34 | 0.73 | 202 |
| heavy line | 16 % → 13 % | 46.9 px | 0.34 | 0.79 | 235 |
| pressure swell | 12 % → 10 % | 46.8 px | 0.34 | 0.84 | 176 |
| fast wave | 29 % → 15 % | 32.9 px | 0.34 | 0.52 | 782 |
| slow wave | 34 % → 17 % | 39.2 px | 0.34 | 0.51 | 999 |
| spiral | 44 % → 18 % | 28.7 px | 0.34 | 0.42 | 980 |
| loop | 29 % → 18 % | 37.7 px | 0.34 | 0.62 | 537 |
| tilted | 12 % → 12 % | 34.2 px | 0.34 | 1.00 | 264 |
| over the wet one | 27 % → 23 % | 41.1 px | 0.34 | 0.86 | 248 |
| long, no reload | 49 % → 21 % | 21.8 px | 0.33 | 0.44 | 2046 | quarters: 0.01 → 0.02 → 0.02 → 0.03

Numbers say: light vs heavy: width 43.6 → 46.9 px, dark 0.34 → 0.34; pressure barely changes the width; the long stroke does not run out of paint.

## Brush Artist · Refs · #14 Henry Ward olive totem
Heavy acrylic · 48 px · 25.8 s

![Brush Artist · Refs · #14 Henry Ward olive totem](Brush-Artist-Refs-14-Henry-Ward-olive-totem.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 16 % → 15 % | 46.8 px | 0.31 | 0.95 | 192 |
| heavy line | 17 % → 16 % | 49.8 px | 0.31 | 0.95 | 223 |
| pressure swell | 13 % → 13 % | 49.6 px | 0.32 | 0.96 | 144 |
| fast wave | 39 % → 31 % | 44.9 px | 0.30 | 0.79 | 693 |
| slow wave | 39 % → 32 % | 45.4 px | 0.30 | 0.81 | 1115 |
| spiral | 59 % → 32 % | 38.7 px | 0.30 | 0.55 | 847 |
| loop | 33 % → 29 % | 42.7 px | 0.30 | 0.89 | 446 |
| tilted | 14 % → 14 % | 39.5 px | 0.31 | 1.00 | 262 |
| over the wet one | 30 % → 28 % | 43.3 px | 0.31 | 0.94 | 208 |
| long, no reload | 68 % → 33 % | 30.6 px | 0.30 | 0.48 | 1400 | quarters: 0.25 → 0.18 → 0.09 → 0.04

Numbers say: light vs heavy: width 46.8 → 49.8 px, dark 0.31 → 0.31; pressure barely changes the width.

## Brush Artist · Refs · #15 Ultramarine brush script
Ink · 4 px · 31.6 s

![Brush Artist · Refs · #15 Ultramarine brush script](Brush-Artist-Refs-15-Ultramarine-brush-script.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 1 % → 3 % | 2.2 px | 0.55 | 3.90 | 29 |
| heavy line | 6 % → 6 % | 16.7 px | 0.58 | 0.99 | 65 |
| pressure swell | 3 % → 4 % | 12.1 px | 0.64 | 1.15 | 38 |
| fast wave | 9 % → 7 % | 10.6 px | 0.54 | 0.81 | 125 |
| slow wave | 7 % → 7 % | 8.4 px | 0.54 | 0.93 | 118 |
| spiral | 11 % → 7 % | 7.2 px | 0.52 | 0.66 | 207 |
| loop | 7 % → 7 % | 9.2 px | 0.53 | 0.98 | 189 |
| tilted | 3 % → 3 % | 8.2 px | 0.62 | 1.02 | 69 |
| over the wet one | 7 % → 7 % | 11.5 px | 0.62 | 1.05 | 69 |
| long, no reload | 16 % → 8 % | 7.3 px | 0.50 | 0.48 | 311 | quarters: 0.15 → 0.04 → 0.01 → 0.00

Numbers say: light vs heavy: width 2.2 → 16.7 px, dark 0.55 → 0.58; wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #18 Blue oil-stick scribbles
Pastel · 10 px · 15.7 s

![Brush Artist · Refs · #18 Blue oil-stick scribbles](Brush-Artist-Refs-18-Blue-oil-stick-scribbles.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 1 % → 1 % | 2.9 px | 0.52 | 1.00 | 49 |
| heavy line | 2 % → 2 % | 5.5 px | 0.53 | 1.00 | 40 |
| pressure swell | 1 % → 1 % | 5.0 px | 0.53 | 1.00 | 24 |
| fast wave | 4 % → 4 % | 4.8 px | 0.53 | 1.00 | 104 |
| slow wave | 4 % → 4 % | 4.4 px | 0.53 | 1.00 | 165 |
| spiral | 7 % → 7 % | 4.5 px | 0.52 | 1.00 | 262 |
| loop | 3 % → 3 % | 4.5 px | 0.52 | 1.00 | 115 |
| tilted | 2 % → 2 % | 4.7 px | 0.53 | 1.00 | 64 |
| over the wet one | 3 % → 3 % | 4.7 px | 0.53 | 1.00 | 41 |
| long, no reload | 10 % → 10 % | 4.4 px | 0.53 | 1.00 | 257 | quarters: 0.06 → 0.06 → 0.06 → 0.06

Numbers say: light vs heavy: width 2.9 → 5.5 px, dark 0.52 → 0.53; the long stroke does not run out of paint.

## Brush Artist · Refs · #20 Orange-red crayon scribble
Pastel · 14 px · 17.8 s

![Brush Artist · Refs · #20 Orange-red crayon scribble](Brush-Artist-Refs-20-Orange-red-crayon-scribble.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 1 % → 1 % | 4.0 px | 0.53 | 1.00 | 31 |
| heavy line | 3 % → 3 % | 8.0 px | 0.53 | 1.00 | 55 |
| pressure swell | 2 % → 2 % | 7.6 px | 0.53 | 1.00 | 35 |
| fast wave | 6 % → 6 % | 7.2 px | 0.53 | 1.00 | 146 |
| slow wave | 6 % → 6 % | 6.6 px | 0.53 | 1.00 | 150 |
| spiral | 9 % → 9 % | 6.2 px | 0.53 | 1.00 | 194 |
| loop | 5 % → 5 % | 6.2 px | 0.53 | 1.00 | 154 |
| tilted | 2 % → 2 % | 5.6 px | 0.53 | 1.00 | 90 |
| over the wet one | 4 % → 4 % | 6.6 px | 0.53 | 1.00 | 97 |
| long, no reload | 13 % → 13 % | 5.7 px | 0.53 | 1.00 | 485 | quarters: 0.07 → 0.07 → 0.08 → 0.08

Numbers say: light vs heavy: width 4.0 → 8.0 px, dark 0.53 → 0.53; the long stroke does not run out of paint.

## Brush Artist · Refs · #21 Gritty black contours
Gouache · 12 px · 32.2 s

![Brush Artist · Refs · #21 Gritty black contours](Brush-Artist-Refs-21-Gritty-black-contours.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 1 % → 0 % | 3.3 px | 0.81 | 0.08 | 132 |
| heavy line | 2 % → 0 % | 5.2 px | 0.81 | 0.03 | 214 |
| pressure swell | 1 % → 0 % | 5.4 px | 0.81 | 0.04 | 162 |
| fast wave | 2 % → 0 % | 2.7 px | 0.81 | 0.01 | 525 |
| slow wave | 4 % → 0 % | 4.4 px | 0.81 | 0.04 | 534 |
| spiral | 5 % → 0 % | 3.1 px | 0.81 | 0.02 | 524 |
| loop | 3 % → 0 % | 4.1 px | 0.81 | 0.02 | 265 |
| tilted | 2 % → 2 % | 4.8 px | 0.81 | 0.93 | 146 |
| over the wet one | 3 % → 0 % | 4.7 px | 0.81 | 0.11 | 206 |
| long, no reload | 6 % → 0 % | 2.7 px | 0.81 | 0.06 | 1003 | quarters: 0.09 → 0.06 → 0.05 → 0.04

Numbers say: light vs heavy: width 3.3 → 5.2 px, dark 0.81 → 0.81.

## Brush Artist · Refs · #22 Bold black brush poster
Ink · 20 px · 37.9 s

![Brush Artist · Refs · #22 Bold black brush poster](Brush-Artist-Refs-22-Bold-black-brush-poster.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 3 % → 5 % | 9.6 px | 0.79 | 1.64 | 56 |
| heavy line | 15 % → 15 % | 44.6 px | 0.88 | 0.99 | 136 |
| pressure swell | 9 % → 9 % | 31.9 px | 0.87 | 1.04 | 101 |
| fast wave | 27 % → 27 % | 31.7 px | 0.87 | 0.98 | 297 |
| slow wave | 22 % → 22 % | 25.4 px | 0.87 | 0.98 | 340 |
| spiral | 34 % → 32 % | 22.4 px | 0.87 | 0.94 | 397 |
| loop | 20 % → 20 % | 26.4 px | 0.88 | 1.00 | 164 |
| tilted | 8 % → 8 % | 23.1 px | 0.88 | 1.01 | 109 |
| over the wet one | 19 % → 19 % | 30.4 px | 0.88 | 1.00 | 92 |
| long, no reload | 45 % → 38 % | 20.3 px | 0.86 | 0.83 | 510 | quarters: 0.54 → 0.45 → 0.35 → 0.26

Numbers say: light vs heavy: width 9.6 → 44.6 px, dark 0.79 → 0.88; wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #23 Dry white on orange + black line
Gouache · 50 px · 33.0 s

![Brush Artist · Refs · #23 Dry white on orange + black line](Brush-Artist-Refs-23-Dry-white-on-orange-black-line.png)

A light paint: laid on a grey sheet (on white it cannot be seen); **dark** = how far it is from the grey either way.

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 5 % → 0 % | 15.7 px | 0.42 | 0.02 | 139 |
| heavy line | 9 % → 0 % | 25.3 px | 0.42 | 0.00 | 288 |
| pressure swell | 6 % → 0 % | 23.8 px | 0.41 | 0.00 | 158 |
| fast wave | 12 % → 0 % | 13.7 px | 0.41 | 0.01 | 504 |
| slow wave | 19 % → 0 % | 21.6 px | 0.41 | 0.02 | 940 |
| spiral | 24 % → 0 % | 15.6 px | 0.40 | 0.01 | 856 |
| loop | 15 % → 1 % | 19.8 px | 0.40 | 0.04 | 557 |
| tilted | 6 % → 6 % | 17.5 px | 0.40 | 0.94 | 343 |
| over the wet one | 14 % → 1 % | 20.6 px | 0.40 | 0.09 | 256 |
| long, no reload | 27 % → 1 % | 12.3 px | 0.40 | 0.05 | 1257 | quarters: 0.02 → 0.03 → 0.03 → 0.03

Numbers say: light vs heavy: width 15.7 → 25.3 px, dark 0.42 → 0.42; the long stroke does not run out of paint.

## Brush Artist · Refs · #24 Picasso flat oil
Oil · 34 px · 28.0 s

![Brush Artist · Refs · #24 Picasso flat oil](Brush-Artist-Refs-24-Picasso-flat-oil.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 11 % → 12 % | 33.4 px | 0.40 | 1.00 | 150 |
| heavy line | 12 % → 13 % | 36.2 px | 0.40 | 1.00 | 180 |
| pressure swell | 10 % → 10 % | 35.8 px | 0.41 | 1.00 | 113 |
| fast wave | 30 % → 30 % | 34.6 px | 0.41 | 1.00 | 460 |
| slow wave | 31 % → 31 % | 35.4 px | 0.40 | 1.00 | 772 |
| spiral | 52 % → 52 % | 34.0 px | 0.40 | 1.00 | 881 |
| loop | 25 % → 25 % | 32.7 px | 0.41 | 1.00 | 598 |
| tilted | 12 % → 12 % | 33.0 px | 0.40 | 1.00 | 297 |
| over the wet one | 23 % → 23 % | 31.9 px | 0.40 | 1.00 | 207 |
| long, no reload | 62 % → 62 % | 27.7 px | 0.39 | 1.00 | 1098 | quarters: 0.28 → 0.27 → 0.26 → 0.24

Numbers say: light vs heavy: width 33.4 → 36.2 px, dark 0.40 → 0.40; pressure barely changes the width; the long stroke does not run out of paint.

## Brush Artist · Refs · #25 Yellow heavy flat stroke
Heavy acrylic · 110 px · 53.1 s

![Brush Artist · Refs · #25 Yellow heavy flat stroke](Brush-Artist-Refs-25-Yellow-heavy-flat-stroke.png)

A light paint: laid on a grey sheet (on white it cannot be seen); **dark** = how far it is from the grey either way.

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 38 % → 39 % | 109.9 px | 0.30 | 1.02 | 495 |
| heavy line | 39 % → 39 % | 114.6 px | 0.30 | 0.98 | 523 |
| pressure swell | 31 % → 32 % | 115.0 px | 0.30 | 1.05 | 420 |
| fast wave | 75 % → 78 % | 86.6 px | 0.30 | 1.04 | 1816 |
| slow wave | 76 % → 74 % | 87.5 px | 0.30 | 0.98 | 2656 |
| spiral | 87 % → 83 % | 57.1 px | 0.29 | 0.96 | 2478 |
| loop | 65 % → 64 % | 83.7 px | 0.30 | 0.99 | 1455 |
| tilted | 29 % → 29 % | 81.2 px | 0.30 | 1.00 | 843 |
| over the wet one | 62 % → 61 % | 91.1 px | 0.30 | 0.98 | 882 |
| long, no reload | 100 % → 99 % | 44.7 px | 0.29 | 0.99 | 4056 | quarters: 0.00 → 0.00 → 0.00 → 0.00

Numbers say: light vs heavy: width 109.9 → 114.6 px, dark 0.30 → 0.30; pressure barely changes the width.

## Brush Artist · Refs · #27 Orange impasto swatch
Heavy acrylic · 60 px · 41.0 s

![Brush Artist · Refs · #27 Orange impasto swatch](Brush-Artist-Refs-27-Orange-impasto-swatch.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 21 % → 21 % | 59.7 px | 0.35 | 1.00 | 251 |
| heavy line | 22 % → 22 % | 62.5 px | 0.35 | 1.00 | 301 |
| pressure swell | 17 % → 17 % | 63.2 px | 0.36 | 1.01 | 245 |
| fast wave | 49 % → 48 % | 56.3 px | 0.35 | 0.98 | 863 |
| slow wave | 49 % → 48 % | 57.1 px | 0.35 | 0.98 | 1156 |
| spiral | 70 % → 63 % | 46.1 px | 0.34 | 0.91 | 1088 |
| loop | 42 % → 40 % | 53.9 px | 0.35 | 0.97 | 558 |
| tilted | 17 % → 17 % | 46.9 px | 0.35 | 1.00 | 322 |
| over the wet one | 36 % → 36 % | 53.9 px | 0.35 | 1.00 | 261 |
| long, no reload | 86 % → 76 % | 38.6 px | 0.35 | 0.88 | 1829 | quarters: 0.33 → 0.31 → 0.29 → 0.27

Numbers say: light vs heavy: width 59.7 → 62.5 px, dark 0.35 → 0.35; pressure barely changes the width.

## Brush Artist · Refs · #28 Miles Davis black lines
Ink · 22 px · 41.9 s

![Brush Artist · Refs · #28 Miles Davis black lines](Brush-Artist-Refs-28-Miles-Davis-black-lines.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 4 % → 6 % | 12.3 px | 0.81 | 1.49 | 52 |
| heavy line | 17 % → 17 % | 49.0 px | 0.88 | 0.99 | 129 |
| pressure swell | 10 % → 10 % | 35.9 px | 0.87 | 1.03 | 95 |
| fast wave | 31 % → 30 % | 35.5 px | 0.87 | 0.98 | 259 |
| slow wave | 25 % → 25 % | 28.7 px | 0.87 | 0.99 | 364 |
| spiral | 39 % → 37 % | 25.5 px | 0.87 | 0.95 | 525 |
| loop | 23 % → 23 % | 29.6 px | 0.88 | 1.00 | 247 |
| tilted | 9 % → 9 % | 25.3 px | 0.88 | 1.01 | 104 |
| over the wet one | 21 % → 21 % | 34.1 px | 0.88 | 1.00 | 75 |
| long, no reload | 51 % → 43 % | 22.9 px | 0.86 | 0.84 | 591 | quarters: 0.59 → 0.51 → 0.40 → 0.31

Numbers say: light vs heavy: width 12.3 → 49.0 px, dark 0.81 → 0.88.

## Brush Artist · Refs · #29 Shrigley magenta asterisk
Watercolor · 70 px · 47.0 s

![Brush Artist · Refs · #29 Shrigley magenta asterisk](Brush-Artist-Refs-29-Shrigley-magenta-asterisk.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 10 % → 13 % | 28.0 px | 0.65 | 1.36 | 112 |
| heavy line | 17 % → 18 % | 50.3 px | 0.64 | 1.03 | 309 |
| pressure swell | 11 % → 12 % | 41.1 px | 0.65 | 1.13 | 131 |
| fast wave | 38 % → 38 % | 43.8 px | 0.64 | 1.01 | 380 |
| slow wave | 35 % → 39 % | 41.0 px | 0.65 | 1.10 | 673 |
| spiral | 61 % → 61 % | 40.0 px | 0.64 | 1.01 | 702 |
| loop | 31 % → 32 % | 40.2 px | 0.65 | 1.03 | 320 |
| tilted | 18 % → 18 % | 49.0 px | 0.65 | 1.00 | 298 |
| over the wet one | 31 % → 34 % | 38.4 px | 0.65 | 1.07 | 149 |
| long, no reload | 75 % → 75 % | 33.6 px | 0.64 | 1.00 | 1016 | quarters: 0.55 → 0.53 → 0.52 → 0.49

Numbers say: light vs heavy: width 28.0 → 50.3 px, dark 0.65 → 0.64; the long stroke does not run out of paint.

## Brush Artist · Refs · #30 Red gouache face patch
Gouache · 60 px · 57.7 s

![Brush Artist · Refs · #30 Red gouache face patch](Brush-Artist-Refs-30-Red-gouache-face-patch.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 16 % → 15 % | 47.0 px | 0.49 | 0.91 | 228 |
| heavy line | 25 % → 20 % | 74.0 px | 0.49 | 0.80 | 334 |
| pressure swell | 19 % → 17 % | 72.7 px | 0.49 | 0.86 | 280 |
| fast wave | 49 % → 28 % | 56.2 px | 0.49 | 0.58 | 621 |
| slow wave | 48 % → 28 % | 55.4 px | 0.49 | 0.59 | 1147 |
| spiral | 60 % → 28 % | 39.4 px | 0.49 | 0.47 | 1124 |
| loop | 40 % → 29 % | 51.6 px | 0.49 | 0.74 | 536 |
| tilted | 16 % → 17 % | 46.0 px | 0.49 | 1.00 | 366 |
| over the wet one | 36 % → 32 % | 55.3 px | 0.49 | 0.89 | 344 |
| long, no reload | 67 % → 30 % | 30.1 px | 0.49 | 0.44 | 1611 | quarters: 0.43 → 0.39 → 0.32 → 0.26

Numbers say: light vs heavy: width 47.0 → 74.0 px, dark 0.49 → 0.49.

## Brush Artist · Refs · #31 Warhol blotted line
Ink · 6 px · 30.8 s

![Brush Artist · Refs · #31 Warhol blotted line](Brush-Artist-Refs-31-Warhol-blotted-line.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 1 % → 3 % | 2.7 px | 0.75 | 3.30 | 58 |
| heavy line | 7 % → 7 % | 20.7 px | 0.83 | 0.98 | 87 |
| pressure swell | 4 % → 4 % | 14.8 px | 0.84 | 1.12 | 70 |
| fast wave | 12 % → 9 % | 13.9 px | 0.82 | 0.76 | 225 |
| slow wave | 10 % → 8 % | 11.2 px | 0.80 | 0.84 | 283 |
| spiral | 15 % → 8 % | 9.7 px | 0.80 | 0.57 | 295 |
| loop | 9 % → 9 % | 11.9 px | 0.80 | 0.93 | 137 |
| tilted | 3 % → 3 % | 8.8 px | 0.84 | 1.03 | 73 |
| over the wet one | 8 % → 8 % | 14.4 px | 0.84 | 1.02 | 69 |
| long, no reload | 21 % → 9 % | 9.6 px | 0.78 | 0.43 | 427 | quarters: 0.25 → 0.13 → 0.05 → 0.01

Numbers say: light vs heavy: width 2.7 → 20.7 px, dark 0.75 → 0.83; wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #32 Thick orange swipes
Heavy acrylic · 90 px · 53.5 s

![Brush Artist · Refs · #32 Thick orange swipes](Brush-Artist-Refs-32-Thick-orange-swipes.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 31 % → 32 % | 89.3 px | 0.38 | 1.03 | 471 |
| heavy line | 32 % → 31 % | 92.9 px | 0.38 | 0.98 | 506 |
| pressure swell | 25 % → 26 % | 93.5 px | 0.39 | 1.04 | 341 |
| fast wave | 65 % → 67 % | 75.6 px | 0.38 | 1.02 | 1296 |
| slow wave | 66 % → 65 % | 76.0 px | 0.38 | 0.98 | 2183 |
| spiral | 80 % → 78 % | 52.8 px | 0.38 | 0.98 | 2826 |
| loop | 57 % → 56 % | 73.4 px | 0.38 | 0.99 | 2194 |
| tilted | 24 % → 24 % | 66.2 px | 0.38 | 1.00 | 558 |
| over the wet one | 51 % → 51 % | 77.2 px | 0.38 | 0.99 | 482 |
| long, no reload | 97 % → 95 % | 43.4 px | 0.38 | 0.98 | 2820 | quarters: 0.38 → 0.38 → 0.37 → 0.37

Numbers say: light vs heavy: width 89.3 → 92.9 px, dark 0.38 → 0.38; pressure barely changes the width; the long stroke does not run out of paint.

## Brush Artist · Refs · #33 Red wet-in-wet band
Watercolor · 80 px · 76.2 s

![Brush Artist · Refs · #33 Red wet-in-wet band](Brush-Artist-Refs-33-Red-wet-in-wet-band.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 19 % → 31 % | 55.6 px | 0.58 | 1.61 | 187 |
| heavy line | 29 % → 39 % | 83.7 px | 0.59 | 1.35 | 362 |
| pressure swell | 19 % → 27 % | 71.5 px | 0.61 | 1.42 | 202 |
| fast wave | 58 % → 74 % | 67.5 px | 0.61 | 1.27 | 566 |
| slow wave | 57 % → 72 % | 65.7 px | 0.63 | 1.26 | 3087 |
| spiral | 75 % → 84 % | 49.6 px | 0.64 | 1.12 | 1133 |
| loop | 51 % → 63 % | 66.4 px | 0.63 | 1.22 | 515 |
| tilted | 24 % → 25 % | 66.3 px | 0.60 | 1.03 | 352 |
| over the wet one | 48 % → 67 % | 66.7 px | 0.60 | 1.40 | 285 |
| long, no reload | 95 % → 99 % | 42.6 px | 0.66 | 1.04 | 1738 | quarters: 0.68 → 0.68 → 0.68 → 0.64

Numbers say: light vs heavy: width 55.6 → 83.7 px, dark 0.58 → 0.59; the long stroke does not run out of paint; wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #34 Magenta oil patches
Oil · 60 px · 35.1 s

![Brush Artist · Refs · #34 Magenta oil patches](Brush-Artist-Refs-34-Magenta-oil-patches.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 20 % → 20 % | 58.8 px | 0.61 | 1.01 | 323 |
| heavy line | 22 % → 22 % | 63.1 px | 0.61 | 1.00 | 295 |
| pressure swell | 17 % → 17 % | 62.7 px | 0.62 | 1.01 | 246 |
| fast wave | 49 % → 50 % | 56.7 px | 0.62 | 1.02 | 806 |
| slow wave | 49 % → 49 % | 57.1 px | 0.62 | 1.00 | 1442 |
| spiral | 71 % → 71 % | 46.9 px | 0.61 | 1.00 | 1476 |
| loop | 42 % → 42 % | 54.3 px | 0.62 | 1.00 | 727 |
| tilted | 18 % → 18 % | 49.8 px | 0.61 | 1.00 | 613 |
| over the wet one | 37 % → 37 % | 53.2 px | 0.61 | 1.00 | 520 |
| long, no reload | 88 % → 88 % | 39.2 px | 0.62 | 1.00 | 2393 | quarters: 0.59 → 0.58 → 0.56 → 0.54

Numbers say: light vs heavy: width 58.8 → 63.1 px, dark 0.61 → 0.61; pressure barely changes the width; the long stroke does not run out of paint.

## Brush Artist · Refs · #35 Red band with runs
Watercolor · 70 px · 71.2 s

![Brush Artist · Refs · #35 Red band with runs](Brush-Artist-Refs-35-Red-band-with-runs.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 17 % → 35 % | 48.3 px | 0.47 | 2.10 | 176 |
| heavy line | 25 % → 43 % | 73.9 px | 0.48 | 1.70 | 317 |
| pressure swell | 17 % → 25 % | 63.0 px | 0.53 | 1.50 | 213 |
| fast wave | 54 % → 73 % | 61.9 px | 0.51 | 1.37 | 731 |
| slow wave | 52 % → 72 % | 59.8 px | 0.54 | 1.38 | 1069 |
| spiral | 72 % → 90 % | 47.4 px | 0.55 | 1.25 | 1162 |
| loop | 47 % → 75 % | 61.4 px | 0.50 | 1.59 | 499 |
| tilted | 21 % → 22 % | 58.1 px | 0.49 | 1.06 | 337 |
| over the wet one | 43 % → 73 % | 62.1 px | 0.49 | 1.69 | 249 |
| long, no reload | 92 % → 98 % | 41.5 px | 0.58 | 1.06 | 1610 | quarters: 0.60 → 0.60 → 0.59 → 0.57

Numbers say: light vs heavy: width 48.3 → 73.9 px, dark 0.47 → 0.48; the long stroke does not run out of paint; wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #36 Magenta letters flat brush
Gouache · 36 px · 48.3 s

![Brush Artist · Refs · #36 Magenta letters flat brush](Brush-Artist-Refs-36-Magenta-letters-flat-brush.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 10 % → 10 % | 29.1 px | 0.45 | 0.98 | 110 |
| heavy line | 17 % → 14 % | 49.1 px | 0.45 | 0.85 | 217 |
| pressure swell | 13 % → 12 % | 49.4 px | 0.45 | 0.89 | 168 |
| fast wave | 35 % → 19 % | 41.0 px | 0.45 | 0.54 | 317 |
| slow wave | 35 % → 19 % | 40.0 px | 0.45 | 0.54 | 536 |
| spiral | 46 % → 19 % | 30.5 px | 0.45 | 0.42 | 596 |
| loop | 27 % → 20 % | 35.4 px | 0.45 | 0.72 | 293 |
| tilted | 11 % → 11 % | 30.0 px | 0.45 | 1.00 | 174 |
| over the wet one | 24 % → 23 % | 38.1 px | 0.45 | 0.92 | 153 |
| long, no reload | 47 % → 19 % | 20.9 px | 0.45 | 0.40 | 1023 | quarters: 0.29 → 0.26 → 0.22 → 0.18

Numbers say: light vs heavy: width 29.1 → 49.1 px, dark 0.45 → 0.45.

## Brush Artist · Refs · #37 Oil still life dabs
Oil · 40 px · 31.1 s

![Brush Artist · Refs · #37 Oil still life dabs](Brush-Artist-Refs-37-Oil-still-life-dabs.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 14 % → 14 % | 39.4 px | 0.39 | 1.00 | 175 |
| heavy line | 15 % → 15 % | 42.6 px | 0.39 | 1.00 | 228 |
| pressure swell | 11 % → 11 % | 42.0 px | 0.40 | 1.00 | 192 |
| fast wave | 35 % → 35 % | 40.4 px | 0.39 | 1.00 | 837 |
| slow wave | 35 % → 35 % | 40.8 px | 0.39 | 1.00 | 1576 |
| spiral | 59 % → 59 % | 39.1 px | 0.38 | 1.00 | 1105 |
| loop | 29 % → 29 % | 37.8 px | 0.39 | 1.00 | 582 |
| tilted | 13 % → 14 % | 37.6 px | 0.39 | 1.00 | 257 |
| over the wet one | 27 % → 27 % | 37.3 px | 0.39 | 1.00 | 271 |
| long, no reload | 69 % → 69 % | 31.1 px | 0.37 | 1.00 | 1344 | quarters: 0.31 → 0.30 → 0.28 → 0.25

Numbers say: light vs heavy: width 39.4 → 42.6 px, dark 0.39 → 0.39; pressure barely changes the width.

## Brush Artist · Refs · #38 Sanguine drawing
Pastel · 6 px · 13.2 s

![Brush Artist · Refs · #38 Sanguine drawing](Brush-Artist-Refs-38-Sanguine-drawing.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 1 % → 1 % | 2.0 px | 0.61 | 1.00 | 26 |
| heavy line | 1 % → 1 % | 3.5 px | 0.62 | 1.00 | 21 |
| pressure swell | 1 % → 1 % | 3.3 px | 0.62 | 1.00 | 13 |
| fast wave | 3 % → 3 % | 3.2 px | 0.61 | 1.00 | 77 |
| slow wave | 3 % → 3 % | 3.0 px | 0.61 | 1.00 | 65 |
| spiral | 4 % → 4 % | 2.9 px | 0.61 | 1.00 | 113 |
| loop | 2 % → 2 % | 3.0 px | 0.61 | 1.00 | 54 |
| tilted | 1 % → 1 % | 3.4 px | 0.62 | 1.00 | 29 |
| over the wet one | 2 % → 2 % | 2.9 px | 0.62 | 1.00 | 29 |
| long, no reload | 7 % → 7 % | 3.0 px | 0.61 | 1.00 | 173 | quarters: 0.04 → 0.05 → 0.05 → 0.05

Numbers say: light vs heavy: width 2.0 → 3.5 px, dark 0.61 → 0.62; the long stroke does not run out of paint.

## Brush Artist · Refs · #39 Very thick impasto
Heavy acrylic · 60 px · 40.5 s

![Brush Artist · Refs · #39 Very thick impasto](Brush-Artist-Refs-39-Very-thick-impasto.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 21 % → 21 % | 59.8 px | 0.61 | 1.02 | 291 |
| heavy line | 22 % → 22 % | 62.6 px | 0.61 | 1.02 | 256 |
| pressure swell | 17 % → 17 % | 63.3 px | 0.63 | 1.03 | 195 |
| fast wave | 49 % → 48 % | 56.4 px | 0.62 | 0.99 | 899 |
| slow wave | 50 % → 49 % | 57.3 px | 0.62 | 0.98 | 1196 |
| spiral | 70 % → 66 % | 46.3 px | 0.62 | 0.94 | 1254 |
| loop | 42 % → 41 % | 54.0 px | 0.62 | 0.97 | 670 |
| tilted | 17 % → 17 % | 46.9 px | 0.62 | 1.00 | 346 |
| over the wet one | 36 % → 37 % | 54.0 px | 0.62 | 1.02 | 283 |
| long, no reload | 87 % → 80 % | 38.8 px | 0.62 | 0.93 | 1804 | quarters: 0.58 → 0.57 → 0.55 → 0.53

Numbers say: light vs heavy: width 59.8 → 62.6 px, dark 0.61 → 0.61; pressure barely changes the width; the long stroke does not run out of paint.

## Brush Artist · Refs · #40 Watercolour blooms
Watercolor · 90 px · 75.0 s

![Brush Artist · Refs · #40 Watercolour blooms](Brush-Artist-Refs-40-Watercolour-blooms.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 22 % → 34 % | 63.3 px | 0.10 | 1.54 | 231 |
| heavy line | 33 % → 42 % | 94.9 px | 0.11 | 1.28 | 391 |
| pressure swell | 22 % → 30 % | 84.1 px | 0.12 | 1.34 | 249 |
| fast wave | 64 % → 79 % | 73.9 px | 0.11 | 1.23 | 927 |
| slow wave | 63 % → 76 % | 72.4 px | 0.16 | 1.21 | 1491 |
| spiral | 79 % → 87 % | 52.1 px | 0.15 | 1.10 | 1148 |
| loop | 56 % → 66 % | 72.5 px | 0.13 | 1.18 | 629 |
| tilted | 26 % → 27 % | 73.1 px | 0.13 | 1.03 | 500 |
| over the wet one | 53 % → 72 % | 73.8 px | 0.13 | 1.36 | 281 |
| long, no reload | 97 % → 100 % | 43.6 px | 0.17 | 1.02 | 2485 | quarters: 0.21 → 0.19 → 0.17 → 0.13

Numbers say: light vs heavy: width 63.3 → 94.9 px, dark 0.10 → 0.11; wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #41 Coloured pencil hatching
Pastel · 4 px · 13.4 s

![Brush Artist · Refs · #41 Coloured pencil hatching](Brush-Artist-Refs-41-Coloured-pencil-hatching.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 1 % → 1 % | 1.6 px | 0.42 | 1.00 | 17 |
| heavy line | 1 % → 1 % | 2.6 px | 0.43 | 1.00 | 13 |
| pressure swell | 1 % → 1 % | 2.1 px | 0.43 | 1.00 | 13 |
| fast wave | 2 % → 2 % | 2.2 px | 0.42 | 1.00 | 63 |
| slow wave | 2 % → 2 % | 2.1 px | 0.43 | 1.00 | 41 |
| spiral | 3 % → 3 % | 2.1 px | 0.43 | 1.00 | 70 |
| loop | 2 % → 2 % | 2.2 px | 0.43 | 1.00 | 45 |
| tilted | 1 % → 1 % | 3.0 px | 0.42 | 1.00 | 47 |
| over the wet one | 2 % → 2 % | 2.2 px | 0.42 | 1.00 | 25 |
| long, no reload | 5 % → 5 % | 2.3 px | 0.43 | 1.00 | 182 | quarters: 0.02 → 0.02 → 0.02 → 0.03

Numbers say: light vs heavy: width 1.6 → 2.6 px, dark 0.42 → 0.43; the long stroke does not run out of paint.

## Brush Artist · Refs · #42 Oil pastel shaggy
Pastel · 18 px · 14.9 s

![Brush Artist · Refs · #42 Oil pastel shaggy](Brush-Artist-Refs-42-Oil-pastel-shaggy.png)

A light paint: laid on a grey sheet (on white it cannot be seen); **dark** = how far it is from the grey either way.

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 2 % → 2 % | 5.1 px | 0.35 | 1.00 | 44 |
| heavy line | 4 % → 4 % | 10.7 px | 0.36 | 1.00 | 34 |
| pressure swell | 3 % → 3 % | 9.5 px | 0.36 | 1.00 | 25 |
| fast wave | 8 % → 8 % | 9.0 px | 0.36 | 1.00 | 78 |
| slow wave | 7 % → 7 % | 8.2 px | 0.36 | 1.00 | 127 |
| spiral | 12 % → 12 % | 7.7 px | 0.36 | 1.00 | 259 |
| loop | 6 % → 6 % | 7.9 px | 0.36 | 1.00 | 135 |
| tilted | 2 % → 2 % | 6.9 px | 0.36 | 1.00 | 79 |
| over the wet one | 6 % → 6 % | 8.5 px | 0.36 | 1.00 | 59 |
| long, no reload | 15 % → 15 % | 6.9 px | 0.36 | 1.00 | 270 | quarters: 0.00 → 0.00 → 0.00 → 0.00

Numbers say: light vs heavy: width 5.1 → 10.7 px, dark 0.35 → 0.36; the long stroke does not run out of paint.

## Brush Artist · Refs · #43 Dragged black ink blocks
Gouache · 70 px · 46.4 s

![Brush Artist · Refs · #43 Dragged black ink blocks](Brush-Artist-Refs-43-Dragged-black-ink-blocks.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 11 % → 0 % | 31.1 px | 0.65 | 0.03 | 195 |
| heavy line | 16 % → 1 % | 46.9 px | 0.65 | 0.08 | 593 |
| pressure swell | 12 % → 1 % | 44.8 px | 0.65 | 0.11 | 534 |
| fast wave | 22 % → 2 % | 25.8 px | 0.65 | 0.09 | 1041 |
| slow wave | 34 % → 4 % | 39.7 px | 0.65 | 0.13 | 1418 |
| spiral | 40 % → 4 % | 26.3 px | 0.65 | 0.11 | 1451 |
| loop | 28 % → 4 % | 36.5 px | 0.65 | 0.14 | 980 |
| tilted | 10 % → 10 % | 28.3 px | 0.65 | 0.98 | 385 |
| over the wet one | 24 % → 9 % | 40.0 px | 0.65 | 0.36 | 314 |
| long, no reload | 47 % → 8 % | 20.9 px | 0.65 | 0.16 | 1920 | quarters: 0.45 → 0.36 → 0.28 → 0.23

Numbers say: light vs heavy: width 31.1 → 46.9 px, dark 0.65 → 0.65.

## Brush Artist · Refs · #44 Blue looping ribbon
Oil · 80 px · 44.9 s

![Brush Artist · Refs · #44 Blue looping ribbon](Brush-Artist-Refs-44-Blue-looping-ribbon.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 28 % → 29 % | 80.0 px | 0.72 | 1.04 | 496 |
| heavy line | 29 % → 29 % | 85.0 px | 0.72 | 1.00 | 607 |
| pressure swell | 23 % → 23 % | 84.4 px | 0.72 | 1.03 | 674 |
| fast wave | 63 % → 65 % | 72.4 px | 0.72 | 1.04 | 1813 |
| slow wave | 62 % → 62 % | 72.1 px | 0.73 | 1.00 | 2128 |
| spiral | 79 % → 79 % | 51.9 px | 0.72 | 1.00 | 2278 |
| loop | 54 % → 54 % | 69.7 px | 0.73 | 1.00 | 1365 |
| tilted | 22 % → 22 % | 62.4 px | 0.72 | 1.00 | 657 |
| over the wet one | 47 % → 48 % | 70.0 px | 0.72 | 1.01 | 468 |
| long, no reload | 97 % → 97 % | 43.5 px | 0.73 | 1.00 | 2762 | quarters: 0.72 → 0.72 → 0.72 → 0.72

Numbers say: light vs heavy: width 80.0 → 85.0 px, dark 0.72 → 0.72; pressure barely changes the width; the long stroke does not run out of paint.

## Brush Artist · Refs · #45 Soft pastel pepper
Pastel · 40 px · 15.7 s

![Brush Artist · Refs · #45 Soft pastel pepper](Brush-Artist-Refs-45-Soft-pastel-pepper.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 4 % → 4 % | 11.3 px | 0.53 | 1.00 | 94 |
| heavy line | 8 % → 8 % | 23.0 px | 0.53 | 1.00 | 83 |
| pressure swell | 5 % → 5 % | 19.5 px | 0.53 | 1.00 | 59 |
| fast wave | 17 % → 17 % | 19.4 px | 0.53 | 1.00 | 186 |
| slow wave | 15 % → 15 % | 17.1 px | 0.53 | 1.00 | 340 |
| spiral | 25 % → 25 % | 16.3 px | 0.53 | 1.00 | 395 |
| loop | 12 % → 12 % | 16.1 px | 0.53 | 1.00 | 223 |
| tilted | 5 % → 5 % | 12.8 px | 0.53 | 1.00 | 106 |
| over the wet one | 11 % → 11 % | 17.7 px | 0.53 | 1.00 | 86 |
| long, no reload | 30 % → 30 % | 13.6 px | 0.53 | 1.00 | 532 | quarters: 0.18 → 0.18 → 0.18 → 0.18

Numbers say: light vs heavy: width 11.3 → 23.0 px, dark 0.53 → 0.53; the long stroke does not run out of paint.

## Brush Artist · Refs · #46 Red-brown ink lips
Watercolor · 50 px · 57.3 s

![Brush Artist · Refs · #46 Red-brown ink lips](Brush-Artist-Refs-46-Red-brown-ink-lips.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 12 % → 24 % | 33.6 px | 0.66 | 2.04 | 87 |
| heavy line | 19 % → 30 % | 54.1 px | 0.64 | 1.62 | 156 |
| pressure swell | 12 % → 21 % | 43.7 px | 0.67 | 1.76 | 126 |
| fast wave | 40 % → 61 % | 46.7 px | 0.66 | 1.50 | 368 |
| slow wave | 39 % → 59 % | 44.6 px | 0.68 | 1.54 | 686 |
| spiral | 63 % → 76 % | 41.7 px | 0.70 | 1.20 | 580 |
| loop | 35 % → 52 % | 44.9 px | 0.67 | 1.51 | 375 |
| tilted | 16 % → 17 % | 43.6 px | 0.66 | 1.07 | 240 |
| over the wet one | 33 % → 52 % | 47.6 px | 0.66 | 1.58 | 157 |
| long, no reload | 79 % → 95 % | 35.4 px | 0.70 | 1.21 | 747 | quarters: 0.71 → 0.71 → 0.70 → 0.65

Numbers say: light vs heavy: width 33.6 → 54.1 px, dark 0.66 → 0.64; the long stroke does not run out of paint; wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #47 Pink knife slabs
Heavy acrylic · 90 px · 37.2 s

![Brush Artist · Refs · #47 Pink knife slabs](Brush-Artist-Refs-47-Pink-knife-slabs.png)

A light paint: laid on a grey sheet (on white it cannot be seen); **dark** = how far it is from the grey either way.

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 34 % → 34 % | 98.8 px | 0.29 | 0.99 | 110 |
| heavy line | 34 % → 34 % | 98.8 px | 0.29 | 0.99 | 124 |
| pressure swell | 26 % → 27 % | 98.8 px | 0.29 | 1.04 | 42 |
| fast wave | 68 % → 58 % | 78.9 px | 0.26 | 0.85 | 271 |
| slow wave | 69 % → 61 % | 80.0 px | 0.26 | 0.88 | 512 |
| spiral | 67 % → 43 % | 44.4 px | 0.27 | 0.63 | 483 |
| loop | 60 % → 54 % | 77.8 px | 0.27 | 0.90 | 227 |
| tilted | 23 % → 23 % | 63.6 px | 0.28 | 1.00 | 103 |
| over the wet one | 53 % → 53 % | 83.8 px | 0.28 | 1.00 | 169 |
| long, no reload | 95 % → 62 % | 42.7 px | 0.25 | 0.65 | 733 | quarters: 0.00 → 0.00 → 0.00 → 0.00

Numbers say: light vs heavy: width 98.8 → 98.8 px, dark 0.29 → 0.29; pressure barely changes the width; the long stroke does not run out of paint.

## Brush Artist · Refs · #48 Black bands with drips
Watercolor · 70 px · 66.0 s

![Brush Artist · Refs · #48 Black bands with drips](Brush-Artist-Refs-48-Black-bands-with-drips.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 18 % → 40 % | 53.1 px | 0.73 | 2.20 | 157 |
| heavy line | 27 % → 49 % | 79.1 px | 0.75 | 1.78 | 235 |
| pressure swell | 18 % → 27 % | 67.4 px | 0.83 | 1.51 | 162 |
| fast wave | 56 % → 76 % | 64.4 px | 0.81 | 1.37 | 511 |
| slow wave | 54 % → 75 % | 62.0 px | 0.82 | 1.40 | 1195 |
| spiral | 72 % → 92 % | 47.4 px | 0.83 | 1.28 | 1121 |
| loop | 48 % → 79 % | 62.2 px | 0.77 | 1.66 | 511 |
| tilted | 21 % → 22 % | 59.0 px | 0.76 | 1.06 | 581 |
| over the wet one | 44 % → 78 % | 63.7 px | 0.76 | 1.78 | 399 |
| long, no reload | 93 % → 99 % | 41.7 px | 0.88 | 1.06 | 1307 | quarters: 0.89 → 0.89 → 0.89 → 0.86

Numbers say: light vs heavy: width 53.1 → 79.1 px, dark 0.73 → 0.75; the long stroke does not run out of paint; wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #49 Magenta letters round brush
Ink · 30 px · 42.5 s

![Brush Artist · Refs · #49 Magenta letters round brush](Brush-Artist-Refs-49-Magenta-letters-round-brush.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 6 % → 8 % | 17.5 px | 0.50 | 1.29 | 53 |
| heavy line | 21 % → 21 % | 62.0 px | 0.51 | 0.99 | 174 |
| pressure swell | 12 % → 13 % | 46.3 px | 0.52 | 1.02 | 99 |
| fast wave | 39 % → 38 % | 44.8 px | 0.51 | 0.99 | 270 |
| slow wave | 32 % → 31 % | 36.7 px | 0.51 | 0.99 | 446 |
| spiral | 50 % → 49 % | 33.2 px | 0.51 | 0.97 | 481 |
| loop | 29 % → 29 % | 37.8 px | 0.51 | 1.00 | 204 |
| tilted | 11 % → 11 % | 31.0 px | 0.52 | 1.01 | 107 |
| over the wet one | 26 % → 26 % | 42.0 px | 0.52 | 1.01 | 89 |
| long, no reload | 62 % → 56 % | 27.7 px | 0.50 | 0.91 | 941 | quarters: 0.41 → 0.36 → 0.30 → 0.25

Numbers say: light vs heavy: width 17.5 → 62.0 px, dark 0.50 → 0.51.

## Brush Artist · Refs · #50 Thick swipes on photo
Heavy acrylic · 40 px · 32.2 s

![Brush Artist · Refs · #50 Thick swipes on photo](Brush-Artist-Refs-50-Thick-swipes-on-photo.png)

A light paint: laid on a grey sheet (on white it cannot be seen); **dark** = how far it is from the grey either way.

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 14 % → 13 % | 39.4 px | 0.26 | 0.99 | 165 |
| heavy line | 14 % → 14 % | 41.6 px | 0.26 | 0.98 | 140 |
| pressure swell | 11 % → 11 % | 41.9 px | 0.25 | 0.99 | 121 |
| fast wave | 34 % → 31 % | 38.9 px | 0.25 | 0.93 | 401 |
| slow wave | 34 % → 33 % | 39.7 px | 0.26 | 0.95 | 933 |
| spiral | 59 % → 47 % | 38.9 px | 0.25 | 0.80 | 699 |
| loop | 28 % → 27 % | 36.9 px | 0.26 | 0.95 | 342 |
| tilted | 13 % → 13 % | 35.4 px | 0.26 | 1.00 | 164 |
| over the wet one | 26 % → 25 % | 36.8 px | 0.26 | 0.98 | 180 |
| long, no reload | 66 % → 46 % | 29.8 px | 0.24 | 0.69 | 1092 | quarters: 0.00 → 0.00 → 0.00 → 0.00

Numbers say: light vs heavy: width 39.4 → 41.6 px, dark 0.26 → 0.26; pressure barely changes the width; the long stroke does not run out of paint.

## Brush Artist · Refs · Drag #e8b4a8
Gouache · 40 px · 29.0 s

![Brush Artist · Refs · Drag #e8b4a8](Brush-Artist-Refs-Drag-e8b4a8.png)

A light paint: laid on a grey sheet (on white it cannot be seen); **dark** = how far it is from the grey either way.

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 2 % → 0 % | 5.0 px | 0.00 | 0.00 | 153 |
| heavy line | 3 % → 0 % | 8.7 px | 0.00 | 0.00 | 179 |
| pressure swell | 2 % → 0 % | 9.1 px | 0.00 | 0.00 | 116 |
| fast wave | 3 % → 0 % | 3.4 px | 0.00 | 0.00 | 367 |
| slow wave | 9 % → 0 % | 10.9 px | 0.00 | 0.00 | 705 |
| spiral | 10 % → 0 % | 6.9 px | 0.00 | 0.00 | 1062 |
| loop | 6 % → 0 % | 7.9 px | 0.34 | 0.01 | 407 |
| tilted | 2 % → 2 % | 6.3 px | 0.34 | 0.89 | 176 |
| over the wet one | 5 % → 0 % | 8.2 px | 0.34 | 0.02 | 178 |
| long, no reload | 12 % → 0 % | 5.4 px | 0.34 | 0.01 | 872 | quarters: 0.01 → 0.01 → 0.01 → 0.01

Numbers say: light vs heavy: width 5.0 → 8.7 px, dark 0.00 → 0.00; the long stroke does not run out of paint.

## Brush Artist · Refs · Drag #e8e4e0
Gouache · 40 px · 29.0 s

![Brush Artist · Refs · Drag #e8e4e0](Brush-Artist-Refs-Drag-e8e4e0.png)

A light paint: laid on a grey sheet (on white it cannot be seen); **dark** = how far it is from the grey either way.

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 2 % → 0 % | 5.0 px | 0.00 | 0.00 | 153 |
| heavy line | 3 % → 0 % | 8.7 px | 0.00 | 0.00 | 150 |
| pressure swell | 2 % → 0 % | 9.1 px | 0.00 | 0.00 | 105 |
| fast wave | 3 % → 0 % | 3.4 px | 0.00 | 0.00 | 335 |
| slow wave | 9 % → 0 % | 10.9 px | 0.00 | 0.00 | 811 |
| spiral | 10 % → 0 % | 6.9 px | 0.00 | 0.00 | 973 |
| loop | 6 % → 0 % | 7.9 px | 0.42 | 0.01 | 344 |
| tilted | 2 % → 2 % | 6.3 px | 0.42 | 0.89 | 190 |
| over the wet one | 5 % → 0 % | 8.2 px | 0.42 | 0.02 | 174 |
| long, no reload | 12 % → 0 % | 5.4 px | 0.43 | 0.01 | 915 | quarters: 0.01 → 0.01 → 0.01 → 0.01

Numbers say: light vs heavy: width 5.0 → 8.7 px, dark 0.00 → 0.00; the long stroke does not run out of paint.

## Brush Artist · Refs · Finger
Pastel · 36 px · 30.2 s · over bands of wet oil paint and oil pastel in turn (it works on paint already there: look at what it does to the bands; covered counts the bands too)

![Brush Artist · Refs · Finger](Brush-Artist-Refs-Finger.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 25 % → 25 % | 73.9 px | 0.80 | 1.00 | 46 |
| heavy line | 27 % → 27 % | 78.5 px | 0.80 | 1.00 | 72 |
| pressure swell | 26 % → 26 % | 97.7 px | 0.80 | 1.00 | 45 |
| fast wave | 32 % → 32 % | 37.1 px | 0.78 | 1.00 | 198 |
| slow wave | 31 % → 31 % | 36.2 px | 0.78 | 1.00 | 321 |
| spiral | 38 % → 38 % | 25.0 px | 0.76 | 1.00 | 347 |
| loop | 30 % → 30 % | 39.4 px | 0.78 | 1.00 | 186 |
| tilted | 26 % → 26 % | 73.4 px | 0.79 | 1.00 | 187 |
| over the wet one | 29 % → 29 % | 6.7 px | 0.79 | 1.00 | 163 |
| long, no reload | 40 % → 40 % | 18.0 px | 0.75 | 1.00 | 698 | quarters: 0.25 → 0.36 → 0.33 → 0.38

Numbers say: light vs heavy: width 73.9 → 78.5 px, dark 0.80 → 0.80; pressure barely changes the width; the long stroke does not run out of paint.

## Brush Artist · Ink — wash
Watercolor · 38 px · 42.0 s

![Brush Artist · Ink — wash](Brush-Artist-Ink-wash.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 11 % → 11 % | 31.6 px | 0.38 | 1.04 | 78 |
| heavy line | 19 % → 19 % | 54.3 px | 0.32 | 1.03 | 130 |
| pressure swell | 12 % → 12 % | 45.1 px | 0.36 | 1.04 | 83 |
| fast wave | 39 % → 41 % | 45.5 px | 0.30 | 1.04 | 376 |
| slow wave | 37 % → 38 % | 42.9 px | 0.37 | 1.03 | 576 |
| spiral | 58 % → 60 % | 38.5 px | 0.30 | 1.04 | 467 |
| loop | 32 % → 33 % | 41.9 px | 0.35 | 1.02 | 255 |
| tilted | 13 % → 14 % | 36.9 px | 0.38 | 1.04 | 143 |
| over the wet one | 29 % → 30 % | 42.7 px | 0.38 | 1.04 | 101 |
| long, no reload | 67 % → 71 % | 29.9 px | 0.29 | 1.07 | 591 | quarters: 0.33 → 0.26 → 0.19 → 0.12

Numbers say: light vs heavy: width 31.6 → 54.3 px, dark 0.38 → 0.32.

## Brush Artist · Ink — brush line
Ink · 16 px · 34.6 s

![Brush Artist · Ink — brush line](Brush-Artist-Ink-brush-line.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 3 % → 5 % | 7.7 px | 0.78 | 1.81 | 52 |
| heavy line | 13 % → 13 % | 39.0 px | 0.88 | 0.99 | 111 |
| pressure swell | 8 % → 8 % | 28.4 px | 0.87 | 1.05 | 99 |
| fast wave | 24 % → 23 % | 28.0 px | 0.87 | 0.96 | 233 |
| slow wave | 20 % → 19 % | 22.6 px | 0.87 | 0.97 | 328 |
| spiral | 30 % → 27 % | 20.1 px | 0.86 | 0.89 | 351 |
| loop | 18 % → 18 % | 23.6 px | 0.88 | 1.00 | 196 |
| tilted | 7 % → 7 % | 20.5 px | 0.88 | 1.01 | 81 |
| over the wet one | 17 % → 17 % | 26.8 px | 0.88 | 1.00 | 93 |
| long, no reload | 42 % → 30 % | 18.9 px | 0.85 | 0.71 | 497 | quarters: 0.49 → 0.40 → 0.30 → 0.20

Numbers say: light vs heavy: width 7.7 → 39.0 px, dark 0.78 → 0.88; wet paint spreads well beyond the stroke.

## Brush Artist · Ink — dry brush
Gouache · 30 px · 25.1 s

![Brush Artist · Ink — dry brush](Brush-Artist-Ink-dry-brush.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 3 % → 0 % | 9.2 px | 0.77 | 0.00 | 84 |
| heavy line | 5 % → 0 % | 14.0 px | 0.00 | 0.00 | 157 |
| pressure swell | 4 % → 0 % | 13.5 px | 0.77 | 0.01 | 99 |
| fast wave | 7 % → 0 % | 8.0 px | 0.77 | 0.00 | 276 |
| slow wave | 11 % → 0 % | 12.2 px | 0.77 | 0.01 | 471 |
| spiral | 14 % → 0 % | 9.2 px | 0.77 | 0.01 | 459 |
| loop | 9 % → 0 % | 11.1 px | 0.77 | 0.02 | 361 |
| tilted | 4 % → 4 % | 11.2 px | 0.77 | 0.94 | 152 |
| over the wet one | 8 % → 1 % | 12.2 px | 0.77 | 0.10 | 121 |
| long, no reload | 16 % → 1 % | 7.2 px | 0.77 | 0.03 | 658 | quarters: 0.21 → 0.15 → 0.12 → 0.11

Numbers say: light vs heavy: width 9.2 → 14.0 px, dark 0.77 → 0.00.

## Brush Artist · Watercolour — blue
Watercolor · 40 px · 37.9 s

![Brush Artist · Watercolour — blue](Brush-Artist-Watercolour-blue.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 6 % → 10 % | 16.7 px | 0.25 | 1.71 | 44 |
| heavy line | 11 % → 12 % | 31.5 px | 0.25 | 1.13 | 105 |
| pressure swell | 7 % → 9 % | 25.4 px | 0.26 | 1.32 | 54 |
| fast wave | 24 % → 25 % | 27.8 px | 0.24 | 1.06 | 167 |
| slow wave | 22 % → 27 % | 25.9 px | 0.26 | 1.22 | 318 |
| spiral | 38 % → 41 % | 25.2 px | 0.22 | 1.08 | 298 |
| loop | 20 % → 22 % | 25.3 px | 0.26 | 1.13 | 137 |
| tilted | 12 % → 12 % | 33.3 px | 0.26 | 1.00 | 165 |
| over the wet one | 21 % → 24 % | 24.7 px | 0.26 | 1.15 | 100 |
| long, no reload | 52 % → 54 % | 23.1 px | 0.22 | 1.04 | 453 | quarters: 0.18 → 0.14 → 0.11 → 0.08

Numbers say: light vs heavy: width 16.7 → 31.5 px, dark 0.25 → 0.25; wet paint spreads well beyond the stroke.

## Brush Artist · Watercolour — violet
Watercolor · 40 px · 40.4 s

![Brush Artist · Watercolour — violet](Brush-Artist-Watercolour-violet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 6 % → 10 % | 16.7 px | 0.40 | 1.71 | 40 |
| heavy line | 11 % → 12 % | 31.5 px | 0.40 | 1.13 | 78 |
| pressure swell | 7 % → 9 % | 25.4 px | 0.41 | 1.32 | 45 |
| fast wave | 24 % → 25 % | 27.8 px | 0.38 | 1.06 | 178 |
| slow wave | 22 % → 27 % | 25.9 px | 0.41 | 1.22 | 296 |
| spiral | 38 % → 41 % | 25.2 px | 0.36 | 1.08 | 288 |
| loop | 20 % → 22 % | 25.3 px | 0.40 | 1.13 | 211 |
| tilted | 12 % → 12 % | 33.3 px | 0.40 | 1.00 | 168 |
| over the wet one | 21 % → 24 % | 24.7 px | 0.40 | 1.15 | 106 |
| long, no reload | 52 % → 54 % | 23.1 px | 0.34 | 1.04 | 454 | quarters: 0.28 → 0.22 → 0.18 → 0.14

Numbers say: light vs heavy: width 16.7 → 31.5 px, dark 0.40 → 0.40; wet paint spreads well beyond the stroke.

## Brush Artist · Watercolour — teal
Watercolor · 40 px · 39.0 s

![Brush Artist · Watercolour — teal](Brush-Artist-Watercolour-teal.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 6 % → 10 % | 16.7 px | 0.16 | 1.71 | 51 |
| heavy line | 11 % → 12 % | 31.5 px | 0.16 | 1.13 | 104 |
| pressure swell | 7 % → 9 % | 25.4 px | 0.17 | 1.32 | 57 |
| fast wave | 24 % → 25 % | 27.8 px | 0.15 | 1.06 | 166 |
| slow wave | 22 % → 27 % | 25.9 px | 0.17 | 1.22 | 358 |
| spiral | 38 % → 41 % | 25.2 px | 0.15 | 1.08 | 309 |
| loop | 20 % → 22 % | 25.3 px | 0.16 | 1.13 | 164 |
| tilted | 12 % → 12 % | 33.3 px | 0.16 | 1.00 | 116 |
| over the wet one | 21 % → 24 % | 24.7 px | 0.16 | 1.15 | 71 |
| long, no reload | 52 % → 54 % | 23.1 px | 0.14 | 1.04 | 435 | quarters: 0.11 → 0.09 → 0.07 → 0.06

Numbers say: light vs heavy: width 16.7 → 31.5 px, dark 0.16 → 0.16; wet paint spreads well beyond the stroke.

## Brush Artist · Gouache
Gouache · 30 px · 42.6 s

![Brush Artist · Gouache](Brush-Artist-Gouache.png)

A light paint: laid on a grey sheet (on white it cannot be seen); **dark** = how far it is from the grey either way.

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 8 % → 8 % | 24.4 px | 0.27 | 0.97 | 89 |
| heavy line | 15 % → 12 % | 42.9 px | 0.27 | 0.78 | 112 |
| pressure swell | 11 % → 9 % | 41.1 px | 0.27 | 0.85 | 81 |
| fast wave | 30 % → 14 % | 35.0 px | 0.26 | 0.45 | 257 |
| slow wave | 29 % → 14 % | 34.0 px | 0.26 | 0.47 | 497 |
| spiral | 40 % → 14 % | 26.7 px | 0.26 | 0.35 | 595 |
| loop | 24 % → 15 % | 30.6 px | 0.26 | 0.62 | 266 |
| tilted | 10 % → 10 % | 27.5 px | 0.27 | 1.01 | 150 |
| over the wet one | 22 % → 19 % | 32.8 px | 0.27 | 0.89 | 117 |
| long, no reload | 43 % → 15 % | 19.1 px | 0.26 | 0.35 | 651 | quarters: 0.01 → 0.01 → 0.01 → 0.01

Numbers say: light vs heavy: width 24.4 → 42.9 px, dark 0.27 → 0.27; the long stroke does not run out of paint.

## Brush Artist · Oil — bristle
Oil · 30 px · 26.4 s

![Brush Artist · Oil — bristle](Brush-Artist-Oil-bristle.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 9 % → 9 % | 27.1 px | 0.54 | 1.00 | 156 |
| heavy line | 10 % → 10 % | 29.4 px | 0.54 | 1.00 | 153 |
| pressure swell | 8 % → 8 % | 29.3 px | 0.55 | 1.00 | 131 |
| fast wave | 24 % → 24 % | 27.6 px | 0.55 | 1.00 | 442 |
| slow wave | 25 % → 25 % | 28.6 px | 0.55 | 1.00 | 853 |
| spiral | 39 % → 39 % | 25.8 px | 0.54 | 1.00 | 826 |
| loop | 20 % → 20 % | 26.3 px | 0.54 | 1.00 | 328 |
| tilted | 11 % → 11 % | 30.6 px | 0.53 | 1.00 | 203 |
| over the wet one | 20 % → 20 % | 26.4 px | 0.53 | 1.00 | 161 |
| long, no reload | 50 % → 50 % | 22.5 px | 0.54 | 1.00 | 1010 | quarters: 0.32 → 0.30 → 0.29 → 0.28

Numbers say: light vs heavy: width 27.1 → 29.4 px, dark 0.54 → 0.54; pressure barely changes the width; the long stroke does not run out of paint.

## Brush Artist · Charcoal — stick
Charcoal · 28 px · 13.7 s

![Brush Artist · Charcoal — stick](Brush-Artist-Charcoal-stick.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 3 % → 3 % | 8.4 px | 0.85 | 1.00 | 35 |
| heavy line | 6 % → 6 % | 17.8 px | 0.85 | 1.00 | 44 |
| pressure swell | 4 % → 4 % | 13.9 px | 0.85 | 1.00 | 27 |
| fast wave | 12 % → 12 % | 14.0 px | 0.85 | 1.00 | 63 |
| slow wave | 11 % → 11 % | 12.5 px | 0.85 | 1.00 | 126 |
| spiral | 19 % → 19 % | 12.7 px | 0.85 | 1.00 | 121 |
| loop | 10 % → 10 % | 12.8 px | 0.85 | 1.00 | 64 |
| tilted | 4 % → 4 % | 10.9 px | 0.85 | 1.00 | 38 |
| over the wet one | 9 % → 9 % | 13.5 px | 0.85 | 1.00 | 27 |
| long, no reload | 27 % → 27 % | 12.2 px | 0.85 | 1.00 | 186 | quarters: 0.26 → 0.25 → 0.26 → 0.27

Numbers say: light vs heavy: width 8.4 → 17.8 px, dark 0.85 → 0.85; the long stroke does not run out of paint.

## Brush Artist · Charcoal — stick B
Charcoal · 36 px · 14.5 s

![Brush Artist · Charcoal — stick B](Brush-Artist-Charcoal-stick-B.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 4 % → 4 % | 10.5 px | 0.85 | 1.00 | 55 |
| heavy line | 7 % → 7 % | 21.1 px | 0.85 | 1.00 | 63 |
| pressure swell | 4 % → 4 % | 16.5 px | 0.85 | 1.00 | 28 |
| fast wave | 15 % → 15 % | 16.8 px | 0.85 | 1.00 | 93 |
| slow wave | 13 % → 13 % | 14.7 px | 0.85 | 1.00 | 150 |
| spiral | 23 % → 23 % | 15.0 px | 0.85 | 1.00 | 175 |
| loop | 11 % → 11 % | 14.8 px | 0.85 | 1.00 | 80 |
| tilted | 4 % → 4 % | 12.3 px | 0.85 | 1.00 | 61 |
| over the wet one | 10 % → 10 % | 15.9 px | 0.85 | 1.00 | 39 |
| long, no reload | 31 % → 31 % | 13.9 px | 0.85 | 1.00 | 232 | quarters: 0.30 → 0.28 → 0.29 → 0.30

Numbers say: light vs heavy: width 10.5 → 21.1 px, dark 0.85 → 0.85; the long stroke does not run out of paint.

## Brush Artist · Charcoal — stick C
Charcoal · 22 px · 14.2 s

![Brush Artist · Charcoal — stick C](Brush-Artist-Charcoal-stick-C.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 2 % → 2 % | 6.9 px | 0.85 | 1.00 | 30 |
| heavy line | 5 % → 5 % | 15.3 px | 0.85 | 1.00 | 29 |
| pressure swell | 3 % → 3 % | 12.2 px | 0.85 | 1.00 | 18 |
| fast wave | 10 % → 10 % | 12.1 px | 0.85 | 1.00 | 43 |
| slow wave | 9 % → 9 % | 10.8 px | 0.85 | 1.00 | 84 |
| spiral | 17 % → 17 % | 11.0 px | 0.85 | 1.00 | 86 |
| loop | 9 % → 9 % | 11.4 px | 0.85 | 1.00 | 49 |
| tilted | 4 % → 4 % | 9.9 px | 0.85 | 1.00 | 35 |
| over the wet one | 8 % → 8 % | 11.7 px | 0.85 | 1.00 | 17 |
| long, no reload | 24 % → 24 % | 11.0 px | 0.85 | 1.00 | 315 | quarters: 0.24 → 0.22 → 0.23 → 0.24

Numbers say: light vs heavy: width 6.9 → 15.3 px, dark 0.85 → 0.85; the long stroke does not run out of paint.

## Brush Artist · Refs · #01 Henry Ward peach cloud — own sheet
own sheet 600 × 600 · Gouache · 44 px · 21.3 s

![Brush Artist · Refs · #01 Henry Ward peach cloud — own sheet](Brush-Artist-Refs-01-Henry-Ward-peach-cloud-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 14 % → 39 % | 40.5 px | 0.59 | 2.74 | 385 |
| stroke 2 | 24 % → 58 % | 79.5 px | 0.59 | 2.40 | 189 |
| stroke 3 | 28 % → 56 % | 81.3 px | 0.59 | 2.01 | 289 |
| stroke 4 | 30 % → 63 % | 99.7 px | 0.59 | 2.05 | 219 |
| stroke 5 | 30 % → 55 % | 86.0 px | 0.59 | 1.86 | 269 |
| stroke 6 | 30 % → 42 % | 91.1 px | 0.59 | 1.42 | 203 |
| stroke 7 | 16 % → 53 % | 38.9 px | 0.59 | 3.38 | 181 |
| stroke 8 | 18 % → 49 % | 44.8 px | 0.59 | 2.76 | 228 |
| stroke 9 | 21 % → 50 % | 54.2 px | 0.59 | 2.39 | 228 |
| stroke 10 | 23 % → 51 % | 61.9 px | 0.59 | 2.21 | 239 |
| stroke 11 | 25 % → 54 % | 72.0 px | 0.59 | 2.11 | 233 |
| stroke 12 | 29 % → 56 % | 88.0 px | 0.59 | 1.92 | 226 |
| stroke 13 | 37 % → 59 % | 108.0 px | 0.59 | 1.59 | 356 |
| stroke 14 | 40 % → 61 % | 113.8 px | 0.59 | 1.54 | 251 |
| stroke 15 | 53 % → 67 % | 156.4 px | 0.59 | 1.27 | 237 |
| stroke 16 | 54 % → 68 % | 164.9 px | 0.59 | 1.24 | 261 |
| stroke 17 | 55 % → 69 % | 155.8 px | 0.59 | 1.24 | 233 |
| stroke 18 | 57 % → 67 % | 164.8 px | 0.59 | 1.19 | 268 |
| stroke 19 | 58 % → 66 % | 163.9 px | 0.59 | 1.13 | 198 |
| stroke 20 | 58 % → 63 % | 167.5 px | 0.59 | 1.09 | 318 |
| stroke 21 | 58 % → 60 % | 168.2 px | 0.59 | 1.04 | 288 |
| stroke 22 | 59 % → 61 % | 173.1 px | 0.59 | 1.03 | 335 |
| stroke 23 | 59 % → 59 % | 167.7 px | 0.59 | 1.00 | 337 |
| stroke 24 | 63 % → 62 % | 187.3 px | 0.59 | 0.99 | 306 |

Numbers say: wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #02 Henry Ward cream strokes — own sheet
own sheet 600 × 600 · Gouache · 46 px · 13.8 s

![Brush Artist · Refs · #02 Henry Ward cream strokes — own sheet](Brush-Artist-Refs-02-Henry-Ward-cream-strokes-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 18 % → 32 % | 37.3 px | 0.70 | 1.77 | 510 |
| stroke 2 | 28 % → 37 % | 72.5 px | 0.70 | 1.34 | 310 |
| stroke 3 | 27 % → 44 % | 68.7 px | 0.71 | 1.64 | 348 |
| stroke 4 | 29 % → 41 % | 71.2 px | 0.71 | 1.42 | 373 |
| stroke 5 | 35 % → 45 % | 85.0 px | 0.71 | 1.29 | 444 |
| stroke 6 | 28 % → 39 % | 66.8 px | 0.70 | 1.42 | 409 |
| stroke 7 | 29 % → 27 % | 74.4 px | 0.70 | 0.92 | 386 |

Numbers say: wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #03 Henry Ward navy contours — own sheet
own sheet 600 × 600 · Heavy acrylic · 22 px · 4.4 s

![Brush Artist · Refs · #03 Henry Ward navy contours — own sheet](Brush-Artist-Refs-03-Henry-Ward-navy-contours-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 12 % → 18 % | 23.4 px | 0.69 | 1.57 | 235 |
| stroke 2 | 20 % → 23 % | 28.6 px | 0.69 | 1.15 | 170 |
| stroke 3 | 23 % → 23 % | 33.7 px | 0.69 | 1.01 | 207 |
| stroke 4 | 23 % → 21 % | 51.1 px | 0.69 | 0.92 | 263 |

Numbers say: wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #04 Henry Ward grey cloud — own sheet
own sheet 600 × 600 · Gouache · 50 px · 24.3 s

![Brush Artist · Refs · #04 Henry Ward grey cloud — own sheet](Brush-Artist-Refs-04-Henry-Ward-grey-cloud-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 14 % → 48 % | 42.2 px | 0.40 | 3.32 | 419 |
| stroke 2 | 19 % → 50 % | 53.3 px | 0.40 | 2.68 | 327 |
| stroke 3 | 27 % → 57 % | 75.3 px | 0.40 | 2.11 | 324 |
| stroke 4 | 30 % → 60 % | 88.0 px | 0.40 | 1.98 | 326 |
| stroke 5 | 36 % → 66 % | 110.1 px | 0.40 | 1.83 | 353 |
| stroke 6 | 40 % → 70 % | 129.7 px | 0.40 | 1.77 | 332 |
| stroke 7 | 46 % → 77 % | 134.2 px | 0.40 | 1.67 | 385 |
| stroke 8 | 45 % → 77 % | 133.7 px | 0.40 | 1.70 | 344 |
| stroke 9 | 45 % → 77 % | 133.8 px | 0.40 | 1.72 | 348 |
| stroke 10 | 46 % → 77 % | 148.0 px | 0.40 | 1.67 | 325 |
| stroke 11 | 46 % → 77 % | 130.7 px | 0.40 | 1.67 | 278 |
| stroke 12 | 47 % → 76 % | 141.7 px | 0.40 | 1.63 | 315 |
| stroke 13 | 46 % → 77 % | 131.3 px | 0.40 | 1.67 | 317 |
| stroke 14 | 47 % → 77 % | 139.7 px | 0.40 | 1.64 | 318 |
| stroke 15 | 46 % → 72 % | 133.2 px | 0.40 | 1.56 | 377 |
| stroke 16 | 47 % → 70 % | 143.4 px | 0.40 | 1.47 | 286 |
| stroke 17 | 45 % → 61 % | 130.9 px | 0.40 | 1.33 | 331 |
| stroke 18 | 45 % → 56 % | 149.2 px | 0.40 | 1.24 | 302 |
| stroke 19 | 46 % → 47 % | 136.3 px | 0.40 | 1.03 | 373 |
| stroke 20 | 47 % → 46 % | 148.0 px | 0.40 | 0.99 | 326 |

Numbers say: wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #05 Henry Ward green in rust loops — own sheet
own sheet 600 × 600 · Heavy acrylic · 20 px · 5.0 s

![Brush Artist · Refs · #05 Henry Ward green in rust loops — own sheet](Brush-Artist-Refs-05-Henry-Ward-green-in-rust-loops-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 12 % → 19 % | 21.2 px | 0.02 | 1.61 | 186 |
| stroke 2 | 12 % → 11 % | 23.7 px | 0.02 | 0.93 | 202 |
| stroke 3 | 23 % → 22 % | 41.7 px | 0.02 | 0.93 | 184 |

Numbers say: wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #06 Henry Ward scrubbed grey — own sheet
own sheet 600 × 600 · Gouache · 50 px · 29.0 s

![Brush Artist · Refs · #06 Henry Ward scrubbed grey — own sheet](Brush-Artist-Refs-06-Henry-Ward-scrubbed-grey-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 17 % → 54 % | 42.0 px | 0.40 | 3.16 | 307 |
| stroke 2 | 22 % → 56 % | 58.8 px | 0.40 | 2.55 | 382 |
| stroke 3 | 28 % → 61 % | 87.1 px | 0.40 | 2.13 | 624 |
| stroke 4 | 29 % → 61 % | 92.8 px | 0.40 | 2.06 | 823 |
| stroke 5 | 42 % → 75 % | 127.0 px | 0.40 | 1.78 | 839 |
| stroke 6 | 45 % → 76 % | 138.6 px | 0.40 | 1.67 | 577 |
| stroke 7 | 47 % → 77 % | 133.9 px | 0.40 | 1.64 | 613 |
| stroke 8 | 47 % → 77 % | 147.9 px | 0.40 | 1.65 | 316 |
| stroke 9 | 45 % → 77 % | 137.9 px | 0.40 | 1.71 | 311 |
| stroke 10 | 45 % → 77 % | 147.0 px | 0.40 | 1.70 | 351 |
| stroke 11 | 46 % → 77 % | 136.1 px | 0.40 | 1.66 | 398 |
| stroke 12 | 47 % → 77 % | 143.2 px | 0.40 | 1.64 | 329 |
| stroke 13 | 45 % → 77 % | 127.5 px | 0.40 | 1.71 | 307 |
| stroke 14 | 44 % → 76 % | 130.2 px | 0.40 | 1.72 | 355 |
| stroke 15 | 45 % → 77 % | 128.6 px | 0.40 | 1.71 | 347 |
| stroke 16 | 46 % → 77 % | 146.4 px | 0.40 | 1.68 | 284 |
| stroke 17 | 45 % → 70 % | 134.2 px | 0.40 | 1.55 | 335 |
| stroke 18 | 47 % → 67 % | 141.3 px | 0.40 | 1.44 | 330 |
| stroke 19 | 45 % → 61 % | 134.0 px | 0.40 | 1.36 | 319 |
| stroke 20 | 45 % → 59 % | 141.3 px | 0.40 | 1.30 | 324 |
| stroke 21 | 45 % → 50 % | 131.4 px | 0.40 | 1.11 | 340 |
| stroke 22 | 46 % → 45 % | 151.0 px | 0.40 | 0.99 | 300 |

Numbers say: wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #07 Henry Ward blue L + black zigzag — own sheet
own sheet 600 × 600 · Heavy acrylic · 34 px · 3.9 s

![Brush Artist · Refs · #07 Henry Ward blue L + black zigzag — own sheet](Brush-Artist-Refs-07-Henry-Ward-blue-L-black-zigzag-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 16 % → 17 % | 36.5 px | 0.59 | 1.11 | 382 |
| stroke 2 | 18 % → 17 % | 44.0 px | 0.59 | 0.93 | 224 |

## Brush Artist · Refs · #08 Henry Ward olive bands — own sheet
own sheet 600 × 600 · Gouache · 34 px · 8.4 s

![Brush Artist · Refs · #08 Henry Ward olive bands — own sheet](Brush-Artist-Refs-08-Henry-Ward-olive-bands-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 9 % → 7 % | 17.9 px | 0.59 | 0.82 | 250 |
| stroke 2 | 15 % → 9 % | 32.8 px | 0.59 | 0.63 | 273 |
| stroke 3 | 13 % → 13 % | 26.4 px | 0.59 | 1.02 | 237 |
| stroke 4 | 15 % → 11 % | 31.5 px | 0.59 | 0.78 | 275 |
| stroke 5 | 20 % → 14 % | 40.1 px | 0.59 | 0.71 | 253 |
| stroke 6 | 13 % → 7 % | 24.2 px | 0.59 | 0.52 | 229 |

## Brush Artist · Refs · #09 Henry Ward white loops — own sheet
own sheet 600 × 600 · Gouache · 46 px · 16.1 s

![Brush Artist · Refs · #09 Henry Ward white loops — own sheet](Brush-Artist-Refs-09-Henry-Ward-white-loops-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 23 % → 4 % | 12.2 px | 0.07 | 0.17 | 2593 |
| stroke 2 | 26 % → 4 % | 26.2 px | 0.07 | 0.14 | 2111 |
| stroke 3 | 34 % → 4 % | 31.4 px | 0.07 | 0.12 | 1857 |
| stroke 4 | 3 % → 1 % | 6.1 px | 0.06 | 0.22 | 248 |
| stroke 5 | 4 % → 2 % | 12.1 px | 0.08 | 0.38 | 312 |
| stroke 6 | 7 % → 4 % | 18.2 px | 0.07 | 0.65 | 285 |
| stroke 7 | 14 % → 4 % | 36.3 px | 0.07 | 0.31 | 299 |
| stroke 8 | 2 % → 0 % | 3.0 px | 0.05 | 0.06 | 239 |

## Brush Artist · Refs · #10 Henry Ward maroon loops — own sheet
own sheet 600 × 600 · Heavy acrylic · 30 px · 5.9 s

![Brush Artist · Refs · #10 Henry Ward maroon loops — own sheet](Brush-Artist-Refs-10-Henry-Ward-maroon-loops-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 12 % → 28 % | 29.0 px | 0.72 | 2.41 | 555 |
| stroke 2 | 22 % → 41 % | 49.1 px | 0.72 | 1.87 | 308 |
| stroke 3 | 29 % → 37 % | 59.1 px | 0.72 | 1.27 | 349 |
| stroke 4 | 42 % → 41 % | 95.0 px | 0.72 | 0.96 | 213 |
| stroke 5 | 35 % → 32 % | 87.1 px | 0.72 | 0.93 | 267 |

Numbers say: wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #11 Henry Ward purple spun balls — own sheet
own sheet 600 × 600 · Heavy acrylic · 36 px · 4.5 s

![Brush Artist · Refs · #11 Henry Ward purple spun balls — own sheet](Brush-Artist-Refs-11-Henry-Ward-purple-spun-balls-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 24 % → 35 % | 26.9 px | 0.68 | 1.44 | 391 |
| stroke 2 | 35 % → 47 % | 38.6 px | 0.68 | 1.34 | 345 |
| stroke 3 | 36 % → 35 % | 39.8 px | 0.68 | 0.97 | 437 |

## Brush Artist · Refs · #12 Henry Ward black-olive cage — own sheet
own sheet 600 × 600 · Gouache · 28 px · 8.3 s

![Brush Artist · Refs · #12 Henry Ward black-olive cage — own sheet](Brush-Artist-Refs-12-Henry-Ward-black-olive-cage-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 7 % → 12 % | 13.4 px | 0.60 | 1.68 | 383 |
| stroke 2 | 7 % → 12 % | 16.3 px | 0.60 | 1.80 | 255 |
| stroke 3 | 15 % → 16 % | 24.2 px | 0.60 | 1.03 | 462 |
| stroke 4 | 16 % → 15 % | 32.2 px | 0.60 | 0.92 | 264 |
| stroke 5 | 16 % → 11 % | 29.0 px | 0.60 | 0.68 | 258 |
| stroke 6 | 25 % → 16 % | 48.3 px | 0.60 | 0.65 | 364 |

Numbers say: wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #13 Henry Ward blue streaky form — own sheet
own sheet 600 × 600 · Gouache · 50 px · 19.0 s

![Brush Artist · Refs · #13 Henry Ward blue streaky form — own sheet](Brush-Artist-Refs-13-Henry-Ward-blue-streaky-form-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 14 % → 8 % | 42.7 px | 0.04 | 0.56 | 418 |
| stroke 2 | 20 % → 7 % | 61.3 px | 0.04 | 0.36 | 473 |
| stroke 3 | 31 % → 8 % | 88.7 px | 0.04 | 0.25 | 361 |
| stroke 4 | 31 % → 7 % | 99.6 px | 0.04 | 0.23 | 316 |
| stroke 5 | 45 % → 8 % | 130.2 px | 0.04 | 0.18 | 348 |
| stroke 6 | 45 % → 9 % | 129.6 px | 0.04 | 0.20 | 386 |
| stroke 7 | 46 % → 10 % | 136.7 px | 0.04 | 0.22 | 349 |
| stroke 8 | 47 % → 8 % | 143.3 px | 0.03 | 0.18 | 343 |
| stroke 9 | 46 % → 7 % | 142.0 px | 0.03 | 0.16 | 334 |
| stroke 10 | 46 % → 7 % | 152.6 px | 0.03 | 0.16 | 295 |
| stroke 11 | 44 % → 5 % | 136.4 px | 0.03 | 0.11 | 305 |
| stroke 12 | 45 % → 6 % | 135.8 px | 0.03 | 0.14 | 321 |
| stroke 13 | 45 % → 7 % | 138.8 px | 0.04 | 0.17 | 334 |
| stroke 14 | 43 % → 7 % | 129.4 px | 0.04 | 0.16 | 359 |
| stroke 15 | 44 % → 7 % | 125.8 px | 0.04 | 0.17 | 323 |
| stroke 16 | 46 % → 7 % | 137.2 px | 0.04 | 0.16 | 321 |
| stroke 17 | 55 % → 4 % | 137.1 px | 0.04 | 0.08 | 321 |
| stroke 18 | 58 % → 4 % | 140.1 px | 0.04 | 0.08 | 317 |
| stroke 19 | 64 % → 5 % | 130.9 px | 0.04 | 0.08 | 276 |
| stroke 20 | 72 % → 5 % | 137.6 px | 0.04 | 0.08 | 284 |
| stroke 21 | 1 % → 0 % | 2.9 px | 0.04 | 0.02 | 195 |
| stroke 22 | 12 % → 7 % | 34.1 px | 0.04 | 0.61 | 244 |
| stroke 23 | 23 % → 8 % | 70.4 px | 0.04 | 0.35 | 322 |
| stroke 24 | 14 % → 5 % | 38.0 px | 0.03 | 0.35 | 392 |
| stroke 25 | 18 % → 6 % | 46.1 px | 0.04 | 0.31 | 351 |

## Brush Artist · Refs · #14 Henry Ward olive totem — own sheet
own sheet 600 × 600 · Heavy acrylic · 48 px · 9.6 s

![Brush Artist · Refs · #14 Henry Ward olive totem — own sheet](Brush-Artist-Refs-14-Henry-Ward-olive-totem-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 19 % → 49 % | 48.9 px | 0.38 | 2.60 | 203 |
| stroke 2 | 22 % → 53 % | 67.8 px | 0.38 | 2.44 | 184 |
| stroke 3 | 31 % → 54 % | 105.7 px | 0.38 | 1.76 | 185 |
| stroke 4 | 32 % → 57 % | 120.2 px | 0.38 | 1.77 | 182 |
| stroke 5 | 41 % → 66 % | 143.0 px | 0.38 | 1.60 | 210 |
| stroke 6 | 41 % → 67 % | 158.1 px | 0.38 | 1.65 | 187 |
| stroke 7 | 39 % → 63 % | 130.7 px | 0.38 | 1.63 | 193 |
| stroke 8 | 39 % → 65 % | 147.7 px | 0.38 | 1.68 | 191 |
| stroke 9 | 39 % → 64 % | 134.6 px | 0.38 | 1.66 | 203 |
| stroke 10 | 39 % → 63 % | 143.8 px | 0.37 | 1.63 | 237 |
| stroke 11 | 41 % → 66 % | 147.3 px | 0.38 | 1.61 | 177 |
| stroke 12 | 39 % → 67 % | 148.5 px | 0.38 | 1.70 | 186 |
| stroke 13 | 40 % → 69 % | 141.8 px | 0.38 | 1.71 | 179 |
| stroke 14 | 38 % → 64 % | 139.1 px | 0.38 | 1.68 | 230 |
| stroke 15 | 41 % → 68 % | 141.2 px | 0.38 | 1.64 | 178 |
| stroke 16 | 40 % → 66 % | 143.5 px | 0.38 | 1.66 | 168 |
| stroke 17 | 39 % → 64 % | 131.8 px | 0.38 | 1.64 | 195 |
| stroke 18 | 42 % → 69 % | 160.9 px | 0.38 | 1.64 | 200 |
| stroke 19 | 41 % → 63 % | 143.3 px | 0.37 | 1.53 | 273 |
| stroke 20 | 42 % → 57 % | 149.6 px | 0.37 | 1.35 | 203 |
| stroke 21 | 48 % → 57 % | 142.8 px | 0.37 | 1.19 | 193 |
| stroke 22 | 56 % → 56 % | 152.7 px | 0.37 | 0.99 | 181 |

Numbers say: wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #15 Ultramarine brush script — own sheet
own sheet 600 × 600 · Ink · 4 px · 12.3 s

![Brush Artist · Refs · #15 Ultramarine brush script — own sheet](Brush-Artist-Refs-15-Ultramarine-brush-script-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 40 % → 42 % | 8.9 px | 0.66 | 1.05 | 71 |
| stroke 2 | 40 % → 42 % | 8.9 px | 0.66 | 1.06 | 72 |
| stroke 3 | 40 % → 42 % | 9.5 px | 0.74 | 1.06 | 34 |
| stroke 4 | 42 % → 45 % | 10.1 px | 0.74 | 1.08 | 20 |
| stroke 5 | 44 % → 48 % | 9.7 px | 0.73 | 1.08 | 50 |
| stroke 6 | 42 % → 44 % | 9.5 px | 0.65 | 1.05 | 77 |
| stroke 7 | 43 % → 47 % | 9.2 px | 0.72 | 1.08 | 47 |
| stroke 8 | 38 % → 41 % | 9.3 px | 0.68 | 1.05 | 74 |
| stroke 9 | 40 % → 42 % | 9.2 px | 0.69 | 1.06 | 80 |
| stroke 10 | 36 % → 38 % | 9.9 px | 0.68 | 1.05 | 75 |
| stroke 11 | 42 % → 45 % | 9.6 px | 0.70 | 1.06 | 68 |
| stroke 12 | 39 % → 41 % | 9.4 px | 0.66 | 1.05 | 56 |
| stroke 13 | 45 % → 48 % | 10.2 px | 0.71 | 1.06 | 40 |
| stroke 14 | 38 % → 41 % | 9.9 px | 0.73 | 1.07 | 30 |
| stroke 15 | 37 % → 39 % | 9.1 px | 0.69 | 1.06 | 60 |
| stroke 16 | 42 % → 45 % | 9.4 px | 0.72 | 1.06 | 53 |
| stroke 17 | 41 % → 44 % | 7.1 px | 0.71 | 1.08 | 63 |
| stroke 18 | 43 % → 45 % | 9.2 px | 0.73 | 1.06 | 28 |
| stroke 19 | 39 % → 41 % | 8.9 px | 0.66 | 1.05 | 79 |
| stroke 20 | 41 % → 43 % | 9.4 px | 0.71 | 1.06 | 55 |
| stroke 21 | 40 % → 43 % | 9.9 px | 0.70 | 1.06 | 54 |
| stroke 22 | 42 % → 44 % | 8.5 px | 0.65 | 1.05 | 71 |
| stroke 23 | 40 % → 43 % | 10.1 px | 0.73 | 1.07 | 35 |
| stroke 24 | 38 % → 41 % | 8.8 px | 0.73 | 1.07 | 50 |
| stroke 25 | 41 % → 43 % | 9.8 px | 0.72 | 1.07 | 46 |
| stroke 26 | 46 % → 49 % | 9.3 px | 0.68 | 1.05 | 58 |
| stroke 27 | 43 % → 45 % | 8.8 px | 0.63 | 1.05 | 72 |
| stroke 28 | 44 % → 46 % | 9.1 px | 0.70 | 1.06 | 47 |
| stroke 29 | 36 % → 39 % | 10.6 px | 0.72 | 1.08 | 31 |
| stroke 30 | 39 % → 41 % | 8.7 px | 0.71 | 1.04 | 61 |
| stroke 31 | 43 % → 46 % | 10.3 px | 0.75 | 1.07 | 35 |
| stroke 32 | 42 % → 46 % | 9.5 px | 0.73 | 1.09 | 29 |
| stroke 33 | 35 % → 38 % | 10.9 px | 0.72 | 1.08 | 28 |
| stroke 34 | 40 % → 43 % | 9.8 px | 0.73 | 1.08 | 32 |
| stroke 35 | 36 % → 37 % | 9.4 px | 0.65 | 1.05 | 62 |

## Brush Artist · Refs · #18 Blue oil-stick scribbles — own sheet
own sheet 600 × 600 · Pastel · 10 px · 5.0 s

![Brush Artist · Refs · #18 Blue oil-stick scribbles — own sheet](Brush-Artist-Refs-18-Blue-oil-stick-scribbles-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 15 % → 31 % | 3.8 px | 0.49 | 2.11 | 206 |
| stroke 2 | 13 % → 37 % | 3.6 px | 0.49 | 2.73 | 303 |
| stroke 3 | 16 % → 26 % | 5.8 px | 0.49 | 1.66 | 381 |
| stroke 4 | 15 % → 29 % | 8.0 px | 0.49 | 1.88 | 394 |
| stroke 5 | 29 % → 34 % | 8.4 px | 0.49 | 1.19 | 331 |
| stroke 6 | 25 % → 26 % | 9.4 px | 0.49 | 1.02 | 235 |
| stroke 7 | 26 % → 32 % | 8.3 px | 0.49 | 1.24 | 291 |
| stroke 8 | 30 % → 30 % | 17.0 px | 0.49 | 1.00 | 304 |

Numbers say: wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #20 Orange-red crayon scribble — own sheet
own sheet 600 × 600 · Pastel · 14 px · 3.6 s

![Brush Artist · Refs · #20 Orange-red crayon scribble — own sheet](Brush-Artist-Refs-20-Orange-red-crayon-scribble-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 8 % → 18 % | 5.5 px | 0.59 | 2.46 | 243 |
| stroke 2 | 9 % → 23 % | 6.8 px | 0.59 | 2.48 | 241 |
| stroke 3 | 13 % → 21 % | 8.5 px | 0.59 | 1.64 | 193 |
| stroke 4 | 24 % → 32 % | 8.9 px | 0.59 | 1.34 | 246 |
| stroke 5 | 27 % → 27 % | 7.7 px | 0.59 | 1.00 | 193 |
| stroke 6 | 22 % → 22 % | 16.8 px | 0.59 | 1.00 | 248 |

Numbers say: wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #21 Gritty black contours — own sheet
own sheet 600 × 600 · Gouache · 12 px · 5.5 s

![Brush Artist · Refs · #21 Gritty black contours — own sheet](Brush-Artist-Refs-21-Gritty-black-contours-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 4 % → 5 % | 4.7 px | 0.37 | 1.13 | 210 |
| stroke 2 | 4 % → 3 % | 7.3 px | 0.37 | 0.60 | 236 |
| stroke 3 | 7 % → 4 % | 6.2 px | 0.37 | 0.56 | 152 |
| stroke 4 | 9 % → 4 % | 10.7 px | 0.37 | 0.51 | 179 |
| stroke 5 | 10 % → 4 % | 12.7 px | 0.37 | 0.42 | 107 |

## Brush Artist · Refs · #22 Bold black brush poster — own sheet
own sheet 600 × 600 · Ink · 20 px · 7.2 s

![Brush Artist · Refs · #22 Bold black brush poster — own sheet](Brush-Artist-Refs-22-Bold-black-brush-poster-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 22 % → 27 % | 36.4 px | 0.94 | 1.20 | 141 |
| stroke 2 | 27 % → 37 % | 41.5 px | 0.95 | 1.36 | 28 |
| stroke 3 | 28 % → 28 % | 43.6 px | 0.95 | 1.00 | 53 |
| stroke 4 | 27 % → 39 % | 53.8 px | 0.94 | 1.42 | 71 |
| stroke 5 | 25 % → 25 % | 43.0 px | 0.94 | 1.00 | 115 |

## Brush Artist · Refs · #23 Dry white on orange + black line — own sheet
own sheet 600 × 600 · Gouache · 50 px · 11.4 s

![Brush Artist · Refs · #23 Dry white on orange + black line — own sheet](Brush-Artist-Refs-23-Dry-white-on-orange-black-line-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 5 % → 10 % | 18.7 px | 0.42 | 1.89 | 174 |
| stroke 2 | 7 % → 9 % | 24.3 px | 0.42 | 1.35 | 207 |
| stroke 3 | 10 % → 10 % | 39.0 px | 0.42 | 0.92 | 189 |
| stroke 4 | 12 % → 11 % | 45.8 px | 0.42 | 0.95 | 189 |
| stroke 5 | 17 % → 14 % | 60.0 px | 0.42 | 0.82 | 196 |
| stroke 6 | 17 % → 15 % | 70.6 px | 0.42 | 0.86 | 200 |
| stroke 7 | 14 % → 14 % | 52.6 px | 0.41 | 1.00 | 193 |
| stroke 8 | 14 % → 13 % | 55.2 px | 0.41 | 0.91 | 219 |
| stroke 9 | 15 % → 14 % | 54.3 px | 0.41 | 0.93 | 192 |
| stroke 10 | 14 % → 14 % | 56.6 px | 0.41 | 0.97 | 189 |
| stroke 11 | 16 % → 15 % | 60.6 px | 0.41 | 0.92 | 196 |
| stroke 12 | 16 % → 15 % | 63.4 px | 0.41 | 0.94 | 213 |
| stroke 13 | 17 % → 16 % | 61.2 px | 0.41 | 0.97 | 234 |
| stroke 14 | 16 % → 16 % | 63.9 px | 0.41 | 0.97 | 344 |
| stroke 15 | 16 % → 14 % | 59.9 px | 0.41 | 0.87 | 298 |
| stroke 16 | 15 % → 12 % | 61.4 px | 0.41 | 0.78 | 286 |
| stroke 17 | 16 % → 11 % | 56.7 px | 0.41 | 0.68 | 274 |
| stroke 18 | 19 % → 11 % | 69.3 px | 0.41 | 0.60 | 237 |

Numbers say: wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #24 Picasso flat oil — own sheet
own sheet 600 × 600 · Oil · 34 px · 9.4 s

![Brush Artist · Refs · #24 Picasso flat oil — own sheet](Brush-Artist-Refs-24-Picasso-flat-oil-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 17 % → 46 % | 35.6 px | 0.23 | 2.73 | 202 |
| stroke 2 | 21 % → 49 % | 48.5 px | 0.24 | 2.38 | 274 |
| stroke 3 | 29 % → 60 % | 64.2 px | 0.23 | 2.05 | 300 |
| stroke 4 | 38 % → 66 % | 85.1 px | 0.23 | 1.75 | 291 |
| stroke 5 | 44 % → 72 % | 97.2 px | 0.23 | 1.63 | 269 |
| stroke 6 | 45 % → 67 % | 104.5 px | 0.23 | 1.50 | 252 |
| stroke 7 | 46 % → 68 % | 97.4 px | 0.23 | 1.46 | 220 |
| stroke 8 | 45 % → 68 % | 109.1 px | 0.23 | 1.51 | 266 |
| stroke 9 | 38 % → 64 % | 83.4 px | 0.23 | 1.69 | 201 |
| stroke 10 | 40 % → 63 % | 95.6 px | 0.23 | 1.58 | 166 |
| stroke 11 | 38 % → 62 % | 81.6 px | 0.23 | 1.62 | 169 |
| stroke 12 | 40 % → 63 % | 94.7 px | 0.23 | 1.60 | 202 |
| stroke 13 | 40 % → 70 % | 87.1 px | 0.23 | 1.76 | 216 |
| stroke 14 | 41 % → 71 % | 92.4 px | 0.23 | 1.74 | 174 |
| stroke 15 | 41 % → 64 % | 86.1 px | 0.23 | 1.58 | 232 |
| stroke 16 | 39 % → 56 % | 91.3 px | 0.23 | 1.43 | 206 |
| stroke 17 | 45 % → 50 % | 93.3 px | 0.23 | 1.12 | 210 |
| stroke 18 | 44 % → 44 % | 106.7 px | 0.23 | 1.00 | 185 |

Numbers say: wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #25 Yellow heavy flat stroke — own sheet
own sheet 600 × 600 · Heavy acrylic · 110 px · 4.1 s

![Brush Artist · Refs · #25 Yellow heavy flat stroke — own sheet](Brush-Artist-Refs-25-Yellow-heavy-flat-stroke-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 19 % → 19 % | 110.5 px | 0.18 | 0.98 | 948 |

## Brush Artist · Refs · #27 Orange impasto swatch — own sheet
own sheet 600 × 600 · Heavy acrylic · 60 px · 5.7 s

![Brush Artist · Refs · #27 Orange impasto swatch — own sheet](Brush-Artist-Refs-27-Orange-impasto-swatch-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 9 % → 29 % | 68.9 px | 0.35 | 3.19 | 90 |
| stroke 2 | 8 % → 41 % | 72.3 px | 0.34 | 4.94 | 71 |
| stroke 3 | 29 % → 45 % | 285.3 px | 0.35 | 1.52 | 45 |
| stroke 4 | 11 % → 15 % | 77.4 px | 0.34 | 1.39 | 80 |
| stroke 5 | 17 % → 33 % | 63.6 px | 0.33 | 1.90 | 115 |
| stroke 6 | 20 % → 40 % | 166.9 px | 0.34 | 1.96 | 73 |
| stroke 7 | 9 % → 18 % | 80.4 px | 0.34 | 2.03 | 59 |
| stroke 8 | 38 % → 44 % | 387.7 px | 0.34 | 1.16 | 56 |
| stroke 9 | 40 % → 40 % | 195.9 px | 0.34 | 1.00 | 99 |
| stroke 10 | 36 % → 38 % | 330.2 px | 0.33 | 1.03 | 63 |

Numbers say: wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #28 Miles Davis black lines — own sheet
own sheet 600 × 600 · Ink · 22 px · 8.7 s

![Brush Artist · Refs · #28 Miles Davis black lines — own sheet](Brush-Artist-Refs-28-Miles-Davis-black-lines-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 22 % → 32 % | 36.6 px | 0.88 | 1.42 | 232 |
| stroke 2 | 28 % → 49 % | 38.3 px | 0.88 | 1.73 | 154 |
| stroke 3 | 39 % → 44 % | 75.1 px | 0.88 | 1.12 | 138 |
| stroke 4 | 42 % → 48 % | 83.7 px | 0.88 | 1.15 | 219 |
| stroke 5 | 55 % → 55 % | 109.9 px | 0.88 | 1.00 | 149 |

Numbers say: wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #29 Shrigley magenta asterisk — own sheet
own sheet 600 × 600 · Watercolor · 70 px · 8.9 s

![Brush Artist · Refs · #29 Shrigley magenta asterisk — own sheet](Brush-Artist-Refs-29-Shrigley-magenta-asterisk-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 13 % → 37 % | 46.6 px | 0.72 | 2.85 | 224 |
| stroke 2 | 12 % → 12 % | 87.1 px | 0.71 | 1.00 | 265 |
| stroke 3 | 28 % → 37 % | 100.9 px | 0.72 | 1.31 | 302 |
| stroke 4 | 23 % → 23 % | 163.9 px | 0.71 | 1.02 | 281 |

Numbers say: wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #30 Red gouache face patch — own sheet
own sheet 600 × 600 · Gouache · 60 px · 18.1 s

![Brush Artist · Refs · #30 Red gouache face patch — own sheet](Brush-Artist-Refs-30-Red-gouache-face-patch-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 12 % → 37 % | 51.5 px | 0.53 | 3.22 | 213 |
| stroke 2 | 15 % → 40 % | 74.6 px | 0.53 | 2.72 | 272 |
| stroke 3 | 24 % → 50 % | 116.0 px | 0.53 | 2.06 | 273 |
| stroke 4 | 27 % → 51 % | 134.1 px | 0.53 | 1.93 | 283 |
| stroke 5 | 34 % → 60 % | 159.9 px | 0.53 | 1.77 | 276 |
| stroke 6 | 35 % → 61 % | 178.3 px | 0.53 | 1.76 | 292 |
| stroke 7 | 34 % → 59 % | 160.9 px | 0.54 | 1.73 | 317 |
| stroke 8 | 34 % → 56 % | 162.5 px | 0.53 | 1.65 | 301 |
| stroke 9 | 36 % → 60 % | 173.1 px | 0.53 | 1.66 | 219 |
| stroke 10 | 38 % → 62 % | 196.8 px | 0.53 | 1.63 | 221 |
| stroke 11 | 37 % → 61 % | 182.5 px | 0.53 | 1.66 | 194 |
| stroke 12 | 36 % → 58 % | 178.3 px | 0.53 | 1.62 | 251 |
| stroke 13 | 33 % → 46 % | 156.5 px | 0.53 | 1.39 | 235 |
| stroke 14 | 33 % → 41 % | 157.7 px | 0.53 | 1.25 | 274 |
| stroke 15 | 33 % → 37 % | 153.4 px | 0.53 | 1.12 | 240 |
| stroke 16 | 39 % → 39 % | 184.9 px | 0.53 | 0.99 | 213 |

Numbers say: wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #31 Warhol blotted line — own sheet
own sheet 600 × 600 · Ink · 6 px · 7.8 s

![Brush Artist · Refs · #31 Warhol blotted line — own sheet](Brush-Artist-Refs-31-Warhol-blotted-line-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 21 % → 42 % | 15.8 px | 0.82 | 1.98 | 113 |
| stroke 2 | 17 % → 23 % | 15.9 px | 0.82 | 1.34 | 121 |
| stroke 3 | 24 % → 25 % | 25.1 px | 0.81 | 1.02 | 110 |
| stroke 4 | 31 % → 40 % | 31.9 px | 0.82 | 1.28 | 73 |
| stroke 5 | 35 % → 44 % | 36.4 px | 0.82 | 1.23 | 114 |
| stroke 6 | 32 % → 33 % | 26.7 px | 0.81 | 1.03 | 100 |

Numbers say: wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #32 Thick orange swipes — own sheet
own sheet 600 × 600 · Heavy acrylic · 90 px · 6.5 s

![Brush Artist · Refs · #32 Thick orange swipes — own sheet](Brush-Artist-Refs-32-Thick-orange-swipes-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 15 % → 29 % | 91.7 px | 0.03 | 1.91 | 474 |
| stroke 2 | 28 % → 40 % | 188.8 px | 0.03 | 1.44 | 621 |
| stroke 3 | 30 % → 29 % | 190.2 px | 0.03 | 0.98 | 624 |

Numbers say: wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #33 Red wet-in-wet band — own sheet
own sheet 600 × 600 · Watercolor · 80 px · 12.7 s

![Brush Artist · Refs · #33 Red wet-in-wet band — own sheet](Brush-Artist-Refs-33-Red-wet-in-wet-band-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 23 % → 57 % | 88.2 px | 0.61 | 2.46 | 555 |
| stroke 2 | 30 % → 52 % | 243.9 px | 0.61 | 1.73 | 188 |
| stroke 3 | 37 % → 54 % | 356.6 px | 0.61 | 1.47 | 174 |
| stroke 4 | 42 % → 61 % | 412.6 px | 0.62 | 1.43 | 213 |
| stroke 5 | 42 % → 55 % | 354.2 px | 0.61 | 1.33 | 222 |
| stroke 6 | 42 % → 47 % | 321.5 px | 0.60 | 1.11 | 223 |

Numbers say: wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #34 Magenta oil patches — own sheet
own sheet 600 × 600 · Oil · 60 px · 7.4 s

![Brush Artist · Refs · #34 Magenta oil patches — own sheet](Brush-Artist-Refs-34-Magenta-oil-patches-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 10 % → 46 % | 68.9 px | 0.13 | 4.68 | 150 |
| stroke 2 | 11 % → 32 % | 71.2 px | 0.13 | 3.02 | 97 |
| stroke 3 | 9 % → 40 % | 71.5 px | 0.13 | 4.71 | 104 |
| stroke 4 | 18 % → 25 % | 149.6 px | 0.13 | 1.37 | 78 |
| stroke 5 | 27 % → 39 % | 145.1 px | 0.12 | 1.43 | 178 |
| stroke 6 | 22 % → 41 % | 187.6 px | 0.13 | 1.86 | 177 |
| stroke 7 | 34 % → 40 % | 268.4 px | 0.13 | 1.18 | 137 |
| stroke 8 | 36 % → 43 % | 256.5 px | 0.13 | 1.19 | 187 |
| stroke 9 | 26 % → 28 % | 170.2 px | 0.13 | 1.08 | 211 |
| stroke 10 | 31 % → 31 % | 275.9 px | 0.13 | 1.00 | 139 |
| stroke 11 | 40 % → 40 % | 359.9 px | 0.13 | 1.00 | 149 |
| stroke 12 | 29 % → 29 % | 205.9 px | 0.13 | 1.00 | 140 |

Numbers say: wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #35 Red band with runs — own sheet
own sheet 600 × 600 · Watercolor · 70 px · 7.7 s

![Brush Artist · Refs · #35 Red band with runs — own sheet](Brush-Artist-Refs-35-Red-band-with-runs-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 21 % → 38 % | 77.5 px | 0.46 | 1.84 | 405 |

Numbers say: wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #36 Magenta letters flat brush — own sheet
own sheet 600 × 600 · Gouache · 36 px · 15.1 s

![Brush Artist · Refs · #36 Magenta letters flat brush — own sheet](Brush-Artist-Refs-36-Magenta-letters-flat-brush-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 20 % → 39 % | 59.1 px | 0.50 | 1.95 | 46 |
| stroke 2 | 20 % → 32 % | 46.7 px | 0.50 | 1.59 | 37 |
| stroke 3 | 29 % → 54 % | 86.9 px | 0.50 | 1.86 | 48 |
| stroke 4 | 26 % → 44 % | 51.3 px | 0.50 | 1.67 | 130 |
| stroke 5 | 33 % → 55 % | 96.2 px | 0.50 | 1.67 | 118 |
| stroke 6 | 42 % → 56 % | 242.7 px | 0.50 | 1.33 | 23 |
| stroke 7 | 30 % → 44 % | 56.8 px | 0.50 | 1.45 | 167 |
| stroke 8 | 31 % → 53 % | 98.5 px | 0.50 | 1.68 | 116 |
| stroke 9 | 38 % → 51 % | 158.3 px | 0.50 | 1.33 | 33 |
| stroke 10 | 37 % → 64 % | 106.7 px | 0.50 | 1.72 | 96 |
| stroke 11 | 39 % → 62 % | 225.8 px | 0.50 | 1.58 | 19 |
| stroke 12 | 43 % → 56 % | 81.9 px | 0.50 | 1.29 | 157 |
| stroke 13 | 33 % → 46 % | 117.7 px | 0.50 | 1.43 | 43 |
| stroke 14 | 35 % → 52 % | 134.5 px | 0.50 | 1.47 | 42 |
| stroke 15 | 38 % → 56 % | 108.6 px | 0.50 | 1.49 | 106 |
| stroke 16 | 41 % → 50 % | 232.0 px | 0.50 | 1.23 | 28 |
| stroke 17 | 44 % → 52 % | 81.7 px | 0.50 | 1.19 | 180 |
| stroke 18 | 27 % → 36 % | 97.6 px | 0.50 | 1.35 | 39 |
| stroke 19 | 40 % → 39 % | 117.2 px | 0.50 | 0.96 | 38 |
| stroke 20 | 45 % → 45 % | 132.3 px | 0.50 | 0.99 | 38 |
| stroke 21 | 41 % → 39 % | 78.7 px | 0.50 | 0.96 | 94 |

Numbers say: wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #37 Oil still life dabs — own sheet
own sheet 600 × 600 · Oil · 40 px · 6.2 s

![Brush Artist · Refs · #37 Oil still life dabs — own sheet](Brush-Artist-Refs-37-Oil-still-life-dabs-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 8 % → 8 % | 50.5 px | 0.39 | 1.01 | 32 |
| stroke 2 | 7 % → 30 % | 52.7 px | 0.39 | 4.05 | 38 |
| stroke 3 | 14 % → 39 % | 109.5 px | 0.39 | 2.81 | 20 |
| stroke 4 | 10 % → 10 % | 47.7 px | 0.39 | 1.01 | 64 |
| stroke 5 | 7 % → 13 % | 51.7 px | 0.39 | 1.78 | 28 |
| stroke 6 | 14 % → 33 % | 90.8 px | 0.39 | 2.32 | 49 |
| stroke 7 | 13 % → 29 % | 144.0 px | 0.39 | 2.16 | 20 |
| stroke 8 | 11 % → 18 % | 117.7 px | 0.39 | 1.62 | 15 |
| stroke 9 | 15 % → 17 % | 79.1 px | 0.38 | 1.09 | 44 |
| stroke 10 | 23 % → 29 % | 117.3 px | 0.38 | 1.28 | 57 |
| stroke 11 | 27 % → 33 % | 223.3 px | 0.39 | 1.23 | 25 |
| stroke 12 | 23 % → 25 % | 253.7 px | 0.39 | 1.07 | 21 |
| stroke 13 | 19 % → 19 % | 189.1 px | 0.40 | 1.01 | 16 |
| stroke 14 | 20 % → 20 % | 163.8 px | 0.39 | 1.01 | 19 |

Numbers say: wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #38 Sanguine drawing — own sheet
own sheet 600 × 600 · Pastel · 6 px · 3.9 s

![Brush Artist · Refs · #38 Sanguine drawing — own sheet](Brush-Artist-Refs-38-Sanguine-drawing-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 3 % → 14 % | 2.9 px | 0.57 | 5.29 | 7 |
| stroke 2 | 3 % → 7 % | 2.9 px | 0.57 | 2.89 | 13 |
| stroke 3 | 3 % → 9 % | 2.9 px | 0.57 | 3.40 | 7 |
| stroke 4 | 2 % → 17 % | 2.7 px | 0.57 | 7.20 | 10 |
| stroke 5 | 2 % → 7 % | 2.7 px | 0.57 | 3.03 | 6 |
| stroke 6 | 3 % → 19 % | 3.4 px | 0.57 | 6.31 | 6 |
| stroke 7 | 5 % → 14 % | 5.2 px | 0.57 | 3.07 | 6 |
| stroke 8 | 4 % → 16 % | 4.7 px | 0.57 | 3.79 | 14 |
| stroke 9 | 3 % → 7 % | 2.9 px | 0.57 | 2.66 | 8 |
| stroke 10 | 4 % → 16 % | 4.7 px | 0.57 | 3.83 | 12 |
| stroke 11 | 3 % → 4 % | 2.9 px | 0.57 | 1.61 | 16 |
| stroke 12 | 4 % → 15 % | 4.8 px | 0.57 | 3.58 | 6 |
| stroke 13 | 8 % → 17 % | 8.9 px | 0.57 | 2.23 | 6 |
| stroke 14 | 4 % → 14 % | 4.9 px | 0.57 | 3.19 | 10 |
| stroke 15 | 9 % → 18 % | 10.7 px | 0.57 | 1.86 | 12 |
| stroke 16 | 6 % → 16 % | 6.6 px | 0.57 | 2.71 | 6 |
| stroke 17 | 4 % → 9 % | 4.4 px | 0.57 | 2.25 | 14 |
| stroke 18 | 3 % → 5 % | 2.9 px | 0.57 | 1.85 | 6 |
| stroke 19 | 6 % → 16 % | 6.9 px | 0.57 | 2.68 | 8 |
| stroke 20 | 8 % → 14 % | 9.2 px | 0.57 | 1.70 | 7 |
| stroke 21 | 4 % → 4 % | 4.3 px | 0.57 | 1.00 | 6 |
| stroke 22 | 8 % → 13 % | 8.6 px | 0.57 | 1.79 | 6 |
| stroke 23 | 7 % → 12 % | 8.3 px | 0.57 | 1.61 | 6 |
| stroke 24 | 4 % → 7 % | 4.7 px | 0.57 | 1.71 | 10 |
| stroke 25 | 8 % → 14 % | 8.7 px | 0.57 | 1.84 | 7 |
| stroke 26 | 6 % → 8 % | 6.5 px | 0.57 | 1.34 | 7 |
| stroke 27 | 4 % → 4 % | 4.3 px | 0.57 | 1.10 | 15 |
| stroke 28 | 7 % → 11 % | 8.2 px | 0.57 | 1.59 | 9 |
| stroke 29 | 8 % → 17 % | 8.8 px | 0.57 | 2.21 | 24 |
| stroke 30 | 13 % → 17 % | 14.9 px | 0.57 | 1.29 | 13 |
| stroke 31 | 5 % → 6 % | 5.4 px | 0.57 | 1.29 | 9 |
| stroke 32 | 10 % → 13 % | 11.8 px | 0.57 | 1.24 | 19 |
| stroke 33 | 7 % → 8 % | 8.5 px | 0.57 | 1.07 | 12 |
| stroke 34 | 11 % → 14 % | 12.0 px | 0.57 | 1.36 | 9 |
| stroke 35 | 9 % → 14 % | 10.0 px | 0.57 | 1.61 | 16 |
| stroke 36 | 10 % → 13 % | 11.4 px | 0.57 | 1.26 | 12 |
| stroke 37 | 9 % → 16 % | 10.5 px | 0.57 | 1.71 | 17 |
| stroke 38 | 13 % → 19 % | 14.8 px | 0.57 | 1.48 | 10 |
| stroke 39 | 14 % → 17 % | 15.7 px | 0.57 | 1.21 | 14 |
| stroke 40 | 6 % → 7 % | 7.2 px | 0.57 | 1.14 | 12 |
| stroke 41 | 16 % → 16 % | 17.7 px | 0.57 | 1.01 | 12 |
| stroke 42 | 14 % → 16 % | 15.2 px | 0.57 | 1.17 | 10 |
| stroke 43 | 10 % → 12 % | 11.6 px | 0.57 | 1.17 | 12 |
| stroke 44 | 12 % → 15 % | 14.3 px | 0.57 | 1.22 | 13 |
| stroke 45 | 2 % → 2 % | 2.7 px | 0.57 | 1.00 | 14 |
| stroke 46 | 16 % → 16 % | 18.5 px | 0.57 | 1.00 | 9 |
| stroke 47 | 13 % → 13 % | 15.0 px | 0.57 | 1.00 | 14 |
| stroke 48 | 12 % → 13 % | 14.3 px | 0.57 | 1.07 | 10 |
| stroke 49 | 19 % → 19 % | 21.5 px | 0.57 | 1.00 | 14 |
| stroke 50 | 10 % → 10 % | 11.6 px | 0.57 | 1.00 | 10 |

Numbers say: wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #39 Very thick impasto — own sheet
own sheet 600 × 600 · Heavy acrylic · 60 px · 7.6 s

![Brush Artist · Refs · #39 Very thick impasto — own sheet](Brush-Artist-Refs-39-Very-thick-impasto-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 27 % → 39 % | 61.5 px | 0.43 | 1.45 | 434 |
| stroke 2 | 32 % → 50 % | 96.9 px | 0.44 | 1.56 | 400 |
| stroke 3 | 38 % → 52 % | 128.8 px | 0.44 | 1.35 | 337 |
| stroke 4 | 32 % → 46 % | 93.6 px | 0.44 | 1.43 | 349 |
| stroke 5 | 43 % → 43 % | 108.0 px | 0.44 | 0.99 | 354 |

Numbers say: wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #40 Watercolour blooms — own sheet
own sheet 600 × 600 · Watercolor · 90 px · 9.0 s

![Brush Artist · Refs · #40 Watercolour blooms — own sheet](Brush-Artist-Refs-40-Watercolour-blooms-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 21 % → 25 % | 92.4 px | 0.13 | 1.20 | 957 |

## Brush Artist · Refs · #41 Coloured pencil hatching — own sheet
own sheet 600 × 600 · Pastel · 4 px · 3.6 s

![Brush Artist · Refs · #41 Coloured pencil hatching — own sheet](Brush-Artist-Refs-41-Coloured-pencil-hatching-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 3 % → 13 % | 2.2 px | 0.35 | 4.64 | 8 |
| stroke 2 | 3 % → 7 % | 2.3 px | 0.35 | 2.29 | 7 |
| stroke 3 | 2 % → 11 % | 1.9 px | 0.35 | 4.38 | 11 |
| stroke 4 | 3 % → 19 % | 2.1 px | 0.35 | 6.73 | 9 |
| stroke 5 | 4 % → 7 % | 2.9 px | 0.35 | 1.83 | 7 |
| stroke 6 | 3 % → 13 % | 2.3 px | 0.35 | 4.19 | 5 |
| stroke 7 | 3 % → 15 % | 2.6 px | 0.35 | 4.43 | 5 |
| stroke 8 | 3 % → 12 % | 2.1 px | 0.35 | 4.20 | 5 |
| stroke 9 | 5 % → 11 % | 3.6 px | 0.35 | 2.27 | 7 |
| stroke 10 | 5 % → 15 % | 3.8 px | 0.35 | 2.99 | 5 |
| stroke 11 | 4 % → 13 % | 3.0 px | 0.35 | 3.28 | 6 |
| stroke 12 | 3 % → 3 % | 2.1 px | 0.35 | 1.00 | 7 |
| stroke 13 | 7 % → 17 % | 5.2 px | 0.35 | 2.45 | 12 |
| stroke 14 | 3 % → 13 % | 2.4 px | 0.35 | 4.19 | 6 |
| stroke 15 | 6 % → 12 % | 4.4 px | 0.35 | 2.09 | 6 |
| stroke 16 | 7 % → 11 % | 5.1 px | 0.35 | 1.61 | 10 |
| stroke 17 | 3 % → 3 % | 2.1 px | 0.35 | 1.00 | 5 |
| stroke 18 | 5 % → 8 % | 3.6 px | 0.35 | 1.65 | 4 |
| stroke 19 | 5 % → 13 % | 3.8 px | 0.35 | 2.72 | 6 |
| stroke 20 | 5 % → 14 % | 3.7 px | 0.35 | 2.92 | 7 |
| stroke 21 | 4 % → 13 % | 3.2 px | 0.35 | 3.20 | 8 |
| stroke 22 | 9 % → 16 % | 6.8 px | 0.35 | 1.77 | 8 |
| stroke 23 | 9 % → 13 % | 6.5 px | 0.35 | 1.55 | 6 |
| stroke 24 | 6 % → 14 % | 4.7 px | 0.35 | 2.18 | 5 |
| stroke 25 | 5 % → 10 % | 3.5 px | 0.35 | 2.27 | 6 |
| stroke 26 | 3 % → 6 % | 2.7 px | 0.35 | 1.81 | 6 |
| stroke 27 | 3 % → 7 % | 2.3 px | 0.35 | 2.26 | 8 |
| stroke 28 | 6 % → 10 % | 4.5 px | 0.35 | 1.70 | 9 |
| stroke 29 | 3 % → 13 % | 2.4 px | 0.35 | 4.21 | 12 |
| stroke 30 | 6 % → 9 % | 4.4 px | 0.35 | 1.46 | 8 |
| stroke 31 | 7 % → 14 % | 5.1 px | 0.35 | 2.14 | 5 |
| stroke 32 | 3 % → 6 % | 2.5 px | 0.35 | 1.79 | 5 |
| stroke 33 | 6 % → 11 % | 5.0 px | 0.35 | 1.67 | 5 |
| stroke 34 | 3 % → 6 % | 2.6 px | 0.35 | 1.73 | 7 |
| stroke 35 | 7 % → 14 % | 5.0 px | 0.35 | 2.09 | 5 |
| stroke 36 | 5 % → 5 % | 3.7 px | 0.35 | 1.01 | 10 |
| stroke 37 | 7 % → 15 % | 5.2 px | 0.35 | 2.15 | 6 |
| stroke 38 | 8 % → 13 % | 5.8 px | 0.35 | 1.66 | 17 |
| stroke 39 | 7 % → 11 % | 5.1 px | 0.35 | 1.67 | 5 |
| stroke 40 | 8 % → 18 % | 6.2 px | 0.35 | 2.21 | 5 |
| stroke 41 | 9 % → 13 % | 6.9 px | 0.35 | 1.48 | 6 |
| stroke 42 | 10 % → 17 % | 7.7 px | 0.35 | 1.73 | 4 |
| stroke 43 | 5 % → 9 % | 3.9 px | 0.35 | 1.66 | 9 |
| stroke 44 | 10 % → 13 % | 7.3 px | 0.35 | 1.40 | 4 |
| stroke 45 | 13 % → 18 % | 9.9 px | 0.35 | 1.35 | 5 |
| stroke 46 | 5 % → 7 % | 3.6 px | 0.34 | 1.41 | 4 |
| stroke 47 | 11 % → 13 % | 8.0 px | 0.35 | 1.20 | 5 |
| stroke 48 | 12 % → 16 % | 9.2 px | 0.35 | 1.34 | 9 |
| stroke 49 | 6 % → 9 % | 4.2 px | 0.35 | 1.66 | 8 |
| stroke 50 | 7 % → 7 % | 5.2 px | 0.34 | 1.00 | 8 |
| stroke 51 | 8 % → 15 % | 6.4 px | 0.35 | 1.74 | 5 |
| stroke 52 | 12 % → 14 % | 9.1 px | 0.35 | 1.19 | 4 |
| stroke 53 | 11 % → 14 % | 8.1 px | 0.35 | 1.36 | 7 |
| stroke 54 | 10 % → 14 % | 7.4 px | 0.35 | 1.47 | 5 |
| stroke 55 | 11 % → 14 % | 8.2 px | 0.35 | 1.33 | 5 |
| stroke 56 | 11 % → 12 % | 8.4 px | 0.35 | 1.11 | 5 |
| stroke 57 | 9 % → 13 % | 7.1 px | 0.35 | 1.37 | 6 |
| stroke 58 | 10 % → 11 % | 7.7 px | 0.35 | 1.14 | 5 |
| stroke 59 | 11 % → 13 % | 8.4 px | 0.35 | 1.18 | 5 |
| stroke 60 | 16 % → 20 % | 11.9 px | 0.35 | 1.26 | 7 |
| stroke 61 | 19 % → 20 % | 14.5 px | 0.35 | 1.04 | 5 |
| stroke 62 | 10 % → 10 % | 7.3 px | 0.35 | 1.00 | 13 |
| stroke 63 | 11 % → 12 % | 8.7 px | 0.35 | 1.07 | 7 |
| stroke 64 | 14 % → 14 % | 10.7 px | 0.35 | 1.02 | 5 |
| stroke 65 | 15 % → 15 % | 11.5 px | 0.35 | 1.00 | 9 |
| stroke 66 | 14 % → 14 % | 10.7 px | 0.35 | 1.00 | 10 |
| stroke 67 | 12 % → 12 % | 8.8 px | 0.35 | 1.06 | 7 |
| stroke 68 | 5 % → 9 % | 3.6 px | 0.35 | 1.88 | 5 |
| stroke 69 | 5 % → 5 % | 4.1 px | 0.35 | 1.00 | 10 |
| stroke 70 | 10 % → 13 % | 7.4 px | 0.35 | 1.28 | 7 |
| stroke 71 | 9 % → 11 % | 7.1 px | 0.35 | 1.15 | 7 |
| stroke 72 | 5 % → 7 % | 4.2 px | 0.35 | 1.23 | 6 |
| stroke 73 | 12 % → 12 % | 9.3 px | 0.35 | 1.00 | 9 |
| stroke 74 | 14 % → 14 % | 10.8 px | 0.35 | 1.00 | 9 |
| stroke 75 | 15 % → 15 % | 11.4 px | 0.35 | 1.00 | 6 |
| stroke 76 | 14 % → 14 % | 10.5 px | 0.35 | 1.00 | 5 |
| stroke 77 | 7 % → 10 % | 5.4 px | 0.35 | 1.34 | 9 |
| stroke 78 | 9 % → 9 % | 7.0 px | 0.35 | 1.00 | 6 |
| stroke 79 | 7 % → 7 % | 5.7 px | 0.35 | 1.00 | 8 |
| stroke 80 | 11 % → 11 % | 8.3 px | 0.35 | 1.00 | 5 |

Numbers say: wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #42 Oil pastel shaggy — own sheet
own sheet 600 × 600 · Pastel · 18 px · 4.3 s

![Brush Artist · Refs · #42 Oil pastel shaggy — own sheet](Brush-Artist-Refs-42-Oil-pastel-shaggy-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 5 % → 27 % | 8.0 px | 0.28 | 5.73 | 15 |
| stroke 2 | 5 % → 24 % | 8.6 px | 0.28 | 4.69 | 11 |
| stroke 3 | 5 % → 29 % | 8.9 px | 0.28 | 5.42 | 17 |
| stroke 4 | 5 % → 11 % | 8.8 px | 0.28 | 2.08 | 13 |
| stroke 5 | 6 % → 11 % | 9.9 px | 0.28 | 1.85 | 17 |
| stroke 6 | 8 % → 37 % | 13.9 px | 0.29 | 4.44 | 14 |
| stroke 7 | 11 % → 31 % | 17.6 px | 0.28 | 2.90 | 16 |
| stroke 8 | 7 % → 38 % | 11.4 px | 0.28 | 5.55 | 23 |
| stroke 9 | 8 % → 21 % | 13.9 px | 0.28 | 2.53 | 15 |
| stroke 10 | 8 % → 18 % | 13.2 px | 0.28 | 2.32 | 15 |
| stroke 11 | 6 % → 27 % | 9.4 px | 0.28 | 4.74 | 10 |
| stroke 12 | 8 % → 19 % | 13.6 px | 0.28 | 2.29 | 14 |
| stroke 13 | 13 % → 24 % | 21.0 px | 0.28 | 1.92 | 11 |
| stroke 14 | 5 % → 23 % | 7.9 px | 0.28 | 4.77 | 12 |
| stroke 15 | 5 % → 24 % | 9.0 px | 0.29 | 4.38 | 15 |
| stroke 16 | 9 % → 21 % | 15.7 px | 0.29 | 2.18 | 17 |
| stroke 17 | 17 % → 39 % | 27.9 px | 0.29 | 2.34 | 10 |
| stroke 18 | 14 % → 25 % | 22.8 px | 0.29 | 1.79 | 10 |
| stroke 19 | 15 % → 32 % | 24.9 px | 0.28 | 2.09 | 11 |
| stroke 20 | 21 % → 39 % | 35.1 px | 0.28 | 1.85 | 16 |
| stroke 21 | 9 % → 16 % | 14.4 px | 0.28 | 1.88 | 21 |
| stroke 22 | 14 % → 17 % | 23.9 px | 0.28 | 1.20 | 10 |
| stroke 23 | 12 % → 17 % | 20.6 px | 0.29 | 1.34 | 12 |
| stroke 24 | 18 % → 26 % | 30.0 px | 0.29 | 1.44 | 10 |
| stroke 25 | 20 % → 34 % | 32.6 px | 0.28 | 1.74 | 16 |
| stroke 26 | 6 % → 14 % | 9.2 px | 0.28 | 2.43 | 10 |
| stroke 27 | 18 % → 26 % | 30.4 px | 0.29 | 1.41 | 15 |
| stroke 28 | 14 % → 24 % | 23.7 px | 0.28 | 1.68 | 16 |
| stroke 29 | 9 % → 27 % | 14.9 px | 0.29 | 3.01 | 10 |
| stroke 30 | 15 % → 36 % | 24.9 px | 0.29 | 2.43 | 15 |
| stroke 31 | 14 % → 17 % | 23.3 px | 0.28 | 1.23 | 12 |
| stroke 32 | 16 % → 29 % | 27.0 px | 0.29 | 1.82 | 11 |
| stroke 33 | 15 % → 16 % | 24.5 px | 0.29 | 1.09 | 10 |
| stroke 34 | 19 % → 27 % | 31.4 px | 0.28 | 1.44 | 16 |
| stroke 35 | 26 % → 36 % | 42.5 px | 0.28 | 1.40 | 16 |
| stroke 36 | 25 % → 34 % | 41.0 px | 0.28 | 1.36 | 24 |
| stroke 37 | 12 % → 12 % | 19.3 px | 0.28 | 1.03 | 16 |
| stroke 38 | 19 % → 25 % | 31.7 px | 0.28 | 1.30 | 10 |
| stroke 39 | 16 % → 22 % | 27.3 px | 0.28 | 1.37 | 10 |
| stroke 40 | 22 % → 31 % | 36.6 px | 0.28 | 1.38 | 12 |
| stroke 41 | 32 % → 36 % | 53.1 px | 0.28 | 1.12 | 11 |
| stroke 42 | 23 % → 30 % | 38.1 px | 0.29 | 1.29 | 13 |
| stroke 43 | 12 % → 12 % | 20.3 px | 0.28 | 1.00 | 11 |
| stroke 44 | 30 % → 37 % | 48.9 px | 0.28 | 1.26 | 15 |
| stroke 45 | 16 % → 16 % | 26.2 px | 0.28 | 1.00 | 12 |
| stroke 46 | 29 % → 34 % | 47.9 px | 0.29 | 1.15 | 15 |
| stroke 47 | 38 % → 41 % | 62.0 px | 0.28 | 1.10 | 11 |
| stroke 48 | 29 % → 36 % | 47.8 px | 0.29 | 1.27 | 17 |
| stroke 49 | 27 % → 30 % | 45.1 px | 0.29 | 1.11 | 11 |
| stroke 50 | 38 % → 40 % | 63.4 px | 0.28 | 1.06 | 11 |
| stroke 51 | 16 % → 16 % | 26.0 px | 0.28 | 1.00 | 10 |
| stroke 52 | 37 % → 38 % | 62.4 px | 0.29 | 1.01 | 14 |
| stroke 53 | 22 % → 26 % | 36.9 px | 0.28 | 1.18 | 14 |
| stroke 54 | 17 % → 19 % | 29.0 px | 0.29 | 1.09 | 21 |
| stroke 55 | 15 % → 15 % | 25.0 px | 0.28 | 1.00 | 12 |
| stroke 56 | 13 % → 14 % | 21.6 px | 0.28 | 1.08 | 12 |
| stroke 57 | 23 % → 23 % | 37.7 px | 0.29 | 1.00 | 22 |
| stroke 58 | 28 % → 29 % | 46.1 px | 0.28 | 1.05 | 21 |
| stroke 59 | 40 % → 40 % | 67.3 px | 0.28 | 1.00 | 11 |
| stroke 60 | 22 % → 22 % | 35.6 px | 0.28 | 1.00 | 15 |

Numbers say: wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #43 Dragged black ink blocks — own sheet
own sheet 600 × 600 · Gouache · 70 px · 11.0 s

![Brush Artist · Refs · #43 Dragged black ink blocks — own sheet](Brush-Artist-Refs-43-Dragged-black-ink-blocks-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 16 % → 12 % | 37.3 px | 0.46 | 0.73 | 561 |
| stroke 2 | 16 % → 13 % | 58.0 px | 0.46 | 0.78 | 880 |
| stroke 3 | 20 % → 16 % | 72.4 px | 0.46 | 0.79 | 834 |
| stroke 4 | 20 % → 16 % | 70.6 px | 0.46 | 0.77 | 592 |
| stroke 5 | 24 % → 14 % | 56.0 px | 0.46 | 0.57 | 578 |

## Brush Artist · Refs · #44 Blue looping ribbon — own sheet
own sheet 600 × 600 · Oil · 80 px · 8.5 s

![Brush Artist · Refs · #44 Blue looping ribbon — own sheet](Brush-Artist-Refs-44-Blue-looping-ribbon-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 32 % → 32 % | 42.2 px | 0.78 | 1.00 | 4297 |

## Brush Artist · Refs · #45 Soft pastel pepper — own sheet
own sheet 600 × 600 · Pastel · 40 px · 6.2 s

![Brush Artist · Refs · #45 Soft pastel pepper — own sheet](Brush-Artist-Refs-45-Soft-pastel-pepper-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 10 % → 39 % | 11.3 px | 0.48 | 3.73 | 557 |
| stroke 2 | 18 % → 34 % | 21.3 px | 0.49 | 1.86 | 441 |
| stroke 3 | 25 % → 37 % | 17.6 px | 0.49 | 1.45 | 423 |
| stroke 4 | 24 % → 35 % | 30.5 px | 0.49 | 1.42 | 466 |
| stroke 5 | 30 % → 30 % | 21.2 px | 0.49 | 1.00 | 363 |
| stroke 6 | 35 % → 44 % | 22.5 px | 0.48 | 1.25 | 417 |
| stroke 7 | 39 % → 43 % | 21.4 px | 0.48 | 1.10 | 527 |
| stroke 8 | 44 % → 44 % | 44.2 px | 0.48 | 1.00 | 484 |

Numbers say: wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #46 Red-brown ink lips — own sheet
own sheet 600 × 600 · Watercolor · 50 px · 7.6 s

![Brush Artist · Refs · #46 Red-brown ink lips — own sheet](Brush-Artist-Refs-46-Red-brown-ink-lips-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 12 % → 24 % | 51.9 px | 0.59 | 1.91 | 165 |
| stroke 2 | 16 % → 27 % | 68.1 px | 0.54 | 1.74 | 115 |

Numbers say: wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #47 Pink knife slabs — own sheet
own sheet 600 × 600 · Heavy acrylic · 90 px · 6.4 s

![Brush Artist · Refs · #47 Pink knife slabs — own sheet](Brush-Artist-Refs-47-Pink-knife-slabs-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 19 % → 39 % | 97.8 px | 0.11 | 1.98 | 63 |
| stroke 2 | 34 % → 51 % | 195.7 px | 0.11 | 1.48 | 87 |
| stroke 3 | 35 % → 51 % | 196.5 px | 0.11 | 1.48 | 81 |
| stroke 4 | 46 % → 46 % | 196.5 px | 0.11 | 0.99 | 69 |

Numbers say: wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #48 Black bands with drips — own sheet
own sheet 600 × 600 · Watercolor · 70 px · 19.8 s

![Brush Artist · Refs · #48 Black bands with drips — own sheet](Brush-Artist-Refs-48-Black-bands-with-drips-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 32 % → 74 % | 82.1 px | 0.39 | 2.33 | 538 |
| stroke 2 | 49 % → 98 % | 158.5 px | 0.40 | 1.99 | 544 |
| stroke 3 | 53 % → 98 % | 164.4 px | 0.39 | 1.86 | 699 |
| stroke 4 | 55 % → 93 % | 161.2 px | 0.36 | 1.67 | 537 |

Numbers say: wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #49 Magenta letters round brush — own sheet
own sheet 600 × 600 · Ink · 30 px · 13.8 s

![Brush Artist · Refs · #49 Magenta letters round brush — own sheet](Brush-Artist-Refs-49-Magenta-letters-round-brush-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 27 % → 46 % | 64.3 px | 0.52 | 1.69 | 53 |
| stroke 2 | 29 % → 40 % | 52.5 px | 0.53 | 1.39 | 36 |
| stroke 3 | 41 % → 67 % | 96.4 px | 0.52 | 1.64 | 51 |
| stroke 4 | 34 % → 52 % | 53.7 px | 0.52 | 1.55 | 145 |
| stroke 5 | 40 % → 66 % | 94.8 px | 0.52 | 1.65 | 113 |
| stroke 6 | 54 % → 70 % | 231.2 px | 0.52 | 1.29 | 27 |
| stroke 7 | 41 % → 56 % | 63.9 px | 0.52 | 1.35 | 165 |
| stroke 8 | 36 % → 61 % | 91.9 px | 0.53 | 1.72 | 95 |
| stroke 9 | 49 % → 60 % | 152.9 px | 0.53 | 1.24 | 35 |
| stroke 10 | 42 % → 72 % | 100.5 px | 0.52 | 1.71 | 87 |
| stroke 11 | 52 % → 72 % | 219.5 px | 0.52 | 1.39 | 22 |
| stroke 12 | 53 % → 68 % | 82.2 px | 0.52 | 1.29 | 128 |
| stroke 13 | 42 % → 54 % | 116.0 px | 0.53 | 1.29 | 44 |
| stroke 14 | 45 % → 69 % | 131.9 px | 0.53 | 1.52 | 48 |
| stroke 15 | 43 % → 63 % | 102.4 px | 0.52 | 1.46 | 94 |
| stroke 16 | 52 % → 61 % | 220.2 px | 0.52 | 1.18 | 30 |
| stroke 17 | 53 % → 64 % | 82.3 px | 0.52 | 1.19 | 155 |
| stroke 18 | 36 % → 44 % | 99.6 px | 0.52 | 1.21 | 46 |
| stroke 19 | 54 % → 53 % | 123.8 px | 0.52 | 0.99 | 45 |
| stroke 20 | 54 % → 54 % | 125.3 px | 0.52 | 1.00 | 39 |
| stroke 21 | 49 % → 49 % | 81.3 px | 0.52 | 1.00 | 129 |

Numbers say: wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #50 Thick swipes on photo — own sheet
own sheet 600 × 600 · Heavy acrylic · 40 px · 5.6 s

![Brush Artist · Refs · #50 Thick swipes on photo — own sheet](Brush-Artist-Refs-50-Thick-swipes-on-photo-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 10 % → 26 % | 46.9 px | 0.32 | 2.58 | 56 |
| stroke 2 | 10 % → 20 % | 48.1 px | 0.31 | 1.93 | 47 |
| stroke 3 | 11 % → 13 % | 45.4 px | 0.32 | 1.16 | 74 |
| stroke 4 | 12 % → 25 % | 47.6 px | 0.32 | 2.05 | 46 |
| stroke 5 | 12 % → 13 % | 46.0 px | 0.32 | 1.07 | 61 |
| stroke 6 | 19 % → 25 % | 109.7 px | 0.31 | 1.30 | 51 |
| stroke 7 | 24 % → 31 % | 102.1 px | 0.32 | 1.29 | 64 |
| stroke 8 | 24 % → 25 % | 134.5 px | 0.32 | 1.03 | 46 |
| stroke 9 | 12 % → 14 % | 52.6 px | 0.31 | 1.20 | 52 |
| stroke 10 | 26 % → 28 % | 88.4 px | 0.31 | 1.08 | 61 |
| stroke 11 | 9 % → 10 % | 47.2 px | 0.32 | 1.09 | 49 |
| stroke 12 | 18 % → 19 % | 100.0 px | 0.32 | 1.07 | 22 |

Numbers say: wet paint spreads well beyond the stroke.

## Brush Artist · Ink — dry brush — own sheet
own sheet 600 × 600 · Gouache · 30 px · 4.3 s

![Brush Artist · Ink — dry brush — own sheet](Brush-Artist-Ink-dry-brush-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| ear | 6 % → 3 % | 7.8 px | 0.86 | 0.44 | 639 |
| drag0 | 6 % → 8 % | 10.2 px | 0.86 | 1.39 | 185 |
| drag1 | 8 % → 8 % | 16.5 px | 0.86 | 1.02 | 157 |
| drag2 | 10 % → 9 % | 22.5 px | 0.86 | 0.87 | 120 |
| drag3 | 12 % → 9 % | 29.4 px | 0.86 | 0.78 | 102 |

## Brush Artist · Watercolour — blue — own sheet
own sheet 600 × 600 · Watercolor · 40 px · 12.4 s

![Brush Artist · Watercolour — blue — own sheet](Brush-Artist-Watercolour-blue-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| s0 | 7 % → 23 % | 28.4 px | 0.25 | 3.20 | 80 |
| s1 | 5 % → 32 % | 9.9 px | 0.38 | 5.85 | 79 |
| s2 | 10 % → 18 % | 43.5 px | 0.19 | 1.75 | 73 |
| s3 | 9 % → 17 % | 26.3 px | 0.28 | 1.85 | 59 |
| s4 | 14 % → 29 % | 37.9 px | 0.36 | 2.11 | 57 |
| s5 | 19 % → 29 % | 38.9 px | 0.37 | 1.52 | 85 |
| s6 | 17 % → 21 % | 47.6 px | 0.27 | 1.22 | 82 |
| s7 | 24 % → 35 % | 31.9 px | 0.37 | 1.44 | 48 |
| s8 | 20 % → 24 % | 77.5 px | 0.27 | 1.18 | 47 |

Numbers say: wet paint spreads well beyond the stroke.

## Brush Artist · Charcoal — stick — own sheet
own sheet 600 × 600 · Charcoal · 28 px · 1.5 s

![Brush Artist · Charcoal — stick — own sheet](Brush-Artist-Charcoal-stick-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| finger0 | 9 % → 18 % | 15.5 px | 0.83 | 2.01 | 47 |
| tip0 | 8 % → 14 % | 22.1 px | 0.83 | 1.75 | 16 |
| finger1 | 17 % → 29 % | 29.4 px | 0.83 | 1.74 | 35 |
| tip1 | 15 % → 21 % | 39.1 px | 0.83 | 1.42 | 9 |
| finger2 | 17 % → 25 % | 29.5 px | 0.83 | 1.53 | 33 |
| tip2 | 14 % → 20 % | 39.0 px | 0.83 | 1.41 | 11 |
| finger3 | 16 % → 19 % | 29.3 px | 0.83 | 1.16 | 36 |
| tip3 | 15 % → 15 % | 39.0 px | 0.83 | 1.00 | 25 |
| cig0 | 25 % → 35 % | 54.8 px | 0.83 | 1.41 | 14 |
| cig1 | 26 % → 35 % | 58.8 px | 0.83 | 1.32 | 14 |
| cig2 | 28 % → 35 % | 63.2 px | 0.83 | 1.22 | 16 |
| cig3 | 30 % → 34 % | 67.3 px | 0.83 | 1.14 | 13 |
| cig4 | 32 % → 34 % | 71.5 px | 0.83 | 1.06 | 10 |
| cig5 | 34 % → 34 % | 75.3 px | 0.83 | 1.00 | 9 |

Numbers say: wet paint spreads well beyond the stroke.

