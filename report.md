![All brushes](contact.png)

# Brush Lab — 180 brushes · 4 Nov 2026 at 21:29

Every sheet: 1500 × 600, ten strokes in a 5 × 2 grid — 1. light line · 2. heavy line · 3. pressure swell · 4. fast wave · 5. slow wave · 6. spiral · 7. loop · 8. tilted · 9. over the wet one · 10. long, no reload (cell 8 holds «tilted» and «over the wet one» crossed). The CPU reference of Mamay's paint engine; the wet layer settles 20 s at the end.

Columns: **covered** = share of the cell with paint right after the stroke → after settling; **width** = painted area of the stroke ÷ its length (px); **dark** = mean darkness of the painted pixels above the paper's own grain (0 = paper, 1 = black); **spread** = how far wet paint went beyond the stroke (1.0 = stayed); **ms** = the stroke on the CPU; long stroke: paint in each quarter of its length (it should run out: wet → streaks → dry tail).

## Ink Line
Ink · 12 px · 25.3 s

![Ink Line](Ink-Line.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 1 % → 4 % | 4.3 px | 0.55 | 2.45 | 36 |
| heavy line | 5 % → 6 % | 15.7 px | 0.68 | 1.14 | 61 |
| pressure swell | 3 % → 4 % | 11.3 px | 0.64 | 1.40 | 31 |
| fast wave | 10 % → 11 % | 11.2 px | 0.59 | 1.11 | 125 |
| slow wave | 8 % → 10 % | 9.6 px | 0.57 | 1.16 | 134 |
| spiral | 14 % → 15 % | 8.9 px | 0.49 | 1.07 | 210 |
| loop | 8 % → 9 % | 10.6 px | 0.61 | 1.15 | 100 |
| tilted | 5 % → 5 % | 14.3 px | 0.64 | 1.05 | 60 |
| over the wet one | 10 % → 11 % | 12.5 px | 0.64 | 1.15 | 50 |
| long, no reload | 18 % → 17 % | 8.1 px | 0.47 | 0.96 | 331 | quarters: 0.22 → 0.09 → 0.04 → 0.02

Numbers say: light vs heavy: width 4.3 → 15.7 px, dark 0.55 → 0.68; wet paint spreads well beyond the stroke.

## Dense Ink
Ink · 14 px · 25.1 s

![Dense Ink](Dense-Ink.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 5 % → 7 % | 15.2 px | 0.72 | 1.27 | 34 |
| heavy line | 7 % → 7 % | 19.1 px | 0.73 | 1.09 | 79 |
| pressure swell | 5 % → 6 % | 17.9 px | 0.72 | 1.18 | 42 |
| fast wave | 13 % → 13 % | 15.2 px | 0.69 | 1.01 | 134 |
| slow wave | 12 % → 12 % | 13.5 px | 0.67 | 1.04 | 144 |
| spiral | 18 % → 15 % | 12.2 px | 0.65 | 0.80 | 238 |
| loop | 11 % → 12 % | 14.8 px | 0.69 | 1.08 | 134 |
| tilted | 5 % → 6 % | 14.5 px | 0.72 | 1.07 | 83 |
| over the wet one | 12 % → 13 % | 17.7 px | 0.72 | 1.12 | 62 |
| long, no reload | 23 % → 15 % | 10.1 px | 0.64 | 0.66 | 340 | quarters: 0.30 → 0.12 → 0.04 → 0.02

Numbers say: light vs heavy: width 15.2 → 19.1 px, dark 0.72 → 0.73.

## Transparent Wash
Watercolor · 22 px · 25.9 s

![Transparent Wash](Transparent-Wash.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 2 % → 5 % | 6.9 px | 0.27 | 2.26 | 56 |
| heavy line | 7 % → 9 % | 20.4 px | 0.27 | 1.23 | 63 |
| pressure swell | 4 % → 6 % | 15.2 px | 0.28 | 1.54 | 27 |
| fast wave | 14 % → 16 % | 16.1 px | 0.20 | 1.17 | 126 |
| slow wave | 12 % → 15 % | 13.7 px | 0.21 | 1.28 | 187 |
| spiral | 18 % → 22 % | 11.9 px | 0.16 | 1.22 | 162 |
| loop | 11 % → 13 % | 14.5 px | 0.22 | 1.20 | 85 |
| tilted | 8 % → 8 % | 21.1 px | 0.24 | 1.06 | 68 |
| over the wet one | 13 % → 16 % | 16.4 px | 0.24 | 1.19 | 47 |
| long, no reload | 26 % → 32 % | 11.6 px | 0.13 | 1.22 | 340 | quarters: 0.11 → 0.04 → 0.02 → 0.01

Numbers say: light vs heavy: width 6.9 → 20.4 px, dark 0.27 → 0.27; wet paint spreads well beyond the stroke.

## Dry Brush
Gouache · 24 px · 24.8 s

![Dry Brush](Dry-Brush.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 5 % → 1 % | 13.8 px | 0.65 | 0.11 | 78 |
| heavy line | 6 % → 0 % | 18.4 px | 0.65 | 0.02 | 77 |
| pressure swell | 5 % → 0 % | 18.1 px | 0.65 | 0.09 | 43 |
| fast wave | 6 % → 1 % | 6.9 px | 0.65 | 0.08 | 158 |
| slow wave | 7 % → 0 % | 7.8 px | 0.65 | 0.07 | 239 |
| spiral | 7 % → 1 % | 4.4 px | 0.65 | 0.08 | 225 |
| loop | 9 % → 0 % | 12.2 px | 0.65 | 0.05 | 145 |
| tilted | 4 % → 3 % | 10.3 px | 0.65 | 0.89 | 79 |
| over the wet one | 9 % → 1 % | 14.3 px | 0.65 | 0.12 | 59 |
| long, no reload | 6 % → 1 % | 2.7 px | 0.65 | 0.15 | 307 | quarters: 0.12 → 0.00 → 0.00 → 0.00

Numbers say: light vs heavy: width 13.8 → 18.4 px, dark 0.65 → 0.65.

## Wax Crayon
Wax · 8 px · 9.8 s

![Wax Crayon](Wax-Crayon.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 1 % → 1 % | 2.5 px | 0.71 | 1.00 | 22 |
| heavy line | 1 % → 1 % | 3.9 px | 0.69 | 1.00 | 18 |
| pressure swell | 1 % → 1 % | 3.3 px | 0.70 | 1.00 | 16 |
| fast wave | 3 % → 3 % | 3.5 px | 0.69 | 1.00 | 43 |
| slow wave | 3 % → 3 % | 3.4 px | 0.70 | 1.00 | 45 |
| spiral | 5 % → 5 % | 3.3 px | 0.70 | 1.00 | 80 |
| loop | 3 % → 3 % | 3.3 px | 0.70 | 1.00 | 42 |
| tilted | 2 % → 2 % | 5.6 px | 0.68 | 1.00 | 28 |
| over the wet one | 3 % → 3 % | 3.6 px | 0.68 | 1.00 | 20 |
| long, no reload | 7 % → 7 % | 3.3 px | 0.70 | 1.00 | 113 | quarters: 0.06 → 0.06 → 0.06 → 0.06

Numbers say: light vs heavy: width 2.5 → 3.9 px, dark 0.71 → 0.69; the long stroke does not run out of paint.

## Oil Pastel
Wax · 12 px · 10.0 s

![Oil Pastel](Oil-Pastel.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 1 % → 1 % | 4.0 px | 0.68 | 1.00 | 32 |
| heavy line | 2 % → 2 % | 6.5 px | 0.68 | 1.00 | 33 |
| pressure swell | 2 % → 2 % | 5.7 px | 0.69 | 1.00 | 26 |
| fast wave | 5 % → 5 % | 5.7 px | 0.68 | 1.00 | 65 |
| slow wave | 5 % → 5 % | 5.5 px | 0.68 | 1.00 | 45 |
| spiral | 8 % → 8 % | 5.5 px | 0.68 | 1.00 | 101 |
| loop | 4 % → 4 % | 5.6 px | 0.68 | 1.00 | 78 |
| tilted | 2 % → 2 % | 6.8 px | 0.68 | 1.00 | 30 |
| over the wet one | 5 % → 5 % | 5.8 px | 0.68 | 1.00 | 25 |
| long, no reload | 13 % → 13 % | 5.6 px | 0.68 | 1.00 | 181 | quarters: 0.10 → 0.09 → 0.10 → 0.10

Numbers say: light vs heavy: width 4.0 → 6.5 px, dark 0.68 → 0.68; the long stroke does not run out of paint.

## Charcoal
Charcoal · 5 px · 9.7 s

![Charcoal](Charcoal.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 1 % → 1 % | 2.0 px | 0.74 | 1.00 | 31 |
| heavy line | 1 % → 1 % | 3.0 px | 0.74 | 1.00 | 16 |
| pressure swell | 1 % → 1 % | 2.7 px | 0.74 | 1.00 | 13 |
| fast wave | 2 % → 2 % | 2.7 px | 0.73 | 1.00 | 41 |
| slow wave | 2 % → 2 % | 2.6 px | 0.74 | 1.00 | 29 |
| spiral | 4 % → 4 % | 2.5 px | 0.74 | 1.00 | 44 |
| loop | 2 % → 2 % | 2.6 px | 0.74 | 1.00 | 22 |
| tilted | 2 % → 2 % | 4.3 px | 0.72 | 1.00 | 9 |
| over the wet one | 2 % → 2 % | 2.4 px | 0.72 | 1.00 | 13 |
| long, no reload | 6 % → 6 % | 2.7 px | 0.73 | 1.00 | 114 | quarters: 0.05 → 0.05 → 0.05 → 0.05

Numbers say: light vs heavy: width 2.0 → 3.0 px, dark 0.74 → 0.74; the long stroke does not run out of paint.

## Impasto
Heavy acrylic · 22 px · 14.6 s

![Impasto](Impasto.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 8 % → 8 % | 24.1 px | 0.71 | 0.93 | 105 |
| heavy line | 10 % → 9 % | 28.8 px | 0.69 | 0.94 | 82 |
| pressure swell | 7 % → 7 % | 28.1 px | 0.72 | 0.94 | 42 |
| fast wave | 20 % → 13 % | 23.4 px | 0.71 | 0.64 | 147 |
| slow wave | 21 % → 14 % | 24.5 px | 0.71 | 0.66 | 284 |
| spiral | 30 % → 14 % | 19.9 px | 0.71 | 0.46 | 279 |
| loop | 18 % → 14 % | 23.9 px | 0.71 | 0.77 | 137 |
| tilted | 8 % → 8 % | 21.7 px | 0.70 | 1.00 | 73 |
| over the wet one | 17 % → 15 % | 25.4 px | 0.70 | 0.91 | 49 |
| long, no reload | 33 % → 14 % | 14.9 px | 0.71 | 0.42 | 328 | quarters: 0.38 → 0.21 → 0.10 → 0.03

Numbers say: light vs heavy: width 24.1 → 28.8 px, dark 0.71 → 0.69.

## Oil Round
Oil · 18 px · 17.6 s

![Oil Round](Oil-Round.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 2 % → 2 % | 7.2 px | 0.75 | 1.00 | 66 |
| heavy line | 7 % → 7 % | 19.3 px | 0.73 | 1.00 | 73 |
| pressure swell | 4 % → 4 % | 13.7 px | 0.72 | 1.00 | 30 |
| fast wave | 11 % → 11 % | 12.8 px | 0.65 | 1.00 | 137 |
| slow wave | 8 % → 8 % | 9.0 px | 0.57 | 1.00 | 177 |
| spiral | 10 % → 10 % | 6.6 px | 0.50 | 1.00 | 216 |
| loop | 6 % → 6 % | 7.2 px | 0.45 | 1.00 | 127 |
| tilted | 4 % → 4 % | 10.1 px | 0.52 | 1.00 | 51 |
| over the wet one | 6 % → 6 % | 7.6 px | 0.52 | 1.00 | 53 |
| long, no reload | 15 % → 15 % | 6.9 px | 0.42 | 1.00 | 307 | quarters: 0.09 → 0.08 → 0.07 → 0.06

Numbers say: light vs heavy: width 7.2 → 19.3 px, dark 0.75 → 0.73.

## Palette Knife
Oil · 20 px · 17.0 s

![Palette Knife](Palette-Knife.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 8 % → 8 % | 21.9 px | 0.67 | 1.00 | 49 |
| heavy line | 8 % → 8 % | 22.5 px | 0.73 | 1.00 | 16 |
| pressure swell | 6 % → 6 % | 22.3 px | 0.74 | 1.00 | 4 |
| fast wave | 16 % → 16 % | 18.9 px | 0.50 | 1.00 | 34 |
| slow wave | 17 % → 17 % | 19.9 px | 0.43 | 1.00 | 58 |
| spiral | 17 % → 17 % | 11.3 px | 0.46 | 1.00 | 49 |
| loop | 16 % → 16 % | 21.0 px | 0.59 | 1.00 | 20 |
| tilted | 5 % → 5 % | 15.0 px | 0.72 | 1.00 | 13 |
| over the wet one | 13 % → 13 % | 21.0 px | 0.72 | 1.00 | 6 |
| long, no reload | 16 % → 16 % | 7.2 px | 0.49 | 1.00 | 55 | quarters: 0.29 → 0.05 → 0.00 → 0.00

Numbers say: light vs heavy: width 21.9 → 22.5 px, dark 0.67 → 0.73; pressure barely changes the width.

## Water
Watercolor · 20 px · 35.7 s · over bands of wet oil paint and oil pastel in turn (it works on paint already there: look at what it does to the bands; covered counts the bands too)

![Water](Water.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 25 % → 27 % | 73.8 px | 0.80 | 1.06 | 36 |
| heavy line | 24 % → 25 % | 69.8 px | 0.81 | 1.04 | 53 |
| pressure swell | 24 % → 25 % | 89.6 px | 0.81 | 1.03 | 50 |
| fast wave | 24 % → 26 % | 27.7 px | 0.81 | 1.07 | 106 |
| slow wave | 24 % → 25 % | 27.8 px | 0.81 | 1.06 | 130 |
| spiral | 24 % → 26 % | 15.9 px | 0.81 | 1.07 | 175 |
| loop | 24 % → 25 % | 31.1 px | 0.81 | 1.03 | 92 |
| tilted | 24 % → 24 % | 67.0 px | 0.81 | 1.00 | 51 |
| over the wet one | 24 % → 25 % | 0.0 px | 0.81 | 1.06 | 39 |
| long, no reload | 24 % → 26 % | 10.7 px | 0.81 | 1.08 | 287 | quarters: 0.21 → 0.27 → 0.18 → 0.27

Numbers say: light vs heavy: width 73.8 → 69.8 px, dark 0.80 → 0.81; pressure barely changes the width; the long stroke does not run out of paint.

## Blender
Pastel · 16 px · 21.0 s · over bands of wet oil paint and oil pastel in turn (it works on paint already there: look at what it does to the bands; covered counts the bands too)

![Blender](Blender.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 24 % → 24 % | 70.7 px | 0.81 | 1.00 | 19 |
| heavy line | 25 % → 25 % | 72.1 px | 0.80 | 1.00 | 26 |
| pressure swell | 24 % → 24 % | 91.3 px | 0.81 | 1.00 | 22 |
| fast wave | 26 % → 26 % | 30.0 px | 0.79 | 1.00 | 81 |
| slow wave | 26 % → 26 % | 29.9 px | 0.79 | 1.00 | 71 |
| spiral | 28 % → 28 % | 18.7 px | 0.77 | 1.00 | 105 |
| loop | 25 % → 25 % | 33.0 px | 0.80 | 1.00 | 66 |
| tilted | 25 % → 25 % | 70.1 px | 0.79 | 1.00 | 44 |
| over the wet one | 26 % → 26 % | 1.8 px | 0.79 | 1.00 | 25 |
| long, no reload | 30 % → 30 % | 13.7 px | 0.76 | 1.00 | 217 | quarters: 0.20 → 0.28 → 0.23 → 0.30

Numbers say: light vs heavy: width 70.7 → 72.1 px, dark 0.81 → 0.80; pressure barely changes the width; the long stroke does not run out of paint.

## Eraser
Eraser · 16 px · 20.8 s · over bands of wet oil paint and oil pastel in turn (it works on paint already there: look at what it does to the bands; covered counts the bands too)

![Eraser](Eraser.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 24 % → 24 % | 69.6 px | 0.82 | 1.00 | 20 |
| heavy line | 23 % → 23 % | 67.9 px | 0.82 | 1.00 | 30 |
| pressure swell | 23 % → 23 % | 87.3 px | 0.82 | 1.00 | 26 |
| fast wave | 22 % → 22 % | 25.7 px | 0.82 | 1.00 | 90 |
| slow wave | 22 % → 22 % | 25.7 px | 0.82 | 1.00 | 78 |
| spiral | 22 % → 22 % | 14.4 px | 0.82 | 1.00 | 133 |
| loop | 22 % → 22 % | 28.6 px | 0.82 | 1.00 | 67 |
| tilted | 23 % → 23 % | 65.1 px | 0.82 | 1.00 | 45 |
| over the wet one | 23 % → 23 % | 0.0 px | 0.82 | 1.00 | 21 |
| long, no reload | 20 % → 20 % | 8.9 px | 0.82 | 1.00 | 197 | quarters: 0.15 → 0.20 → 0.15 → 0.20

Numbers say: light vs heavy: width 69.6 → 67.9 px, dark 0.82 → 0.82; pressure barely changes the width; the long stroke does not run out of paint.

## Fan
Gouache · 30 px · 29.9 s

![Fan](Fan.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 9 % → 3 % | 25.6 px | 0.63 | 0.37 | 31 |
| heavy line | 11 % → 4 % | 30.9 px | 0.63 | 0.39 | 58 |
| pressure swell | 8 % → 5 % | 31.7 px | 0.63 | 0.55 | 28 |
| fast wave | 17 % → 5 % | 20.2 px | 0.63 | 0.26 | 110 |
| slow wave | 18 % → 5 % | 21.0 px | 0.63 | 0.25 | 167 |
| spiral | 24 % → 5 % | 15.5 px | 0.63 | 0.19 | 151 |
| loop | 17 % → 5 % | 22.7 px | 0.63 | 0.28 | 99 |
| tilted | 5 % → 6 % | 15.0 px | 0.63 | 1.05 | 42 |
| over the wet one | 16 % → 8 % | 29.7 px | 0.63 | 0.49 | 40 |
| long, no reload | 22 % → 5 % | 9.9 px | 0.63 | 0.22 | 271 | quarters: 0.29 → 0.07 → 0.01 → 0.00

Numbers say: light vs heavy: width 25.6 → 30.9 px, dark 0.63 → 0.63.

## Sponge
Gouache · 30 px · 29.3 s

![Sponge](Sponge.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 4 % → 0 % | 11.3 px | 0.62 | 0.12 | 25 |
| heavy line | 12 % → 2 % | 35.4 px | 0.62 | 0.14 | 63 |
| pressure swell | 7 % → 2 % | 27.9 px | 0.62 | 0.28 | 42 |
| fast wave | 20 % → 4 % | 23.2 px | 0.62 | 0.19 | 127 |
| slow wave | 21 % → 4 % | 23.8 px | 0.62 | 0.18 | 227 |
| spiral | 28 % → 4 % | 18.3 px | 0.62 | 0.14 | 196 |
| loop | 18 % → 5 % | 23.0 px | 0.62 | 0.29 | 110 |
| tilted | 7 % → 7 % | 18.2 px | 0.62 | 1.04 | 77 |
| over the wet one | 16 % → 6 % | 27.8 px | 0.62 | 0.37 | 49 |
| long, no reload | 29 % → 5 % | 12.9 px | 0.62 | 0.17 | 291 | quarters: 0.29 → 0.13 → 0.07 → 0.04

Numbers say: light vs heavy: width 11.3 → 35.4 px, dark 0.62 → 0.62.

## Ink — sumi brush
Watercolour 1.00 · 22 px · 29.3 s

![Ink — sumi brush](Ink-sumi-brush.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 8 % → 9 % | 23.9 px | 0.87 | 1.12 | 68 |
| heavy line | 13 % → 13 % | 38.1 px | 0.86 | 1.00 | 59 |
| pressure swell | 9 % → 10 % | 34.5 px | 0.87 | 1.05 | 47 |
| fast wave | 28 % → 28 % | 32.5 px | 0.81 | 1.00 | 140 |
| slow wave | 26 % → 26 % | 29.6 px | 0.82 | 1.02 | 227 |
| spiral | 38 % → 37 % | 25.3 px | 0.74 | 0.96 | 287 |
| loop | 22 % → 22 % | 28.5 px | 0.85 | 1.02 | 140 |
| tilted | 9 % → 9 % | 25.3 px | 0.86 | 1.01 | 88 |
| over the wet one | 20 % → 21 % | 30.7 px | 0.86 | 1.03 | 68 |
| long, no reload | 45 % → 40 % | 20.1 px | 0.70 | 0.89 | 385 | quarters: 0.55 → 0.40 → 0.23 → 0.14

Numbers say: light vs heavy: width 23.9 → 38.1 px, dark 0.87 → 0.86.

## Ink — wash
Watercolour 1.00 · 40 px · 32.8 s

![Ink — wash](Ink-wash.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 13 % → 13 % | 37.3 px | 0.42 | 1.02 | 97 |
| heavy line | 19 % → 19 % | 55.2 px | 0.35 | 1.01 | 90 |
| pressure swell | 13 % → 13 % | 48.2 px | 0.41 | 1.02 | 63 |
| fast wave | 41 % → 42 % | 47.8 px | 0.32 | 1.02 | 228 |
| slow wave | 39 % → 40 % | 45.3 px | 0.42 | 1.02 | 310 |
| spiral | 60 % → 62 % | 39.7 px | 0.33 | 1.02 | 351 |
| loop | 34 % → 34 % | 43.8 px | 0.39 | 1.01 | 183 |
| tilted | 15 % → 15 % | 40.7 px | 0.43 | 1.01 | 97 |
| over the wet one | 30 % → 31 % | 43.4 px | 0.43 | 1.02 | 84 |
| long, no reload | 71 % → 75 % | 32.0 px | 0.31 | 1.05 | 523 | quarters: 0.40 → 0.29 → 0.19 → 0.12

Numbers say: light vs heavy: width 37.3 → 55.2 px, dark 0.42 → 0.35.

## Ink — dry brush
Ink 1.00 · 30 px · 24.5 s

![Ink — dry brush](Ink-dry-brush.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 6 % → 5 % | 16.8 px | 0.82 | 0.87 | 64 |
| heavy line | 6 % → 5 % | 18.6 px | 0.82 | 0.78 | 110 |
| pressure swell | 5 % → 4 % | 18.0 px | 0.83 | 0.88 | 76 |
| fast wave | 11 % → 7 % | 13.2 px | 0.80 | 0.60 | 202 |
| slow wave | 12 % → 7 % | 13.5 px | 0.80 | 0.56 | 321 |
| spiral | 18 % → 7 % | 11.6 px | 0.78 | 0.41 | 355 |
| loop | 11 % → 7 % | 14.2 px | 0.79 | 0.66 | 199 |
| tilted | 6 % → 6 % | 16.3 px | 0.80 | 1.06 | 108 |
| over the wet one | 12 % → 11 % | 17.4 px | 0.80 | 0.93 | 77 |
| long, no reload | 19 % → 8 % | 8.4 px | 0.77 | 0.42 | 536 | quarters: 0.25 → 0.08 → 0.02 → 0.01

Numbers say: light vs heavy: width 16.8 → 18.6 px, dark 0.82 → 0.82; pressure barely changes the width.

## Ink — nib
Watercolour 1.00 · 5 px · 24.0 s

![Ink — nib](Ink-nib.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 2 % → 5 % | 5.5 px | 0.89 | 2.46 | 23 |
| heavy line | 2 % → 5 % | 6.4 px | 0.89 | 2.34 | 26 |
| pressure swell | 2 % → 4 % | 6.2 px | 0.89 | 2.53 | 18 |
| fast wave | 5 % → 8 % | 5.9 px | 0.89 | 1.63 | 64 |
| slow wave | 5 % → 8 % | 5.7 px | 0.89 | 1.70 | 65 |
| spiral | 8 % → 11 % | 5.0 px | 0.87 | 1.41 | 108 |
| loop | 4 % → 8 % | 5.7 px | 0.89 | 1.74 | 61 |
| tilted | 4 % → 4 % | 10.3 px | 0.89 | 1.02 | 27 |
| over the wet one | 6 % → 9 % | 6.1 px | 0.89 | 1.61 | 32 |
| long, no reload | 9 % → 12 % | 4.2 px | 0.85 | 1.30 | 154 | quarters: 0.24 → 0.11 → 0.07 → 0.05

Numbers say: light vs heavy: width 5.5 → 6.4 px, dark 0.89 → 0.89; wet paint spreads well beyond the stroke.

## 0.45 · Dry brush
Gouache 0.91 · Ink 0.07 · 34 px · 28.7 s

![0.45 · Dry brush](0-45-Dry-brush.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 8 % → 5 % | 24.2 px | 0.68 | 0.56 | 106 |
| heavy line | 9 % → 5 % | 25.9 px | 0.68 | 0.55 | 112 |
| pressure swell | 7 % → 4 % | 26.7 px | 0.68 | 0.62 | 112 |
| fast wave | 16 % → 5 % | 18.8 px | 0.68 | 0.31 | 282 |
| slow wave | 19 % → 6 % | 22.1 px | 0.68 | 0.33 | 496 |
| spiral | 26 % → 6 % | 17.1 px | 0.68 | 0.23 | 456 |
| loop | 16 % → 7 % | 21.2 px | 0.68 | 0.41 | 265 |
| tilted | 8 % → 8 % | 22.8 px | 0.68 | 1.02 | 125 |
| over the wet one | 17 % → 12 % | 24.3 px | 0.68 | 0.69 | 117 |
| long, no reload | 28 % → 7 % | 12.7 px | 0.68 | 0.25 | 726 | quarters: 0.33 → 0.22 → 0.14 → 0.12

Numbers say: light vs heavy: width 24.2 → 25.9 px, dark 0.68 → 0.68; pressure barely changes the width.

## Dry pastel
Pastel 1.00 · 26 px · 10.6 s

![Dry pastel](Dry-pastel.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 3 % → 3 % | 8.1 px | 0.38 | 1.00 | 34 |
| heavy line | 4 % → 4 % | 12.8 px | 0.39 | 1.00 | 22 |
| pressure swell | 3 % → 3 % | 11.7 px | 0.38 | 1.00 | 32 |
| fast wave | 10 % → 10 % | 11.8 px | 0.39 | 1.00 | 82 |
| slow wave | 10 % → 10 % | 11.3 px | 0.39 | 1.00 | 148 |
| spiral | 14 % → 14 % | 9.5 px | 0.38 | 1.00 | 140 |
| loop | 7 % → 7 % | 9.3 px | 0.39 | 1.00 | 86 |
| tilted | 3 % → 3 % | 8.3 px | 0.38 | 1.00 | 39 |
| over the wet one | 7 % → 7 % | 10.7 px | 0.38 | 1.00 | 29 |
| long, no reload | 18 % → 18 % | 8.2 px | 0.39 | 1.00 | 207 | quarters: 0.08 → 0.08 → 0.08 → 0.07

Numbers say: light vs heavy: width 8.1 → 12.8 px, dark 0.38 → 0.39; the long stroke does not run out of paint.

## 0.45 · Charcoal
Charcoal 1.00 · 18 px · 10.3 s

![0.45 · Charcoal](0-45-Charcoal.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 2 % → 2 % | 6.5 px | 0.80 | 1.00 | 17 |
| heavy line | 3 % → 3 % | 9.2 px | 0.80 | 1.00 | 20 |
| pressure swell | 2 % → 2 % | 8.8 px | 0.80 | 1.00 | 13 |
| fast wave | 7 % → 7 % | 8.5 px | 0.80 | 1.00 | 40 |
| slow wave | 7 % → 7 % | 8.0 px | 0.80 | 1.00 | 74 |
| spiral | 12 % → 12 % | 7.9 px | 0.80 | 1.00 | 82 |
| loop | 6 % → 6 % | 8.1 px | 0.80 | 1.00 | 52 |
| tilted | 3 % → 3 % | 7.5 px | 0.80 | 1.00 | 40 |
| over the wet one | 6 % → 6 % | 7.8 px | 0.80 | 1.00 | 11 |
| long, no reload | 17 % → 17 % | 7.7 px | 0.80 | 1.00 | 146 | quarters: 0.15 → 0.16 → 0.15 → 0.16

Numbers say: light vs heavy: width 6.5 → 9.2 px, dark 0.80 → 0.80; the long stroke does not run out of paint.

## Watercolour — wash
Watercolour 1.00 · 50 px · 34.8 s

![Watercolour — wash](Watercolour-wash.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 16 % → 16 % | 45.5 px | 0.22 | 1.01 | 112 |
| heavy line | 22 % → 22 % | 64.9 px | 0.19 | 1.00 | 130 |
| pressure swell | 15 % → 15 % | 56.1 px | 0.22 | 1.01 | 88 |
| fast wave | 48 % → 49 % | 55.5 px | 0.19 | 1.01 | 291 |
| slow wave | 46 % → 46 % | 53.3 px | 0.24 | 1.00 | 549 |
| spiral | 66 % → 66 % | 43.7 px | 0.21 | 1.00 | 531 |
| loop | 40 % → 40 % | 51.4 px | 0.22 | 1.00 | 280 |
| tilted | 18 % → 18 % | 49.7 px | 0.23 | 1.00 | 178 |
| over the wet one | 36 % → 36 % | 49.6 px | 0.23 | 1.01 | 117 |
| long, no reload | 84 % → 84 % | 37.7 px | 0.20 | 1.00 | 722 | quarters: 0.24 → 0.20 → 0.16 → 0.12

Numbers say: light vs heavy: width 45.5 → 64.9 px, dark 0.22 → 0.19.

## Watercolour — wet-in-wet
Watercolour 1.00 · 44 px · 36.4 s

![Watercolour — wet-in-wet](Watercolour-wet-in-wet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 13 % → 21 % | 38.4 px | 0.32 | 1.58 | 73 |
| heavy line | 19 % → 22 % | 54.6 px | 0.34 | 1.17 | 105 |
| pressure swell | 12 % → 17 % | 46.5 px | 0.35 | 1.34 | 75 |
| fast wave | 41 % → 49 % | 47.7 px | 0.33 | 1.19 | 236 |
| slow wave | 40 % → 48 % | 46.2 px | 0.40 | 1.21 | 449 |
| spiral | 63 % → 69 % | 41.5 px | 0.37 | 1.10 | 399 |
| loop | 34 % → 41 % | 44.4 px | 0.37 | 1.20 | 220 |
| tilted | 15 % → 16 % | 41.5 px | 0.36 | 1.06 | 137 |
| over the wet one | 31 % → 40 % | 44.1 px | 0.36 | 1.31 | 91 |
| long, no reload | 78 % → 87 % | 34.8 px | 0.36 | 1.12 | 611 | quarters: 0.40 → 0.37 → 0.32 → 0.26

Numbers say: light vs heavy: width 38.4 → 54.6 px, dark 0.32 → 0.34; wet paint spreads well beyond the stroke.

## Watercolour — glaze
Watercolour 1.00 · 38 px · 31.9 s

![Watercolour — glaze](Watercolour-glaze.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 13 % → 13 % | 36.6 px | 0.07 | 1.02 | 75 |
| heavy line | 19 % → 19 % | 55.4 px | 0.07 | 1.00 | 96 |
| pressure swell | 13 % → 13 % | 47.0 px | 0.07 | 1.02 | 65 |
| fast wave | 39 % → 40 % | 45.6 px | 0.07 | 1.01 | 195 |
| slow wave | 37 % → 37 % | 42.8 px | 0.07 | 1.01 | 370 |
| spiral | 59 % → 60 % | 38.8 px | 0.06 | 1.01 | 356 |
| loop | 33 % → 33 % | 42.6 px | 0.07 | 1.00 | 183 |
| tilted | 14 % → 14 % | 40.1 px | 0.07 | 1.00 | 130 |
| over the wet one | 30 % → 30 % | 42.3 px | 0.07 | 1.01 | 96 |
| long, no reload | 69 % → 70 % | 30.9 px | 0.06 | 1.01 | 508 | quarters: 0.06 → 0.05 → 0.03 → 0.02

Numbers say: light vs heavy: width 36.6 → 55.4 px, dark 0.07 → 0.07.

## Watercolour — granulating
Watercolour 1.00 · 44 px · 32.6 s

![Watercolour — granulating](Watercolour-granulating.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 14 % → 14 % | 41.4 px | 0.35 | 1.01 | 80 |
| heavy line | 21 % → 21 % | 60.4 px | 0.31 | 1.00 | 104 |
| pressure swell | 14 % → 14 % | 52.2 px | 0.34 | 1.01 | 62 |
| fast wave | 45 % → 45 % | 51.7 px | 0.29 | 1.01 | 249 |
| slow wave | 42 % → 42 % | 48.2 px | 0.35 | 1.01 | 421 |
| spiral | 62 % → 63 % | 41.0 px | 0.30 | 1.01 | 404 |
| loop | 37 % → 37 % | 47.6 px | 0.33 | 1.00 | 212 |
| tilted | 16 % → 16 % | 45.5 px | 0.36 | 1.00 | 123 |
| over the wet one | 33 % → 33 % | 46.2 px | 0.36 | 1.01 | 99 |
| long, no reload | 75 % → 76 % | 33.6 px | 0.29 | 1.01 | 618 | quarters: 0.34 → 0.26 → 0.20 → 0.14

Numbers say: light vs heavy: width 41.4 → 60.4 px, dark 0.35 → 0.31.

## Watercolour — dry brush
Watercolour 1.00 · 36 px · 26.9 s

![Watercolour — dry brush](Watercolour-dry-brush.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 10 % → 10 % | 27.9 px | 0.17 | 1.01 | 100 |
| heavy line | 14 % → 13 % | 39.9 px | 0.16 | 0.93 | 98 |
| pressure swell | 11 % → 11 % | 40.3 px | 0.16 | 0.98 | 76 |
| fast wave | 27 % → 20 % | 30.7 px | 0.13 | 0.74 | 267 |
| slow wave | 24 % → 17 % | 28.0 px | 0.14 | 0.71 | 411 |
| spiral | 34 % → 20 % | 22.4 px | 0.13 | 0.58 | 430 |
| loop | 21 % → 18 % | 27.1 px | 0.14 | 0.86 | 238 |
| tilted | 10 % → 10 % | 28.5 px | 0.17 | 1.00 | 122 |
| over the wet one | 21 % → 20 % | 31.3 px | 0.17 | 0.95 | 94 |
| long, no reload | 36 % → 19 % | 16.0 px | 0.14 | 0.54 | 634 | quarters: 0.09 → 0.03 → 0.01 → 0.00

Numbers say: light vs heavy: width 27.9 → 39.9 px, dark 0.17 → 0.16.

## Gouache
Gouache 1.00 · 30 px · 29.9 s

![Gouache](Gouache.png)

A light paint: laid on a grey sheet (on white it cannot be seen); **dark** = how far it is from the grey either way.

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 8 % → 4 % | 23.8 px | 0.28 | 0.49 | 73 |
| heavy line | 13 % → 4 % | 36.9 px | 0.28 | 0.33 | 120 |
| pressure swell | 10 % → 4 % | 36.7 px | 0.28 | 0.42 | 58 |
| fast wave | 24 % → 5 % | 27.4 px | 0.28 | 0.21 | 196 |
| slow wave | 24 % → 6 % | 27.5 px | 0.28 | 0.25 | 373 |
| spiral | 32 % → 6 % | 21.3 px | 0.28 | 0.18 | 339 |
| loop | 20 % → 6 % | 25.8 px | 0.28 | 0.30 | 191 |
| tilted | 9 % → 9 % | 25.0 px | 0.27 | 1.01 | 121 |
| over the wet one | 20 % → 10 % | 29.5 px | 0.27 | 0.52 | 105 |
| long, no reload | 34 % → 7 % | 15.1 px | 0.27 | 0.22 | 506 | quarters: 0.01 → 0.01 → 0.02 → 0.02

Numbers say: light vs heavy: width 23.8 → 36.9 px, dark 0.28 → 0.28; the long stroke does not run out of paint.

## Oil — alla prima
Oil 0.89 · Oil glaze 0.11 · 30 px · 13.7 s

![Oil — alla prima](Oil-alla-prima.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 9 % → 9 % | 26.4 px | 0.50 | 1.00 | 88 |
| heavy line | 9 % → 9 % | 27.4 px | 0.49 | 1.00 | 89 |
| pressure swell | 8 % → 8 % | 28.7 px | 0.50 | 1.00 | 61 |
| fast wave | 22 % → 22 % | 24.9 px | 0.47 | 1.00 | 231 |
| slow wave | 23 % → 23 % | 26.8 px | 0.50 | 1.00 | 413 |
| spiral | 36 % → 36 % | 23.8 px | 0.49 | 1.00 | 382 |
| loop | 19 % → 19 % | 25.2 px | 0.50 | 1.00 | 194 |
| tilted | 11 % → 11 % | 29.8 px | 0.50 | 1.00 | 101 |
| over the wet one | 20 % → 20 % | 25.0 px | 0.50 | 1.00 | 91 |
| long, no reload | 42 % → 42 % | 19.0 px | 0.47 | 1.00 | 594 | quarters: 0.29 → 0.23 → 0.21 → 0.17

Numbers say: light vs heavy: width 26.4 → 27.4 px, dark 0.50 → 0.49; pressure barely changes the width.

## Oil — impasto
Oil heavy 1.00 · 34 px · 18.7 s

![Oil — impasto](Oil-impasto.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 11 % → 11 % | 30.5 px | 0.23 | 1.00 | 92 |
| heavy line | 12 % → 12 % | 34.5 px | 0.23 | 1.00 | 114 |
| pressure swell | 9 % → 9 % | 34.4 px | 0.24 | 1.00 | 94 |
| fast wave | 27 % → 27 % | 30.8 px | 0.22 | 1.00 | 261 |
| slow wave | 30 % → 30 % | 34.5 px | 0.22 | 1.00 | 465 |
| spiral | 44 % → 44 % | 29.1 px | 0.21 | 1.00 | 438 |
| loop | 24 % → 24 % | 31.5 px | 0.22 | 1.00 | 261 |
| tilted | 12 % → 12 % | 32.6 px | 0.24 | 1.00 | 144 |
| over the wet one | 23 % → 23 % | 30.4 px | 0.24 | 1.00 | 111 |
| long, no reload | 49 % → 49 % | 22.0 px | 0.21 | 1.00 | 684 | quarters: 0.16 → 0.12 → 0.09 → 0.07

Numbers say: light vs heavy: width 30.5 → 34.5 px, dark 0.23 → 0.23.

## Oil — glaze
Oil glaze 1.00 · 40 px · 15.7 s

![Oil — glaze](Oil-glaze.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 9 % → 9 % | 27.0 px | 0.50 | 1.00 | 96 |
| heavy line | 13 % → 13 % | 38.3 px | 0.49 | 1.00 | 121 |
| pressure swell | 10 % → 10 % | 36.6 px | 0.50 | 1.00 | 88 |
| fast wave | 29 % → 29 % | 33.5 px | 0.49 | 1.00 | 268 |
| slow wave | 30 % → 30 % | 34.6 px | 0.50 | 1.00 | 476 |
| spiral | 46 % → 46 % | 30.1 px | 0.49 | 1.00 | 484 |
| loop | 24 % → 24 % | 31.4 px | 0.50 | 1.00 | 223 |
| tilted | 11 % → 11 % | 30.4 px | 0.50 | 1.00 | 136 |
| over the wet one | 23 % → 23 % | 32.5 px | 0.50 | 1.00 | 114 |
| long, no reload | 52 % → 52 % | 23.5 px | 0.49 | 1.00 | 671 | quarters: 0.34 → 0.30 → 0.27 → 0.22

Numbers say: light vs heavy: width 27.0 → 38.3 px, dark 0.50 → 0.49.

## Oil — scumble
Oil 1.00 · 36 px · 15.2 s

![Oil — scumble](Oil-scumble.png)

A light paint: laid on a grey sheet (on white it cannot be seen); **dark** = how far it is from the grey either way.

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 9 % → 9 % | 25.5 px | 0.25 | 1.00 | 125 |
| heavy line | 9 % → 9 % | 25.5 px | 0.24 | 1.00 | 136 |
| pressure swell | 8 % → 8 % | 29.6 px | 0.23 | 1.00 | 89 |
| fast wave | 17 % → 17 % | 19.9 px | 0.16 | 1.00 | 322 |
| slow wave | 21 % → 21 % | 24.1 px | 0.18 | 1.00 | 580 |
| spiral | 28 % → 28 % | 18.8 px | 0.14 | 1.00 | 605 |
| loop | 17 % → 17 % | 22.0 px | 0.20 | 1.00 | 261 |
| tilted | 10 % → 10 % | 27.8 px | 0.24 | 1.00 | 161 |
| over the wet one | 19 % → 19 % | 25.1 px | 0.24 | 1.00 | 126 |
| long, no reload | 30 % → 30 % | 13.3 px | 0.13 | 1.00 | 783 | quarters: 0.00 → 0.00 → 0.00 → 0.00

Numbers say: light vs heavy: width 25.5 → 25.5 px, dark 0.25 → 0.24; pressure barely changes the width.

## Acrylic — heavy body
Impasto 0.98 · 30 px · 14.5 s

![Acrylic — heavy body](Acrylic-heavy-body.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 9 % → 7 % | 26.7 px | 0.51 | 0.80 | 92 |
| heavy line | 10 % → 8 % | 29.1 px | 0.51 | 0.81 | 101 |
| pressure swell | 8 % → 7 % | 29.1 px | 0.53 | 0.88 | 78 |
| fast wave | 20 % → 11 % | 22.9 px | 0.52 | 0.57 | 217 |
| slow wave | 21 % → 14 % | 24.7 px | 0.52 | 0.65 | 390 |
| spiral | 30 % → 13 % | 19.6 px | 0.52 | 0.45 | 381 |
| loop | 18 % → 12 % | 23.5 px | 0.52 | 0.66 | 187 |
| tilted | 8 % → 8 % | 22.4 px | 0.52 | 0.99 | 132 |
| over the wet one | 17 % → 15 % | 25.8 px | 0.52 | 0.86 | 110 |
| long, no reload | 30 % → 16 % | 13.4 px | 0.52 | 0.52 | 529 | quarters: 0.25 → 0.14 → 0.09 → 0.07

Numbers say: light vs heavy: width 26.7 → 29.1 px, dark 0.51 → 0.51; pressure barely changes the width.

## Acrylic — fluid
Watercolour 1.00 · 36 px · 34.2 s

![Acrylic — fluid](Acrylic-fluid.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 12 % → 12 % | 34.8 px | 0.24 | 1.01 | 83 |
| heavy line | 18 % → 18 % | 52.6 px | 0.21 | 0.99 | 89 |
| pressure swell | 12 % → 12 % | 45.4 px | 0.23 | 1.00 | 60 |
| fast wave | 38 % → 38 % | 44.1 px | 0.19 | 0.98 | 284 |
| slow wave | 35 % → 35 % | 40.5 px | 0.22 | 1.00 | 381 |
| spiral | 55 % → 53 % | 36.0 px | 0.19 | 0.98 | 383 |
| loop | 31 % → 31 % | 40.2 px | 0.21 | 1.00 | 221 |
| tilted | 12 % → 12 % | 34.2 px | 0.24 | 1.00 | 112 |
| over the wet one | 27 % → 28 % | 42.3 px | 0.24 | 1.02 | 87 |
| long, no reload | 61 % → 58 % | 27.6 px | 0.19 | 0.95 | 525 | quarters: 0.20 → 0.14 → 0.09 → 0.06

Numbers say: light vs heavy: width 34.8 → 52.6 px, dark 0.24 → 0.21.

## Acrylic — palette knife
Impasto 1.00 · 42 px · 20.6 s

![Acrylic — palette knife](Acrylic-palette-knife.png)

A light paint: laid on a grey sheet (on white it cannot be seen); **dark** = how far it is from the grey either way.

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 15 % → 15 % | 44.0 px | 0.39 | 0.98 | 34 |
| heavy line | 15 % → 15 % | 44.2 px | 0.40 | 0.98 | 60 |
| pressure swell | 12 % → 11 % | 43.5 px | 0.42 | 0.99 | 15 |
| fast wave | 36 % → 20 % | 41.9 px | 0.37 | 0.55 | 71 |
| slow wave | 37 % → 21 % | 42.7 px | 0.37 | 0.57 | 116 |
| spiral | 47 % → 18 % | 30.7 px | 0.37 | 0.39 | 147 |
| loop | 32 % → 24 % | 41.2 px | 0.36 | 0.77 | 69 |
| tilted | 12 % → 12 % | 33.6 px | 0.39 | 1.00 | 32 |
| over the wet one | 26 % → 25 % | 39.8 px | 0.39 | 0.97 | 43 |
| long, no reload | 53 % → 20 % | 23.6 px | 0.35 | 0.38 | 209 | quarters: 0.00 → 0.00 → 0.00 → 0.01

Numbers say: light vs heavy: width 44.0 → 44.2 px, dark 0.39 → 0.40; pressure barely changes the width; the long stroke does not run out of paint.

## Finger on oil
Oil 1.00 · 30 px · 12.8 s

![Finger on oil](Finger-on-oil.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 6 % → 6 % | 16.4 px | 0.36 | 1.00 | 43 |
| heavy line | 9 % → 9 % | 24.7 px | 0.32 | 1.00 | 41 |
| pressure swell | 6 % → 6 % | 22.3 px | 0.38 | 1.00 | 30 |
| fast wave | 11 % → 11 % | 12.5 px | 0.27 | 1.00 | 115 |
| slow wave | 15 % → 15 % | 17.7 px | 0.31 | 1.00 | 209 |
| spiral | 20 % → 20 % | 13.1 px | 0.27 | 1.00 | 214 |
| loop | 13 % → 13 % | 16.9 px | 0.31 | 1.00 | 98 |
| tilted | 9 % → 9 % | 23.8 px | 0.34 | 1.00 | 71 |
| over the wet one | 16 % → 16 % | 20.4 px | 0.34 | 1.00 | 51 |
| long, no reload | 23 % → 23 % | 10.4 px | 0.26 | 1.00 | 262 | quarters: 0.15 → 0.06 → 0.03 → 0.02

Numbers say: light vs heavy: width 16.4 → 24.7 px, dark 0.36 → 0.32.

## Palette knife — oil
Oil heavy 0.93 · Impasto 0.07 · 44 px · 19.7 s

![Palette knife — oil](Palette-knife-oil.png)

A light paint: laid on a grey sheet (on white it cannot be seen); **dark** = how far it is from the grey either way.

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 16 % → 14 % | 45.7 px | 0.37 | 0.90 | 33 |
| heavy line | 16 % → 16 % | 46.3 px | 0.38 | 0.98 | 31 |
| pressure swell | 12 % → 12 % | 45.2 px | 0.38 | 0.99 | 16 |
| fast wave | 39 % → 34 % | 44.9 px | 0.35 | 0.89 | 83 |
| slow wave | 39 % → 36 % | 45.4 px | 0.35 | 0.91 | 150 |
| spiral | 62 % → 37 % | 40.7 px | 0.35 | 0.60 | 123 |
| loop | 34 % → 31 % | 43.7 px | 0.36 | 0.92 | 72 |
| tilted | 13 % → 13 % | 36.6 px | 0.37 | 1.00 | 27 |
| over the wet one | 28 % → 27 % | 40.8 px | 0.37 | 0.97 | 35 |
| long, no reload | 74 % → 39 % | 33.0 px | 0.34 | 0.53 | 224 | quarters: 0.00 → 0.00 → 0.01 → 0.01

Numbers say: light vs heavy: width 45.7 → 46.3 px, dark 0.37 → 0.38; pressure barely changes the width; the long stroke does not run out of paint.

## 0.45 · Sponge
Watercolour 0.93 · Ink 0.07 · 46 px · 36.8 s

![0.45 · Sponge](0-45-Sponge.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 27 % → 25 % | 78.2 px | 0.12 | 0.95 | 54 |
| heavy line | 32 % → 29 % | 91.9 px | 0.12 | 0.92 | 89 |
| pressure swell | 24 % → 21 % | 90.6 px | 0.12 | 0.88 | 66 |
| fast wave | 59 % → 55 % | 68.5 px | 0.12 | 0.92 | 189 |
| slow wave | 61 % → 58 % | 70.4 px | 0.17 | 0.95 | 338 |
| spiral | 77 % → 75 % | 50.7 px | 0.16 | 0.97 | 309 |
| loop | 53 % → 51 % | 69.1 px | 0.14 | 0.95 | 173 |
| tilted | 18 % → 18 % | 50.7 px | 0.17 | 1.00 | 120 |
| over the wet one | 45 % → 42 % | 73.6 px | 0.17 | 0.94 | 83 |
| long, no reload | 94 % → 89 % | 42.0 px | 0.17 | 0.95 | 500 | quarters: 0.17 → 0.18 → 0.16 → 0.14

Numbers say: light vs heavy: width 78.2 → 91.9 px, dark 0.12 → 0.12.

## 0.45 · Eraser
Watercolour 1.00 · 30 px · 21.9 s · over bands of wet oil paint and oil pastel in turn (it works on paint already there: look at what it does to the bands; covered counts the bands too)

![0.45 · Eraser](0-45-Eraser.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 24 % → 24 % | 69.2 px | 0.82 | 1.00 | 26 |
| heavy line | 23 % → 23 % | 67.4 px | 0.81 | 1.00 | 40 |
| pressure swell | 23 % → 23 % | 86.8 px | 0.82 | 1.00 | 38 |
| fast wave | 21 % → 21 % | 24.7 px | 0.81 | 1.00 | 108 |
| slow wave | 20 % → 20 % | 23.5 px | 0.82 | 1.00 | 226 |
| spiral | 20 % → 20 % | 13.5 px | 0.79 | 1.00 | 210 |
| loop | 21 % → 21 % | 27.8 px | 0.80 | 1.00 | 141 |
| tilted | 23 % → 23 % | 64.8 px | 0.81 | 1.00 | 56 |
| over the wet one | 22 % → 22 % | 0.0 px | 0.81 | 1.00 | 55 |
| long, no reload | 17 % → 17 % | 7.5 px | 0.79 | 1.00 | 326 | quarters: 0.13 → 0.16 → 0.13 → 0.17

Numbers say: light vs heavy: width 69.2 → 67.4 px, dark 0.82 → 0.81; pressure barely changes the width; the long stroke does not run out of paint.

## Lift wet paint
Watercolour 1.00 · 30 px · 21.8 s · over bands of wet oil paint and oil pastel in turn (it works on paint already there: look at what it does to the bands; covered counts the bands too)

![Lift wet paint](Lift-wet-paint.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 24 % → 24 % | 70.1 px | 0.82 | 1.00 | 28 |
| heavy line | 24 % → 24 % | 69.8 px | 0.82 | 1.00 | 39 |
| pressure swell | 24 % → 24 % | 89.6 px | 0.82 | 1.00 | 26 |
| fast wave | 24 % → 24 % | 27.7 px | 0.82 | 1.00 | 95 |
| slow wave | 24 % → 24 % | 27.7 px | 0.82 | 1.00 | 140 |
| spiral | 24 % → 24 % | 15.9 px | 0.82 | 1.00 | 178 |
| loop | 24 % → 24 % | 31.1 px | 0.82 | 1.00 | 99 |
| tilted | 24 % → 24 % | 66.8 px | 0.82 | 1.00 | 41 |
| over the wet one | 24 % → 24 % | 0.0 px | 0.82 | 1.00 | 37 |
| long, no reload | 24 % → 24 % | 10.7 px | 0.82 | 1.00 | 252 | quarters: 0.18 → 0.24 → 0.17 → 0.24

Numbers say: light vs heavy: width 70.1 → 69.8 px, dark 0.82 → 0.82; pressure barely changes the width; the long stroke does not run out of paint.

## Sgraffito
Watercolour 1.00 · 10 px · 22.0 s · over bands of wet oil paint and oil pastel in turn (it works on paint already there: look at what it does to the bands; covered counts the bands too)

![Sgraffito](Sgraffito.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 24 % → 24 % | 69.9 px | 0.81 | 1.00 | 14 |
| heavy line | 24 % → 24 % | 69.8 px | 0.82 | 1.00 | 10 |
| pressure swell | 24 % → 24 % | 89.6 px | 0.82 | 1.00 | 5 |
| fast wave | 24 % → 24 % | 27.7 px | 0.82 | 1.00 | 33 |
| slow wave | 24 % → 24 % | 27.7 px | 0.82 | 1.00 | 23 |
| spiral | 24 % → 24 % | 15.9 px | 0.82 | 1.00 | 51 |
| loop | 24 % → 24 % | 31.1 px | 0.82 | 1.00 | 31 |
| tilted | 24 % → 24 % | 66.9 px | 0.82 | 1.00 | 15 |
| over the wet one | 24 % → 24 % | 0.0 px | 0.82 | 1.00 | 14 |
| long, no reload | 24 % → 24 % | 10.6 px | 0.82 | 1.00 | 55 | quarters: 0.17 → 0.24 → 0.17 → 0.24

Numbers say: light vs heavy: width 69.9 → 69.8 px, dark 0.81 → 0.82; pressure barely changes the width; the long stroke does not run out of paint.

## Brush Artist · Refs · #01 Henry Ward peach cloud
Gouache 1.00 · 44 px · 36.1 s

![Brush Artist · Refs · #01 Henry Ward peach cloud](Brush-Artist-Refs-01-Henry-Ward-peach-cloud.png)

A light paint: laid on a grey sheet (on white it cannot be seen); **dark** = how far it is from the grey either way.

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 14 % → 6 % | 39.4 px | 0.34 | 0.45 | 117 |
| heavy line | 14 % → 8 % | 41.4 px | 0.34 | 0.58 | 156 |
| pressure swell | 10 % → 8 % | 38.0 px | 0.34 | 0.77 | 104 |
| fast wave | 28 % → 4 % | 32.5 px | 0.34 | 0.16 | 347 |
| slow wave | 30 % → 10 % | 34.7 px | 0.34 | 0.33 | 603 |
| spiral | 39 % → 8 % | 25.9 px | 0.34 | 0.21 | 629 |
| loop | 26 % → 8 % | 33.7 px | 0.34 | 0.32 | 401 |
| tilted | 12 % → 12 % | 34.2 px | 0.34 | 0.97 | 238 |
| over the wet one | 25 % → 15 % | 34.9 px | 0.34 | 0.60 | 199 |
| long, no reload | 27 % → 12 % | 12.1 px | 0.33 | 0.44 | 1050 | quarters: 0.01 → 0.03 → 0.03 → 0.03

Numbers say: light vs heavy: width 39.4 → 41.4 px, dark 0.34 → 0.34; pressure barely changes the width; the long stroke does not run out of paint.

## Brush Artist · Refs · #02 Henry Ward cream strokes
Gouache 1.00 · 46 px · 34.8 s

![Brush Artist · Refs · #02 Henry Ward cream strokes](Brush-Artist-Refs-02-Henry-Ward-cream-strokes.png)

A light paint: laid on a grey sheet (on white it cannot be seen); **dark** = how far it is from the grey either way.

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 10 % → 4 % | 29.4 px | 0.42 | 0.44 | 154 |
| heavy line | 12 % → 6 % | 35.0 px | 0.42 | 0.48 | 161 |
| pressure swell | 9 % → 6 % | 33.6 px | 0.43 | 0.65 | 99 |
| fast wave | 23 % → 3 % | 26.4 px | 0.42 | 0.14 | 346 |
| slow wave | 26 % → 9 % | 30.0 px | 0.42 | 0.35 | 597 |
| spiral | 31 % → 6 % | 20.5 px | 0.42 | 0.20 | 606 |
| loop | 23 % → 7 % | 29.6 px | 0.42 | 0.29 | 290 |
| tilted | 12 % → 12 % | 34.7 px | 0.42 | 0.99 | 226 |
| over the wet one | 23 % → 11 % | 30.0 px | 0.42 | 0.50 | 186 |
| long, no reload | 25 % → 9 % | 11.0 px | 0.42 | 0.37 | 1022 | quarters: 0.01 → 0.02 → 0.03 → 0.03

Numbers say: light vs heavy: width 29.4 → 35.0 px, dark 0.42 → 0.42; the long stroke does not run out of paint.

## Brush Artist · Refs · #03 Henry Ward navy contours
Impasto 1.00 · 22 px · 16.1 s

![Brush Artist · Refs · #03 Henry Ward navy contours](Brush-Artist-Refs-03-Henry-Ward-navy-contours.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 7 % → 6 % | 19.4 px | 0.69 | 0.90 | 74 |
| heavy line | 7 % → 7 % | 21.1 px | 0.69 | 0.91 | 116 |
| pressure swell | 5 % → 5 % | 20.5 px | 0.74 | 0.91 | 54 |
| fast wave | 16 % → 11 % | 18.6 px | 0.73 | 0.71 | 187 |
| slow wave | 17 % → 12 % | 19.5 px | 0.73 | 0.74 | 364 |
| spiral | 25 % → 13 % | 16.3 px | 0.73 | 0.51 | 415 |
| loop | 14 % → 12 % | 18.6 px | 0.72 | 0.81 | 187 |
| tilted | 8 % → 8 % | 22.6 px | 0.72 | 1.00 | 98 |
| over the wet one | 15 % → 13 % | 19.0 px | 0.72 | 0.87 | 81 |
| long, no reload | 30 % → 13 % | 13.4 px | 0.73 | 0.42 | 542 | quarters: 0.31 → 0.25 → 0.19 → 0.11

Numbers say: light vs heavy: width 19.4 → 21.1 px, dark 0.69 → 0.69; pressure barely changes the width.

## Brush Artist · Refs · #04 Henry Ward grey cloud
Gouache 1.00 · 50 px · 37.8 s

![Brush Artist · Refs · #04 Henry Ward grey cloud](Brush-Artist-Refs-04-Henry-Ward-grey-cloud.png)

A light paint: laid on a grey sheet (on white it cannot be seen); **dark** = how far it is from the grey either way.

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 10 % → 7 % | 29.4 px | 0.34 | 0.71 | 180 |
| heavy line | 12 % → 8 % | 34.1 px | 0.34 | 0.65 | 198 |
| pressure swell | 10 % → 6 % | 36.0 px | 0.34 | 0.64 | 120 |
| fast wave | 19 % → 8 % | 22.4 px | 0.34 | 0.41 | 375 |
| slow wave | 27 % → 12 % | 30.8 px | 0.34 | 0.45 | 653 |
| spiral | 25 % → 11 % | 16.7 px | 0.34 | 0.42 | 748 |
| loop | 20 % → 11 % | 25.5 px | 0.34 | 0.56 | 400 |
| tilted | 12 % → 12 % | 33.9 px | 0.34 | 0.99 | 249 |
| over the wet one | 23 % → 17 % | 29.0 px | 0.34 | 0.76 | 302 |
| long, no reload | 29 % → 13 % | 12.9 px | 0.34 | 0.44 | 1056 | quarters: 0.01 → 0.02 → 0.02 → 0.02

Numbers say: light vs heavy: width 29.4 → 34.1 px, dark 0.34 → 0.34; the long stroke does not run out of paint.

## Brush Artist · Refs · #05 Henry Ward green in rust loops
Impasto 1.00 · 20 px · 16.0 s

![Brush Artist · Refs · #05 Henry Ward green in rust loops](Brush-Artist-Refs-05-Henry-Ward-green-in-rust-loops.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 7 % → 6 % | 18.9 px | 0.55 | 0.91 | 77 |
| heavy line | 7 % → 7 % | 20.7 px | 0.55 | 0.93 | 85 |
| pressure swell | 6 % → 5 % | 20.9 px | 0.57 | 0.91 | 59 |
| fast wave | 16 % → 11 % | 18.8 px | 0.56 | 0.69 | 203 |
| slow wave | 17 % → 12 % | 19.7 px | 0.56 | 0.69 | 296 |
| spiral | 25 % → 12 % | 16.8 px | 0.56 | 0.47 | 349 |
| loop | 14 % → 12 % | 18.8 px | 0.56 | 0.82 | 184 |
| tilted | 8 % → 8 % | 21.8 px | 0.55 | 0.99 | 115 |
| over the wet one | 14 % → 13 % | 18.6 px | 0.55 | 0.88 | 87 |
| long, no reload | 30 % → 12 % | 13.3 px | 0.56 | 0.41 | 554 | quarters: 0.24 → 0.18 → 0.11 → 0.04

Numbers say: light vs heavy: width 18.9 → 20.7 px, dark 0.55 → 0.55; pressure barely changes the width.

## Brush Artist · Refs · #06 Henry Ward scrubbed grey
Gouache 1.00 · 50 px · 37.9 s

![Brush Artist · Refs · #06 Henry Ward scrubbed grey](Brush-Artist-Refs-06-Henry-Ward-scrubbed-grey.png)

A light paint: laid on a grey sheet (on white it cannot be seen); **dark** = how far it is from the grey either way.

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 10 % → 7 % | 29.4 px | 0.35 | 0.71 | 158 |
| heavy line | 12 % → 8 % | 34.1 px | 0.35 | 0.65 | 246 |
| pressure swell | 10 % → 6 % | 36.0 px | 0.36 | 0.64 | 103 |
| fast wave | 19 % → 8 % | 22.4 px | 0.35 | 0.41 | 637 |
| slow wave | 27 % → 12 % | 30.8 px | 0.35 | 0.45 | 788 |
| spiral | 25 % → 11 % | 16.7 px | 0.35 | 0.42 | 803 |
| loop | 20 % → 11 % | 25.5 px | 0.35 | 0.56 | 491 |
| tilted | 12 % → 12 % | 33.9 px | 0.35 | 0.99 | 199 |
| over the wet one | 23 % → 17 % | 29.0 px | 0.35 | 0.76 | 176 |
| long, no reload | 29 % → 13 % | 12.9 px | 0.35 | 0.44 | 809 | quarters: 0.01 → 0.02 → 0.02 → 0.02

Numbers say: light vs heavy: width 29.4 → 34.1 px, dark 0.35 → 0.35; the long stroke does not run out of paint.

## Brush Artist · Refs · #07 Henry Ward blue L + black zigzag
Impasto 1.00 · 34 px · 17.6 s

![Brush Artist · Refs · #07 Henry Ward blue L + black zigzag](Brush-Artist-Refs-07-Henry-Ward-blue-L-black-zigzag.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 11 % → 9 % | 31.5 px | 0.57 | 0.87 | 103 |
| heavy line | 12 % → 10 % | 33.7 px | 0.57 | 0.89 | 109 |
| pressure swell | 9 % → 8 % | 33.3 px | 0.60 | 0.90 | 98 |
| fast wave | 26 % → 19 % | 30.6 px | 0.59 | 0.71 | 338 |
| slow wave | 27 % → 20 % | 31.5 px | 0.59 | 0.74 | 595 |
| spiral | 41 % → 21 % | 27.3 px | 0.59 | 0.52 | 686 |
| loop | 23 % → 18 % | 30.2 px | 0.59 | 0.78 | 215 |
| tilted | 11 % → 11 % | 30.2 px | 0.58 | 1.00 | 135 |
| over the wet one | 22 % → 19 % | 29.8 px | 0.58 | 0.89 | 143 |
| long, no reload | 48 % → 22 % | 21.4 px | 0.59 | 0.46 | 644 | quarters: 0.37 → 0.28 → 0.21 → 0.12

Numbers say: light vs heavy: width 31.5 → 33.7 px, dark 0.57 → 0.57; pressure barely changes the width.

## Brush Artist · Refs · #08 Henry Ward olive bands
Gouache 1.00 · 34 px · 25.7 s

![Brush Artist · Refs · #08 Henry Ward olive bands](Brush-Artist-Refs-08-Henry-Ward-olive-bands.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 4 % → 0 % | 10.7 px | 0.61 | 0.09 | 146 |
| heavy line | 7 % → 1 % | 21.4 px | 0.61 | 0.07 | 186 |
| pressure swell | 5 % → 1 % | 20.4 px | 0.61 | 0.16 | 111 |
| fast wave | 10 % → 1 % | 11.7 px | 0.61 | 0.08 | 234 |
| slow wave | 15 % → 1 % | 17.1 px | 0.61 | 0.09 | 601 |
| spiral | 21 % → 1 % | 13.6 px | 0.61 | 0.04 | 438 |
| loop | 13 % → 2 % | 17.3 px | 0.61 | 0.12 | 273 |
| tilted | 7 % → 7 % | 20.7 px | 0.61 | 0.97 | 128 |
| over the wet one | 14 % → 3 % | 18.8 px | 0.61 | 0.24 | 154 |
| long, no reload | 21 % → 2 % | 9.6 px | 0.61 | 0.07 | 655 | quarters: 0.24 → 0.14 → 0.08 → 0.06

Numbers say: light vs heavy: width 10.7 → 21.4 px, dark 0.61 → 0.61.

## Brush Artist · Refs · #09 Henry Ward white loops
Gouache 1.00 · 46 px · 34.2 s

![Brush Artist · Refs · #09 Henry Ward white loops](Brush-Artist-Refs-09-Henry-Ward-white-loops.png)

A light paint: laid on a grey sheet (on white it cannot be seen); **dark** = how far it is from the grey either way.

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 10 % → 4 % | 29.4 px | 0.45 | 0.44 | 153 |
| heavy line | 12 % → 6 % | 35.0 px | 0.45 | 0.48 | 151 |
| pressure swell | 9 % → 6 % | 33.6 px | 0.45 | 0.65 | 89 |
| fast wave | 23 % → 3 % | 26.4 px | 0.45 | 0.14 | 397 |
| slow wave | 26 % → 9 % | 30.0 px | 0.44 | 0.35 | 882 |
| spiral | 31 % → 6 % | 20.5 px | 0.44 | 0.20 | 778 |
| loop | 23 % → 7 % | 29.6 px | 0.44 | 0.29 | 371 |
| tilted | 12 % → 12 % | 34.7 px | 0.45 | 0.99 | 188 |
| over the wet one | 23 % → 11 % | 30.0 px | 0.45 | 0.50 | 133 |
| long, no reload | 25 % → 9 % | 11.0 px | 0.44 | 0.37 | 749 | quarters: 0.01 → 0.02 → 0.03 → 0.03

Numbers say: light vs heavy: width 29.4 → 35.0 px, dark 0.45 → 0.45; the long stroke does not run out of paint.

## Brush Artist · Refs · #10 Henry Ward maroon loops
Impasto 1.00 · 30 px · 16.9 s

![Brush Artist · Refs · #10 Henry Ward maroon loops](Brush-Artist-Refs-10-Henry-Ward-maroon-loops.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 9 % → 8 % | 26.6 px | 0.70 | 0.91 | 113 |
| heavy line | 10 % → 9 % | 28.7 px | 0.70 | 0.93 | 100 |
| pressure swell | 8 % → 7 % | 28.3 px | 0.74 | 0.92 | 62 |
| fast wave | 23 % → 16 % | 26.2 px | 0.73 | 0.72 | 294 |
| slow wave | 24 % → 18 % | 27.4 px | 0.73 | 0.76 | 428 |
| spiral | 36 % → 18 % | 23.6 px | 0.73 | 0.52 | 409 |
| loop | 20 % → 17 % | 26.0 px | 0.73 | 0.83 | 273 |
| tilted | 10 % → 10 % | 28.0 px | 0.72 | 1.00 | 130 |
| over the wet one | 19 % → 17 % | 25.5 px | 0.72 | 0.91 | 135 |
| long, no reload | 42 % → 19 % | 19.0 px | 0.73 | 0.44 | 752 | quarters: 0.42 → 0.35 → 0.29 → 0.22

Numbers say: light vs heavy: width 26.6 → 28.7 px, dark 0.70 → 0.70; pressure barely changes the width.

## Brush Artist · Refs · #11 Henry Ward purple spun balls
Impasto 1.00 · 36 px · 16.7 s

![Brush Artist · Refs · #11 Henry Ward purple spun balls](Brush-Artist-Refs-11-Henry-Ward-purple-spun-balls.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 11 % → 11 % | 32.8 px | 0.70 | 0.93 | 106 |
| heavy line | 12 % → 11 % | 34.9 px | 0.70 | 0.94 | 106 |
| pressure swell | 9 % → 9 % | 35.0 px | 0.75 | 0.94 | 93 |
| fast wave | 27 % → 22 % | 31.5 px | 0.75 | 0.80 | 393 |
| slow wave | 28 % → 23 % | 32.8 px | 0.75 | 0.82 | 510 |
| spiral | 44 % → 25 % | 29.1 px | 0.74 | 0.56 | 458 |
| loop | 24 % → 21 % | 31.2 px | 0.74 | 0.87 | 223 |
| tilted | 11 % → 11 % | 30.2 px | 0.73 | 1.00 | 121 |
| over the wet one | 22 % → 20 % | 31.0 px | 0.73 | 0.92 | 114 |
| long, no reload | 50 % → 25 % | 22.6 px | 0.75 | 0.49 | 633 | quarters: 0.50 → 0.42 → 0.36 → 0.28

Numbers say: light vs heavy: width 32.8 → 34.9 px, dark 0.70 → 0.70; pressure barely changes the width.

## Brush Artist · Refs · #12 Henry Ward black-olive cage
Gouache 1.00 · 28 px · 24.7 s

![Brush Artist · Refs · #12 Henry Ward black-olive cage](Brush-Artist-Refs-12-Henry-Ward-black-olive-cage.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 4 % → 0 % | 11.3 px | 0.64 | 0.09 | 58 |
| heavy line | 7 % → 1 % | 18.9 px | 0.64 | 0.08 | 116 |
| pressure swell | 5 % → 1 % | 17.5 px | 0.64 | 0.17 | 68 |
| fast wave | 9 % → 1 % | 10.5 px | 0.64 | 0.12 | 189 |
| slow wave | 13 % → 1 % | 15.0 px | 0.64 | 0.09 | 497 |
| spiral | 19 % → 1 % | 12.4 px | 0.64 | 0.06 | 430 |
| loop | 12 % → 2 % | 14.9 px | 0.64 | 0.14 | 202 |
| tilted | 6 % → 6 % | 17.9 px | 0.64 | 0.96 | 117 |
| over the wet one | 12 % → 3 % | 16.6 px | 0.64 | 0.26 | 86 |
| long, no reload | 20 % → 2 % | 9.0 px | 0.64 | 0.08 | 537 | quarters: 0.23 → 0.14 → 0.09 → 0.07

Numbers say: light vs heavy: width 11.3 → 18.9 px, dark 0.64 → 0.64.

## Brush Artist · Refs · #13 Henry Ward blue streaky form
Gouache 1.00 · 50 px · 35.1 s

![Brush Artist · Refs · #13 Henry Ward blue streaky form](Brush-Artist-Refs-13-Henry-Ward-blue-streaky-form.png)

A light paint: laid on a grey sheet (on white it cannot be seen); **dark** = how far it is from the grey either way.

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 10 % → 7 % | 29.4 px | 0.35 | 0.71 | 157 |
| heavy line | 12 % → 8 % | 34.1 px | 0.35 | 0.65 | 169 |
| pressure swell | 10 % → 6 % | 36.0 px | 0.35 | 0.64 | 109 |
| fast wave | 19 % → 8 % | 22.4 px | 0.35 | 0.41 | 437 |
| slow wave | 27 % → 12 % | 30.8 px | 0.35 | 0.45 | 893 |
| spiral | 25 % → 11 % | 16.7 px | 0.35 | 0.42 | 749 |
| loop | 20 % → 11 % | 25.5 px | 0.35 | 0.56 | 317 |
| tilted | 12 % → 12 % | 33.9 px | 0.35 | 0.99 | 220 |
| over the wet one | 23 % → 17 % | 29.0 px | 0.35 | 0.76 | 161 |
| long, no reload | 29 % → 13 % | 12.9 px | 0.35 | 0.44 | 1025 | quarters: 0.01 → 0.02 → 0.02 → 0.02

Numbers say: light vs heavy: width 29.4 → 34.1 px, dark 0.35 → 0.35; the long stroke does not run out of paint.

## Brush Artist · Refs · #14 Henry Ward olive totem
Impasto 1.00 · 48 px · 20.5 s

![Brush Artist · Refs · #14 Henry Ward olive totem](Brush-Artist-Refs-14-Henry-Ward-olive-totem.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 15 % → 14 % | 44.1 px | 0.30 | 0.93 | 131 |
| heavy line | 16 % → 15 % | 46.7 px | 0.30 | 0.94 | 133 |
| pressure swell | 12 % → 12 % | 46.2 px | 0.32 | 0.95 | 114 |
| fast wave | 37 % → 30 % | 43.1 px | 0.30 | 0.80 | 407 |
| slow wave | 38 % → 31 % | 44.4 px | 0.30 | 0.82 | 891 |
| spiral | 55 % → 31 % | 36.4 px | 0.30 | 0.57 | 861 |
| loop | 32 % → 28 % | 42.0 px | 0.30 | 0.88 | 347 |
| tilted | 13 % → 13 % | 37.2 px | 0.31 | 1.00 | 215 |
| over the wet one | 28 % → 26 % | 40.5 px | 0.31 | 0.93 | 182 |
| long, no reload | 66 % → 33 % | 29.4 px | 0.30 | 0.51 | 894 | quarters: 0.25 → 0.18 → 0.10 → 0.05

Numbers say: light vs heavy: width 44.1 → 46.7 px, dark 0.30 → 0.30; pressure barely changes the width.

## Brush Artist · Refs · #15 Ultramarine brush script
Ink 1.00 · 4 px · 24.4 s

![Brush Artist · Refs · #15 Ultramarine brush script](Brush-Artist-Refs-15-Ultramarine-brush-script.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 1 % → 3 % | 2.2 px | 0.55 | 3.90 | 37 |
| heavy line | 6 % → 6 % | 16.7 px | 0.58 | 0.99 | 67 |
| pressure swell | 3 % → 4 % | 12.1 px | 0.64 | 1.15 | 38 |
| fast wave | 9 % → 7 % | 10.6 px | 0.54 | 0.81 | 82 |
| slow wave | 7 % → 7 % | 8.4 px | 0.54 | 0.93 | 102 |
| spiral | 11 % → 7 % | 7.2 px | 0.52 | 0.66 | 145 |
| loop | 7 % → 7 % | 9.2 px | 0.53 | 0.98 | 65 |
| tilted | 3 % → 3 % | 8.2 px | 0.62 | 1.02 | 42 |
| over the wet one | 7 % → 7 % | 11.5 px | 0.62 | 1.06 | 35 |
| long, no reload | 16 % → 8 % | 7.3 px | 0.50 | 0.48 | 235 | quarters: 0.15 → 0.04 → 0.01 → 0.00

Numbers say: light vs heavy: width 2.2 → 16.7 px, dark 0.55 → 0.58; wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #18 Blue oil-stick scribbles
Pastel 1.00 · 10 px · 10.8 s

![Brush Artist · Refs · #18 Blue oil-stick scribbles](Brush-Artist-Refs-18-Blue-oil-stick-scribbles.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 1 % → 1 % | 2.9 px | 0.52 | 1.00 | 21 |
| heavy line | 2 % → 2 % | 5.5 px | 0.53 | 1.00 | 27 |
| pressure swell | 1 % → 1 % | 5.0 px | 0.53 | 1.00 | 21 |
| fast wave | 4 % → 4 % | 4.8 px | 0.53 | 1.00 | 56 |
| slow wave | 4 % → 4 % | 4.4 px | 0.53 | 1.00 | 48 |
| spiral | 7 % → 7 % | 4.5 px | 0.52 | 1.00 | 97 |
| loop | 3 % → 3 % | 4.5 px | 0.52 | 1.00 | 68 |
| tilted | 2 % → 2 % | 4.8 px | 0.53 | 1.00 | 27 |
| over the wet one | 3 % → 3 % | 4.7 px | 0.53 | 1.00 | 27 |
| long, no reload | 10 % → 10 % | 4.4 px | 0.53 | 1.00 | 186 | quarters: 0.06 → 0.06 → 0.06 → 0.06

Numbers say: light vs heavy: width 2.9 → 5.5 px, dark 0.52 → 0.53; the long stroke does not run out of paint.

## Brush Artist · Refs · #20 Orange-red crayon scribble
Pastel 1.00 · 14 px · 11.2 s

![Brush Artist · Refs · #20 Orange-red crayon scribble](Brush-Artist-Refs-20-Orange-red-crayon-scribble.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 1 % → 1 % | 4.0 px | 0.53 | 1.00 | 21 |
| heavy line | 3 % → 3 % | 8.0 px | 0.53 | 1.00 | 28 |
| pressure swell | 2 % → 2 % | 7.6 px | 0.53 | 1.00 | 22 |
| fast wave | 6 % → 6 % | 7.2 px | 0.53 | 1.00 | 67 |
| slow wave | 6 % → 6 % | 6.6 px | 0.53 | 1.00 | 62 |
| spiral | 9 % → 9 % | 6.2 px | 0.53 | 1.00 | 133 |
| loop | 5 % → 5 % | 6.2 px | 0.53 | 1.00 | 72 |
| tilted | 2 % → 2 % | 5.6 px | 0.53 | 1.00 | 35 |
| over the wet one | 4 % → 4 % | 6.6 px | 0.53 | 1.00 | 26 |
| long, no reload | 13 % → 13 % | 5.7 px | 0.53 | 1.00 | 174 | quarters: 0.07 → 0.07 → 0.08 → 0.08

Numbers say: light vs heavy: width 4.0 → 8.0 px, dark 0.53 → 0.53; the long stroke does not run out of paint.

## Brush Artist · Refs · #21 Gritty black contours
Gouache 1.00 · 12 px · 18.2 s

![Brush Artist · Refs · #21 Gritty black contours](Brush-Artist-Refs-21-Gritty-black-contours.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 1 % → 0 % | 2.8 px | 0.81 | 0.02 | 73 |
| heavy line | 2 % → 0 % | 6.1 px | 0.00 | 0.00 | 104 |
| pressure swell | 2 % → 0 % | 6.2 px | 0.81 | 0.03 | 78 |
| fast wave | 2 % → 0 % | 2.3 px | 0.00 | 0.00 | 196 |
| slow wave | 4 % → 0 % | 4.1 px | 0.81 | 0.02 | 210 |
| spiral | 4 % → 0 % | 2.9 px | 0.81 | 0.01 | 412 |
| loop | 3 % → 0 % | 4.3 px | 0.81 | 0.01 | 200 |
| tilted | 3 % → 2 % | 7.1 px | 0.81 | 0.89 | 71 |
| over the wet one | 4 % → 0 % | 5.1 px | 0.81 | 0.04 | 107 |
| long, no reload | 5 % → 0 % | 2.2 px | 0.81 | 0.01 | 629 | quarters: 0.10 → 0.04 → 0.03 → 0.02

Numbers say: light vs heavy: width 2.8 → 6.1 px, dark 0.81 → 0.00.

## Brush Artist · Refs · #22 Bold black brush poster
Ink 1.00 · 20 px · 28.0 s

![Brush Artist · Refs · #22 Bold black brush poster](Brush-Artist-Refs-22-Bold-black-brush-poster.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 3 % → 5 % | 9.6 px | 0.79 | 1.64 | 38 |
| heavy line | 15 % → 15 % | 44.6 px | 0.88 | 0.99 | 110 |
| pressure swell | 9 % → 9 % | 31.9 px | 0.87 | 1.04 | 51 |
| fast wave | 27 % → 27 % | 31.7 px | 0.87 | 0.98 | 196 |
| slow wave | 22 % → 22 % | 25.3 px | 0.87 | 0.99 | 216 |
| spiral | 34 % → 32 % | 22.4 px | 0.87 | 0.94 | 255 |
| loop | 20 % → 20 % | 26.3 px | 0.88 | 1.00 | 130 |
| tilted | 8 % → 8 % | 23.1 px | 0.88 | 1.01 | 57 |
| over the wet one | 19 % → 19 % | 30.3 px | 0.88 | 1.00 | 88 |
| long, no reload | 45 % → 38 % | 20.3 px | 0.86 | 0.83 | 363 | quarters: 0.54 → 0.45 → 0.35 → 0.26

Numbers say: light vs heavy: width 9.6 → 44.6 px, dark 0.79 → 0.88; wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #23 Dry white on orange + black line
Gouache 1.00 · 50 px · 21.9 s

![Brush Artist · Refs · #23 Dry white on orange + black line](Brush-Artist-Refs-23-Dry-white-on-orange-black-line.png)

A light paint: laid on a grey sheet (on white it cannot be seen); **dark** = how far it is from the grey either way.

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 6 % → 0 % | 17.3 px | 0.00 | 0.00 | 88 |
| heavy line | 10 % → 0 % | 29.7 px | 0.41 | 0.00 | 234 |
| pressure swell | 7 % → 0 % | 27.2 px | 0.41 | 0.02 | 113 |
| fast wave | 13 % → 0 % | 15.3 px | 0.41 | 0.01 | 437 |
| slow wave | 20 % → 0 % | 22.8 px | 0.40 | 0.02 | 626 |
| spiral | 23 % → 0 % | 15.4 px | 0.40 | 0.01 | 539 |
| loop | 17 % → 0 % | 22.5 px | 0.40 | 0.03 | 284 |
| tilted | 9 % → 8 % | 24.0 px | 0.40 | 0.93 | 166 |
| over the wet one | 17 % → 1 % | 23.3 px | 0.40 | 0.08 | 144 |
| long, no reload | 27 % → 1 % | 12.2 px | 0.40 | 0.03 | 804 | quarters: 0.02 → 0.03 → 0.03 → 0.03

Numbers say: light vs heavy: width 17.3 → 29.7 px, dark 0.00 → 0.41; the long stroke does not run out of paint.

## Brush Artist · Refs · #24 Picasso flat oil
Oil 0.89 · Oil glaze 0.11 · 34 px · 18.5 s

![Brush Artist · Refs · #24 Picasso flat oil](Brush-Artist-Refs-24-Picasso-flat-oil.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 10 % → 10 % | 28.0 px | 0.38 | 1.00 | 126 |
| heavy line | 10 % → 10 % | 30.4 px | 0.39 | 1.00 | 154 |
| pressure swell | 8 % → 8 % | 29.5 px | 0.41 | 1.00 | 78 |
| fast wave | 25 % → 25 % | 29.0 px | 0.41 | 1.00 | 297 |
| slow wave | 27 % → 27 % | 30.6 px | 0.40 | 1.00 | 515 |
| spiral | 41 % → 41 % | 27.3 px | 0.40 | 1.00 | 520 |
| loop | 22 % → 22 % | 28.2 px | 0.40 | 1.00 | 257 |
| tilted | 11 % → 11 % | 31.3 px | 0.39 | 1.00 | 143 |
| over the wet one | 21 % → 21 % | 26.9 px | 0.39 | 1.00 | 131 |
| long, no reload | 51 % → 51 % | 22.9 px | 0.40 | 1.00 | 792 | quarters: 0.25 → 0.23 → 0.21 → 0.20

Numbers say: light vs heavy: width 28.0 → 30.4 px, dark 0.38 → 0.39; pressure barely changes the width.

## Brush Artist · Refs · #25 Yellow heavy flat stroke
Impasto 1.00 · 110 px · 36.3 s

![Brush Artist · Refs · #25 Yellow heavy flat stroke](Brush-Artist-Refs-25-Yellow-heavy-flat-stroke.png)

A light paint: laid on a grey sheet (on white it cannot be seen); **dark** = how far it is from the grey either way.

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 35 % → 36 % | 101.5 px | 0.30 | 1.02 | 364 |
| heavy line | 36 % → 35 % | 105.1 px | 0.31 | 0.97 | 404 |
| pressure swell | 28 % → 29 % | 105.5 px | 0.30 | 1.04 | 277 |
| fast wave | 73 % → 76 % | 83.8 px | 0.31 | 1.05 | 974 |
| slow wave | 73 % → 72 % | 84.7 px | 0.30 | 0.98 | 1729 |
| spiral | 86 % → 83 % | 56.7 px | 0.29 | 0.97 | 1922 |
| loop | 65 % → 64 % | 83.6 px | 0.31 | 0.99 | 849 |
| tilted | 26 % → 26 % | 71.5 px | 0.30 | 1.00 | 492 |
| over the wet one | 55 % → 54 % | 83.2 px | 0.30 | 0.97 | 476 |
| long, no reload | 98 % → 97 % | 44.1 px | 0.30 | 0.99 | 2693 | quarters: 0.00 → 0.00 → 0.00 → 0.00

Numbers say: light vs heavy: width 101.5 → 105.1 px, dark 0.30 → 0.31; pressure barely changes the width; the long stroke does not run out of paint.

## Brush Artist · Refs · #27 Orange impasto swatch
Impasto 1.00 · 60 px · 21.5 s

![Brush Artist · Refs · #27 Orange impasto swatch](Brush-Artist-Refs-27-Orange-impasto-swatch.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 20 % → 19 % | 56.9 px | 0.34 | 0.97 | 178 |
| heavy line | 20 % → 20 % | 59.5 px | 0.34 | 0.97 | 186 |
| pressure swell | 16 % → 15 % | 59.6 px | 0.36 | 0.97 | 144 |
| fast wave | 48 % → 47 % | 55.1 px | 0.35 | 0.98 | 475 |
| slow wave | 48 % → 47 % | 55.9 px | 0.35 | 0.98 | 822 |
| spiral | 69 % → 62 % | 45.5 px | 0.34 | 0.91 | 782 |
| loop | 42 % → 40 % | 53.9 px | 0.35 | 0.97 | 403 |
| tilted | 16 % → 16 % | 44.0 px | 0.35 | 1.00 | 280 |
| over the wet one | 34 % → 33 % | 50.9 px | 0.35 | 0.96 | 207 |
| long, no reload | 85 % → 75 % | 38.1 px | 0.35 | 0.88 | 1212 | quarters: 0.33 → 0.31 → 0.30 → 0.26

Numbers say: light vs heavy: width 56.9 → 59.5 px, dark 0.34 → 0.34; pressure barely changes the width.

## Brush Artist · Refs · #28 Miles Davis black lines
Ink 1.00 · 22 px · 28.1 s

![Brush Artist · Refs · #28 Miles Davis black lines](Brush-Artist-Refs-28-Miles-Davis-black-lines.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 4 % → 6 % | 12.2 px | 0.81 | 1.49 | 41 |
| heavy line | 17 % → 17 % | 49.0 px | 0.88 | 0.99 | 85 |
| pressure swell | 10 % → 10 % | 35.9 px | 0.87 | 1.03 | 54 |
| fast wave | 31 % → 30 % | 35.4 px | 0.87 | 0.98 | 143 |
| slow wave | 25 % → 25 % | 28.7 px | 0.87 | 0.99 | 261 |
| spiral | 39 % → 37 % | 25.5 px | 0.87 | 0.95 | 233 |
| loop | 23 % → 23 % | 29.6 px | 0.88 | 1.00 | 146 |
| tilted | 9 % → 9 % | 25.3 px | 0.88 | 1.01 | 58 |
| over the wet one | 21 % → 21 % | 34.1 px | 0.88 | 1.01 | 83 |
| long, no reload | 51 % → 43 % | 22.9 px | 0.86 | 0.84 | 395 | quarters: 0.59 → 0.51 → 0.40 → 0.31

Numbers say: light vs heavy: width 12.2 → 49.0 px, dark 0.81 → 0.88.

## Brush Artist · Refs · #29 Shrigley magenta asterisk
Watercolour 1.00 · 70 px · 31.9 s

![Brush Artist · Refs · #29 Shrigley magenta asterisk](Brush-Artist-Refs-29-Shrigley-magenta-asterisk.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 10 % → 13 % | 28.0 px | 0.61 | 1.39 | 52 |
| heavy line | 17 % → 18 % | 50.3 px | 0.61 | 1.04 | 123 |
| pressure swell | 11 % → 13 % | 41.1 px | 0.62 | 1.14 | 77 |
| fast wave | 38 % → 38 % | 43.8 px | 0.60 | 1.01 | 280 |
| slow wave | 35 % → 39 % | 41.0 px | 0.62 | 1.11 | 426 |
| spiral | 61 % → 61 % | 40.0 px | 0.60 | 1.01 | 413 |
| loop | 31 % → 32 % | 40.2 px | 0.61 | 1.03 | 251 |
| tilted | 18 % → 18 % | 49.0 px | 0.61 | 1.00 | 216 |
| over the wet one | 31 % → 34 % | 38.5 px | 0.61 | 1.08 | 106 |
| long, no reload | 75 % → 76 % | 33.6 px | 0.60 | 1.01 | 701 | quarters: 0.53 → 0.50 → 0.48 → 0.45

Numbers say: light vs heavy: width 28.0 → 50.3 px, dark 0.61 → 0.61; the long stroke does not run out of paint.

## Brush Artist · Refs · #30 Red gouache face patch
Gouache 1.00 · 60 px · 40.5 s

![Brush Artist · Refs · #30 Red gouache face patch](Brush-Artist-Refs-30-Red-gouache-face-patch.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 16 % → 15 % | 47.0 px | 0.49 | 0.91 | 143 |
| heavy line | 25 % → 20 % | 73.9 px | 0.49 | 0.80 | 190 |
| pressure swell | 19 % → 17 % | 72.6 px | 0.49 | 0.86 | 161 |
| fast wave | 49 % → 28 % | 56.1 px | 0.49 | 0.58 | 374 |
| slow wave | 48 % → 28 % | 55.4 px | 0.49 | 0.59 | 703 |
| spiral | 60 % → 28 % | 39.3 px | 0.49 | 0.47 | 713 |
| loop | 40 % → 29 % | 51.6 px | 0.49 | 0.74 | 422 |
| tilted | 16 % → 17 % | 46.0 px | 0.49 | 1.00 | 221 |
| over the wet one | 36 % → 32 % | 55.3 px | 0.49 | 0.89 | 169 |
| long, no reload | 67 % → 30 % | 30.0 px | 0.49 | 0.44 | 1173 | quarters: 0.43 → 0.39 → 0.32 → 0.26

Numbers say: light vs heavy: width 47.0 → 73.9 px, dark 0.49 → 0.49.

## Brush Artist · Refs · #31 Warhol blotted line
Ink 1.00 · 6 px · 23.1 s

![Brush Artist · Refs · #31 Warhol blotted line](Brush-Artist-Refs-31-Warhol-blotted-line.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 1 % → 3 % | 2.7 px | 0.75 | 3.31 | 29 |
| heavy line | 7 % → 7 % | 20.7 px | 0.83 | 0.98 | 56 |
| pressure swell | 4 % → 4 % | 14.8 px | 0.84 | 1.12 | 27 |
| fast wave | 12 % → 9 % | 13.9 px | 0.82 | 0.76 | 115 |
| slow wave | 10 % → 8 % | 11.2 px | 0.80 | 0.84 | 112 |
| spiral | 15 % → 8 % | 9.7 px | 0.80 | 0.58 | 165 |
| loop | 9 % → 9 % | 11.9 px | 0.80 | 0.93 | 81 |
| tilted | 3 % → 3 % | 8.8 px | 0.84 | 1.03 | 46 |
| over the wet one | 8 % → 8 % | 14.4 px | 0.84 | 1.02 | 41 |
| long, no reload | 21 % → 9 % | 9.5 px | 0.78 | 0.43 | 281 | quarters: 0.25 → 0.13 → 0.04 → 0.01

Numbers say: light vs heavy: width 2.7 → 20.7 px, dark 0.75 → 0.83; wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #32 Thick orange swipes
Impasto 1.00 · 90 px · 34.2 s

![Brush Artist · Refs · #32 Thick orange swipes](Brush-Artist-Refs-32-Thick-orange-swipes.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 29 % → 29 % | 83.2 px | 0.37 | 1.00 | 300 |
| heavy line | 30 % → 29 % | 86.5 px | 0.38 | 0.97 | 325 |
| pressure swell | 23 % → 23 % | 86.6 px | 0.38 | 1.01 | 239 |
| fast wave | 63 % → 65 % | 73.1 px | 0.38 | 1.03 | 810 |
| slow wave | 64 % → 63 % | 73.5 px | 0.38 | 0.98 | 1658 |
| spiral | 79 % → 77 % | 52.2 px | 0.38 | 0.98 | 1810 |
| loop | 57 % → 56 % | 73.4 px | 0.38 | 0.99 | 745 |
| tilted | 21 % → 21 % | 59.3 px | 0.38 | 1.00 | 480 |
| over the wet one | 47 % → 45 % | 71.0 px | 0.38 | 0.97 | 393 |
| long, no reload | 95 % → 93 % | 42.8 px | 0.38 | 0.98 | 2227 | quarters: 0.38 → 0.38 → 0.37 → 0.35

Numbers say: light vs heavy: width 83.2 → 86.5 px, dark 0.37 → 0.38; pressure barely changes the width; the long stroke does not run out of paint.

## Brush Artist · Refs · #33 Red wet-in-wet band
Watercolour 1.00 · 80 px · 48.7 s

![Brush Artist · Refs · #33 Red wet-in-wet band](Brush-Artist-Refs-33-Red-wet-in-wet-band.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 24 % → 42 % | 69.9 px | 0.53 | 1.73 | 174 |
| heavy line | 34 % → 50 % | 97.7 px | 0.54 | 1.48 | 281 |
| pressure swell | 20 % → 30 % | 73.7 px | 0.57 | 1.54 | 185 |
| fast wave | 65 % → 80 % | 75.4 px | 0.61 | 1.22 | 540 |
| slow wave | 61 % → 78 % | 70.0 px | 0.63 | 1.29 | 860 |
| spiral | 78 % → 89 % | 51.5 px | 0.64 | 1.15 | 909 |
| loop | 54 % → 68 % | 70.2 px | 0.62 | 1.25 | 458 |
| tilted | 28 % → 30 % | 77.1 px | 0.57 | 1.08 | 369 |
| over the wet one | 55 % → 79 % | 75.2 px | 0.57 | 1.45 | 232 |
| long, no reload | 96 % → 99 % | 43.2 px | 0.66 | 1.03 | 1497 | quarters: 0.68 → 0.68 → 0.68 → 0.63

Numbers say: light vs heavy: width 69.9 → 97.7 px, dark 0.53 → 0.54; the long stroke does not run out of paint; wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #34 Magenta oil patches
Oil 0.89 · Oil glaze 0.11 · 60 px · 23.4 s

![Brush Artist · Refs · #34 Magenta oil patches](Brush-Artist-Refs-34-Magenta-oil-patches.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 18 % → 18 % | 52.7 px | 0.60 | 1.01 | 243 |
| heavy line | 20 % → 20 % | 57.0 px | 0.61 | 1.00 | 366 |
| pressure swell | 15 % → 15 % | 55.7 px | 0.62 | 1.01 | 176 |
| fast wave | 48 % → 48 % | 55.0 px | 0.61 | 1.02 | 591 |
| slow wave | 48 % → 48 % | 55.7 px | 0.61 | 1.00 | 1002 |
| spiral | 71 % → 71 % | 46.8 px | 0.61 | 1.00 | 1031 |
| loop | 41 % → 41 % | 53.3 px | 0.61 | 1.00 | 554 |
| tilted | 16 % → 16 % | 46.0 px | 0.60 | 1.00 | 295 |
| over the wet one | 34 % → 34 % | 47.8 px | 0.60 | 1.00 | 239 |
| long, no reload | 83 % → 83 % | 37.1 px | 0.61 | 1.00 | 1495 | quarters: 0.57 → 0.56 → 0.54 → 0.47

Numbers say: light vs heavy: width 52.7 → 57.0 px, dark 0.60 → 0.61; pressure barely changes the width.

## Brush Artist · Refs · #35 Red band with runs
Watercolour 1.00 · 70 px · 50.7 s

![Brush Artist · Refs · #35 Red band with runs](Brush-Artist-Refs-35-Red-band-with-runs.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 40 % → 45 % | 115.4 px | 0.42 | 1.14 | 141 |
| heavy line | 46 % → 51 % | 133.2 px | 0.42 | 1.12 | 325 |
| pressure swell | 21 % → 28 % | 77.8 px | 0.48 | 1.36 | 168 |
| fast wave | 67 % → 77 % | 77.5 px | 0.49 | 1.14 | 602 |
| slow wave | 65 % → 75 % | 75.0 px | 0.52 | 1.16 | 1013 |
| spiral | 87 % → 94 % | 57.4 px | 0.53 | 1.09 | 912 |
| loop | 79 % → 88 % | 102.3 px | 0.48 | 1.11 | 439 |
| tilted | 50 % → 50 % | 138.2 px | 0.47 | 1.02 | 241 |
| over the wet one | 77 % → 84 % | 76.2 px | 0.47 | 1.10 | 166 |
| long, no reload | 97 % → 100 % | 43.5 px | 0.58 | 1.03 | 1161 | quarters: 0.60 → 0.60 → 0.59 → 0.56

Numbers say: light vs heavy: width 115.4 → 133.2 px, dark 0.42 → 0.42; the long stroke does not run out of paint.

## Brush Artist · Refs · #36 Magenta letters flat brush
Gouache 1.00 · 36 px · 34.2 s

![Brush Artist · Refs · #36 Magenta letters flat brush](Brush-Artist-Refs-36-Magenta-letters-flat-brush.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 10 % → 10 % | 29.0 px | 0.45 | 0.98 | 84 |
| heavy line | 17 % → 14 % | 49.0 px | 0.45 | 0.85 | 110 |
| pressure swell | 13 % → 12 % | 49.3 px | 0.45 | 0.89 | 86 |
| fast wave | 35 % → 19 % | 40.9 px | 0.45 | 0.54 | 251 |
| slow wave | 35 % → 19 % | 40.0 px | 0.45 | 0.54 | 464 |
| spiral | 46 % → 19 % | 30.4 px | 0.45 | 0.42 | 484 |
| loop | 27 % → 20 % | 35.4 px | 0.45 | 0.72 | 221 |
| tilted | 11 % → 11 % | 30.0 px | 0.45 | 1.00 | 151 |
| over the wet one | 24 % → 23 % | 38.1 px | 0.45 | 0.93 | 89 |
| long, no reload | 46 % → 19 % | 20.8 px | 0.45 | 0.40 | 570 | quarters: 0.29 → 0.26 → 0.22 → 0.18

Numbers say: light vs heavy: width 29.0 → 49.0 px, dark 0.45 → 0.45.

## Brush Artist · Refs · #37 Oil still life dabs
Oil 0.89 · Oil glaze 0.11 · 40 px · 20.0 s

![Brush Artist · Refs · #37 Oil still life dabs](Brush-Artist-Refs-37-Oil-still-life-dabs.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 12 % → 12 % | 35.4 px | 0.36 | 1.00 | 172 |
| heavy line | 13 % → 13 % | 38.6 px | 0.36 | 1.00 | 174 |
| pressure swell | 10 % → 10 % | 37.8 px | 0.40 | 1.00 | 106 |
| fast wave | 31 % → 31 % | 36.3 px | 0.39 | 1.00 | 469 |
| slow wave | 33 % → 33 % | 38.0 px | 0.39 | 1.00 | 662 |
| spiral | 51 % → 51 % | 33.9 px | 0.38 | 1.00 | 715 |
| loop | 27 % → 27 % | 35.4 px | 0.39 | 1.00 | 315 |
| tilted | 13 % → 13 % | 35.5 px | 0.38 | 1.00 | 188 |
| over the wet one | 25 % → 25 % | 33.6 px | 0.38 | 1.00 | 233 |
| long, no reload | 61 % → 61 % | 27.2 px | 0.38 | 1.00 | 1058 | quarters: 0.29 → 0.26 → 0.24 → 0.21

Numbers say: light vs heavy: width 35.4 → 38.6 px, dark 0.36 → 0.36; pressure barely changes the width.

## Brush Artist · Refs · #38 Sanguine drawing
Pastel 1.00 · 6 px · 9.8 s

![Brush Artist · Refs · #38 Sanguine drawing](Brush-Artist-Refs-38-Sanguine-drawing.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 1 % → 1 % | 2.0 px | 0.61 | 1.00 | 17 |
| heavy line | 1 % → 1 % | 3.5 px | 0.62 | 1.00 | 27 |
| pressure swell | 1 % → 1 % | 3.3 px | 0.62 | 1.00 | 17 |
| fast wave | 3 % → 3 % | 3.2 px | 0.61 | 1.00 | 46 |
| slow wave | 3 % → 3 % | 3.0 px | 0.61 | 1.00 | 45 |
| spiral | 4 % → 4 % | 2.9 px | 0.61 | 1.00 | 63 |
| loop | 2 % → 2 % | 3.0 px | 0.61 | 1.00 | 42 |
| tilted | 1 % → 1 % | 3.4 px | 0.62 | 1.00 | 22 |
| over the wet one | 2 % → 2 % | 2.9 px | 0.62 | 1.00 | 22 |
| long, no reload | 7 % → 7 % | 3.0 px | 0.61 | 1.00 | 183 | quarters: 0.04 → 0.05 → 0.05 → 0.05

Numbers say: light vs heavy: width 2.0 → 3.5 px, dark 0.61 → 0.62; the long stroke does not run out of paint.

## Brush Artist · Refs · #39 Very thick impasto
Impasto 1.00 · 60 px · 22.2 s

![Brush Artist · Refs · #39 Very thick impasto](Brush-Artist-Refs-39-Very-thick-impasto.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 20 % → 19 % | 57.0 px | 0.60 | 0.97 | 174 |
| heavy line | 21 % → 20 % | 59.6 px | 0.60 | 0.97 | 285 |
| pressure swell | 16 % → 15 % | 59.7 px | 0.63 | 0.97 | 156 |
| fast wave | 48 % → 47 % | 55.2 px | 0.62 | 0.98 | 533 |
| slow wave | 49 % → 47 % | 56.1 px | 0.62 | 0.98 | 827 |
| spiral | 69 % → 65 % | 45.6 px | 0.62 | 0.93 | 970 |
| loop | 42 % → 41 % | 54.0 px | 0.62 | 0.97 | 459 |
| tilted | 16 % → 16 % | 44.1 px | 0.61 | 1.00 | 231 |
| over the wet one | 34 % → 33 % | 51.0 px | 0.61 | 0.97 | 245 |
| long, no reload | 85 % → 79 % | 38.3 px | 0.62 | 0.93 | 1741 | quarters: 0.58 → 0.57 → 0.55 → 0.52

Numbers say: light vs heavy: width 57.0 → 59.6 px, dark 0.60 → 0.60; pressure barely changes the width; the long stroke does not run out of paint.

## Brush Artist · Refs · #40 Watercolour blooms
Watercolour 1.00 · 90 px · 57.3 s

![Brush Artist · Refs · #40 Watercolour blooms](Brush-Artist-Refs-40-Watercolour-blooms.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 27 % → 46 % | 79.5 px | 0.08 | 1.69 | 166 |
| heavy line | 39 % → 53 % | 112.7 px | 0.09 | 1.36 | 343 |
| pressure swell | 26 % → 40 % | 98.0 px | 0.09 | 1.54 | 225 |
| fast wave | 68 % → 82 % | 78.6 px | 0.11 | 1.21 | 653 |
| slow wave | 68 % → 81 % | 78.9 px | 0.15 | 1.19 | 1671 |
| spiral | 83 % → 93 % | 54.4 px | 0.15 | 1.13 | 1184 |
| loop | 59 % → 72 % | 75.9 px | 0.13 | 1.24 | 501 |
| tilted | 33 % → 36 % | 93.0 px | 0.12 | 1.07 | 326 |
| over the wet one | 61 % → 81 % | 77.1 px | 0.12 | 1.33 | 229 |
| long, no reload | 98 % → 100 % | 43.9 px | 0.17 | 1.02 | 1343 | quarters: 0.21 → 0.20 → 0.17 → 0.12

Numbers say: light vs heavy: width 79.5 → 112.7 px, dark 0.08 → 0.09; wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #41 Coloured pencil hatching
Pastel 1.00 · 4 px · 9.4 s

![Brush Artist · Refs · #41 Coloured pencil hatching](Brush-Artist-Refs-41-Coloured-pencil-hatching.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 1 % → 1 % | 1.6 px | 0.42 | 1.00 | 13 |
| heavy line | 1 % → 1 % | 2.6 px | 0.43 | 1.00 | 15 |
| pressure swell | 1 % → 1 % | 2.1 px | 0.43 | 1.00 | 8 |
| fast wave | 2 % → 2 % | 2.2 px | 0.42 | 1.00 | 44 |
| slow wave | 2 % → 2 % | 2.1 px | 0.43 | 1.00 | 58 |
| spiral | 3 % → 3 % | 2.1 px | 0.43 | 1.00 | 75 |
| loop | 2 % → 2 % | 2.2 px | 0.43 | 1.00 | 34 |
| tilted | 1 % → 1 % | 3.0 px | 0.42 | 1.00 | 14 |
| over the wet one | 2 % → 2 % | 2.2 px | 0.42 | 1.00 | 9 |
| long, no reload | 5 % → 5 % | 2.3 px | 0.43 | 1.00 | 87 | quarters: 0.02 → 0.02 → 0.02 → 0.03

Numbers say: light vs heavy: width 1.6 → 2.6 px, dark 0.42 → 0.43; the long stroke does not run out of paint.

## Brush Artist · Refs · #42 Oil pastel shaggy
Pastel 1.00 · 18 px · 9.7 s

![Brush Artist · Refs · #42 Oil pastel shaggy](Brush-Artist-Refs-42-Oil-pastel-shaggy.png)

A light paint: laid on a grey sheet (on white it cannot be seen); **dark** = how far it is from the grey either way.

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 2 % → 2 % | 5.1 px | 0.35 | 1.00 | 24 |
| heavy line | 4 % → 4 % | 10.7 px | 0.36 | 1.00 | 26 |
| pressure swell | 3 % → 3 % | 9.5 px | 0.36 | 1.00 | 46 |
| fast wave | 8 % → 8 % | 9.0 px | 0.36 | 1.00 | 126 |
| slow wave | 7 % → 7 % | 8.2 px | 0.36 | 1.00 | 99 |
| spiral | 12 % → 12 % | 7.8 px | 0.36 | 1.00 | 113 |
| loop | 6 % → 6 % | 7.9 px | 0.36 | 1.00 | 57 |
| tilted | 2 % → 2 % | 6.9 px | 0.36 | 1.00 | 52 |
| over the wet one | 6 % → 6 % | 8.5 px | 0.36 | 1.00 | 20 |
| long, no reload | 15 % → 15 % | 6.9 px | 0.36 | 1.00 | 236 | quarters: 0.00 → 0.00 → 0.00 → 0.00

Numbers say: light vs heavy: width 5.1 → 10.7 px, dark 0.35 → 0.36; the long stroke does not run out of paint.

## Brush Artist · Refs · #43 Dragged black ink blocks
Gouache 1.00 · 70 px · 28.1 s

![Brush Artist · Refs · #43 Dragged black ink blocks](Brush-Artist-Refs-43-Dragged-black-ink-blocks.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 10 % → 1 % | 30.5 px | 0.65 | 0.09 | 108 |
| heavy line | 17 % → 2 % | 48.7 px | 0.65 | 0.13 | 276 |
| pressure swell | 12 % → 3 % | 44.8 px | 0.65 | 0.25 | 176 |
| fast wave | 27 % → 3 % | 30.9 px | 0.65 | 0.12 | 474 |
| slow wave | 34 % → 4 % | 38.7 px | 0.65 | 0.12 | 819 |
| spiral | 43 % → 4 % | 28.2 px | 0.65 | 0.10 | 785 |
| loop | 31 % → 4 % | 39.7 px | 0.65 | 0.14 | 501 |
| tilted | 13 % → 13 % | 37.6 px | 0.65 | 0.99 | 240 |
| over the wet one | 28 % → 10 % | 40.7 px | 0.65 | 0.37 | 195 |
| long, no reload | 48 % → 7 % | 21.6 px | 0.65 | 0.15 | 1203 | quarters: 0.49 → 0.38 → 0.30 → 0.22

Numbers say: light vs heavy: width 30.5 → 48.7 px, dark 0.65 → 0.65.

## Brush Artist · Refs · #44 Blue looping ribbon
Oil 1.00 · 80 px · 26.6 s

![Brush Artist · Refs · #44 Blue looping ribbon](Brush-Artist-Refs-44-Blue-looping-ribbon.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 25 % → 26 % | 72.8 px | 0.70 | 1.04 | 265 |
| heavy line | 27 % → 27 % | 78.1 px | 0.69 | 1.00 | 315 |
| pressure swell | 20 % → 21 % | 76.2 px | 0.72 | 1.03 | 188 |
| fast wave | 62 % → 64 % | 71.1 px | 0.72 | 1.04 | 698 |
| slow wave | 62 % → 62 % | 72.0 px | 0.73 | 1.00 | 1202 |
| spiral | 76 % → 77 % | 50.4 px | 0.72 | 1.00 | 1214 |
| loop | 55 % → 55 % | 70.7 px | 0.72 | 1.00 | 691 |
| tilted | 20 % → 20 % | 56.9 px | 0.71 | 1.00 | 344 |
| over the wet one | 43 % → 43 % | 63.7 px | 0.71 | 1.00 | 316 |
| long, no reload | 93 % → 93 % | 41.6 px | 0.73 | 1.00 | 1819 | quarters: 0.72 → 0.71 → 0.71 → 0.64

Numbers say: light vs heavy: width 72.8 → 78.1 px, dark 0.70 → 0.69; pressure barely changes the width; the long stroke does not run out of paint.

## Brush Artist · Refs · #45 Soft pastel pepper
Pastel 1.00 · 40 px · 9.7 s

![Brush Artist · Refs · #45 Soft pastel pepper](Brush-Artist-Refs-45-Soft-pastel-pepper.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 4 % → 4 % | 11.3 px | 0.53 | 1.00 | 53 |
| heavy line | 8 % → 8 % | 23.0 px | 0.53 | 1.00 | 45 |
| pressure swell | 5 % → 5 % | 19.5 px | 0.53 | 1.00 | 37 |
| fast wave | 17 % → 17 % | 19.4 px | 0.53 | 1.00 | 111 |
| slow wave | 15 % → 15 % | 17.1 px | 0.53 | 1.00 | 219 |
| spiral | 25 % → 25 % | 16.3 px | 0.53 | 1.00 | 202 |
| loop | 12 % → 12 % | 16.1 px | 0.53 | 1.00 | 103 |
| tilted | 5 % → 5 % | 12.8 px | 0.53 | 1.00 | 53 |
| over the wet one | 11 % → 11 % | 17.7 px | 0.53 | 1.00 | 48 |
| long, no reload | 30 % → 30 % | 13.6 px | 0.53 | 1.00 | 291 | quarters: 0.18 → 0.18 → 0.18 → 0.18

Numbers say: light vs heavy: width 11.3 → 23.0 px, dark 0.53 → 0.53; the long stroke does not run out of paint.

## Brush Artist · Refs · #46 Red-brown ink lips
Watercolour 1.00 · 50 px · 47.8 s

![Brush Artist · Refs · #46 Red-brown ink lips](Brush-Artist-Refs-46-Red-brown-ink-lips.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 15 % → 31 % | 43.2 px | 0.58 | 2.07 | 63 |
| heavy line | 22 % → 36 % | 62.9 px | 0.60 | 1.64 | 104 |
| pressure swell | 13 % → 22 % | 47.7 px | 0.64 | 1.71 | 64 |
| fast wave | 41 % → 64 % | 47.9 px | 0.64 | 1.55 | 292 |
| slow wave | 41 % → 63 % | 46.9 px | 0.67 | 1.54 | 359 |
| spiral | 65 % → 79 % | 42.7 px | 0.69 | 1.23 | 391 |
| loop | 37 % → 56 % | 47.7 px | 0.66 | 1.51 | 200 |
| tilted | 20 % → 23 % | 56.2 px | 0.60 | 1.12 | 138 |
| over the wet one | 41 % → 63 % | 57.1 px | 0.60 | 1.55 | 92 |
| long, no reload | 80 % → 96 % | 35.8 px | 0.70 | 1.20 | 540 | quarters: 0.71 → 0.71 → 0.70 → 0.65

Numbers say: light vs heavy: width 43.2 → 62.9 px, dark 0.58 → 0.60; the long stroke does not run out of paint; wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #47 Pink knife slabs
Impasto 1.00 · 90 px · 32.4 s

![Brush Artist · Refs · #47 Pink knife slabs](Brush-Artist-Refs-47-Pink-knife-slabs.png)

A light paint: laid on a grey sheet (on white it cannot be seen); **dark** = how far it is from the grey either way.

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 28 % → 27 % | 81.2 px | 0.29 | 0.97 | 188 |
| heavy line | 29 % → 28 % | 83.6 px | 0.29 | 0.97 | 225 |
| pressure swell | 22 % → 22 % | 83.5 px | 0.29 | 1.01 | 147 |
| fast wave | 61 % → 60 % | 70.3 px | 0.28 | 0.99 | 508 |
| slow wave | 61 % → 59 % | 71.0 px | 0.27 | 0.96 | 925 |
| spiral | 76 % → 57 % | 50.1 px | 0.27 | 0.76 | 933 |
| loop | 55 % → 54 % | 71.7 px | 0.28 | 0.97 | 456 |
| tilted | 21 % → 21 % | 59.3 px | 0.29 | 1.00 | 274 |
| over the wet one | 46 % → 44 % | 68.1 px | 0.29 | 0.96 | 218 |
| long, no reload | 92 % → 76 % | 41.4 px | 0.26 | 0.83 | 1255 | quarters: 0.00 → 0.00 → 0.00 → 0.00

Numbers say: light vs heavy: width 81.2 → 83.6 px, dark 0.29 → 0.29; pressure barely changes the width; the long stroke does not run out of paint.

## Brush Artist · Refs · #48 Black bands with drips
Gouache 1.00 · 70 px · 54.7 s

![Brush Artist · Refs · #48 Black bands with drips](Brush-Artist-Refs-48-Black-bands-with-drips.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 27 % → 24 % | 79.0 px | 0.64 | 0.87 | 166 |
| heavy line | 35 % → 29 % | 102.8 px | 0.64 | 0.82 | 251 |
| pressure swell | 25 % → 22 % | 91.9 px | 0.64 | 0.89 | 168 |
| fast wave | 64 % → 43 % | 74.0 px | 0.64 | 0.67 | 494 |
| slow wave | 61 % → 41 % | 70.7 px | 0.64 | 0.67 | 839 |
| spiral | 69 % → 39 % | 45.7 px | 0.64 | 0.56 | 809 |
| loop | 54 % → 42 % | 70.4 px | 0.64 | 0.77 | 438 |
| tilted | 29 % → 29 % | 80.7 px | 0.64 | 1.00 | 414 |
| over the wet one | 58 % → 49 % | 80.4 px | 0.64 | 0.85 | 198 |
| long, no reload | 78 % → 39 % | 34.9 px | 0.64 | 0.50 | 2933 | quarters: 0.61 → 0.57 → 0.51 → 0.42

Numbers say: light vs heavy: width 79.0 → 102.8 px, dark 0.64 → 0.64.

## Brush Artist · Refs · #49 Magenta letters round brush
Ink 1.00 · 30 px · 38.0 s

![Brush Artist · Refs · #49 Magenta letters round brush](Brush-Artist-Refs-49-Magenta-letters-round-brush.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 6 % → 8 % | 17.4 px | 0.50 | 1.29 | 42 |
| heavy line | 21 % → 21 % | 61.9 px | 0.51 | 0.99 | 100 |
| pressure swell | 12 % → 13 % | 46.3 px | 0.52 | 1.02 | 59 |
| fast wave | 39 % → 38 % | 44.8 px | 0.51 | 0.99 | 176 |
| slow wave | 32 % → 31 % | 36.7 px | 0.51 | 0.99 | 278 |
| spiral | 50 % → 49 % | 33.2 px | 0.51 | 0.97 | 290 |
| loop | 29 % → 29 % | 37.8 px | 0.51 | 1.00 | 155 |
| tilted | 11 % → 11 % | 30.9 px | 0.52 | 1.01 | 76 |
| over the wet one | 26 % → 26 % | 42.0 px | 0.52 | 1.01 | 74 |
| long, no reload | 62 % → 56 % | 27.7 px | 0.50 | 0.91 | 411 | quarters: 0.41 → 0.36 → 0.30 → 0.25

Numbers say: light vs heavy: width 17.4 → 61.9 px, dark 0.50 → 0.51.

## Brush Artist · Refs · #50 Thick swipes on photo
Impasto 1.00 · 40 px · 22.3 s

![Brush Artist · Refs · #50 Thick swipes on photo](Brush-Artist-Refs-50-Thick-swipes-on-photo.png)

A light paint: laid on a grey sheet (on white it cannot be seen); **dark** = how far it is from the grey either way.

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 13 % → 13 % | 38.1 px | 0.27 | 0.96 | 106 |
| heavy line | 14 % → 13 % | 40.2 px | 0.27 | 0.96 | 103 |
| pressure swell | 11 % → 10 % | 40.1 px | 0.25 | 0.95 | 85 |
| fast wave | 33 % → 31 % | 38.4 px | 0.25 | 0.93 | 292 |
| slow wave | 34 % → 32 % | 39.1 px | 0.26 | 0.95 | 481 |
| spiral | 58 % → 46 % | 38.5 px | 0.25 | 0.79 | 480 |
| loop | 28 % → 27 % | 36.9 px | 0.26 | 0.95 | 251 |
| tilted | 12 % → 12 % | 34.1 px | 0.26 | 1.00 | 133 |
| over the wet one | 25 % → 24 % | 35.3 px | 0.26 | 0.95 | 113 |
| long, no reload | 66 % → 46 % | 29.5 px | 0.24 | 0.69 | 722 | quarters: 0.00 → 0.00 → 0.00 → 0.00

Numbers say: light vs heavy: width 38.1 → 40.2 px, dark 0.27 → 0.27; pressure barely changes the width; the long stroke does not run out of paint.

## Brush Artist · Refs · Drag #e8b4a8
Gouache 1.00 · 40 px · 29.3 s

![Brush Artist · Refs · Drag #e8b4a8](Brush-Artist-Refs-Drag-e8b4a8.png)

A light paint: laid on a grey sheet (on white it cannot be seen); **dark** = how far it is from the grey either way.

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 4 % → 0 % | 12.7 px | 0.35 | 0.03 | 175 |
| heavy line | 5 % → 0 % | 14.4 px | 0.34 | 0.03 | 171 |
| pressure swell | 4 % → 0 % | 15.5 px | 0.34 | 0.07 | 73 |
| fast wave | 6 % → 0 % | 6.4 px | 0.34 | 0.05 | 338 |
| slow wave | 12 % → 0 % | 13.8 px | 0.34 | 0.02 | 597 |
| spiral | 10 % → 0 % | 6.6 px | 0.34 | 0.05 | 1259 |
| loop | 8 % → 1 % | 10.3 px | 0.34 | 0.09 | 285 |
| tilted | 6 % → 5 % | 16.1 px | 0.34 | 0.90 | 285 |
| over the wet one | 10 % → 1 % | 12.4 px | 0.34 | 0.15 | 185 |
| long, no reload | 9 % → 1 % | 4.0 px | 0.34 | 0.10 | 698 | quarters: 0.01 → 0.01 → 0.02 → 0.02

Numbers say: light vs heavy: width 12.7 → 14.4 px, dark 0.35 → 0.34; the long stroke does not run out of paint.

## Brush Artist · Refs · Drag #e8e4e0
Gouache 1.00 · 40 px · 28.4 s

![Brush Artist · Refs · Drag #e8e4e0](Brush-Artist-Refs-Drag-e8e4e0.png)

A light paint: laid on a grey sheet (on white it cannot be seen); **dark** = how far it is from the grey either way.

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 4 % → 0 % | 12.7 px | 0.43 | 0.03 | 155 |
| heavy line | 5 % → 0 % | 14.4 px | 0.43 | 0.03 | 255 |
| pressure swell | 4 % → 0 % | 15.5 px | 0.43 | 0.07 | 84 |
| fast wave | 6 % → 0 % | 6.4 px | 0.43 | 0.05 | 391 |
| slow wave | 12 % → 0 % | 13.8 px | 0.42 | 0.02 | 550 |
| spiral | 10 % → 0 % | 6.6 px | 0.42 | 0.05 | 984 |
| loop | 8 % → 1 % | 10.3 px | 0.42 | 0.09 | 445 |
| tilted | 6 % → 5 % | 16.1 px | 0.42 | 0.90 | 221 |
| over the wet one | 10 % → 1 % | 12.4 px | 0.42 | 0.15 | 133 |
| long, no reload | 9 % → 1 % | 4.0 px | 0.42 | 0.10 | 895 | quarters: 0.01 → 0.02 → 0.02 → 0.02

Numbers say: light vs heavy: width 12.7 → 14.4 px, dark 0.43 → 0.43; the long stroke does not run out of paint.

## Brush Artist · Refs · Finger
Pastel 1.00 · 36 px · 28.1 s · over bands of wet oil paint and oil pastel in turn (it works on paint already there: look at what it does to the bands; covered counts the bands too)

![Brush Artist · Refs · Finger](Brush-Artist-Refs-Finger.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 25 % → 25 % | 73.8 px | 0.80 | 1.00 | 55 |
| heavy line | 27 % → 27 % | 78.6 px | 0.80 | 1.00 | 177 |
| pressure swell | 26 % → 26 % | 97.7 px | 0.80 | 1.00 | 69 |
| fast wave | 32 % → 32 % | 37.3 px | 0.78 | 1.00 | 228 |
| slow wave | 31 % → 31 % | 36.3 px | 0.78 | 1.00 | 383 |
| spiral | 38 % → 38 % | 25.2 px | 0.76 | 1.00 | 271 |
| loop | 30 % → 30 % | 39.5 px | 0.78 | 1.00 | 150 |
| tilted | 26 % → 26 % | 73.4 px | 0.78 | 1.00 | 114 |
| over the wet one | 29 % → 29 % | 6.8 px | 0.78 | 1.00 | 55 |
| long, no reload | 41 % → 41 % | 18.2 px | 0.76 | 1.00 | 345 | quarters: 0.25 → 0.37 → 0.34 → 0.39

Numbers say: light vs heavy: width 73.8 → 78.6 px, dark 0.80 → 0.80; pressure barely changes the width; the long stroke does not run out of paint.

## Brush Artist · Ink — wash
Watercolour 1.00 · 38 px · 41.1 s

![Brush Artist · Ink — wash](Brush-Artist-Ink-wash.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 11 % → 11 % | 31.6 px | 0.39 | 1.04 | 58 |
| heavy line | 19 % → 19 % | 54.3 px | 0.32 | 1.03 | 126 |
| pressure swell | 12 % → 13 % | 45.2 px | 0.37 | 1.04 | 65 |
| fast wave | 39 % → 41 % | 45.5 px | 0.31 | 1.04 | 229 |
| slow wave | 37 % → 38 % | 42.9 px | 0.37 | 1.03 | 1053 |
| spiral | 58 % → 61 % | 38.6 px | 0.31 | 1.04 | 621 |
| loop | 32 % → 33 % | 41.9 px | 0.35 | 1.02 | 287 |
| tilted | 13 % → 14 % | 37.0 px | 0.38 | 1.04 | 162 |
| over the wet one | 29 % → 30 % | 42.8 px | 0.38 | 1.04 | 133 |
| long, no reload | 67 % → 72 % | 30.0 px | 0.29 | 1.07 | 589 | quarters: 0.34 → 0.27 → 0.19 → 0.12

Numbers say: light vs heavy: width 31.6 → 54.3 px, dark 0.39 → 0.32.

## Brush Artist · Ink — brush line
Ink 1.00 · 16 px · 32.7 s

![Brush Artist · Ink — brush line](Brush-Artist-Ink-brush-line.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 3 % → 5 % | 7.7 px | 0.78 | 1.81 | 56 |
| heavy line | 13 % → 13 % | 38.9 px | 0.88 | 0.99 | 105 |
| pressure swell | 8 % → 8 % | 28.4 px | 0.87 | 1.05 | 54 |
| fast wave | 24 % → 23 % | 28.0 px | 0.87 | 0.96 | 213 |
| slow wave | 20 % → 19 % | 22.6 px | 0.87 | 0.97 | 487 |
| spiral | 30 % → 27 % | 20.1 px | 0.86 | 0.89 | 475 |
| loop | 18 % → 18 % | 23.6 px | 0.88 | 1.00 | 272 |
| tilted | 7 % → 7 % | 20.5 px | 0.88 | 1.01 | 86 |
| over the wet one | 17 % → 17 % | 26.8 px | 0.88 | 1.00 | 87 |
| long, no reload | 42 % → 30 % | 18.9 px | 0.85 | 0.71 | 558 | quarters: 0.49 → 0.40 → 0.30 → 0.20

Numbers say: light vs heavy: width 7.7 → 38.9 px, dark 0.78 → 0.88; wet paint spreads well beyond the stroke.

## Brush Artist · Ink — dry brush
Gouache 1.00 · 30 px · 25.7 s

![Brush Artist · Ink — dry brush](Brush-Artist-Ink-dry-brush.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 3 % → 0 % | 9.8 px | 0.00 | 0.00 | 72 |
| heavy line | 6 % → 0 % | 16.0 px | 0.77 | 0.01 | 242 |
| pressure swell | 4 % → 0 % | 15.4 px | 0.77 | 0.05 | 73 |
| fast wave | 7 % → 0 % | 8.5 px | 0.77 | 0.05 | 382 |
| slow wave | 11 % → 0 % | 12.3 px | 0.77 | 0.03 | 510 |
| spiral | 14 % → 0 % | 9.0 px | 0.77 | 0.03 | 371 |
| loop | 9 % → 1 % | 12.0 px | 0.77 | 0.05 | 202 |
| tilted | 6 % → 5 % | 15.8 px | 0.77 | 0.94 | 114 |
| over the wet one | 10 % → 1 % | 13.2 px | 0.77 | 0.14 | 121 |
| long, no reload | 15 % → 1 % | 6.6 px | 0.77 | 0.05 | 564 | quarters: 0.23 → 0.13 → 0.09 → 0.08

Numbers say: light vs heavy: width 9.8 → 16.0 px, dark 0.00 → 0.77.

## Brush Artist · Watercolour — blue
Watercolour 0.93 · Ink 0.07 · 40 px · 33.0 s

![Brush Artist · Watercolour — blue](Brush-Artist-Watercolour-blue.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 6 % → 11 % | 16.2 px | 0.29 | 1.88 | 39 |
| heavy line | 11 % → 13 % | 31.9 px | 0.29 | 1.17 | 74 |
| pressure swell | 7 % → 9 % | 25.7 px | 0.30 | 1.38 | 45 |
| fast wave | 24 % → 27 % | 28.2 px | 0.29 | 1.12 | 150 |
| slow wave | 23 % → 32 % | 26.4 px | 0.31 | 1.41 | 256 |
| spiral | 39 % → 47 % | 25.6 px | 0.29 | 1.21 | 354 |
| loop | 20 % → 25 % | 25.7 px | 0.30 | 1.25 | 394 |
| tilted | 12 % → 12 % | 34.0 px | 0.30 | 1.00 | 91 |
| over the wet one | 21 % → 25 % | 25.2 px | 0.30 | 1.19 | 42 |
| long, no reload | 53 % → 59 % | 23.6 px | 0.30 | 1.12 | 438 | quarters: 0.23 → 0.21 → 0.19 → 0.16

Numbers say: light vs heavy: width 16.2 → 31.9 px, dark 0.29 → 0.29; wet paint spreads well beyond the stroke.

## Brush Artist · Watercolour — violet
Watercolour 0.93 · Ink 0.07 · 40 px · 33.6 s

![Brush Artist · Watercolour — violet](Brush-Artist-Watercolour-violet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 6 % → 11 % | 16.2 px | 0.36 | 1.88 | 33 |
| heavy line | 11 % → 13 % | 31.9 px | 0.37 | 1.17 | 76 |
| pressure swell | 7 % → 9 % | 25.7 px | 0.38 | 1.38 | 47 |
| fast wave | 24 % → 27 % | 28.2 px | 0.38 | 1.12 | 161 |
| slow wave | 23 % → 32 % | 26.4 px | 0.39 | 1.41 | 270 |
| spiral | 39 % → 47 % | 25.6 px | 0.37 | 1.21 | 551 |
| loop | 20 % → 25 % | 25.7 px | 0.38 | 1.25 | 165 |
| tilted | 12 % → 12 % | 34.0 px | 0.38 | 1.00 | 116 |
| over the wet one | 21 % → 25 % | 25.2 px | 0.38 | 1.19 | 99 |
| long, no reload | 53 % → 59 % | 23.6 px | 0.38 | 1.12 | 475 | quarters: 0.28 → 0.27 → 0.24 → 0.21

Numbers say: light vs heavy: width 16.2 → 31.9 px, dark 0.36 → 0.37; wet paint spreads well beyond the stroke.

## Brush Artist · Watercolour — teal
Watercolour 0.93 · Ink 0.07 · 40 px · 33.9 s

![Brush Artist · Watercolour — teal](Brush-Artist-Watercolour-teal.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 6 % → 11 % | 16.2 px | 0.23 | 1.88 | 36 |
| heavy line | 11 % → 13 % | 31.9 px | 0.23 | 1.17 | 80 |
| pressure swell | 7 % → 9 % | 25.7 px | 0.24 | 1.38 | 38 |
| fast wave | 24 % → 27 % | 28.2 px | 0.23 | 1.12 | 156 |
| slow wave | 23 % → 32 % | 26.4 px | 0.25 | 1.41 | 260 |
| spiral | 39 % → 47 % | 25.6 px | 0.23 | 1.21 | 353 |
| loop | 20 % → 25 % | 25.7 px | 0.24 | 1.25 | 172 |
| tilted | 12 % → 12 % | 34.0 px | 0.24 | 1.00 | 131 |
| over the wet one | 21 % → 25 % | 25.2 px | 0.24 | 1.19 | 129 |
| long, no reload | 53 % → 59 % | 23.6 px | 0.24 | 1.12 | 430 | quarters: 0.18 → 0.16 → 0.15 → 0.13

Numbers say: light vs heavy: width 16.2 → 31.9 px, dark 0.23 → 0.23; wet paint spreads well beyond the stroke.

## Brush Artist · Gouache
Gouache 1.00 · 30 px · 36.5 s

![Brush Artist · Gouache](Brush-Artist-Gouache.png)

A light paint: laid on a grey sheet (on white it cannot be seen); **dark** = how far it is from the grey either way.

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 8 % → 8 % | 24.4 px | 0.27 | 0.97 | 135 |
| heavy line | 15 % → 12 % | 42.8 px | 0.27 | 0.78 | 348 |
| pressure swell | 11 % → 9 % | 41.0 px | 0.27 | 0.85 | 76 |
| fast wave | 30 % → 14 % | 34.9 px | 0.26 | 0.45 | 289 |
| slow wave | 29 % → 14 % | 34.0 px | 0.26 | 0.47 | 479 |
| spiral | 40 % → 14 % | 26.6 px | 0.26 | 0.35 | 333 |
| loop | 24 % → 15 % | 30.6 px | 0.26 | 0.62 | 168 |
| tilted | 10 % → 10 % | 27.4 px | 0.27 | 1.01 | 114 |
| over the wet one | 22 % → 19 % | 32.9 px | 0.27 | 0.89 | 102 |
| long, no reload | 43 % → 15 % | 19.1 px | 0.26 | 0.35 | 540 | quarters: 0.01 → 0.01 → 0.01 → 0.01

Numbers say: light vs heavy: width 24.4 → 42.8 px, dark 0.27 → 0.27; the long stroke does not run out of paint.

## Brush Artist · Oil — bristle
Oil 0.89 · Oil glaze 0.11 · 30 px · 16.8 s

![Brush Artist · Oil — bristle](Brush-Artist-Oil-bristle.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 9 % → 9 % | 26.3 px | 0.53 | 1.00 | 115 |
| heavy line | 10 % → 10 % | 28.6 px | 0.54 | 1.00 | 141 |
| pressure swell | 8 % → 8 % | 28.2 px | 0.55 | 1.00 | 132 |
| fast wave | 24 % → 24 % | 27.3 px | 0.55 | 1.00 | 426 |
| slow wave | 25 % → 25 % | 28.3 px | 0.55 | 1.00 | 797 |
| spiral | 39 % → 39 % | 25.6 px | 0.54 | 1.00 | 691 |
| loop | 20 % → 20 % | 26.3 px | 0.54 | 1.00 | 316 |
| tilted | 11 % → 11 % | 29.9 px | 0.52 | 1.00 | 125 |
| over the wet one | 20 % → 20 % | 25.5 px | 0.52 | 1.00 | 119 |
| long, no reload | 50 % → 50 % | 22.4 px | 0.54 | 1.00 | 968 | quarters: 0.32 → 0.30 → 0.29 → 0.28

Numbers say: light vs heavy: width 26.3 → 28.6 px, dark 0.53 → 0.54; pressure barely changes the width; the long stroke does not run out of paint.

## Brush Artist · Charcoal — stick
Charcoal 0.78 · Pastel 0.22 · 28 px · 11.9 s

![Brush Artist · Charcoal — stick](Brush-Artist-Charcoal-stick.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 5 % → 5 % | 15.3 px | 0.85 | 1.00 | 18 |
| heavy line | 8 % → 8 % | 23.3 px | 0.85 | 1.00 | 43 |
| pressure swell | 5 % → 5 % | 19.8 px | 0.85 | 1.00 | 22 |
| fast wave | 18 % → 18 % | 20.7 px | 0.85 | 1.00 | 88 |
| slow wave | 17 % → 17 % | 19.5 px | 0.85 | 1.00 | 122 |
| spiral | 29 % → 29 % | 19.3 px | 0.85 | 1.00 | 276 |
| loop | 15 % → 15 % | 19.3 px | 0.85 | 1.00 | 63 |
| tilted | 6 % → 6 % | 16.6 px | 0.85 | 1.00 | 52 |
| over the wet one | 13 % → 13 % | 19.8 px | 0.85 | 1.00 | 29 |
| long, no reload | 41 % → 41 % | 18.2 px | 0.85 | 1.00 | 197 | quarters: 0.38 → 0.38 → 0.38 → 0.38

Numbers say: light vs heavy: width 15.3 → 23.3 px, dark 0.85 → 0.85; the long stroke does not run out of paint.

## Brush Artist · Charcoal — stick B
Charcoal 0.78 · Pastel 0.22 · 36 px · 12.5 s

![Brush Artist · Charcoal — stick B](Brush-Artist-Charcoal-stick-B.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 7 % → 7 % | 19.8 px | 0.85 | 1.00 | 31 |
| heavy line | 10 % → 10 % | 30.4 px | 0.85 | 1.00 | 34 |
| pressure swell | 7 % → 7 % | 25.9 px | 0.85 | 1.00 | 37 |
| fast wave | 23 % → 23 % | 26.8 px | 0.85 | 1.00 | 109 |
| slow wave | 22 % → 22 % | 25.5 px | 0.85 | 1.00 | 192 |
| spiral | 38 % → 38 % | 25.4 px | 0.85 | 1.00 | 173 |
| loop | 19 % → 19 % | 25.0 px | 0.85 | 1.00 | 104 |
| tilted | 7 % → 7 % | 20.4 px | 0.85 | 1.00 | 60 |
| over the wet one | 17 % → 17 % | 25.9 px | 0.85 | 1.00 | 66 |
| long, no reload | 51 % → 51 % | 22.6 px | 0.85 | 1.00 | 327 | quarters: 0.47 → 0.47 → 0.47 → 0.47

Numbers say: light vs heavy: width 19.8 → 30.4 px, dark 0.85 → 0.85; the long stroke does not run out of paint.

## Brush Artist · Charcoal — stick C
Charcoal 0.78 · Pastel 0.22 · 22 px · 12.1 s

![Brush Artist · Charcoal — stick C](Brush-Artist-Charcoal-stick-C.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 4 % → 4 % | 12.6 px | 0.85 | 1.00 | 27 |
| heavy line | 7 % → 7 % | 19.0 px | 0.85 | 1.00 | 19 |
| pressure swell | 4 % → 4 % | 16.2 px | 0.85 | 1.00 | 15 |
| fast wave | 15 % → 15 % | 16.9 px | 0.85 | 1.00 | 50 |
| slow wave | 14 % → 14 % | 15.8 px | 0.85 | 1.00 | 88 |
| spiral | 24 % → 24 % | 15.7 px | 0.85 | 1.00 | 91 |
| loop | 12 % → 12 % | 15.9 px | 0.85 | 1.00 | 75 |
| tilted | 5 % → 5 % | 14.4 px | 0.85 | 1.00 | 28 |
| over the wet one | 11 % → 11 % | 16.1 px | 0.85 | 1.00 | 35 |
| long, no reload | 34 % → 34 % | 15.2 px | 0.85 | 1.00 | 144 | quarters: 0.32 → 0.32 → 0.32 → 0.32

Numbers say: light vs heavy: width 12.6 → 19.0 px, dark 0.85 → 0.85; the long stroke does not run out of paint.

## Oil · Henry Ward · Loaded flat
Oil 1.00 · 46 px · 22.3 s

![Oil · Henry Ward · Loaded flat](Oil-Henry-Ward-Loaded-flat.png)

A light paint: laid on a grey sheet (on white it cannot be seen); **dark** = how far it is from the grey either way.

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 12 % → 12 % | 33.8 px | 0.31 | 1.00 | 154 |
| heavy line | 12 % → 12 % | 36.1 px | 0.32 | 1.00 | 187 |
| pressure swell | 10 % → 10 % | 38.1 px | 0.30 | 1.00 | 156 |
| fast wave | 28 % → 28 % | 32.1 px | 0.25 | 1.01 | 558 |
| slow wave | 34 % → 34 % | 39.4 px | 0.25 | 1.00 | 974 |
| spiral | 44 % → 44 % | 29.1 px | 0.23 | 1.00 | 902 |
| loop | 25 % → 25 % | 32.2 px | 0.29 | 1.00 | 549 |
| tilted | 13 % → 13 % | 35.2 px | 0.31 | 1.00 | 305 |
| over the wet one | 24 % → 24 % | 31.7 px | 0.31 | 1.00 | 346 |
| long, no reload | 50 % → 50 % | 22.2 px | 0.21 | 1.00 | 1036 | quarters: 0.00 → 0.00 → 0.00 → 0.00

Numbers say: light vs heavy: width 33.8 → 36.1 px, dark 0.31 → 0.32; pressure barely changes the width; the long stroke does not run out of paint.

## Oil · Henry Ward · Dry scrub
Oil 1.00 · 50 px · 22.6 s

![Oil · Henry Ward · Dry scrub](Oil-Henry-Ward-Dry-scrub.png)

A light paint: laid on a grey sheet (on white it cannot be seen); **dark** = how far it is from the grey either way.

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 9 % → 9 % | 25.9 px | 0.24 | 1.00 | 157 |
| heavy line | 12 % → 12 % | 36.3 px | 0.23 | 1.00 | 217 |
| pressure swell | 10 % → 10 % | 37.0 px | 0.22 | 1.00 | 167 |
| fast wave | 24 % → 24 % | 27.4 px | 0.11 | 1.01 | 561 |
| slow wave | 32 % → 32 % | 37.1 px | 0.16 | 1.00 | 944 |
| spiral | 37 % → 37 % | 24.2 px | 0.14 | 1.00 | 955 |
| loop | 25 % → 25 % | 32.0 px | 0.16 | 1.00 | 624 |
| tilted | 12 % → 12 % | 33.6 px | 0.23 | 1.00 | 268 |
| over the wet one | 23 % → 23 % | 31.8 px | 0.23 | 1.00 | 188 |
| long, no reload | 31 % → 31 % | 13.7 px | 0.16 | 1.00 | 1004 | quarters: 0.00 → 0.00 → 0.00 → 0.00

Numbers say: light vs heavy: width 25.9 → 36.3 px, dark 0.24 → 0.23; the long stroke does not run out of paint.

## Oil · Henry Ward · Dirty contour
Oil 1.00 · 24 px · 20.6 s

![Oil · Henry Ward · Dirty contour](Oil-Henry-Ward-Dirty-contour.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 8 % → 8 % | 24.0 px | 0.74 | 1.00 | 126 |
| heavy line | 9 % → 9 % | 26.3 px | 0.75 | 1.00 | 154 |
| pressure swell | 7 % → 7 % | 26.0 px | 0.77 | 1.00 | 98 |
| fast wave | 18 % → 18 % | 21.3 px | 0.75 | 1.00 | 290 |
| slow wave | 22 % → 22 % | 25.4 px | 0.76 | 1.00 | 511 |
| spiral | 34 % → 34 % | 22.4 px | 0.71 | 1.00 | 485 |
| loop | 18 % → 18 % | 23.5 px | 0.75 | 1.00 | 296 |
| tilted | 9 % → 9 % | 25.6 px | 0.76 | 1.00 | 143 |
| over the wet one | 18 % → 18 % | 23.7 px | 0.76 | 1.00 | 124 |
| long, no reload | 38 % → 38 % | 16.9 px | 0.72 | 1.00 | 580 | quarters: 0.42 → 0.33 → 0.26 → 0.21

Numbers say: light vs heavy: width 24.0 → 26.3 px, dark 0.74 → 0.75; pressure barely changes the width.

## Oil · Henry Ward · Wet drag
Oil 1.00 · 44 px · 17.7 s

![Oil · Henry Ward · Wet drag](Oil-Henry-Ward-Wet-drag.png)

A light paint: laid on a grey sheet (on white it cannot be seen); **dark** = how far it is from the grey either way.

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 13 % → 13 % | 38.7 px | 0.26 | 1.00 | 166 |
| heavy line | 15 % → 15 % | 42.3 px | 0.27 | 1.00 | 177 |
| pressure swell | 11 % → 11 % | 41.9 px | 0.26 | 1.00 | 113 |
| fast wave | 33 % → 33 % | 37.6 px | 0.21 | 1.00 | 634 |
| slow wave | 36 % → 36 % | 41.4 px | 0.22 | 1.00 | 977 |
| spiral | 50 % → 50 % | 32.8 px | 0.19 | 1.00 | 623 |
| loop | 30 % → 30 % | 38.8 px | 0.23 | 1.00 | 361 |
| tilted | 14 % → 14 % | 37.9 px | 0.28 | 1.00 | 176 |
| over the wet one | 27 % → 27 % | 36.5 px | 0.28 | 1.00 | 153 |
| long, no reload | 58 % → 58 % | 25.9 px | 0.18 | 1.00 | 940 | quarters: 0.00 → 0.00 → 0.00 → 0.00

Numbers say: light vs heavy: width 38.7 → 42.3 px, dark 0.26 → 0.27; pressure barely changes the width; the long stroke does not run out of paint.

## Oil · Henry Ward · Thin veil
Oil 0.81 · Ink 0.19 · 56 px · 36.7 s

![Oil · Henry Ward · Thin veil](Oil-Henry-Ward-Thin-veil.png)

A light paint: laid on a grey sheet (on white it cannot be seen); **dark** = how far it is from the grey either way.

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 16 % → 16 % | 46.5 px | 0.21 | 0.98 | 163 |
| heavy line | 17 % → 17 % | 50.6 px | 0.23 | 0.98 | 209 |
| pressure swell | 14 % → 13 % | 51.4 px | 0.24 | 0.97 | 142 |
| fast wave | 34 % → 23 % | 39.0 px | 0.17 | 0.68 | 467 |
| slow wave | 46 % → 39 % | 52.6 px | 0.17 | 0.87 | 871 |
| spiral | 53 % → 37 % | 34.9 px | 0.18 | 0.70 | 1391 |
| loop | 36 % → 32 % | 46.1 px | 0.18 | 0.89 | 482 |
| tilted | 16 % → 16 % | 43.5 px | 0.24 | 1.02 | 235 |
| over the wet one | 31 % → 30 % | 43.9 px | 0.24 | 0.97 | 179 |
| long, no reload | 55 % → 43 % | 24.7 px | 0.16 | 0.78 | 1108 | quarters: 0.00 → 0.01 → 0.01 → 0.00

Numbers say: light vs heavy: width 46.5 → 50.6 px, dark 0.21 → 0.23; pressure barely changes the width; the long stroke does not run out of paint.

## Oil · Henry Ward · Ground
Oil 0.81 · Gouache 0.19 · 140 px · 66.4 s

![Oil · Henry Ward · Ground](Oil-Henry-Ward-Ground.png)

A light paint: laid on a grey sheet (on white it cannot be seen); **dark** = how far it is from the grey either way.

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 45 % → 44 % | 131.5 px | 0.37 | 0.97 | 627 |
| heavy line | 47 % → 44 % | 135.3 px | 0.38 | 0.95 | 662 |
| pressure swell | 37 % → 42 % | 139.9 px | 0.38 | 1.12 | 433 |
| fast wave | 75 % → 82 % | 86.9 px | 0.37 | 1.08 | 2705 |
| slow wave | 88 % → 84 % | 101.9 px | 0.35 | 0.95 | 2789 |
| spiral | 91 % → 74 % | 60.0 px | 0.34 | 0.82 | 3222 |
| loop | 77 % → 75 % | 100.2 px | 0.37 | 0.97 | 1559 |
| tilted | 35 % → 35 % | 97.1 px | 0.38 | 1.00 | 827 |
| over the wet one | 70 % → 67 % | 98.9 px | 0.38 | 0.96 | 704 |
| long, no reload | 99 % → 96 % | 44.5 px | 0.34 | 0.97 | 5051 | quarters: 0.00 → 0.00 → 0.00 → 0.00

Numbers say: light vs heavy: width 131.5 → 135.3 px, dark 0.37 → 0.38; pressure barely changes the width.

## Oil · Henry Ward · HW #02 cream over wet olive
Oil 0.81 · Ink 0.19 · 56 px · 36.2 s

![Oil · Henry Ward · HW #02 cream over wet olive](Oil-Henry-Ward-HW-02-cream-over-wet-olive.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 16 % → 16 % | 46.5 px | 0.66 | 0.98 | 414 |
| heavy line | 17 % → 17 % | 50.6 px | 0.66 | 0.98 | 409 |
| pressure swell | 14 % → 13 % | 51.4 px | 0.66 | 0.97 | 141 |
| fast wave | 34 % → 23 % | 39.0 px | 0.64 | 0.68 | 438 |
| slow wave | 46 % → 39 % | 52.6 px | 0.64 | 0.87 | 799 |
| spiral | 53 % → 37 % | 34.9 px | 0.64 | 0.70 | 789 |
| loop | 36 % → 32 % | 46.1 px | 0.65 | 0.89 | 834 |
| tilted | 16 % → 16 % | 43.5 px | 0.66 | 1.02 | 226 |
| over the wet one | 31 % → 30 % | 43.9 px | 0.66 | 0.97 | 183 |
| long, no reload | 55 % → 43 % | 24.7 px | 0.64 | 0.78 | 1096 | quarters: 0.55 → 0.38 → 0.23 → 0.16

Numbers say: light vs heavy: width 46.5 → 50.6 px, dark 0.66 → 0.66; pressure barely changes the width.

## Oil · Henry Ward · HW #04 grey arcs over ochre
Oil 1.00 · 46 px · 20.4 s

![Oil · Henry Ward · HW #04 grey arcs over ochre](Oil-Henry-Ward-HW-04-grey-arcs-over-ochre.png)

A light paint: laid on a grey sheet (on white it cannot be seen); **dark** = how far it is from the grey either way.

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 12 % → 12 % | 33.8 px | 0.25 | 1.00 | 238 |
| heavy line | 12 % → 12 % | 36.1 px | 0.26 | 1.00 | 161 |
| pressure swell | 10 % → 10 % | 38.1 px | 0.23 | 1.00 | 132 |
| fast wave | 28 % → 28 % | 32.1 px | 0.20 | 1.01 | 404 |
| slow wave | 34 % → 34 % | 39.4 px | 0.21 | 1.00 | 692 |
| spiral | 44 % → 44 % | 29.1 px | 0.20 | 1.00 | 674 |
| loop | 25 % → 25 % | 32.2 px | 0.24 | 1.00 | 351 |
| tilted | 13 % → 13 % | 35.2 px | 0.25 | 1.00 | 193 |
| over the wet one | 24 % → 24 % | 31.7 px | 0.25 | 1.00 | 158 |
| long, no reload | 50 % → 50 % | 22.2 px | 0.18 | 1.00 | 1646 | quarters: 0.00 → 0.00 → 0.00 → 0.00

Numbers say: light vs heavy: width 33.8 → 36.1 px, dark 0.25 → 0.26; pressure barely changes the width; the long stroke does not run out of paint.

## Oil · Henry Ward · HW #09 white arches over wet blue-grey
Oil 1.00 · 46 px · 19.8 s

![Oil · Henry Ward · HW #09 white arches over wet blue-grey](Oil-Henry-Ward-HW-09-white-arches-over-wet-blue-grey.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 12 % → 12 % | 33.8 px | 0.38 | 1.00 | 242 |
| heavy line | 12 % → 12 % | 36.1 px | 0.38 | 1.00 | 160 |
| pressure swell | 10 % → 10 % | 38.1 px | 0.38 | 1.00 | 121 |
| fast wave | 28 % → 28 % | 32.1 px | 0.35 | 1.01 | 427 |
| slow wave | 34 % → 34 % | 39.4 px | 0.34 | 1.00 | 677 |
| spiral | 44 % → 44 % | 29.1 px | 0.33 | 1.00 | 643 |
| loop | 25 % → 25 % | 32.2 px | 0.37 | 1.00 | 421 |
| tilted | 13 % → 13 % | 35.2 px | 0.38 | 1.00 | 196 |
| over the wet one | 24 % → 24 % | 31.7 px | 0.38 | 1.00 | 170 |
| long, no reload | 50 % → 50 % | 22.2 px | 0.32 | 1.00 | 1647 | quarters: 0.27 → 0.19 → 0.14 → 0.11

Numbers say: light vs heavy: width 33.8 → 36.1 px, dark 0.38 → 0.38; pressure barely changes the width.

## Oil · Henry Ward · HW #03 navy contours over wet band
Oil 1.00 · 46 px · 21.5 s

![Oil · Henry Ward · HW #03 navy contours over wet band](Oil-Henry-Ward-HW-03-navy-contours-over-wet-band.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 12 % → 12 % | 33.8 px | 0.40 | 1.00 | 208 |
| heavy line | 12 % → 12 % | 36.1 px | 0.40 | 1.00 | 341 |
| pressure swell | 10 % → 10 % | 38.1 px | 0.40 | 1.00 | 110 |
| fast wave | 28 % → 28 % | 32.1 px | 0.37 | 1.01 | 383 |
| slow wave | 34 % → 34 % | 39.4 px | 0.37 | 1.00 | 700 |
| spiral | 44 % → 44 % | 29.1 px | 0.35 | 1.00 | 669 |
| loop | 25 % → 25 % | 32.2 px | 0.39 | 1.00 | 343 |
| tilted | 13 % → 13 % | 35.2 px | 0.40 | 1.00 | 195 |
| over the wet one | 24 % → 24 % | 31.7 px | 0.40 | 1.00 | 179 |
| long, no reload | 50 % → 50 % | 22.2 px | 0.35 | 1.00 | 947 | quarters: 0.28 → 0.20 → 0.15 → 0.11

Numbers say: light vs heavy: width 33.8 → 36.1 px, dark 0.40 → 0.40; pressure barely changes the width.

## Oil · Henry Ward · Ground #2b2f1c
Oil 0.81 · Gouache 0.19 · 140 px · 65.1 s

![Oil · Henry Ward · Ground #2b2f1c](Oil-Henry-Ward-Ground-2b2f1c.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 45 % → 44 % | 131.5 px | 0.63 | 0.97 | 888 |
| heavy line | 47 % → 44 % | 135.3 px | 0.63 | 0.95 | 643 |
| pressure swell | 37 % → 42 % | 139.9 px | 0.63 | 1.12 | 499 |
| fast wave | 75 % → 82 % | 86.9 px | 0.63 | 1.08 | 1845 |
| slow wave | 88 % → 84 % | 101.9 px | 0.63 | 0.95 | 2911 |
| spiral | 91 % → 74 % | 60.0 px | 0.63 | 0.82 | 3584 |
| loop | 77 % → 75 % | 100.2 px | 0.63 | 0.97 | 2380 |
| tilted | 35 % → 35 % | 97.1 px | 0.63 | 1.00 | 931 |
| over the wet one | 70 % → 67 % | 98.9 px | 0.63 | 0.96 | 741 |
| long, no reload | 99 % → 96 % | 44.5 px | 0.63 | 0.97 | 4068 | quarters: 0.63 → 0.64 → 0.63 → 0.63

Numbers say: light vs heavy: width 131.5 → 135.3 px, dark 0.63 → 0.63; pressure barely changes the width; the long stroke does not run out of paint.

## Oil · Henry Ward · Thin veil #2b3a44
Oil 0.81 · Ink 0.19 · 56 px · 35.1 s

![Oil · Henry Ward · Thin veil #2b3a44](Oil-Henry-Ward-Thin-veil-2b3a44.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 16 % → 16 % | 46.5 px | 0.66 | 0.98 | 346 |
| heavy line | 17 % → 17 % | 50.6 px | 0.66 | 0.98 | 195 |
| pressure swell | 14 % → 13 % | 51.4 px | 0.66 | 0.97 | 130 |
| fast wave | 34 % → 23 % | 39.0 px | 0.64 | 0.68 | 451 |
| slow wave | 46 % → 39 % | 52.6 px | 0.64 | 0.87 | 847 |
| spiral | 53 % → 37 % | 34.9 px | 0.64 | 0.70 | 825 |
| loop | 36 % → 32 % | 46.1 px | 0.65 | 0.89 | 437 |
| tilted | 16 % → 16 % | 43.5 px | 0.66 | 1.02 | 241 |
| over the wet one | 31 % → 30 % | 43.9 px | 0.66 | 0.97 | 209 |
| long, no reload | 55 % → 43 % | 24.7 px | 0.64 | 0.78 | 1306 | quarters: 0.55 → 0.38 → 0.23 → 0.16

Numbers say: light vs heavy: width 46.5 → 50.6 px, dark 0.66 → 0.66; pressure barely changes the width.

## Oil · Henry Ward · Loaded flat #ece6c0
Oil 1.00 · 46 px · 21.6 s

![Oil · Henry Ward · Loaded flat #ece6c0](Oil-Henry-Ward-Loaded-flat-ece6c0.png)

A light paint: laid on a grey sheet (on white it cannot be seen); **dark** = how far it is from the grey either way.

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 12 % → 12 % | 33.8 px | 0.32 | 1.00 | 152 |
| heavy line | 12 % → 12 % | 36.1 px | 0.33 | 1.00 | 160 |
| pressure swell | 10 % → 10 % | 38.1 px | 0.31 | 1.00 | 118 |
| fast wave | 28 % → 28 % | 32.1 px | 0.25 | 1.01 | 385 |
| slow wave | 34 % → 34 % | 39.4 px | 0.26 | 1.00 | 710 |
| spiral | 44 % → 44 % | 29.1 px | 0.24 | 1.00 | 647 |
| loop | 25 % → 25 % | 32.2 px | 0.29 | 1.00 | 371 |
| tilted | 13 % → 13 % | 35.2 px | 0.32 | 1.00 | 206 |
| over the wet one | 24 % → 24 % | 31.7 px | 0.32 | 1.00 | 117 |
| long, no reload | 50 % → 50 % | 22.2 px | 0.22 | 1.00 | 1107 | quarters: 0.00 → 0.00 → 0.00 → 0.00

Numbers say: light vs heavy: width 33.8 → 36.1 px, dark 0.32 → 0.33; pressure barely changes the width; the long stroke does not run out of paint.

## Oil · Henry Ward · Dry scrub #ece6c0
Oil 1.00 · 50 px · 21.0 s

![Oil · Henry Ward · Dry scrub #ece6c0](Oil-Henry-Ward-Dry-scrub-ece6c0.png)

A light paint: laid on a grey sheet (on white it cannot be seen); **dark** = how far it is from the grey either way.

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 9 % → 9 % | 25.9 px | 0.25 | 1.00 | 145 |
| heavy line | 12 % → 12 % | 36.3 px | 0.24 | 1.00 | 160 |
| pressure swell | 10 % → 10 % | 37.0 px | 0.23 | 1.00 | 123 |
| fast wave | 24 % → 24 % | 27.4 px | 0.11 | 1.01 | 397 |
| slow wave | 32 % → 32 % | 37.1 px | 0.17 | 1.00 | 722 |
| spiral | 37 % → 37 % | 24.2 px | 0.14 | 1.00 | 656 |
| loop | 25 % → 25 % | 32.0 px | 0.17 | 1.00 | 390 |
| tilted | 12 % → 12 % | 33.6 px | 0.24 | 1.00 | 204 |
| over the wet one | 23 % → 23 % | 31.8 px | 0.24 | 1.00 | 165 |
| long, no reload | 31 % → 31 % | 13.7 px | 0.16 | 1.00 | 1010 | quarters: 0.00 → 0.00 → 0.00 → 0.00

Numbers say: light vs heavy: width 25.9 → 36.3 px, dark 0.25 → 0.24; the long stroke does not run out of paint.

## Oil · Henry Ward · Ground #8a6a20
Oil 0.81 · Gouache 0.19 · 140 px · 64.5 s

![Oil · Henry Ward · Ground #8a6a20](Oil-Henry-Ward-Ground-8a6a20.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 45 % → 44 % | 131.5 px | 0.42 | 0.97 | 662 |
| heavy line | 47 % → 44 % | 135.3 px | 0.42 | 0.95 | 884 |
| pressure swell | 37 % → 42 % | 139.9 px | 0.42 | 1.12 | 770 |
| fast wave | 75 % → 82 % | 86.9 px | 0.42 | 1.08 | 2304 |
| slow wave | 88 % → 84 % | 101.9 px | 0.42 | 0.95 | 3024 |
| spiral | 91 % → 74 % | 60.0 px | 0.42 | 0.82 | 2802 |
| loop | 77 % → 75 % | 100.2 px | 0.42 | 0.97 | 1534 |
| tilted | 35 % → 35 % | 97.1 px | 0.42 | 1.00 | 771 |
| over the wet one | 70 % → 67 % | 98.9 px | 0.42 | 0.96 | 642 |
| long, no reload | 99 % → 96 % | 44.5 px | 0.42 | 0.97 | 3974 | quarters: 0.42 → 0.42 → 0.42 → 0.40

Numbers say: light vs heavy: width 131.5 → 135.3 px, dark 0.42 → 0.42; pressure barely changes the width; the long stroke does not run out of paint.

## Oil · Henry Ward · Loaded flat #b8bcc0
Oil 1.00 · 46 px · 20.7 s

![Oil · Henry Ward · Loaded flat #b8bcc0](Oil-Henry-Ward-Loaded-flat-b8bcc0.png)

A light paint: laid on a grey sheet (on white it cannot be seen); **dark** = how far it is from the grey either way.

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 12 % → 12 % | 33.8 px | 0.25 | 1.00 | 181 |
| heavy line | 12 % → 12 % | 36.1 px | 0.26 | 1.00 | 156 |
| pressure swell | 10 % → 10 % | 38.1 px | 0.23 | 1.00 | 219 |
| fast wave | 28 % → 28 % | 32.1 px | 0.20 | 1.01 | 517 |
| slow wave | 34 % → 34 % | 39.4 px | 0.21 | 1.00 | 1068 |
| spiral | 44 % → 44 % | 29.1 px | 0.20 | 1.00 | 1129 |
| loop | 25 % → 25 % | 32.2 px | 0.24 | 1.00 | 458 |
| tilted | 13 % → 13 % | 35.2 px | 0.25 | 1.00 | 259 |
| over the wet one | 24 % → 24 % | 31.7 px | 0.25 | 1.00 | 180 |
| long, no reload | 50 % → 50 % | 22.2 px | 0.18 | 1.00 | 1060 | quarters: 0.00 → 0.00 → 0.00 → 0.00

Numbers say: light vs heavy: width 33.8 → 36.1 px, dark 0.25 → 0.26; pressure barely changes the width; the long stroke does not run out of paint.

## Oil · Henry Ward · Dry scrub #c8ccd0
Oil 1.00 · 50 px · 18.7 s

![Oil · Henry Ward · Dry scrub #c8ccd0](Oil-Henry-Ward-Dry-scrub-c8ccd0.png)

A light paint: laid on a grey sheet (on white it cannot be seen); **dark** = how far it is from the grey either way.

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 9 % → 9 % | 25.9 px | 0.23 | 1.00 | 182 |
| heavy line | 12 % → 12 % | 36.3 px | 0.22 | 1.00 | 190 |
| pressure swell | 10 % → 10 % | 37.0 px | 0.21 | 1.00 | 141 |
| fast wave | 24 % → 24 % | 27.4 px | 0.11 | 1.01 | 408 |
| slow wave | 32 % → 32 % | 37.1 px | 0.15 | 1.00 | 769 |
| spiral | 37 % → 37 % | 24.2 px | 0.13 | 1.00 | 793 |
| loop | 25 % → 25 % | 32.0 px | 0.15 | 1.00 | 344 |
| tilted | 12 % → 12 % | 33.6 px | 0.21 | 1.00 | 200 |
| over the wet one | 23 % → 23 % | 31.8 px | 0.21 | 1.00 | 155 |
| long, no reload | 31 % → 31 % | 13.7 px | 0.15 | 1.00 | 948 | quarters: 0.00 → 0.00 → 0.00 → 0.00

Numbers say: light vs heavy: width 25.9 → 36.3 px, dark 0.23 → 0.22; the long stroke does not run out of paint.

## Oil · Henry Ward · Wet drag #9ea4aa
Oil 1.00 · 44 px · 15.8 s

![Oil · Henry Ward · Wet drag #9ea4aa](Oil-Henry-Ward-Wet-drag-9ea4aa.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 13 % → 13 % | 38.7 px | 0.21 | 1.00 | 155 |
| heavy line | 15 % → 15 % | 42.3 px | 0.22 | 1.00 | 166 |
| pressure swell | 11 % → 11 % | 41.9 px | 0.22 | 1.00 | 124 |
| fast wave | 33 % → 33 % | 37.6 px | 0.19 | 1.00 | 420 |
| slow wave | 36 % → 36 % | 41.4 px | 0.20 | 1.00 | 735 |
| spiral | 50 % → 50 % | 32.8 px | 0.17 | 1.00 | 673 |
| loop | 30 % → 30 % | 38.8 px | 0.20 | 1.00 | 333 |
| tilted | 14 % → 14 % | 37.9 px | 0.22 | 1.00 | 183 |
| over the wet one | 27 % → 27 % | 36.5 px | 0.22 | 1.00 | 156 |
| long, no reload | 58 % → 58 % | 25.9 px | 0.17 | 1.00 | 967 | quarters: 0.17 → 0.12 → 0.09 → 0.06

Numbers say: light vs heavy: width 38.7 → 42.3 px, dark 0.21 → 0.22; pressure barely changes the width.

## Oil · Henry Ward · Ground #e8b4a8
Oil 0.81 · Gouache 0.19 · 140 px · 62.1 s

![Oil · Henry Ward · Ground #e8b4a8](Oil-Henry-Ward-Ground-e8b4a8.png)

A light paint: laid on a grey sheet (on white it cannot be seen); **dark** = how far it is from the grey either way.

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 45 % → 44 % | 131.5 px | 0.30 | 0.97 | 671 |
| heavy line | 47 % → 44 % | 135.3 px | 0.30 | 0.95 | 731 |
| pressure swell | 37 % → 42 % | 139.9 px | 0.30 | 1.12 | 508 |
| fast wave | 75 % → 82 % | 86.9 px | 0.30 | 1.08 | 1665 |
| slow wave | 88 % → 84 % | 101.9 px | 0.29 | 0.95 | 2900 |
| spiral | 91 % → 74 % | 60.0 px | 0.28 | 0.82 | 2919 |
| loop | 77 % → 75 % | 100.2 px | 0.30 | 0.97 | 1466 |
| tilted | 35 % → 35 % | 97.1 px | 0.30 | 1.00 | 831 |
| over the wet one | 70 % → 67 % | 98.9 px | 0.30 | 0.96 | 644 |
| long, no reload | 99 % → 96 % | 44.5 px | 0.28 | 0.97 | 4153 | quarters: 0.00 → 0.00 → 0.00 → 0.00

Numbers say: light vs heavy: width 131.5 → 135.3 px, dark 0.30 → 0.30; pressure barely changes the width.

## Oil · Henry Ward · Loaded flat #6e7f90
Oil 1.00 · 46 px · 18.4 s

![Oil · Henry Ward · Loaded flat #6e7f90](Oil-Henry-Ward-Loaded-flat-6e7f90.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 12 % → 12 % | 33.8 px | 0.38 | 1.00 | 162 |
| heavy line | 12 % → 12 % | 36.1 px | 0.38 | 1.00 | 190 |
| pressure swell | 10 % → 10 % | 38.1 px | 0.38 | 1.00 | 131 |
| fast wave | 28 % → 28 % | 32.1 px | 0.35 | 1.01 | 405 |
| slow wave | 34 % → 34 % | 39.4 px | 0.34 | 1.00 | 675 |
| spiral | 44 % → 44 % | 29.1 px | 0.33 | 1.00 | 654 |
| loop | 25 % → 25 % | 32.2 px | 0.37 | 1.00 | 379 |
| tilted | 13 % → 13 % | 35.2 px | 0.38 | 1.00 | 185 |
| over the wet one | 24 % → 24 % | 31.7 px | 0.38 | 1.00 | 182 |
| long, no reload | 50 % → 50 % | 22.2 px | 0.32 | 1.00 | 1013 | quarters: 0.27 → 0.19 → 0.14 → 0.11

Numbers say: light vs heavy: width 33.8 → 36.1 px, dark 0.38 → 0.38; pressure barely changes the width.

## Oil · Henry Ward · Loaded flat #f6f6f2
Oil 1.00 · 46 px · 18.1 s

![Oil · Henry Ward · Loaded flat #f6f6f2](Oil-Henry-Ward-Loaded-flat-f6f6f2.png)

A light paint: laid on a grey sheet (on white it cannot be seen); **dark** = how far it is from the grey either way.

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 12 % → 12 % | 33.8 px | 0.33 | 1.00 | 142 |
| heavy line | 12 % → 12 % | 36.1 px | 0.34 | 1.00 | 142 |
| pressure swell | 10 % → 10 % | 38.1 px | 0.32 | 1.00 | 127 |
| fast wave | 28 % → 28 % | 32.1 px | 0.26 | 1.01 | 389 |
| slow wave | 34 % → 34 % | 39.4 px | 0.26 | 1.00 | 739 |
| spiral | 44 % → 44 % | 29.1 px | 0.25 | 1.00 | 731 |
| loop | 25 % → 25 % | 32.2 px | 0.30 | 1.00 | 345 |
| tilted | 13 % → 13 % | 35.2 px | 0.33 | 1.00 | 181 |
| over the wet one | 24 % → 24 % | 31.7 px | 0.33 | 1.00 | 162 |
| long, no reload | 50 % → 50 % | 22.2 px | 0.22 | 1.00 | 926 | quarters: 0.00 → 0.00 → 0.00 → 0.00

Numbers say: light vs heavy: width 33.8 → 36.1 px, dark 0.33 → 0.34; pressure barely changes the width; the long stroke does not run out of paint.

## Oil · Henry Ward · Dry scrub #f6f6f2
Oil 1.00 · 50 px · 17.6 s

![Oil · Henry Ward · Dry scrub #f6f6f2](Oil-Henry-Ward-Dry-scrub-f6f6f2.png)

A light paint: laid on a grey sheet (on white it cannot be seen); **dark** = how far it is from the grey either way.

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 9 % → 9 % | 25.9 px | 0.26 | 1.00 | 127 |
| heavy line | 12 % → 12 % | 36.3 px | 0.25 | 1.00 | 160 |
| pressure swell | 10 % → 10 % | 37.0 px | 0.24 | 1.00 | 125 |
| fast wave | 24 % → 24 % | 27.4 px | 0.12 | 1.01 | 333 |
| slow wave | 32 % → 32 % | 37.1 px | 0.17 | 1.00 | 655 |
| spiral | 37 % → 37 % | 24.2 px | 0.14 | 1.00 | 689 |
| loop | 25 % → 25 % | 32.0 px | 0.17 | 1.00 | 341 |
| tilted | 12 % → 12 % | 33.6 px | 0.24 | 1.00 | 204 |
| over the wet one | 23 % → 23 % | 31.8 px | 0.24 | 1.00 | 172 |
| long, no reload | 31 % → 31 % | 13.7 px | 0.17 | 1.00 | 890 | quarters: 0.00 → 0.00 → 0.00 → 0.00

Numbers say: light vs heavy: width 25.9 → 36.3 px, dark 0.26 → 0.25; the long stroke does not run out of paint.

## Oil · Henry Ward · Ground #e8e2da
Oil 0.81 · Gouache 0.19 · 140 px · 60.8 s

![Oil · Henry Ward · Ground #e8e2da](Oil-Henry-Ward-Ground-e8e2da.png)

A light paint: laid on a grey sheet (on white it cannot be seen); **dark** = how far it is from the grey either way.

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 45 % → 44 % | 131.5 px | 0.38 | 0.97 | 572 |
| heavy line | 47 % → 44 % | 135.3 px | 0.39 | 0.95 | 649 |
| pressure swell | 37 % → 42 % | 139.9 px | 0.39 | 1.12 | 468 |
| fast wave | 75 % → 82 % | 86.9 px | 0.38 | 1.08 | 1590 |
| slow wave | 88 % → 84 % | 101.9 px | 0.36 | 0.95 | 2594 |
| spiral | 91 % → 74 % | 60.0 px | 0.35 | 0.82 | 2722 |
| loop | 77 % → 75 % | 100.2 px | 0.38 | 0.97 | 1343 |
| tilted | 35 % → 35 % | 97.1 px | 0.39 | 1.00 | 732 |
| over the wet one | 70 % → 67 % | 98.9 px | 0.39 | 0.96 | 629 |
| long, no reload | 99 % → 96 % | 44.5 px | 0.35 | 0.97 | 4115 | quarters: 0.00 → 0.00 → 0.00 → 0.00

Numbers say: light vs heavy: width 131.5 → 135.3 px, dark 0.38 → 0.39; pressure barely changes the width.

## Oil · Henry Ward · Loaded flat #6a7a80
Oil 1.00 · 46 px · 18.2 s

![Oil · Henry Ward · Loaded flat #6a7a80](Oil-Henry-Ward-Loaded-flat-6a7a80.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 12 % → 12 % | 33.8 px | 0.40 | 1.00 | 146 |
| heavy line | 12 % → 12 % | 36.1 px | 0.40 | 1.00 | 162 |
| pressure swell | 10 % → 10 % | 38.1 px | 0.40 | 1.00 | 119 |
| fast wave | 28 % → 28 % | 32.1 px | 0.37 | 1.01 | 385 |
| slow wave | 34 % → 34 % | 39.4 px | 0.37 | 1.00 | 675 |
| spiral | 44 % → 44 % | 29.1 px | 0.35 | 1.00 | 630 |
| loop | 25 % → 25 % | 32.2 px | 0.39 | 1.00 | 347 |
| tilted | 13 % → 13 % | 35.2 px | 0.40 | 1.00 | 190 |
| over the wet one | 24 % → 24 % | 31.7 px | 0.40 | 1.00 | 157 |
| long, no reload | 50 % → 50 % | 22.2 px | 0.35 | 1.00 | 930 | quarters: 0.28 → 0.20 → 0.15 → 0.11

Numbers say: light vs heavy: width 33.8 → 36.1 px, dark 0.40 → 0.40; pressure barely changes the width.

## Oil · Henry Ward · Loaded flat #5a1810
Oil 1.00 · 46 px · 18.0 s

![Oil · Henry Ward · Loaded flat #5a1810](Oil-Henry-Ward-Loaded-flat-5a1810.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 12 % → 12 % | 33.8 px | 0.75 | 1.00 | 142 |
| heavy line | 12 % → 12 % | 36.1 px | 0.75 | 1.00 | 154 |
| pressure swell | 10 % → 10 % | 38.1 px | 0.76 | 1.00 | 118 |
| fast wave | 28 % → 28 % | 32.1 px | 0.75 | 1.01 | 387 |
| slow wave | 34 % → 34 % | 39.4 px | 0.75 | 1.00 | 653 |
| spiral | 44 % → 44 % | 29.1 px | 0.75 | 1.00 | 645 |
| loop | 25 % → 25 % | 32.2 px | 0.76 | 1.00 | 324 |
| tilted | 13 % → 13 % | 35.2 px | 0.75 | 1.00 | 182 |
| over the wet one | 24 % → 24 % | 31.7 px | 0.75 | 1.00 | 157 |
| long, no reload | 50 % → 50 % | 22.2 px | 0.74 | 1.00 | 1021 | quarters: 0.53 → 0.43 → 0.36 → 0.30

Numbers say: light vs heavy: width 33.8 → 36.1 px, dark 0.75 → 0.75; pressure barely changes the width.

## Oil · Henry Ward · Dirty contour #1c2240
Oil 1.00 · 24 px · 16.5 s

![Oil · Henry Ward · Dirty contour #1c2240](Oil-Henry-Ward-Dirty-contour-1c2240.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 8 % → 8 % | 24.0 px | 0.74 | 1.00 | 83 |
| heavy line | 9 % → 9 % | 26.3 px | 0.75 | 1.00 | 82 |
| pressure swell | 7 % → 7 % | 26.0 px | 0.77 | 1.00 | 68 |
| fast wave | 18 % → 18 % | 21.3 px | 0.75 | 1.00 | 222 |
| slow wave | 22 % → 22 % | 25.4 px | 0.76 | 1.00 | 369 |
| spiral | 34 % → 34 % | 22.4 px | 0.71 | 1.00 | 390 |
| loop | 18 % → 18 % | 23.5 px | 0.75 | 1.00 | 187 |
| tilted | 9 % → 9 % | 25.6 px | 0.76 | 1.00 | 113 |
| over the wet one | 18 % → 18 % | 23.7 px | 0.76 | 1.00 | 97 |
| long, no reload | 38 % → 38 % | 16.9 px | 0.72 | 1.00 | 502 | quarters: 0.42 → 0.33 → 0.26 → 0.21

Numbers say: light vs heavy: width 24.0 → 26.3 px, dark 0.74 → 0.75; pressure barely changes the width.

## Brush Artist · Refs · #01 Henry Ward peach cloud — own sheet
own sheet 600 × 600 · Gouache 1.00 · 44 px · 12.8 s

![Brush Artist · Refs · #01 Henry Ward peach cloud — own sheet](Brush-Artist-Refs-01-Henry-Ward-peach-cloud-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 13 % → 32 % | 36.6 px | 0.57 | 2.51 | 123 |
| stroke 2 | 21 % → 49 % | 70.5 px | 0.57 | 2.28 | 134 |
| stroke 3 | 25 % → 46 % | 72.9 px | 0.57 | 1.84 | 132 |
| stroke 4 | 26 % → 50 % | 85.4 px | 0.57 | 1.90 | 141 |
| stroke 5 | 26 % → 46 % | 75.4 px | 0.57 | 1.78 | 167 |
| stroke 6 | 26 % → 35 % | 80.3 px | 0.57 | 1.33 | 125 |
| stroke 7 | 15 % → 53 % | 37.9 px | 0.57 | 3.47 | 123 |
| stroke 8 | 18 % → 49 % | 45.5 px | 0.57 | 2.72 | 160 |
| stroke 9 | 21 % → 50 % | 54.8 px | 0.57 | 2.36 | 144 |
| stroke 10 | 23 % → 51 % | 62.1 px | 0.57 | 2.20 | 146 |
| stroke 11 | 26 % → 54 % | 72.3 px | 0.57 | 2.10 | 139 |
| stroke 12 | 29 % → 56 % | 86.7 px | 0.57 | 1.95 | 129 |
| stroke 13 | 37 % → 59 % | 108.1 px | 0.57 | 1.58 | 146 |
| stroke 14 | 40 % → 61 % | 114.5 px | 0.57 | 1.52 | 148 |
| stroke 15 | 53 % → 67 % | 156.1 px | 0.57 | 1.27 | 138 |
| stroke 16 | 55 % → 68 % | 166.0 px | 0.57 | 1.23 | 133 |
| stroke 17 | 56 % → 69 % | 157.1 px | 0.57 | 1.23 | 145 |
| stroke 18 | 57 % → 68 % | 165.7 px | 0.57 | 1.18 | 135 |
| stroke 19 | 59 % → 66 % | 164.5 px | 0.57 | 1.13 | 133 |
| stroke 20 | 58 % → 63 % | 167.9 px | 0.57 | 1.09 | 146 |
| stroke 21 | 58 % → 60 % | 168.2 px | 0.57 | 1.04 | 155 |
| stroke 22 | 59 % → 61 % | 173.0 px | 0.57 | 1.03 | 139 |
| stroke 23 | 59 % → 59 % | 168.1 px | 0.57 | 1.01 | 140 |
| stroke 24 | 63 % → 62 % | 187.8 px | 0.57 | 1.00 | 132 |

Numbers say: wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #02 Henry Ward cream strokes — own sheet
own sheet 600 × 600 · Gouache 1.00 · 46 px · 7.5 s

![Brush Artist · Refs · #02 Henry Ward cream strokes — own sheet](Brush-Artist-Refs-02-Henry-Ward-cream-strokes-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 14 % → 15 % | 29.6 px | 0.66 | 1.04 | 194 |
| stroke 2 | 21 % → 17 % | 55.3 px | 0.66 | 0.82 | 196 |
| stroke 3 | 21 % → 21 % | 52.3 px | 0.66 | 1.02 | 181 |
| stroke 4 | 22 % → 19 % | 53.7 px | 0.66 | 0.87 | 188 |
| stroke 5 | 27 % → 23 % | 67.5 px | 0.66 | 0.84 | 187 |
| stroke 6 | 22 % → 20 % | 52.9 px | 0.66 | 0.89 | 176 |
| stroke 7 | 22 % → 13 % | 55.9 px | 0.65 | 0.59 | 184 |

## Brush Artist · Refs · #03 Henry Ward navy contours — own sheet
own sheet 600 × 600 · Impasto 1.00 · 22 px · 2.4 s

![Brush Artist · Refs · #03 Henry Ward navy contours — own sheet](Brush-Artist-Refs-03-Henry-Ward-navy-contours-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 10 % → 15 % | 20.3 px | 0.69 | 1.51 | 99 |
| stroke 2 | 18 % → 20 % | 25.7 px | 0.69 | 1.12 | 95 |
| stroke 3 | 21 % → 21 % | 30.8 px | 0.69 | 1.00 | 117 |
| stroke 4 | 20 % → 18 % | 45.1 px | 0.69 | 0.89 | 132 |

Numbers say: wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #04 Henry Ward grey cloud — own sheet
own sheet 600 × 600 · Gouache 1.00 · 50 px · 12.5 s

![Brush Artist · Refs · #04 Henry Ward grey cloud — own sheet](Brush-Artist-Refs-04-Henry-Ward-grey-cloud-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 9 % → 38 % | 26.9 px | 0.39 | 4.15 | 176 |
| stroke 2 | 14 % → 40 % | 39.8 px | 0.39 | 2.86 | 186 |
| stroke 3 | 20 % → 46 % | 55.7 px | 0.39 | 2.29 | 195 |
| stroke 4 | 24 % → 48 % | 71.2 px | 0.39 | 1.98 | 193 |
| stroke 5 | 30 % → 54 % | 91.4 px | 0.39 | 1.81 | 180 |
| stroke 6 | 31 % → 56 % | 101.9 px | 0.39 | 1.80 | 175 |
| stroke 7 | 36 % → 64 % | 106.4 px | 0.39 | 1.75 | 272 |
| stroke 8 | 37 % → 64 % | 111.3 px | 0.39 | 1.70 | 261 |
| stroke 9 | 34 % → 63 % | 102.7 px | 0.39 | 1.83 | 209 |
| stroke 10 | 37 % → 63 % | 119.8 px | 0.39 | 1.68 | 186 |
| stroke 11 | 36 % → 62 % | 102.3 px | 0.39 | 1.71 | 194 |
| stroke 12 | 37 % → 62 % | 111.4 px | 0.39 | 1.68 | 193 |
| stroke 13 | 37 % → 64 % | 106.7 px | 0.39 | 1.71 | 197 |
| stroke 14 | 37 % → 64 % | 110.5 px | 0.39 | 1.72 | 191 |
| stroke 15 | 36 % → 58 % | 104.3 px | 0.39 | 1.61 | 173 |
| stroke 16 | 39 % → 56 % | 118.4 px | 0.39 | 1.44 | 177 |
| stroke 17 | 37 % → 48 % | 106.1 px | 0.39 | 1.30 | 195 |
| stroke 18 | 37 % → 45 % | 122.7 px | 0.39 | 1.21 | 160 |
| stroke 19 | 36 % → 38 % | 108.5 px | 0.39 | 1.04 | 177 |
| stroke 20 | 40 % → 38 % | 124.7 px | 0.39 | 0.95 | 194 |

Numbers say: wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #05 Henry Ward green in rust loops — own sheet
own sheet 600 × 600 · Impasto 1.00 · 20 px · 2.5 s

![Brush Artist · Refs · #05 Henry Ward green in rust loops — own sheet](Brush-Artist-Refs-05-Henry-Ward-green-in-rust-loops-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 11 % → 18 % | 20.2 px | 0.02 | 1.55 | 104 |
| stroke 2 | 12 % → 11 % | 22.7 px | 0.03 | 0.92 | 143 |
| stroke 3 | 22 % → 20 % | 40.1 px | 0.03 | 0.92 | 116 |

Numbers say: wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #06 Henry Ward scrubbed grey — own sheet
own sheet 600 × 600 · Gouache 1.00 · 50 px · 14.0 s

![Brush Artist · Refs · #06 Henry Ward scrubbed grey — own sheet](Brush-Artist-Refs-06-Henry-Ward-scrubbed-grey-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 11 % → 42 % | 26.1 px | 0.39 | 3.97 | 351 |
| stroke 2 | 14 % → 45 % | 37.2 px | 0.39 | 3.19 | 300 |
| stroke 3 | 20 % → 47 % | 60.7 px | 0.39 | 2.39 | 215 |
| stroke 4 | 23 % → 48 % | 71.6 px | 0.39 | 2.12 | 190 |
| stroke 5 | 31 % → 61 % | 94.0 px | 0.39 | 1.95 | 131 |
| stroke 6 | 35 % → 61 % | 108.4 px | 0.39 | 1.73 | 193 |
| stroke 7 | 38 % → 64 % | 108.4 px | 0.39 | 1.69 | 181 |
| stroke 8 | 40 % → 64 % | 125.9 px | 0.39 | 1.62 | 185 |
| stroke 9 | 36 % → 63 % | 111.8 px | 0.39 | 1.74 | 170 |
| stroke 10 | 36 % → 61 % | 117.7 px | 0.39 | 1.70 | 183 |
| stroke 11 | 38 % → 63 % | 110.7 px | 0.39 | 1.66 | 210 |
| stroke 12 | 40 % → 63 % | 121.3 px | 0.39 | 1.58 | 214 |
| stroke 13 | 37 % → 63 % | 103.7 px | 0.39 | 1.74 | 205 |
| stroke 14 | 36 % → 63 % | 104.4 px | 0.39 | 1.78 | 209 |
| stroke 15 | 36 % → 64 % | 103.4 px | 0.39 | 1.77 | 197 |
| stroke 16 | 36 % → 61 % | 116.7 px | 0.39 | 1.67 | 177 |
| stroke 17 | 35 % → 54 % | 104.7 px | 0.39 | 1.53 | 187 |
| stroke 18 | 37 % → 52 % | 111.9 px | 0.39 | 1.40 | 196 |
| stroke 19 | 36 % → 48 % | 108.1 px | 0.39 | 1.31 | 209 |
| stroke 20 | 38 % → 46 % | 118.2 px | 0.39 | 1.21 | 186 |
| stroke 21 | 37 % → 38 % | 106.6 px | 0.39 | 1.04 | 194 |
| stroke 22 | 35 % → 34 % | 116.6 px | 0.39 | 0.96 | 188 |

Numbers say: wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #07 Henry Ward blue L + black zigzag — own sheet
own sheet 600 × 600 · Impasto 1.00 · 34 px · 1.9 s

![Brush Artist · Refs · #07 Henry Ward blue L + black zigzag — own sheet](Brush-Artist-Refs-07-Henry-Ward-blue-L-black-zigzag-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 14 % → 16 % | 32.3 px | 0.59 | 1.12 | 135 |
| stroke 2 | 16 % → 14 % | 39.3 px | 0.59 | 0.90 | 103 |

## Brush Artist · Refs · #08 Henry Ward olive bands — own sheet
own sheet 600 × 600 · Gouache 1.00 · 34 px · 5.2 s

![Brush Artist · Refs · #08 Henry Ward olive bands — own sheet](Brush-Artist-Refs-08-Henry-Ward-olive-bands-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 10 % → 8 % | 20.0 px | 0.58 | 0.79 | 148 |
| stroke 2 | 16 % → 10 % | 37.0 px | 0.58 | 0.58 | 158 |
| stroke 3 | 15 % → 14 % | 31.4 px | 0.58 | 0.93 | 149 |
| stroke 4 | 16 % → 11 % | 35.7 px | 0.58 | 0.68 | 178 |
| stroke 5 | 24 % → 14 % | 48.5 px | 0.58 | 0.61 | 147 |
| stroke 6 | 15 % → 8 % | 29.2 px | 0.58 | 0.52 | 172 |

## Brush Artist · Refs · #09 Henry Ward white loops — own sheet
own sheet 600 × 600 · Gouache 1.00 · 46 px · 7.0 s

![Brush Artist · Refs · #09 Henry Ward white loops — own sheet](Brush-Artist-Refs-09-Henry-Ward-white-loops-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 17 % → 4 % | 8.9 px | 0.06 | 0.22 | 841 |
| stroke 2 | 17 % → 3 % | 17.3 px | 0.07 | 0.15 | 902 |
| stroke 3 | 24 % → 2 % | 22.7 px | 0.07 | 0.10 | 737 |
| stroke 4 | 3 % → 1 % | 7.6 px | 0.06 | 0.32 | 149 |
| stroke 5 | 3 % → 1 % | 7.5 px | 0.07 | 0.40 | 146 |
| stroke 6 | 3 % → 2 % | 7.9 px | 0.07 | 0.85 | 128 |
| stroke 7 | 5 % → 2 % | 13.9 px | 0.07 | 0.46 | 148 |
| stroke 8 | 4 % → 1 % | 7.3 px | 0.06 | 0.35 | 158 |

## Brush Artist · Refs · #10 Henry Ward maroon loops — own sheet
own sheet 600 × 600 · Impasto 1.00 · 30 px · 3.1 s

![Brush Artist · Refs · #10 Henry Ward maroon loops — own sheet](Brush-Artist-Refs-10-Henry-Ward-maroon-loops-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 11 % → 26 % | 26.6 px | 0.72 | 2.43 | 217 |
| stroke 2 | 21 % → 39 % | 46.5 px | 0.71 | 1.87 | 121 |
| stroke 3 | 28 % → 35 % | 55.9 px | 0.72 | 1.27 | 157 |
| stroke 4 | 39 % → 38 % | 87.9 px | 0.72 | 0.97 | 111 |
| stroke 5 | 32 % → 29 % | 80.9 px | 0.72 | 0.91 | 139 |

Numbers say: wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #11 Henry Ward purple spun balls — own sheet
own sheet 600 × 600 · Impasto 1.00 · 36 px · 2.8 s

![Brush Artist · Refs · #11 Henry Ward purple spun balls — own sheet](Brush-Artist-Refs-11-Henry-Ward-purple-spun-balls-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 24 % → 34 % | 26.4 px | 0.68 | 1.41 | 225 |
| stroke 2 | 35 % → 45 % | 38.0 px | 0.68 | 1.31 | 234 |
| stroke 3 | 35 % → 34 % | 39.0 px | 0.68 | 0.96 | 227 |

## Brush Artist · Refs · #12 Henry Ward black-olive cage — own sheet
own sheet 600 × 600 · Gouache 1.00 · 28 px · 5.0 s

![Brush Artist · Refs · #12 Henry Ward black-olive cage — own sheet](Brush-Artist-Refs-12-Henry-Ward-black-olive-cage-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 8 % → 9 % | 14.8 px | 0.59 | 1.19 | 198 |
| stroke 2 | 8 % → 11 % | 18.8 px | 0.59 | 1.36 | 201 |
| stroke 3 | 17 % → 14 % | 26.6 px | 0.59 | 0.84 | 219 |
| stroke 4 | 17 % → 12 % | 34.7 px | 0.59 | 0.66 | 121 |
| stroke 5 | 16 % → 9 % | 30.1 px | 0.59 | 0.53 | 104 |
| stroke 6 | 26 % → 13 % | 50.0 px | 0.59 | 0.48 | 166 |

## Brush Artist · Refs · #13 Henry Ward blue streaky form — own sheet
own sheet 600 × 600 · Gouache 1.00 · 50 px · 11.5 s

![Brush Artist · Refs · #13 Henry Ward blue streaky form — own sheet](Brush-Artist-Refs-13-Henry-Ward-blue-streaky-form-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 9 % → 2 % | 26.6 px | 0.03 | 0.26 | 216 |
| stroke 2 | 13 % → 2 % | 38.6 px | 0.03 | 0.17 | 212 |
| stroke 3 | 21 % → 2 % | 60.7 px | 0.03 | 0.11 | 186 |
| stroke 4 | 23 % → 2 % | 75.5 px | 0.03 | 0.09 | 188 |
| stroke 5 | 33 % → 2 % | 94.8 px | 0.03 | 0.07 | 185 |
| stroke 6 | 35 % → 2 % | 100.0 px | 0.03 | 0.06 | 224 |
| stroke 7 | 36 % → 3 % | 106.9 px | 0.04 | 0.08 | 191 |
| stroke 8 | 39 % → 2 % | 117.8 px | 0.04 | 0.06 | 193 |
| stroke 9 | 36 % → 2 % | 111.1 px | 0.04 | 0.06 | 174 |
| stroke 10 | 37 % → 2 % | 121.1 px | 0.04 | 0.06 | 195 |
| stroke 11 | 35 % → 1 % | 108.4 px | 0.04 | 0.04 | 196 |
| stroke 12 | 36 % → 1 % | 106.5 px | 0.04 | 0.04 | 199 |
| stroke 13 | 35 % → 2 % | 108.2 px | 0.04 | 0.06 | 186 |
| stroke 14 | 34 % → 2 % | 101.1 px | 0.04 | 0.06 | 207 |
| stroke 15 | 33 % → 2 % | 94.0 px | 0.04 | 0.07 | 186 |
| stroke 16 | 37 % → 2 % | 109.2 px | 0.04 | 0.06 | 201 |
| stroke 17 | 43 % → 2 % | 106.3 px | 0.04 | 0.04 | 192 |
| stroke 18 | 47 % → 2 % | 114.1 px | 0.04 | 0.03 | 228 |
| stroke 19 | 50 % → 2 % | 101.3 px | 0.04 | 0.04 | 181 |
| stroke 20 | 56 % → 2 % | 107.5 px | 0.04 | 0.03 | 204 |
| stroke 21 | 4 % → 1 % | 7.9 px | 0.04 | 0.34 | 126 |
| stroke 22 | 3 % → 2 % | 7.8 px | 0.03 | 0.77 | 148 |
| stroke 23 | 5 % → 2 % | 14.6 px | 0.03 | 0.46 | 123 |
| stroke 24 | 4 % → 1 % | 9.9 px | 0.04 | 0.40 | 142 |
| stroke 25 | 4 % → 2 % | 11.5 px | 0.04 | 0.52 | 174 |

## Brush Artist · Refs · #14 Henry Ward olive totem — own sheet
own sheet 600 × 600 · Impasto 1.00 · 48 px · 6.4 s

![Brush Artist · Refs · #14 Henry Ward olive totem — own sheet](Brush-Artist-Refs-14-Henry-Ward-olive-totem-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 18 % → 46 % | 45.8 px | 0.37 | 2.63 | 141 |
| stroke 2 | 21 % → 50 % | 64.3 px | 0.37 | 2.44 | 127 |
| stroke 3 | 29 % → 52 % | 100.3 px | 0.37 | 1.78 | 138 |
| stroke 4 | 30 % → 54 % | 112.7 px | 0.37 | 1.81 | 144 |
| stroke 5 | 39 % → 63 % | 134.6 px | 0.37 | 1.64 | 120 |
| stroke 6 | 39 % → 65 % | 150.1 px | 0.37 | 1.68 | 134 |
| stroke 7 | 37 % → 61 % | 123.6 px | 0.37 | 1.67 | 121 |
| stroke 8 | 37 % → 63 % | 141.6 px | 0.37 | 1.70 | 137 |
| stroke 9 | 37 % → 63 % | 129.7 px | 0.37 | 1.68 | 118 |
| stroke 10 | 38 % → 62 % | 140.9 px | 0.37 | 1.62 | 140 |
| stroke 11 | 40 % → 65 % | 143.5 px | 0.37 | 1.61 | 133 |
| stroke 12 | 38 % → 65 % | 143.4 px | 0.37 | 1.71 | 135 |
| stroke 13 | 38 % → 66 % | 134.6 px | 0.37 | 1.74 | 130 |
| stroke 14 | 37 % → 62 % | 134.4 px | 0.37 | 1.69 | 143 |
| stroke 15 | 40 % → 66 % | 136.6 px | 0.37 | 1.65 | 111 |
| stroke 16 | 38 % → 63 % | 137.8 px | 0.37 | 1.67 | 145 |
| stroke 17 | 37 % → 62 % | 125.2 px | 0.37 | 1.66 | 120 |
| stroke 18 | 40 % → 66 % | 154.7 px | 0.37 | 1.64 | 116 |
| stroke 19 | 40 % → 60 % | 137.7 px | 0.37 | 1.52 | 129 |
| stroke 20 | 40 % → 55 % | 143.4 px | 0.37 | 1.35 | 144 |
| stroke 21 | 46 % → 55 % | 136.7 px | 0.37 | 1.18 | 121 |
| stroke 22 | 54 % → 53 % | 146.5 px | 0.37 | 0.99 | 140 |

Numbers say: wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #15 Ultramarine brush script — own sheet
own sheet 600 × 600 · Ink 1.00 · 4 px · 8.3 s

![Brush Artist · Refs · #15 Ultramarine brush script — own sheet](Brush-Artist-Refs-15-Ultramarine-brush-script-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 40 % → 42 % | 8.9 px | 0.66 | 1.05 | 46 |
| stroke 2 | 40 % → 42 % | 8.9 px | 0.66 | 1.06 | 46 |
| stroke 3 | 40 % → 42 % | 9.5 px | 0.74 | 1.06 | 25 |
| stroke 4 | 42 % → 45 % | 10.1 px | 0.74 | 1.09 | 19 |
| stroke 5 | 44 % → 48 % | 9.7 px | 0.73 | 1.09 | 26 |
| stroke 6 | 42 % → 44 % | 9.5 px | 0.65 | 1.05 | 48 |
| stroke 7 | 43 % → 47 % | 9.2 px | 0.72 | 1.08 | 28 |
| stroke 8 | 38 % → 41 % | 9.3 px | 0.68 | 1.05 | 48 |
| stroke 9 | 40 % → 42 % | 9.2 px | 0.69 | 1.06 | 45 |
| stroke 10 | 36 % → 38 % | 9.9 px | 0.68 | 1.05 | 46 |
| stroke 11 | 42 % → 45 % | 9.6 px | 0.70 | 1.06 | 48 |
| stroke 12 | 39 % → 41 % | 9.4 px | 0.66 | 1.06 | 52 |
| stroke 13 | 45 % → 48 % | 10.2 px | 0.71 | 1.06 | 29 |
| stroke 14 | 38 % → 41 % | 9.8 px | 0.72 | 1.07 | 24 |
| stroke 15 | 37 % → 39 % | 9.1 px | 0.69 | 1.06 | 42 |
| stroke 16 | 42 % → 45 % | 9.4 px | 0.72 | 1.06 | 23 |
| stroke 17 | 41 % → 44 % | 7.1 px | 0.71 | 1.08 | 38 |
| stroke 18 | 43 % → 45 % | 9.2 px | 0.73 | 1.06 | 26 |
| stroke 19 | 39 % → 41 % | 8.9 px | 0.66 | 1.05 | 67 |
| stroke 20 | 41 % → 43 % | 9.4 px | 0.71 | 1.06 | 39 |
| stroke 21 | 41 % → 43 % | 9.9 px | 0.70 | 1.06 | 31 |
| stroke 22 | 42 % → 45 % | 8.5 px | 0.65 | 1.06 | 72 |
| stroke 23 | 40 % → 43 % | 10.1 px | 0.73 | 1.08 | 17 |
| stroke 24 | 38 % → 41 % | 8.8 px | 0.73 | 1.07 | 34 |
| stroke 25 | 41 % → 43 % | 9.8 px | 0.72 | 1.07 | 38 |
| stroke 26 | 46 % → 49 % | 9.3 px | 0.68 | 1.05 | 31 |
| stroke 27 | 43 % → 45 % | 8.8 px | 0.63 | 1.05 | 56 |
| stroke 28 | 44 % → 46 % | 9.1 px | 0.70 | 1.06 | 46 |
| stroke 29 | 36 % → 39 % | 10.6 px | 0.72 | 1.08 | 29 |
| stroke 30 | 39 % → 41 % | 8.7 px | 0.71 | 1.04 | 42 |
| stroke 31 | 43 % → 46 % | 10.3 px | 0.75 | 1.08 | 21 |
| stroke 32 | 42 % → 46 % | 9.5 px | 0.73 | 1.09 | 25 |
| stroke 33 | 35 % → 38 % | 10.9 px | 0.72 | 1.08 | 15 |
| stroke 34 | 40 % → 43 % | 9.8 px | 0.73 | 1.08 | 18 |
| stroke 35 | 36 % → 37 % | 9.4 px | 0.65 | 1.05 | 46 |

## Brush Artist · Refs · #18 Blue oil-stick scribbles — own sheet
own sheet 600 × 600 · Pastel 1.00 · 10 px · 2.9 s

![Brush Artist · Refs · #18 Blue oil-stick scribbles — own sheet](Brush-Artist-Refs-18-Blue-oil-stick-scribbles-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 15 % → 31 % | 3.8 px | 0.49 | 2.11 | 152 |
| stroke 2 | 13 % → 37 % | 3.6 px | 0.49 | 2.73 | 142 |
| stroke 3 | 16 % → 26 % | 5.8 px | 0.49 | 1.66 | 173 |
| stroke 4 | 15 % → 29 % | 8.0 px | 0.49 | 1.88 | 149 |
| stroke 5 | 29 % → 34 % | 8.4 px | 0.49 | 1.19 | 149 |
| stroke 6 | 25 % → 26 % | 9.4 px | 0.49 | 1.02 | 124 |
| stroke 7 | 26 % → 32 % | 8.3 px | 0.49 | 1.24 | 129 |
| stroke 8 | 30 % → 30 % | 17.0 px | 0.49 | 1.00 | 179 |

Numbers say: wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #20 Orange-red crayon scribble — own sheet
own sheet 600 × 600 · Pastel 1.00 · 14 px · 2.6 s

![Brush Artist · Refs · #20 Orange-red crayon scribble — own sheet](Brush-Artist-Refs-20-Orange-red-crayon-scribble-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 8 % → 18 % | 5.5 px | 0.59 | 2.46 | 214 |
| stroke 2 | 9 % → 23 % | 6.8 px | 0.59 | 2.48 | 162 |
| stroke 3 | 13 % → 21 % | 8.5 px | 0.59 | 1.64 | 122 |
| stroke 4 | 24 % → 32 % | 8.9 px | 0.59 | 1.34 | 149 |
| stroke 5 | 27 % → 27 % | 7.7 px | 0.59 | 1.00 | 162 |
| stroke 6 | 22 % → 22 % | 16.8 px | 0.59 | 1.00 | 167 |

Numbers say: wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #21 Gritty black contours — own sheet
own sheet 600 × 600 · Gouache 1.00 · 12 px · 3.8 s

![Brush Artist · Refs · #21 Gritty black contours — own sheet](Brush-Artist-Refs-21-Gritty-black-contours-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 4 % → 3 % | 4.9 px | 0.37 | 0.70 | 92 |
| stroke 2 | 5 % → 2 % | 7.6 px | 0.37 | 0.43 | 152 |
| stroke 3 | 7 % → 2 % | 5.9 px | 0.37 | 0.26 | 118 |
| stroke 4 | 8 % → 3 % | 9.8 px | 0.37 | 0.40 | 134 |
| stroke 5 | 10 % → 3 % | 11.9 px | 0.37 | 0.34 | 79 |

## Brush Artist · Refs · #22 Bold black brush poster — own sheet
own sheet 600 × 600 · Ink 1.00 · 20 px · 5.0 s

![Brush Artist · Refs · #22 Bold black brush poster — own sheet](Brush-Artist-Refs-22-Bold-black-brush-poster-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 22 % → 27 % | 36.3 px | 0.94 | 1.20 | 99 |
| stroke 2 | 27 % → 37 % | 41.4 px | 0.94 | 1.37 | 31 |
| stroke 3 | 28 % → 29 % | 43.6 px | 0.94 | 1.00 | 47 |
| stroke 4 | 27 % → 39 % | 53.7 px | 0.94 | 1.43 | 75 |
| stroke 5 | 25 % → 25 % | 42.9 px | 0.94 | 1.00 | 81 |

## Brush Artist · Refs · #23 Dry white on orange + black line — own sheet
own sheet 600 × 600 · Gouache 1.00 · 50 px · 7.5 s

![Brush Artist · Refs · #23 Dry white on orange + black line — own sheet](Brush-Artist-Refs-23-Dry-white-on-orange-black-line-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 6 % → 11 % | 22.3 px | 0.40 | 1.71 | 131 |
| stroke 2 | 9 % → 10 % | 31.8 px | 0.40 | 1.10 | 142 |
| stroke 3 | 13 % → 11 % | 48.0 px | 0.40 | 0.82 | 139 |
| stroke 4 | 15 % → 12 % | 59.0 px | 0.40 | 0.80 | 147 |
| stroke 5 | 21 % → 14 % | 75.7 px | 0.40 | 0.67 | 146 |
| stroke 6 | 21 % → 16 % | 88.3 px | 0.40 | 0.77 | 125 |
| stroke 7 | 17 % → 15 % | 65.6 px | 0.39 | 0.87 | 125 |
| stroke 8 | 18 % → 14 % | 70.7 px | 0.39 | 0.79 | 146 |
| stroke 9 | 18 % → 15 % | 68.7 px | 0.39 | 0.83 | 140 |
| stroke 10 | 18 % → 15 % | 69.0 px | 0.39 | 0.87 | 146 |
| stroke 11 | 20 % → 17 % | 74.8 px | 0.39 | 0.85 | 137 |
| stroke 12 | 21 % → 17 % | 80.3 px | 0.39 | 0.81 | 170 |
| stroke 13 | 21 % → 19 % | 77.7 px | 0.39 | 0.89 | 128 |
| stroke 14 | 20 % → 19 % | 81.1 px | 0.39 | 0.91 | 158 |
| stroke 15 | 20 % → 16 % | 73.7 px | 0.39 | 0.80 | 125 |
| stroke 16 | 20 % → 14 % | 80.1 px | 0.39 | 0.70 | 133 |
| stroke 17 | 20 % → 13 % | 71.5 px | 0.39 | 0.61 | 131 |
| stroke 18 | 24 % → 13 % | 86.5 px | 0.39 | 0.55 | 129 |

Numbers say: wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #24 Picasso flat oil — own sheet
own sheet 600 × 600 · Oil 0.89 · Oil glaze 0.11 · 34 px · 4.8 s

![Brush Artist · Refs · #24 Picasso flat oil — own sheet](Brush-Artist-Refs-24-Picasso-flat-oil-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 14 % → 42 % | 29.4 px | 0.22 | 3.06 | 120 |
| stroke 2 | 18 % → 46 % | 41.9 px | 0.22 | 2.57 | 130 |
| stroke 3 | 26 % → 56 % | 57.4 px | 0.22 | 2.14 | 121 |
| stroke 4 | 35 % → 62 % | 77.7 px | 0.22 | 1.79 | 122 |
| stroke 5 | 40 % → 67 % | 89.3 px | 0.21 | 1.66 | 127 |
| stroke 6 | 41 % → 62 % | 96.0 px | 0.21 | 1.50 | 138 |
| stroke 7 | 41 % → 61 % | 87.0 px | 0.21 | 1.48 | 119 |
| stroke 8 | 41 % → 61 % | 99.6 px | 0.22 | 1.49 | 125 |
| stroke 9 | 34 % → 57 % | 73.4 px | 0.22 | 1.70 | 121 |
| stroke 10 | 35 % → 56 % | 84.6 px | 0.22 | 1.59 | 120 |
| stroke 11 | 33 % → 55 % | 70.2 px | 0.22 | 1.66 | 131 |
| stroke 12 | 35 % → 55 % | 82.8 px | 0.22 | 1.57 | 135 |
| stroke 13 | 34 % → 62 % | 74.8 px | 0.22 | 1.81 | 122 |
| stroke 14 | 36 % → 63 % | 80.8 px | 0.22 | 1.78 | 124 |
| stroke 15 | 34 % → 57 % | 71.9 px | 0.21 | 1.67 | 145 |
| stroke 16 | 34 % → 50 % | 78.6 px | 0.21 | 1.46 | 149 |
| stroke 17 | 39 % → 44 % | 81.0 px | 0.21 | 1.14 | 127 |
| stroke 18 | 39 % → 39 % | 93.8 px | 0.21 | 1.00 | 127 |

Numbers say: wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #25 Yellow heavy flat stroke — own sheet
own sheet 600 × 600 · Impasto 1.00 · 110 px · 2.8 s

![Brush Artist · Refs · #25 Yellow heavy flat stroke — own sheet](Brush-Artist-Refs-25-Yellow-heavy-flat-stroke-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 18 % → 18 % | 104.3 px | 0.17 | 0.98 | 670 |

## Brush Artist · Refs · #27 Orange impasto swatch — own sheet
own sheet 600 × 600 · Impasto 1.00 · 60 px · 3.0 s

![Brush Artist · Refs · #27 Orange impasto swatch — own sheet](Brush-Artist-Refs-27-Orange-impasto-swatch-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 8 % → 21 % | 61.8 px | 0.33 | 2.60 | 69 |
| stroke 2 | 7 % → 33 % | 62.6 px | 0.33 | 4.67 | 53 |
| stroke 3 | 25 % → 36 % | 245.8 px | 0.33 | 1.40 | 38 |
| stroke 4 | 10 % → 12 % | 69.8 px | 0.33 | 1.25 | 59 |
| stroke 5 | 17 % → 33 % | 63.5 px | 0.33 | 1.90 | 68 |
| stroke 6 | 18 % → 32 % | 145.3 px | 0.33 | 1.79 | 63 |
| stroke 7 | 8 % → 15 % | 70.4 px | 0.33 | 1.87 | 55 |
| stroke 8 | 33 % → 34 % | 337.7 px | 0.33 | 1.04 | 41 |
| stroke 9 | 38 % → 37 % | 185.5 px | 0.33 | 0.98 | 71 |
| stroke 10 | 34 % → 33 % | 305.4 px | 0.33 | 0.98 | 53 |

Numbers say: wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #28 Miles Davis black lines — own sheet
own sheet 600 × 600 · Ink 1.00 · 22 px · 5.7 s

![Brush Artist · Refs · #28 Miles Davis black lines — own sheet](Brush-Artist-Refs-28-Miles-Davis-black-lines-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 22 % → 32 % | 36.5 px | 0.88 | 1.42 | 180 |
| stroke 2 | 28 % → 49 % | 38.2 px | 0.88 | 1.73 | 128 |
| stroke 3 | 39 % → 44 % | 75.1 px | 0.88 | 1.12 | 103 |
| stroke 4 | 42 % → 48 % | 83.7 px | 0.88 | 1.15 | 150 |
| stroke 5 | 55 % → 55 % | 109.8 px | 0.88 | 1.00 | 121 |

Numbers say: wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #29 Shrigley magenta asterisk — own sheet
own sheet 600 × 600 · Watercolour 1.00 · 70 px · 5.8 s

![Brush Artist · Refs · #29 Shrigley magenta asterisk — own sheet](Brush-Artist-Refs-29-Shrigley-magenta-asterisk-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 13 % → 37 % | 46.6 px | 0.67 | 2.86 | 188 |
| stroke 2 | 12 % → 12 % | 87.1 px | 0.67 | 1.00 | 198 |
| stroke 3 | 28 % → 37 % | 100.9 px | 0.67 | 1.31 | 193 |
| stroke 4 | 23 % → 23 % | 164.0 px | 0.67 | 1.02 | 207 |

Numbers say: wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #30 Red gouache face patch — own sheet
own sheet 600 × 600 · Gouache 1.00 · 60 px · 10.6 s

![Brush Artist · Refs · #30 Red gouache face patch — own sheet](Brush-Artist-Refs-30-Red-gouache-face-patch-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 12 % → 37 % | 51.5 px | 0.54 | 3.23 | 163 |
| stroke 2 | 15 % → 40 % | 74.5 px | 0.54 | 2.72 | 157 |
| stroke 3 | 24 % → 50 % | 115.9 px | 0.54 | 2.06 | 155 |
| stroke 4 | 27 % → 52 % | 134.1 px | 0.54 | 1.94 | 181 |
| stroke 5 | 34 % → 60 % | 159.9 px | 0.54 | 1.77 | 159 |
| stroke 6 | 35 % → 61 % | 178.3 px | 0.54 | 1.76 | 166 |
| stroke 7 | 34 % → 59 % | 160.9 px | 0.54 | 1.73 | 166 |
| stroke 8 | 34 % → 56 % | 162.5 px | 0.54 | 1.66 | 181 |
| stroke 9 | 36 % → 60 % | 173.1 px | 0.54 | 1.66 | 168 |
| stroke 10 | 38 % → 62 % | 196.8 px | 0.54 | 1.64 | 165 |
| stroke 11 | 37 % → 61 % | 182.4 px | 0.54 | 1.66 | 154 |
| stroke 12 | 36 % → 58 % | 178.3 px | 0.54 | 1.62 | 170 |
| stroke 13 | 33 % → 46 % | 156.5 px | 0.54 | 1.39 | 163 |
| stroke 14 | 33 % → 41 % | 157.6 px | 0.54 | 1.25 | 204 |
| stroke 15 | 33 % → 37 % | 153.4 px | 0.54 | 1.12 | 184 |
| stroke 16 | 39 % → 39 % | 184.9 px | 0.54 | 0.99 | 170 |

Numbers say: wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #31 Warhol blotted line — own sheet
own sheet 600 × 600 · Ink 1.00 · 6 px · 4.5 s

![Brush Artist · Refs · #31 Warhol blotted line — own sheet](Brush-Artist-Refs-31-Warhol-blotted-line-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 21 % → 42 % | 15.8 px | 0.82 | 1.98 | 85 |
| stroke 2 | 17 % → 23 % | 15.9 px | 0.82 | 1.34 | 70 |
| stroke 3 | 24 % → 25 % | 25.1 px | 0.81 | 1.02 | 78 |
| stroke 4 | 31 % → 40 % | 31.8 px | 0.82 | 1.28 | 50 |
| stroke 5 | 35 % → 44 % | 36.4 px | 0.82 | 1.23 | 59 |
| stroke 6 | 32 % → 33 % | 26.7 px | 0.81 | 1.03 | 60 |

Numbers say: wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #32 Thick orange swipes — own sheet
own sheet 600 × 600 · Impasto 1.00 · 90 px · 3.4 s

![Brush Artist · Refs · #32 Thick orange swipes — own sheet](Brush-Artist-Refs-32-Thick-orange-swipes-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 14 % → 27 % | 86.1 px | 0.03 | 1.90 | 339 |
| stroke 2 | 26 % → 38 % | 177.0 px | 0.03 | 1.43 | 314 |
| stroke 3 | 28 % → 27 % | 177.6 px | 0.03 | 0.98 | 289 |

Numbers say: wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #33 Red wet-in-wet band — own sheet
own sheet 600 × 600 · Watercolour 1.00 · 80 px · 9.1 s

![Brush Artist · Refs · #33 Red wet-in-wet band — own sheet](Brush-Artist-Refs-33-Red-wet-in-wet-band-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 24 % → 59 % | 89.6 px | 0.61 | 2.52 | 386 |
| stroke 2 | 30 % → 53 % | 244.8 px | 0.62 | 1.76 | 115 |
| stroke 3 | 37 % → 55 % | 358.4 px | 0.61 | 1.49 | 105 |
| stroke 4 | 43 % → 62 % | 415.9 px | 0.62 | 1.44 | 94 |
| stroke 5 | 43 % → 57 % | 361.3 px | 0.61 | 1.33 | 117 |
| stroke 6 | 44 % → 49 % | 333.3 px | 0.60 | 1.13 | 119 |

Numbers say: wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #34 Magenta oil patches — own sheet
own sheet 600 × 600 · Oil 0.89 · Oil glaze 0.11 · 60 px · 3.2 s

![Brush Artist · Refs · #34 Magenta oil patches — own sheet](Brush-Artist-Refs-34-Magenta-oil-patches-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 8 % → 40 % | 58.6 px | 0.12 | 4.85 | 96 |
| stroke 2 | 9 % → 28 % | 59.5 px | 0.13 | 3.22 | 74 |
| stroke 3 | 7 % → 34 % | 59.0 px | 0.12 | 4.77 | 60 |
| stroke 4 | 15 % → 20 % | 125.3 px | 0.12 | 1.27 | 60 |
| stroke 5 | 22 % → 32 % | 118.3 px | 0.12 | 1.44 | 102 |
| stroke 6 | 19 % → 36 % | 164.2 px | 0.12 | 1.88 | 64 |
| stroke 7 | 28 % → 33 % | 224.7 px | 0.12 | 1.19 | 70 |
| stroke 8 | 32 % → 38 % | 223.8 px | 0.12 | 1.19 | 89 |
| stroke 9 | 24 % → 26 % | 155.3 px | 0.12 | 1.07 | 89 |
| stroke 10 | 28 % → 28 % | 246.0 px | 0.12 | 1.00 | 64 |
| stroke 11 | 35 % → 35 % | 309.4 px | 0.12 | 1.00 | 63 |
| stroke 12 | 25 % → 25 % | 177.1 px | 0.12 | 1.00 | 73 |

Numbers say: wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #35 Red band with runs — own sheet
own sheet 600 × 600 · Watercolour 1.00 · 70 px · 6.8 s

![Brush Artist · Refs · #35 Red band with runs — own sheet](Brush-Artist-Refs-35-Red-band-with-runs-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 37 % → 51 % | 138.9 px | 0.44 | 1.38 | 319 |

## Brush Artist · Refs · #36 Magenta letters flat brush — own sheet
own sheet 600 × 600 · Gouache 1.00 · 36 px · 10.0 s

![Brush Artist · Refs · #36 Magenta letters flat brush — own sheet](Brush-Artist-Refs-36-Magenta-letters-flat-brush-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 20 % → 39 % | 59.0 px | 0.50 | 1.95 | 32 |
| stroke 2 | 20 % → 32 % | 46.6 px | 0.50 | 1.59 | 32 |
| stroke 3 | 29 % → 54 % | 86.8 px | 0.50 | 1.86 | 29 |
| stroke 4 | 26 % → 44 % | 51.2 px | 0.50 | 1.67 | 112 |
| stroke 5 | 33 % → 55 % | 96.1 px | 0.50 | 1.67 | 72 |
| stroke 6 | 42 % → 56 % | 242.4 px | 0.50 | 1.33 | 14 |
| stroke 7 | 30 % → 44 % | 56.7 px | 0.50 | 1.45 | 114 |
| stroke 8 | 31 % → 53 % | 98.5 px | 0.50 | 1.68 | 62 |
| stroke 9 | 38 % → 51 % | 158.3 px | 0.50 | 1.33 | 24 |
| stroke 10 | 37 % → 63 % | 106.7 px | 0.50 | 1.72 | 72 |
| stroke 11 | 39 % → 62 % | 225.9 px | 0.50 | 1.58 | 15 |
| stroke 12 | 43 % → 56 % | 81.9 px | 0.50 | 1.29 | 111 |
| stroke 13 | 32 % → 46 % | 117.6 px | 0.50 | 1.43 | 34 |
| stroke 14 | 35 % → 52 % | 134.4 px | 0.50 | 1.47 | 27 |
| stroke 15 | 38 % → 56 % | 108.5 px | 0.50 | 1.49 | 72 |
| stroke 16 | 41 % → 50 % | 232.0 px | 0.50 | 1.23 | 15 |
| stroke 17 | 44 % → 52 % | 81.7 px | 0.50 | 1.19 | 116 |
| stroke 18 | 27 % → 36 % | 97.5 px | 0.50 | 1.35 | 33 |
| stroke 19 | 40 % → 39 % | 117.0 px | 0.50 | 0.96 | 26 |
| stroke 20 | 45 % → 45 % | 132.2 px | 0.50 | 0.99 | 33 |
| stroke 21 | 41 % → 39 % | 78.6 px | 0.50 | 0.96 | 73 |

Numbers say: wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #37 Oil still life dabs — own sheet
own sheet 600 × 600 · Oil 0.89 · Oil glaze 0.11 · 40 px · 2.4 s

![Brush Artist · Refs · #37 Oil still life dabs — own sheet](Brush-Artist-Refs-37-Oil-still-life-dabs-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 7 % → 7 % | 42.1 px | 0.38 | 1.00 | 28 |
| stroke 2 | 6 % → 27 % | 42.8 px | 0.38 | 4.44 | 26 |
| stroke 3 | 11 % → 34 % | 88.7 px | 0.38 | 3.01 | 18 |
| stroke 4 | 9 % → 9 % | 41.0 px | 0.38 | 1.00 | 41 |
| stroke 5 | 6 % → 10 % | 41.0 px | 0.38 | 1.73 | 21 |
| stroke 6 | 13 % → 30 % | 80.6 px | 0.38 | 2.32 | 26 |
| stroke 7 | 10 % → 23 % | 110.5 px | 0.38 | 2.21 | 16 |
| stroke 8 | 8 % → 13 % | 86.6 px | 0.38 | 1.62 | 17 |
| stroke 9 | 12 % → 13 % | 65.1 px | 0.37 | 1.08 | 34 |
| stroke 10 | 20 % → 24 % | 102.6 px | 0.38 | 1.20 | 34 |
| stroke 11 | 24 % → 27 % | 195.5 px | 0.39 | 1.17 | 24 |
| stroke 12 | 20 % → 21 % | 220.2 px | 0.39 | 1.01 | 16 |
| stroke 13 | 16 % → 16 % | 162.7 px | 0.39 | 1.00 | 13 |
| stroke 14 | 16 % → 16 % | 127.3 px | 0.38 | 1.00 | 17 |

Numbers say: wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #38 Sanguine drawing — own sheet
own sheet 600 × 600 · Pastel 1.00 · 6 px · 2.1 s

![Brush Artist · Refs · #38 Sanguine drawing — own sheet](Brush-Artist-Refs-38-Sanguine-drawing-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 3 % → 14 % | 2.9 px | 0.57 | 5.30 | 8 |
| stroke 2 | 3 % → 7 % | 2.9 px | 0.58 | 2.89 | 6 |
| stroke 3 | 3 % → 9 % | 2.9 px | 0.57 | 3.40 | 6 |
| stroke 4 | 2 % → 17 % | 2.7 px | 0.57 | 7.20 | 6 |
| stroke 5 | 2 % → 7 % | 2.7 px | 0.57 | 3.03 | 4 |
| stroke 6 | 3 % → 19 % | 3.4 px | 0.57 | 6.31 | 5 |
| stroke 7 | 5 % → 14 % | 5.2 px | 0.57 | 3.07 | 4 |
| stroke 8 | 4 % → 16 % | 4.7 px | 0.57 | 3.79 | 4 |
| stroke 9 | 3 % → 7 % | 2.9 px | 0.57 | 2.66 | 5 |
| stroke 10 | 4 % → 16 % | 4.7 px | 0.57 | 3.83 | 6 |
| stroke 11 | 3 % → 4 % | 2.9 px | 0.57 | 1.61 | 3 |
| stroke 12 | 4 % → 15 % | 4.8 px | 0.57 | 3.58 | 7 |
| stroke 13 | 8 % → 17 % | 8.9 px | 0.57 | 2.23 | 4 |
| stroke 14 | 4 % → 14 % | 4.9 px | 0.57 | 3.19 | 7 |
| stroke 15 | 9 % → 18 % | 10.7 px | 0.57 | 1.86 | 4 |
| stroke 16 | 6 % → 16 % | 6.6 px | 0.57 | 2.71 | 4 |
| stroke 17 | 4 % → 9 % | 4.4 px | 0.57 | 2.25 | 6 |
| stroke 18 | 3 % → 5 % | 2.9 px | 0.57 | 1.85 | 3 |
| stroke 19 | 6 % → 16 % | 6.9 px | 0.57 | 2.68 | 7 |
| stroke 20 | 8 % → 14 % | 9.2 px | 0.57 | 1.70 | 4 |
| stroke 21 | 4 % → 4 % | 4.3 px | 0.57 | 1.00 | 5 |
| stroke 22 | 8 % → 13 % | 8.6 px | 0.57 | 1.79 | 5 |
| stroke 23 | 7 % → 12 % | 8.3 px | 0.57 | 1.61 | 4 |
| stroke 24 | 4 % → 7 % | 4.7 px | 0.57 | 1.71 | 7 |
| stroke 25 | 8 % → 14 % | 8.7 px | 0.57 | 1.84 | 4 |
| stroke 26 | 6 % → 8 % | 6.5 px | 0.57 | 1.34 | 5 |
| stroke 27 | 4 % → 4 % | 4.3 px | 0.57 | 1.10 | 4 |
| stroke 28 | 7 % → 11 % | 8.2 px | 0.57 | 1.59 | 5 |
| stroke 29 | 8 % → 17 % | 8.8 px | 0.57 | 2.21 | 7 |
| stroke 30 | 13 % → 17 % | 14.9 px | 0.57 | 1.29 | 7 |
| stroke 31 | 5 % → 6 % | 5.4 px | 0.57 | 1.29 | 4 |
| stroke 32 | 10 % → 13 % | 11.8 px | 0.57 | 1.24 | 6 |
| stroke 33 | 7 % → 8 % | 8.5 px | 0.57 | 1.07 | 4 |
| stroke 34 | 11 % → 14 % | 12.0 px | 0.57 | 1.36 | 4 |
| stroke 35 | 9 % → 14 % | 10.0 px | 0.57 | 1.61 | 5 |
| stroke 36 | 10 % → 13 % | 11.4 px | 0.57 | 1.26 | 7 |
| stroke 37 | 9 % → 16 % | 10.5 px | 0.57 | 1.71 | 5 |
| stroke 38 | 13 % → 19 % | 14.8 px | 0.57 | 1.48 | 3 |
| stroke 39 | 14 % → 17 % | 15.7 px | 0.57 | 1.21 | 9 |
| stroke 40 | 6 % → 7 % | 7.2 px | 0.57 | 1.14 | 6 |
| stroke 41 | 16 % → 16 % | 17.7 px | 0.57 | 1.01 | 4 |
| stroke 42 | 14 % → 16 % | 15.2 px | 0.57 | 1.17 | 7 |
| stroke 43 | 10 % → 12 % | 11.6 px | 0.57 | 1.17 | 7 |
| stroke 44 | 12 % → 15 % | 14.3 px | 0.57 | 1.22 | 4 |
| stroke 45 | 2 % → 2 % | 2.7 px | 0.57 | 1.00 | 3 |
| stroke 46 | 16 % → 16 % | 18.5 px | 0.57 | 1.00 | 4 |
| stroke 47 | 13 % → 13 % | 15.0 px | 0.57 | 1.00 | 4 |
| stroke 48 | 12 % → 13 % | 14.3 px | 0.57 | 1.07 | 6 |
| stroke 49 | 19 % → 19 % | 21.5 px | 0.57 | 1.00 | 3 |
| stroke 50 | 10 % → 10 % | 11.6 px | 0.57 | 1.00 | 7 |

Numbers say: wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #39 Very thick impasto — own sheet
own sheet 600 × 600 · Impasto 1.00 · 60 px · 4.2 s

![Brush Artist · Refs · #39 Very thick impasto — own sheet](Brush-Artist-Refs-39-Very-thick-impasto-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 26 % → 37 % | 59.6 px | 0.43 | 1.42 | 273 |
| stroke 2 | 31 % → 48 % | 93.9 px | 0.44 | 1.54 | 281 |
| stroke 3 | 37 % → 49 % | 124.6 px | 0.43 | 1.33 | 260 |
| stroke 4 | 31 % → 44 % | 90.9 px | 0.44 | 1.41 | 259 |
| stroke 5 | 42 % → 41 % | 104.2 px | 0.44 | 0.98 | 269 |

Numbers say: wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #40 Watercolour blooms — own sheet
own sheet 600 × 600 · Watercolour 1.00 · 90 px · 7.1 s

![Brush Artist · Refs · #40 Watercolour blooms — own sheet](Brush-Artist-Refs-40-Watercolour-blooms-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 22 % → 28 % | 95.0 px | 0.12 | 1.31 | 787 |

## Brush Artist · Refs · #41 Coloured pencil hatching — own sheet
own sheet 600 × 600 · Pastel 1.00 · 4 px · 2.4 s

![Brush Artist · Refs · #41 Coloured pencil hatching — own sheet](Brush-Artist-Refs-41-Coloured-pencil-hatching-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 3 % → 13 % | 2.2 px | 0.35 | 4.64 | 5 |
| stroke 2 | 3 % → 7 % | 2.3 px | 0.35 | 2.29 | 2 |
| stroke 3 | 2 % → 11 % | 1.9 px | 0.35 | 4.38 | 5 |
| stroke 4 | 3 % → 19 % | 2.1 px | 0.35 | 6.73 | 3 |
| stroke 5 | 4 % → 7 % | 2.9 px | 0.35 | 1.83 | 4 |
| stroke 6 | 3 % → 13 % | 2.3 px | 0.35 | 4.19 | 2 |
| stroke 7 | 3 % → 15 % | 2.6 px | 0.35 | 4.43 | 3 |
| stroke 8 | 3 % → 12 % | 2.1 px | 0.35 | 4.20 | 2 |
| stroke 9 | 5 % → 11 % | 3.6 px | 0.35 | 2.27 | 5 |
| stroke 10 | 5 % → 15 % | 3.8 px | 0.35 | 2.99 | 2 |
| stroke 11 | 4 % → 13 % | 3.0 px | 0.35 | 3.28 | 3 |
| stroke 12 | 3 % → 3 % | 2.1 px | 0.35 | 1.00 | 2 |
| stroke 13 | 7 % → 17 % | 5.2 px | 0.35 | 2.45 | 4 |
| stroke 14 | 3 % → 13 % | 2.4 px | 0.35 | 4.19 | 2 |
| stroke 15 | 6 % → 12 % | 4.4 px | 0.35 | 2.09 | 6 |
| stroke 16 | 7 % → 11 % | 5.1 px | 0.35 | 1.61 | 5 |
| stroke 17 | 3 % → 3 % | 2.1 px | 0.35 | 1.00 | 2 |
| stroke 18 | 5 % → 8 % | 3.6 px | 0.35 | 1.65 | 5 |
| stroke 19 | 5 % → 13 % | 3.8 px | 0.35 | 2.72 | 3 |
| stroke 20 | 5 % → 14 % | 3.7 px | 0.35 | 2.92 | 4 |
| stroke 21 | 4 % → 13 % | 3.2 px | 0.35 | 3.20 | 2 |
| stroke 22 | 9 % → 16 % | 6.8 px | 0.35 | 1.77 | 5 |
| stroke 23 | 9 % → 13 % | 6.5 px | 0.35 | 1.55 | 5 |
| stroke 24 | 6 % → 14 % | 4.7 px | 0.35 | 2.18 | 5 |
| stroke 25 | 5 % → 10 % | 3.5 px | 0.35 | 2.27 | 2 |
| stroke 26 | 3 % → 6 % | 2.7 px | 0.35 | 1.81 | 5 |
| stroke 27 | 3 % → 7 % | 2.3 px | 0.35 | 2.26 | 2 |
| stroke 28 | 6 % → 10 % | 4.5 px | 0.35 | 1.70 | 5 |
| stroke 29 | 3 % → 13 % | 2.4 px | 0.35 | 4.21 | 2 |
| stroke 30 | 6 % → 9 % | 4.4 px | 0.35 | 1.46 | 4 |
| stroke 31 | 7 % → 14 % | 5.1 px | 0.35 | 2.14 | 3 |
| stroke 32 | 3 % → 6 % | 2.5 px | 0.35 | 1.78 | 5 |
| stroke 33 | 6 % → 11 % | 5.0 px | 0.35 | 1.67 | 3 |
| stroke 34 | 3 % → 6 % | 2.6 px | 0.35 | 1.73 | 3 |
| stroke 35 | 7 % → 14 % | 5.0 px | 0.35 | 2.09 | 3 |
| stroke 36 | 5 % → 5 % | 3.7 px | 0.35 | 1.01 | 4 |
| stroke 37 | 7 % → 15 % | 5.2 px | 0.35 | 2.15 | 2 |
| stroke 38 | 8 % → 13 % | 5.8 px | 0.35 | 1.66 | 2 |
| stroke 39 | 7 % → 11 % | 5.1 px | 0.35 | 1.67 | 4 |
| stroke 40 | 8 % → 18 % | 6.2 px | 0.35 | 2.21 | 2 |
| stroke 41 | 9 % → 13 % | 6.9 px | 0.35 | 1.48 | 4 |
| stroke 42 | 10 % → 17 % | 7.7 px | 0.35 | 1.73 | 2 |
| stroke 43 | 5 % → 9 % | 3.9 px | 0.35 | 1.66 | 4 |
| stroke 44 | 10 % → 13 % | 7.3 px | 0.35 | 1.40 | 4 |
| stroke 45 | 13 % → 18 % | 9.9 px | 0.35 | 1.35 | 5 |
| stroke 46 | 5 % → 7 % | 3.6 px | 0.34 | 1.41 | 5 |
| stroke 47 | 11 % → 13 % | 8.0 px | 0.35 | 1.20 | 3 |
| stroke 48 | 12 % → 16 % | 9.2 px | 0.35 | 1.34 | 5 |
| stroke 49 | 6 % → 9 % | 4.2 px | 0.35 | 1.65 | 5 |
| stroke 50 | 7 % → 7 % | 5.2 px | 0.34 | 1.00 | 2 |
| stroke 51 | 8 % → 15 % | 6.4 px | 0.35 | 1.74 | 5 |
| stroke 52 | 12 % → 14 % | 9.1 px | 0.35 | 1.19 | 4 |
| stroke 53 | 11 % → 14 % | 8.1 px | 0.35 | 1.36 | 8 |
| stroke 54 | 10 % → 14 % | 7.4 px | 0.35 | 1.47 | 3 |
| stroke 55 | 11 % → 14 % | 8.2 px | 0.35 | 1.33 | 3 |
| stroke 56 | 11 % → 12 % | 8.4 px | 0.35 | 1.11 | 8 |
| stroke 57 | 9 % → 13 % | 7.1 px | 0.35 | 1.37 | 3 |
| stroke 58 | 10 % → 11 % | 7.7 px | 0.35 | 1.14 | 5 |
| stroke 59 | 11 % → 13 % | 8.4 px | 0.35 | 1.18 | 7 |
| stroke 60 | 16 % → 20 % | 11.9 px | 0.35 | 1.26 | 2 |
| stroke 61 | 19 % → 20 % | 14.5 px | 0.35 | 1.04 | 3 |
| stroke 62 | 10 % → 10 % | 7.3 px | 0.35 | 1.00 | 3 |
| stroke 63 | 11 % → 12 % | 8.7 px | 0.35 | 1.07 | 3 |
| stroke 64 | 14 % → 14 % | 10.7 px | 0.35 | 1.02 | 9 |
| stroke 65 | 15 % → 15 % | 11.5 px | 0.35 | 1.00 | 3 |
| stroke 66 | 14 % → 14 % | 10.7 px | 0.35 | 1.00 | 4 |
| stroke 67 | 12 % → 12 % | 8.8 px | 0.35 | 1.06 | 5 |
| stroke 68 | 5 % → 9 % | 3.6 px | 0.35 | 1.88 | 3 |
| stroke 69 | 5 % → 5 % | 4.1 px | 0.35 | 1.00 | 6 |
| stroke 70 | 10 % → 13 % | 7.4 px | 0.35 | 1.28 | 3 |
| stroke 71 | 9 % → 11 % | 7.1 px | 0.35 | 1.15 | 5 |
| stroke 72 | 5 % → 7 % | 4.2 px | 0.35 | 1.23 | 3 |
| stroke 73 | 12 % → 12 % | 9.3 px | 0.35 | 1.00 | 3 |
| stroke 74 | 14 % → 14 % | 10.8 px | 0.35 | 1.00 | 4 |
| stroke 75 | 15 % → 15 % | 11.4 px | 0.35 | 1.00 | 3 |
| stroke 76 | 14 % → 14 % | 10.5 px | 0.35 | 1.00 | 3 |
| stroke 77 | 7 % → 10 % | 5.4 px | 0.35 | 1.34 | 2 |
| stroke 78 | 9 % → 9 % | 7.0 px | 0.35 | 1.00 | 5 |
| stroke 79 | 7 % → 7 % | 5.7 px | 0.35 | 1.00 | 3 |
| stroke 80 | 11 % → 11 % | 8.3 px | 0.35 | 1.00 | 4 |

Numbers say: wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #42 Oil pastel shaggy — own sheet
own sheet 600 × 600 · Pastel 1.00 · 18 px · 2.5 s

![Brush Artist · Refs · #42 Oil pastel shaggy — own sheet](Brush-Artist-Refs-42-Oil-pastel-shaggy-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 5 % → 27 % | 8.0 px | 0.28 | 5.73 | 13 |
| stroke 2 | 5 % → 24 % | 8.6 px | 0.28 | 4.69 | 13 |
| stroke 3 | 5 % → 29 % | 8.9 px | 0.28 | 5.42 | 11 |
| stroke 4 | 5 % → 11 % | 8.8 px | 0.28 | 2.08 | 8 |
| stroke 5 | 6 % → 11 % | 9.9 px | 0.28 | 1.85 | 6 |
| stroke 6 | 8 % → 37 % | 13.9 px | 0.29 | 4.44 | 10 |
| stroke 7 | 11 % → 31 % | 17.6 px | 0.28 | 2.90 | 7 |
| stroke 8 | 7 % → 38 % | 11.4 px | 0.28 | 5.55 | 6 |
| stroke 9 | 8 % → 21 % | 13.9 px | 0.28 | 2.53 | 7 |
| stroke 10 | 8 % → 18 % | 13.2 px | 0.28 | 2.32 | 10 |
| stroke 11 | 6 % → 27 % | 9.4 px | 0.28 | 4.74 | 10 |
| stroke 12 | 8 % → 19 % | 13.6 px | 0.28 | 2.29 | 8 |
| stroke 13 | 13 % → 24 % | 21.0 px | 0.28 | 1.92 | 14 |
| stroke 14 | 5 % → 23 % | 7.9 px | 0.28 | 4.77 | 12 |
| stroke 15 | 5 % → 24 % | 9.0 px | 0.29 | 4.38 | 7 |
| stroke 16 | 9 % → 21 % | 15.7 px | 0.29 | 2.18 | 8 |
| stroke 17 | 17 % → 39 % | 28.0 px | 0.29 | 2.34 | 13 |
| stroke 18 | 14 % → 25 % | 22.8 px | 0.29 | 1.79 | 6 |
| stroke 19 | 15 % → 32 % | 24.9 px | 0.28 | 2.09 | 8 |
| stroke 20 | 21 % → 39 % | 35.1 px | 0.28 | 1.85 | 11 |
| stroke 21 | 9 % → 16 % | 14.4 px | 0.28 | 1.88 | 8 |
| stroke 22 | 14 % → 17 % | 23.9 px | 0.28 | 1.20 | 8 |
| stroke 23 | 12 % → 17 % | 20.6 px | 0.29 | 1.34 | 9 |
| stroke 24 | 18 % → 26 % | 30.0 px | 0.29 | 1.44 | 6 |
| stroke 25 | 20 % → 34 % | 32.6 px | 0.28 | 1.74 | 7 |
| stroke 26 | 6 % → 14 % | 9.2 px | 0.28 | 2.43 | 13 |
| stroke 27 | 18 % → 26 % | 30.5 px | 0.29 | 1.41 | 11 |
| stroke 28 | 14 % → 24 % | 23.7 px | 0.28 | 1.68 | 6 |
| stroke 29 | 9 % → 27 % | 14.9 px | 0.29 | 3.01 | 11 |
| stroke 30 | 15 % → 36 % | 25.0 px | 0.29 | 2.43 | 7 |
| stroke 31 | 14 % → 17 % | 23.3 px | 0.28 | 1.23 | 12 |
| stroke 32 | 16 % → 29 % | 27.0 px | 0.29 | 1.82 | 8 |
| stroke 33 | 15 % → 16 % | 24.5 px | 0.29 | 1.09 | 6 |
| stroke 34 | 19 % → 27 % | 31.4 px | 0.28 | 1.44 | 7 |
| stroke 35 | 26 % → 36 % | 42.6 px | 0.28 | 1.40 | 13 |
| stroke 36 | 25 % → 34 % | 41.0 px | 0.28 | 1.36 | 8 |
| stroke 37 | 12 % → 12 % | 19.3 px | 0.28 | 1.03 | 8 |
| stroke 38 | 19 % → 25 % | 31.7 px | 0.28 | 1.30 | 10 |
| stroke 39 | 16 % → 22 % | 27.3 px | 0.28 | 1.37 | 9 |
| stroke 40 | 22 % → 31 % | 36.6 px | 0.28 | 1.38 | 13 |
| stroke 41 | 32 % → 36 % | 53.1 px | 0.28 | 1.12 | 7 |
| stroke 42 | 23 % → 30 % | 38.2 px | 0.29 | 1.29 | 6 |
| stroke 43 | 12 % → 12 % | 20.3 px | 0.28 | 1.00 | 8 |
| stroke 44 | 30 % → 37 % | 48.9 px | 0.28 | 1.26 | 11 |
| stroke 45 | 16 % → 16 % | 26.2 px | 0.28 | 1.00 | 8 |
| stroke 46 | 29 % → 34 % | 48.0 px | 0.29 | 1.15 | 11 |
| stroke 47 | 38 % → 41 % | 62.0 px | 0.28 | 1.10 | 9 |
| stroke 48 | 29 % → 36 % | 47.8 px | 0.29 | 1.27 | 6 |
| stroke 49 | 27 % → 30 % | 45.1 px | 0.29 | 1.11 | 9 |
| stroke 50 | 38 % → 40 % | 63.4 px | 0.28 | 1.06 | 12 |
| stroke 51 | 16 % → 16 % | 26.1 px | 0.28 | 1.00 | 7 |
| stroke 52 | 37 % → 38 % | 62.4 px | 0.29 | 1.01 | 9 |
| stroke 53 | 22 % → 26 % | 36.9 px | 0.28 | 1.18 | 6 |
| stroke 54 | 17 % → 19 % | 29.1 px | 0.29 | 1.09 | 10 |
| stroke 55 | 15 % → 15 % | 25.0 px | 0.28 | 1.00 | 11 |
| stroke 56 | 13 % → 14 % | 21.6 px | 0.28 | 1.08 | 7 |
| stroke 57 | 23 % → 23 % | 37.7 px | 0.29 | 1.00 | 6 |
| stroke 58 | 28 % → 29 % | 46.1 px | 0.28 | 1.05 | 11 |
| stroke 59 | 40 % → 40 % | 67.3 px | 0.28 | 1.00 | 8 |
| stroke 60 | 22 % → 22 % | 35.6 px | 0.28 | 1.00 | 6 |

Numbers say: wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #43 Dragged black ink blocks — own sheet
own sheet 600 × 600 · Gouache 1.00 · 70 px · 6.5 s

![Brush Artist · Refs · #43 Dragged black ink blocks — own sheet](Brush-Artist-Refs-43-Dragged-black-ink-blocks-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 15 % → 8 % | 35.8 px | 0.46 | 0.54 | 349 |
| stroke 2 | 18 % → 13 % | 62.1 px | 0.46 | 0.75 | 369 |
| stroke 3 | 19 % → 14 % | 68.8 px | 0.46 | 0.75 | 346 |
| stroke 4 | 19 % → 13 % | 67.6 px | 0.46 | 0.65 | 366 |
| stroke 5 | 26 % → 14 % | 61.7 px | 0.46 | 0.54 | 369 |

## Brush Artist · Refs · #44 Blue looping ribbon — own sheet
own sheet 600 × 600 · Oil 1.00 · 80 px · 4.4 s

![Brush Artist · Refs · #44 Blue looping ribbon — own sheet](Brush-Artist-Refs-44-Blue-looping-ribbon-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 32 % → 32 % | 42.0 px | 0.78 | 1.00 | 2300 |

## Brush Artist · Refs · #45 Soft pastel pepper — own sheet
own sheet 600 × 600 · Pastel 1.00 · 40 px · 4.0 s

![Brush Artist · Refs · #45 Soft pastel pepper — own sheet](Brush-Artist-Refs-45-Soft-pastel-pepper-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 10 % → 39 % | 11.3 px | 0.49 | 3.75 | 310 |
| stroke 2 | 18 % → 34 % | 21.3 px | 0.49 | 1.87 | 298 |
| stroke 3 | 25 % → 37 % | 17.6 px | 0.49 | 1.46 | 249 |
| stroke 4 | 24 % → 35 % | 30.5 px | 0.49 | 1.43 | 293 |
| stroke 5 | 30 % → 30 % | 21.2 px | 0.49 | 1.00 | 196 |
| stroke 6 | 36 % → 44 % | 23.0 px | 0.48 | 1.23 | 287 |
| stroke 7 | 39 % → 43 % | 21.6 px | 0.48 | 1.10 | 303 |
| stroke 8 | 44 % → 44 % | 44.4 px | 0.49 | 1.00 | 282 |

Numbers say: wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #46 Red-brown ink lips — own sheet
own sheet 600 × 600 · Watercolour 1.00 · 50 px · 6.4 s

![Brush Artist · Refs · #46 Red-brown ink lips — own sheet](Brush-Artist-Refs-46-Red-brown-ink-lips-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 13 % → 29 % | 55.7 px | 0.55 | 2.17 | 89 |
| stroke 2 | 18 % → 36 % | 81.1 px | 0.50 | 1.95 | 83 |

Numbers say: wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #47 Pink knife slabs — own sheet
own sheet 600 × 600 · Impasto 1.00 · 90 px · 4.0 s

![Brush Artist · Refs · #47 Pink knife slabs — own sheet](Brush-Artist-Refs-47-Pink-knife-slabs-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 17 % → 32 % | 83.2 px | 0.11 | 1.94 | 268 |
| stroke 2 | 29 % → 43 % | 165.8 px | 0.11 | 1.46 | 265 |
| stroke 3 | 29 % → 43 % | 165.7 px | 0.11 | 1.47 | 266 |
| stroke 4 | 39 % → 38 % | 165.7 px | 0.11 | 0.98 | 262 |

Numbers say: wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #48 Black bands with drips — own sheet
own sheet 600 × 600 · Gouache 1.00 · 70 px · 10.6 s

![Brush Artist · Refs · #48 Black bands with drips — own sheet](Brush-Artist-Refs-48-Black-bands-with-drips-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 28 % → 41 % | 73.2 px | 0.39 | 1.46 | 445 |
| stroke 2 | 43 % → 57 % | 137.5 px | 0.39 | 1.33 | 430 |
| stroke 3 | 45 % → 57 % | 141.4 px | 0.39 | 1.27 | 493 |
| stroke 4 | 48 % → 46 % | 140.3 px | 0.39 | 0.96 | 464 |

## Brush Artist · Refs · #49 Magenta letters round brush — own sheet
own sheet 600 × 600 · Ink 1.00 · 30 px · 8.9 s

![Brush Artist · Refs · #49 Magenta letters round brush — own sheet](Brush-Artist-Refs-49-Magenta-letters-round-brush-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 27 % → 46 % | 64.3 px | 0.52 | 1.70 | 25 |
| stroke 2 | 29 % → 40 % | 52.5 px | 0.53 | 1.40 | 30 |
| stroke 3 | 41 % → 67 % | 96.3 px | 0.52 | 1.64 | 29 |
| stroke 4 | 34 % → 52 % | 53.7 px | 0.52 | 1.55 | 109 |
| stroke 5 | 40 % → 66 % | 94.7 px | 0.52 | 1.65 | 65 |
| stroke 6 | 54 % → 70 % | 231.2 px | 0.52 | 1.29 | 19 |
| stroke 7 | 41 % → 56 % | 63.9 px | 0.52 | 1.35 | 111 |
| stroke 8 | 36 % → 61 % | 91.9 px | 0.53 | 1.73 | 64 |
| stroke 9 | 49 % → 60 % | 152.9 px | 0.53 | 1.24 | 23 |
| stroke 10 | 42 % → 72 % | 100.4 px | 0.52 | 1.71 | 70 |
| stroke 11 | 52 % → 72 % | 219.8 px | 0.52 | 1.39 | 15 |
| stroke 12 | 53 % → 68 % | 82.2 px | 0.52 | 1.29 | 107 |
| stroke 13 | 42 % → 54 % | 115.9 px | 0.53 | 1.29 | 30 |
| stroke 14 | 45 % → 69 % | 131.7 px | 0.53 | 1.52 | 28 |
| stroke 15 | 43 % → 63 % | 102.4 px | 0.52 | 1.46 | 67 |
| stroke 16 | 52 % → 61 % | 220.3 px | 0.52 | 1.18 | 20 |
| stroke 17 | 53 % → 64 % | 82.2 px | 0.52 | 1.19 | 117 |
| stroke 18 | 36 % → 44 % | 99.6 px | 0.52 | 1.22 | 31 |
| stroke 19 | 54 % → 53 % | 123.7 px | 0.52 | 0.99 | 30 |
| stroke 20 | 54 % → 54 % | 125.3 px | 0.52 | 1.00 | 29 |
| stroke 21 | 49 % → 49 % | 81.3 px | 0.52 | 1.00 | 86 |

Numbers say: wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #50 Thick swipes on photo — own sheet
own sheet 600 × 600 · Impasto 1.00 · 40 px · 2.9 s

![Brush Artist · Refs · #50 Thick swipes on photo — own sheet](Brush-Artist-Refs-50-Thick-swipes-on-photo-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 9 % → 21 % | 42.8 px | 0.33 | 2.35 | 36 |
| stroke 2 | 9 % → 16 % | 42.5 px | 0.33 | 1.79 | 25 |
| stroke 3 | 10 % → 11 % | 41.9 px | 0.33 | 1.07 | 46 |
| stroke 4 | 11 % → 18 % | 42.7 px | 0.33 | 1.64 | 30 |
| stroke 5 | 11 % → 10 % | 41.9 px | 0.33 | 0.95 | 36 |
| stroke 6 | 17 % → 21 % | 97.7 px | 0.32 | 1.20 | 24 |
| stroke 7 | 22 % → 26 % | 92.8 px | 0.33 | 1.18 | 40 |
| stroke 8 | 21 % → 21 % | 119.9 px | 0.33 | 0.97 | 33 |
| stroke 9 | 9 % → 10 % | 42.1 px | 0.32 | 1.09 | 35 |
| stroke 10 | 22 % → 21 % | 73.6 px | 0.32 | 0.96 | 40 |
| stroke 11 | 9 % → 8 % | 42.7 px | 0.33 | 0.95 | 33 |
| stroke 12 | 17 % → 16 % | 93.2 px | 0.33 | 0.96 | 18 |

Numbers say: wet paint spreads well beyond the stroke.

## Brush Artist · Ink — dry brush — own sheet
own sheet 600 × 600 · Gouache 1.00 · 30 px · 3.0 s

![Brush Artist · Ink — dry brush — own sheet](Brush-Artist-Ink-dry-brush-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| ear | 6 % → 2 % | 7.0 px | 0.86 | 0.34 | 409 |
| drag0 | 6 % → 9 % | 11.3 px | 0.86 | 1.42 | 107 |
| drag1 | 9 % → 9 % | 18.5 px | 0.86 | 1.02 | 93 |
| drag2 | 11 % → 10 % | 25.6 px | 0.86 | 0.85 | 77 |
| drag3 | 13 % → 10 % | 32.8 px | 0.86 | 0.77 | 69 |

## Brush Artist · Watercolour — blue — own sheet
own sheet 600 × 600 · Watercolour 0.93 · Ink 0.07 · 40 px · 9.3 s

![Brush Artist · Watercolour — blue — own sheet](Brush-Artist-Watercolour-blue-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| s0 | 7 % → 24 % | 28.8 px | 0.30 | 3.32 | 38 |
| s1 | 6 % → 33 % | 10.1 px | 0.37 | 6.00 | 33 |
| s2 | 10 % → 19 % | 44.2 px | 0.26 | 1.81 | 37 |
| s3 | 10 % → 18 % | 26.7 px | 0.31 | 1.92 | 43 |
| s4 | 14 % → 30 % | 38.6 px | 0.36 | 2.16 | 57 |
| s5 | 19 % → 29 % | 39.3 px | 0.37 | 1.54 | 78 |
| s6 | 18 % → 22 % | 48.7 px | 0.31 | 1.25 | 50 |
| s7 | 25 % → 36 % | 32.7 px | 0.37 | 1.46 | 32 |
| s8 | 21 % → 25 % | 79.8 px | 0.30 | 1.20 | 51 |

Numbers say: wet paint spreads well beyond the stroke.

## Brush Artist · Charcoal — stick — own sheet
own sheet 600 × 600 · Charcoal 0.78 · Pastel 0.22 · 28 px · 1.1 s

![Brush Artist · Charcoal — stick — own sheet](Brush-Artist-Charcoal-stick-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| finger0 | 12 % → 25 % | 21.7 px | 0.83 | 2.02 | 36 |
| tip0 | 12 % → 21 % | 33.4 px | 0.83 | 1.69 | 9 |
| finger1 | 23 % → 40 % | 41.1 px | 0.83 | 1.71 | 31 |
| tip1 | 21 % → 29 % | 56.0 px | 0.83 | 1.41 | 16 |
| finger2 | 23 % → 35 % | 41.3 px | 0.83 | 1.53 | 34 |
| tip2 | 21 % → 29 % | 56.0 px | 0.83 | 1.41 | 11 |
| finger3 | 23 % → 27 % | 41.6 px | 0.83 | 1.15 | 30 |
| tip3 | 21 % → 21 % | 56.3 px | 0.83 | 1.00 | 12 |
| cig0 | 33 % → 46 % | 73.2 px | 0.83 | 1.40 | 10 |
| cig1 | 35 % → 46 % | 78.8 px | 0.83 | 1.29 | 14 |
| cig2 | 38 % → 46 % | 84.4 px | 0.83 | 1.21 | 14 |
| cig3 | 40 % → 46 % | 90.0 px | 0.83 | 1.13 | 16 |
| cig4 | 43 % → 45 % | 95.5 px | 0.83 | 1.06 | 14 |
| cig5 | 45 % → 45 % | 101.1 px | 0.83 | 1.00 | 14 |

Numbers say: wet paint spreads well beyond the stroke.

## Oil · Henry Ward · HW #02 cream over wet olive — own sheet
own sheet 600 × 600 · Oil 0.81 · Ink 0.19 · 56 px · 22.7 s

![Oil · Henry Ward · HW #02 cream over wet olive — own sheet](Oil-Henry-Ward-HW-02-cream-over-wet-olive-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 58 % → 100 % | 69.8 px | 0.76 | 1.72 | 1025 |
| stroke 2 | 74 % → 100 % | 136.0 px | 0.74 | 1.35 | 1526 |
| stroke 3 | 76 % → 100 % | 162.6 px | 0.73 | 1.31 | 1416 |
| stroke 4 | 77 % → 100 % | 161.3 px | 0.73 | 1.31 | 1421 |
| stroke 5 | 78 % → 100 % | 162.6 px | 0.73 | 1.29 | 1332 |
| stroke 6 | 77 % → 100 % | 160.7 px | 0.73 | 1.30 | 1247 |
| stroke 7 | 78 % → 100 % | 165.4 px | 0.74 | 1.29 | 1110 |
| stroke 8 | 93 % → 100 % | 166.3 px | 0.75 | 1.08 | 985 |
| stroke 9 | 100 % → 100 % | 116.5 px | 0.77 | 1.00 | 793 |
| stroke 10 | 100 % → 100 % | 395.4 px | 0.74 | 1.00 | 151 |
| stroke 11 | 100 % → 100 % | 407.4 px | 0.73 | 1.00 | 169 |
| stroke 12 | 100 % → 100 % | 441.0 px | 0.74 | 1.00 | 119 |
| stroke 13 | 100 % → 100 % | 394.9 px | 0.74 | 1.00 | 117 |
| stroke 14 | 100 % → 100 % | 360.7 px | 0.74 | 1.00 | 152 |
| stroke 15 | 100 % → 100 % | 372.7 px | 0.73 | 1.00 | 151 |
| stroke 16 | 100 % → 100 % | 500.8 px | 0.72 | 1.00 | 96 |
| stroke 17 | 100 % → 100 % | 355.9 px | 0.73 | 1.00 | 140 |
| stroke 18 | 100 % → 100 % | 392.5 px | 0.72 | 1.00 | 123 |
| stroke 19 | 100 % → 100 % | 466.8 px | 0.73 | 1.00 | 103 |
| stroke 20 | 100 % → 100 % | 388.1 px | 0.74 | 1.00 | 133 |
| stroke 21 | 100 % → 100 % | 358.2 px | 0.74 | 1.00 | 157 |
| stroke 22 | 100 % → 100 % | 335.1 px | 0.74 | 1.00 | 170 |
| stroke 23 | 100 % → 100 % | 359.4 px | 0.73 | 1.00 | 161 |
| stroke 24 | 100 % → 100 % | 438.6 px | 0.73 | 1.00 | 112 |
| stroke 25 | 100 % → 100 % | 380.0 px | 0.73 | 1.00 | 169 |
| stroke 26 | 100 % → 100 % | 415.5 px | 0.74 | 1.00 | 148 |

Numbers say: wet paint spreads well beyond the stroke.

## Oil · Henry Ward · HW #04 grey arcs over ochre — own sheet
own sheet 600 × 600 · Oil 1.00 · 46 px · 17.3 s

![Oil · Henry Ward · HW #04 grey arcs over ochre — own sheet](Oil-Henry-Ward-HW-04-grey-arcs-over-ochre-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 69 % → 39 % | 75.0 px | 0.24 | 0.57 | 1256 |
| stroke 2 | 83 % → 54 % | 136.2 px | 0.25 | 0.66 | 1395 |
| stroke 3 | 84 % → 78 % | 148.9 px | 0.25 | 0.92 | 1421 |
| stroke 4 | 84 % → 62 % | 147.6 px | 0.25 | 0.74 | 1322 |
| stroke 5 | 84 % → 46 % | 146.6 px | 0.21 | 0.55 | 1163 |
| stroke 6 | 81 % → 32 % | 143.7 px | 0.17 | 0.39 | 1215 |
| stroke 7 | 83 % → 37 % | 148.0 px | 0.16 | 0.45 | 973 |
| stroke 8 | 86 % → 30 % | 143.3 px | 0.16 | 0.34 | 1001 |
| stroke 9 | 100 % → 25 % | 104.1 px | 0.16 | 0.25 | 785 |
| stroke 10 | 10 % → 69 % | 37.6 px | 0.25 | 6.87 | 159 |
| stroke 11 | 17 % → 58 % | 59.7 px | 0.24 | 3.36 | 193 |
| stroke 12 | 21 % → 56 % | 78.2 px | 0.22 | 2.75 | 115 |
| stroke 13 | 33 % → 67 % | 92.0 px | 0.25 | 2.01 | 230 |
| stroke 14 | 38 % → 65 % | 145.1 px | 0.24 | 1.74 | 166 |
| stroke 15 | 38 % → 59 % | 131.9 px | 0.25 | 1.54 | 230 |
| stroke 16 | 44 % → 60 % | 163.4 px | 0.24 | 1.37 | 133 |
| stroke 17 | 49 % → 66 % | 182.5 px | 0.25 | 1.35 | 200 |
| stroke 18 | 49 % → 61 % | 169.5 px | 0.24 | 1.23 | 155 |
| stroke 19 | 55 % → 68 % | 181.2 px | 0.25 | 1.24 | 215 |
| stroke 20 | 58 % → 72 % | 178.6 px | 0.25 | 1.25 | 209 |
| stroke 21 | 61 % → 76 % | 198.6 px | 0.25 | 1.23 | 179 |
| stroke 22 | 34 % → 56 % | 125.1 px | 0.22 | 1.62 | 164 |
| stroke 23 | 57 % → 67 % | 209.1 px | 0.24 | 1.17 | 217 |
| stroke 24 | 75 % → 79 % | 286.6 px | 0.25 | 1.06 | 138 |
| stroke 25 | 55 % → 66 % | 188.1 px | 0.23 | 1.21 | 195 |
| stroke 26 | 73 % → 77 % | 255.3 px | 0.24 | 1.04 | 153 |
| stroke 27 | 27 % → 36 % | 83.8 px | 0.18 | 1.32 | 152 |
| stroke 28 | 27 % → 45 % | 95.0 px | 0.16 | 1.69 | 133 |
| stroke 29 | 25 % → 35 % | 103.3 px | 0.16 | 1.37 | 97 |
| stroke 30 | 32 % → 32 % | 95.9 px | 0.16 | 1.00 | 143 |

Numbers say: wet paint spreads well beyond the stroke.

## Oil · Henry Ward · HW #09 white arches over wet blue-grey — own sheet
own sheet 600 × 600 · Oil 1.00 · 46 px · 24.2 s

![Oil · Henry Ward · HW #09 white arches over wet blue-grey — own sheet](Oil-Henry-Ward-HW-09-white-arches-over-wet-blue-grey-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 72 % → 100 % | 73.7 px | 0.22 | 1.39 | 1126 |
| stroke 2 | 82 % → 100 % | 134.8 px | 0.22 | 1.22 | 1469 |
| stroke 3 | 83 % → 100 % | 148.5 px | 0.22 | 1.20 | 1482 |
| stroke 4 | 84 % → 100 % | 150.1 px | 0.22 | 1.19 | 1300 |
| stroke 5 | 82 % → 100 % | 144.6 px | 0.21 | 1.23 | 1287 |
| stroke 6 | 83 % → 100 % | 142.5 px | 0.22 | 1.21 | 1142 |
| stroke 7 | 83 % → 100 % | 145.4 px | 0.23 | 1.21 | 1018 |
| stroke 8 | 85 % → 100 % | 144.8 px | 0.24 | 1.18 | 1016 |
| stroke 9 | 100 % → 100 % | 99.7 px | 0.26 | 1.00 | 764 |
| stroke 10 | 100 % → 100 % | 396.0 px | 0.23 | 1.00 | 197 |
| stroke 11 | 100 % → 100 % | 185.6 px | 0.23 | 1.00 | 272 |
| stroke 12 | 100 % → 100 % | 180.6 px | 0.23 | 1.00 | 329 |
| stroke 13 | 100 % → 100 % | 222.3 px | 0.23 | 1.00 | 202 |
| stroke 14 | 100 % → 100 % | 72.0 px | 0.24 | 1.00 | 366 |
| stroke 15 | 100 % → 100 % | 279.7 px | 0.23 | 1.00 | 244 |
| stroke 16 | 100 % → 100 % | 300.3 px | 0.23 | 1.00 | 181 |
| stroke 17 | 100 % → 100 % | 287.9 px | 0.23 | 1.00 | 180 |
| stroke 18 | 100 % → 100 % | 272.1 px | 0.23 | 1.00 | 244 |
| stroke 19 | 100 % → 100 % | 306.6 px | 0.23 | 1.00 | 222 |
| stroke 20 | 100 % → 100 % | 260.1 px | 0.23 | 1.00 | 256 |
| stroke 21 | 100 % → 100 % | 255.2 px | 0.22 | 1.00 | 188 |
| stroke 22 | 100 % → 100 % | 268.4 px | 0.22 | 1.00 | 220 |
| stroke 23 | 100 % → 100 % | 315.9 px | 0.23 | 1.00 | 250 |
| stroke 24 | 100 % → 100 % | 320.9 px | 0.22 | 1.00 | 127 |
| stroke 25 | 100 % → 100 % | 282.2 px | 0.23 | 1.00 | 162 |
| stroke 26 | 100 % → 100 % | 384.9 px | 0.24 | 1.00 | 96 |
| stroke 27 | 100 % → 100 % | 243.6 px | 0.24 | 1.00 | 168 |
| stroke 28 | 100 % → 100 % | 232.2 px | 0.25 | 1.00 | 128 |

## Oil · Henry Ward · HW #03 navy contours over wet band — own sheet
own sheet 600 × 600 · Oil 1.00 · 46 px · 19.2 s

![Oil · Henry Ward · HW #03 navy contours over wet band — own sheet](Oil-Henry-Ward-HW-03-navy-contours-over-wet-band-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 70 % → 100 % | 71.0 px | 0.22 | 1.43 | 1037 |
| stroke 2 | 83 % → 100 % | 139.1 px | 0.24 | 1.21 | 1374 |
| stroke 3 | 82 % → 100 % | 144.1 px | 0.25 | 1.22 | 1437 |
| stroke 4 | 82 % → 100 % | 143.7 px | 0.28 | 1.22 | 1285 |
| stroke 5 | 81 % → 100 % | 144.1 px | 0.26 | 1.23 | 1259 |
| stroke 6 | 84 % → 100 % | 147.3 px | 0.24 | 1.19 | 1027 |
| stroke 7 | 83 % → 100 % | 143.4 px | 0.19 | 1.20 | 960 |
| stroke 8 | 85 % → 100 % | 144.2 px | 0.15 | 1.17 | 960 |
| stroke 9 | 100 % → 100 % | 104.1 px | 0.12 | 1.00 | 773 |
| stroke 10 | 100 % → 100 % | 419.6 px | 0.27 | 1.00 | 70 |
| stroke 11 | 100 % → 100 % | 378.7 px | 0.30 | 1.00 | 92 |
| stroke 12 | 100 % → 100 % | 358.9 px | 0.26 | 1.00 | 99 |
| stroke 13 | 100 % → 100 % | 345.8 px | 0.26 | 1.00 | 112 |
| stroke 14 | 100 % → 100 % | 326.3 px | 0.30 | 1.00 | 44 |
| stroke 15 | 100 % → 100 % | 358.8 px | 0.30 | 1.00 | 66 |
| stroke 16 | 100 % → 100 % | 226.3 px | 0.23 | 1.00 | 266 |
| stroke 17 | 100 % → 100 % | 260.3 px | 0.25 | 1.00 | 184 |

